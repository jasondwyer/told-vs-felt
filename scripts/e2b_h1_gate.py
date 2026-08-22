#!/usr/bin/env python3
"""Evaluate the H1 gate over a committed campaign artifact (LOCK-h v1.4 §3),
plus the §3b registered secondary analyses.

Separate from the runner on purpose. The §3 criterion needs an exact
Clopper-Pearson interval and no python on this laptop has scipy (handoff trap
9) -- but the separation is a feature independent of that: the runner collects
to a stop rule that depends only on totals, and a runner that cannot compute
the verdict cannot be accused of stopping when it liked the verdict.

## The criterion, as written

At stop, the exact 95% CI on L from b | n_d ~ Binomial(n_d, 1/2), mapped
through pi_hat_d = n_d/N:

    [ (2 p_lo - 1) * pi_hat , (2 p_hi - 1) * pi_hat ]

  PASS          the interval lies entirely within (-bar, +bar)
  FAIL          it lies entirely outside
  INDETERMINATE it straddles a bar -> §3 extends once

The mapped interval is always inside [-pi_hat, +pi_hat], so any campaign
stopping with pi_hat < bar passes automatically. That is §3's feasibility
corollary, not a loophole: a leak cannot exceed the discordance carrying it.
When a PASS arrives that way it is reported as **certification by low
discordance**, not as a powered directional test -- the reporting rule
ratified on 2026-08-21.

## §3b, registered before H1 data and never gate-relevant

Exact uniform-placement permutation test, 200,000 draws, on (i) ICC and
(ii) the count of sessions carrying >= 2 flips; alpha = .05 each, two-sided
by tail probability. Significant -> flips are session-structured, which feeds
the mechanism discussion and any extension planning. Null -> the i.i.d.
treatment stands. H2's post-hoc values (0.017, 0.0115) may be cited
descriptively beside the result, never pooled into it.

Usage:
    python scripts/e2b_h1_gate.py
    python scripts/e2b_h1_gate.py --sessions data/e2b/h1_sessions.json
"""
from __future__ import annotations

import argparse
import json
import os

import numpy as np
from scipy import stats

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "data")


def cp_interval(k: int, n: int, conf: float = 0.95) -> tuple[float, float]:
    a = (1.0 - conf) / 2.0
    lo = 0.0 if k == 0 else float(stats.beta.ppf(a, k, n - k + 1))
    hi = 1.0 if k >= n else float(stats.beta.ppf(1.0 - a, k + 1, n - k))
    return lo, hi


def icc_binary(groups) -> float | None:
    groups = [g for g in groups if g]
    if len(groups) < 2:
        return None
    N = sum(len(g) for g in groups)
    grand = sum(sum(g) for g in groups) / N
    msb = sum(len(g) * (np.mean(g) - grand) ** 2
              for g in groups) / (len(groups) - 1)
    dfw = N - len(groups)
    if dfw <= 0:
        return None
    msw = sum(((np.array(g) - np.mean(g)) ** 2).sum() for g in groups) / dfw
    k0 = (N - sum(len(g) ** 2 for g in groups) / N) / (len(groups) - 1)
    den = msb + (k0 - 1) * msw
    return float(max(0.0, 0.0 if den <= 0 else (msb - msw) / den))


