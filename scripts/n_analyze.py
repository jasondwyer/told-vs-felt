#!/usr/bin/env python3
"""PROPOSAL-n's analyzer -- G-ANL-n (PROPOSAL-n v0.2 §3 "G-ANL-n", §4, §5, §7; §8 step 9), for N-pod.

Committed before LOCK-n v0.1 and before any N-pod read; VERDICTS are computed by this pre-committed analyzer before any
of "the reads" (n §4 "Blinding", m:318's form). MODEL-FREE BY DESIGN: numpy and the standard library only at module
level. The read runner's record schema (valence_core/n/schema.py, pinned by sha256) is imported lazily, on the reading
path and in the battery, and the battery imports valence_core.m.keys lazily to cross-check m:159's stream function.

Layers: (1) numerics -- §4's statistics (Δm, the session bootstrap, the per-session OLS slope, the floor, L(d), P(d));
(2) the outcome layer -- §5 in its order: the unit (NOT-RUN by cause), N1, dose, N2, N4, with G-LEAK-n's certification
and G-READ-n's states as inputs; (3) the sentence layer -- one §7 sentence set per outcome tuple: 7.1 N1's sentence,
7.2 the dose sentence, 7.3 N2's descriptive line, and N4's line, each with its §0.6 label where its outcome is a null;
(4) the reader -- the campaign's cell files through the schema's own checks, the cross-record checks the schema leaves
to the analyzer, the declared read plan re-derived; (5) counters (rule 23) and secondaries (§4 (a)-(f)).

Code's readings are registered in PINS (each strikable by the seat until LOCK-n v1.0); the seat's open questions
(results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md, Q1-Q9) in OPEN, each carried meanwhile and tagged
"pending the seat" in the battery's lines that test it. G-ANL-n's canonical run waits for the seat's answers.

  --selftest            the battery (model-free); prints "  [PASS|FAIL] name got" per check; exit 0 iff every check
                        passes, the count equals EXPECTED_CHECKS and every coverage id is reached (n §3: "a skipped
                        assertion is a failure").
  ganl [--out DIR] [--dose-map P]
                        the battery, then data/n/gates/G-ANL-n.json, write-once, its bound files committed and the
                        pinned dose map (G-CAL-n's figures) required canonically; --out DIR outside the repository is
                        a test run, never of record. Exit 0 written or identical, 2 refused, 4 STOP.
  not-run --record R [--out DIR]
                        N-pod's NOT-RUN output (data/n/verdicts/N-pod_NOT-RUN.json, write-once) from a NOT-RUN
                        record (n §5 "Unit outcome first"), written of record only by the committed analyzer; --out DIR
                        outside the repository is a test run, never of record. Exit 0 written or identical, 2 refused.
  The verdicts command reads the campaign's stage report and G-READ-n's artifact; it is added when their forms are
  committed (n-build's package).
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
import zlib
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

import numpy as np

REPO = Path(__file__).resolve().parents[1]                     # scripts/n_analyze.py -> the repository

# =====================================================================================================================
# 1. Pins and constants
# =====================================================================================================================
PROPOSAL_REL = "PROPOSAL-n-bk-reconciliation-v0_2.md"
PROPOSAL_SHA256 = "30a3d0f55a6681e01245f75490d1f7fdf032b4a1f2c6e59684d6a17584b104f4"
ANALYZER_REL = "scripts/n_analyze.py"
UNIT = "N-pod"
D_N = "2026-12-15"                    # §7.4; the routing of 2026-11-06 ("Everything else as the 11-05 routing had it")
BK_NP_REL = "data/n/bk/experiment_results_json/fixed_text_design/neutral_passages"
TAU = 0.017883544377937845            # BK prereg.json "tau" (n §2.1; G-DATA (vi)); verified against the file
TAU_SENS = TAU / 4                    # §2.1 "a sensitivity row drops reads above TAU/4"
BAR_I = 0.545                         # §5 N1 (i): "the mean Δm at d = +1 ≥ 0.545 nats" (half of BK's 1.09)
DEAD_BAR = 0.5                        # §5 N4: "DEAD iff the CI's upper bound < 0.5 nats"
B_BOOT = 4000                         # §4: "a 95% session-bootstrap CI (4,000 resamples, seed in the lock)"
PCT95 = (2.5, 97.5)
PCT98 = (1.0, 99.0)                   # §4: N4's "98% two-sided session-bootstrap CI (one-sided .01)"
FLOOR_EVENTS = 20                     # §4 secondaries: "decidable-n floor 20 events" (rule 28(a))
MERGE_TOL = 0.05                      # §2.3: "a point within 0.05 of an existing one is merged"
N_RANDOM = 24
BK_FULL = (1.0, 0.5, 0.0, -1.0)       # N1-V's BK-grid points under A1 "struck beyond d = −1" (§2.4; routing 2026-11-06)

ARMS = ("N1-V", "N1-R", "N1-P", "N2-E", "N2-S", "N2-C", "N4-T", "N4-Ts")
N1_ARMS = ("N1-V", "N1-R", "N1-P")
N4_ARMS = ("N4-T", "N4-Ts")
N1P_POINTS = (1.0, -1.0)                   # §2.4: N1-P reads +1 and −1 only
N2_ARMS = ("N2-E", "N2-S", "N2-C")
N1_STATES = ("REPLICATED", "PARTIAL", "NOT-REPLICATED", "INDETERMINATE")
DOSE_STATES = ("DETECTABLE", "NOT-DETECTABLE", "INDETERMINATE")
N2_STATES = ("SPECIFIC", "SHARED", "NULL", "INDETERMINATE")
N4_STATES = ("PASS", "REVERSE", "DEAD", "INDETERMINATE")
GREAD_STATES = ("PASS", "FAIL")
NOT_RUN = "NOT-RUN"
ANSWERED = "answered"                       # §5 (n:136, n:138, n:142), verbatim
CNA = "concluded, not answered"            # §0.6, §5, verbatim
NO_READ = "no read obtained"                # §5 N4, verbatim
F10, F20 = "f=0.10", "f=0.20"

# NOT-RUN causes (§5 "Unit outcome first"): LOCK v1.0 not committed by D_n -- "(no box; a gate STOPPED and no
# re-specification was locked; the PI declined v1.0 for any reason)" -- or locked and "produces no arm's full read set
# before a PI stop, a G-VER STOP or its cap".
NOT_RUN_CAUSES = {
    "clock:no-box": "LOCK-n v1.0 was not committed by its Clock date ({date}): no box",
    "clock:gate-stopped": "LOCK-n v1.0 was not committed by its Clock date ({date}): {stage} STOPPED and no "
                          "re-specification was locked",
    "clock:pi-declined": "LOCK-n v1.0 was not committed by its Clock date ({date}): the PI declined v1.0",
    "clock:not-locked": "LOCK-n v1.0 was not committed by its Clock date ({date})",
    "no-arm:pi-stop": "locked, and no arm's full read set was produced before a PI stop",
    "no-arm:gver-stop": "locked, and no arm's full read set was produced before a G-VER STOP",
    "no-arm:cap": "locked, and no arm's full read set was produced before its cap",
}
GATE_STAGES = ("G-DATA (n)", "G-ACQ (n)", "G-VEC (n)", "G-CAL-n", "G-ANL-n", "G-TIME-n", "G-VER (n)")  # §3, pre-lock

# =====================================================================================================================
# 2. Numerics (§4)
# =====================================================================================================================


class AnlRefusal(SystemExit):
    """Refused before any read is interpreted (exit 2)."""


class AnlStop(SystemExit):
    """A content assertion failed after reading (exit 4)."""


def key_stream(key: str) -> np.random.Generator:
    """m:159's key-to-generator function, re-implemented (no repository import): default_rng(crc32(key) % 2**31).
    The battery asserts it equals valence_core.m.keys.stream and numpy's f|CORR|0 known answer."""
    return np.random.default_rng(zlib.crc32(key.encode()) % 2 ** 31)


def boot_key(arm: str) -> str:
    # PIN (Code, declared at G-ANL-n): PIN-n-12 -- one resample matrix per arm, from the stream "n-boot|{arm}" under
    # m:159's function: B = 4,000 rows of integers(0, n) over the arm's sessions in session-index order; every
    # statistic of the arm (each dose point, the slope) uses the same matrix -- in the TAU/4 row, where the counts
    # differ, each statistic draws the arm's stream at its own count; CIs are percentile intervals with linear
    # interpolation (95%: 2.5/97.5; N4's 98%: 1/99). The lock states this as §4's "seed in the lock".
    return f"n-boot|{arm}"


def boot_index(arm: str, n: int, b: int = B_BOOT) -> np.ndarray:
    if n < 1:
        raise AnlStop(f"STOP: a bootstrap over {n} sessions ({arm})")
    return key_stream(boot_key(arm)).integers(0, n, size=(b, n))


@dataclass(frozen=True)
class Est:
    """An estimate: the session mean and its session-bootstrap interval (level in percent)."""
    mean: float
    lo: float
    hi: float
    level: int = 95

    def excludes0(self) -> bool:
        # PIN-n-8: "its CI excluding 0" -- the interval lies wholly on one side of 0 (lo > 0 or hi < 0); an endpoint
        # at exactly 0 does not exclude it. Either side, as §5 is written (a negative effect can exclude 0).
        return self.lo > 0.0 or self.hi < 0.0

    def as_json(self) -> dict:
        return {"mean": self.mean, "ci": [self.lo, self.hi], "level": self.level}


def pct_interval(samples: np.ndarray, pct: tuple[float, float]) -> tuple[float, float]:
    lo, hi = np.percentile(np.asarray(samples, float), list(pct), method="linear")
    return float(lo), float(hi)


def mean_est(values: Sequence[float], idx: np.ndarray, pct: tuple[float, float] = PCT95) -> Est:
    v = np.asarray(values, float)
    if v.ndim != 1 or idx.shape[1] != v.shape[0]:
        raise AnlStop(f"STOP: a bootstrap matrix over {idx.shape[1]} sessions for {v.shape[0]} values")
    if not np.all(np.isfinite(v)):
        raise AnlStop("STOP: a nonfinite value in a statistic's input (§6: NaN/inf is a pause, never a silent drop)")
    lo, hi = pct_interval(v[idx].mean(axis=1), pct)
    return Est(float(v.mean()), lo, hi, int(round(pct[1] - pct[0])))


def sd0(values: Sequence[float]) -> float:
    """C6: population SD (ddof 0)."""
    return float(np.asarray(values, float).std(ddof=0))


def session_slopes(points: Sequence[float], dm: np.ndarray) -> np.ndarray:
    """§4: per session, the OLS slope of Δm on d over the arm's own dose points. OPEN-Q1 (pending the seat): OLS with an
    intercept, over every point the arm lists, d = 0 included where it is listed with Δm(0) = 0 by construction (BK's
    prereg "primary": "over the five points ... d is identically zero at dose 0"; no source says "intercept")."""
    x = np.asarray(points, float)
    y = np.asarray(dm, float)
    if y.ndim != 2 or y.shape[1] != x.shape[0] or x.shape[0] < 2:
        raise AnlStop(f"STOP: a slope over {x.shape[0]} points for values of shape {y.shape}")
    xc = x - x.mean()
    den = float(xc @ xc)
    if den <= 0.0:
        raise AnlStop("STOP: a slope over a single distinct dose point")
    return (y - y.mean(axis=1, keepdims=True)) @ xc / den


def pearson_r(x: Sequence[float], y: Sequence[float]) -> float | None:
    """PIN-n-18: secondary (d), Pearson's r between the retention interval and Δm at +1 over N1-V's sessions; None
    where either side has no spread."""
    a, b = np.asarray(x, float), np.asarray(y, float)
    if a.shape != b.shape or a.ndim != 1 or a.shape[0] < 2:
        raise AnlStop(f"STOP: a correlation over shapes {a.shape} and {b.shape}")
    ac, bc = a - a.mean(), b - b.mean()
    den = math.sqrt(float(ac @ ac) * float(bc @ bc))
    return None if den == 0.0 else float(ac @ bc) / den


LABEL_MASS_FLOOR = 0.20       # PIN-n-17: the label-mass counter's floor (n:99's reference for N-lap; m:283)


def label_mass_below(masses: Sequence[float]) -> int:
    """§4's counter "label-mass floors on the restricted read" (PIN-n-17): restricted reads whose two-label mass is
    below .20."""
    return sum(1 for m_ in masses if float(m_) < LABEL_MASS_FLOOR)


# =====================================================================================================================
# 3. The dose map (§2.3)
# =====================================================================================================================


RHO = 0.3                              # §2.3: ρ = 0.30 (BK Table A2)
BK_LABEL = {1.0: "+1", 0.5: "+1/2", 0.0: "0", -1.0: "-1"}
SCHEMA_LABEL = {"d_20": "+d_20", "d_eq": "+d_eq"}   # n-build's record labels for the two added points


@dataclass(frozen=True)
class DoseMap:
    """d_eq and d_20 as G-CAL-n pins them (§2.3), and N1-V's realised points after the merge rule. rho, R and R_ell,
    when given (the stage identity's), are checked against §2.3's formulas exactly."""
    d_eq: float
    d_20: float
    rho: float | None = None
    R: float | None = None
    R_ell: float | None = None

    def problems(self) -> list[str]:
        p = []
        if not (math.isfinite(self.d_eq) and self.d_eq > 0.0):
            return [f"d_eq {self.d_eq!r} is not a positive number"]
        if self.d_20 != min(1.0, 2.0 * self.d_eq):
            p.append(f"d_20 {self.d_20!r} is not min(1.0, 2.0 * d_eq) = {min(1.0, 2.0 * self.d_eq)!r} (§2.3)")
        if self.rho is not None or self.R is not None or self.R_ell is not None:
            if self.rho != RHO:
                p.append(f"rho {self.rho!r} is not §2.3's 0.3")
            elif not (isinstance(self.R, float) and isinstance(self.R_ell, float) and self.R > 0.0 and self.R_ell > 0.0):
                p.append(f"R {self.R!r} / R_ell {self.R_ell!r} are not positive floats")
            elif self.d_eq != (0.10 * self.R_ell) / (self.rho * self.R):
                p.append(f"d_eq {self.d_eq!r} is not (0.10 * R_ell) / (rho * R) = "
                         f"{(0.10 * self.R_ell) / (self.rho * self.R)!r} (§2.3)")
        r = self._resolve()[0]
        for lab in ("d_20", "d_eq"):
            if r[lab] == 0.0:
                p.append(f"{lab} folds into d = 0: a dose at 0 is no dose (refused; the seat's if it ever happens)")
        return p

    def _resolve(self) -> tuple[dict[str, float], list[str]]:
        # PIN-n-14 (§2.3 "a point within 0.05 of an existing one is merged"; n-build's dose_points, agreed
        # 2026-11-15): d_20, then d_eq, each folded into the nearest candidate -- +1, +1/2, 0, −1, then d_20 if it was
        # kept -- at an IEEE-double distance abs(value - candidate) ≤ 0.05, a tie going to the earlier candidate
        # (min over the list in order); a value equal to a candidate is that point (d_20 = 1 under the cap folds into
        # +1). Kept labels are returned in fold order.
        cands = list(BK_FULL)
        out = {"+1": 1.0, "+1/2": 0.5, "0": 0.0, "-1": -1.0}
        kept: list[str] = []
        for label, v in (("d_20", self.d_20), ("d_eq", self.d_eq)):
            near = min(cands, key=lambda q: abs(q - v))
            if abs(near - v) <= MERGE_TOL:
                out[label] = near
            else:
                out[label] = v
                cands.append(v)
                kept.append(label)
        return out, kept

    def expected_points(self) -> list[dict]:
        """The stage identity's dose_map.points as n-build's schema lists them, re-derived independently: '+1', '+1/2',
        '+d_20' (if kept), '+d_eq' (if kept), '-1', 'f0.10', 'f0.20', each {label, value, merged}, a kept point's
        merged listing the labels folded into it in fold order ('0' is never listed)."""
        r, kept = self._resolve()
        folded: dict[str, list[str]] = {}
        for lab in ("d_20", "d_eq"):
            if lab not in kept:
                into = SCHEMA_LABEL["d_20"] if (lab == "d_eq" and "d_20" in kept and r[lab] == r["d_20"]) \
                    else BK_LABEL[r[lab]]
                folded.setdefault(into, []).append(SCHEMA_LABEL[lab])
        order = (["+1", "+1/2"] + [SCHEMA_LABEL[x] for x in ("d_20", "d_eq") if x in kept] + ["-1"])
        val = {"+1": 1.0, "+1/2": 0.5, "-1": -1.0, "+d_20": self.d_20, "+d_eq": self.d_eq}
        pts = [{"label": lab, "value": val[lab], "merged": folded.get(lab, [])} for lab in order]
        return pts + [{"label": "f0.10", "value": 0.10, "merged": []}, {"label": "f0.20", "value": 0.20, "merged": []}]

    def kept_label(self, which: str) -> str:
        """The record label under which d_20's or d_eq's reads are found (a folded point is read under its keeper)."""
        r, kept = self._resolve()
        if which in kept:
            return SCHEMA_LABEL[which]
        if which == "d_eq" and "d_20" in kept and r["d_eq"] == r["d_20"]:
            return SCHEMA_LABEL["d_20"]
        return BK_LABEL[r[which]]

    def resolved(self) -> dict[str, float]:
        return self._resolve()[0]

    def points(self) -> tuple[float, ...]:
        """N1-V's realised dose points, descending, 0 included (§2.4)."""
        return tuple(sorted(set(self.resolved().values()), reverse=True))

    def merged(self) -> dict[str, bool]:
        """Whether d_20 / d_eq is an existing point (merged, or equal to one) rather than a point added to the grid."""
        added = self._resolve()[1]
        return {"d_20": "d_20" not in added, "d_eq": "d_eq" not in added}

    def f_point(self, f: str) -> float:
        """N2's program-scale point on BK's scale: f·R_ℓ/(ρ·R) = d_eq (f = 0.10) or 2·d_eq (f = 0.20)."""
        return {F10: self.d_eq, F20: 2.0 * self.d_eq}[f]

    def norm_matched(self, f: str) -> float:
        """OPEN-Q7: N1-V's (and N1-R's) point matched to N2's f: d_eq's resolved point for f = 0.10, d_20's for
        f = 0.20 -- exact iff 2·d_eq ≤ 1 and no merge moved it; the analyzer reports the ratio."""
        return self.resolved()["d_eq" if f == F10 else "d_20"]

    def match_ratio(self, f: str) -> float:
        return self.f_point(f) / self.norm_matched(f)

    def n2_slope_points(self) -> tuple[tuple[float, float, float], tuple[float, float, float]]:
        """OPEN-Q9 (pending the seat): N2's slope over its points on BK's scale, (0, d_eq, 2·d_eq) with Δm(0) = 0, and
        the points its floor's random reads are taken at, (0, d_eq's point, d_20's point) -- equal unless the cap
        binds or a merge moved a point (reported only; no §5 outcome reads N2's slope)."""
        return ((0.0, self.d_eq, 2.0 * self.d_eq), (0.0, self.norm_matched(F10), self.norm_matched(F20)))


# =====================================================================================================================
# 4. The outcome layer (§5, in its order)
# =====================================================================================================================


def ceiling(L: float, P: float | None) -> float:
    # OPEN-Q2: G-LEAK-n's ceiling max(L(d), P(d)); P(d) exists only where N1-P is read (+1, −1, §2.4), and where it is
    # not read the ceiling is L(d) alone (dose's d_eq, N2's norm-matched point). FLAG for the seat.
    return float(L) if P is None else max(float(L), float(P))


def above(mean: float, ceil: float) -> bool:
    """§3 G-LEAK-n: "A signed valenced effect is certified at d iff |mean Δm_V(d)| > max(L(d), P(d))" (strict)."""
    return abs(float(mean)) > float(ceil)


def certified(mean: float, L: float, P: float | None) -> bool:
    """G-LEAK-n's certification from L and P (each site computes its ceiling once and decides with `above`)."""
    return above(mean, ceiling(L, P))


@dataclass
class State:
    """What the outcome layer reads: per-arm completeness and standing pauses, the estimates of §4, G-READ-n's cells
    and the dose map. Built from the campaign's records by the reader (build_state) or literally by the battery."""
    dmap: DoseMap
    complete: dict[str, bool]
    paused: dict[str, bool]
    V: dict[float, Est] = field(default_factory=dict)        # N1-V per resolved point (95%), 0 excluded
    slope_V: Est | None = None
    floor_V: float | None = None
    L: dict[float, float] = field(default_factory=dict)      # N1-R: max_i |mean Δm_i(d)| per point
    P: dict[float, float] = field(default_factory=dict)      # N1-P: |mean Δm_P(d)| at +1, −1
    E: dict[str, Est] = field(default_factory=dict)          # N2-E per f label
    S: dict[str, Est] = field(default_factory=dict)          # N2-S (guard)
    C: dict[str, Est] = field(default_factory=dict)          # N2-C (guard)
    told: Est | None = None                                  # N4-T: m_told (98%)
    e_sham: float | None = None                              # N4-Ts: E
    gread: dict[tuple[str, Any], str] = field(default_factory=dict)   # (axis, point|f) -> PASS / FAIL / NOT-COMPUTED
    # why an arm is not usable, beside `complete` (the reader's; the battery's literal states set `complete` only):
    missing: dict[str, int] = field(default_factory=dict)             # planned reads absent
    nonfinite: dict[str, int] = field(default_factory=dict)           # PIN-n-20: present reads that are not finite
    unusable: dict[str, str] = field(default_factory=dict)            # another reason: "shadow", "tau4-emptied"

    def gr(self, axis: str, key: Any) -> str:
        # PIN-n-11: a G-READ-n cell absent or not computed is "not PASS" for §0.6 (reported as NOT-COMPUTED).
        return self.gread.get((axis, key), "NOT-COMPUTED")


def _causes(st: State, arms: Sequence[str]) -> list[str]:
    """An arm's INDETERMINATE causes, in this order: a standing pause; then, for an arm not usable, what the reader
    found -- reads absent (incomplete), reads non-finite (PIN-n-20), or another reason (its shadows, `shadow`; the
    TAU/4 row emptying it, `tau4-emptied`) -- else `incomplete` (the battery's literal states)."""
    out = [f"pause:{a}" for a in arms if st.paused.get(a)]
    for a in arms:
        if st.complete.get(a):
            continue
        why = ([f"incomplete:{a}"] if st.missing.get(a) else []) + ([f"nonfinite:{a}"] if st.nonfinite.get(a) else []) \
            + ([f"{st.unusable[a]}:{a}"] if st.unusable.get(a) else [])
        out += why or [f"incomplete:{a}"]
    return out


def n1_outcome(st: State) -> dict:
    """§5 N1. INDETERMINATE iff an unadjudicated pause stands on N1's reads, or N1-R or N1-P is incomplete; OPEN-Q6:
    N1-V incomplete too (§5: "An arm with a partial read set is INDETERMINATE"); then REPLICATED / PARTIAL /
    NOT-REPLICATED on conjuncts (i)-(iv)."""
    causes = _causes(st, N1_ARMS)
    if causes:
        return {"state": "INDETERMINATE", "causes": causes}
    v1, vm1 = st.V[1.0], st.V[-1.0]
    ceil1 = ceiling(st.L[1.0], st.P.get(1.0))
    c = {"i": v1.mean >= BAR_I and v1.excludes0(),
         "ii": st.slope_V.mean > st.floor_V,                 # PIN-n-7: signed "exceeds" (floor ≥ 0)
         "iii": above(v1.mean, ceil1),
         "iv": vm1.mean < 0.0 and vm1.excludes0(),           # PIN-n-19: the −1 pole is read (A1), so (iv) is evaluated
         "ci+1": v1.excludes0()}
    if c["i"] and c["ii"] and c["iii"] and c["iv"]:
        state, failing = "REPLICATED", []
    elif c["ii"] and c["iii"] and c["ci+1"]:
        state, failing = "PARTIAL", [k for k in ("i", "iv") if not c[k]]
    else:
        state, failing = "NOT-REPLICATED", [k for k in ("ci+1", "ii", "iii") if not c[k]]
    return {"state": state, "conjuncts": c, "failing": failing, "ceiling": ceil1}


def dose_outcome(st: State, n1: Mapping) -> dict:
    """§5 Dose. INDETERMINATE iff N1 is INDETERMINATE or the points are incomplete; DETECTABLE iff the CI at d_eq
    excludes 0 and G-LEAK-n certifies it there; else NOT-DETECTABLE (its §0.6 label set by the sentence layer)."""
    r = st.dmap.resolved()
    causes = []
    if n1["state"] == "INDETERMINATE":
        causes.append("N1-INDETERMINATE")
    if not (st.complete.get("N1-V") and st.complete.get("N1-R")):
        causes.append("incomplete:points")                   # subsumed by N1's causes (OPEN-Q6): reported beside
    if causes:
        return {"state": "INDETERMINATE", "causes": causes}
    deq, d20 = r["d_eq"], r["d_20"]
    v = st.V[deq]
    ceq = ceiling(st.L[deq], st.P.get(deq))
    cert = above(v.mean, ceq)
    c20 = ceiling(st.L[d20], st.P.get(d20))
    state = "DETECTABLE" if (v.excludes0() and cert) else "NOT-DETECTABLE"
    beside = {"point": d20, "est": st.V[d20], "ceiling": c20, "certified": above(st.V[d20].mean, c20)}
    return {"state": state, "point": deq, "ci_excludes0": v.excludes0(), "certified": cert,
            "ceiling": ceq, "d_20_beside": beside}


def n2_outcome(st: State) -> dict:
    """§5 N2, at f = 0.20 (f = 0.10 beside): INDETERMINATE iff an unadjudicated pause stands on N2's reads -- N2-E's,
    N2-S's or N2-C's, as written; OPEN-Q6 (pending the seat): also N2-E, N1-V or N1-R not usable -- and N1-P where the
    norm-matched point is one N1-P reads (d_20 at +1: the cap binds, or 2·d_eq within 0.05 of 1), whose P(+1) the
    ceiling then takes: the arms whose figures its certification reads. SPECIFIC iff span_reward's effect is not
    certified while N1-V's at the norm-matched point is; SHARED iff span_reward's is certified; NULL iff neither. The
    guards decide nothing; a pause on their reads is a pause on N2's reads."""
    m20 = st.dmap.norm_matched(F20)
    reads = ("N2-E", "N1-V", "N1-R") + (("N1-P",) if m20 in N1P_POINTS else ())
    causes = [f"pause:{a}" for a in N2_ARMS if st.paused.get(a)] + \
             [c for c in _causes(st, reads) if not c.startswith("pause:")]
    if causes:
        return {"state": "INDETERMINATE", "causes": causes}
    ceil20 = ceiling(st.L[m20], st.P.get(m20))
    cert_e = above(st.E[F20].mean, ceil20)
    cert_v = above(st.V[m20].mean, ceil20)
    state = "SPECIFIC" if (not cert_e and cert_v) else "SHARED" if cert_e else "NULL"
    m10 = st.dmap.norm_matched(F10)
    c10 = ceiling(st.L[m10], st.P.get(m10))
    beside = {"f=0.10": {"point": m10, "E": st.E.get(F10), "ceiling": c10,
                         "certified": above(st.E[F10].mean, c10) if F10 in st.E else None},
              "guards": {g: {f: est for f, est in d.items()} for g, d in (("span_sentiment", st.S),
                                                                          ("span_character", st.C))}}
    return {"state": state, "point": m20, "ceiling": ceil20, "certified_E": cert_e, "certified_V": cert_v,
            "match_ratio": st.dmap.match_ratio(F20), "beside": beside}


def n4_outcome(st: State) -> dict:
    """§5 N4: INDETERMINATE with no read obtained iff the arm is incomplete or E undefined (OPEN-Q6: or a pause stands
    on N4's reads); else REVERSE, PASS, DEAD, INDETERMINATE (terminal), in that order."""
    causes = _causes(st, N4_ARMS)
    if not causes and (st.e_sham is None or not math.isfinite(st.e_sham)):
        causes.append("E-undefined")
    if causes:
        return {"state": "INDETERMINATE", "no_read": True, "causes": causes}
    t, e = st.told, float(st.e_sham)
    if t.mean < -e and t.excludes0():
        state = "REVERSE"
    elif t.mean > e and t.excludes0():
        state = "PASS"
    elif t.hi < DEAD_BAR:
        state = "DEAD"
    else:
        state = "INDETERMINATE"
    return {"state": state, "no_read": False, "E": e}


