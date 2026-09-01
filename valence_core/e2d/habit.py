"""The alternation habit — AMENDMENT 2 (v)'s registered frame and secondary.

WHAT THE HABIT IS. D1's rule-25 read found that 6 of 7 valid sessions
alternated strictly across all six free choices, and 7 of 7 opened with the
complement of the last forced round's pole. It is not an e2d artifact: e2a's
published corpus is **157/187 strictly alternating** and **156/187** opening
with the complement. The model is continuing a rhythm the forced block starts.

WHY IT REFRAMES THE PRIMARY. Under forced-end counterbalancing the primary
decomposes exactly. Write the habit's prediction for the first free pick as
"the complement of the last forced pole", and let

    b+  = break rate in sessions where the habit leads AWAY from the +label
          (forced_end = pos, so following the habit picks the sham label and
          BREAKING it picks +)
    bs  = break rate in sessions where the habit leads TOWARD the +label
          (forced_end = neg, so following picks + and breaking picks sham)

Then, when forced-end is EXACTLY balanced, P(first pick = +) =
1/2 * (b+ + (1 - bs)), so

    **Delta_first = 1/2 * (b+ - bs)**

and at any other balance the exact statement is the weighted one,
P(+) = n+/N * b+ + ns/N * (1 - bs). The distinction earns its keep: on e2a's
actual 53/49 split the balanced form gives +0.0528 where the measured primary
is +0.0392, an error of +0.0135 -- about a third of the published effect. e2d's
M arm is exactly 16/16 by cell construction BEFORE exclusions and will not be
after them, so both forms are computed and the balance is reported beside.

Either way the primary IS a break-rate difference, halved. §3's powered
Delta = +0.15 therefore asks for **b+ - bs = 0.30** against a base break rate
of about 0.17. That is the quantity e2d is powered on, and the scope sentence
says so: e2d tests whether a 2x MED state overrides the alternation habit at
that scale. Preprint §10 alternative (i), quantified.

RULE 11. The decomposition is algebra, not a finding, and the e2a rates that
motivate it are post-hoc on committed data. It licenses a frame and a
registered secondary; it is never a verdict, and nothing here can move a
criterion. The neutral-start remedy is a format change and is explicitly NOT
folded in (drawer).
"""

from __future__ import annotations

from typing import Mapping, Sequence


def last_forced_pole(session: Mapping) -> str | None:
    rounds = [r for r in session["rounds"]
              if str(r.get("phase", "")).startswith("forced")]
    return rounds[-1]["pole"] if rounds else None


def first_pick_pole(session: Mapping) -> str | None:
    ch = session.get("choices") or []
    return ch[0]["picked_pole"] if ch else None


def follows_habit(session: Mapping) -> bool | None:
    """Did the first free pick continue the alternation? True = followed the
    habit (picked the complement of the last forced pole), False = broke it."""
    lf, fp = last_forced_pole(session), first_pick_pole(session)
    if lf is None or fp is None:
        return None
    return fp != lf


def strictly_alternates(session: Mapping) -> bool | None:
    picks = [c["pick"] for c in (session.get("choices") or [])]
    if len(picks) < 2:
        return None
    return all(picks[i] != picks[i + 1] for i in range(len(picks) - 1))


