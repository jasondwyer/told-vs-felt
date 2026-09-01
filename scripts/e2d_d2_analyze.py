#!/usr/bin/env python3
"""e2d D2 analyzer -- Q1, Q2, Q3 and the run-dose rule. PROPOSAL-j v1.1 §2.

COMMITTED BEFORE D2 RUNS. An analysis script authored after seeing the data
is a different instrument from one authored before it, however identical the
code, and only one of them can be shown to have been. This one is committed
at D1 and evaluates nothing until a D2 artifact exists.

MODEL-FREE BY DESIGN. The runner measures (AUC resamples, marker deltas,
exclusion counts) and writes them into the artifact; this script applies the
criteria to those measurements. The separation is the same one e2b and B3
use, and it is what lets the criteria be stub-smoked on a synthetic battery
with no model and no data.

THE THREE CRITERIA, ALL REQUIRED (§2 D2):

  Q1 validity     M-arm session exclusion rate, one-sided exact binomial
                  against p0 = 0.15, alpha = .05. FAILS when the rate is
                  significantly ABOVE p0 -- the bar certifies against gross
                  breakdown. At n = 32 it fires at >= 9/32.
  Q2 readability  resampled clean-round AUC at k = F = 2: median >= .70 AND
                  10th percentile >= .60 over B = 20 resamples. Chosen to
                  FAIL on the g2r pattern -- resamples spanning .448 and
                  .759 have a median near .60.
  Q3 direction    Delta+ >= 0.5*G = 0.158 and Delta+ > 2*|Delta_R|. A sign
                  flip (Delta+ < 0) is V1's overdose signature and fails the
                  rung. The Delta- clause is inapplicable in a one-pole
                  design and is DROPPED, not waived.

RUN-DOSE RULE. All three pass -> the run dose is 0.20 and LOCK-j
instantiates. Any one fails -> e2d STOPS, SCOPED, with the failing figure:
"the weak-state boundary is not reachable with coherence on this apparatus
above MED at session scale." There is no automatic fallback rung; a 0.15
rung is licensable by addendum, never inherited.

Usage:
    python scripts/e2d_d2_analyze.py --selftest
    python scripts/e2d_d2_analyze.py --artifact data/e2d/d2_sessions.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from valence_core.stats import binom_test_exact                   # noqa: E402

P0_Q1 = 0.15               # [LOCK-j formula; AMENDMENT 1 (ii) recount: the
                           # maximum is 0.147 under audit v2 on either +pole
                           # count, and rounds up to 0.15 -- unchanged]
ALPHA = 0.05
MEDIAN_BAR = 0.70
PCTL = 10
PCTL_BAR = 0.60
G_DEFAULT = 0.3156         # pre-registered V1 instrument G
K_GATE = 2                 # k = F = 2


# --- the three criteria ---------------------------------------------------
def q1_validity(n_excluded: int, n_sessions: int, p0: float = P0_Q1) -> dict:
    """One-sided exact binomial, alternative 'greater'. Q1 FAILS when the
    exclusion rate is significantly above p0."""
    if n_sessions <= 0:
        return {"passes": False, "why": "no M-arm sessions"}
    p = binom_test_exact(n_excluded, n_sessions, p0, alternative="greater")
    return {"passes": bool(p >= ALPHA), "k": n_excluded, "n": n_sessions,
            "rate": n_excluded / n_sessions, "p0": p0, "p": float(p),
            "alpha": ALPHA,
            "reading": ("exclusion rate is not significantly above p0"
                        if p >= ALPHA else
                        "exclusion rate significantly ABOVE p0 -- the "
                        "apparatus is breaking down at this dose")}


def q2_readability(aucs, median_bar: float = MEDIAN_BAR,
                   pctl_bar: float = PCTL_BAR) -> dict:
    """Median and 10th percentile over the resampled AUCs."""
    vals = [a for a in (aucs or []) if a is not None]
    if not vals:
        return {"passes": False, "why": "no evaluable resamples",
                "n_resamples": 0}
    med = float(np.median(vals))
    p10 = float(np.percentile(vals, PCTL))
    ok_m, ok_p = med >= median_bar, p10 >= pctl_bar
    return {"passes": bool(ok_m and ok_p), "median": med, "p10": p10,
            "median_bar": median_bar, "p10_bar": pctl_bar,
            "median_ok": bool(ok_m), "p10_ok": bool(ok_p),
            "n_resamples": len(vals),
            "min": float(np.min(vals)), "max": float(np.max(vals))}


def q3_direction(delta_plus, delta_R, g: float = G_DEFAULT) -> dict:
    """Delta+ >= 0.5*G, Delta+ > 2*|Delta_R|, and no sign flip."""
    bar = 0.5 * g
    if delta_plus is None:
        return {"passes": False, "why": "Delta+ not evaluable", "bar": bar}
    flip = delta_plus < 0
    ok_mag = delta_plus >= bar
    ok_r = (delta_R is not None) and (delta_plus > 2 * abs(delta_R))
    return {"passes": bool(ok_mag and ok_r and not flip),
            "delta_plus": float(delta_plus), "bar": bar, "G": g,
            "magnitude_ok": bool(ok_mag),
            "delta_R": None if delta_R is None else float(delta_R),
            "beats_2x_random": bool(ok_r), "sign_flip": bool(flip),
            "reading": ("SIGN FLIP -- V1's overdose signature; the rung fails"
                        if flip else
                        "direction and magnitude as registered" if ok_mag
                        else "below the registered magnitude bar")}


def run_dose_rule(q1: dict, q2: dict, q3: dict) -> dict:
    """PROPOSAL-j §2. Computed BEFORE any artifact is written (trap 6)."""
    failing = [name for name, r in (("Q1", q1), ("Q2", q2), ("Q3", q3))
               if not r.get("passes")]
    if not failing:
        return {"run_dose": 0.20, "decision": "PROCEED",
                "statement": ("D2 passes Q1-Q3; the run dose is 0.20 and "
                              "LOCK-j instantiates.")}
    figs = []
    if "Q1" in failing:
        figs.append(f"Q1 {q1.get('k')}/{q1.get('n')} excluded, "
                    f"p = {q1.get('p'):.4f} vs p0 = {q1.get('p0')}"
                    if q1.get("p") is not None else f"Q1 {q1.get('why')}")
    if "Q2" in failing:
        figs.append(f"Q2 median {q2.get('median')}, 10th pct {q2.get('p10')}"
                    if q2.get("median") is not None else f"Q2 {q2.get('why')}")
    if "Q3" in failing:
        figs.append(f"Q3 Delta+ {q3.get('delta_plus')} vs bar "
                    f"{q3.get('bar'):.4f}"
                    + (", SIGN FLIP" if q3.get("sign_flip") else "")
                    if q3.get("delta_plus") is not None
                    else f"Q3 {q3.get('why')}")
    return {"run_dose": None, "decision": "STOP, SCOPED",
            "failing": failing, "failing_figures": figs,
            "statement": ("the weak-state boundary is not reachable with "
                          "coherence on this apparatus above MED at session "
                          "scale -- " + "; ".join(figs)),
            "no_fallback": ("No automatic fallback rung. A 0.15 rung is "
                            "licensable by addendum, never inherited "
                            "[PI-CHOICE: default = stop].")}


def evaluate(art: dict) -> dict:
    """Apply the three criteria to a D2 artifact."""
    excl = art.get("exclusions", {}).get("M", {})
    scope = art.get("exclusion_scope", "?")
    q1 = q1_validity(excl.get("excluded_run_scope", 0), excl.get("n", 0))
    q1["exclusion_scope"] = scope

    rd = (art.get("readability") or {}).get("k2_resampled") or {}
    q2 = q2_readability(rd.get("aucs"))

    mk = art.get("marker") or {}
    g = mk.get("G", G_DEFAULT)
    dd = (mk.get("deltas") or {}).get("clean", {})
    q3 = q3_direction((dd.get("delta_plus_within_M") or {}).get("delta"),
                      (dd.get("delta_R_within_R") or {}).get("delta"), g)
    q3["reading_used"] = "within-arm (M steered vs M unsteered)"
    q3["alternative_reading"] = q3_direction(
        (dd.get("delta_plus_vs_S_arm") or {}).get("delta"),
        (dd.get("delta_R_vs_S_arm") or {}).get("delta"), g)

    out = {"item": "e2d D2", "tier": art.get("tier"),
           "frac": art.get("frac"), "Q1": q1, "Q2": q2, "Q3": q3}
    out["descriptive"] = {
        "k1_resampled": (art.get("readability") or {}).get("k1_resampled"),
        "all_rounds_resampled": (art.get("readability") or {}
                                 ).get("all_rounds_resampled"),
        "transfer": (art.get("readability") or {}).get("transfer"),
        "AUC_R": (art.get("readability") or {}).get("auc_R"),
        "exclusions_strict_scope": excl.get("excluded_strict_scope"),
    }
    out["run_dose_rule"] = run_dose_rule(q1, q2, q3)
    return out


# --- stub smoke: every branch, on a synthetic battery ---------------------
def selftest() -> int:
    """Reaches every branch, including the sign-flip branch and the g2r
    pattern. No model, no data.

    Trap 5 is the shape of this test: each case must be shown to have RUN,
    so the counter below is asserted against the case list rather than a
    bare "no failures" print.
    """
    cases = []

    def case(name, got, want):
        cases.append((name, got, want, got == want))

    # --- Q1 ---------------------------------------------------------------
    case("Q1 clean 3/32 passes", q1_validity(3, 32)["passes"], True)
    case("Q1 fires at 9/32 (§2's stated reach)",
         q1_validity(9, 32)["passes"], False)
    case("Q1 8/32 still passes (the reach is 9, not 8)",
         q1_validity(8, 32)["passes"], True)
    case("Q1 empty arm fails", q1_validity(0, 0)["passes"], False)
    case("Q1 e2a's own rate under the e2a scope passes",
         q1_validity(10, 112)["passes"], True)
    # The scope flag, stated as it actually is. e2a's rate under the strict
    # scope (18/112 = 0.161) sits above p0 = 0.15 but does NOT reject at
    # n = 112 (p = .41). The hazard is Q1's OPERATING CHARACTERISTIC at D2's
    # n = 32: the false-alarm probability goes from 0.15% under the lenient
    # scope's rate to 6.0% under the strict scope's -- above the nominal
    # alpha, and 40x. That is what the flag is about.
    case("Q1 e2a's strict-scope rate does NOT reject at n = 112",
         q1_validity(18, 112)["passes"], True)
    case("Q1 the same rate is only 0.4149 from significance there",
         round(q1_validity(18, 112)["p"], 4), 0.4149)
    case("Q1 9/32 is the reach the proposal states",
         round(q1_validity(9, 32)["p"], 4), 0.0413)

    # --- Q2 ---------------------------------------------------------------
    case("Q2 all .80 passes", q2_readability([0.80] * 20)["passes"], True)
    g2r = [0.448] * 10 + [0.759] * 10          # the pattern it must fail on
    r = q2_readability(g2r)
    case("Q2 g2r pattern (.448/.759) FAILS", r["passes"], False)
    case("Q2 g2r median lands near .60",
         bool(0.55 <= r["median"] <= 0.65), True)
    # 2 low draws of 20 do NOT move a linearly-interpolated 10th percentile
    # (p10 = .886); 4 do (p10 = .300). Worth pinning: the criterion's tail
    # sensitivity is a property of B, and B is [LOCK-j: may be raised].
    case("Q2 high median, 4/20 low tail FAILS on the 10th pct",
         q2_readability([0.95] * 16 + [0.30] * 4)["passes"], False)
    case("Q2 high median, 2/20 low tail still PASSES (p10 = .886)",
         q2_readability([0.95] * 18 + [0.30, 0.31])["passes"], True)
    case("Q2 no resamples fails", q2_readability([])["passes"], False)
    case("Q2 median exactly at the bar passes",
         q2_readability([0.70] * 20)["passes"], True)

    # --- Q3 ---------------------------------------------------------------
    case("Q3 clean pass", q3_direction(0.40, 0.05)["passes"], True)
    case("Q3 below 0.5*G fails", q3_direction(0.10, 0.01)["passes"], False)
    case("Q3 SIGN FLIP fails (overdose signature)",
         q3_direction(-0.40, 0.01)["passes"], False)
    case("Q3 sign flip is reported as such",
         q3_direction(-0.40, 0.01)["sign_flip"], True)
    case("Q3 displacement-matched (Delta_R ~ Delta+) fails 2x rule",
         q3_direction(0.40, 0.30)["passes"], False)
    case("Q3 missing Delta_R fails", q3_direction(0.40, None)["passes"], False)
    case("Q3 missing Delta+ fails", q3_direction(None, 0.01)["passes"], False)
    case("Q3 bar is 0.158 at the registered G",
         round(q3_direction(0.4, 0.01)["bar"], 4), 0.1578)

    # --- run-dose rule, both branches ------------------------------------
    ok = {"passes": True}
    case("run-dose PROCEED when all three pass",
         run_dose_rule(ok, ok, ok)["run_dose"], 0.20)
    stop = run_dose_rule(q1_validity(9, 32), q2_readability(g2r),
                         q3_direction(-0.4, 0.01))
    case("run-dose STOP when all three fail", stop["decision"], "STOP, SCOPED")
    case("run-dose names every failing criterion",
         stop["failing"], ["Q1", "Q2", "Q3"])
    case("run-dose carries the failing figure",
         "SIGN FLIP" in stop["statement"], True)
    one = run_dose_rule(ok, ok, q3_direction(0.10, 0.01))
    case("run-dose STOPs on a single failure", one["decision"], "STOP, SCOPED")
    case("run-dose single failure names only it", one["failing"], ["Q3"])
    case("run-dose offers no fallback rung",
         "never inherited" in one["no_fallback"], True)

    # --- end-to-end over a synthetic artifact ----------------------------
    art = {"tier": "d2", "frac": 0.20, "exclusion_scope": "e2a",
           "exclusions": {"M": {"n": 32, "excluded_run_scope": 3,
                                "excluded_strict_scope": 7}},
           "readability": {"k2_resampled": {"aucs": [0.80] * 20}},
           "marker": {"G": G_DEFAULT, "deltas": {"clean": {
               "delta_plus_within_M": {"delta": 0.40},
               "delta_R_within_R": {"delta": 0.05},
               "delta_plus_vs_S_arm": {"delta": 0.38},
               "delta_R_vs_S_arm": {"delta": 0.04}}}}}
    ev = evaluate(art)
    case("end-to-end PROCEEDs on a clean synthetic artifact",
         ev["run_dose_rule"]["run_dose"], 0.20)
    case("end-to-end carries the alternative Q3 reading",
         ev["Q3"]["alternative_reading"]["passes"], True)
    art["marker"]["deltas"]["clean"]["delta_plus_within_M"]["delta"] = -0.4
    case("end-to-end STOPs when the artifact carries a sign flip",
         evaluate(art)["run_dose_rule"]["decision"], "STOP, SCOPED")
    ev2 = evaluate({"exclusions": {}, "readability": {}, "marker": {}})
    case("empty artifact STOPs rather than passing vacuously",
         ev2["run_dose_rule"]["decision"], "STOP, SCOPED")

    width = max(len(c[0]) for c in cases) + 2
    print("=" * 78)
    print("e2d D2 ANALYZER -- stub smoke (no model, no data)")
    print("=" * 78)
    for name, got, want, ok_ in cases:
        print(f"  [{'PASS' if ok_ else 'FAIL'}] {name:<{width}} "
              f"got {got!r:>18}  want {want!r}")
    n_fail = sum(1 for c in cases if not c[3])
    print("-" * 78)
    # trap 5: a case that never ran must not read as a pass.
    if len(cases) < 28:
        print(f"  INCOMPLETE: only {len(cases)} cases ran; the smoke is "
              f"specified at >= 28. Treating as FAILURE.")
        return 1
    print(f"  {len(cases) - n_fail}/{len(cases)} branches verified "
          f"(every criterion, both directions, plus the sign-flip and g2r "
          f"branches)")
    return 1 if n_fail else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifact", default=None)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    if args.selftest or not args.artifact:
        return selftest()

    art = json.load(open(args.artifact))
    if art.get("tier") != "d2":
        print(f"  NOTE: artifact tier is {art.get('tier')!r}, not 'd2'. "
              f"Evaluating anyway; D1 numbers carry no criterion.")
    out = evaluate(art)                     # computed before anything writes
    print(json.dumps(out, indent=1, default=float))
    if args.out:
        with open(args.out, "w") as fh:
            json.dump(out, fh, indent=1, default=float)
        print(f"  wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
