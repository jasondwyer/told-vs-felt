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

Code's readings are registered in PINS (PIN-n-7 to PIN-n-36 ruled by the seat: PIN-n-29 and -32 amended and PIN-n-30's
sentences amended by its answers of 2026-11-18, §5, PIN-n-33 amended and the fourth form labelled by those of its second
sitting, results/raw/2026-11-18_n-step4-smoke-pause_design-to-code_answers.md §3; later ones strikable until LOCK-n
v1.0); the seat's rulings on the question block
(results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md, Q1-Q9) in OPEN, as
results/raw/2026-11-16_n-ganl_design-to-code_answers.md and ADDENDUM-n1 v0.1 (bound by sha256) give them, with the
answers of 2026-11-18 (results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md, §5) and of its second
sitting (§3) where they amend them. G-ANL-n's canonical run waits for G-CAL-n's dose map.

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
  verdicts --campaign DIR --report R --lock L --date YYYY-MM-DD [--gread G] [--gvec C] [--out DIR]
                        N-pod's VERDICTS and secondary DVs (data/n/verdicts/N-pod_VERDICTS.json, N-pod_secondary.json,
                        write-once), or its NOT-RUN where the stage report has no arm complete before a STOP or the
                        cap: from the campaign's cells, its stage report (n-report-v1) and G-READ-n's artifact
                        (n-gread-v1), under the lock the campaign's identity names. Of record only from the committed
                        analyzer under a committed lock; prints no margin (n §4 "Blinding"). Exit 0 written or
                        identical, 2 refused, 4 STOP.
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
ADDENDUM_REL = "ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md"     # the seat's rulings of 2026-11-16 (v0.1)
ADDENDUM_SHA256 = "e979f8f2af08ddb1f32e3054c002b1d0a3278e49a24b4f6df2cb6c042de95e03"
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
F_TEXT = {F10: "0.10", F20: "0.20"}       # N2's [f] slot (ADDENDUM-n1 §7.6: "at f = [f]")
F_LABEL = {F10: "f0.10", F20: "f0.20"}    # the record labels of N2's reads (n-build's schema)

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


def session_slopes_origin(points: Sequence[float], dm: np.ndarray) -> np.ndarray:
    """§4 as ruled (OPEN-Q1 (b); ADDENDUM-n1 §7.1): per session, the OLS slope of Δm on d through the origin over the
    arm's nonzero dose points, Σ d·Δm / Σ d², BK's construction (its prereg: d "is identically zero at dose 0 by
    construction"). A zero point is refused: the construction fixes it, so it is never an observation."""
    x = np.asarray(points, float)
    y = np.asarray(dm, float)
    if y.ndim != 2 or y.shape[1] != x.shape[0] or x.shape[0] < 1:
        raise AnlStop(f"STOP: a slope over {x.shape[0]} points for values of shape {y.shape}")
    if np.any(x == 0.0):
        raise AnlStop("STOP: a slope through the origin given the point d = 0")
    return y @ x / float(x @ x)


def session_slopes(points: Sequence[float], dm: np.ndarray) -> np.ndarray:
    """The with-intercept slope reported beside the slope of record, descriptive (OPEN-Q1 as ruled: "the with-intercept
    slope is reported beside, labelled descriptive"): per session, OLS with an intercept over the points given, d = 0
    with Δm(0) = 0 included where the arm lists it."""
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

    def label_of(self, value: float) -> str:
        """The record label of N1-V's realised point at ``value`` ('0', or the kept label of +1, +1/2, +d_20, +d_eq or
        −1 whose value it is: a merged point carries its keeper's label), for naming a point (PIN-n-36)."""
        if value == 0.0:
            return "0"
        for p in self.expected_points():
            if not p["label"].startswith("f") and p["value"] == value:
                return p["label"]
        raise ValueError(f"no realised point at d = {value!r}")

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
        """N1-V's (and N1-R's) point matched to N2's f: d_eq's resolved point for f = 0.10, d_20's for f = 0.20 --
        exact iff 2·d_eq ≤ 1 and no merge moved it; the ratio is reported."""
        return self.resolved()["d_eq" if f == F10 else "d_20"]

    def match_ratio(self, f: str) -> float:
        return self.f_point(f) / self.norm_matched(f)

    def cap_binds(self) -> bool:
        """OPEN-Q7 as ruled (ADDENDUM-n1 §5.3): the cap binds iff 2·d_eq > 1, so d_20 = 1 by §2.3's cap."""
        return 2.0 * self.d_eq > 1.0

    def n2_decision_f(self) -> str:
        """OPEN-Q7 as ruled: N2 is decided at f = 0.10 when the cap binds (against N1-V at d_eq, where the norms are
        equal exactly), else at f = 0.20 as §5 writes it; the other f is reported beside."""
        return F10 if self.cap_binds() else F20

    def n1p_points(self) -> tuple[float, ...]:
        """OPEN-Q2 as ruled (ADDENDUM-n1 §5.2): the points N1-P reads, the kept points of +1, +d_20, +d_eq and −1,
        descending."""
        r = self.resolved()
        return tuple(sorted({1.0, -1.0, r["d_20"], r["d_eq"]}, reverse=True))

    def n2_slope_points(self) -> tuple[tuple[float, float], tuple[float, float]]:
        """OPEN-Q9 as ruled ((a) through the origin; ADDENDUM-n1 §7.5): N2's slope over its two points on BK's scale,
        (d_eq, 2·d_eq), and the points its floor's random reads are taken at, d_eq's and d_20's kept points -- equal
        unless the cap binds or a merge moved a point, the mismatch then printed beside (reported only; no §5
        outcome reads N2's slope)."""
        return ((self.d_eq, 2.0 * self.d_eq), (self.norm_matched(F10), self.norm_matched(F20)))


# =====================================================================================================================
# 4. The outcome layer (§5, in its order)
# =====================================================================================================================


def ceiling(L: float, P: float | None) -> float:
    # G-LEAK-n's ceiling max(L(d), P(d)). OPEN-Q2 as ruled (c): N1-P reads +1, +d_20, +d_eq and −1 under the merge
    # (ADDENDUM-n1 §5.2), so P(d) exists at every point a certification is made (ceiling_cert requires it there);
    # where N1-P is not read (+1/2 unless a point merges there) the ceiling G-LEAK-n's table reports is L(d) alone.
    return float(L) if P is None else max(float(L), float(P))


def ceiling_cert(st: "State", pt: float) -> float:
    """The ceiling at a point where §5 certifies or reports a certification beside (N1 at +1; dose at d_eq's point,
    d_20's beside; N2 at its norm-matched points): N1-P reads every such point (OPEN-Q2 as ruled, ADDENDUM-n1 §5.2),
    so P(d) is required there, and its absence STOPs -- a plan the reader did not refuse cannot produce it."""
    if pt not in st.P:
        raise AnlStop(f"STOP: no P(d) at d = {pt!r}, a point where G-LEAK-n certifies (ADDENDUM-n1 §5.2)")
    return ceiling(st.L[pt], st.P[pt])


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
    P: dict[float, float] = field(default_factory=dict)      # N1-P: |mean Δm_P(d)| at each point it reads
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
    # PIN-n-29 as amended (point by point) and PIN-n-36: why a steered arm's reads at one point are not usable, by
    # (arm, the point's value; N2's arms: the f) -- "incomplete", "nonfinite", "shadow", "tau4-emptied" -- [] when
    # usable. The reader records every point it reads; a point not recorded answers from the arm's own `complete`.
    at: dict[tuple[str, Any], list[str]] = field(default_factory=dict)
    # PIN-n-33 as amended and PIN-n-37: the points an unadjudicated pause stands on, by (arm, point or f), the reader's
    # from the stage report's pauses; None (no point map: the battery's literal states, unless a case gives one) reads
    # `paused` per arm at every point.
    paused_at: dict[tuple[str, Any], bool] | None = None

    def paused_on(self, arm: str, key: Any) -> bool:
        """Whether an unadjudicated pause stands on the arm's reads at one point (PIN-n-33 as amended, PIN-n-37)."""
        if self.paused_at is None:
            return bool(self.paused.get(arm))
        return bool(self.paused_at.get((arm, key)))

    def gr(self, axis: str, key: Any) -> str:
        # PIN-n-11: a G-READ-n cell absent or not computed is "not PASS" for §0.6 (reported as NOT-COMPUTED).
        return self.gread.get((axis, key), "NOT-COMPUTED")

    def causes_at(self, arm: str, key: Any) -> list[str]:
        """Why the arm's reads at one point are not usable ([] when they are): PIN-n-29 as amended, PIN-n-36."""
        if (arm, key) in self.at:
            return list(self.at[(arm, key)])
        return [] if self.complete.get(arm) else ["incomplete"]

    def named_at(self, arm: str, key: Any) -> list[str]:
        """causes_at, each named with its arm and the point's record label ('incomplete:N1-P@+d_20'; PIN-n-36)."""
        lab = F_LABEL[key] if key in F_LABEL else self.dmap.label_of(key)
        return [f"{c}:{arm}@{lab}" for c in self.causes_at(arm, key)]


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
    """§5 N1. INDETERMINATE iff an unadjudicated pause stands on N1's reads, or N1-R or N1-P is incomplete, or N1-V is
    (OPEN-Q6 as ruled: §5's "An arm with a partial read set is INDETERMINATE"); then REPLICATED / PARTIAL /
    NOT-REPLICATED on conjuncts (i)-(iv), PARTIAL also needing the mean at +1 above 0 (OPEN-Q8 as ruled, ADDENDUM-n1
    §7.3: the sign). `against`: a certified movement against the conditioned zone at +1 (its CI excluding 0, G-LEAK-n
    certifying it, the mean below 0), which N1's NOT-REPLICATED sentence names."""
    causes = _causes(st, N1_ARMS)
    if causes:
        return {"state": "INDETERMINATE", "causes": causes}
    v1, vm1 = st.V[1.0], st.V[-1.0]
    ceil1 = ceiling_cert(st, 1.0)
    c = {"i": v1.mean >= BAR_I and v1.excludes0(),
         "ii": st.slope_V.mean > st.floor_V,                 # PIN-n-7: signed "exceeds" (floor ≥ 0)
         "iii": above(v1.mean, ceil1),
         "iv": vm1.mean < 0.0 and vm1.excludes0(),           # PIN-n-19: the −1 pole is read (A1), so (iv) is evaluated
         "ci+1": v1.excludes0(),
         "sign": v1.mean > 0.0}                              # ADDENDUM-n1 §7.3: PARTIAL requires the mean at +1 > 0
    if c["i"] and c["ii"] and c["iii"] and c["iv"]:
        state, failing = "REPLICATED", []
    elif c["ii"] and c["iii"] and c["ci+1"] and c["sign"]:
        state, failing = "PARTIAL", [k for k in ("i", "iv") if not c[k]]
    else:
        state, failing = "NOT-REPLICATED", [k for k in ("ci+1", "ii", "iii", "sign") if not c[k]]
    against = c["ci+1"] and c["iii"] and v1.mean < 0.0
    return {"state": state, "conjuncts": c, "failing": failing, "ceiling": ceil1, "against": against}


def dose_outcome(st: State, n1: Mapping) -> dict:
    """§5 Dose. INDETERMINATE iff N1 is INDETERMINATE or the points are incomplete (OPEN-Q6 as ruled: N1-V's, N1-R's or
    N1-P's reads; the d_20 figure beside is then not computed); DETECTABLE iff the CI at d_eq excludes 0, G-LEAK-n
    certifies it there and the mean is above 0 (OPEN-Q8 as ruled, ADDENDUM-n1 §7.3: the sign); else NOT-DETECTABLE (its
    §0.6 label set by the sentence layer), `against` when the movement certified there is against the conditioned
    zone."""
    r = st.dmap.resolved()
    causes = []
    if n1["state"] == "INDETERMINATE":
        causes.append("N1-INDETERMINATE")
    if not (st.complete.get("N1-V") and st.complete.get("N1-R") and st.complete.get("N1-P")):
        causes.append("incomplete:points")                   # subsumed by N1's causes (OPEN-Q6): reported beside
    if causes:
        return {"state": "INDETERMINATE", "causes": causes, "d_20_beside": "not computed"}   # OPEN-Q6 as ruled
    deq, d20 = r["d_eq"], r["d_20"]
    v = st.V[deq]
    ceq = ceiling_cert(st, deq)
    cert = above(v.mean, ceq)
    c20 = ceiling_cert(st, d20)
    state = "DETECTABLE" if (v.excludes0() and cert and v.mean > 0.0) else "NOT-DETECTABLE"
    against = v.excludes0() and cert and v.mean < 0.0
    beside = {"point": d20, "est": st.V[d20], "ceiling": c20, "certified": above(st.V[d20].mean, c20)}
    return {"state": state, "point": deq, "ci_excludes0": v.excludes0(), "certified": cert, "against": against,
            "ceiling": ceq, "d_20_beside": beside}


NOT_COMPUTED = "not computed"               # a figure whose reads are not usable (OPEN-Q6 as ruled; PIN-n-29)


def n2_reads(st: State, f: str) -> list[tuple[str, Any]]:
    """The reads N2's certification at f reads, point by point (PIN-n-29 as amended; the seat's answers of 2026-11-18
    §5.2): N2-E at f, and N1-V, N1-R's 24 directions and N1-P at f's norm-matched point, as (arm, point or f)."""
    m = st.dmap.norm_matched(f)
    return [("N2-E", f), ("N1-V", m), ("N1-R", m), ("N1-P", m)]


def n2_outcome(st: State) -> dict:
    """§5 N2, at its decision f (OPEN-Q7 as ruled, ADDENDUM-n1 §5.3: f = 0.10 against N1-V at d_eq when the cap binds,
    else f = 0.20; the other f beside, with its ratio). INDETERMINATE iff one of the reads its certification reads is
    not usable -- missing, non-finite, its sessions' shadows not usable, or emptied in the TAU/4 row -- or a pause stands
    on one of them (OPEN-Q6 as ruled; PIN-n-29 as amended, ADDENDUM-n1 §7.4's N2 clause read point by point: N2-E at the
    decision f, N1-V, N1-R's 24 directions and N1-P at the norm-matched point; PIN-n-36). Pauses are read point by
    point, as incompleteness is (PIN-n-33 as amended): a pause standing on one of those reads makes N2 INDETERMINATE,
    and one standing on any other read (N1-V at −1, an N1-R cell elsewhere, a guard's) leaves it decided, the points a
    pause stands on being PIN-n-37's. An incompleteness elsewhere in those arms leaves N2 evaluated. SPECIFIC iff
    span_reward's effect is not certified while N1-V's at the norm-matched point is; SHARED iff span_reward's is
    certified; NULL iff neither -- each certification unsigned, as §3 states it (PIN-n-30: the sign enters no N2
    outcome). The guards decide nothing; each guard's figures are reported beside with its pause. The other f's
    figures beside are each 'not computed' where their reads are not usable, and name the arms whose reads there a
    pause stands on (PIN-n-37)."""
    f_dec = st.dmap.n2_decision_f()
    f_bes = F20 if f_dec == F10 else F10
    reads = n2_reads(st, f_dec)
    causes = [f"pause:{a}" for a, k in reads if st.paused_on(a, k)] + [c for a, k in reads for c in st.named_at(a, k)]
    if causes:
        return {"state": "INDETERMINATE", "f": f_dec, "causes": causes}
    m = st.dmap.norm_matched(f_dec)
    ceil_m = ceiling_cert(st, m)
    cert_e = above(st.E[f_dec].mean, ceil_m)
    cert_v = above(st.V[m].mean, ceil_m)
    state = "SPECIFIC" if (not cert_e and cert_v) else "SHARED" if cert_e else "NULL"
    mb = st.dmap.norm_matched(f_bes)
    ok = {a: not st.causes_at(a, k) for a, k in n2_reads(st, f_bes)}
    e_b = st.E[f_bes] if ok["N2-E"] else NOT_COMPUTED
    v_b = st.V[mb] if ok["N1-V"] else NOT_COMPUTED
    c_b = ceiling_cert(st, mb) if (ok["N1-R"] and ok["N1-P"]) else NOT_COMPUTED

    def cert_b(x: Any) -> Any:
        return NOT_COMPUTED if NOT_COMPUTED in (x, c_b) else above(x.mean, c_b)
    beside = {f_bes: {"point": mb, "E": e_b, "V": v_b, "ceiling": c_b,                          # ADDENDUM-n1 §5.3
                      "certified": cert_b(e_b), "certified_V": cert_b(v_b), "match_ratio": st.dmap.match_ratio(f_bes),
                      "paused": [a for a, k in n2_reads(st, f_bes) if st.paused_on(a, k)]},       # PIN-n-37
              "guards": {g: {f: (d[f] if (f in d and not st.causes_at(a, f)) else NOT_COMPUTED) for f in (F10, F20)}
                         | {"paused": bool(st.paused.get(a))}
                         for g, a, d in (("span_sentiment", "N2-S", st.S), ("span_character", "N2-C", st.C))}}
    return {"state": state, "f": f_dec, "point": m, "ceiling": ceil_m, "certified_E": cert_e, "certified_V": cert_v,
            "match_ratio": st.dmap.match_ratio(f_dec), "cap_binds": st.dmap.cap_binds(), "beside": beside}


def n4_outcome(st: State) -> dict:
    """§5 N4: INDETERMINATE with no read obtained iff the arm is incomplete or E undefined, or (OPEN-Q6 as ruled) a
    pause stands on N4's reads; else REVERSE, PASS, DEAD, INDETERMINATE (terminal), in that order."""
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
    """§5 in order: N1, dose (reads N1), N2, N4; the tuple's G-READ-n coordinate is valence at d_eq. The inputs that
    label nulls (§0.6): G-READ-n for valence at +1 (N1) and for span_reward at N2's decision f (OPEN-Q7 as ruled)."""
    n1 = n1_outcome(st)
    dose = dose_outcome(st, n1)
    n2 = n2_outcome(st)
    n4 = n4_outcome(st)
    r = st.dmap.resolved()
    grs = {"d_eq": st.gr("valence", r["d_eq"]), "+1": st.gr("valence", 1.0),
           "E": st.gr("span_reward", st.dmap.n2_decision_f())}
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

# ADDENDUM-n1 §7.6's forms (OPEN-Q8 as ruled; the battery asserts each against the addendum's italic spans, as §5's are
# asserted against the proposal's). The three NOT-DETECTABLE forms carry MOVE_NOT_CERTIFIED where §5 said OLD_MOVE (the
# addendum's quotation); §7.3's clause, MOVE_AGAINST, names a certified movement against the conditioned zone in N1's
# NOT-REPLICATED sentence (PIN-n-28), while at d_eq such a movement takes the seat's fourth form (FOURTH, below).
# A6_DOSE_ND_READABLE_N4 is the cell of §7.2 (N4 not PASS, G-READ-n PASS); N2's sentences say F_AT.
OLD_MOVE = "the margin does not move beyond the leak ceiling"
MOVE_NOT_CERTIFIED = "the margin's movement is not certified (Δm(d_eq) = [x] nats [CI] against a leak ceiling of [c])"
MOVE_AGAINST = ("the margin moves against the conditioned zone beyond the leak ceiling (Δm = [x] nats [CI], ceiling "
                "[c])")
A6_DOSE_ND_READABLE_N4 = ("at this program's dose the state is readable at the decision (AUC [a]) and the margin's "
                          "movement is not certified (Δm(d_eq) = [x] nats [CI] against a leak ceiling of [c]), but "
                          "BK's apparatus has not registered an instructed preference on this checkpoint (N4 [n4]): "
                          "dose is an explanation of record, unresolved")
F_AT = "at f = [f]"
ADDENDUM_FORMS = {"MOVE_NOT_CERTIFIED": MOVE_NOT_CERTIFIED, "A6_DOSE_ND_READABLE_N4": A6_DOSE_ND_READABLE_N4,
                  "MOVE_AGAINST": MOVE_AGAINST, "F_AT": F_AT}
#: secondary (b) in the secondary DVs' output: ADDENDUM-n1 §4 ("is struck; the VERDICTS entry says so"), in its words
B_STRUCK = ("struck (ADDENDUM-n1 §4): nothing is generated in the campaign; §0.4's table stands as the welfare "
            "report")

# The seat's answers of 2026-11-18, §5 (results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md, sha256
# 5843a9bd...7165), transcribed: the battery reads no raw (its hook bars results/raw), so the literal-text checks and the
# values-check hold these to the raw's words. §5.3 (PIN-n-30): each figure of N2's three forms carries its CI and, where
# its mean is below 0, ZONE_WORDS (PIN-n-34). §5.4 (PIN-n-32): where d_eq merges into another point, the NOT-DETECTABLE
# forms print their figure with MERGE_NOTE after it (DETECTABLE's [value] keeps VALUE_MERGED). §5.6 (F11): a movement at
# d_eq certified against the conditioned zone is NOT-DETECTABLE in FOURTH, its readability clause by G-READ-n's state
# (READ_ALT's two branches). The answers of 2026-11-18's second sitting, §3.2
# (results/raw/2026-11-18_n-step4-smoke-pause_design-to-code_answers.md, sha256 cdecf39e...01d3): the fourth form ends
# as A.2 and A.7 do, with LABEL_TAIL, its [label] "answered" iff G-READ-n PASS at d_eq and N4 PASS, CNA_N4 where the
# state is readable and N4 is not PASS, "concluded, not answered" otherwise; the readability clause stays as ruled.
ZONE_WORDS = ", against the conditioned zone"
MERGE_NOTE = " (read at d = [point], the point d_eq merges into under §2.3)"
FOURTH = ("at this program's dose the margin moves against the conditioned zone beyond the leak ceiling (Δm(d_eq) = [x] "
          "nats [CI], ceiling [c])[; the state is readable at the decision (AUC [a]) | ; the state is not readable at "
          "the decision]: dose alone does not account for the program's null on the echo channel, and the effect at "
          "this dose is reversed in sign")
READABLE = "; the state is readable at the decision (AUC [a])"
NOT_READABLE = "; the state is not readable at the decision"
READ_ALT = "[" + READABLE + " | " + NOT_READABLE + "]"
LABEL_TAIL = " — [label]"
CNA_N4 = "concluded, not answered (N4 [n4])"
F4 = {"readable": FOURTH.replace(READ_ALT, READABLE) + LABEL_TAIL,
      "not readable": FOURTH.replace(READ_ALT, NOT_READABLE) + LABEL_TAIL}
RULING_FORMS = ({"ZONE_WORDS": ZONE_WORDS, "MERGE_NOTE": MERGE_NOTE, "CNA_N4": CNA_N4}
                | {f"FOURTH, {k}": v for k, v in F4.items()})
MERGE_SLOT, ZONE_E, ZONE_V = "[merge]", "[zoneE]", "[zoneV]"
DEQ_FIGURE = "Δm(d_eq) = [x] nats [CI]"                                 # §5.4's figure; MERGE_SLOT follows it
MOVE_NC = MOVE_NOT_CERTIFIED.replace(DEQ_FIGURE, DEQ_FIGURE + MERGE_SLOT)
D_ND_ANSWERED = T_DOSE_ND_ANSWERED.replace(OLD_MOVE, MOVE_NC)            # §5's answered form, amended
D_ND_READABLE_N4 = A6_DOSE_ND_READABLE_N4.replace(MOVE_NOT_CERTIFIED, MOVE_NC)
D_FOURTH = {k: v.replace(DEQ_FIGURE, DEQ_FIGURE + MERGE_SLOT) for k, v in F4.items()}

# Code's forms (Appendix A of the question block, adopted with the seat's amendments: OPEN-Q8 as ruled): §5 words the
# cells above only; "PARTIAL and NOT-REPLICATED name the failing conjunct and the figures"; INDETERMINATE, NOT-RUN, N2
# and N4 carry no sentence in §5.
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
                          "readable at the decision: dose is an explanation of record, unresolved")   # A.5, as written
D_ND_NOT_READABLE = C_DOSE_ND_NOT_READABLE.replace(OLD_MOVE, MOVE_NC)    # A.5, amended
C_DOSE_INDET = "INDETERMINATE: the dose question is not evaluated ([causes])"
N2_HEAD = "N2, descriptive (§7.3; it licenses no thesis sentence): "
# A.7's three forms as the seat's answers of 2026-11-18 §5.3 amend them (PIN-n-30, PIN-n-34): every figure with its CI
# and, where its mean is below 0, ZONE_WORDS in [zoneE] / [zoneV], closing the figure's parenthetical, or the sentence
# where the figure has none (SHARED's valence figure).
C_N2 = {"SPECIFIC": N2_HEAD + ("SPECIFIC: at f = [f] this program's evaluative axis (span_reward) does not move BK's "
                               "apparatus beyond the leak ceiling (Δm = [xE] nats [CIE] against [c][zoneE]) while the "
                               "valence direction of record at the norm-matched point does (Δm = [xV] nats [CIV][zoneV]) "
                               "— [label]"),
        "SHARED": N2_HEAD + ("SHARED: at f = [f] this program's evaluative axis (span_reward) moves BK's apparatus "
                             "beyond the leak ceiling (Δm = [xE] nats [CIE] against [c][zoneE]); the valence direction "
                             "of record at the norm-matched point: Δm = [xV] nats [CIV][zoneV]"),
        "NULL": N2_HEAD + ("NULL: at f = [f] neither this program's evaluative axis (span_reward, Δm = [xE] nats "
                           "[CIE][zoneE]) nor the valence direction of record at the norm-matched point (Δm = [xV] nats "
                           "[CIV][zoneV]) moves BK's apparatus beyond the leak ceiling ([c]) — [label]"),
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
         "[-e]", "[reason]", "[f]", "[CIV]", "[zoneE]", "[zoneV]", "[merge]", "[point]")
CONJUNCT_TEXT = {"i": "conjunct (i) (Δm(+1) ≥ 0.545 nats with its 95% CI excluding 0)",
                 "iv": "conjunct (iv) (Δm(−1) < 0 with its 95% CI excluding 0)",
                 "ci+1": "the 95% CI at d = +1 excluding 0",
                 "ii": "conjunct (ii) (the valenced mean slope above its floor)",
                 "iii": "conjunct (iii) (G-LEAK-n certification at d = +1)",
                 "sign": "the mean Δm at d = +1 above 0",
                 "sign-against": "the mean Δm at d = +1 above 0 (" + MOVE_AGAINST + ")"}


def label(n4_state: str, gread_state: str) -> str:
    # OPEN-Q3 as ruled (§0.6; ADDENDUM-n1 §7.2): a null read is answered only if (i) the told positive control (N4)
    # PASSED and (ii) G-READ-n PASSED for that axis and dose; else concluded, not answered. Applied to N1 NOT-REPLICATED
    # (valence, +1), dose NOT-DETECTABLE (valence, d_eq) and N2's span_reward null (SPECIFIC, NULL; span_reward at the
    # decision f).
    return ANSWERED if (n4_state == "PASS" and gread_state == "PASS") else CNA


def failing_text(keys: Sequence[str], against: bool = False) -> str:
    """The failing conditions, by name; the sign's names the certified movement against the conditioned zone when
    there is one (ADDENDUM-n1 §7.3: "with its sentence naming it"; the place in the sentence is Code's form)."""
    return "; ".join(CONJUNCT_TEXT["sign-against" if (k == "sign" and against) else k] for k in keys)


def sentence_n1(state: str, *, n4: str, gr1: str, failing: Sequence[str] | None = None,
                causes: Sequence[str] | None = None, against: bool = False) -> dict:
    if state == "REPLICATED":
        return {"question": "N1", "state": state, "text": T_N1_REPLICATED, "label": None, "form": "§5"}
    if state == "PARTIAL":
        t = C_N1_PARTIAL if failing is None else C_N1_PARTIAL.replace("[failing]", failing_text(failing))
        return {"question": "N1", "state": state, "text": t, "label": None, "form": "Code"}
    if state == "NOT-REPLICATED":
        lab = label(n4, gr1)
        t = C_N1_NOT_REPLICATED.replace("[label]", lab)
        if failing is not None:
            t = t.replace("[failing]", failing_text(failing, against=against))
        return {"question": "N1", "state": state, "text": t, "label": lab, "form": "Code"}
    if state == "INDETERMINATE":
        t = C_N1_INDET if causes is None else C_N1_INDET.replace("[causes]", ", ".join(causes))
        return {"question": "N1", "state": state, "text": t, "label": None, "form": "Code"}
    raise ValueError(f"N1 state {state!r}")


FORM_FOURTH = "the seat's answers of 2026-11-18 §5.6, with §5.4's note and the second sitting's §3.2 label"
FORM_ND = {"answered": "§5, amended by ADDENDUM-n1 §7.6 and the seat's answers of 2026-11-18 §5.4",
           "not readable": "§5, its ellipsis expanded by Code, amended by ADDENDUM-n1 §7.6 and the seat's answers of "
                           "2026-11-18 §5.4",
           "A.6": "ADDENDUM-n1 §7.6, amended by the seat's answers of 2026-11-18 §5.4"}


def sentence_dose(state: str, *, n4: str, gr: str, causes: Sequence[str] | None = None, against: bool = False) -> dict:
    """The dose sentence. ``against``: the movement at d_eq is certified against the conditioned zone (its CI excluding
    0, G-LEAK-n certifying it, the mean below 0; PIN-n-27), so NOT-DETECTABLE takes the seat's fourth form (F11 as
    ruled, §5.6), its readability clause by G-READ-n's state and its label by §0.6 as the others, carried in the
    sentence as the second sitting's §3.2 fills it ('answered', CNA_N4 where readable and N4 not PASS, else CNA)."""
    if against and state != "NOT-DETECTABLE":
        raise ValueError(f"a movement against the conditioned zone at d_eq is NOT-DETECTABLE, not {state!r}")
    if state == "DETECTABLE":
        return {"question": "dose", "state": state, "text": T_DOSE_DETECTABLE, "label": None, "form": "§5"}
    if state == "NOT-DETECTABLE":
        lab = label(n4, gr)
        if against:
            fill = lab if lab == ANSWERED else (CNA_N4.replace("[n4]", n4) if gr == "PASS" else CNA)
            t, form = D_FOURTH["readable" if gr == "PASS" else "not readable"].replace("[label]", fill), FORM_FOURTH
        elif lab == ANSWERED:
            t, form = D_ND_ANSWERED, FORM_ND["answered"]
        elif gr != "PASS":
            t, form = D_ND_NOT_READABLE, FORM_ND["not readable"]
        else:
            t, form = D_ND_READABLE_N4.replace("[n4]", n4), FORM_ND["A.6"]
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


def sentence_set(t: Sequence[str] | str, *, gr1: str = "FAIL", gre: str = "FAIL", n4_no_read: bool = False,
                 dose_against: bool = False) -> dict:
    """One §7 sentence set for an outcome tuple (template form: figures, causes and the failing conjuncts are slots).
    t = (N1, dose, N2, N4, G-READ-n valence at d_eq) or "NOT-RUN". OPEN-Q4 as ruled (confirmed): three inputs that
    are not coordinates change a sentence -- gr1 = G-READ-n (valence, +1), gre = G-READ-n (span_reward, at N2's
    decision f), and n4_no_read (N4's INDETERMINATE "with no read obtained" against the terminal one); the seat's fourth
    NOT-DETECTABLE form (F11 as ruled) adds a fourth, dose_against (a movement at d_eq certified against the
    conditioned zone, which only a NOT-DETECTABLE dose carries: PIN-n-35); the battery runs every tuple under each
    (m's flag precedent: an input, not a coordinate)."""
    if t == NOT_RUN:
        s = {"question": "unit", "state": NOT_RUN, "text": C_NOT_RUN, "label": None, "form": "Code"}
        return {k: dict(s) for k in SLOT_KEYS}
    n1, dose, n2, n4, grd = t
    if n1 not in N1_STATES or dose not in DOSE_STATES or n2 not in N2_STATES or n4 not in N4_STATES \
            or grd not in GREAD_STATES or gr1 not in GREAD_STATES or gre not in GREAD_STATES \
            or not isinstance(n4_no_read, bool) or (n4_no_read and n4 != "INDETERMINATE") \
            or not isinstance(dose_against, bool) or (dose_against and dose != "NOT-DETECTABLE"):
        raise ValueError(f"not a tuple of the outcome space: {t!r} (inputs {gr1!r}, {gre!r}, {n4_no_read!r}, "
                         f"{dose_against!r})")
    return {"7.1": sentence_n1(n1, n4=n4, gr1=gr1), "7.2": sentence_dose(dose, n4=n4, gr=grd, against=dose_against),
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
    norm-matched points. Uncertified effects are reported as such and license no sentence (§3). Each row is read point
    by point (PIN-n-29 as amended; PIN-n-36): computed iff the arm's reads there, N1-R's and, where N1-P reads the
    point, N1-P's are usable, so that the table agrees with N2's outcome."""
    r = st.dmap.resolved()
    rows = []
    labels: dict[float, list[str]] = {}
    for lab in ("+1", "+1/2", "d_20", "d_eq", "-1"):
        labels.setdefault(r[lab], []).append(lab)

    def needs(arm: str, key: Any, pt: float) -> list[str]:
        """Why the reads a certification at pt reads are not usable (N1-P where it is read: OPEN-Q2 as ruled)."""
        reads = [(arm, key), ("N1-R", pt)] + ([("N1-P", pt)] if pt in st.dmap.n1p_points() else [])
        return [c for a, k in reads for c in st.named_at(a, k)]
    for pt in sorted(labels, reverse=True):
        miss = needs("N1-V", pt, pt)
        if miss:
            rows.append({"arm": "N1-V", "point": pt, "labels": labels[pt], "certified": None,
                         "why": f"not usable: {', '.join(miss)}"})
            continue
        P = st.P.get(pt)
        c = ceiling(st.L[pt], P)
        rows.append({"arm": "N1-V", "point": pt, "labels": labels[pt], "mean": st.V[pt].mean, "L": st.L[pt], "P": P,
                     "ceiling": c, "certified": above(st.V[pt].mean, c)})
    for arm, d in (("N2-E", st.E), ("N2-S", st.S), ("N2-C", st.C)):
        for f in (F10, F20):
            pt = st.dmap.norm_matched(f)
            miss = needs(arm, f, pt)
            if miss or f not in d:
                rows.append({"arm": arm, "point": pt, "labels": [f], "certified": None,
                             "why": f"not usable: {', '.join(miss) or arm}"})
                continue
            P = st.P.get(pt)
            c = ceiling(st.L[pt], P)
            rows.append({"arm": arm, "point": pt, "labels": [f], "mean": d[f].mean, "L": st.L[pt], "P": P,
                         "ceiling": c, "certified": above(d[f].mean, c),
                         "match_ratio": st.dmap.match_ratio(f)})
    return rows


GREAD_SECTION5 = {("valence", "+1"): "N1 NOT-REPLICATED's label (§5 N1)",
                  ("valence", "d_eq"): "the dose sentence's label (§5 Dose); the tuple's coordinate"}
GREAD_N2_LABEL = "N2's span_reward null label (§0.6, at N2's decision f: OPEN-Q7 as ruled)"


def gread_table(st: State) -> list[dict]:
    """§3 G-READ-n per axis and dose point, as its artifact gives them; the cells that enter §5 (§0.6) marked. The
    valence points are +1, +1/2, d_20 and d_eq: the −1 reads enter +1's contrast (n §3; GREAD_AXES), so −1 has no
    row."""
    r = st.dmap.resolved()
    rows = []
    for lab in ("+1", "+1/2", "d_20", "d_eq"):
        s = st.gr("valence", r[lab])
        rows.append({"axis": "valence", "point": r[lab], "label": lab, "state": s,
                     "enters": GREAD_SECTION5.get(("valence", lab))})
    for f in (F10, F20):
        rows.append({"axis": "span_reward", "point": st.dmap.f_point(f), "label": f, "state": st.gr("span_reward", f),
                     "enters": GREAD_N2_LABEL if f == st.dmap.n2_decision_f() else None})
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


def italic_spans(s: str) -> list[str]:
    """A line's single-asterisk italic spans, in order (bold's double asterisks skipped)."""
    out, i = [], 0
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


def proposal_spans(text: str) -> dict[str, str]:
    """§5's italic spans at n:136 and n:138, by position, from the proposal's bytes."""
    lines = text.splitlines()
    s136, s138 = italic_spans(lines[135]), italic_spans(lines[137])
    return {"rep": s136[0], "cna": s136[1], "ans": s138[0], "cna138": s138[1], "det": s138[2], "nd_ans": s138[3],
            "nd_cna": s138[4]}


def addendum_spans(text: str) -> dict[str, str]:
    """ADDENDUM-n1 §7.6's italic spans, by position, from the addendum's bytes, with its quotation of the clause §5's
    NOT-DETECTABLE forms said: the movement not certified and the clause it replaces (its first bullet), the cell of
    §7.2 (its second), the movement against the conditioned zone (its third), N2's f and the two labels (its fourth);
    and §4's paragraph, secondary (b) struck."""
    lines = text.splitlines()
    i = next(k for k, s in enumerate(lines) if s.startswith("**7.6 Sentences.**"))
    b = lines[i + 1:i + 5]
    s0, s1, s2, s3 = (italic_spans(x) for x in b)
    q = b[0].split('"')
    j = next(k for k, s in enumerate(lines) if s.startswith("## §4 Secondary (b) struck"))
    return {"add_not_cert": s0[0], "add_old": q[1], "add_a6": s1[0], "add_against": s2[0], "add_f": s3[0],
            "add_ans": s3[1], "add_cna": s3[2], "add_b4": lines[j + 2]}


#: The oracle's own transcription of the seat's answers of 2026-11-18, §5.4's figure with its note and §5.6's fourth
#: form, and of the second sitting's §3.2, the fourth form's ending and its parenthetical for N4 (the battery reads no
#: raw, so a second copy, made apart from the module's: a slip in either fails T2, for the fourth form, its label and
#: the figure, or SENT-RULING, for the note's words and the label's copies).
_ORC_NOTE = "Δm(d_eq) = [x] nats [CI] (read at d = [point], the point d_eq merges into under §2.3)"
_ORC_FOURTH = ("at this program's dose the margin moves against the conditioned zone beyond the leak ceiling "
               "(Δm(d_eq) = [x] nats [CI], ceiling [c])[; the state is readable at the decision (AUC [a]) | ; the "
               "state is not readable at the decision]: dose alone does not account for the program's null on the "
               "echo channel, and the effect at this dose is reversed in sign")
_ORC_TAIL, _ORC_N4 = " — ", " (N4 [n4])"


