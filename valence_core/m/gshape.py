"""PROPOSAL-m G-SHAPE-F0 -- scoring-scope plumbing, model-free (v1.11 §3.1 m:277; §8 step 7
m:358; with m:56, m:159, m:172, m:174, m:261-264, m:271).

m:277: "Model-free: every corrupted render placed inside each F0m and F0m-OLMo round template
beside its bracketed header, a clean gold as the response, run through the full scoring stack
of both substrates; asserts that no class fires on harness bytes or the render itself. It tests
scoring scope, nothing else."

THE ARTIFACT OF RECORD (``data/m/gates/G-SHAPE-F0.json``, write-once) carries three layers:

  Layer A  m:277's placements. Per unit of ``keys.UNITS_BUILT``: the 16 renders of record (READ
           from G-CAL's committed model-free artifact, asserted equal to
           ``scaffold.pool_and_renders()`` and to the pinned sha256) x ``ROUND_TEMPLATES[0..3]``
           (the same objects on both substrates) x the unit's 16 contrast banners x every stored
           gold variant (22) x both phases, the render under the Q-role label -- 2,816 per unit,
           11,264 in all -- each gold scored by that substrate's stack exactly as its runner
           calls it; a placement fires iff any field of ``ROUND_FIRE_FIELDS`` fires.
  Layer C  one scope-widened control per placement: ``seg+gold`` (the segment's harness bytes
           and the gold as one response) must fire on 100% of placements per unit (the stack
           can fire on harness bytes); ``render-as-response`` is reported only.
  Layer S  a static (ast) check of the four production classify call sites
           (``runner_qwen.run_session_qwen``, ``runner_olmo.run_session_olmo``) and
           ``scaffold.SessionLog.add_round``: the runners hand ``classify`` the generation's
           text, never the segment, banner or render (rules R1-R8).

The dynamic runner half lives in the m self-test only (the existing runner checks named in
``RUNNER_DYNAMIC_EVIDENCE`` and this module's one runner-identity check); the self-test stub is
never on a run path. The three OLMo units are one computation run three times on byte-identical
inputs; the artifact records ``olmo_grids_identical``. No model, no tokenizer, no generation.
"""
from __future__ import annotations

import ast
import contextlib
import hashlib
import json
import os
import re
import sys
from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Iterator, Mapping, Sequence

from ..e2d.audit_v3 import AUDIT_VERSION
from ..session_e2a import N_FREE, ROUND_TEMPLATES, SESSION_BANNER
from . import audit as _audit
from . import banner as _banner
from . import corr as _corr
from . import gcal as _gcal
from . import guard, keys
from . import resume as _resume
from . import runner_olmo as _ro
from . import scaffold as _sc
from . import schedule as _schedule
from . import stages as _stages

REPO = Path(__file__).resolve().parents[2]
PACKAGE_DIR = Path(__file__).resolve().parent
GATES_DIR = guard.GATES_DIR                      # data/m/gates; read at call time (selftest patches it)
OLMO_DIR = REPO / "data" / "olmo"                # scaffold_{ckpt}.json / b3_screen_{ckpt}.json; read at call time

SCHEMA = "m-gshape-f0-v1"
STAGE = "G-SHAPE-F0"
ARTIFACT_NAME = "G-SHAPE-F0.json"
SPEC_REF = "PROPOSAL-m v1.11 §3.1 G-SHAPE-F0 (m:277); §8 step 7 (m:358)"
CRITERION_HEAD = "**G-SHAPE-F0 (plumbing).**"
CRITERION = ("Model-free: every corrupted render placed inside each F0m and F0m-OLMo round template "
             "beside its bracketed header, a clean gold as the response, run through the full scoring "
             "stack of both substrates; asserts that no class fires on harness bytes or the render "
             "itself. It tests scoring scope, nothing else.")
RENDERS_SHA256_OF_RECORD = "a04f67b0e5105a0514a0f33e64a4545ef3a3a3c75cece320d78434e853cd4372"
RENDERS_RECORD_CITE = "RESULTS.md@e60b633:919-920"
MODEL_FREE_REL = "data/m/gates/G-CAL_model-free.json"
COMPLETABILITY_REL = "data/m/gates/G-CAL_completability_qwen.json"
SEAT_READ_REL = "data/m/gates/G-CAL_seat_read_of_record.md"
UNITS = keys.UNITS_BUILT                        # ("Q-F0", "OLMo-sft", "OLMo-dpo", "OLMo-instruct")
OLMO_UNITS = tuple(u for u in UNITS if u != "Q-F0")
PHASES = ("forced", "free")
N_ITEMS = 16
N_BANNERS = 16                                   # 4 pairs x 2 maps x 2 clauses
N_TEMPLATES = len(ROUND_TEMPLATES)               # 4
N_GOLD_VARIANTS = 22
N_PER_UNIT = N_BANNERS * N_TEMPLATES * N_GOLD_VARIANTS * len(PHASES)   # 2,816
N_ROUNDS = _sc.N_FORCED + N_FREE                 # 10: the n range the shape check covers
ROUND_FIRE_FIELDS = ("claim", "advisory", "v3.exclusion", "v3.content_label", "v3.advisory",
                     "echo_line", "lexical_raw", "scaffold", "degeneracy", "ends", "strict",
                     "termination")
CONTROLS_REQUIRED = ("seg+gold",)
CONTROLS_REPORTED = ("render-as-response",)
SCORING_STACK_FILES = (
    "valence_core/m/audit.py", "valence_core/m/banner.py", "valence_core/m/corr.py",
    "valence_core/m/keys.py", "valence_core/m/schedule.py", "valence_core/m/scaffold.py",
    "valence_core/m/runner_qwen.py", "valence_core/m/runner_olmo.py",
    "valence_core/session.py", "valence_core/session_e2a.py",
    "valence_core/e2d/audit_v3.py", "valence_core/e2d/contentclass.py",
    "valence_core/e2d/contentclass_v4.py", "valence_core/e2d/contentclass_v5.py",
    "valence_core/e2d/config.py",
    "data/configs/e2b_audit_v2.json", "data/configs/e2a_ban_list.json",
    "data/configs/f_termination_patterns.json", "data/f/pools.json",
    "data/olmo/a1_repair_roster.json",
    "data/olmo/scaffold_sft.json", "data/olmo/scaffold_dpo.json", "data/olmo/scaffold_instruct.json",
    "data/olmo/b3_screen_sft.json", "data/olmo/b3_screen_dpo.json", "data/olmo/b3_screen_instruct.json")
TOOLING_FILES = ("valence_core/m/gshape.py", "scripts/m_sessions.py")
CLOSURE_SCOPE = ("the sha256 of __file__ of every loaded valence_core.* module outside valence_core/m "
                 "(sys.modules read after the imports; the m package is package_sha256's)")
FIRES_LISTED_MAX = 50                            # per unit; n_fired is always exact
SHAPE_LISTED_MAX = 20
EXIT = {"PASS": 0, "STOP": 4}
STOP_REASON_FORMS = ("shape", "fire:<unit>", "coverage:<unit>", "control-silent:<unit>:<control>",
                     "olmo-grids-differ", "scope-static")
LAYER_S_RULES = ("R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8")
RUNNER_FILES = {"valence_core/m/runner_qwen.py": ("run_session_qwen", "qwen"),
                "valence_core/m/runner_olmo.py": ("run_session_olmo", "olmo")}
SCAFFOLD_REL = "valence_core/m/scaffold.py"
GSHAPE_REL = "valence_core/m/gshape.py"
B3_BAN_LIST = {"n_ids": _audit.OLMO_BAN_N_IDS, "sha16": _audit.OLMO_BAN_IDS_SHA16}
SEAMS = ("inputs", "scorer", "controls", "templates", "sources", "drop", "units")

# PIN (Code, declared at LOCK v0.1): the dynamic evidence for the runner half of scoring scope
# is the m self-test's existing runner checks below (their chk-name templates, "{}" standing
# for a computed count), plus this module's one runner-identity check (RUNNER_IDENTITY_CHECK);
# the self-test asserts each template is a chk name in its module's source, so a renamed or
# removed check fails it. They run at the package_sha256 the run of record records (PIN-S5).
# Each is cited for what it contains (ledger 30): "classify outcomes" -- its pass depends on
# what classify returned on the scripted generation text (a runner scoring segment + text
# fails it); "render placed in situ" -- the corrupted render reaches the contrast Q round's
# segment beside a clean response, which the outcome checks then see unfired. Checks that
# assert only generation-side context (the adapter's calls, the prefix and menu rule) pass
# under a runner that scores the segment, so they are not cited.
RUNNER_DYNAMIC_EVIDENCE = (
    ("runner_qwen", "classify outcomes",
     "runner_qwen: {} scripted sessions reach their declared outcomes (clean x8; forced "
     "v2/echo/content/lexical end; free v2/echo/content continue; free lexical ends; scaffold stops)"),
    ("runner_qwen", "classify outcomes",
     "runner_qwen: clean sessions -- 6 reads, valid, complete, domain, first pick coded on P"),
    ("runner_qwen", "render placed in situ",
     "runner_qwen: contrast Q rounds deliver the corrupt_m render ('corrupted'); sham and P clean"),
    ("runner_olmo", "classify outcomes",
     "runner_olmo: {} scripted sessions reach their declared outcomes (clean x8; forced "
     "AuditSpec/echo/lexical end; '* * *' continues; free echo/AuditSpec/lexical end; scaffold stops)"),
    ("runner_olmo", "classify outcomes",
     "runner_olmo: clean sessions -- 6 reads, valid, complete, over contrast/sham x both start orders x "
     "both clauses"),
    ("runner_olmo", "render placed in situ",
     "runner_olmo: items from the item key's [:8]/[8:] split; contrast Q delivers the render"),
)
RUNNER_EVIDENCE_KINDS = ("classify outcomes", "render placed in situ")
RUNNER_NOT_EVIDENCE = (                          # generation-side context only; never cited (above)
    ("runner_qwen", "runner_qwen: the adapter saw injections=() and cached=False on every call, the "
                    "recorded seed, and prefix = transcript so far (free: + menu + pick line)"),
    ("runner_olmo", "runner_olmo: context rule -- menus and pick lines reach the chosen round's prefix "
                    "only; the stored transcript and its pieces carry none; choices record menu, a, b"),
)
RUNNER_IDENTITY_CHECK = ("gshape: the runners hand classify the generation's text, never the segment, "
                         "banner or render -- every scripted runner case on both substrates through the real "
                         "run_session_qwen / run_session_olmo with recording audits: the scored text is the "
                         "adapter's emitted text and the record's; Qwen's render is the segment's Task line "
                         "and the record's task_text; item, earlier, own_pair, echo_lines and phase are the "
                         "round's; six mutated runner copies (segment, transcript or render scored; clean "
                         "text as render; OLMo segment or render scored) are each caught")


# PIN (Code, declared at LOCK v0.1; PIN-S8): a refusal (exit 2, nothing written) is anything
# decided before scoring about paths, the governing proposal, the presence and state of the
# committed inputs (G-CAL's three artifacts; the scoring-stack, tooling and m package sources and
# the import closure on the canonical run) or an existing different artifact; a precondition STOP
# (exit 4, no artifact) is a pinned figure that does not reproduce (numpy's stream, §2.5's banners,
# the renders and every renders sha256 that cites them, the pool and the pools file's sha256, the
# golds, a stack's pinned shas, conditions (1)-(2), the OLMo string files and b3 records). A STOP
# *verdict* (a fire, a coverage gap, a silent control, a shape problem, OLMo grids that differ, a
# Layer-S problem) writes its artifact with the
# evidence (G-PORT's precedent) and exits 4; Code escalates and never self-adjudicates.
class GshapeRefusal(SystemExit):
    """A G-SHAPE-F0 refusal: decided before any scoring; nothing written (exit 2)."""


class GshapeStop(SystemExit):
    """A G-SHAPE-F0 precondition STOP: a pinned figure does not reproduce; no artifact (exit 4)."""


# --- small helpers ------------------------------------------------------------------------
def _sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _sha256_text(s: str) -> str:
    return _sha256(s.encode("utf-8"))


def _json_sha256(obj: Any) -> str:
    return _sha256_text(_resume.json_text(obj))


def _substrate(unit: str) -> str:
    if unit not in UNITS:
        raise ValueError(f"unit {unit!r} is not one of {UNITS}")
    return "qwen" if unit == "Q-F0" else "olmo"


def _read_committed(rel: str) -> bytes:
    """The bytes of a file COMMITTED at HEAD whose working tree holds exactly that blob
    (stages._committed, read at call time); GshapeRefusal otherwise."""
    probs, data = _stages._committed(rel)
    if probs or data is None:
        raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: {rel}: {probs or ['no bytes']} (every input of "
                            f"record is committed at HEAD, rule 27)")
    return data


def _committed_json(rel: str) -> tuple[Any, str]:
    data = _read_committed(rel)
    try:
        return json.loads(data.decode("utf-8")), _sha256(data)
    except (UnicodeDecodeError, ValueError):
        raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: {rel} is not readable JSON") from None


# --- the governing text and the committed sources --------------------------------------------
def criterion_problems(proposal_text: str) -> list[str]:
    """[] iff exactly one line starts with CRITERION_HEAD and it contains CRITERION verbatim."""
    lines = [ln for ln in proposal_text.splitlines() if ln.startswith(CRITERION_HEAD)]
    if len(lines) != 1:
        return [f"{len(lines)} lines start with {CRITERION_HEAD!r} (expected 1)"]
    if CRITERION not in lines[0]:
        return ["the G-SHAPE-F0 line does not carry m:277's criterion verbatim"]
    return []


def sources_map() -> dict:
    """sha256 of every SCORING_STACK_FILES / TOOLING_FILES entry, working-tree bytes."""
    # PIN (Code, declared at LOCK v0.1; PIN-S10): package_sha256 covers valence_core/m/*.py only,
    # so the artifact also records each scoring-stack and tooling file's sha256 (the three
    # b3_screen files included, critic G-SHAPE item 4); LOCK v0.1 compares this map with its own
    # tree, and any difference re-runs G-SHAPE-F0 first.
    out: dict = {"sources": {}, "tooling": {}}
    for part, rels in (("sources", SCORING_STACK_FILES), ("tooling", TOOLING_FILES)):
        for rel in rels:
            try:
                out[part][rel] = _sha256((REPO / rel).read_bytes())
            except OSError:
                out[part][rel] = None
    return out


def sources_digest(m: Mapping[str, Any]) -> str:
    """sha256 of the sources map's json_text: the one line that pairs a self-test with a run."""
    return _json_sha256(dict(m))


def committed_sources() -> tuple[list[str], dict]:
    """(problems, map): problems == [] iff every SCORING_STACK_FILES and TOOLING_FILES entry is
    committed at HEAD and identical in the working tree (stages._committed, read at call time);
    the map is sources_map()'s shape over the sha256 of the bytes that check returned -- the
    checked committed blobs themselves, never a later working-tree read."""
    probs: list[str] = []
    out: dict = {"sources": {}, "tooling": {}}
    for part, rels in (("sources", SCORING_STACK_FILES), ("tooling", TOOLING_FILES)):
        for rel in rels:
            p, data = _stages._committed(rel)
            if p or data is None:
                probs += p or [f"{rel}: no bytes"]
                out[part][rel] = None
            else:
                out[part][rel] = _sha256(data)
    return probs, out


def sources_committed_problems() -> list[str]:
    """[] iff every SCORING_STACK_FILES and TOOLING_FILES entry is committed at HEAD and
    identical in the working tree."""
    return committed_sources()[0]


def package_files() -> list[str]:
    """valence_core/m/*.py, repo-relative and sorted: exactly the files package_sha256 covers."""
    return sorted(p.relative_to(REPO).as_posix() for p in PACKAGE_DIR.glob("*.py"))


def committed_package() -> tuple[list[str], dict]:
    """(problems, {rel: committed bytes}) over package_files(): problems == [] iff each is
    committed at HEAD and identical in the working tree (stages._committed, read at call time)."""
    # PIN (Code, declared at LOCK v0.1; Code's decisions item 11): the canonical run's committed
    # check covers EVERY file of the m package (valence_core/m/*.py, the files package_sha256
    # covers) beside SCORING_STACK_FILES and TOOLING_FILES, and the package_sha256 it records
    # must equal the hash of those committed blobs (package_sha256_of_blobs): the run of record
    # never records a package hash of an uncommitted tree. --out runs skip it (item 10).
    probs: list[str] = []
    blobs: dict = {}
    for rel in package_files():
        p, data = _stages._committed(rel)
        if p or data is None:
            probs += p or [f"{rel}: no bytes"]
        else:
            blobs[rel] = data
    return probs, blobs


def package_sha256_of_blobs(blobs: Mapping[str, bytes]) -> str:
    """resume.package_sha256_of's formula over (repo-relative path, bytes): '{rel}\\n{len}\\n'
    then the bytes, sorted by path -- the committed blobs hash comparably to the working tree."""
    h = hashlib.sha256()
    for rel, data in sorted(blobs.items()):
        h.update(f"{rel}\n{len(data)}\n".encode("utf-8"))
        h.update(data)
    return h.hexdigest()


# PIN (Code, declared at LOCK v0.1; re-verification round 1, F3): the run's import closure
# outside the m package -- the repo-relative __file__ of every loaded valence_core.* module
# whose file is not under valence_core/m, read from sys.modules at call time (after the
# imports; inputs_of_record takes it beside the committed check, provenance_drift again just
# before the write) -- is recorded in the artifact's provenance (import_closure: {rel:
# sha256}, its digest beside) and the canonical run refuses (exit 2) unless each of those
# files is committed at HEAD and identical in the working tree, as the scoring stack is. A
# module loaded after the precondition is drift (a refusal). The m package is covered by
# package_sha256 and its own committed check; a namespace package (no __file__) carries no
# code file. The map is sorted (json_text), so a re-run on unchanged inputs is byte-identical.
def import_closure() -> tuple[list[str], list[str]]:
    """(problems, rels): the sorted repo-relative __file__ of every loaded valence_core.* module
    outside valence_core/m; problems name a module whose file is not a regular file in the repo."""
    probs: list[str] = []
    rels: set[str] = set()
    pkg = PACKAGE_DIR.resolve()
    repo = REPO.resolve()
    for name, mod in sorted(list(sys.modules.items()), key=lambda kv: kv[0]):
        if not (name == "valence_core" or name.startswith("valence_core.")):
            continue
        f = getattr(mod, "__file__", None)
        if not f:
            continue
        p = Path(f).resolve()
        if pkg in p.parents:
            continue
        if repo not in p.parents or not p.is_file():
            probs.append(f"{name}: {f} is not a regular file in the repo (import closure)")
            continue
        rels.add(p.relative_to(repo).as_posix())
    return probs, sorted(rels)


def closure_map() -> tuple[list[str], dict]:
    """(problems, {rel: working-tree sha256}) over import_closure() (the --out runs' record)."""
    probs, rels = import_closure()
    out: dict = {}
    for rel in rels:
        try:
            out[rel] = _sha256((REPO / rel).read_bytes())
        except OSError:
            out[rel] = None
    return probs, out


def committed_closure() -> tuple[list[str], dict]:
    """(problems, {rel: committed sha256}) over import_closure(): problems == [] iff each file is
    committed at HEAD and identical in the working tree (stages._committed, read at call time);
    the map carries the sha256 of the bytes that check returned (the checked blobs)."""
    probs, rels = import_closure()
    out: dict = {}
    for rel in rels:
        p, data = _stages._committed(rel)
        if p or data is None:
            probs += p or [f"{rel}: no bytes"]
            out[rel] = None
        else:
            out[rel] = _sha256(data)
    return probs, out


def _dedup(xs: Sequence[str]) -> list[str]:
    return list(dict.fromkeys(xs))


def provenance_drift(ins: Mapping[str, Any]) -> list[str]:
    """The canonical run's re-check just before its write: [] iff the committed check (the
    sources, the tooling, every m package file and the import closure) still passes, its
    sources map, the package files' and the import closure's committed sha256 equal those
    recorded at the precondition (no module loaded since), and the m package re-hashes
    (uncached) to the package_sha256 recorded then."""
    # PIN (Code, declared at LOCK v0.1; review finding, harness-safety): the canonical run binds
    # its recorded provenance to the bytes that passed the committed check -- the sources map is
    # built from those committed blobs and package_sha256 is taken at the same precondition (and
    # must equal a fresh, uncached re-hash then, so the module code this process imported is the
    # tree's); just before the write the committed check, the map and a fresh package re-hash
    # run again, and any drift is a refusal (exit 2, nothing written, the verdict not recorded).
    sp, now = committed_sources()
    pp, pblobs = committed_package()
    cp_, cnow = committed_closure()
    probs = _dedup(sp + pp + cp_)
    rec_c = ins.get("import_closure")
    if rec_c is None:
        probs.append("the precondition recorded no import closure")
    else:
        for rel in sorted(set(rec_c) | set(cnow)):
            if rel not in cnow:
                probs.append(f"{rel}: left the import closure since the precondition")
            elif rel not in rec_c:
                probs.append(f"{rel}: entered the import closure since the precondition (a module loaded "
                             f"after the committed check)")
            elif rec_c[rel] != cnow[rel]:
                probs.append(f"{rel}: sha256 changed since the precondition")
    rec = ins["sources_map"]
    for part in ("sources", "tooling"):
        for rel in sorted(set(rec[part]) | set(now[part])):
            if rec[part].get(rel) != now[part].get(rel):
                probs.append(f"{rel}: sha256 changed since the precondition")
    rec_p = ins.get("package_committed")
    if rec_p is None:
        probs.append("the precondition recorded no committed m package")
    else:
        now_p = {rel: _sha256(b) for rel, b in pblobs.items()}
        for rel in sorted(set(rec_p) | set(now_p)):
            if rec_p.get(rel) != now_p.get(rel):
                probs.append(f"{rel}: sha256 changed since the precondition")
    fresh = _resume.package_sha256_of(PACKAGE_DIR)
    if fresh != ins["package_sha256"]:
        probs.append(f"package_sha256 re-hashes to {fresh[:16]}..., not the {ins['package_sha256'][:16]}... "
                     f"recorded at the precondition")
    return _dedup(probs)


# --- the two stacks (PIN-S4) ----------------------------------------------------------------
# PIN (Code, declared at LOCK v0.1; PIN-S4): "the full scoring stack of both substrates" (m:277)
# is each substrate's own stack as its startup builds it, without the adapter-dependent ban-id
# halves. Qwen: audit.qwen_audit_of_record + QwenTaskRoundAudit over the pool of record, its
# scaffold set asserted against the e2a ban-list file's ids and strings by assert_qwen_scaffold
# (not against a live tokenizer). OLMo: OLMoTaskRoundAudit(), its six strings asserted against
# each scaffold_{ckpt}.json. Both: the termination counter and the end rules (round_fires'
# termination, ends and strict fields). The OLMo ban-id sha16 2dd86a453a2275ef is generation-side
# and asserted by olmo_startup on the box; it is recorded, not exercised (olmo_stack's PIN). No
# cross-substrate placement: each unit's placements are scored by its own substrate's stack only,
# with its own substrate's echo set (grid and placements select both by _substrate(unit)).
def qwen_stack(pool: Sequence[Mapping[str, Any]]) -> tuple[_audit.QwenTaskRoundAudit, dict]:
    """The Qwen stack as qwen_startup builds it, minus the live-tokenizer half: v2 + audit v3
    of record (pinned shas), its scaffold set asserted against the e2a ban-list file."""
    audit3, cfg = _audit.qwen_audit_of_record()
    fil = json.loads(Path(_audit.E2A_BAN_LIST_PATH).read_bytes())
    sca = _audit.assert_qwen_scaffold(fil["ids"], fil["strings"], audit3)
    stack = _audit.QwenTaskRoundAudit(audit3, pool, fil["strings"])
    rec = {"claim_order": list(_audit.QWEN_CLAIMS), "audit_v2_sha16": cfg["sha16_recomputed"],
           "e2a_ban_list_sha256": cfg["ban_list_sha256"], "audit_version": AUDIT_VERSION,
           "n_scaffold_strings": len(stack.scaffold_strings), "scaffold_assertion": sca,
           "term_sha16": _sc.TERM_SHA16, "end_rule": "qwen_ends (lenient scope); strict_excludes beside",
           "echo_set": "the banner's Note lines + 'Reasoning (one line):' (audit.qwen_echo_lines)",
           "content_others": "the other 15 items' clean text (audit.corr_others)"}
    return stack, rec


