#!/usr/bin/env python3
"""G-PWR (Q-F3): m:285 for PROPOSAL-m v1.11's unit Q-F3, uncached, on r = 29/40 (m:298, m:361).

    <python> -I -B -X pycache_prefix=<a path that does not exist> scripts/mf3_gpwr.py --selftest
    <python> -I -B -X pycache_prefix=<a path that does not exist> scripts/mf3_gpwr.py --record data/mf3/gates/Q-F3_G-PWR.json

On the seat's answers of 2026-11-14 (results/raw/2026-11-14_gf3-and-lock-p-v1_design-to-code_answers.md, committed at
cdccc66), §A.7, verbatim (READINGS item 1): "G-F3 → **G-PWR (Q-F3)** on r = 29/40 by Code's program in F-5's form
(m:285: the power at the planned floors, any n raised, the launch counts and looks, §6's exact sequential false-pause
figures at the look count, the guard's figure); its hours line at m:205's basis as the program has it, with §A.5's
figures beside, by citation of this raw, as the realised basis of record".

F-5's form (results/raw/2026-11-06_ganl-f3_design-to-code_answers.md:28; READINGS item 2): the sibling of
scripts/m_gpwr.py that imports its functions unchanged. m_gpwr's bytes are executed from the load commit's blob as the
module m_gpwr, its commit pinned to the load commit, and its own startup then executes valence_core (m's package and
mf3's) from that commit's blobs. No attribute of an m or mf3 module is substituted. Q7's methods (the seat's step-15
answers) as G-PWR (p) carried them (scripts/p_gpwr.py, 4c882e7). Model-free and exact (Fractions throughout; no float
enters a comparison). Not a stages.py stage: it reads no checkpoint, report or session record, opens nothing under
data/ (the run of record writes its record there once), and writes no file a lock names. The cap is the PI's; this
program sets none.

Inputs of record (each bound to the committed text it is quoted from: build_sources() builds every quote from the
constants this program computes with, and sources_record() requires each verbatim in its text at its commit, so a
constant that differs from its text refuses the run):
  - k = 29 of n_q = 40 on the uncached path; per template beside, A1 3/4, A2 4/4, A3 6/8, A1s 4/8, A2s 4/8, A3s 8/8
    (the seat's §0 and §A.2; the G-F3 entry, 2193832; LOCK-m-F3 v0.2 §3);
  - mf3's schedule.FLOORS (A1 uncached 80; A1s 32; A2 144; A2s 56; A3 144; A3s 56), schedule.UNIT_SIZE (32, 32, 16,
    16, 16, 16) and schedule.N_Q (40), bound to m:184-186 and m:192; schedule.interleave and schedule._n90_exact;
    keys.TEMPLATES, CONTRAST, SHAM and PAIRS; the campaign rows of bars.QF3_BARS (round_degeneracy p0 .05,
    reasoning_line_defect p0 .10, own_pair_lexical p0 .02, each alpha .05; the guard's Fisher half alpha .05 and its
    absolute half p0 .20 alpha .05, both binding on Qwen), bound to m:316 and m:330;
  - LOOK_EVERY: mf3's resume.LOOK_EVERY is m's (its committed lines "from valence_core.m import resume as m_resume"
    and "LOOK_EVERY = m_resume.LOOK_EVERY"), read from valence_core.m.resume (READINGS);
  - the power at the planned floors by the analyzer's f3_power_block (A1 alpha .01, P .70; A2 alpha .01, P .65; A3
    alpha .05, P .65, its POSITIVE probability), against m:190's .878, .862 and .927;
  - G-F3's realised sham counts, 189 of <= 240 task rounds and 98 of <= 144 reasoning lines over its 24 sham sessions
    (the G-F3 entry; the seat's §A.1);
  - m:230's uncached basis, 641.6-713.6 s per session; m:234-241's rows and m:243's line after them, as oracles;
  - beside the hours, by citation: the seat's §A.5 table, its six rows verbatim.
"""
from __future__ import annotations

import os
import sys
if __name__ == "__main__" and not sys.flags.isolated:      # before any import a script directory could shadow
    raise SystemExit("REFUSED: G-PWR (Q-F3) runs in isolated mode (python -I): no script directory, user site or "
                     "environment path enters the import path")
if __name__ == "__main__" and (not sys.pycache_prefix or os.path.exists(sys.pycache_prefix)):
    raise SystemExit("REFUSED: G-PWR (Q-F3) reads no cached bytecode: run with -X pycache_prefix=<a path that does "
                     "not exist>, so every module is compiled from the bytes provenance binds")
if hasattr(sys, "set_int_max_str_digits"):
    # The exact figures are Fractions of thousands of digits (about 3,330 at k = 29). Python's default 4,300-digit cap
    # on int <-> str would turn a larger one (a reading struck and recomputed) into a traceback, not a figure.
    sys.set_int_max_str_digits(0)

import argparse
import fnmatch
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
SELF_REL, M_REL, ANALYZER_REL = "scripts/mf3_gpwr.py", "scripts/m_gpwr.py", "scripts/m_analyze.py"
RECORD_OF_RECORD = "data/mf3/gates/Q-F3_G-PWR.json"   # the run of record's path; nothing else writes there
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


_PINNED = globals().get("_F3GPWR_COMMIT")             # set only by the self-test child's bootstrap (_F3_CHILD_BOOT)
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
bars, resume, m_schedule = M.bars, M.resume, M.schedule            # valence_core.m's, from the load commit's blobs
from valence_core.mf3 import bars as F3B, keys, schedule  # noqa: E402  (through m_gpwr's finder: the load commit's blobs)

# --- the inputs ----------------------------------------------------------------------------------------------------
SCHEMA = "mf3-gpwr-v1"
UNIT = keys.UNIT                                     # "Q-F3"
PATH = "uncached"                                    # LOCK-m-F3 v0.2 §3, since G-ID-F3's FAIL
K = 29                                               # the seat's §0 and §A.2; the G-F3 entry
N_Q = schedule.N_Q                                   # 40 (m:192: "40 for Q-F3")
ARMS, CONTRAST, SHAM, PAIRS = keys.TEMPLATES, keys.CONTRAST, keys.SHAM, keys.PAIRS
PER_TEMPLATE = {"A1": (3, 4), "A1s": (4, 8), "A2": (4, 4), "A2s": (4, 8), "A3": (6, 8), "A3s": (8, 8)}   # beside only
SEAT_ORDER = ("A1", "A2", "A3", "A1s", "A2s", "A3s")   # the order the seat's raw and the G-F3 entry list them in
FLOOR = {a: (schedule.FLOORS[a][PATH] if isinstance(schedule.FLOORS[a], dict) else schedule.FLOORS[a]) for a in ARMS}
UNIT_SIZE = dict(schedule.UNIT_SIZE)
LOOK_EVERY = resume.LOOK_EVERY                       # m's; mf3's resume.LOOK_EVERY is m's (READINGS item 20)
POWER_SPEC = {"A1": (Fraction(1, 100), Fraction(7, 10)), "A2": (Fraction(1, 100), Fraction(13, 20)),
              "A3": (Fraction(1, 20), Fraction(13, 20))}   # (alpha, P): m:184-186, m:190; the analyzer's PIN-V2-2
POWER_GATED = ("A1", "A2")                           # m:190: "A2 ≥ .85 at P = .65; every control ≥ .85 at P = .70"
POWER_ORACLE = {"A1": ".878", "A2": ".862", "A3": ".927", "A1_cached_96_32": ".916"}   # m:190
TAG = f"campaign-{UNIT}"
BAR_CLASSES = ("round_degeneracy", "reasoning_line_defect", "own_pair_lexical")
BAR_ROWS = {  # the campaign rows this program computes with: (kind, p0, alpha, domain, binding); m:316, m:330
    "round_degeneracy": ("binomial_look", Fraction(1, 20), Fraction(1, 20), "sham", True),
    "reasoning_line_defect": ("binomial_look", Fraction(1, 10), Fraction(1, 20), "sham", True),
    "own_pair_lexical": ("binomial_look", Fraction(1, 50), Fraction(1, 20), "lexical_sham", True),
    "exclusion_guard_fisher": ("guard_fisher", None, Fraction(1, 20), "contrast_arm", True),
    "exclusion_guard_abs": ("guard_abs", Fraction(1, 5), Fraction(1, 20), "contrast_arm", True),
}
UNIT_OF = {"round_degeneracy": "rounds", "reasoning_line_defect": "lines", "own_pair_lexical": "rounds"}
DOMAIN_ARMS = {"sham": tuple(SHAM), "lexical_sham": tuple(F3B.LEXICAL_SHAM)}
PER_SESSION = {"rounds": F3B.MAX_ROUNDS, "lines": F3B.MAX_LINES}   # 10 task rounds, 6 reasoning lines per session
SHAM_QUAL = 24                                       # G-F3's sham sessions (m:297: 8 each of A1s, A2s, A3s)
REALISED = {"rounds": (189, 240), "lines": (98, 144)}   # G-F3's sham units: realised / planned (the G-F3 entry; §A.1)
BASIS_S = (Fraction(3208, 5), Fraction(3568, 5))     # m:230: 641.6-713.6 s per session, uncached
GUARD_FIGURE = {("abs", "fisher"): "union", ("fisher",): "fisher", ("abs",): "abs"}
CASE_ORDER = ("projection", "sham_at_floor_r", "sham_at_floor_min", "sham_realised")
NONEXISTENT_PYCACHE = "/nonexistent-mf3-gpwr-pycache"   # the self-test's children, when this process was given none
LOCK_F3_V1_HEAD = "# LOCK-m-F3.md — v1."         # a LOCK-m-F3 at v1.0 or later follows G-PWR (m:298)
_N90_EXACT = schedule._n90_exact                     # mf3's launch rule in exact integers: the cross-check
looks_for = M.looks_for                              # m_gpwr's, unchanged (an alias the self-test's probe can stub)

# m:234-241's uncached planning rows (the oracles): k range -> (A1, A1s, A2 = A3, A2s = A3s, total, looks, the hours
# column at m:230's basis); m:243's totals after the table; m:330's uncached look counts. Bound by build_sources().
TABLE_ROWS = {range(35, 41): (96, 64, 176, 80, 672, 17, "120–133"),
              range(32, 35): (128, 64, 192, 80, 736, 19, "131–146"),
              range(31, 32): (128, 64, 208, 80, 768, 20, "137–152"),
              range(30, 31): (128, 64, 208, 96, 800, 20, "143–159"),
              range(28, 30): (128, 64, 224, 96, 832, 21, "148–165"),
              range(27, 28): (128, 64, 240, 96, 864, 22, "154–171"),
              range(26, 27): (160, 64, 240, 96, 896, 23, "160–178"),
              range(24, 26): (160, 64, 256, 112, 960, 24, "171–190")}
TABLE_AFTER = {23: 992, 22: 1088, 21: 1152, 20: 1184, 1: 23328}
M330_LOOKS = ((17, (672,)), (19, (736,)), (20, (768, 800)), (21, (832,)), (22, (864,)), (23, (896,)), (24, (960,)))

# The seat's texts, verbatim (READINGS items 1-6; each required verbatim in its committed text).
SEAT_RAW = "results/raw/2026-11-14_gf3-and-lock-p-v1_design-to-code_answers.md"
SEAT_COMMIT = "cdccc66"
SEAT_COMMIT_FULL = "cdccc664b1db0ebe8a89dcefdfa4cfe79fc57754"   # the seat's raw is read at this commit
GF3_COMMIT = "2193832"                                           # the G-F3 entry's commit, as the seat's raw cites it
GF3_COMMIT_FULL = "21938326c8c0d23740390ee6a5ad42d941a60803"    # the G-F3 entry is read at this commit
SEAT_SHA256 = "6b963adf126540dab95780d486ab0a6652a1308828548a5cb2763f998040db3a"
SEAT_A7 = ("G-F3 → **G-PWR (Q-F3)** on r = 29/40 by Code's program in F-5's form (m:285: the power at the planned "
           "floors, any n raised, the launch counts and looks, §6's exact sequential false-pause figures at the "
           "look count, the guard's figure); its hours line at m:205's basis as the program has it, with §A.5's "
           "figures beside, by citation of this raw, as the realised basis of record")
F5_RAW = "results/raw/2026-11-06_ganl-f3_design-to-code_answers.md"
F5_SHA256 = "4edfbb8e3d08844e47a329a951f9c2dd381115f0fd92c8b2b77f2207777ca42e"
F5_TEXT = ("G-PWR for Q-F3 is built at its step (after G-F3, before LOCK-m-F3 v1.0) as a sibling script "
           "`scripts/mf3_gpwr.py` that imports `scripts/m_gpwr.py`'s functions unchanged; its arms and floors are "
           "m:183–190's (A1 96/32; A2 144/56; A3 144/56; power floors A2 ≥ .85 at P = .65, every control "
           "≥ .85 at P = .70; the grid rule for A2/A3), re-derived with the planned floors, attained power at the "
           "realised n reported in VERDICTS (m:190). Nothing of it touches a file a lock names.")
Q7_RAW = "results/raw/2026-10-14_m-design-to-code_step15_answers.md"
Q7_SHA256 = "07cd8e5f4535c95c61428a07c426490e694d16601818096d48210c534f780767"
Q7_PRE = ("Code's defaults are the seat's, declared at G-PWR on Q1's terms (strikable until v1.0's commit; a strike "
          "recomputes figures only)")
Q7_A = ("n_j at each look from the projection — each arm launches to its L, interleaved by the campaign rule, every "
        "sham session running its 10 rounds — with two cases beside: the sham arm leaving the rotation at its floor; "
        "the sham arm at G-F0m-Qwen's measured 136 of 160 realised rounds.")
Q7_B = ("the absolute half exact at p0 = .20 over the contrast arm's launches per look; the Fisher half under a common "
        "null rate equal to the absolute p0, with a grid of rates and the supremum beside; the guard's false-pause "
        "figure as the union — the probability that either half fires at some look — computed jointly over "
        "the contrast and sham counts under the common null rate, each half's own figure beside.")
Q7_C = ("the joint figure is `round_degeneracy`'s own, with the guard's beside; the non-separable joint over the bar "
        "and the guard is not computed, and G-PWR says why in one sentence.")
PROPOSAL_M = "PROPOSAL-m-gating-campaign-v1_11.md"
PROPOSAL_M_SHA256 = "42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b"
LOCK_F3 = "LOCK-m-F3.md"     # bound by its quotes, as p_gpwr binds its locks: v1.0 keeps v0.2's text below it
# The root's locks when this program was built (a lock is re-issued in place, never removed): the lock scan covers each.
KNOWN_LOCKS = ("LOCK-g.md", "LOCK-h.md", "LOCK-m-F0.md", "LOCK-m-F3.md", "LOCK-p-OLMo-dpo.md",
               "LOCK-p-OLMo-instruct.md", "LOCK-p-OLMo-sft.md")
# §A.5's table rows, verbatim: printed beside the hours line by citation (the seat's [E]); this program recomputes none.
A5_TOTAL = 832                                       # the launches §A.5's hours are figured on ("832 launches (m:238)")
A5_ROWS = (
    "| G-F3's 24 sham sessions as they fell, 1,298.4 s (exclusions ended early at G-F3's sham rate, 8 of 24) | "
    "**≈ 300 h** | 12.5 |",
    "| the realised r, 29/40: 72.5 % complete at 1,931.6 s, 27.5 % ended by exclusion at 31.9 s | **≈ 326 h** | "
    "13.6 |",
    "| every launch complete, 1,931.6 s | ≈ 446 h | 18.6 |",
    "| the slowest complete session, 2,962.6 s | ≈ 685 h | 28.5 |",
    "| beside: v0.2's four-session basis, 1,319.6 s (`gid:`§4) | ≈ 305 h | 12.7 |",
    "| beside: m:230's pre-registered 641.6–713.6 s | 148–165 h (m:238's column) | 6.2–6.9 |",
)
CAP = ("the PI's, at G-PWR's entry, written into LOCK-m-F3 v1.0 (m:298, m:249; the seat's answers of 2026-11-14, "
       "§A.5 and §D item 4); not set by this program")
POWER_BASIS = ("m:190's base case at the planned floors (m:184-186; LOCK-m-F3 v0.2 §3, uncached): the analyzer's "
               "f3_power_block (PIN-V2-2), each contrast arm split floor/ceil per map at clean share P, its matched "
               "sham pooled at .5; a planning figure -- attained power at the realised n is reported in VERDICTS "
               "(m:190)")
JOINT_SENTENCE = ("The joint over the three bars, and over the bars and the guard, is not computed: a sham session "
                  "that ends early at a pre-pick exclusion enters its pair's sham count and cuts its own rounds and "
                  "lines from the bars' n, a round or line the bars count can be what excludes it, and the three bars "
                  "count claims on the same sham sessions, so these figures are dependent through a model of exclusion "
                  "and claim co-occurrence that no record gives (the three pairs' guard figures, which share no "
                  "session, combine exactly into the unit's).")
GUARD_UNIT_RULE = ("1 - (1 - u_A1)(1 - u_A2)(1 - u_A3), each u its pair's pausing figure at the common rate 1/5: exact "
                   "under Q7 (b)'s model, the three pairs sharing no session")
NOT_FIGURED = {"hair_triggers": "no p0: a ~zero-base-rate class whose fire stops the stage (m:271)",
               "reported_at_looks": "low label mass, top-1-not-a-label and pooled pre-pick exclusions: reported, no "
                                    "bar (m:330)"}

