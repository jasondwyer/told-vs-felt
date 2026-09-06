#!/usr/bin/env python3
"""Blind re-screen of content-class v4 (the ADOPTED spec with the task_echo
guard and the widened null_response). AMENDMENT 2 (iii), adjudication of
2026-09-05 §2a: "Code implements the guard as a rule, re-screens blind as v4,
and the design seat re-eyeballs a fresh 14 + 14 before it becomes
exclusion-bearing."

Same three corpora and the same blind-to-arm discipline as the v3 screen
(scripts/e2d_contentclass_screen.py, frozen; its row builders are imported so
the corpora are identical). Reports per class and per STANDING
(exclusion-bearing vs advisory), the fresh 14 + 14 task_echo hits from e2a
and e2b for eyeballing, the widened null's hits, and -- beside, never as a
tuning -- what the declared novelty floor would give at 3 and 5.
"""
from __future__ import annotations

import argparse, collections, importlib.util, json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from valence_core.e2d import contentclass_v4 as V4                 # noqa: E402
from valence_core.e2d import contentclass as V3                    # noqa: E402

DATA = os.path.join(REPO, "data")
_spec = importlib.util.spec_from_file_location("ccs", os.path.join(REPO, "scripts/e2d_contentclass_screen.py"))
CCS = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(CCS)   # frozen row builders
TASKS = CCS.TASKS


def screen_v4(rows, floor=None):
    preds = []
    old = V4.NOVELTY_FLOOR
    if floor is not None:
        V4.NOVELTY_FLOOR = floor          # sensitivity beside only; restored below
    try:
        for r in rows:
            if r["audit"]:
                preds.append((None, None)); continue
            others = [t for t in TASKS if t != r["task"]]
            preds.append(V4.classify_v4(r["text"], r["task"], r["earlier"], others))
    finally:
        V4.NOVELTY_FLOOR = old
    return preds


