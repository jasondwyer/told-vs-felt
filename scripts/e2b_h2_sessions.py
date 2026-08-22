#!/usr/bin/env python3
"""H2 PROPER -- dose and stability with the state live through ROUNDS and
READS (PROPOSAL-h §2 H2; LOCK-h v1.2 §3a).

The half the archive could not answer. The read-half precursor
(`e2b_h2_readstability.py`) measured what a live state does at a choice
position over prefixes that were themselves generated state-free. Here the
state is live from the forced phase onward, so the prefix each read sees is
one the state helped write -- which is the condition H1 and the verdict tier
actually run in, and the only condition under which pi_d means what LOCK-h
§3 needs it to mean.

## What runs

32 sessions = 2 full blocks x 16 strata (4 roster pairs x 2 label maps x 2
forced-phase end-states), 8 per roster pair, 6 reads each = 192 paired reads
(LOCK-h §3a). Session structure is the e2a lineage, byte-pinned by the Route
3 replay (200/200): banner, 2F = 4 forced rounds alternating poles, then
N_FREE = 6 free choices, each a menu read followed by a round generated under
the state the pick delivered.

State schedule, per PROPOSAL-h §3: the state a session is "on" at any choice
is the state its PREVIOUS selection delivered; at the first free choice it is
the final forced-phase state (which is what the third stratum dimension
counterbalances). Choosing the +tag delivers +axis, the -tag delivers -axis,
live from that choice through the following round and through the next read.

## What this deliberately does NOT compute

**No preference DV.** Delta_first is the verdict tier's statistic and H1 has
not run, so this script records picks (it must -- a flip is a disagreement
between picks) and refuses to aggregate them into a counterbalanced Delta.
The refusal is in code, not in prose: `summarize()` has no branch that
computes it. H2 is a dose-and-stability item; a preference number computed
here would be verdict data collected before its own leakage gate.

## Declared at invocation, because the lock does not fix it

§3a says degeneracy monitors "bind by exact binomial against the declared
harness tolerance" without naming the rate. Following the S2 precedent the
invocation IS the declaration, printed before any scoring: `--degen-p0`,
default 0.05, one-sided exact binomial. The anchor is the e2a archive's own
measured base rate, **29/1894 = 0.0153** over 200 sessions of the same
template family, so 0.05 sits ~3x above the observed rate (rule 21:
measured-base-rate classes bind by exact binomial against a declared p0).
H2 PASS/FAIL is a design-instance disposition on the numbers regardless.

Site: laptop (MLX). Smoke first -- `--n-sessions 2` -- and post the measured
budget before committing to 32.

Usage:
    jlens-qwen36/.venv/bin/python scripts/e2b_h2_sessions.py --n-sessions 2
    jlens-qwen36/.venv/bin/python scripts/e2b_h2_sessions.py
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

from valence_core.adapters import qwen_or_explain               # noqa: E402
from valence_core.adapters.base import Injection                # noqa: E402
from valence_core.e2b import summarize_leak                     # noqa: E402
from valence_core.e2b.statepresent import (                     # noqa: E402
    choice_read_statepresent)
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

# The frozen e2a degeneracy audit (config v3, clause 2a). Frozen means
# frozen: these fragments are the cycle-3/4 list, reproduced here so the
# monitor is the same monitor. No post-data additions, ever.
AUDIT_FRAME_FRAGMENTS = (
    "Config evaluation session", "evaluation session", "[round",
    "Config choice", "Available configs", "Configs available",
    "Configs on offer", "Task:", "Response:",
)

ROSTER = (("granite", "plaza"), ("prism", "slate"),
          ("velvet", "walnut"), ("ridge", "saddle"))


def strata() -> list[dict]:
    """The 16 cells: 4 pairs x 2 label maps x 2 forced-phase end-states."""
    out = []
    for pair in ROSTER:
        for m in (0, 1):
            plus, minus = (pair[m], pair[1 - m])
            for end in ("pos", "neg"):
                out.append({"pair": list(pair), "map": m, "tag_plus": plus,
                            "tag_minus": minus, "forced_end": end})
    return out


def block_order(cells: list[dict], rng: np.random.Generator) -> list[dict]:
    """Seeded within-block order, constrained to ALTERNATE label maps.

    §3a asks for both properties and they pull against each other: a free
    permutation will not alternate, and a fixed alternation is not seeded.
    The resolution is to permute each map's eight cells independently and
    then interleave them, with a seeded coin deciding which map leads. Order
    is random within the constraint, and the constraint holds exactly.
    """
    a = [c for c in cells if c["map"] == 0]
    b = [c for c in cells if c["map"] == 1]
    a = [a[i] for i in rng.permutation(len(a))]
    b = [b[i] for i in rng.permutation(len(b))]
    if int(rng.integers(2)):
        a, b = b, a
    out = []
    for x, y in zip(a, b):
        out += [x, y]
    return out


def run_session(adapter, idx: int, cell: dict, tasks, inj: dict,
                audit: AuditSpec, ban_ids, temp: float,
                axis_key: str, cached: bool) -> dict:
    """One H2 session, state live through rounds and reads."""
    rng = session_rng("h2", idx)
    n_rounds = 2 * F + N_FREE
    seq = task_sequence(rng, tasks, n_rounds)
    tag_plus, tag_minus = cell["tag_plus"], cell["tag_minus"]
    own = (tag_plus, tag_minus)
    label_ids = {t: int(adapter.encode(" " + t,
                                       add_special_tokens=False)[0])
                 for t in own}

    # start_plus is fixed by the stratum's required forced-phase END state:
    # with F = 2 the order is [p, q, p, q], so the last pole is q.
    start_plus = cell["forced_end"] == "neg"
    order = (["pos", "neg"] if start_plus else ["neg", "pos"]) * F
    assert order[-1] == cell["forced_end"]

    transcript = SESSION_BANNER
    rounds, choices, pairs = [], [], []
    excluded, reason = False, None
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
            # v3: a degenerate round BEFORE the first free choice excludes
            excluded, reason = True, f"audit:{degen}@forced{ri}"
        if excluded:
            break

    live = cell["forced_end"]           # state the first free read sits on
    for ci in range(N_FREE):
        if excluded:
            break
        n_round += 1
        a, b = ((tag_plus, tag_minus) if rng.integers(2) == 0
                else (tag_minus, tag_plus))
        menu = MENU_TEMPLATES[(idx + ci) % 4].format(n=n_round, a=a, b=b)
        pr = choice_read_statepresent(
            adapter, transcript + menu, a, b, label_ids, inj[live],
            axis=axis_key, session_id=f"h2:{idx}", round_index=ci)
        pairs.append(pr)
        pick = pr.state_present.pick
        picked_pole = "pos" if pick == tag_plus else "neg"
        tid, ttext = seq[ti]; ti += 1
        chosen = ROUND_TEMPLATES[(idx + ci) % 4].format(
            n=n_round, tag=pick, task=ttext)
        seed = int(rng.integers(2 ** 31))
        prefix = transcript + menu + f" {pick}\n"
        g = adapter.generate(prefix, chosen, injections=[inj[picked_pole]],
                             seed=seed, temp=temp, max_tokens=STOP_CAP,
                             ban_ids=ban_ids, cached=cached)
        degen, lex = classify_response(g.text, audit, own)
        d = pr.as_dict()
        choices.append({"round": ci, "menu_a": a, "menu_b": b,
                        "live_state_at_read": live,
                        "pick": pick, "picked_pole": picked_pole,
                        "task": tid, "seed": seed,
                        "n_tok": len(g.token_ids), "cap_hit": g.cap_hit,
                        "degen": degen, "lexical": lex,
                        "paired_read": d})
        transcript += menu + f" {pick}\n" + chosen + g.text + "\n"
        live = picked_pole             # the pick delivers the next state

    return {"session": idx, "stratum": cell, "start_plus": start_plus,
            "excluded": excluded, "exclude_reason": reason,
            "rounds": rounds, "choices": choices, "transcript": transcript,
            "_pairs": pairs}


def icc_binary(groups):
    groups = [g for g in groups if g]
    if len(groups) < 2:
        return {"icc": None, "reason": "fewer than 2 sessions"}
    N = sum(len(g) for g in groups)
    grand = sum(sum(g) for g in groups) / N
    msb = sum(len(g) * (np.mean(g) - grand) ** 2 for g in groups) / (len(groups) - 1)
    dfw = N - len(groups)
    if dfw <= 0:
        return {"icc": None, "reason": "degenerate degrees of freedom"}
    msw = sum(((np.array(g) - np.mean(g)) ** 2).sum() for g in groups) / dfw
    k0 = (N - sum(len(g) ** 2 for g in groups) / N) / (len(groups) - 1)
    den = msb + (k0 - 1) * msw
    return {"icc": float(max(0.0, 0.0 if den <= 0 else (msb - msw) / den)),
            "k0": float(k0), "n_sessions": len(groups), "n_reads": N}


def exact_binom_upper_p(k: int, n: int, p0: float) -> float:
    """One-sided exact binomial P(X >= k | p0). No scipy on this laptop."""
    if k <= 0:
        return 1.0
    from math import comb
    return float(sum(comb(n, i) * p0 ** i * (1 - p0) ** (n - i)
                     for i in range(k, n + 1)))


def summarize(sessions, degen_p0: float) -> dict:
    """Stability only. There is deliberately no Delta_first here."""
    pairs = [p for s in sessions for p in s["_pairs"]]
    leak = summarize_leak(pairs)
    flips = [[int(c["paired_read"]["leak"]["flipped"]) for c in s["choices"]]
             for s in sessions if s["choices"]]
    n_rounds = sum(len(s["rounds"]) + len(s["choices"]) for s in sessions)
    n_degen = sum(1 for s in sessions
                  for r in s["rounds"] + s["choices"] if r["degen"])
    n_cap = sum(1 for s in sessions
                for r in s["rounds"] + s["choices"] if r["cap_hit"])
    p = exact_binom_upper_p(n_degen, n_rounds, degen_p0) if n_rounds else 1.0
    return {"n_sessions": len(sessions),
            "n_excluded": sum(1 for s in sessions if s["excluded"]),
            "n_paired_reads": len(pairs),
            "pi_hat_d": leak.get("flip_rate"),
            "icc_hat": icc_binary(flips),
            "leak_summary": leak,
            "degeneracy": {"n": n_degen, "of": n_rounds,
                           "rate": n_degen / n_rounds if n_rounds else None,
                           "declared_p0": degen_p0,
                           "exact_binomial_p_one_sided": p,
                           "within_tolerance": bool(p > 0.05)},
            "cap_hits": {"n": n_cap, "of": n_rounds},
            "preference_dv": ("NOT COMPUTED. Delta_first belongs to the "
                              "verdict tier and H1 has not run; H2 is a "
                              "dose-and-stability item.")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-sessions", type=int, default=32)
    ap.add_argument("--layer", type=int, default=48)
    ap.add_argument("--frac", type=float, default=0.10)
    ap.add_argument("--axis-key", default="span_reward")
    ap.add_argument("--temp", type=float, default=TEMP)
    ap.add_argument("--degen-p0", type=float, default=0.05)
    ap.add_argument("--order-seed", type=int, default=2026)
    ap.add_argument("--out", default=os.path.join(DATA, "e2b/h2_sessions.json"))
    args = ap.parse_args()

    cells = strata()
    rng = np.random.default_rng(args.order_seed)
    sched = []
    while len(sched) < args.n_sessions:
        sched += block_order(cells, rng)
    sched = sched[:args.n_sessions]

    print("=== H2 PROPER: state live through ROUNDS and READS ===")
    print(f"  LOCK-h v1.2 §3a: {args.n_sessions} sessions, "
          f"{len(cells)} strata (4 pairs x 2 maps x 2 forced-end states), "
          f"{N_FREE} reads each -> {args.n_sessions * N_FREE} paired reads")
    print(f"  order seed {args.order_seed}; within-block order alternates "
          f"label maps")
    print(f"  DECLARED AT INVOCATION, BEFORE SCORING: degeneracy binds by "
          f"one-sided exact binomial vs p0 = {args.degen_p0} "
          f"(e2a archive base rate 29/1894 = 0.0153)", flush=True)

    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    u, R = load_axis(args.layer)
    t0 = time.time()
    adapter = qwen_or_explain(__file__)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)

    ban_ids, ban_strings = build_ban_list(
        adapter, path=os.path.join(DATA, "configs/e2a_ban_list.json"))
    audit = AuditSpec(ban_strings=tuple(ban_strings),
                      frame_fragments=AUDIT_FRAME_FRAGMENTS)
    # Rule 2: the cached round path is reachable only behind a passed
    # kernel gate, and the decision is READ FROM THE ARTIFACT rather than
    # taken by a flag -- exactly as the e2a runner did it
    # (`use_cached_rounds = g1["results"][str(frac)]["pass"]`). e2a ran its
    # rounds cached under this gate, so running H2 uncached would be the
    # DEVIATION from the sessions H2 must be comparable to, not the safe
    # choice. Choice forwards stay state-free uncached regardless (g3'
    # clause 1): `choice_read_statepresent` goes through `adapter.forward`,
    # which has no cached path at all.
    g1_path = os.path.join(DATA, "e2a/g1_kernel_gate.json")
    g1 = json.load(open(g1_path))
    g1_row = g1["results"].get(str(args.frac))
    use_cached = bool(g1_row and g1_row["pass"])
    print(f"  g1 kernel gate ({os.path.relpath(g1_path, REPO)}, "
          f"template_family {g1.get('template_family')}): frac "
          f"{args.frac} -> "
          + (f"PASS, max KL {g1_row['max_kl']:.3e} < {g1['gate']:.0e}"
             if g1_row else "NOT COVERED")
          + f" -> round generation {'CACHED' if use_cached else 'UNCACHED'}"
            f"; choice forwards uncached always", flush=True)

    inj = {"pos": Injection.at_frac(u, args.layer, args.frac, R),
           "neg": Injection.at_frac(u, args.layer, -args.frac, R)}
    print(f"  dose: |alpha| = {abs(inj['pos'].alpha):.4f} = {args.frac} x "
          f"R_{args.layer} ({R[args.layer]:.2f}); temp {args.temp}; "
          f"ban list {len(ban_ids)} ids (generation only)", flush=True)

    sessions = []
    t1 = time.time()
    for i, cell in enumerate(sched):
        s = run_session(adapter, i, cell, tasks, inj, audit, ban_ids,
                        args.temp, args.axis_key, use_cached)
        sessions.append(s)
        el = time.time() - t1
        print(f"    session {i + 1}/{len(sched)} "
              f"[{'/'.join(cell['pair'])} +{cell['tag_plus']} "
              f"end={cell['forced_end']}] "
              f"{len(s['choices'])} reads"
              + (f" EXCLUDED ({s['exclude_reason']})" if s["excluded"] else "")
              + f"  {el:.0f}s ({el / (i + 1):.1f}s/session)", flush=True)

    summ = summarize(sessions, args.degen_p0)
    prov = adapter.provenance()
    icc = summ["icc_hat"]

    print(f"\n  --- state-through-rounds (pi_hat_d, ICC-hat): H1's "
          f"planning-relevant precursor ---")
    print(f"    paired reads             = {summ['n_paired_reads']}")
    print(f"    pi_hat_d                 = {summ['pi_hat_d']:.4f}"
          if summ["pi_hat_d"] is not None else "    pi_hat_d = n/a")
    print(f"    ICC-hat                  = "
          + (f"{icc['icc']:.4f}" if icc.get("icc") is not None
             else str(icc.get("reason"))))
    d = summ["degeneracy"]
    print(f"\n  degeneracy {d['n']}/{d['of']} = "
          f"{d['rate']:.4f} vs declared p0 {d['declared_p0']} -> exact "
          f"binomial p = {d['exact_binomial_p_one_sided']:.4f} "
          f"[{'WITHIN' if d['within_tolerance'] else 'ABOVE'} tolerance]")
    print(f"  cap hits {summ['cap_hits']['n']}/{summ['cap_hits']['of']}; "
          f"excluded sessions {summ['n_excluded']}/{summ['n_sessions']}")
    print(f"  window: declared {prov['choice_window_declared']}, "
          f"n_encodes_clipped = {prov['n_encodes_clipped']}")
    print(f"  NO PREFERENCE DV COMPUTED (H1 has not run).")

    out = {"item": "H2 proper -- dose and stability, state live through "
                   "rounds and reads",
           "lock": "LOCK-h v1.2 §3a", "layer": args.layer,
           "frac": args.frac, "alpha": abs(inj["pos"].alpha),
           "R_layer": R[args.layer], "axis_key": args.axis_key,
           "temp": args.temp, "order_seed": args.order_seed,
           "round_path_cached": use_cached,
           "g1_gate": {"template_family": g1.get("template_family"),
                       "bar": g1.get("gate"), "row": g1_row,
                       "note": ("choice forwards are state-free uncached "
                                "regardless (g3' clause 1)")},
           "declared_degen_p0": args.degen_p0,
           "n_strata": len(cells), "schedule": [c for c in sched],
           "summary": summ,
           "window": {"declared": prov["choice_window_declared"],
                      "n_encodes_clipped": prov["n_encodes_clipped"]},
           "provenance": prov,
           "sessions": [{k: v for k, v in s.items() if k != "_pairs"}
                        for s in sessions],
           "runtime_s": round(time.time() - t0, 1),
           "decides_nothing": ("H2 PASS/FAIL is a design-instance "
                               "disposition on these numbers.")}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {args.out}  ({out['runtime_s']:.0f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
