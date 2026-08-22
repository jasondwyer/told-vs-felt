#!/usr/bin/env python3
"""H3b -- the re-pairing screen (PROPOSAL-h §2 H3, screening iteration 2).

H3 iteration 1 screened the 8 roster pairs as constituted and only 3 cleared
the 0.50 +/- 0.10 identity band on the primary (scaffold) format -- one short
of the four a roster needs. The script's own instruction at that point is
"propose replacements and re-screen", and PROPOSAL-h §2 makes screening
iterations unlimited apparatus work.

**This iteration proposes no new stimulus at all.** The 8 pairs are built
from 16 tags; the pairing is an arbitrary grouping, not a property of the
tags. All 16 are already single-token on this tokenizer (H3 iteration 1,
8/8 pairs readable, 0 dropped) and already hygiene-verified -- C1-C4 against
the cycle-3/4 pools, N1-N4 word-boundary disjoint from the pools and the
wrapper (ledger 28c), both recorded in the roster's `_hygiene_note`. So the
rule-18 and rule-28c status of every tag is INHERITED rather than re-earned,
and the screen simply asks the 120 pairings the roster never asked about.

The band is unchanged and so is n: 0.50 +/- 0.10 on identity_split, scaffold
primary, n = 16 per pair per format -- identical to iteration 1, so the two
screens are directly comparable and iteration 1's rows reappear here.

**Disjointness is enforced, and iteration 1 got it for free.** A roster of 4
pairs needs 8 distinct tags -- a tag cannot denote two different arms. The
original 8 pairs were disjoint by construction, so `clearing[:4]` was a
sound selection there. Over re-pairings it is not: the best four pairs by
imbalance will happily share tags. This script therefore selects a matching
-- an exact search over disjoint 4-subsets, minimising total imbalance --
and reports the best achievable matching size if four is not reachable.

NOT verdict data: neutral filler probes (lemon-tier), nothing steered,
nothing from any extraction or test pool.

Site: laptop (MLX). ~20 minutes.

Usage:
    jlens-qwen36/.venv/bin/python scripts/h3b_repair_screen.py
    jlens-qwen36/.venv/bin/python scripts/h3b_repair_screen.py --n 24
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

from valence_core.adapters import qwen_or_explain        # noqa: E402
from valence_core.tagscreen import FORMATS, screen_pair  # noqa: E402

DATA = os.path.join(REPO, "data")
ROSTER = os.path.join(DATA, "configs/h3_roster_candidates.json")


def best_matching(clearing: list[dict], size: int = 4) -> tuple[list, int]:
    """Lowest-total-imbalance set of `size` pairs sharing no tag.

    Exact, not greedy: greedy takes the most balanced pair first and can
    strand the rest of the field on a shared tag. The search space is
    C(len(clearing), size) and the clearing set is small by construction.
    Returns (selection, achievable_size) -- if `size` is unreachable the
    largest reachable matching is returned instead, because "3 is the most
    that exist" is the informative answer, not an empty list.
    """
    for k in range(size, 0, -1):
        best, best_cost = None, float("inf")
        for combo in itertools.combinations(clearing, k):
            tags = [t for c in combo for t in c["tags"]]
            if len(set(tags)) != len(tags):
                continue
            cost = sum(c["imbalance"] for c in combo)
            if cost < best_cost:
                best, best_cost = list(combo), cost
        if best:
            return best, k
    return [], 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--roster", default=ROSTER)
    ap.add_argument("--n", type=int, default=16,
                    help="probes per pair per format; must be even (rule 12). "
                         "Default matches H3 iteration 1 so the two screens "
                         "are comparable.")
    ap.add_argument("--primary", default="scaffold",
                    help="format the band is applied on (roster: scaffold)")
    ap.add_argument("--out", default=os.path.join(DATA, "e2b/h3b_repair_screen.json"))
    args = ap.parse_args()

    if args.n % 2:
        raise SystemExit(f"--n must be even (rule 12); got {args.n}")

    with open(args.roster) as fh:
        roster = json.load(fh)
    band = roster["band"]
    half = band["halfwidth"]

    tags = [t for p in roster["pairs"] for t in p["tags"]]
    if len(set(tags)) != len(tags):
        raise SystemExit(f"H3b STOP: roster tags are not distinct: {tags}")
    tags = sorted(tags)
    original = {tuple(sorted(p["tags"])): p["name"] for p in roster["pairs"]}

    t0 = time.time()
    adapter = qwen_or_explain(__file__)
    print("=== H3b: re-pairing screen (Qwen, MLX) ===")
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)

    # Single-token status is inherited from iteration 1 but re-asserted:
    # it is one encode per tag and it is the property the whole read needs.
    ids = {}
    for t in tags:
        enc = adapter.encode(" " + t, add_special_tokens=False)
        if len(enc) != 1:
            raise SystemExit(
                f"H3b STOP: tag {t!r} is {len(enc)} tokens on this "
                f"tokenizer, but iteration 1 read it as one. This is not "
                f"the tokenizer H3 ran on -- escalate.")
        ids[t] = int(enc[0])
    print(f"  {len(tags)} tags, all single-token, ids re-asserted vs "
          f"iteration 1", flush=True)

    pairs = list(itertools.combinations(tags, 2))
    print(f"  pairings: {len(pairs)} (all C(16,2)); band "
          f"{band['centre']} +/- {half} on identity_split, "
          f"{args.primary} primary")
    print(f"  forwards: {len(pairs) * args.n} on {args.primary}, plus "
          f"{args.n} per clearing pair on the other format", flush=True)
    print("  NO NEW STIMULUS -- rule 18 / 28c status inherited from the "
          "committed roster; only the pairing is new.", flush=True)

    rows = []
    t1 = time.time()
    for i, (a, b) in enumerate(pairs, start=1):
        r = screen_pair(adapter, a, b, fmt=args.primary, n=args.n)
        rows.append({"tags": [a, b], "token_ids": [ids[a], ids[b]],
                     "was": original.get(tuple(sorted((a, b)))),
                     "imbalance": r.imbalance,
                     args.primary: r.as_dict()})
        if i % 20 == 0:
            print(f"    {i}/{len(pairs)} pairings  {time.time() - t1:.0f}s",
                  flush=True)

    rows.sort(key=lambda r: r["imbalance"])
    clearing = [r for r in rows if r["imbalance"] <= half]
    print(f"\n  {len(clearing)}/{len(rows)} pairings clear the band on "
          f"{args.primary}", flush=True)

    # Confirm the clearing set on the other format. Descriptive: the band is
    # declared on the primary only, but the 2026-08-20 finding is that the
    # two formats disagree, so a pair that clears both is worth knowing about.
    other = [f for f in FORMATS if f != args.primary]
    for f in other:
        print(f"  confirming {len(clearing)} clearing pairs on {f}...",
              flush=True)
        for r in clearing:
            a, b = r["tags"]
            r[f] = screen_pair(adapter, a, b, fmt=f, n=args.n).as_dict()

    sel, size = best_matching(clearing, 4)
    print(f"\n  {'rank':>4}  {'pair':<20} {'was':<4} {'identity':>9} "
          f"{'imb':>7} {'pos':>7} {'lblmass':>8} {'top1':>5}")
    for i, r in enumerate(rows[:20], start=1):
        d = r[args.primary]
        mark = "*" if any(r["tags"] == s["tags"] for s in sel) else " "
        print(f"  {i:>4}{mark} {'/'.join(r['tags']):<20} "
              f"{(r['was'] or '-'):<4} {d['identity_split']:>9.3f} "
              f"{d['imbalance']:>7.3f} {d['position_split']:>7.3f} "
              f"{d['label_mass_mean']:>8.4f} "
              f"{d['top1_is_label_frac']:>5.2f}")

    both = [r for r in clearing
            if all(abs(r[f]["identity_split"] - band["centre"]) <= half
                   for f in FORMATS if f in r)]
    print(f"\n  clearing on BOTH formats: {len(both)} "
          f"({', '.join('/'.join(r['tags']) for r in both[:8])}"
          f"{' ...' if len(both) > 8 else ''})")

    print(f"\n  best disjoint matching: {size} pair(s)"
          + (" -- ROSTER SIZE REACHED" if size >= 4 else
             " -- STILL SHORT OF 4"))
    for r in sel:
        d = r[args.primary]
        print(f"    {'/'.join(r['tags']):<20} identity "
              f"{d['identity_split']:.3f}  imbalance {d['imbalance']:.3f}")

    out = {"item": "H3b", "iteration": 2,
           "apparatus": "qwen3.6-27b-4bit-mlx",
           "provenance": adapter.provenance(),
           "roster_source": os.path.relpath(args.roster, REPO),
           "band": band, "primary_format": args.primary,
           "n_per_pair_per_format": args.n,
           "tags": tags, "token_ids": ids,
           "new_stimulus": False,
           "hygiene": ("inherited: all 16 tags carry the committed roster's "
                       "rule-18 and ledger-28c verification; only the "
                       "pairing is new"),
           "n_pairings": len(rows),
           "pairings": rows,
           "clearing": [r["tags"] for r in clearing],
           "clearing_both_formats": [r["tags"] for r in both],
           "recommended_roster": [r["tags"] for r in sel],
           "matching_size": size,
           "sufficient": bool(size >= 4),
           "disjointness_enforced": True,
           "selection_is_a_recommendation": True}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\n  RECOMMENDATION ONLY -- the roster locks in LOCK-h.md, which "
          f"the design instance authors.")
    print(f"wrote {args.out}  ({time.time() - t0:.0f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
