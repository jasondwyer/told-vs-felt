#!/usr/bin/env python3
"""B2-r analyzer — [g3-A], [g3-B] and the §3 exploration reading.

COMMITTED BEFORE ANY B2-r TRIAL, as b2_analyze and b3_analyze were before
their campaigns. ADDENDUM-g3 v1.1 §5.

THE THREE READINGS, and only the first two are criteria:

  [g3-A] CONTROL / specificity (§1) — the positive control, dose-free.
      Replicates iff the exact Clopper-Pearson FPR interval at Base AND at
      SFT each separate ABOVE the interval at DPO AND at Instruct. Four
      separations, all required. This is the quantity their OLMo transition
      actually occupies: base/sft affirm promiscuously (16.4%/22.5%) and
      post-training collapses it to ~0. The retired sensitivity criterion
      demanded significance where their effect is smallest (+0.6 pp at
      Instruct) and had power 0.000 at n=48.

  [g3-B] QUALIFICATION / dose (§2) — injected about-rate separates above the
      uninjected control rate, pooled over the four concepts, per strength.
      MED_c is the LOWEST strength passing both this and the coherence gate.

  §3 EXPLORATION — NOT a criterion. Per-stage TPR/FPR/sensitivity with
      two-sided intervals. A null here concludes nothing: their own OLMo
      aggregate (2.9% at DPO) sits below this n's ~0.15-0.20 detection floor.
      A CI excluding 0 upward is a screen hit that licenses a fresh
      pre-registration and issues no claim.

TWO-SIDED THROUGHOUT. `ci_state` returns excludes_upward / excludes_downward /
includes. b2_analyze set `ci_excludes_0` only when the lower bound cleared 0,
so a significantly NEGATIVE sensitivity — a model claiming detection more on
controls, which is their Base — was filed identically to chance. That is a
substantive result and it now has its own name.

Usage:
    jlens-qwen36/.venv/bin/python scripts/b2r_analyze.py --selftest
    jlens-qwen36/.venv/bin/python scripts/b2r_analyze.py --dir data/olmo
"""
from __future__ import annotations

import argparse
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "scripts"))

from b2_analyze import clopper_pearson, newcombe                 # noqa: E402
from valence_core.detection_v2 import ci_state                   # noqa: E402

STAGES = ("base", "sft", "dpo", "instruct")
HIGH, LOW = ("base", "sft"), ("dpo", "instruct")
CONTROL_FLOOR = 64      # of 96 decidable, §1
EXPLORE_FLOOR = 32      # of 48 per cell, §3


def separates_above(k_hi, n_hi, k_lo, n_lo) -> bool:
    """CP lower bound of the high rate exceeds CP upper bound of the low one."""
    lo_hi, _ = clopper_pearson(k_hi, n_hi)
    _, hi_lo = clopper_pearson(k_lo, n_lo)
    return lo_hi > hi_lo


def g3a(control: dict) -> dict:
    """[g3-A]: four pairwise separations, all required."""
    rates, seps = {}, {}
    for s in STAGES:
        c = control.get(s)
        if not c:
            return {"criterion": "[g3-A]", "reading": "INCOMPLETE — not all "
                    "four stages present", "rates": rates}
        k, n = c["affirm"], c["decidable"]
        lo, hi = clopper_pearson(k, n)
        rates[s] = {"fpr": (k / n if n else float("nan")), "k": k, "n": n,
                    "ci": [lo, hi], "meets_floor": n >= CONTROL_FLOOR}
    for h in HIGH:
        for l in LOW:
            seps[f"{h}>{l}"] = separates_above(
                control[h]["affirm"], control[h]["decidable"],
                control[l]["affirm"], control[l]["decidable"])
    allsep = all(seps.values())
    hi_zero = all(rates[h]["ci"][1] < 0.05 for h in HIGH)
    lo_hi = all(rates[l]["fpr"] > 0.05 for l in LOW)
    if allsep:
        r = ("TRANSITION REPLICATES — specificity acquired across "
             "post-training, the quantity their OLMo result occupies")
    elif hi_zero:
        r = ("SCOPED NEGATIVE — Base/SFT affirm ~never; their transition's "
             "LOW END does not exist under completion format at their "
             "decoding. No power confound, no dose argument.")
    elif lo_hi:
        r = ("NO TRANSITION — FPR elevated at all stages; the specificity "
             "acquisition does not survive our regime's post-trained stages")
    else:
        r = "UNNAMED PARTIAL — licenses at most a fresh pre-registration"
    return {"criterion": "[g3-A]", "reading": r, "separations": seps,
            "all_four_separate": allsep, "rates": rates,
            "cells_below_floor": [s for s in STAGES
                                  if not rates[s]["meets_floor"]]}


