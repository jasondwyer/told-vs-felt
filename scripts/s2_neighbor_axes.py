#!/usr/bin/env python3
"""S2, step 2 -- the discriminant validity table: neighbour axes through the
identical e0 qualification battery at matched norm fraction.

PROPOSAL-g §5 S2. Same 12 locked instruments, same val-half contexts, same
layer, same frac, same random controls as the V1/B2b qualification the
reward axis passed. The only thing that varies between arms is which
direction is injected -- which is what makes the resulting numbers a
discriminant table rather than four unrelated experiments.

**Matched norm fraction is proven, not assumed.** `matched_injections`
constructs every axis's dose through `Injection.at_frac` on this model's own
R table and then asserts equal norm across every pair. If the axes were
dosed differently the table would measure the dose, and that failure mode is
invisible in the output.

**Reference arm runs in the same session.** The reward axis is re-measured
here rather than quoted from the 2026-08-08 artifact, because a ratio
between a number from today and a number from a different session with
different sampling silently imports every difference between them.

**S2's n is not pre-registered.** §5 declares no per-cell n for S2, so the
invocation is the declaration -- and, per the S1 precedent, it has to come
before scoring rather than after. The chosen value and the resulting forward
count are printed at startup and written into the artifact.

Site: laptop (the Qwen oracle -- these are published-tier Qwen numbers).

Usage:
    python scripts/s2_neighbor_axes.py                      # grounded panel
    python scripts/s2_neighbor_axes.py --include-vignette   # + PROPOSED axis
    python scripts/s2_neighbor_axes.py --n-per-probe 32     # declared subsample
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

from valence_core.adapters.base import Injection, assert_equal_norm  # noqa: E402
from valence_core.neighbors import (GROUNDED_PANEL, REFERENCE,  # noqa: E402
                                    VIGNETTE, axis_shas,
                                    discriminant_table, load_axis_family,
                                    matched_injections, specificity_reading)
from valence_core.regression.oracle import (B2B_FRAC, B2B_LAYER,  # noqa: E402
                                            VAL_TASKS_B2B,
                                            build_instruments, load_axis)

DATA = os.path.join(REPO, "data")


def build_val_contexts() -> list[tuple[int, str]]:
    """The B2b val-half battery: 24 held-out tasks x 4 paraphrase slots x 12
    probes = 1152 contexts.

    Deliberately duplicated from `oracle.check_b2b` rather than imported --
    that function is on the rule-26 acceptance path and takes an adapter, so
    factoring it out would refactor the very thing the refactor law protects.
    The regression suite pins this copy against the template instead.
    """
    tasks = {json.loads(l)["id"]: json.loads(l)
             for l in open(os.path.join(DATA, "corpus/e0_tasks.jsonl"))
             if l.strip()}
    probes = json.load(open(os.path.join(DATA, "configs/e0_probes.json")))["probes"]
    out = []
    for t_id in VAL_TASKS_B2B:
        t = tasks[t_id]
        for _pi in range(4):
            for qi, probe in enumerate(probes):
                out.append((qi, f"Task: {t['task']}\n"
                                f"Response: {t['completion']}\n"
                                f"Task: {probe}\nResponse:"))
    return out


def stratify(contexts, n_per_probe, seed=26):
    """Equal contexts per probe. None/0 takes all, which makes the battery an
    exact match to the qualification the reward axis passed."""
    by_probe: dict[int, list] = {}
    for qi, text in contexts:
        by_probe.setdefault(qi, []).append((qi, text))
    pool_n = min(len(v) for v in by_probe.values())
    if not n_per_probe:
        return contexts, pool_n
    rng = np.random.default_rng(seed)
    sub = []
    for qi in sorted(by_probe):
        pool = by_probe[qi]
        idx = sorted(rng.choice(len(pool), size=min(n_per_probe, len(pool)),
                                replace=False))
        sub.extend(pool[i] for i in idx)
    return sub, min(n_per_probe, pool_n)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--layer", type=int, default=B2B_LAYER)
    ap.add_argument("--frac", type=float, default=B2B_FRAC)
    ap.add_argument("--n-per-probe", type=int, default=0,
                    help="0 = all 96/probe (the exact qualification "
                         "battery). Whatever is passed IS the declaration.")
    ap.add_argument("--include-vignette", action="store_true",
                    help="include the PROPOSED, unadjudicated vignette axis; "
                         "it is reported but excluded from the registered "
                         "reading either way (rule 6)")
    ap.add_argument("--vignette-npz",
                    default=os.path.join(DATA, "e0/s2_vignette_axis.npz"))
    ap.add_argument("--out", default=os.path.join(DATA, "e0/s2_neighbor_axes.json"))
    args = ap.parse_args()

    instruments, G = build_instruments()
    if instruments is None:
        raise SystemExit("S2 STOP: e0_b1_markers.npz absent; the 12 "
                         "instruments cannot be rebuilt")
    print("=== S2 step 2: discriminant validity table ===")
    print(f"  instruments: {len(instruments)}, G = {G:.6f}", flush=True)

    specs = [REFERENCE, *GROUNDED_PANEL]
    if args.include_vignette:
        specs.append(VIGNETTE)
        print(f"  INCLUDING the vignette axis -- stimulus is PROPOSED and "
              f"unadjudicated; it is reported but cannot decide the "
              f"registered reading (rule 6)", flush=True)

    axes = load_axis_family(
        DATA, args.layer, specs=specs,
        extra_npz=args.vignette_npz if args.include_vignette else None)
    _, R = load_axis(args.layer)
    rand_u = np.load(os.path.join(DATA, "e0/e0_random_dirs.npz"))[
        f"L{args.layer}"].astype(np.float64)

    contexts = build_val_contexts()
    sub, per_probe = stratify(contexts, args.n_per_probe)
    n_arms = 1 + 2 * len(axes) + 2
    print(f"  contexts: {len(sub)}/arm ({per_probe}/probe)"
          + ("  [FULL -- the exact qualification battery]"
             if not args.n_per_probe else "  [DECLARED SUBSAMPLE]"))
    print(f"  arms: {n_arms} (base + {len(axes)} axes x 2 signs + 2 random)")
    print(f"  forwards: {len(sub) * n_arms}", flush=True)
    print(f"  N DECLARED AT INVOCATION, BEFORE SCORING -- S2 has no "
          f"pre-registered n (PROPOSAL-g §5)", flush=True)

    from valence_core.adapters.qwen_mlx import QwenMLXAdapter
    t0 = time.time()
    adapter = QwenMLXAdapter()          # new work: full-session window
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)

    # Matched dose across every axis, proven pairwise, both signs.
    pos = matched_injections(axes, args.layer, args.frac, R, sign=+1)
    neg = matched_injections(axes, args.layer, args.frac, R, sign=-1)
    r_pos = Injection.at_frac(rand_u, args.layer, args.frac, R)
    r_neg = Injection.at_frac(rand_u, args.layer, -args.frac, R)
    for inj in pos.values():            # randoms are the calibration arm:
        assert_equal_norm(inj, r_pos)   # they must carry the same dose too
    print(f"  matched dose verified: |alpha| = {abs(r_pos.alpha):.4f} "
          f"(frac {args.frac} x R_{args.layer} = {R[args.layer]:.2f}) "
          f"across {len(axes)} axes + randoms", flush=True)

    def arm_scores(injections, tag):
        scores = [[] for _ in instruments]
        t = time.time()
        for n, (qi, text) in enumerate(sub, start=1):
            res = adapter.forward(adapter.encode(text), capture_layers=(),
                                  injections=injections)
            lg = res.logits.astype(np.float64)
            lp = lg - (np.log(np.exp(lg - lg.max()).sum()) + lg.max())
            inst = instruments[qi]
            scores[qi].append(float(inst["w"] @ lp[inst["sel_ids"]]))
            if n % 128 == 0:
                print(f"    [{tag}] {n}/{len(sub)} "
                      f"{time.time() - t:.0f}s", flush=True)
        return scores

    def delta(arm, base):
        ds = []
        for qi, inst in enumerate(instruments):
            if not arm[qi]:
                continue
            ds.append((np.mean(arm[qi]) - np.mean(base[qi]))
                      / (inst["sigma"] + 1e-12))
        return float(np.mean(ds)), np.array(ds)

    base = arm_scores([], "base")
    arms = {}
    for name in axes:
        arms[f"{name}_pos"] = delta(arm_scores([pos[name]], f"{name}+"), base)
        arms[f"{name}_neg"] = delta(arm_scores([neg[name]], f"{name}-"), base)
    arms["rand_pos"] = delta(arm_scores([r_pos], "rand+"), base)
    arms["rand_neg"] = delta(arm_scores([r_neg], "rand-"), base)

    rows = discriminant_table(arms, G, specs=specs)
    reading = specificity_reading(rows)

    print(f"\n=== discriminant validity table (potency in G units, "
          f"G = {G:.4f}) ===")
    print(f"  {'axis':<10} {'grounded':<9} {'D+ (G)':>8} {'D- (G)':>8} "
          f"{'amp (G)':>8}  V1")
    for r in rows:
        print(f"  {r['axis']:<10} {str(r['grounded']):<9} "
              f"{r['delta_pos_G']:>+8.3f} {r['delta_neg_G']:>+8.3f} "
              f"{r['amplitude_G']:>8.3f}  "
              f"{'PASS' if r['v1_potency_pass'] else 'fail'}")
    print(f"\n  random envelope: {rows[0]['rand_envelope_sigma']:.4f} sigma")
    print(f"  reading: {reading['branch']} "
          f"(reference/{reading.get('strongest_neighbour', '-')} = "
          f"{reading.get('ratio', float('nan')):.2f}x)")
    if reading.get("excluded_ungrounded"):
        print(f"  excluded from the reading (ungrounded): "
              f"{reading['excluded_ungrounded']}")

    out = {
        "item": "S2",
        "layer": args.layer, "frac": args.frac,
        "alpha": abs(r_pos.alpha), "R_layer": R[args.layer],
        "G": G, "n_instruments": len(instruments),
        "n_contexts_per_arm": len(sub), "n_per_probe": per_probe,
        "n_declared_at_invocation": True,
        "n_arms": n_arms, "n_forwards": len(sub) * n_arms,
        "axis_shas": axis_shas(axes),
        "arms": {k: {"delta": v[0], "per_probe": v[1].tolist()}
                 for k, v in arms.items()},
        "table": rows,
        "reading": reading,
        "provenance": adapter.provenance(),
        "runtime_s": round(time.time() - t0, 1),
    }
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {args.out}  ({out['runtime_s']:.0f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
