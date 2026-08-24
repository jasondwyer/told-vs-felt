#!/usr/bin/env python3
"""B2 analysis -- the positive-control logic. LOCK-g §3 / PROPOSAL-g §4-B2.

COMMITTED BEFORE ANY CAMPAIGN RUNS, as B3's analyzer was and e2b's before
that. Macar's DPO transition is our positive control, so the criterion that
decides whether it replicated must predate the data that answers it.

THE CRITERION, verbatim in effect: the transition replicates iff, IN THE
FIDELITY ARM, the sensitivity CI **excludes 0 at DPO and Instruct** AND
**includes 0 at Base and SFT**. If no stage clears chance in the fidelity
arm at all, that is a **harness-validation stop** -- a design-instance
discussion checked against Macar's reported effect sizes -- and NOT a
finding. Other patterns are findings with named readings: earlier onset
(SFT onward), later onset (Instruct only), no transition (all four clear).

SENSITIVITY = hit - false alarm. d' is NOT computed: it needs a
distributional assumption this design has not earned.

THE INTERVAL, stated because "exact CIs" does not name one. Each rate gets a
**Clopper-Pearson** interval, exact by construction, obtained by inverting
the binomial CDF by bisection (no scipy on this laptop). The difference then
gets a **Newcombe** interval built from those two exact intervals -- the
standard conservative construction for a difference of independent
proportions. "Exact" describes the per-rate intervals; the difference
interval is conservative rather than exact, and saying so is cheaper than
being caught not knowing.

DECIDABLE-N FLOORS bind here. A cell below LOCK-g §3's 16-of-24 floor is
reported descriptively with a flag and is NOT silently read as "includes 0"
-- A2 measured Instruct at 50% undecidable, so this is expected to bite
exactly where the criterion is most load-bearing.

Usage:
    jlens-qwen36/.venv/bin/python scripts/b2_analyze.py --dir data/olmo
    jlens-qwen36/.venv/bin/python scripts/b2_analyze.py --selftest
"""
from __future__ import annotations

import argparse
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from valence_core.stats import binom_cdf, binom_sf_inclusive      # noqa: E402

STAGES = ("base", "sft", "dpo", "instruct")
ALPHA = 0.05


def clopper_pearson(k: int, n: int, alpha: float = ALPHA) -> tuple:
    """Exact interval, by bisecting the binomial CDF. No scipy (trap 1)."""
    if n == 0:
        return (float("nan"), float("nan"))
    lo, hi = 0.0, 1.0
    if k > 0:
        a, b = 0.0, 1.0
        for _ in range(200):
            m = (a + b) / 2
            if binom_sf_inclusive(k, n, m) < alpha / 2:
                a = m
            else:
                b = m
        lo = (a + b) / 2
    if k < n:
        a, b = 0.0, 1.0
        for _ in range(200):
            m = (a + b) / 2
            if binom_cdf(k, n, m) > alpha / 2:
                a = m
            else:
                b = m
        hi = (a + b) / 2
    return (lo, hi)


def newcombe(k1, n1, k2, n2, alpha=ALPHA) -> tuple:
    """Difference interval from two exact per-rate intervals."""
    p1, p2 = (k1 / n1 if n1 else float("nan")), (k2 / n2 if n2 else float("nan"))
    l1, u1 = clopper_pearson(k1, n1, alpha)
    l2, u2 = clopper_pearson(k2, n2, alpha)
    d = p1 - p2
    lo = d - ((p1 - l1) ** 2 + (u2 - p2) ** 2) ** 0.5
    hi = d + ((u1 - p1) ** 2 + (p2 - l2) ** 2) ** 0.5
    return (lo, hi)