def two_sided_tail_p(null: np.ndarray, obs: float) -> float:
    """Two-sided by tail probability, as §3b specifies."""
    hi = float((null >= obs - 1e-12).mean())
    lo = float((null <= obs + 1e-12).mean())
    return float(min(1.0, 2.0 * min(hi, lo)))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sessions", default=os.path.join(DATA, "e2b/h1_sessions.json"))
    ap.add_argument("--bar", type=float, default=0.0735)
    ap.add_argument("--conf", type=float, default=0.95)
    ap.add_argument("--draws", type=int, default=200_000)
    ap.add_argument("--seed", type=int, default=26)
    ap.add_argument("--out", default=os.path.join(DATA, "e2b/h1_gate.json"))
    args = ap.parse_args()

    d = json.load(open(args.sessions))
    b_ = d["budget"]
    N, n_d, b, c = b_["N"], b_["n_d"], b_["b"], b_["c"]
    pi = n_d / N
    L_hat = (b - c) / N

    print("=== H1 GATE (LOCK-h v1.4 §3) ===")
    print(f"  artifact: {os.path.relpath(args.sessions, REPO)}")
    print(f"  audit sha {d.get('audit_sha16')} | rounds cached "
          f"{d.get('round_path_cached')} | sessions run {d['n_run']} of "
          f"{d['n_scheduled']}")
    print(f"  STOP: {b_['stop_reason']} at {b_['stop_at']}")
    print(f"  N = {N}, n_d = {n_d} (b = {b}, c = {c}), "
          f"pi_hat_d = {pi:.4f}, L_hat = {L_hat:+.5f}")

    if n_d == 0:
        p_lo, p_hi = 0.0, 1.0
    else:
        p_lo, p_hi = cp_interval(b, n_d, args.conf)
    L_lo, L_hi = (2 * p_lo - 1) * pi, (2 * p_hi - 1) * pi
    inside = (L_lo > -args.bar) and (L_hi < args.bar)
    outside = (L_lo > args.bar) or (L_hi < -args.bar)
    verdict = "PASS" if inside else ("FAIL" if outside else "INDETERMINATE")

    print(f"\n  exact {args.conf:.0%} CI on p_flip = {b}/{n_d}: "
          f"[{p_lo:.4f}, {p_hi:.4f}]")
    print(f"  mapped through pi_hat_d -> L CI = [{L_lo:+.5f}, {L_hi:+.5f}]")
    print(f"  bar_leak = +/-{args.bar}")
    print(f"\n  VERDICT: {verdict}")
    by_corollary = pi < args.bar
    if verdict == "PASS" and by_corollary:
        print(f"  Reported as CERTIFICATION BY LOW DISCORDANCE, not as a "
              f"powered directional test: pi_hat_d = {pi:.4f} is already "
              f"below the bar, so the mapped interval lies inside "
              f"[-pi_hat, +pi_hat] whatever the b/c split. §3's feasibility "
              f"corollary -- a leak cannot exceed the discordance carrying "
              f"it -- is what certifies here.")
    pil, pih = cp_interval(n_d, N, args.conf)
    print(f"  pi_hat_d exact {args.conf:.0%} CI [{pil:.4f}, {pih:.4f}]; "
          f"upper below bar: {pih < args.bar}")

    # --- §3b registered secondaries -------------------------------------
    groups = [[int(ch["flipped"]) for ch in s["choices"]]
              for s in d["sessions"] if s["choices"]]
    icc_obs = icc_binary(groups)
    ge2_obs = sum(1 for g in groups if sum(g) >= 2)
    n_sess, k = len(groups), max(len(g) for g in groups)
    flat = sum(len(g) for g in groups)
    rng = np.random.default_rng(args.seed)
    null_icc = np.empty(args.draws)
    null_ge2 = np.empty(args.draws, dtype=int)
    sizes = np.array([len(g) for g in groups])
    edges = np.concatenate([[0], np.cumsum(sizes)])
    for t in range(args.draws):
        pos = rng.choice(flat, size=n_d, replace=False)
        v = np.zeros(flat, dtype=int); v[pos] = 1
        gs = [list(v[edges[i]:edges[i + 1]]) for i in range(n_sess)]
        null_icc[t] = icc_binary(gs) or 0.0
        null_ge2[t] = sum(1 for g in gs if sum(g) >= 2)
    p_icc = two_sided_tail_p(null_icc, icc_obs or 0.0)
    p_ge2 = two_sided_tail_p(null_ge2.astype(float), float(ge2_obs))

    print(f"\n  --- §3b REGISTERED SECONDARIES (never gate-relevant) ---")
    print(f"    {n_sess} sessions with reads, {flat} reads, {n_d} flips")
    print(f"    (i)  ICC-hat = {icc_obs:.4f}; null mean {null_icc.mean():.4f}"
          f" -> two-sided p = {p_icc:.4f}  "
          f"{'SIGNIFICANT' if p_icc <= 0.05 else 'null'}")
    print(f"    (ii) sessions with >= 2 flips = {ge2_obs}; null mean "
          f"{null_ge2.mean():.3f} -> two-sided p = {p_ge2:.4f}  "
          f"{'SIGNIFICANT' if p_ge2 <= 0.05 else 'null'}")
    struct = (p_icc <= 0.05) or (p_ge2 <= 0.05)
    print(f"    reading: {'flips are session-structured' if struct else 'the i.i.d. treatment stands'}")
    print(f"    H2's post-hoc values (0.017, 0.0115) are cited descriptively "
          f"beside this, never pooled into it.")

    print(f"\n  monitors: degeneracy {d['n_degenerate']}/{d['n_rounds']} = "
          f"{d['n_degenerate'] / d['n_rounds']:.4f}; excluded "
          f"{d['n_excluded']}/{d['n_run']}; window clipped "
          f"{d['window']['n_encodes_clipped']}")

    out = {"item": "H1 gate evaluation", "lock": "LOCK-h v1.4 §3 + §3b",
           "source": os.path.relpath(args.sessions, REPO),
           "audit_sha16": d.get("audit_sha16"),
           "stop_reason": b_["stop_reason"], "stop_at": b_["stop_at"],
           "N": N, "n_d": n_d, "b": b, "c": c,
           "pi_hat_d": pi, "pi_hat_d_ci": [pil, pih],
           "L_hat": L_hat, "p_flip_ci": [p_lo, p_hi],
           "L_ci": [L_lo, L_hi], "bar_leak": args.bar,
           "verdict": verdict,
           "certified_by_low_discordance": bool(verdict == "PASS"
                                                and by_corollary),
           "secondary_3b": {
               "n_sessions": n_sess, "n_reads": flat, "n_flips": n_d,
               "icc_obs": icc_obs, "icc_p_two_sided": p_icc,
               "sessions_ge2_obs": ge2_obs, "sessions_ge2_p_two_sided": p_ge2,
               "draws": args.draws, "seed": args.seed,
               "reading": ("flips are session-structured" if struct
                           else "the i.i.d. treatment stands"),
               "gate_relevant": False},
           "monitors": {"degeneracy": [d["n_degenerate"], d["n_rounds"]],
                        "excluded": [d["n_excluded"], d["n_run"]],
                        "clipped": d["window"]["n_encodes_clipped"]},
           "decides_nothing": ("Code evaluates the declared criterion over a "
                               "committed artifact; the campaign's "
                               "disposition is the design instance's.")}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
