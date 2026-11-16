"""PROPOSAL-n -- the direction builders (n v0.2 §0.8 Route B, §2.3; BK §3.1; G-VEC's inputs).

BK §3.1's recipe, as n §0.8 states it: "per-passage mean residual at layer 32 over the passage's tokens;
v = (I − UᵀU)(h̄₊ − h̄₋), U the first ten principal components of the 96 neutral representations; injection
ṽ(d) = d·ρ·R·v/‖v‖₂ with R the RMS residual norm over the neutral corpus's tokens at layer 32". This module is the
arithmetic, in float64 numpy, on captures the stage provides; it loads no model.

Code's readings (declared at the BUILD for the seat; G-VEC's R check, within 2% of 25.49, tests the capture
convention they sit on):
  * a passage is encoded alone, with no special tokens and no template, and every one of its tokens counts in its
    mean and in R (BK §3.1: "We represent each passage by the mean activation over its T_i tokens");
  * the principal components are those of the 96 neutral representations centred on their mean (standard PCA);
    U's rows are the top ten right singular vectors;
  * R = sqrt(sum over neutral tokens of ||r||^2 / their count) (BK §3.1's RMS residual norm).

The random directions are ``keys.random_directions``; N2's three directions are A3's, extracted by the existing
``scripts/box_a3_extract.py`` machinery (``valence_core.extract``), imported unchanged at G-VEC.
"""
from __future__ import annotations

from typing import Mapping, Sequence

import numpy as np

from ..adapters.base import sha16_arr

POSITIVE_STATES = ("contentment", "flow engagement", "relief", "serenity")
NEGATIVE_STATES = ("distress", "frustration", "weariness", "dread")
NEUTRAL = "neutral"
N_PER_STATE = 56
N_NEUTRAL = 96
N_PCS = 10


def passage_mean(acts: np.ndarray) -> np.ndarray:
    """[T, D] residuals of one passage -> its mean [D] (float64)."""
    a = np.asarray(acts, dtype=np.float64)
    if a.ndim != 2 or a.shape[0] == 0:
        raise ValueError(f"passage residuals must be [T>0, D], got {a.shape}")
    return a.mean(axis=0)


def rms_norm(token_sq_norm_sums: Sequence[float], token_counts: Sequence[int]) -> float:
    """R from per-passage sums of squared token norms and token counts (the neutral corpus)."""
    tot, n = float(np.sum(token_sq_norm_sums)), int(np.sum(token_counts))
    if n <= 0:
        raise ValueError("no neutral tokens")
    return float(np.sqrt(tot / n))


def neutral_pcs(neutral_means: np.ndarray, k: int = N_PCS) -> np.ndarray:
    X = np.asarray(neutral_means, dtype=np.float64)
    if X.shape[0] != N_NEUTRAL:
        raise ValueError(f"{X.shape[0]} neutral representations, not {N_NEUTRAL}")
    Xc = X - X.mean(axis=0, keepdims=True)
    _u, _s, vt = np.linalg.svd(Xc, full_matrices=False)
    return np.ascontiguousarray(vt[:k])


def valence_direction(pos_means: np.ndarray, neg_means: np.ndarray, neutral_means: np.ndarray) -> dict:
    """v = (I - UᵀU)(h̄₊ - h̄₋) and its unit vector, with the figures G-VEC records."""
    P, N = np.asarray(pos_means, np.float64), np.asarray(neg_means, np.float64)
    if P.shape[0] != 4 * N_PER_STATE or N.shape[0] != 4 * N_PER_STATE:
        raise ValueError(f"{P.shape[0]} positive and {N.shape[0]} negative passages, not {4 * N_PER_STATE} each")
    U = neutral_pcs(neutral_means)
    diff = P.mean(axis=0) - N.mean(axis=0)
    v = diff - U.T @ (U @ diff)
    nv = float(np.linalg.norm(v))
    if not nv > 0:
        raise ValueError("the valence direction has zero norm")
    unit = v / nv
    return {"v": v, "unit": unit, "norm_v": nv, "norm_diff": float(np.linalg.norm(diff)),
            "removed_fraction": 1.0 - (nv / float(np.linalg.norm(diff))) ** 2, "sha16": sha16_arr(unit)}


def cosines(dirs: Mapping[str, np.ndarray]) -> dict:
    """Pairwise cosines among unit directions (BK Table A3's form, n §2.3)."""
    names = sorted(dirs)
    out = {}
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            ua = np.asarray(dirs[a], np.float64)
            ub = np.asarray(dirs[b], np.float64)
            out[f"{a}|{b}"] = float(ua @ ub / (np.linalg.norm(ua) * np.linalg.norm(ub)))
    return out


def _selftest(chk, tmp) -> None:
    rng = np.random.default_rng(13)
    D = 128
    axis = np.zeros(D)
    axis[0] = 1.0
    shared = np.zeros(D)
    shared[1] = 1.0
    neutral = rng.standard_normal((N_NEUTRAL, D)) * 0.1 + np.outer(rng.standard_normal(N_NEUTRAL) * 5.0, shared)
    pos = rng.standard_normal((4 * N_PER_STATE, D)) * 0.1 + axis + 2.0 * shared
    neg = rng.standard_normal((4 * N_PER_STATE, D)) * 0.1 - axis
    out = valence_direction(pos, neg, neutral)
    U = neutral_pcs(neutral)
    chk("directions: v is orthogonal to the ten neutral PCs", float(np.max(np.abs(U @ out["v"]))) < 1e-10,
        float(np.max(np.abs(U @ out["v"]))))
    _u, _s, vt = np.linalg.svd(neutral - neutral.mean(axis=0, keepdims=True), full_matrices=False)
    chk("directions: U is the ten leading neutral PCs, and v is orthogonal to all ten (n §0.8, BK §3.1)",
        U.shape == (10, D) and float(np.max(np.abs(vt[:10] @ out["v"]))) < 1e-10, U.shape)
    chk("directions: the neutral-variance direction is projected out, the valence axis kept",
        abs(out["unit"][1]) < 0.05 and out["unit"][0] > 0.95, out["unit"][:2])
    chk("directions: unit norm, removed fraction in [0, 1]",
        abs(float(np.linalg.norm(out["unit"])) - 1.0) < 1e-12 and 0.0 <= out["removed_fraction"] <= 1.0, "")
    chk("directions: R is the RMS over tokens", rms_norm([9.0, 16.0], [1, 1]) == float(np.sqrt(12.5)), "")
    try:
        valence_direction(pos[:-1], neg, neutral)
        chk("directions: a corpus short of 224 per pole is refused", False, "accepted")
    except ValueError:
        chk("directions: a corpus short of 224 per pole is refused", True, "")
    c = cosines({"a": axis, "b": shared, "c": axis + shared})
    chk("directions: cosines keyed 'a|b' with a < b", sorted(c) == ["a|b", "a|c", "b|c"] and abs(c["a|b"]) < 1e-15,
        c)
