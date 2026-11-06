#!/usr/bin/env python3
"""PROPOSAL-m Q-F3 driver (v1.11 §3.2 m:288-298, §8 step 19 m:361; ADDENDUM-m1 §4 step 5; the design seat's
prebuild answers of 2026-11-06, Q1 (C2) and Q6).

Q-F3's own driver (Q1: "A new driver, scripts/mf3_sessions.py"; scripts/m_sessions.py is untouched). At the
F3 build it wires:

  --selftest          every valence_core.mf3 module's model-free self-test, then this driver's integration
                      checks; "  N/N mf3 selftest checks pass", exit 0 iff all pass.
  --build-schedules   Q-F3's schedule files and manifest (default data/mf3/schedules; --out a test
                      directory); an existing differing file is refused, never overwritten.
  hashes              what LOCK-m-F3 v0.1 names (Q1 (C2)): mf3's package_sha256, each imported
                      valence_core.m module's file sha256, the schedules' manifest sha256, the weights
                      binding of record (the hub cache's snapshot; nothing loaded).
  gshape              G-SHAPE-F3 (m:290), model-free; the canonical artifact data/mf3/gates/G-SHAPE-F3.json
                      needs every source committed at HEAD and unedited; --out a test directory.

and refuses ``time``, ``id``, ``qual`` and ``campaign`` (G-TIME-F3, G-ID-F3, G-F3, the campaign): each is
wired at its own step, on its own word, after its lock (m:361; the OLMo build's PIN O12 form). The stage
drivers they will call are built and stub-tested in valence_core.mf3.stages.

Q6's forms (the seat: "scripts/mf3_sessions.py is written to the same forms from the start"): the
CHECKPOINT STATE INCONSISTENT line is valence_core.m.resume's sealed form, imported by mf3.resume; the
campaign-ruling refusals O4-1 (RULING BESIDE AN END PENDING), O1-3 (RULING REUSED), RM4-1's RULING-line note
and the VC4-1 / VC4-2 help and docstring sentences are the campaign subcommand's, written in
scripts/m_sessions.py's forms when that subcommand is wired; O2-3's listing forms (a bare git status
--porcelain, a name-only ls, git ls-files, git diff --name-status, shasum; no size or time metadata of
data/mf3/ckpt or data/mf3/reports) go into Q-F3's launch checklist until its VERDICTS.

INVOCATION is the first line of every run. Nothing here loads a model.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib
import io
import json
import re
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from valence_core.mf3 import gshape, guard, keys, schedule  # noqa: E402
from valence_core.mf3 import resume as rs  # noqa: E402

DRIVER_REL = "scripts/mf3_sessions.py"
#: Every mf3 module with a self-test, in dependency order (the test double has none).
MODULES = ("keys", "banner", "schedule", "lines", "scaffold", "guard", "runner", "verify", "readrule", "bars",
           "resume", "stages", "gshape")
STAGE_CMDS = ("time", "id", "qual", "campaign")
STAGE_NAMES = {"time": "G-TIME-F3", "id": "G-ID-F3", "qual": "G-F3", "campaign": "the Q-F3 campaign"}


def refusal(cmd: str) -> str:
    return (f"REFUSED: {cmd} ({STAGE_NAMES[cmd]}) is not wired at the F3 build -- each Q-F3 stage subcommand is "
            f"wired at its own step, on its own word, after its lock (m:361); its driver is built and stub-tested "
            f"in valence_core.mf3.stages")


def build_schedules(out: str | None) -> int:
    try:
        shas = schedule.write_schedule_files(out)
    except RuntimeError as e:
        print(f"REFUSED: {e}", flush=True)
        return 2
    d = Path(out) if out is not None else schedule.DEFAULT_OUT
    probs = schedule.verify_schedule_dir(d)
    print(f"SCHEDULES {d}: {len(shas)} files (manifest included); verify {'clean' if not probs else probs[:3]}; "
          f"manifest sha256 {shas[schedule.MANIFEST_NAME]}", flush=True)
    return 0 if not probs else 4


def hashes(snapshot_dir: str | None = None) -> int:
    print(f"MF3 PACKAGE sha256 {guard.package_sha256_of(guard.PACKAGE_DIR)} ({len(list(guard.PACKAGE_DIR.glob('*.py')))} "
          f"files, valence_core/mf3/*.py)", flush=True)
    for m, v in guard.m_module_sha256s().items():
        print(f"M MODULE valence_core/m/{m}.py sha256 {v}", flush=True)
    man = schedule.DEFAULT_OUT / schedule.MANIFEST_NAME
    print(f"SCHEDULES MANIFEST {man.relative_to(REPO)} sha256 "
          f"{hashlib.sha256(man.read_bytes()).hexdigest() if man.is_file() else 'ABSENT'}", flush=True)
    try:
        wb = rs.weights_binding(snapshot_dir or rs.hub_repo_dir() / "snapshots" / gshape.QWEN_REVISION)
        print(f"WEIGHTS {gshape.QWEN_MODEL_ID} revision {wb['revision']} sha256 {wb['sha256']}", flush=True)
    except (OSError, ValueError, KeyError) as e:
        print(f"WEIGHTS unreadable ({type(e).__name__})", flush=True)
        return 4
    return 0


def run_gshape(out: str | None) -> int:
    try:
        res = gshape.write(out)
    except gshape.GshapeRefusal as e:
        print(str(e), flush=True)
        return 2
    except gshape.GshapeStop as e:
        print(str(e), flush=True)
        return 4
    print(("G-SHAPE-F3 canonical run (every source committed at HEAD and unedited)" if res["canonical"]
           else "G-SHAPE-F3 test run (--out; never of record)"), flush=True)
    for ln in gshape.summary_lines(res):
        print(ln, flush=True)
    return gshape.EXIT[res["artifact"]["verdict"]]


def _short(x, n: int = 160) -> str:
    s = x if isinstance(x, str) else repr(x)
    return s if len(s) <= n else s[:n] + "..."


def _selftest(chk) -> None:
    """The driver's integration checks (model-free)."""
    pkg = sorted(p.stem for p in guard.PACKAGE_DIR.glob("*.py") if p.stem not in ("__init__", "testing"))
    chk("mf3_sessions: MODULES lists every mf3 module but the package marker and the test double",
        sorted(MODULES) == pkg, sorted(set(pkg) ^ set(MODULES)))
    labels = {w for p in schedule.roster() for w in p}

    def run(argv):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            try:
                rc = main(argv)
            except SystemExit as e:
                rc = e.code if isinstance(e.code, int) else 2
        return rc, buf.getvalue()

    with tempfile.TemporaryDirectory() as td:
        rc1, out1 = run(["--build-schedules", "--out", str(Path(td) / "s")])
        rc2, out2 = run(["--build-schedules", "--out", str(Path(td) / "s")])
        (Path(td) / "s" / "Q-F3_time_A1.json").write_text("{}")
        rc3, out3 = run(["--build-schedules", "--out", str(Path(td) / "s")])
        rcg, outg = run(["gshape", "--out", str(Path(td) / "g")])
    chk("mf3_sessions: --build-schedules writes 21 files that verify clean, re-runs identically, and refuses a "
        "differing existing file (exit 2)",
        rc1 == 0 and "21 files" in out1 and "verify clean" in out1 and rc2 == 0 and rc3 == 2
        and "SCHEDULE MISMATCH" in out3, (rc1, rc2, rc3))
    committed = schedule.verify_schedule_dir()
    chk("mf3_sessions: data/mf3/schedules equals a fresh regeneration byte for byte, manifest included (20 + 1)",
        committed == [] and len(list(schedule.DEFAULT_OUT.glob("*.json"))) == 21, committed[:3])
    chk("mf3_sessions: gshape --out runs G-SHAPE-F3 as a test run -- PASS; stdout is INVOCATION then the summary "
        "lines (counts and hashes, no label)",
        rcg == 0 and outg.startswith("INVOCATION: ") and "G-SHAPE-F3 PASS" in outg
        and "G-SHAPE-F3 test run" in outg and not any(re.search(rf"\b{w}\b", outg) for w in labels), outg[-300:])
    refused = {c: run([c]) for c in STAGE_CMDS}
    chk("mf3_sessions: time, id, qual and campaign are refused at the F3 build (exit 2), each named",
        all(rc == 2 and refusal(c) in out for c, (rc, out) in refused.items()), {c: rc for c, (rc, _) in refused.items()})
    rc0, out0 = run([])
    chk("mf3_sessions: no action is refused (exit 2) and INVOCATION is the first line",
        rc0 == 2 and out0.startswith("INVOCATION: "))
    rch, outh = run(["hashes"])
    chk("mf3_sessions: hashes prints mf3's package sha256, the eleven m files' (the ten modules and __init__.py) "
        "and the weights binding of record",
        rch == 0 and f"MF3 PACKAGE sha256 {guard.package_sha256_of(guard.PACKAGE_DIR)}" in outh
        and outh.count("M MODULE ") == len(guard.M_HASHED) == 11 and f"revision {gshape.QWEN_REVISION}" in outh, outh[-200:])
    srcs = sorted(guard.PACKAGE_DIR.glob("*.py")) + [REPO / DRIVER_REL]
    cs = guard.check_call_sites([guard.PACKAGE_DIR, REPO / DRIVER_REL])
    with tempfile.TemporaryDirectory() as td:
        planted = Path(td) / "x.py"
        planted.write_text("def f(a):\n    return a.generate('p', 's', cached=True)\n")
        fired = guard.check_call_sites([planted])
    chk("mf3_sessions: the cached-path source guard is clean over mf3 and this driver, and fires on a planted "
        "cached=True", cs == [] and fired != [], cs[:2])
    fb = guard.forbidden_hits(srcs)
    chk("mf3_sessions: no forbidden literal in mf3 or this driver", fb == [], fb[:2])
    ip = guard.import_problems(runtime=True)
    chk("mf3_sessions: the licence's import set holds (static closure and a fresh interpreter, N1)", ip == [], ip[:2])
    chk("mf3_sessions: the quarantined state-present module is not loaded after the self-test",
        not any(m in sys.modules for m in guard.FORBIDDEN_MODULES))
    m_files = sorted((REPO / "valence_core" / "m").glob("*.py"))
    chk("mf3_sessions: the F3 build changes nothing in valence_core/m -- its package hash is the OLMo build's "
        "60199b36...feec", rs.m_resume.package_sha256_of(REPO / "valence_core" / "m").startswith("60199b36")
        and len(m_files) == 18)


