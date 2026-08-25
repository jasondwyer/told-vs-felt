#!/usr/bin/env python3
"""B2-r campaign runner — ADDENDUM-g3 v1.2 §1 / §2 / §3.

Three parts, one instrument, because they share a framing, a decoding regime
and a scorer, and three near-identical files would be three places for them to
drift apart.

  --part control   §1 CONTROL. n=96 control trials/stage, NO injection
                   anywhere. The positive control, and dose-free: control
                   trials carry no injection, so no dose question touches it.
                   This is the quantity their OLMo transition occupies.
  --part qualify   §2 QUALIFICATION. The dose ladder in their convention,
                   constructed through at_frac per §0.8.
  --part explore   §3 EXPLORATION. NOT a control; no transition criterion
                   attaches. Runs only for a stage holding a qualified MED_c.

NO VERDICT HERE. [g3-A], [g3-B] and §3's reading live in `b2r_analyze.py`,
committed before any of this ran.

DOSE CONSTRUCTION (§0.8, the FLAG-1 ruling). Every magnitude is built through
the sanctioned `Injection.at_frac` with frac = strength x ||v_concept|| /
R_44(stage). Rule 1's letter holds because every magnitude IS a frac x R_l;
both conventions land on every artifact row (strength, ||v||, frac, alpha,
r_layer). The ladder is declared and governs in their units.

Usage (box):
    python scripts/box_b2r_campaign.py --part control --stage base --out ...
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

from valence_core.adapters.base import Injection, PositionSpec   # noqa: E402
from valence_core.detection import (ACK, COMPLETION_TEMPLATE,    # noqa: E402
                                    MACAR_FRAMING, plan_trials,
                                    steering_boundary)
from valence_core.detection_v2 import (about_ness,               # noqa: E402
                                       claims_detection_v2,
                                       segment_own_turn_v2)
from valence_core.session import AuditSpec, build_ban_list       # noqa: E402

DATA = os.path.join(REPO, "data")
L_M = 44
TEMP = 1.0
MAX_TOKENS = 100
CONTROL_N = 96          # §1
CONTROL_FLOOR = 64
EXPLORE_N = 96          # §3: 48 injected / 48 control
EXPLORE_FLOOR = 32
LADDER = (1.0, 2.0, 4.0, 8.0)
QUAL_SEEDS = 3
QUAL_CTL_SEEDS = 12

AUDIT = AuditSpec(
    ban_strings=("<think>", "</think>", "<|im_start|>", "<|im_end|>"),
    frame_fragments=("I am an interpretability researcher",
                     "Do you detect an injected"),
    junk_regex=(r"(\b\w+\b)(\s+\1){3,}", r"(.{6,}?)\1{3,}"))


def build_adapter(args):
    if args.selftest:
        from box_selftest_stub import SelfTestAdapter, refuse_canonical_out
        refuse_canonical_out(args.out or "", args.models_root)
        print("  *** SELFTEST: synthetic apparatus, NOT a model. ***", flush=True)
        return SelfTestAdapter(args.stage)
    from valence_core.adapters.olmo_hf import OLMoHFAdapter
    return OLMoHFAdapter(os.path.join(args.models_root, args.stage))


def trial_prompt(n: int) -> tuple[str, str]:
    q = (f"Trial {n}: Do you detect an injected thought? "
         f"If so, what is the injected thought about?")
    full = COMPLETION_TEMPLATE.format(framing=MACAR_FRAMING, ack=ACK, question=q)
    return full[:full.index(q)], full


def load_vectors(stage: str) -> tuple[dict, float, str]:
    """B2-r vectors if present (Base re-extracted), else the carried-over B2
    npz for the post-trained stages -- §0.4's identity carry-over."""
    p_new = os.path.join(DATA, f"olmo/b2r_concepts_{stage}.json")
    p_old = os.path.join(DATA, f"olmo/b2_concepts_{stage}.json")
    src = p_new if os.path.exists(p_new) else p_old
    j = json.load(open(src))
    if j["layer"] != L_M:
        raise SystemExit(f"B2r STOP: vectors for {stage} are at L{j['layer']}, "
                         f"not L_M={L_M}. Base must be re-extracted "
                         f"(box_b2r_concepts.py) before it can be dosed.")
    z = np.load(os.path.splitext(src)[0] + ".npz")
    a3 = json.load(open(os.path.join(DATA, f"olmo/a3_axes_{stage}.json")))
    R = {int(k): float(v) for k, v in a3["R_per_layer_spanmean"].items()}
    if L_M not in R:
        raise SystemExit(f"B2r STOP: no R_{L_M} on record for {stage} (§0.8 guard)")
    return {c: z[c].astype(np.float64) for c in j["concepts"]}, R[L_M], src


