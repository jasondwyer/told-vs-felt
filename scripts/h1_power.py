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

The LOCK-h v1 section at the bottom runs the SETTLED conventions the
design instance issued 2026-08-21 -- pooled Delta with the sign-lock as
a conjunct, the conjunctive MDE with the envelope held at p90, a
bar_leak that also respects a false-verdict-rate ceiling, an
estimation-gate variant, and a cluster correction for pooled
within-session reads. The legacy section above it is unchanged so the
committed 2026-08-20 numbers stay reproducible from this same script.

Model-free, no adapter, seconds. Needs numpy + scipy but NOT MLX or
the Qwen clone, so it runs under any python that has them -- including
the box and any cloud session. Re-run it after any change to n or alpha.

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


# ---------------------------------------------------------------------------
# LOCK-h v1 conventions (design instance, 2026-08-21)
#
# The four assumptions the 2026-08-20 run surfaced are now settled by the
# design instance, and two framings are added that the earlier arithmetic did
# not compute at all. Everything below is the settled set; the legacy section
# above is retained unchanged so the committed 2026-08-20 numbers stay
# reproducible from the same script.
#
#   (a) Delta_first is POOLED over all marker sessions -> exact binomial at
#       the full n, and the SIGN-LOCK is a conjunct, not a footnote.
#   (b) MDE is quoted at 80% power.
#   (c) H1's gate is on |Delta_first| -> two-sided.
#   (d) MDE_verdict is the CONJUNCTIVE MDE with the envelope conjunct held at
#       its p90, and bar_leak = min(0.5 x MDE_conj, the leak that costs a
#       <= 2.5% false-verdict rate).
#   (e) An estimation-gate variant: H1 passes when the CI upper bound on
#       |Delta| clears the bar, rather than when a test fails to reject.
#   (f) A pooled-within-session-reads variant with a cluster correction.
# ---------------------------------------------------------------------------


def exact_envelope(n_sham: int, n_rand: int) -> dict:
    """The control envelope computed EXACTLY rather than simulated.

    max |pseudo-Delta| over the sham and random families is the maximum of
    two independent, discrete, symmetric statistics, so its distribution is
    a closed-form product of two CDFs -- no sampling error, and rule 10's
    warning about under-sampled nulls does not apply. The simulated version
    is kept above for continuity with the committed 2026-08-20 artifact;
    this is the one the LOCK-h numbers use.
    """
    def folded(n):
        """Distribution of |k/n - 0.5| under p = 0.5, aggregating the two
        tails onto each shared magnitude. Correct for either parity."""
        ks = np.arange(n + 1)
        pmf = stats.binom.pmf(ks, n, 0.5)
        vals = np.round(np.abs(ks / n - 0.5), 12)
        uniq = np.unique(vals)
        probs = np.array([float(pmf[vals == u].sum()) for u in uniq])
        return uniq, probs

    vs, ps = folded(n_sham)
    vr, pr = folded(n_rand)
    support = np.unique(np.concatenate([vs, vr]))
    cdf_s = np.array([ps[vs <= v + 1e-12].sum() for v in support])
    cdf_r = np.array([pr[vr <= v + 1e-12].sum() for v in support])
    cdf = cdf_s * cdf_r
    pmf_env = np.diff(np.concatenate([[0.0], cdf]))

    def q(alpha):
        return float(support[np.searchsorted(cdf, alpha - 1e-12)])

    return {"support": support, "pmf": pmf_env, "cdf": cdf,
            "p50": q(0.50), "p90": q(0.90), "p95": q(0.95),
            "mean": float((support * pmf_env).sum()),
            "n_sham": n_sham, "n_rand": n_rand, "exact": True}


def conjunctive_power(delta: float, k_binom: int, env_thresh: float,
                      n_map: int = 48, p0: float = 0.5) -> float:
    """P(ALL verdict conjuncts fire) when the true per-session share is
    p0 + delta. Exact, by convolving the two counterbalance maps.

    The three conjuncts are PROPOSAL-h §3 / the e2a criterion:
      (1) pooled Delta strictly exceeds the control envelope,
      (2) Delta >= 0 in BOTH maps (the sign lock),
      (3) exact binomial at the pooled n.
    """
    n_tot = 2 * n_map
    pmf = stats.binom.pmf(np.arange(n_map + 1), n_map, p0 + delta)
    k1 = np.arange(n_map + 1)[:, None]
    k2 = np.arange(n_map + 1)[None, :]
    tot = k1 + k2
    # strict '>' against the envelope; the epsilon keeps a threshold that is
    # exactly an integer count (env p90 = 6/36 puts it at exactly 64.0) from
    # being lost to binary representation
    k_env = int(np.floor(n_tot * (p0 + env_thresh) + 1e-9)) + 1
    k_sign = int(np.ceil(p0 * n_map - 1e-9))
    ok = (tot >= k_binom) & (tot >= k_env) & (k1 >= k_sign) & (k2 >= k_sign)
    return float((np.outer(pmf, pmf) * ok).sum())


