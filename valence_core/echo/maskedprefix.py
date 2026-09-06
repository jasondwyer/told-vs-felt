"""THE ECHO PRIMITIVE -- quarantined on the rule 5(e) pattern. RECON ONLY.

`read_choice_maskedprefix` takes a choice read with a state that was live
EARLIER in the same forward -- on declared round-task spans -- and provably
NOT at the read position: rounds steered, choice position unsteered,
in-forward memory (KV cache + Gated-DeltaNet recurrent state) retained. It
is the apparatus of the "echo cell" candidate (RECON BLOCK 2026-09-05
§3.0). No verdict quantity is computed from it anywhere; that requires a
committed pre-registration (LOCK-k) and a 5(f) clause, neither of which
exists.

Enforced in code, after `valence_core.e2b.statepresent` (the B3 pattern):

  * IMPORT GUARD -- importable only from inside `valence_core/echo/` or a
    `scripts/recon_echo*.py` runner. Not a security boundary; a loud,
    dated refusal of the accident it is meant to stop.
  * `valence_core.e2b.statepresent` is asserted ABSENT from `sys.modules`
    at import and again before every read -- the two quarantined
    primitives never coexist in one process.
  * PAIRED SHADOW, MANDATORY -- every call runs the mask-off forward over
    the identical token ids and returns a pair or nothing.
  * MASK BUILT HERE from the declared spans, so every position outside them
    is unsteered by construction; the read position (the last token) is
    asserted unsteered before any forward, and every injection's
    `PositionSpec` is asserted not to touch it.
  * BOTH FORWARDS UNCACHED (`adapter.forward_last`: the validated vanilla
    path with no injection, the positional re-forward with one).

`readout.choice_read` is not touched. The shadow is ALSO taken through it,
with `verify=True`, so the identity check against the archived vanilla read
is the same instrument that produced e2a's numbers, not a reimplementation.
"""

from __future__ import annotations

import hashlib
import inspect
import os
import sys
from dataclasses import dataclass, field
from typing import Iterable, Mapping, Sequence

import numpy as np

_PKG_DIR = os.path.dirname(os.path.abspath(__file__))
_THIS_FILE = os.path.abspath(__file__)

#: The other quarantined primitive. Never loaded in the same process.
FORBIDDEN_MODULES = ("valence_core.e2b.statepresent",)


def _importer_is_sanctioned() -> bool:
    for frame in inspect.stack():
        path = os.path.abspath(frame.filename or "")
        if path == _THIS_FILE:
            continue
        if "importlib" in path or path.startswith("<frozen"):
            continue
        if frame.filename.startswith("<") and "importlib" in (
                frame.function or ""):
            continue
        if path.startswith(_PKG_DIR + os.sep):
            return True
        base = os.path.basename(path)
        return base.startswith("recon_echo") and base.endswith(".py")
    return False


if not _importer_is_sanctioned():
    raise ImportError(
        "valence_core.echo.maskedprefix is quarantined (RECON BLOCK "
        "2026-09-05 §3.0, on the CLAUDE.md rule 5(e) pattern). It may be "
        "imported only from inside the echo package or a "
        "scripts/recon_echo*.py runner. A choice read is readout.choice_read; "
        "a state-present read is not licensed outside a committed "
        "pre-registration -- escalate to the design instance rather than "
        "widening this guard.")


def assert_statepresent_absent() -> None:
    hits = [m for m in FORBIDDEN_MODULES if m in sys.modules]
    if hits:
        raise AssertionError(
            f"quarantine collision: {hits} loaded in the same process as "
            f"the echo primitive")


assert_statepresent_absent()

from ..adapters.base import (Injection, LastForwardResult,   # noqa: E402
                             ModelAdapter, PositionSpec, sha16_arr)
from ..readout import EPS, ChoiceRead, choice_read, softmax   # noqa: E402


def prefix_sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def mask_sha(mask: np.ndarray) -> str:
    return hashlib.sha256(
        np.ascontiguousarray(mask, dtype=np.int8).tobytes()).hexdigest()[:16]


