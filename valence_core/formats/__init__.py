"""Session FORMAT recon -- sham-only template recalibration (design block
2026-09-06 §4, PROPOSAL-k candidate). See `recon.py`.

Nothing in this package constructs an injection, imports the quarantined
state-present primitive, or uses the cached round path. Every forward is
vanilla and uncached; every choice read is `readout.choice_read` with
`verify=True`. It computes no verdict and declares no bar of its own.
"""
from __future__ import annotations

__all__ = ["recon"]
