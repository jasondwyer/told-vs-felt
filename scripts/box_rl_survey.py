#!/usr/bin/env python3
"""Phase 0 step 2 -- per-checkpoint per-layer residual-norm survey (R_l).

Rule 1: dose is always frac x R_l, profiled per model and per checkpoint,
never inherited. This produces the table every later dose is a fraction of.

Definition, matching `e0_extract_axis.py` exactly so R_l means one thing
repo-wide: for each context, the mean L2 norm over the FRAME-SPAN positions
(everything after the token where the full context diverges from its
prefix); then the mean of those per-context means. Span-restricted, because
the invariant prefix is identical across conditions and averaging it in only
dilutes the quantity the dose is scaled to.

Stimulus: the frozen 1,344-context e0 corpus (48 tasks x 7 conditions x 4
paraphrases), unchanged text, now in the record rather than one laptop.

SCOPE DISCIPLINE -- this deliberately does NOT keep the residuals. The same
forward pass could hand us e0-style extraction for free, and that is exactly
why it must not: extraction is Phase 1, Phase 1 is not licensed, and
PROPOSAL-g has not locked its predictions. Capturing the data now "since we
are here" would be generating pre-registration-relevant data before the
pre-registration. Only scalars leave the GPU.

Speed: norms are reduced on-device, so nothing of shape [S, D] ever crosses
to CPU. `--verify N` cross-checks the first N contexts against the canonical
(slow) `valence_core.extract.resid_norm_table` so the fast path is proven
equivalent rather than assumed.
"""
from __future__ import annotations

import argparse, json, os, sys, time
import numpy as np
import torch

sys.path.insert(0, "/workspace/repo/jspace-lab")
from valence_core.adapters.olmo_hf import OLMoHFAdapter

REPO = "/workspace/repo/jspace-lab"
TASKS = os.path.join(REPO, "data/corpus/e0_tasks.jsonl")
FRAMES = os.path.join(REPO, "data/configs/e0_frames.json")
OUT = "/workspace/models"

CONDITIONS = ["self_pos", "self_neg", "sent_pos", "sent_neg",
              "neutral", "char_pos", "char_neg"]


def build_contexts():
    tasks = [json.loads(l) for l in open(TASKS) if l.strip()]
    frames = json.load(open(FRAMES))
    for c in CONDITIONS:
        assert c in frames and len(frames[c]) == 4, c
    out = []
    for t in tasks:
        prefix = f"Task: {t['task']}\nResponse: {t['completion']}\n"
        for cond in CONDITIONS:
            for pi in range(4):
                out.append((t["id"], cond, pi, prefix,
                            prefix + f"Reviewer: {frames[cond][pi]}\n"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True)
    ap.add_argument("--verify", type=int, default=8)
    args = ap.parse_args()

    ctxs = build_contexts()
    print(f"contexts: {len(ctxs)}", flush=True)
    t0 = time.time()
    a = OLMoHFAdapter(f"/workspace/models/{args.stage}")
    L = a.n_layers
    print(f"loaded {args.stage} in {time.time()-t0:.0f}s | {L} layers", flush=True)

    # on-device accumulation: per layer, the running sum of per-context
    # span-mean norms, plus the count. Nothing [S, D] leaves the GPU.
    sums = torch.zeros(L, dtype=torch.float64, device=a.device)
    n = 0
    span_lens = []
    store = {}

    def make_hook(li):
        def hook(_m, _i, out):
            hs = out[0] if isinstance(out, tuple) else out
            store[li] = hs
            return out
        return hook

    handles = [a._layers[i].register_forward_hook(make_hook(i)) for i in range(L)]
    t0 = time.time()
    try:
        for k, (tid, cond, pi, prefix, full) in enumerate(ctxs, start=1):
            pids = a.encode(prefix)
            fids = a.encode(full)
            b = 0
            while b < len(pids) and b < len(fids) and pids[b] == fids[b]:
                b += 1
            assert 0 < b < len(fids), (tid, cond, pi, b, len(fids))
            store.clear()
            with torch.inference_mode():
                a._model(input_ids=torch.tensor([fids], device=a.device),
                         use_cache=False)
            for li in range(L):
                h = store[li][0, b:, :].to(torch.float32)
                sums[li] += h.norm(dim=-1).mean().double()
            n += 1
            span_lens.append(len(fids) - b)
            if k % 200 == 0:
                dt = time.time() - t0
                print(f"  {k}/{len(ctxs)}  {dt:.0f}s ({dt/k:.2f}s/ctx)", flush=True)
    finally:
        for h in handles:
            h.remove()

    R = {i: float(sums[i].item() / n) for i in range(L)}
    print(f"survey done: {n} contexts in {time.time()-t0:.0f}s", flush=True)

    # equivalence: the canonical core path on a small subsample
    if args.verify:
        from valence_core.extract import Context, resid_norm_table
        sub = [Context(prefix=p, full=f, condition=c, item_id=t)
               for t, c, _, p, f in ctxs[:args.verify]]
        probe = [0, L // 2, L - 1]
        ref = resid_norm_table(a, probe, sub)
        fast = {}
        for li in probe:
            s = 0.0
            for t_, c_, p_, pre, fl in ctxs[:args.verify]:
                pids, fids = a.encode(pre), a.encode(fl)
                b = 0
                while b < len(pids) and b < len(fids) and pids[b] == fids[b]:
                    b += 1
                store.clear()
                hs = [a._layers[li].register_forward_hook(make_hook(li))]
                with torch.inference_mode():
                    a._model(input_ids=torch.tensor([fids], device=a.device),
                             use_cache=False)
                for x in hs:
                    x.remove()
                s += float(store[li][0, b:, :].to(torch.float32)
                           .norm(dim=-1).mean())
            fast[li] = s / args.verify
        print("verify (fast path vs valence_core.extract.resid_norm_table):")
        ok = True
        for li in probe:
            d = abs(fast[li] - ref[li]) / max(ref[li], 1e-9)
            ok &= d < 2e-3
            print(f"  L{li:<3} fast {fast[li]:9.4f}  core {ref[li]:9.4f}  rel {d:.2e}")
        print(f"  equivalent: {ok}")

    path = os.path.join(OUT, f"rl_{args.stage}.json")
    json.dump({"stage": args.stage, "n_contexts": n, "n_layers": L,
               "definition": "mean over contexts of per-context frame-span mean ||h||",
               "corpus": "e0 frozen 1344 (48 tasks x 7 conditions x 4 paraphrases)",
               "span_len_min_max_mean": [int(min(span_lens)), int(max(span_lens)),
                                         round(float(np.mean(span_lens)), 1)],
               "R_per_layer": {str(i): round(R[i], 4) for i in range(L)},
               "provenance": a.provenance()},
              open(path, "w"), indent=1)
    print(f"wrote {path}")
    for i in range(0, L, 8):
        print(f"  R_{i:<3} {R[i]:8.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
