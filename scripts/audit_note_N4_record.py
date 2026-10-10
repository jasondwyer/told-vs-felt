#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N4 addendum: e2a's correction of record, beside the artifact.

The PI's routing of 2026-10-09: record the audit-v2 e2a count (54/101, Δ +0.0347,
p 0.27535) as an artifact beside data/e2a/analysis.json, so that a reader who opens the
repository finds the correction of record (the Digest seat's FLAG I), and add the control
arms' Wilson intervals (FLAG B).

data/e2a/analysis.json is the frozen-audit analysis as published (55/102) and is not
modified. This script recomputes both audits with the record's own analyzer
(scripts/e2a_recount.py, imported read-only; every repository module it loads is asserted
equal to its blob at the record pin bbc9ffe), extends that analyzer's primary definition
(share of valid sessions whose first free pick was the +pole label) to the three control
arms, asserts every per-arm n, Δ_first and p against analysis.json, and writes:

  data/e2a/analysis.correction-of-record.json   the artifact (the routing's placement)
  results/raw/2026-10-09_note-N4-correction.md  the audit raw

Intervals are 95% two-sided Wilson score on the share P(+pole), also given on the Δ_first
scale (share - 1/2). No model, no randomness, no network.

    jlens-qwen36/.venv/bin/python scripts/audit_note_N4_record.py [--out-json PATH] [--out-md PATH]
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
import subprocess
import sys
from statistics import NormalDist

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = "bbc9ffe72fb8a942431c9bf2622a36e581fdf93c"
N4_AT = "09c3a8c"                                      # the N4 item raw's commit
N4_RAW = "results/raw/2026-10-08_note-N4-e2a.md"
BLOCK = "AUDIT-note-release-v1_2.md"
ARTIFACT = "data/e2a/analysis.correction-of-record.json"
RAW = "results/raw/2026-10-09_note-N4-correction.md"
ARMS = ("reward", "sham", "random1", "random2")
INPUTS = ("scripts/e2a_recount.py", "data/e2a/sessions.jsonl", "data/configs/e2b_audit_v2.json",
          "data/e2a/analysis.json")
CLONE = os.path.join(REPO, "jlens-qwen36")


def git(*a):
    return subprocess.run(["git", "-C", REPO, *a], check=True, capture_output=True, text=True).stdout


def blob_at(path, rev=PIN):
    return subprocess.run(["git", "-C", REPO, "show", f"{rev}:{path}"], check=True, capture_output=True).stdout


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(p):
    with open(p, "rb") as f:
        return sha256_bytes(f.read())


def wilson(k, n, conf=0.95):
    """Wilson score interval (the same form as scripts/audit_note_N4.py:wilson)."""
    z = NormalDist().inv_cdf(1 - (1 - conf) / 2)
    c = (k + z * z / 2) / (n + z * z)
    h = z * math.sqrt(k * (n - k) / n + z * z / 4) / (n + z * z)
    return c - h, c + h


def line_of(path, needle, rev=None):
    """1-based line of the unique line containing needle (working tree, or a commit)."""
    txt = blob_at(path, rev).decode() if rev else open(os.path.join(REPO, path), encoding="utf-8").read()
    hits = [i for i, ln in enumerate(txt.split("\n"), 1) if needle in ln]
    assert len(hits) == 1, (path, rev, needle, hits)
    return hits[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-json", default=os.path.join(REPO, ARTIFACT))
    ap.add_argument("--out-md", default=os.path.join(REPO, RAW))
    a = ap.parse_args()

    # inputs: the working tree must equal the record pin for every file read
    for p in INPUTS:
        assert open(os.path.join(REPO, p), "rb").read() == blob_at(p), f"{p} differs from {PIN[:7]}"
    analysis = json.load(open(os.path.join(REPO, "data/e2a/analysis.json")))

    # the record's analyzer, imported read-only from the repository root
    os.chdir(REPO)
    if REPO not in sys.path:
        sys.path.insert(0, REPO)
    spec = importlib.util.spec_from_file_location("e2a_recount_ro", os.path.join(REPO, "scripts/e2a_recount.py"))
    rc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rc)
    me = os.path.relpath(os.path.abspath(__file__), REPO)
    loaded = sorted({os.path.relpath(m.__file__, REPO) for m in list(sys.modules.values())
                     if getattr(m, "__file__", None) and os.path.abspath(m.__file__).startswith(REPO + os.sep)
                     and not os.path.abspath(m.__file__).startswith(CLONE + os.sep)} | {"scripts/e2a_recount.py"})
    loaded = [p for p in loaded if p != me]
    from_clone = [m.__file__ for m in list(sys.modules.values()) if getattr(m, "__file__", None)
                  and os.path.abspath(m.__file__).startswith(CLONE + os.sep)
                  and not os.path.abspath(m.__file__).startswith(os.path.join(CLONE, ".venv") + os.sep)]
    assert not from_clone, f"modules loaded from the clone outside its .venv: {from_clone}"
    bad = [p for p in loaded if open(os.path.join(REPO, p), "rb").read() != blob_at(p)]
    assert not bad, f"imported module differs from the pin: {bad}"

    def arm_primary(audit, arm):
        valid = [s for s in rc.ROWS if s["arm"] == arm and rc.exclusion(s, audit) is None]
        return sum(1 for s in valid if s["first_free_pick_pos"]), len(valid)

    # the reward arm through the analyzer's own primary(); the extension must agree with it
    kf, nf = rc.primary(rc.FROZEN)
    kv, nv = rc.primary(rc.V2)
    assert (kf, nf) == arm_primary(rc.FROZEN, "reward") == (55, 102)
    assert (kv, nv) == arm_primary(rc.V2, "reward") == (54, 101)
    byf, _, detf = rc.tally(rc.FROZEN)
    byv, _, detv = rc.tally(rc.V2)
    added = sorted(set(d[0] for d in detv) - set(d[0] for d in detf))
    assert added == [1], added

    def row(audit, arm):
        k, n = arm_primary(audit, arm)
        p = rc.binom_p_one_sided(k, n)
        lo, hi = wilson(k, n)
        return {"arm": arm, "k_plus_pole_first_pick": k, "n_valid": n, "share": k / n,
                "delta_first": round(k / n - 0.5, 4), "delta_first_exact": k / n - 0.5,
                "binom_p_one_sided": round(p, 5), "binom_p_one_sided_exact": p,
                "wilson95_share": [lo, hi], "wilson95_delta_first": [lo - 0.5, hi - 0.5]}

    frozen = {arm: row(rc.FROZEN, arm) for arm in ARMS}
    v2 = {arm: row(rc.V2, arm) for arm in ARMS}
    # every frozen-audit figure equals data/e2a/analysis.json; the control arms are unchanged under v2
    for arm in ARMS:
        r_ = frozen[arm]
        assert r_["n_valid"] == analysis[arm]["n"], arm
        assert r_["delta_first"] == analysis[arm]["delta_first"], (arm, r_["delta_first"])
        assert r_["binom_p_one_sided"] == analysis[arm]["binom_p_one_sided"], arm
        if arm != "reward":
            assert {k: v for k, v in v2[arm].items()} == r_, arm
            assert byv[arm] == byf[arm], arm
    rv = v2["reward"]
    assert (rv["delta_first"], rv["binom_p_one_sided"]) == (0.0347, 0.27535)
    assert [round(x, 3) for x in rv["wilson95_share"]] == [0.438, 0.629]

    # locators (asserted unique)
    corr_a = line_of("archive/RESULTS-cycles3-4.md", "> **CORRECTION (2026-08-21", PIN)
    corr_b = line_of("archive/RESULTS-cycles3-4.md",
                     "below are unmodified; this addendum is the correction of record.", PIN)
    n4_v2 = line_of(N4_RAW, "- Audit v2 (`data/configs/e2b_audit_v2.json`): reward excluded", N4_AT)
    n4_fn = line_of(N4_RAW, "| preprint footnote 1 (:174): '54 of 101, Δ = +0.035, p = 0.275' |", N4_AT)
    n4_wil = line_of(N4_RAW, "| 54/101 | Wilson score | [0.4379, 0.6289]", N4_AT)
    blk = line_of(BLOCK, "### N4.", PIN)
    f3_iv = line_of("FINDINGS-3.md", "(P(+) interval ≈ .44–.64)", PIN)
    n4_ref4 = line_of(N4_RAW, "4. The approach-probability interval ≈ [.44, .64] (a record figure, reproduced at 2 dp "
                              "under Clopper-Pearson and Wald)", N4_AT)
    # the item raw's printed figures, asserted equal to this run's at their printed precision
    n4_txt = blob_at(N4_RAW, N4_AT).decode().split("\n")
    assert (f"**{kv}/{nv}**, Δ_first = {rv['delta_first']:+.4f}, one-sided exact binomial p = "
            f"{rv['binom_p_one_sided']:.5f}") in n4_txt[n4_v2 - 1]
    assert f"[{rv['wilson95_share'][0]:.4f}, {rv['wilson95_share'][1]:.4f}]" in n4_txt[n4_wil - 1]
    all_contain_half = all(v2[arm]["wilson95_share"][0] < 0.5 < v2[arm]["wilson95_share"][1] for arm in ARMS) and \
        frozen["reward"]["wilson95_share"][0] < 0.5 < frozen["reward"]["wilson95_share"][1]

    head = git("rev-parse", "HEAD").strip()
    stamp = subprocess.run(["date", "-u", "+%Y-%m-%d %H:%M:%S UTC"], capture_output=True, text=True).stdout.strip()
    script_sha = sha256_file(os.path.abspath(__file__))
    in_shas = {p: sha256_bytes(blob_at(p)) for p in INPUTS}

    COUNT_KEYS = ("k_plus_pole_first_pick", "n_valid", "delta_first", "binom_p_one_sided")

    def arm_block(r_):
        d = {k: r_[k] for k in COUNT_KEYS}
        d["computed_new"] = {"wilson95_share": r_["wilson95_share"], "wilson95_delta_first": r_["wilson95_delta_first"]}
        return d

    interval_note = (f"The record prints the approach-probability interval for 55/102 as about .44-.64 and names no "
                     f"method (FINDINGS-3.md@{PIN[:7]}:{f3_iv}). Clopper-Pearson and Wald reproduce it at two decimals; "
                     f"Wilson gives [.44, .63] ({N4_RAW}@{N4_AT}:{n4_ref4}). The Wilson intervals here are computed new, "
                     f"at the PI's routing, and are not the record's.")
    art = {
        "what": "e2a primary: the correction of record (audit v2). data/e2a/analysis.json beside this file is the "
                "frozen-audit analysis as published (55/102) and is left unmodified.",
        "status": {
            "k_plus_pole_first_pick, n_valid, delta_first, binom_p_one_sided":
                "reproduced: the record's analyzer (scripts/e2a_recount.py) over committed artifacts",
            "computed_new.wilson95_share, computed_new.wilson95_delta_first":
                "computed-new: 95% Wilson score intervals; the record names no interval method"},
        "of_record": {
            "audit": "v2 (data/configs/e2b_audit_v2.json)",
            "reward": arm_block(rv),
            "why": "audit v2 excludes one more reward session (s1), on a defect class the frozen audit fragments "
                   "missed; the control arms are unchanged",
            "record": f"archive/RESULTS-cycles3-4.md@{PIN[:7]}:{corr_a}-{corr_b} (the correction of record)"},
        "as_published": {
            "audit": "frozen (the rule at run time; data/e2a/analysis.json)",
            "reward": arm_block(frozen["reward"]),
            "interval_note": interval_note},
        "control_arms": {arm: arm_block(v2[arm]) for arm in ARMS if arm != "reward"},
        "definitions": {
            "delta_first": "k/n - 1/2, k = valid sessions whose first free pick was the +pole label, n = valid "
                           "sessions of the arm (scripts/e2a_recount.py primary(); extended here to the control arms "
                           "and asserted equal to data/e2a/analysis.json for all four arms under the frozen audit)",
            "binom_p_one_sided": "exact one-sided binomial P(X >= k | n, 1/2), 5 decimals (the record's rounding)",
            "wilson95": "95% two-sided Wilson score interval on the share k/n; the delta_first form subtracts 1/2",
        },
        "provenance": {
            "script": {"path": "scripts/audit_note_N4_record.py", "sha256": script_sha},
            "audit_raw_of_this_file": f"{RAW} (written by the same run, committed with this file)",
            "record_pin": PIN, "inputs_sha256_at_pin": in_shas,
            "repository_modules_imported_equal_to_pin": loaded,
            "item_raw": f"{N4_RAW}@{N4_AT}:{n4_v2} (audit v2), :{n4_fn} (the 54/101 row), :{n4_wil} (its Wilson "
                        f"interval), :{n4_ref4} (the record's interval and its method)",
            "routing": "PI routing of 2026-10-09 (the Digest seat's FLAG I and FLAG B)",
        },
    }
    with open(a.out_json, "w", encoding="utf-8") as fh:
        json.dump(art, fh, indent=1, ensure_ascii=False)
        fh.write("\n")

    def iv(x, d=4):
        return f"[{x[0]:.{d}f}, {x[1]:.{d}f}]"

    o = []
    w = o.append
    w("# AUDIT-note-release v1.2 -- N4 addendum: e2a's correction of record beside the artifact")
    w("")
    w(f"- Code stamp: {stamp} (date -u); HEAD `{head}` (informational). Every data and code input is read from the working tree and "
      f"asserted byte-equal to its blob at the record pin; the N4 item raw is read at {N4_AT}.")
    w(f"- Block `{BLOCK}` (N4 at :{blk}); record pin `{PIN}`")
    w(f"- Script `scripts/audit_note_N4_record.py` sha256 `{script_sha}`; interpreter {sys.executable} "
      f"(Python {sys.version.split()[0]})")
    w(f"- Routing: the PI's routing of 2026-10-09: record the audit-v2 e2a count as an artifact beside "
      f"`data/e2a/analysis.json` (the Digest seat's FLAG I) and add the control arms' Wilson intervals (FLAG B).")
    w(f"- Inputs, each asserted byte-equal to its blob at the pin: " +
      "; ".join(f"`{p}` sha256 `{s}`" for p, s in in_shas.items()) + ".")
    w(f"- The record's analyzer `scripts/e2a_recount.py` is imported read-only; the repository modules it loads, "
      f"each asserted equal to its pinned blob: {', '.join(f'`{p}`' for p in loaded)}.")
    w(f"- Wrote `{os.path.relpath(a.out_json, REPO)}` (the artifact) and `{os.path.relpath(a.out_md, REPO)}` (this "
      f"raw). `data/e2a/analysis.json` is not modified.")
    w("")
    w("## 1. The correction of record")
    w("")
    w(f"- As published (frozen audit, `data/e2a/analysis.json`): **{kf}/{nf}**, Δ_first "
      f"{frozen['reward']['delta_first']:+.4f}, one-sided exact binomial p {frozen['reward']['binom_p_one_sided']:.5f}; "
      f"Wilson 95% on the share {iv(frozen['reward']['wilson95_share'])}.")
    w(f"- Of record (audit v2, `data/configs/e2b_audit_v2.json`): **{kv}/{nv}**, Δ_first {rv['delta_first']:+.4f}, "
      f"p {rv['binom_p_one_sided']:.5f}; Wilson 95% on the share {iv(rv['wilson95_share'])}, on Δ_first "
      f"{iv(rv['wilson95_delta_first'])}. The one added exclusion is reward s{added[0]}; reward excluded "
      f"{byv['reward']}/112 under v2 against {byf['reward']}/112 frozen.")
    w(f"- The record calls the v2 count the correction of record at "
      f"archive/RESULTS-cycles3-4.md@{PIN[:7]}:{corr_a}-{corr_b}. The N4 item raw reproduced it at "
      f"{N4_RAW}@{N4_AT}:{n4_v2} and :{n4_fn}, and its Wilson interval at :{n4_wil}; this run agrees to every "
      f"printed digit.")
    w("")
    w("## 2. All four arms, with Wilson intervals (FLAG B)")
    w("")
    w("Under audit v2; the control arms are identical under both audits (asserted). Every frozen-audit n, Δ_first and "
      "p equals `data/e2a/analysis.json` (asserted).")
    w("")
    w("### 2(a) Counts, Δ_first and p (the record's analyzer over committed artifacts)")
    w("")
    w("| arm | k / n (first free pick +pole) | Δ_first | one-sided exact p | status |")
    w("|---|---|---|---|---|")
    rows_ = [(f"{arm}{' (of record)' if arm == 'reward' else ''}", v2[arm]) for arm in ARMS] + \
        [("reward (as published)", frozen["reward"])]
    for lab, r_ in rows_:
        w(f"| {lab} | {r_['k_plus_pole_first_pick']}/{r_['n_valid']} | {r_['delta_first']:+.4f} | "
          f"{r_['binom_p_one_sided']:.5f} | reproduced |")
    w("")
    w(f"### 2(b) Wilson 95% intervals (computed-new; the record names no interval method, "
      f"{N4_RAW}@{N4_AT}:{n4_ref4})")
    w("")
    w(interval_note)
    w("")
    w("| arm | k / n | Wilson 95%, share | Wilson 95%, Δ_first | status |")
    w("|---|---|---|---|---|")
    for lab, r_ in rows_:
        w(f"| {lab} | {r_['k_plus_pole_first_pick']}/{r_['n_valid']} | {iv(r_['wilson95_share'])} | "
          f"{iv(r_['wilson95_delta_first'])} | computed-new |")
    w("")
    w("Every interval contains 1/2." if all_contain_half else "NOT every interval contains 1/2.")
    w("")
    with open(a.out_md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(o) + "\n")
    print(f"wrote {os.path.relpath(a.out_json, REPO)} and {os.path.relpath(a.out_md, REPO)}")
    for arm in ARMS:
        r_ = v2[arm]
        print(arm, f"{r_['k_plus_pole_first_pick']}/{r_['n_valid']}", r_["delta_first"], r_["binom_p_one_sided"],
              iv(r_["wilson95_share"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
