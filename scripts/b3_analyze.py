#!/usr/bin/env python3
"""B3 analysis -- the screen trigger and the confirm criteria. LOCK-g §4.

COMMITTED BEFORE ANY CAMPAIGN RUNS, deliberately. An analysis script authored
after seeing the data is a different instrument from one authored before it,
however identical the code, and only one of them can be shown to have been.
That is the e2b pattern (analyzer at `a2f074d`, campaign after) and it is
being kept.

THE STATISTIC. Delta_first = (share of valid marker sessions whose FIRST free
choice took the +tag) - 0.5. Delta is a share MINUS CHANCE, not a doubled
share -- the convention of record, fixed by e2b's 47/96 -> -0.0104 and
re-verified in the LOCK-g §7 check.

SCREEN TRIGGER (LOCK-g §4, no binomial at this tier), conjunctively:
  (i)  |Delta_first| exceeds the campaign's OWN realised control envelope --
       max |pseudo-Delta| over the sham and random families, the identical
       statistic computed on arms where no contingency exists;
  (ii) the sign LOCKS across label maps.

CONFIRM TIER adds, and requires all three:
  (iii) one-sided exact binomial p <= .05 at n = 96 (critical k >= 57).

Direction is pre-registered as approach: a significant REVERSE result is
reported as an unexpected-direction finding, never as a pass. Each conjunct
is reported separately, because a criterion that can only be reported as a
single word is one whose failure mode is invisible.

PRE-NAMED COLLATERAL (LOCK-g §4), reported and deciding nothing: the
first-choice-only information structure, and session-share -- which at ~.50
is not evidence of anything.

A smoke artifact is refused outright (rc=2). Smokes are not campaigns.

Usage:
    jlens-qwen36/.venv/bin/python scripts/b3_analyze.py --in data/olmo/b3_screen_base.json
    jlens-qwen36/.venv/bin/python scripts/b3_analyze.py --selftest
"""
from __future__ import annotations

import argparse
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from valence_core.stats import binom_sf_inclusive                 # noqa: E402

ALPHA = 0.05
CONFIRM_N = 96


def delta(sessions, arm) -> tuple[float, int, int]:
    """(Delta, k_plus, n) over VALID sessions of one arm."""
    rows = [s for s in sessions
            if s["arm"] == arm and not s["excluded"]
            and s["first_free_pole"] is not None]
    n = len(rows)
    k = sum(1 for s in rows if s["first_free_pole"] == "pos")
    return ((k / n - 0.5) if n else float("nan")), k, n


def by_map(sessions, arm) -> dict:
    out = {}
    for m in (0, 1):
        rows = [s for s in sessions
                if s["arm"] == arm and not s["excluded"]
                and s["cell"]["map"] == m and s["first_free_pole"] is not None]
        n = len(rows)
        k = sum(1 for s in rows if s["first_free_pole"] == "pos")
        out[str(m)] = {"delta": (k / n - 0.5) if n else float("nan"),
                       "k": k, "n": n}
    return out


def collateral(sessions) -> dict:
    """Pre-named, decides nothing."""
    rows = [s for s in sessions if s["arm"] == "marker" and not s["excluded"]]
    all_ch = [c for s in rows for c in s["choices"]]
    share = (sum(1 for c in all_ch if c["picked_pole"] == "pos")
             / len(all_ch)) if all_ch else float("nan")
    per_round = {}
    for r in range(6):
        sub = [s["choices"][r] for s in rows if len(s["choices"]) > r]
        if sub:
            per_round[str(r)] = {
                "delta": sum(1 for c in sub if c["picked_pole"] == "pos")
                         / len(sub) - 0.5, "n": len(sub)}
    stay = sum(1 for s in rows for a, b in zip(s["choices"], s["choices"][1:])
               if a["picked_pole"] == b["picked_pole"])
    pairs = sum(max(len(s["choices"]) - 1, 0) for s in rows)
    return {"session_share_plus": share,
            "session_share_note": "~.50 is not evidence of anything",
            "first_choice_delta_by_round": per_round,
            "p_stay": (stay / pairs) if pairs else float("nan"),
            "n_adjacent_pairs": pairs}


