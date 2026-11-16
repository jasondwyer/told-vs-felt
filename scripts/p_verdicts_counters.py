#!/usr/bin/env python3
"""PROPOSAL-p's counters at VERDICTS -- Code's own step (the seat's answers of 2026-11-16, §3 and §4).

THE RULING. The seat's answers of 2026-11-16 (results/raw/2026-11-16_p-verdicts-decisions_design-to-code_answers.md,
sha256 01ae2ae7a06574cf6d000e32ba86972425d2b86ec0b972ccb0715d5e5d701b0f, committed at 18102d0), routed by the PI's
"Route as given" on the paste block of 2026-11-16, section B, items 3 and 4. §3, verbatim: "the script imports p's
counter definitions and the frozen key table unchanged and adds no definition of its own; it is committed, with a
self-test that reproduces G-F0m-OLMo (p)'s committed sham figures from the reads files (159/160, 159/160, 160/160),
before it reads any released record. Its stdout is committed in a raw, and each VERDICTS entry reports its counts
beside the analyzer's outputs." §4, verbatim: "Code's step then reads each unit's three checkpoints by path, never
listing `data/p/ckpt`, for the counts the record names and nothing beyond them."

THE SECOND RULING. The seat's answers of 2026-11-16, second sitting, on this script's readings R1 and R2
(results/raw/2026-11-16_p-verdicts-counters_design-to-code_answers.md, sha256
aea918c5f6f374522ad780ce29685c8c3f950b7457a46933022c090e74680395), routed by the PI's "Route as given", section B,
items 1-3: R1 (c), every stage, and R2 (b), computed (RULING_R1 and RULING_R2 below, verbatim from its §0, each
asserted a substring of the raw by the self-test). Its §2.2 amends the briefs: "each unit's three checkpoints and three
call logs".

WHAT IT IMPORTS, UNCHANGED.
  - p §2.3's predicates, from valence_core/p/report.py: ``line_break_in_stored_text`` (the hair trigger),
    ``control_chars``, ``harness_first_line``, ``refusal`` and ``corrupted_spelling`` (with ``clean_task_words`` and the
    pinned lexicon, ``load_lexicon``), the counter names ``COUNTERS``, the round key ``round_key`` and
    ``session_counters`` itself, the tabulation p's stage reports ran (valence_core/p/stage.py:966, with m's pool,
    ``corr.load_pool()``).
  - p's renders of record (``valence_core.p.corrupt.RENDERS_OF_RECORD``), to tie a corrupted round to its item.
  - task_correct's key table and match rule: the script ``task_correct.py`` (sha256 9aa0e2d9…), committed verbatim
    inside results/raw/2026-11-11_p-qual_task-correct.txt (sha256 57e9c7dc…, committed at a225a89) after its header
    line. It is loaded from the raw's bytes as a module, both sha256s checked, and never copied: KEYS, MATCH_RULE,
    READING, SHAM_BLINDING, correct, load_pool, key_table, task_of, tally_file, selftest.
  - m's checkpoint reader (``resume.read_checkpoint``) and the act of release (``readrule.release_full``, m:271).
  - p's call-log functions (valence_core/p/stage.py): ``read_calls``, ``log_consistency_problems`` and
    ``attribute_calls`` (R2 (b): "applies p's `attribute_calls` unchanged"), with ``CALLS_SCHEMA``, ``label`` and
    ``text_sha256`` for the self-test's synthetic logs.
  The packages are the lock's: p's package_sha256 and m's package_sha256 are asserted equal to the values every
  LOCK-p-OLMo-{ckpt} v1.0 names (§8.1), before any count.

WHAT IT ADDS: no definition. It applies the imported predicates to every recorded round of every recorded session of
a stage, by arm (sham, contrast) and phase (forced, free) -- p §2.3's "tabulated over every generation of every p
stage" -- and the imported key table and match rule to the rounds the record names for ``task_correct``.

WHAT THE RECORD NAMES (the rulings applied).
  - p §2.3: the hair trigger and the five counters, over every recorded round of every recorded session of
    G-TIME-OLMo (p), G-F0m-OLMo (p) and the campaign, per unit. Each stage report carried the read domain; the rest was
    "withheld to the unit's VERDICTS ... recomputable from the checkpoint" (``report.WITHHELD``). This step recomputes
    the read domain two ways -- p's own ``session_counters`` over the released records, and this step's table -- and
    asserts both equal to the committed p report built from the same checkpoint; it then reports the withheld cells.
  - ``task_correct`` (the seat's answers of 2026-11-09, results/raw/2026-11-09_p-gtime_design-to-code_answers.md:34;
    its domain, R1 (c)): every recorded round of every recorded session of the unit's three stages, sham and contrast,
    forced and free (``TC_STAGES``). The gate stages' sham rows are recounted and asserted against their committed
    figures (``COMMITTED_SHAM_TC``; ``TC_ASSERTED``); the campaign's sham row has no committed figure, and it is
    counted and printed with no assertion, pass 1's other checks on the campaign checkpoints standing.
  - The proxy's counts over the contrast sessions (R2 (b)): each stage's call log by exact path
    (data/p/ckpt/OLMo-{ckpt}_{time,qual,campaign}_p-calls.jsonl), read by p's ``read_calls``, checked by p's
    ``log_consistency_problems``, attributed by p's ``attribute_calls`` unchanged; for each arm the cells p's report
    gives the sham arm (rounds, attributed, cuts and their round keys, unattributed round keys), and per contrast
    session the number of calls attributed to its rounds. The sham arm's cells are asserted equal to the committed p
    report's. The STOP marks in the p report's run rows are printed (none, on an intact record); a STOP's message,
    where one exists, is the stage entry's verbatim quote (the seat's ruling (c) of 2026-11-09), never the log's.
    CODE'S READING, for the seat: a contrast round with no attributed call is printed (its key among the unattributed,
    its session's count short), as the sham arm's cells print one, rather than STOPped; with the log bound to its
    report by sha256, it can arise only from a call line the log lost.

WHAT IT READS.
  - ``--selftest``: the raw above, data/f/pools.json, data/p/lexicon/web2.txt, the qual and time reads files' sham
    records (data/p/reports/OLMo-{ckpt}_{qual,time}_reads.json, each at the sha256 the task_correct raw printed; of a
    contrast record nothing but its flag), the qual and time p reports, the seat's second ruling's raw, its own source,
    and a scratch directory of synthetic records and call logs. Never a checkpoint, a call log or a p output.
  - ``run``: before gate 1, the task_correct raw, the pools file, the lexicon and the second ruling's raw. No
    checkpoint, call log or p report until five gates pass, in order -- (1) the three end notices' exit statuses,
    stated on the command line, are all 0 (the seat's §5 item 2: a non-zero exit is a STOP for the seat); (2) each
    unit's VERDICTS or NOT-RUN output exists (existence only, never opened); (3) p's and m's package_sha256 are the
    lock's; (4) this script's bytes, and the second ruling's raw's, are their blobs at HEAD (committed, the seat's §3);
    (5) the self-test passes, in this
    process (it reads the files ``--selftest`` reads; an exception inside it closes the gate). Then each unit's three
    checkpoints and three call logs, by exact path (data/p/ckpt/OLMo-{ckpt}_{time,qual,campaign}.json and
    ..._p-calls.jsonl; the directory is never listed), and each stage's committed p report.

TWO PASSES. Every checkpoint and call log is read and checked -- the checkpoint's identity, its content as m's reader
parsed it equal to the bytes hashed, its p report's record of that sha256, the read domain (p's ``session_counters``
and this step's table, each against the committed report), the corrupted rounds against the renders of record, the
asserted sham ``task_correct`` rows against their committed figures; the call log's sha256 and path the ones its p
report records, its bytes unchanged while read, its malformed lines as many as the report records, its runs this
stage's and run by the p package its report names, each of its calls attributed to one recorded round and no round
twice, the sham arm's proxy cells equal to the report's -- before any count is printed. After the gates, any failure
in this pass is a STOP (exit 4): its STOP line is the only line it adds, with counts and keys, never a log line's
position.

WHAT IT PRINTS: counts as k of n, the keys of the rounds counted, the control-character texts by key (F-p13 (a),
JSON-escaped), the proxy's cells by arm and the calls per contrast session, digests, the self-test's lines (in
``run``, gate 5) and the rulings. Never a pick, a menu, a response other than those texts, or a call's text, index or
timing.

Exit codes: 0 done (for the selftest, every check passes); 1 a selftest FAIL; 2 refused (a gate closed, or an input
not as pinned or unreadable); 4 STOP (a recount or a check row differs from its committed figure, a record or a call
log is not as the rule reads it, or an unexpected error). A message names repository paths relative to the root.

Usage, from the repository root, in a battery window, at nice -n 19:
  python -B scripts/p_verdicts_counters.py --selftest
  python -B scripts/p_verdicts_counters.py run --exit OLMo-sft=0 --exit OLMo-dpo=0 --exit OLMo-instruct=0
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import types
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from valence_core.m import corr as m_corr          # noqa: E402  the pool p's stage reports used (stage.py:966)
from valence_core.m import readrule as m_readrule  # noqa: E402  the act of release (m:271)
from valence_core.m import resume as m_resume      # noqa: E402  m's checkpoint reader and package hash
from valence_core.p import corrupt as p_corrupt    # noqa: E402  p's renders of record
from valence_core.p import guard as p_guard        # noqa: E402  p's package hash
from valence_core.p import report as p_report      # noqa: E402  p §2.3's predicates and session_counters, unchanged
from valence_core.p import stage as p_stage        # noqa: E402  read_calls, log_consistency_problems, attribute_calls

SCRIPT_REL = "scripts/p_verdicts_counters.py"
TC_RAW_REL = "results/raw/2026-11-11_p-qual_task-correct.txt"
TC_RAW_SHA256 = "57e9c7dca305096d007507584b7b5e94d95c05b64fb7c2375e51bbd5c05656e2"
TC_SHA256 = "9aa0e2d9155d1093ab260d90abc4dc9c8aeb3cd630b0edf49628561628014e0f"
TC_HEADER = f"# ==== task_correct.py (sha256 {TC_SHA256}) ===="
REPORT_REL = "valence_core/p/report.py"
#: The packages every LOCK-p-OLMo-{ckpt} v1.0 names (§8.1, §8.2; committed at 038bf3e).
P_PACKAGE_SHA256 = "a38d93bb83b64400c2663aee7f26cbe299300cc8a982935cce9b1187ed5ba2d7"
M_PACKAGE_SHA256 = "7756dcf42532b222b50e3bd8f41e2dc20053fa0a7a2b60e033dda559666349bb"
UNITS = ("OLMo-sft", "OLMo-dpo", "OLMo-instruct")
STAGES = ("time", "qual", "campaign")
TC_STAGES = ("time", "qual", "campaign")             # R1 (c): every stage
ARMS = ("sham", "contrast")
PHASES = ("forced", "free")
CKPT_REL = "data/p/ckpt/{unit}_{stage}.json"
CALLS_REL = "data/p/ckpt/{unit}_{stage}_p-calls.jsonl"   # R2 (b): the stage's call log, by exact path
P_REPORT_REL = "data/p/reports/{unit}_{stage}_p-report.json"
READS_REL = "data/p/reports/{unit}_{stage}_reads.json"
OUTPUT_RELS = ("data/p/verdicts/{unit}_VERDICTS.json", "data/p/verdicts/{unit}_NOT-RUN.json")
#: The reads files' sha256s as the task_correct raw printed them (its stdout at a225a89).
READS_SHA256 = {
    "time": {"OLMo-sft": "294361ed8e7362417db5175ae8af9880a86c84d8e7fa5e8242231987474b408d",
             "OLMo-dpo": "b44035beba9a3ab480dd5fbd09b1b0d87ea92fdbef21e4f00fda80c899f6639e",
             "OLMo-instruct": "c7045474cad63d1e2bafb0d05d8d80c2fb2efa87f21ff655c34fc1c6c09f75ad"},
    "qual": {"OLMo-sft": "cad7da75e077c66336743fec2fd9ff4d502a47bb9ac63d806cc29a39a5a3ce77",
             "OLMo-dpo": "92c1cc85da421de1369dd7d127543acf725508108254f5bb1fa087381ac9db4f",
             "OLMo-instruct": "afbcfb35c44a175763c071121cb5b559a75f604dae356c51cc19274544d172d0"},
}
#: The committed sham task_correct figures the step reproduces, {stage: {unit: {phase: (k, n)}}}: G-F0m-OLMo (p)'s,
#: committed at a225a89 and confirmed by the seat's answers of 2026-11-12 (Q2, "159/159/160"); G-TIME-OLMo (p)'s, the
#: seat's "first row" (its answers of 2026-11-09, line 34: "sft 9 of 10 -- round 1's `4`; dpo 10 of 10; instruct 10
#: of 10"), by phase as Code's check at a225a89 printed it.
COMMITTED_SHAM_TC = {
    "qual": {"OLMo-sft": {"forced": (63, 64), "free": (96, 96)},
             "OLMo-dpo": {"forced": (63, 64), "free": (96, 96)},
             "OLMo-instruct": {"forced": (64, 64), "free": (96, 96)}},
    "time": {"OLMo-sft": {"forced": (3, 4), "free": (6, 6)},
             "OLMo-dpo": {"forced": (4, 4), "free": (6, 6)},
             "OLMo-instruct": {"forced": (4, 4), "free": (6, 6)}},
}
#: The stages whose sham task_correct rows have committed figures, asserted (R1 (c)); the campaign's is printed only.
TC_ASSERTED = tuple(COMMITTED_SHAM_TC)
#: The seat's second ruling (R1, R2), its raw and the two rulings quoted verbatim from its §0 (the self-test asserts
#: each a substring of the raw's text).
RULING_RAW_REL = "results/raw/2026-11-16_p-verdicts-counters_design-to-code_answers.md"
RULING_RAW_SHA256 = "aea918c5f6f374522ad780ce29685c8c3f950b7457a46933022c090e74680395"
RULING_R1 = ("At the unit's VERDICTS, `task_correct` runs over every recorded round of every recorded session of the "
             "unit — G-TIME-OLMo (p)'s, G-F0m-OLMo (p)'s and the campaign's; sham and contrast; forced and free. The "
             "gate stages' sham rows are recounted and asserted against their committed figures, as Code built it; the "
             "campaign's sham row has no committed figure, and the step's is its first. Reported as k of n per stage, "
             "arm and phase, beside the bar; it decides nothing.")
RULING_R2 = ("The reports withheld the proxy's contrast counts \"to the unit's VERDICTS\", which is a promise to report "
             "them there. The step reads each unit's three call logs by exact path, applies p's `attribute_calls` "
             "unchanged, and prints for the contrast arm the cells p's report gives the sham arm. Nothing per call, no "
             "text.")
#: The calls this script never makes (it reads files by exact path only); built by concatenation so that the source
#: check of the self-test does not find its own list.
_LISTING_CALLS = tuple(a + b for a, b in ((".", "glob("), (".", "rglob("), (".", "iterdir("), ("os.", "listdir("),
                                          ("os.", "scandir("), ("os.", "walk(")))


class Refused(SystemExit):
    """A gate closed, or an input not as pinned: nothing counted (exit 2)."""


class Stop(SystemExit):
    """A recount differs from its committed figure, or a record is not as the rule reads it (exit 4)."""


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _scrub(msg: str) -> str:
    """A message with repository paths relative to the root (never a machine path)."""
    for root in sorted({str(REPO), str(REPO.resolve())}, key=len, reverse=True):
        msg = msg.replace(root + "/", "").replace(root, "<repo>")
    return msg


# --- the imports --------------------------------------------------------------------------------------------------
def load_task_correct(raw: bytes | None = None) -> types.ModuleType:
    """task_correct.py from the committed raw: the raw's sha256, the one header line, the script's sha256; then the
    script runs as a module (``__name__`` is not ``"__main__"``, so its ``main`` does not run)."""
    raw = (REPO / TC_RAW_REL).read_bytes() if raw is None else raw
    if _sha(raw) != TC_RAW_SHA256:
        raise Refused(f"REFUSED: {TC_RAW_REL} hashes to {_sha(raw)[:16]}, not {TC_RAW_SHA256[:16]}")
    text = raw.decode("utf-8")
    marker = "\n" + TC_HEADER + "\n"
    if text.count(marker) != 1:
        raise Refused(f"REFUSED: {TC_RAW_REL} does not carry task_correct.py's header line exactly once")
    src = text[text.index(marker) + len(marker):]
    if _sha(src.encode("utf-8")) != TC_SHA256:
        raise Refused(f"REFUSED: the script in {TC_RAW_REL} hashes to {_sha(src.encode('utf-8'))[:16]}, not "
                      f"{TC_SHA256[:16]}")
    mod = types.ModuleType("p_task_correct_a225a89")
    mod.__file__ = f"{TC_RAW_REL} (task_correct.py)"
    exec(compile(src, f"{TC_RAW_REL}:task_correct.py", "exec", dont_inherit=True), mod.__dict__)
    return mod


def pool_of_record(tc: types.ModuleType) -> list[dict]:
    """CORR_clean: m's loader (the pool p's stage reports used) and task_correct's (sha256 in full), asserted equal."""
    pool_m = m_corr.load_pool()
    pool_tc = [{"task": x["task"], "gold": list(x["gold"])} for x in tc.load_pool(REPO)]
    if pool_tc != pool_m:
        raise Refused("REFUSED: m's CORR_clean and task_correct's differ")
    return pool_m


