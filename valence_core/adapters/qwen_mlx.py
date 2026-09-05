"""`QwenMLXAdapter` -- the laptop oracle, wrapping the validated `jlens_qwen`
stack unchanged.

CLAUDE.md v3.1 §Phase 0 step 1 and ledger 26. The point of this file is that
it adds no arithmetic. Vanilla forwards delegate to `MLXLensModel.forward`;
injected forwards delegate to `forced_choice.forward_with_positional_state`;
the cached generation path delegates to `conditioning.SteeredStreamSession`.
Every published Qwen number must come back through this wrapper bit-for-bit,
so a difference here is a refactor bug by default, never a new finding.

The one generalization over the cycle-3/4 code: `e2a.generate_round_positional`
hard-codes `LAYER = 48` in its uncached position function. Here the geometry
comes from each `Injection.positions`, so the same loop serves any layer set
-- required, since OLMo's workspace layers are not Qwen's and rule 1 forbids
inheriting either.

`jlens-qwen36/` is a gitignored external clone: this module imports from it,
and nothing is ever written into it.
"""

from __future__ import annotations

import importlib
import os
import sys
from typing import Iterable, Sequence

import numpy as np

from .base import (ForwardResult, GenerateResult, Injection, ModelAdapter,
                   PositionSpec,
                   LastForwardResult)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
CLONE = os.path.join(REPO_ROOT, "jlens-qwen36")


def _ensure_clone_on_path() -> None:
    if not os.path.isdir(CLONE):
        raise RuntimeError(
            f"the jlens-qwen36 clone is missing at {CLONE}. It is gitignored "
            f"by design (external tool + local patches); see CLAUDE.md "
            f"§Environment for setup. The Qwen oracle cannot run without it.")
    if CLONE not in sys.path:
        sys.path.insert(0, CLONE)


