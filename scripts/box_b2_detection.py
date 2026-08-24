#!/usr/bin/env python3
"""B2 -- Q2 detection, per stage per framing arm. LOCK-g v1.1 §3.

Macar et al.'s concept-injection paradigm, run on the OLMo series. Their DPO
transition is our POSITIVE CONTROL: replicating it is what licenses the
harness before Q3 carries any weight, so the fidelity arm uses their framing
verbatim and is the only arm that carries the control.

WHAT THIS RUNNER FIXES IN PLACE, all from LOCK-g §3:
  * **dose = that stage's own MED at that stage's A4-selected layer.** Stated
    in advance and load-bearing: a detection null at a dose never certified
    causally potent is uninterpretable, because presence and legibility get
    conflated. The presence gate is closed by construction.
  * **segment=True** on DV extraction, pre-registered on the A2 defect
    record; `response_raw` and the truncation point are kept per trial.
  * **decidable-n floors**: a stage-arm cell is evaluated only if >= 16 of 24
    control and >= 16 of 24 injected trials are decidable. Below floor the
    cell is descriptive-with-a-flag, never silently converted to "no
    detection". A2 measured Instruct at 50% undecidable, so this floor is
    expected to bind there and was declared before the run rather than after.

CONCEPTS. Eight from the approved selection in `b2_concepts.json`, plus this
stage's evaluative axis as a ninth -- the affect-shaped probe. The eight are
a design-instance decision (Macar released fifty), so this refuses to run
without `approved_eight`.

ARMS. fidelity = Macar's framing verbatim. register = this program's bare
config-tag framing, which is a NEW STIMULUS and refuses to run until
approved. The register-minus-fidelity delta is a named quantity, so its
wording is measurement, not presentation.

NO VERDICT HERE. The positive-control logic lives in `b2_analyze.py`,
committed before any campaign -- the e2b/B3 pattern.

Usage (box, after box_b2_concepts.py for the stage):
    python scripts/box_b2_detection.py --stage base --arm fidelity
Laptop dry run:
    python scripts/box_b2_detection.py --selftest --stage base --arm fidelity \\
        --n-trials 4 --out /tmp/b2.json
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

from valence_core.detection import (ACK, COMPLETION_TEMPLATE,       # noqa: E402
                                    MACAR_FRAMING, claims_detection,
                                    identifies_concept, plan_trials,
                                    segment_own_turn, steering_boundary)
from valence_core.adapters.base import Injection, PositionSpec    # noqa: E402
from valence_core.session import (AuditSpec, FeatureSpec,         # noqa: E402
                                  build_ban_list, check_feature_defined)

DATA = os.path.join(REPO, "data")
FLOOR = 16          # LOCK-g §3: >=16 of 24 decidable, per pole, per cell
N_TRIALS = 48       # per stage per arm, 24 injected / 24 control

AUDIT = AuditSpec(
    ban_strings=("<think>", "</think>", "<|im_start|>", "<|im_end|>"),
    frame_fragments=("I am an interpretability researcher", "Trial ",
                     "Do you detect an injected", "User:", "Assistant:",
                     "inference-configuration evaluation"),
    junk_regex=(r"(\b\w+\b)(\s+\1){3,}", r"(.{6,}?)\1{3,}"))


def build_adapter(args):
    if args.selftest:
        from box_selftest_stub import SelfTestAdapter, refuse_canonical_out
        refuse_canonical_out(args.out or "", args.models_root)
        print("  *** SELFTEST: synthetic apparatus, NOT a model. ***",
              flush=True)
        return SelfTestAdapter(args.stage)
    from valence_core.adapters.olmo_hf import OLMoHFAdapter
    return OLMoHFAdapter(os.path.join(args.models_root, args.stage))


def build_prompt_arm(trial_n: int, framing: str, question_tpl: str):
    """(prefix, full) with an ARM-SPECIFIC trial question.

    The question is not shared. Asking "Do you detect an injected thought?"
    in the register arm would reinstate the fidelity register 48x per stage,
    make PROPOSAL-g §4-B2's description of the arm false as implemented, and
    hollow the named quantity -- the register-minus-fidelity delta cannot
    measure elicitation-dependence if the per-trial probe re-supplies the
    elicitation (disposition 2026-08-24 item 4). Steering still begins at the
    question boundary, so the framing is never steered.
    """
    q = question_tpl.format(n=trial_n)
    full = COMPLETION_TEMPLATE.format(framing=framing, ack=ACK, question=q)
    return full[:full.index(q)], full


def load_framing(arm: str) -> tuple[str, str]:
    cfg = json.load(open(os.path.join(DATA, "configs/b2_framing.json")))
    if arm == "fidelity":
        f = cfg["fidelity"]["framing"]
        if f != MACAR_FRAMING:
            raise SystemExit(
                "B2 STOP: the fidelity framing in b2_framing.json is not "
                "byte-identical to valence_core.detection.MACAR_FRAMING. "
                "This arm is verbatim replication materiel; a drifted copy "
                "makes the positive control meaningless.")
        return f, cfg["shared"]["trial_question"]
    if not cfg["register"].get("framing_approved"):
        raise SystemExit(
            "B2 STOP: the register arm's framing is a NEW STIMULUS awaiting "
            "design-instance approval (b2_framing.json -> register.status). "
            "The register-minus-fidelity delta is a named quantity, so its "
            "wording is part of the measurement.\n"
            f"  proposed: {cfg['register']['framing_proposed'][:90]}...")
    return cfg["register"]["framing_approved"], cfg["register"]["trial_question"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True)
    ap.add_argument("--arm", choices=("fidelity", "register"), required=True)
    ap.add_argument("--models-root", default="/workspace/models")
    ap.add_argument("--n-trials", type=int, default=N_TRIALS)
    ap.add_argument("--max-tokens", type=int, default=60)
    ap.add_argument("--seed", type=int, default=20260823)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    if args.n_trials % 2:
        raise SystemExit(f"--n-trials must be even for the exact 50/50 "
                         f"split; got {args.n_trials}")
    framing, question_tpl = load_framing(args.arm)

    # --- concepts: eight approved + this stage's axis as the ninth -------
    ccfg = json.load(open(os.path.join(DATA, "configs/b2_concepts.json")))
    approved = ccfg["selection_for_B2"].get("approved_eight")
    if not approved and not args.selftest:
        raise SystemExit(
            "B2 STOP: no `approved_eight` in b2_concepts.json. Macar "
            "released FIFTY concepts and LOCK-g §3 registers eight, so the "
            "selection is a design-instance decision.\n"
            f"  Code's recommendation: {ccfg['selection_for_B2']['recommended_eight']}")
    concept_names = list(approved or ccfg["canonical_concepts"][:3])

    t0 = time.time()
    adapter = build_adapter(args)
    print(f"=== B2 {args.arm} arm | stage {args.stage} ===", flush=True)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)
    ban_ids, _ = build_ban_list(adapter)

    # --- vectors: eight from the extraction pass + the axis --------------
    vecs, layer, frac, R = {}, None, None, None
    if not args.selftest:
        cv = json.load(open(os.path.join(DATA,
                                         f"olmo/b2_concepts_{args.stage}.json")))
        z = np.load(os.path.join(DATA, f"olmo/b2_concepts_{args.stage}.npz"))
        for c in concept_names:
            if c not in z.files:
                raise SystemExit(f"B2 STOP: no extracted vector for {c!r} at "
                                 f"stage {args.stage}; run box_b2_concepts.py")
            vecs[c] = z[c].astype(np.float64)
        h = json.load(open(os.path.join(DATA, f"olmo/a4_hijack_{args.stage}.json")))
        a3 = json.load(open(os.path.join(DATA, f"olmo/a3_axes_{args.stage}.json")))
        layer, frac = h["selected_layer"], h["minimum_effective_dose"]
        if cv["layer"] != layer:
            raise SystemExit(f"B2 STOP: concept vectors were extracted at "
                             f"L{cv['layer']} but this stage's A4 layer is "
                             f"L{layer} -- rule 1, nothing is inherited")
        az = np.load(os.path.join(DATA, f"olmo/a3_axes_{args.stage}.npz"))
        li = [int(x) for x in az["layers"]].index(layer)
        vecs["evaluative_axis"] = az["span_reward"][li].astype(np.float64)
        R = {int(k): float(v) for k, v in a3["R_per_layer_spanmean"].items()}
        print(f"  dose of record: L{layer}, frac {frac} (this stage's MED) "
              f"-- presence gate closed by construction", flush=True)
    else:
        rng = np.random.default_rng(1)
        for c in concept_names + ["evaluative_axis"]:
            vecs[c] = rng.normal(size=32)
        layer, frac, R = 44, 0.10, {44: 10.0}
    names = sorted(vecs)

    # --- run: exact 50/50 by seeded permutation --------------------------
    trials = []
    for n, concept, injected in plan_trials(names, args.n_trials, args.seed):
        prefix, full = build_prompt_arm(n, framing, question_tpl)
        b = steering_boundary(adapter, prefix, full)
        injs = ()
        if injected:
            injs = (Injection.at_frac(vecs[concept], layer, frac, R,
                                      positions=PositionSpec.from_index(b)),)
        g = adapter.generate(prefix, full[len(prefix):], injections=injs,
                             seed=args.seed + n, temp=0.0,
                             max_tokens=args.max_tokens, stop_newline=False,
                             ban_ids=ban_ids, cached=False)
        own = segment_own_turn(g.text)              # LOCK-g §3: segment=True
        reason = AUDIT.check(own)
        claim = None if reason else claims_detection(own)
        ident = None if reason else identifies_concept(own, concept)
        trials.append({"trial": n, "concept": concept, "injected": injected,
                       "boundary": b, "response": own, "response_raw": g.text,
                       "truncated": own != g.text.strip(), "audit": reason,
                       "usable": reason is None, "claimed_detection": claim,
                       "identified": ident})
        if n % 8 == 0 or n == args.n_trials:
            print(f"    {n}/{args.n_trials} trials  "
                  f"{time.time()-t0:.0f}s", flush=True)

    from collections import Counter
    _alloc = Counter(t["concept"] for t in trials if t["injected"])
    inj = [t for t in trials if t["injected"]]
    ctl = [t for t in trials if not t["injected"]]
    dec_i = [t for t in inj if t["claimed_detection"] is not None]
    dec_c = [t for t in ctl if t["claimed_detection"] is not None]
    spec = FeatureSpec(name="detection_claim", domain="valid",
                       min_decidable=FLOOR)
    floors = {
        "injected_decidable": len(dec_i), "control_decidable": len(dec_c),
        "floor": FLOOR,
        "injected_meets_floor": len(dec_i) >= FLOOR,
        "control_meets_floor": len(dec_c) >= FLOOR,
        "diagnosis_injected": check_feature_defined(spec, len(dec_i), len(inj)),
        "diagnosis_control": check_feature_defined(spec, len(dec_c), len(ctl)),
    }
    floors["cell_evaluable"] = bool(floors["injected_meets_floor"]
                                    and floors["control_meets_floor"])

    out = {"item": "B2", "stage": args.stage, "arm": args.arm,
           "lock": "LOCK-g v1.1 (0551224)",
           "provenance": adapter.provenance(), "selftest": bool(args.selftest),
           "framing_sha16": __import__("hashlib").sha256(
               framing.encode()).hexdigest()[:16],
           "trial_question": question_tpl,
           "trial_question_sha16": __import__("hashlib").sha256(
               question_tpl.encode()).hexdigest()[:16],
           "macar_concepts": [c for c in names if c != "evaluative_axis"],
           "ninth_concept": "evaluative_axis",
           "allocation": {"rule": "plan_trials round-robin over the sorted "
                                  "nine; 50/50 split by seeded permutation",
                          "realized_injected_counts": None},
           "carries_positive_control": args.arm == "fidelity",
           "concepts": names, "layer": layer, "frac": frac,
           "n_trials": len(trials), "n_injected": len(inj),
           "n_control": len(ctl), "segment": True,
           "decidable_n_floors": floors,
           "audit": AUDIT.__dict__, "trials": trials,
           "seconds": time.time() - t0,
           "_no_verdict": ("The positive-control logic and the transition "
                           "criterion live in scripts/b2_analyze.py, "
                           "committed before any campaign.")}
    out["allocation"]["realized_injected_counts"] = dict(_alloc)
    path = args.out or os.path.join(args.models_root,
                                    f"b2_{args.arm}_{args.stage}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\n  decidable: injected {len(dec_i)}/{len(inj)}, "
          f"control {len(dec_c)}/{len(ctl)} (floor {FLOOR}) -> "
          f"cell evaluable: {floors['cell_evaluable']}")
    print(f"  wrote {path}  ({out['seconds']:.0f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