def code_shas() -> dict:
    return {"p": p_guard.package_sha256(), "m": m_resume.package_sha256()}


def code_problems() -> list[str]:
    """p's and m's package_sha256 against the values every LOCK-p v1.0 names: the definitions are the lock's."""
    got = code_shas()
    return [f"{k}'s package_sha256 is {got[k][:16]}, not the lock's {want[:16]}"
            for k, want in (("p", P_PACKAGE_SHA256), ("m", M_PACKAGE_SHA256)) if got[k] != want]


# --- the tabulation (no definition: the imported predicates over the rounds, by arm and phase) ---------------------
def _arm(rec: dict) -> str:
    flag = rec.get("contrast")
    if flag is True:
        return "contrast"
    if flag is False:
        return "sham"
    raise Stop(f"STOP: a session record's contrast flag is {flag!r}, not a bool")


def _phase(r: dict) -> str:
    ph = r.get("phase")
    if ph not in PHASES:
        raise Stop(f"STOP: a round's phase is {ph!r}, not one of {PHASES}")
    return ph


def _item(r: dict, pool: list[dict]) -> int:
    i = r.get("item")
    if isinstance(i, bool) or not isinstance(i, int) or not 0 <= i < len(pool):
        raise Stop(f"STOP: a round's item is {i!r}, not an index of CORR_clean")
    return i


def check_round(rec: dict, r: dict, pool: list[dict]) -> None:
    """A released round as the rule reads it: a clean round's task text is its item's task; a corrupted round lies in
    a contrast session and its task text is its item's render of record (m:159's delivery; runner_olmo.py:358-361's
    own check)."""
    i, prop = _item(r, pool), r.get("property")
    if prop == "clean":
        if r.get("task_text") != pool[i]["task"]:
            raise Stop(f"STOP: {p_report.round_key(rec, r)}: a clean round's task text is not its item's task")
    elif prop == "corrupted":
        if _arm(rec) != "contrast":
            raise Stop(f"STOP: {p_report.round_key(rec, r)}: a corrupted round in a sham session")
        if r.get("task_text") != p_corrupt.RENDERS_OF_RECORD[i]:
            raise Stop(f"STOP: {p_report.round_key(rec, r)}: a corrupted round's task text is not its item's render")
    else:
        raise Stop(f"STOP: {p_report.round_key(rec, r)}: property {prop!r}")


def p23_table(records: list[dict], pool: list[dict], lexicon: frozenset) -> dict:
    """p §2.3's five counters and the hair trigger over every round of every session, by arm and phase: each counter's
    keys (``round_key``), each cell's round count, and the control-character texts by key."""
    clean = p_report.clean_task_words(pool)
    preds = {"control_chars": lambda r: p_report.control_chars(r["text"]),
             "harness_first_line": lambda r: p_report.harness_first_line(r["text"]),
             "cap_hits": lambda r: bool(r["cap_hit"]),
             "refusals": lambda r: p_report.refusal(r["text"]),
             "corrupted_spelling": lambda r: p_report.corrupted_spelling(r["text"], pool[_item(r, pool)]["gold"],
                                                                         clean, lexicon)}
    if tuple(preds) != tuple(p_report.COUNTERS):
        raise Stop(f"STOP: p's counters are {p_report.COUNTERS}; this step tabulates {tuple(preds)}")
    cells = {a: {ph: {"n": 0, **{c: [] for c in p_report.COUNTERS}} for ph in PHASES} for a in ARMS}
    hair, n_rounds, cc_texts, sessions = [], 0, {}, {a: 0 for a in ARMS}
    for rec in records:
        arm = _arm(rec)
        sessions[arm] += 1
        for r in rec.get("rounds", ()):
            ph, key = _phase(r), p_report.round_key(rec, r)
            cells[arm][ph]["n"] += 1
            n_rounds += 1
            if p_report.line_break_in_stored_text(r["text"]):
                hair.append(key)
            for name, fn in preds.items():
                if fn(r):
                    cells[arm][ph][name].append(key)
            if p_report.control_chars(r["text"]):
                cc_texts[key] = r["text"]
    return {"cells": cells, "hair": hair, "n_rounds": n_rounds, "cc_texts": cc_texts, "sessions": sessions}


