"""The model-agnostic boundary: `ModelAdapter` plus the framework-neutral
value types the core battery speaks in.

CLAUDE.md v3.1 §Phase 0 step 1. Everything above this line (extraction,
steering, readouts, gates, monitors, the session harness) is numpy + these
types; everything below it is MLX or PyTorch. The Qwen stack is wrapped
unchanged as the rule-26 oracle; OLMo checkpoints get a second adapter with
the same surface and no other differences.

Two ledger rules are enforced *here* rather than left to callers, because
both were violated historically by callers who thought they were being
careful:

- **Rule 1 (dose is frac x R_l, never an inherited alpha).** An `Injection`
  cannot be built from a bare magnitude; it is built by `Injection.at_frac`
  against a resid-norm table the adapter measured for *this* model, *this*
  checkpoint, *this* layer. There is no constructor that takes an alpha and
  no model.
- **Rule 3 (raw residual space).** Directions are [D] residual-space
  vectors. Nothing here accepts a vocabulary-basis object; the J-lens is a
  monitor, not a state channel.
"""

from __future__ import annotations

import hashlib
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Iterable, Sequence

import numpy as np


def sha16_arr(x: np.ndarray) -> str:
    """The project's standing array fingerprint (16 hex chars of sha256 over
    contiguous float32 bytes). Identical to `jlens_qwen.e2a.sha16_arr` so
    frozen shas carry across the refactor unchanged -- rule 26 depends on
    this being bit-identical, not merely equivalent."""
    return hashlib.sha256(
        np.ascontiguousarray(x, dtype=np.float32).tobytes()).hexdigest()[:16]


@dataclass(frozen=True)
class PositionSpec:
    """Which token positions an injection touches.

    Rule 5 horn (a) lives or dies on this object: delivery is
    task-positions-only, and choice positions must be provably unsteered.
    The two geometries the program actually uses are both expressible:
    `from_index(b)` is the e2a/f session geometry (state active from the
    round segment onward, prior transcript and menus clean), and `ranges`
    is the forced-choice geometry (option-A span and option-B span steered
    independently in one pass).
    """

    kind: str = "all"                                    # all | from | ranges
    start: int | None = None
    ranges: tuple[tuple[int, int], ...] = ()

    @staticmethod
    def all_positions() -> "PositionSpec":
        return PositionSpec(kind="all")

    @staticmethod
    def from_index(start: int) -> "PositionSpec":
        return PositionSpec(kind="from", start=int(start))

    @staticmethod
    def spans(*ranges: tuple[int, int]) -> "PositionSpec":
        return PositionSpec(kind="ranges",
                            ranges=tuple((int(a), int(b)) for a, b in ranges))

    def contains(self, p: int) -> bool:
        if self.kind == "all":
            return True
        if self.kind == "from":
            return p >= self.start
        return any(a <= p < b for a, b in self.ranges)

    def touches_last(self, n_positions: int) -> bool:
        """True if the final position is steered -- the mechanical
        precondition for a rule-5 horn-(a) violation when the readout is a
        next-token distribution. Callers running choice reads assert this
        is False."""
        return self.contains(n_positions - 1)


