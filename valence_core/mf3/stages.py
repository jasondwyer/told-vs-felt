"""Q-F3's gate-stage and campaign drivers (PROPOSAL-m v1.11 §2.4 m:192, m:247-249; §2.7 m:267; §3 m:271;
§3.2 m:293-298; §4 m:308, m:316, m:318; §6 m:330; ADDENDUM-m1 decision (10') and §4 step 5; the design
seat's prebuild answers of 2026-11-06, Q1 and Q5).

THE STAGES. ``run_gate_stage`` runs G-TIME-F3 (m:293: one session per arm, uncached, the reasoning
lines at 60, the cap trigger counted over all six) and G-F3 (m:297: 40 sessions); ``run_gid_pair_f3``
runs G-ID-F3 (m:295: A2s then A3s, uncached then cached at each index, indices advancing per template
as G-ID-F0m's, m:281, until a complete pair exists; 2/2 byte-identical); ``run_campaign`` runs the
campaign (m:192, m:247, m:330: the six-arm strict-rotation interleave, per-arm stop at floor on DOMAIN
sessions, looks every 40 launches and at the end, the hour cap and a PI stop terminal). Every stage is
built and self-tested on the scripted stub; none is wired in the driver at the build (each subcommand
waits for its step's word).

THE FORMS are ``valence_core.m.stages``'s, which mf3 may not import (the seat's Q1: it reaches
runner_olmo; N1): every rule of m's driver contract is carried here and named where it is applied --
at every stage start the stub guard, the non-stub out root (REPO/data/mf3), an ENDED checkpoint
refused, the adapter's provenance checked, the run-time known answers (numpy's stream, the six F3
banners and the reasoning block against the proposal FILE, roster hygiene, the import set), the
laptop checklist and gate line (non-stub), the licence (C2: the proposal and lock committed, the
analyzer's, mf3's and each imported m module's sha256 as identity_extra and the lock name them, and the
weights of record), the prior stage's persisted end; per session the committed schedule's cell, the
F3 scaffold, the runner, G-VER BEFORE the record is written; every finish in three steps (end pending
with every session, then the pick-free outputs, then the end persisted); a checkpoint carrying an end
pending re-finishes only.

BLINDING (m:318). Stdout carries the PROVENANCE line, ``readrule.session_line`` per session, the bars'
blinded messages, the stage's end line (a gate stage STOP or PASS; G-ID-F3 also FAIL or NOT-DETERMINED;
the campaign COMPLETE, CAP, PI-STOP, PAUSE or STOP) and file paths. A hair trigger in a contrast
session's free phase -- a reasoning line after its first pick included -- is announced by phase alone.
Reports carry no contrast pick and no contrast session's time; G-TIME-F3's contrast block is ruling
(h)'s counts plus the per-line cap booleans (the seat's Q5); the cap-trigger count is reported over all
six sessions (m:293: "cap-reach counted over all six"; the seat's Q5).
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from valence_core.m import corr as m_corr
from valence_core.m import keys as m_keys

from . import banner, bars, guard, keys, readrule, runner, schedule, verify
from . import resume as rs
from . import scaffold as sc_mod

REPO = Path(__file__).resolve().parents[2]
DEFAULT_OUT = REPO / "data" / "mf3"
PROPOSAL_PATH = REPO / "PROPOSAL-m-gating-campaign-v1_11.md"
PROPOSAL_REL = PROPOSAL_PATH.relative_to(REPO).as_posix()
CLAUDE_MD_PATH = REPO / "CLAUDE.md"
# PIN (Code, declared at LOCK-m-F3 v0.1): the analyzer the gate line logs and the licence hashes is
# scripts/m_analyze.py, which G-ANL-F3 extends in place (m:291; the seat's Q3); LOCK-m-F3 v0.1 names
# the extended blob (m:292).
ANALYZER_PATH = REPO / "scripts" / "m_analyze.py"
REPORT_SCHEMA = "m-stage-report-v1"
READS_SCHEMA = "m-stage-reads-v1"
GID_SCHEMA = "m-gid-v1"
ADJ_SCHEMA = "m-adjudication-v1"
GATES = ("time", "qual")
LOOK_EVERY = rs.LOOK_EVERY
STUB_MARK = "SELFTEST-STUB"
WITHHELD_CLASS = "withheld to the unit's VERDICTS entry or NOT-RUN record (m:318 exception (1))"
TERMINAL = ("COMPLETE", "CAP", "PI-STOP")
EXIT_CODES = {"PASS": 0, "COMPLETE": 0, "CAP": 0, "PI-STOP": 0, "PAUSE": 3, "STOP": 4, "FAIL": 5, "NOT-DETERMINED": 6}
STAGE_NAMES = {"time": "G-TIME-F3", "id": "G-ID-F3", "qual": "G-F3", "campaign": f"campaign-{keys.UNIT}"}
#: m:174: "if ≥ 3 of the reasoning lines G-TIME-F3 generates (≤ 36) reach the cap without a newline,
#: the reasoning-line cap becomes 120 (pre-declared)".
CAP_TRIGGER = 3
CAP_AFTER_TRIGGER = 120
_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_HEX40 = re.compile(r"^[0-9a-f]{40}$")
_HEX16 = re.compile(r"^[0-9a-f]{16}$")
_ROSTER_RX = re.compile(r"\b(?:" + "|".join(re.escape(w) for w in sorted({x for p in schedule.roster() for x in p}))
                        + r")\b", re.IGNORECASE)


def exit_code(status: str) -> int:
    if status not in EXIT_CODES:
        raise ValueError(f"unknown stage status {status!r}")
    return EXIT_CODES[status]


def stage_name(stage: str) -> str:
    if stage not in STAGE_NAMES:
        raise ValueError(f"{stage!r} is not a Q-F3 stage")
    return STAGE_NAMES[stage]


# --- paths ---------------------------------------------------------------------------------
def out_paths(stage: str, out_root=DEFAULT_OUT) -> dict[str, Path]:
    """PIN (Code, declared at LOCK-m-F3 v0.1): m's layout under data/mf3 -- schedules/ (read only),
    ckpt/Q-F3_{stage}.json (pick-bearing; -diff), reports/Q-F3_{stage}_report.json and _reads.json (no
    contrast pick), G-ID-F3's artifact at guard.gid_artifact_path()."""
    stage_name(stage)
    root = Path(out_root)
    return {"root": root, "schedules": root / "schedules", "ckpt": root / "ckpt" / f"{keys.UNIT}_{stage}.json",
            "report": root / "reports" / f"{keys.UNIT}_{stage}_report.json",
            "reads": root / "reports" / f"{keys.UNIT}_{stage}_reads.json"}


def for_checkpoint(paths: Mapping[str, Path], cpath: Path) -> dict[str, Path]:
    rd = Path(paths["root"]) / "reports"
    stem = Path(cpath).stem
    return {**paths, "ckpt": Path(cpath), "report": rd / f"{stem}_report.json", "reads": rd / f"{stem}_reads.json"}


def checkpoint_path(ckpt_path, paths: Mapping[str, Path]) -> Path:
    """m's checkpoint-path PIN: <out_root>/ckpt/<name>.json, no roster word, not *_adjudication."""
    cp = Path(ckpt_path) if ckpt_path is not None else Path(paths["ckpt"])
    want = (Path(paths["root"]) / "ckpt").resolve()
    r = cp.expanduser().resolve()
    if r.parent != want or r.suffix != ".json" or not r.stem:
        raise SystemExit(f"CHECKPOINT PATH REFUSED: {cp} resolves to {r}; a checkpoint is {want}/<name>.json (m:318)")
    if _ROSTER_RX.search(str(r)):
        raise SystemExit(f"CHECKPOINT PATH REFUSED: {r} names a roster word (m:318)")
    if r.stem.endswith("_adjudication"):
        raise SystemExit(f"CHECKPOINT PATH REFUSED: {r.name} -- '_adjudication' names the excerpt beside a checkpoint")
    return r


def adjudication_path(cpath: Path) -> Path:
    return Path(cpath).with_name(f"{Path(cpath).stem}_adjudication.json")


def _rel(p: Path, root: Path) -> str:
    try:
        return str(Path(p).resolve().relative_to(Path(root).resolve()))
    except ValueError:
        return str(p)


def _is_stub(adapter) -> bool:
    prov = adapter.provenance() if hasattr(adapter, "provenance") else {}
    return any(STUB_MARK in str(prov.get(k, "")) for k in ("adapter", "apparatus"))


def _stub_guard(adapter, *paths: Path) -> None:
    if _is_stub(adapter):
        for p in paths:
            rs.refuse_canonical_out(p)


def _out_root_guard(adapter, root) -> None:
    if _is_stub(adapter):
        return
    r, want = Path(root).expanduser().resolve(), DEFAULT_OUT.resolve()
    if r != want:
        raise SystemExit(f"OUT ROOT REFUSED: a non-stub Q-F3 run writes under {want} only (ledger 27)")


def _start_provenance(adapter, name: str) -> dict:
    try:
        rec = rs.provenance_record(adapter.provenance())
    except (TypeError, ValueError) as e:
        raise SystemExit(f"PROVENANCE REFUSED ({name}): {e}")
    if _ROSTER_RX.search(json.dumps(rec, sort_keys=True, ensure_ascii=False)):
        raise SystemExit(f"PROVENANCE REFUSED ({name}): the adapter's provenance names a roster word (m:318)")
    return rec


def _append_provenance(ckpt: dict, rec: Mapping) -> None:
    entry = rs.append_provenance(ckpt, rec)
    print("PROVENANCE: " + json.dumps({"record": entry["record"], "stamp": entry["stamp"]}, sort_keys=True,
                                      separators=(",", ":"), ensure_ascii=False), flush=True)


# --- run-time known answers, laptop preflight, git -------------------------------------------
def startup_problems(proposal_path=PROPOSAL_PATH) -> list[str]:
    """numpy's stream, the F3 banners and reasoning block against the proposal FILE, roster hygiene of
    the pool, golds and the eight harness strings, and the licence's import set (static); [] = clean."""
    probs = [f"keys: {p}" for p in m_keys.stream_known_answer()]
    probs += [f"banner: {p}" for p in banner.spec_problems(Path(proposal_path))]
    probs += [f"corr: {p}" for p in m_corr.startup_hygiene()]
    probs += [f"imports: {p}" for p in guard.import_problems(runtime=False)]
    return probs


def _startup_checks(name: str, proposal_path) -> None:
    probs = startup_problems(proposal_path)
    if probs:
        raise SystemExit(f"STARTUP CHECKS FAIL ({name}): {probs[:5]} -- no session runs (m:159, m:258, rule 18)")


def _proposal_path(extra: Mapping[str, Any]) -> Path:
    return REPO / extra["proposal_file"]


def _git(*args: str, repo=REPO, binary: bool = False) -> subprocess.CompletedProcess:
    """A READ-ONLY git query (cat-file, ls-tree, rev-parse) -- never diff or status (m's finding R4)."""
    return subprocess.run(["git", *args], capture_output=True, text=not binary, cwd=repo)


