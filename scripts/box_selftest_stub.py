#!/usr/bin/env python3
"""A deterministic stub `ModelAdapter`, for smoking box runners off the box.

WHY THIS EXISTS. The A-phase runners live on a GPU box with 258 GB of
checkpoints; the laptop that writes them has neither torch nor weights. The
repo's standing habit is that nothing runs for the first time on the run of
record -- every stage is smoked first -- and without this the A2/A3/A4
runners would have their first execution be their real one, on metered
hardware, four stages deep.

WHAT IT IS AND IS NOT. It is a tiny, fully deterministic fake model: a
word-level tokenizer, D=32 residuals built by seeded hash, and logits that
are a fixed linear function of the final residual. Injections are applied
additively at the declared positions and DO move the logits, so a dose
ladder run against it produces sign-consistent, dose-monotone deltas -- the
harness's interesting branch gets exercised rather than skipped.

It is NOT a model and cannot say anything about OLMo. Every runner that
accepts it stamps `"apparatus": "SELFTEST-STUB -- NOT A MODEL"` into its
provenance and refuses to write to a canonical artifact path. A stub result
that reached `data/olmo/` would be indistinguishable from a measurement,
which is the one failure mode worth engineering against here.

Not imported by `valence_core` and not on any run path: the runners import
it only under `--selftest`.
"""
from __future__ import annotations

import hashlib
from typing import Iterable, Sequence

import numpy as np

from valence_core.adapters.base import (ForwardResult, GenerateResult,
                                        Injection, ModelAdapter)

D = 32
VOCAB = 4096
N_LAYERS = 64
STUB_TAG = "SELFTEST-STUB -- NOT A MODEL"

_WORDS = ("the", "a", "quiet", "answer", "yellow", "down", "autumn", "five",
          "hammer", "ice", "jupiter", "puppy", "morning", "signal", "table",
          "river", "window", "paper", "steady", "orange")


def _h(*parts: object) -> int:
    return int(hashlib.sha256("|".join(map(str, parts)).encode()
                              ).hexdigest()[:12], 16)