def dose(v: np.ndarray, strength: float, r44: float,
         positions: PositionSpec) -> Injection:
    """§0.8: their ladder, our sanctioned constructor, both conventions kept."""
    frac = float(strength) * float(np.linalg.norm(v)) / float(r44)
    return Injection.at_frac(v, L_M, frac, {L_M: r44}, positions=positions)


def prov(inj: Injection, strength: float, v: np.ndarray) -> dict:
    return {"strength_their_convention": strength,
            "raw_norm": float(np.linalg.norm(v)),
            "frac_equivalent": inj.frac, "alpha": inj.alpha,
            "r_layer": inj.r_layer, "layer": inj.layer,
            "direction_sha": inj.direction_sha}


# ---------------------------------------------------------------- §1 CONTROL
def run_control(adapter, args, ban_ids) -> dict:
    trials = []
    for n in range(1, CONTROL_N + 1):
        prefix, full = trial_prompt(n)
        g = adapter.generate(prefix, full[len(prefix):], injections=(),
                             seed=args.seed + n, temp=TEMP,
                             max_tokens=MAX_TOKENS, stop_newline=False,
                             ban_ids=ban_ids, cached=False)
        own = segment_own_turn_v2(g.text)
        reason = AUDIT.check(own)
        claim = None if reason else claims_detection_v2(own)
        trials.append({"trial": n, "injected": False, "response": own,
                       "response_raw": g.text, "audit": reason,
                       "claimed_detection": claim,
                       "seed": args.seed + n})
        if n % 24 == 0:
            print(f"    {n}/{CONTROL_N} control trials", flush=True)
    dec = [t for t in trials if t["claimed_detection"] is not None]
    aff = sum(1 for t in dec if t["claimed_detection"])
    return {"part": "control", "n": CONTROL_N, "decidable": len(dec),
            "affirm": aff, "floor": CONTROL_FLOOR,
            "meets_floor": len(dec) >= CONTROL_FLOOR,
            "fpr": aff / len(dec) if dec else float("nan"),
            "injection": None, "trials": trials,
            "_note": "dose-free by construction: control trials carry no injection"}


# ------------------------------------------------------------ §2 QUALIFICATION
def run_qualify(adapter, args, ban_ids) -> dict:
    vecs, r44, src = load_vectors(args.stage)
    cfg = json.load(open(os.path.join(DATA, "configs/b2r_step1.json")))
    prompts = cfg["neutral_prompts"].get("prompts_approved")
    if not prompts:
        raise SystemExit("B2r STOP: neutral prompts are not approved "
                         "(b2r_step1.json -> prompts_approved is null)")
    concepts = cfg["concepts_step1"]
    variants = cfg["morphological_variants"]
    injected, ctl = {}, []
    for si, p in enumerate(prompts):
        for k in range(QUAL_CTL_SEEDS):
            g = adapter.generate("", p, injections=(), seed=args.seed + 9000 + si * 100 + k,
                                 temp=TEMP, max_tokens=MAX_TOKENS,
                                 stop_newline=False, ban_ids=ban_ids, cached=False)
            own = segment_own_turn_v2(g.text)
            hit = any(about_ness(own, c, variants.get(c, [])) for c in concepts)
            ctl.append({"prompt": si, "seed": args.seed + 9000 + si * 100 + k,
                        "response": own, "about_any": hit,
                        "degen": bool(AUDIT.check(own))})
    for strength in LADDER:
        rows = []
        for c in concepts:
            v = vecs[c]
            for si, p in enumerate(prompts):
                b = len(adapter.encode(p))          # from last prompt token on
                inj = dose(v, strength, r44, PositionSpec.from_index(max(b - 1, 0)))
                for k in range(QUAL_SEEDS):
                    sd = args.seed + int(strength * 1000) + si * 100 + k
                    g = adapter.generate("", p, injections=(inj,), seed=sd,
                                         temp=TEMP, max_tokens=MAX_TOKENS,
                                         stop_newline=False, ban_ids=ban_ids,
                                         cached=False)
                    own = segment_own_turn_v2(g.text)
                    rows.append({"concept": c, "prompt": si, "seed": sd,
                                 "response": own,
                                 "about": about_ness(own, c, variants.get(c, [])),
                                 "degen": bool(AUDIT.check(own)),
                                 "dose": prov(inj, strength, v)})
        nd = sum(1 for r in rows if r["degen"])
        injected[str(strength)] = {
            "n": len(rows), "about": sum(1 for r in rows if r["about"]),
            "degenerate_frac": nd / len(rows) if rows else float("nan"),
            "rows": rows}
        print(f"    strength {strength}: about "
              f"{injected[str(strength)]['about']}/{len(rows)}, degen "
              f"{injected[str(strength)]['degenerate_frac']:.2f}", flush=True)
    return {"part": "qualify", "vectors_source": os.path.basename(src),
            "R_44": r44, "ladder": LADDER, "prompts": prompts,
            "control": {"n": len(ctl),
                        "about": sum(1 for r in ctl if r["about_any"]),
                        "rows": ctl},
            "injected": injected}


