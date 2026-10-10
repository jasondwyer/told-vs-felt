"""PROPOSAL-m gate-stage and campaign drivers, Q-F0 subset (v1.11 §2.4 m:247-251;
§2.7 m:267; §3 m:271; §3.1 m:279-286; §3.3 m:302; §4 m:308, m:316, m:318; §6 m:330;
§8 m:357-358).

THE STAGES. ``run_gate_stage`` runs G-TIME (m:280, m:302: one session per arm,
uncached) and the qualification stage (G-F0m-Qwen, m:283; G-F0m-OLMo-{ckpt}, m:302:
8 contrast + 16 sham); ``run_gid_pair`` runs G-ID-F0m (m:281: A0s twice per index,
uncached then cached, 2/2 byte-identical complete pairs); ``run_campaign`` runs a
unit's campaign (m:192, m:247, m:330: strict-rotation interleave, per-arm stop at floor
on DOMAIN sessions -- L is a projection, not a bound -- looks every 40 launches and at
the end, an end by STOP included (the seat's C9(ii), 2026-10-10), the hour cap and a PI
stop terminal). The campaign is built and self-tested on the scripted stub only; it is
not run at step 4.

AT EVERY STAGE START, BEFORE ANY SESSION. The checkpoint path is under
``<out_root>/ckpt/`` (the -diff rule) and names no roster word; a non-stub adapter
writes under REPO/data/m only; an OLMo stage needs its pod id; an ENDED checkpoint is
refused naming its status (a stop by its blinded class only); the adapter's provenance
is JSON-native and names no roster word; the run-time known answers run (numpy's
stream, the banner bytes against §2.5's literals parsed from the proposal FILE the
identity names, roster admissibility of pool, golds, harness strings and e2a's wrapper
-- m:159, m:253-258, rule 18); a non-stub Qwen run passes m:267's laptop checklist,
its analyzer and CLAUDE.md committed at HEAD with identical working-tree bytes, and logs
its gate line (HEAD from ``git rev-parse``); ``identity_extra`` carries the governing
lock's hash (never "pre-lock": every stage here follows its lock), this document's, the
renders' sha16 (the renders of record) and, on a non-stub adapter, the lock's and the
proposal's repo-relative files -- each COMMITTED at HEAD as a regular blob whose bytes
are the working tree's and hash to the identity's value (findings R4, R11; pure object
reads, never ``git diff``) -- and, on a non-stub adapter, the analyzer's and the
package's sha256 (``analyzer_sha256``, ``package_sha256``; the seat's D2, 2026-10-10):
the analyzer's bytes hash to the first, the package this process hashes
(``resume.package_sha256``) is the second, and the committed lock's text names both;
the prior stage's persisted end licenses this one (§8's order, m:280-302) under the
same proposal or one the lock re-adopts
(``prior_proposal_sha256s``), and so must the unit's G-ID artifact wherever it gives
the path; a non-stub stage takes no prior or artifact written on the stub; the path the
G-ID licence gives on THIS backend must be the locked one. Then the adapter's
provenance is appended to the checkpoint and printed (one PROVENANCE line; ledger 27).

PER SESSION, IN THIS ORDER. The cell comes from the COMMITTED schedule file (its
directory verified clean against the construction and every file's sha256 against the
manifest -- a stage never uses regenerated cells, m:159, m:267); the scaffold is
built through ``scaffold.m_config``; ``verify.schedule_check`` runs before the session
as a structural assertion only -- it is true by construction (the scaffold is built
from the very cell it is checked against). What guards m:253/m:271's
schedule_mismatch before a session is ``load_committed`` (the directory regenerated
and every file's sha256 against the manifest), ``startup_problems`` (the banner bytes
against the proposal's §2.5 literals, numpy's stream known answer, roster hygiene) and,
after each session, G-VER: ``verify.verify_and_mark`` runs on the record BEFORE it is
written to the checkpoint ("before any artifact is written", m:284;
``resume.record_session`` refuses an unverified record). Any mismatch is a hair
trigger and STOPs the stage, as does a ``scaffold_absorption`` the runner recorded
(m:271). Generations are never located by searching for "\\n": the verifier rebuilds
from recorded fields.

THE PATH (m:267). G-TIME and every OLMo stage run uncached; G-ID runs both paths from
``guard.gid_paths()`` -- the only place a cached True originates; the Qwen
qualification stage and the Qwen campaign take ``guard.cached_path_admitted(unit,
stage, backend_identifier=...)`` for the backend asking. ``guard.check_call_sites``
must return [] over this file.

STAGE END (m:271). Binomial bars are evaluated ONCE on the realised n over the
sham-template sessions only (``bars.stage_end_eval``); contrast sessions' forced-round
counts are reported beside, their free-round events withheld (``readrule.stage_report``).
The OLMo G-TIME pause (m:302) is evaluated at the OLMo time stage only. Every gate
stage persists its end in its checkpoint (``stage_end``), so the next stage can read it
and no pod change lifts it. ORDER (finding R1), at EVERY finish -- PASS, STOP, PAUSE,
G-ID's verdicts, a G-VER stop, a campaign's STOP / PAUSE / terminal state: the end is
computed in memory and every output built from its persisted form and asserted
(pick-free, persistable) before any write; FIRST the end is written as ``end_pending``
together with every session (the fired one recorded; a G-VER record quarantined in the
pending stop); THEN the report, the reads, the adjudication excerpt (or the removal of a
stale one) and (at G-ID) the artifact are written; THEN the end is persisted and
end_pending cleared (``resume.persist_end``). A checkpoint carrying end_pending is
RE-FINISH-ONLY on any pod and at any invocation: nothing launches, nothing is set
aside, the outputs are re-derived from the checkpoint byte-identically (an identical
G-ID artifact is accepted, a differing one refused) and the end is persisted. An end on
disk therefore always has its outputs, and an announced STOP or PAUSE is never lifted by
a kill in the window.

BLINDING (m:318; build design §0 rule 5). Stdout carries only the PROVENANCE line,
``readrule.session_line`` per session, the bars' blinded messages, the stage's STOP /
PAUSE / PASS line (with its path) and file paths. A hair trigger on a contrast
session's FREE phase is announced by phase alone (m:318 exception (1)), and so is every
later refusal of the stopped stage (resume's blinded stop words): ``readrule.strip_contrast``
and ``stage_report`` withhold it, so this module announces the stop itself. At every
G-TIME stage the contrast session's forced rounds reach stdout and the report as
ruling (h)'s counts only -- rounds generated and excluded yes/no, no class and no round
position (the seat's ruling (h), 2026-10-06; ``_assert_time_counts_only``); the reads
carry m:280's mandated forced-round bytes with {phase, ri, n, text} per round and no
structured class, claim or domain field (Code's extension of (h) to the read,
readrule's TIME_ROUND_KEEP PIN); a forced hair trigger's or G-VER failure's STOP is the
declared m:318 exception (1) carve-out. The
pick-bearing checkpoint and the adjudication excerpt are written only under ``ckpt/``
(marked -diff in .gitattributes). Reports and reads carry no contrast pick; G-ID's
reads and the sham first-pick shares carry sham picks under m:318's exceptions (2)-(4).
Reports carry no adjudication or PI text and no time that includes a contrast session.

ADJUDICATION (m:271: "An adjudication read ... is confined to the fired round(s) and
the harness lines around them; ... the pick it reveals is recorded as seen"). On every
STOP or PAUSE the stage writes ``ckpt/{stem}_adjudication.json`` beside its checkpoint,
holding only what the adjudication needs (``adjudication_path``); it is never printed.

OUTPUTS (PIN, declared below at ``out_paths`` / ``for_checkpoint``), under ``out_root``
(default REPO/data/m; the only root a non-stub adapter writes to), every name derived
from the resolved checkpoint's stem (default ``{unit}_{stage}``): ``ckpt/{stem}.json``
(resume.py's atomic writes; pick-bearing), ``ckpt/{stem}_adjudication.json``
(pick-bearing; a STOP or PAUSE only), ``reports/{stem}_report.json`` (no contrast pick),
``reports/{stem}_reads.json`` (the pre-VERDICTS reads of §3; G-ID's sham-only sessions
in full, §4 exception (4)), and G-ID's artifact at ``guard.gid_artifact_path(unit)``. A
run on the self-test stub is refused anywhere under REPO/data/m
(``resume.refuse_canonical_out``).
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

from . import bars as _bars
from . import banner as _banner
from . import corr as _corr
from . import guard, keys, readrule
from . import resume as _resume
from . import scaffold as _sc
from . import schedule as _schedule
from . import verify as _verify
from .runner_olmo import olmo_startup, run_session_olmo
from .runner_qwen import qwen_startup, run_session_qwen

REPO = Path(__file__).resolve().parents[2]
DEFAULT_OUT = REPO / "data" / "m"
# PIN (Code, declared at LOCK v0.1; findings R3, R11): the proposal a stage reads
# (banner.spec_problems, the gate line, the licence) is the repo-relative file
# identity_extra's ``proposal_file`` names -- REQUIRED on a non-stub run, never
# hard-coded there; this default serves stub runs only (the self-test's document).
PROPOSAL_PATH = REPO / "PROPOSAL-m-gating-campaign-v1_11.md"
PROPOSAL_REL = PROPOSAL_PATH.relative_to(REPO).as_posix()
CLAUDE_MD_PATH = REPO / "CLAUDE.md"
# PIN (Code, declared at LOCK v0.1): the analyzer whose hash m:267's gate line logs is
# G-ANL-F0's `m_analyze.py` (m:278), at the k1/b3 analyzers' home (scripts/).
ANALYZER_PATH = REPO / "scripts" / "m_analyze.py"
REPORT_SCHEMA = "m-stage-report-v1"
READS_SCHEMA = "m-stage-reads-v1"
GID_SCHEMA = "m-gid-v1"
ADJ_SCHEMA = "m-adjudication-v1"
GATES = ("time", "qual")
LOOK_EVERY = _resume.LOOK_EVERY
# PIN (Code, declared at LOCK v0.1): a test double is recognised by the precedent's own
# provenance tag (scripts/box_selftest_stub.py STUB_TAG "SELFTEST-STUB -- NOT A MODEL"),
# and every output path of a stage run on it goes through resume.refuse_canonical_out.
STUB_MARK = "SELFTEST-STUB"
WITHHELD_CLASS = "withheld to the unit's VERDICTS entry or NOT-RUN record (m:318 exception (1))"
TERMINAL = ("COMPLETE", "CAP", "PI-STOP")

# PIN (Code, declared at LOCK v0.1): process exit codes a stage driver returns per
# status -- 0 for PASS (gate stage), COMPLETE, CAP and PI-STOP (campaign, all terminal
# by m:247); non-zero for every outcome that needs the seat or the PI.
EXIT_CODES = {"PASS": 0, "COMPLETE": 0, "CAP": 0, "PI-STOP": 0, "PAUSE": 3, "STOP": 4,
              "FAIL": 5, "NOT-DETERMINED": 6}

_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_HEX16 = re.compile(r"^[0-9a-f]{16}$")


def exit_code(status: str) -> int:
    if status not in EXIT_CODES:
        raise ValueError(f"unknown stage status {status!r}")
    return EXIT_CODES[status]


# --- units, names, paths --------------------------------------------------------
def _check_unit(unit: str, substrate: str | None = None) -> str:
    if isinstance(unit, str) and unit.startswith("Q-F3"):
        raise NotImplementedError("Q-F3: no F3 code in step 4 (§8 step 19 builds it)")
    keys.templates(unit)                          # ValueError: unknown unit, OLMo-base
    sub = "qwen" if unit == "Q-F0" else "olmo"
    if substrate is not None and substrate != sub:
        raise ValueError(f"unit {unit!r} runs on the {sub} substrate, not {substrate!r}")
    return sub


def _ckpt_name(unit: str) -> str:
    return unit.split("-", 1)[1]


def stage_name(unit: str, stage: str) -> str:
    """The spec's stage names (m:280-283, m:302, m:330)."""
    sub = _check_unit(unit)
    if sub == "qwen":
        names = {"time": "G-TIME-F0", "id": "G-ID-F0m", "qual": "G-F0m-Qwen",
                 "campaign": "campaign-Q-F0"}
    else:
        c = _ckpt_name(unit)
        names = {"time": f"G-TIME-OLMo-{c}", "qual": f"G-F0m-OLMo-{c}",
                 "campaign": f"campaign-OLMo-{c}"}
    if stage not in names:
        raise ValueError(f"{stage!r} is not a stage of {unit!r} (no G-ID on OLMo, m:267)")
    return names[stage]


def out_paths(unit: str, stage: str, out_root: str | os.PathLike = DEFAULT_OUT) -> dict[str, Path]:
    """Every path a stage writes or reads.

    PIN (Code, declared at LOCK v0.1): under out_root (default REPO/data/m) --
    schedules/ (read only), ckpt/{unit}_{stage}.json (the default checkpoint,
    pick-bearing; its adjudication excerpt beside it, ``adjudication_path``),
    reports/{unit}_{stage}_report.json and reports/{unit}_{stage}_reads.json (no
    contrast pick: G-ID's reads and the sham first-pick shares carry sham picks under
    m:318's exceptions (2)-(4)) -- the report and reads of the DEFAULT checkpoint; a
    stage names them after its resolved checkpoint (``for_checkpoint``); the G-ID
    artifact lives where the licence reads it, guard.gid_artifact_path(unit).
    """
    stage_name(unit, stage)
    root = Path(out_root)
    return {"root": root, "schedules": root / "schedules",
            "ckpt": root / "ckpt" / f"{unit}_{stage}.json",
            "report": root / "reports" / f"{unit}_{stage}_report.json",
            "reads": root / "reports" / f"{unit}_{stage}_reads.json"}


def for_checkpoint(paths: Mapping[str, Path], cpath: Path) -> dict[str, Path]:
    """The stage's paths with its report and reads named after the RESOLVED checkpoint.

    PIN (Code, declared at LOCK v0.1; finding R10): reports/{checkpoint stem}_report.json
    and reports/{checkpoint stem}_reads.json, as ``adjudication_path`` names the excerpt
    -- the default checkpoint keeps {unit}_{stage}'s names; a campaign or gate stage
    restarted at a new checkpoint path writes its own report and never overwrites the
    one the old checkpoint's run wrote.
    """
    rd = Path(paths["root"]) / "reports"
    stem = Path(cpath).stem
    return {**paths, "ckpt": Path(cpath), "report": rd / f"{stem}_report.json",
            "reads": rd / f"{stem}_reads.json"}


def checkpoint_path(ckpt_path: str | os.PathLike | None, paths: Mapping[str, Path]) -> Path:
    """The checkpoint a stage writes: ``ckpt_path`` or the default, RESOLVED.

    PIN (Code, declared at LOCK v0.1): every checkpoint -- a default one, an operator's
    restart path, and therefore every pod-change set-aside beside it -- resolves to
    ``<out_root>/ckpt/<name>.json``, the directory the -diff rule covers (m:318: a
    pick-bearing file is never rendered by git diff); anything else is a SystemExit. The
    resolved path must name no roster word (whole word, case-insensitive): the report
    carries the checkpoint's name and stdout its path, so a roster word there would
    reach a pick-free artifact after the stage had run (finding N10); a name ending
    ``_adjudication`` is reserved for the excerpt beside a checkpoint.
    """
    cp = Path(ckpt_path) if ckpt_path is not None else Path(paths["ckpt"])
    want = (Path(paths["root"]) / "ckpt").resolve()
    r = cp.expanduser().resolve()
    if r.parent != want or r.suffix != ".json" or not r.stem:
        raise SystemExit(f"CHECKPOINT PATH REFUSED: {cp} resolves to {r}; a checkpoint is "
                         f"<out_root>/ckpt/<name>.json ({want}/...), under the -diff rule (m:318)")
    if _ROSTER_RX.search(str(r)):
        raise SystemExit(f"CHECKPOINT PATH REFUSED: {r} names a roster word; the report carries "
                         f"the checkpoint's name and stdout its path (m:318) -- choose another name")
    if r.stem.endswith("_adjudication"):
        raise SystemExit(f"CHECKPOINT PATH REFUSED: {r.name} -- a name ending '_adjudication' is the "
                         f"adjudication excerpt beside a checkpoint")
    return r


def adjudication_path(cpath: Path) -> Path:
    """The confined adjudication excerpt beside a checkpoint (m:271).

    PIN (Code, declared at LOCK v0.1): ``{checkpoint stem}_adjudication.json`` in the
    checkpoint's directory -- ckpt/{unit}_{stage}_adjudication.json for a default
    checkpoint -- so it is tracked and -diff exactly as the checkpoint is.
    """
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
            _resume.refuse_canonical_out(p)


def _out_root_guard(adapter, root: str | os.PathLike) -> None:
    """A non-stub adapter writes under REPO/data/m only.

    PIN (Code, declared at LOCK v0.1): on any adapter that is not the self-test stub,
    ``out_root`` must resolve to DEFAULT_OUT (REPO/data/m) -- the tracked, -diff layout
    .gitignore and .gitattributes declare -- else SystemExit before anything is written
    (ledger 27: a measurement lands where the repo records it, finding 14).
    """
    if _is_stub(adapter):
        return
    r, want = Path(root).expanduser().resolve(), Path(DEFAULT_OUT).resolve()
    if r != want:
        raise SystemExit(f"OUT ROOT REFUSED: a non-stub run writes under {want} only; {root} resolves "
                         f"to {r} (ledger 27; the -diff layout of .gitattributes)")


def _start_provenance(adapter, name: str) -> dict:
    """``adapter.provenance()`` verbatim (JSON-native), checked before anything is written.

    PIN (Code, declared at LOCK v0.1): a provenance record that is not JSON-native, or
    that names a roster word (it is copied into the report, which must name none), is a
    SystemExit at stage start rather than a late refusal after the stage has run.
    """
    try:
        rec = _resume.provenance_record(adapter.provenance())
    except (TypeError, ValueError) as e:
        raise SystemExit(f"PROVENANCE REFUSED ({name}): {e}")
    if _ROSTER_RX.search(json.dumps(rec, sort_keys=True, ensure_ascii=False)):
        raise SystemExit(f"PROVENANCE REFUSED ({name}): the adapter's provenance names a roster word; "
                         f"the report copies it (m:318)")
    return rec


def _provenance_line(entry: Mapping) -> str:
    return "PROVENANCE: " + json.dumps({"record": entry["record"], "stamp": entry["stamp"]},
                                       sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _append_provenance(ckpt: dict, rec: Mapping) -> None:
    # PIN (Code, declared at LOCK v0.1): the PROVENANCE line is printed once per
    # invocation, when its entry is appended (after the checkpoint is loaded, before the
    # first write): the compact sort-keyed JSON of {record, stamp}.
    entry = _resume.append_provenance(ckpt, rec)
    print(_provenance_line(entry), flush=True)


def _require_pod(unit: str) -> None:
    # PIN (Code, declared at LOCK v0.1): every OLMo stage, gate or campaign, starts and
    # resumes only with $RUNPOD_POD_ID set -- the backend identifier cannot tell two
    # boxes of one class apart (m:267), so without a pod id a gate stage's pod-change
    # detector is blind and a splice across boxes would pass.
    if _check_unit(unit) == "olmo" and _resume.pod_id() is None:
        raise SystemExit(f"POD ID ABSENT: an OLMo stage of {unit} starts or resumes only with "
                         f"${_resume.POD_ENV} set (m:251, m:267); refusing")


# --- run-time known answers, laptop preflight -------------------------------------
def startup_problems(proposal_path: str | os.PathLike = PROPOSAL_PATH) -> list[str]:
    """The run-time known answers every stage runs before any session; [] = clean.

    numpy's stream (keys: f1's f|CORR|0 permutation, m:159), the banner bytes against
    §2.5's literals parsed from ``proposal_path`` -- the file identity_extra's
    proposal_file names (m:253-258; finding R11) -- and roster admissibility of the
    clean pool, golds, declared harness strings and e2a's wrapper (rule 18, m:258).
    """
    probs = [f"keys: {p}" for p in keys.stream_known_answer()]
    probs += [f"banner: {p}" for p in _banner.spec_problems(proposal_path=Path(proposal_path))]
    probs += [f"corr: {p}" for p in _corr.startup_hygiene()]
    return probs


def _startup_checks(name: str, proposal_path: str | os.PathLike) -> None:
    probs = startup_problems(proposal_path)
    if probs:
        raise SystemExit(f"STARTUP CHECKS FAIL ({name}): {probs[:5]} -- no session runs "
                         f"(m:159, m:258, rule 18)")


def _proposal_path(extra: Mapping[str, Any]) -> Path:
    return REPO / extra["proposal_file"]


def _sha16_file(p: Path) -> str | None:
    try:
        return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:16]
    except OSError:
        return None


# --- read-only git (trap 32; k1_stage1.proposal_gate's purpose, object reads only) -----
_HEXSHA = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
_REGULAR_MODES = ("100644", "100755")


def _git(*args: str, repo: str | os.PathLike = REPO, binary: bool = False) -> subprocess.CompletedProcess:
    """A READ-ONLY git query: object and ref reads only -- ``cat-file``, ``ls-tree``,
    ``rev-parse`` (finding R4). Never ``git diff`` or ``git status``: both refresh the
    index's stat cache and so rewrite .git/index (GIT_OPTIONAL_LOCKS=0 does not stop it)."""
    return subprocess.run(["git", *args], capture_output=True, text=not binary, cwd=repo)


def _git_head(repo: str | os.PathLike = REPO) -> str:
    """HEAD's commit from ``git rev-parse --verify HEAD`` (read only), or "unknown".

    PIN (Code, declared at LOCK v0.1; finding R9): "unknown" -- git unavailable, no HEAD,
    a non-hex answer -- is a refusal on every non-stub run (the licence; and the gate
    line on Qwen): m:267's gate line logs HEAD, and the licence hashes HEAD's blobs.
    """
    try:
        r = _git("rev-parse", "--verify", "HEAD", repo=repo)
    except OSError:
        return "unknown"
    out = (r.stdout or "").strip() if r.returncode == 0 else ""
    return out if _HEXSHA.match(out) else "unknown"


def _committed(rel: str, repo: str | os.PathLike = REPO) -> tuple[list[str], bytes | None]:
    """(problems, the file's bytes) for a file the licence names: [] and the bytes when it
    is COMMITTED at HEAD as a regular blob and the working tree holds exactly that blob.

    PIN (Code, declared at LOCK v0.1; finding R4): ``git cat-file -e HEAD:<rel>`` (HEAD
    has the path), ``git ls-tree -z HEAD -- <rel>`` (exactly one entry, mode 100644 /
    100755 type blob -- 120000, a symlink, is refused: git commits the link text, not the
    bytes it points at), ``git cat-file blob HEAD:<rel>`` (the committed bytes); the
    working-tree path must be a regular file, no symlink anywhere on it, whose bytes are
    HEAD's blob byte for byte. Hashing the committed blob rather than trusting a clean
    ``git diff`` defeats a tracked symlink and an assume-unchanged / skip-worktree file,
    and no index is written. Any git error is a problem naming git's first stderr line.
    """
    def gerr(r) -> str:
        e = (r.stderr or b"")
        e = e.decode("utf-8", "replace") if isinstance(e, bytes) else e
        return (e.strip().splitlines() or [""])[0][:120]
    try:
        r = _git("cat-file", "-e", f"HEAD:{rel}", repo=repo)
        if r.returncode != 0:
            return [f"{rel}: not committed at HEAD (git: {gerr(r)})"], None
        lt = _git("ls-tree", "-z", "HEAD", "--", rel, repo=repo)
        ents = [e for e in (lt.stdout or "").split("\0") if e]
        if lt.returncode != 0 or len(ents) != 1 or "\t" not in ents[0]:
            return [f"{rel}: HEAD's tree entry is not one file (git: {gerr(lt)})"], None
        meta, epath = ents[0].split("\t", 1)
        fields = meta.split()
        mode, typ = (fields[0], fields[1]) if len(fields) >= 2 else ("?", "?")
        if epath != rel:
            return [f"{rel}: HEAD's tree entry names {epath!r}"], None
        if mode == "120000":
            return [f"{rel}: a symlink at HEAD -- its target's bytes are in no commit"], None
        if typ != "blob" or mode not in _REGULAR_MODES:
            return [f"{rel}: not a regular file at HEAD ({mode} {typ})"], None
        blob = _git("cat-file", "blob", f"HEAD:{rel}", repo=repo, binary=True)
        if blob.returncode != 0 or not isinstance(blob.stdout, bytes):
            return [f"{rel}: HEAD's blob unreadable (git: {gerr(blob)})"], None
    except OSError as e:
        return [f"{rel}: git unavailable ({type(e).__name__})"], None
    wt = Path(repo) / rel
    try:
        if wt.is_symlink() or wt.resolve() != Path(repo).resolve() / rel or not wt.is_file():
            return [f"{rel}: the working-tree path is not a regular file at that path (a symlink "
                    f"on it, or no file)"], None
        data = wt.read_bytes()
    except OSError:
        return [f"{rel}: unreadable in the working tree"], None
    if data != blob.stdout:
        return [f"{rel}: working-tree bytes are not HEAD's blob (uncommitted edits)"], None
    return [], data


def gate_line(name: str, proposal_path: str | os.PathLike = PROPOSAL_PATH) -> tuple[str, list[str]]:
    """m:267's gate line (proposal, CLAUDE.md, analyzer and HEAD hashes) and its problems.

    PIN (Code, declared at LOCK v0.1): file hashes are sha256 prefixes (16 hex) of the
    files' bytes -- what a lock pins -- the proposal being the file identity_extra names
    (finding R11), and HEAD is ``git rev-parse --verify HEAD`` (finding R9); a missing
    proposal, CLAUDE.md or analyzer, or HEAD "unknown", is a problem (the line cannot be
    logged in full).
    """
    probs: list[str] = []
    hs = {}
    for k, p in (("proposal", Path(proposal_path)), ("CLAUDE.md", CLAUDE_MD_PATH),
                 ("analyzer", ANALYZER_PATH)):
        h = _sha16_file(p)
        if h is None:
            probs.append(f"GATE LINE: {k} absent at {p}")
        hs[k] = h or "ABSENT"
    head = _git_head()
    if head == "unknown":
        probs.append("GATE LINE: HEAD unknown (git rev-parse --verify HEAD failed)")
    line = (f"GATE {name}: proposal {_rel(Path(proposal_path), REPO)} {hs['proposal']}, CLAUDE.md "
            f"{hs['CLAUDE.md']}, analyzer {_rel(ANALYZER_PATH, REPO)} {hs['analyzer']}, HEAD {head}")
    return line, probs


def _repo_rel(p: Path) -> str | None:
    try:
        return Path(p).resolve().relative_to(REPO.resolve()).as_posix()
    except (ValueError, OSError):
        return None


def _laptop_preflight(adapter, unit: str, name: str, extra: Mapping[str, Any]) -> bool:
    """m:267's laptop checklist before a detached Qwen run; True when it ran.

    PIN (Code, declared at LOCK v0.1): run by every Qwen stage driver at its start for a
    non-stub adapter (power, one model process, disk headroom: guard.preflight_laptop),
    then the gate line's files: CLAUDE.md and the analyzer COMMITTED at HEAD with the
    working tree's bytes HEAD's blob (``_committed``, k1_stage1.proposal_gate's trap-32
    rule; findings R8, R9 -- an analyzer outside the repository is refused); any problem
    a SystemExit before any session, then the gate line printed. A run on the self-test
    stub (STUB_MARK) and every OLMo stage (the box's respawn protocol governs there)
    skip it. The analyzer's hash against identity_extra's ``analyzer_sha256`` is the
    licence's (every non-stub run).
    """
    if _check_unit(unit) != "qwen" or _is_stub(adapter):
        return False
    probs = list(guard.preflight_laptop())
    line, gprobs = gate_line(name, _proposal_path(extra))
    probs += gprobs
    for what, path in (("CLAUDE.md", CLAUDE_MD_PATH), ("analyzer", ANALYZER_PATH)):
        rel = _repo_rel(path)
        if rel is None:
            probs.append(f"GATE LINE: {what} {path} lies outside the repository")
            continue
        probs += [f"GATE LINE: {what} {x}" for x in _committed(rel)[0]]
    if probs:
        raise SystemExit(f"LAPTOP PREFLIGHT REFUSES {name}: {probs} (m:267's checklist)")
    print(line, flush=True)
    return True


# --- the licence by file (trap 32; findings N2, 39, R4, R9, R11) --------------------------
def licence_problems(extra: Mapping[str, Any], *, repo: str | os.PathLike = REPO) -> list[str]:
    """The licence by file for a non-stub stage; [] = licensed.

    (a) HEAD is known (``git rev-parse``; finding R9); (b) identity_extra's
    ``proposal_file`` -- the file banner.spec_problems and the gate line read -- is
    committed at HEAD with the working tree's bytes, and its sha256 is
    ``proposal_sha256`` (finding N2: the document read is the document the identity
    names); (c) ``lock_file`` likewise against ``lock_sha256`` (finding 39); (d) the
    analyzer's bytes hash to identity_extra's ``analyzer_sha256`` (finding R8); (e) the
    package this process hashes, ``resume.package_sha256()`` computed here, is
    identity_extra's ``package_sha256``; (f) the committed lock's bytes -- those (c) read
    -- name both 64-hex strings verbatim (the analyzer's PIN-14 precedent). (d)-(f) are the
    seat's D2 (2026-10-10): both keys are required on a non-stub run, so an absent or
    malformed one is a problem here, never a KeyError or a silent pass. git runs
    read-only: object reads only (``_committed``), never diff.
    """
    probs: list[str] = []
    if _git_head(repo) == "unknown":
        probs.append("HEAD unknown (git rev-parse --verify HEAD failed): nothing is licensed "
                     "without the commit the files are read at")
    lock_data: bytes | None = None
    for what, rel, want in (("proposal", extra.get("proposal_file"), extra.get("proposal_sha256")),
                            ("lock", extra.get("lock_file"), extra.get("lock_sha256"))):
        if rel is None:
            probs.append(f"{what}: no file named (identity_extra {what}_file is required on a "
                         f"non-stub run)")
            continue
        cp, data = _committed(rel, repo)
        probs += [f"{what} {x}" for x in cp]
        if data is None:
            continue
        if what == "lock":
            lock_data = data
        sha = hashlib.sha256(data).hexdigest()
        if sha != want:
            probs.append(f"{what} {rel}: sha256 {sha[:16]}... is not identity_extra's "
                         f"{str(want)[:16]}...")
    # PIN (Code, declared at LOCK v0.1; the seat's D2, 2026-10-10): "analyzer_sha256 and
    # package_sha256 are required in the stages' identity_extra on non-stub runs, and the
    # package hash is checked against the lock at stage start." (d) the analyzer's bytes
    # against analyzer_sha256; (e) resume.package_sha256() -- the m package's sources as this
    # process hashes them, read at check time -- against package_sha256; (f) the lock's
    # committed bytes (decoded UTF-8, errors replaced, as the analyzer reads them) contain
    # both 64-hex strings verbatim. A key absent or not 64 lower-case hex is one problem
    # naming it; (f) is checked only for a well-formed key and a committed lock (an absent
    # key or an uncommitted lock is already its own problem).
    have: dict[str, str] = {}
    for k in ("analyzer_sha256", "package_sha256"):
        v = extra.get(k)
        if type(v) is str and _HEX64.match(v):
            have[k] = v
        else:
            probs.append(f"{k}: identity_extra carries none (or not 64 lower-case hex: {v!r}); it is "
                         f"required on a non-stub run (the seat's D2)")
    if "analyzer_sha256" in have:
        try:
            got = hashlib.sha256(Path(ANALYZER_PATH).read_bytes()).hexdigest()
        except OSError:
            got = None
        if got != have["analyzer_sha256"]:
            probs.append(f"analyzer {_rel(ANALYZER_PATH, REPO)}: sha256 "
                         f"{(got or 'ABSENT')[:16]}... is not identity_extra's analyzer_sha256 "
                         f"{have['analyzer_sha256'][:16]}...")
    if "package_sha256" in have:
        got_pkg = _resume.package_sha256()
        if got_pkg != have["package_sha256"]:
            probs.append(f"package valence_core/m: sha256 {got_pkg[:16]}... (resume.package_sha256, "
                         f"computed now) is not identity_extra's package_sha256 "
                         f"{have['package_sha256'][:16]}... (the seat's D2)")
    if lock_data is not None:
        ltext = lock_data.decode("utf-8", "replace")
        for k, v in have.items():
            if v not in ltext:
                probs.append(f"lock {extra.get('lock_file')}: its committed text does not name "
                             f"identity_extra's {k} {v[:16]}... (the seat's D2; the analyzer's PIN-14)")
    return probs


def _licence(adapter, extra: Mapping[str, Any], name: str) -> None:
    """Refuse a non-stub stage whose proposal or lock is not the committed file it names, or
    whose analyzer or package is not the one the identity and the lock name (the seat's D2);
    licensed, print the LICENCE line, each clause scoped to what was checked."""
    if _is_stub(adapter):
        return
    probs = licence_problems(extra)
    if probs:
        raise SystemExit(f"LICENCE REFUSED ({name}): {probs} -- nothing runs before the document "
                         f"and the lock are committed with the hashes the identity names (trap 32)")
    # PIN (Code, declared at LOCK v0.1; the seat's D2, 2026-10-10): the LICENCE line names the
    # package's sha16 after the analyzer's -- both always present here (licence_problems
    # refuses a non-stub run without them) -- and each clause claims only what licence_problems
    # checked: the proposal and the lock "committed at HEAD, working tree identical" (b), (c);
    # the analyzer and the package as the hashes identity_extra and the lock's committed text
    # name, hashed from the working tree at stage start (d)-(f). No stage-start check reads
    # the analyzer or valence_core/m/*.py from git (the Qwen laptop preflight checks the
    # analyzer's commit, _laptop_preflight), so the line never says they are committed.
    print(f"LICENCE {name}: proposal {extra['proposal_file']} {extra['proposal_sha256'][:16]}, lock "
          f"{extra['lock_file']} {extra['lock_sha256'][:16]}: committed at HEAD {_git_head()}, working "
          f"tree identical; analyzer {extra['analyzer_sha256'][:16]} and package "
          f"{extra['package_sha256'][:16]}: the hashes identity_extra and the lock name, hashed from "
          f"the working tree at stage start", flush=True)