def oracle_set(t, *, gr1: str, gre: str, n4_no_read: bool, verb: Mapping[str, str], dose_against: bool = False) -> dict:
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
        # ADDENDUM-n1 §7.6 from its own bytes (§5's clause, as the addendum quotes it, becomes the movement not
        # certified), the [merge] slot after the figure §5.4's note follows; the fourth form from the oracle's copy
        fig = _ORC_NOTE[:_ORC_NOTE.index(" (read at d = ")]
        merged = (lambda s: s.replace(fig, fig + "[merge]"))
        lb2 = verb["ans"] if (n4 == "PASS" and grd == "PASS") else verb["cna"]
        if dose_against:
            a, b = _ORC_FOURTH.index("[; "), _ORC_FOURTH.index("]: dose alone")
            readable, not_readable = _ORC_FOURTH[a + 1:b].split(" | ")
            fill = (verb["ans"] if (n4 == "PASS" and grd == "PASS")
                    else ((verb["cna"] + _ORC_N4.replace("[n4]", n4)) if grd == "PASS" else verb["cna"]))
            s2 = (merged(_ORC_FOURTH[:a] + (readable if grd == "PASS" else not_readable) + _ORC_FOURTH[b + 1:])
                  + _ORC_TAIL + fill, lb2,
                  "the seat's answers of 2026-11-18 §5.6, with §5.4's note and the second sitting's §3.2 label")
        elif n4 == "PASS" and grd == "PASS":
            s2 = (verb["nd_ans"].replace(verb["add_old"], merged(verb["add_not_cert"])), lb2,
                  "§5, amended by ADDENDUM-n1 §7.6 and the seat's answers of 2026-11-18 §5.4")
        elif grd == "FAIL":
            s2 = (C_DOSE_ND_NOT_READABLE.replace(verb["add_old"], merged(verb["add_not_cert"])), lb2,
                  "§5, its ellipsis expanded by Code, amended by ADDENDUM-n1 §7.6 and the seat's answers of 2026-11-18 "
                  "§5.4")
        else:
            s2 = (merged(verb["add_a6"]).replace("[n4]", n4), lb2,
                  "ADDENDUM-n1 §7.6, amended by the seat's answers of 2026-11-18 §5.4")
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
    """Every (tuple, gr1, gre, n4_no_read, dose_against) the tuple pass evaluates: 384 tuples x 4 G-READ inputs, x 2
    where N4 is INDETERMINATE (no read / terminal), x 2 where dose is NOT-DETECTABLE (the seat's fourth form: a movement
    at d_eq certified against the conditioned zone, or not; PIN-n-35), + NOT-RUN once = 2,561."""
    out = []
    for t in tuple_space():
        if t == NOT_RUN:
            out.append((t, None, None, False, False))
            continue
        for gr1, gre in itertools.product(GREAD_STATES, GREAD_STATES):
            for nr in ((False, True) if t[3] == "INDETERMINATE" else (False,)):
                for ag in ((False, True) if t[1] == "NOT-DETECTABLE" else (False,)):
                    out.append((t, gr1, gre, nr, ag))
    return out


# =====================================================================================================================
# 9. The battery (§3 G-ANL-n). Selftest-only helpers carry the `_bt` prefix.
# =====================================================================================================================
EXPECTED_CHECKS = 222

_REQ: list[str] = []
_REQ += [f"N1-{x}" for x in ("REPLICATED", "PARTIAL-i", "PARTIAL-iv", "PARTIAL-i-iv", "NOTREP-ci+1", "NOTREP-ii",
                             "NOTREP-iii", "NOTREP-ci+1-ii", "NOTREP-ci+1-iii", "NOTREP-ii-iii", "NOTREP-ci+1-ii-iii",
                             "NOTREP-sign", "NOTREP-ci+1-sign", "NOTREP-iii-sign")]
_REQ += [f"N1-INDET-{k}:{a}" for k in ("pause", "incomplete") for a in N1_ARMS]
_REQ += ["BND-I-EXACT", "BND-I-BELOW", "BND-CI-LO-ZERO", "BND-CI-HI-ZERO", "BND-CERT-EQUAL", "BND-SLOPE-EQ-FLOOR",
         "BND-IV-ZERO", "BND-P-ABOVE-L", "BND-P-DEQ", "BND-NEG-CERT", "BND-P-REQUIRED"]
_REQ += ["DOSE-DET-POS", "DOSE-ND-AGAINST", "DOSE-ND-CI", "DOSE-ND-UNCERT", "DOSE-ND-NEG-CI", "DOSE-ND-NEG-UNCERT",
         "DOSE-INDET-N1", "DOSE-INDET-POINTS",
         "DOSE-BESIDE-D20"]
_REQ += ["N2-SPECIFIC", "N2-SHARED-V-CERT", "N2-SHARED-V-UNCERT", "N2-NULL", "N2-INDET-pause:N2-E",
         "N2-INDET-pause:N1-V", "N2-INDET-pause:N1-R", "N2-INDET-pause:N1-P", "N2-GUARD-PAUSE",
         "N2-INDET-incomplete:N2-E", "N2-INDET-incomplete:N1-V", "N2-INDET-incomplete:N1-R",
         "N2-INDET-incomplete:N1-P", "N2-GUARDS-DECIDE-NOTHING", "N2-POINT-ELSEWHERE", "N2-POINT-CAUSES",
         "N2-F10-BESIDE", "N2-MATCH-RATIO", "N2-CAP-F10", "N2-UNSIGNED", "N2-BESIDE-FIELDS", "N2-BESIDE-NOT-COMPUTED",
         "N2-PAUSE-POINTWISE"]
_REQ += ["N4-PASS", "N4-REVERSE", "N4-DEAD", "N4-INDET-TERMINAL", "N4-NOREAD-incomplete:N4-T",
         "N4-NOREAD-incomplete:N4-Ts", "N4-NOREAD-pause:N4-T", "N4-NOREAD-pause:N4-Ts", "N4-NOREAD-E-undefined",
         "N4-ORD-REV-OVER-DEAD", "N4-ORD-PASS-OVER-DEAD", "N4-BND-MEAN-EQ-E", "N4-BND-MEAN-EQ-NEGE",
         "N4-BND-HI-EQ-DEAD", "N4-BND-CI-LO-ZERO"]
_REQ += [f"NR-{c}" for c in NOT_RUN_CAUSES] + ["NR-REFUSE-PREMATURE", "NR-REFUSE-STAGE", "NR-REFUSE-UNIT",
                                                "NR-REFUSE-CAUSE", "NR-REFUSE-KEYS"]
_REQ += [f"GLEAK-{a}-{c}" for a in ("N1-V", "N2-E", "N2-S", "N2-C") for c in ("CERT", "UNCERT", "INCOMPLETE")]
_REQ += [f"GREAD-{c}" for c in ("PASS", "FAIL", "NOT-COMPUTED", "ENTERS-N1", "ENTERS-DOSE", "ENTERS-N2")]
_REQ += ["GLEAK-N1P-INCOMPLETE", "GLEAK-POINTWISE"]
_REQ += ["SENT-VERBATIM", "SENT-FAILING-PARTIAL", "SENT-FAILING-NOTREP", "SENT-CAUSES", "SENT-REFUSES",
         "SENT-CODE-FORMS", "SENT-ADDENDUM", "SENT-FILLED-DOSE-ND", "SENT-FILLED-N1-AGAINST", "SENT-FILLED-N2-CAP",
         "SENT-RULING", "SENT-FILLED-DOSE-FOURTH", "SENT-FILLED-N2-ZONE", "SENT-FOURTH-FILLS"]
_REQ += [f"TUP-T{i}" for i in range(1, 11)] + ["TUP-DETERMINISM", "TUP-COUNT"]
_REQ += ["REACH-DOSE-IFF-N1", "REACH-SHAPE-a", "REACH-SHAPE-b", "REACH-SHAPE-c", "REACH-SHAPE-d", "REACH-N4-FREE",
         "REACH-NO-RAISE", "REACH-FOURTH"]
_REQ += ["NUM-KEYSTREAM-M159", "NUM-KNOWN-ANSWER", "NUM-BOOT-DETERMINISM", "NUM-BOOT-CONSTANT", "NUM-BOOT-LOOP",
         "NUM-PCT-METHOD", "NUM-SLOPE-CLOSED-FORM", "NUM-SLOPE-BESIDE", "NUM-SLOPE-INTERCEPT", "NUM-SD0",
         "NUM-NONFINITE-STOP", "NUM-BK-FITS-COINCIDE", "NUM-CAP-DECISION-F", "NUM-N1P-POINTS",
         "NUM-BK-REPRO", "NUM-BK-FIDELITY", "NUM-DOSEMAP-SHAPES", "NUM-DOSEMAP-REFUSE",
         "NUM-DOSEMAP-POINTS", "NUM-PEARSON", "CNT-LABEL-MASS", "NUM-N2-POINTS"]
_REQ += ["STR-PROPOSAL-SHA", "STR-ADDENDUM-SHA", "STR-VERBATIM-IN-PROPOSAL", "STR-TAU-PREREG", "STR-NO-REPO-IMPORT",
         "STR-NO-HEAVY", "STR-OPEN-HOOK", "STR-NO-CANONICAL-WRITE", "STR-PINS"]
_REQ += ["RD-POSITIVE", "RD-FILLED", "RD-NULL", "RD-SPECIFIC", "RD-PARTIAL", "RD-INDET", "RD-NONFINITE", "RD-MERGED",
         "RD-PAUSE", "RD-PAUSE-POINTS", "RD-GREAD", "RD-SENSITIVITY", "RD-SECONDARY", "RD-REFUSE", "RD-FILLED-FIGURES",
         "RD-FILLED-FORMS", "RD-SHADOW", "RD-ASYM", "RD-MERGED-DEQ", "RD-GREAD-MIXED", "CNT-COUNTERS",
         "RD-SECONDARY-FLOOR", "RD-CAP-BINDS", "RD-CAP-SLOPES", "RD-POINTWISE"]
_REQ += ["NUM-DOSEMAP-SCHEMA", "NUM-MERGE-EDGE", "NUM-REACH-CLASS", "CMD-NOTRUN", "CMD-NOTRUN-REFUSE",
         "CMD-GANL-REFUSE", "STR-GANL-ARTIFACT"]
_REQ += ["VD-COMPLETE", "VD-WRITE-ONCE", "VD-EXPOSURE", "VD-SENSITIVITY", "VD-STDOUT", "VD-PISTOP-STANDING",
         "VD-PAUSE-POINTS", "VD-PAUSE-RENDERING", "VD-NOTRUN-CAP", "VD-NOTRUN-PISTOP", "VD-NOTRUN-GVER", "VD-REFUSE",
         "VD-GREAD-MIXED", "VD-PRECHECK", "VD-SOME-ARMS", "VD-MERGED-ROUTE-A", "VD-ONE-OUTCOME", "VD-PLAIN"]
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
MAP_B = DoseMap(0.72, 1.0)             # the cap binds: d_20 merged into +1, N2 decided at d_eq (shape b)
MAP_C = DoseMap(0.49, 2 * 0.49)        # d_20 merged into +1 without the cap, d_eq into +1/2 (shape c)
MAP_D = DoseMap(0.97, 1.0)             # d_20 and d_eq merged into +1 (shape d)
_X = Est(1.0, 0.9, 1.1)                # large positive, CI excludes 0, certified at the battery's L 0.05
_Z = Est(0.0, -0.05, 0.05)             # null: CI includes 0, uncertified


def literal_state(dmap: DoseMap = MAP_A, **over) -> State:
    """A complete, unpaused state with every outcome at its 'positive' value (N1 REPLICATED, dose DETECTABLE, N2
    SHARED, N4 PASS) at L = 0.05 everywhere and P = 0.04 at each point N1-P reads (±1, d_20's and d_eq's: OPEN-Q2 as
    ruled); keyword overrides replace fields. Used by the battery and by map_reach, which the canonical `ganl` run calls
    on the pinned map (hence no `_bt` prefix)."""
    pts = dmap.points()
    st = State(dmap=dmap, complete={a: True for a in ARMS}, paused={a: False for a in ARMS},
               V={p: (Est(-0.7, -0.8, -0.6) if p < 0 else Est(max(p, 0.3), max(p, 0.3) - 0.1, max(p, 0.3) + 0.1))
                  for p in pts if p != 0.0},
               slope_V=Est(0.9, 0.8, 1.0), floor_V=0.3, L={p: 0.05 for p in pts if p != 0.0},
               P={p: 0.04 for p in dmap.n1p_points()}, E={F10: Est(0.2, 0.1, 0.3), F20: Est(0.3, 0.2, 0.4)},
               S={F10: Est(0.0, -0.1, 0.1), F20: Est(0.0, -0.1, 0.1)}, C={F10: Est(0.0, -0.1, 0.1),
                                                                           F20: Est(0.0, -0.1, 0.1)},
               told=Est(1.0, 0.8, 1.2, 98), e_sham=0.1,
               gread={("valence", p): "PASS" for p in pts if p != 0.0} | {("span_reward", F10): "PASS",
                                                                         ("span_reward", F20): "PASS"})
    for k, v in over.items():
        if k in ("complete", "paused", "at"):
            getattr(st, k).update(v)
        elif k in ("V", "L", "P", "E", "S", "C", "gread"):
            getattr(st, k).update(v)
        else:
            setattr(st, k, v)
    return st


def pointwise(dmap: DoseMap, bad: Mapping[tuple[str, Any], Sequence[str]]) -> dict:
    """State overrides for arms not usable at the points in ``bad`` alone ((arm, point or f) -> causes): each such
    arm incomplete, every one of its points recorded (PIN-n-36), [] where usable. For map_reach and the battery."""
    keys = {"N1-V": [p for p in dmap.points() if p != 0.0], "N1-R": [p for p in dmap.points() if p != 0.0],
            "N1-P": list(dmap.n1p_points())}
    arms = sorted({a for a, _ in bad})
    return {"complete": {a: False for a in arms},
            "at": {(a, k): list(bad.get((a, k), [])) for a in arms for k in keys.get(a, [F10, F20])}}


def _apply(st: State, *pats: Mapping[str, Any]) -> State:
    """Update a state's completeness, pauses and point-wise causes from patterns (map_reach's and the battery's)."""
    for pat in pats:
        for k in ("paused", "complete", "at"):
            getattr(st, k).update(pat.get(k, {}))
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
              "NOT-REPLICATED", ["ci+1", "ii", "iii"]),
             # the sign (OPEN-Q8 as ruled, ADDENDUM-n1 §7.3): PARTIAL needs the mean at +1 above 0
             ("NOTREP-sign", {"V": {1.0: Est(-0.6, -0.7, -0.5)}}, "NOT-REPLICATED", ["sign"]),
             ("NOTREP-ci+1-sign", {"V": {1.0: Est(-0.3, -0.6, 0.1)}}, "NOT-REPLICATED", ["ci+1", "sign"]),
             # a negative mean whose CI excludes 0 but within the ceiling: not against (PIN-n-27 needs (iii))
             ("NOTREP-iii-sign", {"V": {1.0: Est(-0.03, -0.04, -0.02)}}, "NOT-REPLICATED", ["iii", "sign"])]
    for cid, over, want, failing in cases:
        g = n1_outcome(literal_state(**over))
        against = cid == "NOTREP-sign"                       # PIN-n-27: CI excluding 0, certified, the mean below 0
        B.chk(f"N1 {want} failing {failing}" + (" (a certified movement against the conditioned zone, PIN-n-27)"
                                                  if against else ""),
              g["state"] == want and g["failing"] == failing and g["against"] is against, g, cover=[f"N1-{cid}"])
    for kind in ("pause", "incomplete"):
        for a in N1_ARMS:
            over = {"paused": {a: True}} if kind == "pause" else {"complete": {a: False}}
            g = n1_outcome(literal_state(**over))
            tag = " (OPEN-Q6 as ruled)" if (kind, a) == ("incomplete", "N1-V") else ""
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
    d = dose_outcome(literal_state(V={deq: Est(0.08, 0.04, 0.12)}, L={deq: 0.06}, P={deq: 0.07}), n1_outcome(st))
    d2 = dose_outcome(literal_state(V={deq: Est(0.08, 0.04, 0.12)}, L={deq: 0.06}, P={deq: 0.09}), n1_outcome(st))
    B.chk("ceiling (OPEN-Q2 as ruled: N1-P read at d_eq): max(L, P) at d_eq -- P(d_eq) 0.07 over L 0.06 leaves 0.08 "
          "certified; P(d_eq) 0.09 governs and 0.08 is not",
          d["state"] == "DETECTABLE" and d["ceiling"] == 0.07 and d2["state"] == "NOT-DETECTABLE"
          and d2["ceiling"] == 0.09, (d["ceiling"], d2["ceiling"]), cover=["BND-P-DEQ"])
    n1_full = n1_outcome(literal_state())
    req = {}
    for name, pt, fn in (("N1 at +1", 1.0, n1_outcome), ("dose at d_eq", deq, lambda s: dose_outcome(s, n1_full)),
                         ("N2 at d_20's point", MAP_A.resolved()["d_20"], n2_outcome)):
        s_ = literal_state()
        del s_.P[pt]
        req[name] = _bt_raises(lambda: fn(s_), (AnlStop,))[0]
    half = [r for r in gleak_table(literal_state()) if r["arm"] == "N1-V" and r["point"] == 0.5]
    req["+1/2 row L alone"] = len(half) == 1 and half[0]["P"] is None and half[0]["ceiling"] == half[0]["L"]
    B.chk("P(d) is required where G-LEAK-n certifies (OPEN-Q2 as ruled: N1-P reads every such point): its absence at "
          "+1 (N1), at d_eq (dose) or at N2's norm-matched point STOPs; G-LEAK-n's table reports L alone at +1/2, "
          "which N1-P does not read", all(req.values()), req, cover=["BND-P-REQUIRED"])
    g = n1_outcome(literal_state(V={1.0: Est(-1.0, -1.1, -0.9)}))
    B.chk("a negative Δm(+1) beyond the ceiling is certified (|mean|) and against the conditioned zone: (ii)-(iii) "
          "hold, CI excludes 0, the sign fails -> NOT-REPLICATED (ADDENDUM-n1 §7.3; PIN-n-27)",
          g["state"] == "NOT-REPLICATED" and g["conjuncts"]["iii"] is True and g["failing"] == ["sign"]
          and g["against"] is True, g, cover=["BND-NEG-CERT"])
    # dose
    n1 = n1_outcome(literal_state())
    for cid, v, Ld, want, ag in (("DOSE-DET-POS", Est(0.3, 0.2, 0.4), 0.05, "DETECTABLE", False),
                                 ("DOSE-ND-AGAINST", Est(-0.3, -0.4, -0.2), 0.05, "NOT-DETECTABLE", True),
                                 ("DOSE-ND-CI", Est(0.3, -0.01, 0.6), 0.05, "NOT-DETECTABLE", False),
                                 ("DOSE-ND-UNCERT", Est(0.04, 0.02, 0.06), 0.05, "NOT-DETECTABLE", False),
                                 ("DOSE-ND-NEG-CI", Est(-0.3, -0.6, 0.1), 0.05, "NOT-DETECTABLE", False),
                                 ("DOSE-ND-NEG-UNCERT", Est(-0.03, -0.04, -0.02), 0.05, "NOT-DETECTABLE", False)):
        dd = dose_outcome(literal_state(V={deq: v}, L={deq: Ld}), n1)
        B.chk(f"dose {want}: Δm(d_eq) {v.mean} [{v.lo}, {v.hi}] against L {Ld}" + (
            " (certified against the conditioned zone: the sign, ADDENDUM-n1 §7.3)" if ag else ""),
            dd["state"] == want and dd["against"] is ag, dd, cover=[cid])
    ok = True
    for kind in ("pause", "incomplete"):
        for a in N1_ARMS:
            over = {"paused": {a: True}} if kind == "pause" else {"complete": {a: False}}
            s_ = literal_state(**over)
            dd = dose_outcome(s_, n1_outcome(s_))
            ok &= dd["state"] == "INDETERMINATE" and "N1-INDETERMINATE" in dd["causes"]
    B.chk("dose INDETERMINATE whenever N1 is, under each of N1's six causes", ok, cover=["DOSE-INDET-N1"])
    pts_ok = {}
    for a in ("N1-R", "N1-P"):
        s_ = literal_state(complete={a: False})
        dd_i = dose_outcome(s_, n1_outcome(s_))
        pts_ok[a] = (dd_i["causes"], dd_i.get("d_20_beside"))
    B.chk("dose INDETERMINATE names 'incomplete:points' beside N1's, for N1-R and N1-P alike (subsumed), and reports "
          "the d_20 figure beside as not computed (OPEN-Q6 as ruled)",
          all(c == (["N1-INDETERMINATE", "incomplete:points"], "not computed") for c in pts_ok.values()), pts_ok,
          cover=["DOSE-INDET-POINTS"])
    s_ = literal_state()
    dd = dose_outcome(s_, n1_outcome(s_))
    d20 = s_.dmap.resolved()["d_20"]
    s_p = literal_state(V={d20: Est(0.06, 0.04, 0.08)}, L={d20: 0.05}, P={d20: 0.07})
    dp = dose_outcome(s_p, n1_outcome(s_p))["d_20_beside"]
    B.chk("dose reports d_20 beside (point, estimate, ceiling, certification), its ceiling max(L, P): 0.06 against "
          "P(d_20) 0.07 over L 0.05 is not certified", dd["d_20_beside"]["point"] == d20
          and dd["d_20_beside"]["certified"] is True and dp["ceiling"] == 0.07 and dp["certified"] is False,
          (dd["d_20_beside"], dp), cover=["DOSE-BESIDE-D20"])
    # N2
    m20 = MAP_A.norm_matched(F20)
    for cid, over, want in (("N2-SPECIFIC", {"E": {F20: Est(0.01, -0.02, 0.04)}}, "SPECIFIC"),
                            ("N2-SHARED-V-CERT", {}, "SHARED"),
                            ("N2-SHARED-V-UNCERT", {"V": {m20: _Z}}, "SHARED"),
                            ("N2-NULL", {"E": {F20: Est(0.01, -0.02, 0.04)}, "V": {m20: _Z}}, "NULL")):
        g = n2_outcome(literal_state(**over))
        B.chk(f"N2 {want} ({cid})", g["state"] == want, g, cover=[cid])
    # PIN-n-29 as amended: N2's causes point by point -- N2-E at the decision f (f = 0.20 on shape (a), 0.10 when the
    # cap binds), N1-V, N1-R and N1-P at its norm-matched point (+d_20 on shape (a), +d_eq on shape (b))
    for arm in ("N2-E", "N1-V", "N1-R", "N1-P"):
        ga, gb = n2_outcome(literal_state(paused={arm: True})), n2_outcome(literal_state(MAP_B, paused={arm: True}))
        B.chk(f"N2 INDETERMINATE by pause:{arm}, on shape (a) and when the cap binds: a literal state's pause stands "
              "on every point of its arm, so on the reads N2's certification reads (n:140; PIN-n-29 and PIN-n-33 as "
              "amended)",
              ga["state"] == gb["state"] == "INDETERMINATE" and ga["causes"] == gb["causes"] == [f"pause:{arm}"],
              (ga, gb), cover=[f"N2-INDET-pause:{arm}"])
    gs = {(sh, a): n2_outcome(literal_state(dm_, paused={a: True})) for sh, dm_ in (("a", MAP_A), ("b", MAP_B))
          for a in ("N2-S", "N2-C")}
    gname = {"N2-S": "span_sentiment", "N2-C": "span_character"}
    B.chk("a pause on a guard's reads alone (N2-S, N2-C) leaves N2 evaluated, on shape (a) and when the cap binds, the "
          "guard's figures reported beside with its pause (PIN-n-33)",
          all(g["state"] == "SHARED" and g["beside"]["guards"][gname[a]]["paused"] is True
              and g["beside"]["guards"][gname["N2-C" if a == "N2-S" else "N2-S"]]["paused"] is False
              for (sh, a), g in gs.items()), {k: g["state"] for k, g in gs.items()}, cover=["N2-GUARD-PAUSE"])
    # PIN-n-33 as amended (the answers of 2026-11-18, second sitting, §3.1) and PIN-n-37: a pause standing on one
    # point alone (paused_at), each case on shape (a) and when the cap binds; a decided N2's beside keeps its figures
    # as the unpaused state's (the v5 review's B5), and a guard paused at either f carries its flag
    pw, want_pw = {}, {}
    fig_k = ("E", "V", "ceiling", "certified", "certified_V")
    for sh, dm_ in (("a", MAP_A), ("b", MAP_B)):
        f_d = dm_.n2_decision_f()
        f_o = F10 if f_d == F20 else F20
        m_, mo = dm_.norm_matched(f_d), dm_.norm_matched(f_o)
        base_b = n2_outcome(literal_state(dm_))["beside"][f_o]
        for arm, key, mine in (("N1-V", -1.0, False), ("N1-R", 0.5, False), ("N2-E", f_o, False), ("N1-P", mo, False),
                               ("N2-S", f_d, False), ("N2-S", f_o, False), ("N2-E", f_d, True), ("N1-V", m_, True),
                               ("N1-R", m_, True), ("N1-P", m_, True)):
            o_ = outcomes(literal_state(dm_, paused={arm: True}, paused_at={(arm, key): True}))
            g_ = o_["N2"]
            bes = g_.get("beside", {}).get(f_o, {})
            pw[(sh, arm, key)] = (o_["N1"]["state"], g_["state"], g_.get("causes"), bes.get("paused"),
                                  g_.get("beside", {}).get("guards", {}).get("span_sentiment", {}).get("paused"),
                                  None if mine else all(bes.get(k) == base_b[k] for k in fig_k))
            n1_w = "INDETERMINATE" if arm in N1_ARMS else "REPLICATED"
            want_pw[(sh, arm, key)] = ((n1_w, "INDETERMINATE", [f"pause:{arm}"], None, None, None) if mine else
                                       (n1_w, "SHARED", None, [arm] if (arm, key) in (("N2-E", f_o), ("N1-P", mo))
                                        else [], arm == "N2-S", True))
    B.chk("pauses point by point (PIN-n-33 as amended: the answers of 2026-11-18, second sitting, §3.1; PIN-n-37), "
          "on shape (a) and when the cap binds: a pause standing on one of N2's reads (N2-E at the decision f, N1-V, "
          "N1-R or N1-P at its norm-matched point) makes N2 INDETERMINATE (pause:arm); one on any other read (N1-V at "
          "−1, N1-R at +1/2, the other f's N2-E and N1-P beside, a guard's at either f) leaves it decided, the beside "
          "naming the arms paused at its own reads with its figures as the unpaused state's, and a guard's figures "
          "carrying its pause; N1 stays per arm (n:134)",
          pw == want_pw, [k for k in want_pw if pw.get(k) != want_pw[k]], cover=["N2-PAUSE-POINTWISE"])
    for arm in ("N2-E", "N1-V", "N1-R", "N1-P"):
        ga, gb = (n2_outcome(literal_state(complete={arm: False})),
                  n2_outcome(literal_state(MAP_B, complete={arm: False})))
        wa = f"incomplete:{arm}@" + ("f0.20" if arm == "N2-E" else "+d_20")
        wb = f"incomplete:{arm}@" + ("f0.10" if arm == "N2-E" else "+d_eq")
        B.chk(f"N2 INDETERMINATE by an incomplete {arm}, the cause naming the point its certification reads ({wa}; "
              f"{wb} when the cap binds: OPEN-Q6 as ruled, PIN-n-29 as amended, PIN-n-36)",
              ga["state"] == gb["state"] == "INDETERMINATE" and ga["causes"] == [wa] and gb["causes"] == [wb],
              (ga, gb), cover=[f"N2-INDET-incomplete:{arm}"])
    el = {}
    bes_k = ("E", "V", "ceiling", "certified", "certified_V")
    for sh, dm_, fb in (("a", MAP_A, F10), ("b", MAP_B, F20)):
        for name, bad in (("N1-P at -1", {("N1-P", -1.0): ["incomplete"]}),
                          ("N1-R at +1/2", {("N1-R", 0.5): ["nonfinite"]}),
                          ("N1-V at -1", {("N1-V", -1.0): ["tau4-emptied"]}),
                          ("N1-P at +1", {("N1-P", 1.0): ["shadow"]}),
                          ("N2-E at the other f", {("N2-E", fb): ["incomplete"]})):
            s_ = literal_state(dm_, **pointwise(dm_, bad))
            o_ = outcomes(s_)
            arm = next(iter(bad))[0]
            bes = o_["N2"].get("beside", {}).get(fb, {})
            got = (o_["N1"]["state"], o_["N1"].get("causes"), o_["dose"]["state"], o_["N2"]["state"],
                   tuple(k for k in bes_k if bes.get(k) == "not computed"))
            want_n1 = (("REPLICATED", None, "DETECTABLE") if arm == "N2-E"
                       else ("INDETERMINATE", [f"incomplete:{arm}"], "INDETERMINATE"))
            # the beside's figures not computed only where a read of its own point is the one not usable: N2-E at the
            # other f (span_reward's figure and its certification); N1-P at +1 when the cap binds (+1 is the beside's
            # point there: the ceiling and both certifications)
            want_nc = (("E", "certified") if arm == "N2-E" else
                       ("ceiling", "certified", "certified_V") if (sh, name) == ("b", "N1-P at +1") else ())
            el[(sh, name)] = got == want_n1 + ("SHARED", want_nc)
    B.chk("an incompleteness elsewhere in N2's arms (N1-P at −1 and at +1, N1-R at +1/2, N1-V at −1, N2-E at the "
          "other f) leaves N2 evaluated, while N1 and dose are INDETERMINATE by their own rules (N1 per arm, n:134), on "
          "shape (a) and when the cap binds; its beside's figures are each computed unless a read at the beside's own "
          "point is the one not usable (the seat's answers of 2026-11-18 §5.2)", all(el.values()),
          [k for k, v in el.items() if not v], cover=["N2-POINT-ELSEWHERE"])
    m_a = MAP_A.norm_matched(F20)
    bad_a = {("N2-E", F20): ["incomplete", "nonfinite"], ("N1-V", m_a): ["nonfinite"],
             ("N1-R", m_a): ["tau4-emptied"], ("N1-P", m_a): ["shadow"]}
    pc = {"a": n2_outcome(literal_state(**(pointwise(MAP_A, bad_a) | {"paused": {"N1-R": True}})))["causes"],
          "c": n2_outcome(literal_state(MAP_C, **pointwise(MAP_C, {("N1-P", 1.0): ["incomplete"]})))["causes"],
          "d": n2_outcome(literal_state(MAP_D, **pointwise(MAP_D, {("N1-V", 1.0): ["shadow"]})))["causes"]}
    want_pc = {"a": ["pause:N1-R", "incomplete:N2-E@f0.20", "nonfinite:N2-E@f0.20", "nonfinite:N1-V@+d_20",
                     "tau4-emptied:N1-R@+d_20", "shadow:N1-P@+d_20"],
               "c": ["incomplete:N1-P@+1"], "d": ["shadow:N1-V@+1"]}
    B.chk("N2's causes at its own reads, in order: pauses by arm first, then each read's causes by kind, the point named "
          "by its record label, a merged point by its keeper's (+1 on shapes (c) and (d); PIN-n-36)", pc == want_pc, pc,
          cover=["N2-POINT-CAUSES"])
    base = n2_outcome(literal_state(E={F20: Est(0.01, -0.02, 0.04)}))["state"]
    same = all(n2_outcome(literal_state(E={F20: Est(0.01, -0.02, 0.04)}, S={F20: s}, C={F20: c}))["state"] == base
               for s in (_X, _Z, Est(-1, -1.1, -0.9)) for c in (_X, _Z, Est(-1, -1.1, -0.9)))
    B.chk("N2's guards decide nothing (span_sentiment, span_character varied over nine pairs, the outcome fixed)",
          same and base == "SPECIFIC", base, cover=["N2-GUARDS-DECIDE-NOTHING"])
    g = n2_outcome(literal_state(E={F10: Est(0.01, -0.02, 0.04)}))
    B.chk("N2 reports f = 0.10 beside (its own certification at d_eq's point), deciding nothing",
          g["state"] == "SHARED" and g["beside"]["f=0.10"]["certified"] is False, g["beside"]["f=0.10"],
          cover=["N2-F10-BESIDE"])
    ga, gb = n2_outcome(literal_state()), n2_outcome(literal_state(MAP_B))
    B.chk("N2's decision f and the norm match (OPEN-Q7 as ruled, ADDENDUM-n1 §5.3): shape (a) decided at f = 0.20, "
          "ratio 1, f = 0.10 beside; when the cap binds (shape b, 2·0.72 > 1) decided at f = 0.10 against d_eq, ratio "
          "1, with f = 0.20 beside against d = 1 at the ratio 1.44",
          ga["f"] == F20 and ga["match_ratio"] == 1.0 and ga["cap_binds"] is False and F10 in ga["beside"]
          and gb["f"] == F10 and gb["point"] == 0.72 and gb["match_ratio"] == 1.0 and gb["cap_binds"] is True
          and gb["beside"][F20]["point"] == 1.0 and abs(gb["beside"][F20]["match_ratio"] - 1.44) < 1e-12,
          (ga["f"], gb["f"], gb["match_ratio"], gb["beside"].get(F20, {}).get("match_ratio")),
          cover=["N2-MATCH-RATIO"])
    e_unc = {F10: Est(0.01, -0.02, 0.04)}
    sa, sb = n2_outcome(literal_state(E=e_unc))["state"], n2_outcome(literal_state(MAP_B, E=e_unc))["state"]
    B.chk("the decision f decides: span_reward uncertified at f = 0.10 and certified at f = 0.20 gives SHARED on "
          "shape (a), decided at 0.20, and SPECIFIC when the cap binds, decided at 0.10 (OPEN-Q7 as ruled)",
          sa == "SHARED" and sb == "SPECIFIC", (sa, sb), cover=["N2-CAP-F10"])
    neg = Est(-0.3, -0.4, -0.2)
    un = {"E-negative": n2_outcome(literal_state(E={F20: neg}))["state"],
          "V-negative": n2_outcome(literal_state(E={F20: Est(0.01, -0.02, 0.04)}, V={2 / 3: neg}))["state"]}
    B.chk("N2's certifications are unsigned (PIN-n-30; §3's |mean|): span_reward at −0.3 beyond the ceiling is "
          "SHARED; span_reward still and the valence direction at −0.3 at the norm-matched point is SPECIFIC",
          un == {"E-negative": "SHARED", "V-negative": "SPECIFIC"}, un, cover=["N2-UNSIGNED"])
    sa_, sb_ = literal_state(), literal_state(MAP_B)
    ga_, gb_ = n2_outcome(sa_), n2_outcome(sb_)
    ia_ = n2_outcome(literal_state(complete={"N2-E": False}))
    ib_ = n2_outcome(literal_state(MAP_B, complete={"N2-E": False}))
    bf = {"a": ga_["beside"][F10]["E"] == sa_.E[F10] and ga_["beside"][F10]["V"] == sa_.V[1 / 3]
          and ga_["beside"][F10]["certified_V"] is True and ga_["beside"][F10]["point"] == 1 / 3,
          "b": gb_["beside"][F20]["E"] == sb_.E[F20] and gb_["beside"][F20]["V"] == sb_.V[1.0]
          and gb_["beside"][F20]["certified_V"] is True and gb_["beside"][F20]["point"] == 1.0,
          "indet-f": (ia_["state"], ia_["f"], ib_["state"], ib_["f"]) == ("INDETERMINATE", F20, "INDETERMINATE", F10)}
    gu_ = n2_outcome(literal_state(E={F10: Est(0.01, -0.02, 0.04)}))["beside"][F10]
    bf["a-E-uncertified"] = gu_["certified"] is False and gu_["certified_V"] is True
    B.chk("N2's beside carries the other f's span_reward estimate and N1-V at its point with that certification "
          "(ADDENDUM-n1 §5.3: 'against N1-V at d = 1' when the cap binds), on shapes (a) and (b), each certified on "
          "its own (span_reward uncertified beside a certified valence); an INDETERMINATE N2 names its decision f",
          all(bf.values()), bf, cover=["N2-BESIDE-FIELDS"])
    m_b10 = MAP_A.norm_matched(F10)
    nc = {}
    for name, bad in (("N2-E", {("N2-E", F10): ["incomplete"]}), ("N1-V", {("N1-V", m_b10): ["nonfinite"]}),
                      ("N1-R", {("N1-R", m_b10): ["shadow"]}), ("N1-P", {("N1-P", m_b10): ["incomplete"]})):
        g_ = n2_outcome(literal_state(**pointwise(MAP_A, bad)))
        b_ = g_.get("beside", {}).get(F10, {})
        nc[name] = (g_["state"], *(b_.get(k) == "not computed" for k in ("E", "V", "ceiling", "certified",
                                                                         "certified_V")))
    want_nc = {"N2-E": ("SHARED", True, False, False, True, False), "N1-V": ("SHARED", False, True, False, False, True),
               "N1-R": ("SHARED", False, False, True, True, True), "N1-P": ("SHARED", False, False, True, True, True)}
    B.chk("N2's beside (the other f) reports each figure 'not computed' where its reads are not usable -- span_reward's "
          "estimate (N2-E), N1-V's, the ceiling (N1-R, N1-P) and the certifications that read them -- while N2 is "
          "decided at its own f (PIN-n-29 as amended)", nc == want_nc, nc, cover=["N2-BESIDE-NOT-COMPUTED"])
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
        tag = " (OPEN-Q6 as ruled)" if "pause" in cid else ""
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
    gi = gleak_table(literal_state(complete={"N1-P": False}))
    rows_v = {r["point"]: r for r in gi if r["arm"] == "N1-V"}
    rows_e = [r for r in gi if r["arm"] == "N2-E"]
    gi_ok = (all(rows_v[p]["certified"] is None and "N1-P" in rows_v[p]["why"] for p in MAP_A.n1p_points())
             and rows_v[0.5]["certified"] is not None and len(rows_e) == 2
             and all(r["certified"] is None and "N1-P" in r["why"] for r in rows_e))
    B.chk("G-LEAK-n's table with N1-P incomplete: every row at a point N1-P reads (±1, d_20's and d_eq's; N2's "
          "matched points) is not computed, naming N1-P, and +1/2, which N1-P does not read, is computed (OPEN-Q2 as "
          "ruled)", gi_ok, {p: r.get("why") for p, r in rows_v.items()}, cover=["GLEAK-N1P-INCOMPLETE"])
    gp = gleak_table(literal_state(**pointwise(MAP_A, {("N1-P", -1.0): ["incomplete"], ("N1-R", 0.5): ["nonfinite"],
                                                       ("N2-E", F10): ["shadow"]})))
    why = {(r["arm"], r["labels"][0]): r.get("why") for r in gp if r["certified"] is None}
    done = {(r["arm"], r["labels"][0]) for r in gp if r["certified"] is not None}
    want_why = {("N1-V", "-1"): "not usable: incomplete:N1-P@-1", ("N1-V", "+1/2"): "not usable: nonfinite:N1-R@+1/2",
                ("N2-E", F10): "not usable: shadow:N2-E@f0.10"}
    B.chk("G-LEAK-n's table is read point by point (PIN-n-29 as amended, PIN-n-36), as N2 is: N1-P incomplete at −1, "
          "N1-R non-finite at +1/2 and N2-E's shadows at f = 0.10 leave exactly those rows not computed, each naming "
          "its cause and point, and every other row computed", why == want_why
          and {("N1-V", "+1"), ("N1-V", "d_20"), ("N1-V", "d_eq"), ("N2-E", F20), ("N2-S", F10), ("N2-S", F20),
               ("N2-C", F10), ("N2-C", F20)} == done, (why, sorted(done)), cover=["GLEAK-POINTWISE"])
    st3 = literal_state(gread={("valence", 1.0): "FAIL", ("span_reward", F10): "PASS"})
    del st3.gread[("valence", MAP_A.resolved()["d_eq"])]
    gt = gread_table(st3)
    states = {r["state"] for r in gt}
    for c in ("PASS", "FAIL", "NOT-COMPUTED"):
        B.chk(f"G-READ-n table: a {c} cell is reported as such", c in states, sorted(states), cover=[f"GREAD-{c}"])
    ent = {r["label"]: r["enters"] for r in gt if r["enters"]}
    ent_b = {r["label"]: r["enters"] for r in gread_table(literal_state(MAP_B)) if r["enters"]}
    B.chk("G-READ-n table: exactly three cells enter §5 -- valence +1 (N1), valence d_eq (dose), span_reward at N2's "
          "decision f (N2): f = 0.20 on shape (a), f = 0.10 when the cap binds (OPEN-Q7 as ruled)",
          sorted(ent) == sorted(["+1", "d_eq", F20]) and sorted(ent_b) == sorted(["+1", "d_eq", F10]), (ent, ent_b),
          cover=["GREAD-ENTERS-N1", "GREAD-ENTERS-DOSE", "GREAD-ENTERS-N2"])


