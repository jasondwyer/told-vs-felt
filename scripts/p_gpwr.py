#!/usr/bin/env python3
"""G-PWR (p): m:285 for PROPOSAL-p's three OLMo units, OLMo-{sft,dpo,instruct} (p v0.2 §4.1, §8 step 6).

    <python> -I -B -X pycache_prefix=<a path that does not exist> scripts/p_gpwr.py --selftest
    <python> -I -B -X pycache_prefix=<a path that does not exist> scripts/p_gpwr.py --record data/p/gates/G-PWR-p.json

On the seat's read of G-F0m-OLMo (p) x3 (results/raw/2026-11-12_p-qual_design-to-code_answers.md, committed at
a2c354e), §4.3 item 1, verbatim: "G-PWR (p), model-free, now: m:192's launch rule per arm from each checkpoint's k on
the primary's domain over its 24 qualification sessions — sft 23 (the forced-round exclusion), dpo 24, instruct 24 —
at m:205's basis, m:206–214's rows, looks ⌈total/40⌉, the sequential false-pause probabilities and the exclusion
guard's figure (m:285); the PI's cap share per checkpoint within p's 12 h budget (p §6.1), decided at G-PWR as p §4.1
has it. The sham seconds (102.1, 88.4, 85.2 s over sixteen) are reported beside, no basis."

A sibling of scripts/m_gpwr.py whose functions it imports unchanged (READINGS item 1): m_gpwr's bytes are executed from
the load commit's blob as the module m_gpwr, its commit pinned to the load commit, and its own startup then executes
valence_core.m from that commit's blobs, as at Q-F0's G-PWR. No attribute of an m module is substituted. Model-free
and exact (Fractions throughout; no float enters a comparison). Not a stages.py stage: it reads no checkpoint, report
or session record, and it moves no file a lock names. The cap share is the PI's; this program sets none.

Inputs of record (each bound to the committed text it is quoted from: build_sources() builds every quote from the
constants this program computes with, and sources_record() requires each quote verbatim in its text at its commit,
so a constant that differs from its text refuses the run):
  - k of n_q = 24 per checkpoint: sft 23, dpo 24, instruct 24 (the seat's §4.3 item 1);
  - beside, per template (m:192): A0s 16 of 16 at each checkpoint (the G-F0m-OLMo (p) x3 entry, a225a89), so A0 =
    k - 16 of 8;
  - the floors A0-OLMo 80, A0s-OLMo 32 (schedule.FLOORS; p:84 "floors 80/32"), the balance unit 32, a look every 40
    launches and at the end (resume.LOOK_EVERY);
  - the bars of record, bars.OLMO_BARS(ckpt)'s campaign rows (m:316, m:330): round_degeneracy p0 .02 alpha .05 on the
    sham arm's rounds, binding; the guard's Fisher half alpha .05, binding; its absolute half p0 .20 alpha .05,
    reported only on OLMo;
  - the sham's realised rounds at G-F0m-OLMo (p): 160 of 160 at each checkpoint (the entry);
  - m:205's OLMo basis, 22.7 s per session at SFT/DPO and 19.5 s at instruct, applied to the unit's total + 26;
  - beside, no basis: the sham seconds, m's report's sum over the sixteen sham sessions (the entry's table).
"""
from __future__ import annotations

import os
import sys
if __name__ == "__main__" and not sys.flags.isolated:      # before any import a script directory could shadow
    raise SystemExit("REFUSED: G-PWR (p) runs in isolated mode (python -I): no script directory, user site or "
                     "environment path enters the import path")
if __name__ == "__main__" and (not sys.pycache_prefix or os.path.exists(sys.pycache_prefix)):
    raise SystemExit("REFUSED: G-PWR (p) reads no cached bytecode: run with -X pycache_prefix=<a path that does not "
                     "exist>, so every module is compiled from the bytes provenance binds")

import argparse
import hashlib
import io
import json
import subprocess
import types
from contextlib import redirect_stdout
from fractions import Fraction
from math import ceil
from pathlib import Path
from types import SimpleNamespace

REPO = Path(__file__).resolve().parents[1]
SELF_REL, M_REL, ANALYZER_REL = "scripts/p_gpwr.py", "scripts/m_gpwr.py", "scripts/m_analyze.py"
GIT = ("git", "--no-replace-objects", "-C", str(REPO))   # no replace ref can stand another object in for a bound one
_GIT_ENV = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}   # no GIT_DIR, index or object store


class _GitRead(Exception):
    """A git read that failed: the run refuses, stating it."""


def _git_bytes(*args: str) -> bytes:
    r = subprocess.run([*GIT, *args], env=_GIT_ENV, capture_output=True)
    if r.returncode != 0:
        raise _GitRead(f"git {' '.join(args)} exited {r.returncode}: "
                       f"{r.stderr.decode('utf-8', 'replace').strip()[:300]}")
    return r.stdout


def _git_text(*args: str) -> str:
    return _git_bytes(*args).decode("utf-8")


def _blob_id(data: bytes, like: str) -> str:
    return hashlib.new("sha1" if len(like) == 40 else "sha256", b"blob %d\0" % len(data) + data).hexdigest()


def _commit_of(rev: str) -> str:
    return _git_text("rev-parse", "--verify", "--quiet", f"{rev}^{{commit}}").strip()


def _commit_blob(commit: str, rel: str) -> tuple[str, bytes]:
    """rel's blob id and bytes in commit's tree, the bytes checked to hash to the id."""
    oid = _git_text("rev-parse", "--verify", "--quiet", f"{commit}:{rel}").strip()
    data = _git_bytes("cat-file", "blob", oid)
    if _blob_id(data, oid) != oid:
        raise _GitRead(f"{rel}: the bytes read do not hash to the blob {oid}")
    return oid, data


def _load_m_gpwr(commit: str):
    """scripts/m_gpwr.py's bytes in commit's tree, executed as the module m_gpwr with its commit pinned to commit."""
    oid, src = _commit_blob(commit, M_REL)
    mod = types.ModuleType("m_gpwr")
    mod.__file__ = str(REPO / M_REL)
    mod._GPWR_COMMIT = commit
    sys.modules["m_gpwr"] = mod
    exec(compile(src, mod.__file__, "exec", dont_inherit=True), mod.__dict__)
    return mod, oid


_PINNED = globals().get("_PGPWR_COMMIT")             # set only by the self-test child's bootstrap (_P_CHILD_BOOT)
try:
    _LOAD_COMMIT = _commit_of(_PINNED or "HEAD")
    if _PINNED and _LOAD_COMMIT != _PINNED:
        raise _GitRead(f"the self-test's commit {_PINNED!r} does not resolve to itself")
    M, M_BLOB = _load_m_gpwr(_LOAD_COMMIT)
except (_GitRead, ImportError) as e:
    if __name__ == "__main__":
        raise SystemExit(f"REFUSED: {e}")
    raise
if M._LOAD_COMMIT != _LOAD_COMMIT:
    raise SystemExit(f"REFUSED: m_gpwr resolved {M._LOAD_COMMIT}, not the load commit {_LOAD_COMMIT}")
bars, resume, schedule = M.bars, M.resume, M.schedule
from valence_core.m import keys  # noqa: E402  (through m_gpwr's finder: the load commit's blob)

SCHEMA = "p-gpwr-v1"
PROPOSAL = "PROPOSAL-p"
CKPTS = ("sft", "dpo", "instruct")
PATH = "uncached"                                    # each LOCK-p v0.1's §0 line; the seat's p answers of 2026-11-09
K = {"sft": 23, "dpo": 24, "instruct": 24}           # the seat's §4.3 item 1
N_Q = schedule.N_Q                                   # 24 (m:192: "n_q = 24 for Q-F0 and each OLMo checkpoint")
CONTRAST_N, SHAM_N, SHAM_VALID = 8, 16, 16           # qual's counts per checkpoint; the entry: "16 of 16" valid
ARMS = M.ARMS                                        # m's arm roles (A0, A0s), contrast first
FLOOR = {"A0": schedule.FLOORS["A0-OLMo"], "A0s": schedule.FLOORS["A0s-OLMo"]}
SHAM_ROUNDS_REALISED = (160, 160)                    # each checkpoint's sham arm at G-F0m-OLMo (p): realised / planned
BASIS_S = {"sft": Fraction(227, 10), "dpo": Fraction(227, 10), "instruct": Fraction(39, 2)}   # m:205 [C]
GATE_SESSIONS = 26                                   # m:205: "+ 26 sessions per checkpoint (24 qualification + 2 timing)"
SHAM_SECONDS_BESIDE = {"sft": "102.105", "dpo": "88.389", "instruct": "85.237"}   # the entry's table; no basis
BUDGET_H = 12                                        # p §6.1: "The budget is 12 h"
NONEXISTENT_PYCACHE = "/nonexistent-p-gpwr-pycache"  # the self-test's children, when this process was given none
GUARD_FIGURE = {("abs", "fisher"): "union", ("fisher",): "fisher", ("abs",): "abs"}
CASE_ORDER = ("projection", "sham_at_floor_r", "sham_at_floor_min", "sham_realised_rounds")   # m_gpwr.compute's order
CAP_SHARE = ("the PI's, per checkpoint, within p's 12 h budget, decided at G-PWR (p §4.1, §6.1; the seat's read of "
             "G-F0m-OLMo (p) x3, §4.3 item 1 and §8 item 4); not set by this program")
POWER_BASIS = ("m:190's base case: A0 split n/2 per map at clean share .70, the sham pooled at .5, alpha .01 "
               "(m_analyze.power_exact), at p's planned floors A0-OLMo 80 and A0s-OLMo 32")
PIN3_BASIS = ("PIN-3's base case re-derived at the planned floors (Q7; R1 C6), as at Q-F0: the analyzer's power_block "
              "at n = 80 split [40, 40] at clean share .70, the sham pooled at mS = 32 at .5, alpha .01. A planning "
              "figure; the figure of record for the verdict sentences is the attained power at the realised n, "
              "reported in VERDICTS (m:190).")
NOT_FIGURED = {"hair_triggers": "no p0: a ~zero-base-rate class whose fire stops the stage (m:271); p's added "
                                "line_break_in_stored_text likewise",
               "lexical": "no domain on OLMo: every banner names labels; reported only (m:330)"}

