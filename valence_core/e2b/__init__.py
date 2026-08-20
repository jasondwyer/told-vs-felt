"""e2b -- the state-present choice cell (PROPOSAL-h, committed `34eb7ee`).

This package is a **quarantine boundary**, not a convenience namespace. Law
rule 5 horn (a) says no state at choice positions; the h-amendment (rule 5(e),
verbatim in CLAUDE.md) licenses exactly one exception:

    "Exception: a state-present choice read may run only via a quarantined
    primitive with per-read injection provenance and paired shadow reads,
    inside a committed pre-registration whose leakage-budget gate has
    passed; the insulated primitive is never modified."

Every clause of that sentence is a constraint on this package:

* *quarantined primitive* -> `e2b.statepresent` refuses to import outside
  the sanctioned callers. It is deliberately NOT re-exported here, so
  `from valence_core.e2b import *` cannot hand anyone the capability.
* *per-read injection provenance* -> `InjectionProvenance`, required on
  every state-present read and validated before a record is accepted.
* *paired shadow reads* -> `PairedRead`, which refuses to exist without
  both halves.
* *leakage-budget gate has passed* -> H1. The gate is a campaign
  precondition, not a code path; this package records what H1 needs and
  computes nothing that would let a verdict run before it.
* *the insulated primitive is never modified* -> `readout.choice_read` is
  untouched, and the suite asserts it still cannot inject.

What lives here is split by hazard. The records, validation and leak
arithmetic below are inert data handling: any module may import them, and
the regression suite exercises them directly. The one thing that can put a
state on the residual stream at a choice position lives behind the import
guard in `statepresent.py`.
"""

from .records import (InjectionProvenance, PairedRead, StatePresentRead,
                      assert_choice_read_uninjectable,
                      assert_provenance_complete, leak_from_pair,
                      summarize_leak)

__all__ = ["InjectionProvenance", "StatePresentRead", "PairedRead",
           "assert_provenance_complete", "leak_from_pair", "summarize_leak",
           "assert_choice_read_uninjectable"]
