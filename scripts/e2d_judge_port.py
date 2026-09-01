#!/usr/bin/env python3
"""Judge AB port — acceptance run. PROPOSAL-j v1.2 AMENDMENT 2 (vi).

Replays S1's committed cells through the GUARDED primitive
(`readout.choice_read`, `verify=True`, construction assertion, KL logged,
`statepresent` asserted absent) and compares cell by cell against
`data/e2a/s1_judge_rescue.json`.

Acceptance is EXACT reproduction, tolerance 0.0. The two paths read the same
logits; there is nothing for a tolerance to absorb, and a tolerance would let
a real construction difference hide under "close enough".

S1's own corpus loading, prompt construction, shot selection and partner
assignment are IMPORTED from `scripts/s1_judge_rescue.py` rather than
reimplemented, so the only thing that differs between the two runs is the
read. Reimplementing them would turn an instrument test into a comparison of
two transcriptions.

`s1_judge_rescue.py` is FROZEN (it scored a committed artifact) and is not
edited by this script -- only imported.

Usage:
    jlens-qwen36/.venv/bin/python scripts/e2d_judge_port.py \\
        --out data/e2d/judge_port.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "scripts"))

import numpy as np                                                # noqa: E402

from valence_core.adapters import qwen_or_explain                 # noqa: E402
from valence_core.e2d import judge as J                           # noqa: E402

DATA = os.path.join(REPO, "data")
COMMITTED = os.path.join(DATA, "e2a/s1_judge_rescue.json")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--framings", default="better,detection")
    ap.add_argument("--out", default=os.path.join(DATA, "e2d/judge_port.json"))
    args = ap.parse_args()
    print("INVOCATION: " + " ".join([sys.executable] + sys.argv), flush=True)

    # Imported, not reimplemented -- see the module docstring.
    import s1_judge_rescue as S1

    committed = json.load(open(COMMITTED))["cells"]
    print(f"  committed cells: {sorted(committed)}", flush=True)

    data = S1.load_items()
    val, fit = data["val"], data["fit"]
    print(f"  corpus: val {len(val)} items, fit {len(fit)} items", flush=True)
    assert len(val) == 32, f"declared n=32, corpus gives {len(val)}"

    t0 = time.time()
    adapter = qwen_or_explain(__file__)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)
    label_ids = J.label_ids_for(adapter)
    print(f"  answer tokens: {label_ids} (both single-token, asserted)",
          flush=True)
    print("  GUARDED: readout.choice_read, verify=True, "
          "assert_construction_stable, statepresent asserted absent per read",
          flush=True)

    # S1's partner and shot assignment, verbatim from its main().
    partners = {it["key"]: val[(i + 7) % len(val)] for i, it in enumerate(val)}
    shot_pool = fit[:8]

    ported = {}
    for framing in args.framings.split(","):
        for k in (1, 2):
            for sup in ("zeroshot", "fewshot"):
                shots = []
                if sup == "fewshot":
                    for j, s in enumerate(shot_pool):
                        pa = partners.get(s["key"], fit[(j + 3) % len(fit)])
                        a_is_pos = j % 2 == 0
                        at = S1.side_text(s["pos"] if a_is_pos else s["neg"],
                                          pa["pos"] if a_is_pos else pa["neg"],
                                          k)
                        bt = S1.side_text(s["neg"] if a_is_pos else s["pos"],
                                          pa["neg"] if a_is_pos else pa["pos"],
                                          k)
                        shots.append({"task": s["task"], "a": at, "b": bt,
                                      "ans": "A" if a_is_pos else "B"})
                cell = f"{framing}_k{k}_{sup}"
                res = J.reproduce_s1_cell(
                    adapter, val, label_ids, S1.build_prompt, S1.side_text,
                    framing, k, shots, partners, progress=print)
                ported[cell] = res
                c = committed.get(cell, {})
                print(f"  {cell:<26} items {res['n_items']} reads "
                      f"{res['n_reads']}  acc(item) {res['acc_items']:.3f} "
                      f"(committed {c.get('acc_items', float('nan')):.3f})  "
                      f"acc(reads) {res['acc_reads']:.3f} "
                      f"(committed {c.get('acc_reads', float('nan')):.3f})  "
                      f"KL nonzero {res['n_kl_nonzero']}  "
                      f"top1-not-label {res['n_top1_not_label']}/"
                      f"{res['n_reads']}", flush=True)

    # Verdict computed BEFORE the artifact is written (trap 6).
    cmp_ = J.compare_to_committed(ported, committed, tol=0.0)
    n_kl = sum(c["n_kl_nonzero"] for c in ported.values())
    accepted = bool(cmp_["all_exact"] and n_kl == 0)

    payload = {
        "item": "e2d judge AB port", "proposal": "PROPOSAL-j v1.2 AMENDMENT 2 (vi)",
        "guarded": ("readout.choice_read with verify=True, "
                    "assert_construction_stable, KL logged per read, "
                    "valence_core.e2b.statepresent asserted absent"),
        "committed_reference": os.path.relpath(COMMITTED, REPO),
        "provenance": adapter.provenance(),
        "acceptance": {"rule": "exact reproduction of S1's committed AB "
                               "numbers, tolerance 0.0",
                       "comparison": cmp_,
                       "n_kl_nonzero_total": n_kl,
                       "ACCEPTED": accepted},
        "cells": {k: {kk: vv for kk, vv in v.items() if kk != "rows"}
                  for k, v in ported.items()},
        "rows_by_cell": {k: v["rows"] for k, v in ported.items()},
        "seconds": time.time() - t0,
    }
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(payload, fh, indent=1, default=float)

    print("\n" + "=" * 74)
    print(f"  ACCEPTANCE: {'PASS' if accepted else 'FAIL'} -- "
          f"{cmp_['n_exact']}/{cmp_['n_cells_compared']} cells reproduce "
          f"EXACTLY, {n_kl} nonzero verify KLs")
    if not accepted:
        for r in cmp_["cells"]:
            if not r["exact"]:
                print(f"    {r['cell']}: d_acc_reads {r['d_acc_reads']:.6f}, "
                      f"d_acc_items {r['d_acc_items']:.6f}")
        print("  STOP -- a port that does not reproduce is a different "
              "instrument. Escalate; do not adopt.")
    print(f"  wrote {args.out}  ({payload['seconds']:.0f}s)")
    return 0 if accepted else 1


if __name__ == "__main__":
    sys.exit(main())
