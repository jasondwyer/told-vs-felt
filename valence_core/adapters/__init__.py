"""Backend adapters. Each module imports its own framework and nothing else
imports it, so `valence_core` stays importable on a box with only one of
MLX / torch installed.

`get_adapter(name)` resolves lazily for the same reason.
"""

from __future__ import annotations

from .base import (ForwardResult, GenerateResult, Injection, ModelAdapter,
                   PositionSpec, assert_equal_norm, sha16_arr)

__all__ = ["ModelAdapter", "Injection", "PositionSpec", "ForwardResult",
           "GenerateResult", "assert_equal_norm", "sha16_arr", "get_adapter"]


def get_adapter(name: str, **kwargs) -> ModelAdapter:
    if name in ("qwen", "qwen_mlx", "qwen3.6-27b-4bit-mlx"):
        from .qwen_mlx import QwenMLXAdapter
        return QwenMLXAdapter(**kwargs)
    if name in ("olmo", "olmo_hf"):
        from .olmo_hf import OLMoHFAdapter      # Phase 0 step 2
        return OLMoHFAdapter(**kwargs)
    raise KeyError(f"unknown adapter {name!r}")