READINGS = [
    "The form: a sibling script importing scripts/m_gpwr.py's functions unchanged, executed from the load commit's "
    "blob. The seat's F-5 (results/raw/2026-11-06_ganl-f3_design-to-code_answers.md) rules this form for Q-F3's G-PWR; "
    "Code applies it to p, reading p v0.2 §4.2's \"m's modules imported unchanged by import, never by copy\" as "
    "covering m's G-PWR script. No attribute of an m module is substituted.",
    "Q7's methods (the seat's step-15 answers, results/raw/2026-10-14_m-design-to-code_step15_answers.md) are carried "
    "to p's three units by p v0.2 §4.1 (every m sentence about OLMo-{ckpt} read with p's unit in its place). Code's "
    "reading, declared here for the seat; a strike recomputes figures only.",
    "The guard on OLMo: m:316 makes the absolute half reported only on OLMo (bars.OLMO_BARS: binding false), so the "
    "guard's pausing figure is the Fisher half's own, computed as Q7 (b) computes it at the common null rate .20, with "
    "its grid and refined maximum beside; the absolute half's figure and the union are reported beside, in Q7 (b)'s "
    "form. The joint's guard beside is the Fisher half's. The pausing halves are read from the bars' binding flags.",
    "Q7 (a)'s cases: the sham arm at its floor at ceil(32 / r) and at 32, Code's reading at Q-F0 kept: 34 at sft's "
    "r = 23/24; 32 at r = 1 (dpo, instruct), where the two cases coincide. The realised-rounds case is G-F0m-OLMo "
    "(p)'s 160 of 160 sham rounds at each checkpoint, 10 per sham launch, equal to the projection's; it is computed "
    "and reported as such.",
    "round_degeneracy at OLMo's p0 .02: m_gpwr.degeneracy holds Qwen's p0 .05 as a module constant, so this program "
    "computes the same three fields by the same bars calls (critical_k, seq_false_pause) at the p0 and alpha of "
    "bars.OLMO_BARS' campaign row; the self-test asserts equality with m_gpwr.degeneracy at Qwen's p0.",
    "The projection is m_gpwr.project's, over m's arm roles A0 and A0s; the self-test asserts the same launch "
    "sequence from schedule.interleave over each OLMo unit's own arms, A0-OLMo-{ckpt} and A0s-OLMo-{ckpt}.",
    "k is the seat's (§4.3 item 1). Beside it, per template (m:192): A0s 16 of 16 at each checkpoint (the G-F0m-OLMo "
    "(p) x3 entry, a225a89), so A0 = k - 16 of 8: 7/8 at sft, 8/8 at dpo and instruct.",
    "The hours: m:205's OLMo basis (22.7 s per session at SFT and DPO, 19.5 s at instruct) applied to each unit's "
    "total + 26 sessions, as m:209-212's OLMo column, and their sum beside p §6.1's 12 h budget. The sham seconds "
    "are reported beside, no basis (§4.3 item 1).",
    "The cap share per checkpoint is the PI's at G-PWR (p §4.1, §6.1; the seat's §8 item 4: [your call at G-PWR]); "
    "this program sets none.",
    "m:190's raise is not triggered: power at the floors is at least .85 at each unit. Had it been below, this "
    "program would stop and escalate. The planning row (m:209: k 24-21, L 96 and 64, total 160, 4 looks) stands as "
    "each unit's input and is recomputed here, with PIN-3's base case at the planned floors, as at Q-F0.",
]

# m:209-214's planning rows (the oracles): k range -> (L A0, L A0s, total, looks, the Qwen hours column, kept only to
# bind the row's text); m:214's totals; m:209-212's OLMo hours column (instruct, SFT/DPO) at one place; m:214's
# three-checkpoint sums. Every one is bound to PROPOSAL-m's text by build_sources().
TABLE_ROWS = {range(21, 25): (96, 64, 160, 4, "21.7"), range(17, 21): (128, 64, 192, 5, "26.0"),
              range(14, 17): (160, 64, 224, 6, "30.4"), range(12, 14): (192, 96, 288, 8, "39.0")}
TABLE_TOTALS = {11: 320, 10: 320, 9: 384, 8: 416, 7: 480, 6: 544, 5: 640, 1: 3168}
TABLE_HOURS = {160: ("1.0", "1.2"), 192: ("1.2", "1.4"), 224: ("1.4", "1.6"), 288: ("1.7", "2.0")}
TABLE_SUMS = {160: "3.4", 192: "3.9", 224: "4.5"}
# The G-F0m-OLMo (p) x3 entry's table rows (a225a89): the columns this program does not use, kept to bind the row's
# text (sham cap hits, the proxy's word, contrast forced rounds, the forced-round exclusions).
ENTRY_ROW_REST = {"sft": ("1", " attributed", "29", "1 (lexical)"), "dpo": ("0", "", "32", "0"),
                  "instruct": ("0", "", "32", "0")}
ANSWERS_SHA256 = "a32d4d17c9d17d7920539f8c7e6945e8a71712bb76ba2f0154e22f3dbb9e1112"   # the routing's relay; a2c354e
PROPOSAL_M_SHA256 = "42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b"  # named by each LOCK-p v0.2
PROPOSAL_P_SHA256 = "42f2977b941bc016d3155ba9e34828f1b050121d9f18a9e3307e3f7023cf3b32"  # named by each LOCK-p v0.2

# The reviewed figures: per case, the stop, the sham rounds n_j, crit_j and the false pause at OLMo's p0 .02, the
# guard's looks, absolute crits and its three figures at .20 (abs, Fisher, union), and the grid's maxima. The blind
# review recomputed every one on the standard library alone; the run's out-of-process verifier, also on the standard
# library alone, recomputes all but the Fisher half, the union and the grid maxima. sft's floor case is ceil(32 / r)
# = 34; at r = 1 it is 32.
_C64 = {"stop": {"A0": 96, "A0s": 64}, "n_j": [200, 400, 600, 640], "crit_j": [8, 14, 19, 20], "fp": "0.0863",
        "n1n2": [[20, 20], [40, 40], [60, 60], [96, 64]], "abs_crit_j": [8, 13, 18, 27],
        "guard": ("0.0929", "0.0699", "0.1311")}
_C34 = {"stop": {"A0": 96, "A0s": 34}, "n_j": [200, 340, 340, 340], "crit_j": [8, 12, 12, 12], "fp": "0.0705",
        "n1n2": [[20, 20], [46, 34], [86, 34], [96, 34]], "abs_crit_j": [8, 15, 24, 27],
        "guard": ("0.0868", "0.0553", "0.1198")}
_C32 = {"stop": {"A0": 96, "A0s": 32}, "n_j": [200, 320, 320, 320], "crit_j": [8, 12, 12, 12], "fp": "0.0609",
        "n1n2": [[20, 20], [48, 32], [88, 32], [96, 32]], "abs_crit_j": [8, 15, 25, 27],
        "guard": ("0.0873", "0.0545", "0.1198")}
REVIEWED = {c: {"projection": _C64, "sham_at_floor_r": _C34 if c == "sft" else _C32, "sham_at_floor_min": _C32,
                "sham_realised_rounds": _C64} for c in ("sft", "dpo", "instruct")}
REVIEWED_GRID = {"max": ("0.0768", "1/2"), "refined": ("0.0768", "251/500", ["49/100", "51/100"]),
                 "union_le_p0": ("0.1311", "1/5")}
REVIEWED_RULE = {c: {"A0": {"floor": 80, "ceil_1.15_floor": 92, "N90": 86 if c == "sft" else 80, "L": 96},
                     "A0s": {"floor": 32, "ceil_1.15_floor": 37, "N90": 35 if c == "sft" else 32, "L": 64}}
                 for c in ("sft", "dpo", "instruct")}
# The power at the floors 80/32 is Q-F0's uncached figure: m_gpwr's own pin of its exact value's sha256.
POWER_EXACT_SHA256 = "cf7dd3ea9f9c040c7a1d2bea711764088948654b9316ecd47e40ec1d575d4346"


def build_sources(over: dict | None = None) -> tuple:
    """The committed texts the inputs are quoted from: (revision, path, the blob's sha256 or None, the quotes it must
    carry), every quote built from the constants this program computes with (over: the self-test's perturbations). A
    revision "LOAD" is the load commit."""
    v = {"K": K, "SHAM_SECONDS_BESIDE": SHAM_SECONDS_BESIDE, "SHAM_VALID": SHAM_VALID, "SHAM_N": SHAM_N,
         "CONTRAST_N": CONTRAST_N, "SHAM_ROUNDS_REALISED": SHAM_ROUNDS_REALISED, "BASIS_S": BASIS_S,
         "GATE_SESSIONS": GATE_SESSIONS, "BUDGET_H": BUDGET_H, "PATH": PATH, "FLOOR": FLOOR, "TABLE_ROWS": TABLE_ROWS,
         "TABLE_TOTALS": TABLE_TOTALS, "TABLE_HOURS": TABLE_HOURS, "TABLE_SUMS": TABLE_SUMS,
         "ANSWERS_SHA256": ANSWERS_SHA256, "PROPOSAL_M_SHA256": PROPOSAL_M_SHA256,
         "PROPOSAL_P_SHA256": PROPOSAL_P_SHA256, "ENTRY_ROW_REST": ENTRY_ROW_REST}
    v.update(over or {})
    k, ss, R, B, T, S = (v["K"], v["SHAM_SECONDS_BESIDE"], v["SHAM_ROUNDS_REALISED"][0], v["BASIS_S"],
                         v["TABLE_TOTALS"], v["TABLE_SUMS"])
    seat_s = ", ".join(M.dec(Fraction(ss[c]), 1) for c in CKPTS)
    rest = v["ENTRY_ROW_REST"]
    rows_entry = tuple(
        f"| {c} | 0/{R} | 0 | {v['SHAM_VALID']} of {v['SHAM_N']} | {rest[c][0]} | all 0 | "
        f"{R}/{R}{rest[c][1]}, 0 cuts | {ss[c]} | {rest[c][2]} | {rest[c][3]} | 0 of {rest[c][2]} |" for c in CKPTS)
    rows_m = tuple(f"| {max(rg)}–{min(rg)} | {a0} | {a0s} | **{tot}** | {lk} | {qh} | {v['TABLE_HOURS'][tot][0]} / "
                   f"{v['TABLE_HOURS'][tot][1]} |" for rg, (a0, a0s, tot, lk, qh) in v["TABLE_ROWS"].items())
    m214 = (f"(k = 11–10: {T[11]}; 9: {T[9]}; 8: {T[8]}; 7: {T[7]}; 6: {T[6]}; 5: {T[5]}; … 1: {T[1]:,}. Three "
            f"checkpoints at 160/192/224 ≈ {S[160]}/{S[192]}/{S[224]} h of generation.)")
    locks = tuple(("LOAD", f"LOCK-p-OLMo-{c}.md", None,
                   (f"2. **The path:** {v['PATH']} (m:267; each LOCK-p v0.1's §0 line)", v["PROPOSAL_M_SHA256"],
                    v["PROPOSAL_P_SHA256"])) for c in CKPTS)
    return (
        ("a2c354e", "results/raw/2026-11-12_p-qual_design-to-code_answers.md", v["ANSWERS_SHA256"],
         (f"sft {k['sft']} (the forced-round exclusion), dpo {k['dpo']}, instruct {k['instruct']}",
          f"k = {k['sft']}/{k['dpo']}/{k['instruct']}",
          f"The sham seconds ({seat_s} s over sixteen) are reported beside, no basis.",
          "decided at G-PWR as p §4.1 has it")),
        ("a225a89", "RESULTS.md", None,
         (f"Each checkpoint ran {v['CONTRAST_N'] + v['SHAM_N']} sessions, {v['CONTRAST_N']} contrast and "
          f"{v['SHAM_N']} sham.",) + rows_entry
         + ("The sham seconds are m's report's sum over the sixteen.",
            "Each sham session ran its 4 forced and 6 free rounds, with no exclusion and no claim.")),
        ("LOAD", "PROPOSAL-m-gating-campaign-v1_11.md", v["PROPOSAL_M_SHA256"],
         rows_m + (m214,
                   f"OLMo basis {M.dec(B['instruct'], 1)} s per session at instruct and {M.dec(B['sft'], 1)} s at "
                   f"SFT/DPO",
                   f"applied to the unit's total + {v['GATE_SESSIONS']} sessions per checkpoint (24 qualification + 2 "
                   f"timing)",
                   "on OLMo the absolute bar is reported only, computed against the same .20")),
        ("LOAD", "PROPOSAL-p-olmo-told-controls-frame-dose-v0_2.md", v["PROPOSAL_P_SHA256"],
         (f"**The budget is {v['BUDGET_H']} h**", f"floors {v['FLOOR']['A0']}/{v['FLOOR']['A0s']}")),
    ) + locks + (
        ("LOAD", "results/raw/2026-11-06_ganl-f3_design-to-code_answers.md", None,
         ("as a sibling script `scripts/mf3_gpwr.py` that imports `scripts/m_gpwr.py`'s functions unchanged",)),
        ("LOAD", "results/raw/2026-10-14_m-design-to-code_step15_answers.md", None,
         ("## Q7 — G-PWR's methods", "strikable until v1.0's commit; a strike recomputes figures only")),
    )


