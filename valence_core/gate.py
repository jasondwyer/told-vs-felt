"""The matched-pair swing criterion (ledger 9) -- the program's standing
association/preference bar, ported off `scripts/c1_gate.py`.

The shape of the argument, which is why this is the bar and not a z-test:
a conditioned pair and every control pair are measured in *both*
counterbalanced replicates. The quantity of interest is the **swing** --
how much a pair's signed alignment moves when the assignment flips. A tag
artifact produces a large alignment but cannot swing with an assignment it
knows nothing about, so the control-pair swings are the null, and the
conditioned swing has to clear all of them.

Rule 9 in force here:
  (i)   sign lock: D_cond > 0 in the oriented direction;
  (ii)  magnitude: D_cond > max |control swing|;
  (iii) >= 20 shared control pairs (28 standard) for the criterion to be
        valid at all;
  and z is **descriptive only** -- it is computed and reported because it
  is informative, and it decides nothing. Rule 10 is why: an under-sampled
  null flatters weak signals, and this program has a 6.8-sigma corpse
  (r2, 6 pairs) to prove it.

Bars are committed before data generation (rule 9) -- this module computes
a verdict, it never chooses one.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

MIN_CONTROL_PAIRS = 20          # rule 9 floor; 28 is the standard roster


@dataclass(frozen=True)
class SwingResult:
    d_cond: float
    swings: tuple[float, ...]
    n_pairs: int
    max_abs_swing: float
    mean_abs_swing: float
    sd_swing: float
    z_descriptive: float
    sign_ok: bool
    magnitude_ok: bool
    n_ok: bool
    passed: bool
    notes: tuple[str, ...] = field(default_factory=tuple)

    def summary(self) -> str:
        return (f"D_cond={self.d_cond:+.4f}  "
                f"null n={self.n_pairs} max|s|={self.max_abs_swing:.4f} "
                f"sd={self.sd_swing:.4f}  z={self.z_descriptive:+.1f} (descriptive)  "
                f"sign {'PASS' if self.sign_ok else 'fail'} / "
                f"magnitude {'PASS' if self.magnitude_ok else 'fail'} / "
                f"n {'ok' if self.n_ok else 'BELOW FLOOR'}  "
                f"-> {'PASS' if self.passed else 'FAIL'}")


def matched_pair_swing(hi_rep: dict, lo_rep: dict,
                       min_pairs: int = MIN_CONTROL_PAIRS) -> SwingResult:
    """`hi_rep` is the replicate in which the conditioned tag C carries the
    *hi* state; `lo_rep` its counterbalanced partner. Both dicts need
    `cos_ad_raw` (the unsigned conditioned alignment) and `ctrl_cos_by_pair`
    ({"tagA|tagB": cosine}).

    Only control pairs present in *both* replicates contribute -- a swing is
    undefined for a pair measured once.
    """
    shared = sorted(set(hi_rep.get("ctrl_cos_by_pair", {}))
                    & set(lo_rep.get("ctrl_cos_by_pair", {})))
    swings = tuple(float(hi_rep["ctrl_cos_by_pair"][k]
                         - lo_rep["ctrl_cos_by_pair"][k]) for k in shared)
    d_cond = float(hi_rep["cos_ad_raw"] - lo_rep["cos_ad_raw"])

    if swings:
        arr = np.asarray(swings, dtype=np.float64)
        max_abs = float(np.max(np.abs(arr)))
        mean_abs = float(np.mean(np.abs(arr)))
        sd = float(np.std(arr))                 # population sd, as published
        z = d_cond / sd if sd > 0 else float("nan")
    else:
        max_abs = mean_abs = sd = z = float("nan")

    sign_ok = d_cond > 0
    mag_ok = bool(swings) and d_cond > max_abs
    n_ok = len(swings) >= min_pairs

    notes = []
    if not n_ok:
        notes.append(
            f"only {len(swings)} shared control pairs (>= {min_pairs} "
            f"pre-registered) -- criterion NOT valid; rule 10: under-sampled "
            f"nulls flatter weak signals")
    return SwingResult(
        d_cond=d_cond, swings=swings, n_pairs=len(swings),
        max_abs_swing=max_abs, mean_abs_swing=mean_abs, sd_swing=sd,
        z_descriptive=z, sign_ok=sign_ok, magnitude_ok=mag_ok, n_ok=n_ok,
        passed=bool(sign_ok and mag_ok and n_ok), notes=tuple(notes))


def orient_replicates(rep_a: dict, rep_b: dict) -> tuple[dict, dict]:
    """Return (hi_rep, lo_rep) by each replicate's own assignment record, so
    orientation is never a caller's guess. Raises if both replicates claim
    the same assignment -- that is a counterbalancing failure (rule 12), not
    something to average over."""
    def c_state(rep):
        return rep["assignment"]["C"]
    if c_state(rep_a) == c_state(rep_b):
        raise ValueError(
            f"both replicates assign C -> {c_state(rep_a)!r}: not "
            f"counterbalanced, so no swing is defined (rule 12)")
    return (rep_a, rep_b) if c_state(rep_a) == "hi" else (rep_b, rep_a)


__all__ = ["MIN_CONTROL_PAIRS", "SwingResult", "matched_pair_swing",
           "orient_replicates"]
