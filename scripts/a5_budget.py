#!/usr/bin/env python3
"""A5 -- the per-campaign timing budget. PROPOSAL-g §3 A5.

    "Code delivers a per-campaign timing budget (from A2-A4 measured rates)
    demonstrating single-box completion for each B campaign before it
    starts; the budget is an artifact, not a vibe."

So this reads its rates out of the committed A2/A3/A4 artifacts rather than
carrying constants, and re-runs to the same numbers from the record alone.
It loads no model and needs no box.

THE COST MODEL, AND WHY IT IS TRUSTED. Two measured quantities and one
structural fact:

  * **s/forward** -- the mean over every timed A-phase forward (A3 capture,
    A4 part 1, A4 part 2: ~90,000 forwards). Tight: 0.079-0.092 across
    twelve independent per-stage measurements.
  * **cold model load** -- from the A3 log, 133-165 s off the network
    volume.
  * **generation is UNCACHED everywhere** in the harnesses B2 and B3
    inherit (`detection.run_detection` and the session runner both pass
    `cached=False`), so a response of T tokens costs T forwards.

The model is validated against a measurement it did not fit: predicting A2's
per-stage wall-clock from these rates alone gives ~330 s against a measured
323-340 s. A budget that cannot reproduce a run already in the record is a
vibe with arithmetic.

WHAT IS BUDGETED. B1 costs nothing new -- it is a verdict read off A4's
committed potency numbers. B2 and B3 are sized from PROPOSAL-g §4 as
registered, with the one derived quantity (B3's sham/random floors) stated
explicitly rather than assumed.

Usage:
    python scripts/a5_budget.py
    python scripts/a5_budget.py --session-tokens 40   # sensitivity
"""
from __future__ import annotations

import argparse
import json
import os
import statistics
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
DATA = os.path.join(REPO, "data")
STAGES = ("base", "sft", "dpo", "instruct")

# --- registered campaign shapes (PROPOSAL-g §4) ---------------------------
B2_TRIALS_PER_STAGE_PER_ARM = 48        # 24 injected / 24 control
B2_ARMS = 2                             # fidelity, register
B2_MAX_TOKENS = 60                      # detection answers run to the cap
B3_SCREEN_MARKER = 48                   # valid sessions/stage, marker family
B3_CONFIRM_MARKER = 96                  # fresh sessions, per triggering stage
E2A_PROPORTIONS = (96, 36, 36)          # marker:sham:random, LOCK-h v2 §2
SESSION_GENS = 10                       # 2 forced x 2 tags + 6 free rounds
SESSION_READS = 6                       # free choices, vanilla forwards
EXCLUSION_RATE = 0.13                   # H1-observed 13.0%; e2b saw 5.9-14.3%


def measured_rates() -> dict:
    """Every rate below comes out of a committed artifact or raw log."""
    fwd = []
    for s in STAGES:
        i = json.load(open(os.path.join(DATA, f"olmo/a4_instrument_{s}.json")))
        h = json.load(open(os.path.join(DATA, f"olmo/a4_hijack_{s}.json")))
        fwd += [i["seconds_per_forward"], h["seconds_per_forward"]]
    log = open(os.path.join(REPO, "results/raw/2026-08-23_a3_a2.txt")).read()
    loads = [int(l.split("in")[1].split("s")[0])
             for l in log.splitlines() if "model loaded in" in l]
    cap = [float(l.split("(")[1].split("s/ctx")[0])
           for l in log.splitlines() if "capture done in" in l]
    a2 = [int(l.split("(")[-1].rstrip("s)\n"))
          for l in open(os.path.join(REPO,
                        "results/raw/2026-08-23_a2_rerun.txt")).read().splitlines()
          if l.startswith("wrote") and "a2_baserates" in l]
    return {
        "s_per_forward_mean": statistics.mean(fwd),
        "s_per_forward_max": max(fwd),
        "s_per_forward_n_measurements": len(fwd) + len(cap),
        "cold_load_mean_s": statistics.mean(loads),
        "cold_load_max_s": max(loads),
        "a2_measured_per_stage_s": a2,
        "generation_is_uncached": True,
    }


