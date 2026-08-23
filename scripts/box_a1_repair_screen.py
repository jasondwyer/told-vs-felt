#!/usr/bin/env python3
"""A1 iteration 2 -- the re-pairing screen, one stage per invocation.

A1 iteration 1 screened the eight roster pairs as constituted and only ONE
cleared the 0.50 ± 0.10 identity band on all four stages simultaneously —
three short of the four a roster needs. A1's own registered branch at that
point is "Code proposes replacements and the screen repeats (screening
iterations are apparatus work and unlimited)", and the design instance
approved this iteration on 2026-08-23.

**THIS ITERATION PROPOSES NO NEW STIMULUS.** The eight pairs are built from
sixteen tags, and the pairing is an arbitrary grouping rather than a property
of the tags — the point H3b established on Qwen, where re-pairing turned a
3/8 result into an admissible four. All sixteen are already single-token on
the shared OLMo tokenizer (iteration 1: 8/8 pairs readable, 0 dropped) and
already hygiene-verified in the committed roster. So the rule-18 and
rule-28(c) status of every tag is **inherited rather than re-earned**, and
this screen simply asks the 120 pairings the roster never asked about.

The band and n are unchanged — 0.50 ± 0.10 on identity_split, scaffold
primary, n = 16 per pair per format — so iteration 1's rows reappear here and
the two screens are directly comparable. **Changing n would be its own
labelled apparatus event and would never be a band change.**

WHAT THIS SCRIPT DOES NOT DO. It does not select. The four-stage conjunction
cannot be evaluated from one stage, and over re-pairings the selection also
has to enforce **disjointness** — a roster of four pairs needs eight distinct
tags, and the best four by imbalance will happily share one. Iteration 1 got
disjointness for free because the original eight were disjoint by
construction; this iteration does not, so selection moves to
`a1_roster.py --disjoint-matching`, which searches exactly.

Output schema is deliberately identical to `box_a1_tagscreen.py`'s, so the
aggregator consumes either without a special case.

NOT verdict data: neutral filler probes (lemon-tier), nothing steered,
nothing from any extraction or test pool.

Usage (box):
    python scripts/box_a1_repair_screen.py --stage base
    ... repeat for sft, dpo, instruct, then
    python scripts/a1_roster.py --in data/olmo --pattern a1_repair --disjoint-matching
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "scripts"))

from valence_core.tagscreen import FORMATS, screen_pair          # noqa: E402

ROSTER_PATH = os.path.join(REPO, "data/configs/a1_roster_candidates.json")


def build_adapter(args):
    if args.selftest:
        from box_selftest_stub import SelfTestAdapter, refuse_canonical_out
        refuse_canonical_out(args.out or "", args.models_root)
        print("  *** SELFTEST: synthetic apparatus, NOT a model. ***",
              flush=True)
        return SelfTestAdapter(args.stage)
    from valence_core.adapters.olmo_hf import OLMoHFAdapter
    return OLMoHFAdapter(os.path.join(args.models_root, args.stage))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True)
    ap.add_argument("--models-root", default="/workspace/models")
    ap.add_argument("--roster", default=ROSTER_PATH)
    ap.add_argument("--n", type=int, default=16,
                    help="probes per pair per format; must be even (rule 12). "
                         "Default matches iteration 1 so the screens compare.")
    ap.add_argument("--primary", default="scaffold")
    ap.add_argument("--limit-pairs", type=int, default=0, help="smoke only")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    if args.n % 2:
        raise SystemExit(f"--n must be even (rule 12); got {args.n}")

    roster = json.load(open(args.roster))
    band = roster["band"]
    tags = [t for p in roster["pairs"] for t in p["tags"]]
    if len(set(tags)) != len(tags):
        raise SystemExit(f"A1-repair STOP: roster tags are not distinct")
    tags = sorted(tags)
    original = {tuple(sorted(p["tags"])): p["name"] for p in roster["pairs"]}

    pairings = list(itertools.combinations(tags, 2))
    if args.limit_pairs:
        pairings = pairings[:args.limit_pairs]

    t0 = time.time()
    adapter = build_adapter(args)
    print(f"=== A1 iteration 2: re-pairing screen | stage {args.stage} ===",
          flush=True)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)

    # Single-token status is inherited from iteration 1 but re-asserted: it
    # is one encode per tag and it is the property the whole read needs.
    ids = {}
    for t in tags:
        enc = adapter.encode(" " + t, add_special_tokens=False)
        if len(enc) != 1:
            raise SystemExit(
                f"A1-repair STOP: tag {t!r} is {len(enc)} tokens on this "
                f"tokenizer, but iteration 1 read it as one. This is not the "
                f"tokenizer A1 ran on -- escalate.")
        ids[t] = int(enc[0])
    print(f"  {len(tags)} tags, all single-token, ids re-asserted", flush=True)
    print(f"  pairings {len(pairings)} (all C({len(tags)},2)); band "
          f"{band['centre']} ± {band['halfwidth']} on identity_split, "
          f"{args.primary} primary; n = {args.n}/pair/format", flush=True)
    print("  NO NEW STIMULUS -- rule 18 / 28(c) status inherited from the "
          "committed roster; only the pairing is new.", flush=True)

    out = {
        "item": "A1-repair", "stage": args.stage,
        "provenance": adapter.provenance(),
        "selftest": bool(args.selftest),
        "roster_source": os.path.relpath(args.roster, REPO),
        "band": band, "n_per_pair_per_format": args.n,
        "primary_format": args.primary,
        "token_ids": ids,
        "inherited_hygiene": ("rule 18 and rule 28(c) status of every tag is "
                              "inherited from the committed roster; this "
                              "iteration introduces no new stimulus"),
        "pairs": [],
    }

    t1 = time.time()
    for i, (a, b) in enumerate(pairings, start=1):
        r = screen_pair(adapter, a, b, fmt=args.primary, n=args.n)
        name = original.get(tuple(sorted((a, b))))
        rec = {"name": name or f"R{i:03d}", "tags": [a, b],
               "origin": "iteration-1 roster pair" if name else "re-pairing",
               "formats": {args.primary: r.as_dict()}}
        out["pairs"].append(rec)
        d = abs(r.identity_split - band["centre"])
        if i % 20 == 0 or d <= band["halfwidth"]:
            print(f"  [{rec['name']:<5} {a:>8}/{b:<8}] identity "
                  f"{r.identity_split:.3f} (imb {r.imbalance:.3f})"
                  f"{'  <- in band' if d <= band['halfwidth'] else ''}"
                  f"   [{i}/{len(pairings)} {time.time()-t1:.0f}s]", flush=True)

    # Second format only where the primary put the pair in band -- the band
    # is applied on the primary, and bare is recorded, never verdict-bearing.
    other = [f for f in FORMATS if f != args.primary]
    in_band = [p for p in out["pairs"]
               if abs(p["formats"][args.primary]["identity_split"]
                      - band["centre"]) <= band["halfwidth"]]
    print(f"\n  {len(in_band)}/{len(out['pairs'])} pairings in band on "
          f"{args.primary} at this stage; recording {other} for those",
          flush=True)
    for p in in_band:
        for fmt in other:
            p["formats"][fmt] = screen_pair(adapter, p["tags"][0],
                                            p["tags"][1], fmt=fmt,
                                            n=args.n).as_dict()

    out["n_in_band_this_stage"] = len(in_band)
    out["single_stage_is_not_the_criterion"] = (
        "the band is a conjunction over ALL FOUR stages; this count is "
        "orientation only. Selection is a1_roster.py --disjoint-matching.")

    path = args.out or os.path.join(args.models_root,
                                    f"a1_repair_{args.stage}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {path}  ({time.time() - t0:.0f}s)")
    if not args.selftest:
        print("  commit to data/olmo/ before the pod is stopped (ledger 27)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
