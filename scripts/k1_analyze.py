#!/usr/bin/env python3
"""PROPOSAL-k Stage 1 analyzer (§1.3-§1.6). Committed BEFORE any Stage 1
forward, with a synthetic battery that reaches every G2 branch, G1/G3
pass and fail, and the assertion-failure STOP.

    --selftest                the battery (model-free, seconds)
    --run [--shuffles 200 --workers 8 --out-name k1_analysis.json]
                              the real reads: probes, G1-G5, the outcome
                              sentence -> data/k/<out-name>; raw stdout is
                              the caller's to tee into results/raw/
"""
from __future__ import annotations

import argparse, json, os, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from valence_core.k import analysis as A                         # noqa: E402

DATA = os.path.join(REPO, "data")


def selftest() -> int:
    results = []
    def chk(name, ok, got=""):
        results.append(bool(ok)); print(f"  [{'PASS' if ok else 'FAIL'}] {name:70s} {got}", flush=True)
    t0 = time.time()
    expect = {"ABSENT": "ABSENT", "PRESENT": "PRESENT", "INDETERMINATE": "INDETERMINATE", "G1_FAIL": "G1_FAIL", "G3_FAIL": "G3_FAIL", "STOP": "STOP"}
    for br, want in expect.items():
        meta, sess = A.synthetic(br, n_sessions=8, dim=8)
        if br == "STOP":
            ev = A.evaluate(meta, {"families": {}}, sess)
            chk(f"battery {br}: identity failure -> STOP without evaluating gates", ev["branch"] == "STOP" and not ev["gates_evaluated"], ev["branch"])
            continue
        loaded = A.load_stacks(meta)
        probes = A.run_probes(loaded, n_shuffles=20, workers=8, seed=5, only=A.GATE_FAMILIES)
        ev = A.evaluate(meta, probes, sess)
        chk(f"battery {br} -> {want}", ev["branch"] == want, f"got {ev['branch']}; G1 {ev.get('G1', {}).get('verdict')} G2 {ev.get('G2', {}).get('verdict')} G3 {ev.get('G3', {}).get('verdict')}")
        if br == "ABSENT":
            chk("ABSENT: G1 medians at bar (A >= .90, B >= .75), every band layer above null",
                ev["G1"]["median_auc_labelA"] >= A.G1_MEDIAN_A and ev["G1"]["median_auc_labelB"] >= A.G1_MEDIAN_B and all(ev["G1"]["above_null_every_layer"].values()))
            chk("ABSENT: G2 no layer above null in L49-L63", ev["G2"]["n_above"] == 0)
            chk("ABSENT: G3 median >= .90 over L51-L62", ev["G3"]["median_auc"] >= A.G3_MEDIAN and ev["G3"]["above_null_every_layer"])
            chk("G4 computed on exactly R+A, R+B, M++, R++ (prohibition asserted)", set(k for k in ev["G4"] if k != "prohibition") == {"R+A", "R+B", "M++", "R++"})
            chk("G4 signed shift exists on R masks only", all("signed_shift_toward_first_block_label" in ev["G4"][m] for m in ("R+A", "R+B", "R++")) and "signed_shift_toward_first_block_label" not in ev["G4"]["M++"])
            chk("G5 per-pair shares with exact intervals; alternation and stay rates over all sessions",
                len(ev["G5"]["per_pair_first_pick_share"]) == 4 and ev["G5"]["strict_alternation"]["n"] == 8 and ev["G5"]["stay_transitions"]["n"] == 40)
            chk("the battery probes the four gate families only; the real run probes all twelve (comparators, beside, text-only)",
                set(probes["families"]) == set(A.GATE_FAMILIES) and len(A.families(loaded)) == 12)
            chk("sentence of record selected verbatim from §1.5", ev["sentence"] == A.SENTENCES["ABSENT"])
        if br == "INDETERMINATE":
            chk("INDETERMINATE: exactly 2 G2 layers above null", ev["G2"]["n_above"] == 2, ev["G2"]["layers_above_null"])
    lo, hi = A.clopper_pearson(0, 48); lo2, hi2 = A.clopper_pearson(3, 102)
    chk("Clopper-Pearson: 0/48 -> [0, .074]; 3/102 -> [.006, .083]", abs(hi - 0.0740) < 2e-3 and abs(lo2 - 0.0061) < 2e-3 and abs(hi2 - 0.0834) < 2e-3, f"{hi:.4f} {lo2:.4f} {hi2:.4f}")
    chk("bars are the proposal's: G1 .90/.75 over L51-L61; G2 L49-L63 with >= 3 for PRESENT; G3 .90 over L51-L62; 200 shuffles",
        A.G1_BAND == tuple(range(51, 62)) and A.G2_LAYERS == tuple(range(49, 64)) and A.G3_BAND == tuple(range(51, 63)) and A.N_SHUFFLES == 200 and A.G2_PRESENT_MIN_LAYERS == 3)
    meta_s, sess_s = A.synthetic("ABSENT", n_sessions=8, dim=8)
    meta_s["per_session"]["2"]["masks"].pop("R++")
    chk("a missing mask is an assertion failure -> STOP before any probe", A.evaluate(meta_s, {"families": {}}, sess_s)["branch"] == "STOP" and any("R++" in f for f in A.assertion_failures(meta_s)))
    meta_v, sess_v = A.synthetic("ABSENT", n_sessions=8, dim=8)
    meta_v["per_session"]["1"]["excluded"] = True
    lv, la = A.load_stacks(meta_v, domain="valid"), A.load_stacks(meta_v, domain="all")
    chk("domain: 'valid' drops an excluded session, 'all' keeps it; both declared in the output", lv["n_sessions"] == 7 and la["n_sessions"] == 8 and lv["domain"] == "valid")
    chk("select_sentence is disjunction-complete: G3 FAIL dominates, then G1 FAIL, then G2's three",
        A.select_sentence({"verdict": "FAIL"}, {"verdict": "PRESENT"}, {"verdict": "FAIL"})[0] == "G3_FAIL"
        and A.select_sentence({"verdict": "FAIL"}, {"verdict": "ABSENT"}, {"verdict": "PASS"})[0] == "G1_FAIL"
        and A.select_sentence({"verdict": "PASS"}, {"verdict": "INDETERMINATE"}, {"verdict": "PASS"})[0] == "INDETERMINATE")
    n_ok = sum(results)
    print("-" * 78); print(f"  {n_ok}/{len(results)} analyzer battery checks pass ({time.time() - t0:.0f}s)")
    return 0 if n_ok == len(results) else 1


