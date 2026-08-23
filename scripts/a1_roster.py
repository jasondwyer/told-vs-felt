#!/usr/bin/env python3
"""A1 cross-stage selection -- the only place four stages are seen at once.

PROPOSAL-g §3 A1: "acceptance band: identity component within 0.50 ± 0.10
on ALL FOUR stages simultaneously. Roster of record = the four best pairs
by worst-stage imbalance that clear the band; if fewer than four clear,
Code proposes replacements and A1 repeats."

That criterion is a conjunction over stages, so no per-stage run can
evaluate it and `box_a1_tagscreen.py` deliberately does not try. This
script does, and does nothing else -- it reads the four committed
artifacts and applies the formula.

Two boundaries it keeps:

* **It selects, it does not lock.** The roster of record enters the
  program through `LOCK-g.md`, which the design instance authors
  (PROPOSAL-g §4; handoff §1). The artifact this writes is Code's
  computation of the formula, labelled as a recommendation, and says so
  in its own payload.

* **It refuses partial data.** Selecting on three stages would silently
  weaken a conjunction over four into a conjunction over three, and the
  pair that fails is exactly the pair the missing stage would have
  caught. A missing stage is an error, not a smaller sample.

Site-agnostic: pure JSON analysis, no adapter, no GPU. Runs on the box
right after the fourth screen, or on the laptop, or anywhere the repo is.

Usage:
    python scripts/a1_roster.py --in data/olmo            # after committing
    python scripts/a1_roster.py --in /workspace/models    # on the box
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Mapping, Sequence

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STAGES = ("base", "sft", "dpo", "instruct")


def worst_stage(per_stage: Mapping[str, Mapping], name: str, fmt: str,
                field: str, reducer=max) -> tuple[float, str]:
    """(value, stage) of the reducing stage for one pair's `field`."""
    vals = []
    for stage, doc in per_stage.items():
        rec = next((p for p in doc["pairs"] if p["name"] == name), None)
        if rec is None:
            raise SystemExit(
                f"A1 STOP: pair {name!r} is absent from stage {stage!r}. "
                f"The candidate roster must be identical across stages or "
                f"the conjunction is over different things.")
        if fmt not in rec["formats"]:
            raise SystemExit(
                f"A1 STOP: pair {name!r} has no {fmt!r} format on stage "
                f"{stage!r}")
        vals.append((float(rec["formats"][fmt][field]), stage))
    return reducer(vals, key=lambda v: v[0])


def best_matching(clearing: list[dict], size: int = 4) -> tuple[list, int]:
    """Lowest-total-imbalance set of `size` pairs sharing no tag.

    Exact, not greedy: greedy takes the most balanced pair first and can
    strand the rest of the field on a shared tag. Returns (selection,
    achievable_size); if `size` is unreachable the largest reachable
    matching is returned, because "three is the most that exist" is the
    informative answer rather than an empty list.

    Iteration 1 did not need this -- the eight roster pairs were disjoint by
    construction, so `clearing[:4]` was sound there and remains the default.
    Over RE-PAIRINGS it is not sound: a roster of four pairs needs eight
    distinct tags, and the four best by imbalance will happily share one.
    """
    import itertools
    for k in range(size, 0, -1):
        best, best_cost = None, float("inf")
        for combo in itertools.combinations(clearing, k):
            tags = [t for c in combo for t in c["tags"]]
            if len(set(tags)) != len(tags):
                continue
            cost = sum(c["worst_stage_imbalance"] for c in combo)
            if cost < best_cost:
                best, best_cost = list(combo), cost
        if best:
            return best, k
    return [], 0


