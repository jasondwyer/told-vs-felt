"""Model-free half of the ledger-26 suite: every published number that can
be recomputed from a committed artifact, recomputed through `valence_core`.

    uv run python -m valence_core.regression.analysis      (or any python)

Each check names the document it is holding the port to, so a failure says
which claim just stopped reproducing rather than merely that something
moved. Every input is in the repo (ledger 27) -- this suite does not read
the gitignored clone, which is the point: it must run on the box.

Deliberately NOT in here: anything requiring a forward pass. Those are the
three oracle criteria and they run on the laptop.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass

import numpy as np

from ..gate import matched_pair_swing
from ..stats import binom_test_exact, fisher_one_sided
from ..adapters.base import sha16_arr

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(REPO, "data")

TOL = 5e-5


@dataclass
class Check:
    name: str
    source: str
    expected: str
    got: str
    ok: bool


def _c(name, source, expected, got, ok) -> Check:
    return Check(name, source, str(expected), str(got), bool(ok))


def check_frozen_shas() -> list[Check]:
    """Rule 1: the direction artifacts every published dose was computed
    from are the ones in the record."""
    out = []
    Z = np.load(os.path.join(DATA, "e0/e0_axes.npz"))
    stack = np.stack([Z["span_reward"], Z["span_sentiment"], Z["span_character"]])
    got = sha16_arr(stack)
    out.append(_c("e0 axes sha", "e2a.AXES_SHA", "d4791bdc4877da3d", got,
                  got == "d4791bdc4877da3d"))
    layers = [int(x) for x in Z["layers"]]
    R = np.load(os.path.join(DATA, "e0/e0_random_dirs.npz"))
    gotr = sha16_arr(np.stack([R[f"L{L}"] for L in layers]))
    out.append(_c("e0 random-dirs sha", "e2a.RAND_SHA", "b6bd2f5f580ee13e",
                  gotr, gotr == "b6bd2f5f580ee13e"))
    out.append(_c("workspace layers", "workspace_layers.WORKSPACE_LAYERS",
                  [40, 44, 48, 52, 56, 60], layers,
                  layers == [40, 44, 48, 52, 56, 60]))
    return out


def check_screen_pvalues() -> list[Check]:
    """FINDINGS-4 summary ledger: five contrasts, five p-values. `delta` is
    stored as (share - 0.5), so the count is recoverable exactly."""
    path = os.path.join(DATA, "f/screen_analysis.json")
    contrasts = json.load(open(path))["contrasts"]
    out = []
    for arm, c in contrasts.items():
        n = int(c["n"])
        k = round((c["delta"] + 0.5) * n)
        alt = "two-sided" if c["sided"] == "two" else "greater"
        p = binom_test_exact(k, n, 0.5, alternative=alt)
        out.append(_c(f"screen p [{arm}] {k}/{n}", "FINDINGS-4 summary ledger",
                      f"{c['p']:.5f}", f"{p:.5f}", abs(p - c["p"]) < TOL))
    return out


def check_postscreen_descriptives() -> list[Check]:
    """FINDINGS-4 §7 and the post-screen descriptive entry."""
    out = []
    p = fisher_one_sided(7, 1, 2, 5)
    out.append(_c("CORR exclusion asymmetry (post-hoc, weightless)",
                  "FINDINGS-4 §7", "0.035", f"{p:.3f}", round(p, 3) == 0.035))
    p = binom_test_exact(128, 257, 0.5)
    out.append(_c("brevity-tracking pooled 128/257", "FINDINGS-4 §6",
                  "1.0", f"{p:.4f}", abs(p - 1.0) < 1e-9))
    p = binom_test_exact(23, 44, 0.5)
    out.append(_c("FDBK first-choice 23/44 = .523", "FINDINGS-4 §3",
                  "n.s.", f"p={p:.3f}", p > 0.05))
    return out


def check_c1r3_gate() -> list[Check]:
    """FINDINGS-2 finding 3 + the r3 confirmatory verdict."""
    pa, pb = (os.path.join(DATA, f"configs/c1r3_gate_rep{r}.json") for r in "AB")
    if not (os.path.exists(pa) and os.path.exists(pb)):
        return [_c("c1r3 matched-pair swing", "FINDINGS-2 finding 3",
                   "gate JSONs present", "MISSING from the record", False)]
    A, B = json.load(open(pa)), json.load(open(pb))
    hi, lo = (A, B) if A["assignment"]["C"] == "hi" else (B, A)
    r = matched_pair_swing(hi, lo)
    return [
        _c("c1r3 control pairs", "rule 9 (28 standard)", 28, r.n_pairs,
           r.n_pairs == 28),
        _c("c1r3 z (descriptive)", "FINDINGS-2 finding 3 (28 said 1.6)",
           "1.6", f"{r.z_descriptive:.1f}", abs(r.z_descriptive - 1.6) < 0.05),
        _c("c1r3 verdict", "r3 confirmatory FAIL", "FAIL",
           "PASS" if r.passed else "FAIL", r.passed is False),
    ]


def check_axis_geometry() -> list[Check]:
    """e0_axes.meta.json's per-layer report: the V2/V3 guard decompositions
    and axis cosines that licensed the reward axis as a drug (PROPOSAL-e).
    24 published values -- 6 workspace layers x 4 quantities."""
    from ..extract import cosine, residual_fraction
    Z = np.load(os.path.join(DATA, "e0/e0_axes.npz"))
    meta = json.load(open(os.path.join(DATA, "e0/e0_axes.meta.json")))
    out = []
    for li, row in enumerate(meta["report"]["span"]):
        rw = Z["span_reward"][li]
        se = Z["span_sentiment"][li]
        ch = Z["span_character"][li]
        for label, got, exp in (
                ("cos reward.sentiment", cosine(rw, se), row["cos_reward_sentiment"]),
                ("cos reward.character", cosine(rw, ch), row["cos_reward_character"]),
                ("V2 self-residual", residual_fraction(rw, ch), row["v2_self_residual_frac"]),
                ("V3 eval-residual", residual_fraction(rw, se), row["v3_eval_residual_frac"])):
            out.append(_c(f"L{row['layer']} {label}", "e0_axes.meta.json report",
                          f"{exp:.3f}", f"{got:.3f}", round(got, 3) == exp))
    return out


def check_instrument_invariants() -> list[Check]:
    """Not published numbers -- properties the instruments must have, checked
    because each one has a plausible silent-failure mode."""
    from ..readout import softmax, symmetric_kl
    from ..discrim import auc_from_scores, logistic_auc
    out = []

    p = softmax(np.array([1.0, 2.0, 3.0, 0.5]))
    out.append(_c("softmax normalizes", "readout", "1.0", f"{p.sum():.12f}",
                  abs(p.sum() - 1.0) < 1e-12))
    out.append(_c("symmetric KL(p,p) = 0", "g3' verify identity", "0.0",
                  f"{symmetric_kl(p, p):.2e}", symmetric_kl(p, p) == 0.0))

    # A tie-blind AUC silently inflates when a probe saturates.
    a = auc_from_scores([1.0, 1.0, 1.0, 1.0], [1, 1, 0, 0])
    out.append(_c("AUC all-ties = 0.5", "discrim tie handling", "0.5",
                  f"{a:.3f}", a == 0.5))
    a = auc_from_scores([3.0, 2.0, 1.0, 0.0], [1, 1, 0, 0])
    out.append(_c("AUC separable = 1.0", "discrim", "1.0", f"{a:.3f}", a == 1.0))

    rng = np.random.default_rng(0)
    Xf = rng.normal(size=(40, 8)); yf = (Xf[:, 0] > 0).astype(int)
    Xv = rng.normal(size=(40, 8)); yv = (Xv[:, 0] > 0).astype(int)
    a1 = logistic_auc(Xf, yf, Xv, yv)
    a2 = logistic_auc(Xf, yf, Xv, yv)
    out.append(_c("logistic fit deterministic", "discrim (seeded GD)",
                  f"{a1:.6f}", f"{a2:.6f}", a1 == a2))
    return out


def run_all() -> list[Check]:
    checks: list[Check] = []
    checks += check_frozen_shas()
    checks += check_axis_geometry()
    checks += check_screen_pvalues()
    checks += check_postscreen_descriptives()
    checks += check_c1r3_gate()
    checks += check_instrument_invariants()
    return checks


def main() -> int:
    checks = run_all()
    width = max(len(c.name) for c in checks) + 2
    print("=" * 78)
    print("LEDGER 26 -- analysis-tier regression (no model)")
    print("=" * 78)
    for c in checks:
        status = "PASS" if c.ok else "FAIL"
        print(f"  [{status}] {c.name:<{width}} expected {c.expected:>12} "
              f"got {c.got:>12}   ({c.source})")
    n_fail = sum(1 for c in checks if not c.ok)
    print("-" * 78)
    print(f"  {len(checks) - n_fail}/{len(checks)} reproduced through valence_core")
    if n_fail:
        print("  RULE 26: a mismatch is a refactor bug until proven otherwise.")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
