#!/usr/bin/env python3
"""PROPOSAL-p driver (p v0.2 §4.2, §8 steps 4-5; the design seat's answers of 2026-11-07, Q0-Q4).

p's own driver (p §4.2: "drivers scripts/p_sessions.py and scripts/p_analyze.py"; scripts/m_sessions.py is
untouched). At the p BUILD (p §8 step 4) it wires:

  --selftest          every valence_core.p module's model-free self-test, then this driver's integration checks;
                      "  N/N p selftest checks pass", exit 0 iff all pass. Safe on the box: the gcal cases run with
                      the canonical roots pointed at a scratch root and the loader trapped -- the refusal case with
                      the pod id removed, the wiring case with a stand-in pod id and stand-ins for G-CAL-p's precheck,
                      the weights check and G-CAL-p's run, and the OLMo adapter module a stand-in -- so no self-test
                      can load a model or write a record.
  --build-schedules   p's schedule files and manifest (data/p/schedules; --out a test directory, never inside the repo);
                      an existing differing file is refused, never overwritten.
  hashes              the licence (p §4.2, C2's form): p's package_sha256, each imported valence_core.m module's
                      file sha256 and valence_core/adapters/olmo_hf.py's, each by name on one line; the substitution
                      register; the schedules' manifest sha256.
  gshape              G-SHAPE-p (p §4.2), model-free; the canonical artifact data/p/gates/G-SHAPE-p.json needs
                      every source committed at HEAD and unedited; --out a test directory (never inside the repo).
  gcal --unit OLMo-{ckpt} [--resume]
                      G-CAL-p-{ckpt} (p §3), on the box only, on the PI's go for the box (p §8 step 5). Before the
                      load: G-CAL-p's precheck (the unit, the paths with no link on the way, the proposal, an
                      existing checkpoint or artifact, the renders, the reference artifact, the seat's read of record,
                      the generation call's pin, §3.2's conditions, the weights of record, the pod id, the gate line,
                      the code of record committed, this driver among it) and the weights files on this box (each
                      listed file a regular file at the manifest's byte count, nothing unlisted); then the DRIVER and
                      WEIGHTS lines; then, in G-CAL-p's run and still before the load, the key set, f0's honesty
                      asserts and, on a --resume, the checkpoint's validity, every identity field the adapter does not
                      give, and the pod change; then the OLMo adapter
                      at the manifest's path with runner_olmo's declared read window, wrapped in §2.2's proxy. After
                      the load and before any generation: m's startup and the comparison of the two identity fields
                      the loaded adapter gives (the backend identifier, the ban ids).
                      Exit 0 PASS; 4 FAIL (that checkpoint NOT-RUN, cause dose-not-completable, escalated) or STOP;
                      2 refused.

and refuses ``time``, ``qual`` and ``campaign`` (G-TIME-OLMo (p), G-F0m-OLMo (p), the campaign): p §8 step 6 wires
them after scripts/p_analyze.py, G-ANL-p and each checkpoint's LOCK-p v0.1, on their own word.

PIN (Code, declared at the p BUILD): the weights-files check is p's own, written to scripts/m_sessions.py's
``olmo_weights_problems`` semantics (a size check, never a re-hash -- the respawn protocol's step (i) re-hashes the
volume once per box), so p's licence binds no m script. A refusal exits 2; any other STOP raised on the way (a
register or keys STOP among them) exits 4, named.

INVOCATION is the first line of every run. Nothing but ``gcal`` loads a model.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib
import io
import json
import os
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from valence_core.m import gcal as m_gcal  # noqa: E402
from valence_core.m import resume as m_resume  # noqa: E402
from valence_core.m import stages as m_stages  # noqa: E402
from valence_core.p import gcal, gshape, guard, register, schedule  # noqa: E402

DRIVER_REL = "scripts/p_sessions.py"
#: Every p module with a self-test, in dependency order (the package marker and the test double have none).
MODULES = ("register", "corrupt", "keys", "schedule", "proxy", "report", "guard", "gcal", "gshape")
STAGE_CMDS = ("time", "qual", "campaign")
STAGE_NAMES = {"time": "G-TIME-OLMo (p)", "qual": "G-F0m-OLMo (p)", "campaign": "the PROPOSAL-p campaign"}
GCAL_EXIT = {"PASS": 0, "FAIL": 4}


def refusal(cmd: str) -> str:
    return (f"REFUSED: {cmd} ({STAGE_NAMES[cmd]}) is not wired at the p BUILD -- p §8 step 6 wires each stage after "
            f"scripts/p_analyze.py, G-ANL-p and its checkpoint's LOCK-p v0.1, on its own word")


def build_schedules(out: str | None) -> int:
    try:
        shas = schedule.write_schedule_files(out)
    except (RuntimeError, schedule.ScheduleRefusal, OSError) as e:
        print(f"REFUSED: {e}", flush=True)
        return 2
    except SystemExit as e:
        print(f"STOP: {e}", flush=True)
        return 4
    d = Path(out) if out is not None else schedule.DEFAULT_OUT
    probs = schedule.verify_schedule_dir(d)
    print(f"SCHEDULES {d}: {len(shas)} files (manifest included); verify {'clean' if not probs else probs[:3]}; "
          f"manifest sha256 {shas[schedule.MANIFEST_NAME]}", flush=True)
    return 0 if not probs else 4


def hashes() -> int:
    for ln in guard.licence_lines():
        print(ln, flush=True)
    for e in register.table():
        print("REGISTER " + json.dumps(e, sort_keys=True, ensure_ascii=False), flush=True)
    man = schedule.DEFAULT_OUT / schedule.MANIFEST_NAME
    print(f"SCHEDULES MANIFEST {man.relative_to(REPO)} sha256 "
          f"{hashlib.sha256(man.read_bytes()).hexdigest() if man.is_file() else 'ABSENT'}", flush=True)
    return 0


def run_gshape(out: str | None) -> int:
    try:
        res = gshape.write(out)
    except gshape.GshapePRefusal as e:
        print(str(e), flush=True)
        return 2
    except OSError as e:
        print(f"REFUSED: G-SHAPE-p's output path: {type(e).__name__}: {e}", flush=True)
        return 2
    except SystemExit as e:
        print(f"STOP: {e}", flush=True)
        return 4
    for ln in gshape.summary_lines(res):
        print(ln, flush=True)
    return gshape.EXIT[res["artifact"]["verdict"]]


def weights_files_problems(ckpt: str, w: dict, *, models_root: str | os.PathLike | None = None,
                           files: dict | None = None) -> list[str]:
    """[] iff every file the committed manifest lists for ``ckpt`` is a regular file at its byte count under the
    entry's path, and the directory holds no unlisted file (``models_root`` and ``files`` are the self-test's
    seams: a scratch root, and the manifest's names at small byte counts; ``run_gcal`` passes neither)."""
    try:
        if files is None:
            _cp, data = m_stages._committed(m_gcal.MANIFEST_REL)
            files = json.loads(data.decode("utf-8"))[ckpt]["files"]
        sizes = {str(k): v["bytes"] for k, v in files.items()}
        if any(type(v) is not int or v < 0 for v in sizes.values()):
            raise TypeError("a byte count that is not a non-negative int")
    except (ValueError, UnicodeDecodeError, KeyError, TypeError, AttributeError) as e:
        return [f"{m_gcal.MANIFEST_REL}[{ckpt}].files: malformed ({type(e).__name__}: {e})"]
    if len(sizes) != w["n_files"]:
        return [f"{m_gcal.MANIFEST_REL}[{ckpt}]: files lists {len(sizes)} entries, n_files {w['n_files']}"]
    root = Path(w["path"]) if models_root is None else Path(models_root) / ckpt
    if root.is_symlink() or not root.is_dir():
        return [f"weights path {root}: not a directory on this box"]
    try:
        extra = sorted(set(os.listdir(root)) - set(sizes))
    except OSError as e:
        return [f"weights path {root}: unreadable ({type(e).__name__})"]
    out = [f"{root}: files the manifest does not list: {extra[:5]}"] if extra else []
    for name in sorted(sizes):
        p = root / name
        try:
            if p.is_symlink() or not p.is_file():
                out.append(f"{p}: not a regular file")
            elif p.stat().st_size != sizes[name]:
                out.append(f"{p}: {p.stat().st_size} bytes, the manifest's {sizes[name]}")
        except OSError as e:
            out.append(f"{p}: unreadable ({type(e).__name__})")
    return out