# --- the prior stage --------------------------------------------------------------
# PIN (Code, declared at LOCK v0.1): the stage order of §8 and m:280-302 is enforced on
# the prior stage's PERSISTED end (stage_end): G-ID-F0m needs G-TIME-F0 PASS; G-F0m-Qwen
# needs G-TIME-F0 PASS and the unit's G-ID artifact on disk (any verdict -- a FAIL or
# NOT-DETERMINED sends Q-F0 uncached, m:281); G-F0m-OLMo needs G-TIME-OLMo PASS, or its
# PAUSE with the seat's adjudication named (recorded in this stage's checkpoint only,
# m:302); a campaign needs its unit's qualification stage PASS (m:283, m:302).
PRIOR_STAGE = {"id": "time", "qual": "time", "campaign": "qual"}


def written_on_stub(ck: Mapping) -> bool:
    """Was this checkpoint written (in any part) by the self-test stub, or is that
    undeterminable? PIN (Code, declared at LOCK v0.1): a checkpoint whose provenance list
    is absent or empty, or any of whose entries carries STUB_MARK in its adapter or
    apparatus, counts as written on the stub ("an undetermined licence is not a granted
    one", e2d_tstep_check.py:58-87)."""
    prov = ck.get("provenance")
    if not isinstance(prov, list) or not prov:
        return True
    return any(not isinstance(e, Mapping) or not isinstance(e.get("record"), Mapping)
               or any(STUB_MARK in str(e["record"].get(k, "")) for k in ("adapter", "apparatus"))
               for e in prov)


def accepted_proposals(proposal_sha256: str | None,
                       prior_proposal_sha256s: Sequence[str] = ()) -> frozenset[str] | None:
    """The proposal hashes a prior stage or the G-ID artifact may carry: this run's, plus
    those its governing lock re-adopts. None = no check (a direct call without a run).

    PIN (Code, declared at LOCK v0.1; finding R11; the seat's ruling (n), 2026-10-06,
    routed by the PI): ``prior_proposal_sha256s`` is approved "on one condition the lock
    states: a stage is re-adopted only if the proposal sections governing it are
    byte-identical between the two versions, which Code checks and records at the lock."
    The condition binds at the LOCK, not here: the lock that names an earlier proposal's
    sha256 in this list names, for each stage it re-adopts under it, the governing
    sections as (start marker, end marker) spans; Code runs
    ``governing_sections_identical(earlier, current, spans)`` on the two committed
    proposal files and records its result -- every span's two sha256 and the verdict --
    in the lock. The list is per RUN, not per stage: one listed proposal licenses every
    prior artifact the run checks under it (at the Qwen qualification, the G-TIME prior
    checkpoint and the G-ID artifact; at the campaign, the qualification prior and the
    G-ID artifact). So the lock lists an earlier proposal only when the check passes for
    EVERY stage whose artifact the run accepts under that list, each stage's spans
    recorded; if any of them differs, the proposal is not listed, and the stages run under
    it are not re-adopted. At run time a stage accepts exactly the list the identity
    carries, recorded in its checkpoint's licence (``_record_licence``); it does not
    re-derive the condition.
    """
    if proposal_sha256 is None:
        return None
    return frozenset((proposal_sha256, *prior_proposal_sha256s))


def governing_sections_identical(old_path: str | os.PathLike, new_path: str | os.PathLike,
                                 spans: Sequence[Sequence[str]]) -> dict:
    """Ruling (n)'s check at a lock: are the proposal sections governing a re-adopted
    stage byte-identical between the two proposal versions?

    ``spans`` is a non-empty list of (start_marker, end_marker) strings. Each marker must
    occur exactly once in each file (overlapping occurrences counted) and each end marker
    after its start marker in both files, else ValueError (refused, never a verdict). A
    span is the bytes from its start marker, inclusive, to its end marker, exclusive.
    Returns {"identical": all spans identical, "old_file", "new_file" (the paths as
    given), "sha256_old_file", "sha256_new_file" (the two whole files), "spans": [{"start",
    "end", "sha256_old", "sha256_new", "identical"}]} in the order given.

    PIN (Code, declared at LOCK v0.1; ruling (n)): markers are matched as UTF-8 bytes,
    exactly (no normalisation of whitespace, line endings or case); a marker that is
    empty, or not a str, refuses the check; the result is recorded at the lock verbatim.
    """
    def raw(p) -> bytes:
        try:
            return Path(p).read_bytes()
        except OSError as e:
            raise ValueError(f"governing_sections_identical: cannot read {p} ({type(e).__name__})")

    def count(hay: bytes, needle: bytes) -> int:
        n, at = 0, hay.find(needle)
        while at >= 0:
            n += 1
            at = hay.find(needle, at + 1)
        return n

    if isinstance(spans, (str, bytes)) or not isinstance(spans, Sequence) or not spans:
        raise ValueError("governing_sections_identical: spans must be a non-empty list of "
                         "(start_marker, end_marker) pairs")
    files = {"old": raw(old_path), "new": raw(new_path)}
    out: list[dict] = []
    for sp in spans:
        if (isinstance(sp, (str, bytes)) or not isinstance(sp, Sequence) or len(sp) != 2
                or not all(type(m) is str and m for m in sp)):
            raise ValueError(f"governing_sections_identical: a span is two non-empty marker strings, "
                             f"got {sp!r}")
        start, end = sp
        a_m, b_m = start.encode("utf-8"), end.encode("utf-8")
        shas: dict[str, str] = {}
        for which, body in files.items():
            for m, label in ((a_m, "start"), (b_m, "end")):
                c = count(body, m)
                if c != 1:
                    raise ValueError(f"governing_sections_identical: the {label} marker {m.decode()!r} "
                                     f"occurs {c} times in the {which} file (exactly once required)")
            a, b = body.find(a_m), body.find(b_m)
            if b < a + len(a_m):
                raise ValueError(f"governing_sections_identical: the end marker {end!r} does not "
                                 f"follow the start marker {start!r} in the {which} file")
            shas[which] = hashlib.sha256(body[a:b]).hexdigest()
        out.append({"start": start, "end": end, "sha256_old": shas["old"], "sha256_new": shas["new"],
                    "identical": shas["old"] == shas["new"]})
    return {"identical": all(s["identical"] for s in out), "old_file": str(old_path),
            "new_file": str(new_path),
            "sha256_old_file": hashlib.sha256(files["old"]).hexdigest(),
            "sha256_new_file": hashlib.sha256(files["new"]).hexdigest(), "spans": out}


def gid_artifact_problems(unit: str, *, accepted: frozenset[str] | None,
                          require_real: bool) -> list[str]:
    """The unit's G-ID artifact against this run's licence; [] = admissible (or absent).

    PIN (Code, declared at LOCK v0.1; finding R3): an artifact on disk licenses the
    qualification and sets the Qwen path (m:281-283, m:267) only when its
    identity.proposal_sha256 is this run's or one the governing lock re-adopts
    (``prior_proposal_sha256s``); on a non-stub run it must not be written on the stub
    (its ``provenance`` list, as ``written_on_stub`` reads a checkpoint's -- absent or
    empty counts as the stub). An unreadable artifact is a problem, never a pass.
    """
    p = guard.gid_artifact_path(unit)
    if not p.is_file():
        return []
    try:
        art = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError) as e:
        return [f"G-ID ARTIFACT UNREADABLE at {p} ({type(e).__name__})"]
    if not isinstance(art, dict):
        return [f"G-ID ARTIFACT UNREADABLE at {p} (not a JSON object)"]
    probs: list[str] = []
    ident = art.get("identity")
    got = ident.get("proposal_sha256") if isinstance(ident, Mapping) else None
    if accepted is not None and got not in accepted:
        probs.append(f"G-ID ARTIFACT UNDER ANOTHER PROPOSAL: {p} ran under proposal "
                     f"{str(got)[:16]}..., which is neither this run's nor one its lock re-adopts")
    if require_real and written_on_stub(art):
        probs.append(f"G-ID ARTIFACT ON THE STUB: {p} was written by the self-test stub (or its "
                     f"provenance cannot show otherwise); it licenses no run on a model")
    return probs


def prior_gate(unit: str, stage: str, prior_ckpt: str | os.PathLike | None,
               prior_adjudication: str | None = None, *, proposal_sha256: str | None = None,
               prior_proposal_sha256s: Sequence[str] = (), require_real: bool = False) -> dict:
    """The prior stage's licence for ``stage``, or SystemExit naming what is missing.

    ``proposal_sha256``: this run's; a prior (and, for the Qwen qualification, the G-ID
    artifact) under another proposal is refused unless its hash is in
    ``prior_proposal_sha256s`` -- the earlier proposals the governing lock re-adopts
    after an amendment (finding R11; approved by the seat's ruling (n) on the condition
    ``accepted_proposals``'s PIN states); a prior under an EARLIER LOCK is allowed -- the
    locks advance between stages, m:279-286. ``require_real``: this run is not on the
    stub, so a prior or artifact written on the stub (or whose provenance cannot show
    otherwise) is refused (finding N17).
    """
    sub = _check_unit(unit)
    name = stage_name(unit, stage)
    want = PRIOR_STAGE.get(stage)
    if want is None:
        if prior_ckpt is not None or prior_adjudication is not None:
            raise ValueError(f"{name} takes no prior stage (it is the first after its lock)")
        return {}
    if prior_ckpt is None:
        raise SystemExit(f"PRIOR STAGE REQUIRED: {name} runs only after {stage_name(unit, want)}; "
                         f"name its checkpoint (prior_ckpt)")
    p = Path(prior_ckpt)
    if not p.is_file():
        raise SystemExit(f"PRIOR STAGE ABSENT: no checkpoint at {p} ({stage_name(unit, want)} "
                         f"precedes {name})")
    ck = _resume.read_checkpoint(p)
    ident = ck["identity"]
    if ident.get("unit") != unit or ident.get("stage") != want:
        raise SystemExit(f"PRIOR STAGE MISMATCH: {p} is {ident.get('unit')}/{ident.get('stage')}, "
                         f"not {unit}/{want}")
    accepted = accepted_proposals(proposal_sha256, prior_proposal_sha256s)
    if accepted is not None and ident.get("proposal_sha256") not in accepted:
        raise SystemExit(f"PRIOR STAGE UNDER ANOTHER PROPOSAL: {p} ran under proposal "
                         f"{str(ident.get('proposal_sha256'))[:16]}..., this run under "
                         f"{proposal_sha256[:16]}... (its lock re-adopts "
                         f"{len(tuple(prior_proposal_sha256s))} earlier) -- {name} does not run on it")
    if require_real and written_on_stub(ck):
        raise SystemExit(f"PRIOR STAGE ON THE STUB: {p} was written by the self-test stub (or its "
                         f"provenance cannot show otherwise); it licenses no run on a model")
    end = ck.get("stage_end")
    status = end.get("status") if isinstance(end, Mapping) else None
    if status is None:
        raise SystemExit(f"PRIOR STAGE NOT ENDED: {stage_name(unit, want)} at {p} has no "
                         f"recorded end; {name} waits for it")
    adj = None
    if prior_adjudication is not None:
        if not (sub == "olmo" and stage == "qual" and status == "PAUSE"):
            raise SystemExit(f"PRIOR ADJUDICATION REFUSED: only an OLMo qualification after a "
                             f"G-TIME-OLMo PAUSE takes one (prior status {status})")
        if not (isinstance(prior_adjudication, str) and prior_adjudication.strip()):
            raise SystemExit("PRIOR ADJUDICATION REFUSED: empty text")
        adj = prior_adjudication.strip()
    ok = status == "PASS" or (status == "PAUSE" and adj is not None)
    if not ok:
        raise SystemExit(f"PRIOR STAGE {status}: {stage_name(unit, want)} ended {status} at {p}; "
                         f"{name} does not run until the seat re-specifies"
                         + (" (or names its adjudication of the pause)"
                            if status == "PAUSE" and sub == "olmo" and stage == "qual" else "")
                         + " (m:280-283, m:302)")
    if sub == "qwen" and stage == "qual":
        if not guard.gid_artifact_path(unit).is_file():
            raise SystemExit(f"G-ID ARTIFACT ABSENT: {name} runs after G-ID-F0m's artifact exists "
                             f"(any verdict; m:281-283) -- none at {guard.gid_artifact_path(unit)}")
        aprobs = gid_artifact_problems(unit, accepted=accepted, require_real=require_real)
        if aprobs:
            raise SystemExit(f"{aprobs[0]} -- {name} does not run on it" + (
                f" (also: {aprobs[1:]})" if aprobs[1:] else ""))
    return {"checkpoint": _rel(p, REPO), "stage": want, "status": status, "adjudication": adj}


LICENCE_KEYS = ("analyzer_sha256", "lock_file", "package_sha256", "prior_proposal_sha256s",
                "proposal_file")


def _record_licence(ckpt: dict, extra: Mapping[str, Any], where: Path) -> None:
    # PIN (Code, declared at LOCK v0.1; findings R8, R11; the seat's D2, 2026-10-10): the
    # files, hashes and earlier-proposal list that licensed the stage -- proposal_file,
    # lock_file, prior_proposal_sha256s (the governing lock's re-adoption list),
    # analyzer_sha256 and package_sha256 -- are recorded in the checkpoint (``licence``) at
    # its first write; a resume or a re-finish offering different ones is refused, as a
    # different prior is.
    want = {k: copy.deepcopy(extra.get(k)) for k in LICENCE_KEYS}
    have = ckpt.get("licence")
    if have is None:
        ckpt["licence"] = want
    elif not _resume.same_json(have, want):
        raise SystemExit(f"CHECKPOINT MISMATCH: {where} was licensed by {have}; this run offers "
                         f"{want} -- refusing")


def _record_prior(ckpt: dict, prior: Mapping, where: Path) -> None:
    # PIN (Code, declared at LOCK v0.1): the prior licence is recorded at the first write
    # (the adjudication text, if any, in the checkpoint only); a resume re-checks it and
    # refuses a different prior status or adjudication.
    if not prior:
        return
    have = ckpt.get("prior")
    if have is None:
        ckpt["prior"] = dict(prior)
    elif (have.get("status"), have.get("adjudication")) != (prior["status"], prior["adjudication"]):
        raise SystemExit(f"CHECKPOINT MISMATCH: {where} recorded the prior stage as "
                         f"{have.get('status')} / adjudication {'named' if have.get('adjudication') else 'none'}; "
                         f"this run offers {prior['status']} / "
                         f"{'named' if prior['adjudication'] else 'none'} (or a different text)")


# --- committed schedules --------------------------------------------------------
def load_committed(unit: str, wanted: Sequence[tuple[str, str]],
                   sched_dir: str | os.PathLike) -> dict[str, dict]:
    """The committed schedule files a stage runs from (m:159, m:267): the directory
    verified clean (schedule.verify_schedule_dir), each file's bytes hashed against
    the manifest, its header and cells sha checked. ``wanted`` = [(kind, template)]
    with kind a gate word or "campaign". Returns {template: {name, sha256, n, cells}}."""
    d = Path(sched_dir)
    # PIN (Code, declared at LOCK v0.1): a schedule directory that is not clean (or a file
    # whose sha256 is not the manifest's) refuses the stage at its start, before any
    # session, as a SystemExit -- not a per-session schedule_mismatch.
    probs = _schedule.verify_schedule_dir(d)
    if probs:
        raise SystemExit(f"SCHEDULES NOT CLEAN at {d}: {probs[:3]} -- a stage runs only from the "
                         f"committed, verified schedule files; it never regenerates them (m:159)")
    try:
        manifest = json.loads((d / _schedule.MANIFEST_NAME).read_text(encoding="utf-8"))["files"]
    except (OSError, ValueError, KeyError) as e:
        raise SystemExit(f"SCHEDULE MANIFEST UNREADABLE at {d} ({type(e).__name__})")
    out: dict[str, dict] = {}
    for kind, template in wanted:
        name = _schedule.schedule_filename(unit, kind, template)
        raw = (d / name).read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        if manifest.get(name) != sha:
            raise SystemExit(f"SCHEDULE SHA MISMATCH: {name} sha256 {sha[:16]} is not the "
                             f"manifest's -- refusing (m:267)")
        obj = json.loads(raw.decode("utf-8"))
        want_kind = "campaign" if kind == "campaign" else "gate"
        if (obj.get("unit") != unit or obj.get("template") != template
                or obj.get("kind") != want_kind or (want_kind == "gate" and obj.get("gate") != kind)
                or obj.get("n") != len(obj.get("cells") or ())
                or _schedule.cells_sha256(obj["cells"]) != obj.get("sha256_of_cells")):
            raise SystemExit(f"SCHEDULE FILE MALFORMED: {name} -- refusing")
        out[template] = {"name": name, "sha256": sha, "n": obj["n"], "cells": obj["cells"]}
    return out


def _schedules_sha(scheds: Mapping[str, Mapping]) -> str:
    # PIN (Code, declared at LOCK v0.1): a stage's schedule_sha256 (resume identity) is
    # sha256 over "{file name} {file sha256}\n" for the stage's files, sorted by name.
    body = "".join(f"{v['name']} {v['sha256']}\n" for v in sorted(scheds.values(),
                                                                 key=lambda v: v["name"]))
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


# --- startup, identity -----------------------------------------------------------
def _bar_set(unit: str) -> tuple[_bars.Bar, ...]:
    return _bars.QF0_BARS if unit == "Q-F0" else _bars.OLMO_BARS(_ckpt_name(unit))


def _startup(adapter, unit: str) -> tuple[Any, str, str]:
    """(setup, audit sha16, ban sha16) once per stage."""
    if unit == "Q-F0":
        st = qwen_startup(adapter)
        audit_sha = st.audit_cfg["sha16_recomputed"]
    else:
        st = olmo_startup(adapter, _ckpt_name(unit))
        audit_sha = st.audit_sha16
    # PIN (Code, declared at LOCK v0.1): the identity's ban_sha is the sha16 of
    # json.dumps(sorted(ban ids)) of the ban list the stage actually generates with --
    # audit.assert_olmo_scaffold's form; on OLMo it equals b3's 2dd86a453a2275ef.
    ban_sha = hashlib.sha256(json.dumps(sorted(int(i) for i in st.ban_ids)).encode()).hexdigest()[:16]
    return st, audit_sha, ban_sha


# PIN (Code, declared at LOCK v0.1; the seat's D2, 2026-10-10): optional on the stub only --
# lock_file, proposal_file, analyzer_sha256 and package_sha256 are REQUIRED on a non-stub run
# (``_extra``); prior_proposal_sha256s stays optional everywhere.
_OPTIONAL_EXTRA = ("lock_file", "proposal_file", "prior_proposal_sha256s", "analyzer_sha256",
                   "package_sha256")


def _repo_rel_ok(v: Any) -> bool:
    """A repo-relative posix path: non-empty str, not absolute, no '..', no backslash,
    normalized, naming no roster word."""
    return (type(v) is str and bool(v) and not Path(v).is_absolute() and ".." not in Path(v).parts
            and "\\" not in v and Path(v).as_posix() == v and not _ROSTER_RX.search(v))


def _extra(identity_extra: Mapping[str, Any], *, stage: str, sub: str, stub: bool = True) -> dict:
    """The values a stage cannot derive, validated.

    PIN (Code, declared at LOCK v0.1; the seat's D2, 2026-10-10, for the two sha256 keys):
    identity_extra carries {lock_sha256,
    proposal_sha256, locked_path, renders_sha16}: the governing lock's sha256 and this
    document's (64 lower-case hex; "pre-lock" is refused -- G-TIME and G-ID follow LOCK
    v0.1, qualification v0.2, the campaign v1.0, m:279-286, m:302), the path the lock
    fixes ("cached" | "uncached"; G-TIME and every OLMo stage "uncached", m:267, m:280),
    and the renders' sha16 the lock pins. G-ID-F0m carries no locked_path (the path is
    locked at v0.2, AFTER G-ID, m:282; a value is refused) but carries renders_sha16 like
    every stage (its scaffold is built with the renders of record). Optional keys:
    ``lock_file`` and ``proposal_file`` -- the lock's and the proposal's repo-relative
    posix paths (no '..', no roster word), REQUIRED on a non-stub adapter (the licence
    by file checks each committed at HEAD with sha256 as named; findings 39, R11); on
    the stub the lock file may be omitted and the proposal defaults to PROPOSAL_REL;
    ``prior_proposal_sha256s`` -- the earlier proposals' sha256 the governing lock
    re-adopts after an amendment (a list of distinct 64-hex, never this run's own;
    default none): a prior stage or the G-ID artifact under one of them is accepted
    (finding R11; approved by the seat's ruling (n): a stage is re-adopted only where its
    governing proposal sections are byte-identical between the versions, which Code checks
    with ``governing_sections_identical`` and records at the lock -- ``accepted_proposals``'s
    PIN); ``analyzer_sha256`` and ``package_sha256`` -- the analyzer's and the m package's
    sha256 the lock pins (64 lower-case hex), REQUIRED on a non-stub adapter, as the files
    are (the seat's D2, 2026-10-10: the licence checks the analyzer's bytes, the package
    this process hashes, and the lock's text naming both, finding R8); on the stub each is
    optional and form-checked when given.
    """
    gid = stage == "id"
    want = ("lock_sha256", "proposal_sha256", "renders_sha16") + (() if gid else ("locked_path",))
    keys_ok = isinstance(identity_extra, Mapping) and (
        set(want) <= set(identity_extra) <= set(want) | set(_OPTIONAL_EXTRA))
    if not keys_ok:
        got = sorted(identity_extra) if isinstance(identity_extra, Mapping) else identity_extra
        raise ValueError(f"identity_extra must carry exactly {want} (+ optional {_OPTIONAL_EXTRA})"
                         + (" (G-ID has no locked path, m:282)" if gid else "") + f"; got {got}")
    out: dict[str, Any] = {k: identity_extra[k] for k in want}
    for k in ("lock_sha256", "proposal_sha256"):
        if type(out[k]) is not str or not _HEX64.match(out[k]):
            raise ValueError(f"{k} must be a sha256 hex digest (64 lower-case hex); 'pre-lock' is "
                             f"refused: every stage built here runs after its governing lock")
    for k in ("lock_file", "proposal_file"):
        v = identity_extra.get(k)
        if v is None:
            if not stub:
                raise ValueError(f"identity_extra must name {k} (the repo-relative path) on a "
                                 f"non-stub run: the licence by file checks it (findings 39, R11)")
            v = PROPOSAL_REL if k == "proposal_file" else None
        elif not _repo_rel_ok(v):
            raise ValueError(f"{k} must be a repo-relative posix path (no '..', no roster word), "
                             f"got {v!r}")
        out[k] = v
    pp = identity_extra.get("prior_proposal_sha256s")
    if pp is None:
        pp = []
    if (type(pp) not in (list, tuple) or any(type(x) is not str or not _HEX64.match(x) for x in pp)
            or len(set(pp)) != len(pp) or out["proposal_sha256"] in pp):
        raise ValueError(f"prior_proposal_sha256s must be a list of distinct sha256 hex digests, "
                         f"none of them this run's proposal_sha256; got {pp!r}")
    # PIN (Code, declared at LOCK v0.1; finding R11): recorded sorted (the lock names a set).
    out["prior_proposal_sha256s"] = sorted(pp)
    # PIN (Code, declared at LOCK v0.1; the seat's D2, 2026-10-10): on a non-stub run
    # analyzer_sha256 and package_sha256 are required, exactly as lock_file and proposal_file
    # are -- an absent one is a ValueError here, before anything else at stage start; given,
    # each must be 64 lower-case hex (stub or not); on the stub an absent one is recorded None.
    for k in ("analyzer_sha256", "package_sha256"):
        v = identity_extra.get(k)
        if v is None:
            if not stub:
                raise ValueError(f"identity_extra must carry {k} on a non-stub run (the seat's D2, "
                                 f"2026-10-10): the licence checks it at stage start")
        elif type(v) is not str or not _HEX64.match(v):
            raise ValueError(f"{k} must be a sha256 hex digest (64 lower-case hex), got {v!r}")
        out[k] = v
    if type(out["renders_sha16"]) is not str or not _HEX16.match(out["renders_sha16"]):
        raise ValueError("renders_sha16 must be 16 lower-case hex")
    if not gid:
        lp = out["locked_path"]
        if lp not in ("cached", "uncached"):
            raise ValueError(f"locked_path must be 'cached' or 'uncached', got {lp!r}")
        if (stage == "time" or sub == "olmo") and lp != "uncached":
            raise ValueError(f"locked_path {lp!r}: G-TIME and every OLMo stage are uncached by "
                             f"spec (m:267, m:280)")
    return out


def _renders_of_record(extra: Mapping[str, Any], name: str) -> tuple[list[dict], list[str], str]:
    pool, renders = _sc.pool_and_renders()
    rsha = _corr.renders_sha(renders)
    if extra["renders_sha16"] != rsha:
        raise SystemExit(f"RENDERS MISMATCH ({name}): the lock's renders sha16 "
                         f"{extra['renders_sha16']} is not the renders of record built here "
                         f"({rsha}); no session runs (m:176, m:279, m:286)")
    return pool, renders, rsha


def _pending_on_disk(cpath: Path) -> bool:
    """Does the checkpoint at ``cpath`` carry an end pending? Read tolerantly (False when
    absent or unreadable); load_or_init re-reads it under the identity check."""
    try:
        ck = json.loads(Path(cpath).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError):
        return False
    return isinstance(ck, dict) and _resume.pending_end(ck) is not None


def _locked(name: str, extra: Mapping[str, Any], admitted: bool, cpath: Path | None = None) -> str:
    """The run's path, which must be the locked one (m:267, m:282) -- except where the
    checkpoint at ``cpath`` carries an end pending: that invocation launches nothing (a
    re-finish, finding R1), so the locked path names it whatever the licence on this
    backend now gives."""
    path = "cached" if admitted else "uncached"
    # PIN (Code, declared at LOCK v0.1; round-3 verification): "re-finish-only on any pod
    # and at any invocation" holds across a backend change too -- a pending end is
    # re-finished under the locked path even where this backend's G-ID licence differs;
    # the drivers assert that such an invocation reaches the re-finish (no launch).
    if extra["locked_path"] != path and cpath is not None and _pending_on_disk(cpath):
        print(f"PATH ({name}): the lock fixes {extra['locked_path']}; this backend's licence gives "
              f"{path}; an end is pending at {Path(cpath).name}, so this invocation only "
              f"re-finishes it (nothing launches)", flush=True)
        return extra["locked_path"]
    if extra["locked_path"] != path:
        raise SystemExit(f"PATH MISMATCH ({name}): the lock fixes the {extra['locked_path']} path; "
                         f"the G-ID licence on this backend gives {path} -- refusing (m:267, m:282; "
                         f"a new backend needs its own G-ID, rule 2)")
    return path


def _identity(adapter, unit: str, stage: str, template_set: Sequence[str], path: str,
              n: Mapping[str, int], scheds: Mapping, audit_sha: str, ban_sha: str,
              extra: Mapping, pool: Sequence[Mapping], renders_sha: str,
              hour_cap: Any = None) -> dict:
    return _resume.Identity(unit=unit, stage=stage, template_set=list(template_set),
                           schedule_sha256=_schedules_sha(scheds), path=path, hour_cap=hour_cap,
                           n=dict(n), audit_v2_sha16=audit_sha, ban_sha=ban_sha,
                           backend_identifier=_resume.backend_identifier(adapter.provenance()),
                           lock_sha256=extra["lock_sha256"],
                           proposal_sha256=extra["proposal_sha256"],
                           package_sha256=_resume.package_sha256(),
                           pool_sha16=_resume.pool_sha16(pool), renders_sha16=renders_sha)


def _begin(adapter, unit: str, stage: str, name: str, cpath: Path, paths: Mapping,
           extra: Mapping[str, Any]) -> dict:
    """Every stage's start, in order, before any session or write: the stub guard, the
    non-stub out root, the pod id (OLMo), an ENDED checkpoint refused, the adapter's
    provenance checked, the run-time known answers against the proposal file
    ``extra`` names, the laptop preflight (non-stub Qwen). Returns the provenance record
    the stage appends once its checkpoint is loaded."""
    _stub_guard(adapter, *[p for p in (paths["root"], cpath, paths["report"],
                                       paths.get("reads"), paths.get("gid")) if p is not None])
    _out_root_guard(adapter, paths["root"])
    _require_pod(unit)
    _resume.refuse_ended(cpath)
    prov = _start_provenance(adapter, name)
    _startup_checks(name, _proposal_path(extra))
    _laptop_preflight(adapter, unit, name, extra)
    return prov


def _licensed(adapter, unit: str, stage: str, name: str, extra: Mapping[str, Any],
              prior_ckpt, prior_adjudication: str | None = None) -> dict:
    """The prior: the licence by file (non-stub), then the prior stage under this run's
    proposal or one its lock re-adopts (a non-stub run takes no stub-written prior)."""
    stub = _is_stub(adapter)
    _licence(adapter, extra, name)
    return prior_gate(unit, stage, prior_ckpt, prior_adjudication,
                      proposal_sha256=extra["proposal_sha256"],
                      prior_proposal_sha256s=extra["prior_proposal_sha256s"], require_real=not stub)


def _refuse_stopped(ckpt: Mapping, where: Path) -> None:
    # PIN (Code, declared at LOCK v0.1): a resume never lifts a STOP; the stopped
    # checkpoint is the adjudication's record and the seat re-specifies (m:271).
    # (resume.load_or_init refuses an ended checkpoint first; this is the backstop.)
    if ckpt.get("stop"):
        raise SystemExit(f"STAGE ENDED at {where} (STOP): a resume never lifts a STOP -- the "
                         f"seat adjudicates and re-specifies (m:271)")


# --- one session ------------------------------------------------------------------
def _launch(adapter, setup, unit: str, stage: str, template: str, s: int, cell: Mapping,
            *, path_cached: bool) -> tuple[dict | None, list[str]]:
    """Scaffold, run, G-VER. (record or None, problems).

    ``verify.schedule_check(sc, cell)`` is a STRUCTURAL assertion only: ``sc`` is built
    from ``cell`` itself, so it holds by construction and fires only if m_config's
    handling of a cell changes (finding 32). The schedule_mismatch guards that bind
    before a session are load_committed and startup_problems; G-VER binds after it.
    """
    pool, renders = _sc.pool_and_renders()
    path = "cached" if path_cached else "uncached"
    sc = _sc.m_config(unit, stage, template, s, cell, path, pool=pool, renders=renders)
    pre = _verify.schedule_check(sc, cell)
    if pre:
        return None, pre
    if sc.substrate == "qwen":
        rec = run_session_qwen(adapter, sc, setup.audit, setup.ban_ids, path_cached=path_cached,
                               term_rx=setup.term_rx)
    else:
        if path_cached:
            raise ValueError("OLMo sessions are uncached (m:267)")
        rec = run_session_olmo(adapter, sc, setup.audit, setup.ban_ids, term_rx=setup.term_rx)
    problems = _verify.verify_and_mark(rec, substrate=sc.substrate, pool=pool, renders=renders,
                                       schedule_cell=cell)
    return rec, problems


def _verify_hit(template: str, s: int, problems: Sequence[str], rec: dict | None) -> dict:
    # PIN (Code, declared at LOCK v0.1): a G-VER failure names its trigger by the first
    # problem's class (schedule_mismatch or template_breakage). The record is NOT a
    # finished session: it is kept, verified False, in the checkpoint's stop block for
    # the adjudication read (m:318 exception (1)); it never enters `sessions`.
    bar = _verify.MISMATCH if problems[0].startswith(_verify.MISMATCH) else _verify.BREAK
    return {"bar": bar, "template": template, "s": s, "phase": None,
            "contrast": keys.is_contrast(template), "problems": list(problems),
            "record": rec, "round": None,
            "j": rec.get("j") if isinstance(rec, Mapping) else None,
            "path": rec.get("path") if isinstance(rec, Mapping) else None}


def _hair_hit(rec: Mapping) -> dict | None:
    h = rec.get("hair_triggers") or []
    if not h:
        return None
    # PIN (Code, declared at LOCK v0.1): the fired round is the session's last recorded
    # round (a runner ends the session there; verify refuses a record that continues
    # past it); its phase, n and ri/ci go to the checkpoint's stop block only -- for the
    # adjudication read m:271 confines -- and are never printed.
    last = (rec.get("rounds") or [{}])[-1]
    rnd = {"phase": h[0]["phase"], "n": last.get("n"),
           "index": last.get("ri", last.get("ci"))}
    return {"bar": h[0]["name"], "template": rec["template"], "s": rec["s"],
            "phase": h[0]["phase"], "contrast": bool(rec["contrast"]), "problems": [],
            "record": None, "round": rnd, "j": rec.get("j"), "path": rec.get("path")}


def announce_stop(unit: str, stage: str, hit: Mapping) -> tuple[list[str], dict]:
    """(stdout lines, blinded stop block) for a hair trigger (m:271, m:318).

    A contrast session's free-phase trigger is announced by phase alone: no class,
    no round, no pick (m:318 exception (1)); readrule withholds it from every
    pick-free form, so this is the only announcement it gets before VERDICTS.
    """
    # PIN (Code, declared at LOCK v0.1): the free-phase contrast announcement names the
    # stage, the template and s (both already on the session's printed line) and the
    # phase; the bar's class goes to the checkpoint's stop block only. Every other trigger
    # prints the bar's own blinded message (name, template, phase where it has one) -- a
    # G-VER failure has no phase and names its harness class (template_breakage /
    # schedule_mismatch), which describes the harness, not the session's content.
    name = stage_name(unit, stage)
    t, s, ph = hit["template"], hit["s"], hit["phase"]
    if hit["contrast"] and ph == "free":
        return ([f"STOP {name}: a hair trigger fired in the free phase of a contrast session "
                 f"({t} s={s}); its class is withheld (m:318 exception (1)); the stage stops for "
                 f"the seat's adjudication"],
                {"bar": WITHHELD_CLASS, "template": t, "s": s, "phase": "free"})
    bar = {b.name: b for b in _bar_set(unit)}[hit["bar"]]
    ctx: dict = {"template": t}
    if ph is not None:
        ctx["phase"] = ph
    res = bar.evaluate(1, 1, **ctx)
    return ([res.message, f"STOP {name}: hair trigger {hit['bar']} ({t} s={s}); the stage stops "
                          f"(m:271)"],
            {"bar": hit["bar"], "template": t, "s": s, "phase": ph})