READINGS = [
    "The seat's answers of 2026-11-14, §A.7, verbatim: \"" + SEAT_A7 + "\".",
    "F-5 (the seat's G-ANL-F3 answers, " + F5_RAW + "), verbatim: \"" + F5_TEXT + "\"",
    "Q7 (the seat's step-15 answers, " + Q7_RAW + "), verbatim: \"" + Q7_PRE + "\".",
    "Q7 (a), verbatim: \"" + Q7_A + "\"",
    "Q7 (b), verbatim: \"" + Q7_B + "\"",
    "Q7 (c), verbatim: \"" + Q7_C + "\"",
    "Code's reading, the form: a sibling of scripts/m_gpwr.py importing its functions unchanged (F-5), executed from "
    "the load commit's blob. m_gpwr.compute and m_gpwr.project serve Q-F0's two arm roles, so Q-F3's six-arm "
    "projection, its three bars and its three guards are composed here from m_gpwr's functions (launch_count, "
    "looks_for, guard_block, rec, dec, fs) and mf3's (schedule.interleave, schedule._n90_exact, keys, bars); the "
    "self-test asserts the composition equal to m_gpwr's own figures at Q-F0's two arms. No attribute of an m or mf3 "
    "module is substituted.",
    "Code's reading of F-5's \"A1 96/32\": it is m:184's cached floor. Q-F3 runs uncached since G-ID-F3's FAIL "
    "(LOCK-m-F3 v0.2 §3, \"path = uncached\"); m:184 gives A1's floor as \"96 cached, 80 uncached / 32\" (m:230: "
    "\"A1 floor 80\"; mf3's schedule.FLOORS; the analyzer's F3_PLANNED). So A1 runs at 80/32, in the power (.878) and "
    "the launch rule alike; m:190's figure at 96/32 (.916) is printed beside and used nowhere.",
    "Code's reading of the power floors (m:190): A1, a control, needs >= .85 at P = .70 and alpha .01; A2 needs >= "
    ".85 at P = .65 and alpha .01; A3, the screen, has no floor, and its POSITIVE probability at alpha .05 and P = "
    ".65 is reported, not gated. Each figure is the analyzer's f3_power_block at the planned floors. m:190's raise is "
    "not triggered; had A1 or A2 fallen below .85, this program would STOP and escalate, applying neither the raise "
    "nor the grid rule for A2/A3.",
    "Code's reading of the launch rule (m:192): r = 29/40 is one rate for the unit, pooled over all 40 (m:297); each "
    "arm's L is m_gpwr.launch_count at its own floor and its own balance unit (mf3's schedule.UNIT_SIZE: 32 for A1 "
    "and A1s, 16 for A2 to A3s), cross-checked against mf3's schedule._n90_exact. The rows for k = 1..40 are computed "
    "the same way and checked against m:234-241's rows (the hours column at m:230's basis included) and m:243's "
    "line after them; looks = ceil(total / 40), checked against m:330's uncached list.",
    "Code's reading of the projection: mf3's schedule.interleave over keys.TEMPLATES (A1, A1s, A2, A2s, A3, A3s). The "
    "live arm with the fewest launches goes next, ties to table order, and an arm leaves the rotation for good at its "
    "stop. Each arm launches to its L. Looks fall at every 40th launch and at the end, and an end on a multiple adds "
    "no look (m:330; m_gpwr.project's form, over six arms).",
    "Code's reading of how the three bars' domains are pooled: each bar is cumulative over its own domain, with one "
    "count per look (m:330), at its own p0 and alpha from mf3's bars, by valence_core.m.bars' critical_k and "
    "seq_false_pause (as mf3's bars import them). round_degeneracy counts the three sham arms' task rounds (A1s + A2s "
    "+ A3s; 10 per sham launch; p0 .05). reasoning_line_defect counts the same three arms' reasoning lines (6 per sham "
    "launch; p0 .10). own_pair_lexical counts A2s + A3s task rounds (10 per launch; p0 .02). No contrast-arm unit "
    "enters a bar's n (m:271's sham domain; m:330). crit_j at each look is checked against the mf3 bar's own "
    "evaluate().",
    "Code's reading of Q7 (a)'s floor case, its Q-F0 reading kept: the three sham arms leave the rotation at their "
    "floors, computed at ceil(floor / r), which is 45, 78 and 78 at r = 29/40, and at the floor itself, 32, 56 and 56. "
    "Every contrast arm launches to its L. Both keep 10 rounds and 6 lines per sham launch, which over-counts the "
    "units of the sessions they assume end early at an exclusion. The guards move with the sham arms' launches and "
    "are recomputed in both.",
    "Code's reading of Q7 (a)'s realised case, carried to Q-F3: G-F3's realised counts over its 24 sham sessions, 189 "
    "of <= 240 task rounds and 98 of <= 144 reasoning lines (the G-F3 entry; the seat's §A.1), taken as pooled "
    "rates per sham launch, 189/24 = 63/8 rounds and 98/24 = 49/12 lines. Each rate applies alike to every sham launch "
    "of each bar's domain, own_pair_lexical's A2s + A3s rounds at the same 63/8. Only the three bars are recomputed "
    "there; the guards count launches, which the case does not move.",
    "Code's reading of the realised case's rounding: the cumulative count at a look, launches x rate, is not whole at "
    "every look. Each is rounded to the nearest whole unit, a half up (floor(x + 1/2)), before the bar is evaluated. "
    "The rounded counts are non-decreasing, and their unrounded values are recorded beside (n_j_exact).",
    "Code's reading of the guard's binding halves: the guard is figured per contrast arm against its matched sham "
    "(m:316; keys.PAIRS: A1-A1s, A2-A2s, A3-A3s), each pair's cumulative launches per look passed to m_gpwr's guard "
    "functions in its arm roles (the contrast as A0, the sham as A0s). Both halves bind on Qwen (m:316; mf3's bars' "
    "binding flags, read), so the pausing figure is the union, each half's own figure beside: the absolute half exact "
    "at p0 .20 over the contrast arm's launches; the Fisher half at the common null rate .20, with the grid j/100, "
    "its refined maximum (+/- .01 by .001) and the union's maximum over common rates <= .20 (Code's Q-F0 reading, "
    "kept), the grid and the maxima figured on the projection only. Each pair's figure is its own. The unit's figure, "
    "m:285's \"the exclusion guard's false-pause figure\" for a unit whose guard runs per contrast arm, is the "
    "probability that some pair's guard pauses, " + GUARD_UNIT_RULE + "; it is figured in every case the guards are.",
    "Code's reading of the joint (Q7 (c), adapted to Q-F3's three bars and its guard of three pairs): the joint figure "
    "is each bar's own (projection case), with the guard's beside: each pair's union and the unit's figure. The joint "
    "over the three bars, and over the bars and the guard, is not computed (the sentence under JOINT). The hair "
    "triggers carry no p0 and have no figure.",
    "Code's reading of the hours basis: §A.7's \"m:205's basis\" is read as the unit's own pre-registered basis "
    "line. m:205 is Q-F0's and the OLMo checkpoints' line and holds no Q-F3 figure; m:230 is Q-F3's uncached one, "
    "641.6-713.6 s per session, applied to the unit's total (m:192: \"hours = the unit's total × the basis named\"), "
    "with m:238's column, 148-165 h, as its oracle. §A.5's figures are printed beside, by citation of the seat's "
    "raw (its path, commit and sha256; each row verbatim), as the realised basis of record. This program recomputes "
    "none of them.",
    "Code's reading of the cap: the PI's, at G-PWR's entry, written into LOCK-m-F3 v1.0 (m:298, m:249; the seat's "
    "§A.5 and §D item 4). This program sets none.",
    "Code's reading of LOOK_EVERY and of what this program opens: LOOK_EVERY is mf3's resume.LOOK_EVERY, which is m's "
    "(its committed source lines \"from valence_core.m import resume as m_resume\" and \"LOOK_EVERY = "
    "m_resume.LOOK_EVERY\", each required verbatim), read from "
    "valence_core.m.resume. valence_core.mf3.resume is not imported, because its import (through "
    "valence_core.m.corr) opens a file under data/, and this program opens nothing under data/. For the same reason "
    "Q-F0's figures are checked against m_gpwr's own pins of its reviewed run, not against m's committed record "
    "under data/m/gates.",
]

# The reviewed figures: an independent recomputation on the standard library alone (no import of this program, of
# m_gpwr, of valence_core or of the analyzer) of every figure this program prints, by algorithms written apart: N90 by
# an ascending scan with a one-step tail recurrence, the projection by an explicit rotation, the bars by a pmf
# recurrence in integers, the Fisher firing set by cumulative hypergeometric tails per margin total, the guard by a
# 2-D list DP, and the power by direct enumeration. REVIEWED_EXACT_SHA256 is the sha256 of that recomputation's exact
# values, in exact_figures()' canonical form.
REVIEWED_RULE = {"A1": (80, 92, 119, 128), "A1s": (32, 37, 50, 64), "A2": (144, 166, 210, 224), "A2s": (56, 65, 84, 96),
                 "A3": (144, 166, 210, 224), "A3s": (56, 65, 84, 96)}
REVIEWED_POWER = {"A1": ("0.878", "0.8784"), "A2": ("0.862", "0.8620"), "A3": ("0.927", "0.9273"),
                  "A1_cached_96_32": ("0.916", "0.9161")}
REVIEWED_ROWS = {  # k: (A1, A1s, A2, A2s, A3, A3s, total, looks)
    40: (96, 64, 176, 80, 176, 80, 672, 17), 39: (96, 64, 176, 80, 176, 80, 672, 17),
    38: (96, 64, 176, 80, 176, 80, 672, 17), 37: (96, 64, 176, 80, 176, 80, 672, 17),
    36: (96, 64, 176, 80, 176, 80, 672, 17), 35: (96, 64, 176, 80, 176, 80, 672, 17),
    34: (128, 64, 192, 80, 192, 80, 736, 19), 33: (128, 64, 192, 80, 192, 80, 736, 19),
    32: (128, 64, 192, 80, 192, 80, 736, 19), 31: (128, 64, 208, 80, 208, 80, 768, 20),
    30: (128, 64, 208, 96, 208, 96, 800, 20), 29: (128, 64, 224, 96, 224, 96, 832, 21),
    28: (128, 64, 224, 96, 224, 96, 832, 21), 27: (128, 64, 240, 96, 240, 96, 864, 22),
    26: (160, 64, 240, 96, 240, 96, 896, 23), 25: (160, 64, 256, 112, 256, 112, 960, 24),
    24: (160, 64, 256, 112, 256, 112, 960, 24), 23: (160, 64, 272, 112, 272, 112, 992, 25),
    22: (160, 96, 288, 128, 288, 128, 1088, 28), 21: (192, 96, 304, 128, 304, 128, 1152, 29),
    20: (192, 96, 320, 128, 320, 128, 1184, 30), 19: (192, 96, 336, 144, 336, 144, 1248, 32),
    18: (224, 96, 352, 144, 352, 144, 1312, 33), 17: (224, 96, 368, 160, 368, 160, 1376, 35),
    16: (224, 96, 400, 160, 400, 160, 1440, 36), 15: (256, 128, 432, 176, 432, 176, 1600, 40),
    14: (256, 128, 448, 192, 448, 192, 1664, 42), 13: (288, 128, 496, 208, 496, 208, 1824, 46),
    12: (320, 128, 528, 224, 528, 224, 1952, 49), 11: (352, 160, 576, 240, 576, 240, 2144, 54),
    10: (384, 160, 640, 272, 640, 272, 2368, 60), 9: (416, 192, 704, 288, 704, 288, 2592, 65),
    8: (480, 224, 800, 336, 800, 336, 2976, 75), 7: (544, 224, 912, 384, 912, 384, 3360, 84),
    6: (608, 288, 1056, 448, 1056, 448, 3904, 98), 5: (736, 320, 1280, 528, 1280, 528, 4672, 117),
    4: (928, 416, 1600, 656, 1600, 656, 5856, 147), 3: (1216, 544, 2128, 880, 2128, 880, 7776, 195),
    2: (1856, 800, 3184, 1312, 3184, 1312, 11648, 292), 1: (3680, 1600, 6384, 2640, 6384, 2640, 23328, 584)}
_PROJ_LOOKS = [  # (launches, A1, A1s, A2, A2s, A3, A3s): the projection's, and the realised case's (the same launches)
    (40, 7, 7, 7, 7, 6, 6), (80, 14, 14, 13, 13, 13, 13), (120, 20, 20, 20, 20, 20, 20),
    (160, 27, 27, 27, 27, 26, 26), (200, 34, 34, 33, 33, 33, 33), (240, 40, 40, 40, 40, 40, 40),
    (280, 47, 47, 47, 47, 46, 46), (320, 54, 54, 53, 53, 53, 53), (360, 60, 60, 60, 60, 60, 60),
    (400, 68, 64, 67, 67, 67, 67), (440, 76, 64, 75, 75, 75, 75), (480, 84, 64, 83, 83, 83, 83),
    (520, 92, 64, 91, 91, 91, 91), (560, 102, 64, 101, 96, 101, 96), (600, 115, 64, 115, 96, 114, 96),
    (640, 128, 64, 128, 96, 128, 96), (680, 128, 64, 148, 96, 148, 96), (720, 128, 64, 168, 96, 168, 96),
    (760, 128, 64, 188, 96, 188, 96), (800, 128, 64, 208, 96, 208, 96), (832, 128, 64, 224, 96, 224, 96)]