def _git_head(repo=REPO) -> str:
    try:
        r = _git("rev-parse", "--verify", "HEAD", repo=repo)
    except OSError:
        return "unknown"
    out = (r.stdout or "").strip() if r.returncode == 0 else ""
    return out if re.match(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$", out) else "unknown"


def committed(rel: str, repo=REPO) -> tuple[list[str], bytes | None]:
    """m's committed-blob check (finding R4), carried: committed at HEAD as one regular blob, the working
    tree's bytes exactly HEAD's (no symlink on the path); git object reads only."""
    def gerr(r) -> str:
        e = r.stderr or b""
        e = e.decode("utf-8", "replace") if isinstance(e, bytes) else e
        return (e.strip().splitlines() or [""])[0][:120]
    try:
        r = _git("cat-file", "-e", f"HEAD:{rel}", repo=repo)
        if r.returncode != 0:
            return [f"{rel}: not committed at HEAD (git: {gerr(r)})"], None
        lt = _git("ls-tree", "-z", "HEAD", "--", rel, repo=repo)
        ents = [e for e in (lt.stdout or "").split("\0") if e]
        if lt.returncode != 0 or len(ents) != 1 or "\t" not in ents[0]:
            return [f"{rel}: HEAD's tree entry is not one file"], None
        meta, epath = ents[0].split("\t", 1)
        f = meta.split()
        mode, typ = (f[0], f[1]) if len(f) >= 2 else ("?", "?")
        if epath != rel or mode == "120000" or typ != "blob" or mode not in ("100644", "100755"):
            return [f"{rel}: not a regular file at HEAD ({mode} {typ})"], None
        blob = _git("cat-file", "blob", f"HEAD:{rel}", repo=repo, binary=True)
        if blob.returncode != 0 or not isinstance(blob.stdout, bytes):
            return [f"{rel}: HEAD's blob unreadable"], None
    except OSError as e:
        return [f"{rel}: git unavailable ({type(e).__name__})"], None
    wt = Path(repo) / rel
    try:
        if wt.is_symlink() or wt.resolve() != Path(repo).resolve() / rel or not wt.is_file():
            return [f"{rel}: the working-tree path is not a regular file at that path"], None
        data = wt.read_bytes()
    except OSError:
        return [f"{rel}: unreadable in the working tree"], None
    if data != blob.stdout:
        return [f"{rel}: working-tree bytes are not HEAD's blob (uncommitted edits)"], None
    return [], data


def gate_line(name: str, proposal_path=PROPOSAL_PATH) -> tuple[str, list[str]]:
    """m:267's gate line (proposal, CLAUDE.md, analyzer and HEAD hashes) and its problems."""
    probs, hs = [], {}
    for k, p in (("proposal", Path(proposal_path)), ("CLAUDE.md", CLAUDE_MD_PATH), ("analyzer", ANALYZER_PATH)):
        try:
            hs[k] = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
        except OSError:
            probs.append(f"GATE LINE: {k} absent at {p}")
            hs[k] = "ABSENT"
    head = _git_head()
    if head == "unknown":
        probs.append("GATE LINE: HEAD unknown")
    return (f"GATE {name}: proposal {_rel(Path(proposal_path), REPO)} {hs['proposal']}, CLAUDE.md {hs['CLAUDE.md']}, "
            f"analyzer {_rel(ANALYZER_PATH, REPO)} {hs['analyzer']}, HEAD {head}"), probs


def _laptop_preflight(adapter, name: str, extra: Mapping[str, Any]) -> bool:
    """m:267's laptop checklist (power, one model process, disk; guard.preflight_laptop, imported) and
    the gate line's files committed (m's PIN, carried); a stub run skips it."""
    if _is_stub(adapter):
        return False
    probs = list(guard.preflight_laptop())
    line, gp = gate_line(name, _proposal_path(extra))
    probs += gp
    for what, path in (("CLAUDE.md", CLAUDE_MD_PATH), ("analyzer", ANALYZER_PATH)):
        probs += [f"GATE LINE: {what} {x}" for x in committed(path.relative_to(REPO).as_posix())[0]]
    if probs:
        raise SystemExit(f"LAPTOP PREFLIGHT REFUSES {name}: {probs} (m:267's checklist)")
    print(line, flush=True)
    return True


# --- the licence (C2) ------------------------------------------------------------------------
def licence_problems(extra: Mapping[str, Any], *, repo=REPO, hub_repo=None, environ=None) -> list[str]:
    """The licence for a non-stub Q-F3 stage; [] = licensed.

    (a) HEAD known; (b) the proposal file committed with the working tree's bytes, its sha256 the
    identity's; (c) the lock file likewise; (d) the analyzer's bytes hash to ``analyzer_sha256``; (e) mf3's
    package as this process hashes it now is ``package_sha256`` (Q1 (C2) part (a)); (e') each valence_core.m
    file of ``guard.M_HASHED`` as hashed now is ``m_module_sha256``'s (part (b)); (f) the committed lock's
    text names the analyzer's and mf3's sha256 verbatim and each m file by name, its path and sha256 on one
    line (part (b): "listed by name"); (g) the weights of record -- HF_HUB_OFFLINE is exactly "1", the hub
    cache's refs/main for the model of record names ``weights_revision``, the binding computed now on that
    snapshot is ``weights_revision`` / ``weights_sha256``, and the lock names both."""
    # PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q1 (C2): "Every non-stub mf3 stage checks both at
    # start, as stages.py:530–608 checks m's"): m's (a)-(f), with (e) mf3's package and (e') the files
    # N1 and the build review's finding 7 declare (guard.M_HASHED), plus (g) Q6's weights binding. (f)'s
    # one-line naming of each m file and (g)'s offline and refs/main conditions are the build review's
    # findings 8 and 5: the load (jlens_qwen.model.load -> the hub's resolution of refs/main) must read the
    # snapshot the binding hashes. The rest of m's pre-load check (scripts/m_sessions.py: MLXLM_USE_MODELSCOPE,
    # a local path named like the model id, the hub's own offline resolution, the SNAPSHOT line) is the
    # driver's, built with the stage wiring (flag F-2).
    probs: list[str] = []
    if _git_head(repo) == "unknown":
        probs.append("HEAD unknown (git rev-parse --verify HEAD failed)")
    lock_data = None
    for what, rel, want in (("proposal", extra.get("proposal_file"), extra.get("proposal_sha256")),
                            ("lock", extra.get("lock_file"), extra.get("lock_sha256"))):
        if rel is None:
            probs.append(f"{what}: no file named (identity_extra {what}_file is required on a non-stub run)")
            continue
        cp, data = committed(rel, repo)
        probs += [f"{what} {x}" for x in cp]
        if data is None:
            continue
        if what == "lock":
            lock_data = data
        if hashlib.sha256(data).hexdigest() != want:
            probs.append(f"{what} {rel}: sha256 is not identity_extra's")
    named: dict[str, str] = {}
    for k in ("analyzer_sha256", "package_sha256", "weights_sha256"):
        v = extra.get(k)
        if type(v) is str and _HEX64.match(v):
            named[k] = v
        else:
            probs.append(f"{k}: identity_extra carries none (or not 64 lower-case hex); required on a non-stub run")
    wr = extra.get("weights_revision")
    if type(wr) is str and _HEX40.match(wr):
        named["weights_revision"] = wr
    else:
        probs.append("weights_revision: identity_extra carries none (or not 40 lower-case hex)")
    mm = extra.get("m_module_sha256")
    if not isinstance(mm, Mapping) or sorted(mm) != sorted(guard.M_HASHED):
        probs.append(f"m_module_sha256: identity_extra must map each of {guard.M_HASHED} to its sha256")
        mm = {}
    if "analyzer_sha256" in named:
        try:
            got = hashlib.sha256(ANALYZER_PATH.read_bytes()).hexdigest()
        except OSError:
            got = None
        if got != named["analyzer_sha256"]:
            probs.append("analyzer: its sha256 is not identity_extra's analyzer_sha256")
    if "package_sha256" in named and guard.package_sha256_of(guard.PACKAGE_DIR) != named["package_sha256"]:
        probs.append("package valence_core/mf3: its sha256 (computed now) is not identity_extra's package_sha256")
    now = guard.m_module_sha256s()
    for m, v in sorted(mm.items()):
        if now.get(m) != v:
            probs.append(f"valence_core/m/{m}.py: its sha256 (computed now) is not identity_extra's (Q1 (C2) part (b))")
    if "weights_sha256" in named and "weights_revision" in named:
        env = os.environ if environ is None else environ
        if env.get("HF_HUB_OFFLINE") != "1":
            probs.append(f"weights: HF_HUB_OFFLINE is {env.get('HF_HUB_OFFLINE')!r}, not '1' (an online load can move "
                         f"refs/main past the bound revision)")
        hub = rs.hub_repo_dir() if hub_repo is None else Path(hub_repo)
        try:
            refs = (hub / "refs" / "main").read_text(encoding="utf-8")
        except (OSError, ValueError):
            refs = None
        if refs != named["weights_revision"]:
            probs.append(f"weights: the hub cache's refs/main for {rs.QWEN_MODEL_ID} is "
                         f"{'unreadable' if refs is None else repr(refs[:44])}, not the bound revision (raw text) -- the "
                         f"load would read another snapshot")
        try:
            wb = rs.weights_binding(hub / "snapshots" / named["weights_revision"])
            if (wb["revision"], wb["sha256"]) != (named["weights_revision"], named["weights_sha256"]):
                probs.append("weights: the snapshot of record binds differently now (revision or content addresses)")
        except (OSError, ValueError, KeyError) as e:
            probs.append(f"weights: the snapshot of record is unreadable ({type(e).__name__})")
    if lock_data is not None:
        lt = lock_data.decode("utf-8", "replace")
        for k, v in named.items():
            if v not in lt:
                probs.append(f"lock {extra.get('lock_file')}: its committed text does not name {k} {v[:16]}...")
        lock_lines = lt.splitlines()
        for m, v in sorted(mm.items()):
            path = f"valence_core/m/{m}.py"
            if not any(path in ln and v in ln for ln in lock_lines):
                probs.append(f"lock {extra.get('lock_file')}: no line of its committed text names {path} with its "
                             f"sha256 {v[:16]}... (Q1 (C2) part (b): listed by name)")
    return probs


def _licence(adapter, extra: Mapping[str, Any], name: str) -> None:
    if _is_stub(adapter):
        return
    probs = licence_problems(extra)
    if probs:
        raise SystemExit(f"LICENCE REFUSED ({name}): {probs} -- nothing runs before the document, the lock, the code "
                         f"and the weights are the ones the identity and the lock name")
    print(f"LICENCE {name}: proposal {extra['proposal_file']} {extra['proposal_sha256'][:16]}, lock {extra['lock_file']} "
          f"{extra['lock_sha256'][:16]}: committed at HEAD {_git_head()}, working tree identical; analyzer "
          f"{extra['analyzer_sha256'][:16]}, mf3 package {extra['package_sha256'][:16]}, the {len(guard.M_HASHED)} m "
          f"files and the weights {extra['weights_revision'][:12]}: the hashes identity_extra and the lock name, "
          f"hashed at stage start", flush=True)


# --- the prior stage, the G-ID-F3 artifact -----------------------------------------------------
# PIN (Code, declared at LOCK-m-F3 v0.1; m's PRIOR_STAGE carried, m:293-298): G-ID-F3 needs G-TIME-F3
# PASS; G-F3 needs G-TIME-F3 PASS and G-ID-F3's artifact on disk at the run's reasoning cap (any verdict:
# FAIL or NOT-DETERMINED send Q-F3 uncached, m:295); the campaign needs G-F3 PASS.
PRIOR_STAGE = {"id": "time", "qual": "time", "campaign": "qual"}


def written_on_stub(ck: Mapping) -> bool:
    prov = ck.get("provenance")
    if not isinstance(prov, list) or not prov:
        return True
    return any(not isinstance(e, Mapping) or not isinstance(e.get("record"), Mapping)
               or any(STUB_MARK in str(e["record"].get(k, "")) for k in ("adapter", "apparatus")) for e in prov)


def accepted_proposals(proposal_sha256, prior=()):
    return None if proposal_sha256 is None else frozenset((proposal_sha256, *prior))


def gid_artifact_problems(*, accepted, require_real: bool, reasoning_cap: int) -> list[str]:
    p = guard.gid_artifact_path()
    if not p.is_file():
        return []
    try:
        art = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError) as e:
        return [f"G-ID ARTIFACT UNREADABLE at {p} ({type(e).__name__})"]
    ident = art.get("identity") if isinstance(art, Mapping) else None
    if not isinstance(ident, Mapping):
        return [f"G-ID ARTIFACT UNREADABLE at {p} (no identity)"]
    probs = []
    if accepted is not None and ident.get("proposal_sha256") not in accepted:
        probs.append(f"G-ID ARTIFACT UNDER ANOTHER PROPOSAL: {p}")
    if require_real and written_on_stub(art):
        probs.append(f"G-ID ARTIFACT ON THE STUB: {p} licenses no run on a model")
    # PIN (Code, declared at LOCK-m-F3 v0.1; m:174, m:295; the build design's B7): the artifact's cap must
    # be the run's; a cap change after G-ID-F3 sets the artifact aside by git mv to a dated .superseded
    # name and G-ID-F3 re-runs before any later Q-F3 session.
    if ident.get("reasoning_cap") != reasoning_cap:
        probs.append(f"G-ID ARTIFACT AT ANOTHER CAP: {p} ran at reasoning cap {ident.get('reasoning_cap')!r}, this run "
                     f"at {reasoning_cap} -- G-ID-F3 re-runs at the fixed cap (m:174)")
    return probs


def prior_gate(stage: str, prior_ckpt, *, proposal_sha256=None, prior_proposal_sha256s=(),
               require_real: bool = False, reasoning_cap: int | None = None) -> dict:
    name = stage_name(stage)
    want = PRIOR_STAGE.get(stage)
    if want is None:
        if prior_ckpt is not None:
            raise ValueError(f"{name} takes no prior stage (it is the first after its lock)")
        return {}
    if prior_ckpt is None:
        raise SystemExit(f"PRIOR STAGE REQUIRED: {name} runs only after {stage_name(want)}; name its checkpoint")
    p = Path(prior_ckpt)
    if not p.is_file():
        raise SystemExit(f"PRIOR STAGE ABSENT: no checkpoint at {p}")
    ck = rs.read_checkpoint(p)
    ident = ck["identity"]
    if ident.get("unit") != keys.UNIT or ident.get("stage") != want:
        raise SystemExit(f"PRIOR STAGE MISMATCH: {p} is {ident.get('unit')}/{ident.get('stage')}, not {keys.UNIT}/{want}")
    accepted = accepted_proposals(proposal_sha256, prior_proposal_sha256s)
    if accepted is not None and ident.get("proposal_sha256") not in accepted:
        raise SystemExit(f"PRIOR STAGE UNDER ANOTHER PROPOSAL: {p} -- {name} does not run on it")
    if require_real and written_on_stub(ck):
        raise SystemExit(f"PRIOR STAGE ON THE STUB: {p} licenses no run on a model")
    end = ck.get("stage_end")
    status = end.get("status") if isinstance(end, Mapping) else None
    if status is None:
        raise SystemExit(f"PRIOR STAGE NOT ENDED: {stage_name(want)} at {p} has no recorded end")
    if status != "PASS":
        raise SystemExit(f"PRIOR STAGE {status}: {stage_name(want)} ended {status} at {p}; {name} does not run until "
                         f"the seat re-specifies (m:293-297)")
    # PIN (Code, declared at LOCK-m-F3 v0.1; m:174, m:294-296; the build review's finding 4): the cap is fixed by
    # G-TIME-F3's trigger (m:294) and applied from G-ID-F3 on (m:295, before LOCK v0.2 records it, m:296). So G-ID-F3
    # and G-F3 re-compute the trigger from G-TIME-F3's own checkpoint and refuse any other cap, and the campaign runs
    # at G-F3's cap. Only the fixed cap is printed.
    if stage in ("id", "qual"):
        fixed = cap_trigger(ck.get("sessions") or [])["fixed_cap"]
        if reasoning_cap != fixed:
            raise SystemExit(f"NOT THE FIXED CAP: {name} would run at reasoning cap {reasoning_cap!r}; G-TIME-F3's lines "
                             f"at {p} fix the cap at {fixed} (m:174, m:294-295) -- refusing")
    elif stage == "campaign" and ident.get("reasoning_cap") != reasoning_cap:
        raise SystemExit(f"NOT THE FIXED CAP: the campaign would run at reasoning cap {reasoning_cap!r}; G-F3 at {p} ran "
                         f"at {ident.get('reasoning_cap')!r} (m:174) -- refusing")
    if stage == "qual":
        if not guard.gid_artifact_path().is_file():
            raise SystemExit(f"G-ID ARTIFACT ABSENT: {name} runs after G-ID-F3's artifact exists (m:295-297)")
        ap = gid_artifact_problems(accepted=accepted, require_real=require_real, reasoning_cap=reasoning_cap)
        if ap:
            raise SystemExit(f"{ap[0]} -- {name} does not run on it")
    return {"checkpoint": _rel(p, REPO), "stage": want, "status": status, "adjudication": None}


LICENCE_KEYS = ("analyzer_sha256", "lock_file", "m_module_sha256", "package_sha256", "prior_proposal_sha256s",
                "proposal_file", "weights_revision", "weights_sha256")


def _record_licence(ckpt: dict, extra: Mapping[str, Any], where: Path) -> None:
    want = {k: copy.deepcopy(extra.get(k)) for k in LICENCE_KEYS}
    have = ckpt.get("licence")
    if have is None:
        ckpt["licence"] = want
    elif not rs.same_json(have, want):
        raise SystemExit(f"CHECKPOINT MISMATCH: {where} was licensed by other files or hashes -- refusing")


def _record_prior(ckpt: dict, prior: Mapping, where: Path) -> None:
    if not prior:
        return
    have = ckpt.get("prior")
    if have is None:
        ckpt["prior"] = dict(prior)
    elif have.get("status") != prior["status"]:
        raise SystemExit(f"CHECKPOINT MISMATCH: {where} recorded another prior status -- refusing")


# --- committed schedules -------------------------------------------------------------------
def load_committed(wanted: Sequence[tuple[str, str]], sched_dir) -> dict[str, dict]:
    """The committed Q-F3 schedule files a stage runs from: the directory verified clean against the
    construction and the manifest (schedule.verify_schedule_dir), each file's sha256 the manifest's."""
    d = Path(sched_dir)
    probs = schedule.verify_schedule_dir(d)
    if probs:
        raise SystemExit(f"SCHEDULES NOT CLEAN at {d}: {probs[:3]} -- a stage runs only from the committed, verified "
                         f"schedule files (m:159)")
    try:
        manifest = json.loads((d / schedule.MANIFEST_NAME).read_text(encoding="utf-8"))["files"]
    except (OSError, ValueError, KeyError) as e:
        raise SystemExit(f"SCHEDULE MANIFEST UNREADABLE at {d} ({type(e).__name__})")
    out = {}
    for kind, template in wanted:
        name = schedule.schedule_filename(kind, template)
        raw = (d / name).read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        if manifest.get(name) != sha:
            raise SystemExit(f"SCHEDULE SHA MISMATCH: {name} -- refusing (m:267)")
        obj = json.loads(raw.decode("utf-8"))
        wk = "campaign" if kind == "campaign" else "gate"
        if (obj.get("unit") != keys.UNIT or obj.get("template") != template or obj.get("kind") != wk
                or (wk == "gate" and obj.get("gate") != kind) or obj.get("n") != len(obj.get("cells") or ())
                or schedule.cells_sha256(obj["cells"]) != obj.get("sha256_of_cells")):
            raise SystemExit(f"SCHEDULE FILE MALFORMED: {name} -- refusing")
        out[template] = {"name": name, "sha256": sha, "n": obj["n"], "cells": obj["cells"]}
    return out


def _schedules_sha(scheds: Mapping[str, Mapping]) -> str:
    body = "".join(f"{v['name']} {v['sha256']}\n" for v in sorted(scheds.values(), key=lambda v: v["name"]))
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


# --- identity_extra, identity, start ----------------------------------------------------------
_OPTIONAL_EXTRA = ("lock_file", "proposal_file", "prior_proposal_sha256s", "analyzer_sha256", "package_sha256",
                   "m_module_sha256")
_STUB_WEIGHTS = {"weights_revision": "0" * 40, "weights_sha256": "0" * 64}


def _repo_rel_ok(v: Any) -> bool:
    return (type(v) is str and bool(v) and not Path(v).is_absolute() and ".." not in Path(v).parts
            and "\\" not in v and Path(v).as_posix() == v and not _ROSTER_RX.search(v))


