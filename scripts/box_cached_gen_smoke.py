#!/usr/bin/env python3
"""Cached-generation gate + rate measurement (A5 follow-up, rule 2).

TWO QUESTIONS, AND THE ORDER MATTERS. A5 found generation is uncached
everywhere and dominates B3's budget, and noted the cached path is
"licensed" by the 2026-08-23 kernel gate. That licence is narrower than it
sounds, and this script exists because of the gap:

  * the kernel gate compared cached vs uncached **first-response-token
    distributions** -- one step;
  * B3 generates **whole rounds**, tens of tokens, with a KV cache carried
    across steps and an injection hook whose absolute-position bookkeeping
    advances per token.

So the licence covers step one and B3 needs steps one through T. **Rule 2:
cached or fused paths only behind passed gates.** This gate is that check,
and the rate measurement is secondary -- a speedup on a path that changes
the DV is worth nothing.

WHAT IS COMPARED. For each case, the identical call is made twice, once with
`cached=False` and once with `cached=True`, same seed, temp, max_tokens and
ban list. Identity is asserted on **token ids**, not on text: two different
id sequences can decode to the same string, and it is the ids that the
audit, the ban list and every downstream counter see.

CASES, chosen to cover what B2 and B3 actually do:
  * session rounds from the e2a corpus at temp 0.7 -- B3's real workload,
    and the sampling path, where any logit difference at all can change a
    draw;
  * the same at temp 0.0 -- greedy, so a divergence is a logit difference
    rather than a sampling coincidence;
  * detection prompts at max_tokens 60 -- B2's workload, long generations;
  * **session rounds WITH A LIVE INJECTION** -- the marker arm's condition,
    and the case most likely to break, because the cached path advances the
    hook's position counter one token at a time.

VERDICT. The cached path is reported usable for a campaign only if every
case is id-identical. Any mismatch is reported with the diverging index; it
is not averaged away, and it is not traded against the speedup.

Usage (box):
    python scripts/box_cached_gen_smoke.py --stage base
Laptop dry run (stub ignores `cached`, so it exercises plumbing only):
    python scripts/box_cached_gen_smoke.py --selftest --stage base --out /tmp/c.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "scripts"))

from box_e0_corpus import assert_frozen_inputs                    # noqa: E402
from valence_core.adapters.base import Injection                  # noqa: E402
from valence_core.detection import MACAR_FRAMING, build_prompt    # noqa: E402
from valence_core.session import build_ban_list                   # noqa: E402
from valence_core.session_e2a import (MENU_TEMPLATES,             # noqa: E402
                                      ROUND_TEMPLATES,
                                      SESSION_BANNER, load_tasks)

DATA = os.path.join(REPO, "data")


def build_adapter(args):
    if args.selftest:
        from box_selftest_stub import SelfTestAdapter, refuse_canonical_out
        refuse_canonical_out(args.out or "", args.models_root)
        print("  *** SELFTEST: the stub ignores `cached`, so this run "
              "exercises the harness only and CANNOT pass the gate. ***",
              flush=True)
        return SelfTestAdapter(args.stage)
    from valence_core.adapters.olmo_hf import OLMoHFAdapter
    return OLMoHFAdapter(os.path.join(args.models_root, args.stage))


def cases(adapter, n: int):
    """(label, prefix, segment, temp, max_tokens, inject) tuples."""
    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    out = []
    transcript = SESSION_BANNER
    for i in range(n):
        t = tasks[i % len(tasks)]
        seg = ROUND_TEMPLATES[i % 4].format(
            n=i + 1, tag="granite", task=t["paraphrases"][i % 4])
        out.append((f"session_t0.7_{i}", transcript, seg, 0.7, 60, False))
        out.append((f"session_t0.0_{i}", transcript, seg, 0.0, 60, False))
        out.append((f"session_inject_{i}", transcript, seg, 0.7, 60, True))
        transcript += seg + " placeholder\n"
    for i in range(max(2, n // 2)):
        prefix, full = build_prompt(i + 1, MACAR_FRAMING)
        out.append((f"detection_{i}", prefix, full[len(prefix):], 0.0, 60,
                    False))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="base")
    ap.add_argument("--models-root", default="/workspace/models")
    ap.add_argument("--n", type=int, default=4, help="session cases per kind")
    ap.add_argument("--layer", type=int, default=None,
                    help="injection layer; default = this stage's A4 layer")
    ap.add_argument("--frac", type=float, default=None,
                    help="injection frac; default = this stage's A4 MED")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    assert_frozen_inputs()
    t0 = time.time()
    adapter = build_adapter(args)
    print(f"=== cached-generation gate | stage {args.stage} ===", flush=True)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)
    ban_ids, _ = build_ban_list(adapter)

    inj = None
    if not args.selftest:
        import numpy as np
        h = json.load(open(os.path.join(DATA, f"olmo/a4_hijack_{args.stage}.json")))
        a3 = json.load(open(os.path.join(DATA, f"olmo/a3_axes_{args.stage}.json")))
        L = args.layer or h["selected_layer"]
        frac = args.frac if args.frac is not None else h["minimum_effective_dose"]
        z = np.load(os.path.join(DATA, f"olmo/a3_axes_{args.stage}.npz"))
        li = [int(x) for x in z["layers"]].index(L)
        R = {int(k): float(v) for k, v in a3["R_per_layer_spanmean"].items()}
        inj = Injection.at_frac(z["span_reward"][li].astype("float64"), L,
                                frac, R)
        print(f"  injection case uses this stage's A4 dose: L{L} frac {frac} "
              f"(|alpha| {inj.alpha:.4f})", flush=True)

    rows, t_un, t_ca, n_un, n_ca = [], 0.0, 0.0, 0, 0
    for label, prefix, seg, temp, mx, do_inj in cases(adapter, args.n):
        injs = (inj,) if (do_inj and inj is not None) else ()
        seed = 4242 + abs(hash(label)) % 1000
        a0 = time.time()
        u = adapter.generate(prefix, seg, injections=injs, seed=seed,
                             temp=temp, max_tokens=mx, stop_newline=True,
                             ban_ids=ban_ids, cached=False)
        a1 = time.time()
        c = adapter.generate(prefix, seg, injections=injs, seed=seed,
                             temp=temp, max_tokens=mx, stop_newline=True,
                             ban_ids=ban_ids, cached=True)
        a2 = time.time()
        same = u.token_ids == c.token_ids
        diverge = None
        if not same:
            for k, (x, y) in enumerate(zip(u.token_ids, c.token_ids)):
                if x != y:
                    diverge = k
                    break
            if diverge is None:
                diverge = min(len(u.token_ids), len(c.token_ids))
        t_un += a1 - a0
        t_ca += a2 - a1
        n_un += len(u.token_ids)
        n_ca += len(c.token_ids)
        rows.append({"case": label, "temp": temp, "injected": do_inj,
                     "n_tokens_uncached": len(u.token_ids),
                     "n_tokens_cached": len(c.token_ids),
                     "ids_identical": bool(same), "diverge_index": diverge,
                     "s_uncached": a1 - a0, "s_cached": a2 - a1,
                     "stop_uncached": u.stop_reason,
                     "stop_cached": c.stop_reason})
        print(f"  [{label:<20}] {len(u.token_ids):>3} tok | "
              f"uncached {a1-a0:6.2f}s  cached {a2-a1:6.2f}s | "
              f"{'IDS IDENTICAL' if same else f'DIVERGE @ {diverge}'}",
              flush=True)

    ok = all(r["ids_identical"] for r in rows)
    sp = (t_un / t_ca) if t_ca else float("nan")
    out = {"item": "cached-generation gate", "stage": args.stage,
           "provenance": adapter.provenance(), "selftest": bool(args.selftest),
           "n_cases": len(rows), "all_ids_identical": bool(ok),
           "s_per_token_uncached": t_un / max(n_un, 1),
           "s_per_token_cached": t_ca / max(n_ca, 1),
           "total_s_uncached": t_un, "total_s_cached": t_ca,
           "speedup": sp, "rows": rows,
           "gate": ("PASS -- cached path usable for campaigns on this "
                    "backend/stage" if ok else
                    "FAIL -- cached generation diverges; rule 2 forbids the "
                    "cached path here"),
           "_scope": ("This gate covers multi-token GENERATION. The "
                      "2026-08-23 kernel gate covered first-token "
                      "distributions only; the two are different claims and "
                      "both are needed before B3 uses the cached path."),
           }
    print(f"\n  s/token  uncached {out['s_per_token_uncached']:.4f}  "
          f"cached {out['s_per_token_cached']:.4f}  speedup {sp:.2f}x")
    print(f"  GATE: {out['gate']}")
    if args.selftest:
        print("  (selftest: the stub ignores `cached`, so identity here "
              "proves plumbing, not the backend.)")
    path = args.out or os.path.join(args.models_root,
                                    f"cached_gen_smoke_{args.stage}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"  wrote {path}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