def run_selftest() -> int:
    results: list[bool] = []

    def chk(name, ok, got="", note="", *rest) -> None:
        ok = bool(ok)
        results.append(ok)
        tail = " ".join(_short(x) for x in (got, note, *rest) if x is not None and not (isinstance(x, str) and x == ""))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" {tail}" if tail else ""), flush=True)

    for m in MODULES:
        mod = importlib.import_module(f"valence_core.mf3.{m}")
        try:
            mod._selftest(chk)
        except (Exception, SystemExit) as e:                    # noqa: BLE001
            chk(f"{m}: _selftest raised", False, f"{type(e).__name__}: {e}")
    try:
        _selftest(chk)
    except (Exception, SystemExit) as e:                        # noqa: BLE001
        chk("mf3_sessions: integration selftest raised", False, f"{type(e).__name__}: {e}")
    print(f"  {sum(results)}/{len(results)} mf3 selftest checks pass", flush=True)
    return 0 if all(results) else 1


def main(argv: list[str] | None = None) -> int:
    shown = sys.argv if argv is None else [sys.argv[0]] + list(argv)
    print("INVOCATION: " + " ".join([sys.executable] + shown), flush=True)
    ap = argparse.ArgumentParser(description="PROPOSAL-m Q-F3 driver (self-test, schedules, hashes, G-SHAPE-F3; "
                                             "the stage subcommands are refused at the F3 build)")
    ap.add_argument("--selftest", action="store_true", help="model-free self-test of valence_core.mf3")
    ap.add_argument("--build-schedules", action="store_true", help="write Q-F3's schedule files + manifest")
    ap.add_argument("--out", default=None, help="output directory for --build-schedules")
    sub = ap.add_subparsers(dest="cmd")
    g = sub.add_parser("gshape", help="G-SHAPE-F3 (m:290), model-free; canonical without --out")
    g.add_argument("--out", dest="gshape_out", default=None, help="a test directory (never of record)")
    h = sub.add_parser("hashes", help="the hashes LOCK-m-F3 v0.1 names (Q1 (C2)) and the weights binding")
    h.add_argument("--snapshot-dir", default=None, help="the hub snapshot directory (default: the cache's of record)")
    for c in STAGE_CMDS:
        sub.add_parser(c, help=f"{STAGE_NAMES[c]}: refused at the F3 build (wired at its step)")
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
        return hashes(a.snapshot_dir)
    if a.cmd in STAGE_CMDS:
        print(refusal(a.cmd), flush=True)
        return 2
    print("REFUSED: no action (--selftest, --build-schedules, hashes or gshape)", flush=True)
    return 2


if __name__ == "__main__":
    sys.exit(main())
