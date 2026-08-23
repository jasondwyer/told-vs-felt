#!/usr/bin/env python3
"""e2b VERDICT CAMPAIGN -- the state-present operant, run under LOCK-h v2.0 §2.

Licensed by the v2.0 commit. This is the cell PROPOSAL-h exists to visit:
the state live at the moment of choice, with the choice itself delivering it.

## Three arms, three contingencies

  marker  96 valid  choosing the +tag delivers +axis, the -tag delivers
                    -axis, live from that choice through the following round
                    AND the next read. THIS is the verdict tier's geometry,
                    and it is what makes the arm different from H1: there the
                    schedule selected every state, here the CHOICE does.
  sham    36 valid  no state anywhere. Reads go through `readout.choice_read`
                    -- the untouched, state-free primitive -- because a read
                    with no state needs no exception and must not borrow one.
  random  36 valid  identical to marker with a norm-matched NON-axis
                    direction, so a preference for the axis and a preference
                    for "any strong direction" separate.

## Stopping cannot see an outcome

Each arm runs until its VALID target, capped (160/64/64). Validity is
exclusions only -- audit, lexical -- which are properties of generated round
text, never of a choice. No arm is completed or extended after seeing its
data (PROPOSAL-h §3, restated in v2 §2).

## What this script refuses to do

It does not evaluate the primary criterion. Delta_first, the control
envelope, the sign lock and the exact binomial are computed by
`e2b_verdict_analyze.py` over the committed artifact -- the same separation
H1 used, and for the same reason: a runner that cannot compute the verdict
cannot be accused of stopping when it liked the verdict.

## In-campaign leak monitor (v2 §2, declared)

At each 128-paired-read checkpoint the mapped L CI is computed exactly as in
H1. **PAUSE iff the CI excludes 0 AND |L_hat| > bar_leak/2 = 0.0368**;
report-only otherwise. The pi_hat_d > 0.30 stability ceiling carries over.
Neither monitor can touch the verdict criteria (law rule 7). The
Clopper-Pearson interval is computed in pure python here -- no scipy on this
laptop -- against a discordant count small enough for exact arithmetic.

Site: laptop (MLX). Smoke first; the budget is measured, not projected.

Usage:
    jlens-qwen36/.venv/bin/python scripts/e2b_verdict_campaign.py --smoke \
        --out /tmp/verdict_smoke.json
    jlens-qwen36/.venv/bin/python scripts/e2b_verdict_campaign.py

`--smoke` REQUIRES an explicit `--out` and refuses the canonical path. When
this was written the default `--out` was harmless because
`data/e2b/verdict_campaign.json` did not exist yet; it is the verdict of
record now, and the smoke line above previously demonstrated the invocation
that would overwrite it. Both smokes that ran passed `--out` to a
scratchpad, so the record was never touched -- but a usage line showing a
hazardous invocation is a loaded gun, and the guard below is what unloads it
(design-instance adjudication 2026-08-22).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
import time

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from valence_core.adapters import qwen_or_explain               # noqa: E402
from valence_core.adapters.base import Injection                # noqa: E402
from valence_core.e2b.statepresent import (                     # noqa: E402
    choice_read_statepresent)
from valence_core.readout import choice_read                    # noqa: E402
from valence_core.regression.oracle import load_axis            # noqa: E402
from valence_core.session import (AuditSpec, build_ban_list,    # noqa: E402
                                  classify_response)
from valence_core.session_e2a import (MENU_TEMPLATES,           # noqa: E402
                                      N_FREE, ROUND_TEMPLATES,
                                      SESSION_BANNER, STOP_CAP,
                                      load_tasks, session_rng,
                                      task_sequence)

DATA = os.path.join(REPO, "data")
F = 2
TEMP = 0.7
BAR_LEAK = 0.0735
ROSTER = (("granite", "plaza"), ("prism", "slate"),
          ("velvet", "walnut"), ("ridge", "saddle"))

ARMS = {
    "marker": {"target": 96, "scheduled": 128, "cap": 160, "strata": 16},
    "sham":   {"target": 36, "scheduled": 48,  "cap": 64,  "strata": 8},
    "random": {"target": 36, "scheduled": 48,  "cap": 64,  "strata": 8},
}


# --- exact binomial + Clopper-Pearson, pure python -----------------------
def binom_cdf(k: int, n: int, p: float) -> float:
    if k < 0:
        return 0.0
    if k >= n:
        return 1.0
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i)
               for i in range(0, k + 1))


def cp_interval(k: int, n: int, conf: float = 0.95) -> tuple[float, float]:
    """Exact interval by inverting the binomial tails via bisection.

    scipy's beta.ppf is unavailable here; inverting the CDF is the same
    interval by definition, and n is a discordant count in the tens.
    """
    a = (1.0 - conf) / 2.0
    if n == 0:
        return 0.0, 1.0
    lo, hi = 0.0, 1.0
    if k > 0:                       # P(X >= k | lo) = a
        x, y = 0.0, 1.0
        for _ in range(200):
            m = (x + y) / 2
            (x, y) = (m, y) if 1.0 - binom_cdf(k - 1, n, m) < a else (x, m)
        lo = (x + y) / 2
    if k < n:                       # P(X <= k | hi) = a
        x, y = 0.0, 1.0
        for _ in range(200):
            m = (x + y) / 2
            (x, y) = (x, m) if binom_cdf(k, n, m) < a else (m, y)
        hi = (x + y) / 2
    return lo, hi


def strata_for(arm: str) -> list[dict]:
    """16 cells for marker (pairs x maps x forced-end); 8 for sham/random
    (pairs x maps), with forced order counterbalanced inside the stratum by
    seeded assignment rather than by being a stratum dimension."""
    out = []
    for pair in ROSTER:
        for m in (0, 1):
            base = {"pair": list(pair), "map": m,
                    "tag_plus": pair[m], "tag_minus": pair[1 - m]}
            if ARMS[arm]["strata"] == 16:
                for end in ("pos", "neg"):
                    out.append({**base, "forced_end": end})
            else:
                out.append({**base, "forced_end": None})
    return out


def build_schedule(arm: str, rng) -> list[dict]:
    cells = strata_for(arm)
    n = ARMS[arm]["scheduled"]
    per = n // len(cells)
    sched = []
    for rep in range(per):
        block = [dict(c) for c in cells]
        if ARMS[arm]["strata"] == 8:
            # forced order counterbalanced within stratum across reps
            for c in block:
                c["forced_end"] = "pos" if (rep % 2 == 0) else "neg"
        idx = rng.permutation(len(block))
        sched += [block[i] for i in idx]
    return sched[:n]


def run_session(adapter, arm, idx, cell, tasks, inj, audit, ban_ids, temp,
                axis_key, cached, term_rx):
    rng = session_rng(f"e2b-{arm}", idx)
    seq = task_sequence(rng, tasks, 2 * F + N_FREE)
    tag_plus, tag_minus = cell["tag_plus"], cell["tag_minus"]
    own = (tag_plus, tag_minus)
    label_ids = {t: int(adapter.encode(" " + t,
                                       add_special_tokens=False)[0])
                 for t in own}
    forced_end = cell["forced_end"]
    start_plus = forced_end == "neg"
    order = (["pos", "neg"] if start_plus else ["neg", "pos"]) * F

    transcript = SESSION_BANNER
    rounds, choices = [], []
    excluded, reason = False, None
    n_term = 0
    ti = n_round = 0

    def note_term(text, tag, pos):
        nonlocal n_term
        if any(re.search(r, text) for r in term_rx):
            n_term += 1
            return {"arm": arm, "config": tag, "round_pos": pos}
        return None

    terms = []
    for ri, pole in enumerate(order):
        n_round += 1
        tid, ttext = seq[ti]; ti += 1
        tag = tag_plus if pole == "pos" else tag_minus
        seg = ROUND_TEMPLATES[(idx + ri) % 4].format(
            n=n_round, tag=tag, task=ttext)
        seed = int(rng.integers(2 ** 31))
        injs = [] if inj is None else [inj[pole]]
        g = adapter.generate(transcript, seg, injections=injs, seed=seed,
                             temp=temp, max_tokens=STOP_CAP,
                             ban_ids=ban_ids, cached=cached)
        degen, lex = classify_response(g.text, audit, own)
        t = note_term(g.text, tag, f"forced{ri}")
        if t:
            terms.append(t)
        rounds.append({"phase": "forced", "round": ri, "pole": pole,
                       "tag": tag, "task": tid, "seed": seed,
                       "n_tok": len(g.token_ids), "cap_hit": g.cap_hit,
                       "degen": degen, "lexical": lex,
                       "termination": bool(t)})
        transcript += seg + g.text + "\n"
        if lex:
            excluded, reason = True, f"lexical:{lex}@forced{ri}"
        elif degen:
            excluded, reason = True, f"audit:{degen}@forced{ri}"
        if excluded:
            break

    live = forced_end
    for ci in range(N_FREE):
        if excluded:
            break
        n_round += 1
        a, b = ((tag_plus, tag_minus) if rng.integers(2) == 0
                else (tag_minus, tag_plus))
        menu = MENU_TEMPLATES[(idx + ci) % 4].format(n=n_round, a=a, b=b)
        if inj is None:
            # sham: no state anywhere, so the untouched state-free primitive.
            cr = choice_read(adapter, transcript + menu, a, b, label_ids)
            pick = cr.pick
            pr_dict = {"state_present": None, "shadow": cr.as_dict(),
                       "leak": None}
            flipped = None
        else:
            pr = choice_read_statepresent(
                adapter, transcript + menu, a, b, label_ids, inj[live],
                axis=axis_key, session_id=f"{arm}:{idx}", round_index=ci)
            pick = pr.state_present.pick
            pr_dict = pr.as_dict()
            flipped = pr_dict["leak"]["flipped"]
        picked_pole = "pos" if pick == tag_plus else "neg"
        tid, ttext = seq[ti]; ti += 1
        chosen = ROUND_TEMPLATES[(idx + ci) % 4].format(
            n=n_round, tag=pick, task=ttext)
        seed = int(rng.integers(2 ** 31))
        prefix = transcript + menu + f" {pick}\n"
        injs = [] if inj is None else [inj[picked_pole]]
        g = adapter.generate(prefix, chosen, injections=injs, seed=seed,
                             temp=temp, max_tokens=STOP_CAP,
                             ban_ids=ban_ids, cached=cached)
        degen, lex = classify_response(g.text, audit, own)
        t = note_term(g.text, pick, f"free{ci}")
        if t:
            terms.append(t)
        choices.append({"round": ci, "menu_a": a, "menu_b": b,
                        "live_state_at_read": live, "pick": pick,
                        "picked_pole": picked_pole, "flipped": flipped,
                        "task": tid, "seed": seed,
                        "n_tok": len(g.token_ids), "cap_hit": g.cap_hit,
                        "degen": degen, "lexical": lex,
                        "termination": bool(t), "paired_read": pr_dict})
        transcript += menu + f" {pick}\n" + chosen + g.text + "\n"
        live = picked_pole          # THE CHOICE delivers the next state

    return {"arm": arm, "session": idx, "stratum": cell,
            "excluded": excluded, "exclude_reason": reason,
            "valid": bool(not excluded and choices),
            "first_free_pick_pos": (choices[0]["picked_pole"] == "pos"
                                    if choices else None),
            "n_termination": n_term, "terminations": terms,
            "rounds": rounds, "choices": choices, "transcript": transcript}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true",
                    help="tiny per-arm targets to measure the budget")
    ap.add_argument("--layer", type=int, default=48)
    ap.add_argument("--frac", type=float, default=0.10)
    ap.add_argument("--axis-key", default="span_reward")
    ap.add_argument("--temp", type=float, default=TEMP)
    ap.add_argument("--order-seed", type=int, default=2026)
    ap.add_argument("--checkpoint-every", type=int, default=128)
    ap.add_argument("--out", default=os.path.join(DATA, "e2b/verdict_campaign.json"))
    args = ap.parse_args()

    # Adjudicated 2026-08-22. Fires ONLY under --smoke, so the campaign path
    # is behaviourally identical to the run that produced the verdict.
    canonical = os.path.abspath(os.path.join(DATA, "e2b/verdict_campaign.json"))
    if args.smoke and os.path.abspath(args.out) == canonical:
        raise SystemExit(
            "\nSMOKE REFUSED: --out defaults to the verdict artifact of "
            "record\n"
            f"  {os.path.relpath(canonical, REPO)}\n\n"
            "  A smoke is not the campaign, and a 6-session smoke written "
            "there\n"
            "  would overwrite the 2026-08-22 NULL with something that looks "
            "like\n"
            "  it. Pass an explicit scratch path:\n\n"
            "      --smoke --out /tmp/verdict_smoke.json\n")

    arms = {k: dict(v) for k, v in ARMS.items()}
    if args.smoke:
        for k in arms:
            arms[k].update(target=2, scheduled=2, cap=2)

    acfg = json.load(open(os.path.join(DATA, "configs/e2b_audit_v2.json")))
    blob = json.dumps({k: v for k, v in acfg.items() if k != "sha16"},
                      sort_keys=True, separators=(",", ":")).encode()
    if hashlib.sha256(blob).hexdigest()[:16] != acfg["sha16"]:
        raise SystemExit("VERDICT STOP: audit artifact sha mismatch")
    tcfg = json.load(open(os.path.join(DATA, "configs/f_termination_patterns.json")))
    term_rx = tcfg["term_regex"]

    print("=== e2b VERDICT CAMPAIGN (LOCK-h v2.0 §2) ===")
    if args.smoke:
        print("  *** SMOKE -- 2 sessions per arm, NOT the campaign ***")
    print(f"  arms: " + ", ".join(
        f"{k} {v['target']} valid / {v['scheduled']} scheduled / cap "
        f"{v['cap']}" for k, v in arms.items()))
    print(f"  AUDIT v2 sha {acfg['sha16']} (verified); termination counter "
          f"{len(term_rx)} patterns")
    print(f"  contingency: THE CHOICE delivers the state, live through the "
          f"following round and the next read (marker/random); sham has no "
          f"state anywhere and reads via the untouched choice_read")
    print(f"  leak monitor: PAUSE iff CI excludes 0 AND |L_hat| > "
          f"{BAR_LEAK / 2:.4f}; stability ceiling pi_hat_d > 0.30",
          flush=True)

    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    u, R = load_axis(args.layer)
    rand = np.load(os.path.join(DATA, "e0/e0_random_dirs.npz"))[
        f"L{args.layer}"].astype(np.float64)
    t0 = time.time()
    adapter = qwen_or_explain(__file__)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)

    ban_ids, ban_strings = build_ban_list(
        adapter, path=os.path.join(DATA, "configs/e2a_ban_list.json"))
    audit = AuditSpec(ban_strings=tuple(ban_strings),
                      frame_fragments=tuple(acfg["frame_fragments"]),
                      junk_regex=tuple(acfg["junk_regex"]))
    g1 = json.load(open(os.path.join(DATA, "e2a/g1_kernel_gate.json")))
    row = g1["results"].get(str(args.frac))
    cached = bool(row and row["pass"])
    inj_axis = {"pos": Injection.at_frac(u, args.layer, args.frac, R),
                "neg": Injection.at_frac(u, args.layer, -args.frac, R)}
    inj_rand = {"pos": Injection.at_frac(rand, args.layer, args.frac, R),
                "neg": Injection.at_frac(rand, args.layer, -args.frac, R)}
    inj_for = {"marker": inj_axis, "random": inj_rand, "sham": None}
    # Per-read injection provenance must name the direction that was
    # ACTUALLY injected (rule 5(e)). Passing the axis key for every arm
    # would stamp the random arm's reads `span_reward`, which is false
    # provenance on the one arm whose entire purpose is not being the axis.
    axis_label = {"marker": args.axis_key,
                  "random": f"random_dir_L{args.layer}",
                  "sham": None}
    print(f"  dose |alpha| = {abs(inj_axis['pos'].alpha):.4f}; rounds "
          f"{'CACHED' if cached else 'UNCACHED'}; temp {args.temp}",
          flush=True)

    rng = np.random.default_rng(args.order_seed)
    sched = {a: build_schedule(a, rng) for a in arms}
    order = [a for a in arms for _ in range(arms[a]["scheduled"])]
    order = [order[i] for i in rng.permutation(len(order))]

    sessions, checkpoints = [], []
    valid = {a: 0 for a in arms}
    ran = {a: 0 for a in arms}
    n_pr = n_d = 0
    b_ct = c_ct = 0
    next_cp = args.checkpoint_every
    paused = None
    t1 = time.time()

    for arm in order:
        if valid[arm] >= arms[arm]["target"] or ran[arm] >= arms[arm]["cap"]:
            continue
        if ran[arm] >= len(sched[arm]):
            sched[arm] += build_schedule(arm, rng)
        cell = sched[arm][ran[arm]]
        s = run_session(adapter, arm, ran[arm], cell, tasks,
                        inj_for[arm], audit, ban_ids, args.temp,
                        axis_label[arm], cached, term_rx)
        ran[arm] += 1
        sessions.append(s)
        if s["valid"]:
            valid[arm] += 1
        for ch in s["choices"]:
            if ch["flipped"] is None:
                continue
            n_pr += 1
            if ch["flipped"]:
                n_d += 1
                if ch["pick"] == cell["tag_plus"]:
                    b_ct += 1
                else:
                    c_ct += 1
        el = time.time() - t1
        print(f"    [{arm:<6}] {ran[arm]:>3}/{arms[arm]['cap']} "
              f"valid {valid[arm]:>3}/{arms[arm]['target']}"
              + (f" EXCLUDED({s['exclude_reason']})" if s["excluded"] else "")
              + f"  paired_reads {n_pr}  {el:.0f}s", flush=True)

        while n_pr >= next_cp:
            pi = n_d / n_pr
            L = (b_ct - c_ct) / n_pr
            lo, hi = cp_interval(b_ct, n_d) if n_d else (0.0, 1.0)
            Llo, Lhi = (2 * lo - 1) * pi, (2 * hi - 1) * pi
            excl0 = not (Llo <= 0.0 <= Lhi)
            pause = excl0 and abs(L) > BAR_LEAK / 2
            cp = {"at_reads": next_cp, "n_paired": n_pr, "n_d": n_d,
                  "b": b_ct, "c": c_ct, "pi_hat_d": pi, "L_hat": L,
                  "L_ci": [Llo, Lhi], "ci_excludes_zero": excl0,
                  "pause": bool(pause),
                  "stability_pause": bool(pi > 0.30)}
            checkpoints.append(cp)
            print(f"      --- CHECKPOINT {next_cp} reads: pi_hat_d "
                  f"{pi:.4f}, L_hat {L:+.5f}, CI [{Llo:+.5f}, {Lhi:+.5f}] "
                  f"-> {'PAUSE' if pause else 'report-only'}"
                  + (" | STABILITY PAUSE" if cp["stability_pause"] else ""),
                  flush=True)
            if pause or cp["stability_pause"]:
                paused = cp
            next_cp += args.checkpoint_every
        if paused:
            print("      LEAK/STABILITY MONITOR FIRED -- halting for a "
                  "design-instance disposition (law rule 7: monitors never "
                  "touch the verdict criteria)", flush=True)
            break
        if all(valid[a] >= arms[a]["target"] or ran[a] >= arms[a]["cap"]
               for a in arms):
            break

    prov = adapter.provenance()
    n_rounds = sum(len(s["rounds"]) + len(s["choices"]) for s in sessions)
    out = {"item": "e2b verdict campaign", "lock": "LOCK-h v2.0 §2",
           "smoke": bool(args.smoke), "audit_sha16": acfg["sha16"],
           "round_path_cached": cached, "layer": args.layer,
           "frac": args.frac, "alpha": abs(inj_axis["pos"].alpha),
           "axis_key": args.axis_key,
           "axis_label_by_arm": {"marker": args.axis_key,
                                 "random": f"random_dir_L{args.layer}",
                                 "sham": None},
           "temp": args.temp,
           "order_seed": args.order_seed,
           "arms": arms, "valid": valid, "ran": ran,
           "n_paired_reads": n_pr, "n_d": n_d, "b": b_ct, "c": c_ct,
           "checkpoints": checkpoints, "paused": paused,
           "n_rounds": n_rounds,
           "n_terminations": sum(s["n_termination"] for s in sessions),
           "window": {"declared": prov["choice_window_declared"],
                      "n_encodes_clipped": prov["n_encodes_clipped"]},
           "provenance": prov, "sessions": sessions,
           "runtime_s": round(time.time() - t0, 1),
           "primary_evaluated": False,
           "decides_nothing": ("Collection only. Delta_first, the control "
                               "envelope, the sign lock and the exact "
                               "binomial are computed by "
                               "e2b_verdict_analyze.py over this artifact.")}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\n  valid {valid} | ran {ran} | paired reads {n_pr} "
          f"(n_d {n_d}, b {b_ct}, c {c_ct})")
    print(f"  terminations {out['n_terminations']}; window clipped "
          f"{prov['n_encodes_clipped']}")
    print(f"  PRIMARY NOT EVALUATED HERE -- run e2b_verdict_analyze.py")
    print(f"\nwrote {args.out}  ({out['runtime_s']:.0f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