def read_domain_view(t: dict) -> dict:
    """The cells a stage's p report carried (``report.session_counters``' read domain), from this step's table."""
    c = t["cells"]
    sham_all = {k: sorted(c["sham"]["forced"][k] + c["sham"]["free"][k])
                for k in ("control_chars", "harness_first_line", "cap_hits", "refusals")}
    sham_cc = set(sham_all["control_chars"])
    con_cc = c["contrast"]["forced"]["control_chars"]
    return {"n_sham_rounds": c["sham"]["forced"]["n"] + c["sham"]["free"]["n"],
            "n_sham_forced_rounds": c["sham"]["forced"]["n"],
            "hair_trigger": len(t["hair"]),
            "sham": {**sham_all, "corrupted_spelling": sorted(c["sham"]["forced"]["corrupted_spelling"])},
            "sham_cc_texts": {k: v for k, v in sorted(t["cc_texts"].items()) if k in sham_cc},
            "contrast_forced_cc": sorted(con_cc),
            "contrast_forced_cc_texts": {k: t["cc_texts"][k] for k in sorted(con_cc)},
            "n_contrast_forced_rounds": c["contrast"]["forced"]["n"]}


def committed_view(rep: dict) -> dict:
    """The same cells as a p report (or ``session_counters``' output, under ``counters``) records them; each count
    asserted equal to its key list's length."""
    c = rep["counters"]
    for k in p_report.COUNTERS:
        if c["sham"][k]["n"] != len(c["sham"][k]["keys"]):
            raise Stop(f"STOP: the p report's sham {k} count is not its key list's length")
    cf = c["contrast_forced_control_chars"]
    if cf["n"] != len(cf["keys"]):
        raise Stop("STOP: the p report's contrast forced control-character count is not its key list's length")
    return {"n_sham_rounds": c["n_sham_rounds"], "n_sham_forced_rounds": c["n_sham_forced_rounds"],
            "hair_trigger": c["hair_trigger"]["n"],
            "sham": {k: sorted(c["sham"][k]["keys"]) for k in p_report.COUNTERS},
            "sham_cc_texts": dict(sorted(c["sham"]["control_chars"]["texts"].items())),
            "contrast_forced_cc": sorted(cf["keys"]),
            "contrast_forced_cc_texts": dict(sorted(cf["texts"].items())),
            "n_contrast_forced_rounds": cf["n_forced_rounds"]}


def tc_rows(records: list[dict], pool: list[dict], item_key: dict, tc: types.ModuleType) -> tuple[dict, dict]:
    """task_correct's k of n by arm and phase, under the match rule as task_correct.py reads it (``correct``) and under
    its alternative reading (``alt=True``), which the step prints beside, as task_correct.py does."""
    rows = {a: {ph: [0, 0] for ph in PHASES} for a in ARMS}
    alt = {a: {ph: [0, 0] for ph in PHASES} for a in ARMS}
    for rec in records:
        arm = _arm(rec)
        for r in rec.get("rounds", ()):
            ph, key = _phase(r), item_key[_item(r, pool)]
            rows[arm][ph][0] += bool(tc.correct(r["text"], key))
            rows[arm][ph][1] += 1
            alt[arm][ph][0] += bool(tc.correct(r["text"], key, alt=True))
            alt[arm][ph][1] += 1
    return rows, alt


def proxy_cells(records: list[dict], events: list[dict], where: str) -> dict:
    """R2 (b): p's ``attribute_calls``, unchanged, over the stage's records and its call log's events. For each arm the
    cells p's report gives the sham arm (stage.py's ``build_report``: rounds, attributed, cuts with their round keys,
    unattributed round keys), and per contrast session the number of calls attributed to its rounds. A STOP, with its
    line: attribution problems; a call attributed to no recorded round (an orphan); a call matching a round another
    call was attributed to (a re-run), which leaves a session's number of calls undetermined."""
    att = p_stage.attribute_calls(records, events)
    if att["problems"]:
        raise Stop(f"STOP: {where}: p's attribute_calls reports {att['problems'][:3]}")
    n_calls = sum(1 for e in events if e.get("event") == "call")
    if att["n_orphans"]:
        raise Stop(f"STOP: {where}: {att['n_orphans']} of {n_calls} calls attributed to no recorded round")
    if n_calls != len(att["by_round"]):
        raise Stop(f"STOP: {where}: {n_calls} calls for {len(att['by_round'])} attributed rounds: a call matches a "
                   f"round another call was attributed to (a re-run)")
    cells = {}
    for a in ARMS:
        keys = [p_report.round_key(rec, r) for rec in records if _arm(rec) == a for r in rec.get("rounds", ())]
        hit = {k: att["by_round"].get(k) for k in keys}
        cells[a] = {"n_rounds": len(keys), "n_attributed": sum(v is not None for v in hit.values()),
                    "n_cuts": sum(1 for v in hit.values() if v is not None and v.get("cut")),
                    "cut_keys": [k for k, v in hit.items() if v is not None and v.get("cut")],
                    "unattributed_keys": [k for k, v in hit.items() if v is None]}
    per_session: dict[tuple[str, int], int] = {}
    for rec in records:
        if _arm(rec) == "contrast":
            sk = (str(rec["template"]), rec["s"])
            if isinstance(sk[1], bool) or not isinstance(sk[1], int) or sk in per_session:
                raise Stop(f"STOP: {where}: a contrast session's index is {sk[1]!r} (not an int, or twice)")
            per_session[sk] = sum(1 for r in rec.get("rounds", ()) if p_report.round_key(rec, r) in att["by_round"])
    return {"cells": cells, "per_session": per_session, "n_calls": n_calls}


def calls_by_count(per_session: dict) -> list[str]:
    """The calls per contrast session, grouped: '10 calls: A0-OLMo-x s=0-7' -- every session's count recoverable."""
    groups: dict[tuple[int, str], list[int]] = {}
    for (tpl, s), n in per_session.items():
        groups.setdefault((n, tpl), []).append(s)
    return [f"{n} call{'s' if n != 1 else ''}: {tpl} s={_spans(ss)} ({len(ss)} session{'s' if len(ss) != 1 else ''})"
            for (n, tpl), ss in sorted(groups.items(), key=lambda kv: (-kv[0][0], kv[0][1]))]


def committed_proxy(rep: dict) -> dict:
    """The sham arm's proxy cells as a p report records them (``proxy.sham``), in ``proxy_cells``' form."""
    sh = (rep.get("proxy") or {}).get("sham") or {}
    return {k: sh.get(k) for k in ("n_rounds", "n_attributed", "n_cuts", "cut_keys", "unattributed_keys")}


def _spans(nums: list[int]) -> str:
    """Session indices as runs (0-3, 5): every index printed, none per call."""
    out, nums = [], sorted(nums)
    i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(f"{nums[i]}" if i == j else f"{nums[i]}-{nums[j]}")
        i = j + 1
    return ", ".join(out)


# --- the run's gates, paths and two passes --------------------------------------------------------------------------
def third_run_ended(root: Path) -> bool:
    """Each unit has its VERDICTS or NOT-RUN output (gate 2). Existence only: no output is opened."""
    return all(any((root / rel.format(unit=u)).is_file() for rel in OUTPUT_RELS) for u in UNITS)


def checkpoint_paths(root: Path) -> list[tuple[str, str, Path]]:
    """The nine checkpoints, by exact path: each unit's time, qual and campaign checkpoint, never a listing."""
    return [(u, s, root / CKPT_REL.format(unit=u, stage=s)) for u in UNITS for s in STAGES]


def script_committed_problems() -> list[str]:
    """Gate 4: this script's working-tree blob, and the second ruling's raw's, are their blobs at HEAD (git hash-object
    against git rev-parse)."""
    def git(*args: str) -> str:
        r = subprocess.run(["git", *args], capture_output=True, text=True, cwd=REPO)
        return r.stdout.strip() if r.returncode == 0 else ""
    out = []
    for rel in (SCRIPT_REL, RULING_RAW_REL):
        head, work = git("rev-parse", f"HEAD:{rel}"), git("hash-object", "--", rel)
        if not head or head != work:
            out.append(f"{rel} is not committed at HEAD as it stands (blob {work[:12]}, HEAD's {head[:12] or 'absent'})")
    return out


