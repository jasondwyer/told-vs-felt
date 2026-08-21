#!/usr/bin/env python3
"""LOCK-h §6 verification -- exact operating characteristics of the §3 gate.

LOCK-h v1 does not bind until this passes. §6 asks, per pi_d cell, for
(a) pass-when-clean at true L = 0, gated at >= 0.80 for every pi_d <= 0.30;
(b) the same at the first-reads-only floor, reported not gated; and
(c) power to FAIL at true L = bar_leak, gated at >= 0.80 for pi_d in
[bar_leak, 0.30].

**Exact, not simulated.** Every distribution here is discrete and finite, so
the whole operating characteristic is a finite sum. Rule 10 is explicit that
under-sampled nulls flatter weak signals, and a gate's own certification is
the last place to accept sampling error.

THE §3 PROCESS, as implemented:

  Each paired read is discordant w.p. pi_d; a discordant read is b-type
  (toward the +arm) w.p. p_flip. The true leak is L = pi_d (2 p_flip - 1),
  so p_flip = 1/2 + L / (2 pi_d) and |L| <= pi_d always -- §3's feasibility
  corollary, which the arithmetic inherits rather than assumes.

  Stopping: first of n_d = n_d* discordant pairs, or N = N_max reads.
  Conditional on n_d the split b is Binomial(n_d, p_flip) INDEPENDENT of the
  stopping time, because the rule reads only the totals. That is what makes
  the conditional test exact under inverse sampling, and it is also what
  makes this enumeration exact: the stopping law and the split factorise.

  Gate at stop: exact (Clopper-Pearson) 95% CI on p_flip, mapped to L
  through pi_hat = n_d/N. PASS iff the mapped CI lies strictly inside
  (-bar, +bar); FAIL iff it lies strictly outside; otherwise INDETERMINATE
  (§3: "CI straddles the bar" -> extend once).

TWO PLACES §6 IS AMBIGUOUS, BOTH RESOLVED BY COMPUTING BOTH BRANCHES:

  (b) "first-reads-only floor (m = 1, 640 sessions equivalent)". Read
      literally -- 640 sessions each contributing one paired read -- it is
      the SAME computation as (a) under ICC 0 and returns identical numbers,
      which cannot be what a "pessimistic bound" means. The bound that is
      pessimistic is the fully-clustered one: if the m = 6 reads within a
      session carried one session's worth of information, N_max = 640 reads
      would be N_max/6 = 107 independent paired reads. Both are reported;
      the clustered one is the informative row.

  (c) "power to FAIL at true L = bar_leak". §3 gives FAIL a specific meaning
      (CI strictly beyond the bar), and at a true L sitting exactly ON the
      bar that probability is structurally bounded -- see
      `structural_limit_note()`. Both the strict reading and P(not PASS) are
      reported, plus P(FAIL) at leaks above the bar, so the design instance
      can see which requirement is reachable and where.

Model-free, no adapter. Needs numpy + scipy (HANDOFF trap 9: no python on
the laptop has scipy; use a scratch venv, never the miniconda base).

Usage:
    python scripts/lockh_verify.py
    python scripts/lockh_verify.py --n-d 124 --n-max 640
"""
from __future__ import annotations

import argparse
import json
import os

import numpy as np
from scipy import stats

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PI_GRID = (0.02, 0.05, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30)


def cp_interval(b: int, n: int, conf: float = 0.95) -> tuple[float, float]:
    """Clopper-Pearson interval on p_flip, with the standard edge rules."""
    a = (1.0 - conf) / 2.0
    lo = 0.0 if b == 0 else float(stats.beta.ppf(a, b, n - b + 1))
    hi = 1.0 if b == n else float(stats.beta.ppf(1.0 - a, b + 1, n - b))
    return lo, hi


def cp_table(n_max_nd: int, conf: float = 0.95) -> dict[int, np.ndarray]:
    """Cache every interval the enumeration can need.

    The interval depends on (b, n_d) only -- never on pi_d, on N, or on the
    true leak -- so it is computed once and reused across every cell of
    every table. Without this the verification is ~4M beta.ppf calls.
    """
    out = {}
    for n in range(0, n_max_nd + 1):
        arr = np.empty((n + 1, 2))
        for b in range(n + 1):
            arr[b] = cp_interval(b, n, conf)
        out[n] = arr
    return out


