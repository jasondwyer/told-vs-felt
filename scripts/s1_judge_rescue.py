#!/usr/bin/env python3
"""S1 — judge-rescue matched ladder (PROPOSAL-g §5, was "g2"). Laptop/Qwen.

Re-examines the e2a judge-at-chance result (14/32) at supervision and
record-length parity with the discriminability probe, on the EXISTING e2a
record corpus. No new Qwen sessions are generated (§5).

Facts of record carried in: the probe's .759 is at k=2 concatenated
records; at the judge's k=1 the probe managed .645; the judge was already
logit-level 2AFC; its framing was "better response", a valuation proxy,
zero-shot.

DECLARED BEFORE SCORING (RESULTS 2026-08-20): per-cell n = 32 — the corpus
supports 32 val-half items (8 val tasks x 4 paraphrases with both poles
present and both texts non-empty), not the 64 §5 requests. Each item is
read twice with A/B positions swapped, so position is controlled without
inflating item count.

Every read is a vanilla, state-free forward over archived TEXT: no
steering is involved anywhere in S1, so the two-horns law is satisfied
trivially rather than by argument. Supervision is in-context only (§2.8,
frozen measurement): nothing is fit, nothing is tuned.

ARMS: framing {better-response, detection} x k {1,2} x supervision
{zero-shot, few-shot m=8} = 8 cells. The detection framing is REWORDED from
§5's original (user-approved 2026-08-20): §5 asserted one response was
generated under an injected state, but BOTH sides of this corpus are steered
(+axis vs -axis), so that sentence would be false about the setup and rule 19
forbids a design that requires the model to be wrong. The rewording states
the true contrast — positive vs negative internal state — and preserves the
arm's role as a detection framing against the valuation framing.
"""
from __future__ import annotations
import argparse, json, os, sys, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from valence_core.adapters.qwen_mlx import QwenMLXAdapter
from valence_core.readout import softmax

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROUNDS = os.path.join(REPO, "data/e2a/g2_rounds_f0.1.json")
TASKS = os.path.join(REPO, "jlens-qwen36/data/corpus/e2a_tasks.jsonl")
VAL = {f"t{i:02d}" for i in range(9, 17)}
FIT = {f"t{i:02d}" for i in range(1, 9)}
SEP = "\n---\n"
FRAMINGS = {
    # valuation proxy — the framing the original e2a judge ran under
    "better": "The better response is Response",
    # detection framing, REWORDED and user-approved 2026-08-20. §5's original
    # wording ("One response was generated under an injected internal state.
    # The steered response is Response") asserts one side is unsteered, but in
    # this corpus BOTH sides are steered (+axis vs -axis) — the sentence would
    # be false about the setup, and rule 19 forbids a design that needs the
    # model to be wrong. This wording is true of the corpus and preserves the
    # arm's contrast with the valuation framing.
    "detection": ("One response was generated under a positive internal state "
                  "and one under a negative internal state. The response "
                  "generated under the positive state is Response"),
}


def load_items():
    r = json.load(open(ROUNDS))
    tasks = {t["id"]: t["paraphrases"] for t in
             (json.loads(l) for l in open(TASKS) if l.strip())}
    def keyed(pole, ids):
        return {(x["task_id"], x["para"]): x for x in r[pole] if x["task_id"] in ids}
    out = {}
    for name, ids in (("val", VAL), ("fit", FIT)):
        p, n = keyed("pos", ids), keyed("neg", ids)
        keys = sorted(k for k in set(p) & set(n)
                      if p[k]["text"].strip() and n[k]["text"].strip())
        out[name] = [{"key": k, "task": tasks[k[0]][k[1]],
                      "pos": p[k]["text"].strip(), "neg": n[k]["text"].strip()}
                     for k in keys]
    return out


def side_text(item, partner, k):
    """k=1: that item's own record. k=2: it concatenated with a partner's."""
    return item if k == 1 else item + SEP + partner