REVIEWED_CASES = {
    "projection": {
        "stop": (128, 64, 224, 96, 224, 96),
        "looks": _PROJ_LOOKS,
        "bars": {
            "round_degeneracy": (
                [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 1980, 2140, 2300, 2460] + [2560] * 8,
                [16, 28, 40, 51, 63, 74, 85, 96, 106, 116, 125, 133, 142] + [147] * 8, "0.1703"),
            "reasoning_line_defect": (
                [120, 240, 360, 480, 600, 720, 840, 960, 1080, 1188, 1284, 1380, 1476] + [1536] * 8,
                [19, 33, 47, 60, 73, 86, 100, 113, 125, 137, 147, 158, 168] + [174] * 8, "0.1584"),
            "own_pair_lexical": (
                [130, 260, 400, 530, 660, 800, 930, 1060, 1200, 1340, 1500, 1660, 1820] + [1920] * 8,
                [6, 10, 14, 17, 20, 24, 27, 30, 33, 36, 40, 44, 47] + [50] * 8, "0.1641"),
        },
        "guards": {
            "A1": ([[7, 7], [14, 14], [20, 20], [27, 27], [34, 34], [40, 40], [47, 47], [54, 54], [60, 60], [68, 64],
                    [76, 64], [84, 64], [92, 64], [102, 64], [115, 64]] + [[128, 64]] * 6,
                   [4, 6, 8, 10, 12, 13, 15, 17, 18, 20, 22, 24, 26, 28, 31] + [34] * 6,
                   [8, 51, 119, 238, 398, 568, 816, 1097, 1384, 1689, 1901, 2117, 2329, 2594, 2945] + [3290] * 6,
                   ("0.1599", "0.1070", "0.2094")),
            "A2": ([[7, 7], [13, 13], [20, 20], [27, 27], [33, 33], [40, 40], [47, 47], [53, 53], [60, 60], [67, 67],
                    [75, 75], [83, 83], [91, 91], [101, 96], [115, 96], [128, 96], [148, 96], [168, 96], [188, 96],
                    [208, 96], [224, 96]],
                   [4, 6, 8, 10, 12, 13, 15, 17, 18, 20, 22, 24, 26, 28, 31, 34, 39, 43, 48, 52, 56],
                   [8, 44, 119, 238, 371, 568, 816, 1052, 1384, 1743, 2222, 2754, 3350, 3954, 4540, 5075, 5905, 6738,
                    7565, 8398, 9062],
                   ("0.1781", "0.1320", "0.2401")),
            "A3": ([[6, 6], [13, 13], [20, 20], [26, 26], [33, 33], [40, 40], [46, 46], [53, 53], [60, 60], [67, 67],
                    [75, 75], [83, 83], [91, 91], [101, 96], [114, 96], [128, 96], [148, 96], [168, 96], [188, 96],
                    [208, 96], [224, 96]],
                   [4, 6, 8, 10, 12, 13, 15, 17, 18, 20, 22, 24, 26, 28, 31, 34, 39, 43, 48, 52, 56],
                   [6, 44, 119, 222, 371, 568, 777, 1052, 1384, 1743, 2222, 2754, 3350, 3954, 4500, 5075, 5905, 6738,
                    7565, 8398, 9062],
                   ("0.1682", "0.1322", "0.2327")),
        },
    },
    "sham_at_floor_r": {
        "stop": (128, 45, 224, 78, 224, 78),
        "looks": [
            (40, 7, 7, 7, 7, 6, 6), (80, 14, 14, 13, 13, 13, 13), (120, 20, 20, 20, 20, 20, 20),
            (160, 27, 27, 27, 27, 26, 26), (200, 34, 34, 33, 33, 33, 33), (240, 40, 40, 40, 40, 40, 40),
            (280, 47, 45, 47, 47, 47, 47), (320, 55, 45, 55, 55, 55, 55), (360, 63, 45, 63, 63, 63, 63),
            (400, 71, 45, 71, 71, 71, 71), (440, 80, 45, 80, 78, 79, 78), (480, 93, 45, 93, 78, 93, 78),
            (520, 107, 45, 106, 78, 106, 78), (560, 120, 45, 120, 78, 119, 78), (600, 128, 45, 136, 78, 135, 78),
            (640, 128, 45, 156, 78, 155, 78), (680, 128, 45, 176, 78, 175, 78), (720, 128, 45, 196, 78, 195, 78),
            (760, 128, 45, 216, 78, 215, 78), (777, 128, 45, 224, 78, 224, 78)],
        "bars": {
            "round_degeneracy": ([200, 400, 600, 800, 1000, 1200, 1390, 1550, 1710, 1870] + [2010] * 10,
                                 [16, 28, 40, 51, 63, 74, 84, 93, 102, 110] + [118] * 10, "0.1547"),
            "reasoning_line_defect": ([120, 240, 360, 480, 600, 720, 834, 930, 1026, 1122] + [1206] * 10,
                                      [19, 33, 47, 60, 73, 86, 99, 109, 120, 130] + [139] * 10, "0.1441"),
            "own_pair_lexical": ([130, 260, 400, 530, 660, 800, 940, 1100, 1260, 1420] + [1560] * 10,
                                 [6, 10, 14, 17, 20, 24, 27, 31, 35, 38] + [42] * 10, "0.1482"),
        },
        "guards": {
            "A1": ([[7, 7], [14, 14], [20, 20], [27, 27], [34, 34], [40, 40], [47, 45], [55, 45], [63, 45], [71, 45],
                    [80, 45], [93, 45], [107, 45], [120, 45]] + [[128, 45]] * 6,
                   [4, 6, 8, 10, 12, 13, 15, 17, 19, 21, 23, 26, 29, 32] + [34] * 6,
                   [8, 51, 119, 238, 398, 568, 778, 919, 1060, 1211, 1369, 1604, 1858, 2093] + [2239] * 6,
                   ("0.1595", "0.0957", "0.2050")),
            "A2": ([[7, 7], [13, 13], [20, 20], [27, 27], [33, 33], [40, 40], [47, 47], [55, 55], [63, 63], [71, 71],
                    [80, 78], [93, 78], [106, 78], [120, 78], [136, 78], [156, 78], [176, 78], [196, 78], [216, 78],
                    [224, 78]],
                   [4, 6, 8, 10, 12, 13, 15, 17, 19, 21, 23, 26, 29, 32, 36, 41, 45, 50, 54, 56],
                   [8, 44, 119, 238, 371, 568, 816, 1141, 1529, 1979, 2477, 2910, 3341, 3809, 4332, 4997, 5659, 6329,
                    6989, 7255],
                   ("0.1774", "0.1234", "0.2355")),
            "A3": ([[6, 6], [13, 13], [20, 20], [26, 26], [33, 33], [40, 40], [47, 47], [55, 55], [63, 63], [71, 71],
                    [79, 78], [93, 78], [106, 78], [119, 78], [135, 78], [155, 78], [175, 78], [195, 78], [215, 78],
                    [224, 78]],
                   [4, 6, 8, 10, 12, 13, 15, 17, 19, 21, 23, 26, 29, 32, 36, 40, 45, 49, 54, 56],
                   [6, 44, 119, 222, 371, 568, 816, 1141, 1529, 1979, 2452, 2910, 3341, 3775, 4301, 4968, 5628, 6293,
                    6962, 7255],
                   ("0.1699", "0.1234", "0.2297")),
        },
    },
    "sham_at_floor_min": {
        "stop": (128, 32, 224, 56, 224, 56),
        "looks": [
            (40, 7, 7, 7, 7, 6, 6), (80, 14, 14, 13, 13, 13, 13), (120, 20, 20, 20, 20, 20, 20),
            (160, 27, 27, 27, 27, 26, 26), (200, 34, 32, 34, 34, 33, 33), (240, 42, 32, 42, 42, 41, 41),
            (280, 50, 32, 50, 50, 49, 49), (320, 59, 32, 59, 56, 58, 56), (360, 72, 32, 72, 56, 72, 56),
            (400, 86, 32, 85, 56, 85, 56), (440, 99, 32, 99, 56, 98, 56), (480, 112, 32, 112, 56, 112, 56),
            (520, 126, 32, 125, 56, 125, 56), (560, 128, 32, 144, 56, 144, 56), (600, 128, 32, 164, 56, 164, 56),
            (640, 128, 32, 184, 56, 184, 56), (680, 128, 32, 204, 56, 204, 56), (720, 128, 32, 224, 56, 224, 56)],
        "bars": {
            "round_degeneracy": ([200, 400, 600, 800, 990, 1150, 1310] + [1440] * 11,
                                 [16, 28, 40, 51, 62, 71, 80] + [87] * 11, "0.1370"),
            "reasoning_line_defect": ([120, 240, 360, 480, 594, 690, 786] + [864] * 11,
                                      [19, 33, 47, 60, 73, 83, 94] + [102] * 11, "0.1225"),
            "own_pair_lexical": ([130, 260, 400, 530, 670, 830, 990] + [1120] * 11,
                                 [6, 10, 14, 17, 21, 24, 28] + [31] * 11, "0.1354"),
        },
        "guards": {
            "A1": ([[7, 7], [14, 14], [20, 20], [27, 27], [34, 32], [42, 32], [50, 32], [59, 32], [72, 32], [86, 32],
                    [99, 32], [112, 32], [126, 32]] + [[128, 32]] * 5,
                   [4, 6, 8, 10, 12, 14, 16, 18, 21, 24, 27, 31] + [34] * 6,
                   [8, 51, 119, 238, 373, 470, 568, 679, 840, 1013, 1171, 1331, 1506] + [1530] * 5,
                   ("0.1539", "0.0802", "0.1925")),
            "A2": ([[7, 7], [13, 13], [20, 20], [27, 27], [34, 34], [42, 42], [50, 50], [59, 56], [72, 56], [85, 56],
                    [99, 56], [112, 56], [125, 56], [144, 56], [164, 56], [184, 56], [204, 56], [224, 56]],
                   [4, 6, 8, 10, 12, 14, 16, 18, 21, 24, 27, 31, 34, 38, 42, 47, 51, 56],
                   [8, 44, 119, 238, 398, 633, 925, 1254, 1553, 1855, 2178, 2478, 2780, 3216, 3676, 4138, 4602, 5069],
                   ("0.1746", "0.1086", "0.2265")),
            "A3": ([[6, 6], [13, 13], [20, 20], [26, 26], [33, 33], [41, 41], [49, 49], [58, 56], [72, 56], [85, 56],
                    [98, 56], [112, 56], [125, 56], [144, 56], [164, 56], [184, 56], [204, 56], [224, 56]],
                   [4, 6, 8, 10, 12, 14, 16, 18, 21, 24, 27, 31, 34, 38, 42, 47, 51, 56],
                   [6, 44, 119, 222, 371, 599, 888, 1235, 1553, 1855, 2156, 2478, 2780, 3216, 3676, 4138, 4602, 5069],
                   ("0.1613", "0.1090", "0.2162")),
        },
    },
    "sham_realised": {
        "stop": (128, 64, 224, 96, 224, 96),
        "looks": _PROJ_LOOKS,
        "bars": {
            "round_degeneracy": ([158, 315, 473, 630, 788, 945, 1103, 1260, 1418, 1559, 1685, 1811, 1937] + [2016] * 8,
                                 [14, 23, 33, 42, 51, 60, 68, 77, 86, 93, 100, 107, 114] + [118] * 8, "0.1553"),
            "reasoning_line_defect": ([82, 163, 245, 327, 408, 490, 572, 653, 735, 809, 874, 939, 1005] + [1045] * 8,
                                      [14, 24, 33, 43, 52, 61, 70, 79, 88, 96, 103, 110, 117] + [122] * 8, "0.1601"),
            "own_pair_lexical": ([102, 205, 315, 417, 520, 630, 732, 835, 945, 1055, 1181, 1307, 1433] + [1512] * 8,
                                 [6, 9, 12, 14, 17, 20, 22, 25, 27, 30, 33, 36, 39] + [40] * 8, "0.1333"),
        },
    },
}
REVIEWED_GRID = {  # per contrast arm: the 99 grid displays (j/100), the maximum, the refined maximum, the union's
    "A1": ("0.0006,0.0073,0.0200,0.0330,0.0439,0.0531,0.0609,0.0677,0.0736,0.0787,0.0832,0.0873,0.0909,0.0940,0.0969,"
           "0.0994,0.1016,0.1036,0.1054,0.1070,0.1085,0.1099,0.1111,0.1122,0.1132,0.1140,0.1146,0.1151,0.1155,0.1159,"
           "0.1162,0.1164,0.1167,0.1170,0.1172,0.1174,0.1175,0.1175,0.1175,0.1175,0.1174,0.1173,0.1173,0.1173,0.1173,"
           "0.1173,0.1173,0.1174,0.1175,0.1176,0.1177,0.1178,0.1179,0.1179,0.1179,0.1179,0.1179,0.1178,0.1176,0.1175,"
           "0.1174,0.1173,0.1172,0.1171,0.1170,0.1169,0.1167,0.1164,0.1161,0.1158,0.1155,0.1153,0.1150,0.1147,0.1143,"
           "0.1138,0.1130,0.1120,0.1108,0.1093,0.1075,0.1056,0.1034,0.1010,0.0984,0.0956,0.0925,0.0890,0.0851,0.0807,"
           "0.0759,0.0704,0.0644,0.0580,0.0514,0.0445,0.0365,0.0256,0.0099",
           ("0.1179", "11/20"), ("0.1179", "11/20", ["27/50", "14/25"]), ("0.2094", "1/5")),
    "A2": ("0.0033,0.0229,0.0428,0.0563,0.0668,0.0759,0.0838,0.0904,0.0961,0.1012,0.1057,0.1096,0.1132,0.1166,0.1198,"
           "0.1229,0.1257,0.1282,0.1302,0.1320,0.1335,0.1349,0.1361,0.1372,0.1382,0.1392,0.1400,0.1406,0.1412,0.1416,"
           "0.1420,0.1423,0.1426,0.1428,0.1431,0.1433,0.1434,0.1435,0.1434,0.1433,0.1432,0.1430,0.1427,0.1425,0.1422,"
           "0.1418,0.1415,0.1413,0.1411,0.1410,0.1410,0.1412,0.1415,0.1419,0.1423,0.1427,0.1431,0.1434,0.1437,0.1438,"
           "0.1440,0.1440,0.1439,0.1438,0.1436,0.1434,0.1432,0.1430,0.1428,0.1425,0.1422,0.1417,0.1412,0.1405,0.1397,"
           "0.1388,0.1378,0.1367,0.1354,0.1339,0.1321,0.1301,0.1277,0.1251,0.1222,0.1191,0.1159,0.1124,0.1085,0.1044,"
           "0.1000,0.0953,0.0899,0.0828,0.0737,0.0632,0.0517,0.0385,0.0191",
           ("0.1440", "31/50"), ("0.1440", "309/500", ["61/100", "63/100"]), ("0.2401", "1/5")),
    "A3": ("0.0033,0.0228,0.0427,0.0563,0.0668,0.0761,0.0841,0.0909,0.0969,0.1022,0.1069,0.1109,0.1144,0.1177,0.1209,"
           "0.1238,0.1264,0.1286,0.1305,0.1322,0.1336,0.1349,0.1361,0.1372,0.1382,0.1392,0.1401,0.1409,0.1416,0.1423,"
           "0.1428,0.1434,0.1439,0.1444,0.1450,0.1455,0.1460,0.1465,0.1470,0.1473,0.1477,0.1480,0.1482,0.1484,0.1485,"
           "0.1485,0.1484,0.1484,0.1483,0.1483,0.1483,0.1483,0.1484,0.1485,0.1486,0.1486,0.1486,0.1484,0.1482,0.1479,"
           "0.1475,0.1471,0.1466,0.1460,0.1455,0.1450,0.1445,0.1441,0.1437,0.1433,0.1428,0.1423,0.1416,0.1408,0.1400,"
           "0.1390,0.1381,0.1370,0.1358,0.1344,0.1329,0.1311,0.1289,0.1265,0.1237,0.1207,0.1175,0.1140,0.1100,0.1056,"
           "0.1009,0.0959,0.0900,0.0824,0.0730,0.0627,0.0517,0.0386,0.0191",
           ("0.1486", "14/25"), ("0.1486", "559/1000", ["11/20", "57/100"]), ("0.2327", "1/5")),
}
REVIEWED_HOURS = ("148.28", "164.92", "148", "165")
# The unit's guard figure per case, GUARD_UNIT_RULE over the same recomputation's exact unions (Code, standard library).
REVIEWED_GUARD_UNIT = {"projection": "0.5390", "sham_at_floor_r": "0.5318", "sham_at_floor_min": "0.5105"}
REVIEWED_EXACT_SHA256 = "ab9f2fc8ab5d753d374ba40d9304610a0d6235731db3ec6838d060fdd0f89575"


# --- small exact helpers -------------------------------------------------------------------------------------------
def half_up(x: Fraction) -> int:
    """The nearest integer to a non-negative Fraction, a half up: floor(x + 1/2)."""
    x = Fraction(x)
    return (2 * x.numerator + x.denominator) // (2 * x.denominator)


def frac_text(x: Fraction) -> str:
    """m_gpwr.fs's form, an integer without its "/1"."""
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else M.fs(x)


def short(x: Fraction, places: int = 2) -> str:
    """A probability as the proposal writes it: ".05", ".70" (half-up at `places`, the leading zero dropped)."""
    d = M.dec(Fraction(x), places)
    if not d.startswith("0."):
        raise ValueError(f"short() serves probabilities below 1, got {x}")
    return d[1:]


def hours_col(total: int) -> str:
    """m:234-241's hours column at m:230's basis: the whole hours at each end, a half up."""
    return f"{half_up(total * BASIS_S[0] / 3600)}–{half_up(total * BASIS_S[1] / 3600)}"


def row_label(rg: range) -> str:
    return f"{max(rg)}–{min(rg)}" if len(rg) > 1 else str(rg[0])


# --- the committed texts the inputs are read from ------------------------------------------------------------------
def build_sources(over: dict | None = None) -> tuple:
    """The committed texts the inputs are quoted from: (revision, path, the blob's sha256 or None, the quotes it must
    carry), every quote built from the constants this program computes with (over: the self-test's perturbations). A
    revision "LOAD" is the load commit."""
    v = {"K": K, "N_Q": N_Q, "PER_TEMPLATE": PER_TEMPLATE, "FLOORS": schedule.FLOORS, "UNIT_SIZE": schedule.UNIT_SIZE,
         "LOOK_EVERY": LOOK_EVERY, "PATH": PATH, "POWER_SPEC": POWER_SPEC, "POWER_ORACLE": POWER_ORACLE,
         "POWER_FLOOR": M.POWER_FLOOR, "BAR_ROWS": BAR_ROWS, "LEXICAL": DOMAIN_ARMS["lexical_sham"],
         "SHAM_QUAL": SHAM_QUAL, "REALISED": REALISED, "BASIS_S": BASIS_S, "TABLE_ROWS": TABLE_ROWS,
         "TABLE_AFTER": TABLE_AFTER, "M330_LOOKS": M330_LOOKS, "A5_ROWS": A5_ROWS, "A5_TOTAL": A5_TOTAL,
         "SEAT_A7": SEAT_A7, "F5_TEXT": F5_TEXT, "Q7": (Q7_PRE, Q7_A, Q7_B, Q7_C), "SEAT_SHA256": SEAT_SHA256,
         "PROPOSAL_M_SHA256": PROPOSAL_M_SHA256, "F5_SHA256": F5_SHA256, "Q7_SHA256": Q7_SHA256,
         "GF3_COMMIT": GF3_COMMIT}
    v.update(over or {})
    FL, US, PS, PO, B, RL = v["FLOORS"], v["UNIT_SIZE"], v["POWER_SPEC"], v["POWER_ORACLE"], v["BASIS_S"], v["REALISED"]
    k, nq, pf, br = v["K"], v["N_Q"], v["POWER_FLOOR"], v["BAR_ROWS"]
    pt = ", ".join(f"{a} {v['PER_TEMPLATE'][a][0]}/{v['PER_TEMPLATE'][a][1]}" for a in SEAT_ORDER)
    k29 = [(rg, row) for rg, row in v["TABLE_ROWS"].items() if 29 in rg]
    (rg29, (a1, a1s, a23, a23s, tot, lk, _h)), = k29 if len(k29) == 1 else [(range(0), (0,) * 7)]
    rows_m = tuple(f"| {row_label(rg)} | {r[0]} | {r[1]} | {r[2]} | {r[3]} | **{r[4]}** | {r[5]} | {r[6]} |"
                   for rg, r in v["TABLE_ROWS"].items())
    after = "(k = " + "; ".join(("… " if kk == 1 else "") + f"{kk}: {t:,}"
                                for kk, t in v["TABLE_AFTER"].items()) + ".)"
    looks330 = ", ".join(f"{n} at {' and '.join(str(t) for t in ts)}" for n, ts in v["M330_LOOKS"]) + " (uncached)"
    seat = (v["SEAT_A7"], f"**r = {k}/{nq}** ({pt})", f"By template {pt}, as the block has it.",
            f"`round_degeneracy` 7 of {RL['rounds'][0]} sham rounds", f"m:297's 19 is at the planned {RL['rounds'][1]}",
            f"`reasoning_line_defect` 2 of {RL['lines'][0]} lines", f"m:297's 22 is at the planned {RL['lines'][1]}",
            f"m:238's uncached planning row at k {row_label(rg29)} is **{v['A5_TOTAL']} launches** (A1 {a1}, A1s "
            f"{a1s}, A2 {a23}, A2s {a23s}, A3 {a23}, A3s {a23s}; looks {lk})",
            f"The campaign's detached generation, {v['A5_TOTAL']} launches × the basis:",
            "**The cap is the PI's, at G-PWR's entry, written into LOCK-m-F3 v1.0** (m:298, m:249)",
            "**Your cap for Q-F3**, at G-PWR's entry",
            f"the G-F3 entry (`{v['GF3_COMMIT']}`)") + tuple(v["A5_ROWS"])
    entry = (f"**{k} of {nq} sessions are valid, so r for Q-F3's launch rule is {k}/{nq}** (m:192)",
             f"Both binomial bars, on the {v['SHAM_QUAL']} sham sessions' realised counts, are silent:",
             f"`round_degeneracy` 7/{RL['rounds'][0]} and `reasoning_line_defect` 2/{RL['lines'][0]}, each against a "
             f"critical of 16 at its realised n.")
    prop = rows_m + (
        after,
        f"| A1 / A1s | **Q-F3** | F3 | same | same | {FL['A1']['cached']} cached, {FL['A1']['uncached']} uncached / "
        f"{FL['A1s']} | control α {short(PS['A1'][0])} / sham | {US['A1']} |",
        f"| A2 / A2s | **Q-F3** | F3 | COMMON + TOLD-OBJ | same | {FL['A2']} / {FL['A2s']} | confirmatory α "
        f"{short(PS['A2'][0])} / sham | {US['A2']} |",
        f"| A3 / A3s | **Q-F3** | F3 | COMMON | same | {FL['A3']} / {FL['A3s']} | screen (PROPOSAL-f:101–106) "
        f"α {short(PS['A3'][0])} / sham | {US['A3']} |",
        f"A0/A1 ({FL['A1']['cached']}, {FL['A1s']}): {PO['A1_cached_96_32']} at P = {short(PS['A1'][1])}; "
        f"({FL['A1']['uncached']}, {FL['A1s']}): {PO['A1']}",
        f"A2 ({FL['A2']}, {FL['A2s']}): {PO['A2']} at P = {short(PS['A2'][1])}, α = {short(PS['A2'][0])}",
        f"A3 ({FL['A3']}, {FL['A3s']}), α = {short(PS['A3'][0])}: POSITIVE probability {PO['A3']} at P = "
        f"{short(PS['A3'][1])}",
        f"**Power floors:** A2 ≥ {short(pf)} at P = {short(PS['A2'][1])}; every control ≥ {short(pf)} at "
        f"P = {short(PS['A1'][1])}.",
        "L = ceil_unit( max( ⌈1.15 · floor⌉, N₉₀(r) ) )",
        f"n_q = 24 for Q-F0 and each OLMo checkpoint, {nq} for Q-F3",
        f"looks = ⌈total/{v['LOOK_EVERY']}⌉, §6",
        f"Q-F3 uncached (A1 floor {FL['A1']['uncached']}; basis **{M.dec(B[0], 1)}–{M.dec(B[1], 1)} s per session",
        "Hour caps: wall-clock of detached generation time, set by the PI in that unit's LOCK v1.0",
        "**G-PWR (each LOCK v1.0).** §2.4's power with planned floors; any n raised; launch counts from the unit's "
        "k; the unit's look count and the exact sequential false-pause probabilities of §6 for that look count; "
        "the exclusion guard's false-pause figure.",
        f"`round_degeneracy` on the sham sessions' ≤ {RL['rounds'][1]} rounds, p0 "
        f"{short(br['round_degeneracy'][1])} (critical 19); **reasoning-line defects** on the sham sessions' ≤ "
        f"{RL['lines'][1]} lines, p0 {short(br['reasoning_line_defect'][1])} (critical 22)",
        f"r for Q-F3 = pooled over all {nq}.",
        "**G-VER, G-PWR, LOCK-m-F3 v1.0** as §3.1, with D2 and the hash of the preprint of record as edited for v2.",
        f"one-sided Fisher exact at α {short(br['exclusion_guard_fisher'][2])} (**binding on both substrates**)",
        f"— **{short(br['exclusion_guard_abs'][1])} on Qwen,",
        f"Cadence every {v['LOOK_EVERY']} launches and at the end",
        looks330,
        f"`round_degeneracy` — Qwen p0 {short(br['round_degeneracy'][1])}, OLMo p0 .02, domain the unit's sham "
        f"arms",
        f"**[Q-F3]** reasoning-line defects p0 {short(br['reasoning_line_defect'][1])}, domain the three F3 sham arms",
        f"p0 {short(br['own_pair_lexical'][1])} per task round",
        f"domain {' and '.join(v['LEXICAL'])}, reported for the label-naming arms")
    return (
        (SEAT_COMMIT_FULL, SEAT_RAW, v["SEAT_SHA256"], seat),
        (GF3_COMMIT_FULL, "RESULTS.md", None, entry),
        ("LOAD", PROPOSAL_M, v["PROPOSAL_M_SHA256"], prop),
        ("LOAD", LOCK_F3, None,
         (f"- **`path = {v['PATH']}`.** G-ID-F3 computed FAIL (`efb7bef`)",
          f"**The campaign's launches** are the {v['PATH']} table's, m:234–241 (v0.2 §4)")),
        ("LOAD", F5_RAW, v["F5_SHA256"], ("- **F-5.** " + v["F5_TEXT"],)),
        ("LOAD", Q7_RAW, v["Q7_SHA256"], ("## Q7 — G-PWR's methods", v["Q7"][0] + ":", "- **(a)** " + v["Q7"][1],
                                          "- **(b)** " + v["Q7"][2], "- **(c)** " + v["Q7"][3])),
        ("LOAD", "valence_core/mf3/resume.py", None, ("from valence_core.m import resume as m_resume",
                                                      "LOOK_EVERY = m_resume.LOOK_EVERY")),
    )


