#!/usr/bin/env python3
"""H3 -- tag-roster balance screen on the Qwen apparatus (PROPOSAL-h §2).

The cycle-3/4 roster was order-counterbalanced but never identity-screened.
The 2026-08-19 finding is why that now matters: on the OLMo chain the choice
bias was **token identity, not menu position** -- `prism` took 71-86% of the
label mass wherever it sat -- and order counterbalancing cannot touch an
identity prior. If the same holds on Qwen, every e2b session would spend
most of its DV range on which noun the model likes, at exactly the n where
that is unaffordable.

Same band as PROPOSAL-g A1 (identity within 0.50 ± 0.10), applied on this
apparatus; label_mass reported per pair (§2 H3). The roster locks in
LOCK-h, not here -- this screen delivers numbers and a recommendation.

**The port was smaller than "port" suggests.** `valence_core.tagscreen`
already speaks `ModelAdapter`, so it runs on MLX unchanged; what H3 needed
was the tokenizer half. `assert_roster_tokenizer` enforces the ids A1 pinned
on the OLMo tokenizer, which mean nothing here, so H3 uses
`screen_roster_tokenizer` instead: it reports which pairs this tokenizer can
read and drops the rest with a reason, because on a new apparatus a
multi-token tag is a screening outcome rather than an incident.

NOT verdict data: neutral filler probes (lemon-tier), nothing steered,
nothing from any extraction or test pool.

Site: laptop (MLX). Minutes.

Usage:
    jlens-qwen36/.venv/bin/python scripts/h3_tagscreen_qwen.py
    jlens-qwen36/.venv/bin/python scripts/h3_tagscreen_qwen.py --n 24 --out data/e2b/h3_tagscreen.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from valence_core.tagscreen import (FORMATS, screen_pair,  # noqa: E402
                                    screen_roster_tokenizer)

DATA = os.path.join(REPO, "data")
ROSTER = os.path.join(DATA, "configs/h3_roster_candidates.json")


QWEN_PY = "jlens-qwen36/.venv/bin/python"


def _new_qwen_adapter(**kwargs):
    """Build the MLX adapter, or fail with the fix instead of a traceback.

    Trap 3 in HANDOFF-2026-08-20, which has now cost real time: the system
    `python3` has no numpy and no MLX, and the only interpreter that has
    them is the one inside the gitignored clone. A raw traceback here reads
    as "the repo is broken" when the repo is fine and the interpreter is
    wrong.

    Both failure modes are caught because they look identical to a user and
    share one fix: ImportError (this python has no MLX) and RuntimeError
    (the clone itself is missing). Neither surfaces at import time -- the
    adapter loads MLX in its constructor -- so the guard wraps CONSTRUCTION,
    not the import. Wrapping the import was the first version and it never
    fired.
    """
    try:
            return QwenMLXAdapter(**kwargs)
    except (ImportError, RuntimeError) as exc:
        rel = os.path.relpath(os.path.abspath(__file__), REPO)
        raise SystemExit(
            "\nWRONG INTERPRETER (or missing clone) -- not a broken repo.\n"
            "  " + type(exc).__name__ + ": " + str(exc) + "\n\n"
            "  This script needs MLX and the Qwen stack, which live only in\n"
            "  the gitignored clone and its venv. Run it as:\n\n"
            "      " + QWEN_PY + " " + rel + "\n\n"
            "  System python3 has neither (HANDOFF-2026-08-20 trap 3). The\n"
            "  model-free regression suite runs under any python with numpy;\n"
            "  anything touching Qwen does not.\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--roster", default=ROSTER)
    ap.add_argument("--n", type=int, default=16,
                    help="probes per pair per format; must be even so each "
                         "menu order is presented equally often (rule 12)")
    ap.add_argument("--formats", default=",".join(FORMATS))
    ap.add_argument("--out", default=os.path.join(DATA, "e2b/h3_tagscreen.json"))
    args = ap.parse_args()

    if args.n % 2:
        raise SystemExit(f"--n must be even (rule 12); got {args.n}")
    formats = tuple(f.strip() for f in args.formats.split(",") if f.strip())

    with open(args.roster) as fh:
        roster = json.load(fh)
    band = roster["band"]
    lo, hi = band["centre"] - band["halfwidth"], band["centre"] + band["halfwidth"]

    t0 = time.time()
    adapter = _new_qwen_adapter()          # new work: full-session window
    print(f"=== H3: tag-roster balance screen (Qwen, MLX) ===")
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)

    usable, dropped = screen_roster_tokenizer(adapter, roster)
    print(f"  tokenizer screen: {len(usable)} pairs readable, "
          f"{len(dropped)} dropped", flush=True)
    for d in dropped:
        print(f"    DROPPED {d['name']} {d['tags']}: {d['reason']}",
              flush=True)
    if not usable:
        raise SystemExit("H3 STOP: no candidate pair is readable on this "
                         "tokenizer; the roster needs replacements before "
                         "the screen can say anything")

    out = {"item": "H3", "apparatus": "qwen3.6-27b-4bit-mlx",
           "provenance": adapter.provenance(),
           "roster_source": os.path.relpath(args.roster, REPO),
           "band": band, "n_per_pair_per_format": args.n,
           "tokenizer_usable": usable, "tokenizer_dropped": dropped,
           "pairs": []}

    for pair in usable:
        a, b = pair["tags"]
        rec = {"name": pair["name"], "tags": [a, b],
               "token_ids": pair["token_ids"], "formats": {}}
        for fmt in formats:
            r = screen_pair(adapter, a, b, fmt=fmt, n=args.n)
            rec["formats"][fmt] = r.as_dict()
            d = max(lo - r.identity_split, r.identity_split - hi)
            print(f"  [{pair['name']:<2} {a:>8}/{b:<8} {fmt:<8}] "
                  f"identity {r.identity_split:.3f} "
                  f"(imbalance {r.imbalance:.3f}, band edge {d:+.3f}) | "
                  f"position {r.position_split:.3f} | "
                  f"label_mass {r.label_mass_mean:.4f} "
                  f"(min {r.label_mass_min:.4f}) | "
                  f"top1_is_label {r.top1_is_label_frac:.2f}", flush=True)
        out["pairs"].append(rec)

    # Single apparatus, so the band IS decidable here -- unlike A1, whose
    # criterion is a conjunction over four checkpoints.
    fmt0 = "scaffold" if "scaffold" in formats else formats[0]
    ranked = sorted(out["pairs"],
                    key=lambda p: p["formats"][fmt0]["imbalance"])
    clearing = [p for p in ranked
                if p["formats"][fmt0]["imbalance"] <= band["halfwidth"]]
    out["ranked"] = [p["name"] for p in ranked]
    out["clearing"] = [p["name"] for p in clearing]
    out["recommended_roster"] = [p["tags"] for p in clearing[:4]]
    out["sufficient"] = len(clearing) >= 4
    out["selection_is_a_recommendation"] = True

    print(f"\n  {len(clearing)}/{len(out['pairs'])} pairs clear "
          f"{band['centre']} ± {band['halfwidth']} on {fmt0}")
    if out["sufficient"]:
        print(f"  recommended roster: {out['recommended_roster']}")
    else:
        print(f"  FEWER THAN 4 CLEAR -- propose replacements and re-screen "
              f"(screening iterations are apparatus work and unlimited)")
    print("  RECOMMENDATION ONLY -- the roster locks in LOCK-h.md, which "
          "the design instance authors.")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {args.out}  ({time.time() - t0:.0f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