class QwenMLXAdapter(ModelAdapter):
    name = "qwen3.6-27b-4bit-mlx"

    # DECLARED choice-read window (PROPOSAL-g clause, adopted 2026-08-18).
    # Chosen, not inherited: the tokenizer reports model_max_length 262144
    # and `MLXLensModel.encode` carried a max_length=512 default -- neither
    # is a scientific choice, and the 512 became an experimental parameter
    # purely by inheritance. 8192 is declared with headroom against the
    # measured ceiling: the window-coverage audit (2026-08-18) found the
    # longest archived choice-read prefix across e2a+f to be 666 tokens.
    # A session that grows past 8192 is an incident, not a silent clip.
    CHOICE_WINDOW = 8192
    #
    # Historical fidelity only: the 512-token tail truncation every
    # published cycle-3/4 number was produced through. Reachable ONLY via
    # legacy_truncate=True, which the rule-26 oracle sets explicitly. New
    # work runs full-session.
    LEGACY_ENCODE_MAX_LENGTH = 512

    def __init__(self, model=None, model_id: str = "mlx-community/Qwen3.6-27B-4bit",
                 choice_window: int | None = None,
                 legacy_truncate: bool = False):
        _ensure_clone_on_path()
        self._mx = importlib.import_module("mlx.core")
        self._model_mod = importlib.import_module("jlens_qwen.model")
        self._fc = importlib.import_module("jlens_qwen.forced_choice")
        self._cond = importlib.import_module("jlens_qwen.conditioning")
        self._patch_gdn = importlib.import_module("jlens_qwen.patch_gdn")
        self.model_id = model_id
        self.legacy_truncate = bool(legacy_truncate)
        self.max_length = (self.LEGACY_ENCODE_MAX_LENGTH
                           if self.legacy_truncate else None)
        # Startup assertion: the window is declared, positive, and (in
        # legacy mode) consistent with the truncation actually applied.
        self.choice_window = (
            self.LEGACY_ENCODE_MAX_LENGTH if self.legacy_truncate
            else (self.CHOICE_WINDOW if choice_window is None else choice_window))
        if not isinstance(self.choice_window, int) or self.choice_window <= 0:
            raise ValueError(
                f"choice_window must be a positive int, got "
                f"{self.choice_window!r}")
        self.n_clipped = 0
        self._model = model if model is not None else self._model_mod.load(model_id)
        # Ops kernel, not fused: every published strain/accuracy number was
        # measured on it (conditioning.SteeredStreamSession's own note).
        self._patch_gdn.set_inference_mode(False)

    # --- tokenization -----------------------------------------------------
    def encode(self, text: str, add_special_tokens: bool = True) -> list[int]:
        """Full-session by default. Under `legacy_truncate=True` it tail-
        truncates to 512 exactly as `MLXLensModel.encode` did, which is the
        path every published cycle-3/4 number came through -- kept reachable
        for rule-26 reproduction and for nothing else."""
        ids = list(self._model.tokenizer.encode(
            text, add_special_tokens=add_special_tokens))
        if self.max_length and len(ids) > self.max_length:
            # Legacy mode only. Counted rather than silent: the count is
            # reported in provenance, which is precisely what was missing
            # when this truncation shaped every published choice read.
            self.n_clipped += 1
            ids = ids[-self.max_length:]
        return ids

    def decode(self, ids: Sequence[int]) -> str:
        return self._model.tokenizer.decode(list(ids))

    @property
    def eos_id(self) -> int | None:
        return getattr(self._model.tokenizer, "eos_token_id", None)

    @property
    def special_token_strings(self) -> list[str]:
        return [str(t) for t in
                getattr(self._model.tokenizer, "all_special_tokens", [])]

    @property
    def n_layers(self) -> int:
        return len(self._model.layers)

    # --- injection plumbing ----------------------------------------------
    def _mx_vec(self, u: np.ndarray, alpha: float):
        return self._mx.array(np.asarray(u * alpha, dtype=np.float32))

    def _positional_fns(self, injections: Sequence[Injection]) -> dict:
        """{layer: fn(p, h)} in the convention
        `forward_with_positional_state` expects. Injections sharing a layer
        are summed at each position they both cover -- the multi_steer
        semantics, kept."""
        by_layer: dict[int, list[Injection]] = {}
        for inj in injections:
            by_layer.setdefault(int(inj.layer), []).append(inj)

        def make(layer_injs):
            deltas = [(self._mx_vec(i.u, i.alpha), i.positions)
                      for i in layer_injs]

            def fn(p, h):
                out = h.astype(self._mx.float32)
                for d, pos in deltas:
                    if pos.contains(p):
                        out = out + d
                return out
            return fn

        return {layer: make(injs) for layer, injs in by_layer.items()}

    # --- forwards ---------------------------------------------------------
    def forward(self, ids: Sequence[int],
                capture_layers: Iterable[int] = (),
                injections: Sequence[Injection] = ()) -> ForwardResult:
        mx = self._mx
        arr = mx.array([list(ids)])
        caps = list(capture_layers)
        if not injections:
            # The validated vanilla path, untouched -- rule-26 criterion
            # (iii) requires this to be the identical code path e2a's
            # choice_read used, not an equivalent one.
            final, acts = self._model.forward(arr, capture_layers=caps)
        else:
            final, acts = self._fc.forward_with_positional_state(
                self._model, arr, self._positional_fns(injections),
                capture_layers=caps)
        logits = self._model.unembed(final[:, -1, :])[0].astype(mx.float32)
        return ForwardResult(
            logits=np.array(logits.tolist(), dtype=np.float32),
            acts={l: np.array(acts[l][0].tolist(), dtype=np.float32)
                  for l in acts},
            n_positions=len(list(ids)))

    def forward_last(self, ids: Sequence[int],
                     capture_layers: Iterable[int] = (),
                     injections: Sequence[Injection] = ()) -> LastForwardResult:
        """`forward` at the final position only -- identical dispatch (the
        validated vanilla path when there is no injection, the positional
        re-forward otherwise; both uncached), identical logits; the captured
        residuals are sliced to the last position BEFORE the numpy
        conversion. `forward` is untouched."""
        mx = self._mx
        arr = mx.array([list(ids)])
        caps = list(capture_layers)
        if not injections:
            final, acts = self._model.forward(arr, capture_layers=caps)
        else:
            final, acts = self._fc.forward_with_positional_state(
                self._model, arr, self._positional_fns(injections),
                capture_layers=caps)
        logits = self._model.unembed(final[:, -1, :])[0].astype(mx.float32)
        last = {l: np.array(acts[l][0, -1, :].astype(mx.float32).tolist(),
                            dtype=np.float32) for l in acts}
        return LastForwardResult(
            logits=np.array(logits.tolist(), dtype=np.float32),
            resid_last=last, n_positions=len(list(ids)))

    def embed(self, text: str) -> np.ndarray:
        """Exactly `e2a_g2_discriminability.embed`: vanilla forward, mean over
        positions of the post-norm final residual, float64. The empty-string
        guard is kept -- a degenerate round would otherwise fail to encode,
        and dropping it silently would change the sample."""
        mx = self._mx
        ids = mx.array([self.encode(text if text.strip() else " ")])
        final, _ = self._model.forward(ids, capture_layers=[])
        v = final[0].astype(mx.float32).mean(axis=0)
        mx.eval(v)
        return np.array(v.tolist(), dtype=np.float64)

    # --- generation -------------------------------------------------------
    def generate(self, prefix_text: str, segment_text: str,
                 injections: Sequence[Injection] = (),
                 *, seed: int | None = None, temp: float = 0.0,
                 max_tokens: int = 60, stop_newline: bool = True,
                 ban_ids: Iterable[int] = (),
                 cached: bool = False) -> GenerateResult:
        """Port of `e2a.generate_round_positional`, generalized over layers.

        Delivery geometry: the state is active from the segment boundary
        onward and never before it (rule 5 horn (a) by construction). Any
        `PositionSpec` carried on the injections is overridden here with
        `from_index(boundary)` -- the boundary is a property of the texts,
        not of the caller's bookkeeping, and computing it here is what makes
        the guarantee structural.
        """
        mx = self._mx
        prefix_ids = self.encode(prefix_text)
        seg_ids = self.encode(prefix_text + segment_text)
        boundary = 0
        while (boundary < len(prefix_ids) and boundary < len(seg_ids)
               and prefix_ids[boundary] == seg_ids[boundary]):
            boundary += 1

        placed = [inj.with_positions(PositionSpec.from_index(boundary))
                  for inj in injections]
        ban_ids = list(ban_ids)
        if seed is not None:
            mx.random.seed(seed)

        eos = self.eos_id
        generated: list[int] = []
        first_logits = None
        cap_hit = True
        stop_reason = "cap"
        content_seen = False
        ban_vec = None

        def sample(logits):
            nonlocal ban_vec
            lg = logits.astype(mx.float32)
            if ban_ids:                     # round generation only (rule 13)
                if ban_vec is None:
                    v = np.zeros(lg.shape[-1], dtype=np.float32)
                    v[ban_ids] = -1e30
                    ban_vec = mx.array(v)
                lg = lg + ban_vec
            if temp <= 0.0:
                return int(mx.argmax(lg).tolist())
            return int(mx.random.categorical(lg / temp).tolist())

        def is_stop(tok: int) -> bool:
            if eos is not None and tok == eos:
                return True
            # Leading pure-whitespace tokens are template whitespace, not
            # response content (g2r refinement: without this, responses
            # opening with a newline truncated to empty, and the empties
            # were pole-correlated).
            return (stop_newline and content_seen
                    and "\n" in self.decode([tok]))

        def note(tok: int) -> None:
            nonlocal content_seen
            if self.decode([tok]).strip():
                content_seen = True

        if cached:
            fns = self._induce_fns_flat(placed)
            session = self._cond.SteeredStreamSession(self._model, {})
            if boundary:
                session.extend(seg_ids[:boundary])
            session.induce_fns = fns
            logits, _ = session.extend(seg_ids[boundary:])
            first_logits = logits
            for _ in range(max_tokens):
                tok = sample(logits)
                if is_stop(tok):
                    cap_hit, stop_reason = False, (
                        "eos" if tok == eos else "newline")
                    break
                generated.append(tok)
                note(tok)
                logits, _ = session.extend([tok])
        else:
            pos_fns = self._positional_fns(placed)
            ids = mx.array([seg_ids])
            for step in range(max_tokens):
                final, _ = self._fc.forward_with_positional_state(
                    self._model, ids, pos_fns, capture_layers=[])
                logits = self._model.unembed(final[:, -1, :])[0]
                if step == 0:
                    first_logits = logits
                tok = sample(logits)
                if is_stop(tok):
                    cap_hit, stop_reason = False, (
                        "eos" if tok == eos else "newline")
                    break
                generated.append(tok)
                note(tok)
                ids = mx.concatenate([ids, mx.array([[tok]])], axis=1)

        return GenerateResult(
            text=self.decode(generated).strip(),
            token_ids=generated,
            first_logits=np.array(
                first_logits.astype(mx.float32).tolist(), dtype=np.float32),
            cap_hit=cap_hit,
            stop_reason=stop_reason)

    def _induce_fns_flat(self, injections: Sequence[Injection]) -> dict:
        """{layer: fn(h)} for the cached stream, which applies its callable to
        every position of the chunk it is fed. The positional guarantee is
        carried by *which* chunk gets the state (prefix extended before
        `induce_fns` is set), exactly as e2a did it."""
        by_layer: dict[int, list[Injection]] = {}
        for inj in injections:
            by_layer.setdefault(int(inj.layer), []).append(inj)

        def make(layer_injs):
            deltas = [self._mx_vec(i.u, i.alpha) for i in layer_injs]

            def fn(h):
                out = h.astype(self._mx.float32)
                for d in deltas:
                    out = out + d
                return out
            return fn

        return {layer: make(injs) for layer, injs in by_layer.items()}

    # --- profiling --------------------------------------------------------
    def resid_norms(self, layers: Iterable[int],
                    texts: Sequence[str]) -> dict[int, float]:
        """Mean L2 residual norm per layer, averaged over all positions of
        all `texts`.

        Convention, matching `e0_extract_axis.py` exactly: per text, the mean
        L2 norm over its positions; then the mean of those per-text means.
        That is NOT the same as a global mean over all positions when texts
        differ in length, and the published `R_per_layer_spanmean` (R48 =
        103.01) is the former -- so this must be too, or the repo would carry
        two incompatible definitions of the quantity every dose is a fraction
        of.

        For span-restricted profiling over an extraction corpus (the e0 case,
        where only the frame span counts), use
        `valence_core.extract.resid_norm_table`, which takes the boundaries
        into account. This method is the whole-text profiler.
        """
        layers = sorted(set(int(l) for l in layers))
        per_text = {l: [] for l in layers}
        for text in texts:
            res = self.forward(self.encode(text), capture_layers=layers)
            for l in layers:
                h = res.acts[l]                       # [S, D]
                per_text[l].append(float(np.linalg.norm(h, axis=-1).mean()))
        return {l: float(np.mean(per_text[l])) for l in layers}

    # --- provenance -------------------------------------------------------
    def provenance(self) -> dict:
        import platform
        from importlib.metadata import PackageNotFoundError, version
        # `mlx.__version__` does not exist; reading it yielded "?" in the
        # first rule-26 run, which is a ledger-27 defect (versions must be
        # pinned in the logged entry, not elided).
        vers = {}
        for pkg in ("mlx", "mlx-lm", "numpy"):
            try:
                vers[pkg] = version(pkg)
            except PackageNotFoundError:
                vers[pkg] = "absent"
        mlx_ver = vers["mlx"]
        return {
            "adapter": self.name,
            "model_id": self.model_id,
            "dtype": "4bit-quantized (MLX)",
            "backend": "mlx",
            "mlx_version": mlx_ver,
            "library_versions": vers,
            "python": platform.python_version(),
            "platform": platform.platform(),
            "gdn_inference_mode": "ops (fused disabled)",
            "n_layers": self.n_layers,
            "choice_window_declared": self.choice_window,
            "legacy_truncate_512": self.legacy_truncate,
            "n_encodes_clipped": self.n_clipped,
        }
