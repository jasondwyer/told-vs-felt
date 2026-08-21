#!/usr/bin/env python3
"""H1 -- the leakage budget, run as locked (LOCK-h v1.3 §3 + §3a).

The campaign the whole e2b exception is gated on. 112 sessions scheduled
(7 blocks x 16 strata), execution stopping at §3's read-level exits:
n_d = 200 discordant pairs or N = 640 paired reads, whichever comes first.
Per the v1.3 recorded corollary the n_d* exit needs pi_d >= 0.3125, which the
0.30 stability ceiling forbids, so N_max binds across the licensed range and
the stop at **session 107, read 4** is the only reachable one short of a
pause. Scheduled sessions past the stop are not run.

## How H1 differs from H2, which is the whole point of it

PROPOSAL-h §2: sessions "identical to verdict sessions in every respect
except that NO contingency differs between arms (both tags deliver identical
nothing); the state is nonetheless live at choice reads per the delivery
schedule (§3), alternating +/- by the counterbalanced forced-phase order."

Read out into three concrete differences from `e2b_h2_sessions.py`:

  1. **Forced phase: unchanged.** Still steered by pole, still ending on the
     stratum's forced-phase end state. The forced exposure is not a
     contingency on choice.
  2. **Post-choice rounds: UNSTEERED.** "Both tags deliver identical
     nothing" is exactly that -- picking a tag delivers no state, so the
     round that follows a choice is generated with no injection at all.
     This is the one place H1's transcripts diverge from a verdict session.
  3. **Read states: SCHEDULED, not selected.** The state live at read ci
     alternates from the forced-phase end state -- `forced_end` when ci is
     even, its opposite when odd -- and does **not** depend on what the
     model picked. That is what licenses pooling all m = 6 reads (the
     2026-08-21 design ruling: "H1 states are scheduled, nothing is
     selected"), and it is why H1 can measure leak without measuring
     preference.

**This reading is Code's and is flagged as such in the dated entry.** The
alternative -- post-choice rounds steered by the schedule -- would make
"both tags deliver identical nothing" false, since a tag would then deliver
a state. If the design instance meant that, the change is one line.

## What the run does and does not decide

It records b, c, n_d and N and stops. **It does not evaluate the gate.** The
§3 criterion needs an exact Clopper-Pearson interval and no python on this
laptop has scipy (handoff trap 9), so gate evaluation is a separate
scipy-side analysis over the committed artifact. That separation is a
feature, not a workaround: the run's job is to collect to a declared stop
rule that depends only on totals, and a runner that cannot compute the
verdict cannot be accused of stopping when it liked the verdict.

Monitors: audit v2, frozen and sha-pinned, printed in the header.

Site: laptop (MLX). ~2.5 h on the gate-licensed cached round path.

Usage:
    jlens-qwen36/.venv/bin/python scripts/e2b_h1_sessions.py --n-sessions 1
    jlens-qwen36/.venv/bin/python scripts/e2b_h1_sessions.py
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from valence_core.adapters.base import Injection                # noqa: E402
from valence_core.e2b import summarize_leak                     # noqa: E402
from valence_core.e2b.session import (MENU_TEMPLATES,           # noqa: E402
                                      N_FREE, ROUND_TEMPLATES,
                                      SESSION_BANNER, STOP_CAP,
                                      load_tasks, session_rng,
                                      task_sequence)
from valence_core.e2b.statepresent import (                     # noqa: E402
    choice_read_statepresent)
from valence_core.regression.oracle import load_axis            # noqa: E402
from valence_core.session import (AuditSpec, build_ban_list,    # noqa: E402
                                  classify_response)

DATA = os.path.join(REPO, "data")
QWEN_PY = "jlens-qwen36/.venv/bin/python"
F = 2
TEMP = 0.7
ROSTER = (("granite", "plaza"), ("prism", "slate"),
          ("velvet", "walnut"), ("ridge", "saddle"))

# LOCK-h §6(b), bound in. Below 0.08 the certified ceiling is 1.00 -- at a
# discordance that far under the bar the feasibility corollary carries the
# certification however the flips cluster (verified in lockh_verify).
ICC_CEILING = ((0.08, 0.75), (0.10, 0.50), (0.15, 0.20),
               (0.20, 0.10), (0.25, 0.05), (0.30, 0.00))


def icc_ceiling_at(pi: float) -> float:
    """Conservative: the ceiling for the smallest grid point >= pi."""
    if pi < ICC_CEILING[0][0]:
        return 1.00
    for edge, val in ICC_CEILING:
        if pi <= edge:
            return val
    return 0.00


def _new_qwen_adapter(**kwargs):
    try:
        from valence_core.adapters.qwen_mlx import QwenMLXAdapter
        return QwenMLXAdapter(**kwargs)
    except (ImportError, RuntimeError) as exc:
        rel = os.path.relpath(os.path.abspath(__file__), REPO)
        raise SystemExit(
            "\nWRONG INTERPRETER (or missing clone) -- not a broken repo.\n"
            "  " + type(exc).__name__ + ": " + str(exc) + "\n\n"
            "  Run it as:\n\n      " + QWEN_PY + " " + rel + "\n")


def strata() -> list[dict]:
    out = []
    for pair in ROSTER:
        for m in (0, 1):
            for end in ("pos", "neg"):
                out.append({"pair": list(pair), "map": m,
                            "tag_plus": pair[m], "tag_minus": pair[1 - m],
                            "forced_end": end})
    return out


def block_order(cells, rng):
    a = [c for c in cells if c["map"] == 0]
    b = [c for c in cells if c["map"] == 1]
    a = [a[i] for i in rng.permutation(len(a))]
    b = [b[i] for i in rng.permutation(len(b))]
    if int(rng.integers(2)):
        a, b = b, a
    return [x for pair in zip(a, b) for x in pair]


def icc_binary(groups):
    groups = [g for g in groups if g]
    if len(groups) < 2:
        return {"icc": None, "reason": "fewer than 2 sessions"}
    N = sum(len(g) for g in groups)
    grand = sum(sum(g) for g in groups) / N
    msb = sum(len(g) * (np.mean(g) - grand) ** 2
              for g in groups) / (len(groups) - 1)
    dfw = N - len(groups)
    if dfw <= 0:
        return {"icc": None, "reason": "degenerate degrees of freedom"}
    msw = sum(((np.array(g) - np.mean(g)) ** 2).sum() for g in groups) / dfw
    k0 = (N - sum(len(g) ** 2 for g in groups) / N) / (len(groups) - 1)
    den = msb + (k0 - 1) * msw
    return {"icc": float(max(0.0, 0.0 if den <= 0 else (msb - msw) / den)),
            "k0": float(k0), "n_sessions": len(groups), "n_reads": N}


def run_session(adapter, idx, cell, tasks, inj, audit, ban_ids, temp,
                axis_key, cached, budget):
    """One H1 session. `budget` is a mutable dict carrying the global read
    counters, so the read-level stop can truncate a session mid-flight."""
    rng = session_rng("h1", idx)
    seq = task_sequence(rng, tasks, 2 * F + N_FREE)
    tag_plus, tag_minus = cell["tag_plus"], cell["tag_minus"]
    own = (tag_plus, tag_minus)
    label_ids = {t: int(adapter.encode(" " + t,
                                       add_special_tokens=False)[0])
                 for t in own}
    start_plus = cell["forced_end"] == "neg"
    order = (["pos", "neg"] if start_plus else ["neg", "pos"]) * F
    assert order[-1] == cell["forced_end"]

    transcript = SESSION_BANNER
    rounds, choices = [], []
    excluded, reason, truncated = False, None, False
    ti = n_round = 0

    for ri, pole in enumerate(order):
        n_round += 1
        tid, ttext = seq[ti]; ti += 1
        tag = tag_plus if pole == "pos" else tag_minus
        seg = ROUND_TEMPLATES[(idx + ri) % 4].format(
            n=n_round, tag=tag, task=ttext)
        seed = int(rng.integers(2 ** 31))
        g = adapter.generate(transcript, seg, injections=[inj[pole]],
                             seed=seed, temp=temp, max_tokens=STOP_CAP,
                             ban_ids=ban_ids, cached=cached)
        degen, lex = classify_response(g.text, audit, own)
        rounds.append({"phase": "forced", "round": ri, "pole": pole,
                       "tag": tag, "task": tid, "seed": seed,
                       "n_tok": len(g.token_ids), "cap_hit": g.cap_hit,
                       "degen": degen, "lexical": lex})
        transcript += seg + g.text + "\n"
        if lex:
            excluded, reason = True, f"lexical:{lex}@forced{ri}"
        elif degen:
            excluded, reason = True, f"audit:{degen}@forced{ri}"
        if excluded:
            break

    for ci in range(N_FREE):
        if excluded or budget["stop"]:
            break
        n_round += 1
        # SCHEDULED, not selected: alternate from the forced-phase end state.
        live = (cell["forced_end"] if ci % 2 == 0
                else ("neg" if cell["forced_end"] == "pos" else "pos"))
        a, b = ((tag_plus, tag_minus) if rng.integers(2) == 0
                else (tag_minus, tag_plus))
        menu = MENU_TEMPLATES[(idx + ci) % 4].format(n=n_round, a=a, b=b)
        pr = choice_read_statepresent(
            adapter, transcript + menu, a, b, label_ids, inj[live],
            axis=axis_key, session_id=f"h1:{idx}", round_index=ci)
        pick = pr.state_present.pick
        shadow = pr.shadow.pick
        flipped = pick != shadow
        # b = flips toward the +arm tag, c = toward the -arm tag
        direction = None
        if flipped:
            direction = "b" if pick == tag_plus else "c"
            budget["b" if direction == "b" else "c"] += 1
            budget["n_d"] += 1
        budget["N"] += 1
        d = pr.as_dict()
        tid, ttext = seq[ti]; ti += 1
        rec = {"round": ci, "menu_a": a, "menu_b": b,
               "live_state_at_read": live, "scheduled_not_selected": True,
               "pick": pick, "shadow_pick": shadow, "flipped": flipped,
               "flip_direction": direction, "task": tid,
               "paired_read": d, "global_read_index": budget["N"]}
        if budget["N"] >= budget["N_max"] or budget["n_d"] >= budget["n_d_star"]:
            budget["stop"] = True
            budget["stop_reason"] = ("N_max" if budget["N"] >= budget["N_max"]
                                     else "n_d_star")
            # 1-indexed to match the lock's language ("session 107, read 4")
            budget["stop_at"] = {"session": idx + 1, "read": ci + 1}
            choices.append(rec)
            truncated = True
            transcript += menu + f" {pick}\n"
            break
        # contingency-free: the pick delivers NOTHING, so this round is
        # generated with no injection at all
        chosen = ROUND_TEMPLATES[(idx + ci) % 4].format(
            n=n_round, tag=pick, task=ttext)
        seed = int(rng.integers(2 ** 31))
        prefix = transcript + menu + f" {pick}\n"
        g = adapter.generate(prefix, chosen, injections=[], seed=seed,
                             temp=temp, max_tokens=STOP_CAP,
                             ban_ids=ban_ids, cached=cached)
        degen, lex = classify_response(g.text, audit, own)
        rec.update({"seed": seed, "n_tok": len(g.token_ids),
                    "cap_hit": g.cap_hit, "degen": degen, "lexical": lex})
        choices.append(rec)
        transcript += menu + f" {pick}\n" + chosen + g.text + "\n"

    return {"session": idx, "stratum": cell, "excluded": excluded,
            "exclude_reason": reason, "truncated_by_stop": truncated,
            "rounds": rounds, "choices": choices, "transcript": transcript}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-sessions", type=int, default=112)
    ap.add_argument("--n-max", type=int, default=640)
    ap.add_argument("--n-d-star", type=int, default=200)
    ap.add_argument("--checkpoint-every", type=int, default=128)
    ap.add_argument("--layer", type=int, default=48)
    ap.add_argument("--frac", type=float, default=0.10)
    ap.add_argument("--axis-key", default="span_reward")
    ap.add_argument("--temp", type=float, default=TEMP)
    ap.add_argument("--order-seed", type=int, default=2026)
    ap.add_argument("--out", default=os.path.join(DATA, "e2b/h1_sessions.json"))
    args = ap.parse_args()

    cells = strata()
    rng = np.random.default_rng(args.order_seed)
    sched = []
    while len(sched) < args.n_sessions:
        sched += block_order(cells, rng)
    sched = sched[:args.n_sessions]

    acfg = json.load(open(os.path.join(DATA, "configs/e2b_audit_v2.json")))
    blob = json.dumps({k: v for k, v in acfg.items() if k != "sha16"},
                      sort_keys=True, separators=(",", ":")).encode()
    sha_now = hashlib.sha256(blob).hexdigest()[:16]
    if sha_now != acfg["sha16"]:
        raise SystemExit(f"H1 STOP: audit artifact sha mismatch -- recorded "
                         f"{acfg['sha16']}, recomputed {sha_now}")

    print("=== H1: the leakage budget, as locked (LOCK-h v1.3 §3/§3a) ===")
    print(f"  scheduled {args.n_sessions} sessions (7 blocks x 16 strata); "
          f"stop at n_d = {args.n_d_star} or N = {args.n_max} paired reads")
    print(f"  v1.3 corollary: n_d* needs pi_d >= "
          f"{args.n_d_star / args.n_max:.4f}, forbidden by the 0.30 ceiling "
          f"-> N_max binds; expected stop session 107, read 4")
    print(f"  AUDIT v2 FROZEN, sha16 = {acfg['sha16']} (verified) -- "
          f"{len(acfg['frame_fragments'])} fragments + "
          f"{len(acfg['junk_regex'])} junk patterns")
    print(f"  CONTINGENCY-FREE: both tags deliver nothing, so post-choice "
          f"rounds are UNSTEERED; read states are SCHEDULED (alternating "
          f"from the forced-phase end state), never selected")
    print(f"  THIN-MARGIN NOTE (carried per the adjudication): H2's upper "
          f"bound was 0.0636 against bar 0.0735. If H1's CI crosses, the "
          f"directional test is the design working, not a surprise.",
          flush=True)

    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    u, R = load_axis(args.layer)
    t0 = time.time()
    adapter = _new_qwen_adapter()
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)

    ban_ids, ban_strings = build_ban_list(
        adapter, path=os.path.join(DATA, "configs/e2a_ban_list.json"))
    audit = AuditSpec(ban_strings=tuple(ban_strings),
                      frame_fragments=tuple(acfg["frame_fragments"]),
                      junk_regex=tuple(acfg["junk_regex"]))
    g1 = json.load(open(os.path.join(DATA, "e2a/g1_kernel_gate.json")))
    row = g1["results"].get(str(args.frac))
    cached = bool(row and row["pass"])
    print(f"  g1 gate frac {args.frac}: "
          + (f"PASS max KL {row['max_kl']:.3e}" if row else "NOT COVERED")
          + f" -> rounds {'CACHED' if cached else 'UNCACHED'}; choice "
            f"forwards uncached always")
    inj = {"pos": Injection.at_frac(u, args.layer, args.frac, R),
           "neg": Injection.at_frac(u, args.layer, -args.frac, R)}
    print(f"  dose |alpha| = {abs(inj['pos'].alpha):.4f}; temp {args.temp}",
          flush=True)

    budget = {"N": 0, "n_d": 0, "b": 0, "c": 0, "stop": False,
              "stop_reason": None, "stop_at": None,
              "N_max": args.n_max, "n_d_star": args.n_d_star}
    sessions, checkpoints = [], []
    next_cp = args.checkpoint_every
    t1 = time.time()
    for i, cell in enumerate(sched):
        if budget["stop"]:
            break
        s = run_session(adapter, i, cell, tasks, inj, audit, ban_ids,
                        args.temp, args.axis_key, cached, budget)
        sessions.append(s)
        el = time.time() - t1
        print(f"    s{i + 1}/{len(sched)} [{'/'.join(cell['pair'])} "
              f"+{cell['tag_plus']} end={cell['forced_end']}] "
              f"reads={len(s['choices'])} N={budget['N']} "
              f"n_d={budget['n_d']} (b{budget['b']}/c{budget['c']})"
              + (f" EXCLUDED({s['exclude_reason']})" if s["excluded"] else "")
              + (" TRUNCATED" if s["truncated_by_stop"] else "")
              + f"  {el:.0f}s", flush=True)
        while budget["N"] >= next_cp:
            flips = [[int(c["flipped"]) for c in x["choices"]]
                     for x in sessions if x["choices"]]
            pi = budget["n_d"] / budget["N"]
            icc = icc_binary(flips)
            ceil_ = icc_ceiling_at(pi)
            cp = {"at_reads": next_cp, "N": budget["N"],
                  "n_d": budget["n_d"], "pi_hat_d": pi, "icc_hat": icc,
                  "icc_ceiling_for_pi": ceil_,
                  "above_ceiling": bool(icc.get("icc") is not None
                                        and icc["icc"] > ceil_),
                  "stability_pause": bool(pi > 0.30)}
            checkpoints.append(cp)
            print(f"      --- CHECKPOINT at {next_cp} reads: "
                  f"pi_hat_d = {pi:.4f}, ICC-hat = "
                  + (f"{icc['icc']:.4f}" if icc.get("icc") is not None
                     else str(icc.get("reason")))
                  + f", ceiling {ceil_:.2f} -> "
                  + ("ABOVE CEILING (PAUSE)" if cp["above_ceiling"]
                     else "within")
                  + (" | STABILITY PAUSE pi>0.30" if cp["stability_pause"]
                     else ""), flush=True)
            next_cp += args.checkpoint_every

    n_rounds = sum(len(s["rounds"]) + len(s["choices"]) for s in sessions)
    n_degen = sum(1 for s in sessions
                  for r in s["rounds"] + s["choices"] if r.get("degen"))
    prov = adapter.provenance()
    print(f"\n  STOPPED: {budget['stop_reason']} at "
          f"{budget['stop_at']} -- N = {budget['N']}, n_d = {budget['n_d']} "
          f"(b = {budget['b']}, c = {budget['c']})")
    print(f"  pi_hat_d = {budget['n_d'] / budget['N']:.4f}; "
          f"L_hat = (b - c)/N = "
          f"{(budget['b'] - budget['c']) / budget['N']:+.5f}")
    print(f"  sessions run {len(sessions)} of {len(sched)} scheduled; "
          f"excluded {sum(1 for s in sessions if s['excluded'])}; "
          f"degeneracy {n_degen}/{n_rounds}")
    print(f"  window: declared {prov['choice_window_declared']}, clipped "
          f"{prov['n_encodes_clipped']}")
    print(f"  GATE NOT EVALUATED HERE -- the §3 criterion needs an exact "
          f"CI and scipy; evaluate over this artifact.")

    out = {"item": "H1 leakage budget", "lock": "LOCK-h v1.3 §3/§3a",
           "audit_sha16": acfg["sha16"], "round_path_cached": cached,
           "layer": args.layer, "frac": args.frac,
           "alpha": abs(inj["pos"].alpha), "axis_key": args.axis_key,
           "temp": args.temp, "order_seed": args.order_seed,
           "n_scheduled": len(sched), "n_run": len(sessions),
           "budget": budget, "checkpoints": checkpoints,
           "n_rounds": n_rounds, "n_degenerate": n_degen,
           "n_excluded": sum(1 for s in sessions if s["excluded"]),
           "window": {"declared": prov["choice_window_declared"],
                      "n_encodes_clipped": prov["n_encodes_clipped"]},
           "provenance": prov, "sessions": sessions,
           "runtime_s": round(time.time() - t0, 1),
           "gate_evaluated": False,
           "decides_nothing": ("Collection to a declared stop rule that "
                               "depends only on totals. The §3 gate is "
                               "evaluated separately over this artifact.")}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {args.out}  ({out['runtime_s']:.0f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