SOURCES = build_sources()


def bar_names(ckpt: str) -> tuple[str, str, str]:
    return (f"round_degeneracy@campaign-OLMo-{ckpt}", f"exclusion_guard_fisher@campaign-OLMo-{ckpt}",
            f"exclusion_guard_abs@campaign-OLMo-{ckpt}")


def olmo_bars(ckpt: str) -> dict:
    return {b.name: b for b in bars.OLMO_BARS(ckpt)}


def bar_problems_p(ckpt: str, by_name: dict | None = None) -> list[str]:
    """The constants this program computes with, against bars.OLMO_BARS(ckpt)'s campaign rows (m:316, m:330): the
    degeneracy row's p0 and alpha are read from the bar itself, so this checks kind, domain and binding, and that the
    guard's p0 and alphas equal m_gpwr's GUARD_ABS_P0 and ALPHA, which m_gpwr.guard_block computes with."""
    B = olmo_bars(ckpt) if by_name is None else by_name
    dn, fn, an = bar_names(ckpt)
    out = [f"{n}: missing" for n in (dn, fn, an) if n not in B]
    if out:
        return out
    d, f, a = B[dn], B[fn], B[an]
    if (d.kind, d.p0q, d.alphaq, d.domain, d.binding) != ("binomial_look", Fraction(1, 50), Fraction(1, 20), "sham",
                                                          True):
        out.append(f"{dn}: {(d.kind, d.p0q, d.alphaq, d.domain, d.binding)}")
    if (f.kind, f.alphaq, f.domain, f.binding) != ("guard_fisher", M.ALPHA, "contrast_arm", True):
        out.append(f"{fn}: {(f.kind, f.alphaq, f.domain, f.binding)}")
    if (a.kind, a.p0q, a.alphaq, a.domain, a.binding) != ("guard_abs", M.GUARD_ABS_P0, M.ALPHA, "contrast_arm", False):
        out.append(f"{an}: {(a.kind, a.p0q, a.alphaq, a.domain, a.binding)}")
    return out


def guard_halves(fisher_bar, abs_bar) -> tuple[str, ...]:
    """The guard's halves whose fire pauses, read from the bars' binding flags (m:316: on OLMo the absolute half is
    reported only)."""
    return tuple(h for h, b in (("abs", abs_bar), ("fisher", fisher_bar)) if b.binding)


def olmo_profile(ckpt: str) -> dict:
    B = olmo_bars(ckpt)
    d, f, a = (B[n] for n in bar_names(ckpt))
    return {"unit": f"OLMo-{ckpt}", "k": K[ckpt], "n_q": N_Q, "floors": dict(FLOOR),
            "per_template_beside": {"A0": (K[ckpt] - SHAM_VALID, CONTRAST_N), "A0s": (SHAM_VALID, SHAM_N)},
            "degen": (d.p0q, d.alphaq), "guard": (a.p0q, a.alphaq), "guard_halves": guard_halves(f, a),
            "sham_realised": SHAM_ROUNDS_REALISED}


def qf0_profile() -> dict:
    """The self-test's regression profile: Q-F0's inputs, read from m_gpwr's own constants and Q-F0's bars."""
    d, f, a = M._bar(M.DEGEN_BAR), M._bar(M.FISHER_BAR), M._bar(M.ABS_BAR)
    return {"unit": M.UNIT, "k": M.K, "n_q": M.N_Q, "floors": dict(M.FLOOR),
            "per_template_beside": dict(M.PER_TEMPLATE), "degen": (d.p0q, d.alphaq), "guard": (a.p0q, a.alphaq),
            "guard_halves": guard_halves(f, a), "sham_realised": M.SHAM_ROUNDS_REALISED}


def degeneracy(rounds: list[int], p0: Fraction, alpha: Fraction) -> dict:
    """m_gpwr.degeneracy's three fields at the unit's own p0 and alpha (READINGS item 5)."""
    return {"n_j": rounds, "crit_j": [bars.critical_k(n, p0, alpha) for n in rounds],
            "false_pause": M.rec(bars.seq_false_pause(rounds, p0, alpha))}


def frac_text(x: Fraction) -> str:
    """m_gpwr.fs's form, an integer without its "/1" (Q-F0's realised 17/2 unchanged; OLMo's 10 reads 10)."""
    return str(x.numerator) if x.denominator == 1 else M.fs(x)


def count_of(x: int, n: int) -> str:
    """A per-template count as "x/n", unreduced (16 of 16 reads 16/16, not m_gpwr.fs's 1/1)."""
    if type(x) is not int or type(n) is not int or not 0 <= x <= n or n < 1:
        raise ValueError(f"a count x of n needs ints 0 <= x <= n, n >= 1, got {x!r} of {n!r}")
    return f"{x}/{n}"


def hours_rec(h: Fraction) -> dict:
    return {"exact": M.fs(h), "display": M.dec(h, 2), "one_place": M.dec(h, 1)}


def hours_block(ckpt: str, total: int) -> dict:
    """m:205: hours = (the unit's total + 26) x the OLMo basis per session, as m:209-212's OLMo column."""
    return {"basis_s_per_session": M.fs(BASIS_S[ckpt]), "sessions": total + GATE_SESSIONS,
            "of_which_gate_sessions": GATE_SESSIONS,
            "hours": hours_rec(Fraction(total + GATE_SESSIONS) * BASIS_S[ckpt] / 3600)}


def compute_unit(m, prof: dict) -> dict:
    """m:285 for one unit, on m_gpwr's functions and Q7's methods (m_gpwr.compute's form, the unit's own inputs)."""
    k, n_q, floor = prof["k"], prof["n_q"], prof["floors"]
    if type(k) is not int or type(n_q) is not int or n_q < 1 or not 0 <= k <= n_q:
        raise ValueError(f"k must be an int in [0, n_q] and n_q a positive int, got k {k!r}, n_q {n_q!r}")
    if k == 0:
        raise SystemExit(f"STOP: {prof['unit']}: k = 0 -- m:192: the rule yields no launch count; G-PWR cannot run, "
                         f"LOCK v1.0 cannot be committed")
    r = Fraction(k, n_q)
    half = floor["A0"] // 2
    pwr = m.power_exact(half, floor["A0"] - half, floor["A0s"])
    if pwr < M.POWER_FLOOR:
        raise SystemExit(f"STOP: {prof['unit']}: power at the floors is below .85; m:190 raises n in whole units, a "
                         f"rule this program does not apply -- escalate (Code never self-adjudicates)")
    pin3 = dict(m.power_block(half, floor["A0"] - half, floor["A0s"])["of_record"])
    pin3["basis"] = PIN3_BASIS
    launch = {a: M.launch_count(floor[a], r) for a in ARMS}
    for a in ARMS:
        if launch[a]["L"] != schedule._n90_launch(floor[a], k, n_q):
            raise SystemExit(f"STOP: {prof['unit']}: the launch rule disagrees with schedule._n90_launch for {a}")
    L = {a: launch[a]["L"] for a in ARMS}
    total = sum(L.values())
    n_looks = M.looks_for(total)
    rows = {}
    for j in range(1, n_q + 1):
        lj = {a: M.launch_count(floor[a], Fraction(j, n_q))["L"] for a in ARMS}
        t = sum(lj.values())
        rows[str(j)] = {**lj, "total": t, "looks": M.looks_for(t)}
    same_row = [int(j) for j in rows if (rows[j]["A0"], rows[j]["A0s"]) == (L["A0"], L["A0s"])]
    floor_r = ceil(Fraction(floor["A0s"]) / r)
    cases = {
        "projection": {"stop": dict(L), "rounds_per_sham_launch": "10"},
        "sham_at_floor_r": {"stop": {"A0": L["A0"], "A0s": floor_r}, "rounds_per_sham_launch": "10"},
        "sham_at_floor_min": {"stop": {"A0": L["A0"], "A0s": floor["A0s"]}, "rounds_per_sham_launch": "10"},
        "sham_realised_rounds": {"stop": dict(L), "rounds_per_sham_launch":
                                 frac_text(Fraction(*prof["sham_realised"]) * bars.MAX_ROUNDS)},
    }
    rounds = {}
    for name, cs in cases.items():          # the cheap pass: every case's looks and rounds, checked before any figure
        lks = M.project(cs["stop"])
        per = Fraction(cs["rounds_per_sham_launch"])
        rounds[name] = [lk["A0s"] * per for lk in lks]
        if any(x.denominator != 1 for x in rounds[name]):
            raise SystemExit(f"STOP: {prof['unit']}: case {name}: non-integer sham rounds {rounds[name]}")
        cs["looks"] = lks
        cs["n_looks"] = len(lks)
    proj = cases["projection"]
    if proj["n_looks"] != n_looks:
        raise SystemExit(f"STOP: {prof['unit']}: the projection's looks {proj['n_looks']} differ from ceil(total/40) "
                         f"= {n_looks}")
    p0, alpha = prof["degen"]
    halves = tuple(prof["guard_halves"])
    fig = GUARD_FIGURE[halves]
    for name, cs in cases.items():
        cs["round_degeneracy"] = degeneracy([int(x) for x in rounds[name]], p0, alpha)
        if name != "sham_realised_rounds":
            cs["guard"] = M.guard_block(cs["looks"], with_grid=(name == "projection"))
            cs["guard_figure"] = {"pausing_halves": list(halves), "figure": fig,
                                  "at_common_rate_p0": cs["guard"]["at_common_rate_p0"][fig]}
    return {
        "unit": prof["unit"],
        "inputs": {"k": k, "n_q": n_q, "r": M.fs(r),
                   "per_template_beside": {a: count_of(*prof["per_template_beside"][a]) for a in ARMS},
                   "floors": dict(floor), "balance_unit": schedule.UNIT_SIZE, "look_every": resume.LOOK_EVERY,
                   "round_degeneracy": {"p0": M.fs(p0), "alpha": M.fs(alpha), "domain": "sham rounds"},
                   "guard": {"abs_p0": M.fs(prof["guard"][0]), "alpha": M.fs(prof["guard"][1]),
                             "unit": "sessions launched", "pausing_halves": list(halves)},
                   "sham_rounds_realised_at_G-F0m": list(prof["sham_realised"])},
        "power": {"at_floors": {"A0": floor["A0"], "A0s": floor["A0s"], **M.rec(pwr, 3), "exact4": M.dec(pwr),
                                "basis": POWER_BASIS},
                  "power_floor": M.fs(M.POWER_FLOOR), "n_raised": False, "pin3_of_record_at_floors": pin3},
        "launch": {"rule": launch, "L": L, "total": total, "looks": n_looks, "k_with_this_row": same_row,
                   "rows_by_k": rows},
        "cases": cases,
        "joint": {"figure": "round_degeneracy's own (projection case)",
                  "value": proj["round_degeneracy"]["false_pause"],
                  "guard_beside": proj["guard"]["at_common_rate_p0"][fig], "guard_beside_figure": fig,
                  "not_computed": M.JOINT_SENTENCE},
    }