def mde_conjunctive(k_binom: int, env_thresh: float, n_map: int = 48,
                    power: float = 0.80, step: float = 0.0005) -> float:
    """Smallest true Delta the FULL conjunction detects at `power`."""
    for d in np.arange(0.0, 0.5 + step, step):
        if conjunctive_power(float(d), k_binom, env_thresh, n_map) >= power:
            return float(d)
    return 0.5


def max_leak_at_false_verdict_rate(k_binom: int, env_thresh: float,
                                   n_map: int = 48, rate: float = 0.025,
                                   step: float = 0.0005) -> tuple[float, float]:
    """Largest leak whose false-verdict rate stays <= `rate`.

    A leak does not merely add noise: a systematic displacement of size L
    makes the verdict criteria fire on a campaign with NO genuine coupling.
    This inverts that -- how large may L be before the conjunction fires
    more than `rate` of the time on nothing. Returns (L, rate at L).
    """
    prev, prev_r = 0.0, conjunctive_power(0.0, k_binom, env_thresh, n_map)
    for d in np.arange(0.0, 0.5 + step, step):
        r = conjunctive_power(float(d), k_binom, env_thresh, n_map)
        if r > rate:
            return prev, prev_r
        prev, prev_r = float(d), r
    return prev, prev_r


def clopper_upper(k: int, n: int, conf: float = 0.95) -> float:
    """Upper limit of the two-sided exact (Clopper-Pearson) interval."""
    a = (1.0 - conf) / 2.0
    return 1.0 if k >= n else float(stats.beta.ppf(1.0 - a, k + 1, n - k))


def _est_kmax(n: int, bar: float, conf: float) -> int:
    """Largest k whose CI upper bound still clears the bar (monotone in k)."""
    lo, hi = -1, n
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if clopper_upper(mid, n, conf) - 0.5 <= bar:
            lo = mid
        else:
            hi = mid
    return lo