def _extra(identity_extra: Mapping[str, Any], *, stage: str, stub: bool) -> dict:
    """The values a stage cannot derive, validated.

    PIN (Code, declared at LOCK-m-F3 v0.1; m's _extra carried): identity_extra carries {lock_sha256,
    proposal_sha256, renders_sha16, reasoning_cap, weights_revision, weights_sha256} and, except at G-ID-F3,
    locked_path (G-TIME-F3 "uncached"); optional on the stub, REQUIRED on a non-stub run: lock_file,
    proposal_file, analyzer_sha256, package_sha256 (mf3's) and m_module_sha256 (each m file of guard.M_HASHED).
    The reasoning cap is 60 at G-TIME-F3 and, from G-ID-F3 on, the cap G-TIME-F3's trigger fixes (prior_gate)."""
    gid = stage == "id"
    want = ("lock_sha256", "proposal_sha256", "renders_sha16", "reasoning_cap", "weights_revision",
            "weights_sha256") + (() if gid else ("locked_path",))
    if not isinstance(identity_extra, Mapping) or not (set(want) <= set(identity_extra) <= set(want) | set(_OPTIONAL_EXTRA)):
        raise ValueError(f"identity_extra must carry exactly {want} (+ optional {_OPTIONAL_EXTRA})")
    out: dict[str, Any] = {k: identity_extra[k] for k in want}
    for k in ("lock_sha256", "proposal_sha256", "weights_sha256"):
        if type(out[k]) is not str or not _HEX64.match(out[k]):
            raise ValueError(f"{k} must be a sha256 hex digest ('pre-lock' refused: every Q-F3 stage follows its lock)")
    if type(out["weights_revision"]) is not str or not _HEX40.match(out["weights_revision"]):
        raise ValueError("weights_revision must be the snapshot's 40-hex revision")
    if not stub and (out["weights_revision"], out["weights_sha256"]) == tuple(_STUB_WEIGHTS.values()):
        raise ValueError("the stub's weights binding is refused on a non-stub run")
    if type(out["renders_sha16"]) is not str or not _HEX16.match(out["renders_sha16"]):
        raise ValueError("renders_sha16 must be 16 lower-case hex")
    cap = out["reasoning_cap"]
    if type(cap) is not int or cap not in sc_mod.REASONING_CAPS or (stage == "time" and cap != sc_mod.REASONING_CAPS[0]):
        raise ValueError(f"reasoning_cap must be one of {sc_mod.REASONING_CAPS} (60 at G-TIME-F3, m:174)")
    for k in ("lock_file", "proposal_file"):
        v = identity_extra.get(k)
        if v is None:
            if not stub:
                raise ValueError(f"identity_extra must name {k} on a non-stub run")
            v = PROPOSAL_REL if k == "proposal_file" else None
        elif not _repo_rel_ok(v):
            raise ValueError(f"{k} must be a repo-relative posix path (no '..', no roster word)")
        out[k] = v
    pp = identity_extra.get("prior_proposal_sha256s") or []
    if (type(pp) not in (list, tuple) or any(type(x) is not str or not _HEX64.match(x) for x in pp)
            or len(set(pp)) != len(pp) or out["proposal_sha256"] in pp):
        raise ValueError("prior_proposal_sha256s must be distinct sha256 digests, none this run's")
    out["prior_proposal_sha256s"] = sorted(pp)
    for k in ("analyzer_sha256", "package_sha256"):
        v = identity_extra.get(k)
        if v is None:
            if not stub:
                raise ValueError(f"identity_extra must carry {k} on a non-stub run (the licence checks it)")
        elif type(v) is not str or not _HEX64.match(v):
            raise ValueError(f"{k} must be a sha256 hex digest")
        out[k] = v
    mm = identity_extra.get("m_module_sha256")
    if mm is None:
        if not stub:
            raise ValueError("identity_extra must carry m_module_sha256 on a non-stub run (Q1 (C2) part (b))")
    elif not isinstance(mm, Mapping) or sorted(mm) != sorted(guard.M_HASHED) or any(
            type(v) is not str or not _HEX64.match(v) for v in mm.values()):
        raise ValueError(f"m_module_sha256 must map each of {guard.M_HASHED} to a sha256 digest")
    out["m_module_sha256"] = None if mm is None else dict(sorted(mm.items()))
    if not gid:
        lp = out["locked_path"]
        if lp not in ("cached", "uncached") or (stage == "time" and lp != "uncached"):
            raise ValueError(f"locked_path {lp!r} not allowed (G-TIME-F3 is uncached, m:293)")
    return out


def _renders_of_record(extra: Mapping[str, Any], name: str) -> tuple[list, list, str]:
    pool, renders = sc_mod.pool_and_renders()
    rsha = m_corr.renders_sha(renders)
    if extra["renders_sha16"] != rsha:
        raise SystemExit(f"RENDERS MISMATCH ({name}): the lock's renders sha16 is not the renders of record built here "
                         f"(m:176: Q-F3 does not recalibrate)")
    return pool, renders, rsha


def _startup(adapter) -> tuple[runner.F3Setup, str, str]:
    st = runner.f3_startup(adapter)
    ban_sha = hashlib.sha256(json.dumps(sorted(int(i) for i in st.ban_ids)).encode()).hexdigest()[:16]
    return st, st.audit_cfg["sha16_recomputed"], ban_sha


def _pending_on_disk(cpath: Path) -> bool:
    try:
        ck = json.loads(Path(cpath).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError):
        return False
    return isinstance(ck, dict) and rs.pending_end(ck) is not None


def _locked(name: str, extra: Mapping[str, Any], admitted: bool, cpath: Path | None = None) -> str:
    path = "cached" if admitted else "uncached"
    if extra["locked_path"] != path and cpath is not None and _pending_on_disk(cpath):
        print(f"PATH ({name}): the lock fixes {extra['locked_path']}; this backend's licence gives {path}; an end is "
              f"pending at {Path(cpath).name}, so this invocation only re-finishes it", flush=True)
        return extra["locked_path"]
    if extra["locked_path"] != path:
        raise SystemExit(f"PATH MISMATCH ({name}): the lock fixes the {extra['locked_path']} path; the G-ID-F3 licence on "
                         f"this backend at this cap gives {path} -- refusing (m:267, rule 2)")
    return path


def _identity(adapter, stage: str, template_set, path: str, n, scheds, audit_sha: str, ban_sha: str,
              extra: Mapping[str, Any], pool, renders_sha: str, hour_cap=None) -> dict:
    return rs.Identity(stage=stage, template_set=list(template_set), schedule_sha256=_schedules_sha(scheds),
                       path=path, hour_cap=hour_cap, n=dict(n), audit_v2_sha16=audit_sha, ban_sha=ban_sha,
                       backend_identifier=rs.backend_identifier(adapter.provenance()),
                       lock_sha256=extra["lock_sha256"], proposal_sha256=extra["proposal_sha256"],
                       reasoning_cap=extra["reasoning_cap"], weights_revision=extra["weights_revision"],
                       weights_sha256=extra["weights_sha256"], pool_sha16=rs.pool_sha16(pool),
                       renders_sha16=renders_sha)


def _begin(adapter, stage: str, name: str, cpath: Path, paths: Mapping, extra: Mapping[str, Any]) -> dict:
    _stub_guard(adapter, *[p for p in (paths["root"], cpath, paths.get("report"), paths.get("reads"),
                                       paths.get("gid")) if p is not None])
    _out_root_guard(adapter, paths["root"])
    rs.refuse_ended(cpath)
    prov = _start_provenance(adapter, name)
    _startup_checks(name, _proposal_path(extra))
    _laptop_preflight(adapter, name, extra)
    return prov


def _licensed(adapter, stage: str, name: str, extra: Mapping[str, Any], prior_ckpt) -> dict:
    stub = _is_stub(adapter)
    _licence(adapter, extra, name)
    return prior_gate(stage, prior_ckpt, proposal_sha256=extra["proposal_sha256"],
                      prior_proposal_sha256s=extra["prior_proposal_sha256s"], require_real=not stub,
                      reasoning_cap=extra["reasoning_cap"])


def _refuse_stopped(ckpt: Mapping, where: Path) -> None:
    if ckpt.get("stop"):
        raise SystemExit(f"STAGE ENDED at {where} (STOP): a resume never lifts a STOP (m:271)")


# --- one session -------------------------------------------------------------------------------
def _launch(adapter, setup: runner.F3Setup, stage: str, template: str, s: int, cell: Mapping, *,
            path_cached: bool, reasoning_cap: int) -> tuple[dict | None, list[str]]:
    """Scaffold, run, G-VER (before anything is written, m:284)."""
    pool, renders = sc_mod.pool_and_renders()
    sc = sc_mod.f3_config(stage, template, s, cell, "cached" if path_cached else "uncached",
                          reasoning_cap=reasoning_cap, pool=pool, renders=renders)
    rec = runner.run_session_f3(adapter, sc, setup.audit, setup.ban_ids, path_cached=path_cached,
                                term_rx=setup.term_rx)
    problems = verify.verify_and_mark(rec, pool=pool, renders=renders, schedule_cell=cell,
                                      scaffold_strings=setup.audit.scaffold_strings)
    return rec, problems


def _verify_hit(template: str, s: int, problems: Sequence[str], rec: dict | None) -> dict:
    bar = verify.MISMATCH if problems[0].startswith(verify.MISMATCH) else verify.BREAK
    return {"bar": bar, "template": template, "s": s, "phase": None, "ci": None,
            "contrast": keys.is_contrast(template), "problems": list(problems), "record": rec, "round": None,
            "j": rec.get("j") if isinstance(rec, Mapping) else None,
            "path": rec.get("path") if isinstance(rec, Mapping) else None}


def _hair_hit(rec: Mapping) -> dict | None:
    h = rec.get("hair_triggers") or []
    if not h:
        return None
    # PIN (Code, declared at LOCK-m-F3 v0.1; m's _hair_hit carried): the fired generation is the session's
    # last recorded one -- a task round, or a reasoning line (phase "reasoning", its ci); its identifiers
    # go to the stop block only, for the confined adjudication read.
    if h[0]["phase"] == "reasoning":
        x = (rec.get("reasoning") or [{}])[-1]
        rnd = {"phase": "reasoning", "n": x.get("n"), "index": x.get("ci")}
    else:
        last = (rec.get("rounds") or [{}])[-1]
        rnd = {"phase": h[0]["phase"], "n": last.get("n"), "index": last.get("ri", last.get("ci"))}
    return {"bar": h[0]["name"], "template": rec["template"], "s": rec["s"], "phase": h[0]["phase"],
            "ci": h[0].get("ci"), "contrast": bool(rec["contrast"]), "problems": [], "record": None,
            "round": rnd, "j": rec.get("j"), "path": rec.get("path")}


def _withheld_phase(hit: Mapping) -> bool:
    """A contrast session's free-phase event: a free round, or a reasoning line after its first pick."""
    return bool(hit["contrast"]) and (hit["phase"] == "free" or (hit["phase"] == "reasoning" and (hit.get("ci") or 0) >= 1))


def announce_stop(stage: str, hit: Mapping) -> tuple[list[str], dict]:
    """(stdout lines, blinded stop block) for a hair trigger (m:271, m:318): a contrast session's free-phase
    trigger (a reasoning line after the first pick included) by phase alone; every other by the bar's
    blinded message."""
    name = stage_name(stage)
    t, s, ph = hit["template"], hit["s"], hit["phase"]
    if _withheld_phase(hit):
        return ([f"STOP {name}: a hair trigger fired in the free phase of a contrast session ({t} s={s}); its class "
                 f"is withheld (m:318 exception (1)); the stage stops for the seat's adjudication"],
                {"bar": WITHHELD_CLASS, "template": t, "s": s, "phase": "free"})
    b = bars.bar(hit["bar"])
    ctx: dict = {"template": t} if b.domain == "every" else {}
    if ph is not None:
        ctx["phase"] = ph
    res = b.evaluate(1, 1, **ctx)
    return ([res.message, f"STOP {name}: hair trigger {hit['bar']} ({t} s={s}); the stage stops (m:271)"],
            {"bar": hit["bar"], "template": t, "s": s, "phase": ph})


def _stop_record(hit: Mapping, blinded: Mapping) -> dict:
    return {"kind": "hair_trigger", "bar": hit["bar"], "template": hit["template"], "s": hit["s"], "j": hit.get("j"),
            "path": hit.get("path"), "phase": hit["phase"], "ci": hit.get("ci"),
            "round": copy.deepcopy(hit.get("round")), "problems": list(hit["problems"]),
            "record": copy.deepcopy(hit["record"]), "blinded": dict(blinded)}


def _hit_from_stop(stop: Mapping | None) -> dict | None:
    if stop is None:
        return None
    return {"bar": stop["bar"], "template": stop["template"], "s": stop["s"], "phase": stop["phase"],
            "ci": stop.get("ci"), "contrast": keys.is_contrast(stop["template"]), "problems": list(stop["problems"]),
            "record": copy.deepcopy(stop["record"]), "round": copy.deepcopy(stop["round"]), "j": stop.get("j"),
            "path": stop.get("path")}


def _pend(ckpt: dict, cpath: Path, pending: Mapping, name: str) -> tuple[dict, bool]:
    have = rs.pending_end(ckpt)
    first = have is None
    if first:
        rs.set_end_pending(ckpt, pending)
    elif not rs.same_json(have, pending):
        raise SystemExit(f"END PENDING MISMATCH ({name}) at {cpath}: the end on disk is not the one re-derived -- refusing")
    final = rs.apply_end(copy.deepcopy(ckpt))
    rs.assert_writable(cpath, final)
    return final, first


def _write_pending(cpath: Path, ckpt: dict, final: dict) -> None:
    rs.write_checkpoint(cpath, ckpt)
    final["state"] = copy.deepcopy(ckpt["state"])


def _refinish_line(name: str, status: str, cpath: Path) -> str:
    return (f"RE-FINISH {name}: {cpath.name} carries an end pending ({status}); nothing launches -- the outputs are "
            f"re-derived from the checkpoint and the end persisted (m:267, m:271)")


def _remove_stale(apath: Path) -> None:
    if apath.is_file() or apath.is_symlink():
        apath.unlink()


# --- pick-free outputs ----------------------------------------------------------------------------
def _assert_pick_free(obj: Any, what: str) -> None:
    if _ROSTER_RX.search(json.dumps(obj, sort_keys=True, ensure_ascii=False)):
        raise ValueError(f"{what}: a roster label reached a pick-free artifact; refused")


def _sham_seconds(records: Sequence[Mapping]) -> dict:
    sh = [r for r in records if not r["contrast"]]
    return {"sham_sessions": len(sh), "sham_seconds": round(sum(float(r["seconds"]) for r in sh), 3),
            "contrast_seconds": "withheld to the unit's VERDICTS entry (m:318)"}


def _reads(records: Sequence[Mapping]) -> list[dict]:
    return [readrule.strip_contrast(r) if r["contrast"] else readrule.redact_sham(r) for r in records]


def _write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rs.atomic_write_json(path, obj, indent=1)


def _ident_summary(ident: Mapping) -> dict:
    return {k: copy.deepcopy(ident[k]) for k in ("lock_sha256", "proposal_sha256", "schedule_sha256", "path",
                                                 "audit_v2_sha16", "ban_sha", "backend_identifier", "package_sha256",
                                                 "m_module_sha256", "pool_sha16", "renders_sha16", "reasoning_cap",
                                                 "weights_revision", "weights_sha256")}


def _sha16_text(text: str | None) -> str | None:
    return None if text is None else hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def _stage_line(name: str, status: str, path: str) -> str:
    return f"STAGE {name} {status} path={path}"


def _write_unless_identical(path: Path, obj: Any) -> None:
    if path.is_file() and path.read_text(encoding="utf-8") == rs.json_text(obj, indent=1):
        return
    _write_json(path, obj)


# --- the confined adjudication excerpt (m:271; m:318 exception (1)) -------------------------------
def _session_ids(rec: Mapping) -> dict:
    return {"unit": rec.get("unit"), "stage": rec.get("stage"), "template": rec.get("template"), "s": rec.get("s"),
            "j": rec.get("j"), "path": rec.get("path"), "contrast": bool(rec.get("contrast"))}


def _round_excerpt(rec: Mapping, rd: Mapping) -> tuple[dict, list[dict]]:
    ph = rd.get("phase")
    idx = rd.get("ri") if ph == "forced" else rd.get("ci")
    tr = rec.get("transcript") or ""
    header = next((tr[p["start"]:p["end"]] for p in rec.get("pieces") or []
                   if p.get("kind") == "round" and p.get("phase") == ph and p.get("idx") == idx), None)
    ex = {**_session_ids(rec), "kind": "round", "phase": ph, "index": idx, "n": rd.get("n"), "header": header,
          "generation": rd.get("text"), "audit": copy.deepcopy(rd.get("audit"))}
    picks = [{**_session_ids(rec), "ci": idx, "n": rd.get("n"), "pick": rd.get("label")}] if ph == "free" else []
    return ex, picks


def _line_excerpt(rec: Mapping, x: Mapping) -> tuple[dict, list[dict]]:
    # PIN (Code, declared at LOCK-m-F3 v0.1): a reasoning line's excerpt is its block, its text and its
    # audit; a line after the first pick follows a chosen round whose pick the read reveals, so the line's
    # excerpt lists the previous choice's pick as revealed (m:271: "the pick it reveals is recorded as seen").
    ci = x.get("ci")
    ex = {**_session_ids(rec), "kind": "reasoning_line", "phase": "reasoning", "index": ci, "n": x.get("n"),
          "header": banner.reasoning_block(x["n"]) if type(x.get("n")) is int else None, "generation": x.get("text"),
          "audit": copy.deepcopy(x.get("audit"))}
    ch = rec.get("choices") or []
    picks = ([{**_session_ids(rec), "ci": ci - 1, "n": ch[ci - 1].get("n"), "pick": ch[ci - 1].get("pick")}]
             if type(ci) is int and ci >= 1 and len(ch) >= ci else [])
    return ex, picks