@dataclass
class MaskedPrefixRead:
    """One forward's view at the read position. Restricted two-label
    quantities (the e2a read) plus the raw label logits and log-probs, plus
    the residual at the read position for every captured layer."""
    logit_a: float
    logit_b: float
    logprob_a: float
    logprob_b: float
    p_a: float                      # restricted, as e2a's read
    p_b: float
    label_mass: float
    pick: str
    top1_id: int
    top1_is_label: bool
    resid_last: dict[int, np.ndarray] = field(default_factory=dict)
    #: Stage C: residuals at DECLARED positions, [len(capture_positions), D]
    #: per layer, rows in `capture_positions` order (the read position is
    #: always among them; `resid_last` is its row).
    resid_at: dict[int, np.ndarray] = field(default_factory=dict)
    capture_positions: tuple[int, ...] = ()

    def as_dict(self) -> dict:
        d = {"logit_a": self.logit_a, "logit_b": self.logit_b,
             "logprob_a": self.logprob_a, "logprob_b": self.logprob_b,
             "p_a": self.p_a, "p_b": self.p_b,
             "label_mass": self.label_mass, "pick": self.pick,
             "top1_id": self.top1_id, "top1_is_label": self.top1_is_label,
             "resid_sha16_by_layer": {int(l): sha16_arr(v)
                                      for l, v in self.resid_last.items()}}
        if self.resid_at:
            d["capture_positions"] = list(self.capture_positions)
            d["resid_at_sha16_by_layer"] = {int(l): sha16_arr(v)
                                            for l, v in self.resid_at.items()}
        return d


@dataclass
class SpanProvenance:
    start: int
    end: int
    tag: str
    layer: int
    alpha: float
    direction_sha: str
    frac: float | None
    sign: int

    def as_dict(self) -> dict:
        return self.__dict__.copy()


@dataclass
class EchoPair:
    state: MaskedPrefixRead
    shadow: MaskedPrefixRead
    shadow_choice_read: ChoiceRead
    n_positions: int
    read_position: int
    label_a: str
    label_b: str
    spans: list[SpanProvenance]
    mask_sha16: str
    n_steered: int
    prefix_sha16: str
    shadow_vs_choice_read_abs_dpa: float
    session_id: str = ""
    read_name: str = ""

    def as_dict(self) -> dict:
        return {"session_id": self.session_id, "read_name": self.read_name,
                "label_a": self.label_a, "label_b": self.label_b,
                "n_positions": self.n_positions,
                "read_position": self.read_position,
                "spans": [s.as_dict() for s in self.spans],
                "mask_sha16": self.mask_sha16, "n_steered": self.n_steered,
                "prefix_sha16": self.prefix_sha16,
                "state": self.state.as_dict(),
                "shadow": self.shadow.as_dict(),
                "shadow_choice_read": self.shadow_choice_read.as_dict(),
                "shadow_vs_choice_read_abs_dpa":
                    self.shadow_vs_choice_read_abs_dpa}


def _view(res: LastForwardResult, ia: int, ib: int, label_a: str,
          label_b: str, positions: Sequence[int] = (),
          read_position: int | None = None) -> MaskedPrefixRead:
    lg = np.asarray(res.logits, dtype=np.float64)
    p = softmax(res.logits)
    logp = lg - (lg.max() + np.log(np.sum(np.exp(lg - lg.max()))))
    pa, pb = float(p[ia]), float(p[ib])
    mass = pa + pb
    top1 = int(np.argmax(res.logits))
    return MaskedPrefixRead(
        logit_a=float(lg[ia]), logit_b=float(lg[ib]),
        logprob_a=float(logp[ia]), logprob_b=float(logp[ib]),
        p_a=pa / (mass + EPS), p_b=pb / (mass + EPS), label_mass=mass,
        pick=label_a if pa >= pb else label_b, top1_id=top1,
        top1_is_label=top1 in (ia, ib),
        resid_last=(
            {int(l): np.asarray(v, dtype=np.float32)
             for l, v in res.resid_last.items()} if not positions else
            {int(l): np.asarray(v[list(positions).index(read_position)],
                                dtype=np.float32)
             for l, v in res.resid_last.items()}),
        resid_at=({int(l): np.asarray(v, dtype=np.float32)
                   for l, v in res.resid_last.items()} if positions else {}),
        capture_positions=tuple(int(p) for p in positions))


def build_mask(n_positions: int,
               spans: Sequence[tuple[int, int, Injection, str]]) -> np.ndarray:
    """Per-position mask: 0 unsteered, else the sign of the covering
    injection's alpha. Spans must be disjoint, in range, and end before the
    read position (n_positions - 1)."""
    n = int(n_positions)
    mask = np.zeros(n, dtype=np.int8)
    for a, b, inj, tag in spans:
        a, b = int(a), int(b)
        if not (0 <= a < b <= n - 1):
            raise AssertionError(
                f"span {tag} [{a}, {b}) is not inside [0, {n - 1}) -- it "
                f"would reach the read position {n - 1} or fall off the text")
        if np.any(mask[a:b] != 0):
            raise AssertionError(f"span {tag} [{a}, {b}) overlaps another span")
        mask[a:b] = 1 if inj.alpha > 0 else -1
    if mask[n - 1] != 0:
        raise AssertionError("read position is steered")
    return mask