def est_gate_n(bar: float, conf: float = 0.95, assurance: float = 0.80,
               n_max: int = 6000) -> dict:
    """The estimation framing: H1 PASSES when the interval clears the bar.

    Two n's, because they answer different questions:
      n_possible  -- the smallest n at which a PERFECT result (Delta-hat = 0)
                     produces an interval inside the bar. Below this the gate
                     cannot pass however clean the data.
      n_assurance -- the smallest n at which the gate passes with probability
                     >= `assurance` when the true leak really is zero. This
                     is the honest counterpart to 'power >= 0.8', because a
                     gate that only passes on a perfect draw is not a gate.
    """
    n_possible = None
    for n in range(4, n_max + 1, 2):
        if clopper_upper(n // 2, n, conf) - 0.5 <= bar:
            n_possible = n
            break
    n_assurance, pr_at = None, None
    for n in range(n_possible or 4, n_max + 1, 2):
        kmax = _est_kmax(n, bar, conf)
        if kmax < 0:
            continue
        pr = float(stats.binom.cdf(kmax, n, 0.5)
                   - stats.binom.cdf(n - kmax - 1, n, 0.5))
        if pr >= assurance:
            n_assurance, pr_at = n, pr
            break
    return {"ci_conf": conf, "bar": bar, "n_possible": n_possible,
            "n_assurance": n_assurance, "assurance_target": assurance,
            "assurance_achieved": pr_at,
            "half_width_at_n_possible": (
                clopper_upper((n_possible or 0) // 2, n_possible, conf) - 0.5
                if n_possible else None)}


def cluster_table(n_reads_required: int, reads_per_session: int,
                  iccs=(0.0, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0)) -> list[dict]:
    """Sessions needed if H1 pools every within-session read.

    DEFF = 1 + (m - 1) x ICC, the standard design effect; n_eff = n x m/DEFF.
    At ICC = 1 the six reads carry one session's worth of information and
    pooling buys exactly nothing, which is the sanity check on the formula.

    CAVEAT, and it is not a small one: pooling reads 2..6 changes the DV.
    The registered primary is the FIRST free choice, whose live state is the
    counterbalanced forced-phase state. Later reads sit under a state the
    subject's own previous choice delivered, so they are a different
    quantity measured on a selected sub-population -- not more of the same
    quantity. The arithmetic below says what pooling would buy IF the reads
    were exchangeable; whether they may be pooled at all is a design-instance
    question, not an arithmetic one.
    """
    rows = []
    for icc in iccs:
        deff = 1.0 + (reads_per_session - 1) * icc
        n_sessions = int(np.ceil(n_reads_required * deff / reads_per_session))
        rows.append({"icc": icc, "deff": round(deff, 3),
                     "reads_per_session": reads_per_session,
                     "n_sessions_required": n_sessions,
                     "n_reads_total": n_sessions * reads_per_session,
                     "effective_independent_reads": int(
                         np.floor(n_sessions * reads_per_session / deff))})
    return rows


def lockh_v1(args, k_binom_1s: int) -> dict:
    """The LOCK-h v1 table. Arithmetic only -- it instantiates nothing."""
    env = exact_envelope(args.n_sham, args.n_rand)
    env_t = env[f"p{int(args.env_quantile * 100)}"]
    k_binom_2s = critical_k(args.n_verdict, args.alpha / 2.0)

    print("\n" + "=" * 74)
    print("  LOCK-h v1 TABLE -- design-instance conventions, 2026-08-21")
    print("=" * 74)
    print(f"  verdict tier: marker n = {args.n_verdict} "
          f"({args.n_map}/map), sham n = {args.n_sham}, "
          f"random n = {args.n_rand}")
    print(f"  control envelope, EXACT (not simulated): "
          f"p50 {env['p50']:.4f} | p90 {env['p90']:.4f} | "
          f"p95 {env['p95']:.4f} | mean {env['mean']:.4f}")
    print(f"  envelope conjunct held at p{int(args.env_quantile * 100)} "
          f"= {env_t:.4f}")
    print(f"  binomial conjunct: k >= {k_binom_1s} one-sided "
          f"(registered, PROPOSAL-h §3); k >= {k_binom_2s} if read two-sided")
    print(f"  sign-lock conjunct: Delta >= 0 in BOTH maps of "
          f"{args.n_map}")

    variants = []
    for label, kb in (("one-sided (registered)", k_binom_1s),
                      ("two-sided (sensitivity)", k_binom_2s)):
        mde_c = mde_conjunctive(kb, env_t, args.n_map, args.power)
        pw0 = conjunctive_power(0.0, kb, env_t, args.n_map)
        leak, leak_r = max_leak_at_false_verdict_rate(
            kb, env_t, args.n_map, args.false_verdict_rate)
        bar_half = 0.5 * mde_c
        bar = min(bar_half, leak)
        variants.append({
            "binomial_reading": label, "k_binom": kb,
            "env_threshold": env_t, "env_quantile": args.env_quantile,
            "mde_conjunctive": mde_c,
            "power_at_delta_zero": pw0,
            "half_mde": bar_half,
            "leak_at_false_verdict_rate": leak,
            "false_verdict_rate_at_that_leak": leak_r,
            "false_verdict_rate_target": args.false_verdict_rate,
            "bar_leak": bar,
            "binding_branch": ("0.5 x MDE_conj" if bar_half <= leak
                               else f"leak at <= {args.false_verdict_rate:.1%} "
                                    f"false-verdict rate")})

    print(f"\n  {'binomial reading':<24} {'MDE_conj':>9} {'0.5xMDE':>9} "
          f"{'leak@2.5%':>10} {'bar_leak':>9}  binds")
    for v in variants:
        print(f"  {v['binomial_reading']:<24} {v['mde_conjunctive']:>9.4f} "
              f"{v['half_mde']:>9.4f} {v['leak_at_false_verdict_rate']:>10.4f} "
              f"{v['bar_leak']:>9.4f}  {v['binding_branch']}")
    print(f"\n  type-I of the full conjunction at Delta = 0: "
          f"{variants[0]['power_at_delta_zero']:.5f} one-sided "
          f"(the sign-lock and envelope conjuncts, not the binomial, are "
          f"what hold it there)")

    reg = variants[0]
    bar = reg["bar_leak"]

    print(f"\n  --- H1 n under bar_leak = {bar:.4f} "
          f"({reg['binding_branch']}) ---")
    n_rej = None
    for n in range(4, 6001, 2):
        if power_two_sided(n, args.alpha, bar) >= 0.80:
            n_rej = n
            break
    pw_at_drafted = power_two_sided(args.n_h1, args.alpha, bar)
    print(f"  rejection framing (two-sided exact, power >= 0.80): "
          f"n >= {n_rej}")
    print(f"    power at the drafted n = {args.n_h1}: {pw_at_drafted:.3f}")

    est = est_gate_n(bar, args.ci_conf, 0.80)
    print(f"  estimation framing ({args.ci_conf:.0%} CI upper bound "
          f"<= bar):")
    print(f"    n at which the gate CAN pass (Delta-hat = 0): "
          f"{est['n_possible']}  "
          f"(half-width {est['half_width_at_n_possible']:.4f})")
    print(f"    n at which it passes with probability >= 0.80 when the "
          f"true leak is 0: {est['n_assurance']} "
          f"(achieved {est['assurance_achieved']:.3f})")

    basis = est["n_assurance"] or n_rej
    clus = cluster_table(basis, args.reads_per_session)
    print(f"\n  --- pooled within-session reads, cluster-corrected "
          f"(m = {args.reads_per_session}, e2a lineage) ---")
    print(f"  sessions needed to buy {basis} independent-equivalent reads:")
    print(f"    {'ICC':>5} {'DEFF':>6} {'sessions':>9} {'total reads':>12}")
    for r in clus:
        print(f"    {r['icc']:>5.2f} {r['deff']:>6.2f} "
              f"{r['n_sessions_required']:>9} {r['n_reads_total']:>12}")
    print(f"  NOTE: pooling reads 2..{args.reads_per_session} changes the DV "
          f"(later reads sit under a self-delivered state, on a selected "
          f"sub-population). Arithmetic only.")

    print(f"\n  ARITHMETIC ONLY -- LOCK-h.md is design-instance authored.")
    return {
        "conventions_dated": "2026-08-21",
        "envelope_exact": {k: (v.tolist() if isinstance(v, np.ndarray) else v)
                           for k, v in env.items()},
        "envelope_threshold_used": env_t,
        "variants": variants,
        "registered_variant": reg["binomial_reading"],
        "bar_leak": bar,
        "h1_rejection_framing": {
            "test": "two-sided exact binomial",
            "alpha": args.alpha, "power_target": 0.80,
            "n_required": n_rej,
            "power_at_drafted_n": pw_at_drafted,
            "drafted_n": args.n_h1},
        "h1_estimation_framing": est,
        "cluster_correction": {
            "basis_n_independent_reads": basis,
            "basis_framing": ("estimation, assurance 0.80"
                              if est["n_assurance"] else
                              "rejection, power 0.80"),
            "reads_per_session": args.reads_per_session,
            "rows": clus,
            "caveat": ("pooling reads 2..m changes the DV: the registered "
                       "primary is the FIRST free choice, and later reads "
                       "sit under a state the subject's own previous choice "
                       "delivered, on a selected sub-population")},
        "reading_of_'two-sided'": (
            "taken as settling H1's gate, which is on |Delta_first|. The "
            "verdict tier's binomial stays ONE-sided because PROPOSAL-h §3 "
            "registers it that way and a paste-block convention does not "
            "amend a committed pre-registration; the two-sided verdict is "
            "computed as a sensitivity row so the difference is visible."),
        "decides_nothing": ("Code delivers arithmetic; LOCK-h.md is authored "
                            "by the design instance."),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-verdict", type=int, default=96)
    ap.add_argument("--n-h1", type=int, default=64)
    ap.add_argument("--n-sham", type=int, default=36)
    ap.add_argument("--n-rand", type=int, default=36)
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--power", type=float, default=0.80)
    ap.add_argument("--n-map", type=int, default=48,
                    help="marker sessions per counterbalance map; the "
                         "sign-lock conjunct is evaluated on each")
    ap.add_argument("--env-quantile", type=float, default=0.90,
                    help="quantile of the control envelope at which the "
                         "envelope conjunct is held (LOCK-h v1: p90)")
    ap.add_argument("--false-verdict-rate", type=float, default=0.025,
                    help="the rate a leak may not push the verdict criteria past on a campaign with no genuine coupling")
    ap.add_argument("--reads-per-session", type=int, default=6,
                    help="consequential free choices per session "
                         "(e2a lineage: 6), for the cluster correction")
    ap.add_argument("--ci-conf", type=float, default=0.95,
                    help="confidence level for the estimation-gate "
                         "variant")
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

    lock = lockh_v1(args, k)

    out = {
        "item": "LOCK-h power arithmetic",
        "lockh_v1": lock,
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
