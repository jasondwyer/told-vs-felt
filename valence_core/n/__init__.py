"""PROPOSAL-n -- the reconciliation unit's package (n v0.2 §8 step 6; the seat's answers of 2026-11-15, §5.1).

Built in order: ``schema`` first (the read runner's record schema, committed alone so that step 9's analyzer can be
built from it in parallel), then the rest of step 6 -- the OLMo 5(f) primitive (§2.2), the renderer of record, the
direction builders, the random-direction draws, the read runner with fidelity re-compute and capture-on, the
told-line variants, the verifier and the probe code for G-READ-n -- each importing ``valence_core.m``'s shared
modules and ``valence_core.adapters.olmo_hf`` unchanged.
"""