def cell(art: dict) -> dict:
    tr = art["trials"]
    inj = [t for t in tr if t["injected"] and t["claimed_detection"] is not None]
    ctl = [t for t in tr if not t["injected"] and t["claimed_detection"] is not None]
    hk = sum(1 for t in inj if t["claimed_detection"])
    fk = sum(1 for t in ctl if t["claimed_detection"])
    ident = [t for t in tr if t["injected"] and t["identified"] is not None]
    lo, hi = newcombe(hk, len(inj), fk, len(ctl))
    floors = art["decidable_n_floors"]
    return {"stage": art["stage"], "arm": art["arm"],
            "hit_rate": hk / len(inj) if inj else float("nan"),
            "false_alarm_rate": fk / len(ctl) if ctl else float("nan"),
            "sensitivity": (hk / len(inj) - fk / len(ctl))
                           if inj and ctl else float("nan"),
            "ci": [lo, hi], "ci_excludes_0": bool(inj and ctl and lo > 0),
            "n_injected_decidable": len(inj), "n_control_decidable": len(ctl),
            "identification_rate": (sum(1 for t in ident if t["identified"])
                                    / len(ident)) if ident else float("nan"),
            "undecidable_rate": 1 - (len(inj) + len(ctl)) / max(len(tr), 1),
            "cell_evaluable": floors["cell_evaluable"],
            "floor_diagnosis": [floors["diagnosis_injected"],
                                floors["diagnosis_control"]]}


def read_pattern(fid: dict) -> dict:
    """The registered mapping, applied to the fidelity arm only."""
    clears = {s: (fid[s]["ci_excludes_0"] if s in fid else None) for s in STAGES}
    evaluable = {s: (fid[s]["cell_evaluable"] if s in fid else None)
                 for s in STAGES}
    have = [s for s in STAGES if clears[s] is not None]
    if len(have) < 4:
        return {"reading": "INCOMPLETE -- not all four fidelity cells present",
                "clears": clears, "evaluable": evaluable}
    c = [clears[s] for s in STAGES]
    if not any(c):
        r = ("HARNESS-VALIDATION STOP -- no stage clears chance in the "
             "fidelity arm. Design-instance discussion against Macar's "
             "reported effect sizes; NOT a finding.")
    elif c == [False, False, True, True]:
        r = "TRANSITION REPLICATES AT DPO -- the registered positive control"
    elif all(c):
        r = "NO TRANSITION -- all four stages above chance"
    elif c == [False, True, True, True]:
        r = "EARLIER ONSET (SFT onward) -- a finding with a named reading"
    elif c == [False, False, False, True]:
        r = "LATER ONSET (Instruct only) -- a finding with a named reading"
    else:
        r = ("PARTIAL PATTERN, unnamed -- reported as-is for design-instance "
             "reading; no registered label covers it")
    flagged = [s for s in STAGES if evaluable.get(s) is False]
    return {"reading": r, "clears": clears, "evaluable": evaluable,
            "cells_below_decidable_floor": flagged,
            "floor_caveat": ("a below-floor cell is descriptive and is NOT "
                             "read as 'includes 0'" if flagged else None)}


def analyze(cells: dict) -> dict:
    fid = {c["stage"]: c for c in cells.values() if c["arm"] == "fidelity"}
    reg = {c["stage"]: c for c in cells.values() if c["arm"] == "register"}
    delta = {s: (reg[s]["sensitivity"] - fid[s]["sensitivity"])
             for s in STAGES if s in reg and s in fid}
    out = {"item": "B2 analysis", "fidelity": fid, "register": reg,
           "positive_control": read_pattern(fid),
           "elicitation_dependence_register_minus_fidelity": delta,
           "confound_check_undecidable_rates": {
               s: fid[s]["undecidable_rate"] for s in fid},
           "_note": ("any DPO-onset result is additionally checked against "
                     "undecidable-rate shifts before the transition is "
                     "claimed (PROPOSAL-g §4-B2 confound note)"),
           "_disposition": "Code reports what the criterion returns. The "
                           "disposition is the design instance's."}
    return out


def _synth(stage, arm, hit_k, fa_k, n=24, undec=0):
    tr = []
    for i in range(n):
        d = None if i < undec else (i < hit_k + undec)
        tr.append({"injected": True, "claimed_detection": d,
                   "identified": bool(d)})
    for i in range(n):
        d = None if i < undec else (i < fa_k + undec)
        tr.append({"injected": False, "claimed_detection": d,
                   "identified": None})
    dec_i = sum(1 for t in tr if t["injected"] and t["claimed_detection"] is not None)
    dec_c = sum(1 for t in tr if not t["injected"] and t["claimed_detection"] is not None)
    return {"stage": stage, "arm": arm, "trials": tr,
            "decidable_n_floors": {"cell_evaluable": dec_i >= 16 and dec_c >= 16,
                                   "diagnosis_injected": None,
                                   "diagnosis_control": None}}