def outcomes(st: State) -> dict:
    """§5 in order: N1, dose (reads N1), N2, N4; the tuple's G-READ-n coordinate is valence at d_eq."""
    n1 = n1_outcome(st)
    dose = dose_outcome(st, n1)
    n2 = n2_outcome(st)
    n4 = n4_outcome(st)
    r = st.dmap.resolved()
    grs = {"d_eq": st.gr("valence", r["d_eq"]), "+1": st.gr("valence", 1.0), "E": st.gr("span_reward", F20)}
    return {"N1": n1, "dose": dose, "N2": n2, "N4": n4, "gread": grs,
            "tuple": (n1["state"], dose["state"], n2["state"], n4["state"], "PASS" if grs["d_eq"] == "PASS" else "FAIL")}


# =====================================================================================================================
# 5. The sentence layer (§5's sentences, §7's slots, §0.6's labels)
# =====================================================================================================================
# §5's verbatim templates (n:136, n:138); the battery asserts each is the proposal's italic span, character for
# character. Their bracketed slots are filled at VERDICTS; "theirs 1.09 [1.00, 1.19]" is text, not a slot.
T_N1_REPLICATED = ("BK's fixed-text effect replicates on OLMo-2-32B Instruct in this program's implementation [on their "
                   "/ on a reconstructed direction]: Δm(+1) = [x] nats [CI], theirs 1.09 [1.00, 1.19]; slope [y] "
                   "against a floor of [z]; leak ceiling [max(L, P)]")
T_DOSE_DETECTABLE = ("at d_eq = [value] — this program's f = 0.10 on BK's scale — the effect is [x] nats [CI] above a "
                     "leak ceiling of [c]: dose alone does not account for the program's null on the echo channel")
T_DOSE_ND_ANSWERED = ("at this program's dose the state is readable at the decision (AUC [a]) and the margin does not "
                      "move beyond the leak ceiling: dose is an explanation of record for the program's null")
T_DOSE_ND_NOT_ANSWERED = "…and not readable at the decision: dose is an explanation of record, unresolved"
VERBATIM = {"T_N1_REPLICATED": (136, T_N1_REPLICATED), "T_DOSE_DETECTABLE": (138, T_DOSE_DETECTABLE),
            "T_DOSE_ND_ANSWERED": (138, T_DOSE_ND_ANSWERED), "T_DOSE_ND_NOT_ANSWERED": (138, T_DOSE_ND_NOT_ANSWERED),
            "ANSWERED": (138, ANSWERED), "CNA": (136, CNA), "NO_READ": (142, NO_READ)}

# Code's forms (OPEN-Q8; each a FLAG for the seat's wording, strikable until LOCK-n v1.0): §5 words the cells above
# only; "PARTIAL and NOT-REPLICATED name the failing conjunct and the figures"; INDETERMINATE, NOT-RUN, N2 and N4 carry
# no sentence in §5.
ROUTE_SLOT = "[on their / on a reconstructed direction]"
C_N1_PARTIAL = ("PARTIAL: BK's fixed-text effect on OLMo-2-32B Instruct, in this program's implementation [on their / on "
                "a reconstructed direction], meets (ii) and (iii) and its CI at d = +1 excludes 0, but [failing] fails: "
                "Δm(+1) = [x] nats [CI], theirs 1.09 [1.00, 1.19]; Δm(−1) = [x−] nats [CI−]; slope [y] against a floor "
                "of [z]; leak ceiling [max(L, P)]")
C_N1_NOT_REPLICATED = ("NOT-REPLICATED: BK's fixed-text effect does not replicate on OLMo-2-32B Instruct in this "
                       "program's implementation [on their / on a reconstructed direction]; [failing] fails: Δm(+1) = "
                       "[x] nats [CI], theirs 1.09 [1.00, 1.19]; slope [y] against a floor of [z]; leak ceiling "
                       "[max(L, P)] — [label]")
C_N1_INDET = "INDETERMINATE: N1 is not evaluated ([causes])"
C_DOSE_ND_NOT_READABLE = ("at this program's dose the margin does not move beyond the leak ceiling and the state is not "
                          "readable at the decision: dose is an explanation of record, unresolved")
C_DOSE_ND_READABLE_N4 = ("at this program's dose the state is readable at the decision (AUC [a]) and the margin does not "
                         "move beyond the leak ceiling, but BK's apparatus has not registered an instructed preference "
                         "on this checkpoint (N4 [n4]): dose is an explanation of record, unresolved")
C_DOSE_INDET = "INDETERMINATE: the dose question is not evaluated ([causes])"
N2_HEAD = "N2, descriptive (§7.3; it licenses no thesis sentence): "
C_N2 = {"SPECIFIC": N2_HEAD + ("SPECIFIC: at f = 0.20 this program's evaluative axis (span_reward) does not move BK's "
                               "apparatus beyond the leak ceiling (Δm = [xE] nats against [c]) while the valence direction "
                               "of record at the norm-matched point does (Δm = [xV] nats) — [label]"),
        "SHARED": N2_HEAD + ("SHARED: at f = 0.20 this program's evaluative axis (span_reward) moves BK's apparatus beyond "
                             "the leak ceiling (Δm = [xE] nats [CIE] against [c]); the valence direction of record at the "
                             "norm-matched point: Δm = [xV] nats"),
        "NULL": N2_HEAD + ("NULL: at f = 0.20 neither this program's evaluative axis (span_reward, Δm = [xE] nats) nor "
                           "the valence direction of record at the norm-matched point (Δm = [xV] nats) moves BK's "
                           "apparatus beyond the leak ceiling ([c]) — [label]"),
        "INDETERMINATE": N2_HEAD + "INDETERMINATE: N2 is not evaluated ([causes])"}
C_N4 = {"PASS": ("PASS: BK's apparatus registers an instructed preference on this checkpoint: m_told = [x] nats [CI98] "
                 "against E = [e]; it licenses the answered reading of nulls in this format on this checkpoint (§0.6, "
                 "with G-READ-n), nothing else"),
        "REVERSE": "REVERSE: m_told = [x] nats [CI98] below −E = [-e]",
        "DEAD": "DEAD: the 98% CI's upper bound is below 0.5 nats: m_told = [x] nats [CI98]",
        "INDETERMINATE": "INDETERMINATE: m_told = [x] nats [CI98] against E = [e]",
        "NO-READ": "INDETERMINATE, no read obtained ([causes])"}
C_NOT_RUN = "NOT-RUN: [reason]; no question of PROPOSAL-n v0.2 §1 is answered on N-pod"
SLOTS = ("[on their / on a reconstructed direction]", "[x]", "[CI]", "[y]", "[z]", "[max(L, P)]", "[value]", "[c]",
         "[a]", "[failing]", "[x−]", "[CI−]", "[label]", "[causes]", "[n4]", "[xE]", "[CIE]", "[xV]", "[CI98]", "[e]",
         "[-e]", "[reason]")
CONJUNCT_TEXT = {"i": "conjunct (i) (Δm(+1) ≥ 0.545 nats with its 95% CI excluding 0)",
                 "iv": "conjunct (iv) (Δm(−1) < 0 with its 95% CI excluding 0)",
                 "ci+1": "the 95% CI at d = +1 excluding 0",
                 "ii": "conjunct (ii) (the valenced mean slope above its floor)",
                 "iii": "conjunct (iii) (G-LEAK-n certification at d = +1)"}


def label(n4_state: str, gread_state: str) -> str:
    # OPEN-Q3: §0.6 -- a null read is answered only if (i) the told positive control (N4) PASSED and (ii) G-READ-n
    # PASSED for that axis and dose; else concluded, not answered. Applied to N1 NOT-REPLICATED (valence, +1), dose
    # NOT-DETECTABLE (valence, d_eq) and N2's span_reward null (SPECIFIC, NULL; span_reward, f = 0.20). FLAG.
    return ANSWERED if (n4_state == "PASS" and gread_state == "PASS") else CNA


def failing_text(keys: Sequence[str]) -> str:
    return "; ".join(CONJUNCT_TEXT[k] for k in keys)


def sentence_n1(state: str, *, n4: str, gr1: str, failing: Sequence[str] | None = None,
                causes: Sequence[str] | None = None) -> dict:
    if state == "REPLICATED":
        return {"question": "N1", "state": state, "text": T_N1_REPLICATED, "label": None, "form": "§5"}
    if state == "PARTIAL":
        t = C_N1_PARTIAL if failing is None else C_N1_PARTIAL.replace("[failing]", failing_text(failing))
        return {"question": "N1", "state": state, "text": t, "label": None, "form": "Code"}
    if state == "NOT-REPLICATED":
        lab = label(n4, gr1)
        t = C_N1_NOT_REPLICATED.replace("[label]", lab)
        if failing is not None:
            t = t.replace("[failing]", failing_text(failing))
        return {"question": "N1", "state": state, "text": t, "label": lab, "form": "Code"}
    if state == "INDETERMINATE":
        t = C_N1_INDET if causes is None else C_N1_INDET.replace("[causes]", ", ".join(causes))
        return {"question": "N1", "state": state, "text": t, "label": None, "form": "Code"}
    raise ValueError(f"N1 state {state!r}")


def sentence_dose(state: str, *, n4: str, gr: str, causes: Sequence[str] | None = None) -> dict:
    if state == "DETECTABLE":
        return {"question": "dose", "state": state, "text": T_DOSE_DETECTABLE, "label": None, "form": "§5"}
    if state == "NOT-DETECTABLE":
        lab = label(n4, gr)
        if lab == ANSWERED:
            t, form = T_DOSE_ND_ANSWERED, "§5"
        elif gr != "PASS":
            t, form = C_DOSE_ND_NOT_READABLE, "§5, its ellipsis expanded by Code"
        else:
            t, form = C_DOSE_ND_READABLE_N4.replace("[n4]", n4), "Code"
        return {"question": "dose", "state": state, "text": t, "label": lab, "form": form}
    if state == "INDETERMINATE":
        t = C_DOSE_INDET if causes is None else C_DOSE_INDET.replace("[causes]", ", ".join(causes))
        return {"question": "dose", "state": state, "text": t, "label": None, "form": "Code"}
    raise ValueError(f"dose state {state!r}")


def sentence_n2(state: str, *, n4: str, gre: str, causes: Sequence[str] | None = None) -> dict:
    if state not in N2_STATES:
        raise ValueError(f"N2 state {state!r}")
    t = C_N2[state]
    lab = None
    if state in ("SPECIFIC", "NULL"):
        lab = label(n4, gre)
        t = t.replace("[label]", lab)
    if state == "INDETERMINATE" and causes is not None:
        t = t.replace("[causes]", ", ".join(causes))
    return {"question": "N2", "state": state, "text": t, "label": lab, "form": "Code"}


def sentence_n4(state: str, *, no_read: bool = False, causes: Sequence[str] | None = None) -> dict:
    if state not in N4_STATES:
        raise ValueError(f"N4 state {state!r}")
    key = "NO-READ" if (state == "INDETERMINATE" and no_read) else state
    t = C_N4[key]
    if key == "NO-READ" and causes is not None:
        t = t.replace("[causes]", ", ".join(causes))
    return {"question": "N4", "state": state, "text": t, "label": None, "form": "Code",
            "no_read": bool(key == "NO-READ")}


SLOT_KEYS = ("7.1", "7.2", "7.3", "N4")


def sentence_set(t: Sequence[str] | str, *, gr1: str = "FAIL", gre: str = "FAIL", n4_no_read: bool = False) -> dict:
    """One §7 sentence set for an outcome tuple (template form: figures, causes and the failing conjuncts are slots).
    t = (N1, dose, N2, N4, G-READ-n valence at d_eq) or "NOT-RUN". OPEN-Q4: three inputs that are not coordinates
    change a sentence -- gr1 = G-READ-n (valence, +1), gre = G-READ-n (span_reward, f = 0.20), and n4_no_read (N4's
    INDETERMINATE "with no read obtained" against the terminal one); the battery runs every tuple under each (m's flag
    precedent: an input, not a coordinate)."""
    if t == NOT_RUN:
        s = {"question": "unit", "state": NOT_RUN, "text": C_NOT_RUN, "label": None, "form": "Code"}
        return {k: dict(s) for k in SLOT_KEYS}
    n1, dose, n2, n4, grd = t
    if n1 not in N1_STATES or dose not in DOSE_STATES or n2 not in N2_STATES or n4 not in N4_STATES \
            or grd not in GREAD_STATES or gr1 not in GREAD_STATES or gre not in GREAD_STATES \
            or not isinstance(n4_no_read, bool) or (n4_no_read and n4 != "INDETERMINATE"):
        raise ValueError(f"not a tuple of the outcome space: {t!r} (inputs {gr1!r}, {gre!r}, {n4_no_read!r})")
    return {"7.1": sentence_n1(n1, n4=n4, gr1=gr1), "7.2": sentence_dose(dose, n4=n4, gr=grd),
            "7.3": sentence_n2(n2, n4=n4, gre=gre), "N4": sentence_n4(n4, no_read=n4_no_read)}


def tuple_space() -> list:
    """§3 G-ANL-n: 4 × 3 × 4 × 4 × 2 = 384 tuples, + NOT-RUN = 385."""
    return list(itertools.product(N1_STATES, DOSE_STATES, N2_STATES, N4_STATES, GREAD_STATES)) + [NOT_RUN]


# =====================================================================================================================
# 6. G-LEAK-n's and G-READ-n's tables (reported in VERDICTS; certification per arm x point)
# =====================================================================================================================


def gleak_table(st: State) -> list[dict]:
    """§3 G-LEAK-n, per dose point: L(d), P(d) where N1-P is read, the ceiling, and each valenced arm's certification
    there -- N1-V at each of its realised points (a merged point under every label it carries), N2-E/S/C at their
    norm-matched points. Uncertified effects are reported as such and license no sentence (§3)."""
    r = st.dmap.resolved()
    rows = []
    labels: dict[float, list[str]] = {}
    for lab in ("+1", "+1/2", "d_20", "d_eq", "-1"):
        labels.setdefault(r[lab], []).append(lab)

    def needs(arm: str, pt: float) -> list[str]:
        """The arms whose figures a certification at pt reads (N1-P only where it is read: +1, −1)."""
        return [arm, "N1-R"] + (["N1-P"] if pt in N1P_POINTS else [])
    for pt in sorted(labels, reverse=True):
        miss = [a for a in needs("N1-V", pt) if not st.complete.get(a)]
        if miss:
            rows.append({"arm": "N1-V", "point": pt, "labels": labels[pt], "certified": None,
                         "why": f"incomplete: {', '.join(miss)}"})
            continue
        P = st.P.get(pt)
        c = ceiling(st.L[pt], P)
        rows.append({"arm": "N1-V", "point": pt, "labels": labels[pt], "mean": st.V[pt].mean, "L": st.L[pt], "P": P,
                     "ceiling": c, "certified": above(st.V[pt].mean, c)})
    for arm, d in (("N2-E", st.E), ("N2-S", st.S), ("N2-C", st.C)):
        for f in (F10, F20):
            pt = st.dmap.norm_matched(f)
            miss = [a for a in needs(arm, pt) if not st.complete.get(a)]
            if miss or f not in d:
                rows.append({"arm": arm, "point": pt, "labels": [f], "certified": None,
                             "why": f"incomplete: {', '.join(miss) or arm}"})
                continue
            P = st.P.get(pt)
            c = ceiling(st.L[pt], P)
            rows.append({"arm": arm, "point": pt, "labels": [f], "mean": d[f].mean, "L": st.L[pt], "P": P,
                         "ceiling": c, "certified": above(d[f].mean, c),
                         "match_ratio": st.dmap.match_ratio(f)})
    return rows


GREAD_SECTION5 = {("valence", "+1"): "N1 NOT-REPLICATED's label (§5 N1)",
                  ("valence", "d_eq"): "the dose sentence's label (§5 Dose); the tuple's coordinate",
                  ("span_reward", F20): "N2's span_reward null label (OPEN-Q3)"}


def gread_table(st: State) -> list[dict]:
    """§3 G-READ-n per axis and dose point, as its artifact gives them; the cells that enter §5 (§0.6) marked."""
    r = st.dmap.resolved()
    rows = []
    for lab in ("+1", "+1/2", "d_20", "d_eq", "-1"):
        s = st.gr("valence", r[lab])
        rows.append({"axis": "valence", "point": r[lab], "label": lab, "state": s,
                     "enters": GREAD_SECTION5.get(("valence", lab))})
    for f in (F10, F20):
        rows.append({"axis": "span_reward", "point": st.dmap.f_point(f), "label": f, "state": st.gr("span_reward", f),
                     "enters": GREAD_SECTION5.get(("span_reward", f))})
    return rows


# =====================================================================================================================
# 7. NOT-RUN (§5 "Unit outcome first")
# =====================================================================================================================
NOT_RUN_RECORD_SCHEMA = "n-not-run-v1"


def _iso_date(s: Any) -> bool:
    if not (isinstance(s, str) and len(s) == 10 and s[4] == "-" and s[7] == "-"):
        return False
    try:
        import datetime
        datetime.date.fromisoformat(s)
    except ValueError:
        return False
    return True


def not_run_reason(rec: Mapping) -> str:
    """The NOT-RUN record's reason (its sentence's [reason] slot); refuses a malformed record (AnlRefusal)."""
    probs = []
    if not isinstance(rec, Mapping):
        raise AnlRefusal("REFUSED: a NOT-RUN record is not a JSON object")
    if rec.get("schema") != NOT_RUN_RECORD_SCHEMA:
        probs.append(f"schema {rec.get('schema')!r}")
    if rec.get("unit") != UNIT:
        probs.append(f"unit {rec.get('unit')!r} (n's analyzer writes {UNIT}; N-lap's records wait for its lock)")
    cause = rec.get("cause")
    if cause not in NOT_RUN_CAUSES:
        probs.append(f"cause {cause!r} is not one of {sorted(NOT_RUN_CAUSES)}")
    date = rec.get("date")
    if not _iso_date(date):
        probs.append(f"date {date!r} is not an ISO calendar date")
    elif isinstance(cause, str) and cause.startswith("clock:") and date <= D_N:
        # PIN-n-21: the record's date is the day it is made (PI date); a Clock cause can be recorded only after D_n,
        # which is inclusive (§7.4), so LOCK-n v1.0 can still be committed on D_n itself
        probs.append(f"a Clock cause dated {date}, on or before D_n = {D_N} (inclusive, §7.4): LOCK-n v1.0 can "
                     "still be committed")
    stage = rec.get("stage")
    if cause == "clock:gate-stopped":
        if stage not in GATE_STAGES:
            probs.append(f"stage {stage!r} is not one of {list(GATE_STAGES)}")
    elif stage is not None:
        probs.append("stage given for a cause that names none")
    if not (isinstance(rec.get("detail"), str) and rec["detail"].strip()):
        probs.append("detail missing")
    extra = set(rec) - {"schema", "unit", "cause", "date", "stage", "detail"}
    if extra:
        probs.append(f"unknown keys {sorted(extra)}")
    if probs:
        raise AnlRefusal(f"REFUSED: the NOT-RUN record: {probs}")
    return NOT_RUN_CAUSES[cause].format(date=D_N, stage=stage)


# =====================================================================================================================
# 8. The tuple pass's oracle (an independent second implementation of the selection; §5's verbatim cells read from
#    the proposal file, never from this module's constants)
# =====================================================================================================================


def proposal_spans(text: str) -> dict[str, str]:
    """§5's italic spans at n:136 and n:138, by position, from the proposal's bytes."""
    lines = text.splitlines()

    def spans(n: int) -> list[str]:
        out, s = [], lines[n - 1]
        i = 0
        while True:
            a = s.find("*", i)
            if a < 0:
                break
            if s.startswith("**", a):
                i = a + 2
                continue
            b = s.find("*", a + 1)
            if b < 0:
                break
            if s.startswith("**", b):
                i = b + 2
                continue
            out.append(s[a + 1:b])
            i = b + 1
        return out
    s136, s138 = spans(136), spans(138)
    return {"rep": s136[0], "cna": s136[1], "ans": s138[0], "cna138": s138[1], "det": s138[2], "nd_ans": s138[3],
            "nd_cna": s138[4]}


def oracle_set(t, *, gr1: str, gre: str, n4_no_read: bool, verb: Mapping[str, str]) -> dict:
    if t == NOT_RUN:
        return {k: {"question": "unit", "state": NOT_RUN, "text": C_NOT_RUN, "label": None, "form": "Code"}
                for k in SLOT_KEYS}
    n1, dose, n2, n4, grd = t
    lab = (lambda g: verb["ans"] if (n4 == "PASS" and g == "PASS") else verb["cna"])
    if n1 == "REPLICATED":
        s1 = (verb["rep"], None, "§5")
    elif n1 == "PARTIAL":
        s1 = (C_N1_PARTIAL, None, "Code")
    elif n1 == "NOT-REPLICATED":
        s1 = (C_N1_NOT_REPLICATED.replace("[label]", lab(gr1)), lab(gr1), "Code")
    else:
        s1 = (C_N1_INDET, None, "Code")
    if dose == "DETECTABLE":
        s2 = (verb["det"], None, "§5")
    elif dose == "NOT-DETECTABLE":
        if n4 == "PASS" and grd == "PASS":
            s2 = (verb["nd_ans"], verb["ans"], "§5")
        elif grd == "FAIL":
            s2 = (C_DOSE_ND_NOT_READABLE, verb["cna"], "§5, its ellipsis expanded by Code")
        else:
            s2 = (C_DOSE_ND_READABLE_N4.replace("[n4]", n4), verb["cna"], "Code")
    else:
        s2 = (C_DOSE_INDET, None, "Code")
    if n2 in ("SPECIFIC", "NULL"):
        s3 = (C_N2[n2].replace("[label]", lab(gre)), lab(gre), "Code")
    else:
        s3 = (C_N2[n2], None, "Code")
    s4 = C_N4["NO-READ" if (n4 == "INDETERMINATE" and n4_no_read) else n4]
    out = {}
    for k, q, st, (txt, lb, form) in (("7.1", "N1", n1, s1), ("7.2", "dose", dose, s2), ("7.3", "N2", n2, s3)):
        out[k] = {"question": q, "state": st, "text": txt, "label": lb, "form": form}
    out["N4"] = {"question": "N4", "state": n4, "text": s4, "label": None, "form": "Code",
                 "no_read": bool(n4 == "INDETERMINATE" and n4_no_read)}
    return out


def evaluations() -> list[tuple]:
    """Every (tuple, gr1, gre, n4_no_read) the tuple pass evaluates: 384 tuples x 4 G-READ inputs, x 2 where N4 is
    INDETERMINATE (no read / terminal), + NOT-RUN once = 1,921."""
    out = []
    for t in tuple_space():
        if t == NOT_RUN:
            out.append((t, None, None, False))
            continue
        for gr1, gre in itertools.product(GREAD_STATES, GREAD_STATES):
            for nr in ((False, True) if t[3] == "INDETERMINATE" else (False,)):
                out.append((t, gr1, gre, nr))
    return out


# =====================================================================================================================
# 9. The battery (§3 G-ANL-n). Selftest-only helpers carry the `_bt` prefix.
# =====================================================================================================================
EXPECTED_CHECKS = 171

_REQ: list[str] = []
_REQ += [f"N1-{x}" for x in ("REPLICATED", "PARTIAL-i", "PARTIAL-iv", "PARTIAL-i-iv", "NOTREP-ci+1", "NOTREP-ii",
                             "NOTREP-iii", "NOTREP-ci+1-ii", "NOTREP-ci+1-iii", "NOTREP-ii-iii", "NOTREP-ci+1-ii-iii")]
_REQ += [f"N1-INDET-{k}:{a}" for k in ("pause", "incomplete") for a in N1_ARMS]
_REQ += ["BND-I-EXACT", "BND-I-BELOW", "BND-CI-LO-ZERO", "BND-CI-HI-ZERO", "BND-CERT-EQUAL", "BND-SLOPE-EQ-FLOOR",
         "BND-IV-ZERO", "BND-P-ABOVE-L", "BND-P-ABSENT", "BND-NEG-CERT"]
_REQ += ["DOSE-DET-POS", "DOSE-DET-NEG", "DOSE-ND-CI", "DOSE-ND-UNCERT", "DOSE-INDET-N1", "DOSE-INDET-POINTS",
         "DOSE-BESIDE-D20"]
_REQ += ["N2-SPECIFIC", "N2-SHARED-V-CERT", "N2-SHARED-V-UNCERT", "N2-NULL", "N2-INDET-pause:N2-E",
         "N2-INDET-pause:N2-S", "N2-INDET-pause:N2-C", "N2-NOT-PAUSED-BY-N1",
         "N2-INDET-incomplete:N2-E", "N2-INDET-incomplete:N1-V", "N2-INDET-incomplete:N1-R",
         "N2-INDET-incomplete:N1-P", "N2-GUARDS-DECIDE-NOTHING",
         "N2-F10-BESIDE", "N2-MATCH-RATIO"]
_REQ += ["N4-PASS", "N4-REVERSE", "N4-DEAD", "N4-INDET-TERMINAL", "N4-NOREAD-incomplete:N4-T",
         "N4-NOREAD-incomplete:N4-Ts", "N4-NOREAD-pause:N4-T", "N4-NOREAD-pause:N4-Ts", "N4-NOREAD-E-undefined",
         "N4-ORD-REV-OVER-DEAD", "N4-ORD-PASS-OVER-DEAD", "N4-BND-MEAN-EQ-E", "N4-BND-MEAN-EQ-NEGE",
         "N4-BND-HI-EQ-DEAD", "N4-BND-CI-LO-ZERO"]
_REQ += [f"NR-{c}" for c in NOT_RUN_CAUSES] + ["NR-REFUSE-PREMATURE", "NR-REFUSE-STAGE", "NR-REFUSE-UNIT",
                                                "NR-REFUSE-CAUSE", "NR-REFUSE-KEYS"]
_REQ += [f"GLEAK-{a}-{c}" for a in ("N1-V", "N2-E", "N2-S", "N2-C") for c in ("CERT", "UNCERT", "INCOMPLETE")]
_REQ += [f"GREAD-{c}" for c in ("PASS", "FAIL", "NOT-COMPUTED", "ENTERS-N1", "ENTERS-DOSE", "ENTERS-N2")]
_REQ += ["SENT-VERBATIM", "SENT-FAILING-PARTIAL", "SENT-FAILING-NOTREP", "SENT-CAUSES", "SENT-REFUSES",
         "SENT-CODE-FORMS"]
_REQ += [f"TUP-T{i}" for i in range(1, 11)] + ["TUP-DETERMINISM", "TUP-COUNT"]
_REQ += ["REACH-DOSE-IFF-N1", "REACH-SHAPE-a", "REACH-SHAPE-b", "REACH-SHAPE-d", "REACH-N4-FREE", "REACH-NO-RAISE"]
_REQ += ["NUM-KEYSTREAM-M159", "NUM-KNOWN-ANSWER", "NUM-BOOT-DETERMINISM", "NUM-BOOT-CONSTANT", "NUM-BOOT-LOOP",
         "NUM-PCT-METHOD", "NUM-SLOPE-CLOSED-FORM", "NUM-SLOPE-INTERCEPT", "NUM-SD0", "NUM-NONFINITE-STOP",
         "NUM-BK-REPRO", "NUM-BK-FIDELITY", "NUM-DOSEMAP-SHAPES", "NUM-DOSEMAP-REFUSE",
         "NUM-DOSEMAP-POINTS", "NUM-PEARSON", "CNT-LABEL-MASS", "NUM-N2-POINTS"]
_REQ += ["STR-PROPOSAL-SHA", "STR-VERBATIM-IN-PROPOSAL", "STR-TAU-PREREG", "STR-NO-REPO-IMPORT", "STR-NO-HEAVY",
         "STR-OPEN-HOOK", "STR-NO-CANONICAL-WRITE", "STR-PINS"]
_REQ += ["RD-POSITIVE", "RD-FILLED", "RD-NULL", "RD-SPECIFIC", "RD-PARTIAL", "RD-INDET", "RD-NONFINITE", "RD-MERGED",
         "RD-PAUSE", "RD-GREAD", "RD-SENSITIVITY", "RD-SECONDARY", "RD-REFUSE", "RD-FILLED-FIGURES", "RD-FILLED-FORMS",
         "RD-SHADOW", "RD-ASYM", "RD-MERGED-DEQ", "RD-GREAD-MIXED", "CNT-COUNTERS", "RD-SECONDARY-FLOOR"]
_REQ += ["NUM-DOSEMAP-SCHEMA", "NUM-MERGE-EDGE", "NUM-REACH-CLASS", "CMD-NOTRUN", "CMD-NOTRUN-REFUSE",
         "CMD-GANL-REFUSE", "STR-GANL-ARTIFACT"]
REQUIRED_COVERAGE = frozenset(_REQ)


