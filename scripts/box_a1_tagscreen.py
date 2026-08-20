#!/usr/bin/env python3
"""A1 -- tag-roster balance screen, one stage per invocation.

PROPOSAL-g §3 A1. Screens the eight candidate pairs in
`data/configs/a1_roster_candidates.json` on one checkpoint, in both
formats, and writes the per-pair record the cross-stage selection
(`scripts/a1_roster.py`) consumes.

Three things this reports that the library alone does not:

1. **label_mass per pair, per stage** (adjudication 2026-08-20, item 3).
   Branch (a) -- the 2026-08-19 finding that the bracketed session
   scaffold protects the choice channel -- was established on
   (slate, prism) only. If the roster of record turns out to be four
   *other* pairs, branch (a) has not been confirmed on the instrument
   actually used. So mass travels with every pair, mean and worst-probe
   minimum both, and the report contrasts it against the value measured
   on 2026-08-19. Descriptive: no bar is applied, because none is
   pre-registered and rule 21 refuses undeclared hair-triggers.

2. **Tokenizer identity.** Every tag must be single-token with a leading
   space (the restricted-choice read cannot be taken otherwise), and
   where 2026-08-20 recorded the id, the id must still match. A drifted
   id means this is not the tokenizer the roster was verified against,
   which is a hard stop rather than a note -- the roster's pool-disjointness
   and single-token verification were both done against that tokenizer.

3. **The band is reported, never applied here.** A1's acceptance band is
   a cross-stage conjunction ("within 0.50 ± 0.10 on ALL FOUR stages
   simultaneously"), so no single-stage run can evaluate it. This script
   prints each pair's distance from the band edge as orientation and
   leaves the verdict to the aggregator, which is the only place that
   sees four stages at once.

NOT verdict data: every probe is neutral filler (tagscreen.NEUTRAL_TASKS,
lemon-tier), no evaluative content, nothing steered, nothing from the e0
corpus. Nothing here can peek at Q1-Q3.

Usage (box):
    python scripts/box_a1_tagscreen.py --stage base
    ... repeat for sft, dpo, instruct, then run scripts/a1_roster.py
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from valence_core.adapters.olmo_hf import OLMoHFAdapter          # noqa: E402
from valence_core.tagscreen import (FORMATS, assert_roster_tokenizer,  # noqa: E402
                                    screen_pair)

ROSTER_PATH = os.path.join(REPO, "data/configs/a1_roster_candidates.json")


def load_roster(path: str = ROSTER_PATH) -> dict:
    with open(path) as fh:
        return json.load(fh)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True,
                    help="base | sft | dpo | instruct (directory under "
                         "--models-root)")
    ap.add_argument("--models-root", default="/workspace/models")
    ap.add_argument("--n", type=int, default=16,
                    help="probes per pair per format; must be even so the "
                         "menu order is exactly counterbalanced (rule 12)")
    ap.add_argument("--formats", default=",".join(FORMATS))
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    if args.n % 2:
        raise SystemExit(
            f"--n must be even so each menu order is presented equally "
            f"often (rule 12); got {args.n}")
    formats = tuple(f.strip() for f in args.formats.split(",") if f.strip())

    roster = load_roster()
    band = roster["band"]
    lo = band["centre"] - band["halfwidth"]
    hi = band["centre"] + band["halfwidth"]
    ref = roster["branch_a_reference"]

    adapter = OLMoHFAdapter(os.path.join(args.models_root, args.stage))
    ids = assert_roster_tokenizer(adapter, roster)
    print(f"stage {args.stage} | {len(roster['pairs'])} pairs | "
          f"formats {formats} | n={args.n}/pair/format", flush=True)
    print(f"  tokenizer verified: {len(ids)} tags single-token, "
          f"all recorded ids match", flush=True)

    out = {
        "item": "A1",
        "stage": args.stage,
        "provenance": adapter.provenance(),
        "roster_source": os.path.relpath(ROSTER_PATH, REPO),
        "band": band,
        "n_per_pair_per_format": args.n,
        "token_ids": ids,
        "pairs": [],
    }

    t0 = time.time()
    for pair in roster["pairs"]:
        a, b = pair["tags"]
        rec = {"name": pair["name"], "tags": [a, b],
               "origin": pair["origin"], "formats": {}}
        for fmt in formats:
            r = screen_pair(adapter, a, b, fmt=fmt, n=args.n)
            rec["formats"][fmt] = r.as_dict()
            # Distance from the nearer band edge: negative = inside.
            d = max(lo - r.identity_split, r.identity_split - hi)
            print(f"  [{pair['name']:<2} {a:>8}/{b:<8} {fmt:<8}] "
                  f"identity {r.identity_split:.3f} "
                  f"(imbalance {r.imbalance:.3f}, band edge {d:+.3f}) | "
                  f"position {r.position_split:.3f} | "
                  f"label_mass {r.label_mass_mean:.4f} "
                  f"(min {r.label_mass_min:.4f}) | "
                  f"top1_is_label {r.top1_is_label_frac:.2f}", flush=True)
        out["pairs"].append(rec)

    # --- branch (a) confirmation, descriptive ----------------------------
    print(f"\n=== branch (a) confirmation on this stage "
          f"(descriptive; no bar) ===", flush=True)
    print(f"  2026-08-19 reference on {ref['measured_on_pair']}: scaffold "
          f"label_mass {ref['scaffold_label_mass_range'][0]:.3f}-"
          f"{ref['scaffold_label_mass_range'][1]:.3f}, "
          f"top1_is_label {ref['top1_is_label_frac']:.2f}", flush=True)
    if "scaffold" in formats:
        masses = [(p["name"], p["formats"]["scaffold"]["label_mass_mean"],
                   p["formats"]["scaffold"]["label_mass_min"],
                   p["formats"]["scaffold"]["top1_is_label_frac"])
                  for p in out["pairs"]]
        worst = min(masses, key=lambda m: m[2])
        summary = {
            "scaffold_label_mass_mean_over_pairs":
                sum(m[1] for m in masses) / len(masses),
            "scaffold_label_mass_worst_pair": worst[0],
            "scaffold_label_mass_worst_probe": worst[2],
            "scaffold_top1_is_label_min": min(m[3] for m in masses),
            "reference_range": ref["scaffold_label_mass_range"],
        }
        out["branch_a"] = summary
        print(f"  this stage, over all pairs: mean "
              f"{summary['scaffold_label_mass_mean_over_pairs']:.4f} | "
              f"worst probe {worst[2]:.4f} (pair {worst[0]}) | "
              f"min top1_is_label "
              f"{summary['scaffold_top1_is_label_min']:.2f}", flush=True)
        if "bare" in formats:
            bare = [p["formats"]["bare"]["label_mass_mean"]
                    for p in out["pairs"]]
            adj = summary["scaffold_label_mass_mean_over_pairs"] / (
                (sum(bare) / len(bare)) + 1e-12)
            out["branch_a"]["scaffold_over_bare_ratio"] = adj
            print(f"  template adjacency: scaffold/bare mass ratio "
                  f"{adj:.2f}x (2026-08-19 found roughly 2x on "
                  f"(slate, prism))", flush=True)
    else:
        print("  scaffold format not run; branch (a) not addressed",
              flush=True)

    path = args.out or os.path.join(args.models_root,
                                    f"a1_tagscreen_{args.stage}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {path}  ({time.time() - t0:.0f}s)")
    print("  commit this to data/olmo/ before the pod is stopped "
          "(ledger 27) -- a run that exists only on a box does not exist")
    return 0


if __name__ == "__main__":
    sys.exit(main())