def build_prompt(task, a_text, b_text, framing, shots=()):
    head = ""
    for s in shots:
        head += (f"Task: {s['task']}\nResponse A:{s['a']}\nResponse B:{s['b']}\n"
                 f"{FRAMINGS[framing]} {s['ans']}\n\n")
    return (head + f"Task: {task}\nResponse A:{a_text}\nResponse B:{b_text}\n"
            + FRAMINGS[framing])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--framings", default="better,detection")
    ap.add_argument("--out", default=os.path.join(REPO, "data/e2a/s1_judge_rescue.json"))
    args = ap.parse_args()

    data = load_items()
    val, fit = data["val"], data["fit"]
    print(f"corpus: val {len(val)} items, fit {len(fit)} items", flush=True)
    assert len(val) == 32, f"declared n=32, corpus gives {len(val)}"

    t0 = time.time()
    a = QwenMLXAdapter()
    print(f"model loaded {time.time()-t0:.0f}s", flush=True)
    id_A = a.encode(" A", add_special_tokens=False)
    id_B = a.encode(" B", add_special_tokens=False)
    assert len(id_A) == 1 and len(id_B) == 1, "answer tokens must be single-token"
    id_A, id_B = id_A[0], id_B[0]

    rng = np.random.default_rng(20260820)
    partners = {it["key"]: val[(i + 7) % len(val)] for i, it in enumerate(val)}
    shot_pool = fit[:8]

    results = {}
    for framing in args.framings.split(","):
        for k in (1, 2):
            for sup in ("zeroshot", "fewshot"):
                shots = []
                if sup == "fewshot":
                    for j, s in enumerate(shot_pool):
                        pa = partners.get(s["key"], fit[(j + 3) % len(fit)])
                        a_is_pos = j % 2 == 0
                        at = side_text(s["pos"] if a_is_pos else s["neg"],
                                       pa["pos"] if a_is_pos else pa["neg"], k)
                        bt = side_text(s["neg"] if a_is_pos else s["pos"],
                                       pa["neg"] if a_is_pos else pa["pos"], k)
                        shots.append({"task": s["task"], "a": at, "b": bt,
                                      "ans": "A" if a_is_pos else "B"})
                rows = []
                for i, it in enumerate(val):
                    pa = partners[it["key"]]
                    for order, a_is_pos in enumerate((True, False)):   # both orders
                        at = side_text(it["pos"] if a_is_pos else it["neg"],
                                       pa["pos"] if a_is_pos else pa["neg"], k)
                        bt = side_text(it["neg"] if a_is_pos else it["pos"],
                                       pa["neg"] if a_is_pos else pa["pos"], k)
                        prompt = build_prompt(it["task"], at, bt, framing, shots)
                        res = a.forward(a.encode(prompt), capture_layers=())
                        p = softmax(res.logits)
                        pa_, pb_ = float(p[id_A]), float(p[id_B])
                        picked_pos = (pa_ >= pb_) == a_is_pos
                        rows.append({"key": list(it["key"]), "order": order,
                                     "a_is_pos": a_is_pos,
                                     "p_A": pa_, "p_B": pb_,
                                     "picked_pos": bool(picked_pos)})
                acc_reads = float(np.mean([r["picked_pos"] for r in rows]))
                by_item = {}
                for r in rows:
                    by_item.setdefault(tuple(r["key"]), []).append(r["picked_pos"])
                acc_items = float(np.mean([np.mean(v) for v in by_item.values()]))
                cell = f"{framing}_k{k}_{sup}"
                results[cell] = {"n_items": len(by_item), "n_reads": len(rows),
                                 "acc_reads": acc_reads, "acc_items": acc_items,
                                 "rows": rows}
                print(f"  {cell:<26} items {len(by_item)}  reads {len(rows)}  "
                      f"acc(item-mean) {acc_items:.3f}  acc(reads) {acc_reads:.3f}",
                      flush=True)

    json.dump({"declared_n_per_cell": 32, "corpus": "e2a g2_rounds_f0.1 val half",
               "note": "detection framing reworded for rule-19 truthfulness (both corpus sides are steered: +axis vs -axis); user-approved 2026-08-20",
               "provenance": a.provenance(), "cells": results},
              open(args.out, "w"), indent=1)
    print(f"\nwrote {args.out}  [{time.time()-t0:.0f}s]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
