"""Residual capture and mean-difference axis extraction -- ported from
`scripts/e0_extract_axis.py`, the pass that produced the validated reward
axis.

Pure measurement: unsteered forwards over fixed text, capture at the
workspace layers, per-layer mean differences between condition pairs. Rule 2
is untouched by construction (no steering, no generation); rule 3 is
satisfied by staying in raw residual space -- no vocabulary basis is ever
involved.

Three things this module keeps that a casual reimplementation would lose:

1. **Span aggregation is primary, last-position is secondary.** The axis is
   a mean over the *varying* span (the frame tokens), not over the whole
   context, because the fixed prefix is identical across conditions and
   averaging it in only shrinks the contrast.
2. **R_l is the mean of per-context span-means** -- the quantity every dose
   is a fraction of (rule 1). Published R48 = 103.01 on the e0 corpus.
3. **The guard decompositions travel with the axis** (PROPOSAL-e V2/V3):
   the fraction of the reward axis orthogonal to the character axis
   (self-indexing) and to the sentiment axis (evaluative-not-affective).
   An axis extracted without them is not licensed as a drug.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Mapping, Sequence

import numpy as np

from .adapters.base import ModelAdapter, sha16_arr

EPS = 1e-12


# --- hygiene (rule 18) ---------------------------------------------------
def assert_disjoint(corpus_texts: Sequence[str],
                    pools: Mapping[str, Sequence[str]],
                    label: str = "corpus") -> None:
    """Rule 18, both directions of containment, exact-string.

    Raises rather than warns, and runs at startup rather than at analysis:
    an extraction corpus that overlaps a probe battery invalidates the
    readout, and discovering that afterwards costs a cycle.
    """
    for text in corpus_texts:
        t = text.strip()
        if not t:
            continue
        for name, pool in pools.items():
            for p in pool:
                if t in p or p in t:
                    raise SystemExit(
                        f"HYGIENE FAIL (rule 18): {label} overlaps {name}: "
                        f"{p[:60]!r}")


# --- contexts ------------------------------------------------------------
@dataclass(frozen=True)
class Context:
    """One extraction context. `prefix` is the invariant part; `full` is
    prefix + the condition-varying continuation. The span is everything
    after the token boundary between them."""

    prefix: str
    full: str
    condition: str
    item_id: str = ""
    variant: int = 0


def span_start(adapter: ModelAdapter, prefix: str, full: str) -> int:
    """First token index where `full` diverges from `prefix` -- computed on
    token ids, not characters, so a BPE merge across the boundary cannot
    silently shift the span."""
    a = adapter.encode(prefix)
    b = adapter.encode(full)
    k = 0
    while k < len(a) and k < len(b) and a[k] == b[k]:
        k += 1
    return k


@dataclass
class CaptureResult:
    span: np.ndarray                 # [n_ctx, n_layers, D]
    last: np.ndarray                 # [n_ctx, n_layers, D]
    conditions: np.ndarray           # [n_ctx] of str
    item_ids: np.ndarray
    layers: tuple[int, ...]
    resid_norms: dict[int, float]    # R_l, mean of per-context span-means
    span_lens: tuple[int, ...] = ()

    def r_table(self) -> dict[int, float]:
        return dict(self.resid_norms)


def capture(adapter: ModelAdapter, contexts: Sequence[Context],
            layers: Iterable[int], progress_every: int = 50) -> CaptureResult:
    """One unsteered forward per context; span-mean and final-position
    residuals at each layer, plus the R_l table."""
    layers = tuple(int(l) for l in layers)
    span_rows, last_rows, span_norms, span_lens = [], [], {l: [] for l in layers}, []
    conds, items = [], []

    for n, ctx in enumerate(contexts, start=1):
        k = span_start(adapter, ctx.prefix, ctx.full)
        ids = adapter.encode(ctx.full)
        S = len(ids)
        if not 0 < k < S:
            raise ValueError(
                f"degenerate span for {ctx.item_id}/{ctx.condition}: "
                f"boundary {k} of {S} tokens")
        res = adapter.forward(ids, capture_layers=layers)
        per_span, per_last = [], []
        for l in layers:
            h = res.acts[l].astype(np.float64)        # [S, D]
            sp = h[k:, :]
            per_span.append(sp.mean(axis=0))
            per_last.append(h[S - 1, :])
            span_norms[l].append(float(np.linalg.norm(sp, axis=1).mean()))
        span_rows.append(np.stack(per_span))
        last_rows.append(np.stack(per_last))
        conds.append(ctx.condition)
        items.append(ctx.item_id)
        span_lens.append(S - k)
        if progress_every and n % progress_every == 0:
            print(f"  {n}/{len(contexts)} contexts", flush=True)

    return CaptureResult(
        span=np.stack(span_rows), last=np.stack(last_rows),
        conditions=np.array(conds), item_ids=np.array(items),
        layers=layers,
        resid_norms={l: float(np.mean(span_norms[l])) for l in layers},
        span_lens=tuple(span_lens))


def resid_norm_table(adapter: ModelAdapter, contexts: Sequence[Context],
                     layers: Iterable[int]) -> dict[int, float]:
    """R_l over an extraction corpus, span-restricted. The canonical dose
    denominator (rule 1); profile this per model and per checkpoint."""
    return capture(adapter, contexts, layers, progress_every=0).resid_norms


# --- axes ----------------------------------------------------------------
def mean_diff_axis(cap: CaptureResult, pos_condition: str, neg_condition: str,
                   variant: str = "span") -> np.ndarray:
    """[n_layers, D] mean(pos) - mean(neg). The axis, before normalization:
    callers that need a direction normalize; callers that need the raw
    contrast magnitude do not."""
    arr = cap.span if variant == "span" else cap.last
    p = arr[cap.conditions == pos_condition]
    n = arr[cap.conditions == neg_condition]
    if not len(p) or not len(n):
        raise ValueError(
            f"empty condition group: {pos_condition}={len(p)}, "
            f"{neg_condition}={len(n)}")
    return p.mean(axis=0) - n.mean(axis=0)


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) /
                 (np.linalg.norm(a) * np.linalg.norm(b) + EPS))


def residual_fraction(axis: np.ndarray, guard: np.ndarray) -> float:
    """Fraction of `axis` orthogonal to `guard`.

    PROPOSAL-e's V2 (self-indexing: guard = character axis) and V3
    (evaluative-not-affective: guard = sentiment axis). High is good: it is
    the share of the drug that the confound does not explain.
    """
    g = guard / (np.linalg.norm(guard) + EPS)
    res = axis - np.dot(axis, g) * g
    return float(np.linalg.norm(res) / (np.linalg.norm(axis) + EPS))


@dataclass
class AxisReport:
    layer: int
    r_layer: float
    norms: dict[str, float]
    cosines: dict[str, float]
    guards: dict[str, float]
    axis_over_r: float

    def as_dict(self) -> dict:
        return {"layer": self.layer, "R_layer": round(self.r_layer, 2),
                **{f"norm_{k}": round(v, 3) for k, v in self.norms.items()},
                "axis_over_R": round(self.axis_over_r, 4),
                **{f"cos_{k}": round(v, 3) for k, v in self.cosines.items()},
                **{f"{k}_residual_frac": round(v, 3)
                   for k, v in self.guards.items()}}


def axis_report(cap: CaptureResult, axes: Mapping[str, np.ndarray],
                primary: str, guards: Mapping[str, str]) -> list[AxisReport]:
    """Per-layer geometry for a primary axis and its guards.

    `axes` maps name -> [n_layers, D]; `guards` maps guard-name ->
    axis-name (e.g. {"v2_self": "character", "v3_eval": "sentiment"}).
    """
    out = []
    for li, layer in enumerate(cap.layers):
        prim = axes[primary][li]
        r = cap.resid_norms[layer]
        out.append(AxisReport(
            layer=layer, r_layer=r,
            norms={k: float(np.linalg.norm(v[li])) for k, v in axes.items()},
            cosines={k: cosine(prim, v[li])
                     for k, v in axes.items() if k != primary},
            guards={gname: residual_fraction(prim, axes[aname][li])
                    for gname, aname in guards.items()},
            axis_over_r=float(np.linalg.norm(prim)) / (r + EPS)))
    return out


def freeze_sha(axes: Mapping[str, np.ndarray], order: Sequence[str]) -> str:
    """The frozen fingerprint over a stacked axis family, in the declared
    order. Rule 1: this is what later runs sha-verify against, so `order` is
    part of the freeze and must not be reshuffled."""
    return sha16_arr(np.stack([axes[a] for a in order]))


__all__ = ["Context", "CaptureResult", "AxisReport", "assert_disjoint",
           "span_start", "capture", "resid_norm_table", "mean_diff_axis",
           "cosine", "residual_fraction", "axis_report", "freeze_sha"]