def compute(m, bars_override: dict | None = None) -> dict:
    """The record's figures. bars_override (the self-test's STOP probe only): a checkpoint's stand-in bars for the
    bars check."""
    for c in CKPTS:
        bp = bar_problems_p(c, (bars_override or {}).get(c))
        if bp:
            raise SystemExit(f"STOP: this program's constants differ from the bars of record: {bp}")
    units = {}
    for c in CKPTS:
        u = compute_unit(m, olmo_profile(c))
        u["hours_at_m205_basis"] = hours_block(c, u["launch"]["total"])
        units[f"OLMo-{c}"] = u
    hsum = sum(Fraction(units[f"OLMo-{c}"]["hours_at_m205_basis"]["hours"]["exact"]) for c in CKPTS)
    return {"schema": SCHEMA, "proposal": PROPOSAL, "path": PATH, "units": units,
            "campaigns": {"hours_at_m205_basis_sum": hours_rec(hsum), "budget_h": BUDGET_H, "cap_share": CAP_SHARE,
                          "sham_seconds_beside": {f"OLMo-{c}": {"sum_over_sixteen_sham_sessions_s": SHAM_SECONDS_BESIDE[c],
                                                                "basis": "none"} for c in CKPTS}},
            "not_figured": dict(NOT_FIGURED), "readings": list(READINGS)}


# --- the committed texts the inputs are read from --------------------------------------------------------------
def sources_record(load_commit: str, sources=SOURCES) -> tuple[list[str], list[dict]]:
    """Each source read from its commit's blob: its sha256 checked where one is declared, every quote required
    verbatim. Returns (problems, the sources as recorded: commit, path, sha256)."""
    probs, rec_ = [], []
    for rev, rel, want_sha, quotes in sources:
        try:
            commit = load_commit if rev == "LOAD" else _commit_of(rev)
            _, data = _commit_blob(commit, rel)
        except _GitRead as e:
            probs.append(f"{rev}:{rel}: {e}")
            continue
        sha = hashlib.sha256(data).hexdigest()
        if want_sha and sha != want_sha:
            probs.append(f"{rev}:{rel}: sha256 {sha}, not {want_sha}")
        text = data.decode("utf-8")
        probs += [f"{rev}:{rel}: lacks {q[:60]!r}" for q in quotes if q not in text]
        rec_.append({"commit": commit, "path": rel, "sha256": sha})
    return probs, rec_


# --- the record's checks ---------------------------------------------------------------------------------------
def display_problems(res: dict) -> list[str]:
    """Every {exact, display} pair, at any depth, displays its exact value half-up: the power at three places, hours
    at two (and one), everything else at four."""
    bad = []

    def walk(x, path):
        if isinstance(x, dict):
            if "exact" in x and "display" in x and isinstance(x["exact"], str):
                if path.endswith("at_floors") or path.endswith("pin3_of_record_at_floors"):
                    places = 3
                elif path.endswith("hours") or path.endswith("hours_at_m205_basis_sum"):
                    places = 2
                    if x.get("one_place") != M.dec(Fraction(x["exact"]), 1):
                        bad.append(path + ".one_place")
                else:
                    places = 4
                if x["display"] != M.dec(Fraction(x["exact"]), places):
                    bad.append(path)
            for k_, v_ in x.items():
                walk(v_, f"{path}.{k_}")
        elif isinstance(x, list):
            for i_, v_ in enumerate(x):
                walk(v_, f"{path}[{i_}]")
    walk(res, "$")
    return bad


def record_problems(res: dict) -> list[str]:
    """The record's fields against the oracles of record: the planning row at each unit (m:209); the inputs, literal
    (k and r, the per-template counts, OLMo's degeneracy p0 1/50 and alpha 1/20 and the bars' own, the guard's p0,
    alpha and pausing half); the power at the floors (.878, its exact value's sha256 m_gpwr's own pin: the floors are
    Q-F0's uncached ones); every case's stop, rounds, crit_j and false pause both against the reviewed figures and
    against bars' critical_k and seq_false_pause at OLMo's p0; the guard's looks, crits and three figures against the
    reviewed ones, its pausing figure's value equal to the Fisher half's; the grid's maxima; the joint's values; the
    hours at m:205's basis (m:209's OLMo column, m:214's sum); the fixed texts; and the display rule."""
    out = []
    if (res.get("schema"), res.get("proposal"), res.get("path")) != ("p-gpwr-v1", "PROPOSAL-p", "uncached"):
        out.append("schema / proposal / path")
    if sorted(res.get("units", {})) != sorted(f"OLMo-{c}" for c in CKPTS):
        return out + ["units"]
    if SHAM_ROUNDS_REALISED != (SHAM_VALID * bars.MAX_ROUNDS, SHAM_N * bars.MAX_ROUNDS) or bars.MAX_ROUNDS != 10:
        out.append("the realised sham rounds are not 16 valid sessions of 10 rounds")
    if BASIS_S["dpo"] != BASIS_S["sft"]:
        out.append("m:205's SFT/DPO basis is one figure")
    p0q, alq = Fraction(1, 50), Fraction(1, 20)
    for c in CKPTS:
        u = res["units"][f"OLMo-{c}"]
        la, inp = u["launch"], u["inputs"]
        if (la["L"], la["total"], la["looks"]) != ({"A0": 96, "A0s": 64}, 160, 4):
            out.append(f"OLMo-{c}: the launch row {la['L']} {la['total']} {la['looks']} is not m:209's")
        if la["k_with_this_row"] != [21, 22, 23, 24]:
            out.append(f"OLMo-{c}: the same row at k = {la['k_with_this_row']}")
        if la["rule"] != REVIEWED_RULE[c]:
            out.append(f"OLMo-{c}: the launch rule {la['rule']} is not the reviewed one")
        if (inp["k"], inp["n_q"], inp["r"]) != ({"sft": 23, "dpo": 24, "instruct": 24}[c], 24,
                                                {"sft": "23/24", "dpo": "1/1", "instruct": "1/1"}[c]):
            out.append(f"OLMo-{c}: k / n_q / r")
        if inp["per_template_beside"] != {"A0": "7/8" if c == "sft" else "8/8", "A0s": "16/16"}:
            out.append(f"OLMo-{c}: per template beside {inp['per_template_beside']}")
        dgb = olmo_bars(c)[bar_names(c)[0]]
        if inp["round_degeneracy"] != {"p0": "1/50", "alpha": "1/20", "domain": "sham rounds"} or \
                (dgb.p0q, dgb.alphaq) != (p0q, alq):
            out.append(f"OLMo-{c}: round_degeneracy's inputs {inp['round_degeneracy']} are not OLMo's 1/50, 1/20")
        if inp["guard"] != {"abs_p0": "1/5", "alpha": "1/20", "unit": "sessions launched",
                            "pausing_halves": ["fisher"]}:
            out.append(f"OLMo-{c}: the guard's inputs {inp['guard']} (m:316: the Fisher half alone pauses on OLMo)")
        if inp["sham_rounds_realised_at_G-F0m"] != [160, 160]:
            out.append(f"OLMo-{c}: realised sham rounds")
        af = u["power"]["at_floors"]
        if (af["A0"], af["A0s"], af["display"], u["power"]["n_raised"]) != (80, 32, "0.878", False) or \
                hashlib.sha256(str(af["exact"]).encode("utf-8")).hexdigest() != POWER_EXACT_SHA256:
            out.append(f"OLMo-{c}: power at the floors")
        if sorted(u["cases"]) != sorted(CASE_ORDER):
            out.append(f"OLMo-{c}: cases {sorted(u['cases'])}")
            continue
        for cname in CASE_ORDER:
            cs, want = u["cases"][cname], REVIEWED[c][cname]
            rd = cs["round_degeneracy"]
            if cs["stop"] != want["stop"] or cs["rounds_per_sham_launch"] != "10":
                out.append(f"OLMo-{c} {cname}: stop {cs['stop']} / rounds {cs['rounds_per_sham_launch']}")
            if (rd["n_j"], rd["crit_j"], rd["false_pause"]["display"]) != (want["n_j"], want["crit_j"], want["fp"]):
                out.append(f"OLMo-{c} {cname}: round_degeneracy {rd['n_j']} {rd['crit_j']} "
                           f"{rd['false_pause']['display']} is not the reviewed one")
            if rd["crit_j"] != [bars.critical_k(n, p0q, alq) for n in rd["n_j"]] or \
                    Fraction(rd["false_pause"]["exact"]) != bars.seq_false_pause(rd["n_j"], p0q, alq):
                out.append(f"OLMo-{c} {cname}: round_degeneracy is not bars' at OLMo's p0 1/50, alpha 1/20")
            if cname == "sham_realised_rounds":
                if "guard" in cs or "guard_figure" in cs:
                    out.append(f"OLMo-{c} {cname}: a guard figure where Q7 (a)'s rounds-only case has none")
                continue
            g, gf = cs["guard"], cs["guard_figure"]
            at = g["at_common_rate_p0"]
            if (g["looks_n1_n2"], g["abs_crit_j"], at["p"], (at["abs"]["display"], at["fisher"]["display"],
                                                              at["union"]["display"])) != \
                    (want["n1n2"], want["abs_crit_j"], "1/5", want["guard"]):
                out.append(f"OLMo-{c} {cname}: the guard's looks, crits or figures are not the reviewed ones")
            if (gf["pausing_halves"], gf["figure"], gf["at_common_rate_p0"]) != (["fisher"], "fisher", at["fisher"]):
                out.append(f"OLMo-{c} {cname}: the pausing figure is not the Fisher half's value (m:316)")
        g = u["cases"]["projection"]["guard"]
        if ((g["fisher_grid_max"]["display"], g["fisher_grid_max"]["p"]),
                (g["fisher_grid_max_refined"]["display"], g["fisher_grid_max_refined"]["p"],
                 g["fisher_grid_max_refined"]["rates"]),
                (g["union_grid_max_p_le_p0"]["display"], g["union_grid_max_p_le_p0"]["p"])) != \
                (REVIEWED_GRID["max"], REVIEWED_GRID["refined"], REVIEWED_GRID["union_le_p0"]):
            out.append(f"OLMo-{c}: the grid's maxima are not the reviewed ones")
        jj, pr = u["joint"], u["cases"]["projection"]
        if (jj["value"], jj["guard_beside"], jj["guard_beside_figure"]) != \
                (pr["round_degeneracy"]["false_pause"], pr["guard"]["at_common_rate_p0"]["fisher"], "fisher"):
            out.append(f"OLMo-{c}: the joint's values are not the projection's round_degeneracy and Fisher half")
        hb = u["hours_at_m205_basis"]
        want_h = TABLE_HOURS[160][0 if c == "instruct" else 1]
        if (hb["sessions"], hb["of_which_gate_sessions"], hb["basis_s_per_session"], hb["hours"]["one_place"]) != \
                (186, 26, {"sft": "227/10", "dpo": "227/10", "instruct": "39/2"}[c], want_h):
            out.append(f"OLMo-{c}: hours {hb['sessions']} {hb['hours']['one_place']} vs m:209's {want_h}")
        if jj["not_computed"] != M.JOINT_SENTENCE:
            out.append(f"OLMo-{c}: joint.not_computed")
    camp = res.get("campaigns", {})
    if camp.get("hours_at_m205_basis_sum", {}).get("one_place") != TABLE_SUMS[160] or \
            camp.get("hours_at_m205_basis_sum", {}).get("exact") != "20119/6000":
        out.append("campaigns: the hours' sum is not m:214's 3.4 at 160 each (20119/6000 h)")
    if (camp.get("budget_h"), camp.get("cap_share")) != (12, CAP_SHARE):
        out.append("campaigns: budget / cap share")
    if camp.get("sham_seconds_beside") != {
            "OLMo-sft": {"sum_over_sixteen_sham_sessions_s": "102.105", "basis": "none"},
            "OLMo-dpo": {"sum_over_sixteen_sham_sessions_s": "88.389", "basis": "none"},
            "OLMo-instruct": {"sum_over_sixteen_sham_sessions_s": "85.237", "basis": "none"}}:
        out.append("campaigns: sham seconds beside")
    if res.get("not_figured") != NOT_FIGURED or res.get("readings") != READINGS:
        out.append("not_figured / readings")
    return out + display_problems(res)