class _Battery:
    """The check recorder: every chk prints one line; coverage ids are marked as reached."""

    def __init__(self) -> None:
        self.results: list[bool] = []
        self.reached: set[str] = set()
        self.extra: dict = {}

    @staticmethod
    def short(x: Any, n: int = 200) -> str:
        s = " ".join((x if isinstance(x, str) else repr(x)).split())
        return s if len(s) <= n else s[:n - 3] + "..."

    def chk(self, name: str, ok: Any, got: Any = "", cover: Sequence[str] = ()) -> bool:
        ok = bool(ok)
        self.results.append(ok)
        if ok:
            for c in cover:
                if c not in REQUIRED_COVERAGE:
                    raise KeyError(f"coverage id {c!r} is not declared")
                self.reached.add(c)
        tail = "" if (ok or got in ("", None)) else " " + self.short(got)
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
    except (Exception, SystemExit) as e:                              # noqa: BLE001
        return False, f"wrong exception {type(e).__name__}: {e}"
    return False, "no exception"


MAP_A = DoseMap(1 / 3, 2 / 3)          # all points distinct (shape a)
MAP_B = DoseMap(0.72, 1.0)             # d_20 merged into +1 (shape b)
MAP_D = DoseMap(0.97, 1.0)             # d_20 and d_eq merged into +1 (shape d)
_X = Est(1.0, 0.9, 1.1)                # large positive, CI excludes 0, certified at the battery's L 0.05
_Z = Est(0.0, -0.05, 0.05)             # null: CI includes 0, uncertified


def literal_state(dmap: DoseMap = MAP_A, **over) -> State:
    """A complete, unpaused state with every outcome at its 'positive' value (N1 REPLICATED, dose DETECTABLE, N2
    SHARED, N4 PASS) at L = 0.05 everywhere and P = 0.04 at ±1; keyword overrides replace fields. Used by the battery
    and by map_reach, which the canonical `ganl` run calls on the pinned map (hence no `_bt` prefix)."""
    pts = dmap.points()
    st = State(dmap=dmap, complete={a: True for a in ARMS}, paused={a: False for a in ARMS},
               V={p: (Est(-0.7, -0.8, -0.6) if p < 0 else Est(max(p, 0.3), max(p, 0.3) - 0.1, max(p, 0.3) + 0.1))
                  for p in pts if p != 0.0},
               slope_V=Est(0.9, 0.8, 1.0), floor_V=0.3, L={p: 0.05 for p in pts if p != 0.0},
               P={1.0: 0.04, -1.0: 0.04}, E={F10: Est(0.2, 0.1, 0.3), F20: Est(0.3, 0.2, 0.4)},
               S={F10: Est(0.0, -0.1, 0.1), F20: Est(0.0, -0.1, 0.1)}, C={F10: Est(0.0, -0.1, 0.1),
                                                                           F20: Est(0.0, -0.1, 0.1)},
               told=Est(1.0, 0.8, 1.2, 98), e_sham=0.1,
               gread={("valence", p): "PASS" for p in pts if p != 0.0} | {("span_reward", F10): "PASS",
                                                                         ("span_reward", F20): "PASS"})
    for k, v in over.items():
        if k in ("complete", "paused"):
            getattr(st, k).update(v)
        elif k in ("V", "L", "P", "E", "S", "C", "gread"):
            getattr(st, k).update(v)
        else:
            setattr(st, k, v)
    return st


def _bt_outcomes(B: _Battery) -> None:
    o = outcomes(literal_state())
    B.chk("N1 REPLICATED: (i) Δm(+1) 1.0 ≥ 0.545, CI [0.9, 1.1]; (ii) slope 0.9 > floor 0.3; (iii) 1.0 > max(L 0.05, "
          "P 0.04); (iv) Δm(−1) −0.7, CI [−0.8, −0.6]", o["N1"]["state"] == "REPLICATED" and o["N1"]["failing"] == [],
          o["N1"], cover=["N1-REPLICATED"])
    cases = [("PARTIAL-i", {"V": {1.0: Est(0.4, 0.3, 0.5)}}, "PARTIAL", ["i"]),
             ("PARTIAL-iv", {"V": {-1.0: Est(-0.1, -0.2, 0.05)}}, "PARTIAL", ["iv"]),
             ("PARTIAL-i-iv", {"V": {1.0: Est(0.4, 0.3, 0.5), -1.0: Est(0.1, 0.05, 0.15)}}, "PARTIAL", ["i", "iv"]),
             ("NOTREP-ci+1", {"V": {1.0: Est(0.6, -0.1, 1.3)}}, "NOT-REPLICATED", ["ci+1"]),
             ("NOTREP-ii", {"floor_V": 0.95}, "NOT-REPLICATED", ["ii"]),
             ("NOTREP-iii", {"L": {1.0: 2.0}}, "NOT-REPLICATED", ["iii"]),
             ("NOTREP-ci+1-ii", {"V": {1.0: Est(0.6, -0.1, 1.3)}, "floor_V": 0.95}, "NOT-REPLICATED", ["ci+1", "ii"]),
             ("NOTREP-ci+1-iii", {"V": {1.0: Est(0.6, -0.1, 1.3)}, "L": {1.0: 2.0}}, "NOT-REPLICATED", ["ci+1", "iii"]),
             ("NOTREP-ii-iii", {"floor_V": 0.95, "L": {1.0: 2.0}}, "NOT-REPLICATED", ["ii", "iii"]),
             ("NOTREP-ci+1-ii-iii", {"V": {1.0: Est(0.6, -0.1, 1.3)}, "floor_V": 0.95, "L": {1.0: 2.0}},
              "NOT-REPLICATED", ["ci+1", "ii", "iii"])]
    for cid, over, want, failing in cases:
        g = n1_outcome(literal_state(**over))
        B.chk(f"N1 {want} failing {failing}", g["state"] == want and g["failing"] == failing, g, cover=[f"N1-{cid}"])
    for kind in ("pause", "incomplete"):
        for a in N1_ARMS:
            over = {"paused": {a: True}} if kind == "pause" else {"complete": {a: False}}
            g = n1_outcome(literal_state(**over))
            tag = " (OPEN-Q6, pending the seat)" if (kind, a) == ("incomplete", "N1-V") else ""
            B.chk(f"N1 INDETERMINATE by {kind}:{a}{tag}",
                  g["state"] == "INDETERMINATE" and g["causes"] == [f"{kind}:{a}"],
                  g, cover=[f"N1-INDET-{kind}:{a}"])
    # boundaries
    g = n1_outcome(literal_state(V={1.0: Est(BAR_I, 0.4, 0.7)}))
    B.chk("boundary: Δm(+1) exactly 0.545 meets (i) (≥)", g["state"] == "REPLICATED", g, cover=["BND-I-EXACT"])
    g = n1_outcome(literal_state(V={1.0: Est(math.nextafter(BAR_I, 0.0), 0.4, 0.7)}))
    B.chk("boundary: Δm(+1) one ulp below 0.545 fails (i)", g["state"] == "PARTIAL" and g["failing"] == ["i"], g,
          cover=["BND-I-BELOW"])
    g = n1_outcome(literal_state(V={1.0: Est(1.0, 0.0, 2.0)}))
    B.chk("boundary: a CI with lower bound exactly 0 does not exclude 0", g["state"] == "NOT-REPLICATED"
          and g["failing"] == ["ci+1"], g, cover=["BND-CI-LO-ZERO"])
    g = n1_outcome(literal_state(V={-1.0: Est(-0.5, -1.0, 0.0)}))
    B.chk("boundary: a CI with upper bound exactly 0 does not exclude 0 ((iv) fails)", g["failing"] == ["iv"], g,
          cover=["BND-CI-HI-ZERO"])
    g = n1_outcome(literal_state(V={1.0: Est(0.75, 0.7, 0.8)}, L={1.0: 0.75}))
    B.chk("boundary: |Δm(+1)| equal to the ceiling is not certified (strict >)", g["failing"] == ["iii"], g,
          cover=["BND-CERT-EQUAL"])
    g = n1_outcome(literal_state(slope_V=Est(0.3, 0.2, 0.4), floor_V=0.3))
    B.chk("boundary: a slope equal to its floor does not exceed it ((ii) fails)", g["failing"] == ["ii"], g,
          cover=["BND-SLOPE-EQ-FLOOR"])
    g = n1_outcome(literal_state(V={-1.0: Est(0.0, -0.1, 0.1)}))
    B.chk("boundary: Δm(−1) exactly 0 fails (iv) (< 0)", g["state"] == "PARTIAL" and g["failing"] == ["iv"], g,
          cover=["BND-IV-ZERO"])
    g = n1_outcome(literal_state(V={1.0: Est(0.9, 0.8, 1.0)}, L={1.0: 0.5}, P={1.0: 0.95}))
    B.chk("ceiling: P(+1) 0.95 above L(+1) 0.5 governs (0.9 uncertified)", g["failing"] == ["iii"]
          and g["ceiling"] == 0.95, g, cover=["BND-P-ABOVE-L"])
    st = literal_state()
    deq = st.dmap.resolved()["d_eq"]
    d = dose_outcome(literal_state(V={deq: Est(0.08, 0.04, 0.12)}, L={deq: 0.06}), n1_outcome(st))
    B.chk("ceiling (OPEN-Q2, pending the seat): at d_eq, where N1-P is not read, the ceiling is L(d_eq) alone (0.08 > "
          "0.06 certified)",
          d["state"] == "DETECTABLE" and d["ceiling"] == 0.06 and deq not in st.P, d, cover=["BND-P-ABSENT"])
    g = n1_outcome(literal_state(V={1.0: Est(-1.0, -1.1, -0.9)}))
    B.chk("a negative Δm(+1) beyond the ceiling is certified (|mean|); (i) fails, (ii)-(iii) hold, CI excludes 0 -> "
          "PARTIAL (PIN-n-8, as §5 is written)", g["state"] == "PARTIAL" and g["conjuncts"]["iii"] is True
          and g["failing"] == ["i"], g, cover=["BND-NEG-CERT"])
    # dose
    n1 = n1_outcome(literal_state())
    for cid, v, Ld, want in (("DOSE-DET-POS", Est(0.3, 0.2, 0.4), 0.05, "DETECTABLE"),
                             ("DOSE-DET-NEG", Est(-0.3, -0.4, -0.2), 0.05, "DETECTABLE"),
                             ("DOSE-ND-CI", Est(0.3, -0.01, 0.6), 0.05, "NOT-DETECTABLE"),
                             ("DOSE-ND-UNCERT", Est(0.04, 0.02, 0.06), 0.05, "NOT-DETECTABLE")):
        dd = dose_outcome(literal_state(V={deq: v}, L={deq: Ld}), n1)
        B.chk(f"dose {want}: Δm(d_eq) {v.mean} [{v.lo}, {v.hi}] against L {Ld}", dd["state"] == want, dd, cover=[cid])
    ok = True
    for kind in ("pause", "incomplete"):
        for a in N1_ARMS:
            over = {"paused": {a: True}} if kind == "pause" else {"complete": {a: False}}
            s_ = literal_state(**over)
            dd = dose_outcome(s_, n1_outcome(s_))
            ok &= dd["state"] == "INDETERMINATE" and "N1-INDETERMINATE" in dd["causes"]
    B.chk("dose INDETERMINATE whenever N1 is, under each of N1's six causes", ok, cover=["DOSE-INDET-N1"])
    s_ = literal_state(complete={"N1-R": False})
    dd = dose_outcome(s_, n1_outcome(s_))
    B.chk("dose INDETERMINATE names 'incomplete:points' beside N1's (subsumed; OPEN-Q6, pending the seat)",
          dd["causes"] == ["N1-INDETERMINATE", "incomplete:points"], dd, cover=["DOSE-INDET-POINTS"])
    s_ = literal_state()
    dd = dose_outcome(s_, n1_outcome(s_))
    d20 = s_.dmap.resolved()["d_20"]
    B.chk("dose reports d_20 beside (point, estimate, ceiling, certification)", dd["d_20_beside"]["point"] == d20
          and dd["d_20_beside"]["certified"] is True, dd["d_20_beside"], cover=["DOSE-BESIDE-D20"])
    # N2
    m20 = MAP_A.norm_matched(F20)
    for cid, over, want in (("N2-SPECIFIC", {"E": {F20: Est(0.01, -0.02, 0.04)}}, "SPECIFIC"),
                            ("N2-SHARED-V-CERT", {}, "SHARED"),
                            ("N2-SHARED-V-UNCERT", {"V": {m20: _Z}}, "SHARED"),
                            ("N2-NULL", {"E": {F20: Est(0.01, -0.02, 0.04)}, "V": {m20: _Z}}, "NULL")):
        g = n2_outcome(literal_state(**over))
        B.chk(f"N2 {want} ({cid})", g["state"] == want, g, cover=[cid])
    for cid, over in (("N2-INDET-pause:N2-E", {"paused": {"N2-E": True}}),
                      ("N2-INDET-pause:N2-S", {"paused": {"N2-S": True}}),
                      ("N2-INDET-pause:N2-C", {"paused": {"N2-C": True}}),
                      ("N2-INDET-incomplete:N2-E", {"complete": {"N2-E": False}}),
                      ("N2-INDET-incomplete:N1-V", {"complete": {"N1-V": False}}),
                      ("N2-INDET-incomplete:N1-R", {"complete": {"N1-R": False}})):
        g = n2_outcome(literal_state(**over))
        why = cid.split("N2-INDET-", 1)[1]
        B.chk(f"N2 INDETERMINATE by {why}" + (" (§5, n:140: 'an unadjudicated pause stands on N2's reads'; the "
                                              "guards' reads are N2's reads)" if why.startswith("pause:")
                                              else " (OPEN-Q6, pending the seat)"),
              g["state"] == "INDETERMINATE" and g["causes"] == [why], g, cover=[cid])
    g_np = n2_outcome(literal_state(paused={"N1-V": True, "N1-R": True}))
    g_npb = n2_outcome(literal_state(MAP_B, paused={"N1-P": True}))
    B.chk("a pause on N1-V's or N1-R's reads, or on N1-P's where d_20 sits at +1 (shape b), alone leaves N2 "
          "evaluated (§5's N2 reads are N2-E's, N2-S's and N2-C's; OPEN-Q6, pending the seat: those N1 arms' "
          "incompleteness is a cause, their pauses are not)", g_np["state"] == "SHARED" and g_npb["state"] == "SHARED",
          (g_np["state"], g_npb["state"]), cover=["N2-NOT-PAUSED-BY-N1"])
    gb = n2_outcome(literal_state(MAP_B, complete={"N1-P": False}))
    ga = n2_outcome(literal_state(MAP_A, complete={"N1-P": False}))
    B.chk("N2 INDETERMINATE by incomplete:N1-P where d_20 sits at +1 (shape b: the ceiling takes P(+1)); with every "
          "point distinct (shape a) N1-P enters no N2 certification and N2 is evaluated (OPEN-Q6, pending the seat)",
          gb["state"] == "INDETERMINATE" and gb["causes"] == ["incomplete:N1-P"] and ga["state"] == "SHARED",
          (gb, ga["state"]), cover=["N2-INDET-incomplete:N1-P"])
    base = n2_outcome(literal_state(E={F20: Est(0.01, -0.02, 0.04)}))["state"]
    same = all(n2_outcome(literal_state(E={F20: Est(0.01, -0.02, 0.04)}, S={F20: s}, C={F20: c}))["state"] == base
               for s in (_X, _Z, Est(-1, -1.1, -0.9)) for c in (_X, _Z, Est(-1, -1.1, -0.9)))
    B.chk("N2's guards decide nothing (span_sentiment, span_character varied over nine pairs, the outcome fixed)",
          same and base == "SPECIFIC", base, cover=["N2-GUARDS-DECIDE-NOTHING"])
    g = n2_outcome(literal_state(E={F10: Est(0.01, -0.02, 0.04)}))
    B.chk("N2 reports f = 0.10 beside (its own certification at d_eq's point), deciding nothing",
          g["state"] == "SHARED" and g["beside"]["f=0.10"]["certified"] is False, g["beside"]["f=0.10"],
          cover=["N2-F10-BESIDE"])
    gb = n2_outcome(literal_state(MAP_B))
    B.chk("N2 reports the norm match: ratio 1 on shape (a); 2·0.72/1 = 1.44 when the cap binds (shape b; OPEN-Q7, "
          "pending the seat)",
          n2_outcome(literal_state())["match_ratio"] == 1.0 and abs(gb["match_ratio"] - 1.44) < 1e-12, gb["match_ratio"],
          cover=["N2-MATCH-RATIO"])
    # N4
    for cid, told, e, want in (("N4-PASS", Est(1.0, 0.8, 1.2, 98), 0.1, "PASS"),
                               ("N4-REVERSE", Est(-1.0, -1.2, -0.8, 98), 0.1, "REVERSE"),
                               ("N4-DEAD", Est(0.05, -0.1, 0.2, 98), 0.1, "DEAD"),
                               ("N4-INDET-TERMINAL", Est(0.3, -0.1, 0.7, 98), 0.1, "INDETERMINATE")):
        g = n4_outcome(literal_state(told=told, e_sham=e))
        B.chk(f"N4 {want}", g["state"] == want and g["no_read"] is False, g, cover=[cid])
    for cid, over in (("N4-NOREAD-incomplete:N4-T", {"complete": {"N4-T": False}}),
                      ("N4-NOREAD-incomplete:N4-Ts", {"complete": {"N4-Ts": False}}),
                      ("N4-NOREAD-pause:N4-T", {"paused": {"N4-T": True}}),
                      ("N4-NOREAD-pause:N4-Ts", {"paused": {"N4-Ts": True}}),
                      ("N4-NOREAD-E-undefined", {"e_sham": float("nan")})):
        g = n4_outcome(literal_state(**over))
        tag = " (OPEN-Q6, pending the seat)" if "pause" in cid else ""
        B.chk(f"N4 INDETERMINATE, no read obtained, by {cid[10:]}{tag}", g["state"] == "INDETERMINATE" and g["no_read"]
              and g["causes"] == [cid[10:]], g, cover=[cid])
    g = n4_outcome(literal_state(told=Est(-0.3, -0.4, -0.2, 98), e_sham=0.1))
    B.chk("N4 order: REVERSE before DEAD (mean −0.3 < −E, CI excludes 0, upper −0.2 < 0.5)", g["state"] == "REVERSE",
          g, cover=["N4-ORD-REV-OVER-DEAD"])
    g = n4_outcome(literal_state(told=Est(0.3, 0.2, 0.4, 98), e_sham=0.1))
    B.chk("N4 order: PASS before DEAD (mean 0.3 > E, CI excludes 0, upper 0.4 < 0.5)", g["state"] == "PASS", g,
          cover=["N4-ORD-PASS-OVER-DEAD"])
    g = n4_outcome(literal_state(told=Est(0.1, 0.05, 0.6, 98), e_sham=0.1))
    B.chk("N4 boundary: mean equal to E is not PASS (strict >)", g["state"] == "INDETERMINATE", g,
          cover=["N4-BND-MEAN-EQ-E"])
    g = n4_outcome(literal_state(told=Est(-0.1, -0.6, -0.05, 98), e_sham=0.1))
    B.chk("N4 boundary: mean equal to −E is not REVERSE (strict <); upper −0.05 < 0.5 -> DEAD", g["state"] == "DEAD",
          g, cover=["N4-BND-MEAN-EQ-NEGE"])
    g = n4_outcome(literal_state(told=Est(0.05, -0.4, DEAD_BAR, 98), e_sham=0.1))
    B.chk("N4 boundary: an upper bound equal to 0.5 is not DEAD (strict <)", g["state"] == "INDETERMINATE", g,
          cover=["N4-BND-HI-EQ-DEAD"])
    g = n4_outcome(literal_state(told=Est(0.8, 0.0, 1.6, 98), e_sham=0.1))
    B.chk("N4 boundary: a 98% CI with lower bound exactly 0 does not exclude 0 (not PASS)", g["state"] ==
          "INDETERMINATE", g, cover=["N4-BND-CI-LO-ZERO"])


def _bt_notrun(B: _Battery) -> None:
    good = {"schema": NOT_RUN_RECORD_SCHEMA, "unit": UNIT, "date": "2026-12-16", "detail": "a synthetic record"}
    for c in NOT_RUN_CAUSES:
        rec = dict(good, cause=c) | ({"stage": "G-CAL-n"} if c == "clock:gate-stopped" else {})
        try:
            r = not_run_reason(rec)
            ok = r == NOT_RUN_CAUSES[c].format(date=D_N, stage="G-CAL-n") and "{" not in r
        except SystemExit as e:
            ok, r = False, str(e)
        txt = sentence_set(NOT_RUN)
        B.chk(f"NOT-RUN by {c}: '{r}'", ok and all(v["state"] == NOT_RUN for v in txt.values()), r,
              cover=[f"NR-{c}"])
    for cid, rec, frag in (("NR-REFUSE-PREMATURE", dict(good, cause="clock:no-box", date=D_N), "on or before D_n"),
                           ("NR-REFUSE-STAGE", dict(good, cause="clock:gate-stopped", stage="G-NONE"), "stage"),
                           ("NR-REFUSE-UNIT", dict(good, cause="no-arm:cap", unit="N-lap"), "unit"),
                           ("NR-REFUSE-CAUSE", dict(good, cause="dose-not-completable"), "cause"),
                           ("NR-REFUSE-KEYS", dict(good, cause="no-arm:cap", extra=1), "unknown keys")):
        ok, msg = _bt_raises(lambda r=rec: not_run_reason(r), (AnlRefusal,))
        B.chk(f"NOT-RUN record refused ({cid[10:]})", ok and frag in msg, msg, cover=[cid])


def _bt_tables(B: _Battery) -> None:
    st = literal_state(V={0.5: _Z}, E={F10: _Z}, S={F20: _X}, C={F10: _Z, F20: _X})
    rows = gleak_table(st)
    seen = {(r["arm"], {True: "CERT", False: "UNCERT", None: "INCOMPLETE"}[r["certified"]]) for r in rows}
    st2 = literal_state(complete={"N1-R": False})
    seen |= {(r["arm"], {True: "CERT", False: "UNCERT", None: "INCOMPLETE"}[r["certified"]]) for r in gleak_table(st2)}
    for a in ("N1-V", "N2-E", "N2-S", "N2-C"):
        for c in ("CERT", "UNCERT", "INCOMPLETE"):
            B.chk(f"G-LEAK-n table: {a} {c.lower()} reached", (a, c) in seen, sorted(seen), cover=[f"GLEAK-{a}-{c}"])
    st3 = literal_state(gread={("valence", 1.0): "FAIL", ("span_reward", F10): "PASS"})
    del st3.gread[("valence", MAP_A.resolved()["d_eq"])]
    gt = gread_table(st3)
    states = {r["state"] for r in gt}
    for c in ("PASS", "FAIL", "NOT-COMPUTED"):
        B.chk(f"G-READ-n table: a {c} cell is reported as such", c in states, sorted(states), cover=[f"GREAD-{c}"])
    ent = {r["label"]: r["enters"] for r in gt if r["enters"]}
    B.chk("G-READ-n table: exactly three cells enter §5 -- valence +1 (N1), valence d_eq (dose), span_reward f = 0.20 "
          "(N2)", sorted(ent) == sorted(["+1", "d_eq", F20]), ent,
          cover=["GREAD-ENTERS-N1", "GREAD-ENTERS-DOSE", "GREAD-ENTERS-N2"])


def _bt_sentences(B: _Battery, verb: Mapping[str, str]) -> None:
    ok = (T_N1_REPLICATED == verb["rep"] and T_DOSE_DETECTABLE == verb["det"] and T_DOSE_ND_ANSWERED == verb["nd_ans"]
          and T_DOSE_ND_NOT_ANSWERED == verb["nd_cna"] and ANSWERED == verb["ans"] and CNA == verb["cna"] == verb["cna138"]
          and C_DOSE_ND_NOT_READABLE.endswith(verb["nd_cna"].lstrip("…").split("and ", 1)[1]))
    B.chk("§5's four sentences and two labels are the proposal's italic spans at n:136 and n:138, character for "
          "character; Code's expansion of the ellipsis ends in the span's own words", ok, cover=["SENT-VERBATIM"])
    forms = {tuple(f) for f in (["i"], ["iv"], ["i", "iv"])}
    txt = {f: sentence_n1("PARTIAL", n4="PASS", gr1="PASS", failing=list(f))["text"] for f in forms}
    B.chk("N1 PARTIAL names its failing conjuncts (OPEN-Q8, pending the seat): three forms, each naming exactly its "
          "conjuncts, no slot left",
          len(set(txt.values())) == 3 and all("[failing]" not in t for t in txt.values())
          and all(all(CONJUNCT_TEXT[k] in t for k in f) and all(CONJUNCT_TEXT[k] not in t for k in ("i", "iv")
                                                                if k not in f) for f, t in txt.items()),
          cover=["SENT-FAILING-PARTIAL"])
    sets = [list(c) for r in (1, 2, 3) for c in itertools.combinations(("ci+1", "ii", "iii"), r)]
    txt = [sentence_n1("NOT-REPLICATED", n4="PASS", gr1="FAIL", failing=f)["text"] for f in sets]
    B.chk("N1 NOT-REPLICATED names its failing conjuncts (OPEN-Q8, pending the seat): seven forms, each naming "
          "exactly its own", len(set(txt)) == 7
          and all(all(CONJUNCT_TEXT[k] in t for k in f) for f, t in zip(sets, txt)), cover=["SENT-FAILING-NOTREP"])
    t = sentence_n1("INDETERMINATE", n4="PASS", gr1="PASS", causes=["pause:N1-R", "incomplete:N1-P"])["text"]
    t2 = sentence_n4("INDETERMINATE", no_read=True, causes=["incomplete:N4-T"])["text"]
    B.chk("INDETERMINATE sentences carry their causes (OPEN-Q8, pending the seat)",
          "pause:N1-R, incomplete:N1-P" in t and "incomplete:N4-T" in t2
          and "no read obtained" in t2, (t, t2), cover=["SENT-CAUSES"])
    bad = [("N1", lambda: sentence_n1("PASS", n4="PASS", gr1="PASS")),
           ("set", lambda: sentence_set(("REPLICATED", "DETECTABLE", "SHARED", "PASS", "MAYBE"))),
           ("no-read on PASS", lambda: sentence_set(("REPLICATED", "DETECTABLE", "SHARED", "PASS", "PASS"),
                                                     n4_no_read=True))]
    res = [(n, _bt_raises(f)) for n, f in bad]
    B.chk("the sentence layer refuses a value outside the outcome space (three cases)", all(r[0] for _, r in res), res,
          cover=["SENT-REFUSES"])
    cf = code_forms()
    dig = hashlib.sha256(_canon(cf).encode("utf-8")).hexdigest()

    def brackets(text: str) -> list[str]:
        out, i = [], 0
        while (a := text.find("[", i)) >= 0:
            b = text.find("]", a)
            if b < 0:
                return out + [text[a:]]
            if not text[a + 1:a + 2].isdigit():              # "theirs 1.09 [1.00, 1.19]" is text, not a slot
                out.append(text[a:b + 1])
            i = b + 1
        return out
    stray = sorted({t for v in cf.values() for t in brackets(v) if t not in SLOTS})
    B.chk(f"Code's {len(cf)} sentence forms (OPEN-Q8) are pinned by digest (CODE_FORMS_SHA256), pairwise distinct, "
          "and use declared slots only", dig == CODE_FORMS_SHA256 and len(set(cf.values())) == len(cf) and not stray,
          (dig, stray), cover=["SENT-CODE-FORMS"])