def decide(cp: np.ndarray, pi_hat: float, bar: float) -> np.ndarray:
    """PASS=1 / IND=0 / FAIL=-1 for every b at one stopping state.

    The mapped interval is [(2 p_lo - 1) pi_hat, (2 p_hi - 1) pi_hat]. Note
    what falls out for free: the mapped interval is always inside
    [-pi_hat, +pi_hat], so ANY stop with pi_hat < bar passes automatically.
    That is not a loophole, it is §3's feasibility corollary -- a leak
    cannot exceed the discordance that carries it, so certified-low
    discordance certifies a low leak.
    """
    lo = (2.0 * cp[:, 0] - 1.0) * pi_hat
    hi = (2.0 * cp[:, 1] - 1.0) * pi_hat
    out = np.zeros(len(cp), dtype=int)
    out[(lo > -bar) & (hi < bar)] = 1
    out[(lo > bar) | (hi < -bar)] = -1
    return out


def stopping_law(pi: float, n_d_star: int, n_max: int) -> list[tuple[int, int, float]]:
    """(n_d, N, probability) over every reachable stopping state.

    Early exit: N is the trial index of the n_d*-th discordant read, a
    negative binomial. Late exit: N = n_max with n_d < n_d* discordant,
    a binomial. The two branches are exhaustive and their masses sum to 1,
    which the caller asserts rather than trusts.
    """
    states = []
    ns = np.arange(n_d_star, n_max + 1)
    early = stats.nbinom.pmf(ns - n_d_star, n_d_star, pi)
    for n, p in zip(ns, early):
        if p > 0:
            states.append((n_d_star, int(n), float(p)))
    ks = np.arange(0, n_d_star)
    late = stats.binom.pmf(ks, n_max, pi)
    for k, p in zip(ks, late):
        if p > 0:
            states.append((int(k), n_max, float(p)))
    return states


def outcome_probs(pi: float, leak: float, n_d_star: int, n_max: int,
                  bar: float, cps: dict) -> dict:
    """Exact P(PASS/IND/FAIL) for one (pi_d, true leak) cell."""
    if abs(leak) > pi:                       # infeasible: |L| <= pi_d always
        return {"feasible": False, "pass": None, "ind": None, "fail": None}
    p_flip = 0.5 + leak / (2.0 * pi)
    tot = {1: 0.0, 0: 0.0, -1: 0.0}
    mass = 0.0
    for n_d, N, p_state in stopping_law(pi, n_d_star, n_max):
        mass += p_state
        dec = decide(cps[n_d], n_d / N, bar)
        pmf = stats.binom.pmf(np.arange(n_d + 1), n_d, p_flip)
        for code in (1, 0, -1):
            tot[code] += p_state * float(pmf[dec == code].sum())
    assert abs(mass - 1.0) < 1e-9, f"stopping law mass {mass}"
    return {"feasible": True, "pass": tot[1], "ind": tot[0], "fail": tot[-1]}


def structural_limit_note(bar: float, pi: float, cps: dict) -> dict:
    """Why 'power to FAIL at true L = bar' cannot reach 0.80 at ANY n.

    FAIL needs the whole CI strictly beyond the bar. A true leak sitting
    exactly ON the bar is the BOUNDARY of the hypothesis the gate tests, and
    at its own boundary a correctly-sized interval test has power equal to
    its SIZE, not to anything approaching 0.80: the CI half-width and the
    sampling SD both shrink like 1/sqrt(n_d), so their ratio is frozen at
    the critical value and P(FAIL) sits at the one-sided error rate
    alpha/2 = 0.025 for every n.

    So this is not a shortfall a larger n_d*/N_max can close, and it does
    not drift toward 1/2 either -- it is pinned. §6(c) as written asks for
    80% power at the one point where the test is defined to have 2.5%. The
    fix is to state the power requirement at a leak strictly ABOVE the bar
    (the caller reports that ladder), or to gate P(not PASS) instead.

    Demonstrated rather than argued: the same cell is evaluated at a ladder
    of n_d with N chosen so pi_hat is held at pi, and the value is flat.
    """
    ladder = []
    for n_d in (124, 250, 500, 1000, 2000):
        N = int(round(n_d / pi))
        cp = cps[n_d] if n_d in cps else np.array(
            [cp_interval(b, n_d) for b in range(n_d + 1)])
        dec = decide(cp, n_d / N, bar)
        p_flip = 0.5 + bar / (2.0 * pi)
        pmf = stats.binom.pmf(np.arange(n_d + 1), n_d, p_flip)
        ladder.append({"n_d": n_d, "N_for_pi_hat": N,
                       "P_fail": float(pmf[dec == -1].sum()),
                       "P_pass": float(pmf[dec == 1].sum())})
    return {"pi_d": pi, "ladder": ladder,
            "limit": "alpha/2 = 0.025, flat in n_d",
            "note": ("A true leak exactly ON the bar is the boundary of the "
                     "tested hypothesis, where an interval test's power "
                     "equals its size: CI half-width and sampling SD both "
                     "shrink like 1/sqrt(n_d), so P(FAIL) is pinned at "
                     "alpha/2 = 0.025 for every n_d. The >= 0.80 requirement "
                     "in §6(c) is therefore not short by a sample size and "
                     "no n_d*/N_max can satisfy it; it asks for 80% power at "
                     "the one point where the test is defined to have 2.5%.")}