def _load_olmo(path: str):
    from valence_core.adapters.olmo_hf import OLMoHFAdapter
    from valence_core.m import runner_olmo
    return OLMoHFAdapter(path, choice_window=runner_olmo.CHOICE_WINDOW)


def run_gcal(unit: str, resume: bool) -> int:
    """G-CAL-p on one checkpoint, on the box (the docstring's order of refusals)."""
    try:
        pre = gcal.precheck(unit, stub=False, resume=resume)
    except gcal.GcalPRefusal as e:
        print(f"REFUSED: {e}; nothing loaded", file=sys.stderr, flush=True)
        return 2
    except SystemExit as e:
        print(f"STOP: {e}; nothing loaded", file=sys.stderr, flush=True)
        return 4
    ck, w = pre["ckpt"], pre["weights"]
    wp = weights_files_problems(ck, w)
    if wp:
        print(f"REFUSED: {gcal.stage_label(unit)}: weights: {wp}; nothing loaded", file=sys.stderr, flush=True)
        return 2
    print(f"DRIVER {DRIVER_REL} {guard.driver_sha256()}: committed at HEAD {m_stages._git_head()}, working tree "
          f"identical (G-CAL-p's precheck)", flush=True)
    print(f"WEIGHTS {ck}: {w['repo']} revision {w['revision']}, files_aggregate_sha256 {w['sha256']}; {w['n_files']} "
          f"files at {w['path']}, each at the manifest's byte count (the full re-hash is the respawn protocol's step "
          f"(i), in this box's BACKEND entry)", flush=True)
    try:
        res = gcal.run(lambda: _load_olmo(w["path"]), unit, stub=False, resume=resume)
    except gcal.GcalPRefusal as e:
        print(f"REFUSED: {e}", file=sys.stderr, flush=True)
        return 2
    except SystemExit as e:
        print(f"STOP: {e}", file=sys.stderr, flush=True)
        return 4
    return GCAL_EXIT[res["verdict"]]