def read_choice_maskedprefix(adapter: ModelAdapter, transcript_text: str,
                             label_a: str, label_b: str,
                             label_ids: Mapping[str, int],
                             spans: Sequence[tuple[int, int, Injection, str]],
                             capture_layers: Iterable[int] = (),
                             session_id: str = "",
                             read_name: str = "",
                             capture_positions: Sequence[int] | None = None
                             ) -> EchoPair:
    """The echo read with its mandatory shadow.

    `spans`: (token_start, token_end, injection, tag) -- half-open token
    ranges in the tokenization of `transcript_text`, each carrying its own
    declared `Injection` (built via `Injection.at_frac`, rule 1). The
    injection's own `PositionSpec` is REPLACED with exactly its span.

    `capture_positions` (Stage C): residuals are ALSO returned at these
    declared positions (`resid_at`, rows in the given order). Every capture
    position must be UNSTEERED (mask == 0) -- the recon reads the state's
    echo at positions the state never touched -- and the read position is
    always captured.
    """
    assert_statepresent_absent()
    for _, _, inj, tag in spans:
        if not isinstance(inj, Injection):
            raise TypeError(f"span {tag}: injections must be declared "
                            f"Injection objects (rule 1)")
    ids = adapter.encode(transcript_text)
    n = len(ids)
    adapter.assert_choice_window(n, where="read_choice_maskedprefix")
    mask = build_mask(n, spans)
    placed = [inj.with_positions(PositionSpec.spans((int(a), int(b))))
              for a, b, inj, _ in spans]
    for inj in placed:
        if inj.positions.touches_last(n):
            raise AssertionError("an injection touches the read position")
    # The mask is the declared spans and nothing else: check the placed
    # PositionSpecs against it position by position (O(n), cheap, explicit).
    covered = np.zeros(n, dtype=np.int8)
    for inj in placed:
        for p in range(n):
            if inj.positions.contains(p):
                covered[p] = 1 if inj.alpha > 0 else -1
    if not np.array_equal(covered, mask):
        raise AssertionError("placed PositionSpecs disagree with the mask")

    caps = sorted({int(l) for l in capture_layers})
    ia, ib = label_ids[label_a], label_ids[label_b]

    if capture_positions is None:
        res_state = adapter.forward_last(ids, capture_layers=caps,
                                         injections=placed)
        res_shadow = adapter.forward_last(ids, capture_layers=caps,
                                          injections=())
        positions: tuple[int, ...] = ()
    else:
        positions = tuple(int(p) for p in capture_positions)
        if (n - 1) not in positions:
            raise AssertionError("the read position must be among the "
                                 "capture positions")
        for p in positions:
            if not (0 <= p < n):
                raise AssertionError(f"capture position {p} outside [0, {n})")
            if mask[p] != 0:
                raise AssertionError(
                    f"capture position {p} is steered; the recon reads the "
                    f"echo only at unsteered positions")
        res_state = adapter.forward_at(ids, caps, positions, injections=placed)
        res_shadow = adapter.forward_at(ids, caps, positions, injections=())
    # The untouched insulated primitive, with its own verify forward.
    cr = choice_read(adapter, transcript_text, label_a, label_b, label_ids,
                     verify=True)
    state = _view(res_state, ia, ib, label_a, label_b, positions, n - 1)
    shadow = _view(res_shadow, ia, ib, label_a, label_b, positions, n - 1)
    dpa = abs(shadow.p_a - cr.p_a)
    prov = [SpanProvenance(start=int(a), end=int(b), tag=str(tag),
                           layer=int(inj.layer), alpha=float(inj.alpha),
                           direction_sha=str(inj.direction_sha),
                           frac=inj.frac, sign=1 if inj.alpha > 0 else -1)
            for (a, b, inj, tag) in spans]
    return EchoPair(state=state, shadow=shadow, shadow_choice_read=cr,
                    n_positions=n, read_position=n - 1,
                    label_a=label_a, label_b=label_b, spans=prov,
                    mask_sha16=mask_sha(mask), n_steered=int(np.sum(mask != 0)),
                    prefix_sha16=prefix_sha(transcript_text),
                    shadow_vs_choice_read_abs_dpa=float(dpa),
                    session_id=session_id, read_name=read_name)


__all__ = ["read_choice_maskedprefix", "build_mask", "EchoPair",
           "MaskedPrefixRead", "SpanProvenance", "prefix_sha", "mask_sha",
           "assert_statepresent_absent", "FORBIDDEN_MODULES"]