def break_rates(sessions: Sequence[Mapping]) -> dict:
    """b+ and bs, and the Delta_first they imply.

    Sessions with no free choice contribute to neither rate and are counted
    as undecidable rather than dropped silently (rule 28a's habit).
    """
    b_plus = {"break": 0, "n": 0}       # forced_end = pos: breaking picks +
    b_sham = {"break": 0, "n": 0}       # forced_end = neg: breaking picks sham
    undecidable = 0
    for s in sessions:
        lf, fp = last_forced_pole(s), first_pick_pole(s)
        if lf is None or fp is None:
            undecidable += 1
            continue
        broke = (fp == lf)
        bucket = b_plus if lf == "pos" else b_sham
        bucket["n"] += 1
        bucket["break"] += int(broke)

    def rate(d):
        return d["break"] / d["n"] if d["n"] else None

    bp, bs = rate(b_plus), rate(b_sham)
    n_p, n_s = b_plus["n"], b_sham["n"]
    N = n_p + n_s
    balanced = weighted = None
    if bp is not None and bs is not None and N:
        balanced = 0.5 * (bp - bs)
        weighted = (n_p / N) * bp + (n_s / N) * (1 - bs) - 0.5
    return {"b_plus": {"breaks": b_plus["break"], "n": n_p, "rate": bp,
                       "meaning": "forced_end = pos; breaking the habit picks "
                                  "the +label"},
            "b_sham": {"breaks": b_sham["break"], "n": n_s, "rate": bs,
                       "meaning": "forced_end = neg; breaking the habit picks "
                                  "the sham label"},
            # AMENDMENT 2 (v) states the identity for EXACT counterbalancing,
            # and there it is exact. Both forms are reported because the
            # difference is not academic: on e2a's actual 53/49 split the
            # balanced form gives +0.0528 against a measured +0.0392 -- an
            # error of +0.0135, about a THIRD of the published effect. After
            # exclusions e2d's M arm will also be imbalanced, so the figure
            # that reproduces the primary is the weighted one.
            "delta_first_balanced_form": balanced,
            "delta_first_weighted_form": weighted,
            "forced_end_balance": {"pos": n_p, "neg": n_s,
                                   "exactly_balanced": n_p == n_s,
                                   "imbalance": abs(n_p - n_s)},
            "n_undecidable": undecidable,
            "identity": ("Delta_first = 1/2 * (b_plus - b_sham) under EXACT "
                         "forced-end counterbalancing (AMENDMENT 2 (v)); the "
                         "weighted form n+/N*b+ + ns/N*(1-bs) - 1/2 "
                         "reproduces the measured primary at any balance")}


def secondaries(sessions: Sequence[Mapping]) -> dict:
    """AMENDMENT 2 (v)'s registered secondary, by arm. NOT verdict-relevant.

    Two figures: the habit-break rate on the first pick, and the
    strict-alternation rate over all six choices. Reported per arm so a state
    effect on the habit itself -- the thing the registered DV cannot see --
    would at least be visible.
    """
    by_arm: dict[str, dict] = {}
    for s in sessions:
        a = by_arm.setdefault(s["arm"], {"n": 0, "broke": 0, "decidable": 0,
                                         "alt_n": 0, "alt_yes": 0})
        a["n"] += 1
        fh = follows_habit(s)
        if fh is not None:
            a["decidable"] += 1
            a["broke"] += int(not fh)
        sa = strictly_alternates(s)
        if sa is not None:
            a["alt_n"] += 1
            a["alt_yes"] += int(sa)
    out = {}
    for arm, a in sorted(by_arm.items()):
        out[arm] = {
            "sessions": a["n"],
            "habit_break_rate_first_pick": (a["broke"] / a["decidable"]
                                            if a["decidable"] else None),
            "n_decidable": a["decidable"], "n_breaks": a["broke"],
            "strict_alternation_rate": (a["alt_yes"] / a["alt_n"]
                                        if a["alt_n"] else None),
            "n_alt_decidable": a["alt_n"]}
    return {"verdict_relevant": False,
            "registered": "AMENDMENT 2 (v), secondary",
            "by_arm": out}


def frame(sessions: Sequence[Mapping], arm: str = "M") -> dict:
    """The full registered frame for one arm."""
    arm_sessions = [s for s in sessions if s["arm"] == arm]
    br = break_rates(arm_sessions)
    return {"arm": arm, "n_sessions": len(arm_sessions),
            "break_rates": br,
            "powered_effect_in_break_terms": {
                "delta_first": 0.15,
                "required_b_plus_minus_b_sham": 0.30,
                "e2a_base_break_rate": 1 - 156 / 187,
                "note": ("§3's powered Delta = +0.15 is a break-rate "
                         "difference of 0.30 against a base of ~0.17. e2d "
                         "tests whether a 2x MED state overrides the "
                         "alternation habit at that scale.")},
            "rule_11": ("post-hoc frame on committed data; licenses a frame "
                        "and a secondary, never a verdict")}


__all__ = ["last_forced_pole", "first_pick_pole", "follows_habit",
           "strictly_alternates", "break_rates", "secondaries", "frame"]
