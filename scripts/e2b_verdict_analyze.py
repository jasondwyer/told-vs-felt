#!/usr/bin/env python3
"""Evaluate the e2b verdict criterion over a committed campaign artifact
(LOCK-h v2.0 §2), plus the registered secondary and the named descriptives.

Written and committed BEFORE the campaign ran, deliberately. An analysis
script authored after seeing the data is a different instrument from one
authored before it, however identical the code, and only one of them can be
shown to have been.

## The primary, exactly as §2 states it

Counterbalanced Delta_first for the MARKER family passes iff, conjunctively:

  (i)   it exceeds the campaign's own REALISED control envelope --
        max |pseudo-Delta| across the sham and random families, each
        computed identically to the marker's own statistic;
  (ii)  the sign locks across label maps (Delta >= 0 in BOTH);
  (iii) one-sided exact binomial p <= .05 at the marker's valid n
        (critical k >= 57 at n = 96).

Direction is pre-registered as APPROACH. A significant result in the
reverse direction is an unexpected-direction finding and is reported as
such -- never as a pass (e2a's locked criterion, carried forward).

A screen-tier pass triggers the confirm campaign: an independent
fresh-session campaign, marker n = 96, identical criteria. This script
cannot and does not confirm anything on its own.

## What it refuses to do

No arm is completed or extended after seeing data, so this script takes the
artifact as it stands and never asks for more. It reports the conjunction
term by term: a criterion that can only be reported as a single word is a
criterion whose failure mode is invisible.

Needs numpy + scipy (HANDOFF trap 9: use a scratch venv, never the miniconda
base).

Usage:
    python scripts/e2b_verdict_analyze.py
    python scripts/e2b_verdict_analyze.py --campaign data/e2b/verdict_campaign.json
"""
from __future__ import annotations

import argparse
import collections
import json
import os

import numpy as np
from scipy import stats

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "data")


def arm_sessions(d, arm):
    return [s for s in d["sessions"] if s["arm"] == arm and s["valid"]]


def delta_first(sessions):
    """Share choosing the +pole at the FIRST free choice, minus 0.5.

    For sham the +pole is nominal -- the map still designates a tag, and the
    pseudo-Delta is computed identically, which is the only way the envelope
    is a comparison rather than an analogy.
    """
    picks = [s["first_free_pick_pos"] for s in sessions
             if s["first_free_pick_pos"] is not None]
    k, n = sum(picks), len(picks)
    return {"k": k, "n": n, "share": (k / n if n else None),
            "delta": (k / n - 0.5 if n else None)}


def by_map(sessions):
    out = {}
    for m in (0, 1):
        out[m] = delta_first([s for s in sessions if s["stratum"]["map"] == m])
    return out


def stay_switch(sessions):
    """p(stay | on +) vs p(stay | on -), by the state live at the read.

    'Stay' is the pick repeating the previous pick. The live state at read
    ci IS what the previous pick delivered, so this is the approach/escape
    asymmetry the secondary asks for.
    """
    tab = {"pos": [0, 0], "neg": [0, 0]}          # [stays, total]
    for s in sessions:
        ch = s["choices"]
        for i in range(1, len(ch)):
            live = ch[i]["live_state_at_read"]
            if live not in tab:
                continue
            tab[live][1] += 1
            tab[live][0] += int(ch[i]["pick"] == ch[i - 1]["pick"])
    out = {}
    for k, (st, tot) in tab.items():
        out[k] = {"stays": st, "n": tot, "p_stay": (st / tot if tot else None)}
    return out


def shadow_delta_first(sessions):
    """Delta_first computed from the SHADOW reads -- e2a's insulated design
    running inside e2b for free (PROPOSAL-h §0.2 (ii))."""
    k = n = 0
    for s in sessions:
        if not s["choices"]:
            continue
        pr = s["choices"][0]["paired_read"]
        sh = pr.get("shadow")
        if not sh:
            continue
        n += 1
        k += int(sh["pick"] == s["stratum"]["tag_plus"])
    return {"k": k, "n": n, "share": (k / n if n else None),
            "delta": (k / n - 0.5 if n else None)}


def leak_by_sign(sessions):
    pos, neg, mass, flips, tot = [], [], [], 0, 0
    for s in sessions:
        for c in s["choices"]:
            lk = c["paired_read"].get("leak")
            if not lk:
                continue
            tot += 1
            flips += int(lk["flipped"])
            (pos if lk["sign"] == 1 else neg).append(lk["d_p_a"])
            mass.append(abs(lk["d_label_mass"]))
    f = lambda x: float(np.mean(x)) if x else None
    out = {"n": tot, "flip_rate": (flips / tot if tot else None),
           "mean_d_p_a_on_pos": f(pos), "mean_d_p_a_on_neg": f(neg),
           "mean_abs_d_label_mass": f(mass)}
    if pos and neg:
        out["state_reversing_half_gap"] = (f(pos) - f(neg)) / 2
        out["common_mode"] = (f(pos) + f(neg)) / 2
    return out