SOURCES = build_sources()
QUOTE_COUNTS = (18, 3, 33, 2, 1, 5, 2)   # each source's quotes as built: a quote dropped from build_sources fails


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
        probs += [f"{rev}:{rel}: lacks {q[:70]!r}" for q in quotes if q not in text]
        rec_.append({"commit": commit, "path": rel, "sha256": sha})
    return probs, rec_


def sources_problems(load_commit: str) -> tuple[list[str], list[dict]]:
    """sources_record's problems, and each source read at its own commit (sources_commits_ok; the review's MINOR-2):
    the self-test's sources check and the run of record both take the sources from here."""
    probs, rec_ = sources_record(load_commit)
    if not probs and not sources_commits_ok(rec_):
        probs = probs + [f"the inputs were not each read at its own commit: {[s['commit'] for s in rec_]}"]
    return probs, rec_


def citation_problems() -> list[str]:
    """The pinned commits are the citations they stand for (the review's MINOR-B): each abbreviation is its full sha's
    prefix (2193832 as the seat's raw cites the G-F3 entry, a quote build_sources binds), and each text first appears
    at its pinned commit, absent from that commit's first parent."""
    out = []
    if not (SEAT_COMMIT_FULL.startswith(SEAT_COMMIT) and GF3_COMMIT_FULL.startswith(GF3_COMMIT)):
        out.append(f"an abbreviation is not its pinned commit's prefix: {SEAT_COMMIT}, {GF3_COMMIT}")
    try:
        _commit_blob(SEAT_COMMIT_FULL + "^", SEAT_RAW)
        out.append(f"{SEAT_RAW} is already in {SEAT_COMMIT_FULL}'s parent: not the commit that placed it")
    except _GitRead:
        pass
    try:
        before = _commit_blob(GF3_COMMIT_FULL + "^", "RESULTS.md")[1].decode("utf-8")
    except _GitRead as e:
        return out + [f"RESULTS.md at {GF3_COMMIT_FULL}'s parent: {e}"]
    entry = next(q for _, rel, _, q in SOURCES if rel == "RESULTS.md")
    return out + [f"the G-F3 entry's quote {x[:50]!r} is already in {GF3_COMMIT_FULL}'s parent" for x in entry
                  if x in before]


# --- the bars of record --------------------------------------------------------------------------------------------
def bar_name(cls: str) -> str:
    return f"{cls}@{TAG}"


def f3_bars() -> dict:
    return {b.name: b for b in F3B.QF3_BARS}


def bar_of(cls: str):
    return f3_bars()[bar_name(cls)]


def bar_problems_f3(by_name: dict | None = None) -> list[str]:
    """The constants this program computes with, against mf3's bars of record (the campaign rows of bars.QF3_BARS:
    kind, p0, alpha, domain, binding); the guard's p0 and alphas against m_gpwr's GUARD_ABS_P0 and ALPHA, which
    m_gpwr.guard_block computes with; the per-session units and the domains' arms; the arithmetic, m's."""
    B = f3_bars() if by_name is None else by_name
    out = [f"{bar_name(c)}: missing" for c in BAR_ROWS if bar_name(c) not in B]
    if out:
        return out
    for cls, want in BAR_ROWS.items():
        b = B[bar_name(cls)]
        got = (b.kind, b.p0q, b.alphaq, b.domain, b.binding)
        if got != want:
            out.append(f"{bar_name(cls)}: {got}")
    a, f = B[bar_name("exclusion_guard_abs")], B[bar_name("exclusion_guard_fisher")]
    if (a.p0q, a.alphaq, f.alphaq) != (M.GUARD_ABS_P0, M.ALPHA, M.ALPHA):
        out.append("the guard's p0 and alphas are not m_gpwr's GUARD_ABS_P0 and ALPHA")
    if (F3B.MAX_ROUNDS, F3B.MAX_LINES, bars.MAX_ROUNDS) != (10, 6, 10):
        out.append("the units per session are not 10 task rounds and 6 reasoning lines")
    if (tuple(SHAM), tuple(F3B.LEXICAL_SHAM), tuple(CONTRAST)) != (("A1s", "A2s", "A3s"), ("A2s", "A3s"),
                                                                  ("A1", "A2", "A3")):
        out.append("the domains' arms are not A1s/A2s/A3s (sham), A2s/A3s (lexical), A1/A2/A3 (contrast)")
    if F3B.critical_k is not bars.critical_k or F3B.seq_false_pause is not bars.seq_false_pause:
        out.append("mf3's bars do not carry valence_core.m.bars' critical_k and seq_false_pause")
    return out


def guard_halves(by_name: dict | None = None) -> tuple[str, ...]:
    """The guard's halves whose fire pauses, read from the bars' binding flags (m:316: both bind on Qwen)."""
    B = f3_bars() if by_name is None else by_name
    a, f = B[bar_name("exclusion_guard_abs")], B[bar_name("exclusion_guard_fisher")]
    return tuple(h for h, b in (("abs", a), ("fisher", f)) if b.binding)


# --- the composition ----------------------------------------------------------------------------------------------
def project_arms(stop: dict, arms=None, interleave=None) -> list[dict]:
    """m_gpwr.project's form over any arm list: the launch sequence under `interleave` (mf3's schedule.interleave by
    default: the live arm with the fewest launches next, ties to table order, an arm out of the rotation for good once
    done), each arm launching until it has launched stop[arm] times; looks at every LOOK_EVERY-th launch and at the end
    (m:330), an end on a multiple adding no look. Returns the looks with the cumulative launches per arm."""
    arms = tuple(ARMS if arms is None else arms)
    interleave = schedule.interleave if interleave is None else interleave
    if not all(type(stop.get(a)) is int and stop[a] >= 1 for a in arms):
        raise ValueError(f"project_arms: every arm launches at least once, got {stop}")
    counts = {a: 0 for a in arms}
    it = interleave(list(arms), lambda a: counts[a] >= stop[a])
    looks, total = [], 0
    for arm in it:
        counts[arm] += 1
        total += 1
        if total % LOOK_EVERY == 0:
            looks.append({"look": len(looks) + 1, "launches": total, **{a: counts[a] for a in arms}})
        if all(counts[a] >= stop[a] for a in arms):
            break
    if not looks or looks[-1]["launches"] != total:
        looks.append({"look": len(looks) + 1, "launches": total, **{a: counts[a] for a in arms}, "end": True})
    else:
        looks[-1]["end"] = True
    return looks


def bar_figure(ns: list[int], b) -> dict:
    """m_gpwr.degeneracy's three fields for any binomial bar, at the bar's own p0 and alpha (mf3's bars' arithmetic,
    valence_core.m.bars')."""
    return {"n_j": list(ns), "crit_j": [F3B.critical_k(n, b.p0q, b.alphaq) for n in ns],
            "false_pause": M.rec(F3B.seq_false_pause(ns, b.p0q, b.alphaq))}


def guard_for_pair(looks: list[dict], c: str, s: str, with_grid: bool, halves: tuple | None = None) -> dict:
    """m_gpwr.guard_block on one contrast arm and its matched sham, in m_gpwr's arm roles (the contrast as A0, the sham
    as A0s), with the pausing figure read from the halves that bind."""
    gb = M.guard_block([{"A0": lk[c], "A0s": lk[s]} for lk in looks], with_grid=with_grid)
    halves = guard_halves() if halves is None else tuple(halves)
    fig = GUARD_FIGURE[halves]
    return {**gb, "guard_figure": {"pausing_halves": list(halves), "figure": fig,
                                   "at_common_rate_p0": gb["at_common_rate_p0"][fig]}}


def guard_unit(guards: dict, fig: str) -> dict:
    """The unit's guard figure: the probability that some pair's guard pauses, GUARD_UNIT_RULE over each pair's pausing
    figure at the common rate (exact: under Q7 (b)'s model the three pairs share no session, so their events are
    independent)."""
    surv = Fraction(1)
    for c in CONTRAST:
        surv *= 1 - Fraction(guards[c]["guard_figure"]["at_common_rate_p0"]["exact"])
    return {"rule": GUARD_UNIT_RULE, "pairs": [list(p) for p in PAIRS], "figure_per_pair": fig, **M.rec(1 - surv)}


def case_units(looks: list[dict], per: dict, rounding: bool) -> dict:
    """Each bar's n_j over its own domain: the domain arms' cumulative launches at each look x the units per launch;
    whole at every look, or (the realised case) rounded half up per cumulative count, the exact values beside."""
    out = {}
    for cls in BAR_CLASSES:
        dom = DOMAIN_ARMS[bar_of(cls).domain]
        rate = Fraction(per[UNIT_OF[cls]])
        exact = [Fraction(sum(lk[a] for a in dom)) * rate for lk in looks]
        if rounding:
            out[cls] = ([half_up(x) for x in exact], [M.fs(x) for x in exact])
        else:
            if any(x.denominator != 1 for x in exact):
                raise SystemExit(f"STOP: non-integer {UNIT_OF[cls]} for {cls}: {[M.fs(x) for x in exact][:4]}")
            out[cls] = ([int(x) for x in exact], None)
    return out


def power_block_f3(m) -> dict:
    """m:190's power at the planned floors per contrast arm, by the analyzer's f3_power_block (its planned figure, at
    mf3's floors); A1 and A2 gated at .85, A3 (the screen) reported. A floor not met STOPs (m:190's raise is the
    seat's to apply, never this program's)."""
    arms = {}
    for a in CONTRAST:
        fl, sf = FLOOR[a], FLOOR[keys.sham_of(a)]
        half = fl // 2
        pb = m.f3_power_block(a, half, fl - half, sf, PATH)
        of, plan = pb["of_record"], pb["planned"]
        if (plan["n"], plan["mS"], of["n"], of["mS"]) != (fl, sf, fl, sf) or plan["exact"] != of["exact"]:
            raise SystemExit(f"STOP: {a}: the analyzer's planned floors {(plan['n'], plan['mS'])} are not mf3's "
                             f"{(fl, sf)} on the {PATH} path")
        if (Fraction(of["alpha"]), Fraction(of["P"])) != POWER_SPEC[a]:
            raise SystemExit(f"STOP: {a}: the analyzer's alpha and P {(of['alpha'], of['P'])} are not m:190's")
        pw = Fraction(plan["exact"])
        gated = a in POWER_GATED
        if gated and pw < M.POWER_FLOOR:
            raise SystemExit(f"STOP: {a}: power at the planned floors {M.dec(pw)} is below .85; m:190 raises n in "
                             f"whole units, a rule this program does not apply -- escalate (Code never "
                             f"self-adjudicates)")
        arms[a] = {"n": fl, "split": list(of["split"]), "mS": sf, "alpha": of["alpha"], "P": of["P"],
                   **M.rec(pw, 3), "exact4": M.dec(pw), "gated": gated}
    bc = m.f3_power_block("A1", 48, 48, 32, "cached")["planned"]
    if (bc["n"], bc["mS"]) != (schedule.FLOORS["A1"]["cached"], FLOOR["A1s"]):
        raise SystemExit(f"STOP: the analyzer's cached A1 floors {(bc['n'], bc['mS'])} are not m:184's")
    bpw = Fraction(bc["exact"])
    return {"arms": arms, "power_floor": M.fs(M.POWER_FLOOR), "n_raised": False, "basis": POWER_BASIS,
            "beside_A1_cached_96_32": {"n": bc["n"], "mS": bc["mS"], **M.rec(bpw, 3), "exact4": M.dec(bpw),
                                       "used": False}}


_LC_MEMO: dict = {}


def _launch_count(floor: int, k: int, n_q: int, unit: int) -> dict:
    """m_gpwr.launch_count at r = k/n_q, memoised within the process (A2/A3 and A2s/A3s share their floors)."""
    key = (floor, k, n_q, unit)
    if key not in _LC_MEMO:
        _LC_MEMO[key] = M.launch_count(floor, Fraction(k, n_q), unit)
    return dict(_LC_MEMO[key])


def rows_by_k() -> dict:
    """m:192's row for every k = 1..n_q at the unit's floors and balance units: L per arm, the total, the looks."""
    rows = {}
    for k in range(1, N_Q + 1):
        lk = {a: _launch_count(FLOOR[a], k, N_Q, UNIT_SIZE[a])["L"] for a in ARMS}
        t = sum(lk.values())
        rows[str(k)] = {**lk, "total": t, "looks": looks_for(t)}
    return rows