def n_d_ladder(pi: float, bar: float, n_max_locked: int,
               target: float = 0.80,
               n_ds=(124, 160, 200, 250, 300, 400)) -> list[dict]:
    """Pass-when-clean over a ladder of (n_d*, N_max), not a single answer.

    §6 hands the design instance the n_d*/N_max dial, so the useful output is
    the trade surface rather than one point -- and the surface has a feature
    worth seeing: **raising n_d* alone does nothing once N_max binds.** At
    pi_d = 0.25 a run needs ~n_d*/pi_d reads to reach n_d* discordant, so an
    n_d* of 300 against N_max = 640 simply converts early exits into late
    ones at n_d ~ 160. Each rung is therefore evaluated twice: against the
    locked N_max, and against an N_max sized to actually reach that n_d*.
    """
    cps = cp_table(max(n_ds))
    rows = []
    for n_d_star in n_ds:
        sized = int(np.ceil(n_d_star / pi * 1.15))
        for n_max, tag in ((n_max_locked, "locked"), (sized, "sized")):
            if n_max < n_d_star:
                rows.append({"n_d_star": n_d_star, "n_max": n_max,
                             "basis": tag, "pass_when_clean": None,
                             "note": "N_max < n_d*: unreachable"})
                continue
            r = outcome_probs(pi, 0.0, n_d_star, n_max, bar, cps)
            rows.append({"n_d_star": n_d_star, "n_max": n_max, "basis": tag,
                         "pass_when_clean": r["pass"],
                         "sessions_at_m6": int(np.ceil(n_max / 6)),
                         "meets": bool(r["pass"] >= target)})
    return rows