def collect(root: Path, reader, *, pool: list[dict], item_key: dict, lexicon: frozenset, tc: types.ModuleType,
            committed_tc: dict = COMMITTED_SHAM_TC, campaign_pkg: str = P_PACKAGE_SHA256) -> list[dict]:
    """Pass 1: read and check all nine checkpoints and their call logs; nothing is printed. Each check that fails
    STOPs here."""
    out = []
    for u, s, path in checkpoint_paths(root):
        rel = path.relative_to(root).as_posix()
        ck = reader(path)
        data = path.read_bytes()
        if json.loads(data) != ck:
            raise Stop(f"STOP: {rel}: the content checked is not the bytes hashed (it changed while it was read)")
        before = data
        ident = ck.get("identity") or {}
        if ident.get("unit") != u or ident.get("stage") != s:
            raise Stop(f"STOP: {rel} is {ident.get('unit')}/{ident.get('stage')}, not {u}/{s}")
        records = m_readrule.release_full(ck["sessions"])
        for rec in records:
            for r in rec.get("rounds", ()):
                check_round(rec, r, pool)
        rrel = (root / P_REPORT_REL.format(unit=u, stage=s)).relative_to(root).as_posix()
        rep_bytes = (root / rrel).read_bytes()
        rep = json.loads(rep_bytes)
        if (rep.get("checkpoint") or {}).get("sha256") != _sha(before) or rep.get("unit") != u:
            raise Stop(f"STOP: {rrel} does not record {rel}'s sha256 (or names another unit)")
        if s == "campaign" and rep.get("p_package_sha256") != campaign_pkg:
            raise Stop(f"STOP: {rrel} was not built by the lock's p package")
        theirs = committed_view(rep)
        if committed_view({"counters": p_report.session_counters(records, pool, lexicon)}) != theirs:
            raise Stop(f"STOP: {u} {s}: p's session_counters over the released records differs from {rrel}")
        t = p23_table(records, pool, lexicon)
        mine = read_domain_view(t)
        if mine != theirs:
            raise Stop(f"STOP: {u} {s}: this step's read-domain cells differ from {rrel}: "
                       f"{sorted(k for k in mine if mine[k] != theirs[k])}")
        res = {"unit": u, "stage": s, "rel": rel, "ck_sha": _sha(before), "rrel": rrel, "rep_sha": _sha(rep_bytes),
               "rep_pkg": rep.get("p_package_sha256"), "t": t}
        # R2 (b): the stage's call log, by exact path; p's read_calls, log_consistency_problems, attribute_calls
        cpath = root / CALLS_REL.format(unit=u, stage=s)
        crel = cpath.relative_to(root).as_posix()
        if not cpath.is_file():
            raise Stop(f"STOP: {crel}: absent")
        cbytes = cpath.read_bytes()
        cl = rep.get("call_log") if isinstance(rep.get("call_log"), dict) else {}
        if cl.get("sha256") != _sha(cbytes) or cl.get("path") != f"ckpt/{u}_{s}_p-calls.jsonl":
            raise Stop(f"STOP: {rrel} does not record {crel}'s sha256 (or names another log)")
        events, lprobs = p_stage.read_calls(cpath)
        if any(x.endswith(": absent") or ": unreadable (" in x for x in lprobs):
            raise Stop(f"STOP: {crel}: absent or unreadable when p's read_calls read it")
        if cpath.read_bytes() != cbytes:
            raise Stop(f"STOP: {crel}: the log changed while it was read")
        if (not lprobs) is not cl.get("well_formed") or len(lprobs) != cl.get("n_malformed_lines"):
            raise Stop(f"STOP: {crel}: {len(lprobs)} malformed line(s) by p's read_calls; {rrel} records "
                       f"well_formed {cl.get('well_formed')!r}, {cl.get('n_malformed_lines')!r} malformed")
        cons = p_stage.log_consistency_problems(u, events, gate=s)
        if cons:
            raise Stop(f"STOP: {crel} is not this stage's: {cons[:3]}")
        runs = [e for e in events if e.get("event") == "run"]
        pkgs = sorted({str(e.get("p_package_sha256")) for e in runs})
        if pkgs != [str(rep.get("p_package_sha256"))]:
            raise Stop(f"STOP: {crel}'s runs ran under p package(s) {[x[:16] for x in pkgs]}, not the one {rrel} "
                       f"names")
        if cl.get("n_runs") != len(runs):
            raise Stop(f"STOP: {crel} holds {len(runs)} run(s); {rrel} records {cl.get('n_runs')!r}")
        px = proxy_cells(records, events, f"{u} {s} ({crel})")
        if px["cells"]["sham"] != committed_proxy(rep):
            raise Stop(f"STOP: {u} {s}: the sham arm's proxy cells differ from {rrel}'s")
        if (rep.get("proxy") or {}).get("attribution_complete") is not (not px["cells"]["sham"]["unattributed_keys"]):
            raise Stop(f"STOP: {u} {s}: {rrel}'s attribution_complete does not match the sham arm's attribution")
        res.update(crel=crel, calls_sha=_sha(cbytes), px=px, n_runs=len(runs), n_malformed=len(lprobs),
                   stop_rows=[row for row in (cl.get("runs") or []) if isinstance(row, dict) and row.get("stop")])
        if s in TC_STAGES:
            rows, alt = tc_rows(records, pool, item_key, tc)
            if s in committed_tc:
                if {ph: tuple(rows["sham"][ph]) for ph in PHASES} != committed_tc[s][u]:
                    raise Stop(f"STOP: {u} {s}: the sham task_correct recount is not the committed figure")
            res.update(rows=rows, alt=alt, tc_asserted=s in committed_tc)
        out.append(res)
    return out


def collect_guarded(root: Path, reader, **kw) -> list[dict]:
    """Pass 1 after the gates: a failure other than a STOP -- m's reader's own refusal, a missing file, anything else
    raised while released records are being read -- is a STOP too (exit 4), never a refusal."""
    try:
        return collect(root, reader, **kw)
    except Stop:
        raise
    except (Exception, SystemExit) as e:        # noqa: BLE001
        raise Stop(f"STOP: pass 1 failed after the gates: {type(e).__name__}: {e}") from None


def _say(*parts: str) -> None:
    print(*parts, flush=True)


def _cell_line(cell: dict) -> str:
    return ", ".join(f"{k} {len(cell[k])}" for k in p_report.COUNTERS)


def _frac(kn) -> str:
    return f"{kn[0]} of {kn[1]}"


def emit(results: list[dict]) -> None:
    """Pass 2: print every stage's counts, after every check of pass 1 has passed."""
    for res in results:
        t, c = res["t"], res["t"]["cells"]
        u, s = res["unit"], res["stage"]
        _say(f"== {u} / {s}: checkpoint {res['rel']} sha256 {res['ck_sha']}; its p report {res['rrel']} sha256 "
             f"{res['rep_sha']} records that sha256 (built by p package {str(res['rep_pkg'])[:16]}…)")
        _say(f"   recorded sessions: sham {t['sessions']['sham']}, contrast {t['sessions']['contrast']}; recorded "
             f"rounds {t['n_rounds']}")
        _say("   p §2.3, rounds counted of the recorded rounds in the cell, by arm and phase:")
        for a in ARMS:
            for ph in PHASES:
                _say(f"     {a} {ph} (n = {c[a][ph]['n']}): {_cell_line(c[a][ph])}")
        _say(f"   the hair trigger line_break_in_stored_text: {len(t['hair'])} of {t['n_rounds']} rounds")
        hits = [(a, ph, k, c[a][ph][k]) for a in ARMS for ph in PHASES for k in p_report.COUNTERS if c[a][ph][k]]
        for a, ph, k, keys in hits:
            _say(f"   counted, {k}, {a} {ph}: {', '.join(keys)}")
        if not hits:
            _say("   counted: no round in any cell")
        for k in sorted(t["cc_texts"]):
            _say(f"   control-character text (F-p13 (a)), {k}: {json.dumps(t['cc_texts'][k])}")
        _say("   the read domain (the sham rounds' five counters, the corrupted-spelling counter on the sham forced "
             "rounds, the contrast forced rounds' control characters, the hair trigger), by p's session_counters "
             "and by this step's table, equals the committed p report's: yes")
        wf = c["contrast"]["forced"]
        _say(f"   withheld at the stage report, counted here: contrast forced (n = {wf['n']}): "
             f"{', '.join(f'{k} {len(wf[k])}' for k in p_report.COUNTERS if k != 'control_chars')}; contrast "
             f"free (n = {c['contrast']['free']['n']}): {_cell_line(c['contrast']['free'])}; sham free "
             f"(n = {c['sham']['free']['n']}): corrupted_spelling {len(c['sham']['free']['corrupted_spelling'])}")
        px = res["px"]
        stop_txt = ("none" if not res["stop_rows"] else json.dumps(res["stop_rows"], sort_keys=True))
        _say(f"   the proxy (R2 (b)): call log {res['crel']} sha256 {res['calls_sha']}, the one its p report records; "
             f"{res['n_runs']} run(s), {res['n_malformed']} malformed line(s) as the report records, {px['n_calls']} "
             f"calls, each attributed to one recorded round (p's attribute_calls); STOP marks in the p report's run "
             f"rows: {stop_txt}")
        for a in ARMS:
            cc = px["cells"][a]
            _say(f"     {a}: {cc['n_attributed']} of {cc['n_rounds']} rounds attributed, {cc['n_cuts']} cut(s)"
                 + (f" ({', '.join(cc['cut_keys'])})" if cc["cut_keys"] else "")
                 + (f"; unattributed: {', '.join(cc['unattributed_keys'])}" if cc["unattributed_keys"] else "")
                 + ("; the committed p report's cells: equal" if a == "sham" else ""))
        _say("     calls per contrast session (calls attributed to its rounds): "
             + ("; ".join(calls_by_count(px["per_session"])) or "no contrast session"))
        if "rows" in res:
            rows, alt, con = res["rows"], res["alt"], res["rows"]["contrast"]
            allc = [con["forced"][0] + con["free"][0], con["forced"][1] + con["free"][1]]
            note = ("the committed figure: equal" if res["tc_asserted"]
                    else "no committed figure: this is its first, not asserted")
            _say(f"   task_correct (R1 (c)): sham forced {_frac(rows['sham']['forced'])}, free "
                 f"{_frac(rows['sham']['free'])} ({note}); contrast forced "
                 f"{_frac(con['forced'])}, free {_frac(con['free'])}, all {_frac(allc)}")
            _say("   the alternative reading (punctuation deleted, not spaced): "
                 + ("no count changes" if alt == rows else f"counts differ -- {alt}"))


def load_ruling(raw: bytes | None = None) -> str:
    """The seat's second ruling's raw, at its pinned sha256: the text RULING_R1 and RULING_R2 quote."""
    raw = (REPO / RULING_RAW_REL).read_bytes() if raw is None else raw
    if _sha(raw) != RULING_RAW_SHA256:
        raise Refused(f"REFUSED: {RULING_RAW_REL} hashes to {_sha(raw)[:16]}, not {RULING_RAW_SHA256[:16]}")
    return raw.decode("utf-8")


