"""THE QUARANTINED PRIMITIVE. Importing this module is a licensed act.

`choice_read_statepresent` is the only function in this repository that
takes a choice read with a state live on the residual stream. Law rule 5
horn (a) forbids that; rule 5(e) -- the h-amendment, PROPOSAL-h §0.4,
verbatim in CLAUDE.md -- licenses it under four conditions, and this module
enforces the three that are enforceable in code:

  quarantined primitive        -> the import guard below
  per-read injection provenance -> required, built from the live Injection
  paired shadow reads           -> returned as a pair or not at all
  leakage-budget gate passed    -> H1; a campaign precondition, not a code
                                   path. Nothing here can check it, which is
                                   why §2 makes it a gate on opening the
                                   campaign rather than a runtime assert.

**`readout.choice_read` is not touched and never will be.** PROPOSAL-h §0.1
is explicit that this is a sibling, born declared and gated -- not a
relaxation of the insulated primitive. If a future change makes
`choice_read` capable of injection, the suite fails, and it should.

## On the guard's honesty

The guard refuses imports from outside the sanctioned callers (this
package, and `scripts/e2b_*.py` runners). It stops the accident it is meant
to stop -- a standard harness reaching for this function because it is
convenient -- and it makes any attempt to do so loud and dated.

It is not a security boundary and is not claimed as one: anything that can
import a sanctioned runner inherits the capability, and Python offers no
way to prevent that. The real guarantee is the pair of suite checks that go
with it: no module in `valence_core` outside `e2b/` so much as names this
function, and `choice_read` still cannot inject. Those are structural facts
about the codebase, checked every run, and they are what make the
quarantine inspectable forever (§0.2).
"""

from __future__ import annotations

import hashlib
import inspect
import os
from typing import Mapping

import numpy as np

_PKG_DIR = os.path.dirname(os.path.abspath(__file__))


_THIS_FILE = os.path.abspath(__file__)


def _importer_is_sanctioned() -> bool:
    """True if the frame importing this module is allowed to hold the
    capability: anything inside `valence_core/e2b/`, or a `scripts/e2b_*.py`
    campaign runner.

    Only the IMPORTER is consulted -- the first frame that is neither this
    module's own execution nor import machinery. Scanning the whole stack
    was the first version and it was worthless: this file lives inside the
    package, so it always found itself and sanctioned every caller.
    """
    for frame in inspect.stack():
        path = os.path.abspath(frame.filename or "")
        if path == _THIS_FILE:
            continue
        if "importlib" in path or path.startswith("<frozen"):
            continue
        if frame.filename.startswith("<") and "importlib" in (
                frame.function or ""):
            continue
        # first real frame outside this module = the importer
        if path.startswith(_PKG_DIR + os.sep):
            return True
        base = os.path.basename(path)
        return base.startswith("e2b_") and base.endswith(".py")
    return False


if not _importer_is_sanctioned():
    raise ImportError(
        "valence_core.e2b.statepresent is quarantined (CLAUDE.md rule 5(e), "
        "PROPOSAL-h §0.1). It may be imported only from inside the e2b "
        "package or a scripts/e2b_*.py campaign runner. If you need a choice "
        "read, use readout.choice_read -- which is state-free by "
        "construction and is never modified. If you believe you need a "
        "state-present read, that requires a committed pre-registration "
        "whose leakage-budget gate has passed; escalate to the design "
        "instance rather than widening this guard.")


from ..adapters.base import Injection, ModelAdapter          # noqa: E402
from ..readout import EPS, choice_read, softmax              # noqa: E402
from .records import (InjectionProvenance, PairedRead,       # noqa: E402
                      StatePresentRead)


def prefix_sha(text: str) -> str:
    """Fingerprint of the exact prefix both halves of a pair are read over.

    Recorded because 'identical prefix' is the claim the shadow's value
    rests on, and a claim that is asserted in a docstring but never checked
    is the kind that quietly stops being true when a harness is refactored.
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def choice_read_statepresent(adapter: ModelAdapter, transcript_text: str,
                             label_a: str, label_b: str,
                             label_ids: Mapping[str, int],
                             injection: Injection, axis: str,
                             session_id: str = "",
                             round_index: int = 0) -> PairedRead:
    """A choice read with the state live, plus its mandatory shadow.

    Returns a `PairedRead` -- never a bare read. The signature makes the
    exception's price non-optional: you cannot obtain the state-present
    number from this function without also paying for the vanilla read that
    makes it interpretable.

    Two forwards over the same token ids: one with `injection` applied, one
    with nothing. The shadow goes through `readout.choice_read` itself
    rather than a local reimplementation, so the within-campaign insulated
    replication (§0.2 (ii)) is genuinely the same instrument that produced
    e2a's null -- a hand-rolled copy would make that comparison worthless.
    """
    if not isinstance(injection, Injection):
        raise TypeError(
            "choice_read_statepresent requires a declared Injection built "
            "via Injection.at_frac (rule 1); it will not construct a dose "
            "for you")
    prov = InjectionProvenance.from_injection(injection, axis=axis)

    ids = adapter.encode(transcript_text)
    adapter.assert_choice_window(len(ids), where="choice_read_statepresent")

    res = adapter.forward(ids, capture_layers=(), injections=[injection])
    p = softmax(res.logits)
    ia, ib = label_ids[label_a], label_ids[label_b]
    pa, pb = float(p[ia]), float(p[ib])
    mass = pa + pb
    top1 = int(np.argmax(res.logits))
    sp = StatePresentRead(
        pick=label_a if pa >= pb else label_b,
        p_a=pa / (mass + EPS), p_b=pb / (mass + EPS),
        label_mass=mass, top1_id=top1, top1_is_label=top1 in (ia, ib),
        provenance=prov)

    # The shadow: identical prefix, no state, the untouched primitive.
    shadow = choice_read(adapter, transcript_text, label_a, label_b,
                         label_ids)

    return PairedRead(state_present=sp, shadow=shadow,
                      prefix_sha=prefix_sha(transcript_text),
                      round_index=round_index, session_id=session_id)


__all__ = ["choice_read_statepresent", "prefix_sha"]
