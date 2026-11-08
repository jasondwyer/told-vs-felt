#!/usr/bin/env python3
"""PROPOSAL-m Q-F3 driver (v1.11 §3.2 m:288-298, §8 step 19 m:361; ADDENDUM-m1 §4 step 5; the design seat's
prebuild answers of 2026-11-06, Q1 (C2) and Q6).

Q-F3's own driver (Q1: "A new driver, scripts/mf3_sessions.py"; scripts/m_sessions.py is untouched). It wires:

  --selftest          every valence_core.mf3 module's model-free self-test, then this driver's integration
                      checks; "  N/N mf3 selftest checks pass", exit 0 iff all pass.
  --build-schedules   Q-F3's schedule files and manifest (default data/mf3/schedules; --out a test
                      directory); an existing differing file is refused, never overwritten.
  hashes              what LOCK-m-F3 v0.1 names (Q1 (C2)): mf3's package_sha256, each imported
                      valence_core.m module's file sha256, the schedules' manifest sha256, the weights
                      binding of record (the hub cache's snapshot; nothing loaded).
  gshape              G-SHAPE-F3 (m:290), model-free; the canonical artifact data/mf3/gates/G-SHAPE-F3.json
                      needs every source committed at HEAD and unedited; --out a test directory.
  time --proposal-file F --lock-file L --analyzer-sha256 H --package-sha256 H --renders-sha16 H [--resume]
                      G-TIME-F3 (m:293): one session per Q-F3 arm (6) on Qwen, uncached, reasoning cap 60,
                      under LOCK-m-F3 v0.1 (wired at its step, after the lock: lock §11 item 1). The flags are
                      the lock's values (lock §1, "How a stage cites this file"); m_module_sha256 and the
                      weights binding are read from the lock's committed text. Before the load: the identity
                      (refused on its own), then the precheck (the licence by file, the run-time known answers,
                      the renders, the committed schedules, the checkpoint, m:267's laptop checklist, the gate
                      line), the driver check and the snapshot check, refused together (exit 2); then the DRIVER
                      and SNAPSHOT lines. After
                      it: the snapshot re-read and the model id (a STOP, exit 4). Exit 0 PASS, 4 STOP.

and refuses ``id``, ``qual`` and ``campaign`` (G-ID-F3, G-F3, the campaign): each is wired at its own step, on
its own word, after its lock (m:361; the OLMo build's PIN O12 form). The stage drivers they will call are built
and stub-tested in valence_core.mf3.stages.

Q6's forms (the seat: "scripts/mf3_sessions.py is written to the same forms from the start"): the
CHECKPOINT STATE INCONSISTENT line is valence_core.m.resume's sealed form, imported by mf3.resume; the
campaign-ruling refusals O4-1 (RULING BESIDE AN END PENDING), O1-3 (RULING REUSED), RM4-1's RULING-line note
and the VC4-1 / VC4-2 help and docstring sentences are the campaign subcommand's, written in
scripts/m_sessions.py's forms when that subcommand is wired; O2-3's listing forms (a bare git status
--porcelain, a name-only ls, git ls-files, git diff --name-status, shasum; no size or time metadata of
data/mf3/ckpt or data/mf3/reports) go into Q-F3's launch checklist until its VERDICTS. The rest of m's
pre-load check (the MLXLM_USE_MODELSCOPE and local-path refusals, the hub's own offline resolution, the
SNAPSHOT line, the post-load re-read with its model-id STOP) is the ``time`` wiring's (the routing of
2026-11-07: "Build at time"), in scripts/m_sessions.py's forms.

INVOCATION is the first line of every run. Nothing here loads a model except ``time``, through
``_load_qwen``, after every pre-load refusal.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib
import io
import json
import os
import re
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from valence_core.mf3 import gshape, guard, keys, schedule, stages  # noqa: E402
from valence_core.mf3 import resume as rs  # noqa: E402

DRIVER_REL = "scripts/mf3_sessions.py"
#: Every mf3 module with a self-test, in dependency order (the test double has none).
MODULES = ("keys", "banner", "schedule", "lines", "scaffold", "guard", "runner", "verify", "readrule", "bars",
           "resume", "stages", "gshape")
STAGE_CMDS = ("time", "id", "qual", "campaign")
STAGE_NAMES = {"time": "G-TIME-F3", "id": "G-ID-F3", "qual": "G-F3", "campaign": "the Q-F3 campaign"}
# PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; the seat's F-1, carrying the step-10 read's Q2: "an edit … that wires a
# subcommand … does not re-run G-SHAPE-F0", here G-SHAPE-F3): ``time`` is wired for Q-F3 under LOCK-m-F3 v0.1
# (lock §11 item 1: "the `time` subcommand is wired in `scripts/mf3_sessions.py` at its step"), on the PI's routing
# of 2026-11-07, item 1 ("… → LOCK-m-F3 v0.1 → G-TIME-F3 [go]"). The edit touches no scoring-stack function. The
# new blob's sha256 is printed by the DRIVER line and recorded in the G-TIME-F3 entry and in LOCK-m-F3 v0.2 (the
# step-10 read's Q2 condition, which Code reads F-1's "with the same scope" as carrying; the routing of
# 2026-11-07). id, qual and campaign stay refused until their steps.
WIRED_CMDS = ("time",)
REFUSED_CMDS = tuple(c for c in STAGE_CMDS if c not in WIRED_CMDS)
# PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's TIME_* form carried, scripts/m_sessions.py): G-TIME-F3 cites
# LOCK-m-F3.md (lock §1); one session per Q-F3 arm (m:293: "One session per Q-F3 arm (6), as G-TIME-F0"), the
# counts the committed time schedules carry (n 1 each); locked_path "uncached" (m:293, "G-TIME-F3 (Qwen,
# uncached)"); reasoning cap 60 (m:174; stages._extra refuses any other at G-TIME-F3). The five flags are the
# lock's values, as LOCK-m-F0 §0's "How a stage cites this file" made them for m's driver. The values are Q-F3's;
# TIME_REASONING_CAP and TIME_FLAG_HELP have no counterpart in m.
TIME_LOCK_FILE = "LOCK-m-F3.md"
TIME_FLAGS = ("proposal_file", "lock_file", "analyzer_sha256", "package_sha256", "renders_sha16")
TIME_COUNTS = tuple((t, 1) for t in keys.TEMPLATES)
TIME_LOCKED_PATH = "uncached"
TIME_REASONING_CAP = 60
TIME_FLAG_HELP = {"proposal_file": "the proposal of record (PROPOSAL-m-gating-campaign-v1_11.md)",
                  "lock_file": f"the lock ({TIME_LOCK_FILE})",
                  "analyzer_sha256": "the analyzer's sha256, as the lock names it",
                  "package_sha256": "mf3's package_sha256, as the lock names it",
                  "renders_sha16": "the renders' sha16, as the lock names it"}
HF_OFFLINE_ENV = "HF_HUB_OFFLINE"
# PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's PIN at LOCK v0.2 carried, scripts/m_sessions.py): the model id the
# Qwen path loads -- QwenMLXAdapter's default, passed explicitly by _load_qwen; the model of record mf3.resume
# binds -- and mlx_lm.utils._download's default allow_patterns, with which the snapshot check resolves the
# snapshot as the load does. The self-test asserts both equal their sources (the adapter's and mlx_lm's source,
# read, not imported) and m's driver's constants (its source, read, not imported).
QWEN_MODEL_ID = rs.QWEN_MODEL_ID
MLX_LM_ALLOW_PATTERNS = ("*.json", "model*.safetensors", "*.py", "tokenizer.model", "*.tiktoken",
                         "tiktoken.model", "*.txt", "*.jsonl", "*.jinja")
_HEX64_RX = re.compile(r"\b[0-9a-f]{64}\b")
_WEIGHTS_RX = re.compile(r"(?<![\w-])WEIGHTS (\S+) revision ([0-9a-f]{40}) sha256 ([0-9a-f]{64})\b")
# PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's TOTALS_RX / redact_totals / _say carried): every REFUSED and STOP
# line of the stage path passes through redact_totals (the step-14 read's Q3) and goes to stderr, as m's do.
TOTALS_RX = re.compile(r"hour_cap_ms_used \S+ != the sessions\\*' \S+ ms")
TOTALS_REDACTED = ("hour_cap_ms_used and the sessions' total differ (both figures redacted at the driver's "
                   "print: the step-14 read, Q3)")


def redact_totals(text: str) -> str:
    """``text`` with every occurrence of Q3's two totals replaced by TOTALS_REDACTED."""
    return TOTALS_RX.sub(TOTALS_REDACTED, text)


def _say(line: str) -> None:
    # a REFUSED or STOP line of the stage path: redacted (Q3), then printed to stderr
    print(redact_totals(line), file=sys.stderr, flush=True)


def refusal(cmd: str) -> str:
    return (f"REFUSED: {cmd} ({STAGE_NAMES[cmd]}) is not wired yet -- each Q-F3 stage subcommand is wired at its "
            f"own step, on its own word, after its lock (m:361); its driver is built and stub-tested in "
            f"valence_core.mf3.stages")


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


# --- the time wiring: G-TIME-F3 (m:293) ------------------------------------------------------------
def _load_qwen():
    """The Qwen adapter, through the package's one loader (valence_core.adapters.qwen_or_explain), with
    QWEN_MODEL_ID passed explicitly (the snapshot check reads the same constant)."""
    from valence_core.adapters import qwen_or_explain
    return qwen_or_explain(__file__, model_id=QWEN_MODEL_ID)


def lock_m_modules(lock_text: str) -> tuple[dict[str, str] | None, list[str]]:
    """(m_module_sha256, problems) read from a lock's committed text: for each file of guard.M_HASHED,
    the one sha256 named on the lines that name its path; (None, problems) if any file is named on no
    line with a sha256, or with two different ones."""
    out: dict[str, str] = {}
    probs: list[str] = []
    lines = lock_text.splitlines()
    for m in guard.M_HASHED:
        path = f"valence_core/m/{m}.py"
        found = {h for ln in lines if path in ln for h in _HEX64_RX.findall(ln)}
        if len(found) != 1:
            probs.append(f"--lock-file {TIME_LOCK_FILE}: its committed text names {path} with "
                         f"{'no' if not found else len(found)} sha256 (one is required: lock §1, the eleven m files)")
            continue
        out[m] = found.pop()
    return (None, probs) if probs else (dict(sorted(out.items())), [])


def lock_weights(lock_text: str) -> tuple[tuple[str, str] | None, list[str]]:
    """((revision, sha256), problems) read from a lock's committed text: its one WEIGHTS line (lock §1),
    which must name QWEN_MODEL_ID; (None, problems) if there is none, more than one value, or another model."""
    found = set(_WEIGHTS_RX.findall(lock_text))
    if len(found) != 1:
        return None, [f"--lock-file {TIME_LOCK_FILE}: its committed text carries {len(found)} distinct WEIGHTS "
                      f"lines (one is required: lock §1, the weights of record)"]
    model, rev, sha = found.pop()
    if model != QWEN_MODEL_ID:
        return None, [f"--lock-file {TIME_LOCK_FILE}: its WEIGHTS line names {model}, not the model of record "
                      f"{QWEN_MODEL_ID}"]
    return (rev, sha), []