def run(exits: dict) -> int:
    tc = load_task_correct()
    pool = pool_of_record(tc)
    item_key = tc.key_table(pool)
    lex = p_report.load_lexicon()
    ruling = load_ruling()
    if RULING_R1 not in ruling or RULING_R2 not in ruling:
        raise Refused(f"REFUSED: the rulings this step quotes are not verbatim in {RULING_RAW_REL}")
    if exits != {u: 0 for u in UNITS}:
        raise Refused(f"REFUSED (gate 1): the three end notices' exit statuses must each be stated, and be 0: "
                      f"{exits}")
    if not third_run_ended(REPO):
        raise Refused("REFUSED (gate 2): not every unit has its VERDICTS or NOT-RUN output; no checkpoint read")
    cp = code_problems()
    if cp:
        raise Refused(f"REFUSED (gate 3): {cp}")
    sp = script_committed_problems()
    if sp:
        raise Refused(f"REFUSED (gate 4): {sp}")
    _say("p's counters at VERDICTS (Code's own step; the seat's answers of 2026-11-16, §3 and §4) -- descriptive "
         "(rule 23): no bar, no verdict sentence, no label")
    _say(f"gate 1: the end notices' exit statuses, as stated: {', '.join(f'{u}={exits[u]}' for u in UNITS)}")
    _say("gate 2: each unit's VERDICTS or NOT-RUN output exists (existence only, none opened)")
    shas = code_shas()
    _say(f"gate 3: p's package_sha256 {shas['p']} and m's {shas['m']}, the lock's")
    _say(f"gate 4: {SCRIPT_REL} sha256 {_sha((REPO / SCRIPT_REL).read_bytes())} and {RULING_RAW_REL} sha256 "
         f"{RULING_RAW_SHA256}, each its blob at HEAD")
    _say("gate 5: the self-test, in this process:")
    try:
        rc = run_selftest()
    except (Exception, SystemExit) as e:        # noqa: BLE001  run_selftest contains its own; this is a backstop
        raise Refused(f"REFUSED (gate 5): the self-test raised {type(e).__name__}: {e}; no checkpoint read") from None
    if rc != 0:
        raise Refused("REFUSED (gate 5): the self-test did not pass; no checkpoint read")
    _say(f"imports: {REPORT_REL} sha256 {_sha((REPO / REPORT_REL).read_bytes())}; task_correct.py from "
         f"{TC_RAW_REL} (raw sha256 {TC_RAW_SHA256}; script sha256 {TC_SHA256})")
    _say(f"pools data/f/pools.json (CORR_clean, 16 items) sha256 {_sha((REPO / 'data/f/pools.json').read_bytes())}; "
         f"lexicon {p_report.LEXICON_REL} sha256 {p_report.LEXICON_SHA256}")
    _say(f"key table (task_correct.py's KEYS, the seat's, verbatim): {', '.join(tc.KEYS)}")
    _say(f"match rule (task_correct.py's MATCH_RULE, the seat's, verbatim): {tc.MATCH_RULE}")
    _say(tc.READING)
    _say(f"the seat's second ruling ({RULING_RAW_REL}, sha256 {RULING_RAW_SHA256}), §0, verbatim:")
    _say(f"  R1: (c), every stage. {RULING_R1}")
    _say(f"  R2: (b), computed. {RULING_R2}")
    results = collect_guarded(REPO, m_resume.read_checkpoint, pool=pool, item_key=item_key, lexicon=lex, tc=tc)
    emit(results)
    return 0


# --- the self-test (never a checkpoint, a call log or a p output) --------------------------------------------------
def sham_records_from_reads(path: Path, pool: list[dict], tc: types.ModuleType) -> tuple[list[dict], int]:
    """The reads file's sham records as released-record rounds, each round's item from its own ``Task:`` line, as
    task_correct.py's ``tally_file`` finds it (a forced round's ``item`` and ``task_text`` must agree; a round's text is
    its generation piece). Of a contrast record nothing but its flag is read."""
    data = json.loads(path.read_bytes())
    sessions = data.get("sessions")
    if not isinstance(sessions, list):
        raise Refused(f"REFUSED: {path.name} carries no sessions list")
    by_task: dict[str, list[int]] = {}
    for i, it in enumerate(pool):
        by_task.setdefault(it["task"], []).append(i)
    out, n_contrast = [], 0
    for rec in sessions:
        flag = rec.get("contrast")
        if flag is True:
            n_contrast += 1
            continue
        if flag is not False or rec.get("blinding") != tc.SHAM_BLINDING:
            raise Refused(f"REFUSED: {path.name}: a record is neither a flagged contrast nor a sham-redacted one")
        t = rec["transcript"]
        frags: dict[tuple, str] = {}
        for p in rec["pieces"]:
            if p["kind"] in ("round", "generation"):
                kk = (p["kind"], p["phase"], p["idx"])
                if kk in frags:
                    raise Refused(f"REFUSED: {path.name}: a duplicate {p['kind']} piece")
                frags[kk] = t[p["start"]:p["end"]]
        rounds = []
        for r in rec["rounds"]:
            ph = r["phase"]
            ix = r["ri"] if ph == "forced" else r["ci"]
            task = tc.task_of(frags[("round", ph, ix)])
            owners = by_task.get(task, [])
            if len(owners) != 1:
                raise Refused(f"REFUSED: {path.name}: a {ph} round's task matches {len(owners)} items")
            if ph == "forced" and (r.get("item") != owners[0] or r.get("task_text") != task):
                raise Refused(f"REFUSED: {path.name}: a forced round's item or task_text disagrees with its Task line")
            if frags.get(("generation", ph, ix)) != r["text"]:
                raise Refused(f"REFUSED: {path.name}: a {ph} round's text differs from its generation piece")
            rounds.append({"phase": ph, ("ri" if ph == "forced" else "ci"): ix, "item": owners[0],
                           "property": "clean", "task_text": task, "text": r["text"], "cap_hit": r["cap_hit"]})
        out.append({"contrast": False, "template": rec["template"], "s": rec["s"], "rounds": rounds})
    return out, n_contrast


def _synthetic(pool: list[dict]) -> list[dict]:
    """Two released-form records (SELF-TEST ONLY) with one hit per named cell; texts chosen so that each predicate's
    outcome is fixed by its definition (the report module's docstring, m's ``gcal.normalize`` and task_correct.py's
    rule cases). Each round carries its own seed, as a recorded round does (attribute_calls' key)."""
    def rnd(ph, ix, item, text, seed, *, cap=False, prop="clean"):
        task = pool[item]["task"] if prop == "clean" else p_corrupt.RENDERS_OF_RECORD[item]
        return {"phase": ph, ("ri" if ph == "forced" else "ci"): ix, "item": item, "property": prop,
                "task_text": task, "text": text, "cap_hit": cap, "seed": seed}
    sham = {"contrast": False, "template": "A0s-OLMo-syn", "s": 0, "rounds": [
        rnd("forced", 0, 0, "77", 101),
        rnd("forced", 1, 8, "Januwy", 102),
        rnd("free", 0, 5, "Cold. \x07", 103),
        rnd("free", 1, 10, "12 wheels", 104, cap=True),
        rnd("free", 2, 1, "Seven\r", 105)]}
    con = {"contrast": True, "template": "A0-OLMo-syn", "s": 1, "rounds": [
        rnd("forced", 0, 4, "I'm sorry, I can't say. three", 201),
        rnd("forced", 1, 2, "### Response: March \x1b", 202, prop="corrupted"),
        rnd("free", 0, 15, "Shut", 203),
        rnd("free", 1, 13, "Twenty-four \x7f", 204)]}
    return [sham, con]


#: SELF-TEST ONLY: the synthetic calls the proxy cut (by seed), and the sham cells a report records for them, written
#: by hand (not computed by the function under test).
SYN_CUT_SEEDS = (104, 203)
SYN_SHAM_PROXY = {"n_rounds": 5, "n_attributed": 5, "n_cuts": 1, "cut_keys": ["A0s-OLMo-syn s=0 free 1"],
                  "unattributed_keys": []}


#: SELF-TEST ONLY: a text the synthetic call log carries where p's carries returned texts; it must never print.
SENTINEL = "SENTINEL-RETURNED"


def _synthetic_events(u: str, s: str, recs: list[dict]) -> list[dict]:
    """SELF-TEST ONLY: a call log's events for the synthetic records, in p's form (stage.py's run and end lines,
    proxy.py's call line): one call per round, its number, seed and stored text's sha256; on SYN_CUT_SEEDS a cut event
    as proxy.py writes one, its returned text carrying SENTINEL."""
    ev = [{"event": "run", "schema": p_stage.CALLS_SCHEMA, "run": 1, "resume": False, "stage": p_stage.label(u, s),
           "unit": u, "register_entered": [1, 2, 6, 7, 8, 9], "p_package_sha256": P_PACKAGE_SHA256,
           "proposal_p_sha256": "0" * 64, "stale_reservations": []}]
    n = 0
    for rec in recs:
        for r in rec["rounds"]:
            cut = ({"returned_text": f"{r['text']}\n{SENTINEL}", "stored_text": r["text"], "n_tok_returned": 9,
                    "n_tok_stored": 3, "stop_reason_returned": "cap", "cap_hit_returned": False}
                   if r["seed"] in SYN_CUT_SEEDS else None)
            ev.append({"event": "call", "run": 1, "call": n, "seed": r["seed"],
                       "text_sha256": p_stage.text_sha256(r["text"]), "cut": cut})
            n += 1
    ev.append({"event": "end", "run": 1, "outcome": "returned", "status": "PASS", "exception": None,
               "stop_marker": None, "stop_line_failed": None, "n_generate": n, "n_cuts": len(SYN_CUT_SEEDS),
               "term_d_at_stage_end": None})
    return ev


def _write_events(path: Path, events: list[dict]) -> None:
    path.write_text("".join(json.dumps(e) + "\n" for e in events), encoding="ascii")


def _synthetic_root(td: Path, pool: list[dict], lex: frozenset) -> Path:
    """A scratch root (SELF-TEST ONLY): the nine synthetic checkpoints, their call logs and their p reports, each report
    built by p's own ``session_counters`` over the checkpoint's sessions, recording its sha256, one run, and the sham
    proxy cells written by hand."""
    root = td / "root"
    for u, s, path in checkpoint_paths(root):
        recs = _synthetic(pool)
        ck = {"identity": {"unit": u, "stage": s}, "sessions": recs}
        path.parent.mkdir(parents=True, exist_ok=True)
        data = json.dumps(ck).encode("utf-8")
        path.write_bytes(data)
        lp = root / CALLS_REL.format(unit=u, stage=s)
        _write_events(lp, _synthetic_events(u, s, recs))
        rp = root / P_REPORT_REL.format(unit=u, stage=s)
        rp.parent.mkdir(parents=True, exist_ok=True)
        rp.write_text(json.dumps({"unit": u, "checkpoint": {"path": "x", "sha256": _sha(data)},
                                  "p_package_sha256": P_PACKAGE_SHA256,
                                  "counters": p_report.session_counters(recs, pool, lex),
                                  "call_log": {"path": f"ckpt/{u}_{s}_p-calls.jsonl", "sha256": _sha(lp.read_bytes()),
                                               "n_runs": 1, "well_formed": True, "n_malformed_lines": 0,
                                               "runs": [{"run": 1, "resume": False, "outcome": "returned",
                                                         "exception_type": None, "stop": False}]},
                                  "proxy": {"sham": dict(SYN_SHAM_PROXY), "attribution_complete": True}}),
                      encoding="utf-8")
    return root


