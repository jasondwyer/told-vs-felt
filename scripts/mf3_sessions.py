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
  time --smoke --smoke-out DIR (with time's five flags)
                      ADDENDUM-m2's smoke (A-m2 §3.2), never of record: twelve sham sessions, A-m2 §3.1's four
                      reasoning-block forms over A1s, A2s and A3s, on G-TIME-F3's committed cells and item key under
                      the arm key m-smoke-f3|{form}|{template}|0, uncached, cap 60, each record through G-VER; the
                      rule's counts (A-m2 §1, §3.3, §3.4) printed. It writes only DIR, a new directory outside the
                      repository, checked before the load, again before it is made, and before every write; it
                      never names, opens or creates the stage's checkpoint. Exit 0 complete, 2 refused before the
                      load, 4 STOP (a STOP selects nothing: no tally, no rule, and no summary.json unless its
                      rename and its removal both fail or it cannot be examined, which the STOP line says; what a
                      failed summary write left is touched only while DIR is the directory the smoke made; A-m2
                      v0.3 §3.3).

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
import dataclasses
import errno
import hashlib
import importlib
import io
import json
import os
import re
import stat
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from valence_core.mf3 import gshape, guard, keys, schedule, stages  # noqa: E402
from valence_core.mf3 import resume as rs  # noqa: E402
from valence_core.m import audit as m_audit  # noqa: E402
from valence_core.m import corr as m_corr  # noqa: E402
from valence_core.mf3 import banner, runner, verify  # noqa: E402
from valence_core.mf3 import scaffold as sc_mod  # noqa: E402

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


# --- ADDENDUM-m2's smoke (A-m2 §3.1-§3.4; never of record) ------------------------------------------------------
# PIN (Code, declared in the A-m2 pre-read, P4, accepted by the seat (ans2 §3); A-m2 v0.3 §3.2, §4.2: "a committed
# driver with a `--smoke` form that refuses to write under `data/`"): `time --smoke --smoke-out DIR` runs A-m2 §3.2's
# twelve sham sessions. The forms F-0, F-a, F-b and F-c (A-m2 §3.1) are this driver's constants, checked at the run
# against A-m2 v0.3's committed text, its sha256 pinned (v0.3 §4.2; ans3 §1, #48). They run over A1s, A2s and A3s,
# form-major. Each session
# runs on G-TIME-F3's committed schedule cell (s = 0), with G-TIME-F3's item key and the arm key
# m-smoke-f3|{form}|{template}|0, uncached, at reasoning cap 60, through runner.run_session_f3 unchanged. The
# scaffold differs from mf3's only in reasoning(ci), which returns the form's bytes at the menu's n after
# F3Scaffold.reasoning has drawn the seed (m:159's draw order kept). G-VER runs on every record, with one
# substitution: the scaffold it builds (verify.py:79's scaffold.f3_config) is the smoke's. Nothing is written inside
# the repository, so nothing under data/; the stage's checkpoint is never named, opened or created; nothing is of
# record.
#: A-m2 v0.3 §4.2 (ans3 §1, #48): the driver pins the committed A-m2's sha256, this version's, and parses §3.1's
#: four literals from it.
ADDENDUM_M2_VERSION = "v0.3"
ADDENDUM_M2_REL = "ADDENDUM-m2-f3-reasoning-block-v0_3.md"
ADDENDUM_M2_SHA256 = "83093812afdd513a9522024e8b766254e47d9aa226d5894577baf69855d9fa67"
SMOKE_NAME = "A-m2 smoke"
#: A-m2 §3.1's four forms, in §3.1's order (the run order), each replacing m:174's block; {n} is the menu's n.
SMOKE_FORMS = (("F-0", "[round {n} | reasoning]\nReasoning (one line):\n"),
               ("F-a", "[round {n} | reasoning]\nReasoning (one line):"),
               ("F-b", "[round {n} | reasoning]\nReasoning (one line): So far,"),
               ("F-c", "[round {n} | reasoning]\nGive one line of reasoning.\n"))
#: A-m2 §3.2: "one session per sham template per form -- A1s (TOLD-MAP-SHAM), A2s (TOLD-OBJ), A3s (COMMON)".
SMOKE_TEMPLATES = ("A1s", "A2s", "A3s")
SMOKE_ARM_KEY = "m-smoke-f3|{form}|{template}|0"
SMOKE_STAGE = "time"            # the cells, the item key, the uncached path and the cap are G-TIME-F3's
SMOKE_S = 0
SMOKE_ITEM_KEY = keys.item_key(SMOKE_S, keys.item_gate(SMOKE_STAGE))          # "m-f3-items-time|0"
#: A-m2 §3.2: "Qwen, the backend of record (a734dadec8f8ce9b)" -- a non-stub smoke on another backend STOPs.
SMOKE_BACKEND = "a734dadec8f8ce9b"
#: A-m2 v0.3 §3.3: "Among the selectable forms, F-a and F-b, select the one with the fewest (i); ties by fewest (ii),
#: then the smaller departure from m:174: F-a before F-b." F-0 is the control and F-c a diagnostic arm (ans2 §7).
SMOKE_SELECTABLE = ("F-a", "F-b")
SMOKE_STOP_DEFECTS = 3          # A-m2 v0.3 §3.3's two stops: F-0 below 3 defect lines; the selected form at 3 or more
#: A-m2 v0.3 §3.3 (ans2 §2, Q2 (U)): (i) is the bar's numerator, the union of m:265's three classes (the tally's key).
SMOKE_I_KEY = "union"
SMOKE_FRAME_RX = re.compile(r"=== .+? ===")                                   # counter (a)'s frame (P2)
SMOKE_HARNESS_KINDS = ("banner", "round", "joiner", "menu", "pick", "reasoning", "reasoning_joiner")
SMOKE_MODEL_KINDS = ("generation", "reasoning_text")
_A_M2_BULLET_RX = re.compile(r"^- \*\*(F-[0-9a-z]+) \([^)\n]*\):\*\* `([^`\n]+)`")


def addendum_m2_text_problems(data: bytes, *, check_sha: bool = True) -> list[str]:
    """A-m2's bytes against the pin and §3.1's four bullets against SMOKE_FORMS; [] = clean. Each bullet's
    backticked literal is read with its escaped ``\\n`` as a newline."""
    if check_sha and hashlib.sha256(data).hexdigest() != ADDENDUM_M2_SHA256:
        return [f"{ADDENDUM_M2_REL}: its sha256 is not the pinned {ADDENDUM_M2_VERSION}'s ({ADDENDUM_M2_SHA256[:16]}...)"]
    got: dict[str, list[str]] = {}
    for ln in data.decode("utf-8", "replace").split("\n"):
        m = _A_M2_BULLET_RX.match(ln)
        if m:
            got.setdefault(m.group(1), []).append(m.group(2).replace("\\n", "\n"))
    probs = [f"A-m2 §3.1: form {f} parses as {got.get(f)!r}; the driver's is {b!r}"
             for f, b in SMOKE_FORMS if got.get(f) != [b]]
    extra_forms = sorted(set(got) - {f for f, _ in SMOKE_FORMS})
    if extra_forms:
        probs.append(f"A-m2 §3.1: forms {extra_forms} are not the driver's")
    return probs


def addendum_m2_problems() -> list[str]:
    """A-m2 committed at HEAD with the working tree's bytes (stages.committed), then its text's problems."""
    cp, data = stages.committed(ADDENDUM_M2_REL)
    if cp or data is None:
        return list(cp) or [f"{ADDENDUM_M2_REL}: unreadable"]
    return addendum_m2_text_problems(data)


class SmokeScaffold(sc_mod.F3Scaffold):
    """mf3's F3 scaffold with one of A-m2 §3.1's reasoning blocks (the smoke only)."""

    def __init__(self, *, form: str, **kw) -> None:
        if form not in dict(SMOKE_FORMS):
            raise ValueError(f"not an A-m2 form: {form!r}")
        super().__init__(**kw)
        self._form_bytes = dict(SMOKE_FORMS)[form]

    def reasoning(self, ci: int):
        rs_ = super().reasoning(ci)        # the seed drawn and the order checked as mf3 does
        return dataclasses.replace(rs_, seg=self._form_bytes.replace("{n}", str(rs_.n)))


def smoke_config(form: str, template: str, cell, *, pool=None, renders=None) -> SmokeScaffold:
    """f3_config's construction for G-TIME-F3's session s = 0, with the smoke's arm key and the form's block."""
    if template not in SMOKE_TEMPLATES:
        raise ValueError(f"the smoke runs {SMOKE_TEMPLATES} only (A-m2 §3.2), not {template!r}")
    c = sc_mod.check_cell(template, cell)
    if pool is None or renders is None:
        p0, r0 = sc_mod.pool_and_renders()
        pool = p0 if pool is None else pool
        renders = r0 if renders is None else renders
    arm = SMOKE_ARM_KEY.format(form=form, template=template)
    contrast = keys.is_contrast(template)
    text, note_lines = banner.build_banner(template, c["P"], c["Q"], c["clause"])
    meta = {"substrate": "qwen", "unit": keys.UNIT, "stage": SMOKE_STAGE, "template": template,
            "contrast": contrast, "path": "uncached", "j": SMOKE_S,
            "keys": {"arm": arm, "items": SMOKE_ITEM_KEY}, "format": sc_mod.FORMAT}
    return SmokeScaffold(form=form, reasoning_cap=TIME_REASONING_CAP, banner=text, cell=c, s=SMOKE_S,
                         arm_rng=keys.stream(arm), items=m_corr.ItemStreams(keys.stream(SMOKE_ITEM_KEY)),
                         delivery=m_corr.Delivery(pool, renders, contrast=contrast), note_lines=note_lines,
                         meta=meta)


def smoke_verify(rec, form: str, cell, *, pool, renders, scaffold_strings) -> list[str]:
    """G-VER on a smoke record: verify.verify_session with scaffold.f3_config answering, for that one session,
    with the smoke's scaffold (restored on return)."""
    template = rec.get("template") if isinstance(rec, dict) else None

    def cfg(stage, tpl, s, schedule_cell, path, *, reasoning_cap, pool=None, renders=None):
        if (stage, tpl, s, path, reasoning_cap) != (SMOKE_STAGE, template, SMOKE_S, "uncached", TIME_REASONING_CAP):
            raise ValueError("not the smoke's session")
        return smoke_config(form, tpl, schedule_cell, pool=pool, renders=renders)

    real = sc_mod.f3_config
    sc_mod.f3_config = cfg
    try:
        return verify.verify_session(rec, pool=pool, renders=renders, schedule_cell=cell,
                                     scaffold_strings=scaffold_strings)
    finally:
        sc_mod.f3_config = real


def smoke_harness_lines(rec, ci: int) -> tuple[str, ...]:
    """P1: the complete harness-written lines of the session as rendered up to reasoning line ``ci`` (A-m2 §1).

    PIN (Code, declared in the A-m2 pre-read, P1; A-m2 §1, m:265): over the record's pieces, which tile the
    transcript, the span before line ci's reasoning_text piece splits into newline-terminated lines; a line is
    in the domain iff no model-written piece (generation, reasoning_text) touches it: none overlaps any of its
    characters, its newline included, and no zero-length one sits within it. A model text can hold a newline (the
    adapter's stop rule does not stop on a first token that carries content and a newline together), so overlap,
    not a piece's start, decides. Every other piece kind is the harness's. An unterminated final fragment is not a
    complete line. The distinct lines, in first-occurrence order, each non-empty after ws_norm (asserted)."""
    pieces, t = rec["pieces"], rec["transcript"]
    kinds = {p["kind"] for p in pieces}
    if not kinds <= set(SMOKE_HARNESS_KINDS + SMOKE_MODEL_KINDS):
        raise ValueError(f"unknown piece kinds {sorted(kinds - set(SMOKE_HARNESS_KINDS + SMOKE_MODEL_KINDS))}")
    texts = [p for p in pieces if p["kind"] == "reasoning_text"]
    upto = texts[ci]["start"]
    spans = [(p["start"], p["end"]) for p in pieces if p["kind"] in SMOKE_MODEL_KINDS]
    out: list[str] = []
    seen: set[str] = set()
    a = 0
    while True:
        b = t.find("\n", a, upto)
        if b < 0:
            break
        if not any(ps <= b and (pe > a if pe > ps else ps >= a) for ps, pe in spans):
            k = m_audit.ws_norm(t[a:b])
            if not k:
                raise ValueError(f"an empty harness line at {a}")
            if k not in seen:
                seen.add(k)
                out.append(t[a:b])
        a = b + 1
    return tuple(out)


def smoke_line_reads(rec) -> list[dict]:
    """Per reasoning line: the record's empty / cap classes, P1's echo (A-m2 §1: verbatim equality after ws_norm,
    case-sensitive) and counter (a) (P2: containment of a domain line, or the banner's frame)."""
    out = []
    for ci, x in enumerate(rec.get("reasoning") or ()):
        dom = smoke_harness_lines(rec, ci)
        t = m_audit.ws_norm(x["text"])
        echo = next((i for i, ln in enumerate(dom) if m_audit.ws_norm(ln) == t), None)
        contains = any(m_audit.ws_norm(ln) in t for ln in dom)
        frame = bool(SMOKE_FRAME_RX.search(t))
        kept = [c for c in (x.get("audit") or {}).get("classes") or () if c in ("empty", "cap_no_newline")]
        classes = kept + (["echo"] if echo is not None else [])
        out.append({"ci": ci, "n": x["n"], "text": x["text"], "classes": classes, "echo_index": echo,
                    "echo_line": dom[echo] if echo is not None else None, "counter_a": contains or frame,
                    "contains": contains, "frame": frame, "package_classes": list((x.get("audit") or {}).get("classes") or ()),
                    "scaffold": list((x.get("audit") or {}).get("scaffold") or ()), "domain_size": len(dom)})
    return out


def _within(r: Path, root: Path) -> bool:
    """Whether ``r`` is ``root`` or lies under it, by spelling and by file identity: on a case-insensitive volume
    another spelling names the same directory (the smoke review's round-1 MINOR-1). The deepest ancestor of ``r`` that
    can be examined, and each of its parents, are compared with ``root`` by ``os.path.samefile``; a component that
    cannot be examined (EACCES) is stepped over, never raised."""
    root = Path(root).resolve()
    if r == root or root in r.parents:
        return True
    q = r
    while q != q.parent:
        try:
            if q.exists():
                break
        except OSError:
            pass
        q = q.parent
    for a in (q, *q.parents):
        try:
            if os.path.samefile(a, root):
                return True
        except OSError:
            continue
    return False


def _within_repo(r: Path) -> bool:
    return _within(r, REPO)


def _lstat_state(p: Path) -> tuple[str, str | None]:
    """('absent' | 'present' | 'unexaminable', the error's name) for one spelling, by ``os.lstat``: a link is present,
    dangling or not. The same answer on every Python version (``Path.exists`` returns False on EACCES under 3.14,
    where 3.12 and 3.13 raise; the smoke review's round-3 NOTE 5)."""
    try:
        os.lstat(p)
    except (FileNotFoundError, NotADirectoryError):
        return "absent", None
    except OSError as e:
        return "unexaminable", type(e).__name__
    return "present", None


def smoke_out_problems(smoke_out) -> tuple[Path | None, list[str]]:
    """(the resolved output directory, problems): it must lie outside the repository (so outside data/, A-m2 §3.2),
    by spelling and by file identity; it must not exist, neither as given (a link, dangling or not, included: the
    round-3 NOTE 10) nor resolved; its parent must be a writable directory. Classified by ``os.lstat`` and
    ``os.stat`` (round-3 NOTE 5)."""
    if smoke_out is None:
        return None, ["--smoke needs --smoke-out DIR: the smoke writes outside the repository only (A-m2 §3.2)"]
    try:
        given = Path(smoke_out).expanduser()        # an unknown ~user raises here (the smoke review's round-4 MINOR-1)
        r = given.resolve()
    except (OSError, RuntimeError, ValueError) as e:
        return None, [f"--smoke-out {smoke_out}: does not resolve ({type(e).__name__})"]
    if _within_repo(r):
        return None, [f"--smoke-out {smoke_out}: resolves inside the repository; the smoke writes nothing there, so "
                      f"nothing under data/ (A-m2 §3.2)"]
    states = [_lstat_state(given), _lstat_state(r)]
    bad = next((e for s, e in states if s == "unexaminable"), None)
    if bad is not None:
        return None, [f"--smoke-out {smoke_out}: cannot be examined ({bad})"]
    if any(s == "present" for s, _ in states):
        return None, [f"--smoke-out {smoke_out}: exists; the smoke writes a new directory only"]
    try:
        pst = os.stat(r.parent)
    except (FileNotFoundError, NotADirectoryError):
        return None, [f"--smoke-out {smoke_out}: its parent is not a directory"]
    except OSError as e:
        return None, [f"--smoke-out {smoke_out}: cannot be examined ({type(e).__name__})"]
    if not stat.S_ISDIR(pst.st_mode):
        return None, [f"--smoke-out {smoke_out}: its parent is not a directory"]
    if not os.access(r.parent, os.W_OK | os.X_OK):
        return None, [f"--smoke-out {smoke_out}: its parent is not writable"]
    return r, []


def smoke_precheck(extra: dict) -> list[str]:
    """The smoke's refusals that need no model, before the load; [] = none fired. time_precheck's, less the
    checkpoint's (the smoke never names, opens or creates the stage's checkpoint), plus A-m2's (its committed
    sha256 and §3.1's four literals) and the forms' roster hygiene."""
    name = SMOKE_NAME
    probs = [f"licence: {p}" for p in stages.licence_problems(extra)]
    proposal = stages._proposal_path(extra)
    probs += [f"startup: {p}" for p in stages.startup_problems(proposal)]
    try:
        stages._renders_of_record(extra, name)
    except SystemExit as e:
        probs.append(f"renders: {e}")
    try:
        stages.load_committed([(SMOKE_STAGE, t) for t in SMOKE_TEMPLATES], schedule.DEFAULT_OUT)
    except SystemExit as e:
        probs.append(f"schedules: {e}")
    probs += [f"addendum: {p}" for p in addendum_m2_problems()]
    probs += [f"forms: {p}" for p in smoke_form_hygiene()]
    probs += [f"preflight: {p}" for p in guard.preflight_laptop()]
    probs += [f"gate line: {p}" for p in stages.gate_line(name, proposal)[1]]
    for what, path in (("CLAUDE.md", stages.CLAUDE_MD_PATH), ("analyzer", stages.ANALYZER_PATH)):
        rel = _repo_rel(path)
        probs += ([f"gate line: {what} {path} lies outside the repository"] if rel is None
                  else [f"gate line: {what} {x}" for x in stages.committed(rel)[0]])
    return [redact_totals(p) for p in probs]


def smoke_form_hygiene() -> list[str]:
    """m:258's roster admissibility (valence_core.m.corr.hygiene over ROSTERS_OF_RECORD, both rosters, placeholders
    blanked), run on the four forms' bytes as new harness strings (the pre-read's P4); [] = clean."""
    return m_corr.hygiene(m_corr.ROSTERS_OF_RECORD, tuple(b for _, b in SMOKE_FORMS))


def _printable(text: str) -> str:
    """``text`` with every non-printable character, and the backslash itself, escaped as Python's repr writes it (C0,
    C1, DEL, a carriage return; the smoke review's round-1 MINOR-3 and round-2 NOTE 3), so the raw reads back
    unambiguously; the raw prints the transcript line by line, and the JSON keeps the exact bytes."""
    return "".join(c if (c.isprintable() and c != "\\") else repr(c)[1:-1] for c in text)


def smoke_session_lines(k: int, form: str, rec: dict, problems: list[str]) -> list[str]:
    """The raw's block for one smoke session, the record's part: a header line, the transcript line by line (escaped,
    _printable), every task response with its claim and scaffold hits, and every read with its probabilities and
    label-mass flags. Sham sessions outside every unit, printed in full (A-m2 v0.3 §3.2; outside §3.4's blinding scope)."""
    cell, exc = rec["cell"], rec.get("exclusion") or {}
    state = f"excluded {exc.get('class')}@{exc.get('phase')}" if rec["excluded"] else "valid"
    out = [f"SMOKE SESSION {k}/{len(SMOKE_FORMS) * len(SMOKE_TEMPLATES)} {form} {rec['template']}: arm key "
           f"{rec['keys']['arm']}, items {rec['keys']['items']}; pair {cell['pair'][0]}/{cell['pair'][1]}, P {cell['P']}, "
           f"Q {cell['Q']}, start {cell['start']}, clause {cell['clause']}; {state}; complete {rec['complete']}; G-VER "
           f"{'clean' if not problems else problems}; {rec['seconds']:.1f} s"]
    out.append("  transcript:")
    out += ["  | " + _printable(ln) for ln in rec["transcript"].split("\n")]
    for r in rec["rounds"]:
        a = r["audit"]
        out.append(f"  round {r['n']} ({r['phase']}, {r['role']}, item {r['item']}): claim {a['claim']}, advisory "
                   f"{list(a.get('advisory') or ())}, scaffold {list(a.get('scaffold') or ())}, n_tok {r['n_tok']}, "
                   f"{r['stop_reason']}: {r['text']!r}")
    for c in rec["choices"]:
        rd = c.get("read") or {}
        out.append(f"  read {c['n']}: menu {c['menu_a']} / {c['menu_b']}, pick {c['pick']} ({c['picked_role']}); p_a "
                   f"{rd.get('p_a')}, p_b {rd.get('p_b')}, low_label_mass {c.get('low_label_mass')}, top1_not_label "
                   f"{c.get('top1_not_label')}")
    return out


def smoke_reads_lines(reads: list[dict]) -> list[str]:
    """The raw's block for one smoke session, the lines' part: every reasoning line with P1's classes, its echo, its
    counter (a), the package's own classes and its scaffold hits."""
    return [f"  line {x['n']} (ci {x['ci']}): classes {x['classes']}, echo {x['echo_index']} {x['echo_line']!r}, "
            f"(a) {x['counter_a']} (contains {x['contains']}, frame {x['frame']}); package classes "
            f"{x['package_classes']}, scaffold {x['scaffold']}: {x['text']!r}" for x in reads]


def smoke_block(k: int, form: str, template: str, rec: dict, problems: list[str], reads) -> tuple[list[str], list[str]]:
    """(the session's block for the raw, its errors): the record's part, then the lines' part when the reads exist. A
    part that raises is replaced by one line naming the error, so whatever can be printed is printed and the session
    is still written (the smoke review's round-3 NOTE 2); the caller STOPs on any error after the write."""
    out: list[str] = []
    errs: list[str] = []
    try:
        out += smoke_session_lines(k, form, rec, problems)
    except Exception as e:                                      # noqa: BLE001 -- printed, then a STOP
        errs.append(f"the record's part raised {type(e).__name__}: {e}")
        out.append(f"SMOKE SESSION {k}/{len(SMOKE_FORMS) * len(SMOKE_TEMPLATES)} {form} {template}: {errs[-1]}")
    if reads is not None:
        try:
            out += smoke_reads_lines(reads)
        except Exception as e:                                  # noqa: BLE001 -- printed, then a STOP
            errs.append(f"the lines' part raised {type(e).__name__}: {e}")
            out.append(f"  {errs[-1]}")
    return out, errs


def smoke_tally(entries) -> dict:
    """Per form, over every session it ran, excluded ones included: sessions, lines, (i)'s three members and their
    union (A-m2 v0.3 §3.3), (ii) counter (a), and the task responses beside."""
    t = {f: {"sessions": 0, "valid": 0, "complete": 0, "lines": 0, "echo": 0, "empty": 0, "cap": 0, "union": 0,
             "counter_a": 0, "responses": 0, "free_responses": 0} for f, _ in SMOKE_FORMS}
    for form, rec, reads in entries:
        x = t[form]
        x["sessions"] += 1
        x["valid"] += int(not rec["excluded"])
        x["complete"] += int(bool(rec["complete"]))
        for r in reads:
            x["lines"] += 1
            x["echo"] += int("echo" in r["classes"])
            x["empty"] += int("empty" in r["classes"])
            x["cap"] += int("cap_no_newline" in r["classes"])
            x["union"] += int(bool(r["classes"]))
            x["counter_a"] += int(r["counter_a"])
        x["responses"] += len(rec["rounds"])
        x["free_responses"] += sum(r["phase"] == "free" for r in rec["rounds"])
    return t


def smoke_select(tally: dict) -> dict:
    """A-m2 v0.3 §3.3's rule over the tallies: among SMOKE_SELECTABLE, the fewest (i) (the union, SMOKE_I_KEY), ties
    by the fewest (ii) (counter (a)), then the departure order (SMOKE_SELECTABLE's); the two stops read (i). Counter
    (b) breaks no tie (ans2 §1, Q1 (T)); F-0 and F-c are reported, never selected (ans2 §7)."""
    def key(f):
        return (tally[f][SMOKE_I_KEY], tally[f]["counter_a"], SMOKE_SELECTABLE.index(f))

    sel = min(SMOKE_SELECTABLE, key=key)
    stop1 = tally["F-0"][SMOKE_I_KEY] < SMOKE_STOP_DEFECTS
    stop2 = tally[sel][SMOKE_I_KEY] >= SMOKE_STOP_DEFECTS
    return {"selected": sel, "keys": {f: list(key(f)) for f in SMOKE_SELECTABLE}, "stop_uninformative": stop1,
            "stop_selected_defects": stop2, "adopted": None if (stop1 or stop2) else sel}


def _oserr(e: OSError) -> str:
    """An OSError as its class and its errno's name ("OSError ENOSPC"), for the smoke's STOP lines."""
    code = errno.errorcode.get(e.errno) if isinstance(e.errno, int) else None
    return f"{type(e).__name__}{' ' + code if code else ''}"


def _out_dir_moved(out_dir: Path, made) -> list[str]:
    """[] while ``out_dir`` still resolves to itself and is the directory the smoke made (``made``: its os.stat right
    after the mkdir); a path component swapped during the run is refused before the next write (the smoke review's
    round-5 NOTE 2). A swap between this check and the write it guards stays possible; it needs a hand on the path
    within that instant."""
    try:
        now = out_dir.resolve()
        if now != out_dir:
            return [f"it now resolves to {now}, not {out_dir}"]
        if not os.path.samestat(os.stat(out_dir), made):
            return ["it is no longer the directory the smoke made"]
    except (OSError, RuntimeError) as e:
        return [f"it cannot be examined ({type(e).__name__})"]
    return []


def _smoke_write(path: Path, obj, name: str, *, pin=None) -> None:
    """An atomic JSON write through mf3.resume's ``atomic_write_json`` (m's: serialized first, then a temp file,
    fsync, ``os.replace``, the directory's fsync). With ``pin`` (the out directory and its os.stat after the mkdir),
    the directory is checked first, and one that moved is a STOP before anything is written (round-5 NOTE 2). An
    ``OSError`` is a STOP, its errno named and whether the file is on disk said (the smoke review's round-4 NOTE 3: a
    failure after the replace, the directory's fsync, leaves it written); so is an object that does not serialize
    (``TypeError`` / ``ValueError``: a non-native value, NaN, a lone surrogate; round-3 NOTE 1), which leaves no file
    and no temp file."""
    if pin is not None:
        moved = _out_dir_moved(*pin)
        if moved:
            raise SystemExit(f"OUT DIR ({name}): before writing {path.name}: {moved} -- the smoke stops; "
                             f"{path.name} not written")
    try:
        rs.atomic_write_json(path, obj, indent=1)
    except OSError as e:
        try:
            state = f"{path.name} is on disk" if path.exists() else f"{path.name} is not on disk"
        except OSError:
            state = f"whether {path.name} is on disk is unknown"
        raise SystemExit(f"OUT DIR ({name}): {_oserr(e)} writing {path.name}; {state} -- the smoke stops")
    except (TypeError, ValueError) as e:
        raise SystemExit(f"SERIALIZE ({name}): {type(e).__name__} for {path.name}: {e} -- nothing written; the smoke "
                         f"stops")


def _summary_stopped(spath: Path) -> str:
    """The STOP line's tail after a failed summary write. A stopped smoke selects nothing (A-m2 v0.3 §3.3), so a
    summary.json the failed write left on disk (a directory fsync failing after the replace), or the temp file that
    m's cleanup could not remove, is renamed ``.stopped``, or removed if the rename fails; each outcome is said, and
    so is a file whose presence cannot be examined (the smoke review's round-4 NOTE 3 and round-5 NOTE 1)."""
    tails = []
    for p in (spath, spath.with_name(spath.name + ".tmp")):
        try:
            os.lstat(p)
        except (FileNotFoundError, NotADirectoryError):
            continue
        except OSError as e:
            tails.append(f"whether {p.name} is on disk is unknown ({_oserr(e)}): if it is, it is not a selection")
            continue
        stopped = p.with_name(p.name + ".stopped")
        try:
            os.rename(p, stopped)
            tails.append(f"{p.name} renamed {stopped.name}")
            continue
        except OSError as e1:
            err1 = _oserr(e1)
        try:
            os.unlink(p)
            tails.append(f"{p.name} could not be renamed ({err1}) and was removed")
        except OSError as e2:
            tails.append(f"{p.name} is on disk, its rename ({err1}) and its removal ({_oserr(e2)}) failed: it is not "
                         f"a selection")
    return ("; " + "; ".join(tails) + "; a stopped smoke selects nothing (A-m2 v0.3 §3.3)") if tails else ""


def run_smoke_sessions(adapter, extra: dict, out_dir: Path) -> dict:
    """The twelve sessions (A-m2 §3.2), after the load. Every refusal is a SystemExit (the caller's STOP).
    ``out_dir`` is smoke_out_problems' resolved path: the re-check before the mkdir refuses any other (round-5
    NOTE 2)."""
    name = SMOKE_NAME
    proposal = stages._proposal_path(extra)
    stages._startup_checks(name, proposal)
    stages._laptop_preflight(adapter, name, extra)          # m:267's checklist and the gate line (a stub skips it)
    stages._licence(adapter, extra, name)                   # the licence at the smoke's start (a stub skips it)
    probs = addendum_m2_problems() + smoke_form_hygiene()
    if probs:
        raise SystemExit(f"A-m2 ({name}): {probs} -- no session runs")
    print(f"A-M2 {ADDENDUM_M2_REL} {ADDENDUM_M2_SHA256[:16]}: committed at HEAD, working tree identical; §3.1's four "
          f"forms parse equal to the driver's and pass m:258's roster hygiene", flush=True)
    try:
        prov = rs.provenance_record(adapter.provenance())
        bid = rs.backend_identifier(adapter.provenance())
    except (TypeError, ValueError) as e:
        raise SystemExit(f"PROVENANCE ({name}): {type(e).__name__}: {e} -- no session runs")
    print("PROVENANCE: " + json.dumps(prov, sort_keys=True, separators=(",", ":"), ensure_ascii=False), flush=True)
    print(f"BACKEND {bid}", flush=True)
    if not stages._is_stub(adapter) and bid != SMOKE_BACKEND:
        raise SystemExit(f"BACKEND ({name}): {bid} is not the backend of record {SMOKE_BACKEND} (A-m2 §3.2) -- no "
                         f"session runs")
    setup = runner.f3_startup(adapter)
    pool, renders, _ = stages._renders_of_record(extra, name)
    scheds = stages.load_committed([(SMOKE_STAGE, t) for t in SMOKE_TEMPLATES], schedule.DEFAULT_OUT)
    # the smoke review's round-4 NOTE 6: the out directory was checked before the load, minutes ago; it is checked
    # again just before it is made and must still resolve to itself (a directory or a link swapped in meanwhile is
    # refused)
    again, oprobs = smoke_out_problems(str(out_dir))
    if oprobs or again != out_dir:
        raise SystemExit(f"OUT DIR ({name}): re-checked before it is made: "
                         f"{oprobs or [f'it now resolves to {again}, not {out_dir}']} -- no session runs")
    try:
        out_dir.mkdir(parents=False, exist_ok=False)
        pin = (out_dir, os.stat(out_dir))                   # the directory the smoke made (round-5 NOTE 2)
    except OSError as e:
        raise SystemExit(f"OUT DIR ({name}): {_oserr(e)} making the output directory -- no session runs")
    entries = []
    k = 0
    for form, fb in SMOKE_FORMS:
        for template in SMOKE_TEMPLATES:
            k += 1
            cell = scheds[template]["cells"][SMOKE_S]
            sc = smoke_config(form, template, cell, pool=pool, renders=renders)
            rec = runner.run_session_f3(adapter, sc, setup.audit, setup.ban_ids, path_cached=False,
                                        term_rx=setup.term_rx)
            problems = smoke_verify(rec, form, cell, pool=pool, renders=renders,
                                    scaffold_strings=setup.audit.scaffold_strings)
            rec["verified"] = not problems
            # the smoke review's round-1 MINOR-2, round-2 NOTE 2 and round-3 NOTE 2: the line reads are computed, the
            # session's block is printed (stdout is the raw; both parts, the reads' classes with the record's), then
            # the session is written once, atomically, its reads inside; a read that raises, a block part that
            # raises, or a write that fails is a STOP after what could be printed and written was, not a traceback
            try:
                reads, lines_error = smoke_line_reads(rec), None
            except Exception as e:                              # noqa: BLE001 -- reported, then a STOP
                reads, lines_error = None, f"{type(e).__name__}: {e}"
            block, block_errors = smoke_block(k, form, template, rec, problems, reads)
            for ln in block:
                print(ln, flush=True)
            jpath = out_dir / f"{k:02d}_{form}_{template}.json"
            doc = {"schema": "a-m2-smoke-session-v1", "form": form, "form_bytes": fb,
                   "addendum_m2_sha256": ADDENDUM_M2_SHA256, "g_ver": problems, "lines": reads,
                   "lines_error": lines_error, "record": rec}
            _smoke_write(jpath, doc, name, pin=pin)
            hair = [h for h in rec.get("hair_triggers") or () if h.get("phase") != "reasoning"]
            # round-4 NOTE 4, round-5 NOTE 4: every stop a session carries is named on its G-VER, READS or RAW BLOCK
            # line; a failed write of the session names only itself (the raw printed before the write carries the
            # rest; the smoke review's round-6 NOTE 2)
            hair_also = (f"; a task-round scaffold_absorption fired too (phase {hair[0].get('phase')})" if hair else "")
            also = (f"; the block raised {block_errors}" if block_errors else "") + hair_also
            if problems:
                raise SystemExit(f"G-VER ({name}): {form} {template}: {problems[:3]}"
                                 + (f"; the line reads raised {doc['lines_error']}" if doc["lines_error"] else "")
                                 + also + " -- the smoke stops")
            if doc["lines_error"]:
                raise SystemExit(f"READS ({name}): {form} {template}: the line reads raised {doc['lines_error']}{also} "
                                 f"-- the smoke stops (the session's record is written)")
            if block_errors:
                raise SystemExit(f"RAW BLOCK ({name}): {form} {template}: {block_errors}{hair_also} -- the smoke stops "
                                 f"(the session's record is written)")
            if hair:
                raise SystemExit(f"HAIR TRIGGER ({name}): {form} {template}: a task-round scaffold_absorption fired -- the "
                                 f"smoke stops (m:271's stop, carried)")
            entries.append((form, rec, reads))
    tally = smoke_tally(entries)
    sel = smoke_select(tally)
    tied = [f for f in SMOKE_SELECTABLE if f != sel["selected"] and sel["keys"][f][:2] == sel["keys"][sel["selected"]][:2]]
    summary = {"schema": "a-m2-smoke-summary-v1", "addendum_m2_sha256": ADDENDUM_M2_SHA256, "i_key": SMOKE_I_KEY,
               "selectable": list(SMOKE_SELECTABLE), "tally": tally, "selection": sel, "tied_on_i_ii": tied}
    # A-m2 v0.3 §3.3 (ans3 §1, #49): a smoke that stops under the driver's own refusals selects nothing, and the
    # driver prints no tally and no rule; so summary.json is written before either is printed, and a write that
    # fails is a STOP like any other
    spath = out_dir / "summary.json"
    try:
        _smoke_write(spath, summary, name, pin=pin)
    except SystemExit as e:
        # a stopped smoke selects nothing (A-m2 v0.3 §3.3): what the failed write left is renamed or removed, but only
        # while the directory is still the one the smoke made (the smoke review's round-6 NOTE 1)
        tail = (_summary_stopped(spath) if not _out_dir_moved(*pin) else
                "; the output directory moved, so nothing under it was renamed or removed")
        raise SystemExit(f"{e}{tail}")
    for f, _ in SMOKE_FORMS:
        x = tally[f]
        print(f"SMOKE TALLY {f}: sessions {x['sessions']} (valid {x['valid']}, complete {x['complete']}); lines "
              f"{x['lines']}; echo {x['echo']}, empty {x['empty']}, cap {x['cap']}, union {x['union']}; counter (a) "
              f"{x['counter_a']}; task responses {x['responses']} (free {x['free_responses']})", flush=True)
    print(f"SMOKE RULE (A-m2 {ADDENDUM_M2_VERSION} §3.3: (i) the union of empty, cap-reach and echo lines; ties by "
          f"(ii), counter (a); then F-a before F-b; selectable F-a and F-b, F-0 the control, F-c a diagnostic arm): keys "
          f"(i, ii, departure) {sel['keys']}; selected: {sel['selected']}; tied with it on (i) and (ii): "
          f"{tied or 'none'}", flush=True)
    print(f"SMOKE STOPS (A-m2 {ADDENDUM_M2_VERSION} §3.3): F-0 below {SMOKE_STOP_DEFECTS} defect lines: "
          f"{'FIRES' if sel['stop_uninformative'] else 'no'}; the selected form at {SMOKE_STOP_DEFECTS} or more: "
          f"{'FIRES' if sel['stop_selected_defects'] else 'no'}; adopted: {sel['adopted'] or 'none'}", flush=True)
    return {"status": "COMPLETE", "tally": tally, "selection": sel, "tied": tied}


def run_smoke(*, proposal_file, lock_file, analyzer_sha256, package_sha256, renders_sha16, smoke_out,
              adapter_factory=None) -> int:
    """A-m2's smoke. Exit 0 when the twelve sessions ran and verified, whatever the rule's stops say (the SMOKE STOPS
    line reports them; the seat reads it); 2 refused before the load (nothing loaded or written); 4 STOP (any
    SystemExit after the refusals: the load, the snapshot re-read, the licence, the backend, the output directory
    (re-checked just before it is made, then made, then pinned: moved before a write), a write or a serialization
    that fails, G-VER, a line read or a block part that raises, a task-round hair trigger), which prints no tally
    and no rule and leaves no summary.json unless its rename and its removal both fail or it cannot be examined,
    which the STOP line says (A-m2 v0.3 §3.3); any other exception is uncaught (a traceback; exit 1, or 130 on
    Ctrl-C), as at run_time. ``adapter_factory`` is the self-test's seam: a stub only (a non-stub adapter
    is refused there), with the Qwen pre-load checks skipped and the out directory still refused inside the
    repository."""
    given = {"proposal_file": proposal_file, "lock_file": lock_file, "analyzer_sha256": analyzer_sha256,
             "package_sha256": package_sha256, "renders_sha16": renders_sha16}
    missing = ["--" + k.replace("_", "-") for k in TIME_FLAGS if given[k] is None]
    if missing:
        _say(f"REFUSED: time --smoke needs {missing}: the lock's values (lock §1); nothing loaded")
        return 2
    out_dir, oprobs = smoke_out_problems(smoke_out)
    if oprobs or out_dir is None:
        _say(f"REFUSED: {SMOKE_NAME}: {oprobs}; nothing loaded")
        return 2
    extra, probs = time_identity_extra(proposal_file, lock_file, analyzer_sha256=analyzer_sha256,
                                       package_sha256=package_sha256, renders_sha16=renders_sha16)
    if probs or extra is None:
        _say(f"REFUSED: {SMOKE_NAME}: {probs}; nothing loaded")
        return 2
    try:
        if adapter_factory is None:
            pre = smoke_precheck(extra)
            dprobs, dsha = driver_problems()
            sprobs, snap = qwen_snapshot()
            if snap is not None and snap["revision"] != extra["weights_revision"]:
                sprobs = list(sprobs) + [f"refs/main is {snap['revision']}, not the lock's weights revision "
                                         f"{extra['weights_revision']} (lock §1; the licence's (g))"]
            pre += [f"driver: {p}" for p in dprobs] + [f"snapshot: {p}" for p in sprobs]
            if pre or dsha is None or snap is None:
                _say(f"REFUSED: {SMOKE_NAME}: {pre}; nothing loaded")
                return 2
            print(f"DRIVER {DRIVER_REL} {dsha}: committed at HEAD {stages._git_head()}, working tree identical", flush=True)
            print(snapshot_line(snap), flush=True)
            adapter = _load_qwen()
            sprobs2, snap2 = qwen_snapshot()
            if sprobs2 or snap2 is None:
                raise SystemExit(f"SNAPSHOT RE-READ REFUSED ({SMOKE_NAME}): after the load the snapshot check refuses: "
                                 f"{sprobs2} -- no session runs")
            if snap2["revision"] != snap["revision"]:
                raise SystemExit(f"SNAPSHOT MOVED ({SMOKE_NAME}): before the load {snap['revision']}; after it "
                                 f"{snap2['revision']} -- no session runs")
            if getattr(adapter, "model_id", None) != snap["model_id"]:
                raise SystemExit(f"MODEL ID ({SMOKE_NAME}): the adapter loaded {getattr(adapter, 'model_id', None)!r}, "
                                 f"the snapshot check read {snap['model_id']!r} -- no session runs")
            print(f"SNAPSHOT re-read after the load: unchanged ({snap['revision']}); adapter model_id "
                  f"{snap['model_id']}", flush=True)
        else:
            adapter = adapter_factory()
            if not stages._is_stub(adapter):
                raise SystemExit(f"SEAM ({SMOKE_NAME}): adapter_factory takes a stub adapter only -- the Qwen path runs "
                                 f"through the pre-load checks")
        run_smoke_sessions(adapter, extra, out_dir)
    except SystemExit as e:
        _say(f"STOP: {e}")
        return 4
    return 0


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
    _selftest_smoke(chk, labels, run)
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


def _selftest_smoke(chk, labels, run) -> None:
    """A-m2's smoke (model-free). Every case that could reach the Qwen branch runs with ``_load_qwen`` a trap or a
    stand-in and run_smoke_sessions a trap or a stand-in; the stub runs go through run_smoke's adapter_factory seam
    into a temporary directory outside the repository. Every call of run_smoke, run_smoke_sessions, smoke_precheck
    and main runs under the traps: the stage's checkpoint functions and run_gate_stage, any open() under
    data/mf3/ckpt, and a write inside the repository through open() or io.open for writing, os.open with a write
    flag, os.mkdir, os.replace, os.rename, os.unlink or os.remove (paths read positionally or by keyword; an
    absolute path whatever its dir_fd; the last component of a move, a mkdir or a removal not followed; the smoke
    review's round-3 NOTE 8, round-4 NOTE 2 and round-6 NOTE 1). Other deletions (os.rmdir, shutil), links,
    truncation and io.FileIO are outside these guards; the smoke's own deletions are m's unlink of its temp file in
    DIR on a failed write and _summary_stopped's removal of a summary file in DIR when its rename fails (round-5 and
    round-6 NOTE 5), and the data/mf3 hash below covers deletions there. The guards have positive controls, on
    their factories and as traps() installs them, the four checkpoint-function traps included; every stub run
    records that its traps are in place at the load, and every traps() call site records its entry (round-3 NOTE 3,
    round-4 NOTE 1, round-5 NOTE 3, round-6 NOTE 4). The pure functions (the refusals' classifier, the keys, P1 and
    the line reads on records,
    smoke_verify on a tampered record, the identity and the A-m2 text checks) run outside the traps (round-3 NOTE
    7). The tree under data/mf3 is hashed before and after (the self-test's own hash reads those files, outside the
    traps)."""
    import builtins
    import inspect
    from unittest import mock

    from valence_core.mf3 import testing

    G = globals()
    real_cfg0 = sc_mod.f3_config
    real_committed = stages.committed
    loads: list = []
    ckpt_calls: list = []
    opened_ckpt: list = []
    ckpt_dir = (REPO / "data" / "mf3" / "ckpt").resolve()
    real_open, real_io_open = builtins.open, io.open

    def t_loader():
        loads.append(1)
        raise SystemExit("selftest: the Qwen loader was reached from the smoke")

    def t_ckpt(name):
        def f(*a, **k):
            ckpt_calls.append(name)
            raise SystemExit(f"selftest: the smoke reached {name}")
        return f

    wrote_repo: list = []
    real_os_open, real_mkdir, real_replace, real_rename = os.open, os.mkdir, os.replace, os.rename
    real_aw, real_fsync_dir, real_path_mkdir = rs.atomic_write_json, rs.m_resume._fsync_dir, Path.mkdir
    real_ckpt_fns = (stages.checkpoint_path, rs.refuse_ended, rs.pending_at, stages.run_gate_stage)
    real_unlink, real_remove = os.unlink, os.remove
    write_flags = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
    # the path arguments each guard reads, by position and by keyword, with their dir_fd keywords (traps and controls)
    spec_mkdir = ((0, "path", "dir_fd"),)
    spec_move = ((0, "src", "src_dir_fd"), (1, "dst", "dst_dir_fd"))

    def _path(x):
        try:
            return Path(os.fsdecode(x)).resolve() if isinstance(x, (str, bytes, os.PathLike)) else None
        except (OSError, RuntimeError, TypeError, ValueError):
            return None

    def _final(x):
        # the last component not followed (a move or a mkdir acts on the entry itself, a link included): the parent
        # resolved, the name kept (the smoke review's round-4 NOTE 2)
        try:
            if not isinstance(x, (str, bytes, os.PathLike)):
                return None
            q = Path(os.fsdecode(x))
            return q.parent.resolve() / q.name
        except (OSError, RuntimeError, TypeError, ValueError):
            return None

    def _relative_to_fd(x, fd) -> bool:
        # a relative path under a dir_fd cannot be resolved here; an absolute one ignores its dir_fd
        try:
            return fd is not None and not os.path.isabs(os.fsdecode(x))
        except (TypeError, ValueError):
            return True

    def _refuse(pth, writing: bool):
        if pth is not None and _within(pth, ckpt_dir):
            opened_ckpt.append(pth.name)
            raise SystemExit("selftest: the smoke opened a file under data/mf3/ckpt")
        if writing and pth is not None and _within(pth, REPO):
            wrote_repo.append(str(pth))
            raise SystemExit("selftest: the smoke wrote inside the repository")

    def guarded(opener):
        def f(file, *a, **k):
            mode = a[0] if a else k.get("mode", "r")
            _refuse(_path(file), isinstance(mode, str) and any(c in mode for c in "wax+"))
            return opener(file, *a, **k)
        return f

    def guarded_os_open(opener):
        def f(path, flags, *a, **k):
            if not _relative_to_fd(path, k.get("dir_fd")):
                _refuse(_path(path), bool(flags & write_flags))
            return opener(path, flags, *a, **k)
        return f

    def guarded_paths(fn, spec: tuple):
        def f(*a, **k):
            for i, kw, fdkw in spec:
                x = a[i] if len(a) > i else k.get(kw)
                if x is not None and not _relative_to_fd(x, k.get(fdkw)):
                    _refuse(_final(x), True)
            return fn(*a, **k)
        return f

    def traps_in_place() -> bool:
        # every name traps() guards is not its original
        return all(cur is not orig for cur, orig in (
            (builtins.open, real_open), (io.open, real_io_open), (os.open, real_os_open), (os.mkdir, real_mkdir),
            (os.replace, real_replace), (os.rename, real_rename), (os.unlink, real_unlink), (os.remove, real_remove),
            (stages.checkpoint_path, real_ckpt_fns[0]), (rs.refuse_ended, real_ckpt_fns[1]),
            (rs.pending_at, real_ckpt_fns[2]), (stages.run_gate_stage, real_ckpt_fns[3])))

    traps_entered: list = []

    @contextlib.contextmanager
    def trap_record():
        # entered last in every traps() list: records that the traps are in place at that site (round-6 NOTE 4)
        traps_entered.append(traps_in_place())
        yield

    def traps():
        # the checkpoint functions, the stage, any open() under data/mf3/ckpt (the smoke review's round-1 MINOR-7,
        # NOTE 6) and a guarded write inside the repository (round-3 NOTE 8, round-4 NOTE 2, round-6 NOTE 1)
        return [mock.patch.object(stages, "checkpoint_path", t_ckpt("checkpoint_path")),
                mock.patch.object(rs, "refuse_ended", t_ckpt("refuse_ended")),
                mock.patch.object(rs, "pending_at", t_ckpt("pending_at")),
                mock.patch.object(stages, "run_gate_stage", t_ckpt("run_gate_stage")),
                mock.patch.object(builtins, "open", guarded(real_open)),
                mock.patch.object(io, "open", guarded(real_io_open)),
                mock.patch.object(os, "open", guarded_os_open(real_os_open)),
                mock.patch.object(os, "mkdir", guarded_paths(real_mkdir, spec_mkdir)),
                mock.patch.object(os, "replace", guarded_paths(real_replace, spec_move)),
                mock.patch.object(os, "rename", guarded_paths(real_rename, spec_move)),
                mock.patch.object(os, "unlink", guarded_paths(real_unlink, spec_mkdir)),
                mock.patch.object(os, "remove", guarded_paths(real_remove, spec_mkdir)),
                trap_record()]

    def gpatch(name, val):
        return mock.patch.dict(G, {name: val})

    def tree_state(root: Path) -> dict:
        out = {}
        for q in sorted(root.rglob("*")):
            k = str(q.relative_to(root))
            out[k] = ("link", os.readlink(q)) if q.is_symlink() else (
                ("file", hashlib.sha256(q.read_bytes()).hexdigest()) if q.is_file() else ("dir", None))
        return out

    data_root = REPO / "data" / "mf3"
    data_before = tree_state(data_root)
    pool, renders = sc_mod.pool_and_renders()
    swapped = str(REPO).swapcase()
    case_insensitive = Path(swapped).exists() and os.path.samefile(swapped, REPO)

    # --- the guards' positive controls (round-3 NOTE 3): fake openers, so nothing opens even if a guard fails ----
    probe = ckpt_dir / "probe.json"
    fake = guarded(lambda *a, **k: "opened")
    fake_os = guarded_os_open(lambda *a, **k: "opened")
    fake_mk, fake_rp = guarded_paths(lambda *a, **k: "made", spec_mkdir), guarded_paths(lambda *a, **k: "moved", spec_move)

    def fires(fn, *a, **k):
        try:
            fn(*a, **k)
            return False
        except SystemExit:
            return True
    spellings = [str(probe), os.fsencode(str(probe)), probe] + ([Path(str(probe).swapcase())] if case_insensitive else [])
    with tempfile.TemporaryDirectory() as td:
        outside = Path(td) / "probe.json"
        lnk = Path(td) / "lnk"
        lnk.symlink_to(outside)
        lnk_in = Path(td) / "lnk-in"
        lnk_in.symlink_to(REPO / "probe-target")            # a link outside the repository, pointing in
        ctl = {"ckpt reads": [fires(fake, x) for x in spellings],
               "repo writes": [fires(fake, REPO / "probe-w.txt", "w"), fires(fake, REPO / "data" / "probe-a", "a"),
                               fires(fake, REPO / "probe-x", "x"), fires(fake, REPO / "probe-rp", "r+"),
                               fires(fake, REPO / "probe-kw", mode="wb"),
                               fires(fake_os, REPO / "probe-os", os.O_WRONLY | os.O_CREAT),
                               fires(fake_os, probe, os.O_RDONLY), fires(fake_mk, REPO / "probe-dir"),
                               fires(fake_rp, outside, REPO / "probe-moved"), fires(fake_rp, REPO / "probe-src", outside),
                               fires(fake_mk, path=REPO / "probe-kw-dir"),
                               fires(fake_rp, src=outside, dst=REPO / "probe-kw-dst"),
                               fires(fake_rp, outside, REPO / "probe-abs-fd", dst_dir_fd=3),
                               fires(fake_os, REPO / "probe-os-fd", os.O_WRONLY | os.O_CREAT, dir_fd=3),
                               fires(fake_mk, REPO / "probe-mk-fd", dir_fd=3)],
               "passes": [fake(outside) == "opened", fake(REPO / "CLAUDE.md") == "opened",
                          fake(outside, "w") == "opened", fake_os(outside, os.O_WRONLY | os.O_CREAT) == "opened",
                          fake_os(REPO / "CLAUDE.md", os.O_RDONLY) == "opened", fake_mk(Path(td) / "d") == "made",
                          fake_rp(outside, Path(td) / "moved") == "moved",
                          fake_rp(outside, "rel-name", dst_dir_fd=3) == "moved", not fires(fake_rp, outside, lnk_in),
                          fake_os("rel-os", os.O_WRONLY | os.O_CREAT, dir_fd=3) == "opened",
                          fake_mk("rel-mk", dir_fd=3) == "made"],
               "final component": [_final(lnk) == Path(td).resolve() / "lnk", _path(lnk) == outside.resolve()]}
    n_ctl = (len(opened_ckpt), len(wrote_repo))
    opened_ckpt.clear()
    wrote_repo.clear()
    chk("mf3_sessions smoke: the guards' positive controls -- an open of a path under data/mf3/ckpt fires in its str, "
        "bytes and Path spellings (and a case-swapped one on a case-insensitive volume), and so does an os.open of it; "
        "a write inside the repository fires for open() in modes w, a, x, r+ and mode=wb, for os.open with a write "
        "flag, for os.mkdir and for os.replace from or onto it, by position or by keyword, and for an absolute path "
        "given a dir_fd (os.open, os.mkdir, os.replace); reads inside the repository, every call outside it and a "
        "relative path under a dir_fd pass; "
        "a move's last component is not followed, so a move onto a link outside the repository that points in passes "
        "(fake openers: nothing is opened)",
        all(ctl["ckpt reads"]) and all(ctl["repo writes"]) and all(ctl["passes"]) and all(ctl["final component"])
        and n_ctl == (len(spellings) + 1, 14), (case_insensitive, ctl, n_ctl))

    # --- the traps as traps() installs them (round-4 NOTE 1): each fires on a path whose parent does not exist, so a
    # trap left out raises FileNotFoundError and nothing is read, created or moved
    absent_ck = ckpt_dir / "selftest-absent-dir" / "x.json"
    absent_rp = REPO / "selftest-absent-dir" / "x"
    parents_absent = not absent_ck.parent.exists() and not absent_rp.parent.exists()

    def refuses_empty(fn) -> bool:
        # the empty call below is safe only while each real function needs an argument (round-6 NOTE 4)
        try:
            inspect.signature(fn).bind()
        except TypeError:
            return True
        return False
    empty_safe = all(refuses_empty(f) for f in real_ckpt_fns)
    installed: dict = {}
    with tempfile.TemporaryDirectory() as td:
        src_file = Path(td) / "src"
        src_file.write_text("x")

        def live(fn) -> bool:
            # a trap raises SystemExit; a missing one leaves the real call, which fails on the absent parent (OSError)
            # or, for the four checkpoint functions, refuses the empty call before its body (TypeError)
            try:
                fn()
            except SystemExit:
                return True
            except (OSError, TypeError):
                return False
            return False
        if parents_absent:
            with contextlib.ExitStack() as es:
                for cm in traps():
                    es.enter_context(cm)
                installed = {"open ckpt": live(lambda: open(absent_ck)),
                             "io.open ckpt": live(lambda: io.open(absent_ck)),
                             "os.open ckpt": live(lambda: os.open(absent_ck, os.O_RDONLY)),
                             "open write": live(lambda: open(absent_rp, "w")),
                             "io.open write": live(lambda: io.open(absent_rp, "w")),
                             "Path.write_text": live(lambda: absent_rp.write_text("x")),
                             "os.open write": live(lambda: os.open(absent_rp, os.O_WRONLY | os.O_CREAT)),
                             "os.mkdir": live(lambda: os.mkdir(absent_rp)),
                             "Path.mkdir": live(lambda: absent_rp.mkdir()),
                             "os.replace": live(lambda: os.replace(src_file, absent_rp)),
                             "os.rename": live(lambda: os.rename(src_file, absent_rp)),
                             "os.unlink": live(lambda: os.unlink(absent_rp)),
                             "os.remove": live(lambda: os.remove(absent_rp)),
                             "checkpoint_path": empty_safe and live(lambda: stages.checkpoint_path()),
                             "refuse_ended": empty_safe and live(lambda: rs.refuse_ended()),
                             "pending_at": empty_safe and live(lambda: rs.pending_at()),
                             "run_gate_stage": empty_safe and live(lambda: stages.run_gate_stage())}
        src_kept = src_file.is_file()
    n_live = (len(opened_ckpt), len(wrote_repo), len(ckpt_calls))
    opened_ckpt.clear()
    wrote_repo.clear()
    ckpt_calls.clear()
    chk("mf3_sessions smoke: the traps as traps() installs them -- each guard fires live (open, io.open and os.open "
        "under data/mf3/ckpt; open, io.open, Path.write_text and os.open for writing, os.mkdir, Path.mkdir, os.replace "
        "os.rename, os.unlink and os.remove inside the repository), on paths whose parents do not exist, so a missing "
        "trap would have read, made, moved or removed nothing; and the four checkpoint-function traps, called empty "
        "once each real function is shown to refuse that call before its body",
        parents_absent and empty_safe and len(installed) == 17 and all(installed.values()) and n_live == (3, 10, 4)
        and src_kept
        and not absent_rp.parent.exists() and not absent_ck.parent.exists(), (parents_absent, installed, n_live))

    # --- A-m2's text and the forms ----------------------------------------------------------------------------
    am2_path = REPO / ADDENDUM_M2_REL
    am2 = am2_path.read_bytes() if am2_path.is_file() else b""
    chk(f"mf3_sessions smoke: A-m2 {ADDENDUM_M2_VERSION} is committed at HEAD with its pinned sha256, and §3.1's four "
        "bullets parse to the driver's four forms exactly (addendum_m2_problems)", addendum_m2_problems() == [],
        addendum_m2_problems()[:2])
    t0 = am2.decode("utf-8", "replace")
    mut_form = t0.replace("Reasoning (one line): So far,`", "Reasoning (one line): So far`", 1).encode("utf-8")
    mut_extra = t0.replace("- **F-c (", "- **F-d (inline, extra):** `x`\n- **F-c (", 1).encode("utf-8")
    chk("mf3_sessions smoke: addendum_m2_text_problems refuses another sha256, a changed form literal (F-b without "
        "its comma) and an extra form bullet; it parses the escaped \\n as a newline",
        addendum_m2_text_problems(am2 + b" ") != [] and any("F-b" in p for p in addendum_m2_text_problems(
            mut_form, check_sha=False)) and any("F-d" in p for p in addendum_m2_text_problems(mut_extra, check_sha=False))
        and addendum_m2_text_problems(am2, check_sha=False) == []
        and dict(SMOKE_FORMS)["F-0"].endswith(":\n") and dict(SMOKE_FORMS)["F-a"].endswith(":"))
    chk("mf3_sessions smoke: the four forms keep m:174's header line and pass m:258's roster admissibility; a planted "
        "roster word fires it; F-0 is mf3's own block, banner.reasoning_block(n), at every n of 5..10",
        all(b.startswith("[round {n} | reasoning]\n") for _, b in SMOKE_FORMS)
        and smoke_form_hygiene() == [] and m_corr.hygiene(m_corr.ROSTERS_OF_RECORD, ("[round {n} | reasoning]\n"
                                                                                     "Reasoning on maple:",)) != []
        and all(dict(SMOKE_FORMS)["F-0"].replace("{n}", str(n)) == banner.reasoning_block(n) for n in banner.N_RANGE))

    # --- keys, cells, the scaffold -------------------------------------------------------------------------------
    sched = stages.load_committed([(SMOKE_STAGE, t) for t in SMOKE_TEMPLATES], schedule.DEFAULT_OUT)
    raw_sched = {t: json.loads((schedule.DEFAULT_OUT / sched[t]["name"]).read_text()) for t in SMOKE_TEMPLATES}
    ok_keys = True
    for f, b in SMOKE_FORMS:
        for t in SMOKE_TEMPLATES:
            cell = sched[t]["cells"][SMOKE_S]
            sc = smoke_config(f, t, cell, pool=pool, renders=renders)
            ref = sc_mod.f3_config(SMOKE_STAGE, t, SMOKE_S, cell, "uncached", reasoning_cap=60, pool=pool, renders=renders)
            ok_keys &= sc.keys == {"arm": f"m-smoke-f3|{f}|{t}|0", "items": "m-f3-items-time|0"}
            ok_keys &= sc.keys["items"] == raw_sched[t]["session_keys"]["items"].format(s=SMOKE_S) == ref.keys["items"]
            ok_keys &= sc.keys["arm"] != ref.keys["arm"] and sc.banner == ref.banner and sc.note_lines == ref.note_lines
            ok_keys &= (sc.P, sc.Q, sc.start, sc.order) == (ref.P, ref.Q, ref.start, ref.order)
            rng = keys.stream(sc.keys["arm"])
            want_seeds = [int(rng.integers(2**31)) for _ in range(4)]
            want_line = int(rng.integers(2**31))
            got = [sc.forced(i) for i in range(4)]
            rs0 = sc.reasoning(0)
            ref_forced = [ref.forced(i) for i in range(4)]
            ok_keys &= [x.seed for x in got] == want_seeds and rs0.seed == want_line
            ok_keys &= [(x.item, x.task_text, x.seg) for x in got] == [(x.item, x.task_text, x.seg) for x in ref_forced]
            ok_keys &= rs0.seg == b.replace("{n}", "5") and rs0.n == 5 and rs0.cap == 60
    chk("mf3_sessions smoke: per form and sham template, the arm key is m-smoke-f3|{form}|{template}|0 and the item key "
        "G-TIME-F3's (its schedule file's session_keys); banner, Note lines, labels, start and F2 block order are the "
        "stage's; the forced rounds' items, deliveries and segments are the stage's; the seeds are the smoke key's "
        "stream in m:159's order; reasoning(0) returns the form's bytes at n = 5", ok_keys)
    refused_cfg = []
    for fn in (lambda: smoke_config("F-d", "A2s", sched["A2s"]["cells"][0]),
               lambda: smoke_config("F-a", "A2", sched["A2s"]["cells"][0])):
        try:
            fn()
            refused_cfg.append(False)
        except ValueError:
            refused_cfg.append(True)
    chk("mf3_sessions smoke: smoke_config refuses a form outside A-m2 §3.1 and a contrast template", all(refused_cfg),
        refused_cfg)

    # --- the stub sessions ---------------------------------------------------------------------------------------
    smap: dict[int, tuple] = {}
    for f, _ in SMOKE_FORMS:
        for t in SMOKE_TEMPLATES:
            rng = keys.stream(SMOKE_ARM_KEY.format(form=f, template=t))
            for i in range(sc_mod.N_FORCED):
                smap.setdefault(int(rng.integers(2**31)), (f, t, "forced", i))
            for ci in range(6):
                smap.setdefault(int(rng.integers(2**31)), (f, t, "line", ci))
                rng.integers(2)
                smap.setdefault(int(rng.integers(2**31)), (f, t, "chosen", ci))
    banner_line = banner.SESSION_BANNER.rstrip("\n")
    empty_cap = {"text": "", "n_tok": 60, "cap_hit": True, "stop_reason": "cap"}
    CTRL_TEXT = "fine\x1b[0m\x7f here \\ ok"
    run_on = {"text": " ".join(["word"] * 20), "n_tok": 60, "cap_hit": True, "stop_reason": "cap"}

    def rule_default(f, t, kind, i, call):
        if kind == "line" and f == "F-0" and i < 3:
            return banner_line                               # 3 echoes per F-0 session: 9 in all
        if kind == "line" and f == "F-0" and t == "A2s" and i == 4:
            return dict(empty_cap)                           # empty and cap at once: one union line
        if kind == "line" and f == "F-a" and t == "A1s" and i == 1:
            return dict(run_on)                              # cap reached, no echo: F-a's one union line
        if kind == "line" and f == "F-b" and i == 0:
            return "=== Config selection ==="                # frame only: (a), not echo
        if kind == "line" and f == "F-c" and t == "A1s" and i == 3:
            return "As noted: " + banner.COMMON + " So far fine."   # the package's Q8 echo (containment); not §1's
        if kind == "chosen" and f == "F-c" and t == "A2s" and i == 0:
            return CTRL_TEXT                                 # control characters and a backslash: the raw escapes them
        return None

    def policy(rule):
        def texts(call):
            f, t, kind, i = smap[call["seed"]]
            x = rule(f, t, kind, i, call)
            if x is None:
                x = (testing.LINES[i % len(testing.LINES)] if kind == "line"
                     else testing.CLEAN[(i + (4 if kind == "chosen" else 0)) % len(testing.CLEAN)])
            return x
        return texts

    trapped_at_load: list = []

    def stub_factory(rule, cls=testing.F3Adapter, pre=None):
        def make():
            # the traps are in place where the load stands (round-5 NOTE 3)
            trapped_at_load.append(traps_in_place())
            if pre is not None:
                pre()                                       # stands where the load stands (round-4 NOTE 6)
            a = cls("mf3-smoke-scripted")
            a.load(policy(rule), None)
            return a
        return make

    def stub_run(rule, tag, cls=testing.F3Adapter, extra_cms=(), pre_load=None, post=None):
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "p").mkdir()                        # the smoke directory's parent, swappable (round-4 NOTE 6)
            out = Path(td) / "p" / tag
            buf, err = io.StringIO(), io.StringIO()
            with contextlib.ExitStack() as es:
                for cm in [gpatch("_load_qwen", t_loader), gpatch("addendum_m2_problems", lambda: []), *traps(),
                           *extra_cms, contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err)]:
                    es.enter_context(cm)
                try:
                    rc = run_smoke(**tflags, smoke_out=str(out), adapter_factory=stub_factory(
                        rule, cls, pre=(lambda: pre_load(out)) if pre_load else None))
                except Exception as e:                          # noqa: BLE001 -- reported as a failed check
                    rc = f"raised {type(e).__name__}"
            files = sorted(p.name for p in out.iterdir()) if out.is_dir() else []
            docs = [json.loads((out / n).read_text()) for n in files if n.endswith(".json") and n != "summary.json"]
            summ = json.loads((out / "summary.json").read_text()) if (out / "summary.json").is_file() else None
            made = out.exists()
            if post is not None:
                post(out)                                   # before the temporary directory goes
        return rc, buf.getvalue(), err.getvalue(), files, docs, summ, made

    tflags = {"proposal_file": stages.PROPOSAL_REL, "lock_file": TIME_LOCK_FILE,
              "analyzer_sha256": hashlib.sha256(stages.ANALYZER_PATH.read_bytes()).hexdigest(),
              "package_sha256": guard.package_sha256_of(guard.PACKAGE_DIR), "renders_sha16": m_corr.renders_sha(renders)}
    rc, out, err, files, docs, summ, _ = stub_run(rule_default, "smoke")
    chk("mf3_sessions smoke: the seed map covers 12 sessions x 16 generations without a collision", len(smap) == 192,
        len(smap))
    chk("mf3_sessions smoke: a stub run through run_smoke's seam -- exit 0; twelve session files (form-major, F-0 F-a "
        "F-b F-c x A1s A2s A3s) and summary.json in the new directory; every record G-VER clean, its line reads "
        "in its JSON (one per reasoning line); the checkpoint functions, the stage, any open() under data/mf3/ckpt "
        "and any guarded write inside the repository never reached, the traps in place at the load",
        rc == 0 and len(files) == 13 and "summary.json" in files
        and [(d["form"], d["record"]["template"]) for d in docs] == [(f, t) for f, _ in SMOKE_FORMS for t in SMOKE_TEMPLATES]
        and all(d["g_ver"] == [] and d["record"]["verified"] is True and d["lines_error"] is None for d in docs)
        and all(isinstance(d["lines"], list) and len(d["lines"]) == len(d["record"]["reasoning"]) for d in docs)
        and not ckpt_calls and not opened_ckpt and not wrote_repo and trapped_at_load[:1] == [True],
        (rc, len(files), err[-300:]))
    seg_ok = True
    for d in docs:
        rec, fb = d["record"], d["form_bytes"]
        t = rec["transcript"]
        for p in rec["pieces"]:
            if p["kind"] == "reasoning":
                n = 5 + p["idx"]
                seg_ok &= t[p["start"]:p["end"]] == fb.replace("{n}", str(n))
        seg_ok &= rec["keys"]["arm"] == f"m-smoke-f3|{d['form']}|{rec['template']}|0" and rec["stage"] == "time"
        seg_ok &= rec["path"] == "uncached" and rec["reasoning_cap"] == 60 and d["addendum_m2_sha256"] == ADDENDUM_M2_SHA256
    chk("mf3_sessions smoke: every reasoning piece is its form's bytes at its n; the records carry the smoke's arm key, "
        "stage time, the uncached path and cap 60", seg_ok)
    by = {(d["form"], d["record"]["template"]): d for d in docs}
    if len(by) != 12 or summ is None or not all(isinstance(d["lines"], list) for d in docs):
        chk("mf3_sessions smoke: the stub run produced the twelve records, with their line reads, that the later "
            "checks read", False, len(by))
        return
    # P1 on the stub records
    r0 = by[("F-0", "A2s")]["record"]
    dom0 = smoke_harness_lines(r0, 1)
    menu0 = r0["choices"][0]
    task_heads = [x for x in dom0 if x.startswith("[round ") and "| reasoning]" not in x and "| choice]" not in x]
    chk("mf3_sessions smoke: P1's domain on an F-0 record at line 2 -- the banner line, both Note lines, the five task "
        "headers and Task lines so far (four forced and round 5's), the two reasoning headers, the menu header, "
        "Reasoning (one line):, the menu's options line and 'Config choice (one word): <pick>'; no Response: line, no "
        "bare 'Config choice (one word):', no empty line",
        dom0[0] == banner_line and len(r0["note_lines"]) == 2 and all(x in dom0 for x in r0["note_lines"])
        and len(task_heads) == 5 and sum(x.startswith("Task: ") for x in dom0) == 5
        and "[round 5 | reasoning]" in dom0 and "[round 6 | reasoning]" in dom0 and "[round 5 | choice]" in dom0
        and "Reasoning (one line):" in dom0
        and f"Config choice (one word): {menu0['pick']}" in dom0 and "Config choice (one word):" not in dom0
        and menu0["menu"].split("\n")[1] in dom0
        and not any(x.startswith("Response:") for x in dom0) and all(m_audit.ws_norm(x) for x in dom0), dom0)
    dom5 = smoke_harness_lines(r0, 5)
    syn_t = ("B\nN\n[round 1 | config: x]\nTask: t\nResponse:\n[round 2 | config: x]\nTask: u\nResponse:y\n"
             "[round 5 | reasoning]\nReasoning (one line):\nL\n")
    syn_k = [("banner", "B\nN\n"), ("round", "[round 1 | config: x]\nTask: t\nResponse:"), ("generation", ""),
             ("joiner", "\n"), ("round", "[round 2 | config: x]\nTask: u\nResponse:"), ("generation", "y"),
             ("joiner", "\n"), ("reasoning", "[round 5 | reasoning]\nReasoning (one line):\n"),
             ("reasoning_text", "L"), ("reasoning_joiner", "\n")]
    syn_p, pos = [], 0
    for kind_, frag in syn_k:
        syn_p.append({"kind": kind_, "start": pos, "end": pos + len(frag)})
        pos += len(frag)
    syn = {"transcript": syn_t, "pieces": syn_p}
    nl_k = [("banner", "B\n"), ("round", "[round 1 | config: x]\nTask: t\nResponse:"), ("generation", ":\nTask: fake"),
            ("joiner", "\n"), ("reasoning", "[round 5 | reasoning]\nReasoning (one line):\n"), ("reasoning_text", "L"),
            ("reasoning_joiner", "\n")]
    nl_p, pos = [], 0
    for kind_, frag in nl_k:
        nl_p.append({"kind": kind_, "start": pos, "end": pos + len(frag)})
        pos += len(frag)
    nl_rec = {"transcript": "".join(f for _, f in nl_k), "pieces": nl_p}
    chk("mf3_sessions smoke: P1's domain holds each line once (ws_norm-distinct) at the last line, where the menu's pick "
        "line repeats; at that line the empty reasoning line before it (a zero-length piece at a line's start) is "
        "outside the domain and nothing raises; on a synthetic record an empty response's line and a non-empty one are "
        "both outside the domain and every other line is in it, in order; a model text holding a newline keeps both "
        "lines it touches out (the second, 'Task: fake', included)",
        len({m_audit.ws_norm(x) for x in dom5}) == len(dom5) and all(m_audit.ws_norm(x) for x in dom5)
        and "".join(f for _, f in syn_k) == syn_t
        and smoke_harness_lines(syn, 0) == ("B", "N", "[round 1 | config: x]", "Task: t", "[round 2 | config: x]",
                                            "Task: u", "[round 5 | reasoning]", "Reasoning (one line):")
        and smoke_harness_lines(nl_rec, 0) == ("B", "[round 1 | config: x]", "Task: t", "[round 5 | reasoning]",
                                               "Reasoning (one line):"),
        smoke_harness_lines(syn, 0))
    doms = {f: [smoke_harness_lines(by[(f, "A3s")]["record"], ci) for ci in range(6)] for f, _ in SMOKE_FORMS}
    chk("mf3_sessions smoke: P1 across the forms -- under F-a and F-b no domain line holds the label (the model "
        "continues it) and none holds F-b's opener; under F-c 'Give one line of reasoning.' is in the domain and the "
        "label is not; under F-0 the label is",
        all(not any("Reasoning (one line)" in x for x in dl) for f in ("F-a", "F-b") for dl in doms[f])
        and not any("So far," in x for dl in doms["F-b"] for x in dl)
        and all("Give one line of reasoning." in dl and "Reasoning (one line):" not in dl for dl in doms["F-c"])
        and all("Reasoning (one line):" in dl for dl in doms["F-0"]))
    reads0 = by[("F-0", "A1s")]["lines"]
    readsb = by[("F-b", "A1s")]["lines"]
    chk("mf3_sessions smoke: the scripted banner lines under F-0 are echo at index 0 and (a), with the package's own "
        "classes [] beside (the banner is outside Q8's set); F-b's frame line is (a) and not echo; a clean line is "
        "neither",
        [x["echo_index"] for x in reads0[:3]] == [0, 0, 0] and all(x["counter_a"] for x in reads0[:3])
        and all(x["package_classes"] == [] for x in reads0[:3])
        and reads0[3]["classes"] == [] and not reads0[3]["counter_a"]
        and readsb[0]["classes"] == [] and readsb[0]["counter_a"] and readsb[0]["frame"] and not readsb[0]["contains"],
        (reads0[:4], readsb[:1]))
    rec_c = json.loads(json.dumps(r0))
    tests = {"equal, spaced": "  " + "Config choice (one word):   " + menu0["pick"] + " ",
             "contains": "I saw " + banner_line + " again", "case": banner_line.lower(),
             "later header": "[round 9 | reasoning]", "response": "Response:"}
    got_c = {}
    for k_, txt in tests.items():
        rec_c["reasoning"][2]["text"] = txt
        x = smoke_line_reads({**rec_c, "reasoning": rec_c["reasoning"][:3]})[2]
        got_c[k_] = (x["echo_index"] is not None, x["counter_a"])
    chk("mf3_sessions smoke: the match is equality after ws_norm and case-sensitive (a spaced copy of the menu's pick "
        "line echoes); containment is (a) only; a lower-cased banner is no echo but keeps the frame, so (a); a header "
        "not yet written and the bare Response: fragment are neither",
        got_c == {"equal, spaced": (True, True), "contains": (False, True), "case": (False, True),
                  "later header": (False, False), "response": (False, False)}, got_c)
    tal = summ["tally"]
    pc = by[("F-c", "A1s")]["lines"][3]
    chk("mf3_sessions smoke: a line holding COMMON inside other text is the package's Q8 echo (containment) but not "
        "§1's: classes [], (a) True, package classes ['echo'] -- the smoke's classes never take the package's echo",
        pc["classes"] == [] and pc["counter_a"] and pc["contains"] and pc["package_classes"] == ["echo"], pc)
    ec = by[("F-0", "A2s")]["lines"][4]
    ca = by[("F-a", "A1s")]["lines"][1]
    union_ok = all(tal[f]["union"] == sum(bool(x["classes"]) for d in docs if d["form"] == f for x in d["lines"])
                   for f, _ in SMOKE_FORMS)
    chk("mf3_sessions smoke: the defect classes and their union -- an empty line at the cap is empty and cap_no_newline, "
        "counted once in the union; a run-on line at the cap is cap_no_newline alone; per form the union is the number "
        "of lines with any class; empty and cap are tallied per form",
        ec["classes"] == ["empty", "cap_no_newline"] and ca["classes"] == ["cap_no_newline"] and union_ok
        and (tal["F-0"]["empty"], tal["F-0"]["cap"], tal["F-0"]["union"]) == (1, 1, 10)
        and (tal["F-a"]["empty"], tal["F-a"]["cap"], tal["F-a"]["union"]) == (0, 1, 1)
        and all(tal[f]["free_responses"] == 18 for f, _ in SMOKE_FORMS), {f: tal[f]["union"] for f, _ in SMOKE_FORMS})
    chk("mf3_sessions smoke: the stub run's rule -- F-0 union 10 (echo 9), (a) 9; F-a union 1 (a cap line), (a) 0; F-b "
        "union 0, (a) 3; F-c union 0, (a) 1; 18 lines per form; among F-a and F-b the union decides: F-b, no tie, no "
        "stop, adopted F-b; the keys name F-a and F-b only",
        tal["F-0"]["echo"] == 9 and tal["F-0"]["counter_a"] == 9 and tal["F-a"]["counter_a"] == 0
        and tal["F-b"]["union"] == 0 and tal["F-b"]["counter_a"] == 3 and tal["F-c"]["union"] == 0
        and tal["F-c"]["counter_a"] == 1 and all(tal[f]["lines"] == 18 for f, _ in SMOKE_FORMS)
        and summ["selection"]["selected"] == "F-b" and summ["tied_on_i_ii"] == []
        and not summ["selection"]["stop_uninformative"] and not summ["selection"]["stop_selected_defects"]
        and summ["selection"]["adopted"] == "F-b" and sorted(summ["selection"]["keys"]) == ["F-a", "F-b"]
        and summ["i_key"] == "union" and summ["selectable"] == ["F-a", "F-b"], summ["selection"])
    blocks = out.split("SMOKE SESSION ")[1:]
    blocks_ok = len(blocks) == 12
    for blk, d in zip(blocks, docs):
        rec = d["record"]
        blocks_ok &= all(("  | " + _printable(ln) + "\n") in blk for ln in rec["transcript"].split("\n")[:-1])
        blocks_ok &= blk.count("\n  round ") == len(rec["rounds"]) and blk.count("\n  line ") == len(rec["reasoning"])
        blocks_ok &= blk.count("\n  read ") == len(rec["choices"])
    chk("mf3_sessions smoke: stdout is the raw -- the A-M2, PROVENANCE and BACKEND lines in that order before the first "
        "SMOKE SESSION block, then twelve SMOKE SESSION "
        "blocks, each with its own transcript line by line and one line per task round, reasoning line and read; four "
        "SMOKE TALLY lines, SMOKE RULE and SMOKE STOPS, after the last block and naming A-m2 v0.3 §3.3; nothing on "
        "stderr",
        blocks_ok and 0 <= out.find("A-M2 ") < out.find("PROVENANCE: ") < out.find("BACKEND ") < out.find("SMOKE SESSION ")
        and out.count("SMOKE TALLY ") == 4 and "SMOKE RULE" in out and "SMOKE STOPS" in out and err == ""
        and out.rfind("SMOKE SESSION ") < out.find("SMOKE TALLY ")
        and f"SMOKE RULE (A-m2 {ADDENDUM_M2_VERSION} §3.3:" in out and f"SMOKE STOPS (A-m2 {ADDENDUM_M2_VERSION} §3.3)" in out,
        err[-300:])
    ctrl_rec = by[("F-c", "A2s")]["record"]
    chk("mf3_sessions smoke: the raw escapes non-printable characters (a carriage return, ESC, DEL) and the backslash, "
        "and keeps printable ones, the em dash of a round header included; wired into the run: a scripted response with "
        "ESC, DEL and a backslash prints escaped in its transcript and round lines, no raw ESC or DEL byte reaches "
        "stdout, and the session's JSON keeps the exact bytes",
        _printable("a\rb\x1bc\x7f") == "a\\rb\\x1bc\\x7f" and _printable("a\\b") == "a\\\\b"
        and _printable("[round 2 — active config: x]") == "[round 2 — active config: x]"
        and ("  | Response:" + _printable(CTRL_TEXT) + "\n") in out and "\x1b" not in out and "\x7f" not in out
        and CTRL_TEXT in ctrl_rec["transcript"] and any(r["text"] == CTRL_TEXT for r in ctrl_rec["rounds"]),
        [r["audit"]["claim"] for r in ctrl_rec["rounds"] if r["text"] == CTRL_TEXT])

    # --- the rule, by hand ---------------------------------------------------------------------------------------
    def tl(**kw):
        base = {f: {"echo": 0, "union": 0, "counter_a": 0} for f, _ in SMOKE_FORMS}
        for f, (e, u, a_) in kw.items():
            base[f.replace("_", "-")] = {"echo": e, "union": u, "counter_a": a_}
        return base
    s1 = smoke_select(tl(F_0=(5, 5, 6), F_a=(1, 1, 2), F_b=(1, 1, 1), F_c=(0, 0, 0)))
    s2 = smoke_select(tl(F_0=(2, 2, 2), F_a=(0, 0, 0)))
    s3 = smoke_select(tl(F_0=(6, 6, 6), F_a=(3, 3, 3), F_b=(3, 3, 3), F_c=(0, 0, 0)))
    s4 = smoke_select(tl(F_0=(5, 5, 5), F_a=(0, 4, 0), F_b=(1, 1, 1)))
    s5 = smoke_select(tl(F_0=(0, 0, 0), F_c=(0, 0, 0), F_a=(2, 2, 2), F_b=(1, 1, 1)))
    s6 = smoke_select(tl(F_0=(3, 3, 3), F_a=(2, 2, 2), F_b=(2, 2, 3)))
    s7 = smoke_select(tl(F_0=(4, 4, 4), F_a=(1, 3, 3), F_b=(1, 3, 3)))
    chk("mf3_sessions smoke: the rule (A-m2 v0.3 §3.3) -- among F-a and F-b only, fewest (i), then (ii) (F-b over F-a at "
        "1/1 against 1/2); F-0 below 3 fires the first stop; the selected form at 3 or more fires the second; (i) is the "
        "union, so an F-a with no echo but 4 cap or empty lines loses to an F-b at 1; F-0 and F-c are never selected, "
        "even at 0 (F-b is, and F-0 at 0 fires the first stop); the keys name F-a and F-b only",
        s1["selected"] == "F-b" and s1["adopted"] == "F-b" and s2["stop_uninformative"] and s2["adopted"] is None
        and s3["selected"] == "F-a" and s3["stop_selected_defects"] and s3["adopted"] is None
        and s4["selected"] == "F-b" and s5["selected"] == "F-b" and s5["stop_uninformative"] and s5["adopted"] is None
        and sorted(s1["keys"]) == ["F-a", "F-b"] and SMOKE_I_KEY == "union" and SMOKE_SELECTABLE == ("F-a", "F-b"),
        (s1["selected"], s4["selected"], s5["selected"]))
    chk("mf3_sessions smoke: the stops at their bounds -- F-0 at exactly 3 does not fire the first; a selected form at 2 "
        "does not fire the second (F-a at 2/2 adopted); the first stop reads the union (F-0 at echo 2, union 9 does "
        "not fire it); at a full tie on (i) and (ii) the departure order picks F-a",
        not s6["stop_uninformative"] and not s6["stop_selected_defects"] and s6["adopted"] == "F-a"
        and smoke_select(tl(F_0=(2, 9, 2), F_a=(0, 0, 0)))["stop_uninformative"] is False
        and smoke_select(tl(F_0=(9, 2, 9), F_a=(0, 0, 0)))["stop_uninformative"] is True
        and s7["selected"] == "F-a", (s6, s7["selected"]))

    # --- refusals ------------------------------------------------------------------------------------------------
    as_root = hasattr(os, "geteuid") and os.geteuid() == 0
    with tempfile.TemporaryDirectory() as td:
        present = Path(td) / "present"
        present.mkdir()
        afile = Path(td) / "afile"
        afile.write_text("x")
        ro = Path(td) / "ro"
        ro.mkdir()
        locked = Path(td) / "locked"
        (locked / "sub").mkdir(parents=True)
        link = Path(td) / "link"
        link.symlink_to(REPO / "data")
        dangling = Path(td) / "dangling"
        dangling.symlink_to(Path(td) / "nowhere")
        loop = Path(td) / "loop"
        loop.symlink_to(loop)
        exists_msg = ": exists; the smoke writes a new directory only"
        cases = {"none": (None, "--smoke needs --smoke-out"),
                 "repo": (str(REPO / "scratch-x"), "inside the repository"),
                 "data": (str(REPO / "data" / "mf3" / "smoke"), "inside the repository"),
                 "link into data": (str(link / "smoke"), "inside the repository"),
                 "present": (str(present), exists_msg),
                 "dangling link": (str(dangling), exists_msg),
                 "no parent": (str(Path(td) / "a" / "b"), "its parent is not a directory"),
                 "parent a file": (str(afile / "new"), "its parent is not a directory"),
                 "name too long": (str(Path(td) / ("n" * 300)), "cannot be examined (OSError)"),
                 "unknown ~user": ("~selftest-no-such-user/smoke", "does not resolve (RuntimeError)"),
                 "symlink loop": (str(loop / "new"), ("does not resolve", "cannot be examined"))}
        if not as_root:                                     # root ignores the permission bits (round-3 NOTE 6)
            cases["parent not writable"] = (str(ro / "new"), "its parent is not writable")
            cases["parent unsearchable"] = (str(locked / "sub" / "new"), "cannot be examined (PermissionError)")
        if case_insensitive:
            cases["case-swapped spelling"] = (swapped + "/data/mf3/smoke-x", "inside the repository")
        outs = {}
        ro.chmod(0o500)
        locked.chmod(0o000)
        try:
            for k_, (arg, _) in cases.items():
                try:
                    outs[k_] = smoke_out_problems(arg)[1]
                except Exception as e:                          # noqa: BLE001 -- reported as a failed check
                    outs[k_] = [f"raised {type(e).__name__}"]
        finally:
            ro.chmod(0o700)
            locked.chmod(0o700)
        ok_new = smoke_out_problems(str(Path(td) / "new"))[1]
    chk("mf3_sessions smoke: --smoke-out is refused, each with its own message, when absent; inside the repository "
        "(data/ included, through a link, and, on a case-insensitive volume, under another spelling of the "
        "repository's path: the diagnostic leads with whether this volume is one); existing, a dangling link "
        "included; without a parent directory, or under a file; under a parent that is not writable; under a "
        "component that cannot be examined, and with a name too long to examine under a parent that is fine; an "
        "unknown ~user is refused as not resolving and a symlink loop as not resolving or not examinable (the word "
        "differs by Python version), neither raised (no traceback; the two permission cases skipped under root); a "
        "new directory outside the repository is accepted",
        all(len(outs[k_]) == 1 and any(w in outs[k_][0] for w in (want if isinstance(want, tuple) else (want,)))
            for k_, (_, want) in cases.items()) and ok_new == [],
        (f"case_insensitive {case_insensitive}, root {as_root}", {k_: outs[k_][:1] for k_ in outs}))
    cli = {}
    n_ckpt = len(ckpt_calls)
    with contextlib.ExitStack() as es:
        for cm in [gpatch("_load_qwen", t_loader), gpatch("run_smoke_sessions", t_ckpt("run_smoke_sessions")), *traps()]:
            es.enter_context(cm)
        with tempfile.TemporaryDirectory() as td:
            base = ["time", "--proposal-file", tflags["proposal_file"], "--lock-file", tflags["lock_file"],
                    "--analyzer-sha256", tflags["analyzer_sha256"], "--package-sha256", tflags["package_sha256"],
                    "--renders-sha16", tflags["renders_sha16"]]
            cli["no out"] = run(base + ["--smoke"])
            cli["resume"] = run(base + ["--smoke", "--resume", "--smoke-out", str(Path(td) / "o")])
            cli["out without smoke"] = run(base + ["--smoke-out", str(Path(td) / "o")])
            cli["inside repo"] = run(base + ["--smoke", "--smoke-out", str(REPO / "data" / "x")])
            cli["no flags"] = run(["time", "--smoke", "--smoke-out", str(Path(td) / "o")])
            dl = Path(td) / "dangling"
            dl.symlink_to(Path(td) / "nowhere")
            cli["dangling"] = run(base + ["--smoke", "--smoke-out", str(dl)])
    chk("mf3_sessions smoke: the CLI refuses (exit 2, nothing loaded, no checkpoint function, stage or session reached) "
        "--smoke without --smoke-out, with --resume, --smoke-out without --smoke, an out directory inside data/, a "
        "missing lock flag and a dangling link as the out directory, each with its own message",
        all(rc_ == 2 for rc_, _ in cli.values()) and not loads and len(ckpt_calls) == n_ckpt and not opened_ckpt
        and not wrote_repo and "--smoke needs --smoke-out" in cli["no out"][1]
        and "takes no --resume" in cli["resume"][1] and "it needs --smoke" in cli["out without smoke"][1]
        and "inside the repository" in cli["inside repo"][1] and "'--proposal-file'" in cli["no flags"][1]
        and ": exists; the smoke writes a new directory only" in cli["dangling"][1],
        {k_: rc_ for k_, (rc_, _) in cli.items()})

    # --- the Qwen branch of run_smoke, with stand-ins (the smoke review's round-1 MINOR-6) ------------------------
    extra0 = time_identity_extra(**tflags)[0]
    info = {"model_id": QWEN_MODEL_ID, "revision": extra0["weights_revision"], "snapshot_dir": "<snap>",
            "n_snapshots": 1, "offline": "1"}

    class _Loaded:
        def __init__(self, mid):
            self.model_id = mid

    def qwen_case(pre=(), snaps=None, loaded=QWEN_MODEL_ID, drv=([], "f" * 64)):
        seq = list(snaps if snaps is not None else [([], info), ([], info)])
        sessions: list = []
        loaded_: list = []

        def snap_fn(*a, **k):
            return seq.pop(0) if seq else ([], info)

        def load_fn():
            loaded_.append(1)
            return _Loaded(loaded)

        def sess_fn(adapter, extra, out_dir):
            sessions.append(out_dir)
            return {"status": "COMPLETE"}
        with tempfile.TemporaryDirectory() as td, contextlib.ExitStack() as es:
            for cm in [gpatch("smoke_precheck", lambda extra: list(pre)),
                       gpatch("driver_problems", lambda: drv), gpatch("qwen_snapshot", snap_fn),
                       gpatch("_load_qwen", load_fn), gpatch("run_smoke_sessions", sess_fn), *traps()]:
                es.enter_context(cm)
            buf, err_ = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err_):
                rc_ = run_smoke(**tflags, smoke_out=str(Path(td) / "o"))
        return rc_, buf.getvalue(), err_.getvalue(), len(loaded_), len(sessions)
    q_pre = qwen_case(pre=["planted-pre"], drv=(["planted-driver"], None), snaps=[(["planted-snap"], None)])
    q_rev = qwen_case(snaps=[([], {**info, "revision": "0" * 40})])
    q_ok = qwen_case()
    q_moved = qwen_case(snaps=[([], info), ([], {**info, "revision": "1" * 40})])
    q_mid = qwen_case(loaded="another/model")
    q_reread = qwen_case(snaps=[([], info), (["planted re-read"], None)])
    ok_order = (q_ok[1].find("DRIVER ") < q_ok[1].find("SNAPSHOT ") < q_ok[1].find("SNAPSHOT re-read after the load"))
    chk("mf3_sessions smoke: run_smoke's Qwen branch -- a precheck, a driver and a snapshot problem are refused together "
        "in one REFUSED line (exit 2, nothing loaded); "
        "a refs/main other than the lock's revision is refused (exit 2); when clear, the DRIVER line, then the SNAPSHOT "
        "line, then one load and the re-read's line, then the sessions (exit 0); a moved revision, another model id or "
        "a re-read that refuses after the load each STOP before any session (exit 4)",
        q_pre[0] == 2 and q_pre[2].count("REFUSED") == 1
        and sum(ln.startswith("REFUSED") and all(x in ln for x in ("planted-pre", "planted-driver", "planted-snap"))
                for ln in q_pre[2].splitlines()) == 1
        and q_pre[3] == 0 and q_pre[4] == 0
        and q_rev[0] == 2 and "not the lock's weights revision" in q_rev[2] and q_rev[3] == 0
        and q_ok[0] == 0 and q_ok[3] == 1 and q_ok[4] == 1 and q_ok[1].find("DRIVER ") >= 0 and ok_order
        and q_moved[0] == 4 and "SNAPSHOT MOVED" in q_moved[2] and q_moved[4] == 0
        and q_mid[0] == 4 and "MODEL ID" in q_mid[2] and q_mid[4] == 0
        and q_reread[0] == 4 and "SNAPSHOT RE-READ REFUSED" in q_reread[2] and q_reread[4] == 0,
        [(c[0], c[3], c[4]) for c in (q_pre, q_rev, q_ok, q_moved, q_mid, q_reread)])

    # --- STOPs inside the run ------------------------------------------------------------------------------------
    def rule_hair(f, t, kind, i, call):
        if f == "F-a" and t == "A2s" and kind == "chosen" and i == 1:
            return "fine <|im_end|> here"
        return rule_default(f, t, kind, i, call)

    def rule_line_hair(f, t, kind, i, call):
        if f == "F-0" and t == "A1s" and kind == "line" and i == 2:
            return "<|im_start|>"
        return rule_default(f, t, kind, i, call)
    def no_rule(text: str) -> bool:
        # A-m2 v0.3 §3.3 (#49): a smoke stopped under the driver's own refusals prints no tally and no rule
        return not any(x in text for x in ("SMOKE TALLY", "SMOKE RULE", "SMOKE STOPS"))
    rc_h, out_h, err_h, files_h, _, summ_h, _ = stub_run(rule_hair, "hair")
    rc_l, out_l, err_l, files_l, docs_l, summ_l, _ = stub_run(rule_line_hair, "linehair")
    chk("mf3_sessions smoke: a task-round scaffold string stops the smoke after its session (exit 4, five session "
        "files, no summary, no rule printed); a reasoning-line scaffold string ends that session only (twelve "
        "sessions, exit 0)",
        rc_h == 4 and "HAIR TRIGGER" in err_h and len(files_h) == 5 and summ_h is None and no_rule(out_h)
        and rc_l == 0 and len(files_l) == 13 and docs_l[0]["record"]["excluded"] and len(docs_l[0]["lines"]) == 3,
        (rc_h, len(files_h), rc_l, len(files_l)))

    class _NonStub(testing.F3Adapter):
        def provenance(self):
            return {**dict(super().provenance()), "adapter": "selftest-nonstub", "apparatus": "selftest-nonstub"}
    rc_s, out_s, err_s, files_s, _, _, made_s = stub_run(rule_default, "seam", cls=_NonStub)
    chk("mf3_sessions smoke: the adapter_factory seam refuses a non-stub adapter (exit 4, SEAM) before any session, "
        "the output directory never made, no tally or rule printed", rc_s == 4 and "SEAM" in err_s and not made_s
        and no_rule(out_s), (rc_s, err_s[-200:]))

    class _Fake(testing.F3Adapter):
        def provenance(self):
            return {**dict(super().provenance()), "torch": "other"}
    bk_buf = io.StringIO()
    with tempfile.TemporaryDirectory() as td, contextlib.ExitStack() as es:
        for cm in [mock.patch.object(stages, "_is_stub", lambda a: False), gpatch("addendum_m2_problems", lambda: []),
                   mock.patch.object(stages, "_laptop_preflight", lambda *a, **k: True),
                   mock.patch.object(stages, "_licence", lambda *a, **k: None), contextlib.redirect_stdout(bk_buf),
                   *traps()]:
            es.enter_context(cm)
        try:
            run_smoke_sessions(_Fake("mf3-smoke-fake"), extra0, Path(td) / "o")
            backend_stop = None
        except SystemExit as e:
            backend_stop = str(e)
        except Exception as e:                                  # noqa: BLE001 -- reported as a failed check
            backend_stop = f"raised {type(e).__name__}"
        bk_out = bk_buf.getvalue()
        made = (Path(td) / "o").exists()
        fake_ok = testing.F3Adapter("mf3-smoke-fake-ok")
        fake_ok.load(policy(rule_default), None)
        with mock.patch.object(rs, "backend_identifier", lambda prov: SMOKE_BACKEND):
            try:
                res_ok = run_smoke_sessions(fake_ok, extra0, Path(td).resolve() / "o2")
            except (Exception, SystemExit) as e:               # noqa: BLE001 -- reported as a failed check
                res_ok = {"status": f"raised {type(e).__name__}: {str(e)[:120]}"}
    chk("mf3_sessions smoke: off the backend of record a non-stub smoke STOPs before any session and writes nothing; on "
        "it (the identifier a734dadec8f8ce9b) the same path runs the twelve sessions to COMPLETE",
        backend_stop is not None and "BACKEND" in backend_stop and not made and no_rule(bk_out)
        and "SMOKE SESSION " not in bk_out and res_ok.get("status") == "COMPLETE",
        (backend_stop, res_ok.get("status")))
    tam = json.loads(json.dumps(by[("F-a", "A3s")]["record"]))
    piece = next(p for p in tam["pieces"] if p["kind"] == "reasoning")
    i_t = piece["start"] + 1                                     # "[round ..." -> "[Round ...": the block's bytes only
    tam["transcript"] = tam["transcript"][:i_t] + "R" + tam["transcript"][i_t + 1:]
    tam_probs = smoke_verify(tam, "F-a", sched["A3s"]["cells"][0], pool=pool, renders=renders,
                             scaffold_strings=testing.f3_kit().ban_strings)
    restored = sc_mod.f3_config is real_cfg0
    with mock.patch.object(verify, "verify_session", side_effect=SystemExit("planted")):
        try:
            smoke_verify(tam, "F-a", sched["A3s"]["cells"][0], pool=pool, renders=renders,
                         scaffold_strings=testing.f3_kit().ban_strings)
        except SystemExit:
            pass
    chk("mf3_sessions smoke: G-VER under the smoke refuses an F-a record whose reasoning block's bytes alone are changed "
        "(its keys kept): the transcript differs from the harness rebuilt; scaffold.f3_config is the module's own after "
        "the stub runs' calls and after a call whose G-VER raises",
        any("transcript bytes differ" in p for p in tam_probs) and restored and sc_mod.f3_config is real_cfg0,
        tam_probs[:2])
    real_sv = smoke_verify
    calls_sv: list = []

    def sv_fail_third(rec, form, cell, **kw):
        calls_sv.append(1)
        return ["BREAK: planted"] if len(calls_sv) == 3 else real_sv(rec, form, cell, **kw)
    with gpatch("smoke_verify", sv_fail_third):
        rc_v, out_v, err_v, files_v, docs_v, summ_v, _ = stub_run(rule_default, "gver")
    chk("mf3_sessions smoke: a G-VER problem on a record stops the smoke after that session (exit 4; three session "
        "files, the third marked unverified with its problems; no summary)",
        rc_v == 4 and "G-VER" in err_v and len(files_v) == 3 and summ_v is None and no_rule(out_v)
        and docs_v[2]["g_ver"] == ["BREAK: planted"] and docs_v[2]["record"]["verified"] is False, (rc_v, len(files_v)))
    real_lr = smoke_line_reads
    calls_lr: list = []

    def lr_fail_second(rec):
        calls_lr.append(1)
        if len(calls_lr) == 2:
            raise ValueError("planted")
        return real_lr(rec)
    with gpatch("smoke_line_reads", lr_fail_second):
        rc_r, out_r, err_r, files_r, docs_r, summ_r, _ = stub_run(rule_default, "reads")
    chk("mf3_sessions smoke: a line read that raises is a STOP after its session, not a traceback (exit 4, READS): the "
        "session's record is written with lines None and the error, and its transcript is in the raw",
        rc_r == 4 and "READS" in err_r and len(files_r) == 2 and docs_r[1]["lines"] is None
        and "ValueError: planted" in (docs_r[1]["lines_error"] or "") and out_r.count("SMOKE SESSION ") == 2
        and all(("  | " + _printable(ln) + "\n") in out_r for ln in docs_r[1]["record"]["transcript"].split("\n")[:-1])
        and summ_r is None and no_rule(out_r), (rc_r, len(files_r), err_r[-200:]))
    real_ssl = smoke_session_lines
    calls_ssl: list = []

    def ssl_fail_second(k, form, rec, problems):
        calls_ssl.append(1)
        if len(calls_ssl) == 2:
            raise KeyError("planted")
        return real_ssl(k, form, rec, problems)
    with gpatch("smoke_session_lines", ssl_fail_second):
        rc_b, out_b, err_b, files_b, docs_b, summ_b, _ = stub_run(rule_default, "block")
    chk("mf3_sessions smoke: a block part that raises is a STOP after its session, not a traceback (exit 4, RAW "
        "BLOCK): one line names the error in the session's place, its line reads are still printed, and its record "
        "is written with its reads (round-3 NOTE 2)",
        rc_b == 4 and "RAW BLOCK" in err_b and len(files_b) == 2 and docs_b[1]["lines"] is not None
        and "SMOKE SESSION 2/12 F-0 A2s: the record's part raised KeyError" in out_b
        and out_b.count("\n  line ") == len(docs_b[0]["lines"]) + len(docs_b[1]["lines"])
        and summ_b is None and no_rule(out_b), (rc_b, len(files_b), err_b[-200:]))

    # --- the write path (round-3 MINOR-1): m's atomic write made to fail at a chosen call -------------------------
    def failing_write(at: int, how: str):
        calls_w: list = []

        def w(path, obj, **kw):
            calls_w.append(Path(path).name)
            if len(calls_w) == at and how == "enospc":
                with mock.patch.object(os, "replace", side_effect=OSError(errno.ENOSPC, "No space left on device")):
                    return real_aw(path, obj, **kw)
            if len(calls_w) == at and how == "nan":
                return real_aw(path, {**obj, "planted": float("nan")}, **kw)
            return real_aw(path, obj, **kw)
        return w, calls_w
    wr = {}
    for tag_, at, how in (("w1", 1, "enospc"), ("w2", 2, "enospc"), ("w13", 13, "enospc"), ("wnan", 1, "nan")):
        w, calls_w = failing_write(at, how)
        wr[tag_] = stub_run(rule_default, tag_, extra_cms=[mock.patch.object(rs, "atomic_write_json", w)]), calls_w
    (rc1, o1, e1, f1, _, _, _), c1 = wr["w1"]
    (rc2, o2, e2, f2, d2, _, _), c2 = wr["w2"]
    (rc13, o13, e13, f13, d13, s13, _), c13 = wr["w13"]
    (rcn, on, en, fn_, _, _, _), cn = wr["wnan"]
    first_t = d2[0]["record"]["transcript"].split("\n")[:-1] if d2 else ["<none>"]
    chk("mf3_sessions smoke: a write that fails is a STOP, not a traceback (exit 4, OUT DIR with the errno's name), "
        "after the session's block was printed and with no temp file left -- at the first session's write: one block "
        "(its transcript and its line reads), no file; at the second: the first session's file, its reads inside, and "
        "two blocks; at summary.json: the twelve session files, no summary, and no tally or rule printed (A-m2 v0.3 "
        "§3.3); a record that does not serialize (NaN) is a STOP too (SERIALIZE), nothing written",
        rc1 == 4 and "OUT DIR" in e1 and "ENOSPC" in e1 and o1.count("SMOKE SESSION ") == 1 and "\n  | " in o1
        and "\n  line " in o1 and f1 == [] and c1 == ["01_F-0_A1s.json"]
        and rc2 == 4 and "OUT DIR" in e2 and f2 == ["01_F-0_A1s.json"] and d2[0]["lines"] is not None
        and o2.count("SMOKE SESSION ") == 2 and all(("  | " + _printable(ln) + "\n") in o2 for ln in first_t)
        and rc13 == 4 and "summary.json" in e13 and len(f13) == 12 and s13 is None and o13.count("SMOKE SESSION ") == 12
        and "stopped" not in e13 and "selects nothing" not in e13
        and len(c13) == 13 and c13[-1] == "summary.json"
        and rcn == 4 and "SERIALIZE" in en and "ValueError" in en and fn_ == []
        and all(no_rule(x) for x in (o1, o2, o13, on))
        and not any(n.endswith(".tmp") for n in (*f1, *f2, *f13, *fn_)),
        [(r_[0][0], len(r_[0][3]), r_[0][2][-90:]) for r_ in wr.values()])
    calls_fs: list = []

    def fsync_fails_at_summary(d):
        calls_fs.append(1)
        if len(calls_fs) == 13:
            raise OSError(errno.EIO, "Input/output error")
        return real_fsync_dir(d)
    rc_f, out_f, err_f, files_f, _, summ_f, _ = stub_run(
        rule_default, "fsync", extra_cms=[mock.patch.object(rs.m_resume, "_fsync_dir", fsync_fails_at_summary)])
    chk("mf3_sessions smoke: a directory fsync that fails after summary.json is replaced is a STOP (exit 4, OUT DIR "
        "EIO, 'summary.json is on disk'), and the summary is renamed summary.json.stopped: no summary.json is left as a "
        "selection and no tally or rule is printed (A-m2 v0.3 §3.3; round-4 NOTE 3)",
        rc_f == 4 and "OSError EIO writing summary.json; summary.json is on disk" in err_f
        and "renamed summary.json.stopped" in err_f and "summary.json" not in files_f
        and "summary.json.stopped" in files_f and len(files_f) == 13 and summ_f is None and no_rule(out_f),
        (rc_f, files_f[-2:], err_f[-200:]))
    rc_m, out_m, err_m, files_m, _, _, made_m = stub_run(
        rule_default, "mkdir", extra_cms=[mock.patch.object(Path, "mkdir", side_effect=OSError(errno.ENOSPC, "No space"))])
    rc_a, out_a, err_a, files_a, _, _, made_a = stub_run(rule_default, "appeared", pre_load=lambda o: o.mkdir())

    def swap_parent(o):
        par = o.parent
        par.rename(par.with_name("p0"))
        par.with_name("p1").mkdir()
        par.symlink_to(par.with_name("p1"))
    rc_w, out_w, err_w, files_w, _, _, made_w = stub_run(rule_default, "swapped", pre_load=swap_parent)
    chk("mf3_sessions smoke: the output directory -- a mkdir that fails is a STOP naming its errno (exit 4, OSError "
        "ENOSPC making the output directory); a directory that appeared during the load, and a parent swapped for a "
        "link during it, are refused when the directory is re-checked just before it is made (exit 4); in all three "
        "no session runs and nothing is written (round-4 NOTEs 4 and 6)",
        rc_m == 4 and "OSError ENOSPC making the output directory" in err_m and "SMOKE SESSION" not in out_m
        and not made_m and rc_a == 4 and "re-checked before it is made" in err_a and ": exists;" in err_a
        and "SMOKE SESSION" not in out_a and made_a and files_a == [] and no_rule(out_m) and no_rule(out_a)
        and rc_w == 4 and "re-checked before it is made" in err_w and "it now resolves to" in err_w
        and "SMOKE SESSION" not in out_w and not made_w and no_rule(out_w),
        (rc_m, err_m[-120:], rc_a, err_a[-160:], rc_w, err_w[-200:]))
    calls_sv2: list = []
    calls_ssl2: list = []

    def sv_fail_third2(rec, form, cell, **kw):
        calls_sv2.append(1)
        return ["BREAK: planted"] if len(calls_sv2) == 3 else real_sv(rec, form, cell, **kw)

    def ssl_fail_third(k, form, rec, problems):
        calls_ssl2.append(1)
        if len(calls_ssl2) == 3:
            raise KeyError("planted-block")
        return real_ssl(k, form, rec, problems)
    with gpatch("smoke_verify", sv_fail_third2), gpatch("smoke_session_lines", ssl_fail_third):
        rc_g2, out_g2, err_g2, files_g2, _, _, _ = stub_run(rule_default, "gver-block")
    chk("mf3_sessions smoke: a G-VER problem and a block part that raises in the same session are both named on the "
        "STOP line (exit 4; three session files; round-4 NOTE 4)",
        rc_g2 == 4 and "G-VER" in err_g2 and "BREAK: planted" in err_g2 and "planted-block" in err_g2
        and len(files_g2) == 3 and no_rule(out_g2), (rc_g2, err_g2[-200:]))
    calls_lr3: list = []
    calls_ssl3: list = []

    def lr_fail_first(rec):
        calls_lr3.append(1)
        if len(calls_lr3) == 1:
            raise ValueError("planted-reads")
        return real_lr(rec)

    def ssl_fail_first(k, form, rec, problems):
        calls_ssl3.append(1)
        if len(calls_ssl3) == 1:
            raise KeyError("planted-block3")
        return real_ssl(k, form, rec, problems)
    with gpatch("smoke_line_reads", lr_fail_first), gpatch("smoke_session_lines", ssl_fail_first):
        rc_rb, out_rb, err_rb, files_rb, _, _, _ = stub_run(rule_default, "reads-block")
    calls_sv4: list = []

    def sv_fail_fifth(rec, form, cell, **kw):
        calls_sv4.append(1)
        return ["BREAK: planted5"] if len(calls_sv4) == 5 else real_sv(rec, form, cell, **kw)
    with gpatch("smoke_verify", sv_fail_fifth):
        rc_gh, out_gh, err_gh, files_gh, _, _, _ = stub_run(rule_hair, "gver-hair")
    calls_lr5: list = []
    calls_ssl5: list = []

    def lr_fail_fifth(rec):
        calls_lr5.append(1)
        if len(calls_lr5) == 5:
            raise ValueError("planted-reads5")
        return real_lr(rec)

    def ssl_fail_fifth(k, form, rec, problems):
        calls_ssl5.append(1)
        if len(calls_ssl5) == 5:
            raise KeyError("planted-block5")
        return real_ssl(k, form, rec, problems)
    with gpatch("smoke_line_reads", lr_fail_fifth):
        rc_rh, out_rh, err_rh, files_rh, _, _, _ = stub_run(rule_hair, "reads-hair")
    with gpatch("smoke_session_lines", ssl_fail_fifth):
        rc_bh, out_bh, err_bh, files_bh, _, _, _ = stub_run(rule_hair, "block-hair")
    fired_too = "a task-round scaffold_absorption fired too"
    chk("mf3_sessions smoke: every stop a session carries is named on its G-VER, READS or RAW BLOCK line -- a line read "
        "and a block part that raise (READS, both errors); and in the session whose task round fired "
        "scaffold_absorption, a G-VER problem, a line read that raises and a block part that raises (G-VER, READS and "
        "RAW BLOCK, the fire named on each); exit 4, no tally or rule (round-5 NOTE 4, round-6 NOTE 2)",
        rc_rb == 4 and "READS" in err_rb and "planted-reads" in err_rb and "planted-block3" in err_rb
        and len(files_rb) == 1 and rc_gh == 4 and "BREAK: planted5" in err_gh and fired_too in err_gh
        and len(files_gh) == 5 and rc_rh == 4 and "READS" in err_rh and "planted-reads5" in err_rh
        and fired_too in err_rh and len(files_rh) == 5 and rc_bh == 4 and "RAW BLOCK" in err_bh
        and "planted-block5" in err_bh and fired_too in err_bh and len(files_bh) == 5
        and all(no_rule(x) for x in (out_rb, out_gh, out_rh, out_bh)),
        (rc_rb, err_rb[-120:], rc_gh, err_gh[-120:], rc_rh, err_rh[-120:], rc_bh, err_bh[-120:]))

    # --- the out directory pinned after its mkdir (round-5 NOTE 2): a parent swapped for a link, or the directory
    # replaced, during the run is refused before the next write, so nothing lands elsewhere
    pinh: dict = {}

    def rule_swap_mid(f, t, kind, i, call):
        if "out" in pinh and not pinh.get("swapped"):
            pinh["swapped"] = True
            par = pinh["out"].parent
            par.rename(par.with_name("p0"))
            (par.with_name("p1") / pinh["out"].name).mkdir(parents=True)
            par.symlink_to(par.with_name("p1"))
        return rule_default(f, t, kind, i, call)

    def post_swap(o):
        orig, other = o.parent.with_name("p0") / o.name, o.parent.with_name("p1") / o.name
        pinh["orig"] = sorted(x.name for x in orig.iterdir()) if orig.is_dir() else None
        pinh["other"] = sorted(x.name for x in other.iterdir()) if other.is_dir() else None
    rc_x, out_x, err_x, files_x, _, _, _ = stub_run(rule_swap_mid, "midswap", pre_load=lambda o: pinh.__setitem__("out", o),
                                                     post=post_swap)
    reph: dict = {}

    def rule_replace_mid(f, t, kind, i, call):
        if "out" in reph and not reph.get("replaced"):
            reph["replaced"] = True
            o = reph["out"]
            o.rename(o.with_name(o.name + "-orig"))
            o.mkdir()
        return rule_default(f, t, kind, i, call)
    rc_y, out_y, err_y, files_y, _, _, _ = stub_run(rule_replace_mid, "midrepl",
                                                     pre_load=lambda o: reph.__setitem__("out", o))
    lateh: dict = {"n": 0}

    def write_then_swap(path, obj, **kw):
        real_aw(path, obj, **kw)
        lateh["n"] += 1
        if lateh["n"] == 12:                                # after the twelfth session's write, before the summary
            par = Path(path).parent.parent
            par.rename(par.with_name("p0"))
            (par.with_name("p1") / Path(path).parent.name).mkdir(parents=True)
            (par.with_name("p1") / Path(path).parent.name / "summary.json").write_text('{"decoy": 1}')   # round-6 NOTE 1
            par.symlink_to(par.with_name("p1"))

    def post_late(o):
        orig, other = o.parent.with_name("p0") / o.name, o.parent.with_name("p1") / o.name
        lateh["orig"] = sorted(x.name for x in orig.iterdir()) if orig.is_dir() else None
        lateh["other"] = sorted(x.name for x in other.iterdir()) if other.is_dir() else None
        lateh["decoy"] = (other / "summary.json").read_text() if (other / "summary.json").is_file() else None
    rc_z, out_z, err_z, files_z, _, _, _ = stub_run(
        rule_default, "lateswap", extra_cms=[mock.patch.object(rs, "atomic_write_json", write_then_swap)], post=post_late)
    remh: dict = {}

    def rule_remove_mid(f, t, kind, i, call):
        if "out" in remh and not remh.get("removed"):
            remh["removed"] = True
            remh["out"].rmdir()                             # empty: session 1 has written nothing yet
        return rule_default(f, t, kind, i, call)
    rc_q, out_q, err_q, files_q, _, _, made_q = stub_run(rule_remove_mid, "midrm",
                                                         pre_load=lambda o: remh.__setitem__("out", o))
    chk("mf3_sessions smoke: the out directory is pinned after its mkdir -- a parent swapped for a link during the "
        "first session, the directory replaced at its own path during it, the directory removed during it, and a "
        "parent swapped after the twelfth session's write are each refused before the next write (exit 4, 'before "
        "writing'; a removed one as 'cannot be examined'); nothing lands in the swapped-in directory, a summary.json "
        "already there is neither renamed nor removed, and no tally, rule or summary.json follows (round-5 NOTE 2, "
        "round-6 NOTEs 1 and 3)",
        rc_x == 4 and "before writing 01_F-0_A1s.json" in err_x and "it now resolves to" in err_x
        and pinh.get("orig") == [] and pinh.get("other") == [] and files_x == []
        and rc_y == 4 and "before writing 01_F-0_A1s.json" in err_y
        and "no longer the directory the smoke made" in err_y and files_y == []
        and rc_q == 4 and "before writing 01_F-0_A1s.json" in err_q and "cannot be examined (FileNotFoundError)" in err_q
        and not made_q and no_rule(out_q)
        and rc_z == 4 and "before writing summary.json" in err_z and lateh.get("other") == ["summary.json"]
        and lateh.get("decoy") == '{"decoy": 1}' and "the output directory moved, so nothing under it was" in err_z
        and "renamed summary.json" not in err_z
        and lateh.get("orig") is not None and len(lateh["orig"]) == 12 and "summary.json" not in lateh["orig"]
        and all(no_rule(x) for x in (out_x, out_y, out_z)),
        (rc_x, err_x[-140:], rc_y, err_y[-140:], rc_z, err_z[-140:], pinh.get("other"), lateh.get("other")))

    # --- _summary_stopped (round-5 NOTE 1): what a failed summary write leaves is renamed, removed or reported -----
    def ss_case(names, faults):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            for n in names:
                (d / n).write_text("{}")
            with contextlib.ExitStack() as es:
                for fname, nm, code in faults:
                    def make_fault(real_fn=getattr(os, fname), nm=nm, code=code):
                        def f(*a, **k):
                            if a and Path(os.fsdecode(a[0])).name == nm:
                                raise OSError(code, os.strerror(code))
                            return real_fn(*a, **k)
                        return f
                    es.enter_context(mock.patch.object(os, fname, make_fault()))
                tail = _summary_stopped(d / "summary.json")
            left = sorted(p.name for p in d.iterdir())
        return tail, left
    EIO = errno.EIO
    ss = {"renamed": ss_case(["summary.json"], []),
          "removed": ss_case(["summary.json"], [("rename", "summary.json", EIO)]),
          "both fail": ss_case(["summary.json"], [("rename", "summary.json", EIO), ("unlink", "summary.json", EIO)]),
          "unknown": ss_case(["summary.json"], [("lstat", "summary.json", EIO)]),
          "tmp left": ss_case(["summary.json.tmp"], []),
          "nothing": ss_case([], [])}
    end = "; a stopped smoke selects nothing (A-m2 v0.3 §3.3)"
    chk("mf3_sessions smoke: after a failed summary write, a summary.json on disk is renamed .stopped, or removed "
        "when the rename fails; when both fail, or its presence cannot be examined, the STOP line says it is not a "
        "selection; a summary.json.tmp left by m's failed cleanup is renamed too; with nothing on disk there is no "
        "tail (round-5 NOTE 1)",
        ss["renamed"] == ("; summary.json renamed summary.json.stopped" + end, ["summary.json.stopped"])
        and ss["removed"] == ("; summary.json could not be renamed (OSError EIO) and was removed" + end, [])
        and ss["both fail"] == ("; summary.json is on disk, its rename (OSError EIO) and its removal (OSError EIO) "
                                "failed: it is not a selection" + end, ["summary.json"])
        and ss["unknown"] == ("; whether summary.json is on disk is unknown (OSError EIO): if it is, it is not a "
                              "selection" + end, ["summary.json"])
        and ss["tmp left"] == ("; summary.json.tmp renamed summary.json.tmp.stopped" + end, ["summary.json.tmp.stopped"])
        and ss["nothing"] == ("", []), ss)
    mut_am2 = t0.replace("So far,", "So far;", 1).encode("utf-8")
    n_pre = len(ckpt_calls)
    with contextlib.ExitStack() as es:
        for cm in [mock.patch.object(stages, "committed", lambda rel, repo=stages.REPO: ([], mut_am2)
                                     if rel == ADDENDUM_M2_REL else real_committed(rel, repo)), *traps()]:
            es.enter_context(cm)
        try:
            pre_m = smoke_precheck(extra0)
        except SystemExit as e:                                 # a trap reached: reported as a failed check
            pre_m = [f"trap: {e}"]
    with contextlib.ExitStack() as es:
        for cm in [gpatch("SMOKE_FORMS", SMOKE_FORMS[:3] + (("F-c", "[round {n} | reasoning]\nGive one line on ridge.\n"),)),
                   *traps()]:
            es.enter_context(cm)
        try:
            pre_f = smoke_precheck(extra0)
        except SystemExit as e:                                 # a trap reached: reported as a failed check
            pre_f = [f"trap: {e}"]
    pre_clean = not opened_ckpt and len(ckpt_calls) == n_pre
    chk("mf3_sessions smoke: the precheck runs m:258's admissibility on the forms (a planted roster word in a form gives "
        "a 'forms:' problem)", any(x.startswith("forms:") and "ridge" in x for x in pre_f),
        [x for x in pre_f if x.startswith("forms")][:1])
    chk("mf3_sessions smoke: the precheck refuses an A-m2 whose committed bytes differ from the pin (an 'addendum:' "
        "problem); run under the traps, it reaches no checkpoint function and opens nothing under data/mf3/ckpt, and "
        "names no checkpoint", any(x.startswith("addendum:") for x in pre_m) and pre_clean
        and not any("checkpoint" in x.lower() for x in pre_m), [x for x in pre_m if x.startswith("addendum")][:1])
    chk("mf3_sessions smoke: nothing under data/mf3 changed across the smoke's self-test (the tree hashed before and "
        "after); no trapped smoke path opened a file under data/mf3/ckpt, made a guarded write inside the "
        "repository, reached a checkpoint function or the stage, or loaded the model; open(), io.open, os.open, "
        "os.mkdir, os.replace, os.rename, Path.mkdir, mf3.resume's atomic_write_json, m's _fsync_dir and "
        "scaffold.f3_config are the originals again; every stub run (24) had its traps in place at the load, and "
        "every traps() site entered (35) had them in place",
        tree_state(data_root) == data_before and not opened_ckpt and not wrote_repo and not ckpt_calls and not loads
        and builtins.open is real_open and io.open is real_io_open and os.open is real_os_open and os.mkdir is real_mkdir
        and os.replace is real_replace and os.rename is real_rename and Path.mkdir is real_path_mkdir
        and all(trapped_at_load) and len(trapped_at_load) == 24 and all(traps_entered) and len(traps_entered) == 35
        and os.unlink is real_unlink and os.remove is real_remove
        and rs.atomic_write_json is real_aw and rs.m_resume._fsync_dir is real_fsync_dir
        and sc_mod.f3_config is real_cfg0,
        (len(opened_ckpt), wrote_repo[:2], ckpt_calls[:3], len(loads), len(trapped_at_load), len(traps_entered)))


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
    t.add_argument("--smoke", action="store_true", help="A-m2's smoke (A-m2 §3): twelve sham sessions in four "
                                                       "reasoning-block forms, never of record")
    t.add_argument("--smoke-out", default=None, help="the smoke's output directory: outside the repository, "
                                                     "not existing")
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
    if a.cmd == "time" and a.smoke:
        if a.resume:
            print("refused: time --smoke takes no --resume (the smoke keeps no checkpoint)", file=sys.stderr)
            return 2
        return run_smoke(proposal_file=a.proposal_file, lock_file=a.lock_file, analyzer_sha256=a.analyzer_sha256,
                         package_sha256=a.package_sha256, renders_sha16=a.renders_sha16, smoke_out=a.smoke_out)
    if a.cmd == "time" and a.smoke_out is not None:
        print("refused: --smoke-out names the smoke's directory; it needs --smoke", file=sys.stderr)
        return 2
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