def rows_problems(rows: dict) -> list[str]:
    """The rows against mf3's _n90_exact and the oracles of record: m:234-241's rows (their looks and hours columns
    too), m:243's line after the table, m:330's uncached look counts."""
    out = []
    if sorted(int(k) for k in rows) != list(range(1, N_Q + 1)):
        return ["rows: k is not 1..n_q"]
    for k in range(1, N_Q + 1):
        row = rows[str(k)]
        bad = [a for a in ARMS if row[a] != _N90_EXACT(FLOOR[a], k, N_Q, UNIT_SIZE[a])]
        if bad:
            out.append(f"k {k}: m_gpwr's L is not mf3's _n90_exact for {bad}")
        if row["total"] != sum(row[a] for a in ARMS) or row["looks"] != -(-row["total"] // LOOK_EVERY):
            out.append(f"k {k}: total or looks")
    for rg, (a1, a1s, a23, a23s, tot, lk, h) in TABLE_ROWS.items():
        for k in rg:
            row = rows[str(k)]
            if tuple(row[x] for x in ARMS + ("total", "looks")) != (a1, a1s, a23, a23s, a23, a23s, tot, lk):
                out.append(f"k {k}: not m:234-241's row {row_label(rg)}")
        if hours_col(tot) != h:
            out.append(f"row {row_label(rg)}: hours {hours_col(tot)} at m:230's basis, not the table's {h}")
    for k, tot in TABLE_AFTER.items():
        if rows[str(k)]["total"] != tot:
            out.append(f"k {k}: total {rows[str(k)]['total']}, not m:243's {tot}")
    for n_looks, totals in M330_LOOKS:
        out += [f"m:330: {t} launches give {looks_for(t)} looks, not {n_looks}" for t in totals
                if looks_for(t) != n_looks]
    return out


def compute(m) -> dict:
    """The record's figures (m:285 for Q-F3, on Q7's methods). STOPs, in order: the bars; k = 0; a power floor; the
    launch cross-check; a launch row other than m:238's; non-integer units; the realised case's denominators; the
    look count; the rows' oracles; the citation's total."""
    bp = bar_problems_f3()
    if bp:
        raise SystemExit(f"STOP: this program's constants differ from the bars of record: {bp}")
    if type(K) is not int or type(N_Q) is not int or N_Q < 1 or not 0 <= K <= N_Q:
        raise ValueError(f"k must be an int in [0, n_q] and n_q a positive int, got k {K!r}, n_q {N_Q!r}")
    if K == 0:
        raise SystemExit("STOP: k = 0 -- m:192: the rule yields no launch count; G-PWR cannot run, LOCK v1.0 cannot be "
                         "committed")
    r = Fraction(K, N_Q)
    power = power_block_f3(m)
    launch = {a: M.launch_count(FLOOR[a], r, UNIT_SIZE[a]) for a in ARMS}
    for a in ARMS:
        if launch[a]["L"] != _N90_EXACT(FLOOR[a], K, N_Q, UNIT_SIZE[a]):
            raise SystemExit(f"STOP: the launch rule disagrees with mf3's schedule._n90_exact for {a}")
    L = {a: launch[a]["L"] for a in ARMS}
    total = sum(L.values())
    n_looks = looks_for(total)
    own = [(rg, row) for rg, row in TABLE_ROWS.items() if K in rg]
    if len(own) != 1 or (L["A1"], L["A1s"], L["A2"], L["A2s"], L["A3"], L["A3s"], total) != \
            (own[0][1][0], own[0][1][1], own[0][1][2], own[0][1][3], own[0][1][2], own[0][1][3], own[0][1][4]):
        raise SystemExit(f"STOP: the launch row at k = {K} ({L}, total {total}) is not m:234-241's")
    floor_r = {a: ceil(Fraction(FLOOR[a]) / r) for a in SHAM}
    whole = {"rounds": Fraction(PER_SESSION["rounds"]), "lines": Fraction(PER_SESSION["lines"])}
    cases = {
        "projection": {"stop": dict(L), "per": whole, "rounding": False},
        "sham_at_floor_r": {"stop": {**L, **floor_r}, "per": whole, "rounding": False},
        "sham_at_floor_min": {"stop": {**L, **{a: FLOOR[a] for a in SHAM}}, "per": whole, "rounding": False},
        "sham_realised": {"stop": dict(L), "per": None, "rounding": True},
    }
    units = {}
    for name in CASE_ORDER:                 # the cheap pass: every case's looks and units, checked before any figure
        cs = cases[name]
        if cs["per"] is None:
            if any(REALISED[u][1] != SHAM_QUAL * PER_SESSION[u] for u in ("rounds", "lines")):
                raise SystemExit(f"STOP: G-F3's planned units {REALISED} are not {SHAM_QUAL} sham sessions x "
                                 f"{PER_SESSION}")
            cs["per"] = {u: Fraction(*REALISED[u]) * PER_SESSION[u] for u in ("rounds", "lines")}
        cs["looks"] = project_arms(cs["stop"])
        cs["n_looks"] = len(cs["looks"])
        units[name] = case_units(cs["looks"], cs["per"], cs["rounding"])
    proj = cases["projection"]
    if proj["n_looks"] != n_looks:
        raise SystemExit(f"STOP: the projection's looks {proj['n_looks']} differ from ceil(total/40) = {n_looks}")
    rows = rows_by_k()
    rp = rows_problems(rows)
    if rp:
        raise SystemExit(f"STOP: the rows by k differ from the oracles of record: {rp[:4]}")
    same_row = [int(k) for k in rows if all(rows[k][a] == L[a] for a in ARMS)]
    if total != A5_TOTAL:
        raise SystemExit(f"STOP: the total {total} is not the {A5_TOTAL} launches §A.5's hours are figured on")
    halves = guard_halves()
    fig = GUARD_FIGURE[halves]
    out_cases = {}
    for name in CASE_ORDER:
        cs = cases[name]
        oc = {"stop": cs["stop"], "per_sham_launch": {u: frac_text(cs["per"][u]) for u in ("rounds", "lines")},
              "rounding": "half up, per cumulative count" if cs["rounding"] else "none",
              "looks": cs["looks"], "n_looks": cs["n_looks"], "bars": {}}
        for cls in BAR_CLASSES:
            ns, ex = units[name][cls]
            oc["bars"][cls] = bar_figure(ns, bar_of(cls))
            if ex is not None:
                oc["bars"][cls]["n_j_exact"] = ex
        if name != "sham_realised":
            oc["guards"] = {c: guard_for_pair(cs["looks"], c, s, with_grid=(name == "projection"), halves=halves)
                            for c, s in PAIRS}
            oc["guard_unit"] = guard_unit(oc["guards"], fig)
        out_cases[name] = oc
    pc = out_cases["projection"]
    hours = {"basis_line": "m:230", "basis_s_per_session": [M.fs(b) for b in BASIS_S], "launches": total,
             "hours": [hours_rec(Fraction(total) * b / 3600) for b in BASIS_S],
             "m238_column": own[0][1][6]}
    return {
        "schema": SCHEMA, "unit": UNIT, "path": PATH,
        "inputs": {"k": K, "n_q": N_Q, "r": M.fs(r),
                   "per_template_beside": {a: f"{PER_TEMPLATE[a][0]}/{PER_TEMPLATE[a][1]}" for a in ARMS},
                   "floors": dict(FLOOR), "balance_units": dict(UNIT_SIZE), "look_every": LOOK_EVERY,
                   "bars": {cls: {"name": bar_name(cls), "p0": M.fs(bar_of(cls).p0q), "alpha": M.fs(bar_of(cls).alphaq),
                                  "domain": bar_of(cls).domain, "domain_arms": list(DOMAIN_ARMS[bar_of(cls).domain]),
                                  "unit": UNIT_OF[cls], "per_session": PER_SESSION[UNIT_OF[cls]],
                                  "binding": bar_of(cls).binding} for cls in BAR_CLASSES},
                   "guard": {"abs_p0": M.fs(M.GUARD_ABS_P0), "alpha": M.fs(M.ALPHA), "unit": "sessions launched",
                             "pausing_halves": list(halves), "pairs": [list(p) for p in PAIRS]},
                   "realised_at_G-F3": {"sham_sessions": SHAM_QUAL, "task_rounds": list(REALISED["rounds"]),
                                        "reasoning_lines": list(REALISED["lines"])}},
        "power": power,
        "launch": {"rule": launch, "L": L, "total": total, "looks": n_looks, "k_with_this_row": sorted(same_row),
                   "rows_by_k": rows},
        "cases": out_cases,
        "joint": {"figure": "each bar's own (projection case)",
                  "figures": {cls: pc["bars"][cls]["false_pause"] for cls in BAR_CLASSES},
                  "guards_beside": {c: pc["guards"][c]["guard_figure"]["at_common_rate_p0"] for c in CONTRAST},
                  "guards_beside_figure": fig, "guard_unit_beside": pc["guard_unit"],
                  "not_computed": JOINT_SENTENCE},
        "hours": hours,
        "beside_A5": {"raw": SEAT_RAW, "commit": SEAT_COMMIT, "sha256": SEAT_SHA256, "section": "§A.5",
                      "launches": A5_TOTAL, "rows": list(A5_ROWS)},
        "cap": CAP, "not_figured": dict(NOT_FIGURED), "readings": list(READINGS),
    }


def hours_rec(h: Fraction) -> dict:
    return {"exact": M.fs(h), "display": M.dec(h, 2), "whole": str(half_up(h))}


# --- the record's checks -------------------------------------------------------------------------------------------
def display_problems(res: dict) -> list[str]:
    """Every {exact, display} pair, at any depth, displays its exact value half-up: the power at three places (and its
    exact4 at four), the hours at two (and whole), everything else at four."""
    bad = []

    def walk(x, path):
        if isinstance(x, dict):
            if "exact" in x and "display" in x and isinstance(x["exact"], str):
                if path.startswith("$.power"):
                    places = 3
                    if x.get("exact4") != M.dec(Fraction(x["exact"]), 4):
                        bad.append(path + ".exact4")
                elif path.startswith("$.hours"):
                    places = 2
                    if x.get("whole") != str(half_up(Fraction(x["exact"]))):
                        bad.append(path + ".whole")
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


def exact_figures(res: dict) -> dict:
    """The record's exact values in the canonical form REVIEWED_EXACT_SHA256 is taken over."""
    out = {"power": {a: res["power"]["arms"][a]["exact"] for a in CONTRAST}, "cases": {}, "grid": {},
           "hours": [h["exact"] for h in res["hours"]["hours"]]}
    out["power"]["A1_cached_96_32"] = res["power"]["beside_A1_cached_96_32"]["exact"]
    for name in CASE_ORDER:
        cs = res["cases"][name]
        e = {"bars": {cls: cs["bars"][cls]["false_pause"]["exact"] for cls in BAR_CLASSES}}
        if "guards" in cs:
            e["guards"] = {c: {h: cs["guards"][c]["at_common_rate_p0"][h]["exact"] for h in ("abs", "fisher", "union")}
                           for c in CONTRAST}
        out["cases"][name] = e
    for c in CONTRAST:
        g = res["cases"]["projection"]["guards"][c]
        out["grid"][c] = {"values": [x["fisher"]["exact"] for x in g["fisher_grid"]],
                          "max": g["fisher_grid_max"]["exact"], "refined": g["fisher_grid_max_refined"]["exact"],
                          "union_max": g["union_grid_max_p_le_p0"]["exact"]}
    return out


def exact_sha256(res: dict) -> str:
    return hashlib.sha256(json.dumps(exact_figures(res), sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def record_problems(res: dict) -> list[str]:
    """The record's fields against the oracles of record and the reviewed figures: the inputs, literal; the power
    (m:190's figures; the reviewed displays); the launch rule and the rows (the reviewed ones; m:234-243 are checked in
    compute); every case's stop, units per launch, looks, bars (n_j, crit_j and the false pause, each also against
    valence_core.m.bars' own critical_k and seq_false_pause at the bar's p0 and alpha; the realised case's rounding),
    and guards (looks, crits, Fisher cells, the three figures at .20, the pausing union; the projection's grid and
    maxima); the joint; the hours; the fixed texts; the exact values' digest; the display rule."""
    out = []
    try:
        if (res.get("schema"), res.get("unit"), res.get("path")) != (SCHEMA, "Q-F3", "uncached"):
            out.append("schema / unit / path")
        inp = res["inputs"]
        want_inp = {"k": 29, "n_q": 40, "r": "29/40",
                    "per_template_beside": {"A1": "3/4", "A1s": "4/8", "A2": "4/4", "A2s": "4/8", "A3": "6/8",
                                            "A3s": "8/8"},
                    "floors": {"A1": 80, "A1s": 32, "A2": 144, "A2s": 56, "A3": 144, "A3s": 56},
                    "balance_units": {"A1": 32, "A1s": 32, "A2": 16, "A2s": 16, "A3": 16, "A3s": 16}, "look_every": 40,
                    "bars": {"round_degeneracy": {"name": "round_degeneracy@campaign-Q-F3", "p0": "1/20",
                                                  "alpha": "1/20", "domain": "sham", "domain_arms": ["A1s", "A2s", "A3s"],
                                                  "unit": "rounds", "per_session": 10, "binding": True},
                             "reasoning_line_defect": {"name": "reasoning_line_defect@campaign-Q-F3", "p0": "1/10",
                                                       "alpha": "1/20", "domain": "sham",
                                                       "domain_arms": ["A1s", "A2s", "A3s"], "unit": "lines",
                                                       "per_session": 6, "binding": True},
                             "own_pair_lexical": {"name": "own_pair_lexical@campaign-Q-F3", "p0": "1/50",
                                                  "alpha": "1/20", "domain": "lexical_sham",
                                                  "domain_arms": ["A2s", "A3s"], "unit": "rounds", "per_session": 10,
                                                  "binding": True}},
                    "guard": {"abs_p0": "1/5", "alpha": "1/20", "unit": "sessions launched",
                              "pausing_halves": ["abs", "fisher"], "pairs": [["A1", "A1s"], ["A2", "A2s"], ["A3", "A3s"]]},
                    "realised_at_G-F3": {"sham_sessions": 24, "task_rounds": [189, 240], "reasoning_lines": [98, 144]}}
        out += [f"inputs.{k_}" for k_ in sorted(set(want_inp) | set(inp)) if inp.get(k_) != want_inp.get(k_)]
        pw = res["power"]
        for a in CONTRAST:
            pa = pw["arms"][a]
            alpha, P = POWER_SPEC[a]
            if (pa["display"], pa["exact4"]) != REVIEWED_POWER[a] or pa["display"] != "0" + POWER_ORACLE[a] or \
                    (pa["n"], pa["mS"], pa["split"], pa["alpha"], pa["P"], pa["gated"]) != \
                    (FLOOR[a], FLOOR[keys.sham_of(a)], [FLOOR[a] // 2, FLOOR[a] - FLOOR[a] // 2], M.fs(alpha),
                     M.fs(P), a in ("A1", "A2")):
                out.append(f"power.{a}")
            if pa["gated"] and Fraction(pa["exact"]) < Fraction(17, 20):
                out.append(f"power.{a}: below its floor, recorded as met")
        bs = pw["beside_A1_cached_96_32"]
        if ((bs["display"], bs["exact4"]) != REVIEWED_POWER["A1_cached_96_32"] or bs["display"] != "0.916"
                or (bs["n"], bs["mS"], bs["used"]) != (96, 32, False)):
            out.append("power.beside_A1_cached_96_32")
        if (pw["power_floor"], pw["n_raised"], pw["basis"]) != ("17/20", False, POWER_BASIS):
            out.append("power: floor / n_raised / basis")
        la = res["launch"]
        rule = {a: (la["rule"][a]["floor"], la["rule"][a]["ceil_1.15_floor"], la["rule"][a]["N90"], la["rule"][a]["L"])
                for a in ARMS}
        if rule != REVIEWED_RULE or la["L"] != {a: REVIEWED_RULE[a][3] for a in ARMS} or \
                (la["total"], la["looks"], la["k_with_this_row"]) != (832, 21, [28, 29]):
            out.append("launch: the rule, L, total, looks or the same row")
        rows = {int(k_): tuple(v_[x] for x in ARMS + ("total", "looks")) for k_, v_ in la["rows_by_k"].items()}
        if rows != REVIEWED_ROWS:
            out.append("launch.rows_by_k: not the reviewed rows")
        if sorted(res["cases"]) != sorted(CASE_ORDER):
            return out + [f"cases {sorted(res['cases'])}"]
        for name in CASE_ORDER:
            cs, want = res["cases"][name], REVIEWED_CASES[name]
            if tuple(cs["stop"][a] for a in ARMS) != want["stop"] or sorted(cs["stop"]) != sorted(ARMS):
                out.append(f"{name}: stop")
            per = {"rounds": "63/8", "lines": "49/12"} if name == "sham_realised" else {"rounds": "10", "lines": "6"}
            rnd = "half up, per cumulative count" if name == "sham_realised" else "none"
            if (cs["per_sham_launch"], cs["rounding"]) != (per, rnd):
                out.append(f"{name}: units per sham launch or rounding")
            lks = [(lk["launches"],) + tuple(lk[a] for a in ARMS) for lk in cs["looks"]]
            if lks != [tuple(x) for x in want["looks"]] or cs["n_looks"] != len(cs["looks"]) or \
                    [lk["look"] for lk in cs["looks"]] != list(range(1, len(cs["looks"]) + 1)) or \
                    [bool(lk.get("end")) for lk in cs["looks"]] != [False] * (len(cs["looks"]) - 1) + [True]:
                out.append(f"{name}: looks")
            for cls in BAR_CLASSES:
                bf = cs["bars"][cls]
                n_w, c_w, fp_w = want["bars"][cls]
                if (bf["n_j"], bf["crit_j"], bf["false_pause"]["display"]) != (n_w, c_w, fp_w):
                    out.append(f"{name}.{cls}: not the reviewed figures")
                p0, al = BAR_ROWS[cls][1], BAR_ROWS[cls][2]
                if bf["crit_j"] != [bars.critical_k(n, p0, al) for n in bf["n_j"]] or \
                        Fraction(bf["false_pause"]["exact"]) != bars.seq_false_pause(bf["n_j"], p0, al):
                    out.append(f"{name}.{cls}: not valence_core.m.bars' at p0 {M.fs(p0)}, alpha {M.fs(al)}")
                dom = DOMAIN_ARMS[BAR_ROWS[cls][3]]
                rate = Fraction(per[UNIT_OF[cls]])
                exact = [Fraction(sum(lk[a] for a in dom)) * rate for lk in cs["looks"]]
                if name == "sham_realised":
                    if bf.get("n_j_exact") != [M.fs(x) for x in exact] or bf["n_j"] != [half_up(x) for x in exact]:
                        out.append(f"{name}.{cls}: the rounding of the realised units")
                elif "n_j_exact" in bf or bf["n_j"] != [int(x) for x in exact]:
                    out.append(f"{name}.{cls}: n_j is not the domain's launches x the units per launch")
            if name == "sham_realised":
                if "guards" in cs or "guard_unit" in cs:
                    out.append(f"{name}: a guard figure where the rounds-and-lines-only case has none")
                continue
            for c in CONTRAST:
                g = cs["guards"][c]
                n1n2, crits, cells, figs = want["guards"][c]
                at = g["at_common_rate_p0"]
                if (g["looks_n1_n2"], g["abs_crit_j"], g["fisher_cells_j"], at["p"],
                        (at["abs"]["display"], at["fisher"]["display"], at["union"]["display"])) != \
                        (n1n2, crits, cells, "1/5", figs):
                    out.append(f"{name}.guard {c}: not the reviewed figures")
                if g["looks_n1_n2"] != [[lk[c], lk[keys.sham_of(c)]] for lk in cs["looks"]]:
                    out.append(f"{name}.guard {c}: its looks are not the pair's launches")
                if g["guard_figure"] != {"pausing_halves": ["abs", "fisher"], "figure": "union",
                                         "at_common_rate_p0": at["union"]}:
                    out.append(f"{name}.guard {c}: the pausing figure is not the union (m:316)")
                if ("fisher_grid" in g) != (name == "projection"):
                    out.append(f"{name}.guard {c}: the grid belongs to the projection only")
                if name == "projection":
                    grid, gmax, ref, umax = REVIEWED_GRID[c]
                    if ",".join(x["fisher"]["display"] for x in g["fisher_grid"]) != grid or \
                            [x["p"] for x in g["fisher_grid"]] != [M.fs(Fraction(j, 100)) for j in range(1, 100)]:
                        out.append(f"projection.guard {c}: the grid")
                    if ((g["fisher_grid_max"]["display"], g["fisher_grid_max"]["p"]),
                            (g["fisher_grid_max_refined"]["display"], g["fisher_grid_max_refined"]["p"],
                             g["fisher_grid_max_refined"]["rates"]),
                            (g["union_grid_max_p_le_p0"]["display"], g["union_grid_max_p_le_p0"]["p"])) != \
                            (gmax, ref, umax):
                        out.append(f"projection.guard {c}: the grid's maxima")
                    at20 = [x for x in g["fisher_grid"] if x["p"] == "1/5"]
                    if not at20 or at20[0]["fisher"] != at["fisher"]:
                        out.append(f"projection.guard {c}: the Fisher half at .20 is not its grid entry at 1/5")
            gu, surv = cs["guard_unit"], Fraction(1)
            for c in CONTRAST:
                surv *= 1 - Fraction(cs["guards"][c]["at_common_rate_p0"]["union"]["exact"])
            if (gu["rule"], gu["pairs"], gu["figure_per_pair"], Fraction(gu["exact"]), gu["display"]) != \
                    (GUARD_UNIT_RULE, [list(p) for p in PAIRS], "union", 1 - surv, REVIEWED_GUARD_UNIT[name]):
                out.append(f"{name}: the unit's guard figure")
        jj, pc = res["joint"], res["cases"]["projection"]
        if (jj["figure"], jj["guards_beside_figure"], jj["not_computed"]) != \
                ("each bar's own (projection case)", "union", JOINT_SENTENCE) or \
                jj["figures"] != {cls: pc["bars"][cls]["false_pause"] for cls in BAR_CLASSES} or \
                jj["guards_beside"] != {c: pc["guards"][c]["at_common_rate_p0"]["union"] for c in CONTRAST} or \
                jj["guard_unit_beside"] != pc["guard_unit"]:
            out.append("joint")
        hb = res["hours"]
        if (hb["basis_line"], hb["basis_s_per_session"], hb["launches"], hb["m238_column"]) != \
                ("m:230", ["3208/5", "3568/5"], 832, "148–165") or \
                (hb["hours"][0]["display"], hb["hours"][1]["display"], hb["hours"][0]["whole"],
                 hb["hours"][1]["whole"]) != REVIEWED_HOURS or \
                f"{hb['hours'][0]['whole']}–{hb['hours'][1]['whole']}" != hb["m238_column"]:
            out.append("hours")
        if res["beside_A5"] != {"raw": SEAT_RAW, "commit": SEAT_COMMIT, "sha256": SEAT_SHA256, "section": "§A.5",
                                "launches": 832, "rows": list(A5_ROWS)}:
            out.append("beside_A5")
        if (res["cap"], res["not_figured"], res["readings"]) != (CAP, NOT_FIGURED, READINGS):
            out.append("cap / not_figured / readings")
        if exact_sha256(res) != REVIEWED_EXACT_SHA256:
            out.append("the exact values are not the independent recomputation's (their sha256)")
    except (KeyError, TypeError, IndexError, ValueError, AttributeError) as e:
        out.append(f"the record's shape: {type(e).__name__}: {e}")
    return out + display_problems(res)


def evaluate_problems(res: dict) -> list[str]:
    """crit_j at every look of every case against the mf3 bar's own evaluate(): its crit, firing at crit and silent at
    crit - 1, each at the look's index ("end" at the last)."""
    out = []
    for name in CASE_ORDER:
        for cls in BAR_CLASSES:
            b = bar_of(cls)
            bf = res["cases"][name]["bars"][cls]
            nl = len(bf["n_j"])
            for j, (n, c) in enumerate(zip(bf["n_j"], bf["crit_j"]), 1):
                look = "end" if j == nl else j
                if b.evaluate(0, n, look=look).crit != c:
                    out.append(f"{name}.{cls} look {j}: crit {c}, the bar's {b.evaluate(0, n, look=look).crit}")
                elif c is not None and (not b.evaluate(c, n, look=look).fired
                                        or (c > 0 and b.evaluate(c - 1, n, look=look).fired)):
                    out.append(f"{name}.{cls} look {j}: the bar does not fire at {c} and stay silent at {c - 1}")
    return out


def region_problems_f3(n1: int, n2: int) -> list[str]:
    """m_gpwr.guard_regions at one look against mf3's guard bars' own evaluate(): every (a, c) cell of the Fisher set
    and the absolute half's critical count."""
    reg = M.guard_regions([(n1, n2)])[0]
    f, a = bar_of("exclusion_guard_fisher"), bar_of("exclusion_guard_abs")
    out = [f"fisher cell {(x, y)} at {(n1, n2)}" for x in range(n1 + 1) for y in range(n2 + 1)
           if ((x, y) in reg["fisher"]) != f.evaluate(x, n1, sham_k=y, sham_n=n2).exceeds]
    if reg["abs_crit"] != a.evaluate(0, n1).crit:
        out.append(f"abs crit {reg['abs_crit']} vs the bar's {a.evaluate(0, n1).crit} at n1 = {n1}")
    return out


def lock_texts(commit: str) -> dict:
    """Every LOCK*.md at the repository's root in commit's tree, by its text."""
    names = [p for p in _git_text("ls-tree", "--name-only", commit).splitlines()
             if p.startswith("LOCK") and p.endswith(".md")]
    return {n: _commit_blob(commit, n)[1].decode("utf-8") for n in sorted(names)}


def lock_scan(commit: str) -> tuple[dict, list[str]]:
    """lock_texts at commit, and the scan's completeness (the review's MINOR-1): the names it read equal the root's
    LOCK*.md listed apart, and the root still carries every lock known when this program was built."""
    texts = lock_texts(commit)
    root = _git_bytes("ls-tree", "-z", "--name-only", commit).split(b"\0")
    names = sorted(n for n in (x.decode("utf-8") for x in root if x) if fnmatch.fnmatchcase(n, "LOCK*.md"))
    probs = [] if sorted(texts) == names else [f"the lock scan read {sorted(texts)}; the root lists {names}"]
    missing = sorted(set(KNOWN_LOCKS) - set(names))
    if missing:
        probs.append(f"the root lacks locks known when this program was built: {missing}")
    return texts, probs


def lock_problems(texts: dict, rels, in_force_only: bool) -> list[str]:
    """The locks that name any of rels. in_force_only: the locks in force at G-PWR's step, so a LOCK-m-F3.md at v1.0
    or later (which follows G-PWR, m:298, and names its program and record by design) is not counted."""
    out = []
    for name, text in texts.items():
        if in_force_only and name == LOCK_F3 and text.startswith(LOCK_F3_V1_HEAD):
            continue
        out += [f"{name} names {rel}" for rel in rels if rel and rel in text]
    return out


# --- the report ----------------------------------------------------------------------------------------------------
def _row_groups(rows: dict) -> list[tuple[str, tuple]]:
    """The rows by k, descending, with equal rows merged as m:234-241 merges them ("40-35")."""
    out, ks = [], sorted((int(k) for k in rows), reverse=True)
    for k in ks:
        t = tuple(rows[str(k)][x] for x in ARMS + ("total", "looks"))
        if out and out[-1][2] == t:
            out[-1][1] = k
        else:
            out.append([k, k, t])
    return [((f"{hi}-{lo}" if hi != lo else str(hi)), t) for hi, lo, t in out]


def reference_report(res: dict) -> list[str]:
    """The report's lines, rendered from the record: report() prints exactly these."""
    inp, pw, la = res["inputs"], res["power"], res["launch"]
    L_ = [f"G-PWR {res['unit']} ({res['path']}): PROPOSAL-m v1.11 m:285 on k = {inp['k']} of {inp['n_q']}, r = "
          f"{inp['r']} (" + ", ".join(f"{a} {inp['per_template_beside'][a]}" for a in ARMS)
          + " beside); model-free and exact"]
    for a in CONTRAST:
        p = pw["arms"][a]
        tail = "floor .85: met" if p["gated"] else "no floor (the screen): reported"
        L_.append(f"POWER {a} at the planned floors ({p['n']}, {p['mS']}), split {p['split']}, alpha {p['alpha']}, P "
                  f"{p['P']}: {p['display']} ({p['exact4']}); {tail}")
    b = pw["beside_A1_cached_96_32"]
    L_.append(f"POWER beside: A1 at F-5's {b['n']}/{b['mS']} (m:184's cached floor): {b['display']} ({b['exact4']}); "
              f"not used (READINGS)")
    L_.append("NO N RAISED: m:190's raise is not triggered")
    for a in ARMS:
        r_ = la["rule"][a]
        L_.append(f"LAUNCH {a}: floor {r_['floor']}, ceil(1.15 floor) {r_['ceil_1.15_floor']}, N90 {r_['N90']}, unit "
                  f"{inp['balance_units'][a]} -> L {r_['L']}")
    L_.append(f"TOTAL {la['total']}; LOOKS {la['looks']}; the same row at k = {la['k_with_this_row']}")
    L_.append("ROWS by k (m:192; checked against m:234-243 and m:330): A1/A1s/A2/A2s/A3/A3s, total, looks")
    L_ += [f"  k {lab}: {'/'.join(str(x) for x in t[:6])}, {t[6]}, {t[7]}" for lab, t in _row_groups(la["rows_by_k"])]
    for name in CASE_ORDER:
        cs = res["cases"][name]
        rnd = "" if cs["rounding"] == "none" else f" ({cs['rounding']})"
        L_ += ["", f"CASE {name}: stop {cs['stop']}, per sham launch {cs['per_sham_launch']['rounds']} rounds and "
                   f"{cs['per_sham_launch']['lines']} lines{rnd}, {cs['n_looks']} looks"]
        L_ += [f"  look {lk['look']}: launches {lk['launches']} (" + ", ".join(f"{a} {lk[a]}" for a in ARMS) + ")"
               + (" end" if lk.get("end") else "") for lk in cs["looks"]]
        for cls in BAR_CLASSES:
            bf = cs["bars"][cls]
            L_.append(f"  {cls}: n_j {bf['n_j']} crit_j {bf['crit_j']} false pause {bf['false_pause']['display']}")
        for c, s in PAIRS:
            if "guards" not in cs:
                break
            g = cs["guards"][c]
            at, gf = g["at_common_rate_p0"], g["guard_figure"]
            L_.append(f"  guard {c}/{s}: (n1, n2)_j {g['looks_n1_n2']} abs crit_j {g['abs_crit_j']} Fisher cells_j "
                      f"{g['fisher_cells_j']}")
            L_.append(f"  guard {c}/{s} at the common rate {at['p']}: abs {at['abs']['display']}, Fisher "
                      f"{at['fisher']['display']}, union {at['union']['display']}; pausing on Qwen: {gf['figure']} "
                      f"{gf['at_common_rate_p0']['display']}")
            if "fisher_grid" in g:
                L_.append(f"  guard {c}/{s}, Fisher half on the grid: "
                          + ", ".join(f"{x['p']}:{x['fisher']['display']}" for x in g["fisher_grid"]))
                L_.append(f"  guard {c}/{s}, Fisher grid max {g['fisher_grid_max']['display']} at p "
                          f"{g['fisher_grid_max']['p']}; refined {g['fisher_grid_max_refined']['display']} at p "
                          f"{g['fisher_grid_max_refined']['p']} (rates {g['fisher_grid_max_refined']['rates']})")
                L_.append(f"  guard {c}/{s}, union grid max over p <= 1/5: {g['union_grid_max_p_le_p0']['display']} "
                          f"at p {g['union_grid_max_p_le_p0']['p']}")
        if "guard_unit" in cs:
            L_.append(f"  guard, the unit's figure (some pair pauses at the common rate 1/5; the pairs share no "
                      f"session): {cs['guard_unit']['display']}")
    jj = res["joint"]
    L_ += ["", "JOINT: " + jj["figure"] + ": " + ", ".join(f"{cls} {jj['figures'][cls]['display']}" for cls in
                                                           BAR_CLASSES)
           + f"; the guards' beside ({jj['guards_beside_figure']} at .20): "
           + ", ".join(f"{c} {jj['guards_beside'][c]['display']}" for c in CONTRAST)
           + f"; the unit's guard figure {jj['guard_unit_beside']['display']}",
           f"  {jj['not_computed']}"]
    hb = res["hours"]
    lo, hi = (M.dec(Fraction(x), 1) for x in hb["basis_s_per_session"])
    L_.append(f"HOURS at m:230's basis (READINGS): {hb['launches']} launches x {lo}-{hi} s per session = "
              f"{hb['hours'][0]['display']}-{hb['hours'][1]['display']} h ({hb['hours'][0]['whole']}-"
              f"{hb['hours'][1]['whole']} h; m:238's column {hb['m238_column']} h)")
    bz = res["beside_A5"]
    L_.append(f"BESIDE, by citation, verbatim: the seat's answers of 2026-11-14, {bz['section']}, its table on "
              f"{bz['launches']} launches ({bz['raw']} at {bz['commit']}, sha256 {bz['sha256']}):")
    L_ += [f"  {row}" for row in bz["rows"]]
    L_.append(f"CAP: {res['cap']}")
    L_.append("NOT FIGURED: " + "; ".join(f"{k_}: {v_}" for k_, v_ in res["not_figured"].items()))
    L_.append("READINGS:")
    L_ += [f"  - {x}" for x in res["readings"]]
    return L_


def report(res: dict) -> None:
    for line in reference_report(res):
        print(line)


def _rebuilt_lines(res: dict) -> list[str]:
    """The report rebuilt from the record, written apart from reference_report: a second rendering, so a defect in
    one does not pass through the other (m_gpwr's line_problems' purpose, over every line)."""
    arms = ["A1", "A1s", "A2", "A2s", "A3", "A3s"]
    i, pw, la = res["inputs"], res["power"], res["launch"]
    out = ["G-PWR %s (%s): PROPOSAL-m v1.11 m:285 on k = %s of %s, r = %s (%s beside); model-free and exact"
           % (res["unit"], res["path"], i["k"], i["n_q"], i["r"],
              ", ".join("%s %s" % (a, i["per_template_beside"][a]) for a in arms))]
    for a in ("A1", "A2", "A3"):
        p = pw["arms"][a]
        out.append("POWER %s at the planned floors (%s, %s), split %s, alpha %s, P %s: %s (%s); %s"
                   % (a, p["n"], p["mS"], p["split"], p["alpha"], p["P"], p["display"], p["exact4"],
                      "floor .85: met" if p["gated"] else "no floor (the screen): reported"))
    bb = pw["beside_A1_cached_96_32"]
    out.append("POWER beside: A1 at F-5's %s/%s (m:184's cached floor): %s (%s); not used (READINGS)"
               % (bb["n"], bb["mS"], bb["display"], bb["exact4"]))
    out.append("NO N RAISED: m:190's raise is not triggered")
    for a in arms:
        r = la["rule"][a]
        out.append("LAUNCH %s: floor %s, ceil(1.15 floor) %s, N90 %s, unit %s -> L %s"
                   % (a, r["floor"], r["ceil_1.15_floor"], r["N90"], i["balance_units"][a], r["L"]))
    out.append("TOTAL %s; LOOKS %s; the same row at k = %s" % (la["total"], la["looks"], la["k_with_this_row"]))
    out.append("ROWS by k (m:192; checked against m:234-243 and m:330): A1/A1s/A2/A2s/A3/A3s, total, looks")
    k = N_Q
    while k >= 1:
        row = la["rows_by_k"][str(k)]
        lo = k
        while lo > 1 and all(la["rows_by_k"][str(lo - 1)][x] == row[x] for x in arms + ["total", "looks"]):
            lo -= 1
        out.append("  k %s: %s, %s, %s" % (str(k) if lo == k else "%d-%d" % (k, lo),
                                            "/".join(str(row[a]) for a in arms), row["total"], row["looks"]))
        k = lo - 1
    for c in ("projection", "sham_at_floor_r", "sham_at_floor_min", "sham_realised"):
        cs = res["cases"][c]
        out.append("")
        out.append("CASE %s: stop %s, per sham launch %s rounds and %s lines%s, %s looks"
                   % (c, cs["stop"], cs["per_sham_launch"]["rounds"], cs["per_sham_launch"]["lines"],
                      "" if cs["rounding"] == "none" else " (%s)" % cs["rounding"], cs["n_looks"]))
        for lk in cs["looks"]:
            out.append("  look %s: launches %s (%s)%s" % (lk["look"], lk["launches"],
                                                          ", ".join("%s %s" % (a, lk[a]) for a in arms),
                                                          " end" if lk.get("end") else ""))
        for b in ("round_degeneracy", "reasoning_line_defect", "own_pair_lexical"):
            bf = cs["bars"][b]
            out.append("  %s: n_j %s crit_j %s false pause %s" % (b, bf["n_j"], bf["crit_j"],
                                                                 bf["false_pause"]["display"]))
        if "guards" in cs:
            for ca, sa in (("A1", "A1s"), ("A2", "A2s"), ("A3", "A3s")):
                g = cs["guards"][ca]
                at = g["at_common_rate_p0"]
                out.append("  guard %s/%s: (n1, n2)_j %s abs crit_j %s Fisher cells_j %s"
                           % (ca, sa, g["looks_n1_n2"], g["abs_crit_j"], g["fisher_cells_j"]))
                out.append("  guard %s/%s at the common rate %s: abs %s, Fisher %s, union %s; pausing on Qwen: %s %s"
                           % (ca, sa, at["p"], at["abs"]["display"], at["fisher"]["display"], at["union"]["display"],
                              g["guard_figure"]["figure"], g["guard_figure"]["at_common_rate_p0"]["display"]))
                if "fisher_grid" in g:
                    out.append("  guard %s/%s, Fisher half on the grid: %s"
                               % (ca, sa, ", ".join("%s:%s" % (x["p"], x["fisher"]["display"])
                                                    for x in g["fisher_grid"])))
                    mx, rf, un = g["fisher_grid_max"], g["fisher_grid_max_refined"], g["union_grid_max_p_le_p0"]
                    out.append("  guard %s/%s, Fisher grid max %s at p %s; refined %s at p %s (rates %s)"
                               % (ca, sa, mx["display"], mx["p"], rf["display"], rf["p"], rf["rates"]))
                    out.append("  guard %s/%s, union grid max over p <= 1/5: %s at p %s"
                               % (ca, sa, un["display"], un["p"]))
            out.append("  guard, the unit's figure (some pair pauses at the common rate 1/5; the pairs share no "
                       "session): %s" % cs["guard_unit"]["display"])
    j = res["joint"]
    out.append("")
    out.append("JOINT: %s: %s; the guards' beside (%s at .20): %s; the unit's guard figure %s"
               % (j["figure"], ", ".join("%s %s" % (b, j["figures"][b]["display"])
                                         for b in ("round_degeneracy", "reasoning_line_defect", "own_pair_lexical")),
                  j["guards_beside_figure"], ", ".join("%s %s" % (ca, j["guards_beside"][ca]["display"])
                                                       for ca in ("A1", "A2", "A3")),
                  j["guard_unit_beside"]["display"]))
    out.append("  %s" % j["not_computed"])
    h = res["hours"]
    tenths = [Fraction(x) * 10 for x in h["basis_s_per_session"]]
    basis = ["%d.%d" % divmod(t.numerator, 10) if t.denominator == 1 else "?" for t in tenths]
    out.append("HOURS at m:230's basis (READINGS): %s launches x %s-%s s per session = %s-%s h (%s-%s h; m:238's "
               "column %s h)" % (h["launches"], basis[0], basis[1], h["hours"][0]["display"], h["hours"][1]["display"],
                                 h["hours"][0]["whole"], h["hours"][1]["whole"], h["m238_column"]))
    z = res["beside_A5"]
    out.append("BESIDE, by citation, verbatim: the seat's answers of 2026-11-14, %s, its table on %s launches (%s at %s, "
               "sha256 %s):" % (z["section"], z["launches"], z["raw"], z["commit"], z["sha256"]))
    out += ["  %s" % row for row in z["rows"]]
    out.append("CAP: %s" % res["cap"])
    out.append("NOT FIGURED: " + "; ".join("%s: %s" % kv for kv in res["not_figured"].items()))
    out.append("READINGS:")
    out += ["  - %s" % x for x in res["readings"]]
    return out


def line_problems_f3(res: dict, so: str) -> list[str]:
    """The stdout against the second rendering, line by line, and its line count."""
    want, got = _rebuilt_lines(res), so.splitlines()
    out = [f"line {i + 1}: {g!r} for {w!r}" for i, (w, g) in enumerate(zip(want, got)) if w != g]
    if len(want) != len(got):
        out.append(f"{len(got)} lines for {len(want)}")
    return out


# --- self-test -----------------------------------------------------------------------------------------------------
_F3_CHILD_BOOT = """\
import hashlib, os, subprocess, sys, types
repo, commit = sys.argv[1], sys.argv[2]
env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
g = ["git", "--no-replace-objects", "-C", repo]
oid = subprocess.run(g + ["rev-parse", "--verify", commit + ":scripts/mf3_gpwr.py"], env=env, capture_output=True,
                     text=True, check=True).stdout.strip()
src = subprocess.run(g + ["cat-file", "blob", oid], env=env, capture_output=True, check=True).stdout
if hashlib.new("sha1" if len(oid) == 40 else "sha256", b"blob %d\\0" % len(src) + src).hexdigest() != oid:
    raise SystemExit("REFUSED: the self-test's script does not hash to its blob")
path = os.path.join(repo, "scripts", "mf3_gpwr.py")
mod = types.ModuleType("__main__")
mod.__file__, mod._F3GPWR_COMMIT = path, commit
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


def _qf0_composition(m) -> tuple[bool, list]:
    """Q-F0's figures unchanged, and this program's composition at Q-F0's inputs: m_gpwr.compute in this process (with
    mf3's modules loaded) meets m_gpwr's own inputs, display and fixed checks -- its pins of the reviewed Q-F0 run's
    figures, by sha256 -- and, case by case, project_arms over (A0, A0s) under m's schedule.interleave, bar_figure at
    Q-F0's round_degeneracy row and guard_for_pair reproduce m_gpwr's looks, round_degeneracy and guard blocks."""
    res0 = json.loads(resume.json_text(M.compute(m), indent=1))
    probs = [f"m_gpwr's own check: {x}" for x in M.inputs_problems(res0) + M.display_problems(res0)
             + M.fixed_problems(res0)]
    d0, f0, a0 = M._bar(M.DEGEN_BAR), M._bar(M.FISHER_BAR), M._bar(M.ABS_BAR)
    halves0 = tuple(h for h, b in (("abs", a0), ("fisher", f0)) if b.binding)
    for name, cs in res0["cases"].items():
        lks = project_arms(cs["stop"], M.ARMS, m_schedule.interleave)
        if lks != cs["looks"] or lks != M.project(cs["stop"]):
            probs.append(f"{name}: project_arms' looks are not m_gpwr's")
        if bar_figure(cs["round_degeneracy"]["n_j"], d0) != cs["round_degeneracy"]:
            probs.append(f"{name}: bar_figure is not m_gpwr.degeneracy")
        if "guard" in cs:
            g = guard_for_pair(lks, "A0", "A0s", name == "projection", halves0)
            if g.pop("guard_figure")["figure"] != "union" or g != cs["guard"]:
                probs.append(f"{name}: guard_for_pair is not m_gpwr's guard block")
    checked = sorted(res0["cases"]) == ["projection", "sham_at_floor_min", "sham_at_floor_r", "sham_realised_rounds"]
    return (not probs and checked), probs


def _bar_probe() -> tuple[bool, list]:
    """bar_problems_f3 against stand-in bars (plain records of the compared fields), each with one field perturbed,
    and with a row missing."""
    real = f3_bars()
    bad = []
    for cls in BAR_ROWS:
        name = bar_name(cls)
        for fld in ("kind", "p0q", "alphaq", "domain", "binding"):
            if cls == "exclusion_guard_fisher" and fld == "p0q":
                continue                       # the Fisher half carries no p0 (bars: guard_fisher)
            orig = real[name]
            base = {k_: getattr(orig, k_) for k_ in ("kind", "p0q", "alphaq", "domain", "binding")}
            val = {"kind": "hair_trigger", "p0q": Fraction(1, 3), "alphaq": Fraction(1, 3), "domain": "every",
                   "binding": not orig.binding}[fld]
            pert = dict(real, **{name: SimpleNamespace(**dict(base, **{fld: val}))})
            if not any(pr.startswith(name + ":") for pr in bar_problems_f3(pert)):
                bad.append((cls, fld))
        if bar_problems_f3({k_: v_ for k_, v_ in real.items() if k_ != name}) == []:
            bad.append((cls, "a missing row"))
    return not bad, bad


def _stop_message(f) -> str:
    try:
        f()
    except SystemExit as e:
        return str(e)
    return ""


def _run_check_f3(fn) -> tuple[bool, str]:
    """m_gpwr._run_check's verdict, a STOP (SystemExit) included: a check that raises or stops is a FAIL, and the rest
    still run."""
    try:
        r = fn()
        ok, detail = r if isinstance(r, tuple) else (r, "")
    except (Exception, SystemExit) as e:  # noqa: BLE001
        ok, detail = False, f"raised {type(e).__name__}: {e}"
    return bool(ok), detail


def _with(name: str, value, fn):
    """fn() with this module's global `name` set to value, restored after (the self-test's probes only)."""
    g = globals()
    keep = g[name]
    g[name] = value
    try:
        return fn()
    finally:
        g[name] = keep


def _stop_probe(m) -> tuple[bool, list]:
    """compute()'s STOP branches, each provoked by one stand-in of this module's own names, must stop the run with a
    message beginning 'STOP' (the rows' memo, filled by the record's run, keeps the rows-oracle probe cheap)."""
    missed = []
    rows29 = {**TABLE_ROWS, range(28, 30): (128, 64, 208, 96, 832, 21, "148–165")}
    for label, name, val, want in (
            ("the bars", "bar_problems_f3", lambda by_name=None: ["stand-in"], "STOP: this program's constants"),
            ("k = 0", "K", 0, "STOP: k = 0"),
            ("the launch cross-check", "_N90_EXACT", lambda *a, **kw: 0, "STOP: the launch rule disagrees"),
            ("a launch row other than m:238's", "TABLE_ROWS", rows29, "STOP: the launch row at k = 29"),
            ("non-integer units", "PER_SESSION", {"rounds": 10, "lines": Fraction(19, 3)}, "STOP: non-integer lines"),
            ("the look count", "looks_for", lambda total: 99, "STOP: the projection's looks"),
            ("the realised case's denominators", "REALISED", {"rounds": (189, 241), "lines": (98, 144)},
             "STOP: G-F3's planned units"),
            ("the rows' oracles", "TABLE_AFTER", {**TABLE_AFTER, 23: 993}, "STOP: the rows by k differ"),
            ("the citation's total", "A5_TOTAL", 864, "STOP: the total 832")):
        msg = _with(name, val, lambda: _stop_message(lambda: compute(m)))
        if not msg.startswith(want):
            missed.append((label, msg[:120]))
    return not missed, missed


class _PowerStandIn:
    """The analyzer with one arm's planned power replaced (the self-test's power probes only)."""

    def __init__(self, real, arm: str, value: Fraction):
        self.real, self.arm, self.value = real, arm, value

    def f3_power_block(self, arm, n0, n1, mS, path):
        pb = json.loads(json.dumps(self.real.f3_power_block(arm, n0, n1, mS, path)))
        if arm == self.arm and path == PATH:
            for part in ("of_record", "planned"):
                pb[part]["exact"] = M.fs(self.value)
                pb[part]["display"] = M.dec(self.value, 3)
        return pb


def _realised_rule() -> tuple[bool, list]:
    """The realised case's rule on literals: 63/8 and 49/12 per sham launch; half up on a tie (157.5 -> 158), down below
    a half (81 2/3 -> 82 is up: 2/3 > 1/2; 102 3/8 -> 102 down); non-decreasing over the projection's looks."""
    bad = []
    if {u: Fraction(*REALISED[u]) * PER_SESSION[u] for u in ("rounds", "lines")} != {"rounds": Fraction(63, 8),
                                                                                       "lines": Fraction(49, 12)}:
        bad.append("rates")
    if [half_up(Fraction(315, 2)), half_up(Fraction(245, 3)), half_up(Fraction(819, 8)), half_up(Fraction(1))] != \
            [158, 82, 102, 1]:
        bad.append("half up")
    looks = [dict(zip(("launches",) + ARMS, x)) for x in _PROJ_LOOKS]
    for cls, (ns, ex) in case_units(looks, {"rounds": Fraction(63, 8), "lines": Fraction(49, 12)}, True).items():
        if any(b < a for a, b in zip(ns, ns[1:])) or [half_up(Fraction(x)) for x in ex] != ns:
            bad.append(cls)
    return not bad, bad


def selftest(m) -> int:
    """Every check is guarded: an exception or a STOP is a FAIL, and the rest still run. The oracles: m_gpwr's own
    self-test at the load commit (the imported functions) and m_gpwr's pins of its reviewed Q-F0 run (the composition
    at Q-F0's inputs); the bars of record (bars.QF3_BARS, their evaluate()); m:184-192, m:230-243, m:297, m:316 and
    m:330, the seat's raw, the G-F3 entry, LOCK-m-F3 v0.2, F-5's and Q7's raws, bound by build_sources(); the reviewed
    figures (an independent recomputation of every printed figure on the standard library alone, and of the exact
    values by digest); mf3's schedule._n90_exact; the stdout against a second rendering of the record."""
    fails = []

    def chk(name, fn):
        ok, detail = _run_check_f3(fn)
        print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{str(detail)[:300]!r}]" if detail and not ok else ""))
        if not ok:
            fails.append(name)

    chk("m_gpwr is the load commit's blob, executed as the module m_gpwr with its commit pinned to the load commit",
        lambda: (M_BLOB == _git_text("rev-parse", f"{_LOAD_COMMIT}:{M_REL}").strip()
                 and M._LOAD_COMMIT == _LOAD_COMMIT and M.__name__ == "m_gpwr", (M_BLOB, M._LOAD_COMMIT)))
    chk("m_gpwr's own self-test passes at the load commit, in its own isolated process", _m_selftest)
    chk("Q-F0's figures unchanged (m_gpwr.compute here, mf3 loaded, meets m_gpwr's own pins of its reviewed run), and "
        "the composition at Q-F0's inputs reproduces m_gpwr's looks, round_degeneracy and guard blocks in every case",
        lambda: _qf0_composition(m))
    chk("this process executed valence_core (m and mf3) from the load commit's blobs only",
        lambda: (lambda ft: (not ft and "valence_core/mf3/schedule.py" in M._LOADED
                             and "valence_core/mf3/bars.py" in M._LOADED and "valence_core/m/bars.py" in M._LOADED,
                             ft))(M._from_tree()))
    chk("the bars of record: bar_problems_f3 is empty (mf3's campaign rows; m_gpwr's guard constants; 10 rounds and 6 "
        "lines per session; the domains' arms; m's arithmetic)",
        lambda: (lambda pr: (not pr, pr))(bar_problems_f3()))
    chk("bar_problems_f3 reports each compared field of each campaign row perturbed, and a missing row", _bar_probe)
    chk("the guard's pausing halves from the bars' binding flags: both on Qwen, so the union (m:316)",
        lambda: guard_halves() == ("abs", "fisher") and GUARD_FIGURE[guard_halves()] == "union"
        and guard_halves({**f3_bars(), bar_name("exclusion_guard_abs"): SimpleNamespace(
            binding=False)}) == ("fisher",))
    chk("the projection's form: mf3's interleave refuses anything but the six arms in table order; project_arms "
        "refuses a stop below 1, a bool or a missing arm; an end on a multiple of 40 adds no look and is flagged once",
        lambda: M._raises(lambda: project_arms({a: 1 for a in ARMS}, arms=("A1", "A2", "A1s", "A2s", "A3", "A3s")))
        and all(M._raises(lambda s=s: project_arms(s)) for s in (
            {**{a: 1 for a in ARMS}, "A2s": 0}, {**{a: 1 for a in ARMS}, "A1": True},
            {a: 1 for a in ARMS if a != "A3s"}))
        and [(lk["launches"], bool(lk.get("end"))) for lk in project_arms({a: 20 for a in ARMS})]
        == [(40, False), (80, False), (120, True)])
    chk("the realised case's rule: 63/8 rounds and 49/12 lines per sham launch; floor(x + 1/2) per cumulative count "
        "(157.5 -> 158, 81 2/3 -> 82, 102 3/8 -> 102); the counts non-decreasing", _realised_rule)
    chk("the launch rule at r = 29/40 (m:192): the reviewed (floor, ceil(1.15 floor), N90, L) per arm, each L equal to "
        "mf3's _n90_exact at its own balance unit",
        lambda: all((lambda lc: (lc["floor"], lc["ceil_1.15_floor"], lc["N90"], lc["L"]) == REVIEWED_RULE[a]
                     and lc["L"] == _N90_EXACT(FLOOR[a], K, N_Q, UNIT_SIZE[a]))(
            M.launch_count(FLOOR[a], Fraction(K, N_Q), UNIT_SIZE[a])) for a in ARMS))
    chk("power below .85 STOPs at A1 and at A2 (stand-in analyzers at .849); A3 below .85 does not STOP (the screen); "
        "exactly .85 does not STOP (m:190's floor is >= .85)",
        lambda: _stop_message(lambda: power_block_f3(_PowerStandIn(m, "A1", Fraction(849, 1000)))).startswith(
            "STOP: A1: power at the planned floors")
        and _stop_message(lambda: power_block_f3(_PowerStandIn(m, "A2", Fraction(849, 1000)))).startswith(
            "STOP: A2: power at the planned floors")
        and power_block_f3(_PowerStandIn(m, "A3", Fraction(1, 2)))["arms"]["A3"]["display"] == "0.500"
        and power_block_f3(_PowerStandIn(m, "A2", Fraction(17, 20)))["arms"]["A2"]["display"] == "0.850")
    chk("k = 0 STOPs (m:192); k outside [0, n_q], or not an int, is refused",
        lambda: _with("K", 0, lambda: _stop_message(lambda: compute(m))).startswith("STOP: k = 0")
        and all(_with("K", kk, lambda: M._raises(lambda: compute(m))) for kk in (41, -1, 29.0, True)))
    try:
        res = compute(m)
        text = resume.json_text(res, indent=1)
        back = json.loads(text)
        buf = io.StringIO()
        with redirect_stdout(buf):
            report(back)
        so = buf.getvalue()
    except BaseException as e:  # noqa: BLE001 -- includes compute()'s SystemExit STOPs
        res, back, so = None, None, f"{type(e).__name__}: {e}"
    chk("compute() completes and report() prints", lambda: (res is not None, so[:300]))
    if res is not None:
        def record_ok():
            pr = record_problems(back) + line_problems_f3(back, so)
            return (not pr and resume.json_text(back, indent=1) == text and so.splitlines() == reference_report(back),
                    pr[:5])
        chk("the record: the reviewed figures (every printed figure; the exact values by digest), the oracles, the "
            "fixed texts and the display rule; a JSON round trip; the stdout rebuilt line by line from the record",
            record_ok)
        chk("crit_j at every look of every case, for each bar, equals the mf3 bar's own evaluate(): its crit, firing "
            "at crit and silent at crit - 1",
            lambda: (lambda pr: (not pr, pr[:5]))(evaluate_problems(back)))

        def regions_ok():
            pts = sorted({tuple(x) for c in CONTRAST for x in back["cases"]["projection"]["guards"][c]["looks_n1_n2"]}
                         | {tuple(back["cases"][n]["guards"][c]["looks_n1_n2"][-1]) for n in CASE_ORDER[1:3]
                            for c in CONTRAST})
            pr = [x for n1, n2 in pts for x in region_problems_f3(n1, n2)]
            return not pr and len(pts) == 39, (len(pts), pr[:4])
        chk("the guard's regions at every distinct projection look of the three pairs, and at the floor cases' last "
            "looks, equal mf3's guard bars' evaluate(): each Fisher cell and the absolute half's critical count",
            regions_ok)
        chk("the regions check reports a dropped Fisher cell and an absolute crit moved by one (its probe)",
            lambda: _region_probe())

        def record_check_bites():
            bad = []
            for path, val in ((("launch", "total"), 864), (("launch", "L", "A2"), 208),
                              (("cases", "projection", "stop", "A3s"), 80),
                              (("cases", "sham_at_floor_r", "stop", "A1s"), 44),
                              (("cases", "projection", "bars", "own_pair_lexical", "crit_j", 0), 7),
                              (("cases", "projection", "bars", "reasoning_line_defect", "false_pause", "display"),
                               "0.1585"),
                              (("cases", "sham_realised", "bars", "round_degeneracy", "n_j", 0), 157),
                              (("cases", "sham_realised", "per_sham_launch", "rounds"), "8"),
                              (("cases", "projection", "guards", "A2", "guard_figure", "figure"), "fisher"),
                              (("cases", "projection", "guards", "A2", "guard_figure", "at_common_rate_p0"),
                               back["cases"]["projection"]["guards"]["A2"]["at_common_rate_p0"]["fisher"]),
                              (("cases", "projection", "guards", "A3", "fisher_grid_max", "p"), "13/25"),
                              (("cases", "sham_at_floor_min", "guards", "A1", "abs_crit_j", 0), 5),
                              (("joint", "guards_beside", "A1"),
                               back["cases"]["projection"]["guards"]["A1"]["at_common_rate_p0"]["abs"]),
                              (("power", "arms", "A3", "gated"), True), (("power", "arms", "A1", "exact4"), "0.8785"),
                              (("hours", "hours", 1, "whole"), "164"), (("inputs", "per_template_beside", "A3"), "3/4"),
                              (("inputs", "bars", "own_pair_lexical", "p0"), "1/20"), (("readings",), READINGS[:-1]),
                              (("beside_A5", "rows", 0), "| altered |"), (("cap",), "1,000 h"),
                              (("cases", "sham_realised", "bars", "round_degeneracy", "n_j_exact", 0), "157/1"),
                              (("cases", "projection", "guard_unit", "display"), "0.5391"),
                              (("cases", "sham_at_floor_min", "guard_unit", "exact"),
                               back["cases"]["sham_at_floor_min"]["guards"]["A1"]["at_common_rate_p0"]["union"]
                               ["exact"]),
                              (("joint", "guard_unit_beside"), back["cases"]["sham_at_floor_r"]["guard_unit"]),
                              (("cases", "sham_realised", "guard_unit"), back["cases"]["projection"]["guard_unit"])):
                r2 = json.loads(json.dumps(back))
                x = r2
                for k_ in path[:-1]:
                    x = x[k_]
                x[path[-1]] = val
                if not record_problems(r2):
                    bad.append(path)
            r3 = json.loads(json.dumps(back))
            g3 = r3["cases"]["projection"]["guards"]["A1"]["fisher_grid"][40]["fisher"]
            g3["exact"] = M.fs(Fraction(g3["exact"]) + Fraction(1, 10 ** 12))    # a display-invisible change
            if not any("sha256" in p for p in record_problems(r3)):
                bad.append("an exact grid value moved below the display")
            r4 = json.loads(json.dumps(back))
            gu4 = r4["cases"]["projection"]["guard_unit"]
            gu4["exact"] = M.fs(Fraction(gu4["exact"]) + Fraction(1, 10 ** 12))    # the unit figure, likewise
            if not any("the unit's guard figure" in p for p in record_problems(r4)):
                bad.append("the unit's guard figure moved below the display")
            return not bad, bad
        chk("record_problems reports a perturbed total, L, stop, crit, false pause, realised rounding and rate, "
            "pausing figure (label and value), grid maximum, abs crit, joint, gate flag, exact4, hours, count, p0, "
            "readings, the cited row, the cap, a realised exact count, the unit's guard figure (display and exact), "
            "the joint's and one in the realised case; and an exact value moved below its display (the digest), and "
            "the unit's figure likewise",
            record_check_bites)

        def report_check_bites():
            lines = so.splitlines()
            alt = []
            for old, new in (("abs 0.1781, Fisher 0.1320", "abs 0.1320, Fisher 0.1781"),
                             ("A3 0.2327", "A3 0.2401"), ("  k 29-28: ", "  k 29-27: "),
                             ("832 launches x 641.6-713.6 s", "832 launches x 641.6-713.7 s"),
                             ("| **≈ 326 h** |", "| **≈ 327 h** |"),
                             ("TOTAL 832; LOOKS 21", "TOTAL 832; LOOKS 20"),
                             ("per sham launch 63/8 rounds", "per sham launch 8 rounds"),
                             ("POWER A3 at the planned floors (144, 56)", "POWER A3 at the planned floors (144, 48)"),
                             ("share no session): 0.5390", "share no session): 0.5318"),
                             ("the unit's guard figure 0.5390", "the unit's guard figure 0.5105")):
                new_lines = [ln.replace(old, new) for ln in lines]
                alt.append((old, new_lines))
            first = next(i for i, ln in enumerate(lines) if ln.startswith("CASE sham_at_floor_min"))
            nxt = next(i for i, ln in enumerate(lines) if i > first and ln.startswith("CASE "))
            alt.append(("a dropped case", lines[:first] + lines[nxt:]))
            alt.append(("a dropped reading", lines[:-1]))
            bad = [n for n, ls in alt if ls == lines or not line_problems_f3(back, "\n".join(ls))]
            return not bad, bad
        chk("line_problems_f3 reports a report with the guard's halves swapped, a joint guard showing another pair's "
            "union, a rows label, the hours' basis, a cited row, the looks, the realised rate, a power floor or the "
            "unit's guard figure (a case's or the joint's) altered, a case section dropped, or a reading dropped",
            report_check_bites)
        chk("compute's STOP branches: the bars, k = 0, the launch cross-check, a launch row other than m:238's, "
            "non-integer units, the look count, the realised case's denominators, the rows' oracles, the citation's "
            "total", lambda: _stop_probe(m))
        chk("the checks a correct run never fires, each made to fire once: the rows' oracles (an hours cell and a "
            "row of m:234-241, m:330's look count) stop compute(); the analyzer's planned floors, its alpha and P, "
            "and its cached A1 floors stop power_block_f3(); evaluate_problems reports a crit moved; bar_problems_f3 "
            "reports m_gpwr's guard p0 moved", lambda: _unexercised_probes(m, back))
    chk("the sources: every input's committed text, at its own commit (the seat's raw at cdccc66, the G-F3 entry at "
        "2193832, the rest at the load commit), carries its quotes, each source with its quote count as built; the "
        "seat's raw, PROPOSAL-m, F-5's raw and Q7's raw at their sha256s (LOCK-m-F3 and the G-F3 entry by their "
        "quotes)",
        lambda: (lambda pr, rc: (not pr and sources_commits_ok(rc) and sources_shape_ok(SOURCES), (pr, rc)))(
            *sources_problems(_LOAD_COMMIT)))

    def sources_bite():
        lacks = sources_record(_LOAD_COMMIT, ((SOURCES[0][0], SOURCES[0][1], "0" * 64,
                                              ("not in the answers, by construction",)),))[0]
        real = sources_record
        moved = _with("sources_record", lambda lc, s=SOURCES: (lambda pr, rc: (pr, [dict(x, commit=lc) for x in rc]))(
            *real(lc, s)), lambda: sources_problems(_LOAD_COMMIT)[0])
        rc = real(_LOAD_COMMIT)[1]
        last = SOURCES[-1]
        dropped = SOURCES[:-1] + ((last[0], last[1], last[2], last[3][1:]),)   # the resume import line dropped
        return (any("lacks" in x for x in lacks) and any("sha256" in x for x in lacks)
                and any("own commit" in x for x in moved)
                and not sources_commits_ok([dict(rc[0], commit=_LOAD_COMMIT)] + rc[1:])
                and not sources_shape_ok(dropped), (lacks[:2], moved[:1]))
    chk("the sources check reports a quote the text lacks, a sha256 that differs, and every source read at the load "
        "commit (sources_problems); sources_commits_ok refuses the seat's raw recorded at the load commit; "
        "sources_shape_ok refuses the sources with one quote dropped", sources_bite)

    def citations_ok():
        now = citation_problems()
        typo = _with("SEAT_COMMIT", "cdccc67", citation_problems)
        later_entry = _with("GF3_COMMIT", _LOAD_COMMIT[:7],
                            lambda: _with("GF3_COMMIT_FULL", _LOAD_COMMIT, citation_problems))
        later_seat = _with("SEAT_COMMIT", _LOAD_COMMIT[:7],
                           lambda: _with("SEAT_COMMIT_FULL", _LOAD_COMMIT, citation_problems))
        return (not now and any("prefix" in x for x in typo) and any("G-F3 entry" in x for x in later_entry)
                and any(SEAT_RAW in x for x in later_seat), (now, typo[:1], later_entry[:1], later_seat[:1]))
    chk("the pinned commits are the citations they stand for: cdccc66, and 2193832 as the seat's raw cites the G-F3 "
        "entry, are their full shas' prefixes, and the seat's raw and the G-F3 entry each first appear at its pinned "
        "commit; the check reports a mistyped abbreviation and the load commit pinned in either's place",
        citations_ok)
    chk("the int-to-str digit cap is lifted: a figure of 5,001 digits renders (M.fs)",
        lambda: len(M.fs(Fraction(1, 10 ** 5000))) == 5003)

    def bound_constants():
        bad = []
        f2 = json.loads(json.dumps(schedule.FLOORS))
        f2["A1"]["uncached"] = 96
        for over in ({"K": 28}, {"N_Q": 41}, {"PER_TEMPLATE": {**PER_TEMPLATE, "A3": (5, 8)}},
                     {"FLOORS": f2}, {"FLOORS": {**schedule.FLOORS, "A2s": 48}},
                     {"UNIT_SIZE": {**schedule.UNIT_SIZE, "A3": 32}}, {"LOOK_EVERY": 32}, {"PATH": "cached"},
                     {"POWER_SPEC": {**POWER_SPEC, "A3": (Fraction(1, 100), Fraction(13, 20))}},
                     {"POWER_ORACLE": {**POWER_ORACLE, "A2": ".848"}}, {"POWER_FLOOR": Fraction(4, 5)},
                     {"BAR_ROWS": {**BAR_ROWS, "own_pair_lexical": ("binomial_look", Fraction(1, 20), Fraction(1, 20),
                                                                    "lexical_sham", True)}},
                     {"BAR_ROWS": {**BAR_ROWS, "exclusion_guard_abs": ("guard_abs", Fraction(3, 20), Fraction(1, 20),
                                                                       "contrast_arm", True)}},
                     {"LEXICAL": ("A1s", "A3s")}, {"SHAM_QUAL": 23}, {"REALISED": {"rounds": (190, 240),
                                                                                    "lines": (98, 144)}},
                     {"REALISED": {"rounds": (189, 240), "lines": (98, 150)}},
                     {"BASIS_S": (Fraction(3208, 5), Fraction(3569, 5))},
                     {"TABLE_ROWS": {**TABLE_ROWS, range(28, 30): (128, 64, 224, 96, 832, 21, "148–166")}},
                     {"TABLE_AFTER": {**TABLE_AFTER, 22: 1080}}, {"M330_LOOKS": M330_LOOKS[:-1] + ((25, (960,)),)},
                     {"A5_ROWS": A5_ROWS[:5] + ("| beside: m:230's |",)}, {"A5_TOTAL": 864},
                     {"SEAT_A7": SEAT_A7.replace("29/40", "28/40")}, {"F5_TEXT": F5_TEXT.replace("96/32", "80/32")},
                     {"Q7": (Q7_PRE, Q7_A.replace("136 of 160", "189 of 240"), Q7_B, Q7_C)},
                     {"SEAT_SHA256": "0" * 64}, {"PROPOSAL_M_SHA256": "1" * 64}, {"F5_SHA256": "3" * 64},
                     {"Q7_SHA256": "4" * 64}, {"GF3_COMMIT": "2193833"}):
            if not sources_record(_LOAD_COMMIT, build_sources(over))[0]:
                bad.append(sorted(over))
        return not bad, bad
    chk("each constant bound to its text: a perturbed k, n_q, per-template count, floor (two), balance unit, look "
        "cadence, path, alpha, m:190 figure, power floor, bar p0 (two), lexical domain, sham sessions, realised units "
        "(two), basis, table row, after-line total, m:330 look count, cited row, cited total, verbatim text (three), "
        "pinned sha256 (four) or the G-F3 entry's cited commit refuses the sources (31 cases)", bound_constants)

    def locks_ok():
        texts, scan = lock_scan(_LOAD_COMMIT)
        now = lock_problems(texts, [SELF_REL, RECORD_OF_RECORD], in_force_only=True)
        real = lock_texts
        dropped = _with("lock_texts", lambda c: dict(sorted(real(c).items())[1:]),
                        lambda: lock_scan(_LOAD_COMMIT)[1])
        unknown = _with("KNOWN_LOCKS", KNOWN_LOCKS + ("LOCK-not-at-root.md",), lambda: lock_scan(_LOAD_COMMIT)[1])
        probe = {"LOCK-x.md": f"names `{SELF_REL}`", LOCK_F3: f"# LOCK-m-F3.md — v0.2\n{RECORD_OF_RECORD}"}
        later = {LOCK_F3: f"{LOCK_F3_V1_HEAD}0 (x)\n{SELF_REL}\n{RECORD_OF_RECORD}"}
        return (not now and not scan and any("the lock scan read" in x for x in dropped)
                and any("the root lacks" in x for x in unknown)
                and len(lock_problems(probe, [SELF_REL, RECORD_OF_RECORD], True)) == 2
                and lock_problems(later, [SELF_REL], True) == [] and lock_problems(later, [SELF_REL], False) != [],
                (now, scan, dropped, unknown))
    chk("no lock in force at G-PWR's step names this program or its record of record (every LOCK*.md at the load "
        "commit; a LOCK-m-F3 at v1.0 follows G-PWR and is exempt), and the scan is complete (lock_scan: its names "
        "equal the root's LOCK*.md listed apart, the seven known when this program was built among them); the checks "
        "report a lock that names either, a scan that drops a lock, and a known lock the root lacks", locks_ok)
    chk("the harness counts a check that raises, stops, or returns a false value, as a FAIL",
        lambda: _run_check_f3(lambda: 1 / 0)[0] is False and _run_check_f3(lambda: (False, "x"))[0] is False
        and _run_check_f3(lambda: (_ for _ in ()).throw(SystemExit("STOP: x")))[0] is False
        and _run_check_f3(lambda: True)[0] is True)
    print(f"selftest: {'PASS' if not fails else 'FAIL'} ({len(fails)} failed)")
    return 0 if not fails else 1


def _region_probe() -> tuple[bool, list]:
    """region_problems_f3 against m_gpwr's guard_regions with one defect each, through a stand-in of this module's own
    reference (never m_gpwr's attribute)."""
    real = M.guard_regions
    bad = []

    def drop_cell(looks, alpha=M.ALPHA, abs_p0=M.GUARD_ABS_P0):
        out = real(looks, alpha, abs_p0)
        for r_ in out:
            r_["fisher"] = set(sorted(r_["fisher"])[1:])
        return out

    def crit_up(looks, alpha=M.ALPHA, abs_p0=M.GUARD_ABS_P0):
        out = real(looks, alpha, abs_p0)
        for r_ in out:
            r_["abs_crit"] = None if r_["abs_crit"] is None else r_["abs_crit"] + 1
        return out
    for label, stand_in in (("a dropped cell", drop_cell), ("abs crit", crit_up)):
        stub = SimpleNamespace(guard_regions=stand_in, ALPHA=M.ALPHA, GUARD_ABS_P0=M.GUARD_ABS_P0)
        if not _with("M", _MProxy(stub), lambda: region_problems_f3(20, 20)):
            bad.append(label)
    return not bad, bad


class _MProxy:
    """m_gpwr with the stub's attributes stood in (the self-test's probes only): every other attribute is m_gpwr's
    own."""

    def __init__(self, stub):
        self._stub = stub

    def __getattr__(self, name):
        return getattr(self._stub, name) if hasattr(self._stub, name) else getattr(sys.modules["m_gpwr"], name)


class _AnalyzerStandIn:
    """The analyzer with one call's block altered by `mutate` (the probes of power_block_f3's STOPs only)."""

    def __init__(self, real, arm: str, path: str, mutate):
        self.real, self.arm, self.path, self.mutate = real, arm, path, mutate

    def f3_power_block(self, arm, n0, n1, mS, path):
        pb = json.loads(json.dumps(self.real.f3_power_block(arm, n0, n1, mS, path)))
        if (arm, path) == (self.arm, self.path):
            self.mutate(pb)
        return pb


def _unexercised_probes(m, back: dict) -> tuple[bool, list]:
    """The checks a correct run never fires, each made to fire once (the review's MINOR-3): the rows' oracles stop
    compute() on an hours cell and a row of m:234-241 and on m:330's look count; power_block_f3() stops on the
    analyzer's planned floors, its alpha and P, and its cached A1 floors; evaluate_problems reports a crit moved;
    bar_problems_f3 reports m_gpwr's guard p0 moved (a stand-in of this module's own reference M)."""
    missed = []
    t1 = {**TABLE_ROWS, range(35, 41): (96, 64, 176, 80, 672, 17, "121–133")}
    t2 = {**TABLE_ROWS, range(32, 35): (128, 64, 208, 80, 736, 19, "131–146")}
    for label, name, val in (("an hours cell", "TABLE_ROWS", t1), ("a row's launches", "TABLE_ROWS", t2),
                             ("m:330's look count", "M330_LOOKS", ((18, (672,)),) + M330_LOOKS[1:])):
        msg = _with(name, val, lambda: _stop_message(lambda: compute(m)))
        if not msg.startswith("STOP: the rows by k differ"):
            missed.append((label, msg[:100]))

    def n_up(pb):
        pb["planned"]["n"] += 16

    def alpha_moved(pb):
        pb["of_record"]["alpha"] = "1/20"

    def cached_floor(pb):
        pb["planned"]["n"] = 80
    for label, arm, path, mut, want in (
            ("planned floors", "A2", PATH, n_up, "STOP: A2: the analyzer's planned floors"),
            ("alpha and P", "A1", PATH, alpha_moved, "STOP: A1: the analyzer's alpha and P"),
            ("cached A1 floors", "A1", "cached", cached_floor, "STOP: the analyzer's cached A1 floors")):
        msg = _stop_message(lambda: power_block_f3(_AnalyzerStandIn(m, arm, path, mut)))
        if not msg.startswith(want):
            missed.append((label, msg[:100]))
    r2 = json.loads(json.dumps(back))
    r2["cases"]["sham_at_floor_r"]["bars"]["reasoning_line_defect"]["crit_j"][3] += 1
    if not evaluate_problems(r2):
        missed.append(("evaluate_problems", "silent on a crit moved"))
    moved = _with("M", _MProxy(SimpleNamespace(GUARD_ABS_P0=Fraction(3, 20))), bar_problems_f3)
    if not any("GUARD_ABS_P0" in x for x in moved):
        missed.append(("bar_problems_f3", "silent on m_gpwr's guard p0 moved"))
    return not missed, missed


def sources_shape_ok(sources) -> bool:
    """The sources as built: their sha256 pins and each one's quote count (QUOTE_COUNTS; round 3's NOTE 1), so a quote
    dropped from build_sources fails (a quote shortened in place still matches: the count binds the set, not the
    words)."""
    return ([s[2] for s in sources] == [SEAT_SHA256, None, PROPOSAL_M_SHA256, None, F5_SHA256, Q7_SHA256, None]
            and [len(s[3]) for s in sources] == list(QUOTE_COUNTS))


def sources_commits_ok(recorded: list[dict]) -> bool:
    """Each source read at its own commit (the review's MINOR-2): the seat's raw at cdccc66, the G-F3 entry at
    2193832, every other at the load commit."""
    return [s["commit"] for s in recorded] == [SEAT_COMMIT_FULL, GF3_COMMIT_FULL] + [_LOAD_COMMIT] * (len(SOURCES) - 2)


# --- provenance and the run of record ------------------------------------------------------------------------------
def provenance_f3() -> dict:
    """The run of record binds committed blobs only: this script, m_gpwr (executed from its blob), the analyzer, every
    valence_core/m/*.py and every valence_core/mf3/*.py at the load commit, each with working-tree bytes equal to its
    blob, and the closure of the repository modules this process loaded; m_gpwr's helpers decide each condition,
    unchanged. mf3's package sha256 is recorded by valence_core.m.resume's formula."""
    head_pkg = sorted(p for p in M._git("ls-tree", "--name-only", _LOAD_COMMIT, "valence_core/m/").split()
                      if p.endswith(".py"))
    disk_pkg = sorted(str(p.relative_to(REPO)) for p in (REPO / "valence_core" / "m").glob("*.py"))
    head_f3 = sorted(p for p in M._git("ls-tree", "--name-only", _LOAD_COMMIT, "valence_core/mf3/").split()
                     if p.endswith(".py"))
    disk_f3 = sorted(str(p.relative_to(REPO)) for p in (REPO / "valence_core" / "mf3").glob("*.py"))
    closure = sorted(set(M.closure_files()) | {SELF_REL})
    blobs, disk = {}, {}
    for rel in M.bound_paths(head_pkg) + closure + [p for p in head_f3 if p not in closure]:
        blobs[rel] = M._gitrun("rev-parse", f"{_LOAD_COMMIT}:{rel}", text=True).stdout.strip()
        disk[rel] = (M._gitrun("hash-object", "--no-filters", "--", rel, text=True).stdout.strip()
                     if (REPO / rel).is_file() and not (REPO / rel).is_symlink() else "")
    probs = M.provenance_problems(head_pkg, disk_pkg, blobs, disk, closure)
    if head_f3 != disk_f3:
        probs.append(f"valence_core/mf3/*.py differ from the load commit's tree: {sorted(set(head_f3) ^ set(disk_f3))}")
    probs += [f"{rel}: not committed at the load commit with identical working-tree bytes" for rel in head_f3
              if rel not in closure and (not blobs.get(rel) or blobs[rel] != disk.get(rel))]
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
        raise SystemExit("REFUSED: G-PWR (Q-F3) of record binds committed blobs only:\n  " + "\n  ".join(probs))
    data = {rel: M._blob_bytes(blobs[rel]) for rel in M.bound_paths(head_pkg) + closure}
    sha = lambda rel: hashlib.sha256(data[rel]).hexdigest()  # noqa: E731
    pkg = M._pkg_sha256([(rel, data[rel]) for rel in head_pkg])
    if pkg != resume.package_sha256():
        raise SystemExit(f"REFUSED: the package's sha256 over the load commit's blobs {pkg} is not its value on disk "
                         f"{resume.package_sha256()}")
    pkg_f3 = M._pkg_sha256([(rel, M._blob_bytes(blobs[rel])) for rel in head_f3])
    if pkg_f3 != resume.package_sha256_of(REPO / "valence_core" / "mf3"):
        raise SystemExit("REFUSED: mf3's package sha256 over the load commit's blobs is not its value on disk")
    return {"head": _LOAD_COMMIT, "script_sha256": sha(SELF_REL), "m_gpwr_sha256": sha(M_REL), "m_gpwr_blob": M_BLOB,
            "analyzer_sha256": sha(ANALYZER_REL), "package_sha256": pkg, "mf3_package_sha256": pkg_f3,
            "closure": {rel: sha(rel) for rel in closure if rel != SELF_REL}, "isolated": bool(sys.flags.isolated),
            "pycache_prefix": sys.pycache_prefix, "python": sys.version.split()[0]}


def _selftest_child() -> subprocess.CompletedProcess:
    """The self-test of record: this script's blob at the load commit, in its own isolated process."""
    return subprocess.run([sys.executable, "-I", "-B", "-X", f"pycache_prefix={sys.pycache_prefix}", "-c",
                           _F3_CHILD_BOOT, str(REPO), _LOAD_COMMIT], capture_output=True, text=True)


def main(argv=None) -> int:
    try:
        return _main(argv)
    except (_GitRead, M._GitFailed) as e:             # stated, not a traceback: nothing is written
        raise SystemExit(f"REFUSED: {e}")


def _main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--record", type=Path, help="write the G-PWR (Q-F3) JSON here (required for a run; refused if it "
                                                "exists, or if a lock names it)")
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
    rel = M._repo_rel(str(a.record))
    lock_txts, scan = lock_scan(_LOAD_COMMIT)
    if scan:
        raise SystemExit(f"REFUSED: the lock scan is incomplete: {scan}")
    named = lock_problems(lock_txts, [rel], in_force_only=False) if rel else []
    if named:
        raise SystemExit(f"REFUSED: the record's path is a file a lock names: {named}")
    if not sys.flags.isolated:
        raise SystemExit("REFUSED: a run of record runs in isolated mode (python -I)")
    if not sys.pycache_prefix or os.path.exists(sys.pycache_prefix):
        raise SystemExit("REFUSED: a run of record reads no cached bytecode: -X pycache_prefix=<a path that does not "
                         "exist>")
    prov = provenance_f3()
    loaded_at_prov = dict(M._LOADED)
    sp, srcs = sources_problems(_LOAD_COMMIT)
    if sp:
        raise SystemExit(f"REFUSED: the inputs' committed texts: {sp}")
    cp = citation_problems()
    if cp:
        raise SystemExit(f"REFUSED: the pinned commits are not the citations they stand for: {cp}")
    print(f"PROVENANCE {json.dumps(prov)}")
    print(f"SOURCES {json.dumps(srcs)}")
    st = _selftest_child()
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
    late += line_problems_f3(json.loads(text), shown.getvalue())
    if late:
        raise SystemExit(f"REFUSED: {late}")
    print(shown.getvalue(), end="")
    M.write_record(a.record, text)
    print(f"\nWROTE {a.record} sha256 {hashlib.sha256(a.record.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
