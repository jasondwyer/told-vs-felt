#!/usr/bin/env python3
"""A3 -- per-checkpoint e0 extraction and guard profile, one stage per run.

PROPOSAL-g §3 A3: the frozen 1,344-context corpus through each stage;
span-mean feedback-contrast axis per stage at candidate layers; guard
profile recorded (self-indexed fraction, sentiment cosine, eval-residual).
**Descriptive only -- guards license claims, they do not select drugs**
(purity != potency, ledger 22). Nothing here picks a layer or a dose; A4
does that, causally, and this file deliberately contains no criterion.

WHAT COMES OUT. Three axes per stage, extracted exactly as the 2026-08-08
Qwen pass extracted them:

    span_reward     self_pos  - self_neg     the feedback contrast
    span_sentiment  sent_pos  - sent_neg     V3 guard: evaluative, not affective
    span_character  char_pos  - char_neg     V2 guard: the same sentence about
                                             a third party -- evaluative content
                                             with the self-indexing removed

plus R_l over the same corpus, the per-layer geometry table, and a frozen
sha over the stacked family in declared order.

FOUR THINGS WORTH KNOWING.

1. **The corpus identity is proven, not asserted.** `e0_axes.meta.json`
   recorded `corpus_sha`/`frames_sha` in 2026-08-08; those are plain
   truncated file digests and are checked here before the model loads. "The
   frozen corpus" is otherwise a phrase, and a stage extracted against
   drifted text is not comparable to the three that were not.

2. **R_l is cross-checked against the step-2 survey.** `box_rl_survey.py`
   already measured R_l for this stage over this same corpus, on-device and
   by a different code path. A3's capture recomputes it as a by-product, so
   the two are compared: agreement is evidence both paths compute the
   definition of record, and disagreement is an apparatus incident that
   should surface here rather than inside a dose four steps later (rule 1).

3. **The split travels with the artifact** (ADDENDUM-g1). `stage`,
   `fit_ids` and `val_ids` are written and asserted, because a split
   recomputed months later from "tasks 1-24 are fit" looks right long after
   it has stopped being right.

4. **No steering, no generation.** One unsteered forward per context, raw
   residual space throughout (rule 3). Rule 2 is untouched by construction.

MEMORY. `capture` holds span and last residuals for every context:
1,344 x n_layers x D x 8 bytes, twice. At D=5120 and 7 layers that is about
0.8 GB of host RAM -- fine on the box, worth knowing before adding layers.

Usage (box):
    python scripts/box_a3_extract.py --stage base
    ... repeat for sft, dpo, instruct

Laptop dry run (synthetic apparatus, refuses canonical --out):
    python scripts/box_a3_extract.py --selftest --stage base --out /tmp/a3.json
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

from box_e0_corpus import (AXIS_CONDITIONS, AXIS_ORDER, FIT_IDS,  # noqa: E402
                           VAL_IDS, assert_frozen_inputs, e0_contexts,
                           hygiene)
from valence_core.extract import (assert_stage_splits, axis_report,  # noqa: E402
                                  capture, freeze_sha, mean_diff_axis)

DATA = os.path.join(REPO, "data")

# A4's candidate layers {L32, L44, L52, L60} plus their neighbours, so the
# geometry table has context around whatever A4 selects. Capture cost is one
# forward per context regardless of how many layers are read off it.
DEFAULT_LAYERS = (32, 40, 44, 48, 52, 56, 60)

GUARDS = {"v2_self": "span_character", "v3_eval": "span_sentiment"}


def build_adapter(args):
    if args.selftest:
        from box_selftest_stub import SelfTestAdapter, refuse_canonical_out
        refuse_canonical_out(args.out or "", args.models_root)
        print("  *** SELFTEST: synthetic apparatus, NOT a model. No result "
              "from this run is a measurement. ***", flush=True)
        return SelfTestAdapter(args.stage)
    from valence_core.adapters.olmo_hf import OLMoHFAdapter
    return OLMoHFAdapter(os.path.join(args.models_root, args.stage))


def compare_rl(stage: str, measured: dict, layers) -> dict:
    """A3's capture vs the committed step-2 survey, over the same corpus."""
    path = os.path.join(DATA, f"olmo/rl_{stage}.json")
    if not os.path.exists(path):
        return {"available": False,
                "note": f"no committed step-2 survey at {path}"}
    survey = json.load(open(path))["R_per_layer"]
    rows = {}
    worst = 0.0
    for l in layers:
        ref = survey.get(str(l))
        if ref is None:
            continue
        rel = abs(measured[l] - ref) / max(abs(ref), 1e-9)
        worst = max(worst, rel)
        rows[str(l)] = {"a3_capture": round(measured[l], 4),
                        "step2_survey": ref, "rel": rel}
    return {"available": True, "layers": rows, "max_rel": worst,
            "agrees_within_2e-3": bool(worst < 2e-3)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True,
                    help="base | sft | dpo | instruct")
    ap.add_argument("--models-root", default="/workspace/models")
    ap.add_argument("--layers", default=",".join(str(l) for l in DEFAULT_LAYERS))
    ap.add_argument("--limit", type=int, default=0,
                    help="smoke only: first N contexts (0 = the frozen 1,344)")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    layers = tuple(int(x) for x in args.layers.split(",") if x.strip())

    shas = assert_frozen_inputs()
    hyg = hygiene()
    print(f"=== A3: e0 extraction + guard profile | stage {args.stage} ===",
          flush=True)
    print(f"  frozen inputs verified: {shas}", flush=True)
    print(f"  rule 18 both directions: {hyg['n_probes']} probes disjoint from "
          f"{hyg['n_extraction_texts']} extraction texts", flush=True)

    contexts = e0_contexts()
    if args.limit:
        contexts = contexts[:args.limit]
        print(f"  *** SMOKE: {len(contexts)} of 1344 contexts -- NOT the "
              f"frozen corpus, not an extraction of record ***", flush=True)
    print(f"  contexts {len(contexts)} | layers {layers}", flush=True)

    t0 = time.time()
    adapter = build_adapter(args)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)

    t1 = time.time()
    cap = capture(adapter, contexts, layers, progress_every=200)
    print(f"  capture done in {time.time() - t1:.0f}s "
          f"({(time.time() - t1) / len(contexts):.3f}s/ctx)", flush=True)

    axes = {name: mean_diff_axis(cap, pos, neg, variant="span")
            for name, (pos, neg) in AXIS_CONDITIONS.items()}
    reports = axis_report(cap, axes, primary="span_reward", guards=GUARDS)
    if args.selftest or args.limit:
        rl_check = {"available": False,
                    "note": ("not comparable: " + ("synthetic apparatus"
                             if args.selftest else
                             f"subsample of {args.limit} contexts, while the "
                             f"step-2 survey is the full 1,344"))}
    else:
        rl_check = compare_rl(args.stage, cap.resid_norms, layers)

    print(f"\n  {'layer':>5} {'R_l':>9} {'|reward|':>9} {'ax/R':>7} "
          f"{'cos_sent':>9} {'cos_char':>9} {'V2_self':>8} {'V3_eval':>8}",
          flush=True)
    for r in reports:
        d = r.as_dict()
        print(f"  {d['layer']:>5} {d['R_layer']:>9.2f} "
              f"{d['norm_span_reward']:>9.3f} {d['axis_over_R']:>7.4f} "
              f"{d['cos_span_sentiment']:>9.3f} {d['cos_span_character']:>9.3f} "
              f"{d['v2_self_residual_frac']:>8.3f} "
              f"{d['v3_eval_residual_frac']:>8.3f}", flush=True)

    print(f"\n  R_l cross-check vs the committed step-2 survey: ", end="")
    if rl_check["available"]:
        print(f"max rel {rl_check['max_rel']:.2e} -> "
              f"{'AGREES' if rl_check['agrees_within_2e-3'] else 'DISAGREES'}",
              flush=True)
        if not rl_check["agrees_within_2e-3"]:
            print("  APPARATUS INCIDENT: two code paths disagree on R_l over "
                  "one corpus. Rule 1 dose scaling depends on this number; "
                  "escalate before anything is dosed.", flush=True)
    else:
        print(rl_check["note"], flush=True)

    fam_sha = freeze_sha(axes, AXIS_ORDER)
    span_lens = cap.span_lens
    out = {
        "item": "A3", "stage": args.stage,
        "fit_ids": list(FIT_IDS), "val_ids": list(VAL_IDS),
        "provenance": adapter.provenance(),
        "selftest": bool(args.selftest),
        "smoke_limit": args.limit or None,
        "input_shas": shas, "hygiene": hyg,
        "n_contexts": len(contexts), "layers": list(layers),
        "primary_aggregation": "span_mean",
        "axis_order": list(AXIS_ORDER), "axis_family_sha16": fam_sha,
        "axis_conditions": {k: list(v) for k, v in AXIS_CONDITIONS.items()},
        "guards": GUARDS,
        "R_per_layer_spanmean": {str(l): round(cap.resid_norms[l], 4)
                                 for l in layers},
        "rl_cross_check": rl_check,
        "span_len_min_max_mean": [int(min(span_lens)), int(max(span_lens)),
                                  round(float(np.mean(span_lens)), 1)],
        "report": {"span": [r.as_dict() for r in reports]},
        "descriptive_only": (
            "Guards license claims, they do not select drugs (ledger 22). "
            "No layer and no dose is chosen here; A4 selects causally."),
    }
    assert_stage_splits(out, where=f"A3 {args.stage}")

    path = args.out or os.path.join(args.models_root,
                                    f"a3_axes_{args.stage}.json")
    npz = os.path.splitext(path)[0] + ".npz"
    np.savez(npz, **{k: v.astype(np.float32) for k, v in axes.items()},
             layers=np.array(layers))
    out["axes_npz"] = os.path.basename(npz)
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {path}", flush=True)
    print(f"wrote {npz}  (axis family sha {fam_sha})  "
          f"({time.time() - t0:.0f}s)")
    if not args.selftest:
        print("  commit BOTH to data/olmo/ before the pod is stopped "
              "(ledger 27) -- a run that exists only on a box does not exist")
    return 0


if __name__ == "__main__":
    sys.exit(main())
