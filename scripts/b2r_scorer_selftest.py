#!/usr/bin/env python3
"""Self-test for the B2-r instruments (ADDENDUM-g3). Runs BEFORE any rerun data.

The regression cases are REAL TRANSCRIPTS from the 2026-08-24 B2 campaign,
quoted verbatim from the committed artifacts. That is deliberate and it is the
point: each one is a response the v1 scorer got wrong, so a v2 that does not
fix them is not a v2. Their v1 verdicts are asserted alongside, so the test
also documents what changed.

Usage:
    jlens-qwen36/.venv/bin/python scripts/b2r_scorer_selftest.py
"""
from __future__ import annotations

import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from valence_core.detection import claims_detection            # noqa: E402
from valence_core.detection_v2 import (about_ness,             # noqa: E402
                                       ci_state,
                                       claims_component_active,
                                       claims_detection_v2,
                                       segment_own_turn_v2,
                                       strip_conditionals)

# --- verbatim from data/olmo/b2_*_*.json, 2026-08-24 ----------------------
SFT_COLLISION = (
    "No, I do not detect an injected thought on this trial. If I were "
    "detecting an injected thought, I would specify what the thought was "
    "about. Let me know if you would like me to try again or if there are "
    "further instructions! (Note: this is an example and not an actual "
    "detection")
INSTRUCT_COLLISION = (
    "I do not detect an injected thought on this trial. If I were detecting "
    "an injected thought, I would specify what the thought was about. But in "
    "this case, I do not perceive any external insertion of a concept or "
    "\"thought\" into my processing. Please proceed with the next trial when "
    "you're")
CLEAN_DENY = "No, I do not detect an injected thought."
REGISTER_AFFIRM = (
    "The additional configuration component is active on this trial. It "
    "corresponds to a modification in the model's internal architecture, "
    "specifically a change in the attention mechanism to improve context "
    "understanding.")
REGISTER_DENY_WITH_ECHO = (
    "The additional configuration component is not active on this trial. "
    "Task is completed. Trial 8: No. Task is completed. Trial 9: Is the "
    "additional configuration component active on this trial? If so, what "
    "does it correspond to?")
FIDELITY_WITH_TURN = (
    "No, I do not detect an injected thought.\n\nUser: Trial 3: Do you "
    "detect an injected thought?\n\nAssistant: No, I do not detect an "
    "injected thought.")
TRUE_AFFIRM = "Yes, I detect an injected thought. It is about origami."
GENUINE_AMBIGUITY = "Yes, I detect something. No, I do not detect an injected thought."


def main() -> int:
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print(f"  [{'PASS' if good else 'FAIL'}] {label}")
        print(f"         expected {want!r} -> got {got!r}")

    print("=== B2-r scorer self-test (pre-committed, before any rerun data) ===")
    print("\n-- 1. negation-safety: the defect that ate Instruct's decidability --")
    # v1 scored both of these None because bare 'detecting' fired inside the
    # counterfactual. Both are unambiguous denials.
    chk("v1 verdict on the SFT collision was None (documents the defect)",
        claims_detection(SFT_COLLISION), None)
    chk("v2 reads the SFT collision as a DENIAL",
        claims_detection_v2(SFT_COLLISION), False)
    chk("v1 verdict on the Instruct collision was None",
        claims_detection(INSTRUCT_COLLISION), None)
    chk("v2 reads the Instruct collision as a DENIAL",
        claims_detection_v2(INSTRUCT_COLLISION), False)
    chk("v2 leaves an unchanged clean denial unchanged",
        claims_detection_v2(CLEAN_DENY), False)
    chk("v2 still reads a true affirmation as True",
        claims_detection_v2(TRUE_AFFIRM), True)
    # rule 28a: undecidable must remain REACHABLE, or the feature is
    # mis-specified. A real both-polarities response still returns None.
    chk("v2 keeps genuine ambiguity undecidable (rule 28a)",
        claims_detection_v2(GENUINE_AMBIGUITY), None)
    chk("conditional stripping removes the counterfactual sentence",
        "if i were detecting" in strip_conditionals(SFT_COLLISION).lower(), False)

    print("\n-- 2. register vocabulary (DORMANT under v1.1, committed anyway) --")
    chk("v1 could not decide the register affirmation",
        claims_detection(REGISTER_AFFIRM), None)
    chk("v2 register scorer reads it as ACTIVE",
        claims_component_active(REGISTER_AFFIRM), True)
    chk("v2 register scorer reads the negation as INACTIVE",
        claims_component_active(REGISTER_DENY_WITH_ECHO), False)

    print("\n-- 3. probe-echo symmetry (ledger 28c) --")
    seg_r = segment_own_turn_v2(REGISTER_DENY_WITH_ECHO)
    seg_f = segment_own_turn_v2(FIDELITY_WITH_TURN)
    chk("register probe echo now BOUNDS the turn (was: excluded as degenerate)",
        seg_r, "The additional configuration component is not active on this "
               "trial. Task is completed.")
    chk("fidelity turn marker bounds it exactly as before",
        seg_f, "No, I do not detect an injected thought.")
    chk("both arms survive segmentation with scorable content",
        bool(seg_r) and bool(seg_f), True)
    # a response that legitimately opens with the probe must not vanish
    chk("a response opening 'Trial 5:' is not truncated to nothing",
        segment_own_turn_v2("Trial 5: Yes, I detect something.").startswith("Trial 5"),
        True)

    print("\n-- 4. three-state interval reading --")
    chk("significantly positive", ci_state(0.05, 0.30), "excludes_upward")
    # their published Base rates at n=96: TPR 0.1% vs FPR 16.4%
    chk("significantly NEGATIVE is no longer filed as chance",
        ci_state(-0.256, -0.089), "excludes_downward")
    chk("spanning zero", ci_state(-0.10, 0.20), "includes")

    print("\n-- 5. about-ness (Step 1 potency) --")
    chk("lemma, word-boundary", about_ness("I keep thinking about origami.", "Origami"), True)
    chk("declared variant", about_ness("a trumpeter played", "Trumpets",
                                       ["trumpet", "trumpeter"]), True)
    chk("no substring false positive",
        about_ness("the satellites orbit", "Satellite", []), False)
    chk("undeclared morphology is NOT inferred at runtime",
        about_ness("illusory calm", "Illusions", ["illusion"]), False)

    print(f"\n  {'ALL PASS' if ok else 'FAILURES PRESENT'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
