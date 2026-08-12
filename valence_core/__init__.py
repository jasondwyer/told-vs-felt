"""valence_core -- the model-agnostic measurement battery.

CLAUDE.md v3.1 §Phase 0 step 1. Ported (not rewritten) from the cycle-1..4
Qwen stack; accepted only by ledger 26, the refactor regression law.

Import policy: nothing at this level imports a backend. `valence_core.*`
is numpy plus `valence_core.adapters.base` types; MLX lives only inside
`adapters.qwen_mlx`, torch only inside `adapters.olmo_hf`. Importing this
package on a machine with neither must succeed.
"""

from __future__ import annotations

from .adapters.base import (ForwardResult, GenerateResult, Injection,
                            ModelAdapter, PositionSpec, assert_equal_norm,
                            sha16_arr)

__all__ = ["ModelAdapter", "Injection", "PositionSpec", "ForwardResult",
           "GenerateResult", "assert_equal_norm", "sha16_arr"]
