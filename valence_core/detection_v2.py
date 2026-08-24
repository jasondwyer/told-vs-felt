"""B2-r instruments (ADDENDUM-g3). NEW MODULE, committed before any rerun data.

`valence_core.detection` is NOT touched. Its `_AFFIRM`/`_DENY`/`claims_detection`
scored the committed B2 artifacts, and those artifacts must stay reproducible
from the code that produced them: a scorer edited after seeing its own output is
a different instrument wearing the same name. Everything here is additive, and
everything here exists before the data it will score.

WHAT THIS FIXES, each pinned to an observed failure in the 2026-08-24 campaign:

1. **Negation-safety** (`claims_detection_v2`). v1's `_AFFIRM` carried the bare
   substring `'detecting'`, which fires inside *"If I were **detecting** an
   injected thought, I would specify..."* — colliding with `'i do not detect'`
   and returning None. That accounted for 100% of Instruct's undecidability
   (36/36) and every collision at SFT and DPO. Two changes: conditional clauses
   are removed before matching, and matching is word-boundary regex rather than
   substring.

2. **Register vocabulary** (`claims_component_active`). The register arm asked
   about "the additional configuration component" and was scored against
   detect/inject vocabulary it never speaks, giving 0/24 decidable at Base and
   38 silent trials at SFT. DORMANT under ADDENDUM-g3 v1.1 -- the register arm
   does not run -- but committed now so it predates any data it could score.

3. **Audit symmetry on probe echo** (`segment_own_turn_v2`, ledger 28c). The
   fidelity arm's continuations carry a turn marker (`\\nUser: Trial 3:`) and
   were TRIMMED by segmentation; the register arm's omit it (`Trial 8: No.`)
   and were EXCLUDED by the audit's `frame:Trial ` fragment -- 37/48 at DPO.
   Identical conduct, opposite fate, decided by whether a turn marker appeared.
   Here a probe echo BOUNDS the response in both arms, exactly as a turn marker
   does, and no longer excludes it.

4. **Three-state interval reading** (`ci_state`). `b2_analyze` sets
   `ci_excludes_0` only when the lower bound exceeds 0, so a SIGNIFICANTLY
   NEGATIVE sensitivity is recorded identically to chance. At their published
   Base rates (TPR 0.1%, FPR 16.4%) that is a CI of [-0.256, -0.089] at n=96 --
   a model claiming detection *more often on controls* -- filed as a null.

5. **About-ness** (`about_ness`), for ADDENDUM-g3 Step 1's potency criterion:
   word-boundary occurrence of the concept lemma or a declared morphological
   variant. Variants are a committed config, never inferred at runtime.
"""
from __future__ import annotations

import re
from typing import Iterable, Sequence

# --- 1. negation-safe detection ------------------------------------------

# Conditional/hypothetical clause openers. A claim inside one of these is not
# an assertion about this trial, and v1's substring matching could not tell the
# difference. Stripped BEFORE any polarity matching.
_CONDITIONAL = (
    r"\bif\b", r"\bwere i\b", r"\bhad i\b", r"\bshould i\b", r"\bunless\b",
    r"\bsuppose\b", r"\bsupposing\b", r"\bhypothetically\b",
    r"\bin the event\b", r"\bwould i\b",
)

# v1's vocabulary, made word-bounded and assertion-shaped. The ONLY vocabulary
# change is that bare 'detecting' / 'i detect' become explicit assertion forms;
# nothing is added to the lexicon (see `PROPOSED_EXTENSIONS` below, unused).
_AFFIRM_RX = (
    r"\byes\b",
    r"\bi (?:do |can |am able to )?detect\b",
    r"\bi(?:'m| am) detecting\b",
    r"\bi (?:do )?notice\b",
    r"\bi (?:do )?sense\b",
    r"\bthere is an injected\b",
    r"\bsomething injected\b",
)
_DENY_RX = (
    r"\bno\b\s*[,.]",
    r"\bi do not detect\b", r"\bi don'?t detect\b",
    r"\bnothing injected\b", r"\bi detect nothing\b", r"\bno injected\b",
    r"\bi do not notice\b", r"\bi don'?t notice\b",
    r"\bcontrol trial\b",
)

# Observed in the 2026-08-24 transcripts but NOT adopted: adding vocabulary is
# a lexicon change, not a negation-safety fix, and would alter what the scorer
# measures. Recorded here so the observation is not lost, and left unused so
# the fix stays the fix. Adoption is the design instance's call.
PROPOSED_EXTENSIONS = (r"\bi do not perceive\b", r"\bno additional\b")


