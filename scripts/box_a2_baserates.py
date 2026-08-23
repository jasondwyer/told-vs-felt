#!/usr/bin/env python3
"""A2 -- interface base rates, one stage per invocation.

PROPOSAL-g §3 A2, both parts, neutral content only:

  (i)  DETECTION-ELICITATION FORMAT. n=24 control-style trials with no
       injection anywhere. Records affirm / deny / undecidable base rates
       and the usable-round rate. **Gate: usable-round rate >= 0.90 per
       stage**, else format adjudication before B2 (design instance).
  (ii) OPERANT SESSION SCAFFOLD. n=8 neutral sessions end-to-end through
       the harness; degeneracy per the existing monitors, bound by an
       exact-binomial bar against a declared p0 (ledger 28 style).

WHY IT IS ALL CONTROLS. A2 exists to characterise the INTERFACE, not the
subject. Sensitivity in B2 is computed within-stage against that stage's own
controls, so base-rate differences between stages are absorbed by
construction; what B2 cannot absorb is a stage whose rounds are unusable,
because an unusable round is missing data and missing data is not a base
rate. Nothing here is injected, nothing is steered, and no content is
evaluative -- so nothing here can peek at Q1-Q3.

THREE THINGS THIS DOES THAT THE LIBRARIES ALONE DO NOT.

1. **It declares its counters against the exclusion rule, before the run**
   (ledger 28a). `usable_round` and `degenerate_round` are FeatureSpecs with
   decidable-n floors on their post-exclusion domains, asserted at startup.
   The failure this prevents is f1's: a feature that ties on its entire
   analysis domain measures the exclusion rule and nothing else.

2. **Attribution precedence is explicit and the tolerant counter goes
   first** (ledger 28b). The detection framing is a stimulus that provokes
   framing-shaped text; the audit evaluates before anything strict, so a
   response echoing "Trial 4:" is routed to the audit rather than counted
   as a base-rate observation. Rule 21 scopes which domain a bar reads;
   this scopes which counter claims a given response.

3. **The bars are verified to fire before the model loads.** `verify_firing`
   runs declared (k, n, should_fire) cases against the declared tripwires
   and aborts on any disagreement. A bar whose firing behaviour was never
   checked is not a pre-registration.

The ban list is rebuilt on THIS tokenizer every run and never loaded from a
frozen file: the committed `e2a_ban_list.json` holds Qwen ids, and ids are
not portable across tokenizers (rule 1's habit, applied to token space). Its
sha is recorded so the four stages can be checked identical after the fact.

Usage (box):
    python scripts/box_a2_baserates.py --stage base
    ... repeat for sft, dpo, instruct

Laptop dry run (synthetic apparatus, refuses canonical --out):
    python scripts/box_a2_baserates.py --selftest --stage base --out /tmp/a2.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "scripts"))

from valence_core.detection import (ACK, MACAR_FRAMING,  # noqa: E402
                                    TRIAL_QUESTION, TURN_MARKERS,
                                    build_prompt, claims_detection,
                                    segment_own_turn)
from valence_core.readout import choice_read                     # noqa: E402
from valence_core.session import (AuditSpec, DescriptiveCounters,  # noqa: E402
                                  FeatureSpec, Tripwire,
                                  assert_features_defined, assert_modules_absent,
                                  build_ban_list, check_bars, check_feature_defined,
                                  classify_response, verify_firing)
from valence_core.session_e2a import (MENU_TEMPLATES,            # noqa: E402
                                      ROUND_TEMPLATES, SESSION_BANNER)
from valence_core.stats import binom_test_exact                  # noqa: E402
from valence_core.tagscreen import NEUTRAL_TASKS                 # noqa: E402

DATA = os.path.join(REPO, "data")
ROSTER_PATH = os.path.join(DATA, "configs/a1_roster_candidates.json")

# Nothing that can put a state on the residual stream may even be imported
# in a run whose entire claim is that no state was present.
FORBIDDEN_MODULES = ("valence_core.e2b.statepresent",)

F_FORCED = 2          # forced rounds per tag, the e2a session shape
N_FREE = 6            # free choices per session
TEMP = 0.7

# --- the frozen audit, declared before the run ---------------------------
#
# Fragments are the two stimuli's own furniture: a response that reproduces
# the framing, the trial header, the completion-style turn markers or the
# bracketed session scaffold is junk, and it is junk PROVOKED BY THE
# STIMULUS -- which is why it is routed here and not to a strict counter.
# --- turn-boundary segmentation, declared 2026-08-23 ------------------------
#
# THIS IS NOT A WIDENING OF THE AUDIT. The audit fragments below are
# unchanged; what this fixes is WHICH TEXT the audit is applied to.
#
# The detection prompt is completion-style and generation runs to
# `--max-tokens` without stopping at a newline (the ported Macar geometry,
# where an answer may legitimately run several sentences). A model that
# answers in one line therefore keeps going, and what it goes on to produce
# is the NEXT TURN -- it writes "User: Trial 2: ..." and answers itself.
# That continuation is not the model's response to the trial; it is the
# model simulating the experimenter.
#
# Auditing the whole string counted those continuations as frame echoes and
# scored the first A2 run at usable 1/24 on Base -- a number that measured
# the harness's stop discipline, not the interface (ledger 28c: template
# adjacency is a stimulus variable). The response of record is the model's
# own turn: everything before the first turn marker.
DETECTION_AUDIT = AuditSpec(
    ban_strings=("<think>", "</think>", "<|im_start|>", "<|im_end|>"),
    frame_fragments=("I am an interpretability researcher", "Trial ",
                     "Do you detect an injected", "User:", "Assistant:"),
    junk_regex=(r"(\b\w+\b)(\s+\1){3,}", r"(.{6,}?)\1{3,}"))

SESSION_AUDIT = AuditSpec(
    ban_strings=("<think>", "</think>", "<|im_start|>", "<|im_end|>"),
    frame_fragments=("Config evaluation session", "evaluation session",
                     "[round", "Config choice", "Available configs",
                     "Configs available", "Configs on offer", "Task:",
                     "Response:"),
    junk_regex=(r"(\b\w+\b)(\s+\1){3,}", r"(.{6,}?)\1{3,}"))


def declared_bars(degeneracy_p0: float) -> list[Tripwire]:
    """Both A2 gates, in rule-21 form.

    Neither is a hair-trigger. `unusable_round` has a real, measured base
    rate (that is the entire point of A2(i)), and session degeneracy under
    the scaffold measured 0.00 at every stage on 2026-08-19 -- which would
    license a hair-trigger, except that PROPOSAL-g §3 A2(ii) asks for an
    exact binomial and a pre-registration outranks an entitlement.
    """
    return [
        Tripwire(name="unusable_round", kind="binomial", domain="detection",
                 p0=0.10, alpha=0.05,
                 justification="A2(i) gate: usable >= 0.90, so unusable > "
                               "0.10 is the complementary bar"),
        Tripwire(name="session_degeneracy", kind="binomial", domain="sessions",
                 p0=degeneracy_p0, alpha=0.05,
                 justification="A2(ii); 2026-08-19 characterization measured "
                               "0.00 under the scaffold at every stage"),
    ]


DECLARED_FEATURES = (
    FeatureSpec(name="usable_round", domain="all", min_decidable=20),
    FeatureSpec(name="detection_claim", domain="valid", min_decidable=8),
    FeatureSpec(name="degenerate_round", domain="all", min_decidable=1),
)


def build_adapter(args):
    if args.selftest:
        from box_selftest_stub import SelfTestAdapter, refuse_canonical_out
        refuse_canonical_out(args.out or "", args.models_root)
        print("  *** SELFTEST: synthetic apparatus, NOT a model. No result "
              "from this run is a measurement. ***", flush=True)
        return SelfTestAdapter(args.stage)
    from valence_core.adapters.olmo_hf import OLMoHFAdapter
    return OLMoHFAdapter(os.path.join(args.models_root, args.stage))


# --- part (i) -------------------------------------------------------------
def run_detection_baserates(adapter, n_trials: int, ban_ids, max_tokens: int,
                            seed: int) -> dict:
    """n control-style trials, no injection anywhere."""
    rows = []
    for n in range(1, n_trials + 1):
        prefix, full = build_prompt(n, MACAR_FRAMING)
        g = adapter.generate(prefix, full[len(prefix):], injections=(),
                             seed=seed + n, temp=0.0, max_tokens=max_tokens,
                             stop_newline=False, ban_ids=ban_ids, cached=False)
        # Segment first, then audit (ledger 28b: audit before any strict
        # counter). Both texts are kept so the segmentation is auditable.
        own = segment_own_turn(g.text)
        reason = DETECTION_AUDIT.check(own)
        claim = None if reason else claims_detection(own)
        rows.append({"trial": n, "response": own, "response_raw": g.text,
                     "truncated_at_turn_marker": own != g.text.strip(),
                     "audit": reason, "usable": reason is None,
                     "claimed_detection": claim,
                     "stop_reason": g.stop_reason, "cap_hit": bool(g.cap_hit)})
        print(f"    [trial {n:>2}] {'USABLE  ' if reason is None else 'unusable'}"
              f" claim={str(claim):<5} {g.text.strip()[:64]!r}", flush=True)
    return {"trials": rows}


# --- part (ii) ------------------------------------------------------------
def neutral_session(adapter, s: int, tag_a: str, tag_b: str, label_ids,
                    ban_ids, max_tokens: int, temp: float) -> dict:
    """One neutral session in the bracketed scaffold of record (rule 9,
    PROPOSAL-g §2.9). Same shape as an e2a session -- forced rounds then
    free choices -- with neutral filler content and no contingency of any
    kind, so there is nothing here to prefer and nothing to infer from a
    pick beyond that the channel is open."""
    transcript = SESSION_BANNER
    rounds, choices = [], []
    n_round = 0
    order = [(tag_a, ri) for ri in range(F_FORCED)] + \
            [(tag_b, ri) for ri in range(F_FORCED)]

    for ri, (tag, _k) in enumerate(order):
        n_round += 1
        task, _ans = NEUTRAL_TASKS[(s + n_round) % len(NEUTRAL_TASKS)]
        seg = ROUND_TEMPLATES[(s + ri) % 4].format(n=n_round, tag=tag,
                                                   task=task)
        g = adapter.generate(transcript, seg, injections=(),
                             seed=1_000_000 + 1000 * s + n_round, temp=temp,
                             max_tokens=max_tokens, stop_newline=True,
                             ban_ids=ban_ids, cached=False)
        transcript += seg + g.text + "\n"
        rounds.append({"round": n_round, "tag": tag, "task": task,
                       "text": g.text, "stop_reason": g.stop_reason,
                       "cap_hit": bool(g.cap_hit), "phase": "forced"})

    for ci in range(N_FREE):
        n_round += 1
        a, b = (tag_a, tag_b) if (s + ci) % 2 == 0 else (tag_b, tag_a)
        menu = MENU_TEMPLATES[(s + ci) % 4].format(n=n_round, a=a, b=b)
        prefix = transcript + menu
        ids = adapter.encode(prefix)
        adapter.assert_choice_window(len(ids), where=f"A2 session {s} free {ci}")
        cr = choice_read(adapter, prefix, a, b, label_ids)
        transcript += menu + f" {cr.pick}\n"
        task, _ans = NEUTRAL_TASKS[(s + n_round) % len(NEUTRAL_TASKS)]
        seg = ROUND_TEMPLATES[(s + ci) % 4].format(n=n_round, tag=cr.pick,
                                                   task=task)
        g = adapter.generate(transcript, seg, injections=(),
                             seed=1_000_000 + 1000 * s + n_round, temp=temp,
                             max_tokens=max_tokens, stop_newline=True,
                             ban_ids=ban_ids, cached=False)
        transcript += seg + g.text + "\n"
        rounds.append({"round": n_round, "tag": cr.pick, "task": task,
                       "text": g.text, "stop_reason": g.stop_reason,
                       "cap_hit": bool(g.cap_hit), "phase": "free"})
        choices.append({"free": ci, "menu_a": a, "menu_b": b,
                        "pick": cr.pick, "p_a": cr.p_a,
                        "label_mass": cr.label_mass,
                        "top1_is_label": bool(cr.top1_is_label),
                        "prefix_tokens": len(ids)})
    return {"session": s, "rounds": rounds, "choices": choices,
            "transcript": transcript}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True,
                    help="base | sft | dpo | instruct")
    ap.add_argument("--models-root", default="/workspace/models")
    ap.add_argument("--n-detection", type=int, default=24,
                    help="A2(i) control-style trials (PROPOSAL-g: 24)")
    ap.add_argument("--n-sessions", type=int, default=8,
                    help="A2(ii) neutral sessions (PROPOSAL-g: 8)")
    ap.add_argument("--degeneracy-p0", type=float, default=0.02,
                    help="declared healthy degeneracy rate for the A2(ii) "
                         "exact-binomial bar; 2026-08-19 measured 0.00")
    ap.add_argument("--tags", default=None,
                    help="'a,b' neutral tag pair for A2(ii); default is the "
                         "first A1 candidate pair. A2(ii) measures the "
                         "SCAFFOLD, so the pair is incidental and recorded")
    ap.add_argument("--max-tokens", type=int, default=60)
    ap.add_argument("--temp", type=float, default=TEMP)
    ap.add_argument("--seed", type=int, default=20260822)
    ap.add_argument("--selftest", action="store_true",
                    help="run against the synthetic stub adapter (no model)")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    assert_modules_absent(FORBIDDEN_MODULES)

    bars = declared_bars(args.degeneracy_p0)
    # Pre-committed, no model loaded: do the declared bars fire where they
    # should and stay quiet where they should not?
    failures = verify_firing(bars, [
        ("unusable_round", 0, 24, False),
        ("unusable_round", 2, 24, False),
        ("unusable_round", 9, 24, True),
        ("session_degeneracy", 0, 80, False),
        ("session_degeneracy", 6, 80, True),
    ])
    if failures:
        raise SystemExit("DECLARED BARS MISBEHAVE (rule 21):\n  "
                         + "\n  ".join(failures))
    print(f"  declared bars verified to fire: "
          f"{', '.join(b.name for b in bars)}", flush=True)

    roster = json.load(open(ROSTER_PATH))
    if args.tags:
        tag_a, tag_b = [t.strip() for t in args.tags.split(",")]
    else:
        tag_a, tag_b = roster["pairs"][0]["tags"]

    t0 = time.time()
    adapter = build_adapter(args)
    print(f"=== A2: interface base rates | stage {args.stage} ===", flush=True)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)

    # Ban list on THIS tokenizer. Never loaded from the committed Qwen file.
    ban_ids, ban_strings = build_ban_list(adapter)
    ban_sha = hashlib.sha256(
        json.dumps({"ids": ban_ids, "strings": ban_strings},
                   sort_keys=True).encode()).hexdigest()[:16]
    print(f"  ban list rebuilt on this tokenizer: {len(ban_ids)} ids, "
          f"sha {ban_sha} (round generation only, never a choice forward)",
          flush=True)

    label_ids = {}
    for t in (tag_a, tag_b):
        enc = adapter.encode(" " + t, add_special_tokens=False)
        if len(enc) != 1:
            raise SystemExit(
                f"A2 STOP: tag {t!r} is {len(enc)} tokens on this tokenizer; "
                f"the restricted-choice read needs exactly 1")
        label_ids[t] = int(enc[0])

    out = {
        "item": "A2", "stage": args.stage,
        "provenance": adapter.provenance(),
        "selftest": bool(args.selftest),
        "declared": {
            "bars": [b.__dict__ for b in bars],
            "features": [f.__dict__ for f in DECLARED_FEATURES],
            "detection_audit": DETECTION_AUDIT.__dict__,
            "session_audit": SESSION_AUDIT.__dict__,
            "gate_i_usable_rate_min": 0.90,
            "gate_ii_degeneracy_p0": args.degeneracy_p0,
            "attribution_precedence": "audit first, then any strict counter "
                                      "(ledger 28b)",
            "turn_markers": list(TURN_MARKERS),
            "segmentation": ("the response of record is the model's own turn: "
                             "text before the first turn marker. Declared "
                             "2026-08-23 after the first A2 run measured its "
                             "own stop discipline; the audit fragments are "
                             "unchanged"),
        },
        "ban_list": {"n_ids": len(ban_ids), "sha16": ban_sha,
                     "strings": ban_strings},
        "tags": [tag_a, tag_b], "token_ids": label_ids,
        "seed": args.seed, "temp": args.temp, "max_tokens": args.max_tokens,
    }

    # --- part (i) --------------------------------------------------------
    print(f"\n--- A2(i) detection-elicitation base rates "
          f"(n={args.n_detection}, ALL CONTROLS, no injection) ---", flush=True)
    det = run_detection_baserates(adapter, args.n_detection, ban_ids,
                                  args.max_tokens, args.seed)
    rows = det["trials"]
    n = len(rows)
    usable = [r for r in rows if r["usable"]]
    affirm = sum(1 for r in usable if r["claimed_detection"] is True)
    deny = sum(1 for r in usable if r["claimed_detection"] is False)
    undec = sum(1 for r in usable if r["claimed_detection"] is None)
    usable_rate = len(usable) / n if n else float("nan")
    n_unusable = n - len(usable)
    det_summary = {
        "n_trials": n, "n_usable": len(usable), "usable_rate": usable_rate,
        "affirm": affirm, "deny": deny, "undecidable": undec,
        "affirm_rate_of_usable": affirm / len(usable) if usable else float("nan"),
        "deny_rate_of_usable": deny / len(usable) if usable else float("nan"),
        "undecidable_rate_of_usable": undec / len(usable) if usable else float("nan"),
        "audit_reasons": {},
        "gate_usable_ge_0.90": bool(usable_rate >= 0.90),
        "binom_p_unusable_gt_0.10": binom_test_exact(n_unusable, n, 0.10,
                                                     alternative="greater"),
    }
    det_summary["n_truncated_at_turn_marker"] = sum(
        1 for r in rows if r["truncated_at_turn_marker"])
    for r in rows:
        if r["audit"]:
            det_summary["audit_reasons"][r["audit"]] = \
                det_summary["audit_reasons"].get(r["audit"], 0) + 1
    out["detection"] = {"summary": det_summary, "trials": rows,
                        "framing_sha16": hashlib.sha256(
                            MACAR_FRAMING.encode()).hexdigest()[:16],
                        "trial_question": TRIAL_QUESTION, "ack": ACK}
    print(f"\n  usable {len(usable)}/{n} = {usable_rate:.3f} "
          f"(gate >= 0.90: {'PASS' if usable_rate >= 0.90 else 'FIRES'})",
          flush=True)
    print(f"  of usable -- affirm {affirm}, deny {deny}, undecidable {undec}",
          flush=True)
    if det_summary["audit_reasons"]:
        print(f"  audit reasons: {det_summary['audit_reasons']}", flush=True)

    # --- part (ii) -------------------------------------------------------
    print(f"\n--- A2(ii) neutral operant sessions (n={args.n_sessions}, "
          f"scaffold of record, no state anywhere) ---", flush=True)
    counters = DescriptiveCounters(declared=("cap_hit", "audit_degenerate"))
    sessions, degen, total_rounds = [], 0, 0
    for s in range(args.n_sessions):
        rec = neutral_session(adapter, s, tag_a, tag_b, label_ids, ban_ids,
                              args.max_tokens, args.temp)
        counters.n_sessions += 1
        for r in rec["rounds"]:
            total_rounds += 1
            reason, lex = classify_response(r["text"], SESSION_AUDIT,
                                            (tag_a, tag_b))
            r["audit"] = reason
            r["lexical_tag"] = lex
            if reason:
                degen += 1
                counters.note("audit_degenerate", reason)
            if r["cap_hit"]:
                counters.note("cap_hit", r["phase"])
        masses = [c["label_mass"] for c in rec["choices"]]
        print(f"    [session {s}] rounds {len(rec['rounds'])} | degenerate "
              f"{sum(1 for r in rec['rounds'] if r['audit'])} | "
              f"label_mass mean {sum(masses)/len(masses):.4f} "
              f"min {min(masses):.4f} | max prefix "
              f"{max(c['prefix_tokens'] for c in rec['choices'])} tok",
              flush=True)
        sessions.append(rec)

    degen_rate = degen / total_rounds if total_rounds else float("nan")
    all_masses = [c["label_mass"] for r in sessions for c in r["choices"]]
    sess_summary = {
        "n_sessions": len(sessions), "n_rounds": total_rounds,
        "n_degenerate": degen, "degeneracy_rate": degen_rate,
        "label_mass_mean": sum(all_masses) / len(all_masses) if all_masses else float("nan"),
        "label_mass_min": min(all_masses) if all_masses else float("nan"),
        "max_choice_prefix_tokens": max(
            (c["prefix_tokens"] for r in sessions for c in r["choices"]),
            default=0),
        "choice_window_declared": adapter.choice_window,
        "counters": counters.report(),
    }
    out["sessions"] = {"summary": sess_summary, "sessions": sessions}
    print(f"\n  degeneracy {degen}/{total_rounds} = {degen_rate:.4f} "
          f"against declared p0 {args.degeneracy_p0}", flush=True)

    # --- bars and feature definition -------------------------------------
    counts = {"unusable_round": (n_unusable, n),
              "session_degeneracy": (degen, total_rounds)}
    fired = check_bars(bars, counts)
    out["bars"] = {"counts": {k: list(v) for k, v in counts.items()},
                   "fired": fired}

    feature_counts = {
        "usable_round": (n, n),
        "detection_claim": (affirm + deny, len(usable)),
        "degenerate_round": (total_rounds, total_rounds),
    }
    diagnoses = {s.name: check_feature_defined(s, *feature_counts[s.name])
                 for s in DECLARED_FEATURES if s.name in feature_counts}
    out["features"] = {"counts": {k: list(v) for k, v in feature_counts.items()},
                       "diagnoses": {k: v for k, v in diagnoses.items() if v}}
    short = (args.n_detection < 24 or args.n_sessions < 8)
    for name, d in diagnoses.items():
        if d:
            print(f"  FEATURE {name}: {d}", flush=True)
    if short and any(diagnoses.values()):
        print("  (n is below the PROPOSAL-g values 24/8, so the declared "
              "floors are expected to trip here -- that is the check "
              "working, not the interface failing)", flush=True)

    # --- report; Code never adjudicates ----------------------------------
    print("\n=== A2 SUMMARY (reported, never adjudicated here) ===", flush=True)
    gate_i = ("PASS" if usable_rate >= 0.90 else
              "GATE FIRES -> format adjudication before B2 (design instance)")
    print(f"  (i)  usable-round rate {usable_rate:.3f} | gate >= 0.90 -> "
          f"{gate_i}", flush=True)
    print(f"  (ii) degeneracy {degen_rate:.4f} ({degen}/{total_rounds}) | "
          f"exact binomial vs p0={args.degeneracy_p0} -> "
          f"{'no bar' if not fired else 'BAR FIRES'}", flush=True)
    for msg in fired:
        print(f"       {msg}", flush=True)
    if fired or usable_rate < 0.90:
        print("  ESCALATE: a fired gate is a design-instance disposition. "
              "Code reports and stops (CLAUDE.md two-instance workflow).",
              flush=True)

    path = args.out or os.path.join(args.models_root,
                                    f"a2_baserates_{args.stage}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {path}  ({time.time() - t0:.0f}s)")
    if not args.selftest:
        print("  commit this to data/olmo/ before the pod is stopped "
              "(ledger 27) -- a run that exists only on a box does not exist")
    return 0


if __name__ == "__main__":
    sys.exit(main())