def _bt_sentences(B: _Battery, verb: Mapping[str, str]) -> None:
    ok = (T_N1_REPLICATED == verb["rep"] and T_DOSE_DETECTABLE == verb["det"] and T_DOSE_ND_ANSWERED == verb["nd_ans"]
          and T_DOSE_ND_NOT_ANSWERED == verb["nd_cna"] and ANSWERED == verb["ans"] and CNA == verb["cna"] == verb["cna138"]
          and C_DOSE_ND_NOT_READABLE.endswith(verb["nd_cna"].lstrip("…").split("and ", 1)[1]))
    B.chk("§5's four sentences and two labels are the proposal's italic spans at n:136 and n:138, character for "
          "character; Code's expansion of the ellipsis ends in the span's own words", ok, cover=["SENT-VERBATIM"])
    add = {"MOVE_NOT_CERTIFIED": MOVE_NOT_CERTIFIED == verb["add_not_cert"], "OLD_MOVE": OLD_MOVE == verb["add_old"],
           "A6": A6_DOSE_ND_READABLE_N4 == verb["add_a6"], "MOVE_AGAINST": MOVE_AGAINST == verb["add_against"],
           "F_AT": F_AT == verb["add_f"], "labels": ANSWERED == verb["add_ans"] and CNA == verb["add_cna"],
           "once": T_DOSE_ND_ANSWERED.count(OLD_MOVE) == C_DOSE_ND_NOT_READABLE.count(OLD_MOVE) == 1
           and A6_DOSE_ND_READABLE_N4.count(MOVE_NOT_CERTIFIED) == 1
           and all(C_N2[s].count(F_AT) == 1 for s in ("SPECIFIC", "SHARED", "NULL")),
           "replaced": all(f.count(MOVE_NC) == 1 for f in (D_ND_ANSWERED, D_ND_NOT_READABLE, D_ND_READABLE_N4))
           and OLD_MOVE not in D_ND_ANSWERED + D_ND_NOT_READABLE and MOVE_NOT_CERTIFIED not in D_ND_READABLE_N4
           and MOVE_NC == MOVE_NOT_CERTIFIED.replace(DEQ_FIGURE, DEQ_FIGURE + MERGE_SLOT) != MOVE_NOT_CERTIFIED,
           "b struck": B_STRUCK.startswith("struck (ADDENDUM-n1 §4): ")
           and all(c[:1].upper() + c[1:] in verb["add_b4"] or c in verb["add_b4"]
                   for c in B_STRUCK.split(": ", 1)[1].split("; "))
           and "is struck; the VERDICTS entry says so" in verb["add_b4"]}
    B.chk("ADDENDUM-n1 §7.6's forms are its italic spans, character for character (the movement not certified, the "
          "cell of §7.2, the movement against the conditioned zone, 'at f = [f]', the two labels) and §5's clause is "
          "its quotation; each replaced exactly once by the movement not certified, the [merge] slot after its "
          "figure (OPEN-Q8 as ruled; the seat's answers of 2026-11-18 §5.4); secondary (b) reads struck in §4's own "
          "clauses", all(add.values()), [k for k, v in add.items() if not v], cover=["SENT-ADDENDUM"])
    # The seat's answers of 2026-11-18 §5 (transcribed: the battery reads no raw), each against words written here
    spec_v = ("while the valence direction of record at the norm-matched point does (Δm = [xV] nats "
              "[CIV][, against the conditioned zone])")                       # §5.3's quotation, its "…" dropped
    n2f = {s: C_N2[s] for s in ("SPECIFIC", "SHARED", "NULL")}
    rul = {"zone words": ZONE_WORDS == ", against the conditioned zone",
           "SPECIFIC's quoted clause": spec_v in n2f["SPECIFIC"].replace(ZONE_V, "[, against the conditioned zone]"),
           "every figure, its CI and the words (PIN-n-34)": all(
               f.count(t) == 1 for f in n2f.values() for t in ("[xE]", "[CIE]", ZONE_E, "[xV]", "[CIV]", ZONE_V))
           and all(f.index("[xE]") < f.index("[CIE]") < f.index(ZONE_E) and f.index("[xV]") < f.index("[CIV]")
                   < f.index(ZONE_V) for f in n2f.values())
           and all(f[f.index(z) + len(z):][:1] in (")", "") for f in n2f.values() for z in (ZONE_E, ZONE_V)),
           "the note (§5.4), against the oracle's copy": DEQ_FIGURE + MERGE_NOTE == _ORC_NOTE,
           "the figure once in each NOT-DETECTABLE form": all(f.count(DEQ_FIGURE) == 1 for f in (
               MOVE_NOT_CERTIFIED, A6_DOSE_ND_READABLE_N4, FOURTH)),
           "the fourth form (§5.6) and its alternation": FOURTH == _ORC_FOURTH and FOURTH.count(READ_ALT) == 1
           and READ_ALT == "[; the state is readable at the decision (AUC [a]) | ; the state is not readable at the "
                           "decision]",
           "its branches, the [merge] slot after the figure": all(
               D_FOURTH[k] == F4[k].replace(DEQ_FIGURE, DEQ_FIGURE + MERGE_SLOT) and READ_ALT not in F4[k]
               and F4[k].count(DEQ_FIGURE + ", ceiling [c])") == 1 for k in ("readable", "not readable"))
           and "AUC [a]" in F4["readable"] and "[a]" not in F4["not readable"],
           "'an explanation of record' in the three forms only": all(
               "dose is an explanation of record" in f for f in (D_ND_ANSWERED, D_ND_NOT_READABLE, D_ND_READABLE_N4))
           and not any("explanation of record" in f for f in D_FOURTH.values()),
           "the fourth form's ending and its fill for N4 (the second sitting's §3.2), against the oracle's copies": (
               LABEL_TAIL == _ORC_TAIL + "[label]" and CNA_N4 == CNA + _ORC_N4
               and all(F4[k] == FOURTH.replace(READ_ALT, r) + _ORC_TAIL + "[label]" and F4[k].count("[label]") == 1
                       and D_FOURTH[k].endswith(LABEL_TAIL) for k, r in (("readable", READABLE),
                                                                         ("not readable", NOT_READABLE))))}
    B.chk("the seat's forms of 2026-11-18 (§5.3, §5.4, §5.6) as transcribed: the zone's words; SPECIFIC's quoted "
          "clause; each figure of N2's three forms with its CI and the words closing its parenthetical; the merge note "
          "after the figure Δm(d_eq) = [x] nats [CI], once in each NOT-DETECTABLE form; the fourth form equal to the "
          "oracle's copy, its two readability branches; 'dose is an explanation of record' only where no movement is "
          "certified; and the second sitting's §3.2: the fourth form ending ' — [label]', its fill 'concluded, not "
          "answered (N4 [n4])'", all(rul.values()), [k for k, v in rul.items() if not v], cover=["SENT-RULING"])
    forms = {tuple(f) for f in (["i"], ["iv"], ["i", "iv"])}
    txt = {f: sentence_n1("PARTIAL", n4="PASS", gr1="PASS", failing=list(f))["text"] for f in forms}
    B.chk("N1 PARTIAL names its failing conjuncts (OPEN-Q8 as ruled): three forms, each naming exactly its "
          "conjuncts, no slot left",
          len(set(txt.values())) == 3 and all("[failing]" not in t for t in txt.values())
          and all(all(CONJUNCT_TEXT[k] in t for k in f) and all(CONJUNCT_TEXT[k] not in t for k in ("i", "iv")
                                                                if k not in f) for f, t in txt.items()),
          cover=["SENT-FAILING-PARTIAL"])
    sets = [list(c) for r in (1, 2, 3, 4) for c in itertools.combinations(("ci+1", "ii", "iii", "sign"), r)]
    txt = [sentence_n1("NOT-REPLICATED", n4="PASS", gr1="FAIL", failing=f)["text"] for f in sets]
    t_ag = sentence_n1("NOT-REPLICATED", n4="PASS", gr1="FAIL", failing=["ii", "sign"], against=True)["text"]
    B.chk("N1 NOT-REPLICATED names its failing conditions (OPEN-Q8 as ruled; the sign, ADDENDUM-n1 §7.3): fifteen "
          "forms, each naming exactly its own; with a certified movement against the conditioned zone, the sign names "
          "it (PIN-n-28)", len(set(txt)) == 15
          and all(all(CONJUNCT_TEXT[k] in t for k in f) and all(CONJUNCT_TEXT[k] not in t for k in ("ci+1", "ii", "iii",
                                                                                                 "sign") if k not in f)
                  for f, t in zip(sets, txt))
          and all(MOVE_AGAINST not in t for t in txt) and MOVE_AGAINST in t_ag and CONJUNCT_TEXT["ii"] in t_ag,
          cover=["SENT-FAILING-NOTREP"])
    t = sentence_n1("INDETERMINATE", n4="PASS", gr1="PASS", causes=["pause:N1-R", "incomplete:N1-P"])["text"]
    t2 = sentence_n4("INDETERMINATE", no_read=True, causes=["incomplete:N4-T"])["text"]
    B.chk("INDETERMINATE sentences carry their causes (OPEN-Q8 as ruled)",
          "pause:N1-R, incomplete:N1-P" in t and "incomplete:N4-T" in t2
          and "no read obtained" in t2, (t, t2), cover=["SENT-CAUSES"])
    bad = [("N1", lambda: sentence_n1("PASS", n4="PASS", gr1="PASS")),
           ("set", lambda: sentence_set(("REPLICATED", "DETECTABLE", "SHARED", "PASS", "MAYBE"))),
           ("no-read on PASS", lambda: sentence_set(("REPLICATED", "DETECTABLE", "SHARED", "PASS", "PASS"),
                                                     n4_no_read=True)),
           ("against on DETECTABLE", lambda: sentence_set(("REPLICATED", "DETECTABLE", "SHARED", "PASS", "PASS"),
                                                          dose_against=True)),
           ("dose sentence: against on INDETERMINATE", lambda: sentence_dose("INDETERMINATE", n4="PASS", gr="PASS",
                                                                             against=True))]
    res = [(n, _bt_raises(f)) for n, f in bad]
    B.chk("the sentence layer refuses a value outside the outcome space (five cases; a movement against the "
          "conditioned zone at d_eq on a dose not NOT-DETECTABLE among them, in the set and in the dose sentence: "
          "PIN-n-35)", all(r[0] for _, r in res), res, cover=["SENT-REFUSES"])
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
    B.chk(f"the module's {len(cf)} sentence forms beyond §5's verbatim cells (Code's, OPEN-Q8 as ruled, ADDENDUM-n1 "
          "§7.6's and the seat's of 2026-11-18) are pinned by digest (CODE_FORMS_SHA256), pairwise distinct, and use "
          "declared slots only", dig == CODE_FORMS_SHA256 and len(set(cf.values())) == len(cf) and not stray,
          (dig, stray), cover=["SENT-CODE-FORMS"])
    # ADDENDUM-n1 §7.6's forms filled, against literal text written here (the v3 review's B1-B3)
    def s4(x): return f"{x:+.4f}"
    def p4(x): return f"{x:.4f}"
    def c4(e): return f"[{e.lo:+.4f}, {e.hi:+.4f}]"
    nc, ag = Est(0.03, -0.01, 0.07), Est(-0.3, -0.4, -0.2)
    note = " (read at d = +1/2, the point d_eq merges into under §2.3)"          # §5.4, shape (c): d_eq into +1/2
    got_d, want_d, got_4, want_4 = {}, {}, {}, {}
    for mk, v in (("nc", nc), ("ag", ag)):
        for sh, dm_ in (("unmerged", MAP_A), ("merged", MAP_C)):
            deq_ = dm_.resolved()["d_eq"]
            nt = note if sh == "merged" else ""
            dead = {"told": Est(0.2, 0.1, 0.3, 98), "e_sham": 0.5}
            fail = {"gread": {("valence", deq_): "FAIL"}}
            for form, over in (("answered", {}), ("not readable", fail), ("A.6", dead),
                               ("not readable, N4 DEAD", fail | dead)):
                st_f = literal_state(dm_, V={deq_: v}, **over)
                o_f = outcomes(st_f)
                s_f = sentence_set_filled(o_f, st_f, route="B", auc={"d_eq": 0.9})["7.2"]
                got = (o_f["dose"]["state"], o_f["dose"]["against"], s_f["label"], s_f["text"])
                lab_w = "answered" if form == "answered" else "concluded, not answered"
                if mk == "nc":
                    mv = (f"the margin's movement is not certified (Δm(d_eq) = {s4(nc.mean)} nats {c4(nc)}{nt} against a "
                          f"leak ceiling of {p4(0.05)})")
                    t_w = {"answered": "at this program's dose the state is readable at the decision (AUC 0.900) and "
                                       + mv + ": dose is an explanation of record for the program's null",
                           "not readable": "at this program's dose " + mv + " and the state is not readable at the "
                                           "decision: dose is an explanation of record, unresolved",
                           "A.6": "at this program's dose the state is readable at the decision (AUC 0.900) and " + mv
                                  + ", but BK's apparatus has not registered an instructed preference on this "
                                    "checkpoint (N4 DEAD): dose is an explanation of record, unresolved"}[
                        form.split(",")[0]]                     # A.5 not readable, with N4 PASS or not
                    got_d[(sh, form)], want_d[(sh, form)] = got, ("NOT-DETECTABLE", False, lab_w, t_w)
                else:
                    rd_ = ("; the state is not readable at the decision" if form.startswith("not readable")
                           else "; the state is readable at the decision (AUC 0.900)")
                    tail = {"answered": " — answered", "A.6": " — concluded, not answered (N4 DEAD)"}.get(
                        form, " — concluded, not answered")                        # the second sitting's §3.2
                    t_w = ("at this program's dose the margin moves against the conditioned zone beyond the leak "
                           f"ceiling (Δm(d_eq) = {s4(ag.mean)} nats {c4(ag)}{nt}, ceiling {p4(0.05)}){rd_}: dose alone "
                           "does not account for the program's null on the echo channel, and the effect at this dose "
                           "is reversed in sign" + tail)
                    got_4[(sh, form)], want_4[(sh, form)] = got, ("NOT-DETECTABLE", True, lab_w, t_w)
    B.chk("the dose NOT-DETECTABLE sentence, filled, equals literal text in each of its three forms (answered; not "
          "readable, with N4 PASS and with N4 DEAD; N4 not PASS) with the movement not certified, on shape (a) and "
          "with d_eq merged into +1/2 (shape c), where the figure carries the seat's note (ADDENDUM-n1 §7.6; the "
          "seat's answers of 2026-11-18 §5.4; eight sentences)", got_d == want_d,
          [k for k in want_d if got_d.get(k) != want_d[k]], cover=["SENT-FILLED-DOSE-ND"])
    B.chk("a movement at d_eq certified against the conditioned zone takes the seat's fourth NOT-DETECTABLE form, "
          "filled, equal to literal text: its readability clause by G-READ-n (readable in the answered and N4-not-PASS "
          "cells, not readable in the other two), the note where d_eq merges, and its label in the sentence in each of "
          "its three fills: answered; concluded, not answered (N4 DEAD), readable with N4 not PASS; concluded, not "
          "answered, not readable with N4 PASS and with N4 DEAD (F11 as ruled, §5.6; §5.4; the second sitting's §3.2; "
          "eight sentences)", got_4 == want_4, [k for k in want_4 if got_4.get(k) != want_4[k]],
          cover=["SENT-FILLED-DOSE-FOURTH"])
    ends, wrong = {"answered": 0, "N4": 0, "otherwise": 0}, []
    for t_, gr1_, gre_, nr_, da_ in evaluations():
        if not da_:
            continue
        n4_, grd_ = t_[3], t_[4]
        cat = "answered" if (n4_, grd_) == ("PASS", "PASS") else "N4" if grd_ == "PASS" else "otherwise"
        want_e = {"answered": " — answered", "N4": f" — concluded, not answered (N4 {n4_})",
                  "otherwise": " — concluded, not answered"}[cat]
        txt = sentence_set(t_, gr1=gr1_, gre=gre_, n4_no_read=nr_, dose_against=True)["7.2"]["text"]
        ends[cat] += 1
        if not txt.endswith(want_e) or txt.count(" — ") != 1:
            wrong.append((t_, gr1_, gre_, nr_))
    B.chk("the fourth form carries its label in the sentence on each of the tuple pass's 640 evaluations with a "
          "movement at d_eq certified against the conditioned zone (the second sitting's §3.2): ' — answered' on 64 "
          "(G-READ-n PASS at d_eq, N4 PASS), ' — concluded, not answered (N4 [n4])' with N4's state on 256 (G-READ-n "
          "PASS, N4 not PASS), ' — concluded, not answered' on 320 (G-READ-n not PASS)",
          not wrong and ends == {"answered": 64, "N4": 256, "otherwise": 320}, (ends, wrong[:3]),
          cover=["SENT-FOURTH-FILLS"])
    got_1, want_1 = {}, {}
    for k1, v in (("against", Est(-0.6, -0.7, -0.5)), ("within", Est(-0.03, -0.04, -0.02))):
        st_f = literal_state(V={1.0: v})
        o_f = outcomes(st_f)
        got_1[k1] = sentence_set_filled(o_f, st_f, route="B", auc={"d_eq": 0.9})["7.1"]["text"]
        failing = ("the mean Δm at d = +1 above 0 (the margin moves against the conditioned zone beyond the leak "
                   f"ceiling (Δm = {s4(v.mean)} nats {c4(v)}, ceiling {p4(0.05)}))" if k1 == "against" else
                   "conjunct (iii) (G-LEAK-n certification at d = +1); the mean Δm at d = +1 above 0")
        want_1[k1] = ("NOT-REPLICATED: BK's fixed-text effect does not replicate on OLMo-2-32B Instruct in this "
                      f"program's implementation on a reconstructed direction; {failing} fails: Δm(+1) = {s4(v.mean)} "
                      f"nats {c4(v)}, theirs 1.09 [1.00, 1.19]; slope {s4(0.9)} against a floor of {p4(0.3)}; leak "
                      f"ceiling {p4(0.05)} — answered")
    B.chk("N1's NOT-REPLICATED sentence, filled, equals literal text: a certified movement against the conditioned "
          "zone named in the sign's place with the seat's clause (PIN-n-28), and a negative mean within the ceiling "
          "named as (iii) and the sign, no clause", got_1 == want_1, [k for k in want_1 if got_1.get(k) != want_1[k]],
          cover=["SENT-FILLED-N1-AGAINST"])
    head = "N2, descriptive (§7.3; it licenses no thesis sentence): "
    e_lo = Est(0.01, -0.02, 0.04)
    v72 = Est(0.72, 0.62, 0.82)
    spec = (head + "SPECIFIC: at f = 0.10 this program's evaluative axis (span_reward) does not move BK's apparatus "
            f"beyond the leak ceiling (Δm = {s4(0.01)} nats {c4(e_lo)} against {p4(0.05)}) while the valence direction "
            f"of record at the norm-matched point does (Δm = {s4(0.72)} nats {c4(v72)}) — ")
    want_2 = {"SHARED": head + "SHARED: at f = 0.10 this program's evaluative axis (span_reward) moves BK's apparatus "
                               f"beyond the leak ceiling (Δm = {s4(0.2)} nats {c4(Est(0.2, 0.1, 0.3))} against "
                               f"{p4(0.05)}); the valence direction of record at the norm-matched point: Δm = "
                               f"{s4(0.72)} nats {c4(v72)}",
              "SPECIFIC": spec + "answered", "SPECIFIC, f0.10 FAIL": spec + "concluded, not answered",
              "SPECIFIC, f0.20 FAIL": spec + "answered"}
    got_2 = {}
    for k2, over in (("SHARED", {}), ("SPECIFIC", {"E": {F10: e_lo}}),
                     ("SPECIFIC, f0.10 FAIL", {"E": {F10: e_lo}, "gread": {("span_reward", F10): "FAIL"}}),
                     ("SPECIFIC, f0.20 FAIL", {"E": {F10: e_lo}, "gread": {("span_reward", F20): "FAIL"}})):
        st_f = literal_state(MAP_B, **over)
        got_2[k2] = sentence_set_filled(outcomes(st_f), st_f, route="B", auc={"d_eq": 0.9})["7.3"]["text"]
    B.chk("N2's sentence where the cap binds (2·0.72 > 1), filled, equals literal text: 'at f = 0.10', span_reward's "
          "figures at f = 0.10, the valence direction's at d_eq, each with its CI (PIN-n-30, PIN-n-34), the ceiling "
          "there; its label from span_reward's G-READ-n at f = 0.10 alone (OPEN-Q7 as ruled)", got_2 == want_2,
          [k for k in want_2 if got_2.get(k) != want_2[k]], cover=["SENT-FILLED-N2-CAP"])
    zw = ", against the conditioned zone"
    m23 = MAP_A.norm_matched(F20)
    v23, e_n, v_neg, v_sub, e_neg = (Est(2 / 3, 2 / 3 - 0.1, 2 / 3 + 0.1), Est(-0.01, -0.04, 0.02),
                                     Est(-0.3, -0.4, -0.2), Est(-0.03, -0.04, -0.02), Est(-0.3, -0.4, -0.2))
    sp_ = head + "SPECIFIC: at f = 0.20 this program's evaluative axis (span_reward) does not move BK's apparatus beyond "
    sh_ = head + "SHARED: at f = 0.20 this program's evaluative axis (span_reward) moves BK's apparatus beyond the leak "
    want_z = {
        "SPECIFIC, the valence direction against": sp_ + f"the leak ceiling (Δm = {s4(0.01)} nats {c4(e_lo)} against "
        f"{p4(0.05)}) while the valence direction of record at the norm-matched point does (Δm = {s4(-0.3)} nats "
        f"{c4(v_neg)}{zw}) — answered",
        "SPECIFIC, span_reward below 0 within the ceiling": sp_ + f"the leak ceiling (Δm = {s4(-0.01)} nats {c4(e_n)} "
        f"against {p4(0.05)}{zw}) while the valence direction of record at the norm-matched point does (Δm = "
        f"{s4(2 / 3)} nats {c4(v23)}) — answered",
        "SHARED, span_reward against": sh_ + f"ceiling (Δm = {s4(-0.3)} nats {c4(e_neg)} against {p4(0.05)}{zw}); the "
        f"valence direction of record at the norm-matched point: Δm = {s4(2 / 3)} nats {c4(v23)}",
        "SHARED, the valence direction below 0": sh_ + f"ceiling (Δm = {s4(0.3)} nats {c4(Est(0.3, 0.2, 0.4))} against "
        f"{p4(0.05)}); the valence direction of record at the norm-matched point: Δm = {s4(-0.03)} nats {c4(v_sub)}{zw}",
        "NULL, both below 0": head + "NULL: at f = 0.20 neither this program's evaluative axis (span_reward, Δm = "
        f"{s4(-0.01)} nats {c4(e_n)}{zw}) nor the valence direction of record at the norm-matched point (Δm = "
        f"{s4(-0.03)} nats {c4(v_sub)}{zw}) moves BK's apparatus beyond the leak ceiling ({p4(0.05)}) — answered",
        "NULL, span_reward exactly 0": head + "NULL: at f = 0.20 neither this program's evaluative axis (span_reward, "
        f"Δm = {s4(0.0)} nats {c4(_Z)}) nor the valence direction of record at the norm-matched point (Δm = "
        f"{s4(-0.03)} nats {c4(v_sub)}{zw}) moves BK's apparatus beyond the leak ceiling ({p4(0.05)}) — answered",
        "NULL, the valence direction exactly 0": head + "NULL: at f = 0.20 neither this program's evaluative axis "
        f"(span_reward, Δm = {s4(-0.01)} nats {c4(e_n)}{zw}) nor the valence direction of record at the norm-matched "
        f"point (Δm = {s4(0.0)} nats {c4(_Z)}) moves BK's apparatus beyond the leak ceiling ({p4(0.05)}) — answered"}
    got_z = {}
    for kz, over in (("SPECIFIC, the valence direction against", {"E": {F20: e_lo}, "V": {m23: v_neg}}),
                     ("SPECIFIC, span_reward below 0 within the ceiling", {"E": {F20: e_n}}),
                     ("SHARED, span_reward against", {"E": {F20: e_neg}}),
                     ("SHARED, the valence direction below 0", {"V": {m23: v_sub}}),
                     ("NULL, both below 0", {"E": {F20: e_n}, "V": {m23: v_sub}}),
                     ("NULL, span_reward exactly 0", {"E": {F20: _Z}, "V": {m23: v_sub}}),
                     ("NULL, the valence direction exactly 0", {"E": {F20: e_n}, "V": {m23: _Z}})):
        st_f = literal_state(**over)
        got_z[kz] = sentence_set_filled(outcomes(st_f), st_f, route="B", auc={"d_eq": 0.9})["7.3"]["text"]
    B.chk("N2's three forms, filled, equal literal text with the seat's words where a figure's mean is below 0, "
          "certified or not, on either figure, and on neither at a mean of exactly 0 (the seat's answers of 2026-11-18 "
          "§5.3: PIN-n-30, PIN-n-34); the sign decides no N2 outcome (seven sentences)", got_z == want_z,
          [k for k in want_z if got_z.get(k) != want_z[k]], cover=["SENT-FILLED-N2-ZONE"])


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
    fig = _ORC_NOTE[:_ORC_NOTE.index(" (read at d = ")]
    nd_am = verb["nd_ans"].replace(verb["add_old"], verb["add_not_cert"].replace(fig, fig + "[merge]"))  # §5's, amended
    for (t, gr1, gre, nr, ag) in evaluations():
        kw = {} if t == NOT_RUN else {"gr1": gr1, "gre": gre, "n4_no_read": nr, "dose_against": ag}
        out = sentence_set(t, **kw)
        orc = oracle_set(t, gr1=gr1, gre=gre, n4_no_read=nr, verb=verb, dose_against=ag)
        h.update((_canon({"t": t, "gr1": gr1, "gre": gre, "n4_no_read": nr, "dose_against": ag, "set": out})
                  + "\n").encode("utf-8"))
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
            keys = {"7.1": (n1, gr1, n4), "7.2": (dose, grd, n4, ag), "7.3": (n2, gre, n4), "N4": (n4, nr)}
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
                  nd_am if (dose == "NOT-DETECTABLE" and n4 == "PASS" and grd == "PASS" and not ag) else None}
            r["T8"] = all((out[k]["text"] == v) if v is not None else
                          (out[k]["text"] not in (verb["rep"], verb["det"], verb["nd_ans"], nd_am))
                          for k, v in v8.items())
        toks = {m for v in out.values() for m in re.findall(r"\[[^\[\]]*\]", v["text"])}
        r["T9"] = toks <= allowed
        for kk in names:
            counts[kk][0] += bool(r[kk])
            counts[kk][1] += 1
            if not r[kk]:
                fails.setdefault(kk, (t, gr1, gre, nr, ag))
        for k in SLOT_KEYS:
            form = (out[k]["state"], out[k]["form"], out[k]["label"], out[k].get("no_read", False))
            tal[k][form] = tal[k].get(form, 0) + 1
    return counts, h.hexdigest(), tal, fails


def _bt_expected_tallies() -> dict:
    """Hand-derived (Code's arithmetic, derived in results/raw/2026-11-18_n-analyze_v4_review.md): 2,560 evaluations of
    the 384 tuples + NOT-RUN. The 640 added by the dose's fourth input (PIN-n-35) repeat the 640 NOT-DETECTABLE
    evaluations, a third of the 1,920, which hold a third of each N1, N2 and N4 form's count, so each of those gains a
    third; 7.2's fourth form takes 64 answered (N4 PASS, G-READ-n PASS at d_eq) and 576 concluded, not answered."""
    a = "the seat's answers of 2026-11-18 §5.4"
    f4 = "the seat's answers of 2026-11-18 §5.6, with §5.4's note and the second sitting's §3.2 label"
    t = {"7.1": {("REPLICATED", "§5", None, False): 640, ("PARTIAL", "Code", None, False): 640,
                 ("NOT-REPLICATED", "Code", ANSWERED, False): 64, ("NOT-REPLICATED", "Code", CNA, False): 576,
                 ("INDETERMINATE", "Code", None, False): 640},
         "7.2": {("DETECTABLE", "§5", None, False): 640,
                 ("NOT-DETECTABLE", f"§5, amended by ADDENDUM-n1 §7.6 and {a}", ANSWERED, False): 64,
                 ("NOT-DETECTABLE", f"§5, its ellipsis expanded by Code, amended by ADDENDUM-n1 §7.6 and {a}", CNA,
                  False): 320,
                 ("NOT-DETECTABLE", f"ADDENDUM-n1 §7.6, amended by {a}", CNA, False): 256,
                 ("NOT-DETECTABLE", f4, ANSWERED, False): 64, ("NOT-DETECTABLE", f4, CNA, False): 576,
                 ("INDETERMINATE", "Code", None, False): 640},
         "7.3": {("SPECIFIC", "Code", ANSWERED, False): 64, ("SPECIFIC", "Code", CNA, False): 576,
                 ("SHARED", "Code", None, False): 640, ("NULL", "Code", ANSWERED, False): 64,
                 ("NULL", "Code", CNA, False): 576, ("INDETERMINATE", "Code", None, False): 640},
         "N4": {("PASS", "Code", None, False): 512, ("REVERSE", "Code", None, False): 512,
                ("DEAD", "Code", None, False): 512, ("INDETERMINATE", "Code", None, False): 512,
                ("INDETERMINATE", "Code", None, True): 512}}
    for k in t:
        t[k][(NOT_RUN, "Code", None, False)] = 1
    return t


def _bt_tuples(B: _Battery, verb: Mapping[str, str]) -> None:
    counts, sha, tal, fails = _bt_tuple_pass(verb)
    n_ev = len(evaluations())
    names = {"T1": "one sentence set: the four slots 7.1, 7.2, 7.3, N4, each a non-empty text, each state the "
                   "tuple's coordinate (NOT-RUN: all four)",
             "T2": "the set equals the oracle's (§5's verbatim cells read from the proposal file, ADDENDUM-n1 §7.6's "
                   "from the addendum's, the seat's forms of 2026-11-18 from the oracle's own copy)",
             "T3": "7.1 depends on (N1, G-READ-n valence +1, N4) only",
             "T4": "7.2 depends on (dose, G-READ-n valence d_eq, N4, the dose's movement certified against the "
                   "conditioned zone) only",
             "T5": "7.3 depends on (N2, G-READ-n span_reward at N2's decision f, N4) only",
             "T6": "N4's line depends on (N4, no read obtained) only",
             "T7": "(OPEN-Q3 as ruled) a §0.6 label exactly on the null outcomes (NOT-REPLICATED, "
                   "NOT-DETECTABLE, SPECIFIC, NULL); answered iff N4 PASS and the slot's G-READ-n cell PASS",
             "T8": "§5's sentences exactly in their cells (REPLICATED; DETECTABLE; NOT-DETECTABLE answered with no "
                   "movement certified, as ADDENDUM-n1 §7.6 and the seat's answers of 2026-11-18 §5.4 amend it) and "
                   "nowhere else",
             "T9": "no bracketed token outside the declared slots (BK's '[1.00, 1.19]' is text)"}
    for kk, nm in names.items():
        c = counts[kk]
        B.chk(f"tuples {kk}: {c[0]}/{c[1]} evaluations: {nm}", c[0] == c[1] == n_ev, fails.get(kk, ""),
              cover=[f"TUP-{kk}"])
    want = _bt_expected_tallies()
    B.chk("tuples T10: the forms tally as derived by hand -- 7.1 640 each (NOT-REPLICATED 64 answered / 576 CNA); 7.2 "
          "DETECTABLE and INDETERMINATE 640 each, NOT-DETECTABLE 64 / 320 / 256 in the three forms and 64 / 576 in the "
          "fourth; 7.3 640 each (SPECIFIC and NULL 64 / 576); N4 512 x 5; NOT-RUN 1",
          tal == want, {k: tal[k] for k in tal if tal[k] != want.get(k)}, cover=["TUP-T10"])
    n_t = len(tuple_space())
    B.chk(f"the outcome space (OPEN-Q4 as ruled: confirmed; PIN-n-35): {n_t} tuples (4 x 3 x 4 x 4 x 2 = 384, + "
          f"NOT-RUN), {n_ev} evaluations (384 x 4 G-READ inputs + 96 x 4 for N4's second INDETERMINATE form + 128 x 4 "
          f"+ 32 x 4 for the dose's movement certified against the conditioned zone, the seat's fourth form + NOT-RUN)",
          n_t == 385 and n_ev == 2561,
          (n_t, n_ev), cover=["TUP-COUNT"])
    _, sha2, _, _ = _bt_tuple_pass(verb)
    B.extra["outputs_sha256"] = sha
    B.chk("two passes over the 2,561 evaluations give byte-identical canonical JSON", sha == sha2, sha[:16],
          cover=["TUP-DETERMINISM"])


# --- reachability (OPEN-Q5) ------------------------------------------------------------------------------------------
_MENU = (Est(1.0, 0.9, 1.1), Est(0.3, 0.2, 0.4), Est(0.03, 0.01, 0.05), Est(0.2, -0.1, 0.5), Est(0.0, -0.05, 0.05),
         Est(-0.8, -0.9, -0.7))
_PATTERNS = ([{}] + [{"paused": {a: True}} for a in N1_ARMS] + [{"complete": {a: False}} for a in N1_ARMS])
_N2_PATTERNS = ({}, {"paused": {"N2-E": True}}, {"complete": {"N2-E": False}})


def map_reach(dmap: DoseMap, fourth: set | None = None) -> tuple[set, bool, bool]:
    """The (N1, dose, N2) triples the outcome layer produces over a grid of states on one dose map: six estimates at
    each distinct point of +1, −1, d_eq, d_20, the slope above or not above its floor, span_reward's effect at N2's
    decision f certified or not, and every completeness / pause pattern, two point by point (N1-P at −1 and N1-R at
    +1/2, which make N1 INDETERMINATE and leave N2 evaluated wherever its point is not +1/2: PIN-n-29 as amended);
    returns the set, whether dose INDETERMINATE <=> N1 INDETERMINATE held throughout, and whether nothing raised.
    ``fourth``, if given, collects (dose, its movement certified against the conditioned zone), the input of the seat's
    fourth form (PIN-n-35)."""
    r = dmap.resolved()
    pts = sorted({1.0, -1.0, r["d_eq"], r["d_20"]}, reverse=True)
    fd = dmap.n2_decision_f()
    pats = list(_PATTERNS) + [pointwise(dmap, {("N1-P", -1.0): ["incomplete"]}),
                              pointwise(dmap, {("N1-R", 0.5): ["incomplete"]})]
    seen, iff, clean = set(), True, True
    for combo in itertools.product(_MENU, repeat=len(pts)):
        V = dict(zip(pts, combo))
        for slope_ok, e_cert in itertools.product((True, False), (True, False)):
            for pat, pat2 in itertools.product(pats, _N2_PATTERNS):
                over = {"V": V, "floor_V": 0.3 if slope_ok else 1.5,
                        "E": {fd: Est(0.3, 0.2, 0.4) if e_cert else Est(0.01, -0.02, 0.04)}}
                st = _apply(literal_state(dmap, **over), pat, pat2)
                try:
                    o = outcomes(st)
                except (Exception, SystemExit):                     # noqa: BLE001
                    clean = False
                    continue
                n1, dose, n2 = o["N1"]["state"], o["dose"]["state"], o["N2"]["state"]
                iff &= (n1 == "INDETERMINATE") == (dose == "INDETERMINATE")
                seen.add((n1, dose, n2))
                if fourth is not None:
                    fourth.add((dose, bool(o["dose"].get("against"))))
    return seen, iff, clean