def olmo_scaffold_string_problems(strings_by_ckpt: Mapping[str, Sequence[str]]) -> list[str]:
    """Each checkpoint's scaffold_{ckpt}.json ban strings must be OLMo's six (m:262)."""
    probs = []
    if tuple(sorted(strings_by_ckpt)) != tuple(sorted(keys.CKPTS)):
        probs.append(f"checkpoints {sorted(strings_by_ckpt)} are not {sorted(keys.CKPTS)}")
    for ck, ss in sorted(strings_by_ckpt.items()):
        if sorted(ss) != sorted(_audit.OLMO_SCAFFOLD_STRINGS) or len(set(ss)) != len(ss):
            probs.append(f"scaffold_{ck}.json ban strings are not OLMo's six")
    return probs


def _olmo_files() -> tuple[dict, dict]:
    """Each checkpoint's own scaffold_{ckpt}.json ban strings and b3_screen_{ckpt}.json ban_list
    (OLMO_DIR read at call time; the self-test points it at a planted copy)."""
    d = Path(OLMO_DIR)
    strings, b3 = {}, {}
    for ck in keys.CKPTS:
        strings[ck] = list(json.loads((d / f"scaffold_{ck}.json").read_bytes())["ban_strings"])
        b3[ck] = dict(json.loads((d / f"b3_screen_{ck}.json").read_bytes())["ban_list"])
    return strings, b3


def olmo_stack() -> tuple[_audit.OLMoTaskRoundAudit, dict]:
    """OLMo's stack as olmo_startup builds it, minus the box-side ban-id half: b3's AuditSpec,
    echo, lexical; its six strings asserted against every checkpoint's scaffold file."""
    # PIN (Code, declared at LOCK v0.1; PIN-S4, critic G-SHAPE item 3): the OLMo stack takes no
    # checkpoint (OLMoTaskRoundAudit(), olmo_roster, build_banner), so the three OLMo units are
    # one computation run three times on byte-identical inputs; the only per-checkpoint input
    # is the scaffold_{ckpt}.json string check. The ban-id half (sha16 2dd86a453a2275ef, 9 ids)
    # needs the OLMo tokenizer and is generation-side: olmo_startup asserts it on the box
    # (LOCK-m-OLMo-{ckpt} v0.1, m:302). Recorded here from b3_screen_{ckpt}.json, not exercised.
    strings, b3 = _olmo_files()
    sp = olmo_scaffold_string_problems(strings)
    if sp:
        raise GshapeStop(f"G-SHAPE-F0 STOP: OLMo scaffold strings: {sp}")
    bad = sorted(ck for ck, v in b3.items() if v != B3_BAN_LIST)
    if bad:
        raise GshapeStop(f"G-SHAPE-F0 STOP: b3_screen ban_list of {bad} is not {B3_BAN_LIST}")
    stack = _audit.OLMoTaskRoundAudit()
    rec = {"claim_order": list(_audit.OLMO_CLAIMS), "audit_sha16": _ro.olmo_audit_sha16(),
           "scaffold_strings": list(_audit.OLMO_SCAFFOLD_STRINGS),
           "scaffold_strings_checked": {f"scaffold_{ck}.json": "equal" for ck in keys.CKPTS},
           "term_sha16": _sc.TERM_SHA16, "end_rule": "olmo_ends (the first claim in any round)",
           "echo_set": "the banner's Note lines (audit.olmo_echo_lines)",
           "ban_ids": {ck: b3[ck] for ck in keys.CKPTS},
           "ban_ids_note": ("generation-side (m:262 'asserted at startup'); olmo_startup asserts it on "
                            "the box before any OLMo session (LOCK-m-OLMo-{ckpt} v0.1, m:302); not "
                            "exercised by G-SHAPE-F0")}
    return stack, rec


# --- inputs of record (§4 of the build spec) -----------------------------------------------
def _seat_renders_sha(text: str) -> str | None:
    hits = re.findall(r"^renders_sha256: `([0-9a-f]{64})`$", text, flags=re.M)
    return hits[0] if len(hits) == 1 else None


def inputs_of_record(*, canonical: bool, proposal_rel: str = _stages.PROPOSAL_REL) -> dict:
    """Every precondition, in order; GshapeRefusal (exit 2) or GshapeStop (exit 4) on the first
    failure, nothing scored or written before."""
    # PIN (Code, declared at LOCK v0.1; PIN-S7): the renders placed are G-CAL's RECORD -- read from
    # the committed model-free artifact's renders_of_record.items[i].render -- asserted equal to
    # scaffold.pool_and_renders(), to the pinned renders sha256, to the completability identity's
    # and to the seat read's cited line; they are never computed as G-SHAPE's own
    # (RESULTS.md@e60b633:919-920). The proposal is the committed blob and must equal G-CAL's
    # provenance proposal sha256.
    kp = keys.stream_known_answer()
    if kp:
        raise GshapeStop(f"G-SHAPE-F0 STOP: {kp} -- every render, key and roster rests on numpy's stream")
    pdata = _read_committed(proposal_rel)
    proposal_sha = _sha256(pdata)
    cp = criterion_problems(pdata.decode("utf-8", "replace"))
    if cp:
        raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: {proposal_rel} is not the governing proposal: {cp}")
    # PIN (Code, declared at LOCK v0.1; critic G-SHAPE item 4; Code's decisions items 10-11;
    # re-verification round 1, F3): the canonical run refuses unless every SCORING_STACK_FILES
    # and TOOLING_FILES entry, every m package file (valence_core/m/*.py) AND every file of the
    # import closure (import_closure: each loaded valence_core.* module outside valence_core/m)
    # is committed at HEAD and identical in the working tree, so the artifact's sources map and
    # import closure name committed blobs only and its package_sha256 is the hash of the
    # committed package (asserted equal). A --out test run (refused under data/m) does not
    # check it, so the build's self-test can run before the build commit; its artifact is never
    # of record, and the driver prints which case applied.
    pkg = _resume.package_sha256()
    if canonical:
        sp, smap = committed_sources()
        pp, pblobs = committed_package()
        clp, cmap = committed_closure()
        cp_all = _dedup(sp + pp + clp)
        if cp_all:
            raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: the scoring stack, the tooling, every m package file and "
                                f"the import closure must be committed at HEAD and unedited for the run of "
                                f"record: {cp_all[:4]}"
                                + (f" (+{len(cp_all) - 4} more)" if len(cp_all) > 4 else ""))
        fresh = _resume.package_sha256_of(PACKAGE_DIR)
        if fresh != pkg:
            raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: the m package re-hashes to {fresh[:16]}..., not the "
                                f"{pkg[:16]}... this process first hashed (a file changed since import)")
        cpk = package_sha256_of_blobs(pblobs)
        if cpk != pkg:
            raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: the m package's committed blobs hash to {cpk[:16]}..., "
                                f"not the package_sha256 {pkg[:16]}... this run would record (an uncommitted "
                                f"package is never recorded)")
        pcommitted = {rel: _sha256(b) for rel, b in pblobs.items()}
    else:
        smap = sources_map()
        pcommitted = None
        cmap = closure_map()[1]
    bp = _banner.spec_problems(REPO / proposal_rel)
    if bp:
        raise GshapeStop(f"G-SHAPE-F0 STOP: the banners placed are not §2.5's bytes: {bp}")
    # G-CAL's model-free artifact
    mf, mf_sha = _committed_json(MODEL_FREE_REL)
    if not isinstance(mf, dict) or mf.get("schema") != _gcal.MODEL_FREE_SCHEMA:
        raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: {MODEL_FREE_REL} is not {_gcal.MODEL_FREE_SCHEMA}")
    if (mf.get("provenance") or {}).get("proposal_sha256") != proposal_sha:
        raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: G-CAL's provenance proposal_sha256 is not "
                            f"{proposal_rel}'s committed blob ({proposal_sha[:16]}...)")
    ror = mf.get("renders_of_record") or {}
    if ror.get("renders_sha256") != RENDERS_SHA256_OF_RECORD:
        raise GshapeStop(f"G-SHAPE-F0 STOP: G-CAL's renders_sha256 {str(ror.get('renders_sha256'))[:16]}... "
                         f"is not the renders of record {RENDERS_SHA256_OF_RECORD[:16]}...")
    conds = mf.get("conditions") or {}
    bad_c = [c for c in ("1", "2") if (conds.get(c) or {}).get("verdict") != "PASS"]
    if bad_c:
        raise GshapeStop(f"G-SHAPE-F0 STOP: G-CAL conditions {bad_c} are not PASS in {MODEL_FREE_REL}")
    # G-CAL's completability artifact
    # PIN (Code, declared at LOCK v0.1; Code's decisions item 2 over spec §4.6-4.7): an absent,
    # uncommitted, other-schema or non-PASS completability artifact, and a seat read with no single
    # 'renders_sha256: `...`' line, are refusals (the input of record is not there); a renders
    # sha256 there that is not the pin is a STOP ("STOP on any mismatch" of the renders).
    comp, comp_sha = _committed_json(COMPLETABILITY_REL)
    if not isinstance(comp, dict) or comp.get("schema") != _gcal.ART_SCHEMA or comp.get("verdict") != "PASS":
        raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: {COMPLETABILITY_REL} is not a {_gcal.ART_SCHEMA} PASS")
    if (comp.get("identity") or {}).get("renders_sha256") != RENDERS_SHA256_OF_RECORD:
        raise GshapeStop(f"G-SHAPE-F0 STOP: {COMPLETABILITY_REL}'s identity renders_sha256 is not the "
                         f"renders of record")
    # the seat's read of record
    seat = _read_committed(SEAT_READ_REL)
    seat_cited = _seat_renders_sha(seat.decode("utf-8", "replace"))
    if seat_cited is None:
        raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: {SEAT_READ_REL} carries no single 'renders_sha256: `...`' "
                            f"line")
    if seat_cited != RENDERS_SHA256_OF_RECORD:
        raise GshapeStop(f"G-SHAPE-F0 STOP: {SEAT_READ_REL} cites renders_sha256 {seat_cited[:16]}..., not "
                         f"the renders of record")
    # the renders of record, from G-CAL's record
    items = ror.get("items")
    if (not isinstance(items, list) or len(items) != N_ITEMS
            or [x.get("i") if isinstance(x, dict) else None for x in items] != list(range(N_ITEMS))
            or not all(isinstance(x.get("render"), str) for x in items)):
        raise GshapeStop(f"G-SHAPE-F0 STOP: {MODEL_FREE_REL} renders_of_record.items is not 16 items "
                         f"in order")
    renders = [x["render"] for x in items]
    pool, computed = _sc.pool_and_renders()
    if renders != computed:
        raise GshapeStop("G-SHAPE-F0 STOP: G-CAL's recorded renders are not scaffold.pool_and_renders()'s")
    if _sha256_text("\n".join(renders)) != RENDERS_SHA256_OF_RECORD:
        raise GshapeStop("G-SHAPE-F0 STOP: the recorded renders do not hash to the renders of record")
    if _resume.pool_sha16(pool) != (mf.get("provenance") or {}).get("pool_sha16"):
        raise GshapeStop("G-SHAPE-F0 STOP: the served pool's sha16 is not G-CAL's provenance pool_sha16")
    # PIN (Code, declared at LOCK v0.1; re-verification round 1, V16): the pools file is hashed
    # here, from its bytes, and must equal the pools_file_sha256 G-CAL recorded; the artifact
    # records both (inputs.pools_file_sha256, inputs.pools_file_sha256_gcal_provenance). A
    # difference is a pinned figure that does not reproduce: a precondition STOP.
    pools_sha = _sha256(_corr.POOLS_PATH.read_bytes())
    pools_gcal = (mf.get("provenance") or {}).get("pools_file_sha256")
    if pools_sha != pools_gcal:
        raise GshapeStop(f"G-SHAPE-F0 STOP: the pools file hashes to {pools_sha[:16]}..., not G-CAL's recorded "
                         f"pools_file_sha256 {str(pools_gcal)[:16]}...")
    clean = [it["task"] for it in pool]
    golds = [it.get("gold") for it in pool]
    flat = [g for gl in golds if isinstance(gl, list) for g in gl]
    if (len(set(renders) | set(clean)) != 2 * N_ITEMS or any("\n" in t for t in renders)
            or not all(isinstance(gl, list) and gl and all(isinstance(g, str) and g for g in gl)
                       for gl in golds)
            or len(flat) != N_GOLD_VARIANTS or len(set(flat)) != N_GOLD_VARIANTS):
        raise GshapeStop("G-SHAPE-F0 STOP: renders and clean tasks are not 32 distinct single lines, or "
                         f"the golds are not 16 items with {N_GOLD_VARIANTS} distinct variants")
    try:
        qs, qrec = qwen_stack(pool)
        ostack, orec = olmo_stack()
        term_rx = _sc.load_term_rx()
    except (GshapeRefusal, GshapeStop):
        raise
    except (SystemExit, ValueError, TypeError, KeyError, OSError) as e:
        raise GshapeStop(f"G-SHAPE-F0 STOP: a stack of record did not build: {type(e).__name__}: {e}") \
            from None
    return {"proposal_rel": proposal_rel, "proposal_sha256": proposal_sha,
            "model_free_sha256": mf_sha, "completability_sha256": comp_sha,
            "completability_verdict": comp["verdict"], "seat_sha256": _sha256(seat),
            "seat_renders_sha256": seat_cited, "renders": renders, "pool": pool,
            "pools_file_sha256": pools_sha, "pools_file_sha256_gcal": pools_gcal,
            "qwen_stack": qs, "qwen_rec": qrec, "olmo_stack": ostack, "olmo_rec": orec,
            "term_rx": term_rx, "canonical": canonical, "sources_map": smap, "package_sha256": pkg,
            "package_committed": pcommitted, "import_closure": cmap}


# --- the fire predicate (PIN-S3) -------------------------------------------------------------
# PIN (Code, declared at LOCK v0.1; PIN-S3): "no class fires" (m:277) is read strictly -- any
# field of ROUND_FIRE_FIELDS is a fire: a claim; a v5 advisory; audit v3's exclusion, content
# label or advisory; a raw echo or lexical hit beside (or pre-empted by) a claim;
# scaffold_absorption; round_degeneracy's numerator; the substrate's end rule; the strict scope;
# the termination counter. A placement fires iff round_fires(...) != []; any fire is a STOP.
def _f_claim(ra, text, rx) -> bool:
    return ra.claim is not None


def _f_advisory(ra, text, rx) -> bool:
    return bool(ra.advisory)


def _f_v3_exclusion(ra, text, rx) -> bool:
    return ra.v3 is not None and ra.v3.get("exclusion") is not None


def _f_v3_content_label(ra, text, rx) -> bool:
    return ra.v3 is not None and ra.v3.get("content_label") is not None


def _f_v3_advisory(ra, text, rx) -> bool:
    return ra.v3 is not None and bool(ra.v3.get("advisory"))


def _f_echo(ra, text, rx) -> bool:
    return ra.echo_line is not None


def _f_lexical(ra, text, rx) -> bool:
    return ra.lexical_raw is not None


def _f_scaffold(ra, text, rx) -> bool:
    return bool(ra.scaffold)


def _f_degeneracy(ra, text, rx) -> bool:
    return bool(ra.degeneracy)


def _f_ends(ra, text, rx) -> bool:
    return _audit.ends_session(ra)


def _f_strict(ra, text, rx) -> bool:
    return _audit.strict_excludes(ra)


def _f_termination(ra, text, rx) -> bool:
    return _sc.termination(text, rx)


FIRE_TESTS: tuple[tuple[str, Callable[..., bool]], ...] = (
    ("claim", _f_claim), ("advisory", _f_advisory), ("v3.exclusion", _f_v3_exclusion),
    ("v3.content_label", _f_v3_content_label), ("v3.advisory", _f_v3_advisory),
    ("echo_line", _f_echo), ("lexical_raw", _f_lexical), ("scaffold", _f_scaffold),
    ("degeneracy", _f_degeneracy), ("ends", _f_ends), ("strict", _f_strict),
    ("termination", _f_termination))


def round_fires(ra: _audit.RoundAudit, text: str, term_rx: Sequence[str], *,
                tests: Sequence[tuple[str, Callable[..., bool]]] | None = None) -> list[str]:
    """The fields of ROUND_FIRE_FIELDS that fire on one scored text, in declared order."""
    return [name for name, fn in (FIRE_TESTS if tests is None else tests) if fn(ra, text, term_rx)]


# --- Layer A: the enumeration (PIN-S1, PIN-S2) -----------------------------------------------
@dataclass(frozen=True)
class Placement:
    unit: str
    substrate: str
    template: str            # the unit's contrast template (A0 / A0-OLMo-{ckpt})
    pi: int
    mp: int
    cl: int
    t: int                   # ROUND_TEMPLATES index
    n: int
    i: int                   # item
    gi: int                  # gold variant index
    gold: str
    phase: str
    P: str
    Q: str
    banner: str
    echo_lines: tuple
    seg: str
    render: str

    @property
    def header(self) -> str:
        return self.seg.split("\n", 1)[0]

    def key(self) -> list:
        return [self.unit, self.pi, self.mp, self.cl, self.t, self.n, self.i, self.gold, self.phase]


def round_n(t: int, phase: str) -> int:
    # PIN (Code, declared at LOCK v0.1; PIN-S1): n is t + 1 at forced and t + 2F + 1 = t + 5 at
    # free (the forced round and the chosen round sharing t's template); n never enters
    # classify, and template_shape_problems covers every n in 1..10.
    return t + 1 + (_sc.N_FORCED if phase == "free" else 0)


def placements(unit: str, renders: Sequence[str], pool: Sequence[Mapping[str, Any]], *,
               templates: Sequence[str] | None = None) -> Iterator[Placement]:
    """m:277's placements for one unit, in enumeration order (pair, map, clause; template;
    item; gold variant; phase)."""
    # PIN (Code, declared at LOCK v0.1; PIN-S1): per unit, the 16 renders of record x
    # ROUND_TEMPLATES[0..3] (m:159's "round templates"; F0m-OLMo's are the same objects: b3 and
    # scaffold._round format them) x the unit's 16 contrast banners (4 pairs x 2 maps x 2 clauses)
    # x every stored gold variant (22) x both phases, the render under the Q-role label: 2,816 per
    # unit, 11,264 in all. Menus (no Task line) and sham banners (no render, m:172) are not
    # placements.
    # PIN (Code, declared at LOCK v0.1; PIN-S2): "a clean gold" is each gold string verbatim as
    # stored in CORR_clean -- unframed, no case, punctuation or sentence added (ledger 33).
    tpls = ROUND_TEMPLATES if templates is None else tuple(templates)
    sub = _substrate(unit)
    tA = keys.templates(unit)[0]
    roster = _schedule.roster_for(unit)
    for pi in range(len(roster)):
        for mp in (0, 1):
            for cl in (0, 1):
                P, Q = roster[pi][mp], roster[pi][1 - mp]
                bnr, notes = _banner.build_banner(tA, P, Q, cl)
                el = _audit.qwen_echo_lines(notes) if sub == "qwen" else _audit.olmo_echo_lines(notes)
                for t, tpl in enumerate(tpls):
                    for i, render in enumerate(renders):
                        for gi, g in enumerate(pool[i]["gold"]):
                            for phase in PHASES:
                                n = round_n(t, phase)
                                yield Placement(unit=unit, substrate=sub, template=tA, pi=pi, mp=mp,
                                                cl=cl, t=t, n=n, i=i, gi=gi, gold=g, phase=phase,
                                                P=P, Q=Q, banner=bnr, echo_lines=tuple(el),
                                                seg=tpl.format(n=n, tag=Q, task=render), render=render)


def expected_keys(pool: Sequence[Mapping[str, Any]]) -> Counter:
    """The exact product a unit's placements must cover (unit stripped), built from the
    constants alone, independently of ``placements``."""
    return Counter((pi, mp, cl, t, round_n(t, ph), i, g, ph)
                   for pi in range(4) for mp in (0, 1) for cl in (0, 1) for t in range(N_TEMPLATES)
                   for i in range(N_ITEMS) for g in pool[i]["gold"] for ph in PHASES)


def score(stack, pl: Placement, text: str) -> _audit.RoundAudit:
    """``text`` scored exactly as the unit's runner calls its stack (runner_qwen.py:161/:192,
    runner_olmo.py:139/:166), with ``earlier`` empty."""
    if pl.substrate == "qwen":
        return stack.classify(text, render=pl.render, item=pl.i, earlier=(), own_pair=(pl.P, pl.Q),
                              echo_lines=pl.echo_lines, phase=pl.phase)
    return stack.classify(text, own_pair=(pl.P, pl.Q), echo_lines=pl.echo_lines, phase=pl.phase)


def _gold(pl: Placement) -> str:
    return pl.gold


def _seg_gold(pl: Placement) -> str:
    return pl.seg + pl.gold


def _render_alone(pl: Placement) -> str:
    return pl.render


# PIN (Code, declared at LOCK v0.1; PIN-S6, trimmed per Code's decisions): Layer C is ONE
# scope-widened control per placement -- seg+gold, the segment's harness bytes and the gold
# scored as one response -- which must fire on 100% of placements per unit (instrument
# validity, not an m:277 criterion; a silent control is a STOP). render-as-response (the
# render scored as the response) is reported only: Qwen's v5 task_echo sees it on items whose
# render stays close to the task; OLMo's stack takes no render input, which is why Layer S,
# not Layer A, is what covers a runner that scored the render.
CONTROL_TEXTS: dict[str, Callable[[Placement], str]] = {"seg+gold": _seg_gold,
                                                        "render-as-response": _render_alone}


def grid(ins: Mapping[str, Any], units: Sequence[str] = UNITS, *,
         scorer: Callable[[Placement], str] | None = None,
         controls: Mapping[str, Callable[[Placement], str]] | None = None,
         templates: Sequence[str] | None = None,
         drop: Callable[[Placement], bool] | None = None) -> dict:
    """Layers A and C over ``units``: per unit the grid record and the controls record."""
    scorer = _gold if scorer is None else scorer
    ctl = dict(CONTROL_TEXTS if controls is None else controls)
    if tuple(sorted(ctl)) != tuple(sorted(CONTROLS_REQUIRED + CONTROLS_REPORTED)):
        raise ValueError(f"controls must be exactly {CONTROLS_REQUIRED + CONTROLS_REPORTED}")
    term_rx = ins["term_rx"]
    out: dict = {}
    for unit in units:
        stack = ins["qwen_stack"] if _substrate(unit) == "qwen" else ins["olmo_stack"]
        ukeys, rows, fires = [], [], []
        n_fired = n_misplaced = 0
        cstat = {c: {"n": 0, "n_fired": 0, "items": set(), "fields": set(), "advisories": set()}
                 for c in ctl}
        for pl in placements(unit, ins["renders"], ins["pool"], templates=templates):
            if drop is not None and drop(pl):
                continue
            # PIN (Code, declared at LOCK v0.1): every placement is checked as placed -- its segment
            # is [a bracketed header naming round n and ending ': {Q}]', 'Task: ' + the i-th render
            # of record, 'Response:'] and its gold the stored variant -- so the shape check binds
            # the placements scored, not only a parallel enumeration; a misplacement is a 'shape' STOP.
            sl = pl.seg.split("\n")
            if (len(sl) != 3 or sl[1] != "Task: " + ins["renders"][pl.i] or sl[2] != "Response:"
                    or not sl[0].startswith(f"[round {pl.n} ") or not sl[0].endswith(f": {pl.Q}]")
                    or pl.render != ins["renders"][pl.i] or pl.gold != ins["pool"][pl.i]["gold"][pl.gi]):
                n_misplaced += 1
            text = scorer(pl)
            ra = score(stack, pl, text)
            f = round_fires(ra, text, term_rx)
            cf = {}
            for c, fn in ctl.items():
                ct = fn(pl)
                cra = score(stack, pl, ct)
                cf[c] = round_fires(cra, ct, term_rx)
                st = cstat[c]
                st["n"] += 1
                if cf[c]:
                    st["n_fired"] += 1
                    st["items"].add(pl.i)
                    st["fields"].update(cf[c])
                    st["advisories"].update(cra.advisory)
            k = pl.key()
            ukeys.append(k)
            # PIN (Code, declared at LOCK v0.1): a row is the placement key without its unit,
            # the scored text, its fire fields, its RoundAudit and each control's fire fields;
            # rows_sha256 = sha256 of json_text(rows) in enumeration order. OLMo's three
            # checkpoints must give one rows_sha256 (olmo_grids_identical).
            rows.append(k[1:] + [text, f, ra.as_dict(), {c: cf[c] for c in sorted(cf)}])
            if f:
                n_fired += 1
                if len(fires) < FIRES_LISTED_MAX:
                    fires.append({"key": k, "fields": f, "detail": ra.detail})
        seen = Counter(tuple(k[1:]) for k in ukeys)
        cov = {"renders": len({k[6] for k in ukeys}), "templates": len({k[4] for k in ukeys}),
               "phases": len({k[8] for k in ukeys}), "banners": len({tuple(k[1:4]) for k in ukeys}),
               "gold_variants": len({(k[6], k[7]) for k in ukeys}),
               "exact": seen == expected_keys(ins["pool"])}
        out[unit] = {
            "grid": {"template": keys.templates(unit)[0], "substrate": _substrate(unit), "n": len(ukeys),
                     "n_fired": n_fired, "fires": fires, "fires_listed": len(fires), "n_misplaced": n_misplaced,
                     "placements_sha256": _json_sha256(ukeys), "rows_sha256": _json_sha256(rows),
                     "coverage": cov},
            "controls": {c: {"n": cstat[c]["n"], "n_fired": cstat[c]["n_fired"],
                             "required": c in CONTROLS_REQUIRED,
                             "fired_items": sorted(cstat[c]["items"]),
                             "fired_fields": [x for x in ROUND_FIRE_FIELDS if x in cstat[c]["fields"]],
                             "advisories": sorted(cstat[c]["advisories"])} for c in sorted(ctl)}}
    return out


