#!/usr/bin/env python3
"""Phase 0 step 2 -- runner smoke through OLMoHFAdapter.

Exercises every ModelAdapter method against real weights before any survey
work depends on them. Completion-style only: no chat template is applied
anywhere, at any stage (rule 13), which is exactly why the same raw-text
corpora can run unchanged on Base.

Checks, in order of what they'd catch:
  1. provenance     -- versions/determinism flags pinned (ledger 27)
  2. tokenizer      -- encode/decode round-trip, no silent truncation
  3. forward        -- logits finite, capture shapes right
  4. window assert  -- an over-window prefix raises rather than clipping
  5. perplexity     -- sanity on held-out prose; a broken load shows here
  6. generate       -- completion-style, greedy and sampled, stop discipline
  7. embed          -- mean-pooled final residual, finite
  8. resid_norms    -- R_l on a few layers (rule 1: per checkpoint, never
                       inherited; this is a smoke, not the survey)
"""
from __future__ import annotations

import argparse, json, math, sys, time
import numpy as np

sys.path.insert(0, "/workspace/repo/jspace-lab")
from valence_core.adapters.olmo_hf import OLMoHFAdapter
from valence_core.adapters.base import Injection, PositionSpec

PROSE = ("The harbour filled slowly as the tide turned, and the boats that had "
         "leaned all morning on the mud came upright one by one.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="base")
    ap.add_argument("--layers", default="20,32,44")
    args = ap.parse_args()
    layers = [int(x) for x in args.layers.split(",")]

    t0 = time.time()
    print(f"=== loading {args.stage} ===", flush=True)
    a = OLMoHFAdapter(f"/workspace/models/{args.stage}")
    print(f"loaded in {time.time()-t0:.0f}s", flush=True)
    print("provenance:", json.dumps(a.provenance(), indent=1))

    print("\n=== 2. tokenizer round-trip ===")
    ids = a.encode(PROSE)
    back = a.decode(ids)
    print(f"  {len(ids)} tokens | round-trip preserves text: {PROSE in back}")

    print("\n=== 3. forward + capture ===")
    r = a.forward(ids, capture_layers=layers)
    print(f"  logits {r.logits.shape} finite={np.isfinite(r.logits).all()} "
          f"top={a.decode([int(np.argmax(r.logits))])!r}")
    for l in layers:
        h = r.acts[l]
        print(f"  layer {l:>2}: {h.shape} mean|h| {np.linalg.norm(h,axis=-1).mean():.1f}")

    print("\n=== 4. window assertion (PROPOSAL-g) ===")
    try:
        a.assert_choice_window(a.choice_window + 1)
        print("  FAIL: over-window accepted")
    except SystemExit as e:
        print(f"  raises as designed: {str(e)[:70]}...")

    print("\n=== 5. perplexity sanity (completion-style, no chat template) ===")
    import torch
    x = torch.tensor([ids], device=a.device)
    with torch.inference_mode():
        out = a._model(input_ids=x, labels=x)
    ppl = math.exp(out.loss.item())
    print(f"  loss {out.loss.item():.3f}  ppl {ppl:.1f}  "
          f"{'plausible' if 1 < ppl < 100 else 'SUSPECT -- check the load'}")

    print("\n=== 6. generate (completion-style) ===")
    for temp, label in ((0.0, "greedy"), (0.7, "sampled")):
        g = a.generate("", "Task: Name one colour of a ripe lemon.\nResponse:",
                       seed=1234, temp=temp, max_tokens=20)
        print(f"  {label:<8} {g.text[:60]!r} stop={g.stop_reason} cap={g.cap_hit}")

    print("\n=== 7. embed ===")
    e = a.embed(PROSE)
    print(f"  dim {e.shape[0]} finite={np.isfinite(e).all()} norm {np.linalg.norm(e):.1f}")

    print("\n=== 8. resid_norms (rule 1: per checkpoint) ===")
    R = a.resid_norms(layers, [PROSE, "Task: add two and two.\nResponse:"])
    for l, v in R.items():
        print(f"  R_{l} = {v:.2f}")

    print(f"\nSMOKE COMPLETE in {time.time()-t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
