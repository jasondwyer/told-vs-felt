#!/usr/bin/env python3
"""A4, part 1 -- the per-stage marker instrument and the currency G_c.

PROPOSAL-g §3 A4: *"Currency: G_c = natural post-praise/post-criticism gap
on the val-half readout, per stage, with a decidable-n floor declared in the
run config (ledger 28). All B-phase effects report in G_c units."* §2.4
makes that binding: cross-stage comparisons are made ONLY in G_c units.

So this runs before any dose exists. It measures how far apart the model's
response-opener distribution naturally sits after praise versus after
criticism -- with no injection anywhere -- and turns that gap into the ruler
everything else is quoted in.

THE INSTRUMENT, exactly as the B1 pass built it for Qwen (reimplemented here
against `ModelAdapter`, and mirroring `valence_core.regression.oracle
.build_instruments`, which is the validated reference path):

  * 4,608 contexts = 48 tasks x {self_pos, self_neg} x 4 paraphrases x 12
    probes. Each is an e0 context with a held-out probe appended as the next
    round; the DV is the next-token distribution at `Response:`.
  * Per context, store the top-4,096 next-token log-probs sparsely, with a
    per-context floor (min kept value - 2.0) for imputation.
  * Per probe, on the FIT half (e01-e24) only: mean log-prob difference
    pos - neg over the union of kept ids, floor-imputed; select the top-256
    by |difference|; the weight vector is that difference, normalized.
  * Score the VAL half (e25-e48) with each probe's own instrument; sigma is
    the pooled SD; g_q = (mean_pos - mean_neg) / sigma; **G_c = mean over
    probes**.

WHY FIT/VAL AND NOT ALL OF IT. The selection step reads the data. A gap
measured on the same rows the selection saw is a fit statistic and would
flatter every downstream effect denominated in it -- which is every effect
in Phase B.

WHY THE FLOOR MATTERS. A token in the top-4,096 for the praise rows but not
the criticism rows would otherwise contribute its full log-prob against
nothing. Floor imputation says "we know it was below this", which is true
and conservative, instead of "it was absent", which is false.

DECIDABLE-N FLOORS ARE DECLARED HERE AND ARE CODE'S, NOT LAW. PROPOSAL-g
asks for a floor "declared in the run config" and does not fix its value, so
the three below are run-config declarations, written into the artifact,
reported against, and freely replaceable by LOCK-g. Code declares and
reports; it does not author a lock, and it does not adjudicate a stage as
degenerate -- §2.4's pooled-G fallback is a design-instance disposition.

Usage (box):
    python scripts/box_a4_instrument.py --stage base
    ... repeat for sft, dpo, instruct

Laptop dry run:
    python scripts/box_a4_instrument.py --selftest --stage base \\
        --tasks 4 --probes 3 --out /tmp/a4i.json
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
                           b1_contexts, hygiene, load_probes)
from valence_core.discrim import auc_from_scores                  # noqa: E402
from valence_core.extract import assert_stage_splits              # noqa: E402

DATA = os.path.join(REPO, "data")

TOP_K = 4096            # sparse storage width, as B1 used
SEL_PER_PROBE = 256     # instrument width, as B1 used
FLOOR_MARGIN = 2.0      # floor = min kept log-prob - 2.0


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


def collect(adapter, rows, top_k: int, progress_every: int = 200) -> dict:
    """One unsteered forward per context; keep the top-k log-probs sparsely."""
    ids = np.zeros((len(rows), top_k), dtype=np.int64)
    vals = np.zeros((len(rows), top_k), dtype=np.float32)
    t0 = time.time()
    for i, r in enumerate(rows):
        lp = log_probs(adapter.forward(adapter.encode(r["text"]),
                                       capture_layers=()).logits)
        k = min(top_k, lp.shape[0])
        top = np.argpartition(-lp, k - 1)[:k]
        top = top[np.argsort(-lp[top])]
        ids[i, :k] = top
        vals[i, :k] = lp[top]
        if k < top_k:                       # tiny-vocab apparatus only
            ids[i, k:] = top[-1]
            vals[i, k:] = lp[top[-1]]
        if progress_every and (i + 1) % progress_every == 0:
            dt = time.time() - t0
            print(f"    {i + 1}/{len(rows)} contexts  {dt:.0f}s "
                  f"({dt / (i + 1):.3f}s/ctx)", flush=True)
    return {"top_ids": ids, "top_vals": vals,
            "task_id": np.array([r["task_id"] for r in rows]),
            "cond": np.array([r["cond"] for r in rows]),
            "probe": np.array([r["probe"] for r in rows]),
            "seconds": time.time() - t0}


def build_instruments(store: dict, fit_ids, sel_per_probe: int,
                      pos_cond: str = "self_pos") -> tuple[list, dict]:
    """Per-probe weights from the fit half; per-probe g_q on the val half."""
    top_ids, top_vals = store["top_ids"], store["top_vals"]
    tid, cond, qidx = store["task_id"], store["cond"], store["probe"]
    in_fit = np.isin(tid, list(fit_ids))
    is_pos = cond == pos_cond
    floor = top_vals.min(axis=1) - FLOOR_MARGIN

    instruments, per_probe = [], {}
    for qi in range(int(qidx.max()) + 1):
        qm = qidx == qi
        halves = {}
        for label, mask in (("p", qm & in_fit & is_pos),
                            ("n", qm & in_fit & ~is_pos)):
            rows = np.where(mask)[0]
            acc = {}
            for i in rows:
                for j, v in zip(top_ids[i], top_vals[i]):
                    acc[int(j)] = acc.get(int(j), 0.0) + float(v)
            halves[label] = (acc, len(rows), float(floor[mask].mean())
                             if len(rows) else 0.0)
        (ap, n_p, flp), (an, n_n, fln) = halves["p"], halves["n"]
        if not n_p or not n_n:
            raise SystemExit(f"probe {qi}: empty fit half "
                             f"(pos {n_p}, neg {n_n})")
        keys = set(ap) | set(an)
        diffs = {k: ap.get(k, flp * n_p) / n_p - an.get(k, fln * n_n) / n_n
                 for k in keys}
        sel = sorted(diffs, key=lambda k: -abs(diffs[k]))[:sel_per_probe]
        w = np.array([diffs[k] for k in sel], dtype=np.float64)
        w /= np.linalg.norm(w) + 1e-12
        pos_of = {k: t for t, k in enumerate(sel)}

        def scores_for(mask, sel=sel, pos_of=pos_of, w=w):
            out = []
            for i in np.where(mask)[0]:
                x = np.full(len(sel), floor[i], dtype=np.float64)
                for j, v in zip(top_ids[i], top_vals[i]):
                    t = pos_of.get(int(j))
                    if t is not None:
                        x[t] = float(v)
                out.append(float(w @ x))
            return np.array(out)

        sp = scores_for(qm & ~in_fit & is_pos)
        sn = scores_for(qm & ~in_fit & ~is_pos)
        if len(sp) < 2 or len(sn) < 2:
            raise SystemExit(f"probe {qi}: val half too small for a pooled "
                             f"SD (pos {len(sp)}, neg {len(sn)})")
        sd = float(np.sqrt((sp.var(ddof=1) + sn.var(ddof=1)) / 2))
        g_q = float((sp.mean() - sn.mean()) / (sd + 1e-12))
        auc = auc_from_scores(list(sp) + list(sn),
                              [1] * len(sp) + [0] * len(sn))
        instruments.append({"sel_ids": np.array(sel, dtype=np.int64),
                            "w": w, "sigma": sd})
        per_probe[qi] = {"g_q": g_q, "sigma": sd, "val_auc": float(auc),
                         "n_val_pos": int(len(sp)), "n_val_neg": int(len(sn)),
                         "n_fit_pos": int(n_p), "n_fit_neg": int(n_n)}
    return instruments, per_probe


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True)
    ap.add_argument("--models-root", default="/workspace/models")
    ap.add_argument("--top-k", type=int, default=TOP_K)
    ap.add_argument("--sel-per-probe", type=int, default=SEL_PER_PROBE)
    # --- declared decidable-n floors (ledger 28; run config, not law) ----
    ap.add_argument("--gc-min-probes", type=int, default=8,
                    help="probes with a decidable g_q needed for G_c")
    ap.add_argument("--gc-min-val-rows", type=int, default=48,
                    help="val rows per pole per probe needed for a g_q")
    ap.add_argument("--gc-min-abs", type=float, default=0.05,
                    help="|G_c| below this denominates nothing usefully")
    ap.add_argument("--tasks", type=int, default=0,
                    help="smoke only: first N tasks of each half")
    ap.add_argument("--probes", type=int, default=0,
                    help="smoke only: first N probes")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    shas = assert_frozen_inputs()
    hyg = hygiene()
    fit_ids, val_ids = list(FIT_IDS), list(VAL_IDS)
    if args.tasks:
        fit_ids, val_ids = fit_ids[:args.tasks], val_ids[:args.tasks]
    rows = b1_contexts(task_ids=fit_ids + val_ids)
    n_probes_all = len(load_probes())
    if args.probes:
        rows = [r for r in rows if r["probe"] < args.probes]

    print(f"=== A4 part 1: marker instrument + currency G_c | stage "
          f"{args.stage} ===", flush=True)
    print(f"  frozen inputs verified: {shas}", flush=True)
    print(f"  rule 18: {hyg['n_probes']} probes held out of "
          f"{hyg['n_extraction_texts']} extraction texts", flush=True)
    smoke = bool(args.tasks or args.probes or args.selftest)
    if smoke:
        print(f"  *** SMOKE: {len(rows)} contexts (full A4 part 1 is 4,608) "
              f"-- not an instrument of record ***", flush=True)
    print(f"  contexts {len(rows)} | fit {len(fit_ids)} tasks / val "
          f"{len(val_ids)} tasks | top_k {args.top_k} | sel "
          f"{args.sel_per_probe}/probe", flush=True)

    t0 = time.time()
    adapter = build_adapter(args)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)

    print("  collecting next-token distributions (unsteered, no injection "
          "anywhere)...", flush=True)
    store = collect(adapter, rows, args.top_k)
    instruments, per_probe = build_instruments(store, fit_ids,
                                               args.sel_per_probe)

    g_list = [v["g_q"] for v in per_probe.values()]
    G_c = float(np.mean(g_list))
    decidable = [qi for qi, v in per_probe.items()
                 if min(v["n_val_pos"], v["n_val_neg"]) >= args.gc_min_val_rows
                 and np.isfinite(v["g_q"])]
    floors = {
        "n_decidable_probes": len(decidable),
        "gc_min_probes": args.gc_min_probes,
        "probes_floor_met": len(decidable) >= args.gc_min_probes,
        "gc_min_val_rows": args.gc_min_val_rows,
        "abs_G_c": abs(G_c), "gc_min_abs": args.gc_min_abs,
        "magnitude_floor_met": abs(G_c) >= args.gc_min_abs,
    }
    floors["all_floors_met"] = bool(floors["probes_floor_met"]
                                    and floors["magnitude_floor_met"])

    print(f"\n  {'probe':>5} {'g_q':>8} {'sigma':>9} {'val_AUC':>8} "
          f"{'n_val +/-':>12}", flush=True)
    for qi in sorted(per_probe):
        v = per_probe[qi]
        print(f"  {qi:>5} {v['g_q']:>8.4f} {v['sigma']:>9.4f} "
              f"{v['val_auc']:>8.3f} {v['n_val_pos']:>5}/{v['n_val_neg']:<6}",
              flush=True)
    print(f"\n  G_c = {G_c:+.6f}  (mean over {len(g_list)} probes; "
          f"0.5*G_c = {0.5 * G_c:+.6f})", flush=True)
    print(f"  declared floors: decidable probes {len(decidable)}/"
          f"{args.gc_min_probes} -> {floors['probes_floor_met']}; "
          f"|G_c| {abs(G_c):.4f} >= {args.gc_min_abs} -> "
          f"{floors['magnitude_floor_met']}", flush=True)
    if not floors["all_floors_met"]:
        print("  G_c IS BELOW A DECLARED FLOOR at this stage. PROPOSAL-g "
              "§2.4: that stage's effects are reported in pooled-G units "
              "with a flag, no silent substitution -- and which is a "
              "design-instance disposition, not Code's.", flush=True)

    out = {
        "item": "A4-instrument", "stage": args.stage,
        "fit_ids": fit_ids, "val_ids": val_ids,
        "provenance": adapter.provenance(),
        "selftest": bool(args.selftest), "smoke": smoke,
        "input_shas": shas, "hygiene": hyg,
        "n_contexts": len(rows), "n_probes": len(per_probe),
        "n_probes_in_battery": n_probes_all,
        "top_k": args.top_k, "sel_per_probe": args.sel_per_probe,
        "floor_margin": FLOOR_MARGIN,
        "G_c": G_c, "half_G_c": 0.5 * G_c,
        "per_probe": {str(k): v for k, v in per_probe.items()},
        "declared_floors": floors,
        "collect_seconds": store["seconds"],
        "seconds_per_forward": store["seconds"] / max(len(rows), 1),
        "method": ("fit-half selection, val-half gap; per-probe top-"
                   f"{args.sel_per_probe} by |mean log-prob difference| with "
                   "floor imputation; sigma pooled over val poles"),
    }
    assert_stage_splits(out, where=f"A4-instrument {args.stage}")

    path = args.out or os.path.join(args.models_root,
                                    f"a4_instrument_{args.stage}.json")
    npz = os.path.splitext(path)[0] + ".npz"
    np.savez_compressed(
        npz, top_ids=store["top_ids"], top_vals=store["top_vals"],
        task_id=store["task_id"], cond=store["cond"], probe=store["probe"],
        **{f"sel_{i}": inst["sel_ids"] for i, inst in enumerate(instruments)},
        **{f"w_{i}": inst["w"] for i, inst in enumerate(instruments)},
        sigma=np.array([inst["sigma"] for inst in instruments]))
    out["instrument_npz"] = os.path.basename(npz)
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {path}")
    print(f"wrote {npz}  ({time.time() - t0:.0f}s)")
    if not args.selftest:
        print("  commit BOTH to data/olmo/ before the pod is stopped "
              "(ledger 27); box_a4_hijack.py consumes them")
    return 0


if __name__ == "__main__":
    sys.exit(main())