def _canon(x: Any) -> str:
    return json.dumps(x, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _bt_tuple_pass(verb: Mapping[str, str]) -> tuple[dict, str, dict, dict]:
    """Every evaluation of evaluations(): the set, T1-T9 per evaluation (counted), the tallies and the sha."""
    names = [f"T{i}" for i in range(1, 10)]
    counts = {k: [0, 0] for k in names}
    fails: dict = {}
    first: dict = {}
    tal = {"7.1": {}, "7.2": {}, "7.3": {}, "N4": {}}
    h = hashlib.sha256()
    allowed = set(SLOTS) | {"[1.00, 1.19]"}
    import re
    for (t, gr1, gre, nr) in evaluations():
        kw = {} if t == NOT_RUN else {"gr1": gr1, "gre": gre, "n4_no_read": nr}
        out = sentence_set(t, **kw)
        orc = oracle_set(t, gr1=gr1, gre=gre, n4_no_read=nr, verb=verb)
        h.update((_canon({"t": t, "gr1": gr1, "gre": gre, "n4_no_read": nr, "set": out}) + "\n").encode("utf-8"))
        r = {}
        r["T1"] = (list(out) == list(SLOT_KEYS) and all(isinstance(v.get("text"), str) and v["text"].strip()
                                                       for v in out.values())
                   and (all(v["state"] == NOT_RUN for v in out.values()) if t == NOT_RUN else
                        [out[k]["state"] for k in SLOT_KEYS] == list(t[:4])))
        r["T2"] = out == orc
        if t == NOT_RUN:
            r["T3"] = r["T4"] = r["T5"] = r["T6"] = r["T7"] = r["T8"] = True
        else:
            n1, dose, n2, n4, grd = t
            keys = {"7.1": (n1, gr1, n4), "7.2": (dose, grd, n4), "7.3": (n2, gre, n4), "N4": (n4, nr)}
            for kk, tk in zip(("T3", "T4", "T5", "T6"), SLOT_KEYS):
                key = (tk,) + keys[tk]
                first.setdefault(key, out[tk])
                r[kk] = first[key] == out[tk]
            nulls = {"7.1": (n1 == "NOT-REPLICATED", gr1), "7.2": (dose == "NOT-DETECTABLE", grd),
                     "7.3": (n2 in ("SPECIFIC", "NULL"), gre), "N4": (False, None)}
            r["T7"] = all((out[k]["label"] is None) if not isnull else
                          out[k]["label"] == (ANSWERED if (n4 == "PASS" and g == "PASS") else CNA)
                          for k, (isnull, g) in nulls.items())
            v8 = {"7.1": verb["rep"] if n1 == "REPLICATED" else None,
                  "7.2": verb["det"] if dose == "DETECTABLE" else
                  verb["nd_ans"] if (dose == "NOT-DETECTABLE" and n4 == "PASS" and grd == "PASS") else None}
            r["T8"] = all((out[k]["text"] == v) if v is not None else
                          (out[k]["text"] not in (verb["rep"], verb["det"], verb["nd_ans"])) for k, v in v8.items())
        toks = {m for v in out.values() for m in re.findall(r"\[[^\[\]]*\]", v["text"])}
        r["T9"] = toks <= allowed
        for kk in names:
            counts[kk][0] += bool(r[kk])
            counts[kk][1] += 1
            if not r[kk]:
                fails.setdefault(kk, (t, gr1, gre, nr))
        for k in SLOT_KEYS:
            form = (out[k]["state"], out[k]["form"], out[k]["label"], out[k].get("no_read", False))
            tal[k][form] = tal[k].get(form, 0) + 1
    return counts, h.hexdigest(), tal, fails


def _bt_expected_tallies() -> dict:
    """Hand-derived (Code's arithmetic, re-derived in the BUILD raw): 1,920 evaluations of the 384 tuples + NOT-RUN."""
    t = {"7.1": {("REPLICATED", "§5", None, False): 480, ("PARTIAL", "Code", None, False): 480,
                 ("NOT-REPLICATED", "Code", ANSWERED, False): 48, ("NOT-REPLICATED", "Code", CNA, False): 432,
                 ("INDETERMINATE", "Code", None, False): 480},
         "7.2": {("DETECTABLE", "§5", None, False): 640, ("NOT-DETECTABLE", "§5", ANSWERED, False): 64,
                 ("NOT-DETECTABLE", "§5, its ellipsis expanded by Code", CNA, False): 320,
                 ("NOT-DETECTABLE", "Code", CNA, False): 256, ("INDETERMINATE", "Code", None, False): 640},
         "7.3": {("SPECIFIC", "Code", ANSWERED, False): 48, ("SPECIFIC", "Code", CNA, False): 432,
                 ("SHARED", "Code", None, False): 480, ("NULL", "Code", ANSWERED, False): 48,
                 ("NULL", "Code", CNA, False): 432, ("INDETERMINATE", "Code", None, False): 480},
         "N4": {("PASS", "Code", None, False): 384, ("REVERSE", "Code", None, False): 384,
                ("DEAD", "Code", None, False): 384, ("INDETERMINATE", "Code", None, False): 384,
                ("INDETERMINATE", "Code", None, True): 384}}
    for k in t:
        t[k][(NOT_RUN, "Code", None, False)] = 1
    return t


def _bt_tuples(B: _Battery, verb: Mapping[str, str]) -> None:
    counts, sha, tal, fails = _bt_tuple_pass(verb)
    n_ev = len(evaluations())
    names = {"T1": "one sentence set: the four slots 7.1, 7.2, 7.3, N4, each a non-empty text, each state the "
                   "tuple's coordinate (NOT-RUN: all four)",
             "T2": "the set equals the oracle's (§5's verbatim cells read from the proposal file)",
             "T3": "7.1 depends on (N1, G-READ-n valence +1, N4) only",
             "T4": "7.2 depends on (dose, G-READ-n valence d_eq, N4) only",
             "T5": "7.3 depends on (N2, G-READ-n span_reward f = 0.20, N4) only",
             "T6": "N4's line depends on (N4, no read obtained) only",
             "T7": "(OPEN-Q3, pending the seat) a §0.6 label exactly on the null outcomes (NOT-REPLICATED, "
                   "NOT-DETECTABLE, SPECIFIC, NULL); answered iff N4 PASS and the slot's G-READ-n cell PASS",
             "T8": "§5's verbatim sentences exactly in their cells (REPLICATED; DETECTABLE; NOT-DETECTABLE answered) "
                   "and nowhere else",
             "T9": "no bracketed token outside the declared slots (BK's '[1.00, 1.19]' is text)"}
    for kk, nm in names.items():
        c = counts[kk]
        B.chk(f"tuples {kk}: {c[0]}/{c[1]} evaluations: {nm}", c[0] == c[1] == n_ev, fails.get(kk, ""),
              cover=[f"TUP-{kk}"])
    want = _bt_expected_tallies()
    B.chk("tuples T10: the forms tally as derived by hand -- 7.1 480 each (NOT-REPLICATED 48 answered / 432 CNA); 7.2 "
          "640 each (NOT-DETECTABLE 64 / 320 / 256); 7.3 480 each (SPECIFIC and NULL 48 / 432); N4 384 x 5; NOT-RUN 1",
          tal == want, {k: tal[k] for k in tal if tal[k] != want.get(k)}, cover=["TUP-T10"])
    n_t = len(tuple_space())
    B.chk(f"the outcome space (OPEN-Q4, pending the seat): {n_t} tuples (4 x 3 x 4 x 4 x 2 = 384, + NOT-RUN), {n_ev} "
          f"evaluations (384 x 4 G-READ inputs + 96 x 4 for N4's second INDETERMINATE form + NOT-RUN)",
          n_t == 385 and n_ev == 1921,
          (n_t, n_ev), cover=["TUP-COUNT"])
    _, sha2, _, _ = _bt_tuple_pass(verb)
    B.extra["outputs_sha256"] = sha
    B.chk("two passes over the 1,921 evaluations give byte-identical canonical JSON", sha == sha2, sha[:16],
          cover=["TUP-DETERMINISM"])


# --- reachability (OPEN-Q5) ------------------------------------------------------------------------------------------
_MENU = (Est(1.0, 0.9, 1.1), Est(0.3, 0.2, 0.4), Est(0.03, 0.01, 0.05), Est(0.2, -0.1, 0.5), Est(0.0, -0.05, 0.05),
         Est(-0.8, -0.9, -0.7))
_PATTERNS = ([{}] + [{"paused": {a: True}} for a in N1_ARMS] + [{"complete": {a: False}} for a in N1_ARMS])
_N2_PATTERNS = ({}, {"paused": {"N2-E": True}}, {"complete": {"N2-E": False}})


def map_reach(dmap: DoseMap) -> tuple[set, bool, bool]:
    """The (N1, dose, N2) triples the outcome layer produces over a grid of states on one dose map: six estimates at
    each distinct point of +1, −1, d_eq, d_20, the slope above or not above its floor, span_reward's f = 0.20 effect
    certified or not, and every completeness / pause pattern; returns the set, whether dose INDETERMINATE <=> N1
    INDETERMINATE held throughout, and whether nothing raised."""
    r = dmap.resolved()
    pts = sorted({1.0, -1.0, r["d_eq"], r["d_20"]}, reverse=True)
    seen, iff, clean = set(), True, True
    for combo in itertools.product(_MENU, repeat=len(pts)):
        V = dict(zip(pts, combo))
        for slope_ok, e_cert in itertools.product((True, False), (True, False)):
            for pat, pat2 in itertools.product(_PATTERNS, _N2_PATTERNS):
                over = {"V": V, "floor_V": 0.3 if slope_ok else 1.5,
                        "E": {F20: Est(0.3, 0.2, 0.4) if e_cert else Est(0.01, -0.02, 0.04)}}
                st = literal_state(dmap, **over)
                for k in ("paused", "complete"):
                    getattr(st, k).update(pat.get(k, {}))
                    getattr(st, k).update(pat2.get(k, {}))
                try:
                    o = outcomes(st)
                except (Exception, SystemExit):                     # noqa: BLE001
                    clean = False
                    continue
                n1, dose, n2 = o["N1"]["state"], o["dose"]["state"], o["N2"]["state"]
                iff &= (n1 == "INDETERMINATE") == (dose == "INDETERMINATE")
                seen.add((n1, dose, n2))
    return seen, iff, clean


def map_reach_by_hand(shape: str) -> set:
    """Hand-derived reachable (N1, dose, N2) triples per merge shape (the question block's Q5 gives the derivation:
    results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md)."""
    det = ("DETECTABLE", "NOT-DETECTABLE")
    if shape == "a":
        return {(a, d, c) for a in ("REPLICATED", "PARTIAL", "NOT-REPLICATED") for d in det for c in N2_STATES} | \
               {("INDETERMINATE", "INDETERMINATE", c) for c in N2_STATES}
    if shape == "b":
        return ({(a, d, c) for a in ("REPLICATED", "PARTIAL") for d in det for c in ("SPECIFIC", "SHARED",
                                                                                    "INDETERMINATE")}
                | {("NOT-REPLICATED", d, c) for d in det for c in N2_STATES}
                | {("INDETERMINATE", "INDETERMINATE", c) for c in N2_STATES})
    if shape == "d":
        return ({(a, "DETECTABLE", c) for a in ("REPLICATED", "PARTIAL") for c in ("SPECIFIC", "SHARED",
                                                                                   "INDETERMINATE")}
                | {("NOT-REPLICATED", "DETECTABLE", c) for c in ("SPECIFIC", "SHARED", "INDETERMINATE")}
                | {("NOT-REPLICATED", "NOT-DETECTABLE", c) for c in N2_STATES}
                | {("INDETERMINATE", "INDETERMINATE", c) for c in N2_STATES})
    raise ValueError(shape)


def _bt_reachability(B: _Battery) -> None:
    res = {}
    for shape, dm in (("a", MAP_A), ("b", MAP_B), ("d", MAP_D)):
        seen, iff, clean = map_reach(dm)
        res[shape] = (seen, iff, clean)
    B.chk("reachability: on every enumerated state of the three shapes, dose is INDETERMINATE iff N1 is (so 160 of the "
          "384 product tuples are unreachable on any map: 64 with N1 INDETERMINATE and dose decided, 96 the reverse)",
          all(v[1] for v in res.values()), cover=["REACH-DOSE-IFF-N1"])
    B.chk("reachability: the outcome layer raised on no enumerated state", all(v[2] for v in res.values()),
          cover=["REACH-NO-RAISE"])
    for shape, n in (("a", 28), ("b", 24), ("d", 17)):
        seen = res[shape][0]
        want = map_reach_by_hand(shape)
        what = {"a": "all points distinct", "b": "d_20 merged into +1 (the cap binds)",
                "d": "d_20 and d_eq merged into +1"}[shape]
        B.chk(f"reachability, shape ({shape}) {what}: "
              f"{len(seen)} (N1, dose, N2) triples, the hand-derived {n}; x N4 (4) x G-READ-n at d_eq (2) = "
              f"{n * 8} reachable tuples + NOT-RUN", seen == want and len(want) == n,
              (sorted(seen - want)[:3], sorted(want - seen)[:3]), cover=[f"REACH-SHAPE-{shape}"])
    st = literal_state()
    free = set()
    for told, e in ((Est(1.0, 0.8, 1.2, 98), 0.1), (Est(-1.0, -1.2, -0.8, 98), 0.1), (Est(0.05, -0.1, 0.2, 98), 0.1),
                    (Est(0.3, -0.1, 0.7, 98), 0.1), (Est(0.3, -0.1, 0.7, 98), float("nan"))):
        for pat in _PATTERNS + [{"paused": {"N2-E": True}}]:
            s_ = literal_state(told=told, e_sham=e)
            for k in ("paused", "complete"):
                getattr(s_, k).update(pat.get(k, {}))
            o = outcomes(s_)
            free.add((o["N1"]["state"], o["N4"]["state"], o["N4"]["no_read"]))
    want = {(a, b, c) for a in ("REPLICATED", "INDETERMINATE") for b, c in (("PASS", False), ("REVERSE", False),
                                                                            ("DEAD", False), ("INDETERMINATE", False),
                                                                            ("INDETERMINATE", True))}
    B.chk("reachability: N4 reads its own arms only -- each of its five forms beside N1 REPLICATED and N1 "
          "INDETERMINATE", want <= free, sorted(want - free)[:3], cover=["REACH-N4-FREE"])
    B.extra["reachability"] = {s: {"triples": len(v[0]), "tuples": len(v[0]) * 8 + 1} for s, v in res.items()}


# --- numerics --------------------------------------------------------------------------------------------------------
F_CORR_0_PERMUTATION = (7, 9, 10, 1, 13, 12, 6, 2, 5, 8, 0, 11, 15, 3, 4, 14)   # valence_core.m.keys' known answer


def fidelity_ratio(cached_m: float, fresh_m: float, lp_s: float, lp_u: float) -> float:
    """§2.1: |cached − fresh| as a fraction of the read's scale, BK's frozen scale-relative criterion (TAU); the scale
    max(|log p(S)|, |log p(U)|) of the cached read (G-DATA (vi): the definition of record, by reproduction)."""
    return abs(float(cached_m) - float(fresh_m)) / max(abs(float(lp_s)), abs(float(lp_u)))


def _bt_hand_pct(a: Sequence[float], p: float) -> float:
    s = sorted(float(x) for x in a)
    pos = (len(s) - 1) * p / 100.0
    lo = int(math.floor(pos))
    hi = min(lo + 1, len(s) - 1)
    return s[lo] + (s[hi] - s[lo]) * (pos - lo)


def _bt_numerics(B: _Battery) -> None:
    if str(REPO) not in sys.path:
        sys.path.insert(0, str(REPO))
    from valence_core.m import keys as m_keys                  # lazy, battery only: the cross-check's reference
    ks = ("n-boot|N1-V", "n-boot|N4-T", "n-rand|0", "f|CORR|0")
    same = all(np.array_equal(key_stream(k).integers(0, 2 ** 31, size=8), m_keys.stream(k).integers(0, 2 ** 31, size=8))
               for k in ks)
    B.chk("key_stream is m:159's key-to-generator function (equal to valence_core.m.keys.stream on four keys)", same,
          cover=["NUM-KEYSTREAM-M159"])
    perm = tuple(int(x) for x in key_stream("f|CORR|0").permutation(16))
    B.chk("numpy's stream known answer: f|CORR|0's permutation(16) is m's pinned value", perm == F_CORR_0_PERMUTATION
          == tuple(m_keys.F_CORR_0_PERMUTATION), perm, cover=["NUM-KNOWN-ANSWER"])
    a1, a2, b1 = boot_index("N1-V", 160), boot_index("N1-V", 160), boot_index("N2-E", 160)
    # PIN-n-12 in its own words, re-derived literally: default_rng(crc32("n-boot|{arm}") % 2**31).integers(0, n,
    # size=(4000, n)) -- the stream the lock names as §4's seed
    lit = {(arm, n): np.random.default_rng(zlib.crc32(f"n-boot|{arm}".encode()) % 2 ** 31).integers(0, n, size=(4000, n))
           for arm, n in (("N1-V", 160), ("N1-R", 40), ("N4-T", 160))}
    B.chk("the resample matrix is PIN-n-12's stream, re-derived literally from its words for N1-V, N1-R (40) and "
          "N4-T: equal on a repeat, different across arms, 4,000 x n indices in [0, n)",
          np.array_equal(a1, a2) and not np.array_equal(a1, b1) and a1.shape == (4000, 160)
          and int(a1.min()) == 0 and int(a1.max()) == 159
          and all(np.array_equal(boot_index(arm, n), m_) for (arm, n), m_ in lit.items()),
          a1.shape, cover=["NUM-BOOT-DETERMINISM"])
    e = mean_est([0.25] * 40, boot_index("N1-R", 40))
    B.chk("a constant vector's estimate is (c, c, c)", (e.mean, e.lo, e.hi) == (0.25, 0.25, 0.25), e,
          cover=["NUM-BOOT-CONSTANT"])
    rng = key_stream("n-anl-test|values")
    vals = rng.normal(0.4, 0.6, size=37)
    idx = key_stream("n-anl-test|idx").integers(0, 37, size=(500, 37))
    got = mean_est(vals, idx)
    boots = [sum(float(vals[j]) for j in row) / 37 for row in idx]
    want = (sum(float(v) for v in vals) / 37, _bt_hand_pct(boots, 2.5), _bt_hand_pct(boots, 97.5))
    B.chk("mean_est equals a loop over the resamples with a hand percentile (linear interpolation), to 1e-12",
          all(abs(x - y) <= 1e-12 for x, y in zip((got.mean, got.lo, got.hi), want)), (got, want),
          cover=["NUM-BOOT-LOOP"])
    arr = [3.0, 1.0, 4.0, 1.0, 5.0, 9.0, 2.0, 6.0]
    B.chk("percentile intervals use linear interpolation (numpy's 'linear' equals the hand rule at 1, 2.5, 97.5, 99)",
          all(abs(pct_interval(np.array(arr), (p, 100 - p))[0] - _bt_hand_pct(arr, p)) <= 1e-12
              for p in (1.0, 2.5)) and all(abs(pct_interval(np.array(arr), (100 - p, p))[1] - _bt_hand_pct(arr, p))
                                           <= 1e-12 for p in (97.5, 99.0)), cover=["NUM-PCT-METHOD"])
    x = (1.0, 0.5, 2 / 3, 1 / 3, 0.0, -1.0)
    y = np.array([[1.1, 0.4, 0.7, 0.2, 0.0, -0.9], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.0, 1.0, 4 / 3, 2 / 3, 0.0, -2.0]])
    s = session_slopes(x, y)
    want = [float(np.polyfit(np.array(x), row, 1)[0]) for row in y]
    xm = sum(x) / 6
    closed = [sum((xi - xm) * yi for xi, yi in zip(x, row)) / sum((xi - xm) ** 2 for xi in x) for row in y.tolist()]
    B.chk("the per-session slope is OLS with an intercept (equal to polyfit and to the closed form; an exact line of "
          "slope 2 gives 2; a flat session 0)", all(abs(a - b) <= 1e-12 and abs(a - c) <= 1e-12
                                                     for a, b, c in zip(s, want, closed))
          and abs(s[2] - 2.0) <= 1e-12 and s[1] == 0.0, list(s), cover=["NUM-SLOPE-CLOSED-FORM"])
    xa = (1.0, 0.5, 0.0, -1.0)
    ya = np.array([[1.0, 0.6, 0.0, -0.6]])
    s_int = float(session_slopes(xa, ya)[0])
    s_org = float(sum(a * b for a, b in zip(xa, ya[0])) / sum(a * a for a in xa))
    B.chk("on an asymmetric grid OLS with an intercept and a fit through the origin differ, so OPEN-Q1 (pending the "
          "seat) decides a figure (here %.4f vs %.4f)" % (s_int, s_org), abs(s_int - s_org) > 1e-3,
          cover=["NUM-SLOPE-INTERCEPT"])
    v = [1.0, 2.0, 4.0]
    m_ = sum(v) / 3
    B.chk("sd0 is the population SD (ddof 0), C6", abs(sd0(v) - math.sqrt(sum((a - m_) ** 2 for a in v) / 3)) <= 1e-15,
          cover=["NUM-SD0"])
    ok, msg = _bt_raises(lambda: mean_est([0.1, float("nan"), 0.2], boot_index("N1-V", 3)), (AnlStop,))
    ok2, msg2 = _bt_raises(lambda: mean_est([0.1, float("inf")], boot_index("N1-V", 2)), (AnlStop,))
    B.chk("a nonfinite value in a statistic's input STOPs (never a silent drop)", ok and ok2, (msg, msg2),
          cover=["NUM-NONFINITE-STOP"])
    _bt_bk(B)
    shp = {"a": MAP_A.points() == (1.0, 2 / 3, 0.5, 1 / 3, 0.0, -1.0) and MAP_A.merged() == {"d_20": False,
                                                                                               "d_eq": False},
           "b": MAP_B.points() == (1.0, 0.72, 0.5, 0.0, -1.0) and MAP_B.merged() == {"d_20": True, "d_eq": False},
           "d": MAP_D.points() == (1.0, 0.5, 0.0, -1.0) and MAP_D.merged() == {"d_20": True, "d_eq": True},
           "merge-1/2": DoseMap(0.53125, 1.0).resolved()["d_eq"] == 0.5,
           "no-merge": DoseMap(0.5625, 1.0).resolved()["d_eq"] == 0.5625,
           "d_20-into-1/2": DoseMap(0.25, 0.5).resolved()["d_20"] == 0.5}
    B.chk("the dose map: shapes (a), (b), (d) and the merge rule at clear distances (0.03125 merges, 0.0625 does not; "
          "d_20 = 2·0.25 = 0.5 is BK's +1/2)", all(shp.values()), shp, cover=["NUM-DOSEMAP-SHAPES"])
    good = DoseMap((0.10 * 23.90625) / (0.3 * 25.5), min(1.0, 2.0 * ((0.10 * 23.90625) / (0.3 * 25.5))), 0.3, 25.5,
                   23.90625)
    d_r2 = (0.10 * 23.90625) / (0.2 * 25.5)                                  # d_eq computed from a rho of 0.2
    bad = {"d_20-above": DoseMap(0.4, 0.9).problems(), "d_20-below": DoseMap(0.4, 0.6).problems(),
           "neg": DoseMap(-0.1, 0.0).problems(), "nan": DoseMap(float("nan"), 1.0).problems(),
           "fold0": DoseMap(0.02, 0.04).problems(),
           "rho-above": replace(good, rho=0.30000000000000004).problems(),
           "rho-below": DoseMap(d_r2, min(1.0, 2.0 * d_r2), 0.2, 25.5, 23.90625).problems(),
           "R-negative": replace(good, R=-25.5).problems(), "R_ell-zero": replace(good, R_ell=0.0).problems(),
           "R-null": replace(good, R=None).problems(), "d_eq": replace(good, R_ell=24.0).problems()}
    B.chk("the dose map refuses d_20 above or below min(1.0, 2.0 * d_eq), a non-positive or nonfinite d_eq, a fold "
          "into 0, rho above or below 0.3 (each with d_eq computed from it where that matters), R or R_ell not a "
          "positive float, and d_eq ≠ (0.10 * R_ell) / (rho * R) (PIN-n-14); it passes shapes (a), (b), (d) and an "
          "exact identity (R_ell 23.90625, R 25.5: d_eq 0.3125)", all(bad.values()) and not MAP_A.problems()
          and not MAP_B.problems() and not MAP_D.problems() and not good.problems() and good.d_eq == 0.3125,
          {k: v[:1] for k, v in bad.items()}, cover=["NUM-DOSEMAP-REFUSE"])
    pa, pb, pd = MAP_A.expected_points(), MAP_B.expected_points(), MAP_D.expected_points()
    f_pts = [{"label": "f0.10", "value": 0.10, "merged": []}, {"label": "f0.20", "value": 0.20, "merged": []}]
    want = {"a": [{"label": "+1", "value": 1.0, "merged": []}, {"label": "+1/2", "value": 0.5, "merged": []},
                  {"label": "+d_20", "value": 2 / 3, "merged": []}, {"label": "+d_eq", "value": 1 / 3, "merged": []},
                  {"label": "-1", "value": -1.0, "merged": []}] + f_pts,
            "b": [{"label": "+1", "value": 1.0, "merged": ["+d_20"]}, {"label": "+1/2", "value": 0.5, "merged": []},
                  {"label": "+d_eq", "value": 0.72, "merged": []}, {"label": "-1", "value": -1.0, "merged": []}] + f_pts,
            "d": [{"label": "+1", "value": 1.0, "merged": ["+d_20", "+d_eq"]},
                  {"label": "+1/2", "value": 0.5, "merged": []}, {"label": "-1", "value": -1.0, "merged": []}] + f_pts}
    both = DoseMap(0.29, 0.58)                      # d_20 0.58 and d_eq 0.29 both kept (no candidate within 0.05)
    kl = {"a": (MAP_A.kept_label("d_20"), MAP_A.kept_label("d_eq")), "b": (MAP_B.kept_label("d_20"),
                                                                          MAP_B.kept_label("d_eq")),
          "d": (MAP_D.kept_label("d_20"), MAP_D.kept_label("d_eq"))}
    B.chk("the dose map lists its points as n-build's schema does (order, values, merged lists in fold order) for "
          "shapes (a), (b), (d); d_20 and d_eq are read under their keepers' labels", pa == want["a"] and pb == want["b"]
          and pd == want["d"] and kl == {"a": ("+d_20", "+d_eq"), "b": ("+1", "+d_eq"), "d": ("+1", "+1")}
          and [p["label"] for p in both.expected_points()][:4] == ["+1", "+1/2", "+d_20", "+d_eq"],
          {"a": pa == want["a"], "b": pb == want["b"], "d": pd == want["d"], "labels": kl},
          cover=["NUM-DOSEMAP-POINTS"])
    xr, yr = [3.0, 1.0, 4.0, 1.0, 5.0], [2.0, 7.0, 1.0, 8.0, 2.0]
    mx, my = sum(xr) / 5, sum(yr) / 5
    hand = (sum((a - mx) * (b - my) for a, b in zip(xr, yr))
            / math.sqrt(sum((a - mx) ** 2 for a in xr) * sum((b - my) ** 2 for b in yr)))
    B.chk("secondary (d)'s Pearson r (PIN-n-18): equal to the hand formula and to numpy's corrcoef; None when one side "
          "has no spread", abs(pearson_r(xr, yr) - hand) <= 1e-12
          and abs(pearson_r(xr, yr) - float(np.corrcoef(xr, yr)[0, 1])) <= 1e-12 and pearson_r(xr, [1.0] * 5) is None,
          pearson_r(xr, yr), cover=["NUM-PEARSON"])
    B.chk("the label-mass counter (PIN-n-17) counts reads strictly below .20 (0.19 counts; 0.20 and 0.9 do not)",
          label_mass_below([0.19, 0.20, 0.9, 0.0]) == 2 and LABEL_MASS_FLOOR == 0.20, cover=["CNT-LABEL-MASS"])
    n2a, n2b = MAP_A.n2_slope_points(), MAP_B.n2_slope_points()
    B.chk("N2's slope points (OPEN-Q9, pending the seat): (0, d_eq, 2·d_eq) on BK's scale, its floor at (0, d_eq's "
          "point, d_20's point) -- equal on shape (a); 2·0.72 against +1 when the cap binds (shape b)",
          n2a == ((0.0, 1 / 3, 2 / 3), (0.0, 1 / 3, 2 / 3)) and n2b == ((0.0, 0.72, 1.44), (0.0, 0.72, 1.0)),
          (n2a, n2b), cover=["NUM-N2-POINTS"])


