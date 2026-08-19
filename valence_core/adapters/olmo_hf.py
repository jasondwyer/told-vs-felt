"""`OLMoHFAdapter` -- the Phase-2 execution adapter (PyTorch / HF / CUDA).

Same surface as `QwenMLXAdapter`, no other differences. Everything the core
battery does is expressed through `ModelAdapter`, so the only thing that
changes between the Qwen oracle and an OLMo checkpoint is which adapter is
constructed.

Three points where a PyTorch port could silently diverge from the MLX
original, handled explicitly rather than by accident:

1. **Injection site.** MLX patched the residual as it *exited* a layer
   (`hidden = layer(...)` then patch). A `forward_hook` on the decoder layer
   is the exact analog: it sees the layer's output and returns a modified
   one. A `forward_pre_hook` would be off by one layer, and a hook on the
   attention submodule would be off by a residual add.
2. **Position bookkeeping under KV cache.** With a cache, a hook sees only
   the *new* token positions, not the whole sequence. The absolute offset is
   tracked so `PositionSpec` means the same thing cached and uncached --
   this is where a cached/uncached kernel gate (rule 2) would otherwise
   fail for a reason that has nothing to do with kernels.
3. **Injection dtype.** Weights are bf16, so the delta is computed in fp32
   and cast at the add. bf16 carries ~3 decimal digits, so this is a real
   numerics decision, and it is one of the things the per-backend rule-2
   characterization has to measure rather than assume.

The choice-read window is DECLARED (PROPOSAL-g clause), and additionally
bounded by the checkpoint's own `max_position_embeddings` -- our design
parameter, sanity-checked against the model's actual capability.
"""

from __future__ import annotations

import os
from typing import Iterable, Sequence

import numpy as np

from .base import (ForwardResult, GenerateResult, Injection, ModelAdapter,
                   PositionSpec)

# Declared, not inherited. Same reasoning as the Qwen oracle: the measured
# ceiling across every archived session prefix was 666 tokens (2026-08-18
# window-coverage audit), so 8192 is generous headroom while still being a
# number a session can be checked against.
DEFAULT_CHOICE_WINDOW = 8192