def g3b(ladder: dict) -> dict:
    """[g3-B]: per strength, injected about-rate separates above control."""
    out, med = {}, None
    ctl = ladder["control"]
    for strength in sorted(ladder["injected"], key=float):
        c = ladder["injected"][strength]
        sep = separates_above(c["about"], c["n"], ctl["about"], ctl["n"])
        coh = c["degenerate_frac"] <= 0.25
        passes = bool(sep and coh)
        lo, hi = clopper_pearson(c["about"], c["n"])
        out[strength] = {"about_rate": c["about"] / c["n"] if c["n"] else float("nan"),
                         "ci": [lo, hi], "separates": sep,
                         "degenerate_frac": c["degenerate_frac"],
                         "coherent": coh, "passes": passes}
        if passes and med is None:
            med = float(strength)
    return {"criterion": "[g3-B]", "MED_c": med, "ladder": out,
            "hard_stop": med is None,
            "note": ("MED_c is the LOWEST strength passing potency AND "
                     "coherence; no pass -> this stage HARD-STOPS in §3")}


def explore(cell: dict) -> dict:
    """§3: descriptive-with-intervals. No criterion attaches."""
    ki, ni = cell["hit"], cell["inj_decidable"]
    kf, nf = cell["fa"], cell["ctl_decidable"]
    lo, hi = newcombe(ki, ni, kf, nf)
    return {"tpr": ki / ni if ni else float("nan"),
            "fpr": kf / nf if nf else float("nan"),
            "sensitivity": (ki / ni - kf / nf) if ni and nf else float("nan"),
            "ci": [lo, hi], "ci_state": ci_state(lo, hi),
            "meets_floor": ni >= EXPLORE_FLOOR and nf >= EXPLORE_FLOOR,
            "screen_hit": ci_state(lo, hi) == "excludes_upward",
            "note": ("a screen hit licenses a fresh confirmatory "
                     "pre-registration and issues no claim; a null concludes "
                     "nothing at this n (their aggregate 2.9% is below the "
                     "~0.15-0.20 floor)")}


# --- pre-committed synthetic battery (v1.1 §5) ----------------------------
def _ctl(rates, n=96):
    return {s: {"affirm": round(r * n), "decidable": n}
            for s, r in zip(STAGES, rates)}