def _bt_bk(B: _Battery) -> None:
    """§4's statistics on BK's released reads (data/n/bk, read only): G-DATA (iii)'s and (vi)'s figures."""
    red = json.loads((REPO / BK_NP_REL / "reduced.json").read_text(encoding="utf-8"))
    member = "olmo_32b"
    rows = red["reads"][member]
    sh = {(x["cell"], x["run"]): x["margin"] for x in rows if x["arm"] == "neutral" and x["direction_kind"] == "none"}
    by: dict = {}
    for x in rows:
        if x["arm"] == "neutral" and x["direction_kind"] != "none":
            by.setdefault((x["direction_kind"], x["dir_index"], x["cell"], x["run"]), {})[x["point"]] = \
                x["margin"] - sh[(x["cell"], x["run"])]
    pts = (-1.0, -0.5, 0.0, 0.5, 1.0)
    vk = sorted(k for k in by if k[0] == "valenced")
    dm = np.array([[0.0 if p == 0.0 else by[k][p] for p in pts] for k in vk])
    sl = session_slopes(pts, dm)
    means = {p: float(dm[:, i].mean()) for i, p in enumerate(pts) if p != 0.0}
    sds = {p: sd0(dm[:, i]) for i, p in enumerate(pts) if p in (1.0, 0.5, -1.0)}
    rnd = {}
    for k in by:
        if k[0] == "random":
            rnd.setdefault(k[1], []).append(k)
    rs = {i: float(session_slopes(pts, np.array([[0.0 if p == 0.0 else by[k][p] for p in pts] for k in sorted(ks)])).mean())
          for i, ks in rnd.items()}
    L1 = max(abs(float(np.mean([by[k][1.0] for k in ks]))) for ks in rnd.values())
    got = {"n": len(vk), "dirs": len(rnd), "mean+1": round(means[1.0], 4), "mean+1/2": round(means[0.5], 4),
           "mean-1/2": round(means[-0.5], 4), "mean-1": round(means[-1.0], 4), "sd+1": round(sds[1.0], 4),
           "sd+1/2": round(sds[0.5], 4), "sd-1": round(sds[-1.0], 4), "slope": round(float(sl.mean()), 4),
           "slope_sd": round(sd0(sl), 4), "rand_min": round(min(rs.values()), 4), "rand_max": round(max(rs.values()), 4),
           "floor": round(max(abs(v) for v in rs.values()), 4)}
    want = {"n": 160, "dirs": 24, "mean+1": 1.09, "mean+1/2": 0.5072, "mean-1/2": -0.3841, "mean-1": -0.7554,
            "sd+1": 0.6233, "sd+1/2": 0.3703, "sd-1": 0.4546, "slope": 0.9164, "slope_sd": 0.4466, "rand_min": -0.288,
            "rand_max": 0.3641, "floor": 0.3641}
    B.extra["bk_repro"] = dict(got, L_plus1=L1, slope_ci_ours=list(mean_est(sl, boot_index("BK-N1-V", 160)).as_json()
                                                                  ["ci"]))
    B.chk("§4's statistics on BK's 160 neutral sessions reproduce G-DATA (iii): Panel D means 1.0900 / 0.5072 / "
          "−0.3841 / −0.7554; SDs (ddof 0) 0.6233 / 0.3703 / 0.4546; slope 0.9164, SD 0.4466; the 24 random slopes "
          "−0.2880 to +0.3641, so the floor on BK's five points is 0.3641", got == want,
          {k: (got[k], want[k]) for k in want if got[k] != want[k]}, cover=["NUM-BK-REPRO"])
    fid = [fidelity_ratio(x["margin"], x["fresh_margin"], x["logprob_S"], x["logprob_U"]) for x in rows
           if x["arm"] == "neutral" and x.get("fresh_margin") is not None]
    above_tau = sum(r > TAU for r in fid)
    above_sens = sum(r > TAU_SENS for r in fid)
    B.extra["bk_fidelity"] = {"reads": len(fid), "above_tau": above_tau, "above_tau_over_4": above_sens,
                              "max_ratio": round(max(fid), 6)}
    B.chk("fidelity_ratio on BK's 2,400 neutral re-computed reads reproduces G-DATA (vi): 0 above TAU (p0 = 0/2,400), "
          "570 above TAU/4, largest ratio 0.012143", len(fid) == 2400 and above_tau == 0 and above_sens == 570
          and round(max(fid), 6) == 0.012143, B.extra["bk_fidelity"], cover=["NUM-BK-FIDELITY"])


# --- structure ---------------------------------------------------------------------------------------------------------
#: Code's readings, declared (each strikable by the seat until LOCK-n v1.0).
PINS = {
    "PIN-n-7": "'exceeds its floor' is the signed mean slope above the floor (floor ≥ 0)",
    "PIN-n-8": "'its CI excluding 0' is lo > 0 or hi < 0; an endpoint at 0 does not exclude; either side",
    "PIN-n-11": "a G-READ-n cell absent or not computed is not PASS for §0.6",
    "PIN-n-12": "one resample matrix per arm from 'n-boot|{arm}' (m:159's function), B = 4,000, shared by the arm's "
                "statistics; in the TAU/4 row, where they differ in session count, each draws the arm's stream at its "
                "own count; percentile intervals, linear interpolation; 95% 2.5/97.5, N4's 98% 1/99",
    "PIN-n-14": "the merge rule (n-build's dose_points, agreed 2026-11-15): d_20, then d_eq, each folded into the "
                "nearest candidate (+1, +1/2, 0, −1, then +d_20 if kept) at an IEEE-double distance ≤ 0.05, a tie to "
                "the earlier candidate; a fold into 0 refused; rho == 0.3, d_eq == (0.10 * R_ell) / (rho * R), d_20 == "
                "min(1.0, 2.0 * d_eq) exactly",
    "PIN-n-16": "the TAU/4 sensitivity row drops a read whose re-computation exceeds TAU/4; a shadow that exceeds drops "
                "its session's Δm at every dose; a session missing a point drops out of the slopes; reads with no "
                "re-computation are kept",
    "PIN-n-17": "the label-mass counter counts restricted reads with two-label mass below .20 (n:99; m:283)",
    "PIN-n-18": "secondary (d) is Pearson's r between the retention interval and Δm at +1 over N1-V's sessions",
    "PIN-n-19": "(iv) is evaluated: the −1 pole is read under A1 'struck beyond d = −1' (routing 2026-11-06)",
    "PIN-n-20": "a non-finite read is present but no read for the statistics: its arm is not usable (§5 'a partial "
                "read set'; cause nonfinite:<arm>); a steered arm is usable only when the shadows (N1-V's d = 0 "
                "reads) of every session it reads are present and finite (cause shadow:<arm>); an arm the TAU/4 row "
                "empties at a point is not usable in that row (cause tau4-emptied:<arm>)",
    "PIN-n-21": "a NOT-RUN record is dated the PI date it is made; a Clock cause is refused on or before D_n, which is "
                "inclusive (§7.4), so LOCK-n v1.0 can still be committed on D_n itself",
    "PIN-n-22": "secondaries: (a) the share of finite restricted reads picking S, per arm and dose label; (c) the "
                "Δm groups by present order and by ordered cue pair (cue_S|cue_U), per arm and dose label, over "
                "steered reads with a finite shadow (N4, unsteered, has none); (a), (c) and (d) report a figure at "
                "n ≥ 20 only (rule 28(a)'s decidable-n floor, n §4)",
}
#: The seat's open questions (results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md, Q1-Q9): what the code
#: carries meanwhile, each pending the seat; G-ANL-n's canonical run waits for the answers.
OPEN = {
    "OPEN-Q1": "the slope fit: OLS with an intercept over the arm's dose points, d = 0 with Δm(0) = 0 included where "
               "listed (or through the origin)",
    "OPEN-Q2": "the leak ceiling where N1-P is not read: L(d) alone",
    "OPEN-Q3": "'answered' needs N4 PASS and G-READ-n PASS (§0.6) for N1 NOT-REPLICATED, dose NOT-DETECTABLE and N2's "
               "null; the (G-READ-n PASS, N4 not PASS) dose cell's sentence",
    "OPEN-Q4": "three inputs that change a sentence are not coordinates: G-READ-n (valence, +1), G-READ-n "
               "(span_reward, f = 0.20), N4's no-read INDETERMINATE; the tuple pass runs every tuple under each",
    "OPEN-Q5": "the impossible tuples carry a sentence set (total functions); reachability reported separately, per "
               "merge shape",
    "OPEN-Q6": "INDETERMINATE causes §5 does not name: N1-V incomplete (N1); dose's 'points incomplete' as N1-V's or "
               "N1-R's reads, beside N1's causes; N2-E, N1-V or N1-R incomplete, and N1-P where d_20 sits at +1 (N2), "
               "while a pause on those N1 arms alone leaves N2 evaluated, as written; a pause on N4's reads (N4)",
    "OPEN-Q7": "the norm-matched point is d_20's (f = 0.20) and d_eq's (f = 0.10), the ratio reported",
    "OPEN-Q8": "Code's sentence forms where §5 words none",
    "OPEN-Q9": "N2's slope over {0, d_eq, 2·d_eq} on BK's scale, its floor on the random reads at d_eq's and d_20's "
               "points",
}
_HEAVY = ("torch", "transformers", "mlx", "mlx_lm", "accelerate", "safetensors")


def _norm(p: Any, base: str | None = None) -> str | None:
    """A path as an absolute, normalised string, without touching the filesystem (no stat, no realpath): a relative
    path against ``base``, by default the process's working directory (as the OS resolves it)."""
    import os
    try:
        s = os.fspath(p)
    except TypeError:
        return None
    if isinstance(s, bytes):
        s = s.decode("utf-8", "replace")
    if not isinstance(s, str):
        return None
    import os.path as op
    return op.normpath(s) if op.isabs(s) else op.normpath(op.join(base or os.getcwd(), s))


def _barred(s: str) -> bool:
    """data/mf3 entirely; any data/<unit>/ckpt, /reports or /verdicts; results/raw (the battery reads none of them)."""
    root = str(REPO) + "/"
    if not s.startswith(root):
        return False
    rel = s[len(root):]
    parts = rel.split("/")
    if parts[:2] == ["data", "mf3"]:
        return True
    if len(parts) >= 3 and parts[0] == "data" and parts[2] in ("ckpt", "reports", "verdicts"):
        return True
    return parts[:2] == ["results", "raw"]


class _Hook:
    """During the battery: builtins.open, io.open, os.open, Path.open/read_bytes/read_text, os.stat/lstat, os.listdir,
    os.scandir and subprocess.run refuse a barred path, by string, before any filesystem call or process start; a
    relative path is resolved as the OS would (the working directory) and, for a process's arguments, against the
    repository too (git -C); the path is the first positional argument or a file= / path= / args= / cwd= keyword.
    Refusals are recorded."""

    def __init__(self) -> None:
        self.caught: list[str] = []
        self.saved: dict = {}

    def check(self, p: Any, base: str | None = None) -> None:
        s = _norm(p, base)
        if s is not None and _barred(s):
            self.caught.append(s[len(str(REPO)) + 1:])
            raise PermissionError(f"the n analyzer's battery never touches {s[len(str(REPO)) + 1:]}")

    def __enter__(self) -> "_Hook":
        import builtins
        import io
        import os
        import pathlib
        import subprocess
        hook = self
        targets = {"open": (builtins, "open"), "io_open": (io, "open"), "os_open": (os, "open"),
                   "p_open": (pathlib.Path, "open"), "p_rb": (pathlib.Path, "read_bytes"),
                   "p_rt": (pathlib.Path, "read_text"), "stat": (os, "stat"), "lstat": (os, "lstat"),
                   "listdir": (os, "listdir"), "scandir": (os, "scandir"), "run": (subprocess, "run")}

        def wrapped(orig, proc: bool):
            def wrap(*a, **kw):
                if proc:
                    argv = a[0] if a else kw.get("args")
                    items = [argv] if isinstance(argv, (str, bytes, os.PathLike)) else list(argv or [])
                    for x in items + ([kw["cwd"]] if kw.get("cwd") is not None else []):
                        hook.check(x)
                        hook.check(x, base=str(REPO))
                else:
                    for x in a[:1] + tuple(v for k, v in kw.items() if k in ("file", "path")):
                        hook.check(x)
                return orig(*a, **kw)
            return wrap
        for k, (obj, attr) in targets.items():
            orig = getattr(obj, attr)
            self.saved[k] = (obj, attr, orig)
            setattr(obj, attr, wrapped(orig, k == "run"))
        return self

    def __exit__(self, *exc) -> None:
        for obj, attr, orig in self.saved.values():
            setattr(obj, attr, orig)


