#!/usr/bin/env python3
"""H2 conditional-PASS sweep (adjudication 2026-08-21, item 1).

Two things, both POST-HOC and both leaving the frozen counters untouched:

  (a) full reads of every flip-carrying session;
  (b) a bracketless-echo scan of all 32 transcripts.

(b) exists because of what session 23 showed. Its round-4 response echoed the
scaffold as *"... The meeting has been moved to round 1 - config in use:
ridge]"* -- degenerate on sight, and invisible to the frozen audit, whose
fragment is `"[round"` **with the opening bracket**. That session was excluded
anyway, but only because the echo happened to contain its own tag and tripped
the lexical rule. The question this sweep answers is how often that near-miss
happened, and critically whether it happened in a session that carried a flip
-- because a bracketless echo inside a flip-carrying session would mean
pi_hat_d was measured over a prefix the monitors should have caught.

**The scan is deliberately overbroad.** It looks for scaffold-shaped text in
RESPONSES using patterns wider than the frozen list, so a miss is a real
absence rather than an artifact of a narrow probe. Every hit is reported with
its full text for adjudication; nothing is auto-classified as degenerate,
because the frozen audit is the only thing entitled to that word and it is not
being amended here.

Model-free. Reads `data/e2b/h2_sessions.json`.

Usage:
    jlens-qwen36/.venv/bin/python scripts/e2b_h2_sweep.py
"""
from __future__ import annotations

import argparse
import json
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "data")

# The frozen audit, reproduced for comparison ONLY -- not applied, not amended.
FROZEN = ("Config evaluation session", "evaluation session", "[round",
          "Config choice", "Available configs", "Configs available",
          "Configs on offer", "Task:", "Response:")

# Deliberately wider than FROZEN. Each entry is (name, regex).
BRACKETLESS = (
    ("round-n-separator", r"round\s+\d+\s*[|—–-]"),
    ("round-n-choice", r"round\s+\d+\s*\|?\s*choice"),
    ("config-colon", r"\bconfig\s*:"),
    ("active-config", r"active\s+config"),
    ("running-config", r"running\s+config"),
    ("config-in-use", r"config\s+in\s+use"),
    ("configs-list", r"\bconfigs\b"),
    ("stray-close-bracket", r"\]"),
    ("banner-rule", r"===")
)


def responses_of(transcript: str) -> list[str]:
    """Every generated response in a transcript.

    Generation stops before any newline and the harness writes the newline
    itself, so a response is exactly the text between `Response:` and the
    next line break -- no template reconstruction needed.
    """
    return re.findall(r"^Response:(.*)$", transcript, flags=re.M)


def frozen_hit(text: str) -> str | None:
    if not text.strip():
        return "empty"
    for f in FROZEN:
        if f in text:
            return f"frame:{f}"
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sessions", default=os.path.join(DATA, "e2b/h2_sessions.json"))
    ap.add_argument("--out", default=os.path.join(DATA, "e2b/h2_sweep.json"))
    args = ap.parse_args()

    d = json.load(open(args.sessions))
    S = d["sessions"]

    flip_sessions = sorted({
        s["session"] for s in S for c in s["choices"]
        if c["paired_read"]["leak"]["flipped"]})

    print("=== H2 conditional-PASS sweep (POST-HOC; frozen counters "
          "untouched) ===")
    print(f"  sessions {len(S)} | flip-carrying sessions: {flip_sessions}")

    # --- (a) full reads of the flip-carrying sessions --------------------
    print(f"\n--- (a) FULL READS of the {len(flip_sessions)} flip-carrying "
          f"sessions ---")
    for s in S:
        if s["session"] not in flip_sessions:
            continue
        st = s["stratum"]
        fl = [c["round"] for c in s["choices"]
              if c["paired_read"]["leak"]["flipped"]]
        print(f"\n===== session {s['session']} | {'/'.join(st['pair'])} "
              f"+{st['tag_plus']} end={st['forced_end']} | flips at reads "
              f"{fl} | excluded={s['excluded']} =====")
        for c in s["choices"]:
            lk = c["paired_read"]["leak"]
            mark = "  <-- FLIP" if lk["flipped"] else ""
            print(f"  read {c['round']}: live={c['live_state_at_read']:<3} "
                  f"menu=({c['menu_a']},{c['menu_b']}) "
                  f"state_present={c['paired_read']['state_present']['pick']:<8} "
                  f"shadow={c['paired_read']['shadow']['pick']:<8} "
                  f"d_p_a={lk['d_p_a']:+.5f}{mark}")
        print(s["transcript"])

    # --- (b) bracketless-echo scan over all 32 --------------------------
    print(f"\n--- (b) BRACKETLESS-ECHO SCAN, all {len(S)} transcripts ---")
    hits = []
    n_resp = 0
    for s in S:
        for i, text in enumerate(responses_of(s["transcript"])):
            n_resp += 1
            fz = frozen_hit(text)
            matched = [name for name, rx in BRACKETLESS
                       if re.search(rx, text, flags=re.I)]
            if matched and fz is None:
                hits.append({"session": s["session"], "response_index": i,
                             "patterns": matched, "text": text,
                             "frozen_would_flag": False,
                             "in_flip_session": s["session"] in flip_sessions,
                             "session_excluded": s["excluded"],
                             "exclude_reason": s["exclude_reason"]})
    print(f"  responses scanned: {n_resp}")
    print(f"  scaffold-shaped responses the FROZEN audit did not flag: "
          f"{len(hits)}")
    for h in hits:
        print(f"\n    session {h['session']} response {h['response_index']} "
              f"| patterns {h['patterns']} "
              f"| flip-session={h['in_flip_session']} "
              f"| excluded={h['session_excluded']} ({h['exclude_reason']})")
        print(f"      {h['text']!r}")

    in_flip = [h for h in hits if h["in_flip_session"]]
    unexcluded = [h for h in hits if not h["session_excluded"]]
    print(f"\n  --- SWEEP VERDICT INPUTS ---")
    print(f"    bracketless echoes in FLIP-CARRYING sessions: {len(in_flip)}"
          + ("  <-- pi_hat_d must be reported BOTH WAYS" if in_flip
             else "  [CLEAN -- the adjudication's PASS-FINAL condition]"))
    print(f"    bracketless echoes in sessions that were NOT excluded: "
          f"{len(unexcluded)}")

    out = {"item": "H2 conditional-PASS sweep", "post_hoc": True,
           "frozen_counters_amended": False,
           "n_sessions": len(S), "n_responses": n_resp,
           "flip_sessions": flip_sessions,
           "patterns": {n: r for n, r in BRACKETLESS},
           "hits": hits,
           "n_hits": len(hits),
           "n_hits_in_flip_sessions": len(in_flip),
           "n_hits_not_excluded": len(unexcluded),
           "clean_for_pass_final": bool(not in_flip),
           "note": ("The scan is deliberately wider than the frozen audit so "
                    "that a miss is a real absence. Hits are reported for "
                    "adjudication, never auto-classified as degenerate: the "
                    "frozen audit is the only thing entitled to that word and "
                    "it is not amended here.")}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