def prf(rows, preds, keep):
    tp = sum(1 for r, (p, s) in zip(rows, preds) if r["marked"] and p and keep(s))
    fn = sum(1 for r, (p, s) in zip(rows, preds) if r["marked"] and not (p and keep(s)))
    fp = sum(1 for r, (p, s) in zip(rows, preds) if not r["marked"] and p and keep(s))
    tn = sum(1 for r, (p, s) in zip(rows, preds) if not r["marked"] and not (p and keep(s)))
    return {"tp": tp, "fn": fn, "fp": fp, "tn": tn,
            "recall": tp / (tp + fn) if tp + fn else None,
            "precision": tp / (tp + fp) if tp + fp else None}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(DATA, "e2d/contentclass_screen_v4.json"))
    ap.add_argument("--examples", type=int, default=14)
    args = ap.parse_args()
    print("INVOCATION: " + " ".join([sys.executable] + sys.argv), flush=True)
    ed = CCS.e2d_rounds(); ar = CCS.archive_rounds()
    pe, pa = screen_v4(ed), screen_v4(ar)
    pe3 = CCS.screen(ed); pa3 = CCS.screen(ar)          # v3, for the delta
    print(f"  e2d {len(ed)} rounds; archive {len(ar)} ({collections.Counter(r['corpus'] for r in ar)})", flush=True)
    out = {"spec_version": V4.SPEC_VERSION, "blind_to_arm": True,
           "declared_before_screen": {"NOVELTY_FLOOR": V4.NOVELTY_FLOOR, "NULL_RESIDUAL_WORDS": V4.NULL_RESIDUAL_WORDS, "run": 5, "verb_lexicon": "v3, frozen"},
           "standing": {"exclusion_bearing": list(V4.EXCLUSION_BEARING), "advisory": list(V4.ADVISORY)},
           "e2d": {"n": len(ed),
                   "all_classes_vs_read": prf(ed, pe, lambda s: s is not None),
                   "exclusion_bearing_vs_read": prf(ed, pe, lambda s: s == "exclusion"),
                   "predicted_by_class": dict(collections.Counter(p for p, _ in pe if p)),
                   "v3_for_delta": {"predicted_by_class": dict(collections.Counter(p for p in pe3 if p))},
                   "in_sample_caveat": "the v3 draft was revised against this corpus; v4 adds a declared guard and a widened class without further tuning"},
           "archive_overbreadth": {}, "fresh_examples_for_eyeballing": {}}
    # per-class precision/recall vs the read's marks (the read marks a round, not a class -- so per class this is hit-rate among marked vs unmarked)
    per_class = {}
    for c in V4.CLASSES:
        hits_marked = sum(1 for r, (p, _) in zip(ed, pe) if p == c and r["marked"])
        hits_unmarked = sum(1 for r, (p, _) in zip(ed, pe) if p == c and not r["marked"])
        per_class[c] = {"hits_on_marked_rounds": hits_marked, "hits_on_unmarked_rounds": hits_unmarked,
                        "precision_vs_read": hits_marked / (hits_marked + hits_unmarked) if hits_marked + hits_unmarked else None}
    out["e2d"]["per_class_vs_read"] = per_class
    for corpus in ("e2a", "e2b"):
        sub = [(r, p) for r, p in zip(ar, pa) if r["corpus"] == corpus]
        hits = [(r, p) for r, p in sub if p[0]]
        excl = [(r, p) for r, p in hits if p[1] == "exclusion"]
        adv = [(r, p) for r, p in hits if p[1] == "advisory"]
        v3hits = sum(1 for r, p in zip(ar, pa3) if r["corpus"] == corpus and p)
        out["archive_overbreadth"][corpus] = {
            "n": len(sub), "hits_all": len(hits), "rate_all": len(hits) / len(sub),
            "hits_exclusion_bearing": len(excl), "rate_exclusion_bearing": len(excl) / len(sub),
            "hits_advisory": len(adv), "rate_advisory": len(adv) / len(sub),
            "by_class": dict(collections.Counter(p[0] for _, p in hits)),
            "v3_hits_for_delta": v3hits}
        echo = [(r, p) for r, p in hits if p[0] == "task_echo"]
        nulls = [(r, p) for r, p in hits if p[0] == "null_response"]
        out["fresh_examples_for_eyeballing"][corpus] = {
            "task_echo_v4_hits_total": len(echo),
            "task_echo": [{"task": r["task"][:90], "text": r["text"][:200], "novelty": V4.novelty(r["text"], r["task"])} for r, _ in echo[:args.examples]],
            "null_response_v4_hits_total": len(nulls),
            "null_response": [{"task": r["task"][:90], "text": r["text"][:200]} for r, _ in nulls[:args.examples]]}
    # the archives hold fewer than 14 + 14 v4 echo hits; supplement with the
    # e2d echo hits (in-sample; the read's mark is shown beside each)
    ed_echo = [(r, p) for r, p in zip(ed, pe) if p[0] == "task_echo"]
    out["fresh_examples_for_eyeballing"]["e2d_supplement_in_sample"] = {
        "task_echo_v4_hits_total": len(ed_echo),
        "task_echo": [{"task": r["task"][:90], "text": r["text"][:200], "novelty": V4.novelty(r["text"], r["task"]),
                       "read_marked": bool(r["marked"])} for r, _ in ed_echo[:args.examples]]}
    # per-arm, joined back only now
    by_arm = collections.Counter(); tot = collections.Counter(); by_arm_excl = collections.Counter()
    for r, (p, s) in zip(ed, pe):
        tot[r["_arm"]] += 1
        if p: by_arm[r["_arm"]] += 1
        if s == "exclusion": by_arm_excl[r["_arm"]] += 1
    out["e2d"]["by_arm_unblinded_after"] = {a: {"hits_all": by_arm[a], "hits_exclusion_bearing": by_arm_excl[a], "rounds": tot[a],
                                                "rate_all": by_arm[a] / tot[a], "rate_exclusion_bearing": by_arm_excl[a] / tot[a]} for a in sorted(tot)}
    # novelty-floor sensitivity, beside (the declared floor stands)
    sens = {}
    for fl in (3, 4, 5):
        pe_f = screen_v4(ed, floor=fl); pa_f = screen_v4(ar, floor=fl)
        sens[str(fl)] = {"e2d_echo_hits": sum(1 for p, _ in pe_f if p == "task_echo"),
                         "e2d_echo_on_marked": sum(1 for r, (p, _) in zip(ed, pe_f) if p == "task_echo" and r["marked"]),
                         "e2a_echo_hits": sum(1 for r, (p, _) in zip(ar, pa_f) if r["corpus"] == "e2a" and p == "task_echo"),
                         "e2b_echo_hits": sum(1 for r, (p, _) in zip(ar, pa_f) if r["corpus"] == "e2b" and p == "task_echo")}
    out["novelty_floor_sensitivity_beside"] = {"declared": V4.NOVELTY_FLOOR, "not_a_tuning": True, "by_floor": sens}
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    e = out["e2d"]
    print(f"  e2d vs the read, all classes: recall {e['all_classes_vs_read']['recall']:.3f} precision {e['all_classes_vs_read']['precision']:.3f}  (TP {e['all_classes_vs_read']['tp']} FN {e['all_classes_vs_read']['fn']} FP {e['all_classes_vs_read']['fp']})")
    print(f"  e2d vs the read, exclusion-bearing only: recall {e['exclusion_bearing_vs_read']['recall']:.3f} precision {e['exclusion_bearing_vs_read']['precision']:.3f}  (TP {e['exclusion_bearing_vs_read']['tp']} FN {e['exclusion_bearing_vs_read']['fn']} FP {e['exclusion_bearing_vs_read']['fp']})")
    print(f"  e2d predicted by class v4: {e['predicted_by_class']}   (v3: {e['v3_for_delta']['predicted_by_class']})")
    print(f"  per class vs read: { {c: (v['hits_on_marked_rounds'], v['hits_on_unmarked_rounds']) for c, v in per_class.items()} }  (marked, unmarked)")
    for c, v in out["archive_overbreadth"].items():
        print(f"  {c} overbreadth: all {v['hits_all']}/{v['n']} = {v['rate_all']:.4f}; exclusion-bearing {v['hits_exclusion_bearing']} = {v['rate_exclusion_bearing']:.4f}; advisory {v['hits_advisory']}; by class {v['by_class']}; v3 hits {v['v3_hits_for_delta']}")
    print(f"  per-arm (unblinded after): { {a: (round(v['rate_all'], 4), round(v['rate_exclusion_bearing'], 4)) for a, v in e['by_arm_unblinded_after'].items()} }  (all, exclusion-bearing)")
    print(f"  novelty floor sensitivity (declared {V4.NOVELTY_FLOOR}): {sens}")
    print(f"  wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
