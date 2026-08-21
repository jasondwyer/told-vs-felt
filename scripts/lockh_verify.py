#!/usr/bin/env python3
"""LOCK-h §6 verification -- exact operating characteristics of the §3 gate.

LOCK-h does not bind until this passes. §6 of v1.1 asks, per pi_d cell:
(a) pass-when-clean at true L = 0 -- GATED >= 0.80 for every pi_d <= 0.30;
(b) the fully-clustered floor plus the max-ICC ceiling table -- REPORTED, and
    the table BINDS into the lock as its stated exposure, so it is ASSERTED
    here against the values §6(b) carries;
(c) detection: P(FAIL) at true L = 2 x bar_leak -- GATED >= 0.80 across
    feasible pi_d <= 0.30, with P(not-PASS) at L = bar reported beside it.

v1.0 -> v1.1 changed n_d* 124 -> 200 and restated (c). Both v1.0 numbers
remain reproducible from this script:
    --n-d 124 --c-leak-multiple 1.0

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

  Both were resolved for v1.0 by computing every branch rather than picking
  one, and v1.1 adopted the resolutions: the non-bound "first-reads floor"
  is retired in favour of the fully-clustered bound, and the detection gate
  moved off the boundary of the tested hypothesis to 2 x bar.

Model-free, no adapter. Needs numpy + scipy (HANDOFF trap 9: no python on
the laptop has scipy; use a scratch venv, never the miniconda base).

Usage:
    python scripts/lockh_verify.py                      # v1.1 §6
    python scripts/lockh_verify.py --n-d 124 --c-leak-multiple 1.0   # v1.0
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
        if not ok:                 # first failing rung ends the tolerance;
            break                      # never report past a gap
        best = icc
    return {"pi_d": pi, "max_icc_tolerated": best, "rows": rows}


BOUND_IN_ICC = "0.08:0.75,0.10:0.50,0.15:0.20,0.20:0.10,0.25:0.05,0.30:0.00"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bar", type=float, default=0.0735)
    ap.add_argument("--n-d", type=int, default=200, dest="n_d_star")
    ap.add_argument("--n-max", type=int, default=640)
    ap.add_argument("--m", type=int, default=6)
    ap.add_argument("--target", type=float, default=0.80)
    ap.add_argument("--c-leak-multiple", type=float, default=2.0,
                    help="multiple of bar_leak at which the detection gate "
                         "(c) is evaluated. v1.1 = 2.0; v1.0's 1.0 sat on "
                         "the boundary of the tested hypothesis, where "
                         "power equals size")
    ap.add_argument("--expect-icc", default=BOUND_IN_ICC,
                    help="max-ICC ceiling table bound into LOCK-h §6(b); "
                         "asserted, since the lock carries it as its stated "
                         "exposure. Empty string skips the assertion.")
    ap.add_argument("--out", default=os.path.join(REPO, "data/e2b/lockh_verify_v11.json"))
    args = ap.parse_args()

    bar, n_d_star, n_max = args.bar, args.n_d_star, args.n_max
    n_clustered = n_max // args.m
    c_leak = bar * args.c_leak_multiple

    print("=== LOCK-h §6 verification (exact) ===")
    print(f"  §3 plan: stop at n_d = {n_d_star} discordant OR N = {n_max} "
          f"paired reads, whichever first")
    print(f"  bar_leak = {bar}; gate = exact 95% CI on p_flip mapped "
          f"through pi_hat = n_d/N")
    print(f"  pooled basis m = {args.m}, ICC 0 -> {n_max} independent "
          f"paired reads (~{int(np.ceil(n_max / args.m))} sessions)")
    print(f"  (a) gated >= {args.target} at L = 0, pi_d <= 0.30")
    print(f"  (c) gated >= {args.target} at L = {args.c_leak_multiple:g} x "
          f"bar = {c_leak:.4f}, feasible pi_d <= 0.30")
    print(f"  (b) clustered floor -> {n_clustered} paired reads; ICC ceiling "
          f"table ASSERTED against the lock\n")

    cps = cp_table(n_d_star)

    rows = []
    print(f"  {'pi_d':>5} | {'(a) PASS@L=0':>12} {'IND':>7} | "
          f"{'(b) clust':>9} | {'(c) FAIL@2bar':>13} | "
          f"{'FAIL@bar':>9} {'notPASS@bar':>11}")
    print("  " + "-" * 82)
    for pi in PI_GRID:
        a = outcome_probs(pi, 0.0, n_d_star, n_max, bar, cps)
        b = outcome_probs(pi, 0.0, min(n_d_star, n_clustered), n_clustered,
                          bar, cps)
        c = outcome_probs(pi, c_leak, n_d_star, n_max, bar, cps)
        ctx = outcome_probs(pi, bar, n_d_star, n_max, bar, cps)
        row = {"pi_d": pi,
               "a_pass_when_clean": a["pass"], "a_ind": a["ind"],
               "a_meets": bool(a["pass"] >= args.target),
               "b_clustered_pass_when_clean": b["pass"],
               "c_leak": c_leak, "c_feasible": c["feasible"],
               "c_fail_at_c_leak": c["fail"],
               "c_meets": (bool(c["fail"] >= args.target)
                           if c["feasible"] else None),
               "ctx_fail_at_bar": ctx["fail"] if ctx["feasible"] else None,
               "ctx_not_pass_at_bar": (None if not ctx["feasible"]
                                       else 1.0 - ctx["pass"])}
        rows.append(row)
        cs = (f"{c['fail']:>13.3f}" if c["feasible"]
              else f"{'n/a':>13}")
        xs = (f"{ctx['fail']:>9.3f} {1 - ctx['pass']:>11.3f}"
              if ctx["feasible"] else f"{'n/a':>9} {'n/a':>11}")
        print(f"  {pi:>5.2f} | {a['pass']:>12.3f} {a['ind']:>7.3f} | "
              f"{b['pass']:>9.3f} | {cs} | {xs}")

    gated_a = [r for r in rows if r["pi_d"] <= 0.30]
    short_a = [r for r in gated_a if not r["a_meets"]]
    gated_c = [r for r in rows if r["c_feasible"] and r["pi_d"] <= 0.30]
    short_c = [r for r in gated_c if not r["c_meets"]]
    min_c = min((r["c_fail_at_c_leak"] for r in gated_c), default=None)

    print(f"\n  (a) {len(gated_a) - len(short_a)}/{len(gated_a)} cells clear"
          + (f" -- SHORT at pi_d = "
             f"{', '.join(str(r['pi_d']) for r in short_a)}"
             if short_a else "  [GATE MET]"))
    print(f"  (c) {len(gated_c) - len(short_c)}/{len(gated_c)} feasible "
          f"cells clear at L = {c_leak:.4f}"
          + (f" -- SHORT at pi_d = "
             f"{', '.join(str(r['pi_d']) for r in short_c)}"
             if short_c else f"  [GATE MET, min = {min_c:.3f}]"))
    print(f"      feasibility: L = {c_leak:.4f} requires pi_d >= {c_leak:.4f}, "
          f"so pi_d = "
          f"{', '.join(str(r['pi_d']) for r in rows if not r['c_feasible'])} "
          f"carry no such leak and are excluded, not failed")
    notpass = [r["ctx_not_pass_at_bar"] for r in rows
               if r["ctx_not_pass_at_bar"] is not None]
    print(f"      reported beside it, not gated: P(not-PASS) at L = bar, "
          f"min = {min(notpass):.3f} (pi_d = "
          f"{[r['pi_d'] for r in rows if r['ctx_not_pass_at_bar'] == min(notpass)][0]})")

    # (b) the ICC ceiling table, asserted against what the lock carries
    icc = {}
    print(f"\n  (b) max-ICC ceiling (DEFF = 1 + (m-1)*ICC on N_max = "
          f"{n_max}), ASSERTED against LOCK-h §6(b):")
    print(f"    {'pi_d':>5} {'computed':>9} {'bound-in':>9}  match")
    expect = {}
    if args.expect_icc:
        for part in args.expect_icc.split(","):
            k, v = part.split(":")
            expect[float(k)] = float(v)
    icc_ok = True
    for pi in sorted(expect) or (0.08, 0.10, 0.15, 0.20, 0.25, 0.30):
        t = icc_tolerance(pi, bar, n_d_star, n_max, args.m, args.target)
        icc[str(pi)] = t
        got = t["max_icc_tolerated"]
        exp = expect.get(pi)
        ok = (exp is not None and got is not None
              and abs(got - exp) < 1e-9)
        icc_ok = icc_ok and ok
        print(f"    {pi:>5.2f} {(f'{got:.2f}' if got is not None else 'none'):>9} "
              f"{(f'{exp:.2f}' if exp is not None else '-'):>9}  "
              f"{'OK' if ok else 'MISMATCH'}")
    if expect:
        verdict = ("MATCHES the lock" if icc_ok else
                   "MISMATCH -- the lock carries values this plan does "
                   "not produce")
        print(f"    ICC table assertion: {verdict}")
    else:
        icc_ok = True
        print("    (assertion skipped: --expect-icc empty)")

    green = (not short_a) and (not short_c) and icc_ok
    print(f"\n  VERDICT: {'GREEN' if green else 'NOT GREEN'} -- "
          + ("all gated cells clear and the bound-in ICC table reproduces; "
             "LOCK-h verified"
             if green else
             "reported to the design instance for adjustment per §6"))

    out = {"item": "LOCK-h §6 verification", "lock_version": "v1.1",
           "exact": True, "bar_leak": bar, "n_d_star": n_d_star,
           "n_max": n_max, "m": args.m,
           "clustered_floor_reads": n_clustered,
           "target": args.target,
           "c_leak_multiple": args.c_leak_multiple, "c_leak": c_leak,
           "pi_grid": list(PI_GRID), "rows": rows,
           "a_short_cells": [r["pi_d"] for r in short_a],
           "c_short_cells": [r["pi_d"] for r in short_c],
           "c_min_over_feasible": min_c,
           "b_icc_tolerance": icc,
           "b_icc_bound_in": expect,
           "b_icc_assertion_matches": bool(icc_ok),
           "green": bool(green),
           "reproduces_v1_0_with": "--n-d 124 --c-leak-multiple 1.0",
           "decides_nothing": ("Code verifies; the commit is the design "
                               "instance's and Jason's.")}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
