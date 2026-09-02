#!/usr/bin/env python3
"""Overbreadth screen for the content-class draft. AMENDMENT 2 (iii).

BLIND TO ARM: the detector never sees which arm a round came from, and the
arm is joined back only for the final report. That is the same discipline
audit v2 was screened under, and it matters here more than there, because the
D2 read found content-shaped junk concentrated in the axis arm -- a detector
tuned while watching the arm labels could manufacture that result.

THREE CORPORA, and they answer different questions:
  e2d (912 rounds, marks available)  precision/recall against the read
  e2a archive (1,894 responses)      overbreadth on a corpus with no marks
  e2b campaign (1,707 rounds)        the same, on the state-present corpus

Precision and recall on e2d are IN-SAMPLE: the draft was revised after seeing
where it failed on this corpus, so those two numbers are the optimistic end.
The e2a and e2b hit rates are the out-of-sample check, and hits there are
listed for eyeballing rather than assumed to be true positives -- which is how
audit v2 was screened ("the bar was met by the screen reclassifying its own
reference set").

This adopts nothing. It produces a screened candidate for adjudication.
"""
from __future__ import annotations

import argparse, collections, json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from valence_core.e2d import contentclass as CC                   # noqa: E402
from valence_core.e2d import marks as MRK                         # noqa: E402

DATA = os.path.join(REPO, "data")
TASKS = [p for l in open(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
         if l.strip() for p in json.loads(l)["paraphrases"]]


def e2d_rounds():
    out = []
    for tier in ("d1", "d2", "d3"):
        path = os.path.join(DATA, f"e2d/{tier}_sessions.json")
        if not os.path.exists(path):
            continue
        ss = json.load(open(path))["sessions"]
        mk = MRK.marked_set(MRK.load(os.path.join(
            DATA, f"e2d/{tier}_read_marks.json")))
        for s in ss:
            earlier = []
            for r in s["rounds"] + s["choices"]:
                out.append({"corpus": tier, "text": r["text"],
                            "task": r["task_text"], "earlier": list(earlier),
                            "audit": r["degen"],
                            "marked": f"{s['arm']}|{s['session']}|{r['phase']}" in mk,
                            "_arm": s["arm"]})
                earlier.append(r["text"])
    return out


HDR = re.compile(r'^\[round .*\]$', re.M)
MENU = ("Configs available", "Options:", "Configs on offer", "Available configs")


def transcript_rounds(transcript, corpus):
    """(task, response) pairs from an archived transcript."""
    lines = transcript.split("\n"); out = []; i = 0; earlier = []
    while i < len(lines):
        if re.match(r'^\[round .*\]$', lines[i]):
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if nxt.startswith("Task:"):
                task = nxt[len("Task:"):].strip()
                j = i + 2
                if j >= len(lines) or not lines[j].startswith("Response:"):
                    i += 1; continue
                buf = [lines[j][len("Response:"):]]; j += 1
                while j < len(lines):
                    if re.match(r'^\[round .*\]$', lines[j]):
                        n2 = lines[j + 1] if j + 1 < len(lines) else ""
                        if n2.startswith("Task:") or any(n2.startswith(p) for p in MENU):
                            break
                    buf.append(lines[j]); j += 1
                txt = "\n".join(buf).strip()
                out.append({"corpus": corpus, "text": txt, "task": task,
                            "earlier": list(earlier), "audit": None,
                            "marked": None, "_arm": None})
                earlier.append(txt); i = j; continue
            if any(nxt.startswith(p) for p in MENU):
                j = i + 1
                while j < len(lines) and not re.match(r'^\[round .*\]$', lines[j]):
                    j += 1
                i = j; continue
        i += 1
    return out


def archive_rounds():
    out = []
    p = os.path.join(DATA, "e2a/sessions.jsonl")
    if os.path.exists(p):
        for l in open(p):
            if l.strip():
                out += transcript_rounds(json.loads(l)["transcript"], "e2a")
    p = os.path.join(DATA, "e2b/verdict_campaign.json")
    if os.path.exists(p):
        for s in json.load(open(p))["sessions"]:
            if s.get("transcript"):
                out += transcript_rounds(s["transcript"], "e2b")
    return out


def screen(rows):
    preds = []
    for r in rows:
        # rule 28(b): a round the audit already claimed is not offered here,
        # exactly as it is not offered to the read.
        if r["audit"]:
            preds.append(None); continue
        others = [t for t in TASKS if t != r["task"]]
        preds.append(CC.classify(r["text"], r["task"], r["earlier"], others))
    return preds


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(DATA, "e2d/contentclass_screen.json"))
    ap.add_argument("--show", type=int, default=10)
    args = ap.parse_args()
    print("INVOCATION: " + " ".join([sys.executable] + sys.argv), flush=True)

    ed = e2d_rounds(); ar = archive_rounds()
    pe, pa = screen(ed), screen(ar)
    print(f"  e2d {len(ed)} rounds; archive {len(ar)} rounds "
          f"({collections.Counter(r['corpus'] for r in ar)})", flush=True)

    tp = sum(1 for r, p in zip(ed, pe) if r["marked"] and p)
    fn = sum(1 for r, p in zip(ed, pe) if r["marked"] and not p)
    fp = sum(1 for r, p in zip(ed, pe) if not r["marked"] and p)
    tn = sum(1 for r, p in zip(ed, pe) if not r["marked"] and not p)
    out = {"spec_version": CC.SPEC_VERSION, "blind_to_arm": True,
           "adopted": False,
           "e2d": {"n": len(ed), "tp": tp, "fn": fn, "fp": fp, "tn": tn,
                   "recall": tp / (tp + fn) if tp + fn else None,
                   "precision": tp / (tp + fp) if tp + fp else None,
                   "in_sample_caveat": ("the draft was revised after seeing "
                                        "where it failed on this corpus; "
                                        "these are the optimistic end"),
                   "predicted": dict(collections.Counter(p for p in pe if p))},
           "archive_overbreadth": {}}
    for corpus in ("e2a", "e2b"):
        sub = [(r, p) for r, p in zip(ar, pa) if r["corpus"] == corpus]
        hits = [(r, p) for r, p in sub if p]
        out["archive_overbreadth"][corpus] = {
            "n": len(sub), "hits": len(hits),
            "rate": len(hits) / len(sub) if sub else None,
            "by_class": dict(collections.Counter(p for _, p in hits)),
            "examples": [{"class": p, "task": r["task"][:70],
                          "text": r["text"][:160]} for r, p in hits[:args.show]]}
    # per-arm, joined back only now
    by_arm = collections.Counter()
    tot_arm = collections.Counter()
    for r, p in zip(ed, pe):
        tot_arm[r["_arm"]] += 1
        if p:
            by_arm[r["_arm"]] += 1
    out["e2d"]["by_arm_unblinded_after"] = {
        a: {"hits": by_arm[a], "rounds": tot_arm[a],
            "rate": by_arm[a] / tot_arm[a]} for a in sorted(tot_arm)}

    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    e = out["e2d"]
    print(f"  e2d vs the read: recall {e['recall']:.3f} precision "
          f"{e['precision']:.3f}  (TP {tp} FN {fn} FP {fp})")
    for c, v in out["archive_overbreadth"].items():
        print(f"  {c} overbreadth: {v['hits']}/{v['n']} = {v['rate']:.4f}  "
              f"{v['by_class']}")
    print(f"  per-arm (unblinded after scoring): "
          f"{ {a: round(v['rate'], 4) for a, v in e['by_arm_unblinded_after'].items()} }")
    print(f"  wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
