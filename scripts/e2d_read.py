#!/usr/bin/env python3
"""Rule-25 read helper — dump transcripts for reading, validate marks.

AMENDMENT 2 (iii) makes the read the arbiter at D2. This script exists to
make that read practical over 64 sessions and to keep its output honest. It
is DELIBERATELY NOT A DETECTOR: it contains no patterns, no heuristics and no
candidate classifier for content-shaped junk.

That omission is the point. The class-level spec for scorer_v3 is drafted
AFTER the read and screened for overbreadth against the archives; a detector
written before the read would supply the categories the read is supposed to
discover, and the reader would then confirm the detector instead of the
transcripts. v1 and v2 each fixed the instance and missed the class, and the
ordering the amendment sets is what stops a third repeat.

  dump      every round of every session, with a stable key per round, so a
            mark can be attached to exactly the round that earned it
  validate  a marks file against the sessions it claims to describe: keys
            resolve, classes are the four closed ones, no duplicates
  tabulate  the marked-round rates the entry reports

Usage:
    python scripts/e2d_read.py dump     --sessions data/e2d/d2_sessions.json
    python scripts/e2d_read.py validate --sessions ... --marks ...
    python scripts/e2d_read.py tabulate --sessions ... --marks ...
"""
from __future__ import annotations

import argparse
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from valence_core.e2d import marks as MRK                         # noqa: E402


def dump(sessions, only_arm=None, with_text=True) -> None:
    for s in sessions:
        if only_arm and s["arm"] != only_arm:
            continue
        c = s["cell"]
        print("=" * 78)
        print(f"{s['arm']} s{s['session']}  pair={c['pair']} map={c['map']} "
              f"forced_end={c['forced_end']} tag_plus={s['tag_plus']}  "
              f"excluded={s['excluded']} {s['exclude_reason'] or ''}")
        for r in list(s["rounds"]) + list(s["choices"]):
            flags = []
            if r["degen"]:
                flags.append(f"AUDIT:{r['degen']}")
            if r.get("lexical"):
                flags.append(f"LEX:{r['lexical']}")
            if r["steered"]:
                flags.append("+axis")
            if r.get("cap_hit"):
                flags.append("CAP")
            print(f"  [{s['arm']}|{s['session']}|{r['phase']}] "
                  f"task={r['task']} {' '.join(flags)}")
            print(f"      TASK: {r['task_text']}")
            if with_text:
                print(f"      RESP: {r['text']!r}")


def validate(sessions, doc) -> int:
    keys = {f"{s['arm']}|{s['session']}|{r['phase']}"
            for s in sessions for r in list(s["rounds"]) + list(s["choices"])}
    problems = []
    seen = set()
    for m in doc["marks"]:
        k = f"{m['arm']}|{m['session']}|{m['phase']}"
        if k not in keys:
            problems.append(f"no such round: {k}")
        if k in seen:
            problems.append(f"duplicate mark on {k}")
        seen.add(k)
        if m["class"] not in MRK.CLASSES:
            problems.append(f"unknown class {m['class']!r} on {k}")
        if not str(m.get("reason", "")).strip():
            problems.append(f"empty reason on {k} -- a mark without a reason "
                            f"is not a read, it is an assertion")
    print(f"  marks: {len(doc['marks'])} over {len(seen)} distinct rounds "
          f"of {len(keys)} total")
    if problems:
        print("  PROBLEMS:")
        for p in problems:
            print(f"    {p}")
        return 1
    print("  VALID: every key resolves, every class is one of the four, "
          "no duplicates, every mark carries a reason")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=("dump", "validate", "tabulate"))
    ap.add_argument("--sessions", required=True)
    ap.add_argument("--marks", default=None)
    ap.add_argument("--arm", default=None)
    ap.add_argument("--no-text", action="store_true")
    args = ap.parse_args()

    art = json.load(open(args.sessions))
    sessions = art["sessions"]
    if args.action == "dump":
        dump(sessions, args.arm, not args.no_text)
        return 0
    if not args.marks:
        raise SystemExit(f"{args.action} needs --marks")
    doc = MRK.load(args.marks)
    if args.action == "validate":
        return validate(sessions, doc)
    print(json.dumps(MRK.tabulate(doc, sessions), indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