def _hit_event(records: Sequence[Mapping], hit: Mapping) -> dict:
    if hit.get("round") is None:
        rec = hit.get("record") if isinstance(hit.get("record"), Mapping) else {}
        return {"event": "STOP", "kind": "harness", "bar": hit["bar"],
                "session": {**_session_ids(rec), "template": hit["template"], "s": hit["s"],
                            "contrast": bool(hit["contrast"])},
                "problems": list(hit["problems"]), "rounds": [], "picks_revealed": []}
    want = (hit["template"], hit["s"], hit.get("path"))
    rec = next((r for r in reversed(records) if (r["template"], r["s"], r.get("path")) == want), None)
    rounds, picks = [], []
    if rec is not None:
        if hit["phase"] == "reasoning" and rec.get("reasoning"):
            ex, picks = _line_excerpt(rec, rec["reasoning"][-1])
            rounds = [ex]
        elif rec.get("rounds"):
            ex, picks = _round_excerpt(rec, rec["rounds"][-1])
            rounds = [ex]
    return {"event": "STOP", "kind": "hair_trigger", "bar": hit["bar"],
            "session": _session_ids(rec) if rec is not None else {"template": hit["template"], "s": hit["s"]},
            "rounds": rounds, "picks_revealed": picks}


def _bars_event(records: Sequence[Mapping], status: str, fired: Sequence[bars.BarResult]) -> dict:
    rounds, picks = [], []
    names = {r.name.split("@")[0] for r in fired}
    for r in records:
        if not keys.is_sham(r["template"]):
            continue
        if "round_degeneracy" in names:
            for rd in r["rounds"]:
                if (rd.get("audit") or {}).get("claim") in bars.DEGEN_CLAIMS:
                    ex, pk = _round_excerpt(r, rd)
                    rounds.append(ex)
                    picks += pk
        if "reasoning_line_defect" in names:
            for x in r.get("reasoning") or []:
                if x["audit"]["classes"]:
                    ex, pk = _line_excerpt(r, x)
                    rounds.append(ex)
                    picks += pk
    return {"event": status, "kind": "bars", "bars": [b.name for b in fired], "counts": [b.as_dict() for b in fired],
            "rounds": rounds, "picks_revealed": picks}


def _adjudication_doc(stage: str, name: str, cpath: Path, root: Path, events: Sequence[Mapping]) -> dict:
    return {"schema": ADJ_SCHEMA, "unit": keys.UNIT, "stage": stage, "stage_name": name,
            "form": "confined adjudication read (m:271; m:318 exception (1)): pick-bearing, under ckpt/ (-diff); never "
                    "printed", "checkpoint": _rel(cpath, root), "events": [dict(e) for e in events]}


# --- gate stages ----------------------------------------------------------------------------------
def run_gate_stage(adapter, *, gate: str, templates_counts: Sequence[tuple[str, int]], ckpt_path=None,
                   resume: bool = False, identity_extra: Mapping[str, Any], out_root=DEFAULT_OUT,
                   prior_ckpt=None) -> dict:
    """G-TIME-F3 (m:293) or G-F3 (m:297). ``prior_ckpt`` (G-TIME-F3's checkpoint) is G-F3's."""
    if gate not in GATES:
        raise ValueError(f"run_gate_stage runs {GATES}; G-ID-F3 is run_gid_pair_f3, the campaign run_campaign")
    name = stage_name(gate)
    paths = out_paths(gate, out_root)
    cpath = checkpoint_path(ckpt_path, paths)
    paths = for_checkpoint(paths, cpath)
    extra = _extra(identity_extra, stage=gate, stub=_is_stub(adapter))
    prov = _begin(adapter, gate, name, cpath, paths, extra)
    prior = _licensed(adapter, gate, name, extra, prior_ckpt)
    pool, _r, rsha = _renders_of_record(extra, name)
    scheds = load_committed([(gate, t) for t in keys.TEMPLATES], paths["schedules"])
    tc = [(t, m) for t, m in templates_counts]
    if tc != [(t, scheds[t]["n"]) for t in keys.TEMPLATES]:
        raise ValueError(f"{name}: templates_counts {tc} != the committed schedule's")
    order = schedule.gate_launch_order(tc)
    bars.assert_firing_complete()
    setup, audit_sha, ban_sha = _startup(adapter)
    cap = extra["reasoning_cap"]
    path_cached = guard.cached_path_admitted(gate, backend_identifier=rs.backend_identifier(adapter.provenance()),
                                             reasoning_cap=cap)
    if path_cached and gate == "time":
        raise AssertionError("G-TIME-F3 is uncached by spec (m:293)")
    path = _locked(name, extra, path_cached, cpath)
    refinish_only = path != ("cached" if path_cached else "uncached")
    ident = _identity(adapter, gate, keys.TEMPLATES, path, dict(tc), scheds, audit_sha, ban_sha, extra, pool, rsha)
    ckpt = rs.load_or_init(cpath, ident, resume)
    if refinish_only and rs.pending_end(ckpt) is None:
        raise SystemExit(f"PATH MISMATCH ({name}): the end pending at {cpath} is gone -- refusing to launch (m:267)")
    _refuse_stopped(ckpt, cpath)
    _record_prior(ckpt, prior, cpath)
    _record_licence(ckpt, extra, cpath)
    _append_provenance(ckpt, prov)
    cpath.parent.mkdir(parents=True, exist_ok=True)
    rs.write_checkpoint(cpath, ckpt)
    pending = rs.pending_end(ckpt)
    if pending is not None:
        print(_refinish_line(name, pending["status"], cpath), flush=True)
        return _finish_gate(gate, name, ckpt, cpath, paths, _hit_from_stop(pending["stop"]))
    done = rs.done_ids(ckpt)
    hit = None
    for t, j in order:
        if (t, j) in done:
            continue
        rs.note_launch(ckpt)
        rec, problems = _launch(adapter, setup, gate, t, j, scheds[t]["cells"][j], path_cached=path_cached,
                                reasoning_cap=cap)
        if problems:
            hit = _verify_hit(t, j, problems, rec)
            break
        rs.record_session(ckpt, rec)
        hit = _hair_hit(rec)
        if hit is None:
            rs.write_checkpoint(cpath, ckpt)
        print(readrule.session_line(rec), flush=True)
        if hit is not None:
            break
    return _finish_gate(gate, name, ckpt, cpath, paths, hit)


def cap_trigger(records: Sequence[Mapping]) -> dict:
    """m:174's cap trigger over G-TIME-F3's reasoning lines -- all six sessions (the seat's Q5)."""
    # PIN (Code, declared at LOCK-m-F3 v0.1; m:174, m:293, the seat's Q5): the count is the lines whose
    # generation stopped on the cap (cap_no_newline), over every reasoning line every G-TIME-F3 session
    # generated, contrast sessions included; ">= 3" gives the pre-declared 120, else 60 stays. Reported as
    # counts only. The cap so fixed (m:294) is applied from G-ID-F3 on, which prior_gate checks against this
    # function on G-TIME-F3's checkpoint (m:295), and LOCK-m-F3 v0.2 records it (m:296).
    ls = [x for r in records for x in r.get("reasoning") or []]
    k = sum(bool(x["cap_hit"]) for x in ls)
    return {"cap_reached": k, "lines": len(ls), "threshold": CAP_TRIGGER, "max_lines": 36,
            "fixed_cap": CAP_AFTER_TRIGGER if k >= CAP_TRIGGER else sc_mod.REASONING_CAPS[0],
            "rule": "m:174: >= 3 of the reasoning lines G-TIME-F3 generates (<= 36) reach the cap without a newline "
                    "-> 120; counted over all six sessions (m:293; the seat's Q5)"}


def _contrast_first_reads(records: Sequence[Mapping]) -> dict:
    return {c: _read_flags([r for r in records if r["template"] == c], first_only=True) for c in keys.CONTRAST}


def _gate_end(gate: str, records: Sequence[Mapping], hit: Mapping | None) -> dict:
    """A gate stage's end from its sessions (and the hit): a pure function, re-derived at a re-finish."""
    if hit is not None:
        lines_, blinded = announce_stop(gate, hit)
        return {"status": "STOP", "fired": [hit["bar"]], "results": [], "lines": lines_,
                "stop": _stop_record(hit, blinded), "events": [_hit_event(records, hit)], "no_test": []}
    end_bars = [b for b in bars.QF3_BARS if b.stage == gate and b.kind == "binomial_stage_end"]
    results = [bars.evaluate(records, b) for b in end_bars]
    fired = [r for r in results if r.fired]
    nt = [r.name for r in results if bars.no_test(r)]
    status = "STOP" if fired else "PASS"
    lines_ = [r.message for r in results] + [f"NO TEST {n}: realised n = 0 -- reported, not fired (B30, by analogy with m:271)"
                                             for n in nt]
    return {"status": status, "fired": [r.name for r in fired], "results": results, "lines": lines_, "stop": None,
            "events": [_bars_event(records, status, fired)] if fired else [], "no_test": nt}


def _assert_time_form(report: Mapping, reads: Mapping) -> None:
    """Ruling (h) and Q5 at G-TIME-F3's finish: each contrast block and read in its declared form."""
    sr = report.get("stage_report")
    if sr is not None:
        for c in keys.CONTRAST:
            blk = sr["templates"].get(c)
            if blk is None:
                continue
            per = blk.get("per_session")
            if (tuple(blk) != readrule.TIME_CONTRAST_KEYS or not isinstance(per, list)
                    or any(tuple(p) != readrule.TIME_SESSION_KEYS
                           or not all(type(x) is bool for x in p["reasoning_cap_reached"]) for p in per)):
                raise ValueError(f"{c}: the G-TIME-F3 contrast block is not its declared form; refused before any write")
    for r in reads.get("sessions") or []:
        if not r.get("contrast"):
            continue
        ks: set = set()
        stack: list[Any] = [r]
        while stack:
            x = stack.pop()
            if isinstance(x, Mapping):
                ks |= set(x)
                stack.extend(x.values())
            elif isinstance(x, list):
                stack.extend(x)
        if ks & (readrule.m_rr.TIME_WITHHELD | {"reasoning"}) or any(
                not set(rd) <= set(readrule.m_rr.TIME_ROUND_KEEP) for rd in r["rounds"]):
            raise ValueError("a G-TIME-F3 contrast read carries a class or line field; refused before any write")


def _finish_gate(gate: str, name: str, ckpt: dict, cpath: Path, paths: Mapping, hit: Mapping | None) -> dict:
    end = _gate_end(gate, ckpt["sessions"], hit)
    final, first = _pend(ckpt, cpath, {"status": end["status"], "fired": end["fired"], "stop": end["stop"]}, name)
    records, ident = final["sessions"], final["identity"]
    stop_block = copy.deepcopy(final["stop"]["blinded"]) if final.get("stop") else None
    status, results, events = end["status"], end["results"], end["events"]
    apath = adjudication_path(cpath)
    files = {"checkpoint": _rel(cpath, paths["root"]), "reads": _rel(paths["reads"], paths["root"])}
    if events:
        files["adjudication"] = _rel(apath, paths["root"])
    report = {"schema": REPORT_SCHEMA, "form": "pick-free stage report (m:271, m:318)", "unit": keys.UNIT,
              "stage": gate, "stage_name": name, "status": status, "planned": dict(ident["n"]),
              "recorded": {t: sum(r["template"] == t for r in records) for t in keys.TEMPLATES},
              "bars": [r.as_dict() for r in results], "no_test": list(end["no_test"]), "stop": stop_block,
              "timing": _sham_seconds(records),
              "stage_report": readrule.stage_report(records) if records else None,
              "identity": _ident_summary(ident), "provenance": rs.report_provenance(final), "files": files}
    if gate == "time":
        report["cap_trigger"] = cap_trigger(records)
    if gate == "qual":
        report["contrast_first_read_flags"] = _contrast_first_reads(records)
    _assert_pick_free(report, name)
    reads = {"schema": READS_SCHEMA, "unit": keys.UNIT, "stage": gate, "stage_name": name,
             "form": "pre-VERDICTS reads (m:271): contrast = banner + forced rounds; sham = menus removed, chosen tag "
                     "and labels [config]", "sessions": _reads(records)}
    if gate == "time":
        _assert_time_form(report, reads)
    adj = _adjudication_doc(gate, name, cpath, paths["root"], events) if events else None
    if first:
        _write_pending(cpath, ckpt, final)
    _write_json(paths["report"], report)
    _write_json(paths["reads"], reads)
    if adj is not None:
        _write_json(apath, adj)
    else:
        _remove_stale(apath)
    rs.persist_end(cpath, final)
    for ln in end["lines"]:
        print(ln, flush=True)
    if gate == "time":
        ct = report["cap_trigger"]
        print(f"CAP TRIGGER {name}: {ct['cap_reached']} of {ct['lines']} reasoning lines reached the cap (threshold "
              f"{CAP_TRIGGER}); the fixed cap would be {ct['fixed_cap']} (recorded at LOCK-m-F3 v0.2, m:294)", flush=True)
    print(_stage_line(name, status, ident["path"]), flush=True)
    for k, p in [("CHECKPOINT", cpath), ("REPORT", paths["report"]), ("READS", paths["reads"])] + (
            [("ADJUDICATION", apath)] if events else []):
        print(f"{k} {p}", flush=True)
    return {"status": status, "stage_name": name, "checkpoint": cpath, "report": paths["report"],
            "reads": paths["reads"], "bars": results, "adjudication": apath if events else None,
            "cap_trigger": report.get("cap_trigger")}


# --- G-ID-F3 ---------------------------------------------------------------------------------------
def gid_decide(pairs: Sequence[Mapping[str, Any]]) -> dict:
    """G-ID-F3's criterion over the pairs run so far (A2s's in j order, then A3s's): per template the
    first complete identical pair decides it; a divergence anywhere is FAIL; a template past j = 15 without
    one is NOT-DETERMINED; both decided -> PASS (2/2)."""
    # PIN (Code, declared at LOCK-m-F3 v0.1; m:295 "A2s and A3s once each; criterion 2/2 as above"; the seat's
    # Q8: "as G-ID-F0m's"; N2: m:281's "indices advance until two complete sessions exist"): one complete
    # pair per template, indices advancing per template past an incomplete pair (a complete pair = both halves
    # complete: 4 forced rounds and 6 x (line, read, chosen round)); a divergence -- complete or not -- fails
    # G-ID-F3 (m's PIN: "a path that changes a session's length or exclusion has diverged").
    decided: list[bool] = []
    for t in keys.GID_TEMPLATES:
        tp = [p for p in pairs if p["template"] == t]
        got = False
        for p in tp:
            if not p["identical"]:
                decided.append(False)
                return {"verdict": "FAIL", "n_pairs": len(decided), "pairs_identical": decided, "at": [t, p["j"]]}
            if p["complete"]:
                decided.append(True)
                got = True
                break
        if not got:
            verdict = "NOT-DETERMINED" if len(tp) >= schedule.GATE_MAX else "OPEN"
            return {"verdict": verdict, "n_pairs": len(decided), "pairs_identical": decided,
                    "at": [t, tp[-1]["j"]] if tp else [t, None], "open_template": t}
    return {"verdict": "PASS", "n_pairs": 2, "pairs_identical": decided, "at": None}


def _gen_meta(rec: Mapping) -> list[tuple]:
    """(kind, n_tok, cap_hit, stop_reason) of every generation a record holds: its rounds, then its lines."""
    return ([("round", int(r["n_tok"]), bool(r["cap_hit"]), str(r["stop_reason"])) for r in rec.get("rounds") or []]
            + [("line", int(x["n_tok"]), bool(x["cap_hit"]), str(x["stop_reason"])) for x in rec.get("reasoning") or []])


def _gid_pair(t: str, j: int, u: Mapping, c: Mapping) -> dict:
    # PIN (Code, declared at LOCK-m-F3 v0.1; m:281 / m:295's criterion; the build review's finding 9): the pair's
    # verdict is m:281's -- byte-identical transcripts. Beside it, descriptive only, each pair reports whether
    # every generation's token count, cap flag and stop reason agree as well ("meta_identical"): the adapter
    # strips a generation's text, so two paths can write one transcript with different cap-reach (the
    # cap_no_newline class; the cap trigger). Binding it would change the criterion, which is the seat's (F-7).
    return {"template": t, "j": j, "complete": bool(u["complete"] and c["complete"]),
            "identical": u["transcript"] == c["transcript"], "complete_uncached": bool(u["complete"]),
            "complete_cached": bool(c["complete"]), "meta_identical": _gen_meta(u) == _gen_meta(c)}


