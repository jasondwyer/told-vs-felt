"""Ledger 26 -- the refactor regression law.

Two tiers, because they have different costs and different failure meanings:

- `analysis` (this package, no model): published numbers recomputed from
  committed artifacts through the new core. Runs in under a second on any
  machine with the repo checked out, including the box before a checkpoint
  is downloaded. Fails loudly if a statistical port drifted.
- `oracle` (needs the Qwen model on the laptop): the three criteria named
  in CLAUDE.md §Phase 0 step 1 -- g1r kernel-gate KLs, a 128-context B2b
  subsample, and e2a choice-read construction KL = 0.0 exactly.

Rule 26's disposition clause applies to both: a mismatch is a refactor bug
until proven otherwise. Nothing here is permitted to "explain" a difference.
"""

from __future__ import annotations

__all__ = ["analysis"]