def run_selftest() -> int:
    results: list[tuple[bool, str]] = []

    def chk(name: str, ok: bool, got: object = "") -> None:
        results.append((bool(ok), name))
        tail = "" if ok else f"  GOT {json.dumps(got, default=str)[:600]}"
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}{tail}", flush=True)

    try:
        _selftest_body(chk)
    except (Exception, SystemExit) as e:        # noqa: BLE001  an exception is a FAIL, never an escape
        chk("the self-test ran to its end without raising", False, f"{type(e).__name__}: {_scrub(str(e))}")
    n_ok = sum(1 for ok, _ in results if ok)
    print(f"  {n_ok}/{len(results)} selftest checks pass", flush=True)
    return 0 if n_ok == len(results) else 1


def _selftest_body(chk) -> None:
    raw = (REPO / TC_RAW_REL).read_bytes()
    tc = load_task_correct(raw)
    chk(f"task_correct.py loaded from {TC_RAW_REL}: the raw's sha256 {TC_RAW_SHA256[:16]}…, the script's "
        f"{TC_SHA256[:16]}…, one header line; it defines the names this step uses",
        all(hasattr(tc, n) for n in ("KEYS", "MATCH_RULE", "READING", "SHAM_BLINDING", "correct", "load_pool",
                                     "key_table", "task_of", "tally_file", "selftest")))
    try:
        load_task_correct(raw + b"\n")
        refused = False
    except Refused:
        refused = True
    chk("a raw whose bytes differ from the pinned ones is refused before anything is loaded", refused)
    rc = tc.selftest()
    chk("task_correct.py's own rule cases pass (its selftest, imported unchanged)", rc == 0, rc)
    pool = pool_of_record(tc)
    item_key = tc.key_table(pool)
    chk("CORR_clean: m's loader and task_correct's agree (16 items); the key table maps each item to one key",
        len(pool) == 16 and sorted(item_key) == list(range(16)), sorted(item_key))
    shas = code_shas()
    chk("the packages are the lock's: p's package_sha256 and m's equal the values every LOCK-p v1.0 names",
        code_problems() == [], shas)
    chk("p's renders of record are its sha256 of record (p §1.2), the source a corrupted round is checked against",
        p_corrupt.sha_p(p_corrupt.RENDERS_OF_RECORD) == p_corrupt.RENDERS_SHA256_P)
    lex = p_report.load_lexicon()

    ruling = load_ruling()
    try:
        load_ruling(ruling.encode("utf-8") + b"\n")
        r_refused = False
    except Refused:
        r_refused = True
    chk(f"the seat's second ruling: {RULING_RAW_REL} at its sha256 ({RULING_RAW_SHA256[:16]}…), other bytes refused; "
        f"RULING_R1 and RULING_R2 verbatim in it; TC_STAGES every stage, the asserted ones G-TIME's and G-F0m's",
        r_refused and RULING_R1 in ruling and RULING_R2 in ruling and TC_STAGES == STAGES
        and TC_ASSERTED == ("qual", "time"),
        {"refused": r_refused, "r1": RULING_R1 in ruling, "r2": RULING_R2 in ruling, "tc": TC_STAGES,
         "asserted": TC_ASSERTED})

    # (1) the committed sham task_correct figures, from the reads files: by the imported tally_file, and by this step
    for stage in TC_ASSERTED:
        for u in UNITS:
            path = REPO / READS_REL.format(unit=u, stage=stage)
            chk(f"{stage} {u}: the reads file is the one the task_correct raw printed (sha256 "
                f"{READS_SHA256[stage][u][:16]}…)", _sha(path.read_bytes()) == READS_SHA256[stage][u])
            k, k_alt, n_sham, n_con = tc.tally_file(path, pool, item_key)
            want = COMMITTED_SHAM_TC[stage][u]
            got_imported = {ph: tuple(k[ph]) for ph in PHASES}
            recs, n_con2 = sham_records_from_reads(path, pool, tc)
            rows, alt = tc_rows(recs, pool, item_key, tc)
            got_step = {ph: tuple(rows["sham"][ph]) for ph in PHASES}
            got_alt = {ph: tuple(alt["sham"][ph]) for ph in PHASES}
            chk(f"{stage} {u}: the sham task_correct from the reads file, {want['forced'][0]}/{want['forced'][1]} "
                f"forced and {want['free'][0]}/{want['free'][1]} free -- by the imported tally_file and by this step's "
                f"count over the same rounds, the alternative reading beside equal to the imported one",
                got_imported == want and got_step == want and got_alt == {ph: tuple(k_alt[ph]) for ph in PHASES}
                and n_con2 == n_con and len(recs) == n_sham,
                {"imported": got_imported, "step": got_step, "alt": got_alt, "want": want})
            mine = committed_view({"counters": p_report.session_counters(recs, pool, lex)})
            rep = json.loads((REPO / P_REPORT_REL.format(unit=u, stage=stage)).read_bytes())
            theirs = committed_view(rep)
            keys = ("n_sham_rounds", "n_sham_forced_rounds", "sham", "sham_cc_texts")
            chk(f"{stage} {u}: p's own session_counters over the reads file's sham records gives the committed p "
                f"report's sham cells (round counts, the five counters' keys, the control-character texts); no "
                f"withheld cell is computed here",
                {x: mine[x] for x in keys} == {x: theirs[x] for x in keys},
                {x: (mine[x], theirs[x]) for x in keys if mine[x] != theirs[x]})

    # (2) the released-record path, on two synthetic records (one hit per named cell)
    syn = _synthetic(pool)
    for rec in syn:
        for r in rec["rounds"]:
            check_round(rec, r, pool)
    t = p23_table(syn, pool, lex)
    c = t["cells"]
    want_cells = {
        "sham forced": {"n": 2, "corrupted_spelling": ["A0s-OLMo-syn s=0 forced 1"]},
        "sham free": {"n": 3, "control_chars": ["A0s-OLMo-syn s=0 free 0"], "cap_hits": ["A0s-OLMo-syn s=0 free 1"]},
        "contrast forced": {"n": 2, "control_chars": ["A0-OLMo-syn s=1 forced 1"],
                            "harness_first_line": ["A0-OLMo-syn s=1 forced 1"],
                            "refusals": ["A0-OLMo-syn s=1 forced 0"]},
        "contrast free": {"n": 2, "control_chars": ["A0-OLMo-syn s=1 free 1"]},
    }
    got_cells = {f"{a} {ph}": {"n": c[a][ph]["n"], **{k: c[a][ph][k] for k in p_report.COUNTERS if c[a][ph][k]}}
                 for a in ARMS for ph in PHASES}
    chk("synthetic released records: p §2.3's cells by arm and phase, one hit per named cell and none elsewhere",
        got_cells == want_cells, got_cells)
    chk("synthetic released records: the hair trigger counts the one stored line break; the control-character texts "
        "are listed by key", t["hair"] == ["A0s-OLMo-syn s=0 free 2"] and t["n_rounds"] == 9
        and sorted(t["cc_texts"]) == ["A0-OLMo-syn s=1 forced 1", "A0-OLMo-syn s=1 free 1", "A0s-OLMo-syn s=0 free 0"],
        {"hair": t["hair"], "cc": sorted(t["cc_texts"]), "n": t["n_rounds"]})
    real = committed_view({"counters": p_report.session_counters(syn, pool, lex)})
    chk("synthetic released records: this step's read-domain cells equal p's own session_counters' over the same "
        "records", read_domain_view(t) == real, {"step": read_domain_view(t), "p": real})
    rows, _ = tc_rows(syn, pool, item_key, tc)
    want_rows = {"sham": {"forced": [1, 2], "free": [2, 3]}, "contrast": {"forced": [2, 2], "free": [0, 2]}}
    chk("synthetic released records: task_correct by arm and phase (77; Januwy; Cold.; 12 against 2; Seven; three; "
        "March; Shut against closed; Twenty-four against 24)", rows == want_rows, rows)
    stops = []
    for rec_i, round_i, field, value in ((0, 0, "task_text", "Compute 31 + 47."), (0, 0, "property", "corrupted"),
                                         (0, 0, "item", 16), (0, 0, "item", True),
                                         (1, 1, "task_text", p_corrupt.RENDERS_OF_RECORD[12])):
        rec = json.loads(json.dumps(syn[rec_i]))
        rec["rounds"][round_i][field] = value
        try:
            check_round(rec, rec["rounds"][round_i], pool)
            stops.append(False)
        except Stop:
            stops.append(True)
    chk("a released round not as the rule reads it STOPs: a clean round off its item's task, a corrupted round in a "
        "sham session, an item outside CORR_clean, a bool item, a corrupted round off its item's render",
        stops == [True] * 5, stops)

    # (3) the run: its gates (on bad inputs, before anything is read) and its two passes, on a scratch root
    gates = []
    for exits in ({"OLMo-sft": 0, "OLMo-dpo": 0}, {"OLMo-sft": 0, "OLMo-dpo": 2, "OLMo-instruct": 0}):
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                run(exits)
            gates.append("ran")
        except Refused as e:
            gates.append("gate 1" if "(gate 1)" in str(e) and not buf.getvalue() else f"other: {e}")
    chk("the run's gate 1 refuses, printing nothing, unless the three exit statuses are stated and each is 0",
        gates == ["gate 1", "gate 1"], gates)
    with tempfile.TemporaryDirectory(prefix="p_counters_selftest_") as td:
        root = Path(td) / "gate"
        (root / "data" / "p" / "verdicts").mkdir(parents=True)
        g0 = third_run_ended(root)
        (root / OUTPUT_RELS[0].format(unit="OLMo-sft")).write_text("{}", encoding="utf-8")
        (root / OUTPUT_RELS[0].format(unit="OLMo-dpo")).write_text("{}", encoding="utf-8")
        g2 = third_run_ended(root)
        (root / OUTPUT_RELS[1].format(unit="OLMo-instruct")).write_text("{}", encoding="utf-8")
        g3 = third_run_ended(root)
        chk("gate 2: closed with no output and with two of three, open once each unit has its VERDICTS or NOT-RUN "
            "output", (g0, g2, g3) == (False, False, True), (g0, g2, g3))
        paths = [p.relative_to(root).as_posix() for _, _, p in checkpoint_paths(root)]
        logs = [(root / CALLS_REL.format(unit=u, stage=s)).relative_to(root).as_posix() for u, s, _ in
                checkpoint_paths(root)]
        chk("the run reads nine checkpoints and nine call logs by exact path, each unit's time, qual and campaign",
            paths == [f"data/p/ckpt/{u}_{s}.json" for u in UNITS for s in STAGES]
            and logs == [f"data/p/ckpt/{u}_{s}_p-calls.jsonl" for u in UNITS for s in STAGES], (paths, logs))

        sroot = _synthetic_root(Path(td), pool, lex)
        reader = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731  SELF-TEST ONLY
        tc_syn = {s: {u: {"forced": (1, 2), "free": (2, 3)} for u in UNITS} for s in TC_ASSERTED}
        kw = dict(pool=pool, item_key=item_key, lexicon=lex, tc=tc, committed_tc=tc_syn)
        res = collect(sroot, reader, **kw)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            emit(res)
        printed = buf.getvalue()
        chk("the run's two passes on synthetic checkpoints: nine stages checked, then printed, each with its counts, "
            "its withheld cells and task_correct at every stage (R1 (c)): the contrast rows (2 of 2 forced, 0 of 2 "
            "free) at all nine, the sham rows asserted at time and qual and printed unasserted at the campaign",
            len(res) == 9 and printed.count("== ") == 9
            and printed.count("contrast forced 2 of 2, free 0 of 2, all 2 of 4") == 9
            and printed.count("task_correct (R1 (c)): sham forced 1 of 2, free 2 of 3") == 9
            and printed.count("(the committed figure: equal)") == 6
            and printed.count("(no committed figure: this is its first, not asserted)") == 3
            and printed.count("withheld at the stage report, counted here") == 9, printed[:300])
        sham_line = ("     sham: 5 of 5 rounds attributed, 1 cut(s) (A0s-OLMo-syn s=0 free 1); the committed p report's "
                     "cells: equal\n")
        con_line = "     contrast: 4 of 4 rounds attributed, 1 cut(s) (A0-OLMo-syn s=1 free 0)\n"
        per_line = ("     calls per contrast session (calls attributed to its rounds): 4 calls: A0-OLMo-syn s=1 "
                    "(1 session)\n")
        chk("the proxy (R2 (b)) on synthetic call logs in p's form, through p's attribute_calls: at all nine stages the "
            "log bound to its report by sha256, the sham cells equal the report's (written by hand), the contrast cells "
            "in the sham's form (4 of 4, the cut by key), the calls per contrast session, no STOP mark; no call's "
            "number, seed, digest or returned text printed",
            printed.count(sham_line) == 9 and printed.count(con_line) == 9 and printed.count(per_line) == 9
            and printed.count("STOP marks in the p report's run rows: none") == 9
            and printed.count(", the one its p report records; 1 run(s), 0 malformed line(s) as the report records, "
                              "9 calls, each attributed to one recorded round") == 9
            and '"call"' not in printed and "seed" not in printed and SENTINEL not in printed
            and not any(p_stage.text_sha256(r["text"]) in printed for rec in _synthetic(pool) for r in rec["rounds"]),
            printed[-900:])
        cells = proxy_cells(_synthetic(pool), _synthetic_events("OLMo-dpo", "qual", _synthetic(pool)), "syn")
        chk("proxy_cells on the synthetic records against the hand-computed sham cells (build_report's rule): the "
            "sham cells equal SYN_SHAM_PROXY; the contrast 4 of 4 with one cut; one contrast session with 4 calls",
            cells["cells"]["sham"] == SYN_SHAM_PROXY
            and cells["cells"]["contrast"] == {"n_rounds": 4, "n_attributed": 4, "n_cuts": 1,
                                               "cut_keys": ["A0-OLMo-syn s=1 free 0"], "unattributed_keys": []}
            and cells["per_session"] == {("A0-OLMo-syn", 1): 4} and cells["n_calls"] == 9, cells)
        chk("calls_by_count groups the sessions by their number of calls, every index kept: 10 calls for s=0-3 and 5, "
            "7 for s=4; a run ending at the last index stays one run (4 calls for s=0-1)",
            calls_by_count({("A0-x", 0): 10, ("A0-x", 1): 10, ("A0-x", 2): 10, ("A0-x", 3): 10, ("A0-x", 4): 7,
                            ("A0-x", 5): 10})
            == ["10 calls: A0-x s=0-3, 5 (5 sessions)", "7 calls: A0-x s=4 (1 session)"]
            and calls_by_count({("A0-x", 0): 4, ("A0-x", 1): 4}) == ["4 calls: A0-x s=0-1 (2 sessions)"])

        saved_view = globals()["read_domain_view"]

        def off_by_one(t_):
            v = saved_view(t_)
            v["n_sham_rounds"] += 1
            return v
        globals()["read_domain_view"] = off_by_one
        out_ = io.StringIO()
        try:
            with contextlib.redirect_stdout(out_):
                collect(sroot, reader, **kw)
            step_stop = "ran"
        except Stop as e:
            step_stop = ("stop" if "this step's read-domain cells differ" in str(e) and not out_.getvalue()
                         else f"other: {e}")
        finally:
            globals()["read_domain_view"] = saved_view
        chk("pass 1 STOPs, printing nothing, when this step's table differs from a report p's session_counters "
            "reproduces (the step-table branch)", step_stop == "stop", step_stop)

        def reader_refuses(p):
            raise SystemExit("CHECKPOINT UNREADABLE (synthetic)")

        def reader_missing(p):
            raise FileNotFoundError("synthetic: no such file")
        guarded = []
        for rdr in (reader_refuses, reader_missing):
            try:
                collect_guarded(sroot, rdr, **kw)
                guarded.append("ran")
            except Stop:
                guarded.append("stop")
            except SystemExit:
                guarded.append("refused")
        chk("after the gates, a failure that is not a STOP -- m's reader's own refusal, a missing file -- is a STOP, "
            "never a refusal", guarded == ["stop", "stop"], guarded)

        def stops_silently(mutate) -> str:
            """A fresh synthetic root, mutated, through pass 1: 'stop: <its message>' when it STOPs printing nothing."""
            mdir = Path(td) / "m"
            if mdir.exists():
                shutil.rmtree(mdir)
            mdir.mkdir()
            m_root = _synthetic_root(mdir, pool, lex)
            kw2 = dict(kw)
            mutate(m_root, kw2)
            out = io.StringIO()
            try:
                with contextlib.redirect_stdout(out):
                    collect(m_root, reader, **kw2)
                return "ran"
            except Stop as e:
                return ("stop: " + str(e)) if not out.getvalue() else "stop, but printed"

        def stopped_as(got_: dict, want_: dict) -> bool:
            return all(got_[k].startswith("stop: ") and want_[k] in got_[k] for k in want_)

        def edit_report(root_, fn, u="OLMo-sft", s="time"):
            rp = root_ / P_REPORT_REL.format(unit=u, stage=s)
            d = json.loads(rp.read_text(encoding="utf-8"))
            fn(d)
            rp.write_text(json.dumps(d), encoding="utf-8")

        def edit_ckpt(root_, fn, u="OLMo-dpo", s="campaign"):
            """Edit a synthetic checkpoint and re-record it in its report (sha256, and the counters p's own
            session_counters gives over its sessions), so the case reaches its own check."""
            cp_ = root_ / CKPT_REL.format(unit=u, stage=s)
            d = json.loads(cp_.read_text(encoding="utf-8"))
            fn(d)
            data = json.dumps(d).encode("utf-8")
            cp_.write_bytes(data)
            edit_report(root_, lambda r: r.update(checkpoint={"path": "x", "sha256": _sha(data)},
                                                  counters=p_report.session_counters(d["sessions"], pool, lex)),
                        u=u, s=s)

        def bad_sha(root_, kw2):
            edit_report(root_, lambda d: d["checkpoint"].update(sha256="0" * 64), u="OLMo-instruct", s="campaign")

        def bad_cell(root_, kw2):
            edit_report(root_, lambda d: d["counters"]["sham"].update(
                refusals={"n": 1, "keys": ["A0s-OLMo-syn s=0 free 1"], "domain": "every sham round"}),
                u="OLMo-dpo", s="qual")

        def bad_ident(root_, kw2):
            edit_ckpt(root_, lambda d: d["identity"].update(stage="qual"), u="OLMo-dpo", s="time")

        def bad_tc(root_, kw2):
            kw2["committed_tc"] = {s: {u: {"forced": (2, 2), "free": (2, 3)} for u in UNITS} for s in TC_ASSERTED}

        def bad_pkg(root_, kw2):
            kw2["campaign_pkg"] = "f" * 64

        want = {"sha": "does not record data/p/ckpt/OLMo-instruct_campaign.json's sha256",
                "cell": "p's session_counters over the released records differs",
                "identity": "is OLMo-dpo/qual, not OLMo-dpo/time",
                "task_correct": "the sham task_correct recount is not the committed figure",
                "package": "was not built by the lock's p package"}
        got = {name: stops_silently(fn) for name, fn in (("sha", bad_sha), ("cell", bad_cell), ("identity", bad_ident),
                                                         ("task_correct", bad_tc), ("package", bad_pkg))}
        chk("pass 1 STOPs before anything is printed, each with its own message: a p report not recording its "
            "checkpoint's sha256, a read-domain cell that differs, a checkpoint naming another stage, a sham "
            "task_correct row off its committed figure, a campaign report built by another p package",
            stopped_as(got, want), got)

        # the call logs (R2 (b)): each defect a silent STOP in pass 1, each with its own message
        def log_of(root_, u="OLMo-instruct", s="campaign"):
            return root_ / CALLS_REL.format(unit=u, stage=s)

        def edit_log(root_, fn, u="OLMo-instruct", s="campaign", record=True):
            """Edit a synthetic call log; re-record its sha256 in its report unless record is False."""
            p_ = log_of(root_, u, s)
            evs = [json.loads(x) for x in p_.read_text(encoding="ascii").splitlines()]
            _write_events(p_, fn(evs))
            if record:
                edit_report(root_, lambda d: d["call_log"].update(sha256=_sha(p_.read_bytes())), u=u, s=s)

        def append_line(root_, line, u="OLMo-instruct", s="campaign"):
            p_ = log_of(root_, u, s)
            p_.write_text(p_.read_text(encoding="ascii") + line, encoding="ascii")
            edit_report(root_, lambda d: d["call_log"].update(sha256=_sha(p_.read_bytes())), u=u, s=s)

        def call_like(seed, text, n=99):
            return {"event": "call", "run": 1, "call": n, "seed": seed, "text_sha256": p_stage.text_sha256(text),
                    "cut": None}

        stop_call = {"event": "call", "run": 1, "call": 9, "seed": 999,
                     "stop": {"message": "PROXY STOP: synthetic", "returned_text": SENTINEL, "stored_text": None}}

        def log_unrecorded(root_, kw2):
            edit_log(root_, lambda evs: evs[:-1] + [call_like(999, "x"), evs[-1]], record=False)

        def log_orphan(root_, kw2):
            edit_log(root_, lambda evs: evs[:-1] + [call_like(999, "x"), evs[-1]])

        def log_stop_call(root_, kw2):
            edit_log(root_, lambda evs: evs[:-1] + [stop_call, evs[-1]])

        def log_rerun(root_, kw2):
            edit_log(root_, lambda evs: evs[:-1] + [call_like(101, "77"), evs[-1]])

        def log_other_stage(root_, kw2):
            edit_log(root_, lambda evs: [{**evs[0], "stage": p_stage.label("OLMo-dpo", "qual")}] + evs[1:],
                     u="OLMo-dpo", s="time")

        def log_malformed(root_, kw2):
            append_line(root_, "not a JSON line\n")

        def log_absent(root_, kw2):
            log_of(root_, u="OLMo-sft", s="qual").unlink()

        def log_package(root_, kw2):
            edit_log(root_, lambda evs: [{**evs[0], "p_package_sha256": "e" * 64}] + evs[1:], u="OLMo-sft", s="qual")

        def report_sham_cell(root_, kw2):
            edit_report(root_, lambda d: d["proxy"]["sham"].update(n_cuts=0))

        def report_runs(root_, kw2):
            edit_report(root_, lambda d: d["call_log"].update(n_runs=2), u="OLMo-dpo", s="campaign")

        def report_complete(root_, kw2):
            edit_report(root_, lambda d: d["proxy"].update(attribution_complete=False), u="OLMo-dpo", s="qual")

        def seed_shared(root_, kw2):
            edit_ckpt(root_, lambda d: d["sessions"][1]["rounds"][3].update(seed=203))

        def seed_none(root_, kw2):
            edit_ckpt(root_, lambda d: d["sessions"][0]["rounds"][0].update(seed=None))
            edit_log(root_, lambda evs: [e for e in evs if e.get("seed") != 101], u="OLMo-dpo", s="campaign")

        def index_not_int(root_, kw2):
            edit_ckpt(root_, lambda d: d["sessions"][1].update(s="1"))

        def session_twice(root_, kw2):
            twin = {"contrast": True, "template": "A0-OLMo-syn", "s": 1, "rounds": [
                {"phase": "forced", "ri": 0, "item": 0, "property": "clean", "task_text": pool[0]["task"],
                 "text": "77", "cap_hit": False, "seed": 301}]}
            edit_ckpt(root_, lambda d: d["sessions"].append(twin))

        want = {"an unrecorded log": "does not record data/p/ckpt/OLMo-instruct_campaign_p-calls.jsonl's sha256",
                "an orphan call": "attributed to no recorded round",
                "a STOP call line": "attributed to no recorded round",
                "a re-run call": "(a re-run)",
                "another stage's run line": "is not this stage's",
                "a malformed line": "1 malformed line(s) by p's read_calls",
                "an absent log": "data/p/ckpt/OLMo-sft_qual_p-calls.jsonl: absent",
                "another p package": "ran under p package",
                "a sham proxy cell": "the sham arm's proxy cells differ",
                "the report's run count": "holds 1 run(s); data/p/reports/OLMo-dpo_campaign_p-report.json records 2",
                "the report's attribution flag": "attribution_complete does not match",
                "two rounds sharing a seed": "p's attribute_calls reports ['two recorded rounds share a seed",
                "a round with no int seed": "p's attribute_calls reports ['a recorded round carries no int seed",
                "a session index not an int": "a contrast session's index is '1' (not an int, or twice)",
                "a contrast session twice": "a contrast session's index is 1 (not an int, or twice)"}
        got = {name: stops_silently(fn) for name, fn in (
            ("an unrecorded log", log_unrecorded), ("an orphan call", log_orphan), ("a STOP call line", log_stop_call),
            ("a re-run call", log_rerun), ("another stage's run line", log_other_stage),
            ("a malformed line", log_malformed), ("an absent log", log_absent), ("another p package", log_package),
            ("a sham proxy cell", report_sham_cell), ("the report's run count", report_runs),
            ("the report's attribution flag", report_complete), ("two rounds sharing a seed", seed_shared),
            ("a round with no int seed", seed_none), ("a session index not an int", index_not_int),
            ("a contrast session twice", session_twice))}
        chk("pass 1 STOPs before anything is printed on a call log not as the rule reads it, each with its own message: "
            "a log its report does not record, a call attributed to no round (an orphan; a proxy STOP line), a call "
            "matching an attributed round, a run line of another stage, a malformed line the report does not record, "
            "an absent log, runs under a p package the report does not name, a sham cell or run count or attribution "
            "flag the report records otherwise, two rounds sharing a seed, a round with no int seed, a contrast "
            "session index not an int or twice; no message carries a log line's position or a returned text",
            stopped_as(got, want) and not any(SENTINEL in v or "not JSON" in v for v in got.values()), got)

        real_read_calls = p_stage.read_calls

        def touching_read_calls(path):
            res_ = real_read_calls(path)
            if Path(path).name == "OLMo-sft_time_p-calls.jsonl":
                with open(path, "ab") as fh:
                    fh.write(b"\n")
            return res_
        mdir = Path(td) / "m3"
        m3 = _synthetic_root(mdir, pool, lex)
        p_stage.read_calls = touching_read_calls
        out3 = io.StringIO()
        try:
            with contextlib.redirect_stdout(out3):
                collect(m3, reader, **kw)
            touched = "ran"
        except Stop as e:
            touched = "stop: " + str(e) if not out3.getvalue() else "stop, but printed"
        finally:
            p_stage.read_calls = real_read_calls
        chk("pass 1 STOPs, printing nothing, when a call log's bytes change while p's read_calls reads it (p's "
            "read_calls restored after)",
            touched.startswith("stop: ") and "data/p/ckpt/OLMo-sft_time_p-calls.jsonl: the log changed while it was "
            "read" in touched and p_stage.read_calls is real_read_calls, touched)

        mdir = Path(td) / "m2"
        m2 = _synthetic_root(mdir, pool, lex)
        edit_log(m2, lambda evs: [e for e in evs if e.get("seed") != 204], u="OLMo-dpo", s="campaign")
        append_line(m2, "not a JSON line\n", u="OLMo-sft", s="time")
        edit_report(m2, lambda d: d["call_log"].update(well_formed=False, n_malformed_lines=1))
        out2 = io.StringIO()
        with contextlib.redirect_stdout(out2):
            emit(collect(m2, reader, **kw))
        p2 = out2.getvalue()
        dpo_c = p2[p2.index("== OLMo-dpo / campaign"):p2.index("== OLMo-instruct / time")]
        sft_t = p2[p2.index("== OLMo-sft / time"):p2.index("== OLMo-sft / qual")]
        chk("printed, not stopped (Code's reading of the sham cells' form): a contrast round with no call -- at that "
            "stage the contrast cell reads 3 of 4 attributed with the round's key, and its session 3 calls; a malformed "
            "line the report records -- its count printed; every other stage as before",
            "contrast: 3 of 4 rounds attributed, 1 cut(s) (A0-OLMo-syn s=1 free 0); unattributed: A0-OLMo-syn s=1 "
            "free 1\n" in dpo_c and "4 calls: A0-OLMo-syn s=1" not in dpo_c and "3 calls: A0-OLMo-syn s=1 (1 session)"
            in dpo_c and p2.count(con_line) == 8 and "8 calls, each attributed" in dpo_c
            and "1 run(s), 1 malformed line(s) as the report records, 9 calls" in sft_t
            and p2.count("0 malformed line(s) as the report records") == 8 and SENTINEL not in p2, dpo_c[-700:])
    src = Path(__file__).read_text(encoding="utf-8")
    chk("this script's source makes no directory-listing call: it reads files by exact path (the package hashes it "
        "imports list their own package directories; nothing under data/p/ckpt is listed)",
        not any(x in src for x in _LISTING_CALLS), [x for x in _LISTING_CALLS if x in src])