# --- the report ------------------------------------------------------------------------------------------------
def _unit_lines(name: str, u: dict) -> list[str]:
    inp, pw, la = u["inputs"], u["power"], u["launch"]
    L_ = [f"UNIT {name}: k = {inp['k']} of {inp['n_q']}, r = {inp['r']} (A0 {inp['per_template_beside']['A0']}, A0s "
          f"{inp['per_template_beside']['A0s']} beside)"]
    af, p3 = pw["at_floors"], pw["pin3_of_record_at_floors"]
    L_.append(f"  POWER at the floors (A0 {af['A0']}, A0s {af['A0s']}): {af['display']} ({af['exact4']}) >= .85; "
              f"no n raised")
    L_.append(f"  PIN-3 of record at the floors: {p3['display']} split {p3['split']} mS {p3['mS']}")
    for arm, lr in la["rule"].items():
        L_.append(f"  LAUNCH {arm}: floor {lr['floor']}, ceil(1.15 floor) {lr['ceil_1.15_floor']}, N90 {lr['N90']} -> "
                  f"L {lr['L']}")
    L_.append(f"  TOTAL {la['total']}; LOOKS {la['looks']}; the same row at k = {la['k_with_this_row']}")
    hb = u["hours_at_m205_basis"]
    L_.append(f"  HOURS at m:205's basis: {hb['sessions']} sessions ({la['total']} + {hb['of_which_gate_sessions']}) x "
              f"{M.dec(Fraction(hb['basis_s_per_session']), 1)} s = {hb['hours']['display']} h "
              f"({hb['hours']['one_place']})")
    for cname in CASE_ORDER:
        cs = u["cases"][cname]
        L_ += [f"  CASE {cname}: stop {cs['stop']}, rounds per sham launch {cs['rounds_per_sham_launch']}, "
               f"{cs['n_looks']} looks"]
        L_ += [f"    look {lk['look']}: launches {lk['launches']} (A0 {lk['A0']}, A0s {lk['A0s']})"
               f"{' end' if lk.get('end') else ''}" for lk in cs["looks"]]
        rd = cs["round_degeneracy"]
        L_.append(f"    round_degeneracy: n_j {rd['n_j']} crit_j {rd['crit_j']} false pause "
                  f"{rd['false_pause']['display']}")
        if "guard" in cs:
            g, gf = cs["guard"], cs["guard_figure"]
            at = g["at_common_rate_p0"]
            L_.append(f"    guard: (n1, n2)_j {g['looks_n1_n2']} abs crit_j {g['abs_crit_j']} Fisher cells_j "
                      f"{g['fisher_cells_j']}")
            L_.append(f"    guard at the common rate {at['p']}: abs {at['abs']['display']}, Fisher "
                      f"{at['fisher']['display']}, union {at['union']['display']}; pausing on this unit: "
                      f"{gf['figure']} {gf['at_common_rate_p0']['display']}")
            if "fisher_grid" in g:
                L_.append("    Fisher half on the grid: " + ", ".join(f"{x['p']}:{x['fisher']['display']}"
                                                                  for x in g["fisher_grid"]))
                L_.append(f"    Fisher grid max {g['fisher_grid_max']['display']} at p {g['fisher_grid_max']['p']}; "
                          f"refined {g['fisher_grid_max_refined']['display']} at p "
                          f"{g['fisher_grid_max_refined']['p']} (rates {g['fisher_grid_max_refined']['rates']})")
                L_.append(f"    union grid max over p <= 1/5: {g['union_grid_max_p_le_p0']['display']} at p "
                          f"{g['union_grid_max_p_le_p0']['p']}")
    jj = u["joint"]
    L_.append(f"  JOINT: {jj['figure']}: {jj['value']['display']}; the guard's beside ({jj['guard_beside_figure']} at "
              f".20): {jj['guard_beside']['display']}")
    return L_


def reference_report(res: dict) -> list[str]:
    """The report's lines, rendered from the record: report() prints exactly these."""
    names = [f"OLMo-{c}" for c in CKPTS]
    L_ = [f"G-PWR (p): {res['proposal']}'s three OLMo units ({res['path']}); model-free and exact"]
    for name in names:
        L_ += [""] + _unit_lines(name, res["units"][name])
    camp = res["campaigns"]
    L_ += ["", "CAMPAIGNS at m:205's basis: " + ", ".join(
        f"{n} {res['units'][n]['hours_at_m205_basis']['hours']['display']} h" for n in names)
        + f"; sum {camp['hours_at_m205_basis_sum']['display']} h ({camp['hours_at_m205_basis_sum']['one_place']}); "
          f"p's budget {camp['budget_h']} h (p §6.1)",
        "SHAM SECONDS beside, no basis (m's report's sum over the sixteen sham sessions at G-F0m-OLMo (p)): "
        + ", ".join(f"{n} {camp['sham_seconds_beside'][n]['sum_over_sixteen_sham_sessions_s']} s" for n in names),
        f"CAP SHARE: {camp['cap_share']}",
        f"JOINT NOT COMPUTED: {res['units'][names[0]]['joint']['not_computed']}",
        "NOT FIGURED: " + "; ".join(f"{k_}: {v_}" for k_, v_ in res["not_figured"].items()),
        "READINGS:"]
    L_ += [f"  - {x}" for x in res["readings"]]
    return L_


def report(res: dict) -> None:
    for line in reference_report(res):
        print(line)


def _rebuilt_lines(res: dict) -> list[str]:
    """The report rebuilt from the record, written apart from reference_report and _unit_lines: a second rendering,
    so a defect in one does not pass through the other (m_gpwr's line_problems' purpose, over every line)."""
    names = ["OLMo-sft", "OLMo-dpo", "OLMo-instruct"]
    out = ["G-PWR (p): %s's three OLMo units (%s); model-free and exact" % (res["proposal"], res["path"])]
    for n in names:
        u = res["units"][n]
        i, a, p3 = u["inputs"], u["power"]["at_floors"], u["power"]["pin3_of_record_at_floors"]
        la, hb = u["launch"], u["hours_at_m205_basis"]
        out.append("")
        out.append("UNIT %s: k = %s of %s, r = %s (A0 %s, A0s %s beside)"
                   % (n, i["k"], i["n_q"], i["r"], i["per_template_beside"]["A0"], i["per_template_beside"]["A0s"]))
        out.append("  POWER at the floors (A0 %s, A0s %s): %s (%s) >= .85; no n raised"
                   % (a["A0"], a["A0s"], a["display"], a["exact4"]))
        out.append("  PIN-3 of record at the floors: %s split %s mS %s" % (p3["display"], p3["split"], p3["mS"]))
        for arm in ("A0", "A0s"):
            r = la["rule"][arm]
            out.append("  LAUNCH %s: floor %s, ceil(1.15 floor) %s, N90 %s -> L %s"
                       % (arm, r["floor"], r["ceil_1.15_floor"], r["N90"], r["L"]))
        out.append("  TOTAL %s; LOOKS %s; the same row at k = %s" % (la["total"], la["looks"], la["k_with_this_row"]))
        tenths = Fraction(hb["basis_s_per_session"]) * 10           # the basis is a whole number of tenths
        basis = "%d.%d" % divmod(tenths.numerator, 10) if tenths.denominator == 1 else "?"
        out.append("  HOURS at m:205's basis: %s sessions (%s + %s) x %s s = %s h (%s)"
                   % (hb["sessions"], la["total"], hb["of_which_gate_sessions"], basis, hb["hours"]["display"],
                      hb["hours"]["one_place"]))
        for c in ("projection", "sham_at_floor_r", "sham_at_floor_min", "sham_realised_rounds"):
            cs = u["cases"][c]
            out.append("  CASE %s: stop %s, rounds per sham launch %s, %s looks"
                       % (c, cs["stop"], cs["rounds_per_sham_launch"], cs["n_looks"]))
            for lk in cs["looks"]:
                out.append("    look %s: launches %s (A0 %s, A0s %s)%s"
                           % (lk["look"], lk["launches"], lk["A0"], lk["A0s"], " end" if lk.get("end") else ""))
            rd = cs["round_degeneracy"]
            out.append("    round_degeneracy: n_j %s crit_j %s false pause %s"
                       % (rd["n_j"], rd["crit_j"], rd["false_pause"]["display"]))
            if "guard" in cs:
                g, gf = cs["guard"], cs["guard_figure"]
                at = g["at_common_rate_p0"]
                out.append("    guard: (n1, n2)_j %s abs crit_j %s Fisher cells_j %s"
                           % (g["looks_n1_n2"], g["abs_crit_j"], g["fisher_cells_j"]))
                out.append("    guard at the common rate %s: abs %s, Fisher %s, union %s; pausing on this unit: %s %s"
                           % (at["p"], at["abs"]["display"], at["fisher"]["display"], at["union"]["display"],
                              gf["figure"], gf["at_common_rate_p0"]["display"]))
                if "fisher_grid" in g:
                    out.append("    Fisher half on the grid: "
                               + ", ".join("%s:%s" % (x["p"], x["fisher"]["display"]) for x in g["fisher_grid"]))
                    mx, rf, un = g["fisher_grid_max"], g["fisher_grid_max_refined"], g["union_grid_max_p_le_p0"]
                    out.append("    Fisher grid max %s at p %s; refined %s at p %s (rates %s)"
                               % (mx["display"], mx["p"], rf["display"], rf["p"], rf["rates"]))
                    out.append("    union grid max over p <= 1/5: %s at p %s" % (un["display"], un["p"]))
        j = u["joint"]
        out.append("  JOINT: %s: %s; the guard's beside (%s at .20): %s"
                   % (j["figure"], j["value"]["display"], j["guard_beside_figure"], j["guard_beside"]["display"]))
    cp = res["campaigns"]
    hs = cp["hours_at_m205_basis_sum"]
    out.append("")
    out.append("CAMPAIGNS at m:205's basis: "
               + ", ".join("%s %s h" % (n, res["units"][n]["hours_at_m205_basis"]["hours"]["display"]) for n in names)
               + "; sum %s h (%s); p's budget %s h (p §6.1)" % (hs["display"], hs["one_place"], cp["budget_h"]))
    out.append("SHAM SECONDS beside, no basis (m's report's sum over the sixteen sham sessions at G-F0m-OLMo (p)): "
               + ", ".join("%s %s s" % (n, cp["sham_seconds_beside"][n]["sum_over_sixteen_sham_sessions_s"])
                           for n in names))
    out.append("CAP SHARE: %s" % cp["cap_share"])
    out.append("JOINT NOT COMPUTED: %s" % res["units"]["OLMo-sft"]["joint"]["not_computed"])
    out.append("NOT FIGURED: " + "; ".join("%s: %s" % kv for kv in res["not_figured"].items()))
    out.append("READINGS:")
    out += ["  - %s" % x for x in res["readings"]]
    return out