def map_reach_by_hand(shape: str) -> set:
    """Hand-derived reachable (N1, dose, N2) triples per coupling shape: which of N1's +1, dose's d_eq point and N2's
    decision point coincide (the question block's Q5 derivation,
    results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md, with N2's decision f as OPEN-Q7 is ruled). (a) none; (b)
    the cap binds and d_eq's point is not +1: N2 is decided at dose's point, so no DETECTABLE beside NULL; (c) d_20's
    point is +1 without the cap: N2 is decided at N1's +1, which REPLICATED and PARTIAL certify, so no NULL beside them;
    (d) d_eq's point is +1: all three meet there."""
    det = ("DETECTABLE", "NOT-DETECTABLE")
    dec = ("REPLICATED", "PARTIAL", "NOT-REPLICATED")
    if shape == "a":
        return {(a, d, c) for a in dec for d in det for c in N2_STATES} | \
               {("INDETERMINATE", "INDETERMINATE", c) for c in N2_STATES}
    if shape == "b":
        return ({(a, d, c) for a in dec for d in det for c in N2_STATES if (d, c) != ("DETECTABLE", "NULL")}
                | {("INDETERMINATE", "INDETERMINATE", c) for c in N2_STATES})
    if shape == "c":
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
    res, fourth = {}, {}
    for shape, dm in (("a", MAP_A), ("b", MAP_B), ("c", MAP_C), ("d", MAP_D)):
        fourth[shape] = set()
        seen, iff, clean = map_reach(dm, fourth[shape])
        res[shape] = (seen, iff, clean)
    B.chk("reachability: on every enumerated state of the four shapes, dose is INDETERMINATE iff N1 is (so 160 of the "
          "384 product tuples are unreachable on any map: 64 with N1 INDETERMINATE and dose decided, 96 the reverse)",
          all(v[1] for v in res.values()), cover=["REACH-DOSE-IFF-N1"])
    B.chk("reachability: the outcome layer raised on no enumerated state", all(v[2] for v in res.values()),
          cover=["REACH-NO-RAISE"])
    for shape, n in (("a", 28), ("b", 25), ("c", 24), ("d", 17)):
        seen = res[shape][0]
        want = map_reach_by_hand(shape)
        what = {"a": "all points distinct", "b": "the cap binds, N2 decided at d_eq's point (OPEN-Q7 as ruled)",
                "c": "d_20 merged into +1 without the cap, N2 decided there",
                "d": "d_20 and d_eq merged into +1"}[shape]
        B.chk(f"reachability, shape ({shape}) {what}: "
              f"{len(seen)} (N1, dose, N2) triples, the hand-derived {n}; x N4 (4) x G-READ-n at d_eq (2) = "
              f"{n * 8} reachable tuples + NOT-RUN", seen == want and len(want) == n,
              (sorted(seen - want)[:3], sorted(want - seen)[:3]), cover=[f"REACH-SHAPE-{shape}"])
    want4 = {("DETECTABLE", False), ("NOT-DETECTABLE", False), ("NOT-DETECTABLE", True), ("INDETERMINATE", False)}
    B.chk("reachability: on each of the four shapes the dose is NOT-DETECTABLE both with a movement at d_eq certified "
          "against the conditioned zone (the seat's fourth form) and without one, and no other dose carries one "
          "(PIN-n-35)", all(f == want4 for f in fourth.values()), {s: sorted(f) for s, f in fourth.items()},
          cover=["REACH-FOURTH"])
    st = literal_state()
    free = set()
    for told, e in ((Est(1.0, 0.8, 1.2, 98), 0.1), (Est(-1.0, -1.2, -0.8, 98), 0.1), (Est(0.05, -0.1, 0.2, 98), 0.1),
                    (Est(0.3, -0.1, 0.7, 98), 0.1), (Est(0.3, -0.1, 0.7, 98), float("nan"))):
        for pat in _PATTERNS + [{"paused": {"N2-E": True}}]:
            s_ = _apply(literal_state(told=told, e_sham=e), pat)
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
    xo = (1.0, 0.5, 2 / 3, 1 / 3, -1.0)
    yo = np.array([[1.1, 0.4, 0.7, 0.2, -0.9], [0.0, 0.0, 0.0, 0.0, 0.0], [2.0, 1.0, 4 / 3, 2 / 3, -2.0]])
    so = session_slopes_origin(xo, yo)
    want_o = [float(np.linalg.lstsq(np.array(xo)[:, None], row, rcond=None)[0][0]) for row in yo]
    closed_o = [sum(xi * yi for xi, yi in zip(xo, row)) / sum(xi * xi for xi in xo) for row in yo.tolist()]
    ok0, msg0 = _bt_raises(lambda: session_slopes_origin((1.0, 0.0, -1.0), np.array([[1.0, 0.0, -1.0]])), (AnlStop,))
    B.chk("the per-session slope of record is OLS through the origin over the nonzero points (OPEN-Q1 as ruled (b)): "
          "equal to a no-intercept least squares and to Σ d·Δm / Σ d²; an exact line of slope 2 gives 2, a flat "
          "session 0; the point d = 0 refused", all(abs(a - b) <= 1e-12 and abs(a - c) <= 1e-12
                                                   for a, b, c in zip(so, want_o, closed_o))
          and abs(so[2] - 2.0) <= 1e-12 and so[1] == 0.0 and ok0, (list(so), msg0), cover=["NUM-SLOPE-CLOSED-FORM"])
    x = (1.0, 0.5, 2 / 3, 1 / 3, 0.0, -1.0)
    y = np.array([[1.1, 0.4, 0.7, 0.2, 0.0, -0.9], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.0, 1.0, 4 / 3, 2 / 3, 0.0, -2.0]])
    s = session_slopes(x, y)
    want = [float(np.polyfit(np.array(x), row, 1)[0]) for row in y]
    xm = sum(x) / 6
    closed = [sum((xi - xm) * yi for xi, yi in zip(x, row)) / sum((xi - xm) ** 2 for xi in x) for row in y.tolist()]
    B.chk("the with-intercept slope reported beside is OLS with an intercept over the points with d = 0, Δm(0) = 0 "
          "(equal to polyfit and to the closed form; an exact line of slope 2 gives 2; a flat session 0)",
          all(abs(a - b) <= 1e-12 and abs(a - c) <= 1e-12 for a, b, c in zip(s, want, closed))
          and abs(s[2] - 2.0) <= 1e-12 and s[1] == 0.0, list(s), cover=["NUM-SLOPE-BESIDE"])
    xa = (1.0, 0.5, 0.0, -1.0)
    ya = np.array([[1.0, 0.6, 0.0, -0.6]])
    s_int = float(session_slopes(xa, ya)[0])
    s_org = float(session_slopes_origin((1.0, 0.5, -1.0), np.array([[1.0, 0.6, -0.6]]))[0])
    B.chk("on an asymmetric grid the two fits differ, so OPEN-Q1's ruling decides a figure: through the origin %.4f "
          "(the slope of record; by hand 1.9 / 2.25), with an intercept %.4f (beside)" % (s_org, s_int),
          abs(s_int - s_org) > 1e-3 and abs(s_org - 1.9 / 2.25) <= 1e-12, cover=["NUM-SLOPE-INTERCEPT"])
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
           "c": MAP_C.points() == (1.0, 0.5, 0.0, -1.0) and MAP_C.merged() == {"d_20": True, "d_eq": True}
           and (MAP_C.resolved()["d_20"], MAP_C.resolved()["d_eq"]) == (1.0, 0.5),
           "d": MAP_D.points() == (1.0, 0.5, 0.0, -1.0) and MAP_D.merged() == {"d_20": True, "d_eq": True},
           "merge-1/2": DoseMap(0.53125, 1.0).resolved()["d_eq"] == 0.5,
           "no-merge": DoseMap(0.5625, 1.0).resolved()["d_eq"] == 0.5625,
           "d_20-into-1/2": DoseMap(0.25, 0.5).resolved()["d_20"] == 0.5}
    B.chk("the dose map: shapes (a), (b), (c), (d) and the merge rule at clear distances (0.03125 merges, 0.0625 does "
          "not; d_20 = 2·0.25 = 0.5 is BK's +1/2; on (c) d_20 = 0.98 folds into +1 and d_eq = 0.49 into +1/2)",
          all(shp.values()), shp, cover=["NUM-DOSEMAP-SHAPES"])
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
          "positive float, and d_eq ≠ (0.10 * R_ell) / (rho * R) (PIN-n-14); it passes shapes (a) to (d) and an "
          "exact identity (R_ell 23.90625, R 25.5: d_eq 0.3125)", all(bad.values()) and not MAP_A.problems()
          and not MAP_B.problems() and not MAP_C.problems() and not MAP_D.problems() and not good.problems()
          and good.d_eq == 0.3125,
          {k: v[:1] for k, v in bad.items()}, cover=["NUM-DOSEMAP-REFUSE"])
    pa, pb, pc, pd = MAP_A.expected_points(), MAP_B.expected_points(), MAP_C.expected_points(), MAP_D.expected_points()
    f_pts = [{"label": "f0.10", "value": 0.10, "merged": []}, {"label": "f0.20", "value": 0.20, "merged": []}]
    want = {"a": [{"label": "+1", "value": 1.0, "merged": []}, {"label": "+1/2", "value": 0.5, "merged": []},
                  {"label": "+d_20", "value": 2 / 3, "merged": []}, {"label": "+d_eq", "value": 1 / 3, "merged": []},
                  {"label": "-1", "value": -1.0, "merged": []}] + f_pts,
            "b": [{"label": "+1", "value": 1.0, "merged": ["+d_20"]}, {"label": "+1/2", "value": 0.5, "merged": []},
                  {"label": "+d_eq", "value": 0.72, "merged": []}, {"label": "-1", "value": -1.0, "merged": []}] + f_pts,
            "c": [{"label": "+1", "value": 1.0, "merged": ["+d_20"]},
                  {"label": "+1/2", "value": 0.5, "merged": ["+d_eq"]}, {"label": "-1", "value": -1.0, "merged": []}]
            + f_pts,
            "d": [{"label": "+1", "value": 1.0, "merged": ["+d_20", "+d_eq"]},
                  {"label": "+1/2", "value": 0.5, "merged": []}, {"label": "-1", "value": -1.0, "merged": []}] + f_pts}
    both = DoseMap(0.29, 0.58)                      # d_20 0.58 and d_eq 0.29 both kept (no candidate within 0.05)
    kl = {"a": (MAP_A.kept_label("d_20"), MAP_A.kept_label("d_eq")), "b": (MAP_B.kept_label("d_20"),
                                                                          MAP_B.kept_label("d_eq")),
          "c": (MAP_C.kept_label("d_20"), MAP_C.kept_label("d_eq")), "d": (MAP_D.kept_label("d_20"),
                                                                          MAP_D.kept_label("d_eq"))}
    B.chk("the dose map lists its points as n-build's schema does (order, values, merged lists in fold order) for "
          "shapes (a) to (d); d_20 and d_eq are read under their keepers' labels", pa == want["a"] and pb == want["b"]
          and pc == want["c"] and pd == want["d"]
          and kl == {"a": ("+d_20", "+d_eq"), "b": ("+1", "+d_eq"), "c": ("+1", "+1/2"), "d": ("+1", "+1")}
          and [p["label"] for p in both.expected_points()][:4] == ["+1", "+1/2", "+d_20", "+d_eq"],
          {"a": pa == want["a"], "b": pb == want["b"], "c": pc == want["c"], "d": pd == want["d"], "labels": kl},
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
    n2a, n2b, n2c = MAP_A.n2_slope_points(), MAP_B.n2_slope_points(), MAP_C.n2_slope_points()
    B.chk("N2's slope points (OPEN-Q9 as ruled (a), through the origin): (d_eq, 2·d_eq) on BK's scale, its floor at "
          "(d_eq's point, d_20's point) -- equal on shape (a); 2·0.72 against +1 when the cap binds (shape b); both "
          "moved by a merge on shape (c) (0.49 to +1/2, 0.98 to +1)",
          n2a == ((1 / 3, 2 / 3), (1 / 3, 2 / 3)) and n2b == ((0.72, 1.44), (0.72, 1.0))
          and n2c == ((0.49, 2 * 0.49), (0.5, 1.0)), (n2a, n2b, n2c), cover=["NUM-N2-POINTS"])
    caps = {"a": (MAP_A.cap_binds(), MAP_A.n2_decision_f()), "b": (MAP_B.cap_binds(), MAP_B.n2_decision_f()),
            "c": (MAP_C.cap_binds(), MAP_C.n2_decision_f()), "d": (MAP_D.cap_binds(), MAP_D.n2_decision_f()),
            "edge": (DoseMap(0.5, 1.0).cap_binds(), DoseMap(0.5, 1.0).n2_decision_f())}
    B.chk("OPEN-Q7 as ruled: the cap binds iff 2·d_eq > 1 (shapes b and d; not at d_eq = 0.5 exactly, where 2·d_eq = "
          "1 and the norms match at f = 0.20), and N2 is then decided at f = 0.10, else at f = 0.20",
          caps == {"a": (False, F20), "b": (True, F10), "c": (False, F20), "d": (True, F10), "edge": (False, F20)},
          caps, cover=["NUM-CAP-DECISION-F"])
    n1p = {"a": MAP_A.n1p_points(), "b": MAP_B.n1p_points(), "c": MAP_C.n1p_points(), "d": MAP_D.n1p_points()}
    B.chk("OPEN-Q2 as ruled (c): N1-P's points are the kept points of +1, +d_20, +d_eq and −1, descending -- four on "
          "shape (a), three where d_20 folds into +1 (b), +1/2 where d_eq folds there (c), two where both fold into +1 "
          "(d)", n1p == {"a": (1.0, 2 / 3, 1 / 3, -1.0), "b": (1.0, 0.72, -1.0), "c": (1.0, 0.5, -1.0),
                         "d": (1.0, -1.0)}, n1p, cover=["NUM-N1P-POINTS"])


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
    pts = (-1.0, -0.5, 0.5, 1.0)               # BK's nonzero points: the slope of record, through the origin
    pts0 = (-1.0, -0.5, 0.0, 0.5, 1.0)         # with d = 0, Δm(0) = 0: the with-intercept figure beside
    vk = sorted(k for k in by if k[0] == "valenced")
    dm = np.array([[by[k][p] for p in pts] for k in vk])
    sl = session_slopes_origin(pts, dm)
    sl0 = session_slopes(pts0, np.array([[0.0 if p == 0.0 else by[k][p] for p in pts0] for k in vk]))
    means = {p: float(dm[:, i].mean()) for i, p in enumerate(pts)}
    sds = {p: sd0(dm[:, i]) for i, p in enumerate(pts) if p in (1.0, 0.5, -1.0)}
    rnd = {}
    for k in by:
        if k[0] == "random":
            rnd.setdefault(k[1], []).append(k)
    rs = {i: float(session_slopes_origin(pts, np.array([[by[k][p] for p in pts] for k in sorted(ks)])).mean())
          for i, ks in rnd.items()}
    rs0 = {i: float(session_slopes(pts0, np.array([[0.0 if p == 0.0 else by[k][p] for p in pts0]
                                                   for k in sorted(ks)])).mean()) for i, ks in rnd.items()}
    gap = max([float(np.max(np.abs(sl - sl0)))] + [abs(rs[i] - rs0[i]) for i in rs])
    B.extra["bk_fits_gap"] = gap
    B.chk("on BK's symmetric grid the two fits coincide (OPEN-Q1 as ruled: \"0.9164 either way\"): per session and per "
          "random direction, through the origin over the four nonzero points and with an intercept over the five, to "
          "1e-12 (largest gap %.2e)" % gap, gap <= 1e-12 and round(float(sl0.mean()), 4) == 0.9164,
          cover=["NUM-BK-FITS-COINCIDE"])
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
          "−0.2880 to +0.3641, so the floor through the origin on BK's four nonzero points is 0.3641", got == want,
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
#: Code's readings: PIN-n-7 to PIN-n-26 accepted by the seat (results/raw/2026-11-16_n-ganl_design-to-code_answers.md
#: §2); PIN-n-27, -28 and -31 accepted, PIN-n-29 and -32 amended, PIN-n-30 accepted with its sentences amended
#: (results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md §5); PIN-n-33 amended, PIN-n-34 to PIN-n-36
#: accepted (results/raw/2026-11-18_n-step4-smoke-pause_design-to-code_answers.md §3); PIN-n-37 declared since,
#: strikable by the seat until LOCK-n v1.0.
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
                "re-computation are kept, and so are finite reads whose re-computation is non-finite (no comparison, "
                "so not above TAU/4)",
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
    "PIN-n-23": "the exposure counts realised (§0.4's table; §8 step 15) are the campaign's reads on disk at d = −1, "
                "finite or not: N1-V's and N1-P's negative valenced, N1-R's negative random, each with its fresh "
                "re-computations beside; G-CAL-n's generations under negative steering are its own entry's",
    "PIN-n-24": "verdicts binds the stage report to the cells on disk (the identity, the plan, every cell by its shas "
                "and record count, each arm's planned, obtained and complete, the counters as n-build's runner "
                "counts them, the launch indices exactly 0..m−1, at most one pause standing and it the stage's last "
                "event, each pause against the reads, the cap's used time) and follows its end state: PAUSE refuses; "
                "PI-STOP, G-VER-STOP or CAP with no arm complete is NOT-RUN no-arm:<end>, an arm's full read set "
                "being the report's complete (every planned read produced, finite or not: a non-finite read makes "
                "its arm INDETERMINATE, PIN-n-20, never the unit NOT-RUN); any other end is analyzed, a pause "
                "standing (under PI-STOP only) making the arms in its scope INDETERMINATE; one outcome per unit",
    "PIN-n-25": "G-READ-n's artifact binds the campaign (its plan and identity shas, exactly the campaign's cells by "
                "both shas, the campaign's n package, exactly its capture layers, each result at a kept point with "
                "the labels merged into it); a status is read per (axis, point) by the point's value, an absent one "
                "NOT-COMPUTED; the dose sentence's AUC is the band median at d_eq's kept label",
    "PIN-n-26": "LOCK-n v1.0 says what it is in the whole line 'lock: LOCK-n v1.0' and states its direction of record "
                "as one whole line, 'direction of record: Route A' or 'direction of record: Route B'; verdicts "
                "checks the first and reads the route from the second (Code's form for the lock)",
    "PIN-n-27": "a certified movement against the conditioned zone (ADDENDUM-n1 §7.3) mirrors DETECTABLE with the mean "
                "below 0: the CI excludes 0 and G-LEAK-n certifies |mean| (at +1 for N1, at d_eq for dose)",
    "PIN-n-28": "N1's NOT-REPLICATED sentence names a certified movement against the conditioned zone in its failing "
                "list, as the sign's condition with MOVE_AGAINST beside it in parentheses (ADDENDUM-n1 §7.3 'with its "
                "sentence naming it'; the place is Code's form). The sign's name, 'the mean Δm at d = +1 above 0', is "
                "Code's form too (CONJUNCT_TEXT); the seat's clause repeats Δm(+1) and its CI, which the sentence "
                "states again after 'fails:'",
    "PIN-n-29": "as the seat amended it (results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md §5.2), N2's "
                "causes are read point by point: its certification reads N2-E at the decision f, and N1-V, N1-R's 24 "
                "directions and N1-P at the norm-matched point; N2 is INDETERMINATE iff one of those reads is missing "
                "or non-finite, or a pause stands on one of them; an incompleteness elsewhere in those arms (the "
                "seat's examples, N1-P at −1 and N1-R at +1/2; Code's note: +1/2 is N2's own point where d_20 folds "
                "into it, or d_eq does when the cap binds) makes N1 or dose INDETERMINATE by their own rules and "
                "leaves N2 evaluated; N1 stays per arm (n:134); the other f's figures beside are 'not computed' where "
                "their reads are missing. ADDENDUM-n1 §7.4's N2 clause is read as this (OPEN-Q6); the mechanics are "
                "PIN-n-36's",
    "PIN-n-30": "N2's certifications stay unsigned, as n §3's G-LEAK-n states them (|mean| against the ceiling, no CI "
                "condition), and the sign enters no N2 outcome: ADDENDUM-n1 §7.3's sign rule names DETECTABLE and "
                "PARTIAL only (accepted, the 2026-11-18 answers §5.3). So N1-V moving against the conditioned zone at "
                "the norm-matched point, span_reward not certified, gives SPECIFIC, and so does N1-V beyond the ceiling "
                "with a CI that includes 0; the sentences say which: in A.7's three forms each figure carries its CI "
                "and, where its mean is below 0, the words 'against the conditioned zone' (§5.3; PIN-n-34). When the "
                "cap binds that point is d_eq; there the dose sentence, if the dose question is evaluated, names the "
                "same movement in the seat's fourth NOT-DETECTABLE form (its CI excluding 0; §5.6) or as not certified "
                "(its CI including 0)",
    "PIN-n-31": "the capture arrays are bound by the per-layer row hashes their cells record (check_cell holds their "
                "names and layers to the band), which must equal the stage report's and G-READ-n's artifact's for the "
                "cell; the reader reads no array and needs none present -- they are G-READ-n's input, never in git "
                "(ADDENDUM-n1 §6.2), whose rows n-build's loader checks against those hashes before any fit (G-READ-n "
                "reads captures only through it: n-build's PIN, declared at its BUILD, 83a50a0) -- and refuses a file "
                "beside the cells that no cell names",
    "PIN-n-32": "as the seat amended it (the 2026-11-18 answers §5.4): where d_eq merges into another point (+1/2 or "
                "+1), the three NOT-DETECTABLE forms and the fourth print the figure as 'Δm(d_eq) = [x] nats [CI] "
                "(read at d = [point], the point d_eq merges into under §2.3)' (MERGE_NOTE), as DETECTABLE's [value] "
                "does (VALUE_MERGED); a sentence does not state a figure as d_eq's when the read was elsewhere. The "
                "merge stays in the dose outcome's point and in G-LEAK-n's table",
    "PIN-n-33": "as the seat amended it (results/raw/2026-11-18_n-step4-smoke-pause_design-to-code_answers.md §3.1), "
                "pauses are read point by point, as incompleteness is: a pause standing on one of the reads N2 uses "
                "-- N2-E at the decision f, and N1-V, N1-R's 24 directions and N1-P at the norm-matched point -- "
                "makes N2 INDETERMINATE; one standing on any other read (N1-V at −1, an N1-R cell elsewhere) leaves "
                "N2 decided, superseding the answers of 2026-11-16 §1.6's sentence; and, the half that stands, one "
                "on a guard's reads alone (N2-S's or N2-C's) leaves N2 decided, the guard's figures reported beside "
                "with its pause. The points a pause stands on are PIN-n-37's",
    "PIN-n-34": "§5.3's words go on every figure of A.7's three forms, SPECIFIC's span_reward figure and SHARED's "
                "valence figure too, which the seat's text does not name (it names SPECIFIC's valence figure and "
                "SHARED's and NULL's parentheticals, span_reward's included): each figure carries its CI ([CIE], "
                "[CIV]; SHARED's span_reward figure had it already) and, where its mean is below 0, ', against the "
                "conditioned zone' ([zoneE], [zoneV]), certified or not, closing its parenthetical (after 'against "
                "[c]' where it has one, so that span_reward's reads '... against [c], against the conditioned zone' in "
                "SPECIFIC and SHARED; SHARED's valence figure, outside any parenthesis, ends the sentence)",
    "PIN-n-35": "the seat's fourth NOT-DETECTABLE form (F11 as ruled, the 2026-11-18 answers §5.6) is chosen by a "
                "fourth input that is not a coordinate (OPEN-Q4): the dose's movement at d_eq certified against the "
                "conditioned zone (PIN-n-27), which only a NOT-DETECTABLE dose carries; the tuple pass runs each "
                "NOT-DETECTABLE tuple under it, 640 evaluations more, 2,561 in all; the label by §0.6 as the others",
    "PIN-n-36": "point by point (PIN-n-29 as amended), the reader records why each steered arm's reads at each point "
                "are not usable -- a planned read absent ('incomplete'), a read non-finite ('nonfinite'), a session's "
                "shadow not usable ('shadow': PIN-n-20 per point, N1-V's d = 0 reads a cause of its other points), the "
                "point left with no session in the TAU/4 row ('tau4-emptied') -- and computes each point's statistics "
                "where its reads are usable. The per-arm statistics -- N1-V's slopes, N1-R's floor, N2's floor (N1-R "
                "at d_eq's and d_20's points) and the N2 arms' slopes -- stay on a complete arm only; a slope with no "
                "common session in the TAU/4 row marks its arm 'tau4-emptied' and not its points, so that row decides "
                "N2 where 977b78b had it INDETERMINATE. G-LEAK-n's table reads each row the same way, so that it "
                "agrees with N2. N2's causes name a point by its record label ('incomplete:N1-P@+d_20', "
                "'shadow:N2-E@f0.20') and a pause by its arm ('pause:N1-V'). An INDETERMINATE N2 reports no beside, as "
                "at 977b78b: §5.2's 'not computed where its reads are missing' is read for a decided N2's beside",
    "PIN-n-37": "for N2's rule (PIN-n-33 as amended), the points a standing pause stands on (paused_points), each "
                "within its scope's arms (n-build's schema): its read, where it has one (a rendering pause's, not on "
                "disk, by its id); its binomial batch's trials, the reads carrying a re-computation launched from the "
                "batch's first_launch_index to its last (the runner's trials, the dose rule's and the keyed "
                "sample's); and, where one of those reads is a session's shadow (N1-V's d = 0 read), every read of "
                "that session, each read against it. That last is Code's extension, capped by the scope: the "
                "runner's SCOPE applies its shadow clause to the read that fired alone (relayed to n-build), and "
                "PIN-n-36's 'shadow' cause reads a shadow the same way. For a batch the seat may prefer every read "
                "launched in its range, or every read of its scope's arms (the per-arm reading). Under the runner's "
                "launch order (arm-major, the 160 shadows first: its ORDER pin) and n §2.1's cadence of 160 reads, a "
                "batch from the stage's start holds every shadow launched, and so stands on every read of its "
                "scope's arms, as the per-arm reading would; a later batch holds none, and its trials, the keyed "
                "sample's among them, reach nearly every point its range reads, as the first alternative would. The "
                "reader binds a standing batch to the records before reading it (the runner's batch: its ends, its n "
                "and k, its scope holding its trials' arms) and holds every pause's read to the plan. N1's and N4's "
                "pauses stay per arm, as their incompleteness is (n:134; §5 N4, OPEN-Q6 as ruled), and so does a "
                "guard's beside flag: PIN-n-24's 'a pause standing (under PI-STOP only) making the arms in its scope "
                "INDETERMINATE' is read as those per-arm rules, and for N2 through the points read here. The other "
                "f's figures beside a decided N2 stay computed and name the arms whose reads there a pause stands on "
                "('paused'), as the guards' carry theirs",
}
#: The seat's rulings on the question block (results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md, Q1-Q9), in
#: results/raw/2026-11-16_n-ganl_design-to-code_answers.md and ADDENDUM-n1 v0.1, with the amendments of the answers of
#: 2026-11-18 (results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md §5) and of its second sitting
#: (results/raw/2026-11-18_n-step4-smoke-pause_design-to-code_answers.md §3), as the code carries them.
OPEN = {
    "OPEN-Q1": "ruled (b), ADDENDUM-n1 §7.1: per session, OLS through the origin over the arm's nonzero dose points; "
               "the floor refit the same way; the with-intercept slope reported beside, descriptive",
    "OPEN-Q2": "ruled (c), ADDENDUM-n1 §5.2: N1-P reads +1, +d_20, +d_eq and −1 under the merge, so P(d) exists at "
               "every point a certification is made; the ceiling max(L, P) unchanged",
    "OPEN-Q3": "ruled (a), ADDENDUM-n1 §7.2: answered iff N4 PASS and G-READ-n PASS for the axis and dose (N1 at +1, "
               "dose at d_eq, N2 for span_reward at its decision f); the cell (G-READ-n PASS, N4 not PASS) has its "
               "own sentence (A.6, as §7.6 and the 2026-11-18 answers §5.4 amend it), unless the movement at d_eq is "
               "certified against the conditioned zone, which takes the fourth form (§5.6), its label in that cell "
               "'concluded, not answered (N4 [n4])' (the second sitting's §3.2)",
    "OPEN-Q4": "confirmed: three inputs that change a sentence are not coordinates: G-READ-n (valence, +1), G-READ-n "
               "(span_reward, at N2's decision f), N4's no-read INDETERMINATE; 385 tuples, 1,921 evaluations. The "
               "seat's fourth NOT-DETECTABLE form (the 2026-11-18 answers §5.6) adds a fourth input, the dose's movement "
               "certified against the conditioned zone: 2,561 evaluations (PIN-n-35)",
    "OPEN-Q5": "confirmed: the sentence functions are total; reachability reported per merge shape; no tuple refused",
    "OPEN-Q6": "ruled (a), amended for N1-P, ADDENDUM-n1 §7.4: N1 INDETERMINATE when N1-V is incomplete; dose when N1 "
               "is, or N1-V's, N1-R's or N1-P's reads at d_eq are incomplete (the d_20 figure beside then reported as "
               "not computed); N2 when N2-E, N1-V, N1-R or N1-P at the norm-matched point is incomplete (read point "
               "by point, the 2026-11-18 answers §5.2: PIN-n-29 as amended; the other f's figures beside reported as "
               "not computed where their reads are missing); N4, no read obtained, when a pause stands on its reads",
    "OPEN-Q7": "ruled, ADDENDUM-n1 §5.3: when the cap binds (2·d_eq > 1), N2 is decided at f = 0.10 against N1-V at "
               "d_eq, with f = 0.20 beside against N1-V at d = 1 and the ratio 2·d_eq; otherwise at f = 0.20, f = 0.10 "
               "beside",
    "OPEN-Q8": "ruled: Appendix A adopted with the amendments of ADDENDUM-n1 §7.6 (the movement clause in the three "
               "NOT-DETECTABLE forms, the sign clause, the labels by §0.6, 'at f = [f]') and of the 2026-11-18 answers "
               "§5.3, §5.4 and §5.6 (N2's figures with their CIs and the zone's words; the merge note in the "
               "NOT-DETECTABLE forms; the fourth NOT-DETECTABLE form), and of its second sitting's §3.2 (the fourth "
               "form's label in the sentence, in three fills)",
    "OPEN-Q9": "ruled (a), through the origin, ADDENDUM-n1 §7.5: N2's slope over (d_eq, 2·d_eq), its floor on the "
               "random reads at d_eq's and d_20's kept points, the mismatch printed beside where they differ",
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


def _bt_structure(B: _Battery, ptext: bytes, hook: _Hook, atext: bytes) -> None:
    import ast
    B.chk("proposal: PROPOSAL-n v0.2's sha256 is the pinned 30a3d0f5...04f4", hashlib.sha256(ptext).hexdigest()
          == PROPOSAL_SHA256, hashlib.sha256(ptext).hexdigest()[:16], cover=["STR-PROPOSAL-SHA"])
    B.chk("addendum: ADDENDUM-n1 v0.1's sha256 is the pinned e979f8f2...5e03", hashlib.sha256(atext).hexdigest()
          == ADDENDUM_SHA256, hashlib.sha256(atext).hexdigest()[:16], cover=["STR-ADDENDUM-SHA"])
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
# 10. The reader (n-read-v1 / n-cell-v1, valence_core/n/schema.py at d791bd9, sha256 0ea39600...0db6: the schema's
#     follow-up commit, ADDENDUM-n1 §5-§6 -- keepers, the capture band per layer, kfold10, the cap's loads)
# =====================================================================================================================
# The schema module is imported lazily, on the verdicts path and in the battery only (LAZY_SCHEMA), and bound by its
# sha256 in every output; its checks run on every cell the analyzer loads ("the checks both sides run"). What the
# schema leaves to the analyzer ("CROSS-RECORD PROPERTIES ... The analyzer re-checks what it uses") is checked here:
# each steered read's shadow exists with its ids_sha; a session's cues and present order agree across its reads; N4-T
# and N4-Ts carry the same schedule_zone per session, 80 S and 80 U (n §2.4).
SCHEMA_REL = "valence_core/n/schema.py"
SCHEMA_SHA256 = "0ea39600919aceb43ee25962314e4239f609ef8da7536b12063372dfdfb30db6"     # d791bd9
LAZY_SCHEMA = "valence_core.n.schema"
N_SESSIONS, N_FLOOR = 160, 40
#: n §2.4's table, independently of the schema's ARM_CELLS (the reader cross-checks the two): arm -> (directions,
#: dose labels before §2.3's merges, sessions).
PLAN_TABLE = {
    "N1-V": ((("valence",), ("+1", "+1/2", "+d_20", "+d_eq", "-1")), (("none",), ("0",))),
    "N1-R": ((tuple(f"rand_{i:02d}" for i in range(N_RANDOM)), ("+1", "+1/2", "+d_20", "+d_eq", "-1")),),
    "N1-P": ((("valence",), ("+1", "+d_20", "+d_eq", "-1")),),        # ADDENDUM-n1 §5.2 (OPEN-Q2 as ruled)
    "N2-E": ((("span_reward",), ("f0.10", "f0.20")),),
    "N2-S": ((("span_sentiment",), ("f0.10", "f0.20")),),
    "N2-C": ((("span_character",), ("f0.10", "f0.20")),),
    "N4-T": ((("none",), ("0",)),),
    "N4-Ts": ((("none",), ("0",)),),
}
GUARD_DIRS = {"N2-E": "span_reward", "N2-S": "span_sentiment", "N2-C": "span_character"}


def schema_module():
    """The record schema, imported lazily; refused unless its bytes are the pinned ones (d791bd9)."""
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


def plan_cells(dmap: DoseMap) -> list[tuple[str, str, str]]:
    """The declared cells (arm, direction, record label), in PLAN_TABLE's order: each arm reads the keeper of every
    label it lists, in its listed order, a keeper read once (ADDENDUM-n1 §5.1: a merged point is read once, under the
    kept label; §5.2: N1-P's +d_20 and +d_eq at their keepers, +1/2 where d_20 or d_eq folds there). Derived from the
    analyzer's own dose map, not the schema's."""
    keeper = {"+1": "+1", "+1/2": "+1/2", "-1": "-1", "0": "0", "f0.10": "f0.10", "f0.20": "f0.20",
              "+d_20": dmap.kept_label("d_20"), "+d_eq": dmap.kept_label("d_eq")}
    out = []
    for arm, rows in PLAN_TABLE.items():
        for dirs, labels in rows:
            for d in dirs:
                labs: list[str] = []
                for lab in labels:
                    if keeper[lab] not in labs:
                        labs.append(keeper[lab])
                out.extend((arm, d, lab) for lab in labs)
    return out


def own_plan(dmap: DoseMap) -> list[str]:
    """§2.4's declared read set, as ADDENDUM-n1 §5 amends it, derived without the schema (the reader asserts it equals
    the schema's read_plan): N1-R on the 40 floor sessions, every other arm on all 160, each cell of plan_cells."""
    return sorted(f"{arm}|{d}|{lab}|{session_key(r)}" for arm, d, lab in plan_cells(dmap) for r in runs_of(arm))


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
    cross-record checks the schema leaves to the analyzer. Refuses (exit 2) on a cell that fails a check, a file beside
    the cells that is neither a cell nor one of their capture arrays by name, an identity that differs between cells, a
    dose map whose points the analyzer derives differently, a plan the analyzer derives differently, a read outside the
    plan or a broken cross-record property. The capture arrays are bound by the per-layer row hashes their cells
    record, and are not read (PIN-n-31): an absent array is no refusal."""
    sm = sm or schema_module()
    cdir = Path(cdir)
    if not cdir.is_dir():
        raise AnlRefusal(f"REFUSED: no campaign directory {cdir.name!r}")
    names = sorted(p.name for p in cdir.iterdir())
    jsons = [n for n in names if n.endswith(".json")]
    cells, ident0, records = {}, None, {}
    captures: set[str] = set()
    for n in jsons:
        try:
            data = (cdir / n).read_bytes()
            cell = json.loads(data.decode("utf-8"))
            sm.check_cell(cell, where=n)
        except (OSError, ValueError) as e:
            raise AnlRefusal(f"REFUSED: cell {n}: {_err_where(e)}")
        if n != sm.cell_filename(cell["arm"], cell["direction_id"], cell["dose_label"]):
            raise AnlRefusal(f"REFUSED: cell {n} is named for another cell")
        # PIN-n-31: check_cell holds capture_files to capture_filename(n, layer) and capture_sha256 to the identity's
        # capture layers; the arrays are G-READ-n's input, never in git (ADDENDUM-n1 §6.2), bound here by those hashes
        captures |= set(cell["capture_files"].values())
        cap = dict(cell["capture_sha256"])
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
    extra = sorted(set(names) - set(jsons) - captures)
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
    plan = sm.read_plan(ident0)
    if plan != own_plan(dmap):
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
    Called only on a usable point with usable shadows (build_state's guard, PIN-n-36): a missing or non-finite read
    here STOPs."""
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
                drop: Callable[[str], bool] | None = None,
                paused_at: Mapping[tuple[str, Any], bool] | None = None) -> tuple[State, dict]:
    """The outcome layer's State from the campaign (n §4), and the figures beside it. ``paused``: per arm, whether an
    unadjudicated pause stands on its reads (the stage report's); ``paused_at``: the points they stand on (PIN-n-37:
    paused_points), None reading ``paused`` at every point of a paused arm. ``drop``: the TAU/4 sensitivity row's read
    filter (PIN-n-16), None for the primary (ungated, n §2.1).

    Read point by point (PIN-n-29 as amended; PIN-n-36): a steered arm's reads at one point are usable iff every
    planned read there is present and finite and the shadows (N1-V's d = 0 reads) of every session it reads are too
    (PIN-n-20 per point: N1-R's 40 floor sessions, the others' 160); State.at records why not, per point, and each
    point's statistics (V, L, P, N2's E, S, C) are computed where its reads are usable. An arm is complete only if every
    point is (`shadow` when only its shadows fail it); the per-arm statistics -- N1-V's slope, N1-R's floor and N2's
    floor, the N2 arms' slopes -- are computed on a complete arm only. In the TAU/4 row a point left with no session is
    marked `tau4-emptied`, and its arm with it, and a slope with no common session marks its arm alone, its points
    staying usable (never a STOP; PIN-n-36); each statistic's matrix is drawn from its arm's stream
    for that statistic's session count (PIN-n-12). Slopes are fitted through the origin over the nonzero points
    (OPEN-Q1 and OPEN-Q9 as ruled), N1-V's with-intercept slope beside, descriptive; N1-P's P(d) at each point it
    reads."""
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
               unusable=unusable, paused_at=None if paused_at is None else dict(paused_at))
    fkey = {"f0.10": F10, "f0.20": F20}
    for a in STEERED_ARMS:                                     # PIN-n-29 as amended, PIN-n-36: why, point by point
        by_label: dict[str, list[str]] = {}
        for rid in camp.planned[a]:
            by_label.setdefault(rid.split("|")[2], []).append(rid)
        sh = [] if shadows_ok(a) else ["shadow"]
        for lab, ids in by_label.items():
            if a == "N1-V" and lab == "0":
                continue                                       # the shadows themselves: a cause of the other points
            why = (["incomplete"] if any(r not in camp.present[a] for r in ids) else []) \
                + (["nonfinite"] if any(r in camp.present[a] and not camp.records[r]["finite"] for r in ids) else [])
            st.at[(a, fkey.get(lab, lv.get(lab)))] = why + sh
    fig: dict = {"n": {}, "sd0": {}, "dir_means": {}, "dir_slopes": {}, "P_signed": {}, "slopes_N2": {},
                 "floors_N2": {}}

    def dm(arm, direction, label):
        d = delta_m(camp, arm, direction, label)
        if drop is None:
            return d
        return {run: x for run, x in d.items() if not (drop(f"N1-V|none|0|{session_key(run)}")
                                                        or drop(f"{arm}|{direction}|{label}|{session_key(run)}"))}

    def arm_emptied(arm) -> None:
        st.complete[arm] = False
        st.unusable[arm] = "tau4-emptied"

    def emptied(arm, *vecs) -> bool:
        """The TAU/4 row, for an arm read at one point only (N4's): no session left marks it `tau4-emptied`."""
        if any(len(v) == 0 for v in vecs):
            arm_emptied(arm)
            return True
        return False

    def usable_at(arm, key) -> bool:
        return not st.at[(arm, key)]

    def emptied_at(arm, key, *vecs) -> bool:
        """The TAU/4 row: a point left with no session is `tau4-emptied`, and so is its arm (never a STOP)."""
        if any(len(v) == 0 for v in vecs):
            st.at[(arm, key)] = ["tau4-emptied"]
            arm_emptied(arm)
            return True
        return False

    def slope_est(arm, pts, vecs, fit=session_slopes_origin):
        common = sorted(set.intersection(*[set(v) for v in vecs]))
        if not common:
            return None, 0, None
        Y = np.array([[vv[r] for vv in vecs] for r in common])
        sl = fit(pts, Y)
        return mean_est(sl, boot_index(arm, len(common))), len(common), sl

    nz_pts = [pt for pt in v_pts if pt != 0.0]                            # the nonzero points, the fits' (OPEN-Q1)
    lab_of = {p: lab for lab, p in labels_v.items()}
    vecs = {}
    for lab, pt in labels_v.items():
        if usable_at("N1-V", pt):
            v_ = dm("N1-V", "valence", lab)
            if not emptied_at("N1-V", pt, v_):
                vecs[pt] = v_
                st.V[pt] = mean_est(_vec(v_), boot_index("N1-V", len(v_)))
                fig["n"][("N1-V", lab)] = len(v_)
                fig["sd0"][("N1-V", lab)] = sd0(_vec(v_))
    if st.complete["N1-V"]:
        est, n_c, sl = slope_est("N1-V", nz_pts, [vecs[pt] for pt in nz_pts])
        if est is None:
            arm_emptied("N1-V")
        else:
            st.slope_V, fig["slope_V_n"], fig["slope_V_sd0"] = est, n_c, sd0(sl)
            zero = {r: 0.0 for r in range(N_SESSIONS)}                    # beside, descriptive: with an intercept
            est_i, _, _ = slope_est("N1-V", v_pts, [zero if pt == 0.0 else vecs[pt] for pt in v_pts],
                                    fit=session_slopes)
            fig["slope_V_with_intercept"] = dict(est_i.as_json(), descriptive=True)       # OPEN-Q1 as ruled
    dirs = tuple(f"rand_{i:02d}" for i in range(N_RANDOM))
    dv = {}
    for lab, pt in labels_v.items():
        if usable_at("N1-R", pt):
            per = {d_: dm("N1-R", d_, lab) for d_ in dirs}
            if not emptied_at("N1-R", pt, *per.values()):
                means = {d_: float(_vec(per[d_]).mean()) for d_ in dirs}
                for d_ in dirs:
                    dv[(d_, lab)] = per[d_]
                    fig["dir_means"][(d_, lab)] = means[d_]
                st.L[pt] = max(abs(x) for x in means.values())
    if st.complete["N1-R"]:
        slopes = {}
        for d_ in dirs:
            est, n_c, sl = slope_est("N1-R", nz_pts, [dv[(d_, lab_of[pt])] for pt in nz_pts])
            slopes[d_] = float(sl.mean()) if sl is not None else float("nan")
            fig["dir_slopes"][d_] = slopes[d_] if sl is not None else None        # no NaN in a figure
        if any(math.isnan(x) for x in slopes.values()):
            arm_emptied("N1-R")
        else:
            st.floor_V = max(abs(x) for x in slopes.values())
            fig["floor_dir"] = max(slopes, key=lambda k: (abs(slopes[k]), k))
            # OPEN-Q9 as ruled: N2's floor on the random reads at d_eq's and d_20's kept points, through the origin
            n2_pts, (p10, p20) = dmap.n2_slope_points()
            n2_slopes = {}
            for d_ in dirs:
                _, _, sl = slope_est("N1-R", (p10, p20), [dv[(d_, lab_of[p10])], dv[(d_, lab_of[p20])]])
                n2_slopes[d_] = float(sl.mean())
            fig["floors_N2"] = {"points": [p10, p20], "floor": max(abs(x) for x in n2_slopes.values()),
                                "n2_points": list(n2_pts), "mismatch": [p10, p20] != list(n2_pts)}
    # OPEN-Q2 as ruled (ADDENDUM-n1 §5.2): P(d) at each point N1-P reads, as the plan has them
    for lab in sorted({rid.split("|")[2] for rid in camp.planned["N1-P"]}, key=lambda lab: -lv[lab]):
        pt = lv[lab]
        if usable_at("N1-P", pt):
            v_ = dm("N1-P", "valence", lab)
            if not emptied_at("N1-P", pt, v_):
                e = mean_est(_vec(v_), boot_index("N1-P", len(v_)))
                st.P[pt] = abs(e.mean)
                fig["P_signed"][lab] = e.as_json()
                fig["n"][("N1-P", lab)] = len(v_)
    for arm, d_ in GUARD_DIRS.items():
        tgt = {"N2-E": st.E, "N2-S": st.S, "N2-C": st.C}[arm]
        fv = {}
        for lab, f in (("f0.10", F10), ("f0.20", F20)):
            if usable_at(arm, f):
                v_ = dm(arm, d_, lab)
                if not emptied_at(arm, f, v_):
                    fv[f] = v_
                    tgt[f] = mean_est(_vec(v_), boot_index(arm, len(v_)))
                    fig["n"][(arm, lab)] = len(v_)
                    fig["sd0"][(arm, lab)] = sd0(_vec(v_))
        if st.complete[arm]:
            pts, fl_pts = dmap.n2_slope_points()                          # OPEN-Q9 as ruled: through the origin
            est, n_c, _ = slope_est(arm, pts, [fv[F10], fv[F20]])
            fig["slopes_N2"][arm] = None if est is None else dict(est.as_json(), n=n_c, points=list(pts),
                                                                   floor_points=list(fl_pts),
                                                                   mismatch=list(pts) != list(fl_pts))
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
# to three; d_eq's value to four (Code's form, adopted with Appendix A: OPEN-Q8 as ruled).


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
    beside it, since [x] and [CI] are read there (VALUE_MERGED, Code's form, adopted with Appendix A: OPEN-Q8 as
    ruled)."""
    if point == dm.d_eq:
        return _u(dm.d_eq)
    lab = BK_LABEL.get(point)
    return VALUE_MERGED.format(value=_u(dm.d_eq), point=lab if lab is not None else _u(point))


def merge_text(dm: DoseMap, point: float) -> str:
    """The NOT-DETECTABLE forms' [merge] (PIN-n-32 as amended; the seat's answers of 2026-11-18 §5.4): nothing at
    d_eq's own point; where §2.3's merge moved d_eq onto another point, MERGE_NOTE naming that point as value_text does,
    since the figure printed as Δm(d_eq) is read there."""
    if point == dm.d_eq:
        return ""
    lab = BK_LABEL.get(point)
    return MERGE_NOTE.replace("[point]", lab if lab is not None else _u(point))


def code_forms() -> dict[str, str]:
    """Every sentence form the module writes beyond §5's verbatim cells, by name: Code's (the question block's Appendix
    A with VALUE_MERGED, adopted with the seat's amendments: OPEN-Q8 as ruled), ADDENDUM-n1 §7.6's, with the clause of
    §5 the addendum replaces, and the seat's of 2026-11-18 §5 and of its second sitting §3.2 (RULING_FORMS: its fourth
    form's two branches, each ending in its label, the label's fill for N4, the merge note and the zone's words); the
    battery pins them by digest (CODE_FORMS_SHA256), so that none changes unseen."""
    f = {"C_N1_PARTIAL": C_N1_PARTIAL, "C_N1_NOT_REPLICATED": C_N1_NOT_REPLICATED, "C_N1_INDET": C_N1_INDET,
         "C_DOSE_ND_NOT_READABLE": C_DOSE_ND_NOT_READABLE, "C_DOSE_INDET": C_DOSE_INDET, "C_NOT_RUN": C_NOT_RUN,
         "VALUE_MERGED": VALUE_MERGED, "OLD_MOVE": OLD_MOVE, "B_STRUCK": B_STRUCK}
    for fam, d in (("C_N2", C_N2), ("C_N4", C_N4), ("CONJUNCT_TEXT", CONJUNCT_TEXT),
                   ("NOT_RUN_CAUSES", NOT_RUN_CAUSES), ("ROUTE_TEXT", ROUTE_TEXT), ("ADDENDUM", ADDENDUM_FORMS),
                   ("RULING", RULING_FORMS)):
        f |= {f"{fam}[{k}]": v for k, v in d.items()}
    return f


#: sha256 of _canon(code_forms()) -- a changed form fails the battery until this pin is moved, in the open
CODE_FORMS_SHA256 = "41d0d6544f5d12beef58d5e157bab30f10b1f53223f6f5c488fb72365abeb1da"


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
                        "[c]": _u(n1["ceiling"]), "[x−]": _n(vm1.mean), "[CI−]": _ci(vm1),
                        "[failing]": failing_text(n1["failing"], against=n1["against"])})
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
            # PIN-n-32 as amended (§5.4): where d_eq merges into another point, DETECTABLE's [value] (VALUE_MERGED)
            # and the NOT-DETECTABLE forms' [merge] (MERGE_NOTE, after the figure printed as Δm(d_eq)) name the point
            sub.update({"[value]": value_text(st.dmap, d["point"]), MERGE_SLOT: merge_text(st.dmap, d["point"]),
                        "[x]": _n(v.mean), "[CI]": _ci(v), "[c]": _u(d["ceiling"]),
                        "[a]": "not computed" if a is None else f"{a:.3f}"})
    elif q == "N2":
        n2 = o["N2"]
        if n2["state"] == "INDETERMINATE":
            sub["[causes]"] = ", ".join(n2["causes"])
        else:
            e, v = st.E[n2["f"]], st.V[n2["point"]]
            # PIN-n-30 as accepted, PIN-n-34: each figure with its CI, the zone's words where its mean is below 0
            sub.update({"[xE]": _n(e.mean), "[CIE]": _ci(e), "[c]": _u(n2["ceiling"]), "[f]": F_TEXT[n2["f"]],
                        "[xV]": _n(v.mean), "[CIV]": _ci(v), ZONE_E: ZONE_WORDS if e.mean < 0.0 else "",
                        ZONE_V: ZONE_WORDS if v.mean < 0.0 else ""})
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
    tuple pass asserts), with its N1 failing conjuncts, its INDETERMINATE causes and every figure filled; a movement at
    d_eq certified against the conditioned zone selects the seat's fourth NOT-DETECTABLE form (F11 as ruled)."""
    gr = o["gread"]
    t = o["tuple"]
    base = sentence_set(t, gr1="PASS" if gr["+1"] == "PASS" else "FAIL", gre="PASS" if gr["E"] == "PASS" else "FAIL",
                        n4_no_read=bool(o["N4"].get("no_read")) and o["N4"]["state"] == "INDETERMINATE",
                        dose_against=bool(o["dose"].get("against")))
    return {k: fill(v, o, st, route=route, auc=auc) for k, v in base.items()}


# =====================================================================================================================
# 13. Counters (rule 23: over every read, the non-finite included) and secondaries (n §4; rule 28(a); no claim)
# =====================================================================================================================
COUNTER_NAMES = ("fidelity re-computations", "fidelity exceedances at TAU", "fidelity exceedances at TAU/4",
                 "non-finite re-computations", "non-finite margins", "label mass below .20", "identity bound exceeded")


def counters(camp: Campaign) -> dict:
    """n §4's counters by arm and dose label, over every read in the campaign (rule 23); the rendering-mismatch
    counter is the stage report's (check_record: "a rendering mismatch is never a record (a pause during a stage; a
    G-VER-STOP at G-VER)")."""
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
    drops its session at every point through build_state); a read with no re-computation is kept, and so is a finite
    read whose re-computation is non-finite (its exceeds_tau4 null: no comparison, so not above TAU/4; Code's
    reading, flagged at the verdicts BUILD)."""
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
    out["b_free_text"] = B_STRUCK
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
                       first_is_s: Callable[[int], bool] = lambda r: r % 3 == 0,
                       lock_sha256: str | None = None, capture_cells: Sequence[tuple] = (),
                       sampled: Sequence[str] = ()) -> Path:
    """Write a synthetic campaign (every cell of the plan over the example identity's dose map) to ``root``: shadows
    m0(run) = 0.1 + 0.01 (run % 7); each steered read m0 + delta(arm, direction, label, run); N4-T's margin toward its
    told zone told(run, zone) and N4-Ts's toward its referent zone sham(run, zone), the zone S for even runs;
    ``omit``: (arm, direction, label) cells left out; ``nonfinite``: read_ids written non-finite; ``fresh_shift``:
    read_id -> fresh shift; ``first_is_s``: a run's present order (S first); ``lock_sha256``: the identity's lock;
    ``capture_cells``: the (arm, direction, label) cells whose capture arrays are written (empty, by name only: the
    reader never reads one, PIN-n-31); ``sampled``: read_ids written with the campaign's keyed-sample re-computation
    (at a point the dose rule does not re-compute). Each cell records its per-layer row hashes as sha256 of
    'name|layer'."""
    root.mkdir(parents=True, exist_ok=True)
    ident = sm.example_identity(R_ell=R_ell)
    if lock_sha256 is not None:
        ident = dict(ident, lock_sha256=lock_sha256)
    launch = 0
    for arm, d_, lab in plan_cells(dose_map_of(ident)):
        if (arm, d_, lab) in omit:
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
                                    fresh_shift=fresh_shift.get(rid, 0.0),
                                    fidelity="sample" if rid in sampled else "auto")
            launch += 1
            recs.append(rec)
        name = sm.cell_filename(arm, d_, lab)
        band = ident["capture_layers"]
        cell = {"schema": sm.CELL_SCHEMA, "stage_identity": ident, "arm": arm, "direction_id": d_,
                "dose_label": lab, "records": recs,
                "capture_files": {str(x): sm.capture_filename(name, x) for x in band}, "capture_rows": len(recs),
                "capture_sha256": {str(x): hashlib.sha256(f"{name}|{x}".encode()).hexdigest() for x in band}}
        if mutate is not None:
            mutate(cell)
        (root / name).write_text(json.dumps(cell), encoding="utf-8")
        if (arm, d_, lab) in capture_cells:
            for x in band:
                (root / sm.capture_filename(name, x)).write_bytes(b"")
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
    offset of mean +0.045 (so the fit through the origin and the with-intercept fit, whose d = 0 point is not offset,
    differ); rand_05 has a negative slope and an offset
    (−0.8·d + 0.05; L = its |mean|, the floor its |slope|); N1-P is −0.9 at +1 (P(+1) above L(+1)), +0.3 at +d_eq
    (P(d_eq) above L(d_eq) = 0.2, so the dose ceiling is P's) and +0.2 at +d_20 and −1;
    N2-E is +1.0 plus the offset at f = 0.10 and +0.1 plus twice the offset at f = 0.20 (so the two f labels' means
    and SDs differ); the rest stay near 0."""
    w = 0.03 * (run % 4)
    if arm == "N1-V":
        return _BT_PTS[lab] + w
    if arm == "N1-R" and d_ == _BT_RAND_NEG:
        return -0.8 * _BT_PTS[lab] + 0.05
    if arm == "N1-P":
        return {"+1": -0.9, "+d_eq": 0.3}.get(lab, 0.2) + 0.01 * ((run % 3) - 1)
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
        B.chk("reader path: a campaign written with the schema's builders (7,680 reads, 138 cells, nothing merged; "
              "N1-P at +1, +d_20, +d_eq and −1, ADDENDUM-n1 §5.2) reads back through check_cell to (REPLICATED, "
              "DETECTABLE, SHARED, PASS, PASS)",
              o["tuple"] == ("REPLICATED", "DETECTABLE", "SHARED", "PASS", "PASS") and len(camp.records) == 7680
              and len(camp.cells) == 138 and len(camp.planned["N1-P"]) == 640,
              (o["tuple"], len(camp.records), len(camp.cells)), cover=["RD-POSITIVE"])
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
        def zone(e): return ", against the conditioned zone" if e.mean < 0 else ""      # §5.3, a mean below 0
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
                    f"{u4(ceil_at(st, d20))}{zone(st.E[F20])}); the valence direction of record at the norm-matched "
                    f"point: Δm = {f4(st.V[d20].mean)} nats {ci4(st.V[d20])}{zone(st.V[d20])}"),
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
                              f"BK's apparatus beyond the leak ceiling (Δm = {f4(st3.E[F20].mean)} nats "
                              f"{ci4(st3.E[F20])} against {u4(ceil_at(st3, d20))}{zone(st3.E[F20])}) while the valence "
                              f"direction of record at the norm-matched point does (Δm = {f4(st3.V[d20].mean)} nats "
                              f"{ci4(st3.V[d20])}{zone(st3.V[d20])}) — concluded, not answered"),
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
        _c5, st5, _f5, o5 = _bt_eval(ind, sm)
        B.chk("reader path: a missing N1-R cell at +1/2 -> N1 and dose INDETERMINATE (incomplete:N1-R), N2 evaluated, "
              "since its certification reads N1-R at +d_20 alone (SHARED; PIN-n-29 as amended); a missing N4-Ts cell -> "
              "N4 INDETERMINATE, no read obtained", o5["tuple"][:4] == ("INDETERMINATE", "INDETERMINATE", "SHARED",
                                                                       "INDETERMINATE")
              and o5["N1"]["causes"] == ["incomplete:N1-R"] and o5["N4"]["no_read"]
              and o5["N4"]["causes"] == ["incomplete:N4-Ts"] and st5.at[("N1-R", 0.5)] == ["incomplete"]
              and st5.at[("N1-R", d20)] == [] and 0.5 not in st5.L and d20 in st5.L and st5.floor_V is None,
              (o5["tuple"], o5["N1"], o5["N4"]), cover=["RD-INDET"])
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
              "(nonfinite:N1-V, shadow:N1-P), N2's at the points it reads (shadow:N2-E@f0.20, shadow:N1-V@+d_20, "
              "shadow:N1-P@+d_20: the shadow a cause of every point, PIN-n-36); N1-R (40 floor sessions) keeps its "
              "floor and L; N4 PASS",
              o10["tuple"][:4] == ("INDETERMINATE",) * 3 + ("PASS",)
              and o10["N1"]["causes"] == ["nonfinite:N1-V", "shadow:N1-P"]
              and o10["N2"]["causes"] == ["shadow:N2-E@f0.20", "shadow:N1-V@+d_20", "shadow:N1-P@+d_20"]
              and st10.unusable == {"N1-P": "shadow", "N2-E": "shadow", "N2-S": "shadow", "N2-C": "shadow"}
              and st10.floor_V is not None and len(st10.L) == len(camp10.dmap.points()) - 1,
              (o10["tuple"], o10["N1"].get("causes"), o10["N2"].get("causes"), st10.unusable), cover=["RD-SHADOW"])
        # PIN-n-29 as amended: N1-P's −1 cell missing (elsewhere), then one N1-R read at N2's point non-finite
        pw1 = _bt_write_campaign(base / "pw1", sm, delta=_bt_delta_positive, omit=[("N1-P", "valence", "-1")])
        _cp1, stp1, _fp1, op1 = _bt_eval(pw1, sm)
        pw2 = _bt_write_campaign(base / "pw2", sm, delta=_bt_delta_positive,
                                 nonfinite=[f"N1-R|rand_03|+d_20|{session_key(5)}"])
        _cp2, stp2, _fp2, op2 = _bt_eval(pw2, sm)
        pw3 = _bt_write_campaign(base / "pw3", sm, delta=_bt_delta_positive, omit=[("N2-E", "span_reward", "f0.10")])
        _cp3, stp3, fp3, op3 = _bt_eval(pw3, sm)
        # every N1-P read at −1 re-computed above TAU/4 and below TAU: the TAU/4 row empties that point alone
        pw4 = _bt_write_campaign(base / "pw4", sm, delta=_bt_delta_positive,
                                 fresh_shift={f"N1-P|valence|-1|{session_key(r)}": 0.02 for r in range(N_SESSIONS)})
        _cp4, stp4, _fp4, op4 = _bt_eval(pw4, sm)
        _cs4, sts4, _fs4, os4 = _bt_eval(pw4, sm, drop=True)
        # one random direction's +1 reads (its 40 floor sessions) above TAU/4: the TAU/4 row empties N1-R at +1 (the
        # dose rule re-computes reads at 0 and ±1 only, so no other point can be emptied alone; N2's own point, emptied,
        # is N2-POINT-CAUSES's literal case)
        pw5 = _bt_write_campaign(base / "pw5", sm, delta=_bt_delta_positive,
                                 fresh_shift={f"N1-R|rand_04|+1|{session_key(r)}": 0.02 for r in range(N_FLOOR)})
        _cs5, sts5, _fs5, os5 = _bt_eval(pw5, sm, drop=True)
        # two causes at one of N2's points: N1-P's +d_20 cell missing and the shadow of run 100 non-finite
        pw6 = _bt_write_campaign(base / "pw6", sm, delta=_bt_delta_positive, omit=[("N1-P", "valence", "+d_20")],
                                 nonfinite=[f"N1-V|none|0|{session_key(100)}"])
        op6 = _bt_eval(pw6, sm)[3]
        keys1 = ({f"{a}@{x}" for a in ("N1-V", "N1-R") for x in ("+1", "+1/2", "+d_20", "+d_eq", "-1")}
                 | {f"N1-P@{x}" for x in ("+1", "+d_20", "+d_eq", "-1")}
                 | {f"{a}@{x}" for a in ("N2-E", "N2-S", "N2-C") for x in ("f0.10", "f0.20")})
        rows1 = {(r["arm"], r["labels"][0]): r for r in gleak_table(stp1)}
        rows2 = {(r["arm"], r["labels"][0]): r for r in gleak_table(stp2)}
        pc1 = state_figures(stp1, _fp1)["point_causes"]
        pw_ok = {"N1-P at -1": op1["tuple"][:4] == ("INDETERMINATE", "INDETERMINATE", "SHARED", "PASS")
                 and op1["N1"]["causes"] == ["incomplete:N1-P"] and sorted(stp1.P) == sorted([1.0, d20, deq])
                 and rows1[("N1-V", "-1")]["why"] == "not usable: incomplete:N1-P@-1"
                 and rows1[("N1-V", "d_20")]["certified"] is True and pc1["N1-P@-1"] == ["incomplete"]
                 and set(pc1) == keys1 and all(v == [] for k, v in pc1.items() if k != "N1-P@-1")
                 and all(op1["N2"]["beside"][F10][k] != "not computed"
                         for k in ("E", "V", "ceiling", "certified", "certified_V")),
                 "N1-R at +d_20": op2["tuple"][:4] == ("INDETERMINATE", "INDETERMINATE", "INDETERMINATE", "PASS")
                 and op2["N1"]["causes"] == ["nonfinite:N1-R"] and op2["N2"]["causes"] == ["nonfinite:N1-R@+d_20"]
                 and rows2[("N1-V", "d_20")]["why"] == "not usable: nonfinite:N1-R@+d_20"
                 and rows2[("N2-E", F20)]["certified"] is None and rows2[("N2-E", F10)]["certified"] is not None
                 and d20 not in stp2.L and 0.5 in stp2.L,
                 "N2-E at f = 0.10": op3["tuple"][:4] == ("REPLICATED", "DETECTABLE", "SHARED", "PASS")
                 and sorted(stp3.E) == [F20] and op3["N2"]["beside"][F10]["E"] == "not computed"
                 and op3["N2"]["beside"][F10]["certified"] == "not computed"
                 and op3["N2"]["beside"][F10]["certified_V"] is True and "N2-E" not in fp3["slopes_N2"]
                 and ("N2-E", "f0.20") in fp3["n"],
                 "the TAU/4 row empties N1-P at -1": op4["tuple"][:4] == ("REPLICATED", "DETECTABLE", "SHARED", "PASS")
                 and stp4.at[("N1-P", -1.0)] == [] and sts4.at[("N1-P", -1.0)] == ["tau4-emptied"]
                 and sts4.unusable.get("N1-P") == "tau4-emptied" and os4["N1"]["causes"] == ["tau4-emptied:N1-P"]
                 and os4["tuple"][:3] == ("INDETERMINATE", "INDETERMINATE", "SHARED")
                 and sorted(sts4.P) == sorted([1.0, d20, deq]),
                 "the TAU/4 row empties N1-R at +1 (one direction)": sts5.at[("N1-R", 1.0)] == ["tau4-emptied"]
                 and sts5.unusable.get("N1-R") == "tau4-emptied" and os5["N1"]["causes"] == ["tau4-emptied:N1-R"]
                 and os5["tuple"][:3] == ("INDETERMINATE", "INDETERMINATE", "SHARED") and 1.0 not in sts5.L
                 and sorted(sts5.L) == sorted([0.5, d20, deq, -1.0])
                 and [r["why"] for r in gleak_table(sts5) if r["arm"] == "N1-V" and r["point"] == 1.0]
                 == ["not usable: tau4-emptied:N1-R@+1"],
                 "two causes at one point, in order": op6["N2"]["causes"] == [
                     "shadow:N2-E@f0.20", "shadow:N1-V@+d_20", "incomplete:N1-P@+d_20", "shadow:N1-P@+d_20"]}
        B.chk("reader path, point by point (PIN-n-29 as amended, PIN-n-36): N1-P's −1 cell missing leaves N2 SHARED "
              "with N1 and dose INDETERMINATE, P computed at its other points, G-LEAK-n's −1 row not computed and its "
              "+d_20 row computed, the point causes in VERDICTS' figures; one N1-R read at +d_20 non-finite makes N2 "
              "INDETERMINATE (nonfinite:N1-R@+d_20), the rows at +d_20 not computed, L computed elsewhere; N2-E's "
              "f = 0.10 cell missing leaves N2 decided at f = 0.20, its beside's span_reward figure not computed and "
              "no N2 slope; the TAU/4 row emptying N1-P at −1 alone marks that point and its arm (tau4-emptied:N1-P), "
              "N1 and dose INDETERMINATE and N2 SHARED in that row, P computed at N1-P's other points; emptying one "
              "random direction at +1 marks N1-R's +1 and the arm (G-LEAK-n's +1 row not computed), N2 decided, L "
              "computed at the other points; two causes at one point named in the reader's order (incomplete, then "
              "shadow); N2's beside computed where no read of its own point is missing; VERDICTS' point causes, every "
              "key",
              all(pw_ok.values()),
              [k for k, v in pw_ok.items() if not v] or (op1["tuple"], op2["tuple"], op3["tuple"], os4["tuple"]),
              cover=["RD-POINTWISE"])
        p_minus = lambda a, d, l, r: (-0.9 if (a == "N1-P" and l == "+1")             # noqa: E731
                                      else _bt_delta_positive(a, d, l, r))
        mg = _bt_write_campaign(base / "mg", sm, R_ell=37.485, delta=p_minus)
        camp7, st7, fig7, o7 = _bt_eval(mg, sm)
        B.chk("reader path (shape c): R_ell 37.485 gives d_eq ≈ 0.49, folded into +1/2, and d_20 ≈ 0.98, folded into "
              "+1 with the cap not binding -> 5,280 reads (N1-P at +1, +1/2 and −1); N2 is decided at f = 0.20 "
              "against +1, the ratio 2·d_eq "
              "reported; N1-P at −0.9 there puts P(+1) above L(+1), and N2's reported ceiling is max(L, P) = P(+1), "
              "the one its certification used (E 0.625 below it: SPECIFIC)", len(camp7.records) == 5280
              and sorted({rid.split("|")[2] for rid in camp7.planned["N1-P"]}) == ["+1", "+1/2", "-1"]
              and not camp7.dmap.cap_binds() and o7["N2"]["f"] == F20 and o7["N2"]["point"] == 1.0
              and camp7.dmap.resolved()["d_eq"] == 0.5
              and abs(o7["N2"]["match_ratio"] - 2.0 * camp7.dmap.d_eq) <= 1e-12
              and st7.P[1.0] > st7.L[1.0] and o7["N2"]["ceiling"] == st7.P[1.0] and o7["N2"]["state"] == "SPECIFIC",
              (len(camp7.records), o7["N2"].get("f"), o7["N2"].get("point"), o7["N2"].get("ceiling"),
               o7["N2"]["state"]), cover=["RD-MERGED"])
        cb = _bt_write_campaign(base / "cb", sm, R_ell=50.0, delta=p_minus)
        camp7b, st7b, fig7b, o7b = _bt_eval(cb, sm)
        bes = o7b["N2"].get("beside", {}).get(F20, {})
        B.chk("reader path (shape b): R_ell 50 gives 2·d_eq ≈ 1.31 > 1, so the cap binds and +d_20 merges into +1 -> "
              "6,400 reads (N1-P at +1, +d_eq and −1); N2 is decided at f = 0.10 against N1-V at d_eq (ratio 1; E "
              "0.3125 above its ceiling max(L, P)(d_eq): SHARED) "
              "and f = 0.20 is reported beside against +1 at the ratio 2·d_eq, where N1-P at −0.9 puts P(+1) above "
              "L(+1) and the beside's ceiling is max(L, P) = P(+1) (E 0.625 below it: not certified); the label's "
              "input reads span_reward's G-READ-n at f = 0.10 (OPEN-Q7 as ruled; the label itself: "
              "SENT-FILLED-N2-CAP)", len(camp7b.records) == 6400
              and sorted({rid.split("|")[2] for rid in camp7b.planned["N1-P"]}) == ["+1", "+d_eq", "-1"]
              and camp7b.dmap.cap_binds() and o7b["N2"]["f"] == F10 and o7b["N2"]["point"] == camp7b.dmap.d_eq
              and o7b["N2"]["match_ratio"] == 1.0 and o7b["N2"]["state"] == "SHARED"
              and o7b["N2"]["ceiling"] == max(st7b.L[camp7b.dmap.d_eq], st7b.P[camp7b.dmap.d_eq])
              and bes.get("point") == 1.0 and abs(bes.get("match_ratio", 0.0) - 2.0 * camp7b.dmap.d_eq) <= 1e-12
              and st7b.P[1.0] > st7b.L[1.0] and bes.get("ceiling") == st7b.P[1.0] and bes.get("certified") is False
              and _bt_eval(cb, sm, gread=_bt_gread_all(camp7b.dmap) | {("span_reward", F10): "FAIL"})[3]["gread"]["E"]
              == "FAIL",
              (len(camp7b.records), o7b["N2"].get("f"), o7b["N2"].get("point"), o7b["N2"]["state"], bes),
              cover=["RD-CAP-BINDS"])
        deq_b = camp7b.dmap.d_eq

        def org_b(xs, ys):                                                  # through the origin, by hand
            return sum(a * b for a, b in zip(xs, ys)) / sum(a * a for a in xs)
        hand_e = float(np.mean([org_b([deq_b, 2 * deq_b], [0.3125 + 0.03 * ((r % 4) - 1.5),
                                                           0.625 + 0.03 * ((r % 4) - 1.5)]) for r in range(160)]))
        hand_fl = abs(float(np.mean([org_b([deq_b, 1.0], [0.01 * ((r % 3) - 1)] * 2) for r in range(40)])))
        sn2, fn2 = fig7b["slopes_N2"]["N2-E"], fig7b["floors_N2"]
        B.chk("reader path (shape b): N2's slope through the origin over (d_eq, 2·d_eq) and its floor at the kept "
              "points (d_eq, +1), the mismatch printed beside each (OPEN-Q9 as ruled; ADDENDUM-n1 §7.5), to the hand "
              "computation", sn2["points"] == [deq_b, 2 * deq_b] and sn2["floor_points"] == [deq_b, 1.0]
              and sn2["mismatch"] is True and abs(sn2["mean"] - hand_e) <= 1e-9 and fn2["points"] == [deq_b, 1.0]
              and fn2["n2_points"] == [deq_b, 2 * deq_b] and fn2["mismatch"] is True
              and abs(fn2["floor"] - hand_fl) <= 1e-9, (sn2.get("mean"), hand_e, fn2.get("floor"), hand_fl),
              cover=["RD-CAP-SLOPES"])
        # F11: the asymmetric campaign; every statistic against a hand computation from the deltas as written
        asym = _bt_write_campaign(base / "asym", sm, delta=_bt_asym, told=_bt_asym_told, sham=_bt_asym_sham)
        camp11, st11, fig11, o11 = _bt_eval(asym, sm)
        lv = label_values(camp11.identity)
        vpts = sorted(set(lv.values()), reverse=True)                       # 0 included
        labs = {p: l for l, p in lv.items()}
        nzp = [p for p in vpts if p != 0.0]

        def y_of(arm, d_, run):
            return [0.0 if p == 0.0 else _bt_asym(arm, d_, labs[p], run) for p in vpts]

        def org(xs, ys):                                                    # through the origin, by hand
            return sum(a * b for a, b in zip(xs, ys)) / sum(a * a for a in xs)
        hand_slope_v = float(np.mean([org(nzp, [_bt_asym("N1-V", "valence", labs[p], r) for p in nzp])
                                      for r in range(160)]))
        hand_slope_v_int = float(np.mean([np.polyfit(vpts, y_of("N1-V", "valence", r), 1)[0] for r in range(160)]))
        dirs = [f"rand_{i:02d}" for i in range(N_RANDOM)]
        hand_floor = max(abs(float(np.mean([org(nzp, [_bt_asym("N1-R", d_, labs[p], r) for p in nzp])
                                            for r in range(40)]))) for d_ in dirs)
        hand_L = {p: max(abs(float(np.mean([_bt_asym("N1-R", d_, labs[p], r) for r in range(40)]))) for d_ in dirs)
                  for p in vpts if p != 0.0}
        hand_P = {p: abs(float(np.mean([_bt_asym("N1-P", "valence", lab, r) for r in range(160)])))
                  for lab, p in (("+1", 1.0), ("+d_20", 0.625), ("+d_eq", 0.3125), ("-1", -1.0))}
        p_deq, p_d20 = camp11.dmap.d_eq, camp11.dmap.resolved()["d_20"]
        hand_n2 = float(np.mean([org([p_deq, 2.0 * p_deq], [_bt_asym("N2-E", "span_reward", "f0.10", r),
                                                             _bt_asym("N2-E", "span_reward", "f0.20", r)])
                                 for r in range(160)]))
        hand_n2_floor = max(abs(float(np.mean([org([p_deq, p_d20], [_bt_asym("N1-R", d_, labs[p_deq], r),
                                                                     _bt_asym("N1-R", d_, labs[p_d20], r)])
                                               for r in range(40)]))) for d_ in dirs)
        tv = np.array([_bt_asym_told(r, "") for r in range(160)])
        tmeans = tv[boot_index("N4-T", 160)].mean(axis=1)
        hand_98 = (_bt_hand_pct(tmeans, 1.0), _bt_hand_pct(tmeans, 99.0))
        close = lambda a, b: abs(a - b) <= 1e-9                              # noqa: E731
        asym_ok = {
            "tuple": o11["tuple"] == ("REPLICATED", "DETECTABLE", "SPECIFIC", "INDETERMINATE", "PASS"),
            "slope_V through the origin": close(st11.slope_V.mean, hand_slope_v),
            "with-intercept slope beside (d = 0 in the fit), differing": close(
                fig11["slope_V_with_intercept"]["mean"], hand_slope_v_int)
            and abs(hand_slope_v - hand_slope_v_int) > 1e-3 and fig11["slope_V_with_intercept"]["descriptive"] is True,
            "floor (|slope|, rand_05 negative)": close(st11.floor_V, hand_floor) and fig11["floor_dir"] == _BT_RAND_NEG,
            "L (|mean|)": all(close(st11.L[p], hand_L[p]) for p in hand_L) and len(st11.L) == len(hand_L),
            "P (|mean| at each of N1-P's four points)": all(close(st11.P[p], hand_P[p]) for p in hand_P)
            and len(st11.P) == 4 and fig11["P_signed"]["+1"]["mean"] < 0.0,
            "N1 ceiling max(L, P) = P(+1)": hand_P[1.0] > hand_L[1.0] and close(o11["N1"]["ceiling"], hand_P[1.0]),
            "dose ceiling max(L, P) at d_eq, P's": hand_P[p_deq] > hand_L[p_deq]
            and close(o11["dose"]["ceiling"], hand_P[p_deq]),
            "E by f": close(st11.E[F10].mean, 1.045) and close(st11.E[F20].mean, 0.19),
            "N2's per-f n and SD (ddof 0)": fig11["n"][("N2-E", "f0.10")] == fig11["n"][("N2-E", "f0.20")] == 160
            and close(fig11["sd0"][("N2-E", "f0.10")],
                      float(np.std([_bt_asym("N2-E", "span_reward", "f0.10", r) for r in range(160)])))
            and close(fig11["sd0"][("N2-E", "f0.20")],
                      float(np.std([_bt_asym("N2-E", "span_reward", "f0.20", r) for r in range(160)])))
            and fig11["sd0"][("N2-E", "f0.20")] > 1.5 * fig11["sd0"][("N2-E", "f0.10")],
            "N2 slope (d_eq, 2 d_eq) through the origin": close(fig11["slopes_N2"]["N2-E"]["mean"], hand_n2)
            and fig11["slopes_N2"]["N2-E"]["points"] == [p_deq, 2.0 * p_deq]
            and fig11["slopes_N2"]["N2-E"]["mismatch"] is False,
            "N2's floor at d_eq's and d_20's points": close(fig11["floors_N2"]["floor"], hand_n2_floor)
            and fig11["floors_N2"]["points"] == [p_deq, p_d20] and fig11["floors_N2"]["mismatch"] is False,
            "E_sham |negative mean|": close(st11.e_sham, 0.3),
            "m_told 98%": close(st11.told.lo, hand_98[0]) and close(st11.told.hi, hand_98[1])
            and _bt_hand_pct(tmeans, 2.5) > 0.0 > hand_98[0] and st11.told.level == 98}
        B.chk("reader path (F11): an asymmetric campaign -- a random direction with a negative slope and offset, N1-P "
              "at −0.9 / +0.2, N2-E at 1.0 / 0.1 by f with spreads in the ratio 1:2, a negative sham mean, a session "
              "offset of mean +0.045 -- reads to the hand computation: the slope through the origin and the "
              "with-intercept slope beside (they differ here), the floor as max |mean slope|, L and P as |mean| at "
              "their own points, the ceilings, E by f, N2's per-f n and SD, N2's slope and its floor through the "
              "origin, E, and m_told's 98% CI (whose 95% would have excluded 0)", all(asym_ok.values()),
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
              "INDETERMINATE (pause:N2-E, pause:N1-R: both stand on its reads, PIN-n-29 as amended), N4 PASS",
              paused["tuple"][:4] == ("INDETERMINATE",) * 3 + ("PASS",)
              and paused["N1"]["causes"] == ["pause:N1-R"] and paused["N2"]["causes"] == ["pause:N2-E", "pause:N1-R"],
              paused["tuple"], cover=["RD-PAUSE"])
        # PIN-n-37: the points the report's standing pauses stand on (paused_points), against sets derived here from
        # the dose map's points (State's), not from the plan's read ids
        nz = {p for p in camp.dmap.points() if p != 0.0}
        pts_ = {"N1-V": nz, "N1-R": nz, "N1-P": set(camp.dmap.n1p_points()), "N2-E": {F10, F20},
                "N2-S": {F10, F20}, "N2-C": {F10, F20}}

        def keys_(*arms: str) -> set:
            return {(a, k) for a in arms for k in pts_[a]}

        def pq(**kw: Any) -> dict:
            return {"read_id": None, "arms_in_scope": [], "adjudicated": False, "binomial": None} | kw

        def bat(lo: int, hi: int) -> dict:
            return {"first_launch_index": lo, "last_launch_index": hi}
        li_ = {rid: r["launch_index"] for rid, r in camp.records.items()}
        m1p = sorted(li_[r] for r in camp.planned["N1-P"] if r.split("|")[2] == "-1")
        sh3, sh159 = f"N1-V|none|0|{session_key(3)}", f"N1-V|none|0|{session_key(159)}"
        steered = sorted(STEERED_ARMS)
        cases_pp = {
            "a read alone (N1-V at −1)": ([pq(read_id=f"N1-V|valence|-1|{session_key(7)}", arms_in_scope=["N1-V"])],
                                         {("N1-V", -1.0)}),
            "a rendering pause's read (N2-E at f0.10)": (
                [pq(read_id=f"N2-E|span_reward|f0.10|{session_key(7)}", arms_in_scope=["N2-E"])], {("N2-E", F10)}),
            "a floor session's shadow, the runner's scope": ([pq(read_id=sh3, arms_in_scope=steered)],
                                                             keys_(*steered)),
            "the same shadow, its scope N1-V alone": ([pq(read_id=sh3, arms_in_scope=["N1-V"])], keys_("N1-V")),
            "a neutral session's shadow (N1-R reads it not)": (
                [pq(read_id=sh159, arms_in_scope=steered)], keys_(*(a for a in steered if a != "N1-R"))),
            "a binomial batch over N1-P's −1 cell": ([pq(arms_in_scope=["N1-P"], binomial=bat(m1p[0], m1p[-1]))],
                                                     {("N1-P", -1.0)}),
            "the same batch outside its scope": ([pq(arms_in_scope=["N1-V"], binomial=bat(m1p[0], m1p[-1]))], set()),
            "a binomial batch of one shadow": ([pq(arms_in_scope=["N1-V", "N2-E"], binomial=bat(li_[sh159],
                                                                                                li_[sh159]))],
                                               keys_("N1-V", "N2-E")),
            "N4's pause (read per arm)": ([pq(read_id=f"N4-Ts|none|0|{session_key(9)}", arms_in_scope=["N4-Ts"])],
                                          set()),
            "an adjudicated pause": ([pq(read_id=sh3, arms_in_scope=steered, adjudicated=True)], set())}
        nt_v = min(li_[r] for r in camp.planned["N1-V"] if r.split("|")[2] == "+1/2"
                   and camp.records[r]["fidelity"] is None)                # a read the keyed sample does not hold
        n4t = li_[f"N4-Ts|none|0|{session_key(9)}"]                        # a d = 0 read, re-computed, not a shadow
        cases_pp |= {"a range holding no trial": ([pq(arms_in_scope=["N1-V"], binomial=bat(nt_v, nt_v))], set()),
                     "an N4 trial is no shadow": ([pq(arms_in_scope=["N1-V", "N4-Ts"], binomial=bat(n4t, n4t))],
                                                  set())}
        # the review's B1: a range over N1-P's +d_20, +d_eq and −1 cells, −1 alone re-computed by the dose rule; and
        # the same range on a campaign with two +d_eq reads on the keyed sample (a re-computation at another point)
        lo_p = min(li_[r] for r in camp.planned["N1-P"] if r.split("|")[2] == "+d_20")
        hi_p = max(li_[r] for r in camp.planned["N1-P"] if r.split("|")[2] == "-1")
        cases_pp["a range over N1-P's +d_20 to −1 cells"] = ([pq(arms_in_scope=["N1-P"], binomial=bat(lo_p, hi_p))],
                                                             {("N1-P", -1.0)})
        got_pp = {k: {kk for kk, v in paused_points({"pauses": qs}, camp).items() if v}
                  for k, (qs, _w) in cases_pp.items()}
        want_pp = {k: w for k, (_qs, w) in cases_pp.items()}
        smp = _bt_write_campaign(base / "smp", sm, delta=_bt_delta_positive,
                                 sampled=[f"N1-P|valence|+d_eq|{session_key(r)}" for r in (3, 7)])
        camp_s = load_campaign(smp, sm)
        k_s = "the same range, two +d_eq reads on the keyed sample"
        got_pp[k_s] = {kk for kk, v in paused_points({"pauses": [pq(arms_in_scope=["N1-P"],
                                                                     binomial=bat(lo_p, hi_p))]}, camp_s).items() if v}
        want_pp[k_s] = {("N1-P", camp_s.dmap.resolved()["d_eq"]), ("N1-P", -1.0)}
        B.chk("reader path: the points a standing pause stands on (PIN-n-37), within its scope: its read's point; a "
              "shadow's every read of its session (N1-R's only on a floor session); a binomial batch's trials, the "
              "reads carrying a re-computation in its range (the dose rule's and the keyed sample's, not every read "
              "in it), and through a shadow among them its session's reads, a range holding no trial standing on "
              "nothing and an N4 d = 0 trial being no shadow; nothing for N4's pause (per arm) or an adjudicated one "
              "(fourteen cases)", got_pp == want_pp,
              [k for k in want_pp if got_pp.get(k) != want_pp[k]], cover=["RD-PAUSE-POINTS"])
        gr = _bt_gread_all(camp.dmap, "FAIL")
        o8 = _bt_eval(null, sm, gread=gr)
        B.chk("reader path: G-READ-n FAIL everywhere -> the tuple's coordinate FAIL; the NOT-REPLICATED and NULL "
              "labels concluded, not answered", o8[3]["tuple"][4] == "FAIL"
              and sentence_set_filled(o8[3], o8[1], route="B", auc={"d_eq": None})["7.1"]["label"] == CNA,
              o8[3]["tuple"], cover=["RD-GREAD"])
        # F12: mixed G-READ-n states on a campaign where N4 PASSES and nothing else moves; each label and the tuple's
        # coordinate must read its own cell (valence at +1 for N1, at d_eq for dose and the coordinate, span_reward
        # at N2's decision f for N2: f = 0.20 on this map, the cap not binding; the binding case is RD-CAP-BINDS)
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
                                   "§5, its ellipsis expanded by Code, amended by ADDENDUM-n1 §7.6 and the seat's "
                                   "answers of 2026-11-18 §5.4", ANSWERED, False),
                    "+1-fails": (("NOT-REPLICATED", "NOT-DETECTABLE", "NULL", "PASS", "PASS"), CNA, ANSWERED,
                                 "§5, amended by ADDENDUM-n1 §7.6 and the seat's answers of 2026-11-18 §5.4",
                                 CNA, True)}
        stop_auc = _bt_raises(lambda: sentence_set_filled(o_m, st_m, route="B", auc={"d_eq": None}), (AnlStop,))
        stop_route = _bt_raises(lambda: sentence_set_filled(o_m, st_m, route="C", auc={"d_eq": 0.81}), (AnlStop,))
        B.chk("reader path (F12): G-READ-n FAIL at d_eq only -> the coordinate FAIL, N1's label answered, the dose "
              "sentence not readable; FAIL at +1 only -> the coordinate PASS, N1's label concluded, the dose sentence "
              "answered with its AUC; N2's label follows span_reward at its decision f (0.20 here, OPEN-Q7 as ruled); "
              "a readable dose sentence without an "
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
              "below 20, (d) r over 160 sessions, (e) six cosines and the matched means -- and (b) reads struck, by "
              "ADDENDUM-n1 §4", sec["d_retention_r"]["n"] == 160 and len(sec["e_directions"]["cosines"]) == 6
              and sec["b_free_text"] == B_STRUCK and "struck" in B_STRUCK and all(
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
        n2s = sm.cell_filename("N2-S", "span_sentiment", "f0.20")
        capx = _bt_write_campaign(base / "capx", sm, delta=_bt_delta_positive,
                                  capture_cells=[("N2-S", "span_sentiment", "f0.20")])
        site = sm.example_identity()["layer"]
        (capx / sm.capture_filename(n2s, site)).write_bytes(b"x")          # the site's layer: outside the band
        refs["capture-layer"] = _bt_raises(lambda: load_campaign(capx, sm), (AnlRefusal,))
        capo = _bt_write_campaign(base / "capo", sm, delta=_bt_delta_positive, omit=[("N2-S", "span_sentiment",
                                                                                      "f0.20")])
        (capo / sm.capture_filename(n2s, site + 1)).write_bytes(b"")       # a band layer of a cell not present
        refs["capture-cell"] = _bt_raises(lambda: load_campaign(capo, sm), (AnlRefusal,))
        capk = _bt_write_campaign(base / "capk", sm, delta=_bt_delta_positive,
                                  capture_cells=[("N2-S", "span_sentiment", "f0.20"), ("N1-P", "valence", "-1")])
        (capk / sm.capture_filename(sm.cell_filename("N1-P", "valence", "-1"), site + 1)).unlink()
        camp_k = load_campaign(capk, sm)

        class _SmPlan:                          # the schema with a read plan one read short of the analyzer's
            def __init__(self, base_sm):
                self._b = base_sm

            def __getattr__(self, k):
                return getattr(self._b, k)

            def read_plan(self, ident):
                return self._b.read_plan(ident)[1:]
        refs["plan"] = _bt_raises(lambda: load_campaign(capk, _SmPlan(sm)), (AnlRefusal,))
        cap_ok = (len(camp_k.cells) == 138 and camp_k.cells[n2s]["capture_sha256"]
                  == {str(x): hashlib.sha256(f"{n2s}|{x}".encode()).hexdigest() for x in range(site + 1, 64)})
        refs["shadow-absent"] = _bt_raises(lambda: load_campaign(_bt_write_campaign(base / "sa", sm,
                                                                                     delta=_bt_delta_positive,
                                                                                     omit=[("N1-V", "none", "0")]), sm),
                                           (AnlRefusal,))
        want = {"stray": "beside the cells", "identity": "stage identity differs", "shadow": "shadow",
                "zones": "schedule zones", "schema": "margin", "cues": "cues or present order differ",
                "balance": "80 S and 80 U", "capture-layer": "beside the cells", "capture-cell": "beside the cells",
                "shadow-absent": "is not on disk", "plan": "differs from the analyzer's own derivation"}
        B.chk("reader path refuses: a file no cell names; a stage identity that differs between cells; a read whose "
              "ids_sha differs from its shadow's; N4-T and N4-Ts zones that differ; a record the schema's check_cell "
              "refuses; a session whose cues differ between reads; a schedule of 81 S and 79 U on both N4 arms; a "
              "capture array named for the site's layer (outside the band) or for a cell not present; steered reads "
              "whose shadows are not on disk; a schema whose read plan differs from the analyzer's own derivation. It "
              "accepts capture arrays named for a present cell's band layers, one of "
              "them absent, reading none and binding each cell by the row hashes it records (PIN-n-31)",
              all(refs[k][0] and want[k] in refs[k][1] for k in want) and cap_ok,
              {k: (v[0], v[1][:80]) for k, v in refs.items()} | {"accepted": cap_ok}, cover=["RD-REFUSE"])


# =====================================================================================================================
# 14. Outputs: write-once, the not-run command, G-ANL-n's artifact
# =====================================================================================================================
GANL_REL = "data/n/gates/G-ANL-n.json"
GANL_SCHEMA = "n-ganl-v1"
VERDICTS_REL = "data/n/verdicts"
NOT_RUN_OUT_SCHEMA = "n-not-run-out-v1"


def json_text(obj: Any) -> str:
    """An output's text: sorted keys, one-space indent, UTF-8; a non-finite number STOPs (no NaN is ever written)."""
    try:
        return json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False, allow_nan=False) + "\n"
    except ValueError as e:
        raise AnlStop(f"STOP: an output holds a non-finite number ({type(e).__name__})")


def _err_where(e: BaseException) -> str:
    """A refusal's cause without its values (n §4 "Blinding": nothing from a read reaches the terminal): a schema
    error by its field path alone, any other error by its type, and a file-system error with its message."""
    s = str(e)
    if type(e).__name__ == "SchemaError":
        return "SchemaError at " + s.split(": ", 1)[0]
    if isinstance(e, OSError):
        return f"{type(e).__name__}: {e.strerror or s}"
    return type(e).__name__


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


def write_all_once(items: Sequence[tuple[Path, str]]) -> list[str]:
    """write_once over several outputs, refused before any of them is written when one exists with other bytes, so a
    refusal never leaves a new output beside an old one."""
    for path, text in items:
        if path.exists() and path.read_bytes() != text.encode("utf-8"):
            raise AnlRefusal(f"REFUSED: {path.name} exists with other bytes (write-once)")
    return [write_once(path, text) for path, text in items]


def analyzer_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def not_run_doc(rec: Mapping[str, Any], record_ref: Mapping[str, Any],
                extra: Mapping[str, Any] | None = None) -> dict:
    """N-pod's NOT-RUN output from a NOT-RUN record, which not_run_reason validates (n §5 "Unit outcome first"), with
    its sentence set; ``record_ref`` names the record (a file, or the stage report it was derived from); ``extra``
    adds bindings (a derived NOT-RUN's lock and schema module)."""
    reason = not_run_reason(rec)
    sset = {k: dict(v, text=v["text"].replace("[reason]", reason)) for k, v in sentence_set(NOT_RUN).items()}
    return {"schema": NOT_RUN_OUT_SCHEMA, "unit": UNIT, "outcome": NOT_RUN, "cause": rec["cause"], "reason": reason,
            "record": dict(record_ref), "date": rec["date"], "sentences": sset,
            "proposal_sha256": PROPOSAL_SHA256, "addendum_sha256": ADDENDUM_SHA256,
            "analyzer_sha256": analyzer_sha256(), "pins": PINS, "open": OPEN, **dict(extra or {})}


def run_not_run(record: Path, out_dir: Path) -> tuple[Path, str]:
    """`not-run`: N-pod's NOT-RUN output from a NOT-RUN record file, write-once. It takes a Clock cause only: a no-arm
    NOT-RUN is derived from the stage report by `verdicts` (the schema's docstring). It refuses beside VERDICTS: a unit
    has one outcome."""
    try:
        data = Path(record).read_bytes()
        rec = json.loads(data.decode("utf-8"))
    except (OSError, ValueError) as e:
        raise AnlRefusal(f"REFUSED: the NOT-RUN record: {type(e).__name__}")
    if not (isinstance(rec, dict) and isinstance(rec.get("cause"), str) and rec["cause"].startswith("clock:")):
        raise AnlRefusal("REFUSED: not-run takes a Clock cause; a no-arm NOT-RUN is derived from the stage report by "
                         "verdicts")
    doc = not_run_doc(rec, {"name": Path(record).name, "sha256": hashlib.sha256(data).hexdigest()})
    one_outcome(Path(out_dir), "NOT-RUN")
    path = Path(out_dir) / f"{UNIT}_NOT-RUN.json"
    return path, write_once(path, json_text(doc))


def one_outcome(out_dir: Path, writing: str) -> None:
    """A unit has one outcome: a NOT-RUN is never written beside VERDICTS, nor VERDICTS beside a NOT-RUN."""
    other = {"NOT-RUN": f"{UNIT}_VERDICTS.json", "VERDICTS": f"{UNIT}_NOT-RUN.json"}[writing]
    if (out_dir / other).exists():
        raise AnlRefusal(f"REFUSED: {other} is already in the output directory; a unit has one outcome")


# --- the battery's verdicts path: reports, G-READ-n artifacts and locks to the schema, around written campaigns ---
def _bt_lock_text(*, route: str | None = "B", names_analyzer: bool = True, routes: int = 1,
                  v10: bool = True) -> bytes:
    """A literal LOCK-n v1.0 for the battery: PIN-n-26's line saying what it is (left out when ``v10`` is false, so
    only the title names v1.0), the analyzer's sha256 between backticks (or not), and its direction of record as
    PIN-n-26's whole line, ``routes`` times."""
    lines = ["# LOCK-n v1.0 (a battery literal)", ""] + ([LOCK_V10_LINE, ""] if v10 else [])
    lines += [f"`{analyzer_sha256() if names_analyzer else '0' * 64}`", ""]
    lines += [f"{ROUTE_LINE}{route}"] * (routes if route is not None else 0)
    return ("\n".join(lines) + "\n").encode("utf-8")


def _bt_files(cdir: Path | None) -> tuple[dict, dict]:
    """The battery's own count of a campaign written at ``cdir``, from its files (not load_campaign or report_counters,
    which the reader checks a report against; the review's B2): the cells as a report names them (both shas, of the
    files' bytes, and the record count), and the counters as n-build's runner counts them (its answer of 2026-11-16):
    per 'arm|dose_label' the records re-computed and those above TAU and TAU/4 (``is True``); the records non-finite
    on either path; the records outside the identity bound; per 'arm|dose_label' the finite records whose label mass
    is under .20; and the records' duration_ms sum, the cap's used time."""
    cells: dict = {}
    fid: dict = {}
    lm: dict = {}
    nonfin = oob = used = 0
    for f in (sorted(Path(cdir).glob("*.json")) if cdir is not None else []):
        cell = json.loads(f.read_text(encoding="utf-8"))
        cells[f.name] = {"json_sha256": hashlib.sha256(f.read_bytes()).hexdigest(),
                         "capture_sha256": dict(cell["capture_sha256"]),
                         "records": len(cell["records"])}
        key = f"{cell['arm']}|{cell['dose_label']}"
        for r in cell["records"]:
            used += r["duration_ms"]
            fb = r["fidelity"]
            if fb is not None:
                x = fid.setdefault(key, {"trials": 0, "exceed_tau": 0, "exceed_tau4": 0})
                x["trials"] += 1
                x["exceed_tau"] += fb["exceeds_tau"] is True
                x["exceed_tau4"] += fb["exceeds_tau4"] is True
            nonfin += r["finite"] is False or (fb is not None and fb["finite"] is False)
            oob += r["identity"] is not None and r["identity"]["within"] is False
            if r["finite"] is True and r["restricted"]["label_mass"] < 0.20:
                lm[key] = lm.get(key, 0) + 1
    return cells, {"fidelity": fid, "nonfinite_reads": nonfin, "identity_out_of_bound": oob,
                   "label_mass_below_floor": lm, "used_ms": used}


def _bt_report_for(ident: Mapping[str, Any], cdir: Path | None, sm, *, end_state: str = "COMPLETE",
                   pauses: Sequence[dict] = (), stop: dict | None = None, hour_cap_ms: int | None = None,
                   used_ms: int | None = None, label_mass: bool = False,
                   counters_over: Mapping[str, Any] | None = None, loads_ms: Sequence[int] = (5000,)) -> dict:
    """A stage report of the campaign written at ``cdir`` (None: a report of no record), as n-build's runner writes
    one, from the battery's own count of the files (_bt_files): its cells, per-arm counts against the schema's plan,
    counters and used time (``used_ms`` overrides it); the label-mass counter null, as the runner leaves it, or the
    files' count with ``label_mass``; ``counters_over`` replaces counters. Checked by the schema's check_report."""
    plan = sm.read_plan(ident)
    cells, cnt = _bt_files(cdir)
    per_arm = {}
    for a in ARMS:
        got = sum(c["records"] for n, c in cells.items() if n.split("__")[0] == a)
        planned = sum(1 for x in plan if x.split("|")[0] == a)
        per_arm[a] = {"planned": planned, "obtained": got, "complete": got == planned}
    named = [[q["kind"]] + list(q["also_fired"]) for q in pauses]
    batches = [q["binomial"] for q in pauses if q["binomial"] is not None]
    used = cnt["used_ms"] if used_ms is None else used_ms
    ctr = {"fidelity": cnt["fidelity"], "nonfinite_reads": cnt["nonfinite_reads"],
           "identity_out_of_bound": cnt["identity_out_of_bound"],
           "rendering_mismatches": 1 if end_state == "G-VER-STOP" else sum(1 for ks in named if ks[0] == "rendering"),
           "label_mass_below_floor": cnt["label_mass_below_floor"] if label_mass else None}
    ctr.update(counters_over or {})
    rep = {"schema": sm.REPORT_SCHEMA, "stage_identity": dict(ident),
           "stage_identity_sha256": sm.identity_sha256(ident),
           "read_plan_sha256": sm.read_plan_sha256(ident), "end_state": end_state, "per_arm": per_arm, "cells": cells,
           "pauses": [dict(q) for q in pauses],
           "binomial_state": {"trials": sum(x["trials"] for x in cnt["fidelity"].values()),
                              "exceed_tau": sum(x["exceed_tau"] for x in cnt["fidelity"].values()),
                              "evaluations": len(batches), "fires": len(batches)},
           "stop": stop, "cap": {"hour_cap_ms": hour_cap_ms, "used_ms": used,
                                 "hit": hour_cap_ms is not None and used >= hour_cap_ms, "loads_ms": list(loads_ms)},
           "counters": ctr}
    sm.check_report(rep)
    return rep


def _bt_gread_for(camp: Campaign, sm, *, statuses: Mapping | None = None, drop: Sequence[str] = (),
                  layers: Sequence[int] | None = None) -> dict:
    """A G-READ-n artifact bound to the campaign as n-build's probe writes one: the report's shas, every cell of the
    campaign by both shas, the campaign's n package and its capture layers (or ``layers``), one result per kept
    (axis, point) with its merged labels, PASS unless ``statuses`` says otherwise; ``drop``: 'axis|label' results
    left out. Checked by the schema's check_gread."""
    ident = camp.identity
    art = sm.example_gread(statuses=statuses, layers=tuple(ident["capture_layers"] if layers is None else layers))
    kept = {p["label"]: p["merged"] for p in ident["dose_map"]["points"]}
    art["results"] = [dict(r, merged=list(kept[r["dose_label"]])) for r in art["results"]
                      if r["dose_label"] in kept and f"{r['axis']}|{r['dose_label']}" not in drop]
    art["campaign"] = {"read_plan_sha256": sm.read_plan_sha256(ident),
                       "stage_identity_sha256": sm.identity_sha256(ident),
                       "cells": {n: {"json_sha256": c["json_sha256"], "capture_sha256": c["capture_sha256"]}
                                 for n, c in camp.cells.items()}}
    art["probe"]["package_sha256"] = ident["package_sha256"]
    sm.check_gread(art)
    return art


def _bt_dig(d: Any, *keys: Any) -> Any:
    """d[k1][k2]..., or None where a key is missing (a battery check reads a mutant's output without raising)."""
    for k in keys:
        if not isinstance(d, dict) or k not in d:
            return None
        d = d[k]
    return d


def _bt_verdicts(B: _Battery) -> None:
    """The `verdicts` command end to end on written campaigns: a complete campaign (TAU/4-only re-computations, one
    re-computation non-finite on the fresh path alone under an adjudicated pause), write-once, the exposure and
    sensitivity rows, the printed line; a PI-STOP with a pause standing, then adjudicated; a PI-STOP with some arms
    complete; a merged dose map under a Route A lock; the three NOT-RUNs a report derives; one outcome per unit; every
    refusal by its message; G-READ-n's states reaching the tuple; _plain's STOPs; the precheck."""
    import re
    import tempfile
    sm = schema_module()
    dig = _bt_dig
    with tempfile.TemporaryDirectory(prefix="n_anl_vd_") as td:
        base = Path(td)

        def put(name: str, obj: Any, raw: bytes | None = None) -> Path:
            p = base / name
            p.write_bytes(raw if raw is not None else json.dumps(obj).encode("utf-8"))
            return p

        def sha(p: Path) -> str:
            return hashlib.sha256(p.read_bytes()).hexdigest()

        def doc_of(d: Path, name: str = "N-pod_VERDICTS.json") -> dict:
            p = d / name
            return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}

        def run(cd: Path, rp: Path, gp: Path | None, lk: Path, out_: Path, gv: Path | None = None,
                date: str = "2026-12-20") -> tuple[dict | None, str]:
            try:
                return run_verdicts(cd, rp, gp, lk, date, gv, out_), ""
            except (AnlRefusal, AnlStop) as e:
                return None, str(e)[:90]

        def expect(camp_: Campaign, art_: Mapping[str, Any], route: str) -> tuple[dict, dict]:
            g_, auc_, _rows = gread_states(art_, camp_)
            st_, _fig = build_state(camp_, paused={}, gread=g_)
            o_ = outcomes(st_)
            return o_, json.loads(json.dumps(sentence_set_filled(o_, st_, route=route, auc=auc_)))
        lock = put("LOCK-n.md", None, _bt_lock_text())
        lsha = sha(lock)
        # The complete campaign. Re-computed above TAU/4 and not TAU (a fresh shift of 0.015 nats): N1-V's +1 reads of
        # runs 0-39; rand_00's +1 reads of runs 20-39 and its −1 reads of runs 0-19 (so in the TAU/4 row its slope has
        # no common session: the dir_slopes fix, then N1-R tau4-emptied). N1-V's +1 read of run 100 is non-finite on
        # the fresh path alone, under an adjudicated nonfinite pause after which the run resumed.
        shift = {f"N1-V|valence|+1|{session_key(r)}": 0.015 for r in range(40)}
        shift |= {f"N1-R|rand_00|+1|{session_key(r)}": 0.015 for r in range(20, 40)}
        shift |= {f"N1-R|rand_00|-1|{session_key(r)}": 0.015 for r in range(20)}
        fresh_bad = f"N1-V|valence|+1|{session_key(100)}"

        def fresh_nonfinite(cell: dict) -> None:
            for r in cell["records"]:
                if r["read_id"] == fresh_bad:
                    r["fidelity"].update({k: None for k in ("fresh_logprob_S", "fresh_logprob_U", "fresh_margin",
                                                            "fresh_capture_sha16", "fresh_capture_sha16_U", "absdiff",
                                                            "scale", "rel", "exceeds_tau", "exceeds_tau4")},
                                         finite=False)
        cdir = _bt_write_campaign(base / "c", sm, delta=_bt_delta_positive, lock_sha256=lsha, fresh_shift=shift,
                                  mutate=fresh_nonfinite)
        camp = load_campaign(cdir, sm)
        cells_main, cnt_main = _bt_files(cdir)
        li_bad = camp.records[fresh_bad]["launch_index"]
        pz_adj = dict(sm.example_pause(1, kind="nonfinite", launch_index=li_bad, adjudicated=True,
                                       resumed_at=li_bad + 1), read_id=fresh_bad)
        rep_obj = _bt_report_for(camp.identity, cdir, sm, pauses=[pz_adj], label_mass=True)
        rep = put("report.json", rep_obj)
        art_obj = _bt_gread_for(camp, sm)
        art = put("gread.json", art_obj)
        pairs = [f"{x}|{y}" for i, x in enumerate(GVEC_DIRS) for y in GVEC_DIRS[i + 1:]]
        cos_vals = {p: 0.125 * (k + 1) for k, p in enumerate(pairs)}
        gvf = put("gvec.json", {"cosines": cos_vals})
        out = base / "out"
        res, err = run(cdir, rep, art, lock, out, gvf)
        verd = doc_of(out)
        sec = doc_of(out, "N-pod_secondary.json")
        o, sset = expect(camp, art_obj, "B")
        table = [(r.get("label"), r.get("state")) for r in (dig(verd, "gread", "table") or [])]
        ok = {"ran": res is not None,
              "tuple": verd.get("tuple") == list(o["tuple"]) == ["REPLICATED", "DETECTABLE", "SHARED", "PASS", "PASS"]
              and res is not None and res["tuple"] == verd["tuple"],
              "sentences": verd.get("sentences") == sset,
              "bindings": verd.get("lock") == {"name": "LOCK-n.md", "sha256": lsha}
              and verd.get("analyzer_sha256") == analyzer_sha256()
              and verd.get("report") == {"name": "report.json", "sha256": sha(rep), "end_state": "COMPLETE"}
              and dig(verd, "gread", "artifact") == {"name": "gread.json", "sha256": sha(art)}
              and verd.get("proposal_sha256") == PROPOSAL_SHA256 and verd.get("addendum_sha256") == ADDENDUM_SHA256
              and verd.get("date") == "2026-12-20"
              and verd.get("schema_module") == {"path": SCHEMA_REL, "sha256": SCHEMA_SHA256},
              "campaign": verd.get("campaign") == {"stage_identity_sha256": sm.identity_sha256(camp.identity),
                                                   "read_plan_sha256": sm.read_plan_sha256(camp.identity),
                                                   "cells": cells_main},
              "route": verd.get("route") == "B" and ROUTE_TEXT["B"] in (dig(verd, "sentences", "7.1", "text") or ""),
              "auc": dig(verd, "gread", "auc") == {"d_eq": 0.96},
              "gread-table": table == [("+1", "PASS"), ("+1/2", "PASS"), ("d_20", "PASS"), ("d_eq", "PASS"),
                                       (F10, "PASS"), (F20, "PASS")],
              "counters": dig(verd, "counters", "report") == rep_obj["counters"]
              and dig(verd, "counters", "report", "fidelity", "N1-V|+1") == {"trials": 160, "exceed_tau": 0,
                                                                              "exceed_tau4": 40}
              and dig(verd, "counters", "report", "nonfinite_reads") == 1
              and dig(verd, "counters", "records", "N1-V|+1", "fidelity exceedances at TAU/4") == 40
              and dig(verd, "counters", "records", "N1-V|+1", "non-finite re-computations") == 1
              and dig(verd, "counters", "pauses") == [pz_adj]
              and dig(verd, "counters", "cap", "used_ms") == cnt_main["used_ms"]
              and dig(verd, "counters", "cap", "loads_ms") == rep_obj["cap"]["loads_ms"] == [5000],
              "secondary": sec.get("schema") == SECONDARY_SCHEMA and str(sec.get("claim")).startswith("none")
              and "a_first_pick_share" in (sec.get("secondaries") or {})
              and verd.get("secondary") == {"name": "N-pod_secondary.json",
                                            "sha256": sha(out / "N-pod_secondary.json") if sec else None},
              "cosines": verd.get("cosines") == sec.get("cosines") == {"source": {"name": "gvec.json",
                                                                                  "sha256": sha(gvf)},
                                                                       "values": cos_vals}
              and dig(sec, "secondaries", "e_directions", "cosines") == cos_vals,
              "outputs": res is not None and [(n, h) for n, h, _s in res["outputs"]]
              == [("N-pod_secondary.json", "written"), ("N-pod_VERDICTS.json", "written")]
              and all(s == sha(out / n) for n, _h, s in res["outputs"])}
        B.chk("verdicts on a complete campaign (an adjudicated pause in it) writes the secondary DVs and VERDICTS: the "
              "tuple and the filled sentences those of the reader path under the artifact's states, every input bound "
              "by sha256 (the secondary by its own), the route read from the lock, the dose sentence's AUC from the "
              "artifact, the G-READ-n table's six rows, the report's counters and n §4's, the cosines in both",
              all(ok.values()), [k for k, v in ok.items() if not v] or verd.get("tuple") or err, cover=["VD-COMPLETE"])
        res2, _e2 = run(cdir, rep, art, lock, out, gvf)
        r3 = _bt_raises(lambda: run_verdicts(cdir, rep, art, lock, "2026-12-21", gvf, out), (AnlRefusal,))
        wa = base / "wa"
        wa.mkdir()
        (wa / "b.json").write_text("old\n", encoding="utf-8")
        r_wa = _bt_raises(lambda: write_all_once([(wa / "a.json", "new a\n"), (wa / "b.json", "new b\n")]),
                          (AnlRefusal,))
        # the pair through verdicts: VERDICTS of another date present and no secondary; refused, nothing written
        out_p = base / "out_pair"
        run(cdir, rep, art, lock, out_p, gvf)
        (out_p / "N-pod_secondary.json").unlink()
        r_pair = _bt_raises(lambda: run_verdicts(cdir, rep, art, lock, "2026-12-21", gvf, out_p), (AnlRefusal,))
        B.chk("verdicts is write-once: the same inputs again leave identical bytes; another date refuses; with two "
              "outputs, the second existing with other bytes refuses before the first is written, directly and "
              "through verdicts (VERDICTS present, the secondary absent: no secondary written)",
              res2 is not None and [h for _n, h, _s in res2["outputs"]] == ["identical", "identical"] and r3[0]
              and "write-once" in r3[1] and r_wa[0] and "b.json exists with other bytes" in r_wa[1]
              and not (wa / "a.json").exists() and r_pair[0] and "N-pod_VERDICTS.json exists with other bytes"
              in r_pair[1] and not (out_p / "N-pod_secondary.json").exists(),
              (res2 and res2["outputs"], r3[1][:60], r_wa[1][:60], r_pair[1][:60]), cover=["VD-WRITE-ONCE"])
        ex = verd.get("exposure") or {}
        B.chk("verdicts reports §0.4's exposure realised (PIN-n-23): 160 N1-V and 160 N1-P reads at −1 (negative "
              "valenced), 960 N1-R (negative random), each re-computed fresh",
              ex.get("N1-V") == {"class": "negative valenced", "planned": 160, "reads": 160,
                                 "fresh_recomputations": 160}
              and dig(ex, "N1-P", "reads") == 160 and ex.get("N1-R") == {"class": "negative random", "planned": 960,
                                                                       "reads": 960, "fresh_recomputations": 960}
              and dig(ex, "totals", "negative valenced") == 320 and dig(ex, "totals", "negative random") == 960, ex,
              cover=["VD-EXPOSURE"])
        g_m, _a, _r = gread_states(art_obj, camp)
        st_s, _fs = build_state(camp, paused={}, gread=g_m, drop=tau4_drop(camp))
        sens = verd.get("sensitivity") or {}
        ds = dig(sens, "figures", "per_arm", "dir_slopes") or {}
        ok_s = {"shift TAU/4 only": all(camp.records[r]["fidelity"]["exceeds_tau4"] is True
                                        and camp.records[r]["fidelity"]["exceeds_tau"] is False for r in shift),
                "tuple": sens.get("tuple") == list(outcomes(st_s)["tuple"]) and sens.get("tuple") != verd.get("tuple")
                and sens.get("tuple") == ["INDETERMINATE", "INDETERMINATE", "SHARED", "PASS", "PASS"]
                and all(v == [] for (a, _k), v in st_s.at.items() if a == "N1-R"),
                "n": dig(verd, "figures", "per_arm", "n", "N1-V|+1") == 160
                and dig(sens, "figures", "per_arm", "n", "N1-V|+1") == 120
                and dig(sens, "figures", "per_arm", "n", "N1-V|+1/2") == 160,
                "emptied": dig(sens, "figures", "unusable", "N1-R") == "tau4-emptied" and "rand_00" in ds
                and ds["rand_00"] is None and isinstance(ds.get("rand_01"), float)}
        B.chk("verdicts reports the TAU/4 sensitivity row (PIN-n-16) beside the primary: 40 N1-V reads at +1 dropped "
              "(n 120 against the primary's 160), rand_00 left with no common session (its slope null, no NaN), so "
              "N1-R tau4-emptied and the row's N1 INDETERMINATE, its points usable, so N2 decided (INDETERMINATE, "
              "INDETERMINATE, SHARED, PASS, PASS: PIN-n-36); its tuple the reader path's under the filter",
              all(ok_s.values()), [k for k, v in ok_s.items() if not v] or sens.get("tuple"), cover=["VD-SENSITIVITY"])
        line = verdicts_line(res) if res is not None else ""
        B.chk("verdicts prints one line and no margin (§4 'Blinding'): the tuple, and each output's name, how and "
              "sha256", re.fullmatch(r"VERDICTS: \(REPLICATED, DETECTABLE, SHARED, PASS, PASS\) -> "
                                     r"N-pod_secondary\.json \(written; sha256 [0-9a-f]{64}\); "
                                     r"N-pod_VERDICTS\.json \(written; sha256 [0-9a-f]{64}\)", line) is not None,
              line[:100], cover=["VD-STDOUT"])
        # PI-STOP with a pause standing on the last read (N4-Ts, non-finite), every arm complete; then that pause
        # adjudicated, under COMPLETE
        last = f"N4-Ts|none|0|{session_key(159)}"
        cdir2 = _bt_write_campaign(base / "c2", sm, delta=_bt_delta_positive, lock_sha256=lsha, nonfinite=[last])
        camp2 = load_campaign(cdir2, sm)
        li = camp2.records[last]["launch_index"]
        stop_pi = {"kind": "PI-STOP", "record_sha256": "7" * 64, "detail": "the PI stopped the unit"}
        pz = dict(sm.example_pause(1, kind="nonfinite", launch_index=li, arms=("N4-Ts",)), read_id=last)
        rep2 = put("report_pistop.json", _bt_report_for(camp2.identity, cdir2, sm, end_state="PI-STOP", pauses=[pz],
                                                        stop=stop_pi))
        art2 = put("gread2.json", _bt_gread_for(camp2, sm))
        run(cdir2, rep2, art2, lock, base / "out2")
        v2 = doc_of(base / "out2")
        pz_done = dict(pz, adjudicated=True, ruling_sha256="f" * 64)
        run(cdir2, put("report_adj.json", _bt_report_for(camp2.identity, cdir2, sm, pauses=[pz_done])), art2, lock,
            base / "out2b")
        v2b = doc_of(base / "out2b")
        B.chk("verdicts under PI-STOP with a pause standing on N4-Ts analyzes the unit (PIN-n-24): N1, dose and N2 "
              "decided, N4 INDETERMINATE by pause:N4-Ts, then nonfinite:N4-Ts; the same pause adjudicated (COMPLETE) "
              "stands no more: nonfinite:N4-Ts alone",
              (v2.get("tuple") or [])[:4] == ["REPLICATED", "DETECTABLE", "SHARED", "INDETERMINATE"]
              and dig(v2, "outcomes", "N4", "causes") == ["pause:N4-Ts", "nonfinite:N4-Ts"]
              and (v2b.get("tuple") or [])[:4] == ["REPLICATED", "DETECTABLE", "SHARED", "INDETERMINATE"]
              and dig(v2b, "outcomes", "N4", "causes") == ["nonfinite:N4-Ts"],
              (v2.get("tuple"), dig(v2, "outcomes", "N4", "causes"), dig(v2b, "outcomes", "N4", "causes")),
              cover=["VD-PISTOP-STANDING"])
        # PIN-n-33 as amended and PIN-n-37: standing batches, each bound as the runner counts a batch (report_problems
        # binds it; it binds a batch, not its fire, and the fires here are not ones the runner would write), under
        # PI-STOP (the v5 review's B3, B6). A, on a campaign with one N1-P −1 read above TAU (ck): a fire adjudicated
        # at N1-P's last +1 read, then the run's-end batch from the next trial (N1-P's first −1 read: its +d_20 and
        # +d_eq carry none) to the stage's last (N4-Ts's), k = 1, standing on N1-P at −1 (N4's arms per arm), so N2
        # decided. C: the same clear on c2, then the non-finite read at m − 1 also firing the binomial, its batch from
        # the same trial to that read: the same point. B, on the main campaign: the run's-end batch from the stage's
        # first trial, its 80 reads above TAU/4 not counted (k = 0), its re-computation non-finite on the fresh path a
        # trial: through every shadow it stands on every read of its scope's steered arms, so N2 INDETERMINATE.
        def trials_of(c: Campaign) -> list[int]:
            return sorted(r["launch_index"] for r in c.records.values() if r["fidelity"] is not None)

        def batch_of(c: Campaign, lo: int, hi: int) -> tuple[dict, list]:
            ins = [r for r in c.records.values() if r["fidelity"] is not None and lo <= r["launch_index"] <= hi]
            return ({"first_launch_index": lo, "last_launch_index": hi, "n": len(ins),
                     "k": sum(r["fidelity"]["exceeds_tau"] is True for r in ins)}, sorted({r["arm"] for r in ins}))

        def clear_and_end(c: Campaign, end_read: str | None = None) -> list[dict]:
            tl = trials_of(c)
            l1 = max(r["launch_index"] for rid, r in c.records.items() if rid.startswith("N1-P|valence|+1|"))
            p1 = sm.example_pause(1, kind="fidelity-binomial", launch_index=l1, adjudicated=True, resumed_at=l1 + 1)
            f1, a1 = batch_of(c, tl[0], l1)
            p1.update(read_id=next(rid for rid, r in c.records.items() if r["launch_index"] == l1), arms_in_scope=a1)
            p1["binomial"].update(f1)
            hi = tl[-1] if end_read is None else c.records[end_read]["launch_index"]
            p2 = (sm.example_pause(2, kind="fidelity-binomial", launch_index=None) if end_read is None else
                  dict(sm.example_pause(2, kind="nonfinite", launch_index=hi, also_fired=("fidelity-binomial",)),
                       read_id=end_read))
            f2, a2 = batch_of(c, next(i for i in tl if i > l1), hi)
            p2["binomial"].update(f2)
            p2["arms_in_scope"] = sorted(set(a2) | ({end_read.split("|")[0]} if end_read else set()))
            return [p1, p2]
        hot = f"N1-P|valence|-1|{session_key(5)}"
        cdir_k = _bt_write_campaign(base / "ck", sm, delta=_bt_delta_positive, lock_sha256=lsha,
                                    fresh_shift={hot: 2.0})
        camp_k = load_campaign(cdir_k, sm)
        art_k = put("g_k.json", _bt_gread_for(camp_k, sm))
        pa = clear_and_end(camp_k)
        run(cdir_k, put("report_pa.json", _bt_report_for(camp_k.identity, cdir_k, sm, end_state="PI-STOP", pauses=pa,
                                                         stop=stop_pi)), art_k, lock, base / "out_pa")
        va = doc_of(base / "out_pa")
        pc = clear_and_end(camp2, end_read=last)
        run(cdir2, put("report_pc.json", _bt_report_for(camp2.identity, cdir2, sm, end_state="PI-STOP", pauses=pc,
                                                        stop=stop_pi)), art2, lock, base / "out_pc")
        vc = doc_of(base / "out_pc")
        tl_m = trials_of(camp)
        fb, ab = batch_of(camp, tl_m[0], tl_m[-1])
        pb = sm.example_pause(2, kind="fidelity-binomial", launch_index=None)
        pb["binomial"].update(fb)
        pb["arms_in_scope"] = ab
        run(cdir, put("report_pb.json", _bt_report_for(camp.identity, cdir, sm, end_state="PI-STOP",
                                                       pauses=[pz_adj, pb], stop=stop_pi, label_mass=True)),
            art, lock, base / "out_pb")
        vb = doc_of(base / "out_pb")
        n1pts = sorted(f"{a}@{lab_}" for a in ("N1-V", "N1-R", "N1-P")
                       for lab_ in ("+1", "+1/2", "+d_20", "+d_eq", "-1") if not (a == "N1-P" and lab_ == "+1/2"))
        ok_pp = {"A": (va.get("tuple") or [])[:4] == ["INDETERMINATE", "INDETERMINATE", "SHARED", "INDETERMINATE"]
                 and pa[-1]["binomial"]["k"] == 1 and dig(va, "outcomes", "N1", "causes") == ["pause:N1-P"]
                 and (dig(va, "outcomes", "N4", "causes") or [])[:2] == ["pause:N4-T", "pause:N4-Ts"]
                 and dig(va, "figures", "pause_points") == ["N1-P@-1"]
                 and (dig(va, "sensitivity", "tuple") or [])[:3] == ["INDETERMINATE", "INDETERMINATE", "SHARED"]
                 and dig(va, "sensitivity", "figures", "pause_points") == ["N1-P@-1"],
                 "C": (vc.get("tuple") or [])[:3] == ["INDETERMINATE", "INDETERMINATE", "SHARED"]
                 and dig(vc, "outcomes", "N1", "causes") == ["pause:N1-P"]
                 and dig(vc, "figures", "pause_points") == ["N1-P@-1"],
                 "B": (fb["k"], fb["n"]) == (0, len(tl_m)) and dig(vb, "outcomes", "N2", "state") == "INDETERMINATE"
                 and dig(vb, "outcomes", "N2", "causes") == ["pause:N1-V", "pause:N1-R", "pause:N1-P"]
                 and dig(vb, "figures", "pause_points") == n1pts and len(n1pts) == 14}
        B.chk("verdicts under PI-STOP with a standing batch, bound as the runner counts a batch (PIN-n-33 as amended, "
              "PIN-n-37): A, after a "
              "fire adjudicated at N1-P's last +1 read, the run's-end batch from N1-P's first −1 read to the stage's "
              "last trial, k = 1, stands on N1-P at −1 alone: N1, dose and N4 INDETERMINATE (pause:N1-P; pause:N4-T, "
              "pause:N4-Ts, per arm), N2 decided, SHARED, in the primary and the TAU/4 row, the figures naming the "
              "point; C, the same clear, then a non-finite read at m − 1 that also fires the binomial: N1 and N2 the "
              "same, and the same point; B, "
              "the run's-end batch from the stage's first trial (its 80 reads above TAU/4 not counted, k = 0; its "
              "re-computation non-finite on the fresh path a trial): through every shadow it stands on all 14 points "
              "of N1-V, N1-R and N1-P, so N2 INDETERMINATE (pause:N1-V, pause:N1-R, pause:N1-P)",
              all(ok_pp.values()), [k for k, v in ok_pp.items() if not v] or (va.get("tuple"), vc.get("tuple")),
              cover=["VD-PAUSE-POINTS"])
        # PI-STOP with some arms complete: N1-P without its −1 reads, N4-Ts with none
        cdir4 = _bt_write_campaign(base / "c4", sm, delta=_bt_delta_positive, lock_sha256=lsha,
                                   omit=[("N1-P", "valence", "-1"), ("N4-Ts", "none", "0")])
        camp4 = load_campaign(cdir4, sm)
        art4_obj = _bt_gread_for(camp4, sm)
        r4, err4 = run(cdir4, put("report_some.json", _bt_report_for(camp4.identity, cdir4, sm, end_state="PI-STOP",
                                                                     stop=stop_pi)),
                       put("gread4.json", art4_obj), lock, base / "out4")
        v4 = doc_of(base / "out4")
        o4, _s4 = expect(camp4, art4_obj, "B")
        ex4 = v4.get("exposure") or {}
        B.chk("verdicts under PI-STOP with some arms complete analyzes the unit (§5: a locked unit that completes any "
              "arm is analyzed): N1 and N4 INDETERMINATE by their incomplete arms, the tuple the reader path's; the "
              "exposure row counts the −1 reads alone: N1-P 0 of 160, the negative valenced total N1-V's 160",
              r4 is not None and r4["tuple"] == v4.get("tuple") == list(o4["tuple"])
              and v4["tuple"][0] == v4["tuple"][3] == "INDETERMINATE"
              and not (base / "out4" / "N-pod_NOT-RUN.json").exists()
              and ex4.get("N1-P") == {"class": "negative valenced", "planned": 160, "reads": 0,
                                      "fresh_recomputations": 0}
              and dig(ex4, "N1-V", "reads") == 160 and dig(ex4, "totals", "negative valenced") == 160,
              (v4.get("tuple"), ex4.get("N1-P"), dig(ex4, "totals", "negative valenced"), err4),
              cover=["VD-SOME-ARMS"])
        # the v5 review's B4: a rendering pause standing at m whose read is planned and not on disk (N1-P's first −1
        # read, its cell omitted), under PI-STOP: accepted, and standing on N1-P at −1 by its id (PIN-n-37)
        pr4 = dict(sm.example_pause(1, kind="rendering", launch_index=len(camp4.records), arms=("N1-P",)),
                   read_id=f"N1-P|valence|-1|{session_key(0)}")
        r4r, err4r = run(cdir4, put("report_rend.json", _bt_report_for(camp4.identity, cdir4, sm, end_state="PI-STOP",
                                                                       pauses=[pr4], stop=stop_pi)),
                         base / "gread4.json", lock, base / "out4r")
        v4r = doc_of(base / "out4r")
        B.chk("verdicts under PI-STOP with a rendering pause standing at m, its read planned and not on disk (N1-P's "
              "first −1 read, the cell omitted): accepted (its read is the plan's), the pause standing on N1-P at −1 "
              "by its id (PIN-n-37; the figures list it), N1 INDETERMINATE (pause:N1-P, then incomplete:N1-P), N2 "
              "decided, SHARED",
              r4r is not None and dig(v4r, "figures", "pause_points") == ["N1-P@-1"]
              and (v4r.get("tuple") or [None] * 3)[2] == "SHARED"
              and dig(v4r, "outcomes", "N1", "causes") == ["pause:N1-P", "incomplete:N1-P"],
              (err4r, v4r.get("tuple"), dig(v4r, "figures", "pause_points")), cover=["VD-PAUSE-RENDERING"])
        # a merged dose map (R_ell 40.0: +d_20 into +1, +d_eq into +1/2) under a Route A lock, FAIL at +1/2
        lk_a = put("LOCK-A.md", None, _bt_lock_text(route="A"))
        cdir5 = _bt_write_campaign(base / "c5", sm, R_ell=40.0, delta=_bt_delta_positive, lock_sha256=sha(lk_a))
        camp5 = load_campaign(cdir5, sm)
        art5_obj = _bt_gread_for(camp5, sm, statuses={"valence|+1/2": "FAIL"})
        r5, err5 = run(cdir5, put("report5.json", _bt_report_for(camp5.identity, cdir5, sm)),
                       put("gread5.json", art5_obj), lk_a, base / "out5")
        v5 = doc_of(base / "out5")
        o5, s5 = expect(camp5, art5_obj, "A")
        merged5 = {r["dose_label"]: r["merged"] for r in art5_obj["results"] if r["axis"] == "valence"}
        B.chk("verdicts on a merged dose map (R_ell 40.0) under a Route A lock: the artifact's results at the kept "
              "points, listing the labels merged into them, are accepted; the tuple's G-READ-n coordinate is d_eq's, "
              "read at +1/2 (FAIL there: FAIL, AUC 0.62); N1's sentence names their direction",
              merged5 == {"+1": ["+d_20"], "+1/2": ["+d_eq"]} and r5 is not None
              and r5["tuple"] == v5.get("tuple") == list(o5["tuple"]) and v5["tuple"][4] == "FAIL"
              and dig(v5, "gread", "auc") == {"d_eq": 0.62} and v5.get("route") == "A" and v5.get("sentences") == s5
              and ROUTE_TEXT["A"] in (dig(v5, "sentences", "7.1", "text") or ""),
              (v5.get("tuple"), dig(v5, "gread", "auc"), v5.get("route"), err5), cover=["VD-MERGED-ROUTE-A"])
        # the NOT-RUNs a report derives: no arm complete before the cap, a PI-STOP, a G-VER-STOP
        keep = {("N1-V", "none", "0"), ("N1-V", "valence", "+1")}
        omit = [(arm, d_, lab) for arm, rows in PLAN_TABLE.items() for dirs, labels in rows for d_ in dirs
                for lab in labels if (arm, d_, lab) not in keep]
        cdir3 = _bt_write_campaign(base / "c3", sm, delta=_bt_delta_positive, lock_sha256=lsha, omit=omit)
        camp3 = load_campaign(cdir3, sm)
        used3 = _bt_files(cdir3)[1]["used_ms"]
        rc3 = _bt_report_for(camp3.identity, cdir3, sm, end_state="CAP", hour_cap_ms=used3)
        rep_cap = put("report_cap.json", rc3)
        rep_pis = put("report_pis.json", _bt_report_for(camp3.identity, cdir3, sm, end_state="PI-STOP", stop=stop_pi))
        empty = base / "empty"
        empty.mkdir()
        stop_gv = {"kind": "G-VER-STOP", "record_sha256": "6" * 64, "detail": "G-VER: a session's tokens differ"}
        rep_gv = put("report_gver.json", _bt_report_for(camp.identity, None, sm, end_state="G-VER-STOP",
                                                        stop=stop_gv))
        nr = {}
        for k, (cd, rp) in {"cap": (cdir3, rep_cap), "pi-stop": (cdir3, rep_pis), "gver-stop": (empty, rep_gv)}.items():
            rr, _er = run(cd, rp, None, lock, base / f"out_{k}")
            doc = doc_of(base / f"out_{k}", "N-pod_NOT-RUN.json")
            nr[k] = (rr and rr["tuple"], doc.get("cause"), dig(doc, "record", "sha256") == sha(rp), doc.get("date"),
                     dig(doc, "record", "derived_from"), dig(doc, "record", "end_state"),
                     dig(doc, "record", "stop_record_sha256"), doc.get("lock") == {"name": "LOCK-n.md", "sha256": lsha},
                     doc.get("schema_module") == {"path": SCHEMA_REL, "sha256": SCHEMA_SHA256})
        want = {k: (NOT_RUN, f"no-arm:{k}", True, "2026-12-20", "the stage report", e, s, True, True)
                for k, e, s in (("cap", "CAP", None), ("pi-stop", "PI-STOP", "7" * 64),
                                ("gver-stop", "G-VER-STOP", "6" * 64))}
        B.chk("verdicts derives N-pod's NOT-RUN where no arm is complete: before the cap (no-arm:cap), a PI stop "
              "(no-arm:pi-stop) and a G-VER STOP with no record (no-arm:gver-stop), each bound to its report, its end "
              "state, the STOP's record, the lock and the schema module",
              nr == want, nr, cover=["VD-NOTRUN-CAP", "VD-NOTRUN-PISTOP", "VD-NOTRUN-GVER"])
        # one outcome per unit
        rec_clock = {"schema": NOT_RUN_RECORD_SCHEMA, "unit": UNIT, "cause": "clock:pi-declined", "date": "2026-12-16",
                     "detail": "a synthetic record"}
        one = {"verdicts beside a NOT-RUN": (_bt_raises(lambda: run_verdicts(cdir, rep, art, lock, "2026-12-20", None,
                                                                             base / "out_cap"), (AnlRefusal,)),
                                             "already in the output directory"),
               "a derived NOT-RUN beside VERDICTS": (_bt_raises(lambda: run_verdicts(cdir3, rep_cap, None, lock,
                                                                                     "2026-12-20", None, out),
                                                                (AnlRefusal,)), "already in the output directory"),
               "not-run beside VERDICTS": (_bt_raises(lambda: run_not_run(put("rec_clock.json", rec_clock), out),
                                                      (AnlRefusal,)), "already in the output directory"),
               "not-run on a no-arm cause": (_bt_raises(lambda: run_not_run(
                   put("rec_noarm.json", dict(rec_clock, cause="no-arm:cap")), base / "out_noarm"), (AnlRefusal,)),
                   "takes a Clock cause")}
        bad1 = {k: m[:70] for k, ((okr, m), want_m) in one.items() if not (okr and want_m in m)}
        B.chk("one outcome per unit (§5): verdicts refuses beside a NOT-RUN; a derived NOT-RUN and not-run refuse "
              "beside VERDICTS; not-run takes a Clock cause only (a no-arm NOT-RUN is derived from the stage report)",
              not bad1 and not (base / "out_cap" / "N-pod_VERDICTS.json").exists()
              and not (out / "N-pod_NOT-RUN.json").exists() and not (base / "out_noarm").exists(), bad1,
              cover=["VD-ONE-OUTCOME"])
        # refusals, each by its message
        def rv(cd: Path, rp: Path, gp: Path | None = art, lk: Path = lock, date: str = "2026-12-20",
               gv: Path | None = None) -> tuple[bool, str]:
            return _bt_raises(lambda: run_verdicts(cd, rp, gp, lk, date, gv, base / "out_refused"), (AnlRefusal,))

        def report_with(**over: Any) -> Path:
            obj = json.loads(json.dumps(rep_obj))
            for k, v in over.items():
                obj[k] = v
            return put(f"rep_{len(list(base.glob('rep_*')))}.json", obj)

        def counters_with(**over: Any) -> dict:
            return dict(json.loads(json.dumps(rep_obj["counters"])), **over)

        def on_main(name: str, pauses: Sequence[dict], **kw: Any) -> Path:
            return put(name, _bt_report_for(camp.identity, cdir, sm, pauses=pauses, **kw))
        r_cells = json.loads(json.dumps(rep_obj["cells"]))
        r_cells[sorted(r_cells)[0]]["json_sha256"] = "1" * 64
        ident_pod = dict(camp.identity, pod_id="another-pod")
        per_lie = json.loads(json.dumps(rep_obj["per_arm"]))
        per_lie["N2-C"]["complete"] = False
        cnt = json.loads(json.dumps(rep_obj["counters"]))
        cnt["fidelity"]["N1-V|+1"]["exceed_tau4"] += 1
        rc3_cells = json.loads(json.dumps(rc3))
        rc3_cells["cells"][sorted(rc3_cells["cells"])[0]]["json_sha256"] = "1" * 64
        rc3_arm = json.loads(json.dumps(rc3))
        rc3_arm["per_arm"]["N1-V"]["complete"] = True
        # the v5 review's B7: bz and rs name a read of the plan not on disk (N1-P's −1 cell, omitted from c4)
        bz = sm.example_pause(1, kind="fidelity-binomial", launch_index=500, adjudicated=True, resumed_at=501,
                              arms=("N1-P",))
        bz["binomial"]["k"] = 0
        bz["read_id"] = f"N1-P|valence|-1|{session_key(3)}"
        rid3 = f"N1-V|valence|+1|{session_key(3)}"
        L3 = camp.records[rid3]["launch_index"]
        L0 = camp.records[f"N1-V|none|0|{session_key(3)}"]["launch_index"]
        rz = dict(sm.example_pause(1, kind="rendering", launch_index=L3, adjudicated=True), read_id=rid3)
        kz = dict(sm.example_pause(1, kind="nonfinite", launch_index=L3, adjudicated=True, resumed_at=L3 + 1),
                  read_id=rid3)
        iz = dict(sm.example_pause(1, kind="identity-bound", launch_index=L0, adjudicated=True, resumed_at=L0 + 1),
                  read_id=f"N1-V|none|0|{session_key(3)}")
        rs = dict(sm.example_pause(1, kind="rendering", launch_index=len(camp4.records) + 2, arms=("N1-P",)),
                  read_id=f"N1-P|valence|-1|{session_key(3)}")
        rn = dict(pz_adj, resumed_at_launch_index=len(camp.records) + 100)
        rid_early = next(r for r, x in camp2.records.items() if x["launch_index"] == li - 5)
        pz_early = dict(pz, read_id=rid_early, launch_index=li - 5, arms_in_scope=[rid_early.split("|")[0]])
        lk_other = put("LOCK-other.md", None, _bt_lock_text(route="A"))
        lk_noan = put("LOCK-noan.md", None, _bt_lock_text(names_analyzer=False))
        lk_noroute = put("LOCK-noroute.md", None, _bt_lock_text(route=None))
        lk_two = put("LOCK-two.md", None, _bt_lock_text(routes=2))
        lk_c = put("LOCK-c.md", None, _bt_lock_text(route="C"))
        lk_v09 = put("LOCK-v09.md", None, _bt_lock_text(v10=False))

        def gver_with(lk: Path) -> Path:
            ident_l = dict(camp.identity, lock_sha256=sha(lk))
            return put(f"gv_{lk.stem}.json", _bt_report_for(ident_l, None, sm, end_state="G-VER-STOP", stop=stop_gv))
        art_plan = json.loads(json.dumps(art_obj))
        art_plan["campaign"]["read_plan_sha256"] = "a" * 64
        art_ident = json.loads(json.dumps(art_obj))
        art_ident["campaign"]["stage_identity_sha256"] = "b" * 64
        art_cap = json.loads(json.dumps(art_obj))
        cap0 = art_cap["campaign"]["cells"][sorted(art_cap["campaign"]["cells"])[0]]["capture_sha256"]
        cap0[sorted(cap0)[0]] = "3" * 64                                    # one layer's row hash differs
        art_json = json.loads(json.dumps(art_obj))
        art_json["campaign"]["cells"][sorted(art_json["campaign"]["cells"])[-1]]["json_sha256"] = "3" * 64
        art_less = json.loads(json.dumps(art_obj))
        del art_less["campaign"]["cells"][sorted(art_less["campaign"]["cells"])[-1]]
        art_pkg = json.loads(json.dumps(art_obj))
        art_pkg["probe"]["package_sha256"] = "5" * 64 if camp.identity["package_sha256"] != "5" * 64 else "6" * 64
        art_merged = json.loads(json.dumps(art_obj))
        next(r for r in art_merged["results"] if r["dose_label"] == "+1")["merged"] = ["+d_20"]
        dm_m = dict(camp.identity["dose_map"])
        dm_m["points"] = [p for p in dm_m["points"] if p["label"] != "+d_eq"]
        notkept = gread_problems(art_obj, replace(camp, identity=dict(camp.identity, dose_map=dm_m)), rep_obj)
        five = dict(list(cos_vals.items())[:5])
        refs = {
            "date": (rv(cdir, rep, date="20261220"), "ISO calendar date"),
            "schema-report": (rv(cdir, report_with(end_state="DONE")),
                              "the stage report: SchemaError at report.end_state"),
            "schema-gread": (rv(cdir, rep, put("g_bar.json", dict(art_obj, probe=dict(art_obj["probe"], bar=0.5)))),
                             "G-READ-n's artifact: SchemaError at gread.probe"),
            "pause": (rv(cdir, put("rep_pause.json", _bt_report_for(
                camp.identity, cdir, sm, end_state="PAUSE", pauses=[sm.example_pause(1, kind="rendering")]))), "PAUSE"),
            "not-campaign": (rv(cdir, put("rep_time.json", sm.example_report(
                sm.example_identity("time"), end_state="CAP", hour_cap_ms=1000, used_ms=1000))), "not a campaign"),
            "lock-other": (rv(cdir, rep, lk=lk_other), "lock_sha256"),
            "lock-analyzer": (rv(empty, gver_with(lk_noan), None, lk_noan), "does not name this analyzer"),
            "lock-version": (rv(empty, gver_with(lk_v09), None, lk_v09), "does not say it is LOCK-n v1.0"),
            "lock-no-route": (rv(empty, gver_with(lk_noroute), None, lk_noroute), "direction of record"),
            "lock-two-routes": (rv(empty, gver_with(lk_two), None, lk_two), "direction of record"),
            "lock-route-C": (rv(empty, gver_with(lk_c), None, lk_c), "direction of record"),
            "cells": (rv(cdir, report_with(cells=r_cells)), "not the files on disk"),
            "identity": (rv(cdir, report_with(stage_identity=ident_pod,
                                              stage_identity_sha256=sm.identity_sha256(ident_pod))),
                         "stage identity is not the cells'"),
            # a per-arm lie the schema's per_arm rule refuses first (complete is obtained == planned): report_problems'
            # own per-arm check cannot fire alone (round-2 M08, equivalent)
            "per-arm": (rv(cdir, report_with(per_arm=per_lie, end_state="PI-STOP", stop=stop_pi)),
                        "SchemaError at report.per_arm.N2-C"),
            "per-arm-no-arm": (rv(cdir3, put("rep_c3_arm.json", rc3_arm), None), "SchemaError at report.per_arm.N1-V"),
            "cells-no-arm": (rv(cdir3, put("rep_c3_cells.json", rc3_cells), None), "not the files on disk"),
            "counters": (rv(cdir, report_with(counters=cnt)), "counters.fidelity"),
            "nonfinite-count": (rv(cdir, report_with(counters=counters_with(nonfinite_reads=2))),
                                "counters.nonfinite_reads"),
            "oob-count": (rv(cdir, report_with(counters=counters_with(identity_out_of_bound=1))),
                          "counters.identity_out_of_bound"),
            "label-mass": (rv(cdir, report_with(counters=counters_with(label_mass_below_floor={"N1-V|+1": 1}))),
                           "counters.label_mass_below_floor"),
            "cap-used": (rv(cdir, report_with(cap={"hour_cap_ms": None, "used_ms": cnt_main["used_ms"] + 1,
                                                   "hit": False, "loads_ms": [5000]})), "cap.used_ms"),
            "pause-read": (rv(cdir4, put("rep_bz.json", _bt_report_for(camp4.identity, cdir4, sm, end_state="PI-STOP",
                                                                       pauses=[bz], stop=stop_pi)),
                              base / "gread4.json"), "is not on disk"),
            "rendering-on-disk": (rv(cdir, on_main("rep_rz.json", [rz])), "a rendering pause not resumed"),
            "kind-nonfinite": (rv(cdir, on_main("rep_kz.json", [kz])), "a non-finite pause at a finite read"),
            "kind-identity": (rv(cdir, on_main("rep_iz.json", [iz], counters_over={"identity_out_of_bound": 1})),
                              "an identity-bound pause at a read within the bound"),
            "resumed-nowhere": (rv(cdir, on_main("rep_rn.json", [rn])), "resumed where no read was launched"),
            "standing-not-last": (rv(cdir4, put("rep_snl.json", _bt_report_for(camp4.identity, cdir4, sm,
                                                                              end_state="PI-STOP", pauses=[rs],
                                                                              stop=stop_pi)),
                                     base / "gread4.json"), "not the stage's last event"),
            "standing-later": (rv(cdir2, put("rep_early.json", _bt_report_for(
                camp2.identity, cdir2, sm, end_state="PI-STOP", pauses=[pz_early], stop=stop_pi)), art2),
                "launched after this standing pause"),
            "gread-missing": (rv(cdir, rep, None), "--gread"),
            "gread-plan": (rv(cdir, rep, put("g_plan.json", art_plan)), "plan or identity sha256"),
            "gread-identity": (rv(cdir, rep, put("g_ident.json", art_ident)), "plan or identity sha256"),
            "gread-capture": (rv(cdir, rep, put("g_cap.json", art_cap)), "not the campaign's files"),
            "gread-json": (rv(cdir, rep, put("g_json.json", art_json)), "not the campaign's files"),
            "gread-cells-missing": (rv(cdir, rep, put("g_less.json", art_less)), "not the campaign's files"),
            "gread-package": (rv(cdir, rep, put("g_pkg.json", art_pkg)), "another n package"),
            "gread-layers": (rv(cdir, rep, put("g_layers.json", _bt_gread_for(camp, sm, layers=(63,)))),
                             "capture layers"),
            "gread-merged": (rv(cdir, rep, put("g_merged.json", art_merged)), "merged; the dose map"),
            "gread-not-kept": ((bool(notkept), "; ".join(notkept)), "a point the dose map does not keep"),
            "cosines": (rv(cdir, rep, gv=put("cos.json", {"cosines": {"a|b": "x"}})), "cosines"),
            "cosines-five": (rv(cdir, rep, gv=put("cos5.json", {"cosines": five})), "the six pairs"),
            "dir-not-empty": (rv(cdir, rep_gv, None), "not empty"),
        }

        def gap(cell: dict) -> None:
            if cell["arm"] == "N4-Ts" and cell["dose_label"] == "0":
                cell["records"][-1]["launch_index"] += 5
        cdir_gap = _bt_write_campaign(base / "cgap", sm, delta=_bt_delta_positive, lock_sha256=lsha, mutate=gap)
        camp_gap = load_campaign(cdir_gap, sm)
        refs["launch-gap"] = (rv(cdir_gap, put("rep_gap.json", _bt_report_for(camp_gap.identity, cdir_gap, sm)),
                                 put("g_gap.json", _bt_gread_for(camp_gap, sm))), "launch indices are not exactly")
        p2 = sm.example_pause(2, kind="fidelity-binomial", launch_index=None, arms=("N1-V",))
        p2["binomial"]["k"] = 0
        refs["two-standing"] = (rv(cdir2, put("rep_two.json", _bt_report_for(
            camp2.identity, cdir2, sm, end_state="PI-STOP", pauses=[pz, p2], stop=stop_pi)), art2),
            "more than one pause stands")
        # PIN-n-37's inputs: a pause's read outside the plan (a rendering pause standing, its read not on disk); a
        # standing batch not the runner's (the v5 review's F1, B3): A's run's-end batch with its count, its
        # exceedances, its start (moved back onto a read with no re-computation), its end (one trial short of the
        # stage's last) or its scope (without N1-P) not the records'; and C's batch, ending at a read, with its count
        rr = dict(sm.example_pause(1, kind="rendering", launch_index=len(camp.records), arms=("N1-R",)),
                  read_id=f"N1-R|rand_00|+1|{session_key(40)}")
        refs["pause-not-planned"] = (rv(cdir, on_main("rep_rr.json", [rr], end_state="PI-STOP", stop=stop_pi)),
                                     "is not a read of the plan")

        def with_b(ps: Sequence[dict], **kw: Any) -> list:
            out_ = json.loads(json.dumps(list(ps)))
            out_[-1]["binomial"].update(kw)
            return out_
        b2, tl_k = pa[-1]["binomial"], trials_of(camp_k)
        sc_ = json.loads(json.dumps(pa))
        sc_[-1]["arms_in_scope"] = [a for a in sc_[-1]["arms_in_scope"] if a != "N1-P"]
        for k_, ps_, want_ in (("batch-count", with_b(pa, n=b2["n"] + 1), "its batch is not the records' trials"),
                               ("batch-exceedances", with_b(pa, k=0), "its batch is not the records' trials"),
                               ("batch-start", with_b(pa, first_launch_index=b2["first_launch_index"] - 1),
                                "its batch is not the records' trials"),
                               ("batch-end", with_b(pa, last_launch_index=tl_k[-2], n=b2["n"] - 1),
                                "its batch is not the records' trials"),
                               ("batch-scope", sc_, "its scope does not hold the arms of its batch's trials")):
            refs[k_] = (rv(cdir_k, put(f"rep_{k_}.json", _bt_report_for(camp_k.identity, cdir_k, sm,
                                                                       end_state="PI-STOP", pauses=ps_,
                                                                       stop=stop_pi)), art_k), want_)
        refs["batch-read-count"] = (rv(cdir2, put("rep_batch-read-count.json", _bt_report_for(
            camp2.identity, cdir2, sm, end_state="PI-STOP", pauses=with_b(pc, n=pc[-1]["binomial"]["n"] + 1),
            stop=stop_pi)), art2), "its batch is not the records' trials")
        bad = {k: m[:70] for k, ((okr, m), want_m) in refs.items() if not (okr and want_m in m)}
        if "DONE" in refs["schema-report"][0][1] or "§3" in refs["schema-gread"][0][1]:
            bad["schema-blind"] = "a schema refusal printed the schema's text, not its field path alone"
        B.chk(f"verdicts refuses, each by its message ({len(refs)} cases): a date; a report or an artifact the schema "
              "refuses (by its field path alone); a PAUSE; a stage not a campaign; a "
              "lock not the identity's, not naming this analyzer, not saying it is LOCK-n v1.0, or without one "
              "direction of record A or B; a report not the cells on disk (cells, identity, per-arm counts, on a "
              "complete campaign and on one with no arm complete; the counters, label mass and used time), a pause's "
              "read not on disk or not of its kind, a rendering pause not resumed whose read is on disk, a resumption "
              "where nothing was launched, a read after a standing pause, a standing pause not the last event, launch "
              "indices not 0..m−1, two pauses standing, a pause's read not of the plan, a standing batch not the "
              "runner's (its count, its exceedances, its start, its end, its scope, and one ending at a read: "
              "PIN-n-37); G-READ-n's artifact missing, or not the campaign's (plan, "
              "identity, a cell's capture or json sha, a cell left out, the package, the layers, merged labels, a "
              "point not kept); a malformed "
              "cosines file or one without the six pairs; a report of no record beside a non-empty campaign directory",
              not bad, bad, cover=["VD-REFUSE"])
        # G-READ-n's states reach the tuple and the labels
        mixed = {}
        for k, (stt, drop) in {"FAIL": ({"valence|+d_eq": "FAIL"}, ()), "absent": (None, ("valence|+d_eq",)),
                               "E-FAIL": ({"span_reward|f0.20": "FAIL"}, ())}.items():
            gp = put(f"g_{k}.json", _bt_gread_for(camp, sm, statuses=stt, drop=drop))
            run(cdir, rep, gp, lock, base / f"out_g{k}")
            vv = doc_of(base / f"out_g{k}")
            mixed[k] = ((vv.get("tuple") or [None] * 5)[4], dig(vv, "gread", "auc", "d_eq"),
                        dig(vv, "outcomes", "gread", "E"))
        B.chk("G-READ-n's artifact reaches the tuple: valence at +d_eq FAIL gives the coordinate FAIL and the AUC "
              "0.62; the result absent gives NOT-COMPUTED, so FAIL, and no AUC (PIN-n-11, PIN-n-25); span_reward at "
              "f0.20 FAIL reaches N2's label state E, f0.10's PASS not",
              mixed == {"FAIL": ("FAIL", 0.62, "PASS"), "absent": ("FAIL", None, "PASS"),
                        "E-FAIL": ("PASS", 0.96, "FAIL")}, mixed, cover=["VD-GREAD-MIXED"])
        nan_stop = _bt_raises(lambda: _plain({"x": [1.0, float("nan")]}), (AnlStop,))
        key_stop = _bt_raises(lambda: _plain({1.0: 1, "1.0": 2}), (AnlStop,))
        js_stop = _bt_raises(lambda: json_text({"x": float("inf")}), (AnlStop,))
        # a STOP while VERDICTS is formed writes nothing: G-LEAK-n's table made to carry a NaN for one call
        g_orig = globals()["gleak_table"]
        globals()["gleak_table"] = lambda st_: [{"x": float("nan")}]
        try:
            v_stop = _bt_raises(lambda: run_verdicts(cdir, rep, art, lock, "2026-12-20", None, base / "out_stop"),
                                (AnlStop,))
        finally:
            globals()["gleak_table"] = g_orig
        B.chk("VERDICTS' form STOPs rather than write a non-finite figure or fold two keys into one: _plain on a NaN, "
              "_plain on two keys that write alike (1.0 and '1.0'), json_text on an inf; a STOP while VERDICTS is "
              "formed leaves no output, the secondary included",
              nan_stop[0] and "non-finite" in nan_stop[1] and key_stop[0] and "write alike" in key_stop[1]
              and js_stop[0] and "non-finite" in js_stop[1] and v_stop[0] and "non-finite" in v_stop[1]
              and not (base / "out_stop").exists(),
              (nan_stop[1][:50], key_stop[1][:50], js_stop[1][:50], v_stop[1][:50]), cover=["VD-PLAIN"])
        never = REPO / "LOCK-n.__never_committed__.md"
        pre = {"lock-outside": verdicts_precheck(None, str(lock)),
               "report-outside": verdicts_precheck(None, str(REPO / "LOCK-n.md"), (str(rep), None, None), bound=()),
               "uncommitted": verdicts_precheck(None, str(REPO / "LOCK-n.md"),
                                                bound=("scripts/__n_analyze_never_committed__.py",)),
               "lock-uncommitted": verdicts_precheck(None, str(never)),
               "of-record": verdicts_precheck(None, str(REPO / "LOCK-n.md"), bound=()),
               "repo-root": verdicts_precheck(str(REPO), str(lock)),
               "repo-sub": verdicts_precheck(str(REPO / "data"), str(lock)),    # resolve() stats it: not under data/n
               "outside": verdicts_precheck(str(base / "vo"), str(lock))}
        ok_p = {"lock-outside": pre["lock-outside"][0] == 2 and "(LOCK-n.md is not)" in pre["lock-outside"][1],
                "report-outside": pre["report-outside"][0] == 2 and "(report.json is not)" in pre["report-outside"][1],
                "uncommitted": pre["uncommitted"][0] == 2 and "committed analyzer" in pre["uncommitted"][1],
                "lock-uncommitted": pre["lock-uncommitted"][0] == 2 and never.name in pre["lock-uncommitted"][1],
                "of-record": pre["of-record"] == (0, "", REPO / VERDICTS_REL),
                "repo-root": pre["repo-root"][0] == 2 and "inside the repository" in pre["repo-root"][1],
                "repo-sub": pre["repo-sub"][0] == 2 and "inside the repository" in pre["repo-sub"][1],
                "outside": pre["outside"] == (0, "", (base / "vo").resolve())}
        B.chk("verdicts' refusals before any read: VERDICTS of record only from inputs in the repository (the lock, "
              "the report), from the committed analyzer and a committed lock; a --out at the repository root or "
              "inside it; with nothing left to check it names data/n/verdicts, and a --out outside the repository "
              "proceeds", all(ok_p.values()), {k: pre[k][:2] for k, v in ok_p.items() if not v},
              cover=["VD-PRECHECK"])