def _exits(values: list[str] | None) -> dict:
    out: dict = {}
    for v in values or []:
        u, sep, code = v.partition("=")
        if not sep or u in out or u not in UNITS:
            raise Refused(f"REFUSED (gate 1): --exit takes UNIT=STATUS once per unit, UNIT one of {UNITS}: {v!r}")
        try:
            out[u] = int(code)
        except ValueError:
            raise Refused(f"REFUSED (gate 1): {v!r}: the status is not an integer") from None
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="p's counters at VERDICTS (Code's own step; the seat's answers of "
                                             "2026-11-16, §3 and §4)")
    ap.add_argument("--selftest", action="store_true", help="the self-test: never a checkpoint, call log or p output")
    ap.add_argument("cmd", nargs="?", choices=["run"], help="run: after the third run ends")
    ap.add_argument("--exit", action="append", metavar="UNIT=STATUS",
                    help="run: each end notice's exit status, once per unit (gate 1)")
    a = ap.parse_args(argv)
    try:
        if a.selftest:
            return run_selftest()
        if a.cmd == "run":
            return run(_exits(a.exit))
        ap.print_usage(sys.stderr)
        return 2
    except Refused as e:
        print(_scrub(str(e)), file=sys.stderr, flush=True)
        return 2
    except Stop as e:
        print(_scrub(str(e)), file=sys.stderr, flush=True)
        return 4
    except (SystemExit, OSError) as e:          # an input not as pinned or unreadable (m's, p's or task_correct's)
        print(_scrub(f"REFUSED: {type(e).__name__}: {e}"), file=sys.stderr, flush=True)
        return 2
    except Exception as e:                      # noqa: BLE001  anything else: a STOP, its message scrubbed
        print(_scrub(f"STOP: unexpected {type(e).__name__}: {e}"), file=sys.stderr, flush=True)
        return 4


if __name__ == "__main__":
    sys.exit(main())
