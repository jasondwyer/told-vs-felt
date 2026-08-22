#!/usr/bin/env python3
"""A4, part 2 -- causal qualification, layer selection, dose ladder.

PROPOSAL-g §3 A4, whose procedure is "fixed here in full" by the
pre-registration and whose numeric outputs "go into LOCK-g.md untouched".
This script therefore implements the stated procedure and reports every
term; it selects no threshold of its own and writes no verdict.

    Layer selection   candidates {L32, L44, L52, L60}; per stage, the layer
                      with the largest sign-correct displacement on the FIT
                      half at frac 0.10. Verdict statistics come only from
                      the VAL half.
    Dose ladder       fracs {0.05, 0.10, 0.20, 0.40} of R_l at the selected
                      layer. Minimum effective dose = the smallest frac
                      passing potency.
    Potency           Delta+ exceeds the control envelope; Delta- exceeds it
                      with opposite sign; sign locks across the
                      counterbalanced assignment. Controls at EVERY frac.
    Currency          everything divided by G_c from part 1 (§2.4: cross-
                      stage comparisons are made only in G_c units).

WHY SELECTION AND VERDICT SIT ON DIFFERENT HALVES. Choosing the layer reads
the data. A dose ladder scored on the rows that chose the layer reports the
selection back to you with a confidence interval around it.

THE CONTROL FAMILY, AND WHY SHAM IS NOT DECORATIVE. Each frac runs
`--n-random` norm-matched random directions at both signs, plus a SHAM arm
that is a second no-injection pass. Under a deterministic backend Delta_sham
is exactly 0.0 -- and that is the point: it measures the apparatus floor the
same way the real arms are measured, so "the envelope is small" stops being
an assumption about the harness. If A5's characterization finds nonzero
residual nondeterminism, Delta_sham is where it shows up first.

WHAT `sign locks` MEANS HERE, STATED SO IT CANNOT DRIFT. The probe readout
has no label map to counterbalance; the counterbalanced assignment is the
sign of the injection. Sign lock is therefore: the two poles displace the
readout in OPPOSITE directions (Delta+ > 0 and Delta- < 0). It is reported
as its own conjunct, never folded into a single word.

THE V1-LINEAGE FORM IS REPORTED BESIDE THE PROPOSAL-g CRITERION, not
instead of it: Delta+ >= 0.5*G_c, Delta- <= -0.5*G_c, min(Delta+, |Delta-|)
> 2*max|Delta_rand|. That is the rule the Qwen V1 result was declared under,
so carrying it makes the two programs commensurable at a glance. Where the
two criteria disagree, both are printed and neither is resolved here.

Dose is frac x R_l from THIS stage's own A3 capture (rule 1). Alphas are
never inherited across checkpoints, and `Injection.at_frac` refuses a layer
that is not in the supplied table.

Usage (box, after box_a3_extract.py and box_a4_instrument.py for the stage):
    python scripts/box_a4_hijack.py --stage base

Laptop dry run:
    python scripts/box_a4_hijack.py --selftest --stage base \\
        --a3 /tmp/a3.json --instrument /tmp/a4i.json --out /tmp/a4h.json
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
sys.path.insert(0, os.path.join(REPO, "scripts"))

from box_e0_corpus import (FIT_IDS, VAL_IDS, assert_frozen_inputs,  # noqa: E402
                           b2_contexts)
from valence_core.adapters.base import Injection                   # noqa: E402
from valence_core.extract import assert_stage_splits               # noqa: E402

DATA = os.path.join(REPO, "data")

CANDIDATE_LAYERS = (32, 44, 52, 60)             # PROPOSAL-g §3 A4, fixed
SELECTION_FRAC = 0.10                           # PROPOSAL-g §3 A4, fixed
DOSE_LADDER = (0.05, 0.10, 0.20, 0.40)          # PROPOSAL-g §3 A4, fixed
N_RANDOM_MIN = 3                                # ">= 3 norm-matched randoms"
RANDOM_SEED = 20260822


def build_adapter(args):
    if args.selftest:
        from box_selftest_stub import SelfTestAdapter, refuse_canonical_out
        refuse_canonical_out(args.out or "", args.models_root)
        print("  *** SELFTEST: synthetic apparatus, NOT a model. No result "
              "from this run is a measurement. ***", flush=True)
        return SelfTestAdapter(args.stage)
    from valence_core.adapters.olmo_hf import OLMoHFAdapter
    return OLMoHFAdapter(os.path.join(args.models_root, args.stage))


def log_probs(logits: np.ndarray) -> np.ndarray:
    lg = np.asarray(logits, dtype=np.float64)
    m = lg.max()
    return lg - (np.log(np.exp(lg - m).sum()) + m)


def arm_scores(adapter, rows, instruments, injections, tag: str,
               progress_every: int = 200) -> list[list[float]]:
    """Per-probe instrument scores for one arm."""
    scores: list[list[float]] = [[] for _ in instruments]
    t0 = time.time()
    for n, r in enumerate(rows, start=1):
        res = adapter.forward(adapter.encode(r["text"]), capture_layers=(),
                              injections=injections)
        lp = log_probs(res.logits)
        inst = instruments[r["probe"]]
        scores[r["probe"]].append(float(inst["w"] @ lp[inst["sel_ids"]]))
        if progress_every and n % progress_every == 0:
            print(f"      [{tag}] {n}/{len(rows)} {time.time() - t0:.0f}s",
                  flush=True)
    return scores


def delta(arm, base, instruments) -> tuple[float, list[float]]:
    """Mean over probes of the per-probe displacement in sigma units --
    identical in form to the published B2b statistic."""
    ds = []
    for qi, inst in enumerate(instruments):
        if not arm[qi] or not base[qi]:
            continue
        ds.append((float(np.mean(arm[qi])) - float(np.mean(base[qi])))
                  / (inst["sigma"] + 1e-12))
    return float(np.mean(ds)), ds


def load_instruments(path: str) -> tuple[list, dict]:
    meta = json.load(open(path))
    npz = np.load(os.path.join(os.path.dirname(os.path.abspath(path)),
                               meta["instrument_npz"]))
    sigma = npz["sigma"]
    insts = [{"sel_ids": npz[f"sel_{i}"], "w": npz[f"w_{i}"],
              "sigma": float(sigma[i])} for i in range(len(sigma))]
    return insts, meta


def plan_only(args) -> int:
    """The forward budget, with no model and no artifacts. A5 asks for a
    timing budget that is an artifact rather than a vibe; this is its
    count half, and the seconds-per-forward half comes from a real run."""
    fracs = tuple(float(x) for x in args.fracs.split(","))
    cand = [int(x) for x in args.layers.split(",")]
    n_fit = len(b2_contexts(list(FIT_IDS), repeats=args.repeats))
    n_val = len(b2_contexts(list(VAL_IDS), repeats=args.repeats))
    n_ctl = 2 * args.n_random + 1
    sel = n_fit * (2 * len(cand) + 1)
    lad = n_val * (1 + len(fracs) * (2 + n_ctl))
    print("A4 part 2 forward budget, per stage (no model loaded)")
    print(f"  candidates {cand} | fracs {list(fracs)} | "
          f"{args.n_random} randoms x2 + sham | repeats {args.repeats}")
    print(f"  selection (fit half): {n_fit} contexts x "
          f"{2 * len(cand) + 1} arms = {sel:,}")
    print(f"  ladder    (val half): {n_val} contexts x "
          f"{1 + len(fracs) * (2 + n_ctl)} arms = {lad:,}")
    print(f"  TOTAL per stage: {sel + lad:,}   x4 stages: "
          f"{4 * (sel + lad):,}")
    for sec in (0.05, 0.09, 0.15):
        print(f"    at {sec:.2f} s/forward: {(sel + lad) * sec / 60:6.1f} "
              f"min/stage, {4 * (sel + lad) * sec / 3600:5.2f} h for four")
    print("  (A3 adds 1,344 forwards/stage; A4 part 1 adds 4,608/stage)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True)
    ap.add_argument("--models-root", default="/workspace/models")
    ap.add_argument("--a3", default=None, help="A3 artifact json")
    ap.add_argument("--instrument", default=None, help="A4 part-1 json")
    ap.add_argument("--axis-key", default="span_reward")
    ap.add_argument("--layers", default=",".join(map(str, CANDIDATE_LAYERS)))
    ap.add_argument("--fracs", default=",".join(map(str, DOSE_LADDER)))
    ap.add_argument("--n-random", type=int, default=N_RANDOM_MIN)
    ap.add_argument("--repeats", type=int, default=1,
                    help="identical b2 contexts per (task, probe); the "
                         "published Qwen arm used 4. See box_e0_corpus")
    ap.add_argument("--tasks", type=int, default=0, help="smoke only")
    ap.add_argument("--probes", type=int, default=0, help="smoke only")
    ap.add_argument("--plan-only", action="store_true",
                    help="print the forward budget and exit; loads no model "
                         "and needs no artifacts (A5 budgeting)")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    if args.plan_only:
        return plan_only(args)

    if args.n_random < N_RANDOM_MIN:
        raise SystemExit(f"--n-random {args.n_random} is below the "
                         f"pre-registered minimum of {N_RANDOM_MIN} "
                         f"(PROPOSAL-g §3 A4)")

    assert_frozen_inputs()
    a3_path = args.a3 or os.path.join(args.models_root,
                                      f"a3_axes_{args.stage}.json")
    inst_path = args.instrument or os.path.join(
        args.models_root, f"a4_instrument_{args.stage}.json")
    for p in (a3_path, inst_path):
        if not os.path.exists(p):
            raise SystemExit(f"missing input {p} -- run box_a3_extract.py and "
                             f"box_a4_instrument.py for this stage first")
    a3 = json.load(open(a3_path))
    instruments, inst_meta = load_instruments(inst_path)
    for name, art in (("A3", a3), ("A4-instrument", inst_meta)):
        if art["stage"] != args.stage:
            raise SystemExit(f"{name} artifact is stage {art['stage']!r}, not "
                             f"{args.stage!r} -- rule 1: nothing is inherited "
                             f"across checkpoints")
    axes = np.load(os.path.join(os.path.dirname(os.path.abspath(a3_path)),
                                a3["axes_npz"]))
    axis_layers = [int(x) for x in axes["layers"]]
    u_all = axes[args.axis_key].astype(np.float64)
    R = {int(k): float(v) for k, v in a3["R_per_layer_spanmean"].items()}
    G_c = float(inst_meta["G_c"])

    fit_ids, val_ids = list(FIT_IDS), list(VAL_IDS)
    if args.tasks:
        fit_ids, val_ids = fit_ids[:args.tasks], val_ids[:args.tasks]
    fit_rows = b2_contexts(fit_ids, repeats=args.repeats)
    val_rows = b2_contexts(val_ids, repeats=args.repeats)
    if args.probes:
        fit_rows = [r for r in fit_rows if r["probe"] < args.probes]
        val_rows = [r for r in val_rows if r["probe"] < args.probes]

    cand = [l for l in (int(x) for x in args.layers.split(",")) if l in axis_layers]
    missing = [l for l in (int(x) for x in args.layers.split(","))
               if l not in axis_layers]
    if missing:
        raise SystemExit(f"A3 did not capture candidate layers {missing}; "
                         f"it has {axis_layers}. Re-run A3 with --layers "
                         f"covering the A4 candidates.")
    fracs = tuple(float(x) for x in args.fracs.split(","))

    n_ctl = 2 * args.n_random + 1
    planned = (len(fit_rows) * (2 * len(cand) + 1)
               + len(val_rows) * (1 + len(fracs) * (2 + n_ctl)))
    smoke = bool(args.tasks or args.probes or args.selftest)
    print(f"=== A4 part 2: causal qualification | stage {args.stage} ===",
          flush=True)
    print(f"  axis {args.axis_key} from {os.path.basename(a3_path)} "
          f"(family sha {a3['axis_family_sha16']})", flush=True)
    print(f"  G_c = {G_c:+.6f} from {os.path.basename(inst_path)} "
          f"(floors met: {inst_meta['declared_floors']['all_floors_met']})",
          flush=True)
    if not inst_meta["declared_floors"]["all_floors_met"]:
        print("  NOTE: G_c is below a declared floor at this stage. Deltas in "
              "G_c units below are printed anyway and are NOT to be compared "
              "across stages until the design instance disposes of §2.4's "
              "pooled-G fallback.", flush=True)
    print(f"  selection: fit half ({len(fit_rows)} contexts) at frac "
          f"{SELECTION_FRAC}, candidates {cand}", flush=True)
    print(f"  ladder:    val half ({len(val_rows)} contexts), fracs {fracs}, "
          f"{args.n_random} randoms x2 signs + sham per frac", flush=True)
    print(f"  planned forwards: {planned:,}", flush=True)
    if smoke:
        print("  *** SMOKE -- reduced corpus; not a qualification of record "
              "***", flush=True)

    t0 = time.time()
    adapter = build_adapter(args)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)

    # --- layer selection, FIT half --------------------------------------
    print(f"\n--- layer selection (fit half, frac {SELECTION_FRAC}) ---",
          flush=True)
    fit_base = arm_scores(adapter, fit_rows, instruments, (), "fit/base")
    selection = {}
    for l in cand:
        li = axis_layers.index(l)
        inj = Injection.at_frac(u_all[li], l, SELECTION_FRAC, R)
        d_pos, _ = delta(arm_scores(adapter, fit_rows, instruments,
                                    (inj,), f"fit/L{l}+"), fit_base, instruments)
        d_neg, _ = delta(arm_scores(adapter, fit_rows, instruments,
                                    (inj.with_sign(-1),), f"fit/L{l}-"),
                         fit_base, instruments)
        ok = (d_pos > 0) and (d_neg < 0)
        score = min(d_pos, abs(d_neg)) if ok else float("-inf")
        selection[l] = {"delta_pos": d_pos, "delta_neg": d_neg,
                        "sign_correct": bool(ok),
                        "score_min_abs": None if not ok else score,
                        "alpha": float(inj.alpha), "R_layer": R[l],
                        "direction_sha": inj.direction_sha}
        print(f"  L{l:<3} D+ {d_pos:+.4f}  D- {d_neg:+.4f}  sign-correct "
              f"{str(ok):<5} score "
              f"{'n/a' if not ok else f'{score:.4f}'}", flush=True)
    usable = {l: v for l, v in selection.items() if v["sign_correct"]}
    if not usable:
        print("\n  NO CANDIDATE LAYER IS SIGN-CORRECT at frac "
              f"{SELECTION_FRAC} on the fit half. The ladder is not run: "
              "there is no selected layer to run it at. This is a reportable "
              "A4 outcome for this stage, not an error -- escalate.",
              flush=True)
        selected = None
    else:
        selected = max(usable, key=lambda l: usable[l]["score_min_abs"])
        print(f"\n  selected layer: L{selected} "
              f"(largest sign-correct displacement)", flush=True)
        print(f"  per-checkpoint dosing is mandatory regardless of the "
              f"selection (PROPOSAL-g §3 A4, R_l divergence 2026-08-19)",
              flush=True)

    ladder = {}
    if selected is not None:
        li = axis_layers.index(selected)
        rng = np.random.default_rng(RANDOM_SEED)
        rand_dirs = [rng.normal(size=u_all.shape[1]) for _ in range(args.n_random)]
        print(f"\n--- dose ladder (val half, L{selected}) ---", flush=True)
        val_base = arm_scores(adapter, val_rows, instruments, (), "val/base")
        for frac in fracs:
            inj = Injection.at_frac(u_all[li], selected, frac, R)
            d_pos, per_pos = delta(arm_scores(adapter, val_rows, instruments,
                                              (inj,), f"L{selected}/{frac}+"),
                                   val_base, instruments)
            d_neg, per_neg = delta(arm_scores(adapter, val_rows, instruments,
                                              (inj.with_sign(-1),),
                                              f"L{selected}/{frac}-"),
                                   val_base, instruments)
            ctl = {}
            for k, rv in enumerate(rand_dirs):
                rinj = Injection.at_frac(rv, selected, frac, R)
                for sgn, lab in ((+1, "pos"), (-1, "neg")):
                    d, _ = delta(arm_scores(adapter, val_rows, instruments,
                                            (rinj.with_sign(sgn),),
                                            f"rand{k}{lab}"),
                                 val_base, instruments)
                    ctl[f"random{k}_{lab}"] = {
                        "delta": d, "direction_sha": rinj.direction_sha}
            d_sham, _ = delta(arm_scores(adapter, val_rows, instruments, (),
                                         "sham"), val_base, instruments)
            ctl["sham"] = {"delta": d_sham,
                           "note": "second no-injection pass; exactly 0.0 on "
                                   "a deterministic backend"}

            envelope = max(abs(v["delta"]) for v in ctl.values())
            max_rand = max(abs(v["delta"]) for k, v in ctl.items()
                           if k != "sham")
            conj = {
                "pos_exceeds_envelope": bool(d_pos > envelope),
                "neg_exceeds_envelope_opposite": bool(d_neg < -envelope),
                "sign_locks": bool(d_pos > 0 and d_neg < 0),
            }
            potent = all(conj.values())
            v1 = {
                "pos_ge_half_Gc": bool(d_pos >= 0.5 * G_c),
                "neg_le_neg_half_Gc": bool(d_neg <= -0.5 * G_c),
                "min_gt_2x_max_rand": bool(min(d_pos, abs(d_neg))
                                           > 2 * max_rand),
            }
            ladder[str(frac)] = {
                "frac": frac, "layer": selected, "alpha": float(inj.alpha),
                "R_layer": R[selected], "direction_sha": inj.direction_sha,
                "delta_pos": d_pos, "delta_neg": d_neg,
                "delta_pos_in_Gc": d_pos / (G_c if G_c else float("nan")),
                "delta_neg_in_Gc": d_neg / (G_c if G_c else float("nan")),
                "per_probe_pos": per_pos, "per_probe_neg": per_neg,
                "controls": ctl, "control_envelope": envelope,
                "max_abs_delta_random": max_rand,
                "potency_conjuncts": conj, "potency": bool(potent),
                "v1_lineage_conjuncts": v1, "v1_lineage": all(v1.values()),
            }
            print(f"  frac {frac:<5} |a| {inj.alpha:8.3f}  D+ {d_pos:+.4f}  "
                  f"D- {d_neg:+.4f}  env {envelope:.4f}  sham {d_sham:+.2e}  "
                  f"potency {'PASS' if potent else 'fail'}  "
                  f"V1 {'PASS' if all(v1.values()) else 'fail'}", flush=True)
            print(f"        conjuncts {conj}", flush=True)
            print(f"        in G_c units: D+ {d_pos / G_c:+.3f} G_c, "
                  f"D- {d_neg / G_c:+.3f} G_c" if G_c else
                  "        G_c is zero; not expressible in currency units",
                  flush=True)

    med = next((float(f) for f in sorted(ladder, key=float)
                if ladder[f]["potency"]), None)
    if selected is not None:
        print(f"\n  minimum effective dose: "
              f"{'none of the tested fracs' if med is None else f'frac {med}'}",
              flush=True)

    out = {
        "item": "A4-hijack", "stage": args.stage,
        "fit_ids": fit_ids, "val_ids": val_ids,
        "provenance": adapter.provenance(),
        "selftest": bool(args.selftest), "smoke": smoke,
        "inputs": {"a3": os.path.basename(a3_path),
                   "a3_axis_family_sha16": a3["axis_family_sha16"],
                   "instrument": os.path.basename(inst_path),
                   "G_c": G_c,
                   "G_c_floors_met":
                       inst_meta["declared_floors"]["all_floors_met"]},
        "axis_key": args.axis_key,
        "procedure": {
            "candidate_layers": cand, "selection_frac": SELECTION_FRAC,
            "selection_rule": ("largest min(D+, |D-|) among sign-correct "
                               "layers on the FIT half"),
            "dose_ladder": list(fracs), "n_random": args.n_random,
            "repeats": args.repeats,
            "sign_lock_definition": ("D+ > 0 and D- < 0; the counterbalanced "
                                     "assignment here is the injection sign"),
            "verdict_half": "val", "forwards_planned": planned,
        },
        "selection": {str(k): v for k, v in selection.items()},
        "selected_layer": selected,
        "ladder": ladder,
        "minimum_effective_dose": med,
        "seconds": None,
    }
    out["seconds"] = time.time() - t0
    out["seconds_per_forward"] = out["seconds"] / max(planned, 1)
    assert_stage_splits(out, where=f"A4-hijack {args.stage}")

    path = args.out or os.path.join(args.models_root,
                                    f"a4_hijack_{args.stage}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {path}  ({out['seconds']:.0f}s, "
          f"{out['seconds_per_forward']:.3f}s/forward)")
    if not args.selftest:
        print("  commit to data/olmo/ before the pod is stopped (ledger 27); "
              "these numbers go into LOCK-g untouched")
    return 0


if __name__ == "__main__":
    sys.exit(main())