def gid_pairs(records: Sequence[Mapping], upto: tuple[str, int] | None = None) -> tuple[list[dict], dict]:
    """(pairs, decision) re-derived from the sessions on disk exactly as the loop builds them; ``upto`` =
    the hit's (template, j), where the loop recorded no pair."""
    have = {(r["template"], r["s"], r["path"]): r for r in records}
    pairs: list[dict] = []
    for t in keys.GID_TEMPLATES:
        for j in range(schedule.GATE_MAX):
            if upto is not None and (t, j) == tuple(upto):
                return pairs, gid_decide(pairs)
            u, c = have.get((t, j, "uncached")), have.get((t, j, "cached"))
            if u is None or c is None:
                return pairs, gid_decide(pairs)
            pairs.append(_gid_pair(t, j, u, c))
            d = gid_decide(pairs)
            if d["verdict"] != "OPEN":
                return pairs, d
            if d.get("open_template") != t:
                break
    return pairs, gid_decide(pairs)


def run_gid_pair_f3(adapter, *, ckpt_path=None, resume: bool = False, identity_extra: Mapping[str, Any],
                    prior_ckpt, out_root=DEFAULT_OUT) -> dict:
    """G-ID-F3 (m:295): A2s then A3s, at each index uncached then cached under the same keys, at the fixed
    reasoning cap; writes the artifact guard.cached_path_admitted reads. ``prior_ckpt``: G-TIME-F3's (PASS)."""
    name = stage_name("id")
    paths = out_paths("id", out_root)
    cpath = checkpoint_path(ckpt_path, paths)
    paths = for_checkpoint(paths, cpath)
    gid_path = guard.gid_artifact_path()
    extra = _extra(identity_extra, stage="id", stub=_is_stub(adapter))
    prov = _begin(adapter, "id", name, cpath, {**paths, "gid": gid_path}, extra)
    # PIN (Code, declared at LOCK-m-F3 v0.1; m's PIN carried; B7): a G-ID-F3 artifact is never overwritten
    # (a re-run after a cap change starts with the old one set aside by git mv); the one exception is the
    # re-finish of this stage's own pending end, which accepts it only byte-identical.
    if gid_path.exists() and not rs.pending_at(cpath):
        raise SystemExit(f"G-ID ARTIFACT EXISTS at {gid_path}; it is never overwritten")
    prior = _licensed(adapter, "id", name, extra, prior_ckpt)
    pool, _r, rsha = _renders_of_record(extra, name)
    scheds = load_committed([("id", t) for t in keys.GID_TEMPLATES], paths["schedules"])
    bars.assert_firing_complete()
    setup, audit_sha, ban_sha = _startup(adapter)
    cap = extra["reasoning_cap"]
    ident = _identity(adapter, "id", keys.GID_TEMPLATES, "cached+uncached",
                      {t: scheds[t]["n"] for t in keys.GID_TEMPLATES}, scheds, audit_sha, ban_sha, extra, pool, rsha)
    ckpt = rs.load_or_init(cpath, ident, resume)
    _refuse_stopped(ckpt, cpath)
    _record_prior(ckpt, prior, cpath)
    _record_licence(ckpt, extra, cpath)
    _append_provenance(ckpt, prov)
    cpath.parent.mkdir(parents=True, exist_ok=True)
    rs.write_checkpoint(cpath, ckpt)
    pending = rs.pending_end(ckpt)
    if pending is not None:
        print(_refinish_line(name, pending["status"], cpath), flush=True)
        return _finish_gid(name, ckpt, cpath, paths, _hit_from_stop(pending["stop"]), gid_path)
    have = {(r["template"], r["s"], r["path"]): r for r in ckpt["sessions"]}
    pairs: list[dict] = []
    hit = None
    for t in keys.GID_TEMPLATES:
        cells = scheds[t]["cells"]
        for j in range(len(cells)):
            halves: dict[str, dict] = {}
            for path_cached in guard.gid_paths():
                path = "cached" if path_cached else "uncached"
                rec = have.get((t, j, path))
                if rec is None:
                    rs.note_launch(ckpt)
                    rec, problems = _launch(adapter, setup, "id", t, j, cells[j], path_cached=path_cached,
                                            reasoning_cap=cap)
                    if problems:
                        hit = _verify_hit(t, j, problems, rec)
                        break
                    rs.record_session(ckpt, rec)
                    hit = _hair_hit(rec)
                    if hit is None:
                        rs.write_checkpoint(cpath, ckpt)
                    print(readrule.session_line(rec), flush=True)
                    if hit is not None:
                        break
                halves[path] = rec
            if hit is not None:
                break
            pairs.append(_gid_pair(t, j, halves["uncached"], halves["cached"]))
            d = gid_decide(pairs)
            if d["verdict"] != "OPEN" or d.get("open_template") != t:
                break
        if hit is not None or gid_decide(pairs)["verdict"] != "OPEN":
            break
    return _finish_gid(name, ckpt, cpath, paths, hit, gid_path, loop_pairs=pairs)


def _gid_end(records: Sequence[Mapping], hit: Mapping | None, decision: Mapping) -> dict:
    if hit is not None:
        lines_, blinded = announce_stop("id", hit)
        return {"status": "STOP", "fired": [hit["bar"]], "results": [], "lines": lines_,
                "stop": _stop_record(hit, blinded), "events": [_hit_event(records, hit)]}
    status = decision["verdict"]
    if status not in ("PASS", "FAIL", "NOT-DETERMINED"):
        raise AssertionError(f"G-ID-F3 ended with an open decision ({status})")
    res = bars.bar("gid_divergence@G-ID-F3").evaluate(int(status == "FAIL"), max(len(decision["pairs_identical"]), 1))
    return {"status": status, "fired": [res.name] if res.fired else [], "results": [res], "lines": [res.message],
            "stop": None, "events": []}


def _finish_gid(name: str, ckpt: dict, cpath: Path, paths: Mapping, hit: Mapping | None, gid_path: Path,
                loop_pairs: list[dict] | None = None) -> dict:
    pairs, decision = gid_pairs(ckpt["sessions"], None if hit is None else (hit["template"], hit["s"]))
    if loop_pairs is not None and loop_pairs != pairs:
        raise AssertionError("G-ID-F3: the pairs re-derived from the sessions differ from the loop's")
    end = _gid_end(ckpt["sessions"], hit, decision)
    final, first = _pend(ckpt, cpath, {"status": end["status"], "fired": end["fired"], "stop": end["stop"]}, name)
    records, ident = final["sessions"], final["identity"]
    status, results, events = end["status"], end["results"], end["events"]
    stop_block = copy.deepcopy(final["stop"]["blinded"]) if final.get("stop") else None
    timing = {p: round(sum(float(r["seconds"]) for r in records if r["path"] == p), 3) for p in ("uncached", "cached")}
    by_path = {p: [r for r in records if r["path"] == p] for p in ("uncached", "cached")}
    apath = adjudication_path(cpath)
    files = {"checkpoint": _rel(cpath, paths["root"]), "reads": _rel(paths["reads"], paths["root"])}
    if events:
        files["adjudication"] = _rel(apath, paths["root"])
    report = {"schema": REPORT_SCHEMA, "form": "pick-free stage report (m:271, m:295)", "unit": keys.UNIT,
              "stage": "id", "stage_name": name, "status": status, "criterion": guard.GID_CRITERION, "pairs": pairs,
              "bars": [r.as_dict() for r in results], "stop": stop_block,
              "timing": {"uncached_seconds": timing["uncached"], "cached_seconds": timing["cached"]},
              "stage_report": {p: (readrule.stage_report(v) if v else None) for p, v in by_path.items()},
              "identity": _ident_summary(ident), "provenance": rs.report_provenance(final), "files": files}
    _assert_pick_free(report, name)
    # PIN (Code, declared at LOCK-m-F3 v0.1; m's PIN carried): G-ID-F3's sessions are sham-only and read in full
    # at G-ID (m:271; §4 exception (4)), so its reads file carries the full records.
    reads = {"schema": READS_SCHEMA, "unit": keys.UNIT, "stage": "id", "stage_name": name,
             "form": "full records: G-ID-F3's sham-only sessions (m:271; §4 exception (4))",
             "sessions": copy.deepcopy(readrule.release_full(records))}
    art = None
    if status in ("PASS", "FAIL", "NOT-DETERMINED"):
        art = {"schema": GID_SCHEMA, "unit": keys.UNIT, "criterion": guard.GID_CRITERION, "verdict": status,
               "n_pairs": int(decision["n_pairs"]), "pairs_identical": list(decision["pairs_identical"]),
               "stage_name": name, "path_order": ["uncached", "cached"], "templates": list(keys.GID_TEMPLATES),
               "key_template": {t: keys.arm_key("id", t, "{s}") for t in keys.GID_TEMPLATES}, "indices": pairs,
               "timing": report["timing"], "identity": _ident_summary(ident), "provenance": rs.report_provenance(final)}
        _assert_pick_free(art, name)
    if gid_path.exists():
        if art is None or gid_path.read_text(encoding="utf-8") != rs.json_text(art, indent=1):
            raise SystemExit(f"G-ID ARTIFACT DIFFERS at {gid_path}: it is not the artifact this finish re-derives -- "
                             f"never overwritten; no output written")
    adj = _adjudication_doc("id", name, cpath, paths["root"], events) if events else None
    if first:
        _write_pending(cpath, ckpt, final)
    _write_json(paths["report"], report)
    _write_json(paths["reads"], reads)
    if adj is not None:
        _write_json(apath, adj)
    else:
        _remove_stale(apath)
    if art is not None:
        _write_unless_identical(gid_path, art)
    rs.persist_end(cpath, final)
    for ln in end["lines"]:
        print(ln, flush=True)
    print(_stage_line(name, status, ident["path"]), flush=True)
    for k, p in [("CHECKPOINT", cpath), ("REPORT", paths["report"]), ("READS", paths["reads"])] + (
            [("ADJUDICATION", apath)] if events else []) + ([("G-ID ARTIFACT", gid_path)] if gid_path.exists() else []):
        print(f"{k} {p}", flush=True)
    return {"status": status, "stage_name": name, "checkpoint": cpath, "report": paths["report"],
            "reads": paths["reads"], "artifact": gid_path if gid_path.exists() else None, "pairs": pairs,
            "decision": dict(decision), "adjudication": apath if events else None}


# --- the campaign ------------------------------------------------------------------------------------
def _per_arm(v: Mapping[str, int], what: str) -> dict[str, int]:
    if not isinstance(v, Mapping) or sorted(v) != sorted(keys.TEMPLATES) or any(
            type(x) is not int or x < 1 for x in v.values()):
        raise ValueError(f"{what} must map each of Q-F3's six arms to a positive int, got {v!r}")
    return {a: int(v[a]) for a in keys.TEMPLATES}


def _read_flags(records: Sequence[Mapping], *, first_only: bool) -> dict:
    reads: list[Mapping] = []
    for r in records:
        ch = r.get("choices") or []
        if first_only:
            if r.get("domain") and ch:
                reads.append(ch[0])
        else:
            reads.extend(ch)
    return {"scope": "first reads of domain sessions" if first_only else "all reads", "reads": len(reads),
            "low_label_mass": sum(bool(c.get("low_label_mass")) for c in reads),
            "top1_not_label": sum(bool(c.get("top1_not_label")) for c in reads)}


def campaign_look(records: Sequence[Mapping], look: Any) -> dict:
    """One §6 look (m:330, m:316): round_degeneracy and reasoning-line defects over the three sham arms,
    the pooled own-pair lexical bar over A2s + A3s, and per contrast arm the Fisher guard against its
    matched sham and the absolute guard (both binding); pooled pre-pick exclusion counts and read flags
    per arm; reported beside: each contrast arm's forced-round degeneracy and every arm outside the lexical
    bar's domain's lexical count (contrast arms over forced rounds only)."""
    # PIN (Code, declared at LOCK-m-F3 v0.1; the build design's B23): the lexical bar's numerator is the
    # rounds claimed lexical under m:261's claiming order, forced and free, over A2s + A3s; "reported for the
    # label-naming arms" (m:330) and the contrast arms: A1s over all its rounds, each contrast arm over its
    # forced rounds only (m:271's withholding, as Q-F0's looks withhold a contrast arm's free rounds).
    res = [bars.evaluate(records, bars.bar(f"round_degeneracy@campaign-{keys.UNIT}"), look=look),
           bars.evaluate(records, bars.bar(f"reasoning_line_defect@campaign-{keys.UNIT}"), look=look),
           bars.evaluate(records, bars.bar(f"own_pair_lexical@campaign-{keys.UNIT}"), look=look)]
    fis, ab = bars.bar(f"exclusion_guard_fisher@campaign-{keys.UNIT}"), bars.bar(f"exclusion_guard_abs@campaign-{keys.UNIT}")
    arms_ = {a: [r for r in records if r["template"] == a] for a in keys.TEMPLATES}
    for c, s in keys.PAIRS:
        kc = sum(sc_mod.prepick_excluded(r) for r in arms_[c])
        ks = sum(sc_mod.prepick_excluded(r) for r in arms_[s])
        res.append(fis.evaluate(kc, len(arms_[c]), template=c, look=look, sham_k=ks, sham_n=len(arms_[s])))
        res.append(ab.evaluate(kc, len(arms_[c]), template=c, look=look))
    beside = {}
    for a in keys.TEMPLATES:
        rounds = [x for r in arms_[a] for x in r["rounds"] if keys.is_sham(a) or x["phase"] == "forced"]
        beside[a] = {"scope": "all task rounds" if keys.is_sham(a) else "forced rounds only",
                     "rounds": len(rounds),
                     "degeneracy": sum(x["audit"]["claim"] in bars.DEGEN_CLAIMS for x in rounds),
                     "lexical": sum(x["audit"]["claim"] == "lexical" for x in rounds)}
    arms_out = {a: {"launched": len(g), "prepick_excluded": sum(sc_mod.prepick_excluded(r) for r in g),
                    "domain": sum(bool(r["domain"]) for r in g),
                    "read_flags": _read_flags(g, first_only=keys.is_contrast(a))} for a, g in arms_.items()}
    return {"look": look, "at_launches": len(records), "fired": any(r.fired for r in res),
            "results": [r.as_dict() for r in res], "arms": arms_out, "beside": beside}


def _pause_public(p: Mapping) -> dict:
    adj = p.get("adjudication")
    return {"kind": p["kind"], "at_launches": p["at_launches"], "adjudicated": adj is not None,
            "adjudication_sha16": _sha16_text(adj)}


