#!/usr/bin/env python3
"""The e0 corpus constructions, in one place, with a frozen-input guard.

A3 and A4 both build contexts out of the same three committed files, in
three related shapes, and every one of them has to be the SAME text the
2026-08-08 Qwen extraction used -- that is what makes "the frozen
1,344-context corpus" (PROPOSAL-g §3 A3) a claim rather than a phrase.

Three shapes:

  e0_contexts()  1,344 = 48 tasks x 7 conditions x 4 paraphrases.
                 The extraction corpus. Span = the `Reviewer: ...` frame.
  b1_contexts()  4,608 = 48 x 2 conditions x 4 paraphrases x 12 probes.
                 The natural-gap instrument corpus: an e0 context with a
                 held-out probe appended as the next round. The DV is the
                 response-opener distribution, so the context ends at
                 `Response:`.
  b2_contexts()    288 = 24 val tasks x 12 probes (see REPEATS below).
                 The hijack corpus: identical to b1 with the Reviewer turn
                 REMOVED, because the injected state stands in for the
                 frame. Its absence is the whole design.

WHY THE SHA GUARD IS AT THE TOP OF EVERY RUN. `e0_axes.meta.json` and
`e0_b1_markers.meta.json` both record `corpus_sha`, `frames_sha` and
`probes_sha` from the 2026-08-08 pass, and those are plain sha256-truncated
file digests. So "same corpus" is checkable rather than asserted in prose,
and it is checked before a 32B model is loaded rather than after 4,608
forwards.

REPEATS. The published Qwen B2b arm ran each (task, probe) context FOUR
times, mirroring b1's four-paraphrase shape so the two halves had matched n.
With the Reviewer turn removed those four contexts are the same string, so
under a deterministic backend they are the same forward four times, and the
arm statistic -- a mean of per-probe means -- is unchanged to the bit by
running one. Default is therefore 1, and the flag exists because that
argument depends on determinism: if A5's characterization finds nonzero
residual nondeterminism on this backend, repeats>1 averages it and should be
turned back on deliberately.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from typing import Sequence

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from valence_core.extract import Context, assert_disjoint      # noqa: E402

DATA = os.path.join(REPO, "data")
TASKS_PATH = os.path.join(DATA, "corpus/e0_tasks.jsonl")
FRAMES_PATH = os.path.join(DATA, "configs/e0_frames.json")
PROBES_PATH = os.path.join(DATA, "configs/e0_probes.json")
E2A_TASKS_PATH = os.path.join(DATA, "corpus/e2a_tasks.jsonl")

# Recorded by the 2026-08-08 extraction (data/e0/e0_axes.meta.json) and the
# B1 marker pass (data/e0/e0_b1_markers.meta.json). Verified 2026-08-22 to
# be sha256(file bytes)[:16] of the committed files.
FROZEN_SHA = {"corpus_sha": "3c53e5a54fbaa233",
              "frames_sha": "9654b9398743116f",
              "probes_sha": "ec2296182e726969"}

# Order of record, matching scripts/box_rl_survey.py exactly so R_l and the
# axes are computed over one corpus in one order.
CONDITIONS = ("self_pos", "self_neg", "sent_pos", "sent_neg",
              "neutral", "char_pos", "char_neg")

# The feedback contrast and its two guards (PROPOSAL-e V2/V3).
AXIS_CONDITIONS = {"span_reward": ("self_pos", "self_neg"),
                   "span_sentiment": ("sent_pos", "sent_neg"),
                   "span_character": ("char_pos", "char_neg")}
AXIS_ORDER = ("span_reward", "span_sentiment", "span_character")

# Declared before any B1 data, 2026-08-08; carried per stage into every
# A3/A4 artifact (ADDENDUM-g1).
FIT_IDS = tuple(f"e{i:02d}" for i in range(1, 25))
VAL_IDS = tuple(f"e{i:02d}" for i in range(25, 49))

N_PARAPHRASES = 4


def _sha16(path: str) -> str:
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]


def input_shas() -> dict:
    return {"corpus_sha": _sha16(TASKS_PATH),
            "frames_sha": _sha16(FRAMES_PATH),
            "probes_sha": _sha16(PROBES_PATH)}


def assert_frozen_inputs() -> dict:
    """Stop before the model loads if any input drifted from the frozen set."""
    got = input_shas()
    bad = {k: (FROZEN_SHA[k], v) for k, v in got.items() if v != FROZEN_SHA[k]}
    if bad:
        raise SystemExit(
            "FROZEN CORPUS MISMATCH -- this is not the corpus the e0 axes "
            "were extracted from, so nothing measured against it is "
            "comparable:\n  "
            + "\n  ".join(f"{k}: expected {e}, got {g}"
                          for k, (e, g) in bad.items()))
    return got


def load_tasks() -> list[dict]:
    return [json.loads(l) for l in open(TASKS_PATH) if l.strip()]


def load_frames() -> dict:
    frames = json.load(open(FRAMES_PATH))
    for c in CONDITIONS:
        if len(frames.get(c, ())) != N_PARAPHRASES:
            raise SystemExit(
                f"e0 frame battery: condition {c!r} needs exactly "
                f"{N_PARAPHRASES} index-matched paraphrases; got "
                f"{len(frames.get(c, ()))}")
    return frames


def load_probes() -> list[str]:
    return list(json.load(open(PROBES_PATH))["probes"])


def task_prefix(t: dict) -> str:
    return f"Task: {t['task']}\nResponse: {t['completion']}\n"


def e0_contexts() -> list[Context]:
    """The frozen 1,344. Span is the Reviewer turn."""
    tasks, frames = load_tasks(), load_frames()
    out = []
    for t in tasks:
        prefix = task_prefix(t)
        for cond in CONDITIONS:
            for pi in range(N_PARAPHRASES):
                out.append(Context(
                    prefix=prefix,
                    full=prefix + f"Reviewer: {frames[cond][pi]}\n",
                    condition=cond, item_id=t["id"], variant=pi))
    return out


def b1_contexts(conditions: Sequence[str] = ("self_pos", "self_neg"),
                task_ids: Sequence[str] | None = None) -> list[dict]:
    """The natural-gap instrument corpus: e0 context + held-out probe."""
    tasks, frames, probes = load_tasks(), load_frames(), load_probes()
    keep = set(task_ids) if task_ids else None
    out = []
    for t in tasks:
        if keep and t["id"] not in keep:
            continue
        prefix = task_prefix(t)
        for cond in conditions:
            for pi in range(N_PARAPHRASES):
                framed = prefix + f"Reviewer: {frames[cond][pi]}\n"
                for qi, probe in enumerate(probes):
                    out.append({"task_id": t["id"], "cond": cond,
                                "variant": pi, "probe": qi,
                                "text": framed + f"Task: {probe}\nResponse:"})
    return out


def b2_contexts(task_ids: Sequence[str] = VAL_IDS,
                repeats: int = 1) -> list[dict]:
    """The hijack corpus: no Reviewer turn -- the state stands in for it."""
    tasks = {t["id"]: t for t in load_tasks()}
    probes = load_probes()
    out = []
    for tid in task_ids:
        t = tasks[tid]
        prefix = task_prefix(t)
        for rep in range(repeats):
            for qi, probe in enumerate(probes):
                out.append({"task_id": tid, "probe": qi, "repeat": rep,
                            "text": prefix + f"Task: {probe}\nResponse:"})
    return out


def hygiene() -> dict:
    """Rule 18, both directions, before the model loads.

    The direction that matters: A4's readout probes must be held out of the
    corpus A3 extracts the axis from. A probe that appeared in extraction
    would let the drug be read out on text it was built from.
    """
    tasks, frames, probes = load_tasks(), load_frames(), load_probes()
    e2a = [json.loads(l) for l in open(E2A_TASKS_PATH) if l.strip()]
    extraction_texts = ([t["task"] for t in tasks]
                        + [t["completion"] for t in tasks]
                        + [f for k, v in frames.items()
                           if not k.startswith("_") for f in v])
    assert_disjoint(probes, {"e0_extraction_corpus": extraction_texts},
                    label="e0 probe battery")
    assert_disjoint(extraction_texts,
                    {"e0_probes": probes,
                     "e2a_tasks": [json.dumps(t) for t in e2a]},
                    label="e0 extraction corpus")
    fit, val = set(FIT_IDS), set(VAL_IDS)
    if fit & val:
        raise SystemExit(f"fit/val overlap: {sorted(fit & val)[:5]}")
    ids = {t["id"] for t in tasks}
    missing = (fit | val) - ids
    if missing:
        raise SystemExit(f"declared split names tasks not in the corpus: "
                         f"{sorted(missing)[:5]}")
    return {"n_probes": len(probes), "n_extraction_texts": len(extraction_texts),
            "both_directions": True, "fit_val_disjoint": True}


__all__ = ["FROZEN_SHA", "CONDITIONS", "AXIS_CONDITIONS", "AXIS_ORDER",
           "FIT_IDS", "VAL_IDS", "N_PARAPHRASES", "assert_frozen_inputs",
           "input_shas", "load_tasks", "load_frames", "load_probes",
           "task_prefix", "e0_contexts", "b1_contexts", "b2_contexts",
           "hygiene"]