def _short(x, n: int = 160) -> str:
    s = x if isinstance(x, str) else repr(x)
    return s if len(s) <= n else s[:n] + "..."


def _selftest(chk) -> None:
    """The driver's integration checks (model-free; safe on the box)."""
    from unittest import mock
    me = sys.modules[__name__]
    pkg = sorted(p.stem for p in guard.PACKAGE_DIR.glob("*.py") if p.stem not in ("__init__", "testing"))
    chk("p_sessions: MODULES lists every p module but the package marker and the test double",
        sorted(MODULES) == pkg, sorted(set(pkg) ^ set(MODULES)))

    def run(argv):
        buf, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
            try:
                rc = main(argv)
            except SystemExit as e:
                rc = e.code if isinstance(e.code, int) else 2
        return rc, buf.getvalue() + err.getvalue()

    with tempfile.TemporaryDirectory() as td:
        rc1, out1 = run(["--build-schedules", "--out", str(Path(td) / "s")])
        rc2, out2 = run(["--build-schedules", "--out", str(Path(td) / "s")])
        first = sorted((Path(td) / "s").glob("*.json"))[0]
        first.write_text("{}")
        rc3, out3 = run(["--build-schedules", "--out", str(Path(td) / "s")])
        rc4, out4 = run(["--build-schedules", "--out", str(REPO / "data" / "p" / "schedules")])
        rcg, outg = run(["gshape", "--out", str(Path(td) / "g")])
    chk("p_sessions: --build-schedules writes 19 files that verify clean, re-runs identically, and refuses a "
        "differing existing file and a test directory inside the repository (exit 2)",
        rc1 == 0 and "19 files" in out1 and "verify clean" in out1 and rc2 == 0 and rc3 == 2
        and "SCHEDULE MISMATCH" in out3 and rc4 == 2, (rc1, rc2, rc3, rc4, out1[-160:]))
    committed = schedule.verify_schedule_dir()
    chk("p_sessions: data/p/schedules equals a fresh regeneration byte for byte, manifest included (18 + 1)",
        committed == [] and len(list(schedule.DEFAULT_OUT.glob("*.json"))) == 19, committed[:3])
    chk("p_sessions: gshape --out runs G-SHAPE-p as an --out run -- PASS; INVOCATION is the first line",
        rcg == 0 and outg.startswith("INVOCATION: ") and "G-SHAPE-p: PASS" in outg and "never of record" in outg,
        outg[-300:])
    refused = {c: run([c]) for c in STAGE_CMDS}
    chk("p_sessions: time, qual and campaign are refused at the p BUILD (exit 2), each named",
        all(rc == 2 and refusal(c) in out for c, (rc, out) in refused.items()), {c: rc for c, (rc, _) in refused.items()})
    rc0, out0 = run([])
    chk("p_sessions: no action is refused (exit 2) and INVOCATION is the first line",
        rc0 == 2 and out0.startswith("INVOCATION: "))
    rch, outh = run(["hashes"])
    chk("p_sessions: hashes prints p's package sha256, the seventeen m files' (sixteen modules and __init__.py), "
        "olmo_hf.py's and the register's four entries",
        rch == 0 and f"LICENCE valence_core/p package_sha256 {guard.package_sha256()}" in outh
        and outh.count("LICENCE valence_core/m/") == len(guard.M_HASHED) == 17
        and f"LICENCE {guard.OLMO_HF_REL} sha256 {guard.olmo_hf_sha256()}" in outh
        and outh.count("REGISTER ") == len(register.ENTRIES) == 4, outh[-300:])

    trapped: list = []

    def trap(path):
        trapped.append(path)
        raise AssertionError("the self-test reached the OLMo loader")

    class _NoAdapter:
        def __init__(self, *a, **kw):
            trapped.append(("OLMoHFAdapter", a))
            raise AssertionError("the self-test constructed an OLMo adapter")

    fake_hf = type(sys)("valence_core.adapters.olmo_hf")
    fake_hf.OLMoHFAdapter = _NoAdapter
    env_no_pod = {k: v for k, v in os.environ.items() if k != m_resume.POD_ENV}
    loaded_before = "valence_core.adapters.olmo_hf" in sys.modules
    real_hf = sys.modules.get("valence_core.adapters.olmo_hf")
    with tempfile.TemporaryDirectory() as td, mock.patch.dict(os.environ, env_no_pod, clear=True), \
            mock.patch.object(gcal, "GATES_DIR", Path(td) / "gates"), \
            mock.patch.object(gcal, "CKPT_DIR", Path(td) / "ckpt"), mock.patch.object(me, "_load_olmo", trap):
        gc = {u: run(["gcal", "--unit", u]) for u in ("OLMo-sft", "Q-F0", "OLMo-base")}
    chk("p_sessions: gcal is refused before any load in every state of the record (the pod id removed, the canonical "
        "roots a scratch root, the loader trapped) -- POD ID ABSENT for OLMo-sft, and Q-F0 and the base checkpoint "
        "refused (exit 2); the loader never reached, the OLMo adapter module never imported",
        all(rc == 2 and "REFUSED" in out for rc, out in gc.values()) and "POD ID ABSENT" in gc["OLMo-sft"][1]
        and trapped == [] and ("valence_core.adapters.olmo_hf" in sys.modules) == loaded_before,
        {u: (rc, _short(o, 120)) for u, (rc, o) in gc.items()})
    seen: list = []

    def recorder(factory, unit, **kw):
        seen.append((unit, kw))
        return {"verdict": "PASS"}

    env_box = dict(env_no_pod, **{m_resume.POD_ENV: "selftest-pod"})
    w_sft = {"repo": "selftest/olmo", "revision": "0" * 12, "sha256": "0" * 64, "path": "/workspace/models/sft",
             "n_files": 3}                          # a literal stand-in: no record file is read (R3-1)
    with tempfile.TemporaryDirectory() as td, mock.patch.dict(os.environ, env_box, clear=True), \
            mock.patch.dict(sys.modules, {"valence_core.adapters.olmo_hf": fake_hf}), \
            mock.patch.object(gcal, "GATES_DIR", Path(td) / "gates"), \
            mock.patch.object(gcal, "CKPT_DIR", Path(td) / "ckpt"), \
            mock.patch.object(gcal, "precheck", lambda unit, **kw: {"ckpt": "sft", "weights": w_sft}), \
            mock.patch.object(me, "weights_files_problems", lambda ck, w, **kw: []), \
            mock.patch.object(gcal, "run", recorder), mock.patch.object(me, "_load_olmo", trap):
        rcb, outb = run(["gcal", "--unit", "OLMo-sft"])
    restored = sys.modules.get("valence_core.adapters.olmo_hf") is real_hf
    di, wi = outb.find("DRIVER scripts/p_sessions.py "), outb.find("WEIGHTS sft: ")
    chk("p_sessions: on a simulated clear box (a pod id; G-CAL-p's precheck and the weights check passing as "
        "stand-ins, so no state of the record matters; G-CAL-p's run replaced by a recorder, the loader trapped, the "
        "OLMo adapter module a stand-in that refuses construction) "
        "the driver prints the DRIVER then the WEIGHTS line and calls G-CAL-p's run once, canonical (stub false, "
        "resume false); no adapter is made and sys.modules is restored",
        rcb == 0 and 0 <= di < wi and seen == [("OLMo-sft", {"stub": False, "resume": False})] and trapped == []
        and restored, (rcb, di, wi, seen, trapped, _short(outb, 200)))
    names = ["config.json", "model-00001-of-00002.safetensors", "model-00002-of-00002.safetensors",
             "tokenizer.json"]                      # literal stand-ins: no record file is read (R3-1)
    w = {"repo": "selftest/olmo", "revision": "0" * 12, "sha256": "0" * 64, "path": "/nonexistent/sft",
         "n_files": len(names)}
    with tempfile.TemporaryDirectory() as td:
        files = {n: {"bytes": k + 1} for k, n in enumerate(names)}
        root = Path(td) / "sft"
        root.mkdir()
        miss = weights_files_problems("sft", w, models_root=td, files=files)
        for n, v in files.items():
            (root / n).write_bytes(b"x" * v["bytes"])
        clean = weights_files_problems("sft", w, models_root=td, files=files)
        (root / names[0]).write_bytes(b"")
        short = weights_files_problems("sft", w, models_root=td, files=files)
        (root / names[0]).write_bytes(b"x")
        (root / "adapter_config.json").write_text("{}")
        extra = weights_files_problems("sft", w, models_root=td, files=files)
    chk("p_sessions: the weights-files check (literal file names at small byte counts) refuses missing files, a wrong "
        "byte count and an unlisted file, and passes the files at their counts",
        len(miss) == len(files) and clean == [] and len(short) == 1 and len(extra) == 1,
        (len(miss), clean[:2], short[:1], extra[:1]))
    ip = guard.import_problems(runtime=True)
    chk("p_sessions: the licence's import set holds, and term (e)'s static check is clean over p and this driver",
        ip == [], ip[:2])
    chk("p_sessions: the quarantined state-present module is not loaded after the self-test",
        not any(m in sys.modules for m in guard.FORBIDDEN_MODULES))


