"""Statistics the ledger names, in pure python + numpy.

No scipy: the laptop env does not have it, the box should not need it, and
every test here is short enough that an exact implementation is preferable
to a dependency whose default `alternative=` or continuity correction could
silently change a published number.

Ported semantics, not reinvented ones:

- `paired_tost` is `scripts/slice2_primary_tost.py:paired_tost` verbatim in
  behavior -- per-item differences, ddof=1, Z90 = 1.645, equivalent iff the
  90% CI is contained in +/-margin.
- `binom_test_exact` is the bar rule 21 makes binding for measured-base-rate
  defect classes ("exact binomial vs declared p0 at every scale"). Two-sided
  uses the method of small p-values (sum of all outcomes no more likely than
  the observed one), which is what an exact binomial test means when nobody
  says otherwise.
- `fisher_one_sided` is the cycle-4 exclusion-asymmetry test (the CORR
  anomaly, p = .035, post-hoc and weightless -- rule 11).

Rule 9 governs use, not implementation: z is descriptive, criteria are
sign-lock plus magnitude against the control null, and bars are committed
before data.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb, sqrt
from typing import Iterable, Sequence

import numpy as np

Z90 = 1.645        # one-sided 95% / TOST 90% CI (slice-2 locked spec)


# --- equivalence ---------------------------------------------------------
@dataclass(frozen=True)
class TOSTResult:
    equivalent: bool
    mean_diff: float
    half_width: float
    margin: float
    n: int

    @property
    def ci(self) -> tuple[float, float]:
        return (self.mean_diff - self.half_width, self.mean_diff + self.half_width)


def paired_tost(vec_a: Sequence[float], vec_b: Sequence[float],
                margin: float, z: float = Z90) -> TOSTResult:
    """Paired TOST: the per-item difference cancels item difficulty, so the
    CI on the mean difference is far tighter than an unpaired interval.
    Equivalent iff the 90% CI lies wholly inside +/-margin."""
    a = np.asarray(vec_a, dtype=np.float64)
    b = np.asarray(vec_b, dtype=np.float64)
    if a.shape != b.shape:
        raise ValueError(f"paired TOST needs matched vectors: {a.shape} vs {b.shape}")
    d = a - b
    mean_d = float(np.mean(d))
    se = float(np.std(d, ddof=1) / sqrt(len(d)))
    half = z * se
    return TOSTResult(
        equivalent=bool((mean_d - half) >= -margin and (mean_d + half) <= margin),
        mean_diff=mean_d, half_width=half, margin=float(margin), n=int(len(d)))


# --- exact binomial ------------------------------------------------------
def binom_pmf(k: int, n: int, p: float) -> float:
    if k < 0 or k > n:
        return 0.0
    if p <= 0.0:
        return 1.0 if k == 0 else 0.0
    if p >= 1.0:
        return 1.0 if k == n else 0.0
    return comb(n, k) * (p ** k) * ((1.0 - p) ** (n - k))


def binom_sf_inclusive(k: int, n: int, p: float) -> float:
    """P(X >= k)."""
    return float(sum(binom_pmf(i, n, p) for i in range(max(k, 0), n + 1)))


def binom_cdf(k: int, n: int, p: float) -> float:
    """P(X <= k)."""
    return float(sum(binom_pmf(i, n, p) for i in range(0, min(k, n) + 1)))


def binom_test_exact(k: int, n: int, p0: float,
                     alternative: str = "two-sided") -> float:
    """Exact binomial p-value for k successes in n against declared p0.

    `alternative`: "greater" (P(X >= k)), "less" (P(X <= k)), or "two-sided"
    (method of small p-values). Rule 21 makes this the binding form for any
    defect class with a measured, non-zero healthy base rate -- hair-trigger
    bars are reserved for classes whose healthy base rate is ~zero.
    """
    if n < 0 or not (0 <= k <= n):
        raise ValueError(f"invalid counts k={k} n={n}")
    if alternative == "greater":
        return binom_sf_inclusive(k, n, p0)
    if alternative == "less":
        return binom_cdf(k, n, p0)
    if alternative != "two-sided":
        raise ValueError(f"unknown alternative {alternative!r}")
    obs = binom_pmf(k, n, p0)
    tol = obs * (1.0 + 1e-9)
    return float(sum(pm for i in range(n + 1)
                     if (pm := binom_pmf(i, n, p0)) <= tol))


# --- checkpointed monitors (rule 21) -------------------------------------
@dataclass(frozen=True)
class MonitorReading:
    fired: bool
    k: int
    n: int
    p_value: float
    critical_k: int | None
    p0: float
    alpha: float


class CheckpointedBinomialMonitor:
    """A defect-class bar that binds at *every* checkpoint, not only at the
    final n -- the cycle-4 form of the tripwire framework (rule 21).

    The bar is an exact one-sided binomial against a declared base rate p0
    at the declared alpha. `critical_k(n)` is the smallest count that would
    fire at that n, so a run can print its own headroom before it starts and
    the bar cannot be renegotiated mid-run.

    Verdict criteria are untouchable by anything here (rule 21, final
    clause): a monitor firing pauses a run, it never edits a criterion.
    """

    def __init__(self, name: str, p0: float, alpha: float = 0.05,
                 checkpoints: Iterable[int] = ()):
        if not 0.0 <= p0 <= 1.0:
            raise ValueError(f"p0 out of range: {p0}")
        self.name = name
        self.p0 = float(p0)
        self.alpha = float(alpha)
        self.checkpoints = tuple(sorted(int(c) for c in checkpoints))

    def critical_k(self, n: int) -> int | None:
        """Smallest k with P(X >= k | n, p0) <= alpha; None if unreachable at
        this n (the honest answer when a run is too small to fire -- a bar
        that cannot fire should be declared, not discovered afterward)."""
        for k in range(0, n + 1):
            if binom_sf_inclusive(k, n, self.p0) <= self.alpha:
                return k
        return None

    def check(self, k: int, n: int) -> MonitorReading:
        p = binom_test_exact(k, n, self.p0, alternative="greater")
        return MonitorReading(fired=bool(p <= self.alpha), k=int(k), n=int(n),
                              p_value=p, critical_k=self.critical_k(n),
                              p0=self.p0, alpha=self.alpha)

    def headroom_table(self, ns: Iterable[int] | None = None) -> list[dict]:
        """Pre-run declaration: at each checkpoint, the count that fires and
        the count that is still clean. Printed into the pre-registration."""
        out = []
        for n in (tuple(ns) if ns is not None else self.checkpoints):
            crit = self.critical_k(n)
            out.append({"n": int(n), "critical_k": crit,
                        "max_clean_k": None if crit is None else crit - 1,
                        "can_fire": crit is not None})
        return out


# --- 2x2 ------------------------------------------------------------------
def fisher_one_sided(a: int, b: int, c: int, d: int) -> float:
    """One-sided Fisher exact for the table [[a, b], [c, d]], testing excess
    in the a cell. Hypergeometric tail, exact."""
    n = a + b + c + d
    row1, col1 = a + b, a + c
    lo = max(0, col1 - (n - row1))
    hi = min(row1, col1)
    denom = comb(n, col1)
    return float(sum(comb(row1, i) * comb(n - row1, col1 - i)
                     for i in range(a, hi + 1)) / denom) if denom else float("nan")


__all__ = ["Z90", "TOSTResult", "paired_tost", "binom_pmf", "binom_cdf",
           "binom_sf_inclusive", "binom_test_exact", "MonitorReading",
           "CheckpointedBinomialMonitor", "fisher_one_sided"]