def selftest() -> int:
    def build(pattern, arm="fidelity", undec=0):
        return {f"{s}-{arm}": cell(_synth(s, arm, k, 1, undec=undec))
                for s, k in zip(STAGES, pattern)}
    cases = [
        ("registered DPO transition (2,2,20,20 hits vs 1 FA)",
         build([2, 2, 20, 20]), "TRANSITION REPLICATES AT DPO"),
        ("nothing clears anywhere -> harness-validation stop",
         build([1, 1, 1, 1]), "HARNESS-VALIDATION STOP"),
        ("everything clears -> no transition", build([20, 20, 20, 20]),
         "NO TRANSITION"),
        ("earlier onset from SFT", build([2, 20, 20, 20]), "EARLIER ONSET"),
        ("later onset, Instruct only", build([2, 2, 2, 20]), "LATER ONSET"),
        ("DPO only -> unnamed partial pattern", build([2, 2, 20, 2]),
         "PARTIAL PATTERN"),
    ]
    ok = True
    print("=== b2_analyze self-test (pre-committed, before any real data) ===")
    for label, cells, want in cases:
        got = analyze(cells)["positive_control"]["reading"]
        good = got.startswith(want)
        ok &= good
        print(f"  [{'PASS' if good else 'FAIL'}] {label}")
        print(f"         expected {want!r} -> got {got.split(' -- ')[0]!r}")
    # a below-floor cell must be flagged, not silently read
    cells = build([2, 2, 20, 20], undec=12)
    pc = analyze(cells)["positive_control"]
    good = pc["cells_below_decidable_floor"] == list(STAGES)
    ok &= good
    print(f"  [{'PASS' if good else 'FAIL'}] 12/24 undecidable flags every "
          f"cell below the 16-of-24 floor")
    # The exact interval checked against its CLOSED FORM, not against a
    # remembered figure. For k=0 the two-sided 1-alpha Clopper-Pearson upper
    # bound is exactly 1 - (alpha/2)^(1/n); a first pass here asserted a
    # loose band and annotated it "~0.117", which is the ONE-sided bound --
    # the computation was right and the comment was wrong, which is the way
    # round that survives review.
    lo, hi = clopper_pearson(0, 24)
    closed = 1 - (ALPHA / 2) ** (1 / 24)
    good = lo == 0.0 and abs(hi - closed) < 1e-9
    ok &= good
    print(f"  [{'PASS' if good else 'FAIL'}] Clopper-Pearson(0/24) upper "
          f"{hi:.6f} == closed form 1-(a/2)^(1/n) {closed:.6f}")
    print(f"  {'ALL PASS' if ok else 'FAILURES PRESENT'}")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=os.path.join(REPO, "data/olmo"))
    ap.add_argument("--out", default=None)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    cells = {}
    for arm in ("fidelity", "register"):
        for s in STAGES:
            p = os.path.join(args.dir, f"b2_{arm}_{s}.json")
            if os.path.exists(p):
                cells[f"{s}-{arm}"] = cell(json.load(open(p)))
    if not cells:
        raise SystemExit(f"no B2 artifacts under {args.dir}")
    res = analyze(cells)
    print("=== B2 analysis ===")
    for arm in ("fidelity", "register"):
        for s in STAGES:
            c = res[arm].get(s)
            if not c:
                continue
            print(f"  {arm:<9} {s:<9} hit {c['hit_rate']:.3f} fa "
                  f"{c['false_alarm_rate']:.3f}  sens "
                  f"{c['sensitivity']:+.3f}  CI [{c['ci'][0]:+.3f}, "
                  f"{c['ci'][1]:+.3f}]  excl0 {c['ci_excludes_0']}  "
                  f"evaluable {c['cell_evaluable']}")
    print(f"\n  POSITIVE CONTROL: {res['positive_control']['reading']}")
    if res["positive_control"].get("cells_below_decidable_floor"):
        print(f"  below floor: "
              f"{res['positive_control']['cells_below_decidable_floor']}")
    if args.out:
        json.dump(res, open(args.out, "w"), indent=1)
        print(f"  wrote {args.out}")
    print("  DISPOSITION IS THE DESIGN INSTANCE'S.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
