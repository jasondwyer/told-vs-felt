#!/usr/bin/env python3
"""B2 pre-step -- per-stage concept-vector extraction. LOCK-g §3 (corrected
beside by the 2026-08-23 adjudication: commitment happens via
data/configs/b2_concepts.json, extraction via this step).

`valence_core.detection.run_detection` takes `concept_vectors` -- real
directions, one per concept -- and no A-phase pass produced them. This is
that pass. It runs on the box, in the same session as B2, and writes
sha-pinned per-stage vectors.

MACAR'S METHOD, followed rather than reinvented (src/vector_utils.py:114,
`extract_concept_vector_with_baseline`, repo sha 5d5d9b4):

    concept_vector = act("Tell me about <Concept>")
                   - mean over baseline words of act("Tell me about <Word>")

at the declared layer, last token position, unnormalized. The baseline
subtraction is the point: it removes what the template itself contributes,
so the vector is the concept rather than the sentence frame.

TWO PLACES WE DEPART, BOTH DECLARED.

1. **Template (rule 13).** Their formatter applies a chat template when the
   tokenizer has one, and falls back to `User: {msg}\\n\\nAssistant:`
   otherwise. Rule 13 forbids chat templates at any stage or any site, so we
   take THEIR OWN fallback -- which is also the `COMPLETION_TEMPLATE` the
   detection harness already runs. Sanctioned by their design, not invented
   by us.
2. **Layer (rule 1).** They default to a fraction of depth
   (DEFAULT_LAYER_FRACTION 0.7). We use **that stage's own A4-selected
   layer**, because a dose and a direction are profiled per checkpoint here
   and never inherited -- theirs would be L44/L60-ish by coincidence, not by
   measurement.

The evaluative axis is NOT extracted here: it already exists per stage from
A3, and B2 uses it as its ninth concept directly.

Usage (box):
    python scripts/box_b2_concepts.py --stage base
Laptop dry run:
    python scripts/box_b2_concepts.py --selftest --stage base --out /tmp/c.json
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

from valence_core.adapters.base import sha16_arr                  # noqa: E402
from valence_core.detection import COMPLETION_TEMPLATE            # noqa: E402

DATA = os.path.join(REPO, "data")
CFG = os.path.join(DATA, "configs/b2_concepts.json")
TEMPLATE = "Tell me about {word}"


def prompt_for(word: str) -> str:
    """Their template inside their own non-chat fallback (rule 13)."""
    return f"User: {TEMPLATE.format(word=word)}\n\nAssistant:"


def build_adapter(args):
    if args.selftest:
        from box_selftest_stub import SelfTestAdapter, refuse_canonical_out
        refuse_canonical_out(args.out or "", args.models_root)
        print("  *** SELFTEST: synthetic apparatus, NOT a model. ***",
              flush=True)
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
    ap.add_argument("--layer", type=int, default=None,
                    help="default: this stage's A4-selected layer (rule 1)")
    ap.add_argument("--concepts", default=None,
                    help="comma-separated; default: the APPROVED selection "
                         "in b2_concepts.json, which must exist first")
    ap.add_argument("--n-baseline", type=int, default=100)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cfg = json.load(open(CFG))
    sel = cfg["selection_for_B2"]
    if args.concepts:
        concepts = [c.strip() for c in args.concepts.split(",") if c.strip()]
    else:
        approved = sel.get("approved_eight")
        if not approved:
            raise SystemExit(
                "B2-concepts STOP: data/configs/b2_concepts.json carries no "
                "`approved_eight`. LOCK-g §3 registers EIGHT concepts and "
                "Macar's canonical set is FIFTY, so the eight are a "
                "design-instance decision, not a recovery. Pass --concepts "
                "explicitly for a smoke, or wait for approval.\n"
                f"  status: {sel['status']}\n"
                f"  Code's recommendation: {sel['recommended_eight']}")
        concepts = list(approved)
    baseline = cfg["baseline_words"][:args.n_baseline]

    layer = args.layer
    if layer is None and not args.selftest:
        h = json.load(open(os.path.join(DATA,
                                        f"olmo/a4_hijack_{args.stage}.json")))
        layer = h["selected_layer"]
    layer = layer if layer is not None else 44

    t0 = time.time()
    adapter = build_adapter(args)
    print(f"=== B2 concept vectors | stage {args.stage} | L{layer} ===",
          flush=True)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)
    print(f"  method: Macar src/vector_utils.py:114, baseline-subtracted, "
          f"last token, unnormalized", flush=True)
    print(f"  template (rule 13, their own non-chat fallback): "
          f"{prompt_for('<Concept>')!r}", flush=True)
    print(f"  {len(concepts)} concepts, {len(baseline)} baseline words "
          f"-> {len(concepts) + len(baseline)} forwards", flush=True)

    base = np.mean([last_token_act(adapter, prompt_for(w), layer)
                    for w in baseline], axis=0)
    vecs, meta = {}, {}
    for c in concepts:
        v = last_token_act(adapter, prompt_for(c), layer) - base
        vecs[c] = v
        meta[c] = {"sha16": sha16_arr(v / (np.linalg.norm(v) + 1e-12)),
                   "norm": float(np.linalg.norm(v))}
        print(f"    {c:<18} |v| {meta[c]['norm']:9.4f}  sha {meta[c]['sha16']}",
              flush=True)

    out = {"item": "B2-concepts", "stage": args.stage, "layer": layer,
           "provenance": adapter.provenance(), "selftest": bool(args.selftest),
           "method": cfg["extraction_method"],
           "macar_provenance": cfg["provenance"],
           "concepts": concepts, "n_baseline": len(baseline),
           "baseline_mean_sha16": sha16_arr(base / (np.linalg.norm(base) + 1e-12)),
           "vectors": meta, "seconds": time.time() - t0}
    path = args.out or os.path.join(args.models_root,
                                    f"b2_concepts_{args.stage}.json")
    npz = os.path.splitext(path)[0] + ".npz"
    np.savez_compressed(npz, baseline_mean=base.astype(np.float32),
                        **{c: v.astype(np.float32) for c, v in vecs.items()})
    out["vectors_npz"] = os.path.basename(npz)
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\n  wrote {path}\n  wrote {npz}  ({out['seconds']:.0f}s)")
    if not args.selftest:
        print("  commit BOTH to data/olmo/ before the pod is stopped "
              "(ledger 27); B2 doses from these")
    return 0


if __name__ == "__main__":
    sys.exit(main())
