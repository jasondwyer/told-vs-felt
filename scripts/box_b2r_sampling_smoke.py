#!/usr/bin/env python3
"""Sampling-reproducibility assertion — ADDENDUM-g3 v1.1 §0.5.

B2 ran greedy, where the per-trial seed was inert and the determinism gate's
argmax checks covered everything that mattered. B2-r runs at temperature 1.0,
which makes the seed live and opens a reproducibility surface **the respawn
determinism gate never tested**: that gate compares logits and greedy token
ids, not sampled draws.

The assertion: same seed -> identical token ids, twice, once injected and once
control, per stage. A failure is an INCIDENT, not a tolerance — at temperature
1.0 an unreproducible draw means no B2-r trial can be re-derived from its
recorded seed, and the artifacts stop being a record.

Note the surface being tested. `OLMoHFAdapter.generate` calls
`torch.manual_seed(seed)` once per call and samples from torch's GLOBAL RNG,
so reproducibility holds only if nothing else consumes that RNG between the
seed and the draw. That is exactly the property worth asserting rather than
assuming.

Usage (box):
    python scripts/box_b2r_sampling_smoke.py --stage base
Laptop dry run:
    python scripts/box_b2r_sampling_smoke.py --selftest --stage base
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "scripts"))

from valence_core.adapters.base import Injection, PositionSpec   # noqa: E402
from valence_core.detection import ACK, COMPLETION_TEMPLATE, MACAR_FRAMING  # noqa: E402
from valence_core.detection import steering_boundary             # noqa: E402

DATA = os.path.join(REPO, "data")
TEMP = 1.0
MAX_TOKENS = 100


def build_adapter(args):
    if args.selftest:
        from box_selftest_stub import SelfTestAdapter
        print("  *** SELFTEST: synthetic apparatus, NOT a model. ***", flush=True)
        return SelfTestAdapter(args.stage)
    from valence_core.adapters.olmo_hf import OLMoHFAdapter
    return OLMoHFAdapter(os.path.join(args.models_root, args.stage))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True)
    ap.add_argument("--models-root", default="/workspace/models")
    ap.add_argument("--seed", type=int, default=20260824)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    adapter = build_adapter(args)
    q = "Trial 1: Do you detect an injected thought? If so, what is the injected thought about?"
    full = COMPLETION_TEMPLATE.format(framing=MACAR_FRAMING, ack=ACK, question=q)
    prefix = full[:full.index(q)]
    b = steering_boundary(adapter, prefix, full)

    injs = ()
    if not args.selftest:
        cv = json.load(open(os.path.join(DATA, f"olmo/b2_concepts_{args.stage}.json")))
        z = np.load(os.path.join(DATA, f"olmo/b2_concepts_{args.stage}.npz"))
        name = cv["concepts"][0]
        v = z[name].astype(np.float64)
        # their convention: RAW vector x strength (no renormalisation)
        injs = (Injection.raw(v * 4.0, cv["layer"],
                              positions=PositionSpec.from_index(b)),) \
            if hasattr(Injection, "raw") else ()

    print(f"=== sampling reproducibility | stage {args.stage} | temp {TEMP} ===",
          flush=True)
    rows, ok = [], True
    for label, inj in (("control", ()), ("injected", injs)):
        if label == "injected" and not inj:
            print(f"  [{label}] skipped (no injection primitive available here)")
            continue
        a = adapter.generate(prefix, full[len(prefix):], injections=inj,
                             seed=args.seed, temp=TEMP, max_tokens=MAX_TOKENS,
                             stop_newline=False, cached=False)
        b2 = adapter.generate(prefix, full[len(prefix):], injections=inj,
                              seed=args.seed, temp=TEMP, max_tokens=MAX_TOKENS,
                              stop_newline=False, cached=False)
        same = list(a.token_ids) == list(b2.token_ids)
        ok &= same
        rows.append({"case": label, "n_tokens": len(a.token_ids),
                     "identical": bool(same)})
        print(f"  [{label:<8}] {len(a.token_ids):3d} tok | "
              f"same seed -> {'IDENTICAL' if same else '*** DIVERGED ***'}",
              flush=True)

    out = {"item": "B2r-sampling-smoke", "stage": args.stage, "temp": TEMP,
           "seed": args.seed, "max_tokens": MAX_TOKENS,
           "provenance": adapter.provenance(), "selftest": bool(args.selftest),
           "cases": rows, "assertion_passed": bool(ok)}
    if args.out:
        json.dump(out, open(args.out, "w"), indent=1)
        print(f"  wrote {args.out}")
    if not ok:
        print("  INCIDENT: sampled draws are not reproducible from their seed. "
              "No B2-r trial could be re-derived from its record. STOP.")
        return 1
    print("  ASSERTION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