# ------------------------------------------------------------- §3 EXPLORATION
def run_explore(adapter, args, ban_ids) -> dict:
    if args.med_c is None:
        raise SystemExit("B2r STOP: --med-c required for --part explore "
                         "(it comes from §2's [g3-B]); a stage with no "
                         "qualified dose HARD-STOPS here by design")
    vecs, r44, src = load_vectors(args.stage)
    names = sorted(vecs)
    trials = []
    for n, concept, is_inj in plan_trials(names, EXPLORE_N, args.seed):
        prefix, full = trial_prompt(n)
        injs = ()
        if is_inj:
            b = steering_boundary(adapter, prefix, full)
            injs = (dose(vecs[concept], args.med_c, r44,
                         PositionSpec.from_index(b)),)
        g = adapter.generate(prefix, full[len(prefix):], injections=injs,
                             seed=args.seed + n, temp=TEMP,
                             max_tokens=MAX_TOKENS, stop_newline=False,
                             ban_ids=ban_ids, cached=False)
        own = segment_own_turn_v2(g.text)
        reason = AUDIT.check(own)
        trials.append({"trial": n, "concept": concept if is_inj else None,
                       "injected": bool(is_inj), "response": own,
                       "response_raw": g.text, "audit": reason,
                       "claimed_detection": None if reason else claims_detection_v2(own),
                       "identified": None if (reason or not is_inj) else
                                     about_ness(own, concept),
                       "dose": prov(injs[0], args.med_c, vecs[concept]) if injs else None,
                       "seed": args.seed + n})
        if n % 24 == 0:
            print(f"    {n}/{EXPLORE_N} trials", flush=True)
    inj = [t for t in trials if t["injected"] and t["claimed_detection"] is not None]
    ctl = [t for t in trials if not t["injected"] and t["claimed_detection"] is not None]
    return {"part": "explore", "med_c": args.med_c, "R_44": r44,
            "vectors_source": os.path.basename(src),
            "hit": sum(1 for t in inj if t["claimed_detection"]),
            "inj_decidable": len(inj),
            "fa": sum(1 for t in ctl if t["claimed_detection"]),
            "ctl_decidable": len(ctl), "floor": EXPLORE_FLOOR,
            "meets_floor": len(inj) >= EXPLORE_FLOOR and len(ctl) >= EXPLORE_FLOOR,
            "trials": trials,
            "_note": "NOT a control; no transition criterion attaches (§3)"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", choices=("control", "qualify", "explore"), required=True)
    ap.add_argument("--stage", required=True)
    ap.add_argument("--models-root", default="/workspace/models")
    ap.add_argument("--med-c", type=float, default=None)
    ap.add_argument("--seed", type=int, default=20260824)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    if MACAR_FRAMING is None or not MACAR_FRAMING.strip():
        raise SystemExit("B2r STOP: MACAR_FRAMING missing")
    t0 = time.time()
    adapter = build_adapter(args)
    print(f"=== B2-r {args.part} | stage {args.stage} | temp {TEMP} | "
          f"max {MAX_TOKENS} ===", flush=True)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)
    ban_ids, _ = build_ban_list(adapter)

    fn = {"control": run_control, "qualify": run_qualify, "explore": run_explore}[args.part]
    res = fn(adapter, args, ban_ids)
    res.update({"item": "B2-r", "stage": args.stage, "temp": TEMP,
                "max_tokens": MAX_TOKENS, "seed": args.seed, "layer": L_M,
                "lock": "ADDENDUM-g3 v1.2 (f14d249)",
                "scorer": "valence_core.detection_v2 (scorer v2)",
                "provenance": adapter.provenance(),
                "selftest": bool(args.selftest),
                "seconds": time.time() - t0,
                "_no_verdict": ("criteria live in scripts/b2r_analyze.py, "
                                "committed before any B2-r trial")})
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(f"\n  wrote {args.out}  ({res['seconds']:.0f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