def time_identity_extra(proposal_file: str, lock_file: str, *, analyzer_sha256: str, package_sha256: str,
                        renders_sha16: str) -> tuple[dict | None, list[str]]:
    """G-TIME-F3's identity_extra and the problems that stop it being built ((None, problems)).

    PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's stage_identity_extra carried, scripts/m_sessions.py): the
    proposal's and the lock's sha256 are computed here from their COMMITTED blobs (stages.committed:
    committed at HEAD, working tree identical). The lock is TIME_LOCK_FILE, and its committed text must name
    the proposal's sha256 in full. The analyzer's and mf3's package sha256 and the renders' sha16 are the
    values the command line gives -- the lock's -- and are never derived here from the bytes they are
    checked against: the licence checks the first two at stage start ((d), (e)) and _renders_of_record the
    third. m_module_sha256 and the weights binding are read from the lock's committed text (the routing of
    2026-11-07): each of guard.M_HASHED's eleven files with the one sha256 the lines naming it carry, and
    the one WEIGHTS line, which must name QWEN_MODEL_ID; the licence then checks them against the files
    ((e')), the hub cache ((g)) and that same text ((f)). reasoning_cap 60 (m:174) and locked_path
    "uncached" (m:293) are this driver's; prior_proposal_sha256s is omitted (none under LOCK-m-F3 v0.1,
    lock §1). The result is validated by stages._extra (non-stub)."""
    probs: list[str] = []
    extra: dict = {}
    lock_text = ""
    for key, given in (("proposal", proposal_file), ("lock", lock_file)):
        p = Path(given)
        p = p if p.is_absolute() else REPO / p
        try:
            rel = p.resolve().relative_to(REPO.resolve()).as_posix()
        except (ValueError, OSError, RuntimeError):
            probs.append(f"--{key}-file {given}: lies outside the repository (or does not resolve)")
            continue
        if key == "lock" and rel != TIME_LOCK_FILE:
            probs.append(f"--lock-file {rel}: G-TIME-F3 cites {TIME_LOCK_FILE} (lock §1)")
            continue
        cp, data = stages.committed(rel)
        if cp or data is None:
            probs.append(f"--{key}-file {rel}: {cp} (the identity hashes its committed blob)")
            continue
        extra[f"{key}_file"] = rel
        extra[f"{key}_sha256"] = hashlib.sha256(data).hexdigest()
        if key == "lock":
            lock_text = data.decode("utf-8", "replace")
    if probs:
        return None, probs
    if extra["proposal_sha256"] not in lock_text:
        return None, [f"--proposal-file {extra['proposal_file']}: its sha256 {extra['proposal_sha256'][:16]}... is "
                      f"not named in full in {TIME_LOCK_FILE}'s committed text (lock §1 binds the proposal of record)"]
    mm, mprobs = lock_m_modules(lock_text)
    wb, wprobs = lock_weights(lock_text)
    if mprobs or wprobs or mm is None or wb is None:
        return None, mprobs + wprobs
    extra.update(analyzer_sha256=analyzer_sha256, package_sha256=package_sha256, renders_sha16=renders_sha16,
                 m_module_sha256=mm, weights_revision=wb[0], weights_sha256=wb[1],
                 reasoning_cap=TIME_REASONING_CAP, locked_path=TIME_LOCKED_PATH)
    try:
        stages._extra(extra, stage="time", stub=False)
    except ValueError as e:
        return None, [str(e)]
    return extra, []


def _repo_rel(path: Path) -> str | None:
    try:
        return Path(path).resolve().relative_to(REPO.resolve()).as_posix()
    except (ValueError, OSError, RuntimeError):
        return None


def time_precheck(extra: dict, *, resume_run: bool, out_root: Path) -> list[str]:
    """G-TIME-F3's refusals that need no model, made before the Qwen load; [] = none fired.

    PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's stage_precheck carried for "time", scripts/m_sessions.py): the
    licence by file ((a)-(g)); the run-time known answers on the proposal the identity names; the renders of
    record; the committed schedule files; the checkpoint (the path itself; an ENDED one; one on disk without
    --resume and no end pending); m:267's laptop checklist (power, one model process, disk); the gate line and
    its files (CLAUDE.md and the analyzer committed, working tree identical; HEAD known). The stage
    (stages.run_gate_stage) makes each of them again after the load, except the refusal of a looping link at
    the checkpoint path, which only this precheck makes. NOT made here, so made only by the stage after the
    load: a resume's comparison of the checkpoint with this run (rs.load_or_init's identity and readability
    refusals, stages._record_licence), runner.f3_startup's pins, the counts against the committed files' n,
    the bars' firing-case completeness and the stage's internal assertions. ``run_time`` adds the driver
    check's and the snapshot check's problems and refuses once. Every problem passes through redact_totals."""
    name = stages.stage_name("time")
    probs = [f"licence: {p}" for p in stages.licence_problems(extra)]
    proposal = stages._proposal_path(extra)
    probs += [f"startup: {p}" for p in stages.startup_problems(proposal)]
    try:
        stages._renders_of_record(extra, name)
    except SystemExit as e:
        probs.append(f"renders: {e}")
    paths = stages.out_paths("time", out_root)
    try:
        stages.load_committed([("time", t) for t, _ in TIME_COUNTS], paths["schedules"])
    except SystemExit as e:
        probs.append(f"schedules: {e}")
    try:
        cpath = stages.checkpoint_path(None, paths)
        rs.refuse_ended(cpath)
        # is_symlink: checkpoint_path resolve()s non-strictly; on Python 3.13+ a looping link comes back
        # unresolved, so the resolved path can still be a link, which only this precheck refuses; on 3.12
        # resolve() raises RuntimeError on the loop (caught below) -- m's comment, carried
        if (cpath.exists() or cpath.is_symlink()) and not resume_run and not rs.pending_at(cpath):
            probs.append(f"checkpoint: CHECKPOINT EXISTS at {cpath}; pass --resume to continue it or move it aside "
                         f"(never overwritten)")
    except SystemExit as e:
        probs.append(f"checkpoint: {e}")
    except (RuntimeError, OSError) as e:
        probs.append(f"checkpoint: the checkpoint path does not resolve ({type(e).__name__})")
    probs += [f"preflight: {p}" for p in guard.preflight_laptop()]
    probs += [f"gate line: {p}" for p in stages.gate_line(name, proposal)[1]]
    for what, path in (("CLAUDE.md", stages.CLAUDE_MD_PATH), ("analyzer", stages.ANALYZER_PATH)):
        rel = _repo_rel(path)
        probs += ([f"gate line: {what} {path} lies outside the repository"] if rel is None
                  else [f"gate line: {what} {x}" for x in stages.committed(rel)[0]])
    return [redact_totals(p) for p in probs]


def driver_problems() -> tuple[list[str], str | None]:
    """(problems, sha256) of this driver's bytes: [] and the sha256 of its committed blob when it is
    committed at HEAD with the working tree's bytes (stages.committed); else the problems and None.

    PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's driver_problems carried): the step-10 read's Q2 makes the
    record of the wiring driver's blob a condition of every wiring of its kind ("the new blob's sha256 printed
    by the DRIVER line and recorded in the entry of the stage it wires and in the next lock revision …"), which
    Code reads F-1 as carrying to this driver (the routing of 2026-11-07: G-TIME-F3's entry and LOCK-m-F3
    v0.2). run_time's Qwen path refuses an uncommitted driver and prints the DRIVER line from this one call
    before the load, so the value recorded is a value the run logged. A process running any file but the driver
    of record (REPO/DRIVER_REL) -- a copy, edited or not -- is refused: the DRIVER line names that path's committed
    blob, which would not be the code running (the review's MINOR-2; m derives DRIVER_REL from __file__)."""
    try:
        here = Path(__file__).resolve()
    except (OSError, RuntimeError):
        here = None
    if here != (REPO / DRIVER_REL).resolve():
        return [f"this process runs {__file__}, not the driver of record {DRIVER_REL} (the DRIVER line names that "
                f"file's committed blob)"], None
    cp, data = stages.committed(DRIVER_REL)
    if cp or data is None:
        return list(cp) or [f"{DRIVER_REL}: unreadable"], None
    return [], hashlib.sha256(data).hexdigest()


def qwen_snapshot(*, model_id: str | None = None, cache_dir: str | os.PathLike | None = None,
                  environ: dict | None = None, cwd: str | os.PathLike | None = None) -> tuple[list[str], dict | None]:
    """(problems, info) of the Qwen weights an offline load reads; [] and the info when clear.

    PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's qwen_snapshot carried verbatim in its checks, the routing of
    2026-11-07: "Build at time"): each refusal mirrors how the load resolves the weights (jlens_qwen.model.load
    -> mlx_lm.load -> mlx_lm.utils._download -> huggingface_hub.snapshot_download): HF_HUB_OFFLINE must be
    exactly "1"; MLXLM_USE_MODELSCOPE must not be "true" in any case (mlx_lm tests it so, and would take
    modelscope's downloader); no path or link named like the model id may exist relative to the working
    directory (mlx_lm loads an existing one before the hub cache; a dangling link is refused conservatively);
    the hub cache's `refs/main` for QWEN_MODEL_ID must be, as raw file text, a 40-hex revision whose snapshot
    directory exists and holds config.json, tokenizer.json, model.safetensors.index.json and every weight
    file the index names (each a plain file name, resolving to a file); and the hub's own offline resolution
    with mlx_lm's patterns (snapshot_download, local_files_only) must succeed and return that same directory.
    The cache is huggingface_hub's HF_HUB_CACHE. info: model_id, revision, snapshot_dir, n_snapshots
    (snapshot directories of the model's cache repo), offline. The licence's (g) checks the bound revision
    and the binding; this check is the load's own resolution, and its SNAPSHOT line is the raw's record."""
    env = os.environ if environ is None else environ
    probs: list[str] = []
    if env.get(HF_OFFLINE_ENV) != "1":
        probs.append(f"{HF_OFFLINE_ENV} is {env.get(HF_OFFLINE_ENV)!r}, not '1' (Code's form of the offline load: the "
                     f"licence's (g) and the seat's step-10 read, Q5)")
    ms = env.get("MLXLM_USE_MODELSCOPE", "False")
    if str(ms).lower() == "true":
        probs.append(f"MLXLM_USE_MODELSCOPE is {ms!r} (mlx_lm tests .lower() == 'true'): mlx_lm would load "
                     f"through modelscope, not the hub cache")
    model_id = QWEN_MODEL_ID if model_id is None else str(model_id)
    here = Path.cwd() if cwd is None else Path(cwd)
    if (here / model_id).exists() or (here / model_id).is_symlink():
        probs.append(f"{here / model_id} exists or is a link: mlx_lm loads a local path named like the model id "
                     f"before the hub cache (a dangling link refused conservatively)")
    if cache_dir is None:
        from huggingface_hub import constants as hf_constants
        cache_dir = hf_constants.HF_HUB_CACHE
    repo = Path(cache_dir) / ("models--" + model_id.replace("/", "--"))
    try:
        rev = (repo / "refs" / "main").read_text(encoding="utf-8")
    except (OSError, ValueError):
        return probs + [f"no readable refs/main for {model_id} under {cache_dir}"], None
    if not re.fullmatch(r"[0-9a-f]{40}", rev):
        return probs + [f"refs/main for {model_id} is not, as raw text, a 40-hex revision: {rev[:60]!r} (the "
                        f"hub's offline load reads it raw)"], None
    snap = repo / "snapshots" / rev
    if not snap.is_dir():
        return probs + [f"refs/main names {rev}, but no snapshot directory {snap} exists"], None
    try:
        n_snap = sum(1 for d in (repo / "snapshots").iterdir() if d.is_dir())
        index = json.loads((snap / "model.safetensors.index.json").read_text(encoding="utf-8"))
        weights = sorted(set(index["weight_map"].values()))
        bad = [w for w in weights if type(w) is not str or not w or "/" in w or "\\" in w or w in (".", "..")]
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as e:
        return probs + [f"snapshot {rev}: model.safetensors.index.json unreadable "
                        f"({type(e).__name__})"], None
    if bad:
        return probs + [f"snapshot {rev}: the index names a weight that is not a plain file name: {bad[:2]!r}"], None
    need = ["config.json", "tokenizer.json", "model.safetensors.index.json"] + weights
    missing = [f for f in need if not (snap / f).is_file()]
    if missing:
        probs.append(f"snapshot {rev} is incomplete: {missing[:4]} missing (an offline load would fail)")
    if not weights:
        probs.append(f"snapshot {rev}: the index names no weight file")
    try:
        from huggingface_hub import snapshot_download
        got = snapshot_download(model_id, local_files_only=True, allow_patterns=list(MLX_LM_ALLOW_PATTERNS),
                                cache_dir=str(cache_dir))
        if Path(got).resolve() != snap.resolve():
            probs.append(f"the hub's offline resolution gives {got}, not refs/main's snapshot {snap}")
    except Exception as e:                                      # noqa: BLE001 -- any failure refuses
        probs.append(f"the hub's offline resolution with mlx_lm's patterns refuses: {type(e).__name__}")
    info = {"model_id": model_id, "revision": rev, "snapshot_dir": str(snap),
            "n_snapshots": n_snap, "offline": env.get(HF_OFFLINE_ENV)}
    return probs, (None if probs else info)


