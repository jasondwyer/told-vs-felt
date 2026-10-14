#!/usr/bin/env python3
"""PROPOSAL-m analyzer -- G-ANL-F0 (v1.11 §3.1 m:278; §8 step 8, m:358). Committed BEFORE any
Q-F0 or OLMo campaign session: "VERDICTS are computed by the pre-committed analyzer before any
of 'the reads'" (m:318). MODEL-FREE BY DESIGN: no model library, no *_sessions.py, nothing
generates.

  --selftest        the synthetic battery of m:278 -- (i) every per-arm outcome of §5 for A0 and
                    A0-OLMo-{ckpt} (NOT-RUN by each listed cause, INDETERMINATE-by-no-domain, the
                    OLMo PENDING state); (ii) the 5 x 6^3 = 1,080 v1 tuples under both values of
                    the 0.12-artifact flag over the placeholder sentence table; (iii) every counter
                    per substrate -- plus the VERDICTS reader path on checkpoints the production
                    writers build on the self-test stub in a temp directory. Prints
                    "  [PASS|FAIL] name got" per check and ends "  N/N m_analyze battery checks
                    pass"; exit 0 iff every check passes, N == EXPECTED_CHECKS and every
                    coverage id is reached (m:278: "a skipped assertion is a failure").
  ganl [--out DIR]  the battery, then the write-once artifact data/m/gates/G-ANL-F0.json
                    (--out DIR: a non-canonical test directory). Exit 0 written or identical,
                    2 refused, 4 STOP (the battery failed; nothing written).
  verdicts --unit U --lock PATH --decisions PATH [--campaign P] [--time P] [--qual P]
           [--adjudication P] [--pi-stop P] [--olmo-states P] [--sentences P]
           [--flag-source P] [--out DIR]
                    one unit's VERDICTS (step 17; each OLMo checkpoint as it ends):
                    {U}_VERDICTS.json and {U}_secondary.json, or {U}_NOT-RUN.json when §5's
                    no-first-read cause holds.
  not-run --unit U --record PATH [--time P] [--qual P] [--out DIR]
                    a unit NOT-RUN by its Clock or by "dose not completable" -> {U}_NOT-RUN.json.
  posting --posting v1 --tuple PATH --sentences PATH [--rewrites PATH] [--flag-source P]
          [--verdicts-dir D] [--out DIR]
                    §7's v1 outputs under a declared tuple -> POSTING-v1_outputs.{of-record,
                    posted}.json (one per table kind). On the posted text, C7's posting bar
                    (PIN-44): PASS / FAIL, and the comparison with the VERDICTS enumeration
                    with the PI's rewrites applied (--rewrites, the rewrite list by row id:
                    required there, refused on the table of record); a FAIL writes nothing
                    and prints its record on stdout.

Exit codes (PIN-26): 0 written or identical (selftest: every check passes); 1 a selftest FAIL;
2 refused -- decided before any pick-bearing byte is interpreted, or a write-once conflict;
5 (posting only) FAIL against C7's bar on the posted text, nothing written (PIN-44);
4 STOP -- a content assertion failed after reading (any other SystemExit maps to 4, as
m_sessions.py's gcal drivers map theirs).

At step 8 no lock exists, so verdicts / not-run / posting refuse on real data; the battery runs
them in temp directories only, and reads nothing under data/m/ckpt, data/m/reports,
data/m/verdicts or results/raw (PIN-29).
"""
from __future__ import annotations

import argparse
import ast
import builtins
import contextlib
import copy
import hashlib
import io
import itertools
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

# PIN (Code, declared at LOCK v0.1): PIN-1 -- module-level imports are the declared model-free
# primitives only; stages is imported lazily on the verdict path (LAZY_VERDICT_MODULES), guard,
# testing, corr, scaffold and schedule in the battery only. The closure of the verdict path is
# computed mechanically (closure()) and bound by its sha256 in the lock.
from valence_core import session as _session                      # noqa: E402
from valence_core.e2d import habit                                # noqa: E402
from valence_core.m import audit, bars, keys, readrule, resume    # noqa: E402

# --- pinned identities -----------------------------------------------------------------------
PROPOSAL_REL = "PROPOSAL-m-gating-campaign-v1_11.md"
# PIN (Code, declared at LOCK v0.1): PIN-31 -- the proposal's sha256 is pinned here; every
# m-verbatim constant below is verified against the proposal file at run time (the battery).
PROPOSAL_SHA256 = "42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b"
ANALYZER_REL = "scripts/m_analyze.py"
GATES_REL = "data/m/gates"
PLACEHOLDER_REL = "data/m/gates/m_posting_sentences.placeholder.json"
TABLE_OF_RECORD_REL = "data/m/gates/m_posting_sentences.json"
TABLE_POSTED_REL = "data/m/gates/m_posting_sentences.posted-v1.json"
FLAG_SOURCE_REL = "data/m/gates/G-CAL_model-free.json"
FLAG_SCHEMA = "m-gcal-model-free-v1"
FLAG_INTRODUCED_AT = "bab921c"
GANL_REL = "data/m/gates/G-ANL-F0.json"
VERDICTS_REL = "data/m/verdicts"
CKPT_REL = "data/m/ckpt"
BLOCKED_REL = ("data/m/ckpt", "data/m/reports", "data/m/verdicts", "results/raw")
CLOCK_DATE = "2026-10-30"          # D1 = D_O (m:16 (11)); verified against the proposal
LAZY_VERDICT_MODULES = ("valence_core.m.stages",)
MODULE_LEVEL_IMPORTS = ("valence_core.session", "valence_core.e2d.habit", "valence_core.m.audit",
                        "valence_core.m.bars", "valence_core.m.keys", "valence_core.m.readrule",
                        "valence_core.m.resume")       # the declared model-free primitives (PIN-1)

GANL_SCHEMA = "m-ganl-f0-v1"
VERDICTS_SCHEMA = "m-verdicts-v1"
SECONDARY_SCHEMA = "m-secondary-v1"
NOT_RUN_RECORD_SCHEMA = "m-not-run-v1"
NOT_RUN_OUT_SCHEMA = "m-not-run-out-v1"
TABLE_SCHEMA = "m-posting-sentences-v1"
TUPLE_SCHEMA = "m-posting-tuple-v1"
POSTING_OUT_SCHEMA = "m-posting-v1-outputs-v1"
OLMO_STATES_SCHEMA = "m-olmo-states-v1"
DECISIONS_SCHEMA = "m-decisions-v1"
PI_STOP_SCHEMA = "m-pi-stop-record-v1"
ADJ_SCHEMA = "m-verdicts-adjudication-v1"
REWRITES_SCHEMA = "m-posting-rewrites-v1"

UNITS = ("Q-F0", "OLMo-sft", "OLMo-dpo", "OLMo-instruct")
Q5 = ("PASS", "REVERSE", "DEAD", "INDETERMINATE", "NOT-RUN")
O6 = Q5 + ("PENDING",)
ARM_STATES = ("PASS", "REVERSE", "DEAD", "INDETERMINATE")
STAGE_WORD = {"sft": "SFT", "dpo": "DPO", "instruct": "instruct"}      # m:338's spelling
GVER_BARS = ("schedule_mismatch", "template_breakage")                # verify.MISMATCH / BREAK
HAIR_BAR = "scaffold_absorption"
STUB_MARK = "SELFTEST-STUB"                                           # == stages.STUB_MARK (battery)

# --- exact arithmetic (PIN-2) ------------------------------------------------------------------
HALF = Fraction(1, 2)
ALPHA = bars.q("0.01")             # the controls' alpha (m:326)
GUARD_ALPHA = bars.q("0.05")       # the exclusion guard's (m:316)
DEAD_P = Fraction(13, 20)          # .5 + .15 (m:326)
CP_TAIL = Fraction(1, 40)          # two-sided 95%
POWER_P = Fraction(7, 10)          # m:190's sizing share
FLOOR_EVENTS = 20                  # m:312 "m's floor is 20 events"
CP_TOL = Fraction(1, 10 ** 8)


class AnlRefusal(SystemExit):
    """Refused (exit 2): decided before any pick-bearing byte is interpreted, or write-once."""


class AnlStop(SystemExit):
    """STOP (exit 4): a content assertion failed after reading."""


class AnlPostingFail(SystemExit):
    """The posting's FAIL against C7's bar on the posted text (exit 5, PIN-44): nothing written;
    ``lines`` (stdout, the record of that step: the residue by row id and, row by row, each residue
    item in full as the enumeration carries it (row_id, loc, clauses, a, b, c, treatments; no
    sentence text: the table is the reading of record), each comparison set with its rows in full,
    and the unwritten record's declared tuple (with its reasons and pending), inputs, comparator,
    flag and binding) and ``bar`` carry the result."""

    def __init__(self, lines: Sequence[str], bar: Mapping) -> None:
        super().__init__("\n".join(lines))
        self.lines, self.bar = list(lines), copy.deepcopy(dict(bar))


class BothArmsEmpty(ValueError):
    """Neither arm has a domain session: the unit layer's NOT-RUN (§5), never an arm outcome."""


def fs(x: Any) -> str:
    """An exact rational as 'num/den' (the stored form of every p, share and bound)."""
    x = Fraction(x)
    return f"{x.numerator}/{x.denominator}"


def dec(x: Any, places: int = 4) -> str:
    """Half-up display of a NON-NEGATIVE Fraction (bars._dec); display only."""
    x = Fraction(x)
    if x < 0:
        raise ValueError("dec() displays a non-negative Fraction; use sdec() for a signed value")
    return bars._dec(x, places)


def sdec(x: Any, places: int = 4) -> str:
    """A signed Fraction: an ASCII sign, then bars._dec of the magnitude (half-up on the magnitude)."""
    # PIN (Code, declared at LOCK v0.1): PIN-36 -- bars._dec is defined for non-negative Fractions
    # only (it misprints -1/20 as "-1.9500"); every signed value prints as "-" or "+" (zero takes
    # "+") followed by _dec(|x|), so -1/20 prints "-0.0500" and +1/20 "+0.0500" (gcal.dec4's form).
    x = Fraction(x)
    return ("-" if x < 0 else "+") + bars._dec(abs(x), places)


def binom_cdf(k: int, n: int, p: Any) -> Fraction:
    """Exact P(X <= k), X ~ Bin(n, p)."""
    return 1 - bars.binom_sf(k + 1, n, p)


def p_up(k: int, n: int) -> Fraction:
    """One-sided exact binomial vs .5 toward clean: P(X >= k)."""
    return bars.binom_sf(k, n, HALF)


def p_down(k: int, n: int) -> Fraction:
    """Toward corrupted: P(X <= k) = P(n - X >= n - k) under p = .5."""
    return bars.binom_sf(n - k, n, HALF)


def dead_pred(k: int, n: int) -> bool:
    """DEAD's predicate, exact (PIN-2): the two-sided CP 95% upper bound on P is < 13/20 iff
    k < n and P(Bin(n, 13/20) <= k) < 1/40 (P(X <= k; p) strictly decreasing in p)."""
    # PIN (Code, declared at LOCK v0.1): PIN-2 -- DEAD ⇔ k < n ∧ P(Bin(n,13/20) ≤ k) < 1/40,
    # strict (equality is not DEAD); at k = n the upper bound is 1, never DEAD.
    return k < n and binom_cdf(k, n, DEAD_P) < CP_TAIL


def cp_interval(k: int, n: int) -> tuple[Fraction, Fraction] | None:
    """Two-sided Clopper-Pearson 95% on P by exact bisection on Fractions to width < 1e-8.
    Display only: no decision reads it (PIN-2)."""
    if n == 0:
        return None
    if k == 0:
        lo = Fraction(0)
    else:
        a, b = Fraction(0), Fraction(1)            # P(X >= k; p) increases in p
        while b - a >= CP_TOL:
            m = (a + b) / 2
            if bars.binom_sf(k, n, m) < CP_TAIL:
                a = m
            else:
                b = m
        lo = (a + b) / 2
    if k == n:
        hi = Fraction(1)
    else:
        a, b = Fraction(0), Fraction(1)            # P(X <= k; p) decreases in p
        while b - a >= CP_TOL:
            m = (a + b) / 2
            if binom_cdf(k, n, m) > CP_TAIL:
                a = m
            else:
                b = m
        hi = (a + b) / 2
    return lo, hi


def _cnt(x: Any, what: str) -> int:
    if isinstance(x, (bool, float)) or not isinstance(x, int) or x < 0:
        raise ValueError(f"{what} must be a non-negative int count, got {x!r}")
    return x


# --- §5 per-arm outcome (positive controls) ------------------------------------------------------
def arm_outcome(n0: int, k0: int, n1: int, k1: int, mS: int, j: int, alpha: Fraction = ALPHA) -> dict:
    """§5's ordered evaluation for a positive control (m:326), conjuncts as m:310.

    n_m / k_m: the arm's domain sessions on map m and those coded 1 (the P-role label chosen at
    the first free choice, m:306); mS / j: the matched sham's domain sessions and its P-role first
    picks (E = |j/mS - 1/2|, m:310). Order: INDETERMINATE 'no read obtained' -> REVERSE -> PASS ->
    DEAD -> INDETERMINATE (terminal; not-PASS)."""
    n0, k0, n1, k1, mS, j = (_cnt(v, w) for v, w in ((n0, "n0"), (k0, "k0"), (n1, "n1"), (k1, "k1"),
                                                     (mS, "mS"), (j, "j")))
    if k0 > n0 or k1 > n1 or j > mS:
        raise ValueError(f"a count exceeds its denominator: {(n0, k0, n1, k1, mS, j)}")
    alpha = bars.q(alpha)
    n, k = n0 + n1, k0 + k1
    if n + mS == 0:
        raise BothArmsEmpty("neither arm has a domain session: the unit is NOT-RUN by §5 (m:324), "
                            "never an arm outcome")
    st: dict[str, Any] = {"n0": n0, "k0": k0, "n1": n1, "k1": k1, "n": n, "k": k, "mS": mS, "j": j}
    if n:
        P = Fraction(k, n)
        st.update(P=P, delta=P - HALF, p_up=p_up(k, n), p_down=p_down(k, n),
                  share0=Fraction(k0, n0) if n0 else None, share1=Fraction(k1, n1) if n1 else None,
                  dead_tail=binom_cdf(k, n, DEAD_P))
    if mS:
        PS = Fraction(j, mS)
        st.update(PS=PS, E=abs(PS - HALF))
    if n == 0 or mS == 0:
        # PIN (Code, declared at LOCK v0.1): PIN-4 -- the no-read sub-reason is recorded beside the
        # shared sentence: 'contrast-empty' (the arm has no domain session) or 'sham-empty' (its
        # sham has none, so E is undefined, m:247, m:310); predicates are unevaluable (None).
        return {"state": "INDETERMINATE", "noread": "contrast-empty" if n == 0 else "sham-empty",
                "route": None, "stats": st, "pred": None}
    P, E = st["P"], st["E"]
    delta = st["delta"]
    pred = {
        "i_up": delta > E, "i_dn": delta < -E,
        "ii_up": n0 > 0 and n1 > 0 and 2 * k0 >= n0 and 2 * k1 >= n1,
        "ii_dn": n0 > 0 and n1 > 0 and 2 * k0 <= n0 and 2 * k1 <= n1,
        "iii_up": st["p_up"] <= alpha, "iii_dn": st["p_down"] <= alpha,
        "dead": dead_pred(k, n),
    }
    if pred["i_dn"] and pred["ii_dn"] and pred["iii_dn"]:
        state = "REVERSE"
    elif pred["i_up"] and pred["ii_up"] and pred["iii_up"]:
        state = "PASS"
    elif pred["dead"]:
        state = "DEAD"
    else:
        state = "INDETERMINATE"
    route = None
    if state == "INDETERMINATE":
        route = {"toward_clean": [c for c in ("i", "ii", "iii") if not pred[f"{c}_up"]],
                 "toward_corrupted": [c for c in ("i", "ii", "iii") if not pred[f"{c}_dn"]],
                 "dead": False}
    return {"state": state, "noread": None, "route": route, "stats": st, "pred": pred}


def outcome_json(out: Mapping) -> dict:
    """An arm outcome in its stored form: every rational as 'num/den' beside its display."""
    st = {}
    for k_, v in out["stats"].items():
        if isinstance(v, Fraction):
            st[k_] = {"exact": fs(v), "display": sdec(v) if k_ == "delta" else dec(v)}
        else:
            st[k_] = v
    return {"state": out["state"], "noread": out["noread"], "route": out["route"],
            "pred": None if out["pred"] is None else dict(out["pred"]), "stats": st}


# --- attained power (PIN-3) -----------------------------------------------------------------------
def power_exact(n0: int, n1: int, mS: int, alpha: Fraction = ALPHA, p: Fraction = POWER_P) -> Fraction:
    """Exact P(PASS under (i)-(iii)) with clean share p on both maps (n0, n1) and the sham at .5 on
    mS (E pooled). 0 when a map or the sham is empty ((ii) or E fails)."""
    n0, n1, mS = _cnt(n0, "n0"), _cnt(n1, "n1"), _cnt(mS, "mS")
    if n0 == 0 or n1 == 0 or mS == 0:
        return Fraction(0)
    p = Fraction(p)
    a, b = p.numerator, p.denominator
    n = n0 + n1
    crit = bars.critical_k(n, HALF, alpha)
    if crit is None:
        return Fraction(0)

    def weights(m: int) -> dict[int, int]:
        return {i: comb(m, i) * a ** i * (b - a) ** (m - i) for i in range(m + 1) if 2 * i >= m}
    w0, w1 = weights(n0), weights(n1)
    D = [0] * (n + 1)
    for x, wx in w0.items():
        for y, wy in w1.items():
            D[x + y] += wx * wy
    tail = [0] * (n + 2)
    for kk in range(n, -1, -1):
        tail[kk] = tail[kk + 1] + D[kk]
    total = 0
    for jj in range(mS + 1):
        # (i): k/n - 1/2 > |jj/mS - 1/2|  <=>  2 k mS > n mS + n |2 jj - mS|
        bound = n * mS + n * abs(2 * jj - mS)
        thr = bound // (2 * mS) + 1
        t = max(thr, crit)
        if t <= n:
            total += comb(mS, jj) * tail[t]
    return Fraction(total, b ** n * 2 ** mS)


def power_block(n_realised0: int, n_realised1: int, mS: int) -> dict:
    """The power figure of record (m:190's base case at the realised n) and the realised split."""
    # PIN (Code, declared at LOCK v0.1): PIN-3 -- the figure of record splits the realised domain
    # n as floor(n/2) on map 0 and ceil(n/2) on map 1 (m:190: "each arm split n/2 per map"), the
    # sham pooled at its realised domain m; the realised map split is reported beside, labelled.
    # Accepted by the seat (C6, 2026-10-10) as the declared base-case computation, re-derived at G-PWR
    # (step 15) with the planned floors, where the realised-n figure becomes the figure of record
    # (m:190).
    n = n_realised0 + n_realised1
    rec = power_exact(n // 2, n - n // 2, mS)
    real = power_exact(n_realised0, n_realised1, mS)
    return {"of_record": {"exact": fs(rec), "display": dec(rec, 3),
                          "basis": "m:190's base case at the realised n: the arm split floor(n/2) / "
                                   "ceil(n/2) per map at clean share .70, the sham pooled at .5, "
                                   "alpha .01 (descriptive; the power figure of record)",
                          "n": n, "split": [n // 2, n - n // 2], "mS": mS},
            "realised_split": {"exact": fs(real), "display": dec(real, 3),
                               "basis": "the realised per-map domain counts (beside; not of record)",
                               "split": [n_realised0, n_realised1], "mS": mS}}


# --- NOT-RUN causes (PIN-5), PENDING (PIN-6) -------------------------------------------------------
# PIN (Code, declared at LOCK v0.1): PIN-5 -- the cause codes, their cites and the reason phrases a
# label prints after "was not run: " (Code-authored, accepted with their precedence by the seat, C6,
# 2026-10-10; the PI rewrites them at posting). The record names one primary cause (the earliest in time) and lists the others in
# `also`; the label prints the primary. The <stage> of clock:gate-stopped / clock:not-locked is one
# of gate_stop_stages(unit): every gate that precedes the unit's LOCK v1.0 and can end in a STOP --
# G-ID-F0m included (its divergence verdict sends Q-F0 uncached, m:281, but a hair-trigger fire or a
# G-VER failure there stops the stage, m:271, m:284), and G-CAL on every unit (it serves all units,
# m:176, m:276; the OLMo track starts at step 9, after it, m:300, m:358). clock:not-locked is the
# residual Clock cause (m:347 is unconditional): a Clock miss whose blocking stage had not reached
# its end (a pause awaiting the seat's adjudication, m:302; a gate still open) -- confirmed by the
# seat (C1, 2026-10-10): m:324's parenthetical ends "or any reason", so its list is not exhaustive by
# its own words, and clock:not-locked:<stage> is a reading of that clause, not an addition to it.
NOT_RUN_CAUSES: dict[str, dict] = {
    "clock:no-box": {"cite": "m:324 (no box; ...)", "units": "olmo",
                     "phrase": "no box before its Clock date ({date})"},
    "clock:gate-stopped": {"cite": "m:324 a gate STOPPED and no re-specification was locked; m:271 a "
                                   "hair-trigger fire anywhere stops the stage; m:275, m:276, m:280, "
                                   "m:281, m:283, m:284, m:302, m:176, m:358", "units": "both",
                           "param": "stage",
                           "phrase": "{stage} stopped and no re-specification was locked by its "
                                     "Clock date ({date})"},
    "clock:not-locked": {"cite": "m:347 A Q-F0 not locked by D1 / a checkpoint not locked by D_O is "
                                 "NOT-RUN; m:302 a pause -> the seat's adjudication (residual: the "
                                 "blocking stage had not reached its end; m:324's 'or any reason', the "
                                 "seat's C1)",
                         "units": "both", "param": "stage",
                         "phrase": "{stage} had not reached its end and no LOCK v1.0 was committed by "
                                   "its Clock date ({date})"},
    "clock:pi-declined": {"cite": "m:324 the PI declined to commit v1.0, for projected hours or any "
                                  "reason", "units": "both",
                          "phrase": "the PI declined to commit its LOCK v1.0 by its Clock date ({date})"},
    "clock:k-zero": {"cite": "m:192 At k = 0 ... the unit is NOT-RUN by its Clock", "units": "both",
                     "phrase": "no valid qualification session (k = 0), so no launch count and no "
                               "LOCK v1.0 by its Clock date ({date})"},
    "dose-not-completable": {"cite": "m:324, m:302 NOT-RUN \"dose not completable\"", "units": "olmo",
                             "phrase": "dose not completable"},
    "no-first-read:pi-stop": {"cite": "m:324 before a PI stop", "units": "both",
                              "phrase": "no session reached a first read before a PI stop"},
    "no-first-read:gver-stop": {"cite": "m:324, m:284 a G-VER STOP", "units": "both",
                                "phrase": "no session reached a first read before a G-VER STOP"},
    "no-first-read:cap": {"cite": "m:324 or its cap", "units": "both",
                          "phrase": "no session reached a first read before its hour cap"},
    "pending-closed-at-v2": {"cite": "m:324 closed there ... else NOT-RUN with the reason recorded",
                             "units": "olmo", "v2_only": True,
                             "phrase": "still pending at the v2 posting, with no session"},
}
NOT_RUN_FROM_RECORD = ("clock:no-box", "clock:gate-stopped", "clock:not-locked", "clock:pi-declined",
                       "clock:k-zero", "dose-not-completable")
PARAM_CAUSES = ("clock:gate-stopped", "clock:not-locked")


def gate_stop_stages(unit: str) -> tuple[str, ...]:
    """The gates before the unit's LOCK v1.0 that can end in a STOP (and so reach NOT-RUN through the
    Clock, m:324), in step order. G-ID-F0m is one: its divergence verdict only sends Q-F0 uncached
    (m:281), but a hair-trigger fire or a G-VER failure stops it (m:271, m:284). G-CAL serves every
    unit (m:176, m:276) and precedes the OLMo track (step 9, m:358). OLMo has no G-ID (uncached,
    m:267); G-PORT passed before the OLMo track and is Q-F0's."""
    if unit == "Q-F0":
        return ("G-PORT", "G-CAL", "G-SHAPE-F0", "G-ANL-F0", "G-TIME-F0", "G-ID-F0m", "G-F0m-Qwen")
    c = _ckpt(unit)
    return ("G-CAL", "G-SHAPE-F0", "G-ANL-F0", f"G-TIME-OLMo-{c}", f"G-F0m-OLMo-{c}")


def _ckpt(unit: str) -> str:
    if unit.startswith("OLMo-") and unit[5:] in keys.CKPTS:
        return unit[5:]
    raise ValueError(f"not an OLMo unit: {unit!r}")


def _sub(unit: str) -> str:
    if unit not in UNITS:
        raise ValueError(f"unknown unit {unit!r}; built units are {UNITS}")
    return "qwen" if unit == "Q-F0" else "olmo"


def parse_cause(code: str) -> tuple[str, str | None]:
    if not isinstance(code, str):
        raise ValueError(f"cause code must be a str, got {code!r}")
    for pc in PARAM_CAUSES:
        if code.startswith(pc + ":"):
            return pc, code[len(pc) + 1:]
    if code not in NOT_RUN_CAUSES or code in PARAM_CAUSES:
        raise ValueError(f"unknown NOT-RUN cause {code!r}; vocabulary {sorted(NOT_RUN_CAUSES)} "
                         f"(gate-stopped / not-locked as clock:<cause>:<stage>)")
    return code, None


# PIN (Code, declared at LOCK v0.1): PIN-43 -- every declared date (a NOT-RUN record's, a declared
# OLMo NOT-RUN state's in --olmo-states, a PENDING declaration's Clock comparison, a decision's) is an
# ASCII YYYY-MM-DD that is a real calendar date (datetime.date.fromisoformat accepts it): non-ASCII
# digits, the basic and week forms (20261030, 2026-W44-5) and impossible days (2026-02-30, 2026-02-29)
# refuse; a NOT-RUN record's and a declared NOT-RUN state's date are checked whatever the cause, since
# each is carried into an output even where the reason phrase has no {date} (dose-not-completable).
# Confirmed by the seat (C5, 2026-10-10), the fixes ratified; for a no-first-read NOT-RUN declared in
# --olmo-states the date is the calendar date of the terminal event that made the NOT-RUN final -- the
# PI stop, the G-VER STOP, or the day the cap was reached -- as that unit's entry records it; where the
# unit's own output carries no date, the declarer supplies the entry's.
def _iso_date(d: Any) -> bool:
    if not (isinstance(d, str) and re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", d)):
        return False
    import datetime as _dt
    try:
        _dt.date.fromisoformat(d)
    except ValueError:
        return False
    return True


def not_run_reason(unit: str, code: str, date: str | None = None) -> str:
    """The reason phrase of a cause for a unit; ValueError where the cause is not the unit's."""
    base, param = parse_cause(code)
    spec = NOT_RUN_CAUSES[base]
    if spec["units"] == "olmo" and _sub(unit) != "olmo":
        raise ValueError(f"cause {code!r} applies to OLMo checkpoints only (m:324), not {unit}")
    _sub(unit)
    if base in PARAM_CAUSES and param not in gate_stop_stages(unit):
        raise ValueError(f"stage {param!r} is not a STOPping gate of {unit} ({gate_stop_stages(unit)})")
    if "{date}" in spec["phrase"]:
        if not _iso_date(date):
            raise ValueError(f"cause {code!r} needs its Clock date (YYYY-MM-DD), got {date!r}")
    return spec["phrase"].format(date=date, stage=param)


PENDING_SUBSTATES = ("unlocked-before-D_O", "locked-running", "restarting-after-box-change",
                     "awaiting-verdicts-session")


def pending_state(unit: str, decl: Mapping, *, verdicts_exists: bool, notrun_exists: bool) -> str:
    """A declared PENDING (m:324), validated for totality and exclusivity with NOT-RUN."""
    # PIN (Code, declared at LOCK v0.1): PIN-6 -- PENDING is a declared input {state, substate,
    # clock_passed, date}; it is refused for Q-F0 (v1 posts after Q-F0's VERDICTS or NOT-RUN, m:349,
    # m:347), refused for unlocked-before-D_O with clock_passed true (that unit is NOT-RUN by its
    # Clock), and refused where the unit's VERDICTS or NOT-RUN output exists. The Clock comparison
    # is the declared clock_passed beside the declared date it was made on (YYYY-MM-DD), both
    # recorded as given. The boundary-day comparison is settled by the seat (C7, 2026-10-10): a
    # unit's LOCK v1.0 is "committed by its Clock date" iff the commit's committer date, in UTC, falls
    # on or before the Clock date (the day inclusive, to 23:59:59 UTC); it remains a declared input,
    # so no date-vs-D_O consistency is imposed here.
    if unit == "Q-F0":
        raise ValueError("Q-F0 is never PENDING at a v1 posting (m:349, m:347)")
    _ckpt(unit)
    if not isinstance(decl, Mapping) or decl.get("state") != "PENDING":
        raise ValueError("a PENDING declaration is {state: PENDING, substate, clock_passed, date}")
    if sorted(decl) != ["clock_passed", "date", "state", "substate"]:
        raise ValueError(f"a PENDING declaration has exactly state, substate, clock_passed, date: "
                         f"{sorted(decl)}")
    sub = decl["substate"]
    if sub not in PENDING_SUBSTATES:
        raise ValueError(f"PENDING sub-state {sub!r} not in {PENDING_SUBSTATES}")
    if type(decl["clock_passed"]) is not bool:
        raise ValueError("clock_passed must be a bool (declared, recorded as given)")
    if not _iso_date(decl["date"]):
        raise ValueError(f"the Clock comparison's date must be YYYY-MM-DD (declared, recorded as given): "
                         f"{decl['date']!r}")
    if sub == "unlocked-before-D_O" and decl["clock_passed"]:
        raise ValueError("unlocked with D_O passed is NOT-RUN by its Clock, never PENDING (m:324)")
    if verdicts_exists or notrun_exists:
        raise ValueError(f"{unit} has a {'VERDICTS' if verdicts_exists else 'NOT-RUN'} output; PENDING "
                         f"is exclusive with both (m:324)")
    return sub


def validate_not_run_record(rec: Mapping, *, unit: str | None = None) -> dict:
    """A NOT-RUN record {schema, unit, cause, also, date, detail, decisions...} -> its parts."""
    want = ["also", "cause", "date", "decisions_with_other_outcomes_known", "detail", "schema", "unit"]
    if not isinstance(rec, Mapping) or sorted(rec) != want:
        raise ValueError(f"a NOT-RUN record has exactly {want}; got "
                         f"{sorted(rec) if isinstance(rec, Mapping) else type(rec).__name__}")
    if rec["schema"] != NOT_RUN_RECORD_SCHEMA:
        raise ValueError(f"NOT-RUN record schema {rec['schema']!r} != {NOT_RUN_RECORD_SCHEMA!r}")
    u = rec["unit"]
    if unit is not None and u != unit:
        raise ValueError(f"the record names {u!r}, the command {unit!r}")
    reason = not_run_reason(u, rec["cause"], rec["date"])
    if not _iso_date(rec["date"]):
        raise ValueError(f"a NOT-RUN record's date must be a real YYYY-MM-DD date: {rec['date']!r}")
    if not isinstance(rec["also"], list):
        raise ValueError("also must be a list of cause codes")
    for c in rec["also"]:
        not_run_reason(u, c, rec["date"])
    if not isinstance(rec["detail"], str):
        raise ValueError("detail must be a str")
    decisions = validate_decisions(rec["decisions_with_other_outcomes_known"], u)
    return {"unit": u, "cause": rec["cause"], "also": list(rec["also"]), "reason": reason,
            "date": rec["date"], "detail": rec["detail"], "decisions": decisions}


# PIN (Code, declared at LOCK v0.1): PIN-35 -- m:318's record of decisions taken with another unit's
# outcome known is a REQUIRED declared input (may be an empty list): the not-run record's key, and
# verdicts' --decisions file {schema m-decisions-v1, unit, decisions_with_other_outcomes_known};
# entries are {decision, date, other_unit, other_state}, carried verbatim into {U}_VERDICTS.json /
# {U}_NOT-RUN.json; a missing key is refused. other_unit is any OTHER unit of m:324 -- Q-F0, an OLMo
# checkpoint, or Q-F3 (an OLMo checkpoint PENDING at v1 may reach VERDICTS after Q-F3's, m:338,
# m:340, m:324, under this analyzer, PIN-14). other_state is the other unit's known outcome: for a
# built unit its §5 state word or NOT-RUN (Q5); for Q-F3 "NOT-RUN" or {A1, A2, A3[, A3*]} in m:326's
# and m:340's words. PENDING is refused: a PENDING unit has no VERDICTS (m:318, m:324).
OTHER_UNITS = UNITS + ("Q-F3",)
QF3_WORDS = {"A1": ("PASS", "REVERSE", "DEAD", "INDETERMINATE"),                       # m:326 controls
             "A2": ("PASS", "REVERSE", "FAIL", "INDETERMINATE"),                       # m:326 "FAIL for DEAD"
             "A3": ("NO-READ", "REVERSE", "POSITIVE", "NULL-x↑", "NULL-x↓", "NULL"),   # m:326 A3's order
             "A3*": ("NO-READ", "REVERSE", "POSITIVE", "NULL-x↑", "NULL-x↓", "NULL", "CONFIRMED",
                     "DISCORDANT", "UNLICENSED")}                                    # m:340 Step 4


def other_state_problem(other_unit: str, st: Any) -> str | None:
    """Why a decision's other_state is not a known outcome of other_unit (None = accepted)."""
    if other_unit == "Q-F3":
        if st == "NOT-RUN":
            return None
        if not (isinstance(st, Mapping) and {"A1", "A2", "A3"} <= set(st) <= set(QF3_WORDS)):
            return "Q-F3's other_state is 'NOT-RUN' or {A1, A2, A3[, A3*]} (m:326, m:340)"
        bad = [k for k, v in st.items() if v not in QF3_WORDS[k]]
        return f"Q-F3 {bad[0]} {st[bad[0]]!r} not in {QF3_WORDS[bad[0]]}" if bad else None
    if st == "PENDING":
        return "PENDING is no known outcome: a PENDING unit has no VERDICTS (m:318, m:324)"
    if st not in Q5:
        return f"other_state {st!r} not in {Q5}"
    return None


def validate_decisions(items: Any, unit: str) -> list[dict]:
    if not isinstance(items, list):
        raise ValueError("decisions_with_other_outcomes_known must be a list (empty when none)")
    out = []
    for d in items:
        if not isinstance(d, Mapping) or sorted(d) != ["date", "decision", "other_state", "other_unit"]:
            raise ValueError(f"a decision is {{decision, date, other_unit, other_state}}: {d!r}")
        if not (isinstance(d["decision"], str) and d["decision"].strip()):
            raise ValueError("a decision names what was decided (non-empty str)")
        if not _iso_date(d["date"]):
            raise ValueError(f"decision date must be YYYY-MM-DD: {d['date']!r}")
        if d["other_unit"] not in OTHER_UNITS or d["other_unit"] == unit:
            raise ValueError(f"other_unit must be another unit of m:324 {OTHER_UNITS}: {d['other_unit']!r}")
        why = other_state_problem(d["other_unit"], d["other_state"])
        if why:
            raise ValueError(why)
        out.append(copy.deepcopy(dict(d)))
    return out


def decisions_file(doc: Any, unit: str) -> list[dict]:
    if not isinstance(doc, Mapping) or doc.get("schema") != DECISIONS_SCHEMA or doc.get("unit") != unit:
        raise ValueError(f"the decisions input is {{schema {DECISIONS_SCHEMA}, unit {unit}, "
                         f"decisions_with_other_outcomes_known}}")
    if "decisions_with_other_outcomes_known" not in doc:
        raise ValueError("decisions_with_other_outcomes_known is required (m:318; may be empty)")
    if sorted(doc) != ["decisions_with_other_outcomes_known", "schema", "unit"]:
        raise ValueError(f"unexpected keys in the decisions input: {sorted(doc)}")
    return validate_decisions(doc["decisions_with_other_outcomes_known"], unit)


# --- unit composition (§5 m:324) -----------------------------------------------------------------
def unit_state(unit: str, ev: Mapping) -> tuple[str, Any]:
    """('NOT-RUN', {code, reason, also}) | ('ANALYZED', arm outcome) | ('PENDING', substate).

    ev kinds: {'kind': 'not-run', 'record': ...}; {'kind': 'pending', 'decl', 'verdicts_exists',
    'notrun_exists'}; {'kind': 'campaign', 'ended', 'stop_bar', 'pi_stop_record', 'counts'}."""
    _sub(unit)
    kind = ev.get("kind")
    if kind == "not-run":
        r = validate_not_run_record(ev["record"], unit=unit)
        return "NOT-RUN", {"code": r["cause"], "reason": r["reason"], "also": r["also"]}
    if kind == "pending":
        return "PENDING", pending_state(unit, ev["decl"], verdicts_exists=ev["verdicts_exists"],
                                        notrun_exists=ev["notrun_exists"])
    if kind != "campaign":
        raise ValueError(f"unknown evidence kind {kind!r}")
    ended, bar, c = ev["ended"], ev.get("stop_bar"), ev["counts"]
    if ended not in ("COMPLETE", "CAP", "PI-STOP", "STOP"):
        raise AnlRefusal(f"REFUSED: the campaign has not ended (status {ended!r}); VERDICTS waits for a "
                         f"terminal state (m:247)")
    if ended == "STOP":
        if bar in GVER_BARS:
            pass                                    # a PI stop by m:284
        elif bar == HAIR_BAR:
            if not ev.get("pi_stop_record"):
                raise AnlRefusal("REFUSED: the campaign ended on a scaffold_absorption hair-trigger "
                                 "STOP; it is analyzed only on a declared PI-stop record (--pi-stop; "
                                 "PIN-8, the seat's C2)")
        else:
            raise AnlRefusal(f"REFUSED: a campaign STOP on bar {bar!r} is neither G-VER nor a "
                             f"scaffold_absorption hair trigger")
    n = c["n0"] + c["n1"]
    if n + c["mS"] == 0:
        if ended == "COMPLETE":
            raise AnlStop("STOP: a COMPLETE campaign with no domain session in either arm -- "
                          "impossible at floors >= 1; a bookkeeping defect")
        code = {"CAP": "no-first-read:cap", "PI-STOP": "no-first-read:pi-stop"}.get(ended)
        if code is None:
            code = "no-first-read:gver-stop" if bar in GVER_BARS else "no-first-read:pi-stop"
        return "NOT-RUN", {"code": code, "reason": not_run_reason(unit, code), "also": []}
    return "ANALYZED", arm_outcome(c["n0"], c["k0"], c["n1"], c["k1"], c["mS"], c["j"])


def coordinate(state: tuple[str, Any]) -> str:
    """The tuple coordinate of a unit state: the state word (no-read collapses to INDETERMINATE)."""
    word, val = state
    if word == "ANALYZED":
        return val["state"]
    if word in ("NOT-RUN", "PENDING"):
        return word
    raise ValueError(f"unknown unit state {word!r}")


# --- records (V4) ---------------------------------------------------------------------------------
REASONING_MARK = "reasoning"


def _has_reasoning(rec: Mapping) -> bool:
    if any(REASONING_MARK in k for k in rec):
        return True
    for x in list(rec.get("rounds") or []) + list(rec.get("choices") or []):
        if isinstance(x, Mapping) and any(REASONING_MARK in k for k in x):
            return True
    return False


def record_problems(rec: Mapping, unit: str, stage: str) -> list[str]:
    """V4's per-record content assertions; any problem is a STOP (exit 4)."""
    # PIN (Code, declared at LOCK v0.1): PIN-34 -- a record whose domain disagrees with its forced
    # rounds (readrule._forced_domain), or whose first_free_pick_P disagrees with its first choice,
    # is a STOP, not a refusal; so are a cell whose P is not pair[map], a foreign substrate or
    # template, and reasoning-line material (Q-F0 and OLMo have none). (An unverified record is
    # already refused by resume.read_checkpoint at V2.)
    probs = []
    if rec.get("schema") != resume.SESSION_SCHEMA:
        return [f"schema {rec.get('schema')!r}"]
    if rec.get("substrate") != _sub(unit):
        probs.append(f"substrate {rec.get('substrate')!r} is not {unit}'s")
    if rec.get("unit") != unit or rec.get("stage") != stage:
        probs.append("unit/stage differ from the checkpoint's")
    if rec.get("template") not in keys.templates(unit):
        probs.append(f"template {rec.get('template')!r} is not {unit}'s")
    if rec.get("verified") is not True:
        probs.append("not a verified record")
    try:
        d = readrule._forced_domain(rec)
    except (ValueError, KeyError, TypeError) as e:
        return probs + [f"domain: {e}"]
    ch = rec.get("choices") or []
    cell = rec.get("cell") or {}
    if d:
        if not ch or rec.get("first_free_pick_P") is not (ch[0].get("pick") == cell.get("P")):
            probs.append("first_free_pick_P disagrees with the first choice")
    elif rec.get("first_free_pick_P") is not None:
        probs.append("first_free_pick_P set outside the domain")
    try:
        if cell["P"] != cell["pair"][cell["map"]] or cell["map"] not in (0, 1):
            probs.append("cell.P is not pair[map]")
    except (KeyError, IndexError, TypeError):
        probs.append("cell malformed")
    if _has_reasoning(rec):
        probs.append("reasoning-line material in a Q-F0 / OLMo record")
    return probs


def campaign_counts(records: Sequence[Mapping], unit: str) -> dict:
    """The arm and sham counts §5 reads, from campaign session records (domain per m:308)."""
    c, s = keys.templates(unit)
    con = [r for r in records if r["template"] == c]
    sh = [r for r in records if r["template"] == s]
    dc = [r for r in con if r["domain"]]
    ds = [r for r in sh if r["domain"]]
    n = {m: [r for r in dc if r["cell"]["map"] == m] for m in (0, 1)}
    return {"n0": len(n[0]), "k0": sum(bool(r["first_free_pick_P"]) for r in n[0]),
            "n1": len(n[1]), "k1": sum(bool(r["first_free_pick_P"]) for r in n[1]),
            "mS": len(ds), "j": sum(bool(r["first_free_pick_P"]) for r in ds),
            "launched": {c: len(con), s: len(sh)}, "domain": {c: len(dc), s: len(ds)},
            "sham_by_map": {str(m): {"n": sum(r["cell"]["map"] == m for r in ds),
                                     "j": sum(bool(r["first_free_pick_P"]) for r in ds
                                              if r["cell"]["map"] == m)} for m in (0, 1)}}


def _prepick(rec: Mapping) -> bool:
    # PIN (Code, declared at LOCK v0.1): PIN-33 -- stages._prepick's definition, cited (stages.py
    # _prepick): a session excluded at the forced phase (m:308); the battery asserts the two agree
    # on every record, both directions. The rate is that count over the arm's campaign session
    # records (launched), the guard's own denominator; a G-VER-quarantined record is reported
    # beside, not counted.
    exc = rec.get("exclusion")
    return bool(exc) and exc.get("phase") == "forced"


def prepick_counts(records: Sequence[Mapping], unit: str) -> dict:
    """Per arm, the campaign session records excluded at the forced phase (PIN-33's numerator)."""
    return {a: sum(_prepick(r) for r in records if r["template"] == a) for a in keys.templates(unit)}


def excluding_round(rec: Mapping) -> Mapping | None:
    """The round that set the session's exclusion (its first run-scope excluding round)."""
    exc = rec.get("exclusion")
    if not exc:
        return None
    for r in rec["rounds"]:
        ra = audit._ra(r["audit"])
        if ra.excludes("run"):
            if ra.claim != exc.get("class") or ra.phase != exc.get("phase"):
                raise AnlStop(f"STOP: a record's exclusion ({exc.get('class')}@{exc.get('phase')}) is not "
                              f"its first excluding round's ({ra.claim}@{ra.phase})")
            return r
    raise AnlStop("STOP: a record carries an exclusion and no excluding round")


# --- counters (m:278 (iii); m:314; PIN-11, PIN-12) ------------------------------------------------
SCOPE_ALL = "all campaign sessions, excluded included"


@dataclass(frozen=True)
class CounterDecl:
    name: str
    spec_name: str                  # m:314's text, verbatim and in m:314's order
    unit: str                       # round | read | session | line
    numerator: str
    denominator: str
    keys_verdicts: tuple[str, ...]
    scope: str = SCOPE_ALL
    q_f3_only: bool = False

    def as_dict(self) -> dict:
        return {"name": self.name, "spec_name": self.spec_name, "unit": self.unit,
                "numerator": self.numerator, "denominator": self.denominator,
                "keys_verdicts": list(self.keys_verdicts), "scope": self.scope,
                "q_f3_only": self.q_f3_only}


_R = "rounds generated"
_K_RP = ("arm", "phase", "property")
# PIN (Code, declared at LOCK v0.1): PIN-11 -- the counters are m:314's two lists in full, in its
# order, each with its record fields, unit, denominator and VERDICTS keys; the [Q-F3] counter is
# declared, scoped to Q-F3 and not tabulated at Q-F0. Tabulation mirrors audit.tally's claim logic
# exactly (each v5 advisory entry counted once, as tally counts it) with the property axis added.
COUNTERS: dict[str, tuple[CounterDecl, ...]] = {
    "qwen": (
        CounterDecl("cap_hit", "cap_hit", "round", "round.cap_hit", _R, _K_RP),
        CounterDecl("audit_degenerate", "audit_degenerate (v2)", "round", "audit.claim == 'v2'", _R,
                    ("arm", "phase", "category", "property")),
        CounterDecl("harness_echo", "harness_echo", "round", "audit.claim == 'echo'", _R, _K_RP),
        CounterDecl("content_exclusion", "content_exclusion (v3/v4)", "round",
                    "audit.claim == 'content'", _R, ("arm", "phase", "class", "property")),
        CounterDecl("content_advisory", "content_advisory (v5)", "round",
                    "each entry of audit.advisory (v5 advisory classes)", _R,
                    ("arm", "phase", "class", "property")),
        CounterDecl("lexical", "lexical", "round", "audit.claim == 'lexical'", _R, _K_RP),
        CounterDecl("post_choice_degeneracy", "post_choice_degeneracy", "round",
                    "free round with audit.claim in {v2, echo, content} (audit.tally's PIN)",
                    "free rounds generated", ("arm", "claim", "property")),
        CounterDecl("low_label_mass", "low_label_mass", "read", "choice.low_label_mass",
                    "reads taken", ("arm", "read position")),
        CounterDecl("top1_not_label", "top1_not_label", "read", "choice.top1_not_label",
                    "reads taken", ("arm", "read position")),
        CounterDecl("termination", "termination", "round",
                    "round.termination (f's patterns, raw; not a claim)", _R, _K_RP),
        CounterDecl("reasoning_line_defect", "reasoning-line defects by class [Q-F3]", "line",
                    "not tabulated at Q-F0: Q-F3's runner and scorer (G-ANL-F3, step 19)",
                    "reasoning lines generated", (), q_f3_only=True),
        CounterDecl("pre_pick_exclusion", "pre-pick exclusions", "session",
                    "exclusion.phase == 'forced'", "sessions launched",
                    ("arm", "property of the excluding forced round")),
    ),
    "olmo": (
        CounterDecl("cap_hit", "cap_hit", "round", "round.cap_hit", _R, _K_RP),
        CounterDecl("audit_degenerate", "audit_degenerate (b3's `AuditSpec`)", "round",
                    "audit.claim == 'audit'", _R, ("arm", "phase", "category", "property")),
        CounterDecl("harness_echo", "harness_echo", "round", "audit.claim == 'echo'", _R, _K_RP),
        CounterDecl("lexical", "lexical", "round", "audit.claim == 'lexical'", _R, _K_RP),
        CounterDecl("low_label_mass", "low_label_mass", "read", "choice.low_label_mass",
                    "reads taken", ("arm", "read position")),
        CounterDecl("top1_not_label", "top1_not_label", "read", "choice.top1_not_label",
                    "reads taken", ("arm", "read position")),
        CounterDecl("termination", "termination", "round",
                    "round.termination (f's patterns, raw; not a claim)", _R, _K_RP),
        CounterDecl("pre_pick_exclusion", "pre-pick exclusions", "session",
                    "exclusion.phase == 'forced'", "sessions launched",
                    ("arm", "property of the excluding forced round")),
    ),
}


def tabulated_names(sub: str) -> tuple[str, ...]:
    return tuple(d.name for d in COUNTERS[sub] if not d.q_f3_only)


def m314_counter_text() -> str:
    """The m:314 span the declaration must reproduce verbatim (asserted against the proposal)."""
    q = ", ".join(d.spec_name for d in COUNTERS["qwen"])
    o = ", ".join(d.spec_name for d in COUNTERS["olmo"])
    return f"per substrate:** Qwen — {q}; OLMo — {o}. Denominators = units generated."


def tabulate(records: Sequence[Mapping], sub: str) -> tuple[_session.DescriptiveCounters, dict]:
    """The rule-23 counters over ALL the records (excluded included), keyed by property (VERDICTS
    form, PIN-12), through session.DescriptiveCounters (an undeclared name raises), with the
    denominators beside."""
    dc = _session.DescriptiveCounters(declared=tabulated_names(sub))
    den = {"rounds": {}, "free_rounds": {}, "reads": {}, "sessions": {}}

    def bump(d: dict, key: str) -> None:
        d[key] = d.get(key, 0) + 1
    for rec in records:
        if rec["substrate"] != sub:
            raise AnlStop(f"STOP: a {rec['substrate']} record among {sub} records")
        if _has_reasoning(rec):
            raise AnlStop("STOP: reasoning-line material in a Q-F0 / OLMo record (Q-F3's counter is "
                          "not tabulated here)")
        tpl = str(rec["template"])
        ex = bool(rec["excluded"])
        dc.n_sessions += 1
        bump(den["sessions"], tpl)
        for r in rec["rounds"]:
            ra = audit._ra(r["audit"])
            ph, prop = ra.phase, str(r["property"])
            bump(den["rounds"], f"{tpl}|{ph}|{prop}")
            if ph == "free":
                bump(den["free_rounds"], f"{tpl}|{prop}")
            if ra.claim in ("v2", "audit"):
                dc.note("audit_degenerate", tpl, ph, audit._category(ra.detail), prop, excluded=ex)
            elif ra.claim == "echo":
                dc.note("harness_echo", tpl, ph, prop, excluded=ex)
            elif ra.claim == "content":
                dc.note("content_exclusion", tpl, ph, ra.detail.split(":", 1)[1], prop, excluded=ex)
            elif ra.claim == "lexical":
                dc.note("lexical", tpl, ph, prop, excluded=ex)
            if sub == "qwen":
                for a in ra.advisory:
                    dc.note("content_advisory", tpl, ph, a.split(":", 1)[1], prop, excluded=ex)
                if ph == "free" and ra.claim in ("v2", "echo", "content"):
                    dc.note("post_choice_degeneracy", tpl, ra.claim, prop, excluded=ex)
            if r.get("cap_hit"):
                dc.note("cap_hit", tpl, ph, prop, excluded=ex)
            if r.get("termination"):
                dc.note("termination", tpl, ph, prop, excluded=ex)
        for i, c in enumerate(rec.get("choices") or ()):
            pos = i + 1
            bump(den["reads"], f"{tpl}|{pos}")
            if c.get("low_label_mass"):
                dc.note("low_label_mass", tpl, pos, excluded=ex)
            if c.get("top1_not_label"):
                dc.note("top1_not_label", tpl, pos, excluded=ex)
        exc = rec.get("exclusion")
        if ex and exc and exc.get("phase") == "forced":
            xr = excluding_round(rec)
            dc.note("pre_pick_exclusion", tpl, str(xr["property"]), excluded=ex)
    return dc, den


# Which key position carries property / read position (collapsed to compare with audit.tally).
_COLLAPSE = {"cap_hit": 2, "audit_degenerate": 3, "harness_echo": 2, "content_exclusion": 3,
             "content_advisory": 3, "lexical": 2, "post_choice_degeneracy": 2, "low_label_mass": 1,
             "top1_not_label": 1, "termination": 2, "pre_pick_exclusion": 1}


def collapse_to_tally(dc: _session.DescriptiveCounters) -> dict:
    """The VERDICTS counters summed over property (and read position): audit.tally's keys."""
    out: dict = {}
    for k_, v in dc.counts.items():
        name, key = k_[0], list(k_[1:])
        del key[_COLLAPSE[name]]
        kk = (name, *key)
        out[kk] = out.get(kk, 0) + v
    return out


def counters_json(dc: _session.DescriptiveCounters, den: Mapping, sub: str) -> dict:
    rep = dc.report()
    return {"declared": [d.as_dict() for d in COUNTERS[sub]], "scope": SCOPE_ALL,
            "n_sessions": rep["n_sessions"], "tabulated_over_excluded_too": True,
            "n_excluded_included": dc.n_excluded_included,
            "counters": rep["counters"], "denominators": den,
            "not_tabulated": [d.name for d in COUNTERS[sub] if d.q_f3_only]}


PER_PROPERTY_REFERENCE = ("f1 CORR's 7-vs-1 anomaly (archive:91-93) is the reference (m:314); the column it "
                          "refers to is sessions_excluded_prepick, m's pre-pick column (sessions excluded "
                          "before the first read, by property; the seat's C7 on G-PORT A5, 2026-10-10); "
                          "sessions_excluded_any_phase is reported beside it")


def per_property_table(records: Sequence[Mapping], unit: str) -> dict:
    """m:314's per-property exclusion table, per arm x property (clean, corrupted)."""
    # PIN (Code, declared at LOCK v0.1): PIN-12 -- round columns key on round.property; the session
    # columns key on the property of the round that set the session's exclusion. Settled by the seat
    # (C7, 2026-10-10; G-PORT A5), where the interim text had named sessions_excluded_any_phase the
    # like-for-like column: f1's 7-vs-1 refers to the pre-pick column
    # (sessions_excluded_prepick, sessions excluded before the first read, by property);
    # sessions_excluded_any_phase is reported beside it -- fixed, no longer interim. The sham's
    # corrupted column is asserted zero.
    sub = _sub(unit)
    classes = audit.QWEN_CLAIMS if sub == "qwen" else audit.OLMO_CLAIMS
    tab: dict = {}
    for arm in keys.templates(unit):
        tab[arm] = {p: {"rounds_generated": 0, "rounds_claimed_by_class": {c: 0 for c in classes},
                        "rounds_excluding_by_class": {c: 0 for c in classes},
                        "sessions_excluded_prepick": 0, "sessions_excluded_any_phase": 0}
                    for p in ("clean", "corrupted")}
    for rec in records:
        t = tab[rec["template"]]
        for r in rec["rounds"]:
            row = t[r["property"]]
            row["rounds_generated"] += 1
            cl = (r["audit"] or {}).get("claim")
            if cl is not None:
                row["rounds_claimed_by_class"][cl] += 1
        xr = excluding_round(rec)
        if xr is not None:
            row = t[xr["property"]]
            row["rounds_excluding_by_class"][xr["audit"]["claim"]] += 1
            row["sessions_excluded_any_phase"] += 1
            if _prepick(rec):
                row["sessions_excluded_prepick"] += 1
    sham = keys.templates(unit)[1]
    if tab[sham]["corrupted"]["rounds_generated"]:
        raise AnlStop("STOP: the sham arm carries corrupted rounds (scaffold.py: sham rounds are clean)")
    return {"by_arm": tab, "reference": PER_PROPERTY_REFERENCE}


def beside_blocks(records: Sequence[Mapping], unit: str) -> dict:
    """Reported beside, not rule-23 counters (m:261, m:262, m:271, m:308, m:316, m:330)."""
    sub = _sub(unit)
    out: dict = {}
    for arm in keys.templates(unit):
        g = [r for r in records if r["template"] == arm]
        deg = {}
        for ph in ("forced", "free"):
            rs = [x for r in g for x in r["rounds"] if x["phase"] == ph]
            deg[ph] = {"num": sum((x["audit"] or {}).get("claim") in bars.DEGEN_CLAIMS[sub] for x in rs),
                       "den": len(rs), "domain": f"{arm} {ph} rounds generated (contrast free rounds "
                                                 f"released at VERDICTS)"}
        lenient = [r for r in g if r["complete"] and r["exclusion"] is None and not r["hair_triggers"]]
        strict = [r for r in lenient if r.get("strict_exclusion") is None]
        hair = {ph: sum(any(h.get("name") == HAIR_BAR and h.get("phase") == ph for h in r["hair_triggers"])
                        for r in g) for ph in ("forced", "free")}
        allr = [c for r in g for c in (r.get("choices") or [])]
        first = [r["choices"][0] for r in g if r["domain"] and r.get("choices")]
        out[arm] = {
            "round_degeneracy": deg,
            # PIN (Code, declared at LOCK v0.1): PIN-12 -- whole-session validity (m:308 "reported
            # beside"): lenient = complete, no exclusion, no hair trigger; strict additionally no
            # claim in any round (strict_exclusion None); on OLMo strict = lenient by b3's rule.
            "whole_session_validity": {"launched": len(g), "valid_lenient": len(lenient),
                                       "valid_strict": len(strict)},
            "scaffold_absorption_sessions": hair,
            "read_flags": {"all_reads": {"reads": len(allr),
                                         "low_label_mass": sum(bool(c.get("low_label_mass")) for c in allr),
                                         "top1_not_label": sum(bool(c.get("top1_not_label")) for c in allr)},
                           "first_reads_of_domain_sessions": {
                               "reads": len(first),
                               "low_label_mass": sum(bool(c.get("low_label_mass")) for c in first),
                               "top1_not_label": sum(bool(c.get("top1_not_label")) for c in first)}},
            "prepick_pooled": {"num": sum(_prepick(r) for r in g), "den": len(g),
                               "domain": f"{arm} campaign sessions launched"},
        }
    return out


# --- the guard at the last look (PIN-10) ---------------------------------------------------------
def bar_set(unit: str) -> tuple:
    return bars.QF0_BARS if unit == "Q-F0" else bars.OLMO_BARS(_ckpt(unit))


def _guard_bars(unit: str):
    bs = bar_set(unit)
    return (next(b for b in bs if b.kind == "guard_fisher"), next(b for b in bs if b.kind == "guard_abs"))


def _guard_pair(look: Mapping, unit: str) -> dict:
    fis, ab = _guard_bars(unit)
    res = {r["name"]: r for r in look["results"]}
    f, a = res[fis.name], res[ab.name]
    return {"fisher": {"name": fis.name, "p": f["p"], "fired": bool(f["fired"]), "binding": True},
            "abs": {"name": ab.name, "p": a["p"], "fired": bool(a["fired"]), "exceeds": bool(a["exceeds"]),
                    "binding": bool(ab.binding)}}


def guard_at_last_look(ck: Mapping, unit: str, ended: str) -> dict:
    """'The unit's last look' (m:326) and its guard results; nothing recomputed (PIN-10)."""
    # PIN (Code, declared at LOCK v0.1): PIN-10 -- the seat's C9(ii) (2026-10-10; m:330's "at the end"
    # includes an end by STOP): the last look is campaign.end_look whenever present -- stages evaluates
    # and records it at COMPLETE, CAP, PI-STOP and at the STOP point alike -- and the sentence names it,
    # at a STOP as the STOP's ("the end look at the STOP (at N launches)", or "look k at N launches, the
    # end look at the STOP" where the end look is the cadence look recorded at N). A STOP-ended campaign
    # with a launch recorded and no end look is refused at V2 (run_verdicts), so the cadence fallback
    # below serves no VERDICTS run; with no launch recorded there is no look ('no look reached'). No
    # end-of-data guard is recomputed here; neither result moves a verdict (m:316).
    camp = ck.get("campaign") or {}
    el = camp.get("end_look")
    at_stop = ended == "STOP"
    if el:
        at = el["at_launches"]
        if at_stop:
            label = (f"look {el['end_is_look']} at {at} launches, the end look at the STOP" if "end_is_look" in el
                     else f"the end look at the STOP (at {at} launches)")
        else:
            label = (f"look {el['end_is_look']} at {at} launches, the end look" if "end_is_look" in el
                     else f"the end look at {at} launches")
        return {"reached": True, "label": label, "source": "end_look", "at_stop": at_stop,
                **_guard_pair(el, unit)}
    if ck.get("looks"):
        lk = ck["looks"][-1]["result"]
        return {"reached": True, "source": "cadence",
                "label": f"look {lk['look']} at {lk['at_launches']} launches, the last cadence look",
                "at_stop": at_stop, **_guard_pair(lk, unit)}
    return {"reached": False, "label": "no look reached", "source": None, "at_stop": at_stop}


def every_look(ck: Mapping, unit: str) -> list[dict]:
    out = []
    for lk in ck.get("looks") or []:
        r = lk["result"]
        out.append({"look": r["look"], "at_launches": r["at_launches"], "fired": bool(r["fired"]),
                    **_guard_pair(r, unit)})
    el = (ck.get("campaign") or {}).get("end_look")
    if el:
        out.append({"look": "end", "at_launches": el["at_launches"], "fired": bool(el["fired"]),
                    **_guard_pair(el, unit)})
    return out


# --- the verdict sentence (PIN-4) ----------------------------------------------------------------
# PIN (Code, declared at LOCK v0.1): PIN-4 -- the verdict sentence is these clauses, joined by "; "
# and ended with ".", in this order, built only from the clauses m:326, m:247, m:190 and m:316
# mandate: the state (or 'no read obtained' with its sub-reason); counts per map; P, Δ_c and its
# CP CI (omitted when n = 0); E and P_arm − P_sham (omitted when m_S = 0); both one-sided p's at
# α .01 (omitted when n = 0); REVERSE's phrase; the pre-pick exclusion rates; the guard at the
# unit's last look (Fisher binding; the absolute bar binding on Qwen, reported only on OLMo);
# shortfall and attained power only when an arm is below its floor (m:247). Attained power is in
# the VERDICTS output always (m:190).
SENTENCE_TEMPLATES = {
    "head": "{arm} ({unit}): {state}",
    "noread": "{arm} ({unit}): INDETERMINATE, no read obtained ({why})",
    "noread_contrast": "the arm has no domain session",
    "noread_sham": "its sham {sham} has no domain session, so E is undefined",
    "counts": "n = {n} domain sessions of {launched} launched (map 0: {k0}/{n0}, map 1: {k1}/{n1} on the "
              "clean-role label)",
    "P": "P = {k}/{n} = {P}; Δ_c = {delta}, two-sided Clopper–Pearson 95% CI [{lo}, {hi}]",
    "E": "E = {E} from {sham} ({j}/{mS} domain sessions, P_sham = {PS}); P_arm − P_sham = {diff}",
    "tests": "exact one-sided binomial vs 0.5: p = {pu} toward clean, p = {pd} toward corrupted, α = .01",
    "reverse": "instruction inversion; reported; not-PASS for licensing",
    "prepick": "pre-pick exclusion rate {a}/{A} = {r} beside {sham}'s {b}/{B} = {rs}",
    "guard": "the guard at the unit's last look ({label}): Fisher one-sided vs {sham} p = {pf}, {ff} "
             "(binding); absolute vs .20 p = {pa}, {fa} ({ab})",
    "noguard": "the guard at the unit's last look: no look reached",
    "floor": "below floor: {arm} {n}/{fc}, shortfall {x}; {sham} {mS}/{fsh}, shortfall {y}; attained "
             "power {pw} at the realised n (m:190's base case: n/2 per map at P = .70, the sham "
             "pooled at .5, α .01); {pwr} at the realised map split",
}


def _rate_text(a: int, A: int) -> str:
    return dec(Fraction(a, A)) if A else "undefined (no session launched)"


def verdict_sentence(unit: str, out: Mapping, counts: Mapping, guard: Mapping, floors: Mapping,
                     power: Mapping) -> str:
    T = SENTENCE_TEMPLATES
    arm, sham = keys.templates(unit)
    st = out["stats"]
    parts = []
    if out["noread"]:
        why = T["noread_contrast"] if out["noread"] == "contrast-empty" else T["noread_sham"].format(sham=sham)
        parts.append(T["noread"].format(arm=arm, unit=unit, why=why))
    else:
        parts.append(T["head"].format(arm=arm, unit=unit, state=out["state"]))
    parts.append(T["counts"].format(n=st["n"], launched=counts["launched"][arm], k0=st["k0"], n0=st["n0"],
                                    k1=st["k1"], n1=st["n1"]))
    if st["n"]:
        lo, hi = cp_interval(st["k"], st["n"])
        parts.append(T["P"].format(k=st["k"], n=st["n"], P=dec(st["P"]), delta=sdec(st["delta"]),
                                   lo=sdec(lo - HALF), hi=sdec(hi - HALF)))
    if st["mS"]:
        diff = sdec(st["P"] - st["PS"]) if st["n"] else "undefined (no arm domain session)"
        parts.append(T["E"].format(E=dec(st["E"]), sham=sham, j=st["j"], mS=st["mS"], PS=dec(st["PS"]),
                                   diff=diff))
    if st["n"]:
        parts.append(T["tests"].format(pu=dec(st["p_up"]), pd=dec(st["p_down"])))
    if out["state"] == "REVERSE":
        parts.append(T["reverse"])
    a, A = counts["prepick"][arm], counts["launched"][arm]
    b, B = counts["prepick"][sham], counts["launched"][sham]
    parts.append(T["prepick"].format(a=a, A=A, r=_rate_text(a, A), sham=sham, b=b, B=B, rs=_rate_text(b, B)))
    if guard["reached"]:
        f, ab = guard["fisher"], guard["abs"]
        fa = (("fired" if ab["fired"] else "not fired") if ab["binding"]
              else ("P ≤ α" if ab["exceeds"] else "P > α"))
        parts.append(T["guard"].format(label=guard["label"], sham=sham, pf=dec(Fraction(f["p"])),
                                       ff="fired" if f["fired"] else "not fired", pa=dec(Fraction(ab["p"])),
                                       fa=fa, ab="binding" if ab["binding"] else "reported only"))
    else:
        parts.append(T["noguard"])
    fc, fsh = floors[arm], floors[sham]
    if st["n"] < fc or st["mS"] < fsh:
        parts.append(T["floor"].format(arm=arm, n=st["n"], fc=fc, x=max(0, fc - st["n"]), sham=sham,
                                       mS=st["mS"], fsh=fsh, y=max(0, fsh - st["mS"]),
                                       pw=power["of_record"]["display"],
                                       pwr=power["realised_split"]["display"]))
    return "; ".join(parts) + "."


# --- secondaries (m:312; PIN-13) -----------------------------------------------------------------
F1_CROSSING = ("its comparison with f1 at positions 5–6 crosses f1's 512-token read tail (§2.7 (12)), "
               "stated beside")


def rate(num: int, den: int, domain: str, floor: int = FLOOR_EVENTS) -> dict:
    """{num, den, domain} with the share; a CP 95% interval at or above the floor, a count below it."""
    d = {"num": num, "den": den, "domain": domain, "floor": floor, "count_only": den < floor,
         "share": fs(Fraction(num, den)) if den else None,
         "share_display": dec(Fraction(num, den)) if den else None, "interval": None}
    if den >= floor:
        lo, hi = cp_interval(num, den)
        d["interval"] = [dec(lo), dec(hi)]
    return d


def valid_through(rec: Mapping, p: int) -> bool:
    """'Valid through position p' (m:308; PIN-13): the choice at position p (1-based) was made and no
    exclusion-bearing event preceded it."""
    ch = rec.get("choices") or []
    if p > len(ch):
        return False
    xr = excluding_round(rec)
    if xr is None:
        return True
    return xr["phase"] == "free" and xr["ci"] + 1 >= p


def _frac_or_none(a: int, b: int) -> str | None:
    return fs(Fraction(a, b)) if b else None


def habit_identity(sessions: Sequence[Mapping]) -> dict:
    """e2d/habit.py's within-arm identity (m:312), on the arm's domain sessions."""
    # PIN (Code, declared at LOCK v0.1): PIN-13 -- habit.break_rates(<the arm's domain sessions>)
    # (no `arm` key; frame() and its e2d powered-effect block are not used); b+, bs and the weighted
    # form are recomputed in Fractions from break_rates' integer counts (an empty bucket contributes
    # 0 and its rate is None; break_rates' floats are not carried); the weighted form + 1/2 must
    # equal the arm's P exactly.
    br = habit.break_rates(sessions)
    bp, bs = br["b_plus"], br["b_sham"]
    N = bp["n"] + bs["n"]
    weighted = None
    if N:
        weighted = (Fraction(bp["n"], N) * (Fraction(bp["breaks"], bp["n"]) if bp["n"] else 0)
                    + Fraction(bs["n"], N) * (1 - Fraction(bs["breaks"], bs["n"]) if bs["n"] else 0)
                    - HALF)
    P = Fraction(sum(bool(s["first_free_pick_P"]) for s in sessions), len(sessions)) if sessions else None
    return {"b_plus": {"breaks": bp["breaks"], "n": bp["n"], "rate": _frac_or_none(bp["breaks"], bp["n"])},
            "b_sham": {"breaks": bs["breaks"], "n": bs["n"], "rate": _frac_or_none(bs["breaks"], bs["n"])},
            "n_undecidable": br["n_undecidable"],
            "forced_end_balance": {"pos": bp["n"], "neg": bs["n"], "exactly_balanced": bp["n"] == bs["n"]},
            "delta_first_weighted_form": None if weighted is None else fs(weighted),
            "delta_first_weighted_display": None if weighted is None else sdec(weighted),
            "delta_c": None if P is None else fs(P - HALF),
            "identity_holds": (weighted is not None and P is not None and weighted + HALF == P),
            "identity": br["identity"]}


def secondaries(records: Sequence[Mapping], unit: str) -> dict:
    _sub(unit)
    c_arm, s_arm = keys.templates(unit)
    out: dict = {"schema": SECONDARY_SCHEMA, "unit": unit, "claim": "none -- secondary DVs issue no claim "
                 "(m:358)", "floor_events": FLOOR_EVENTS, "a": {}, "b": {}, "d": {}, "e": {},
                 "not_built": "(c) and (f) are [Q-F3] (G-ANL-F3)", "f1_crossing_note": F1_CROSSING}
    for arm in (c_arm, s_arm):
        g = [r for r in records if r["template"] == arm]
        # (a) clean-label share by position
        out["a"][arm] = {str(p): rate(sum(r["choices"][p - 1]["picked_role"] == "P" for r in g
                                          if valid_through(r, p)),
                                      sum(valid_through(r, p) for r in g),
                                      f"{arm} sessions valid through position {p}")
                         for p in range(1, 7)}
        # (d) per-pair first-pick shares pooled over maps, and per pair x start order
        dom = [r for r in g if r["domain"]]
        pairs = sorted({r["cell"]["pair_index"] for r in dom})
        out["d"][arm] = {"per_pair": {str(pi): rate(sum(bool(r["first_free_pick_P"]) for r in dom
                                                        if r["cell"]["pair_index"] == pi),
                                                    sum(r["cell"]["pair_index"] == pi for r in dom),
                                                    f"{arm} domain sessions of pair {pi}, pooled over maps")
                                      for pi in pairs},
                         "per_pair_start": {f"{pi}|{st}": rate(
                             sum(bool(r["first_free_pick_P"]) for r in dom
                                 if r["cell"]["pair_index"] == pi and r["cell"]["start"] == st),
                             sum(r["cell"]["pair_index"] == pi and r["cell"]["start"] == st for r in dom),
                             f"{arm} domain sessions of pair {pi}, start order {st}")
                             for pi in pairs for st in (0, 1)},
                         "habit": habit_identity(dom)}
        # (e) termination attempts per round
        out["e"][arm] = {ph: rate(sum(bool(x.get("termination")) for r in g for x in r["rounds"]
                                      if x["phase"] == ph),
                                  sum(x["phase"] == ph for r in g for x in r["rounds"]),
                                  f"{arm} {ph} rounds generated")
                         for ph in ("forced", "free")}
    # (b) lose-shift, contrast arm only (a sham session has no corrupted round, m:312)
    ev = {"corrupted": [0, 0], "clean": [0, 0]}
    for r in (x for x in records if x["template"] == c_arm):
        for p in range(1, 6):
            if not valid_through(r, p + 1):
                continue
            prev = [x for x in r["rounds"] if x["phase"] == "free" and x["ci"] == p - 1]
            if len(prev) != 1:
                raise AnlStop("STOP: a session valid through a choice lacks its previous chosen round")
            switch = r["choices"][p]["pick"] != r["choices"][p - 1]["pick"]
            e = ev[prev[0]["property"]]
            e[0] += int(switch)
            e[1] += 1
    out["b"][c_arm] = {cond: rate(v[0], v[1], f"{c_arm} transitions after a chosen {cond} round by "
                                              f"sessions valid through the next choice")
                       for cond, v in ev.items()}
    out["b"]["scope"] = "contrast arm only (m:312)"
    return out


# --- §7 v1 outputs (PIN-15..PIN-23, PIN-27) --------------------------------------------------------
ROWS = ("e2a", "f1", "e2b", "olmo-base", "olmo-sft", "olmo-dpo", "olmo-instruct")
CELLS = ("e2a", "f1", "e2b", "weight", "S1", "olmo-base", "olmo-sft", "olmo-dpo", "olmo-instruct")
ANSWERED = "Answered"
LABEL_S1 = "Answered, as recognition"
LABEL_WEIGHT = "concluded, not answered"
ANSWERED_SET = (ANSWERED, LABEL_S1)
PFX_F0 = "concluded, not answered — the told control at F0 on this substrate "
PFX_O = "concluded, not answered — the told control at this stage "
TEMPLATE_F0 = PFX_F0 + "[did not pass: outcome | was not run: reason]"
TEMPLATE_O = PFX_O + "[did not pass: outcome | was not run: reason | is pre-registered and pending at this posting]"
LABEL_E2B = ("concluded, not answered — no told control at a state-present read; leakage certification "
             "π̂_d = 0.0172, exact 95% CI [0.0086, 0.0305], against the 0.0735 bar reported beside")
LABEL_BASE = "concluded, not answered — told control not run at base, by decision (7′)"
ABSTRACT_ALL = "and not at the SFT, DPO or instruct stage of the OLMo lineage"
ABSTRACT_SOME = "and, on the OLMo lineage, not at the [passing stages]"
ABSTRACT_NONE = "; the OLMo lineage's post-training nulls are reported as concluded, not answered (§5.5)"
TITLES = {"Main": "Functional for the Character, Not for the Network",
          "Fallback-1": "Marked, expressed, remembered, not acted on",
          "Fallback-2": "Marked, expressed, remembered"}
S81_TOKEN = {"PASS": "PASS", "DEAD": "DEAD", "REVERSE": "REVERSE", "INDETERMINATE": "INDETERMINATE",
             "NOT-RUN": "not run", "PENDING": "pending"}
S81_CONTROLS = (("A0 (Q-F0)", "Q-F0"), ("A0-OLMo-sft", "OLMo-sft"), ("A0-OLMo-dpo", "OLMo-dpo"),
                ("A0-OLMo-instruct", "OLMo-instruct"))
RANK = {"main": 3, "fallback-1": 2, "fallback-2": 1}
CEIL_RANK = {"Main": 3, "Fallback-1": 2, "Fallback-2": 1}
TREAT = {"a": "assert no null on these cells", "b": "state as a reading proposed, not a result",
         "strike": "strike the dose note", "carry": "carry the dose note"}


def check_tuple(t: Sequence[str]) -> tuple[str, str, str, str]:
    """t = (Q-F0, OLMo-sft, OLMo-dpo, OLMo-instruct) (PIN-23: an explicit input; base has none)."""
    if len(t) != 4 or t[0] not in Q5 or any(x not in O6 for x in t[1:]):
        raise ValueError(f"a v1 tuple is (q in {Q5}, s, d, i in {O6}); got {tuple(t)!r}")
    return tuple(t)  # type: ignore[return-value]


def licensing(t) -> dict:
    """Step 1 (m:337): L0 := (A0 = PASS); L0-OLMo-c := (A0-OLMo-c = PASS); L1 is [v2]."""
    q, s, d, i = check_tuple(t)
    return {"L0": q == "PASS", "L0-OLMo-sft": s == "PASS", "L0-OLMo-dpo": d == "PASS",
            "L0-OLMo-instruct": i == "PASS"}


def _reason_of(unit: str, reasons: Mapping) -> str:
    r = reasons.get(unit)
    if not (isinstance(r, str) and r.strip()):
        raise ValueError(f"{unit} is NOT-RUN with no reason recorded (m:324)")
    return r


def label_set(t, reasons: Mapping) -> dict:
    """Step 2's seven rows (m:338), plain text, one bracket alternative chosen."""
    # PIN (Code, declared at LOCK v0.1): PIN-15 -- the outcome slot takes the §5 state word, the
    # reason slot the PIN-5 phrase; one bracket alternative, plain text (no asterisks, no brackets).
    q, s, d, i = check_tuple(t)
    f0 = (ANSWERED if q == "PASS" else PFX_F0 + "did not pass: " + q if q != "NOT-RUN"
          else PFX_F0 + "was not run: " + _reason_of("Q-F0", reasons))
    out = {"e2a": f0, "f1": f0, "e2b": LABEL_E2B, "olmo-base": LABEL_BASE}
    for c, x in zip(keys.CKPTS, (s, d, i)):
        u = f"OLMo-{c}"
        out[f"olmo-{c}"] = (ANSWERED if x == "PASS" else PFX_O + "is pre-registered and pending at this posting"
                            if x == "PENDING" else PFX_O + "was not run: " + _reason_of(u, reasons)
                            if x == "NOT-RUN" else PFX_O + "did not pass: " + x)
    return {r: out[r] for r in ROWS}


def cell_labels(t, reasons: Mapping) -> dict:
    """Every cell of the posting rule's clause (a), S1 and the weight channel from m:14."""
    ls = label_set(t, reasons)
    return {"e2a": ls["e2a"], "f1": ls["f1"], "e2b": ls["e2b"], "weight": LABEL_WEIGHT, "S1": LABEL_S1,
            "olmo-base": ls["olmo-base"], "olmo-sft": ls["olmo-sft"], "olmo-dpo": ls["olmo-dpo"],
            "olmo-instruct": ls["olmo-instruct"]}


def ceiling(t) -> tuple[str, str]:
    """Step 5 at v1 (m:341): Main unreachable; Fallback-1 iff L0; Fallback-2 otherwise."""
    # PIN (Code, declared at LOCK v0.1): PIN-18 -- the ceiling output is its name and its m:334
    # title, verbatim.
    name = "Fallback-1" if licensing(t)["L0"] else "Fallback-2"
    return name, TITLES[name]


def abstract_clause(t) -> str:
    """Step 2's three-way abstract OLMo clause (m:338), verbatim."""
    # PIN (Code, declared at LOCK v0.1): PIN-16 -- '[passing stages]' renders 'the {A} stage' or 'the
    # {A} or {B} stage' in lineage order (SFT, DPO, instruct, as m:338 spells them).
    # PIN (Code, declared at LOCK v0.1): PIN-27 -- the clause is emitted verbatim even where its host
    # sentence is enumerated under (a); the entry notes that it can dangle.
    _, s, d, i = check_tuple(t)
    passing = [STAGE_WORD[c] for c, x in zip(keys.CKPTS, (s, d, i)) if x == "PASS"]
    if len(passing) == 3:
        return ABSTRACT_ALL
    if not passing:
        return ABSTRACT_NONE
    stages_ = f"the {passing[0]} stage" if len(passing) == 1 else f"the {passing[0]} or {passing[1]} stage"
    return ABSTRACT_SOME.replace("the [passing stages]", stages_)


def s81_text(t) -> str:
    """Step 7's §8.1 status text (m:343)."""
    # PIN (Code, declared at LOCK v0.1): PIN-17 -- confirmed by the seat (C4, 2026-10-10): one clause
    # per control with a v1 coordinate (A0, A0-OLMo-sft/-dpo/-instruct) with m:343's tokens; Q-F3's A1
    # belongs to §8.2, 'open' at v1; re-verified against the placed preprint at LOCK v1.0.
    tt = check_tuple(t)
    return "; ".join(f"{name}: {S81_TOKEN[x]}" for (name, _), x in zip(S81_CONTROLS, tt))


def step7(t) -> str:
    check_tuple(t)
    return "open"                                   # m:343: "open" at v1 by construction


def dose_note(flag: bool, table: Mapping) -> dict:
    """f1's CORR line dose note (m:338), invariant over the tuple."""
    if type(flag) is not bool:
        raise ValueError("the 0.12-artifact flag is a bool input")
    spans = [r["dose_note_span"] for r in table["rows"] if r["dose_note"]]
    if not flag:
        return {"status": "none (struck, §7.5(c))", "text": None}
    if not spans:
        return {"status": "to be carried; absent from the table (§7.5(c))", "text": None}
    return {"status": "carried", "text": " | ".join(spans)}


def enumeration(t, flag: bool, table: Mapping, reasons: Mapping) -> list[dict]:
    """The §7.5 enumeration under the tuple (m:349), over the declared table, in table order."""
    # PIN (Code, declared at LOCK v0.1): PIN-21 -- (a) fires iff a null cell's label is not Answered;
    # (b) iff the row's thesis ranks above the ceiling (main 3 > fallback-1 2 > fallback-2 1); (c)
    # is two-sided on m:349's own "iff": flag false strikes every dose-note row; flag true with no
    # dose-note row carries the note at the f1-corr-line row(s); flag true with a dose-note row
    # yields nothing. Rows with no clause are omitted; the PI rewrites each item at posting.
    # PIN (Code, declared at LOCK v0.1): PIN-22 -- S1 ('Answered, as recognition', m:14) counts as
    # Answered under clause (a); the weight channel, base and e2b fire in every tuple (m:349).
    labels = cell_labels(t, reasons)
    cname, _ = ceiling(t)
    has_dose = any(r["dose_note"] for r in table["rows"])
    items = []
    for r in table["rows"]:
        clauses, a, b, c = [], None, None, None
        bad = [x for x in r["null_cells"] if labels[x] not in ANSWERED_SET]
        if bad:
            clauses.append("a")
            a = {"cells": [{"cell": x, "label": labels[x]} for x in bad]}
        if r["thesis"] is not None and RANK[r["thesis"]] > CEIL_RANK[cname]:
            clauses.append("b")
            b = {"thesis": r["thesis"], "ceiling": cname}
        if not flag and r["dose_note"]:
            c = {"flag": False, "treatment": "strike"}
        elif flag and not has_dose and "f1-corr-line" in r["kinds"]:
            c = {"flag": True, "treatment": "carry"}
        if c is not None:
            clauses.append("c")
        if clauses:
            items.append({"row_id": r["id"], "loc": dict(r["loc"]), "clauses": clauses, "a": a, "b": b, "c": c,
                          "treatments": [TREAT[x] if x != "c" else TREAT[c["treatment"]] for x in clauses]})
    return items


def v1_outputs(t, reasons: Mapping, flag: bool, table: Mapping) -> dict:
    """§7's v1 outputs (m:336: Steps 1, 2, 5 and 7, Step 7 'open'), then the §7.5 enumeration."""
    cn, title = ceiling(t)
    return {"licensing": licensing(t), "labels": label_set(t, reasons), "ceiling": {"name": cn, "title": title},
            "abstract_clause": abstract_clause(t), "s81": s81_text(t), "step7": step7(t),
            "dose_note": dose_note(flag, table), "enumeration": enumeration(t, flag, table, reasons)}


# --- the sentence table (PIN-20) -------------------------------------------------------------------
TABLE_KINDS = ("placeholder", "of-record", "posted")
THESES = (None, "main", "fallback-1", "fallback-2")
KINDS_VOCAB = ("abstract-fifth-stage", "abstract-olmo-clause", "subtitle-clause-2", "contribution-2v",
               "s5.5-label:e2a", "s5.5-label:e2b", "s5.5-label:f1", "s5.5-q3", "s5.5-summary",
               "s6-this-paper-row", "s7.1-title", "s7.2-sceptic", "s7.4-last", "s7.5-first",
               "s7.7-penultimate", "f1-corr-line", "dose-note", "s8.1-status", "tab2-row", "pi-edit")


def _forbidden() -> tuple[str, ...]:
    # built, never written whole: a site-check suite greps the repo for these literals
    return ("choice_read_" + "state" + "present", "(10)" + " the", "slip" + " (10)")


def _ws(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def table_problems(tab: Any, *, read_repo_file: Callable[[str], bytes | None] | None = None) -> list[str]:
    """Every reason the declared sentence table is refused; [] = accepted."""
    # PIN (Code, declared at LOCK v0.1): PIN-20 -- schema m-posting-sentences-v1; `kind` (placeholder |
    # of-record | posted) is authoritative; paths data/m/gates/m_posting_sentences.placeholder.json
    # (LOCK v0.1 hashes it), .../m_posting_sentences.json (the table of record, LOCK v1.0) and
    # .../m_posting_sentences.posted-v1.json; a forbidden literal in any text is refused (the roster-
    # word refusal is dropped: a table carries no pick). The table of record's classification is
    # Code's, outcome-blind at LOCK v1.0, values-checked.
    p: list[str] = []
    if not isinstance(tab, Mapping):
        return ["the table is not a JSON object"]
    want = ["cells", "kind", "kinds_vocabulary", "posting", "preprint", "rows", "schema"]
    if sorted(tab) != want:
        return [f"table keys {sorted(tab)} != {want}"]
    if tab["schema"] != TABLE_SCHEMA:
        p.append(f"schema {tab['schema']!r}")
    if tab["kind"] not in TABLE_KINDS:
        p.append(f"kind {tab['kind']!r} not in {TABLE_KINDS}")
    if tab["posting"] != "v1":
        p.append(f"posting {tab['posting']!r} (v1 only; v2 is G-ANL-F3's)")
    if list(tab["cells"]) != list(CELLS):
        p.append(f"cells {tab['cells']!r} != {list(CELLS)}")
    if list(tab["kinds_vocabulary"]) != list(KINDS_VOCAB):
        p.append("kinds_vocabulary differs from the declared vocabulary")
    rows = tab["rows"]
    if not isinstance(rows, list) or not rows:
        return p + ["rows must be a non-empty list"]
    rk = ["dose_note", "dose_note_span", "id", "kinds", "loc", "null_cells", "text", "text_sha256", "thesis"]
    ids, locs = [], []
    for r in rows:
        if not isinstance(r, Mapping) or sorted(r) != rk:
            p.append(f"row keys {sorted(r) if isinstance(r, Mapping) else r!r} != {rk}")
            continue
        rid = r["id"]
        ids.append(rid)
        lc = r["loc"]
        if not (isinstance(lc, Mapping) and sorted(lc) == ["line", "section", "sentence"]
                and type(lc["line"]) is int and type(lc["sentence"]) is int and lc["line"] >= 1
                and lc["sentence"] >= 1 and isinstance(lc["section"], str)):
            p.append(f"{rid}: loc must be {{line (int >= 1), sentence (int >= 1), section (str)}}")
        else:
            locs.append((lc["line"], lc["sentence"]))
        if not isinstance(r["text"], str) or not r["text"]:
            p.append(f"{rid}: text must be a non-empty str")
            continue
        if r["text_sha256"] != hashlib.sha256(r["text"].encode("utf-8")).hexdigest():
            p.append(f"{rid}: text_sha256 is not sha256(text)")
        if not isinstance(r["null_cells"], list) or any(c not in CELLS for c in r["null_cells"]):
            p.append(f"{rid}: null_cells outside the cells {list(CELLS)}")
        if r["thesis"] not in THESES:
            p.append(f"{rid}: thesis {r['thesis']!r} not in {THESES}")
        if type(r["dose_note"]) is not bool:
            p.append(f"{rid}: dose_note must be a bool")
        elif r["dose_note"]:
            if not (isinstance(r["dose_note_span"], str) and r["dose_note_span"]
                    and r["dose_note_span"] in r["text"]):
                p.append(f"{rid}: a dose-note row needs a non-empty span that is a substring of its text")
        elif r["dose_note_span"] is not None:
            p.append(f"{rid}: a span on a row whose dose_note is false")
        if not isinstance(r["kinds"], list) or any(k not in KINDS_VOCAB for k in r["kinds"]):
            p.append(f"{rid}: a kind outside the vocabulary")
        for f in _forbidden():
            if f in r["text"]:
                p.append(f"{rid}: a forbidden literal in the text")
    if len(set(ids)) != len(ids):
        p.append("duplicate row ids")
    if any(b <= a for a, b in zip(locs, locs[1:])):
        p.append("rows are not in strictly increasing (loc.line, loc.sentence) order")
    if not any(isinstance(r, Mapping) and "f1-corr-line" in (r.get("kinds") or []) for r in rows):
        p.append("no row of kind f1-corr-line")
    pre = tab["preprint"]
    if tab["kind"] == "placeholder":
        if pre is not None:
            p.append("a placeholder table carries no preprint")
    elif tab["kind"] in ("of-record", "posted"):
        if not (isinstance(pre, Mapping) and sorted(pre) == ["bytes", "lines", "path", "sha256"]):
            p.append("an of-record / posted table names its preprint {path, sha256, bytes, lines}")
        else:
            data = read_repo_file(pre["path"]) if read_repo_file is not None else None
            if data is None:
                p.append(f"preprint {pre['path']!r} unreadable")
            elif (hashlib.sha256(data).hexdigest() != pre["sha256"] or len(data) != pre["bytes"]
                  or data.decode("utf-8").count("\n") != pre["lines"]):
                p.append("the preprint's sha256 / bytes / lines differ from the table's")
            else:
                p += _placement_problems(rows, data.decode("utf-8"))
    return p


def _placement_problems(rows: Sequence[Any], text: str) -> list[str]:
    """Each row's text (whitespace-normalized) must occur in the preprint and BEGIN on its declared
    loc.line (it may run on to later lines); rows sharing a line occur there in loc.sentence order."""
    lines = text.split("\n")
    body = _ws(text)
    p: list[str] = []
    cursor: dict[int, int] = {}          # rows arrive in (line, sentence) order (checked above)
    for r in rows:
        if not (isinstance(r, Mapping) and isinstance(r.get("text"), str) and isinstance(r.get("loc"), Mapping)):
            continue
        w = _ws(r["text"])
        if w not in body:
            p.append(f"{r['id']}: row text not found in the preprint")
            continue
        ln = r["loc"].get("line")
        if type(ln) is not int or not 1 <= ln <= len(lines):
            p.append(f"{r['id']}: loc.line {ln!r} is not a line of the preprint")
            continue
        head, rest = _ws(lines[ln - 1]), _ws("\n".join(lines[ln - 1:]))
        start = cursor.get(ln, 0)
        i = rest.find(w, start)
        if not head or i < 0 or i >= len(head):
            first = rest.find(w)
            p.append(f"{r['id']}: rows sharing line {ln} do not occur there in loc.sentence order"
                     if start and head and 0 <= first < len(head)
                     else f"{r['id']}: row text does not begin on its declared preprint line {ln}")
            continue
        cursor[ln] = i + len(w)
    return p


# The placeholder's rows (§9.5): (id, null_cells, thesis, dose_note, kinds). Synthetic; not derived
# from PREPRINT-v1_0-draft.md (not the preprint of record, m:58).
PLACEHOLDER_SPEC = (
    ("P01", [], None, False, []),
    ("P02", ["e2a"], None, False, ["s5.5-label:e2a"]),
    ("P03", ["f1"], None, True, ["f1-corr-line", "dose-note", "s5.5-label:f1"]),
    ("P04", ["e2b"], None, False, ["s5.5-label:e2b"]),
    ("P05", ["weight"], None, False, []),
    ("P06", ["olmo-base"], None, False, ["tab2-row"]),
    ("P07", ["olmo-sft"], None, False, ["tab2-row"]),
    ("P08", ["olmo-dpo"], None, False, ["tab2-row"]),
    ("P09", ["olmo-instruct"], None, False, ["tab2-row"]),
    ("P10", ["S1"], None, False, []),
    ("P11", ["e2a", "f1", "e2b"], None, False, ["s5.5-summary"]),
    ("P12", ["olmo-sft", "olmo-dpo", "olmo-instruct"], None, False, ["abstract-olmo-clause", "s5.5-q3"]),
    ("P13", ["e2a", "olmo-sft"], None, False, ["contribution-2v"]),
    ("P14", [], "main", False, ["s7.1-title"]),
    ("P15", [], "fallback-1", False, ["s7.2-sceptic"]),
    ("P16", [], "fallback-2", False, ["subtitle-clause-2"]),
    ("P17", ["e2a"], "fallback-1", False, ["s7.7-penultimate"]),
    ("P18", [], None, True, ["dose-note"]),
    ("P19", ["e2a", "f1"], None, False, ["abstract-fifth-stage"]),
    ("P20", [], None, False, ["s8.1-status"]),
    ("P21", ["olmo-dpo"], "fallback-1", False, ["s7.4-last"]),
)
#: (line, sentence) of each placeholder row: Pnn on line nn as its first sentence, except P21, the
#: second sentence of line 20 (two rows of one preprint line, PIN-20).
PLACEHOLDER_LOC = {r[0]: (int(r[0][1:]), 1) for r in PLACEHOLDER_SPEC} | {"P21": (20, 2)}
#: Expected fire counts over the 1,080 tuples: (a), (b), (c) under flag True, (c) under flag False.
PLACEHOLDER_FIRES = {
    "P01": (0, 0, 0, 0), "P02": (864, 0, 0, 0), "P03": (864, 0, 0, 1080), "P04": (1080, 0, 0, 0),
    "P05": (1080, 0, 0, 0), "P06": (1080, 0, 0, 0), "P07": (900, 0, 0, 0), "P08": (900, 0, 0, 0),
    "P09": (900, 0, 0, 0), "P10": (0, 0, 0, 0), "P11": (1080, 0, 0, 0), "P12": (1075, 0, 0, 0),
    "P13": (1044, 0, 0, 0), "P14": (0, 1080, 0, 0), "P15": (0, 864, 0, 0), "P16": (0, 0, 0, 0),
    "P17": (864, 864, 0, 0), "P18": (0, 0, 0, 1080), "P19": (864, 0, 0, 0), "P20": (0, 0, 0, 0),
    "P21": (900, 864, 0, 0),
}


def placeholder_table() -> dict:
    """The placeholder table (PIN-20): synthetic '[placeholder Pnn] ...' texts at PLACEHOLDER_LOC."""
    rows = []
    for rid, cells, thesis, dose, kinds in PLACEHOLDER_SPEC:
        ln, sn = PLACEHOLDER_LOC[rid]
        what = (("asserts a null on " + ", ".join(cells)) if cells else "asserts no null")
        what += f" and states the {thesis} thesis" if thesis else ""
        span = f"synthetic dose note {rid}" if dose else None
        text = f"[placeholder {rid}] A synthetic sentence that {what}" + (f"; {span}." if dose else ".")
        rows.append({"id": rid, "loc": {"line": ln, "section": "placeholder", "sentence": sn}, "text": text,
                     "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                     "null_cells": list(cells), "thesis": thesis, "dose_note": dose,
                     "dose_note_span": span, "kinds": list(kinds)})
    return {"schema": TABLE_SCHEMA, "kind": "placeholder", "posting": "v1", "preprint": None,
            "cells": list(CELLS), "kinds_vocabulary": list(KINDS_VOCAB), "rows": rows}


# --- the 0.12-artifact flag (PIN-19) --------------------------------------------------------------
def flag_of_record(path: Path, committed: Callable[[Path], tuple[list[str], bytes | None]]) -> dict:
    """TRUE iff G-CAL's model-free artifact is committed at HEAD and identical in the working tree,
    has schema m-gcal-model-free-v1, and carries an f1_012 block."""
    # PIN (Code, declared at LOCK v0.1): PIN-19 -- existence-keyed (STOP-4 item 8; m:349's "iff"):
    # renders_sha_matches_calib is recorded beside the flag and is not part of it; the battery runs
    # both values.
    p = Path(path)
    out = {"path": _repo_rel(p), "sha256": None, "introduced_at": FLAG_INTRODUCED_AT, "value": False,
           "renders_sha_matches_calib": None, "reason": None}
    if not p.is_file():
        out["reason"] = "absent"
        return out
    probs, data = committed(p)
    if probs or data is None:
        out["reason"] = "not committed at HEAD with identical working-tree bytes"
        return out
    out["sha256"] = hashlib.sha256(data).hexdigest()
    try:
        doc = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        out["reason"] = "not JSON"
        return out
    if not isinstance(doc, Mapping) or doc.get("schema") != FLAG_SCHEMA:
        out["reason"] = "schema is not m-gcal-model-free-v1"
        return out
    blk = doc.get("f1_012")
    if not isinstance(blk, Mapping):
        out["reason"] = "no f1_012 block"
        return out
    out["value"] = True
    out["reason"] = "committed, schema m-gcal-model-free-v1, f1_012 present"
    out["renders_sha_matches_calib"] = blk.get("renders_sha_matches_calib")
    return out


# --- the closure (PIN-1) ---------------------------------------------------------------------------
_CLOSURE_CODE = r'''
import builtins, hashlib, importlib, importlib.util, io, json, sys
from pathlib import Path
repo = Path(sys.argv[1]).resolve()
analyzer = Path(sys.argv[2]).resolve()
lazies = sys.argv[3:]
sys.path.insert(0, str(repo))
opened = set()
_bo, _io = builtins.open, io.open
def _hook(f, *a, **k):
    try:
        p = Path(f).resolve()
        if repo in p.parents:
            opened.add(p.relative_to(repo).as_posix())
    except Exception:
        pass
    return _bo(f, *a, **k)
builtins.open = _hook
io.open = _hook
spec = importlib.util.spec_from_file_location("m_analyze_closure", analyzer)
mod = importlib.util.module_from_spec(spec)
sys.modules["m_analyze_closure"] = mod
spec.loader.exec_module(mod)
for m in lazies:
    importlib.import_module(m)
builtins.open, io.open = _bo, _io
pkg = (repo / "valence_core" / "m").resolve()
mods = {}
for name, m in sorted(sys.modules.items()):
    f = getattr(m, "__file__", None)
    if not (name == "valence_core" or name.startswith("valence_core.")) or not f:
        continue
    p = Path(f).resolve()
    if p.parent == pkg or pkg in p.parents:
        continue
    mods[p.relative_to(repo).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
data = {rel: hashlib.sha256((repo / rel).read_bytes()).hexdigest()
        for rel in sorted(opened) if not rel.endswith(".py")}
print(json.dumps({"modules": mods, "data": data}, sort_keys=True))
'''


def closure(analyzer: Path | None = None) -> dict:
    """The verdict path's import closure outside valence_core/m, computed in a fresh interpreter."""
    # PIN (Code, declared at LOCK v0.1): PIN-1 -- a fresh `python -I -B` imports this file and
    # LAZY_VERDICT_MODULES; the closure is {modules: sha256 of __file__ of every loaded valence_core.*
    # module outside valence_core/m, data: sha256 of every repository non-.py file opened during
    # those imports}; its sha256 is over the compact sort-keyed JSON.
    a = Path(analyzer or Path(__file__).resolve())
    r = subprocess.run([sys.executable, "-I", "-B", "-c", _CLOSURE_CODE, str(REPO), str(a),
                        *LAZY_VERDICT_MODULES], capture_output=True, text=True, cwd=str(REPO))
    if r.returncode != 0:
        raise AnlStop(f"STOP: the closure could not be computed: {(r.stderr or '').strip()[-300:]}")
    return json.loads(r.stdout)


def closure_sha256(cl: Mapping) -> str:
    return hashlib.sha256(json.dumps(cl, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


# --- environment and IO --------------------------------------------------------------------------
def _repo_rel(p: Path | str) -> str:
    try:
        return Path(p).resolve().relative_to(REPO.resolve()).as_posix()
    except (ValueError, OSError):
        return str(p)


def _sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


@dataclass
class Env:
    """What a command needs from the site: the production env reads git and the repo; the battery
    substitutes temp-directory doubles (PIN-30: stub provenance only through allow_stub)."""
    proposal_path: Path
    committed: Callable[[Path], tuple[list[str], bytes | None]]
    analyzer_path: Path
    package_sha256: str
    closure_sha256: str
    allow_stub: bool
    gate_line: Callable[[str], tuple[str, list[str]]]
    read_repo_file: Callable[[str], bytes | None]
    say: Callable[[str], None] = field(default=lambda line: print(line, flush=True))


def _prod_committed(p: Path) -> tuple[list[str], bytes | None]:
    from valence_core.m import stages
    rel = _repo_rel(p)
    if rel == str(p):
        return [f"{p}: outside the repository"], None
    return stages._committed(rel)


def _prod_read(rel: str) -> bytes | None:
    q = (REPO / rel).resolve()
    if REPO.resolve() not in q.parents or not q.is_file():
        return None
    return q.read_bytes()


def production_env() -> Env:
    from valence_core.m import stages
    return Env(proposal_path=REPO / PROPOSAL_REL, committed=_prod_committed,
               analyzer_path=Path(__file__).resolve(), package_sha256=resume.package_sha256(),
               closure_sha256=closure_sha256(closure()), allow_stub=False,
               gate_line=lambda name: stages.gate_line(name, REPO / PROPOSAL_REL), read_repo_file=_prod_read)


def write_texts_once(pairs: Sequence[tuple[Path, Any]]) -> str:
    """Write each (path, obj) once (json_text(indent=1)); 'written' / 'identical'; a different file
    anywhere refuses all (nothing written)."""
    # PIN (Code, declared at LOCK v0.1): PIN-37 -- every output is write-once and timestamp-free; a
    # re-run on unchanged inputs is byte-identical ('identical'); an artifact that must be replaced is
    # moved aside by hand with `git mv` to a dated superseded name on the seat's ruling, recorded in
    # an entry, before the canonical name is written again.
    # PIN (Code, declared at LOCK v0.1): PIN-25 -- outputs: data/m/gates/G-ANL-F0.json (step 8; the
    # 2,160-row output table is not committed, its sha256 recorded); data/m/verdicts/{unit}_VERDICTS
    # .json, _secondary.json, _NOT-RUN.json and POSTING-v1_outputs.{of-record,posted}.json (named by
    # the table kind: m:278's enumeration over the table of record and its re-run on the posted text
    # are two records of one posting); the .gitignore admit block (and any -diff) for
    # data/m/verdicts/ is deferred to the commit that first writes there.
    texts =[(Path(p), resume.json_text(o, indent=1)) for p, o in pairs]
    status = []
    for p, text in texts:
        if p.exists() or p.is_symlink():
            same = p.is_file() and not p.is_symlink() and p.read_text(encoding="utf-8") == text
            if not same:
                raise AnlRefusal(f"REFUSED: {p.name} exists with different bytes -- write-once (move it "
                                 f"aside by hand on the seat's ruling, PIN-37)")
            status.append("identical")
        else:
            status.append("new")
    for (p, _), (_, o), st in zip(texts, pairs, status):
        if st == "new":
            p.parent.mkdir(parents=True, exist_ok=True)
            resume.atomic_write_json(p, o, indent=1)
    return "identical" if all(s == "identical" for s in status) else "written"


def _load_mapping(p: Path, what: str) -> Mapping:
    """_load_json that refuses (exit 2) a document that is not a JSON object (PIN-26)."""
    doc = _load_json(p, what)
    if not isinstance(doc, Mapping):
        raise AnlRefusal(f"REFUSED: {what} is not a JSON object ({type(doc).__name__})")
    return doc


def refuse_beside(target: Path, others: Sequence[Path]) -> None:
    """m:324's exclusivity at write time: a unit's VERDICTS and NOT-RUN outputs never coexist."""
    # PIN (Code, declared at LOCK v0.1): PIN-41 -- a unit is NOT-RUN or analyzed, never both (m:324:
    # NOT-RUN iff its causes hold; "a locked unit that produces sessions is analyzed"): `verdicts`
    # refuses (exit 2, nothing written) to write {U}_VERDICTS.json beside an existing
    # {U}_NOT-RUN.json, or {U}_NOT-RUN.json beside an existing {U}_VERDICTS.json or _secondary.json;
    # `not-run` refuses beside an existing {U}_VERDICTS.json; the posting's cross-check refuses a
    # unit carrying both (PIN-23). A wrong one is moved aside only under PIN-37.
    for o in others:
        if o.exists() or o.is_symlink():
            raise AnlRefusal(f"REFUSED: {o.name} exists, so {target.name} is not written beside it -- a "
                             f"unit's VERDICTS and NOT-RUN outputs are exclusive (m:324; PIN-41)")


def _load_json(p: Path, what: str) -> Any:
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError) as e:
        raise AnlRefusal(f"REFUSED: {what} unreadable ({type(e).__name__})")


def _file_rec(p: Path, data: bytes) -> dict:
    return {"path": _repo_rel(p), "sha256": _sha256_bytes(data)}


# --- VERDICTS (PIN-7) -----------------------------------------------------------------------------
@dataclass
class VerdictInputs:
    unit: str
    lock: Path
    decisions: Path
    campaign: Path
    time: Path
    qual: Path
    out: Path
    adjudication: Path | None = None
    pi_stop: Path | None = None
    olmo_states: Path | None = None
    sentences: Path | None = None
    flag_source: Path | None = None


def _read_bytes(p: Path, what: str) -> bytes:
    try:
        return Path(p).read_bytes()
    except OSError as e:
        raise AnlRefusal(f"REFUSED: {what} unreadable ({type(e).__name__})")


def _validate_olmo_states(doc: Any, out_dir: Path) -> tuple[dict, dict, dict]:
    """--olmo-states for Q-F0's VERDICTS: {schema, states: {OLMo-c: {...}}} -> (coords, reasons, decl)."""
    if not isinstance(doc, Mapping) or doc.get("schema") != OLMO_STATES_SCHEMA or sorted(doc) != ["schema", "states"]:
        raise ValueError(f"the OLMo states input is {{schema {OLMO_STATES_SCHEMA}, states}}")
    st = doc["states"]
    if not isinstance(st, Mapping) or sorted(st) != sorted(UNITS[1:]):
        raise ValueError(f"states must name exactly {UNITS[1:]}")
    coords, reasons = {}, {}
    for u in UNITS[1:]:
        d = st[u]
        if not isinstance(d, Mapping) or d.get("state") not in O6:
            raise ValueError(f"{u}: state must be one of {O6}")
        pend = None
        if d["state"] == "PENDING":
            pend = {k_: v for k_, v in d.items() if k_ != "state"}
        elif d["state"] == "NOT-RUN":
            if sorted(d) != ["cause", "date", "state"]:
                raise ValueError(f"{u}: a NOT-RUN state is {{state, cause, date}}")
            reasons[u] = not_run_reason(u, d["cause"], d["date"])
            if not _iso_date(d["date"]):            # PIN-43: whatever the cause (dose-not-completable's phrase has no date)
                raise ValueError(f"{u}: a NOT-RUN state's date must be a real YYYY-MM-DD date: {d['date']!r}")
        elif sorted(d) != ["state"]:
            raise ValueError(f"{u}: an outcome state is {{state}}")
        crosscheck_coordinate(u, d["state"], reasons.get(u), pend, out_dir)
        coords[u] = d["state"]
    return coords, reasons, {u: dict(st[u]) for u in UNITS[1:]}


def run_verdicts(inp: VerdictInputs, env: Env) -> tuple[str, list[str], list[Path]]:
    """V0-V11. Returns (status, stdout lines, written paths); raises AnlRefusal / AnlStop."""
    # PIN (Code, declared at LOCK v0.1): PIN-7 -- one unit per invocation; refusals decided before any
    # pick is interpreted (V1), then on structure (V2); readrule.release_full names the release (V3);
    # V4's content assertions STOP; outputs are written once, and stdout is printed after writing. A
    # unit NOT-RUN by §5's no-first-read cause gets {U}_NOT-RUN.json from this command.
    U = inp.unit
    lines: list[str] = []
    # V0 -- the gate line is printed first (m:267), before any refusal
    gl, gprobs = env.gate_line(f"VERDICTS {U}")
    env.say(gl)
    if gprobs:
        raise AnlRefusal(f"REFUSED: the gate line cannot be logged in full: {gprobs}")
    # V1 -- refusals decided before any pick-bearing byte is interpreted
    if U not in keys.UNITS_BUILT or U not in UNITS:
        raise AnlRefusal(f"REFUSED: unit {U!r} is not a built unit {UNITS}")
    pbytes = _read_bytes(env.proposal_path, "the proposal")
    if _sha256_bytes(pbytes) != PROPOSAL_SHA256:
        raise AnlRefusal("REFUSED: the proposal's sha256 is not the pinned v1.11's (PIN-31)")
    aprobs, abytes = env.committed(env.analyzer_path)
    if aprobs or abytes is None:
        raise AnlRefusal(f"REFUSED: the analyzer is not committed at HEAD: {aprobs}")
    lprobs, lbytes = env.committed(inp.lock)
    if lprobs or lbytes is None:
        raise AnlRefusal(f"REFUSED: the lock is not committed at HEAD: {lprobs}")
    ltext = lbytes.decode("utf-8", "replace")
    a_sha = _sha256_bytes(abytes)
    for what, val in (("analyzer sha256", a_sha), ("package_sha256", env.package_sha256),
                      ("closure sha256", env.closure_sha256)):
        # PIN (Code, declared at LOCK v0.1): PIN-14 -- the analyzer of record for a unit is the blob
        # its LOCK v1.0 hashes: the lock text names the analyzer's sha256, package_sha256 and the
        # closure sha256 (PIN-1), each asserted here. When HEAD's three equal the lock's, VERDICTS
        # runs at HEAD with no worktree; otherwise from a worktree of the lock commit with every data
        # input and output passed as an absolute path into the main tree, on the PI's word for the
        # worktree (git writes; not implemented at step 8). G-ANL-F3's versioning (m:291) is deferred
        # by the seat to before step 19 (C7, 2026-10-10).
        if val not in ltext:
            raise AnlRefusal(f"REFUSED: the lock does not name this run's {what} (PIN-14, PIN-1)")
    try:
        decisions = decisions_file(_load_json(inp.decisions, "the decisions input"), U)
    except ValueError as e:
        raise AnlRefusal(f"REFUSED: decisions input: {e}")
    dbytes = _read_bytes(inp.decisions, "the decisions input")
    outs = {"verdicts": inp.out / f"{U}_VERDICTS.json", "secondary": inp.out / f"{U}_secondary.json",
            "not_run": inp.out / f"{U}_NOT-RUN.json"}
    inputs: dict = {"lock": _file_rec(inp.lock, lbytes), "decisions": _file_rec(inp.decisions, dbytes)}
    table = coords = reasons = flag = states_decl = None
    if U == "Q-F0":
        if inp.sentences is None or inp.olmo_states is None:
            raise AnlRefusal("REFUSED: Q-F0's VERDICTS needs --sentences (the table of record) and "
                             "--olmo-states (V10)")
        sprobs, sbytes = env.committed(inp.sentences)
        if sprobs or sbytes is None:
            raise AnlRefusal(f"REFUSED: the sentence table is not committed at HEAD: {sprobs}")
        table = _load_json(inp.sentences, "the sentence table")
        tp = table_problems(table, read_repo_file=env.read_repo_file)
        if tp or table.get("kind") != "of-record":
            raise AnlRefusal(f"REFUSED: the sentence table is not an accepted table of record: "
                             f"{tp or ['kind ' + repr(table.get('kind'))]}")
        # PIN (Code, declared at LOCK v0.1): PIN-40 -- LOCK-m-F0 v1.0 hashes the sentence table of
        # record and the preprint of record (m:286: "values-checked and hashed here, so that the
        # VERDICTS entry (step 17) enumerates over it"): Q-F0's VERDICTS refuses unless the lock
        # text names both the table's sha256 and its preprint's sha256 (the table's own record of
        # it, verified against the file by table_problems). The posting's of-record table, when a
        # Q-F0 output of this command records one (its VERDICTS, or a locked unit's no-first-read
        # NOT-RUN), must be that table (and so the lock's); on Q-F0's Clock NOT-RUN path the table
        # of record is built at the posting (m:278, m:286) and no lock binds it; a posted-kind table
        # is the re-run on the posted text, which no lock hashes.
        for what, val in (("sentence table of record's sha256", _sha256_bytes(sbytes)),
                          ("preprint of record's sha256", (table.get("preprint") or {}).get("sha256"))):
            if not (isinstance(val, str) and val and val in ltext):
                raise AnlRefusal(f"REFUSED: the lock does not name the {what} (m:286; PIN-40)")
        try:
            coords, reasons, states_decl = _validate_olmo_states(_load_json(inp.olmo_states,
                                                                            "the OLMo states"), inp.out)
        except ValueError as e:
            raise AnlRefusal(f"REFUSED: --olmo-states: {e}")
        inputs["sentences"] = _file_rec(inp.sentences, sbytes)
        inputs["olmo_states"] = _file_rec(inp.olmo_states, _read_bytes(inp.olmo_states, "the OLMo states"))
        flag = flag_of_record(inp.flag_source or REPO / FLAG_SOURCE_REL, env.committed)
    adj_doc = adj_bytes = pis_doc = pis_bytes = None
    if inp.adjudication is not None:
        adj_bytes = _read_bytes(inp.adjudication, "the adjudication")
        adj_doc = _load_json(inp.adjudication, "the adjudication")
    if inp.pi_stop is not None:
        pis_bytes = _read_bytes(inp.pi_stop, "the PI-stop record")
        pis_doc = _load_json(inp.pi_stop, "the PI-stop record")
    # V2 -- refusals on checkpoint structure
    try:
        ck = resume.read_checkpoint(inp.campaign)
    except SystemExit as e:
        raise AnlRefusal(f"REFUSED: the campaign checkpoint: {e}")
    cbytes = _read_bytes(inp.campaign, "the campaign checkpoint")
    csha = _sha256_bytes(cbytes)
    ident = ck["identity"]
    if ident.get("unit") != U or ident.get("stage") != "campaign":
        raise AnlRefusal(f"REFUSED: the campaign checkpoint is {ident.get('unit')}/{ident.get('stage')}, "
                         f"not {U}/campaign")
    if ident.get("lock_sha256") != _sha256_bytes(lbytes):
        raise AnlRefusal("REFUSED: the campaign's identity lock_sha256 is not the lock's sha256")
    if resume.pending_end(ck) is not None:
        raise AnlRefusal("REFUSED: the campaign carries an end pending (re-finish it first, finding R1)")
    ended = resume.ended_status(ck)
    if ended not in ("COMPLETE", "CAP", "PI-STOP", "STOP"):
        raise AnlRefusal(f"REFUSED: the campaign has not ended (status {ended!r}); VERDICTS waits for its "
                         f"terminal state (m:247)")
    camp = ck.get("campaign") or {}
    if ended == "STOP" and ck["sessions"] and not camp.get("end_look"):
        # PIN (Code, declared at LOCK v0.1): PIN-10 -- the seat's C9(ii) (2026-10-10): a STOP-ended
        # campaign with at least one launch recorded carries its end look, evaluated and recorded by
        # stages at the STOP point; one without it was not written by the lock's package -- a
        # structural refusal here at V2, before V3 releases any record. With no launch recorded (a
        # G-VER STOP at the first launch) there is no look to carry.
        raise AnlRefusal("REFUSED: a STOP-ended campaign records no end look at its STOP (the seat's C9(ii)) -- "
                         "not written by the lock's package")
    end_look = camp.get("end_look")
    reused_lk = None
    if end_look is not None:
        # PIN (Code, declared at LOCK v1.0): PIN-46 -- the seat's round-2 item 3 (lock §9.6) orders "(c)
        # the end look's launch count" built "as VERDICTS refusals" that "guard the checkpoint against a
        # hand edit". Code's reading: wherever campaign.end_look is recorded (STOP and terminal alike), its
        # at_launches is an int (exact type: a bool or a float is no launch count) equal to len(sessions),
        # the launches recorded -- never a provenance `launched` sum (a G-VER record is quarantined in the
        # stop block, never a session); an end look reusing cadence look k (end_is_look k) carries that
        # look's count too: ck.looks records a look k (its result's look) at the end look's at_launches,
        # as the writer reuses only the look recorded at n. Checked before PIN-45's refusal and PIN-9's
        # branch, so each refusal shows its own message.
        n_rec = len(ck["sessions"])
        el_n = end_look.get("at_launches") if isinstance(end_look, Mapping) else None
        if type(el_n) is not int or el_n != n_rec:
            raise AnlRefusal(f"REFUSED: the end look's launch count ({el_n!r}) is not the launches recorded "
                             f"({n_rec}) -- not written by the lock's package")
        if "end_is_look" in end_look:
            k_el = end_look["end_is_look"]
            looks_k = [lk_ for lk_ in ck["looks"] if isinstance(lk_, Mapping) and isinstance(lk_.get("result"), Mapping)
                       and type(lk_["result"].get("look")) is type(k_el) and lk_["result"].get("look") == k_el]
            reused_lk = next((lk_ for lk_ in looks_k if type(lk_.get("at_launches")) is int
                              and lk_["at_launches"] == el_n), None)
            if reused_lk is None:
                raise AnlRefusal(f"REFUSED: the end look's launch count ({el_n!r}) is not that of the look it reuses "
                                 f"(look {k_el!r}, recorded at {[lk_.get('at_launches') for lk_ in looks_k]}) -- not "
                                 f"written by the lock's package")
    pauses = camp.get("pauses") or []
    if isinstance(end_look, Mapping):
        # PIN (Code, declared at LOCK v1.0): PIN-45 -- the seat's round-2 item 3 (lock §9.6) orders "(b) a
        # fired end look without a matching pause" built "as VERDICTS refusals". Code's reading, mirroring
        # the writer's invariants (stages._campaign_end, _stop_end_look, run_campaign's cadence pause; its
        # one adjudication write is a resume, and an ended campaign is never resumed): an end look is
        # fired iff its `fired` or any result's is, or -- reusing look k -- look k's as ck.looks records
        # it; its bars are its fired results' names in order. A pause raised at the end (a fresh end
        # look's; a reused look k's at a hair-trigger STOP, which pre-empted the cadence pause) is matched
        # only by the LAST pause {kind end_look, look 'end' | kind look, look k, at_launches, bars},
        # unadjudicated (its ruling enters as PIN-9's declared file); a reused look k's at a terminal or
        # G-VER end by SOME pause {kind look, look k, at_launches, bars} carrying a str adjudication
        # (ruled before the end, through stages: by the seat's adjudication, or by the PI's stop text
        # recorded as the pause's ruling (stages.py:2124-2129); a schedule_exhausted pause may follow it
        # at the same n). kind, look and at_launches compare by value and exact type, as the writer
        # writes ints and strs. The rule is chosen by the end's class as recorded, and at a STOP that
        # class is checked by ids against the writer's own assertions (stages._stop_end_look): a
        # hair-trigger STOP's (template, s) is the last session recorded, a G-VER STOP's none of them (a
        # relabel that also moves the id off the record passes: PIN-45's limits). Checked before PIN-9's
        # branch, so a deleted pause is never read as no pause.
        el_res = end_look.get("results") if isinstance(end_look.get("results"), list) else []
        el_bars = [r_.get("name") for r_ in el_res if isinstance(r_, Mapping) and r_.get("fired")]
        lk_res = reused_lk["result"] if reused_lk is not None else {}
        lk_rs = lk_res.get("results") if isinstance(lk_res.get("results"), list) else []
        lk_fired = bool(lk_res.get("fired")) or any(isinstance(r_, Mapping) and r_.get("fired") for r_ in lk_rs)
        if end_look.get("fired") or el_bars or lk_fired:
            reused = "end_is_look" in end_look
            want = ({"kind": "look", "look": end_look["end_is_look"]} if reused
                    else {"kind": "end_look", "look": "end"})
            want.update(at_launches=end_look.get("at_launches"), bars=el_bars)

            def _matches(p_: Any) -> bool:
                return (isinstance(p_, Mapping) and isinstance(p_.get("bars"), list) and p_["bars"] == el_bars
                        and all(type(p_.get(k_)) is type(want[k_]) and p_.get(k_) == want[k_]
                                for k_ in ("kind", "look", "at_launches")))
            stop_el = ck.get("stop")
            if isinstance(stop_el, Mapping):
                # the class that chooses the rule below, by ids only, against the writer's assertions
                # (stages._stop_end_look); a stop block is recorded only at a STOP (resume.ended_status), and any
                # other STOP bar is refused after PIN-8 whichever rule is chosen
                hit_id = (stop_el.get("template"), stop_el.get("s"))
                rec_ids = [(r_["template"], r_["s"]) for r_ in ck["sessions"]]
                if stop_el.get("bar") == HAIR_BAR and rec_ids[-1:] != [hit_id]:
                    raise AnlRefusal(f"REFUSED: a hair-trigger STOP's session {hit_id!r} is not the last one recorded "
                                     f"(the last: {rec_ids[-1:]!r}) -- not written by the lock's package")
                if stop_el.get("bar") in GVER_BARS and hit_id in rec_ids:
                    raise AnlRefusal(f"REFUSED: a G-VER STOP's quarantined record {hit_id!r} is among the sessions "
                                     f"recorded -- not written by the lock's package")
            end_raised = not reused or (ended == "STOP" and (stop_el.get("bar") if isinstance(stop_el, Mapping)
                                                             else None) not in GVER_BARS)
            if end_raised:
                # raised at the end (stages._campaign_end, _stop_end_look; appended by resume.apply_end): the
                # campaign's last pause, never adjudicated in the checkpoint (an ended campaign is never resumed)
                ok_pause = bool(pauses) and _matches(pauses[-1]) and pauses[-1].get("adjudication") is None
            else:
                # a cadence look's pause, raised before the end and ruled before the end, through stages (the
                # seat's adjudication, or the PI's stop text recorded as the pause's ruling: stages.py:2124-2129)
                ok_pause = any(_matches(p_) and isinstance(p_.get("adjudication"), str) for p_ in pauses)
            if not ok_pause:
                where = ("the campaign's last pause must be {}, unadjudicated" if end_raised
                         else "some pause must be {}, adjudicated").format(want)
                raise AnlRefusal(f"REFUSED: a fired end look records no matching pause ({where}) -- "
                                 f"not written by the lock's package")
    used_adj = None
    if pauses and pauses[-1].get("adjudication") is None:
        # PIN (Code, declared at LOCK v0.1): PIN-9 -- confirmed by the seat (C3, 2026-10-10): VERDICTS
        # refuses while the campaign's last pause is unadjudicated unless the seat's adjudication is
        # supplied as a declared file naming the unit, the checkpoint's sha256 and the pause; its path
        # and sha256 are recorded. Code never self-adjudicates. The seat's C9(i): the adjudication of a
        # fired end look on a terminal campaign enters as this declared --adjudication file; stages.py
        # need not record it. Code's reading, flagged for the seat: a pause raised at a STOP (when the
        # end look the seat's C9(ii) orders there fires; the pause is Code's application of m:330) is the
        # campaign's last pause, so C3's route covers it too.
        last = pauses[-1]
        ok = (isinstance(adj_doc, Mapping) and adj_doc.get("schema") == ADJ_SCHEMA and adj_doc.get("unit") == U
              and adj_doc.get("campaign_sha256") == csha
              and adj_doc.get("pause") == {"kind": last.get("kind"), "at_launches": last.get("at_launches")}
              and isinstance(adj_doc.get("text"), str) and adj_doc["text"].strip())
        if not ok:
            raise AnlRefusal("REFUSED: the campaign's last pause is unadjudicated; the seat's adjudication "
                             "enters as a declared --adjudication file (PIN-9)")
        used_adj = _file_rec(inp.adjudication, adj_bytes)
    elif adj_doc is not None:
        raise AnlRefusal("REFUSED: --adjudication given but the last pause is adjudicated (or none exists)")
    stop = ck.get("stop") or None
    stop_bar = stop.get("bar") if isinstance(stop, Mapping) else None
    used_pis = None
    if ended == "STOP" and stop_bar == HAIR_BAR:
        # PIN (Code, declared at LOCK v0.1): PIN-8 -- confirmed by the seat (C2, 2026-10-10; m:316's
        # path -- an adjudication "may end in a PI stop (terminal, analyzed as obtained)" -- applied to
        # the hair triggers): a scaffold_absorption hair-trigger STOP is analyzed only on a declared
        # PI-stop record naming the unit and the checkpoint's sha256 (path and sha256 recorded); it
        # then follows m:324's PI-stop rule. Whether an adjudicated fire may instead resume is for the
        # adjudication, if one arises; nothing is built for it. A G-VER STOP is a PI stop by m:284.
        ok = (isinstance(pis_doc, Mapping) and pis_doc.get("schema") == PI_STOP_SCHEMA
              and pis_doc.get("unit") == U and pis_doc.get("campaign_sha256") == csha
              and pis_doc.get("bar") == HAIR_BAR and isinstance(pis_doc.get("text"), str)
              and pis_doc["text"].strip())
        if not ok:
            raise AnlRefusal("REFUSED: the campaign ended on a scaffold_absorption hair-trigger STOP; it is "
                             "analyzed only on a declared PI-stop record naming it (--pi-stop; PIN-8)")
        used_pis = _file_rec(inp.pi_stop, pis_bytes)
    elif pis_doc is not None:
        raise AnlRefusal("REFUSED: --pi-stop given but the campaign did not end on a hair-trigger STOP")
    if ended == "STOP" and stop_bar not in GVER_BARS and stop_bar != HAIR_BAR:
        raise AnlRefusal(f"REFUSED: a campaign STOP on {stop_bar!r} is neither G-VER nor a hair trigger")
    prov = resume.report_provenance(ck)
    for e in prov:
        if resume.backend_identifier(e["record"]) != ident.get("backend_identifier"):
            raise AnlRefusal("REFUSED: a launching invocation's backend identifier is not the identity's "
                             "(no splicing, m:251)")
        if STUB_MARK in json.dumps(e["record"]) and not env.allow_stub:
            # PIN (Code, declared at LOCK v0.1): PIN-30 -- STUB_MARK provenance is accepted only by
            # the battery's internal path; the CLI refuses it.
            raise AnlRefusal("REFUSED: the campaign was written by the self-test stub (STUB_MARK)")
    if _sub(U) == "olmo" and not (isinstance(ident.get("pod_id"), str) and ident["pod_id"]):
        raise AnlRefusal("REFUSED: an OLMo campaign identity carries no pod id (m:267; never spliced)")
    c_arm, s_arm = keys.templates(U)
    floors = camp.get("floors") or {}
    if sorted(floors) != sorted((c_arm, s_arm)) or any(type(v) is not int or v < 0 for v in floors.values()):
        # a structural refusal: decided at V2, before V3 releases or V4 reads any record (PIN-7, PIN-26)
        raise AnlRefusal(f"REFUSED: the campaign records no floors for {c_arm} and {s_arm} (campaign.floors)")
    gates = {}
    for stg, path in (("time", inp.time), ("qual", inp.qual)):
        try:
            g = resume.read_checkpoint(path)
        except SystemExit as e:
            raise AnlRefusal(f"REFUSED: the {stg} checkpoint: {e}")
        gi = g["identity"]
        if gi.get("unit") != U or gi.get("stage") != stg or not isinstance(g.get("stage_end"), Mapping):
            raise AnlRefusal(f"REFUSED: the {stg} checkpoint is not an ended {U}/{stg} gate stage")
        for e in resume.report_provenance(g):
            if STUB_MARK in json.dumps(e["record"]) and not env.allow_stub:
                raise AnlRefusal(f"REFUSED: the {stg} checkpoint was written by the self-test stub")
        gates[stg] = g
        inputs[stg] = _file_rec(path, _read_bytes(path, f"the {stg} checkpoint"))
    inputs["campaign"] = {"path": _repo_rel(inp.campaign), "sha256": csha}
    # V3 -- the act of release is named (m:271)
    records = readrule.release_full(ck["sessions"])
    grecs = {stg: readrule.release_full(g["sessions"]) for stg, g in gates.items()}
    # V4 -- STOP on any content defect
    for stg, rs in (("campaign", records), *grecs.items()):
        for rec in rs:
            pr = record_problems(rec, U, stg)
            if pr:
                raise AnlStop(f"STOP: a {stg} record fails V4 ({pr[0]})")
    counts = campaign_counts(records, U)
    counts["prepick"] = prepick_counts(records, U)
    if ended == "COMPLETE" and any(counts["domain"][a] < floors.get(a, 0) for a in (c_arm, s_arm)):
        raise AnlStop("STOP: COMPLETE with an arm below its floor -- a bookkeeping defect")
    # V5 -- unit outcome
    state = unit_state(U, {"kind": "campaign", "ended": ended, "stop_bar": stop_bar,
                           "pi_stop_record": used_pis is not None, "counts": counts})
    quarantined = []
    if isinstance(stop, Mapping) and stop_bar in GVER_BARS and isinstance(stop.get("record"), Mapping):
        qr = stop["record"]
        quarantined.append({"template": qr.get("template"), "s": qr.get("s"), "bar": stop_bar,
                            "reached_first_read": bool(qr.get("choices")), "counted": False})
    dc, den = tabulate(records, _sub(U))
    common = {"unit": U, "proposal_sha256": PROPOSAL_SHA256, "analyzer_sha256": a_sha,
              "package_sha256": env.package_sha256, "closure_sha256": env.closure_sha256,
              "inputs": inputs, "adjudication": used_adj, "pi_stop_record": used_pis,
              "release": "readrule.release_full: the contrast picks are reported and the withheld "
                         "free-round events are released (m:271)",
              "ended": ended, "stop_bar": stop_bar,
              "pauses": [{"kind": p.get("kind"), "at_launches": p.get("at_launches"),
                          "adjudicated": p.get("adjudication") is not None} for p in pauses],
              "counters": counters_json(dc, den, _sub(U)), "per_property_table": per_property_table(records, U),
              "gate_release": {stg: gate_release(g, U, stg) for stg, g in gates.items()},
              "quarantined": quarantined, "decisions_with_other_outcomes_known": decisions}
    if state[0] == "NOT-RUN":
        doc = {"schema": NOT_RUN_OUT_SCHEMA, "state": "NOT-RUN", "cause": state[1]["code"], "also": [],
               "reason": state[1]["reason"], "rows": unit_rows(U, ("NOT-RUN", state[1]["reason"])),
               "source": "verdicts: §5's no-first-read cause, detected from the campaign checkpoint", **common}
        refuse_beside(outs["not_run"], (outs["verdicts"], outs["secondary"]))
        status = write_texts_once([(outs["not_run"], doc)])
        lines.append(f"NOT-RUN {U}: {state[1]['reason']} ({status}: {outs['not_run'].name})")
        return status, lines, [outs["not_run"]]
    out = state[1]
    # V6-V7
    guard = guard_at_last_look(ck, U, ended)
    power = power_block(out["stats"]["n0"], out["stats"]["n1"], out["stats"]["mS"])
    sentence = verdict_sentence(U, out, counts, guard, floors, power)
    rates, tests = rates_and_tests(out, counts, guard, U)
    doc = {"schema": VERDICTS_SCHEMA, **common, "rates": rates, "tests": tests,
           "counter_rates": counter_rates(dc, den), "unit_state": "ANALYZED", "arm": {"template": c_arm,
           **outcome_json(out)}, "sham": {"template": s_arm, "domain": counts["mS"], "j": counts["j"],
           "by_map": counts["sham_by_map"], "role": "E only (tier sham, m:182-183)"},
           "counts": {k_: counts[k_] for k_ in ("launched", "domain", "prepick")},
           "floors": dict(floors), "power": power, "sentence": sentence, "guard_last_look": guard,
           "looks": every_look(ck, U), "beside": beside_blocks(records, U),
           "rows": unit_rows(U, (out["state"], None))}
    if U == "Q-F0":
        t = (out["state"], coords["OLMo-sft"], coords["OLMo-dpo"], coords["OLMo-instruct"])
        doc["tuple"] = dict(zip(UNITS, t))
        doc["olmo_states_declared"] = copy.deepcopy(states_decl)
        doc["flag"] = flag
        doc["v1_outputs"] = v1_outputs(t, reasons, bool(flag["value"]), table)
    sec = secondaries(records, U)
    refuse_beside(outs["verdicts"], (outs["not_run"],))
    status = write_texts_once([(outs["verdicts"], doc), (outs["secondary"], sec)])
    lines.append(f"VERDICTS {U}: {sentence}")
    lines.append(f"VERDICTS {U}: {status}: {outs['verdicts'].name}, {outs['secondary'].name}")
    return status, lines, [outs["verdicts"], outs["secondary"]]


def counter_rates(dc: _session.DescriptiveCounters, den: Mapping) -> list[dict]:
    """Every tabulated counter cell as a rate {num, den, domain} (m:358 "every rate with its domain")."""
    out = []
    for k_, v in sorted(dc.counts.items(), key=lambda kv: [str(x) for x in kv[0]]):
        name, key = k_[0], list(k_[1:])
        arm = key[0]
        if name in ("low_label_mass", "top1_not_label"):
            which, dk, dom = "reads", f"{arm}|{key[1]}", f"{arm} reads taken at position {key[1]}"
        elif name == "pre_pick_exclusion":
            which, dk, dom = "sessions", arm, (f"{arm} sessions launched (numerator keyed by the excluding "
                                               f"round's property, {key[-1]})")
        elif name == "post_choice_degeneracy":
            which, dk, dom = "free_rounds", f"{arm}|{key[-1]}", f"{arm} free rounds generated, property {key[-1]}"
        else:
            which, dk, dom = "rounds", f"{arm}|{key[1]}|{key[-1]}", (f"{arm} {key[1]} rounds generated, property "
                                                                    f"{key[-1]}")
        out.append({"counter": name, "key": "|".join(map(str, key)), "num": v, "den": den[which][dk],
                    "domain": dom + "; " + SCOPE_ALL})
    return out


def rates_and_tests(out: Mapping, counts: Mapping, guard: Mapping, unit: str) -> tuple[list[dict], dict]:
    """The arm's rates (each with its domain) and p's (each with its test) for the VERDICTS output."""
    c, s_ = keys.templates(unit)
    st = out["stats"]
    rates = [{"rate": "P", "num": st["k"], "den": st["n"], "domain": f"{c} domain sessions (m:308), coded on the "
              f"P-role label at the first free choice (m:306)"},
             {"rate": "P_sham", "num": st["j"], "den": st["mS"], "domain": f"{s_} domain sessions (m:308)"},
             {"rate": "share_map0", "num": st["k0"], "den": st["n0"], "domain": f"{c} domain sessions on map 0"},
             {"rate": "share_map1", "num": st["k1"], "den": st["n1"], "domain": f"{c} domain sessions on map 1"}]
    for a in (c, s_):
        rates.append({"rate": f"prepick_{a}", "num": counts["prepick"][a], "den": counts["launched"][a],
                      "domain": f"{a} campaign session records (launched); numerator excluded at the forced "
                                f"phase (stages._prepick's definition)"})
    tests: dict = {}
    if st["n"]:
        tests["p_up"] = {"p": fs(st["p_up"]), "display": dec(st["p_up"]),
                         "test": "exact one-sided binomial vs 0.5 toward clean, P(X >= k), X ~ Bin(n, 1/2); (iii) "
                                 "at alpha .01"}
        tests["p_down"] = {"p": fs(st["p_down"]), "display": dec(st["p_down"]),
                           "test": "exact one-sided binomial vs 0.5 toward corrupted, P(X <= k), X ~ Bin(n, 1/2); "
                                   "(iii) for REVERSE at alpha .01"}
        tests["dead_tail"] = {"p": fs(st["dead_tail"]), "display": dec(st["dead_tail"]),
                              "test": "P(X <= k), X ~ Bin(n, 13/20): DEAD iff < 1/40 and k < n (the two-sided "
                                      "Clopper-Pearson 95% upper bound on Delta_c < +0.15)"}
    if guard.get("reached"):
        tests["guard_fisher"] = {"p": guard["fisher"]["p"], "test": "one-sided Fisher exact, the arm's pre-pick "
                                 "exclusions vs its sham's, alpha .05, at the unit's last look (m:316)"}
        tests["guard_abs"] = {"p": guard["abs"]["p"], "test": "exact one-sided binomial of the arm's pre-pick "
                              "exclusions vs .20, alpha .05, at the unit's last look (m:316)"}
    return rates, tests


def rates_tests_problems(doc: Mapping) -> list[str]:
    """A VERDICTS output's rates each carry {num, den, domain}; its p's each {p, test}."""
    probs = []
    for r in list(doc.get("rates") or []) + list(doc.get("counter_rates") or []):
        if not (isinstance(r, Mapping) and type(r.get("num")) is int and type(r.get("den")) is int
                and isinstance(r.get("domain"), str) and r["domain"]):
            probs.append(f"rate without num/den/domain: {r!r}"[:120])
    for k_, t in (doc.get("tests") or {}).items():
        if not (isinstance(t, Mapping) and isinstance(t.get("p"), str) and isinstance(t.get("test"), str) and t["test"]):
            probs.append(f"p without its test: {k_}")
    if not doc.get("rates") or not doc.get("tests"):
        probs.append("no rates or no tests")
    return probs


def unit_rows(unit: str, state: tuple[str, str | None]) -> dict:
    """The label row(s) a unit's own output records: Q-F0 -> e2a and f1; OLMo-c -> its row."""
    word, reason = state
    if unit == "Q-F0":
        lab = (ANSWERED if word == "PASS" else PFX_F0 + "was not run: " + str(reason) if word == "NOT-RUN"
               else PFX_F0 + "did not pass: " + word)
        return {"e2a": lab, "f1": lab}
    lab = (ANSWERED if word == "PASS" else PFX_O + "was not run: " + str(reason) if word == "NOT-RUN"
           else PFX_O + "did not pass: " + word)
    return {f"olmo-{_ckpt(unit)}": lab, "state": word}


def gate_release(g: Mapping, unit: str, stage: str) -> dict:
    """A gate stage's release at VERDICTS / NOT-RUN (m:271)."""
    # PIN (Code, declared at LOCK v0.1): PIN-32 -- the G-TIME and qualification contrast first picks
    # (by role) and the released free-round events, tabulated separately from the counters of record
    # and never merged into them; G-ID sessions are not re-reported.
    recs = g["sessions"]
    c_arm = keys.templates(unit)[0]
    picks, events = [], []
    for r in recs:
        if r["template"] != c_arm:
            continue
        picks.append({"s": r["s"], "domain": bool(r["domain"]),
                      "first_pick_role": r["choices"][0]["picked_role"] if r["domain"] else None,
                      "first_free_pick_P": r["first_free_pick_P"]})
        for x in r["rounds"]:
            if x["phase"] == "free" and (x["audit"] or {}).get("claim") is not None:
                events.append({"s": r["s"], "ci": x["ci"], "claim": x["audit"]["claim"],
                               "property": x["property"]})
        exc = r.get("exclusion")
        if exc and exc.get("phase") == "free":
            events.append({"s": r["s"], "exclusion": exc.get("class"), "phase": "free"})
    dc, den = tabulate(recs, _sub(unit))
    return {"stage": stage, "stage_end": dict(g["stage_end"]), "contrast_first_picks": picks,
            "released_free_round_events": events, "counters_beside": counters_json(dc, den, _sub(unit))}


# --- NOT-RUN and posting commands -------------------------------------------------------------------
def analyzer_binding(env: Env) -> dict:
    """`not-run` and `posting`: the pinned proposal and a committed analyzer, refused (exit 2) before
    any input is read; the analyzer's, package's and closure's sha256s, for the output."""
    # PIN (Code, declared at LOCK v0.1): PIN-42 -- `not-run` and `posting` bind their outputs to the
    # analyzer as `verdicts` does short of a lock (neither has one: a Clock NOT-RUN may precede any
    # LOCK v1.0, and the posting reads none): they refuse (exit 2, before any input is read) unless
    # the proposal is the pinned v1.11 and this file is committed at HEAD with identical working-tree
    # bytes, and record analyzer_sha256, package_sha256 and closure_sha256 in {U}_NOT-RUN.json and
    # POSTING-v1_outputs.*.json, so each output names the verdict logic that wrote it (rule 27).
    # Code-added at step 8; confirmed by the seat (C5, 2026-10-10).
    pbytes = _read_bytes(env.proposal_path, "the proposal")
    if _sha256_bytes(pbytes) != PROPOSAL_SHA256:
        raise AnlRefusal("REFUSED: the proposal's sha256 is not the pinned v1.11's (PIN-31)")
    aprobs, abytes = env.committed(env.analyzer_path)
    if aprobs or abytes is None:
        raise AnlRefusal(f"REFUSED: the analyzer is not committed at HEAD: {aprobs} (PIN-42)")
    return {"analyzer_sha256": _sha256_bytes(abytes), "package_sha256": env.package_sha256,
            "closure_sha256": env.closure_sha256}


def run_not_run(unit: str, record: Path, time_p: Path | None, qual_p: Path | None, out: Path,
                env: Env) -> tuple[str, list[str], list[Path]]:
    """A Clock / dose NOT-RUN (PIN-38): validates the record, releases any gate stages, writes once."""
    # PIN (Code, declared at LOCK v0.1): PIN-38 -- `not-run` takes the Clock causes and "dose not
    # completable"; the no-first-read causes are detected from the campaign checkpoint by `verdicts`
    # (which writes {U}_NOT-RUN.json), and pending-closed-at-v2 is v2's (G-ANL-F3). Every refusal
    # (the gate stages' identity, end and stub provenance included) is decided before any gate
    # record is released (V3) or read (V4).
    if unit not in UNITS:
        raise AnlRefusal(f"REFUSED: unit {unit!r} is not a built unit")
    binding = analyzer_binding(env)
    rbytes = _read_bytes(record, "the NOT-RUN record")
    try:
        rec = validate_not_run_record(_load_json(record, "the NOT-RUN record"), unit=unit)
    except ValueError as e:
        raise AnlRefusal(f"REFUSED: NOT-RUN record: {e}")
    base, _ = parse_cause(rec["cause"])
    if base not in NOT_RUN_FROM_RECORD:
        raise AnlRefusal(f"REFUSED: cause {rec['cause']!r} is not a record cause (no-first-read: from the "
                         f"campaign by `verdicts`; pending-closed-at-v2: v2)")
    gates = {}
    for stg, p in (("time", time_p), ("qual", qual_p)):
        if p is None:
            continue
        try:
            g = resume.read_checkpoint(p)
        except SystemExit as e:
            raise AnlRefusal(f"REFUSED: the {stg} checkpoint: {e}")
        if g["identity"].get("unit") != unit or g["identity"].get("stage") != stg:
            raise AnlRefusal(f"REFUSED: the {stg} checkpoint is not {unit}/{stg}")
        if not isinstance(g.get("stage_end"), Mapping):
            raise AnlRefusal(f"REFUSED: the {stg} checkpoint has not ended")
        for e in resume.report_provenance(g):
            if STUB_MARK in json.dumps(e["record"]) and not env.allow_stub:
                raise AnlRefusal(f"REFUSED: the {stg} checkpoint was written by the self-test stub")
        gates[stg] = g
    rel = {}
    for stg, g in gates.items():
        recs = readrule.release_full(g["sessions"])
        for r in recs:
            pr = record_problems(r, unit, stg)
            if pr:
                raise AnlStop(f"STOP: a {stg} record fails V4 ({pr[0]})")
        rel[stg] = gate_release(g, unit, stg)
    doc = {"schema": NOT_RUN_OUT_SCHEMA, "unit": unit, "state": "NOT-RUN", "cause": rec["cause"],
           "also": rec["also"], "reason": rec["reason"], "date": rec["date"],
           "date_is_clock_of_record": rec["date"] == CLOCK_DATE, "detail": rec["detail"],
           "record": _file_rec(record, rbytes), "rows": unit_rows(unit, ("NOT-RUN", rec["reason"])),
           "gate_release": rel or None,
           "release": "readrule.release_full (m:271, m:358)" if rel else None,
           "decisions_with_other_outcomes_known": rec["decisions"], "proposal_sha256": PROPOSAL_SHA256,
           **binding}
    path = out / f"{unit}_NOT-RUN.json"
    refuse_beside(path, (out / f"{unit}_VERDICTS.json", out / f"{unit}_secondary.json"))
    status = write_texts_once([(path, doc)])
    return status, [f"NOT-RUN {unit}: {rec['reason']} ({status}: {path.name})"], [path]


def crosscheck_coordinate(u: str, x: str, reason: str | None, pend: Any, out_dir: Path) -> None:
    """A tuple coordinate against the unit's own outputs in out_dir (PIN-23); AnlRefusal if they disagree:
    PENDING only with neither output (pending_state); NOT-RUN only with a NOT-RUN output of the same
    reason (pending-closed-at-v2 refused at v1); an outcome state only with a VERDICTS output saying it."""
    vp, npth = out_dir / f"{u}_VERDICTS.json", out_dir / f"{u}_NOT-RUN.json"
    vex, nex = vp.is_file(), npth.is_file()
    if x == "PENDING":
        try:
            pending_state(u, {"state": "PENDING", **pend} if isinstance(pend, Mapping) else pend,
                          verdicts_exists=vex, notrun_exists=nex)
        except ValueError as e:
            raise AnlRefusal(f"REFUSED: {u} PENDING: {e}")
    elif x == "NOT-RUN":
        if not nex or vex:
            raise AnlRefusal(f"REFUSED: {u} is NOT-RUN in the tuple but has no NOT-RUN output (or has a VERDICTS "
                             f"output)")
        nr = _load_mapping(npth, f"{u}'s NOT-RUN output")
        if nr.get("reason") != reason:
            raise AnlRefusal(f"REFUSED: {u}'s reason differs from its NOT-RUN output's")
        if str(nr.get("cause", "")).startswith("pending-closed-at-v2"):
            raise AnlRefusal(f"REFUSED: {u}: pending-closed-at-v2 is the v2 posting's (G-ANL-F3)")
    else:
        if not vex or nex:
            raise AnlRefusal(f"REFUSED: {u} = {x} in the tuple but has no VERDICTS output (or has a NOT-RUN)")
        vd = _load_mapping(vp, f"{u}'s VERDICTS")
        arm = vd.get("arm")
        got = arm.get("state") if isinstance(arm, Mapping) else None
        if got != x:
            raise AnlRefusal(f"REFUSED: {u} = {x} in the tuple; its VERDICTS says {got!r}")


def posting_out_name(kind: str) -> str:
    """The posting output's file name, by table kind (PIN-25): the enumeration over the table of
    record and the re-run on the posted text (m:278, m:73) are two records of one posting."""
    if kind not in ("of-record", "posted"):
        raise ValueError(f"no posting output for a {kind!r} table")
    return f"POSTING-v1_outputs.{kind}.json"


BAR_NOT_APPLICABLE = ("C7's bar is 'The pass bar for the posting's re-run on the posted text'; Code's reading "
                      "(PIN-44): this run is over the table of record, so the bar does not apply and no rewrite "
                      "list is taken")
# the fields of an enumeration item as enumeration() writes them (PIN-21): a comparator item carries exactly these
ENUM_ITEM_KEYS = ("a", "b", "c", "clauses", "loc", "row_id", "treatments")


def rewrite_ids(data: bytes) -> list[str]:
    """The PI's rewrite list (PIN-44) from its committed bytes: {schema, posting v1, rows}, exact key
    set, rows distinct non-empty strings (may be empty); AnlRefusal otherwise."""
    try:
        doc = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as e:
        raise AnlRefusal(f"REFUSED: the rewrite list unreadable ({type(e).__name__})")
    if not isinstance(doc, Mapping) or sorted(doc) != ["posting", "rows", "schema"] \
            or doc["schema"] != REWRITES_SCHEMA or doc["posting"] != "v1":
        raise AnlRefusal(f"REFUSED: the rewrite list is {{schema {REWRITES_SCHEMA}, posting v1, rows}} (PIN-44)")
    rows = doc["rows"]
    if not isinstance(rows, list) or not all(isinstance(x, str) and x for x in rows):
        raise AnlRefusal("REFUSED: the rewrite list's rows are a list of row ids, each a non-empty string (PIN-44)")
    if len(set(rows)) != len(rows):
        raise AnlRefusal("REFUSED: the rewrite list names a row id more than once (PIN-44)")
    return list(rows)


def posting_comparator(verdicts_dir: Path, out: Path) -> tuple[dict, list[dict]]:
    """(the comparator's record, its enumeration) for the posted text's re-run (PIN-44): Q-F0's VERDICTS
    (its stored v1_outputs enumeration); where that file does not exist, the posting's own of-record
    output (its outputs' enumeration); neither -> AnlRefusal (nothing to compare with). The file must
    be what it is taken for (a VERDICTS: schema m-verdicts-v1, unit Q-F0; an of-record output: schema
    m-posting-v1-outputs-v1, table_kind of-record); an item is refused unless it is an object carrying
    exactly enumeration()'s fields (str row_id, list clauses), and a row id named twice is refused; the
    record names the comparator's kind, path, sha256 and the tuple it stores (informational)."""
    vp, op = verdicts_dir / "Q-F0_VERDICTS.json", out / posting_out_name("of-record")
    if vp.is_file():
        kind, p, what, blk_key = "verdicts", vp, "Q-F0's VERDICTS", "v1_outputs"
        ident = {"schema": VERDICTS_SCHEMA, "unit": "Q-F0"}
    elif op.is_file():
        kind, p, what, blk_key = "posting-of-record", op, "the posting's of-record output", "outputs"
        ident = {"schema": POSTING_OUT_SCHEMA, "table_kind": "of-record"}
    else:
        raise AnlRefusal("REFUSED: the posted text's re-run has nothing to compare with -- neither Q-F0's VERDICTS "
                         "(verdicts-dir) nor the posting's of-record output (out) exists (PIN-44)")
    data = _read_bytes(p, what)
    try:
        doc = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as e:
        raise AnlRefusal(f"REFUSED: {what} unreadable ({type(e).__name__})")
    if not (isinstance(doc, Mapping) and all(doc.get(k_) == v_ for k_, v_ in ident.items())):
        raise AnlRefusal(f"REFUSED: {what} is not what it is taken for ("
                         + ", ".join(f"{k_} {v_}" for k_, v_ in ident.items()) + "; PIN-44)")
    blk = doc.get(blk_key)
    en = blk.get("enumeration") if isinstance(blk, Mapping) else None
    if not (isinstance(en, list) and all(isinstance(it, Mapping) and sorted(it) == list(ENUM_ITEM_KEYS)
                                         and isinstance(it.get("row_id"), str)
                                         and isinstance(it.get("clauses"), list) for it in en)):
        raise AnlRefusal(f"REFUSED: {what} records no v1 enumeration to compare with ({blk_key}.enumeration; PIN-44)")
    if len({it["row_id"] for it in en}) != len(en):
        raise AnlRefusal(f"REFUSED: {what} names a row id more than once in its enumeration (PIN-44)")
    tup = doc.get("tuple")
    return ({"kind": kind, "path": _repo_rel(p), "sha256": _sha256_bytes(data),
             "tuple": dict(tup) if isinstance(tup, Mapping) else None}, [dict(it) for it in en])


def posting_bar(outputs: Mapping, flag: bool, table: Mapping, comparator: Mapping, expected_from: Sequence[Mapping],
                rewrites: Sequence[str], tuple_rec: Mapping) -> dict:
    """C7's bar on the posted text and the comparison with the comparator's enumeration with the PI's
    rewrites applied (PIN-44). The comparison is reported; it does not decide the verdict."""
    # PIN (Code, declared at LOCK v1.0): PIN-44 -- the seat's round-2 item 3 (a) (lock §9.6): "the
    # `posting` command renders PASS/FAIL against the bar (PASS iff the enumeration under (a), (b) and (c)
    # is empty and the dose note is present iff the flag); and it compares the posting re-run's
    # enumeration with the VERDICTS enumeration with the PI's rewrites applied (a declared input: the
    # rewrite list, by row id), reporting any row that differs." Code's readings: the bar is rendered on
    # a posted-kind run only (C7: "The pass bar for the posting's re-run on the posted text"); the bar's
    # second conjunct ("the dose note is present iff the flag") is computed from dose_note's own status
    # (the table carries a dose-note span iff dose_note(True, table) is 'carried'), not only through
    # clause (c); expected = the comparator's rows less the rewrite
    # list's; changed = in both, the two enumeration items differing in a field other than loc, moved = in
    # both, differing in loc alone (informational; differs does not count it); the comparator's stored
    # tuple is recorded beside this run's (informational); a FAIL writes nothing, prints its record
    # (posting_fail_lines) and exits 5.
    enum = [json.loads(json.dumps(it)) for it in outputs["enumeration"]]
    present = dose_note(True, table)["status"] == "carried"
    iff = present == flag
    residue = [it["row_id"] for it in enum]
    rw = set(rewrites)
    expected = [it for it in expected_from if it["row_id"] not in rw]
    exp_by = {it["row_id"]: it for it in expected}
    act_by = {it["row_id"]: it for it in enum}
    only_actual = [r for r in residue if r not in exp_by]
    only_expected = [it["row_id"] for it in expected if it["row_id"] not in act_by]
    differ = [{"row_id": r, "expected": exp_by[r], "actual": act_by[r]}
              for r in residue if r in exp_by and exp_by[r] != act_by[r]]

    def sans_loc(it_: Mapping) -> dict:
        return {k_: v_ for k_, v_ in it_.items() if k_ != "loc"}
    changed = [d_ for d_ in differ if sans_loc(d_["expected"]) != sans_loc(d_["actual"])]
    moved = [d_ for d_ in differ if sans_loc(d_["expected"]) == sans_loc(d_["actual"])]
    in_comp = {it["row_id"] for it in expected_from}
    comparison = {"comparator": dict(comparator), "same_tuple": comparator.get("tuple") == dict(tuple_rec),
                  "only_actual": only_actual, "only_expected": only_expected,
                  "changed": changed, "moved": moved,
                  "rewrites_not_in_comparator": [r for r in rewrites if r not in in_comp],
                  "differs": bool(only_actual or only_expected or changed)}
    return {"applies": True, "verdict": "PASS" if (not enum and iff) else "FAIL", "enumeration_empty": not enum,
            "dose_note_iff_flag": iff, "residue": residue, "comparison": comparison}


def posting_bar_lines(bar: Mapping) -> list[str]:
    """The bar's stdout lines (PIN-44): the verdict, the residue by row id, the comparison."""
    cmp_ = bar["comparison"]
    ch = ", ".join(c["row_id"] for c in cmp_["changed"]) or "none"
    mv = ", ".join(m_["row_id"] for m_ in cmp_["moved"]) or "none"
    return [f"POSTING v1: {bar['verdict']} against C7's bar (PIN-44): enumeration empty {bar['enumeration_empty']}, "
            f"dose note present iff the flag {bar['dose_note_iff_flag']}"
            + ("; nothing written" if bar["verdict"] == "FAIL" else ""),
            f"POSTING v1: residue by row id ({len(bar['residue'])}): {', '.join(bar['residue']) or 'none'}",
            f"POSTING v1: comparison with the {cmp_['comparator']['kind']} enumeration with the PI's rewrites applied "
            f"(sha256 {cmp_['comparator']['sha256'][:16]}; its tuple this run's {cmp_['same_tuple']}): differs "
            f"{cmp_['differs']}; only_actual {cmp_['only_actual']}; only_expected {cmp_['only_expected']}; changed "
            f"{ch}; moved {mv}; rewrites not in the comparator {cmp_['rewrites_not_in_comparator']}"]


def posting_fail_lines(bar: Mapping, enum: Sequence[Mapping], expected_from: Sequence[Mapping], inputs: Mapping,
                       flag: Mapping, binding: Mapping, declared: Mapping) -> list[str]:
    """A FAIL's record (PIN-44): it writes nothing, so its stdout is the record of that step -- every
    residue row in full as the enumeration carries it (enumeration()'s fields only: no tag, pick or
    free-round event is in an item), each comparison set (moved included) with its rows in full, and the
    unwritten record's declared tuple (with its reasons and pending), inputs (path and sha256 each),
    comparator, flag and binding. Deterministic (sorted keys)."""
    def js(x: Any) -> str:
        return json.dumps(x, sort_keys=True)
    cmp_ = bar["comparison"]
    enum_n = [json.loads(json.dumps(it)) for it in enum]
    act_by = {it["row_id"]: it for it in enum_n}
    exp_by = {it["row_id"]: it for it in expected_from}
    out = [f"POSTING v1: residue {i} of {len(enum_n)}, {it['row_id']}: {js(it)}" for i, it in enumerate(enum_n, 1)]
    out += [f"POSTING v1: comparison only_actual {r}: {js(act_by[r])}" for r in cmp_["only_actual"]]
    out += [f"POSTING v1: comparison only_expected {r}: {js(exp_by[r])}" for r in cmp_["only_expected"]]
    out += [f"POSTING v1: comparison changed {c['row_id']}: expected {js(c['expected'])}; actual {js(c['actual'])}"
            for c in cmp_["changed"]]
    out += [f"POSTING v1: comparison moved {m_['row_id']}: expected {js(m_['expected'])}; actual "
            f"{js(m_['actual'])}" for m_ in cmp_["moved"]]
    out.append(f"POSTING v1: comparison rewrites not in the comparator: {js(cmp_['rewrites_not_in_comparator'])}")
    out.append(f"POSTING v1: the unwritten record: declared {js(declared)}; inputs {js(inputs)}; comparator "
               f"{js(cmp_['comparator'])}; flag {js(flag)}; binding {js(binding)}")
    return out


def run_posting(tuple_p: Path, sentences: Path, flag_source: Path, verdicts_dir: Path, out: Path,
                env: Env, rewrites: Path | None = None) -> tuple[str, list[str], list[Path]]:
    """§7's v1 outputs under the declared tuple, cross-checked against existing unit outputs; it
    never opens a checkpoint (PIN-23). On the posted text, C7's bar (PIN-44): a FAIL raises
    AnlPostingFail (exit 5) and writes nothing."""
    # PIN (Code, declared at LOCK v0.1): PIN-23 -- the tuple is an explicit input, computed at Q-F0's
    # VERDICTS and again at the posting under the states then standing; each coordinate is cross-
    # checked against the unit's VERDICTS or NOT-RUN output; each entry records the tuple it used.
    binding = analyzer_binding(env)
    tb = _read_bytes(tuple_p, "the tuple")
    doc = _load_json(tuple_p, "the tuple")
    if not isinstance(doc, Mapping) or sorted(doc) != ["pending", "posting", "reasons", "schema", "tuple"] \
            or doc["schema"] != TUPLE_SCHEMA or doc["posting"] != "v1":
        raise AnlRefusal(f"REFUSED: the tuple is {{schema {TUPLE_SCHEMA}, posting v1, tuple, reasons, pending}}")
    tt = doc["tuple"]
    if not isinstance(tt, Mapping) or sorted(tt) != sorted(UNITS):
        raise AnlRefusal(f"REFUSED: the tuple names exactly {UNITS}")
    try:
        t = check_tuple(tuple(tt[u] for u in UNITS))
    except ValueError as e:
        raise AnlRefusal(f"REFUSED: {e}")
    reasons, pend = doc["reasons"], doc["pending"]
    if not isinstance(reasons, Mapping) or not isinstance(pend, Mapping):
        raise AnlRefusal("REFUSED: reasons and pending are objects")
    if sorted(reasons) != sorted(u for u, x in zip(UNITS, t) if x == "NOT-RUN") \
            or sorted(pend) != sorted(u for u, x in zip(UNITS, t) if x == "PENDING"):
        raise AnlRefusal("REFUSED: reasons name exactly the NOT-RUN units, pending exactly the PENDING ones")
    for u, x in zip(UNITS, t):
        crosscheck_coordinate(u, x, reasons.get(u), pend.get(u), verdicts_dir)
    sp, sbytes = env.committed(sentences)
    if sp or sbytes is None:
        raise AnlRefusal(f"REFUSED: the sentence table is not committed at HEAD: {sp}")
    table = _load_json(sentences, "the sentence table")
    tp = table_problems(table, read_repo_file=env.read_repo_file)
    if tp or table.get("kind") not in ("of-record", "posted"):
        raise AnlRefusal(f"REFUSED: the sentence table is refused: {tp or ['a placeholder serves G-ANL-F0 only']}")
    for qv in (verdicts_dir / "Q-F0_VERDICTS.json", verdicts_dir / "Q-F0_NOT-RUN.json"):
        # PIN-40: once Q-F0's LOCK v1.0 was reached, its `verdicts` output (VERDICTS, or the
        # no-first-read NOT-RUN a locked unit gets) records the table of record it read; the
        # posting's of-record table is that one (LOCK-m-F0 v1.0's, m:278, m:286). A Clock NOT-RUN
        # record (`not-run`) carries none: the table is built at the posting.
        if table["kind"] != "of-record" or not qv.is_file():
            continue
        rec_sha = ((_load_mapping(qv, f"Q-F0's {qv.stem[5:]} output").get("inputs") or {}).get("sentences")
                   or {}).get("sha256")
        if (rec_sha is not None or qv.name.endswith("_VERDICTS.json")) and rec_sha != _sha256_bytes(sbytes):
            raise AnlRefusal(f"REFUSED: the table of record is not the one Q-F0's {qv.stem[5:]} output read "
                             f"(LOCK-m-F0 v1.0's, m:286; PIN-40)")
    inputs = {"tuple": _file_rec(tuple_p, tb), "sentences": _file_rec(sentences, sbytes)}
    posted = table["kind"] == "posted"
    rw_ids: list[str] = []
    comp_rec = comp_rows = None
    if not posted:                       # PIN-44: C7's bar is the posted text's; no rewrite list here
        if rewrites is not None:
            raise AnlRefusal("REFUSED: --rewrites is the posted text's input (C7's bar, PIN-44); the run over the "
                             "table of record takes none")
    else:
        if rewrites is None:
            raise AnlRefusal("REFUSED: the re-run on the posted text needs --rewrites, the PI's rewrite list by row "
                             "id (C7's bar, PIN-44)")
        if Path(rewrites).is_dir():              # PIN-44: an empty --rewrites is a given path, read as '.'
            raise AnlRefusal(f"REFUSED: the rewrite list unreadable (the path {str(rewrites)!r} names a directory, "
                             f"not a file; an empty --rewrites is read as '.') (PIN-44)")
        rwp, rwb = env.committed(rewrites)
        if rwp or rwb is None:
            raise AnlRefusal(f"REFUSED: the rewrite list is not committed at HEAD: {rwp} (PIN-44)")
        rw_ids = rewrite_ids(rwb)
        inputs["rewrites"] = _file_rec(rewrites, rwb)
        comp_rec, comp_rows = posting_comparator(verdicts_dir, out)
    flag = flag_of_record(flag_source, env.committed)
    outputs = v1_outputs(t, reasons, bool(flag["value"]), table)
    bar = (posting_bar(outputs, bool(flag["value"]), table, comp_rec, comp_rows, rw_ids, dict(zip(UNITS, t)))
           if posted else {"applies": False, "reason": BAR_NOT_APPLICABLE})
    doc_out = {"schema": POSTING_OUT_SCHEMA, "posting": "v1", "tuple": dict(zip(UNITS, t)),
               "reasons": dict(reasons), "pending": dict(pend), "flag": flag, "inputs": inputs,
               "table_kind": table["kind"], "outputs": outputs, "bar": bar,
               "proposal_sha256": PROPOSAL_SHA256, **binding}
    head = (f"POSTING v1: tuple {t}; ceiling {doc_out['outputs']['ceiling']['name']}; "
            f"{len(doc_out['outputs']['enumeration'])} enumerated rows")
    if posted and bar["verdict"] == "FAIL":
        raise AnlPostingFail([head + " on the posted text"] + posting_bar_lines(bar)
                             + posting_fail_lines(bar, outputs["enumeration"], comp_rows, inputs, flag, binding,
                                                  {k_: doc_out[k_] for k_ in ("tuple", "reasons", "pending")}), bar)
    path = out / posting_out_name(table["kind"])
    status = write_texts_once([(path, doc_out)])
    return status, [f"{head} ({status}: {path.name})"] + (posting_bar_lines(bar) if posted else []), [path]


# --- the PIN register (repeated in the G-ANL-F0 entry) --------------------------------------------
PINS = {
    "PIN-1": "The analyzer of m:278 is the single file scripts/m_analyze.py: every outcome, unit-state, "
             "sentence, counter, secondary and posting computation lives in it. The analyzer's sha256, "
             "package_sha256 and the import closure outside the package together bind the verdict logic: "
             "the closure is computed mechanically in a fresh interpreter that imports this file and the "
             "declared lazy verdict-path module (valence_core.m.stages) -- sha256 of __file__ of every "
             "loaded valence_core.* module outside valence_core/m, plus every repository data file "
             "opened during those imports -- recorded in G-ANL-F0.json with its sha256; a VERDICTS run "
             "whose closure sha256 is not named in its lock is refused (exit 2). stages is imported "
             "lazily on the verdict path; guard, testing, corr, scaffold and schedule in the battery "
             "only. The gate-line files (the proposal, CLAUDE.md, this file) are logged by "
             "stages.gate_line, not bound by the closure. Step 8 edits nothing under valence_core/.",
    "PIN-2": "Every decision is exact (Fraction); floats are refused. (iii) is P <= alpha, which equals "
             "P < alpha because a dyadic P never equals 1/100 (asserted at n = 80, 96, 213). DEAD iff "
             "k < n and P(Bin(n, 13/20) <= k) < 1/40, the exact form of 'CI upper bound on Delta_c < "
             "+0.15' (strict; k = n is never DEAD). Displayed Clopper-Pearson bounds are exact "
             "bisection on Fractions to width < 1e-8, printed half-up to 4 places, and never decide.",
    "PIN-3": "Attained power of record = P(PASS under (i)-(iii) at alpha .01), enumerated exactly at "
             "m:190's base case at the realised n: the arm's realised domain n split floor(n/2) on map 0 "
             "and ceil(n/2) on map 1 at clean share .70, the sham pooled at its realised domain m at .5. "
             "The figure at the realised map split is reported beside, labelled. Both are 0 when a map "
             "or the sham is empty. Descriptive only. Accepted by the seat (C6, 2026-10-10) as the "
             "declared base-case computation, re-derived at G-PWR (step 15) with the planned floors, where "
             "the realised-n figure becomes the figure of record (m:190).",
    "PIN-4": "The verdict sentence is the clauses of SENTENCE_TEMPLATES in order (state or 'no read "
             "obtained' with its sub-reason; counts per map; P, Delta_c, CP CI; E and P_arm - P_sham; "
             "both one-sided p's; REVERSE's phrase; pre-pick rates of arm and sham; the guard at the "
             "unit's last look; shortfall and attained power -- the figure of record, the realised-split figure "
             "beside -- only when an arm is below its floor, m:247). Attained power is always in the VERDICTS "
             "output (m:190). The absolute guard prints 'fired / not fired (binding)' on Qwen and "
             "'P <= alpha / P > alpha (reported only)' on OLMo.",
    "PIN-5": "NOT-RUN cause codes and reason phrases as NOT_RUN_CAUSES tables them (Code-authored, "
             "accepted with their precedence by the seat, C6, 2026-10-10; the PI rewrites at posting). The record names one primary cause "
             "(the earliest) and lists the others in `also`; the label prints the primary. The <stage> "
             "of clock:gate-stopped and clock:not-locked is one of gate_stop_stages(unit): Q-F0 G-PORT, "
             "G-CAL, G-SHAPE-F0, G-ANL-F0, G-TIME-F0, G-ID-F0m, G-F0m-Qwen (G-ID-F0m's divergence only "
             "sends Q-F0 uncached, m:281, but a hair-trigger fire or a G-VER failure stops it, m:271, "
             "m:284); OLMo-c G-CAL (it serves all units, m:176, m:276; the OLMo track starts at step 9, "
             "m:300, m:358), G-SHAPE-F0, G-ANL-F0, G-TIME-OLMo-c, G-F0m-OLMo-c. clock:not-locked is the "
             "residual Clock cause (m:347 is unconditional): the blocking stage had not reached its end "
             "(a pause awaiting the seat's adjudication, m:302; a gate still open) -- confirmed by the "
             "seat (C1, 2026-10-10): m:324's parenthetical ends 'or any reason', so its list is not "
             "exhaustive by its own words; clock:not-locked:<stage> is a reading of that clause, not an "
             "addition to it.",
    "PIN-6": "PENDING is a declared input {state, substate, clock_passed, date}, substate in "
             "{unlocked-before-D_O, locked-running, restarting-after-box-change, "
             "awaiting-verdicts-session}; refused for Q-F0, refused with clock_passed for "
             "unlocked-before-D_O, refused where a VERDICTS or NOT-RUN output exists. clock_passed and "
             "the date the comparison was made on (YYYY-MM-DD) are recorded as given -- in the posting "
             "output's pending block and in Q-F0's VERDICTS (olmo_states_declared). The boundary-day "
             "comparison is settled by the seat (C7, 2026-10-10): a unit's LOCK v1.0 is 'committed by "
             "its Clock date' iff the commit's committer date, in UTC, falls on or before the Clock date "
             "(the day inclusive, to 23:59:59 UTC); it remains a declared input.",
    "PIN-7": "VERDICTS reads one unit's declared campaign, G-TIME and qualification checkpoints after "
             "refusals decided before any pick is read (unit; pinned proposal; this file and the lock "
             "committed at HEAD; analyzer, package and closure sha256s named in the lock; the decisions "
             "input; Q-F0's table of record and OLMo states), then on structure (ended, no end pending, "
             "an adjudicated last pause, a G-VER or PI-stop-disposed STOP, the lock's sha, floors recorded for "
             "both arms, one backend identifier across launching invocations, an OLMo identity carrying its pod id -- a pod "
             "splice is refused at write time by resume -- and no stub provenance). It calls "
             "readrule.release_full, writes once, and prints after writing. A unit NOT-RUN by §5's "
             "no-first-read cause gets {U}_NOT-RUN.json from this command.",
    "PIN-8": "Confirmed by the seat (C2, 2026-10-10; m:316's path -- an adjudication 'may end in a PI "
             "stop (terminal, analyzed as obtained)' -- applied to the hair triggers): a campaign ended by "
             "a scaffold_absorption hair-trigger STOP is refused unless a declared PI-stop record "
             "(m-pi-stop-record-v1 naming the unit and the campaign checkpoint's sha256; path and sha256 "
             "recorded) is supplied; with it, m:324's PI-stop rule applies (no first read: NOT-RUN "
             "no-first-read:pi-stop; otherwise analyzed as obtained). Whether an adjudicated fire may "
             "instead resume is for the adjudication, if one arises; nothing is built for it. A G-VER "
             "STOP is a PI stop by m:284.",
    "PIN-9": "Confirmed by the seat (C3, 2026-10-10): VERDICTS refuses while the campaign's last pause is "
             "unadjudicated; the seat's adjudication enters as a declared --adjudication file "
             "(m-verdicts-adjudication-v1 naming the unit, the checkpoint's sha256 and the pause's kind and "
             "launch count), its path and sha256 recorded. Code never self-adjudicates. The seat's C9(i): "
             "the adjudication of a fired end look on a terminal campaign enters as that declared "
             "--adjudication file; stages.py need not record it. Code's reading, flagged for the seat: a "
             "pause raised at a STOP (when the end look the seat's C9(ii) orders there fires; the pause is "
             "Code's application of m:330) is the campaign's last pause, so C3's route covers it too.",
    "PIN-10": "The seat's C9(ii) (2026-10-10; m:330's 'at the end' includes an end by STOP): 'the unit's "
              "last look' = campaign.end_look, which stages evaluates and records at COMPLETE, CAP, PI-STOP "
              "and at the STOP point alike; at a STOP the sentence names it as the STOP's ('the end look at "
              "the STOP (at N launches)', or 'look k at N launches, the end look at the STOP' where the end "
              "look is the cadence look recorded at N). A STOP-ended campaign with a launch recorded and no "
              "end look is a structural refusal at V2, before V3 releases anything (not written by the "
              "lock's package); with no launch recorded, 'no look reached'. A fired end look at a STOP is a "
              "pause (m:330's 'A fired bar pauses', Code's application) and takes PIN-9's path (Code's "
              "reading of C3, flagged for the seat; see PIN-9). Guard "
              "results are selected by the unit's declared guard bars. "
              "No end-of-data guard is recomputed in the analyzer. Neither moves a verdict (m:316).",
    "PIN-11": "Counters are declared as m:314's two lists in full (verified verbatim against m:314 and "
              "against audit.DECLARED_COUNTERS_* plus the [Q-F3] entry); the [Q-F3] counter is declared, "
              "scoped to Q-F3, not tabulated at Q-F0. The counters of record are over the unit's "
              "campaign sessions, excluded included, mirroring audit.tally's claim logic (summed over "
              "property they equal audit.tally); G-TIME and qualification sessions are tabulated "
              "separately as m:271's release.",
    "PIN-12": "Property keys: round counters by round.property; session counters by the excluding "
              "round's property; read counters by arm and read position (no property). Settled by the seat "
              "(C7, 2026-10-10; G-PORT A5), where the interim text had named sessions_excluded_any_phase "
              "the like-for-like column: f1's 7-vs-1 refers to the per-property table's pre-pick "
              "column (sessions excluded before the first read, by property); sessions_excluded_any_phase "
              "is reported beside it -- fixed, no longer interim. Whole-session validity: lenient = "
              "complete, no exclusion, no hair trigger; strict adds no claim in any round.",
    "PIN-13": "Secondaries (a), (b), (d) and (e) are built now (m:312, pre-registered), in a separate "
              "{unit}_secondary.json, with the 20-event floor and count-only below it. 'Valid through "
              "position p' = the choice at p was made and no exclusion-bearing event preceded it. (d)'s "
              "habit identity is habit.break_rates(<the arm's domain sessions>) (no `arm` key; frame()'s "
              "e2d powered-effect block omitted), b+, bs and the weighted form recomputed in Fractions; "
              "the weighted form + 1/2 equals the arm's P exactly.",
    "PIN-14": "The analyzer of record for a unit is the blob hashed in that unit's LOCK v1.0; the lock "
              "names the analyzer's sha256, package_sha256 and the closure sha256, each asserted. When "
              "HEAD's three equal the lock's, VERDICTS runs at HEAD with no worktree; otherwise from a "
              "worktree of the lock commit with every data input and output passed as an absolute path "
              "into the main tree, and only on the PI's word for the worktree (not implemented at step 8). "
              "G-ANL-F3's versioning (m:291) is deferred by the seat to before step 19 (C7, 2026-10-10).",
    "PIN-15": "Label slots: the outcome as the §5 state word; the reason as the PIN-5 phrase; one bracket "
              "alternative, plain text.",
    "PIN-16": "'[passing stages]' = 'the {A} stage' or 'the {A} or {B} stage', in lineage order, with names "
              "as m:338 spells them (SFT, DPO, instruct).",
    "PIN-17": "Confirmed by the seat (C4, 2026-10-10): §8.1 text = one clause per control with a v1 "
              "coordinate (A0, A0-OLMo-sft/-dpo/-instruct) with m:343's tokens; A1 belongs to §8.2, 'open' "
              "at v1; re-verified against the placed preprint at LOCK v1.0.",
    "PIN-18": "The ceiling output is its name and its m:334 title, verbatim.",
    "PIN-19": "Flag of record TRUE iff data/m/gates/G-CAL_model-free.json is committed at HEAD and identical "
              "in the working tree, has schema m-gcal-model-free-v1, and carries an f1_012 block; "
              "existence-keyed; renders_sha_matches_calib recorded beside, not part of the flag. The "
              "battery runs both values.",
    "PIN-20": "Sentence table schema m-posting-sentences-v1, paths and placeholder as PLACEHOLDER_SPEC / "
              "PLACEHOLDER_LOC; validation as table_problems (the roster-word refusal dropped, the "
              "forbidden-literal check kept). One row per sentence: loc = {line, sentence, section}, "
              "sentence the 1-based ordinal of the sentence on its preprint line, so two sentences of one "
              "line are two rows; rows in strictly increasing (line, sentence) order; on an of-record or "
              "posted table each row's text begins on its declared preprint line (it may run on) and "
              "rows sharing a line occur there in sentence order. The table of record's classification "
              "is Code's, outcome-blind at LOCK v1.0, values-checked.",
    "PIN-21": "The enumeration procedure of enumeration(); (c) is two-sided on m:349's own 'iff': strike "
              "when the flag is false, carry when the flag is true and no dose-note row exists.",
    "PIN-22": "S1 ('Answered, as recognition') counts as Answered under clause (a).",
    "PIN-23": "The tuple is an explicit input, computed at Q-F0 VERDICTS and again at the posting; each "
              "entry records the tuple it used. Each coordinate is cross-checked against the unit's own "
              "outputs (at Q-F0 VERDICTS for the declared OLMo states, and at the posting): PENDING only with "
              "neither output, NOT-RUN only with a NOT-RUN output of the same reason, an outcome state only "
              "with a VERDICTS output saying it. The posting never opens a checkpoint.",
    "PIN-24": "The battery reaches every per-arm outcome per unit, the full 5 x 6^3 product under both flag "
              "values (the flag an input, not a coordinate), and a reader-path subset built by the "
              "production writers on the stub. The 1,080-tuple pass uses 'clock:pi-declined' for every "
              "NOT-RUN coordinate; every other code is exercised in the NR group, and a further pass over "
              "the 1,080 tuples gives each unit a distinct reason (per-unit routing against the oracle). Each "
              "flag value's T10 tallies are taken from that flag's own outputs. A coverage registry and a "
              "fixed check count make any skip a failure.",
    "PIN-25": "Outputs: data/m/gates/G-ANL-F0.json (step 8; the 2,160-row output table is not committed -- "
              "its sha256 is recorded and it regenerates byte-identically); data/m/verdicts/"
              "{unit}_VERDICTS.json, _secondary.json, _NOT-RUN.json, and the posting's "
              "POSTING-v1_outputs.of-record.json (the enumeration over the table of record) and "
              "POSTING-v1_outputs.posted.json (its re-run on the posted text, m:278, m:73) -- named by the "
              "table kind, so both records of one posting are written. The .gitignore admit block (and "
              "any -diff) for data/m/verdicts/ is deferred to the commit that first writes there. All "
              "write-once, timestamp-free, json_text(indent=1).",
    "PIN-26": "Exit codes: --selftest 0/1; ganl 0 written or identical, 2 refused, 4 STOP (a closure that "
              "cannot be computed included -- every SystemExit of ganl maps through the same rule); "
              "verdicts, not-run, posting 0 written or identical, 2 refused (decided before any pick is "
              "interpreted, write-once or exclusivity, or an input that is not a JSON object); posting also 5: "
              "FAIL against C7's bar on the posted text's re-run, nothing written (PIN-44; the code is Code's, "
              "added at LOCK v1.0); 4 STOP (a content assertion after reading; any other SystemExit maps to 4).",
    "PIN-27": "The abstract clause is emitted verbatim even where its host sentence is enumerated under (a); "
              "the entry notes that it can dangle.",
    "PIN-28": "The analyzer runs guard.check_call_sites and the forbidden-literal grep over itself in its "
              "battery, both directions.",
    "PIN-29": "During --selftest and ganl, an open hook (builtins.open, io.open, Path.open/read_bytes/"
              "read_text) refuses any path under data/m/ckpt, data/m/reports, data/m/verdicts or "
              "results/raw; the no-canonical-write snapshot hashes data/m files outside those directories "
              "and takes only os.stat of files inside them (never their bytes).",
    "PIN-30": "STUB_MARK provenance is accepted only by the battery's internal path. The CLI refuses it.",
    "PIN-31": "The proposal sha256 is pinned in the analyzer. Every m-verbatim constant is verified against "
              "the proposal file at run time.",
    "PIN-32": "VERDICTS and NOT-RUN outputs carry the G-TIME and qualification contrast first picks (by role) "
              "and the released free-round events from {unit}_time.json and {unit}_qual.json, tabulated "
              "beside, never merged into the counters of record. G-ID sessions are not re-reported.",
    "PIN-33": "Pre-pick exclusion rate = sessions excluded at the forced phase (stages._prepick's "
              "definition, asserted equal both directions) / campaign session records of the arm "
              "(launched) -- the guard's own denominator; a G-VER-quarantined record is reported beside, "
              "not counted.",
    "PIN-34": "A record whose domain disagrees with its forced rounds, or whose first_free_pick_P disagrees "
              "with its first choice, is a STOP (exit 4), not a refusal.",
    "PIN-35": "m:318's decisions taken with another unit's outcome known are a required declared input "
              "(the not-run record's key; verdicts' --decisions file), [{decision, date, other_unit, "
              "other_state}] (may be empty), carried verbatim into {U}_VERDICTS.json / {U}_NOT-RUN.json; "
              "a missing key is refused. other_unit is any other unit of m:324 (Q-F0, an OLMo checkpoint "
              "or Q-F3); other_state its known outcome -- a built unit's §5 state word or NOT-RUN, Q-F3's "
              "'NOT-RUN' or {A1, A2, A3[, A3*]} in m:326's and m:340's words; PENDING is refused (no "
              "VERDICTS exist, m:318).",
    "PIN-36": "Signed values print as an ASCII sign ('+' for zero) then bars._dec of the magnitude, half-up "
              "on the magnitude: -1/20 -> '-0.0500', +1/20 -> '+0.0500'.",
    "PIN-37": "Write-once supersession: an artifact that must be replaced (a seat strike of a PIN, a "
              "re-specified input) is moved aside by hand with `git mv` to a dated superseded name on the "
              "seat's ruling, recorded in an entry; a re-run on unchanged inputs is byte-identical.",
    "PIN-38": "`not-run` takes the Clock causes and 'dose not completable'; no-first-read causes come from "
              "the campaign checkpoint through `verdicts`; pending-closed-at-v2 is refused at v1 (v2's, "
              "G-ANL-F3). Its refusals (a gate stage's unit / stage, end and stub provenance included) are "
              "decided before any gate record is released or read.",
    "PIN-39": "The canonical `ganl` run writes G-ANL-F0.json against committed blobs only (rule 27): the "
              "analyzer, the placeholder, the proposal, every valence_core/m/*.py and every closure file must "
              "be committed at HEAD with identical working-tree bytes, else exit 2 before the battery; a "
              "--out test directory is exempt.",
    "PIN-40": "LOCK-m-F0 v1.0 hashes the sentence table of record and the preprint of record (m:286): Q-F0's "
              "VERDICTS refuses unless the lock text names the table's sha256 and its preprint's sha256. "
              "The posting's of-record table, when a Q-F0 output of `verdicts` records one (its VERDICTS, "
              "or a locked unit's no-first-read NOT-RUN), must be that table (and so the lock's); on Q-F0's "
              "Clock NOT-RUN path the table of record is built at the posting (m:278, m:286) and no lock "
              "binds it; a posted-kind table (the re-run on the posted text) is hashed by no lock.",
    "PIN-41": "m:324's exclusivity is enforced at write time: `verdicts` never writes {U}_VERDICTS.json beside "
              "an existing {U}_NOT-RUN.json nor {U}_NOT-RUN.json beside an existing {U}_VERDICTS.json / "
              "_secondary.json, and `not-run` never writes beside an existing {U}_VERDICTS.json (exit 2, "
              "nothing written); the posting refuses a unit carrying both.",
    "PIN-42": "`not-run` and `posting` bind their outputs as `verdicts` does short of a lock (neither has "
              "one): each refuses (exit 2, before any input is read) unless the proposal is the pinned "
              "v1.11 and this file is committed at HEAD with identical working-tree bytes, and records "
              "analyzer_sha256, package_sha256 and closure_sha256 in {U}_NOT-RUN.json / "
              "POSTING-v1_outputs.*.json (rule 27). Code-added at step 8 (a binding the spec does not "
              "state); confirmed by the seat (C5, 2026-10-10).",
    "PIN-43": "every declared date (a NOT-RUN record's, a declared OLMo NOT-RUN state's, a PENDING "
              "declaration's Clock comparison, a decision's) is an ASCII YYYY-MM-DD that is a real calendar "
              "date (non-ASCII digits, the basic and week forms and impossible days refuse); a NOT-RUN "
              "record's and a declared NOT-RUN state's date are checked whatever the cause. Confirmed by "
              "the seat (C5, 2026-10-10), Code's fixes ratified. For a no-first-read NOT-RUN declared in "
              "--olmo-states the date is the calendar date of the terminal event that made the NOT-RUN "
              "final -- the PI stop, the G-VER STOP, or the day the cap was reached -- as that unit's entry "
              "records it; where the unit's own output carries no date, the declarer supplies the entry's.",
    "PIN-44": "Declared at LOCK v1.0, built at step 15 on the seat's round-2 item 3 (a) (lock §9.6): \"the "
              "`posting` command renders PASS/FAIL against the bar (PASS iff the enumeration under (a), (b) and "
              "(c) is empty and the dose note is present iff the flag); and it compares the posting re-run's "
              "enumeration with the VERDICTS enumeration with the PI's rewrites applied (a declared input: the "
              "rewrite list, by row id), reporting any row that differs.\" The bar reads the posted table's "
              "declared classification (the seat: \"no analyzer reads prose\"). Code's readings: C7's bar is "
              "\"The pass bar for the posting's re-run on the posted text\", so it is rendered on a run whose "
              "table kind is posted; an of-record run records it as not applicable, with that reason, and takes "
              "no rewrite list (an empty --rewrites is a given path: refused there, and refused as unreadable "
              "on a posted run). The rewrite list is a declared input, posting --rewrites PATH: {schema "
              "m-posting-rewrites-v1, posting v1, rows: [row_id, ...]}, exact key set, rows distinct non-empty "
              "strings (may be empty); required on a posted run and refused on an of-record run (exit 2); "
              "committed at HEAD with identical working-tree bytes (the sentence table's rule) and read only "
              "after PIN-42's binding; its path and sha256 recorded in inputs.rewrites. PASS iff (i) this run's "
              "enumeration is empty and (ii) the dose note is present iff the flag of record, (ii) computed from "
              "dose_note's own status (present iff dose_note(True, table) is 'carried': the table carries a "
              "dose-note span), not only through clause (c). The comparator (\"the VERDICTS enumeration\") is "
              "Q-F0's VERDICTS output in the verdicts directory, its stored v1_outputs enumeration; where that "
              "file does not exist (Q-F0 NOT-RUN: on its Clock path the table of record is built at the posting, "
              "m:278, PIN-40; a no-first-read NOT-RUN from `verdicts` records no enumeration either), the "
              "posting's own of-record output in the out directory, its outputs' enumeration. Refused (exit 2): "
              "neither; a comparator that is not what it is taken for (a VERDICTS file whose schema is not "
              "m-verdicts-v1 or whose unit is not Q-F0; an of-record output whose schema is not "
              "m-posting-v1-outputs-v1 or whose table_kind is not of-record); one recording no enumeration (an "
              "item that is not an object, or does not carry exactly enumeration()'s fields, a str row_id and a "
              "list clauses among them, included); one naming a row id twice. Its kind, path, sha256 and stored "
              "tuple (None where it stores none, or one that is not an object) are recorded, with whether that "
              "tuple is this run's (same_tuple: informational, it decides nothing). Expected = the comparator's "
              "rows less those the rewrite list names; actual = this run's enumeration; reported: only_actual, "
              "only_expected, changed (in both, the two enumeration items differing in a field other than loc), "
              "moved (in both, the two items differing in loc alone: informational, as a line added or removed "
              "in the posted text moves every later row), rewrites_not_in_comparator (informational) and "
              "differs (any of only_actual, only_expected and changed). The comparison is reported; it does not "
              "decide PASS / FAIL. A PASS writes once (identical on a re-run; exit 0). A FAIL writes nothing, so "
              "its stdout is the record of that step: the verdict, the residue by row id and, row by row, each "
              "residue item in full as the enumeration carries it (row_id, loc, clauses, a, b, c, treatments; no "
              "tag, pick or free-round event is in an item), each comparison set (moved included) with its rows "
              "in full, and the unwritten record's declared tuple (with its reasons and pending), inputs (path "
              "and sha256 each), comparator, flag and binding (the analyzer's, package's and closure's sha256), "
              "in sorted-key JSON; it exits 5 (PIN-26). The output gains `bar` {applies, verdict, "
              "enumeration_empty, dose_note_iff_flag, residue, comparison}; `outputs` is unchanged.",
    "PIN-45": "Declared at LOCK v1.0, built at step 15 on the seat's round-2 item 3 (lock §9.6), which orders "
              "\"(b) a fired end look without a matching pause\" built \"as VERDICTS refusals\" that \"guard the "
              "checkpoint against a hand edit\". Code's reading, mirroring the writer's invariants in stages "
              "(_campaign_end, _stop_end_look, run_campaign's cadence-look pause; stages writes a pause's "
              "adjudication only on a resume, and an ended campaign is never resumed): an end look is fired iff "
              "its `fired` is true, or any of its results is fired, or -- where it reuses cadence look k "
              "(end_is_look k) -- look k as ck.looks records it is fired (its result's `fired` or any of its "
              "results'); a hand edit clearing one of these beside another is still a fired end look. Its bars "
              "are the names of its fired results, in order. A pause raised at the end -- a fresh end look's (no "
              "end_is_look; terminal or STOP), or a reused look k's at a hair-trigger STOP on a multiple of 40, "
              "where the hit pre-empted the cadence pause -- is matched only by the campaign's last pause being "
              "{kind end_look, look 'end' (fresh) or kind look, look k (reused), at_launches the end look's, bars "
              "its fired bars} with no adjudication: an ended campaign's end pause is never adjudicated in the "
              "checkpoint, and its ruling enters only as PIN-9's declared --adjudication file. A reused look k's "
              "at a terminal or G-VER end is matched by some pause {kind look, look k, at_launches the end "
              "look's, bars} carrying a str adjudication -- raised before the end and ruled before the end, "
              "through stages: by the seat's adjudication, or by the PI's stop text recorded as the pause's "
              "ruling (stages.py:2124-2129); a schedule_exhausted pause may follow it at the same n. kind, look "
              "and at_launches are compared by value and exact type, as the writer writes ints and strs (a count "
              "6.0 is not 6). The rule is chosen by the end's class as the checkpoint records it: STOP iff a stop "
              "block is recorded, else the terminal block's status (resume.ended_status); a STOP's bar G-VER or "
              "the hair trigger, any other refused after PIN-8 whichever rule is chosen. What no other V2 check "
              "pins is checked here, for a fired end look at a STOP, by ids only (no pick-bearing field is read), "
              "against the writer's own assertions (stages._stop_end_look): a hair-trigger STOP's (template, s) "
              "is the last session recorded, a G-VER STOP's (template, s) none of them (its record is "
              "quarantined in the stop block). Otherwise a structural refusal at V2 (exit 2; nothing released or "
              "written), after PIN-46's and before PIN-9's branch, so that a deleted pause is never read as no "
              "pause. An unfired end look needs no pause; none is checked. Its limits, Code's reading too: an end "
              "look with every fired flag cleared -- a fresh one, or a reused one together with the look it "
              "reuses as ck.looks records it -- cannot be told at V2 from a silent one without recomputing "
              "campaign_look from the session records, which are pick-bearing until V3 (PIN-7's order); and a "
              "hair-trigger STOP at a reused look whose stop block is replaced by a terminal PI-STOP, its end "
              "pause given a ruling, has the shape of the PI's stop of a paused look at n, which ids cannot tell "
              "apart; and a hair-trigger STOP whose stop block is relabelled G-VER with its (template, s) moved to "
              "an id not recorded (at a reused look, its pause given a ruling) passes, as V2 checks a G-VER STOP's "
              "id only against the record, as the writer asserts; moved to its arm's next launch (s the count of "
              "that template's sessions recorded) it has the shape of a G-VER STOP there, which ids cannot tell "
              "apart. No V2 refusal catches any of the three.",
    "PIN-46": "Declared at LOCK v1.0, built at step 15 on the seat's round-2 item 3 (lock §9.6), which orders "
              "\"(c) the end look's launch count\" built \"as VERDICTS refusals\" that \"guard the checkpoint "
              "against a hand edit\". Code's reading: wherever campaign.end_look is recorded, at every end that "
              "records one (STOP and terminal alike; Code's round-2 block had scoped it to the STOP), its "
              "at_launches is an int (exact type: a bool or a float is no launch count) equal to len(sessions), "
              "the launches recorded (a G-VER record is quarantined in the stop block, never a session); "
              "provenance `launched` sums are never used. An end look reusing cadence look k (end_is_look k) "
              "carries that look's launch count too: ck.looks must record a look k (its result's look, by value "
              "and exact type) whose at_launches is the end look's (an int, by exact type too), as the writer "
              "reuses only the look recorded at n. Otherwise a structural refusal at V2 (exit 2; nothing released or written), after PIN-10's "
              "and before PIN-45's, so that each refusal shows its own message on its own case.",
}
SEAT_ROUTED = {"PIN-5": "routed before LOCK v0.1; ruled by the seat (C1, 2026-10-10): confirmed -- m:324's "
                        "parenthetical ends 'or any reason'; clock:not-locked:<stage> reads that clause",
               "PIN-8": "routed before LOCK v0.1; ruled by the seat (C2, 2026-10-10): confirmed",
               "PIN-9": "routed before LOCK v0.1; ruled by the seat (C3, 2026-10-10): confirmed; C9(i) for a fired "
                        "end look's adjudication on a terminal campaign",
               "PIN-17": "routed before LOCK v0.1; ruled by the seat (C4, 2026-10-10): confirmed"}


# =============================================================================================
# THE BATTERY (m:278). Selftest-only helpers carry the `_bt` prefix.
# =============================================================================================
EXPECTED_CHECKS = 444        # the battery's fixed check list (any skip or addition changes it)

# PIN (Code, declared at LOCK v0.1): PIN-24 -- the battery reaches every per-arm outcome per unit, the
# full 5 x 6^3 product under both flag values (the flag an input, not a coordinate; 'clock:pi-declined'
# for every NOT-RUN coordinate there, every other code in the NR group, and a distinct reason per unit
# in a further pass), and a reader-path subset built by the production writers on the stub;
# REQUIRED_COVERAGE and EXPECTED_CHECKS make a skip a FAIL.
_REQUIRED: list[str] = []
for _u in UNITS:
    _REQUIRED += [f"OUT-{x}-{_u}" for x in ("PASS", "REVERSE", "DEAD", "INDET-iii", "INDET-i-equal",
                                            "INDET-ii-share", "INDET-ii-emptymap", "INDET-E-half",
                                            "NOREAD-contrast-empty", "NOREAD-sham-empty")]
_REQUIRED += ["ARM-BOTHEMPTY-RAISES", "BND-PASS-INDET-80", "BND-PASS-INDET-96", "BND-REV-80", "BND-REV-96",
              "BND-DEAD-80", "BND-DEAD-96", "BND-SHARE-HALF", "BND-KN-NOTDEAD", "BND-DELTA-EQ-E",
              "BND-PLEALPHA-80", "BND-PLEALPHA-96", "BND-PLEALPHA-213", "BND-DEAD-CP-AGREE",
              "ORD-REV-OVER-DEAD", "ORD-PASS-OVER-DEAD", "ORD-NOREAD-FIRST", "ORD-UNIT-FIRST",
              "PWR-916", "PWR-878", "PWR-ZERO-EMPTYMAP", "PWR-BRUTE", "PWR-RECORD-VS-REALISED",
              "SENT-PASS", "SENT-REVERSE", "SENT-DEAD", "SENT-INDET", "SENT-NOREAD-CONTRAST",
              "SENT-NOREAD-SHAM", "SENT-GUARD-QWEN-BINDING", "SENT-GUARD-OLMO-REPORTED", "SENT-NOLOOK",
              "SENT-FLOOR-PRESENT", "SENT-FLOOR-ABSENT", "SENT-PREPICK", "SIGN-DISPLAY", "BND-REV-SHARE-HALF",
              "BND-REV-EMPTYMAP", "BND-REV-DELTA-EQ-E", "PWR-ODD-N"]
for _u in UNITS:
    for _c in ("clock:pi-declined", "clock:k-zero", "no-first-read:pi-stop", "no-first-read:gver-stop",
               "no-first-read:cap", "clock:gate-stopped", "clock:not-locked"):
        _REQUIRED.append(f"NR-{_c}-{_u}")
    if _u != "Q-F0":
        _REQUIRED += [f"NR-clock:no-box-{_u}", f"NR-dose-not-completable-{_u}",
                      f"NR-pending-closed-at-v2-{_u}"]
        _REQUIRED += [f"PEND-{s}-{_u}" for s in PENDING_SUBSTATES]
_REQUIRED += ["NR-REFUSE-no-box-Q-F0", "NR-REFUSE-dose-Q-F0", "NR-REFUSE-unknown-stage",
              "NR-REFUSE-v2-at-v1", "PEND-CLOCK-REFUSED", "PEND-VERDICTS-REFUSED", "PEND-NOTRUN-REFUSED",
              "PEND-QF0-REFUSED", "PEND-VERDICTS-CARRIES", "DEC-CARRIED", "DEC-MISSING-REFUSED", "DEC-QF3-PENDING",
              "PEND-DATE", "PEND-DATE-RECORDED", "DEC-UNIT-DATE",
              "PEND-DATE-TRAILING", "PEND-DATE-CLOCK-FALSE", "PEND-EXTRA-KEYS", "DEC-DATE-TRAILING",
              "DATE-ISO-REAL", "NR-RECORD-DATE", "OLMO-STATES-DATE",
              "NR-STOP-ROUTING", "NR-GATE-STOPPED-GID-Q-F0", "NR-GATE-STOPPED-GCAL-OLMO", "ROWS-EQ-LABELSET"]
_REQUIRED += [f"TUP-T{i}-{f}" for i in range(1, 11) for f in ("T", "F")] + ["TUP-REASONS-DISTINCT"]
_REQUIRED += [f"ENUM-{r[0]}-{f}" for r in PLACEHOLDER_SPEC for f in ("T", "F")]
_REQUIRED += ["ENUM-NODOSE-T", "ENUM-NODOSE-F", "ENUM-PLACEHOLDER-FILE", "ENUM-SAMELINE"]
_REQUIRED += [f"ENUM-REF-{i:02d}" for i in range(1, 22)]
_REQUIRED += ["FLAG-OF-RECORD-TRUE", "FLAG-FALSE-absent", "FLAG-FALSE-schema", "FLAG-FALSE-f1_012",
              "FLAG-FALSE-uncommitted", "FLAG-RENDERS-BESIDE"]
_REQUIRED += ["CNT-DECL-M314", "CNT-DECL-AUDIT", "CNT-FIRE-SILENT", "CNT-EXCLUDED-TABULATED",
              "CNT-PROPERTY-KEYS", "CNT-DENOMINATORS", "CNT-UNDECLARED-RAISES", "CNT-PER-PROPERTY",
              "CNT-REASONING-STOP", "CNT-GATE-RELEASE", "CNT-TALLY-EQUAL", "CNT-PREPICK-STAGES",
              "CNT-PROPERTY-EXACT", "CNT-COUNTS-CRAFTED", "CNT-PREPICK-RATES", "CNT-EXCLROUND-STOP"]
_REQUIRED += ["SEC-FLOOR-19-20", "SEC-B-CONTRAST-ONLY", "SEC-D-SHAM-COUNT-ONLY", "SEC-VALID-THROUGH",
              "SEC-HABIT-IDENTITY", "SEC-VALUES"]
_REQUIRED += ["C3-CAP-ZERO", "C3-PISTOP-ZERO", "C3-GVER-ZERO", "C3-GVER-DATA", "C3-HAIR-NODISP",
              "C3-HAIR-DISP", "C3-CAP-SHAM-ONLY", "C3-COMPLETE", "C3-COMPLETE-BELOW-FLOOR",
              "C3-COMPLETE-EMPTY", "C3-OLMO-COMPLETE", "C3-ENDLOOK-PAUSE", "C3-LASTLOOK-END-WINS",
              "C3-LASTLOOK-STOP-ENDISLOOK", "C3-COUNTS-INDEPENDENT", "C3-STOP-NO-ENDLOOK-REFUSED",
              "C3-HAIR-ENDLOOK-LABEL", "C3-HAIR-ENDLOOK-PAUSE", "C3-GVER-ENDLOOK-PAUSE", "C3-HAIR-LOOK40-PAUSE",
              "C3-STOP-NO-ENDLOOK-HAIR-REFUSED", "C3-LASTLOOK-STOP-PAST-CADENCE", "C3-PISTOP-DATA-LABEL"]
_REQUIRED += ["C3-ENDLOOK-COUNT-REUSE", "C3-ENDLOOK-COUNT-TERMINAL", "C3-ENDLOOK-COUNT-STOP",        # PIN-46
              "C3-ENDLOOK-NOPAUSE-TERMINAL", "C3-ENDLOOK-NOPAUSE-HAIR", "C3-ENDLOOK-NOPAUSE-GVER",      # PIN-45
              "C3-ENDLOOK-NOPAUSE-REUSE", "C3-ENDLOOK-PAUSE-KIND", "C3-ENDLOOK-PAUSE-COUNT", "C3-ENDLOOK-PAUSE-BARS",
              "C3-ENDLOOK-PAUSE-NOT-LAST", "C3-ENDLOOK-FIRED-CLEARED", "C3-ENDLOOK-ORDER", "C3-ENDLOOK-REUSE-NOT-LAST"]
_REQUIRED += ["C3-ENDLOOK-COUNT-REUSED-LOOK", "C3-ENDLOOK-COUNT-BOOL", "C3-ENDLOOK-COUNT-MISSING",           # round 2
              "C3-ENDLOOK-PAUSE-ADJ-FILLED", "C3-ENDLOOK-REUSE-APPENDED", "C3-ENDLOOK-REUSE-FIRED-LOOK",
              "C3-ENDLOOK-FIRED-FLAG-ONLY", "C3-ENDLOOK-PAUSE-LOOK", "C3-ENDLOOK-PAUSE-TYPE",
              "C3-ENDLOOK-REUSE-PAUSE-ALTERED", "C3-ENDLOOK-PAUSE-BARS-ORDER", "C3-ENDLOOK-REUSE-K"]
_REQUIRED += ["C3-ENDLOOK-PAUSE-ADJ-NOTNONE", "C3-ENDLOOK-PAUSE-LAST-UNRULED",                         # round 3
              "C3-ENDLOOK-REUSE-FIRED-LOOK-DISJUNCTS", "C3-ENDLOOK-REUSE-ADJ-NONSTR", "C3-ENDLOOK-REUSE-K-TYPE",
              "C3-ENDLOOK-REUSE-GUARDS", "C3-ENDLOOK-STOP-CLASS"]
_REQUIRED += [f"C3-PROD-END-P{i}" for i in range(1, 11)]
_REQUIRED += [f"REF-{x}" for x in ("NOT-ENDED", "END-PENDING", "UNADJUDICATED", "OTHER-UNIT", "STAGE",
                                   "LOCK-SHA", "ANALYZER-NOT-IN-LOCK", "PACKAGE-NOT-IN-LOCK",
                                   "CLOSURE-NOT-IN-LOCK", "TABLE-NOT-IN-LOCK", "PREPRINT-NOT-IN-LOCK",
                                   "PROPOSAL-SHA", "BACKEND-SPLICE", "POD", "STUB",
                                   "DOMAIN-STOP", "FIRSTPICK-STOP", "CELL-STOP", "UNVERIFIED",
                                   "WRITE-ONCE", "CANONICAL-OUT", "LOCK-UNCOMMITTED", "ANALYZER-UNCOMMITTED",
                                   "FFP-OUTSIDE-STOP", "EXCLROUND-STOP", "NO-FLOORS", "NO-FLOORS-BEFORE-V4",
                                   "FIXTURE-S0", "STUB-CAMPAIGN-ONLY", "STUB-GATE-ONLY", "ADJ-BINDING",
                                   "PISTOP-BINDING", "SURPLUS-SEAT-INPUT", "GATE-NOT-ENDED", "GATE-WRONG-STAGE",
                                   "ADJ-SCHEMA", "ADJ-TEXT", "PISTOP-SCHEMA", "PISTOP-TEXT",
                                   "SURPLUS-ADJ-ADJUDICATED", "SURPLUS-PISTOP-TERMINAL", "FLOORS-NEGATIVE",
                                   "NO-FLOORS-BEFORE-V3")]
_REQUIRED += ["CMD-NOTRUN", "CMD-NOTRUN-NOFIRSTREAD-REFUSED", "CMD-POSTING", "CMD-POSTING-CROSSCHECK",
              "CMD-VERDICTS-IDENTICAL", "CMD-VERDICTS-QF0-V1", "CMD-VERDICTS-RATES", "CMD-VERDICTS-OLMO-CROSSCHECK",
              "CMD-VERDICTS-QF0-FLAG-FALSE", "CMD-VERDICTS-QF0-TABLE-REFUSALS", "CMD-EXCLUSIVE-WRITE",
              "CMD-POSTING-BOTH-KINDS", "CMD-POSTING-FLAG-FALSE", "CMD-POSTING-REASON-MISMATCH",
              "CMD-POSTING-BOTH-OUTPUTS", "CMD-POSTING-KEYSET", "CMD-POSTING-TABLE-REFUSALS", "CMD-POSTING-MALFORMED",
              "CMD-POSTING-TABLE-BOUND", "CMD-POSTING-TUPLE", "CMD-POSTING-BINDING", "CMD-VERDICTS-BINDING",
              "CMD-SECONDARY-HABIT", "CMD-VERDICTS-DECISIONS", "CMD-VERDICTS-NR-DECISIONS", "CMD-NOTRUN-DECISIONS",
              "NR-CMD-GATE-NOT-ENDED", "NR-CMD-GATE-WRONG-STAGE", "NR-CMD-STUB", "NR-CMD-BINDING",
              "NR-CMD-GATE-BEFORE-RELEASE", "NR-CMD-BINDING-FIRST", "NR-CMD-PROPOSAL-SHA",
              "CMD-POSTING-BINDING-FIRST", "CMD-POSTING-PROPOSAL-SHA"]
_REQUIRED += ["CMD-POSTING-BAR-NA", "CMD-POSTING-BAR-PASS", "CMD-POSTING-CMP-MATCH", "CMD-POSTING-CMP-VERDICTS",  # PIN-44
              "CMD-POSTING-BAR-FAIL", "CMD-POSTING-EXIT-5", "CMD-POSTING-BAR-DOSE", "CMD-POSTING-CMP-DIFFERS",
              "CMD-POSTING-CMP-SELECT", "CMD-POSTING-REWRITES-KIND", "CMD-POSTING-REWRITES-FORM",
              "CMD-POSTING-REWRITES-AFTER-BINDING"]
_REQUIRED += ["CMD-POSTING-RESIDUE-ORDER", "CMD-POSTING-REWRITES-EMPTY", "CMD-POSTING-CMP-TUPLE"]           # round 2
_REQUIRED += ["CMD-POSTING-CMP-TUPLE-NONE", "CMD-POSTING-CMP-IDENTITY", "CMD-POSTING-FAIL-RECORD"]       # round 3
_REQUIRED += ["STR-PROPOSAL-SHA", "STR-CONSTANTS", "STR-CONSTANTS-MUTANT", "STR-OPEN-HOOK",
              "STR-NO-HEAVY", "STR-CALL-SITES", "STR-FORBIDDEN", "STR-NO-CANONICAL-WRITE",
              "STR-DETERMINISM", "STR-CLOSURE", "STR-LAZY-IMPORTS", "STR-PIN-COMMENTS", "STR-INSULATED",
              "STR-STDOUT-HYGIENE", "STR-GANL-COMMITTED", "STR-GANL-EXIT", "STR-GANL-ARTIFACT",
              "STR-GANL-SHA16", "STR-GANL-FLAG", "STR-GANL-REGISTER", "STR-GANL-PLACEHOLDER",
              "STR-GANL-BATTERY-BLOCK", "STR-GANL-CONTENT-EXIT", "STR-PIN-V10-TEXTS"]
REQUIRED_COVERAGE = frozenset(_REQUIRED)
del _u, _c


class _Battery:
    """The check recorder: every chk prints one line; coverage ids are marked as reached."""

    def __init__(self) -> None:
        self.results: list[bool] = []
        self.reached: set[str] = set()
        self.scrub: list[str] = []
        self.extra: dict = {}

    def clean(self, s: str) -> str:
        """Temp-directory paths scrubbed, so every printed line is deterministic."""
        for t in sorted(self.scrub, key=len, reverse=True):
            s = s.replace(t, "<tmp>")
        return s

    def short(self, x: Any, n: int = 160) -> str:
        s = self.clean(x if isinstance(x, str) else repr(x))
        s = " ".join(s.split())
        return s if len(s) <= n else s[:n - 3] + "..."

    def chk(self, name: str, ok: Any, got: Any = "", cover: Sequence[str] = ()) -> bool:
        ok = bool(ok)
        self.results.append(ok)
        if ok:
            for c in cover:
                if c not in REQUIRED_COVERAGE:
                    raise KeyError(f"coverage id {c!r} is not declared")
                self.reached.add(c)
        tail = "" if got in ("", None) else " " + self.short(got)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}{tail}", flush=True)
        return ok

    def group(self, name: str, fn: Callable[[], None]) -> None:
        try:
            fn()
        except (Exception, SystemExit) as e:                         # noqa: BLE001
            self.chk(f"{name}: group raised", False, f"{type(e).__name__}: {e}")


def _bt_raises(fn: Callable[[], Any], exc=(ValueError,)) -> tuple[bool, str]:
    try:
        fn()
    except exc as e:                                                  # type: ignore[misc]
        return True, str(e)
    except Exception as e:                                            # noqa: BLE001
        return False, f"wrong exception {type(e).__name__}: {e}"
    return False, "no exception"


# --- open hook (PIN-29) --------------------------------------------------------------------------
class _OpenHook:
    # PIN (Code, declared at LOCK v0.1): PIN-29 -- during --selftest and ganl, builtins.open, io.open
    # and Path.open/read_bytes/read_text refuse any path under data/m/ckpt, data/m/reports,
    # data/m/verdicts or results/raw; the no-canonical-write snapshot takes only os.stat there.
    def __init__(self) -> None:
        self.blocked = [(REPO / r).resolve() for r in BLOCKED_REL]
        self.saved: tuple = ()
        self.caught: list[str] = []

    def _check(self, f: Any) -> None:
        if isinstance(f, int):
            return
        try:
            p = Path(os.fspath(f)).resolve()
        except TypeError:
            return
        for b in self.blocked:
            if p == b or b in p.parents:
                self.caught.append(_repo_rel(p))
                raise PermissionError(f"PIN-29: the analyzer's battery never reads {_repo_rel(p)} "
                                      f"(pick-bearing or derived; m:318)")

    def __enter__(self) -> "_OpenHook":
        bo, io_open = builtins.open, io.open
        po, prb, prt = pathlib.Path.open, pathlib.Path.read_bytes, pathlib.Path.read_text
        self.saved = (bo, io_open, po, prb, prt)
        hook = self

        def h_open(f, *a, **k):
            hook._check(f)
            return bo(f, *a, **k)

        def h_io(f, *a, **k):
            hook._check(f)
            return io_open(f, *a, **k)

        def h_popen(self_, *a, **k):
            hook._check(self_)
            return po(self_, *a, **k)

        def h_rb(self_):
            hook._check(self_)
            return prb(self_)

        def h_rt(self_, *a, **k):
            hook._check(self_)
            return prt(self_, *a, **k)
        builtins.open, io.open = h_open, h_io
        pathlib.Path.open, pathlib.Path.read_bytes, pathlib.Path.read_text = h_popen, h_rb, h_rt
        return self

    def __exit__(self, *exc) -> None:
        bo, io_open, po, prb, prt = self.saved
        builtins.open, io.open = bo, io_open
        pathlib.Path.open, pathlib.Path.read_bytes, pathlib.Path.read_text = po, prb, prt


def _bt_snapshot() -> dict:
    """data/m's state: sha256 of files outside the blocked dirs, os.stat only inside them (PIN-29)."""
    root = REPO / "data" / "m"
    out = {}
    blocked = [(REPO / r).resolve() for r in BLOCKED_REL]
    for p in sorted(root.rglob("*")) if root.is_dir() else []:
        if not p.is_file():
            continue
        rp = p.resolve()
        if any(rp == b or b in rp.parents for b in blocked):
            st = os.stat(p)
            out[_repo_rel(p)] = f"stat:{st.st_size}:{st.st_mtime_ns}:{st.st_ino}"
        else:
            with builtins.open(p, "rb") as fh:
                out[_repo_rel(p)] = hashlib.sha256(fh.read()).hexdigest()
    return out


# --- the proposal constants (PIN-31) ---------------------------------------------------------------
def constants_by_line() -> dict[int, list[str]]:
    """Every m-verbatim constant with the proposal line it must appear on (1-based)."""
    return {
        14: ["*Answered, as recognition*", "the weight channel (*concluded, not answered*)",
             "*" + LABEL_BASE + "*", LABEL_E2B],
        16: [f"D1 (Q-F0) **{CLOCK_DATE}**", f"D_O (each OLMo checkpoint) **{CLOCK_DATE}**"],
        190: [".916 at P = .70; (80, 32): .878", "96 at .01 → 60; 80 at .01 → 51",
              "each arm split n/2 per map at clean share P in both maps, its sham split m/2 per map at .5",
              "Attained power at the realised n is reported in VERDICTS, descriptively, and is the power "
              "figure of record for the verdict sentences"],
        192: ["At k = 0 the rule yields no launch count"],
        247: ["its shortfall and attained power in its verdict sentence",
              "a sham arm with no domain session leaves E undefined"],
        306: ["**Δ_c = P − 0.5**", "P_arm − P_sham beside"],
        310: ["(i) signed, strict: Δ_c(X) > E toward clean; REVERSE: Δ_c(X) < −E",
              "(ii) non-strict: each map's clean share ≥ .5 (≤ .5 for REVERSE)",
              "**a map with no domain session fails (ii)**",
              "CI: two-sided Clopper–Pearson 95% on P, expressed on Δ_c"],
        312: ["m's floor is 20 events", F1_CROSSING,
              "(32 and 56 give 8 and 14 per pair, below the floor of 20)",
              "`e2d/habit.py`'s within-arm identity at F0m/F0m-OLMo"],
        314: [m314_counter_text(), "f1 CORR's 7-vs-1 anomaly (archive:91–93) is the reference"],
        316: ["(**binding on both substrates**)", "on OLMo the absolute bar is reported only"],
        324: ["(no box; a gate STOPPED and no re-specification was locked; the PI declined to commit v1.0, "
              "for projected hours or any reason)", "\"dose not completable\"",
              "before a PI stop, a G-VER STOP, or its cap",
              "unlocked with D_O not yet passed, or locked and running, restarting after a box change, or "
              "awaiting its VERDICTS session", "NOT-RUN sets every cell of the unit to NOT-RUN with the "
              "reason recorded"],
        326: ["INDETERMINATE with the sentence *no read obtained* if the arm has no domain session or its E "
              "is undefined", "(" + SENTENCE_TEMPLATES["reverse"] + ")",
              "DEAD if the CI upper bound on Δ_c < +0.15",
              "**Every contrast arm's verdict sentence states the arm's pre-pick exclusion rate beside its "
              "sham's, with the guard's result at that unit's last look**",
              # Q-F3's outcome words, for a decision's other_state (PIN-35)
              "**A2, α = .01:** the same with FAIL for DEAD",
              "**NO-READ** if no domain session or E undefined; else REVERSE → POSITIVE → **NULL-x if",
              "NULL-x↑ toward clean, NULL-x↓ toward corrupted** → NULL"],
        340: ["**CONFIRMED** (in the screen's direction)", "**DISCORDANT** if f2's (i)–(iii) hold in the "
              "other direction", "**UNLICENSED** otherwise"],
        334: ["Main: *" + TITLES["Main"] + "*", "Fallback-1: *" + TITLES["Fallback-1"] + "*",
              "Fallback-2: *" + TITLES["Fallback-2"] + "*"],
        337: ["L0 := (A0 = PASS); L0-OLMo-c := (A0-OLMo-c = PASS) for c ∈ {sft, dpo, instruct}"],
        338: ["*" + TEMPLATE_F0 + "*", "*" + TEMPLATE_O + "*", "*" + LABEL_E2B + "*",
              "*" + LABEL_BASE + "***", '"' + ABSTRACT_ALL + '"', '"' + ABSTRACT_SOME + '"',
              '"' + ABSTRACT_NONE + '"', "S1 and the weight channel untouched",
              "f1's CORR line carries its dose note iff G-CAL's 0.12 artifact exists (input flag)"],
        341: ["**Fallback-1 iff L0; Fallback-2 otherwise** (Q-F0 NOT-RUN sets L0 = false)",
              "L0-OLMo-c never enters the ceiling"],
        343: ["(PASS / DEAD / REVERSE / INDETERMINATE / not run / pending)", "\"open\" at v1 by construction"],
        349: ["*(c) The f1 CORR dose note is carried iff G-CAL's 0.12 artifact exists*",
              "The never-*Answered* cells — the weight channel, the OLMo base row and e2b — are reached by "
              "clause (a) like any other; nothing exempts them"],
    }


def constant_problems(lines: Sequence[str]) -> list[str]:
    out = []
    for n, consts in constants_by_line().items():
        line = lines[n - 1] if 0 < n <= len(lines) else ""
        for c in consts:
            if c not in line:
                out.append(f"m:{n}: {c[:60]!r}")
    return out


# --- battery: per-arm outcomes ------------------------------------------------------------------
_OUT_CASES = {  # name: (n0, k0, n1, k1, mS, j, state, check)
    "PASS": (40, 28, 40, 28, 32, 16, "PASS"),
    "REVERSE": (40, 12, 40, 12, 32, 16, "REVERSE"),
    "DEAD": (40, 20, 40, 20, 32, 16, "DEAD"),
    "INDET-iii": (40, 24, 40, 24, 32, 16, "INDETERMINATE"),
    "INDET-i-equal": (40, 28, 40, 28, 40, 28, "INDETERMINATE"),
    "INDET-ii-share": (40, 19, 40, 37, 32, 16, "INDETERMINATE"),
    "INDET-ii-emptymap": (0, 0, 80, 60, 32, 16, "INDETERMINATE"),
    "INDET-E-half": (40, 40, 40, 40, 32, 32, "INDETERMINATE"),
    "NOREAD-contrast-empty": (0, 0, 0, 0, 32, 16, "INDETERMINATE"),
    "NOREAD-sham-empty": (40, 28, 40, 28, 0, 0, "INDETERMINATE"),
}


def _bt_ev(n0, k0, n1, k1, mS, j, ended="COMPLETE"):
    return {"kind": "campaign", "ended": ended, "stop_bar": None, "pi_stop_record": False,
            "counts": {"n0": n0, "k0": k0, "n1": n1, "k1": k1, "mS": mS, "j": j}}


def _bt_outcomes(B: _Battery) -> None:
    for U in UNITS:
        for name, (n0, k0, n1, k1, mS, j, want) in _OUT_CASES.items():
            ended = "CAP" if name.startswith("NOREAD") else "COMPLETE"
            st = unit_state(U, _bt_ev(n0, k0, n1, k1, mS, j, ended))
            out = st[1]
            ok = st[0] == "ANALYZED" and out["state"] == want
            if name == "INDET-iii":
                ok = ok and out["route"]["toward_clean"] == ["iii"] and not out["pred"]["dead"]
            elif name == "INDET-i-equal":
                ok = ok and out["stats"]["delta"] == out["stats"]["E"] == Fraction(1, 5) and \
                    "i" in out["route"]["toward_clean"] and out["pred"]["iii_up"] and out["pred"]["ii_up"]
            elif name == "INDET-ii-share":
                ok = ok and out["route"]["toward_clean"] == ["ii"]
            elif name == "INDET-ii-emptymap":
                ok = ok and out["route"]["toward_clean"] == ["ii"] and out["pred"]["i_up"] and out["pred"]["iii_up"]
            elif name == "INDET-E-half":
                ok = ok and out["stats"]["E"] == HALF and not out["pred"]["i_up"] and not out["pred"]["i_dn"]
            elif name == "NOREAD-contrast-empty":
                ok = ok and out["noread"] == "contrast-empty" and out["pred"] is None
            elif name == "NOREAD-sham-empty":
                ok = ok and out["noread"] == "sham-empty" and out["pred"] is None
            elif name == "DEAD":
                ok = ok and out["pred"]["dead"] and not out["pred"]["iii_up"] and not out["pred"]["iii_dn"]
            elif name == "REVERSE":
                ok = ok and out["pred"]["dead"]          # REVERSE ⊂ DEAD here: the order decides
            B.chk(f"outcome {U} {name}: {(n0, k0, n1, k1, mS, j)} -> {want}", ok,
                  (out["state"], out["route"] if out["state"] == "INDETERMINATE" else None),
                  cover=[f"OUT-{name}-{U}"])
    ok, msg = _bt_raises(lambda: arm_outcome(0, 0, 0, 0, 0, 0), (BothArmsEmpty,))
    ok2 = unit_state("Q-F0", _bt_ev(0, 0, 0, 0, 0, 0, "CAP"))[0] == "NOT-RUN"
    B.chk("both arms empty: arm_outcome raises BothArmsEmpty; the unit layer gives NOT-RUN instead", ok and ok2,
          msg[:60], cover=["ARM-BOTHEMPTY-RAISES"])
    # boundaries at n = 80 and 96, (i) and (ii) satisfied (sham E = 0, balanced maps)
    for n, kp, kr, kd, tag in ((80, 51, 29, 43, "80"), (96, 60, 36, 52, "96")):
        h = n // 2

        def st(k):
            a = k // 2
            return arm_outcome(h, a, h, k - a, 32, 16)["state"]
        B.chk(f"boundary n = {n}: PASS at {kp}, INDETERMINATE at {kp - 1} ((i), (ii) hold)",
              st(kp) == "PASS" and st(kp - 1) == "INDETERMINATE", (st(kp), st(kp - 1)),
              cover=[f"BND-PASS-INDET-{tag}"])
        B.chk(f"boundary n = {n}: REVERSE at {kr}, not at {kr + 1}",
              st(kr) == "REVERSE" and st(kr + 1) != "REVERSE", (st(kr), st(kr + 1)), cover=[f"BND-REV-{tag}"])
        d1 = arm_outcome(h, kd // 2, h, kd - kd // 2, 32, 16)
        d2 = arm_outcome(h, (kd + 1) // 2, h, kd + 1 - (kd + 1) // 2, 32, 16)
        B.chk(f"boundary n = {n}: DEAD at {kd}, not at {kd + 1} (exact tail at 13/20 vs 1/40)",
              d1["pred"]["dead"] and d1["state"] == "DEAD" and not d2["pred"]["dead"] and d2["state"] != "DEAD",
              (d1["state"], d2["state"]), cover=[f"BND-DEAD-{tag}"])
    o = arm_outcome(40, 20, 40, 31, 32, 16)
    B.chk("a map share exactly .5 passes (ii): 20/40 + 31/40 -> PASS at 51/80",
          o["state"] == "PASS" and o["stats"]["share0"] == HALF, o["state"], cover=["BND-SHARE-HALF"])
    kn = [arm_outcome(n // 2, n // 2, n - n // 2, n - n // 2, 32, 32)["pred"]["dead"] for n in (1, 2, 32, 80)]
    B.chk("k = n is never DEAD (CP upper bound 1)", not any(kn) and not dead_pred(5, 5), kn,
          cover=["BND-KN-NOTDEAD"])
    e = arm_outcome(40, 28, 40, 28, 40, 28)
    e2 = arm_outcome(40, 28, 40, 28, 40, 27)
    B.chk("Δ_c = E fails (i) (strict); Δ_c > E by one sham pick passes",
          not e["pred"]["i_up"] and e["state"] == "INDETERMINATE" and e2["state"] == "PASS",
          (e["state"], e2["state"]), cover=["BND-DELTA-EQ-E"])
    # the REVERSE-direction mirrors of the three boundaries above (m:310's '≤ .5 for REVERSE', 'a map
    # with no domain session fails (ii)', and (i) strict: Δ_c(X) < −E)
    rh = arm_outcome(40, 20, 40, 9, 32, 16)
    B.chk("REVERSE: a map share exactly .5 satisfies (ii) toward corrupted: 20/40 + 9/40 -> REVERSE at 29/80",
          rh["state"] == "REVERSE" and rh["stats"]["share0"] == HALF and rh["pred"]["ii_dn"], rh["state"],
          cover=["BND-REV-SHARE-HALF"])
    re_ = arm_outcome(0, 0, 80, 20, 32, 16)
    B.chk("REVERSE: a map with no domain session fails (ii) toward corrupted: 0 + 20/80 -> DEAD, not REVERSE "
          "((i) and (iii) hold)", re_["state"] == "DEAD" and not re_["pred"]["ii_dn"] and re_["pred"]["i_dn"]
          and re_["pred"]["iii_dn"], re_["state"], cover=["BND-REV-EMPTYMAP"])
    rq, rq2 = arm_outcome(40, 12, 40, 12, 40, 28), arm_outcome(40, 12, 40, 12, 40, 27)
    B.chk("REVERSE: Δ_c = −E fails (i) (strict) -> DEAD; one fewer sham pick (E .175 < .2) -> REVERSE",
          rq["stats"]["delta"] == -rq["stats"]["E"] and not rq["pred"]["i_dn"] and rq["state"] == "DEAD"
          and rq2["state"] == "REVERSE", (rq["state"], rq2["state"]), cover=["BND-REV-DELTA-EQ-E"])
    for n in (80, 96, 213):
        dy = all((p_up(k, n) <= ALPHA) == (p_up(k, n) < ALPHA) and p_up(k, n) != ALPHA for k in range(n + 1))
        B.chk(f"P ≤ α ≡ P < α at n = {n} (a dyadic P never equals 1/100)", dy, n,
              cover=[f"BND-PLEALPHA-{n}"])
    agree = []
    for n in (32, 80):
        for k in range(n + 1):
            iv = cp_interval(k, n)
            agree.append(dead_pred(k, n) == (iv[1] < DEAD_P))
    for n, k in ((96, 52), (96, 53), (213, 124)):
        agree.append(dead_pred(k, n) == (cp_interval(k, n)[1] < DEAD_P))
    B.chk("DEAD's exact tail agrees with the bisected CP upper bound < .65 at every k of n = 32, 80 and the "
          "boundaries 96 (52, 53) and 213 (124)", all(agree), f"{sum(agree)}/{len(agree)}",
          cover=["BND-DEAD-CP-AGREE"])
    r = arm_outcome(40, 15, 40, 14, 32, 16)
    B.chk("order: 29/80 meets REVERSE and DEAD -> REVERSE", r["state"] == "REVERSE" and r["pred"]["dead"],
          r["state"], cover=["ORD-REV-OVER-DEAD"])
    pd_ = arm_outcome(107, 62, 106, 62, 32, 16)
    B.chk("order: n = 213, k = 124 (maps 62/107 + 62/106) meets PASS and DEAD -> PASS",
          pd_["state"] == "PASS" and pd_["pred"]["dead"] and dec(pd_["stats"]["p_up"]) == "0.0098"
          and dec(pd_["stats"]["dead_tail"]) == "0.0236", (pd_["state"], dec(pd_["stats"]["p_up"])),
          cover=["ORD-PASS-OVER-DEAD"])
    nr = arm_outcome(40, 30, 40, 30, 0, 0)
    w = arm_outcome(40, 30, 40, 30, 32, 16)
    B.chk("order: a sham with no domain session gives no read even where the contrast data would PASS",
          nr["state"] == "INDETERMINATE" and nr["noread"] == "sham-empty" and w["state"] == "PASS",
          (nr["state"], w["state"]), cover=["ORD-NOREAD-FIRST"])
    rec = {"schema": NOT_RUN_RECORD_SCHEMA, "unit": "Q-F0", "cause": "clock:pi-declined", "also": [],
           "date": CLOCK_DATE, "detail": "battery", "decisions_with_other_outcomes_known": []}
    su = unit_state("Q-F0", {"kind": "not-run", "record": rec})
    B.chk("order: unit outcome first -- a NOT-RUN unit emits no arm outcome",
          su[0] == "NOT-RUN" and "state" not in su[1] and coordinate(su) == "NOT-RUN", su[0],
          cover=["ORD-UNIT-FIRST"])
    B.chk("signed display: -1/20 -> '-0.0500', +1/20 -> '+0.0500', 0 -> '+0.0000'; bars._dec misprints the "
          "negative (why sdec exists)", sdec(Fraction(-1, 20)) == "-0.0500" and sdec(Fraction(1, 20)) == "+0.0500"
          and sdec(0) == "+0.0000" and bars._dec(Fraction(-1, 20)) != "-0.0500",
          (sdec(Fraction(-1, 20)), bars._dec(Fraction(-1, 20))), cover=["SIGN-DISPLAY"])


def _bt_power(B: _Battery) -> None:
    p1, p2 = power_exact(48, 48, 32), power_exact(40, 40, 32)
    B.chk("power (48, 48, 32) = .9161 (m:190's .916 at (96, 32))", dec(p1) == "0.9161" and dec(p1, 3) == "0.916",
          dec(p1), cover=["PWR-916"])
    B.chk("power (40, 40, 32) = .8784 (m:190's .878 at (80, 32))", dec(p2) == "0.8784" and dec(p2, 3) == "0.878",
          dec(p2), cover=["PWR-878"])
    B.chk("power is 0 with a map or the sham empty",
          power_exact(0, 80, 32) == power_exact(40, 40, 0) == 0 and power_exact(1, 1, 1) >= 0,
          cover=["PWR-ZERO-EMPTYMAP"])
    brute_ok = []
    for n0, n1, mS in ((5, 6, 4), (7, 7, 6), (3, 9, 5)):
        tot = Fraction(0)
        for k0 in range(n0 + 1):
            for k1 in range(n1 + 1):
                for j in range(mS + 1):
                    if arm_outcome(n0, k0, n1, k1, mS, j, alpha=bars.q("0.05"))["state"] == "PASS":
                        tot += (Fraction(comb(n0, k0) * 7 ** k0 * 3 ** (n0 - k0), 10 ** n0)
                                * Fraction(comb(n1, k1) * 7 ** k1 * 3 ** (n1 - k1), 10 ** n1)
                                * Fraction(comb(mS, j), 2 ** mS))
        brute_ok.append(tot == power_exact(n0, n1, mS, alpha=bars.q("0.05")))
    mut = power_exact(5, 6, 4, alpha=bars.q("0.05"), p=Fraction(6, 10)) != power_exact(5, 6, 4, alpha=bars.q("0.05"))
    B.chk("power equals a brute-force sum of arm_outcome's PASS over the full (k0, k1, j) space (3 shapes, "
          "α .05); a different share gives a different figure", all(brute_ok) and mut, brute_ok,
          cover=["PWR-BRUTE"])
    blk = power_block(10, 70, 32)
    B.chk("the figure of record is m:190's n/2 split at the realised n (80 -> 40/40: .878); the realised "
          "10/70 split is reported beside and differs", blk["of_record"]["display"] == "0.878"
          and blk["of_record"]["split"] == [40, 40] and blk["realised_split"]["display"] != "0.878"
          and power_block(0, 81, 32)["of_record"]["split"] == [40, 41],
          (blk["of_record"]["display"], blk["realised_split"]["display"]), cover=["PWR-RECORD-VS-REALISED"])
    # odd n: the figure of record is the floor / ceil split's own figure (both realised splits of 81
    # give it), and it differs from the even splits on either side (so a dropped session is caught)
    odd = [power_block(0, 81, 32)["of_record"], power_block(81, 0, 32)["of_record"]]
    p4041, p4040, p4141 = power_exact(40, 41, 32), power_exact(40, 40, 32), power_exact(41, 41, 32)
    B.chk("odd n: the figure of record at n = 81 is the 40 / 41 split's exact figure (from either realised split), "
          "distinct from 40 / 40 and 41 / 41", all(o["exact"] == fs(p4041) and o["split"] == [40, 41] for o in odd)
          and len({p4041, p4040, p4141}) == 3, (odd[0]["display"], dec(p4040, 3), dec(p4141, 3)),
          cover=["PWR-ODD-N"])


_GUARD_Q = {"reached": True, "label": "the end look at 112 launches", "source": "end_look",
            "at_stop": False,
            "fisher": {"name": "f", "p": "1/2", "fired": False, "binding": True},
            "abs": {"name": "a", "p": "1/100", "fired": True, "exceeds": True, "binding": True}}
_GUARD_O = {**_GUARD_Q, "abs": {"name": "a", "p": "1/100", "fired": False, "exceeds": True, "binding": False}}


def _bt_sentences(B: _Battery) -> None:
    def S(U, n0, k0, n1, k1, mS, j, guard=_GUARD_Q, floors=None, launched=None, prepick=None):
        c, s = keys.templates(U)
        out = arm_outcome(n0, k0, n1, k1, mS, j)
        counts = {"launched": launched or {c: n0 + n1 + 4, s: mS + 2},
                  "prepick": prepick or {c: 4, s: 2}}
        fl = floors or {c: n0 + n1, s: mS}
        return verdict_sentence(U, out, counts, guard, fl, power_block(n0, n1, mS)), out
    s_pass, _ = S("Q-F0", 40, 28, 40, 28, 32, 16)
    want_pass = ("A0 (Q-F0): PASS; n = 80 domain sessions of 84 launched (map 0: 28/40, map 1: 28/40 on the "
                 "clean-role label); P = 56/80 = 0.7000; Δ_c = +0.2000, two-sided Clopper–Pearson 95% CI "
                 "[+0.0872, +0.2974]; E = 0.0000 from A0s (16/32 domain sessions, P_sham = 0.5000); "
                 "P_arm − P_sham = +0.2000; exact one-sided binomial vs 0.5: p = 0.0002 toward clean, "
                 "p = 0.9999 toward corrupted, α = .01; pre-pick exclusion rate 4/84 = 0.0476 beside A0s's "
                 "2/34 = 0.0588; the guard at the unit's last look (the end look at 112 launches): Fisher "
                 "one-sided vs A0s p = 0.5000, not fired (binding); absolute vs .20 p = 0.0100, fired "
                 "(binding).")
    B.chk("sentence PASS: the exact text (every mandated clause, in order)", s_pass == want_pass,
          s_pass if s_pass != want_pass else "", cover=["SENT-PASS", "SENT-PREPICK", "SENT-GUARD-QWEN-BINDING",
                                                         "SENT-FLOOR-ABSENT"])
    s_rev, _ = S("Q-F0", 40, 12, 40, 12, 32, 16)
    B.chk("sentence REVERSE: state word and 'instruction inversion; reported; not-PASS for licensing'",
          s_rev.startswith("A0 (Q-F0): REVERSE; ") and "; instruction inversion; reported; not-PASS for "
          "licensing; pre-pick" in s_rev and "instruction inversion" not in s_pass, s_rev[:40],
          cover=["SENT-REVERSE"])
    s_dead, _ = S("OLMo-dpo", 40, 20, 40, 20, 32, 16, guard=_GUARD_O)
    B.chk("sentence DEAD on OLMo: the absolute bar 'reported only', Fisher 'binding'",
          s_dead.startswith("A0-OLMo-dpo (OLMo-dpo): DEAD; ") and "absolute vs .20 p = 0.0100, P ≤ α (reported "
          "only)" in s_dead and "(binding); absolute" in s_dead and "reported only" not in s_pass,
          s_dead[-80:], cover=["SENT-DEAD", "SENT-GUARD-OLMO-REPORTED"])
    s_ind, _ = S("Q-F0", 40, 24, 40, 24, 32, 16)
    B.chk("sentence INDETERMINATE (data): the state word and both p's, no REVERSE phrase",
          s_ind.startswith("A0 (Q-F0): INDETERMINATE; n = 80") and "toward corrupted" in s_ind
          and "no read obtained" not in s_ind, s_ind[:50], cover=["SENT-INDET"])
    s_nc, _ = S("OLMo-sft", 0, 0, 0, 0, 32, 16, floors={"A0-OLMo-sft": 80, "A0s-OLMo-sft": 32},
                launched={"A0-OLMo-sft": 5, "A0s-OLMo-sft": 34}, prepick={"A0-OLMo-sft": 5, "A0s-OLMo-sft": 2})
    want_nc = ("A0-OLMo-sft (OLMo-sft): INDETERMINATE, no read obtained (the arm has no domain session); "
               "n = 0 domain sessions of 5 launched (map 0: 0/0, map 1: 0/0 on the clean-role label); E = "
               "0.0000 from A0s-OLMo-sft (16/32 domain sessions, P_sham = 0.5000); P_arm − P_sham = undefined "
               "(no arm domain session); pre-pick exclusion rate 5/5 = 1.0000 beside A0s-OLMo-sft's 2/34 = "
               "0.0588; the guard at the unit's last look (the end look at 112 launches): Fisher one-sided vs "
               "A0s-OLMo-sft p = 0.5000, not fired (binding); absolute vs .20 p = 0.0100, fired (binding); "
               "below floor: A0-OLMo-sft 0/80, shortfall 80; A0s-OLMo-sft 32/32, shortfall 0; attained power "
               "0.000 at the realised n (m:190's base case: n/2 per map at P = .70, the sham pooled at .5, "
               "α .01); 0.000 at the realised map split.")
    B.chk("sentence no read (contrast empty): 'no read obtained' with its sub-reason, below-floor clause with "
          "shortfall and power", s_nc == want_nc, s_nc if s_nc != want_nc else "",
          cover=["SENT-NOREAD-CONTRAST", "SENT-FLOOR-PRESENT"])
    s_ns, _ = S("Q-F0", 40, 28, 40, 28, 0, 0, guard={"reached": False, "label": "no look reached",
                                                     "source": None, "at_stop": True},
                floors={"A0": 80, "A0s": 32})
    B.chk("sentence no read (sham empty): 'its sham A0s has no domain session, so E is undefined'; 'no look "
          "reached'", s_ns.startswith("A0 (Q-F0): INDETERMINATE, no read obtained (its sham A0s has no domain "
                                      "session, so E is undefined); ")
          and "the guard at the unit's last look: no look reached" in s_ns and "E = " not in s_ns
          and "below floor: A0 80/80, shortfall 0; A0s 0/32, shortfall 32" in s_ns, s_ns[-120:],
          cover=["SENT-NOREAD-SHAM", "SENT-NOLOOK"])


def _bt_notrun(B: _Battery) -> None:
    def rec(U, cause, also=()):
        return {"schema": NOT_RUN_RECORD_SCHEMA, "unit": U, "cause": cause, "also": list(also), "date": CLOCK_DATE,
                "detail": "battery", "decisions_with_other_outcomes_known": []}

    def labels_ok(U, reason):
        t = ["PASS", "PASS", "PASS", "PASS"]
        t[UNITS.index(U)] = "NOT-RUN"
        ls = label_set(tuple(t), {U: reason})
        if U == "Q-F0":
            return ls["e2a"] == ls["f1"] == PFX_F0 + "was not run: " + reason and unit_rows(U, ("NOT-RUN", reason)) \
                == {"e2a": ls["e2a"], "f1": ls["f1"]}
        return ls[f"olmo-{_ckpt(U)}"] == PFX_O + "was not run: " + reason
    for U in UNITS:
        codes = ["clock:pi-declined", "clock:k-zero", f"clock:gate-stopped:{gate_stop_stages(U)[-1]}",
                 "clock:not-locked:" + ("G-CAL" if U == "Q-F0" else f"G-TIME-OLMo-{_ckpt(U)}")]
        if U != "Q-F0":
            codes += ["clock:no-box", "dose-not-completable"]
        for code in codes:
            st = unit_state(U, {"kind": "not-run", "record": rec(U, code)})
            reason = st[1]["reason"]
            base = parse_cause(code)[0]
            B.chk(f"NOT-RUN {U} by {code}: every cell NOT-RUN, reason recorded, label 'was not run: <reason>'",
                  st[0] == "NOT-RUN" and coordinate(st) == "NOT-RUN" and reason == not_run_reason(U, code, CLOCK_DATE)
                  and labels_ok(U, reason), reason, cover=[f"NR-{base}-{U}"])
        for ended, bar, code in (("CAP", None, "no-first-read:cap"), ("PI-STOP", None, "no-first-read:pi-stop"),
                                 ("STOP", "template_breakage", "no-first-read:gver-stop")):
            st = unit_state(U, {"kind": "campaign", "ended": ended, "stop_bar": bar, "pi_stop_record": False,
                                "counts": {"n0": 0, "k0": 0, "n1": 0, "k1": 0, "mS": 0, "j": 0}})
            B.chk(f"NOT-RUN {U} by {code} (no session reached a first read before the {ended})",
                  st[0] == "NOT-RUN" and st[1]["code"] == code and labels_ok(U, st[1]["reason"]),
                  st[1]["reason"], cover=[f"NR-{code}-{U}"])
        if U != "Q-F0":
            st = unit_state(U, {"kind": "not-run", "record": {**rec(U, "pending-closed-at-v2")}})
            reason = st[1]["reason"]
            refused = False
            with tempfile.TemporaryDirectory() as td:
                d = Path(td)
                (d / f"{U}_NOT-RUN.json").write_text(json.dumps({"reason": reason, "cause": "pending-closed-at-v2"}))
                try:
                    _bt_posting_call(d, U, reason)
                except AnlRefusal as e:
                    refused = "pending-closed-at-v2" in str(e)
            B.chk(f"NOT-RUN {U} pending-closed-at-v2 reaches the state function; the v1 posting refuses it",
                  st[0] == "NOT-RUN" and refused, reason, cover=[f"NR-pending-closed-at-v2-{U}"])
    # the STOP routes of a campaign with no first read: a hair-trigger STOP disposed by a PI-stop record
    # follows the PI-stop rule (PIN-8); either G-VER bar is a G-VER STOP (m:284)
    z = {"n0": 0, "k0": 0, "n1": 0, "k1": 0, "mS": 0, "j": 0}
    routes = {U: (unit_state(U, {"kind": "campaign", "ended": "STOP", "stop_bar": HAIR_BAR, "pi_stop_record": True,
                                 "counts": z})[1]["code"],
                  unit_state(U, {"kind": "campaign", "ended": "STOP", "stop_bar": "schedule_mismatch",
                                 "pi_stop_record": False, "counts": z})[1]["code"]) for U in UNITS}
    B.chk("NOT-RUN routing on a STOP with no first read: scaffold_absorption + PI-stop record -> "
          "no-first-read:pi-stop; schedule_mismatch -> no-first-read:gver-stop (every unit)",
          all(v == ("no-first-read:pi-stop", "no-first-read:gver-stop") for v in routes.values()),
          routes["Q-F0"], cover=["NR-STOP-ROUTING"])
    r1 = _bt_raises(lambda: not_run_reason("Q-F0", "clock:no-box", CLOCK_DATE))
    r2 = _bt_raises(lambda: not_run_reason("Q-F0", "dose-not-completable"))
    r3 = _bt_raises(lambda: not_run_reason("OLMo-sft", "clock:gate-stopped:G-PORT", CLOCK_DATE))
    r4 = _bt_raises(lambda: not_run_reason("OLMo-dpo", "clock:gate-stopped:G-ID-F0m", CLOCK_DATE))
    r5 = _bt_raises(lambda: not_run_reason("Q-F0", "clock:gate-stopped:G-ID-F3", CLOCK_DATE))
    r6 = _bt_raises(lambda: not_run_reason("Q-F0", "clock:not-locked:G-TIME-OLMo-sft", CLOCK_DATE))
    B.chk("refused: clock:no-box on Q-F0", r1[0], r1[1][:60], cover=["NR-REFUSE-no-box-Q-F0"])
    B.chk("refused: dose-not-completable on Q-F0", r2[0], r2[1][:60], cover=["NR-REFUSE-dose-Q-F0"])
    B.chk("refused: a <stage> that is not the unit's (G-PORT and G-ID-F0m on OLMo -- no G-ID, m:267; Q-F3's "
          "G-ID-F3 and an OLMo stage on Q-F0)", r3[0] and r4[0] and r5[0] and r6[0], r4[1][:60],
          cover=["NR-REFUSE-unknown-stage"])
    def reason_or_err(f):
        try:
            return f()
        except ValueError as e:
            return f"REFUSED {e}"
    gid = [reason_or_err(lambda c=c: not_run_reason("Q-F0", f"{c}:G-ID-F0m", CLOCK_DATE)) for c in PARAM_CAUSES]
    gid_also = reason_or_err(lambda: validate_not_run_record(rec("Q-F0", "clock:pi-declined",
                                                                 ("clock:gate-stopped:G-ID-F0m",)))["also"])
    B.chk("G-ID-F0m is a STOPping gate of Q-F0 (a hair-trigger fire or G-VER failure stops it, m:271, m:284): "
          "accepted as the primary cause and in `also`", gid[0].startswith("G-ID-F0m stopped")
          and gid[1].startswith("G-ID-F0m had not") and gid_also == ["clock:gate-stopped:G-ID-F0m"],
          gid[0][:60], cover=["NR-GATE-STOPPED-GID-Q-F0"])
    gcal = {U: reason_or_err(lambda U=U: not_run_reason(U, "clock:gate-stopped:G-CAL", CLOCK_DATE)) for U in UNITS}
    B.chk("G-CAL is a STOPping gate of every unit (it serves all units, m:176, m:276; the OLMo track starts "
          "at step 9, m:358): clock:gate-stopped:G-CAL accepted on Q-F0 and each OLMo checkpoint",
          all(v.startswith("G-CAL stopped") for v in gcal.values()), gcal["OLMo-sft"][:60],
          cover=["NR-GATE-STOPPED-GCAL-OLMO"])
    # every unit's label row equals its own output's row (unit_rows), for every coordinate it can have
    rows_ok = []
    for U in UNITS:
        for x in Q5:
            t = ["PASS", "PASS", "PASS", "PASS"]
            t[UNITS.index(U)] = x
            why = not_run_reason(U, "clock:k-zero", CLOCK_DATE) if x == "NOT-RUN" else None
            ls = label_set(tuple(t), {U: why} if why else {})
            ur = unit_rows(U, (x, why))
            if U == "Q-F0":
                rows_ok.append(ur == {"e2a": ls["e2a"], "f1": ls["f1"]})
            else:
                rows_ok.append(ur == {f"olmo-{_ckpt(U)}": ls[f"olmo-{_ckpt(U)}"], "state": x})
    B.chk("unit_rows (a unit's own VERDICTS / NOT-RUN rows) equals label_set's row for every unit and every "
          "state in Q5 (OLMo DEAD / REVERSE / NOT-RUN included)", all(rows_ok) and len(rows_ok) == 20,
          f"{sum(rows_ok)}/{len(rows_ok)}", cover=["ROWS-EQ-LABELSET"])
    ok_v2 = True
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        rp = d / "rec.json"
        rp.write_text(json.dumps(rec("OLMo-dpo", "pending-closed-at-v2")))
        try:
            run_not_run("OLMo-dpo", rp, None, None, d, _bt_env(d))
            ok_v2 = False
        except AnlRefusal:
            pass
    B.chk("refused: the not-run command takes no pending-closed-at-v2 record at v1", ok_v2,
          cover=["NR-REFUSE-v2-at-v1"])
    # PENDING
    for U in UNITS[1:]:
        for sub in PENDING_SUBSTATES:
            st = unit_state(U, {"kind": "pending", "decl": {"state": "PENDING", "substate": sub,
                                                            "clock_passed": False, "date": "2026-10-20"},
                                "verdicts_exists": False, "notrun_exists": False})
            ls = label_set(("PASS", *(["PENDING" if u == U else "PASS" for u in UNITS[1:]])), {})
            B.chk(f"PENDING {U} {sub}", st == ("PENDING", sub)
                  and ls[f"olmo-{_ckpt(U)}"] == PFX_O + "is pre-registered and pending at this posting",
                  st, cover=[f"PEND-{sub}-{U}"])
    pd_ = {"state": "PENDING", "substate": "unlocked-before-D_O", "clock_passed": True, "date": "2026-11-02"}
    B.chk("PENDING refused: unlocked-before-D_O with the Clock passed (NOT-RUN by its Clock)",
          _bt_raises(lambda: pending_state("OLMo-sft", pd_, verdicts_exists=False, notrun_exists=False))[0],
          cover=["PEND-CLOCK-REFUSED"])
    ok_ = {"state": "PENDING", "substate": "locked-running", "clock_passed": True, "date": "2026-11-02"}
    B.chk("PENDING refused where a VERDICTS output exists",
          _bt_raises(lambda: pending_state("OLMo-dpo", ok_, verdicts_exists=True, notrun_exists=False))[0]
          and pending_state("OLMo-dpo", ok_, verdicts_exists=False, notrun_exists=False) == "locked-running",
          cover=["PEND-VERDICTS-REFUSED"])
    B.chk("PENDING refused where a NOT-RUN output exists",
          _bt_raises(lambda: pending_state("OLMo-dpo", ok_, verdicts_exists=False, notrun_exists=True))[0],
          cover=["PEND-NOTRUN-REFUSED"])
    B.chk("PENDING refused for Q-F0",
          _bt_raises(lambda: pending_state("Q-F0", ok_, verdicts_exists=False, notrun_exists=False))[0],
          cover=["PEND-QF0-REFUSED"])
    # the Clock comparison's date beside clock_passed (decision 2): required, YYYY-MM-DD, and recorded
    # as given on either side of D_O and on the boundary day -- the boundary-day comparison is settled
    # by the seat (C7, 2026-10-10): committed by the Clock date iff the commit's committer date, in UTC,
    # falls on or before it (the day inclusive, to 23:59:59 UTC); it remains a declared input, so no
    # date-vs-D_O consistency is imposed (PIN-6)
    no_date = {k_: v for k_, v in ok_.items() if k_ != "date"}
    bad_dates = [_bt_raises(lambda d=d: pending_state("OLMo-dpo", {**ok_, "date": d}, verdicts_exists=False,
                                                      notrun_exists=False))[0]
                 for d in ("2026/11/02", "02 Nov 2026", None, 20261102)]
    given = [pending_state("OLMo-dpo", {**ok_, "clock_passed": cp_, "date": d}, verdicts_exists=False,
                           notrun_exists=False) for cp_ in (True, False) for d in ("2026-10-29", CLOCK_DATE, "2026-11-02")]
    B.chk("PENDING: the Clock comparison's date is required beside clock_passed (a declaration without it, or with "
          "a date not YYYY-MM-DD, is refused); either clock_passed is accepted on either side of D_O and on it",
          _bt_raises(lambda: pending_state("OLMo-dpo", no_date, verdicts_exists=False, notrun_exists=False))[0]
          and all(bad_dates) and given == ["locked-running"] * 6, (bad_dates, len(given)), cover=["PEND-DATE"])
    # the date is exactly YYYY-MM-DD (a full match): a character before or after it refuses, under either
    # clock_passed; the bare date is accepted under both
    def pend_refused(decl):
        return _bt_raises(lambda: pending_state("OLMo-dpo", decl, verdicts_exists=False, notrun_exists=False))[0]
    trail = ("2026-11-02x", "2026-11-02 ", "2026-11-02\n", "2026-11-022", " 2026-11-02", "x2026-11-02")
    tr_ref = [pend_refused({**ok_, "clock_passed": cp_, "date": d}) for cp_ in (True, False) for d in trail]
    tr_acc = [pending_state("OLMo-dpo", {**ok_, "clock_passed": cp_, "date": "2026-11-02"}, verdicts_exists=False,
                            notrun_exists=False) for cp_ in (True, False)]
    B.chk("PENDING: a date with a character beyond YYYY-MM-DD (a trailing x, space or newline, a third day digit, a "
          "leading space or letter) is refused under clock_passed true and false; the bare 2026-11-02 is accepted "
          "under both", all(tr_ref) and len(tr_ref) == 12 and tr_acc == ["locked-running"] * 2,
          (sum(tr_ref), tr_acc), cover=["PEND-DATE-TRAILING"])
    # the date check does not depend on clock_passed: with it false, a malformed date refuses on every sub-state
    malformed = ("2026/11/02", "02 Nov 2026", None, 20261102, "2026-11-2", "")
    cf_ref = [pend_refused({**ok_, "substate": s_, "clock_passed": False, "date": d})
              for s_ in PENDING_SUBSTATES for d in malformed]
    cf_acc = [pending_state("OLMo-dpo", {**ok_, "substate": s_, "clock_passed": False, "date": CLOCK_DATE},
                            verdicts_exists=False, notrun_exists=False) for s_ in PENDING_SUBSTATES]
    B.chk("PENDING with clock_passed false: a malformed date (slashes, words, None, an int, a one-digit day, empty) "
          "is refused on every sub-state, as under true; a YYYY-MM-DD date is accepted on every sub-state",
          all(cf_ref) and len(cf_ref) == 6 * len(PENDING_SUBSTATES) and cf_acc == list(PENDING_SUBSTATES),
          (sum(cf_ref), cf_acc), cover=["PEND-DATE-CLOCK-FALSE"])
    # a PENDING declaration has exactly its four keys: an extra key refuses, directly and through the
    # cross-check the posting and Q-F0's V10 apply to a PENDING coordinate (crosscheck_coordinate)
    extras = ({"note": "battery"}, {"reason": "pending (battery)"}, {"cause": "clock:pi-declined"})
    ex_ref = [pend_refused({**ok_, **e}) for e in extras]
    with tempfile.TemporaryDirectory() as td:
        bare = {k_: v for k_, v in ok_.items() if k_ != "state"}
        cc_ref = [_bt_raises(lambda e=e: crosscheck_coordinate("OLMo-dpo", "PENDING", None, {**bare, **e}, Path(td)),
                             (AnlRefusal,))[0] for e in extras]
        cc_acc = crosscheck_coordinate("OLMo-dpo", "PENDING", None, bare, Path(td)) is None
    B.chk("PENDING: a declaration with a key beyond {state, substate, clock_passed, date} (note, reason, cause) is "
          "refused, directly and through the posting's / V10's cross-check; exactly the four keys are accepted",
          all(ex_ref) and all(cc_ref) and cc_acc and pend_refused(ok_) is False,
          (ex_ref, cc_ref, cc_acc), cover=["PEND-EXTRA-KEYS"])
    # decisions (PIN-35)
    dd = [{"decision": "OLMo-dpo cap kept", "date": "2026-10-20", "other_unit": "Q-F0", "other_state": "PASS"}]
    r_ = validate_not_run_record({**rec("OLMo-dpo", "clock:pi-declined"), "decisions_with_other_outcomes_known": dd})
    B.chk("decisions with another unit's outcome known: a non-empty list is carried verbatim",
          r_["decisions"] == dd and decisions_file({"schema": DECISIONS_SCHEMA, "unit": "OLMo-dpo",
                                                    "decisions_with_other_outcomes_known": dd}, "OLMo-dpo") == dd,
          cover=["DEC-CARRIED"])
    bad = dict(rec("OLMo-dpo", "clock:pi-declined"))
    del bad["decisions_with_other_outcomes_known"]
    B.chk("decisions: a missing key is refused (record and file); a decision naming its own unit is refused",
          _bt_raises(lambda: validate_not_run_record(bad))[0]
          and _bt_raises(lambda: decisions_file({"schema": DECISIONS_SCHEMA, "unit": "Q-F0"}, "Q-F0"))[0]
          and _bt_raises(lambda: validate_decisions([{**dd[0], "other_unit": "OLMo-dpo"}], "OLMo-dpo"))[0],
          cover=["DEC-MISSING-REFUSED"])
    f3 = [{"decision": "OLMo-instruct PI-stopped (§7.3)", "date": "2026-12-01", "other_unit": "Q-F3",
           "other_state": {"A1": "PASS", "A2": "FAIL", "A3": "POSITIVE"}},
          {"decision": "OLMo-dpo closed at v2", "date": "2027-01-10", "other_unit": "Q-F3",
           "other_state": {"A1": "PASS", "A2": "PASS", "A3": "POSITIVE", "A3*": "CONFIRMED"}},
          {"decision": "OLMo-sft cap kept", "date": "2026-12-02", "other_unit": "Q-F3", "other_state": "NOT-RUN"}]
    try:
        acc = validate_decisions(f3, "OLMo-instruct") == f3
    except ValueError as e:
        acc = f"REFUSED {e}"[:80]
    bads = [[{**f3[0], "other_state": "PASS"}], [{**f3[0], "other_state": {"A1": "PASS", "A2": "DEAD", "A3": "NULL"}}],
            [{**f3[0], "other_state": {"A1": "PASS", "A3": "NULL"}}], [{**dd[0], "other_state": "PENDING"}],
            [{**dd[0], "other_unit": "OLMo-sft", "other_state": "PENDING"}], [{**dd[0], "other_unit": "Q-F9"}]]
    refused = [_bt_raises(lambda b=b: validate_decisions(b, "OLMo-dpo"))[0] for b in bads]
    B.chk("decisions: Q-F3 is an other_unit (its NOT-RUN, or A1/A2/A3[/A3*] in m:326's and m:340's words) and "
          "is carried verbatim; a bare word, a foreign A-word, a missing A2, PENDING (no VERDICTS exist, m:318) "
          "and an unknown unit are refused", acc is True and all(refused), (acc, refused), cover=["DEC-QF3-PENDING"])
    # the decisions file names its own unit; a decision's date is YYYY-MM-DD (both directions)
    dfile = {"schema": DECISIONS_SCHEMA, "unit": "OLMo-dpo", "decisions_with_other_outcomes_known": dd}
    own = decisions_file(dfile, "OLMo-dpo") == dd
    other_unit = _bt_raises(lambda: decisions_file(dfile, "OLMo-sft"))
    bad_d = [_bt_raises(lambda d=d: validate_decisions([{**dd[0], "date": d}], "OLMo-dpo"))[0]
             for d in ("2026/10/20", "20 Oct 2026", "2026-10-2", None)]
    B.chk("decisions: a decisions file naming another unit is refused (its own is accepted); a decision dated other "
          "than YYYY-MM-DD is refused (2026-10-20 accepted)", own and other_unit[0] and all(bad_d),
          (other_unit[1][:50], bad_d), cover=["DEC-UNIT-DATE"])
    # a decision's date is exactly YYYY-MM-DD (a full match), in the list, the decisions file and the NOT-RUN record
    d_trail = ("2026-10-20x", "2026-10-20 ", "2026-10-20\n", "2026-10-200")
    dt_list = [_bt_raises(lambda d=d: validate_decisions([{**dd[0], "date": d}], "OLMo-dpo"))[0] for d in d_trail]
    dt_file = [_bt_raises(lambda d=d: decisions_file({**dfile, "decisions_with_other_outcomes_known":
                                                      [{**dd[0], "date": d}]}, "OLMo-dpo"))[0] for d in d_trail]
    dt_rec = [_bt_raises(lambda d=d: validate_not_run_record({**rec("OLMo-dpo", "clock:pi-declined"),
                                                              "decisions_with_other_outcomes_known":
                                                              [{**dd[0], "date": d}]}))[0] for d in d_trail]
    B.chk("decisions: a decision date with a character beyond YYYY-MM-DD (a trailing x, space or newline, a third day "
          "digit) is refused -- in the list, the decisions file and the NOT-RUN record; 2026-10-20 is accepted in each",
          all(dt_list) and all(dt_file) and all(dt_rec) and validate_decisions(dd, "OLMo-dpo") == dd
          and decisions_file(dfile, "OLMo-dpo") == dd and r_["decisions"] == dd, (dt_list, dt_file, dt_rec),
          cover=["DEC-DATE-TRAILING"])
    # PIN-43: dates are ASCII and real calendar dates, in all three validators; a NOT-RUN record's date is checked
    # whatever its cause (dose-not-completable's phrase has no {date})
    unreal = ("\uff12\uff10\uff12\uff16-\uff11\uff11-\uff10\uff12", "2026-02-30", "2026-13-01", "2026-00-10",
              "20261030", "2026-W44-5", "2026-02-29", "1900-02-29")
    real = ("2026-02-28", "2024-02-29", "2000-02-29", "2026-10-30")
    pend_ok = {"state": "PENDING", "substate": "locked-running", "clock_passed": False}
    u_pend = [_bt_raises(lambda d=d: pending_state("OLMo-dpo", {**pend_ok, "date": d}, verdicts_exists=False,
                                                   notrun_exists=False))[0] for d in unreal]
    a_pend = [pending_state("OLMo-dpo", {**pend_ok, "date": d}, verdicts_exists=False, notrun_exists=False)
              for d in real]
    u_dec = [_bt_raises(lambda d=d: validate_decisions([{**dd[0], "date": d}], "OLMo-dpo"))[0] for d in unreal]
    a_dec = [validate_decisions([{**dd[0], "date": d}], "OLMo-dpo")[0]["date"] for d in real]
    u_why = [_bt_raises(lambda d=d: not_run_reason("Q-F0", "clock:pi-declined", d))[0] for d in unreal]
    B.chk("dates (PIN-43): full-width digits, the basic and week forms (20261030, 2026-W44-5) and impossible days "
          "(02-30, the non-leap 2026-02-29 and 1900-02-29, month 13, month 00) are refused by the PENDING, decision and "
          "Clock-date validators; 2026-02-28, the leap days 2024-02-29 and 2000-02-29 and 2026-10-30 are accepted",
          all(u_pend) and all(u_dec) and all(u_why) and a_pend == ["locked-running"] * 4 and a_dec == list(real),
          (u_pend, u_dec, u_why, a_pend, a_dec), cover=["DATE-ISO-REAL"])
    nr_bad = [_bt_raises(lambda d=d: validate_not_run_record({**rec("OLMo-dpo", "dose-not-completable"),
                                                              "date": d}))[0] for d in (None, "2026-02-30", "")]
    nr_ok = validate_not_run_record({**rec("OLMo-dpo", "dose-not-completable"), "date": "2026-10-30"})
    B.chk("NOT-RUN record (PIN-43): a dose-not-completable record dated None, 2026-02-30 or '' is refused although its "
          "reason phrase has no {date}; dated 2026-10-30 it is accepted and the date is carried",
          all(nr_bad) and nr_ok["date"] == "2026-10-30", (nr_bad, nr_ok["date"]), cover=["NR-RECORD-DATE"])
    # PIN-43: a declared OLMo NOT-RUN state in --olmo-states is date-checked whatever its cause (its date is carried
    # into Q-F0's VERDICTS olmo_states_declared)
    with tempfile.TemporaryDirectory() as td_:
        od_ = Path(td_)
        _bt_olmo_outputs(od_)
        def ost(d, cause="dose-not-completable"):
            return {"schema": OLMO_STATES_SCHEMA, "states": {
                "OLMo-sft": {"state": "PENDING", "substate": "locked-running", "clock_passed": False,
                             "date": CLOCK_DATE},
                "OLMo-dpo": {"state": "NOT-RUN", "cause": cause, "date": d},
                "OLMo-instruct": {"state": "DEAD"}}}
        os_bad = [_bt_raises(lambda d=d: _validate_olmo_states(ost(d), od_))[0]
                  for d in (None, "", "2026-02-30", "\uff12\uff10\uff12\uff16-\uff11\uff10-\uff13\uff10", "20261030", 12345)]
        # whatever the cause: a no-first-read cause (no {date} in its phrase either) refuses a bad date too; the date
        # check fires before the cross-check against the unit's NOT-RUN output
        os_bad += [_bt_raises(lambda d=d: _validate_olmo_states(ost(d, "no-first-read:cap"), od_))[0]
                   for d in (None, "2026-02-30")]
        os_ok = _validate_olmo_states(ost(CLOCK_DATE), od_)
    B.chk("OLMo states (PIN-43): a declared dose-not-completable NOT-RUN state dated None, '', 2026-02-30, full-width "
          "digits, 20261030 or 12345 is refused although its reason phrase has no {date}, and so is a no-first-read:cap "
          "state dated None or 2026-02-30; dated 2026-10-30 it is accepted and the date is carried in the declaration",
          all(os_bad) and len(os_bad) == 8 and os_ok[2]["OLMo-dpo"]["date"] == CLOCK_DATE and os_ok[0]["OLMo-dpo"] == "NOT-RUN",
          (os_bad, os_ok[2]["OLMo-dpo"]), cover=["OLMO-STATES-DATE"])


def _bt_posting_call(d: Path, U: str, reason: str) -> None:
    """A v1 posting whose U coordinate is NOT-RUN with `reason` (others PENDING-free); for refusals."""
    t = {u: ("NOT-RUN" if u == U else "PASS") for u in UNITS}
    for u in UNITS:
        if u != U:
            (d / f"{u}_VERDICTS.json").write_text(json.dumps({"arm": {"state": "PASS"}}))
    tp = d / "tuple.json"
    tp.write_text(json.dumps({"schema": TUPLE_SCHEMA, "posting": "v1", "tuple": t, "reasons": {U: reason},
                              "pending": {}}))
    run_posting(tp, d / "nope.json", d / "nope-flag.json", d, d, _bt_env(d))


# --- battery: the 1,080 tuples ------------------------------------------------------------------
def _bt_oracle(t: tuple, flag: bool, table: Mapping, whys: Mapping | None = None) -> dict:
    """An independent second implementation of the v1 outputs (table-driven). ``whys``: a per-unit
    NOT-RUN reason (default: the PI-declined phrase for every unit, the 1,080-tuple pass's)."""
    q, s, d, i = t
    why = "the PI declined to commit its LOCK v1.0 by its Clock date (2026-10-30)"
    wy = {u: (whys or {}).get(u, why) for u in ("Q-F0", "OLMo-sft", "OLMo-dpo", "OLMo-instruct")}
    L = dict(zip(("L0", "L0-OLMo-sft", "L0-OLMo-dpo", "L0-OLMo-instruct"), (x == "PASS" for x in t)))
    head = "concluded, not answered — the told control "

    def f0(x):
        return {"PASS": "Answered", "NOT-RUN": f"{head}at F0 on this substrate was not run: {wy['Q-F0']}"}.get(
            x, f"{head}at F0 on this substrate did not pass: {x}")

    def ol(x, u):
        return {"PASS": "Answered", "NOT-RUN": f"{head}at this stage was not run: {wy[u]}",
                "PENDING": f"{head}at this stage is pre-registered and pending at this posting"}.get(
            x, f"{head}at this stage did not pass: {x}")
    labels = {"e2a": f0(q), "f1": f0(q), "e2b": LABEL_E2B, "olmo-base": LABEL_BASE,
              "olmo-sft": ol(s, "OLMo-sft"), "olmo-dpo": ol(d, "OLMo-dpo"), "olmo-instruct": ol(i, "OLMo-instruct")}
    cname = ["Fallback-2", "Fallback-1"][q == "PASS"]
    names = [w for w, x in zip(("SFT", "DPO", "instruct"), (s, d, i)) if x == "PASS"]
    if len(names) == 3:
        ab = "and not at the SFT, DPO or instruct stage of the OLMo lineage"
    elif len(names) == 0:
        ab = "; the OLMo lineage's post-training nulls are reported as concluded, not answered (§5.5)"
    else:
        ab = "and, on the OLMo lineage, not at the " + " or ".join(names) + " stage"
    tok = lambda x: {"NOT-RUN": "not run", "PENDING": "pending"}.get(x, x)
    s81 = f"A0 (Q-F0): {tok(q)}; A0-OLMo-sft: {tok(s)}; A0-OLMo-dpo: {tok(d)}; A0-OLMo-instruct: {tok(i)}"
    spans = [r["dose_note_span"] for r in table["rows"] if r["dose_note"]]
    dn = ({"status": "carried", "text": " | ".join(spans)} if flag and spans else
          {"status": "to be carried; absent from the table (§7.5(c))", "text": None} if flag else
          {"status": "none (struck, §7.5(c))", "text": None})
    cl = dict(labels, weight="concluded, not answered", S1="Answered, as recognition")
    crank = 2 if cname == "Fallback-1" else 1
    items = []
    for r in table["rows"]:
        a_cells = [c for c in r["null_cells"] if not cl[c].startswith("Answered")]
        fire_b = r["thesis"] is not None and {"main": 3, "fallback-1": 2, "fallback-2": 1}[r["thesis"]] > crank
        if flag:
            c_t = "carry" if (not spans and "f1-corr-line" in r["kinds"]) else None
        else:
            c_t = "strike" if r["dose_note"] else None
        cls = [x for x, on in (("a", a_cells), ("b", fire_b), ("c", c_t)) if on]
        if not cls:
            continue
        items.append({"row_id": r["id"], "loc": dict(r["loc"]), "clauses": cls,
                      "a": {"cells": [{"cell": c, "label": cl[c]} for c in a_cells]} if a_cells else None,
                      "b": {"thesis": r["thesis"], "ceiling": cname} if fire_b else None,
                      "c": {"flag": flag, "treatment": c_t} if c_t else None,
                      "treatments": [{"a": "assert no null on these cells",
                                      "b": "state as a reading proposed, not a result"}.get(x)
                                     or f"{c_t} the dose note" for x in cls]})
    return {"licensing": L, "labels": labels, "ceiling": {"name": cname, "title": TITLES[cname]},
            "abstract_clause": ab, "s81": s81, "step7": "open", "dose_note": dn, "enumeration": items}


def _bt_tuple_pass(table: Mapping) -> tuple[dict, str, dict, dict]:
    """Every (t, flag): the outputs; T1-T9 per evaluation (counted); returns tallies and the sha."""
    reasons_all = {u: not_run_reason(u, "clock:pi-declined", CLOCK_DATE) for u in UNITS}
    counts = {f"T{i}": [0, 0, 0, 0] for i in range(1, 10)}       # [ok T, total T, ok F, total F]
    fails: dict = {}
    # every content tally is kept per flag value, so each flag's T10 reads its own outputs
    tallies = {"tuples": {True: 0, False: 0}, "fires": {True: {}, False: {}},
               "by_flag": {f: {"L0": 0, "L0c": {c: 0 for c in keys.CKPTS}, "lic_vectors": set(),
                               "ceiling": {"Fallback-1": 0, "Fallback-2": 0},
                               "abstract": {"all": 0, "one": 0, "two": 0, "none": 0}, "abstract_texts": set(),
                               "f0": {"Answered": 0, "REVERSE": 0, "DEAD": 0, "INDETERMINATE": 0, "NOT-RUN": 0},
                               "olmo": {c: {"Answered": 0, "did-not-pass": 0, "not-run": 0, "pending": 0}
                                        for c in keys.CKPTS},
                               "s81": set(), "open": 0} for f in (True, False)}}
    h = hashlib.sha256()
    dose_first: dict = {}
    by_flag: dict = {}
    for flag in (True, False):
        for t in itertools.product(Q5, O6, O6, O6):
            reasons = {u: reasons_all[u] for u, x in zip(UNITS, t) if x == "NOT-RUN"}
            out = v1_outputs(t, reasons, flag, table)
            by_flag[(t, flag)] = out
            orc = _bt_oracle(t, flag, table)
            h.update((json.dumps({"t": list(t), "flag": flag, "outputs": out}, sort_keys=True,
                                 ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8"))
            col = 0 if flag else 2
            q, s, d, i = t
            res = {}
            # T1 licensing
            lic = out["licensing"]
            res["T1"] = (sorted(lic) == sorted(orc["licensing"]) and all(type(v) is bool for v in lic.values())
                         and lic == orc["licensing"] and not (q == "NOT-RUN" and lic["L0"]))
            # T2 labels
            alts_ok = True
            for row, x in (("e2a", q), ("f1", q), ("olmo-sft", s), ("olmo-dpo", d), ("olmo-instruct", i)):
                preds = [x == "PASS", x in ("REVERSE", "DEAD", "INDETERMINATE"), x == "NOT-RUN"]
                if row.startswith("olmo"):
                    preds.append(x == "PENDING")
                alts_ok &= sum(preds) == 1
            res["T2"] = (alts_ok and out["labels"] == orc["labels"] and list(out["labels"]) == list(ROWS)
                         and out["labels"]["e2b"] == LABEL_E2B and out["labels"]["olmo-base"] == LABEL_BASE)
            # T3 ceiling
            res["T3"] = (sum([lic["L0"], not lic["L0"]]) == 1 and out["ceiling"] == orc["ceiling"]
                         and out["ceiling"]["name"] != "Main"
                         and ceiling((q, "PASS", "PASS", "PASS")) == (out["ceiling"]["name"], out["ceiling"]["title"]))
            # T4 abstract
            k = sum(x == "PASS" for x in (s, d, i))
            res["T4"] = (sum([k == 3, 1 <= k <= 2, k == 0]) == 1 and out["abstract_clause"] == orc["abstract_clause"]
                         and abstract_clause(("NOT-RUN", s, d, i)) == out["abstract_clause"])
            # T5 §8.1
            cl = out["s81"].split("; ")
            res["T5"] = (len(cl) == 4 and all(c.startswith(nm + ": ") and c[len(nm) + 2:] in S81_TOKEN.values()
                                              for c, (nm, _) in zip(cl, S81_CONTROLS)) and out["s81"] == orc["s81"])
            # T6 step 7
            res["T6"] = out["step7"] == "open"
            # T7 dose note
            dose_first.setdefault(flag, out["dose_note"])
            res["T7"] = out["dose_note"] == orc["dose_note"] == dose_first[flag]
            # T8 enumeration
            ids = [it["row_id"] for it in out["enumeration"]]
            order = [r["id"] for r in table["rows"]]
            res["T8"] = (out["enumeration"] == orc["enumeration"] and all(it["clauses"] for it in out["enumeration"])
                         and ids == [x for x in order if x in ids]
                         and set(ids) == {it["row_id"] for it in orc["enumeration"]})
            # T9 flag invariance (needs both flags: checked in the second pass below)
            for kk in ("T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"):
                counts[kk][col] += bool(res[kk])
                counts[kk][col + 1] += 1
                if not res[kk]:
                    fails.setdefault(kk, (t, flag))
            # tallies
            tallies["tuples"][flag] += 1
            tf = tallies["by_flag"][flag]
            tf["L0"] += lic["L0"]
            for c in keys.CKPTS:
                tf["L0c"][c] += lic[f"L0-OLMo-{c}"]
            tf["lic_vectors"].add(tuple(lic.values()))

            def bump(d, key):
                d[key] = d.get(key, 0) + 1
            bump(tf["ceiling"], out["ceiling"]["name"])
            ac = out["abstract_clause"]
            bump(tf["abstract"], "all" if ac == ABSTRACT_ALL else "none" if ac == ABSTRACT_NONE
                 else ("two" if " or " in ac else "one") if ac.startswith("and, on the OLMo lineage, not at the ")
                 else "other")
            tf["abstract_texts"].add(ac)
            lab = out["labels"]
            bump(tf["f0"], "Answered" if lab["e2a"] == ANSWERED else "NOT-RUN" if "was not run: " in lab["e2a"]
                 else lab["e2a"].rsplit("did not pass: ", 1)[-1])
            for c in keys.CKPTS:
                lc = lab[f"olmo-{c}"]
                bump(tf["olmo"][c], "Answered" if lc == ANSWERED else "pending" if lc.endswith("pending at this posting")
                     else "not-run" if "was not run: " in lc else "did-not-pass")
            tf["s81"].add(out["s81"])
            tf["open"] += out["step7"] == "open"
            fr = tallies["fires"][flag]
            for it in out["enumeration"]:
                for c_ in it["clauses"]:
                    fr[(it["row_id"], c_)] = fr.get((it["row_id"], c_), 0) + 1
    for flag in (True, False):
        col = 0 if flag else 2
        for t in itertools.product(Q5, O6, O6, O6):
            a, b = by_flag[(t, flag)], by_flag[(t, not flag)]

            def strip(o):
                oo = {k_: v for k_, v in o.items() if k_ not in ("dose_note", "enumeration")}
                en = []
                for it in o["enumeration"]:
                    cls = [c for c in it["clauses"] if c != "c"]
                    if cls:
                        en.append({**{k_: v for k_, v in it.items() if k_ not in ("c", "clauses", "treatments")},
                                   "clauses": cls, "treatments": [x for c, x in zip(it["clauses"], it["treatments"])
                                                                  if c != "c"]})
                oo["enumeration"] = en
                return oo
            ok = strip(a) == strip(b)
            counts["T9"][col] += ok
            counts["T9"][col + 1] += 1
            if not ok:
                fails.setdefault("T9", (t, flag))
    return counts, h.hexdigest(), tallies, fails


def _bt_tuples(B: _Battery, table: Mapping) -> None:
    counts, sha, tal, fails = _bt_tuple_pass(table)
    B.extra["outputs_sha256"] = sha
    names = {"T1": "exactly one licensing state, equal to the oracle; NOT-RUN never licenses",
             "T2": "one label set (one alternative per row), equal to the oracle; e2b and base fixed",
             "T3": "one ceiling in {Fallback-1, Fallback-2}, never Main; the OLMo coordinates never enter",
             "T4": "one abstract clause of the three-way; Q-F0 never enters",
             "T5": "one §8.1 text, one token per control",
             "T6": "Step 7 'open'",
             "T7": "the dose note equals the oracle and is invariant over the tuple",
             "T8": "the §7.5 enumeration equals the oracle; no empty item; table order",
             "T9": "outputs under the two flag values differ only in the dose note and the (c) items"}
    total = 0
    for kk in ("T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9"):
        c = counts[kk]
        total += c[1] + c[3]
        for flag, col in ((True, 0), (False, 2)):
            B.chk(f"tuples {kk} flag={'T' if flag else 'F'}: {c[col]}/{c[col + 1]} tuples: {names[kk]}",
                  c[col] == c[col + 1] == 1080, fails.get(kk, ""), cover=[f"TUP-{kk}-{'T' if flag else 'F'}"])
    def agg(tf: Mapping) -> bool:
        return (tf["L0"] == 216 and all(v == 180 for v in tf["L0c"].values()) and len(tf["lic_vectors"]) == 16
                and tf["ceiling"] == {"Fallback-1": 216, "Fallback-2": 864}
                and tf["abstract"] == {"all": 5, "one": 375, "two": 75, "none": 625} and len(tf["abstract_texts"]) == 8
                and tf["f0"] == {"Answered": 216, "REVERSE": 216, "DEAD": 216, "INDETERMINATE": 216, "NOT-RUN": 216}
                and all(tf["olmo"][c] == {"Answered": 180, "did-not-pass": 540, "not-run": 180, "pending": 180}
                        for c in keys.CKPTS) and len(tf["s81"]) == 1080 and tf["open"] == 1080)
    common_ok = tal["tuples"] == {True: 1080, False: 1080} and total == 2160 * 9
    for flag, fl in ((True, "T"), (False, "F")):
        tf = tal["by_flag"][flag]
        B.chk(f"tuples T10 flag={fl}: 1,080 distinct tuples, 2,160 evaluations x 9 assertions; over the flag={fl} "
              f"outputs: L0 216; each L0-OLMo-c 180; 16 licensing vectors; Fallback-1 216 / Fallback-2 864; "
              f"abstract 5 / 450 (375 + 75) / 625, 8 texts; e2a/f1 216 per branch; OLMo rows 180 / 540 / 180 / 180; "
              f"1,080 §8.1 texts; 'open' 1,080", common_ok and agg(tf), (tf["ceiling"], tf["abstract"], total),
              cover=[f"TUP-T10-{fl}"])
    tt = tal["by_flag"][True]
    tal_out = {"tuples_per_flag": 1080, "evaluations": 2160, "assertions": total, "L0_true": tt["L0"],
               "L0_OLMo_c_true": dict(tt["L0c"]), "licensing_vectors": len(tt["lic_vectors"]),
               "ceiling": tt["ceiling"], "abstract": tt["abstract"], "abstract_texts": len(tt["abstract_texts"]),
               "e2a_f1_branches": tt["f0"], "olmo_row_branches": tt["olmo"], "s81_texts": len(tt["s81"]),
               "step7_open": tt["open"], "per_flag": "each flag's tallies asserted on its own outputs (equal)"}
    fires = {}
    for rid, *_ in PLACEHOLDER_SPEC:
        a, b_, cT, cF = PLACEHOLDER_FIRES[rid]
        got = {f: (tal["fires"][f].get((rid, "a"), 0), tal["fires"][f].get((rid, "b"), 0),
                   tal["fires"][f].get((rid, "c"), 0)) for f in (True, False)}
        fires[rid] = {"T": list(got[True]), "F": list(got[False])}
        B.chk(f"enumeration {rid} flag=T fires (a, b, c) = {(a, b_, cT)}", got[True] == (a, b_, cT), got[True],
              cover=[f"ENUM-{rid}-T"])
        B.chk(f"enumeration {rid} flag=F fires (a, b, c) = {(a, b_, cF)}", got[False] == (a, b_, cF), got[False],
              cover=[f"ENUM-{rid}-F"])
    tal_out["placeholder_fires"] = fires
    B.extra["tallies"] = tal_out
    # NOT-RUN reason routing: every unit a DISTINCT reason, all 1,080 tuples (the pass above uses one
    # unit-independent phrase, PIN-24), labels and enumeration against the oracle
    whys = {"Q-F0": not_run_reason("Q-F0", "clock:k-zero", CLOCK_DATE),
            "OLMo-sft": not_run_reason("OLMo-sft", "clock:no-box", CLOCK_DATE),
            "OLMo-dpo": not_run_reason("OLMo-dpo", "dose-not-completable"),
            "OLMo-instruct": not_run_reason("OLMo-instruct", "clock:gate-stopped:G-TIME-OLMo-instruct", CLOCK_DATE)}
    dis, multi = 0, 0
    for t in itertools.product(Q5, O6, O6, O6):
        rs = {u: whys[u] for u, x in zip(UNITS, t) if x == "NOT-RUN"}
        o, orc = v1_outputs(t, rs, True, table), _bt_oracle(t, True, table, whys)
        dis += o["labels"] == orc["labels"] and o["enumeration"] == orc["enumeration"]
        multi += len(rs) >= 2
    B.chk(f"NOT-RUN reasons routed per unit: {dis}/1080 tuples with a distinct reason per unit ({multi} with two "
          f"or more NOT-RUN units) give the oracle's labels and enumeration", dis == 1080 and multi == 155,
          (dis, multi), cover=["TUP-REASONS-DISTINCT"])
    # determinism: a second, fresh pass gives the same sha
    _, sha2, _, _ = _bt_tuple_pass(table)
    B.chk("two passes over the 2,160 evaluations give byte-identical canonical JSON (sha256 equal)", sha == sha2,
          sha[:16], cover=["STR-DETERMINISM"])


def _bt_table(B: _Battery) -> dict:
    built = placeholder_table()
    p = REPO / PLACEHOLDER_REL
    data = p.read_bytes() if p.is_file() else b""
    mut = resume.json_text({**built, "rows": built["rows"][:-1]}, indent=1).encode("utf-8")
    B.chk("the placeholder file is the builder's json_text(indent=1) byte for byte, and validates; a mutated "
          "table differs", data == resume.json_text(built, indent=1).encode("utf-8") and not table_problems(built)
          and mut != data, _sha256_bytes(data)[:16], cover=["ENUM-PLACEHOLDER-FILE"])
    var = copy.deepcopy(built)
    for r in var["rows"]:
        if r["dose_note"]:
            r["dose_note"], r["dose_note_span"] = False, None
            r["kinds"] = [k for k in r["kinds"] if k != "dose-note"]
    for flag in (True, False):
        fired, treat = {}, {}
        for t in itertools.product(Q5, O6, O6, O6):
            reasons = {u: "r" for u, x in zip(UNITS, t) if x == "NOT-RUN"}
            for it in enumeration(t, flag, var, reasons):
                if "c" in it["clauses"]:
                    fired[it["row_id"]] = fired.get(it["row_id"], 0) + 1
                    treat[it["c"]["treatment"]] = treat.get(it["c"]["treatment"], 0) + 1
        want = {"P03": 1080} if flag else {}
        dn = dose_note(flag, var)
        B.chk(f"no-dose-row variant flag={'T' if flag else 'F'}: (c) carries ('carry', every item) at the "
              f"f1-corr-line row (P03) in all 1,080 tuples under T, none under F", fired == want
              and treat == ({"carry": 1080} if flag else {})
              and dn["status"] == ("to be carried; absent from the table (§7.5(c))" if flag else "none (struck, §7.5(c))"),
              (fired, treat), cover=[f"ENUM-NODOSE-{'T' if flag else 'F'}"])
    # refusals, one case each
    def mut_(fn):
        t = copy.deepcopy(built)
        fn(t)
        return table_problems(t)

    def rowset(i, k, v):
        def f(t):
            t["rows"][i][k] = v
        return f
    pre_text = "Line one.\n[placeholder P01] A synthetic sentence that asserts no null.\n"
    rec_tab = copy.deepcopy(built)
    rec_tab["kind"] = "of-record"
    rec_tab["rows"] = [r for r in rec_tab["rows"] if r["id"] in ("P01", "P03")]
    rec_tab["rows"][1]["text"] = "Line one."
    rec_tab["rows"][1]["dose_note_span"] = "one"
    rec_tab["rows"][1]["text_sha256"] = hashlib.sha256(b"Line one.").hexdigest()
    rec_tab["rows"][0], rec_tab["rows"][1] = rec_tab["rows"][1], rec_tab["rows"][0]
    rec_tab["rows"][0]["loc"] = {"line": 1, "section": "s", "sentence": 1}
    rec_tab["rows"][1]["loc"] = {"line": 2, "section": "s", "sentence": 1}
    pb = pre_text.encode("utf-8")
    rec_tab["preprint"] = {"path": "PREPRINT-x.md", "sha256": _sha256_bytes(pb), "bytes": len(pb), "lines": 2}
    p01 = rec_tab["rows"][1]["text"]
    pres = {"PREPRINT-x.md": pb, "PREPRINT-same.md": f"Line one. {p01}\n".encode("utf-8"),
            "PREPRINT-swap.md": f"{p01} Line one.\n".encode("utf-8")}
    reader = lambda rel: pres.get(rel)

    def on(tab, path, locs):
        t = copy.deepcopy(tab)
        b = pres[path]
        t["preprint"] = {"path": path, "sha256": _sha256_bytes(b), "bytes": len(b), "lines": b.count(b"\n")}
        for r, (ln, sn) in zip(t["rows"], locs):
            r["loc"] = {"line": ln, "section": "s", "sentence": sn}
        return t
    ok_rec = table_problems(rec_tab, read_repo_file=reader) == []
    bad_hash = copy.deepcopy(rec_tab)
    bad_hash["preprint"]["sha256"] = "0" * 64
    bad_text = copy.deepcopy(rec_tab)
    bad_text["rows"][1]["text"] = "[placeholder P01] Not in the preprint."
    bad_text["rows"][1]["text_sha256"] = hashlib.sha256(bad_text["rows"][1]["text"].encode()).hexdigest()
    same_ok = on(rec_tab, "PREPRINT-same.md", ((1, 1), (1, 2)))
    wrong_line = on(rec_tab, "PREPRINT-x.md", ((1, 1), (1, 2)))         # P01's text is on line 2
    swapped = on(rec_tab, "PREPRINT-swap.md", ((1, 1), (1, 2)))         # line 1 holds P01, then "Line one."
    acc_same = table_problems(same_ok, read_repo_file=reader)
    pl_pair = [r["loc"] for r in built["rows"] if r["loc"]["line"] == 20]
    B.chk("table accepted: two sentences of one preprint line are two rows (loc.sentence 1, 2) -- the "
          "placeholder's P20 / P21 and an of-record table over a one-line preprint",
          acc_same == [] and not table_problems(built) and [x["sentence"] for x in pl_pair] == [1, 2],
          acc_same[:1], cover=["ENUM-SAMELINE"])
    forb = _forbidden()[1]
    cases = [
        ("schema", mut_(lambda t: t.__setitem__("schema", "x")), "schema 'x'"),
        ("kind outside the vocabulary", mut_(lambda t: t.__setitem__("kind", "draft")), "kind 'draft'"),
        ("cells", mut_(lambda t: t.__setitem__("cells", list(CELLS)[:-1])), "cells ["),
        ("a null cell outside cells", mut_(rowset(1, "null_cells", ["e2c"])), "P02: null_cells outside"),
        ("a thesis outside the vocabulary", mut_(rowset(13, "thesis", "fallback-3")), "P14: thesis"),
        ("dose_note true without its span", mut_(rowset(2, "dose_note_span", "not in the text")),
         "P03: a dose-note row needs"),
        ("a span while dose_note is false", mut_(rowset(0, "dose_note_span", "A synthetic")), "P01: a span on a row"),
        ("text_sha256 wrong", mut_(rowset(0, "text_sha256", "0" * 64)), "P01: text_sha256"),
        ("duplicate ids", mut_(rowset(1, "id", "P01")), "duplicate row ids"),
        ("rows out of (loc.line, loc.sentence) order", mut_(lambda t: t["rows"].reverse()),
         "(loc.line, loc.sentence) order"),
        ("a kind outside the vocabulary", mut_(rowset(0, "kinds", ["s9.9-new"])), "P01: a kind outside"),
        ("no f1-corr-line row", mut_(rowset(2, "kinds", ["dose-note"])), "no row of kind f1-corr-line"),
        ("a placeholder with a preprint", mut_(lambda t: t.__setitem__("preprint", {"path": "x"})),
         "a placeholder table carries no preprint"),
        ("an of-record preprint hash mismatch (an exact table accepted)",
         table_problems(bad_hash, read_repo_file=reader) if ok_rec else [], "sha256 / bytes / lines differ"),
        ("an of-record row not in the preprint", table_problems(bad_text, read_repo_file=reader) if ok_rec else [],
         "row text not found in the preprint"),
        ("a forbidden literal", mut_(lambda t: (t["rows"][0].__setitem__("text", "x " + forb),
                                                t["rows"][0].__setitem__("text_sha256", hashlib.sha256(
                                                    ("x " + forb).encode()).hexdigest()))), "forbidden literal"),
        ("posting other than v1", mut_(lambda t: t.__setitem__("posting", "v2")), "posting 'v2'"),
        ("a duplicate (loc.line, loc.sentence) (P21 made sentence 1 of line 20, as P20)",
         mut_(lambda t: t["rows"][20]["loc"].__setitem__("sentence", 1)), "(loc.line, loc.sentence) order"),
        ("a loc without its sentence ordinal", mut_(lambda t: t["rows"][0]["loc"].pop("sentence")),
         "P01: loc must be {line (int >= 1), sentence (int >= 1), section (str)}"),
        ("an of-record row whose text does not begin on its declared line",
         table_problems(wrong_line, read_repo_file=reader) if ok_rec else [],
         "P01: row text does not begin on its declared preprint line 1"),
        ("of-record rows sharing a line out of their in-line order",
         table_problems(swapped, read_repo_file=reader) if ok_rec else [],
         "P01: rows sharing line 1 do not occur there in loc.sentence order"),
    ]
    for i, (what, probs, needle) in enumerate(cases, 1):
        B.chk(f"table refused: {what}", any(needle in x for x in probs), probs[:1], cover=[f"ENUM-REF-{i:02d}"])
    return built


def _bt_flag(B: _Battery) -> None:
    real = flag_of_record(REPO / FLAG_SOURCE_REL, _prod_committed)
    B.chk("flag of record: data/m/gates/G-CAL_model-free.json committed, schema m-gcal-model-free-v1, f1_012 "
          "present -> TRUE (read-only; the sha and renders_sha_matches_calib printed beside, not asserted)",
          real["value"] is True,
          (real["value"], (real["sha256"] or "")[:16], real["renders_sha_matches_calib"]), cover=["FLAG-OF-RECORD-TRUE"])
    B.extra["flag_of_record"] = {k: real[k] for k in ("path", "sha256", "introduced_at", "value",
                                                      "renders_sha_matches_calib")}
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        doc = json.loads((REPO / FLAG_SOURCE_REL).read_bytes())
        ok_c = lambda p: ([], Path(p).read_bytes())
        p = d / "f.json"
        absent = flag_of_record(d / "absent.json", ok_c)
        p.write_text(json.dumps({**doc, "schema": "other"}))
        sch = flag_of_record(p, ok_c)
        p.write_text(json.dumps({k: v for k, v in doc.items() if k != "f1_012"}))
        no12 = flag_of_record(p, ok_c)
        p.write_text(json.dumps(doc))
        unc = flag_of_record(p, lambda q: (["not committed"], None))
        good = flag_of_record(p, ok_c)
        d2 = copy.deepcopy(doc)
        d2["f1_012"]["renders_sha_matches_calib"] = False
        p.write_text(json.dumps(d2))
        rb = flag_of_record(p, ok_c)
    B.chk("flag FALSE on a temp copy: absent", absent["value"] is False and absent["reason"] == "absent",
          cover=["FLAG-FALSE-absent"])
    B.chk("flag FALSE: schema wrong", sch["value"] is False and good["value"] is True, cover=["FLAG-FALSE-schema"])
    B.chk("flag FALSE: f1_012 missing", no12["value"] is False, cover=["FLAG-FALSE-f1_012"])
    B.chk("flag FALSE: uncommitted", unc["value"] is False, cover=["FLAG-FALSE-uncommitted"])
    B.chk("renders_sha_matches_calib false is recorded beside; the flag stays TRUE (existence-keyed)",
          rb["value"] is True and rb["renders_sha_matches_calib"] is False, cover=["FLAG-RENDERS-BESIDE"])


# --- battery: counters, secondaries -------------------------------------------------------------
def _bt_suite_records(sub: str) -> list[dict]:
    from valence_core.m import testing
    return [copy.deepcopy(rec) for (_c, rec, _calls, _p) in testing.suite(sub)]


def _bt_counters(B: _Battery, lines: Sequence[str]) -> None:
    from valence_core.m import stages
    ok314 = m314_counter_text() in lines[313]
    mut = m314_counter_text().replace("termination, reasoning", "reasoning") not in lines[313]
    B.chk("counters: the declaration reproduces m:314's two lists verbatim and in order (a reordered copy does "
          "not)", ok314 and mut, m314_counter_text()[:60], cover=["CNT-DECL-M314"])
    B.chk("counters: the tabulated names equal audit.DECLARED_COUNTERS_QWEN / _OLMO; Qwen adds the [Q-F3] "
          "counter, declared and scoped", tabulated_names("qwen") == audit.DECLARED_COUNTERS_QWEN
          and tabulated_names("olmo") == audit.DECLARED_COUNTERS_OLMO
          and [d.name for d in COUNTERS["qwen"] if d.q_f3_only] == ["reasoning_line_defect"],
          cover=["CNT-DECL-AUDIT"])
    q = _bt_suite_records("qwen")
    o = _bt_suite_records("olmo")
    clean_q = next(r for r in q if r["template"] == "A0" and r["s"] == 0)

    def tot(rs, sub, name):
        return _bt_tab(rs, sub)[0].total(name)

    def craft(fn):
        r = copy.deepcopy(clean_q)
        fn(r)
        return r

    def set_claim(rd, claim, detail):
        rd["audit"].update(claim=claim, detail=detail, degeneracy=claim in ("v2", "echo"))

    crafted = {
        "cap_hit": craft(lambda r: r["rounds"][0].__setitem__("cap_hit", True)),
        "audit_degenerate": craft(lambda r: set_claim(r["rounds"][5], "v2", "audit:frame:[round")),
        "harness_echo": craft(lambda r: set_claim(r["rounds"][5], "echo", "echo:0")),
        "content_exclusion": craft(lambda r: set_claim(r["rounds"][5], "content", "content:stuck_attractor")),
        "content_advisory": craft(lambda r: r["rounds"][2]["audit"].__setitem__("advisory", ["content:task_echo"])),
        "lexical": craft(lambda r: set_claim(r["rounds"][5], "lexical", "lexical:x")),
        "post_choice_degeneracy": craft(lambda r: set_claim(r["rounds"][6], "v2", "audit:junk:x")),
        "low_label_mass": craft(lambda r: r["choices"][1].__setitem__("low_label_mass", True)),
        "top1_not_label": craft(lambda r: r["choices"][1].__setitem__("top1_not_label", True)),
        "termination": craft(lambda r: r["rounds"][3].__setitem__("termination", True)),
    }
    clean_tot = {n: tot([clean_q], "qwen", n) for n in tabulated_names("qwen")}
    fire = {n: tot([r], "qwen", n) >= 1 for n, r in crafted.items()}
    excl = [r for r in q if r["exclusion"] and r["exclusion"]["phase"] == "forced"]
    fire["pre_pick_exclusion"] = tot(excl[:1], "qwen", "pre_pick_exclusion") == 1
    clean_ok = clean_q["exclusion"] is None and len(clean_q["choices"]) == 6
    silent = all(v == 0 for v in clean_tot.values())
    B.chk("counters: each Qwen counter fires on a crafted record and is silent on a clean one",
          all(fire.values()) and silent and clean_ok, {k_: v for k_, v in fire.items() if not v} or clean_tot,
          cover=["CNT-FIRE-SILENT"])
    dc_all, den_all = _bt_tab(q, "qwen")
    n_ex = sum(bool(r["excluded"]) for r in q)
    B.chk("counters: tabulated over all sessions, excluded included (n_sessions = every record; excluded ones "
          "counted)", dc_all.n_sessions == len(q) and n_ex > 0 and dc_all.n_excluded_included > 0,
          (dc_all.n_sessions, n_ex), cover=["CNT-EXCLUDED-TABULATED"])
    props = {k_[-1] for k_ in dc_all.counts if k_[0] in ("cap_hit", "lexical", "harness_echo", "termination")}
    contrast_corr = [x for r in q if r["contrast"] for x in r["rounds"] if x["property"] == "corrupted"]
    B.chk("counters: round counters carry the property key (VERDICTS form); read counters carry the read "
          "position", props <= {"clean", "corrupted"} and bool(props) and bool(contrast_corr)
          and all(isinstance(k_[2], int) for k_ in dc_all.counts if k_[0] in ("low_label_mass", "top1_not_label")),
          sorted(props), cover=["CNT-PROPERTY-KEYS"])
    rounds = sum(len(r["rounds"]) for r in q)
    reads = sum(len(r["choices"]) for r in q)
    B.chk("counters: denominators -- rounds generated, free rounds, reads taken, sessions launched",
          sum(den_all["rounds"].values()) == rounds and sum(den_all["reads"].values()) == reads
          and sum(den_all["sessions"].values()) == len(q)
          and sum(den_all["free_rounds"].values()) == sum(x["phase"] == "free" for r in q for x in r["rounds"]),
          (rounds, reads), cover=["CNT-DENOMINATORS"])
    dcx = _session.DescriptiveCounters(declared=tabulated_names("olmo"))
    B.chk("counters: an undeclared name raises (content_exclusion on OLMo; the [Q-F3] counter anywhere)",
          _bt_raises(lambda: dcx.note("content_exclusion", "x"), (KeyError,))[0]
          and _bt_raises(lambda: dcx.note("reasoning_line_defect", "x"), (KeyError,))[0], cover=["CNT-UNDECLARED-RAISES"])
    # per-property table, hand counts on two crafted Qwen records
    a = copy.deepcopy(next(r for r in q if r["template"] == "A0" and r["exclusion"]
                           and r["exclusion"]["phase"] == "forced"))
    b = copy.deepcopy(clean_q)
    tb = per_property_table([a, b], "Q-F0")["by_arm"]
    xr = excluding_round(a)
    hand = {"clean": 0, "corrupted": 0}
    for r in (a, b):
        for x in r["rounds"]:
            hand[x["property"]] += 1
    ok_tab = (tb["A0"]["clean"]["rounds_generated"] == hand["clean"]
              and tb["A0"]["corrupted"]["rounds_generated"] == hand["corrupted"]
              and tb["A0"][xr["property"]]["sessions_excluded_prepick"] == 1
              and tb["A0"][xr["property"]]["sessions_excluded_any_phase"] == 1
              and tb["A0"][xr["property"]]["rounds_excluding_by_class"][a["exclusion"]["class"]] == 1
              and tb["A0s"]["corrupted"]["rounds_generated"] == 0)
    bad_sham = copy.deepcopy(next(r for r in q if r["template"] == "A0s"))
    bad_sham["rounds"][0]["property"] = "corrupted"
    stop_sham = _bt_raises(lambda: per_property_table([bad_sham], "Q-F0"), (AnlStop,))[0]
    B.chk("per-property table equals hand counts (rounds by property, the excluding round's class and property, "
          "pre-pick and any-phase columns); a sham corrupted round is a STOP", ok_tab and stop_sham,
          tb["A0"], cover=["CNT-PER-PROPERTY"])
    # the excluding round must agree with the session's exclusion, class and phase (else STOP)
    other_cls = "lexical" if a["exclusion"]["class"] != "lexical" else "echo"
    a_cls, a_ph = copy.deepcopy(a), copy.deepcopy(a)
    a_cls["exclusion"]["class"] = other_cls
    a_ph["exclusion"]["phase"] = "free"
    x_cls = _bt_raises(lambda: excluding_round(a_cls), (AnlStop,))
    x_ph = _bt_raises(lambda: excluding_round(a_ph), (AnlStop,))
    B.chk("excluding round: a session whose exclusion class or phase disagrees with its first excluding round's is "
          "a STOP (excluding_round, so tabulate and the per-property table); an agreeing one returns that round",
          x_cls[0] and x_ph[0] and "is not its first excluding round's" in x_cls[1]
          and xr["audit"]["claim"] == a["exclusion"]["class"] and xr["phase"] == a["exclusion"]["phase"]
          and _bt_raises(lambda: tabulate([a_cls], "qwen"), (AnlStop,))[0], (x_cls[1][:60], x_ph[1][:40]),
          cover=["CNT-EXCLROUND-STOP"])
    # the property axis uncollapsed: exact keyed counts on crafted records, a free-phase exclusion on a
    # corrupted round (any-phase column != pre-pick column), and whole-session validity strict < lenient
    corr_f = [i for i, x in enumerate(clean_q["rounds"]) if x["phase"] == "forced" and x["property"] == "corrupted"]
    corr_v = [i for i, x in enumerate(clean_q["rounds"]) if x["phase"] == "free" and x["property"] == "corrupted"]
    clean_v = [i for i, x in enumerate(clean_q["rounds"]) if x["phase"] == "free" and x["property"] == "clean"]
    rA = copy.deepcopy(clean_q)                        # excluded at a corrupted FORCED round (pre-pick)
    fi = corr_f[0]
    set_claim(rA["rounds"][fi], "content", "content:stuck_attractor")
    rA["rounds"][0]["termination"] = True               # forced round 0 is clean
    rA["rounds"] = rA["rounds"][:fi + 1]
    rA.update(choices=[], domain=False, complete=False, excluded=True, first_free_pick_P=None,
              exclusion={"class": "content", "phase": "forced", "detail": "content:stuck_attractor"})
    rB = copy.deepcopy(clean_q)                        # excluded at a corrupted FREE round (not pre-pick)
    vi = corr_v[0]
    ci = rB["rounds"][vi]["ci"]
    set_claim(rB["rounds"][vi], "lexical", "lexical:x")
    rB["rounds"][corr_f[0]]["cap_hit"] = True
    rB["rounds"][clean_v[0]]["audit"]["advisory"] = ["content:task_echo"]
    rB["rounds"] = rB["rounds"][:vi + 1]
    rB.update(choices=rB["choices"][:ci + 1], complete=False, excluded=True,
              exclusion={"class": "lexical", "phase": "free", "detail": "lexical:x"})
    rS = copy.deepcopy(next(r for r in q if r["template"] == "A0s" and r["s"] == 0))
    si = next(i for i, x in enumerate(rS["rounds"]) if x["phase"] == "free")
    set_claim(rS["rounds"][si], "echo", "echo:0")
    want_keys = {("content_exclusion", "A0", "forced", "stuck_attractor", "corrupted"): 1,
                 ("termination", "A0", "forced", "clean"): 1, ("pre_pick_exclusion", "A0", "corrupted"): 1,
                 ("lexical", "A0", "free", "corrupted"): 1, ("cap_hit", "A0", "forced", "corrupted"): 1,
                 ("content_advisory", "A0", "free", "task_echo", "clean"): 1,
                 ("harness_echo", "A0s", "free", "clean"): 1, ("post_choice_degeneracy", "A0s", "echo", "clean"): 1}
    got_keys = dict(_bt_tab([rA, rB, rS], "qwen")[0].counts)
    tbp = per_property_table([rA, rB, rS], "Q-F0")["by_arm"]
    n_cl = sum(x["property"] == "clean" for r in (rA, rB) for x in r["rounds"])
    n_co = sum(x["property"] == "corrupted" for r in (rA, rB) for x in r["rounds"])
    want_tab = {"rounds_generated": n_co, "sessions_excluded_prepick": 1, "sessions_excluded_any_phase": 2,
                "excl": {"content": 1, "lexical": 1}, "claimed": {"content": 1, "lexical": 1}}
    co = tbp["A0"]["corrupted"]
    tab_ok = (co["rounds_generated"] == want_tab["rounds_generated"] and tbp["A0"]["clean"]["rounds_generated"] == n_cl
              and co["sessions_excluded_prepick"] == 1 and co["sessions_excluded_any_phase"] == 2
              and {k_: v for k_, v in co["rounds_excluding_by_class"].items() if v} == want_tab["excl"]
              and {k_: v for k_, v in co["rounds_claimed_by_class"].items() if v} == want_tab["claimed"]
              and tbp["A0"]["clean"]["sessions_excluded_any_phase"] == 0
              and {k_: v for k_, v in tbp["A0s"]["clean"]["rounds_claimed_by_class"].items() if v} == {"echo": 1})
    rSt = copy.deepcopy(clean_q)
    rSt["strict_exclusion"] = {"class": "v2", "phase": "free"}
    val = beside_blocks([clean_q, rSt, rA], "Q-F0")["A0"]["whole_session_validity"]
    B.chk("counters by property, uncollapsed: the exact keyed counts on crafted records (a corrupted forced-round "
          "exclusion, a corrupted free-round exclusion, a clean advisory, a sham echo); the per-property table's "
          "any-phase column (2) differs from its pre-pick column (1) on the corrupted row; whole-session validity "
          "lenient 2 / strict 1 of 3", got_keys == want_keys and tab_ok
          and val == {"launched": 3, "valid_lenient": 2, "valid_strict": 1},
          (sorted(set(got_keys.items()) ^ set(want_keys.items()))[:2], val), cover=["CNT-PROPERTY-EXACT"])
    rr = copy.deepcopy(clean_q)
    rr["reasoning_line"] = "x"
    B.chk("counters: a record carrying reasoning-line material is a STOP at Q-F0 (record check and tabulation)",
          _bt_raises(lambda: tabulate([rr], "qwen"), (AnlStop,))[0]
          and any("reasoning" in p for p in record_problems(rr, "Q-F0", "qual")), cover=["CNT-REASONING-STOP"])
    # equality with audit.tally, both directions
    eq = []
    for rs, sub in ((q, "qwen"), (o, "olmo")):
        mine = collapse_to_tally(_bt_tab(rs, sub)[0])
        ref = _session.DescriptiveCounters(declared=audit.DECLARED_COUNTERS_QWEN if sub == "qwen"
                                           else audit.DECLARED_COUNTERS_OLMO)
        for r in rs:
            audit.tally(ref, r)
        eq.append(mine == dict(ref.counts))
    drift = copy.deepcopy(q)
    for r in drift:
        for x in r["rounds"]:
            if x["phase"] == "free" and x["audit"]["claim"] is None:
                x["termination"] = True
                break
    ref2 = _session.DescriptiveCounters(declared=audit.DECLARED_COUNTERS_QWEN)
    for r in q:
        audit.tally(ref2, r)
    neq = collapse_to_tally(_bt_tab(drift, "qwen")[0]) != dict(ref2.counts)
    B.chk("counters summed over property (and read position) equal audit.tally on the same records (Qwen and "
          "OLMo); records that differ give tables that differ", all(eq) and neq, eq, cover=["CNT-TALLY-EQUAL"])
    pp = [(stages._prepick(r), _prepick(r)) for r in q + o]
    flip = copy.deepcopy(next(r for r in q if r["exclusion"] and r["exclusion"]["phase"] == "forced"))
    flip["exclusion"]["phase"] = "free"
    B.chk("pre-pick: this file's definition equals stages._prepick on every record (both values occur); a "
          "free-phase exclusion is not pre-pick for either", all(a_ == b_ for a_, b_ in pp)
          and {a_ for a_, _ in pp} == {True, False} and not _prepick(flip) and not stages._prepick(flip),
          sum(a_ for a_, _ in pp), cover=["CNT-PREPICK-STAGES"])


def _bt_tab(rs, sub):
    return tabulate(rs, sub)


def _bt_mkrec(template: str, pair_index: int, mp: int, start: int, picks: Sequence[str], *, domain: bool = True,
              excl_free_ci: int | None = None, contrast: bool | None = None) -> dict:
    """A minimal synthetic m record for the secondaries (only the fields they read)."""
    contrast = keys.is_contrast(template) if contrast is None else contrast
    roles = list(picks)
    forced_roles = ["P", "Q", "P", "Q"] if start == 0 else ["Q", "P", "Q", "P"]
    rounds = [{"phase": "forced", "ri": i, "role": rl, "pole": "pos" if rl == "P" else "neg",
               "property": "corrupted" if (contrast and rl == "Q") else "clean", "termination": False,
               "audit": {"claim": None}} for i, rl in enumerate(forced_roles)]
    choices = []
    for ci, rl in enumerate(roles):
        choices.append({"ci": ci, "pick": f"L{rl}", "picked_role": rl, "picked_pole": "pos" if rl == "P" else "neg"})
        claim = "lexical" if excl_free_ci == ci else None
        rounds.append({"phase": "free", "ci": ci, "role": rl, "pole": "pos" if rl == "P" else "neg",
                       "property": "corrupted" if (contrast and rl == "Q") else "clean", "termination": False,
                       "audit": {"substrate": "qwen", "phase": "free", "claim": claim,
                                 "detail": None if claim is None else "lexical:x", "v3": None, "advisory": [],
                                 "echo_line": None, "lexical_raw": None, "scaffold": []}})
    for r in rounds[:4]:
        r["audit"] = {"substrate": "qwen", "phase": "forced", "claim": None, "detail": None, "v3": None,
                      "advisory": [], "echo_line": None, "lexical_raw": None, "scaffold": []}
    exc = {"class": "lexical", "phase": "free", "detail": "lexical:x"} if excl_free_ci is not None else None
    return {"template": template, "domain": domain and bool(choices), "cell": {"pair_index": pair_index, "map": mp,
            "start": start}, "choices": choices if domain else [], "rounds": rounds if domain else rounds[:4],
            "exclusion": exc, "first_free_pick_P": (roles[0] == "P") if (domain and choices) else None,
            "substrate": "qwen"}


def _bt_secondaries(B: _Battery) -> None:
    rs19 = [_bt_mkrec("A0", 0, 0, 0, ["P", "Q"]) for _ in range(19)]
    rs20 = rs19 + [_bt_mkrec("A0", 0, 0, 0, ["P", "Q"])]
    a19 = secondaries(rs19, "Q-F0")["a"]["A0"]["1"]
    a20 = secondaries(rs20, "Q-F0")["a"]["A0"]["1"]
    B.chk("secondary floor: 19 events count-only (no interval), 20 events an interval",
          a19["count_only"] and a19["interval"] is None and not a20["count_only"] and a20["interval"] is not None,
          (a19["den"], a20["den"]), cover=["SEC-FLOOR-19-20"])
    rs = [_bt_mkrec("A0", 0, 0, 0, ["Q", "P", "P"]), _bt_mkrec("A0s", 1, 0, 0, ["Q", "P", "P"])]
    sb = secondaries(rs, "Q-F0")["b"]
    B.chk("secondary (b) lose-shift: contrast arm only (no sham key); the transition after a corrupted chosen "
          "round counted", set(sb) == {"A0", "scope"} and sb["A0"]["corrupted"]["den"] == 1
          and sb["A0"]["corrupted"]["num"] == 1 and sb["A0"]["clean"]["den"] == 1 and sb["A0"]["clean"]["num"] == 0,
          sb["A0"], cover=["SEC-B-CONTRAST-ONLY"])
    for m_ in (32, 56):
        sh = [_bt_mkrec("A0s", i % 4, i % 2, (i // 4) % 2, ["P"]) for i in range(m_)]
        d = secondaries(sh, "Q-F0")["d"]["A0s"]["per_pair"]
        B.chk(f"secondary (d): a sham arm of {m_} gives {m_ // 4} per pair -> count-only", len(d) == 4
              and all(v["den"] == m_ // 4 and v["count_only"] for v in d.values()), m_ // 4,
              cover=["SEC-D-SHAM-COUNT-ONLY"])
    ex = _bt_mkrec("A0", 0, 0, 0, ["P", "Q", "P"], excl_free_ci=1)
    vt = [valid_through(ex, p) for p in (1, 2, 3, 4)]
    vn = [valid_through(_bt_mkrec("A0", 0, 0, 0, ["P", "Q", "P"]), p) for p in (1, 2, 3, 4)]
    B.chk("'valid through p': a session excluded at free round ci = 1 is valid through 1 and 2, not 3 (its "
          "third choice notwithstanding); unexcluded, through 3", vt == [True, True, False, False]
          and vn == [True, True, True, False], (vt, vn), cover=["SEC-VALID-THROUGH"])
    dom = [_bt_mkrec("A0", 0, i % 2, i % 2, ["P" if i % 3 else "Q"]) for i in range(11)]
    hi = habit_identity(dom)
    P = Fraction(sum(r["first_free_pick_P"] for r in dom), len(dom))
    bad = copy.deepcopy(dom)
    bad[0]["choices"][0]["picked_pole"] = "neg" if bad[0]["choices"][0]["picked_pole"] == "pos" else "pos"
    hb = habit_identity(bad)
    B.chk("habit identity: break_rates' weighted form + 1/2 reproduces the arm's P exactly (Fractions); a "
          "pole/role inconsistency breaks it", hi["identity_holds"] and Fraction(hi["delta_first_weighted_form"])
          + HALF == P and not hb["identity_holds"], (hi["delta_first_weighted_form"], fs(P)),
          cover=["SEC-HABIT-IDENTITY"])
    # the values of (a), (d) per pair x start and (e), hand-counted on crafted records
    r1 = _bt_mkrec("A0", 0, 0, 0, ["P", "Q", "P"])
    r2 = _bt_mkrec("A0", 0, 1, 1, ["Q", "P"])
    r3 = _bt_mkrec("A0", 1, 0, 0, ["P", "P", "Q"], excl_free_ci=1)     # valid through 1 and 2, not 3
    r4 = _bt_mkrec("A0", 1, 1, 1, ["P"], domain=False)                 # no read: forced rounds only
    r1["rounds"][4]["termination"] = True                               # free ci 0
    r2["rounds"][0]["termination"] = True                               # forced round 0
    for x in r1["rounds"][5:7]:
        x["cap_hit"] = True                                             # cap_hit is not termination
    sv = secondaries([r1, r2, r3, r4], "Q-F0")
    a_ = {p_: (sv["a"]["A0"][p_]["num"], sv["a"]["A0"][p_]["den"]) for p_ in ("1", "2", "3")}
    d_ = {k_: (v["num"], v["den"]) for k_, v in sv["d"]["A0"]["per_pair_start"].items()}
    e_ = {ph: (sv["e"]["A0"][ph]["num"], sv["e"]["A0"][ph]["den"]) for ph in ("forced", "free")}
    B.chk("secondary values, hand-counted: (a) P-role share at p = 1, 2, 3 is 2/3, 2/3, 1/1 (the free-excluded "
          "session drops at p = 3); (d) per pair x start 0|0 1/1, 0|1 0/1, 1|0 1/1, 1|1 0/0; (e) terminations "
          "forced 1/16, free 1/8 (cap_hit is not a termination)",
          a_ == {"1": (2, 3), "2": (2, 3), "3": (1, 1)}
          and d_ == {"0|0": (1, 1), "0|1": (0, 1), "1|0": (1, 1), "1|1": (0, 0)}
          and e_ == {"forced": (1, 16), "free": (1, 8)}, (a_, d_, e_), cover=["SEC-VALUES"])


def _bt_counts_path(B: _Battery) -> None:
    """record -> counts -> outcome on crafted campaign records (campaign_counts, prepick_counts, unit_state)."""
    def arm(tpl, mp, picks_first, n_dom, *, start=0):
        return [_bt_mkrec(tpl, i % 4, mp, start, [picks_first[i]]) for i in range(n_dom)]
    a0 = (arm("A0", 0, ["P"] * 28 + ["Q"] * 12, 40) + arm("A0", 1, ["Q"] * 12 + ["P"] * 28, 40)
          + [_bt_mkrec("A0", 0, 0, 0, ["P"], domain=False) for _ in range(5)])
    a0s = arm("A0s", 0, ["P", "Q"] * 8, 16) + arm("A0s", 1, ["Q", "P"] * 8, 16) \
        + [_bt_mkrec("A0s", 0, 1, 0, ["P"], domain=False) for _ in range(3)]
    flip = copy.deepcopy(a0)
    for r in flip:
        if r["domain"]:
            r["choices"][0]["picked_role"] = "Q" if r["choices"][0]["picked_role"] == "P" else "P"
            r["first_free_pick_P"] = not r["first_free_pick_P"]
    c1, c2 = campaign_counts(a0 + a0s, "Q-F0"), campaign_counts(flip + a0s, "Q-F0")
    u1 = unit_state("Q-F0", {"kind": "campaign", "ended": "COMPLETE", "stop_bar": None, "pi_stop_record": False,
                             "counts": c1})
    u2 = unit_state("Q-F0", {"kind": "campaign", "ended": "COMPLETE", "stop_bar": None, "pi_stop_record": False,
                             "counts": c2})
    pick = lambda c: tuple(c[k_] for k_ in ("n0", "k0", "n1", "k1", "mS", "j"))
    B.chk("record -> counts -> outcome: crafted records 28/40 + 28/40 vs sham 16/32 (5 + 3 non-domain launched) -> "
          "PASS; the role-flipped twin (12/40 + 12/40) -> REVERSE",
          pick(c1) == (40, 28, 40, 28, 32, 16) and c1["launched"] == {"A0": 85, "A0s": 35}
          and c1["domain"] == {"A0": 80, "A0s": 32} and u1[1]["state"] == "PASS"
          and pick(c2) == (40, 12, 40, 12, 32, 16) and u2[1]["state"] == "REVERSE", (pick(c1), u1[1]["state"],
                                                                                    u2[1]["state"]),
          cover=["CNT-COUNTS-CRAFTED"])
    # non-domain sham sessions and free-phase exclusions: mS, E and both pre-pick rates
    fx = {"class": "lexical", "phase": "forced", "detail": "lexical:x"}
    con = (arm("A0", 0, ["P", "P", "Q", "Q", "P"], 5) + arm("A0", 1, ["P", "Q"], 2)
           + [_bt_mkrec("A0", 1, 1, 0, ["P", "Q"], excl_free_ci=1) for _ in range(3)])
    nd_c = [_bt_mkrec("A0", 2, 0, 0, ["P"], domain=False) for _ in range(2)]
    sh = arm("A0s", 0, ["P", "Q", "Q", "Q"], 4) + arm("A0s", 1, ["P", "Q", "Q", "Q"], 4)
    nd_s = [_bt_mkrec("A0s", 3, 1, 1, ["P"], domain=False) for _ in range(3)]
    for r in nd_c + nd_s:
        r["exclusion"] = dict(fx)
    recs = con + nd_c + sh + nd_s
    cc, pp = campaign_counts(recs, "Q-F0"), prepick_counts(recs, "Q-F0")
    oc = arm_outcome(cc["n0"], cc["k0"], cc["n1"], cc["k1"], cc["mS"], cc["j"])
    B.chk("record -> counts with non-domain sham sessions and free-phase exclusions: mS 8 (3 non-domain sham "
          "launches not counted), E = 1/4; pre-pick A0 2/12 (the 3 free-phase exclusions not pre-pick), A0s 3/11",
          (cc["mS"], cc["j"], cc["n0"] + cc["n1"], cc["k0"] + cc["k1"]) == (8, 2, 10, 7) and oc["stats"]["E"] == Fraction(1, 4)
          and pp == {"A0": 2, "A0s": 3} and cc["launched"] == {"A0": 12, "A0s": 11},
          (cc["mS"], fs(oc["stats"]["E"]), pp, cc["launched"]), cover=["CNT-PREPICK-RATES"])


# --- battery: the reader path on production-written checkpoints -----------------------------------
def _bt_env(base: Path, **over) -> Env:
    """A temp-directory env: commits are the files' own bytes; the closure and package are this site's."""
    cl = over.pop("closure_sha256", _BT_STATE.get("closure_sha256", "0" * 64))
    env = Env(proposal_path=REPO / PROPOSAL_REL, committed=lambda p: ([], Path(p).read_bytes()) if Path(p).is_file()
              else ([f"{p}: absent"], None), analyzer_path=Path(__file__).resolve(),
              package_sha256=_BT_STATE.get("package_sha256", "0" * 64), closure_sha256=cl, allow_stub=True,
              gate_line=lambda name: (f"GATE {name}: (battery)", []),
              read_repo_file=lambda rel: (base / rel).read_bytes() if (base / rel).is_file() else None,
              say=lambda line: None)
    for k_, v in over.items():
        setattr(env, k_, v)
    return env


_BT_STATE: dict = {}


@contextlib.contextmanager
def _bt_patched(obj, attr: str, value):
    saved = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        setattr(obj, attr, saved)


@contextlib.contextmanager
def _bt_pod(value):
    had, prev = resume.POD_ENV in os.environ, os.environ.get(resume.POD_ENV)
    os.environ[resume.POD_ENV] = value
    try:
        yield
    finally:
        if had:
            os.environ[resume.POD_ENV] = prev
        else:
            os.environ.pop(resume.POD_ENV, None)


class _Camp:
    """Stub campaigns through stages.run_campaign (the production writer), in a temp out_root."""

    def __init__(self, base: Path, lock_sha: str) -> None:
        from valence_core.m import corr, scaffold
        self.base, self.lock_sha = base, lock_sha
        self.rsha = corr.renders_sha(scaffold.pool_and_renders()[1])

    def xtra(self) -> dict:
        return {"lock_sha256": self.lock_sha, "proposal_sha256": "2" * 64, "renders_sha16": self.rsha,
                "locked_path": "uncached"}

    def root(self, name: str) -> Path:
        from valence_core.m import schedule
        r = resume.refuse_canonical_out(self.base / name / "m")
        schedule.write_schedule_files(r / "schedules")
        return r

    def prior(self, root: Path, unit: str) -> Path:
        tpls = list(keys.templates(unit))
        ident = resume.Identity(unit=unit, stage="qual", template_set=tpls, lock_sha256="1" * 64,
                                schedule_sha256="3" * 64, path="uncached", hour_cap=None, n={t: 1 for t in tpls},
                                audit_v2_sha16="4" * 16, ban_sha="5" * 16, backend_identifier="6" * 16,
                                proposal_sha256="2" * 64)
        p = root / "ckpt" / f"{unit}_qualprior.json"
        if p.is_file():
            return p
        p.parent.mkdir(parents=True, exist_ok=True)
        ck = resume.load_or_init(p, ident, False)
        ck["stage_end"] = {"status": "PASS", "fired": [], "adjudication": None}
        resume.write_checkpoint(p, ck)
        return p

    def adapter(self, unit: str, counts: Mapping[str, int], rule=None, interrupt=None):
        from valence_core.m import schedule, stages, testing
        r = schedule.roster_for(unit)
        cells = {}
        for t, m in counts.items():
            cs = schedule.campaign_schedule(unit, t, r, -(-m // schedule.UNIT_SIZE))[:m]
            cells.update({(t, s): c for s, c in enumerate(cs)})
        ad = testing.ScriptedAdapter() if unit == "Q-F0" else testing.OLMoScriptedAdapter()
        ad.load(stages._script_policy(unit, "campaign", cells, rule, interrupt), None)
        return ad

    def run(self, unit: str, root: Path, ad, floors, *, cap: float = 10.0, **kw):
        from valence_core.m import stages
        buf = io.StringIO()
        res = exc = None
        with contextlib.redirect_stdout(buf):
            try:
                res = stages.run_campaign(ad, unit=unit, floors=floors, launch_counts=floors, hour_cap=cap,
                                          identity_extra=self.xtra(), prior_ckpt=self.prior(root, unit),
                                          substrate="qwen" if unit == "Q-F0" else "olmo", out_root=root, **kw)
            except (SystemExit, stages._Interrupt) as e:
                exc = e
        return res, exc

    def time_ckpt(self, root: Path) -> Path:
        from valence_core.m import stages
        ad = self.adapter_gate()
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            res = stages.run_gate_stage(ad, unit="Q-F0", gate="time", templates_counts=[("A0", 1), ("A0s", 1)],
                                        identity_extra=self.xtra(), substrate="qwen", out_root=root)
        return Path(res["checkpoint"])

    def adapter_gate(self):
        from valence_core.m import schedule, stages, testing
        r = schedule.roster_for("Q-F0")
        cells = {}
        for t in ("A0", "A0s"):
            cells.update({(t, s): c for s, c in enumerate(schedule.gate_schedule("Q-F0", "time", t, r, 1))})
        ad = testing.ScriptedAdapter()
        ad.load(stages._script_policy("Q-F0", "time", cells, None, None), None)
        return ad

    def qual_ckpt(self, root: Path) -> Path:
        """A qualification checkpoint assembled from testing.suite('qwen')'s records (the production
        session builders, stage qual), marked verified, recorded through resume's public API."""
        recs = _bt_suite_records("qwen")
        ident = resume.Identity(unit="Q-F0", stage="qual", template_set=["A0", "A0s"], lock_sha256="1" * 64,
                                schedule_sha256="3" * 64, path="uncached", hour_cap=None,
                                n={"A0": 16, "A0s": 16}, audit_v2_sha16="4" * 16, ban_sha="5" * 16,
                                backend_identifier="6" * 16, proposal_sha256="2" * 64)
        p = root / "ckpt" / "Q-F0_qual.json"
        ck = resume.load_or_init(p, ident, False)
        resume.append_provenance(ck, {"adapter": STUB_MARK + " -- NOT A MODEL", "stage": "battery"},
                                 stamp="2026-10-10T00:00:00Z")
        for r in recs:
            r["verified"] = True
            resume.record_session(ck, r)
            ck["provenance"][-1]["launched"] += 1
        ck["stage_end"] = {"status": "PASS", "fired": [], "adjudication": None}
        resume.write_checkpoint(p, ck)
        return p


def _bt_reader(B: _Battery) -> None:
    from valence_core.m import guard, stages
    with tempfile.TemporaryDirectory(prefix="m_analyze_bt_") as td:
        base = resume.refuse_canonical_out(Path(td))
        B.scrub += [str(base), str(Path(td)), str(Path(td).resolve()), str(base).replace("/private/", "/", 1)]
        a_sha = _sha256_bytes(Path(__file__).read_bytes())
        # the Q-F0 table of record (temp, over a temp preprint) and OLMo states, for V10; LOCK v1.0
        # names the table's and its preprint's sha256 (m:286; PIN-40)
        _BT_STATE["rec_table"], _BT_STATE["olmo_states"] = _bt_qf0_v10_inputs(base)
        t_sha = _sha256_bytes(Path(_BT_STATE["rec_table"]).read_bytes())
        pp_sha = json.loads(Path(_BT_STATE["rec_table"]).read_text(encoding="utf-8"))["preprint"]["sha256"]
        lock_text = (f"LOCK (battery) analyzer {a_sha} package {_BT_STATE['package_sha256']} closure "
                     f"{_BT_STATE['closure_sha256']} sentence table {t_sha} preprint {pp_sha}\n")
        lock = base / "LOCK-battery.md"
        lock.write_text(lock_text, encoding="utf-8")
        lsha = _sha256_bytes(lock_text.encode("utf-8"))
        C = _Camp(base, lsha)
        dec_p = {}
        for U in UNITS:
            p = base / f"decisions-{U}.json"
            p.write_text(json.dumps({"schema": DECISIONS_SCHEMA, "unit": U, "decisions_with_other_outcomes_known": []}))
            dec_p[U] = p
        with _bt_patched(guard, "GATES_DIR", base / "no-gates"):
            g_root = C.root("gates")
            time_p = C.time_ckpt(g_root)
            qual_p = C.qual_ckpt(g_root)

            def V(U, camp_p, out_name, env=None, **kw):
                inp = VerdictInputs(unit=U, lock=kw.pop("lock", lock), decisions=kw.pop("decisions", dec_p[U]),
                                    campaign=camp_p, time=kw.pop("time", time_p), qual=kw.pop("qual", qual_p),
                                    out=base / "out" / out_name, **kw)
                if U == "Q-F0":
                    inp.sentences = inp.sentences or _BT_STATE["rec_table"]
                    inp.olmo_states = inp.olmo_states or _BT_STATE["olmo_states"]
                    _bt_olmo_outputs(inp.out)
                try:
                    st, lines, paths = run_verdicts(inp, env or _bt_env(base))
                    return ("ok", st, lines, paths)
                except AnlRefusal as e:
                    return ("refused", B.clean(str(e)), [], [])
                except AnlStop as e:
                    return ("stop", B.clean(str(e)), [], [])
                except Exception as e:                                # noqa: BLE001 -- a crash fails its own check
                    return ("crash", B.clean(f"{type(e).__name__}: {e}"), [], [])
            base_c = _bt_env(base).committed

            def uncommitted(target):
                """An env double's commit check: ``target`` uncommitted, every other file committed."""
                return lambda q: (["not committed (battery double)"], None) if Path(q).resolve() == \
                    Path(target).resolve() else base_c(q)

            def stub_free(src: Path, name: str, campaign: bool = False) -> Path:
                """A copy of a stub-written checkpoint with STUB_MARK scrubbed from its provenance records
                (a campaign's identity backend re-derived), for the PIN-30 checks in isolation."""
                ck = json.loads(Path(src).read_text())
                for e in ck.get("provenance") or []:
                    e["record"] = json.loads(json.dumps(e["record"]).replace(STUB_MARK, "BATTERY-NO-MARK"))
                if campaign:
                    ck["identity"]["backend_identifier"] = resume.backend_identifier(
                        resume.report_provenance(ck)[0]["record"])
                p = Path(src).parent / f"{name}.json"
                p.write_text(json.dumps(ck))
                return p

            def gate_variant(src: Path, name: str, fn) -> Path:
                ck = json.loads(Path(src).read_text())
                fn(ck)
                p = Path(src).parent / f"{name}.json"
                p.write_text(json.dumps(ck))
                return p
            # COMPLETE
            r1 = C.root("complete")
            rule1 = lambda t, s, n, c: "Config choice one." if (t == "A0" and s == 0 and n == 1) else None
            res, exc = C.run("Q-F0", r1, C.adapter("Q-F0", {"A0": 4, "A0s": 3}, rule1), {"A0": 3, "A0s": 3})
            cp = Path(res["checkpoint"])
            v = V("Q-F0", cp, "complete")
            doc = json.loads((base / "out" / "complete" / "Q-F0_VERDICTS.json").read_text()) if v[0] == "ok" else {}
            B.chk("reader: a COMPLETE stub campaign (production writer) -> analyzed; VERDICTS and secondary written; "
                  "the sentence names the end look", v[0] == "ok" and v[1] == "written"
                  and doc.get("arm", {}).get("state") in ARM_STATES and "the end look" in doc.get("sentence", "")
                  and (base / "out" / "complete" / "Q-F0_secondary.json").is_file(),
                  (v[0], v[1][:80] if v[0] != "ok" else doc.get("arm", {}).get("state")), cover=["C3-COMPLETE"])
            v2 = V("Q-F0", cp, "complete")
            B.chk("reader: the same VERDICTS run again is byte-identical ('identical'); its stdout carries no roster "
                  "word", v2[0] == "ok" and v2[1] == "identical"
                  and not stages._ROSTER_RX.search("\n".join(v[2] + v2[2])), v2[1][:60],
                  cover=["CMD-VERDICTS-IDENTICAL", "STR-STDOUT-HYGIENE"])
            rtp = rates_tests_problems(doc)
            planted = copy.deepcopy(doc)
            planted.setdefault("rates", [{}])[0] = {**planted["rates"][0], "domain": ""}
            planted.setdefault("tests", {"x": {}})["p_up"] = {"p": "1/2"}
            B.chk("reader: every rate in the VERDICTS output carries {num, den, domain} and every p its test (m:358); "
                  "a planted rate without its domain and a p without its test are caught",
                  rtp == [] and len(rates_tests_problems(planted)) >= 2 and doc.get("counter_rates"),
                  (len(doc.get("rates") or []), len(doc.get("counter_rates") or []), rtp[:1]),
                  cover=["CMD-VERDICTS-RATES"])
            bad_states = base / "olmo-states-bad.json"
            sd = json.loads(Path(_BT_STATE["olmo_states"]).read_text())
            sd["states"]["OLMo-instruct"] = {"state": "PASS"}
            bad_states.write_text(json.dumps(sd))
            vbs = V("Q-F0", cp, "bad-states", sentences=_BT_STATE["rec_table"], olmo_states=bad_states)
            B.chk("refused: Q-F0's declared OLMo states contradict an existing OLMo output (instruct PASS declared, its "
                  "VERDICTS says DEAD)", vbs[0] == "refused" and "its VERDICTS says 'DEAD'" in vbs[1], vbs[1][:70],
                  cover=["CMD-VERDICTS-OLMO-CROSSCHECK"])
            vo = doc.get("v1_outputs") or {}
            B.chk("reader: Q-F0's VERDICTS carries §7's v1 outputs under the tuple (its own state, the declared OLMo "
                  "states) over the table of record, and the flag of record",
                  doc.get("tuple", {}).get("OLMo-sft") == "PENDING" and vo.get("step7") == "open"
                  and vo.get("ceiling", {}).get("name") in ("Fallback-1", "Fallback-2")
                  and doc.get("flag", {}).get("value") is True and isinstance(vo.get("enumeration"), list),
                  doc.get("tuple"), cover=["CMD-VERDICTS-QF0-V1"])
            # the output's binding fields and power, against independently computed values
            st_ = (doc.get("arm") or {}).get("stats") or {}
            pw = json.loads(json.dumps(power_block(st_.get("n0", 0), st_.get("n1", 0), st_.get("mS", 0))))
            bind_ok = (doc.get("analyzer_sha256") == a_sha and doc.get("package_sha256") == _BT_STATE["package_sha256"]
                       and doc.get("closure_sha256") == _BT_STATE["closure_sha256"]
                       and doc.get("proposal_sha256") == PROPOSAL_SHA256 and doc.get("power") == pw
                       and isinstance(pw.get("of_record"), Mapping) and st_.get("n", 0) > 0)
            B.chk("reader: Q-F0's VERDICTS records the analyzer's, package's and closure's sha256s (the lock's), the "
                  "pinned proposal, and the power block of record at its own realised n", bind_ok,
                  (doc.get("analyzer_sha256") == a_sha, ((doc.get("power") or {}).get("of_record") or {}).get("display")),
                  cover=["CMD-VERDICTS-BINDING"])
            # the secondary output's habit block (d), per arm, from the arm's domain sessions
            sec_p = base / "out" / "complete" / "Q-F0_secondary.json"
            sec_d = json.loads(sec_p.read_text()) if sec_p.is_file() else {}
            rel_recs = readrule.release_full(json.loads(cp.read_text())["sessions"])
            hab_ok = []
            for arm_t, (kk, nn) in (("A0", ("k", "n")), ("A0s", ("j", "mS"))):
                got_h = ((sec_d.get("d") or {}).get(arm_t) or {}).get("habit")
                want_h = json.loads(json.dumps(habit_identity([r for r in rel_recs if r["template"] == arm_t
                                                               and r["domain"]])))
                hab_ok.append(got_h == want_h and isinstance(got_h, Mapping) and got_h.get("identity_holds") is True
                              and got_h.get("delta_c") == fs(Fraction(st_.get(kk, 0), st_.get(nn, 1)) - HALF))
            B.chk("reader: the secondary output carries (d)'s habit identity per arm (habit.break_rates over the arm's "
                  "domain sessions): it holds, and its delta_c is the VERDICTS arm's / sham's P - 1/2", all(hab_ok),
                  hab_ok, cover=["CMD-SECONDARY-HABIT"])
            # m:318's decisions, non-empty, carried verbatim into the VERDICTS output
            dd_q = [{"decision": "Q-F0 campaign cap kept (battery)", "date": "2026-10-21", "other_unit": "OLMo-sft",
                     "other_state": "DEAD"},
                    {"decision": "Q-F0 sham floor kept (battery)", "date": "2026-10-22", "other_unit": "Q-F3",
                     "other_state": "NOT-RUN"}]
            dec_ne = base / "decisions-Q-F0-nonempty.json"
            dec_ne.write_text(json.dumps({"schema": DECISIONS_SCHEMA, "unit": "Q-F0",
                                          "decisions_with_other_outcomes_known": dd_q}))
            vdn = V("Q-F0", cp, "decisions", decisions=dec_ne)
            ddoc = json.loads((base / "out" / "decisions" / "Q-F0_VERDICTS.json").read_text()) if vdn[0] == "ok" else {}
            dec_oth = base / "decisions-OLMo-sft-for-Q-F0.json"
            dec_oth.write_text(json.dumps({"schema": DECISIONS_SCHEMA, "unit": "OLMo-sft",
                                           "decisions_with_other_outcomes_known": []}))
            vdo = V("Q-F0", cp, "decisions-other", decisions=dec_oth)
            B.chk("reader: a non-empty decisions list is carried verbatim into {U}_VERDICTS.json (the empty one into "
                  "the default run); a decisions file naming another unit is refused",
                  vdn[0] == "ok" and ddoc.get("decisions_with_other_outcomes_known") == dd_q
                  and doc.get("decisions_with_other_outcomes_known") == [] and vdo[0] == "refused"
                  and "decisions input" in vdo[1], (vdn[0], vdo[1][:50]), cover=["CMD-VERDICTS-DECISIONS"])
            # V10 under a FALSE flag, end to end: an absent and an uncommitted flag source
            ph_tab = base / "table-placeholder.json"
            ph_tab.write_text(resume.json_text(placeholder_table(), indent=1), encoding="utf-8")
            fl_abs = base / "flag-absent.json"
            fl_unc = base / "flag-uncommitted.json"
            fl_unc.write_bytes((REPO / FLAG_SOURCE_REL).read_bytes())
            vfa = V("Q-F0", cp, "flag-absent", flag_source=fl_abs)
            vfu = V("Q-F0", cp, "flag-unc", flag_source=fl_unc, env=_bt_env(base, committed=uncommitted(fl_unc)))
            fdocs = [json.loads((base / "out" / n / "Q-F0_VERDICTS.json").read_text()) if v_[0] == "ok" else {}
                     for n, v_ in (("flag-absent", vfa), ("flag-unc", vfu))]

            def struck(d, src):
                o = d.get("v1_outputs") or {}
                strikes = [it["row_id"] for it in o.get("enumeration") or [] if (it.get("c") or {}).get("treatment")
                           == "strike"]
                return (d.get("flag", {}).get("value") is False and d["flag"]["path"] == _repo_rel(src)
                        and o.get("dose_note") == {"status": "none (struck, §7.5(c))", "text": None}
                        and strikes == ["P03", "P18"])
            B.chk("Q-F0 VERDICTS (V10) under a FALSE flag: an absent and an uncommitted --flag-source each give "
                  "flag FALSE with the passed path recorded, the dose note struck, and the (c) strike items (P03, "
                  "P18)", vfa[0] == vfu[0] == "ok" and struck(fdocs[0], fl_abs) and struck(fdocs[1], fl_unc),
                  (vfa[0], vfu[0], (fdocs[0].get("flag") or {}).get("reason")), cover=["CMD-VERDICTS-QF0-FLAG-FALSE"])
            vph = V("Q-F0", cp, "v10-placeholder", sentences=ph_tab)
            vut = V("Q-F0", cp, "v10-uncommitted", env=_bt_env(base, committed=uncommitted(_BT_STATE["rec_table"])))
            B.chk("refused at Q-F0's VERDICTS: a placeholder table (it serves G-ANL-F0 only, m:286) and an "
                  "uncommitted table of record", vph[0] == "refused" and "kind 'placeholder'" in vph[1]
                  and vut[0] == "refused" and "sentence table is not committed" in vut[1], (vph[1][:60], vut[1][:50]),
                  cover=["CMD-VERDICTS-QF0-TABLE-REFUSALS"])
            # write-once conflict
            vp = base / "out" / "complete" / "Q-F0_VERDICTS.json"
            keep = vp.read_bytes()
            vp.write_text(keep.decode("utf-8").replace('"unit": "Q-F0"', '"unit": "Q-F0" '))
            vw = V("Q-F0", cp, "complete")
            vp.write_bytes(keep)
            B.chk("refused: a write-once conflict (an existing VERDICTS with different bytes)",
                  vw[0] == "refused" and "write-once" in vw[1], vw[1][:60], cover=["REF-WRITE-ONCE"])
            # mutated copies of the COMPLETE checkpoint
            ck0 = json.loads(cp.read_text())

            def mutated(name, fn):
                ck = copy.deepcopy(ck0)
                fn(ck)
                p = r1 / "ckpt" / f"{name}.json"
                p.write_text(json.dumps(ck))
                return p
            tests = [
                ("NOT-ENDED", "refused", lambda ck: ck["campaign"].__setitem__("terminal", None), "has not ended"),
                ("STAGE", "refused", lambda ck: (ck["identity"].__setitem__("stage", "qual"),
                                                 [r.__setitem__("stage", "qual") for r in ck["sessions"]]),
                 "not Q-F0/campaign"),
                ("BACKEND-SPLICE", "refused", lambda ck: ck["provenance"][0]["record"].__setitem__("stage", "elsewhere"),
                 "backend identifier"),
                ("DOMAIN-STOP", "stop", lambda ck: ck["sessions"][0].__setitem__("domain", True), "domain field disagrees"),
                ("FIRSTPICK-STOP", "stop", lambda ck: _bt_flip_first(ck), "first_free_pick_P disagrees"),
                ("CELL-STOP", "stop", lambda ck: ck["sessions"][0]["cell"].__setitem__("P", ck["sessions"][0]["cell"]["Q"]),
                 "cell.P is not pair[map]"),
                ("UNVERIFIED", "refused", lambda ck: ck["sessions"][1].__setitem__("verified", False),
                 "not a verified record"),
                ("FFP-OUTSIDE-STOP", "stop", lambda ck: ck["sessions"][0].__setitem__("first_free_pick_P", False),
                 "first_free_pick_P set outside the domain"),
                ("EXCLROUND-STOP", "stop", lambda ck: ck["sessions"][0]["exclusion"].__setitem__(
                    "class", "lexical" if ck["sessions"][0]["exclusion"]["class"] != "lexical" else "echo"),
                 "is not its first excluding round's"),
                ("NO-FLOORS", "refused", lambda ck: ck["campaign"].__setitem__("floors", {}), "records no floors"),
                # the floors refusal is structural (V2): it is decided before V4 reads a defective record
                ("NO-FLOORS-BEFORE-V4", "refused", lambda ck: (ck["campaign"].__setitem__("floors", {}),
                                                               ck["sessions"][0].__setitem__("domain", True)),
                 "records no floors"),
            ]
            s0 = ck0["sessions"][0]
            B.chk("reader fixture: the COMPLETE campaign's session 0 is a forced-phase exclusion outside the domain "
                  "(the FFP-OUTSIDE, EXCLROUND and DOMAIN mutants act on it)", s0["domain"] is False
                  and s0["first_free_pick_P"] is None and (s0.get("exclusion") or {}).get("phase") == "forced",
                  (s0["domain"], (s0.get("exclusion") or {}).get("class")), cover=["REF-FIXTURE-S0"])
            for tag, want, fn, needle in tests:
                vv = V("Q-F0", mutated(tag, fn), f"m-{tag}")
                B.chk(f"{'refused' if want == 'refused' else 'STOP'}: {tag.lower().replace('-', ' ')} ({needle})",
                      vv[0] == want and needle in vv[1], vv[1][:70], cover=[f"REF-{tag}"])
            # a floor is a non-negative int: a negative floor on either arm, a bool and a float each refuse alone,
            # as a missing one does; zero floors are structurally accepted (the COMPLETE campaign is analyzed)
            fl_bad = {"neg-contrast": {"A0": -1, "A0s": 3}, "neg-sham": {"A0": 3, "A0s": -1},
                      "bool": {"A0": True, "A0s": 3}, "float": {"A0": 3.0, "A0s": 3}}
            fl_res = {k_: V("Q-F0", mutated(f"floors-{k_}", lambda ck, f_=f_: ck["campaign"].__setitem__("floors", f_)),
                            f"floors-{k_}") for k_, f_ in fl_bad.items()}
            v_fz = V("Q-F0", mutated("floors-zero", lambda ck: ck["campaign"].__setitem__("floors", {"A0": 0, "A0s": 0})),
                     "floors-zero")
            B.chk("refused: a negative floor (contrast or sham), a bool floor and a float floor, each alone (records no "
                  "floors, as for a missing one); zero floors are accepted (analyzed)",
                  all(r_[0] == "refused" and "records no floors" in r_[1] for r_ in fl_res.values()) and v_fz[0] == "ok",
                  ({k_: r_[0] for k_, r_ in fl_res.items()}, v_fz[0]), cover=["REF-FLOORS-NEGATIVE"])
            # the floors refusal is decided at V2, before V3 releases anything: readrule.release_full is never
            # called on it; an accepted run releases the campaign and both gate stages (3 calls)
            rel_calls: list = []
            real_release = readrule.release_full

            def counting_release(recs):
                rel_calls.append(len(recs))
                return real_release(recs)
            p_nf3 = mutated("no-floors-v3", lambda ck: ck["campaign"].__setitem__("floors", {}))
            with _bt_patched(readrule, "release_full", counting_release):
                v_nf3 = V("Q-F0", p_nf3, "m-no-floors-v3")
                n_nf3 = len(rel_calls)
                v_rel = V("Q-F0", cp, "release-count")
                n_rel = len(rel_calls) - n_nf3
            B.chk("refused before V3: the floors refusal releases no record (readrule.release_full not called, nothing "
                  "written); an accepted run releases the campaign and both gate stages (3 calls)",
                  v_nf3[0] == "refused" and "records no floors" in v_nf3[1] and n_nf3 == 0
                  and not any((base / "out" / "m-no-floors-v3").glob("Q-F0_*")) and v_rel[0] == "ok" and n_rel == 3,
                  (v_nf3[0], n_nf3, v_rel[0], n_rel), cover=["REF-NO-FLOORS-BEFORE-V3"])
            vu = V("OLMo-sft", cp, "other-unit")
            B.chk("refused: a different unit's checkpoint (Q-F0's campaign read as OLMo-sft)", vu[0] == "refused"
                  and "not OLMo-sft/campaign" in vu[1], vu[1][:70], cover=["REF-OTHER-UNIT"])
            other_lock = base / "LOCK-other.md"
            other_lock.write_text(lock_text + "x\n")
            vl = V("Q-F0", cp, "lock-sha", lock=other_lock)
            B.chk("refused: the identity's lock sha256 is not the lock's", vl[0] == "refused" and "lock_sha256" in vl[1],
                  vl[1][:70], cover=["REF-LOCK-SHA"])
            for tag, drop in (("ANALYZER", a_sha), ("PACKAGE", _BT_STATE["package_sha256"]),
                              ("CLOSURE", _BT_STATE["closure_sha256"]), ("TABLE", t_sha), ("PREPRINT", pp_sha)):
                lk = base / f"LOCK-no-{tag}.md"
                lk.write_text(lock_text.replace(drop, "-"))
                vv = V("Q-F0", cp, f"no-{tag}", lock=lk)
                B.chk(f"refused: the {tag.lower()} sha256 is not named in the lock (the full lock is accepted: "
                      f"C3-COMPLETE)", vv[0] == "refused" and "lock does not name" in vv[1], vv[1][:70],
                      cover=[f"REF-{tag}-NOT-IN-LOCK"])
            vpz = V("Q-F0", cp, "proposal", env=_bt_env(base, proposal_path=lock))
            B.chk("refused: a proposal whose sha256 is not the pinned v1.11's", vpz[0] == "refused" and "proposal" in vpz[1],
                  vpz[1][:70], cover=["REF-PROPOSAL-SHA"])
            vst = V("Q-F0", cp, "stub", env=_bt_env(base, allow_stub=False))
            B.chk("refused: STUB_MARK provenance outside the battery's internal path (PIN-30)",
                  vst[0] == "refused" and "stub" in vst[1], vst[1][:70], cover=["REF-STUB"])
            vlu = V("Q-F0", cp, "lock-uncommitted", env=_bt_env(base, committed=uncommitted(lock)))
            B.chk("refused: the lock not committed at HEAD (the analyzer committed; env double)",
                  vlu[0] == "refused" and "the lock is not committed at HEAD" in vlu[1], vlu[1][:60],
                  cover=["REF-LOCK-UNCOMMITTED"])
            vau = V("Q-F0", cp, "analyzer-uncommitted", env=_bt_env(base, committed=uncommitted(Path(__file__))))
            B.chk("refused: the analyzer not committed at HEAD (the lock committed; env double)",
                  vau[0] == "refused" and "the analyzer is not committed at HEAD" in vau[1], vau[1][:60],
                  cover=["REF-ANALYZER-UNCOMMITTED"])
            # PIN-30 per checkpoint: the campaign's and the gate stages' stub checks, each on its own
            no_stub = _bt_env(base, allow_stub=False)
            cp_ns = stub_free(cp, "campaign-no-stub", campaign=True)
            time_ns, qual_ns = stub_free(time_p, "time-no-stub"), stub_free(qual_p, "qual-no-stub")
            v_none = V("Q-F0", cp_ns, "stub-none", time=time_ns, qual=qual_ns, env=no_stub)
            v_camp = V("Q-F0", cp, "stub-campaign", time=time_ns, qual=qual_ns, env=no_stub)
            v_time = V("Q-F0", cp_ns, "stub-time", time=time_p, qual=qual_ns, env=no_stub)
            v_qual = V("Q-F0", cp_ns, "stub-qual", time=time_ns, qual=qual_p, env=no_stub)
            B.chk("refused (PIN-30), each check alone: a stub-written campaign beside stub-free gate stages; a stub-free "
                  "campaign beside a stub-written time or qualification stage; with no stub provenance anywhere the "
                  "CLI path analyzes", v_none[0] == "ok" and v_camp[0] == "refused" and "the campaign was written by "
                  "the self-test stub" in v_camp[1] and v_time[0] == "refused" and "the time checkpoint was written by "
                  "the self-test stub" in v_time[1] and v_qual[0] == "refused" and "the qual checkpoint was written "
                  "by the self-test stub" in v_qual[1], (v_none[0], v_camp[1][:40], v_time[1][:40]),
                  cover=["REF-STUB-CAMPAIGN-ONLY", "REF-STUB-GATE-ONLY"])
            # end pending (a finish killed before its end persisted)
            rp_ = C.root("pending")
            real = resume.write_checkpoint

            def w(path, ck):
                if (ck.get("campaign") or {}).get("terminal") is not None and "end_pending" not in ck:
                    raise stages._Interrupt("battery: killed before the end was persisted")
                real(path, ck)
            with _bt_patched(resume, "write_checkpoint", w):
                resp, excp = C.run("Q-F0", rp_, C.adapter("Q-F0", {"A0": 2, "A0s": 2}), {"A0": 2, "A0s": 2})
            vpd = V("Q-F0", rp_ / "ckpt" / "Q-F0_campaign.json", "pending")
            B.chk("refused: an end pending (finding R1)", isinstance(excp, stages._Interrupt) and vpd[0] == "refused"
                  and "end pending" in vpd[1], vpd[1][:70], cover=["REF-END-PENDING"])
            # a fired end look on a terminal campaign: refused without, analyzed with the seat's adjudication
            r_el = C.root("endlook")
            rule_el = lambda t, s, n, c: "Config choice one." if (t == "A0" and s < 3 and n == 1) else None
            res_el, _ = C.run("Q-F0", r_el, C.adapter("Q-F0", {"A0": 4, "A0s": 1}, rule_el), {"A0": 1, "A0s": 1})
            cp_el = Path(res_el["checkpoint"])
            ck_el = json.loads(cp_el.read_text())
            ve1 = V("Q-F0", cp_el, "endlook")
            adj = base / "adj.json"
            last = ck_el["campaign"]["pauses"][-1] if ck_el["campaign"]["pauses"] else {}
            adj.write_text(json.dumps({"schema": ADJ_SCHEMA, "unit": "Q-F0",
                                       "campaign_sha256": _sha256_bytes(cp_el.read_bytes()),
                                       "pause": {"kind": last.get("kind"), "at_launches": last.get("at_launches")},
                                       "text": "battery: the seat's adjudication (synthetic)"}))
            ve2 = V("Q-F0", cp_el, "endlook2", adjudication=adj)
            dj = json.loads((base / "out" / "endlook2" / "Q-F0_VERDICTS.json").read_text()) if ve2[0] == "ok" else {}
            B.chk("a fired end look on a terminal campaign: refused without --adjudication; analyzed with it, its path "
                  "and sha256 recorded", res_el["status"] == "PAUSE" and ck_el["campaign"]["terminal"]["status"] ==
                  "COMPLETE" and ve1[0] == "refused" and ve2[0] == "ok" and dj.get("adjudication", {}).get("sha256")
                  == _sha256_bytes(adj.read_bytes()), (res_el["status"], ve1[1][:40]),
                  cover=["C3-ENDLOOK-PAUSE", "REF-UNADJUDICATED"])
            # CAP with zero domain sessions
            r_cap = C.root("cap0")
            rule_all = lambda t, s, n, c: "Config choice one." if n == 1 else None
            import time as _time

            def rule_all_slow(t, s, n, c):
                # a session that ends at forced round 1 can take under half a millisecond (0 ms of
                # cap time); the first one is slowed so the cap is reached after it
                if t == "A0" and s == 0 and n == 1:
                    _time.sleep(0.01)
                return rule_all(t, s, n, c)
            res_c, _ = C.run("Q-F0", r_cap, C.adapter("Q-F0", {"A0": 6, "A0s": 6}, rule_all_slow),
                             {"A0": 2, "A0s": 2}, cap=1e-9)
            vc = V("Q-F0", Path(res_c["checkpoint"]), "cap0")
            nr = json.loads((base / "out" / "cap0" / "Q-F0_NOT-RUN.json").read_text()) if vc[0] == "ok" else {}
            B.chk("C3: CAP with no session reaching a first read -> NOT-RUN no-first-read:cap ({U}_NOT-RUN.json)",
                  res_c["status"] == "CAP" and vc[0] == "ok" and nr.get("cause") == "no-first-read:cap"
                  and nr.get("rows", {}).get("e2a", "").endswith("before its hour cap"), nr.get("cause"),
                  cover=["C3-CAP-ZERO"])
            # PI-STOP with zero domain sessions
            r_pi = C.root("pistop0")
            cut = lambda t, s, n, c: t == "A0s" and s == 0 and n == 1
            C.run("Q-F0", r_pi, C.adapter("Q-F0", {"A0": 2, "A0s": 2}, rule_all, cut), {"A0": 2, "A0s": 2})
            res_p, exc_p = C.run("Q-F0", r_pi, C.adapter("Q-F0", {"A0": 2, "A0s": 2}, rule_all), {"A0": 2, "A0s": 2},
                                 resume=True, pi_stop="PI: stop (battery)")
            vpi = V("Q-F0", r_pi / "ckpt" / "Q-F0_campaign.json", "pistop0")
            nrp = json.loads((base / "out" / "pistop0" / "Q-F0_NOT-RUN.json").read_text()) if vpi[0] == "ok" else {}
            B.chk("C3: PI-STOP with no session reaching a first read -> NOT-RUN no-first-read:pi-stop",
                  res_p is not None and res_p["status"] == "PI-STOP" and nrp.get("cause") == "no-first-read:pi-stop",
                  (res_p or {}).get("status"), cover=["C3-PISTOP-ZERO"])
            # G-VER STOP, zero and with data
            real_run = stages.run_session_qwen

            def tamper_at(tpl, s_):
                def tampered(adapter, sc, audit_, ban_ids, *, path_cached, term_rx):
                    rec = real_run(adapter, sc, audit_, ban_ids, path_cached=path_cached, term_rx=term_rx)
                    if sc.template == tpl and sc.s == s_:
                        rec["rounds"][0]["text"] += " x"
                    return rec
                return tampered
            r_g0 = C.root("gver0")
            with _bt_patched(stages, "run_session_qwen", tamper_at("A0", 0)):
                res_g0, _ = C.run("Q-F0", r_g0, C.adapter("Q-F0", {"A0": 2, "A0s": 2}), {"A0": 2, "A0s": 2})
            vg0 = V("Q-F0", Path(res_g0["checkpoint"]), "gver0")
            nrg = json.loads((base / "out" / "gver0" / "Q-F0_NOT-RUN.json").read_text()) if vg0[0] == "ok" else {}
            B.chk("C3: a G-VER STOP before any first read -> NOT-RUN no-first-read:gver-stop (the quarantined record "
                  "beside, not counted)", res_g0["status"] == "STOP" and nrg.get("cause") == "no-first-read:gver-stop"
                  and nrg.get("quarantined", [{}])[0].get("counted") is False, nrg.get("cause"),
                  cover=["C3-GVER-ZERO"])
            r_g1 = C.root("gver1")
            with _bt_patched(stages, "run_session_qwen", tamper_at("A0", 2)):
                res_g1, _ = C.run("Q-F0", r_g1, C.adapter("Q-F0", {"A0": 4, "A0s": 4}), {"A0": 4, "A0s": 4})
            vg1 = V("Q-F0", Path(res_g1["checkpoint"]), "gver1")
            dg1 = json.loads((base / "out" / "gver1" / "Q-F0_VERDICTS.json").read_text()) if vg1[0] == "ok" else {}
            ckg1 = json.loads(Path(res_g1["checkpoint"]).read_text())
            gl1 = dg1.get("guard_last_look") or {}
            el1 = (ckg1.get("campaign") or {}).get("end_look") or {}
            B.chk("C3: a G-VER STOP after domain sessions (launch 5 quarantined; 4 recorded, no cadence look) -> "
                  "analyzed as obtained (a PI stop by m:284); its end look, evaluated by stages at the STOP point (the "
                  "seat's C9(ii)), is the last look, named in the guard and the sentence as 'the end look at the STOP "
                  "(at 4 launches)'", res_g1["status"] == "STOP" and vg1[0] == "ok" and not ckg1["looks"]
                  and len(ckg1["sessions"]) == 4 and el1.get("look") == "end" and el1.get("at_launches") == 4
                  and gl1.get("source") == "end_look" and gl1.get("at_stop") is True
                  and gl1.get("label") == "the end look at the STOP (at 4 launches)"
                  and "the guard at the unit's last look (the end look at the STOP (at 4 launches)): Fisher"
                  in dg1.get("sentence", ""), (vg1[1][:30], gl1.get("label")), cover=["C3-GVER-DATA"])
            # past the first cadence look (40 launches): COMPLETE at 42 -> the end look is the last look;
            # a G-VER STOP at launch 41 -> the end look at the STOP IS look 1 at 40 (Code's application of the
            # seat's C9(ii))
            r_lk = C.root("look-end")
            res_lk, _ = C.run("Q-F0", r_lk, C.adapter("Q-F0", {"A0": 21, "A0s": 21}), {"A0": 21, "A0s": 21})
            v_lk = V("Q-F0", Path(res_lk["checkpoint"]), "look-end")
            d_lk = json.loads((base / "out" / "look-end" / "Q-F0_VERDICTS.json").read_text()) if v_lk[0] == "ok" else {}
            ck_lk = json.loads(Path(res_lk["checkpoint"]).read_text())
            r_ls = C.root("look-stop")
            with _bt_patched(stages, "run_session_qwen", tamper_at("A0", 20)):
                res_ls, _ = C.run("Q-F0", r_ls, C.adapter("Q-F0", {"A0": 21, "A0s": 21}), {"A0": 21, "A0s": 21})
            v_ls = V("Q-F0", Path(res_ls["checkpoint"]), "look-stop")
            d_ls = json.loads((base / "out" / "look-stop" / "Q-F0_VERDICTS.json").read_text()) if v_ls[0] == "ok" else {}
            ck_ls = json.loads(Path(res_ls["checkpoint"]).read_text())
            g_lk, g_ls = d_lk.get("guard_last_look") or {}, d_ls.get("guard_last_look") or {}
            ck2 = copy.deepcopy(ck_ls)                     # a second cadence look (at 80), production-shaped,
            if ck2["looks"]:                               # and no end look: the cadence fallback's label
                lk2 = copy.deepcopy(ck2["looks"][-1])
                lk2.update(look_index=1, at_launches=80)
                lk2["result"].update(look=2, at_launches=80)
                ck2["looks"].append(lk2)
            ck2["campaign"]["end_look"] = None
            g2 = guard_at_last_look(ck2, "Q-F0", "STOP")
            el_ls = (ck_ls.get("campaign") or {}).get("end_look") or {}
            B.chk("last look: COMPLETE at 42 launches with look 1 at 40 on disk -> the end look (at 42) is named, not "
                  "the cadence look (not at a STOP)", v_lk[0] == "ok" and [lk["at_launches"] for lk in ck_lk["looks"]]
                  == [40] and g_lk.get("source") == "end_look" and g_lk.get("label") == "the end look at 42 launches"
                  and g_lk.get("at_stop") is False
                  and "(the end look at 42 launches)" in d_lk.get("sentence", ""), (v_lk[1][:30], g_lk.get("label")),
                  cover=["C3-LASTLOOK-END-WINS"])
            B.chk("last look: a G-VER STOP at launch 41 after look 1 at 40 -> the end look at the STOP IS look 1 "
                  "(end_is_look 1, no new pause: Code's application of the seat's C9(ii)), named 'look 1 at 40 launches, the end look at the "
                  "STOP' in the guard and the sentence; guard_at_last_look's cadence fallback keeps its label (a second "
                  "cadence look at 80, no end look: 'look 2 at 80 launches, the last cadence look')",
                  v_ls[0] == "ok" and res_ls["status"] == "STOP"
                  and [lk["at_launches"] for lk in ck_ls["looks"]] == [40] and el_ls.get("end_is_look") == 1
                  and el_ls.get("at_launches") == 40 and ck_ls["campaign"]["pauses"] == []
                  and g_ls.get("source") == "end_look" and g_ls.get("at_stop") is True
                  and g_ls.get("label") == "look 1 at 40 launches, the end look at the STOP"
                  and "(look 1 at 40 launches, the end look at the STOP)" in d_ls.get("sentence", "")
                  and g2["label"] == "look 2 at 80 launches, the last cadence look" and g2["source"] == "cadence",
                  (v_ls[1][:30], res_ls["status"], g_ls.get("label")), cover=["C3-LASTLOOK-STOP-ENDISLOOK"])
            # a STOP past a cadence look on a launch count that is not a multiple of 40: a G-VER STOP at launch 42
            # (A0s s=20 quarantined; 41 recorded) after look 1 at 40 -> the end look evaluated at the STOP point (at
            # 41), not look 1 reused; named 'the end look at the STOP (at 41 launches)'
            r_lp = C.root("look-past")
            with _bt_patched(stages, "run_session_qwen", tamper_at("A0s", 20)):
                res_lp, _ = C.run("Q-F0", r_lp, C.adapter("Q-F0", {"A0": 21, "A0s": 21}), {"A0": 21, "A0s": 21})
            v_lp = V("Q-F0", Path(res_lp["checkpoint"]), "look-past")
            d_lp = json.loads((base / "out" / "look-past" / "Q-F0_VERDICTS.json").read_text()) if v_lp[0] == "ok" else {}
            ck_lp = json.loads(Path(res_lp["checkpoint"]).read_text())
            g_lp = d_lp.get("guard_last_look") or {}
            el_lp = (ck_lp.get("campaign") or {}).get("end_look") or {}
            B.chk("last look: a G-VER STOP at launch 42 (41 recorded) past look 1 at 40 -> the end look evaluated at the "
                  "STOP point (look 'end' at 41, no end_is_look; look 1 not reused -- the seat's C9(ii)), named 'the end "
                  "look at the STOP (at 41 launches)' in the guard and the sentence",
                  v_lp[0] == "ok" and res_lp["status"] == "STOP" and len(ck_lp["sessions"]) == 41
                  and [lk["at_launches"] for lk in ck_lp["looks"]] == [40] and el_lp.get("look") == "end"
                  and el_lp.get("at_launches") == 41 and "end_is_look" not in el_lp and ck_lp["campaign"]["pauses"] == []
                  and g_lp.get("source") == "end_look" and g_lp.get("at_stop") is True
                  and g_lp.get("label") == "the end look at the STOP (at 41 launches)"
                  and "(the end look at the STOP (at 41 launches))" in d_lp.get("sentence", ""),
                  (v_lp[1][:30], res_lp["status"], g_lp.get("label")), cover=["C3-LASTLOOK-STOP-PAST-CADENCE"])
            # Code's guard for the seat's C9(ii), at V2: a STOP-ended campaign with a launch recorded and no end look is refused
            # before V3 releases anything (readrule.release_full not called, nothing written); with the end look
            # (as stages writes it) it is analyzed, and a STOP with no launch recorded carries none and is analyzed
            # (C3-GVER-ZERO)
            def no_end_look(src: Path, name: str) -> Path:
                ck_ = json.loads(Path(src).read_text())
                ck_["campaign"]["end_look"] = None
                p_ = Path(src).parent / f"{name}.json"
                p_.write_text(json.dumps(ck_))
                return p_
            rel_n: list = []
            real_rel_n = readrule.release_full

            def count_rel_n(recs):
                rel_n.append(len(recs))
                return real_rel_n(recs)
            with _bt_patched(readrule, "release_full", count_rel_n):
                v_nel = {"G-VER at 41": V("Q-F0", no_end_look(Path(res_ls["checkpoint"]), "no-end-look-41"),
                                          "no-end-look-41"),
                         "G-VER at 5": V("Q-F0", no_end_look(Path(res_g1["checkpoint"]), "no-end-look-5"),
                                         "no-end-look-5")}
                n_rel_n = len(rel_n)
            ckg0 = json.loads(Path(res_g0["checkpoint"]).read_text())
            B.chk("refused at V2 (Code's guard for the seat's C9(ii)): a STOP-ended campaign with launches recorded and no end look (its "
                  "end look removed: the G-VER STOPs at 41 and at 5) -- 'records no end look at its STOP', before V3 "
                  "releases any record, nothing written; with its end look each is analyzed (C3-LASTLOOK-STOP-ENDISLOOK, "
                  "C3-GVER-DATA); a G-VER STOP with no launch recorded has no end look and is analyzed (NOT-RUN)",
                  all(r_[0] == "refused" and "records no end look at its STOP (the seat's C9(ii))" in r_[1]
                      for r_ in v_nel.values()) and n_rel_n == 0
                  and not any(any((base / "out" / n_).glob("Q-F0_*")) for n_ in ("no-end-look-41", "no-end-look-5"))
                  and v_ls[0] == "ok" and vg1[0] == "ok" and ckg0["sessions"] == []
                  and ckg0["campaign"]["end_look"] is None and vg0[0] == "ok",
                  ({k_: r_[0] for k_, r_ in v_nel.items()}, n_rel_n), cover=["C3-STOP-NO-ENDLOOK-REFUSED"])
            # hair-trigger STOP: refused without a PI-stop record, analyzed with one
            r_h = C.root("hair")
            rh = lambda t, s, n, c: "<|im_end|>" if (t == "A0" and s == 1 and n == 7) else None
            res_h, _ = C.run("Q-F0", r_h, C.adapter("Q-F0", {"A0": 4, "A0s": 4}, rh), {"A0": 4, "A0s": 4})
            cp_h = Path(res_h["checkpoint"])
            vh1 = V("Q-F0", cp_h, "hair")
            pis = base / "pistop.json"
            pis.write_text(json.dumps({"schema": PI_STOP_SCHEMA, "unit": "Q-F0", "bar": HAIR_BAR,
                                       "campaign_sha256": _sha256_bytes(cp_h.read_bytes()),
                                       "text": "PI: stop on the hair trigger (battery)"}))
            vh2 = V("Q-F0", cp_h, "hair2", pi_stop=pis)
            B.chk("C3: a scaffold_absorption hair-trigger STOP with no disposition is refused (PIN-8)",
                  res_h["status"] == "STOP" and vh1[0] == "refused" and "PI-stop record" in vh1[1], vh1[1][:60],
                  cover=["C3-HAIR-NODISP"])
            B.chk("C3: the same STOP with a declared PI-stop record -> analyzed as obtained (path and sha recorded)",
                  vh2[0] == "ok" and json.loads((base / "out" / "hair2" / "Q-F0_VERDICTS.json").read_text())
                  ["pi_stop_record"]["sha256"] == _sha256_bytes(pis.read_bytes()), vh2[1][:50], cover=["C3-HAIR-DISP"])
            # the seat's C9(ii): the hair-trigger STOP (contrast free phase, launch 3) carries its end look at the
            # STOP point, and the sentence names it as the STOP's
            ck_h = json.loads(cp_h.read_text())
            dh2 = json.loads((base / "out" / "hair2" / "Q-F0_VERDICTS.json").read_text()) if vh2[0] == "ok" else {}
            gh2 = dh2.get("guard_last_look") or {}
            B.chk("C3: the hair-trigger STOP at launch 3 records its end look at the STOP point (look 'end' at 3, "
                  "silent, no pause); VERDICTS names it 'the end look at the STOP (at 3 launches)' in the guard and the "
                  "sentence (the seat's C9(ii))", vh2[0] == "ok" and len(ck_h["sessions"]) == 3
                  and (ck_h["campaign"]["end_look"] or {}).get("look") == "end"
                  and ck_h["campaign"]["end_look"]["at_launches"] == 3 and ck_h["campaign"]["pauses"] == []
                  and gh2.get("source") == "end_look" and gh2.get("at_stop") is True
                  and gh2.get("label") == "the end look at the STOP (at 3 launches)"
                  and "(the end look at the STOP (at 3 launches))" in dh2.get("sentence", ""),
                  (vh2[1][:30], gh2.get("label")), cover=["C3-HAIR-ENDLOOK-LABEL"])
            # the declared seat inputs bind (PIN-8, PIN-9): an adjudication or PI-stop record is for THIS unit,
            # THIS checkpoint (its sha256) and THIS pause / bar -- each field alone refuses; the exact one is
            # accepted (C3-ENDLOOK-PAUSE, C3-HAIR-DISP)
            adj_doc0, pis_doc0 = json.loads(adj.read_text()), json.loads(pis.read_text())

            def seat_variant(doc0, name, **over):
                p = base / f"{name}.json"
                p.write_text(json.dumps({**doc0, **over}))
                return p
            # a hair-trigger STOP whose end look FIRES (3/3 contrast pre-pick exclusions against 0/3 on the sham, at
            # launch 6): its end_look pause is appended unadjudicated, so PIN-9's path applies beside PIN-8's -- the
            # seat's adjudication (naming that pause) AND the PI-stop record are each required: refused with
            # neither, with the PI-stop record only (PIN-9), with the adjudication only (PIN-8); analyzed with both,
            # both recorded (path and sha256)
            r_hf = C.root("hair-endlook")
            rhf = lambda t, s, n, c: ("<|im_end|>" if (t == "A0s" and s == 2 and n == 7)       # noqa: E731
                                      else "Config choice one." if (t == "A0" and s < 3 and n == 1) else None)
            res_hf, _ = C.run("Q-F0", r_hf, C.adapter("Q-F0", {"A0": 4, "A0s": 4}, rhf), {"A0": 4, "A0s": 4})
            cp_hf = Path(res_hf["checkpoint"])
            ck_hf = json.loads(cp_hf.read_text())
            pz_hf = (ck_hf.get("campaign") or {}).get("pauses") or [{}]
            sha_hf = _sha256_bytes(cp_hf.read_bytes())
            adj_hf = seat_variant(adj_doc0, "adj-hair-endlook", campaign_sha256=sha_hf,
                                  pause={"kind": pz_hf[-1].get("kind"), "at_launches": pz_hf[-1].get("at_launches")})
            pis_hf = seat_variant(pis_doc0, "pis-hair-endlook", campaign_sha256=sha_hf)
            v_hf = {"neither": V("Q-F0", cp_hf, "hf-neither"),
                    "pi-stop only": V("Q-F0", cp_hf, "hf-pis", pi_stop=pis_hf),
                    "adjudication only": V("Q-F0", cp_hf, "hf-adj", adjudication=adj_hf),
                    "both": V("Q-F0", cp_hf, "hf-both", adjudication=adj_hf, pi_stop=pis_hf)}
            d_hf = (json.loads((base / "out" / "hf-both" / "Q-F0_VERDICTS.json").read_text())
                    if v_hf["both"][0] == "ok" else {})
            g_hf = d_hf.get("guard_last_look") or {}
            B.chk("C3: a hair-trigger STOP at launch 6 whose end look fires (the .20 absolute guard, binding on Qwen): the "
                  "end_look pause {end_look, 6} is unadjudicated -- refused with neither seat input and with the PI-stop "
                  "record only (PIN-9), with the adjudication only (PIN-8); analyzed with both, each recorded with its "
                  "path and sha256, the guard at 'the end look at the STOP (at 6 launches)', fired",
                  res_hf["status"] == "STOP" and len(ck_hf["sessions"]) == 6
                  and pz_hf == [{"at_launches": 6, "kind": "end_look", "look": "end",
                                 "bars": [r_["name"] for r_ in ck_hf["campaign"]["end_look"]["results"] if r_["fired"]],
                                 "adjudication": None}]
                  and v_hf["neither"][0] == v_hf["pi-stop only"][0] == "refused"
                  and all("last pause is unadjudicated" in v_hf[k_][1] for k_ in ("neither", "pi-stop only"))
                  and v_hf["adjudication only"][0] == "refused" and "PI-stop record" in v_hf["adjudication only"][1]
                  and v_hf["both"][0] == "ok"
                  and (d_hf.get("adjudication") or {}).get("sha256") == _sha256_bytes(adj_hf.read_bytes())
                  and (d_hf.get("pi_stop_record") or {}).get("sha256") == _sha256_bytes(pis_hf.read_bytes())
                  and g_hf.get("label") == "the end look at the STOP (at 6 launches)" and g_hf.get("at_stop") is True
                  and (g_hf.get("abs") or {}).get("fired") is True
                  and "(the end look at the STOP (at 6 launches))" in d_hf.get("sentence", ""),
                  ({k_: r_[0] for k_, r_ in v_hf.items()}, g_hf.get("label")), cover=["C3-HAIR-ENDLOOK-PAUSE"])
            # a G-VER STOP whose freshly evaluated end look FIRES (A0 s=3 quarantined at launch 7 after 3/3 contrast
            # pre-pick exclusions against 0/3 on the sham): its end_look pause {end_look, 6} is unadjudicated and a
            # G-VER STOP needs no PI-stop record (PIN-8 is the hair triggers'), so PIN-9's path is the only seat
            # input -- refused with neither and with a PI-stop record only (PIN-9); analyzed with the adjudication
            # alone, recorded with its path and sha256; refused with both (a surplus --pi-stop)
            r_ge = C.root("gver-endlook")
            rge = lambda t, s, n, c: "Config choice one." if (t == "A0" and s < 3 and n == 1) else None   # noqa: E731
            with _bt_patched(stages, "run_session_qwen", tamper_at("A0", 3)):
                res_ge, _ = C.run("Q-F0", r_ge, C.adapter("Q-F0", {"A0": 4, "A0s": 4}, rge), {"A0": 4, "A0s": 4})
            cp_ge = Path(res_ge["checkpoint"])
            ck_ge = json.loads(cp_ge.read_text())
            pz_ge = (ck_ge.get("campaign") or {}).get("pauses") or [{}]
            sha_ge = _sha256_bytes(cp_ge.read_bytes())
            adj_ge = seat_variant(adj_doc0, "adj-gver-endlook", campaign_sha256=sha_ge,
                                  pause={"kind": pz_ge[-1].get("kind"), "at_launches": pz_ge[-1].get("at_launches")})
            pis_ge = seat_variant(pis_doc0, "pis-gver-endlook", campaign_sha256=sha_ge)
            v_ge = {"neither": V("Q-F0", cp_ge, "ge-neither"),
                    "pi-stop only": V("Q-F0", cp_ge, "ge-pis", pi_stop=pis_ge),
                    "adjudication": V("Q-F0", cp_ge, "ge-adj", adjudication=adj_ge),
                    "both": V("Q-F0", cp_ge, "ge-both", adjudication=adj_ge, pi_stop=pis_ge)}
            d_ge = (json.loads((base / "out" / "ge-adj" / "Q-F0_VERDICTS.json").read_text())
                    if v_ge["adjudication"][0] == "ok" else {})
            g_ge = d_ge.get("guard_last_look") or {}
            B.chk("C3: a G-VER STOP at launch 7 whose end look, evaluated fresh at 6 launches, fires: the end_look pause "
                  "{end_look, 6} is unadjudicated -- refused with no seat input and with a PI-stop record only (PIN-9); "
                  "analyzed with the seat's adjudication alone (path and sha256 recorded, no PI-stop record), the guard "
                  "at 'the end look at the STOP (at 6 launches)', fired; with both, the --pi-stop is surplus (refused)",
                  res_ge["status"] == "STOP" and (ck_ge.get("stop") or {}).get("bar") != HAIR_BAR
                  and len(ck_ge["sessions"]) == 6
                  and pz_ge == [{"at_launches": 6, "kind": "end_look", "look": "end",
                                 "bars": [r_["name"] for r_ in ck_ge["campaign"]["end_look"]["results"] if r_["fired"]],
                                 "adjudication": None}]
                  and v_ge["neither"][0] == v_ge["pi-stop only"][0] == "refused"
                  and all("last pause is unadjudicated" in v_ge[k_][1] for k_ in ("neither", "pi-stop only"))
                  and v_ge["adjudication"][0] == "ok"
                  and (d_ge.get("adjudication") or {}).get("sha256") == _sha256_bytes(adj_ge.read_bytes())
                  and d_ge.get("pi_stop_record") is None
                  and g_ge.get("label") == "the end look at the STOP (at 6 launches)" and g_ge.get("at_stop") is True
                  and (g_ge.get("abs") or {}).get("fired") is True and (g_ge.get("fisher") or {}).get("fired") is True
                  and "(the end look at the STOP (at 6 launches))" in d_ge.get("sentence", "")
                  and v_ge["both"][0] == "refused" and "--pi-stop given" in v_ge["both"][1],
                  ({k_: r_[0] for k_, r_ in v_ge.items()}, g_ge.get("label")), cover=["C3-GVER-ENDLOOK-PAUSE"])
            # stages' case (b): a hair-trigger STOP on launch 40 whose look 1 fires -- the end look IS look 1 and the
            # pause it raised at the STOP is kind 'look' {look, 40}: PIN-9 and PIN-8 each apply -- refused with
            # neither, with the PI-stop record only (PIN-9), with the PI-stop record and an adjudication naming
            # {end_look, 40} (the wrong kind; PIN-9), with the adjudication only (PIN-8); analyzed with both, named
            # 'look 1 at 40 launches, the end look at the STOP'
            r_hl = C.root("hair-look40")
            rhl = lambda t, s, n, c: ("<|im_end|>" if (t == "A0s" and s == 19 and n == 7)      # noqa: E731
                                      else "Config choice one." if (t == "A0s" and n == 6) else None)
            res_hl, _ = C.run("Q-F0", r_hl, C.adapter("Q-F0", {"A0": 21, "A0s": 21}, rhl), {"A0": 21, "A0s": 21})
            cp_hl = Path(res_hl["checkpoint"])
            ck_hl = json.loads(cp_hl.read_text())
            pz_hl = (ck_hl.get("campaign") or {}).get("pauses") or [{}]
            lk_hl = ck_hl["looks"][0]["result"] if ck_hl.get("looks") else {}
            sha_hl = _sha256_bytes(cp_hl.read_bytes())
            adj_hl = seat_variant(adj_doc0, "adj-hair-look40", campaign_sha256=sha_hl,
                                  pause={"kind": "look", "at_launches": 40})
            adj_hl_k = seat_variant(adj_doc0, "adj-hair-look40-kind", campaign_sha256=sha_hl,
                                    pause={"kind": "end_look", "at_launches": 40})
            pis_hl = seat_variant(pis_doc0, "pis-hair-look40", campaign_sha256=sha_hl)
            v_hl = {"neither": V("Q-F0", cp_hl, "hl-neither"),
                    "pi-stop only": V("Q-F0", cp_hl, "hl-pis", pi_stop=pis_hl),
                    "wrong kind": V("Q-F0", cp_hl, "hl-kind", adjudication=adj_hl_k, pi_stop=pis_hl),
                    "adjudication only": V("Q-F0", cp_hl, "hl-adj", adjudication=adj_hl),
                    "both": V("Q-F0", cp_hl, "hl-both", adjudication=adj_hl, pi_stop=pis_hl)}
            d_hl = (json.loads((base / "out" / "hl-both" / "Q-F0_VERDICTS.json").read_text())
                    if v_hl["both"][0] == "ok" else {})
            g_hl = d_hl.get("guard_last_look") or {}
            B.chk("C3: a hair-trigger STOP on launch 40 whose look 1 fires (stages' case (b)): the pause {look, 40} is "
                  "unadjudicated -- refused with neither seat input, with the PI-stop record only and with an "
                  "adjudication naming {end_look, 40} (PIN-9), with the adjudication only (PIN-8); analyzed with both, "
                  "each recorded, the guard at 'look 1 at 40 launches, the end look at the STOP'",
                  res_hl["status"] == "STOP" and len(ck_hl["sessions"]) == 40 and lk_hl.get("fired") is True
                  and (ck_hl["campaign"].get("end_look") or {}).get("end_is_look") == 1
                  and pz_hl == [{"at_launches": 40, "kind": "look", "look": 1,
                                 "bars": [r_["name"] for r_ in lk_hl["results"] if r_["fired"]], "adjudication": None}]
                  and all(v_hl[k_][0] == "refused" and "last pause is unadjudicated" in v_hl[k_][1]
                          for k_ in ("neither", "pi-stop only", "wrong kind"))
                  and v_hl["adjudication only"][0] == "refused" and "PI-stop record" in v_hl["adjudication only"][1]
                  and v_hl["both"][0] == "ok"
                  and (d_hl.get("adjudication") or {}).get("sha256") == _sha256_bytes(adj_hl.read_bytes())
                  and (d_hl.get("pi_stop_record") or {}).get("sha256") == _sha256_bytes(pis_hl.read_bytes())
                  and g_hl.get("label") == "look 1 at 40 launches, the end look at the STOP" and g_hl.get("at_stop") is True
                  and "(look 1 at 40 launches, the end look at the STOP)" in d_hl.get("sentence", ""),
                  ({k_: r_[0] for k_, r_ in v_hl.items()}, g_hl.get("label")), cover=["C3-HAIR-LOOK40-PAUSE"])
            # the V2 refusal is bar-agnostic: the hair-trigger STOP at launch 3 with its end look removed,
            # offered with a PI-stop record bound to that copy (PIN-8 satisfied), is refused at V2 before V3
            # releases any record; with its end look it is analyzed (C3-HAIR-DISP)
            cp_hne = no_end_look(cp_h, "hair-no-end-look")
            pis_hne = seat_variant(pis_doc0, "pis-hair-no-end-look", campaign_sha256=_sha256_bytes(cp_hne.read_bytes()))
            rel_h: list = []

            def count_rel_h(recs):
                rel_h.append(len(recs))
                return real_rel_n(recs)
            with _bt_patched(readrule, "release_full", count_rel_h):
                v_hne = V("Q-F0", cp_hne, "hair-no-end-look", pi_stop=pis_hne)
            B.chk("refused at V2 (Code's guard for the seat's C9(ii)), whatever the STOP's bar: the hair-trigger STOP at launch 3 with its "
                  "end look removed, offered with a PI-stop record bound to that checkpoint -- 'records no end look at "
                  "its STOP', before V3 releases any record, nothing written; with its end look it is analyzed "
                  "(C3-HAIR-DISP)",
                  v_hne[0] == "refused" and "records no end look at its STOP (the seat's C9(ii))" in v_hne[1]
                  and rel_h == [] and not any((base / "out" / "hair-no-end-look").glob("Q-F0_*"))
                  and (ck_h.get("stop") or {}).get("bar") == HAIR_BAR and vh2[0] == "ok",
                  (v_hne[0], v_hne[1][:60], len(rel_h)), cover=["C3-STOP-NO-ENDLOOK-HAIR-REFUSED"])
            # PIN-46 and PIN-45 (step 15): hand edits of production-written checkpoints, each offered to VERDICTS
            # with readrule.release_full counted (a refusal at V2 releases nothing) -- (the result, the release
            # calls, the Q-F0_* files written); a seat input, where given, is bound to the edited copy's sha256
            def v2_edit(src: Path, name: str, fn, *, adj_pause=None, pis_=False):
                ck_ = json.loads(Path(src).read_text())
                fn(ck_)
                p_ = Path(src).parent / f"{name}.json"
                p_.write_text(json.dumps(ck_))
                sha_ = _sha256_bytes(p_.read_bytes())
                kw_ = {}
                if adj_pause is not None:
                    kw_["adjudication"] = seat_variant(adj_doc0, f"adj-{name}", campaign_sha256=sha_, pause=adj_pause)
                if pis_:
                    kw_["pi_stop"] = seat_variant(pis_doc0, f"pis-{name}", campaign_sha256=sha_)
                calls_: list = []

                def count_(recs):
                    calls_.append(len(recs))
                    return real_rel_n(recs)
                with _bt_patched(readrule, "release_full", count_):
                    r_ = V("Q-F0", p_, name, **kw_)
                return r_, len(calls_), sorted(x.name for x in (base / "out" / name).glob("Q-F0_*"))
            MSG_B = "REFUSED: a fired end look records no matching pause ("
            MSG_C = "REFUSED: the end look's launch count ("

            def v2_refused(res_, needle):
                return (res_[0][0] == "refused" and res_[0][1].startswith(needle)
                        and res_[0][1].endswith("-- not written by the lock's package") and res_[1] == 0 and res_[2] == [])
            # (c) the end look's launch count (PIN-46)
            ck_lp0 = json.loads(Path(res_lp["checkpoint"]).read_text())

            def reuse_look1(ck_):                # what the D2 review's mutant endislook_any_look writes on this fixture, by hand
                ck_["campaign"]["end_look"] = {**copy.deepcopy(ck_["looks"][0]["result"]), "end_is_look": 1}
            c_1 = v2_edit(Path(res_lp["checkpoint"]), "count-reuse-41", reuse_look1)
            B.chk("refused at V2 (PIN-46): the end look reused at 40 (look 1, end_is_look 1) against 41 sessions recorded "
                  "-- the closest existing case to the D2 review's endislook_any_look scenario (there a hair-trigger "
                  "STOP at launch 42, 42 recorded; here the G-VER STOP at launch 42, 41 recorded, past a silent look 1 "
                  "at 40): 'the end look's launch count (40) is not the launches recorded (41)', release_full not called, "
                  "nothing written; unedited it is analyzed (C3-LASTLOOK-STOP-PAST-CADENCE)",
                  v2_refused(c_1, MSG_C) and "(40) is not the launches recorded (41)" in c_1[0][1] and v_lp[0] == "ok"
                  and len(ck_lp0["sessions"]) == 41 and ck_lp0["looks"][0]["result"]["fired"] is False,
                  (c_1[0][0], c_1[0][1][:72], c_1[1], c_1[2]), cover=["C3-ENDLOOK-COUNT-REUSE"])
            c_1n = v2_edit(Path(res_lp["checkpoint"]), "count-reuse-at-41", lambda ck_: ck_["campaign"].__setitem__(
                "end_look", {**copy.deepcopy(ck_["looks"][0]["result"]), "end_is_look": 1, "at_launches": 41}))
            B.chk("refused at V2 (PIN-46, the reuse clause): on the same G-VER STOP (41 recorded), the end look recorded "
                  "as look 1 reused but with at_launches 41 -- its count is the launches recorded, but look 1 is "
                  "recorded at 40, not 41: 'the end look's launch count (41) is not that of the look it reuses (look 1, "
                  "recorded at [40])', release_full not called, nothing written",
                  v2_refused(c_1n, MSG_C) and "(41) is not that of the look it reuses (look 1, recorded at [40])"
                  in c_1n[0][1], (c_1n[0][0], c_1n[0][1][:90], c_1n[1], c_1n[2]),
                  cover=["C3-ENDLOOK-COUNT-REUSED-LOOK"])
            el_n = ck_el["campaign"]["end_look"]["at_launches"]
            el_pz = {"kind": "end_look", "at_launches": el_n}
            c_2 = {d_: v2_edit(cp_el, f"count-terminal{d_:+d}", lambda ck_, d_=d_: ck_["campaign"]["end_look"].__setitem__(
                       "at_launches", el_n + d_), adj_pause=el_pz) for d_ in (1, -1)}
            B.chk("refused at V2 (PIN-46): the terminal COMPLETE campaign's fired end look with its at_launches +1 and -1, "
                  "each offered with the seat's adjudication bound to that copy and its pause -- PIN-46's own message, "
                  "not PIN-45's (the launch count is checked first), release_full not called, nothing written; "
                  "unedited: refused without --adjudication, analyzed with it (C3-ENDLOOK-PAUSE)",
                  all(v2_refused(r_, MSG_C) and f"({el_n + d_}) is not the launches recorded ({el_n})" in r_[0][1]
                      for d_, r_ in c_2.items()) and el_n == len(ck_el["sessions"]) and ve1[0] == "refused"
                  and ve2[0] == "ok", {d_: (r_[0][0], r_[1], r_[2]) for d_, r_ in c_2.items()},
                  cover=["C3-ENDLOOK-COUNT-TERMINAL"])
            c_3 = v2_edit(Path(res_g1["checkpoint"]), "count-stop-1",
                          lambda ck_: ck_["campaign"]["end_look"].__setitem__("at_launches", 3))
            c_3f = v2_edit(Path(res_g1["checkpoint"]), "count-stop-float",
                           lambda ck_: ck_["campaign"]["end_look"].__setitem__("at_launches", 4.0))
            B.chk("refused at V2 (PIN-46): a STOP's end look (the G-VER STOP at launch 5, end look at 4, 4 recorded) with "
                  "its at_launches -1 -- 'the end look's launch count (3) is not the launches recorded (4)' -- and as "
                  "the float 4.0 (a launch count is an int); release_full not called, nothing written; unedited it is "
                  "analyzed (C3-GVER-DATA)",
                  v2_refused(c_3, MSG_C) and "(3) is not the launches recorded (4)" in c_3[0][1] and vg1[0] == "ok"
                  and v2_refused(c_3f, MSG_C) and "(4.0) is not the launches recorded (4)" in c_3f[0][1]
                  and el1.get("at_launches") == 4, (c_3[0][0], c_3[0][1][:72], c_3[1], c_3[2], c_3f[0][0]),
                  cover=["C3-ENDLOOK-COUNT-STOP"])
            # (b) a fired end look without a matching pause (PIN-45)
            drop_last = lambda ck_: ck_["campaign"]["pauses"].pop()                               # noqa: E731
            b_1 = v2_edit(cp_el, "nopause-terminal", drop_last)
            B.chk("refused at V2 (PIN-45): the terminal COMPLETE campaign's fresh fired end look with its end_look pause "
                  "removed (no pause left, so PIN-9 would ask for no adjudication) -- 'a fired end look records no "
                  "matching pause', release_full not called, nothing written; unedited: refused without "
                  "--adjudication, analyzed with it (C3-ENDLOOK-PAUSE)",
                  v2_refused(b_1, MSG_B) and "the campaign's last pause must be" in b_1[0][1]
                  and len(ck_el["campaign"]["pauses"]) == 1 and ve1[0] == "refused" and ve2[0] == "ok",
                  (b_1[0][0], b_1[0][1][:60], b_1[1], b_1[2]), cover=["C3-ENDLOOK-NOPAUSE-TERMINAL"])
            b_2 = v2_edit(cp_hf, "nopause-hair", drop_last, pis_=True)
            B.chk("refused at V2 (PIN-45): the hair-trigger STOP at launch 6 whose fresh end look fires, its end_look "
                  "pause removed, offered with a PI-stop record bound to that copy -- 'a fired end look records no "
                  "matching pause', release_full not called, nothing written; unedited it is analyzed with both seat "
                  "inputs (C3-HAIR-ENDLOOK-PAUSE)", v2_refused(b_2, MSG_B) and v_hf["both"][0] == "ok",
                  (b_2[0][0], b_2[0][1][:60], b_2[1], b_2[2]), cover=["C3-ENDLOOK-NOPAUSE-HAIR"])
            b_3 = v2_edit(cp_ge, "nopause-gver", drop_last)
            B.chk("refused at V2 (PIN-45): the G-VER STOP at launch 7 whose end look, evaluated fresh at 6, fires, its "
                  "end_look pause removed -- 'a fired end look records no matching pause', release_full not called, "
                  "nothing written; unedited it is analyzed with the seat's adjudication (C3-GVER-ENDLOOK-PAUSE)",
                  v2_refused(b_3, MSG_B) and v_ge["adjudication"][0] == "ok",
                  (b_3[0][0], b_3[0][1][:60], b_3[1], b_3[2]), cover=["C3-ENDLOOK-NOPAUSE-GVER"])
            b_4 = v2_edit(cp_hl, "nopause-reuse", drop_last, pis_=True)
            B.chk("refused at V2 (PIN-45): the hair-trigger STOP on launch 40 whose end look is look 1 reused (fired), its "
                  "pause {look, 40} removed, offered with a PI-stop record bound to that copy -- 'a fired end look "
                  "records no matching pause' (the campaign's last pause must be {kind look, look 1, ...}, unadjudicated: "
                  "the hit pre-empted the cadence pause, raised at the STOP), release_full not called, nothing "
                  "written; unedited it is analyzed with both seat inputs (C3-HAIR-LOOK40-PAUSE)",
                  v2_refused(b_4, MSG_B)
                  and "(the campaign's last pause must be {'kind': 'look', 'look': 1, 'at_launches': 40" in b_4[0][1]
                  and v_hl["both"][0] == "ok", (b_4[0][0], b_4[0][1][:60], b_4[1], b_4[2]),
                  cover=["C3-ENDLOOK-NOPAUSE-REUSE"])
            el_bars = list(ck_el["campaign"]["pauses"][-1]["bars"])
            b_5 = v2_edit(cp_el, "pause-kind", lambda ck_: ck_["campaign"]["pauses"][-1].__setitem__("kind", "look"),
                          adj_pause={"kind": "look", "at_launches": el_n})
            B.chk("refused at V2 (PIN-45): the terminal campaign's end_look pause with its kind altered to 'look', offered "
                  "with an adjudication naming the altered pause (which PIN-9 alone would accept) -- 'a fired end look "
                  "records no matching pause', release_full not called, nothing written",
                  v2_refused(b_5, MSG_B), (b_5[0][0], b_5[0][1][:60], b_5[1], b_5[2]), cover=["C3-ENDLOOK-PAUSE-KIND"])
            b_6 = v2_edit(cp_el, "pause-count", lambda ck_: ck_["campaign"]["pauses"][-1].__setitem__("at_launches", el_n - 1),
                          adj_pause={"kind": "end_look", "at_launches": el_n - 1})
            B.chk("refused at V2 (PIN-45): the terminal campaign's end_look pause with its at_launches altered (-1; the end "
                  "look's own count untouched, so PIN-46 holds), offered with an adjudication naming the altered pause "
                  "-- 'a fired end look records no matching pause', release_full not called, nothing written",
                  v2_refused(b_6, MSG_B), (b_6[0][0], b_6[0][1][:60], b_6[1], b_6[2]), cover=["C3-ENDLOOK-PAUSE-COUNT"])
            b_6l = v2_edit(cp_el, "pause-not-last", lambda ck_: ck_["campaign"]["pauses"].append(
                {"at_launches": el_n, "kind": "schedule_exhausted", "arm": "A0",
                 "adjudication": "battery: a hand-appended ruled pause (synthetic)"}))
            B.chk("refused at V2 (PIN-45): the terminal campaign's fresh fired end look whose end_look pause is followed "
                  "by a hand-appended, adjudicated pause (so PIN-9 would ask for no adjudication) -- a fresh end look's "
                  "pause is the campaign's last: 'a fired end look records no matching pause', release_full not called, "
                  "nothing written", v2_refused(b_6l, MSG_B) and "the campaign's last pause must be" in b_6l[0][1],
                  (b_6l[0][0], b_6l[0][1][:60], b_6l[1], b_6l[2]), cover=["C3-ENDLOOK-PAUSE-NOT-LAST"])
            b_7 = {k_: v2_edit(cp_el, f"pause-bars-{k_}", lambda ck_, b_=b_: ck_["campaign"]["pauses"][-1].__setitem__(
                       "bars", b_), adj_pause=el_pz)
                   for k_, b_ in (("extra", el_bars + ["battery-extra-bar"]), ("empty", []))}
            B.chk("refused at V2 (PIN-45): the terminal campaign's end_look pause with its bars altered (one appended, "
                  "emptied; its end look fires one bar -- order: C3-ENDLOOK-PAUSE-BARS-ORDER), each offered with the "
                  "seat's adjudication -- 'a fired end look records no matching pause', release_full not called, "
                  "nothing written",
                  bool(el_bars) and all(v2_refused(r_, MSG_B) for r_ in b_7.values()),
                  ({k_: (r_[0][0], r_[1]) for k_, r_ in b_7.items()}, el_bars), cover=["C3-ENDLOOK-PAUSE-BARS"])
            b_8 = v2_edit(cp_el, "fired-cleared", lambda ck_: (ck_["campaign"]["end_look"].__setitem__("fired", False),
                                                               ck_["campaign"]["pauses"].pop()))

            def el_result_1(ck_):                # the end look's own fired result as 2 alone (a truthy non-bool)
                el_ = ck_["campaign"]["end_look"]
                el_["fired"] = False
                on_ = [r_ for r_ in el_["results"] if r_["fired"]]
                for r_ in el_["results"]:
                    r_["fired"] = False
                on_[0]["fired"] = 2
                ck_["campaign"]["pauses"].pop()
            b_8i = v2_edit(cp_el, "fired-result-int", el_result_1)

            def el_flag_2(ck_):                  # the end look's own `fired` as 2 alone (results cleared)
                el_ = ck_["campaign"]["end_look"]
                for r_ in el_["results"]:
                    r_["fired"] = False
                el_["fired"] = 2
                ck_["campaign"]["pauses"].pop()
            b_8f = v2_edit(cp_el, "fired-flag-int", el_flag_2)
            B.chk("refused at V2 (PIN-45): the terminal campaign's end look with `fired` cleared while its results stay "
                  "fired, its pause removed; with `fired` cleared and its one fired result's `fired` as 2 alone (a "
                  "truthy non-bool, read by truth value; the rest cleared), its pause removed; and with its own `fired` "
                  "as 2 alone (every result cleared), its pause removed -- each still a fired end look (the second's "
                  "bars its result's name): 'a fired end look records no matching pause', "
                  "release_full not called, nothing written",
                  v2_refused(b_8, MSG_B) and ck_el["campaign"]["end_look"]["fired"] is True
                  and any(r_["fired"] for r_ in ck_el["campaign"]["end_look"]["results"])
                  and len(el_bars) == 1 and v2_refused(b_8i, MSG_B) and f"'bars': {el_bars!r}" in b_8i[0][1]
                  and v2_refused(b_8f, MSG_B) and "'bars': []" in b_8f[0][1],
                  (b_8[0][0], b_8[0][1][:60], b_8[1], b_8[2], b_8i[0][0], b_8i[0][1][:60], b_8f[0][0],
                   b_8f[0][1][:60]),
                  cover=["C3-ENDLOOK-FIRED-CLEARED"])
            b_9 = {"terminal": v2_edit(cp_el, "order-terminal", drop_last, adj_pause=el_pz),
                   "hair-look40": v2_edit(cp_hl, "order-hair40", drop_last, adj_pause={"kind": "look", "at_launches": 40},
                                          pis_=True)}
            B.chk("refusal order (PIN-45 before PIN-9's branch): a removed pause offered with a supplied --adjudication "
                  "naming it (the terminal campaign; the hair-trigger STOP at 40 with its PI-stop record too) is refused "
                  "by PIN-45's own message, not accepted and not PIN-9's surplus refusal; release_full not called, "
                  "nothing written", all(v2_refused(r_, MSG_B) and "--adjudication given" not in r_[0][1]
                                         for r_ in b_9.values()),
                  {k_: (r_[0][0], r_[0][1][:40]) for k_, r_ in b_9.items()}, cover=["C3-ENDLOOK-ORDER"])
            # positive control: a terminal reuse (end_is_look 1 at 40) whose matching cadence pause is NOT the last --
            # built by the production writers, with only the committed A0s schedule shortened to its first 20 cells
            # so that it can exhaust: look 1 fires at 40 (PAUSE), the seat's adjudication resumes it, A0s (19 domain
            # of 20 launched, floor 20) exhausts its schedule at 40 (PAUSE), the PI's stop ends it (PI-STOP at 40)
            real_lc = stages.load_committed

            def short_a0s(unit_, wanted_, dir_):
                got_ = real_lc(unit_, wanted_, dir_)
                return {t_: ({**s_, "n": 20, "cells": s_["cells"][:20]} if t_ == "A0s" else s_) for t_, s_ in got_.items()}
            r_rn = C.root("reuse-not-last")
            rule_rn = lambda t, s, n, c: ("Config choice one." if (t == "A0s" and s == 0 and n == 1)    # noqa: E731
                                          else "Config choice one." if (t == "A0s" and n == 6) else None)
            fl_rn = {"A0": 20, "A0s": 20}
            st_rn = []
            with _bt_patched(stages, "load_committed", short_a0s):
                for kw_rn in ({}, {"resume": True, "adjudication": "battery: the seat resumes the paused look (synthetic)"},
                              {"resume": True, "pi_stop": "PI: stop at the exhausted schedule (battery)"}):
                    res_rn, _ = C.run("Q-F0", r_rn, C.adapter("Q-F0", {"A0": 20, "A0s": 20}, rule_rn), fl_rn, **kw_rn)
                    st_rn.append((res_rn or {}).get("status"))
            cp_rn = r_rn / "ckpt" / "Q-F0_campaign.json"
            ck_rn = json.loads(cp_rn.read_text())
            el_rn = ck_rn["campaign"]["end_look"] or {}
            pz_rn = ck_rn["campaign"]["pauses"]
            v_rn = V("Q-F0", cp_rn, "reuse-not-last")
            b_10 = v2_edit(cp_rn, "reuse-not-last-dropped", lambda ck_: ck_["campaign"]["pauses"].pop(0))
            B.chk("accepted (PIN-45's positive control): a terminal reuse whose matching cadence pause is not the last -- "
                  "production-written under a battery patch that shortens the committed A0s schedule to its first 20 "
                  "cells (PAUSE at look 1 fired at 40, resumed by the seat; PAUSE schedule_exhausted at 40; PI-STOP at "
                  "40, the end look look 1 reused, fired): pauses [look 1 at 40, schedule_exhausted at 40], both "
                  "adjudicated -> analyzed with no seat input; its cadence pause removed it is refused (PIN-45: some "
                  "pause must be {kind look, look 1, ...}, adjudicated)",
                  st_rn == ["PAUSE", "PAUSE", "PI-STOP"] and len(ck_rn["sessions"]) == 40
                  and el_rn.get("end_is_look") == 1 and el_rn.get("at_launches") == 40 and el_rn.get("fired") is True
                  and [(p_["kind"], p_["at_launches"]) for p_ in pz_rn] == [("look", 40), ("schedule_exhausted", 40)]
                  and pz_rn[0].get("look") == 1 and all(p_.get("adjudication") for p_ in pz_rn)
                  and pz_rn[0]["bars"] == [r_["name"] for r_ in el_rn.get("results", []) if r_["fired"]]
                  and (ck_rn["campaign"]["terminal"] or {}).get("status") == "PI-STOP" and v_rn[0] == "ok"
                  and v_rn[1] == "written" and v2_refused(b_10, MSG_B)
                  and "(some pause must be {'kind': 'look', 'look': 1, 'at_launches': 40" in b_10[0][1]
                  and ", adjudicated)" in b_10[0][1],
                  (st_rn, [p_.get("kind") for p_ in pz_rn], v_rn[0], b_10[0][0]), cover=["C3-ENDLOOK-REUSE-NOT-LAST"])
            # production-written ends the round-1 review built (its P1-P10; F5), each offered to VERDICTS as written
            # (the original bytes; the seat inputs its end needs bound to it): every one is accepted. prod_d is
            # (sessions, the looks' fired flags, the stop's bar, the terminal status, (end look's look, at_launches,
            # end_is_look, fired), [(pause kind, at_launches, adjudicated)])
            def prod_v(name, cp_, adj_pause=None, pis_=False):
                sha_ = _sha256_bytes(Path(cp_).read_bytes())
                kw_ = {}
                if adj_pause is not None:
                    kw_["adjudication"] = seat_variant(adj_doc0, f"adj-{name}", campaign_sha256=sha_, pause=adj_pause)
                if pis_:
                    kw_["pi_stop"] = seat_variant(pis_doc0, f"pis-{name}", campaign_sha256=sha_)
                return V("Q-F0", Path(cp_), name, **kw_)

            def prod_d(cp_):
                ck_ = json.loads(Path(cp_).read_text())
                el_ = ck_["campaign"]["end_look"] or {}
                return (len(ck_["sessions"]), [lk_["result"]["fired"] for lk_ in ck_["looks"]],
                        (ck_.get("stop") or {}).get("bar"), (ck_["campaign"]["terminal"] or {}).get("status"),
                        (el_.get("look"), el_.get("at_launches"), el_.get("end_is_look"), el_.get("fired")),
                        [(p_["kind"], p_["at_launches"], p_["adjudication"] is not None) for p_ in ck_["campaign"]["pauses"]])

            def prod_run(tag, counts, rule, floors, invocations):
                r_ = C.root(f"prod-{tag}")
                st_ = []
                for kw_, patch_ in invocations:
                    with (_bt_patched(*patch_) if patch_ else contextlib.nullcontext()):
                        s_, _ = C.run("Q-F0", r_, C.adapter("Q-F0", counts, rule), floors, **kw_)
                    st_.append((s_ or {}).get("status"))
                return r_ / "ckpt" / "Q-F0_campaign.json", st_
            rule_sd = lambda t, s, n, c: "Config choice one." if (t == "A0s" and n == 6) else None   # noqa: E731
            adj_p = {"resume": True, "adjudication": "battery: the seat resumes the paused look (synthetic)"}
            c20, c21, c22 = ({"A0": k_, "A0s": k_} for k_ in (20, 21, 22))
            prod = {"P1": prod_run("p1", c20, None, c20, [({}, None)]),
                    "P2": prod_run("p2", c20, rule_sd, c20, [({}, None), (adj_p, None)]),
                    "P3": prod_run("p3", c21, rule_sd, c21, [({}, None), ({"resume": True, "pi_stop": "PI: stop at the "
                                                                           "fired look (battery)"}, None)]),
                    "P4": prod_run("p4", c21, rule_sd, c21, [({}, None), (adj_p, (stages, "run_session_qwen",
                                                                                  tamper_at("A0", 20)))]),
                    "P5": prod_run("p5", c21, lambda t, s, n, c: "<|im_end|>" if (t == "A0s" and s == 19 and n == 7)
                                   else None, c21, [({}, None)]),
                    "P6": prod_run("p6", c21, rule_sd, c21, [({}, None), (adj_p, None)]),
                    "P7": prod_run("p7", c22, lambda t, s, n, c: ("<|im_end|>" if (t == "A0" and s == 20 and n == 7)
                                                                 else rule_sd(t, s, n, c)), c22, [({}, None), (adj_p, None)]),
                    "P8": prod_run("p8", c22, rule_sd, c22, [({}, None), (adj_p, (stages, "run_session_qwen",
                                                                                  tamper_at("A0s", 20)))])}

            def short2(unit_, wanted_, dir_):
                got_ = real_lc(unit_, wanted_, dir_)
                return {t_: ({**s_, "n": 2, "cells": s_["cells"][:2]} if t_ == "A0s" else s_) for t_, s_ in got_.items()}
            rule9 = lambda t, s, n, c: ("Config choice one." if (n == 1 and ((t == "A0" and s < 3) or (t == "A0s" and s == 0)))  # noqa: E731
                                        else None)
            prod["P9"] = prod_run("p9", {"A0": 4, "A0s": 2}, rule9, {"A0": 1, "A0s": 2},
                                  [({}, (stages, "load_committed", short2)),
                                   ({"resume": True, "pi_stop": "PI: stop at the exhausted schedule (battery)"},
                                    (stages, "load_committed", short2))])
            with _bt_patched(resume, "hour_cap_exceeded", lambda ck__, cap__: len(ck__["sessions"]) >= 5):
                prod["P10"] = prod_run("p10", {"A0": 12, "A0s": 12}, lambda t, s, n, c: (
                    "Config choice one." if (t == "A0" and n == 1 and s < 3) else None), {"A0": 6, "A0s": 6}, [({}, None)])
            fz_ = lambda cp_: {"kind": prod_d(cp_)[5][-1][0], "at_launches": prod_d(cp_)[5][-1][1]}  # noqa: E731
            prod_want = {
                "P1": ("COMPLETE at 40, silent look 1 reused", ["COMPLETE"],
                       (40, [False], None, "COMPLETE", (1, 40, 1, False), []), {}),
                "P2": ("COMPLETE at 40, look 1 fired and ruled by the seat, reused", ["PAUSE", "COMPLETE"],
                       (40, [True], None, "COMPLETE", (1, 40, 1, True), [("look", 40, True)]), {}),
                "P3": ("PI-STOP of the fired look 1's pause at 40, reused", ["PAUSE", "PI-STOP"],
                       (40, [True], None, "PI-STOP", (1, 40, 1, True), [("look", 40, True)]), {}),
                "P4": ("G-VER STOP at launch 41 past a fired, ruled look 1, reused", ["PAUSE", "STOP"],
                       (40, [True], "template_breakage", None, (1, 40, 1, True), [("look", 40, True)]), {}),
                "P5": ("hair-trigger STOP at 40, silent look 1 reused", ["STOP"],
                       (40, [False], HAIR_BAR, None, (1, 40, 1, False), []), {"pis_": True}),
                "P6": ("COMPLETE at 42 past a ruled look 1, its fresh end look fired", ["PAUSE", "PAUSE"],
                       (42, [True], None, "COMPLETE", ("end", 42, None, True), [("look", 40, True), ("end_look", 42, False)]),
                       {"adj": True}),
                "P7": ("hair-trigger STOP at 41 past a ruled look 1, its fresh end look fired", ["PAUSE", "STOP"],
                       (41, [True], HAIR_BAR, None, ("end", 41, None, True), [("look", 40, True), ("end_look", 41, False)]),
                       {"adj": True, "pis_": True}),
                "P8": ("G-VER STOP at launch 42 (41 recorded) past a ruled look 1, its fresh end look fired",
                       ["PAUSE", "STOP"], (41, [True], "template_breakage", None, ("end", 41, None, True),
                                           [("look", 40, True), ("end_look", 41, False)]), {"adj": True}),
                "P9": ("PI-STOP of an exhausted schedule at 5 (A0s cut to 2 cells by a battery patch), its fresh end "
                       "look fired", ["PAUSE", "PAUSE"], (5, [], None, "PI-STOP", ("end", 5, None, True),
                                                          [("schedule_exhausted", 5, True), ("end_look", 5, False)]),
                       {"adj": True}),
                "P10": ("CAP at 5 (the hour cap patched to bind at 5 launches), its fresh end look fired", ["PAUSE"],
                        (5, [], None, "CAP", ("end", 5, None, True), [("end_look", 5, False)]), {"adj": True})}
            for k_, (what_, st_w, d_w, kw_w) in prod_want.items():
                cp_k, st_k = prod[k_]
                v_k = prod_v(f"prod-{k_}", cp_k, adj_pause=fz_(cp_k) if kw_w.get("adj") else None,
                             pis_=kw_w.get("pis_", False))
                v_k0 = prod_v(f"prod-{k_}-noadj", cp_k, pis_=kw_w.get("pis_", False)) if kw_w.get("adj") else None
                B.chk(f"accepted (PIN-45, PIN-46; no false refusal): {k_}, {what_} -- production-written, offered as "
                      f"written" + (" with the seat's adjudication bound to it (without it PIN-9 asks for it)"
                                    if kw_w.get("adj") else "") + (" and a PI-stop record" if kw_w.get("pis_") else "")
                      + " -> analyzed and written",
                      st_k == st_w and prod_d(cp_k) == d_w and v_k[0] == "ok" and v_k[1] == "written"
                      and (v_k0 is None or (v_k0[0] == "refused" and "last pause is unadjudicated" in v_k0[1])),
                      (st_k, prod_d(cp_k), v_k[0], v_k[1][:60]), cover=[f"C3-PROD-END-{k_}"])
            # hand edits of production-written checkpoints, each conjunct of PIN-45 / PIN-46 alone (the round-1
            # reviews' h1-h14 and the battery lens's cases): each its refusal's own message, release_full not
            # called, nothing written
            def set_last(k__, v__):
                return lambda ck_: ck_["campaign"]["pauses"][-1].__setitem__(k__, v__)
            hl_pz = {"kind": "look", "at_launches": 40}
            h_adj = {"terminal": v2_edit(cp_el, "adj-filled-terminal", set_last("adjudication", "hand: filled in (battery)")),
                     "hair-40-reuse": v2_edit(cp_hl, "adj-filled-hair40", set_last("adjudication", "hand: filled in (battery)"),
                                              pis_=True),
                     "hair-6-fresh": v2_edit(cp_hf, "adj-filled-hair6", set_last("adjudication", "hand: filled in (battery)"),
                                             pis_=True)}
            B.chk("refused at V2 (PIN-45): a pause raised at the end with its adjudication filled in by hand -- the terminal "
                  "campaign's end_look pause (no seat input offered), the hair STOP at 40's look pause and the hair STOP "
                  "at 6's end_look pause (each with a PI-stop record): stages never adjudicates an ended campaign's "
                  "pause, so PIN-9 would ask for nothing -- 'the campaign's last pause must be {...}, unadjudicated', "
                  "release_full not called, nothing written",
                  all(v2_refused(r_, MSG_B) and "(the campaign's last pause must be {" in r_[0][1]
                      and ", unadjudicated)" in r_[0][1] for r_ in h_adj.values()),
                  {k_: (r_[0][0], r_[0][1][:50]) for k_, r_ in h_adj.items()}, cover=["C3-ENDLOOK-PAUSE-ADJ-FILLED"])
            cp_p2 = prod["P2"][0]

            def unrule_append(ck_):
                ck_["campaign"]["pauses"][-1]["adjudication"] = None
                ck_["campaign"]["pauses"].append({"at_launches": 40, "kind": "schedule_exhausted", "arm": "A0s",
                                                  "adjudication": "hand: a ruled pause appended (battery)"})
            h_app = {"hair-40": v2_edit(cp_hl, "appended-hair40", lambda ck_: ck_["campaign"]["pauses"].append(
                         {"at_launches": 40, "kind": "schedule_exhausted", "arm": "A0s",
                          "adjudication": "hand: a ruled pause appended (battery)"}), pis_=True),
                     "terminal-40": v2_edit(cp_p2, "appended-p2", unrule_append)}
            B.chk("refused at V2 (PIN-45): a reused look's pause followed by a hand-appended, adjudicated pause (so PIN-9 "
                  "would ask for nothing) -- at the hair STOP at 40 (the look pause is the end's: 'the campaign's last "
                  "pause must be {...}, unadjudicated') and on P2's COMPLETE at 40 with its ruled look pause un-ruled "
                  "('some pause must be {...}, adjudicated'); release_full not called, nothing written",
                  v2_refused(h_app["hair-40"], MSG_B) and "(the campaign's last pause must be {'kind': 'look'" in h_app[
                      "hair-40"][0][1] and v2_refused(h_app["terminal-40"], MSG_B)
                  and "(some pause must be {'kind': 'look', 'look': 1, 'at_launches': 40" in h_app["terminal-40"][0][1]
                  and ", adjudicated)" in h_app["terminal-40"][0][1],
                  {k_: (r_[0][0], r_[0][1][:60]) for k_, r_ in h_app.items()}, cover=["C3-ENDLOOK-REUSE-APPENDED"])

            def clear_el(ck_):
                el_ = ck_["campaign"]["end_look"]
                el_["fired"] = False
                for r_ in el_["results"]:
                    r_["fired"] = False
                ck_["campaign"]["pauses"].pop()
            h_5 = v2_edit(cp_hl, "reuse-flags-cleared", clear_el, pis_=True)
            B.chk("refused at V2 (PIN-45): the hair STOP at 40's reused end look with `fired` and every result's cleared, "
                  "its pause removed -- look 1 as ck.looks records it is still fired, so it is a fired end look (bars "
                  "[]): 'a fired end look records no matching pause', release_full not called, nothing written",
                  v2_refused(h_5, MSG_B) and "'bars': []" in h_5[0][1] and ck_hl["looks"][0]["result"]["fired"] is True,
                  (h_5[0][0], h_5[0][1][:60], h_5[1], h_5[2]), cover=["C3-ENDLOOK-REUSE-FIRED-LOOK"])

            def clear_results(ck_):
                for r_ in ck_["campaign"]["end_look"]["results"]:
                    r_["fired"] = False
                ck_["campaign"]["pauses"].pop()
            h_6 = v2_edit(cp_el, "fired-flag-only", clear_results)
            B.chk("refused at V2 (PIN-45): the terminal end look with `fired` true but every result's cleared, its pause "
                  "removed -- still a fired end look (bars []): 'a fired end look records no matching pause', "
                  "release_full not called, nothing written",
                  v2_refused(h_6, MSG_B) and "'bars': []" in h_6[0][1], (h_6[0][0], h_6[0][1][:60], h_6[1], h_6[2]),
                  cover=["C3-ENDLOOK-FIRED-FLAG-ONLY"])
            h_7 = {"fresh": v2_edit(cp_el, "pause-look-fresh", set_last("look", 1), adj_pause=el_pz),
                   "reuse": v2_edit(cp_hl, "pause-look-reuse", set_last("look", 2), adj_pause=hl_pz, pis_=True)}
            B.chk("refused at V2 (PIN-45): the matching pause's look altered (the terminal end_look pause 'end' -> 1; the "
                  "hair STOP at 40's look pause 1 -> 2), each with the seat inputs naming the altered pause (PIN-9 "
                  "compares kind and at_launches only) -- 'a fired end look records no matching pause', release_full "
                  "not called, nothing written", all(v2_refused(r_, MSG_B) for r_ in h_7.values()),
                  {k_: (r_[0][0], r_[0][1][:40]) for k_, r_ in h_7.items()}, cover=["C3-ENDLOOK-PAUSE-LOOK"])
            h_8 = {"count-float": v2_edit(cp_el, "pause-count-float", set_last("at_launches", float(el_n)), adj_pause=el_pz),
                   "look-float": v2_edit(cp_hl, "pause-look-float", set_last("look", 1.0), adj_pause=hl_pz, pis_=True),
                   "look-bool": v2_edit(cp_hl, "pause-look-bool", set_last("look", True), adj_pause=hl_pz, pis_=True)}
            B.chk("refused at V2 (PIN-45, compared by value and exact type): the end_look pause's at_launches as the float "
                  "n.0 (equal by ==, which PIN-9's comparison accepts) and the hair STOP at 40's look pause's look as "
                  "1.0 or as the bool True (== 1, an int subclass; each with both seat inputs) -- 'a fired end look "
                  "records no matching pause', release_full not called, nothing written",
                  all(v2_refused(r_, MSG_B) for r_ in h_8.values()),
                  {k_: (r_[0][0], r_[0][1][:40]) for k_, r_ in h_8.items()}, cover=["C3-ENDLOOK-PAUSE-TYPE"])
            h_9 = {"count": v2_edit(cp_hl, "reuse-pause-count", set_last("at_launches", 39),
                                    adj_pause={"kind": "look", "at_launches": 39}, pis_=True),
                   "bars": v2_edit(cp_hl, "reuse-pause-bars", lambda ck_: ck_["campaign"]["pauses"][-1]["bars"].append(
                       "battery-extra-bar"), adj_pause=hl_pz, pis_=True)}
            B.chk("refused at V2 (PIN-45): the reused look's pause (the hair STOP at 40) with its at_launches altered "
                  "(39) or a bar appended, each with the seat inputs naming the pause -- 'a fired end look records no "
                  "matching pause', release_full not called, nothing written",
                  all(v2_refused(r_, MSG_B) for r_ in h_9.values()),
                  {k_: (r_[0][0], r_[0][1][:40]) for k_, r_ in h_9.items()}, cover=["C3-ENDLOOK-REUSE-PAUSE-ALTERED"])
            ge_bars = list(ck_ge["campaign"]["pauses"][-1]["bars"])
            h_11 = v2_edit(cp_ge, "bars-reversed", set_last("bars", ge_bars[::-1]),
                           adj_pause={"kind": "end_look", "at_launches": ck_ge["campaign"]["pauses"][-1]["at_launches"]})
            B.chk("refused at V2 (PIN-45, bars in results order): the G-VER STOP at 7's end_look pause (two fired bars) "
                  "naming its bars in reverse order, with the seat's adjudication naming the pause -- 'a fired end look "
                  "records no matching pause', release_full not called, nothing written; in results order (unedited) it "
                  "is analyzed with that adjudication",
                  len(ge_bars) == 2 and v2_refused(h_11, MSG_B) and v_ge["adjudication"][0] == "ok",
                  (ge_bars, h_11[0][0], h_11[0][1][:40]), cover=["C3-ENDLOOK-PAUSE-BARS-ORDER"])
            ck_c0 = json.loads(Path(res_c["checkpoint"]).read_text())
            h_12 = v2_edit(Path(res_c["checkpoint"]), "count-bool", lambda ck_: ck_["campaign"]["end_look"].__setitem__(
                "at_launches", True))
            B.chk("refused at V2 (PIN-46, an int by exact type): the CAP campaign with one launch recorded (its end look "
                  "at 1) with at_launches the bool True (== 1, an int subclass) -- 'the end look's launch count (True) "
                  "is not the launches recorded (1)', release_full not called, nothing written; unedited it is analyzed",
                  len(ck_c0["sessions"]) == 1 and (ck_c0["campaign"].get("end_look") or {}).get("at_launches") == 1
                  and v2_refused(h_12, MSG_C) and "(True) is not the launches recorded (1)" in h_12[0][1] and vc[0] == "ok",
                  (len(ck_c0["sessions"]), h_12[0][0], h_12[0][1][:60]), cover=["C3-ENDLOOK-COUNT-BOOL"])

            def look_k2(ck_):
                ck_["campaign"]["end_look"]["look"] = 2
                ck_["campaign"]["pauses"][-1]["look"] = 2
            h_13 = {"end_is_look": v2_edit(cp_hl, "reuse-k-edited", lambda ck_: ck_["campaign"]["end_look"].__setitem__(
                        "end_is_look", 2), adj_pause=hl_pz, pis_=True),
                    "look": v2_edit(cp_hl, "reuse-look-edited", look_k2, adj_pause=hl_pz, pis_=True)}
            B.chk("refused at V2: the hair STOP at 40's reused end look with end_is_look edited 1 -> 2 alone -- by PIN-46 "
                  "('the end look's launch count (40) is not that of the look it reuses (look 2, recorded at [])': no "
                  "look 2 is recorded); with its result's look and its pause's look edited 1 -> 2 instead (end_is_look "
                  "kept) -- by PIN-45, whose wanted look is end_is_look's ('... must be {kind look, look 1, ...}'); "
                  "release_full not called, nothing written",
                  v2_refused(h_13["end_is_look"], MSG_C)
                  and "(40) is not that of the look it reuses (look 2, recorded at [])" in h_13["end_is_look"][0][1]
                  and v2_refused(h_13["look"], MSG_B) and "{'kind': 'look', 'look': 1, 'at_launches': 40" in h_13["look"][0][1],
                  {k_: (r_[0][0], r_[0][1][:60]) for k_, r_ in h_13.items()}, cover=["C3-ENDLOOK-REUSE-K"])
            h_c4 = {"stop": v2_edit(Path(res_g1["checkpoint"]), "count-missing-stop",
                                    lambda ck_: ck_["campaign"]["end_look"].pop("at_launches")),
                    "terminal": v2_edit(cp_el, "count-missing-terminal",
                                        lambda ck_: ck_["campaign"]["end_look"].pop("at_launches"), adj_pause=el_pz)}
            B.chk("refused at V2 (PIN-46): the end look's at_launches key deleted (the G-VER STOP at 5, its end look "
                  "unfired; the terminal campaign) -- 'the end look's launch count (None) is not the launches "
                  "recorded', release_full not called, nothing written",
                  all(v2_refused(r_, MSG_C) and "(None) is not the launches recorded" in r_[0][1] for r_ in h_c4.values()),
                  {k_: (r_[0][0], r_[0][1][:60]) for k_, r_ in h_c4.items()}, cover=["C3-ENDLOOK-COUNT-MISSING"])
            # round 3 (disp_r2): the end-raised rule by value and type (R2BC-2, L2-3), each disjunct of look k's firing
            # alone (R2BC-3, L2-2), the reused pause's str ruling (R2BC-4, L2-3), each exact-type and guard conjunct of
            # PIN-46's reuse clause (R2BC-5, L2-1), and the end's class at a STOP (R2BC-1)
            k_adj = {k_: v2_edit(cp_el, f"adj-notnone-{k_}", set_last("adjudication", v_))
                     for k_, v_ in (("empty", ""), ("false", False), ("int", 1))}
            B.chk("refused at V2 (PIN-45, an end-raised pause carries adjudication None exactly): the terminal end_look "
                  "pause with its adjudication '', false or 1 (none of them None, so PIN-9 would ask for nothing), no "
                  "seat input -- 'the campaign's last pause must be {...}, unadjudicated', release_full not called, "
                  "nothing written",
                  all(v2_refused(r_, MSG_B) and ", unadjudicated)" in r_[0][1] for r_ in k_adj.values()),
                  {k_: (r_[0][0], r_[0][1][:50]) for k_, r_ in k_adj.items()}, cover=["C3-ENDLOOK-PAUSE-ADJ-NOTNONE"])
            k_last = v2_edit(cp_el, "end-then-unruled", lambda ck_: ck_["campaign"]["pauses"].append(
                {"at_launches": el_n, "kind": "schedule_exhausted", "arm": "A0", "adjudication": None}),
                adj_pause={"kind": "schedule_exhausted", "at_launches": el_n})
            B.chk("refused at V2 (PIN-45, an end-raised pause is the LAST pause): the terminal end_look pause followed by "
                  "a hand-appended unruled pause, offered with an adjudication naming that pause (which PIN-9 alone would "
                  "accept) -- 'the campaign's last pause must be {...}, unadjudicated', release_full not called, nothing "
                  "written", v2_refused(k_last, MSG_B) and ", unadjudicated)" in k_last[0][1],
                  (k_last[0][0], k_last[0][1][:50], k_last[1], k_last[2]), cover=["C3-ENDLOOK-PAUSE-LAST-UNRULED"])

            def lk1_only(which_):
                def f_(ck_):
                    clear_el(ck_)
                    lr_ = ck_["looks"][0]["result"]
                    if which_ in ("flag", "flag-2"):
                        for r_ in lr_["results"]:
                            r_["fired"] = False
                        if which_ == "flag-2":
                            lr_["fired"] = 2
                    elif which_ == "result-2":
                        lr_["fired"] = False
                        on_ = [r_ for r_ in lr_["results"] if r_["fired"]]
                        for r_ in lr_["results"]:
                            r_["fired"] = False
                        on_[0]["fired"] = 2
                    else:
                        lr_["fired"] = False
                return f_
            k_lk = {w_: v2_edit(cp_hl, f"reuse-look1-{w_}-only", lk1_only(w_), pis_=True)
                    for w_ in ("flag", "results", "flag-2", "result-2")}
            B.chk("refused at V2 (PIN-45, each disjunct of look k's firing alone): the hair STOP at 40's reused end look "
                  "cleared and its pause removed, look 1 as ck.looks records it fired by its result's `fired` alone (its "
                  "results cleared), by its results alone (its `fired` cleared), by its result's `fired` as 2 alone "
                  "(a truthy non-bool, read by truth value; its results cleared), and by one of its results' `fired` "
                  "as 2 alone (its `fired` and the rest cleared), a PI-stop record offered -- still a "
                  "fired end look (bars []): 'the campaign's last pause must be {kind look, look 1, ...}', release_full "
                  "not called, nothing written",
                  all(v2_refused(r_, MSG_B) and "(the campaign's last pause must be {'kind': 'look', 'look': 1" in r_[0][1]
                      and "'bars': []" in r_[0][1] for r_ in k_lk.values())
                  and ck_hl["looks"][0]["result"]["fired"] is True
                  and any(r_["fired"] for r_ in ck_hl["looks"][0]["result"]["results"]),
                  {k_: (r_[0][0], r_[0][1][:50]) for k_, r_ in k_lk.items()},
                  cover=["C3-ENDLOOK-REUSE-FIRED-LOOK-DISJUNCTS"])
            k_rs = {k_: v2_edit(cp_p2, f"ruled-nonstr-{k_}", set_last("adjudication", v_))
                    for k_, v_ in (("true", True), ("int", 1))}
            k_rs0 = v2_edit(cp_p2, "ruled-empty-str", set_last("adjudication", ""))
            B.chk("PIN-45, a reused cadence pause is ruled by a str (the writer writes a stripped, non-empty text, "
                  "stages.py:2028-2030 and 2129; '' is accepted as a str, Code's reading): P2's ruled look pause with "
                  "its ruling replaced by true or 1 (not a str; PIN-9 reads any non-None as adjudicated) is refused at "
                  "V2 -- 'some pause must be {...}, adjudicated', release_full not called, nothing written; with its "
                  "ruling '' it is analyzed with no seat input (written)",
                  all(v2_refused(r_, MSG_B) and ", adjudicated)" in r_[0][1] for r_ in k_rs.values())
                  and k_rs0[0][0] == "ok" and k_rs0[0][1] == "written"
                  and k_rs0[2] == ["Q-F0_VERDICTS.json", "Q-F0_secondary.json"],
                  ({k_: (r_[0][0], r_[0][1][:50]) for k_, r_ in k_rs.items()}, k_rs0[0][:2]),
                  cover=["C3-ENDLOOK-REUSE-ADJ-NONSTR"])

            def k_float_both(ck_):
                ck_["campaign"]["end_look"]["end_is_look"] = 1.0
                ck_["campaign"]["pauses"][-1]["look"] = 1.0
            k_kt = {"end_is_look": v2_edit(cp_hl, "reuse-k-float", lambda ck_: ck_["campaign"]["end_look"].__setitem__(
                        "end_is_look", 1.0), adj_pause=hl_pz, pis_=True),
                    "both": v2_edit(cp_hl, "reuse-k-float-both", k_float_both, adj_pause=hl_pz, pis_=True),
                    "look-at": v2_edit(cp_hl, "reuse-look-at-float", lambda ck_: ck_["looks"][0].__setitem__(
                        "at_launches", 40.0), adj_pause=hl_pz, pis_=True)}
            B.chk("refused at V2 (PIN-46's reuse clause by exact type, on a fired reuse): the hair STOP at 40's end_is_look "
                  "as 1.0 (alone, and with its pause's look 1.0 too) -- '(look 1.0, recorded at [])'; look 1's at_launches "
                  "in ck.looks as 40.0 (read_checkpoint compares by value) -- '(look 1, recorded at [40.0])'; each with "
                  "both seat inputs, release_full not called, nothing written",
                  v2_refused(k_kt["end_is_look"], MSG_C) and "(look 1.0, recorded at [])" in k_kt["end_is_look"][0][1]
                  and v2_refused(k_kt["both"], MSG_C) and "(look 1.0, recorded at [])" in k_kt["both"][0][1]
                  and v2_refused(k_kt["look-at"], MSG_C) and "(look 1, recorded at [40.0])" in k_kt["look-at"][0][1],
                  {k_: (r_[0][0], r_[0][1][:50]) for k_, r_ in k_kt.items()}, cover=["C3-ENDLOOK-REUSE-K-TYPE"])
            cp_p1 = prod["P1"][0]

            def el_set(k__, v__):
                return lambda ck_: ck_["campaign"]["end_look"].__setitem__(k__, v__)
            k_g = {"end_is_look 1.0": v2_edit(cp_p1, "silent-eil-float", el_set("end_is_look", 1.0)),
                   "end_is_look True": v2_edit(cp_p1, "silent-eil-bool", el_set("end_is_look", True)),
                   "end_is_look null": v2_edit(cp_p1, "silent-eil-null", el_set("end_is_look", None)),
                   "look 1 at 40.0": v2_edit(cp_p1, "silent-lk-float", lambda ck_: ck_["looks"][0].__setitem__(
                       "at_launches", 40.0)),
                   "look 1's result not an object": v2_edit(cp_p1, "silent-lk-res", lambda ck_: ck_["looks"][0].__setitem__(
                       "result", "x")),
                   "look 1's result look True": v2_edit(cp_p1, "silent-lk-look-bool",
                                                        lambda ck_: ck_["looks"][0]["result"].__setitem__("look", True))}
            k_gn = v2_edit(cp_el, "endlook-not-object", lambda ck_: ck_["campaign"].__setitem__("end_look", "x"))
            B.chk("refused at V2 (PIN-46's reuse clause, its types and guards, on a SILENT reuse, where PIN-45 cannot "
                  "stand in): P1's reused end look with end_is_look 1.0, True or null, with look 1 recorded at 40.0, "
                  "with look 1's result not an object, or with look 1's result's look the bool True (end_is_look 1 "
                  "kept) -- 'is not that of the look it reuses'; the terminal campaign's end "
                  "look not an object -- '(None) is not the launches recorded'; release_full not called, nothing written "
                  "(a refusal, never a crash)",
                  all(v2_refused(r_, MSG_C) and "is not that of the look it reuses" in r_[0][1] for r_ in k_g.values())
                  and v2_refused(k_gn, MSG_C) and "(None) is not the launches recorded" in k_gn[0][1],
                  ({k_: (r_[0][0], r_[0][1][:40]) for k_, r_ in k_g.items()}, k_gn[0][:2]),
                  cover=["C3-ENDLOOK-REUSE-GUARDS"])

            def stop_set(**kv_):
                return lambda ck_: ck_["stop"].update(kv_)

            def as_gver_ruled(bar_):
                def f_(ck_):
                    ck_["stop"]["bar"] = bar_
                    ck_["campaign"]["pauses"][-1]["adjudication"] = "hand: filled in (battery)"
                return f_

            def stop_on(i_):
                return lambda ck_: ck_["stop"].update(template=ck_["sessions"][i_]["template"], s=ck_["sessions"][i_]["s"])
            ge_pz = {"kind": "end_look", "at_launches": ck_ge["campaign"]["pauses"][-1]["at_launches"]}
            hf_pz = {"kind": "end_look", "at_launches": ck_hf["campaign"]["pauses"][-1]["at_launches"]}
            k_cg = {"hair 40 as template_breakage, ruled": v2_edit(cp_hl, "class-hl-tb", as_gver_ruled("template_breakage")),
                    "hair 40 as schedule_mismatch, ruled": v2_edit(cp_hl, "class-hl-sm", as_gver_ruled("schedule_mismatch")),
                    "hair 6 as template_breakage": v2_edit(cp_hf, "class-hf-tb", stop_set(bar="template_breakage"),
                                                           adj_pause=hf_pz),
                    "G-VER 7 on the last session's id": v2_edit(cp_ge, "class-ge-last", stop_on(-1), adj_pause=ge_pz),
                    "G-VER 7 on the first session's id": v2_edit(cp_ge, "class-ge-first", stop_on(0), adj_pause=ge_pz)}
            k_ch = {"G-VER 7 as the hair bar": v2_edit(cp_ge, "class-ge-hair", stop_set(bar=HAIR_BAR), adj_pause=ge_pz,
                                                       pis_=True),
                    "hair 40 on the first session's id": v2_edit(cp_hl, "class-hl-first", stop_on(0), adj_pause=hl_pz,
                                                                 pis_=True),
                    "hair 40 at s 18": v2_edit(cp_hl, "class-hl-s18", stop_set(s=18), adj_pause=hl_pz, pis_=True),
                    "hair 40 as template A0": v2_edit(cp_hl, "class-hl-a0", stop_set(template="A0"), adj_pause=hl_pz,
                                                      pis_=True)}
            id_ = lambda x_: (x_["template"], x_["s"])                                        # noqa: E731
            hl_ids = (id_(ck_hl["stop"]), id_(ck_hl["sessions"][-1]))
            ge_ids = (id_(ck_ge["sessions"][0]), id_(ck_ge["sessions"][-1]))
            k_cx = v2_edit(cp_hl, "class-hl-notobj", lambda ck_: ck_.__setitem__("stop", "x"), adj_pause=hl_pz)

            def hair_at_zero(ck_):                 # the G-VER STOP at launch 1 (no session) rewritten as a hair STOP
                ck_["stop"]["bar"] = HAIR_BAR      # with a fired fresh end look at 0 and its unadjudicated pause
                ck_["campaign"]["end_look"] = {"look": "end", "at_launches": 0, "fired": True,
                                               "results": [{"name": "battery-bar", "fired": True}]}
                ck_["campaign"]["pauses"].append({"at_launches": 0, "kind": "end_look", "look": "end",
                                                  "bars": ["battery-bar"], "adjudication": None})
            k_c0 = v2_edit(Path(res_g0["checkpoint"]), "class-hair-zero", hair_at_zero,
                           adj_pause={"kind": "end_look", "at_launches": 0}, pis_=True)
            B.chk("refused at V2 (PIN-45, the end's class at a STOP whose end look fires, checked by ids against the "
                  "writer's assertions in stages._stop_end_look): a hair-trigger STOP rewritten as G-VER (the hair STOP at "
                  "40 as template_breakage or schedule_mismatch, its reused look's pause given a ruling, no seat input; "
                  "the hair STOP at 6 as template_breakage, with the adjudication only) or a G-VER STOP's record id set "
                  "to the last session's or to the first session's (not the last) -- 'a G-VER STOP's quarantined record "
                  "(...) is among the sessions recorded'; a G-VER STOP rewritten as the hair trigger, or the hair STOP "
                  "at 40's id set to the first session's, to s 18 (its template kept) or to template A0 (its s kept), "
                  "the last two each sharing one component with the last session's id (each with both seat inputs) -- "
                  "'a hair-trigger STOP's "
                  "session (...) is not the last one recorded'; release_full "
                  "not called, nothing written; unedited they are analyzed (C3-HAIR-LOOK40-PAUSE, C3-HAIR-ENDLOOK-PAUSE, "
                  "C3-GVER-ENDLOOK-PAUSE); a stop block that is not an object (adjudication given) is refused as a STOP "
                  "neither G-VER nor a hair trigger, not a crash; the G-VER STOP at launch 1 (no session) rewritten as a "
                  "hair STOP with a fired end look at 0 and its pause (both seat inputs) -- '... is not the last one "
                  "recorded (the last: [])'",
                  all(v2_refused(r_, "REFUSED: a G-VER STOP's quarantined record (") for r_ in k_cg.values())
                  and all(v2_refused(r_, "REFUSED: a hair-trigger STOP's session (") for r_ in k_ch.values())
                  and v_hl["both"][0] == v_hf["both"][0] == v_ge["adjudication"][0] == "ok"
                  and k_cx[0][0] == "refused" and "is neither G-VER nor a hair trigger" in k_cx[0][1] and k_cx[1:] == (0, [])
                  and v2_refused(k_c0, "REFUSED: a hair-trigger STOP's session (") and "(the last: [])" in k_c0[0][1]
                  and hl_ids[0] == hl_ids[1] and hl_ids[0][0] != "A0" and hl_ids[0][1] != 18 and ge_ids[0] != ge_ids[1],
                  ({k_: (r_[0][0], r_[0][1][:50]) for k_, r_ in {**k_cg, **k_ch}.items()}, k_cx[0][:2], k_c0[0][:2],
                   hl_ids, ge_ids),
                  cover=["C3-ENDLOOK-STOP-CLASS"])
            adj_bad = {"sha": {"campaign_sha256": _sha256_bytes(cp.read_bytes())},
                       "pause": {"pause": {**adj_doc0["pause"], "at_launches": (adj_doc0["pause"]["at_launches"] or 0) + 1}},
                       "kind": {"pause": {**adj_doc0["pause"], "kind": "battery-other-kind"}},
                       "unit": {"unit": "OLMo-sft"}}
            adj_res = {k_: V("Q-F0", cp_el, f"adj-{k_}", adjudication=seat_variant(adj_doc0, f"adj-{k_}", **o_))
                       for k_, o_ in adj_bad.items()}
            B.chk("refused: an --adjudication naming another checkpoint's sha256, another pause (launch count or kind) "
                  "or another unit, each alone (the exact one is accepted)",
                  all(r_[0] == "refused" and "last pause is unadjudicated" in r_[1] for r_ in adj_res.values())
                  and ve2[0] == "ok", {k_: r_[0] for k_, r_ in adj_res.items()}, cover=["REF-ADJ-BINDING"])
            pis_bad = {"sha": {"campaign_sha256": _sha256_bytes(cp.read_bytes())}, "unit": {"unit": "OLMo-sft"},
                       "bar": {"bar": "template_breakage"}}
            pis_res = {k_: V("Q-F0", cp_h, f"pis-{k_}", pi_stop=seat_variant(pis_doc0, f"pis-{k_}", **o_))
                       for k_, o_ in pis_bad.items()}
            B.chk("refused: a --pi-stop record naming another checkpoint's sha256, another unit or another bar, each "
                  "alone (the exact one is accepted)", all(r_[0] == "refused" and "PI-stop record" in r_[1]
                                                           for r_ in pis_res.values()) and vh2[0] == "ok",
                  {k_: r_[0] for k_, r_ in pis_res.items()}, cover=["REF-PISTOP-BINDING"])
            # the seat inputs' own form (PIN-8, PIN-9): the declared schema and a non-empty text are required --
            # another document's schema, a missing schema, and a blank, empty, non-str or missing text each refuse
            # alone (the exact documents are accepted: C3-ENDLOOK-PAUSE, C3-HAIR-DISP)
            def seat_without(doc0, name, key):
                p = base / f"{name}.json"
                p.write_text(json.dumps({k_: v_ for k_, v_ in doc0.items() if k_ != key}))
                return p
            adj_sch = {"pi-stop's": V("Q-F0", cp_el, "adj-sch-pis", adjudication=seat_variant(
                           adj_doc0, "adj-sch-pis", schema=PI_STOP_SCHEMA)),
                       "excerpt's": V("Q-F0", cp_el, "adj-sch-excerpt", adjudication=seat_variant(
                           adj_doc0, "adj-sch-excerpt", schema=stages.ADJ_SCHEMA)),
                       "missing": V("Q-F0", cp_el, "adj-sch-missing", adjudication=seat_without(
                           adj_doc0, "adj-sch-missing", "schema"))}
            B.chk("refused: an --adjudication carrying another document's schema (the PI-stop record's; stages' "
                  "adjudication excerpt's) or none, each alone (the exact one is accepted)",
                  all(r_[0] == "refused" and "last pause is unadjudicated" in r_[1] for r_ in adj_sch.values())
                  and ve2[0] == "ok" and stages.ADJ_SCHEMA != ADJ_SCHEMA, {k_: r_[0] for k_, r_ in adj_sch.items()},
                  cover=["REF-ADJ-SCHEMA"])
            adj_txt = {k_: V("Q-F0", cp_el, f"adj-txt-{k_}", adjudication=(
                           seat_without(adj_doc0, f"adj-txt-{k_}", "text") if o_ is None
                           else seat_variant(adj_doc0, f"adj-txt-{k_}", text=o_[0])))
                       for k_, o_ in (("blank", (" \n\t ",)), ("empty", ("",)), ("null", (None,)), ("int", (7,)),
                                      ("missing", None))}
            B.chk("refused: an --adjudication whose text is blank, empty, null, not a str or missing, each alone (the "
                  "seat's ruling is its text; the exact one is accepted)",
                  all(r_[0] == "refused" and "last pause is unadjudicated" in r_[1] for r_ in adj_txt.values())
                  and ve2[0] == "ok", {k_: r_[0] for k_, r_ in adj_txt.items()}, cover=["REF-ADJ-TEXT"])
            pis_sch = {"adjudication's": V("Q-F0", cp_h, "pis-sch-adj", pi_stop=seat_variant(
                           pis_doc0, "pis-sch-adj", schema=ADJ_SCHEMA)),
                       "missing": V("Q-F0", cp_h, "pis-sch-missing", pi_stop=seat_without(
                           pis_doc0, "pis-sch-missing", "schema"))}
            B.chk("refused: a --pi-stop record carrying another document's schema (the adjudication's) or none, each "
                  "alone (the exact one is accepted)",
                  all(r_[0] == "refused" and "PI-stop record" in r_[1] for r_ in pis_sch.values()) and vh2[0] == "ok",
                  {k_: r_[0] for k_, r_ in pis_sch.items()}, cover=["REF-PISTOP-SCHEMA"])
            pis_txt = {k_: V("Q-F0", cp_h, f"pis-txt-{k_}", pi_stop=(
                           seat_without(pis_doc0, f"pis-txt-{k_}", "text") if o_ is None
                           else seat_variant(pis_doc0, f"pis-txt-{k_}", text=o_[0])))
                       for k_, o_ in (("blank", (" \n\t ",)), ("empty", ("",)), ("null", (None,)), ("int", (7,)),
                                      ("missing", None))}
            B.chk("refused: a --pi-stop record whose text is blank, empty, null, not a str or missing, each alone (the "
                  "PI's stop is its text; the exact one is accepted)",
                  all(r_[0] == "refused" and "PI-stop record" in r_[1] for r_ in pis_txt.values()) and vh2[0] == "ok",
                  {k_: r_[0] for k_, r_ in pis_txt.items()}, cover=["REF-PISTOP-TEXT"])
            ck_cp = json.loads(cp.read_text())
            v_sadj = V("Q-F0", cp, "surplus-adj", adjudication=adj)
            v_spis = V("Q-F0", cp, "surplus-pis", pi_stop=pis)
            B.chk("refused: a surplus --adjudication (no pause here; an adjudicated last pause: "
                  "REF-SURPLUS-ADJ-ADJUDICATED) and a surplus --pi-stop (COMPLETE here; CAP, PI-STOP, G-VER STOP: "
                  "REF-SURPLUS-PISTOP-TERMINAL) -- nothing undeclared enters the record (each is accepted where its "
                  "campaign needs it: C3-ENDLOOK-PAUSE, C3-HAIR-DISP)", ve2[0] == "ok" and vh2[0] == "ok" and not any(
                      p_.get("adjudication") is None for p_ in (ck_cp.get("campaign") or {}).get("pauses") or [])
                  and v_sadj[0] == "refused" and "--adjudication given" in v_sadj[1] and v_spis[0] == "refused"
                  and "--pi-stop given" in v_spis[1], (v_sadj[1][:50], v_spis[1][:50]), cover=["REF-SURPLUS-SEAT-INPUT"])
            # a last pause already adjudicated, as stages.py records it on a resume -- production-written: the
            # reuse-not-last campaign above, whose last pause (schedule_exhausted at 40) stages ruled by the PI's
            # stop (an end pause is never adjudicated in the checkpoint: PIN-45): analyzed with no --adjudication;
            # one given -- even naming that checkpoint and pause exactly -- is surplus and refused
            ck_ad = json.loads(cp_rn.read_text())
            cp_ad = cp_rn
            adj_ad = seat_variant(adj_doc0, "adj-ruled", campaign_sha256=_sha256_bytes(cp_ad.read_bytes()),
                                  pause={"kind": ck_ad["campaign"]["pauses"][-1]["kind"],
                                         "at_launches": ck_ad["campaign"]["pauses"][-1]["at_launches"]})
            v_ad0 = V("Q-F0", cp_ad, "ruled-none")
            v_ad1 = V("Q-F0", cp_ad, "ruled-surplus", adjudication=adj_ad)
            d_ad = json.loads((base / "out" / "ruled-none" / "Q-F0_VERDICTS.json").read_text()) if v_ad0[0] == "ok" else {}
            B.chk("a last pause already adjudicated (production-written under the battery patch that shortens the "
                  "committed A0s schedule to its first 20 cells -- the C3-ENDLOOK-REUSE-NOT-LAST campaign: its ruling "
                  "recorded with the pause by stages, the PI's stop of an exhausted schedule): analyzed with no "
                  "--adjudication (the pause recorded "
                  "adjudicated, no seat input recorded); an --adjudication naming that unit, checkpoint and pause "
                  "exactly is surplus and refused", bool(ck_ad["campaign"]["pauses"]) and v_ad0[0] == "ok"
                  and isinstance(ck_ad["campaign"]["pauses"][-1].get("adjudication"), str)
                  and [p_.get("adjudicated") for p_ in d_ad.get("pauses") or []][-1:] == [True]
                  and d_ad.get("adjudication") is None and v_ad1[0] == "refused" and "--adjudication given" in v_ad1[1],
                  (v_ad0[0], v_ad1[1][:50]), cover=["REF-SURPLUS-ADJ-ADJUDICATED"])
            # a surplus --pi-stop on every other terminal kind: CAP, PI-STOP and G-VER STOP (before and after a first
            # read); the same campaigns without it are analyzed (C3-CAP-ZERO, C3-PISTOP-ZERO, C3-GVER-ZERO, -DATA)
            spis = {"CAP": V("Q-F0", Path(res_c["checkpoint"]), "spis-cap", pi_stop=pis),
                    "PI-STOP": V("Q-F0", r_pi / "ckpt" / "Q-F0_campaign.json", "spis-pistop", pi_stop=pis),
                    "G-VER-0": V("Q-F0", Path(res_g0["checkpoint"]), "spis-gver0", pi_stop=pis),
                    "G-VER-1": V("Q-F0", Path(res_g1["checkpoint"]), "spis-gver1", pi_stop=pis)}
            B.chk("refused: a surplus --pi-stop on a CAP, a PI-STOP and a G-VER STOP campaign (no first read, and after "
                  "one), each -- no hair-trigger STOP to dispose; each is analyzed without it",
                  all(r_[0] == "refused" and "--pi-stop given" in r_[1] for r_ in spis.values())
                  and vc[0] == vpi[0] == vg0[0] == vg1[0] == "ok", {k_: r_[0] for k_, r_ in spis.items()},
                  cover=["REF-SURPLUS-PISTOP-TERMINAL"])
            # CAP with the sham the only domain arm: the contrast arm has no read
            r_cs = C.root("capsham")
            rule_cs = lambda t, s, n, c: ("Config choice one." if t == "A0" and n == 1 else None)

            def slow(t, s, n, c):
                if t == "A0s" and s == 0 and n == 1:
                    _time.sleep(0.4)
                return rule_cs(t, s, n, c)
            res_cs, _ = C.run("Q-F0", r_cs, C.adapter("Q-F0", {"A0": 2, "A0s": 2}, slow), {"A0": 2, "A0s": 2},
                              cap=0.25 / 3600)
            vcs = V("Q-F0", Path(res_cs["checkpoint"]), "capsham")
            dcs = json.loads((base / "out" / "capsham" / "Q-F0_VERDICTS.json").read_text()) if vcs[0] == "ok" else {}
            # the at-STOP label is the STOP's alone: at CAP the end look keeps its unchanged label (not 'at the STOP')
            n_cs = len(json.loads(Path(res_cs["checkpoint"]).read_text())["sessions"])
            gcs = dcs.get("guard_last_look") or {}
            B.chk("C3: CAP with the sham the only domain arm -> analyzed; the contrast arm INDETERMINATE, no read "
                  "obtained (contrast-empty); the guard names the end look 'the end look at N launches' (at_stop False: "
                  "a CAP is not a STOP) in the guard and the sentence",
                  res_cs["status"] == "CAP" and dcs.get("arm", {}).get("noread")
                  == "contrast-empty" and "no read obtained" in dcs.get("sentence", "")
                  and gcs.get("source") == "end_look" and gcs.get("at_stop") is False
                  and gcs.get("label") == f"the end look at {n_cs} launches"
                  and f"(the end look at {n_cs} launches)" in dcs.get("sentence", "") and "at the STOP" not in
                  dcs.get("sentence", ""), (res_cs["status"], dcs.get("arm", {}).get("noread"), gcs.get("label")),
                  cover=["C3-CAP-SHAM-ONLY"])
            # a PI-STOP after first reads (3 launches; the 4th interrupted, then the PI's stop): analyzed as obtained
            # (m:324); its end look keeps the unchanged label (at_stop False: a PI stop is not a STOP)
            r_pd = C.root("pistop-data")
            cut_pd = lambda t, s, n, c: t == "A0s" and s == 1 and n == 1                          # noqa: E731
            C.run("Q-F0", r_pd, C.adapter("Q-F0", {"A0": 2, "A0s": 2}, None, cut_pd), {"A0": 2, "A0s": 2})
            res_pd, _ = C.run("Q-F0", r_pd, C.adapter("Q-F0", {"A0": 2, "A0s": 2}), {"A0": 2, "A0s": 2},
                              resume=True, pi_stop="PI: stop after first reads (battery)")
            cp_pd = r_pd / "ckpt" / "Q-F0_campaign.json"
            ck_pd = json.loads(cp_pd.read_text()) if cp_pd.is_file() else {}
            n_pd = len(ck_pd.get("sessions") or [])
            v_pd = V("Q-F0", cp_pd, "pistop-data")
            d_pd = json.loads((base / "out" / "pistop-data" / "Q-F0_VERDICTS.json").read_text()) if v_pd[0] == "ok" else {}
            g_pd = d_pd.get("guard_last_look") or {}
            B.chk("C3: a PI-STOP after first reads -> analyzed as obtained; the guard names its end look 'the end look at "
                  "N launches' (at_stop False: a PI stop is not a STOP) in the guard and the sentence",
                  res_pd is not None and res_pd["status"] == "PI-STOP" and n_pd >= 2 and v_pd[0] == "ok"
                  and d_pd.get("arm", {}).get("state") in ARM_STATES
                  and g_pd.get("source") == "end_look" and g_pd.get("at_stop") is False
                  and g_pd.get("label") == f"the end look at {n_pd} launches"
                  and f"(the end look at {n_pd} launches)" in d_pd.get("sentence", "")
                  and "at the STOP" not in d_pd.get("sentence", ""),
                  ((res_pd or {}).get("status"), n_pd, v_pd[1][:40] if v_pd[0] != "ok" else g_pd.get("label")),
                  cover=["C3-PISTOP-DATA-LABEL"])
            # COMPLETE with an arm below floor; COMPLETE with an empty domain
            vbf = V("Q-F0", mutated("below-floor", lambda ck: ck["campaign"].__setitem__("floors", {"A0": 9, "A0s": 3})),
                    "below-floor")
            B.chk("STOP: COMPLETE with an arm below its floor", vbf[0] == "stop" and "below its floor" in vbf[1],
                  vbf[1][:60], cover=["C3-COMPLETE-BELOW-FLOOR"])
            ckc = json.loads(Path(res_c["checkpoint"]).read_text())
            ckc["campaign"]["terminal"]["status"] = "COMPLETE"
            ckc["campaign"]["floors"] = {"A0": 0, "A0s": 0}
            pce = r_cap / "ckpt" / "complete-empty.json"
            pce.write_text(json.dumps(ckc))
            vce = V("Q-F0", pce, "complete-empty")
            B.chk("STOP: COMPLETE with no domain session in either arm (the unit layer's bookkeeping STOP)",
                  vce[0] == "stop" and "no domain session in either arm" in vce[1], vce[1][:60],
                  cover=["C3-COMPLETE-EMPTY"])
            # OLMo: a COMPLETE stub campaign on a pod; the pod-less identity refused
            from valence_core.m import runner_olmo, testing
            kit = testing.olmo_kit()
            setup = runner_olmo.OLMoSetup(audit=kit["audit"], ban_ids=kit["ban_ids"], ban_strings=kit["ban_strings"],
                                          term_rx=kit["term_rx"], audit_sha16=runner_olmo.olmo_audit_sha16())
            r_o = C.root("olmo")
            OS = {"A0-OLMo-sft": 2, "A0s-OLMo-sft": 2}
            with _bt_patched(stages, "olmo_startup", lambda adapter, ckpt: setup), _bt_pod("pod-battery"):
                res_o, exc_o = C.run("OLMo-sft", r_o, C.adapter("OLMo-sft", OS), OS)
            t_o, q_o = _bt_olmo_gates(base, r_o)
            vo_ = V("OLMo-sft", Path(res_o["checkpoint"]), "olmo", time=t_o, qual=q_o)
            do = json.loads((base / "out" / "olmo" / "OLMo-sft_VERDICTS.json").read_text()) if vo_[0] == "ok" else {}
            ost = do.get("rows", {}).get("state")
            B.chk("reader: an OLMo COMPLETE stub campaign -> analyzed; its row state and row label only (no v1 "
                  "outputs), the label label_set's for that state; the absolute guard 'reported only'",
                  vo_[0] == "ok" and "v1_outputs" not in do and ost in ARM_STATES
                  and ost == (do.get("arm") or {}).get("state")
                  and do["rows"].get("olmo-sft") == label_set(("PASS", ost, "PASS", "PASS"), {})["olmo-sft"]
                  and "(reported only)" in do.get("sentence", ""),
                  (vo_[0], vo_[1][:60]), cover=["C3-OLMO-COMPLETE"])
            # record -> counts, independently of campaign_counts / prepick_counts: COMPLETE, CAP with the
            # sham the only domain arm, OLMo COMPLETE
            rc = [(_bt_recount(cp, "Q-F0"), doc), (_bt_recount(Path(res_cs["checkpoint"]), "Q-F0"), dcs),
                  (_bt_recount(Path(res_o["checkpoint"]), "OLMo-sft"), do)]
            rc_ok = [bool(d) and all(d["arm"]["stats"][k_] == want[k_] for k_ in ("n0", "k0", "n1", "k1", "mS", "j"))
                     and all(d["counts"][k_] == want[k_] for k_ in ("launched", "prepick", "domain")) for want, d in rc]
            B.chk("reader: the VERDICTS counts (n0, k0, n1, k1, mS, j; launched, pre-pick, domain per arm) equal an "
                  "independent recount from the checkpoint's raw sessions (the first pick coded from choices[0].pick "
                  "vs cell.P) -- COMPLETE, CAP sham-only, OLMo COMPLETE", all(rc_ok) and any(w["k0"] + w["k1"] for w, _ in rc),
                  rc_ok, cover=["C3-COUNTS-INDEPENDENT"])
            # m:324's exclusivity at write time (PIN-41)
            xv = base / "out" / "excl-v"
            xv.mkdir(parents=True)
            (xv / "Q-F0_NOT-RUN.json").write_text(json.dumps({"reason": "x", "cause": "clock:pi-declined"}))
            vxv = V("Q-F0", cp, "excl-v")
            xn = base / "out" / "excl-n"
            xn.mkdir(parents=True)
            (xn / "Q-F0_VERDICTS.json").write_text(json.dumps({"arm": {"state": "PASS"}}))
            vxn = V("Q-F0", Path(res_c["checkpoint"]), "excl-n")
            xr_rec = base / "excl-rec.json"
            xr_rec.write_text(json.dumps({"schema": NOT_RUN_RECORD_SCHEMA, "unit": "Q-F0", "cause": "clock:pi-declined",
                                          "also": [], "date": CLOCK_DATE, "detail": "battery",
                                          "decisions_with_other_outcomes_known": []}))
            nx_ok, nx_msg = _bt_raises(lambda: run_not_run("Q-F0", xr_rec, None, None, xn, _bt_env(base)), (AnlRefusal,))
            B.chk("exclusivity (m:324): verdicts refuses a VERDICTS beside an existing NOT-RUN and a no-first-read "
                  "NOT-RUN beside an existing VERDICTS; not-run refuses beside an existing VERDICTS (nothing written)",
                  vxv[0] == "refused" and "exclusive" in vxv[1] and not (xv / "Q-F0_VERDICTS.json").exists()
                  and vxn[0] == "refused" and "exclusive" in vxn[1] and not (xn / "Q-F0_NOT-RUN.json").exists()
                  and nx_ok and "exclusive" in nx_msg, (vxv[1][:50], vxn[1][:50]), cover=["CMD-EXCLUSIVE-WRITE"])
            cko = json.loads(Path(res_o["checkpoint"]).read_text())
            cko["identity"]["pod_id"] = None
            pno = r_o / "ckpt" / "no-pod.json"
            pno.write_text(json.dumps(cko))
            vnp = V("OLMo-sft", pno, "no-pod", time=t_o, qual=q_o)
            B.chk("refused: an OLMo campaign identity without its pod id", vnp[0] == "refused" and "pod" in vnp[1],
                  vnp[1][:60], cover=["REF-POD"])
            # the gate stages' own refusals at V2: not ended; another stage; another unit -- each a refusal,
            # decided before V4 reads a record (a not-ended stage with a defective record is still refused)
            time_ne = gate_variant(time_p, "time-not-ended", lambda ck: ck.__setitem__("stage_end", None))
            time_ne_bad = gate_variant(time_p, "time-not-ended-defect", lambda ck: (
                ck.__setitem__("stage_end", None), ck["sessions"][0].__setitem__("first_free_pick_P",
                                                                                 not ck["sessions"][0]["first_free_pick_P"])))
            g_res = {"not-ended": V("Q-F0", cp, "gate-not-ended", time=time_ne),
                     "not-ended+defect": V("Q-F0", cp, "gate-not-ended-defect", time=time_ne_bad),
                     "stage": V("Q-F0", cp, "gate-stage", time=qual_p),
                     "unit": V("Q-F0", cp, "gate-unit", time=t_o)}
            B.chk("refused: a time checkpoint not ended (also with a defective record), a qualification checkpoint "
                  "passed as the time stage, and another unit's time stage -- each a refusal, not a STOP (the ended "
                  "Q-F0/time and Q-F0/qual stages are accepted: C3-COMPLETE)", v[0] == "ok"
                  and all(r_[0] == "refused" and "is not an ended Q-F0/time gate stage" in r_[1] for r_ in g_res.values()),
                  {k_: r_[0] for k_, r_ in g_res.items()}, cover=["REF-GATE-NOT-ENDED", "REF-GATE-WRONG-STAGE"])
            # the decisions on the no-first-read NOT-RUN path of `verdicts`
            vcd = V("Q-F0", Path(res_c["checkpoint"]), "cap0-decisions", decisions=dec_ne)
            nrd_c = (json.loads((base / "out" / "cap0-decisions" / "Q-F0_NOT-RUN.json").read_text())
                     if vcd[0] == "ok" else {})
            B.chk("reader: `verdicts`' no-first-read {U}_NOT-RUN.json carries a non-empty decisions list verbatim, and "
                  "the analyzer's, package's and closure's sha256s", vcd[0] == "ok"
                  and nrd_c.get("decisions_with_other_outcomes_known") == dd_q and nrd_c.get("analyzer_sha256") == a_sha
                  and nrd_c.get("closure_sha256") == _BT_STATE["closure_sha256"]
                  and nrd_c.get("package_sha256") == _BT_STATE["package_sha256"], vcd[1][:50],
                  cover=["CMD-VERDICTS-NR-DECISIONS"])
        # canonical --out refused in the battery (resume.refuse_canonical_out)
        ok_c, msg = _bt_raises(lambda: resume.refuse_canonical_out(REPO / VERDICTS_REL), (SystemExit,))
        B.chk("refused: a canonical --out in the battery (data/m/verdicts)", ok_c and "SELFTEST REFUSED" in msg,
              cover=["REF-CANONICAL-OUT"])
        # the not-run and posting commands end to end
        nd = base / "nr"
        nd.mkdir()
        rec = {"schema": NOT_RUN_RECORD_SCHEMA, "unit": "Q-F0", "cause": "clock:pi-declined", "also": ["clock:k-zero"],
               "date": CLOCK_DATE, "detail": "battery", "decisions_with_other_outcomes_known": []}
        rp = nd / "rec.json"
        rp.write_text(json.dumps(rec))
        s1, l1, p1 = run_not_run("Q-F0", rp, time_p, qual_p, nd, _bt_env(base))
        nrd = json.loads(p1[0].read_text())
        s1b, _, _ = run_not_run("Q-F0", rp, time_p, qual_p, nd, _bt_env(base))
        B.chk("not-run: a Clock NOT-RUN record -> {U}_NOT-RUN.json with its reason, rows, the gate-stage release "
              "(contrast first picks by role) and the decisions; a re-run is identical",
              s1 == "written" and s1b == "identical" and nrd["reason"] == not_run_reason("Q-F0", "clock:pi-declined",
                                                                                      CLOCK_DATE)
              and nrd["gate_release"]["qual"]["contrast_first_picks"] and nrd["also"] == ["clock:k-zero"],
              nrd["reason"][:60], cover=["CMD-NOTRUN", "CNT-GATE-RELEASE"])
        rp2 = nd / "rec2.json"
        rp2.write_text(json.dumps({**rec, "cause": "no-first-read:cap"}))
        ok_r, msg_r = _bt_raises(lambda: run_not_run("Q-F0", rp2, None, None, nd, _bt_env(base)), (AnlRefusal,))
        B.chk("not-run: a no-first-read cause is refused (it comes from the campaign through `verdicts`)", ok_r,
              msg_r[:60], cover=["CMD-NOTRUN-NOFIRSTREAD-REFUSED"])

        def nr_try(name, time=None, qual=None, env=None, record=rp):
            d_ = base / "nr-cases" / name
            d_.mkdir(parents=True)
            try:
                st_, _, ps_ = run_not_run("Q-F0", record, time, qual, d_, env or _bt_env(base))
                return "ok", st_, json.loads(ps_[0].read_text())
            except AnlRefusal as e:
                return "refused", B.clean(str(e)), sorted(x.name for x in d_.iterdir())
            except AnlStop as e:
                return "stop", B.clean(str(e)), sorted(x.name for x in d_.iterdir())
            except Exception as e:                                    # noqa: BLE001 -- a crash fails its own check
                return "crash", B.clean(f"{type(e).__name__}: {e}"), sorted(x.name for x in d_.iterdir())
        # m:318's decisions, non-empty, carried verbatim into {U}_NOT-RUN.json
        rp_dd = nd / "rec-decisions.json"
        rp_dd.write_text(json.dumps({**rec, "decisions_with_other_outcomes_known": dd_q}))
        n_dd = nr_try("decisions", record=rp_dd)
        B.chk("not-run: a non-empty decisions list is carried verbatim into {U}_NOT-RUN.json (the empty one into the "
              "default run)", n_dd[0] == "ok" and n_dd[2].get("decisions_with_other_outcomes_known") == dd_q
              and nrd["decisions_with_other_outcomes_known"] == [], n_dd[1][:50], cover=["CMD-NOTRUN-DECISIONS"])
        # the gate stages' refusals, each decided before a record is released or read (exit 2, nothing written)
        n_g = {"not-ended": nr_try("g-not-ended", time=time_ne), "not-ended+defect": nr_try("g-ne-defect", time=time_ne_bad),
               "stage": nr_try("g-stage", time=qual_p), "unit": nr_try("g-unit", time=t_o)}
        B.chk("not-run refused: a time stage not ended (also with a defective record: refused, not a STOP), a "
              "qualification checkpoint passed as the time stage, another unit's time stage; nothing written (the "
              "ended Q-F0/time and Q-F0/qual stages are released: CMD-NOTRUN)", s1 == "written"
              and set(nrd["gate_release"] or {}) == {"time", "qual"}
              and all(r_[0] == "refused" and r_[2] == [] for r_ in n_g.values())
              and "has not ended" in n_g["not-ended"][1] and "has not ended" in n_g["not-ended+defect"][1]
              and "is not Q-F0/time" in n_g["stage"][1] and "is not Q-F0/time" in n_g["unit"][1],
              {k_: r_[0] for k_, r_ in n_g.items()}, cover=["NR-CMD-GATE-NOT-ENDED", "NR-CMD-GATE-WRONG-STAGE"])
        # PIN-38's order: a gate stage's end is decided before any gate record is released (V3) -- with a time
        # stage not ended (with or without a defective record) readrule.release_full is never called; ended time
        # and qual stages are each released (2 calls)
        nr_calls: list = []
        real_release_nr = readrule.release_full

        def counting_release_nr(recs):
            nr_calls.append(len(recs))
            return real_release_nr(recs)
        with _bt_patched(readrule, "release_full", counting_release_nr):
            n_ne_r = [nr_try("g-ne-release", time=time_ne), nr_try("g-ne-defect-release", time=time_ne_bad)]
            n_ne_calls = len(nr_calls)
            n_ok_r = nr_try("g-release-ok", time=time_p, qual=qual_p)
            n_ok_calls = len(nr_calls) - n_ne_calls
        B.chk("not-run: a time stage not ended (with or without a defective record) is refused before any gate record "
              "is released (readrule.release_full not called; nothing written); ended time and qual stages are both "
              "released (2 calls)", all(r_[0] == "refused" and "has not ended" in r_[1] and r_[2] == [] for r_ in n_ne_r)
              and n_ne_calls == 0 and n_ok_r[0] == "ok" and n_ok_calls == 2, (n_ne_calls, n_ok_r[0], n_ok_calls),
              cover=["NR-CMD-GATE-BEFORE-RELEASE"])
        # PIN-30 on `not-run`: a stub-written gate stage refused off the battery path; a stub-free one released
        n_s = nr_try("g-stub", time=time_p, env=_bt_env(base, allow_stub=False))
        n_ns = nr_try("g-no-stub", time=time_ns, env=_bt_env(base, allow_stub=False))
        B.chk("not-run (PIN-30): a stub-written time stage is refused off the battery path; a stub-free one is "
              "released", n_s[0] == "refused" and "the time checkpoint was written by the self-test stub" in n_s[1]
              and n_ns[0] == "ok" and (n_ns[2].get("gate_release") or {}).get("time") is not None,
              (n_s[1][:50], n_ns[0]), cover=["NR-CMD-STUB"])
        # PIN-42: `not-run` binds its output to a committed analyzer (and the posting, below)
        n_unc = nr_try("analyzer-uncommitted", env=_bt_env(base, committed=uncommitted(Path(__file__))))
        n_prop = nr_try("proposal", env=_bt_env(base, proposal_path=lock))
        B.chk("not-run (PIN-42): refused with the analyzer uncommitted or a proposal not the pinned v1.11 (nothing "
              "written); its output records the analyzer's, package's and closure's sha256s",
              n_unc[0] == "refused" and "analyzer is not committed" in n_unc[1] and n_unc[2] == []
              and n_prop[0] == "refused" and "proposal" in n_prop[1] and nrd.get("analyzer_sha256") == a_sha
              and nrd.get("package_sha256") == _BT_STATE["package_sha256"]
              and nrd.get("closure_sha256") == _BT_STATE["closure_sha256"], (n_unc[1][:50], n_prop[1][:40]),
              cover=["NR-CMD-BINDING"])
        # PIN-42's order: the binding is decided before any input is read -- with the analyzer uncommitted an
        # absent record, a record that is not an object and a not-ended time stage each refuse on the analyzer;
        # with it committed each refuses on its own input (so each would have refused had it been read first)
        unc_a = _bt_env(base, committed=uncommitted(Path(__file__)))
        rp_abs, rp_mal = nd / "absent-record.json", nd / "malformed-record.json"
        rp_mal.write_text("[]")
        b_first = {"absent": nr_try("bind-absent", record=rp_abs, env=unc_a),
                   "malformed": nr_try("bind-malformed", record=rp_mal, env=unc_a),
                   "gate": nr_try("bind-gate", time=time_ne, env=unc_a)}
        b_own = {"absent": nr_try("own-absent", record=rp_abs), "malformed": nr_try("own-malformed", record=rp_mal),
                 "gate": nr_try("own-gate", time=time_ne)}
        B.chk("not-run (PIN-42): the binding is decided before any input is read -- with the analyzer uncommitted, an "
              "absent record, a record that is not an object and a not-ended time stage each refuse on the analyzer "
              "(nothing written); with it committed each refuses on its own input",
              all(r_[0] == "refused" and "analyzer is not committed" in r_[1] and r_[2] == [] for r_ in b_first.values())
              and all(r_[0] == "refused" and "analyzer is not committed" not in r_[1] for r_ in b_own.values())
              and "the NOT-RUN record unreadable" in b_own["absent"][1] and "NOT-RUN record: " in b_own["malformed"][1]
              and "has not ended" in b_own["gate"][1], {k_: r_[1][:30] for k_, r_ in b_own.items()},
              cover=["NR-CMD-BINDING-FIRST"])
        B.chk("not-run: {U}_NOT-RUN.json records the pinned proposal's sha256 (the default and the decisions run; "
              "`verdicts`' no-first-read NOT-RUN too)", nrd.get("proposal_sha256") == PROPOSAL_SHA256
              and n_dd[2].get("proposal_sha256") == PROPOSAL_SHA256 and nrd_c.get("proposal_sha256") == PROPOSAL_SHA256,
              str(nrd.get("proposal_sha256"))[:16], cover=["NR-CMD-PROPOSAL-SHA"])
        pdir = base / "post"
        pdir.mkdir()
        (pdir / "Q-F0_NOT-RUN.json").write_text(json.dumps({"reason": nrd["reason"], "cause": "clock:pi-declined"}))
        (pdir / "OLMo-sft_VERDICTS.json").write_text(json.dumps({"arm": {"state": "PASS"}}))
        (pdir / "OLMo-dpo_NOT-RUN.json").write_text(json.dumps({"reason": "dose not completable",
                                                                "cause": "dose-not-completable"}))
        tp = pdir / "tuple.json"
        tdoc = {"schema": TUPLE_SCHEMA, "posting": "v1", "tuple": {"Q-F0": "NOT-RUN", "OLMo-sft": "PASS",
                                                                   "OLMo-dpo": "NOT-RUN", "OLMo-instruct": "PENDING"},
                "reasons": {"Q-F0": nrd["reason"], "OLMo-dpo": "dose not completable"},
                "pending": {"OLMo-instruct": {"substate": "locked-running", "clock_passed": False,
                                              "date": "2026-10-29"}}}
        tp.write_text(json.dumps(tdoc))
        env_p = _bt_env(base)
        sp_, lp_, pp_ = run_posting(tp, _BT_STATE["rec_table"], REPO / FLAG_SOURCE_REL, pdir, pdir, env_p)
        po = json.loads(pp_[0].read_text())
        pl_ = po["outputs"]["labels"]
        B.chk("posting: the v1 outputs under the declared tuple (Fallback-2; e2a and f1 'was not run: <Q-F0's "
              "reason>'; sft Answered; dpo 'was not run: dose not completable'; instruct pending), written as "
              "POSTING-v1_outputs.of-record.json", sp_ == "written" and po["outputs"]["ceiling"]["name"] == "Fallback-2"
              and pl_["e2a"] == pl_["f1"] == PFX_F0 + "was not run: " + nrd["reason"]
              and pl_["olmo-sft"] == "Answered" and pl_["olmo-dpo"] == PFX_O + "was not run: dose not completable"
              and pl_["olmo-instruct"] == PFX_O + "is pre-registered and pending at this posting"
              and pp_[0].name == "POSTING-v1_outputs.of-record.json", lp_[0][:70], cover=["CMD-POSTING"])
        B.chk("posting: the output records the tuple it used, its reasons and its PENDING declarations (the Clock "
              "comparison's date beside clock_passed, as given); Q-F0's VERDICTS records its declared OLMo states "
              "(the PENDING date included)", po.get("tuple") == tdoc["tuple"] and po.get("reasons") == tdoc["reasons"]
              and po.get("pending") == tdoc["pending"] and po["pending"]["OLMo-instruct"]["date"] == "2026-10-29"
              and doc.get("olmo_states_declared") == json.loads(Path(_BT_STATE["olmo_states"]).read_text())["states"]
              and doc["olmo_states_declared"]["OLMo-sft"]["date"] == CLOCK_DATE,
              (po.get("tuple"), (doc.get("olmo_states_declared") or {}).get("OLMo-sft")),
              cover=["CMD-POSTING-TUPLE", "PEND-DATE-RECORDED"])
        # PIN-42: the posting binds its output to a committed analyzer
        pb_d = base / "post-binding"
        pb_d.mkdir()
        p_unc = _bt_raises(lambda: run_posting(tp, _BT_STATE["rec_table"], REPO / FLAG_SOURCE_REL, pdir, pb_d,
                                               _bt_env(base, committed=uncommitted(Path(__file__)))), (AnlRefusal,))
        p_prop = _bt_raises(lambda: run_posting(tp, _BT_STATE["rec_table"], REPO / FLAG_SOURCE_REL, pdir, pb_d,
                                                _bt_env(base, proposal_path=lock)), (AnlRefusal,))
        B.chk("posting (PIN-42): refused with the analyzer uncommitted or a proposal not the pinned v1.11 (nothing "
              "written); its output records the analyzer's, package's and closure's sha256s",
              p_unc[0] and "analyzer is not committed" in p_unc[1] and p_prop[0] and "proposal" in p_prop[1]
              and list(pb_d.iterdir()) == [] and po.get("analyzer_sha256") == a_sha
              and po.get("package_sha256") == _BT_STATE["package_sha256"]
              and po.get("closure_sha256") == _BT_STATE["closure_sha256"], (p_unc[1][:50], p_prop[1][:40]),
              cover=["CMD-POSTING-BINDING"])
        # PIN-42's order on the posting: with the analyzer uncommitted an absent tuple, a tuple contradicting a
        # unit's VERDICTS and an absent sentence table each refuse on the analyzer; with it committed each refuses
        # on its own input
        pbf = base / "post-bind-first"
        pbf.mkdir()
        tp_abs, tp_x = pdir / "absent-tuple.json", pdir / "tuple-contradicts.json"
        tp_x.write_text(json.dumps({**tdoc, "tuple": {**tdoc["tuple"], "OLMo-sft": "DEAD"}}))
        unc_p = _bt_env(base, committed=uncommitted(Path(__file__)))
        pcases = {"absent-tuple": (tp_abs, _BT_STATE["rec_table"]), "contradicting": (tp_x, _BT_STATE["rec_table"]),
                  "absent-table": (tp, base / "absent-table.json")}
        pb_first = {k_: _bt_raises(lambda a=a, s=s: run_posting(a, s, REPO / FLAG_SOURCE_REL, pdir, pbf, unc_p),
                                   (AnlRefusal,)) for k_, (a, s) in pcases.items()}
        pb_own = {k_: _bt_raises(lambda a=a, s=s: run_posting(a, s, REPO / FLAG_SOURCE_REL, pdir, pbf, env_p),
                                 (AnlRefusal,)) for k_, (a, s) in pcases.items()}
        B.chk("posting (PIN-42): the binding is decided before any input is read -- with the analyzer uncommitted, an "
              "absent tuple, a tuple contradicting a unit's VERDICTS and an absent sentence table each refuse on the "
              "analyzer (nothing written); with it committed each refuses on its own input",
              all(r_[0] and "analyzer is not committed" in r_[1] for r_ in pb_first.values())
              and all(r_[0] and "analyzer is not committed" not in r_[1] for r_ in pb_own.values())
              and "the tuple unreadable" in pb_own["absent-tuple"][1] and "its VERDICTS says" in pb_own["contradicting"][1]
              and "sentence table is not committed" in pb_own["absent-table"][1] and list(pbf.iterdir()) == [],
              {k_: B.clean(r_[1])[:30] for k_, r_ in pb_own.items()}, cover=["CMD-POSTING-BINDING-FIRST"])
        tdoc2 = copy.deepcopy(tdoc)
        tdoc2["tuple"]["OLMo-sft"] = "DEAD"
        tp.write_text(json.dumps(tdoc2))
        ok_x, msg_x = _bt_raises(lambda: run_posting(tp, _BT_STATE["rec_table"], REPO / FLAG_SOURCE_REL, pdir, pdir,
                                                     env_p), (AnlRefusal,))
        tdoc3 = copy.deepcopy(tdoc)
        tdoc3["tuple"]["OLMo-instruct"] = "PENDING"
        (pdir / "OLMo-instruct_VERDICTS.json").write_text(json.dumps({"arm": {"state": "DEAD"}}))
        tp.write_text(json.dumps(tdoc3))
        ok_y, _ = _bt_raises(lambda: run_posting(tp, _BT_STATE["rec_table"], REPO / FLAG_SOURCE_REL, pdir, pdir,
                                                 env_p), (AnlRefusal,))
        (pdir / "OLMo-instruct_VERDICTS.json").unlink()
        tdoc4 = copy.deepcopy(tdoc)
        tdoc4["tuple"]["OLMo-instruct"] = "DEAD"
        tdoc4["pending"] = {}
        tp.write_text(json.dumps(tdoc4))
        (pdir / "OLMo-instruct_VERDICTS.json").write_text(json.dumps({"arm": {"state": "DEAD"}}))
        z = pdir / "z"
        z.mkdir()
        st4, _, _ = run_posting(tp, _BT_STATE["rec_table"], REPO / FLAG_SOURCE_REL, pdir, z, env_p)
        B.chk("posting: each coordinate is cross-checked against the unit's VERDICTS / NOT-RUN output (a tuple "
              "contradicting a VERDICTS is refused; PENDING beside an existing VERDICTS is refused; a VERDICTS "
              "file carries its verdict)", ok_x and ok_y and st4 == "written", msg_x[:60],
              cover=["CMD-POSTING-CROSSCHECK", "PEND-VERDICTS-CARRIES"])
        # the re-run on the posted text (m:278, m:73) writes its own record beside the table of record's -- under
        # C7's bar (PIN-44): a posted copy of the table of record enumerates rows, so it FAILs and writes nothing;
        # a posted text that enumerates nothing PASSes and writes its record
        tp.write_text(json.dumps(tdoc4))
        posted = base / "table-posted.json"
        pt = json.loads(Path(_BT_STATE["rec_table"]).read_text(encoding="utf-8"))
        pt["kind"] = "posted"
        posted.write_text(resume.json_text(pt, indent=1), encoding="utf-8")
        posted_min = _bt_posted_min(base, "min", dose=True)
        rw_d = base / "rewrites"
        rw_d.mkdir()

        def rw_file(name, ids_, **over):
            p_ = rw_d / f"{name}.json"
            p_.write_text(json.dumps({"schema": REWRITES_SCHEMA, "posting": "v1", "rows": list(ids_), **over}))
            return p_
        rw_none = rw_file("none", [])
        bk = base / "post-kinds"
        bk.mkdir()
        s_r1, _, p_r1 = run_posting(tp, _BT_STATE["rec_table"], REPO / FLAG_SOURCE_REL, pdir, bk, env_p)
        en_r1 = [it["row_id"] for it in json.loads(p_r1[0].read_text())["outputs"]["enumeration"]]
        rw_bk = rw_file("post-kinds", en_r1)
        f_bk = _bt_raises(lambda: run_posting(tp, posted, REPO / FLAG_SOURCE_REL, pdir, bk, env_p, rewrites=rw_none),
                          (AnlPostingFail,))
        ls_bk = sorted(x.name for x in bk.iterdir())
        s_r2, _, p_r2 = run_posting(tp, _BT_STATE["rec_table"], REPO / FLAG_SOURCE_REL, pdir, bk, env_p)
        s_p, _, p_p = run_posting(tp, posted_min, REPO / FLAG_SOURCE_REL, pdir, bk, env_p, rewrites=rw_bk)
        d_p = json.loads(p_p[0].read_text())
        B.chk("posting: the table of record's run and the posted text's re-run write two records in one directory -- "
              "POSTING-v1_outputs.of-record.json; a posted copy of the table of record (it enumerates rows) FAILs "
              "C7's bar and writes nothing (PIN-44); the of-record run again is identical; a posted text that "
              "enumerates nothing, its rewrite list naming every row the of-record run enumerated, PASSes and "
              "writes .posted.json beside it (compared with the posting's own of-record enumeration: Q-F0 is NOT-RUN)",
              s_r1 == "written" and bool(en_r1) and f_bk[0] and ls_bk == ["POSTING-v1_outputs.of-record.json"]
              and s_r2 == "identical" and p_r2[0] == p_r1[0] and s_p == "written"
              and (p_r1[0].name, p_p[0].name) == ("POSTING-v1_outputs.of-record.json", "POSTING-v1_outputs.posted.json")
              and d_p["table_kind"] == "posted" and d_p["bar"]["verdict"] == "PASS"
              and d_p["bar"]["comparison"]["comparator"]["kind"] == "posting-of-record"
              and d_p["bar"]["comparison"]["comparator"]["path"] == _repo_rel(p_r1[0])
              and d_p["bar"]["comparison"]["comparator"]["sha256"] == _sha256_bytes(p_r1[0].read_bytes())
              and d_p["bar"]["comparison"]["comparator"]["tuple"] == json.loads(p_r1[0].read_text())["tuple"]
              and d_p["bar"]["comparison"]["same_tuple"] is True
              and d_p["bar"]["comparison"]["differs"] is False,
              (s_r1, f_bk[0], s_r2, s_p, len(en_r1)), cover=["CMD-POSTING-BOTH-KINDS"])
        p_docs = [po, json.loads(p_r1[0].read_text()), json.loads(p_p[0].read_text())]
        B.chk("posting: POSTING-v1_outputs.*.json records the pinned proposal's sha256 (the table of record's runs and "
              "the posted text's re-run)", all(d_.get("proposal_sha256") == PROPOSAL_SHA256 for d_ in p_docs),
              [str(d_.get("proposal_sha256"))[:16] for d_ in p_docs], cover=["CMD-POSTING-PROPOSAL-SHA"])
        # the posting under a FALSE flag, end to end (absent; uncommitted)
        fa_d, fu_d = base / "post-fa", base / "post-fu"
        fa_d.mkdir()
        fu_d.mkdir()
        _, _, pfa = run_posting(tp, _BT_STATE["rec_table"], fl_abs, pdir, fa_d, env_p)
        _, _, pfu = run_posting(tp, _BT_STATE["rec_table"], fl_unc, pdir, fu_d,
                                _bt_env(base, committed=uncommitted(fl_unc)))
        pf = [json.loads(x[0].read_text()) for x in (pfa, pfu)]

        def struck_p(d, src):
            o = d["outputs"]
            return (d["flag"]["value"] is False and d["flag"]["path"] == _repo_rel(src)
                    and o["dose_note"] == {"status": "none (struck, §7.5(c))", "text": None}
                    and [it["row_id"] for it in o["enumeration"] if (it["c"] or {}).get("treatment") == "strike"]
                    == ["P03", "P18"])
        B.chk("posting under a FALSE flag: an absent and an uncommitted --flag-source each give flag FALSE with the "
              "passed path recorded, the dose note struck, and the (c) strike items (P03, P18)",
              struck_p(pf[0], fl_abs) and struck_p(pf[1], fl_unc), (pf[0]["flag"]["reason"], pf[1]["flag"]["reason"]),
              cover=["CMD-POSTING-FLAG-FALSE"])

        # the posting's refusals, one case each (exit 2; nothing written)
        def refused_post(td, table=None, env=None, vdir=None):
            q_ = base / "post-ref"
            q_.mkdir(exist_ok=True)
            tp.write_text(json.dumps(td))
            before = sorted(x.name for x in q_.iterdir())
            ok_, msg_ = _bt_raises(lambda: run_posting(tp, table or _BT_STATE["rec_table"], REPO / FLAG_SOURCE_REL,
                                                       vdir or pdir, q_, env or env_p), (AnlRefusal,))
            return ok_ and sorted(x.name for x in q_.iterdir()) == before, B.clean(msg_)
        tq = copy.deepcopy(tdoc4)                          # Q-F0 NOT-RUN, sft PASS, dpo NOT-RUN, instruct DEAD
        bad_reason = copy.deepcopy(tq)
        bad_reason["reasons"]["Q-F0"] = not_run_reason("Q-F0", "clock:k-zero", CLOCK_DATE)
        rr_ = refused_post(bad_reason)
        B.chk("posting refused: a NOT-RUN coordinate whose reason differs from the unit's NOT-RUN output",
              rr_[0] and "reason differs" in rr_[1], rr_[1][:60], cover=["CMD-POSTING-REASON-MISMATCH"])
        both = base / "post-both"
        both.mkdir()
        for f_ in pdir.glob("*_*.json"):
            if f_.name.startswith(("Q-F0_", "OLMo-")):
                (both / f_.name).write_bytes(f_.read_bytes())
        (both / "Q-F0_VERDICTS.json").write_text(json.dumps({"arm": {"state": "PASS"}}))
        tq_pass = copy.deepcopy(tq)
        tq_pass["tuple"]["Q-F0"] = "PASS"
        tq_pass["reasons"].pop("Q-F0")
        rb1, rb2 = refused_post(tq, vdir=both), refused_post(tq_pass, vdir=both)
        B.chk("posting refused: a unit carrying both a VERDICTS and a NOT-RUN output, whether its coordinate is "
              "NOT-RUN or an outcome (m:324)", rb1[0] and rb2[0] and "has a VERDICTS output" in rb1[1]
              and "has a NOT-RUN" in rb2[1], (rb1[1][:50], rb2[1][:50]), cover=["CMD-POSTING-BOTH-OUTPUTS"])
        ks = copy.deepcopy(tq)
        ks["reasons"]["OLMo-sft"] = "x"
        ks2 = copy.deepcopy(tq)
        ks2["pending"] = {"OLMo-instruct": {"substate": "locked-running", "clock_passed": False,
                                            "date": "2026-10-29"}}
        rk1, rk2 = refused_post(ks), refused_post(ks2)
        B.chk("posting refused: reasons naming a unit that is not NOT-RUN; pending naming a unit that is not PENDING",
              rk1[0] and rk2[0] and "reasons name exactly" in rk1[1] and "reasons name exactly" in rk2[1],
              rk1[1][:60], cover=["CMD-POSTING-KEYSET"])
        ru = refused_post(tq, env=_bt_env(base, committed=uncommitted(_BT_STATE["rec_table"])))
        rph = refused_post(tq, table=ph_tab)
        B.chk("posting refused: an uncommitted sentence table; a placeholder table (it serves G-ANL-F0 only, m:286)",
              ru[0] and "not committed" in ru[1] and rph[0] and "a placeholder serves G-ANL-F0 only" in rph[1],
              (ru[1][:50], rph[1][:50]), cover=["CMD-POSTING-TABLE-REFUSALS"])
        mal = base / "post-mal"
        mal.mkdir()
        for f_ in pdir.glob("*_*.json"):
            if f_.name.startswith(("Q-F0_", "OLMo-")):
                (mal / f_.name).write_bytes(f_.read_bytes())
        (mal / "Q-F0_NOT-RUN.json").write_text("[]")
        rm_ = refused_post(tq, vdir=mal)
        B.chk("posting refused (exit 2, not a traceback): a unit output that is not a JSON object",
              rm_[0] and "not a JSON object" in rm_[1], rm_[1][:60], cover=["CMD-POSTING-MALFORMED"])
        # PIN-40 at the posting: with Q-F0's VERDICTS on record, the table of record is the one it recorded
        bd = base / "post-bound"
        bd.mkdir()
        tsha = _sha256_bytes(Path(_BT_STATE["rec_table"]).read_bytes())
        # Q-F0's stub VERDICTS carries an (empty) v1 enumeration: the comparator of PIN-44's posted run below
        for u in UNITS:
            (bd / f"{u}_VERDICTS.json").write_text(json.dumps({"arm": {"state": "PASS"}, "inputs": {
                "sentences": {"sha256": tsha if u == "Q-F0" else None}},
                **({"schema": VERDICTS_SCHEMA, "unit": "Q-F0", "v1_outputs": {"enumeration": []}} if u == "Q-F0" else {})}))
        tall = {"schema": TUPLE_SCHEMA, "posting": "v1", "tuple": {u: "PASS" for u in UNITS}, "reasons": {},
                "pending": {}}
        other = base / "table-of-record-other.json"
        other.write_text(json.dumps(json.loads(Path(_BT_STATE["rec_table"]).read_text(encoding="utf-8"))))
        rbo = refused_post(tall, table=other, vdir=bd)
        tp.write_text(json.dumps(tall))
        ob = base / "post-bound-out"
        ob.mkdir()
        sbo, _, _ = run_posting(tp, _BT_STATE["rec_table"], REPO / FLAG_SOURCE_REL, bd, ob, env_p)
        spo, _, _ = run_posting(tp, posted_min, REPO / FLAG_SOURCE_REL, bd, ob, env_p, rewrites=rw_none)
        bn = base / "post-bound-nr"                        # a locked Q-F0's no-first-read NOT-RUN (from verdicts)
        bn.mkdir()
        for u in UNITS[1:]:
            (bn / f"{u}_VERDICTS.json").write_bytes((bd / f"{u}_VERDICTS.json").read_bytes())
        why_c = not_run_reason("Q-F0", "no-first-read:cap")
        (bn / "Q-F0_NOT-RUN.json").write_text(json.dumps({"reason": why_c, "cause": "no-first-read:cap",
                                                          "inputs": {"sentences": {"sha256": tsha}}}))
        tnr = {**tall, "tuple": {**tall["tuple"], "Q-F0": "NOT-RUN"}, "reasons": {"Q-F0": why_c}}
        rbn = refused_post(tnr, table=other, vdir=bn)
        B.chk("posting: once Q-F0's lock was reached, an of-record table other than the one its `verdicts` output "
              "read is refused -- after its VERDICTS and after a no-first-read NOT-RUN (PIN-40); the recorded "
              "table is accepted; a posted-kind table is not bound; a Clock NOT-RUN binds none (CMD-POSTING)",
              rbo[0] and "not the one Q-F0's VERDICTS output read" in rbo[1] and rbn[0]
              and "not the one Q-F0's NOT-RUN output read" in rbn[1] and sbo == spo == "written",
              (rbo[1][:60], rbn[1][:60], sbo, spo), cover=["CMD-POSTING-TABLE-BOUND"])
        # C7's posting bar and the comparison (PIN-44), against Q-F0's VERDICTS of the COMPLETE campaign (its v1
        # outputs over the table of record, under its tuple: its own state and the declared OLMo states)
        vdir_v = base / "out" / "complete"
        en_v = [it["row_id"] for it in doc["v1_outputs"]["enumeration"]]
        sd_v = json.loads(Path(_BT_STATE["olmo_states"]).read_text())["states"]
        t_v = {"schema": TUPLE_SCHEMA, "posting": "v1", "tuple": dict(doc["tuple"]),
               "reasons": {"OLMo-dpo": not_run_reason("OLMo-dpo", sd_v["OLMo-dpo"]["cause"], sd_v["OLMo-dpo"]["date"])},
               "pending": {"OLMo-sft": {k_: v_ for k_, v_ in sd_v["OLMo-sft"].items() if k_ != "state"}}}
        tp_v, tp_n, tp_all = base / "tuple-verdicts.json", base / "tuple-notrun.json", base / "tuple-all-pass.json"
        tp_v.write_text(json.dumps(t_v))
        tp_n.write_text(json.dumps(tdoc4))
        tp_all.write_text(json.dumps(tall))

        def post_try(name, table, rewrites=None, *, tuple_p=tp_v, vdir=vdir_v, flag=REPO / FLAG_SOURCE_REL, env=None):
            o_ = base / "post-bar" / name
            o_.mkdir(parents=True, exist_ok=True)
            before = {x.name for x in o_.iterdir()}
            try:
                st_, ln_, ps_ = run_posting(tuple_p, table, flag, vdir, o_, env or env_p, rewrites=rewrites)
                res_ = {"r": "ok", "st": st_, "lines": ln_, "doc": json.loads(ps_[0].read_text())}
            except AnlPostingFail as e:
                res_ = {"r": "fail", "lines": e.lines, "bar": e.bar, "exit": _exit_of(e)}
            except AnlRefusal as e:
                res_ = {"r": "refused", "msg": B.clean(str(e)), "exit": _exit_of(e)}
            res_["new"] = sorted({x.name for x in o_.iterdir()} - before)
            return res_
        B.chk("posting (PIN-44): an of-record run records C7's bar as not applicable, with its reason, and takes no "
              "rewrite list (its inputs carry none)", po.get("bar") == {"applies": False, "reason": BAR_NOT_APPLICABLE}
              and "rewrites" not in po.get("inputs", {}) and json.loads(p_r1[0].read_text()).get("bar") == po["bar"]
              and "'The pass bar for the posting's re-run on the posted text'; Code's reading (PIN-44)"
              in BAR_NOT_APPLICABLE, po.get("bar", {}).get("applies"), cover=["CMD-POSTING-BAR-NA"])
        rw_v = rw_file("verdicts-all", en_v)
        pv1, pv2 = post_try("pass", posted_min, rw_v), post_try("pass", posted_min, rw_v)
        bv = (pv1.get("doc") or {}).get("bar") or {}
        cv = bv.get("comparison") or {}
        qv_p = vdir_v / "Q-F0_VERDICTS.json"
        t_tab_min = json.loads(posted_min.read_text(encoding="utf-8"))
        B.chk("posting (C7's bar, PIN-44): PASS on a minimal posted table that enumerates nothing (the flag of record "
              "TRUE, its dose-note row carried), its rewrite list naming every row Q-F0's VERDICTS enumerated: bar "
              "{applies, PASS, enumeration empty, dose note iff the flag, residue []}; the comparison with the VERDICTS "
              "enumeration (kind, path, sha256 and its stored tuple recorded; that tuple this run's) differs in "
              "nothing; inputs.rewrites recorded; outputs are v1_outputs' own; written (exit 0), identical on a re-run",
              table_problems(t_tab_min, read_repo_file=env_p.read_repo_file) == [] and bool(en_v)
              and pv1["r"] == "ok" and pv1["st"] == "written" and pv1["new"] == ["POSTING-v1_outputs.posted.json"]
              and pv2["r"] == "ok" and pv2["st"] == "identical"
              and sorted(bv) == ["applies", "comparison", "dose_note_iff_flag", "enumeration_empty", "residue", "verdict"]
              and bv["applies"] is True and bv["verdict"] == "PASS" and bv["enumeration_empty"] is True
              and bv["dose_note_iff_flag"] is True and bv["residue"] == []
              and cv.get("comparator") == {"kind": "verdicts", "path": _repo_rel(qv_p), "sha256": _sha256_bytes(qv_p.read_bytes()),
                                           "tuple": t_v["tuple"]}
              and cv.get("same_tuple") is True
              and cv["differs"] is False and cv["only_actual"] == cv["only_expected"] == cv["changed"] == cv["moved"] == []
              and cv["rewrites_not_in_comparator"] == []
              and pv1["doc"]["inputs"].get("rewrites") == _file_rec(rw_v, rw_v.read_bytes())
              and pv1["doc"]["outputs"] == json.loads(json.dumps(v1_outputs(
                  tuple(t_v["tuple"][u] for u in UNITS), t_v["reasons"], True, t_tab_min)))
              and pv1["doc"]["outputs"]["dose_note"]["status"] == "carried" and pv1["doc"]["flag"]["value"] is True,
              (pv1["r"], pv1.get("st"), pv2.get("st"), bv.get("verdict"), cv.get("differs")),
              cover=["CMD-POSTING-BAR-PASS", "CMD-POSTING-CMP-MATCH", "CMD-POSTING-CMP-VERDICTS"])
        pf1 = post_try("fail", posted, rw_none)
        bf = pf1.get("bar") or {}
        # the FAIL's stdout is the record of that step (A FAIL writes nothing): every residue row in full, as the
        # enumeration carries it and in table order (the VERDICTS stored the same items: same table, same tuple),
        # and the unwritten record's inputs and binding; an item carries enumeration()'s fields only (no tag, pick
        # or free-round event), and no roster word reaches the lines
        en_items = doc["v1_outputs"]["enumeration"]
        want_res = [f"POSTING v1: residue {i_} of {len(en_items)}, {it_['row_id']}: {json.dumps(it_, sort_keys=True)}"
                    for i_, it_ in enumerate(en_items, 1)]
        got_res = [ln_ for ln_ in pf1.get("lines") or [] if ln_.startswith("POSTING v1: residue ")
                   and not ln_.startswith("POSTING v1: residue by row id")]
        rec_ln = [ln_ for ln_ in pf1.get("lines") or [] if ln_.startswith("POSTING v1: the unwritten record: ")]
        b_env = analyzer_binding(env_p)
        js_ = lambda x_: json.dumps(x_, sort_keys=True)                                       # noqa: E731
        fl_rec = flag_of_record(REPO / FLAG_SOURCE_REL, env_p.committed)
        cmp_v = {"kind": "verdicts", "path": _repo_rel(qv_p), "sha256": _sha256_bytes(qv_p.read_bytes()),
                 "tuple": t_v["tuple"]}

        def want_record(table_p_, rw_p_):
            return ("POSTING v1: the unwritten record: declared "
                    + js_({"tuple": t_v["tuple"], "reasons": t_v["reasons"], "pending": t_v["pending"]})
                    + "; inputs " + js_({"tuple": _file_rec(tp_v, tp_v.read_bytes()),
                                         "sentences": _file_rec(table_p_, table_p_.read_bytes()),
                                         "rewrites": _file_rec(rw_p_, rw_p_.read_bytes())})
                    + "; comparator " + js_(cmp_v) + "; flag " + js_(fl_rec) + "; binding " + js_(b_env))

        def item_fields_ok(it_):
            a_, b_, c_ = it_.get("a"), it_.get("b"), it_.get("c")
            return (sorted(it_) == list(ENUM_ITEM_KEYS)
                    and (a_ is None or (sorted(a_) == ["cells"] and all(sorted(x_) == ["cell", "label"] for x_ in a_["cells"])))
                    and (b_ is None or sorted(b_) == ["ceiling", "thesis"])
                    and (c_ is None or sorted(c_) == ["flag", "treatment"]))
        B.chk("posting (C7's bar, PIN-44): FAIL with residue -- a posted copy of the table of record under the VERDICTS "
              "tuple, its rewrite list empty: AnlPostingFail (exit 5), nothing written, the residue by row id printed "
              "(every row the VERDICTS enumerated, in table order) with the comparison (no row differs: the same rows "
              "enumerate); its record on stdout: each residue row in full (sorted-key JSON, enumeration()'s fields "
              "only), the unwritten record exactly: the declared tuple with its reasons and pending, the inputs (the "
              "tuple's, the posted table's and the rewrite list's path and sha256), comparator, flag and binding "
              "(analyzer, package, closure sha256), each in sorted-key JSON; no roster word",
              pf1["r"] == "fail" and pf1["exit"] == 5 and pf1["new"] == [] and bf.get("verdict") == "FAIL"
              and bf.get("enumeration_empty") is False and bf.get("dose_note_iff_flag") is True
              and bf.get("residue") == en_v and (bf.get("comparison") or {}).get("differs") is False
              and any(ln_.startswith("POSTING v1: residue by row id") and ", ".join(en_v) in ln_ for ln_ in pf1["lines"])
              and any("FAIL against C7's bar" in ln_ and "nothing written" in ln_ for ln_ in pf1["lines"])
              and any("comparison with the verdicts enumeration" in ln_ for ln_ in pf1["lines"])
              and got_res == want_res and all(item_fields_ok(it_) for it_ in en_items)
              and rec_ln == [want_record(posted, rw_none)] and bf["comparison"]["comparator"] == cmp_v
              and "POSTING v1: comparison rewrites not in the comparator: []" in pf1["lines"]
              and not stages._ROSTER_RX.search("\n".join(pf1["lines"])),
              (pf1["r"], pf1.get("exit"), len(bf.get("residue") or []), len(got_res), len(rec_ln)),
              cover=["CMD-POSTING-BAR-FAIL"])
        # the residue is listed in table order, not by id: a posted copy of the table of record whose row ids run
        # backwards (rows still in loc order), and a minimal posted table P09, P01, P03 (two null-cell rows)
        pt_rev = copy.deepcopy(pt)
        for r_, i_ in zip(pt_rev["rows"], [r_["id"] for r_ in pt_rev["rows"]][::-1]):
            r_["id"] = i_
        posted_rev = base / "table-posted-ids-reversed.json"
        posted_rev.write_text(resume.json_text(pt_rev, indent=1), encoding="utf-8")
        pf_rev = post_try("fail-ids-reversed", posted_rev, rw_none)
        res_rev = (pf_rev.get("bar") or {}).get("residue") or []

        def posted_rows(name, spec):
            texts = {rid: f"[posted {rid}] A synthetic posted sentence" + (f"; synthetic dose note {rid}." if d else ".")
                     for rid, _, _, d in spec}
            body = "".join(texts[rid] + "\n" for rid, *_ in spec)
            pre = f"PREPRINT-posted-{name}.md"
            (base / pre).write_text(body, encoding="utf-8")
            pb = body.encode("utf-8")
            rows = [{"id": rid, "loc": {"line": ln, "section": "posted", "sentence": 1}, "text": texts[rid],
                     "text_sha256": hashlib.sha256(texts[rid].encode("utf-8")).hexdigest(), "null_cells": list(nc),
                     "thesis": None, "dose_note": d, "dose_note_span": f"synthetic dose note {rid}" if d else None,
                     "kinds": list(k)} for ln, (rid, nc, k, d) in enumerate(spec, 1)]
            t = {"schema": TABLE_SCHEMA, "kind": "posted", "posting": "v1", "cells": list(CELLS),
                 "kinds_vocabulary": list(KINDS_VOCAB), "rows": rows,
                 "preprint": {"path": pre, "sha256": _sha256_bytes(pb), "bytes": len(pb), "lines": body.count("\n")}}
            p = base / f"table-posted-{name}.json"
            p.write_text(resume.json_text(t, indent=1), encoding="utf-8")
            return p
        posted_ord = posted_rows("order", [("P09", ["weight"], [], False), ("P01", ["weight"], [], False),
                                           ("P03", [], ["f1-corr-line", "dose-note"], True)])
        pf_o = post_try("fail-order", posted_ord, rw_none)
        B.chk("posting (C7's bar, PIN-44): the residue is listed in table order, not by id -- a posted copy of the "
              "table of record whose row ids run backwards (rows still in loc order) FAILs with its residue in row "
              "order; a minimal posted table P09, P01 (each a null on the weight channel), P03 FAILs with residue "
              "[P09, P01], printed so",
              pf_rev["r"] == "fail" and len(res_rev) >= 2 and res_rev != sorted(res_rev)
              and res_rev == [r_["id"] for r_ in pt_rev["rows"] if r_["id"] in set(res_rev)]
              and pf_o["r"] == "fail" and pf_o["bar"]["residue"] == ["P09", "P01"]
              and any(ln_.endswith("residue by row id (2): P09, P01") for ln_ in pf_o["lines"]),
              (pf_rev["r"], res_rev[:4], pf_o["r"], (pf_o.get("bar") or {}).get("residue")),
              cover=["CMD-POSTING-RESIDUE-ORDER"])
        me_mod = sys.modules[__name__]

        def via_main(name, table, rewrites):
            o_ = base / "post-main" / name
            o_.mkdir(parents=True, exist_ok=True)
            argv_ = (["posting", "--posting", "v1", "--tuple", str(tp_v), "--sentences", str(table), "--verdicts-dir",
                      str(vdir_v), "--out", str(o_)] + (["--rewrites", str(rewrites)] if rewrites is not None else []))
            out_, err_ = io.StringIO(), io.StringIO()
            with _bt_patched(me_mod, "production_env", lambda: env_p), contextlib.redirect_stdout(out_), \
                    contextlib.redirect_stderr(err_):
                try:
                    rc_ = main(argv_)
                except SystemExit as e:
                    rc_ = ("SystemExit", str(e.code)[:40])
            return rc_, out_.getvalue(), err_.getvalue(), sorted(x.name for x in o_.iterdir())
        m_fail, m_pass = via_main("fail", posted, rw_none), via_main("pass", posted_min, rw_v)
        m_rec = via_main("of-record-rewrites", _BT_STATE["rec_table"], rw_none)
        B.chk("exit codes (PIN-26, PIN-44): through main() (--rewrites), the posted text's FAIL returns 5 with its "
              "record on stdout (the residue by row id and in full, the unwritten record) and nothing written; its "
              "PASS returns 0 and writes; --rewrites on the table of record returns 2 (refused, nothing written); "
              "PIN-26 states the posting's 5 before 'any other SystemExit maps to 4'",
              m_fail[0] == 5 and "FAIL against C7's bar" in m_fail[1] and ", ".join(en_v) in m_fail[1] and m_fail[3] == []
              and all(ln_ in m_fail[1] for ln_ in want_res) and "POSTING v1: the unwritten record: declared {" in m_fail[1]
              and m_pass[0] == 0 and "PASS against C7's bar" in m_pass[1]
              and m_pass[3] == ["POSTING-v1_outputs.posted.json"] and m_rec[0] == 2
              and "--rewrites is the posted text's input" in m_rec[2] and m_rec[3] == []
              and "FAIL against C7's bar" in PINS["PIN-26"] and "posting also 5" in PINS["PIN-26"]
              and PINS["PIN-26"].index("posting also 5") < PINS["PIN-26"].index("any other SystemExit maps to 4"),
              (m_fail[0], m_pass[0], m_rec[0]), cover=["CMD-POSTING-EXIT-5"])
        m_e_rec, m_e_pst = via_main("empty-of-record", _BT_STATE["rec_table"], ""), via_main("empty-posted", posted_min, "")
        B.chk("posting refused (PIN-44; exit 2, nothing written): an empty --rewrites is a given path, through main() -- "
              "on the table of record refused as a rewrite list given there; on the posted text refused as unreadable "
              "(it names no file)",
              m_e_rec[0] == 2 and "--rewrites is the posted text's input" in m_e_rec[2] and m_e_rec[3] == []
              and m_e_pst[0] == 2 and "the rewrite list unreadable" in m_e_pst[2] and m_e_pst[3] == [],
              (m_e_rec[0], m_e_rec[2][-60:], m_e_pst[0], m_e_pst[2][-60:]), cover=["CMD-POSTING-REWRITES-EMPTY"])
        posted_nodose = _bt_posted_min(base, "nodose", dose=False)
        pd_t = post_try("dose-true-nodose", posted_nodose, rw_v)
        pd_f = post_try("dose-false-dose", posted_min, rw_v, flag=fl_abs)
        pd_c = post_try("dose-false-nodose", posted_nodose, rw_v, flag=fl_abs)
        # the conjunct is computed on its own (from dose_note's status), not through clause (c): called directly with
        # an empty enumeration -- unreachable through run_posting, where (c) mirrors it -- it alone FAILs the bar
        t_nodose = json.loads(posted_nodose.read_text(encoding="utf-8"))
        pd_x = {fl_: posting_bar({"enumeration": []}, fl_, t_tab_min if not fl_ else t_nodose,
                                cv.get("comparator") or {"kind": "verdicts", "path": "", "sha256": "", "tuple": None}, [], [],
                                t_v["tuple"])
                for fl_ in (True, False)}
        B.chk("posting (C7's bar, PIN-44): the dose conjunct is false under each flag value -- flag TRUE with no "
              "dose-note row (carried at P03, the f1 CORR line) and flag FALSE with one (struck at P03) each FAIL with "
              "dose_note_iff_flag false and residue [P03], nothing written; flag FALSE with no dose-note row PASSes "
              "(dose_note_iff_flag true); called directly with an empty enumeration, the conjunct alone FAILs the bar "
              "under each flag value",
              all(r_["r"] == "fail" and r_["bar"]["dose_note_iff_flag"] is False and r_["bar"]["residue"] == ["P03"]
                  and r_["new"] == [] for r_ in (pd_t, pd_f))
              and pd_c["r"] == "ok" and pd_c["doc"]["bar"]["verdict"] == "PASS"
              and pd_c["doc"]["bar"]["dose_note_iff_flag"] is True and pd_c["doc"]["flag"]["value"] is False
              and all(x_["verdict"] == "FAIL" and x_["enumeration_empty"] is True and x_["dose_note_iff_flag"] is False
                      for x_ in pd_x.values()),
              (pd_t["r"], pd_f["r"], pd_c["r"], {k_: x_["verdict"] for k_, x_ in pd_x.items()}),
              cover=["CMD-POSTING-BAR-DOSE"])
        pt_chg = copy.deepcopy(pt)
        for r_ in pt_chg["rows"]:
            if r_["id"] == "P17":
                r_["thesis"] = None
        posted_chg = base / "table-posted-changed.json"
        posted_chg.write_text(resume.json_text(pt_chg, indent=1), encoding="utf-8")
        dx_a = post_try("cmp-only-actual", posted, rw_file("p02", ["P02", "X99"]))
        dx_e = post_try("cmp-only-expected", posted_min, rw_none)
        dx_c = post_try("cmp-changed", posted_chg, rw_none)
        dx_n = post_try("cmp-not-in", posted_min, rw_file("not-in-comparator", en_v + ["P01", "X99"]))
        pt_a3 = copy.deepcopy(pt)                         # P11 keeps clause (a), on one null cell instead of three
        for r_ in pt_a3["rows"]:
            if r_["id"] == "P11":
                r_["null_cells"] = ["e2b"]
        posted_a3 = base / "table-posted-same-letters.json"
        posted_a3.write_text(resume.json_text(pt_a3, indent=1), encoding="utf-8")
        dx_3 = post_try("cmp-same-letters", posted_a3, rw_none)
        pt_oe = copy.deepcopy(pt)                         # P02 no longer enumerates: only_expected on a FAIL
        for r_ in pt_oe["rows"]:
            if r_["id"] == "P02":
                r_["null_cells"], r_["thesis"] = [], None
        posted_oe = base / "table-posted-p02-cleared.json"
        posted_oe.write_text(resume.json_text(pt_oe, indent=1), encoding="utf-8")
        dx_o = post_try("cmp-only-expected-fail", posted_oe, rw_none)
        ca_ = (dx_a.get("bar") or {}).get("comparison") or {}
        ce_ = ((dx_e.get("doc") or {}).get("bar") or {}).get("comparison") or {}
        cc_ = (dx_c.get("bar") or {}).get("comparison") or {}
        cn_ = ((dx_n.get("doc") or {}).get("bar") or {}).get("comparison") or {}
        c3_ = (dx_3.get("bar") or {}).get("comparison") or {}
        co_ = (dx_o.get("bar") or {}).get("comparison") or {}
        ch_c, ch_3 = cc_.get("changed") or [], c3_.get("changed") or []
        # the whole item is compared: called directly, an item whose treatments differ is changed; one that differs
        # in loc alone is moved, not changed (informational: differs does not count it); one that moved AND differs
        # elsewhere is changed; the identical item is neither. A FAIL prints the moved row in full.
        it0 = json.loads(json.dumps(en_items[0]))
        moved, treat = copy.deepcopy(it0), copy.deepcopy(it0)
        moved["loc"]["line"] += 1
        treat["treatments"] = list(treat["treatments"]) + ["battery-extra-treatment"]
        both_ = copy.deepcopy(treat)
        both_["loc"]["line"] += 1
        bx_d = {k_: posting_bar({"enumeration": [x_]}, True, t_tab_min, cv["comparator"], [it0], [], t_v["tuple"])
                for k_, x_ in (("same", it0), ("moved", moved), ("treatments", treat), ("moved+treatments", both_))}
        dx_d = {k_: b_["comparison"]["changed"] for k_, b_ in bx_d.items()}
        mx_d = {k_: b_["comparison"]["moved"] for k_, b_ in bx_d.items()}
        mv_lines = posting_fail_lines(bx_d["moved"], [moved], [it0], {}, {}, {}, {})

        def has_line(res_, start_):
            return any(ln_.startswith(start_) for ln_ in res_.get("lines") or [])

        def line_of(res_, rx_):
            got_ = [ln_[m_.end():] for ln_ in res_.get("lines") or [] for m_ in [re.match(rx_, ln_)] if m_]
            return got_[0] if len(got_) == 1 else None
        js_ = lambda x_: json.dumps(x_, sort_keys=True)                                       # noqa: E731
        it_by = {it_["row_id"]: it_ for it_ in en_items}
        B.chk("posting (PIN-44): the comparison reports each kind of difference and does not decide the verdict -- "
              "only_actual (P02 in the rewrite list yet still enumerated: FAIL); only_expected (nothing rewritten, "
              "nothing enumerated: every VERDICTS row, yet PASS, written; on a FAIL, P02 cleared on a posted copy); "
              "changed, the two items differing in a field other than loc (P17's thesis struck: clauses [a, b] -> [a]; "
              "P11 on one null cell of three: clauses [a] on both sides; called directly, an item with other "
              "treatments, also when it moved; the identical one not); moved, differing in loc alone (called "
              "directly: moved, not changed, differs false; a FAIL prints it in full); rewrite ids the VERDICTS never "
              "enumerated (P01, X99) informational only (PASS, differs false; on a FAIL printed as the JSON list "
              "[\"X99\"]); on a FAIL each set's rows are printed exactly, in full (only_actual P02 as this run "
              "enumerates it, only_expected P02 as the VERDICTS stored it, changed P17 with both items, P17's residue "
              "line with this run's item), and the summary names changed and moved by row id",
              dx_a["r"] == "fail" and ca_.get("only_actual") == ["P02"] and ca_.get("only_expected") == []
              and ca_.get("changed") == [] and ca_.get("differs") is True
              and has_line(dx_a, "POSTING v1: comparison only_actual P02: {")
              and line_of(dx_a, r"POSTING v1: comparison only_actual P02: ") == js_(it_by["P02"])
              == line_of(dx_a, r"POSTING v1: residue \d+ of \d+, P02: ")
              and ca_.get("rewrites_not_in_comparator") == ["X99"]
              and 'POSTING v1: comparison rewrites not in the comparator: ["X99"]' in dx_a["lines"]
              and line_of(dx_o, r"POSTING v1: comparison only_expected P02: ") == js_(it_by["P02"])
              and line_of(dx_c, r"POSTING v1: comparison changed P17: ")
              == f"expected {js_(ch_c[0]['expected'])}; actual {js_(ch_c[0]['actual'])}"
              and line_of(dx_c, r"POSTING v1: residue \d+ of \d+, P17: ") == js_(ch_c[0]["actual"])
              and js_(ch_c[0]["expected"]) == js_(it_by["P17"])
              and any("; changed P17; moved none; rewrites not in the comparator" in ln_ for ln_ in dx_c["lines"])
              and dx_e["r"] == "ok" and dx_e["doc"]["bar"]["verdict"] == "PASS" and ce_.get("only_expected") == en_v
              and ce_.get("only_actual") == [] and ce_.get("differs") is True
              and dx_c["r"] == "fail" and [c_["row_id"] for c_ in ch_c] == ["P17"]
              and ch_c[0]["expected"].get("clauses") == ["a", "b"] and ch_c[0]["actual"].get("clauses") == ["a"]
              and ch_c[0]["actual"].get("b") is None and sorted(ch_c[0]["actual"]) == list(ENUM_ITEM_KEYS)
              and has_line(dx_c, "POSTING v1: comparison changed P17: expected {")
              and cc_.get("only_actual") == [] and cc_.get("only_expected") == [] and cc_.get("differs") is True
              and dx_3["r"] == "fail" and [c_["row_id"] for c_ in ch_3] == ["P11"] and c3_.get("differs") is True
              and ch_3[0]["expected"].get("clauses") == ch_3[0]["actual"].get("clauses") == ["a"]
              and len(ch_3[0]["expected"]["a"]["cells"]) == 3 and len(ch_3[0]["actual"]["a"]["cells"]) == 1
              and dx_o["r"] == "fail" and co_.get("only_expected") == ["P02"] and co_.get("differs") is True
              and has_line(dx_o, "POSTING v1: comparison only_expected P02: {")
              and dx_d["same"] == [] and mx_d["same"] == [] and dx_d["moved"] == []
              and [c_["row_id"] for c_ in mx_d["moved"]] == [it0["row_id"]] and bx_d["moved"]["comparison"]["differs"] is False
              and [c_["row_id"] for c_ in dx_d["treatments"]] == [it0["row_id"]] and mx_d["treatments"] == []
              and [c_["row_id"] for c_ in dx_d["moved+treatments"]] == [it0["row_id"]] and mx_d["moved+treatments"] == []
              and (f"POSTING v1: comparison moved {it0['row_id']}: expected {js_(it0)}; actual {js_(moved)}") in mv_lines
              and any(f"; changed none; moved {it0['row_id']}; " in ln_ for ln_ in posting_bar_lines(bx_d["moved"]))
              and dx_n["r"] == "ok" and cn_.get("rewrites_not_in_comparator") == ["P01", "X99"]
              and cn_.get("differs") is False,
              (dx_a["r"], dx_e["r"], dx_c["r"], dx_3["r"], dx_o["r"], dx_n["r"], {k_: len(v_) for k_, v_ in dx_d.items()}),
              cover=["CMD-POSTING-CMP-DIFFERS"])
        bm = base / "post-cmp-malformed"
        bm.mkdir()
        for u in UNITS:
            (bm / f"{u}_VERDICTS.json").write_text(json.dumps({"arm": {"state": "PASS"}, **(
                {"schema": VERDICTS_SCHEMA, "unit": "Q-F0"} if u == "Q-F0" else {})}))
        s_nei = post_try("select-neither", posted_min, rw_none, tuple_p=tp_n, vdir=pdir)
        s_mal = post_try("select-malformed", posted_min, rw_none, tuple_p=tp_all, vdir=bm)
        o_mb = base / "post-bar" / "select-malformed-beside"   # the same, beside the posting's own of-record output
        o_mb.mkdir(parents=True)
        (o_mb / posting_out_name("of-record")).write_bytes(p_r1[0].read_bytes())
        s_mb = post_try("select-malformed-beside", posted_min, rw_none, tuple_p=tp_all, vdir=bm)
        it_full = json.loads(json.dumps(en_items[0]))
        s_it = {}
        for k_, en_bad in (("no-clauses", [{"row_id": "P02"}]), ("int-id", [{**it_full, "row_id": 2}]),
                           ("not-object", [5]), ("no-loc", [{k__: v__ for k__, v__ in it_full.items() if k__ != "loc"}]),
                           ("clauses-not-list", [{**it_full, "clauses": "a"}]),
                           ("extra-field", [{**it_full, "battery-extra-field": "x"}])):
            bm2 = base / f"post-cmp-malformed-items-{k_}"
            bm2.mkdir()
            for u in UNITS:
                (bm2 / f"{u}_VERDICTS.json").write_text(json.dumps({"arm": {"state": "PASS"}, **(
                    {"schema": VERDICTS_SCHEMA, "unit": "Q-F0", "v1_outputs": {"enumeration": en_bad}}
                    if u == "Q-F0" else {})}))
            s_it[k_] = post_try(f"select-malformed-items-{k_}", posted_min, rw_none, tuple_p=tp_all, vdir=bm2)
        s_bo1, s_bo2 = post_try("select-both", _BT_STATE["rec_table"]), post_try("select-both", posted_min, rw_v)
        B.chk("posting (PIN-44): the comparator is Q-F0's VERDICTS where it exists (even beside the posting's own "
              "of-record output); the posting's own of-record output where it does not (Q-F0 NOT-RUN: "
              "CMD-POSTING-BOTH-KINDS); neither -> refused (exit 2, nothing written); a VERDICTS recording no v1 "
              "enumeration -> refused, also beside the posting's own of-record output (no fallback); a VERDICTS "
              "enumeration item without a list clauses, with a non-str row_id (every other field present), not an "
              "object, lacking only loc, or with an extra field (not exactly enumeration()'s fields) -> refused",
              s_bo1["r"] == "ok" and s_bo2["r"] == "ok"
              and s_bo2["doc"]["bar"]["comparison"]["comparator"]["kind"] == "verdicts"
              and (base / "post-bar" / "select-both" / "POSTING-v1_outputs.of-record.json").is_file()
              and d_p["bar"]["comparison"]["comparator"]["kind"] == "posting-of-record"
              and s_nei["r"] == "refused" and s_nei["exit"] == 2 and "nothing to compare with" in s_nei["msg"]
              and s_nei["new"] == [] and s_mal["r"] == "refused" and "records no v1 enumeration" in s_mal["msg"]
              and s_mal["new"] == [] and s_mb["r"] == "refused" and "records no v1 enumeration" in s_mb["msg"]
              and s_mb["new"] == [] and all(r_["r"] == "refused" and "records no v1 enumeration" in r_["msg"]
                                            and r_["exit"] == 2 and r_["new"] == [] for r_ in s_it.values()),
              (s_nei.get("msg", "")[:50], s_mal.get("msg", "")[:50], s_mb["r"], {k_: r_["r"] for k_, r_ in s_it.items()}),
              cover=["CMD-POSTING-CMP-SELECT"])
        bt_ = base / "post-cmp-tuple"                      # Q-F0's VERDICTS stores another tuple than this posting's
        bt_.mkdir()
        t_other = {**tall["tuple"], "OLMo-sft": "DEAD"}
        for u in UNITS:
            (bt_ / f"{u}_VERDICTS.json").write_text(json.dumps({"arm": {"state": "PASS"}, **(
                {"schema": VERDICTS_SCHEMA, "unit": "Q-F0", "tuple": t_other, "v1_outputs": {"enumeration": []}}
                if u == "Q-F0" else {})}))
        s_tu = post_try("cmp-other-tuple", posted_min, rw_none, tuple_p=tp_all, vdir=bt_)
        c_tu = ((s_tu.get("doc") or {}).get("bar") or {}).get("comparison") or {}
        B.chk("posting (PIN-44): the comparator's stored tuple is recorded beside this run's, informational only -- a "
              "VERDICTS under another tuple (OLMo-sft DEAD there, PASS here): same_tuple false, its tuple recorded, "
              "the bar PASS and written (the comparison decides nothing); under the same tuple same_tuple is true "
              "(CMD-POSTING-BAR-PASS)",
              s_tu["r"] == "ok" and s_tu["doc"]["bar"]["verdict"] == "PASS" and c_tu.get("same_tuple") is False
              and (c_tu.get("comparator") or {}).get("tuple") == t_other and c_tu.get("differs") is False
              and any("its tuple this run's False" in ln_ for ln_ in s_tu.get("lines") or [])
              and any("its tuple this run's True" in ln_ for ln_ in pv1.get("lines") or [])
              and cv.get("same_tuple") is True, (s_tu["r"], c_tu.get("same_tuple")), cover=["CMD-POSTING-CMP-TUPLE"])
        # a comparator storing no tuple, or one that is not an object: recorded None, same_tuple false (L2-5)
        s_tn = {}
        for k_, tv_ in (("none", None), ("list", ["PASS"])):
            bt2 = base / f"post-cmp-tuple-{k_}"
            bt2.mkdir()
            for u in UNITS:
                (bt2 / f"{u}_VERDICTS.json").write_text(json.dumps({"arm": {"state": "PASS"}, **(
                    {"schema": VERDICTS_SCHEMA, "unit": "Q-F0", "v1_outputs": {"enumeration": []},
                     **({"tuple": tv_} if tv_ is not None else {})} if u == "Q-F0" else {})}))
            s_tn[k_] = post_try(f"cmp-tuple-{k_}", posted_min, rw_none, tuple_p=tp_all, vdir=bt2)
        B.chk("posting (PIN-44): a VERDICTS storing no tuple, or a tuple that is not an object -> its tuple recorded "
              "None and same_tuple false (informational: the bar PASSes and is written)",
              all(r_["r"] == "ok" and r_["doc"]["bar"]["verdict"] == "PASS"
                  and r_["doc"]["bar"]["comparison"]["comparator"]["tuple"] is None
                  and r_["doc"]["bar"]["comparison"]["same_tuple"] is False for r_ in s_tn.values()),
              {k_: r_["r"] for k_, r_ in s_tn.items()}, cover=["CMD-POSTING-CMP-TUPLE-NONE"])
        # the comparator is what it is taken for, and names each row once (RV2A-4): a VERDICTS of another schema,
        # with none, or of another unit; an of-record output of another schema or table kind; a VERDICTS
        # enumeration naming a row id twice -- each refused (exit 2, nothing written)
        s_id = {}
        it_mv1 = json.loads(json.dumps(en_items[0]))        # the first item again, different: its loc.line + 1
        it_mv1["loc"]["line"] += 1
        for k_, over_ in (("verdicts-schema", {"schema": "m-verdicts-v0"}), ("verdicts-no-schema", {"schema": None}),
                          ("verdicts-unit", {"unit": "OLMo-sft"}),
                          ("verdicts-dup", {"v1_outputs": {"enumeration": [it_full, it_full]}}),
                          ("verdicts-dup-apart", {"v1_outputs": {"enumeration": [
                              it_full, json.loads(json.dumps(en_items[1])), it_mv1]}})):
            bi_ = base / f"post-cmp-ident-{k_}"
            bi_.mkdir()
            for u in UNITS:
                q_doc = {"arm": {"state": "PASS"}}
                if u == "Q-F0":
                    q_doc.update({"schema": VERDICTS_SCHEMA, "unit": "Q-F0", "v1_outputs": {"enumeration": []}}, **over_)
                    if q_doc["schema"] is None:
                        q_doc.pop("schema")
                (bi_ / f"{u}_VERDICTS.json").write_text(json.dumps(q_doc))
            s_id[k_] = post_try(f"cmp-ident-{k_}", posted_min, rw_none, tuple_p=tp_all, vdir=bi_)
        for k_, over_ in (("of-record-schema", {"schema": "m-posting-v1-outputs-v0"}),
                          ("of-record-kind", {"table_kind": "posted"})):
            oi_ = base / "post-bar" / f"cmp-ident-{k_}"
            oi_.mkdir(parents=True)
            (oi_ / posting_out_name("of-record")).write_text(json.dumps({**json.loads(p_r1[0].read_text()), **over_}))
            s_id[k_] = post_try(f"cmp-ident-{k_}", posted_min, rw_none, tuple_p=tp_n, vdir=pdir)
        B.chk("posting refused (PIN-44; exit 2, nothing written): a comparator that is not what it is taken for -- a "
              "VERDICTS of another schema, with no schema, or of another unit; the posting's of-record output of "
              "another schema or table kind -- and a VERDICTS enumeration naming a row id twice: two identical "
              "adjacent copies, and two DIFFERENT items not adjacent (the first item, the second, then the first "
              "again with its loc.line + 1) (each alone; the comparators of CMD-POSTING-BAR-PASS and "
              "CMD-POSTING-BOTH-KINDS are accepted)",
              all(s_id[k_]["r"] == "refused" and "is not what it is taken for" in s_id[k_]["msg"]
                  for k_ in ("verdicts-schema", "verdicts-no-schema", "verdicts-unit", "of-record-schema",
                             "of-record-kind"))
              and all(s_id[k_]["r"] == "refused" and "names a row id more than once" in s_id[k_]["msg"]
                      for k_ in ("verdicts-dup", "verdicts-dup-apart"))
              and len(en_items) >= 2 and en_items[0]["row_id"] != en_items[1]["row_id"] and it_mv1 != it_full
              and all(r_["exit"] == 2 and r_["new"] == [] for r_ in s_id.values())
              and pv1["r"] == "ok" and d_p["bar"]["comparison"]["comparator"]["kind"] == "posting-of-record",
              {k_: (r_["r"], r_.get("msg", "")[:40]) for k_, r_ in s_id.items()}, cover=["CMD-POSTING-CMP-IDENTITY"])
        # the FAIL record, every line exactly, on a FAIL whose actual item differs from the comparator's (P17's
        # thesis struck on a posted copy of the table of record): built here from the table, the tuple, the flag
        # and the binding, not from the run's own result (RV2A-1, L2-6, RV2A-3)
        t_c = tuple(t_v["tuple"][u] for u in UNITS)
        out_c = json.loads(json.dumps(v1_outputs(t_c, t_v["reasons"], bool(fl_rec["value"]), pt_chg)))
        en_c = out_c["enumeration"]
        act_c = {it_["row_id"]: it_ for it_ in en_c}
        iff_c = (dose_note(True, pt_chg)["status"] == "carried") == bool(fl_rec["value"])
        want_c = ([f"POSTING v1: tuple {t_c}; ceiling {out_c['ceiling']['name']}; {len(en_c)} enumerated rows on the "
                   f"posted text",
                   f"POSTING v1: FAIL against C7's bar (PIN-44): enumeration empty False, dose note present iff the flag "
                   f"{iff_c}; nothing written",
                   f"POSTING v1: residue by row id ({len(en_c)}): {', '.join(it_['row_id'] for it_ in en_c)}",
                   f"POSTING v1: comparison with the verdicts enumeration with the PI's rewrites applied (sha256 "
                   f"{cmp_v['sha256'][:16]}; its tuple this run's True): differs True; only_actual []; only_expected []; "
                   f"changed P17; moved none; rewrites not in the comparator []"]
                  + [f"POSTING v1: residue {i_} of {len(en_c)}, {it_['row_id']}: {js_(it_)}" for i_, it_ in enumerate(en_c, 1)]
                  + [f"POSTING v1: comparison changed P17: expected {js_(it_by['P17'])}; actual {js_(act_c['P17'])}",
                     "POSTING v1: comparison rewrites not in the comparator: []", want_record(posted_chg, rw_none)])
        # the same with a changed row AND moved rows (R3M-6): P17's thesis struck as above, and a blank line inserted
        # in a copy of the preprint before the line of the last enumerated row but one other than P17, so that row
        # and every later one begin one line down (each item otherwise unchanged; two moved rows at least, so their
        # order is pinned too); the changed line precedes the moved lines
        ln_mv = sorted(it_["loc"]["line"] for it_ in en_items if it_["row_id"] != "P17")[-2]
        pre_rec = pt_chg["preprint"]
        pre_ln = (base / pre_rec["path"]).read_text(encoding="utf-8").split("\n")
        body_mv = "\n".join(pre_ln[:ln_mv - 1] + [""] + pre_ln[ln_mv - 1:])
        (base / "PREPRINT-battery-moved.md").write_text(body_mv, encoding="utf-8")
        pb_mv = body_mv.encode("utf-8")
        pt_mv = copy.deepcopy(pt_chg)
        pt_mv["preprint"] = {"path": "PREPRINT-battery-moved.md", "sha256": _sha256_bytes(pb_mv), "bytes": len(pb_mv),
                             "lines": body_mv.count("\n")}
        for r_ in pt_mv["rows"]:
            if r_["loc"]["line"] >= ln_mv:
                r_["loc"]["line"] += 1
        posted_mv = base / "table-posted-changed-moved.json"
        posted_mv.write_text(resume.json_text(pt_mv, indent=1), encoding="utf-8")
        dx_m = post_try("cmp-changed-moved", posted_mv, rw_none)
        out_m = json.loads(json.dumps(v1_outputs(t_c, t_v["reasons"], bool(fl_rec["value"]), pt_mv)))
        en_m = out_m["enumeration"]
        act_m = {it_["row_id"]: it_ for it_ in en_m}
        iff_m = (dose_note(True, pt_mv)["status"] == "carried") == bool(fl_rec["value"])
        mv_ids = [r_["id"] for r_ in pt_chg["rows"] if r_["loc"]["line"] >= ln_mv and r_["id"] != "P17"
                  and r_["id"] in act_m and r_["id"] in it_by]
        sans_ = lambda x_: {k_: v_ for k_, v_ in x_.items() if k_ != "loc"}                    # noqa: E731
        want_m = ([f"POSTING v1: tuple {t_c}; ceiling {out_m['ceiling']['name']}; {len(en_m)} enumerated rows on the "
                   f"posted text",
                   f"POSTING v1: FAIL against C7's bar (PIN-44): enumeration empty False, dose note present iff the flag "
                   f"{iff_m}; nothing written",
                   f"POSTING v1: residue by row id ({len(en_m)}): {', '.join(it_['row_id'] for it_ in en_m)}",
                   f"POSTING v1: comparison with the verdicts enumeration with the PI's rewrites applied (sha256 "
                   f"{cmp_v['sha256'][:16]}; its tuple this run's True): differs True; only_actual []; only_expected []; "
                   f"changed P17; moved {', '.join(mv_ids)}; rewrites not in the comparator []"]
                  + [f"POSTING v1: residue {i_} of {len(en_m)}, {it_['row_id']}: {js_(it_)}" for i_, it_ in enumerate(en_m, 1)]
                  + [f"POSTING v1: comparison changed P17: expected {js_(it_by['P17'])}; actual {js_(act_m['P17'])}"]
                  + [f"POSTING v1: comparison moved {r_}: expected {js_(it_by[r_])}; actual {js_(act_m[r_])}"
                     for r_ in mv_ids]
                  + ["POSTING v1: comparison rewrites not in the comparator: []", want_record(posted_mv, rw_none)])
        B.chk("posting (PIN-44): a FAIL's stdout record, every line exactly as built from the posted table, the tuple "
              "(with its reasons and pending), the flag of record and the binding -- on a FAIL whose actual P17 differs "
              "from the VERDICTS' P17: the head, the verdict, the residue by row id, the comparison summary (changed "
              "P17, moved none), each residue item in full, the changed row with both items, the rewrites line, and "
              "the unwritten record (declared, inputs, comparator, flag, binding); and on a FAIL with a changed row "
              "AND moved rows (P17's thesis struck, and a blank line inserted in a copy of the preprint before the "
              "last enumerated row but one other than P17, which moves that row and every later one a line down: two "
              "moved rows at least): every line exactly, in order -- the summary naming both, the changed line "
              "before the moved lines, each moved row with both items (differing in loc alone), in table order",
              dx_c["r"] == "fail" and dx_c["lines"] == want_c and act_c["P17"] != it_by["P17"]
              and table_problems(pt_mv, read_repo_file=env_p.read_repo_file) == []
              and dx_m["r"] == "fail" and dx_m["lines"] == want_m and len(mv_ids) >= 2
              and sans_(act_m["P17"]) != sans_(it_by["P17"])
              and all(act_m[r_] != it_by[r_] and sans_(act_m[r_]) == sans_(it_by[r_]) for r_ in mv_ids),
              (len(dx_c.get("lines") or []), len(want_c),
               next((i_ for i_, (a_, b_) in enumerate(zip(dx_c.get("lines") or [], want_c)) if a_ != b_), None),
               dx_m["r"], dx_m.get("msg", "")[:80], mv_ids, len(dx_m.get("lines") or []), len(want_m),
               next((i_ for i_, (a_, b_) in enumerate(zip(dx_m.get("lines") or [], want_m)) if a_ != b_), None)),
              cover=["CMD-POSTING-FAIL-RECORD"])
        k_miss = post_try("rw-missing", posted_min, None)
        k_rec = post_try("rw-of-record", _BT_STATE["rec_table"], rw_none)
        B.chk("posting refused (PIN-44; exit 2, nothing written): a posted run with no rewrite list; an of-record run "
              "given one", k_miss["r"] == "refused" and "needs --rewrites" in k_miss["msg"] and k_miss["new"] == []
              and k_rec["r"] == "refused" and "--rewrites is the posted text's input" in k_rec["msg"]
              and k_rec["new"] == [] and k_miss["exit"] == k_rec["exit"] == 2,
              (k_miss.get("msg", "")[:50], k_rec.get("msg", "")[:50]), cover=["CMD-POSTING-REWRITES-KIND"])
        rw_bad_obj, rw_bad_json = rw_d / "not-object.json", rw_d / "not-json.json"
        rw_bad_obj.write_text("[]")
        rw_bad_json.write_text("{")
        rw_no_rows = rw_d / "no-rows.json"
        rw_no_rows.write_text(json.dumps({"schema": REWRITES_SCHEMA, "posting": "v1"}))
        form = {"schema": (rw_file("bad-schema", [], schema="m-posting-rewrites-v0"), "the rewrite list is {schema"),
                "extra-key": (rw_file("bad-extra", [], note="x"), "the rewrite list is {schema"),
                "posting": (rw_file("bad-posting", [], posting="v2"), "the rewrite list is {schema"),
                "no-rows": (rw_no_rows, "the rewrite list is {schema"),
                "not-object": (rw_bad_obj, "the rewrite list is {schema"),
                "not-json": (rw_bad_json, "the rewrite list unreadable"),
                "rows-not-list": (rw_file("bad-rows", [], rows="P02"), "rows are a list of row ids"),
                "int-id": (rw_file("int-id", ["P02", 7]), "rows are a list of row ids"),
                "empty-id": (rw_file("empty-id", ["P02", ""]), "rows are a list of row ids"),
                "duplicate": (rw_file("duplicate", ["P02", "P02"]), "names a row id more than once")}
        f_res = {k_: post_try(f"rw-form-{k_}", posted_min, p_) for k_, (p_, _) in form.items()}
        f_unc = post_try("rw-form-uncommitted", posted_min, rw_v, env=_bt_env(base, committed=uncommitted(rw_v)))
        base_cp = env_p.committed
        f_prb = post_try("rw-form-problems", posted_min, rw_v, env=_bt_env(base, committed=lambda q: (
            ["battery double: problems beside bytes"], Path(q).read_bytes()) if Path(q).resolve() == rw_v.resolve()
            else base_cp(q)))
        B.chk("posting refused (PIN-44; exit 2, nothing written): a rewrite list not committed at HEAD (also where the "
              "commit check reports a problem beside bytes); of another schema, with an extra key, of another "
              "posting, with no rows, not an object, not JSON; rows not a list, a non-string id, an empty id, a "
              "duplicate id -- each alone",
              all(r_["r"] == "refused" and form[k_][1] in r_["msg"] and r_["new"] == [] and r_["exit"] == 2
                  for k_, r_ in f_res.items())
              and all(r_["r"] == "refused" and "the rewrite list is not committed at HEAD" in r_["msg"]
                      and r_["new"] == [] for r_ in (f_unc, f_prb)),
              {k_: r_["r"] for k_, r_ in f_res.items()}, cover=["CMD-POSTING-REWRITES-FORM"])
        ab_first = post_try("rw-bind-first", posted_min, rw_d / "absent.json",
                            env=_bt_env(base, committed=uncommitted(Path(__file__))))
        ab_own = post_try("rw-bind-own", posted_min, rw_d / "absent.json")
        B.chk("posting (PIN-42, PIN-44): the rewrite list is read only after the binding -- with the analyzer "
              "uncommitted an absent rewrite list refuses on the analyzer; with it committed, on the rewrite list",
              ab_first["r"] == "refused" and "analyzer is not committed" in ab_first["msg"]
              and ab_own["r"] == "refused" and "the rewrite list is not committed at HEAD" in ab_own["msg"]
              and ab_first["new"] == ab_own["new"] == [], (ab_first.get("msg", "")[:40], ab_own.get("msg", "")[:40]),
              cover=["CMD-POSTING-REWRITES-AFTER-BINDING"])


def _bt_recount(ck_path: Path, unit: str) -> dict:
    """An independent recount of a campaign checkpoint's raw sessions (the battery's oracle for
    campaign_counts + prepick_counts): the first pick coded from choices[0].pick against cell.P."""
    c, s_ = keys.templates(unit)
    w = {"n0": 0, "k0": 0, "n1": 0, "k1": 0, "mS": 0, "j": 0, "launched": {c: 0, s_: 0}, "prepick": {c: 0, s_: 0},
         "domain": {c: 0, s_: 0}}
    for r in json.loads(Path(ck_path).read_text(encoding="utf-8"))["sessions"]:
        t = r["template"]
        w["launched"][t] += 1
        if (r.get("exclusion") or {}).get("phase") == "forced":
            w["prepick"][t] += 1
        if not r["domain"]:
            continue
        w["domain"][t] += 1
        hit = int(r["choices"][0]["pick"] == r["cell"]["P"])
        if t == c:
            w[f"n{r['cell']['map']}"] += 1
            w[f"k{r['cell']['map']}"] += hit
        else:
            w["mS"] += 1
            w["j"] += hit
    return w


def _bt_flip_first(ck: dict) -> None:
    for r in ck["sessions"]:
        if r["domain"]:
            r["first_free_pick_P"] = not r["first_free_pick_P"]
            return


def _bt_olmo_gates(base: Path, root: Path) -> tuple[Path, Path]:
    """OLMo-sft time and qual checkpoints from testing.suite('olmo')'s records (stage qual), for the reader."""
    recs = _bt_suite_records("olmo")
    out = []
    for stg in ("time", "qual"):
        ident = resume.Identity(unit="OLMo-sft", stage=stg, template_set=["A0-OLMo-sft", "A0s-OLMo-sft"],
                                lock_sha256="1" * 64, schedule_sha256="3" * 64, path="uncached", hour_cap=None,
                                n={"A0-OLMo-sft": 16, "A0s-OLMo-sft": 16}, audit_v2_sha16="4" * 16, ban_sha="5" * 16,
                                backend_identifier="6" * 16, proposal_sha256="2" * 64)
        p = root / "ckpt" / f"OLMo-sft_{stg}.json"
        ck = resume.load_or_init(p, ident, False)
        resume.append_provenance(ck, {"adapter": STUB_MARK + " -- NOT A MODEL", "stage": "battery"},
                                 stamp="2026-10-10T00:00:00Z")
        for r in recs:
            r2 = copy.deepcopy(r)
            r2["stage"] = stg
            r2["verified"] = True
            resume.record_session(ck, r2)
            ck["provenance"][-1]["launched"] += 1
        ck["stage_end"] = {"status": "PASS", "fired": [], "adjudication": None}
        resume.write_checkpoint(p, ck)
        out.append(p)
    return out[0], out[1]


def _bt_olmo_outputs(out: Path) -> None:
    """The OLMo outputs the declared OLMo states cross-check against (a dpo NOT-RUN, an instruct VERDICTS)."""
    out.mkdir(parents=True, exist_ok=True)
    (out / "OLMo-dpo_NOT-RUN.json").write_text(json.dumps({"reason": "dose not completable",
                                                          "cause": "dose-not-completable"}))
    (out / "OLMo-instruct_VERDICTS.json").write_text(json.dumps({"arm": {"state": "DEAD"}}))


def _bt_qf0_v10_inputs(base: Path) -> tuple[Path, Path]:
    """A temp table of record over a temp 'preprint' and the OLMo states, for Q-F0's V10."""
    t = placeholder_table()
    by_line: dict[int, list[str]] = {}
    for r in t["rows"]:                                    # rows sharing a line join it in sentence order
        by_line.setdefault(r["loc"]["line"], []).append(r["text"])
    body = "\n".join(" ".join(by_line.get(n, [])) for n in range(1, max(by_line) + 1)) + "\n"
    (base / "PREPRINT-battery.md").write_text(body, encoding="utf-8")
    pb = body.encode("utf-8")
    t["kind"] = "of-record"
    t["preprint"] = {"path": "PREPRINT-battery.md", "sha256": _sha256_bytes(pb), "bytes": len(pb),
                     "lines": body.count("\n")}
    tp = base / "table-of-record.json"
    tp.write_text(resume.json_text(t, indent=1), encoding="utf-8")
    sp = base / "olmo-states.json"
    sp.write_text(json.dumps({"schema": OLMO_STATES_SCHEMA, "states": {
        "OLMo-sft": {"state": "PENDING", "substate": "locked-running", "clock_passed": False, "date": CLOCK_DATE},
        "OLMo-dpo": {"state": "NOT-RUN", "cause": "dose-not-completable", "date": CLOCK_DATE},
        "OLMo-instruct": {"state": "DEAD"}}}))
    return tp, sp


def _bt_posted_min(base: Path, name: str, dose: bool = True) -> Path:
    """A minimal posted-kind table over its own temp 'preprint', for C7's bar (PIN-44): P01 asserts no
    null; P03, the f1 CORR line, asserts no null and carries the dose note iff ``dose``. Under any tuple
    it enumerates nothing when the flag equals ``dose`` (no null cell, no thesis; (c) silent)."""
    texts = {"P01": "[posted P01] A synthetic posted sentence that asserts no null.",
             "P03": "[posted P03] A synthetic posted CORR line that asserts no null"
                    + ("; synthetic dose note P03." if dose else ".")}
    body = texts["P01"] + "\n" + texts["P03"] + "\n"
    pre = f"PREPRINT-posted-{name}.md"
    (base / pre).write_text(body, encoding="utf-8")
    pb = body.encode("utf-8")
    rows = []
    for ln, (rid, kinds) in enumerate((("P01", []), ("P03", ["f1-corr-line"] + (["dose-note"] if dose else []))), 1):
        d_ = dose and rid == "P03"
        rows.append({"id": rid, "loc": {"line": ln, "section": "posted", "sentence": 1}, "text": texts[rid],
                     "text_sha256": hashlib.sha256(texts[rid].encode("utf-8")).hexdigest(), "null_cells": [],
                     "thesis": None, "dose_note": d_, "dose_note_span": "synthetic dose note P03" if d_ else None,
                     "kinds": kinds})
    t = {"schema": TABLE_SCHEMA, "kind": "posted", "posting": "v1", "cells": list(CELLS),
         "kinds_vocabulary": list(KINDS_VOCAB), "rows": rows,
         "preprint": {"path": pre, "sha256": _sha256_bytes(pb), "bytes": len(pb), "lines": body.count("\n")}}
    p = base / f"table-posted-{name}.json"
    p.write_text(resume.json_text(t, indent=1), encoding="utf-8")
    return p


# --- battery: structure --------------------------------------------------------------------------
def _bt_structure(B: _Battery, lines: Sequence[str], hook: _OpenHook) -> None:
    from valence_core.m import guard
    me = Path(__file__).resolve()
    src = me.read_text(encoding="utf-8")
    probs = constant_problems(lines)
    B.chk("proposal constants: every m-verbatim constant appears on its cited line (m:14, :16, :190, :192, :247, "
          ":306, :310, :312, :314, :316, :324, :326, :334, :337, :338, :340, :341, :343, :349)", probs == [], probs[:2],
          cover=["STR-CONSTANTS"])
    mutant = list(lines)
    mutant[337] = mutant[337].replace("did not pass: outcome", "did not pass: verdict")
    mutant[333] = mutant[333].replace("not acted on", "not acted upon")
    mp = constant_problems(mutant)
    B.chk("proposal constants: a mutated proposal (m:338's slot, m:334's title) is caught", len(mp) >= 2,
          mp[:2], cover=["STR-CONSTANTS-MUTANT"])
    caught = []
    planted = REPO / CKPT_REL / "PLANTED-battery-never-exists.json"
    for how in (lambda: open(planted, "rb"), lambda: io.open(planted, "rb"), lambda: planted.read_bytes(),
                lambda: planted.read_text(), lambda: planted.open("rb"),
                lambda: open(REPO / "results" / "raw" / "PLANTED.txt")):
        try:
            how()
            caught.append(False)
        except PermissionError:
            caught.append(True)
        except OSError:
            caught.append(False)
    passed = (REPO / PROPOSAL_REL).read_bytes()[:10] != b""
    B.chk("open hook: planted reads under data/m/ckpt (open, io.open, Path.read_bytes/read_text/open) and "
          "results/raw are caught before the file is touched; an allowed read passes",
          all(caught) and len(caught) == 6 and passed and hook.caught[-1:] == ["results/raw/PLANTED.txt"],
          (caught, hook.caught[-1:]), cover=["STR-OPEN-HOOK"])
    heavy = sorted({m.split(".")[0] for m in sys.modules} & {"torch", "mlx", "mlx_lm", "transformers"})
    B.chk("no torch, mlx, mlx_lm or transformers in sys.modules", heavy == [], heavy, cover=["STR-NO-HEAVY"])
    # PIN (Code, declared at LOCK v0.1): PIN-28 -- guard.check_call_sites and the forbidden-literal grep
    # run over this file in its battery, both directions.
    cs = guard.check_call_sites([me])
    with tempfile.TemporaryDirectory() as td:
        pl = Path(td) / "m_analyze_planted.py"
        pl.write_text(src + "\n\ndef _smuggle(adapter):\n    return adapter.generate('p', 's', injections=(), "
                            "cached=True)\n", encoding="utf-8")
        cs_bad = guard.check_call_sites([pl])
        fb = Path(td) / "planted.py"
        fb.write_text("x = '" + _forbidden()[0] + "'\n", encoding="utf-8")
        hits_bad = [f for f in _forbidden() if f in fb.read_text(encoding="utf-8")]
    B.chk("guard.check_call_sites is [] over this file and fires on a planted cached=True", cs == [] and len(cs_bad) >= 1
          and all("literal True" in x for x in cs_bad), (len(cs), len(cs_bad)), cover=["STR-CALL-SITES"])
    hits = [f for f in _forbidden() if f in src]
    B.chk("no forbidden literal in this file; the grep fires on a planted copy", hits == [] and hits_bad != [],
          hits, cover=["STR-FORBIDDEN"])
    cl = _BT_STATE["closure"]
    mods = cl["modules"]
    ok_cl = ("valence_core/session.py" in mods and "valence_core/e2d/habit.py" in mods
             and "valence_core/e2d/runner.py" in mods and not any(k.startswith("valence_core/m/") for k in mods)
             and "data/olmo/a1_repair_roster.json" in cl["data"]
             and closure_sha256(cl) == _BT_STATE["closure_sha256"]
             and closure_sha256({**cl, "data": {}}) != _BT_STATE["closure_sha256"])
    B.chk("closure: computed in a fresh interpreter -- valence_core modules outside the package (session, habit, "
          "stages' e2d.runner ...), none inside it, the data file opened at import; its sha moves with any entry",
          ok_cl, (len(mods), sorted(cl["data"])), cover=["STR-CLOSURE"])
    every = lambda q: ([], b"x")
    one_out = lambda q: ([f"{_repo_rel(q)}: not committed"], None) if _repo_rel(q) == "valence_core/e2d/habit.py" \
        else ([], b"x")
    gp_all, gp_one = ganl_commit_problems(every, cl), ganl_commit_problems(one_out, cl)
    B.chk("canonical ganl: every analyzer / placeholder / proposal / package / closure file must be committed (PIN-39); "
          "one uncommitted closure file (habit.py) is named", gp_all == [] and gp_one == [
              "valence_core/e2d/habit.py: not committed"], gp_one, cover=["STR-GANL-COMMITTED"])
    # PIN-26: a canonical `ganl` whose closure cannot be computed exits 4 (STOP), never 1 (the selftest-FAIL
    # code); the battery itself is replaced by a guard so nothing can recurse or write
    me_mod = sys.modules[__name__]

    def no_closure(*a, **k):
        raise AnlStop("STOP: the closure could not be computed: battery (simulated)")

    def no_battery():
        raise RuntimeError("battery: recursion guard")
    rc_g, err = None, io.StringIO()
    with _bt_patched(me_mod, "closure", no_closure), _bt_patched(me_mod, "battery", no_battery), \
            contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
        try:
            rc_g = main(["ganl"])
        except SystemExit as e:
            rc_g = ("SystemExit", str(e.code)[:40])
    B.chk("exit codes (PIN-26): a canonical ganl whose closure cannot be computed returns 4 (STOP), not 1",
          rc_g == 4 and "closure could not be computed" in err.getvalue(), rc_g, cover=["STR-GANL-EXIT"])
    tree = ast.parse(src)
    bad_imp = lazy_import_problems(tree)
    planted_tree = ast.parse("def verdict_helper():\n    from valence_core.m import testing\n"
                             "def _bt_x():\n    from valence_core.m import testing\n")
    planted_mod = ast.parse(src + "\nfrom valence_core.m import testing as _planted_testing\n"
                                  "import valence_core.m.guard\n")
    mod_level = sorted({n for node in tree.body if isinstance(node, (ast.Import, ast.ImportFrom))
                        for n in ([a.name for a in node.names] if isinstance(node, ast.Import)
                                  else [f"{node.module}.{a.name}" for a in node.names]) if n.startswith("valence_core")})
    B.chk("lazy imports: module-level valence_core imports are exactly the declared primitives (MODULE_LEVEL_IMPORTS); "
          "outside the battery a function-level one names only the declared lazy verdict-path module (stages); a "
          "planted module-level testing / guard import and a planted verdict-path testing import are caught, a "
          "battery one is not", bad_imp == [] and mod_level == sorted(MODULE_LEVEL_IMPORTS)
          and lazy_import_problems(planted_tree) == [("verdict_helper", ["valence_core.m.testing"])]
          and lazy_import_problems(planted_mod) == [("<module>", ["valence_core.m.testing"]),
                                                    ("<module>", ["valence_core.m.guard"])],
          (bad_imp[:2], lazy_import_problems(planted_mod)[:2]), cover=["STR-LAZY-IMPORTS"])
    # the G-ANL-F0 manifest (decision 12) against independently read values, both directions
    fake_res = {"closure": _BT_STATE["closure"], "closure_sha256": _BT_STATE["closure_sha256"], "checks_pass": 1,
                "checks_total": 1, "expected_checks": EXPECTED_CHECKS, "coverage_ids": ["X"], "outputs_sha256": "a" * 64,
                "tallies": {"T": 1}, "flag_of_record": {"value": True}}
    art = ganl_artifact(fake_res)
    a_probs = ganl_artifact_problems(art, fake_res)
    plants = {"package": {**art, "package_sha256": "0" * 64},
              "analyzer": {**art, "analyzer": {**art["analyzer"], "sha256": "0" * 64}},
              "closure": {**art, "closure": {**art["closure"], "data": {}}},
              "battery": {**art, "battery": {**art["battery"], "checks_pass": 0}},
              "stamp": {**art, "written_at": "2026-10-10T00:00:00Z"}, "head": {**art, "head": "2c50e03"}}
    caught_p = {k_: bool(ganl_artifact_problems(v, fake_res)) for k_, v in plants.items()}
    B.chk("G-ANL-F0 manifest: the analyzer / placeholder / proposal sha256s are the files', package_sha256 is "
          "resume's, the closure and battery block are the run's, no timestamp or HEAD key; a planted wrong package, "
          "analyzer, closure or battery count, a timestamp and a HEAD are each caught", a_probs == []
          and all(caught_p.values()) and art["package_sha256"] == _BT_STATE["package_sha256"],
          (a_probs[:2], caught_p), cover=["STR-GANL-ARTIFACT"])
    # each remaining sub-check of ganl_artifact_problems, one planted field at a time: the plant is caught as
    # exactly its own problem (the true manifest has none: a_probs above)

    def only(plant):
        return ganl_artifact_problems(plant, fake_res)
    an_ = {k_: v_ for k_, v_ in art["analyzer"].items() if k_ != "sha16"}
    p16 = {"wrong": only({**art, "analyzer": {**an_, "sha16": "0" * 16}}),
           "sha256-tail": only({**art, "analyzer": {**an_, "sha16": art["analyzer"]["sha256"][-16:]}}),
           "missing": only({**art, "analyzer": an_})}
    B.chk("G-ANL-F0 manifest: analyzer.sha16 is its sha256's first 16 hex digits -- a wrong one, the sha256's last 16 "
          "and a missing one are each caught as exactly 'analyzer sha16'", a_probs == []
          and art["analyzer"]["sha16"] == art["analyzer"]["sha256"][:16]
          and all(v_ == ["analyzer sha16"] for v_ in p16.values()), p16, cover=["STR-GANL-SHA16"])
    pfl = {"flipped": only({**art, "flag_of_record": {**art["flag_of_record"], "value": not art["flag_of_record"]["value"]}}),
           "null": only({**art, "flag_of_record": None}),
           "extra-key": only({**art, "flag_of_record": {**art["flag_of_record"], "reason": "battery"}})}
    B.chk("G-ANL-F0 manifest: the flag of record is the battery's -- a flipped value, a null and an extra key are each "
          "caught as exactly 'flag_of_record'", a_probs == [] and all(v_ == ["flag_of_record"] for v_ in pfl.values()),
          pfl, cover=["STR-GANL-FLAG"])
    preg = {"pin-dropped": only({**art, "pins": {k_: v_ for k_, v_ in PINS.items() if k_ != "PIN-1"}}),
            "pin-edited": only({**art, "pins": {**PINS, "PIN-8": PINS["PIN-8"] + " (edited)"}}),
            "seat-routed": only({**art, "seat_routed": {**SEAT_ROUTED, "PIN-8": "ruled (battery)"}}),
            "schema": only({**art, "schema": "m-ganl-f0-v0"})}
    B.chk("G-ANL-F0 manifest: the PIN register, the seat-routed list and the schema are this file's -- a dropped and "
          "an edited PIN, an edited seat-routed entry and another schema are each caught as exactly 'pins / "
          "seat_routed / schema'", a_probs == [] and all(v_ == ["pins / seat_routed / schema"] for v_ in preg.values()),
          preg, cover=["STR-GANL-REGISTER"])
    pph = {"placeholder-sha": only({**art, "placeholder": {**art["placeholder"], "sha256": "0" * 64}}),
           "placeholder-path": only({**art, "placeholder": {**art["placeholder"], "path": TABLE_OF_RECORD_REL}}),
           "proposal-path": only({**art, "proposal": {**art["proposal"], "path": "PROPOSAL-m-gating-campaign-v1_10.md"}})}
    B.chk("G-ANL-F0 manifest: the placeholder's path and sha256 are the file's -- a wrong sha256 and another path are "
          "each caught as exactly 'placeholder path / sha256' (the proposal's path likewise)", a_probs == []
          and pph["placeholder-sha"] == pph["placeholder-path"] == ["placeholder path / sha256"]
          and pph["proposal-path"] == ["proposal path / sha256"], pph, cover=["STR-GANL-PLACEHOLDER"])
    pbt = {k_: only({**art, "battery": {**art["battery"], k_: alt}})
           for k_, alt in (("checks_total", 2), ("expected_checks", EXPECTED_CHECKS + 1), ("coverage_ids", ["X", "Y"]),
                           ("outputs_sha256", "b" * 64), ("tallies", {"T": 2}))}
    B.chk("G-ANL-F0 manifest: the battery block is the run's beyond checks_pass -- a wrong checks_total, "
          "expected_checks, coverage_ids, outputs_sha256 and tallies are each caught as exactly 'battery.<key>'",
          a_probs == [] and all(v_ == [f"battery.{k_}"] for k_, v_ in pbt.items()), pbt, cover=["STR-GANL-BATTERY-BLOCK"])
    # run_ganl's content-check branch (PIN-26): a manifest failing its own content check returns 4 (STOP) and writes
    # nothing; the same battery double with the true manifest writes it (0) -- temp --out directories, the battery
    # replaced by a double so nothing recurses
    ok_res = {**fake_res, "ok": True}
    real_art = ganl_artifact
    outs_g: dict = {}
    with tempfile.TemporaryDirectory() as td:
        for tag, fn in (("planted-head", lambda res: {**real_art(res), "head": "2c50e03"}), ("true", real_art)):
            d_ = Path(td) / tag
            err_ = io.StringIO()
            with _bt_patched(me_mod, "battery", lambda: ok_res), _bt_patched(me_mod, "ganl_artifact", fn), \
                    contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err_):
                try:
                    rc_ = main(["ganl", "--out", str(d_)])
                except SystemExit as e:
                    rc_ = ("SystemExit", str(e.code)[:40])
            outs_g[tag] = (rc_, "fails its own content check" in err_.getvalue(),
                           sorted(x.name for x in d_.iterdir()) if d_.is_dir() else [])
    B.chk("exit codes (PIN-26): a ganl whose manifest fails its own content check (a planted HEAD key) returns 4 (STOP) "
          "and writes nothing; the same battery double with the true manifest writes G-ANL-F0.json (0)",
          outs_g.get("planted-head") == (4, True, []) and outs_g.get("true") == (0, False, [Path(GANL_REL).name]),
          outs_g, cover=["STR-GANL-CONTENT-EXIT"])
    # PIN sites, exactly (FA-1, FID2-2): the register is the literal set PIN-1 to PIN-46; PIN-1 to PIN-43 (LOCK v0.1's
    # 43-entry register) carry the v0.1 marker and PIN-44 to PIN-46 (declared at LOCK v1.0: their text begins so)
    # the v1.0 marker; each site names a register id; no other marker appears anywhere. Each planted control is
    # caught by its own problem, one plant per direction of each set (L2-7); the plants are built by
    # concatenation, so none is a marker in this file
    mk_rx = r"# PIN \(Code, declared at LOCK ([^)\n]*)\)(?:: (PIN-\d+))?"
    mk_head = "# PIN (Code" + ", declared at LOCK "
    v01_ = {f"PIN-{i_}" for i_ in range(1, 44)}
    v10_ = {"PIN-44", "PIN-45", "PIN-46"}

    def marker_problems(src_: str, pins_: Mapping) -> list[str]:
        by_: dict = {"v0.1": set(), "v1.0": set()}
        probs_ = []
        for ver_, id_ in re.findall(mk_rx, src_):
            if ver_ not in by_:
                probs_.append(f"a marker of LOCK {ver_!r} ({id_ or 'no id'})")
            else:
                by_[ver_].add(id_ or "(no PIN id)")
        for ver_, want_ in (("v0.1", v01_), ("v1.0", v10_)):
            if want_ - by_[ver_]:
                probs_.append(f"{ver_} register ids without their site: {sorted(want_ - by_[ver_])}")
            if by_[ver_] - want_:
                probs_.append(f"{ver_} sites naming no {ver_} register id: {sorted(by_[ver_] - want_)}")
        if (v01_ | v10_) - set(pins_):
            probs_.append(f"the register lacks {sorted((v01_ | v10_) - set(pins_))}")
        if set(pins_) - (v01_ | v10_):
            probs_.append(f"the register has entries beyond PIN-46: {sorted(set(pins_) - (v01_ | v10_))}")
        decl_ = {p_ for p_, t_ in pins_.items() if t_.startswith("Declared at LOCK v1.0")}
        if decl_ != v10_:
            probs_.append(f"the entries declared at LOCK v1.0 are {sorted(decl_)}")
        return probs_

    def unmark(src_: str, ver_: str, pid_: str) -> str:
        old_ = mk_head + ver_ + "): " + pid_ + " --"
        return src_.replace(old_, "# (planted) " + pid_ + " --") if src_.count(old_) == 1 else ""
    real_mk = marker_problems(src, PINS)
    plants = {"a v0.2 marker": (src + mk_head + "v0.2): PIN-96 -- battery\n", PINS, "a marker of LOCK 'v0.2'"),
              "a v2.0 marker": (src + mk_head + "v2.0): PIN-98 -- battery\n", PINS, "a marker of LOCK 'v2.0'"),
              "a v1.1 marker": (src + mk_head + "v1.1): PIN-97 -- battery\n", PINS, "a marker of LOCK 'v1.1'"),
              "a v0.1 site removed": (unmark(src, "v0.1", "PIN-27"), PINS,
                                      "v0.1 register ids without their site: ['PIN-27']"),
              "a new id under v0.1": (src + mk_head + "v0.1): PIN-44 -- battery\n", PINS,
                                      "v0.1 sites naming no v0.1 register id: ['PIN-44']"),
              "a marker naming no id": (src + mk_head + "v0.1): battery\n", PINS,
                                        "v0.1 sites naming no v0.1 register id: ['(no PIN id)']"),
              "a v1.0 site removed": (unmark(src, "v1.0", "PIN-45"), PINS,
                                      "v1.0 register ids without their site: ['PIN-45']"),
              "an old id under v1.0": (src + mk_head + "v1.0): PIN-9 -- battery\n", PINS,
                                       "v1.0 sites naming no v1.0 register id: ['PIN-9']"),
              "a register entry deleted with its site": (unmark(src, "v0.1", "PIN-27"), {
                  k_: v_ for k_, v_ in PINS.items() if k_ != "PIN-27"}, "the register lacks ['PIN-27']"),
              "a planted register id": (src, {**PINS, "PIN-99": "planted (battery)"},
                                        "the register has entries beyond PIN-46: ['PIN-99']"),
              "a new register id declared at v0.1, with its site": (src + mk_head + "v0.1): PIN-47 -- battery\n", {
                  **PINS, "PIN-47": "planted (battery)"}, "the register has entries beyond PIN-46: ['PIN-47']"),
              "a v1.0 entry not declared so": (src, {**PINS, "PIN-45": "Planted: " + PINS.get("PIN-45", "")},
                                               "the entries declared at LOCK v1.0 are ['PIN-44', 'PIN-46']"),
              "a v0.1 entry declared at v1.0": (src, {**PINS, "PIN-27": "Declared at LOCK v1.0 (planted): " + PINS.get(
                  "PIN-27", "")}, "the entries declared at LOCK v1.0 are ['PIN-27', 'PIN-44', 'PIN-45', 'PIN-46']")}
    caught = {k_: bool(s_) and any(x_.startswith(want_) for x_ in marker_problems(s_, p_))
              for k_, (s_, p_, want_) in plants.items()}
    B.chk("PIN register: the register is exactly PIN-1 to PIN-46; PIN-1 to PIN-43 (LOCK v0.1's register) each have "
          "their site marked as declared at LOCK v0.1 and PIN-44 to PIN-46 (their texts declared at LOCK v1.0) theirs "
          "at LOCK v1.0; every site names a register id of its version; no other marker anywhere; each planted "
          "control is caught by its own problem, one per direction of each set (a v0.2 / v2.0 / v1.1 marker; a v0.1 "
          "site removed; a new id and a marker naming no id under v0.1; a v1.0 site removed; an old id under v1.0; a "
          "register entry deleted with its site; a planted register id; a new register id declared at v0.1 with its "
          "site; a v1.0 entry not declared so; a v0.1 entry declared at v1.0)",
          real_mk == [] and all(caught.values()),
          (real_mk[:2], [k_ for k_, v_ in caught.items() if not v_]), cover=["STR-PIN-COMMENTS"])
    # the texts declared at LOCK v1.0 (Code's check; strengthened in round 3, FID2-1): each register text and its
    # site comment says "Code's reading"; every mention of the seat in them begins one of three declared forms
    # (seat_forms_ below: 'the seat's round-2 item 3 (', '(the seat: "no analyzer reads prose")', 'the seat's
    # adjudication'); every quotation in them (a double-quoted fragment; single quotes mark values and names) is
    # found verbatim in a declared seat source -- the battery's copies below of the seat's words (R2 item 3 (a); R2
    # item 3 (b) and (c); R1 C7's bar), markdown emphasis removed and checked against the seat's blocks by Code's
    # scratch quote sweep, as the battery reads nothing under results/raw (PIN-29) -- and each register text quotes
    # the words of the ruling it builds (PIN-44's site comment the ruling too)
    seat_src_ = {
        "R2 item 3 (a)": (
            "(a) C7's posting bar. Build it as: the `posting` command renders PASS/FAIL against the bar (PASS iff the "
            "enumeration under (a), (b) and (c) is empty and the dose note is present iff the flag); and it compares the "
            "posting re-run's enumeration with the VERDICTS enumeration with the PI's rewrites applied (a declared "
            "input: the rewrite list, by row id), reporting any row that differs. The second gap Code names — that the "
            "(a)/(b) result rests on the posted table's declared classification rather than a reading of the text — is "
            "by design: the sentence table, values-checked and hashed where built, is the reading of record (m:278), "
            "and no analyzer reads prose. Until (a) is built nothing is needed, since the posting is after step 17."),
        "R2 item 3 (b), (c)": (
            "(b) a fired end look without a matching pause and (c) the end look's launch count — both built at step 15 "
            "as VERDICTS refusals. They guard the checkpoint against a hand edit; the campaign (step 16) writes no "
            "checkpoint before LOCK v1.0's analyzer is of record, so step 15 is early enough."),
        "R1 C7": (
            "The pass bar for the posting's re-run on the posted text (m:278, m:349). PASS iff, on the posted text, the "
            "analyzer's enumeration under (a), (b) and (c) is empty — no sentence asserting a null on a cell not "
            "Answered, none asserting a thesis above the ceiling obtained — and the dose note is present iff the flag; "
            "the enumeration of record is the VERDICTS one with the PI's rewrites applied, and any residue is listed by "
            "sentence and rewritten before posting. Fixed here, before the v1 posting.")}
    r2_3a = ("the `posting` command renders PASS/FAIL against the bar (PASS iff the enumeration under (a), (b) and (c) "
             "is empty and the dose note is present iff the flag); and it compares the posting re-run's enumeration "
             "with the VERDICTS enumeration with the PI's rewrites applied (a declared input: the rewrite list, by row "
             "id), reporting any row that differs.")
    quotes_ = {"PIN-44": [r2_3a, "no analyzer reads prose", "The pass bar for the posting's re-run on the posted text",
                          "the VERDICTS enumeration"],
               "PIN-45": ["(b) a fired end look without a matching pause", "as VERDICTS refusals",
                          "guard the checkpoint against a hand edit"],
               "PIN-46": ["(c) the end look's launch count", "as VERDICTS refusals",
                          "guard the checkpoint against a hand edit"]}
    seat_forms_ = ("the seat's round-2 item 3 (", "(the seat: \"no analyzer reads prose\")", "the seat's adjudication")

    def ws_(x_: str) -> str:
        return re.sub(r"\s+", " ", x_)

    def site_text(src_l_: list, pid_: str) -> str:
        i_ = next((j_ for j_, l_ in enumerate(src_l_) if (mk_head + "v1.0): " + pid_ + " --") in l_), None)
        if i_ is None:
            return ""
        blk_ = []
        for l_ in src_l_[i_:]:
            if not l_.strip().startswith("#"):
                break
            blk_.append(l_.strip().lstrip("#").strip())
        return " ".join(blk_)

    def v10_problems(src_: str, pins_: Mapping) -> list[str]:
        src_l_ = src_.splitlines()
        ids_ = sorted((p_ for p_, t_ in pins_.items() if t_.startswith("Declared at LOCK v1.0")), key=lambda x: int(x[4:]))
        probs_ = [] if ids_ == ["PIN-44", "PIN-45", "PIN-46"] else [f"the v1.0 entries are {ids_}"]
        for p_ in ids_:
            for where_, tx_ in (("text", pins_[p_]), ("site", site_text(src_l_, p_))):
                if "Code's reading" not in tx_:
                    probs_.append(f"{p_} {where_}: not plainly Code's reading")
                if tx_.count("seat") != sum(tx_.count(f_) for f_ in seat_forms_):
                    probs_.append(f"{p_} {where_}: names the seat beyond citing its ruling or its adjudication")
                for q_ in re.findall(r'"([^"]+)"', tx_):
                    if not any(ws_(q_) in ws_(s_) for s_ in seat_src_.values()):
                        probs_.append(f"{p_} {where_}: quotes {q_[:30]!r}, in no declared seat source")
            probs_ += [f"{p_}: does not quote {q_[:30]!r}" for q_ in quotes_.get(p_, []) if f"\"{q_}\"" not in pins_[p_]]
        if r2_3a not in site_text(src_l_, "PIN-44"):
            probs_.append("PIN-44 site: does not quote the ruling")
        return probs_

    def src_plant(old_: str, new_: str) -> str:
        return src.replace(old_, new_) if src.count(old_) == 1 else ""
    real_v10 = v10_problems(src, PINS)
    q_ = '"'
    pl_v10 = {"a misquoted ruling in PIN-44": (src, {**PINS, "PIN-44": PINS["PIN-44"].replace(
                  "reporting any row that differs", "reporting every row that differs")}, "PIN-44 text: quotes"),
              "a misquoted ruling in PIN-44's site comment": (src_plant(
                  "# rewrite list, by row id), reporting any row" + " that differs.",
                  "# rewrite list, by row id), reporting every row" + " that differs."), PINS, "PIN-44 site: quotes"),
              "a misquoted ruling in PIN-45's site comment": (src_plant(
                  "# fired end look without a matching" + " pause" + q_ + " built",
                  "# fired end look with no matching" + " pause" + q_ + " built"), PINS, "PIN-45 site: quotes"),
              "a quotation in PIN-45 in no seat source": (src, {**PINS, "PIN-45": PINS["PIN-45"] + " (R2: " + q_
                                                                + "an end pause is never ruled in the checkpoint" + q_
                                                                + ")"}, "PIN-45 text: quotes"),
              "a ruling quote unquoted in PIN-45": (src, {**PINS, "PIN-45": PINS["PIN-45"].replace(
                  q_ + "as VERDICTS refusals" + q_, "as VERDICTS refusals")}, "PIN-45: does not quote"),
              "PIN-44's site comment quoting a prefix of the ruling": (src_plant(
                  "reporting any row" + " that differs." + q_ + " Code's readings",
                  "reporting any row" + q_ + " Code's readings"), PINS, "PIN-44 site: does not quote the ruling"),
              "the seat credited in PIN-46": (src, {**PINS, "PIN-46": PINS["PIN-46"].replace(
                  "Code's reading:", "The seat's reading:")}, "PIN-46 text: names the seat"),
              "the seat's round-2 block credited in PIN-46": (src, {**PINS, "PIN-46": PINS["PIN-46"].replace(
                  "Code's round-2 block", "the seat's round-2 block")}, "PIN-46 text: names the seat"),
              "the seat credited beside Code's reading in PIN-45": (src, {**PINS, "PIN-45": PINS["PIN-45"]
                                                                          + " The seat's reading: (battery)."},
                                                                    "PIN-45 text: names the seat"),
              "PIN-45 not plainly Code's reading": (src, {**PINS, "PIN-45": PINS["PIN-45"].replace(
                  "Code's reading", "A reading")}, "PIN-45 text: not plainly Code's reading"),
              "PIN-46's site comment not plainly Code's reading": (src_plant(
                  "# hand edit" + q_ + ". Code's reading: wherever campaign.end_look",
                  "# hand edit" + q_ + ". A reading: wherever campaign.end_look"), PINS,
                  "PIN-46 site: not plainly Code's reading"),
              "PIN-46's site comment crediting the seat": (src_plant(
                  "# branch, so each refusal" + " shows its own message.",
                  "# branch, so each refusal" + " shows its own message. The seat's reading (battery)."), PINS,
                  "PIN-46 site: names the seat")}
    caught_v10 = {k_: bool(s_) and any(x_.startswith(want_) for x_ in v10_problems(s_, p_))
                  for k_, (s_, p_, want_) in pl_v10.items()}
    only_v10 = ("a ruling quote unquoted in PIN-45", "PIN-44's site comment quoting a prefix of the ruling")
    B.chk("PIN register (Code's check; strengthened in round 3): the texts declared at LOCK v1.0 (PIN-44, -45, -46) and "
          "their site comments each say \"Code's reading\"; every mention of the seat in them begins one of three "
          "declared forms ('the seat's round-2 item 3 (', '(the seat: \"no analyzer reads prose\")', 'the seat's "
          "adjudication'); every quotation in them (a double-quoted fragment) is found verbatim in a declared seat "
          "source (the battery's copies of R2 item 3 (a), R2 item 3 (b)/(c) and R1 C7's bar, checked against the "
          "seat's blocks by Code's scratch sweep); each register text quotes the words of the ruling it builds, "
          "PIN-44's site comment the ruling too; each planted control is caught by its own problem (a misquote in "
          "PIN-44's text and site comment and in PIN-45's site comment; a quotation in no seat source; a ruling "
          "quote unquoted in PIN-45 and PIN-44's site comment quoting a prefix of the ruling, each caught only by "
          "its own problem; the seat credited in PIN-46, with Code's round-2 block, and beside Code's reading in "
          "PIN-45 and in PIN-46's site comment; \"Code's reading\" removed from PIN-45's text and from PIN-46's site "
          "comment)",
          real_v10 == [] and all(caught_v10.values())
          and all(len(v10_problems(*pl_v10[k_][:2])) == 1 for k_ in only_v10),
          (real_v10[:2], [k_ for k_, v_ in caught_v10.items() if not v_],
           {k_: v10_problems(*pl_v10[k_][:2]) for k_ in only_v10}), cover=["STR-PIN-V10-TEXTS"])
    B.chk("insulation: the quarantined state-present module is not in sys.modules",
          not any(m in sys.modules for m in guard.FORBIDDEN_MODULES), cover=["STR-INSULATED"])


def lazy_import_problems(tree: ast.Module) -> list[tuple[str, list[str]]]:
    """valence_core imports outside the declared sets: at module level (any nesting outside a def or
    class) only MODULE_LEVEL_IMPORTS; inside a def or class outside the battery only
    LAZY_VERDICT_MODULES ('<module>' names a module-level offender)."""
    bad = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Import, ast.ImportFrom)):
            continue
        names = ([a.name for a in node.names] if isinstance(node, ast.Import)
                 else [f"{node.module}.{a.name}" if node.module else a.name for a in node.names])
        vc = [n for n in names if n.startswith("valence_core")]
        if not vc:
            continue
        fn = _enclosing(tree, node)
        if fn == "":
            if not all(n in MODULE_LEVEL_IMPORTS for n in vc):
                bad.append(("<module>", vc))
            continue
        if fn.startswith("_bt") or fn in ("_Camp", "_Battery", "_OpenHook"):
            continue
        if not all(n in LAZY_VERDICT_MODULES for n in vc):
            bad.append((fn, vc))
    return bad


def _enclosing(tree: ast.Module, target: ast.AST) -> str:
    """The name of the top-level def / class that contains ``target`` ('' at module level)."""
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and any(sub is target for sub in ast.walk(node)):
            return node.name
    return ""


def battery() -> dict:
    """Run every group; returns the summary (counts, coverage, sha, tallies)."""
    B = _Battery()
    snap0 = _bt_snapshot()
    with _OpenHook() as hook:
        pb = (REPO / PROPOSAL_REL).read_bytes()
        B.chk("proposal: sha256 is the pinned v1.11's (42ab36ec...6c6b)", _sha256_bytes(pb) == PROPOSAL_SHA256,
              _sha256_bytes(pb)[:16], cover=["STR-PROPOSAL-SHA"])
        lines = pb.decode("utf-8").splitlines()
        try:
            _BT_STATE["closure"] = closure()
            _BT_STATE["closure_sha256"] = closure_sha256(_BT_STATE["closure"])
        except (Exception, SystemExit) as e:                      # noqa: BLE001
            _BT_STATE["closure"] = {"modules": {}, "data": {}}
            _BT_STATE["closure_sha256"] = "0" * 64
            B.chk("closure: computed", False, f"{type(e).__name__}: {e}")
        _BT_STATE["package_sha256"] = resume.package_sha256()
        B.group("outcomes", lambda: _bt_outcomes(B))
        B.group("power", lambda: _bt_power(B))
        B.group("sentences", lambda: _bt_sentences(B))
        B.group("not-run / pending", lambda: _bt_notrun(B))
        table = {}

        def tab():
            table.update(_bt_table(B))
        B.group("sentence table", tab)
        B.group("tuples", lambda: _bt_tuples(B, table or placeholder_table()))
        B.group("flag", lambda: _bt_flag(B))
        B.group("counters", lambda: _bt_counters(B, lines))
        B.group("secondaries", lambda: _bt_secondaries(B))
        B.group("campaign counts", lambda: _bt_counts_path(B))
        B.group("reader path", lambda: _bt_reader(B))
        B.group("structure", lambda: _bt_structure(B, lines, hook))
    snap1 = _bt_snapshot()
    B.chk("the battery wrote nothing canonical (data/m before == after; blocked dirs by os.stat only)",
          snap0 == snap1, sorted(set(snap0.items()) ^ set(snap1.items()))[:2], cover=["STR-NO-CANONICAL-WRITE"])
    unreached = sorted(REQUIRED_COVERAGE - B.reached)
    B.chk(f"coverage: every one of the {len(REQUIRED_COVERAGE)} required ids reached", unreached == [], unreached[:4])
    n_ok, n = sum(B.results), len(B.results) + 1
    count_ok = n == EXPECTED_CHECKS
    B.chk(f"check count {n} == EXPECTED_CHECKS {EXPECTED_CHECKS} (a skipped assertion is a failure)", count_ok, n)
    n_ok = sum(B.results)
    print(f"  {n_ok}/{n} m_analyze battery checks pass", flush=True)
    return {"checks_pass": n_ok, "checks_total": n, "expected_checks": EXPECTED_CHECKS,
            "ok": n_ok == n and count_ok and not unreached, "coverage_ids": sorted(B.reached),
            "outputs_sha256": B.extra.get("outputs_sha256"), "tallies": B.extra.get("tallies"),
            "flag_of_record": B.extra.get("flag_of_record"), "closure": _BT_STATE.get("closure"),
            "closure_sha256": _BT_STATE.get("closure_sha256")}


# --- ganl -------------------------------------------------------------------------------------------
def ganl_commit_problems(committed: Callable[[Path], tuple[list[str], bytes | None]], cl: Mapping) -> list[str]:
    """PIN-39's files: the analyzer, the placeholder, the proposal, valence_core/m/*.py and the closure."""
    rels = ([ANALYZER_REL, PLACEHOLDER_REL, PROPOSAL_REL]
            + sorted(_repo_rel(f) for f in (REPO / "valence_core" / "m").glob("*.py"))
            + sorted(cl["modules"]) + sorted(cl["data"]))
    return [x for rel in rels for x in committed(REPO / rel)[0]]


def run_ganl(out: str | None) -> int:
    canonical = REPO / GATES_REL
    if out is None or Path(out).expanduser().resolve() == canonical.resolve():
        dest = canonical
        # PIN (Code, declared at LOCK v0.1): PIN-39 -- the artifact of record is written against committed
        # blobs only (rule 27): the analyzer, the placeholder, the proposal, every valence_core/m/*.py
        # (package_sha256's files) and every closure file must be committed at HEAD with identical
        # working-tree bytes, or `ganl` refuses (exit 2) before the battery; a --out test directory is
        # exempt (non-canonical).
        try:
            probs = ganl_commit_problems(_prod_committed, closure())
        except SystemExit as e:                  # PIN-26: AnlStop (the closure) -> 4, AnlRefusal -> 2
            print(str(e), file=sys.stderr, flush=True)
            return _exit_of(e)
        if probs:
            print(f"REFUSED: the artifact of record is written against committed blobs only; not committed "
                  f"with identical working-tree bytes: {probs[:4]}{' ...' if len(probs) > 4 else ''}",
                  file=sys.stderr)
            return 2
    else:
        if not str(out).strip():
            print("REFUSED: an empty --out", file=sys.stderr)
            return 2
        try:
            dest = resume.refuse_canonical_out(out)
        except SystemExit as e:
            print(f"REFUSED: {e}", file=sys.stderr)
            return 2
    path = dest / Path(GANL_REL).name
    if path.exists():
        print(f"NOTE: {path.name} exists; the battery runs and the write is write-once (identical or refused)",
              flush=True)
    res = battery()
    if not res["ok"]:
        print("STOP: the battery did not pass; nothing written", file=sys.stderr)
        return 4
    art = ganl_artifact(res)
    probs = ganl_artifact_problems(art, res)
    if probs:
        print(f"STOP: the G-ANL-F0 artifact fails its own content check: {probs[:3]}; nothing written",
              file=sys.stderr)
        return 4
    try:
        st = write_texts_once([(path, art)])
    except AnlRefusal as e:
        print(str(e), file=sys.stderr)
        return 2
    print(f"G-ANL-F0: {st}: {_repo_rel(path)} (sha256 {_sha256_bytes(path.read_bytes())})", flush=True)
    return 0


GANL_KEYS = ("analyzer", "battery", "closure", "closure_sha256", "counters", "decisions_other_states",
             "flag_of_record", "gate_stop_stages", "not_run_vocabulary", "package_sha256", "pending_substates",
             "pins", "placeholder", "proposal", "schema", "seat_routed", "spec", "stage", "templates", "verdict")


def ganl_artifact(res: Mapping) -> dict:
    """The G-ANL-F0 manifest (decision 12): shas, closure, battery counts, coverage, tallies,
    outputs_sha256, flag of record, counters, vocabularies, PINs; no timestamp, no HEAD."""
    ab = Path(__file__).read_bytes()
    pl = (REPO / PLACEHOLDER_REL).read_bytes()
    pb = (REPO / PROPOSAL_REL).read_bytes()
    art = {"schema": GANL_SCHEMA, "stage": "G-ANL-F0", "spec": "PROPOSAL-m v1.11 §3.1 m:278; §8 step 8 m:358",
           "analyzer": {"path": ANALYZER_REL, "sha256": _sha256_bytes(ab), "sha16": _sha256_bytes(ab)[:16]},
           "placeholder": {"path": PLACEHOLDER_REL, "sha256": _sha256_bytes(pl)},
           "proposal": {"path": PROPOSAL_REL, "sha256": _sha256_bytes(pb)},
           "package_sha256": resume.package_sha256(),
           "closure": res["closure"], "closure_sha256": res["closure_sha256"],
           "battery": {"checks_pass": res["checks_pass"], "checks_total": res["checks_total"],
                       "expected_checks": res["expected_checks"], "coverage_ids": res["coverage_ids"],
                       "tuples_per_flag": 1080, "evaluations": 2160, "outputs_sha256": res["outputs_sha256"],
                       "outputs_form": "sha256 over the lines json.dumps({t, flag, outputs}, sort_keys, ensure_ascii "
                                       "False, compact) + newline, flag True then False, t in itertools.product(Q5, O6, "
                                       "O6, O6) order; regenerable byte-identically (not committed)",
                       "tallies": res["tallies"]},
           "flag_of_record": res["flag_of_record"],
           "counters": {s: [d.as_dict() for d in COUNTERS[s]] for s in ("qwen", "olmo")},
           "not_run_vocabulary": NOT_RUN_CAUSES, "gate_stop_stages": {u: list(gate_stop_stages(u)) for u in UNITS},
           "pending_substates": list(PENDING_SUBSTATES),
           "decisions_other_states": {"built_units": list(Q5), "Q-F3": {k_: list(v) for k_, v in QF3_WORDS.items()},
                                      "other_units": list(OTHER_UNITS)},
           "templates": {"sentence": SENTENCE_TEMPLATES, "label_prefixes": {"f0": PFX_F0, "olmo": PFX_O},
                         "labels": {"e2b": LABEL_E2B, "olmo-base": LABEL_BASE, "S1": LABEL_S1, "weight": LABEL_WEIGHT},
                         "abstract": {"all": ABSTRACT_ALL, "some": ABSTRACT_SOME, "none": ABSTRACT_NONE},
                         "titles": TITLES, "s81_tokens": S81_TOKEN},
           "pins": PINS, "seat_routed": SEAT_ROUTED, "verdict": "PASS"}
    return art


def ganl_artifact_problems(art: Mapping, res: Mapping) -> list[str]:
    """The manifest against independently read values: its key set (no timestamp, no HEAD), the
    analyzer / placeholder / proposal bytes on disk, the pinned proposal, package_sha256, the closure
    and its sha, the battery block, the flag of record and the PIN register."""
    probs = []
    if sorted(art) != sorted(GANL_KEYS):
        probs.append(f"keys {sorted(set(art) ^ set(GANL_KEYS))}")
    for k_, rel, src in (("analyzer", ANALYZER_REL, Path(__file__)), ("placeholder", PLACEHOLDER_REL, REPO / PLACEHOLDER_REL),
                         ("proposal", PROPOSAL_REL, REPO / PROPOSAL_REL)):
        blk = art.get(k_) or {}
        if blk.get("path") != rel or blk.get("sha256") != _sha256_bytes(src.read_bytes()):
            probs.append(f"{k_} path / sha256")
    if (art.get("analyzer") or {}).get("sha16") != (art.get("analyzer") or {}).get("sha256", "")[:16]:
        probs.append("analyzer sha16")
    if (art.get("proposal") or {}).get("sha256") != PROPOSAL_SHA256:
        probs.append("proposal sha256 is not the pinned v1.11's")
    if art.get("package_sha256") != resume.package_sha256():
        probs.append("package_sha256")
    if art.get("closure") != res.get("closure") or art.get("closure_sha256") != res.get("closure_sha256") \
            or not isinstance(art.get("closure"), Mapping) or closure_sha256(art["closure"]) != art["closure_sha256"]:
        probs.append("closure / closure_sha256")
    bt = art.get("battery") or {}
    for k_ in ("checks_pass", "checks_total", "expected_checks", "coverage_ids", "outputs_sha256", "tallies"):
        if bt.get(k_) != res.get(k_):
            probs.append(f"battery.{k_}")
    if art.get("flag_of_record") != res.get("flag_of_record"):
        probs.append("flag_of_record")
    if art.get("pins") != PINS or art.get("seat_routed") != SEAT_ROUTED or art.get("schema") != GANL_SCHEMA:
        probs.append("pins / seat_routed / schema")
    return probs


# --- CLI ----------------------------------------------------------------------------------------------
def _exit_of(e: BaseException) -> int:
    # PIN (Code, declared at LOCK v0.1): PIN-26 -- exit codes: --selftest 0/1; ganl 0 written or
    # identical, 2 refused, 4 STOP (its SystemExits, the closure's AnlStop included, map here);
    # verdicts / not-run / posting 0 written or identical, 2 refused (before any pick is
    # interpreted, write-once, exclusivity, or an input that is not a JSON object); posting also 5:
    # FAIL against C7's bar on the posted text's re-run, nothing written (PIN-44; Code's code, added
    # at LOCK v1.0); 4 STOP (and any other SystemExit).
    if isinstance(e, AnlRefusal):
        return 2
    if isinstance(e, AnlPostingFail):
        return 5
    return 4


def main(argv: list[str] | None = None) -> int:
    shown = sys.argv if argv is None else [sys.argv[0]] + list(argv)
    print("INVOCATION: " + " ".join([sys.executable] + shown), flush=True)
    ap = argparse.ArgumentParser(description="PROPOSAL-m analyzer (G-ANL-F0)")
    ap.add_argument("--selftest", action="store_true", help="the synthetic battery (model-free)")
    sub = ap.add_subparsers(dest="cmd")
    g = sub.add_parser("ganl", help="the battery, then data/m/gates/G-ANL-F0.json (write-once)")
    g.add_argument("--out", default=None, help="a non-canonical test directory (default data/m/gates)")
    v = sub.add_parser("verdicts", help="one unit's VERDICTS")
    v.add_argument("--unit", required=True)
    v.add_argument("--lock", required=True)
    v.add_argument("--decisions", required=True)
    for a in ("campaign", "time", "qual", "adjudication", "pi-stop", "olmo-states", "sentences", "flag-source", "out"):
        v.add_argument(f"--{a}", default=None)
    n = sub.add_parser("not-run", help="a Clock / dose NOT-RUN record")
    n.add_argument("--unit", required=True)
    n.add_argument("--record", required=True)
    for a in ("time", "qual", "out"):
        n.add_argument(f"--{a}", default=None)
    p = sub.add_parser("posting", help="§7's v1 outputs under a declared tuple")
    p.add_argument("--posting", required=True, choices=["v1"])
    p.add_argument("--tuple", required=True)
    p.add_argument("--sentences", required=True)
    for a in ("rewrites", "flag-source", "verdicts-dir", "out"):
        p.add_argument(f"--{a}", default=None)
    args = ap.parse_args(argv)
    if args.selftest:
        if args.cmd is not None:
            print("refused: --selftest takes no subcommand", file=sys.stderr)
            return 2
        return 0 if battery()["ok"] else 1
    if args.cmd == "ganl":
        try:
            return run_ganl(args.out)
        except SystemExit as e:                  # PIN-26: never exit 1 (the selftest-FAIL code)
            print(str(e.code if not isinstance(e, (AnlRefusal, AnlStop)) else e), file=sys.stderr, flush=True)
            return _exit_of(e)
    if args.cmd is None:
        ap.print_usage(sys.stderr)
        return 2
    try:
        env = production_env()
        if args.cmd == "verdicts":
            U = args.unit
            ck = REPO / CKPT_REL
            inp = VerdictInputs(unit=U, lock=Path(args.lock), decisions=Path(args.decisions),
                                campaign=Path(args.campaign or ck / f"{U}_campaign.json"),
                                time=Path(args.time or ck / f"{U}_time.json"), qual=Path(args.qual or ck / f"{U}_qual.json"),
                                out=Path(args.out or REPO / VERDICTS_REL),
                                adjudication=Path(args.adjudication) if args.adjudication else None,
                                pi_stop=Path(args.pi_stop) if args.pi_stop else None,
                                olmo_states=Path(args.olmo_states) if args.olmo_states else None,
                                sentences=Path(args.sentences) if args.sentences else None,
                                flag_source=Path(args.flag_source) if args.flag_source else None)
            st, lines, _ = run_verdicts(inp, env)
        elif args.cmd == "not-run":
            st, lines, _ = run_not_run(args.unit, Path(args.record), Path(args.time) if args.time else None,
                                       Path(args.qual) if args.qual else None,
                                       Path(args.out or REPO / VERDICTS_REL), env)
        else:
            st, lines, _ = run_posting(Path(args.tuple), Path(args.sentences),
                                       Path(args.flag_source or REPO / FLAG_SOURCE_REL),
                                       Path(args.verdicts_dir or REPO / VERDICTS_REL),
                                       Path(args.out or REPO / VERDICTS_REL), env,
                                       rewrites=Path(args.rewrites) if args.rewrites is not None else None)
    except AnlPostingFail as e:                  # PIN-26 / PIN-44: the FAIL's record on stdout, exit 5
        for ln in e.lines:
            print(ln, flush=True)
        return _exit_of(e)
    except SystemExit as e:
        print(str(e.code if not isinstance(e, (AnlRefusal, AnlStop)) else e), file=sys.stderr, flush=True)
        return _exit_of(e)
    for ln in lines:
        print(ln, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
