"""Embedding-probe discriminability -- the manipulation-check instrument,
ported from `scripts/e2a_g2_discriminability.py`.

The question it answers: does a state leave a signature in the *text* the
model produces under it, strong enough that a readout can tell the poles
apart from the record alone? That is the precondition for any
comprehension-mediated channel -- if the transcript does not carry the
state, there is nothing downstream for a choice to be informed by.

Two properties worth preserving deliberately:

- **The probe is fit and evaluated on disjoint task halves** (fit t01-t08,
  val t09-t16), so a qualifying AUC is generalization across items, not
  memorization of a paraphrase.
- **Everything is deterministic and seeded.** The logistic fit is plain
  gradient descent with a fixed seed, iteration count, learning rate and L2
  -- not a solver whose version could move a published AUC. Record
  composition at k > 1 draws from a seeded generator keyed to k.

The instrument reads generated text through an unsteered forward. No state
is ever live at readout (rule 5).
"""

from __future__ import annotations

import zlib
from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np

from .adapters.base import ModelAdapter

AUC_BAR = 0.70                   # e2a g2 qualifying bar
ROUND_SEP = "\n---\n"


def seed_for(*parts: object) -> int:
    """Deterministic per-item seed from stable key parts (crc32, as used for
    every generated round in cycles 3-4). Order matters and is part of the
    key -- reordering the parts produces a different, equally valid stream,
    so a rerun must pass them the same way."""
    key = "|".join(str(p) for p in parts)
    return zlib.crc32(key.encode()) % (2 ** 31)


def auc_from_scores(scores: Sequence[float],
                    labels: Sequence[int]) -> float:
    """Mann-Whitney AUC with explicit tie handling (ties score 0.5).

    Split out from the fit so it is testable on its own: a tie-blind AUC
    silently inflates when a probe saturates, which is exactly the regime a
    manipulation check operates in.
    """
    s = np.asarray(scores, dtype=np.float64)
    y = np.asarray(labels)
    pos, neg = s[y == 1], s[y == 0]
    if not len(pos) or not len(neg):
        return float("nan")
    gt = (pos[:, None] > neg[None, :]).sum()
    eq = (pos[:, None] == neg[None, :]).sum()
    return float((gt + 0.5 * eq) / (len(pos) * len(neg)))


def logistic_auc(X_fit: np.ndarray, y_fit: np.ndarray,
                 X_val: np.ndarray, y_val: np.ndarray,
                 seed: int = 7, iters: int = 300, lr: float = 0.1,
                 l2: float = 1e-2) -> float:
    """Standardize on the fit half, fit logistic regression by full-batch
    gradient descent, score the val half, return AUC.

    Hyperparameters are the published ones and are arguments only so a
    future instrument can declare different ones explicitly; changing a
    default here would move every historical AUC.
    """
    rng = np.random.default_rng(seed)
    mu, sd = X_fit.mean(0), X_fit.std(0) + 1e-6
    Xf, Xv = (X_fit - mu) / sd, (X_val - mu) / sd
    w = rng.normal(0, 0.01, Xf.shape[1])
    b = 0.0
    for _ in range(iters):
        z = Xf @ w + b
        p = 1 / (1 + np.exp(-z))
        w -= lr * (Xf.T @ (p - y_fit) / len(y_fit) + l2 * w)
        b -= lr * float(np.mean(p - y_fit))
    return auc_from_scores(Xv @ w + b, y_val)


@dataclass
class LadderRung:
    k: int
    auc: float
    qualified: bool


def build_records(rows: Sequence[dict], k: int, rng: np.random.Generator,
                  text_key: str = "text") -> list[str]:
    """k=1 is the round text itself; k>1 concatenates k distinct rounds drawn
    without replacement, one record per row, so record count is held constant
    across the ladder and AUC changes reflect record *length*, not sample
    size."""
    if k == 1:
        return [r[text_key] for r in rows]
    out = []
    for _ in range(len(rows)):
        picks = rng.choice(len(rows), size=k, replace=False)
        out.append(ROUND_SEP.join(rows[j][text_key] for j in picks))
    return out


def ladder_auc(adapter: ModelAdapter, rounds: dict[str, Sequence[dict]],
               k: int, fit_ids: Iterable[str], val_ids: Iterable[str],
               seed: int = 11, task_key: str = "task_id") -> float:
    """AUC at record length k. `rounds` maps pole -> rows; label 1 = "pos"."""
    fit_ids, val_ids = set(fit_ids), set(val_ids)
    rng = np.random.default_rng(seed + k)
    X, y, half = [], [], []
    for pole, label in (("pos", 1), ("neg", 0)):
        rows = list(rounds[pole])
        for half_name, ids_set in (("fit", fit_ids), ("val", val_ids)):
            sub = [r for r in rows if r[task_key] in ids_set]
            if not sub:
                continue
            for rec in build_records(sub, k, rng):
                X.append(adapter.embed(rec))
                y.append(label)
                half.append(half_name)
    X, y, half = np.array(X), np.array(y), np.array(half)
    return logistic_auc(X[half == "fit"], y[half == "fit"],
                        X[half == "val"], y[half == "val"])


def run_ladder(adapter: ModelAdapter, rounds: dict[str, Sequence[dict]],
               fit_ids: Iterable[str], val_ids: Iterable[str],
               ks: Sequence[int] = (1, 2, 3, 4),
               bar: float = AUC_BAR) -> list[LadderRung]:
    """Ascend the record-length ladder, stopping at the first rung that
    clears `bar`. Lazy by design: a qualifying k makes longer records
    irrelevant, and running them anyway invites picking the prettiest."""
    out = []
    for k in ks:
        a = ladder_auc(adapter, rounds, k, fit_ids, val_ids)
        out.append(LadderRung(k=k, auc=a, qualified=bool(a >= bar)))
        if a >= bar:
            break
    return out


__all__ = ["AUC_BAR", "ROUND_SEP", "LadderRung", "seed_for", "auc_from_scores",
           "logistic_auc", "build_records", "ladder_auc", "run_ladder"]