class OLMoHFAdapter(ModelAdapter):
    name = "olmo-hf"

    def __init__(self, path: str, *, device: str = "cuda",
                 dtype: str = "bfloat16",
                 choice_window: int | None = None,
                 deterministic: bool = True,
                 seed: int = 20260818):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer

        self._torch = torch
        self.path = str(path)
        self.device = device
        self.dtype_name = dtype
        self.seed = seed
        self.deterministic = deterministic

        if deterministic:
            # Rule 2. CUBLAS_WORKSPACE_CONFIG must be set BEFORE the first
            # CUDA context or the deterministic cuBLAS path is unavailable;
            # env.sh sets it, and this refuses to pretend otherwise.
            if not os.environ.get("CUBLAS_WORKSPACE_CONFIG"):
                raise RuntimeError(
                    "deterministic=True requires CUBLAS_WORKSPACE_CONFIG "
                    "(':4096:8') in the environment before torch initializes "
                    "CUDA. Set it in env.sh, not here.")
            torch.use_deterministic_algorithms(True, warn_only=True)
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False
        torch.manual_seed(seed)

        self._tok = AutoTokenizer.from_pretrained(self.path)
        self._model = AutoModelForCausalLM.from_pretrained(
            self.path, dtype=getattr(torch, dtype)).to(device).eval()

        cfg = self._model.config
        cap = int(getattr(cfg, "max_position_embeddings", 0) or 0)
        self.choice_window = int(choice_window or DEFAULT_CHOICE_WINDOW)
        if cap and self.choice_window > cap:
            raise ValueError(
                f"declared choice_window {self.choice_window} exceeds the "
                f"checkpoint's max_position_embeddings {cap}")
        self._layers = self._model.model.layers
        self._n_layers = len(self._layers)

    # --- tokenization -----------------------------------------------------
    def encode(self, text: str, add_special_tokens: bool = True) -> list[int]:
        """No truncation, ever. The window is asserted, not silently applied
        -- that distinction is the whole point of the PROPOSAL-g clause."""
        return list(self._tok.encode(text, add_special_tokens=add_special_tokens))

    def decode(self, ids: Sequence[int]) -> str:
        return self._tok.decode(list(ids))

    @property
    def eos_id(self) -> int | None:
        return self._tok.eos_token_id

    @property
    def special_token_strings(self) -> list[str]:
        return [str(t) for t in (self._tok.all_special_tokens or [])]

    @property
    def n_layers(self) -> int:
        return self._n_layers

    # --- hook plumbing ----------------------------------------------------
    def _delta_for(self, inj: Injection, dtype):
        t = self._torch
        v = t.from_numpy(np.ascontiguousarray(inj.u * inj.alpha,
                                              dtype=np.float32))
        return v.to(self.device).to(dtype)

    def _make_hooks(self, injections: Sequence[Injection],
                    capture_layers: Iterable[int], store: dict,
                    offset_ref: list[int]):
        """Returns handles. `offset_ref[0]` is the absolute index of the
        first position in this call -- nonzero when a KV cache is in play,
        which is what keeps PositionSpec meaning the same thing on both
        paths."""
        t = self._torch
        by_layer: dict[int, list[Injection]] = {}
        for inj in injections:
            by_layer.setdefault(int(inj.layer), []).append(inj)
        capture = set(int(l) for l in capture_layers)
        handles = []

        def make(layer_idx):
            injs = by_layer.get(layer_idx, [])

            def hook(_module, _inp, out):
                hs = out[0] if isinstance(out, tuple) else out
                if injs:
                    base = offset_ref[0]
                    S = hs.shape[1]
                    acc = t.zeros_like(hs)
                    touched = False
                    for inj in injs:
                        mask = t.tensor(
                            [1.0 if inj.positions.contains(base + p) else 0.0
                             for p in range(S)],
                            device=hs.device, dtype=t.float32)
                        if mask.any():
                            touched = True
                            d = self._delta_for(inj, t.float32)
                            acc = acc + (mask[None, :, None] * d[None, None, :]
                                         ).to(acc.dtype)
                    if touched:
                        hs = (hs.to(t.float32) + acc.to(t.float32)).to(hs.dtype)
                if layer_idx in capture:
                    store[layer_idx] = hs.detach()
                if isinstance(out, tuple):
                    return (hs,) + tuple(out[1:])
                return hs
            return hook

        for li in sorted(set(by_layer) | capture):
            handles.append(self._layers[li].register_forward_hook(make(li)))
        return handles

    # --- forwards ---------------------------------------------------------
    def forward(self, ids: Sequence[int],
                capture_layers: Iterable[int] = (),
                injections: Sequence[Injection] = ()) -> ForwardResult:
        t = self._torch
        ids = list(ids)
        store: dict[int, object] = {}
        offset = [0]
        handles = self._make_hooks(injections, capture_layers, store, offset)
        try:
            x = t.tensor([ids], device=self.device)
            with t.inference_mode():
                out = self._model(input_ids=x, use_cache=False)
            logits = out.logits[0, -1, :].to(t.float32).cpu().numpy()
            acts = {l: v[0].to(t.float32).cpu().numpy() for l, v in store.items()}
        finally:
            for h in handles:
                h.remove()
        return ForwardResult(logits=logits.astype(np.float32), acts=acts,
                             n_positions=len(ids))

    def embed(self, text: str) -> np.ndarray:
        """Mean-pooled final-layer post-norm residual, matching the Qwen
        adapter's definition so discriminability numbers mean the same thing
        across backends."""
        t = self._torch
        ids = self.encode(text if text.strip() else " ")
        with t.inference_mode():
            out = self._model.model(
                input_ids=t.tensor([ids], device=self.device), use_cache=False)
        hs = out.last_hidden_state[0]
        return hs.to(t.float32).mean(dim=0).cpu().numpy().astype(np.float64)

    # --- generation -------------------------------------------------------
    def generate(self, prefix_text: str, segment_text: str,
                 injections: Sequence[Injection] = (),
                 *, seed: int | None = None, temp: float = 0.0,
                 max_tokens: int = 60, stop_newline: bool = True,
                 ban_ids: Iterable[int] = (),
                 cached: bool = False) -> GenerateResult:
        t = self._torch
        prefix_ids = self.encode(prefix_text)
        seg_ids = self.encode(prefix_text + segment_text)
        boundary = 0
        while (boundary < len(prefix_ids) and boundary < len(seg_ids)
               and prefix_ids[boundary] == seg_ids[boundary]):
            boundary += 1

        placed = [i.with_positions(PositionSpec.from_index(boundary))
                  for i in injections]
        ban_ids = list(ban_ids)
        if seed is not None:
            t.manual_seed(seed)

        gen: list[int] = []
        first_logits = None
        cap_hit, stop_reason, content_seen = True, "cap", False

        def pick(logits_1d):
            lg = logits_1d.to(t.float32)
            if ban_ids:
                lg = lg.clone()
                lg[ban_ids] = -1e30
            if temp <= 0.0:
                return int(t.argmax(lg).item())
            probs = t.softmax(lg / temp, dim=-1)
            return int(t.multinomial(probs, 1).item())

        store: dict[int, object] = {}
        offset = [0]
        handles = self._make_hooks(placed, (), store, offset)
        try:
            with t.inference_mode():
                if cached:
                    x = t.tensor([seg_ids], device=self.device)
                    out = self._model(input_ids=x, use_cache=True)
                    past = out.past_key_values
                    logits = out.logits[0, -1, :]
                    first_logits = logits.to(t.float32).cpu().numpy()
                    offset[0] = len(seg_ids)
                    for _ in range(max_tokens):
                        tok = pick(logits)
                        if self._is_stop(tok, content_seen, stop_newline):
                            cap_hit, stop_reason = False, (
                                "eos" if tok == self.eos_id else "newline")
                            break
                        gen.append(tok)
                        content_seen |= bool(self.decode([tok]).strip())
                        out = self._model(
                            input_ids=t.tensor([[tok]], device=self.device),
                            past_key_values=past, use_cache=True)
                        past = out.past_key_values
                        logits = out.logits[0, -1, :]
                        offset[0] += 1
                else:
                    ids = list(seg_ids)
                    for step in range(max_tokens):
                        offset[0] = 0
                        out = self._model(
                            input_ids=t.tensor([ids], device=self.device),
                            use_cache=False)
                        logits = out.logits[0, -1, :]
                        if step == 0:
                            first_logits = logits.to(t.float32).cpu().numpy()
                        tok = pick(logits)
                        if self._is_stop(tok, content_seen, stop_newline):
                            cap_hit, stop_reason = False, (
                                "eos" if tok == self.eos_id else "newline")
                            break
                        gen.append(tok)
                        content_seen |= bool(self.decode([tok]).strip())
                        ids.append(tok)
        finally:
            for h in handles:
                h.remove()

        return GenerateResult(
            text=self.decode(gen).strip(), token_ids=gen,
            first_logits=np.asarray(first_logits, dtype=np.float32),
            cap_hit=cap_hit, stop_reason=stop_reason)

    def _is_stop(self, tok: int, content_seen: bool, stop_newline: bool) -> bool:
        if self.eos_id is not None and tok == self.eos_id:
            return True
        return (stop_newline and content_seen
                and "\n" in self.decode([tok]))

    # --- profiling --------------------------------------------------------
    def resid_norms(self, layers: Iterable[int],
                    texts: Sequence[str]) -> dict[int, float]:
        """Mean of per-text mean L2 norms -- the same convention as the Qwen
        adapter and `e0_extract_axis`, so R_l means one thing repo-wide.
        Rule 1: this must be measured per checkpoint, never inherited."""
        layers = sorted(set(int(l) for l in layers))
        per = {l: [] for l in layers}
        for text in texts:
            res = self.forward(self.encode(text), capture_layers=layers)
            for l in layers:
                per[l].append(float(np.linalg.norm(res.acts[l], axis=-1).mean()))
        return {l: float(np.mean(per[l])) for l in layers}

    # --- provenance -------------------------------------------------------
    def provenance(self) -> dict:
        import platform
        from importlib.metadata import PackageNotFoundError, version
        t = self._torch
        vers = {}
        for pkg in ("torch", "transformers", "accelerate", "safetensors",
                    "huggingface_hub", "numpy"):
            try:
                vers[pkg] = version(pkg)
            except PackageNotFoundError:
                vers[pkg] = "absent"
        return {
            "adapter": self.name, "path": self.path, "dtype": self.dtype_name,
            "backend": "torch/cuda", "device": self.device,
            "gpu": t.cuda.get_device_name(0) if t.cuda.is_available() else None,
            "cuda": t.version.cuda,
            "capability": list(t.cuda.get_device_capability(0))
            if t.cuda.is_available() else None,
            "deterministic": self.deterministic,
            "cublas_workspace_config": os.environ.get("CUBLAS_WORKSPACE_CONFIG"),
            "seed": self.seed,
            "choice_window_declared": self.choice_window,
            "n_layers": self.n_layers,
            "library_versions": vers,
            "python": platform.python_version(),
        }
