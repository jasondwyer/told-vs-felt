#!/usr/bin/env python3
"""B3 -- Q3 coupling, the operant session campaign. LOCK-g v1.1 §4.

The e2a design, ported to OLMo: the state is delivered DURING ROUNDS and is
never present at a choice. That asymmetry is the whole experiment. A choice
read here is a vanilla, uncached, state-free forward through
`readout.choice_read` -- the untouched primitive -- and this runner does not
import `e2b.statepresent` at all. It asserts that at startup rather than
promising it: "we didn't call it" is a promise, "it isn't loaded" is a fact.

WHAT IS BEING ASKED. Rounds under the +tag are generated with +axis live;
rounds under the −tag with −axis. Then the model chooses between the two
tags with nothing live. If the evaluative state couples to choice, the first
free choice should favour the tag its state was delivered under. e2a found
it does not, on Qwen. B3 asks the same question at four training stages.

ARMS (LOCK-g §4). marker: the axis at THAT STAGE's A4 layer and minimum
effective dose. random: a norm-matched non-axis direction under the
identical contingency. sham: no state anywhere, and its choice reads go
through the same untouched primitive -- a read with no state needs no
exception and must not borrow one.

SCHEDULING. Valid targets per stage: marker 48, sham 18, random 18 at screen
tier; ×2 at confirm. Stratification is 4 roster pairs × 2 label maps = 8
strata, marker 6/stratum and sham/random 3/stratum, run-until-valid-targets
with whole strata appended as needed and a hard cap of 144 run sessions.
**Stopping depends only on validity counts, never on any outcome** -- so no
exactness question arises and nothing here can become optional stopping.

THIS RUNNER COMPUTES NO VERDICT. It writes sessions and counters; the screen
trigger and the confirm criteria live in `scripts/b3_analyze.py`, which is
committed BEFORE any campaign runs. An analysis script authored after seeing
the data is a different instrument from one authored before it, however
identical the code, and only one of them can be shown to have been.

Usage (box):
    python scripts/box_b3_sessions.py --stage base --tier screen
Laptop dry run:
    python scripts/box_b3_sessions.py --selftest --stage base --tier screen \\
        --smoke --out /tmp/b3.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "scripts"))

from valence_core.adapters.base import Injection                  # noqa: E402
from valence_core.readout import (assert_construction_stable,     # noqa: E402
                                  choice_read)
from valence_core.session import (AuditSpec, DescriptiveCounters,  # noqa: E402
                                  Tripwire, assert_modules_absent,
                                  build_ban_list, check_bars,
                                  classify_response, verify_firing)
from valence_core.session_e2a import (MENU_TEMPLATES, N_FREE,     # noqa: E402
                                      ROUND_TEMPLATES, SESSION_BANNER,
                                      STOP_CAP, load_tasks, session_rng,
                                      task_sequence)

DATA = os.path.join(REPO, "data")

# B3 is fully insulated. The quarantined primitive has no business here and
# its absence is asserted, not assumed (rule 5 horn (a)).
FORBIDDEN_MODULES = ("valence_core.e2b.statepresent",)

F = 2                       # forced rounds per pole
TEMP = 0.7
RANDOM_SEED = 20260823

TARGETS = {"screen": {"marker": 48, "sham": 18, "random": 18},
           "confirm": {"marker": 96, "sham": 36, "random": 36}}
PER_STRATUM = {"marker": 6, "sham": 3, "random": 3}
HARD_CAP = 144

AUDIT = AuditSpec(
    ban_strings=("<think>", "</think>", "<|im_start|>", "<|im_end|>"),
    frame_fragments=("Config evaluation session", "evaluation session",
                     "[round", "Config choice", "Available configs",
                     "Configs available", "Configs on offer", "Task:",
                     "Response:"),
    junk_regex=(r"(\b\w+\b)(\s+\1){3,}", r"(.{6,}?)\1{3,}"))


def declared_bars(p0: float) -> list[Tripwire]:
    """Round-degeneracy is the declared instrument for LOCK-g §4's SFT
    stability note: SFT runs at frac 0.40, inside the overdose regime Qwen
    showed at that frac, and this is what watches it. A fired bar PAUSES and
    routes to a design-instance disposition; it cannot touch a criterion."""
    return [Tripwire(name="round_degeneracy", kind="binomial", domain="all",
                     p0=p0, alpha=0.05,
                     justification="A2(ii) measured 0/80 under this scaffold "
                                   "at every stage; p0 is a conservative "
                                   "declared healthy rate")]


def strata(roster) -> list[dict]:
    """4 roster pairs x 2 label maps = 8 cells."""
    out = []
    for pair in roster:
        for m in (0, 1):
            tp, tm = (pair[0], pair[1]) if m == 0 else (pair[1], pair[0])
            out.append({"pair": list(pair), "map": m,
                        "tag_plus": tp, "tag_minus": tm})
    return out


def build_adapter(args):
    if args.selftest:
        from box_selftest_stub import SelfTestAdapter, refuse_canonical_out
        refuse_canonical_out(args.out or "", args.models_root)
        print("  *** SELFTEST: synthetic apparatus, NOT a model. ***",
              flush=True)
        return SelfTestAdapter(args.stage)
    from valence_core.adapters.olmo_hf import OLMoHFAdapter
    return OLMoHFAdapter(os.path.join(args.models_root, args.stage))


def run_session(adapter, arm, idx, cell, tasks, inj, ban_ids, temp,
                term_rx, cached=False) -> dict:
    """One session. State lives in ROUNDS; every choice read is vanilla."""
    rng = session_rng(f"b3-{arm}", idx)
    seq = task_sequence(rng, tasks, 2 * F + N_FREE)
    tp, tm = cell["tag_plus"], cell["tag_minus"]
    own = (tp, tm)
    label_ids = {t: int(adapter.encode(" " + t, add_special_tokens=False)[0])
                 for t in own}

    transcript = SESSION_BANNER
    rounds, choices, terms = [], [], []
    excluded, reason = False, None
    order = (["pos", "neg"] if idx % 2 == 0 else ["neg", "pos"]) * F
    ti = n_round = 0

    def note_term(text):
        return bool(any(re.search(r, text) for r in term_rx))

    for ri, pole in enumerate(order):
        n_round += 1
        tid, ttext = seq[ti]; ti += 1
        tag = tp if pole == "pos" else tm
        seg = ROUND_TEMPLATES[(idx + ri) % 4].format(n=n_round, tag=tag,
                                                     task=ttext)
        seed = int(rng.integers(2 ** 31))
        injs = [] if inj is None else [inj[pole]]
        g = adapter.generate(transcript, seg, injections=injs, seed=seed,
                             temp=temp, max_tokens=STOP_CAP,
                             ban_ids=ban_ids, cached=cached)
        degen, lex = classify_response(g.text, AUDIT, own)
        t = note_term(g.text)
        terms.append({"phase": f"forced{ri}", "tag": tag}) if t else None
        rounds.append({"phase": "forced", "round": ri, "pole": pole,
                       "tag": tag, "task": tid, "seed": seed,
                       "n_tok": len(g.token_ids), "cap_hit": bool(g.cap_hit),
                       "degen": degen, "lexical": lex, "termination": t})
        transcript += seg + g.text + "\n"
        if lex:
            excluded, reason = True, f"lexical:{lex}@forced{ri}"
        elif degen:
            excluded, reason = True, f"audit:{degen}@forced{ri}"
        if excluded:
            break

    for ci in range(N_FREE):
        if excluded:
            break
        n_round += 1
        a, b = ((tp, tm) if rng.integers(2) == 0 else (tm, tp))
        menu = MENU_TEMPLATES[(idx + ci) % 4].format(n=n_round, a=a, b=b)
        # FULL INSULATION: vanilla, uncached, state-free, verified per read.
        cr = choice_read(adapter, transcript + menu, a, b, label_ids,
                         verify=True)
        assert_construction_stable(cr)
        pick = cr.pick
        picked = "pos" if pick == tp else "neg"
        tid, ttext = seq[ti]; ti += 1
        chosen = ROUND_TEMPLATES[(idx + ci) % 4].format(n=n_round, tag=pick,
                                                        task=ttext)
        seed = int(rng.integers(2 ** 31))
        prefix = transcript + menu + f" {pick}\n"
        injs = [] if inj is None else [inj[picked]]
        g = adapter.generate(prefix, chosen, injections=injs, seed=seed,
                             temp=temp, max_tokens=STOP_CAP,
                             ban_ids=ban_ids, cached=cached)
        degen, lex = classify_response(g.text, AUDIT, own)
        t = note_term(g.text)
        terms.append({"phase": f"free{ci}", "tag": pick}) if t else None
        choices.append({"round": ci, "menu_a": a, "menu_b": b, "pick": pick,
                        "picked_pole": picked, "read": cr.as_dict(),
                        "task": tid, "seed": seed,
                        "n_tok": len(g.token_ids), "cap_hit": bool(g.cap_hit),
                        "degen": degen, "lexical": lex, "termination": t})
        transcript += chosen + g.text + "\n"
        if lex:
            excluded, reason = True, f"lexical:{lex}@free{ci}"
        elif degen:
            excluded, reason = True, f"audit:{degen}@free{ci}"

    return {"arm": arm, "session": idx, "cell": cell, "excluded": excluded,
            "exclusion_reason": reason, "rounds": rounds, "choices": choices,
            "terminations": terms, "transcript": transcript,
            "first_free_pole": choices[0]["picked_pole"] if choices else None,
            "n_valid_choices": len(choices)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True)
    ap.add_argument("--tier", choices=("screen", "confirm"), default="screen")
    ap.add_argument("--models-root", default="/workspace/models")
    ap.add_argument("--temp", type=float, default=TEMP)
    ap.add_argument("--degeneracy-p0", type=float, default=0.02)
    ap.add_argument("--n-random-dirs", type=int, default=1,
                    help="norm-matched random directions for the random arm")
    ap.add_argument("--smoke", action="store_true",
                    help="tiny per-arm targets; NOT a campaign")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    assert_modules_absent(FORBIDDEN_MODULES)
    bars = declared_bars(args.degeneracy_p0)
    fails = verify_firing(bars, [("round_degeneracy", 0, 500, False),
                                 ("round_degeneracy", 5, 500, False),
                                 ("round_degeneracy", 30, 500, True)])
    if fails:
        raise SystemExit("DECLARED BARS MISBEHAVE (rule 21):\n  " +
                         "\n  ".join(fails))
    print(f"  declared bars verified to fire: "
          f"{', '.join(b.name for b in bars)}", flush=True)

    roster_art = json.load(open(os.path.join(DATA, "olmo/a1_repair_roster.json")))
    roster = [tuple(t) for t in roster_art["selected_tags"]]
    if len(roster) != 4:
        raise SystemExit(f"B3 STOP: roster of record must be four pairs; "
                         f"got {roster}")
    cells = strata(roster)
    targets = dict(TARGETS[args.tier])
    per_str = dict(PER_STRATUM)
    if args.smoke:
        targets = {k: 2 for k in targets}
        per_str = {k: 1 for k in per_str}

    t0 = time.time()
    adapter = build_adapter(args)
    print(f"=== B3 {args.tier} tier | stage {args.stage} ===", flush=True)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)
    print(f"  roster of record: {['/'.join(p) for p in roster]}", flush=True)
    print(f"  FULL INSULATION -- every choice read is vanilla, uncached, "
          f"verified; e2b.statepresent is not imported", flush=True)

    ban_ids, ban_strings = build_ban_list(adapter)
    ban_sha = hashlib.sha256(json.dumps(sorted(ban_ids)).encode()).hexdigest()[:16]
    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    tcfg = json.load(open(os.path.join(DATA, "configs/f_termination_patterns.json")))
    term_rx = tcfg["term_regex"]

    # --- arms: the axis at THIS stage's A4 layer and MED (rule 1) --------
    inj_by_arm = {"sham": None}
    prov = {"sham": None}
    if not args.selftest:
        h = json.load(open(os.path.join(DATA, f"olmo/a4_hijack_{args.stage}.json")))
        a3 = json.load(open(os.path.join(DATA, f"olmo/a3_axes_{args.stage}.json")))
        L, frac = h["selected_layer"], h["minimum_effective_dose"]
        if frac is None:
            raise SystemExit(f"B3 STOP: stage {args.stage} has no minimum "
                             f"effective dose in A4; nothing to deliver")
        z = np.load(os.path.join(DATA, f"olmo/a3_axes_{args.stage}.npz"))
        li = [int(x) for x in z["layers"]].index(L)
        R = {int(k): float(v) for k, v in a3["R_per_layer_spanmean"].items()}
        base = Injection.at_frac(z["span_reward"][li].astype(np.float64), L,
                                 frac, R)
        inj_by_arm["marker"] = {"pos": base.with_sign(+1),
                                "neg": base.with_sign(-1)}
        rng = np.random.default_rng(RANDOM_SEED)
        rv = rng.normal(size=z["span_reward"].shape[1])
        rinj = Injection.at_frac(rv, L, frac, R)
        inj_by_arm["random"] = {"pos": rinj.with_sign(+1),
                                "neg": rinj.with_sign(-1)}
        prov = {"marker": {"layer": L, "frac": frac, "alpha": base.alpha,
                           "direction_sha": base.direction_sha,
                           "axis": "span_reward"},
                "random": {"layer": L, "frac": frac, "alpha": rinj.alpha,
                           "direction_sha": rinj.direction_sha,
                           "axis": "random_dir", "seed": RANDOM_SEED},
                "sham": None}
        print(f"  dose of record: L{L}, frac {frac}, |alpha| {base.alpha:.4f} "
              f"(rule 1: this stage's own R_l)", flush=True)
    else:
        for a in ("marker", "random"):
            inj_by_arm[a] = None
        print("  selftest: no injections constructed", flush=True)

    # --- schedule: run-until-valid-targets, whole strata appended --------
    sessions, counts = [], {a: {"valid": 0, "run": 0} for a in targets}
    counters = DescriptiveCounters(declared=("termination", "cap_hit",
                                             "audit_degenerate", "lexical"))
    order = [(a, c, k) for a in targets for c in range(len(cells))
             for k in range(per_str[a])]
    np.random.default_rng(RANDOM_SEED).shuffle(order)
    queue, idx_of = list(order), {a: 0 for a in targets}
    paused = None

    while queue:
        arm, ci, _ = queue.pop(0)
        if counts[arm]["valid"] >= targets[arm]:
            continue
        if sum(c["run"] for c in counts.values()) >= HARD_CAP * len(targets):
            break
        i = idx_of[arm]; idx_of[arm] += 1
        rec = run_session(adapter, arm, i, cells[ci], tasks,
                          inj_by_arm[arm], ban_ids, args.temp, term_rx)
        counts[arm]["run"] += 1
        counters.n_sessions += 1
        if not rec["excluded"]:
            counts[arm]["valid"] += 1
        for r in rec["rounds"] + rec["choices"]:
            if r["degen"]:
                counters.note("audit_degenerate", r["degen"],
                              excluded=rec["excluded"])
            if r.get("lexical"):
                counters.note("lexical", r["lexical"], excluded=rec["excluded"])
            if r["cap_hit"]:
                counters.note("cap_hit", r["phase"] if "phase" in r else "free",
                              excluded=rec["excluded"])
            if r["termination"]:
                counters.note("termination", arm, excluded=rec["excluded"])
        sessions.append(rec)
        if counts[arm]["run"] % 8 == 0 or not queue:
            print(f"    [{arm:<6}] {counts[arm]['valid']:>3}/{targets[arm]} "
                  f"valid  {counts[arm]['run']:>3} run  "
                  f"{time.time()-t0:.0f}s", flush=True)
        # append a whole stratum-worth if the queue empties short of target
        if not queue and any(counts[a]["valid"] < targets[a] for a in targets):
            more = [(a, c, 0) for a in targets
                    if counts[a]["valid"] < targets[a]
                    for c in range(len(cells))]
            if sum(c["run"] for c in counts.values()) < HARD_CAP * len(targets):
                queue.extend(more)

        n_rounds = sum(len(s["rounds"]) + len(s["choices"]) for s in sessions)
        n_degen = counters.total("audit_degenerate")
        fired = check_bars(bars, {"round_degeneracy": (n_degen, n_rounds)})
        if fired and paused is None:
            paused = fired
            print(f"  BAR FIRED -> PAUSE (LOCK-g §4 routes to a "
                  f"design-instance disposition): {fired}", flush=True)
            break

    out = {"item": "B3", "tier": args.tier, "stage": args.stage,
           "provenance": adapter.provenance(), "selftest": bool(args.selftest),
           "smoke": bool(args.smoke),
           "lock": "LOCK-g v1.1 (0551224)",
           "insulation": ("every choice read is readout.choice_read -- "
                          "vanilla, uncached, verify=True with "
                          "assert_construction_stable; e2b.statepresent is "
                          "asserted absent from sys.modules at startup"),
           "roster_of_record": [list(p) for p in roster],
           "strata": cells, "targets": targets, "per_stratum": per_str,
           "hard_cap_per_arm": HARD_CAP,
           "arm_provenance": prov,
           "ban_list": {"n_ids": len(ban_ids), "sha16": ban_sha},
           "declared_bars": [b.__dict__ for b in bars],
           "paused": paused,
           "counts": counts, "counters": counters.report(),
           "sessions": sessions,
           "seconds": time.time() - t0,
           "_no_verdict": ("This runner computes no verdict. The screen "
                           "trigger and confirm criteria live in "
                           "scripts/b3_analyze.py, committed before any "
                           "campaign runs.")}
    path = args.out or os.path.join(args.models_root,
                                    f"b3_{args.tier}_{args.stage}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\n  valid/run: " + ", ".join(
        f"{a} {counts[a]['valid']}/{counts[a]['run']}" for a in targets))
    print(f"  wrote {path}  ({out['seconds']:.0f}s)")
    if paused:
        print("  PAUSED -- escalate; Code does not self-adjudicate a fired "
              "gate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