def line_problems_p(res: dict, so: str) -> list[str]:
    """The stdout against the second rendering, line by line, and its line count."""
    want, got = _rebuilt_lines(res), so.splitlines()
    out = [f"line {i + 1}: {g!r} for {w!r}" for i, (w, g) in enumerate(zip(want, got)) if w != g]
    if len(want) != len(got):
        out.append(f"{len(got)} lines for {len(want)}")
    return out


# --- self-test -------------------------------------------------------------------------------------------------
_P_CHILD_BOOT = """\
import hashlib, os, subprocess, sys, types
repo, commit = sys.argv[1], sys.argv[2]
env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
g = ["git", "--no-replace-objects", "-C", repo]
oid = subprocess.run(g + ["rev-parse", "--verify", commit + ":scripts/p_gpwr.py"], env=env, capture_output=True,
                     text=True, check=True).stdout.strip()
src = subprocess.run(g + ["cat-file", "blob", oid], env=env, capture_output=True, check=True).stdout
if hashlib.new("sha1" if len(oid) == 40 else "sha256", b"blob %d\\0" % len(src) + src).hexdigest() != oid:
    raise SystemExit("REFUSED: the self-test's script does not hash to its blob")
path = os.path.join(repo, "scripts", "p_gpwr.py")
mod = types.ModuleType("__main__")
mod.__file__, mod._PGPWR_COMMIT = path, commit
sys.modules["__main__"], sys.argv = mod, [path, "--selftest"]
exec(compile(src, path, "exec", dont_inherit=True), mod.__dict__)
"""                                                    # the self-test of record runs the script's blob at the load commit


def _child_prefix() -> str:
    return (sys.pycache_prefix if sys.pycache_prefix and not os.path.exists(sys.pycache_prefix)
            else NONEXISTENT_PYCACHE)


def _m_selftest() -> tuple[bool, str]:
    """m_gpwr's own self-test, run as m runs it: its blob at the load commit, in its own isolated process."""
    st = subprocess.run([sys.executable, "-I", "-B", "-X", f"pycache_prefix={_child_prefix()}", "-c", M._CHILD_BOOT,
                         str(REPO), _LOAD_COMMIT], capture_output=True, text=True)
    last = st.stdout.strip().splitlines()[-1] if st.stdout.strip() else ""
    n_pass = sum(1 for ln in st.stdout.splitlines() if ln.startswith("PASS"))
    n_fail = sum(1 for ln in st.stdout.splitlines() if ln.startswith("FAIL"))
    return (st.returncode == 0 and last == "selftest: PASS (0 failed)" and n_fail == 0 and n_pass > 0,
            f"rc {st.returncode}, {n_pass} PASS, {n_fail} FAIL, last {last!r}, stderr {st.stderr.strip()[-200:]!r}")


def _qf0_regression(m, mutate=None) -> tuple[bool, list]:
    """compute_unit at Q-F0's profile against m's committed Q-F0 record (data/m/gates/Q-F0_G-PWR.json at the load
    commit), field by field over m's keys: the power, the launch block, every case, the joint. mutate (the
    self-test's meta-probe only) perturbs the composition's output before the comparison."""
    _, blob = _commit_blob(_LOAD_COMMIT, "data/m/gates/Q-F0_G-PWR.json")
    rec_m = json.loads(blob.decode("utf-8"))
    mine = json.loads(resume.json_text(compute_unit(m, qf0_profile()), indent=1))
    if mutate is not None:
        mutate(mine)
    diffs = []
    pm, pp = rec_m["power"], mine["power"]
    for k_ in ("A0", "A0s", "exact", "display", "exact4"):
        if pm["at_floors"][k_] != pp["at_floors"][k_]:
            diffs.append(f"power.at_floors.{k_}")
    for k_ in ("power_floor", "n_raised"):
        if pm[k_] != pp[k_]:
            diffs.append(f"power.{k_}")
    if {k_: v for k_, v in pm["pin3_of_record_at_floors"].items() if k_ != "basis"} != \
            {k_: v for k_, v in pp["pin3_of_record_at_floors"].items() if k_ != "basis"}:
        diffs.append("power.pin3_of_record_at_floors")
    if rec_m["launch"] != mine["launch"]:
        diffs.append("launch")
    if sorted(rec_m["cases"]) != sorted(mine["cases"]):
        diffs.append("cases' names")
    for cname, cm in rec_m["cases"].items():
        for k_, v in cm.items():
            if mine["cases"].get(cname, {}).get(k_) != v:
                diffs.append(f"cases.{cname}.{k_}")
    for k_ in ("figure", "value", "guard_beside", "not_computed"):
        if rec_m["joint"][k_] != mine["joint"][k_]:
            diffs.append(f"joint.{k_}")
    checked = len(rec_m["cases"]) and all(cm for cm in rec_m["cases"].values())
    return (not diffs and bool(checked)), diffs


def _bar_probe() -> tuple[bool, list]:
    """bar_problems_p against stand-in bars (plain records of the compared fields), each with one field perturbed."""
    bad = []
    for c in CKPTS:
        real = olmo_bars(c)
        for name in bar_names(c):
            for fld in ("kind", "p0q", "alphaq", "domain", "binding"):
                orig = real[name]
                base = {k_: getattr(orig, k_) for k_ in ("kind", "p0q", "alphaq", "domain", "binding")}
                val = {"kind": "hair_trigger", "p0q": Fraction(1, 3), "alphaq": Fraction(1, 3), "domain": "every",
                       "binding": not orig.binding}[fld]
                if name.startswith("exclusion_guard_fisher") and fld == "p0q":
                    continue                       # the Fisher half carries no p0 (bars: guard_fisher)
                pert = dict(real, **{name: SimpleNamespace(**dict(base, **{fld: val}))})
                if not any(pr.startswith(name + ":") for pr in bar_problems_p(c, pert)):
                    bad.append((name, fld))
        if bar_problems_p(c, {k_: v for k_, v in real.items() if k_ != bar_names(c)[0]}) == []:
            bad.append((c, "a missing row"))
    return not bad, bad


def _interleave_same(stop: dict, ckpt: str) -> tuple[bool, str]:
    """m_gpwr.project's looks equal those of schedule.interleave's launch sequence over the OLMo unit's own arms
    (READINGS item 6): every LOOK_EVERY-th launch and the end."""
    arms = list(keys.templates(f"OLMo-{ckpt}"))
    role = dict(zip(arms, ARMS))
    counts = {a: 0 for a in arms}
    seq = []
    for arm in schedule.interleave(arms, lambda a: counts[a] >= stop[role[a]]):
        counts[arm] += 1
        seq.append(role[arm])
        if all(counts[a] >= stop[role[a]] for a in arms):
            break
    tot, looks = {a: 0 for a in ARMS}, []
    for i, r_ in enumerate(seq, 1):
        tot[r_] += 1
        if i % resume.LOOK_EVERY == 0 or i == len(seq):
            looks.append((i, tot["A0"], tot["A0s"]))
    proj = [(lk["launches"], lk["A0"], lk["A0s"]) for lk in M.project(stop)]
    return (looks == proj and arms == [f"A0-OLMo-{ckpt}", f"A0s-OLMo-{ckpt}"], f"{arms}: looks {looks} vs {proj}")


def _stop_message(f) -> str:
    try:
        f()
    except SystemExit as e:
        return str(e)
    return ""


def _run_check_p(fn) -> tuple[bool, str]:
    """m_gpwr._run_check's verdict, a STOP (SystemExit) included: a check that raises or stops is a FAIL, and the
    rest still run."""
    try:
        r = fn()
        ok, detail = r if isinstance(r, tuple) else (r, "")
    except (Exception, SystemExit) as e:  # noqa: BLE001
        ok, detail = False, f"raised {type(e).__name__}: {e}"
    return bool(ok), detail


def _perturbed(res: dict, path: tuple, val) -> dict:
    r2 = json.loads(json.dumps(res))
    x = r2
    for k_ in path[:-1]:
        x = x[k_]
    x[path[-1]] = val
    return r2


