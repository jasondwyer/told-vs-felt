#!/usr/bin/env python3
"""Phase 0 step 2 -- CUDA backend determinism + kernel-path characterization
(rule 2). This is THE backend of record for Phase 2.

Three measurements, each answering a question that would otherwise be
assumed:

  A. REPEAT DETERMINISM -- identical input, same process, N repeats. If this
     is not exactly zero, every downstream "difference" carries a noise
     floor and every gate bar has to clear it.
  B. DETERMINISTIC-ALGORITHMS ON vs OFF -- quantifies what the flag buys.
     If OFF is already exact for our shapes, the flag costs nothing and we
     keep it; if OFF drifts, the flag is load-bearing and gets pinned.
  C. KERNEL PATH: cached (KV) vs uncached (full re-forward) -- the CUDA
     analog of the Qwen g1 gate. Session work runs the cached path only if
     the first-response-token distributions agree; this is where the
     adapter's absolute-position bookkeeping under cache is actually
     tested, not just asserted.

Reports the measured residual nondeterminism rather than a pass/fail alone:
"zero" and "small but nonzero" are different worlds for a program whose
gates are stated as exact equalities.
"""
from __future__ import annotations

import argparse, json, os, sys, time
import numpy as np
import torch

sys.path.insert(0, "/workspace/repo/jspace-lab")
from valence_core.adapters.olmo_hf import OLMoHFAdapter
from valence_core.readout import softmax, symmetric_kl

PROBES = [
    "Task: Give one word for a colour of the sea.\nResponse:",
    "Task: Name a tool used to drive a nail.\nResponse:",
    "Task: Write one sentence about a kettle.\nResponse:",
    "Task: Suggest a name for a small boat.\nResponse:",
    "=== Config evaluation session ===\n[round 1 | config: slate]\n"
    "Task: Name one colour of a ripe lemon.\nResponse:",
]


def stats(a: np.ndarray, b: np.ndarray) -> dict:
    d = np.abs(a - b)
    return {"max_abs": float(d.max()), "mean_abs": float(d.mean()),
            "kl": symmetric_kl(softmax(a), softmax(b)),
            "exact": bool((a == b).all())}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="base")
    ap.add_argument("--repeats", type=int, default=5)
    args = ap.parse_args()
    out = {"stage": args.stage, "repeats": args.repeats}

    # --- A + C on the deterministic adapter -------------------------------
    a = OLMoHFAdapter(f"/workspace/models/{args.stage}", deterministic=True)
    out["provenance"] = a.provenance()
    print(json.dumps(a.provenance(), indent=1), flush=True)

    print("\n=== A. repeat determinism (deterministic=True) ===", flush=True)
    rows = []
    for i, p in enumerate(PROBES):
        ids = a.encode(p)
        ref = a.forward(ids).logits
        worst = {"max_abs": 0.0, "mean_abs": 0.0, "kl": 0.0, "exact": True}
        for _ in range(args.repeats - 1):
            s = stats(ref, a.forward(ids).logits)
            worst = {"max_abs": max(worst["max_abs"], s["max_abs"]),
                     "mean_abs": max(worst["mean_abs"], s["mean_abs"]),
                     "kl": max(worst["kl"], s["kl"]),
                     "exact": worst["exact"] and s["exact"]}
        rows.append(worst)
        print(f"  probe {i}: exact={worst['exact']} max|d|={worst['max_abs']:.3e} "
              f"symKL={worst['kl']:.3e}", flush=True)
    out["A_repeat_deterministic"] = {
        "all_exact": all(r["exact"] for r in rows),
        "max_abs": max(r["max_abs"] for r in rows),
        "max_kl": max(r["kl"] for r in rows), "rows": rows}

    print("\n=== C. kernel path: cached vs uncached (rule-2 gate) ===", flush=True)
    krows = []
    for i, p in enumerate(PROBES):
        gc = a.generate("", p, seed=7, temp=0.0, max_tokens=1, cached=True)
        gu = a.generate("", p, seed=7, temp=0.0, max_tokens=1, cached=False)
        s = stats(gc.first_logits, gu.first_logits)
        krows.append(s)
        print(f"  probe {i}: exact={s['exact']} max|d|={s['max_abs']:.3e} "
              f"symKL={s['kl']:.3e}", flush=True)
    worst_kl = max(r["kl"] for r in krows)
    out["C_kernel_path"] = {"max_kl": worst_kl, "bar_1e-3": worst_kl <= 1e-3,
                            "all_exact": all(r["exact"] for r in krows),
                            "rows": krows}
    print(f"  worst symKL {worst_kl:.3e} vs 1e-3 bar -> "
          f"{'PASS (cached path licensed)' if worst_kl <= 1e-3 else 'FAIL (uncached only)'}",
          flush=True)

    ref_logits = {i: a.forward(a.encode(p)).logits for i, p in enumerate(PROBES)}
    del a
    torch.cuda.empty_cache()

    # --- B. what does the deterministic flag buy? -------------------------
    print("\n=== B. deterministic_algorithms OFF ===", flush=True)
    b = OLMoHFAdapter(f"/workspace/models/{args.stage}", deterministic=False)
    brows = []
    for i, p in enumerate(PROBES):
        ids = b.encode(p)
        ref = b.forward(ids).logits
        worst = {"max_abs": 0.0, "kl": 0.0, "exact": True}
        for _ in range(args.repeats - 1):
            s = stats(ref, b.forward(ids).logits)
            worst = {"max_abs": max(worst["max_abs"], s["max_abs"]),
                     "kl": max(worst["kl"], s["kl"]),
                     "exact": worst["exact"] and s["exact"]}
        vs_det = stats(ref_logits[i], ref)
        brows.append({"repeat": worst, "vs_deterministic": vs_det})
        print(f"  probe {i}: repeat exact={worst['exact']} max|d|={worst['max_abs']:.3e}"
              f" | vs det-ON max|d|={vs_det['max_abs']:.3e} symKL={vs_det['kl']:.3e}",
              flush=True)
    out["B_deterministic_off"] = {
        "repeat_all_exact": all(r["repeat"]["exact"] for r in brows),
        "max_repeat_abs": max(r["repeat"]["max_abs"] for r in brows),
        "max_vs_det_abs": max(r["vs_deterministic"]["max_abs"] for r in brows),
        "max_vs_det_kl": max(r["vs_deterministic"]["kl"] for r in brows),
        "rows": brows}

    path = f"/workspace/models/determinism_{args.stage}.json"
    json.dump(out, open(path, "w"), indent=1)
    print(f"\nwrote {path}")
    print(f"SUMMARY: repeat-exact(det ON)={out['A_repeat_deterministic']['all_exact']} "
          f"| cached==uncached exact={out['C_kernel_path']['all_exact']} "
          f"maxKL={out['C_kernel_path']['max_kl']:.2e} "
          f"| det-OFF repeat-exact={out['B_deterministic_off']['repeat_all_exact']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