def snapshot_line(info: dict) -> str:
    return (f"SNAPSHOT {info['model_id']} {info['revision']}: refs/main; {info['snapshot_dir']}; "
            f"{info['n_snapshots']} snapshot(s) in the model's cache repo; {HF_OFFLINE_ENV}={info['offline']}")


def run_time(*, proposal_file: str | None, lock_file: str | None, analyzer_sha256: str | None,
             package_sha256: str | None, renders_sha16: str | None, resume_run: bool, adapter_factory=None,
             out_root: Path | None = None) -> int:
    """G-TIME-F3 (m:293) through stages.run_gate_stage. Exit: stages.EXIT_CODES for the stage's status (0
    PASS, 4 STOP) and 4 STOP for any SystemExit from the loader or the stage, or the driver's own post-load
    snapshot re-read or model-id check (each "STOP: " and its message); 2 refused before the load (nothing
    loaded or written); any other exception is uncaught (a traceback; exit 1, or 130 on Ctrl-C).

    PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's _run_stage Qwen path carried, scripts/m_sessions.py):
    ``adapter_factory`` and ``out_root`` are the self-test's seam (a scripted stub writing a test directory,
    which stages refuses anywhere under data/mf3); without the factory the adapter is Qwen through
    qwen_or_explain, the out root is stages.DEFAULT_OUT (read at call time), a given ``out_root`` is refused
    before any load, and time_precheck, the driver check (one driver_problems call) and the snapshot check
    (one qwen_snapshot call), their problems refused together, then the DRIVER and SNAPSHOT lines, come before
    the load; after it, the snapshot is read again and the adapter's model_id compared: a re-read that refuses,
    a moved refs/main or another model id STOPs before a session (SNAPSHOT RE-READ REFUSED / SNAPSHOT MOVED /
    MODEL ID). A STOP, and any exit other than 0 or 2, is escalated to the seat; Code never self-adjudicates."""
    given = {"proposal_file": proposal_file, "lock_file": lock_file, "analyzer_sha256": analyzer_sha256,
             "package_sha256": package_sha256, "renders_sha16": renders_sha16}
    missing = ["--" + k.replace("_", "-") for k in TIME_FLAGS if given[k] is None]
    if missing:
        _say(f"REFUSED: time needs {missing}: the lock's values (lock §1, \"How a stage cites this file\"); "
             f"nothing loaded")
        return 2
    if out_root is not None and adapter_factory is None:
        _say("REFUSED: time: an out root names a test directory; the Qwen run writes data/mf3 only (nothing loaded)")
        return 2
    name = stages.stage_name("time")
    extra, probs = time_identity_extra(proposal_file, lock_file, analyzer_sha256=analyzer_sha256,
                                       package_sha256=package_sha256, renders_sha16=renders_sha16)
    if probs or extra is None:
        _say(f"REFUSED: {name}: {probs}; nothing loaded")
        return 2
    root = Path(stages.DEFAULT_OUT if out_root is None else out_root)
    try:
        if adapter_factory is None:
            pre = time_precheck(extra, resume_run=resume_run, out_root=root)
            dprobs, dsha = driver_problems()
            sprobs, snap = qwen_snapshot()
            # the snapshot's revision against the lock's (m's REVISION_STAGES refusal, carried): the licence's (g) read
            # refs/main at the precheck; this read is the load's own, so a move between the two is refused here,
            # before the load, not only by the re-read after it (the review's NOTE 3)
            if snap is not None and snap["revision"] != extra["weights_revision"]:
                sprobs = list(sprobs) + [f"refs/main is {snap['revision']}, not the lock's weights revision "
                                         f"{extra['weights_revision']} (lock §1; the licence's (g))"]
            pre += [f"driver: {p}" for p in dprobs] + [f"snapshot: {p}" for p in sprobs]
            if pre or dsha is None or snap is None:
                _say(f"REFUSED: {name}: {pre}; nothing loaded")
                return 2
            print(f"DRIVER {DRIVER_REL} {dsha}: committed at HEAD {stages._git_head()}, working tree identical",
                  flush=True)
            print(snapshot_line(snap), flush=True)
            adapter = _load_qwen()
            # the snapshot re-read after the load (m's): a re-read that refuses, a moved refs/main or another
            # model id STOPs before any session (a SystemExit, exit 4 below). It narrows, not closes, the window
            # between the precheck's read and the load's: a move and back between the two reads is not seen
            sprobs2, snap2 = qwen_snapshot()
            if sprobs2 or snap2 is None:
                raise SystemExit(f"SNAPSHOT RE-READ REFUSED ({name}): after the load the snapshot check refuses: "
                                 f"{sprobs2} -- no session runs")
            if snap2["revision"] != snap["revision"]:
                raise SystemExit(f"SNAPSHOT MOVED ({name}): before the load {snap['revision']}; after it "
                                 f"{snap2['revision']} -- no session runs")
            if getattr(adapter, "model_id", None) != snap["model_id"]:
                raise SystemExit(f"MODEL ID ({name}): the adapter loaded {getattr(adapter, 'model_id', None)!r}, "
                                 f"the snapshot check read {snap['model_id']!r} -- no session runs")
            print(f"SNAPSHOT re-read after the load: unchanged ({snap['revision']}); adapter model_id "
                  f"{snap['model_id']}", flush=True)
        else:
            adapter = adapter_factory()
        res = stages.run_gate_stage(adapter, gate="time", templates_counts=list(TIME_COUNTS), resume=resume_run,
                                    identity_extra=extra, out_root=root)
    except SystemExit as e:
        _say(f"STOP: {e}")
        return 4
    return stages.EXIT_CODES[res["status"]]


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
        (Path(td) / "s" / "Q-F3_time_A1.json").write_text("{}")
        rc3, out3 = run(["--build-schedules", "--out", str(Path(td) / "s")])
        rcg, outg = run(["gshape", "--out", str(Path(td) / "g")])
    chk("mf3_sessions: --build-schedules writes 21 files that verify clean, re-runs identically, and refuses a "
        "differing existing file (exit 2)",
        rc1 == 0 and "21 files" in out1 and "verify clean" in out1 and rc2 == 0 and rc3 == 2
        and "SCHEDULE MISMATCH" in out3, (rc1, rc2, rc3))
    committed_ = schedule.verify_schedule_dir()
    chk("mf3_sessions: data/mf3/schedules equals a fresh regeneration byte for byte, manifest included (20 + 1)",
        committed_ == [] and len(list(schedule.DEFAULT_OUT.glob("*.json"))) == 21, committed_[:3])
    chk("mf3_sessions: gshape --out runs G-SHAPE-F3 as a test run -- PASS; stdout is INVOCATION then the summary "
        "lines (counts and hashes, no label)",
        rcg == 0 and outg.startswith("INVOCATION: ") and "G-SHAPE-F3 PASS" in outg
        and "G-SHAPE-F3 test run" in outg and not any(re.search(rf"\b{w}\b", outg) for w in labels), outg[-300:])
    refused = {c: run([c]) for c in REFUSED_CMDS}
    chk("mf3_sessions: id, qual and campaign are refused (exit 2), each named; time is wired (WIRED_CMDS) and the "
        "four are STAGE_CMDS",
        all(rc == 2 and refusal(c) in out for c, (rc, out) in refused.items())
        and WIRED_CMDS == ("time",) and set(REFUSED_CMDS) | set(WIRED_CMDS) == set(STAGE_CMDS)
        and len(REFUSED_CMDS) == 3, {c: rc for c, (rc, _) in refused.items()})
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
    m_files = sorted((REPO / "valence_core" / "m").glob("*.py"))
    chk("mf3_sessions: valence_core/m holds 18 files and its package hash is 7756dcf4...49bb -- the OLMo build's "
        "60199b36...feec as moved by the G-ANL-F3 hygiene commit's N12 self-test fix to gcal.py (the seat's ruling, "
        "2026-11-07); the F3 build changes nothing there",
        rs.m_resume.package_sha256_of(REPO / "valence_core" / "m").startswith("7756dcf4") and len(m_files) == 18)
    _selftest_time(chk, labels, run)
    chk("mf3_sessions: the quarantined state-present module is not loaded after the self-test",
        not any(m in sys.modules for m in guard.FORBIDDEN_MODULES))