def run_campaign(adapter, *, floors: Mapping[str, int], launch_counts: Mapping[str, int], hour_cap: Any,
                 prior_ckpt, ckpt_path=None, resume: bool = False, identity_extra: Mapping[str, Any],
                 out_root=DEFAULT_OUT, adjudication: str | None = None, pi_stop: str | None = None) -> dict:
    """Q-F3's campaign (m:192, m:247, m:330): floors / launch counts / hour cap are LOCK-m-F3 v1.0's;
    ``prior_ckpt`` is G-F3's (PASS); ``adjudication`` names the seat's ruling on a pending pause; ``pi_stop``
    the PI's stop (terminal). m's run_campaign, carried: L is a projection, the committed schedule bounds."""
    fl, lc = _per_arm(floors, "floors"), _per_arm(launch_counts, "launch_counts")
    if any(fl[a] > lc[a] for a in keys.TEMPLATES):
        raise ValueError("a floor exceeds its launch count")
    for nm, v in (("adjudication", adjudication), ("pi_stop", pi_stop)):
        if v is not None and not (isinstance(v, str) and v.strip()):
            raise ValueError(f"{nm} must be a non-empty text when given")
    name = stage_name("campaign")
    paths = out_paths("campaign", out_root)
    cpath = checkpoint_path(ckpt_path, paths)
    paths = for_checkpoint(paths, cpath)
    stub = _is_stub(adapter)
    extra = _extra(identity_extra, stage="campaign", stub=stub)
    prov = _begin(adapter, "campaign", name, cpath, {**paths, "reads": None}, extra)
    prior = _licensed(adapter, "campaign", name, extra, prior_ckpt)
    pool, _r, rsha = _renders_of_record(extra, name)
    scheds = load_committed([("campaign", a) for a in keys.TEMPLATES], paths["schedules"])
    n_sched = {a: int(scheds[a]["n"]) for a in keys.TEMPLATES}
    if any(lc[a] > n_sched[a] for a in keys.TEMPLATES):
        raise ValueError(f"a launch count exceeds the committed schedule ({n_sched})")
    bars.assert_firing_complete()
    setup, audit_sha, ban_sha = _startup(adapter)
    cap = extra["reasoning_cap"]
    path_cached = guard.cached_path_admitted("campaign", backend_identifier=rs.backend_identifier(adapter.provenance()),
                                             reasoning_cap=cap)
    # PIN (Code, declared at LOCK-m-F3 v0.1; m's PIN carried, and B7): the G-ID-F3 artifact on disk is
    # re-checked as G-F3 checked it -- this run's proposal (or one the lock re-adopts), not the stub's on a
    # non-stub run, and AT THE RUN'S CAP: an artifact at another cap refuses the campaign (G-ID-F3 re-runs
    # first, m:174), it never sends it uncached.
    ap = gid_artifact_problems(accepted=accepted_proposals(extra["proposal_sha256"], extra["prior_proposal_sha256s"]),
                               require_real=not stub, reasoning_cap=cap)
    if ap:
        raise SystemExit(f"{ap[0]} -- {name} does not take its path from it")
    path = _locked(name, extra, path_cached, cpath)
    refinish_only = path != ("cached" if path_cached else "uncached")
    ident = _identity(adapter, "campaign", keys.TEMPLATES, path, n_sched, scheds, audit_sha, ban_sha, extra, pool,
                      rsha, hour_cap=hour_cap)
    show = adjudication is None and pi_stop is None and _paused_unadjudicated(cpath)
    ckpt = rs.load_or_init(cpath, ident, resume or show)
    _refuse_stopped(ckpt, cpath)
    _record_prior(ckpt, prior, cpath)
    _record_licence(ckpt, extra, cpath)
    camp = ckpt.get("campaign")
    if camp is None:
        camp = ckpt["campaign"] = {"floors": fl, "launch_counts_projection": lc, "pauses": [], "terminal": None,
                                   "end_look": None, "pi_stop": None}
    elif camp.get("floors") != fl or camp.get("launch_counts_projection") != lc:
        raise SystemExit("CHECKPOINT MISMATCH: floors / launch-count projection differ from the recorded ones")
    if camp["terminal"] is not None:
        raise SystemExit(f"CAMPAIGN ENDED at {cpath} ({camp['terminal']['status']}); terminal (m:247)")
    rec_pi = camp.get("pi_stop")
    if pi_stop is not None and rec_pi is not None and pi_stop.strip() != rec_pi:
        raise SystemExit(f"CHECKPOINT MISMATCH: {cpath} records the PI's stop; this run offers another text -- refusing")
    pending = rs.pending_end(ckpt)
    if pending is not None:
        return _refinish_campaign(name, ckpt, cpath, paths, prov, pending, adjudication=adjudication,
                                  pi_stop=pi_stop if rec_pi is None else None)
    if refinish_only:
        raise SystemExit(f"PATH MISMATCH ({name}): the end pending at {cpath} is gone -- refusing to launch (m:267)")
    pi = pi_stop.strip() if pi_stop is not None else rec_pi
    if pi is not None and not ckpt["sessions"]:
        raise SystemExit(f"PI STOP REFUSED at {cpath}: no session has launched -- a unit that never launches is NOT-RUN "
                         f"by its Clock (m:192)")
    last = camp["pauses"][-1] if camp["pauses"] else None
    if last is not None and last["adjudication"] is None and adjudication is None and pi is None:
        return _show_pause(name, ckpt, cpath, paths)
    camp["pi_stop"] = pi
    if last is not None and last["kind"] == "schedule_exhausted" and pi is None:
        raise SystemExit(f"SCHEDULE EXHAUSTED at {cpath}: {last.get('arm')} has no committed cell left below its floor; "
                         f"only the PI's stop ends this campaign (m:192, m:247)")
    if last is not None and last["adjudication"] is None:
        last["adjudication"] = adjudication.strip() if adjudication is not None else pi
    elif adjudication is not None:
        raise SystemExit(f"NO PAUSE TO ADJUDICATE at {cpath}: the campaign is not paused")
    _append_provenance(ckpt, prov)
    cpath.parent.mkdir(parents=True, exist_ok=True)
    rs.write_checkpoint(cpath, ckpt)
    records = ckpt["sessions"]
    launches = {a: sum(r["template"] == a for r in records) for a in keys.TEMPLATES}
    domain = {a: sum(bool(r["domain"]) for r in records if r["template"] == a) for a in keys.TEMPLATES}
    status = "PI-STOP" if pi is not None else None
    hit = pause = None
    rotation = schedule.interleave(list(keys.TEMPLATES), lambda a: domain[a] >= fl[a], start_counts=dict(launches))
    while status is None:
        if rs.hour_cap_exceeded(ckpt, hour_cap):
            status = "CAP"
            break
        arm = next(rotation, None)
        if arm is None:
            status = "COMPLETE"
            break
        s = launches[arm]
        if s >= n_sched[arm]:
            pause = {"at_launches": len(records), "kind": "schedule_exhausted", "arm": arm, "adjudication": None}
            status = "PAUSE"
            break
        rs.note_launch(ckpt)
        rec, problems = _launch(adapter, setup, "campaign", arm, s, scheds[arm]["cells"][s], path_cached=path_cached,
                                reasoning_cap=cap)
        if problems:
            hit = _verify_hit(arm, s, problems, rec)
            status = "STOP"
            break
        at = len(records) + 1
        look = campaign_look(records + [rec], at // LOOK_EVERY) if at % LOOK_EVERY == 0 else None
        rs.record_session(ckpt, rec, look=look)
        launches[arm] += 1
        domain[arm] += int(bool(rec["domain"]))
        hit = _hair_hit(rec)
        if hit is None:
            if look is not None and look["fired"]:
                pause = {"at_launches": at, "kind": "look", "look": look["look"],
                         "bars": [r["name"] for r in look["results"] if r["fired"]], "adjudication": None}
            else:
                rs.write_checkpoint(cpath, ckpt)
        print(readrule.session_line(rec), flush=True)
        if hit is not None:
            status = "STOP"
            break
        if look is not None:
            if look["fired"]:
                status = "PAUSE"
            else:
                for r in look["results"]:
                    print(r["message"], flush=True)
    pending, lines_ = _campaign_end(name, ckpt, status, hit, pause, pi)
    return _complete_campaign(name, ckpt, cpath, paths, pending, hit, lines_)


def _paused_unadjudicated(cpath: Path) -> bool:
    if not Path(cpath).is_file():
        return False
    try:
        ck = json.loads(Path(cpath).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError):
        return False
    camp = ck.get("campaign") if isinstance(ck, dict) else None
    if (not isinstance(camp, dict) or rs.pending_end(ck) is not None or rs.ended_status(ck) is not None
            or not camp.get("pauses")):
        return False
    last = camp["pauses"][-1]
    return isinstance(last, dict) and last.get("adjudication") is None


def _is_gver(hit: Mapping) -> bool:
    return hit["bar"] in (verify.MISMATCH, verify.BREAK)


def _stop_end_look(ckpt: Mapping, hit: Mapping) -> tuple[dict | None, dict | None]:
    """m's _stop_end_look, carried (the seat's C9(ii)): the end look at a STOP over the recorded launches."""
    records = ckpt["sessions"]
    n = len(records)
    if n == 0:
        return None, None
    last_look = ckpt["looks"][-1] if ckpt["looks"] else None
    if n % LOOK_EVERY == 0 and last_look is not None and last_look["at_launches"] == n:
        res = last_look["result"]
        end_look = {**copy.deepcopy(res), "end_is_look": res["look"]}
        if _is_gver(hit) or not res["fired"]:
            return end_look, None
        return end_look, {"at_launches": n, "kind": "look", "look": res["look"],
                          "bars": [r["name"] for r in res["results"] if r["fired"]], "adjudication": None}
    end_look = campaign_look(records, "end")
    if not end_look["fired"]:
        return end_look, None
    return end_look, {"at_launches": n, "kind": "end_look", "look": "end",
                      "bars": [r["name"] for r in end_look["results"] if r["fired"]], "adjudication": None}


def _pause_lines(name: str, ckpt: Mapping, pause: Mapping | None, end_look: Mapping | None) -> list[str]:
    if pause is None:
        if end_look is None:
            return []
        if "end_is_look" in end_look:
            return [f"END LOOK {name}: the end look is look {end_look['end_is_look']} (at {end_look['at_launches']} launches)"]
        return [r["message"] for r in end_look["results"]]
    if pause["kind"] == "look":
        looks = {lk["result"]["look"]: lk["result"] for lk in ckpt["looks"]}
        return [r["message"] for r in looks[pause["look"]]["results"]]
    if pause["kind"] == "schedule_exhausted":
        return [f"PAUSE {name}: {pause['arm']} exhausted its committed schedule ({ckpt['identity']['n'][pause['arm']]}) "
                f"below its floor; the PI decides (m:192, m:247)"]
    if pause["kind"] == "end_look" and end_look is not None:
        return [r["message"] for r in end_look["results"]]
    return []


def _stop_lines(name: str, ckpt: Mapping, hit: Mapping, end_look: Mapping | None, pause: Mapping | None) -> list[str]:
    lines_ = list(announce_stop("campaign", hit)[0])
    if end_look is None:
        return lines_
    if "end_is_look" in end_look and _is_gver(hit):
        return lines_ + _pause_lines(name, ckpt, None, end_look)
    return lines_ + [r["message"] for r in end_look["results"]]


def _campaign_end(name: str, ckpt: Mapping, status: str | None, hit: Mapping | None, pause: Mapping | None,
                  pi: str | None) -> tuple[dict, list[str]]:
    records = ckpt["sessions"]
    stop = terminal = end_look = None
    fired: list[str] = []
    lines_: list[str] = []
    pause = copy.deepcopy(pause)
    if hit is not None:
        _, blinded = announce_stop("campaign", hit)
        stop, status = _stop_record(hit, blinded), "STOP"
        end_look, pause = _stop_end_look(ckpt, hit)
        fired = [hit["bar"]] + list((pause or {}).get("bars") or [])
        lines_ = _stop_lines(name, ckpt, hit, end_look, pause)
    elif status in TERMINAL:
        n = len(records)
        if n == 0:
            raise AssertionError("a campaign cannot end terminal with no launch")
        terminal = {"status": status, "at_launches": n}
        if status == "PI-STOP":
            terminal["text"] = pi
        last_look = ckpt["looks"][-1] if ckpt["looks"] else None
        if n % LOOK_EVERY == 0 and last_look is not None and last_look["at_launches"] == n:
            end_look = {**copy.deepcopy(last_look["result"]), "end_is_look": last_look["result"]["look"]}
        else:
            end_look = campaign_look(records, "end")
            if end_look["fired"]:
                pause = {"at_launches": n, "kind": "end_look", "look": "end",
                         "bars": [r["name"] for r in end_look["results"] if r["fired"]], "adjudication": None}
                fired, status = list(pause["bars"]), "PAUSE"
        lines_ = _pause_lines(name, ckpt, pause, end_look)
    elif status == "PAUSE" and pause is not None:
        fired = list(pause.get("bars") or [])
        lines_ = _pause_lines(name, ckpt, pause, None)
    else:
        raise AssertionError(f"a campaign invocation ended without an end ({status!r})")
    return ({"status": status, "fired": fired, "stop": stop, "terminal": terminal, "end_look": end_look,
             "pause": pause}, lines_)


def _campaign_report(name: str, ck: Mapping, cpath: Path, paths: Mapping, status: str, stop_block) -> dict:
    ident, camp, records = ck["identity"], ck["campaign"], ck["sessions"]
    launches = {a: sum(r["template"] == a for r in records) for a in keys.TEMPLATES}
    domain = {a: sum(bool(r["domain"]) for r in records if r["template"] == a) for a in keys.TEMPLATES}
    end_look = camp["end_look"]
    # PIN (Code, declared at LOCK-m-F3 v0.1; m's PIN carried): the campaign report is pick-free -- looks with
    # pooled pre-pick exclusion, domain and read-flag counts per arm, pauses without their texts, the terminal
    # status, the hour cap reached, the SHAM arms' generation ms (a total including contrast sessions stays in
    # the checkpoint) -- and the campaign writes no reads file and no first-pick share (m:318).
    return {"schema": REPORT_SCHEMA, "form": "pick-free campaign report (m:318: at looks, pooled pre-pick exclusion "
                                             "counts per arm)",
            "unit": keys.UNIT, "stage": "campaign", "stage_name": name, "status": status,
            "floors": dict(camp["floors"]), "launch_counts_projection": dict(camp["launch_counts_projection"]),
            "schedule_n": {a: int(ident["n"][a]) for a in keys.TEMPLATES}, "hour_cap": ident["hour_cap"],
            "hour_cap_reached": bool(rs.hour_cap_exceeded(ck, ident["hour_cap"])),
            "sham_generation_ms": {a: sum(rs.session_ms(r) for r in records if r["template"] == a) for a in keys.SHAM},
            "arms": {a: {"launched": launches[a], "domain": domain[a],
                         "prepick_excluded": sum(sc_mod.prepick_excluded(r) for r in records if r["template"] == a)}
                     for a in keys.TEMPLATES},
            "looks": [lk["result"] for lk in ck["looks"]],
            "looks_count": len(ck["looks"]) + int(end_look is not None and "end_is_look" not in end_look),
            "end_look": end_look, "pauses": [_pause_public(p) for p in camp["pauses"]],
            "terminal": ({k: camp["terminal"][k] for k in ("status", "at_launches")} if camp["terminal"] else None),
            "stop": copy.deepcopy(stop_block), "identity": _ident_summary(ident), "provenance": rs.report_provenance(ck),
            "files": {"checkpoint": _rel(cpath, paths["root"])}}


def _campaign_events(ckpt: Mapping, hit: Mapping | None) -> list[dict]:
    camp, records = ckpt["campaign"], ckpt["sessions"]
    looks = {lk["result"]["look"]: lk["result"] for lk in ckpt["looks"]}
    events: list[dict] = []
    for p in camp["pauses"]:
        ev: dict = {"event": "PAUSE", "kind": p["kind"], "at_launches": p["at_launches"], "bars": list(p.get("bars") or [])}
        if p["kind"] == "look":
            ev["counts"] = copy.deepcopy(looks.get(p["look"]))
        elif p["kind"] == "end_look":
            ev["counts"] = copy.deepcopy(camp["end_look"])
        else:
            upto = [r for r in records[:p["at_launches"]] if r["template"] == p["arm"]]
            ev["counts"] = {"arm": p["arm"], "floor": camp["floors"][p["arm"]], "schedule_n": ckpt["identity"]["n"][p["arm"]],
                            "launched": len(upto), "domain": sum(bool(r["domain"]) for r in upto)}
        ev["picks_revealed"] = []
        events.append(ev)
    if hit is not None:
        events.append({**_hit_event(records, hit), "at_launches": len(records)})
    return events


def _campaign_outputs(name: str, ck: Mapping, cpath: Path, paths: Mapping, status: str, hit) -> tuple[dict, dict | None, Path]:
    stop_block = ck["stop"]["blinded"] if ck.get("stop") else None
    report = _campaign_report(name, ck, cpath, paths, status, stop_block)
    events = _campaign_events(ck, hit)
    apath = adjudication_path(cpath)
    if events:
        report["files"]["adjudication"] = _rel(apath, paths["root"])
    _assert_pick_free(report, name)
    adj = _adjudication_doc("campaign", name, cpath, paths["root"], events) if events else None
    return report, adj, apath


def _write_campaign_outputs(paths: Mapping, report: Mapping, adj, apath: Path) -> Path | None:
    _write_json(paths["report"], report)
    if adj is not None:
        _write_json(apath, adj)
        return apath
    _remove_stale(apath)
    return None


def _campaign_done(name: str, ck: Mapping, cpath: Path, paths: Mapping, status: str, apath, lines_) -> dict:
    for ln in lines_:
        print(ln, flush=True)
    print(_stage_line(name, status, ck["identity"]["path"]), flush=True)
    for k, p in [("CHECKPOINT", cpath), ("REPORT", paths["report"])] + ([("ADJUDICATION", apath)] if apath else []):
        print(f"{k} {p}", flush=True)
    return {"status": status, "stage_name": name, "checkpoint": cpath, "report": paths["report"],
            "launches": {a: sum(r["template"] == a for r in ck["sessions"]) for a in keys.TEMPLATES},
            "domain": {a: sum(bool(r["domain"]) for r in ck["sessions"] if r["template"] == a) for a in keys.TEMPLATES},
            "adjudication": apath}


def _complete_campaign(name: str, ckpt: dict, cpath: Path, paths: Mapping, pending: Mapping, hit, lines_) -> dict:
    final, first = _pend(ckpt, cpath, pending, name)
    report, adj, apath = _campaign_outputs(name, final, cpath, paths, pending["status"], hit)
    if first:
        _write_pending(cpath, ckpt, final)
    written = _write_campaign_outputs(paths, report, adj, apath)
    rs.persist_end(cpath, final)
    return _campaign_done(name, final, cpath, paths, pending["status"], written, lines_)


def _refinish_campaign(name: str, ckpt: dict, cpath: Path, paths: Mapping, prov: Mapping, pending: Mapping, *,
                       adjudication, pi_stop) -> dict:
    _append_provenance(ckpt, prov)
    rs.write_checkpoint(cpath, ckpt)
    print(_refinish_line(name, pending["status"], cpath), flush=True)
    hit = _hit_from_stop(pending["stop"])
    lines_ = (_stop_lines(name, ckpt, hit, pending.get("end_look"), pending.get("pause")) if hit is not None
              else _pause_lines(name, ckpt, pending.get("pause"), pending.get("end_look")))
    res = _complete_campaign(name, ckpt, cpath, paths, pending, hit, lines_)
    skipped = [w for w, v in (("the seat's adjudication", adjudication), ("the PI's stop", pi_stop)) if v is not None]
    ended = "STOP" if pending.get("stop") is not None else (pending.get("terminal") or {}).get("status")
    if skipped and ended is not None:
        raise SystemExit(f"NOT APPLIED ({name}): this invocation re-finished the end pending at {cpath} "
                         f"({pending['status']}); {' and '.join(skipped)} it offered was not applied, and cannot be "
                         f"through stages: that end leaves the campaign ended ({ended}) -- a ruling on a pause it carries "
                         f"enters VERDICTS as the declared --adjudication file, a PI's stop on a hair trigger as the "
                         f"declared --pi-stop record (the seat's C3 and C2, carried)")
    if skipped:
        raise SystemExit(f"NOT APPLIED ({name}): this invocation re-finished the end pending at {cpath} "
                         f"({pending['status']}); {' and '.join(skipped)} it offered was not applied -- offer it again")
    return res


def _show_pause(name: str, ckpt: Mapping, cpath: Path, paths: Mapping) -> dict:
    last = ckpt["campaign"]["pauses"][-1]
    report, adj, apath = _campaign_outputs(name, ckpt, cpath, paths, "PAUSE", None)
    apath = _write_campaign_outputs(paths, report, adj, apath)
    tail = ("only the PI's stop (pi_stop) ends it (m:192, m:247)" if last["kind"] == "schedule_exhausted"
            else "a resume needs the seat's adjudication (m:330) or the PI's stop; Code never self-adjudicates")
    return _campaign_done(name, ckpt, cpath, paths, "PAUSE", apath,
                          [f"PAUSE {name}: the campaign at {cpath.name} is paused ({last['kind']}, at "
                           f"{last['at_launches']} launches); its report and excerpt are re-derived, nothing launched; {tail}"])


# --- self-test helpers (selftests only) -----------------------------------------------------------------
class _Interrupt(RuntimeError):
    """A simulated crash inside a session: the checkpoint keeps what was written."""


def _script_policy(stage: str, cells: Mapping[tuple[str, int], Mapping],
                   rule: Callable[[str, int, str, int, dict], Any] | None = None,
                   interrupt: Callable[[str, int, str, int], bool] | None = None) -> Callable[[dict], Any]:
    """A texts-callable addressing every generation as (template, s, kind, index) through its seed: m:159's
    arm-rng draws replayed for F3 (4 forced seeds; per choice the reasoning seed, the menu draw, the chosen
    seed). ``rule`` returns a text / spec or None for a clean one."""
    from . import testing
    smap: dict[int, tuple] = {}
    for (t, s), cell in cells.items():
        rng = keys.stream(keys.arm_key(stage, t, s))
        for i in range(sc_mod.N_FORCED):
            smap.setdefault(int(rng.integers(2**31)), (t, s, "forced", i))
        for ci in range(6):
            smap.setdefault(int(rng.integers(2**31)), (t, s, "line", ci))
            rng.integers(2)
            smap.setdefault(int(rng.integers(2**31)), (t, s, "chosen", ci))

    def texts(call: dict):
        t, s, kind, i = smap[call["seed"]]
        if interrupt is not None and interrupt(t, s, kind, i):
            raise _Interrupt(f"selftest interrupt at {t} s={s} {kind} {i}")
        x = rule(t, s, kind, i, call) if rule is not None else None
        if x is None:
            x = (testing.LINES[(i + s) % len(testing.LINES)] if kind == "line"
                 else testing.CLEAN[(i + s + (4 if kind == "chosen" else 0)) % len(testing.CLEAN)])
        return x
    return texts


def _selftest(chk) -> None:
    import contextlib
    import io
    import tempfile
    from unittest import mock

    from . import testing

    prop_sha = hashlib.sha256(PROPOSAL_PATH.read_bytes()).hexdigest()
    _pool, renders = sc_mod.pool_and_renders()
    base_extra = {"lock_sha256": "a" * 64, "proposal_sha256": prop_sha, "renders_sha16": m_corr.renders_sha(renders),
                  "reasoning_cap": 60, **_STUB_WEIGHTS}

    def quiet(fn, *a, **k):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            try:
                return fn(*a, **k), buf.getvalue(), None
            except (SystemExit, ValueError) as e:
                return None, buf.getvalue(), e

    def gate_cells(gate):
        return {(t, j): schedule.gate_schedule(gate, t, schedule.GATE_PLAN_COUNTS[(gate, t)])[j]
                for t in (keys.TEMPLATES if gate != "id" else keys.GID_TEMPLATES)
                for j in range(schedule.GATE_PLAN_COUNTS[(gate, t)])}

    def adapter(stage, rule=None, interrupt=None):
        a = testing.F3Adapter()
        a.load(_script_policy(stage, gate_cells(stage) if stage != "campaign" else camp_cells, rule, interrupt), None)
        return a

    camp_cells = {(t, s): schedule.campaign_schedule(t, 1)[s] for t in keys.TEMPLATES for s in range(16)}
    tc_time = [(t, 1) for t in keys.TEMPLATES]
    tc_qual = [(t, schedule.GATE_PLAN_COUNTS[("qual", t)]) for t in keys.TEMPLATES]
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "mf3"
        schedule.write_schedule_files(root / "schedules")
        gates_dir = Path(td) / "gates"
        gates_dir.mkdir()
        with mock.patch.object(guard, "GATES_DIR", gates_dir):
            # --- G-TIME-F3: PASS, the cap trigger counted over all six ------------------------
            def caps(t, s, kind, i, call):
                if kind == "line" and keys.is_contrast(t) and i < 2 and t != "A3":
                    return {"text": "x " * 30, "n_tok": 60, "cap_hit": True, "stop_reason": "cap"}
                if kind == "line" and t == "A2s" and i == 0:
                    return {"text": "y " * 30, "n_tok": 60, "cap_hit": True, "stop_reason": "cap"}
                return None
            res, out, err = quiet(run_gate_stage, adapter("time", caps), gate="time", templates_counts=tc_time,
                                  identity_extra={**base_extra, "locked_path": "uncached"}, out_root=root)
            ck_time = root / "ckpt" / "Q-F3_time.json"
            rep = json.loads((root / "reports" / "Q-F3_time_report.json").read_text())
            reads = json.loads((root / "reports" / "Q-F3_time_reads.json").read_text())
            chk("mf3.stages: G-TIME-F3 on the stub -- six sessions, PASS; the cap trigger counts cap-reach over all six "
                "sessions' lines (4 contrast + 1 sham = 5 of 36 -> 120); contrast blocks are ruling (h)'s counts plus "
                "the per-line cap booleans; the stopped/ended checkpoint persists PASS",
                err is None and res["status"] == "PASS" and rep["cap_trigger"]["cap_reached"] == 5
                and rep["cap_trigger"]["lines"] == 36 and rep["cap_trigger"]["fixed_cap"] == 120
                and set(rep["stage_report"]["templates"]["A1"]) == set(readrule.TIME_CONTRAST_KEYS)
                and rep["stage_report"]["templates"]["A1"]["per_session"][0]["reasoning_cap_reached"][:2] == [True, True]
                and rs.read_checkpoint(ck_time)["stage_end"]["status"] == "PASS"
                and all("reasoning" not in r for r in reads["sessions"] if r["contrast"]), (err, rep.get("cap_trigger")))
            labels = {w for p in schedule.roster() for w in p}
            chk("mf3.stages: G-TIME-F3's stdout, report and reads name no label in a pick-free form; session lines are "
                "the declared forms",
                not any(re.search(rf"\b{w}\b", out) for w in labels)
                and not any(re.search(rf"\b{w}\b", json.dumps(rep)) for w in labels)
                and sum(ln.startswith("time A") for ln in out.splitlines()) == 6, out[:200])
            # --- G-TIME-F3: the sham line bar fires (STOP); n = 0 lines is no test (reported, not fired) -----
            def echo_sham(t, s, kind, i, call):
                return "Reasoning (one line): ok" if kind == "line" and keys.is_sham(t) and i < 2 else None
            r2 = root.parent / "time-stop"
            schedule.write_schedule_files(r2 / "schedules")
            res2, out2, err2 = quiet(run_gate_stage, adapter("time", echo_sham), gate="time", templates_counts=tc_time,
                                     identity_extra={**base_extra, "locked_path": "uncached"}, out_root=r2)
            adj2 = json.loads((r2 / "ckpt" / "Q-F3_time_adjudication.json").read_text())
            chk("mf3.stages: G-TIME-F3 STOPs when its sham reasoning-line bar fires (6 echo lines of 18 >= 5); the "
                "excerpt holds the sham lines; the cap-trigger count is still reported",
                err2 is None and res2["status"] == "STOP" and res2["bars"][1].fired
                and adj2["events"][0]["kind"] == "bars" and len(adj2["events"][0]["rounds"]) == 6
                and "CAP TRIGGER" in out2, (err2, res2 and res2["status"]))

            def lex_sham(t, s, kind, i, call):
                if kind == "forced" and keys.is_sham(t) and i == 3:
                    return gate_cells("time")[(t, 0)]["P"].capitalize() + " is the answer."
                return None
            r3 = root.parent / "time-notest"
            schedule.write_schedule_files(r3 / "schedules")
            res3, out3, err3 = quiet(run_gate_stage, adapter("time", lex_sham), gate="time", templates_counts=tc_time,
                                     identity_extra={**base_extra, "locked_path": "uncached"}, out_root=r3)
            rep3 = json.loads((r3 / "reports" / "Q-F3_time_report.json").read_text())
            chk("mf3.stages: every sham session excluded at its fourth forced round leaves 0 sham lines -- the line "
                "bar is reported as no test and not fired, and the stage ends on its other bars (B30, by analogy with "
                "m:271's 'reported, not fired')",
                err3 is None and res3["status"] == "PASS" and "NO TEST reasoning_line_defect@G-TIME-F3" in out3
                and rep3["no_test"] == ["reasoning_line_defect@G-TIME-F3"], (err3, res3 and res3["status"]))
            # --- refusals at the start ----------------------------------------------------------------
            refused = []
            for kw in ({"identity_extra": {**base_extra, "locked_path": "cached"}},
                       {"identity_extra": {**base_extra, "locked_path": "uncached", "reasoning_cap": 120}},
                       {"identity_extra": {**base_extra, "locked_path": "uncached", "lock_sha256": "pre-lock"}},
                       {"identity_extra": {**base_extra, "locked_path": "uncached", "renders_sha16": "0" * 16}},
                       {"identity_extra": {**base_extra, "locked_path": "uncached"}, "prior_ckpt": ck_time}):
                _, _, e = quiet(lambda **k: run_gate_stage(adapter("time"), gate="time", templates_counts=tc_time,
                                                           out_root=root.parent / "never", **k), **kw)
                refused.append(e is not None or False)
            try:
                quiet(run_gate_stage, adapter("time"), gate="time", templates_counts=tc_time,
                      identity_extra={**base_extra, "locked_path": "uncached"}, out_root=root)
                refused.append(False)
            except Exception:                                  # noqa: BLE001
                refused.append(False)
            _, _, e = quiet(run_gate_stage, adapter("time"), gate="time", templates_counts=tc_time,
                            identity_extra={**base_extra, "locked_path": "uncached"}, out_root=root)
            refused[-1] = e is not None and "STAGE ENDED" in str(e)
            chk("mf3.stages: G-TIME-F3 refuses a cached lock, a cap of 120, a pre-lock hash, renders other than the "
                "renders of record, a prior stage, and a re-run of its ended checkpoint", all(refused), refused)
            # --- a G-TIME-F3 whose trigger does not fire: the cap stays 60 -------------------------------
            def caps60(t, s, kind, i, call):
                if kind == "line" and t == "A1" and i < 2:
                    return {"text": "x " * 30, "n_tok": 60, "cap_hit": True, "stop_reason": "cap"}
                return None
            r60 = root.parent / "time-60"
            schedule.write_schedule_files(r60 / "schedules")
            res60, _, err60 = quiet(run_gate_stage, adapter("time", caps60), gate="time", templates_counts=tc_time,
                                    identity_extra={**base_extra, "locked_path": "uncached"}, out_root=r60)
            ck_time60 = r60 / "ckpt" / "Q-F3_time.json"
            rep60 = json.loads((r60 / "reports" / "Q-F3_time_report.json").read_text())
            chk("mf3.stages: a G-TIME-F3 whose lines reach the cap twice (2 of 36 < 3) leaves the cap at 60",
                err60 is None and res60["status"] == "PASS" and rep60["cap_trigger"]["cap_reached"] == 2
                and rep60["cap_trigger"]["fixed_cap"] == 60, (err60, rep60.get("cap_trigger")))
            # --- G-ID-F3 ------------------------------------------------------------------------------
            ex60 = {**base_extra}
            _, _, e_cap = quiet(run_gid_pair_f3, adapter("id"), identity_extra=ex60, prior_ckpt=ck_time,
                                out_root=root, ckpt_path=root / "ckpt" / "gid-wrong-cap.json")
            _, _, e_cap2 = quiet(run_gid_pair_f3, adapter("id"), identity_extra={**base_extra, "reasoning_cap": 120},
                                 prior_ckpt=ck_time60, out_root=root, ckpt_path=root / "ckpt" / "gid-wrong-cap2.json")
            chk("mf3.stages: G-ID-F3 runs only at the cap G-TIME-F3's trigger fixes, re-computed from its checkpoint "
                "(60 refused where the lines fix 120, 120 where they fix 60; m:294-295); no artifact is written",
                e_cap is not None and "NOT THE FIXED CAP" in str(e_cap) and e_cap2 is not None
                and "NOT THE FIXED CAP" in str(e_cap2) and not guard.gid_artifact_path().exists(),
                (str(e_cap)[:90], str(e_cap2)[:90]))
            res4, out4, err4 = quiet(run_gid_pair_f3, adapter("id"), identity_extra=ex60, prior_ckpt=ck_time60,
                                     out_root=root)
            art = json.loads(guard.gid_artifact_path().read_text())
            chk("mf3.stages: G-ID-F3 -- A2s then A3s, uncached then cached at j = 0 each; 2/2 identical -> PASS; the "
                "artifact carries the cap, the backend and both templates' key templates",
                err4 is None and res4["status"] == "PASS" and art["verdict"] == "PASS" and art["n_pairs"] == 2
                and art["identity"]["reasoning_cap"] == 60 and art["templates"] == ["A2s", "A3s"]
                and [(p["template"], p["j"]) for p in art["indices"]] == [("A2s", 0), ("A3s", 0)], (err4, art.get("verdict")))
            bid = rs.backend_identifier(testing.F3Adapter().provenance())
            chk("mf3.stages: the G-ID-F3 PASS licenses the cached path at its cap only",
                guard.cached_path_admitted("qual", backend_identifier=bid, reasoning_cap=60)
                and not guard.cached_path_admitted("qual", backend_identifier=bid, reasoning_cap=120))
            _, _, e5 = quiet(run_gid_pair_f3, adapter("id"), identity_extra=ex60, prior_ckpt=ck_time60,
                             out_root=root, ckpt_path=root / "ckpt" / "gid-again.json")
            chk("mf3.stages: a G-ID-F3 artifact is never overwritten", e5 is not None and "ARTIFACT EXISTS" in str(e5))
            gdir2 = Path(td) / "gates2"
            gdir2.mkdir()
            with mock.patch.object(guard, "GATES_DIR", gdir2):
                def diverge(t, s, kind, i, call):
                    return "Eight." if (call["cached"] and t == "A3s" and kind == "forced" and i == 1) else None
                res6, _, err6 = quiet(run_gid_pair_f3, adapter("id", diverge), identity_extra=ex60, prior_ckpt=ck_time60,
                                      out_root=root, ckpt_path=root / "ckpt" / "gid-fail.json")
                fart = json.loads(guard.gid_artifact_path().read_text())

                def incomplete(t, s, kind, i, call):
                    return ("{Pc} wins." .replace("{Pc}", gate_cells("id")[(t, s)]["P"].capitalize())
                            if t == "A2s" and s == 0 and kind == "chosen" and i == 2 else None)
                gdir3 = Path(td) / "gates3"
                gdir3.mkdir()
                with mock.patch.object(guard, "GATES_DIR", gdir3):
                    res7, _, err7 = quiet(run_gid_pair_f3, adapter("id", incomplete), identity_extra=ex60,
                                          prior_ckpt=ck_time60, out_root=root, ckpt_path=root / "ckpt" / "gid-adv.json")
                def meta_diverge(t, s, kind, i, call):
                    if t == "A2s" and kind == "line" and i == 0:
                        return ({"text": "Plain line.", "n_tok": 60, "cap_hit": True, "stop_reason": "cap"}
                                if call["cached"] else
                                {"text": "Plain line.", "n_tok": 3, "cap_hit": False, "stop_reason": "newline"})
                    return None
                gdir4 = Path(td) / "gates4"
                gdir4.mkdir()
                with mock.patch.object(guard, "GATES_DIR", gdir4):
                    res_m, _, err_m = quiet(run_gid_pair_f3, adapter("id", meta_diverge), identity_extra=ex60,
                                            prior_ckpt=ck_time60, out_root=root, ckpt_path=root / "ckpt" / "gid-meta.json")
                    mart = json.loads(guard.gid_artifact_path().read_text())
            chk("mf3.stages: G-ID-F3 reports, beside m:281's criterion, whether the pair's generations agree in token "
                "count, cap flag and stop reason -- a transcript-identical pair whose cached line reached the cap is "
                "PASS with meta_identical false (descriptive, finding 9); the clean pairs are meta-identical",
                err_m is None and res_m["status"] == "PASS" and mart["pairs_identical"] == [True, True]
                and [p["meta_identical"] for p in mart["indices"]] == [False, True]
                and all(p["meta_identical"] for p in art["indices"]), (err_m, mart.get("indices")))
            chk("mf3.stages: G-ID-F3 FAILs on a divergent pair (A3s); an incomplete identical A2s pair advances A2s's "
                "index to j = 1 before A3s runs (m:281's rule, the seat's Q8)",
                err6 is None and res6["status"] == "FAIL" and fart["verdict"] == "FAIL"
                and fart["pairs_identical"] == [True, False]
                and err7 is None and res7["status"] == "PASS"
                and [(p["template"], p["j"], p["complete"]) for p in res7["pairs"]]
                == [("A2s", 0, False), ("A2s", 1, True), ("A3s", 0, True)], (err6, err7, res7 and res7["pairs"]))
            # --- G-F3 -------------------------------------------------------------------------------------
            exq = {**base_extra, "locked_path": "cached"}
            res8, out8, err8 = quiet(run_gate_stage, adapter("qual"), gate="qual", templates_counts=tc_qual,
                                     identity_extra=exq, out_root=root, prior_ckpt=ck_time60)
            rq = json.loads((root / "reports" / "Q-F3_qual_report.json").read_text())
            chk("mf3.stages: G-F3 on the cached path the G-ID-F3 PASS licenses -- 40 sessions, PASS, both bars silent, "
                "the contrast arms' first-read flags reported, no label in the report",
                err8 is None and res8["status"] == "PASS" and sum(rq["recorded"].values()) == 40
                and [b["name"] for b in rq["bars"]] == ["round_degeneracy@G-F3", "reasoning_line_defect@G-F3"]
                and sorted(rq["contrast_first_read_flags"]) == list(keys.CONTRAST) and rq["identity"]["path"] == "cached"
                and not any(re.search(rf"\b{w}\b", json.dumps(rq)) for w in labels), err8)
            _, _, e9 = quiet(run_gate_stage, adapter("qual"), gate="qual", templates_counts=tc_qual,
                             identity_extra={**base_extra, "locked_path": "uncached"}, out_root=root,
                             prior_ckpt=ck_time60, ckpt_path=root / "ckpt" / "qual-uncached.json")
            _, _, e10 = quiet(run_gate_stage, adapter("qual"), gate="qual", templates_counts=tc_qual,
                              identity_extra={**base_extra, "reasoning_cap": 120, "locked_path": "uncached"},
                              out_root=root, prior_ckpt=ck_time, ckpt_path=root / "ckpt" / "qual-120.json")
            _, _, e10b = quiet(run_gate_stage, adapter("qual"), gate="qual", templates_counts=tc_qual,
                               identity_extra={**base_extra, "reasoning_cap": 120, "locked_path": "uncached"},
                               out_root=root, prior_ckpt=ck_time60, ckpt_path=root / "ckpt" / "qual-120b.json")
            chk("mf3.stages: G-F3 refuses a lock fixing uncached where the licence gives cached, a cap other than the "
                "one G-TIME-F3's trigger fixes, and (at the fixed cap) a G-ID-F3 artifact at another cap",
                e9 is not None and "PATH MISMATCH" in str(e9) and e10b is not None and "NOT THE FIXED CAP" in str(e10b)
                and e10 is not None and "ANOTHER CAP" in str(e10), (str(e9)[:80], str(e10)[:80], str(e10b)[:80]))
            ck_qual = root / "ckpt" / "Q-F3_qual.json"
            # --- the campaign ------------------------------------------------------------------------------
            exc = {**base_extra, "locked_path": "cached"}
            fl = {a: 2 for a in keys.TEMPLATES}
            lc = {a: 4 for a in keys.TEMPLATES}
            res11, out11, err11 = quiet(run_campaign, adapter("campaign"), floors=fl, launch_counts=lc, hour_cap=40,
                                        prior_ckpt=ck_qual, identity_extra=exc, out_root=root)
            rc = json.loads((root / "reports" / "Q-F3_campaign_report.json").read_text())
            _, _, e_cc = quiet(run_campaign, adapter("campaign"), floors=fl, launch_counts=lc, hour_cap=40,
                               prior_ckpt=ck_qual, identity_extra={**exc, "reasoning_cap": 120}, out_root=root,
                               ckpt_path=root / "ckpt" / "camp-120.json")
            chk("mf3.stages: the campaign refuses a cap other than G-F3's", e_cc is not None
                and "NOT THE FIXED CAP" in str(e_cc), str(e_cc)[:90])
            chk("mf3.stages: a campaign on the stub runs the six-arm rotation to every floor (12 launches) -> COMPLETE "
                "with an end look; the report is pick-free (no reads file, no first-pick share)",
                err11 is None and res11["status"] == "COMPLETE" and res11["launches"] == {a: 2 for a in keys.TEMPLATES}
                and rc["end_look"]["look"] == "end" and not (root / "reports" / "Q-F3_campaign_reads.json").exists()
                and not any(re.search(rf"\b{w}\b", json.dumps(rc)) for w in labels), (err11, res11 and res11["status"]))
            lk = rc["end_look"]
            chk("mf3.stages: a look evaluates round_degeneracy and reasoning-line defects over the three shams, the "
                "pooled lexical bar over A2s + A3s, and both guards per contrast arm (9 results)",
                [r["name"].split("@")[0] for r in lk["results"]]
                == ["round_degeneracy", "reasoning_line_defect", "own_pair_lexical"]
                + ["exclusion_guard_fisher", "exclusion_guard_abs"] * 3
                and lk["beside"]["A1"]["scope"] == "forced rounds only" and lk["beside"]["A1s"]["scope"] == "all task rounds")
            cp2 = root / "ckpt" / "camp-stop.json"

            def contrast_line_scaffold(t, s, kind, i, call):
                return "<|im_start|> go" if (t == "A2" and s == 0 and kind == "line" and i == 2) else None
            res12, out12, err12 = quiet(run_campaign, adapter("campaign", contrast_line_scaffold), floors=fl,
                                        launch_counts=lc, hour_cap=40, prior_ckpt=ck_qual, identity_extra=exc,
                                        out_root=root, ckpt_path=cp2)
            stop12 = rs.read_checkpoint(cp2)["stop"]
            chk("mf3.stages: a scaffold string on a contrast session's third reasoning line STOPs the campaign, "
                "announced by phase alone (class withheld, m:318 exception (1)); the stop block keeps the class",
                err12 is None and res12["status"] == "STOP" and "class is withheld" in out12
                and "scaffold_absorption" not in out12 and stop12["bar"] == "scaffold_absorption"
                and stop12["blinded"]["bar"] == WITHHELD_CLASS and stop12["phase"] == "reasoning", (err12, out12[-300:]))
            cp3 = root / "ckpt" / "camp-interrupt.json"

            def boom(t, s, kind, i):
                return t == "A2" and s == 0 and kind == "chosen" and i == 1

            def crash(cp, interrupt, f, l):
                try:
                    with contextlib.redirect_stdout(io.StringIO()):
                        run_campaign(adapter("campaign", None, interrupt), floors=f, launch_counts=l, hour_cap=40,
                                     prior_ckpt=ck_qual, identity_extra=exc, out_root=root, ckpt_path=cp)
                except _Interrupt:
                    return True
                return False
            interrupted = crash(cp3, boom, fl, lc)
            n_before = len(rs.read_checkpoint(cp3)["sessions"])
            res14, _, err14 = quiet(run_campaign, adapter("campaign"), floors=fl, launch_counts=lc, hour_cap=40,
                                    prior_ckpt=ck_qual, identity_extra=exc, out_root=root, ckpt_path=cp3, resume=True)
            chk("mf3.stages: a crash mid-session keeps what was written (the interrupted session is not recorded); a "
                "--resume skips every finished session and completes",
                interrupted and n_before == 2 and err14 is None and res14["status"] == "COMPLETE"
                and sum(res14["launches"].values()) == 12, (interrupted, n_before, err14))
            cp4 = root / "ckpt" / "camp-pi.json"
            fl_big = {a: 3 for a in keys.TEMPLATES}
            lc_big = {a: 6 for a in keys.TEMPLATES}

            def stop_after(t, s, kind, i):
                return t == "A3s" and s == 1 and kind == "forced" and i == 0
            crash(cp4, stop_after, fl_big, lc_big)
            res15, out15, err15 = quiet(run_campaign, adapter("campaign"), floors=fl_big, launch_counts=lc_big,
                                        hour_cap=40, prior_ckpt=ck_qual, identity_extra=exc, out_root=root,
                                        ckpt_path=cp4, resume=True, pi_stop="the PI stops the campaign")
            term = rs.read_checkpoint(cp4)["campaign"]["terminal"]
            chk("mf3.stages: a PI stop ends a launched campaign terminal (PI-STOP), its text in the checkpoint only",
                err15 is None and res15["status"] == "PI-STOP" and term["status"] == "PI-STOP"
                and "the PI stops" not in out15, (err15, res15 and res15["status"]))
        # --- the licence (C2) on a temporary repository and a hub-cache layout --------------------------
        repo = Path(td) / "repo"
        repo.mkdir()
        hub = Path(td) / "hub" / "models--x--y"
        snap = hub / "snapshots" / ("c" * 40)
        (hub / "blobs").mkdir(parents=True, exist_ok=True)
        (hub / "refs").mkdir(parents=True, exist_ok=True)
        snap.mkdir(parents=True, exist_ok=True)
        for f, txt in {"config.json": "{}", "tokenizer.json": "{}", "w.safetensors": "w",
                       "model.safetensors.index.json": json.dumps({"weight_map": {"a": "w.safetensors"}})}.items():
            b = hub / "blobs" / hashlib.sha256(txt.encode()).hexdigest()
            b.write_text(txt)
            os.symlink(f"../../blobs/{b.name}", snap / f)
        (hub / "refs" / "main").write_text("c" * 40)
        wb = rs.weights_binding(snap)
        mm = guard.m_module_sha256s()
        an = hashlib.sha256(ANALYZER_PATH.read_bytes()).hexdigest()
        pk = guard.package_sha256_of(guard.PACKAGE_DIR)
        (repo / "P.md").write_text("proposal\n")

        def lock_text(m_rows: Mapping[str, str]) -> str:
            return "\n".join([f"analyzer {an}", f"package {pk}", f"weights {wb['revision']} {wb['sha256']}"]
                             + [f"| `valence_core/m/{m}.py` | `{v}` |" for m, v in m_rows.items()]) + "\n"
        swapped = dict(mm)
        swapped["audit"], swapped["bars"] = mm["bars"], mm["audit"]
        locks = {"L.md": lock_text(mm), "L-swapped.md": lock_text(swapped),
                 "L-unnamed.md": "\n".join([an, pk, wb["revision"], wb["sha256"]] + list(mm.values())) + "\n"}
        for f, txt in locks.items():
            (repo / f).write_text(txt)
        for cmd in (["init", "-q"], ["add", "P.md", *locks],
                    ["-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q", "-m", "t"]):
            subprocess.run(["git", *cmd], cwd=repo, capture_output=True)
        ex = {"proposal_file": "P.md", "proposal_sha256": hashlib.sha256(b"proposal\n").hexdigest(), "lock_file": "L.md",
              "lock_sha256": hashlib.sha256(locks["L.md"].encode()).hexdigest(), "analyzer_sha256": an,
              "package_sha256": pk, "m_module_sha256": mm, "weights_revision": wb["revision"],
              "weights_sha256": wb["sha256"]}
        off = {"HF_HUB_OFFLINE": "1"}
        ok = licence_problems(ex, repo=repo, hub_repo=hub, environ=off)
        bad = {"another package": ({**ex, "package_sha256": "9" * 64}, off),
               "an m module moved": ({**ex, "m_module_sha256": {**mm, "audit": "9" * 64}}, off),
               "other weights": ({**ex, "weights_sha256": "9" * 64}, off),
               "an absent m module": ({**ex, "m_module_sha256": {k: v for k, v in mm.items() if k != "corr"}}, off),
               "m's __init__.py unlisted": ({**ex, "m_module_sha256": {k: v for k, v in mm.items() if k != "__init__"}},
                                            off),
               "a lock not naming them": ({**ex, "lock_file": "P.md", "lock_sha256": ex["proposal_sha256"]}, off),
               "a lock naming the m hashes without their files": (
                   {**ex, "lock_file": "L-unnamed.md",
                    "lock_sha256": hashlib.sha256(locks["L-unnamed.md"].encode()).hexdigest()}, off),
               "a lock listing two m hashes under swapped names": (
                   {**ex, "lock_file": "L-swapped.md",
                    "lock_sha256": hashlib.sha256(locks["L-swapped.md"].encode()).hexdigest()}, off),
               "an online load (HF_HUB_OFFLINE unset)": (ex, {}),
               "HF_HUB_OFFLINE other than '1'": (ex, {"HF_HUB_OFFLINE": "true"})}
        silent = [k for k, (v, env) in bad.items() if not licence_problems(v, repo=repo, hub_repo=hub, environ=env)]
        (hub / "refs" / "main").write_text("d" * 40)
        moved = licence_problems(ex, repo=repo, hub_repo=hub, environ=off)
        (hub / "refs" / "main").write_text("c" * 40 + "\n")
        newline = licence_problems(ex, repo=repo, hub_repo=hub, environ=off)
        (hub / "refs" / "main").write_text("c" * 40)
        (repo / "P.md").write_text("edited\n")
        dirty = licence_problems(ex, repo=repo, hub_repo=hub, environ=off)
    chk("mf3.stages: the licence (C2) is clean when the committed lock names the analyzer's and mf3's hashes, each "
        "m file (the ten modules and __init__.py) by name with its sha256 on one line, and the weights, they hold "
        "now, the load is offline and refs/main names the bound revision", ok == [], ok[:2])
    chk(f"mf3.stages: the licence refuses each of {len(bad)} departures (another package, a moved, absent or unlisted "
        "m file, other weights, a lock not naming them, naming the m hashes without their files or under swapped "
        "names, an online load), a refs/main moved to another revision or not the raw revision, and an uncommitted "
        "proposal edit",
        not silent and any("refs/main" in x for x in moved) and any("refs/main" in x for x in newline)
        and dirty != [], (silent, moved[:1], newline[:1], dirty[:1]))
    chk("mf3.stages: guard.check_call_sites is clean over mf3 (the path threads from cached_path_admitted and gid_paths)",
        guard.check_call_sites([guard.PACKAGE_DIR]) == [], guard.check_call_sites([guard.PACKAGE_DIR])[:3])