# --- template shape ------------------------------------------------------------------------
def shape_labels() -> list[str]:
    """Every label a Q role takes on any built unit (both maps make every roster word one)."""
    return sorted({roster[pi][1 - mp] for u in UNITS for roster in [_schedule.roster_for(u)]
                   for pi in range(len(roster)) for mp in (0, 1)})


def template_shape_problems(templates: Sequence[str] = ROUND_TEMPLATES,
                            renders: Sequence[str] | None = None,
                            labels: Sequence[str] | None = None) -> list[str]:
    """Each template, at every n in 1..10, every render and every Q label, is exactly
    [bracketed header naming round n and ending ': {label}]', 'Task: ' + render, 'Response:']."""
    renders = _sc.pool_and_renders()[1] if renders is None else list(renders)
    labels = shape_labels() if labels is None else list(labels)
    probs: list[str] = []
    for ti, tpl in enumerate(templates):
        for n in range(1, N_ROUNDS + 1):
            for ri, r in enumerate(renders):
                if "\n" in r:
                    probs.append(f"render {ri} carries a newline")
                    continue
                for lab in labels:
                    try:
                        seg = tpl.format(n=n, tag=lab, task=r)
                    except (KeyError, IndexError, ValueError) as e:
                        probs.append(f"template {ti}: format raised {type(e).__name__}")
                        continue
                    lines = seg.split("\n")
                    if len(lines) != 3 or lines[1] != "Task: " + r or lines[2] != "Response:":
                        probs.append(f"template {ti} n={n} render {ri}: not header / Task line / Response:")
                        continue
                    h = lines[0]
                    if not (h.startswith(f"[round {n} ") and h.endswith(f": {lab}]")):
                        probs.append(f"template {ti} n={n}: header is not a bracketed round header "
                                     f"ending in the label")
    return sorted(set(probs))


# --- Layer S: static runner scope (PIN-S5) -------------------------------------------------
@lru_cache(maxsize=128)
def _parse(rel: str, text: str):
    """ast.parse, cached by (path, text): the trees are only read, never mutated."""
    return ast.parse(text, filename=rel)


def _package_sources() -> dict[str, str]:
    return {f"valence_core/m/{p.name}": p.read_text(encoding="utf-8")
            for p in sorted(PACKAGE_DIR.glob("*.py"))}


def _is_name(n, ident: str | None = None) -> bool:
    return isinstance(n, ast.Name) and (ident is None or n.id == ident)


def _is_attr(n, base: str, attr: str) -> bool:
    return isinstance(n, ast.Attribute) and n.attr == attr and _is_name(n.value, base)


def _stmt_lists(node) -> Iterator[list]:
    for n in ast.walk(node):
        for fld in ("body", "orelse", "finalbody"):
            b = getattr(n, fld, None)
            if isinstance(b, list) and b and all(isinstance(s, ast.stmt) for s in b):
                yield b


def _target_names(t) -> list[str]:
    return [n.id for n in ast.walk(t) if isinstance(n, ast.Name)]


def _own_bindings(stmt, name: str) -> bool:
    """Whether ``stmt`` ITSELF binds ``name`` (nested statements are visited on their own)."""
    if isinstance(stmt, ast.Assign):
        return any(name in _target_names(t) for t in stmt.targets)
    if isinstance(stmt, (ast.AnnAssign, ast.AugAssign)):
        return name in _target_names(stmt.target)
    if isinstance(stmt, (ast.For, ast.AsyncFor)):
        return name in _target_names(stmt.target)
    if isinstance(stmt, (ast.With, ast.AsyncWith)):
        return any(it.optional_vars is not None and name in _target_names(it.optional_vars)
                   for it in stmt.items)
    if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return stmt.name == name
    if isinstance(stmt, (ast.Import, ast.ImportFrom)):
        return any((a.asname or a.name.split(".")[0]) == name for a in stmt.names)
    if isinstance(stmt, ast.Delete):
        return any(name in _target_names(t) for t in stmt.targets)
    if isinstance(stmt, ast.Try):
        return any(h.name == name for h in stmt.handlers)
    return False


def _binds(stmt, name: str) -> bool:
    """Whether ``stmt`` or anything nested in it binds ``name`` (walrus included)."""
    for n in ast.walk(stmt):
        if isinstance(n, ast.stmt) and _own_bindings(n, name):
            return True
        if isinstance(n, ast.NamedExpr) and _is_name(n.target, name):
            return True
    return False


def _bindings(fn, name: str) -> list:
    return [s for s in ast.walk(fn) if isinstance(s, ast.stmt) and s is not fn and _own_bindings(s, name)]


def _single_value(fn, name: str):
    """The value of the one plain assignment binding ``name`` in ``fn``, else None."""
    bs = _bindings(fn, name)
    if len(bs) != 1:
        return None
    s = bs[0]
    if isinstance(s, ast.Assign) and len(s.targets) == 1 and _is_name(s.targets[0], name):
        return s.value
    if isinstance(s, ast.AnnAssign) and _is_name(s.target, name) and s.value is not None:
        return s.value
    return None


def _runner_problems(rel: str, tree, fname: str, sub: str) -> tuple[list[str], set]:
    """R1-R6 on one runner; (problems, the generation names whose .text classify scored)."""
    probs: list[str] = []
    fns = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == fname]
    if len(fns) != 1:
        return [f"R1 {rel}: {len(fns)} top-level definitions of {fname} (expected 1)"], set()
    fn = fns[0]
    params = [a.arg for a in fn.args.posonlyargs + fn.args.args]
    if params[:4] != ["adapter", "scaffold", "audit", "ban_ids"] or "term_rx" not in [
            a.arg for a in fn.args.kwonlyargs]:
        probs.append(f"R1 {rel}:{fn.lineno}: {fname}'s signature is not (adapter, scaffold, audit, "
                     f"ban_ids, *, ..., term_rx)")
    for p in ("adapter", "audit", "term_rx"):
        if _bindings(fn, p):
            probs.append(f"R1 {rel}: the parameter {p!r} is rebound inside {fname}")
    scs = [s.targets[0].id for s in fn.body if isinstance(s, ast.Assign) and len(s.targets) == 1
           and _is_name(s.targets[0]) and _is_name(s.value, "scaffold")]
    sc = scs[0] if len(scs) == 1 and len(_bindings(fn, scs[0])) == 1 else None
    if sc is None:
        probs.append(f"R5 {rel}: {fname} does not bind the scaffold parameter to one name once")
        sc = "sc"
    # R5: own and echo_lines; R6: log
    v = _single_value(fn, "own")
    if not (isinstance(v, ast.Tuple) and len(v.elts) == 2 and _is_attr(v.elts[0], sc, "P")
            and _is_attr(v.elts[1], sc, "Q")):
        probs.append(f"R5 {rel}: own is not bound once as ({sc}.P, {sc}.Q)")
    v = _single_value(fn, "echo_lines")
    if not (isinstance(v, ast.Call) and _is_attr(v.func, "_audit", f"{sub}_echo_lines")
            and len(v.args) == 1 and _is_attr(v.args[0], sc, "note_lines") and not v.keywords):
        probs.append(f"R5 {rel}: echo_lines is not bound once as _audit.{sub}_echo_lines({sc}.note_lines)")
    v = _single_value(fn, "log")
    log_ok = (isinstance(v, ast.Call) and _is_attr(v.func, "_sc", "SessionLog") and len(v.args) == 2
              and _is_name(v.args[0], sc) and isinstance(v.args[1], ast.Constant) and v.args[1].value == sub)
    if not log_ok:
        probs.append(f"R6 {rel}: log is not bound once as _sc.SessionLog({sc}, {sub!r})")
    # R1: exactly two classify references, both calls on the audit parameter
    attrs = [n for n in ast.walk(fn) if isinstance(n, ast.Attribute) and n.attr == "classify"]
    calls = [n for n in ast.walk(fn) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
             and n.func.attr == "classify"]
    if len(attrs) != 2 or len(calls) != 2 or not all(_is_name(c.func.value, "audit") for c in calls):
        probs.append(f"R1 {rel}: {fname} carries {len(attrs)} classify reference(s) / {len(calls)} call(s); "
                     f"expected exactly two calls audit.classify(...)")
    where = {}
    for L in _stmt_lists(fn):
        for k, st in enumerate(L):
            if isinstance(st, ast.Assign) and isinstance(st.value, ast.Call) and st.value in calls:
                where[id(st.value)] = (L, k, st)
    phases, gnames, sites = [], set(), []
    for c in calls:
        if id(c) not in where:
            probs.append(f"R2 {rel}:{c.lineno}: the classify result is not bound by a plain assignment")
            continue
        L, k, st = where[id(c)]
        ra = st.targets[0].id if len(st.targets) == 1 and _is_name(st.targets[0]) else None
        if ra is None:
            probs.append(f"R2 {rel}:{c.lineno}: the classify result is not bound to one name")
            continue
        # R2: the only positional argument is <G>.text, G the nearest generate in this block
        if (len(c.args) != 1 or not isinstance(c.args[0], ast.Attribute) or c.args[0].attr != "text"
                or not _is_name(c.args[0].value)):
            probs.append(f"R2 {rel}:{c.lineno}: the scored text is not <generation>.text alone")
            continue
        G = c.args[0].value.id
        gi = next((j for j in range(k - 1, -1, -1) if _binds(L[j], G)), None)
        gen = L[gi] if gi is not None else None
        gv = gen.value if isinstance(gen, ast.Assign) else None
        if not (isinstance(gen, ast.Assign) and len(gen.targets) == 1 and _is_name(gen.targets[0], G)
                and isinstance(gv, ast.Call) and _is_attr(gv.func, "adapter", "generate")
                and len(gv.args) >= 2 and isinstance(gv.args[1], ast.Attribute) and gv.args[1].attr == "seg"
                and _is_name(gv.args[1].value)
                and any(kw.arg == "injections" and isinstance(kw.value, ast.Tuple) and not kw.value.elts
                        for kw in gv.keywords)):
            probs.append(f"R2 {rel}:{c.lineno}: {G} is not bound, in the same block, by "
                         f"{G} = adapter.generate(<prefix>, <spec>.seg, injections=(), ...)")
            continue
        S = gv.args[1].value.id
        # G cannot be rebound in between: L[gi] is the nearest statement binding it; S can
        if any(_binds(s, S) for s in L[gi + 1:k]):
            probs.append(f"R2 {rel}:{c.lineno}: {S} is rebound between generate and classify")
        gnames.add(G)
        sites.append((L, k, G, c.lineno))
        # R3: the phase literal follows the scaffold method that made S
        si = next((j for j in range(gi - 1, -1, -1) if _binds(L[j], S)), None)
        sv = L[si].value if si is not None and isinstance(L[si], ast.Assign) else None
        meth = (sv.func.attr if isinstance(sv, ast.Call) and isinstance(sv.func, ast.Attribute)
                and _is_name(sv.func.value, sc) and sv.func.attr in ("forced", "chosen") else None)
        kw = {x.arg: x.value for x in c.keywords}
        ph = kw.get("phase")
        ph = ph.value if isinstance(ph, ast.Constant) and isinstance(ph.value, str) else None
        phases.append(ph)
        want_ph = {"forced": "forced", "chosen": "free"}.get(meth)
        if want_ph is None or ph != want_ph:
            probs.append(f"R3 {rel}:{c.lineno}: phase={ph!r} does not match {S}'s scaffold method "
                         f"({sc}.{meth or '?'})")
        # R4 / R5: the keywords
        want_kw = ({"render", "item", "earlier", "own_pair", "echo_lines", "phase"} if sub == "qwen"
                   else {"own_pair", "echo_lines", "phase"})
        if None in kw or set(kw) != want_kw:
            probs.append(f"R4 {rel}:{c.lineno}: classify's keywords are {sorted(map(str, kw))}, "
                         f"expected {sorted(want_kw)}")
        if sub == "qwen":
            if not _is_attr(kw.get("render"), S, "task_text"):
                probs.append(f"R4 {rel}:{c.lineno}: render is not {S}.task_text")
            if not _is_attr(kw.get("item"), S, "item"):
                probs.append(f"R4 {rel}:{c.lineno}: item is not {S}.item")
            if not _is_name(kw.get("earlier"), "earlier"):
                probs.append(f"R4 {rel}:{c.lineno}: earlier is not the session's earlier list")
        if not _is_name(kw.get("own_pair"), "own") or not _is_name(kw.get("echo_lines"), "echo_lines"):
            probs.append(f"R5 {rel}:{c.lineno}: own_pair / echo_lines are not own / echo_lines")
        # R6: the next statement records exactly this round
        nxt = L[k + 1] if k + 1 < len(L) else None
        nv = nxt.value if isinstance(nxt, ast.Expr) else None
        if not (isinstance(nv, ast.Call) and _is_attr(nv.func, "log", "add_round") and not nv.keywords
                and [a.id if isinstance(a, ast.Name) else None for a in nv.args] == [S, G, ra, "term_rx"]):
            probs.append(f"R6 {rel}:{c.lineno}: the next statement is not log.add_round({S}, {G}, {ra}, term_rx)")
    if sorted(p for p in phases if p is not None) != ["forced", "free"] or len(phases) != 2:
        probs.append(f"R3 {rel}: classify phases are {phases}, expected one 'forced' and one 'free'")
    # R4: Qwen's earlier = [] once, appended only with a scored generation's .text
    if sub == "qwen":
        v = _single_value(fn, "earlier")
        if not (isinstance(v, ast.List) and not v.elts):
            probs.append(f"R4 {rel}: earlier is not bound once to an empty list")
        apps = [n for n in ast.walk(fn) if isinstance(n, ast.Call) and _is_attr(n.func, "earlier", "append")]
        for a in apps:
            if (len(a.args) != 1 or a.keywords or not isinstance(a.args[0], ast.Attribute)
                    or a.args[0].attr != "text" or not _is_name(a.args[0].value)
                    or a.args[0].value.id not in gnames):
                probs.append(f"R4 {rel}:{a.lineno}: earlier.append takes something other than a scored "
                             f"generation's .text")
        uses = sum(1 for n in ast.walk(fn) if _is_name(n, "earlier"))
        allowed = 1 + len(apps) + sum(1 for c in calls for x in c.keywords
                                      if x.arg == "earlier" and _is_name(x.value, "earlier"))
        if uses != allowed or not apps:
            probs.append(f"R4 {rel}: earlier is used outside its binding, its appends and classify "
                         f"({uses} uses, {allowed} accounted for)")
        # R4 order: a round's own text never reaches its own classify's earlier -- each
        # earlier.append(G.text) is a statement of the block that scored G, after that classify,
        # with G not rebound in between; each classify site is followed by exactly one
        stmt_of = {id(st.value): (L2, j) for L2 in _stmt_lists(fn) for j, st in enumerate(L2)
                   if isinstance(st, ast.Expr)}

        def app_name(a) -> str | None:
            x = a.args[0] if len(a.args) == 1 and not a.keywords else None
            return (x.value.id if isinstance(x, ast.Attribute) and x.attr == "text" and _is_name(x.value)
                    else None)

        n_after = Counter()
        for a in apps:
            L2, j = stmt_of.get(id(a), (None, None))
            site = next((s for s in sites if L2 is s[0] and j > s[1] and app_name(a) == s[2]
                         and not any(_binds(st, s[2]) for st in s[0][s[1] + 1:j])), None)
            if site is None:
                probs.append(f"R4 {rel}:{a.lineno}: earlier.append is not a statement after the classify that "
                             f"scored its generation, in that block, the generation not rebound in between")
            else:
                n_after[id(site)] += 1
        for s in sites:
            if n_after[id(s)] != 1:
                probs.append(f"R4 {rel}:{s[3]}: the classify scoring {s[2]} is followed in its block by "
                             f"{n_after[id(s)]} earlier.append({s[2]}.text) (expected exactly 1)")
    return probs, gnames


def _add_round_problems(tree) -> list[str]:
    """R7: SessionLog.add_round's record literal carries str(g.text), termination(g.text, term_rx)
    and ra.as_dict() (g / ra its parameters, none rebound); after the literal r is only appended
    to self.rounds and returned; and no SessionLog method rewrites a recorded round's text,
    termination or audit (_rounds_rewrites)."""
    rel = SCAFFOLD_REL
    cls = [n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "SessionLog"]
    fns = [n for c in cls for n in c.body if isinstance(n, ast.FunctionDef) and n.name == "add_round"]
    if len(cls) != 1 or len(fns) != 1:
        return [f"R7 {rel}: {len(cls)} SessionLog class(es), {len(fns)} add_round definition(s)"]
    fn = fns[0]
    ps = [a.arg for a in fn.args.args]
    if len(ps) != 5 or ps[0] != "self":
        return [f"R7 {rel}:{fn.lineno}: add_round's parameters are {ps}, expected (self, spec, g, ra, term_rx)"]
    g, ra, rx = ps[2], ps[3], ps[4]
    probs = []
    for p in (g, ra, rx):
        if _bindings(fn, p):
            probs.append(f"R7 {rel}: add_round rebinds {p!r}")
    v = _single_value(fn, "r")
    if not isinstance(v, ast.Dict):
        return probs + [f"R7 {rel}: add_round's record r is not bound once to a dict literal"]
    ent: dict[str, list] = {}
    for kn, vn in zip(v.keys, v.values):
        if isinstance(kn, ast.Constant) and isinstance(kn.value, str):
            ent.setdefault(kn.value, []).append(vn)
    txt, term, aud = ent.get("text", []), ent.get("termination", []), ent.get("audit", [])
    if not (len(txt) == 1 and isinstance(txt[0], ast.Call) and _is_name(txt[0].func, "str")
            and len(txt[0].args) == 1 and _is_attr(txt[0].args[0], g, "text") and not txt[0].keywords):
        probs.append(f"R7 {rel}: the record's text is not str({g}.text)")
    if not (len(term) == 1 and isinstance(term[0], ast.Call) and _is_name(term[0].func, "termination")
            and len(term[0].args) == 2 and _is_attr(term[0].args[0], g, "text")
            and _is_name(term[0].args[1], rx) and not term[0].keywords):
        probs.append(f"R7 {rel}: the record's termination is not termination({g}.text, {rx})")
    if not (len(aud) == 1 and isinstance(aud[0], ast.Call) and _is_attr(aud[0].func, ra, "as_dict")
            and not aud[0].args and not aud[0].keywords):
        probs.append(f"R7 {rel}: the record's audit is not {ra}.as_dict()")
    for n in ast.walk(fn):
        if (isinstance(n, ast.Subscript) and isinstance(n.ctx, (ast.Store, ast.Del)) and _is_name(n.value, "r")
                and isinstance(n.slice, ast.Constant) and n.slice.value in R7_KEYS):
            probs.append(f"R7 {rel}:{n.lineno}: add_round rewrites r[{n.slice.value!r}]")
    # after its literal, r is only appended to self.rounds and returned: any other use (r.update,
    # r.__setitem__, r[...] = ..., an alias, dict.update(r, ...)) could rewrite the record
    apps = [n for n in ast.walk(fn) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
            and n.func.attr == "append" and _is_attr(n.func.value, "self", "rounds") and len(n.args) == 1
            and _is_name(n.args[0], "r") and not n.keywords]
    if not apps:
        probs.append(f"R7 {rel}: add_round does not append r to self.rounds")
    allowed = {id(a.args[0]) for a in apps}
    allowed |= {id(s.value) for s in ast.walk(fn) if isinstance(s, ast.Return) and _is_name(s.value, "r")}
    allowed |= {id(t) for s in _bindings(fn, "r") if isinstance(s, ast.Assign) for t in s.targets}
    for n in ast.walk(fn):
        if _is_name(n, "r") and id(n) not in allowed:
            probs.append(f"R7 {rel}:{n.lineno}: add_round uses r other than appending it to self.rounds "
                         f"and returning it")
    for m in (n for c in cls for n in c.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))):
        probs += _rounds_rewrites(rel, m)
    return probs


R7_KEYS = ("text", "termination", "audit")
_DICT_MUTATORS = ("update", "__setitem__", "setdefault", "pop", "__delitem__")
_LIST_MUTATORS = ("append", "extend", "insert", "__setitem__", "__delitem__", "pop", "remove", "clear",
                  "__iadd__")


def _rounds_rewrites(rel: str, fn) -> list[str]:
    """R7, SessionLog-wide (every method of the class): no subscript store / delete and no
    mutating call (update, __setitem__, setdefault, pop, __delitem__) on a round record -- a
    subscript of self.rounds, or a name bound by iterating or indexing it -- for the keys text,
    termination and audit (a key that is not a string constant counts); no record replaced,
    deleted or added in self.rounds except add_round's one self.rounds.append(r); self.rounds
    rebound in __init__ only. Syntactic: a plain alias of self.rounds (x = self.rounds) is
    followed one step; deeper aliasing, dict.update(record, ...) on an element and edits to the
    bodies of termination() / str are not (the dynamic runner-identity check covers the text)."""
    def is_rounds(e) -> bool:
        return _is_attr(e, "self", "rounds")

    lists: set[str] = set()
    for n in ast.walk(fn):
        if isinstance(n, ast.Assign) and is_rounds(n.value):
            for t in n.targets:
                lists.update(_target_names(t))

    def is_list(e) -> bool:
        return is_rounds(e) or (isinstance(e, ast.Name) and e.id in lists)

    elems: set[str] = set()
    for n in ast.walk(fn):
        it = tgt = None
        if isinstance(n, (ast.For, ast.AsyncFor, ast.comprehension)):
            it, tgt = n.iter, n.target
        elif isinstance(n, ast.Assign) and len(n.targets) == 1:
            it, tgt = n.value, n.targets[0]
        if it is not None and (isinstance(it, ast.Subscript) and is_list(it.value)
                               or isinstance(n, (ast.For, ast.AsyncFor, ast.comprehension)) and is_list(it)):
            elems.update(_target_names(tgt))

    def is_elem(e) -> bool:
        return (isinstance(e, ast.Subscript) and is_list(e.value)) or (isinstance(e, ast.Name) and e.id in elems)

    def key_hit(k) -> bool:
        return not (isinstance(k, ast.Constant) and isinstance(k.value, str)) or k.value in R7_KEYS

    probs = []
    where = f"R7 {rel}:{{}}: SessionLog.{fn.name} "
    for n in ast.walk(fn):
        if isinstance(n, ast.Subscript) and isinstance(n.ctx, (ast.Store, ast.Del)):
            if is_list(n.value):
                probs.append(where.format(n.lineno) + "replaces or deletes a round record in self.rounds")
            elif is_elem(n.value) and key_hit(n.slice):
                probs.append(where.format(n.lineno) + "rewrites a round record's text / termination / audit")
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
            tgt, meth = n.func.value, n.func.attr
            if is_list(tgt) and meth in _LIST_MUTATORS:
                own_append = (fn.name == "add_round" and is_rounds(tgt) and meth == "append" and len(n.args) == 1
                              and _is_name(n.args[0], "r") and not n.keywords)
                if not own_append:
                    probs.append(where.format(n.lineno) + f"changes self.rounds by .{meth}(...)")
            elif is_elem(tgt) and meth in _DICT_MUTATORS:
                hit = (bool(n.args) or any(k.arg is None or k.arg in R7_KEYS for k in n.keywords)
                       if meth == "update" else (not n.args or key_hit(n.args[0])))
                if hit:
                    probs.append(where.format(n.lineno) + f"rewrites a round record by .{meth}(...)")
        elif isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign)) and fn.name != "__init__":
            if any(is_rounds(t) for t in (n.targets if isinstance(n, ast.Assign) else [n.target])):
                probs.append(where.format(n.lineno) + "rebinds self.rounds outside __init__")
    return probs


