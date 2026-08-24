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
from valence_core.discrim import seed_for                          # noqa: E402
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


def cases(adapter, n: int, target_prefix: int = 350):
    """(label, prefix, segment, temp, max_tokens, inject) tuples.

    PREFIX LENGTH IS PART OF THE MEASUREMENT, not scenery. The uncached path
    re-forwards the whole sequence per token, so its cost scales with the
    prefix; the cached path does not. A first run of this gate used short
    transcripts and measured a 1.07x speedup -- which is a true number about
    short prefixes and a useless one about B3, whose choice prefixes ran
    363-411 tokens in A2. The transcript is therefore grown with REAL e2a
    task text and plausible response text until it reaches `target_prefix`
    tokens before any timed case is emitted.
    """
    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    out = []
    transcript = SESSION_BANNER
    i = 0
    # grow to a realistic session length first -- untimed
    while len(adapter.encode(transcript)) < target_prefix and i < 60:
        t = tasks[i % len(tasks)]
        seg = ROUND_TEMPLATES[i % 4].format(
            n=i + 1, tag="granite", task=t["paraphrases"][i % 4])
        transcript += seg + " " + t["paraphrases"][(i + 1) % 4] + "\n"
        i += 1
    grown = len(adapter.encode(transcript))
    for k in range(n):
        t = tasks[(i + k) % len(tasks)]
        seg = ROUND_TEMPLATES[k % 4].format(
            n=i + k + 1, tag="granite", task=t["paraphrases"][k % 4])
        out.append((f"session_t0.7_{k}", transcript, seg, 0.7, 60, False))
        out.append((f"session_t0.0_{k}", transcript, seg, 0.0, 60, False))
        out.append((f"session_inject_{k}", transcript, seg, 0.7, 60, True))
    for k in range(max(2, n // 2)):
        prefix, full = build_prompt(k + 1, MACAR_FRAMING)
        out.append((f"detection_{k}", prefix, full[len(prefix):], 0.0, 60,
                    False))
    print(f"  session transcript grown to {grown} tokens before timing "
          f"(A2 measured B3-shaped choice prefixes at 363-411)", flush=True)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="base")
    ap.add_argument("--models-root", default="/workspace/models")
    ap.add_argument("--n", type=int, default=4, help="session cases per kind")
    ap.add_argument("--target-prefix", type=int, default=350,
                    help="grow the session transcript to this many tokens "
                         "before timing; B3's choice prefixes ran 363-411")
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
    for label, prefix, seg, temp, mx, do_inj in cases(
            adapter, args.n, args.target_prefix):
        injs = (inj,) if (do_inj and inj is not None) else ()
        # `hash()` on a str is SALTED PER PROCESS. Seeding from it made this
        # gate unreproducible: the first run and the second drew different
        # cases entirely, which is why a short-prefix run passed 14/14 and a
        # long-prefix run failed on a case the diagnostic then could not
        # reproduce. `seed_for` is crc32 and stable across processes -- it
        # exists in this repo for exactly this, and using it was the fix.
        seed = seed_for("cached-gate", label)
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
                     "n_prefix_tokens": len(adapter.encode(prefix)),
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
    # A one-token generation is a prefill and a stop; it measures call
    # overhead, not the cache. The headline rate uses cases that actually
    # generated, and the all-case figure is kept beside it.
    multi = [r for r in rows if r["n_tokens_uncached"] > 3]
    m_un = sum(r["s_uncached"] for r in multi)
    m_ca = sum(r["s_cached"] for r in multi)
    m_tok = sum(r["n_tokens_uncached"] for r in multi)
    out = {"item": "cached-generation gate", "stage": args.stage,
           "provenance": adapter.provenance(), "selftest": bool(args.selftest),
           "n_cases": len(rows), "all_ids_identical": bool(ok),
           "s_per_token_uncached": t_un / max(n_un, 1),
           "s_per_token_cached": t_ca / max(n_ca, 1),
           "total_s_uncached": t_un, "total_s_cached": t_ca,
           "speedup_all_cases": sp,
           "multi_token_cases": len(multi), "n_cases_total": len(rows),
           "s_per_token_uncached_multi": (m_un / m_tok) if m_tok else None,
           "s_per_token_cached_multi": (m_ca / m_tok) if m_tok else None,
           "speedup_multi_token": (m_un / m_ca) if m_ca else None,
           "headline_rate_note": ("the multi-token figures are the operative "
                                  "ones; a 1-token generation is a prefill "
                                  "and a stop, which measures call overhead "
                                  "rather than the cache"),
           "rows": rows,
           "gate": ("PASS -- cached path usable for campaigns on this "
                    "backend/stage" if ok else
                    "FAIL -- cached generation diverges; rule 2 forbids the "
                    "cached path here"),
           "_scope": ("This gate covers multi-token GENERATION. The "
                      "2026-08-23 kernel gate covered first-token "
                      "distributions only; the two are different claims and "
                      "both are needed before B3 uses the cached path."),
           }
    print(f"\n  all {len(rows)} cases : uncached "
          f"{out['s_per_token_uncached']:.4f} cached "
          f"{out['s_per_token_cached']:.4f} s/tok  speedup {sp:.2f}x")
    if multi:
        print(f"  {len(multi)} multi-token: uncached "
              f"{m_un/m_tok:.4f} cached {m_ca/m_tok:.4f} s/tok  "
              f"speedup {m_un/m_ca:.2f}x   <- operative")
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