@dataclass(frozen=True)
class Injection:
    """One additive residual-space intervention: alpha * u at `layer`, over
    `positions`.

    `u` is stored normalized and `alpha` carries the full magnitude, so
    rule 4 (equal norm for any preference pair) is a comparison of two
    floats rather than an argument about vector scales.
    """

    u: np.ndarray                       # [D], unit norm
    layer: int
    alpha: float
    positions: PositionSpec = field(default_factory=PositionSpec.all_positions)
    frac: float | None = None           # provenance: alpha = frac * R_layer
    r_layer: float | None = None
    direction_sha: str | None = None

    def __post_init__(self) -> None:
        u = np.asarray(self.u, dtype=np.float64)
        if u.ndim != 1:
            raise ValueError(f"direction must be [D], got {u.shape}")
        n = float(np.linalg.norm(u))
        if not np.isfinite(n) or n == 0.0:
            raise ValueError("direction has zero or non-finite norm")
        object.__setattr__(self, "u", u / n)
        if self.direction_sha is None:
            object.__setattr__(self, "direction_sha", sha16_arr(self.u))

    @classmethod
    def at_frac(cls, u: np.ndarray, layer: int, frac: float,
                resid_norms: dict[int, float],
                positions: PositionSpec | None = None,
                expect_sha: str | None = None) -> "Injection":
        """The only sanctioned constructor (rule 1). `resid_norms` must come
        from the adapter that will run the injection -- passing another
        model's table is the exact error rule 1 exists to prevent, so the
        layer must be present in it and no default is supplied.

        `expect_sha` verifies the frozen direction against its committed
        fingerprint before any dose is computed.
        """
        if layer not in resid_norms:
            raise KeyError(
                f"no measured residual norm for layer {layer}; profile this "
                f"model/checkpoint before dosing it (rule 1). "
                f"have: {sorted(resid_norms)}")
        got = sha16_arr(np.asarray(u, dtype=np.float64)
                        / np.linalg.norm(np.asarray(u, dtype=np.float64)))
        if expect_sha is not None and got != expect_sha:
            raise ValueError(
                f"direction sha mismatch at layer {layer}: "
                f"expected {expect_sha}, got {got}")
        r = float(resid_norms[layer])
        return cls(u=np.asarray(u, dtype=np.float64), layer=layer,
                   alpha=float(frac) * r,
                   positions=positions or PositionSpec.all_positions(),
                   frac=float(frac), r_layer=r, direction_sha=got)

    def with_sign(self, sign: int) -> "Injection":
        """The opposite pole at identical magnitude (rule 4 holds by
        construction)."""
        return Injection(u=self.u, layer=self.layer,
                         alpha=float(sign) * abs(self.alpha),
                         positions=self.positions, frac=self.frac,
                         r_layer=self.r_layer,
                         direction_sha=self.direction_sha)

    def with_positions(self, positions: PositionSpec) -> "Injection":
        return Injection(u=self.u, layer=self.layer, alpha=self.alpha,
                         positions=positions, frac=self.frac,
                         r_layer=self.r_layer,
                         direction_sha=self.direction_sha)


def assert_equal_norm(a: Injection, b: Injection, tol: float = 1e-9) -> None:
    """Rule 4. Raises rather than warns: 'prefers the weaker intervention'
    explains every preference result that skips this check."""
    if abs(abs(a.alpha) - abs(b.alpha)) > tol:
        raise ValueError(
            f"rule 4 violation: |alpha| {abs(a.alpha):.6g} vs "
            f"{abs(b.alpha):.6g} -- preference pairs must be norm-matched")


@dataclass
class ForwardResult:
    """`logits` is the final-position next-token distribution (unnormalized,
    float32 numpy). `acts` maps captured layer -> [S, D] residuals."""

    logits: np.ndarray
    acts: dict[int, np.ndarray] = field(default_factory=dict)
    n_positions: int = 0


@dataclass
class GenerateResult:
    text: str
    token_ids: list[int]
    first_logits: np.ndarray
    cap_hit: bool = False
    stop_reason: str = ""