def _bt_snapshot() -> dict:
    """data/n's state outside its ckpt / reports / verdicts directories: every file's sha256 (a walk pruned at exactly
    the directories _barred bars, so nothing inside them is listed or stat'ed)."""
    import os
    out = {}
    root = REPO / "data" / "n"
    for d, dirs, files in os.walk(root):
        dirs[:] = sorted(x for x in dirs if not _barred(os.path.normpath(os.path.join(d, x))))
        for f in sorted(files):
            p = Path(d) / f
            out[str(p.relative_to(REPO))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def _bt_structure(B: _Battery, ptext: bytes, hook: _Hook) -> None:
    import ast
    B.chk("proposal: PROPOSAL-n v0.2's sha256 is the pinned 30a3d0f5...04f4", hashlib.sha256(ptext).hexdigest()
          == PROPOSAL_SHA256, hashlib.sha256(ptext).hexdigest()[:16], cover=["STR-PROPOSAL-SHA"])
    lines = ptext.decode("utf-8").splitlines()
    miss = [k for k, (n, s) in VERBATIM.items() if s not in lines[n - 1]]
    B.chk("every verbatim constant is on its declared proposal line (n:136, n:138, n:142)", miss == [], miss,
          cover=["STR-VERBATIM-IN-PROPOSAL"])
    pre = (REPO / BK_NP_REL / "prereg.json").read_bytes()
    sums = (REPO / "data/n/bk/SHA256SUMS").read_text(encoding="utf-8")
    pre_ok = f"{hashlib.sha256(pre).hexdigest()}  experiment_results_json/fixed_text_design/neutral_passages/prereg.json" \
        in sums
    B.chk("TAU is BK's prereg.json 'tau', and prereg.json is the SHA256SUMS copy", json.loads(pre)["tau"] == TAU
          and pre_ok, (json.loads(pre)["tau"], pre_ok), cover=["STR-TAU-PREREG"])
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    mods = set()
    for node in tree.body:
        if isinstance(node, ast.Import):
            mods |= {a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom):
            mods.add((node.module or "").split(".")[0])
    allowed = {"__future__", "argparse", "hashlib", "itertools", "json", "math", "sys", "zlib", "dataclasses",
               "pathlib", "typing", "numpy"}
    B.chk("module-level imports are numpy and the standard library only (no repository module, no model library)",
          mods <= allowed, sorted(mods - allowed), cover=["STR-NO-REPO-IMPORT"])
    heavy = sorted(m for m in _HEAVY if m in sys.modules)
    B.chk("no model library is imported by the battery (torch, transformers, mlx, mlx_lm, accelerate, safetensors)",
          heavy == [], heavy, cover=["STR-NO-HEAVY"])
    n0 = len(hook.caught)
    import os
    import subprocess
    # Each probe names an absent path, so that even a broken hook would list, stat or read nothing that exists; the
    # data/mf3 probes go through hook.check (a string test, no filesystem call) and a process that reads no argument.
    absent = "__n_anl_probe_absent__"
    probes = []
    for fn, arg in ((open, REPO / f"data/n/ckpt/{absent}.json"),
                    (lambda q: Path(q).read_text(), REPO / f"results/raw/{absent}.txt"),
                    (lambda q: os.stat(q), REPO / f"data/n/ckpt/{absent}"),
                    (lambda q: os.listdir(q), REPO / f"data/n/reports/{absent}"),
                    (lambda q: os.scandir(q), REPO / f"data/n/verdicts/{absent}"),
                    (lambda q: os.open(q, os.O_RDONLY), REPO / f"data/n/reports/{absent}.json"),
                    (lambda q: open(file=q), REPO / f"data/n/ckpt/{absent}.npy"),
                    (lambda q: subprocess.run(["/usr/bin/true", q], check=False), f"data/mf3/{absent}"),
                    (hook.check, REPO / f"data/mf3/{absent}")):
        probes.append(_bt_raises(lambda f=fn, a=arg: f(a), (PermissionError,))[0])
    B.chk(f"the battery's hook refuses, before any filesystem call or process start, {len(probes)} probes: opens "
          "(positional, file=, os.open) under data/n/ckpt, data/n/reports and results/raw, a stat, a listing and a "
          "scan under data/n's ckpt, reports and verdicts, a process naming data/mf3 by a repository-relative path, "
          "and data/mf3 by string; nothing else was refused during the battery",
          all(probes) and len(hook.caught) == n0 + len(probes) and n0 == 0, (probes, hook.caught[:3]),
          cover=["STR-OPEN-HOOK"])
    src = Path(__file__).read_text(encoding="utf-8")
    import re
    body = re.sub(r"\n(PINS|OPEN) = \{.*?\n\}\n", "\n", src, flags=re.S)      # the registers themselves cite nothing
    pins_used = set(re.findall(r"PIN-n-\d+", body))
    open_used = set(re.findall(r"OPEN-Q\d+", body))
    B.chk("every PIN-n and OPEN-Q cited outside the registers is registered, and every registered one is cited",
          pins_used == set(PINS) and open_used == set(OPEN) and len(body) < len(src),
          (sorted(pins_used ^ set(PINS)), sorted(open_used ^ set(OPEN))), cover=["STR-PINS"])


# =====================================================================================================================
# 10. The reader (n-read-v1 / n-cell-v1, valence_core/n/schema.py at 5a97527, sha256 77c12d6d...94bc)
# =====================================================================================================================
# The schema module is imported lazily, on the verdicts path and in the battery only (LAZY_SCHEMA), and bound by its
# sha256 in every output; its checks run on every cell the analyzer loads ("the checks both sides run"). What the
# schema leaves to the analyzer ("CROSS-RECORD PROPERTIES ... The analyzer re-checks what it uses") is checked here:
# each steered read's shadow exists with its ids_sha; a session's cues and present order agree across its reads; N4-T
# and N4-Ts carry the same schedule_zone per session, 80 S and 80 U (n §2.4).
SCHEMA_REL = "valence_core/n/schema.py"
SCHEMA_SHA256 = "77c12d6d0e7eee370291e0f5e587204f4ae613c65ce57f95c336f507273494bc"     # 5a97527
LAZY_SCHEMA = "valence_core.n.schema"
N_SESSIONS, N_FLOOR = 160, 40
#: n §2.4's table, independently of the schema's ARM_CELLS (the reader cross-checks the two): arm -> (directions,
#: dose labels before §2.3's merges, sessions).
PLAN_TABLE = {
    "N1-V": ((("valence",), ("+1", "+1/2", "+d_20", "+d_eq", "-1")), (("none",), ("0",))),
    "N1-R": ((tuple(f"rand_{i:02d}" for i in range(N_RANDOM)), ("+1", "+1/2", "+d_20", "+d_eq", "-1")),),
    "N1-P": ((("valence",), ("+1", "-1")),),
    "N2-E": ((("span_reward",), ("f0.10", "f0.20")),),
    "N2-S": ((("span_sentiment",), ("f0.10", "f0.20")),),
    "N2-C": ((("span_character",), ("f0.10", "f0.20")),),
    "N4-T": ((("none",), ("0",)),),
    "N4-Ts": ((("none",), ("0",)),),
}
GUARD_DIRS = {"N2-E": "span_reward", "N2-S": "span_sentiment", "N2-C": "span_character"}


def schema_module():
    """The record schema, imported lazily; refused unless its bytes are the pinned ones (5a97527)."""
    if str(REPO) not in sys.path:
        sys.path.insert(0, str(REPO))
    got = hashlib.sha256((REPO / SCHEMA_REL).read_bytes()).hexdigest()
    if got != SCHEMA_SHA256:
        raise AnlRefusal(f"REFUSED: {SCHEMA_REL} hashes to {got[:16]}, not the schema of record {SCHEMA_SHA256[:16]}")
    import importlib
    mod = importlib.import_module(LAZY_SCHEMA)
    if Path(mod.__file__).resolve() != (REPO / SCHEMA_REL).resolve():
        raise AnlRefusal(f"REFUSED: {LAZY_SCHEMA} was imported from another file than the hashed {SCHEMA_REL}")
    return mod


def session_key(run: int) -> str:
    """BK's run -> its session_id, by the skeletons' layout (floor_b0-b7 hold runs 0-39, five each; neu_b0-b5 runs
    40-159, twenty each); the schema's bk_cell_of is cross-checked against this in the battery."""
    if not 0 <= run < N_SESSIONS:
        raise ValueError(run)
    return f"floor_b{run // 5}/{run}" if run < N_FLOOR else f"neu_b{(run - N_FLOOR) // 20}/{run}"


def own_plan(kept_labels: Sequence[str]) -> list[str]:
    """§2.4's declared read set over the kept dose labels, derived without the schema (the reader asserts it equals
    the schema's read_plan): N1-R on the 40 floor sessions, every other arm on all 160; a folded label is read under
    its keeper, so only kept labels appear."""
    kept = set(kept_labels) | {"0"}
    out = []
    for arm, rows in PLAN_TABLE.items():
        runs = range(N_FLOOR) if arm == "N1-R" else range(N_SESSIONS)
        for dirs, labels in rows:
            for d in dirs:
                for lab in labels:
                    if lab in kept:
                        out.extend(f"{arm}|{d}|{lab}|{session_key(r)}" for r in runs)
    return sorted(out)


def dose_map_of(identity: Mapping[str, Any]) -> DoseMap:
    dm = identity["dose_map"]
    return DoseMap(dm["d_eq"], dm["d_20"], dm["rho"], dm["R"], dm["R_ell"])


def lock_names(text: str, value: str) -> bool:
    """A lock names a sha256 when it stands as a whole line or between backticks (p's form, round 3's NOTE 3)."""
    return any(ln.strip() == value for ln in text.splitlines()) or f"`{value}`" in text


@dataclass
class Campaign:
    """What the reader hands the statistics: the identity, the dose map, the records by read_id, each arm's planned
    read_ids, the planned reads present on disk and those of them that are not finite, and the cells read."""
    identity: dict
    dmap: DoseMap
    records: dict
    planned: dict
    present: dict
    nonfinite: dict
    cells: dict

    def usable(self, arm: str) -> bool:
        """PIN-n-20: an arm is usable iff every planned read is present and finite (§5: "An arm with a partial read
        set is INDETERMINATE"; a non-finite read is no read for the statistics)."""
        return self.present[arm] == self.planned[arm] and not self.nonfinite[arm]


def load_campaign(cdir: Path, sm=None) -> Campaign:
    """Load a campaign's cell files (every file beside them named by a cell), run the schema's checks on each, and the
    cross-record checks the schema leaves to the analyzer. Refuses (exit 2) on a cell that fails a check, a cell or
    capture file whose bytes are not those the cell records, an identity that differs between cells, a dose map whose
    points the analyzer derives differently, a plan the analyzer derives differently, a read outside the plan or a
    broken cross-record property."""
    sm = sm or schema_module()
    cdir = Path(cdir)
    if not cdir.is_dir():
        raise AnlRefusal(f"REFUSED: no campaign directory {cdir.name!r}")
    names = sorted(p.name for p in cdir.iterdir())
    jsons = [n for n in names if n.endswith(".json")]
    cells, ident0, records = {}, None, {}
    for n in jsons:
        try:
            data = (cdir / n).read_bytes()
            cell = json.loads(data.decode("utf-8"))
            sm.check_cell(cell, where=n)
        except (OSError, ValueError) as e:
            raise AnlRefusal(f"REFUSED: cell {n}: {type(e).__name__}: {e}"[:400])
        if n != sm.cell_filename(cell["arm"], cell["direction_id"], cell["dose_label"]):
            raise AnlRefusal(f"REFUSED: cell {n} is named for another cell")
        if cell["capture_file"] not in names:
            raise AnlRefusal(f"REFUSED: cell {n}'s capture array {cell['capture_file']} is absent")
        cap = hashlib.sha256((cdir / cell["capture_file"]).read_bytes()).hexdigest()
        if cap != cell["capture_sha256"]:
            raise AnlRefusal(f"REFUSED: cell {n}'s capture array does not hash to its recorded capture_sha256")
        if ident0 is None:
            ident0 = cell["stage_identity"]
        elif _canon(cell["stage_identity"]) != _canon(ident0):
            raise AnlRefusal(f"REFUSED: cell {n}'s stage identity differs from the first cell's")
        for rec in cell["records"]:
            if rec["read_id"] in records:
                raise AnlRefusal(f"REFUSED: read {rec['read_id']} appears in two cells")
            records[rec["read_id"]] = rec
        cells[n] = {"json_sha256": hashlib.sha256(data).hexdigest(), "capture_sha256": cap,
                    "records": len(cell["records"])}
    extra = sorted(set(names) - set(jsons) - {n[:-5] + ".npy" for n in jsons})
    if ident0 is None:
        raise AnlRefusal(f"REFUSED: no cell file in {cdir.name!r}")
    if extra:
        raise AnlRefusal(f"REFUSED: files beside the cells that no cell names: {extra[:4]}")
    if ident0["stage"] != "campaign" or ident0["proposal_sha256"] != PROPOSAL_SHA256:
        raise AnlRefusal("REFUSED: not a campaign of PROPOSAL-n v0.2 (stage or proposal_sha256)")
    dmap = dose_map_of(ident0)
    probs = dmap.problems()
    if probs or dmap.expected_points() != ident0["dose_map"]["points"]:
        raise AnlRefusal(f"REFUSED: the dose map: {probs or 'its points differ from the analyzer derivation'}")
    kept = [p["label"] for p in ident0["dose_map"]["points"]]
    plan = sm.read_plan(ident0)
    if plan != own_plan(kept):
        raise AnlRefusal("REFUSED: the schema's read plan differs from the analyzer's own derivation of n §2.4")
    planned: dict = {a: set() for a in ARMS}
    for rid in plan:
        planned[rid.split("|", 1)[0]].add(rid)
    outside = sorted(set(records) - set(plan))
    if outside:
        raise AnlRefusal(f"REFUSED: {len(outside)} read(s) outside the declared plan, e.g. {outside[0]}")
    present = {a: {r for r in planned[a] if r in records} for a in ARMS}
    nonfinite = {a: sorted(r for r in present[a] if not records[r]["finite"]) for a in ARMS}
    _cross_checks(records)
    return Campaign(identity=ident0, dmap=dmap, records=records, planned=planned, present=present,
                    nonfinite=nonfinite, cells=cells)


def _cross_checks(records: Mapping[str, Mapping]) -> None:
    """The cross-record properties the schema leaves to the analyzer ("The analyzer re-checks what it uses"): every
    steered read's shadow is on disk (the runner writes a steered read only after its shadow) with its ids_sha; a
    session's cues and present order agree across its reads; N4-T and N4-Ts carry the same schedule zone per session;
    a complete N4 arm's schedule is 80 S and 80 U (n §2.4)."""
    by_session: dict = {}
    for rid, r in records.items():
        s = r["session_id"]
        key = (r["cue_S"], r["cue_U"], tuple(r["present"]))
        by_session.setdefault(s, set()).add(key)
        if r["shadow_read_id"] is not None:
            sh = records.get(r["shadow_read_id"])
            if sh is None:
                raise AnlRefusal(f"REFUSED: {rid}'s shadow {r['shadow_read_id']} is not on disk")
            if sh["ids_sha"] != r["ids_sha"]:
                raise AnlRefusal(f"REFUSED: {rid}'s ids_sha differs from its shadow's")
    bad = sorted(s for s, ks in by_session.items() if len(ks) != 1)
    if bad:
        raise AnlRefusal(f"REFUSED: session(s) whose cues or present order differ between reads: {bad[:3]}")
    z: dict = {}
    for r in records.values():
        if r["arm"] in N4_ARMS:
            z.setdefault(r["session_id"], {})[r["arm"]] = r["schedule_zone"]
    if any(len(v) == 2 and v["N4-T"] != v["N4-Ts"] for v in z.values()):
        raise AnlRefusal("REFUSED: N4-T and N4-Ts carry different schedule zones for a session")
    for arm in N4_ARMS:
        zs = [r["schedule_zone"] for r in records.values() if r["arm"] == arm]
        if len(zs) == N_SESSIONS and sorted(zs) != ["S"] * 80 + ["U"] * 80:
            raise AnlRefusal(f"REFUSED: {arm}'s schedule is not 80 S and 80 U (n §2.4)")


# =====================================================================================================================
# 11. From the campaign to the state (§4's statistics on the records)
# =====================================================================================================================


def label_values(identity: Mapping[str, Any]) -> dict[str, float]:
    """Each kept BK-scale label -> its point on BK's scale ('0' included); N2's f labels excluded."""
    out = {"0": 0.0}
    for p in identity["dose_map"]["points"]:
        if not p["label"].startswith("f"):
            out[p["label"]] = float(p["value"])
    return out


def runs_of(arm: str) -> list[int]:
    return list(range(N_FLOOR)) if arm == "N1-R" else list(range(N_SESSIONS))


def delta_m(camp: Campaign, arm: str, direction: str, label: str) -> dict[int, float]:
    """Δm(d) = m(c_steer(d)) − m(c_uns) per session (n §4), for one (arm, direction, kept label), keyed by BK's run.
    Called only on a usable arm with usable shadows (build_state's guard): a missing or non-finite read here STOPs."""
    out = {}
    for run in runs_of(arm):
        sid = session_key(run)
        r, sh = camp.records.get(f"{arm}|{direction}|{label}|{sid}"), camp.records.get(f"N1-V|none|0|{sid}")
        if r is None or sh is None or not r["finite"] or not sh["finite"]:
            raise AnlStop(f"STOP: Δm of {arm}|{direction}|{label} at {sid} without a finite read and shadow")
        out[run] = float(r["margin"]) - float(sh["margin"])
    return out


def _vec(d: Mapping[int, float]) -> np.ndarray:
    return np.array([d[k] for k in sorted(d)], float)


STEERED_ARMS = ("N1-V", "N1-R", "N1-P", "N2-E", "N2-S", "N2-C")


def build_state(camp: Campaign, *, paused: Mapping[str, bool], gread: Mapping[tuple, str],
                drop: Callable[[str], bool] | None = None) -> tuple[State, dict]:
    """The outcome layer's State from the campaign (n §4), and the figures beside it. ``paused``: per arm, whether an
    unadjudicated pause stands on its reads (the stage report's). ``drop``: the TAU/4 sensitivity row's read filter
    (PIN-n-16), None for the primary (ungated, n §2.1).

    An arm's statistics are computed only when it is usable (PIN-n-20) and, for a steered arm, when the shadows (N1-V's
    d = 0 reads) of every session it reads are usable (N1-R's 40 floor sessions, the others' 160); a steered arm whose
    own reads are usable but whose shadows are not is marked `shadow`. In the TAU/4 row an arm left with no session at some point is marked `tau4-emptied` (never a STOP), and
    each statistic's matrix is drawn from its arm's stream for that statistic's session count (PIN-n-12)."""
    ident, dmap = camp.identity, camp.dmap
    lv = label_values(ident)
    v_pts = sorted({lv[x] for x in lv}, reverse=True)                     # N1-V's points, 0 included
    labels_v = {x: lv[x] for x in lv if x != "0"}
    missing = {a: len(camp.planned[a] - camp.present[a]) for a in ARMS}
    nonfin = {a: len(camp.nonfinite[a]) for a in ARMS}
    def shadows_ok(arm: str) -> bool:
        ids = (f"N1-V|none|0|{session_key(r)}" for r in runs_of(arm))
        return all(s in camp.present["N1-V"] and camp.records[s]["finite"] for s in ids)
    unusable: dict[str, str] = {}
    for a in STEERED_ARMS:
        if a != "N1-V" and camp.usable(a) and not shadows_ok(a):
            unusable[a] = "shadow"
    st = State(dmap=dmap, complete={a: camp.usable(a) and a not in unusable for a in ARMS},
               paused={a: bool(paused.get(a)) for a in ARMS}, gread=dict(gread), missing=missing, nonfinite=nonfin,
               unusable=unusable)
    fig: dict = {"n": {}, "sd0": {}, "dir_means": {}, "dir_slopes": {}, "P_signed": {}, "slopes_N2": {},
                 "floors_N2": {}}

    def dm(arm, direction, label):
        d = delta_m(camp, arm, direction, label)
        if drop is None:
            return d
        return {run: x for run, x in d.items() if not (drop(f"N1-V|none|0|{session_key(run)}")
                                                        or drop(f"{arm}|{direction}|{label}|{session_key(run)}"))}

    def emptied(arm, *vecs) -> bool:
        if any(len(v) == 0 for v in vecs):
            st.complete[arm] = False
            st.unusable[arm] = "tau4-emptied"
            return True
        return False

    def slope_est(arm, pts, vecs):
        common = sorted(set.intersection(*[set(v) for v in vecs]))
        if not common:
            return None, 0, None
        Y = np.array([[vv[r] for vv in vecs] for r in common])
        sl = session_slopes(pts, Y)
        return mean_est(sl, boot_index(arm, len(common))), len(common), sl

    if st.complete["N1-V"]:
        vecs = {pt: dm("N1-V", "valence", lab) for lab, pt in labels_v.items()}
        if not emptied("N1-V", *vecs.values()):
            for lab, pt in labels_v.items():
                st.V[pt] = mean_est(_vec(vecs[pt]), boot_index("N1-V", len(vecs[pt])))
                fig["n"][("N1-V", lab)] = len(vecs[pt])
                fig["sd0"][("N1-V", lab)] = sd0(_vec(vecs[pt]))
            zero = {r: 0.0 for r in range(N_SESSIONS)}
            est, n_c, sl = slope_est("N1-V", v_pts, [zero if pt == 0.0 else vecs[pt] for pt in v_pts])
            if est is None:
                emptied("N1-V", [])
            else:
                st.slope_V, fig["slope_V_n"], fig["slope_V_sd0"] = est, n_c, sd0(sl)
    if st.complete["N1-R"]:
        dirs = tuple(f"rand_{i:02d}" for i in range(N_RANDOM))
        dv = {(d_, lab): dm("N1-R", d_, lab) for d_ in dirs for lab in labels_v}
        if not emptied("N1-R", *dv.values()):
            for lab, pt in labels_v.items():
                means = {d_: float(_vec(dv[(d_, lab)]).mean()) for d_ in dirs}
                for d_ in dirs:
                    fig["dir_means"][(d_, lab)] = means[d_]
                st.L[pt] = max(abs(x) for x in means.values())
            zero = {r: 0.0 for r in range(N_FLOOR)}
            slopes = {}
            for d_ in dirs:
                pts_vecs = [zero if pt == 0.0 else dv[(d_, next(l for l, p in labels_v.items() if p == pt))]
                            for pt in v_pts]
                est, n_c, sl = slope_est("N1-R", v_pts, pts_vecs)
                slopes[d_] = float(sl.mean()) if sl is not None else float("nan")
                fig["dir_slopes"][d_] = slopes[d_]
            if any(math.isnan(x) for x in slopes.values()):
                emptied("N1-R", [])
            else:
                st.floor_V = max(abs(x) for x in slopes.values())
                fig["floor_dir"] = max(slopes, key=lambda k: (abs(slopes[k]), k))
                # OPEN-Q9 (pending the seat): N2's floor on the random reads at d_eq's and d_20's points
                p10, p20 = dmap.norm_matched(F10), dmap.norm_matched(F20)
                lab_of = {p: l for l, p in labels_v.items()}
                n2_slopes = {}
                for d_ in dirs:
                    _, _, sl = slope_est("N1-R", (0.0, p10, p20), [zero, dv[(d_, lab_of[p10])], dv[(d_, lab_of[p20])]])
                    n2_slopes[d_] = float(sl.mean())
                fig["floors_N2"] = {"points": [0.0, p10, p20], "floor": max(abs(x) for x in n2_slopes.values())}
    if st.complete["N1-P"]:
        pv = {pt: dm("N1-P", "valence", lab) for lab, pt in (("+1", 1.0), ("-1", -1.0))}
        if not emptied("N1-P", *pv.values()):
            for lab, pt in (("+1", 1.0), ("-1", -1.0)):
                e = mean_est(_vec(pv[pt]), boot_index("N1-P", len(pv[pt])))
                st.P[pt] = abs(e.mean)
                fig["P_signed"][lab] = e.as_json()
                fig["n"][("N1-P", lab)] = len(pv[pt])
    for arm, d_ in GUARD_DIRS.items():
        if not st.complete[arm]:
            continue
        fv = {f: dm(arm, d_, lab) for lab, f in (("f0.10", F10), ("f0.20", F20))}
        if emptied(arm, *fv.values()):
            continue
        tgt = {"N2-E": st.E, "N2-S": st.S, "N2-C": st.C}[arm]
        for lab, f in (("f0.10", F10), ("f0.20", F20)):
            tgt[f] = mean_est(_vec(fv[f]), boot_index(arm, len(fv[f])))
            fig["n"][(arm, lab)] = len(fv[f])
            fig["sd0"][(arm, lab)] = sd0(_vec(fv[f]))
        pts, _ = dmap.n2_slope_points()                                   # OPEN-Q9 (pending the seat)
        est, n_c, _ = slope_est(arm, pts, [{r: 0.0 for r in range(N_SESSIONS)}, fv[F10], fv[F20]])
        fig["slopes_N2"][arm] = None if est is None else dict(est.as_json(), n=n_c, points=list(pts))
    if st.complete["N4-T"] and st.complete["N4-Ts"]:
        told, sham = [], []
        for run in range(N_SESSIONS):
            sid = session_key(run)
            for arm, acc in (("N4-T", told), ("N4-Ts", sham)):
                r = camp.records[f"{arm}|none|0|{sid}"]
                if drop is not None and drop(r["read_id"]):
                    continue
                acc.append(float(r["margin"]) if r["schedule_zone"] == "S" else -float(r["margin"]))
        if not emptied("N4-T", told) and not emptied("N4-Ts", sham):
            st.told = mean_est(told, boot_index("N4-T", len(told)), PCT98)
            st.e_sham = abs(float(np.mean(sham)))
            fig["n"][("N4-T", "0")], fig["n"][("N4-Ts", "0")] = len(told), len(sham)
    return st, fig


# =====================================================================================================================
# 12. Filling the sentences (VERDICTS)
# =====================================================================================================================
# Figures: nats to four decimals with their sign (Δm, slopes, m_told); ceilings, floors and E unsigned to four; an AUC
# to three; d_eq's value to four (Code's form, under OPEN-Q8).


def _n(x: float) -> str:
    return f"{x:+.4f}"


def _u(x: float) -> str:
    return f"{x:.4f}"


def _ci(e: Est) -> str:
    return f"[{_n(e.lo)}, {_n(e.hi)}]"


ROUTE_TEXT = {"A": "on their direction", "B": "on a reconstructed direction"}


VALUE_MERGED = "{value} (read at d = {point}, the point it merges into under §2.3)"


def value_text(dm: DoseMap, point: float) -> str:
    """The dose sentence's [value]: d_eq to four decimals; where §2.3's merge moved d_eq onto another point, that point
    beside it, since [x] and [CI] are read there (VALUE_MERGED, Code's form, under OPEN-Q8)."""
    if point == dm.d_eq:
        return _u(dm.d_eq)
    lab = BK_LABEL.get(point)
    return VALUE_MERGED.format(value=_u(dm.d_eq), point=lab if lab is not None else _u(point))


def code_forms() -> dict[str, str]:
    """Every sentence form Code wrote where §5 words none (OPEN-Q8: the question block's Appendix A, and
    VALUE_MERGED), by name; the battery pins them by digest (CODE_FORMS_SHA256), so that none changes unseen."""
    f = {"C_N1_PARTIAL": C_N1_PARTIAL, "C_N1_NOT_REPLICATED": C_N1_NOT_REPLICATED, "C_N1_INDET": C_N1_INDET,
         "C_DOSE_ND_NOT_READABLE": C_DOSE_ND_NOT_READABLE, "C_DOSE_ND_READABLE_N4": C_DOSE_ND_READABLE_N4,
         "C_DOSE_INDET": C_DOSE_INDET, "C_NOT_RUN": C_NOT_RUN, "VALUE_MERGED": VALUE_MERGED}
    for fam, d in (("C_N2", C_N2), ("C_N4", C_N4), ("CONJUNCT_TEXT", CONJUNCT_TEXT),
                   ("NOT_RUN_CAUSES", NOT_RUN_CAUSES), ("ROUTE_TEXT", ROUTE_TEXT)):
        f |= {f"{fam}[{k}]": v for k, v in d.items()}
    return f


#: sha256 of _canon(code_forms()) -- a changed form fails the battery until this pin is moved, in the open
CODE_FORMS_SHA256 = "50d78c1c06d8fdc5e011e92b2c48714f744f7c1f6c6e9db51c123e7ec5b16a8b"


def fill(sent: Mapping[str, Any], o: Mapping[str, Any], st: State, *, route: str, auc: Mapping[str, float | None],
         reason: str | None = None) -> dict:
    """One sentence of the set with its slots filled from the outcome and the state; refuses (STOP) if a slot is
    left. ``auc``: G-READ-n's band median AUC at the cells the dose sentence names ('d_eq')."""
    t = sent["text"]
    q = sent["question"]
    sub: dict[str, str] = {}
    if route not in ROUTE_TEXT:
        raise AnlStop(f"STOP: the direction route {route!r} is neither A nor B")
    if q == "unit":
        sub["[reason]"] = reason or ""
    elif q == "N1":
        n1 = o["N1"]
        if n1["state"] == "INDETERMINATE":
            sub["[causes]"] = ", ".join(n1["causes"])
        else:
            v1, vm1 = st.V[1.0], st.V[-1.0]
            sub.update({ROUTE_SLOT: ROUTE_TEXT[route], "[x]": _n(v1.mean), "[CI]": _ci(v1),
                        "[y]": _n(st.slope_V.mean), "[z]": _u(st.floor_V), "[max(L, P)]": _u(n1["ceiling"]),
                        "[x−]": _n(vm1.mean), "[CI−]": _ci(vm1), "[failing]": failing_text(n1["failing"])})
    elif q == "dose":
        d = o["dose"]
        if d["state"] == "INDETERMINATE":
            sub["[causes]"] = ", ".join(d["causes"])
        else:
            v = st.V[d["point"]]
            a = auc.get("d_eq")
            if a is None and "[a]" in t:
                raise AnlStop("STOP: a dose sentence that calls the state readable carries no AUC (G-READ-n's band "
                              "median at d_eq)")
            sub.update({"[value]": value_text(st.dmap, d["point"]), "[x]": _n(v.mean), "[CI]": _ci(v),
                        "[c]": _u(d["ceiling"]),
                        "[a]": "not computed" if a is None else f"{a:.3f}"})
    elif q == "N2":
        n2 = o["N2"]
        if n2["state"] == "INDETERMINATE":
            sub["[causes]"] = ", ".join(n2["causes"])
        else:
            e20 = st.E[F20]
            sub.update({"[xE]": _n(e20.mean), "[CIE]": _ci(e20), "[c]": _u(n2["ceiling"]),
                        "[xV]": _n(st.V[n2["point"]].mean)})
    elif q == "N4":
        n4 = o["N4"]
        if n4["no_read"]:
            sub["[causes]"] = ", ".join(n4["causes"])
        else:
            sub.update({"[x]": _n(st.told.mean), "[CI98]": _ci(st.told), "[e]": _u(n4["E"]), "[-e]": _n(-n4["E"])})
    out = t
    for k in sorted(sub, key=len, reverse=True):
        out = out.replace(k, sub[k])
    left = [s for s in SLOTS if s in out]
    if left:
        raise AnlStop(f"STOP: a sentence keeps slots {left} after filling ({q}, {sent['state']})")
    return dict(sent, text=out)


def sentence_set_filled(o: Mapping[str, Any], st: State, *, route: str, auc: Mapping[str, float | None]) -> dict:
    """The §7 sentence set for a VERDICTS: the tuple's template set (sentence_set, the same functions the battery's
    tuple pass asserts), with its N1 failing conjuncts, its INDETERMINATE causes and every figure filled."""
    gr = o["gread"]
    t = o["tuple"]
    base = sentence_set(t, gr1="PASS" if gr["+1"] == "PASS" else "FAIL", gre="PASS" if gr["E"] == "PASS" else "FAIL",
                        n4_no_read=bool(o["N4"].get("no_read")) and o["N4"]["state"] == "INDETERMINATE")
    return {k: fill(v, o, st, route=route, auc=auc) for k, v in base.items()}


# =====================================================================================================================
# 13. Counters (rule 23: over every read, the non-finite included) and secondaries (n §4; rule 28(a); no claim)
# =====================================================================================================================
COUNTER_NAMES = ("fidelity re-computations", "fidelity exceedances at TAU", "fidelity exceedances at TAU/4",
                 "non-finite re-computations", "non-finite margins", "label mass below .20", "identity bound exceeded")


def counters(camp: Campaign) -> dict:
    """n §4's counters by arm and dose label, over every read in the campaign (rule 23); the rendering-mismatch
    counter is the stage report's (a mismatch is a STOP, never a record; schema docstring)."""
    out: dict = {}
    for r in camp.records.values():
        key = f"{r['arm']}|{r['dose_label']}"
        c = out.setdefault(key, {n: 0 for n in COUNTER_NAMES} | {"reads": 0})
        c["reads"] += 1
        f = r["fidelity"]
        if f is not None:
            c["fidelity re-computations"] += 1
            c["fidelity exceedances at TAU"] += bool(f["exceeds_tau"])
            c["fidelity exceedances at TAU/4"] += bool(f["exceeds_tau4"])
            c["non-finite re-computations"] += not f["finite"]
        if not r["finite"]:
            c["non-finite margins"] += 1
        else:
            c["label mass below .20"] += label_mass_below([r["restricted"]["label_mass"]])
        if r["identity"] is not None and not r["identity"]["within"]:
            c["identity bound exceeded"] += 1
    return {k: out[k] for k in sorted(out)}


def tau4_drop(camp: Campaign) -> Callable[[str], bool]:
    """PIN-n-16's filter for the sensitivity row: a read whose re-computation exceeds TAU/4 (a shadow that exceeds
    drops its session at every point through build_state); a read with no re-computation is kept."""
    def drop(rid: str) -> bool:
        r = camp.records.get(rid)
        return bool(r is not None and r["fidelity"] is not None and r["fidelity"]["exceeds_tau4"])
    return drop


def secondaries(camp: Campaign, st: State, gvec: Mapping[str, Any] | None) -> dict:
    """n §4's secondaries (a)-(e); (f) is the VERDICTS' sensitivity row. Descriptive, issuing no claim (rule 11). The
    readings of (a), (c) and the n ≥ 20 floor of (a), (c) and (d) are PIN-n-22's; (d)'s r is PIN-n-18's."""
    out: dict = {"floor_events": FLOOR_EVENTS}
    a = {}
    for r in camp.records.values():
        if not r["finite"]:
            continue
        k = f"{r['arm']}|{r['dose_label']}"
        x = a.setdefault(k, {"n": 0, "pick_S": 0})
        x["n"] += 1
        x["pick_S"] += r["restricted"]["pick"] == "S"
    out["a_first_pick_share"] = {k: dict(v, share=(v["pick_S"] / v["n"] if v["n"] >= FLOOR_EVENTS else None),
                                         below_floor=v["n"] < FLOOR_EVENTS) for k, v in sorted(a.items())}
    out["b_free_text"] = "not recorded: n §2.1 'No new text is generated for N1, N2 or N4' (the schema's reading 7)"
    c: dict = {}
    for r in camp.records.values():
        if r["shadow_read_id"] is None or not r["finite"]:
            continue
        sh = camp.records.get(r["shadow_read_id"])
        if sh is None or not sh["finite"]:
            continue
        x = float(r["margin"]) - float(sh["margin"])
        k = f"{r['arm']}|{r['dose_label']}"
        for g in (f"present_first_is_S={r['present_first_is_S']}", f"pair={r['cue_S']}|{r['cue_U']}"):
            c.setdefault(k, {}).setdefault(g, []).append(x)
    out["c_groups"] = {k: {g: ({"n": len(v), "mean": float(np.mean(v))} if len(v) >= FLOOR_EVENTS else {"n": len(v)})
                           for g, v in sorted(gs.items())} for k, gs in sorted(c.items())}
    ri, dmv = [], []
    for run in range(N_SESSIONS):
        sid = session_key(run)
        r, sh = camp.records.get(f"N1-V|valence|+1|{sid}"), camp.records.get(f"N1-V|none|0|{sid}")
        if r is not None and sh is not None and r["finite"] and sh["finite"]:
            ri.append(float(r["retention_interval"]))
            dmv.append(float(r["margin"]) - float(sh["margin"]))
    out["d_retention_r"] = {"n": len(ri), "pearson_r": pearson_r(ri, dmv) if len(ri) >= FLOOR_EVENTS else None}
    e = {"means": {}, "cosines": None}
    for arm, d_ in GUARD_DIRS.items():
        for f in (F10, F20):
            est = {"N2-E": st.E, "N2-S": st.S, "N2-C": st.C}[arm].get(f)
            e["means"][f"{d_}|{f}"] = None if est is None else est.as_json()
    for f in (F10, F20):
        pt = st.dmap.norm_matched(f)
        e["means"][f"valence|{f}"] = st.V[pt].as_json() if pt in st.V else None
    if gvec is not None:
        names = ("span_character", "span_reward", "span_sentiment", "valence")
        e["cosines"] = {f"{x}|{y}": gvec["cosines"].get(f"{x}|{y}") for i, x in enumerate(names) for y in names[i + 1:]}
    out["e_directions"] = e
    return out


# --- the battery's reader path: synthetic campaigns through the schema's own builders -------------------------------
def _bt_margin_tokens(m: float) -> tuple[list[float], list[float]]:
    """Three non-positive log-prob tokens per label whose sums differ by m (margin = logprob_S - logprob_U)."""
    s = 1.0 + max(0.0, -m)
    return [0.0, 0.0, -s], [0.0, 0.0, -(s + m)]


def _bt_write_campaign(root: Path, sm, *, R_ell: float = 23.90625, delta: Callable[[str, str, str, int], float],
                       told: Callable[[int, str], float] = lambda r, z: 1.0 + 0.05 * ((r % 4) - 1.5),
                       sham: Callable[[int, str], float] = lambda r, z: 0.02 * ((r % 5) - 2),
                       omit: Sequence[tuple] = (), nonfinite: Sequence[str] = (), fresh_shift: Mapping[str, float] = {},
                       mutate: Callable[[dict], None] | None = None,
                       first_is_s: Callable[[int], bool] = lambda r: r % 3 == 0) -> Path:
    """Write a synthetic campaign (every cell of the plan over the example identity's dose map) to ``root``: shadows
    m0(run) = 0.1 + 0.01 (run % 7); each steered read m0 + delta(arm, direction, label, run); N4-T's margin toward its
    told zone told(run, zone) and N4-Ts's toward its referent zone sham(run, zone), the zone S for even runs;
    ``omit``: (arm, direction, label) cells left out; ``nonfinite``: read_ids written non-finite; ``fresh_shift``:
    read_id -> fresh shift; ``first_is_s``: a run's present order (S first)."""
    root.mkdir(parents=True, exist_ok=True)
    ident = sm.example_identity(R_ell=R_ell)
    kept = sm.dose_point_values(ident)
    launch = 0
    for arm, rows in PLAN_TABLE.items():
        for dirs, labels in rows:
            for d_ in dirs:
                for lab in labels:
                    if lab not in kept or (arm, d_, lab) in omit:
                        continue
                    recs = []
                    for i, run in enumerate(runs_of(arm)):
                        zone = "S" if run % 2 == 0 else "U"
                        m0 = 0.1 + 0.01 * (run % 7)
                        if arm == "N4-T":
                            m = told(run, zone) * (1 if zone == "S" else -1)
                        elif arm == "N4-Ts":
                            m = sham(run, zone) * (1 if zone == "S" else -1)
                        elif d_ == "none":
                            m = m0
                        else:
                            m = m0 + delta(arm, d_, lab, run)
                        ts, tu = _bt_margin_tokens(m)
                        rid = f"{arm}|{d_}|{lab}|{session_key(run)}"
                        rec = sm.example_record(ident, arm, d_, lab, run, launch=launch, row=i, zone=zone,
                                                logprob_S_tokens=ts, logprob_U_tokens=tu,
                                                present_first_is_S=first_is_s(run), finite=rid not in nonfinite,
                                                fresh_shift=fresh_shift.get(rid, 0.0))
                        launch += 1
                        recs.append(rec)
                    name = sm.cell_filename(arm, d_, lab)
                    cell = {"schema": sm.CELL_SCHEMA, "stage_identity": ident, "arm": arm, "direction_id": d_,
                            "dose_label": lab, "records": recs, "capture_file": name[:-5] + ".npy",
                            "capture_rows": len(recs), "capture_sha256": hashlib.sha256(b"").hexdigest()}
                    if mutate is not None:
                        mutate(cell)
                    (root / name).write_text(json.dumps(cell), encoding="utf-8")
                    (root / (name[:-5] + ".npy")).write_bytes(b"")
    return root


def _bt_delta_positive(arm: str, d_: str, lab: str, run: int) -> float:
    """N1-V and N2-E move with the dose (Δm = d on BK's scale, f·4 on N2's), small session spread; the random and
    same-pole arms and the guards stay near 0."""
    wobble = 0.03 * ((run % 4) - 1.5)
    pts = {"+1": 1.0, "+1/2": 0.5, "-1": -1.0, "+d_20": 0.625, "+d_eq": 0.3125, "f0.10": 0.3125, "f0.20": 0.625}
    if arm == "N1-V" or arm == "N2-E":
        return pts[lab] + wobble
    return 0.01 * ((run % 3) - 1)


_BT_PTS = {"+1": 1.0, "+1/2": 0.5, "-1": -1.0, "+d_20": 0.625, "+d_eq": 0.3125, "f0.10": 0.3125, "f0.20": 0.625}
_BT_RAND_NEG = "rand_05"


def _bt_asym(arm: str, d_: str, lab: str, run: int) -> float:
    """F11's asymmetric campaign (the example map: d_eq 0.3125, d_20 0.625): N1-V moves with the dose plus a session
    offset of mean +0.045 (so the slope's d = 0 point moves the slope); rand_05 has a negative slope and an offset
    (−0.8·d + 0.05; L = its |mean|, the floor its |slope|); N1-P is −0.9 at +1 and +0.2 at −1 (P(+1) above L(+1));
    N2-E is +1.0 plus the offset at f = 0.10 and +0.1 plus twice the offset at f = 0.20 (so the two f labels' means
    and SDs differ); the rest stay near 0."""
    w = 0.03 * (run % 4)
    if arm == "N1-V":
        return _BT_PTS[lab] + w
    if arm == "N1-R" and d_ == _BT_RAND_NEG:
        return -0.8 * _BT_PTS[lab] + 0.05
    if arm == "N1-P":
        return (-0.9 if lab == "+1" else 0.2) + 0.01 * ((run % 3) - 1)
    if arm == "N2-E":
        return (1.0 + w) if lab == "f0.10" else (0.1 + 2.0 * w)
    return 0.01 * ((run % 3) - 1)


def _bt_asym_told(r: int, z: str) -> float:
    # m_told's mean 0.6, a ± 3.53 split: its 95% CI excludes 0, its 98% CI does not (checked by hand in RD-ASYM)
    return 0.6 + 3.53 if r % 2 == 0 else 0.6 - 3.53


def _bt_asym_sham(r: int, z: str) -> float:
    return -0.3 + 0.02 * ((r % 5) - 2)              # E = |mean| = 0.3, the sham mean negative


def _bt_gread_all(dmap: DoseMap, state: str = "PASS") -> dict:
    g = {("valence", p): state for p in dmap.points() if p != 0.0}
    return g | {("span_reward", F10): state, ("span_reward", F20): state}


def _bt_eval(root: Path, sm, *, paused: Mapping[str, bool] | None = None, gread: Mapping | None = None,
             drop: bool = False):
    camp = load_campaign(root, sm)
    st, fig = build_state(camp, paused=paused or {}, gread=gread if gread is not None else _bt_gread_all(camp.dmap),
                          drop=tau4_drop(camp) if drop else None)
    return camp, st, fig, outcomes(st)


def _bt_reader(B: _Battery) -> None:
    import tempfile
    sm = schema_module()
    with tempfile.TemporaryDirectory(prefix="n_anl_rd_") as td:
        base = Path(td)
        pos = _bt_write_campaign(base / "pos", sm, delta=_bt_delta_positive)
        camp, st, fig, o = _bt_eval(pos, sm)
        B.chk("reader path: a campaign written with the schema's builders (7,360 reads, 136 cells, nothing merged) "
              "reads back through check_cell to (REPLICATED, DETECTABLE, SHARED, PASS, PASS)",
              o["tuple"] == ("REPLICATED", "DETECTABLE", "SHARED", "PASS", "PASS") and len(camp.records) == 7360
              and len(camp.cells) == 136, (o["tuple"], len(camp.records), len(camp.cells)), cover=["RD-POSITIVE"])
        sset = sentence_set_filled(o, st, route="B", auc={"d_eq": 0.95})
        B.chk("reader path: the filled sentence set keeps no slot; N1's sentence is §5's with the figures and 'on a "
              "reconstructed direction'", all(not any(s in v["text"] for s in SLOTS) for v in sset.values())
              and sset["7.1"]["text"].startswith("BK's fixed-text effect replicates on OLMo-2-32B Instruct in this "
                                                 "program's implementation on a reconstructed direction: Δm(+1) = +"),
              sset["7.1"]["text"][:160], cover=["RD-FILLED"])
        # F10: every filled figure against the battery's own literal text (its own formatting; the module's
        # templates, slot map and number forms are not used to build the expectation)
        def f4(x): return f"{x:+.4f}"
        def u4(x): return f"{x:.4f}"
        def ci4(e): return f"[{e.lo:+.4f}, {e.hi:+.4f}]"
        def ceil_at(s, pt): return max(s.L[pt], s.P[pt]) if pt in s.P else s.L[pt]
        rd = "on a reconstructed direction"
        n2h = "N2, descriptive (§7.3; it licenses no thesis sentence): "
        deq, d20 = camp.dmap.resolved()["d_eq"], camp.dmap.resolved()["d_20"]
        want_pos = {
            "7.1": (f"BK's fixed-text effect replicates on OLMo-2-32B Instruct in this program's implementation {rd}: "
                    f"Δm(+1) = {f4(st.V[1.0].mean)} nats {ci4(st.V[1.0])}, theirs 1.09 [1.00, 1.19]; slope "
                    f"{f4(st.slope_V.mean)} against a floor of {u4(st.floor_V)}; leak ceiling {u4(ceil_at(st, 1.0))}"),
            "7.2": (f"at d_eq = {u4(camp.dmap.d_eq)} — this program's f = 0.10 on BK's scale — the effect is "
                    f"{f4(st.V[deq].mean)} nats {ci4(st.V[deq])} above a leak ceiling of {u4(ceil_at(st, deq))}: dose "
                    "alone does not account for the program's null on the echo channel"),
            "7.3": (n2h + "SHARED: at f = 0.20 this program's evaluative axis (span_reward) moves BK's apparatus "
                    f"beyond the leak ceiling (Δm = {f4(st.E[F20].mean)} nats {ci4(st.E[F20])} against "
                    f"{u4(ceil_at(st, d20))}); the valence direction of record at the norm-matched point: Δm = "
                    f"{f4(st.V[d20].mean)} nats"),
            "N4": (f"PASS: BK's apparatus registers an instructed preference on this checkpoint: m_told = "
                   f"{f4(st.told.mean)} nats {ci4(st.told)} against E = {u4(st.e_sham)}; it licenses the answered "
                   "reading of nulls in this format on this checkpoint (§0.6, with G-READ-n), nothing else")}
        B.chk("reader path: the filled set (REPLICATED, DETECTABLE, SHARED, PASS) equals the battery's literal text, "
              "figure for figure: Δm, CIs, slope, floor, the ceilings max(L, P) at +1, d_eq and the norm-matched point, "
              "m_told's 98% CI and E", {k: sset[k]["text"] for k in want_pos} == want_pos,
              [k for k in want_pos if sset[k]["text"] != want_pos[k]], cover=["RD-FILLED-FIGURES"])
        null = _bt_write_campaign(base / "null", sm, delta=lambda a, d, l, r: 0.01 * ((r % 3) - 1),
                                  told=lambda r, z: 0.02 * ((r % 5) - 2))
        o2 = _bt_eval(null, sm)[3]
        B.chk("reader path: nothing moves -> (NOT-REPLICATED, NOT-DETECTABLE, NULL, DEAD)", o2["tuple"][:4] ==
              ("NOT-REPLICATED", "NOT-DETECTABLE", "NULL", "DEAD"), o2["tuple"], cover=["RD-NULL"])
        spec = _bt_write_campaign(base / "spec", sm,
                                  delta=lambda a, d, l, r: 0.0 if a == "N2-E" else _bt_delta_positive(a, d, l, r),
                                  told=lambda r, z: -1.0 + 0.05 * ((r % 4) - 1.5),
                                  sham=lambda r, z: 0.1 + 0.02 * ((r % 5) - 2))
        _c3, st3, _f3, o3 = _bt_eval(spec, sm)
        B.chk("reader path: span_reward still, the valence direction moving -> N2 SPECIFIC; the told line pulling the "
              "other way -> N4 REVERSE", o3["tuple"][2:4] == ("SPECIFIC", "REVERSE"), o3["tuple"], cover=["RD-SPECIFIC"])
        part = _bt_write_campaign(base / "part", sm,
                                  delta=lambda a, d, l, r: 0.3 * _bt_delta_positive(a, d, l, r) if a == "N1-V"
                                  else _bt_delta_positive(a, d, l, r),
                                  told=lambda r, z: 2.0 if r % 2 == 0 else -1.5)
        _c4, st4, _f4, o4 = _bt_eval(part, sm)
        B.chk("reader path: Δm(+1) near 0.3 -> N1 PARTIAL failing (i); a told margin split +2 / -1.5 -> N4 "
              "INDETERMINATE (terminal)", o4["N1"]["state"] == "PARTIAL" and o4["N1"]["failing"] == ["i"]
              and o4["N4"]["state"] == "INDETERMINATE" and not o4["N4"]["no_read"], (o4["tuple"], o4["N1"].get("failing")),
              cover=["RD-PARTIAL"])
        s3 = sentence_set_filled(o3, st3, route="A", auc={"d_eq": 0.9})
        s4 = sentence_set_filled(o4, st4, route="B", auc={"d_eq": 0.9})
        want_forms = {
            ("spec", "7.3"): (n2h + "SPECIFIC: at f = 0.20 this program's evaluative axis (span_reward) does not move "
                              f"BK's apparatus beyond the leak ceiling (Δm = {f4(st3.E[F20].mean)} nats against "
                              f"{u4(ceil_at(st3, d20))}) while the valence direction of record at the norm-matched "
                              f"point does (Δm = {f4(st3.V[d20].mean)} nats) — concluded, not answered"),
            ("spec", "N4"): (f"REVERSE: m_told = {f4(st3.told.mean)} nats {ci4(st3.told)} below −E = "
                             f"{f4(-st3.e_sham)}"),
            ("part", "7.1"): ("PARTIAL: BK's fixed-text effect on OLMo-2-32B Instruct, in this program's "
                              f"implementation {rd}, meets (ii) and (iii) and its CI at d = +1 excludes 0, but conjunct "
                              "(i) (Δm(+1) ≥ 0.545 nats with its 95% CI excluding 0) fails: Δm(+1) = "
                              f"{f4(st4.V[1.0].mean)} nats {ci4(st4.V[1.0])}, theirs 1.09 [1.00, 1.19]; Δm(−1) = "
                              f"{f4(st4.V[-1.0].mean)} nats {ci4(st4.V[-1.0])}; slope {f4(st4.slope_V.mean)} against "
                              f"a floor of {u4(st4.floor_V)}; leak ceiling {u4(ceil_at(st4, 1.0))}"),
            ("part", "N4"): f"INDETERMINATE: m_told = {f4(st4.told.mean)} nats {ci4(st4.told)} against E = "
                            f"{u4(st4.e_sham)}"}
        got_forms = {(c, k): (s3 if c == "spec" else s4)[k]["text"] for c, k in want_forms}
        B.chk("reader path: Code's forms filled, against the battery's literal text: N2 SPECIFIC with its label, N4 "
              "REVERSE with −E printed negative (E = 0.1), N1 PARTIAL with its failing conjunct and Δm(−1), N4's "
              "terminal INDETERMINATE", got_forms == want_forms and st3.e_sham > 0.05,
              [k for k in want_forms if got_forms[k] != want_forms[k]], cover=["RD-FILLED-FORMS"])
        ind = _bt_write_campaign(base / "ind", sm, delta=_bt_delta_positive,
                                 omit=[("N1-R", "rand_07", "+1/2"), ("N4-Ts", "none", "0")])
        o5 = _bt_eval(ind, sm)[3]
        B.chk("reader path: a missing N1-R cell -> N1, dose and N2 INDETERMINATE (incomplete:N1-R); a missing N4-Ts "
              "cell -> N4 INDETERMINATE, no read obtained", o5["tuple"][:4] == ("INDETERMINATE",) * 4
              and o5["N1"]["causes"] == ["incomplete:N1-R"] and o5["N4"]["no_read"]
              and o5["N4"]["causes"] == ["incomplete:N4-Ts"], (o5["N1"], o5["N4"]), cover=["RD-INDET"])
        nf = _bt_write_campaign(base / "nf", sm, delta=_bt_delta_positive,
                                nonfinite=[f"N1-V|valence|+1|{session_key(17)}"])
        camp6, st6, fig6, o6 = _bt_eval(nf, sm)
        B.chk("reader path: one non-finite read in N1-V at +1 -> N1-V not usable (PIN-n-20) -> N1 INDETERMINATE "
              "(nonfinite:N1-V), every planned read counted present; the counter tabulates it",
              o6["N1"]["state"] == "INDETERMINATE" and o6["N1"]["causes"] == ["nonfinite:N1-V"]
              and camp6.present["N1-V"] == camp6.planned["N1-V"] and st6.missing["N1-V"] == 0
              and counters(camp6)["N1-V|+1"]["non-finite margins"] == 1, o6["N1"], cover=["RD-NONFINITE"])
        # F1: a non-finite shadow (N1-V's d = 0 read) at a session N1-R does not read (run 100 >= 40): N1-V is not
        # usable, N1-P and the N2 arms are marked `shadow`, N1-R keeps its statistics, N4 is decided; no exception.
        nfs = _bt_write_campaign(base / "nfs", sm, delta=_bt_delta_positive,
                                 nonfinite=[f"N1-V|none|0|{session_key(100)}"])
        camp10, st10, fig10, o10 = _bt_eval(nfs, sm)
        B.chk("reader path: a non-finite shadow at run 100 -> N1, dose and N2 INDETERMINATE, N1's causes "
              "(nonfinite:N1-V, shadow:N1-P), N2's (shadow:N2-E, nonfinite:N1-V); N1-R (40 floor sessions) keeps its "
              "floor and L; N4 PASS", o10["tuple"][:4] == ("INDETERMINATE",) * 3 + ("PASS",)
              and o10["N1"]["causes"] == ["nonfinite:N1-V", "shadow:N1-P"]
              and o10["N2"]["causes"] == ["shadow:N2-E", "nonfinite:N1-V"]
              and st10.unusable == {"N1-P": "shadow", "N2-E": "shadow", "N2-S": "shadow", "N2-C": "shadow"}
              and st10.floor_V is not None and len(st10.L) == len(camp10.dmap.points()) - 1,
              (o10["tuple"], o10["N1"].get("causes"), o10["N2"].get("causes"), st10.unusable), cover=["RD-SHADOW"])
        mg = _bt_write_campaign(base / "mg", sm, R_ell=50.0,
                                delta=lambda a, d, l, r: (-0.9 if (a == "N1-P" and l == "+1")
                                                          else _bt_delta_positive(a, d, l, r)))
        camp7, st7, fig7, o7 = _bt_eval(mg, sm)
        B.chk("reader path: R_ell 50 merges +d_20 into +1 -> 6,240 reads; N2's norm-matched point is +1, the ratio "
              "2·d_eq reported; N1-P at −0.9 there puts P(+1) above L(+1), and N2's reported ceiling is max(L, P) = "
              "P(+1), the one its certification used (E 0.625 below it: SPECIFIC)", len(camp7.records) == 6240
              and o7["N2"]["point"] == 1.0 and abs(o7["N2"]["match_ratio"] - 2.0 * camp7.dmap.d_eq) <= 1e-12
              and st7.P[1.0] > st7.L[1.0] and o7["N2"]["ceiling"] == st7.P[1.0] and o7["N2"]["state"] == "SPECIFIC",
              (len(camp7.records), o7["N2"]["point"], o7["N2"].get("ceiling"), o7["N2"]["state"]),
              cover=["RD-MERGED"])
        # F11: the asymmetric campaign; every statistic against a hand computation from the deltas as written
        asym = _bt_write_campaign(base / "asym", sm, delta=_bt_asym, told=_bt_asym_told, sham=_bt_asym_sham)
        camp11, st11, fig11, o11 = _bt_eval(asym, sm)
        lv = label_values(camp11.identity)
        vpts = sorted(set(lv.values()), reverse=True)                       # 0 included
        labs = {p: l for l, p in lv.items()}
        def y_of(arm, d_, run):
            return [0.0 if p == 0.0 else _bt_asym(arm, d_, labs[p], run) for p in vpts]
        hand_slope_v = float(np.mean([np.polyfit(vpts, y_of("N1-V", "valence", r), 1)[0] for r in range(160)]))
        dirs = [f"rand_{i:02d}" for i in range(N_RANDOM)]
        hand_floor = max(abs(float(np.mean([np.polyfit(vpts, y_of("N1-R", d_, r), 1)[0] for r in range(40)])))
                         for d_ in dirs)
        hand_L = {p: max(abs(float(np.mean([_bt_asym("N1-R", d_, labs[p], r) for r in range(40)]))) for d_ in dirs)
                  for p in vpts if p != 0.0}
        hand_P = {p: abs(float(np.mean([_bt_asym("N1-P", "valence", lab, r) for r in range(160)])))
                  for lab, p in (("+1", 1.0), ("-1", -1.0))}
        p_deq = camp11.dmap.d_eq
        hand_n2 = float(np.mean([np.polyfit([0.0, p_deq, 2.0 * p_deq],
                                            [0.0, _bt_asym("N2-E", "span_reward", "f0.10", r),
                                             _bt_asym("N2-E", "span_reward", "f0.20", r)], 1)[0] for r in range(160)]))
        tv = np.array([_bt_asym_told(r, "") for r in range(160)])
        tmeans = tv[boot_index("N4-T", 160)].mean(axis=1)
        hand_98 = (_bt_hand_pct(tmeans, 1.0), _bt_hand_pct(tmeans, 99.0))
        close = lambda a, b: abs(a - b) <= 1e-9                              # noqa: E731
        asym_ok = {
            "tuple": o11["tuple"] == ("REPLICATED", "DETECTABLE", "SPECIFIC", "INDETERMINATE", "PASS"),
            "slope_V (d = 0 in the fit)": close(st11.slope_V.mean, hand_slope_v),
            "floor (|slope|, rand_05 negative)": close(st11.floor_V, hand_floor) and fig11["floor_dir"] == _BT_RAND_NEG,
            "L (|mean|)": all(close(st11.L[p], hand_L[p]) for p in hand_L) and len(st11.L) == len(hand_L),
            "P (+1 and −1 apart, |mean|)": close(st11.P[1.0], hand_P[1.0]) and close(st11.P[-1.0], hand_P[-1.0])
            and fig11["P_signed"]["+1"]["mean"] < 0.0,
            "N1 ceiling max(L, P) = P(+1)": hand_P[1.0] > hand_L[1.0] and close(o11["N1"]["ceiling"], hand_P[1.0]),
            "dose ceiling L(d_eq) alone": close(o11["dose"]["ceiling"], hand_L[p_deq]),
            "E by f": close(st11.E[F10].mean, 1.045) and close(st11.E[F20].mean, 0.19),
            "N2's per-f n and SD (ddof 0)": fig11["n"][("N2-E", "f0.10")] == fig11["n"][("N2-E", "f0.20")] == 160
            and close(fig11["sd0"][("N2-E", "f0.10")],
                      float(np.std([_bt_asym("N2-E", "span_reward", "f0.10", r) for r in range(160)])))
            and close(fig11["sd0"][("N2-E", "f0.20")],
                      float(np.std([_bt_asym("N2-E", "span_reward", "f0.20", r) for r in range(160)])))
            and fig11["sd0"][("N2-E", "f0.20")] > 1.5 * fig11["sd0"][("N2-E", "f0.10")],
            "N2 slope (0, d_eq, 2 d_eq)": close(fig11["slopes_N2"]["N2-E"]["mean"], hand_n2),
            "E_sham |negative mean|": close(st11.e_sham, 0.3),
            "m_told 98%": close(st11.told.lo, hand_98[0]) and close(st11.told.hi, hand_98[1])
            and _bt_hand_pct(tmeans, 2.5) > 0.0 > hand_98[0] and st11.told.level == 98}
        B.chk("reader path (F11): an asymmetric campaign -- a random direction with a negative slope and offset, N1-P "
              "at −0.9 / +0.2, N2-E at 1.0 / 0.1 by f with spreads in the ratio 1:2, a negative sham mean, a session "
              "offset of mean +0.045 -- reads to the hand computation: the slope with its d = 0 point, the floor as "
              "max |mean slope|, L and P as |mean| at their own points, the ceilings, E by f, N2's per-f n and SD, "
              "N2's slope, E, and m_told's 98% CI (whose 95% would have excluded 0)", all(asym_ok.values()),
              [k for k, v in asym_ok.items() if not v] or o11["tuple"], cover=["RD-ASYM"])
        # F3: d_eq merged into +1/2 (R_ell 39.78: d_eq ≈ 0.52, d_20 at the cap) -- the dose sentence reads +1/2
        mdq = _bt_write_campaign(base / "mdq", sm, R_ell=39.78, delta=_bt_delta_positive)
        camp12, st12, fig12, o12 = _bt_eval(mdq, sm)
        s12 = sentence_set_filled(o12, st12, route="B", auc={"d_eq": 0.9})
        want12 = (f"at d_eq = {u4(camp12.dmap.d_eq)} (read at d = +1/2, the point it merges into under §2.3) — this "
                  f"program's f = 0.10 on BK's scale — the effect is {f4(st12.V[0.5].mean)} nats {ci4(st12.V[0.5])} "
                  f"above a leak ceiling of {u4(ceil_at(st12, 0.5))}: dose alone does not account for the program's "
                  "null on the echo channel")
        B.chk("reader path: d_eq ≈ 0.52 merged into +1/2 -> the dose question reads +1/2, and its sentence prints "
              "d_eq's value with the point read beside it", camp12.dmap.merged()["d_eq"] and o12["dose"]["point"] == 0.5
              and o12["dose"]["state"] == "DETECTABLE" and s12["7.2"]["text"] == want12, s12["7.2"]["text"][:120],
              cover=["RD-MERGED-DEQ"])
        paused = _bt_eval(pos, sm, paused={"N1-R": True, "N2-E": True})[3]
        B.chk("reader path: unadjudicated pauses on N1-R and N2-E -> N1 and dose INDETERMINATE (pause:N1-R), N2 "
              "INDETERMINATE (pause:N2-E), N4 PASS", paused["tuple"][:4] == ("INDETERMINATE",) * 3 + ("PASS",)
              and paused["N1"]["causes"] == ["pause:N1-R"] and paused["N2"]["causes"] == ["pause:N2-E"],
              paused["tuple"], cover=["RD-PAUSE"])
        gr = _bt_gread_all(camp.dmap, "FAIL")
        o8 = _bt_eval(null, sm, gread=gr)
        B.chk("reader path: G-READ-n FAIL everywhere -> the tuple's coordinate FAIL; the NOT-REPLICATED and NULL "
              "labels concluded, not answered", o8[3]["tuple"][4] == "FAIL"
              and sentence_set_filled(o8[3], o8[1], route="B", auc={"d_eq": None})["7.1"]["label"] == CNA,
              o8[3]["tuple"], cover=["RD-GREAD"])
        # F12: mixed G-READ-n states on a campaign where N4 PASSES and nothing else moves; each label and the tuple's
        # coordinate must read its own cell (valence at +1 for N1, at d_eq for dose and the coordinate, span_reward
        # at f = 0.20 for N2)
        null2 = _bt_write_campaign(base / "null2", sm, delta=lambda a, d, l, r: 0.01 * ((r % 3) - 1))
        camp13 = load_campaign(null2, sm)
        pts13 = camp13.dmap.resolved()
        mix = {}
        for name, fails in (("d_eq-fails", {("valence", pts13["d_eq"]), ("span_reward", F10)}),
                            ("+1-fails", {("valence", 1.0), ("span_reward", F20)})):
            g = {k: ("FAIL" if k in fails else "PASS") for k in _bt_gread_all(camp13.dmap)}
            st_m, _fg = build_state(camp13, paused={}, gread=g)
            o_m = outcomes(st_m)
            s_m = sentence_set_filled(o_m, st_m, route="B", auc={"d_eq": 0.81})
            mix[name] = (o_m["tuple"], s_m["7.1"]["label"], s_m["7.2"]["label"], s_m["7.2"]["form"],
                         s_m["7.3"]["label"], "AUC 0.810" in s_m["7.2"]["text"])
        want_mix = {"d_eq-fails": (("NOT-REPLICATED", "NOT-DETECTABLE", "NULL", "PASS", "FAIL"), ANSWERED, CNA,
                                   "§5, its ellipsis expanded by Code", ANSWERED, False),
                    "+1-fails": (("NOT-REPLICATED", "NOT-DETECTABLE", "NULL", "PASS", "PASS"), CNA, ANSWERED, "§5",
                                 CNA, True)}
        stop_auc = _bt_raises(lambda: sentence_set_filled(o_m, st_m, route="B", auc={"d_eq": None}), (AnlStop,))
        stop_route = _bt_raises(lambda: sentence_set_filled(o_m, st_m, route="C", auc={"d_eq": 0.81}), (AnlStop,))
        B.chk("reader path (F12): G-READ-n FAIL at d_eq only -> the coordinate FAIL, N1's label answered, the dose "
              "sentence not readable; FAIL at +1 only -> the coordinate PASS, N1's label concluded, the dose sentence "
              "answered with its AUC; N2's label follows span_reward at f = 0.20; a readable dose sentence without an "
              "AUC, and a route other than A or B, STOP", mix == want_mix and stop_auc[0] and stop_route[0],
              (mix, stop_auc[1][:50], stop_route[1][:50]), cover=["RD-GREAD-MIXED"])
        # F14: at +1 a fresh shift of 0.02 (rel ≈ 0.009: above TAU/4, below TAU) on runs 0, 4, ...; at −1 a shift of
        # 0.5 (above both) on runs 1, 5, ...; the shadow of run 2 shifted by 0.01 (rel ≈ 0.009: its session drops at
        # every point and in every arm), the shadow of run 3 by 1e-9 (above the identity bound 0, far below TAU/4);
        # N2-S at f = 0.10 with five label masses of exactly .20 and three just below
        shifted = {f"N1-V|valence|+1|{session_key(r)}": 0.02 for r in range(0, 160, 4)}
        shifted |= {f"N1-V|valence|-1|{session_key(r)}": 0.5 for r in range(1, 160, 4)}
        shifted[f"N1-V|none|0|{session_key(2)}"] = 0.01
        shifted[f"N1-V|none|0|{session_key(3)}"] = 1e-9
        def masses(cell):
            if cell["arm"] == "N2-S" and cell["dose_label"] == "f0.10":
                for i in range(8):
                    cell["records"][i]["restricted"]["label_mass"] = 0.20 if i < 5 else 0.19999999999999998
        sens = _bt_write_campaign(base / "sens", sm, delta=_bt_delta_positive, fresh_shift=shifted, mutate=masses)
        camp9 = load_campaign(sens, sm)
        st_p, fig_p = build_state(camp9, paused={}, gread=_bt_gread_all(camp9.dmap))
        st_s, fig_s = build_state(camp9, paused={}, gread=_bt_gread_all(camp9.dmap), drop=tau4_drop(camp9))
        cn = counters(camp9)
        sens_ok = {
            "primary keeps all": fig_p["n"][("N1-V", "+1")] == 160 and fig_p["n"][("N1-V", "-1")] == 160
            and fig_p["slope_V_n"] == 160,
            "TAU/4 row drops 40 + 40 + run 2": fig_s["n"][("N1-V", "+1")] == 119 and fig_s["n"][("N1-V", "-1")] == 119
            and fig_s["slope_V_n"] == 79 and fig_s["n"][("N1-V", "+1/2")] == 159
            and fig_s["n"][("N2-E", "f0.10")] == 159 and fig_s["n"][("N1-P", "+1")] == 159,
            "TAU/4-only at +1": cn["N1-V|+1"]["fidelity exceedances at TAU/4"] == 40
            and cn["N1-V|+1"]["fidelity exceedances at TAU"] == 0,
            "both at −1": cn["N1-V|-1"]["fidelity exceedances at TAU/4"] == 40
            and cn["N1-V|-1"]["fidelity exceedances at TAU"] == 40,
            "shadows": cn["N1-V|0"]["fidelity exceedances at TAU/4"] == 1
            and cn["N1-V|0"]["fidelity exceedances at TAU"] == 0,
            "identity bound": cn["N1-V|0"]["identity bound exceeded"] == 2
            and sum(c["identity bound exceeded"] for c in cn.values()) == 2,
            "label mass below .20 (strict)": cn["N2-S|f0.10"]["label mass below .20"] == 3
            and sum(c["label mass below .20"] for c in cn.values()) == 3}
        B.chk("reader path (F14): the TAU/4 row (PIN-n-16) drops the 40 reads above TAU/4 at +1 (none above TAU), the "
              "40 above both at −1, and run 2 everywhere (its shadow above TAU/4), from those points and the slopes "
              "(79 sessions left), the primary keeping all 160; the counters, through `counters`, tell TAU/4 from "
              "TAU, count two identity-bound exceedances and the three label masses strictly below .20",
              all(sens_ok.values()), [k for k, v in sens_ok.items() if not v],
              cover=["RD-SENSITIVITY", "CNT-COUNTERS"])
        sec = secondaries(camp, st, {"cosines": {"span_character|span_reward": 0.1, "span_character|span_sentiment": 0.2,
                                                 "span_character|valence": 0.3, "span_reward|span_sentiment": 0.4,
                                                 "span_reward|valence": 0.5, "span_sentiment|valence": 0.6}})
        B.chk("reader path: the secondaries compute -- (a) first-pick shares per arm and dose, (c) groups count-only "
              "below 20, (d) r over 160 sessions, (e) six cosines and the matched means -- and (b) reads 'not recorded'",
              sec["d_retention_r"]["n"] == 160 and len(sec["e_directions"]["cosines"]) == 6
              and sec["b_free_text"].startswith("not recorded") and all(
                  ("mean" in g) == (g["n"] >= FLOOR_EVENTS) for gs in sec["c_groups"].values() for g in gs.values()),
              sec["d_retention_r"], cover=["RD-SECONDARY"])
        # M38: secondary (c)'s floor at exactly 20 events (S first in runs 0-19), and at 19 (one of them non-finite)
        s20 = _bt_write_campaign(base / "s20", sm, delta=_bt_delta_positive, first_is_s=lambda r: r < 20,
                                 nonfinite=[f"N2-C|span_character|f0.20|{session_key(5)}"])
        camp14 = load_campaign(s20, sm)
        st14, _f14 = build_state(camp14, paused={}, gread=_bt_gread_all(camp14.dmap))
        cg = secondaries(camp14, st14, None)["c_groups"]
        g20, g19 = cg["N2-E|f0.20"]["present_first_is_S=True"], cg["N2-C|f0.20"]["present_first_is_S=True"]
        B.chk("reader path: secondary (c) reports a group's mean at exactly 20 events (the decidable-n floor, rule "
              "28(a)) and withholds it at 19", g20["n"] == 20 and abs(g20.get("mean", 9.0) - 0.625) <= 1e-9
              and g19 == {"n": 19}, (g20, g19), cover=["RD-SECONDARY-FLOOR"])
        # refusals
        refs = {}
        stray = _bt_write_campaign(base / "stray", sm, delta=_bt_delta_positive)
        (stray / "notes.txt").write_text("x", encoding="utf-8")
        refs["stray"] = _bt_raises(lambda: load_campaign(stray, sm), (AnlRefusal,))
        def pod(cell):
            if cell["arm"] == "N2-C":
                cell["stage_identity"] = dict(cell["stage_identity"], pod_id="another-pod")
        refs["identity"] = _bt_raises(lambda: load_campaign(_bt_write_campaign(base / "id", sm, delta=_bt_delta_positive,
                                                                                mutate=pod), sm), (AnlRefusal,))
        def ids(cell):
            if cell["arm"] == "N2-S" and cell["dose_label"] == "f0.10":
                cell["records"][3]["ids_sha"] = cell["records"][3]["ids_sha_bk"] = "f" * 16
        refs["shadow"] = _bt_raises(lambda: load_campaign(_bt_write_campaign(base / "sh", sm, delta=_bt_delta_positive,
                                                                              mutate=ids), sm), (AnlRefusal,))
        def zone(cell):
            if cell["arm"] == "N4-Ts":
                r = cell["records"][1]
                r["schedule_zone"] = "S"
        refs["zones"] = _bt_raises(lambda: load_campaign(_bt_write_campaign(base / "z", sm, delta=_bt_delta_positive,
                                                                             mutate=zone), sm), (AnlRefusal,))
        def bad(cell):
            if cell["arm"] == "N1-P":
                cell["records"][0]["margin"] = 9.0
        refs["schema"] = _bt_raises(lambda: load_campaign(_bt_write_campaign(base / "bad", sm, delta=_bt_delta_positive,
                                                                              mutate=bad), sm), (AnlRefusal,))
        def cues(cell):
            # one N4-Ts read of run 2 with its cues swapped (the schema's own checks still pass: N4-Ts has no spans
            # and its sham line names no zone), so the session's cues differ between its reads
            if cell["arm"] == "N4-Ts":
                r = cell["records"][2]
                r["cue_S"], r["cue_U"] = r["cue_U"], r["cue_S"]
                r["present_first_is_S"] = r["present"][0] == r["cue_S"]
        refs["cues"] = _bt_raises(lambda: load_campaign(_bt_write_campaign(base / "cu", sm, delta=_bt_delta_positive,
                                                                            mutate=cues), sm), (AnlRefusal,))
        def unbalanced(cell):
            # run 1 (zone U) moved to S on both N4 arms alike, the told line following it: 81 S and 79 U
            if cell["arm"] in N4_ARMS:
                r = cell["records"][1]
                r["schedule_zone"] = "S"
                if cell["arm"] == "N4-T":
                    r["told_line"] = sm.TOLD_LINE.format(zone=r["cue_S"])
        refs["balance"] = _bt_raises(lambda: load_campaign(_bt_write_campaign(base / "ub", sm,
                                                                               delta=_bt_delta_positive,
                                                                               mutate=unbalanced), sm), (AnlRefusal,))
        capx = _bt_write_campaign(base / "capx", sm, delta=_bt_delta_positive)
        (capx / sm.cell_filename("N2-S", "span_sentiment", "f0.20").replace(".json", ".npy")).write_bytes(b"x")
        refs["capture"] = _bt_raises(lambda: load_campaign(capx, sm), (AnlRefusal,))
        capa = _bt_write_campaign(base / "capa", sm, delta=_bt_delta_positive)
        (capa / sm.cell_filename("N1-P", "valence", "-1").replace(".json", ".npy")).unlink()
        refs["capture-absent"] = _bt_raises(lambda: load_campaign(capa, sm), (AnlRefusal,))
        refs["shadow-absent"] = _bt_raises(lambda: load_campaign(_bt_write_campaign(base / "sa", sm,
                                                                                     delta=_bt_delta_positive,
                                                                                     omit=[("N1-V", "none", "0")]), sm),
                                           (AnlRefusal,))
        want = {"stray": "beside the cells", "identity": "stage identity differs", "shadow": "shadow",
                "zones": "schedule zones", "schema": "margin", "cues": "cues or present order differ",
                "balance": "80 S and 80 U", "capture": "capture_sha256", "capture-absent": "is absent",
                "shadow-absent": "is not on disk"}
        B.chk("reader path refuses: a file no cell names; a stage identity that differs between cells; a read whose "
              "ids_sha differs from its shadow's; N4-T and N4-Ts zones that differ; a record the schema's check_cell "
              "refuses; a session whose cues differ between reads; a schedule of 81 S and 79 U on both N4 arms; a "
              "capture array whose bytes are not its recorded sha256, or absent; steered reads whose shadows are not on "
              "disk",
              all(refs[k][0] and want[k] in refs[k][1] for k in want),
              {k: (v[0], v[1][:80]) for k, v in refs.items()}, cover=["RD-REFUSE"])


# =====================================================================================================================
# 14. Outputs: write-once, the not-run command, G-ANL-n's artifact
# =====================================================================================================================
GANL_REL = "data/n/gates/G-ANL-n.json"
GANL_SCHEMA = "n-ganl-v1"
VERDICTS_REL = "data/n/verdicts"
NOT_RUN_OUT_SCHEMA = "n-not-run-out-v1"


def json_text(obj: Any) -> str:
    return json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False) + "\n"