def selftest() -> int:
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got.startswith(want)
        ok &= good
        print(f"  [{'PASS' if good else 'FAIL'}] {label}")
        print(f"         expected {want!r} -> got {got.split(' — ')[0]!r}")

    print("=== b2r_analyze self-test (pre-committed, before any B2-r data) ===")
    print("\n-- [g3-A] the five declared cases --")
    # 1. their published OLMo pattern
    chk("true specificity transition (their rates: .164/.225/.000/.003)",
        g3a(_ctl([0.164, 0.225, 0.000, 0.003]))["reading"],
        "TRANSITION REPLICATES")
    # 2. flat high
    chk("flat-high-FPR lineage -> no transition",
        g3a(_ctl([0.20, 0.20, 0.20, 0.20]))["reading"], "NO TRANSITION")
    # 3. flat zero -> the safely-reached scoped negative
    chk("flat-zero lineage -> scoped negative (B2's own regime)",
        g3a(_ctl([0.0, 0.0, 0.0, 0.0]))["reading"], "SCOPED NEGATIVE")
    # 4. partial
    chk("only Base high -> unnamed partial",
        g3a(_ctl([0.20, 0.01, 0.00, 0.00]))["reading"], "UNNAMED PARTIAL")

    print("\n-- significantly NEGATIVE sensitivity must not read as includes-0 --")
    # their Base: TPR 0.1% vs FPR 16.4%, at n=48/48
    neg = explore({"hit": 0, "inj_decidable": 48, "fa": 8, "ctl_decidable": 48})
    good = neg["ci_state"] == "excludes_downward" and not neg["screen_hit"]
    ok &= good
    print(f"  [{'PASS' if good else 'FAIL'}] hit 0/48 vs fa 8/48 -> "
          f"{neg['ci_state']!r} (sens {neg['sensitivity']:+.3f}), screen_hit="
          f"{neg['screen_hit']}")
    pos = explore({"hit": 14, "inj_decidable": 48, "fa": 0, "ctl_decidable": 48})
    good = pos["ci_state"] == "excludes_upward" and pos["screen_hit"]
    ok &= good
    print(f"  [{'PASS' if good else 'FAIL'}] hit 14/48 vs fa 0/48 -> "
          f"{pos['ci_state']!r}, screen_hit={pos['screen_hit']}")
    nul = explore({"hit": 2, "inj_decidable": 48, "fa": 1, "ctl_decidable": 48})
    good = nul["ci_state"] == "includes" and not nul["screen_hit"]
    ok &= good
    print(f"  [{'PASS' if good else 'FAIL'}] hit 2/48 vs fa 1/48 -> "
          f"{nul['ci_state']!r}, screen_hit={nul['screen_hit']}")

    print("\n-- [g3-B] ladder, including the §2 no-pass hard stop --")
    lad = {"control": {"about": 1, "n": 24},
           "injected": {"1.0": {"about": 2, "n": 24, "degenerate_frac": 0.0},
                        "2.0": {"about": 5, "n": 24, "degenerate_frac": 0.0},
                        "4.0": {"about": 16, "n": 24, "degenerate_frac": 0.04},
                        "8.0": {"about": 20, "n": 24, "degenerate_frac": 0.60}}}
    r = g3b(lad)
    good = r["MED_c"] == 4.0 and not r["hard_stop"]
    ok &= good
    print(f"  [{'PASS' if good else 'FAIL'}] MED_c picks the lowest strength "
          f"passing BOTH gates -> {r['MED_c']}")
    good = r["ladder"]["8.0"]["separates"] and not r["ladder"]["8.0"]["passes"]
    ok &= good
    print(f"  [{'PASS' if good else 'FAIL'}] strength 8 is potent but "
          f"INCOHERENT (degen .60) so it does not qualify — the inverted U")
    lad2 = {"control": {"about": 1, "n": 24},
            "injected": {s: {"about": 1, "n": 24, "degenerate_frac": 0.0}
                         for s in ("1.0", "2.0", "4.0", "8.0")}}
    r2 = g3b(lad2)
    good = r2["hard_stop"] and r2["MED_c"] is None
    ok &= good
    print(f"  [{'PASS' if good else 'FAIL'}] no strength passes -> HARD STOP "
          f"for that stage's §3 cell")

    print(f"\n  {'ALL PASS' if ok else 'FAILURES PRESENT'}")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=os.path.join(REPO, "data/olmo"))
    ap.add_argument("--out", default=None)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    # Loading path, wired BEFORE any B2-r trial exists. The criteria above are
    # untouched; this only finds the artifacts and prints what they return.
    out = {"item": "B2-r analysis", "lock": "ADDENDUM-g3 v1.2"}
    ctl = {}
    for s in STAGES:
        p = os.path.join(args.dir, f"b2r_control_{s}.json")
        if os.path.exists(p):
            a = json.load(open(p))
            ctl[s] = {"affirm": a["affirm"], "decidable": a["decidable"]}
    if len(ctl) == 4:
        out["g3a"] = g3a(ctl)
        print("=== [g3-A] CONTROL — the specificity transition ===")
        for s in STAGES:
            r = out["g3a"]["rates"][s]
            print(f"  {s:<9} FPR {r['fpr']:.4f}  ({r['k']}/{r['n']})  "
                  f"CI [{r['ci'][0]:.4f}, {r['ci'][1]:.4f}]  "
                  f"floor {'OK' if r['meets_floor'] else 'BELOW'}")
        for k, v in out["g3a"]["separations"].items():
            print(f"    {k:<18} {v}")
        print(f"  READING: {out['g3a']['reading']}")
    elif ctl:
        print(f"=== [g3-A] INCOMPLETE — {len(ctl)}/4 control cells present ===")

    lad = {}
    for s in STAGES:
        p = os.path.join(args.dir, f"b2r_qualify_{s}.json")
        if os.path.exists(p):
            a = json.load(open(p))
            lad[s] = g3b({"control": {"about": a["control"]["about"],
                                      "n": a["control"]["n"]},
                          "injected": {k: {"about": v["about"], "n": v["n"],
                                           "degenerate_frac": v["degenerate_frac"]}
                                       for k, v in a["injected"].items()}})
    if lad:
        out["g3b"] = lad
        print("\n=== [g3-B] QUALIFICATION — the dose ladder ===")
        for s, r in lad.items():
            print(f"  {s:<9} MED_c = {r['MED_c']}"
                  f"{'   *** HARD STOP for this stage in §3 ***' if r['hard_stop'] else ''}")
            for st, c in r["ladder"].items():
                print(f"    s={st:<5} about {c['about_rate']:.3f}  "
                      f"separates {str(c['separates']):<5} degen "
                      f"{c['degenerate_frac']:.2f}  coherent "
                      f"{str(c['coherent']):<5} -> {'QUALIFIES' if c['passes'] else 'no'}")

    exp = {}
    for s in STAGES:
        p = os.path.join(args.dir, f"b2r_explore_{s}.json")
        if os.path.exists(p):
            exp[s] = explore(json.load(open(p)))
    if exp:
        out["explore"] = exp
        print("\n=== §3 EXPLORATION — descriptive, NO criterion attaches ===")
        for s, e in exp.items():
            print(f"  {s:<9} TPR {e['tpr']:.4f}  FPR {e['fpr']:.4f}  sens "
                  f"{e['sensitivity']:+.4f}  CI [{e['ci'][0]:+.4f}, "
                  f"{e['ci'][1]:+.4f}]  {e['ci_state']}  "
                  f"screen_hit={e['screen_hit']}  floor "
                  f"{'OK' if e['meets_floor'] else 'BELOW'}")

    if not (ctl or lad or exp):
        raise SystemExit(f"no B2-r artifacts under {args.dir}")
    if args.out:
        json.dump(out, open(args.out, "w"), indent=1)
        print(f"\n  wrote {args.out}")
    print("  DISPOSITION IS THE DESIGN INSTANCE'S.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