def battery() -> dict:
    B = _Battery()
    snap0 = _bt_snapshot()
    with _Hook() as hook:
        ptext = (REPO / PROPOSAL_REL).read_bytes()
        atext = (REPO / ADDENDUM_REL).read_bytes()
        verb = proposal_spans(ptext.decode("utf-8")) | addendum_spans(atext.decode("utf-8"))
        B.group("outcomes", lambda: _bt_outcomes(B))
        B.group("not-run", lambda: _bt_notrun(B))
        B.group("tables", lambda: _bt_tables(B))
        B.group("sentences", lambda: _bt_sentences(B, verb))
        B.group("tuples", lambda: _bt_tuples(B, verb))
        B.group("reachability", lambda: _bt_reachability(B))
        B.group("numerics", lambda: _bt_numerics(B))
        B.group("reader path", lambda: _bt_reader(B))
        B.group("commands", lambda: _bt_commands(B))
        B.group("verdicts", lambda: _bt_verdicts(B))
        B.group("structure", lambda: _bt_structure(B, ptext, hook, atext))
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
BOUND_RELS = (PROPOSAL_REL, ADDENDUM_REL, SCHEMA_REL, f"{BK_NP_REL}/prereg.json", f"{BK_NP_REL}/reduced.json")


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
    # the coupling shapes (map_reach_by_hand): dose and N2 meet N1 at +1 when d_eq sits there (d); N2 is decided at
    # dose's point when the cap binds (b), at N1's +1 when d_20 sits there without the cap (c); else none (a)
    m = dmap.norm_matched(dmap.n2_decision_f())
    shape = "d" if r["d_eq"] == 1.0 else "b" if dmap.cap_binds() else "c" if m == 1.0 else "a"
    seen, iff, clean = map_reach(dmap)
    return {"shape": shape, "triples": len(seen), "tuples": len(seen) * 8 + 1, "dose_iff_n1": iff, "raised": not clean,
            "agrees_with_hand": seen == map_reach_by_hand(shape)}