def session_share(sessions):
    sh = [np.mean([c["picked_pole"] == "pos" for c in s["choices"]])
          for s in sessions if s["choices"]]
    return {"n": len(sh), "mean": float(np.mean(sh)) if sh else None}


def icc_binary(groups):
    groups = [g for g in groups if g]
    if len(groups) < 2:
        return None
    N = sum(len(g) for g in groups)
    grand = sum(sum(g) for g in groups) / N
    msb = sum(len(g) * (np.mean(g) - grand) ** 2
              for g in groups) / (len(groups) - 1)
    dfw = N - len(groups)
    if dfw <= 0:
        return None
    msw = sum(((np.array(g) - np.mean(g)) ** 2).sum() for g in groups) / dfw
    k0 = (N - sum(len(g) ** 2 for g in groups) / N) / (len(groups) - 1)
    den = msb + (k0 - 1) * msw
    return float(max(0.0, 0.0 if den <= 0 else (msb - msw) / den))


def perm_3b(sessions, draws=200_000, seed=26):
    """§3b, re-run on this campaign's realised flips. Same standing:
    registered secondary, never gate-relevant."""
    groups = [[int(c["flipped"]) for c in s["choices"]
               if c["flipped"] is not None] for s in sessions]
    groups = [g for g in groups if g]
    if not groups:
        return {"n_flips": 0, "note": "no paired reads"}
    sizes = np.array([len(g) for g in groups])
    edges = np.concatenate([[0], np.cumsum(sizes)])
    flat = int(sizes.sum())
    nf = sum(sum(g) for g in groups)
    icc_obs = icc_binary(groups) or 0.0
    ge2_obs = sum(1 for g in groups if sum(g) >= 2)
    rng = np.random.default_rng(seed)
    ni, ng = np.empty(draws), np.empty(draws)
    for t in range(draws):
        v = np.zeros(flat, dtype=int)
        v[rng.choice(flat, size=nf, replace=False)] = 1
        gs = [list(v[edges[i]:edges[i + 1]]) for i in range(len(groups))]
        ni[t] = icc_binary(gs) or 0.0
        ng[t] = sum(1 for g in gs if sum(g) >= 2)
    two = lambda null, o: float(min(1.0, 2 * min(
        (null >= o - 1e-12).mean(), (null <= o + 1e-12).mean())))
    return {"n_sessions": len(groups), "n_reads": flat, "n_flips": nf,
            "icc_obs": icc_obs, "icc_p": two(ni, icc_obs),
            "sessions_ge2_obs": ge2_obs, "sessions_ge2_p": two(ng, ge2_obs),
            "draws": draws, "gate_relevant": False}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--campaign", default=os.path.join(DATA, "e2b/verdict_campaign.json"))
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--draws", type=int, default=200_000)
    ap.add_argument("--out", default=os.path.join(DATA, "e2b/verdict_analysis.json"))
    args = ap.parse_args()

    d = json.load(open(args.campaign))
    if d.get("smoke"):
        print("REFUSING: this artifact is a smoke, not the campaign.")
        return 2
    marker = arm_sessions(d, "marker")
    sham = arm_sessions(d, "sham")
    random_ = arm_sessions(d, "random")

    print("=== e2b VERDICT ANALYSIS (LOCK-h v2.0 §2) ===")
    print(f"  artifact: {os.path.relpath(args.campaign, REPO)}")
    print(f"  audit sha {d.get('audit_sha16')} | rounds cached "
          f"{d.get('round_path_cached')} | paused: {bool(d.get('paused'))}")
    print(f"  valid: marker {len(marker)}, sham {len(sham)}, "
          f"random {len(random_)}  (targets 96/36/36)")

    dm = delta_first(marker)
    maps = by_map(marker)
    ds, dr = delta_first(sham), delta_first(random_)
    env = max(abs(x["delta"]) for x in (ds, dr) if x["delta"] is not None)
    k, n = dm["k"], dm["n"]
    p_one = float(stats.binom.sf(k - 1, n, 0.5)) if n else 1.0
    k_crit = next((i for i in range(n + 1)
                   if stats.binom.sf(i - 1, n, 0.5) <= args.alpha), n + 1)

    c1 = dm["delta"] is not None and dm["delta"] > env
    c2 = all(m["delta"] is not None and m["delta"] >= 0 for m in maps.values())
    c3 = p_one <= args.alpha
    reverse = dm["delta"] is not None and dm["delta"] < 0 and \
        float(stats.binom.cdf(k, n, 0.5)) <= args.alpha

    print(f"\n  PRIMARY -- counterbalanced Delta_first, marker family")
    print(f"    Delta = {dm['delta']:+.4f}  ({k}/{n})")
    print(f"    (i)   > realised control envelope {env:.4f} "
          f"(sham {ds['delta']:+.4f} n={ds['n']}, random {dr['delta']:+.4f} "
          f"n={dr['n']}) -> {'PASS' if c1 else 'fail'}")
    print(f"    (ii)  sign locks across maps: map0 {maps[0]['delta']:+.4f} "
          f"(n={maps[0]['n']}), map1 {maps[1]['delta']:+.4f} "
          f"(n={maps[1]['n']}) -> {'PASS' if c2 else 'fail'}")
    print(f"    (iii) one-sided exact binomial p = {p_one:.4f} "
          f"(critical k >= {k_crit} at n = {n}) -> "
          f"{'PASS' if c3 else 'fail'}")
    verdict = ("SCREEN-TIER PASS" if (c1 and c2 and c3)
               else ("UNEXPECTED-DIRECTION FINDING" if reverse else "NULL"))
    print(f"\n  VERDICT: {verdict}")
    if verdict == "SCREEN-TIER PASS":
        print("    Triggers the CONFIRM campaign (independent fresh sessions,"
              " marker n = 96, identical criteria). Nothing is confirmed by "
              "this campaign alone, and the §5 welfare pre-commitment "
              "triggers only on screen + confirm.")
    elif verdict == "UNEXPECTED-DIRECTION FINDING":
        print("    Direction was pre-registered as APPROACH; a significant "
              "reverse result is reported as a finding, never as a pass.")

    sec = stay_switch(marker)
    print(f"\n  SECONDARY (verdict-relevant only if the primary fires -- it "
          f"{'did' if verdict == 'SCREEN-TIER PASS' else 'did not'}):")
    for kk in ("pos", "neg"):
        v = sec[kk]
        ps = f"{v['p_stay']:.4f}" if v["p_stay"] is not None else "n/a"
        print(f"    p(stay | on {kk}) = {ps}  ({v['stays']}/{v['n']})")

    shd = shadow_delta_first(marker)
    leak = leak_by_sign(marker)
    lrand = leak_by_sign(random_)
    share = session_share(marker)
    terms = collections.Counter()
    for s in d["sessions"]:
        for t in s.get("terminations", []):
            terms[(t["arm"], t["config"], t["round_pos"])] += 1

    print(f"\n  DESCRIPTIVES (named in advance)")
    print(f"    shadow-read Delta_first = "
          + (f"{shd['delta']:+.4f} ({shd['k']}/{shd['n']}) -- e2a's insulated"
             f" design running inside e2b" if shd["delta"] is not None
             else "n/a"))
    print(f"    marker per-read leak: flip rate "
          f"{leak['flip_rate']:.4f}, state-reversing half-gap "
          + (f"{leak.get('state_reversing_half_gap', float('nan')):+.5f}"
             if leak.get("state_reversing_half_gap") is not None else "n/a"))
    print(f"    random per-read leak: flip rate "
          f"{lrand['flip_rate']:.4f}" if lrand["flip_rate"] is not None
          else "    random per-read leak: n/a")
    print(f"    session-share (marker) = "
          + (f"{share['mean']:.4f}" if share["mean"] is not None else "n/a"))
    print(f"    termination attempts: {sum(terms.values())} over ALL "
          f"sessions incl. excluded; {len(terms)} distinct "
          f"(arm, config, round-pos) cells")

    p3b = perm_3b(marker, args.draws)
    print(f"\n  §3b registered secondary (never gate-relevant): "
          f"ICC {p3b.get('icc_obs')}, p {p3b.get('icc_p')}; sessions with "
          f">=2 flips {p3b.get('sessions_ge2_obs')}, p "
          f"{p3b.get('sessions_ge2_p')}")

    out = {"item": "e2b verdict analysis", "lock": "LOCK-h v2.0 §2",
           "campaign": os.path.relpath(args.campaign, REPO),
           "valid": {"marker": len(marker), "sham": len(sham),
                     "random": len(random_)},
           "primary": {"delta_first": dm, "by_map": {str(k): v for k, v
                                                     in maps.items()},
                       "sham": ds, "random": dr,
                       "control_envelope": env,
                       "p_one_sided": p_one, "critical_k": k_crit,
                       "conjunct_envelope": bool(c1),
                       "conjunct_sign_lock": bool(c2),
                       "conjunct_binomial": bool(c3),
                       "verdict": verdict},
           "secondary_stay_switch": sec,
           "descriptives": {"shadow_delta_first": shd,
                            "marker_leak": leak, "random_leak": lrand,
                            "session_share": share,
                            "terminations": {f"{a}|{c}|{r}": v
                                             for (a, c, r), v in terms.items()},
                            "n_terminations": sum(terms.values())},
           "secondary_3b": p3b,
           "decides_nothing": ("Code evaluates the registered criterion over "
                               "a committed artifact. Disposition, and any "
                               "confirm campaign, are the design instance's.")}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