def _stop_record(hit: Mapping, blinded: Mapping) -> dict:
    """The stop block a hair trigger or G-VER failure persists (pending first, then as
    the checkpoint's ``stop``): the fired round's identifiers, or the quarantined record."""
    return {"kind": "hair_trigger", "bar": hit["bar"], "template": hit["template"],
            "s": hit["s"], "j": hit.get("j"), "path": hit.get("path"), "phase": hit["phase"],
            "round": copy.deepcopy(hit.get("round")), "problems": list(hit["problems"]),
            "record": copy.deepcopy(hit["record"]), "blinded": dict(blinded)}


def _hit_from_stop(stop: Mapping | None) -> dict | None:
    """The hit a pending stop records, rebuilt for a re-finish (finding R1)."""
    if stop is None:
        return None
    return {"bar": stop["bar"], "template": stop["template"], "s": stop["s"], "phase": stop["phase"],
            "contrast": keys.is_contrast(stop["template"]), "problems": list(stop["problems"]),
            "record": copy.deepcopy(stop["record"]), "round": copy.deepcopy(stop["round"]),
            "j": stop.get("j"), "path": stop.get("path")}


def _record_stage_end(ckpt: dict, status: str, fired: Sequence[str]) -> None:
    # PIN (Code, declared at LOCK v0.1): every gate-stage end -- hair trigger, stage-end
    # bar STOP, the OLMo PAUSE, PASS, G-ID's verdicts -- is persisted as stage_end
    # {status, fired bar names, adjudication None} (the drivers through the pending end,
    # resume.apply_end, which builds this very dict; this helper builds synthetic priors);
    # the next stage reads it (prior_gate) and no resume or pod change lifts it
    # (resume.load_or_init). The seat's adjudication is never written here by Code.
    ckpt["stage_end"] = {"status": status, "fired": [str(x) for x in fired], "adjudication": None}


def _pend(ckpt: dict, cpath: Path, pending: Mapping, name: str) -> tuple[dict, bool]:
    """(the end's persisted form, whether this finish must still WRITE the pending end).

    The end computed in memory is set as end_pending (finding R1) and its persisted form
    built (``resume.apply_end``), so every output can be built and asserted (pick-free,
    persistable) before anything is written. On a re-finish the pending end is already on
    disk and must be the one re-derived from it."""
    have = _resume.pending_end(ckpt)
    first = have is None
    if first:
        _resume.set_end_pending(ckpt, pending)
    elif not _resume.same_json(have, pending):
        raise SystemExit(f"END PENDING MISMATCH ({name}) at {cpath}: the end on disk is not the one "
                         f"re-derived from its sessions -- refusing; no session, output or end written (this "
                         f"invocation's provenance entry is already on disk)")
    final = _resume.apply_end(copy.deepcopy(ckpt))
    _resume.assert_writable(cpath, final)
    return final, first


def _write_pending(cpath: Path, ckpt: dict, final: dict) -> None:
    """A finish's FIRST write (finding R1): the pending end in the same atomic write as
    every session the invocation recorded -- before any output. ``final`` follows the
    write's state stamp, so persist_end finds it exactly apply_end(on disk)."""
    _resume.write_checkpoint(cpath, ckpt)
    final["state"] = copy.deepcopy(ckpt["state"])


def _refinish_line(name: str, status: str, cpath: Path) -> str:
    # PIN (Code, declared at LOCK v0.1; finding R1): a re-finish announces itself by the
    # pending end's status only (the stop's class stays blinded, as at its announcement).
    return (f"RE-FINISH {name}: {cpath.name} carries an end pending ({status}); nothing launches -- "
            f"the outputs are re-derived from the checkpoint and the end persisted (m:267, m:271)")


def _remove_stale(apath: Path) -> None:
    # PIN (Code, declared at LOCK v0.1; finding R1): a finish with no STOP or PAUSE event
    # removes any excerpt at its checkpoint's adjudication path -- one left by an earlier
    # write of the same checkpoint name can only mislead (it names the checkpoint).
    if apath.is_file() or apath.is_symlink():
        apath.unlink()


# --- pick-free outputs ----------------------------------------------------------------
_ROSTER_RX = re.compile(r"\b(?:" + "|".join(re.escape(w) for w in
                                              sorted({x for r in (_schedule.roster_for("Q-F0"),
                                                                  _schedule.olmo_roster())
                                                      for p in r for x in p})) + r")\b",
                        re.IGNORECASE)


def _assert_pick_free(obj: Any, what: str) -> None:
    """No roster label anywhere in a pick-free artifact (key or value, whole word)."""
    if _ROSTER_RX.search(json.dumps(obj, sort_keys=True, ensure_ascii=False)):
        raise ValueError(f"{what}: a roster label reached a pick-free artifact; refused")


def _sham_seconds(records: Sequence[Mapping]) -> dict:
    # PIN (Code, declared at LOCK v0.1): stage timing is reported over sham-template
    # sessions only; a contrast session's seconds encode its free-round exclusion
    # position and stay in the checkpoint until VERDICTS (m:318; build design §0 rule 5).
    sh = [r for r in records if not r["contrast"]]
    return {"sham_sessions": len(sh), "sham_seconds": round(sum(float(r["seconds"]) for r in sh), 3),
            "contrast_seconds": "withheld to the unit's VERDICTS entry (m:318)"}


def _reads(records: Sequence[Mapping]) -> list[dict]:
    """§3's pre-VERDICTS reads: contrast stripped to banner + forced rounds, sham redacted."""
    return [readrule.strip_contrast(r) if r["contrast"] else readrule.redact_sham(r) for r in records]


def _write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    _resume.atomic_write_json(path, obj, indent=1)


def _ident_summary(ident: Mapping) -> dict:
    return {k: ident[k] for k in ("lock_sha256", "proposal_sha256", "schedule_sha256", "path",
                                  "audit_v2_sha16", "ban_sha", "backend_identifier",
                                  "package_sha256", "pool_sha16", "renders_sha16")}


def _sha16_text(text: str | None) -> str | None:
    return None if text is None else hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def _stage_line(name: str, status: str, path: str) -> str:
    return f"STAGE {name} {status} path={path}"


def _write_unless_identical(path: Path, obj: Any, *, indent: int = 1) -> None:
    """Write ``obj``; an existing file with exactly these bytes is left as it is."""
    if path.is_file() and path.read_text(encoding="utf-8") == _resume.json_text(obj, indent=indent):
        return
    _write_json(path, obj)


# --- the confined adjudication excerpt (m:271; m:318 exception (1)) ---------------------
# PIN (Code, declared at LOCK v0.1): on every STOP or PAUSE the stage writes
# adjudication_path(checkpoint) (under ckpt/, tracked and -diff like the checkpoint),
# never printed, holding only what the adjudication needs: for a hair trigger, the fired
# session's identifiers and the fired round's header-piece bytes, generation text and
# audit dict; for a G-VER stop (no fired round), the identifiers and the verifier's
# problems; for a fired binomial bar or the OLMo G-TIME pause, the numerator's rounds
# (sham sessions only by construction) with the same fields; for a campaign look,
# end-look or schedule-exhausted pause, the counts only (no round). "picks_revealed"
# lists every pick the excerpt reveals: a free round's header names the chosen config
# and its task line is clean or corrupted by the pick, so each free round in an excerpt
# reveals that round's pick (m:271: "the pick it reveals is recorded as seen"). The
# file is rebuilt from the checkpoint's state at each STOP or PAUSE (a campaign's holds
# one event per pause and its stop), so a re-finish rewrites identical bytes.
def _session_ids(rec: Mapping) -> dict:
    return {"unit": rec.get("unit"), "stage": rec.get("stage"), "template": rec.get("template"),
            "s": rec.get("s"), "j": rec.get("j"), "path": rec.get("path"),
            "contrast": bool(rec.get("contrast"))}


def _round_excerpt(rec: Mapping, rd: Mapping) -> tuple[dict, list[dict]]:
    """(the round as the adjudication reads it, the picks it reveals)."""
    ph = rd.get("phase")
    idx = rd.get("ri") if ph == "forced" else rd.get("ci")
    header = None
    tr = rec.get("transcript") or ""
    for p in rec.get("pieces") or []:
        if p.get("kind") == "round" and p.get("phase") == ph and p.get("idx") == idx:
            header = tr[p["start"]:p["end"]]
            break
    ex = {**_session_ids(rec), "phase": ph, "index": idx, "n": rd.get("n"), "header": header,
          "generation": rd.get("text"), "audit": copy.deepcopy(rd.get("audit"))}
    picks = ([{**_session_ids(rec), "ci": idx, "n": rd.get("n"), "pick": rd.get("label")}]
             if ph == "free" else [])
    return ex, picks


def _hit_event(records: Sequence[Mapping], hit: Mapping) -> dict:
    """A hair-trigger (or G-VER) STOP's excerpt: the fired round only."""
    if hit.get("round") is None:
        rec = hit.get("record") if isinstance(hit.get("record"), Mapping) else {}
        return {"event": "STOP", "kind": "harness", "bar": hit["bar"],
                "session": {**_session_ids(rec), "template": hit["template"], "s": hit["s"],
                            "contrast": bool(hit["contrast"])},
                "problems": list(hit["problems"]), "rounds": [], "picks_revealed": []}
    want = (hit["template"], hit["s"], hit.get("path"))
    rec = next((r for r in reversed(records) if (r["template"], r["s"], r.get("path")) == want), None)
    rounds, picks = [], []
    if rec is not None and rec.get("rounds"):
        ex, picks = _round_excerpt(rec, rec["rounds"][-1])
        rounds = [ex]
    return {"event": "STOP", "kind": "hair_trigger", "bar": hit["bar"],
            "session": _session_ids(rec) if rec is not None else {"template": hit["template"],
                                                                     "s": hit["s"]},
            "rounds": rounds, "picks_revealed": picks}


def _bars_event(records: Sequence[Mapping], status: str, fired: Sequence[_bars.BarResult]) -> dict:
    """A fired binomial bar's (or the OLMo pause's) excerpt: the numerator's rounds."""
    rounds: list[dict] = []
    picks: list[dict] = []
    for r in records:
        if not _bars.sham_domain(r):
            continue
        for rd in r["rounds"]:
            if (rd.get("audit") or {}).get("claim") in _bars.DEGEN_CLAIMS[r["substrate"]]:
                ex, pk = _round_excerpt(r, rd)
                rounds.append(ex)
                picks += pk
    return {"event": status, "kind": "bars", "bars": [b.name for b in fired],
            "counts": [b.as_dict() for b in fired], "rounds": rounds, "picks_revealed": picks}


def _adjudication_doc(unit: str, stage: str, name: str, cpath: Path, root: Path,
                      events: Sequence[Mapping]) -> dict:
    return {"schema": ADJ_SCHEMA, "unit": unit, "stage": stage, "stage_name": name,
            "form": "confined adjudication read (m:271; m:318 exception (1)): pick-bearing, under "
                    "ckpt/ (-diff); never printed",
            "checkpoint": _rel(cpath, root), "events": [dict(e) for e in events]}


# --- gate stages ------------------------------------------------------------------------
def run_gate_stage(adapter, *, unit: str, gate: str, templates_counts: Sequence[tuple[str, int]],
                   ckpt_path: str | os.PathLike | None = None, resume: bool = False,
                   identity_extra: Mapping[str, Any], substrate: str,
                   out_root: str | os.PathLike = DEFAULT_OUT,
                   prior_ckpt: str | os.PathLike | None = None,
                   prior_adjudication: str | None = None) -> dict:
    """G-TIME (m:280, m:302) or the qualification stage (m:283, m:302) of one unit.

    ``prior_ckpt`` (the unit's G-TIME checkpoint) is required for the qualification
    stage and refused for G-TIME; ``prior_adjudication`` only for an OLMo qualification
    after a G-TIME-OLMo PAUSE (prior_gate). A checkpoint carrying an end pending is
    re-finished whatever ``resume`` says (finding R1).
    """
    sub = _check_unit(unit, substrate)
    if gate not in GATES:
        raise ValueError(f"run_gate_stage runs {GATES}; G-ID is run_gid_pair, the campaign "
                         f"run_campaign (got {gate!r})")
    name = stage_name(unit, gate)
    paths = out_paths(unit, gate, out_root)
    cpath = checkpoint_path(ckpt_path, paths)
    paths = for_checkpoint(paths, cpath)
    extra = _extra(identity_extra, stage=gate, sub=sub, stub=_is_stub(adapter))
    prov = _begin(adapter, unit, gate, name, cpath, paths, extra)
    prior = _licensed(adapter, unit, gate, name, extra, prior_ckpt, prior_adjudication)
    pool, _renders, rsha = _renders_of_record(extra, name)
    tpls = keys.templates(unit)
    scheds = load_committed(unit, [(gate, t) for t in tpls], paths["schedules"])
    tc = [(t, m) for t, m in templates_counts]
    # PIN (Code, declared at LOCK v0.1): the counts are the committed gate files' n --
    # G-TIME 1 + 1 (m:280, m:302), qualification 8 contrast + 16 sham (m:283, m:302) --
    # in §2.4's table order; anything else is refused, never re-planned here.
    if tc != [(t, scheds[t]["n"]) for t in tpls]:
        raise ValueError(f"{name}: templates_counts {tc} != the committed schedule's "
                         f"{[(t, scheds[t]['n']) for t in tpls]}")
    order = _schedule.gate_launch_order(tc)
    bar_set = _bars.assert_firing_complete(_bar_set(unit), _bars.FIRING_CASES)
    setup, audit_sha, ban_sha = _startup(adapter, unit)
    bid = _resume.backend_identifier(adapter.provenance())
    path_cached = guard.cached_path_admitted(unit, gate, backend_identifier=bid)
    if path_cached and (gate == "time" or sub == "olmo"):
        raise AssertionError("G-TIME and OLMo are uncached by spec (m:267, m:280)")
    path = _locked(name, extra, path_cached, cpath)
    refinish_only = path != ("cached" if path_cached else "uncached")
    ident = _identity(adapter, unit, gate, tpls, path, dict(tc), scheds, audit_sha, ban_sha,
                      extra, pool, rsha)
    ckpt = _resume.load_or_init(cpath, ident, resume)
    if refinish_only and _resume.pending_end(ckpt) is None:
        # before any write, as the campaign driver refuses it
        raise SystemExit(f"PATH MISMATCH ({name}): the end pending at {cpath} is gone -- refusing "
                         f"to launch on a path this backend's licence does not give (m:267, rule 2)")
    _refuse_stopped(ckpt, cpath)
    _record_prior(ckpt, prior, cpath)
    _record_licence(ckpt, extra, cpath)
    _append_provenance(ckpt, prov)
    cpath.parent.mkdir(parents=True, exist_ok=True)
    _resume.write_checkpoint(cpath, ckpt)
    pending = _resume.pending_end(ckpt)
    if pending is not None:
        # The re-finish (finding R1): no launch; the hit the pending stop records.
        print(_refinish_line(name, pending["status"], cpath), flush=True)
        return _finish_gate(unit, gate, name, ckpt, cpath, paths, bar_set,
                            _hit_from_stop(pending["stop"]))
    done = _resume.done_ids(ckpt)
    hit = None
    for t, j in order:
        if (t, j) in done:
            continue
        _resume.note_launch(ckpt)
        rec, problems = _launch(adapter, setup, unit, gate, t, j, scheds[t]["cells"][j],
                                path_cached=path_cached)
        if problems:
            hit = _verify_hit(t, j, problems, rec)
            break
        _resume.record_session(ckpt, rec)
        hit = _hair_hit(rec)
        if hit is None:
            _resume.write_checkpoint(cpath, ckpt)
        print(readrule.session_line(rec), flush=True)
        if hit is not None:
            break
    return _finish_gate(unit, gate, name, ckpt, cpath, paths, bar_set, hit)


def _contrast_first_reads(unit: str, records: Sequence[Mapping]) -> dict:
    # PIN (Code, declared at LOCK v0.1): the qualification report carries m:283's
    # "reported, no bar" read flags for the CONTRAST arm in the campaign looks' form
    # (_read_flags, finding 12): reads, low label mass and top-1-not-a-label over the
    # FIRST read of each contrast domain session -- label mass and whether the top-1 is
    # a label say nothing about which label; later reads (which encode where a
    # free-round exclusion fell) stay withheld. The sham arm's flags are stage_report's.
    c_tpl = keys.templates(unit)[0]
    return {c_tpl: _read_flags([r for r in records if r["template"] == c_tpl], first_only=True)}


def _gate_end(unit: str, gate: str, records: Sequence[Mapping], bar_set, hit: Mapping | None) -> dict:
    """A gate stage's end, computed from its sessions (and the hit, if any): a pure
    function, so a re-finish re-derives exactly the end it recorded as pending."""
    if hit is not None:
        lines, blinded = announce_stop(unit, gate, hit)
        return {"status": "STOP", "fired": [hit["bar"]], "results": [], "lines": lines,
                "stop": _stop_record(hit, blinded), "events": [_hit_event(records, hit)]}
    # PIN (Code, declared at LOCK v0.1): the stage-end bars are the unit's
    # binomial_stage_end and pause bars whose stage is this gate (Qwen time: G-TIME-F0;
    # qual: G-F0m-Qwen; OLMo time: G-TIME-OLMo-{c} and its pause; OLMo qual:
    # G-F0m-OLMo-{c}), each evaluated once on the sham-template sessions.
    end_bars = [b for b in bar_set if b.stage == gate and b.kind in ("binomial_stage_end", "pause")]
    results = [_bars.stage_end_eval(records, b) for b in end_bars]
    fired_stop = any(r.fired for r, b in zip(results, end_bars) if b.kind == "binomial_stage_end")
    fired_pause = any(r.fired for r, b in zip(results, end_bars) if b.kind == "pause")
    # A round-1/2 OLMo claim fires both; the STOP governs (bars.py's PIN).
    # PIN (Code, declared at LOCK v0.1; the seat's note of 2026-10-06 on the step-3 notes:
    # "at G-TIME-OLMo a claim at realised n <= 2 fires the bar (STOP), which subsumes the
    # pause; the STOP governs"): both bars are recorded as fired (stage_end.fired, the
    # report's bars), the status is STOP, the excerpt holds ONE event (a STOP naming both),
    # and the pause is not separately acted on -- prior_gate takes an adjudication only
    # after a PAUSE, so the qualification does not run on the subsumed pause.
    status = "STOP" if fired_stop else "PAUSE" if fired_pause else "PASS"
    return {"status": status, "fired": [r.name for r in results if r.fired], "results": results,
            "lines": [r.message for r in results], "stop": None,
            "events": ([_bars_event(records, status, [r for r in results if r.fired])]
                       if status in ("STOP", "PAUSE") else [])}


# PIN (Code, declared at LOCK v0.1; the seat's ruling (h), 2026-10-06): at every G-TIME
# stage (G-TIME-F0, each G-TIME-OLMo-{ckpt}) no structured field outside ckpt/ carries the
# contrast session's forced-round class, claim counts or domain: stdout and the report carry
# only ruling (h)'s two counts per session, rounds generated and excluded yes/no (what the
# two locate together is disclosed at readrule's TIME_CONTRAST_KEYS); the reads carry m:280's
# mandated forced-round bytes with {phase, ri, n, text} per round (readrule's TIME_ROUND_KEEP
# PIN: the text shows how many forced rounds ran and each round's header, Task line and
# response). Stdout: its session line by
# phase alone (readrule.session_line); the bars bind on the sham session only (their messages,
# report entries and excerpts read no contrast round). Report: the contrast block is
# ruling (h)'s counts (readrule.stage_report); timing is sham-only. Reads: the G-TIME
# strip (readrule.strip_contrast). This function asserts the report's and the reads'
# contrast forms before anything is written. Kept as built, as m:318 exception (1)
# adjudications: a hair trigger or G-VER failure on the contrast session's FORCED phase is
# announced by the bar's blinded message, the STOP line, the report's blinded stop block
# (bar, template, s, phase) and resume's refusal words -- they name the trigger's class
# (or the harness class), never the round or its n -- and the fired round is read in the
# confined excerpt under ckpt/. Ruling (h)'s counts-only form governs everything else.
def _assert_time_counts_only(unit: str, report: Mapping, reads: Mapping) -> None:
    """Ruling (h) at a G-TIME stage's finish: the report's contrast block carries ruling
    (h)'s counts only and the reads' contrast sessions the G-TIME strip's form (forced bytes,
    {phase, ri, n, text} per round, no class field); ValueError otherwise (before any write)."""
    c_tpl = keys.templates(unit)[0]
    sr = report.get("stage_report")
    if sr is not None:
        blk = sr["templates"][c_tpl]
        per = blk.get("per_session") if isinstance(blk, Mapping) else None
        if (not isinstance(blk, Mapping) or tuple(blk) != readrule.TIME_CONTRAST_KEYS
                or not isinstance(per, list)
                or any(not isinstance(p, Mapping) or tuple(p) != readrule.TIME_SESSION_KEYS
                       or type(p["s"]) is not int or type(p["forced_rounds_generated"]) is not int
                       or type(p["excluded_at_forced"]) is not bool for p in per)):
            raise ValueError(f"{c_tpl}: the G-TIME report's contrast block is not ruling (h)'s counts "
                             f"(rounds generated, excluded yes/no); refused before any write")
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
        if (ks & readrule.TIME_WITHHELD or "rounds" not in r
                or any(not set(rd) <= set(readrule.TIME_ROUND_KEEP) for rd in r["rounds"])):
            raise ValueError(f"{c_tpl}: a G-TIME contrast read carries a class or round field "
                             f"(ruling (h)); refused before any write")


def _finish_gate(unit: str, gate: str, name: str, ckpt: dict, cpath: Path, paths: Mapping,
                 bar_set, hit: Mapping | None) -> dict:
    """The stage end (finding R1): computed in memory and its outputs built and asserted;
    FIRST the end written as end_pending with every session; THEN the report, reads and
    excerpt; THEN the end persisted. A re-finish enters with the end already pending."""
    end = _gate_end(unit, gate, ckpt["sessions"], bar_set, hit)
    final, first = _pend(ckpt, cpath, {"status": end["status"], "fired": end["fired"], "stop": end["stop"]},
                         name)
    records, ident = final["sessions"], final["identity"]
    stop_block = copy.deepcopy(final["stop"]["blinded"]) if final.get("stop") else None
    status, results, events = end["status"], end["results"], end["events"]
    tpls = keys.templates(unit)
    apath = adjudication_path(cpath)
    files = {"checkpoint": _rel(cpath, paths["root"]), "reads": _rel(paths["reads"], paths["root"])}
    if events:
        files["adjudication"] = _rel(apath, paths["root"])
    report = {"schema": REPORT_SCHEMA, "form": "pick-free stage report (m:271, m:318)",
              "unit": unit, "stage": gate, "stage_name": name, "status": status,
              "planned": dict(ident["n"]),
              "recorded": {t: sum(r["template"] == t for r in records) for t in tpls},
              "bars": [r.as_dict() for r in results], "stop": stop_block,
              "timing": _sham_seconds(records),
              "stage_report": readrule.stage_report(records) if records else None,
              "identity": _ident_summary(ident),
              "provenance": _resume.report_provenance(final),
              "files": files}
    if gate == "qual":
        report["contrast_first_read_flags"] = _contrast_first_reads(unit, records)
    _assert_pick_free(report, name)
    reads = {"schema": READS_SCHEMA, "unit": unit, "stage": gate, "stage_name": name,
             "form": "pre-VERDICTS reads (m:271): contrast = banner + forced rounds; sham = "
                     "menus removed, chosen tag [config]",
             "sessions": _reads(records)}
    if gate == "time":
        _assert_time_counts_only(unit, report, reads)
    adj = _adjudication_doc(unit, gate, name, cpath, paths["root"], events) if events else None
    if first:
        _write_pending(cpath, ckpt, final)
    _write_json(paths["report"], report)
    _write_json(paths["reads"], reads)
    if adj is not None:
        _write_json(apath, adj)
    else:
        _remove_stale(apath)
    _resume.persist_end(cpath, final)
    for ln in end["lines"]:
        print(ln, flush=True)
    print(_stage_line(name, status, ident["path"]), flush=True)
    outs = [("CHECKPOINT", cpath), ("REPORT", paths["report"]), ("READS", paths["reads"])]
    if events:
        outs.append(("ADJUDICATION", apath))
    for k, p in outs:
        print(f"{k} {p}", flush=True)
    return {"status": status, "stage_name": name, "checkpoint": cpath, "report": paths["report"],
            "reads": paths["reads"], "bars": results, "adjudication": apath if events else None}


# --- G-ID-F0m ---------------------------------------------------------------------------
def gid_decide(pairs: Sequence[Mapping[str, Any]]) -> dict:
    """G-ID-F0m's criterion over the pairs run so far, in j order (m:281).

    Each pair: {"j", "complete" (both halves complete: 4 forced + 6 reads), "identical"
    (byte-identical transcripts)}. 2 complete identical pairs -> PASS; a divergence ->
    FAIL; past j = 15 without 2 -> NOT-DETERMINED (never PASS); else OPEN (advance j).
    """
    decided: list[bool] = []
    for p in pairs:
        # PIN (Code, declared at LOCK v0.1): a divergence fails G-ID whether or not the
        # pair is complete -- a path that changes a session's length or exclusion has
        # diverged; only a byte-identical incomplete pair advances j (m:281's "an
        # undetermined licence is not a granted one", e2d_tstep_check.py:58-87).
        if not p["identical"]:
            decided.append(False)
            return {"verdict": "FAIL", "n_pairs": len(decided), "pairs_identical": decided,
                    "at_j": p["j"]}
        if p["complete"]:
            decided.append(True)
            if len(decided) == 2:
                return {"verdict": "PASS", "n_pairs": 2, "pairs_identical": decided, "at_j": p["j"]}
    verdict = "NOT-DETERMINED" if len(pairs) >= _schedule.GATE_MAX else "OPEN"
    return {"verdict": verdict, "n_pairs": len(decided), "pairs_identical": decided,
            "at_j": pairs[-1]["j"] if pairs else None}


def run_gid_pair(adapter, *, unit: str = "Q-F0", template: str = "A0s",
                 ckpt_path: str | os.PathLike | None = None, resume: bool = False,
                 identity_extra: Mapping[str, Any], prior_ckpt: str | os.PathLike | None,
                 out_root: str | os.PathLike = DEFAULT_OUT) -> dict:
    """G-ID-F0m (m:281): for j = 0..15, the A0s session uncached then cached under the
    same keys; writes the artifact guard.cached_path_admitted reads. ``prior_ckpt``:
    the unit's G-TIME-F0 checkpoint, which must have ended PASS. A checkpoint carrying an
    end pending is re-finished whatever ``resume`` says (finding R1)."""
    sub = _check_unit(unit)
    if sub != "qwen":
        raise ValueError(f"no G-ID on OLMo (uncached path, m:267): {unit!r}")
    if template != "A0s":
        raise ValueError("G-ID-F0m runs the A0s template only (m:281)")
    name = stage_name(unit, "id")
    paths = out_paths(unit, "id", out_root)
    cpath = checkpoint_path(ckpt_path, paths)
    paths = for_checkpoint(paths, cpath)
    gid_path = guard.gid_artifact_path(unit)
    extra = _extra(identity_extra, stage="id", sub=sub, stub=_is_stub(adapter))
    prov = _begin(adapter, unit, "id", name, cpath, {**paths, "gid": gid_path}, extra)
    # PIN (Code, declared at LOCK v0.1): a G-ID artifact is never overwritten; a re-run
    # after a re-specification starts with the old artifact moved aside by the operator.
    # The one exception is the RE-FINISH of this stage's own checkpoint carrying an end
    # pending (an interrupted finish: the artifact may be written, the end not yet
    # persisted) -- its finish then accepts the artifact only if byte-identical to the
    # one it re-derives and refuses a differing one (_finish_gid).
    if gid_path.exists() and not _resume.pending_at(cpath):
        raise SystemExit(f"G-ID ARTIFACT EXISTS at {gid_path}; it is never overwritten")
    prior = _licensed(adapter, unit, "id", name, extra, prior_ckpt)
    pool, _renders, rsha = _renders_of_record(extra, name)
    scheds = load_committed(unit, [("id", template)], paths["schedules"])
    cells = scheds[template]["cells"]
    bar_set = _bars.assert_firing_complete(_bar_set(unit), _bars.FIRING_CASES)
    setup, audit_sha, ban_sha = _startup(adapter, unit)
    ident = _identity(adapter, unit, "id", [template], "cached+uncached",
                      {template: len(cells)}, scheds, audit_sha, ban_sha, extra, pool, rsha)
    ckpt = _resume.load_or_init(cpath, ident, resume)
    _refuse_stopped(ckpt, cpath)
    _record_prior(ckpt, prior, cpath)
    _record_licence(ckpt, extra, cpath)
    _append_provenance(ckpt, prov)
    cpath.parent.mkdir(parents=True, exist_ok=True)
    _resume.write_checkpoint(cpath, ckpt)
    pending = _resume.pending_end(ckpt)
    if pending is not None:
        print(_refinish_line(name, pending["status"], cpath), flush=True)
        return _finish_gid(unit, name, ckpt, cpath, paths, bar_set,
                           _hit_from_stop(pending["stop"]), len(cells), gid_path)
    have = {(r["s"], r["path"]): r for r in ckpt["sessions"]}
    pairs: list[dict] = []
    hit = None
    for j in range(len(cells)):
        halves: dict[str, dict] = {}
        for path_cached in guard.gid_paths():
            path = "cached" if path_cached else "uncached"
            rec = have.get((j, path))
            if rec is None:
                _resume.note_launch(ckpt)
                rec, problems = _launch(adapter, setup, unit, "id", template, j, cells[j],
                                        path_cached=path_cached)
                if problems:
                    hit = _verify_hit(template, j, problems, rec)
                    break
                _resume.record_session(ckpt, rec)
                hit = _hair_hit(rec)
                if hit is None:
                    _resume.write_checkpoint(cpath, ckpt)
                print(readrule.session_line(rec), flush=True)
                if hit is not None:
                    break
            halves[path] = rec
        if hit is not None:
            break
        pairs.append(_gid_pair(j, halves["uncached"], halves["cached"]))
        if gid_decide(pairs)["verdict"] != "OPEN":
            break
    return _finish_gid(unit, name, ckpt, cpath, paths, bar_set, hit, len(cells), gid_path,
                       loop_pairs=pairs)


def _gid_pair(j: int, u: Mapping, c: Mapping) -> dict:
    return {"j": j, "complete": bool(u["complete"] and c["complete"]),
            "identical": u["transcript"] == c["transcript"],
            "complete_uncached": bool(u["complete"]), "complete_cached": bool(c["complete"])}


def gid_pairs(records: Sequence[Mapping], n_cells: int, upto: int | None = None) -> tuple[list[dict], dict]:
    """(pairs, decision) re-derived from the sessions on disk exactly as run_gid_pair's
    loop builds them: j ascending while both halves are recorded, stopping at the first
    decision; ``upto`` = a hit's j (the loop records no pair at the j it stopped in)."""
    have = {(r["s"], r["path"]): r for r in records}
    pairs: list[dict] = []
    for j in range(n_cells if upto is None else min(n_cells, upto)):
        u, c = have.get((j, "uncached")), have.get((j, "cached"))
        if u is None or c is None:
            break
        pairs.append(_gid_pair(j, u, c))
        if gid_decide(pairs)["verdict"] != "OPEN":
            break
    return pairs, gid_decide(pairs)


def _gid_end(unit: str, records: Sequence[Mapping], bar_set, hit: Mapping | None,
             decision: Mapping) -> dict:
    if hit is not None:
        lines, blinded = announce_stop(unit, "id", hit)
        return {"status": "STOP", "fired": [hit["bar"]], "results": [], "lines": lines,
                "stop": _stop_record(hit, blinded), "events": [_hit_event(records, hit)]}
    status = decision["verdict"]
    if status not in ("PASS", "FAIL", "NOT-DETERMINED"):
        raise AssertionError(f"G-ID ended with an open decision ({status})")
    bar = {b.name: b for b in bar_set}["gid_divergence@G-ID-F0m"]
    res = bar.evaluate(int(status == "FAIL"), max(len(decision["pairs_identical"]), 1),
                       template="A0s")
    return {"status": status, "fired": [res.name] if res.fired else [], "results": [res],
            "lines": [res.message], "stop": None, "events": []}