def _classify_refs_outside(rel: str, tree) -> list[str]:
    """R8: classify references outside _selftest bodies and the two runner functions."""
    parents: dict[int, Any] = {}
    for n in ast.walk(tree):
        for ch in ast.iter_child_nodes(n):
            parents[id(ch)] = n
    probs = []
    allowed = RUNNER_FILES.get(rel, (None,))[0]
    for n in ast.walk(tree):
        if not (isinstance(n, ast.Attribute) and n.attr == "classify"):
            continue
        chain, p = [], parents.get(id(n))
        while p is not None:
            if isinstance(p, (ast.FunctionDef, ast.AsyncFunctionDef)):
                chain.append(p.name)
            p = parents.get(id(p))
        chain.reverse()
        if "_selftest" in chain or (allowed is not None and chain == [allowed]):
            continue
        probs.append(f"R8 {rel}:{n.lineno}: a classify reference outside a _selftest body and the "
                     f"runners' session functions ({'.'.join(chain) or 'module level'})")
    return probs


def runner_scope_problems(sources: Mapping[str, str] | None = None) -> dict:
    """Layer S: {files, rules, r8_scope, problems}; problems == [] iff R1-R8 hold."""
    # PIN (Code, declared at LOCK v0.1; PIN-S5): scoring scope is tested at the classifier
    # (Layer A) and at the runners' call into it (Layer S, this static check of the four
    # production classify sites and SessionLog.add_round). R1: exactly two audit.classify calls
    # per session function, on its audit parameter. R2: each scores <G>.text alone, G bound in
    # the same block by G = adapter.generate(<prefix>, <S>.seg, injections=(), ...), neither
    # rebound in between. R3: phase="forced" where S came from <sc>.forced(...), "free" where
    # from <sc>.chosen(...). R4 (Qwen): render=<S>.task_text, item=<S>.item, earlier=earlier (an
    # empty list appended only with a scored generation's .text, each append a statement after
    # the classify that scored that generation, in its block -- exactly one per classify, so a
    # round's own text never reaches its own classify); the keyword sets exact. R5:
    # own_pair=own, own = (sc.P, sc.Q); echo_lines from _audit.{sub}_echo_lines(sc.note_lines).
    # R6: the next statement is log.add_round(S, G, RA, term_rx). R7: add_round's record literal
    # carries str(g.text), termination(g.text, term_rx) and ra.as_dict() for its g / ra
    # parameters; after it, r is only appended to self.rounds and returned; no SessionLog method
    # stores into, deletes from or calls update / __setitem__ / setdefault / pop on a recorded
    # round's text, termination or audit, or changes self.rounds otherwise. R7 is a syntactic
    # check of those forms, not a proof against every rewrite (deep aliasing, dict.update(rec, ..),
    # an edited termination() body are outside it); the runner-identity self-test check binds
    # the recorded text dynamically. R8:
    # no other classify reference in valence_core/m/*.py outside _selftest bodies (gshape.py
    # exempt: it is the gate). The dynamic half (testing's doubles) runs in the m self-test
    # only; the stub is never on a run path (box_selftest_stub.py's docstring; stages.py's
    # STUB_MARK PIN).
    src = _package_sources() if sources is None else dict(sources)
    probs: list[str] = []
    files = {}
    trees = {}
    for rel, text in sorted(src.items()):
        if not (rel.startswith("valence_core/m/") and rel.endswith(".py")):
            continue
        try:
            trees[rel] = _parse(rel, text)
        except (SyntaxError, ValueError) as e:
            probs.append(f"R8 {rel}: does not parse ({type(e).__name__})")
    for rel, (fname, sub) in RUNNER_FILES.items():
        if rel not in src:
            probs.append(f"R1 {rel}: source absent")
            continue
        files[rel] = _sha256_text(src[rel])
        if rel in trees:
            probs += _runner_problems(rel, trees[rel], fname, sub)[0]
    if SCAFFOLD_REL not in src:
        probs.append(f"R7 {SCAFFOLD_REL}: source absent")
    else:
        files[SCAFFOLD_REL] = _sha256_text(src[SCAFFOLD_REL])
        if SCAFFOLD_REL in trees:
            probs += _add_round_problems(trees[SCAFFOLD_REL])
    for rel, tree in sorted(trees.items()):
        if rel != GSHAPE_REL:
            probs += _classify_refs_outside(rel, tree)
    return {"files": files, "rules": list(LAYER_S_RULES),
            "r8_scope": f"{len([r for r in trees if r != GSHAPE_REL])} files of valence_core/m/*.py "
                        f"(gshape.py exempt; _selftest bodies exempt)",
            "problems": probs}


# --- evaluation and the artifact ------------------------------------------------------------
def _stop_reasons(g: Mapping[str, Any], shape: Sequence[str], layer_s: Mapping[str, Any],
                  olmo_identical: bool | None) -> list[str]:
    reasons = set()
    if shape:
        reasons.add("shape")
    for unit in UNITS:
        if unit not in g:
            reasons.add(f"coverage:{unit}")
            continue
        gu, cu = g[unit]["grid"], g[unit]["controls"]
        if gu["n_misplaced"]:
            reasons.add("shape")
        if gu["n"] != N_PER_UNIT or not gu["coverage"]["exact"]:
            reasons.add(f"coverage:{unit}")
        if gu["n_fired"]:
            reasons.add(f"fire:{unit}")
        for c in CONTROLS_REQUIRED:
            if cu[c]["n"] == 0 or cu[c]["n_fired"] != cu[c]["n"]:
                reasons.add(f"control-silent:{unit}:{c}")
    if olmo_identical is False:
        reasons.add("olmo-grids-differ")
    if layer_s["problems"]:
        reasons.add("scope-static")
    return sorted(reasons)


def evaluate(*, canonical: bool = False, inputs: Mapping[str, Any] | None = None,
             scorer: Callable[[Placement], str] | None = None,
             controls: Mapping[str, Callable[[Placement], str]] | None = None,
             templates: Sequence[str] | None = None, sources: Mapping[str, str] | None = None,
             drop: Callable[[Placement], bool] | None = None,
             units: Sequence[str] | None = None) -> dict:
    """The artifact dict (verdict included). Every keyword but ``canonical`` is a self-test seam."""
    ins = inputs_of_record(canonical=canonical) if inputs is None else inputs
    shape = template_shape_problems(ROUND_TEMPLATES if templates is None else templates, ins["renders"])
    g = grid(ins, UNITS if units is None else units, scorer=scorer, controls=controls,
             templates=templates, drop=drop)
    present = [u for u in OLMO_UNITS if u in g]
    olmo_rows = sorted({g[u]["grid"]["rows_sha256"] for u in present})
    olmo_identical = (len(olmo_rows) == 1) if len(present) == len(OLMO_UNITS) else None
    ls = runner_scope_problems(sources)
    reasons = _stop_reasons(g, shape, ls, olmo_identical)
    pool, renders = ins["pool"], ins["renders"]
    sm = ins["sources_map"]                      # taken at the precondition (committed blobs on the canonical run)
    clo = dict(sorted(ins["import_closure"].items()))
    prov = {"package_sha256": ins["package_sha256"], "sources": sm["sources"], "tooling": sm["tooling"],
            "sources_digest": sources_digest(sm), "import_closure": clo,
            "import_closure_digest": _json_sha256(clo), "import_closure_scope": CLOSURE_SCOPE,
            "proposal_file": ins["proposal_rel"],
            "proposal_sha256": ins["proposal_sha256"], "numpy": _numpy_version(),
            "numpy_stream_known_answer": "clean (f|CORR|0 permutation)"}
    rq, ro = _schedule.roster_for("Q-F0"), _schedule.roster_for(OLMO_UNITS[0])
    art = {
        "schema": SCHEMA, "stage": STAGE, "spec": SPEC_REF, "criterion": CRITERION,
        "inputs": {
            "renders_sha256": RENDERS_SHA256_OF_RECORD, "n_renders": len(renders),
            "renders_source": (f"{MODEL_FREE_REL} renders_of_record.items[i].render, asserted equal to "
                               f"scaffold.pool_and_renders() and to the pinned sha256; never computed as "
                               f"G-SHAPE-F0's own ({RENDERS_RECORD_CITE})"),
            "gcal_model_free": {"path": MODEL_FREE_REL, "sha256": ins["model_free_sha256"]},
            "gcal_completability": {"path": COMPLETABILITY_REL, "sha256": ins["completability_sha256"],
                                    "verdict": ins["completability_verdict"]},
            "seat_read": {"path": SEAT_READ_REL, "sha256": ins["seat_sha256"],
                          "renders_sha256_cited": ins["seat_renders_sha256"]},
            "pools_file": _corr.POOLS_PATH.relative_to(REPO).as_posix(),
            "pools_file_sha256": ins["pools_file_sha256"],
            "pools_file_sha256_gcal_provenance": ins["pools_file_sha256_gcal"],
            "pool_sha16": _resume.pool_sha16(pool),
            "golds": {"n_items": len(pool), "n_variants": sum(len(it["gold"]) for it in pool),
                      "sha256": _json_sha256([list(it["gold"]) for it in pool])},
            "round_templates_sha256": _json_sha256(list(ROUND_TEMPLATES)),
            "olmo_round_templates": ("valence_core.session_e2a.ROUND_TEMPLATES (b3 imports it; m's "
                                     "scaffold._round formats it on both substrates)"),
            "session_banner_sha256": _sha256_text(SESSION_BANNER),
            "harness_strings_sha256": _json_sha256(list(_banner.HARNESS_STRINGS_QF0)),
            "roster_sha256": {"Q-F0": _json_sha256([list(p) for p in rq]),
                              "OLMo": _json_sha256([list(p) for p in ro])}},
        "stacks": {"qwen": ins["qwen_rec"], "olmo": ins["olmo_rec"]},
        "fire_predicate": {"round": list(ROUND_FIRE_FIELDS),
                           "rule": "a placement fires iff any field fires (PIN-S3); any fire is a STOP"},
        "grid": {u: g[u]["grid"] for u in g},
        "grid_total": sum(g[u]["grid"]["n"] for u in g),
        "controls": {u: g[u]["controls"] for u in g},
        "olmo_grids_identical": olmo_identical,
        "olmo_rows_sha256": olmo_rows,
        "template_shape": {"n_problems": len(shape), "problems": shape[:SHAPE_LISTED_MAX],
                           "n_range": [1, N_ROUNDS], "n_labels": len(shape_labels())},
        "layer_s": ls,
        "runner_dynamic_evidence": {
            "where": ("the m self-test (scripts/m_sessions.py --selftest) at this package_sha256; "
                      "testing's doubles, never on a run path (PIN-S5)"),
            "existing_checks": [{"module": m, "evidences": k, "check": c} for m, k, c in RUNNER_DYNAMIC_EVIDENCE],
            "gshape_check": RUNNER_IDENTITY_CHECK},
        "verdict": "PASS" if not reasons else "STOP", "stop_reasons": reasons,
        "stop_reason_forms": list(STOP_REASON_FORMS),
        "provenance": prov}
    _resume.json_text(art)                       # JSON-native or TypeError, before anyone writes it
    return art


def _numpy_version() -> str:
    import numpy as np
    return np.__version__


def _tmp_path(p: Path) -> Path:
    return p.with_name(p.name + ".tmp")


def _write_once_text(path: Path, text: str) -> str:
    """'written' or 'identical'; GshapeRefusal if a different file (or a non-file, or a
    symlink) is there.

    PIN (Code, declared at LOCK v0.1; PIN-S9): the artifact is write-once -- identical bytes
    are accepted as they are, anything else is refused and left untouched (gcal's rule); the
    write is atomic (temp file, fsync, rename, directory fsync) and never through a symlink:
    neither the artifact path nor its temp name ``<name>.tmp`` may be a link (or, for the temp
    name, a non-file) -- write() refuses both before evaluating -- and the temp file is opened
    with O_NOFOLLOW, so a link planted there after that check fails the open instead of being
    followed (a stale regular temp file from a killed run is truncated, as before). A re-run on
    unchanged inputs is byte-identical (no timestamp, no HEAD). Supersession is by hand only, on
    the seat's ruling: the old artifact is moved with ``git mv`` to a dated superseded name
    recorded in an entry, and the re-run then writes the canonical name."""
    p = Path(path)
    if p.exists() or p.is_symlink():
        try:
            same = p.is_file() and not p.is_symlink() and p.read_text(encoding="utf-8") == text
        except (OSError, UnicodeDecodeError):
            same = False
        if not same:
            raise GshapeRefusal(f"G-SHAPE-F0 ARTIFACT EXISTS at {p} with different bytes (or as a link or "
                                f"non-file) -- it is never overwritten; supersession is a hand git mv on "
                                f"the seat's ruling")
        return "identical"
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = _tmp_path(p)
    try:
        fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_NOFOLLOW, 0o666)
    except OSError as e:
        raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: the temp file {tmp} could not be opened without following "
                            f"a link ({type(e).__name__}: {e.strerror}); nothing written") from None
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, p)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    _resume._fsync_dir(p.parent)
    return "written"


def write(out_dir: str | os.PathLike | None = None, **seams) -> dict:
    """G-SHAPE-F0: evaluate and write the artifact once. {"artifact", "path", "how"}; a STOP
    verdict is written too (exit 4 at the driver)."""
    # PIN (Code, declared at LOCK v0.1; PIN-S8/S9): with no --out the path is GATES_DIR /
    # G-SHAPE-F0.json (data/m/gates, admitted by .gitignore's gates *.json line); --out is a
    # test directory through resume.refuse_canonical_out, an empty one refused; a run with any
    # seam set (the self-test's) refuses the canonical path, as gport's supplied rows do.
    unknown = sorted(set(seams) - set(SEAMS))
    if unknown:
        raise TypeError(f"write: unknown seam(s) {unknown}")
    seams = {k: v for k, v in seams.items() if v is not None}
    if out_dir is None:
        if seams:
            raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: a seamed run ({sorted(seams)}) never writes the "
                                f"canonical artifact; name a test directory")
        d, canonical = Path(GATES_DIR), True
    else:
        if str(out_dir).strip() == "":
            raise GshapeRefusal("G-SHAPE-F0 REFUSED: an empty --out is refused (it would write into the "
                                "working directory)")
        try:
            d = _resume.refuse_canonical_out(out_dir)
        except SystemExit as e:
            raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: {e}") from None
        canonical = False
    path = d / ARTIFACT_NAME
    if path.is_symlink():
        raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: the artifact path {path} is a symlink -- never written "
                            f"through a link")
    tmp = _tmp_path(path)
    if tmp.is_symlink() or (tmp.exists() and not tmp.is_file()):
        raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: the temp name {tmp} is a symlink or a non-file -- never "
                            f"written through a link")
    ins = inputs_of_record(canonical=canonical) if seams.get("inputs") is None else seams.pop("inputs")
    art = evaluate(canonical=canonical, inputs=ins, **seams)
    text = _resume.json_text(art, indent=1)
    if canonical:
        drift = provenance_drift(ins)
        if drift:
            raise GshapeRefusal(f"G-SHAPE-F0 REFUSED: the sources drifted between the precondition and the write "
                                f"-- {drift[:4]}" + (f" (+{len(drift) - 4} more)" if len(drift) > 4 else "")
                                + f"; nothing written (this run's verdict {art['verdict']} is not recorded)")
    try:
        how = _write_once_text(path, text)
    except GshapeRefusal as e:
        raise GshapeRefusal(f"{e} (this run's verdict {art['verdict']} is not recorded)") from None
    return {"artifact": art, "path": path, "how": how, "canonical": canonical}


def summary_lines(res: Mapping[str, Any]) -> list[str]:
    """The driver's stdout after INVOCATION: counts and hashes only (no label, pick or menu)."""
    a = res["artifact"]
    inp, prov = a["inputs"], a["provenance"]
    n_src = len(prov["sources"]) + len(prov["tooling"])
    lines = [f"G-SHAPE-F0 inputs: renders sha256 {inp['renders_sha256']}; G-CAL model-free sha256 "
             f"{inp['gcal_model_free']['sha256']}; proposal sha256 {prov['proposal_sha256']}",
             f"G-SHAPE-F0 provenance: package sha256 {prov['package_sha256']}; sources digest "
             f"{prov['sources_digest']} ({n_src} files); import closure digest {prov['import_closure_digest']} "
             f"({len(prov['import_closure'])} files outside valence_core/m); sources committed at HEAD: "
             + ("yes (checked with every m package file and the import closure: canonical run, before scoring "
                "and again before the write)" if res["canonical"] else "not checked (--out test directory)")]
    for u in UNITS:
        if u not in a["grid"]:
            lines.append(f"G-SHAPE-F0 grid {u}: not scored")
            continue
        gu, cu = a["grid"][u], a["controls"][u]
        lines.append(f"G-SHAPE-F0 grid {u}: {gu['n']} placements, {gu['n_fired']} fired")
        lines.append("G-SHAPE-F0 controls " + u + ": "
                     + "; ".join(f"{c} {cu[c]['n_fired']}/{cu[c]['n']} "
                                 f"({'required' if cu[c]['required'] else 'reported'})" for c in sorted(cu)))
    oi = a["olmo_grids_identical"]
    lines.append("G-SHAPE-F0 OLMo grids identical across the three checkpoints: "
                 + ("yes" if oi is True else "NO" if oi is False else "n/a"))
    ts, ls = a["template_shape"]["n_problems"], len(a["layer_s"]["problems"])
    lines.append(f"G-SHAPE-F0 template shape: {'clean' if not ts else f'{ts} problems'}; runner scope "
                 f"(static): {'clean' if not ls else f'{ls} problems'}")
    lines.append(f"G-SHAPE-F0 verdict {a['verdict']}"
                 + (f" {' '.join(a['stop_reasons'])}" if a["stop_reasons"] else ""))
    lines.append(f"G-SHAPE-F0 artifact: {res['path']} ({res['how']})")
    return lines


# --- the canonical paths' state (the selftests' no-write checks) ----------------------------
def canonical_files(gates_dir: str | os.PathLike | None = None) -> dict[str, Path]:
    """data/m/gates/G-SHAPE-F0.json and any other G-SHAPE* entry there (GATES_DIR at call time,
    or ``gates_dir``: the self-test names the real directory while its sandbox patches GATES_DIR)."""
    g = Path(GATES_DIR if gates_dir is None else gates_dir)
    out = {f"gates/{ARTIFACT_NAME}": g / ARTIFACT_NAME}
    if g.is_dir():
        out.update({f"gates/{p.name}": p for p in g.glob("G-SHAPE*")})
    return out


def canonical_snapshot(gates_dir: str | os.PathLike | None = None) -> dict[str, Any]:
    # PIN (Code, declared at LOCK v0.1): gcal's snapshot rule -- bytes (or absence) before and
    # after; the canonical artifact may exist (before or after the run of record).
    return {k: _gcal._path_state(p) for k, p in sorted(canonical_files(gates_dir).items())}


@contextlib.contextmanager
def _selftest_sandbox(mod=None, roots: Sequence[str | os.PathLike] | None = None) -> Iterator[Path]:
    """Self-test only, never on a run path (re-verification round 1, F1): a self-test case that
    writes runs inside this -- ``mod``'s GATES_DIR (this module's by default) and
    guard.GATES_DIR pointed at a fresh temp dir, and ``mod``'s _write_once_text refusing any
    path under ``roots`` (default resume.CANONICAL_ROOTS: data/m, /workspace/models, data/olmo)
    -- so no regression (a write() that ignores --out, a driver that drops it, a path hard-coded
    under data/m) can write a canonical path from inside a self-test, before the build commit
    or after it. Yields the temp canonical gates directory (absent until something writes it)."""
    import tempfile
    from unittest import mock
    mod = sys.modules[__name__] if mod is None else mod
    protect = tuple(Path(r).resolve() for r in (_resume.CANONICAL_ROOTS if roots is None else roots))
    real_write = mod._write_once_text

    def guarded(path, text):
        rp = Path(path).resolve()
        if any(rp == r or r in rp.parents for r in protect):
            raise GshapeRefusal(f"G-SHAPE-F0 selftest sandbox: a write under a canonical root ({path}) is never "
                                f"made from a self-test")
        return real_write(path, text)

    with tempfile.TemporaryDirectory(prefix="gshape_sandbox_") as td:
        canon = Path(td) / "gates"
        with mock.patch.object(mod, "GATES_DIR", canon), mock.patch.object(guard, "GATES_DIR", canon), \
                mock.patch.object(mod, "_write_once_text", guarded):
            yield canon


# --- self-test -------------------------------------------------------------------------------
def _mutated_module(mod, old: str, new: str):
    """A copy of ``mod`` executed from its source with ``old`` replaced once by ``new`` (the
    self-test's runner mutations; in memory only, never written); None if ``old`` is absent."""
    import sys
    import types
    src = Path(mod.__file__).read_text(encoding="utf-8")
    if old not in src:
        return None
    name = f"{mod.__name__}__gshape_mutant"
    m = types.ModuleType(name)
    m.__package__ = mod.__package__
    m.__file__ = mod.__file__
    sys.modules[name] = m
    try:
        exec(compile(src.replace(old, new, 1), f"<{name}>", "exec"), m.__dict__)
    finally:
        sys.modules.pop(name, None)
    return m


def _pin_s_declarations(src: str) -> dict[int, list[str]]:
    """{k: [the text of each PIN declaration citing PIN-Sk]}: a declaration is a run of '#'
    comment lines (or a docstring paragraph) opening 'PIN (Code, declared at LOCK v0.1; ...)'
    whose parenthesis cites PIN-Sk (PIN-S8/S9 cites both)."""
    out: dict[int, list[str]] = {}
    lines = src.splitlines()
    for i, ln in enumerate(lines):
        m = re.search(r"PIN \(Code, declared at LOCK v0\.1; ([^)]*)\)", ln)
        if not m or "PIN-S" not in m.group(1):
            continue
        comment = ln.lstrip().startswith("#")
        block = [ln.strip().lstrip("#").strip()]
        for nxt in lines[i + 1:]:
            t = nxt.strip()
            if (comment and not t.startswith("#")) or (not comment and (not t or t.startswith('"""'))):
                break
            if comment and "PIN (Code, declared at LOCK v0.1" in t:
                break
            block.append(t.lstrip("#").strip() if comment else t)
            if not comment and '"""' in t:
                break
        text = " ".join(block)
        for a, b in re.findall(r"PIN-S(\d+)((?:/S\d+)*)", m.group(1)):
            for k in [a] + re.findall(r"\d+", b):
                out.setdefault(int(k), []).append(text)
    return out


def _chk_name_templates(src: str) -> set[str]:
    """The chk(...) names of a module's source, an f-string's fields as "{}"."""
    out = set()
    for n in ast.walk(ast.parse(src)):
        if not (isinstance(n, ast.Call) and _is_name(n.func, "chk") and n.args):
            continue
        a = n.args[0]
        if isinstance(a, ast.Constant) and isinstance(a.value, str):
            out.add(a.value)
        elif isinstance(a, ast.JoinedStr):
            out.add("".join(v.value if isinstance(v, ast.Constant) else "{}" for v in a.values))
    return out


def _chk_note_templates(src: str, prefix: str) -> list[list[str]]:
    """For each chk(name, ok, *notes) call of a module's source whose name starts with ``prefix``:
    its note arguments, an f-string's fields rendered as '{<source>}' (decisions item 5)."""
    def render(x) -> str:
        if isinstance(x, ast.JoinedStr):
            return "".join(v.value if isinstance(v, ast.Constant) else "{" + ast.unparse(v.value) + "}"
                           for v in x.values)
        if isinstance(x, ast.Constant) and isinstance(x.value, str):
            return x.value
        return ast.unparse(x)

    out = []
    for n in ast.walk(ast.parse(src)):
        if not (isinstance(n, ast.Call) and _is_name(n.func, "chk") and len(n.args) >= 2):
            continue
        a0 = n.args[0]
        name = (a0.value if isinstance(a0, ast.Constant) and isinstance(a0.value, str)
                else render(a0) if isinstance(a0, ast.JoinedStr) else None)
        if name is not None and name.startswith(prefix):
            out.append([render(x) for x in n.args[2:]])
    return out


