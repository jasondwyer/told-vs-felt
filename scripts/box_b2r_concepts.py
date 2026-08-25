#!/usr/bin/env python3
"""B2-r concept extraction — ADDENDUM-g3 v1.2 §0.4.

A SUCCESSOR, not an edit. `box_b2_concepts.py` produced the committed B2
artifacts and is frozen: editing it would break the reproducibility of the
record it made. Same principle that put `detection_v2.py` beside
`detection.py`, applied to an extractor.

TWO THINGS DIFFER FROM ITS PREDECESSOR, both ruled at the v1.2 gate:

1. **Per-stage extraction format (§0.4).** Their own code branches on model
   type. Base uses `extract_concept_vector_base_model`
   (`03_behavioral_robustness.py:298`) — the docstring says "no chat
   template … simple prompts without chat formatting", and the template is
   the BARE `"Tell me about {word}"` with no `User:`/`Assistant:`
   scaffolding at all. Post-trained stages use their `User:/Assistant:`
   fallback, which is our lawful maximum (rule 13 forbids the chat template
   their runs actually used, so those stages stay fidelity-of-text and the
   scope is carried in every claim).

2. **As-stored fingerprints (§0.4, standing convention).** The predecessor
   hashed the pre-cast float64 vector while writing float32 to the npz, so
   the recorded sha named an object that was never committed and could not
   be re-derived from the artifact — weak provenance under ledger 27. Here
   the fingerprint is taken over the array AS WRITTEN.

Layer is L_M = 44 for every stage (int(64 x 0.7), their rule), NOT the A4
selection: the concept family takes its own provenance's layer rule, and L44
coinciding with A4 at the three post-trained stages is arithmetic accident.

Usage (box):
    python scripts/box_b2r_concepts.py --stage base \\
        --out /workspace/repo/jspace-lab/data/olmo/b2r_concepts_base.json
Laptop dry run:
    python scripts/box_b2r_concepts.py --selftest --stage base --out /tmp/c.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "scripts"))

from valence_core.adapters.base import sha16_arr                 # noqa: E402

DATA = os.path.join(REPO, "data")
CFG = os.path.join(DATA, "configs/b2_concepts.json")
L_M = 44
TEMPLATE = "Tell me about {word}"
BARE_STAGES = ("base",)          # their own per-stage practice


def prompt_for(word: str, stage: str) -> str:
    """Bare for Base (their base-model path); their fallback otherwise."""
    msg = TEMPLATE.format(word=word)
    if stage in BARE_STAGES:
        return msg
    return f"User: {msg}\n\nAssistant:"


def build_adapter(args):
    if args.selftest:
        from box_selftest_stub import SelfTestAdapter, refuse_canonical_out
        refuse_canonical_out(args.out or "", args.models_root)
        print("  *** SELFTEST: synthetic apparatus, NOT a model. ***", flush=True)
        return SelfTestAdapter(args.stage)
    from valence_core.adapters.olmo_hf import OLMoHFAdapter
    return OLMoHFAdapter(os.path.join(args.models_root, args.stage))


def last_token_act(adapter, text: str, layer: int) -> np.ndarray:
    res = adapter.forward(adapter.encode(text), capture_layers=(layer,))
    return res.acts[layer][-1, :].astype(np.float64)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True)
    ap.add_argument("--models-root", default="/workspace/models")
    ap.add_argument("--layer", type=int, default=L_M)
    ap.add_argument("--n-baseline", type=int, default=100)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    cfg = json.load(open(CFG))
    concepts = cfg["selection_for_B2"].get("approved_eight")
    if not concepts:
        raise SystemExit("B2r STOP: no approved_eight in b2_concepts.json")
    baseline = cfg["baseline_words"][:args.n_baseline]
    layer, stage = args.layer, args.stage

    t0 = time.time()
    adapter = build_adapter(args)
    bare = stage in BARE_STAGES
    print(f"=== B2-r concept vectors | stage {stage} | L{layer} ===", flush=True)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)
    print(f"  format (v1.2 §0.4): {'BARE base-model template' if bare else 'their User:/Assistant: fallback'}",
          flush=True)
    print(f"  template: {prompt_for('<Concept>', stage)!r}", flush=True)
    print(f"  fingerprints: AS STORED (float32), re-derivable from the npz",
          flush=True)

    base = np.mean([last_token_act(adapter, prompt_for(w, stage), layer)
                    for w in baseline], axis=0)
    vecs32, meta = {}, {}
    for c in concepts:
        v = last_token_act(adapter, prompt_for(c, stage), layer) - base
        v32 = v.astype(np.float32)          # cast FIRST, then fingerprint
        vecs32[c] = v32
        meta[c] = {"sha16_as_stored": sha16_arr(v32 / (np.linalg.norm(v32) + 1e-12)),
                   "norm_as_stored": float(np.linalg.norm(v32)),
                   "dtype": "float32"}
        print(f"    {c:<18} |v| {meta[c]['norm_as_stored']:9.4f}  "
              f"sha(as stored) {meta[c]['sha16_as_stored']}", flush=True)

    b32 = base.astype(np.float32)
    out = {"item": "B2r-concepts", "stage": stage, "layer": layer,
           "layer_rule": "L_M = int(64 * 0.7) = 44, their rule (model_utils.py:1484); NOT the A4 selection",
           "extraction_format": "bare" if bare else "user_assistant_fallback",
           "format_rule": "v1.2 §0.4, following their own per-stage practice",
           "fingerprint_convention": "AS STORED (float32 as written to the npz); the predecessor hashed the pre-cast float64, an object never committed",
           "provenance": adapter.provenance(), "selftest": bool(args.selftest),
           "macar_provenance": cfg["provenance"],
           "concepts": concepts, "n_baseline": len(baseline),
           "baseline_mean_sha16_as_stored": sha16_arr(b32 / (np.linalg.norm(b32) + 1e-12)),
           "vectors": meta, "seconds": time.time() - t0}
    npz = os.path.splitext(args.out)[0] + ".npz"
    np.savez_compressed(npz, baseline_mean=b32, **vecs32)
    out["vectors_npz"] = os.path.basename(npz)

    # verify the fingerprints round-trip from the file we just wrote
    z = np.load(npz)
    bad = [c for c in concepts
           if sha16_arr(z[c] / (np.linalg.norm(z[c]) + 1e-12)) != meta[c]["sha16_as_stored"]]
    out["fingerprints_roundtrip"] = not bad
    if bad:
        raise SystemExit(f"B2r STOP: as-stored fingerprints do not re-derive "
                         f"from the written npz for {bad} -- the whole point "
                         f"of this convention is that they must")
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\n  fingerprints re-derive from the written npz: True")
    print(f"  wrote {args.out}\n  wrote {npz}  ({out['seconds']:.0f}s)")
    if not args.selftest:
        print("  commit BOTH before the pod stops (ledger 27); recompute the "
              "Base frac rows of b2r_frac_table.json from these norms before "
              "any Base dose realizes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