def run_selftest() -> int:
    results: list[bool] = []

    def chk(name, ok, got="", note="", *rest) -> None:
        ok = bool(ok)
        results.append(ok)
        tail = " ".join(_short(x) for x in (got, note, *rest) if x is not None and not (isinstance(x, str) and x == ""))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" {tail}" if tail and not ok else ""), flush=True)

    for m in MODULES:
        mod = importlib.import_module(f"valence_core.p.{m}")
        try:
            mod._selftest(chk)
        except (Exception, SystemExit) as e:                    # noqa: BLE001
            chk(f"{m}: _selftest raised", False, f"{type(e).__name__}: {e}")
    try:
        _selftest(chk)
    except (Exception, SystemExit) as e:                        # noqa: BLE001
        chk("p_sessions: integration selftest raised", False, f"{type(e).__name__}: {e}")
    print(f"  {sum(results)}/{len(results)} p selftest checks pass", flush=True)
    return 0 if all(results) else 1


def main(argv: list[str] | None = None) -> int:
    shown = sys.argv if argv is None else [sys.argv[0]] + list(argv)
    print("INVOCATION: " + " ".join([sys.executable] + shown), flush=True)
    ap = argparse.ArgumentParser(description="PROPOSAL-p driver (self-test, schedules, hashes, G-SHAPE-p, G-CAL-p; "
                                             "the stage subcommands are refused at the p BUILD)")
    ap.add_argument("--selftest", action="store_true", help="model-free self-test of valence_core.p")
    ap.add_argument("--build-schedules", action="store_true", help="write p's schedule files + manifest")
    ap.add_argument("--out", default=None, help="a test directory for --build-schedules (never inside the repository)")
    sub = ap.add_subparsers(dest="cmd")
    g = sub.add_parser("gshape", help="G-SHAPE-p (p §4.2), model-free; canonical without --out")
    g.add_argument("--out", dest="gshape_out", default=None, help="a test directory (never of record; never inside the repo)")
    sub.add_parser("hashes", help="the licence lines, the register and the schedules' manifest")
    c = sub.add_parser("gcal", help="G-CAL-p (p §3) on one checkpoint; the box only, on the PI's go")
    c.add_argument("--unit", required=True, help="OLMo-sft, OLMo-dpo or OLMo-instruct")
    c.add_argument("--resume", action="store_true", help="continue the unit's checkpoint (skip-only)")
    for s in STAGE_CMDS:
        sub.add_parser(s, help=f"{STAGE_NAMES[s]}: refused at the p BUILD (p §8 step 6)")
    try:
        a = ap.parse_args(argv)
    except SystemExit as e:
        return int(e.code) if isinstance(e.code, int) else 2
    if a.selftest:
        return run_selftest()
    if a.build_schedules:
        return build_schedules(a.out)
    if a.cmd == "gshape":
        return run_gshape(a.gshape_out)
    if a.cmd == "hashes":
        return hashes()
    if a.cmd == "gcal":
        return run_gcal(a.unit, a.resume)
    if a.cmd in STAGE_CMDS:
        print(refusal(a.cmd), flush=True)
        return 2
    print("REFUSED: no action (--selftest, --build-schedules, hashes, gshape or gcal)", flush=True)
    return 2


if __name__ == "__main__":
    sys.exit(main())