def write_once(path: Path, text: str) -> str:
    """Write-once: 'written' if new, 'identical' if the same bytes are there, else refused (exit 2). The new file is
    linked into place from a private temporary file (os.link fails if the name exists), so two writers cannot both
    write, and a reader never sees a partial file."""
    import os
    data = text.encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    tmp.write_bytes(data)
    try:
        os.link(tmp, path)
        how = "written"
    except FileExistsError:
        how = "identical" if path.read_bytes() == data else ""
    finally:
        tmp.unlink()
    if not how:
        raise AnlRefusal(f"REFUSED: {path.name} exists with other bytes (write-once)")
    return how


def analyzer_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def run_not_run(record: Path, out_dir: Path) -> tuple[Path, str]:
    """`not-run`: N-pod's NOT-RUN output from a NOT-RUN record (n §5 "Unit outcome first"), with its sentence set."""
    try:
        rec = json.loads(Path(record).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise AnlRefusal(f"REFUSED: the NOT-RUN record: {type(e).__name__}")
    reason = not_run_reason(rec)
    sset = {k: dict(v, text=v["text"].replace("[reason]", reason)) for k, v in sentence_set(NOT_RUN).items()}
    doc = {"schema": NOT_RUN_OUT_SCHEMA, "unit": UNIT, "outcome": NOT_RUN, "cause": rec["cause"], "reason": reason,
           "record": {"name": Path(record).name, "sha256": hashlib.sha256(Path(record).read_bytes()).hexdigest()},
           "date": rec["date"], "sentences": sset,
           "proposal_sha256": PROPOSAL_SHA256, "analyzer_sha256": analyzer_sha256(), "pins": PINS, "open": OPEN}
    path = Path(out_dir) / f"{UNIT}_NOT-RUN.json"
    return path, write_once(path, json_text(doc))


def battery() -> dict:
    B = _Battery()
    snap0 = _bt_snapshot()
    with _Hook() as hook:
        ptext = (REPO / PROPOSAL_REL).read_bytes()
        verb = proposal_spans(ptext.decode("utf-8"))
        B.group("outcomes", lambda: _bt_outcomes(B))
        B.group("not-run", lambda: _bt_notrun(B))
        B.group("tables", lambda: _bt_tables(B))
        B.group("sentences", lambda: _bt_sentences(B, verb))
        B.group("tuples", lambda: _bt_tuples(B, verb))
        B.group("reachability", lambda: _bt_reachability(B))
        B.group("numerics", lambda: _bt_numerics(B))
        B.group("reader path", lambda: _bt_reader(B))
        B.group("commands", lambda: _bt_commands(B))
        B.group("structure", lambda: _bt_structure(B, ptext, hook))
    snap1 = _bt_snapshot()
    B.chk("the battery wrote nothing under data/n (sha256 of every file outside ckpt / reports / verdicts, before = "
          "after)", snap0 == snap1, sorted(set(snap0) ^ set(snap1))[:2], cover=["STR-NO-CANONICAL-WRITE"])
    unreached = sorted(REQUIRED_COVERAGE - B.reached)
    B.chk(f"coverage: every one of the {len(REQUIRED_COVERAGE)} required ids reached", unreached == [], unreached[:6])
    n = len(B.results) + 1
    B.chk(f"check count {n} == EXPECTED_CHECKS {EXPECTED_CHECKS} (a skipped assertion is a failure)",
          n == EXPECTED_CHECKS, n)
    n_ok = sum(B.results)
    print(f"  {n_ok}/{n} n_analyze battery checks pass", flush=True)
    return {"checks_pass": n_ok, "checks_total": n, "expected_checks": EXPECTED_CHECKS,
            "ok": n_ok == n and n == EXPECTED_CHECKS and not unreached, "coverage_ids": sorted(B.reached),
            **B.extra}


# =====================================================================================================================
# 15. G-ANL-n's run (n §3 "G-ANL-n"): the battery, then the artifact, write-once, against committed blobs
# =====================================================================================================================
BOUND_RELS = (PROPOSAL_REL, SCHEMA_REL, f"{BK_NP_REL}/prereg.json", f"{BK_NP_REL}/reduced.json")


def committed_problems(rels: Sequence[str]) -> list[str]:
    """Each path committed at HEAD with identical working-tree bytes: `git status --porcelain` empty and the
    working tree's blob id equal to HEAD's (ids only; nothing under a ckpt or reports directory is among them)."""
    import subprocess
    probs = []
    for rel in rels:
        def git(*args: str) -> str:
            return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True).stdout.strip()
        if git("status", "--porcelain", "--", rel):
            probs.append(f"{rel}: not committed as it stands")
            continue
        head = git("rev-parse", f"HEAD:{rel}")
        if not head or git("hash-object", "--", rel) != head:
            probs.append(f"{rel}: the working tree's bytes are not HEAD's")
    return probs


