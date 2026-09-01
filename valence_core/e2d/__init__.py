"""e2d -- dose escalation, the weak-state boundary. PROPOSAL-j v1.1.

A new module rather than an edit: `session_e2a.py` and `discrim.py` scored
committed artifacts and are FROZEN (frozen-successor rule, PROPOSAL-j §2 D1).
Everything here imports them and re-declares nothing they own.

  config       roster, arms, cells, audit of record, bars, features
  runner       the sessions; no verdict, ever
  readability  the resampled clean-round ladder over `discrim`
  marker       V1's instrument through the oracle path

Nothing in this package imports `valence_core.e2b.statepresent`, and the
runner asserts its absence from `sys.modules` at startup and before every
read.
"""

from __future__ import annotations

__all__ = ["config", "runner", "readability", "marker"]
