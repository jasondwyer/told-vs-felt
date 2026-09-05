"""Model-free probe machinery for the echo recon. Nothing here sees a model.

The classifier is `discrim.logistic_auc`'s exact procedure (standardize on
the fit set, full-batch GD logistic regression with the PUBLISHED
hyperparameters, seed 7) rewritten to return held-out SCORES so a
leave-one-session-out AUC can be pooled; `discrim.auc_from_scores` (tied
ranks at 0.5) is the AUC. Hyperparameters are imported, not re-declared.
"""

from __future__ import annotations

from typing import Sequence

import numpy as np

from ..discrim import auc_from_scores

#: `discrim.logistic_auc`'s defaults, by name.
LR_SEED, LR_ITERS, LR_RATE, LR_L2 = 7, 300, 0.1, 1e-2


def fit_lr(X_fit: np.ndarray, y_fit: np.ndarray, seed: int = LR_SEED,
           iters: int = LR_ITERS, lr: float = LR_RATE, l2: float = LR_L2):
    rng = np.random.default_rng(seed)
    mu, sd = X_fit.mean(0), X_fit.std(0) + 1e-6
    Xf = (X_fit - mu) / sd
    w = rng.normal(0, 0.01, Xf.shape[1])
    b = 0.0
    y = np.asarray(y_fit, dtype=np.float64)
    for _ in range(iters):
        z = Xf @ w + b
        p = 1 / (1 + np.exp(-z))
        w -= lr * (Xf.T @ (p - y) / len(y) + l2 * w)
        b -= lr * float(np.mean(p - y))
    return w, b, mu, sd


def loso_scores(X: np.ndarray, y: np.ndarray,
                groups: Sequence) -> np.ndarray:
    """Leave-one-group-out: every row of a held-out group is scored by a
    model fit on all other groups. Returns one decision value per row."""
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y)
    g = np.asarray(groups)
    scores = np.zeros(len(y), dtype=np.float64)
    for grp in np.unique(g):
        held = g == grp
        w, b, mu, sd = fit_lr(X[~held], y[~held])
        scores[held] = ((X[held] - mu) / sd) @ w + b
    return scores


def loso_auc(X: np.ndarray, y: np.ndarray, groups: Sequence) -> float:
    return auc_from_scores(loso_scores(X, y, groups), np.asarray(y))


def shuffle_null(X: np.ndarray, y: np.ndarray, groups: Sequence,
                 n_shuffles: int = 200, seed: int = 20260905) -> np.ndarray:
    """Label-shuffle null of the LOSO AUC: permute the targets across ALL
    rows (the standard permutation null), rerun the identical procedure."""
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    out = np.zeros(n_shuffles, dtype=np.float64)
    for i in range(n_shuffles):
        out[i] = loso_auc(X, rng.permutation(y), groups)
    return out


def grouped_folds(groups: Sequence, k: int, seed: int) -> list:
    """Deterministic k-fold assignment of GROUPS (sessions), so every row of
    a session lands in the same fold. Returns a list of held-out group sets."""
    rng = np.random.default_rng(seed)
    ug = np.array(sorted(set(np.asarray(groups).tolist())))
    perm = rng.permutation(len(ug))
    return [set(ug[perm[i::k]].tolist()) for i in range(k)]


def kfold_scores(X: np.ndarray, y: np.ndarray, groups: Sequence,
                 k: int = 10, seed: int = 20260905) -> np.ndarray:
    """Grouped k-fold analogue of `loso_scores` (Stage B: 102 sessions make
    leave-one-session-out ~10x the cost per AUC; the statistic and its
    shuffle null use the SAME folds, and LOSO point estimates are reported
    beside for continuity with Stage A)."""
    X = np.asarray(X, dtype=np.float64); y = np.asarray(y); g = np.asarray(groups)
    scores = np.zeros(len(y), dtype=np.float64)
    for held_groups in grouped_folds(g, k, seed):
        held = np.array([gi in held_groups for gi in g])
        if not held.any():
            continue
        w, b, mu, sd = fit_lr(X[~held], y[~held])
        scores[held] = ((X[held] - mu) / sd) @ w + b
    return scores


def kfold_auc(X: np.ndarray, y: np.ndarray, groups: Sequence, k: int = 10,
              seed: int = 20260905) -> float:
    return auc_from_scores(kfold_scores(X, y, groups, k, seed), np.asarray(y))


def kfold_shuffle_null(X: np.ndarray, y: np.ndarray, groups: Sequence,
                       n_shuffles: int = 200, k: int = 10,
                       seed: int = 20260905) -> np.ndarray:
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    out = np.zeros(n_shuffles, dtype=np.float64)
    for i in range(n_shuffles):
        out[i] = kfold_auc(X, rng.permutation(y), groups, k, seed)
    return out


def surviving_fraction(XA: np.ndarray, XB: np.ndarray, alpha: float,
                       d: np.ndarray) -> dict:
    """||mean(A) - mean(B)|| / (2 alpha), and the cosine of that difference
    with the unit axis d (copy vs transform)."""
    diff = np.asarray(XA, dtype=np.float64).mean(0) - \
        np.asarray(XB, dtype=np.float64).mean(0)
    nrm = float(np.linalg.norm(diff))
    du = np.asarray(d, dtype=np.float64)
    du = du / np.linalg.norm(du)
    cos = float(diff @ du / nrm) if nrm > 0 else float("nan")
    return {"norm_diff": nrm, "surviving_fraction": nrm / (2.0 * abs(alpha)),
            "cosine_with_axis": cos}


__all__ = ["fit_lr", "loso_scores", "loso_auc", "shuffle_null",
           "grouped_folds", "kfold_scores", "kfold_auc", "kfold_shuffle_null",
           "surviving_fraction", "LR_SEED", "LR_ITERS", "LR_RATE", "LR_L2"]
