#!/usr/bin/env python3
"""e2d scoring — marker readout and readability ladders over a sessions file.

Split out from the runner by PROPOSAL-j v1.2 AMENDMENT 2 (iii): the rule-25
read is Q2's arbiter, and the read cannot exist until the sessions do. So
generation and scoring are separate passes and the marks file is an input
here, not an afterthought.

WHAT THIS PRODUCES, all of it measurement and none of it a criterion:

  MARKER (AMENDMENT 2 (iv))
    Delta+  within M, PAIRED BY SESSION -- Q3's ratified primary
    Delta_R within R, the same estimator
    beside, labelled: the pooled within-arm form, the across-arm form vs the
    S arm, and task-matched pairs where task_ids coincide
    paired sign test and a seeded sign-flip permutation test

  READABILITY (AMENDMENT 2 (iii))
    k = 2 resampled ladder on **v2-clean AND read-clean** rounds -- Q2's set
    the same on v2-clean alone, reported beside
    k = 1, all-rounds, and AUC_R on arm R, all descriptive
    a stored classifier for the campaign transfer figure

The criteria live in `scripts/e2d_d2_analyze.py`. This script computes no
verdict and writes no canonical artifact of another tier's.
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
from valence_core.e2d import habit as HB                          # noqa: E402
from valence_core.e2d import marker as MK                         # noqa: E402
from valence_core.e2d import marks as MRK                         # noqa: E402
from valence_core.e2d import readability as RD                    # noqa: E402
from valence_core.e2d.runner import FORBIDDEN_MODULES             # noqa: E402
from valence_core.session import assert_modules_absent            # noqa: E402

DATA = os.path.join(REPO, "data")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sessions", required=True)
    ap.add_argument("--marks", default=None,
                    help="the rule-25 read-marks file (AMENDMENT 2 (iii)). "
                         "Omitted -> Q2's clean set is v2-clean only and the "
                         "output says so.")
    ap.add_argument("--out", required=True)
    ap.add_argument("--b", type=int, default=RD.B_RESAMPLES)
    ap.add_argument("--no-marker", action="store_true")
    ap.add_argument("--no-ladder", action="store_true")
    args = ap.parse_args()
    print("INVOCATION: " + " ".join([sys.executable] + sys.argv), flush=True)

    assert_modules_absent(FORBIDDEN_MODULES)
    art = json.load(open(args.sessions))
    sessions = art["sessions"]
    tier = art.get("tier", "?")
    print(f"  sessions: {len(sessions)} from tier {tier} at frac "
          f"{art.get('frac')}, round path "
          f"{'CACHED' if art.get('round_path_cached') else 'UNCACHED'}",
          flush=True)

    marked = None
    marks_doc = None
    if args.marks:
        marks_doc = MRK.load(args.marks)
        marked = MRK.marked_set(marks_doc)
        print(f"  read-marks: {len(marks_doc['marks'])} marks over "
              f"{len({(m['arm'], m['session']) for m in marks_doc['marks']})} "
              f"sessions, reader {marks_doc['reader']!r} -- PROVISIONAL",
              flush=True)
    else:
        print("  read-marks: NONE SUPPLIED -- Q2's clean set will be v2-clean "
              "only, and the output records that", flush=True)

    t0 = time.time()
    adapter = qwen_or_explain(__file__)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)

    out = {"item": "e2d scoring", "tier": tier, "frac": art.get("frac"),
           "sessions_file": os.path.relpath(args.sessions, REPO),
           "marks_file": (os.path.relpath(args.marks, REPO)
                          if args.marks else None),
           "read_marks_applied": marked is not None,
           "provenance": adapter.provenance()}

    # --- descriptive tables that need no model ---------------------------
    out["audit_rates_by_round_class"] = MRK.audit_rates(sessions)
    if marks_doc is not None:
        out["read_mark_rates"] = MRK.tabulate(marks_doc, sessions)
    out["habit"] = {"frame_M": HB.frame(sessions, "M"),
                    "secondaries": HB.secondaries(sessions)}

    # --- marker (AMENDMENT 2 (iv)) ---------------------------------------
    if not args.no_marker:
        instruments, g = MK.instruments_or_stop()
        probes = json.load(open(os.path.join(
            DATA, "configs/e0_probes.json")))["probes"]
        print(f"  marker instrument: G = {g:.6f}, bar 0.5*G = "
              f"{MK.bar_from(g):.4f}, {len(probes)} probes", flush=True)
        text_of = {r["task"]: r["task_text"]
                   for s in sessions for r in s["rounds"] + s["choices"]}
        t1 = time.time()
        rows = MK.collect(adapter, instruments, probes, sessions,
                          lambda tid: text_of[tid], progress=print)
        n_fw = sum(len(r["scores"]) for r in rows if r["scores"])
        print(f"    {n_fw} probe forwards in {time.time() - t1:.0f}s",
              flush=True)

        prim_M = MK.paired_by_session(rows, instruments, "M",
                                      clean_only=True, marked=marked)
        prim_R = MK.paired_by_session(rows, instruments, "R",
                                      clean_only=True, marked=marked)
        diffs_M = [p["diff"] for p in prim_M["per_session"]
                   if p["diff"] is not None]
        diffs_R = [p["diff"] for p in prim_R["per_session"]
                   if p["diff"] is not None]
        out["marker"] = {
            "G": g, "bar_half_G": MK.bar_from(g),
            "n_generations_scored": sum(1 for r in rows if r["scores"]),
            "n_skipped": sum(1 for r in rows if r["skipped"]),
            "n_probe_forwards": n_fw,
            "seconds": time.time() - t1,
            # AMENDMENT 2 (iv): this is Q3's primary.
            "primary_paired_within_M": prim_M,
            "paired_within_R": prim_R,
            "sign_test_M": MK.sign_test(diffs_M),
            "sign_flip_test_M": MK.sign_flip_test(diffs_M),
            "sign_test_R": MK.sign_test(diffs_R),
            # reported beside, labelled
            "beside_pooled_and_across_arm": MK.deltas(rows, instruments,
                                                      clean_only=True),
            "beside_task_matched_M": MK.task_matched(rows, instruments, "M",
                                                     marked=marked),
            "beside_task_matched_R": MK.task_matched(rows, instruments, "R",
                                                     marked=marked),
        }
        if marked is not None:
            # the same primary WITHOUT the read-marks, so the marks' effect on
            # Q3 is visible rather than absorbed
            out["marker"]["primary_paired_within_M_v2clean_only"] = \
                MK.paired_by_session(rows, instruments, "M", clean_only=True,
                                     marked=None)

    # --- readability (AMENDMENT 2 (iii)) ---------------------------------
    if not args.no_ladder:
        t2 = time.time()
        lad = {}
        sets = [("v2_and_read_clean", marked)] if marked is not None else []
        sets.append(("v2_clean_only", None))
        for name, mk in sets:
            rounds_M = RD.clean_rounds(sessions, "M", marked=mk)
            entry = {"n_clean_pos": len(rounds_M["pos"]),
                     "n_clean_neg": len(rounds_M["neg"])}
            if rounds_M["pos"] and rounds_M["neg"]:
                entry["k2"] = RD.resampled_auc(adapter, rounds_M, k=2,
                                               b=args.b, key=f"e2d-{tier}")
                entry["k1"] = RD.resampled_auc(adapter, rounds_M, k=1,
                                               b=args.b, key=f"e2d-{tier}")
                entry["gate_would_say"] = RD.gate(entry["k2"])
            else:
                entry["why"] = "one pole had no rounds after filtering"
            lad[name] = entry
            print(f"    ladder[{name}]: pos {entry['n_clean_pos']} / neg "
                  f"{entry['n_clean_neg']}"
                  + (f", k2 median {entry['k2']['median']:.4f}"
                     if "k2" in entry and entry["k2"]["median"] is not None
                     else ""), flush=True)

        # all-rounds (degeneracy included) and AUC_R, both descriptive
        allr = RD.clean_rounds(sessions, "M", marked=None)
        allr_incl = {"pos": [], "neg": []}
        for s in sessions:
            if s["arm"] != "M":
                continue
            for r in s["rounds"] + s["choices"]:
                if not r["text"].strip():
                    continue
                allr_incl["pos" if r["steered"] else "neg"].append(
                    {"text": r["text"], "task_id": r["task"]})
        if allr_incl["pos"] and allr_incl["neg"]:
            lad["all_rounds_degeneracy_included"] = RD.resampled_auc(
                adapter, allr_incl, k=2, b=args.b, key=f"e2d-{tier}-all")
        rounds_R = RD.clean_rounds(sessions, "R", marked=marked)
        if rounds_R["pos"] and rounds_R["neg"]:
            lad["AUC_R"] = RD.resampled_auc(adapter, rounds_R, k=2, b=args.b,
                                            key=f"e2d-{tier}-R")
        # stored classifier for the campaign transfer figure
        base = RD.clean_rounds(sessions, "M", marked=marked)
        if base["pos"] and base["neg"]:
            clf = RD.fit_and_store(adapter, base, k=2, key=f"e2d-{tier}")
            lad["stored_classifier"] = {
                "k": clf["k"], "n_fit": clf["n_fit"],
                "hyperparams": clf["hyperparams"],
                "w": clf["w"].tolist(), "b": clf["b"],
                "mu": clf["mu"].tolist(), "sd": clf["sd"].tolist(),
                "self_score": RD.score_stored(adapter, clf, base,
                                              key=f"e2d-{tier}")}
        lad["seconds"] = time.time() - t2
        out["readability"] = lad

    out["wall_clock_s"] = time.time() - t0
    out["_no_verdict"] = ("measurement only; the criteria live in "
                          "scripts/e2d_d2_analyze.py")
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1, default=float)
    print(f"\n  wrote {args.out}  ({out['wall_clock_s']:.0f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