def analyze(art: dict, tier: str | None = None) -> dict:
    if art.get("smoke"):
        raise SystemExit("REFUSED: this is a smoke artifact, not a campaign "
                         "(LOCK-g §4). Smokes are not analysed.")
    tier = tier or art["tier"]
    S = art["sessions"]
    d_m, k_m, n_m = delta(S, "marker")
    maps = by_map(S, "marker")
    controls = {}
    for arm in ("sham", "random"):
        d, k, n = delta(S, arm)
        controls[arm] = {"pseudo_delta": d, "k": k, "n": n}
    envelope = max((abs(v["pseudo_delta"]) for v in controls.values()
                    if v["n"]), default=float("nan"))

    # Direction is pre-registered as APPROACH, so the criteria are stated
    # directionally and the reverse is evaluated as its own, separate
    # question. Testing |Delta| against the envelope and then labelling a
    # negative result afterwards leaves the reverse branch unreachable at
    # confirm tier, where the one-sided approach binomial cannot fire on a
    # reverse result -- the self-test caught exactly that.
    def locks_toward(positive: bool) -> bool:
        return all(v["n"] and v["delta"] != 0
                   and (v["delta"] > 0) == positive for v in maps.values())

    p_approach = p_reverse = None
    if tier == "confirm" and n_m:
        p_approach = binom_sf_inclusive(k_m, n_m, 0.5)
        # P(X <= k) by symmetry of the fair binomial
        p_reverse = binom_sf_inclusive(n_m - k_m, n_m, 0.5)

    conj = {"delta_exceeds_envelope_upward": bool(d_m > envelope),
            "sign_locks_positive": locks_toward(True)}
    rev = {"delta_exceeds_envelope_downward": bool(d_m < -envelope),
           "sign_locks_negative": locks_toward(False)}
    if tier == "confirm":
        conj["exact_binomial_p_le_.05"] = bool(
            p_approach is not None and p_approach <= ALPHA)
        rev["exact_binomial_reverse_p_le_.05"] = bool(
            p_reverse is not None and p_reverse <= ALPHA)

    passed, reverse = all(conj.values()), all(rev.values())
    p_binom = p_approach
    if passed and tier == "screen":
        verdict = "SCREEN-TIER PASS -- triggers an independent confirm campaign"
    elif passed:
        verdict = "CONFIRM PASS -- the Q3 bet is falsified at this stage"
    elif reverse:
        verdict = ("UNEXPECTED-DIRECTION FINDING -- criteria met with the "
                   "sign reversed; pre-registered as approach, so this is "
                   "never a pass")
    else:
        verdict = "NULL"

    return {"item": "B3 analysis", "tier": tier, "stage": art.get("stage"),
            "lock": art.get("lock"), "n_marker_valid": n_m,
            "delta_first": d_m, "k_plus": k_m,
            "by_label_map": maps, "controls": controls,
            "control_envelope": envelope,
            "conjuncts": conj, "all_conjuncts_met": passed,
            "reverse_conjuncts": rev, "reverse_criteria_met": reverse,
            "exact_binomial_p": p_binom, "exact_binomial_reverse_p": p_reverse,
            "critical_k_at_96": 57 if tier == "confirm" else None,
            "verdict": verdict,
            "collateral": collateral(S),
            "counts": art.get("counts"), "paused": art.get("paused"),
            "_disposition": "Code reports what the criteria return. The "
                            "disposition is the design instance's."}


# --- pre-committed synthetic tests, run before any real data --------------
def _synth(n_marker, k_plus, n_ctl=18, k_ctl=None, tier="screen", maps=None):
    S = []
    k_ctl = n_ctl // 2 if k_ctl is None else k_ctl
    for i in range(n_marker):
        m = i % 2 if maps is None else maps(i)
        pole = "pos" if i < k_plus else "neg"
        S.append({"arm": "marker", "excluded": False, "first_free_pole": pole,
                  "cell": {"map": m}, "choices": [{"picked_pole": pole}]})
    for arm in ("sham", "random"):
        for i in range(n_ctl):
            S.append({"arm": arm, "excluded": False,
                      "first_free_pole": "pos" if i < k_ctl else "neg",
                      "cell": {"map": i % 2}, "choices": []})
    return {"tier": tier, "stage": "synthetic", "sessions": S, "counts": {}}


def selftest() -> int:
    cases = [
        ("clear null (48/96 marker, balanced controls)",
         _synth(96, 48), "NULL"),
        ("strong approach at screen (70/96)", _synth(96, 70), "SCREEN-TIER PASS"),
        ("strong approach at confirm (70/96)",
         _synth(96, 70, tier="confirm"), "CONFIRM PASS"),
        ("marginal, killed by its own envelope (58/96 vs 13/18 controls)",
         _synth(96, 58, k_ctl=13), "NULL"),
        ("reverse (26/96) is a finding, never a pass",
         _synth(96, 26, tier="confirm"), "UNEXPECTED-DIRECTION"),
        ("sign does not lock across maps (all +tag on map 0 only)",
         _synth(96, 48, maps=lambda i: 0 if i < 48 else 1), "NULL"),
    ]
    ok = True
    print("=== b3_analyze self-test (pre-committed, before any real data) ===")
    for label, art, want in cases:
        got = analyze(art)["verdict"]
        good = got.startswith(want)
        ok &= good
        print(f"  [{'PASS' if good else 'FAIL'}] {label}")
        print(f"         expected {want!r} -> got {got!r}")
    # a smoke artifact must be refused
    try:
        analyze({"tier": "screen", "smoke": True, "sessions": []})
        print("  [FAIL] smoke artifact was analysed"); ok = False
    except SystemExit:
        print("  [PASS] smoke artifact refused outright")
    print(f"  {'ALL PASS' if ok else 'FAILURES PRESENT'}")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp")
    ap.add_argument("--tier", choices=("screen", "confirm"), default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest or not args.inp:
        return selftest()

    art = json.load(open(args.inp))
    res = analyze(art, args.tier)
    print(f"=== B3 {res['tier']} analysis | stage {res['stage']} ===")
    print(f"  marker valid n = {res['n_marker_valid']}, "
          f"k(+tag) = {res['k_plus']}")
    print(f"  Delta_first = {res['delta_first']:+.4f}")
    for m, v in res["by_label_map"].items():
        print(f"    map{m}: {v['delta']:+.4f} (n={v['n']})")
    for arm, v in res["controls"].items():
        print(f"  {arm:<7} pseudo-Delta {v['pseudo_delta']:+.4f} (n={v['n']})")
    print(f"  control envelope = {res['control_envelope']:.4f}")
    for k, v in res["conjuncts"].items():
        print(f"    {k:<32} {v}")
    if res["exact_binomial_p"] is not None:
        print(f"    exact binomial p = {res['exact_binomial_p']:.4f}")
    print(f"  VERDICT: {res['verdict']}")
    c = res["collateral"]
    print(f"  collateral (decides nothing): session-share "
          f"{c['session_share_plus']:.4f}, p(stay) {c['p_stay']:.4f}")
    if args.out:
        with open(args.out, "w") as fh:
            json.dump(res, fh, indent=1)
        print(f"  wrote {args.out}")
    print("  DISPOSITION IS THE DESIGN INSTANCE'S.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