def run(args) -> int:
    meta = json.load(open(os.path.join(DATA, "k/k1_reads.json")))
    sessions = json.load(open(os.path.join(DATA, "k/k1_sessions.json")))["sessions"]
    path = os.path.join(DATA, "k", args.out_name)
    if os.path.exists(path) and not args.overwrite:
        raise SystemExit(f"{path} exists; pass --out-name NEW or --overwrite (trap 22)")
    print(f"  reads: {len(meta['per_session'])} sessions, complete {meta.get('complete')}; layers {meta['capture_layers']}", flush=True)
    # §1.5's assertion classes are checked BEFORE any probe is computed: an invalid instrument prints no table (rule 6)
    fails = A.assertion_failures(meta)
    if fails:
        ev = A.evaluate(meta, {"families": {}}, sessions)
        print(f"  STOP -- {len(fails)} assertion failure(s), no gate evaluated, no probe run: {fails[:5]}")
        with open(path, "w") as fh:
            json.dump({"item": "PROPOSAL-k STAGE 1 -- CHANNEL STUDY", "evaluation": ev}, fh, indent=1, default=float)
        print(f"  wrote {path}"); return 1
    t0 = time.time()
    loaded = A.load_stacks(meta, domain="valid")
    probes = A.run_probes(loaded, n_shuffles=args.shuffles, workers=args.workers)
    loaded_all = A.load_stacks(meta, domain="all")
    probes_all = A.run_probes(loaded_all, n_shuffles=args.shuffles, workers=args.workers, only=A.GATE_FAMILIES) if loaded_all["n_sessions"] != loaded["n_sessions"] else None
    print(f"  probes done in {(time.time() - t0) / 60:.1f} min ({probes['n_jobs']} jobs on {loaded['n_sessions']} valid sessions; LOSO; {args.shuffles} shuffles"
          f"{'; beside: ' + str(probes_all['n_jobs']) + ' jobs on all ' + str(loaded_all['n_sessions']) if probes_all else ''})", flush=True)
    ev = A.evaluate(meta, probes, sessions, probes_all=probes_all)
    out = {"item": "PROPOSAL-k STAGE 1 -- CHANNEL STUDY", "n_sessions": len(meta["per_session"]), "n_sessions_valid": loaded["n_sessions"], "n_shuffles": args.shuffles,
           "procedure": "standardized L2 logistic regression (published hyperparameters); grouped leave-one-session-out CV; AUC per layer; label-shuffle null (95th pct); text-only baseline = M0 rows with the start-order target",
           "bars": {"G1": [A.G1_MEDIAN_A, A.G1_MEDIAN_B, list(A.G1_BAND)], "G2": [list(A.G2_LAYERS), A.G2_PRESENT_MIN_LAYERS], "G3": [A.G3_MEDIAN, list(A.G3_BAND)]},
           "probes": probes["families"], "evaluation": ev}
    for name, fam in probes["families"].items():
        print(f"\n  {name}")
        print("  " + "".join(f"{l:>6}" for l in probes["layers"]))
        print("  " + "".join(f"{fam[str(l)]['auc_loso']:.2f}{'*' if fam[str(l)]['above_null'] else ' '}".rjust(6) for l in probes["layers"]))
    print(f"\n  G1 {ev.get('G1', {}).get('verdict')}  G2 {ev.get('G2', {}).get('verdict')}  G3 {ev.get('G3', {}).get('verdict')}  -> branch {ev['branch']}")
    print(f"  SENTENCE (design confirms; never rewrites) [{ev['sentence_provenance']}]: {ev['sentence']}")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, default=float)
    print(f"  wrote {path}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--shuffles", type=int, default=A.N_SHUFFLES)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out-name", default="k1_analysis.json")
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()
    print("INVOCATION: " + " ".join([sys.executable] + sys.argv), flush=True)
    if args.selftest:
        return selftest()
    if args.run:
        return run(args)
    ap.print_help(); return 2


if __name__ == "__main__":
    sys.exit(main())