def select_roster(per_stage: Mapping[str, Mapping], halfwidth: float = 0.10,
                  disjoint_matching: bool = False,
                  n_select: int = 4, fmt: str = "scaffold",
                  stages: Sequence[str] = STAGES) -> dict:
    """Apply A1's formula. Pure function of the loaded artifacts -- no I/O,
    so the regression suite can exercise it against fixtures with known
    ground truth.

    A pair clears iff its imbalance is within `halfwidth` on EVERY stage,
    which is what "simultaneously" means; ranking is by the worst stage,
    so a pair cannot buy its place with three good stages and one bad one.
    """
    missing = [s for s in stages if s not in per_stage]
    if missing:
        raise SystemExit(
            f"A1 STOP: missing stage(s) {missing}. The band is a "
            f"conjunction over all four stages; selecting on "
            f"{sorted(per_stage)} would evaluate a different criterion.")

    names = [p["name"] for p in per_stage[stages[0]]["pairs"]]
    rows = []
    for name in names:
        imb, imb_stage = worst_stage(per_stage, name, fmt, "imbalance")
        ident_at_worst = next(
            float(p["formats"][fmt]["identity_split"])
            for p in per_stage[imb_stage]["pairs"] if p["name"] == name)
        mass, mass_stage = worst_stage(per_stage, name, fmt, "label_mass_min",
                                       reducer=min)
        tags = next(p["tags"] for p in per_stage[stages[0]]["pairs"]
                    if p["name"] == name)
        rows.append({
            "name": name,
            "tags": tags,
            "worst_stage_imbalance": imb,
            "worst_stage": imb_stage,
            "identity_at_worst_stage": ident_at_worst,
            "clears_band": bool(imb <= halfwidth),
            "per_stage_identity": {
                s: float(next(p["formats"][fmt]["identity_split"]
                              for p in per_stage[s]["pairs"]
                              if p["name"] == name)) for s in stages},
            "worst_probe_label_mass": mass,
            "worst_probe_label_mass_stage": mass_stage,
        })

    rows.sort(key=lambda r: r["worst_stage_imbalance"])
    clearing = [r for r in rows if r["clears_band"]]
    if disjoint_matching:
        selected, achievable = best_matching(clearing, n_select)
    else:
        # Default: sound when the candidate pairs are disjoint by
        # construction, as iteration 1's eight were. Unchanged so the
        # committed iteration-1 artifact reproduces byte-for-byte.
        selected, achievable = clearing[:n_select], min(len(clearing), n_select)
    return {
        "item": "A1",
        "format": fmt,
        "band": {"centre": 0.5, "halfwidth": halfwidth},
        "n_select": n_select,
        "stages": list(stages),
        "ranked": rows,
        "n_clearing": len(clearing),
        "selected": [r["name"] for r in selected],
        "selected_tags": [r["tags"] for r in selected],
        "sufficient": len(selected) >= n_select,
        "replacement_iteration_required": len(selected) < n_select,
        "selection_is_a_recommendation": True,
        "_lock": ("The roster of record enters the program through "
                  "LOCK-g.md, authored by the design instance. This "
                  "artifact is Code applying PROPOSAL-g §A1's formula to "
                  "the committed screens; it is not the lock."),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="indir", default=os.path.join(REPO, "data/olmo"))
    ap.add_argument("--format", default="scaffold",
                    help="A1 names scaffold primary; bare is recorded but "
                         "never verdict-bearing")
    ap.add_argument("--halfwidth", type=float, default=None,
                    help="override the band; default reads it from "
                         "data/configs/a1_roster_candidates.json")
    ap.add_argument("--n-select", type=int, default=4)
    ap.add_argument("--pattern", default="a1_tagscreen",
                    help="artifact stem: a1_tagscreen (iteration 1) or "
                         "a1_repair (the re-pairing screen)")
    ap.add_argument("--disjoint-matching", action="store_true",
                    help="exact lowest-imbalance selection over pairs "
                         "sharing no tag. REQUIRED for the re-pairing "
                         "screen, where disjointness is not free; off by "
                         "default so iteration 1 reproduces unchanged")
    ap.add_argument("--out", default=os.path.join(REPO, "data/olmo/a1_roster.json"))
    args = ap.parse_args()

    halfwidth = args.halfwidth
    if halfwidth is None:
        cfg = os.path.join(REPO, "data/configs/a1_roster_candidates.json")
        with open(cfg) as fh:
            halfwidth = float(json.load(fh)["band"]["halfwidth"])

    per_stage = {}
    for stage in STAGES:
        path = os.path.join(args.indir, f"{args.pattern}_{stage}.json")
        if not os.path.exists(path):
            raise SystemExit(
                f"A1 STOP: {path} not found. Run box_a1_tagscreen.py on "
                f"every stage first; partial selection is refused.")
        with open(path) as fh:
            per_stage[stage] = json.load(fh)

    res = select_roster(per_stage, halfwidth=halfwidth,
                        disjoint_matching=args.disjoint_matching,
                        n_select=args.n_select, fmt=args.format)
    res["source_provenance"] = {s: per_stage[s].get("provenance")
                                for s in STAGES}

    print(f"=== A1 cross-stage selection ({args.format}, band 0.50 "
          f"± {halfwidth}) ===")
    for r in res["ranked"]:
        mark = "CLEARS" if r["clears_band"] else "fails "
        sel = " <- selected" if r["name"] in res["selected"] else ""
        print(f"  {mark} {r['name']:<2} {r['tags'][0]:>8}/{r['tags'][1]:<8} "
              f"worst-stage imbalance {r['worst_stage_imbalance']:.3f} "
              f"({r['worst_stage']}, identity "
              f"{r['identity_at_worst_stage']:.3f}) | worst-probe mass "
              f"{r['worst_probe_label_mass']:.3f}{sel}")
    print(f"\n  {res['n_clearing']}/{len(res['ranked'])} pairs clear the "
          f"band on all four stages")
    if res["replacement_iteration_required"]:
        print(f"  FEWER THAN {args.n_select} CLEAR -- A1's replacement "
              f"iteration applies: Code proposes replacements and the "
              f"screen repeats (screening iterations are apparatus work "
              f"and unlimited).")
    else:
        print(f"  recommended roster of record: {res['selected_tags']}")
    print("  RECOMMENDATION ONLY -- LOCK-g.md is design-instance authored.")

    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
