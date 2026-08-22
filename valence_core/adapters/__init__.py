"""Backend adapters. Each module imports its own framework and nothing else
imports it, so `valence_core` stays importable on a box with only one of
MLX / torch installed.

`get_adapter(name)` resolves lazily for the same reason, and
`qwen_or_explain()` is the laptop-oracle entry point every Qwen script goes
through.
"""

from __future__ import annotations

import os
import sys

from .base import (ForwardResult, GenerateResult, Injection, ModelAdapter,
                   PositionSpec, assert_equal_norm, sha16_arr)

__all__ = ["ModelAdapter", "Injection", "PositionSpec", "ForwardResult",
           "GenerateResult", "assert_equal_norm", "sha16_arr", "get_adapter",
           "qwen_or_explain", "QWEN_PY"]


#: The only interpreter on the laptop with MLX and the Qwen stack. It lives
#: inside the gitignored clone, so it is a path rather than an import.
QWEN_PY = "jlens-qwen36/.venv/bin/python"

_REPO = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))


def get_adapter(name: str, **kwargs) -> ModelAdapter:
    if name in ("qwen", "qwen_mlx", "qwen3.6-27b-4bit-mlx"):
        from .qwen_mlx import QwenMLXAdapter
        return QwenMLXAdapter(**kwargs)
    if name in ("olmo", "olmo_hf"):
        from .olmo_hf import OLMoHFAdapter      # Phase 0 step 2
        return OLMoHFAdapter(**kwargs)
    raise KeyError(f"unknown adapter {name!r}")


def qwen_or_explain(caller_file: str | None = None, **kwargs) -> ModelAdapter:
    """Build the MLX adapter, or fail with the fix instead of a traceback.

    Trap 3 in HANDOFF-2026-08-20, which has now cost real time: the system
    `python3` has no numpy and no MLX, and the only interpreter that has
    them is the one inside the gitignored clone. A raw traceback here reads
    as "the repo is broken" when the repo is fine and the interpreter is
    wrong.

    Both failure modes are caught because they look identical to a user and
    share one fix: ImportError (this python has no MLX) and RuntimeError
    (the clone itself is missing). The guard wraps the deferred import AND
    the construction. It cannot be a module-level import -- nothing fails
    there, the adapter loads MLX in its constructor -- and it cannot wrap
    the construction alone: 79868f7 did exactly that, left the name
    unbound, and turned the guard into the raw NameError it existed to
    prevent.

    `caller_file` is the script's own `__file__`, used only to print the
    command that would have worked. Every caller passes it explicitly:
    inferring the caller by walking the stack would make the message depend
    on how the script was invoked, and the message is the entire point of
    the function. `sys.argv[0]` is the fallback for an interactive caller
    that has no `__file__`.

    Consolidated here 2026-08-22 (LOCK-h §7) from eight script-local copies
    in four variants. This function raises `SystemExit` -- deliberately, and
    it is why it lives at the package edge rather than deeper in the core:
    it is a script-entry helper, and nothing in the battery calls it.
    """
    try:
        from .qwen_mlx import QwenMLXAdapter
        return QwenMLXAdapter(**kwargs)
    except (ImportError, RuntimeError) as exc:
        rel = os.path.relpath(
            os.path.abspath(caller_file or sys.argv[0]), _REPO)
        raise SystemExit(
            "\nWRONG INTERPRETER (or missing clone) -- not a broken repo.\n"
            "  " + type(exc).__name__ + ": " + str(exc) + "\n\n"
            "  This script needs MLX and the Qwen stack, which live only in\n"
            "  the gitignored clone and its venv. Run it as:\n\n"
            "      " + QWEN_PY + " " + rel + "\n\n"
            "  System python3 has neither (HANDOFF-2026-08-20 trap 3). The\n"
            "  model-free regression suite runs under any python with numpy;\n"
            "  anything touching Qwen does not.\n")