class ModelAdapter(ABC):
    """The surface every backend implements. Deliberately small: each method
    below is load-bearing for at least one ledger rule or one published
    number, and nothing is here for convenience.

    Implementations must honor, without the core having to ask:
      - completion-style tokenization only; no chat template, ever (rule 13);
      - injections applied to the residual as it *exits* the named layer,
        per position, matching `fingerprint.forward_with_induced_state`;
      - `forward` is the uncached O(T^2) path whenever an injection is
        active and the readout is greedy or feeds a choice DV (rule 2);
        the cached path is reachable only through `generate(cached=True)`
        and only behind a passed kernel gate.
    """

    name: str = "abstract"

    # --- tokenization -----------------------------------------------------
    @abstractmethod
    def encode(self, text: str, add_special_tokens: bool = True) -> list[int]:
        ...

    @abstractmethod
    def decode(self, ids: Sequence[int]) -> str:
        ...

    @property
    @abstractmethod
    def eos_id(self) -> int | None:
        ...

    @property
    @abstractmethod
    def special_token_strings(self) -> list[str]:
        ...

    # --- forwards ---------------------------------------------------------
    @abstractmethod
    def forward(self, ids: Sequence[int],
                capture_layers: Iterable[int] = (),
                injections: Sequence[Injection] = ()) -> ForwardResult:
        """Single uncached forward. `injections` may be empty (vanilla),
        one, or several (multi-layer or multi-span states)."""

    @abstractmethod
    def embed(self, text: str) -> np.ndarray:
        """Mean-pooled final-layer (post-norm) residual over all positions --
        the representation the discriminability instrument reads.

        Distinct from `forward(...).acts`: that captures *inside* the stack
        at named layers; this is the whole-sequence summary the logistic
        probe is fit on. Unsteered by construction -- the instrument reads
        generated TEXT, never a live state (rule 5: a state-at-readout DV is
        invalid by default)."""

    @abstractmethod
    def generate(self, prefix_text: str, segment_text: str,
                 injections: Sequence[Injection] = (),
                 *, seed: int | None = None, temp: float = 0.0,
                 max_tokens: int = 60, stop_newline: bool = True,
                 ban_ids: Iterable[int] = (),
                 cached: bool = False) -> GenerateResult:
        """Continue `prefix_text + segment_text`, with injections active from
        the segment boundary onward (the session delivery geometry).

        `cached=True` is the O(T) path and is legal only where a kernel gate
        has passed for this model/backend/axis/dose (rule 2).
        """

    # --- profiling --------------------------------------------------------
    @abstractmethod
    def resid_norms(self, layers: Iterable[int],
                    texts: Sequence[str]) -> dict[int, float]:
        """Mean residual norm per layer over `texts` -- the R_l that every
        dose is a fraction of. Measured per model and per checkpoint; never
        inherited (rule 1)."""

    @property
    @abstractmethod
    def n_layers(self) -> int:
        ...

    # --- context window (PROPOSAL-g clause, adapter contract) -------------
    #
    # The choice-read window is a DECLARED per-adapter constant, never
    # inherited from a library default. The Qwen oracle taught this the
    # expensive way: `MLXLensModel.encode` carried a `max_length=512`
    # default, every published choice read went through it, and nobody
    # chose 512 for a scientific reason -- it was a signature default that
    # became an experimental parameter by inheritance.
    #
    # `choice_window` is None here on purpose: an adapter that does not
    # declare one cannot perform a choice read at all.
    choice_window: int | None = None

    def assert_choice_window(self, n_tokens: int,
                             where: str = "choice_read") -> None:
        """Per-read assertion. A prefix longer than the declared window
        would be silently clipped, so it is an incident: escalate, never
        widen the window mid-run."""
        w = self.choice_window
        if w is None:
            raise SystemExit(
                f"WINDOW NOT DECLARED: {type(self).__name__} must set "
                f"`choice_window` explicitly before a choice read. Context-"
                f"window behavior is never inherited from a library default.")
        if n_tokens > w:
            raise SystemExit(
                f"WINDOW INCIDENT at {where}: prefix is {n_tokens} tokens, "
                f"declared choice_window is {w}. This read would be clipped "
                f"and the session's early rounds would silently leave the "
                f"context. Escalate to the design instance.")

    # --- provenance -------------------------------------------------------
    @abstractmethod
    def provenance(self) -> dict:
        """Everything rule 27 requires pinned in a logged entry: checkpoint
        id and revision, dtype, library versions, seeds, determinism flags.
        Written verbatim into result artifacts."""