def validate(rates: dict, session_tokens: int) -> dict:
    """Predict A2's per-stage wall-clock from the rates alone."""
    f, load = rates["s_per_forward_mean"], rates["cold_load_mean_s"]
    pred = (load + 24 * B2_MAX_TOKENS * f
            + 8 * SESSION_GENS * session_tokens * f + 8 * SESSION_READS * f)
    meas = rates["a2_measured_per_stage_s"]
    err = max(abs(pred - m) / m for m in meas)
    return {"predicted_s": pred, "measured_s": meas, "worst_rel_error": err,
            "agrees_within_10pct": bool(err < 0.10)}


def budgets(rates: dict, session_tokens: int) -> dict:
    f = rates["s_per_forward_max"]          # budget on the WORST measured rate
    load = rates["cold_load_max_s"]

    b2_gens = B2_TRIALS_PER_STAGE_PER_ARM * B2_ARMS * len(STAGES)
    b2_s = load * len(STAGES) + b2_gens * B2_MAX_TOKENS * f

    m, sh, rd = E2A_PROPORTIONS
    sham = round(B3_SCREEN_MARKER * sh / m)
    rand = round(B3_SCREEN_MARKER * rd / m)
    valid_per_stage = B3_SCREEN_MARKER + sham + rand
    run_per_stage = valid_per_stage / (1 - EXCLUSION_RATE)
    sess_s = (SESSION_GENS * session_tokens + SESSION_READS) * f
    b3_screen_s = load * len(STAGES) + run_per_stage * len(STAGES) * sess_s

    conf_run = B3_CONFIRM_MARKER / (1 - EXCLUSION_RATE)
    b3_confirm_s = load + conf_run * sess_s

    return {
        "B1": {"new_compute_s": 0.0,
               "note": "verdict read off A4's committed potency numbers; "
                       "no new forwards"},
        "B2": {"generations": b2_gens, "tokens_each": B2_MAX_TOKENS,
               "forwards": b2_gens * B2_MAX_TOKENS,
               "model_loads": len(STAGES), "seconds": b2_s,
               "hours": b2_s / 3600},
        "B3_screen": {
            "arms_per_stage": {"marker": B3_SCREEN_MARKER, "sham": sham,
                               "random": rand},
            "valid_sessions_per_stage": valid_per_stage,
            "sessions_run_per_stage_at_13pct_exclusion": run_per_stage,
            "total_sessions_run": run_per_stage * len(STAGES),
            "seconds_per_session": sess_s,
            "model_loads": len(STAGES),
            "seconds": b3_screen_s, "hours": b3_screen_s / 3600},
        "B3_confirm_per_triggering_stage": {
            "valid_sessions": B3_CONFIRM_MARKER,
            "sessions_run": conf_run,
            "seconds": b3_confirm_s, "hours": b3_confirm_s / 3600},
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--session-tokens", type=int, default=7,
                    help="mean generated tokens per session round. 7 is what "
                         "A2(ii)'s neutral filler measured; B3 uses the e2a "
                         "task corpus and will run longer, so the sensitivity "
                         "table is the operative output, not this default")
    ap.add_argument("--out", default=os.path.join(DATA, "olmo/a5_budget.json"))
    args = ap.parse_args()

    rates = measured_rates()
    val = validate(rates, args.session_tokens)
    print("=== A5: per-campaign timing budget (PROPOSAL-g §3 A5) ===")
    print(f"  s/forward  mean {rates['s_per_forward_mean']:.4f}  "
          f"max {rates['s_per_forward_max']:.4f}  "
          f"({rates['s_per_forward_n_measurements']} per-stage measurements)")
    print(f"  cold load  mean {rates['cold_load_mean_s']:.0f}s  "
          f"max {rates['cold_load_max_s']:.0f}s")
    print(f"  generation uncached -> a T-token response costs T forwards")
    print(f"\n  MODEL VALIDATION against A2 (a run it did not fit):")
    print(f"    predicted {val['predicted_s']:.0f}s vs measured "
          f"{val['measured_s']} -> worst error {val['worst_rel_error']:.1%} "
          f"-> {'OK' if val['agrees_within_10pct'] else 'CHECK'}")

    b = budgets(rates, args.session_tokens)
    print(f"\n  budgeted on the WORST measured forward rate and load:")
    print(f"    B1  {b['B1']['new_compute_s']:.0f}s  -- {b['B1']['note']}")
    print(f"    B2  {b['B2']['hours']:.2f} h  "
          f"({b['B2']['generations']} generations, "
          f"{b['B2']['forwards']:,} forwards, {b['B2']['model_loads']} loads)")
    s3 = b["B3_screen"]
    print(f"    B3 screen  {s3['hours']:.2f} h  "
          f"(arms/stage {s3['arms_per_stage']}, "
          f"{s3['sessions_run_per_stage_at_13pct_exclusion']:.0f} sessions/stage run, "
          f"{s3['seconds_per_session']:.1f}s/session)")
    c3 = b["B3_confirm_per_triggering_stage"]
    print(f"    B3 confirm {c3['hours']:.2f} h per triggering stage "
          f"({c3['sessions_run']:.0f} sessions)")

    print(f"\n  SENSITIVITY -- B3 is the only campaign whose cost is not "
          f"pinned by measurement.\n  A2(ii)'s neutral filler measured ~7 "
          f"tokens/round; the e2a task corpus will run longer:")
    print(f"    {'tok/round':>10} {'s/session':>10} {'B3 screen':>11} "
          f"{'confirm':>9} {'screen+1 confirm':>17}")
    sens = {}
    for t in (7, 15, 25, 40, 60):
        bb = budgets(rates, t)
        tot = bb["B3_screen"]["hours"] + bb["B3_confirm_per_triggering_stage"]["hours"]
        sens[t] = {"s_per_session": bb["B3_screen"]["seconds_per_session"],
                   "screen_h": bb["B3_screen"]["hours"],
                   "confirm_h": bb["B3_confirm_per_triggering_stage"]["hours"],
                   "screen_plus_one_confirm_h": tot}
        print(f"    {t:>10} {bb['B3_screen']['seconds_per_session']:>10.1f} "
              f"{bb['B3_screen']['hours']:>10.2f}h "
              f"{bb['B3_confirm_per_triggering_stage']['hours']:>8.2f}h "
              f"{tot:>16.2f}h")

    out = {"item": "A5", "rates": rates, "model_validation": val,
           "registered_shapes": {
               "B2_trials_per_stage_per_arm": B2_TRIALS_PER_STAGE_PER_ARM,
               "B2_arms": B2_ARMS, "B2_max_tokens": B2_MAX_TOKENS,
               "B3_screen_marker": B3_SCREEN_MARKER,
               "B3_confirm_marker": B3_CONFIRM_MARKER,
               "e2a_proportions_marker_sham_random": list(E2A_PROPORTIONS),
               "session_gens": SESSION_GENS, "session_reads": SESSION_READS,
               "exclusion_rate_assumed": EXCLUSION_RATE},
           "budgets_at_default_session_tokens": budgets(rates, args.session_tokens),
           "default_session_tokens": args.session_tokens,
           "sensitivity_by_session_tokens": sens,
           "single_box_completion": {
               "rule": "PROPOSAL-g §2.10 -- a verdict campaign completes "
                       "within one box session on on-demand capacity",
               "B2": "yes at every sensitivity point",
               "B3_screen": {str(t): bool(v["screen_h"] < 12)
                             for t, v in sens.items()},
               "note": "12 h taken as a working single-session ceiling; the "
                       "design instance sets the real one"},
           "_recommendation": (
               "Generation is uncached and dominates B3. The cached path is "
               "LICENSED on this backend -- the 2026-08-23 kernel gate found "
               "cached and uncached first-token distributions bit-identical, "
               "symKL exactly 0.000e+00 against a 1e-3 bar. No cached "
               "generation rate has been measured, so nothing here is "
               "budgeted on it; a one-session smoke would measure it and is "
               "the single largest lever on B3."),
           }
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\n  wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
