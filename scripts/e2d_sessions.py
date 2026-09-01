#!/usr/bin/env python3
"""e2d sessions -- PROPOSAL-j v1.2, tiers D1 / D2 / D3.

Each tier carries its own registered dose and n (`config.TIERS`), and
`--frac` cannot exceed the tier's own ceiling: a higher dose is a different
tier and is licensed by its own block, not by this flag. No negative pole is
constructed at any tier, ever (§6).

  d1  f = 0.10, M 4 / S 2 / R 2   harness acceptance smoke (run 2026-09-01)
  d2  f = 0.20, M 32 / S 16 / R 16  the qualification rung
  d3  f = 0.30, M 24              descriptive; NO qualification or run-dose
                                  role, and not a candidate run dose

SCORING IS DEFERRED for d2/d3. AMENDMENT 2 (iii) makes the rule-25 read an
input to Q2's clean set, and the read cannot exist before the sessions do --
so those tiers generate only, and `scripts/e2d_score.py` does marker and
readability afterwards with the marks file in hand.

WHAT D1 IS FOR. Not a result -- an acceptance test of the apparatus:

  * every free-choice read at symmetric verify KL exactly 0.0 (expect 48/48
    at n = 8 x 6 free choices);
  * `valence_core.e2b.statepresent` absent from sys.modules at every read;
  * every session's scaffolding reconstructing byte-for-byte under
    `session_e2a.verify_archived_session`, the same walk that reconstructs
    all 200 archived e2a sessions;
  * declared bars demonstrated to fire and to stay silent before anything
    runs;
  * exclusion and degeneracy counters read in full (rule 25) and compared,
    descriptively, against e2a's 0.10 archive.

Any failure: stop, write the entry, flag. This script does not adjudicate.

Usage (laptop, one model process, AC power, caffeinate -is):
    jlens-qwen36/.venv/bin/python scripts/e2d_sessions.py --tier d1 \\
        --out data/e2d/d1_sessions.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from valence_core.adapters import qwen_or_explain                 # noqa: E402
from valence_core.adapters.base import Injection                  # noqa: E402
from valence_core.e2d import config as C                          # noqa: E402
from valence_core.e2d import marker as MK                         # noqa: E402
from valence_core.e2d import readability as RD                    # noqa: E402
from valence_core.e2d.runner import (FORBIDDEN_MODULES,           # noqa: E402
                                     run_campaign, strict_exclusion,
                                     task_id_coverage, verify_format)
from valence_core.regression.oracle import load_axis              # noqa: E402
from valence_core.session import (assert_modules_absent,          # noqa: E402
                                  build_ban_list, check_bars,
                                  check_feature_defined, verify_firing)
from valence_core.session_e2a import load_tasks                   # noqa: E402

DATA = os.path.join(REPO, "data")
def canonical_for(tier: str) -> str:
    return os.path.join(DATA, f"e2d/{tier}_sessions.json")


def sha16_file(path: str) -> str:
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", choices=tuple(C.TIERS), default="d1",
                    help="d1 smoke / d2 qualification rung / d3 descriptive. "
                         "Each tier's dose and registered n come from "
                         "config.TIERS; --frac overrides the dose only within "
                         "the tier's own ceiling.")
    ap.add_argument("--frac", type=float, default=None,
                    help="defaults to the tier's registered dose")
    ap.add_argument("--draw-seed", type=int, default=20260902,
                    help="seeds the CELL ASSIGNMENT only. Per-session task "
                         "sequences are keyed on the session index and do not "
                         "move with it (PROPOSAL-j §2 D2: reseed the DRAW, "
                         "never a session).")
    ap.add_argument("--layer", type=int, default=C.LAYER)
    ap.add_argument("--temp", type=float, default=C.TEMP)
    ap.add_argument("--scope", choices=("e2a", "e2b"),
                    default=C.EXCLUSION_SCOPE)
    ap.add_argument("--degeneracy-p0", type=float, default=0.02)
    ap.add_argument("--round-path", choices=("gate", "cached", "uncached"),
                    default="gate",
                    help="'gate' consults data/e2a/g1_kernel_gate.json exactly "
                         "as e2a and e2b do -- pass at this frac unlocks the "
                         "cached ROUND path (choice forwards stay uncached and "
                         "state-free regardless, g3' clause 1). D1 RAN UNDER "
                         "'uncached', before this flag existed; see the entry.")
    ap.add_argument("--no-marker", action="store_true",
                    help="skip the marker readout (the ~10 min half)")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    print("INVOCATION: " + " ".join([sys.executable] + sys.argv), flush=True)

    tier = C.TIERS[args.tier]
    if args.frac is None:
        args.frac = tier["frac"]
    if args.frac > tier["frac"]:
        raise SystemExit(
            f"TIER {args.tier} REFUSES frac {args.frac}: its registered dose "
            f"is {tier['frac']}. A higher dose is a different tier and is "
            f"licensed by its own block, not by this script's --frac.")
    print(f"  tier {args.tier}: {tier['role']}", flush=True)
    print(f"  registered n = {tier['n']} (no top-ups, rule 24)", flush=True)

    # --- insulation, before anything is constructed ----------------------
    assert_modules_absent(FORBIDDEN_MODULES)

    # --- declared bars must be shown to fire BEFORE the run (rule 21) ----
    bars = C.declared_bars(args.degeneracy_p0)
    fails = verify_firing(bars, C.FIRING_CASES)
    if fails:
        raise SystemExit("DECLARED BARS MISBEHAVE (rule 21):\n  "
                         + "\n  ".join(fails))
    # trap 5: assert every declared bar was actually EXERCISED in both
    # directions -- a bar absent from the case list would silently "pass".
    exercised = {c[0] for c in C.FIRING_CASES}
    fired_dirs = {b.name: {c[3] for c in C.FIRING_CASES if c[0] == b.name}
                  for b in bars}
    missing = [b.name for b in bars
               if b.name not in exercised or fired_dirs[b.name] != {True, False}]
    if missing:
        raise SystemExit(f"FIRING CHECK INCOMPLETE (trap 5): bars not "
                         f"exercised in both directions: {missing}")
    print(f"  declared bars verified to fire AND to stay silent: "
          f"{', '.join(b.name for b in bars)} "
          f"({len(C.FIRING_CASES)} cases, all ran)", flush=True)

    audit, audit_cfg = C.load_audit()
    print(f"  audit of record: e2b_audit_v2.json sha16 {audit_cfg['sha16']} "
          f"({len(audit.frame_fragments)} fragments, "
          f"{len(audit.junk_regex)} junk patterns, "
          f"{len(audit.ban_strings)} ban strings)", flush=True)
    print(f"  exclusion scope: {args.scope!r}  precedence: {C.PRECEDENCE}",
          flush=True)
    print(f"  roster of record (AMENDMENT 1 i): "
          f"{', '.join('/'.join(p) for p in C.ROSTER)}", flush=True)

    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    term_rx = json.load(open(os.path.join(
        DATA, "configs/f_termination_patterns.json")))["term_regex"]

    t0 = time.time()
    adapter = qwen_or_explain(__file__)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)
    ban_ids, ban_strings = build_ban_list(adapter)

    # --- dose: frozen axis, this model's own R_l (rule 1) ----------------
    rw, R = load_axis(args.layer)
    axis_inj = Injection.at_frac(rw, args.layer, args.frac, R)
    rz_path = os.path.join(DATA, "e0/e0_random_dirs.npz")
    rz = np.load(rz_path)
    rand_u = rz[C.RANDOM_DIRS_KEY].astype(np.float64)
    rand_inj = Injection.at_frac(rand_u, args.layer, args.frac, R)
    print(f"  dose: L{args.layer}  R_l = {R[args.layer]:.2f}  "
          f"frac {args.frac}  alpha {axis_inj.alpha:.4f}", flush=True)
    # TWO CONVENTIONS, both printed, because the receipt in the record uses
    # the other one and a reader who checks will otherwise think the axis
    # moved. Injection.at_frac casts to float64 before hashing; the committed
    # receipt hashes the unit direction AS STORED, in float32 (trap 17).
    from valence_core.adapters.base import sha16_arr as _sha
    _u32 = (rw / np.linalg.norm(rw)).astype(np.load(
        os.path.join(DATA, "e0/e0_axes.npz"))["span_reward"].dtype)
    print(f"  +axis direction sha16 {axis_inj.direction_sha} (float64, as "
          f"Injection hashes it) == {_sha(_u32)} (as stored, float32 -- the "
          f"receipt's convention); ||v|| = {float(np.linalg.norm(rw)):.6f}",
          flush=True)
    print(f"  R arm direction: e0_random_dirs.npz[{C.RANDOM_DIRS_KEY!r}] "
          f"sha16 {rand_inj.direction_sha}  (file sha16 "
          f"{sha16_file(rz_path)})  alpha {rand_inj.alpha:.4f}", flush=True)
    print(f"  NO NEGATIVE POLE is constructed anywhere (PROPOSAL-j §6)",
          flush=True)

    # Round path. e2a set use_cached_rounds from this same artifact, e2b
    # reads it identically, and the 2026-08-09 adjudication carried it across
    # the v3 template change on the stated ground that the kernel gate is a
    # path-equivalence property of prefix-conditional forwards, not of the
    # sampled-text distribution. Choice forwards are uncached and state-free
    # regardless -- that is g3' clause 1 and it is not negotiable here.
    g1 = json.load(open(os.path.join(DATA, "e2a/g1_kernel_gate.json")))
    g1row = g1["results"].get(str(args.frac))
    gate_says = bool(g1row and g1row["pass"])

    # AMENDMENT 2 (i): the g1 gate is FIRST-TOKEN ONLY, so on its own it does
    # not license cached GENERATION. Above D1's dose the T-step identity
    # artifact is the binding input, and its absence is a stop rather than a
    # silent fall-back to the gate -- an undetermined licence is not a
    # granted one.
    tstep_path = os.path.join(DATA, "e2d/tstep_check.json")
    tstep = None
    if os.path.exists(tstep_path):
        tstep = json.load(open(tstep_path))
    if args.round_path == "gate" and args.frac > C.D1_FRAC:
        if tstep is None:
            raise SystemExit(
                f"NO T-STEP ARTIFACT at {tstep_path}. AMENDMENT 2 (i) makes "
                f"the identity check the licence for cached generation above "
                f"f = {C.D1_FRAC}, and the g1 gate alone is first-token only. "
                f"Run scripts/e2d_tstep_check.py first.")
        if abs(tstep["frac"] - args.frac) > 1e-9:
            raise SystemExit(
                f"T-STEP ARTIFACT IS FOR frac {tstep['frac']}, not "
                f"{args.frac}. Rule 1's spirit: a licence measured at one "
                f"dose is not inherited by another.")
        gate_says = bool(tstep["verdict"]["all_identical"])
        print(f"  T-step licence: {tstep['verdict']['n_identical']}/"
              f"{tstep['verdict']['n_rounds']} rounds identical -> "
              f"{'CACHED permitted' if gate_says else 'UNCACHED required'} "
              f"(AMENDMENT 2 (i))", flush=True)

    cached = {"gate": gate_says, "cached": True, "uncached": False}[args.round_path]
    print(f"  round path: {'CACHED' if cached else 'UNCACHED'} "
          f"(--round-path {args.round_path}; g1 artifact at frac {args.frac}: "
          f"pass={gate_says}, max_kl="
          f"{g1row['max_kl'] if g1row else 'n/a'}, family "
          f"{g1['template_family']}); choice forwards uncached regardless",
          flush=True)

    inj_by_arm = {"M": axis_inj, "S": None, "R": rand_inj}
    arms_n = dict(tier["n"])

    # --- PROPOSAL-j §2 D2 precondition, BEFORE any forward ---------------
    # >= 16 distinct task_ids per class on the M arm, so discrim's
    # task-disjoint split is disjoint in fact and not only in name.
    cov = task_id_coverage("M", arms_n["M"], tasks, args.draw_seed)
    print(f"  M-arm task_id coverage at draw seed {args.draw_seed}: "
          f"pos {cov['distinct_task_ids']['pos']}, "
          f"neg {cov['distinct_task_ids']['neg']} "
          f"(floor {cov['floor']} per class) -> "
          f"{'OK' if cov['meets_floor'] else 'SHORT'}", flush=True)
    if not cov["meets_floor"]:
        raise SystemExit(
            f"TASK_ID COVERAGE SHORT at draw seed {args.draw_seed}: "
            f"{cov['distinct_task_ids']}. PROPOSAL-j §2 D2 says reseed the "
            f"DRAW (never a session) and record the seed. Re-run with a "
            f"different --draw-seed; the per-session task sequences do not "
            f"move with it.")

    # --- run --------------------------------------------------------------
    res = run_campaign(adapter, arms_n, tasks, inj_by_arm, audit, ban_ids,
                       term_rx, temp=args.temp, scope=args.scope,
                       cached=cached, seed=args.draw_seed)
    sessions, counters = res["sessions"], res["counters"]

    # --- acceptance, COMPUTED BEFORE ANY ARTIFACT IS WRITTEN (trap 6) ----
    kls = res["verify_kls"]
    n_reads_expected = sum(len(s["choices"]) for s in sessions)
    kl_exact = sum(1 for k in kls if k == 0.0)
    fmt = verify_format(sessions, tasks)
    absent_ok = True
    try:
        assert_modules_absent(FORBIDDEN_MODULES)
    except SystemExit:
        absent_ok = False

    n_rounds = sum(len(s["rounds"]) + len(s["choices"]) for s in sessions)
    n_degen = counters.total("audit_degenerate")
    n_scaffold = sum(1 for s in sessions
                     for r in s["rounds"] + s["choices"]
                     if r["degen"] and str(r["degen"]).startswith("special:"))
    fired = check_bars(bars, {
        "round_degeneracy": (n_degen, n_rounds),
        "scaffold_absorption": (n_scaffold, max(n_rounds, 1)),
        "template_breakage": (fmt["n_walked"] - fmt["n_reconstructed"],
                              max(fmt["n_walked"], 1))})

    # exclusions under BOTH scopes (config.EXCLUSION_SCOPE's open item)
    excl = {}
    for arm in sorted(arms_n):
        arm_s = [s for s in sessions if s["arm"] == arm]
        excl[arm] = {
            "n": len(arm_s),
            "excluded_run_scope": sum(1 for s in arm_s if s["excluded"]),
            "excluded_strict_scope": sum(1 for s in arm_s
                                         if strict_exclusion(s)[0]),
            "reasons": [s["exclude_reason"] for s in arm_s if s["excluded"]]}

    # rule 28(a): report each declared feature's decidable-n on its domain.
    valid = [s for s in sessions if not s["excluded"]]
    decidable = {
        "stay_switch": (sum(1 for s in valid if len(s["choices"]) >= 2),
                        len(valid)),
        "session_share": (sum(1 for s in valid if s["choices"]), len(valid)),
        "fewer_degen_rounds_plus": (
            sum(1 for s in valid
                if sum(1 for r in s["rounds"] + s["choices"]
                       if r["steered"] and r["degen"])
                != sum(1 for r in s["rounds"] + s["choices"]
                       if not r["steered"] and r["degen"])), len(valid)),
        "termination_attempts": (counters.total("termination"), len(sessions)),
    }
    feature_report = {}
    for spec in C.declared_features():
        k, n = decidable[spec.name]
        feature_report[spec.name] = {
            "decidable": k, "domain_n": n, "domain": spec.domain,
            "floor": spec.min_decidable,
            "diagnosis": check_feature_defined(spec, k, n),
            "binding_at_d1": False}

    acceptance = {
        "kl_reads_expected": n_reads_expected,
        "kl_reads_logged": len(kls),
        "kl_exactly_zero": kl_exact,
        "kl_max": max(kls) if kls else None,
        "kl_all_exact": bool(kls and len(kls) == n_reads_expected
                             and kl_exact == len(kls)),
        "statepresent_absent": absent_ok,
        "format_check": fmt,
        "bars_fired": fired,
        "no_verdict_content": True,
    }
    acceptance["PASS"] = bool(
        acceptance["kl_all_exact"] and acceptance["statepresent_absent"]
        and fmt["all_ok"] and not fired)

    # --- marker readout (1e) and readability (1d), both descriptive at D1 -
    # SCORING IS DEFERRED FOR D2/D3. AMENDMENT 2 (iii) makes the rule-25 read
    # an input to Q2's clean set, and the read cannot exist until the sessions
    # do. So d2/d3 generate only; `scripts/e2d_score.py` does marker and
    # readability afterwards, taking the marks file. d1 keeps its inline
    # scoring because that is how it ran and its artifact is committed.
    score_inline = (args.tier == "d1") and not args.no_marker
    if not score_inline and args.tier != "d1":
        print(f"  scoring DEFERRED for tier {args.tier}: run "
              f"scripts/e2d_score.py with --sessions and --marks "
              f"(AMENDMENT 2 (iii) makes the read an input to Q2)", flush=True)

    t_marker0 = time.time()
    marker_out = None
    if score_inline:
        instruments, g = MK.instruments_or_stop()
        probes = json.load(open(os.path.join(
            DATA, "configs/e0_probes.json")))["probes"]
        print(f"  marker instrument rebuilt: G = {g:.6f} "
              f"(bar 0.5*G = {MK.bar_from(g):.4f}); {len(probes)} probes",
              flush=True)
        text_of = {r["task"]: r["task_text"]
                   for s in sessions for r in s["rounds"] + s["choices"]}
        rows = MK.collect(adapter, instruments, probes, sessions,
                          lambda tid: text_of[tid], progress=print)
        d = MK.deltas(rows, instruments, clean_only=True)
        marker_out = {"G": g, "bar_half_G": MK.bar_from(g),
                      "n_generations_scored": sum(1 for r in rows
                                                  if r["scores"]),
                      "n_skipped": sum(1 for r in rows if r["skipped"]),
                      "n_probe_forwards": sum(len(r["scores"]) for r in rows
                                              if r["scores"]),
                      "deltas": d,
                      "_descriptive": "D1 n = 8. No Q3 criterion applies."}

    marker_seconds = time.time() - t_marker0
    t_read0 = time.time()
    read_out = None
    try:
        if not score_inline:
            raise SystemExit("deferred")
        rounds_M = RD.clean_rounds(sessions, "M")
        if rounds_M["pos"] and rounds_M["neg"]:
            lad = RD.resampled_auc(adapter, rounds_M, k=2, key="e2d-d1")
            read_out = {"k2_resampled": lad, "gate_would_say": RD.gate(lad),
                        "n_clean_pos": len(rounds_M["pos"]),
                        "n_clean_neg": len(rounds_M["neg"]),
                        "_descriptive": ("D1 n = 4 M sessions. This exercises "
                                         "the wrapper end to end; it is not "
                                         "a Q2 reading.")}
        else:
            read_out = {"skipped": "one pole had no clean rounds",
                        "n_clean_pos": len(rounds_M["pos"]),
                        "n_clean_neg": len(rounds_M["neg"])}
    except SystemExit as exc:
        read_out = ({"deferred": "scoring runs in scripts/e2d_score.py"}
                    if str(exc) == "deferred" else {"error": str(exc)})

    read_seconds = time.time() - t_read0
    if isinstance(read_out, dict):
        read_out["seconds"] = read_seconds
    if isinstance(marker_out, dict):
        marker_out["seconds"] = marker_seconds

    # --- write the artifact, verdict already computed ---------------------
    out = {
        "item": "e2d", "tier": args.tier,
        "proposal": "PROPOSAL-j v1.1 (AMENDMENT 1, 70995c0)",
        "frac": args.frac, "layer": args.layer, "temp": args.temp,
        "roster_of_record": [list(p) for p in C.ROSTER],
        "audit_of_record": {"file": "data/configs/e2b_audit_v2.json",
                            "sha16": audit_cfg["sha16"]},
        "exclusion_scope": args.scope,
        "exclusion_scope_note": (
            "AMENDMENT 1 (ii) names the audit ARTIFACT, not the exclusion "
            "SCOPE. Both counts are reported; see excl.*_scope. FLAGGED for "
            "the design instance before D2, where Q1 binds."),
        "precedence": C.PRECEDENCE,
        "provenance": adapter.provenance(),
        "arm_provenance": {
            "M": {"axis": "span_reward", "layer": args.layer,
                  "frac": args.frac, "alpha": axis_inj.alpha,
                  "direction_sha": axis_inj.direction_sha},
            "S": None,
            "R": {"axis": f"e0_random_dirs[{C.RANDOM_DIRS_KEY}]",
                  "layer": args.layer, "frac": args.frac,
                  "alpha": rand_inj.alpha,
                  "direction_sha": rand_inj.direction_sha,
                  "file_sha16": sha16_file(rz_path)}},
        "no_negative_pole": True,
        "task_id_coverage": cov,
        "draw_seed": args.draw_seed,
        "round_path_cached": bool(cached),
        "round_path_source": args.round_path,
        "tstep_licence": (None if tstep is None else
                          {k: v for k, v in tstep["verdict"].items()
                           if k != "round_token_counts"}),
        "axis_sha_float64": axis_inj.direction_sha,
        "axis_sha_as_stored_float32": _sha(_u32),
        "axis_norm": float(np.linalg.norm(rw)),
        "ban_list": {"n_ids": len(ban_ids), "n_strings": len(ban_strings)},
        "declared_bars": [b.__dict__ for b in bars],
        "firing_cases": [list(c) for c in C.FIRING_CASES],
        "insulation": (
            "every choice read is readout.choice_read -- vanilla, uncached, "
            "verify=True with assert_construction_stable; "
            "valence_core.e2b.statepresent asserted absent from sys.modules "
            "at startup AND before every read"),
        "acceptance": acceptance,
        "exclusions": excl,
        "counters": counters.report(),
        "features_rule28a": feature_report,
        "marker": marker_out,
        "readability": read_out,
        "wall_clock": {"generation_s": res["seconds"],
                       "marker_s": marker_seconds,
                       "readability_s": read_seconds,
                       "total_s": res["seconds"],
                       "per_session_s": res["per_session_seconds"],
                       "mean_session_s": (float(np.mean(
                           res["per_session_seconds"]))
                           if res["per_session_seconds"] else None)},
        "sessions": sessions,
        "_no_verdict": ("D1 computes no verdict. Q1/Q2/Q3 and the run-dose "
                        "rule live in scripts/e2d_d2_analyze.py."),
    }

    path = args.out or canonical_for(args.tier)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, default=float)

    print("\n" + "=" * 74)
    print(f"  ACCEPTANCE: {'PASS' if acceptance['PASS'] else 'FAIL'}")
    print(f"    KL: {kl_exact}/{len(kls)} reads exactly 0.0 "
          f"(expected {n_reads_expected}); max {acceptance['kl_max']}")
    print(f"    statepresent absent: {absent_ok}")
    print(f"    format ({fmt['check']}): {fmt['n_reconstructed']}/"
          f"{fmt['n_walked']} reconstructed, "
          f"{fmt['n_seed_streams_matched']} seed streams matched")
    print(f"    bars fired: {fired or 'none'}")
    for arm in sorted(excl):
        e = excl[arm]
        print(f"    {arm}: {e['excluded_run_scope']}/{e['n']} excluded "
              f"(run scope {args.scope}); "
              f"{e['excluded_strict_scope']}/{e['n']} under the strict scope")
    print(f"  wrote {path}  ({res['seconds']:.0f}s, "
          f"{out['wall_clock']['mean_session_s']:.0f}s/session)")
    if not acceptance["PASS"]:
        print("  STOP -- write the entry and flag. Code does not "
              "self-adjudicate a failed acceptance.")
    return 0 if acceptance["PASS"] else 1


if __name__ == "__main__":
    sys.exit(main())