def selftest(m) -> int:
    """Every check is guarded: an exception or a STOP is a FAIL, and the rest still run. The oracles: m_gpwr's own
    self-test at the load commit (the imported functions); m's committed Q-F0 record (the composition, at Q-F0's
    inputs); the bars of record (bars.OLMO_BARS); m:209-214's planning rows and hours and the inputs' committed texts,
    bound by build_sources(); the reviewed figures (the blind review's recomputation of every one, and the run's
    verifier's of all but the Fisher half, the union and the grid maxima, both on the standard library alone);
    schedule.interleave over the OLMo arms; the stdout against a second rendering of the record."""
    fails = []

    def chk(name, fn):
        ok, detail = _run_check_p(fn)
        print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{str(detail)[:300]!r}]" if detail and not ok else ""))
        if not ok:
            fails.append(name)

    chk("m_gpwr is the load commit's blob, executed as the module m_gpwr with its commit pinned to the load commit",
        lambda: (M_BLOB == _git_text("rev-parse", f"{_LOAD_COMMIT}:{M_REL}").strip()
                 and M._LOAD_COMMIT == _LOAD_COMMIT and M.__name__ == "m_gpwr", (M_BLOB, M._LOAD_COMMIT)))
    chk("m_gpwr's own self-test passes at the load commit, in its own isolated process", _m_selftest)
    chk("the bars of record: bar_problems_p is empty at each checkpoint", lambda: (
        (lambda pr: (not pr, pr))([x for c in CKPTS for x in bar_problems_p(c)])))
    chk("bar_problems_p reports each compared field perturbed, and a missing row", _bar_probe)
    chk("compute STOPs on a bar that differs from the program's constants (a stand-in degeneracy row at p0 1/20)",
        lambda: (lambda msg: (msg.startswith("STOP: this program's constants differ from the bars of record"), msg))(
            _stop_message(lambda: compute(m, {"dpo": dict(olmo_bars("dpo"), **{bar_names("dpo")[0]: SimpleNamespace(
                kind="binomial_look", p0q=Fraction(1, 20), alphaq=Fraction(1, 20), domain="sham",
                binding=True)})}))))
    chk("the guard's pausing halves from the bars' binding flags: Fisher alone on OLMo; both on Q-F0 (the union)",
        lambda: all(olmo_profile(c)["guard_halves"] == ("fisher",) for c in CKPTS)
        and qf0_profile()["guard_halves"] == ("abs", "fisher"))
    chk("degeneracy at Qwen's p0 and alpha == m_gpwr.degeneracy, on four round lists",
        lambda: all(degeneracy(r_, M.DEGEN_P0, M.ALPHA) == M.degeneracy(r_)
                    for r_ in ([200, 400, 600, 640], [400, 640], [136, 272, 408, 544, 640], [10])))

    def olmo_p0_reaches():
        bad = []
        for c in CKPTS:
            pr = compute_unit(m, olmo_profile(c))["cases"]["projection"]["round_degeneracy"]
            qw = M.degeneracy(pr["n_j"])
            if not (pr == degeneracy(pr["n_j"], Fraction(1, 50), Fraction(1, 20))
                    and Fraction(pr["false_pause"]["exact"]) != Fraction(qw["false_pause"]["exact"])
                    and pr["false_pause"]["display"] == "0.0863" and qw["false_pause"]["display"] == "0.0976"):
                bad.append((c, pr["false_pause"]["display"], qw["false_pause"]["display"]))
        return not bad, bad
    chk("OLMo's p0 .02 reaches each unit's round_degeneracy through compute_unit: .0863 on the projection, not "
        "Qwen's .0976", olmo_p0_reaches)
    chk("Q-F0 regression: compute_unit at Q-F0's inputs reproduces m's committed record (power, launch, every case, "
        "the joint)", lambda: _qf0_regression(m))
    chk("the regression reports a perturbed case, launch block and joint (its meta-probe)", lambda: all(
        not _qf0_regression(m, mutate)[0] for mutate in (
            lambda d: d["cases"]["sham_at_floor_r"]["round_degeneracy"].__setitem__("crit_j", [0]),
            lambda d: d["launch"].__setitem__("total", 0),
            lambda d: d["joint"].__setitem__("guard_beside", {"exact": "0/1", "display": "0.0000"}))))

    def interleave_ok():
        bad = []
        for c in CKPTS:
            u = compute_unit(m, olmo_profile(c))
            for cname in CASE_ORDER:
                ok, det = _interleave_same(u["cases"][cname]["stop"], c)
                if not ok:
                    bad.append((c, cname, det))
        return not bad, bad
    chk("schedule.interleave over each OLMo unit's own arms gives m_gpwr.project's looks at every case's computed "
        "stop", interleave_ok)

    def rows_ok():
        u = compute_unit(m, olmo_profile("sft"))
        rows = u["launch"]["rows_by_k"]
        bad = []
        for rng, (a0, a0s, tot, lk, _qh) in TABLE_ROWS.items():
            for j in rng:
                if (rows[str(j)]["A0"], rows[str(j)]["A0s"], rows[str(j)]["total"], rows[str(j)]["looks"]) != \
                        (a0, a0s, tot, lk):
                    bad.append(j)
        bad += [j for j, tot in TABLE_TOTALS.items() if rows[str(j)]["total"] != tot]
        return not bad and TABLE_TOTALS[10] == TABLE_TOTALS[11], bad
    chk("rows by k == m:209-214's planning rows (k 24-12) and totals (k 11-5 and 1)", rows_ok)

    def hours_ok():
        bad = []
        for tot, (ins, sd) in TABLE_HOURS.items():
            if (hours_block("instruct", tot)["hours"]["one_place"], hours_block("sft", tot)["hours"]["one_place"],
                    hours_block("dpo", tot)["hours"]["one_place"]) != (ins, sd, sd):
                bad.append(tot)
        for tot, want in TABLE_SUMS.items():
            s = sum(Fraction(hours_block(c, tot)["hours"]["exact"]) for c in CKPTS)
            if M.dec(s, 1) != want:
                bad.append(("sum", tot))
        return not bad, bad
    chk("hours at m:205's basis == m:209-212's OLMo column at 160/192/224/288, and m:214's sums 3.4/3.9/4.5", hours_ok)
    chk("k = 0 STOPs (m:192); k out of [0, n_q], or not an int, is refused", lambda: (
        _stop_message(lambda: compute_unit(m, dict(olmo_profile("sft"), k=0))).startswith("STOP: OLMo-sft: k = 0")
        and M._raises(lambda: compute_unit(m, dict(olmo_profile("sft"), k=25)))
        and M._raises(lambda: compute_unit(m, dict(olmo_profile("sft"), k=23.0)))
        and M._raises(lambda: compute_unit(m, dict(olmo_profile("sft"), k=True)))))
    chk("power below .85 STOPs (m:190): a stand-in analyzer at .84", lambda: _stop_message(
        lambda: compute_unit(SimpleNamespace(power_exact=lambda *a: Fraction(84, 100),
                                             power_block=m.power_block), olmo_profile("dpo"))).startswith(
        "STOP: OLMo-dpo: power at the floors is below .85"))
    chk("power at exactly .85 does not STOP (m:190's floor is >= .85): a stand-in analyzer at 17/20",
        lambda: compute_unit(SimpleNamespace(power_exact=lambda *a: Fraction(17, 20), power_block=m.power_block),
                             olmo_profile("dpo"))["power"]["at_floors"]["display"] == "0.850")
    chk("a non-integer count of sham rounds STOPs: realised 135 of 160 rounds (135/16 per launch)", lambda: (
        _stop_message(lambda: compute_unit(m, dict(olmo_profile("instruct"), sham_realised=(135, 160))))
        .startswith("STOP: OLMo-instruct: case sham_realised_rounds: non-integer sham rounds")))
    chk("the sources: every input's committed text, at its commit, carries its quotes; the answers, PROPOSAL-m and "
        "PROPOSAL-p at their sha256s", lambda: (lambda pr: (not pr and SOURCES[0][2] == ANSWERS_SHA256
                                                          and SOURCES[2][2] == PROPOSAL_M_SHA256
                                                          and SOURCES[3][2] == PROPOSAL_P_SHA256, pr))(
            sources_record(_LOAD_COMMIT)[0]))
    chk("the sources check reports a quote the text lacks and a sha256 that differs", lambda: (
        lambda pr: any("lacks" in x for x in pr) and any("sha256" in x for x in pr))(sources_record(
            _LOAD_COMMIT, ((SOURCES[0][0], SOURCES[0][1], "0" * 64, ("not in the answers, by construction",)),))[0]))

    def bound_constants():
        bad = []
        for over in ({"K": dict(K, sft=22)}, {"K": dict(K, dpo=23)}, {"BASIS_S": dict(BASIS_S, sft=Fraction(228, 10))},
                     {"SHAM_SECONDS_BESIDE": dict(SHAM_SECONDS_BESIDE, sft="102.150")},
                     {"SHAM_ROUNDS_REALISED": (152, 160)}, {"SHAM_N": 24}, {"SHAM_VALID": 15}, {"CONTRAST_N": 9},
                     {"BUDGET_H": 10}, {"PATH": "cached"}, {"GATE_SESSIONS": 24}, {"FLOOR": {"A0": 96, "A0s": 32}},
                     {"TABLE_TOTALS": {**TABLE_TOTALS, 9: 385}}, {"TABLE_SUMS": {**TABLE_SUMS, 160: "3.3"}},
                     {"TABLE_HOURS": {**TABLE_HOURS, 160: ("1.1", "1.2")}},
                     {"TABLE_ROWS": {**TABLE_ROWS, range(21, 25): (96, 64, 160, 4, "21.8")}},
                     {"ENTRY_ROW_REST": {**ENTRY_ROW_REST, "dpo": ("1", "", "32", "0")}},
                     {"ANSWERS_SHA256": "0" * 64}, {"PROPOSAL_M_SHA256": "1" * 64}, {"PROPOSAL_P_SHA256": "2" * 64}):
            if not sources_record(_LOAD_COMMIT, build_sources(over))[0]:
                bad.append(sorted(over))
        return not bad, bad
    chk("each constant bound to its text: a perturbed k (at two units), basis, sham count or seconds, realised rounds, "
        "budget, path, gate sessions, floor, table cell, entry row or pinned sha256 refuses the sources (20 cases)",
        bound_constants)

    def record_ok():
        res = compute(m)
        text = resume.json_text(res, indent=1)
        back = json.loads(text)
        so = io.StringIO()
        with redirect_stdout(so):
            report(back)
        pr = record_problems(back) + line_problems_p(back, so.getvalue())
        ok = (not pr and resume.json_text(back, indent=1) == text and so.getvalue().splitlines()
              == reference_report(back))
        return ok, pr
    chk("the record: its oracles and the reviewed figures, the fixed texts and the display rule; a JSON round trip; "
        "the stdout rebuilt line by line from the record", record_ok)

    def record_check_bites():
        res = json.loads(resume.json_text(compute(m), indent=1))
        u_ = ("units", "OLMo-dpo")
        union = res["units"]["OLMo-dpo"]["cases"]["projection"]["guard"]["at_common_rate_p0"]["union"]
        qwen = M.degeneracy([200, 400, 600, 640])
        bad = []
        for path, val in (((*u_[:1], "OLMo-sft", "launch", "total"), 192),
                          ((*u_, "joint", "guard_beside_figure"), "union"),
                          ((*u_, "joint", "guard_beside"), union),
                          ((*u_, "cases", "projection", "guard_figure", "at_common_rate_p0"), union),
                          ((*u_, "cases", "sham_at_floor_min", "guard_figure", "at_common_rate_p0"), union),
                          ((*u_, "cases", "projection", "round_degeneracy"), qwen),
                          ((*u_, "cases", "projection", "round_degeneracy", "crit_j"), [16, 28, 40, 42]),
                          ((*u_, "inputs", "round_degeneracy", "p0"), "1/20"),
                          (("units", "OLMo-sft", "cases", "sham_at_floor_r", "stop", "A0s"), 35),
                          (("units", "OLMo-instruct", "cases", "sham_realised_rounds", "rounds_per_sham_launch"),
                           "17/2"),
                          (("units", "OLMo-dpo", "inputs", "per_template_beside", "A0"), "1/1"),
                          (("units", "OLMo-instruct", "power", "at_floors", "exact"), "878/1000"),
                          (("campaigns", "cap_share"), "1/3 each"),
                          (("units", "OLMo-sft", "hours_at_m205_basis", "hours", "one_place"), "1.1"),
                          (("units", "OLMo-sft", "cases", "projection", "guard", "fisher_grid_max", "p"), "49/100")):
            if not record_problems(_perturbed(res, path, val)):
                bad.append(path)
        return not bad, bad
    chk("record_problems reports a perturbed total, guard figure (label and value), degeneracy, crit_j and p0, "
        "floor stop, realised rounds, count, power, cap share, hours and grid maximum", record_check_bites)

    def report_check_bites():
        res = json.loads(resume.json_text(compute(m), indent=1))
        so = io.StringIO()
        with redirect_stdout(so):
            report(res)
        lines = so.getvalue().splitlines()
        swapped = [ln.replace("abs 0.0929, Fisher 0.0699", "abs 0.0699, Fisher 0.0929") for ln in lines]
        joint_bar = [ln.replace("(fisher at .20): 0.0699", "(fisher at .20): 0.0863") for ln in lines]
        first = next(i for i, ln in enumerate(lines) if ln.startswith("  CASE sham_at_floor_min"))
        nxt = next(i for i, ln in enumerate(lines) if i > first and ln.startswith("  CASE "))
        dropped = lines[:first] + lines[nxt:]
        rpt1 = [ln.replace("sum 3.35 h (3.4)", "sum 3.4 h (3.4)") for ln in lines]
        rpt2 = [ln.replace("UNIT OLMo-sft: k = 23 of 24, r = 23/24 (A0 7/8,", "UNIT OLMo-sft: k = 23 of 24, r = 23/24 "
                           "(A0 16/16,") for ln in lines]
        rpt3 = [ln.replace("CASE sham_at_floor_r: stop {'A0': 96, 'A0s': 34}", "CASE sham_at_floor_r: stop {'A0': 96, "
                           "'A0s': 64}") for ln in lines]
        rpt4 = [ln.replace("OLMo-dpo 88.389 s, OLMo-instruct 85.237 s", "OLMo-dpo 102.105 s, OLMo-instruct 102.105 s")
                for ln in lines]
        bad = [n for n, ls in (("swapped", swapped), ("joint", joint_bar), ("dropped", dropped), ("sum", rpt1),
                               ("unit count", rpt2), ("case header", rpt3), ("sham seconds", rpt4))
               if ls == lines or not line_problems_p(res, "\n".join(ls))]
        return not bad, bad
    chk("line_problems_p reports a report with the guard's halves swapped, the joint's guard showing the bar's value, "
        "a case section dropped, the hours' sum, a unit's count, a case header's stop or the sham seconds altered",
        report_check_bites)
    chk("the harness counts a check that raises, stops, or returns a false value, as a FAIL",
        lambda: _run_check_p(lambda: 1 / 0)[0] is False and _run_check_p(lambda: (False, "x"))[0] is False
        and _run_check_p(lambda: (_ for _ in ()).throw(SystemExit("STOP: x")))[0] is False)
    print(f"selftest: {'PASS' if not fails else 'FAIL'} ({len(fails)} failed)")
    return 0 if not fails else 1