def pinned_map_reach(dmap: DoseMap) -> dict:
    """The (N1, dose, N2) triples the outcome layer produces on the pinned map (the battery's enumeration), its merge
    shape, and, where the shape is one the battery derives by hand, the agreement with that derivation."""
    r = dmap.resolved()
    # the coupling classes: N2 reads N1-V at +1 when d_20 sits there (b); dose reads +1 too when d_eq does (d)
    shape = "d" if r["d_eq"] == 1.0 else "b" if r["d_20"] == 1.0 else "a"
    seen, iff, clean = map_reach(dmap)
    return {"shape": shape, "triples": len(seen), "tuples": len(seen) * 8 + 1, "dose_iff_n1": iff, "raised": not clean,
            "agrees_with_hand": seen == map_reach_by_hand(shape)}


def ganl_artifact(res: Mapping[str, Any], dmap: DoseMap | None) -> dict:
    sha = analyzer_sha256()
    return {"schema": GANL_SCHEMA, "stage": "G-ANL-n", "verdict": "PASS",
            "spec": "PROPOSAL-n v0.2 §3 G-ANL-n, §8 step 9; the seat's answers of 2026-11-15 §5.1",
            "analyzer": {"path": ANALYZER_REL, "sha256": sha, "sha16": sha[:16]},
            "proposal": {"path": PROPOSAL_REL, "sha256": PROPOSAL_SHA256},
            "schema_module": {"path": SCHEMA_REL, "sha256": SCHEMA_SHA256},
            "battery": {k: res.get(k) for k in ("checks_pass", "checks_total", "expected_checks", "coverage_ids",
                                                 "outputs_sha256", "reachability", "bk_repro", "bk_fidelity")},
            "tuple_space": {"tuples": 385, "evaluations": 1921},
            "dose_map": None if dmap is None else {"d_eq": dmap.d_eq, "d_20": dmap.d_20, "points": dmap.expected_points(),
                                                   "reach": pinned_map_reach(dmap)},
            "pins": PINS, "open": OPEN}


DOSE_MAP_KEYS = ("d_eq", "d_20", "rho", "R", "R_ell")


def dose_map_input_problems(m: Any) -> list[str]:
    """`ganl --dose-map` takes exactly G-CAL-n's five figures, {d_eq, d_20, rho, R, R_ell}, each a finite JSON float
    (never null, a string, an integer or a bool), so that §2.3's formulas are always checked (DoseMap.problems)."""
    if not isinstance(m, dict):
        return ["the dose map is not a JSON object"]
    p = [] if set(m) == set(DOSE_MAP_KEYS) else [f"its keys {sorted(m)} are not {sorted(DOSE_MAP_KEYS)}"]
    for k in DOSE_MAP_KEYS:
        v = m.get(k)
        if not (isinstance(v, float) and math.isfinite(v)):
            p.append(f"{k} {v!r} is not a finite float")
    return p


@dataclass(frozen=True)
class GanlPlan:
    code: int                  # 0 = proceed; 2 = refused before any battery run
    refusal: str | None        # which refusal fired (the battery tests each by name)
    message: str
    canonical: bool
    dest: Path | None
    dmap: DoseMap | None


def ganl_precheck(out: str | None, dose_map: str | None,
                  bound: Sequence[str] | None = None) -> GanlPlan:
    """Every refusal `ganl` makes before its battery runs, in order, by name: 'canonical-uncommitted',
    'canonical-no-map', 'out-inside-repo', 'map-unreadable', 'map-input', 'map-formula'. `bound` (default: the
    analyzer and BOUND_RELS) is the battery's handle on the committed-blob check; nothing here runs the battery."""
    canonical = out is None
    rels = (ANALYZER_REL,) + BOUND_RELS if bound is None else tuple(bound)
    def no(refusal: str, msg: str) -> GanlPlan:
        return GanlPlan(2, refusal, "REFUSED: " + msg, canonical, None, None)
    if canonical:
        probs = committed_problems(rels)
        if probs:
            return no("canonical-uncommitted", f"G-ANL-n's artifact is written against committed blobs only: "
                                               f"{probs[:4]}")
        if dose_map is None:
            return no("canonical-no-map", "the canonical G-ANL-n run binds the pinned dose map (--dose-map; "
                                          "G-CAL-n's figures)")
        dest = REPO / GANL_REL
    else:
        d = Path(out).expanduser().resolve()
        root = REPO.resolve()
        if d == root or root in d.parents:
            return no("out-inside-repo", "a --out directory inside the repository")
        dest = d / Path(GANL_REL).name
    dmap = None
    if dose_map is not None:
        try:
            m = json.loads(Path(dose_map).read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            return no("map-unreadable", f"the dose map: {type(e).__name__}")
        bad = dose_map_input_problems(m)
        if bad:
            return no("map-input", f"the dose map: {bad}")
        dmap = DoseMap(m["d_eq"], m["d_20"], m["rho"], m["R"], m["R_ell"])
        if dmap.problems():
            return no("map-formula", f"the dose map: {dmap.problems()}")
    return GanlPlan(0, None, "", canonical, dest, dmap)


def run_ganl(out: str | None, dose_map: str | None) -> int:
    """`ganl`: the battery, then data/n/gates/G-ANL-n.json, write-once, its bound files committed (canonical); a
    --out test directory outside the repository is never of record. The pinned dose map (G-CAL-n's figures, as
    {d_eq, d_20, rho, R, R_ell}) is required canonically and optional with --out."""
    plan = ganl_precheck(out, dose_map)
    if plan.code:
        print(plan.message, file=sys.stderr)
        return plan.code
    canonical, dest, dmap = plan.canonical, plan.dest, plan.dmap
    assert dest is not None
    sha0 = analyzer_sha256()
    res = battery()
    if not res["ok"]:
        print("STOP: G-ANL-n's battery did not pass; nothing written", file=sys.stderr)
        return 4
    if analyzer_sha256() != sha0 or (canonical and committed_problems((ANALYZER_REL,) + BOUND_RELS)):
        print("STOP: the code moved during the battery; nothing written", file=sys.stderr)
        return 4
    art = ganl_artifact(res, dmap)
    if dmap is not None and (art["dose_map"]["reach"]["raised"] or not art["dose_map"]["reach"]["dose_iff_n1"]
                             or not art["dose_map"]["reach"]["agrees_with_hand"]):
        print("STOP: the pinned map's reachability check failed; nothing written", file=sys.stderr)
        return 4
    try:
        how = write_once(dest, json_text(art))
    except AnlRefusal as e:
        print(str(e), file=sys.stderr)
        return 2
    print(f"G-ANL-n: PASS: {GANL_REL if canonical else dest.name} ({how}; sha256 "
          f"{hashlib.sha256(dest.read_bytes()).hexdigest()})" + ("" if canonical else " -- an --out run, never of record"))
    return 0


def _bt_commands(B: _Battery) -> None:
    """The schema's merge rule against the analyzer's own over a grid of maps; the pinned map's coupling classes; the
    not-run command's write-once output; ganl's refusals before any battery run."""
    import tempfile
    sm = schema_module()
    agree, n_ok, n_ref = True, 0, 0
    for i in range(1, 401):
        d_eq = i * 0.003                                  # 0.003 .. 1.2
        d_20 = min(1.0, 2.0 * d_eq)
        mine = DoseMap(d_eq, d_20)
        try:
            theirs = sm.dose_points(d_eq, d_20)
        except sm.SchemaError:
            theirs = None
        if theirs is None:
            n_ref += 1
            agree &= any("folds into d = 0" in p for p in mine.problems())
        else:
            n_ok += 1
            agree &= not mine.problems() and mine.expected_points() == theirs
    B.chk(f"the merge rule (PIN-n-14) agrees with the schema's dose_points on 400 maps (d_eq 0.003 to 1.2): "
          f"{n_ok} derived alike, {n_ref} refused alike (a fold into 0)", agree and n_ok + n_ref == 400 and n_ref > 0,
          (n_ok, n_ref), cover=["NUM-DOSEMAP-SCHEMA"])
    # The merge rule's edges at a decimal distance of exactly 0.05, where IEEE doubles decide (PIN-n-14): 0.5 − 0.45
    # is 0.04999… (folds), 0.55 − 0.5 is 0.05000…04 (kept), and 0.05 sits exactly 0.05 from both 0 and a kept
    # d_20 = 0.1, a tie that goes to the earlier candidate, 0 (refused). Each against the schema's dose_points too.
    edge_want = {(0.45, 0.9): ({"d_20": 0.9, "d_eq": 0.5}, ["d_20"]),
                 (0.55, 1.0): ({"d_20": 1.0, "d_eq": 0.55}, ["d_eq"]),
                 (0.225, 0.45): ({"d_20": 0.5, "d_eq": 0.225}, ["d_eq"]),
                 (0.275, 0.55): ({"d_20": 0.55, "d_eq": 0.275}, ["d_20", "d_eq"]),
                 (0.05, 0.1): None}
    edge_got, edge_ok = {}, True
    for (de, d2), want in edge_want.items():
        mine = DoseMap(de, d2)
        try:
            theirs = sm.dose_points(de, d2)
        except sm.SchemaError:
            theirs = None
        r, kept = mine._resolve()
        edge_got[(de, d2)] = (None if mine.problems() else ({k: r[k] for k in ("d_20", "d_eq")}, kept),
                              theirs is not None)
        if want is None:
            edge_ok &= (theirs is None and any("d_eq folds into d = 0" in p for p in mine.problems())
                        and r["d_eq"] == 0.0 and kept == ["d_20"])
        else:
            edge_ok &= (not mine.problems() and ({k: r[k] for k in ("d_20", "d_eq")}, kept) == want
                        and theirs == mine.expected_points())
    B.chk("the merge rule at a decimal distance of exactly 0.05 (IEEE decides): 0.45 folds into +1/2 (as d_eq and as "
          "d_20), 0.55 is kept (as d_eq and as d_20), and d_eq = 0.05 beside a kept d_20 = 0.1 ties between 0 and "
          "0.1, goes to 0 and is refused; the schema's dose_points agrees on all five", edge_ok, edge_got,
          cover=["NUM-MERGE-EDGE"])
    cls = {k: pinned_map_reach(m) for k, m in (("a", DoseMap(0.25, 0.5)), ("b", DoseMap(0.52, 1.0)),
                                               ("d", DoseMap(0.97, 1.0)))}
    B.chk("the pinned map's coupling class: d_20 at +1/2 is (a) (28 triples), d_eq at +1/2 with d_20 at +1 is (b) "
          "(24), both at +1 is (d) (17), each agreeing with the hand derivation", {k: (v["shape"], v["triples"],
                                                                                     v["agrees_with_hand"])
                                                                                for k, v in cls.items()}
          == {"a": ("a", 28, True), "b": ("b", 24, True), "d": ("d", 17, True)}, cls, cover=["NUM-REACH-CLASS"])
    with tempfile.TemporaryDirectory(prefix="n_anl_cmd_") as td:
        base = Path(td)
        rec = {"schema": NOT_RUN_RECORD_SCHEMA, "unit": UNIT, "cause": "clock:pi-declined", "date": "2026-12-16",
               "detail": "a synthetic record"}
        rp = base / "rec.json"
        rp.write_text(json.dumps(rec), encoding="utf-8")
        p1, h1 = run_not_run(rp, base / "out")
        p2, h2 = run_not_run(rp, base / "out")
        doc = json.loads(p1.read_text(encoding="utf-8"))
        rp.write_text(json.dumps(dict(rec, cause="clock:no-box")), encoding="utf-8")
        ok3, msg3 = _bt_raises(lambda: run_not_run(rp, base / "out"), (AnlRefusal,))
        B.chk("not-run writes N-pod_NOT-RUN.json once (written, then identical), refuses other bytes (write-once), and "
              "carries the reason in all four sentence slots", (h1, h2) == ("written", "identical") and ok3
              and doc["outcome"] == NOT_RUN and all(doc["reason"] in v["text"] for v in doc["sentences"].values())
              and doc["date"] == "2026-12-16", (h1, h2, msg3[:60]), cover=["CMD-NOTRUN"])
        nr = {"uncommitted": not_run_precheck(None, bound=("scripts/__n_analyze_never_committed__.py",)),
              "of-record": not_run_precheck(None, bound=()),
              "repo-root": not_run_precheck(str(REPO)), "repo-sub": not_run_precheck(str(REPO / "data")),
              "outside": not_run_precheck(str(base / "nr_out"))}
        B.chk("not-run's refusals before any write: the output of record only from the committed analyzer; a --out at "
              "the repository root or inside it; with nothing left to check it names data/n/verdicts, and a --out "
              "outside the repository proceeds", nr["uncommitted"][0] == 2
              and "committed analyzer" in nr["uncommitted"][1] and nr["of-record"] == (0, "", REPO / VERDICTS_REL)
              and nr["repo-root"][0] == 2 and nr["repo-sub"][0] == 2
              and nr["outside"] == (0, "", (base / "nr_out").resolve()), {k: v[:2] for k, v in nr.items()},
              cover=["CMD-NOTRUN-REFUSE"])
        # ganl's refusals, each by name, through the precheck (never run_ganl: a moved refusal must not recurse into
        # the battery). The maps' figures are §2.3-consistent by construction except where a case breaks one.
        def mfile(name: str, obj: Any, raw: str | None = None) -> str:
            p = base / f"map_{name}.json"
            p.write_text(raw if raw is not None else json.dumps(obj), encoding="utf-8")
            return str(p)
        R0, Rl0 = 25.5, 23.90625
        de0 = (0.10 * Rl0) / (RHO * 25.5)
        good = {"d_eq": de0, "d_20": min(1.0, 2.0 * de0), "rho": RHO, "R": R0, "R_ell": Rl0}
        de1 = (0.10 * 0.03) / (RHO * 1.0)                 # ≈ 0.01: d_20 ≈ 0.02 folds into 0
        fold0 = {"d_eq": de1, "d_20": min(1.0, 2.0 * de1), "rho": RHO, "R": 1.0, "R_ell": 0.03}
        outd = str(base / "ganl_out")
        cases = {
            "uncommitted": (lambda: ganl_precheck(None, None, bound=("scripts/__n_analyze_never_committed__.py",)),
                            "canonical-uncommitted", None),
            "no-map": (lambda: ganl_precheck(None, None, bound=()), "canonical-no-map", None),
            "repo-root": (lambda: ganl_precheck(str(REPO), None), "out-inside-repo", None),
            "repo-sub": (lambda: ganl_precheck(str(REPO / "data" / "n"), None), "out-inside-repo", None),
            "missing": (lambda: ganl_precheck(outd, str(base / "absent.json")), "map-unreadable", None),
            "not-json": (lambda: ganl_precheck(outd, mfile("nj", None, raw="{d_eq: 0.3")), "map-unreadable", None),
            "three-keys": (lambda: ganl_precheck(outd, mfile("k3", {k: good[k] for k in ("d_eq", "d_20")})),
                           "map-input", "R_ell None"),
            "null-rho": (lambda: ganl_precheck(outd, mfile("nr", dict(good, rho=None))), "map-input", "rho None"),
            "str-d_eq": (lambda: ganl_precheck(outd, mfile("sd", dict(good, d_eq=str(de0)))), "map-input", "d_eq '"),
            "int-R": (lambda: ganl_precheck(outd, mfile("iR", dict(good, R=25))), "map-input", "R 25 "),
            "bool-R_ell": (lambda: ganl_precheck(outd, mfile("bR", dict(good, R_ell=True))), "map-input", "R_ell True"),
            "nan-d_20": (lambda: ganl_precheck(outd, mfile("nan", dict(good, d_20=float("nan")))), "map-input",
                         "d_20 nan"),
            "extra-key": (lambda: ganl_precheck(outd, mfile("ex", dict(good, note=1.0))), "map-input", "keys"),
            "not-object": (lambda: ganl_precheck(outd, mfile("li", [de0])), "map-input", "not a JSON object"),
            "d_20-wrong": (lambda: ganl_precheck(outd, mfile("dw", dict(good, d_20=good["d_20"] + 0.01))),
                           "map-formula", "d_20"),
            "rho-wrong": (lambda: ganl_precheck(outd, mfile("rw", dict(good, rho=0.31))), "map-formula", "rho 0.31"),
            "d_eq-formula": (lambda: ganl_precheck(outd, mfile("df", dict(good, R=26.0))), "map-formula",
                             "(0.10 * R_ell) / (rho * R)"),
            "fold-into-0": (lambda: ganl_precheck(outd, mfile("f0", fold0)), "map-formula", "d_20 folds into d = 0"),
        }
        got = {k: f() for k, (f, _r, _m) in cases.items()}
        ok_ref = all(got[k].code == 2 and got[k].refusal == r and got[k].dest is None
                     and (m is None or m in got[k].message) for k, (_f, r, m) in cases.items())
        passed = ganl_precheck(outd, mfile("good", good))
        ok_pass = (passed.code == 0 and passed.refusal is None and not passed.canonical
                   and passed.dest == Path(outd).resolve() / "G-ANL-n.json"
                   and passed.dmap == DoseMap(good["d_eq"], good["d_20"], RHO, R0, Rl0))
        B.chk(f"ganl's {len(cases)} refusals before any battery run, each by name (a canonical run whose bound files "
              "are not committed, or with no pinned map; --out at the repository root or inside it; a map unreadable, "
              "not exactly five finite floats, or off §2.3's formulas, a fold into 0 included), and a consistent map "
              "outside the repository proceeds", ok_ref and ok_pass,
              {k: (v.refusal, v.message[:50]) for k, v in got.items() if v.refusal != cases[k][1]}
              or (passed.code, passed.refusal), cover=["CMD-GANL-REFUSE"])
        art = ganl_artifact({"checks_pass": 1, "checks_total": 1, "expected_checks": 1, "coverage_ids": [],
                             "outputs_sha256": "0" * 64}, DoseMap(0.97, 1.0))
        B.chk("G-ANL-n's artifact names the analyzer, proposal and schema by sha256, the tuple space (385; 1,921 "
              "evaluations), the pinned map's points and reach, the PIN and OPEN registers, and no time",
              art["proposal"]["sha256"] == PROPOSAL_SHA256 and art["schema_module"]["sha256"] == SCHEMA_SHA256
              and art["tuple_space"] == {"tuples": 385, "evaluations": 1921} and art["dose_map"]["reach"]["shape"] == "d"
              and art["pins"] == PINS and art["open"] == OPEN and not any(k in json.dumps(art) for k in ("UTC", "T00:")),
              sorted(art), cover=["STR-GANL-ARTIFACT"])


def not_run_precheck(out: str | None, bound: Sequence[str] | None = None) -> tuple[int, str, Path | None]:
    """`not-run`'s refusals before any write: the output of record (no --out, data/n/verdicts) only from the
    committed analyzer (`bound`, default the analyzer itself: the battery's handle); a --out only outside the
    repository. Returns (code, message, output directory)."""
    if out is None:
        probs = committed_problems((ANALYZER_REL,) if bound is None else tuple(bound))
        if probs:
            return 2, f"REFUSED: N-pod's NOT-RUN output of record is written by the committed analyzer only: {probs}", \
                None
        return 0, "", REPO / VERDICTS_REL
    d = Path(out).expanduser().resolve()
    if d == REPO.resolve() or REPO.resolve() in d.parents:
        return 2, f"REFUSED: a --out directory inside the repository (the output of record goes to {VERDICTS_REL}, " \
                  "with no --out)", None
    return 0, "", d


def main(argv: Sequence[str] | None = None) -> int:
    shown = sys.argv if argv is None else [sys.argv[0]] + list(argv)
    print("INVOCATION: " + " ".join([sys.executable] + shown), flush=True)
    ap = argparse.ArgumentParser(description="PROPOSAL-n's analyzer (G-ANL-n; N-pod's VERDICTS and NOT-RUN)")
    ap.add_argument("--selftest", action="store_true", help="the battery (model-free), no artifact")
    sub = ap.add_subparsers(dest="cmd")
    g = sub.add_parser("ganl", help="the battery, then data/n/gates/G-ANL-n.json (write-once)")
    g.add_argument("--out", default=None, help="a test directory outside the repository (never of record)")
    g.add_argument("--dose-map", default=None, help="the pinned dose map {d_eq, d_20, rho, R, R_ell}")
    n = sub.add_parser("not-run", help="N-pod's NOT-RUN output from a NOT-RUN record")
    n.add_argument("--record", required=True)
    n.add_argument("--out", default=None, help="a test directory outside the repository (never of record); "
                                               "without it, data/n/verdicts")
    a = ap.parse_args(argv)
    if a.selftest:
        return 0 if battery()["ok"] else 1
    if a.cmd == "ganl":
        return run_ganl(a.out, a.dose_map)
    if a.cmd == "not-run":
        code, msg, out_dir = not_run_precheck(a.out)
        if code:
            print(msg, file=sys.stderr)
            return code
        try:
            path, how = run_not_run(Path(a.record), out_dir)
        except AnlRefusal as e:
            print(str(e), file=sys.stderr)
            return 2
        print(f"NOT-RUN: {path.name} ({how})", flush=True)
        return 0
    ap.print_usage(sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
