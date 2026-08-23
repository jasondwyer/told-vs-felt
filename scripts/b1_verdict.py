#!/usr/bin/env python3
"""B1 -- the Q1 verdict, read off the committed A4 artifacts. No new forwards.

LOCK-g §2 (licensed 2026-08-23): "Verdict per stage = the registered A4
potency criterion at ANY tested dose, read off the committed A4 artifacts."
The criterion is PROPOSAL-g §3-A4's envelope conjunction, already evaluated
per frac by `box_a4_hijack.py` and stored; this script reads it, applies the
registered mapping verbatim, and writes the artifact. It computes no new
quantity and re-tunes nothing.

The V1-lineage 0.5*G_c rule is reported as context and is NOT a criterion
here (LOCK-g §1, explicit). Guard profiles (A3) are reported alongside and
decide nothing (LOCK-g §2).

Code declares the reading the mapping produces; the DISPOSITION is the
design instance's -- the e2b pattern.

Usage:
    jlens-qwen36/.venv/bin/python scripts/b1_verdict.py
"""
from __future__ import annotations

import argparse
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "data")
STAGES = ("base", "sft", "dpo", "instruct")

MAPPING = {
    "base_pass": "bet confirmed -- marking is a pretraining acquisition",
    "base_fail_later_pass": "bet falsified -- marking enters at the first "
                            "passing stage",
    "all_fail": "marking does not transfer to this lineage/apparatus; a "
                "harness-validation review precedes any claim (ledger rule 2)",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(DATA, "olmo/b1_verdict.json"))
    args = ap.parse_args()

    per_stage = {}
    for s in STAGES:
        h = json.load(open(os.path.join(DATA, f"olmo/a4_hijack_{s}.json")))
        g = json.load(open(os.path.join(DATA, f"olmo/a4_instrument_{s}.json")))
        a3 = json.load(open(os.path.join(DATA, f"olmo/a3_axes_{s}.json")))
        passing = sorted((f for f, v in h["ladder"].items() if v["potency"]),
                         key=float)
        L = h["selected_layer"]
        guards = next(r for r in a3["report"]["span"] if r["layer"] == L)
        per_stage[s] = {
            "selected_layer": L,
            "passing_fracs": [float(f) for f in passing],
            "minimum_effective_dose": h["minimum_effective_dose"],
            "verdict": "PASS" if passing else "FAIL",
            "conjuncts_at_med": (h["ladder"][str(h["minimum_effective_dose"])]
                                 ["potency_conjuncts"] if passing else None),
            "G_c": g["G_c"],
            "v1_lineage_any_frac": any(v["v1_lineage"]
                                       for v in h["ladder"].values()),
            "guard_profile_at_selected_layer": {
                "cos_char": guards["cos_span_character"],
                "v2_self_residual_frac": guards["v2_self_residual_frac"],
                "v3_eval_residual_frac": guards["v3_eval_residual_frac"]},
        }

    base_pass = per_stage["base"]["verdict"] == "PASS"
    later_pass = [s for s in STAGES[1:] if per_stage[s]["verdict"] == "PASS"]
    if base_pass:
        branch, reading = "base_pass", MAPPING["base_pass"]
    elif later_pass:
        branch, reading = "base_fail_later_pass", MAPPING["base_fail_later_pass"]
    else:
        branch, reading = "all_fail", MAPPING["all_fail"]

    out = {"item": "B1", "question": "Q1 -- marking-when",
           "registered_bet": "present at Base -- marking is a pretraining "
                             "acquisition (2026-08-18, pre-R_l-survey)",
           "criterion": "PROPOSAL-g §3-A4 envelope conjunction at ANY tested "
                        "dose, per LOCK-g §2",
           "lock": "LOCK-g v1.1", "new_forwards": 0,
           "per_stage": per_stage, "branch": branch, "reading": reading,
           "first_passing_stage": next(
               (s for s in STAGES if per_stage[s]["verdict"] == "PASS"), None),
           "v1_lineage_context_only": {
               s: per_stage[s]["v1_lineage_any_frac"] for s in STAGES},
           "_disposition": ("Code applies the registered mapping and reports. "
                            "The disposition is the design instance's."),
           }

    print("=== B1 -- Q1 verdict (no new forwards; LOCK-g v1.1 §2) ===")
    print(f"  registered bet: {out['registered_bet']}")
    print(f"\n  {'stage':<9} {'layer':>6} {'passing fracs':>22} {'MED':>6} "
          f"{'verdict':>8}")
    for s in STAGES:
        v = per_stage[s]
        print(f"  {s:<9} L{v['selected_layer']:<5} "
              f"{str(v['passing_fracs']):>22} "
              f"{str(v['minimum_effective_dose']):>6} {v['verdict']:>8}")
    print(f"\n  branch: {branch}")
    print(f"  READING: {reading}")
    print(f"\n  context only, never a criterion here:")
    print(f"    V1-lineage rule passes at any frac: "
          f"{out['v1_lineage_context_only']}")
    print(f"  guard profiles (A3, decide nothing):")
    for s in STAGES:
        g = per_stage[s]["guard_profile_at_selected_layer"]
        print(f"    {s:<9} cos_char {g['cos_char']:.3f}  "
              f"V2_self {g['v2_self_residual_frac']:.3f}  "
              f"V3_eval {g['v3_eval_residual_frac']:.3f}")
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\n  wrote {args.out}")
    print("  DISPOSITION IS THE DESIGN INSTANCE'S.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