def _finish_gid(unit: str, name: str, ckpt: dict, cpath: Path, paths: Mapping, bar_set,
                hit: Mapping | None, n_cells: int, gid_path: Path,
                loop_pairs: list[dict] | None = None) -> dict:
    """G-ID's end, in _finish_gate's order (finding R1); the pairs and the decision are
    re-derived from the sessions on disk (``gid_pairs``), so a re-finish computes them
    as the loop did -- asserted equal to the loop's when there is one."""
    pairs, decision = gid_pairs(ckpt["sessions"], n_cells, None if hit is None else hit["s"])
    if loop_pairs is not None and loop_pairs != pairs:
        raise AssertionError("G-ID: the pairs re-derived from the sessions differ from the loop's")
    end = _gid_end(unit, ckpt["sessions"], bar_set, hit, decision)
    final, first = _pend(ckpt, cpath, {"status": end["status"], "fired": end["fired"], "stop": end["stop"]},
                         name)
    records, ident = final["sessions"], final["identity"]
    status, results, events = end["status"], end["results"], end["events"]
    stop_block = copy.deepcopy(final["stop"]["blinded"]) if final.get("stop") else None
    # PIN (Code, declared at LOCK v0.1): G-ID's report carries readrule.stage_report per
    # path (each (template, s) appears once per path) and both paths' generation seconds
    # (sham-only sessions: "cached timing recorded", m:281).
    timing = {p: round(sum(float(r["seconds"]) for r in records if r["path"] == p), 3)
              for p in ("uncached", "cached")}
    by_path = {p: [r for r in records if r["path"] == p] for p in ("uncached", "cached")}
    apath = adjudication_path(cpath)
    files = {"checkpoint": _rel(cpath, paths["root"]), "reads": _rel(paths["reads"], paths["root"])}
    if events:
        files["adjudication"] = _rel(apath, paths["root"])
    report = {"schema": REPORT_SCHEMA, "form": "pick-free stage report (m:271, m:281)",
              "unit": unit, "stage": "id", "stage_name": name, "status": status,
              "criterion": guard.GID_CRITERION, "pairs": pairs,
              "bars": [r.as_dict() for r in results], "stop": stop_block,
              "timing": {"uncached_seconds": timing["uncached"], "cached_seconds": timing["cached"]},
              "stage_report": {p: (readrule.stage_report(v) if v else None) for p, v in by_path.items()},
              "identity": _ident_summary(ident),
              "provenance": _resume.report_provenance(final),
              "files": files}
    _assert_pick_free(report, name)
    # PIN (Code, declared at LOCK v0.1): G-ID's sessions are sham-only and are read in
    # full at G-ID (m:271; §4 exception (4), m:318), so its reads file carries the full
    # records (readrule.release_full names the act).
    reads = {"schema": READS_SCHEMA, "unit": unit, "stage": "id", "stage_name": name,
             "form": "full records: G-ID's sham-only sessions (m:271; §4 exception (4))",
             "sessions": copy.deepcopy(readrule.release_full(records))}
    art = None
    if status in ("PASS", "FAIL", "NOT-DETERMINED"):
        # PIN (Code, declared at LOCK v0.1): the artifact carries the five fields the
        # licence reads (unit, criterion, verdict, n_pairs, pairs_identical), the
        # identity summary whose backend_identifier the licence also reads (rule 2: a
        # PASS licenses the backend it ran on only) and whose proposal_sha256 prior_gate
        # and run_campaign read (finding R3), the provenance of the invocations that
        # launched its sessions (report_provenance; a non-stub stage refuses a
        # stub-written artifact, finding R3), plus pick-free descriptive fields; n_pairs
        # counts decided pairs (complete identical, or any divergent pair). It is written
        # on PASS / FAIL / NOT-DETERMINED, never on STOP.
        art = {"schema": GID_SCHEMA, "unit": unit, "criterion": guard.GID_CRITERION,
               "verdict": status, "n_pairs": int(decision["n_pairs"]),
               "pairs_identical": list(decision["pairs_identical"]),
               "stage_name": name, "path_order": ["uncached", "cached"],
               "key_template": keys.arm_key(unit, "id", "A0s", "{s}"),
               "indices": pairs, "timing": report["timing"], "identity": _ident_summary(ident),
               "provenance": _resume.report_provenance(final)}
        _assert_pick_free(art, name)
    if gid_path.exists():
        # Only the re-finish of this stage's own pending end reaches here with an
        # artifact on disk (run_gid_pair's start refusal): it must be the very artifact
        # this finish re-derives -- byte for byte -- or the stage refuses, writing nothing.
        if art is None or gid_path.read_text(encoding="utf-8") != _resume.json_text(art, indent=1):
            raise SystemExit(f"G-ID ARTIFACT DIFFERS at {gid_path}: it is not the artifact this "
                             f"finish re-derives from the sessions on disk -- never overwritten; no "
                             f"output written, the end not persisted")
    adj = _adjudication_doc(unit, "id", name, cpath, paths["root"], events) if events else None
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
    _resume.persist_end(cpath, final)
    for ln in end["lines"]:
        print(ln, flush=True)
    print(_stage_line(name, status, ident["path"]), flush=True)
    outs = [("CHECKPOINT", cpath), ("REPORT", paths["report"]), ("READS", paths["reads"])]
    if events:
        outs.append(("ADJUDICATION", apath))
    if gid_path.exists():
        outs.append(("G-ID ARTIFACT", gid_path))
    for k, p in outs:
        print(f"{k} {p}", flush=True)
    return {"status": status, "stage_name": name, "checkpoint": cpath, "report": paths["report"],
            "reads": paths["reads"], "artifact": gid_path if gid_path.exists() else None,
            "pairs": pairs, "decision": dict(decision), "adjudication": apath if events else None}


# --- the campaign -----------------------------------------------------------------------
def _per_arm(v: Mapping[str, int], arms: Sequence[str], what: str) -> dict[str, int]:
    if not isinstance(v, Mapping) or sorted(v) != sorted(arms) or any(
            type(x) is not int or x < 1 for x in v.values()):
        raise ValueError(f"{what} must map each arm of {list(arms)} to a positive int, got {v!r}")
    return {a: int(v[a]) for a in arms}


def _prepick(rec: Mapping) -> bool:
    # PIN (Code, declared at LOCK v0.1): a pre-pick exclusion is a session excluded at
    # the forced phase (m:308: "sessions that never reached a pick"); the guard's k.
    exc = rec.get("exclusion")
    return bool(exc) and exc.get("phase") == "forced"


def _read_flags(records: Sequence[Mapping], *, first_only: bool) -> dict:
    # PIN (Code, declared at LOCK v0.1): m:330's reported read flags at a look, pooled per
    # arm -- the sham arm over ALL its reads; a contrast arm over FIRST reads only, one per
    # domain session (a contrast session's later reads encode where its free-round
    # exclusion fell, m:271, m:318).
    reads: list[Mapping] = []
    for r in records:
        ch = r.get("choices") or []
        if first_only:
            if r.get("domain") and ch:
                reads.append(ch[0])
        else:
            reads.extend(ch)
    return {"scope": "first reads of domain sessions" if first_only else "all reads",
            "reads": len(reads),
            "low_label_mass": sum(bool(c.get("low_label_mass")) for c in reads),
            "top1_not_label": sum(bool(c.get("top1_not_label")) for c in reads)}


def campaign_look(unit: str, records: Sequence[Mapping], look: Any) -> dict:
    """One §6 look (m:330, m:316): round_degeneracy on the sham arm (cumulative),
    the Fisher guard (binding) and the absolute guard (binding on Qwen, reported on
    OLMo) per contrast arm, pooled pre-pick exclusion counts per arm (m:318), and the
    reported read flags (low label mass, top-1-not-a-label) per arm."""
    bar_set = _bar_set(unit)
    c_arm, s_arm = keys.templates(unit)
    deg = next(b for b in bar_set if b.kind == "binomial_look")
    fis = next(b for b in bar_set if b.kind == "guard_fisher")
    ab = next(b for b in bar_set if b.kind == "guard_abs")
    con = [r for r in records if r["template"] == c_arm]
    sh = [r for r in records if r["template"] == s_arm]
    kc, ks = sum(_prepick(r) for r in con), sum(_prepick(r) for r in sh)
    res = [_bars.stage_end_eval(records, deg, look=look),
           fis.evaluate(kc, len(con), template=c_arm, look=look, sham_k=ks, sham_n=len(sh)),
           ab.evaluate(kc, len(con), template=c_arm, look=look)]
    # Reported beside (m:330 "reported on its contrast arms"): the contrast arm's
    # FORCED-round degeneracy only.
    # PIN (Code, declared at LOCK v0.1): its free-round events stay withheld at looks as
    # at gate stages (m:271: a free round's class sits on the pick) -- flagged for the
    # seat: whether m:271's withholding extends to campaign looks.
    forced = [x for r in con for x in r["rounds"] if x["phase"] == "forced"]
    kf = sum((x["audit"] or {}).get("claim") in _bars.DEGEN_CLAIMS[con[0]["substrate"]]
             for x in forced) if con else 0
    arms = {a: {"launched": len(g), "prepick_excluded": sum(_prepick(r) for r in g),
                "domain": sum(bool(r["domain"]) for r in g),
                "read_flags": _read_flags(g, first_only=(a == c_arm))}
            for a, g in ((c_arm, con), (s_arm, sh))}
    return {"look": look, "at_launches": len(records), "fired": any(r.fired for r in res),
            "results": [r.as_dict() for r in res], "arms": arms,
            "contrast_forced_degeneracy": {"k": int(kf), "n": len(forced)}}


def _pause_public(p: Mapping) -> dict:
    # PIN (Code, declared at LOCK v0.1): a pause reaches the pick-free report as {kind,
    # at_launches, adjudicated, adjudication_sha16}; the seat's (or the PI's) text stays
    # in the checkpoint only -- it may name anything, a pair label included.
    adj = p.get("adjudication")
    return {"kind": p["kind"], "at_launches": p["at_launches"], "adjudicated": adj is not None,
            "adjudication_sha16": _sha16_text(adj)}


