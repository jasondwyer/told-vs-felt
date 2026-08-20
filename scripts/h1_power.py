#!/usr/bin/env python3
"""LOCK-h power arithmetic: MDE_verdict, bar_leak, and H1's achieved power.

PROPOSAL-h §2 H1 defines the leakage gate by formula:

    bar_leak = 0.5 x MDE_verdict          (MDE at the verdict tier's
                                           committed n and alpha)
    H1 must have power >= 0.8 to detect a true leak of bar_leak,
    and "if 64 is insufficient under the computed numbers, H1 extends
    before opening, never after."

This computes those numbers so the design instance can instantiate them in
LOCK-h. It decides nothing: every convention the arithmetic needs but the
pre-registration does not state is surfaced as a named assumption with both
branches computed, because picking one silently is how a bar ends up
meaning something nobody registered.

Model-free, no adapter, seconds. Re-run it after any change to n or alpha.

Usage:
    python scripts/h1_power.py
    python scripts/h1_power.py --n-verdict 96 --n-h1 64 --power 0.80
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np
from scipy import stats

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def critical_k(n: int, alpha: float, p0: float = 0.5) -> int:
    """Smallest k with P(X >= k | p0) <= alpha. Exact, not normal-approx:
    the pre-registration says exact binomial, and at these n the approximation
    moves the critical value by a whole count."""
    for k in range(n + 1):
        if stats.binom.sf(k - 1, n, p0) <= alpha:
            return k
    return n + 1


def power_at(n: int, k_crit: int, p1: float) -> float:
    return float(stats.binom.sf(k_crit - 1, n, p1))


def mde_one_sided(n: int, alpha: float, power: float,
                  p0: float = 0.5) -> tuple[float, int]:
    """Smallest true share p1 reaching `power` against the exact one-sided
    test. Returns (p1, k_crit)."""
    k = critical_k(n, alpha, p0)
    for p1 in np.arange(p0, 1.0, 0.0005):
        if power_at(n, k, float(p1)) >= power:
            return float(p1), k
    return 1.0, k


def power_two_sided(n: int, alpha: float, delta: float,
                    p0: float = 0.5) -> float:
    """Power of the exact two-sided binomial to reject p0 when the true
    share is p0 + delta. Two-sided because H1's gate is on |Delta_first| --
    a leak in either direction fails it."""
    k_hi = critical_k(n, alpha / 2.0, p0)
    k_lo = n - k_hi
    p1 = p0 + delta
    return float(stats.binom.sf(k_hi - 1, n, p1) + stats.binom.cdf(k_lo, n, p1))


def envelope_distribution(n_sham: int, n_rand: int, trials: int = 200_000,
                          seed: int = 26) -> dict:
    """The control envelope the verdict must ALSO clear: max pseudo-Delta
    across the sham and random families under the null.

    Simulated rather than derived because it is the maximum of two discrete
    statistics at different n, and the quantity that matters is its upper
    tail, not its mean. This conjunct is the reason the binomial MDE below
    is a LOWER BOUND on the verdict tier's true MDE.
    """
    rng = np.random.default_rng(seed)
    s = np.abs(rng.binomial(n_sham, 0.5, trials) / n_sham - 0.5)
    r = np.abs(rng.binomial(n_rand, 0.5, trials) / n_rand - 0.5)
    env = np.maximum(s, r)
    return {"mean": float(env.mean()), "median": float(np.median(env)),
            "p90": float(np.quantile(env, 0.90)),
            "p95": float(np.quantile(env, 0.95)),
            "max_seen": float(env.max()), "trials": trials,
            "n_sham": n_sham, "n_rand": n_rand}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-verdict", type=int, default=96)
    ap.add_argument("--n-h1", type=int, default=64)
    ap.add_argument("--n-sham", type=int, default=36)
    ap.add_argument("--n-rand", type=int, default=36)
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--power", type=float, default=0.80)
    ap.add_argument("--out", default=os.path.join(REPO, "data/e2b/h1_power.json"))
    args = ap.parse_args()

    print("=== LOCK-h power arithmetic (PROPOSAL-h §2 H1) ===")
    print(f"  verdict n = {args.n_verdict}, alpha = {args.alpha} one-sided, "
          f"MDE at power {args.power}")

    p1, k = mde_one_sided(args.n_verdict, args.alpha, args.power)
    mde_share = p1 - 0.5
    print(f"\n  critical value: k >= {k}/{args.n_verdict} "
          f"(exact one-sided p <= {args.alpha})")
    print(f"  MDE_verdict = {mde_share:.4f} in SHARE units "
          f"(true share {p1:.4f})")
    print(f"              = {2 * mde_share:.4f} if Delta is written as a "
          f"+arm-minus-(-arm) difference")
    bar_leak = 0.5 * mde_share
    print(f"  bar_leak = 0.5 x MDE_verdict = {bar_leak:.4f} (share units)")

    print(f"\n  H1 at n = {args.n_h1}: power to detect a true leak of "
          f"bar_leak")
    pw = power_two_sided(args.n_h1, args.alpha, bar_leak)
    print(f"    two-sided exact, alpha {args.alpha}: power = {pw:.3f}  "
          f"-> {'MEETS' if pw >= 0.8 else 'FAILS'} the >= 0.8 requirement")
    need = None
    if pw < 0.8:
        for n in range(args.n_h1, 4001, 2):
            if power_two_sided(n, args.alpha, bar_leak) >= 0.8:
                need = n
                break
        print(f"    n required for power >= 0.8: {need}"
              + (f"  ({need / args.n_h1:.1f}x the drafted 64)" if need else ""))
        print(f"    PROPOSAL-h §2: 'if 64 is insufficient under the computed "
              f"numbers, H1 extends before opening, never after.'")

    env = envelope_distribution(args.n_sham, args.n_rand)
    print(f"\n  control envelope (max |pseudo-Delta| over sham n={args.n_sham} "
          f"and random n={args.n_rand}, {env['trials']:,} sims):")
    print(f"    mean {env['mean']:.4f} | median {env['median']:.4f} | "
          f"p90 {env['p90']:.4f} | p95 {env['p95']:.4f}")
    binds = env["p90"] > mde_share
    print(f"    binomial MDE {mde_share:.4f} vs envelope p90 {env['p90']:.4f} "
          f"-> the {'ENVELOPE' if binds else 'binomial'} conjunct usually "
          f"dominates")
    print(f"    so MDE_verdict from the binomial alone is a LOWER BOUND on "
          f"the conjunctive criterion's true MDE")

    # --- sensitivity: which undeclared convention moves H1's n, and how far
    print(f"\n  sensitivity -- required H1 n for power >= 0.8, by how "
          f"MDE_verdict is defined:")
    rows = []
    variants = [("binomial only, power 0.80", mde_share),
                ("binomial only, power 0.90",
                 mde_one_sided(args.n_verdict, args.alpha, 0.90)[0] - 0.5),
                ("conjunctive proxy: envelope p90", env["p90"]),
                ("conjunctive proxy: envelope p95", env["p95"])]
    for label, mde in variants:
        bl = 0.5 * mde
        n_req = None
        for n in range(4, 4001, 2):
            if power_two_sided(n, args.alpha, bl) >= 0.8:
                n_req = n
                break
        rows.append({"definition": label, "mde_verdict": float(mde),
                     "bar_leak": float(bl), "h1_n_required": n_req,
                     "multiple_of_drafted": (round(n_req / args.n_h1, 1)
                                             if n_req else None)})
        print(f"    {label:<34} MDE {mde:.4f}  bar_leak {bl:.4f}  "
              f"n >= {n_req}  ({n_req / args.n_h1:.1f}x drafted)")
    print(f"    every reading needs more than the drafted "
          f"{args.n_h1}; the cheapest is {min(r['h1_n_required'] for r in rows)}")

    out = {
        "item": "LOCK-h power arithmetic",
        "sensitivity": rows,
        "inputs": {"n_verdict": args.n_verdict, "n_h1": args.n_h1,
                   "n_sham": args.n_sham, "n_rand": args.n_rand,
                   "alpha": args.alpha, "mde_power": args.power},
        "critical_k": k,
        "mde_verdict_share": mde_share,
        "mde_verdict_difference_convention": 2 * mde_share,
        "bar_leak_share": bar_leak,
        "h1_power_at_drafted_n": pw,
        "h1_meets_requirement": bool(pw >= 0.8),
        "h1_n_required_for_power_0.8": need,
        "control_envelope": env,
        "envelope_dominates_binomial": bool(binds),
        "assumptions": [
            "Delta_first is the pooled share over all marker-family sessions, "
            "so the exact binomial runs at the full n. If the counterbalanced "
            "Delta is instead computed within each map (n/2 each) and then "
            "combined, effective n falls and every number here moves.",
            "MDE is quoted at power " + str(args.power) + "; PROPOSAL-h "
            "declares a power floor for H1 but not for MDE_verdict itself. "
            "That convention belongs in LOCK-h.",
            "H1's power is computed two-sided because its gate is on "
            "|Delta_first|; a one-sided reading would inflate the power.",
            "The binomial MDE ignores the control-envelope and sign-lock "
            "conjuncts, both of which can only make the verdict harder.",
        ],
        "decides_nothing": ("Code delivers arithmetic; LOCK-h.md is authored "
                            "by the design instance."),
    }
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {args.out}")
    print("  ARITHMETIC ONLY -- LOCK-h.md is design-instance authored.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