def ganl_artifact(res: Mapping[str, Any], dmap: DoseMap | None) -> dict:
    sha = analyzer_sha256()
    return {"schema": GANL_SCHEMA, "stage": "G-ANL-n", "verdict": "PASS",
            "spec": "PROPOSAL-n v0.2 §3 G-ANL-n, §8 step 9; the seat's answers of 2026-11-15 §5.1, of 2026-11-16 "
                    "(results/raw/2026-11-16_n-ganl_design-to-code_answers.md) and of 2026-11-18 §5 "
                    "(results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md) and §3 of its second sitting "
                    "(results/raw/2026-11-18_n-step4-smoke-pause_design-to-code_answers.md); ADDENDUM-n1 v0.1 §4-§7",
            "analyzer": {"path": ANALYZER_REL, "sha256": sha, "sha16": sha[:16]},
            "proposal": {"path": PROPOSAL_REL, "sha256": PROPOSAL_SHA256},
            "addendum": {"path": ADDENDUM_REL, "sha256": ADDENDUM_SHA256},
            "schema_module": {"path": SCHEMA_REL, "sha256": SCHEMA_SHA256},
            "battery": {k: res.get(k) for k in ("checks_pass", "checks_total", "expected_checks", "coverage_ids",
                                                 "outputs_sha256", "reachability", "bk_repro", "bk_fidelity")},
            "tuple_space": {"tuples": 385, "evaluations": 2561},
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
                                               ("c", DoseMap(0.49, 2 * 0.49)), ("d", DoseMap(0.97, 1.0)))}
    B.chk("the pinned map's coupling shape: d_20 at +1/2 is (a) (28 triples); d_eq at +1/2 with the cap binding is "
          "(b) (25: N2 decided at dose's point, OPEN-Q7 as ruled); d_eq at +1/2 with d_20 merged into +1 without the "
          "cap is (c) (24); both at +1 is (d) (17); each agreeing with the hand derivation",
          {k: (v["shape"], v["triples"], v["agrees_with_hand"]) for k, v in cls.items()}
          == {"a": ("a", 28, True), "b": ("b", 25, True), "c": ("c", 24, True), "d": ("d", 17, True)}, cls,
          cover=["NUM-REACH-CLASS"])
    with tempfile.TemporaryDirectory(prefix="n_anl_cmd_") as td:
        base = Path(td)
        rec = {"schema": NOT_RUN_RECORD_SCHEMA, "unit": UNIT, "cause": "clock:pi-declined", "date": "2026-12-16",
               "detail": "a synthetic record"}
        rp = base / "rec.json"
        rp.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")       # not json.dumps(rec)'s bytes
        rsha = hashlib.sha256(rp.read_bytes()).hexdigest()
        p1, h1 = run_not_run(rp, base / "out")
        p2, h2 = run_not_run(rp, base / "out")
        doc = json.loads(p1.read_text(encoding="utf-8"))
        rp.write_text(json.dumps(dict(rec, cause="clock:no-box")), encoding="utf-8")
        ok3, msg3 = _bt_raises(lambda: run_not_run(rp, base / "out"), (AnlRefusal,))
        B.chk("not-run writes N-pod_NOT-RUN.json once (written, then identical), refuses other bytes (write-once), "
              "carries the reason in all four sentence slots, and binds the record by its file's sha256 and the "
              "proposal and ADDENDUM-n1 by theirs", (h1, h2) == ("written", "identical") and ok3
              and doc["outcome"] == NOT_RUN and all(doc["reason"] in v["text"] for v in doc["sentences"].values())
              and doc["date"] == "2026-12-16" and doc["record"] == {"name": "rec.json", "sha256": rsha}
              and doc["proposal_sha256"] == PROPOSAL_SHA256 and doc["addendum_sha256"] == ADDENDUM_SHA256,
              (h1, h2, msg3[:60], doc.get("record")), cover=["CMD-NOTRUN"])
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
        B.chk("G-ANL-n's artifact names the analyzer, proposal, ADDENDUM-n1 and schema by sha256, the tuple space "
              "(385; 2,561 evaluations, the tuple pass's own), the pinned map's points and reach, the PIN and OPEN "
              "registers, and no time",
              art["proposal"]["sha256"] == PROPOSAL_SHA256 and art["schema_module"]["sha256"] == SCHEMA_SHA256
              and art["addendum"] == {"path": ADDENDUM_REL, "sha256": ADDENDUM_SHA256}
              and BOUND_RELS == (PROPOSAL_REL, ADDENDUM_REL, SCHEMA_REL, f"{BK_NP_REL}/prereg.json",
                                 f"{BK_NP_REL}/reduced.json")
              and art["tuple_space"] == {"tuples": len(tuple_space()), "evaluations": len(evaluations())}
              == {"tuples": 385, "evaluations": 2561} and art["dose_map"]["reach"]["shape"] == "d"
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


# =====================================================================================================================
# 16. VERDICTS (n §8 step 15; §4 "Blinding": the analyzer computes VERDICTS before "the reads", m:318's form)
# =====================================================================================================================
VERDICTS_SCHEMA = "n-verdicts-v1"
SECONDARY_SCHEMA = "n-secondary-v1"
ROUTE_LINE = "direction of record: Route "
LOCK_V10_LINE = "lock: LOCK-n v1.0"
GVEC_DIRS = ("span_character", "span_reward", "span_sentiment", "valence")
NO_ARM_CAUSE = {"PI-STOP": "no-arm:pi-stop", "G-VER-STOP": "no-arm:gver-stop", "CAP": "no-arm:cap"}
GREAD_LABEL_F = {"f0.10": F10, "f0.20": F20}
EXPOSURE_CLASSES = (("N1-V", "negative valenced"), ("N1-P", "negative valenced"), ("N1-R", "negative random"))


def lock_route(text: str) -> str:
    """PIN-n-26 (Code's form, flagged): LOCK-n v1.0 says what it is in the whole line 'lock: LOCK-n v1.0' (so no
    earlier lock passes for it), and states the direction of record G-VEC declared as one whole line,
    'direction of record: Route A' or 'direction of record: Route B'. Without the first line, or with no, two, or
    another route line, it refuses."""
    if not any(ln.strip() == LOCK_V10_LINE for ln in text.splitlines()):
        raise AnlRefusal(f"REFUSED: the lock does not say it is LOCK-n v1.0 (the whole line '{LOCK_V10_LINE}')")
    lines = [ln.strip() for ln in text.splitlines() if ln.strip().startswith(ROUTE_LINE.strip())]
    if len(lines) != 1 or lines[0] not in (ROUTE_LINE + "A", ROUTE_LINE + "B"):
        raise AnlRefusal(f"REFUSED: the lock does not state one direction of record as a whole line '{ROUTE_LINE}A' "
                         f"or '{ROUTE_LINE}B'")
    return lines[0][-1]


def _load_checked(path: Path, check: Callable[[Any], None], what: str) -> tuple[dict, str]:
    """A JSON file through the schema's own check: (the object, the sha256 of the bytes parsed)."""
    try:
        data = Path(path).read_bytes()
        obj = json.loads(data.decode("utf-8"))
        check(obj)
    except (OSError, ValueError) as e:
        raise AnlRefusal(f"REFUSED: {what}: {_err_where(e)}")
    return obj, hashlib.sha256(data).hexdigest()


def report_counters(camp: Campaign) -> dict:
    """The counters a stage report carries, recomputed from the records (PIN-n-24, n-build's counting, settled):
    per 'arm|dose_label', the records with a fidelity block (trials) and those whose block exceeds TAU and TAU/4;
    records non-finite on either path; records whose identity check is not within; and, per 'arm|dose_label', the
    finite records whose restricted label mass is below PIN-n-17's .20."""
    fid: dict = {}
    lm: dict = {}
    nonfin = oob = 0
    for r in camp.records.values():
        key = f"{r['arm']}|{r['dose_label']}"
        f = r["fidelity"]
        if f is not None:
            x = fid.setdefault(key, {"trials": 0, "exceed_tau": 0, "exceed_tau4": 0})
            x["trials"] += 1
            x["exceed_tau"] += bool(f["exceeds_tau"])
            x["exceed_tau4"] += bool(f["exceeds_tau4"])
        if not r["finite"] or (f is not None and not f["finite"]):
            nonfin += 1
        if r["identity"] is not None and not r["identity"]["within"]:
            oob += 1
        if r["finite"] and label_mass_below([r["restricted"]["label_mass"]]):
            lm[key] = lm.get(key, 0) + 1
    return {"fidelity": dict(sorted(fid.items())), "nonfinite_reads": nonfin, "identity_out_of_bound": oob,
            "label_mass_below_floor": dict(sorted(lm.items()))}


def report_problems(rep: Mapping[str, Any], camp: Campaign, sm) -> list[str]:
    """PIN-n-24: the stage report bound to the campaign on disk, the properties check_report leaves to the reader:
    the identity and the plan; every cell file by its shas and record count; each arm's planned, obtained and complete
    against the records; the counters and the cap's used time against the records; and the launches and pauses as
    n-build's runner makes them (its answer of 2026-11-16): the records' launch indices are exactly 0..m−1; at most
    one pause stands, and it is the stage's last event (its launch index m for a rendering pause, whose read is not
    launched, else m − 1); a pause with a read, other than a rendering pause, names a read on disk, non-finite where
    it names nonfinite and outside the identity bound where it names identity-bound; a rendering pause not resumed
    names a read not on disk; a resumption is where a read was launched or refused; every pause's read is a read of
    the plan. A standing pause's binomial batch is bound to the records, since PIN-n-37 reads it: it is the runner's
    batch -- the reads carrying a re-computation from the first after the last cleared batch (an adjudicated pause's
    batch, which its ruling clears; else the stage's first) to the pause's read, or to the stage's last for a fire at
    the run's end -- its n those trials and its k those above TAU, and its scope holds their arms (the v5 review's F1).
    An adjudicated batch is not checked (its counting is the runner's; no outcome reads it). Three checks here cannot
    fire alone and are kept so the binding is stated whole: the two shas, which check_report ties to the report's
    identity, once the identity is the cells'; and the per-arm counts, which the schema's per_arm rule (complete is
    obtained == planned) and check_report's plan and cell-record checks imply once the identity is the cells' and the
    cells are the files on disk."""
    p = []
    ident = camp.identity
    if ident["stage"] != "campaign":
        p.append("the cells are not a campaign's")
    if _canon(rep["stage_identity"]) != _canon(ident):
        p.append("the report's stage identity is not the cells'")
    if rep["stage_identity_sha256"] != sm.identity_sha256(ident):
        p.append("stage_identity_sha256 is not the cells' identity's")
    if rep["read_plan_sha256"] != sm.read_plan_sha256(ident):
        p.append("read_plan_sha256 is not the cells' plan's")
    if rep["cells"] != camp.cells:
        odd = sorted(set(rep["cells"]) ^ set(camp.cells)) or sorted(n for n in rep["cells"]
                                                                    if rep["cells"][n] != camp.cells[n])
        p.append(f"the report's cells are not the files on disk, e.g. {odd[:2]}")
    for a in ARMS:
        want = {"planned": len(camp.planned[a]), "obtained": len(camp.present[a]),
                "complete": camp.present[a] == camp.planned[a]}
        if rep["per_arm"].get(a) != want:
            p.append(f"per_arm.{a} is {rep['per_arm'].get(a)}; the records give {want}")
    got = report_counters(camp)
    c = rep["counters"]
    for k in ("fidelity", "nonfinite_reads", "identity_out_of_bound"):
        if c[k] != got[k]:
            p.append(f"counters.{k} is not the records' count")
    if c["label_mass_below_floor"] is not None and c["label_mass_below_floor"] != got["label_mass_below_floor"]:
        p.append("counters.label_mass_below_floor is not the records' count at PIN-n-17's .20")
    if rep["cap"]["used_ms"] != sum(r["duration_ms"] for r in camp.records.values()):
        p.append("cap.used_ms is not the records' duration_ms sum")
    m = len(camp.records)
    if sorted(r["launch_index"] for r in camp.records.values()) != list(range(m)):
        p.append(f"the records' launch indices are not exactly 0..{m - 1}")
    last = m - 1
    if sum(1 for q in rep["pauses"] if not q["adjudicated"]) > 1:
        p.append("more than one pause stands")
    attempted = ({r["launch_index"] for r in camp.records.values()}
                 | {q["launch_index"] for q in rep["pauses"] if q["kind"] == "rendering"})
    planned = set().union(*camp.planned.values())
    trial_li = sorted(r["launch_index"] for r in camp.records.values() if r["fidelity"] is not None)
    cleared = max((q["binomial"]["last_launch_index"] for q in rep["pauses"]           # an adjudicated batch's ruling
                   if q["adjudicated"] and q["binomial"] is not None and q["read_id"] is not None), default=-1)
    for q in rep["pauses"]:
        ra = q["resumed_at_launch_index"]
        if ra is not None and ra not in attempted:
            p.append(f"{q['pause_id']}: it resumed where no read was launched or refused")
        b = q["binomial"]
        if b is not None and not q["adjudicated"]:
            first_w = next((i for i in trial_li if i > cleared), None)
            last_w = (trial_li[-1] if trial_li else None) if q["read_id"] is None else q["launch_index"]
            ins = [r for r in camp.records.values() if r["fidelity"] is not None
                   and b["first_launch_index"] <= r["launch_index"] <= b["last_launch_index"]]
            if (b["first_launch_index"], b["last_launch_index"]) != (first_w, last_w) \
                    or (len(ins), sum(r["fidelity"]["exceeds_tau"] is True for r in ins)) != (b["n"], b["k"]):
                p.append(f"{q['pause_id']}: its batch is not the records' trials since the last cleared batch "
                         "(PIN-n-37 reads it)")
            if not {r["arm"] for r in ins} <= set(q["arms_in_scope"]):
                p.append(f"{q['pause_id']}: its scope does not hold the arms of its batch's trials")
        rid = q["read_id"]
        if rid is None:
            continue
        if rid not in planned:
            p.append(f"{q['pause_id']}: its read {rid} is not a read of the plan")
        kinds = [q["kind"]] + list(q["also_fired"])
        rec = camp.records.get(rid)
        if q["kind"] == "rendering":
            if ra is None and rec is not None:
                p.append(f"{q['pause_id']}: a rendering pause not resumed names a read on disk")
        elif rec is None:
            p.append(f"{q['pause_id']}: its read {rid} is not on disk")
        else:
            if "nonfinite" in kinds and rec["finite"] and (rec["fidelity"] is None or rec["fidelity"]["finite"]):
                p.append(f"{q['pause_id']}: a non-finite pause at a finite read")
            if "identity-bound" in kinds and not (rec["identity"] is not None and not rec["identity"]["within"]):
                p.append(f"{q['pause_id']}: an identity-bound pause at a read within the bound")
        if not q["adjudicated"]:
            if last > q["launch_index"]:
                p.append(f"{q['pause_id']}: a read was launched after this standing pause")
            elif q["launch_index"] != (m if q["kind"] == "rendering" else m - 1):
                p.append(f"{q['pause_id']}: a standing pause is not the stage's last event")
    return p


def gread_problems(art: Mapping[str, Any], camp: Campaign, rep: Mapping[str, Any]) -> list[str]:
    """PIN-n-25: G-READ-n's artifact bound to the campaign: its plan and identity shas are the report's; the cells it
    read are exactly the campaign's files, by both shas (n-build's probe lists every cell); its probe ran under the
    campaign's n package, on exactly the capture layers; each result is at a point the dose map keeps, listing the
    labels merged into it (the reader's check, the schema's docstring)."""
    p = []
    ident = camp.identity
    ca = art["campaign"]
    if ca["read_plan_sha256"] != rep["read_plan_sha256"] or ca["stage_identity_sha256"] != rep["stage_identity_sha256"]:
        p.append("its campaign's plan or identity sha256 is not the report's")
    want = {n: {"json_sha256": c["json_sha256"], "capture_sha256": c["capture_sha256"]} for n, c in camp.cells.items()}
    if ca["cells"] != want:
        odd = sorted(set(ca["cells"]) ^ set(want)) or sorted(n for n in ca["cells"] if ca["cells"][n] != want[n])
        p.append(f"the cells it read are not the campaign's files, e.g. {odd[:2]}")
    if art["probe"]["package_sha256"] != ident["package_sha256"]:
        p.append("its probe ran under another n package than the campaign's")
    if list(art["probe"]["layers"]) != list(ident["capture_layers"]):
        p.append("its layers are not the campaign's capture layers")
    kept = {pt["label"]: pt["merged"] for pt in ident["dose_map"]["points"]}
    for r in art["results"]:
        lab = r["dose_label"]
        if lab not in kept:
            p.append(f"a result at {r['axis']} {lab}, a point the dose map does not keep")
        elif r["merged"] != kept[lab]:
            p.append(f"the result at {r['axis']} {lab} lists {r['merged']} merged; the dose map, {kept[lab]}")
    return p


def gread_states(art: Mapping[str, Any], camp: Campaign) -> tuple[dict, dict, list]:
    """G-READ-n's results as the outcome layer reads them (PIN-n-25): (axis, point) -> status, by the point's value,
    so a merged point carries its keeper's result, and an (axis, point) with no result is NOT-COMPUTED (PIN-n-11);
    the dose sentence's AUC, the band median of the result at d_eq's kept label; and the results as reported."""
    lv = label_values(camp.identity)
    g: dict = {}
    rows = []
    for r in sorted(art["results"], key=lambda r: (r["axis"], r["dose_label"])):
        key = (("valence", lv[r["dose_label"]]) if r["axis"] == "valence"
               else ("span_reward", GREAD_LABEL_F[r["dose_label"]]))
        g[key] = r["status"]
        rows.append({"axis": r["axis"], "label": r["dose_label"], "merged": list(r["merged"]), "status": r["status"],
                     "band_median_auc": r["band_median_auc"], "comparator_max": r["comparator"]["max"],
                     "per_layer": r["per_layer"]})
    deq = camp.dmap.kept_label("d_eq")
    auc = {"d_eq": next((r["band_median_auc"] for r in art["results"]
                         if r["axis"] == "valence" and r["dose_label"] == deq), None)}
    return g, auc, rows


def paused_from(rep: Mapping[str, Any]) -> dict[str, bool]:
    """An arm is paused while an unadjudicated pause holds it in scope (n-report-v1)."""
    return {a: any(not q["adjudicated"] and a in q["arms_in_scope"] for q in rep["pauses"]) for a in ARMS}


def paused_points(rep: Mapping[str, Any], camp: Campaign) -> dict[tuple[str, Any], bool]:
    """PIN-n-37: the points the stage report's unadjudicated pauses stand on, for N2's rule (PIN-n-33 as amended), each
    within its pause's scope (n-build's schema: a pause stands on the arms in its scope). A pause stands on its read,
    where it has one (a rendering pause's is not on disk: its id names its point); on its binomial batch's trials, the
    reads carrying a re-computation launched from the batch's first_launch_index to its last (the runner's trials,
    bound to the records by report_problems); and, where one of those reads is a session's shadow (N1-V's d = 0 read),
    on every read of that session, each read against it (Code's extension, capped by the scope: the runner's SCOPE
    applies its shadow clause to the read that fired alone; PIN-n-37). Keyed as State.at is: (arm, the point's value),
    N2's arms by the f; the steered arms only, N4's pauses being read per arm."""
    lv = label_values(camp.identity) | {"f0.10": F10, "f0.20": F20}
    out: dict[tuple[str, Any], bool] = {}
    for q in rep["pauses"]:
        if q["adjudicated"]:
            continue
        scope = sorted(set(q["arms_in_scope"]) & set(STEERED_ARMS))
        rids = [] if q["read_id"] is None else [q["read_id"]]
        b = q["binomial"]
        if b is not None:
            rids += sorted(rid for rid, r in camp.records.items() if r["fidelity"] is not None
                           and b["first_launch_index"] <= r["launch_index"] <= b["last_launch_index"])
        for rid in rids:
            arm, _d, lab, sid = rid.split("|")
            if (arm, lab) == ("N1-V", "0"):                # a shadow (N1-V|none|0): its session's reads pair with it
                for a in scope:
                    for pa, _pd, plab, psid in (p.split("|") for p in camp.planned[a]):
                        if psid == sid and (pa, plab) != ("N1-V", "0"):
                            out[(pa, lv[plab])] = True
            elif arm in scope:
                out[(arm, lv[lab])] = True
    return out


def exposure(camp: Campaign) -> dict:
    """PIN-n-23: §0.4's table realised in the campaign: per arm, the reads on disk at d = −1 (finite or not) against
    the plan, with the fresh re-computations they carry (§2.1; two more forwards each). G-CAL-n's generations under
    negative steering are its own entry's; the campaign generates nothing."""
    out: dict = {}
    for arm, cls in EXPOSURE_CLASSES:
        planned = [r for r in camp.planned[arm] if r.split("|")[2] == "-1"]
        got = [r for r in planned if r in camp.present[arm]]
        out[arm] = {"class": cls, "planned": len(planned), "reads": len(got),
                    "fresh_recomputations": sum(1 for r in got if camp.records[r]["fidelity"] is not None)}
    out["totals"] = {"negative valenced": out["N1-V"]["reads"] + out["N1-P"]["reads"],
                     "negative random": out["N1-R"]["reads"],
                     "generations under negative steering": "none in the campaign; G-CAL-n's are its entry's"}
    return out


def _plain(x: Any) -> Any:
    """JSON-native and finite (a non-finite figure STOPs): an Est as its JSON, dict keys as strings (a tuple key
    joined by '|', a float key by repr), tuples as lists, numpy scalars as Python numbers."""
    if isinstance(x, Est):
        return _plain(x.as_json())
    if isinstance(x, dict):
        def key(k: Any) -> str:
            if isinstance(k, str):
                return k
            if isinstance(k, tuple):
                return "|".join(map(str, k))
            return repr(float(k)) if isinstance(k, (float, np.floating)) else str(k)
        out = {key(k): _plain(v) for k, v in x.items()}
        if len(out) != len(x):
            raise AnlStop("STOP: two keys of a VERDICTS mapping write alike")
        return out
    if isinstance(x, (list, tuple)):
        return [_plain(v) for v in x]
    if x is None or isinstance(x, (bool, str)):
        return x
    if isinstance(x, (int, np.integer)):
        return int(x)
    if isinstance(x, (float, np.floating)):
        if not math.isfinite(float(x)):
            raise AnlStop("STOP: a non-finite figure in VERDICTS")
        return float(x)
    raise AnlStop(f"STOP: a value of type {type(x).__name__} in VERDICTS")


def state_figures(st: State, fig: Mapping[str, Any]) -> dict:
    """§4's figures behind the outcomes: the estimates, the floor, L and P, E, the guards, m_told and E_sham, each
    arm's usability, as an arm and point by point ('arm@label': why not usable, [] when usable; PIN-n-36), the points
    a standing pause stands on ('arm@label', PIN-n-37; null for a state with no point map), and build_state's per-arm
    figures."""
    def name(a: str, k: Any) -> str:
        return f"{a}@{F_LABEL[k] if k in F_LABEL else st.dmap.label_of(k)}"
    at = {name(a, k): v for (a, k), v in sorted(st.at.items(), key=lambda kv: (kv[0][0], str(kv[0][1])))}
    pp = None if st.paused_at is None else sorted(name(a, k) for (a, k), v in st.paused_at.items() if v)
    return _plain({"V": st.V, "slope_V": st.slope_V, "floor_V": st.floor_V, "L": st.L, "P": st.P, "E": st.E,
                   "S": st.S, "C": st.C, "told": st.told, "e_sham": st.e_sham, "complete": st.complete,
                   "paused": st.paused, "missing": st.missing, "nonfinite": st.nonfinite, "unusable": st.unusable,
                   "point_causes": at, "pause_points": pp, "per_arm": dict(fig)})


def _load_gvec(path: Path) -> tuple[dict, str]:
    """The cosines between the four directions (§8 step 15; secondary (e)), from G-VEC's output given to the command:
    {"cosines": {"x|y": float}} with exactly the six pairs of GVEC_DIRS, x before y in that order, each finite,
    bound by sha256 (the file's form is G-VEC's)."""
    try:
        data = Path(path).read_bytes()
        obj = json.loads(data.decode("utf-8"))
    except (OSError, ValueError) as e:
        raise AnlRefusal(f"REFUSED: the cosines file: {type(e).__name__}")
    pairs = {f"{x}|{y}" for i, x in enumerate(GVEC_DIRS) for y in GVEC_DIRS[i + 1:]}
    cos = obj.get("cosines") if isinstance(obj, dict) else None
    if not (isinstance(cos, dict) and set(cos) == pairs
            and all(isinstance(v, float) and math.isfinite(v) for v in cos.values())):
        raise AnlRefusal("REFUSED: the cosines file is not {\"cosines\": {...}} with the six pairs of "
                         f"{', '.join(GVEC_DIRS)}, each a finite float")
    return obj, hashlib.sha256(data).hexdigest()


def verdicts_precheck(out: str | None, lock: str, inputs: Sequence[str | None] = (),
                      bound: Sequence[str] | None = None) -> tuple[int, str, Path | None]:
    """`verdicts`' refusals before any read. VERDICTS of record (no --out: data/n/verdicts) come only from the
    committed analyzer, under a committed lock, from a committed stage report, G-READ-n artifact and cosines file
    (``inputs``; those given), each a file in the repository, so none can be edited before the run (the cells are
    bound by the committed report's shas); ``bound`` replaces the list of committed paths (the battery's handle). A
    --out goes only outside the repository. Returns (code, message, output directory)."""
    root = REPO.resolve()
    if out is None:
        rels = [ANALYZER_REL]
        for x in [lock] + [y for y in inputs if y is not None]:
            xp = Path(x).expanduser().resolve()
            if root not in xp.parents:
                return 2, ("REFUSED: VERDICTS of record take the lock, the report, G-READ-n's artifact and the cosines "
                           f"file from the repository ({Path(x).name} is not)"), None
            rels.append(str(xp.relative_to(root)))
        probs = committed_problems(tuple(rels) if bound is None else tuple(bound))
        if probs:
            return 2, ("REFUSED: VERDICTS of record are written by the committed analyzer from committed inputs "
                       f"only: {probs}"), None
        return 0, "", REPO / VERDICTS_REL
    d = Path(out).expanduser().resolve()
    if d == root or root in d.parents:
        return 2, (f"REFUSED: a --out directory inside the repository (the output of record goes to {VERDICTS_REL}, "
                   "with no --out)"), None
    return 0, "", d


def run_verdicts(campaign: Path, report: Path, gread: Path | None, lock: Path, date: str, gvec: Path | None,
                 out_dir: Path) -> dict:
    """`verdicts` (n §8 step 15): N-pod's VERDICTS and secondary DVs, or its NOT-RUN where the report says no arm's
    full read set was produced before a STOP or the cap (§5 "Unit outcome first"; PIN-n-24's end-state rules). An
    arm's full read set is the report's ``complete``, every planned read produced, finite or not: a non-finite read
    makes its arm INDETERMINATE (PIN-n-20), never the unit NOT-RUN (PIN-n-24). It refuses (AnlRefusal, exit 2),
    before any output, on: a date that is not an ISO calendar date; a report the schema refuses, a PAUSE (the seat
    rules first), or one not a campaign's; a lock not the identity's lock_sha256, not naming this analyzer's sha256,
    not saying it is LOCK-n v1.0, or stating no direction of record (PIN-n-26); a report not bound to the cells on
    disk (PIN-n-24); an output of the other outcome already in the output directory; and, when it analyzes, a
    G-READ-n artifact missing, refused by the schema or not bound to the campaign (PIN-n-25), or a malformed cosines
    file (on the NOT-RUN path neither is read). It writes, write-once, the secondary DVs and then VERDICTS, which
    names the secondary by sha256, both formed before either is written (a STOP while forming them writes nothing,
    and a write-once refusal of either comes before either is written), or the NOT-RUN output. It returns
    {'outputs': [(name, how, sha256)], 'tuple': the outcome tuple or 'NOT-RUN'}, and prints no margin (§4
    "Blinding")."""
    if not _iso_date(date):
        raise AnlRefusal(f"REFUSED: the date {date!r} is not an ISO calendar date (the PI date of the run)")
    sm = schema_module()
    rep, rep_sha = _load_checked(report, sm.check_report, "the stage report")
    end = rep["end_state"]
    if end == "PAUSE":
        raise AnlRefusal("REFUSED: the stage report ends in PAUSE: an unadjudicated pause stands, and the seat "
                         "rules first")
    ident = rep["stage_identity"]
    if ident["stage"] != "campaign" or ident["proposal_sha256"] != PROPOSAL_SHA256:
        raise AnlRefusal("REFUSED: the stage report is not a campaign of PROPOSAL-n v0.2")
    try:
        lbytes = Path(lock).read_bytes()
    except OSError as e:
        raise AnlRefusal(f"REFUSED: the lock: {type(e).__name__}")
    lock_sha = hashlib.sha256(lbytes).hexdigest()
    if lock_sha != ident["lock_sha256"]:
        raise AnlRefusal("REFUSED: the lock is not the one the campaign's identity names (lock_sha256)")
    asha = analyzer_sha256()
    ltext = lbytes.decode("utf-8", "replace")
    if not lock_names(ltext, asha):
        raise AnlRefusal("REFUSED: the lock does not name this analyzer's sha256")
    route = lock_route(ltext)
    base = {"unit": UNIT, "date": date, "proposal_sha256": PROPOSAL_SHA256, "addendum_sha256": ADDENDUM_SHA256,
            "analyzer_sha256": asha,
            "schema_module": {"path": SCHEMA_REL, "sha256": SCHEMA_SHA256},
            "lock": {"name": Path(lock).name, "sha256": lock_sha},
            "report": {"name": Path(report).name, "sha256": rep_sha, "end_state": end}, "pins": PINS, "open": OPEN}
    camp = None
    if rep["cells"]:
        camp = load_campaign(campaign, sm)
        probs = report_problems(rep, camp, sm)
        if probs:
            raise AnlRefusal(f"REFUSED: the stage report is not the campaign on disk: {probs[:3]}")
    elif Path(campaign).is_dir() and any(Path(campaign).iterdir()):
        raise AnlRefusal("REFUSED: the stage report holds no cell, but the campaign directory is not empty")
    out_dir = Path(out_dir)
    if end in NO_ARM_CAUSE and not any(x["complete"] for x in rep["per_arm"].values()):
        rec = {"schema": NOT_RUN_RECORD_SCHEMA, "unit": UNIT, "cause": NO_ARM_CAUSE[end], "date": date,
               "detail": f"derived from the stage report: {end}, no arm complete"}
        doc = not_run_doc(rec, {"name": Path(report).name, "sha256": rep_sha, "derived_from": "the stage report",
                                "end_state": end, "stop_record_sha256": (rep["stop"] or {}).get("record_sha256")},
                          {"lock": base["lock"], "schema_module": base["schema_module"]})
        one_outcome(out_dir, "NOT-RUN")
        path = out_dir / f"{UNIT}_NOT-RUN.json"
        how = write_once(path, json_text(doc))
        return {"outputs": [(path.name, how, hashlib.sha256(path.read_bytes()).hexdigest())], "tuple": NOT_RUN}
    if gread is None:
        raise AnlRefusal("REFUSED: VERDICTS bind G-READ-n's artifact (--gread)")
    art, art_sha = _load_checked(gread, sm.check_gread, "G-READ-n's artifact")
    probs = gread_problems(art, camp, rep)
    if probs:
        raise AnlRefusal(f"REFUSED: G-READ-n's artifact is not the campaign's: {probs[:3]}")
    gv, gv_sha = (None, None) if gvec is None else _load_gvec(gvec)
    paused, pat = paused_from(rep), paused_points(rep, camp)
    g, auc, gres = gread_states(art, camp)
    st, fig = build_state(camp, paused=paused, gread=g, paused_at=pat)
    o = outcomes(st)
    sset = sentence_set_filled(o, st, route=route, auc=auc)
    st_s, fig_s = build_state(camp, paused=paused, gread=g, drop=tau4_drop(camp), paused_at=pat)
    o_s = outcomes(st_s)
    cos = None if gv is None else {"source": {"name": Path(gvec).name, "sha256": gv_sha}, "values": gv["cosines"]}
    sec = dict(base, schema=SECONDARY_SCHEMA, claim="none: descriptive, issuing no claim (n §4; rule 11)",
               cosines=cos, secondaries=_plain(secondaries(camp, st, gv)))
    sec_path, v_path = out_dir / f"{UNIT}_secondary.json", out_dir / f"{UNIT}_VERDICTS.json"
    sec_text = json_text(sec)                      # both outputs are formed before either is written
    sec_sha = hashlib.sha256(sec_text.encode("utf-8")).hexdigest()
    verd = dict(base, schema=VERDICTS_SCHEMA, route=route, tuple=list(o["tuple"]), cosines=cos,
                outcomes=_plain({k: o[k] for k in ("N1", "dose", "N2", "N4", "gread")}), sentences=sset,
                figures=state_figures(st, fig), gleak=_plain(gleak_table(st)),
                gread={"artifact": {"name": Path(gread).name, "sha256": art_sha}, "auc": auc, "results": gres,
                       "table": _plain(gread_table(st))},
                counters={"records": counters(camp), "report": rep["counters"],
                          "binomial_state": rep["binomial_state"], "cap": rep["cap"], "stop": rep["stop"],
                          "pauses": rep["pauses"]},
                exposure=exposure(camp),
                sensitivity={"rule": "PIN-n-16 (n §4 (f)): reads re-computed above TAU/4 dropped",
                             "tuple": list(o_s["tuple"]),
                             "outcomes": _plain({k: o_s[k] for k in ("N1", "dose", "N2", "N4")}),
                             "figures": state_figures(st_s, fig_s)},
                campaign={"stage_identity_sha256": rep["stage_identity_sha256"],
                          "read_plan_sha256": rep["read_plan_sha256"], "cells": camp.cells},
                secondary={"name": sec_path.name, "sha256": sec_sha})
    v_text = json_text(verd)
    one_outcome(out_dir, "VERDICTS")
    sec_how, v_how = write_all_once([(sec_path, sec_text), (v_path, v_text)])
    return {"outputs": [(sec_path.name, sec_how, hashlib.sha256(sec_path.read_bytes()).hexdigest()),
                        (v_path.name, v_how, hashlib.sha256(v_path.read_bytes()).hexdigest())],
            "tuple": list(o["tuple"])}


def verdicts_line(res: Mapping[str, Any]) -> str:
    """The one line `verdicts` prints (§4 "Blinding": no margin): the outcome tuple, and each output's name, how it
    was written and its sha256."""
    t = res["tuple"] if isinstance(res["tuple"], str) else "(" + ", ".join(res["tuple"]) + ")"
    return "VERDICTS: " + t + " -> " + "; ".join(f"{n} ({how}; sha256 {h})" for n, how, h in res["outputs"])


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
    v = sub.add_parser("verdicts", help="N-pod's VERDICTS and secondary DVs, or its NOT-RUN, from the campaign, its "
                                        "stage report, G-READ-n's artifact and the lock (n §8 step 15)")
    v.add_argument("--campaign", required=True, help="the campaign's cell directory")
    v.add_argument("--report", required=True, help="the campaign's stage report (n-report-v1)")
    v.add_argument("--gread", default=None, help="G-READ-n's artifact (n-gread-v1); required unless NOT-RUN")
    v.add_argument("--lock", required=True, help="LOCK-n v1.0, the lock the campaign's identity names")
    v.add_argument("--date", required=True, help="the PI date of the run, YYYY-MM-DD")
    v.add_argument("--gvec", default=None, help="secondary (e)'s cosines, from G-VEC: {\"cosines\": {\"x|y\": float}}")
    v.add_argument("--out", default=None, help="a test directory outside the repository (never of record); "
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
    if a.cmd == "verdicts":
        code, msg, out_dir = verdicts_precheck(a.out, a.lock, (a.report, a.gread, a.gvec))
        if code:
            print(msg, file=sys.stderr)
            return code
        try:
            res = run_verdicts(Path(a.campaign), Path(a.report), Path(a.gread) if a.gread else None, Path(a.lock),
                               a.date, Path(a.gvec) if a.gvec else None, out_dir)
        except AnlRefusal as e:
            print(str(e), file=sys.stderr)
            return 2
        except AnlStop as e:
            print(str(e), file=sys.stderr)
            return 4
        print(verdicts_line(res), flush=True)
        return 0
    ap.print_usage(sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
