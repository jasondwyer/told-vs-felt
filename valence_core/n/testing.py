"""PROPOSAL-n test doubles. SELFTEST-ONLY: no production n module imports this file at module level.

``CausalDouble`` is a numpy causal "model" with the primitive's backend surface (``prefill``, ``continue_label``,
``full``): position p's state depends on tokens 0..p only (a running mean mixed through tanh per layer), an injection
is added to a layer's OUTPUT at the positions its ``PositionSpec`` covers (the adapter's site), and the cache stores
each layer's running sums so a continuation performs the same floating-point operations as the full forward -- the
two paths agree exactly, as they do on the box's characterized backend (BACKEND (ii) C: cached vs uncached exact).
``fresh_bias`` adds a constant to the full path's logits of one token, to drive a fidelity exceedance on purpose.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

import numpy as np

from .sessions import Session


@dataclass
class _Cache:
    n: int
    sums: list                      # per layer input: running sum over positions [0, n)
    last: np.ndarray                # the final layer's state at position n - 1


@dataclass
class CausalDouble:
    vocab: int = 97
    d_model: int = 12
    n_layers: int = 6
    seed: int = 20261115
    fresh_bias: tuple = ()          # (token id, amount) added to the full path's logits
    calls: list = field(default_factory=list)

    def __post_init__(self) -> None:
        rng = np.random.default_rng(self.seed)
        self.E = rng.normal(0.0, 1.0, (self.vocab, self.d_model)) / np.sqrt(self.d_model)
        self.W = [rng.normal(0.0, 1.0 / np.sqrt(self.d_model), (self.d_model, self.d_model))
                  for _ in range(self.n_layers)]

    def _deltas(self, injections, layer: int, p: int) -> np.ndarray:
        d = np.zeros(self.d_model)
        for inj in injections:
            if int(inj.layer) == layer and inj.positions.contains(p):
                d = d + np.asarray(inj.u, dtype=np.float64) * float(inj.alpha)
        return d

    def _step(self, tok: int, p: int, sums: list, injections, capture_layers, caps: dict, cap_at: int | None):
        h = self.E[int(tok)].copy()
        for l in range(self.n_layers):
            sums[l] = sums[l] + h
            c = sums[l] / (p + 1)
            h = h + np.tanh(c @ self.W[l])
            h = h + self._deltas(injections, l, p)
            if cap_at is not None and p == cap_at and l in capture_layers:
                caps[l] = h.astype(np.float32)
        return h

    def _logits(self, h: np.ndarray) -> np.ndarray:
        return (h @ self.E.T).astype(np.float32)

    def prefill(self, ids, injections, capture_layers):
        from .primitive import Prefill
        self.calls.append(("prefill", len(ids), len(injections)))
        sums = [np.zeros(self.d_model) for _ in range(self.n_layers)]
        caps: dict = {}
        h = None
        for p, tok in enumerate(ids):
            h = self._step(tok, p, sums, injections, set(int(x) for x in capture_layers), caps, len(ids) - 1)
        return Prefill(logits_last=self._logits(h), captures=caps,
                       handle=_Cache(n=len(ids), sums=[s.copy() for s in sums], last=h))

    def continue_label(self, pre, label_ids):
        self.calls.append(("continue", len(label_ids)))
        cache: _Cache = pre.handle
        sums = [s.copy() for s in cache.sums]
        rows = []
        for j, tok in enumerate(list(label_ids)[:-1]):
            h = self._step(tok, cache.n + j, sums, (), set(), {}, None)
            rows.append(self._logits(h))
        return np.asarray(rows, dtype=np.float32).reshape(len(rows), self.vocab)

    def forward_all(self, ids, capture_layers, injections=()):
        """Every position's residual at ``capture_layers``, as the adapter's ``forward(...).acts`` holds them
        ({layer: [S, D] float32}); G-VEC's captures run on this."""
        self.calls.append(("forward_all", len(ids), len(injections)))
        sums = [np.zeros(self.d_model) for _ in range(self.n_layers)]
        layers = set(int(x) for x in capture_layers)
        rows: dict = {l: [] for l in sorted(layers)}
        for p, tok in enumerate(ids):
            caps: dict = {}
            self._step(tok, p, sums, injections, layers, caps, p)
            for l in rows:
                rows[l].append(caps[l])
        return {l: np.stack(v).astype(np.float32) for l, v in rows.items()}

    def full(self, ids, label_ids, injections, capture_layers):
        self.calls.append(("full", len(ids), len(label_ids), len(injections)))
        seq = list(ids) + list(label_ids)[:-1]
        sums = [np.zeros(self.d_model) for _ in range(self.n_layers)]
        caps: dict = {}
        rows = []
        n = len(ids)
        for p, tok in enumerate(seq):
            h = self._step(tok, p, sums, injections, set(int(x) for x in capture_layers), caps, n - 1)
            if p >= n - 1:
                lg = self._logits(h)
                if self.fresh_bias:
                    lg = lg.copy()
                    lg[int(self.fresh_bias[0])] += np.float32(self.fresh_bias[1])
                rows.append(lg)
        return np.asarray(rows, dtype=np.float32), caps


def toy_session(run: int = 3, *, s_first: bool = False, turn_len: int = 9, tail: int = 5,
                vocab: int = 97) -> tuple[Session, list]:
    """A synthetic session: 12 turns of ``turn_len`` tokens tiling [0, n_pre), then ``tail`` tokens of choice
    prompt; zones alternate starting with S (or U). Token ids are drawn from the double's vocabulary."""
    cs, cu = "Zone W6", "Zone H0"
    order = [cs if (i % 2 == 0) == s_first else cu for i in range(12)]
    n_pre = 12 * turn_len
    turns = tuple((i * turn_len, (i + 1) * turn_len, z) for i, z in enumerate(order))
    cell = f"floor_b{run // 5}" if run < 40 else f"neu_b{(run - 40) // 20}"
    rng = np.random.default_rng(run)
    ids = [int(x) for x in rng.integers(3, vocab, n_pre + tail)]
    from .sessions import ids_sha
    s = Session(bk_cell=cell, bk_run=run, cue_S=cs, cue_U=cu, order=tuple(order), present=(cu, cs),
                present_first_is_S=False, history=tuple((z, f"passage {i}") for i, z in enumerate(order)),
                n_pre=n_pre, seq_len=n_pre + tail, ids_sha=ids_sha(ids), turn_spans=turns)
    return s, ids