def run_campaign(adapter, *, unit: str, floors: Mapping[str, int],
                 launch_counts: Mapping[str, int], hour_cap: Any,
                 prior_ckpt: str | os.PathLike | None,
                 ckpt_path: str | os.PathLike | None = None, resume: bool = False,
                 identity_extra: Mapping[str, Any], substrate: str,
                 out_root: str | os.PathLike = DEFAULT_OUT,
                 adjudication: str | None = None, pi_stop: str | None = None) -> dict:
    """A unit's campaign (m:192, m:247, m:250, m:330). Built and self-tested on the stub
    only at step 4.

    floors / launch_counts / hour_cap are the unit's LOCK v1.0 values, passed in;
    ``prior_ckpt`` is the unit's qualification checkpoint (it must have ended PASS);
    ``adjudication`` names the seat's ruling on the pending pause; ``pi_stop`` is the
    PI's stop (terminal, analyzed as obtained, m:247, m:316): recorded with its text in
    the checkpoint only, and nothing more launches. A checkpoint carrying an end pending
    is re-finished whatever ``resume`` says (finding R1); a paused campaign re-invoked
    with neither a ruling nor a stop re-derives its report and excerpt and stays paused
    (finding R6).
    """
    sub = _check_unit(unit, substrate)
    arms = list(keys.templates(unit))
    # PIN (Code, declared at LOCK v0.1): floors and launch counts are arguments taken from
    # the unit's LOCK v1.0, never hard-coded. "L is a projection, not a bound" (m:192,
    # m:48): the launch counts are recorded (checkpoint and report) as the projection
    # only; the identity's n is the committed campaign schedule's n (MAX_UNITS x 32,
    # m:159), and an arm launches until its DOMAIN count reaches its floor, the hour cap
    # is reached, its committed schedule is exhausted (a PAUSE for the PI), or a PI stop.
    fl = _per_arm(floors, arms, "floors")
    lc = _per_arm(launch_counts, arms, "launch_counts")
    if any(fl[a] > lc[a] for a in arms):
        raise ValueError(f"a floor exceeds its launch count: floors {fl}, launch counts {lc}")
    for nm, v in (("adjudication", adjudication), ("pi_stop", pi_stop)):
        if v is not None and not (isinstance(v, str) and v.strip()):
            raise ValueError(f"{nm} must be a non-empty text when given")
    name = stage_name(unit, "campaign")
    paths = out_paths(unit, "campaign", out_root)
    cpath = checkpoint_path(ckpt_path, paths)
    paths = for_checkpoint(paths, cpath)
    stub = _is_stub(adapter)
    extra = _extra(identity_extra, stage="campaign", sub=sub, stub=stub)
    # An ended (terminal or stopped) campaign is refused here, before the identity --
    # never with a restart-on-a-new-path advice (_begin -> resume.refuse_ended).
    prov = _begin(adapter, unit, "campaign", name, cpath, {**paths, "reads": None}, extra)
    prior = _licensed(adapter, unit, "campaign", name, extra, prior_ckpt)
    pool, _renders, rsha = _renders_of_record(extra, name)
    scheds = load_committed(unit, [("campaign", a) for a in arms], paths["schedules"])
    n_sched = {a: int(scheds[a]["n"]) for a in arms}
    if any(lc[a] > n_sched[a] for a in arms):
        raise ValueError(f"a launch count exceeds the committed schedule ({n_sched})")
    _bars.assert_firing_complete(_bar_set(unit), _bars.FIRING_CASES)
    setup, audit_sha, ban_sha = _startup(adapter, unit)
    bid = _resume.backend_identifier(adapter.provenance())
    path_cached = guard.cached_path_admitted(unit, "campaign", backend_identifier=bid)
    if path_cached and sub == "olmo":
        raise AssertionError("OLMo is uncached by spec (m:267)")
    if sub == "qwen":
        # PIN (Code, declared at LOCK v0.1; finding R3): where the campaign takes its path
        # from the G-ID licence, the artifact on disk is re-checked as the qualification
        # checked it -- under this run's proposal or one the lock re-adopts, and not
        # written on the stub for a non-stub run; an absent artifact gives the uncached
        # path (the licence's own reading) and has nothing to check.
        aprobs = gid_artifact_problems(
            unit, accepted=accepted_proposals(extra["proposal_sha256"], extra["prior_proposal_sha256s"]),
            require_real=not stub)
        if aprobs:
            raise SystemExit(f"{aprobs[0]} -- {name} does not take its path from it")
    path = _locked(name, extra, path_cached, cpath)
    refinish_only = path != ("cached" if path_cached else "uncached")
    ident = _identity(adapter, unit, "campaign", arms, path, n_sched, scheds, audit_sha, ban_sha,
                      extra, pool, rsha, hour_cap=hour_cap)
    # PIN (Code, declared at LOCK v0.1; finding R6): a paused campaign re-invoked with
    # neither the seat's adjudication nor the PI's stop is SHOWN its pause -- with or
    # without --resume -- never refused as existing: its report and excerpt are
    # re-derived from the checkpoint (no launch, no checkpoint change).
    show = adjudication is None and pi_stop is None and _paused_unadjudicated(cpath)
    ckpt = _resume.load_or_init(cpath, ident, resume or show)
    _refuse_stopped(ckpt, cpath)
    _record_prior(ckpt, prior, cpath)
    _record_licence(ckpt, extra, cpath)
    camp = ckpt.get("campaign")
    if camp is None:
        # PIN (Code, declared at LOCK v0.1): floors and the launch-count projection are
        # recorded in the checkpoint at the first write and must match on every resume
        # (both come from the lock whose hash the identity carries).
        camp = ckpt["campaign"] = {"floors": fl, "launch_counts_projection": lc, "pauses": [],
                                   "terminal": None, "end_look": None, "pi_stop": None}
    elif camp.get("floors") != fl or camp.get("launch_counts_projection") != lc:
        raise SystemExit(f"CHECKPOINT MISMATCH: floors / launch-count projection "
                         f"{camp.get('floors')} / {camp.get('launch_counts_projection')} recorded, "
                         f"{fl} / {lc} offered")
    if camp["terminal"] is not None:
        raise SystemExit(f"CAMPAIGN ENDED at {cpath} ({camp['terminal']['status']}); terminal (m:247)")
    # PIN (Code, declared at LOCK v0.1): the PI's stop is persisted in the checkpoint at
    # the invocation's first write (campaign.pi_stop), before the terminal state, which is
    # persisted last (after the report): a re-invocation after an interrupted finish
    # re-finishes the PI-STOP even when the stop is not offered again, and a DIFFERENT
    # stop text offered then is refused.
    rec_pi = camp.get("pi_stop")
    if pi_stop is not None and rec_pi is not None and pi_stop.strip() != rec_pi:
        raise SystemExit(f"CHECKPOINT MISMATCH: {cpath} records the PI's stop; this run offers a "
                         f"different text -- refusing")
    pending = _resume.pending_end(ckpt)
    if pending is not None:
        return _refinish_campaign(unit, name, ckpt, cpath, paths, prov, pending,
                                  adjudication=adjudication,
                                  pi_stop=pi_stop if rec_pi is None else None)
    if refinish_only:
        raise SystemExit(f"PATH MISMATCH ({name}): the end pending at {cpath} is gone -- refusing "
                         f"to launch on a path this backend's licence does not give (m:267, rule 2)")
    pi = pi_stop.strip() if pi_stop is not None else rec_pi
    if pi is not None and not ckpt["sessions"]:
        # PIN (Code, declared at LOCK v0.1): a PI stop ends a campaign that has launched;
        # a unit that never launches is NOT-RUN by its Clock (m:192), not stopped.
        raise SystemExit(f"PI STOP REFUSED at {cpath}: no session has launched -- a unit that "
                         f"never launches is NOT-RUN by its Clock (m:192), not PI-stopped")
    last = camp["pauses"][-1] if camp["pauses"] else None
    if last is not None and last["adjudication"] is None and adjudication is None and pi is None:
        return _show_pause(unit, name, ckpt, cpath, paths)
    camp["pi_stop"] = pi
    if last is not None and last["kind"] == "schedule_exhausted" and pi is None:
        # PIN (Code, declared at LOCK v0.1): an arm that exhausts its committed schedule
        # below its floor cannot launch again under this lock; only a PI stop ends the
        # campaign (terminal, analyzed as obtained) -- a resume with only an adjudication
        # is refused, never re-paused.
        raise SystemExit(f"SCHEDULE EXHAUSTED at {cpath}: {last.get('arm')} has no committed cell "
                         f"left below its floor; only the PI's stop (pi_stop) ends this campaign "
                         f"(m:192, m:247)")
    if last is not None and last["adjudication"] is None:
        # PIN (Code, declared at LOCK v0.1): a paused campaign resumes only with the
        # seat's adjudication named (recorded with the pause, checkpoint only), or ends by
        # the PI's stop, whose text then stands as the pause's ruling; Code never
        # self-adjudicates.
        last["adjudication"] = adjudication.strip() if adjudication is not None else pi
    elif adjudication is not None:
        raise SystemExit(f"NO PAUSE TO ADJUDICATE at {cpath}: the campaign is not paused")
    _append_provenance(ckpt, prov)
    cpath.parent.mkdir(parents=True, exist_ok=True)
    _resume.write_checkpoint(cpath, ckpt)
    records = ckpt["sessions"]
    launches = {a: sum(r["template"] == a for r in records) for a in arms}
    domain = {a: sum(bool(r["domain"]) for r in records if r["template"] == a) for a in arms}
    status = "PI-STOP" if pi is not None else None
    hit = pause = None
    rotation = _schedule.interleave(arms, lambda a: domain[a] >= fl[a], start_counts=dict(launches))
    while status is None:
        if _resume.hour_cap_exceeded(ckpt, hour_cap):
            status = "CAP"
            break
        arm = next(rotation, None)
        if arm is None:
            status = "COMPLETE"
            break
        s = launches[arm]
        if s >= n_sched[arm]:
            pause = {"at_launches": len(records), "kind": "schedule_exhausted", "arm": arm,
                     "adjudication": None}
            status = "PAUSE"
            break
        _resume.note_launch(ckpt)
        rec, problems = _launch(adapter, setup, unit, "campaign", arm, s, scheds[arm]["cells"][s],
                                path_cached=path_cached)
        if problems:
            hit = _verify_hit(arm, s, problems, rec)
            status = "STOP"
            break
        at = len(records) + 1
        look = campaign_look(unit, records + [rec], at // LOOK_EVERY) if at % LOOK_EVERY == 0 else None
        _resume.record_session(ckpt, rec, look=look)
        launches[arm] += 1
        domain[arm] += int(bool(rec["domain"]))
        hit = _hair_hit(rec)
        if hit is None:
            if look is not None and look["fired"]:
                # the look's pause ends the invocation: written with its session as the
                # pending end (finding R1), not here
                pause = {"at_launches": at, "kind": "look", "look": look["look"],
                         "bars": [r["name"] for r in look["results"] if r["fired"]],
                         "adjudication": None}
            else:
                _resume.write_checkpoint(cpath, ckpt)
        print(readrule.session_line(rec), flush=True)
        if hit is not None:
            status = "STOP"
            break
        if look is not None:
            if look["fired"]:
                # PIN (Code, declared at LOCK v0.1; round-3 verification): a FIRED look
                # announces itself only after its pending end is on disk (its messages go
                # to the finish's lines, _pause_lines) -- an announced PAUSE is never lifted
                # by a kill in the window; a silent look prints at once (its session and
                # look were written above).
                status = "PAUSE"
            else:
                for r in look["results"]:
                    print(r["message"], flush=True)
    pending, lines = _campaign_end(unit, name, ckpt, status, hit, pause, pi)
    return _complete_campaign(unit, name, ckpt, cpath, paths, pending, hit, lines)


def _paused_unadjudicated(cpath: Path) -> bool:
    """Is the campaign at ``cpath`` paused with its last pause unadjudicated (no end
    pending, not ended)? Read tolerantly; False when absent or unreadable."""
    if not Path(cpath).is_file():
        return False
    try:
        ck = json.loads(Path(cpath).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError):
        return False
    camp = ck.get("campaign") if isinstance(ck, dict) else None
    if (not isinstance(camp, dict) or _resume.pending_end(ck) is not None
            or _resume.ended_status(ck) is not None or not camp.get("pauses")):
        return False
    last = camp["pauses"][-1]
    return isinstance(last, dict) and last.get("adjudication") is None


def _campaign_end(unit: str, name: str, ckpt: Mapping, status: str | None, hit: Mapping | None,
                  pause: Mapping | None, pi: str | None) -> tuple[dict, list[str]]:
    """(the pending end, stdout lines) of a campaign invocation's end -- a hit (STOP) with
    its end look at the STOP point, a pause (a look, an exhausted schedule) or a terminal
    state with its end look."""
    camp, records = ckpt["campaign"], ckpt["sessions"]
    stop = terminal = end_look = None
    fired: list[str] = []
    lines: list[str] = []
    pause = copy.deepcopy(pause)
    if hit is not None:
        _, blinded = announce_stop(unit, "campaign", hit)
        stop, status = _stop_record(hit, blinded), "STOP"
        end_look, pause = _stop_end_look(unit, ckpt, hit)
        fired = [hit["bar"]] + list((pause or {}).get("bars") or [])
        # the finish and a re-finish announce the STOP's end from one source (_stop_lines)
        lines = _stop_lines(unit, name, ckpt, hit, end_look, pause)
    elif status in TERMINAL:
        n = len(records)
        if n == 0:
            raise AssertionError("a campaign cannot end terminal with no launch")
        terminal = {"status": status, "at_launches": n}
        if status == "PI-STOP":
            terminal["text"] = pi
        last_look = ckpt["looks"][-1] if ckpt["looks"] else None
        if n % LOOK_EVERY == 0 and last_look is not None and last_look["at_launches"] == n:
            # PIN (Code, declared at LOCK v0.1; the seat's C9(ii), 2026-10-10; m:330): Looks =
            # ceil(total launches / 40): when the campaign ends on a multiple of 40 the look
            # recorded there IS the end look -- no new evaluation, no new pause (its pause, if
            # it fired, was the seat's to adjudicate already). The end by STOP takes the same
            # rule (_stop_end_look).
            end_look = {**copy.deepcopy(last_look["result"]), "end_is_look": last_look["result"]["look"]}
        else:
            # PIN (Code, declared at LOCK v0.1; the seat's C9(ii), 2026-10-10; m:330): otherwise
            # the end look is evaluated once ("and at the end"); a fired end look pauses the
            # unit before its analysis (status PAUSE; the terminal state stands) -- at
            # COMPLETE, CAP and a PI stop alike, and at a STOP (_stop_end_look), where the
            # status stays STOP.
            end_look = campaign_look(unit, records, "end")
            if end_look["fired"]:
                pause = {"at_launches": n, "kind": "end_look", "look": "end",
                         "bars": [r["name"] for r in end_look["results"] if r["fired"]],
                         "adjudication": None}
                fired, status = list(pause["bars"]), "PAUSE"
        # the finish and a re-finish announce the end from one source (_pause_lines)
        lines = _pause_lines(name, ckpt, pause, end_look)
    elif status == "PAUSE" and pause is not None:
        fired = list(pause.get("bars") or [])
        lines = _pause_lines(name, ckpt, pause, None)
    else:
        raise AssertionError(f"a campaign invocation ended without an end ({status!r})")
    return ({"status": status, "fired": fired, "stop": stop, "terminal": terminal,
             "end_look": end_look, "pause": pause}, lines)


def _is_gver(hit: Mapping) -> bool:
    """A G-VER failure's hit (its record quarantined, never a session), not a hair trigger's."""
    return hit["bar"] in (_verify.MISMATCH, _verify.BREAK)


def _stop_end_look(unit: str, ckpt: Mapping, hit: Mapping) -> tuple[dict | None, dict | None]:
    """(the end look, the pause it raises or None) at a campaign STOP: the bars' cumulative
    counts evaluated at the STOP point as the campaign's last look (m:330; the seat's C9(ii),
    2026-10-10). Called once, at the finish (_campaign_end): the end look and pause it returns
    go into the pending end, and a re-finish never calls it again -- _refinish_campaign reuses
    the persisted end_pending block as it stands and re-derives only the lines (_stop_lines)
    and the outputs from it."""
    # PIN (Code, declared at LOCK v0.1; the seat's C9(ii), 2026-10-10; m:330): m:330's "at the
    # end" includes an end by STOP, so the end look is evaluated over the n = len(sessions)
    # launches recorded at the STOP point -- a hair trigger's session is recorded (with the
    # cadence look due at its launch), a G-VER failure's record is quarantined in the stop
    # block and never counted. n = 0 (a G-VER STOP at the first launch): no look (None). n a
    # multiple of 40 with the look recorded at n: that look IS the end look ({**result,
    # end_is_look: k}, as the terminal branch builds it) -- after a G-VER STOP it was announced
    # at the launch that reached n and any pause it raised was adjudicated before the next
    # launch, so no new pause; after a hair trigger at the launch that reached n the hit
    # pre-empted both its announcement and its pause, so its pause (kind "look", look k) is
    # raised here if it fired. Otherwise the end look is evaluated once (campaign_look(...,
    # "end")) and, if it fired, raises an "end_look" pause. The status stays STOP and the stop
    # block is unchanged. A pause raised here is never adjudicated through stages -- the
    # stopped checkpoint is ended (resume.refuse_ended) -- its adjudication enters VERDICTS as
    # the declared --adjudication file (the seat's C9(i), C3). campaign_look is pick-free by
    # construction (sham-arm degeneracy, pooled pre-pick (forced-phase) exclusion counts, the
    # contrast arm's forced-round degeneracy, first-read flags): nothing in it reads a contrast
    # session's free rounds or its free-phase events, so a contrast free-phase trigger's
    # withheld class reaches the end look nowhere (m:318 exception (1); ruling (h)).
    records = ckpt["sessions"]
    n = len(records)
    gver = _is_gver(hit)
    ids = [(r["template"], r["s"]) for r in records]
    if gver and (hit["template"], hit["s"]) in ids:
        raise AssertionError("a G-VER STOP's record is quarantined in the stop block, never a session")
    if not gver and (not ids or ids[-1] != (hit["template"], hit["s"])):
        raise AssertionError("a hair-trigger STOP's session is the last one recorded")
    if n == 0:
        return None, None
    last_look = ckpt["looks"][-1] if ckpt["looks"] else None
    if n % LOOK_EVERY == 0 and last_look is not None and last_look["at_launches"] == n:
        res = last_look["result"]
        end_look = {**copy.deepcopy(res), "end_is_look": res["look"]}
        if gver or not res["fired"]:
            return end_look, None
        return end_look, {"at_launches": n, "kind": "look", "look": res["look"],
                          "bars": [r["name"] for r in res["results"] if r["fired"]], "adjudication": None}
    end_look = campaign_look(unit, records, "end")
    if not end_look["fired"]:
        return end_look, None
    return end_look, {"at_launches": n, "kind": "end_look", "look": "end",
                      "bars": [r["name"] for r in end_look["results"] if r["fired"]], "adjudication": None}


def _stop_lines(unit: str, name: str, ckpt: Mapping, hit: Mapping, end_look: Mapping | None,
                pause: Mapping | None) -> list[str]:
    """The stdout lines that announce a campaign STOP's end, from the hit and the pending end's
    end look and pause (and the checkpoint), so the finish and a re-finish print the same lines:
    the STOP's announcement (announce_stop), then its end look's."""
    # PIN (Code, declared at LOCK v0.1; the seat's C9(ii), 2026-10-10): the end look's lines
    # follow the STOP's: the END LOOK line where the end look is the look a G-VER STOP's last
    # recorded launch already announced (never its messages again, as at a terminal end on a
    # multiple of 40); otherwise the end look's bar messages -- a look the hair trigger
    # pre-empted, or the end look evaluated at the STOP -- printed once, a fired one included.
    lines = list(announce_stop(unit, "campaign", hit)[0])
    if end_look is None:
        return lines
    if "end_is_look" in end_look and _is_gver(hit):
        if pause is not None:
            raise AssertionError("a G-VER STOP raises no pause on a look already announced")
        return lines + _pause_lines(name, ckpt, None, end_look)
    return lines + [r["message"] for r in end_look["results"]]


def _camp_n(ckpt: Mapping, arm: str) -> int:
    """An arm's committed schedule n (the identity's)."""
    return int(ckpt["identity"]["n"][arm])


def _pause_lines(name: str, ckpt: Mapping, pause: Mapping | None, end_look: Mapping | None) -> list[str]:
    """The stdout lines that announce a campaign pause or terminal end, derived from the
    checkpoint so a re-finish prints them again: a look's bar messages (the look recorded
    with its session), an exhausted schedule's PAUSE line, the end look's messages, or --
    where the end look IS the look recorded at the last launch -- the END LOOK line (that
    look's messages were printed at the look; reprinting them would re-announce a bar the
    seat has already adjudicated)."""
    if pause is None:
        if end_look is None:
            return []
        if "end_is_look" in end_look:
            return [f"END LOOK {name}: the end look is look {end_look['end_is_look']} "
                    f"(at {end_look['at_launches']} launches)"]
        return [r["message"] for r in end_look["results"]]
    if pause["kind"] == "look":
        looks = {lk["result"]["look"]: lk["result"] for lk in ckpt["looks"]}
        return [r["message"] for r in looks[pause["look"]]["results"]]
    if pause["kind"] == "schedule_exhausted":
        return [f"PAUSE {name}: {pause['arm']} exhausted its committed schedule "
                f"({_camp_n(ckpt, pause['arm'])}) below its floor; the PI decides (m:192, m:247)"]
    if pause["kind"] == "end_look" and end_look is not None:
        return [r["message"] for r in end_look["results"]]
    return []


def _campaign_report(unit: str, name: str, ck: Mapping, cpath: Path, paths: Mapping, status: str,
                     stop_block: Mapping | None) -> dict:
    """The campaign's pick-free report, a pure function of the checkpoint (the end's
    persisted form) and its status -- so a re-finish or a shown pause re-derives it byte
    for byte."""
    ident, camp, records = ck["identity"], ck["campaign"], ck["sessions"]
    arms = list(keys.templates(unit))
    launches = {a: sum(r["template"] == a for r in records) for a in arms}
    domain = {a: sum(bool(r["domain"]) for r in records if r["template"] == a) for a in arms}
    end_look = camp["end_look"]
    looks_count = len(ck["looks"]) + int(end_look is not None and "end_is_look" not in end_look)
    s_arm = arms[1]
    # PIN (Code, declared at LOCK v0.1): the campaign writes its checkpoint and a pick-free
    # report (looks with pooled pre-pick exclusion, domain and read-flag counts per arm,
    # pauses without their texts, the terminal status, whether the hour cap is reached and
    # the SHAM arm's generation ms -- a total that includes contrast sessions stays in the
    # checkpoint, m:318, build design §0 rule 5) and NO reads file and no first-pick share:
    # §4's exception (2) covers the gate stages only, and the campaign's reads are the
    # VERDICTS entry's (m:318).
    return {"schema": REPORT_SCHEMA, "form": "pick-free campaign report (m:318: at looks, pooled "
                                             "pre-pick exclusion counts per arm)",
            "unit": unit, "stage": "campaign", "stage_name": name, "status": status,
            "floors": dict(camp["floors"]), "launch_counts_projection": dict(camp["launch_counts_projection"]),
            "schedule_n": {a: _camp_n(ck, a) for a in arms},
            "hour_cap": ident["hour_cap"],
            "hour_cap_reached": bool(_resume.hour_cap_exceeded(ck, ident["hour_cap"])),
            "sham_generation_ms": sum(_resume.session_ms(r) for r in records if r["template"] == s_arm),
            "arms": {a: {"launched": launches[a], "domain": domain[a],
                         "prepick_excluded": sum(_prepick(r) for r in records if r["template"] == a)}
                     for a in arms},
            "looks": [lk["result"] for lk in ck["looks"]], "looks_count": looks_count,
            "end_look": end_look, "pauses": [_pause_public(p) for p in camp["pauses"]],
            "terminal": ({k: camp["terminal"][k] for k in ("status", "at_launches")}
                         if camp["terminal"] else None),
            "stop": copy.deepcopy(stop_block), "identity": _ident_summary(ident),
            "provenance": _resume.report_provenance(ck),
            "files": {"checkpoint": _rel(cpath, paths["root"])}}


def _campaign_outputs(unit: str, name: str, ck: Mapping, cpath: Path, paths: Mapping, status: str,
                      hit: Mapping | None) -> tuple[dict, dict | None, Path]:
    """(report, excerpt or None, the excerpt's path), built from the checkpoint and
    asserted pick-free; nothing written."""
    stop_block = ck["stop"]["blinded"] if ck.get("stop") else None
    report = _campaign_report(unit, name, ck, cpath, paths, status, stop_block)
    # The campaign's excerpt holds one event per pause and its stop, rebuilt from its
    # state, so it always matches the checkpoint.
    events = _campaign_events(ck, hit)
    apath = adjudication_path(cpath)
    if events:
        report["files"]["adjudication"] = _rel(apath, paths["root"])
    _assert_pick_free(report, name)
    adj = _adjudication_doc(unit, "campaign", name, cpath, paths["root"], events) if events else None
    return report, adj, apath


def _write_campaign_outputs(paths: Mapping, report: Mapping, adj: Mapping | None, apath: Path) -> Path | None:
    _write_json(paths["report"], report)
    if adj is not None:
        _write_json(apath, adj)
        return apath
    _remove_stale(apath)
    return None


def _campaign_done(name: str, ck: Mapping, cpath: Path, paths: Mapping, status: str,
                   apath: Path | None, lines: Sequence[str]) -> dict:
    for ln in lines:
        print(ln, flush=True)
    print(_stage_line(name, status, ck["identity"]["path"]), flush=True)
    outs = [("CHECKPOINT", cpath), ("REPORT", paths["report"])]
    if apath is not None:
        outs.append(("ADJUDICATION", apath))
    for k, p in outs:
        print(f"{k} {p}", flush=True)
    arms = list(ck["identity"]["template_set"])
    return {"status": status, "stage_name": name, "checkpoint": cpath, "report": paths["report"],
            "launches": {a: sum(r["template"] == a for r in ck["sessions"]) for a in arms},
            "domain": {a: sum(bool(r["domain"]) for r in ck["sessions"] if r["template"] == a)
                       for a in arms},
            "adjudication": apath}


def _complete_campaign(unit: str, name: str, ckpt: dict, cpath: Path, paths: Mapping,
                       pending: Mapping, hit: Mapping | None, lines: Sequence[str]) -> dict:
    """A campaign finish after its end is pending (finding R1): the outputs from the
    end's persisted form, then the end persisted."""
    # PIN (Code, declared at LOCK v0.1): as at the gate stages, a campaign's stop, pause
    # or terminal state is computed in memory, written as end_pending with every session,
    # its report and adjudication excerpt written, and only then persisted (findings N7,
    # N10, N14, R1).
    final, first = _pend(ckpt, cpath, pending, name)
    report, adj, apath = _campaign_outputs(unit, name, final, cpath, paths, pending["status"], hit)
    if first:
        _write_pending(cpath, ckpt, final)
    written = _write_campaign_outputs(paths, report, adj, apath)
    _resume.persist_end(cpath, final)
    return _campaign_done(name, final, cpath, paths, pending["status"], written, lines)


def _refinish_campaign(unit: str, name: str, ckpt: dict, cpath: Path, paths: Mapping, prov: Mapping,
                       pending: Mapping, *, adjudication: str | None, pi_stop: str | None) -> dict:
    """Re-finish a campaign's pending end (finding R1): nothing launches. A ruling this
    invocation offers (the seat's adjudication, a PI stop the checkpoint does not record)
    is NOT applied to an end it has not yet shown: the re-finish completes, then the
    invocation refuses, naming what it did not apply -- and, where the end it re-finished
    leaves the campaign ended (a STOP, or a terminal state beside a fired end look's pause),
    where that ruling enters instead."""
    # PIN (Code, declared at LOCK v0.1; finding R1): "re-finish-only at any invocation" --
    # an invocation offering a ruling re-finishes the pending end first and then exits
    # non-zero (NOT APPLIED); the ruling is offered again on the next invocation -- unless
    # the re-finished end leaves the campaign ended (its stop or terminal state persisted:
    # resume.ended_status non-None), which stages never resumes (resume.refuse_ended).
    # PIN (Code, declared at LOCK v0.1; the seat's C9(i), C3 and C2, 2026-10-10): there the
    # refusal does not say "offer it again" -- a ruling on the ended campaign's pause enters
    # VERDICTS as the declared --adjudication file, a PI's stop on a hair trigger as the
    # declared --pi-stop record; stages records neither.
    _append_provenance(ckpt, prov)
    _resume.write_checkpoint(cpath, ckpt)
    print(_refinish_line(name, pending["status"], cpath), flush=True)
    hit = _hit_from_stop(pending["stop"])
    lines = (_stop_lines(unit, name, ckpt, hit, pending.get("end_look"), pending.get("pause"))
             if hit is not None else _pause_lines(name, ckpt, pending.get("pause"), pending.get("end_look")))
    res = _complete_campaign(unit, name, ckpt, cpath, paths, pending, hit, lines)
    skipped = [w for w, v in (("the seat's adjudication", adjudication), ("the PI's stop", pi_stop))
               if v is not None]
    ended = ("STOP" if pending.get("stop") is not None
             else (pending.get("terminal") or {}).get("status"))
    if skipped and ended is not None:
        raise SystemExit(f"NOT APPLIED ({name}): this invocation re-finished the end pending at "
                         f"{cpath} ({pending['status']}); {' and '.join(skipped)} it offered was not "
                         f"applied, and cannot be through stages: that end leaves the campaign ended "
                         f"({ended}), never resumed (resume.refuse_ended) -- a ruling on a pause it "
                         f"carries enters VERDICTS as the declared --adjudication file, a PI's stop on a hair "
                         f"trigger as the declared --pi-stop record (the seat's C9(i), C3, C2)")
    if skipped:
        raise SystemExit(f"NOT APPLIED ({name}): this invocation re-finished the end pending at "
                         f"{cpath} ({pending['status']}); {' and '.join(skipped)} it offered was not "
                         f"applied -- offer it again (Code never applies a ruling to an end it has "
                         f"not yet shown)")
    return res


def _show_pause(unit: str, name: str, ckpt: Mapping, cpath: Path, paths: Mapping) -> dict:
    """A paused campaign re-invoked without a ruling (finding R6): its report and excerpt
    re-derived from the checkpoint and written; nothing launched; the checkpoint
    unchanged (no provenance entry either); the PAUSE status returned (exit 3)."""
    last = ckpt["campaign"]["pauses"][-1]
    report, adj, apath = _campaign_outputs(unit, name, ckpt, cpath, paths, "PAUSE", None)
    apath = _write_campaign_outputs(paths, report, adj, apath)
    tail = ("only the PI's stop (pi_stop) ends it (m:192, m:247)" if last["kind"] == "schedule_exhausted"
            else "a resume needs the seat's adjudication (m:330) or the PI's stop; Code never "
                 "self-adjudicates")
    line = (f"PAUSE {name}: the campaign at {cpath.name} is paused ({last['kind']}, at "
            f"{last['at_launches']} launches); its report and excerpt are re-derived from the "
            f"checkpoint, nothing launched; {tail}")
    return _campaign_done(name, ckpt, cpath, paths, "PAUSE", apath, [line])


def _campaign_events(ckpt: Mapping, hit: Mapping | None) -> list[dict]:
    """The campaign's adjudication events, rebuilt from its state: one per pause (counts
    only -- a look's or the end look's results and arm counts, or an exhausted arm's
    counts), and the hair-trigger / G-VER stop's fired round when there is one -- a pause
    raised at the STOP point (the seat's C9(ii)) gives its PAUSE event before the STOP's."""
    camp, records = ckpt["campaign"], ckpt["sessions"]
    fl = camp["floors"]
    looks = {lk["result"]["look"]: lk["result"] for lk in ckpt["looks"]}
    events: list[dict] = []
    for p in camp["pauses"]:
        ev: dict = {"event": "PAUSE", "kind": p["kind"], "at_launches": p["at_launches"],
                    "bars": list(p.get("bars") or [])}
        if p["kind"] == "look":
            ev["counts"] = copy.deepcopy(looks.get(p["look"]))
        elif p["kind"] == "end_look":
            ev["counts"] = copy.deepcopy(camp["end_look"])
        else:
            arm = p["arm"]
            upto = [r for r in records[:p["at_launches"]] if r["template"] == arm]
            ev["counts"] = {"arm": arm, "floor": fl[arm], "schedule_n": _camp_n(ckpt, arm),
                            "launched": len(upto), "domain": sum(bool(r["domain"]) for r in upto)}
        ev["picks_revealed"] = []
        events.append(ev)
    if hit is not None:
        events.append({**_hit_event(records, hit), "at_launches": len(records)})
    return events


# --- self-test helpers (selftests only; production code never calls them) ------------
class _Interrupt(RuntimeError):
    """A simulated crash inside a session: the checkpoint keeps what was written."""


def _script_policy(unit: str, stage: str, cells: Mapping[tuple[str, int], Mapping],
                   rule: Callable[[str, int, int, dict], str | None] | None = None,
                   interrupt: Callable[[str, int, int, dict], bool] | None = None) -> Callable[[dict], str]:
    """A ScriptedAdapter texts-callable addressing every generation as (template, s, n):
    the arm rng's draws are replayed (4 seeds; then per choice one menu draw and one
    seed, m:159's order), so a call's seed names its session and round. ``rule`` may
    return a text with {Pc}/{Qc}/{COMMON}/{TOLD} fields, or None for a clean answer."""
    from . import testing
    smap: dict[int, tuple[str, int, int]] = {}
    fills: dict[tuple[str, int], dict] = {}
    for (t, s), cell in cells.items():
        rng = keys.stream(keys.arm_key(unit, stage, t, s))
        seeds = [int(rng.integers(2**31)) for _ in range(_sc.N_FORCED)]
        for _ in range(_sc.N_FREE):
            rng.integers(2)
            seeds.append(int(rng.integers(2**31)))
        for n, seed in enumerate(seeds, 1):
            if seed in smap:
                raise AssertionError("selftest policy: two rounds share a seed")
            smap[seed] = (t, s, n)
        _, lines = _banner.build_banner(t, cell["P"], cell["Q"], cell["clause"])
        fills[(t, s)] = {"Pc": cell["P"].capitalize(), "Qc": cell["Q"].capitalize(),
                         "COMMON": lines[0], "TOLD": lines[1]}

    def texts(call: dict) -> str:
        t, s, n = smap[call["seed"]]
        if interrupt is not None and interrupt(t, s, n, call):
            raise _Interrupt(f"selftest interrupt at {t} s={s} round {n}")
        x = rule(t, s, n, call) if rule is not None else None
        if x is None:
            x = testing.CLEAN[(n - 1 + s) % len(testing.CLEAN)]
        return x.format(**fills[(t, s)])
    return texts


def _selftest(chk) -> None:
    import contextlib
    import io
    import sys
    import tempfile

    from . import testing

    rsha = _corr.renders_sha(_sc.pool_and_renders()[1])

    def xtra(lp: str | None = "uncached", **over) -> dict:
        d = {"lock_sha256": "1" * 64, "proposal_sha256": "2" * 64, "renders_sha16": rsha}
        if lp is not None:
            d["locked_path"] = lp
        d.update(over)
        return d

    def refuses(fn, exc=SystemExit, needle: str = "") -> bool:
        try:
            fn()
            return False
        except exc as e:
            return needle in str(e)

    @contextlib.contextmanager
    def patched(mod, attr: str, value):
        saved = getattr(mod, attr)
        setattr(mod, attr, value)
        try:
            yield
        finally:
            setattr(mod, attr, saved)

    me = sys.modules[__name__]

    class _Done:
        def __init__(self, rc: int, out: Any = "", err: Any = "") -> None:
            self.returncode, self.stdout, self.stderr = rc, out, err
    git_calls: list[tuple] = []

    def fake_git(missing=(), symlink=(), tree=(), blobs=None, head="ab" * 20, head_ok=True):
        # read-only git answered from the working tree (selftest only): a path is committed
        # at HEAD with the working tree's bytes unless it is absent there, named missing /
        # symlink / tree, or given other blob bytes; any other git call fails the check
        blobs = dict(blobs or {})

        def g(*args, repo=REPO, binary=False):
            git_calls.append(args)
            rel = args[2].split(":", 1)[1] if args[:1] == ("cat-file",) else args[-1]
            gone = rel in missing or (rel not in blobs and not (Path(repo) / rel).exists())
            if args[:2] == ("rev-parse", "--verify"):
                return _Done(0, head + "\n") if head_ok else _Done(128, "", "fatal: Needed a single revision")
            if args[:2] == ("cat-file", "-e"):
                return _Done(128, "", "fatal: path does not exist in 'HEAD'") if gone else _Done(0)
            if args[:3] == ("ls-tree", "-z", "HEAD"):
                if gone:
                    return _Done(0, "")
                mode, typ = (("120000", "blob") if rel in symlink else ("040000", "tree") if rel in tree
                             else ("100644", "blob"))
                return _Done(0, f"{mode} {typ} {'0' * 40}\t{rel}\0")
            if args[:2] == ("cat-file", "blob"):
                data = blobs[rel] if rel in blobs else (Path(repo) / rel).read_bytes()
                return _Done(0, data if binary else data.decode("utf-8"))
            raise AssertionError(f"selftest: an unexpected git call {args}")
        return g

    # names, paths, refusals
    chk("stages: stage names are the spec's (G-TIME-F0, G-ID-F0m, G-F0m-Qwen, OLMo time/qual)",
        [stage_name("Q-F0", s) for s in ("time", "id", "qual", "campaign")]
        == ["G-TIME-F0", "G-ID-F0m", "G-F0m-Qwen", "campaign-Q-F0"]
        and stage_name("OLMo-dpo", "time") == "G-TIME-OLMo-dpo"
        and stage_name("OLMo-sft", "qual") == "G-F0m-OLMo-sft")
    refused = []
    for fn, exc in ((lambda: stage_name("OLMo-sft", "id"), ValueError),
                    (lambda: _check_unit("Q-F3"), NotImplementedError),
                    (lambda: _check_unit("OLMo-base"), ValueError),
                    (lambda: _check_unit("Q-F0", "olmo"), ValueError),
                    (lambda: run_gate_stage(None, unit="Q-F3", gate="time", templates_counts=[],
                                            identity_extra={}, substrate="qwen"), NotImplementedError),
                    (lambda: run_gid_pair(None, unit="OLMo-sft", identity_extra={}, prior_ckpt=None),
                     ValueError)):
        try:
            fn()
            refused.append(False)
        except exc:
            refused.append(True)
    chk("stages: refusals (no G-ID on OLMo; Q-F3 NotImplementedError; base; substrate mismatch)",
        all(refused), refused)
    p = out_paths("Q-F0", "qual", "/x/m")
    chk("stages: declared output paths (ckpt/, reports/ _report and _reads, schedules/)",
        (str(p["ckpt"]), str(p["report"]), str(p["reads"]), str(p["schedules"]))
        == ("/x/m/ckpt/Q-F0_qual.json", "/x/m/reports/Q-F0_qual_report.json",
            "/x/m/reports/Q-F0_qual_reads.json", "/x/m/schedules"))
    pc = for_checkpoint(p, Path("/x/m/ckpt/Q-F0_qual.podB.json"))
    pd = for_checkpoint(p, Path("/x/m/ckpt/Q-F0_qual.json"))
    chk("stages: the report and reads are named after the resolved checkpoint's stem (finding R10) -- a "
        "restart name gets its own; the default checkpoint keeps {unit}_{stage}'s names",
        (str(pc["report"]), str(pc["reads"])) == ("/x/m/reports/Q-F0_qual.podB_report.json",
                                                  "/x/m/reports/Q-F0_qual.podB_reads.json")
        and (pd["report"], pd["reads"]) == (p["report"], p["reads"]), str(pc["report"]))
    chk("stages: exit codes -- PASS/COMPLETE/CAP/PI-STOP 0, every seat/PI outcome non-zero",
        [exit_code(s) for s in ("PASS", "COMPLETE", "CAP", "PI-STOP")] == [0, 0, 0, 0]
        and all(exit_code(s) != 0 for s in ("PAUSE", "STOP", "FAIL", "NOT-DETERMINED")))

    # identity_extra: exactly {lock, proposal, locked_path, renders}; never "pre-lock"
    bad_extra = {
        "a fifth key": (lambda: _extra(xtra(path="cached"), stage="qual", sub="qwen")),
        "lock 'pre-lock'": (lambda: _extra(xtra(lock_sha256="pre-lock"), stage="qual", sub="qwen")),
        "proposal 'pre-lock'": (lambda: _extra(xtra(proposal_sha256="pre-lock"), stage="time",
                                               sub="qwen")),
        "upper-case lock hex": (lambda: _extra(xtra(lock_sha256="A" * 64), stage="qual", sub="qwen")),
        "no renders sha": (lambda: _extra({k: v for k, v in xtra().items() if k != "renders_sha16"},
                                          stage="qual", sub="qwen")),
        "no locked_path (qual)": (lambda: _extra(xtra(None), stage="qual", sub="qwen")),
        "a locked_path at G-ID": (lambda: _extra(xtra("uncached"), stage="id", sub="qwen")),
        "G-TIME locked cached": (lambda: _extra(xtra("cached"), stage="time", sub="qwen")),
        "OLMo locked cached": (lambda: _extra(xtra("cached"), stage="qual", sub="olmo")),
        "locked_path 'both'": (lambda: _extra(xtra("both"), stage="campaign", sub="qwen")),
    }
    bad_extra.update({
        "prior proposals not a list": (lambda: _extra(xtra(prior_proposal_sha256s="9" * 64), stage="qual",
                                                      sub="qwen")),
        "a short prior proposal": (lambda: _extra(xtra(prior_proposal_sha256s=["9" * 16]), stage="qual",
                                                  sub="qwen")),
        "a repeated prior proposal": (lambda: _extra(xtra(prior_proposal_sha256s=["9" * 64, "9" * 64]),
                                                     stage="qual", sub="qwen")),
        "its own proposal as a prior": (lambda: _extra(xtra(prior_proposal_sha256s=["2" * 64]), stage="qual",
                                                       sub="qwen")),
        "an analyzer sha of 16 hex": (lambda: _extra(xtra(analyzer_sha256="a" * 16), stage="qual", sub="qwen")),
        "a package sha of 16 hex": (lambda: _extra(xtra(package_sha256="b" * 16), stage="qual", sub="qwen")),
        "a proposal file walking out": (lambda: _extra(xtra(proposal_file="../P.md"), stage="qual", sub="qwen")),
        "an absolute proposal file": (lambda: _extra(xtra(proposal_file="/P.md"), stage="qual", sub="qwen")),
        "no proposal file, non-stub": (lambda: _extra(xtra(lock_file="L.md"), stage="qual", sub="qwen",
                                                      stub=False)),
    })
    let = [nm for nm, fn in bad_extra.items() if not refuses(fn, exc=ValueError)]
    defaults = {"lock_file": None, "proposal_file": PROPOSAL_REL, "prior_proposal_sha256s": [],
                "analyzer_sha256": None, "package_sha256": None}
    good = (_extra(xtra("cached"), stage="qual", sub="qwen")["locked_path"] == "cached"
            and _extra(xtra(None), stage="id", sub="qwen") == {**{k: v for k, v in xtra().items()
                                                                  if k != "locked_path"}, **defaults}
            and _extra(xtra(), stage="campaign", sub="olmo")["locked_path"] == "uncached"
            and _extra(xtra(prior_proposal_sha256s=("9" * 64, "8" * 64), analyzer_sha256="a" * 64,
                            package_sha256="b" * 64, proposal_file="archive/P.md"), stage="qual", sub="qwen")
            == {**xtra(), "lock_file": None, "proposal_file": "archive/P.md",
                "prior_proposal_sha256s": ["8" * 64, "9" * 64], "analyzer_sha256": "a" * 64,
                "package_sha256": "b" * 64})
    chk(f"stages: identity_extra is lock/proposal (64 hex, 'pre-lock' refused), locked_path and "
        f"renders_sha16 (G-ID: no locked_path) plus the optional lock_file / proposal_file (proposal_file "
        f"REQUIRED on a non-stub run, the v1_11 default on the stub only), prior_proposal_sha256s (distinct, "
        f"never its own; recorded sorted), analyzer_sha256 and package_sha256 -- {len(bad_extra)} malformed "
        f"refused, valid accepted", not let and good, let)
    # the seat's D2 (2026-10-10): analyzer_sha256 and package_sha256 REQUIRED on a non-stub run, as the
    # files are; optional (None) on the stub, form-checked wherever given
    d2_full = xtra(proposal_file=PROPOSAL_REL, lock_file="locks/L.md", analyzer_sha256="a" * 64,
                   package_sha256="b" * 64)
    d2_bad = {"no analyzer_sha256": ({k: v for k, v in d2_full.items() if k != "analyzer_sha256"},
                                     "must carry analyzer_sha256"),
              "no package_sha256": ({k: v for k, v in d2_full.items() if k != "package_sha256"},
                                    "must carry package_sha256"),
              "neither": ({k: v for k, v in d2_full.items() if k not in ("analyzer_sha256", "package_sha256")},
                          "must carry analyzer_sha256"),
              "an upper-case analyzer sha": ({**d2_full, "analyzer_sha256": "A" * 64}, "analyzer_sha256 must be"),
              "a package sha of 63 hex": ({**d2_full, "package_sha256": "b" * 63}, "package_sha256 must be"),
              "a non-str package sha": ({**d2_full, "package_sha256": 7}, "package_sha256 must be"),
              "a non-hex analyzer sha": ({**d2_full, "analyzer_sha256": "g" * 64}, "analyzer_sha256 must be"),
              # 64 characters that are not 64 lower-case hex, for the package key as for the analyzer's
              "a non-hex package sha": ({**d2_full, "package_sha256": "g" * 64}, "package_sha256 must be"),
              "an upper-case package sha": ({**d2_full, "package_sha256": "B" * 64}, "package_sha256 must be")}
    d2_let = [nm for nm, (x_, nd) in d2_bad.items()
              if not refuses(lambda x_=x_: _extra(x_, stage="time", sub="qwen", stub=False), exc=ValueError,
                             needle=nd)]
    d2_stub_absent = _extra({k: v for k, v in d2_full.items() if k not in ("analyzer_sha256", "package_sha256")},
                            stage="time", sub="qwen", stub=True)
    d2_stub_cases = ("a non-hex analyzer sha", "an upper-case analyzer sha", "a non-hex package sha",
                     "an upper-case package sha", "a package sha of 63 hex")
    d2_stub_bad = [nm for nm in d2_stub_cases
                   if not refuses(lambda nm=nm: _extra(d2_bad[nm][0], stage="time", sub="qwen", stub=True),
                                  exc=ValueError, needle=d2_bad[nm][1])]
    d2_ok = _extra(d2_full, stage="time", sub="qwen", stub=False)
    chk(f"stages: the seat's D2 -- on a non-stub run identity_extra must carry analyzer_sha256 and "
        f"package_sha256 (each absent, both absent, and {len(d2_bad) - 3} malformed forms refused, ValueError "
        f"naming the key; for each key, 64 characters that are not lower-case hex -- 'g'*64 and upper-case "
        f"hex -- among them); both given are accepted and carried; on the stub both may be absent (None) and a "
        f"malformed one is still refused ({len(d2_stub_cases)} forms, those 64-character ones for both keys)",
        not d2_let and not d2_stub_bad and d2_ok["analyzer_sha256"] == "a" * 64
        and d2_ok["package_sha256"] == "b" * 64
        and (d2_stub_absent["analyzer_sha256"], d2_stub_absent["package_sha256"]) == (None, None),
        (d2_let, d2_stub_bad))
    chk("stages: the renders sha16 must be the renders of record built here (a mismatch refuses)",
        refuses(lambda: _renders_of_record(xtra(renders_sha16="0" * 16), "G-TIME-F0"),
                needle="RENDERS MISMATCH")
        and _renders_of_record(xtra(), "G-TIME-F0")[2] == rsha, rsha)
    chk("stages: the run's path must be the locked one, in either direction (PATH MISMATCH)",
        refuses(lambda: _locked("G-F0m-Qwen", xtra("cached"), False), needle="PATH MISMATCH")
        and refuses(lambda: _locked("G-F0m-Qwen", xtra("uncached"), True), needle="PATH MISMATCH")
        and _locked("G-F0m-Qwen", xtra("cached"), True) == "cached"
        and _locked("G-F0m-Qwen", xtra("uncached"), False) == "uncached")
    # ... except where the checkpoint carries an end pending (a re-finish launches nothing)
    with tempfile.TemporaryDirectory() as td:
        cps = {nm: Path(td) / f"{nm}.json" for nm in ("pending", "none", "null", "unreadable", "absent")}
        cps["pending"].write_text(json.dumps({"end_pending": {"status": "PASS"}}), encoding="utf-8")
        cps["none"].write_text(json.dumps({"sessions": []}), encoding="utf-8")
        cps["null"].write_text(json.dumps({"end_pending": None}), encoding="utf-8")
        cps["unreadable"].write_text("{truncated", encoding="utf-8")
        lk_out: dict[str, Any] = {}

        def lk(lp: str, admitted: bool, cp: Path) -> tuple[Any, str]:
            # (_locked's return or what it raised, what it printed)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                try:
                    got = _locked("G-F0m-Qwen", xtra(lp), admitted, cp)
                except (SystemExit, Exception) as e:          # noqa: BLE001 (recorded, not raised)
                    got = e
            return got, buf.getvalue()
        for lp, admitted in (("cached", False), ("uncached", True)):
            got, out = lk(lp, admitted, cps["pending"])
            lk_out[f"{lp} lock, pending"] = (got == lp and out.startswith("PATH (G-F0m-Qwen): ")
                                             and "re-finishes" in out and out.count("\n") == 1)
        for nm in ("none", "null", "unreadable", "absent"):
            got, out = lk("cached", False, cps[nm])
            lk_out[f"cached lock, {nm}"] = (isinstance(got, SystemExit) and "PATH MISMATCH" in str(got)
                                            and out == "")
        got, out = lk("cached", True, cps["pending"])
        lk_out["matching path, pending: no PATH line"] = got == "cached" and out == ""
    chk("stages: a path mismatch with an end pending at the checkpoint returns the LOCKED path (one PATH "
        "line; the drivers then only re-finish); with no end pending there (no block, a null one, an "
        "unreadable or absent file) it is still PATH MISMATCH, nothing printed; a matching path prints "
        "nothing", all(lk_out.values()), {k: v for k, v in lk_out.items() if not v})

    # the checkpoint path is <out_root>/ckpt/<name>.json (the -diff rule)
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "m"
        pp = out_paths("OLMo-sft", "campaign", root)
        bad_paths = {"under reports/": root / "reports" / "OLMo-sft_campaign_podB.json",
                     "a ckpt/ subdirectory": root / "ckpt" / "podB" / "x.json",
                     "the out_root itself": root / "x.json", "not .json": root / "ckpt" / "x.txt",
                     "a .. walk out of ckpt/": root / "ckpt" / ".." / "reports" / "x.json"}
        let = [nm for nm, q in bad_paths.items()
               if not refuses(lambda q=q: checkpoint_path(q, pp), needle="CHECKPOINT PATH REFUSED")]
        ok_paths = (checkpoint_path(None, pp) == (root / "ckpt" / "OLMo-sft_campaign.json").resolve()
                    and checkpoint_path(root / "ckpt" / "OLMo-sft_campaign.podB.json", pp)
                    == (root / "ckpt" / "OLMo-sft_campaign.podB.json").resolve())
    chk(f"stages: every checkpoint resolves to <out_root>/ckpt/<name>.json ({len(bad_paths)} other "
        f"locations refused; the default and an operator's restart name under ckpt/ accepted)",
        not let and ok_paths, let)

    # the run-time known answers at every stage start
    clean_start = startup_problems()
    fired_start = {}
    for mod, attr in ((keys, "stream_known_answer"), (_banner, "spec_problems"),
                      (_corr, "startup_hygiene")):
        with patched(mod, attr, lambda *a, **k: ["selftest planted problem"]):
            fired_start[attr] = (any("selftest planted problem" in x for x in startup_problems())
                                 and refuses(lambda: _startup_checks("G-TIME-F0", PROPOSAL_PATH),
                                             needle="STARTUP CHECKS FAIL"))
    absent_doc = REPO / "PROPOSAL-m-selftest-absent.md"
    named = startup_problems(absent_doc)
    chk("stages: the startup known answers (numpy stream, banner vs §2.5, roster hygiene) are clean "
        "here and each one's problem refuses the stage before any session; the banner is read from "
        "the proposal file the run names (an absent one is a problem naming it, finding R11)",
        clean_start == [] and all(fired_start.values()) and not absent_doc.exists()
        and any("cannot read" in x and absent_doc.name in x for x in named), (clean_start[:2], named[:1]))

    # the laptop preflight: non-stub Qwen only; CLAUDE.md and the analyzer committed at HEAD
    # with identical working-tree bytes (finding R8), HEAD from git rev-parse (finding R9)
    class _Real:
        def provenance(self) -> dict:
            return {"adapter": "qwen_mlx", "apparatus": "mlx", "platform": "selftest"}
    calls: list[int] = []

    def fake_preflight(problems):
        def f(*a, **k):
            calls.append(1)
            return list(problems)
        return f
    pf_x = _extra(xtra(), stage="time", sub="qwen")
    ana_rel = "scripts/k1_stage1.py"           # a repo file stands in for the analyzer
    ana_in = REPO / ana_rel
    ana_sha = _sha16_file(ana_in)

    def preflight(gitf, ana=ana_in):
        with patched(me, "_git", gitf), patched(me, "ANALYZER_PATH", ana):
            return _laptop_preflight(_Real(), "Q-F0", "G-TIME-F0", pf_x)
    with tempfile.TemporaryDirectory() as td:
        outside = Path(td) / "m_analyze.py"
        outside.write_text("# selftest analyzer\n", encoding="utf-8")
        with patched(guard, "preflight_laptop", fake_preflight(["POWER: selftest"])):
            stub_skips = _laptop_preflight(testing.ScriptedAdapter(), "Q-F0", "G-TIME-F0", pf_x) is False
            olmo_skips = _laptop_preflight(_Real(), "OLMo-sft", "G-TIME-OLMo-sft", pf_x) is False
            n_skip_calls = len(calls)
            power = refuses(lambda: preflight(fake_git()), needle="LAPTOP PREFLIGHT REFUSES")
        pf_refuse = {}
        with patched(guard, "preflight_laptop", fake_preflight([])):
            for nm, gitf, ana, needle in (
                    ("analyzer absent", fake_git(), REPO / "scripts" / "absent_m_analyze.py", "analyzer absent"),
                    ("analyzer outside the repository", fake_git(), outside, "outside the repository"),
                    ("analyzer not committed", fake_git(missing=(ana_rel,)), ana_in, "not committed at HEAD"),
                    ("CLAUDE.md edited after its commit", fake_git(blobs={"CLAUDE.md": b"committed\n"}), ana_in,
                     "CLAUDE.md CLAUDE.md: working-tree bytes are not HEAD's blob"),
                    ("analyzer a symlink at HEAD", fake_git(symlink=(ana_rel,)), ana_in, "a symlink at HEAD"),
                    ("HEAD unknown", fake_git(head_ok=False), ana_in, "HEAD unknown")):
                pf_refuse[nm] = refuses(lambda g=gitf, a=ana: preflight(g, a), needle=needle)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                ran = preflight(fake_git())
        gl = buf.getvalue()
    chk("stages: the laptop preflight is skipped on the stub and on OLMo, and on a non-stub Qwen "
        "adapter calls guard.preflight_laptop, refuses on its problem, an absent analyzer, one outside "
        "the repository or not committed at HEAD, CLAUDE.md whose bytes are not HEAD's, a symlinked "
        "analyzer and HEAD unknown (findings R8, R9), else prints m:267's gate line with HEAD from "
        "git rev-parse",
        stub_skips and olmo_skips and n_skip_calls == 0 and power and all(pf_refuse.values())
        and ran is True and len(calls) == 8 and gl.startswith("GATE G-TIME-F0: proposal ")
        and f"{PROPOSAL_REL} " in gl and "CLAUDE.md " in gl and f" {ana_sha}, HEAD {'ab' * 20}" in gl
        and not any(c[:1] in (("diff",), ("status",)) for c in git_calls),
        (pf_refuse, gl.strip()[:90]))

    # the prior stage's persisted end licenses the next stage
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)

        def prior_ck(unit: str, stage: str, status: str | None, tag: str = "") -> Path:
            tpls = list(keys.templates(unit))
            ident = _resume.Identity(unit=unit, stage=stage, template_set=tpls, lock_sha256="1" * 64,
                                     schedule_sha256="3" * 64, path="uncached", hour_cap=None,
                                     n={t: 1 for t in tpls}, audit_v2_sha16="4" * 16, ban_sha="5" * 16,
                                     backend_identifier="6" * 16, proposal_sha256="2" * 64)
            pth = td / f"{unit}_{stage}{tag}.json"
            ck = _resume.load_or_init(pth, ident, False)
            if status is not None:
                _record_stage_end(ck, status, [])
            _resume.write_checkpoint(pth, ck)
            return pth
        t_pass, t_stop = prior_ck("Q-F0", "time", "PASS"), prior_ck("Q-F0", "time", "STOP", "_s")
        t_open = prior_ck("Q-F0", "time", None, "_o")
        q_pass, q_stop = prior_ck("Q-F0", "qual", "PASS"), prior_ck("Q-F0", "qual", "STOP", "_s")
        o_pause, o_pass = prior_ck("OLMo-sft", "time", "PAUSE"), prior_ck("OLMo-sft", "time", "PASS", "_p")
        gates = td / "gates"
        must_refuse = {
            "G-ID without a prior": (lambda: prior_gate("Q-F0", "id", None), "PRIOR STAGE REQUIRED"),
            "G-ID after G-TIME STOP": (lambda: prior_gate("Q-F0", "id", t_stop), "PRIOR STAGE STOP"),
            "G-ID after an unfinished G-TIME": (lambda: prior_gate("Q-F0", "id", t_open), "NOT ENDED"),
            "G-ID with a qual checkpoint": (lambda: prior_gate("Q-F0", "id", q_pass), "MISMATCH"),
            "G-ID with no file": (lambda: prior_gate("Q-F0", "id", td / "none.json"), "ABSENT"),
            "Qwen qual, no G-ID artifact": (lambda: prior_gate("Q-F0", "qual", t_pass),
                                            "G-ID ARTIFACT ABSENT"),
            "OLMo qual after an unadjudicated PAUSE": (lambda: prior_gate("OLMo-sft", "qual", o_pause),
                                                       "PRIOR STAGE PAUSE"),
            "an adjudication after a PASS": (lambda: prior_gate("OLMo-sft", "qual", o_pass, "seat"),
                                             "PRIOR ADJUDICATION REFUSED"),
            "an adjudication on Qwen": (lambda: prior_gate("Q-F0", "id", t_pass, "seat"),
                                        "PRIOR ADJUDICATION REFUSED"),
            "campaign after qual STOP": (lambda: prior_gate("Q-F0", "campaign", q_stop),
                                         "PRIOR STAGE STOP"),
            "campaign with a G-TIME checkpoint": (lambda: prior_gate("Q-F0", "campaign", t_pass),
                                                  "MISMATCH"),
        }
        with patched(guard, "GATES_DIR", gates):
            let = [nm for nm, (fn, nd) in must_refuse.items() if not refuses(fn, needle=nd)]
            gates.mkdir()
            guard.gid_artifact_path("Q-F0").write_text(json.dumps({"verdict": "FAIL"}), encoding="utf-8")
            oks = [prior_gate("Q-F0", "id", t_pass)["status"] == "PASS",
                   prior_gate("Q-F0", "qual", t_pass)["status"] == "PASS",
                   prior_gate("OLMo-sft", "qual", o_pause, " seat: continue ")
                   == {"checkpoint": _rel(o_pause, REPO), "stage": "time", "status": "PAUSE",
                       "adjudication": "seat: continue"},
                   prior_gate("OLMo-sft", "qual", o_pass)["adjudication"] is None,
                   prior_gate("Q-F0", "campaign", q_pass)["stage"] == "qual",
                   prior_gate("Q-F0", "time", None) == {},
                   refuses(lambda: prior_gate("Q-F0", "time", t_pass), exc=ValueError)]
    chk(f"stages: the prior stage's persisted end gates the next ({len(must_refuse)} refusals: missing, "
        f"STOP, unfinished, wrong stage, no G-ID artifact, unadjudicated OLMo PAUSE, misplaced "
        f"adjudication) and licenses PASS, an adjudicated OLMo PAUSE, a G-ID artifact of any verdict",
        not let and all(oks), (let, oks))
    rp_ck: dict = {}
    first = {"checkpoint": "x.json", "stage": "time", "status": "PAUSE", "adjudication": "seat: a"}
    _record_prior(rp_ck, first, Path("q.json"))
    _record_prior(rp_ck, dict(first), Path("q.json"))
    _record_prior(rp_ck, {}, Path("q.json"))
    chk("stages: the prior licence is recorded once; a resume offering the same one continues, a "
        "different adjudication or status is refused",
        rp_ck["prior"] == first
        and refuses(lambda: _record_prior(rp_ck, {**first, "adjudication": "seat: b"}, Path("q.json")),
                    needle="CHECKPOINT MISMATCH")
        and refuses(lambda: _record_prior(rp_ck, {**first, "status": "PASS", "adjudication": None},
                                          Path("q.json")), needle="CHECKPOINT MISMATCH"))

    # one campaign look on synthetic records: the guards in both directions
    def fake(unit: str, t: str, s: int, prepick: bool, *, free_exclusion: bool = False,
             choices: list | None = None) -> dict:
        sub = "qwen" if unit == "Q-F0" else "olmo"
        claim = {"phase": "forced", "audit": {"substrate": sub, "phase": "forced", "claim": "lexical"}}
        clean = [{"phase": ph, "audit": {"substrate": sub, "phase": ph, "claim": None}}
                 for ph in ["forced"] * 4 + ["free"] * 6]
        exc = ({"class": "lexical", "phase": "forced", "detail": None} if prepick
               else {"class": "lexical", "phase": "free", "detail": None} if free_exclusion else None)
        return {"schema": "m-session-v1", "substrate": sub, "unit": unit, "stage": "campaign",
                "template": t, "contrast": keys.is_contrast(t), "s": s, "j": None,
                "path": "uncached", "rounds": clean[:1] + [claim] if prepick else clean,
                "exclusion": exc, "domain": not prepick, "choices": [] if prepick else (choices or [])}

    def recs(unit: str, k_contrast: int, k_sham: int, **kw) -> list[dict]:
        c, s = keys.templates(unit)
        return ([fake(unit, c, i, i < k_contrast, **kw) for i in range(20)]
                + [fake(unit, s, i, i < k_sham) for i in range(20)])
    hot_q, cold_q = campaign_look("Q-F0", recs("Q-F0", 8, 0), 1), campaign_look("Q-F0", recs("Q-F0", 1, 1), 1)
    hot_o = campaign_look("OLMo-dpo", recs("OLMo-dpo", 8, 0), "end")
    fq = [(r["name"].split("@")[0], r["fired"], r["exceeds"]) for r in hot_q["results"]]
    fo = [(r["name"].split("@")[0], r["fired"], r["exceeds"]) for r in hot_o["results"]]
    chk("stages: campaign_look -- 8/20 contrast pre-pick exclusions vs 0/20 sham fire the Fisher guard "
        "and (Qwen, binding) the .20 absolute guard; 1 vs 1 fires nothing",
        hot_q["fired"] and fq == [("round_degeneracy", False, False),
                                  ("exclusion_guard_fisher", True, True),
                                  ("exclusion_guard_abs", True, True)]
        and not cold_q["fired"] and {k: hot_q["arms"]["A0"][k] for k in ("launched", "prepick_excluded",
                                                                         "domain")}
        == {"launched": 20, "prepick_excluded": 8, "domain": 12}, fq)
    chk("stages: campaign_look on OLMo -- the absolute guard exceeds but is reported only (fired "
        "False); the Fisher guard binds",
        hot_o["fired"] and fo == [("round_degeneracy", False, False),
                                  ("exclusion_guard_fisher", True, True),
                                  ("exclusion_guard_abs", False, True)], fo)
    abs_only = campaign_look("OLMo-dpo", recs("OLMo-dpo", 9, 6), 1)
    fa = [(r["name"].split("@")[0], r["fired"], r["exceeds"]) for r in abs_only["results"]]
    abs_q = campaign_look("Q-F0", recs("Q-F0", 9, 6), 1)
    chk("stages: campaign_look -- OLMo contrast 9/20 vs sham 6/20 pre-pick: the absolute guard exceeds "
        "(reported only) and the look does NOT fire; the same counts on Qwen fire it (binding)",
        abs_only["fired"] is False and fa[2] == ("exclusion_guard_abs", False, True)
        and fa[1][1] is False and abs_q["fired"] is True, (fa, abs_q["fired"]))
    free_exc = campaign_look("Q-F0", recs("Q-F0", 0, 0, free_exclusion=True), 1)
    ff = {r["name"].split("@")[0]: (r["fired"], r["k"]) for r in free_exc["results"]}
    chk("stages: campaign_look -- 20/20 contrast FREE-phase lexical exclusions are not pre-pick: absent "
        "from prepick_excluded and from the guards' k (nothing fires); forced-phase ones count",
        free_exc["arms"]["A0"]["prepick_excluded"] == 0 and ff["exclusion_guard_fisher"] == (False, 0)
        and ff["exclusion_guard_abs"] == (False, 0) and not free_exc["fired"]
        and hot_q["results"][1]["k"] == 8, ff)
    ch = lambda low, top: {"low_label_mass": low, "top1_not_label": top}   # noqa: E731
    flagged = recs("Q-F0", 2, 0, choices=[ch(True, True), ch(True, False), ch(True, True)])
    for r in flagged[20:]:
        r["choices"] = [ch(True, False), ch(False, True)]
    fl_look = campaign_look("Q-F0", flagged, 1)["arms"]
    chk("stages: campaign_look reports m:330's read flags per arm -- sham over all reads, contrast over "
        "first reads of domain sessions only (later reads withheld)",
        fl_look["A0s"]["read_flags"] == {"scope": "all reads", "reads": 40, "low_label_mass": 20,
                                         "top1_not_label": 20}
        and fl_look["A0"]["read_flags"] == {"scope": "first reads of domain sessions", "reads": 18,
                                            "low_label_mass": 18, "top1_not_label": 18},
        (fl_look["A0"]["read_flags"], fl_look["A0s"]["read_flags"]))
    pub = _pause_public({"kind": "look", "at_launches": 40, "look": 1, "bars": ["x"],
                         "adjudication": "seat: the prism echoes are banner copies"})
    chk("stages: a pause reaches the report as {kind, at_launches, adjudicated, adjudication_sha16} "
        "(no text); an unadjudicated one carries no sha",
        sorted(pub) == ["adjudicated", "adjudication_sha16", "at_launches", "kind"]
        and pub["adjudicated"] is True and _HEX16.match(pub["adjudication_sha16"] or "")
        and "prism" not in json.dumps(pub)
        and _pause_public({"kind": "look", "at_launches": 40, "adjudication": None})
        == {"kind": "look", "at_launches": 40, "adjudicated": False, "adjudication_sha16": None}, pub)

    # the hair-trigger announcement
    lines_c, blk_c = announce_stop("Q-F0", "time", {"bar": "scaffold_absorption", "template": "A0",
                                                    "s": 0, "phase": "free", "contrast": True})
    lines_s, blk_s = announce_stop("Q-F0", "time", {"bar": "scaffold_absorption", "template": "A0s",
                                                    "s": 0, "phase": "forced", "contrast": False})
    chk("stages: a contrast free-phase trigger is announced by phase alone (no class); a sham one "
        "names its class and phase",
        not any("scaffold" in ln for ln in lines_c) and "free phase of a contrast" in lines_c[0]
        and blk_c["bar"] == WITHHELD_CLASS
        and "scaffold_absorption" in lines_s[0] and "phase=forced" in lines_s[0]
        and blk_s["bar"] == "scaffold_absorption")
    hh = _hair_hit({"hair_triggers": [{"name": "scaffold_absorption", "phase": "free", "detail": "x"}],
                    "template": "A0", "s": 3, "contrast": True,
                    "rounds": [{"phase": "forced", "ri": 0, "n": 1}, {"phase": "free", "ci": 2, "n": 7}]})
    chk("stages: a hair trigger's stop block records the fired round (phase, n, ri/ci) for the "
        "checkpoint; a G-VER stop and a clean record carry none",
        hh["round"] == {"phase": "free", "n": 7, "index": 2}
        and _verify_hit("A0", 0, ["template_breakage: x"], None)["round"] is None
        and _hair_hit({"hair_triggers": [], "rounds": []}) is None, hh["round"])

    # committed schedules
    with tempfile.TemporaryDirectory() as td:
        sd = Path(td) / "schedules"
        _schedule.write_schedule_files(sd)
        got = load_committed("Q-F0", [("time", "A0"), ("qual", "A0s")], sd)
        ok_load = (got["A0"]["cells"] == _schedule.gate_schedule("Q-F0", "time", "A0",
                                                                  _schedule.roster_for("Q-F0"), 1)
                   and got["A0s"]["n"] == 16)
        bad = []
        name = _schedule.schedule_filename("Q-F0", "qual", "A0s")
        raw = (sd / name).read_bytes()
        (sd / name).write_bytes(raw.replace(b'"start": 0', b'"start": 1', 1))
        try:
            load_committed("Q-F0", [("qual", "A0s")], sd)
            bad.append(False)
        except SystemExit:
            bad.append(True)
        (sd / name).write_bytes(raw)
        man = sd / _schedule.MANIFEST_NAME
        mraw = man.read_bytes()
        man.write_bytes(mraw.replace(hashlib.sha256(raw).hexdigest().encode(), b"0" * 64))
        try:
            load_committed("Q-F0", [("qual", "A0s")], sd)
            bad.append(False)
        except SystemExit:
            bad.append(True)
        man.write_bytes(mraw)
        try:
            load_committed("Q-F0", [("qual", "A0s")], Path(td) / "absent")
            bad.append(False)
        except SystemExit:
            bad.append(True)
    chk("stages: load_committed serves the committed cells (clean dir) and refuses a tampered cell, "
        "a manifest sha mismatch and a missing directory", ok_load and all(bad), bad)

    # the stub never writes where a measurement lands
    a = testing.ScriptedAdapter()
    canon = out_paths("Q-F0", "time", DEFAULT_OUT)

    def snap() -> list:
        return [(p.exists(), p.read_bytes() if p.is_file() else None)
                for p in (canon["ckpt"], canon["report"], canon["reads"])]
    before = snap()
    try:
        run_gate_stage(a, unit="Q-F0", gate="time", templates_counts=[("A0", 1), ("A0s", 1)],
                       identity_extra=xtra(), substrate="qwen", out_root=DEFAULT_OUT)
        ok = False
    except SystemExit as e:
        ok = "SELFTEST REFUSED" in str(e) and snap() == before and not a.calls
    chk("stages: a stage on the self-test stub is refused under REPO/data/m before any write or "
        "generation", ok)

    # one G-TIME stage end to end, both directions of its sham bar
    def run_time(rule, out, adapter=None, **kw):
        _schedule.write_schedule_files(Path(out) / "schedules")
        cells = {(t, 0): _schedule.gate_schedule("Q-F0", "time", t, _schedule.roster_for("Q-F0"), 1)[0]
                 for t in ("A0", "A0s")}
        ad = adapter or testing.ScriptedAdapter()
        ad.load(_script_policy("Q-F0", "time", cells, rule), None)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            res = run_gate_stage(ad, unit="Q-F0", gate="time",
                                 templates_counts=[("A0", 1), ("A0s", 1)],
                                 identity_extra=kw.pop("identity_extra", xtra()),
                                 substrate="qwen", out_root=out, **kw)
        return res, buf.getvalue(), ad

    with tempfile.TemporaryDirectory() as td:
        out = _resume.refuse_canonical_out(Path(td) / "m")
        res, txt, ad = run_time(None, out)
        rep = json.loads(res["report"].read_text())
        reads = json.loads(res["reads"].read_text())
        ck = json.loads(res["checkpoint"].read_text())
        ok_pass = (res["status"] == "PASS" and rep["bars"][0]["name"] == "round_degeneracy@G-TIME-F0"
                   and not rep["bars"][0]["fired"] and [r["template"] for r in ck["sessions"]] == ["A0", "A0s"]
                   and all(r["verified"] and r["path"] == "uncached" for r in ck["sessions"])
                   and all(c["cached"] is False for c in ad.calls)
                   and ck["stage_end"] == {"status": "PASS", "fired": [], "adjudication": None}
                   and ck["identity"]["renders_sha16"] == rsha
                   and ck["identity"]["package_sha256"] == _resume.package_sha256())
        sham = [r for r in ck["sessions"] if not r["contrast"]]
        ok_timing = (rep["timing"]["sham_sessions"] == len(sham) == 1
                     and rep["timing"]["sham_seconds"] == round(sum(float(r["seconds"]) for r in sham), 3)
                     and "withheld" in rep["timing"]["contrast_seconds"])
        con = [r for r in reads["sessions"] if r["contrast"]][0]
        ok_reads = (all(x["phase"] == "forced" for x in con["rounds"]) and "choices" not in con
                    and "choices" not in json.dumps(rep))
        lines = [ln for ln in txt.splitlines()]
        ok_out = (lines[0] == _provenance_line(ck["provenance"][0])
                  and lines[1:3] == ["time A0 s=0 valid", "time A0s s=0 valid"]
                  and "STAGE G-TIME-F0 PASS path=uncached" in lines
                  and not _ROSTER_RX.search(txt) and "choice" not in "\n".join(lines[1:]))
        ok_prov = (len(ck["provenance"]) == 1 and ck["provenance"][0]["launched"] == 2
                   and {k: v for k, v in ck["provenance"][0]["record"].items() if k != "n_encodes_clipped"}
                   == {k: v for k, v in json.loads(json.dumps(ad.provenance())).items()
                       if k != "n_encodes_clipped"}
                   and rep["provenance"] == ck["provenance"] and "provenance" not in ck["identity"]
                   and "provenance" not in _ident_summary(ck["identity"]))
        again = refuses(lambda: run_time(None, out, resume=True), needle="STAGE ENDED")
    chk("stages: G-TIME-F0 on the stub -- A0 then A0s, uncached, verified, PASS persisted as stage_end; "
        "checkpoint, report and reads written; a re-run of the finished stage is refused",
        ok_pass and again, res["status"])
    chk("stages: the report's timing covers the sham session only (count and sum); contrast seconds "
        "withheld", ok_timing, rep["timing"])
    chk("stages: the A0 read is banner + forced rounds; the report carries no choice field", ok_reads)
    chk("stages: stdout is the PROVENANCE line, session lines, bar messages, the stage line with its "
        "path and paths -- no label, no menu", ok_out, lines[:3])
    chk("stages: the adapter's provenance is recorded verbatim in the checkpoint (one entry, its "
        "stamp, 2 launches), copied into the report, never inside the identity", ok_prov,
        (ck.get("provenance") or [{}])[0].get("launched"))
    with tempfile.TemporaryDirectory() as td:
        out = _resume.refuse_canonical_out(Path(td) / "m")
        res, txt, _ = run_time(lambda t, s, n, c: "Config choice one." if t == "A0s" and n in (5, 7, 9)
                               else None, out)
        rep = json.loads(res["report"].read_text())
        ck = json.loads(res["checkpoint"].read_text())
    chk("stages: G-TIME-F0's sham bar fires at 3 free v2 claims in 10 rounds -> STOP (m:280), "
        "persisted as stage_end STOP naming the bar",
        res["status"] == "STOP" and rep["bars"][0]["fired"] and rep["bars"][0]["k"] == 3
        and rep["bars"][0]["n"] == 10 and ck["stage_end"]["status"] == "STOP"
        and ck["stage_end"]["fired"] == ["round_degeneracy@G-TIME-F0"] and "stop" not in ck,
        rep["bars"][0]["message"])

    # a stage start refuses before any session: a startup problem, a non-stub preflight problem
    starts = {}

    def refused_start(fn, needle: str) -> bool:
        # each case in its own out root: one case's outcome never decides another's
        try:
            fn()
            return False
        except (SystemExit, ValueError) as e:
            return needle in str(e)
    with tempfile.TemporaryDirectory() as td:
        outs_ = {k: _resume.refuse_canonical_out(Path(td) / k / "m")
                 for k in ("startup", "preflight", "pre-lock", "renders")}
        with patched(keys, "stream_known_answer", lambda: ["selftest numpy drift"]):
            ad1 = testing.ScriptedAdapter()
            starts["startup"] = (refused_start(lambda: run_time(None, outs_["startup"], adapter=ad1),
                                               "STARTUP CHECKS FAIL")
                                 and not ad1.calls and not (outs_["startup"] / "ckpt").exists())
        ad2 = testing.ScriptedAdapter()
        real_prov = ad2.provenance
        ad2.provenance = lambda: {**real_prov(), "adapter": "qwen_mlx", "apparatus": "mlx"}
        calls.clear()
        with patched(guard, "preflight_laptop", fake_preflight(["ONE PROCESS: selftest"])), \
                patched(sys.modules[__name__], "DEFAULT_OUT", outs_["preflight"]):
            starts["preflight"] = (refused_start(lambda: run_time(None, outs_["preflight"], adapter=ad2,
                                                                  identity_extra=xtra(proposal_file=PROPOSAL_REL,
                                                                                      lock_file="CLAUDE.md",
                                                                                      analyzer_sha256="a" * 64,
                                                                                      package_sha256="b" * 64)),
                                                 "LAPTOP PREFLIGHT REFUSES")
                                   and calls == [1] and not ad2.calls
                                   and not (outs_["preflight"] / "ckpt").exists())
        ad3 = testing.ScriptedAdapter()
        starts["pre-lock"] = (refused_start(lambda: run_time(None, outs_["pre-lock"], adapter=ad3,
                                                             identity_extra=xtra(lock_sha256="pre-lock")),
                                            "pre-lock")
                              and not ad3.calls and not (outs_["pre-lock"] / "ckpt").exists())
        ad4 = testing.ScriptedAdapter()
        starts["renders"] = (refused_start(lambda: run_time(None, outs_["renders"], adapter=ad4,
                                                            identity_extra=xtra(renders_sha16="0" * 16)),
                                           "RENDERS MISMATCH")
                             and not ad4.calls and not (outs_["renders"] / "ckpt").exists())
    chk("stages: a stage start refuses before any generation or write on a startup known-answer "
        "problem, a non-stub laptop preflight problem, a 'pre-lock' lock hash and a renders mismatch",
        all(starts.values()), starts)

    # a checkpoint path naming a roster word is refused at start (N10); whole words only
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "m"
        pp = out_paths("Q-F0", "time", root)
        roster_names = ("Q-F0_time.maple.json", "Q-F0_time.Slate-podB.json", "PRISM.json",
                        "Q-F0_time_adjudication.json")
        let = [nm for nm in roster_names
               if not refuses(lambda nm=nm: checkpoint_path(root / "ckpt" / nm, pp),
                              needle="CHECKPOINT PATH REFUSED")]
        ok_names = [checkpoint_path(root / "ckpt" / nm, pp).name
                    for nm in ("Q-F0_time.maplewood.json", "Q-F0_time.podB.json")]
        out_r = _resume.refuse_canonical_out(Path(td) / "roster" / "m")
        adr = testing.ScriptedAdapter()
        r_int = refused_start(lambda: run_time(None, out_r, adapter=adr,
                                               ckpt_path=out_r / "ckpt" / "Q-F0_time.walnut.json"),
                              "names a roster word")
        r_int = r_int and not adr.calls and not (out_r / "ckpt").exists() and not (out_r / "reports").exists()
    chk("stages: a checkpoint path naming a roster word (whole word, any case, '.'/'-' bounded) or the "
        "reserved '_adjudication' stem is refused at start with nothing written or generated; "
        "'maplewood' and a plain restart name are accepted",
        not let and ok_names == ["Q-F0_time.maplewood.json", "Q-F0_time.podB.json"] and r_int,
        (let, ok_names, r_int))
    chk("stages: the adjudication excerpt sits beside its checkpoint, named after its stem",
        adjudication_path(Path("/x/m/ckpt/Q-F0_time.json")) == Path("/x/m/ckpt/Q-F0_time_adjudication.json")
        and adjudication_path(Path("/x/m/ckpt/Q-F0_campaign.podB.json")).name
        == "Q-F0_campaign.podB_adjudication.json")

    # the adapter's provenance is checked at start: JSON-native, no roster word
    with tempfile.TemporaryDirectory() as td:
        prov_cases = {}
        for nm, extra_prov in (("roster word", {"gpu": "Velvet X100"}), ("non-native", {"gpu": {1, 2}})):
            out_p = _resume.refuse_canonical_out(Path(td) / nm.replace(" ", "_") / "m")
            adp = testing.ScriptedAdapter()
            real_p = adp.provenance
            adp.provenance = lambda real_p=real_p, x=extra_prov: {**real_p(), **x}
            prov_cases[nm] = (refused_start(lambda: run_time(None, out_p, adapter=adp), "PROVENANCE REFUSED")
                              and not adp.calls and not (out_p / "ckpt").exists())
        ok_prov_rec = _start_provenance(testing.ScriptedAdapter(), "G-TIME-F0")["adapter"] == STUB_MARK + \
            " -- NOT A MODEL"
    chk("stages: a provenance record naming a roster word or carrying a non-JSON value refuses the stage "
        "at start (nothing written, nothing generated); the stub's record is accepted",
        all(prov_cases.values()) and ok_prov_rec, prov_cases)

    # a non-stub adapter writes under REPO/data/m only (finding 14)
    with tempfile.TemporaryDirectory() as td:
        out_n = _resume.refuse_canonical_out(Path(td) / "nonstub" / "m")
        with patched(sys.modules[__name__], "_is_stub", lambda adapter: False):
            g_ok = _out_root_guard(testing.ScriptedAdapter(), DEFAULT_OUT) is None
            g_alias = _out_root_guard(testing.ScriptedAdapter(), REPO / "data" / "x" / ".." / "m") is None
            g_bad = refuses(lambda: _out_root_guard(testing.ScriptedAdapter(), out_n), needle="OUT ROOT REFUSED")
            adn = testing.ScriptedAdapter()
            g_run = (refused_start(lambda: run_time(None, out_n, adapter=adn,
                                                    identity_extra=xtra(proposal_file=PROPOSAL_REL,
                                                                        lock_file="CLAUDE.md",
                                                                        analyzer_sha256="a" * 64,
                                                                        package_sha256="b" * 64)),
                                   "OUT ROOT REFUSED")
                     and not adn.calls and not (out_n / "ckpt").exists())
        g_stub = _out_root_guard(testing.ScriptedAdapter(), out_n) is None
    chk("stages: a non-stub adapter's out_root must resolve to REPO/data/m (accepted there, '..' resolved; "
        "refused elsewhere before any write or generation); the stub's is not bound by it",
        g_ok and g_alias and g_bad and g_run and g_stub, (g_ok, g_alias, g_bad, g_run, g_stub))

    # identity_extra's lock_file: required on a non-stub run, optional on the stub, form-checked
    lf_bad = {"absolute": "/tmp/LOCK.md", "a '..' walk": "../LOCK.md", "not normalized": "./LOCK.md",
              "a roster word": "LOCK-m-prism.md", "not a str": 7, "empty": ""}
    let = [nm for nm, v in lf_bad.items()
           if not refuses(lambda v=v: _extra(xtra(lock_file=v), stage="time", sub="qwen"), exc=ValueError)]
    lf_ok = (_extra(xtra(lock_file="locks/LOCK-m-F0-v0.1.md", proposal_file=PROPOSAL_REL, analyzer_sha256="a" * 64,
                         package_sha256="b" * 64), stage="time", sub="qwen", stub=False)["lock_file"]
             == "locks/LOCK-m-F0-v0.1.md"
             and _extra(xtra(), stage="time", sub="qwen", stub=True)["lock_file"] is None
             and refuses(lambda: _extra(xtra(proposal_file=PROPOSAL_REL, analyzer_sha256="a" * 64,
                                             package_sha256="b" * 64), stage="time", sub="qwen", stub=False),
                         exc=ValueError, needle="lock_file"))
    chk(f"stages: identity_extra's lock_file is required on a non-stub run, optional on the stub, and "
        f"refused in {len(lf_bad)} malformed forms", not let and lf_ok, let)

    # the licence by file: committed at HEAD as a regular blob, the working tree's bytes that
    # blob, sha256 as named; HEAD known; never git diff (findings R4, R9; git monkeypatched)
    with tempfile.TemporaryDirectory() as td:
        rp = Path(td)
        (rp / "P.md").write_text("proposal\n", encoding="utf-8")
        (rp / "locks").mkdir()
        (rp / "A.py").write_text("# analyzer\n", encoding="utf-8")
        psha = hashlib.sha256(b"proposal\n").hexdigest()
        asha = hashlib.sha256(b"# analyzer\n").hexdigest()
        pkg = _resume.package_sha256()
        # the lock's text names the analyzer's and the package's sha256 (the seat's D2); the
        # isolating locks below each name exactly what their one case needs
        lock_bodies = {"L": f"lock\nanalyzer {asha}\npackage {pkg}\n",
                       "noana": f"lock\npackage {pkg}\n", "nopkg": f"lock\nanalyzer {asha}\n",
                       "ana3": f"lock\nanalyzer {'3' * 64}\npackage {pkg}\n",
                       "pkg3": f"lock\nanalyzer {asha}\npackage {'3' * 64}\n",
                       # (f) is verbatim 64-hex: a lock abbreviating a sha to its 16-hex prefix (plain, or
                       # with the '…' this repo's documents use) does not name it
                       "ana16": f"lock\nanalyzer {asha[:16]}\npackage {pkg}\n",
                       "ana16e": f"lock\nanalyzer {asha[:16]}…\npackage {pkg}\n",
                       "pkg16": f"lock\nanalyzer {asha}\npackage {pkg[:16]}\n",
                       "pkg16e": f"lock\nanalyzer {asha}\npackage {pkg[:16]}…\n"}
        for nm_, body_ in lock_bodies.items():
            (rp / "locks" / f"{nm_}.md").write_text(body_, encoding="utf-8")
        (rp / "locks" / "real.md").write_text(lock_bodies["L"], encoding="utf-8")
        (rp / "locks" / "W.md").symlink_to(rp / "locks" / "real.md")
        lsha = hashlib.sha256(lock_bodies["L"].encode("utf-8")).hexdigest()
        good_x = {"proposal_file": "P.md", "proposal_sha256": psha, "lock_sha256": lsha,
                  "lock_file": "locks/L.md", "analyzer_sha256": asha, "package_sha256": pkg}

        def with_lock(nm_: str, **over) -> dict:
            return {**good_x, "lock_file": f"locks/{nm_}.md",
                    "lock_sha256": hashlib.sha256(lock_bodies[nm_].encode("utf-8")).hexdigest(), **over}
        lic = {}
        d2 = {}
        git_calls.clear()
        with patched(me, "_git", fake_git()), patched(me, "ANALYZER_PATH", rp / "A.py"):
            lic["clean"] = licence_problems(good_x, repo=rp)
            d2["no analyzer sha"] = licence_problems({k: v for k, v in good_x.items() if k != "analyzer_sha256"},
                                                     repo=rp)
            d2["no package sha"] = licence_problems({k: v for k, v in good_x.items() if k != "package_sha256"},
                                                    repo=rp)
            d2["a malformed package sha"] = licence_problems({**good_x, "package_sha256": "x"}, repo=rp)
            d2["analyzer mismatch"] = licence_problems(with_lock("ana3", analyzer_sha256="3" * 64), repo=rp)
            d2["package mismatch"] = licence_problems(with_lock("pkg3", package_sha256="3" * 64), repo=rp)
            with patched(_resume, "package_sha256", lambda: "5" * 64):
                d2["the package moved (hashed at check time)"] = licence_problems(good_x, repo=rp)
            d2["the lock names no analyzer sha"] = licence_problems(with_lock("noana"), repo=rp)
            d2["the lock names no package sha"] = licence_problems(with_lock("nopkg"), repo=rp)
            for nm_, k_ in (("ana16", "analyzer"), ("ana16e", "analyzer"), ("pkg16", "package"),
                            ("pkg16e", "package")):
                d2[f"the lock names only the {k_} sha's 16-hex prefix ({nm_})"] = licence_problems(
                    with_lock(nm_), repo=rp)
            lic["proposal sha"] = licence_problems({**good_x, "proposal_sha256": "2" * 64}, repo=rp)
            lic["lock sha"] = licence_problems({**good_x, "lock_sha256": "1" * 64}, repo=rp)
            lic["analyzer sha"] = licence_problems({**good_x, "analyzer_sha256": "3" * 64}, repo=rp)
            lic["no lock file"] = licence_problems({k: v for k, v in good_x.items() if k != "lock_file"},
                                                   repo=rp)
            lic["no proposal file"] = licence_problems({k: v for k, v in good_x.items()
                                                        if k != "proposal_file"}, repo=rp)
            lic["absent file"] = licence_problems({**good_x, "lock_file": "locks/none.md"}, repo=rp)
            lic["working-tree symlink"] = licence_problems({**good_x, "lock_file": "locks/W.md"}, repo=rp)
        for nm, gitf in (("proposal not at HEAD", fake_git(missing=("P.md",))),
                         ("lock a symlink at HEAD", fake_git(symlink=("locks/L.md",))),
                         ("lock edited after its commit", fake_git(blobs={"locks/L.md": b"lock v0\n"})),
                         ("lock a tree at HEAD", fake_git(tree=("locks/L.md",))),
                         ("HEAD unknown", fake_git(head_ok=False))):
            with patched(me, "_git", gitf):
                lic[nm] = licence_problems(good_x, repo=rp)
    want_lic = {"proposal sha": "proposal P.md: sha256", "lock sha": "lock locks/L.md: sha256",
                "analyzer sha": "analyzer_sha256", "no lock file": "lock: no file named",
                "no proposal file": "proposal: no file named", "absent file": "not committed at HEAD",
                "working-tree symlink": "not a regular file at that path",
                "proposal not at HEAD": "P.md: not committed at HEAD",
                "lock a symlink at HEAD": "locks/L.md: a symlink at HEAD",
                "lock edited after its commit": "working-tree bytes are not HEAD's blob",
                "lock a tree at HEAD": "not a regular file at HEAD", "HEAD unknown": "HEAD unknown"}
    lic_ok = (lic["clean"] == [] and all(any(w in x for x in lic[k]) for k, w in want_lic.items()))
    chk("stages: the licence by file passes a proposal and lock committed at HEAD as regular blobs whose "
        "bytes are the working tree's and hash to the identity's values (and an analyzer at its pinned "
        "sha256), and names each defect: a sha mismatch (proposal, lock, analyzer), no file named, a file "
        "not at HEAD, a symlink at HEAD or in the working tree, a tree entry, edits after the commit, "
        "HEAD unknown -- by object reads only (cat-file / ls-tree / rev-parse), never git diff",
        lic_ok and ("cat-file", "blob", "HEAD:locks/L.md") in git_calls
        and ("ls-tree", "-z", "HEAD", "--", "P.md") in git_calls
        and all(c[0] in ("cat-file", "ls-tree", "rev-parse") for c in git_calls),
        {k: v[:1] for k, v in lic.items()})
    want_d2 = {"no analyzer sha": "analyzer_sha256: identity_extra carries none",
               "no package sha": "package_sha256: identity_extra carries none",
               "a malformed package sha": "package_sha256: identity_extra carries none (or not 64",
               "analyzer mismatch": "is not identity_extra's analyzer_sha256",
               "package mismatch": "is not identity_extra's package_sha256",
               "the package moved (hashed at check time)": "is not identity_extra's package_sha256",
               "the lock names no analyzer sha": "does not name identity_extra's analyzer_sha256",
               "the lock names no package sha": "does not name identity_extra's package_sha256"}
    for nm_, k_ in (("ana16", "analyzer"), ("ana16e", "analyzer"), ("pkg16", "package"), ("pkg16e", "package")):
        want_d2[f"the lock names only the {k_} sha's 16-hex prefix ({nm_})"] = \
            f"does not name identity_extra's {k_}_sha256"
    d2_lic_bad = [k for k, w in want_d2.items() if not (len(d2[k]) == 1 and w in d2[k][0])]
    chk("stages: the seat's D2 at stage start -- licence_problems passes the analyzer's bytes at analyzer_sha256, "
        "the package this process hashes at package_sha256 and a lock whose committed text names both; it names "
        "exactly one problem (a string, never a KeyError) for each alone: analyzer_sha256 absent, package_sha256 "
        "absent or malformed, an analyzer mismatch, a package mismatch (offered, or the package hashed at check "
        "time moved), a lock text not naming the analyzer sha, not naming the package sha -- and (f) is verbatim "
        "64-hex: a lock naming only a sha's 16-hex prefix, plain or with '…', does not name it (each key alone)",
        lic["clean"] == [] and not d2_lic_bad, {k: d2[k][:1] for k in d2_lic_bad} or len(d2))

    # the licence and the out root on a (simulated) non-stub run, end to end
    real_psha = hashlib.sha256(PROPOSAL_PATH.read_bytes()).hexdigest()
    lock_rel = "FINDINGS-4.md"                 # a repo path stands in for the lock
    real_asha = hashlib.sha256(ana_in.read_bytes()).hexdigest()
    pkg_now = _resume.package_sha256()

    def lock_naming(*shas: str) -> bytes:
        return ("LOCK (selftest stand-in) " + " ".join(shas) + "\n").encode("utf-8")

    def committed_lock(body: bytes):
        # selftest only: the lock path's committed bytes are ``body`` (a lock whose text names the
        # analyzer's and the package's sha256 cannot be a file of this tree); every other path goes
        # through the real _committed (on fake_git)
        real_c = _committed

        def c(rel, repo=REPO):
            return ([], body) if rel == lock_rel else real_c(rel, repo)
        return c
    lock_both = lock_naming(real_asha, pkg_now)
    real_lsha = hashlib.sha256(lock_both).hexdigest()
    real_x = xtra(proposal_sha256=real_psha, lock_sha256=real_lsha, lock_file=lock_rel,
                  proposal_file=PROPOSAL_REL, analyzer_sha256=real_asha, package_sha256=pkg_now)
    lock_nopkg = lock_naming(real_asha)
    lock_pkg5 = lock_naming(real_asha, "5" * 64)
    nonstub = {}
    with tempfile.TemporaryDirectory() as td:
        for nm, x, gitf, body, needle in (
                ("licensed", real_x, fake_git(), lock_both, None),
                ("proposal sha", {**real_x, "proposal_sha256": "2" * 64}, fake_git(), lock_both, "LICENCE REFUSED"),
                ("lock edited", real_x, fake_git(blobs={lock_rel: b"an earlier lock\n"}), None, "LICENCE REFUSED"),
                ("proposal not committed", real_x, fake_git(missing=(PROPOSAL_REL,)), lock_both, "LICENCE REFUSED"),
                ("no lock file", {k: v for k, v in real_x.items() if k != "lock_file"}, fake_git(), lock_both,
                 "lock_file"),
                ("no proposal file", {k: v for k, v in real_x.items() if k != "proposal_file"}, fake_git(),
                 lock_both, "proposal_file"),
                ("no analyzer sha", {k: v for k, v in real_x.items() if k != "analyzer_sha256"}, fake_git(),
                 lock_both, "must carry analyzer_sha256"),
                ("no package sha", {k: v for k, v in real_x.items() if k != "package_sha256"}, fake_git(),
                 lock_both, "must carry package_sha256"),
                ("the lock names no package sha", {**real_x, "lock_sha256": hashlib.sha256(lock_nopkg).hexdigest()},
                 fake_git(), lock_nopkg, "does not name identity_extra's package_sha256"),
                ("a package that is not this process's", {**real_x, "package_sha256": "5" * 64,
                                                          "lock_sha256": hashlib.sha256(lock_pkg5).hexdigest()},
                 fake_git(), lock_pkg5, "is not identity_extra's package_sha256")):
            out_l = _resume.refuse_canonical_out(Path(td) / nm.replace(" ", "_").replace("'", "") / "m")
            adl = testing.ScriptedAdapter()
            with contextlib.ExitStack() as st_l:
                for mod_, attr_, val_ in ((me, "_is_stub", lambda adapter: False), (me, "DEFAULT_OUT", out_l),
                                          (me, "ANALYZER_PATH", ana_in), (guard, "preflight_laptop", fake_preflight([])),
                                          (me, "_git", gitf)):
                    st_l.enter_context(patched(mod_, attr_, val_))
                if body is not None:
                    st_l.enter_context(patched(me, "_committed", committed_lock(body)))
                if needle is None:
                    res_l, txt_l, _ = run_time(None, out_l, adapter=adl, identity_extra=x)
                    ck_l = json.loads(res_l["checkpoint"].read_text())
                    nonstub[nm] = (res_l["status"] == "PASS" and len(adl.calls) == 20
                                   and f"LICENCE G-TIME-F0: proposal {PROPOSAL_REL} {real_psha[:16]}" in txt_l
                                   and f"lock {lock_rel} {real_lsha[:16]}: committed at HEAD {'ab' * 20}, working "
                                       f"tree identical; analyzer {real_asha[:16]} and package {pkg_now[:16]}: "
                                       f"the hashes identity_extra and the lock name, hashed from the working tree "
                                       f"at stage start" in txt_l
                                   and f"package {pkg_now[:16]}: committed" not in txt_l
                                   and txt_l.count("committed at HEAD") == 1
                                   and ck_l["licence"] == {"proposal_file": PROPOSAL_REL, "lock_file": lock_rel,
                                                           "prior_proposal_sha256s": [], "analyzer_sha256": real_asha,
                                                           "package_sha256": pkg_now})
                else:
                    nonstub[nm] = (refused_start(lambda: run_time(None, out_l, adapter=adl, identity_extra=x),
                                                 needle)
                                   and not adl.calls and not (out_l / "ckpt").exists())
    chk("stages: on a non-stub run the licence admits the committed proposal and lock, the analyzer and the package "
        "the lock names (the LICENCE line names the proposal file, the analyzer's and the package's sha16 and HEAD, "
        "and claims 'committed at HEAD, working tree identical' for the proposal and the lock only -- the analyzer "
        "and the package as the hashes the identity and the lock name; the checkpoint records the licence, both "
        "hashes included) and refuses, before any generation or write, a "
        "proposal sha256 that is not the file's, a lock edited after its commit, a proposal not committed, a missing "
        "lock_file, proposal_file, analyzer_sha256 or package_sha256, a lock whose text does not name the package "
        "sha, and a package_sha256 that is not this process's package (the seat's D2)",
        all(nonstub.values()), nonstub)
    # the stub's proposal file is identity_extra's too (finding R11): an absent one refuses the start
    with tempfile.TemporaryDirectory() as td:
        out_a = _resume.refuse_canonical_out(Path(td) / "absent_doc" / "m")
        ada = testing.ScriptedAdapter()
        r11 = (refused_start(lambda: run_time(None, out_a, adapter=ada,
                                              identity_extra=xtra(proposal_file="PROPOSAL-m-selftest-absent.md")),
                             "PROPOSAL-m-selftest-absent.md")
               and not ada.calls and not (out_a / "ckpt").exists())
    chk("stages: a stage reads the proposal file identity_extra names at run time -- a stub run naming an "
        "absent one is refused at start (STARTUP CHECKS FAIL naming it), nothing generated or written",
        r11)
    rl: dict = {}
    lx = _extra(xtra(prior_proposal_sha256s=["9" * 64], analyzer_sha256="a" * 64, package_sha256="b" * 64),
                stage="time", sub="qwen")
    _record_licence(rl, lx, Path("q.json"))
    _record_licence(rl, dict(lx), Path("q.json"))
    chk("stages: the licence (proposal file, lock file, the lock's re-adopted proposals, analyzer and package "
        "sha256) is recorded once; the same one continues; a different re-adoption list, proposal file, analyzer "
        "sha or package sha (the seat's D2) is refused",
        rl["licence"]["prior_proposal_sha256s"] == ["9" * 64] and rl["licence"].get("package_sha256") == "b" * 64
        and tuple(sorted(rl["licence"])) == LICENCE_KEYS
        and refuses(lambda: _record_licence(rl, {**lx, "prior_proposal_sha256s": []}, Path("q.json")),
                    needle="CHECKPOINT MISMATCH")
        and refuses(lambda: _record_licence(rl, {**lx, "proposal_file": "archive/P.md"}, Path("q.json")),
                    needle="CHECKPOINT MISMATCH")
        and refuses(lambda: _record_licence(rl, {**lx, "analyzer_sha256": "c" * 64}, Path("q.json")),
                    needle="CHECKPOINT MISMATCH")
        and refuses(lambda: _record_licence(rl, {**lx, "package_sha256": "c" * 64}, Path("q.json")),
                    needle="CHECKPOINT MISMATCH"), rl.get("licence"))

    # the prior stage: same proposal (or one the lock re-adopts); a non-stub run takes no
    # stub-written prior (N17); the G-ID artifact under the same rules (finding R3)
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)

        def prior_with(tag: str, *, proposal: str = "2" * 64, lock: str = "1" * 64,
                       prov: list | None = None) -> Path:
            tpls = list(keys.templates("Q-F0"))
            ident = _resume.Identity(unit="Q-F0", stage="time", template_set=tpls, lock_sha256=lock,
                                     schedule_sha256="3" * 64, path="uncached", hour_cap=None,
                                     n={t: 1 for t in tpls}, audit_v2_sha16="4" * 16, ban_sha="5" * 16,
                                     backend_identifier="6" * 16, proposal_sha256=proposal)
            pth = td / f"Q-F0_time{tag}.json"
            ck_ = _resume.load_or_init(pth, ident, False)
            for rec_ in prov or []:
                _resume.append_provenance(ck_, rec_, stamp="2026-10-06T00:00:00Z")
            _record_stage_end(ck_, "PASS", [])
            _resume.write_checkpoint(pth, ck_)
            return pth
        real_rec = {"adapter": "qwen_mlx", "apparatus": "mlx", "platform": "selftest"}
        stub_rec = testing.ScriptedAdapter().provenance()
        p_real = prior_with("_real", prov=[real_rec])
        p_stub = prior_with("_stub", prov=[stub_rec])
        p_mixed = prior_with("_mixed", prov=[real_rec, stub_rec])
        p_none = prior_with("_none")
        p_other = prior_with("_other", proposal="9" * 64, prov=[real_rec])
        p_lock = prior_with("_lock", lock="7" * 64, prov=[real_rec])
        pg = {"stub prior, non-stub run": (lambda: prior_gate("Q-F0", "id", p_stub, proposal_sha256="2" * 64,
                                                              require_real=True), "ON THE STUB"),
              "a stub entry among real ones": (lambda: prior_gate("Q-F0", "id", p_mixed, require_real=True),
                                               "ON THE STUB"),
              "no provenance, non-stub run": (lambda: prior_gate("Q-F0", "id", p_none, require_real=True),
                                              "ON THE STUB"),
              "another proposal": (lambda: prior_gate("Q-F0", "id", p_other, proposal_sha256="2" * 64),
                                   "ANOTHER PROPOSAL"),
              "another proposal, not the one re-adopted": (
                  lambda: prior_gate("Q-F0", "id", p_other, proposal_sha256="2" * 64,
                                     prior_proposal_sha256s=["8" * 64]), "ANOTHER PROPOSAL")}
        let = [nm for nm, (fn, nd) in pg.items() if not refuses(fn, needle=nd)]
        oks = [prior_gate("Q-F0", "id", p_real, proposal_sha256="2" * 64, require_real=True)["status"] == "PASS",
               prior_gate("Q-F0", "id", p_stub, proposal_sha256="2" * 64)["status"] == "PASS",
               prior_gate("Q-F0", "id", p_none)["status"] == "PASS",
               prior_gate("Q-F0", "id", p_lock, proposal_sha256="2" * 64, require_real=True)["status"] == "PASS",
               prior_gate("Q-F0", "id", p_other, proposal_sha256="2" * 64,
                          prior_proposal_sha256s=["9" * 64])["status"] == "PASS",
               written_on_stub({"provenance": [{"record": real_rec}]}) is False]
        # the G-ID artifact the qualification needs (and the campaign takes its path from)
        gates = td / "gates"
        gates.mkdir()

        def art(proposal: str | None, prov: list | None) -> None:
            body: dict = {"verdict": "FAIL"}
            if proposal is not None:
                body["identity"] = {"proposal_sha256": proposal}
            if prov is not None:
                body["provenance"] = [{"stamp": "2026-10-06T00:00:00Z", "record": r_, "launched": 2}
                                      for r_ in prov]
            guard.gid_artifact_path("Q-F0").write_text(json.dumps(body), encoding="utf-8")
        art_cases: dict = {}
        with patched(guard, "GATES_DIR", gates):
            for nm, (aprop, aprov, kw, needle) in {
                    "artifact under another proposal": ("7" * 64, [real_rec], {}, "G-ID ARTIFACT UNDER ANOTHER"),
                    "artifact under the re-adopted proposal": ("7" * 64, [real_rec],
                                                               {"prior_proposal_sha256s": ["7" * 64]}, None),
                    "artifact with no identity": (None, [real_rec], {}, "G-ID ARTIFACT UNDER ANOTHER"),
                    "stub artifact, non-stub run": ("2" * 64, [stub_rec], {"require_real": True},
                                                    "G-ID ARTIFACT ON THE STUB"),
                    "artifact without provenance, non-stub run": ("2" * 64, None, {"require_real": True},
                                                                  "G-ID ARTIFACT ON THE STUB"),
                    "stub artifact, stub run": ("2" * 64, [stub_rec], {}, None),
                    "real artifact, non-stub run": ("2" * 64, [real_rec], {"require_real": True}, None)}.items():
                art(aprop, aprov)
                kw_ = {"proposal_sha256": "2" * 64, **kw}
                pr = p_real if kw.get("require_real") else p_stub
                if needle is None:
                    art_cases[nm] = prior_gate("Q-F0", "qual", pr, **kw_)["status"] == "PASS"
                else:
                    art_cases[nm] = refuses(lambda pr=pr, kw_=kw_: prior_gate("Q-F0", "qual", pr, **kw_),
                                            needle=needle)
            guard.gid_artifact_path("Q-F0").write_text("{truncated", encoding="utf-8")
            art_cases["an unreadable artifact"] = refuses(
                lambda: prior_gate("Q-F0", "qual", p_stub, proposal_sha256="2" * 64), needle="UNREADABLE")
            guard.gid_artifact_path("Q-F0").unlink()
            art_cases["no artifact: nothing to check"] = gid_artifact_problems(
                "Q-F0", accepted=frozenset({"2" * 64}), require_real=True) == []
    chk("stages: prior_gate refuses a stub-written prior (or one whose provenance cannot show otherwise) "
        "for a non-stub run and a prior under another proposal unless the lock re-adopts it; it licenses a "
        "real prior, a stub prior for a stub run, a prior under an earlier lock and one under a re-adopted "
        "proposal", not let and all(oks), (let, oks))
    chk("stages: the qualification's G-ID artifact is held to the prior's rules (finding R3) -- refused under "
        "another proposal, with no identity, stub-written (or without provenance) for a non-stub run, or "
        "unreadable; admitted under the run's proposal or a re-adopted one, and a stub one for a stub run",
        all(art_cases.values()), art_cases)

    # ... and the drivers apply it: G-ID end to end, non-stub and stub
    def run_gid(out: Path, prior: Path, adapter=None, **kw):
        _schedule.write_schedule_files(Path(out) / "schedules")
        cells = {("A0s", j): c for j, c in enumerate(
            _schedule.gate_schedule("Q-F0", "id", "A0s", _schedule.roster_for("Q-F0"), _schedule.GATE_MAX))}
        ad = adapter or testing.ScriptedAdapter()
        ad.load(_script_policy("Q-F0", "id", cells), None)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            res = run_gid_pair(ad, unit="Q-F0", identity_extra=kw.pop("identity_extra", xtra(None)),
                               prior_ckpt=prior, out_root=out, **kw)
        return res, buf.getvalue(), ad
    drv = {}
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)

        def time_prior(tag: str, proposal: str, prov: Mapping) -> Path:
            tpls = list(keys.templates("Q-F0"))
            ident = _resume.Identity(unit="Q-F0", stage="time", template_set=tpls, lock_sha256="1" * 64,
                                     schedule_sha256="3" * 64, path="uncached", hour_cap=None,
                                     n={t: 1 for t in tpls}, audit_v2_sha16="4" * 16, ban_sha="5" * 16,
                                     backend_identifier="6" * 16, proposal_sha256=proposal)
            pth = td / f"prior_{tag}.json"
            ck_ = _resume.load_or_init(pth, ident, False)
            _resume.append_provenance(ck_, prov, stamp="2026-10-06T00:00:00Z")
            _record_stage_end(ck_, "PASS", [])
            _resume.write_checkpoint(pth, ck_)
            return pth
        real_rec = {"adapter": "qwen_mlx", "apparatus": "mlx", "platform": "selftest"}
        gid_x = xtra(None, proposal_sha256=real_psha, lock_sha256=real_lsha, lock_file=lock_rel,
                     proposal_file=PROPOSAL_REL, analyzer_sha256=real_asha, package_sha256=pkg_now)
        for nm, prior_p, nonstub_run, x, needle in (
                ("non-stub run, stub prior", time_prior("stub", real_psha, testing.ScriptedAdapter().provenance()),
                 True, gid_x, "PRIOR STAGE ON THE STUB"),
                ("non-stub run, real prior", time_prior("real", real_psha, real_rec), True, gid_x, None),
                ("stub run, prior under another proposal", time_prior("other", "9" * 64, real_rec), False,
                 xtra(None), "ANOTHER PROPOSAL"),
                ("stub run, prior under a re-adopted proposal", time_prior("readopt", "9" * 64, real_rec), False,
                 xtra(None, prior_proposal_sha256s=["9" * 64]), None)):
            out_g = _resume.refuse_canonical_out(td / nm.replace(" ", "_").replace(",", "") / "m")
            adg = testing.ScriptedAdapter()
            if nonstub_run:
                # a provenance record without the stub's tag, as a model adapter's
                adg.provenance = (lambda rp_=adg.provenance: {**rp_(), "adapter": "qwen_mlx",
                                                              "apparatus": "mlx"})
            with contextlib.ExitStack() as stack:
                stack.enter_context(patched(guard, "GATES_DIR", out_g / "gates"))
                if nonstub_run:
                    for mod, attr, val in ((me, "_is_stub", lambda adapter: False), (me, "DEFAULT_OUT", out_g),
                                           (me, "ANALYZER_PATH", ana_in),
                                           (guard, "preflight_laptop", fake_preflight([])),
                                           (me, "_git", fake_git()), (me, "_committed", committed_lock(lock_both))):
                        stack.enter_context(patched(mod, attr, val))
                if needle is None:
                    res_g, _, _ = run_gid(out_g, prior_p, adapter=adg, identity_extra=x)
                    art_g = json.loads(guard.gid_artifact_path("Q-F0").read_text())
                    drv[nm] = (res_g["status"] == "PASS" and len(adg.calls) > 0
                               and art_g["identity"]["proposal_sha256"] == x["proposal_sha256"]
                               and written_on_stub(art_g) is (not nonstub_run))
                else:
                    drv[nm] = (refused_start(lambda: run_gid(out_g, prior_p, adapter=adg, identity_extra=x),
                                             needle)
                               and not adg.calls and not (out_g / "ckpt").exists())
    chk("stages: the drivers gate the prior -- a non-stub G-ID refuses a stub-written G-TIME and runs on "
        "a real one; a G-ID refuses a G-TIME under another proposal and runs on one its lock re-adopts -- "
        "refusals before any generation or write; the artifact records its proposal and provenance (a "
        "stub run's reads as stub-written)", all(drv.values()), drv)

    # the contrast arm's first-read flags (qualification report, N11)
    ch2 = lambda low, top: {"low_label_mass": low, "top1_not_label": top}   # noqa: E731
    cr_recs = ([{"template": "A0", "domain": True, "choices": [ch2(True, True), ch2(False, False)]}] * 3
               + [{"template": "A0", "domain": True, "choices": [ch2(False, False), ch2(True, True)]}] * 2
               + [{"template": "A0", "domain": False, "choices": []},
                  {"template": "A0s", "domain": True, "choices": [ch2(True, True)]}])
    cfr = _contrast_first_reads("Q-F0", cr_recs)["A0"]
    cfr0 = _contrast_first_reads("Q-F0", cr_recs[3:])["A0"]
    chk("stages: the qualification report's contrast first-read flags count the FIRST read of each "
        "contrast domain session only (3 flagged of 5; later reads and sham reads never counted)",
        (cfr["reads"], cfr["low_label_mass"], cfr["top1_not_label"]) == (5, 3, 3)
        and (cfr0["reads"], cfr0["low_label_mass"], cfr0["top1_not_label"]) == (2, 0, 0), (cfr, cfr0))

    # stage-end ordering: an interrupt between the outputs and the persisted end re-finishes
    with tempfile.TemporaryDirectory() as td:
        out_i = _resume.refuse_canonical_out(Path(td) / "refinish" / "m")
        real_w = _resume.write_checkpoint
        cut = {"n": 0}

        def cut_end(path, ck_):
            if ck_.get("stage_end") is not None and cut["n"] == 0:
                cut["n"] += 1
                raise _Interrupt("selftest: the process dies before the end is persisted")
            real_w(path, ck_)
        with patched(_resume, "write_checkpoint", cut_end):
            try:
                run_time(None, out_i)
                died = False
            except _Interrupt:
                died = True
        cp_i = out_i / "ckpt" / "Q-F0_time.json"
        rep1 = (out_i / "reports" / "Q-F0_time_report.json").read_bytes()
        reads1 = (out_i / "reports" / "Q-F0_time_reads.json").read_bytes()
        mid = json.loads(cp_i.read_text())
        ad_r = testing.ScriptedAdapter()
        res_r, txt_r, _ = run_time(None, out_i, adapter=ad_r, resume=True)
        fin = json.loads(cp_i.read_text())
        refin = (died and "stage_end" not in mid and len(mid["sessions"]) == 2
                 and res_r["status"] == "PASS" and not ad_r.calls
                 and (out_i / "reports" / "Q-F0_time_report.json").read_bytes() == rep1
                 and (out_i / "reports" / "Q-F0_time_reads.json").read_bytes() == reads1
                 and fin["stage_end"]["status"] == "PASS"
                 and [e["launched"] for e in fin["provenance"]] == [2, 0]
                 and txt_r.startswith("PROVENANCE: "))
    chk("stages: the end is persisted LAST -- interrupted after the report and reads were written, the "
        "checkpoint has no end; the re-invocation launches nothing, re-finishes byte-identical report and "
        "reads, persists the end, and records its own provenance entry (0 launches)", refin,
        (died, res_r["status"], [e["launched"] for e in fin.get("provenance", [])]))

    # ruling (n): the governing-sections check a lock records, both directions
    def h256(x: str) -> str:
        return hashlib.sha256(x.encode("utf-8")).hexdigest()

    with tempfile.TemporaryDirectory() as td:
        old, new = Path(td) / "old.md", Path(td) / "new.md"
        body = "# P\n## §3 Rule\nalpha beta\n## §4 Next\ngamma\n## §5 End\nomega\n"
        old.write_text(body, encoding="utf-8")
        new.write_text(body.replace("gamma", "GAMMA").replace("omega", "omega!"), encoding="utf-8")
        sp3, sp4 = ("## §3 Rule", "## §4 Next"), ("## §4 Next", "## §5 End")
        r_same = governing_sections_identical(old, new, [sp3])
        r_diff = governing_sections_identical(old, new, [sp3, sp4])
        gs_ok = (r_same == {"identical": True, "old_file": str(old), "new_file": str(new),
                            "sha256_old_file": h256(body),
                            "sha256_new_file": h256(body.replace("gamma", "GAMMA").replace("omega", "omega!")),
                            "spans": [
                     {"start": sp3[0], "end": sp3[1], "sha256_old": h256("## §3 Rule\nalpha beta\n"),
                      "sha256_new": h256("## §3 Rule\nalpha beta\n"), "identical": True}]}
                 and r_same["sha256_old_file"] != r_same["sha256_new_file"]
                 and r_diff["identical"] is False
                 and [s["identical"] for s in r_diff["spans"]] == [True, False]
                 and (r_diff["spans"][1]["sha256_old"], r_diff["spans"][1]["sha256_new"])
                 == (h256("## §4 Next\ngamma\n"), h256("## §4 Next\nGAMMA\n")))
        dup, miss = Path(td) / "dup.md", Path(td) / "miss.md"
        dup.write_text(body + "## §3 Rule\n", encoding="utf-8")
        miss.write_text(body.replace("## §4 Next", "## §4 Later"), encoding="utf-8")
        gs_ref = {
            "a start marker twice in the new file": lambda: governing_sections_identical(old, dup, [sp3]),
            "an end marker absent from the new file": lambda: governing_sections_identical(old, miss, [sp3]),
            "an end marker before its start": lambda: governing_sections_identical(old, new, [sp4[::-1]]),
            "no spans": lambda: governing_sections_identical(old, new, []),
            "an empty marker": lambda: governing_sections_identical(old, new, [("", "## §4 Next")]),
            "a non-str marker": lambda: governing_sections_identical(
                old, new, [("## §3 Rule".encode("utf-8"), "## §4 Next")]),
            "a span of three": lambda: governing_sections_identical(old, new, [sp3 + ("x",)]),
            "a bare string as spans": lambda: governing_sections_identical(old, new, "## §3 Rule"),
            "an unreadable file": lambda: governing_sections_identical(old, Path(td) / "absent.md", [sp3])}
        gs_bad = [k for k, fn in gs_ref.items() if not refuses(fn, ValueError)]
    chk("stages: ruling (n) -- governing_sections_identical: identical spans (a change outside every span "
        "ignored) give identical True with both span sha256 and both whole-file sha256 and paths recorded "
        "(the record a lock keeps); a changed byte inside a span gives that "
        "span False and the verdict False; refuses a marker not exactly once in either file, an end before "
        "its start, no spans, an empty or non-str marker, a malformed span, an unreadable file",
        gs_ok and not gs_bad, (gs_ok, gs_bad))

    # ruling (h): the G-TIME finish's counts-only assertion, both directions
    blk = {"contrast": True, "sessions": 1,
           "per_session": [{"s": 0, "forced_rounds_generated": 2, "excluded_at_forced": True}],
           "free_rounds": readrule.WITHHELD}
    good_rep = {"stage_report": {"templates": {"A0": blk, "A0s": {"excluded_sessions": {"audit@forced": 1}}}}}
    good_reads = {"sessions": [{"contrast": True, "rounds": [{"phase": "forced", "ri": 0, "n": 1, "text": "x"}]},
                               {"contrast": False, "rounds": [{"phase": "forced", "audit": {"claim": "v2"}}]}]}

    def rep_with(**over) -> dict:
        b = copy.deepcopy(blk)
        b.update(over)
        return {"stage_report": {"templates": {"A0": b}}}

    def reads_with(rd: dict, **top) -> dict:
        return {"sessions": [{"contrast": True, "rounds": [rd], **top}]}

    tc_bad = {
        "the class-bearing contrast block": (rep_with(excluded_at_forced={"audit@forced": 1}), good_reads),
        "a claim count beside the counts": (rep_with(claims={"v2": 1}), good_reads),
        "a class in a per-session entry": (rep_with(per_session=[{**blk["per_session"][0], "class": "v2"}]),
                                           good_reads),
        "excluded yes/no as an int": (rep_with(per_session=[{**blk["per_session"][0], "excluded_at_forced": 1}]),
                                      good_reads),
        "an audit dict in a contrast round": (good_rep, reads_with({"phase": "forced", "ri": 0, "n": 1, "text": "x",
                                                                    "audit": {"claim": "v2"}})),
        "a round label": (good_rep, reads_with({"phase": "forced", "ri": 0, "n": 1, "text": "x", "label": "x"})),
        "an exclusion record": (good_rep, reads_with({"phase": "forced", "ri": 0, "n": 1, "text": "x"},
                                                     exclusion={"class": "v2", "phase": "forced"})),
        "a domain flag": (good_rep, reads_with({"phase": "forced", "ri": 0, "n": 1, "text": "x"}, domain=True))}
    tc_fired = [k for k, (rp, rd) in tc_bad.items()
                if not refuses(lambda rp=rp, rd=rd: _assert_time_counts_only("Q-F0", rp, rd), ValueError)]
    tc_silent = []
    for k, (rp, rd) in {"the counts-only block, sham classes beside": (good_rep, good_reads),
                        "no records (a G-VER stop on the first launch)": ({"stage_report": None}, {"sessions": []}),
                        "OLMo's templates": ({"stage_report": {"templates": {"A0-OLMo-sft": blk}}}, good_reads)}.items():
        try:
            _assert_time_counts_only("Q-F0" if "OLMo" not in k else "OLMo-sft", rp, rd)
        except ValueError:
            tc_silent.append(k)
    chk("stages: ruling (h) -- the G-TIME finish refuses (before any write) a report whose contrast block is "
        "not counts only or a contrast read carrying a class, round label, exclusion or domain field; it is "
        "silent on the counts-only form (sham classes beside), on a stage with no records, on OLMo",
        not tc_fired and not tc_silent, (tc_fired, tc_silent))

    # the seat's C9(ii) (2026-10-10; m:330): a campaign ended by STOP evaluates and records the bars'
    # cumulative counts at the STOP point as its last look; stub campaigns through run_campaign
    CC9 = {"A0": 64, "A0s": 32}                    # the launch-count projection; the cells the stub serves
    CF9 = {"A0": 24, "A0s": 20}
    roster9 = _schedule.roster_for("Q-F0")
    cells9: dict = {}
    for t9, m9 in CC9.items():
        cs9 = _schedule.campaign_schedule("Q-F0", t9, roster9, -(-m9 // _schedule.UNIT_SIZE))[:m9]
        cells9.update({(t9, s9): c9 for s9, c9 in enumerate(cs9)})
    real_run9 = run_session_qwen

    def tamper9(tpl: str, s_: int):
        # selftest only: the record of (tpl, s_) is edited after the runner returns, so G-VER fails it
        def tampered(adapter, sc, audit_, ban_ids, *, path_cached, term_rx):
            rec = real_run9(adapter, sc, audit_, ban_ids, path_cached=path_cached, term_rx=term_rx)
            if sc.template == tpl and sc.s == s_:
                rec["rounds"][0]["text"] += " x"
            return rec
        return tampered

    @contextlib.contextmanager
    def kill9():
        # selftest only: the finish's first output write dies -- the end is pending on disk, nothing printed
        real_w = _write_json
        state = {"n": 0}

        def w(path, obj):
            if state["n"] == 0:
                state["n"] += 1
                raise _Interrupt("selftest: killed with the end pending, before any output")
            real_w(path, obj)
        with patched(me, "_write_json", w):
            yield

    def announced9(text: str) -> list[str]:
        return [ln for ln in text.splitlines() if ln.startswith(("BAR ", "STOP ", "PAUSE ", "END LOOK "))]

    with tempfile.TemporaryDirectory() as td9, patched(guard, "GATES_DIR", Path(td9) / "no-gates"):
        def root9(name: str) -> Path:
            r = _resume.refuse_canonical_out(Path(td9) / name / "m")
            _schedule.write_schedule_files(r / "schedules")
            tpls = list(keys.templates("Q-F0"))
            ident = _resume.Identity(unit="Q-F0", stage="qual", template_set=tpls, lock_sha256="1" * 64,
                                     schedule_sha256="3" * 64, path="uncached", hour_cap=None,
                                     n={t: 1 for t in tpls}, audit_v2_sha16="4" * 16, ban_sha="5" * 16,
                                     backend_identifier="6" * 16, proposal_sha256="2" * 64)
            pr = r / "ckpt" / "Q-F0_qualprior.json"
            pr.parent.mkdir(parents=True, exist_ok=True)
            ck_ = _resume.load_or_init(pr, ident, False)
            _record_stage_end(ck_, "PASS", [])
            _resume.write_checkpoint(pr, ck_)
            return r

        def camp9(root: Path, rule=None, floors=CF9, **kw):
            ad = testing.ScriptedAdapter()
            ad.load(_script_policy("Q-F0", "campaign", cells9, rule), None)
            buf = io.StringIO()
            res = exc = None
            with contextlib.redirect_stdout(buf):
                try:
                    res = run_campaign(ad, unit="Q-F0", floors=floors, launch_counts=CC9, hour_cap=10.0,
                                       prior_ckpt=root / "ckpt" / "Q-F0_qualprior.json", identity_extra=xtra(),
                                       substrate="qwen", out_root=root, **kw)
                except (SystemExit, _Interrupt, ValueError) as e:
                    exc = e
            cp_ = root / "ckpt" / "Q-F0_campaign.json"
            ck_ = json.loads(cp_.read_text(encoding="utf-8")) if cp_.is_file() else {}
            rp_ = root / "reports" / "Q-F0_campaign_report.json"
            rep_ = json.loads(rp_.read_text(encoding="utf-8")) if rp_.is_file() else {}
            ap_ = root / "ckpt" / "Q-F0_campaign_adjudication.json"
            ev_ = json.loads(ap_.read_text(encoding="utf-8"))["events"] if ap_.is_file() else []
            return {"res": res, "exc": exc, "txt": buf.getvalue(), "ad": ad, "ck": ck_, "rep": rep_, "ev": ev_}

        def stop_lines9(ck_: Mapping) -> list[str]:
            return announce_stop("Q-F0", "campaign", _hit_from_stop(ck_["stop"]))[0]

        # (a) a hair trigger on a sham session at launch 4 (not a multiple of 40): the end look "end" at 4,
        # its messages after the STOP lines; killed with the end pending, the re-finish prints the same lines
        rule_a = lambda t, s, n, c: "<|im_end|>" if (t == "A0s" and s == 1 and n == 7) else None   # noqa: E731
        a_ref = camp9(root9("c9_a_ref"), rule_a)
        r_ak = root9("c9_a_kill")
        with kill9():
            a_kill = camp9(r_ak, rule_a)
        mid_a = json.loads((r_ak / "ckpt" / "Q-F0_campaign.json").read_text(encoding="utf-8"))
        a_re = camp9(r_ak, rule_a)
        el_a = a_ref["ck"].get("campaign", {}).get("end_look") or {}
        ok_a = (a_ref["exc"] is None and a_ref["res"]["status"] == "STOP" and len(a_ref["ck"]["sessions"]) == 4
                and el_a.get("look") == "end" and el_a.get("at_launches") == 4 and "end_is_look" not in el_a
                and a_ref["ck"]["campaign"]["pauses"] == [] and a_ref["ck"]["looks"] == []
                and announced9(a_ref["txt"]) == stop_lines9(a_ref["ck"]) + [r["message"] for r in el_a["results"]]
                and len(el_a["results"]) == 3 and all("look=end" in r["message"] for r in el_a["results"])
                and a_ref["rep"].get("end_look") == el_a and a_ref["rep"].get("looks_count") == 1
                and a_ref["rep"].get("status") == "STOP"
                and [e["event"] for e in a_ref["ev"]] == ["STOP"])
        ok_a_re = (isinstance(a_kill["exc"], _Interrupt) and announced9(a_kill["txt"]) == []
                   and (mid_a.get("end_pending") or {}).get("status") == "STOP"
                   and isinstance(mid_a["end_pending"].get("end_look"), dict)
                   and a_re["exc"] is None and a_re["res"]["status"] == "STOP" and not a_re["ad"].calls
                   and "RE-FINISH campaign-Q-F0" in a_re["txt"]
                   and announced9(a_re["txt"]) == announced9(a_ref["txt"])
                   and _resume.same_json(a_re["ck"]["campaign"]["end_look"], el_a))
        chk("stages: C9(ii) -- a hair-trigger STOP at launch 4 (not a multiple of 40) records the end look 'end' at 4 "
            "launches (no pause: silent), its three bar messages announced right after the STOP lines; the report "
            "carries it (looks counted 1); killed with that end pending, the re-finish launches nothing and prints "
            "exactly the uninterrupted run's lines", ok_a and ok_a_re,
            (a_ref["res"] and a_ref["res"]["status"], announced9(a_ref["txt"])[:3], ok_a_re))

        # (b) a hair trigger at launch 40, on the session whose look 1 fires: the look never announced before the
        # hit -- the end look IS look 1, its pause (kind look, look 1) appended unadjudicated, its messages once
        rule_b = lambda t, s, n, c: ("<|im_end|>" if (t == "A0s" and s == 19 and n == 7)        # noqa: E731
                                     else "Config choice one." if (t == "A0s" and n == 6) else None)
        r_b = root9("c9_b")
        b = camp9(r_b, rule_b)
        lk_b = b["ck"]["looks"][0]["result"] if b["ck"].get("looks") else {}
        el_b = (b["ck"].get("campaign") or {}).get("end_look") or {}
        ann_b = announced9(b["txt"])
        sl_b = stop_lines9(b["ck"]) if b["ck"].get("stop") else []
        ok_b = (b["exc"] is None and b["res"]["status"] == "STOP" and len(b["ck"]["sessions"]) == 40
                and lk_b.get("fired") is True and el_b.get("end_is_look") == 1 and el_b.get("at_launches") == 40
                and b["ck"]["campaign"]["pauses"] == [{"at_launches": 40, "kind": "look", "look": 1,
                                                       "bars": [r["name"] for r in lk_b["results"] if r["fired"]],
                                                       "adjudication": None}]
                and ann_b == sl_b + [r["message"] for r in lk_b["results"]]
                and sum("look=1" in ln for ln in b["txt"].splitlines()) == len(lk_b["results"])
                and [(e["event"], e["kind"], e["at_launches"]) for e in b["ev"]]
                == [("PAUSE", "look", 40), ("STOP", "hair_trigger", 40)] and b["ev"][0]["counts"] == lk_b
                and b["rep"].get("looks_count") == 1
                and b["rep"].get("pauses") == [{"kind": "look", "at_launches": 40, "adjudicated": False,
                                                "adjudication_sha16": None}])
        cp_b = r_b / "ckpt" / "Q-F0_campaign.json"
        bytes_b = cp_b.read_bytes()
        rep_bytes_b = (r_b / "reports" / "Q-F0_campaign_report.json").read_bytes()
        b_adj = camp9(r_b, rule_b, resume=True, adjudication="selftest: the seat's ruling on look 1")
        ok_b_ref = (isinstance(b_adj["exc"], SystemExit) and "STAGE ENDED" in str(b_adj["exc"])
                    and "(STOP" in str(b_adj["exc"]) and not b_adj["ad"].calls and cp_b.read_bytes() == bytes_b
                    and (r_b / "reports" / "Q-F0_campaign_report.json").read_bytes() == rep_bytes_b)
        chk("stages: C9(ii) -- a hair-trigger STOP on launch 40 whose look 1 fires: the end look IS look 1 (end_is_look "
            "1), its pause {kind look, look 1} appended unadjudicated (excerpt: the PAUSE event before the STOP event), "
            "look 1's bar messages announced once, after the STOP lines; the stopped campaign re-invoked with an "
            "adjudication is refused (STAGE ENDED, STOP), nothing launched, checkpoint and report unchanged -- the "
            "pause's ruling enters VERDICTS as the declared --adjudication file (the seat's C9(i))",
            ok_b and ok_b_ref, (b["res"] and b["res"]["status"], ann_b[2:3], ok_b_ref))

        # (c) a G-VER STOP right after look 1 at 40 (fired, PAUSE, adjudicated): the end look IS look 1, no new
        # pause, and the END LOOK line after the STOP lines (look 1's messages never re-announced)
        rule_c = lambda t, s, n, c: "Config choice one." if (t == "A0s" and n == 6) else None     # noqa: E731
        r_c = root9("c9_c")
        c1 = camp9(r_c, rule_c)
        with patched(me, "run_session_qwen", tamper9("A0", 20)):
            c2 = camp9(r_c, rule_c, resume=True, adjudication="selftest: continue")
        el_c = (c2["ck"].get("campaign") or {}).get("end_look") or {}
        ok_c = (c1["res"] is not None and c1["res"]["status"] == "PAUSE" and c2["exc"] is None
                and c2["res"]["status"] == "STOP" and len(c2["ck"]["sessions"]) == 40
                and c2["ck"]["stop"]["bar"] == _verify.BREAK and el_c.get("end_is_look") == 1
                and el_c.get("at_launches") == 40
                and [(p["kind"], p["at_launches"], p["adjudication"]) for p in c2["ck"]["campaign"]["pauses"]]
                == [("look", 40, "selftest: continue")]
                and announced9(c2["txt"]) == stop_lines9(c2["ck"])
                + ["END LOOK campaign-Q-F0: the end look is look 1 (at 40 launches)"]
                and "look=1" not in c2["txt"] and c2["rep"].get("looks_count") == 1
                and [(e["event"], e["kind"]) for e in c2["ev"]] == [("PAUSE", "look"), ("STOP", "harness")])
        chk("stages: C9(ii) -- a G-VER STOP at launch 41, after look 1 at 40 fired and was adjudicated: the end look IS "
            "look 1 (end_is_look 1, at 40 -- the quarantined record not counted), no new pause, and the END LOOK line "
            "follows the STOP lines (look 1's messages not re-announced)", ok_c,
            (c2["res"] and c2["res"]["status"], announced9(c2["txt"])[-1:]))

        # (d) a G-VER STOP at the first launch: no session recorded, no look -- end_look None
        with patched(me, "run_session_qwen", tamper9("A0", 0)):
            d = camp9(root9("c9_d"), None, floors={"A0": 2, "A0s": 2})
        ok_d = (d["exc"] is None and d["res"]["status"] == "STOP" and d["ck"]["sessions"] == []
                and d["ck"]["campaign"]["end_look"] is None and d["ck"]["campaign"]["pauses"] == []
                and announced9(d["txt"]) == stop_lines9(d["ck"]) and d["rep"].get("end_look") is None
                and d["rep"].get("looks_count") == 0)
        chk("stages: C9(ii) -- a G-VER STOP at the first launch records no end look (end_look None, no pause, looks "
            "counted 0) and announces the STOP lines only", ok_d, (d["res"] and d["res"]["status"], announced9(d["txt"])))

        # (e) a contrast session's FREE-phase hair trigger (blinded, m:318 exception (1)) at launch 7, after 3/3
        # forced-phase (pre-pick) exclusions on the contrast arm: the end look at 7 is present and fires (the .20
        # absolute guard, binding on Qwen) -- pick-free, the withheld class in no stdout line, report or end-look
        # event; it does not depend on the stopped session's free rounds (the trigger at round 9 gives the same)
        def rule_e(n_hit: int):
            return lambda t, s, n, c: ("<|im_end|>" if (t == "A0" and s == 3 and n == n_hit)     # noqa: E731
                                       else "Config choice one." if (t == "A0" and s < 3 and n == 1) else None)
        cls9 = ("scaffold", "absorption")
        e_ref = camp9(root9("c9_e_ref"), rule_e(7))
        e_9 = camp9(root9("c9_e_9"), rule_e(9))
        r_ek = root9("c9_e_kill")
        with kill9():
            e_kill = camp9(r_ek, rule_e(7))
        mid_e = json.loads((r_ek / "ckpt" / "Q-F0_campaign.json").read_text(encoding="utf-8"))
        mid_e_ok = True
        try:
            _resume.read_checkpoint(r_ek / "ckpt" / "Q-F0_campaign.json")
        except SystemExit:
            mid_e_ok = False
        e_re = camp9(r_ek, rule_e(7))
        el_e = (e_ref["ck"].get("campaign") or {}).get("end_look") or {}
        pz_e = e_ref["ck"]["campaign"]["pauses"] if e_ref["ck"] else []
        ev_e = e_ref["ev"]

        def after_session9(text: str, sess: str) -> list[str]:
            # every stdout line, unfiltered, between the stopped session's own line and the STAGE line
            ls_ = text.splitlines()
            i0 = max((i for i, ln in enumerate(ls_) if ln.startswith(sess)), default=None)
            i1 = next((i for i, ln in enumerate(ls_) if ln.startswith("STAGE ")), None)
            return ls_[i0 + 1:i1] if i0 is not None and i1 is not None and i0 < i1 else ["<no session/STAGE line>"]

        def stdout9(text: str, root_name: str) -> list[str]:
            # the run's whole stdout, its out root's name normalised and the stamped PROVENANCE line dropped
            return [ln.replace(root_name, "<root>") for ln in text.splitlines() if not ln.startswith("PROVENANCE")]
        ok_e = (e_ref["exc"] is None and e_ref["res"]["status"] == "STOP" and len(e_ref["ck"]["sessions"]) == 7
                and e_ref["ck"]["stop"]["blinded"]["bar"] == WITHHELD_CLASS
                and el_e.get("look") == "end" and el_e.get("at_launches") == 7 and el_e.get("fired") is True
                and pz_e == [{"at_launches": 7, "kind": "end_look", "look": "end",
                              "bars": [r["name"] for r in el_e["results"] if r["fired"]], "adjudication": None}]
                and announced9(e_ref["txt"]) == stop_lines9(e_ref["ck"]) + [r["message"] for r in el_e["results"]]
                and after_session9(e_ref["txt"], "campaign A0 s=3 ")
                == stop_lines9(e_ref["ck"]) + [r["message"] for r in el_e["results"]]
                and "free phase of a contrast session (A0 s=3)" in e_ref["txt"]
                and not any(w in e_ref["txt"].lower() for w in cls9)
                and not any(w in json.dumps(e_ref["rep"]).lower() for w in cls9) and e_ref["rep"].get("end_look") == el_e
                and [(e["event"], e["kind"]) for e in ev_e] == [("PAUSE", "end_look"), ("STOP", "hair_trigger")]
                and ev_e[0]["counts"] == el_e and not any(w in json.dumps(ev_e[:-1]).lower() for w in cls9)
                and not _ROSTER_RX.search(json.dumps(el_e)) and not _ROSTER_RX.search(json.dumps(ev_e[:-1]))
                and e_9["exc"] is None and e_9["res"]["status"] == "STOP"
                and _resume.same_json(e_9["ck"]["campaign"]["end_look"], el_e)
                and stdout9(e_9["txt"], "c9_e_9") == stdout9(e_ref["txt"], "c9_e_ref")
                and len(e_9["ck"]["sessions"][-1]["rounds"]) != len(e_ref["ck"]["sessions"][-1]["rounds"]))
        ok_e_re = (isinstance(e_kill["exc"], _Interrupt) and announced9(e_kill["txt"]) == [] and mid_e_ok
                   and _resume._pending_problem(mid_e, "campaign") is None
                   and (mid_e.get("end_pending") or {}).get("status") == "STOP"
                   and isinstance(mid_e["end_pending"].get("pause"), dict)
                   and mid_e["end_pending"]["fired"]
                   == [mid_e["end_pending"]["stop"]["bar"]] + list(mid_e["end_pending"]["pause"]["bars"])
                   and e_re["exc"] is None and e_re["res"]["status"] == "STOP" and not e_re["ad"].calls
                   and announced9(e_re["txt"]) == announced9(e_ref["txt"])
                   and not any(w in e_re["txt"].lower() for w in cls9))
        chk("stages: C9(ii) -- a contrast free-phase hair-trigger STOP (blinded) at launch 7 after 3 pre-pick exclusions "
            "on the contrast arm: the end look at 7 fires and its end_look pause is appended unadjudicated (excerpt: "
            "PAUSE then STOP; the pending end's fired = the hit's bar + the pause's bars); stdout from the stopped "
            "session's line to the STAGE line is exactly the phase-only STOP line then the end look's messages (no "
            "prefix filter), and the withheld class appears, in any case, in no stdout line, nor in the report, nor in "
            "any excerpt event but the STOP's own (m:318 exception (1)); the end look is roster-free and identical, and "
            "the whole stdout byte-identical (paths normalised, PROVENANCE dropped), when the trigger fires at round 9 "
            "instead of 7 (it reads and prints no free-phase event); killed with that end pending (resume accepts it: "
            "STOP, end look and pause dicts) the re-finish prints the same lines", ok_e and ok_e_re,
            (e_ref["res"] and e_ref["res"]["status"], announced9(e_ref["txt"])[:1], ok_e_re))
        # the pick-free assertion covers the end look at a STOP: a roster word planted in it refuses the finish
        real_cl9 = campaign_look
        word9 = roster9[0][0]

        def planted9(unit, records, look):
            out = real_cl9(unit, records, look)
            return {**out, "planted": word9} if look == "end" else out
        r_ep = root9("c9_e_plant")
        with patched(me, "campaign_look", planted9):
            e_pl = camp9(r_ep, rule_e(7))
        ck_pl = json.loads((r_ep / "ckpt" / "Q-F0_campaign.json").read_text(encoding="utf-8"))
        chk("stages: C9(ii) -- _campaign_outputs' pick-free assertion runs over the report that carries the end look at "
            "a STOP: a roster label planted in that end look refuses the finish (ValueError) before any write of the "
            "end or an output; unplanted, the same run finishes (above)",
            isinstance(e_pl["exc"], ValueError) and "roster label" in str(e_pl["exc"])
            and "end_pending" not in ck_pl and ck_pl.get("stop") is None
            and not (r_ep / "reports" / "Q-F0_campaign_report.json").exists()
            and not (r_ep / "ckpt" / "Q-F0_campaign_adjudication.json").exists() and ok_e,
            type(e_pl["exc"]).__name__)

        def msgs9(look: Mapping) -> list[str]:
            return [r["message"] for r in look.get("results") or []]

        def look1_9(ck_: Mapping) -> dict:
            return ck_["looks"][0]["result"] if ck_.get("looks") else {}

        def end_look9(ck_: Mapping) -> dict:
            return (ck_.get("campaign") or {}).get("end_look") or {}
        end_line9 = "END LOOK campaign-Q-F0: the end look is look 1 (at 40 launches)"

        # (f) (b)'s silent variant: a hair trigger at launch 40 on a session whose look 1 is SILENT -- the end look
        # IS look 1, no pause; look 1 (never announced before the hit) has its three messages after the STOP lines,
        # once, and no END LOOK line; killed with that end pending, the re-finish prints the same lines
        rule_f = lambda t, s, n, c: "<|im_end|>" if (t == "A0s" and s == 19 and n == 7) else None   # noqa: E731
        f_ref = camp9(root9("c9_f_ref"), rule_f)
        r_fk = root9("c9_f_kill")
        with kill9():
            f_kill = camp9(r_fk, rule_f)
        f_re = camp9(r_fk, rule_f)
        lk_f, el_f = look1_9(f_ref["ck"]), end_look9(f_ref["ck"])
        ok_f = (f_ref["exc"] is None and f_ref["res"]["status"] == "STOP" and len(f_ref["ck"]["sessions"]) == 40
                and lk_f.get("fired") is False and el_f.get("end_is_look") == 1 and el_f.get("at_launches") == 40
                and f_ref["ck"]["campaign"]["pauses"] == [] and len(msgs9(lk_f)) == 3
                and announced9(f_ref["txt"]) == stop_lines9(f_ref["ck"]) + msgs9(lk_f)
                and sum("look=1" in ln for ln in f_ref["txt"].splitlines()) == 3 and "END LOOK" not in f_ref["txt"]
                and [e["event"] for e in f_ref["ev"]] == ["STOP"] and f_ref["rep"].get("pauses") == []
                and f_ref["rep"].get("looks_count") == 1)
        ok_f_re = (isinstance(f_kill["exc"], _Interrupt) and announced9(f_kill["txt"]) == []
                   and f_re["exc"] is None and f_re["res"]["status"] == "STOP" and not f_re["ad"].calls
                   and "RE-FINISH campaign-Q-F0" in f_re["txt"] and announced9(f_re["txt"]) == announced9(f_ref["txt"])
                   and f_re["ck"]["campaign"]["pauses"] == [] and _resume.same_json(end_look9(f_re["ck"]), el_f))
        chk("stages: C9(ii) -- a hair-trigger STOP on launch 40 whose look 1 is silent ((b)'s silent variant): the end "
            "look IS look 1 (end_is_look 1), no pause appended (excerpt: the STOP event only), look 1's three bar "
            "messages announced once, right after the STOP lines, and no END LOOK line; killed with that end pending, "
            "the re-finish launches nothing and prints exactly the same lines", ok_f and ok_f_re,
            (f_ref["res"] and f_ref["res"]["status"], announced9(f_ref["txt"])[-1:], ok_f_re))

        # (g) (c)'s silent variant: a G-VER STOP at launch 41 after a SILENT look 1 at 40 -- look 1 announced at its
        # launch, the end look IS look 1, no pause, and the END LOOK line alone after the STOP lines
        with patched(me, "run_session_qwen", tamper9("A0", 20)):
            g9 = camp9(root9("c9_g"), None)
        lk_g, el_g = look1_9(g9["ck"]), end_look9(g9["ck"])
        ok_g = (g9["exc"] is None and g9["res"]["status"] == "STOP" and len(g9["ck"]["sessions"]) == 40
                and (g9["ck"].get("stop") or {}).get("bar") == _verify.BREAK and lk_g.get("fired") is False
                and el_g.get("end_is_look") == 1 and el_g.get("at_launches") == 40
                and g9["ck"]["campaign"]["pauses"] == [] and len(msgs9(lk_g)) == 3
                and announced9(g9["txt"]) == msgs9(lk_g) + stop_lines9(g9["ck"]) + [end_line9]
                and sum("look=1" in ln for ln in g9["txt"].splitlines()) == 3
                and [(e["event"], e["kind"]) for e in g9["ev"]] == [("STOP", "harness")]
                and g9["rep"].get("looks_count") == 1)
        chk("stages: C9(ii) -- a G-VER STOP at launch 41 after a silent look 1 at 40 ((c)'s silent variant): the end "
            "look IS look 1 (end_is_look 1, at 40), no pause, look 1's messages printed once (at its launch) and the "
            "END LOOK line alone after the STOP lines", ok_g,
            (g9["res"] and g9["res"]["status"], announced9(g9["txt"])[-1:]))

        # (h) a STOP past a cadence look, on a launch count that is not a multiple of 40: a hair trigger at launch 42
        # (A0 s=21, after the sham arm's floor) -- the end look is evaluated at 42 ('end'), never look 1 at 40 reused
        rule_h = lambda t, s, n, c: "<|im_end|>" if (t == "A0" and s == 21 and n == 7) else None    # noqa: E731
        h9 = camp9(root9("c9_h"), rule_h)
        lk_h, el_h = look1_9(h9["ck"]), end_look9(h9["ck"])
        ok_h = (h9["exc"] is None and h9["res"]["status"] == "STOP" and len(h9["ck"]["sessions"]) == 42
                and [lk["at_launches"] for lk in h9["ck"].get("looks") or []] == [40]
                and el_h.get("look") == "end" and el_h.get("at_launches") == 42 and "end_is_look" not in el_h
                and h9["ck"]["campaign"]["pauses"] == [] and len(msgs9(el_h)) == 3
                and announced9(h9["txt"]) == msgs9(lk_h) + stop_lines9(h9["ck"]) + msgs9(el_h)
                and all("look=end" in m_ for m_ in msgs9(el_h))
                and sum("look=end" in ln for ln in h9["txt"].splitlines()) == 3
                and sum("look=1" in ln for ln in h9["txt"].splitlines()) == 3 and "END LOOK" not in h9["txt"]
                and h9["rep"].get("end_look") == el_h and h9["rep"].get("looks_count") == 2
                and [e["event"] for e in h9["ev"]] == ["STOP"])
        chk("stages: C9(ii) -- a hair-trigger STOP at launch 42, past look 1 at 40 (not a multiple of 40): the end look "
            "is evaluated at the STOP point (look 'end' at 42, no end_is_look -- look 1 is not reused), its three "
            "messages after the STOP lines (look 1's printed once, at 40), the report counting 2 looks", ok_h,
            (h9["res"] and h9["res"]["status"], el_h.get("look"), el_h.get("at_launches")))

        # (i) a G-VER STOP whose freshly evaluated end look FIRES: A0 s=3's record quarantined at launch 7 after 3/3
        # forced-phase exclusions on the contrast arm -- the end look at 6 fires, its end_look pause appended
        # unadjudicated (the analyzer's PIN-9 then requires the seat's --adjudication), fired = the G-VER bar + the
        # pause's bars; killed with that end pending, the re-finish prints the same lines
        rule_i = lambda t, s, n, c: "Config choice one." if (t == "A0" and s < 3 and n == 1) else None  # noqa: E731
        with patched(me, "run_session_qwen", tamper9("A0", 3)):
            i_ref = camp9(root9("c9_i_ref"), rule_i)
        r_ik = root9("c9_i_kill")
        with patched(me, "run_session_qwen", tamper9("A0", 3)), kill9():
            i_kill = camp9(r_ik, rule_i)
        mid_i = json.loads((r_ik / "ckpt" / "Q-F0_campaign.json").read_text(encoding="utf-8"))
        el_i = end_look9(i_ref["ck"])
        bars_i = [r["name"] for r in el_i.get("results") or [] if r["fired"]]
        pe_i = mid_i.get("end_pending") or {}
        ok_i = (i_ref["exc"] is None and i_ref["res"]["status"] == "STOP" and len(i_ref["ck"]["sessions"]) == 6
                and (i_ref["ck"].get("stop") or {}).get("bar") == _verify.BREAK and i_ref["ck"]["looks"] == []
                and el_i.get("look") == "end" and el_i.get("at_launches") == 6 and el_i.get("fired") is True
                and "end_is_look" not in el_i and bars_i
                and i_ref["ck"]["campaign"]["pauses"] == [{"at_launches": 6, "kind": "end_look", "look": "end",
                                                           "bars": bars_i, "adjudication": None}]
                and announced9(i_ref["txt"]) == stop_lines9(i_ref["ck"]) + msgs9(el_i)
                and [(e["event"], e["kind"], e["at_launches"]) for e in i_ref["ev"]]
                == [("PAUSE", "end_look", 6), ("STOP", "harness", 6)] and i_ref["ev"][0]["counts"] == el_i
                and i_ref["rep"].get("pauses") == [{"kind": "end_look", "at_launches": 6, "adjudicated": False,
                                                    "adjudication_sha16": None}]
                and i_ref["rep"].get("looks_count") == 1)
        ok_i_pe = (isinstance(i_kill["exc"], _Interrupt) and announced9(i_kill["txt"]) == []
                   and _resume._pending_problem(mid_i, "campaign") is None and pe_i.get("status") == "STOP"
                   and pe_i.get("fired") == [_verify.BREAK] + bars_i and isinstance(pe_i.get("pause"), dict))
        i_re = camp9(r_ik, rule_i)
        ok_i_re = (i_re["exc"] is None and i_re["res"]["status"] == "STOP" and not i_re["ad"].calls
                   and announced9(i_re["txt"]) == announced9(i_ref["txt"])
                   and i_re["ck"]["campaign"]["pauses"] == i_ref["ck"]["campaign"]["pauses"])
        chk("stages: C9(ii) -- a G-VER STOP at launch 7 whose end look, evaluated fresh at 6 launches, fires: its "
            "end_look pause {end_look, 6} appended unadjudicated (excerpt: PAUSE then STOP; the pending end's fired = "
            "the G-VER bar + the pause's bars), the end look's messages after the STOP lines; killed with that end "
            "pending (resume accepts it), the re-finish prints the same lines", ok_i and ok_i_pe and ok_i_re,
            (i_ref["res"] and i_ref["res"]["status"], bars_i, ok_i_pe, ok_i_re))

        # (j) NOT APPLIED names where a ruling goes when the re-finished end leaves the campaign ENDED: a STOP whose
        # end look fired ((i), killed again), and a COMPLETE campaign whose end look fired (status PAUSE, the
        # terminal state standing; the seat's C9(i)) -- each re-finished with an adjudication offered: NOT APPLIED,
        # pointing to VERDICTS' --adjudication file, never 'offer it again'; offered again, refused as ended. A
        # look pause (not ended) keeps 'offer it again'.
        adj9 = "selftest: the seat's ruling on the pause"
        r_jk = root9("c9_j_stop")
        with patched(me, "run_session_qwen", tamper9("A0", 3)), kill9():
            camp9(r_jk, rule_i)
        j_stop = camp9(r_jk, rule_i, resume=True, adjudication=adj9)
        cp_jk = r_jk / "ckpt" / "Q-F0_campaign.json"
        bytes_jk = cp_jk.read_bytes()
        j_stop2 = camp9(r_jk, rule_i, resume=True, adjudication=adj9)
        fl_j = {"A0": 1, "A0s": 1}
        r_jt = root9("c9_j_term")
        with kill9():
            camp9(r_jt, rule_i, floors=fl_j)
        j_term = camp9(r_jt, rule_i, floors=fl_j, resume=True, adjudication=adj9)
        ck_jt = json.loads((r_jt / "ckpt" / "Q-F0_campaign.json").read_text(encoding="utf-8"))
        j_term2 = camp9(r_jt, rule_i, floors=fl_j, resume=True, adjudication=adj9)
        r_jl = root9("c9_j_look")
        with kill9():
            camp9(r_jl, rule_c)
        j_look = camp9(r_jl, rule_c, resume=True, adjudication=adj9)

        def not_applied9(res_: Mapping, ended_: str | None) -> bool:
            e_ = res_["exc"]
            if not (isinstance(e_, SystemExit) and "NOT APPLIED" in str(e_) and not res_["ad"].calls):
                return False
            if ended_ is None:
                return "offer it again" in str(e_) and "--adjudication file" not in str(e_)
            return ("offer it again" not in str(e_) and f"leaves the campaign ended ({ended_})" in str(e_)
                    and "enters VERDICTS as the declared --adjudication file" in str(e_))
        ok_j = (not_applied9(j_stop, "STOP") and "end_pending" not in j_stop["ck"]
                and [(p["kind"], p["adjudication"]) for p in j_stop["ck"]["campaign"]["pauses"]] == [("end_look", None)]
                and isinstance(j_stop2["exc"], SystemExit) and "STAGE ENDED" in str(j_stop2["exc"])
                and not j_stop2["ad"].calls and cp_jk.read_bytes() == bytes_jk
                and not_applied9(j_term, "COMPLETE") and "end_pending" not in ck_jt
                and (ck_jt["campaign"].get("terminal") or {}).get("status") == "COMPLETE"
                and [(p["kind"], p["adjudication"]) for p in ck_jt["campaign"]["pauses"]] == [("end_look", None)]
                and isinstance(j_term2["exc"], SystemExit) and "CAMPAIGN ENDED" in str(j_term2["exc"])
                and not j_term2["ad"].calls
                and not_applied9(j_look, None)
                and [(p["kind"], p["adjudication"]) for p in j_look["ck"]["campaign"]["pauses"]] == [("look", None)])
        chk("stages: a re-finish offered a ruling refuses NOT APPLIED, and where the end it re-finished leaves the "
            "campaign ended -- a STOP whose end look fired, a COMPLETE whose end look fired (the seat's C9(i)) -- the "
            "refusal names the end and points the ruling to VERDICTS' declared --adjudication file, never 'offer it "
            "again' (offered again, it is refused as ended, nothing launched, the checkpoint unchanged); a look pause "
            "(not ended) keeps 'offer it again'", ok_j,
            (str(j_stop["exc"])[:60], str(j_term["exc"])[:60], str(j_look["exc"])[-60:]))

    # the seat's D2 in the G-ID and campaign drivers: the licence precedes the first write. A simulated non-stub
    # run (the G-TIME end-to-end harness's patches and its committed lock, a model adapter's provenance, a real
    # prior ended PASS under this run's proposal -- so that, the licence aside, the run would go on to write)
    # whose package_sha256 is not this process's package, or whose lock text does not name the analyzer sha, is
    # refused LICENCE REFUSED before any write or generation; the same run with everything matching prints the
    # LICENCE line and goes on to launch and write
    lock_noana = lock_naming(pkg_now)
    lic_runs = {   # name -> (identity_extra overrides, the lock's committed bytes, the problem named; None: licensed)
        "licensed": ({}, lock_both, None),
        "a package_sha256 not this process's": (
            {"package_sha256": "5" * 64, "lock_sha256": hashlib.sha256(lock_pkg5).hexdigest()}, lock_pkg5,
            "is not identity_extra's package_sha256"),
        "a lock text not naming the analyzer sha": (
            {"lock_sha256": hashlib.sha256(lock_noana).hexdigest()}, lock_noana,
            "does not name identity_extra's analyzer_sha256")}

    def real_prior_d(pth: Path, stage: str) -> Path:
        # the prior stage ended PASS under this run's proposal, written by a model adapter (prior_gate admits it
        # for a non-stub run); kept outside the out root
        tpls = list(keys.templates("Q-F0"))
        ident = _resume.Identity(unit="Q-F0", stage=stage, template_set=tpls, lock_sha256="1" * 64,
                                 schedule_sha256="3" * 64, path="uncached", hour_cap=None,
                                 n={t: 1 for t in tpls}, audit_v2_sha16="4" * 16, ban_sha="5" * 16,
                                 backend_identifier="6" * 16, proposal_sha256=real_psha)
        pth.parent.mkdir(parents=True, exist_ok=True)
        ck_ = _resume.load_or_init(pth, ident, False)
        _resume.append_provenance(ck_, {"adapter": "qwen_mlx", "apparatus": "mlx", "platform": "selftest"},
                                  stamp="2026-10-06T00:00:00Z")
        _record_stage_end(ck_, "PASS", [])
        _resume.write_checkpoint(pth, ck_)
        return pth

    def tree_d(root: Path) -> dict:
        # every path under the out root, with a file's bytes
        return {p.relative_to(root).as_posix(): (p.read_bytes() if p.is_file() else None)
                for p in sorted(root.rglob("*"))}

    def camp_d(root: Path, prior: Path, adapter, x: Mapping) -> tuple[dict, str, Any]:
        adapter.load(_script_policy("Q-F0", "campaign", cells9, None), None)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            res = run_campaign(adapter, unit="Q-F0", floors={"A0": 1, "A0s": 1}, launch_counts=CC9, hour_cap=10.0,
                               prior_ckpt=prior, identity_extra=x, substrate="qwen", out_root=root)
        return res, buf.getvalue(), adapter

    lic_d: dict[str, dict] = {"G-ID": {}, "campaign": {}}
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        for drv_nm, stage_, base_x in (("G-ID", "id", gid_x), ("campaign", "campaign", real_x)):
            sname = stage_name("Q-F0", stage_)
            for nm, (over, body, problem) in lic_runs.items():
                tag = f"{drv_nm}_{nm}".replace(" ", "_").replace("'", "")
                out_d = _resume.refuse_canonical_out(td / tag / "m")
                _schedule.write_schedule_files(out_d / "schedules")
                prior_d = real_prior_d(td / "priors" / f"{tag}.json", PRIOR_STAGE[stage_])
                x_d = {**base_x, **over}
                ad_d = testing.ScriptedAdapter()
                # a provenance record without the stub's tag, as a model adapter's
                ad_d.provenance = (lambda rp_=ad_d.provenance: {**rp_(), "adapter": "qwen_mlx", "apparatus": "mlx"})
                pths = for_checkpoint(out_paths("Q-F0", stage_, out_d), out_d / "ckpt" / f"Q-F0_{stage_}.json")
                before = tree_d(out_d)
                res_d = exc_d = None
                txt_d = ""
                with contextlib.ExitStack() as st_d:
                    for mod_, attr_, val_ in ((me, "_is_stub", lambda adapter: False), (me, "DEFAULT_OUT", out_d),
                                              (me, "ANALYZER_PATH", ana_in),
                                              (guard, "preflight_laptop", fake_preflight([])),
                                              (me, "_git", fake_git()), (me, "_committed", committed_lock(body)),
                                              (guard, "GATES_DIR", out_d / "gates")):
                        st_d.enter_context(patched(mod_, attr_, val_))
                    gid_art = guard.gid_artifact_path("Q-F0")
                    try:
                        if drv_nm == "G-ID":
                            res_d, txt_d, _ = run_gid(out_d, prior_d, adapter=ad_d, identity_extra=x_d)
                        else:
                            res_d, txt_d, _ = camp_d(out_d, prior_d, ad_d, x_d)
                    except (SystemExit, ValueError, _Interrupt) as e:
                        exc_d = e
                written = [p.name for p in (pths["ckpt"], pths["report"], pths["reads"],
                                            adjudication_path(pths["ckpt"]), gid_art) if p.exists()]
                if problem is None:
                    ck_d = json.loads(pths["ckpt"].read_text(encoding="utf-8")) if pths["ckpt"].is_file() else {}
                    lic_lines = [ln for ln in txt_d.splitlines() if ln.startswith("LICENCE ")]
                    lic_d[drv_nm][nm] = (
                        exc_d is None and res_d is not None and len(ad_d.calls) > 0
                        and len(lic_lines) == 1
                        and lic_lines[0].startswith(f"LICENCE {sname}: proposal {PROPOSAL_REL} {real_psha[:16]}, "
                                                    f"lock {lock_rel} {real_lsha[:16]}: committed at HEAD ")
                        and f"analyzer {real_asha[:16]} and package {pkg_now[:16]}: the hashes" in lic_lines[0]
                        and (ck_d.get("licence") or {}).get("package_sha256") == pkg_now
                        and (ck_d.get("licence") or {}).get("analyzer_sha256") == real_asha
                        and pths["ckpt"].name in written and pths["report"].name in written
                        and (gid_art.name in written) is (drv_nm == "G-ID"))
                else:
                    msg = str(exc_d) if isinstance(exc_d, SystemExit) else ""
                    lic_d[drv_nm][nm] = (
                        f"LICENCE REFUSED ({sname})" in msg and problem in msg
                        and not ad_d.calls and not written and tree_d(out_d) == before)
    chk("stages: the seat's D2 in the G-ID driver -- the licence precedes the first write: a simulated non-stub "
        "G-ID-F0m (a real G-TIME prior) whose package_sha256 is not this process's package, or whose lock text does "
        "not name the analyzer sha, is refused LICENCE REFUSED naming the problem before any write or generation "
        "(no checkpoint, report, reads, G-ID artifact or excerpt; the out root unchanged; no generate call); with "
        "everything matching it prints the LICENCE line (the analyzer's and the package's sha16) once, launches, "
        "writes the checkpoint recording both hashes, the report and the artifact",
        len(lic_d["G-ID"]) == len(lic_runs) and all(lic_d["G-ID"].values()), lic_d["G-ID"])
    chk("stages: the seat's D2 in the campaign driver -- the licence precedes the first write: a simulated "
        "non-stub campaign-Q-F0 (a real qualification prior) whose package_sha256 is not this process's package, "
        "or whose lock text does not name the analyzer sha, is refused LICENCE REFUSED naming the problem before "
        "any write or generation (no checkpoint, report, reads or excerpt; the out root unchanged; no generate "
        "call); with everything matching it prints the LICENCE line (the analyzer's and the package's sha16) "
        "once, launches, writes the checkpoint recording both hashes and the report",
        len(lic_d["campaign"]) == len(lic_runs) and all(lic_d["campaign"].values()), lic_d["campaign"])

    # the call-site guard holds over this file, and fires on a smuggled copy
    src = Path(__file__).read_text(encoding="utf-8")
    probs = guard.check_call_sites([Path(__file__)])
    with tempfile.TemporaryDirectory() as td:
        bad_src = src.replace("path_cached = guard.cached_path_admitted(unit, gate, backend_identifier=bid)",
                              "path_cached = True", 1)
        f = Path(td) / "stages_smuggled.py"
        f.write_text(bad_src, encoding="utf-8")
        fired = guard.check_call_sites([f])
    chk("stages: guard.check_call_sites is clean on stages.py and fires on a copy with a literal "
        "True path outside run_gid_pair", probs == [] and bad_src != src and len(fired) >= 1,
        (probs[:1], fired[:1]))