def _selftest(chk) -> None:
    # (re-verification round 1, F1) the whole self-test runs inside _selftest_sandbox: GATES_DIR
    # (and guard.GATES_DIR) a temp dir and the write refusing every canonical root, so no case --
    # the positive --out writes included, under any regression, before or after the build
    # commit -- can write data/m/gates; the real directory is named explicitly where it is checked.
    me = sys.modules[__name__]
    real_gates, real_write = Path(GATES_DIR), _write_once_text
    with _selftest_sandbox() as sandbox_gates:
        if not (Path(me.GATES_DIR) == sandbox_gates == Path(guard.GATES_DIR) and sandbox_gates != real_gates
                and me._write_once_text is not real_write):
            raise RuntimeError("G-SHAPE-F0 selftest: the sandbox is not active -- no case runs outside it")
        _selftest_body(chk, real_gates, sandbox_gates)


def _selftest_body(chk, real_gates: Path, sandbox_gates: Path) -> None:
    import dataclasses
    import tempfile
    import types
    from unittest import mock

    from . import runner_qwen as _rq
    from . import testing

    me = sys.modules[__name__]
    outer_chk = chk
    n_chk = [0]

    def chk(name, ok, *rest) -> None:                      # every check counted (sec below)
        n_chk[0] += 1
        outer_chk(name, ok, *rest)

    @contextlib.contextmanager
    def sec(label: str, n: int):
        # (verification round 2, residual 6) each section declares
        # its check count; if it raises, its unreported checks are reported FAIL with the exception
        # (the total stays constant) and every later section still runs -- one failure never hides
        # the rest.
        start = n_chk[0]
        try:
            yield
        except (Exception, SystemExit) as e:               # noqa: BLE001 -- reported as FAIL, never lost
            done = n_chk[0] - start
            for j in range(max(n - done, 1)):
                chk(f"gshape: self-test section {label} raised before its check {done + j + 1} of {n}", False,
                    f"{type(e).__name__}: {e}")

    def raised(fn, exc) -> tuple[bool, str]:
        try:
            fn()
        except exc as e:                                   # noqa: PERF203
            return True, str(e)
        except (Exception, SystemExit) as e:               # noqa: BLE001 -- the wrong kind is a failure
            return False, f"{type(e).__name__}: {e}"
        return False, "nothing raised"

    def attempt(fn) -> tuple[Any, str]:
        """(result, "") or (None, the exception): every self-test write() goes through this or
        raised(), so a failing write is a FAIL of its own check, never an abort of the rest."""
        try:
            return fn(), ""
        except (Exception, SystemExit) as e:               # noqa: BLE001
            return None, f"{type(e).__name__}: {e}"

    def need(res, err: str, what: str):
        if res is None:
            raise RuntimeError(f"{what} raised: {err}")
        return res

    reached: list[str] = []

    def no_write(path, text):
        # the write sentinel of the must-refuse cases: nothing reaches a real write there
        reached.append(str(path))
        raise GshapeRefusal(f"G-SHAPE-F0 selftest sentinel: a case that must refuse reached the write ({path})")

    snap0 = canonical_snapshot(real_gates)
    # seg+gold's fired fields on the inputs of record (lexical_raw: the header's Q label hitting the
    # round's own pair, which score() must pass through)
    SEG_GOLD_FIELDS = {"qwen": ["claim", "v3.exclusion", "lexical_raw", "degeneracy", "ends", "strict"],
                       "olmo": ["claim", "lexical_raw", "degeneracy", "ends", "strict"]}
    pkg = _resume.package_sha256()
    sm = sources_map()
    dig = sources_digest(sm)
    # F3 (re-verification round 1): the seven modules outside valence_core/m and the scoring stack that
    # gshape's imports load (the verifier's list); the closure is rebuilt here from each loaded module's
    # __spec__.origin, independently of import_closure()
    F3_CLOSURE = ("valence_core/__init__.py", "valence_core/adapters/__init__.py", "valence_core/adapters/base.py",
                  "valence_core/e2d/__init__.py", "valence_core/e2d/runner.py", "valence_core/readout.py",
                  "valence_core/stats.py")

    def closure_indep() -> list[str]:
        out_ = set()
        for nm_ in list(sys.modules):
            if nm_.split(".")[0] != "valence_core":
                continue
            origin = getattr(getattr(sys.modules.get(nm_), "__spec__", None), "origin", None)
            if not origin or not os.path.isfile(origin):
                continue
            rel_ = os.path.relpath(os.path.realpath(origin), os.path.realpath(REPO)).replace(os.sep, "/")
            if not rel_.startswith("valence_core/m/"):
                out_.add(rel_)
        return sorted(out_)

    clo_rels = closure_indep()
    clo_map = {rel: _sha256((REPO / rel).read_bytes()) for rel in clo_rels}
    cdig = _json_sha256(clo_map)
    ins = inputs_of_record(canonical=False)
    pool, renders, rx = ins["pool"], ins["renders"], ins["term_rx"]
    real_committed = _stages._committed
    mf0 = json.loads((REPO / MODEL_FREE_REL).read_bytes())
    comp0 = json.loads((REPO / COMPLETABILITY_REL).read_bytes())
    seat0 = (REPO / SEAT_READ_REL).read_bytes()
    prop0 = (REPO / _stages.PROPOSAL_REL).read_bytes()
    e2a0 = json.loads(Path(_audit.E2A_BAN_LIST_PATH).read_bytes())
    pair = (UNITS[0], OLMO_UNITS[0])                 # one unit per substrate keeps the variants cheap
    one = (UNITS[0],)
    all_fire = sorted(f"fire:{u}" for u in UNITS)
    word = "harness bytes or the render itself"
    prop_bad = prop0.replace(word.encode(), b"harness lines or the render itself", 1)
    # every file the canonical run's committed check reads, planted committed with the working
    # tree's bytes wherever a canonical case must pass -- so the self-test passes before a commit
    # with any of them edited (verification round 2, residual 1)
    pk_rels = package_files()
    live_rels = _dedup(list(SCORING_STACK_FILES) + list(TOOLING_FILES) + pk_rels + clo_rels)
    pk_only = "valence_core/m/stages.py"            # a package file in neither list (it hosts _committed)
    src_only = next(r for r in SCORING_STACK_FILES if r not in pk_rels)   # a listed file outside the package
    clo_only = "valence_core/stats.py"              # an import-closure file in no other list (F3)

    def live_bytes() -> dict:
        return {rel: (REPO / rel).read_bytes() for rel in live_rels}

    def planted(over):
        def f(rel, repo=REPO):
            if rel in over:
                b = over[rel]
                return ([f"{rel}: not committed at HEAD (selftest plant)"], None) if b is None else ([], b)
            return real_committed(rel, repo)
        return f

    def mf_with(fn):
        m = json.loads(json.dumps(mf0))
        fn(m)
        return json.dumps(m).encode("utf-8")

    def comp_with(fn):
        m = json.loads(json.dumps(comp0))
        fn(m)
        return json.dumps(m).encode("utf-8")

    def one_off(r: str) -> str:
        return r[:-1] + ("x" if r[-1] != "x" else "y")

    def one_byte(m):
        m["renders_of_record"]["items"][3]["render"] = one_off(m["renders_of_record"]["items"][3]["render"])

    a: dict = {}

    # --- 1. the gate on the inputs of record, into a temp --out, twice ----------------------------
    with sec("1", 3):
        # (F1) inside the self-test sandbox: GATES_DIR is a temp dir, not data/m/gates, and nothing reaches it
        in_sandbox = Path(GATES_DIR) == sandbox_gates != real_gates and Path(guard.GATES_DIR) == sandbox_gates
        with tempfile.TemporaryDirectory(prefix="gshape_selftest_") as td:
            out = Path(td) / "gates"
            r1, e1 = attempt(lambda: write(out))
            b1 = (out / ARTIFACT_NAME).read_bytes() if (out / ARTIFACT_NAME).is_file() else b""
            r2, e2 = attempt(lambda: write(out))
            b2 = (out / ARTIFACT_NAME).read_bytes() if (out / ARTIFACT_NAME).is_file() else b""
        a = need(r1, e1, "write(--out)")["artifact"]
        ok = (in_sandbox and not sandbox_gates.exists()
              and r2 is not None and a["verdict"] == "PASS" and a["stop_reasons"] == [] and r1["how"] == "written"
              and r2["how"] == "identical" and b1 == b2 == _resume.json_text(a, indent=1).encode("utf-8")
              and r1["canonical"] is False and a["grid_total"] == len(UNITS) * N_PER_UNIT == 11264
              and all(a["grid"][u]["n"] == N_PER_UNIT and a["grid"][u]["n_fired"] == 0 and a["grid"][u]["fires"] == []
                      and a["grid"][u]["n_misplaced"] == 0 and a["grid"][u]["coverage"]["exact"] for u in UNITS)
              and all(a["controls"][u]["seg+gold"]["n_fired"] == a["controls"][u]["seg+gold"]["n"] == N_PER_UNIT
                      for u in UNITS)
              and all(a["controls"][u]["seg+gold"]["fired_fields"]
                      == (SEG_GOLD_FIELDS["qwen"] if u == "Q-F0" else SEG_GOLD_FIELDS["olmo"]) for u in UNITS)
              and [a["controls"][u]["render-as-response"]["n_fired"] for u in UNITS] == [256, 0, 0, 0]
              and a["controls"]["Q-F0"]["render-as-response"]["fired_items"] == [2, 8]
              and a["controls"]["Q-F0"]["render-as-response"]["advisories"] == ["content:task_echo"]
              and a["layer_s"]["problems"] == [] and a["template_shape"]["n_problems"] == 0
              and a["olmo_grids_identical"] is True and len(a["olmo_rows_sha256"]) == 1)
        chk("gshape: the gate on the inputs of record into a temp --out -- PASS: 2,816 placements per unit "
            "(11,264), 0 fired; seg+gold fired on 2,816/2,816 per unit, its fields exactly Qwen [claim, "
            "v3.exclusion, lexical_raw, degeneracy, ends, strict] / OLMo [claim, lexical_raw, degeneracy, ends, "
            "strict] (lexical_raw: the header's Q label hits the round's own pair as score() passes it); "
            "render-as-response (reported) Qwen "
            "256/2,816 (task_echo, items 2 and 8), OLMo 0; template shape and runner scope (static) clean; "
            "the three OLMo grids identical; a re-run finds the bytes identical (exit-0 'identical'); both writes "
            "run inside the self-test sandbox (GATES_DIR and guard.GATES_DIR a temp dir, not data/m/gates; "
            "nothing reaches it)",
            ok, (a["verdict"], a["stop_reasons"], [a["controls"][u]["render-as-response"]["n_fired"] for u in UNITS]),
            e2)
        prov = a["provenance"]
        chk("gshape: provenance of this self-test -- its package_sha256 and sources digest (SCORING_STACK_FILES "
            "+ TOOLING_FILES, working-tree sha256) and its import-closure digest equal the artifact's; every "
            "listed file hashed; the import closure (F3) is the sha256 of every loaded valence_core module outside "
            "valence_core/m (rebuilt here from __spec__.origin), sorted, its seven non-scoring-stack modules "
            "(valence_core, adapters, adapters.base, e2d, e2d.runner, readout, stats) and the seven loaded "
            "scoring-stack modules among them",
            prov["package_sha256"] == pkg and prov["sources_digest"] == dig
            and sorted(prov["sources"]) == sorted(SCORING_STACK_FILES) and len(SCORING_STACK_FILES) == 26
            and sorted(prov["tooling"]) == sorted(TOOLING_FILES)
            and all(isinstance(v, str) and len(v) == 64 for v in list(prov["sources"].values())
                    + list(prov["tooling"].values()))
            and prov["import_closure"] == clo_map and list(prov["import_closure"]) == clo_rels
            and prov["import_closure_digest"] == cdig and prov["import_closure_scope"] == CLOSURE_SCOPE
            and set(F3_CLOSURE) <= set(clo_rels) and not any(r.startswith("valence_core/m/") for r in clo_rels)
            and {r for r in SCORING_STACK_FILES if r.endswith(".py") and not r.startswith("valence_core/m/")}
            <= set(clo_rels) and len(clo_rels) == 14,
            f"package_sha256 {pkg}", f"sources_digest {dig}", f"import_closure_digest {cdig}")
        want_out = (f"G-SHAPE-F0 provenance: package sha256 {pkg}; sources digest {dig} (28 files); import closure "
                    f"digest {cdig} (14 files outside valence_core/m); sources committed at HEAD: not checked "
                    f"(--out test directory)")
        chk("gshape: the --out run's provenance summary line is, word for word, 'G-SHAPE-F0 provenance: package "
            "sha256 <pkg>; sources digest <digest> (28 files); import closure digest <digest> (14 files outside "
            "valence_core/m); sources committed at HEAD: not checked (--out test directory)'",
            summary_lines(r1)[1] == want_out, summary_lines(r1)[1][-120:])

    # --- 1b. the artifact's record: every input, stack, grid and control value checked ----------
    with sec("1b", 1):
        def fsha(rel: str) -> str:
            return _sha256((REPO / rel).read_bytes())

        rq_, ro_ = _schedule.roster_for("Q-F0"), _schedule.roster_for(OLMO_UNITS[0])
        want_inp = {
            "renders_sha256": RENDERS_SHA256_OF_RECORD, "n_renders": N_ITEMS,
            "gcal_model_free": {"path": MODEL_FREE_REL, "sha256": fsha(MODEL_FREE_REL)},
            "gcal_completability": {"path": COMPLETABILITY_REL, "sha256": fsha(COMPLETABILITY_REL),
                                    "verdict": "PASS"},
            "seat_read": {"path": SEAT_READ_REL, "sha256": fsha(SEAT_READ_REL),
                          "renders_sha256_cited": RENDERS_SHA256_OF_RECORD},
            "pools_file": "data/f/pools.json", "pools_file_sha256": fsha("data/f/pools.json"),
            "pools_file_sha256_gcal_provenance": mf0["provenance"]["pools_file_sha256"],
            "pool_sha16": mf0["provenance"]["pool_sha16"],
            "golds": {"n_items": N_ITEMS, "n_variants": N_GOLD_VARIANTS,
                      "sha256": _json_sha256([list(it["gold"]) for it in pool])},
            "round_templates_sha256": _json_sha256(list(ROUND_TEMPLATES)),
            "session_banner_sha256": _sha256_text(SESSION_BANNER),
            "harness_strings_sha256": _json_sha256(list(_banner.HARNESS_STRINGS_QF0)),
            "roster_sha256": {"Q-F0": _json_sha256([list(p) for p in rq_]),
                              "OLMo": _json_sha256([list(p) for p in ro_])}}
        want_q = {"claim_order": list(_audit.QWEN_CLAIMS), "audit_v2_sha16": _audit.AUDIT_V2_SHA16,
                  "e2a_ban_list_sha256": _audit.E2A_BAN_LIST_SHA256, "audit_version": AUDIT_VERSION,
                  "n_scaffold_strings": len(e2a0["strings"]),
                  "scaffold_assertion": {"n_ids": len(e2a0["ids"]), "n_strings": len(e2a0["strings"]),
                                         "ban_list_sha256": _audit.E2A_BAN_LIST_SHA256},
                  "term_sha16": _sc.TERM_SHA16}
        want_o = {"claim_order": list(_audit.OLMO_CLAIMS), "audit_sha16": _ro.olmo_audit_sha16(_audit.OLMO_AUDIT),
                  "scaffold_strings": list(_audit.OLMO_SCAFFOLD_STRINGS),
                  "scaffold_strings_checked": {f"scaffold_{ck}.json": "equal" for ck in keys.CKPTS},
                  "term_sha16": _sc.TERM_SHA16, "ban_ids": {ck: dict(B3_BAN_LIST) for ck in keys.CKPTS}}
        bad_rec: list = []

        def same(where: str, got: Mapping[str, Any], want: Mapping[str, Any], descriptive: set) -> None:
            if set(got) != set(want) | descriptive:
                bad_rec.append((where, "keys", sorted(set(got) ^ (set(want) | descriptive))))
            bad_rec.extend((where, k) for k in sorted(want) if got.get(k) != want[k])

        inp = a["inputs"]
        same("inputs", inp, want_inp, {"renders_source", "olmo_round_templates"})
        if RENDERS_RECORD_CITE not in inp.get("renders_source", "") or MODEL_FREE_REL not in inp.get("renders_source", ""):
            bad_rec.append(("inputs", "renders_source"))
        same("stacks.qwen", a["stacks"]["qwen"], want_q, {"end_rule", "echo_set", "content_others"})
        same("stacks.olmo", a["stacks"]["olmo"], want_o, {"end_rule", "echo_set", "ban_ids_note"})
        if set(a["stacks"]) != {"qwen", "olmo"}:
            bad_rec.append(("stacks", sorted(a["stacks"])))
        for u in UNITS:
            gu, cu = a["grid"][u], a["controls"][u]
            # the placement keys in enumeration order, built here from the constants alone
            ukeys = [[u, pi, mp, cl, t, t + (5 if ph == "free" else 1), i, g, ph]
                     for pi in range(4) for mp in (0, 1) for cl in (0, 1) for t in range(N_TEMPLATES)
                     for i in range(N_ITEMS) for g in pool[i]["gold"] for ph in PHASES]
            if (gu["placements_sha256"] != _json_sha256(ukeys) or gu["rows_sha256"] == gu["placements_sha256"]
                    or gu["template"] != keys.templates(u)[0] or gu["substrate"] != ("qwen" if u == "Q-F0" else "olmo")
                    or gu["fires_listed"] != 0
                    or gu["coverage"] != {"renders": 16, "templates": 4, "phases": 2, "banners": 16,
                                          "gold_variants": 22, "exact": True}):
                bad_rec.append(("grid", u))
            if (sorted(cu) != sorted(CONTROLS_REQUIRED + CONTROLS_REPORTED)
                    or [cu[c]["required"] for c in ("seg+gold", "render-as-response")] != [True, False]
                    or any(cu[c]["n"] != N_PER_UNIT for c in cu)):
                bad_rec.append(("controls", u))
        if a["olmo_rows_sha256"] != sorted({a["grid"][u]["rows_sha256"] for u in OLMO_UNITS}):
            bad_rec.append(("olmo_rows_sha256",))
        if not all(_schedule.roster_for(u) == ro_ for u in OLMO_UNITS):
            bad_rec.append(("OLMo rosters differ",))
        if (a["fire_predicate"]["round"] != list(ROUND_FIRE_FIELDS)
                or a["template_shape"] != {"n_problems": 0, "problems": [], "n_range": [1, N_ROUNDS],
                                           "n_labels": len(shape_labels())}
                or a["layer_s"]["files"] != {r: _sha256_text(t) for r, t in _package_sources().items()
                                             if r in (*RUNNER_FILES, SCAFFOLD_REL)}
                or a["layer_s"]["rules"] != list(LAYER_S_RULES)
                or (a["schema"], a["stage"], a["spec"], a["criterion"]) != (SCHEMA, STAGE, SPEC_REF, CRITERION)
                or a["stop_reason_forms"] != list(STOP_REASON_FORMS)):
            bad_rec.append(("predicate / shape / layer_s / header",))
        pv = a["provenance"]
        if (pv["proposal_file"] != _stages.PROPOSAL_REL or pv["proposal_sha256"] != _sha256(prop0)
                or pv["numpy"] != _numpy_version() or pv["sources"] != sm["sources"] or pv["tooling"] != sm["tooling"]
                or pv["import_closure"] != {r: fsha(r) for r in closure_indep()}):
            bad_rec.append(("provenance",))
        chk("gshape: the artifact's record -- every inputs value (the renders pin, G-CAL's model-free and "
            "completability and the seat read's paths and sha256 of their bytes, the pools file and its G-CAL "
            "provenance sha, pool sha16, golds, templates, banner, harness strings, rosters), each stack's "
            "record (claim order, pinned shas, the Qwen scaffold assertion's result, the OLMo strings and ban "
            "ids), each grid's placements_sha256 (keys rebuilt here, not the rows), template, substrate and "
            "coverage, each control's required flag (seg+gold true, render-as-response false), the OLMo rows, "
            "the predicate, shape, Layer S files and provenance equal values computed here independently",
            not bad_rec, bad_rec[:4])

    # --- 2. the fire predicate: complete, every field mutation-sensitive -------------------------
    with sec("2", 1):
        RA = _audit.RoundAudit

        def v3(**kw):
            return {"exclusion": None, "advisory": [], "content_label": None, **kw}

        probes = {
            "claim": (RA("qwen", "free", "content", "content:x", v3=v3()), "77", {"claim", "strict"}),
            "advisory": (RA("qwen", "forced", None, None, v3=v3(), advisory=("content:x",)), "77", {"advisory"}),
            "v3.exclusion": (RA("qwen", "forced", None, None, v3=v3(exclusion="content:x")), "77",
                             {"v3.exclusion"}),
            "v3.content_label": (RA("qwen", "forced", None, None, v3=v3(content_label="x")), "77",
                                 {"v3.content_label"}),
            "v3.advisory": (RA("qwen", "forced", None, None, v3=v3(advisory=["content:x"])), "77",
                            {"v3.advisory"}),
            "echo_line": (RA("olmo", "forced", None, None, echo_line=0), "77", {"echo_line"}),
            "lexical_raw": (RA("olmo", "forced", None, None, lexical_raw="x"), "77", {"lexical_raw"}),
            "scaffold": (RA("olmo", "forced", None, None, scaffold=("<|pad|>",)), "77", {"scaffold"}),
            "degeneracy": (RA("qwen", "free", "v2", "audit:frame:[round"), "77", {"claim", "degeneracy", "strict"}),
            "ends": (RA("qwen", "free", "lexical", "lexical:x"), "77", {"claim", "ends", "strict"}),
            "strict": (RA("qwen", "free", "content", "content:x"), "77", {"claim", "strict"}),
            "termination": (RA("olmo", "forced", None, None), "77. End of session.", {"termination"}),
        }
        bad = []
        n_indep = 0
        for f, (ra, text, want) in probes.items():
            got = round_fires(ra, text, rx)
            if got != [x for x in ROUND_FIRE_FIELDS if x in want] or f not in want:
                bad.append((f, "fires", got))
            less = round_fires(ra, text, rx, tests=[t for t in FIRE_TESTS if t[0] != f])
            if set(less) != want - {f}:
                bad.append((f, "removed", less))
            if want == {f}:
                n_indep += 1
                if less != []:
                    bad.append((f, "independent", less))
        empty = round_fires(RA("olmo", "forced", None, None), "77", rx)
        chk("gshape: the fire predicate -- its table is ROUND_FIRE_FIELDS in order; each field's synthetic probe "
            "fires exactly its declared fields (degeneracy, ends and strict with a claim); removing a field from "
            "the table removes it from its probe's result, so every field is mutation-sensitive (the 8 "
            "independent fields' probes then fire nothing); an all-empty probe fires nothing",
            tuple(n for n, _ in FIRE_TESTS) == ROUND_FIRE_FIELDS and set(probes) == set(ROUND_FIRE_FIELDS)
            and not bad and n_indep == 8 and empty == [], bad[:3])

    # --- 3. real classes reach round_fires through the stacks of record --------------------------
    with sec("3", 2):
        rq, ro = _schedule.roster_for("Q-F0")[0], _schedule.roster_for(OLMO_UNITS[0])[0]
        _, nq = _banner.build_banner("A0", rq[0], rq[1], 0)
        _, no = _banner.build_banner(keys.templates(OLMO_UNITS[0])[0], ro[0], ro[1], 0)
        elq, elo = _audit.qwen_echo_lines(nq), _audit.olmo_echo_lines(no)

        def qf(t, item=0, earlier=(), phase="forced", render=None):
            r = renders[item] if render is None else render
            ra = ins["qwen_stack"].classify(t, render=r, item=item, earlier=earlier, own_pair=rq, echo_lines=elq,
                                            phase=phase)
            return round_fires(ra, t, rx)

        def of(t, phase="forced"):
            ra = ins["olmo_stack"].classify(t, own_pair=ro, echo_lines=elo, phase=phase)
            return round_fires(ra, t, rx)

        E5 = ["claim", "echo_line", "degeneracy", "ends", "strict"]
        C5 = ["claim", "v3.exclusion", "v3.content_label", "ends", "strict"]
        ADV = ["advisory", "v3.content_label", "v3.advisory"]
        qtab = [("an e2a ban string (v2 special + scaffold_absorption)", qf("<|im_end|>"),
                 ["claim", "v3.exclusion", "scaffold", "degeneracy", "ends", "strict"]),
                ("the COMMON Note line (echo)", qf(nq[0]), E5),
                ("the reasoning label (echo)", qf(_audit.REASONING_LABEL), E5),
                ("the TOLD line (echo, lexical raw beside)", qf(nq[1]),
                 ["claim", "echo_line", "lexical_raw", "degeneracy", "ends", "strict"]),
                ("'* * *' (null_response)", qf("* * *"), C5),
                ("a repeated answer (stuck_attractor)", qf("77", earlier=("77",)), C5),
                ("a preamble (preamble_without_content)", qf("Sure, I'll answer."), C5),
                ("another item's clean task (wrong_task advisory)", qf(pool[5]["task"]), ADV),
                ("item 2's render as its own response (task_echo advisory)", qf(renders[2], item=2), ADV),
                ("an own label (lexical)", qf("77 " + rq[1]), ["claim", "lexical_raw", "ends", "strict"]),
                ("an end-of-session line (termination only)", qf("77. End of session."), ["termination"]),
                ("an empty response (v2 empty)", qf(""), ["claim", "v3.exclusion", "degeneracy", "ends", "strict"]),
                ("'* * *' at free (no end at free)", qf("* * *", phase="free"),
                 ["claim", "v3.exclusion", "v3.content_label", "strict"]),
                ("COMMON without its final period (the N6 PIN: silent on Qwen)", qf(nq[0][:-1]), [])]
        otab = [("<|pad|> (scaffold only)", of("<|pad|>"), ["scaffold"]),
                ("<think> (AuditSpec + scaffold)", of("<think>"), ["claim", "scaffold", "degeneracy", "ends", "strict"]),
                ("COMMON without its final period at the end (echo stem)", of(no[0][:-1]), E5),
                ("an own label (lexical)", of("77 " + ro[1]), ["claim", "lexical_raw", "ends", "strict"]),
                ("an end-of-session line (termination only)", of("77. End of session."), ["termination"]),
                ("'* * *' (no OLMo class)", of("* * *"), [])]
        qbad = [nm for nm, got, want in qtab if got != want]
        obad = [nm for nm, got, want in otab if got != want]
        union = {f for _, got, _ in qtab for f in got}
        chk(f"gshape: real classes reach round_fires through the Qwen stack of record ({len(qtab)} cases: v2 "
            "special/empty, echo x3, null/stuck/preamble, wrong_task and task_echo advisories, lexical, "
            "termination, the free-phase end rule, and the silent period-less COMMON line); together they "
            "reach every field of ROUND_FIRE_FIELDS",
            not qbad and union == set(ROUND_FIRE_FIELDS), qbad)
        chk(f"gshape: real classes reach round_fires through the OLMo stack ({len(otab)} cases: <|pad|> scaffold "
            "only, <think> AuditSpec + scaffold, the echo stem, lexical, termination, '* * *' silent)",
            not obad, obad)

    # --- 3b. score() hands Qwen's stack the placement's own item ---------------------------------
    with sec("3b", 1):
        WT = "content:wrong_task"
        OTHER_ITEM_WRONG_TASK = (0, 1, 2, 3, 4, 6, 7, 9, 10, 12, 14)   # measured on the inputs of record
        qs = ins["qwen_stack"]
        base_pl = [pl for pl in placements("Q-F0", renders, pool)
                   if (pl.pi, pl.mp, pl.cl, pl.t, pl.gi, pl.phase) == (0, 0, 0, 0, 0, "forced")]
        oth_items = sorted(pl.i for pl in base_pl if WT in score(qs, pl, pool[(pl.i + 1) % N_ITEMS]["task"]).advisory)
        own_items = sorted(pl.i for pl in base_pl if WT in score(qs, pl, pool[pl.i]["task"]).advisory)
        a_oth = evaluate(inputs=ins, units=one, scorer=lambda pl: pool[(pl.i + 1) % N_ITEMS]["task"])
        chk("gshape: score() passes each placement's own item to Qwen's stack -- the next item's clean task "
            "scored as the response raises the wrong_task advisory on items "
            f"{OTHER_ITEM_WRONG_TASK} ({len(OTHER_ITEM_WRONG_TASK)}/16; the grid fires 1,920/2,816 on Q-F0), "
            "and an item's own clean task never does (an item shifted by one inverts both)",
            len(base_pl) == N_ITEMS and oth_items == list(OTHER_ITEM_WRONG_TASK) and own_items == []
            and a_oth["grid"]["Q-F0"]["n_fired"] == 1920, (oth_items, own_items, a_oth["grid"]["Q-F0"]["n_fired"]))

    # --- 4. scope-widened scorers, a silent control, coverage, OLMo identity ---------------------
    with sec("4a", 2):
        a_seg = evaluate(inputs=ins, scorer=lambda pl: pl.seg + pl.gold)
        a_bsg = evaluate(inputs=ins, scorer=lambda pl: pl.banner + pl.seg + pl.gold)
        a_ren = evaluate(inputs=ins, scorer=lambda pl: pl.render)
        a_gq = evaluate(inputs=ins, scorer=lambda pl: pl.gold + " " + pl.Q)
        a_gp = evaluate(inputs=ins, scorer=lambda pl: pl.gold + " " + pl.P)
        chk("gshape: scope-widened scorers STOP -- seg+gold and banner+seg+gold scored in place of the gold fire "
            "on 2,816/2,816 per unit; the gold followed by the round's Q label, or by its P label, fires "
            "2,816/2,816 per unit with lexical_raw on every listed fire (score() hands each stack the round's "
            "own pair); the render scored as the response fires Qwen 256 and OLMo 0 (the classifier-only "
            "blind spot Layer S covers)",
            a_seg["verdict"] == a_bsg["verdict"] == a_ren["verdict"] == "STOP"
            and a_seg["stop_reasons"] == all_fire == a_bsg["stop_reasons"] and a_ren["stop_reasons"] == ["fire:Q-F0"]
            and a_gq["stop_reasons"] == all_fire == a_gp["stop_reasons"]
            and all(x["grid"][u]["n_fired"] == N_PER_UNIT for x in (a_seg, a_bsg, a_gq, a_gp) for u in UNITS)
            and all(x["grid"][u]["fires"] and all("lexical_raw" in f["fields"] for f in x["grid"][u]["fires"])
                    for x in (a_gq, a_gp) for u in UNITS)
            and [a_ren["grid"][u]["n_fired"] for u in UNITS] == [256, 0, 0, 0]
            and all(len(a_seg["grid"][u]["fires"]) == FIRES_LISTED_MAX for u in UNITS),
            (a_seg["stop_reasons"], [a_ren["grid"][u]["n_fired"] for u in UNITS],
             [a_gq["grid"][u]["n_fired"] for u in UNITS], [a_gp["grid"][u]["n_fired"] for u in UNITS]))
        a_term = evaluate(inputs=ins, units=pair, scorer=lambda pl: pl.gold + ". End of session.")
        left2 = [f"coverage:{u}" for u in UNITS if u not in pair]
        chk("gshape: a fire on ONE field is a fire -- the gold followed by '. End of session.' fires the "
            "termination counter alone (every listed fire's fields exactly [termination]) on 2,816/2,816 per "
            "unit, Qwen and OLMo: STOP fire on both (the two units left out STOP coverage, nothing else)",
            a_term["stop_reasons"] == sorted([f"fire:{u}" for u in pair] + left2)
            and all(a_term["grid"][u]["n_fired"] == N_PER_UNIT and len(a_term["grid"][u]["fires"]) == FIRES_LISTED_MAX
                    and all(f["fields"] == ["termination"] for f in a_term["grid"][u]["fires"]) for u in pair),
            (a_term["stop_reasons"], [a_term["grid"][u]["n_fired"] for u in pair]))
    with sec("4b", 1):
        a_sil = evaluate(inputs=ins, controls={"seg+gold": _gold, "render-as-response": _render_alone})
        left_out = [f"coverage:{u}" for u in UNITS if u not in pair]
        a_part = evaluate(inputs=ins, units=pair,
                          controls={"seg+gold": lambda pl: pl.gold if pl.t == 3 else pl.seg + pl.gold,
                                    "render-as-response": _render_alone})
        n_part = N_PER_UNIT - N_PER_UNIT // N_TEMPLATES
        chk("gshape: a silent required control STOPs -- a seg+gold control that scores the gold alone is "
            "control-silent on every unit (0/2,816); one silent on template 3 only (fires 2,112/2,816, Qwen "
            "and OLMo) is control-silent too: the bound is 100% of placements, not 'fired at all'",
            a_sil["verdict"] == "STOP"
            and a_sil["stop_reasons"] == sorted(f"control-silent:{u}:seg+gold" for u in UNITS)
            and all(a_sil["controls"][u]["seg+gold"]["n_fired"] == 0 for u in UNITS)
            and a_part["stop_reasons"] == sorted([f"control-silent:{u}:seg+gold" for u in pair] + left_out)
            and n_part == 2112 and all(a_part["controls"][u]["seg+gold"]["n_fired"] == n_part
                                       and a_part["controls"][u]["seg+gold"]["n"] == N_PER_UNIT for u in pair),
            (a_sil["stop_reasons"], a_part["stop_reasons"],
             [a_part["controls"][u]["seg+gold"]["n_fired"] for u in pair]))
    with sec("4c", 1):
        cov_cases = {"one render dropped": {"drop": lambda pl: pl.i == 3},
                     "one template dropped": {"drop": lambda pl: pl.t == 2},
                     "one phase dropped": {"drop": lambda pl: pl.phase == "free"},
                     "one gold variant dropped": {"drop": lambda pl: pl.i == 1 and pl.gi == 1},
                     "one banner dropped": {"drop": lambda pl: (pl.pi, pl.mp, pl.cl) == (0, 0, 0)},
                     "an extra (duplicate) template": {"templates": tuple(ROUND_TEMPLATES) + (ROUND_TEMPLATES[0],)}}
        cov_bad = {}
        all_cov = sorted(f"coverage:{u}" for u in UNITS)
        x_pair = evaluate(inputs=ins, units=pair)        # the control: the two units left out, nothing else
        if (x_pair["stop_reasons"] != sorted(f"coverage:{u}" for u in UNITS if u not in pair)
                or x_pair["olmo_grids_identical"] is not None):
            cov_bad["units left out"] = x_pair["stop_reasons"]
        for nm, kw in cov_cases.items():
            x = evaluate(inputs=ins, units=pair, **kw)
            if x["stop_reasons"] != all_cov or not all(x["grid"][u]["n"] != N_PER_UNIT for u in pair):
                cov_bad[nm] = x["stop_reasons"]
        real_pl = placements

        def forced_twice(unit, rs, pl_, *, templates=None):
            # each forced placement yielded twice and no free one: the count stays 2,816 (selftest only)
            for x in real_pl(unit, rs, pl_, templates=templates):
                if x.phase == "forced":
                    yield x
                    yield x

        with mock.patch.object(me, "placements", forced_twice):
            x_same = evaluate(inputs=ins, units=pair)
        if (x_same["stop_reasons"] != all_cov or not all(x_same["grid"][u]["n"] == N_PER_UNIT
                                                         and x_same["grid"][u]["coverage"]["exact"] is False
                                                         and x_same["grid"][u]["n_misplaced"] == 0 for u in pair)):
            cov_bad["same count, wrong keys (forced twice, free none)"] = (
                x_same["stop_reasons"], [x_same["grid"][u]["n"] for u in pair])
        chk("gshape: coverage is the exact product per unit -- units left out STOP coverage on those units alone "
            "(OLMo identity then n/a); one render, template, phase, gold variant or banner dropped, or a "
            "duplicate template added, STOPs coverage on the scored units too (Q-F0 and one OLMo unit); a "
            "same-count enumeration with the wrong keys (each forced placement twice, no free one: n = 2,816, "
            "exact False) STOPs coverage by the exact-product term alone",
            not cov_bad and len(cov_cases) == 6, cov_bad)
    with sec("4d", 1):
        a_dif = evaluate(inputs=ins, scorer=lambda pl: pl.gold + " " if pl.unit == "OLMo-dpo" else pl.gold)
        chk("gshape: the three OLMo grids must be one computation -- a trailing space on one checkpoint's scored "
            "text (no fire) makes its rows differ: STOP olmo-grids-differ, nothing else",
            a_dif["stop_reasons"] == ["olmo-grids-differ"] and a_dif["olmo_grids_identical"] is False
            and len(a_dif["olmo_rows_sha256"]) == 2 and a_dif["grid"]["OLMo-dpo"]["n_fired"] == 0,
            a_dif["stop_reasons"])

    # --- 5. inputs: refusals and precondition STOPs (temp --out; committed reads planted) --------
    with sec("5", 3):
        seat_bad = seat0.replace(RENDERS_SHA256_OF_RECORD.encode(), (RENDERS_SHA256_OF_RECORD[:-1] + "0").encode())
        seat_noline = seat0.replace(b"renders_sha256: `", b"renders sha256 `")
        seat_twice = seat0 + b"\nrenders_sha256: `" + RENDERS_SHA256_OF_RECORD.encode() + b"`\n"
        nc = "not committed at HEAD (selftest plant)"
        refusal_cases = {                            # name: (planted committed bytes, message needles)
            "proposal not committed": ({_stages.PROPOSAL_REL: None}, (_stages.PROPOSAL_REL, nc)),
            "proposal's m:277 line one word changed": ({_stages.PROPOSAL_REL: prop_bad},
                                                       ("is not the governing proposal",)),
            "model-free artifact absent": ({MODEL_FREE_REL: None}, (MODEL_FREE_REL, nc)),
            "model-free wrong schema": ({MODEL_FREE_REL: mf_with(lambda m: m.update(schema="m-gcal-x"))},
                                        (f"is not {_gcal.MODEL_FREE_SCHEMA}",)),
            "proposal sha different from G-CAL's": ({MODEL_FREE_REL: mf_with(
                lambda m: m["provenance"].update(proposal_sha256="0" * 64))}, ("provenance proposal_sha256",)),
            "completability FAIL": ({COMPLETABILITY_REL: comp_with(lambda m: m.update(verdict="FAIL"))},
                                    (f"is not a {_gcal.ART_SCHEMA} PASS",)),
            "completability of another schema (verdict PASS)": ({COMPLETABILITY_REL: comp_with(
                lambda m: m.update(schema="m-gcal-x"))}, (f"is not a {_gcal.ART_SCHEMA} PASS",)),
            "completability absent": ({COMPLETABILITY_REL: None}, (COMPLETABILITY_REL, nc)),
            "seat read without its renders_sha256 line": ({SEAT_READ_REL: seat_noline},
                                                          ("carries no single 'renders_sha256",)),
            "seat read with two renders_sha256 lines (both the pin)": ({SEAT_READ_REL: seat_twice},
                                                                       ("carries no single 'renders_sha256",)),
            "seat read absent": ({SEAT_READ_REL: None}, (SEAT_READ_REL, nc))}
        # renders that reproduce (planted record == patched pool_and_renders) but do not hash to the pin
        rr = list(renders)
        rr[3] = one_off(rr[3])
        pool_dup_task = json.loads(json.dumps(pool))
        pool_dup_task[5]["task"] = pool_dup_task[4]["task"]
        pool_dup_gold = json.loads(json.dumps(pool))
        pool_dup_gold[1]["gold"][0] = pool_dup_gold[0]["gold"][0]

        def with_pool(p):
            return mf_with(lambda m: m["provenance"].update(pool_sha16=_resume.pool_sha16(p)))

        def scaffold_fails(*args, **kw):
            raise SystemExit("SCAFFOLD SET MISMATCH (selftest)")

        real_strings, real_b3 = _olmo_files()
        stop_cases = {                               # name: (planted bytes, [(obj, attr, value)], needles)
            "a render altered by one byte": ({MODEL_FREE_REL: mf_with(one_byte)}, [],
                                             ("recorded renders are not scaffold.pool_and_renders()",)),
            "G-CAL's renders sha256 not the pin": ({MODEL_FREE_REL: mf_with(
                lambda m: m["renders_of_record"].update(renders_sha256="0" * 64))}, [], ("is not the renders of record",)),
            "G-CAL condition (1) not PASS": ({MODEL_FREE_REL: mf_with(
                lambda m: m["conditions"]["1"].update(verdict="FAIL"))}, [], ("conditions ['1'] are not PASS",)),
            "G-CAL condition (2) not PASS": ({MODEL_FREE_REL: mf_with(
                lambda m: m["conditions"]["2"].update(verdict="FAIL"))}, [], ("conditions ['2'] are not PASS",)),
            "G-CAL's pool sha16 not the served pool's": ({MODEL_FREE_REL: mf_with(
                lambda m: m["provenance"].update(pool_sha16="0" * 16))}, [], ("served pool's sha16",)),
            "G-CAL's recorded pools_file_sha256 not the pools file's": ({MODEL_FREE_REL: mf_with(
                lambda m: m["provenance"].update(pools_file_sha256="0" * 64))}, [],
                ("not G-CAL's recorded pools_file_sha256",)),
            "completability on other renders": ({COMPLETABILITY_REL: comp_with(
                lambda m: m["identity"].update(renders_sha256="0" * 64))}, [], ("identity renders_sha256 is not",)),
            "the seat read citing other renders": ({SEAT_READ_REL: seat_bad}, [], ("cites renders_sha256",)),
            "renders that reproduce but do not hash to the pin": (
                {MODEL_FREE_REL: mf_with(one_byte)}, [(_sc, "pool_and_renders", lambda: (pool, list(rr)))],
                ("do not hash to the renders of record",)),
            "a clean task equal to another item's (31 distinct texts)": (
                {MODEL_FREE_REL: with_pool(pool_dup_task)},
                [(_sc, "pool_and_renders", lambda: (pool_dup_task, list(renders)))],
                ("are not 32 distinct single lines",)),
            "a gold variant duplicated across items": (
                {MODEL_FREE_REL: with_pool(pool_dup_gold)},
                [(_sc, "pool_and_renders", lambda: (pool_dup_gold, list(renders)))],
                ("distinct variants",)),
            "numpy's stream known answer": ({}, [(keys, "stream_known_answer", lambda: ["planted (selftest)"])],
                                            ("planted (selftest)", "numpy's stream")),
            "§2.5's banners": ({}, [(_banner, "spec_problems", lambda path=None: ["planted (selftest)"])],
                               ("not §2.5's bytes",)),
            "a stack's pinned v2 sha16": ({}, [(_audit, "AUDIT_V2_SHA16", "0" * 16)], ("AUDIT ARTIFACT MISMATCH",)),
            "the Qwen scaffold assertion failing": ({}, [(_audit, "assert_qwen_scaffold", scaffold_fails)],
                                                    ("a stack of record did not build",
                                                     "SCAFFOLD SET MISMATCH (selftest)")),
            "the termination patterns' sha16": ({}, [(_sc, "TERM_SHA16", "0" * 16)], ("TERMINATION PATTERNS MISMATCH",))}
        res_r, res_s = {}, {}

        def hit(r, needles) -> tuple[bool, str]:
            return (r[0] and all(x in r[1] for x in needles), r[1])

        with tempfile.TemporaryDirectory(prefix="gshape_inputs_") as td:
            out = Path(td) / "gates"
            # each checkpoint's own files, read from OLMO_DIR: a copy with one checkpoint's file changed
            olmo_cases = {"scaffold_dpo.json's own strings (each checkpoint's file read)":
                          ("scaffold_dpo.json", lambda o: o.update(ban_strings=list(o["ban_strings"])[:-1] + ["<|pad|> "]),
                           ("OLMo scaffold strings", "scaffold_dpo.json")),
                          "b3_screen_instruct.json's own ban_list (each checkpoint's file read)":
                          ("b3_screen_instruct.json", lambda o: o.update(ban_list={**o["ban_list"], "sha16": "0" * 16}),
                           ("b3_screen ban_list of ['instruct']",))}
            for j, (nm, (fname, edit, needles)) in enumerate(olmo_cases.items()):
                d_ = Path(td) / f"olmo{j}"
                d_.mkdir()
                for ck in keys.CKPTS:
                    for stem in ("scaffold", "b3_screen"):
                        (d_ / f"{stem}_{ck}.json").write_bytes((Path(OLMO_DIR) / f"{stem}_{ck}.json").read_bytes())
                o = json.loads((d_ / fname).read_bytes())
                edit(o)
                (d_ / fname).write_text(json.dumps(o), encoding="utf-8")
                stop_cases[nm] = ({}, [(me, "OLMO_DIR", d_)], needles)
            # V16: the pools file itself is hashed -- a copy one byte longer at POOLS_PATH (the pool served
            # unchanged) STOPs against G-CAL's recorded pools_file_sha256
            pools_copy = Path(td) / "pools.json"
            pools_copy.write_bytes(_corr.POOLS_PATH.read_bytes() + b"\n")
            stop_cases["the pools file changed on disk (one byte appended)"] = (
                {}, [(_corr, "POOLS_PATH", pools_copy)],
                ("the pools file hashes to", "not G-CAL's recorded pools_file_sha256"))
            for nm, (over, needles) in refusal_cases.items():
                with mock.patch.object(_stages, "_committed", planted(over)):
                    res_r[nm] = hit(raised(lambda: write(out), GshapeRefusal), needles)
            written_r = out.exists() and any(out.iterdir())
            for nm, (over, patches, needles) in stop_cases.items():
                with contextlib.ExitStack() as es:
                    es.enter_context(mock.patch.object(_stages, "_committed", planted(over)))
                    for obj, attr, val in patches:
                        es.enter_context(mock.patch.object(obj, attr, val))
                    res_s[nm] = hit(raised(lambda: write(out), GshapeStop), needles)
            written_s = out.exists() and any(out.iterdir())
        bad_r = {k: v[1][:100] for k, v in res_r.items() if not v[0]}
        bad_s = {k: v[1][:100] for k, v in res_s.items() if not v[0]}
        chk(f"gshape: {len(refusal_cases)} input defects refuse (GshapeRefusal, exit 2), each for its own reason, "
            "before any scoring -- "
            "proposal uncommitted or its m:277 line one word changed; G-CAL's model-free artifact absent, of "
            "another schema, or on another proposal; completability absent, FAIL, or of another schema; the "
            "seat read absent, without its renders_sha256 line, or with two -- and nothing is written",
            not bad_r and len(res_r) == 11 and not written_r, bad_r)
        chk(f"gshape: {len(res_s)} pinned figures that do not reproduce STOP, each for its own reason, before any "
            "scoring (GshapeStop, exit 4, no artifact) -- a recorded render one byte off, G-CAL's renders sha "
            "or condition (1) or (2), the pool sha16, G-CAL's recorded pools_file_sha256, the pools file itself "
            "one byte longer (it is hashed, not read from G-CAL), the completability identity's or the seat "
            "read's renders sha, renders that reproduce but miss the pin, a clean task or a gold variant "
            "duplicated, numpy's known answer, §2.5's banners, the v2 sha16, the Qwen scaffold assertion, the "
            "termination sha16, and one checkpoint's own scaffold or b3_screen file changed on disk (each "
            "checkpoint's file read)",
            not bad_s and len(res_s) == 19 and not written_s, bad_s)
        calls: list = []
        real_aqs = _audit.assert_qwen_scaffold

        def spy(ids, strings, audit3=None):
            calls.append((list(ids), list(strings), audit3))
            return real_aqs(ids, strings, audit3)

        with mock.patch.object(_audit, "assert_qwen_scaffold", spy):
            st_q, rec_q = qwen_stack(pool)
        chk("gshape: qwen_stack asserts the Qwen scaffold set -- assert_qwen_scaffold is called once, on the e2a "
            "ban-list file's ids and strings and the stack's own audit v3, and its result is the record's "
            "scaffold_assertion (its failure STOPs, above)",
            len(calls) == 1 and calls[0][0] == list(e2a0["ids"]) and calls[0][1] == list(e2a0["strings"])
            and calls[0][2] is st_q.audit3 and rec_q["scaffold_assertion"] == real_aqs(e2a0["ids"], e2a0["strings"],
                                                                                       st_q.audit3),
            [(len(c[0]), len(c[1])) for c in calls])

    # --- 6. the committed-sources precondition binds the canonical run -------------------------
    with sec("6", 2):
        live = live_bytes()
        other = live[pk_only] + b"\n# a committed blob that is not the working tree (selftest)\n"
        with tempfile.TemporaryDirectory(prefix="gshape_canon_") as td:
            gd = Path(td) / "gates"
            od = Path(td) / "out"
            with mock.patch.object(me, "GATES_DIR", gd):
                with mock.patch.object(_stages, "_committed", planted({**live, SCORING_STACK_FILES[0]: None})):
                    ref, msg = raised(lambda: write(None), GshapeRefusal)
                    sp_bad = sources_committed_problems()
                    nothing = not gd.exists()
                    r_out, e_out = attempt(lambda: write(od))   # a --out run does not check (PIN)
                one_ref = {}
                # each file on its own: tooling, a package-only file, an import-closure-only file (F3)
                for rel in TOOLING_FILES + (pk_only, clo_only):
                    with mock.patch.object(_stages, "_committed", planted({**live, rel: None})):
                        tr, tm = raised(lambda: write(None), GshapeRefusal)
                        one_ref[rel] = tr and "must be committed" in tm and rel in tm and not gd.exists()

                def clo_differs(rel, repo=REPO):
                    # the closure file's working tree differs from HEAD (stages._committed's problem form)
                    if rel == clo_only:
                        return [f"{rel}: the working tree differs from HEAD (selftest plant)"], None
                    return planted(live)(rel, repo)

                with mock.patch.object(_stages, "_committed", clo_differs):
                    dr_, dm_ = raised(lambda: write(None), GshapeRefusal)
                    clo_probs = committed_closure()[0]
                one_ref["an import-closure file whose working tree differs from HEAD"] = (
                    dr_ and "the import closure must be committed" in dm_ and "differs from HEAD" in dm_
                    and clo_only in dm_ and clo_probs == [f"{clo_only}: the working tree differs from HEAD (selftest "
                                                          f"plant)"] and not gd.exists())
                # a loaded valence_core module whose file is outside the repo (no committed blob can cover it)
                outside = Path(td) / "outside.py"
                outside.write_text("# a module file outside the repo (selftest)\n", encoding="utf-8")
                o_name = "valence_core.zz_gshape_selftest_outside"
                o_mod = types.ModuleType(o_name)
                o_mod.__file__ = str(outside)
                try:
                    sys.modules[o_name] = o_mod
                    with mock.patch.object(_stages, "_committed", planted(live)):
                        or_, om_ = raised(lambda: write(None), GshapeRefusal)
                finally:
                    sys.modules.pop(o_name, None)
                one_ref["a loaded valence_core module whose file is outside the repo"] = (
                    or_ and "the import closure must be committed" in om_ and o_name in om_
                    and "is not a regular file in the repo" in om_ and not gd.exists() and o_name not in sys.modules)
                with mock.patch.object(_stages, "_committed", planted({**live, pk_only: other})):
                    br, bm = raised(lambda: write(None), GshapeRefusal)
                one_ref["a committed package blob not the working tree"] = (
                    br and "committed blobs hash to" in bm and not gd.exists())
                with mock.patch.object(_stages, "_committed", planted(live)):
                    sp_ok = sources_committed_problems()
                    pp_ok = committed_package()[0]
                    cl_ok, cl_map = committed_closure()
                    r_can, e_can = attempt(lambda: write(None))
        chk("gshape: the canonical run refuses unless every SCORING_STACK_FILES and TOOLING_FILES entry, every "
            "m package file (valence_core/m/*.py) and every import-closure file (F3) is committed at HEAD and "
            "unedited -- a scoring-stack file, gshape.py, m_sessions.py, stages.py (a package file listed "
            "nowhere else) or valence_core/stats.py (an import-closure file listed nowhere else) planted "
            "uncommitted, that closure file's working tree differing from HEAD, or a loaded valence_core "
            "module whose file is outside the repo: exit-2 refusal naming it, "
            "nothing written; a committed package blob that is not the working tree: refused (the package_sha256 "
            "recorded must hash the committed blobs); with every file planted committed (the working tree's "
            "bytes, so this passes before a commit whatever is edited) the closure check is clean and it writes "
            "GATES_DIR/G-SHAPE-F0.json (patched to a temp dir), the same artifact as the --out run (its import "
            "closure the committed blobs' sha256); a --out run does not check it",
            ref and "must be committed" in msg and nothing and sp_bad and SCORING_STACK_FILES[0] in sp_bad[0]
            and pk_only in pk_rels and pk_only not in SCORING_STACK_FILES + TOOLING_FILES
            and clo_only in clo_rels and clo_only not in SCORING_STACK_FILES + TOOLING_FILES + tuple(pk_rels)
            and len(one_ref) == 7 and all(one_ref.values())
            and sp_ok == [] and pp_ok == [] and cl_ok == [] and cl_map == clo_map
            and r_can is not None and r_can["how"] == "written"
            and r_can["canonical"] is True and r_can["path"] == gd / ARTIFACT_NAME and r_can["artifact"] == a
            and r_can["artifact"]["provenance"]["import_closure"] == clo_map
            and r_out is not None and r_out["how"] == "written" and r_out["artifact"] == a,
            (ref, msg[:80], len(sp_bad), one_ref), (e_can[:160], e_out[:160]))
        # V15: the canonical run's provenance summary line, word for word
        want_can = (f"G-SHAPE-F0 provenance: package sha256 {pkg}; sources digest {dig} (28 files); import closure "
                    f"digest {cdig} (14 files outside valence_core/m); sources committed at HEAD: yes (checked with "
                    f"every m package file and the import closure: canonical run, before scoring and again before "
                    f"the write)")
        got_can = summary_lines(r_can)[1] if r_can is not None else e_can
        chk("gshape: the canonical run's provenance summary line is, word for word, 'G-SHAPE-F0 provenance: package "
            "sha256 <pkg>; sources digest <digest> (28 files); import closure digest <digest> (14 files outside "
            "valence_core/m); sources committed at HEAD: yes (checked with every m package file and the import "
            "closure: canonical run, before scoring and again before the write)'",
            got_can == want_can, got_can[-140:])

    # --- 6b. the canonical run's provenance is the checked bytes; drift before the write refuses -----
    with sec("6b", 1):
        cur = live_bytes()                                 # every file planted committed
        flip = {"on": False}
        real_grid, real_pkg_of = grid, _resume.package_sha256_of

        def planted_live(rel, repo=REPO):
            return ([], cur[rel]) if rel in cur else real_committed(rel, repo)

        def grid_then(edit):
            def g(*args, **kw):
                out_ = real_grid(*args, **kw)
                edit()
                return out_
            return g

        def pkg_of(root):
            return "0" * 64 if flip["on"] else real_pkg_of(root)

        def edit_source():
            cur[SCORING_STACK_FILES[1]] = cur[SCORING_STACK_FILES[1]] + b"\n# drift (selftest)\n"

        def edit_pk_only():
            cur[pk_only] = cur[pk_only] + b"\n# drift (selftest)\n"

        def edit_package():
            flip["on"] = True

        def edit_closure():
            cur[clo_only] = cur[clo_only] + b"\n# drift (selftest)\n"

        late_name, late_rel = "valence_core.zz_gshape_selftest_late", "valence_core/discrim.py"
        out_name = "valence_core.zz_gshape_selftest_outside"

        def load_late():
            # a module loaded after the committed check (a repo file outside the closure), removed after
            late = types.ModuleType(late_name)
            late.__file__ = str(REPO / late_rel)
            sys.modules[late_name] = late

        drift_res = {}
        with tempfile.TemporaryDirectory(prefix="gshape_drift_") as td:
            outside = Path(td) / "outside.py"
            outside.write_text("# a module file outside the repo (selftest)\n", encoding="utf-8")

            def load_outside():
                # a valence_core module loaded after the check from a file outside the repo, removed after
                m_ = types.ModuleType(out_name)
                m_.__file__ = str(outside)
                sys.modules[out_name] = m_

            gd = Path(td) / "gates"
            with mock.patch.object(me, "GATES_DIR", gd), mock.patch.object(_stages, "_committed", planted_live), \
                    mock.patch.object(_resume, "package_sha256_of", pkg_of):
                for nm, edit, needle in (("a scoring-stack file edited after scoring", edit_source,
                                          SCORING_STACK_FILES[1]),
                                         ("a package-only file's committed blob changed after scoring", edit_pk_only,
                                          pk_only),
                                         ("an m package file edited after scoring", edit_package, "package_sha256"),
                                         ("an import-closure file's committed blob changed after scoring (F3)",
                                          edit_closure, clo_only),
                                         ("a module loaded after the precondition (F3)", load_late,
                                          f"{late_rel}: entered the import closure"),
                                         ("a module loaded after the precondition from outside the repo (F3)",
                                          load_outside, "is not a regular file in the repo")):
                    cur.update(live_bytes())
                    flip["on"] = False
                    try:
                        with mock.patch.object(me, "grid", grid_then(edit)):
                            dr, dm = raised(lambda: write(None), GshapeRefusal)
                    finally:
                        sys.modules.pop(late_name, None)
                        sys.modules.pop(out_name, None)
                    drift_res[nm] = (dr and "drifted between the precondition and the write" in dm and needle in dm
                                     and "is not recorded" in dm and not gd.exists(), dm[:160])
                drift_res["the planted late modules are gone again"] = (
                    late_name not in sys.modules and out_name not in sys.modules
                    and late_rel not in import_closure()[1] and import_closure()[0] == [], "")
                cur.update(live_bytes())
                flip["on"] = True                            # a package edited after import, before the check
                pr, pm = raised(lambda: write(None), GshapeRefusal)
                drift_res["the package re-hashes differently at the precondition"] = (
                    pr and "a file changed since import" in pm and not gd.exists(), pm[:120])
                flip["on"] = False
                blob = b"the checked committed blob (selftest)\n"
                cur[src_only] = blob                           # the map must carry the checked bytes' sha
                r_blob, e_blob = attempt(lambda: write(None))
                bp = need(r_blob, e_blob, "write(None) on a planted blob")["artifact"]["provenance"]
                drift_res["the sources map and its digest are the checked blobs"] = (
                    r_blob["how"] == "written"
                    and src_only not in pk_rels and bp["sources"][src_only] == _sha256(blob)
                    != a["provenance"]["sources"][src_only]
                    and bp["sources_digest"] == sources_digest({"sources": bp["sources"], "tooling": bp["tooling"]})
                    != a["provenance"]["sources_digest"]
                    and bp["package_sha256"] == pkg, r_blob["how"])
                cur.update(live_bytes())
                cblob = b"the checked committed closure blob (selftest)\n"
                cur[clo_only] = cblob                          # the closure map must carry it too (F3)
                gd2 = Path(td) / "gates2"
                with mock.patch.object(me, "GATES_DIR", gd2):
                    r_cb, e_cb = attempt(lambda: write(None))
                cbp = need(r_cb, e_cb, "write(None) on a planted closure blob")["artifact"]["provenance"]
                drift_res["the import closure map and its digest are the checked blobs (F3)"] = (
                    r_cb["how"] == "written" and r_cb["path"] == gd2 / ARTIFACT_NAME
                    and cbp["import_closure"][clo_only] == _sha256(cblob) != clo_map[clo_only]
                    and set(cbp["import_closure"]) == set(clo_rels)
                    and all(cbp["import_closure"][r] == clo_map[r] for r in clo_rels if r != clo_only)
                    and cbp["import_closure_digest"] == _json_sha256(cbp["import_closure"]) != cdig,
                    r_cb["how"])
        drift_bad = {k: v[1] for k, v in drift_res.items() if not v[0]}
        chk("gshape: the canonical run's provenance is bound to the bytes the committed check passed -- its "
            "sources map, sources digest, import closure and closure digest are those blobs' (a planted committed "
            "blob that differs from the working tree is what the artifact records) and its package_sha256 is "
            "taken at that check; a scoring-stack file, a package-only file, an m package file or an "
            "import-closure file that changes between the check and the write, a module loaded after the check "
            "(it enters the closure; or its file is outside the repo), or a package that re-hashes differently at "
            "the check, is an exit-2 refusal with nothing written",
            not drift_bad and len(drift_res) == 10, drift_bad)

    # --- 7. template shape ---------------------------------------------------------------------
    with sec("7", 1):
        muts = {"no bracketed header": "round {n} | config: {tag}\nTask: {task}\nResponse:",
                "the Task line not second": "[round {n} | config: {tag}]\nResponse:\nTask: {task}",
                "the tag missing": "[round {n} | config]\nTask: {task}\nResponse:",
                "the round number truncated to one digit (wrong at n = 10 only)":
                    "[round {n!s:.1} | config: {tag}]\nTask: {task}\nResponse:"}
        shape_bad = {}
        for nm, tpl in muts.items():
            tpls = list(ROUND_TEMPLATES)
            tpls[1] = tpl
            p = template_shape_problems(tpls, renders)
            x = evaluate(inputs=ins, templates=tpls, units=pair)
            if not p or "shape" not in x["stop_reasons"] or x["verdict"] != "STOP":
                shape_bad[nm] = (len(p), x["stop_reasons"])
            if nm.startswith("the round number truncated"):
                # placements carry n in 1..8; only the 1..10 template check sees n = 10
                if not all(" n=10:" in q for q in p) or any(x["grid"][u]["n_misplaced"] for u in pair):
                    shape_bad[nm] = (p[:2], [x["grid"][u]["n_misplaced"] for u in pair])
        nl = template_shape_problems(ROUND_TEMPLATES, ["Compute 1 +\n1."])
        real_placements = placements

        def clean_in_segment(unit, rs, pl_, *, templates=None):
            # item 4's clean task placed where its render belongs (selftest only, restored on exit)
            for x in real_placements(unit, rs, pl_, templates=templates):
                yield (dataclasses.replace(x, seg=x.seg.replace(x.render, pl_[x.i]["task"])) if x.i == 4 else x)

        with mock.patch.object(me, "placements", clean_in_segment):
            x_mis = evaluate(inputs=ins, units=pair)
        if (x_mis["stop_reasons"] != sorted(["shape"] + [f"coverage:{u}" for u in UNITS if u not in pair])
                or x_mis["template_shape"]["n_problems"] != 0
                or [x_mis["grid"][u]["n_misplaced"] for u in pair]
                != [N_BANNERS * N_TEMPLATES * len(pool[4]["gold"]) * len(PHASES)] * 2):
            shape_bad["the clean task placed for item 4's render"] = (
                x_mis["stop_reasons"], [x_mis["grid"][u]["n_misplaced"] for u in pair])
        chk("gshape: template shape -- ROUND_TEMPLATES at every n in 1..10, every render and every Q label is "
            "[bracketed round header ending ': {label}]', 'Task: ' + render, 'Response:']; a template without "
            "its bracketed header, with the Task line not second, or without the tag STOPs 'shape'; one whose "
            "round number is cut to one digit fails at n = 10 only (no placement carries n > 8: the 1..10 range "
            "is what sees it) and STOPs 'shape'; a render carrying a newline is a problem; a placement whose "
            "segment carries the clean task in its render's place STOPs 'shape' (checked as placed) while the "
            "template check stays clean",
            template_shape_problems() == [] and not shape_bad and nl != [] and len(muts) == 4, shape_bad)

    # --- 8. Layer S: [] on the sources; every scope mutation caught by its rule ------------------
    with sec("8", 2):
        src0 = _package_sources()
        RQ_, RO_, BN_ = "valence_core/m/runner_qwen.py", "valence_core/m/runner_olmo.py", "valence_core/m/banner.py"
        qsrc = src0[RQ_]
        ind = re.search(r"\n( *)earlier\.append\(g\.text\)", qsrc).group(1)
        free_cls = ('            ra = audit.classify(g.text, render=spec.task_text, item=spec.item, earlier=earlier,\n'
                    '                                own_pair=own, echo_lines=echo_lines, phase="free")')
        free_app = "            earlier.append(g.text)\n            if _audit.qwen_ends(ra):"
        free_gen = ("            g = adapter.generate(prefix, spec.seg, injections=(), seed=spec.seed, temp=temp,\n"
                    "                                 max_tokens=STOP_CAP, ban_ids=ban_ids, cached=path_cached)\n")
        s_muts = (
            ("prefix + g.text scored", RQ_, "audit.classify(g.text, render=", "audit.classify(prefix + g.text, render=", "R2"),
            ("spec.seg + g.text scored", RQ_, "audit.classify(g.text, render=", "audit.classify(spec.seg + g.text, render=", "R2"),
            ("the render scored", RQ_, "audit.classify(g.text, render=", "audit.classify(spec.task_text, render=", "R2"),
            ("render=spec.seg", RQ_, "render=spec.task_text", "render=spec.seg", "R4"),
            ("the render from sc.delivery.clean", RQ_, "render=spec.task_text", "render=sc.delivery.clean[spec.item]", "R4"),
            ("phase swapped", RQ_, None, None, "R3"),
            ("a third classify call", RQ_, f"\n{ind}earlier.append(g.text)",
             f"\n{ind}earlier.append(g.text)\n{ind}audit.classify(g.text, render=spec.task_text, item=spec.item, "
             f"earlier=earlier, own_pair=own, echo_lines=echo_lines, phase=\"forced\")", "R1"),
            ("one classify call removed", RO_, 'ra = audit.classify(g.text, own_pair=own, echo_lines=echo_lines, '
             'phase="free")', 'ra = audit.classify_(g.text, own_pair=own, echo_lines=echo_lines, phase="free")', "R1"),
            ("add_round passed another generation", RQ_, "log.add_round(spec, g, ra, term_rx)",
             "log.add_round(spec, cr, ra, term_rx)", "R6"),
            ("termination(spec.seg + g.text, ...) in add_round", SCAFFOLD_REL, '"termination": termination(g.text, term_rx)',
             '"termination": termination(spec.seg + g.text, term_rx)', "R7"),
            ("str(spec.seg + g.text) recorded", SCAFFOLD_REL, '"text": str(g.text)', '"text": str(spec.seg + g.text)', "R7"),
            ("earlier.append(spec.seg)", RQ_, "earlier.append(g.text)", "earlier.append(spec.seg)", "R4"),
            ("the Qwen runner on OLMo's echo set", RQ_, "_audit.qwen_echo_lines(sc.note_lines)",
             "_audit.olmo_echo_lines(sc.note_lines)", "R5"),
            ("OLMo: spec.seg + g.text scored", RO_, "audit.classify(g.text, own_pair=",
             "audit.classify(spec.seg + g.text, own_pair=", "R2"),
            ("a non-selftest classify call in another module", BN_, None, None, "R8"),
            # each Layer S sub-rule's own must-fail case (review: 14 sub-rules had none)
            ("the audit parameter rebound", RQ_, "    own = (sc.P, sc.Q)\n",
             "    own = (sc.P, sc.Q)\n    audit = _audit.QwenTaskRoundAudit\n", "R1"),
            ("the signature without term_rx", RO_, "                     term_rx: Sequence[str]) -> dict:",
             "                     term_rx_: Sequence[str]) -> dict:", "R1"),
            ("spec rebound between generate and classify", RQ_,
             "max_tokens=STOP_CAP, ban_ids=ban_ids, cached=path_cached)\n        ra = audit.classify(",
             "max_tokens=STOP_CAP, ban_ids=ban_ids, cached=path_cached)\n        spec = sc.forced(0)\n"
             "        ra = audit.classify(", "R2"),
            ("the scored generation bound outside its block", RQ_,
             ("    for ri in range(sc.n_forced):\n", "audit.classify(g.text, render="),
             ("    g0 = adapter.generate(log.transcript, sc.forced(0).seg, injections=(), seed=0)\n"
              "    for ri in range(sc.n_forced):\n", "audit.classify(g0.text, render="), "R2"),
            ("injections not ()", RQ_, "g = adapter.generate(prefix, spec.seg, injections=(), seed=spec.seed",
             "g = adapter.generate(prefix, spec.seg, injections=sc.inj, seed=spec.seed", "R2"),
            ("an extra classify keyword", RQ_, 'own_pair=own, echo_lines=echo_lines, phase="forced")',
             'own_pair=own, echo_lines=echo_lines, phase="forced", seg=spec.seg)', "R4"),
            ("item not spec.item", RQ_, "render=spec.task_text, item=spec.item, earlier=earlier,",
             "render=spec.task_text, item=0, earlier=earlier,", "R4"),
            ("earlier= not the session's list", RQ_, "item=spec.item, earlier=earlier,",
             "item=spec.item, earlier=[spec.seg],", "R4"),
            ("earlier seeded non-empty", RQ_, "earlier: list[str] = []", "earlier: list[str] = [sc.banner]", "R4"),
            ("earlier.insert(0, spec.seg)", RQ_, f"\n{ind}earlier.append(g.text)\n",
             f"\n{ind}earlier.append(g.text)\n{ind}earlier.insert(0, spec.seg)\n", "R4"),
            ("a round's text appended before its own classify (free)", RQ_, (free_cls, free_app),
             ("            earlier.append(g.text)\n" + free_cls, "            if _audit.qwen_ends(ra):"), "R4"),
            ("a round's text appended twice (free)", RQ_, free_app,
             "            earlier.append(g.text)\n" + free_app, "R4"),
            # the R4 order rule's three parts, each killed on its own (re-verification round 1, V11-V13)
            ("g rebound between the free classify and its append (a regeneration)", RQ_, free_app,
             free_gen + free_app, "R4"),
            ("the free round's generation under a second name, the append left on g", RQ_,
             (free_gen.split("\n", 1)[0], free_cls, "            log.add_round(spec, g, ra, term_rx)\n"),
             (free_gen.split("\n", 1)[0].replace(" g = ", " g2 = ", 1), free_cls.replace("(g.text,", "(g2.text,", 1),
              "            log.add_round(spec, g2, ra, term_rx)\n"), "R4"),
            ("the forced round's append removed", RQ_, f"\n{ind}earlier.append(g.text)\n{ind}if _audit.qwen_ends(ra):",
             f"\n{ind}if _audit.qwen_ends(ra):", "R4"),
            ("own bound as (Q, P)", RQ_, "own = (sc.P, sc.Q)", "own = (sc.Q, sc.P)", "R5"),
            ("the log on the other substrate", RQ_, '_sc.SessionLog(sc, "qwen")', '_sc.SessionLog(sc, "olmo")', "R6"),
            ("the audit recorded not ra.as_dict()", SCAFFOLD_REL, '"audit": ra.as_dict(),', '"audit": {},', "R7"),
            ("r['text'] rewritten after the literal", SCAFFOLD_REL, "        self.rounds.append(r)\n        if ra.claim",
             '        r["text"] = spec.task_text + r["text"]\n        self.rounds.append(r)\n        if ra.claim', "R7"),
            ("a copy appended, not r", SCAFFOLD_REL, "        self.rounds.append(r)\n        if ra.claim",
             '        self.rounds.append({**r, "text": spec.task_text})\n        if ra.claim', "R7"),
            ("the round never appended", SCAFFOLD_REL, "        self.rounds.append(r)\n        if ra.claim",
             "        if ra.claim", "R7"),
            ("g rebound in add_round", SCAFFOLD_REL,
             "    def add_round(self, spec: RoundSpec, g, ra, term_rx: Sequence[str]) -> dict:\n",
             "    def add_round(self, spec: RoundSpec, g, ra, term_rx: Sequence[str]) -> dict:\n        g = spec\n", "R7"),
            # R7 beyond the literal (review: rewrites by method call, or from another SessionLog method)
            ("r.update(...) rewrites the termination", SCAFFOLD_REL, "        self.rounds.append(r)\n        if ra.claim",
             "        r.update(termination=termination(spec.seg + g.text, term_rx))\n        self.rounds.append(r)\n"
             "        if ra.claim", "R7"),
            ("r.__setitem__ rewrites the text", SCAFFOLD_REL, "        self.rounds.append(r)\n        if ra.claim",
             '        r.__setitem__("text", spec.seg + r["text"])\n        self.rounds.append(r)\n        if ra.claim', "R7"),
            ("record() rewrites every round's text", SCAFFOLD_REL,
             "        sc = self.sc\n        forced = [r for r in self.rounds",
             '        sc = self.sc\n        for r0 in self.rounds:\n            r0["text"] = sc.banner + r0["text"]\n'
             "        forced = [r for r in self.rounds", "R7"),
            ("record() updates a round by index", SCAFFOLD_REL,
             "        sc = self.sc\n        forced = [r for r in self.rounds",
             "        sc = self.sc\n        for i in range(len(self.rounds)):\n            self.rounds[i].update("
             "termination=False)\n        forced = [r for r in self.rounds", "R7"))
        ls0 = runner_scope_problems(src0)
        caught, s_bad = 0, {}
        for nm, rel, old, new, rule in s_muts:
            text = src0[rel]
            if nm == "phase swapped":
                mt = (text.replace('phase="forced")', 'phase="@@")').replace('phase="free")', 'phase="forced")')
                      .replace('phase="@@")', 'phase="free")'))
            elif nm.startswith("a non-selftest classify"):
                mt = text + "\n\ndef _smuggled(stack, text):\n    return stack.classify(text)\n"
            else:
                mt = text
                for o_, n_ in (zip(old, new) if isinstance(old, tuple) else [(old, new)]):
                    if o_ not in mt:
                        mt = text
                        break
                    mt = mt.replace(o_, n_, 1)
            if mt == text:
                s_bad[nm] = "mutation not applicable"
                continue
            try:
                p = runner_scope_problems({**src0, rel: mt})["problems"]
            except Exception as e:                       # noqa: BLE001 -- a crash is not a catch
                s_bad[nm] = f"raised {type(e).__name__}: {e}"
                continue
            if p and any(x.startswith(rule + " ") for x in p):
                caught += 1
            else:
                s_bad[nm] = p[:2]
        by_rule = Counter(m[4] for m in s_muts)
        chk(f"gshape: Layer S (static runner scope, R1-R8) is [] on the package sources; each of {len(s_muts)} "
            "scope mutations is caught by its rule ("
            + ", ".join(f"{r} x{by_rule[r]}" for r in LAYER_S_RULES) + "): prefix/segment/render scored, "
            "render=seg or clean, phases swapped, a third or a missing classify call, another generation "
            "recorded, termination or text of seg + text in add_round, earlier fed the segment, the other "
            "substrate's echo set, OLMo scoring seg + text, a classify call smuggled into another module; and "
            "one per sub-rule: the audit parameter rebound, the signature, spec rebound between generate and "
            "classify, the scored generation bound outside its block (reported, never a crash), injections, the "
            "exact keyword set, item, earlier= / its empty binding / its uses, a round's text appended before "
            "its own classify or twice, and each part of the R4 order rule on its own (g rebound between the "
            "classify and its append; the free generation under a second name with the append left on g; the "
            "forced append removed), own, the log, the recorded audit, r rewritten / copied / never appended "
            "/ updated / set after its literal, g rebound, "
            "and record() rewriting rounds by loop or by index",
            ls0["problems"] == [] and caught == len(s_muts) == 41 and not s_bad
            and all(by_rule[r] for r in LAYER_S_RULES)
            and set(ls0["files"]) == {RQ_, RO_, SCAFFOLD_REL}, s_bad or caught)
        bad_src = {**src0, RQ_: qsrc.replace("audit.classify(g.text, render=", "audit.classify(spec.seg + g.text, render=",
                                             1)}
        x_ls = evaluate(inputs=ins, units=one, sources=bad_src)
        x_ls0 = evaluate(inputs=ins, units=one, sources=src0)
        left3 = [f"coverage:{u}" for u in UNITS if u not in one]
        chk("gshape: a Layer S problem reaches the verdict -- evaluate on a runner source that scores spec.seg + "
            "g.text STOPs 'scope-static' (Q-F0 scored; the three units left out STOP coverage, nothing else); "
            "the same evaluate on the package sources does not carry it",
            x_ls["verdict"] == "STOP" and x_ls["stop_reasons"] == sorted(["scope-static"] + left3)
            and any(q.startswith("R2 ") for q in x_ls["layer_s"]["problems"])
            and x_ls0["stop_reasons"] == sorted(left3) and x_ls0["layer_s"]["problems"] == [],
            (x_ls["stop_reasons"], x_ls0["stop_reasons"]))

    # --- 9. the one dynamic check: the runners hand classify the generation's text ---------------
    with sec("9", 1):
        kq, ko = testing.qwen_kit(), testing.olmo_kit()

        class _RecQwen(_audit.QwenTaskRoundAudit):
            def __init__(self, base, log):
                super().__init__(base.audit3, pool, base.scaffold_strings)
                self.calls = log

            def classify(self, text, **kw):
                self.calls.append((text, {**kw, "earlier": tuple(kw.get("earlier", ()))}))
                return super().classify(text, **kw)

        class _RecOLMo(_audit.OLMoTaskRoundAudit):
            def __init__(self, log):
                super().__init__()
                self.calls = log

            def classify(self, text, **kw):
                self.calls.append((text, dict(kw)))
                return super().classify(text, **kw)

        def identity_problems(mod, sub, case) -> tuple[list[str], int]:
            unit = testing.QWEN_UNIT if sub == "qwen" else testing.OLMO_UNIT
            tpl = testing.case_template(sub, case.contrast)
            sc = _sc.m_config(unit, testing.STAGE, tpl, case.s, testing.case_cell(sub, tpl, case.s), "uncached",
                              pool=pool, renders=renders)
            ad = testing.ScriptedAdapter() if sub == "qwen" else testing.OLMoScriptedAdapter()
            script = testing.script_for(case, sc.P, sc.Q, sc.note_lines)
            ad.load(script, testing.plan_picks(case.picks, sc.P, sc.Q)[0])
            log: list = []
            if sub == "qwen":
                rec = mod.run_session_qwen(ad, sc, _RecQwen(kq.audit, log), kq.ban_ids, path_cached=False,
                                           term_rx=kq.term_rx)
                el, want_kw = _audit.qwen_echo_lines(sc.note_lines), {"render", "item", "earlier", "own_pair",
                                                                      "echo_lines", "phase"}
            else:
                rec = mod.run_session_olmo(ad, sc, _RecOLMo(log), ko["ban_ids"], term_rx=ko["term_rx"])
                el, want_kw = _audit.olmo_echo_lines(sc.note_lines), {"own_pair", "echo_lines", "phase"}
            rounds = rec["rounds"]
            probs = [] if len(log) == len(rounds) == len(ad.calls) else [f"{case.name}: call counts differ"]
            for j, ((text, kw), r, call) in enumerate(zip(log, rounds, ad.calls)):
                seg = call["segment"]
                lines = seg.split("\n")
                task = lines[1][len("Task: "):] if len(lines) == 3 and lines[1].startswith("Task: ") else None
                if not (text == script[j] == r["text"]) or seg in text or rec["banner"] in text:
                    probs.append(f"{case.name} round {j}: the scored text is not the generation's")
                if (set(kw) != want_kw or kw.get("phase") != r["phase"] or tuple(kw.get("own_pair", ())) != (sc.P, sc.Q)
                        or tuple(kw.get("echo_lines", ())) != tuple(el)):
                    probs.append(f"{case.name} round {j}: classify's session arguments differ")
                if sub == "qwen" and not (kw.get("render") == task == r["task_text"] and kw.get("item") == r["item"]
                                          and kw.get("earlier") == tuple(script[:j])):
                    probs.append(f"{case.name} round {j}: render / item / earlier are not the round's")
            return probs, len(rounds)

        real_probs, n_sess, n_rounds = [], 0, 0
        for sub, mod, cases in (("qwen", _rq, testing.CASES_QWEN), ("olmo", _ro, testing.CASES_OLMO)):
            for c in cases:
                p, nr = identity_problems(mod, sub, c)
                real_probs += p
                n_sess += 1
                n_rounds += nr
        r_muts = (("qwen", _rq, "audit.classify(g.text, render=", "audit.classify(spec.seg + g.text, render="),
                  ("qwen", _rq, "audit.classify(g.text, render=", "audit.classify(log.transcript + g.text, render="),
                  ("qwen", _rq, "audit.classify(g.text, render=", "audit.classify(spec.task_text, render="),
                  ("qwen", _rq, "render=spec.task_text", "render=sc.delivery.clean[spec.item]"),
                  ("olmo", _ro, "audit.classify(g.text, own_pair=", "audit.classify(spec.seg + g.text, own_pair="),
                  ("olmo", _ro, "audit.classify(g.text, own_pair=", "audit.classify(spec.task_text, own_pair="))
        r_caught = []
        for sub, mod, old, new in r_muts:
            mm = _mutated_module(mod, old, new)
            if mm is None:
                r_caught.append(False)
                continue
            case = (testing.CASES_QWEN if sub == "qwen" else testing.CASES_OLMO)[0]    # a contrast clean case
            try:
                p, _ = identity_problems(mm, sub, case)
            except (Exception, SystemExit) as e:          # noqa: BLE001 -- a crash is not a catch
                r_caught.append(f"raised {type(e).__name__}")
                continue
            r_caught.append(bool(p) and case.contrast)
        chk(RUNNER_IDENTITY_CHECK,
            real_probs == [] and n_sess == len(testing.CASES_QWEN) + len(testing.CASES_OLMO)
            and n_rounds > 200 and r_caught == [True] * len(r_muts) and len(r_muts) == 6,
            (n_sess, n_rounds, r_caught), real_probs[:2])

    # --- 10. the cited runner self-test checks exist by name -------------------------------------
    with sec("10", 1):
        names = {m: _chk_name_templates((PACKAGE_DIR / f"{m}.py").read_text(encoding="utf-8"))
                 for m in ("runner_qwen", "runner_olmo")}
        missing = [c[:60] for m, _, c in RUNNER_DYNAMIC_EVIDENCE if c not in names[m]]
        missing += [c[:60] for m, c in RUNNER_NOT_EVIDENCE if c not in names[m]]
        altered = RUNNER_DYNAMIC_EVIDENCE[0][2].replace("declared outcomes", "outcomes")
        cited = {c for _, _, c in RUNNER_DYNAMIC_EVIDENCE}
        kinds = Counter(k for _, k, _ in RUNNER_DYNAMIC_EVIDENCE)
        chk(f"gshape: the {len(RUNNER_DYNAMIC_EVIDENCE)} runner self-test checks the artifact cites as the dynamic "
            "evidence are chk names in runner_qwen / runner_olmo (an f-string count as '{}'), each labelled with "
            "what it contains (4 classify outcomes, 2 render placed in situ); the 2 generation-side context checks "
            "(adapter calls; menus and pick lines) exist and are not cited; a one-word-altered citation is not found",
            not missing and len(RUNNER_DYNAMIC_EVIDENCE) == 6 and altered not in names["runner_qwen"]
            and kinds == Counter({"classify outcomes": 4, "render placed in situ": 2})
            and set(kinds) == set(RUNNER_EVIDENCE_KINDS) and not cited & {c for _, c in RUNNER_NOT_EVIDENCE}
            and [x["check"] for x in a["runner_dynamic_evidence"]["existing_checks"]]
            == [c for _, _, c in RUNNER_DYNAMIC_EVIDENCE]
            and a["runner_dynamic_evidence"]["gshape_check"] == RUNNER_IDENTITY_CHECK, missing)

    # --- 11. OLMo's string half; the governing text -----------------------------------------
    with sec("11", 2):
        strings, b3 = _olmo_files()
        sp = olmo_scaffold_string_problems(strings)
        sp_mut = olmo_scaffold_string_problems({**strings, "dpo": strings["dpo"][:-1] + ["<|pad|> "]})
        sp_less = olmo_scaffold_string_problems({k: v for k, v in strings.items() if k != "instruct"})
        chk("gshape: OLMo's string half -- all three scaffold_{ckpt}.json carry OLMo's six strings and every "
            "b3_screen ban_list is {n_ids 9, sha16 2dd86a453a2275ef} (recorded, not exercised: the ids are the "
            "box's); a mutated string list and a missing checkpoint are detected",
            sp == [] and all(v == B3_BAN_LIST for v in b3.values()) and len(b3) == 3 and sp_mut and sp_less,
            (sp, sp_mut[:1]))
        ptext = prop0.decode("utf-8")
        chk("gshape: the governing text -- CRITERION is verbatim in the proposal's one CRITERION_HEAD line (m:277); "
            "a one-word-mutated line and a doubled head line are detected",
            criterion_problems(ptext) == [] and criterion_problems(prop_bad.decode("utf-8")) != []
            and criterion_problems(ptext + "\n" + CRITERION_HEAD + " x\n") != [] and word in CRITERION)

    # --- 11b. every PIN-S reading kept by the decisions is declared in code -------------------------
    with sec("11b", 2):
        msrc = Path(__file__).read_text(encoding="utf-8")
        decl = _pin_s_declarations(msrc)
        s4 = " ".join(decl.get(4, []))
        s4_needles = ("each substrate's own stack as its startup builds it", "assert_qwen_scaffold",
                      "termination counter and the end rules", "No cross-substrate placement", "recorded, not exercised")
        s9 = " ".join(decl.get(9, []))
        s9_needles = ("write-once", "no timestamp, no HEAD", "Supersession is by hand only", "seat's ruling",
                      "``git mv``", "dated superseded name")
        gone = _pin_s_declarations(msrc.replace("No\n# cross-substrate placement", "Nothing\n# else"))
        gone9 = _pin_s_declarations(msrc.replace("Supersession is by hand only, on\n", "Nothing else, on\n"))
        chk("gshape: every PIN-S reading Code's decisions keep (S1-S10; S11 dropped with Layer B, S12 replaced by "
            "the driver's MODULES check) is declared in a '# PIN (Code, declared at LOCK v0.1; PIN-Sk...' comment "
            "or docstring here; PIN-S4's declaration carries its own-stack reading, the Qwen scaffold assertion, "
            "the termination counter and end rules on both substrates, the recorded-not-exercised OLMo ban ids "
            "and 'No cross-substrate placement'; PIN-S9's carries write-once, no timestamp or HEAD, and "
            "supersession by hand (git mv to a dated superseded name) on the seat's ruling only (decisions item "
            "7); a copy without either sentence is detected",
            sorted(decl) == list(range(1, 11)) and all(n in s4 for n in s4_needles) and all(n in s9 for n in s9_needles)
            and "No cross-substrate placement" not in " ".join(gone.get(4, []))
            and "Supersession is by hand only" not in " ".join(gone9.get(9, [])),
            sorted(decl), [n for n in s4_needles + s9_needles if n not in s4 + " " + s9])
        prov_head = "gshape: provenance of this self-test"
        notes = _chk_note_templates(msrc, prov_head)
        cut = ('f"package_sha256 {' + 'pkg}", f"sources_digest {' + 'dig}", f"import_closure_digest {'
               + 'cdig}")')
        notes_cut = _chk_note_templates(msrc.replace(cut, '"", "", "")', 1), prov_head) if cut in msrc else None
        chk("gshape: decisions item 5 -- the provenance check above prints package_sha256, the sources digest and "
            "the import-closure digest in its note (its chk call's note arguments, read from this module's "
            "source, are f'package_sha256 {pkg}', f'sources_digest {dig}' and f'import_closure_digest {cdig}'), "
            "so a run of record pairs with a self-test pass from the raws alone; a copy with those notes blanked "
            "is detected",
            notes == [["package_sha256 {pkg}", "sources_digest {dig}", "import_closure_digest {cdig}"]]
            and notes_cut == [["", "", ""]], notes, notes_cut)

    # --- 12. write-once and the canonical path -------------------------------------------------
    with sec("12", 1):
        with tempfile.TemporaryDirectory(prefix="gshape_once_") as td:
            d1, d2, d3 = Path(td) / "a", Path(td) / "b", Path(td) / "c"
            canon_tmp = Path(td) / "canon"
            d1.mkdir()
            (d1 / ARTIFACT_NAME).write_text("{}\n", encoding="utf-8")
            w_diff = raised(lambda: write(d1), GshapeRefusal)
            untouched = (d1 / ARTIFACT_NAME).read_text(encoding="utf-8") == "{}\n"
            d2.mkdir()
            (d2 / ARTIFACT_NAME).symlink_to(Path(td) / "elsewhere.json")
            w_link = raised(lambda: write(d2), GshapeRefusal)
            no_target = not (Path(td) / "elsewhere.json").exists()
            # the must-refuse cases run with the write replaced by a sentinel and the canonical
            # directory pointed at a temp dir: a regression there is a FAIL, never a real write
            with mock.patch.object(me, "_write_once_text", no_write), mock.patch.object(me, "GATES_DIR", canon_tmp):
                w_canon = raised(lambda: write(REPO / "data" / "m" / "gates"), GshapeRefusal)
                w_empty = raised(lambda: write("  "), GshapeRefusal)
                w_seam = raised(lambda: write(None, scorer=_gold), GshapeRefusal)
                w_unknown = raised(lambda: write(d3, nonesuch=1), TypeError)
            sentinel_ok = reached == [] and not canon_tmp.exists()
            r_stop, e_stop = attempt(lambda: write(d3, scorer=lambda pl: pl.seg + pl.gold, units=(UNITS[0],)))
            w_stop_diff = raised(lambda: write(d3), GshapeRefusal)
            # a symlink at the temp name: write() refuses before evaluating; _write_once_text's
            # O_NOFOLLOW open refuses it too (a link planted after write's check); the target is
            # untouched and no artifact is written either way; a stale regular temp file is replaced
            d4, d5, d6 = Path(td) / "d", Path(td) / "e", Path(td) / "f"
            victim = Path(td) / "victim.json"
            victim.write_text("victim\n", encoding="utf-8")
            for d_ in (d4, d5, d6):
                d_.mkdir()
            _tmp_path(d4 / ARTIFACT_NAME).symlink_to(victim)
            w_tmp = raised(lambda: write(d4), GshapeRefusal)
            _tmp_path(d5 / ARTIFACT_NAME).symlink_to(victim)
            w_tmp2 = raised(lambda: _write_once_text(d5 / ARTIFACT_NAME, "{}\n"), GshapeRefusal)
            tmp_ok = (w_tmp[0] and "temp name" in w_tmp[1] and w_tmp2[0] and "without following a link" in w_tmp2[1]
                      and victim.read_text(encoding="utf-8") == "victim\n"
                      and not (d4 / ARTIFACT_NAME).exists() and not (d5 / ARTIFACT_NAME).exists()
                      and _tmp_path(d4 / ARTIFACT_NAME).is_symlink() and _tmp_path(d5 / ARTIFACT_NAME).is_symlink())
            _tmp_path(d6 / ARTIFACT_NAME).write_text("stale", encoding="utf-8")
            stale_w, stale_e = attempt(lambda: _write_once_text(d6 / ARTIFACT_NAME, "{}\n"))
            stale_ok = (stale_w == "written" and (d6 / ARTIFACT_NAME).read_text(encoding="utf-8") == "{}\n"
                        and not _tmp_path(d6 / ARTIFACT_NAME).exists())
        chk("gshape: write-once -- a different file at the path is refused and left untouched; a symlink at the "
            "path is refused (nothing written through it); a symlink at the temp name G-SHAPE-F0.json.tmp is "
            "refused before evaluating, and the temp open (O_NOFOLLOW) refuses one planted past that check -- "
            "the link's target untouched, no artifact; a stale regular temp file is replaced; --out under "
            "data/m, an empty --out (write's own refusal), a seamed run with no --out and an unknown seam are "
            "refused with the write replaced by a sentinel and GATES_DIR a temp dir (none reaches it); a STOP "
            "verdict is written with its evidence, and a different run against it is refused with 'not recorded'",
            w_diff[0] and "never overwritten" in w_diff[1] and untouched and w_link[0] and no_target
            and tmp_ok and stale_ok and sentinel_ok
            and w_canon[0] and "SELFTEST REFUSED" in w_canon[1] and w_empty[0] and "an empty --out is refused" in w_empty[1]
            and w_seam[0] and "seamed run" in w_seam[1] and w_unknown[0] and r_stop is not None
            and r_stop["how"] == "written" and r_stop["artifact"]["verdict"] == "STOP" and w_stop_diff[0]
            and "verdict PASS is not recorded" in w_stop_diff[1],
            (w_diff[0], w_link[0], tmp_ok, stale_ok, sentinel_ok, w_canon[0], w_empty[0], w_seam[0], w_unknown[0]),
            (w_tmp[1][:90], w_tmp2[1][:90], e_stop[:90], stale_e[:90], reached[:2]))

    # --- 12b. F1: after the build commit too, no regression reaches the real data/m/gates ---------
    with sec("12b", 1):
        # the post-commit state simulated as the verifier's postcommit_probe.py does -- every file the
        # canonical committed check reads (scoring stack, tooling, m package, import closure) reported
        # committed with the working tree's bytes; no git writes -- and planted write-to-canonical
        # regressions: copies of this module loaded here, whose write() ignores --out (the verifier's
        # V17) or is hard-coded to a directory under a protected root
        site = "        canonical = False\n    path = d / ARTIFACT_NAME"
        v17 = _mutated_module(me, site, "        canonical = False\n    d, canonical = Path(GATES_DIR), True\n"
                                        "    path = d / ARTIFACT_NAME")
        hard = _mutated_module(me, site, "        canonical = False\n    d, canonical = Path(_SELFTEST_DECOY), "
                                         "True\n    path = d / ARTIFACT_NAME")
        real_before = canonical_snapshot(real_gates)
        pc: dict = {"the two regression copies were built": (v17 is not None and hard is not None, "")}
        with tempfile.TemporaryDirectory(prefix="gshape_postcommit_") as td:
            out_pc, decoy, decoy2 = Path(td) / "out", Path(td) / "decoy_root", Path(td) / "decoy_root2"
            with mock.patch.object(_stages, "_committed", planted(live_bytes())):
                # a module copy loaded inside the self-test inherits the sandbox's GATES_DIR (guard.GATES_DIR
                # is patched too), so V17's canonical write lands there: the real directory is never reached
                inherits = v17 is not None and Path(v17.GATES_DIR) == sandbox_gates != real_gates
                r17, e17 = (attempt(lambda: v17.write(out_pc, units=one)) if inherits   # never run unsandboxed
                            else (None, "not run: the copy does not inherit the sandbox's GATES_DIR"))
                pc["V17 (write ignores --out), post-commit: written to the sandbox's GATES_DIR, not --out"] = (
                    inherits and r17 is not None and r17["canonical"] is True and r17["how"] == "written"
                    and r17["path"] == sandbox_gates / ARTIFACT_NAME and (sandbox_gates / ARTIFACT_NAME).is_file()
                    and not (out_pc / ARTIFACT_NAME).exists(), e17[:160])
                if hard is not None:
                    hard._SELFTEST_DECOY = decoy / "gates"
                with _selftest_sandbox(hard, roots=(decoy,)) as canon_h:
                    rh, eh = attempt(lambda: hard.write(out_pc, units=one))
                    pc["a write hard-coded under a protected root, post-commit: refused by the tripwire"] = (
                        rh is None and "selftest sandbox: a write under a canonical root" in eh
                        and not (decoy / "gates" / ARTIFACT_NAME).exists() and not canon_h.exists()
                        and not (out_pc / ARTIFACT_NAME).exists(), eh[:160])
            # the default roots are read from resume.CANONICAL_ROOTS (a decoy planted there: refused)
            with mock.patch.object(_resume, "CANONICAL_ROOTS", (decoy2,)), _selftest_sandbox():
                tw, tm = raised(lambda: me._write_once_text(decoy2 / "gates" / ARTIFACT_NAME, "{}\n"), GshapeRefusal)
            pc["the default tripwire roots are resume.CANONICAL_ROOTS, data/m among them"] = (
                tw and "selftest sandbox" in tm and not (decoy2 / "gates").exists()
                and (REPO / "data" / "m").resolve() in {Path(r).resolve() for r in _resume.CANONICAL_ROOTS}, tm[:120])
        landed = sandbox_gates / ARTIFACT_NAME
        if landed.is_file() and not landed.is_symlink():
            landed.unlink()                              # the outer sandbox left as check 1 found it
        pc["the real data/m/gates G-SHAPE paths unchanged (bytes or absence)"] = (
            _gcal.snapshot_changes(real_before, canonical_snapshot(real_gates)) == [] and not landed.exists(), "")
        pc_bad = {k: v[1] for k, v in pc.items() if not v[0]}
        chk("gshape: F1 -- with the post-commit state simulated (every file of the canonical committed check, the "
            "import closure included, reported committed with the working tree's bytes, as postcommit_probe.py "
            "does; no git writes), a planted write-to-canonical regression (a copy of this module whose write() "
            "ignores --out, V17) loaded inside the self-test writes the sandbox's GATES_DIR (it inherits it through "
            "guard.GATES_DIR), not --out and not the real data/m/gates; a copy hard-coded under a protected root "
            "is refused by the sandbox's tripwire (a decoy root here; the default roots are resume.CANONICAL_ROOTS, "
            "data/m among them); the real G-SHAPE paths are byte-identical before and after",
            not pc_bad and len(pc) == 5, pc_bad)

    # --- 13. imports, insulation, and the canonical paths untouched -----------------------------
    with sec("13", 2):
        heavy = sorted(m for m in sys.modules if m.split(".")[0] in ("torch", "mlx", "mlx_lm", "transformers"))
        try:
            guard.assert_insulated()
            insulated = True
        except SystemExit:
            insulated = False
        chk("gshape: no torch, mlx, mlx_lm or transformers module is loaded and guard.assert_insulated() holds "
            "(the gate is model-free)", not heavy and insulated, heavy[:3])
        chk("gshape: this self-test left every canonical G-SHAPE path under data/m/gates as it found it (bytes "
            "or absence, snapshotted before and compared after)",
            _gcal.snapshot_changes(snap0, canonical_snapshot(real_gates)) == [],
            _gcal.snapshot_changes(snap0, canonical_snapshot(real_gates)))