# --- provenance and the run of record ---------------------------------------------------------------------------
def provenance_p() -> dict:
    """The run of record binds committed blobs only: this script, m_gpwr (executed from its blob), the analyzer and
    every valence_core/m/*.py at the load commit, each with working-tree bytes equal to its blob, and the closure of
    the repository modules this process loaded; m_gpwr's helpers decide each condition, unchanged."""
    head_pkg = sorted(p for p in M._git("ls-tree", "--name-only", _LOAD_COMMIT, "valence_core/m/").split()
                      if p.endswith(".py"))
    disk_pkg = sorted(str(p.relative_to(REPO)) for p in (REPO / "valence_core" / "m").glob("*.py"))
    closure = sorted(set(M.closure_files()) | {SELF_REL})
    blobs, disk = {}, {}
    for rel in M.bound_paths(head_pkg) + closure:
        blobs[rel] = M._gitrun("rev-parse", f"{_LOAD_COMMIT}:{rel}", text=True).stdout.strip()
        disk[rel] = (M._gitrun("hash-object", "--no-filters", "--", rel, text=True).stdout.strip()
                     if (REPO / rel).is_file() and not (REPO / rel).is_symlink() else "")
    probs = M.provenance_problems(head_pkg, disk_pkg, blobs, disk, closure)
    if blobs.get(M_REL) != M_BLOB:
        probs.append(f"{M_REL}: the blob executed {M_BLOB} is not the load commit's {blobs.get(M_REL)}")
    probs += M.loaded_problems(M._LOADED, blobs, M._git("rev-parse", "HEAD").strip(), _LOAD_COMMIT, M._from_tree())
    head_tree = M._git("ls-tree", "-r", "--name-only", _LOAD_COMMIT, "valence_core/").split()
    probs += M.tree_problems(head_tree, *M._tree_on_disk())
    probs += M.path_problems([M._repo_rel(x) for x in sys.path])
    if os.environ.get("PYTHONPATH"):
        probs.append("PYTHONPATH is set: the run of record loads nothing from outside the repository and its "
                     "environment")
    if probs:
        raise SystemExit("REFUSED: G-PWR (p) of record binds committed blobs only:\n  " + "\n  ".join(probs))
    data = {rel: M._blob_bytes(blobs[rel]) for rel in M.bound_paths(head_pkg) + closure}
    sha = lambda rel: hashlib.sha256(data[rel]).hexdigest()  # noqa: E731
    pkg = M._pkg_sha256([(rel, data[rel]) for rel in head_pkg])
    if pkg != resume.package_sha256():
        raise SystemExit(f"REFUSED: the package's sha256 over the load commit's blobs {pkg} is not its value on disk "
                         f"{resume.package_sha256()}")
    return {"head": _LOAD_COMMIT, "script_sha256": sha(SELF_REL), "m_gpwr_sha256": sha(M_REL), "m_gpwr_blob": M_BLOB,
            "analyzer_sha256": sha(ANALYZER_REL), "package_sha256": pkg,
            "closure": {rel: sha(rel) for rel in closure if rel != SELF_REL}, "isolated": bool(sys.flags.isolated),
            "pycache_prefix": sys.pycache_prefix, "python": sys.version.split()[0]}


def main(argv=None) -> int:
    try:
        return _main(argv)
    except (_GitRead, M._GitFailed) as e:             # stated, not a traceback: nothing is written
        raise SystemExit(f"REFUSED: {e}")


def _main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--record", type=Path, help="write the G-PWR (p) JSON here (required for a run; refused if it "
                                                "exists)")
    a = ap.parse_args(argv)
    try:
        m = M._analyzer()
    except ImportError as e:
        raise SystemExit(f"REFUSED: {e}")
    if a.selftest:
        return selftest(m)
    if a.record is None:
        ap.error("a run of record needs --record (rule 27: the record is committed)")
    if a.record.exists() or a.record.is_symlink():
        raise SystemExit(f"REFUSED: {a.record} exists (write-once)")
    if not (a.record.parent.is_dir() and os.access(a.record.parent, os.W_OK)):
        raise SystemExit(f"REFUSED: {a.record.parent} is not a writable directory")
    if len(f".{a.record.name}.tmp-{os.getpid()}".encode()) > os.pathconf(a.record.parent, "PC_NAME_MAX"):
        raise SystemExit("REFUSED: the record's name is too long for its temporary file")
    if not sys.flags.isolated:
        raise SystemExit("REFUSED: a run of record runs in isolated mode (python -I)")
    if not sys.pycache_prefix or os.path.exists(sys.pycache_prefix):
        raise SystemExit("REFUSED: a run of record reads no cached bytecode: -X pycache_prefix=<a path that does not "
                         "exist>")
    prov = provenance_p()
    loaded_at_prov = dict(M._LOADED)
    sp, srcs = sources_record(_LOAD_COMMIT)
    if sp:
        raise SystemExit(f"REFUSED: the inputs' committed texts: {sp}")
    print(f"PROVENANCE {json.dumps(prov)}")
    print(f"SOURCES {json.dumps(srcs)}")
    st = subprocess.run([sys.executable, "-I", "-B", "-X", f"pycache_prefix={sys.pycache_prefix}", "-c",
                         _P_CHILD_BOOT, str(REPO), _LOAD_COMMIT], capture_output=True, text=True)
    print(st.stdout, end="")
    if st.stderr:
        print(st.stderr, end="")
    if st.returncode != 0:
        raise SystemExit("REFUSED: the self-test failed")
    res = compute(m)
    own = record_problems(res)
    if own:
        raise SystemExit(f"REFUSED: the record fails its own checks: {own[:5]}")
    res["sources"] = srcs
    res["provenance"] = prov
    text = resume.json_text(res, indent=1)
    shown = io.StringIO()
    with redirect_stdout(shown):
        report(json.loads(text))
    closure_now = sorted(set(M.closure_files()) | {SELF_REL})
    late = ([f"the run loaded repository modules after provenance: "
             f"{sorted(set(closure_now) - set(prov['closure']) - {SELF_REL})}"]
            if closure_now != sorted(set(prov["closure"]) | {SELF_REL}) else [])
    late += [] if M._LOADED == loaded_at_prov else [f"the run executed repository blobs after provenance: "
                                                    f"{sorted(set(M._LOADED) - set(loaded_at_prov))}"]
    late += [f"modules executed from the working tree: {M._from_tree()}"] if M._from_tree() else []
    head_now = M._git("rev-parse", "HEAD").strip()
    late += [] if head_now == _LOAD_COMMIT else [f"HEAD moved during the run: loaded from {_LOAD_COMMIT}, now {head_now}"]
    late += M.path_problems([M._repo_rel(x) for x in sys.path])
    late += line_problems_p(json.loads(text), shown.getvalue())
    if late:
        raise SystemExit(f"REFUSED: {late}")
    print(shown.getvalue(), end="")
    M.write_record(a.record, text)
    print(f"\nWROTE {a.record} sha256 {hashlib.sha256(a.record.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
