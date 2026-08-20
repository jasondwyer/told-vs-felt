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

**The panel is all three neighbours.** The vignette was approved verbatim
on 2026-08-20, so it is a full member and decides the registered reading
alongside the other two -- it is no longer opt-in. Its axis must exist
first (`s2_extract_vignette.py`); a missing axis is an error rather than a
shorter table, because an absent row reads as a tested-and-null row.

Usage:
    jlens-qwen36/.venv/bin/python scripts/s2_extract_vignette.py     # first: builds the vignette axis
    jlens-qwen36/.venv/bin/python scripts/s2_neighbor_axes.py        # then: the 11-arm panel
    jlens-qwen36/.venv/bin/python scripts/s2_neighbor_axes.py --n-per-probe 32   # declared subsample
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


QWEN_PY = "jlens-qwen36/.venv/bin/python"


def _new_qwen_adapter(**kwargs):
    """Build the MLX adapter, or fail with the fix instead of a traceback.

    Trap 3 in HANDOFF-2026-08-20, which has now cost real time: the system
    `python3` has no numpy and no MLX, and the only interpreter that has
    them is the one inside the gitignored clone. A raw traceback here reads
    as "the repo is broken" when the repo is fine and the interpreter is
    wrong.

    Both failure modes are caught because they look identical to a user and
    share one fix: ImportError (this python has no MLX) and RuntimeError
    (the clone itself is missing). Neither surfaces at import time -- the
    adapter loads MLX in its constructor -- so the guard wraps CONSTRUCTION,
    not the import. Wrapping the import was the first version and it never
    fired.
    """
    try:
            return QwenMLXAdapter(**kwargs)
    except (ImportError, RuntimeError) as exc:
        rel = os.path.relpath(os.path.abspath(__file__), REPO)
        raise SystemExit(
            "\nWRONG INTERPRETER (or missing clone) -- not a broken repo.\n"
            "  " + type(exc).__name__ + ": " + str(exc) + "\n\n"
            "  This script needs MLX and the Qwen stack, which live only in\n"
            "  the gitignored clone and its venv. Run it as:\n\n"
            "      " + QWEN_PY + " " + rel + "\n\n"
            "  System python3 has neither (HANDOFF-2026-08-20 trap 3). The\n"
            "  model-free regression suite runs under any python with numpy;\n"
            "  anything touching Qwen does not.\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--layer", type=int, default=B2B_LAYER)
    ap.add_argument("--frac", type=float, default=B2B_FRAC)
    ap.add_argument("--n-per-probe", type=int, default=0,
                    help="0 = all 96/probe (the exact qualification "
                         "battery). Whatever is passed IS the declaration.")
    ap.add_argument("--drop-vignette", action="store_true",
                    help="run without the vignette axis. The adjudication of "
                         "2026-08-20 made it a full panel member, so this "
                         "produces a DIFFERENT experiment from the "
                         "registered one and is recorded as such in the "
                         "artifact")
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
    if args.drop_vignette:
        specs = [sp for sp in specs if sp.name != VIGNETTE.name]
        print(f"  WARNING: running WITHOUT the vignette axis. It is a full "
              f"panel member as of the 2026-08-20 adjudication, so this is "
              f"not the registered §S2 panel.", flush=True)
    want_vignette = any(sp.name == VIGNETTE.name for sp in specs)
    if want_vignette and not os.path.exists(args.vignette_npz):
        raise SystemExit(
            f"S2 STOP: {args.vignette_npz} not found. The vignette axis is "
            f"part of the approved panel and must be extracted first:\n"
            f"    {QWEN_PY} scripts/s2_extract_vignette.py\n"
            f"Running the panel without it would drop a row, and an absent "
            f"row in a discriminant table reads as a tested-and-null row.")

    axes = load_axis_family(
        DATA, args.layer, specs=specs,
        extra_npz=args.vignette_npz if want_vignette else None)
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
    n_fwd = len(sub) * n_arms
    # Budget at the THROTTLED rate, per the 2026-08-12 calibration note:
    # 1,152-context arms ran 720-736 s each for the first three, then
    # 1,245-1,281 s -- sustained-load thermal throttling, ~1.7x. Quoting the
    # opening rate would under-budget a long multi-arm run by nearly half.
    open_s, throttled_s = 0.62, 1.10
    print(f"  forwards: {n_fwd:,}")
    print(f"  budget: {n_fwd * throttled_s / 3600:.1f} h at the throttled "
          f"rate ({throttled_s} s/ctx) -- NOT the "
          f"{n_fwd * open_s / 3600:.1f} h the opening rate implies "
          f"(RESULTS 2026-08-12 calibration note)", flush=True)
    print(f"  N DECLARED AT INVOCATION, BEFORE SCORING -- S2 has no "
          f"pre-registered n (PROPOSAL-g §5)", flush=True)

    t0 = time.time()
    adapter = _new_qwen_adapter()          # new work: full-session window
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
        "n_arms": n_arms, "n_forwards": n_fwd,
        "budget_h_throttled": round(n_fwd * throttled_s / 3600, 2),
        "panel": [sp.name for sp in specs],
        "is_registered_panel": bool(not args.drop_vignette),
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