def _selftest_time(chk, labels, run) -> None:
    """The time wiring's checks (model-free). The cases that can reach the Qwen branch (``time_q``) run with
    ``_load_qwen`` a trap (in the post-load cases, a stand-in returning an object with a model_id),
    stages.run_gate_stage a trap, stages.DEFAULT_OUT a test root, m:267's laptop checklist stubbed and
    build_schedules and run_selftest trapped; the out-root seam call runs with the loader and the stage trapped and
    DEFAULT_OUT a test root; the stub-factory runs (``stub_run``), which run sessions on the stub through the real
    stage, have the loader trapped and DEFAULT_OUT a test root; the constants check calls the real _load_qwen with
    every Qwen route closed. So no case can load the model, run a session on it or write data/mf3, whatever the
    state of the tree or the machine (the review's MINOR-1). The last check asserts how often each trap was
    reached."""
    import ast
    import importlib.util as ilu
    from unittest import mock

    import huggingface_hub as hh
    import huggingface_hub.constants as hfc
    from valence_core.m import corr as m_corr
    from valence_core.mf3 import scaffold as sc_mod
    from valence_core.mf3 import testing

    G = globals()
    real_qs = G["qwen_snapshot"]
    real_committed = stages.committed
    loads: list = []
    stage_calls: list = []
    escapes: list = []

    def t_escape(name):
        # the round-2 review's NOTE 1: main dispatches --selftest and --build-schedules after time's refusal of
        # them; if that refusal regressed, the self-test would recurse or write data/mf3/schedules -- trapped here
        def f(*a, **k):
            escapes.append(name)
            raise SystemExit(f"selftest: {name} was reached from a time invocation")
        return f

    def t_loader():
        loads.append(1)
        raise SystemExit("selftest: the Qwen loader was reached")

    def t_stage(*a, **k):
        stage_calls.append(1)
        raise SystemExit("selftest: the stage was reached")

    def gpatch(name, val):
        # a module global replaced for the duration (the review's NOTE 12: the module dict, not sys.modules)
        return mock.patch.dict(G, {name: val})

    def run3(argv):
        # (rc, stdout, stderr), kept apart: the time path's REFUSED and STOP lines go to stderr (m's _say)
        buf, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
            try:
                rc = main(argv)
            except SystemExit as e:
                rc = e.code if isinstance(e.code, int) else 2
        return rc, buf.getvalue(), err.getvalue()

    def tree_state(root: Path) -> dict:
        out = {}
        for q in sorted(root.rglob("*")):
            k = str(q.relative_to(root))
            out[k] = ("link", os.readlink(q)) if q.is_symlink() else (
                ("file", hashlib.sha256(q.read_bytes()).hexdigest()) if q.is_file() else ("dir", None))
        return out

    def committed_but(rel_x: str, ret):
        # stages.committed with one path's answer planted; every other path read for real
        return lambda rel, repo=stages.REPO: ret if rel == rel_x else real_committed(rel, repo)

    def labelled(text: str) -> bool:
        return any(re.search(rf"\b{re.escape(w)}\b", text, re.IGNORECASE) for w in labels)

    real_out = stages.DEFAULT_OUT
    data_before = tree_state(real_out) if real_out.is_dir() else {}
    _pool, renders = sc_mod.pool_and_renders()
    lock_cp, lock_blob = stages.committed(TIME_LOCK_FILE)
    prop_sha = hashlib.sha256(stages.PROPOSAL_PATH.read_bytes()).hexdigest()
    tflags = {"proposal_file": stages.PROPOSAL_REL, "lock_file": TIME_LOCK_FILE,
              "analyzer_sha256": hashlib.sha256(stages.ANALYZER_PATH.read_bytes()).hexdigest(),
              "package_sha256": guard.package_sha256_of(guard.PACKAGE_DIR),
              "renders_sha16": m_corr.renders_sha(renders)}
    z64 = "0" * 64

    # --- the identity, from the committed lock ------------------------------------------------------
    ex, ex_probs = time_identity_extra(**tflags)
    lock_text = (lock_blob or b"").decode("utf-8", "replace")
    wl = _WEIGHTS_RX.findall(lock_text)
    chk("mf3_sessions: time's identity_extra from the committed LOCK-m-F3.md -- the proposal's and the lock's sha256 "
        "their committed blobs'; m_module_sha256 the eleven files' as hashed now and as the lock lists them; the "
        "weights its one WEIGHTS line's; reasoning_cap 60, locked_path uncached; stages._extra accepts it",
        lock_cp == [] and ex_probs == [] and ex is not None
        and ex["lock_sha256"] == hashlib.sha256(lock_blob).hexdigest() and ex["proposal_sha256"] == prop_sha
        and ex["m_module_sha256"] == dict(sorted(guard.m_module_sha256s().items()))
        and len(set(wl)) == 1 and (ex["weights_revision"], ex["weights_sha256"]) == wl[0][1:]
        and wl[0][0] == QWEN_MODEL_ID and ex["reasoning_cap"] == 60 and ex["locked_path"] == "uncached"
        and "prior_proposal_sha256s" not in ex, (lock_cp, ex_probs))
    planted_m, planted_w = "c" * 64, "d" * 64
    real_w = wl[0][2] if wl else z64
    planted_lock = lock_text.replace(guard.m_module_sha256s()["corr"], planted_m).replace(real_w, planted_w).encode("utf-8")
    with mock.patch.object(stages, "committed", committed_but(TIME_LOCK_FILE, ([], planted_lock))):
        ex_pl, pl_probs = time_identity_extra(**tflags)
        pl_lic = stages.licence_problems(ex_pl, environ={HF_OFFLINE_ENV: "1"}) if ex_pl is not None else ["no extra"]
    chk("mf3_sessions: m_module_sha256 and the weights are read from the lock's committed text, not from the files or "
        "the hub: a lock whose corr.py line and WEIGHTS line name other sha256 gives those values; the licence, run on "
        "that lock, then refuses the corr.py file ((e')) and the weights binding ((g)), and nothing for (f)",
        pl_probs == [] and ex_pl is not None and ex_pl["m_module_sha256"]["corr"] == planted_m
        and ex_pl["weights_sha256"] == planted_w and ex_pl["lock_sha256"] == hashlib.sha256(planted_lock).hexdigest()
        and any("valence_core/m/corr.py: its sha256 (computed now)" in x for x in pl_lic)
        and any("binds differently now" in x for x in pl_lic) and not any("committed text does not name" in x or
                                                                         "no line of its committed text" in x
                                                                         for x in pl_lic),
        (pl_probs, pl_lic[:3]))
    lic_now = stages.licence_problems(ex, environ={HF_OFFLINE_ENV: "1"}) if ex is not None else ["no extra"]
    chk("mf3_sessions: that identity is licensed now (stages.licence_problems (a)-(g), HF_HUB_OFFLINE=1 given): the "
        "proposal and the lock committed, the analyzer, mf3's package, the eleven m files and the weights the ones "
        "the identity and the lock name", lic_now == [], lic_now[:2])
    lock_rev = ex["weights_revision"] if ex is not None else "0" * 40
    fake_snap = {"model_id": QWEN_MODEL_ID, "revision": lock_rev, "snapshot_dir": "<selftest>/snapshots/" + lock_rev,
                 "n_snapshots": 1, "offline": "1"}

    # --- the lock's text, parsed: missing, doubled and other-model forms are refused ----------------
    one = "\n".join(f"| `valence_core/m/{m}.py` | `{v}` |" for m, v in sorted(guard.m_module_sha256s().items()))
    wline = f"- WEIGHTS {QWEN_MODEL_ID} revision {'a' * 40} sha256 {'b' * 64}"
    p_ok = lock_m_modules(one), lock_weights(wline)
    p_missing = lock_m_modules("\n".join(ln for ln in one.splitlines() if "/corr.py" not in ln))
    p_double = lock_m_modules(one + "\n| `valence_core/m/corr.py` | `" + "c" * 64 + "` |")
    p_noline = lock_weights("no weights here")
    p_two = lock_weights(wline + "\n" + wline.replace("b" * 64, "d" * 64))
    p_other = lock_weights(wline.replace(QWEN_MODEL_ID, "other/model"))
    p_glued = lock_weights(wline.replace("- WEIGHTS", "- XWEIGHTS"))
    p_hyph = lock_weights(wline.replace("- WEIGHTS", "- OLD-WEIGHTS"))
    p_digit = lock_weights(wline.replace("- WEIGHTS", "- 2WEIGHTS"))
    p_under = lock_weights(wline.replace("- WEIGHTS", "- _WEIGHTS"))
    chk("mf3_sessions: the lock parsers -- the eleven m files read one sha256 each and the WEIGHTS line its revision "
        "and sha256; refused: an m file named on no line, an m file with two different sha256, no WEIGHTS line (one "
        "glued to a letter, a digit, an underscore or a hyphen before it is none), two different WEIGHTS lines, a "
        "WEIGHTS line for another model",
        p_ok[0][1] == [] and p_ok[0][0] == dict(sorted(guard.m_module_sha256s().items()))
        and p_ok[1] == (("a" * 40, "b" * 64), [])
        and p_missing[0] is None and "valence_core/m/corr.py with no sha256" in p_missing[1][0]
        and p_double[0] is None and "valence_core/m/corr.py with 2 sha256" in p_double[1][0]
        and p_noline[0] is None and "0 distinct WEIGHTS lines" in p_noline[1][0]
        and p_glued[0] is None and "0 distinct WEIGHTS lines" in p_glued[1][0]
        and all(x[0] is None and "0 distinct WEIGHTS lines" in x[1][0] for x in (p_hyph, p_digit, p_under))
        and p_two[0] is None and "2 distinct WEIGHTS lines" in p_two[1][0]
        and p_other[0] is None and "names other/model" in p_other[1][0],
        (p_missing[1][:1], p_double[1][:1], p_noline[1], p_two[1], p_other[1], p_glued[1]))

    # --- the constants against their sources (read, not imported) -----------------------------------
    m_drv = REPO / "scripts" / "m_sessions.py"
    m_tree = ast.parse(m_drv.read_text(encoding="utf-8"))

    def assigned(name: str):
        for n in m_tree.body:
            if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in n.targets):
                if isinstance(n.value, ast.Call) and n.value.args:       # re.compile("...")
                    return ast.literal_eval(n.value.args[0])
                return ast.literal_eval(n.value)
        return None
    qm_src = REPO / "valence_core" / "adapters" / "qwen_mlx.py"
    qm_default = None
    for n in ast.walk(ast.parse(qm_src.read_text(encoding="utf-8"))):
        if isinstance(n, ast.FunctionDef) and n.name == "__init__" and n.args.defaults:
            for a_, d_ in zip(n.args.args[-len(n.args.defaults):], n.args.defaults):
                if a_.arg == "model_id":
                    qm_default = ast.literal_eval(d_)
    try:
        spec = ilu.find_spec("mlx_lm")
    except (ImportError, ValueError):
        spec = None
    mlx_src = (Path(list(spec.submodule_search_locations)[0]) / "utils.py"
               if spec is not None and spec.submodule_search_locations else None)
    dl = ([n for n in ast.walk(ast.parse(mlx_src.read_text(encoding="utf-8")))
           if isinstance(n, ast.FunctionDef) and n.name == "_download"]
          if mlx_src is not None and mlx_src.is_file() else [])
    pats = [ast.literal_eval(n) for n in ast.walk(dl[0]) if isinstance(n, ast.List)] if dl else []
    seen_kw: list = []
    from valence_core import adapters as adapters_pkg
    # the real _load_qwen, with every route to a model closed (the round-3 review's NOTE-2): qwen_or_explain answers,
    # get_adapter refuses, and importing mlx, mlx_lm or jlens_qwen fails (sys.modules entries None)
    def no_adapter(*a, **k):
        raise SystemExit("selftest: get_adapter was reached from _load_qwen")
    with mock.patch.object(adapters_pkg, "qwen_or_explain", lambda *a, **kw: seen_kw.append(kw) or "selftest-adapter"), \
            mock.patch.object(adapters_pkg, "get_adapter", no_adapter), \
            mock.patch.dict(sys.modules, {m_: None for m_ in ("mlx", "mlx.core", "mlx_lm", "jlens_qwen",
                                                              "jlens_qwen.model")}):
        loaded = _load_qwen()
    chk("mf3_sessions: QWEN_MODEL_ID is the model of record (mf3.resume), QwenMLXAdapter's default and m's driver's, "
        "and _load_qwen passes it explicitly; MLX_LM_ALLOW_PATTERNS is mlx_lm.utils._download's default list and m's "
        "driver's; HF_OFFLINE_ENV, TOTALS_RX's pattern and TOTALS_REDACTED are m's driver's, and the redaction "
        "replaces m's old totals form (the form is sealed at its source now; the pattern is kept as m keeps it)",
        QWEN_MODEL_ID == rs.QWEN_MODEL_ID == qm_default == assigned("QWEN_MODEL_ID") == gshape.QWEN_MODEL_ID
        and loaded == "selftest-adapter" and seen_kw == [{"model_id": QWEN_MODEL_ID}]
        and len(pats) == 1 and tuple(pats[0]) == MLX_LM_ALLOW_PATTERNS == assigned("MLX_LM_ALLOW_PATTERNS")
        and HF_OFFLINE_ENV == assigned("HF_OFFLINE_ENV") and TOTALS_RX.pattern == assigned("TOTALS_RX")
        and TOTALS_REDACTED == assigned("TOTALS_REDACTED")
        and redact_totals("x hour_cap_ms_used 5 != the sessions' 6 ms y") == f"x {TOTALS_REDACTED} y",
        (qm_default, pats, seen_kw, assigned("TOTALS_RX")))

    # time's help names each flag with its TIME_FLAG_HELP text, and --resume (the round-3 review's NOTE-5)
    rc_h, out_h, _err_h = run3(["time", "--help"])
    flat_h = "".join(out_h.split())          # argparse wraps help text, breaking at spaces and hyphens
    names_h = {"proposal_file": "proposal", "lock_file": TIME_LOCK_FILE, "analyzer_sha256": "analyzer's sha256",
               "package_sha256": "package_sha256", "renders_sha16": "renders' sha16"}
    chk("mf3_sessions: time --help lists the five flags, each followed by its own TIME_FLAG_HELP text (which names "
        "what the flag carries), and --resume (exit 0)",
        rc_h == 0 and set(TIME_FLAG_HELP) == set(TIME_FLAGS) == set(names_h) and "--resume" in flat_h
        and all(names_h[k] in v for k, v in TIME_FLAG_HELP.items())
        and all(f"--{k.replace('_', '-')}{k.upper()}" + "".join(v.split()) in flat_h for k, v in TIME_FLAG_HELP.items()),
        out_h[-200:])

    # --- the snapshot check over fake hub caches (the hub held offline by its own constant throughout: the round-2
    # review's NOTE 2 -- the real snapshot_download calls below cannot reach the network whatever the code passes)
    with tempfile.TemporaryDirectory() as td, mock.patch.object(hfc, "HF_HUB_OFFLINE", True):
        base = Path(td)
        rev = hashlib.sha1(b"mf3-time-selftest-revision").hexdigest()

        def fake_cache(nm: str, *, ref=rev, snap_rev=rev, drop=(), index=True, extra_snaps=(), stray=False):
            c = base / f"hfcache_{nm}"
            repo_d = c / ("models--" + QWEN_MODEL_ID.replace("/", "--"))
            (repo_d / "refs").mkdir(parents=True)
            if isinstance(ref, bytes):
                (repo_d / "refs" / "main").write_bytes(ref)
            elif ref is not None:
                (repo_d / "refs" / "main").write_text(ref, encoding="utf-8")
            if snap_rev is not None:
                sd = repo_d / "snapshots" / snap_rev
                sd.mkdir(parents=True)
                files = {"config.json": "{}", "tokenizer.json": "{}",
                         "model-00001-of-00002.safetensors": "w1", "model-00002-of-00002.safetensors": "w2"}
                if index is True:
                    files["model.safetensors.index.json"] = json.dumps({"weight_map": {
                        "a": "model-00001-of-00002.safetensors", "b": "model-00002-of-00002.safetensors"}})
                elif index is not None:
                    files["model.safetensors.index.json"] = index
                for f, body in files.items():
                    if f not in drop:
                        (sd / f).write_text(body, encoding="utf-8")
            for x in extra_snaps:
                (repo_d / "snapshots" / x).mkdir(parents=True)
            if stray:
                (repo_d / "snapshots" / "stray.txt").write_text("x", encoding="utf-8")
            return c

        on = {HF_OFFLINE_ENV: "1"}
        cwd_clean = base / "cwd_clean"
        cwd_clean.mkdir()
        cwd_model = base / "cwd_model"
        (cwd_model / QWEN_MODEL_ID).mkdir(parents=True)
        cwd_link = base / "cwd_link"
        (cwd_link / QWEN_MODEL_ID.split("/")[0]).mkdir(parents=True)
        (cwd_link / QWEN_MODEL_ID).symlink_to(base / "nowhere")

        def qs(nm, env=on, cwd=cwd_clean, **kw):
            return real_qs(cache_dir=fake_cache(nm, **kw), environ=env, cwd=cwd)

        sq = {
            "complete": qs("ok"),
            "two snapshots and a stray file": qs("two", extra_snaps=("f" * 40,), stray=True),
            "offline unset": qs("unset", env={}),
            "offline 'true'": qs("true", env={HF_OFFLINE_ENV: "true"}),
            "a local path named like the model id": qs("cwdmodel", cwd=cwd_model),
            "a dangling link named like the model id": qs("cwdlink", cwd=cwd_link),
            "no refs/main": qs("noref", ref=None),
            "refs/main not utf-8": qs("nonutf", ref=b"\xff" * 40),
            "refs/main not hex": qs("badref", ref="main"),
            "refs/main with a newline": qs("nlref", ref=rev + "\n"),
            "no snapshot dir": qs("nosnap", snap_rev="d" * 40),
            "a weight missing": qs("noweight", drop=("model-00002-of-00002.safetensors",)),
            "config missing": qs("nocfg", drop=("config.json",)),
            "tokenizer missing": qs("notok", drop=("tokenizer.json",)),
            "index unreadable": qs("badindex", index="not json"),
            "index without weight_map": qs("nowm", index="{}"),
            "index naming no weight": qs("emptywm", index=json.dumps({"weight_map": {}})),
            "a weight not a plain name": qs("relweight", index=json.dumps({"weight_map": {"a": "../outside.bin"}})),
            "a weight not a string": qs("intweight", index=json.dumps({"weight_map": {"a": 1}})),
        }
        want_sq = {"offline unset": "HF_HUB_OFFLINE is None, not '1'",
                   "offline 'true'": "HF_HUB_OFFLINE is 'true', not '1'",
                   "a local path named like the model id": "mlx_lm loads a local path named like the model id",
                   "a dangling link named like the model id": "mlx_lm loads a local path named like the model id",
                   "no refs/main": "no readable refs/main for", "refs/main not utf-8": "no readable refs/main for",
                   "refs/main not hex": "is not, as raw text, a 40-hex revision",
                   "refs/main with a newline": "is not, as raw text, a 40-hex revision",
                   "no snapshot dir": "but no snapshot directory", "a weight missing": "is incomplete",
                   "config missing": "['config.json'] missing", "tokenizer missing": "['tokenizer.json'] missing",
                   "index unreadable": "model.safetensors.index.json unreadable (JSONDecodeError)",
                   "index without weight_map": "model.safetensors.index.json unreadable (KeyError)",
                   "index naming no weight": "the index names no weight file",
                   "a weight not a plain name": "not a plain file name",
                   "a weight not a string": "not a plain file name"}
        okp, oki = sq["complete"]
        twp, twi = sq["two snapshots and a stray file"]
        bad_sq = {k: v for k, v in sq.items() if k in want_sq
                  and not (v[1] is None and any(want_sq[k] in x for x in v[0]))}
        chk("mf3_sessions: qwen_snapshot over fake hub caches -- a complete snapshot with HF_HUB_OFFLINE=1 is clear (the "
            "model of record, refs/main's revision, the hub's own offline resolution agreeing) and its SNAPSHOT line "
            "names exactly them; two snapshot directories and a stray file count 2; refused, with no info, in 17 "
            "cases: the variable unset or not exactly '1'; a local path or a dangling link named like the model id; "
            "refs/main absent, not UTF-8, not hex, or with a newline; no snapshot directory; a weight, config.json or "
            "tokenizer.json missing; an index unreadable, without weight_map, naming no weight, or naming a weight "
            "that is not a plain file name or not a string",
            okp == [] and oki is not None and oki["model_id"] == QWEN_MODEL_ID and oki["revision"] == rev
            and oki["n_snapshots"] == 1 and oki["offline"] == "1"
            and snapshot_line(oki) == (f"SNAPSHOT {QWEN_MODEL_ID} {rev}: refs/main; {oki['snapshot_dir']}; 1 snapshot(s) "
                                       f"in the model's cache repo; HF_HUB_OFFLINE=1")
            and twp == [] and twi is not None and twi["n_snapshots"] == 2
            and not bad_sq and len(want_sq) == 17 and set(want_sq) == set(sq) - {"complete", "two snapshots and a stray file"},
            (okp, {k: v[0][:1] for k, v in bad_sq.items()}))
        ms_sq = {v: qs(f"mscope_{i}", env={HF_OFFLINE_ENV: "1", "MLXLM_USE_MODELSCOPE": v})
                 for i, v in enumerate(("True", "true", "TRUE", "tRuE"))}
        ms_off = qs("mscope_false", env={HF_OFFLINE_ENV: "1", "MLXLM_USE_MODELSCOPE": "False"})
        chk("mf3_sessions: qwen_snapshot refuses MLXLM_USE_MODELSCOPE 'true' in any letter case ('True', 'true', "
            "'TRUE', 'tRuE'), with no info, each message naming the value; 'False' is clear",
            all(v[1] is None and any(f"MLXLM_USE_MODELSCOPE is {k!r} (mlx_lm tests .lower() == 'true')" in x
                                     for x in v[0]) for k, v in ms_sq.items())
            and ms_off[0] == [] and ms_off[1] is not None, {k: v[0][:1] for k, v in ms_sq.items()})
        # the hub's own offline resolution (m's case, carried): over a cached tree listing, files outside mlx_lm's
        # patterns absent are clear and a pattern file absent is refused by the hub; the hub is called once with the
        # load's model id and mlx_lm's patterns, offline, on the given cache; a resolution elsewhere is refused
        def tree_listed(c, names):
            d = c / ("models--" + QWEN_MODEL_ID.replace("/", "--")) / "trees"
            d.mkdir(parents=True, exist_ok=True)
            (d / f"{rev}.json").write_text(json.dumps({"format_version": 1, "files": {
                n_: {"size": 1, "blob_id": "0" * 40} for n_ in names}}), encoding="utf-8")
            return c
        present = ["config.json", "tokenizer.json", "model.safetensors.index.json",
                   "model-00001-of-00002.safetensors", "model-00002-of-00002.safetensors"]
        h_np = real_qs(cache_dir=tree_listed(fake_cache("tree_np"), present + ["README.md", ".gitattributes"]),
                       environ=on, cwd=cwd_clean)
        h_pat = real_qs(cache_dir=tree_listed(fake_cache("tree_pat"), present + ["chat_template.jinja"]),
                        environ=on, cwd=cwd_clean)
        h_calls: list = []
        h_rec_c = fake_cache("hub_rec")
        real_sd = hh.snapshot_download

        def rec_sd(*a, **k):
            h_calls.append((a, k))
            return real_sd(*a, **k)
        with mock.patch.object(hh, "snapshot_download", rec_sd):
            h_rec = real_qs(cache_dir=h_rec_c, environ=on, cwd=cwd_clean)
        h_other_dir = base / "hub_elsewhere"
        h_other_dir.mkdir()
        with mock.patch.object(hh, "snapshot_download", lambda *a, **k: str(h_other_dir)):
            h_other = real_qs(cache_dir=fake_cache("hub_other"), environ=on, cwd=cwd_clean)

        def boom(*a, **k):
            raise RuntimeError("selftest: the hub refuses")
        with mock.patch.object(hh, "snapshot_download", boom):
            h_boom = real_qs(cache_dir=fake_cache("hub_boom"), environ=on, cwd=cwd_clean)
        chk("mf3_sessions: qwen_snapshot's hub resolution (m's case) -- over a cached tree listing, files outside "
            "mlx_lm's patterns absent are clear and a pattern file absent (chat_template.jinja) is refused "
            "(IncompleteSnapshotError); the hub is called once with the load's model id and mlx_lm's patterns, offline "
            "(local_files_only) on the cache given; a resolution to another directory, or a hub that raises, is refused",
            h_np[0] == [] and h_np[1] is not None and h_pat[1] is None
            and any("the hub's offline resolution with mlx_lm's patterns refuses: IncompleteSnapshotError" in x
                    for x in h_pat[0])
            and h_rec[0] == [] and h_calls == [((QWEN_MODEL_ID,), {"local_files_only": True,
                                                                  "allow_patterns": list(MLX_LM_ALLOW_PATTERNS),
                                                                  "cache_dir": str(h_rec_c)})]
            and h_other[1] is None and any("the hub's offline resolution gives" in x for x in h_other[0])
            and h_boom[1] is None and any("refuses: RuntimeError" in x for x in h_boom[0]),
            (h_np[0][:2], h_pat[0][:2], h_calls[:1], h_other[0][:1], h_boom[0][:1]))
        # the production defaults: huggingface_hub's HF_HUB_CACHE and os.environ, read at call time
        prod_c = fake_cache("prod")
        with mock.patch.object(hfc, "HF_HUB_CACHE", str(prod_c)), mock.patch.dict(os.environ):
            os.environ[HF_OFFLINE_ENV] = "1"
            pd_on = real_qs(cwd=cwd_clean)
            pd_env_given = real_qs(cache_dir=prod_c, environ={}, cwd=cwd_clean)
            os.environ.pop(HF_OFFLINE_ENV, None)
            pd_off = real_qs(cwd=cwd_clean)
        chk("mf3_sessions: qwen_snapshot's production defaults read huggingface_hub's HF_HUB_CACHE and os.environ at "
            "call time (clear with HF_HUB_OFFLINE=1, refused without it; an explicit environ wins)",
            pd_on[0] == [] and pd_on[1] is not None and pd_on[1]["snapshot_dir"].startswith(str(prod_c))
            and pd_off[1] is None and any("HF_HUB_OFFLINE is None" in x for x in pd_off[0])
            and pd_env_given[1] is None, (pd_on[0][:1], pd_off[0][:1]))
        # the working directory: by default the process's (a path named like the model id there refuses); weight names
        # '..', '' and one with a backslash are not plain file names (m's w_default and w_names, carried)
        cwd_d = base / "cwd_default"
        (cwd_d / QWEN_MODEL_ID).mkdir(parents=True)
        here_ = os.getcwd()
        os.chdir(cwd_d)
        try:
            w_default = real_qs(cache_dir=fake_cache("cwd_default"), environ=on)
        finally:
            os.chdir(here_)
        w_names = {nm_: real_qs(cache_dir=fake_cache(f"wname_{i}", index=json.dumps({"weight_map": {"a": nm_}})),
                                environ=on, cwd=cwd_clean) for i, nm_ in enumerate(("..", "", "a\\b"))}
        chk("mf3_sessions: qwen_snapshot's local-path refusal reads the process's working directory by default, and "
            "the weight names '..', '' and one with a backslash are refused as not plain file names",
            w_default[1] is None and any("mlx_lm loads a local path named like the model id" in x for x in w_default[0])
            and all(v[1] is None and any("not a plain file name" in x for x in v[0]) for v in w_names.values()),
            (w_default[0][:1], {k: v[0][:1] for k, v in w_names.items()}))

    # --- the stub path first (its ended checkpoint serves the precheck's ENDED cases below) -----------
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        made: list = []

        def fresh(nm: str) -> Path:
            r = base / nm / "mf3"
            schedule.write_schedule_files(r / "schedules")
            made.append(r)
            return r

        def gate_cells(gate):
            return {(t, j): schedule.gate_schedule(gate, t, schedule.GATE_PLAN_COUNTS[(gate, t)])[j]
                    for t in keys.TEMPLATES for j in range(schedule.GATE_PLAN_COUNTS[(gate, t)])}
        made_ad: list = []

        def stub(interrupt=None):
            def f():
                a = testing.F3Adapter()
                a.load(stages._script_policy("time", gate_cells("time"), None, interrupt), None)
                made_ad.append(a)
                return a
            return f
        gates = base / "gates"
        gates.mkdir()

        def stub_run(root, factory, resume_run=False, *, stage=None):
            # the stub factory's seam, with the loader a trap, the canonical out root a test root and the G-ID
            # artifact's directory a test directory; ``stage`` replaces stages.run_gate_stage (the exit-code case)
            buf, err = io.StringIO(), io.StringIO()
            with contextlib.ExitStack() as st:
                st.enter_context(mock.patch.object(guard, "GATES_DIR", gates))
                st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", base / "default-out"))
                st.enter_context(gpatch("_load_qwen", t_loader))
                if stage is not None:
                    st.enter_context(mock.patch.object(stages, "run_gate_stage", stage))
                st.enter_context(contextlib.redirect_stdout(buf))
                st.enter_context(contextlib.redirect_stderr(err))
                try:
                    rc = run_time(**tflags, resume_run=resume_run, adapter_factory=factory, out_root=root)
                except stages._Interrupt as e:
                    rc = e
            return rc, buf.getvalue(), err.getvalue()
        sroot = fresh("stub")
        rc_s, out_s, err_s = stub_run(sroot, stub())
        ck_p = sroot / "ckpt" / f"{keys.UNIT}_time.json"
        ck_s = rs.read_checkpoint(ck_p) if ck_p.is_file() else {}
        chk("mf3_sessions: time on the stub factory (the self-test's seam) runs G-TIME-F3 through stages.run_gate_stage "
            "with TIME_COUNTS -- six sessions, one per template, PASS (exit 0); the checkpoint, the report and the reads "
            "under the test root; no DRIVER or SNAPSHOT line (the Qwen path's); stdout and stderr name no label in any "
            "letter case",
            rc_s == 0 and len(made_ad) == 1 and [r["template"] for r in ck_s.get("sessions", [])] == list(keys.TEMPLATES)
            and (ck_s.get("stage_end") or {}).get("status") == "PASS"
            and (sroot / "reports" / f"{keys.UNIT}_time_report.json").is_file()
            and (sroot / "reports" / f"{keys.UNIT}_time_reads.json").is_file()
            and "DRIVER " not in out_s and "SNAPSHOT " not in out_s and not labelled(out_s + err_s)
            and sum(ln.startswith("time A") for ln in out_s.splitlines()) == 6, (rc_s, err_s[-200:], out_s[-200:]))
        rcs = {flag: stub_run(sroot, stub(), flag) for flag in (False, True)}
        chk("mf3_sessions: time on an ended G-TIME-F3 checkpoint, through the stub factory, is a STOP (exit 4, 'STAGE "
            "ENDED') with or without --resume: the stage refuses it after the factory (a resume never re-runs an "
            "ended stage)", all(v[0] == 4 and "STAGE ENDED" in v[2] for v in rcs.values()), {k: v[0] for k, v in rcs.items()})
        # --resume reaches the stage: a run interrupted in A3 leaves four sessions; without --resume the stage refuses
        # the checkpoint (a STOP, exit 4); with it only A3 and A3s are generated, and the stage ends PASS
        rroot = fresh("resume")
        stop_a3 = lambda t, s, kind, i: t == "A3" and kind == "forced" and i == 0
        made_ad.clear()
        rc_ri, _o, _e = stub_run(rroot, stub(stop_a3))
        ck_ri = rs.read_checkpoint(rroot / "ckpt" / f"{keys.UNIT}_time.json")
        open_ckpt = (rroot / "ckpt" / f"{keys.UNIT}_time.json").read_bytes()
        rc_rn, _o, err_rn = stub_run(rroot, stub())
        made_ad.clear()
        rc_ry, out_ry, _e = stub_run(rroot, stub(), True)
        ck_ry = rs.read_checkpoint(rroot / "ckpt" / f"{keys.UNIT}_time.json")
        n_calls = len(made_ad[0].calls) if made_ad else None
        chk("mf3_sessions: time --resume reaches the stage -- a stub run interrupted in A3 leaves A1-A2s recorded; "
            "without --resume the stage refuses the checkpoint (exit 4, 'CHECKPOINT EXISTS'); with it only A3 and A3s "
            "are launched and the stage ends PASS (exit 0)",
            isinstance(rc_ri, stages._Interrupt) and [r["template"] for r in ck_ri["sessions"]] == list(keys.TEMPLATES[:4])
            and rc_rn == 4 and "CHECKPOINT EXISTS" in err_rn and rc_ry == 0
            and [r["template"] for r in ck_ry["sessions"]] == list(keys.TEMPLATES)
            and (ck_ry.get("stage_end") or {}).get("status") == "PASS"
            and sum(ln.startswith("time A") for ln in out_ry.splitlines()) == 2 and n_calls is not None and n_calls > 0,
            (type(rc_ri).__name__, rc_rn, rc_ry, n_calls))
        # the exit code is the stage's status's (stages.EXIT_CODES)
        ex_codes = {st_: stub_run(fresh(f"exit_{st_}"), stub(), stage=lambda *a, _s=st_, **k: {"status": _s})[0]
                    for st_ in ("PASS", "STOP")}
        chk("mf3_sessions: time's exit code is stages.EXIT_CODES of the stage's status (PASS 0, STOP 4)",
            ex_codes == {"PASS": 0, "STOP": 4} == {k: stages.EXIT_CODES[k] for k in ("PASS", "STOP")}, ex_codes)
        ended_ckpt = ck_p.read_bytes()
        # an end pending: a stub run killed after its end was written pending and its outputs, before the end was
        # persisted (m's cut_at_end, carried: the first checkpoint write carrying a stage_end dies)
        from valence_core.m import resume as m_res
        real_w = m_res.write_checkpoint
        cut = {"n": 0}

        def w_cut(path, ck):
            if cut["n"] == 0 and ck.get("stage_end") is not None:
                cut["n"] += 1
                raise stages._Interrupt("selftest: killed before the end was persisted")
            real_w(path, ck)
        proot = fresh("pending")
        with mock.patch.object(m_res, "write_checkpoint", w_cut):
            rc_p, _o, _e = stub_run(proot, stub())
        pend_p = proot / "ckpt" / f"{keys.UNIT}_time.json"
        pending_ckpt = pend_p.read_bytes()
        chk("mf3_sessions: a stub run cut between its outputs and its persisted end leaves a checkpoint with an end "
            "pending (rs.pending_at) and not ended (the precheck's pending case below reads it)",
            isinstance(rc_p, stages._Interrupt) and cut["n"] == 1 and rs.pending_at(pend_p)
            and json.loads(pending_ckpt).get("stage_end") is None, (type(rc_p).__name__, cut["n"]))

    # --- the Qwen path with the loader and the stage trapped -------------------------------------------
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)

        def fresh(nm: str) -> Path:
            r = base / nm / "mf3"
            schedule.write_schedule_files(r / "schedules")
            return r

        def time_q(nm: str, over: dict | None = None, *, setup=None, pre=(), lic=None, resume_flag=False,
                   argv_pre=(), drv=([], "d" * 64), snap=([], fake_snap), snapfn=None, loader=None, more=(),
                   offline_unset=False):
            # drv / snap: the driver check's and the snapshot check's stubs (None: the real function); snapfn
            # replaces qwen_snapshot outright (a sequence for the pre- and post-load reads); loader replaces the
            # trap (the post-load cases return a stand-in carrying a model_id); stages.run_gate_stage is a trap
            # throughout, stages.DEFAULT_OUT the test root, m:267's laptop checklist stubbed (``pre``)
            root = fresh(nm)
            if setup is not None:
                setup(root)
            before = tree_state(root)
            fl = {**tflags, **(over or {})}
            fl = {k: (str(root / "loop_a.md") if v == "@loop" else v) for k, v in fl.items()}
            argv = list(argv_pre) + ["time"] + [x for k, v in fl.items() if v is not None
                                                for x in ("--" + k.replace("_", "-"), v)]
            n0, s0 = len(loads), len(stage_calls)
            with contextlib.ExitStack() as st:
                st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", root))
                st.enter_context(mock.patch.object(stages, "run_gate_stage", t_stage))
                st.enter_context(mock.patch.object(guard, "preflight_laptop", lambda: list(pre)))
                st.enter_context(gpatch("_load_qwen", t_loader if loader is None else loader))
                st.enter_context(gpatch("build_schedules", t_escape("build_schedules")))
                st.enter_context(gpatch("run_selftest", t_escape("run_selftest")))
                if drv is not None:
                    st.enter_context(gpatch("driver_problems", lambda: (list(drv[0]), drv[1])))
                if snapfn is not None:
                    st.enter_context(gpatch("qwen_snapshot", snapfn))
                elif snap is not None:
                    st.enter_context(gpatch("qwen_snapshot", lambda: (list(snap[0]), snap[1])))
                if lic is not None:
                    st.enter_context(mock.patch.object(stages, "licence_problems", lambda extra, **kw: list(lic)))
                for obj, attr, val in more:
                    st.enter_context(gpatch(attr, val) if obj is None else mock.patch.object(obj, attr, val))
                if offline_unset:
                    st.enter_context(mock.patch.dict(os.environ))
                    os.environ.pop(HF_OFFLINE_ENV, None)
                rc_, out_, err_ = run3(argv + (["--resume"] if resume_flag else []))
            return {"rc": rc_, "out": out_, "err": err_, "loads": len(loads) - n0, "stages": len(stage_calls) - s0,
                    "same": before == tree_state(root)}

        def t_ckpt(root: Path):
            # an open checkpoint: the stub run interrupted in A3 (four sessions recorded, no end)
            cp = root / "ckpt" / f"{keys.UNIT}_time.json"
            cp.parent.mkdir(parents=True, exist_ok=True)
            cp.write_bytes(open_ckpt)

        def t_pending(root: Path):
            cp = root / "ckpt" / f"{keys.UNIT}_time.json"
            cp.parent.mkdir(parents=True, exist_ok=True)
            cp.write_bytes(pending_ckpt)

        def t_ended(root: Path):
            cp = root / "ckpt" / f"{keys.UNIT}_time.json"
            cp.parent.mkdir(parents=True, exist_ok=True)
            cp.write_bytes(ended_ckpt)

        def t_tamper(root: Path):
            f = root / "schedules" / "Q-F3_time_A1s.json"
            f.write_bytes(f.read_bytes().replace(b'"map": 0', b'"map": 1', 1))

        def t_loop(root: Path):
            (root / "loop_a.md").symlink_to(root / "loop_b.md")
            (root / "loop_b.md").symlink_to(root / "loop_a.md")

        def t_ckpt_loop(root: Path):
            d = root / "ckpt"
            d.mkdir(parents=True, exist_ok=True)
            (d / f"{keys.UNIT}_time.json").symlink_to(d / "loop_x.json")
            (d / "loop_x.json").symlink_to(d / f"{keys.UNIT}_time.json")

        lock_prefix_only = ([], f"the proposal {prop_sha[:16]}... and nothing else\n".encode())
        snap_bad = lambda: real_qs(cache_dir=base / "no-cache-here", environ={HF_OFFLINE_ENV: "1"}, cwd=base)
        t_refused = {
            "missing": (time_q("missing", {"lock_file": None}), "time needs ['--lock-file']"),
            "outside": (time_q("outside", {"proposal_file": str(base / "outside.md")}), "lies outside the repository"),
            "a looping link": (time_q("loop", {"proposal_file": "@loop"}, setup=t_loop), "lies outside the repository"),
            "a looping link as the lock": (time_q("looplock", {"lock_file": "@loop"}, setup=t_loop),
                                           "lies outside the repository"),
            "uncommitted": (time_q("uncommitted", {"proposal_file": "no-such-proposal.md"}), "not committed at HEAD"),
            "other lock": (time_q("otherlock", {"lock_file": "CLAUDE.md"}), "G-TIME-F3 cites LOCK-m-F3.md"),
            "proposal not in lock": (time_q("propnotinlock", {"proposal_file": "CLAUDE.md"}),
                                     "is not named in full in LOCK-m-F3.md's committed text"),
            "lock names the proposal by sha16 only": (time_q("propprefix", more=(
                (stages, "committed", committed_but(TIME_LOCK_FILE, lock_prefix_only)),)),
                "is not named in full in LOCK-m-F3.md's committed text"),
            "a lock-named non-proposal": (time_q("nonprop", {"proposal_file": "data/mf3/schedules/manifest.json"}, lic=[]),
                                          "startup: banner"),
            "malformed": (time_q("malformed", {"analyzer_sha256": "xyz"}), "analyzer_sha256 must be a sha256 hex digest"),
            "licence (d)": (time_q("lic_d", {"analyzer_sha256": z64}), "is not identity_extra's analyzer_sha256"),
            "licence (e)": (time_q("lic_e", {"package_sha256": z64}), "is not identity_extra's package_sha256"),
            "licence (f)": (time_q("lic_f", {"analyzer_sha256": z64}), "does not name analyzer_sha256"),
            "licence (g), offline": (time_q("lic_g", offline_unset=True), "licence: weights: HF_HUB_OFFLINE is None"),
            "renders": (time_q("renders", {"renders_sha16": "0" * 16}, lic=[]), "renders: RENDERS MISMATCH"),
            "preflight": (time_q("preflight", lic=[], pre=("ONE PROCESS: selftest",)), "preflight: ONE PROCESS: selftest"),
            "exists": (time_q("exists", lic=[], setup=t_ckpt), "checkpoint: CHECKPOINT EXISTS"),
            "ended": (time_q("ended", lic=[], setup=t_ended), "checkpoint: STAGE ENDED"),
            "ended --resume": (time_q("ended_r", lic=[], setup=t_ended, resume_flag=True), "checkpoint: STAGE ENDED"),
            "a looping link at the checkpoint": (time_q("ckloop", lic=[], setup=t_ckpt_loop),
                                                 "checkpoint: the checkpoint path does not resolve"
                                                 if sys.version_info < (3, 13) else "checkpoint: CHECKPOINT EXISTS"),
            "schedules": (time_q("sched", lic=[], setup=t_tamper), "schedules: SCHEDULES NOT CLEAN"),
            "startup": (time_q("startup", lic=[], more=((stages, "startup_problems",
                                                         lambda proposal_path=None: ["selftest startup"]),)),
                        "startup: selftest startup"),
            "gate line": (time_q("gl", lic=[], more=((stages, "gate_line",
                                                       lambda name, proposal_path=None: ("GATE x", ["GATE LINE: selftest"])),)),
                          "gate line: GATE LINE: selftest"),
            "gate line analyzer": (time_q("gl_an", lic=[], more=((stages, "ANALYZER_PATH", base / "nope.py"),)),
                                   "gate line: analyzer"),
            "gate line CLAUDE.md": (time_q("gl_cm", lic=[], more=((stages, "committed", committed_but(
                "CLAUDE.md", (["CLAUDE.md: selftest uncommitted"], None))),)), "gate line: CLAUDE.md CLAUDE.md: selftest"),
            "driver": (time_q("driver", lic=[], drv=(["selftest: uncommitted edits"], None)),
                       "driver: selftest: uncommitted edits"),
            "driver (real check)": (time_q("driver_real", lic=[], drv=None, more=(
                (stages, "committed", committed_but(DRIVER_REL, (["selftest: driver uncommitted"], None))),
                (None, "__file__", str(REPO / DRIVER_REL)))), "driver: selftest: driver uncommitted"),
            "driver (a copy running)": (time_q("driver_copy", lic=[], drv=None, more=((None, "__file__",
                                                                                       str(base / "copy.py")),)),
                                        "driver: this process runs"),
            "driver (a same-name copy elsewhere)": (time_q("driver_samename", lic=[], drv=None, more=((
                None, "__file__", str(base / "elsewhere" / DRIVER_REL)),)), "driver: this process runs"),
            "snapshot": (time_q("snapshot", lic=[], snap=(["selftest: no snapshot"], None)),
                         "snapshot: selftest: no snapshot"),
            "snapshot (real check)": (time_q("snapshot_real", lic=[], snap=None, snapfn=snap_bad),
                                      "snapshot: no readable refs/main"),
            "snapshot revision not the lock's": (time_q("snaprev", lic=[], snap=([], dict(fake_snap, revision="e" * 40))),
                                                 "not the lock's weights revision"),
            "top-level --out": (time_q("topout", lic=[], argv_pre=("--out", str(base / "x"))),
                                "time takes no --selftest / --build-schedules / --out"),
            "--selftest": (time_q("topsel", lic=[], argv_pre=("--selftest",)),
                           "time takes no --selftest / --build-schedules / --out"),
            "--build-schedules": (time_q("topbuild", lic=[], argv_pre=("--build-schedules",)),
                                  "time takes no --selftest / --build-schedules / --out"),
        }
        bad_t = {k: (v[0]["rc"], v[0]["err"][-240:]) for k, v in t_refused.items()
                 if not (v[0]["rc"] == 2 and any(x in v[0]["err"] for x in (v[1] if isinstance(v[1], tuple) else (v[1],)))
                         and "refused" in v[0]["err"].lower()
                         and "refused" not in v[0]["out"].lower() and v[0]["loads"] == 0 and v[0]["stages"] == 0
                         and "DRIVER " not in v[0]["out"] and "SNAPSHOT " not in v[0]["out"]
                         and not (k.startswith("ended") and "CHECKPOINT EXISTS" in v[0]["err"])
                         and v[0]["same"] and not labelled(v[0]["out"] + v[0]["err"]))}
        chk(f"mf3_sessions: time refuses before the load (exit 2, the refusal on stderr and not stdout, no DRIVER or "
            f"SNAPSHOT line, the loader and the stage never reached, the test root unchanged, no label printed) in "
            f"{len(t_refused)} cases: a flag "
            f"missing; a file outside the repository, a looping link as the proposal or the lock, or uncommitted; a "
            f"lock other than LOCK-m-F3.md; "
            f"a proposal the lock does not name, or names by its sha16 only; a lock-named file that is not a proposal; "
            f"a malformed hash; the licence's (d), (e), (f) and (g)'s offline condition; the renders; m:267's "
            f"checklist; an existing checkpoint without --resume; an ENDED one, with or without --resume (with no "
            f"CHECKPOINT EXISTS advice); a looping "
            f"link at the checkpoint path; a tampered schedule; the run-time known answers; the gate line's own "
            f"problems, its analyzer, and CLAUDE.md uncommitted; the driver check, stubbed, real, and on a copy "
            f"running (another name, or the driver's own name elsewhere); the snapshot check, stubbed and real, and a "
            f"snapshot revision not the lock's; a top-level --out, --selftest or --build-schedules beside time (m's "
            f"form, exactly, on stderr; the schedules writer and the self-test never reached)",
            not bad_t and len(t_refused) == 35 and not escapes
            and all(t_refused[k][0]["err"] == "refused: time takes no --selftest / --build-schedules / --out\n"
                    for k in ("top-level --out", "--selftest", "--build-schedules")), (bad_t, escapes))
        multi = time_q("multi", {"renders_sha16": "0" * 16}, lic=["selftest licence"], pre=("ONE PROCESS: selftest",),
                       drv=(["selftest: uncommitted edits"], None), snap=(["selftest: no snapshot"], None))
        ref_lines = [ln for ln in multi["err"].splitlines() if ln.startswith("REFUSED")]
        chk("mf3_sessions: the precheck's problems (the licence's, the renders', m:267's checklist's), the driver "
            "check's and the snapshot check's are refused together, in one REFUSED line naming the stage (exit 2; no "
            "DRIVER or SNAPSHOT line; nothing loaded; m's multi case)",
            multi["rc"] == 2 and len(ref_lines) == 1 and multi["err"].count("REFUSED: G-TIME-F3:") == 1
            and all(x in ref_lines[0] for x in (
                "licence: selftest licence", "renders: RENDERS MISMATCH", "preflight: ONE PROCESS: selftest",
                "driver: selftest: uncommitted edits", "snapshot: selftest: no snapshot"))
            and "DRIVER " not in multi["out"] and "SNAPSHOT " not in multi["out"] and multi["loads"] == 0, ref_lines)
        # the out root seam: given without a factory, refused before anything -- with the traps in place
        n0, s0 = len(loads), len(stage_calls)
        e_ = io.StringIO()
        with contextlib.ExitStack() as st:
            st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", fresh("seam_default")))
            st.enter_context(mock.patch.object(stages, "run_gate_stage", t_stage))
            st.enter_context(mock.patch.object(guard, "preflight_laptop", lambda: []))
            st.enter_context(gpatch("_load_qwen", t_loader))
            st.enter_context(contextlib.redirect_stderr(e_))
            st.enter_context(contextlib.redirect_stdout(io.StringIO()))
            rc_or = run_time(**{**tflags, "lock_file": "CLAUDE.md"}, resume_run=False, out_root=fresh("seam"))
        chk("mf3_sessions: run_time with an out root and no stub factory refuses before anything -- before the identity "
            "(given a lock the identity would refuse, the refusal is the out root's) -- exit 2, the loader and the "
            "stage, trapped, never reached: the Qwen run writes data/mf3 only",
            rc_or == 2 and "an out root names a test directory" in e_.getvalue() and "cites" not in e_.getvalue()
            and len(loads) == n0 and len(stage_calls) == s0, e_.getvalue()[-200:])
        # every pre-load check clear: the DRIVER and SNAPSHOT lines on stdout, then the trapped loader (a STOP, exit 4)
        rl = time_q("reach_load", lic=[])
        lines_l = rl["out"].splitlines()
        drv_i = next((i for i, x in enumerate(lines_l) if x.startswith("DRIVER ")), None)
        snp_i = next((i for i, x in enumerate(lines_l) if x.startswith("SNAPSHOT ")), None)
        chk("mf3_sessions: with every pre-load check clear, time prints on stdout the DRIVER line (the driver's path and "
            "sha256, HEAD, in full) and then the SNAPSHOT line, and only then reaches the loader -- here the trap: STOP "
            "on stderr, exit 4, the stage never reached, the test root unchanged",
            rl["rc"] == 4 and rl["loads"] == 1 and rl["stages"] == 0 and rl["same"] and drv_i is not None
            and snp_i is not None and drv_i < snp_i
            and lines_l[drv_i] == f"DRIVER {DRIVER_REL} {'d' * 64}: committed at HEAD {stages._git_head()}, working tree identical"
            and lines_l[snp_i] == snapshot_line(fake_snap) and "STOP: selftest: the Qwen loader was reached" in rl["err"]
            and "STOP" not in rl["out"], (rl["rc"], rl["loads"], rl["err"][-200:]))
        ra = time_q("abs_paths", {"proposal_file": str(REPO / stages.PROPOSAL_REL), "lock_file": str(REPO / TIME_LOCK_FILE)},
                    lic=[])
        rr = time_q("resume_open", lic=[], setup=t_ckpt, resume_flag=True)
        rp = time_q("pending", lic=[], setup=t_pending)
        chk("mf3_sessions: absolute flag paths inside the repository are accepted (the identity takes their repo-relative "
            "form); --resume lets an existing open checkpoint through the precheck; and a checkpoint with an end "
            "pending passes without --resume (it only re-finishes): each reaches the loader (the trap; exit 4)",
            all(x["rc"] == 4 and x["loads"] == 1 and x["stages"] == 0 and "the Qwen loader was reached" in x["err"]
                for x in (ra, rr, rp)), [(x["rc"], x["err"][-120:]) for x in (ra, rr, rp)])

        # after the load: the order, the re-read, the revision and the model id
        class Stand:
            def __init__(self, mid):
                self.model_id = mid
        order: list = []

        def seq(*answers):
            it = iter(answers)

            def f():
                order.append("snap")
                return next(it)
            return f

        def stand_loader(mid=QWEN_MODEL_ID):
            def f():
                order.append("load")
                return Stand(mid)
            return f
        moved = dict(fake_snap, revision="e" * 40)
        post = {
            "re-read refuses": (time_q("post_refuse", lic=[], loader=stand_loader(),
                                       snapfn=seq(([], fake_snap), (["selftest: gone"], None))),
                                ("STOP: SNAPSHOT RE-READ REFUSED", "selftest: gone")),
            "refs/main moved": (time_q("post_moved", lic=[], loader=stand_loader(),
                                       snapfn=seq(([], fake_snap), ([], moved))),
                                ("STOP: SNAPSHOT MOVED", f"before the load {lock_rev}; after it {'e' * 40}")),
            "another model id": (time_q("post_mid", lic=[], loader=stand_loader("other/model"),
                                        snapfn=seq(([], fake_snap), ([], fake_snap))),
                                 ("STOP: MODEL ID", f"the adapter loaded 'other/model', the snapshot check read "
                                                    f"'{QWEN_MODEL_ID}'")),
        }
        bad_post = {k: (v[0]["rc"], v[0]["err"][-200:]) for k, v in post.items()
                    if not (v[0]["rc"] == 4 and all(x in v[0]["err"] for x in v[1]) and v[0]["stages"] == 0
                            and v[0]["same"] and "SNAPSHOT re-read after the load: unchanged" not in v[0]["out"])}
        order.clear()
        ru = time_q("post_ok", lic=[], loader=stand_loader(), snapfn=seq(([], fake_snap), ([], fake_snap)))
        chk("mf3_sessions: after the load, a re-read that refuses, a moved refs/main or another model id STOPs (exit 4) "
            "before the stage, each STOP naming its evidence (the re-read's problems; both revisions, in order; both "
            "model ids), with no re-read line; with the snapshot unchanged and the model of record, the order is "
            "snapshot, load, "
            "re-read, the re-read line is printed and the stage is reached (here the trap)",
            not bad_post and ru["rc"] == 4 and ru["stages"] == 1 and ru["same"] and order == ["snap", "load", "snap"]
            and f"SNAPSHOT re-read after the load: unchanged ({lock_rev}); adapter model_id {QWEN_MODEL_ID}" in ru["out"]
            and "STOP: selftest: the stage was reached" in ru["err"], (bad_post, ru["rc"], order, ru["err"][-200:]))
        # the real driver check on this file
        dp, dsha = driver_problems()
        cp_d, blob_d = stages.committed(DRIVER_REL)
        here_ok = Path(__file__).resolve() == (REPO / DRIVER_REL).resolve()
        chk("mf3_sessions: driver_problems on this driver -- clear with the committed blob's sha256 exactly when this "
            "process runs the driver of record and its working tree is HEAD's; else its problems and no sha",
            (dp == [] and here_ok and cp_d == [] and blob_d is not None and dsha == hashlib.sha256(blob_d).hexdigest())
            or (dp != [] and dsha is None and (not here_ok or cp_d != [])), (dp[:1], cp_d[:1], here_ok))
    data_after = tree_state(real_out) if real_out.is_dir() else {}
    chk("mf3_sessions: the time checks loaded nothing and wrote nothing under data/mf3 -- the loader trap was reached "
        "4 times in all (each of the four cases that clear every pre-load check asserts its own one reach), the stage "
        "trap once (the post-load case that reaches it), the schedules writer and the self-test never from a time "
        "invocation; data/mf3's file "
        "hashes are unchanged and stages.DEFAULT_OUT is restored",
        data_before == data_after and stages.DEFAULT_OUT == real_out and len(loads) == 4 and len(stage_calls) == 1
        and not escapes, (len(loads), len(stage_calls), escapes, sorted(set(data_before) ^ set(data_after))[:3]))


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
    ap = argparse.ArgumentParser(description="PROPOSAL-m Q-F3 driver (self-test, schedules, hashes, G-SHAPE-F3, "
                                             "G-TIME-F3; id, qual and campaign are refused until their steps)")
    ap.add_argument("--selftest", action="store_true", help="model-free self-test of valence_core.mf3")
    ap.add_argument("--build-schedules", action="store_true", help="write Q-F3's schedule files + manifest")
    ap.add_argument("--out", default=None, help="output directory for --build-schedules")
    sub = ap.add_subparsers(dest="cmd")
    g = sub.add_parser("gshape", help="G-SHAPE-F3 (m:290), model-free; canonical without --out")
    g.add_argument("--out", dest="gshape_out", default=None, help="a test directory (never of record)")
    h = sub.add_parser("hashes", help="the hashes LOCK-m-F3 v0.1 names (Q1 (C2)) and the weights binding")
    h.add_argument("--snapshot-dir", default=None, help="the hub snapshot directory (default: the cache's of record)")
    t = sub.add_parser("time", help="G-TIME-F3 (m:293): six sessions on Qwen, uncached, under LOCK-m-F3 v0.1; the "
                                    "flags are the lock's values (lock §1)")
    for k in TIME_FLAGS:
        t.add_argument("--" + k.replace("_", "-"), default=None, help=TIME_FLAG_HELP[k])
    t.add_argument("--resume", action="store_true", help="continue G-TIME-F3's checkpoint (skip-only)")
    for c in REFUSED_CMDS:
        sub.add_parser(c, help=f"{STAGE_NAMES[c]}: refused until its step")
    try:
        a = ap.parse_args(argv)
    except SystemExit as e:
        return int(e.code) if isinstance(e.code, int) else 2
    if a.cmd == "time" and (a.selftest or a.build_schedules or a.out is not None):
        print(f"refused: {a.cmd} takes no --selftest / --build-schedules / --out", file=sys.stderr)   # m's form
        return 2
    if a.selftest:
        return run_selftest()
    if a.build_schedules:
        return build_schedules(a.out)
    if a.cmd == "gshape":
        return run_gshape(a.gshape_out)
    if a.cmd == "hashes":
        return hashes(a.snapshot_dir)
    if a.cmd == "time":
        return run_time(proposal_file=a.proposal_file, lock_file=a.lock_file, analyzer_sha256=a.analyzer_sha256,
                        package_sha256=a.package_sha256, renders_sha16=a.renders_sha16, resume_run=a.resume)
    if a.cmd in REFUSED_CMDS:
        print(refusal(a.cmd), flush=True)
        return 2
    print("REFUSED: no action (--selftest, --build-schedules, hashes, gshape or time)", flush=True)
    return 2


if __name__ == "__main__":
    sys.exit(main())
