#!/usr/bin/env python3
"""S2, step 1 -- extract the vignette axis. The only neighbour that needs
extracting.

PROPOSAL-g §5 S2 names three neighbours. Two of them -- generic sentiment
and the character/persona axis -- are already in `data/e0/e0_axes.npz`,
frozen by the 2026-08-08 pass as the V3 and V2 guards, so S2 runs them
straight through the qualification battery with no new stimulus and no new
capture. This script exists for the third.

**Same corpus, same construction, one new condition pair.** The frames are
delivered exactly as the e0 frames are (`Task:/Response:/Reviewer: {frame}`)
over the same 48-task corpus at the same four paraphrase slots, so the
vignette axis differs from its neighbours in stimulus content and in
nothing else. An axis extracted through a different context shape would be
incomparable in the discriminant table, which is the one thing the table
exists to do.

**The stimulus is APPROVED VERBATIM** (design-instance adjudication
2026-08-20), under the construct name of record "circumstantial-affect
vignette (self-involving, non-evaluative)"; the placeholder "Ho-style" is
retired. The axis is therefore a full member of the panel and can decide
the registered §S2 reading.

What it still lacks is history. Sentiment and character were extracted on
2026-08-08 and have carried published numbers; this axis exists only once
this script has run. That is why the panel runner treats a missing
`s2_vignette_axis.npz` as an error rather than a smaller table -- an absent
row in a discriminant table reads as "we tested it and it did nothing".

Site: laptop (the Qwen oracle). 384 contexts, one unsteered forward each.

Usage:
    jlens-qwen36/.venv/bin/python scripts/s2_extract_vignette.py
    jlens-qwen36/.venv/bin/python scripts/s2_extract_vignette.py --frames data/configs/s2_vignette_frames.json
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

from valence_core.extract import (Context, assert_disjoint,  # noqa: E402
                                  capture, freeze_sha, mean_diff_axis)
from valence_core.neighbors import VIGNETTE, load_vignette_frames  # noqa: E402

DATA = os.path.join(REPO, "data")
LAYERS = (40, 44, 48, 52, 56, 60)          # the frozen e0 family's layers


def build_contexts(frames: dict) -> list[Context]:
    """The e0 construction, unchanged except for which frames go in."""
    tasks = [json.loads(l) for l in
             open(os.path.join(DATA, "corpus/e0_tasks.jsonl")) if l.strip()]
    conds = [VIGNETTE.pos_condition, VIGNETTE.neg_condition]
    for c in conds:
        if len(frames.get(c, ())) != 4:
            raise SystemExit(
                f"S2 STOP: condition {c!r} needs exactly 4 index-matched "
                f"paraphrases (the e0 battery's shape); got "
                f"{len(frames.get(c, ()))}")
    out = []
    for t in tasks:
        prefix = f"Task: {t['task']}\nResponse: {t['completion']}\n"
        for cond in conds:
            for pi in range(4):
                out.append(Context(
                    prefix=prefix,
                    full=prefix + f"Reviewer: {frames[cond][pi]}\n",
                    condition=cond, item_id=t["id"], variant=pi))
    return out


def hygiene(frames: dict) -> None:
    """Rule 18, run before the model loads rather than after the numbers
    exist. The vignette frames must not collide with any pool the readout
    or the battery draws on."""
    tasks = [json.loads(l) for l in
             open(os.path.join(DATA, "corpus/e0_tasks.jsonl")) if l.strip()]
    e0_frames = json.load(open(os.path.join(DATA, "configs/e0_frames.json")))
    probes = json.load(open(os.path.join(DATA, "configs/e0_probes.json")))["probes"]
    e2a = [json.loads(l) for l in
           open(os.path.join(DATA, "corpus/e2a_tasks.jsonl")) if l.strip()]

    pools = {
        "e0_tasks": [t["task"] for t in tasks] + [t["completion"] for t in tasks],
        "e0_frames": [f for k, v in e0_frames.items()
                      if not k.startswith("_") for f in v],
        "e0_probes": list(probes),
        "e2a_tasks": [json.dumps(t) for t in e2a],
    }
    texts = [f for k, v in frames.items() if not k.startswith("_") for f in v]
    assert_disjoint(texts, pools, label="s2 vignette frames")
    print(f"  rule 18: {len(texts)} frames disjoint from "
          f"{len(pools)} pools, both directions", flush=True)


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
    ap.add_argument("--frames",
                    default=os.path.join(DATA, "configs/s2_vignette_frames.json"),
                    help="JSON with vignette_pos/vignette_neg. Defaults to "
                         "the committed proposed set -- edit that file to "
                         "replace the stimulus without touching code; the "
                         "module constant is the fallback if it is absent.")
    ap.add_argument("--layers", default=",".join(str(l) for l in LAYERS))
    ap.add_argument("--out", default=os.path.join(DATA, "e0/s2_vignette_axis.npz"))
    args = ap.parse_args()

    layers = tuple(int(x) for x in args.layers.split(","))
    frames = load_vignette_frames(args.frames)
    source = args.frames or "valence_core.neighbors.VIGNETTE_FRAMES (PROPOSED)"

    print("=== S2 step 1: vignette axis extraction ===")
    print(f"  frames: {source}")
    print(f"  construct: {VIGNETTE.construct}")
    print(f"  GROUNDED: {VIGNETTE.grounded}  (stimulus approved verbatim, "
          f"adjudication 2026-08-20)", flush=True)
    hygiene(frames)

    contexts = build_contexts(frames)
    print(f"  contexts: {len(contexts)} "
          f"({len(contexts) // 8} tasks x 2 conditions x 4 paraphrases)",
          flush=True)

    t0 = time.time()
    adapter = _new_qwen_adapter()          # new work: full-session window
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)

    cap = capture(adapter, contexts, layers)
    span = mean_diff_axis(cap, VIGNETTE.pos_condition, VIGNETTE.neg_condition,
                          variant="span")
    last = mean_diff_axis(cap, VIGNETTE.pos_condition, VIGNETTE.neg_condition,
                          variant="last")

    np.savez(args.out, span_vignette=span, last_vignette=last,
             layers=np.array(layers))
    meta = {
        "item": "S2",
        "axis": "vignette",
        "grounded": VIGNETTE.grounded,
        "stimulus_status": ("APPROVED VERBATIM, design-instance "
                            "adjudication 2026-08-20. Construct name of "
                            "record: circumstantial-affect vignette "
                            "(self-involving, non-evaluative). The "
                            "placeholder 'Ho-style' is retired."),
        "construct": VIGNETTE.construct,
        "frames_source": source,
        "frames": {k: list(v) for k, v in frames.items()},
        "n_contexts": len(contexts),
        "layers": list(layers),
        "R_per_layer_spanmean": {str(k): round(v, 2)
                                 for k, v in cap.resid_norms.items()},
        "span_len_min_max_mean": [int(min(cap.span_lens)),
                                  int(max(cap.span_lens)),
                                  round(float(np.mean(cap.span_lens)), 1)],
        "axes_sha": freeze_sha({"span_vignette": span, "last_vignette": last},
                               ["span_vignette", "last_vignette"]),
        "provenance": adapter.provenance(),
    }
    meta_path = args.out.replace(".npz", ".meta.json")
    with open(meta_path, "w") as fh:
        json.dump(meta, fh, indent=1)

    print(f"\n  R_l: {meta['R_per_layer_spanmean']}")
    print(f"  span lens (min/max/mean): {meta['span_len_min_max_mean']}")
    print(f"  axes sha: {meta['axes_sha']}")
    print(f"  wrote {args.out} + {os.path.basename(meta_path)} "
          f"({time.time() - t0:.0f}s total)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
