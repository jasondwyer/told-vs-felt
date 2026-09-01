#!/usr/bin/env python3
"""T-step identity check — PROPOSAL-j v1.2 AMENDMENT 2 (i)'s conditional.

WHY THIS EXISTS. The cached round path is licensed by
`data/e2a/g1_kernel_gate.json`, and that gate is **first-token only**: 32 rows
per frac keyed by (pole, probe), one KL pair each, no position dimension, and
`oracle.check_kernel` describes itself as comparing the "first-response-token
distribution". A first-token licence says the two paths agree on token 1. It
says nothing about token 2..T, and a round is up to 60 tokens long.

AMENDMENT 2 (i) therefore requires this check before D2: **>= 8 M-shaped
rounds at f = 0.20, cached vs uncached, token IDs identical.** Any mismatch
sends D2 uncached.

WHAT "M-SHAPED" MEANS HERE. Same generator call D2's M arm makes: the +axis
injection live over the round's task tokens, at 0.20 (alpha = 20.6020), L48,
the e2a v3 round templates, the h-roster tags, the real task corpus, the
frozen ban list, temp 0.7 with the SAME per-round seed on both paths. Two
paths, one seed, one prompt: if the sampled ids differ at any position, the
paths are not interchangeable for generation and the licence does not reach
where D2 would use it.

IDENTITY, NOT KL. The question is not whether the distributions are close --
the gate already answered that for token 1 -- but whether the SAMPLED TEXT is
the same, because that text is what every downstream instrument reads. Two
paths that agree in distribution to 7e-4 can still diverge at a sampling
boundary, and after they diverge once the prefixes differ and everything
after is incomparable. So this reports the first divergent position too.

This writes no canonical artifact and computes no verdict.
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

from valence_core.adapters import qwen_or_explain                 # noqa: E402
from valence_core.adapters.base import Injection                  # noqa: E402
from valence_core.e2d import config as C                          # noqa: E402
from valence_core.regression.oracle import load_axis              # noqa: E402
from valence_core.session import build_ban_list                   # noqa: E402
from valence_core.session_e2a import (ROUND_TEMPLATES,            # noqa: E402
                                      SESSION_BANNER, STOP_CAP,
                                      load_tasks, session_rng,
                                      task_sequence)

DATA = os.path.join(REPO, "data")


def gate_is_tstep(g1: dict) -> tuple[bool, str]:
    """Does the committed gate carry a per-position KL, or only token 1?

    Read structurally rather than trusted: a gate that grew a position
    dimension later should be detected, not assumed absent forever.
    """
    # The artifact nests per-frac dicts under BOTH "results" (summary) and
    # "rows" (each carrying its own "rows" list). Walk whatever is there
    # rather than assuming one shape -- and if no row list is found at all,
    # say so instead of silently concluding "not T-step", because an absent
    # answer and a negative answer are different things (trap 5).
    POSITION_KEYS = ("position", "pos_index", "step", "t", "per_position",
                     "kl_by_pos", "positions")
    found = []
    for container in ("rows", "results"):
        for frac, node in (g1.get(container) or {}).items():
            if not isinstance(node, dict):
                continue
            for r in node.get("rows", []) or []:
                found.append(set(r))
                if any(k in r for k in POSITION_KEYS):
                    return True, (f"{container}[{frac}].rows carry a position "
                                  f"key: {sorted(r)}")
    if not found:
        raise SystemExit(
            "CANNOT DETERMINE the g1 gate's scope: no per-probe row list found "
            "under 'rows' or 'results'. An undetermined licence is not a "
            "granted one -- stop and escalate rather than assuming either way.")
    return False, (f"rows are keyed {sorted(found[0])} across {len(found)} "
                   f"rows — no position dimension; first-response-token only")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-rounds", type=int, default=8,
                    help="AMENDMENT 2 (i) requires >= 8")
    ap.add_argument("--frac", type=float, default=C.D2_FRAC)
    ap.add_argument("--layer", type=int, default=C.LAYER)
    ap.add_argument("--temp", type=float, default=C.TEMP)
    ap.add_argument("--out", default=os.path.join(DATA, "e2d/tstep_check.json"))
    args = ap.parse_args()
    print("INVOCATION: " + " ".join([sys.executable] + sys.argv), flush=True)

    if args.n_rounds < 8:
        raise SystemExit(f"AMENDMENT 2 (i) requires >= 8 rounds; got "
                         f"{args.n_rounds}")

    g1 = json.load(open(os.path.join(DATA, "e2a/g1_kernel_gate.json")))
    tstep, why = gate_is_tstep(g1)
    print(f"  g1 gate: template_family {g1['template_family']}, "
          f"T-step licence = {tstep}", flush=True)
    print(f"    {why}", flush=True)
    row = (g1.get("results") or {}).get(str(args.frac)) \
        or (g1.get("rows") or {}).get(str(args.frac))
    print(f"    at frac {args.frac}: pass={row['pass']}, "
          f"max_kl={row['max_kl']:.6e} (bar {g1['gate']})", flush=True)

    t0 = time.time()
    adapter = qwen_or_explain(__file__)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)
    ban_ids, _ = build_ban_list(adapter)
    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))

    rw, R = load_axis(args.layer)
    inj = Injection.at_frac(rw, args.layer, args.frac, R)
    print(f"  dose: L{args.layer} frac {args.frac} alpha {inj.alpha:.4f} "
          f"(M-shaped: +axis live over task tokens)", flush=True)

    # M-shaped rounds: walk a real session's scaffolding so the prefixes are
    # the ones D2 will actually generate under, not synthetic stubs.
    rounds = []
    for si in range(64):          # enough sessions to reach any --n-rounds
        cell_pair = C.ROSTER[si % len(C.ROSTER)]
        tp = cell_pair[0]
        rng = session_rng(f"e2d-tstep-{si}", si)
        seq = task_sequence(rng, tasks, 2 * C.F + 6)
        transcript = SESSION_BANNER
        for ri in range(2 * C.F):
            tid, ttext = seq[ri]
            seg = ROUND_TEMPLATES[(si + ri) % 4].format(
                n=ri + 1, tag=tp, task=ttext)
            rounds.append({"session": si, "round": ri, "tag": tp,
                           "task": tid, "prefix": transcript, "segment": seg,
                           "seed": int(rng.integers(2 ** 31))})
            transcript += seg + "(placeholder)\n"
        if len(rounds) >= args.n_rounds:
            break
    rounds = rounds[:args.n_rounds]

    results = []
    n_identical = 0
    for i, r in enumerate(rounds, start=1):
        out = {}
        for path in ("cached", "uncached"):
            g = adapter.generate(r["prefix"], r["segment"], injections=[inj],
                                 seed=r["seed"], temp=args.temp,
                                 max_tokens=STOP_CAP, ban_ids=ban_ids,
                                 cached=(path == "cached"))
            out[path] = {"ids": list(map(int, g.token_ids)), "text": g.text}
        a, b = out["cached"]["ids"], out["uncached"]["ids"]
        same = a == b
        n_identical += int(same)
        first_div = None
        if not same:
            for k in range(max(len(a), len(b))):
                if k >= len(a) or k >= len(b) or a[k] != b[k]:
                    first_div = k
                    break
        results.append({
            "session": r["session"], "round": r["round"], "task": r["task"],
            "seed": r["seed"], "n_tok_cached": len(a), "n_tok_uncached": len(b),
            "identical": bool(same), "first_divergent_position": first_div,
            "text_cached": out["cached"]["text"],
            "text_uncached": out["uncached"]["text"]})
        print(f"    [{i}/{len(rounds)}] {'IDENTICAL' if same else 'DIVERGES'}"
              f"  cached {len(a)} tok / uncached {len(b)} tok"
              + (f"  first divergence at position {first_div}"
                 if not same else ""), flush=True)

    # Verdict computed before the artifact is written (trap 6).
    all_identical = (n_identical == len(results)) and len(results) >= 8
    lens = [r["n_tok_cached"] for r in results]
    verdict = {
        "n_rounds": len(results),
        "positions_verified": max(lens) if lens else 0,
        "position_coverage_note": (
            f"identity holds over positions 1..{max(lens) if lens else 0}; "
            f"STOP_CAP is {STOP_CAP}. The amendment's criterion is round "
            f"count, not position count -- this is reported so the limit of "
            f"the evidence is visible rather than implied."),
        "round_token_counts": lens,
        "n_identical": n_identical,
        "all_identical": bool(all_identical),
        "meets_amendment_minimum": bool(len(results) >= 8),
        "round_path_for_d2": "cached" if all_identical else "uncached",
        "rule": ("AMENDMENT 2 (i): >= 8 M-shaped rounds at 0.20, cached vs "
                 "uncached token IDs identical; any mismatch sends D2 "
                 "uncached."),
    }

    payload = {"item": "e2d T-step identity check",
               "proposal": "PROPOSAL-j v1.2 AMENDMENT 2 (i)",
               "frac": args.frac, "layer": args.layer, "temp": args.temp,
               "alpha": inj.alpha, "direction_sha": inj.direction_sha,
               "g1_gate": {"template_family": g1["template_family"],
                           "is_tstep_licence": bool(tstep), "why": why,
                           "max_kl_at_frac": row["max_kl"],
                           "pass_at_frac": row["pass"], "bar": g1["gate"]},
               "provenance": adapter.provenance(),
               "verdict": verdict, "rounds": results,
               "seconds": time.time() - t0}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(payload, fh, indent=1, default=float)

    print("\n" + "=" * 74)
    print(f"  T-STEP IDENTITY: {n_identical}/{len(results)} rounds identical")
    print(f"  ROUND PATH FOR D2: {verdict['round_path_for_d2'].upper()}")
    if not all_identical:
        print("  A first-token licence does not reach token 2..T here. D2 runs "
              "UNCACHED; this is not an incident, it is the conditional doing "
              "its job.")
    print(f"  wrote {args.out}  ({payload['seconds']:.0f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