def icc_tolerance(pi: float, bar: float, n_d_star: int, n_max: int,
                  m: int, target: float = 0.80,
                  grid=(0.0, 0.02, 0.05, 0.10, 0.15, 0.20, 0.30, 0.50,
                        0.75, 1.0)) -> dict:
    """Largest within-session ICC the plan still certifies under.

    §6 asks for the clustered floor as a bound; this turns the bound into a
    tolerance, which is the actionable form. The m = 6 pooling ruling in §3
    is what buys N = 640 from ~107 sessions, and it rests on the reads being
    exchangeable as LEAK measurements. DEFF = 1 + (m-1) ICC, so an ICC of
    just 0.2 costs half the effective reads. The number below is how much
    the plan can absorb before pass-when-clean falls through the floor.
    """
    cps = cp_table(n_d_star)
    best, rows = None, []
    for icc in grid:
        deff = 1.0 + (m - 1) * icc
        n_eff = int(np.floor(n_max / deff))
        if n_eff < 2:
            continue
        r = outcome_probs(pi, 0.0, min(n_d_star, n_eff), n_eff, bar, cps)
        ok = r["pass"] >= target
        rows.append({"icc": icc, "deff": round(deff, 2),
                     "n_eff_reads": n_eff, "pass_when_clean": r["pass"],
                     "meets": bool(ok)})
        if ok:
            best = icc
    return {"pi_d": pi, "max_icc_tolerated": best, "rows": rows}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bar", type=float, default=0.0735)
    ap.add_argument("--n-d", type=int, default=124, dest="n_d_star")
    ap.add_argument("--n-max", type=int, default=640)
    ap.add_argument("--m", type=int, default=6)
    ap.add_argument("--target", type=float, default=0.80)
    ap.add_argument("--out", default=os.path.join(REPO, "data/e2b/lockh_verify.json"))
    args = ap.parse_args()

    bar, n_d_star, n_max = args.bar, args.n_d_star, args.n_max
    n_clustered = n_max // args.m

    print("=== LOCK-h §6 verification (exact) ===")
    print(f"  §3 plan: stop at n_d = {n_d_star} discordant OR N = {n_max} "
          f"paired reads, whichever first")
    print(f"  bar_leak = {bar}; gate = exact 95% CI on p_flip mapped "
          f"through pi_hat = n_d/N")
    print(f"  pooled basis m = {args.m}, ICC 0 -> {n_max} independent "
          f"paired reads (~{int(np.ceil(n_max / args.m))} sessions)")
    print(f"  clustered floor -> {n_clustered} independent paired reads\n")

    cps = cp_table(n_d_star)

    rows = []
    print(f"  {'pi_d':>5} | {'(a) PASS@L=0':>12} {'IND':>7} {'FAIL':>7} | "
          f"{'(b) clustered':>13} | {'(c) FAIL@bar':>12} {'notPASS@bar':>11}")
    print("  " + "-" * 84)
    for pi in PI_GRID:
        a = outcome_probs(pi, 0.0, n_d_star, n_max, bar, cps)
        b = outcome_probs(pi, 0.0, min(n_d_star, n_clustered), n_clustered,
                          bar, cps)
        c = outcome_probs(pi, bar, n_d_star, n_max, bar, cps)
        row = {"pi_d": pi,
               "a_pass_when_clean": a["pass"], "a_ind": a["ind"],
               "a_fail": a["fail"],
               "a_meets": bool(a["pass"] >= args.target),
               "b_clustered_pass_when_clean": b["pass"],
               "b_basis": (f"{n_clustered} paired reads "
                           f"(n_d* capped at {min(n_d_star, n_clustered)})"),
               "c_feasible": c["feasible"],
               "c_fail_at_bar": c["fail"],
               "c_not_pass_at_bar": (None if not c["feasible"]
                                     else 1.0 - c["pass"]),
               "c_meets_strict": (bool(c["fail"] >= args.target)
                                  if c["feasible"] else None)}
        rows.append(row)
        cstr = ("  n/a (pi_d < bar)" if not c["feasible"]
                else f"{c['fail']:>12.3f} {1 - c['pass']:>11.3f}")
        print(f"  {pi:>5.2f} | {a['pass']:>12.3f} {a['ind']:>7.3f} "
              f"{a['fail']:>7.3f} | {b['pass']:>13.3f} |{cstr}")

    gated_a = [r for r in rows if r["pi_d"] <= 0.30]
    short_a = [r for r in gated_a if not r["a_meets"]]
    gated_c = [r for r in rows if r["c_feasible"] and r["pi_d"] <= 0.30]
    short_c = [r for r in gated_c if not r["c_meets_strict"]]

    print(f"\n  (a) gated >= {args.target} for pi_d <= 0.30: "
          f"{len(gated_a) - len(short_a)}/{len(gated_a)} cells clear"
          + (f" -- SHORT at pi_d = "
             f"{', '.join(str(r['pi_d']) for r in short_a)}" if short_a else ""))
    print(f"  (b) reported, not gated -- the clustered floor is the "
          f"pessimistic bound; the literal 'm=1, 640 sessions' reading is "
          f"identical to (a) by construction")
    print(f"  (c) gated >= {args.target} for pi_d in [bar, 0.30]: "
          f"{len(gated_c) - len(short_c)}/{len(gated_c)} cells clear"
          + (f" -- SHORT at pi_d = "
             f"{', '.join(str(r['pi_d']) for r in short_c)}" if short_c else ""))

    extras = {}
    if short_c:
        note = structural_limit_note(bar, 0.25, cps)
        extras["c_structural_limit"] = note
        print(f"\n  (c) IS NOT SHORT BY A SAMPLE SIZE -- it is a category "
              f"error in the requirement.")
        print(f"    A leak exactly ON the bar is the boundary of the tested "
              f"hypothesis, where an interval")
        print(f"    test's power equals its SIZE. P(FAIL) is pinned at "
              f"alpha/2 = 0.025 for every n_d:")
        print(f"    demonstrated at pi_d = 0.25, holding pi_hat fixed:")
        for L in note["ladder"]:
            print(f"      n_d = {L['n_d']:>5} (N = {L['N_for_pi_hat']:>5})  "
                  f"P(FAIL) = {L['P_fail']:.3f}   P(PASS) = {L['P_pass']:.3f}")
        print(f"    Reachable restatements, with numbers, for the design "
              f"instance to choose between:")
        ladder = []
        for mult in (1.0, 1.25, 1.5, 2.0):
            L = bar * mult
            r = [{"pi_d": pi,
                  "p_fail": outcome_probs(pi, L, n_d_star, n_max, bar,
                                          cps)["fail"]}
                 for pi in PI_GRID if pi >= L]
            ladder.append({"leak_multiple_of_bar": mult, "leak": L,
                           "cells": r,
                           "min_p_fail": (min(x["p_fail"] for x in r)
                                          if r else None)})
            if r:
                print(f"      P(FAIL) at L = {mult:.2f} x bar = {L:.4f}: "
                      f"min over feasible pi_d = "
                      f"{min(x['p_fail'] for x in r):.3f}")
        extras["c_fail_ladder"] = ladder
        print(f"      P(not PASS) at L = bar: min over feasible pi_d = "
              f"{min(r['c_not_pass_at_bar'] for r in gated_c):.3f}")

    if short_a:
        extras["a_n_d_ladder"] = {}
        print(f"\n  (a) IS short by a sample size. The trade surface, "
              f"pass-when-clean at true L = 0:")
        for r in short_a:
            lad = n_d_ladder(r["pi_d"], bar, n_max, args.target)
            extras["a_n_d_ladder"][str(r["pi_d"])] = lad
            print(f"    pi_d = {r['pi_d']} (currently "
                  f"{r['a_pass_when_clean']:.3f} at n_d* = {n_d_star}, "
                  f"N_max = {n_max}):")
            print(f"      {'n_d*':>6} {'N_max':>7} {'basis':>7} "
                  f"{'sessions':>9} {'pass@L=0':>9}")
            for x in lad:
                if x["pass_when_clean"] is None:
                    continue
                flag = " <-- meets" if x["meets"] else ""
                print(f"      {x['n_d_star']:>6} {x['n_max']:>7} "
                      f"{x['basis']:>7} {x['sessions_at_m6']:>9} "
                      f"{x['pass_when_clean']:>9.3f}{flag}")

    extras["b_icc_tolerance"] = {}
    print(f"\n  (b) supplementary -- the ICC the plan can absorb "
          f"(DEFF = 1 + (m-1)*ICC on N_max = {n_max}):")
    print(f"    {'pi_d':>5} {'max ICC certifying':>19}")
    for pi in (0.08, 0.10, 0.15, 0.20, 0.25, 0.30):
        t = icc_tolerance(pi, bar, n_d_star, n_max, args.m, args.target)
        extras["b_icc_tolerance"][str(pi)] = t
        mi = t["max_icc_tolerated"]
        print(f"    {pi:>5.2f} {(f'{mi:.2f}' if mi is not None else 'none'):>19}")

    green = (not short_a) and (not short_c)
    print(f"\n  VERDICT: {'GREEN' if green else 'NOT GREEN'} -- "
          + ("all gated cells clear; LOCK-h v1 verified"
             if green else
             "reported to the design instance for adjustment per §6"))

    out = {"item": "LOCK-h §6 verification", "exact": True,
           "bar_leak": bar, "n_d_star": n_d_star, "n_max": n_max,
           "m": args.m, "clustered_floor_reads": n_clustered,
           "target": args.target, "pi_grid": list(PI_GRID),
           "rows": rows,
           "a_short_cells": [r["pi_d"] for r in short_a],
           "c_short_cells": [r["pi_d"] for r in short_c],
           "green": bool(green),
           **extras,
           "ambiguities_resolved": {
               "b_first_reads_floor": (
                   "Read literally (m=1, 640 sessions) §6(b) is identical to "
                   "(a) under ICC 0 and is not a bound of any kind. The "
                   "pessimistic bound reported here is the fully-clustered "
                   "one: N_max/m = %d independent paired reads." % n_clustered),
               "c_fail_definition": (
                   "FAIL is §3's: mapped CI strictly beyond the bar. Both "
                   "that and P(not PASS) are reported, because at a true "
                   "leak exactly on the bar the strict reading is bounded "
                   "by 1/2.")},
           "decides_nothing": ("Code verifies; §6 adjustments and the commit "
                              "are the design instance's and Jason's.")}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
