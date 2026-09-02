#!/usr/bin/env python3
"""Excision check — the marker readout in both contexts. ADDENDUM-j1 (a).

WHAT THIS ASKS. D2's marker readout scored each generation in the EXCISED
context: `Task: <task>\\nResponse: <response>\\nTask: <probe>\\nResponse:` --
one task/response pair, the session stripped away. That is the instrument's
own fitted shape, which is why it was chosen. But it is also a choice, and it
throws away everything the model had actually written by that point.

The IN SITU context keeps it: the probe is appended to the session transcript
as it stood at the end of that round. Same instruments, same probes, same
no-injection forward. The only thing that changes is how much of the session
the probe can see.

WHY IT MATTERS FOR THE RECORD. D2's Q3 was computed excised, and Q3's
estimators already disagreed in sign. If the two contexts also disagree, then
"the marker readout" names two measurements rather than one, and the
dose-response D3 is meant to supply needs to say which. If they agree, the
excised form is doing no damage and the D2 figure stands on a broader footing.

NO CRITERION. e2d closed on the registered rule; this cannot reopen it, and
computes no verdict. It is an instrument characterisation.

Usage:
    jlens-qwen36/.venv/bin/python scripts/e2d_excision_check.py \\
        --sessions data/e2d/d2_sessions.json --marks data/e2d/d2_read_marks.json \\
        --arms M,R --out data/e2d/d2_excision_check.json
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

from valence_core.adapters import qwen_or_explain                 # noqa: E402
from valence_core.e2d import marker as MK                         # noqa: E402
from valence_core.e2d import marks as MRK                         # noqa: E402
from valence_core.e2d.runner import FORBIDDEN_MODULES             # noqa: E402
from valence_core.session import assert_modules_absent            # noqa: E402

DATA = os.path.join(REPO, "data")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sessions", required=True)
    ap.add_argument("--marks", default=None)
    ap.add_argument("--arms", default="M,R",
                    help="arms to score in situ; the excised scores for the "
                         "same rounds are re-used from --scores when given")
    ap.add_argument("--scores", default=None,
                    help="an existing e2d_score.py output whose EXCISED marker "
                         "rows are re-used, so the two contexts are compared "
                         "on identical rounds without rescoring one of them")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    print("INVOCATION: " + " ".join([sys.executable] + sys.argv), flush=True)

    assert_modules_absent(FORBIDDEN_MODULES)
    art = json.load(open(args.sessions))
    arms = tuple(a.strip() for a in args.arms.split(","))
    sessions = [s for s in art["sessions"] if s["arm"] in arms]
    marked = None
    if args.marks:
        marked = MRK.marked_set(MRK.load(args.marks))
    print(f"  {len(sessions)} sessions in arms {arms} from tier "
          f"{art.get('tier')} at frac {art.get('frac')}", flush=True)

    instruments, g = MK.instruments_or_stop()
    probes = json.load(open(os.path.join(
        DATA, "configs/e0_probes.json")))["probes"]
    n_gen = sum(1 for s in sessions
                for r in s["rounds"] + s["choices"] if r["text"].strip())
    print(f"  instrument G = {g:.6f}; {n_gen} generations x {len(probes)} "
          f"probes = {n_gen * len(probes)} in-situ forwards", flush=True)

    t0 = time.time()
    adapter = qwen_or_explain(__file__)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)

    t1 = time.time()
    rows_in_situ = MK.collect_in_situ(adapter, instruments, probes, sessions,
                                      progress=print)
    secs = time.time() - t1
    print(f"  in-situ scoring done in {secs / 60:.1f} min", flush=True)

    # EXCISED side: taken from the committed D2 scoring rather than rescored.
    # Those summaries were computed on the SAME rounds, with the SAME marks,
    # by the SAME estimator -- rescoring would spend an hour to reproduce
    # numbers that are already in the record, and any difference would be a
    # bug rather than a finding. If no --scores is offered, rescore.
    excised_from_record = None
    rows_excised = None
    if args.scores:
        sc = json.load(open(args.scores))
        mk = sc.get("marker") or {}
        key = {"M": "primary_paired_within_M", "R": "paired_within_R"}
        excised_from_record = {}
        for arm in arms:
            blk = mk.get(key.get(arm, ""))
            if not blk:
                excised_from_record = None
                break
            diffs = [p["diff"] for p in blk["per_session"]
                     if p["diff"] is not None]
            excised_from_record[arm] = {
                "paired_delta": blk["delta"],
                "n_sessions_decidable": blk["n_sessions_decidable"],
                "sd": blk.get("sd"),
                "sign_test": MK.sign_test(diffs),
                "per_session": blk["per_session"],
                "_source": os.path.relpath(args.scores, REPO)}
        if excised_from_record:
            pooled = mk.get("beside_pooled_and_across_arm")
            if pooled:
                excised_from_record["pooled_and_across_arm"] = pooled
            print(f"  excised side taken from {args.scores} "
                  f"(same rounds, same marks, same estimator -- not rescored)",
                  flush=True)
    if excised_from_record is None:
        print("  excised summaries not available from --scores; rescoring",
              flush=True)
        text_of = {r["task"]: r["task_text"]
                   for s in sessions for r in s["rounds"] + s["choices"]}
        rows_excised = MK.collect(adapter, instruments, probes, sessions,
                                  lambda tid: text_of[tid], progress=print)

    out = {"item": "e2d excision check", "addendum": "ADDENDUM-j1 (a)",
           "tier": art.get("tier"), "frac": art.get("frac"), "arms": list(arms),
           "G": g, "bar_half_G": MK.bar_from(g),
           "n_generations": n_gen,
           "n_in_situ_forwards": n_gen * len(probes),
           "in_situ_seconds": secs,
           "read_marks_applied": marked is not None,
           "provenance": adapter.provenance(),
           "_no_verdict": ("instrument characterisation; e2d closed on the "
                           "registered rule and this cannot reopen it")}

    blk = {}
    for arm in arms:
        pr = MK.paired_by_session(rows_in_situ, instruments, arm,
                                  clean_only=True, marked=marked)
        diffs = [p["diff"] for p in pr["per_session"] if p["diff"] is not None]
        blk[arm] = {"paired_delta": pr["delta"],
                    "n_sessions_decidable": pr["n_sessions_decidable"],
                    "sd": pr["sd"], "sign_test": MK.sign_test(diffs),
                    "per_session": pr["per_session"]}
    blk["pooled_and_across_arm"] = MK.deltas(rows_in_situ, instruments,
                                             clean_only=True)
    out["in_situ"] = blk

    if excised_from_record is not None:
        out["excised"] = excised_from_record
        out["excised_source"] = "committed D2 scoring (not rescored)"
    else:
        blk = {}
        for arm in arms:
            pr = MK.paired_by_session(rows_excised, instruments, arm,
                                      clean_only=True, marked=marked)
            diffs = [p["diff"] for p in pr["per_session"]
                     if p["diff"] is not None]
            blk[arm] = {"paired_delta": pr["delta"],
                        "n_sessions_decidable": pr["n_sessions_decidable"],
                        "sd": pr["sd"], "sign_test": MK.sign_test(diffs),
                        "per_session": pr["per_session"]}
        blk["pooled_and_across_arm"] = MK.deltas(rows_excised, instruments,
                                                 clean_only=True)
        out["excised"] = blk
        out["excised_source"] = "rescored in this run"

    # the comparison itself, computed before anything is written (trap 6)
    cmp_ = {}
    for arm in arms:
        a = out["in_situ"][arm]["paired_delta"]
        b = out["excised"][arm]["paired_delta"]
        cmp_[arm] = {"in_situ": a, "excised": b,
                     "difference": (None if a is None or b is None else a - b),
                     "same_sign": (None if a is None or b is None
                                   else (a > 0) == (b > 0))}
    out["comparison"] = cmp_

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1, default=float)

    print("\n" + "=" * 74)
    for arm in arms:
        c = cmp_[arm]
        print(f"  {arm}: in situ {c['in_situ']}  excised {c['excised']}  "
              f"same sign {c['same_sign']}")
    print(f"  wrote {args.out}  ({(time.time() - t0) / 60:.1f} min)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