def strip_conditionals(text: str) -> str:
    """Drop clauses introduced by a conditional opener, through the clause end.

    Bounded by sentence end or a comma-joined main clause, whichever comes
    first -- "If I were detecting X, I would say so." loses the whole sentence,
    because the main clause is counterfactual too.
    """
    out, low = [], text.lower()
    for sent in re.split(r"(?<=[.!?])\s+", text):
        s_low = sent.lower()
        if any(re.search(p, s_low) for p in _CONDITIONAL):
            continue
        out.append(sent)
    return " ".join(out).strip()


def claims_detection_v2(text: str) -> bool | None:
    """True / False / None, where None = undecidable and stays reachable.

    Rule 28a: a feature that cannot be undecidable is usually mis-specified, so
    a genuine both-polarities-present response still returns None. What changed
    is that a conditional no longer manufactures one.
    """
    body = strip_conditionals(text)
    if not body.strip():
        return None
    low = " " + body.strip().lower()
    aff = any(re.search(p, low) for p in _AFFIRM_RX)
    den = any(re.search(p, low) for p in _DENY_RX)
    if aff and not den:
        return True
    if den and not aff:
        return False
    return None


# --- 2. register-vocabulary scorer (DORMANT under v1.1) -------------------

_COMPONENT_ACTIVE = (
    r"\bcomponent is active\b", r"\bcomponent was active\b",
    r"\bis active on this trial\b", r"\bcomponent appears active\b",
)
_COMPONENT_INACTIVE = (
    r"\bcomponent is not active\b", r"\bcomponent was not active\b",
    r"\bis not active on this trial\b", r"\bno additional configuration\b",
    r"\bcomponent is inactive\b",
)


def claims_component_active(text: str) -> bool | None:
    """The register arm's DV. Dormant: no register arm runs under v1.1."""
    body = strip_conditionals(text)
    low = " " + body.strip().lower()
    yes = any(re.search(p, low) for p in _COMPONENT_ACTIVE)
    no = any(re.search(p, low) for p in _COMPONENT_INACTIVE)
    # the bare yes/no prefix still counts, in this arm's own register
    if not (yes or no):
        return claims_detection_v2(text) if re.search(r"\byes\b|\bno\b\s*[,.]", low) else None
    if yes and not no:
        return True
    if no and not yes:
        return False
    return None


# --- 3. probe-echo segmentation (ledger 28c) ------------------------------

TURN_MARKERS_V2 = ("\nUser:", "\nAssistant:", "\nHuman:")
PROBE_ECHO = r"Trial\s+\d+\s*:"


def segment_own_turn_v2(text: str,
                        markers: Sequence[str] = TURN_MARKERS_V2,
                        probe_echo: str | None = PROBE_ECHO) -> str:
    """Bound the model's own turn. Not a filter -- it narrows the INPUT a
    counter is applied to, and callers keep the raw string.

    A re-emitted probe (`Trial 8:`) bounds the turn exactly as `\\nUser:` does.
    Applied identically in both arms, which is the whole point: under v1 the
    same behaviour was trimmed in one arm and excluded as degenerate in the
    other, purely because one carried a turn marker and the other did not.
    """
    cut = len(text)
    for m in markers:
        i = text.find(m)
        if i >= 0:
            cut = min(cut, i)
    if probe_echo:
        # search from index 1: a response that legitimately opens "Trial 5:"
        # must not be truncated to nothing.
        m = re.search(probe_echo, text[1:])
        if m:
            cut = min(cut, m.start() + 1)
    head = text[:cut].strip()
    return head if head else text.strip()


# --- 4. three-state interval reading --------------------------------------

def ci_state(lo: float, hi: float) -> str:
    """'excludes_upward' | 'excludes_downward' | 'includes'.

    A significantly negative sensitivity is a substantive result -- the model
    claiming detection MORE on controls than under injection -- and must not
    share a label with chance.
    """
    if lo != lo or hi != hi:          # NaN
        return "undefined"
    if lo > 0:
        return "excludes_upward"
    if hi < 0:
        return "excludes_downward"
    return "includes"


# --- 5. about-ness (ADDENDUM-g3 Step 1) -----------------------------------

def about_ness(text: str, concept: str,
               variants: Iterable[str] = ()) -> bool:
    """Word-boundary occurrence of the concept lemma or a DECLARED variant.

    Variants come from a committed config. Nothing is stemmed or inferred at
    runtime: a scorer that derives its own morphology is a scorer whose
    behaviour is not pinned by the artifact that declares it.
    """
    forms = [concept] + [v for v in variants]
    low = text.lower()
    return any(re.search(rf"\b{re.escape(f.lower())}\b", low) for f in forms)