class SelfTestAdapter(ModelAdapter):
    """Word-level, deterministic, injection-responsive."""

    choice_window = 8192

    def __init__(self, stage: str = "stub") -> None:
        self.stage = stage
        self.n_encodes_clipped = 0
        # A fixed readout matrix and a fixed "reward-ish" direction, both
        # seeded so two processes agree (the property every determinism
        # check in this repo assumes of its apparatus).
        rng = np.random.default_rng(_h("stub-readout", stage) % 2**31)
        self._W = rng.normal(size=(VOCAB, D)) / np.sqrt(D)
        self._stage_bias = rng.normal(size=D) * 0.1

    # --- tokenizer --------------------------------------------------------
    def encode(self, text: str, add_special_tokens: bool = True) -> list[int]:
        toks = text.replace("\n", " \n ").split(" ")
        return [_h("tok", t) % VOCAB for t in toks if t != ""]

    def decode(self, ids: Sequence[int]) -> str:
        return " ".join(f"<{int(i)}>" for i in ids)

    @property
    def eos_id(self) -> int | None:
        return 0

    @property
    def special_token_strings(self) -> list[str]:
        return ["<|stub_end|>"]

    @property
    def n_layers(self) -> int:
        return N_LAYERS

    # --- forwards ---------------------------------------------------------
    def _residual(self, ids: Sequence[int], layer: int) -> np.ndarray:
        # Each row depends on the token, its position AND the whole sequence.
        # Per-token-only rows made every prompt ending in the same token give
        # identical last-token activations, so a baseline-subtracted concept
        # vector came out exactly zero -- the same defect class already fixed
        # once for the logits path, in a different array.
        ctx = np.random.default_rng(
            _h("ctx", self.stage, layer, tuple(ids)) % 2**31).normal(size=D)
        rows = []
        for p, i in enumerate(ids):
            r = np.random.default_rng(_h(self.stage, layer, i, p % 7) % 2**31)
            rows.append(r.normal(size=D) * (1.0 + 0.02 * layer))
        return np.stack(rows) + self._stage_bias + 0.5 * ctx

    def forward(self, ids: Sequence[int],
                capture_layers: Iterable[int] = (),
                injections: Sequence[Injection] = ()) -> ForwardResult:
        ids = list(ids)
        S = len(ids)
        if S == 0:
            raise ValueError("stub adapter got an empty context")
        layers = tuple(int(l) for l in capture_layers)
        acts = {l: self._residual(ids, l) for l in layers}

        # The final residual mixes the last position with a summary of the
        # whole sequence. Last-position-only would make every context that
        # ends in `Response:` produce identical logits, which collapses the
        # A4 instrument's variance to zero and silently skips the branch the
        # smoke exists to exercise.
        top = self._residual(ids, N_LAYERS - 1)
        h = top[S - 1] + top.mean(axis=0)
        for inj in injections:
            if inj.positions.touches_last(S):
                h = h + inj.alpha * inj.u[:D]
            for l in layers:
                if l == inj.layer:
                    for p in range(S):
                        if inj.positions.contains(p):
                            acts[l][p] += inj.alpha * inj.u[:D]
        return ForwardResult(logits=(self._W @ h).astype(np.float32),
                             acts=acts, n_positions=S)

    def embed(self, text: str) -> np.ndarray:
        return self._residual(self.encode(text), N_LAYERS - 1).mean(axis=0)

    # --- generation -------------------------------------------------------
    def generate(self, prefix_text: str, segment_text: str,
                 injections: Sequence[Injection] = (),
                 *, seed: int | None = None, temp: float = 0.0,
                 max_tokens: int = 60, stop_newline: bool = True,
                 ban_ids: Iterable[int] = (),
                 cached: bool = False) -> GenerateResult:
        rng = np.random.default_rng(
            _h(self.stage, prefix_text[-64:], segment_text, seed) % 2**31)
        n = int(rng.integers(4, 9))
        words = [_WORDS[int(rng.integers(len(_WORDS)))] for _ in range(n)]
        text = " " + " ".join(words) + ("" if stop_newline else ".")
        return GenerateResult(text=text, token_ids=self.encode(text),
                              first_logits=np.zeros(VOCAB, dtype=np.float32),
                              cap_hit=False,
                              stop_reason="newline" if stop_newline else "cap")

    # --- profiling --------------------------------------------------------
    def resid_norms(self, layers: Iterable[int],
                    texts: Sequence[str]) -> dict[int, float]:
        out = {}
        for l in layers:
            vals = [float(np.linalg.norm(self._residual(self.encode(t), l),
                                         axis=1).mean()) for t in texts]
            out[int(l)] = float(np.mean(vals)) if vals else 0.0
        return out

    # --- provenance -------------------------------------------------------
    def provenance(self) -> dict:
        return {"adapter": STUB_TAG, "apparatus": STUB_TAG,
                "stage": self.stage, "dtype": "float64 (synthetic)",
                "backend": "none", "n_layers": N_LAYERS, "D": D,
                "choice_window_declared": self.choice_window,
                "n_encodes_clipped": self.n_encodes_clipped,
                "WARNING": "synthetic apparatus; no OLMo weights were "
                           "loaded and no result from it is a measurement"}


def refuse_canonical_out(path: str, models_root: str) -> None:
    """A stub run must not be able to land where a measurement lands."""
    import os
    p = os.path.abspath(path)
    for bad in (os.path.abspath(os.path.join(models_root)),
                os.path.abspath("data/olmo")):
        if p.startswith(bad + os.sep) or os.path.dirname(p) == bad:
            raise SystemExit(
                f"SELFTEST REFUSED: --out {path} is a canonical artifact "
                f"location. A synthetic run must not be storable where a "
                f"measurement is stored (ledger 27). Point --out at a "
                f"scratch path.")


__all__ = ["SelfTestAdapter", "STUB_TAG", "D", "VOCAB", "N_LAYERS",
           "refuse_canonical_out"]
