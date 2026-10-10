#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N2 parts (i)-(v): introspection replication and
the criterion-shift claim (block lines 25-36). Part (vi) is the N2vi raw's.

Read-only on the record. Every repository read is `git show bbc9ffe:<path>`
(or another named commit, for blob-identity checks). The working-tree reads
are the N2(vi) item's JSON and raw and PREPRINT-v1_0-draft.md (the raw and
the preprint also for the pass-1 '97.5' substring search), all untracked at
bbc9ffe; their sha256 are printed (the N2vi paths:
results/raw/2026-10-08_note-N2vi-source.json and .md). The record's own
scorers, audit specs and analyzer functions are compiled from their bbc9ffe
source into isolated module namespaces: nothing is imported from the working
tree and nothing is modified. No model, no randomness, no network.

One input outside the record (section 2(d), post-hoc, approximate): the OLMo-3
base tokenizer.json in the local Hugging Face cache, loaded with the
`tokenizers` library's Tokenizer.from_str (a local JSON parse; no model, no
download). It is used only to emulate B2's 60-token cap on B2-r's stored
generations. Its path, size and sha256 are printed beside the run's own
tokenizer hashes from data/olmo/manifest.json@bbc9ffe; if the file or the
library is absent, the emulation is reported as not run (its ledger row is
omitted, so later rows number one lower, and the text that quotes its counts
says it did not run) and nothing else changes. Round 2 also reads, informationally, the installed `transformers`
decode signature (skip_special_tokens default; no model, no torch needed).

Round 2 adds Code's full read of the 42 affirm-scored B2-r control trials
(rule 25): the classification is declared in this file (READ_*), and the
script asserts it against the texts (every affirm match inside a declared
carrier; the scorer's own rule re-applied with the carriers blanked).

Round 4 (the third checker's six findings): ties the read to the record's
committed class definition (scorer_v3_spec.json class_level_spec.classes),
carries it to the 60-token cut, names the record's sense of 'degenerate'
(AUDIT.check), scopes N1's discrepant clause on the two pass-condition rows,
and cross-checks every 'theirs' row against the N2vi item's JSON and its raw
(results/raw/2026-10-08_note-N2vi-source.md, read-only, sha256 printed).

Round 5 (the fourth checker's three findings): the round-4 code runs only
where the emulation ran, so the tokenizer-absent path runs again; section 4's
read on the restricted set needs no tokenizer and is computed outside the
emulation; the working-tree inputs are listed in full, with the preprint's
sha256 printed; ledger rows 22 and 23 carry the SFT disclosure too.

Round 6 (the PI's routing of 2026-10-09, item 2): section 5(f) adds the source's
refusal-direction ablation rates (Gemma-3-27B; hits 10.8% -> 63.8%, false alarms
0% -> 7.3%; log-only record prose, no n) as their own rows, with the uncorrected
d' = z(H) - z(FA), no correction and no p (JSON: theirs_ablation_uncorrected).
Nothing else changes: the earlier sections regenerate byte for byte, except
pass 3 item 4's live row count (57 -> 60); pass 2 item 9 keeps the 57 rows the
ledger had at pass 2.

Writes the raw (--out) and the ROC JSON for the Draftsman seat (--json-out).
Both default to results/raw/; a checker can regenerate into scratch.

Usage:
    jlens-qwen36/.venv/bin/python scripts/audit_note_N2.py
    jlens-qwen36/.venv/bin/python scripts/audit_note_N2.py \
        --out /path/scratch/N2.md --json-out /path/scratch/N2.json
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import types
from dataclasses import dataclass, field
from fractions import Fraction
from statistics import NormalDist
from typing import Iterable, Sequence

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = "bbc9ffe72fb8a942431c9bf2622a36e581fdf93c"
P = "bbc9ffe"
BLOCK = "AUDIT-note-release-v1_2.md"
ROUTED_BLOCK_SHA = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
DEF_OUT = "results/raw/2026-10-08_note-N2-introspection.md"
DEF_JSON = "results/raw/2026-10-08_note-N2-roc.json"
N2VI_JSON = "results/raw/2026-10-08_note-N2vi-source.json"
N2VI_MD = "results/raw/2026-10-08_note-N2vi-source.md"
PREPRINT = "PREPRINT-v1_0-draft.md"     # working tree; read for the '97.5' search only (since pass 1)
PREPRINT_BLOCK_SHA = ("d6431e97", "222b8")   # the block's abbreviated sha for it (block :21)
STAGES = ("base", "sft", "dpo", "instruct")
EXP_STAGES = ("sft", "dpo", "instruct")
ASSUMED_N = (800, 80)          # design seat's per-configuration assumption, block :34
N_CONFIGS = 20                 # L in {25,32,38,45,51} x alpha in {1,2,4,8}; ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:38-39
POOLED_N = (ASSUMED_N[0] * N_CONFIGS, ASSUMED_N[1] * N_CONFIGS)   # the same premise, pooled
TOKENIZER = os.path.expanduser(
    "~/.cache/huggingface/hub/models--allenai--Olmo-3-1125-32B/snapshots/"
    "c2b61dae89a1ad10e4ad5653d0e46b590902607b/tokenizer.json")
CAP_EMU = 60                   # B2's max new tokens (scripts/box_b2_detection.py@bbc9ffe:129)
CAP_BRACKET = (55, 65)         # sensitivity of the emulation to the approximate cut
Z = NormalDist().inv_cdf


# ----------------------------------------------------------------- git reads
_cache: dict = {}


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", REPO, *args], check=True,
                          capture_output=True).stdout.decode("utf-8")


def show(path: str, rev: str = PIN) -> bytes:
    key = (rev, path)
    if key not in _cache:
        _cache[key] = subprocess.run(
            ["git", "-C", REPO, "show", f"{rev}:{path}"], check=True,
            capture_output=True).stdout
    return _cache[key]


def text(path: str, rev: str = PIN) -> str:
    return show(path, rev).decode("utf-8")


def jload(path: str, rev: str = PIN):
    return json.loads(text(path, rev))


def lines(path: str) -> list[str]:
    return text(path).split("\n")


def loc(path: str, a: int, b: int | None = None) -> str:
    return f"{path}@{P}:{a}" + (f"-{b}" if b and b != a else "")


def anchor(path: str, n: int, needle: str) -> int:
    ln = lines(path)[n - 1]
    if needle not in ln:
        raise AssertionError(f"anchor {path}@{P}:{n} lacks {needle!r}: {ln!r}")
    return n


def find(path: str, pattern: str, expect: int | None = 1) -> list[int]:
    rx = re.compile(pattern)
    hits = [i + 1 for i, ln in enumerate(lines(path)) if rx.search(ln)]
    if expect is not None and len(hits) != expect:
        raise AssertionError(f"{path}@{P}: /{pattern}/ matched {hits}, "
                             f"expected {expect}")
    return hits


def one(path: str, pattern: str) -> int:
    return find(path, pattern, 1)[0]


def blob(rev: str, path: str) -> str:
    return git("rev-parse", f"{rev}:{path}").strip()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


# ------------------------------------------- the record's code, compiled
def rec_module(tag: str, path: str, names: Sequence[str] | None = None,
               pre: dict | None = None) -> types.ModuleType:
    """Compile `path`@bbc9ffe (whole, or only the named top-level defs) into
    a fresh module object. The source is the record's, byte for byte; only the
    selection of top-level statements is ours."""
    src = text(path)
    tree = ast.parse(src)
    if names is None:
        body = tree.body
    else:
        body = [ast.ImportFrom(module="__future__",
                               names=[ast.alias(name="annotations")], level=0)]
        want, found = set(names), set()
        for node in tree.body:
            nm: set = set()
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                nm = {node.name}
            elif isinstance(node, ast.Assign):
                for t in node.targets:
                    if isinstance(t, ast.Name):
                        nm.add(t.id)
                    elif isinstance(t, ast.Tuple):
                        nm |= {e.id for e in t.elts if isinstance(e, ast.Name)}
            if nm & want:
                body.append(node)
                found |= nm & want
        if want - found:
            raise AssertionError(f"{path}@{P}: names not found {want - found}")
    mod = types.ModuleType(f"_audit_n2_record_{tag}")
    mod.__dict__.update(pre or {})
    sys.modules[mod.__name__] = mod
    code = compile(ast.fix_missing_locations(ast.Module(body=body, type_ignores=[])),
                   f"{path}@{P}", "exec")
    exec(code, mod.__dict__)
    return mod


def literal_constants(path: str, names: Sequence[str]) -> dict:
    out = {}
    for node in ast.parse(text(path)).body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id in names:
                    out[t.id] = ast.literal_eval(node.value)
    if set(names) - set(out):
        raise AssertionError(f"{path}: constants missing {set(names) - set(out)}")
    return out


# ------------------------------------------------------------ statistics
def dprime_ll(h: int, ns: int, fa: int, nn: int) -> tuple[float, float]:
    """Log-linear corrected d' and c: H' = (H+1/2)/(Ns+1), F' = (FA+1/2)/(Nn+1)."""
    hp, fp = (h + 0.5) / (ns + 1), (fa + 0.5) / (nn + 1)
    return Z(hp) - Z(fp), -(Z(hp) + Z(fp)) / 2


def fisher_hits_gt_fa(h: int, ns: int, fa: int, nn: int) -> float:
    """One-sided Fisher exact, H1: hit rate > FA rate. Table
    [[H, Ns-H], [FA, Nn-FA]], margins fixed; P(X >= H) under the
    hypergeometric. Exact integer arithmetic."""
    n, k = ns + nn, h + fa
    hi = min(ns, k)
    num = sum(math.comb(ns, x) * math.comb(nn, k - x) for x in range(h, hi + 1))
    return float(Fraction(num, math.comb(n, k)))


def half_up(x: Fraction) -> int:
    return math.floor(x + Fraction(1, 2))


def binom_pmf_exact(k: int, n: int, p: Fraction) -> Fraction:
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def fmt(x, nd=4, sign=False):
    if x is None:
        return "n/a"
    if isinstance(x, float) and x != x:
        return "nan"
    return f"{x:+.{nd}f}" if sign else f"{x:.{nd}f}"


def pfmt(p):
    if p is None:
        return "n/a"
    return f"{p:.4f}" if p >= 1e-4 else f"{p:.2e}"


def deep_eq(a, b, tol=1e-12) -> bool:
    if isinstance(a, tuple):
        a = list(a)
    if isinstance(b, tuple):
        b = list(b)
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(deep_eq(a[k], b[k], tol) for k in a)
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(deep_eq(x, y, tol) for x, y in zip(a, b))
    if isinstance(a, bool) or isinstance(b, bool):
        return a is b or a == b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a != a and b != b:
            return True
        return abs(a - b) <= tol
    return a == b


# ===================================================================== main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(REPO, DEF_OUT))
    ap.add_argument("--json-out", default=os.path.join(REPO, DEF_JSON))
    args = ap.parse_args()

    stamp = subprocess.run(["date", "-u"], check=True, capture_output=True
                           ).stdout.decode().strip()
    head = git("rev-parse", "HEAD").strip()
    assert git("rev-parse", P).strip() == PIN
    block_bytes = show(BLOCK)
    block_sha = sha256_bytes(block_bytes)
    block_lines = block_bytes.decode().split("\n")
    n_block_lines = len(block_lines) - (1 if block_lines[-1] == "" else 0)
    script_path = os.path.abspath(__file__)
    script_sha = sha256_bytes(open(script_path, "rb").read())
    n2vi_path = os.path.join(REPO, N2VI_JSON)
    n2vi_bytes = open(n2vi_path, "rb").read()
    n2vi = json.loads(n2vi_bytes)
    n2vi_tracked = bool(git("ls-tree", "--name-only", PIN, N2VI_JSON).strip())
    # round 4: the N2vi raw, read-only, for the theirs-row cross-check (section 5)
    n2vi_md_bytes = open(os.path.join(REPO, N2VI_MD), "rb").read()
    n2vi_md_lines = n2vi_md_bytes.decode("utf-8").split("\n")
    n2vi_md_tracked = bool(git("ls-tree", "--name-only", PIN, N2VI_MD).strip())
    # round 5: the preprint, read-only (the '97.5' search since pass 1); its sha256 printed from round 5
    pp_path = os.path.join(REPO, PREPRINT)
    pp_bytes = open(pp_path, "rb").read() if os.path.isfile(pp_path) else None
    pp_sha = sha256_bytes(pp_bytes) if pp_bytes is not None else None
    pp_tracked = bool(git("ls-tree", "--name-only", PIN, PREPRINT).strip())
    pp_block_match = (pp_sha is not None and pp_sha.startswith(PREPRINT_BLOCK_SHA[0])
                      and pp_sha.endswith(PREPRINT_BLOCK_SHA[1]))

    out: list[str] = []
    w = out.append
    figures: list[dict] = []
    notes: list[str] = []
    stops: list[dict] = []
    pi_items: list[str] = []

    def fig(figure, printed, source, status, note="", *, named):
        """`named` = where the figure is named: 'block :NN' (AUDIT block line),
        'RESULTS.md@bbc9ffe:NNNN' (the record), or 'computed-new' (Code's)."""
        assert status in ("reproduced", "log-only", "not found", "discrepant",
                          "computed-new")
        assert named.startswith(("block :", "RESULTS.md@", "computed-new")), named
        figures.append({"figure": figure, "named_in": named, "printed": printed,
                        "source": source, "status": status, "note": note})

    # block anchors for this item
    anchor(BLOCK, 25, "### N2.")
    anchor(BLOCK, 30, "base 0.431 = 58/96")
    anchor(BLOCK, 31, "(ii) Reproduce the greedy run")
    anchor(BLOCK, 32, "178 decidable trials")
    anchor(BLOCK, 33, "(iv) Name the scorer of record")
    anchor(BLOCK, 34, "(v) Produce the F2 data")
    anchor(BLOCK, 36, "*Pass:* (i)")
    anchor(BLOCK, 23, "is a STOP on that item if it is not")     # N1's discrepant clause (round 4)
    anchor(BLOCK, 18, "### N1. Claims ledger")
    anchor(BLOCK, 21, f"`{PREPRINT}` at root (post-patch-v4 copy, sha `{PREPRINT_BLOCK_SHA[0]}…"
                      f"{PREPRINT_BLOCK_SHA[1]}`)")                  # the preprint's stated sha (round 5)
    assert n2vi["record_commit"] == PIN and n2vi["block"]["sha256"] == block_sha

    # ---------------------------------------------------- record code
    stats = rec_module("stats", "valence_core/stats.py")
    b2a = rec_module("b2_analyze", "scripts/b2_analyze.py",
                     ["STAGES", "ALPHA", "clopper_pearson", "newcombe", "AXIS",
                      "cell", "read_pattern", "analyze"],
                     {"binom_cdf": stats.binom_cdf,
                      "binom_sf_inclusive": stats.binom_sf_inclusive})
    v2 = rec_module("detection_v2", "valence_core/detection_v2.py")
    v1 = rec_module("detection", "valence_core/detection.py",
                    ["MACAR_FRAMING", "ACK", "TRIAL_QUESTION",
                     "COMPLETION_TEMPLATE", "_AFFIRM", "_DENY",
                     "claims_detection", "identifies_concept", "TURN_MARKERS",
                     "segment_own_turn"],
                    {"re": re, "Sequence": Sequence})
    b2ra = rec_module("b2r_analyze", "scripts/b2r_analyze.py",
                      ["STAGES", "HIGH", "LOW", "CONTROL_FLOOR", "EXPLORE_FLOOR",
                       "separates_above", "g3a", "g3b", "explore"],
                      {"clopper_pearson": b2a.clopper_pearson,
                       "newcombe": b2a.newcombe, "ci_state": v2.ci_state})
    ses = rec_module("session_auditspec", "valence_core/session.py",
                     ["AuditSpec", "DEFAULT_SCAFFOLD_STRINGS"],
                     {"re": re, "dataclass": dataclass, "field": field})
    A_B2 = rec_module("b2_runner_audit", "scripts/box_b2_detection.py",
                      ["AUDIT"], {"AuditSpec": ses.AuditSpec}).AUDIT
    A_B2R = rec_module("b2r_runner_audit", "scripts/box_b2r_campaign.py",
                       ["AUDIT"], {"AuditSpec": ses.AuditSpec}).AUDIT
    b2_prompt = rec_module("b2_prompt", "scripts/box_b2_detection.py",
                           ["build_prompt_arm"],
                           {"COMPLETION_TEMPLATE": v1.COMPLETION_TEMPLATE,
                            "ACK": v1.ACK})
    b2r_prompt = rec_module("b2r_prompt", "scripts/box_b2r_campaign.py",
                            ["trial_prompt"],
                            {"COMPLETION_TEMPLATE": v1.COMPLETION_TEMPLATE,
                             "MACAR_FRAMING": v1.MACAR_FRAMING, "ACK": v1.ACK})
    C_B2R = literal_constants("scripts/box_b2r_campaign.py",
                              ["L_M", "TEMP", "MAX_TOKENS", "CONTROL_N",
                               "CONTROL_FLOOR", "EXPLORE_N", "EXPLORE_FLOOR",
                               "LADDER"])
    C_B2 = literal_constants("scripts/box_b2_detection.py", ["FLOOR", "N_TRIALS"])

    def pipe_v1(raw: str):
        own = v1.segment_own_turn(raw)
        r = A_B2.check(own)
        return own, r, (None if r else v1.claims_detection(own))

    def pipe_v2(raw: str):
        own = v2.segment_own_turn_v2(raw)
        r = A_B2R.check(own)
        return own, r, (None if r else v2.claims_detection_v2(own))

    # ---------------------------------------------------- record data
    ctl = {s: jload(f"data/olmo/b2r_control_{s}.json") for s in STAGES}
    exp = {s: jload(f"data/olmo/b2r_explore_{s}.json") for s in EXP_STAGES}
    qual = {s: jload(f"data/olmo/b2r_qualify_{s}.json") for s in STAGES}
    an_r = jload("data/olmo/b2r_analysis.json")
    b2 = {arm: {s: jload(f"data/olmo/b2_{arm}_{s}.json") for s in STAGES}
          for arm in ("fidelity", "register")}
    an_b2 = jload("data/olmo/b2_analysis.json")
    spec = jload("data/configs/scorer_v3_spec.json")
    framing_cfg = jload("data/configs/b2_framing.json")

    # code line locators (searched, asserted unique)
    R2 = "scripts/box_b2_detection.py"
    RR = "scripts/box_b2r_campaign.py"
    AD = "valence_core/adapters/olmo_hf.py"
    D1 = "valence_core/detection.py"
    D2 = "valence_core/detection_v2.py"
    BA = "scripts/b2_analyze.py"
    BRA = "scripts/b2r_analyze.py"
    SE = "valence_core/session.py"
    L = {
        "b2_temp": one(R2, r"seed=args\.seed \+ n, temp=0\.0"),
        "b2_maxtok": one(R2, r'"--max-tokens", type=int, default=60'),
        "b2_seed": one(R2, r'"--seed", type=int, default=20260823'),
        "b2_seg": one(R2, r"own = segment_own_turn\(g\.text\)"),
        "b2_claim": one(R2, r"claim = None if reason else claims_detection\(own\)"),
        "b2_audit": one(R2, r"^AUDIT = AuditSpec\("),
        "b2_nostop": one(R2, r"max_tokens=args\.max_tokens, stop_newline=False"),
        "b2_floor": one(R2, r"^FLOOR = 16"),
        "rr_temp": one(RR, r"^TEMP = 1\.0"),
        "rr_maxtok": one(RR, r"^MAX_TOKENS = 100"),
        "rr_seed": one(RR, r'"--seed", type=int, default=20260824'),
        "rr_ctl_gen": find(RR, r"seed=args\.seed \+ n, temp=TEMP,", 2)[0],
        "rr_seg": find(RR, r"own = segment_own_turn_v2\(g\.text\)", 4),
        "rr_ctl_claim": one(RR, r"claim = None if reason else claims_detection_v2\(own\)"),
        "rr_exp_claim": one(RR, r'"claimed_detection": None if reason else claims_detection_v2\(own\)'),
        "rr_audit": one(RR, r"^AUDIT = AuditSpec\("),
        "rr_dec_ctl": one(RR, r'dec = \[t for t in trials if t\["claimed_detection"\] is not None\]'),
        "rr_dec_exp": one(RR, r'inj = \[t for t in trials if t\["injected"\] and t\["claimed_detection"\] is not None\]'),
        "rr_explore_def": one(RR, r"^def run_explore"),
        "rr_control_def": one(RR, r"^def run_control"),
        "rr_ctl_loop": one(RR, r"for n in range\(1, CONTROL_N \+ 1\):"),
        "rr_exp_loop": one(RR, r"for n, concept, is_inj in plan_trials\(names, EXPLORE_N, args\.seed\):"),
        "rr_exp_gen": find(RR, r"seed=args\.seed \+ n, temp=TEMP", 2),
        "ad_seed": one(AD, r"^\s+t\.manual_seed\(seed\)"),
        "ad_greedy": one(AD, r"if temp <= 0\.0:"),
        "ad_softmax": one(AD, r"probs = t\.softmax\(lg / temp, dim=-1\)"),
        "ad_multinom": one(AD, r"return int\(t\.multinomial\(probs, 1\)\.item\(\)\)"),
        "ad_ban": one(AD, r"lg\[ban_ids\] = -1e30"),
        "ad_stop": one(AD, r"def _is_stop\("),
        "ad_gen": one(AD, r"def generate\("),
        "ad_loop": one(AD, r"^\s+for step in range\(max_tokens\):"),
        "ad_append": one(AD, r"^\s+ids\.append\(tok\)"),
        "d1_template": one(D1, r'^COMPLETION_TEMPLATE = '),
        "d1_claims": one(D1, r"^def claims_detection\("),
        "d1_seg": one(D1, r"^def segment_own_turn\("),
        "d2_claims": one(D2, r"^def claims_detection_v2\("),
        "d2_seg": one(D2, r"^def segment_own_turn_v2\("),
        "d2_strip": one(D2, r"^def strip_conditionals\("),
        "d2_cistate": one(D2, r"^def ci_state\("),
        "ba_cp": one(BA, r"^def clopper_pearson\("),
        "ba_newc": one(BA, r"^def newcombe\("),
        "ba_cell": one(BA, r"^def cell\("),
        "bra_g3a": one(BRA, r"^def g3a\("),
        "bra_g3b": one(BRA, r"^def g3b\("),
        "bra_explore": one(BRA, r"^def explore\("),
        "bra_cfloor": one(BRA, r"^CONTROL_FLOOR = 64"),
        "bra_efloor": one(BRA, r"^EXPLORE_FLOOR = 32"),
        "se_scaffold": one(SE, r"^DEFAULT_SCAFFOLD_STRINGS = "),
        "se_ban": one(SE, r"^def build_ban_list\("),
        "rb2r_explore": one("scripts/run_b2r.sh", r"--part explore --stage"),
        "rb2r_control": one("scripts/run_b2r.sh", r"--part control --stage"),
        "rbp_b2": one("scripts/run_bphase.sh", r"box_b2_detection\.py --stage"),
        "b2_plan": one(R2, r"for n, concept, injected in plan_trials\(names, args\.n_trials, args\.seed\):"),
        "ad_decode": one(AD, r"^\s+def decode\(self, ids"),
        # round 4: the record's 'degenerate' = AUDIT.check-flagged ([g3-B] qualify rows)
        "rr_degen": find(RR, r'"degen": bool\(AUDIT\.check\(own\)\)', 2),
        "rr_degen_nd": one(RR, r'nd = sum\(1 for r in rows if r\["degen"\]\)'),
        "rr_degen_frac": one(RR, r'"degenerate_frac": nd / len\(rows\)'),
    }
    anchor(AD, L["ad_decode"] + 1, "return self._tok.decode(list(ids))")
    # end of the two scoring functions (for ranges)
    d2_claims_end = L["d2_claims"] + 17
    anchor(D2, d2_claims_end, "return None")
    rr_ctl_gen_line = L["rr_ctl_gen"]
    anchor(RR, rr_ctl_gen_line + 1, "max_tokens=MAX_TOKENS, stop_newline=False")
    anchor(RR, rr_ctl_gen_line + 2, "cached=False")
    anchor(RR, L["rr_audit"] + 4, "junk_regex=")
    anchor(RR, L["rr_dec_exp"] + 1, "ctl = [t for t in trials if not t[\"injected\"] and t[\"claimed_detection\"] is not None]")
    anchor(AD, L["ad_seed"] - 1, "if seed is not None:")
    assert L["ad_greedy"] < L["ad_softmax"] < L["ad_multinom"] and L["ad_loop"] < L["ad_append"]
    # the block names g3a, never g3b (the only 'g3-b' substring is the addendum's file name)
    assert not re.search(r"g3b|\[g3-B\]", text(BLOCK)) and \
        all("ADDENDUM-g3-b2r" in m_.string[max(0, m_.start() - 9):m_.end() + 4]
            for m_ in re.finditer(r"g3-b", text(BLOCK), re.I))
    anchor("scripts/run_bphase.sh", L["rbp_b2"] + 1, "--out")
    # the explore and control invocations pass no --seed
    for k in ("rb2r_explore", "rb2r_control"):
        ln = lines("scripts/run_b2r.sh")[L[k] - 1]
        nxt = lines("scripts/run_b2r.sh")[L[k]]
        assert "--seed" not in ln and "--seed" not in nxt
    ln = lines("scripts/run_bphase.sh")[L["rbp_b2"] - 1] + \
        lines("scripts/run_bphase.sh")[L["rbp_b2"]]
    assert "--max-tokens" not in ln and "--seed" not in ln

    # RESULTS / ADDENDUM anchors
    RS = "RESULTS.md"
    AG = "ADDENDUM-g3-b2r-v1.2.md"
    A = {
        "r_disp": anchor(RS, 6880, "B2-r DISPOSITION"),
        "r_base_5896": anchor(RS, 6899, "Base (0.431, 58/96)"),
        "r_flag3_sep": anchor(RS, 6902, "(0.1023 > 0.0397)"),
        "r_25pts_a": anchor(RS, 6908, "within 2.5 points of their SFT rate"),
        "r_25pts_b": anchor(RS, 6909, "0.225)"),
        "r_medc": anchor(RS, 6919, "MED_c reports as"),
        "r_any_kind_a": anchor(RS, 6951, "zero detection claims of any kind"),
        "r_any_kind_b": anchor(RS, 6952, "decidable trials each"),
        "r_p28_a": anchor(RS, 6955, "(p ≈ .28)"),
        "r_complete": anchor(RS, 6977, "B2-r COMPLETE"),
        "r_temp0": anchor(RS, 6980, "At temperature 0 Base"),
        "r_temp0b": anchor(RS, 6981, "false-alarmed 0/20; at temperature 1.0, with format, framing, checkpoint and"),
        "r_temp0c": anchor(RS, 6982, "prompt unchanged, it false-alarms 25/58 = 0.431"),
        "r_tab_base": anchor(RS, 6996, "**0.4310** (25/58)"),
        "r_tab_sft": anchor(RS, 6997, "**0.2000** (17/85)"),
        "r_tab_dpo": anchor(RS, 6998, "**0.0000** (0/91)"),
        "r_tab_inst": anchor(RS, 6999, "| 0.003 | 91/96 |"),
        "r_2of42": anchor(RS, 7058, "**2 of 42** affirm-scored"),
        "r_0176": anchor(RS, 7061, "SFT FPR 0.200 → 0.176 corrected"),
        "r_exp_sft": anchor(RS, 7081, "| sft | .3000 (12/40) | .2045 (9/44) | +0.0955 | [−.105, +.292] | includes |"),
        "r_exp_dpo": anchor(RS, 7082, "**.0000 (0/43)** | **.0000 (0/45)**"),
        "r_exp_inst": anchor(RS, 7083, "**.0000 (0/44)** | **.0000 (0/45)**"),
        "r_88_89": anchor(RS, 7086, "across 88 and 89 decidable trials"),
        "r_p28_b": anchor(RS, 7091, "(p ≈ 0.28)"),
        "r_template": anchor(RS, 7628, "fidelity-of-text"),
        "r_line198": anchor(RS, 7636, "`box_b2_detection.py:198` hardcodes **`temp=0.0`**"),
        "r_seedinert": anchor(RS, 7641, "`seed=args.seed + n` is INERT at"),
        "r_60": anchor(RS, 7645, "`max_new_tokens` 100 theirs vs 60 ours"),
        "r_b2_complete": anchor(RS, 7719, "B2 COMPLETE, EIGHT CELLS"),
        "r_b2_fid": anchor(RS, 7735, "| **fidelity** |"),
        "r_b2_reg": anchor(RS, 7736, "| **register** |"),
        "r_b2_reg44": anchor(RS, 7782, "hit 4/4, FA 0/1, **+1.000**"),
        "a_ran0": anchor(AG, 31, "ours ran 0.0"),
        "a_fot": anchor(AG, 75, "**fidelity-of-text, not fidelity-of-format**"),
        "a_dec": anchor(AG, 89, "**0.5 Decoding of record, all parts:** temperature 1.0"),
        "a_dv": anchor(AG, 139, "**DV, scorer v2**"),
        "a_floor": anchor(AG, 142, "Floors: ≥64/96 decidable per stage"),
        "a_medc": anchor(AG, 199, "**MED_c per stage = lowest strength passing both.**"),
        "a_fresh": anchor(AG, 220, "permutation, fresh declared seed)"),
        "a_fresh0": anchor(AG, 219, "**Trials:** n = 96 per stage (48 injected / 48 control, seeded"),
        "a_percfg": anchor(AG, 32, "~800 injected / ~80 control per config"),
        "a_pooled_a": anchor(AG, 38, "**0.2 The recovered result the control must now aim at.**"),
        "a_pooled_b": anchor(AG, 39, "aggregated over L ∈ [25,32,38,45,51], α ∈ [1,2,4,8]"),
        "r_v1affirm": anchor(RS, 7767, "`_AFFIRM` contains bare substrings"),
        "r_v1affirm_b": anchor(RS, 7768, "`'detecting'` matches"),
        "r_b2_reg_ci": anchor(RS, 7786, "spans −0.288 to +1.000"),
        "a_exdv": anchor(AG, 227, "**DV:** scorer v2"),
        "a_exfloor": anchor(AG, 228, "Floors ≥32/48 per cell"),
        "a_ctl": anchor(AG, 126, "## 1. CONTROL"),
        "a_base_ext": anchor(AG, 71, "Base: their bare base-model template"),
        "a_inst_row": anchor(AG, 46, "| instruct | 0.9% | 0.3% | +0.6 pp |"),
        "r_chat": anchor(RS, 7620, "Chat template, pinned"),
        "r_chat_end": anchor(RS, 7630, "Rule 13 stands"),
        "r_reg_def": anchor(RS, 7776, "The register arm scores in a vocabulary"),
        "r_reg_def_end": anchor(RS, 7786, "spans −0.288 to +1.000"),
        # round 2: the source's decoding as the record states it; ADDENDUM §0.5; FLAG-3's text and class ruling
        "r_theirs_T_a": anchor(RS, 7634, "Theirs: `DEFAULT_TEMPERATURE = 1.0`"),
        "r_theirs_T_b": anchor(RS, 7635, "default `temperature: float = 1.0`"),
        "a_dec_b": anchor(AG, 90, "100 — their OLMo experiment's declared parameters"),
        "a_dec_c": anchor(AG, 91, "`DEFAULT_TEMPERATURE = 1.0`"),
        "a_dec_all_a": anchor(AG, 95, "Decoding parameters are measurement"),
        "a_dec_all_b": anchor(AG, 96, "this addendum names all of them"),
        "r_flag3_a": anchor(RS, 7054, "FLAG 3 — a defect in scorer v2"),
        "r_2of42_b": anchor(RS, 7059, "control trials, both at SFT"),
        "r_flag3_class_a": anchor(RS, 6923, "FLAG 3 RULED"),
        "r_flag3_class_b": anchor(RS, 6931, "generation different"),
        "r_flag3_class_mid": anchor(RS, 6927, "non-asserting contexts AS A CLASS"),
        "a_sft_row": anchor(AG, 44, "| sft | 14.9% | 22.5% |"),
        "r_src_def_a": anchor(RS, 7433, "`DEFAULT_TEMPERATURE = 1.0`, `DEFAULT_MAX_TOKENS = 100`"),
        "r_src_def_n": anchor(RS, 7436, '("so 10×10 = 100 per concept"), `DEFAULT_CONTROL_SAMPLES_PER_TRIAL = 1`'),
        "r_src_def_n0": anchor(RS, 7435, "`DEFAULT_SAMPLES_PER_TRIAL = 10`"),
        # round 4: the record's eight-concept premise for ~800/~80
        "r_src_8a": anchor(RS, 7438, "With eight"),
        "r_src_8b": anchor(RS, 7439, "~800 injected / ~80 control per (layer, strength)"),
        "r_src_8c": anchor(RS, 7440, "cell** against our 24/24"),
    }
    arc_head = anchor("results/raw/2026-08-25_b2r_arc.txt", 5, "repo head : 745c196")
    assert not find(R2, r"--temp", None)          # no temperature argument exists in the B2 runner
    for s_ in STAGES:
        assert qual[s_]["temp"] == 1.0 and qual[s_]["max_tokens"] == 100
    ba_dprime = one(BA, r"^SENSITIVITY = hit - false alarm\. d' is NOT computed")
    rule11 = one("CLAUDE.md", r"^11\. Post-hoc analyses labeled post-hoc")
    rule25 = one("CLAUDE.md", r"^25\. \[v3-new\] \*\*Read-everything clause")

    # referents' working-tree state vs bbc9ffe (read-only diff)
    referents = ["scripts/b2_analyze.py", "scripts/b2r_analyze.py",
                 "scripts/box_b2_detection.py", "scripts/box_b2r_campaign.py",
                 "scripts/b2r_scorer_selftest.py", "scripts/run_b2r.sh",
                 "scripts/run_bphase.sh", "valence_core/detection.py",
                 "valence_core/detection_v2.py", "valence_core/stats.py",
                 "valence_core/session.py", "valence_core/adapters/olmo_hf.py",
                 "data/configs/b2_concepts.json", "data/configs/b2_framing.json",
                 "data/configs/scorer_v3_spec.json", "data/configs/b2r_step1.json",
                 "data/olmo", "ADDENDUM-g3-b2r-v1.2.md", "RESULTS.md", "CLAUDE.md"]
    wt = subprocess.run(["git", "-C", REPO, "diff", "--name-only", PIN, "--",
                         *referents], check=True, capture_output=True
                        ).stdout.decode().split()

    # ---------------------------------------------- analyzers reproduce
    ctl_counts = {s: {"affirm": ctl[s]["affirm"], "decidable": ctl[s]["decidable"]}
                  for s in STAGES}
    g3a_re = b2ra.g3a(ctl_counts)
    g3b_re = {s: b2ra.g3b({"control": {"about": qual[s]["control"]["about"],
                                       "n": qual[s]["control"]["n"]},
                           "injected": {k: {"about": v["about"], "n": v["n"],
                                            "degenerate_frac": v["degenerate_frac"]}
                                        for k, v in qual[s]["injected"].items()}})
              for s in STAGES}
    exp_re = {s: b2ra.explore(exp[s]) for s in EXP_STAGES}
    rep_g3a = deep_eq(g3a_re, an_r["g3a"])
    rep_g3b = deep_eq(g3b_re, an_r["g3b"])
    rep_exp = deep_eq(exp_re, an_r["explore"])
    cells, axis = {}, {}
    for arm in ("fidelity", "register"):
        for s in STAGES:
            cells[f"{s}-{arm}"] = b2a.cell(b2[arm][s], "macar_eight")
            if arm == "fidelity":
                axis[s] = b2a.cell(b2[arm][s], "axis")
    an_b2_re = b2a.analyze(cells, axis)
    rep_b2 = deep_eq(an_b2_re, an_b2)

    # ---------------------------------------------- replay of the scorers
    replay = {}
    for arm in ("fidelity", "register"):
        for s in STAGES:
            mm = sum(1 for t in b2[arm][s]["trials"]
                     if pipe_v1(t["response_raw"]) != (t["response"], t["audit"],
                                                       t["claimed_detection"]))
            replay[f"B2 {arm} {s}"] = (mm, len(b2[arm][s]["trials"]))
    for s in STAGES:
        mm = sum(1 for t in ctl[s]["trials"]
                 if pipe_v2(t["response_raw"]) != (t["response"], t["audit"],
                                                   t["claimed_detection"]))
        replay[f"B2-r control {s}"] = (mm, len(ctl[s]["trials"]))
    for s in EXP_STAGES:
        mm = sum(1 for t in exp[s]["trials"]
                 if pipe_v2(t["response_raw"]) != (t["response"], t["audit"],
                                                   t["claimed_detection"]))
        replay[f"B2-r explore {s}"] = (mm, len(exp[s]["trials"]))
    replay_ok = all(v[0] == 0 for v in replay.values())
    # scorer of record for B2, established from the artifacts: which pipeline
    # re-derives the stored claimed_detection? (v1 should: 0 mismatches; v2 is
    # the discriminating alternative.)
    b2_cd_v1 = b2_cd_v2 = b2_cd_n = 0
    for arm in ("fidelity", "register"):
        for s in STAGES:
            for t in b2[arm][s]["trials"]:
                b2_cd_n += 1
                b2_cd_v1 += pipe_v1(t["response_raw"])[2] != t["claimed_detection"]
                b2_cd_v2 += pipe_v2(t["response_raw"])[2] != t["claimed_detection"]
    assert b2_cd_v1 == 0 and b2_cd_v2 > 0

    # ------------------- B2's 60-token cap emulated on B2-r (outside the record)
    # The adapter seeds once per trial and draws tokens one at a time; the cap
    # only ends the loop (valence_core/adapters/olmo_hf.py@bbc9ffe:220-221,
    # :265-280). So a 60-cap run at the same seed is the first 60 generated
    # tokens of the 100-cap run. The artifacts store text, not token ids, so the
    # cut is made on a re-encoding of `response_raw`: approximate.
    manifest = jload("data/olmo/manifest.json")
    run_tok = {s: (manifest[s]["files"]["tokenizer.json"]["sha256"],
                   manifest[s]["files"]["tokenizer.json"]["bytes"]) for s in STAGES}
    emu: dict = {"run": False, "reason": None, "path": TOKENIZER,
                 "run_tokenizer_json_sha256_bytes_by_stage": run_tok}
    tok_real = os.path.realpath(TOKENIZER)
    emu_own60: dict = {}
    try:
        import tokenizers as _tkmod
        from tokenizers import Tokenizer as _HFTok
    except Exception as exc:                      # library absent: not run
        _HFTok = None
        emu["reason"] = f"the tokenizers library is not importable ({type(exc).__name__})"
    if _HFTok is not None and not os.path.isfile(tok_real):
        emu["reason"] = f"no tokenizer file at {TOKENIZER}"
    elif _HFTok is not None:
        tbytes = open(tok_real, "rb").read()
        tk = _HFTok.from_str(tbytes.decode("utf-8"))
        emu.update(run=True, realpath=tok_real, sha256=sha256_bytes(tbytes), bytes=len(tbytes),
                   library=f"tokenizers {_tkmod.__version__}",
                   equals_run_tokenizer_at=[s for s in STAGES if run_tok[s][0] == sha256_bytes(tbytes)])

        def enc(raw: str) -> list[int]:
            return tk.encode(raw, add_special_tokens=False).ids

        def dec(ids: list[int], skip: bool = False) -> str:
            return tk.decode(ids, skip_special_tokens=skip)

        # round 2: the library defaults, read from the installed packages (not
        # the run's; the run's versions are in the artifacts' provenance)
        tok_doc = (_HFTok.decode.__doc__ or "")
        m_ = re.search(r"skip_special_tokens \(:obj:`bool`, defaults to :obj:`(True|False)`\)", tok_doc)
        emu["tokenizers_decode_default_skip_special_tokens"] = (m_.group(1) == "True") if m_ else None
        try:
            import inspect as _insp
            import logging as _lg
            _lg.disable(_lg.WARNING)
            import transformers as _tf
            from transformers import PreTrainedTokenizerBase as _PTB
            _lg.disable(_lg.NOTSET)
            emu["transformers_local"] = {
                "version": _tf.__version__,
                "decode_default_skip_special_tokens":
                    _insp.signature(_PTB.decode).parameters["skip_special_tokens"].default}
        except Exception as exc:                  # informational only
            emu["transformers_local"] = {"version": None, "reason": type(exc).__name__}
        emu["run_transformers_version"] = ctl["base"]["provenance"]["library_versions"]["transformers"]
        specials = ("<|endoftext|>", "<|im_end|>", "<|im_start|>")

        per: dict = {}
        for s in STAGES:
            ids_all = [enc(t["response_raw"]) for t in ctl[s]["trials"]]
            rt = sum(dec(i) == t["response_raw"] for i, t in zip(ids_all, ctl[s]["trials"]))
            rt_skip = sum(dec(i, True) == t["response_raw"] for i, t in zip(ids_all, ctl[s]["trials"]))
            rt_skip_fail = [{"trial": t["trial"], "literal_special_strings": [x for x in specials if x in t["response_raw"]],
                             "first_literal_char_offset": min(t["response_raw"].find(x) for x in specials
                                                              if x in t["response_raw"]),
                             "tokens_before_literal": len(enc(t["response_raw"][:min(
                                 t["response_raw"].find(x) for x in specials if x in t["response_raw"])]))}
                            for i, t in zip(ids_all, ctl[s]["trials"]) if dec(i, True) != t["response_raw"]]
            assert all(r_["literal_special_strings"] for r_ in rt_skip_fail)
            cuts_skip_equal = all(
                [pipe_v2(dec(i[:cap], True).strip())[2] for i in ids_all] ==
                [pipe_v2(dec(i[:cap]).strip())[2] for i in ids_all] and
                [pipe_v1(dec(i[:cap], True).strip())[2] for i in ids_all] ==
                [pipe_v1(dec(i[:cap]).strip())[2] for i in ids_all]
                for cap in (CAP_BRACKET[0], CAP_EMU, CAP_BRACKET[1]))
            b2_all = [t for arm in ("fidelity", "register") for t in b2[arm][s]["trials"]]
            b2_ids = [enc(t["response_raw"]) for t in b2_all]
            res = {}
            for cap in (CAP_BRACKET[0], CAP_EMU, CAP_BRACKET[1]):
                txt = [dec(i[:cap]).strip() for i in ids_all]
                c2 = [pipe_v2(x)[2] for x in txt]
                c1 = [pipe_v1(x)[2] for x in txt]
                res[cap] = {"v2": [c2.count(True), sum(x is not None for x in c2)],
                            "v1": [c1.count(True), sum(x is not None for x in c1)]}
            # round 4: which trials false-alarm at the 60 cut (v2), and their segmented cut text
            p60_ = [pipe_v2(dec(i[:CAP_EMU]).strip()) for i in ids_all]
            emu_own60[s] = {t["trial"]: pp[0] for t, pp in zip(ctl[s]["trials"], p60_) if pp[2] is True}
            assert len(emu_own60[s]) == res[CAP_EMU]["v2"][0]
            fa_r, n_r = res[CAP_EMU]["v1"]
            fa_b = sum(1 for t in b2["fidelity"][s]["trials"]
                       if not t["injected"] and t["claimed_detection"] is True)
            n_b = b2["fidelity"][s]["decidable_n_floors"]["control_decidable"]
            p_ = fisher_hits_gt_fa(fa_r, n_r, fa_b, n_b)
            assert abs(p_ - stats.fisher_one_sided(fa_r, n_r - fa_r, fa_b, n_b - fa_b)) < 1e-12
            per[s] = {"b2r_control_trials": len(ids_all), "roundtrip_identical": rt,
                      "roundtrip_identical_skip_special_tokens_true": rt_skip,
                      "roundtrip_fails_with_skip_true": rt_skip_fail,
                      "cut_verdicts_equal_under_both_decode_settings": cuts_skip_equal,
                      "reencoded_len_max": max(len(i) for i in ids_all),
                      "reencoded_len_over_100": sum(len(i) > C_B2R["MAX_TOKENS"] for i in ids_all),
                      "reencoded_len_over_60": sum(len(i) > CAP_EMU for i in ids_all),
                      "b2_trials_calibration": len(b2_ids),
                      "b2_reencoded_len_over_60": sum(len(i) > CAP_EMU for i in b2_ids),
                      "b2_reencoded_len_max": max(len(i) for i in b2_ids),
                      "fa_decidable_by_cap": {str(k): v for k, v in res.items()},
                      "fa_trials_v2_cut60": sorted(emu_own60[s]),
                      "b2_fidelity_control_v1_recorded": [fa_b, n_b],
                      "fisher_p_one_sided_cap60_v1_vs_b2_greedy_v1": p_}
        emu["per_stage"] = per

    # recount from trials
    for s in STAGES:
        tr = ctl[s]["trials"]
        assert sum(1 for t in tr if t["claimed_detection"] is True) == ctl[s]["affirm"]
        assert sum(1 for t in tr if t["claimed_detection"] is not None) == ctl[s]["decidable"]
        assert len(tr) == ctl[s]["n"] == C_B2R["CONTROL_N"]
        assert all(not t["injected"] for t in tr)
        assert all(t["seed"] == ctl[s]["seed"] + t["trial"] for t in tr)
        assert ctl[s]["temp"] == C_B2R["TEMP"] and ctl[s]["max_tokens"] == C_B2R["MAX_TOKENS"]
    for s in EXP_STAGES:
        tr = exp[s]["trials"]
        inj = [t for t in tr if t["injected"] and t["claimed_detection"] is not None]
        cc = [t for t in tr if not t["injected"] and t["claimed_detection"] is not None]
        assert sum(1 for t in inj if t["claimed_detection"]) == exp[s]["hit"]
        assert len(inj) == exp[s]["inj_decidable"]
        assert sum(1 for t in cc if t["claimed_detection"]) == exp[s]["fa"]
        assert len(cc) == exp[s]["ctl_decidable"]
        assert all(t["seed"] == exp[s]["seed"] + t["trial"] for t in tr)
        assert exp[s]["temp"] == 1.0 and exp[s]["max_tokens"] == 100

    # ------------- round 2: Code's read of every affirm-scored control (rule 25)
    # All 42 affirm-scored B2-r section 1 control trials (25 base + 17 SFT) were
    # read in full by Code. The classification below is that reading (post-hoc,
    # descriptive; it is not an instrument and relabels nothing of record). For
    # every trial NOT read as an assertion, the declared carrier phrases are
    # asserted to contain every v2 affirm match on the scorer's own input
    # (" " + strip_conditionals(response).strip().lower()), and the scorer's own
    # three-way rule is re-applied with those carriers blanked.
    READ_NON_ASSERTING = {   # FLAG-3's class (non-asserting contexts) at base: embedded complements / a question
        ("base", 8): ["whether i detect an injected thought"],
        ("base", 33): ["how well i can detect when they inject"],
        ("base", 34): ["how well i can detect when they inject", "how can i detect these thought injections?"],
        ("base", 35): ["how well i detect when they inject"],
        ("base", 36): ["whether i am able to detect an injected thought"],
        ("base", 44): ["whether i can detect when they inject"],
        ("base", 49): ["how well i can detect when they inject"],
        ("base", 89): ["how well i can detect when they inject"],
    }
    READ_AMBIGUOUS = {
        ("base", 94): ["yes, i can try various prompts to figure this out",
                       "response 1: yes, in the context of language"],
        ("sft", 5): ["yes, as an ai, i process and detect thoughts or requests"],
    }
    READ_FLAG3 = {           # the record's two (data/configs/scorer_v3_spec.json regression_cases)
        ("sft", 16): ["i do not believe there is an injected thought"],
        ("sft", 76): ["i will let you know when i can detect an injected thought"],
    }
    READ_SPEC = {**{k: ("non-asserting (embedded complement)" if k != ("base", 34) else
                        "non-asserting (embedded complement; a direct question)", v)
                    for k, v in READ_NON_ASSERTING.items()},
                 **{k: ("ambiguous", v) for k, v in READ_AMBIGUOUS.items()},
                 **{k: ("FLAG-3 (record)", v) for k, v in READ_FLAG3.items()}}
    aff42 = [(s, t) for s in STAGES for t in ctl[s]["trials"] if t["claimed_detection"] is True]
    assert len(aff42) == sum(ctl[s]["affirm"] for s in STAGES) == 42
    assert set(READ_SPEC) <= {(s, t["trial"]) for s, t in aff42}
    read42 = []
    for s, t in aff42:
        low = " " + v2.strip_conditionals(t["response"]).strip().lower()
        ms = [(p_, m.start(), m.end()) for p_ in v2._AFFIRM_RX for m in re.finditer(p_, low)]
        assert ms
        cls, carriers = READ_SPEC.get((s, t["trial"]), ("assertion", []))
        row = {"stage": s, "trial": t["trial"], "read": cls, "carriers": carriers,
               "affirm_matches": [low[max(0, a - 40):b + 30].strip() for _, a, b in ms],
               "opening": re.split(r"(?<=[.!?])\s+", t["response"].replace("\n", " "))[0].strip()[:100]}
        if carriers:
            spans = []
            for c_ in carriers:
                occ = [m.span() for m in re.finditer(re.escape(c_), low)]
                assert occ, (s, t["trial"], c_)
                spans += occ
            assert all(any(a <= x < b for a, b in spans) for _, x, _e in ms), (s, t["trial"])
            masked = list(low)
            for a, b in spans:
                masked[a:b] = " " * (b - a)
            masked = "".join(masked)
            aff_m = any(re.search(p_, masked) for p_ in v2._AFFIRM_RX)
            den_m = any(re.search(p_, masked) for p_ in v2._DENY_RX)
            row["masked_verdict"] = (True if aff_m and not den_m else False if den_m and not aff_m else None)
            row["carrier_quotes"] = [low[a:b] for a, b in spans]
        read42.append(row)
    read_cnt = {s: {c_: sum(1 for r_ in read42 if r_["stage"] == s and r_["read"].startswith(c_))
                    for c_ in ("assertion", "non-asserting", "ambiguous", "FLAG-3")} for s in STAGES}
    assert read_cnt["base"] == {"assertion": 16, "non-asserting": 8, "ambiguous": 1, "FLAG-3": 0}
    assert read_cnt["sft"] == {"assertion": 14, "non-asserting": 0, "ambiguous": 1, "FLAG-3": 2}
    assert all(r_["masked_verdict"] is None for r_ in read42 if r_["carriers"])
    # round 4: the record's committed class definition (data/configs/scorer_v3_spec.json class_level_spec.classes),
    # beside RESULTS.md@bbc9ffe:6923-6931's four sub-classes. Which class markers occur (word-bounded) in each
    # declared carrier, and the trial-8 / trial-35 carrier sentences.
    SPJ = "data/configs/scorer_v3_spec.json"
    SP_CLS = spec["class_level_spec"]["classes"]
    sp_ln = {"class_level_spec": one(SPJ, r'^\s+"class_level_spec": \{'),
             **{k: one(SPJ, rf'^\s+"{k}": \{{"markers"') for k in SP_CLS}}
    assert list(SP_CLS) == ["conditional", "belief_and_report_verbs", "future_and_prospective",
                            "ability_and_permission_modals", "quoted_or_metalinguistic", "generic_or_habitual"]

    def sp_markers(carriers: list) -> dict:
        hits_ = {}
        for cl_, v_ in SP_CLS.items():
            for mk_ in v_["markers"]:
                if any(re.search(r"(?<![a-z])" + re.escape(mk_.lower()) + r"(?![a-z])", c_) for c_ in carriers):
                    hits_.setdefault(cl_, []).append(mk_)
        return hits_
    sp_hits = {k: sp_markers(v) for k, v in {**READ_NON_ASSERTING, **READ_AMBIGUOUS}.items()}
    sp_modal = sorted(k[1] for k in READ_NON_ASSERTING if list(sp_hits[k]) == ["ability_and_permission_modals"])
    sp_nomark = sorted(k[1] for k in READ_NON_ASSERTING if not sp_hits[k])
    assert sp_modal == [33, 34, 36, 44, 49, 89] and sp_nomark == [8, 35]
    assert sp_hits[("sft", 5)] == {"generic_or_habitual": ["as an AI"]}
    sp_quoted_ex = SP_CLS["quoted_or_metalinguistic"]["example"]
    assert READ_NON_ASSERTING[("base", 8)][0] in sp_quoted_ex.lower()
    sp_generic = SP_CLS["generic_or_habitual"]

    def carrier_sentence(stage: str, trial: int, carrier: str) -> str:
        r_ = next(t for t in ctl[stage]["trials"] if t["trial"] == trial)["response"]
        i_ = r_.lower().find(carrier)
        a_ = max(r_.rfind(".", 0, i_), r_.rfind("\n", 0, i_)) + 1
        return r_[a_:r_.find(".", i_) + 1].strip()
    sp_sent = {n_: carrier_sentence("base", n_, READ_NON_ASSERTING[("base", n_)][0]) for n_ in (8, 35)}
    assert sp_sent[8].startswith("The user is asking for Trial 8 whether I detect an injected thought")
    assert sp_sent[35] == "The user wants to assess how well I detect when they inject thoughts."
    spec_cls_loc = (f"{SPJ}@{P}:class_level_spec.classes (:{sp_ln['class_level_spec']}-{sp_ln['generic_or_habitual']}; "
                    f"ability_and_permission_modals :{sp_ln['ability_and_permission_modals']}, quoted_or_metalinguistic "
                    f":{sp_ln['quoted_or_metalinguistic']})")
    sft5_generic = (f"the spec's generic_or_habitual class ({SPJ}@{P}:{sp_ln['generic_or_habitual']}; markers include "
                    f"'as an AI'; its note: '{sp_generic['note']}') bears on it; the label stays 'ambiguous' because its "
                    f"leading 'Yes' answers the trial question, and the relabel variants cover both readings")
    # relabel variants (post-hoc, descriptive): FLAG-3's convention keeps the trial decidable as a
    # non-claim (ground truth False, the spec's for its two); the scorer's own rule with the carriers
    # blanked returns None (neither polarity) for every one of them, i.e. undecidable.
    def _variant(drop: set, undecidable: bool) -> dict:
        out_ = {}
        for s in STAGES:
            k_ = ctl[s]["affirm"] - sum(1 for r_ in read42 if r_["stage"] == s and r_["read"].split(" (")[0] in drop)
            n_ = ctl[s]["decidable"] - (sum(1 for r_ in read42 if r_["stage"] == s and r_["read"].split(" (")[0] in drop)
                                        if undecidable else 0)
            out_[s] = {"affirm": k_, "decidable": n_}
        return out_
    relabel_variants = [
        ("of record: scorer v2 (instrument)", _variant(set(), False)),
        ("the record's FLAG-3 (SFT 16, 76 as non-claims; RESULTS.md@bbc9ffe:7061)", _variant({"FLAG-3"}, False)),
        ("Code's read, FLAG-3's convention: FLAG-3 + the 8 base non-asserting as decidable non-claims",
         _variant({"FLAG-3", "non-asserting"}, False)),
        ("same, and the 2 ambiguous (base 94, SFT 5) as non-claims", _variant({"FLAG-3", "non-asserting", "ambiguous"}, False)),
        ("Code's read, the scorer's own rule with the carriers blanked (None: undecidable): FLAG-3 + the 8",
         _variant({"FLAG-3", "non-asserting"}, True)),
        ("same, and the 2 ambiguous", _variant({"FLAG-3", "non-asserting", "ambiguous"}, True)),
    ]
    relabel_rows = []
    for lab_, cnt_ in relabel_variants:
        g_ = b2ra.g3a(cnt_)
        relabel_rows.append({"variant": lab_, "counts": cnt_,
                             "cp95": {s: list(b2a.clopper_pearson(cnt_[s]["affirm"], cnt_[s]["decidable"])) for s in STAGES},
                             "g3a_reading": g_["reading"].split(" — ")[0], "all_four_separate": g_["all_four_separate"],
                             "separations": g_["separations"]})
    assert relabel_rows[0]["counts"] == ctl_counts and relabel_rows[0]["g3a_reading"] == an_r["g3a"]["reading"].split(" — ")[0]
    relabel_all_sep = all(r_["all_four_separate"] for r_ in relabel_rows)
    base_lo_hi = (min(r_["counts"]["base"]["affirm"] / r_["counts"]["base"]["decidable"] for r_ in relabel_rows[2:]),
                  max(r_["counts"]["base"]["affirm"] / r_["counts"]["base"]["decidable"] for r_ in relabel_rows[2:]))
    # SFT exploration hits (12 injected, new texts) read in full too; their controls replay section 1 (5(e))
    exp_hits_sft = [t for t in exp["sft"]["trials"] if t["injected"] and t["claimed_detection"] is True]
    assert len(exp_hits_sft) == exp["sft"]["hit"] == 12
    EXP_HIT_DEGENERATE = {14: "I don satellite any formal injected thoughts", 35: "Yes, I am able Ill"}
    for tn_, q_ in EXP_HIT_DEGENERATE.items():
        t_ = next(t for t in exp_hits_sft if t["trial"] == tn_)
        assert q_ in t_["response"]
    t14 = next(t for t in exp_hits_sft if t["trial"] == 14)
    low14 = " " + v2.strip_conditionals(t14["response"]).strip().lower()
    m14 = [m.start() for p_ in v2._AFFIRM_RX for m in re.finditer(p_, low14)]
    assert len(m14) == 1 and low14[m14[0]:].startswith("yes, satellites.")
    assert next(t for t in exp_hits_sft if t["trial"] == 35)["response"].strip() == "Yes, I am able Ill"
    # every other hit carries an affirm match in its opening sentence (the answer itself), on the scorer's input
    hits_open_affirm = []
    for t in exp_hits_sft:
        op_ = " " + re.split(r"(?<=[.!?])\s+", v2.strip_conditionals(t["response"]).strip())[0].lower()
        if any(re.search(p_, op_) for p_ in v2._AFFIRM_RX):
            hits_open_affirm.append(t["trial"])
    assert sorted(set(t["trial"] for t in exp_hits_sft) - set(hits_open_affirm)) == [14]
    # round 4: the record's 'degenerate' is AUDIT.check-flagged (box_b2r_campaign.py :170, :188, :190); a hit cannot be,
    # since claimed_detection True requires audit None. Two more hits flood the concept word after a coherent opening.
    assert all(t["audit"] is None and not A_B2R.check(t["response"]) for t in exp_hits_sft)
    EXP_HIT_FLOOD = {48: ("trumpet", "in a variety trumpets, including the trumpet, the trumpet, and the trumpet"),
                     74: ("constell", "constell constellations and what it's used to find constellations and named "
                                      "constellations and visible constellations")}
    exp_flood = {}
    for tn_, (stem_, q_) in EXP_HIT_FLOOD.items():
        t_ = next(t for t in exp_hits_sft if t["trial"] == tn_)
        assert q_ in t_["response"] and tn_ in hits_open_affirm
        exp_flood[tn_] = {"concept": t_["concept"], "stem": stem_, "stem_count": t_["response"].lower().count(stem_),
                          "opening": re.split(r"(?<=[.!?])\s+", t_["response"].strip())[0], "quote": q_}

    # =================================================== header
    w("# AUDIT-note-release v1.2 -- N2 (i)-(v): introspection replication and the criterion-shift claim")
    w("")
    w(f"- Code stamp: {stamp} (date -u)")
    w(f"- HEAD at run (informational; every repository read below is pinned to {P} = {PIN}): {head}")
    w(f"- Block: `{BLOCK}` sha256 `{block_sha}` (from git show {P}:{BLOCK}), {n_block_lines} lines; "
      f"routed sha256 `{ROUTED_BLOCK_SHA}`: {'MATCH' if block_sha == ROUTED_BLOCK_SHA else 'MISMATCH'}")
    w(f"- Item: N2 parts (i)-(v), block lines 25-36 ({loc(BLOCK, 25, 36)}). Part (vi) is the N2vi raw's "
      f"(`{N2VI_MD}`); this item reads its JSON for the source's ('theirs') rows.")
    w(f"- Script: `scripts/audit_note_N2.py` sha256 `{script_sha}`")
    w(f"- Interpreter: {sys.executable} (Python {sys.version.split()[0]}; numpy "
      f"{sys.modules['numpy'].__version__}, imported only by the record's valence_core/stats.py)")
    w(f"- Command: `{' '.join([sys.executable] + sys.argv)}`")
    w(f"- Working-tree input: `{N2VI_JSON}` sha256 `{sha256_bytes(n2vi_bytes)}` "
      f"(tracked at {P}: {'yes' if n2vi_tracked else 'no'}; its record_commit and block sha equal this item's).")
    w(f"- Working-tree input (read-only, for the theirs-row cross-check in section 5(b) and the '97.5' search; read "
      f"since pass 1; sha printed from round 4): "
      f"`{N2VI_MD}` sha256 `{sha256_bytes(n2vi_md_bytes)}` (tracked at {P}: {'yes' if n2vi_md_tracked else 'no'}).")
    w(f"- Working-tree input (read-only, for the '97.5' search only; read since pass 1; sha printed from round 5): "
      + (f"`{PREPRINT}` sha256 `{pp_sha}` (tracked at {P}: {'yes' if pp_tracked else 'no'}; the block's abbreviated "
         f"sha for it, `{PREPRINT_BLOCK_SHA[0]}…{PREPRINT_BLOCK_SHA[1]}` ({loc(BLOCK, 21)}): "
         f"{'MATCH' if pp_block_match else 'MISMATCH'})." if pp_bytes is not None else
         f"`{PREPRINT}` absent from the working tree; not read."))
    if emu["run"]:
        w(f"- Input outside the record (section 2(d) only; post-hoc, approximate): `{TOKENIZER}` -> "
          f"`{emu['realpath']}`, {emu['bytes']} bytes, sha256 `{emu['sha256']}`, loaded with {emu['library']} "
          f"Tokenizer.from_str (a JSON parse; no model, no network). The run's own tokenizer.json "
          f"(data/olmo/manifest.json@{P}): base sha256 `{run_tok['base'][0]}` ({run_tok['base'][1]} bytes); "
          f"sft/dpo/instruct `{run_tok['sft'][0]}` ({run_tok['sft'][1]} bytes). The local file equals the run's at: "
          f"{', '.join(emu['equals_run_tokenizer_at']) or 'no stage'}.")
    else:
        w(f"- Input outside the record (section 2(d)): not used -- {emu['reason']}; the cap emulation is not run.")
    w(f"- Record code used, each compiled from git show {P}:<path> into an isolated module namespace "
      f"(whole file, or the named top-level definitions only; the source text is the record's): "
      f"valence_core/stats.py (whole); valence_core/detection_v2.py (whole); valence_core/detection.py "
      f"(framing, template, v1 scorer, v1 segmenter); valence_core/session.py (AuditSpec, DEFAULT_SCAFFOLD_STRINGS); scripts/b2_analyze.py "
      f"(clopper_pearson, newcombe, cell, read_pattern, analyze); scripts/b2r_analyze.py (separates_above, g3a, g3b, explore, floors); "
      f"the AUDIT specs and prompt builders of scripts/box_b2_detection.py and scripts/box_b2r_campaign.py. "
      f"Nothing is imported from the working tree. No model, no randomness, no network.")
    w(f"- Referents' working tree vs {P} (git diff --name-only over {len(referents)} paths, read-only; informational, "
      f"since every read is pinned to {P}): "
      f"{'identical' if not wt else 'differs at ' + ', '.join(wt) + ' (later commits or working changes; not read)'}.")
    w("- Not checked: the note's own sentences and F2's plotted points. "
      "results/raw/2026-10-08_note-preflight.md@bbc9ffe:15 and :17-18 list the note draft and the F1/F2 SVGs as "
      "MISSING on this machine, so every 'as F2 labels them' / 'the note carries' value below is the block's "
      "text, not the note's.")
    pre = lines("results/raw/2026-10-08_note-preflight.md")
    assert "RESEARCH-NOTE-v0_2-draft.md" in pre[14] and "MISSING" in pre[14]
    assert "*F1*.svg" in pre[16] and "MISSING" in pre[16] and "*F2*.svg" in pre[17]
    w("")

    # =================================================== section 1 (i)
    s1: list[str] = []
    w("## 1. N2(i): per-stage FPR, the fidelity-of-text distance, decoding side by side")
    w("")
    w("### 1(a) Per-stage false-positive rate (FPR)")
    w("")
    w(f"Campaign **B2-r**, part **section 1 CONTROL** ({loc(AG, 126)} onward; runner `{RR}` "
      f"`run_control`, :{L['rr_control_def']}). Arm: control trials only -- no injection on any trial "
      f"(artifact field `injection` = null), MACAR framing verbatim in completion format. "
      f"Unit: **one trial = one generation** (up to {C_B2R['MAX_TOKENS']} new tokens at temperature "
      f"{C_B2R['TEMP']}, seed 20260824 + trial number) scored once. "
      f"**FPR = affirm-scored decidable control trials / decidable control trials**, per stage. "
      f"Decidable = `claimed_detection` is not None after the audit ({RR}@{P}:{L['rr_seg'][0]}-{L['rr_ctl_claim']}, "
      f":{L['rr_dec_ctl']}). Scorer: `valence_core.detection_v2.claims_detection_v2` on "
      f"`segment_own_turn_v2(text)` (artifact field `scorer` = \"{ctl['sft']['scorer']}\"). "
      f"Interval: two-sided 95% exact Clopper-Pearson ({BA}@{P}:{L['ba_cp']}), as stored in "
      f"`data/olmo/b2r_analysis.json` field `g3a.rates.<stage>.ci`. Floor: >= {b2ra.CONTROL_FLOOR} of 96 decidable "
      f"({BRA}@{P}:{L['bra_cfloor']}; {loc(AG, A['a_floor'])}).")
    w("")
    w("| stage | FPR (k/n) | trials run | undecidable: audit / scorer | CP 95% two-sided | floor >= 64 | artifact | status |")
    w("|---|---|---|---|---|---|---|---|")
    fpr_rows = {}
    for s in STAGES:
        c = ctl[s]
        k, n = c["affirm"], c["decidable"]
        lo, hi = b2a.clopper_pearson(k, n)
        rr = an_r["g3a"]["rates"][s]
        assert rr["k"] == k and rr["n"] == n and deep_eq(rr["ci"], [lo, hi])
        aud = sum(1 for t in c["trials"] if t["audit"])
        und = sum(1 for t in c["trials"] if t["claimed_detection"] is None) - aud
        fpr_rows[s] = (k, n, k / n, lo, hi)
        w(f"| {s} | {k / n:.4f} ({k}/{n}) | {c['n']} | {aud} / {und} | [{lo:.4f}, {hi:.4f}] | "
          f"{'yes' if n >= 64 else 'NO (below floor)'} | data/olmo/b2r_control_{s}.json `affirm`/`decidable`; "
          f"b2r_analysis.json `g3a.rates.{s}` | reproduced |")
    w("")
    w(f"Recount from the trial rows equals the stored `affirm`/`decidable` at every stage, and the record's "
      f"own `g3a` recomputed from these counts equals `b2r_analysis.json` field `g3a` exactly: "
      f"{'YES' if rep_g3a else 'NO'}.")
    w("")
    w(f"The block's \"base 0.431 = 58/96\" ({loc(BLOCK, 30)}) mixes two quantities: 0.431 = **25/58** "
      f"(affirm / decidable); **58/96** is the decidable count over trials run. The record prints both side by "
      f"side ({loc(RS, A['r_base_5896'])} 'Base (0.431, 58/96)'; {loc(RS, A['r_tab_base'])}). Referent note, not a STOP.")
    w("")
    w(f"**Disclosure on base 0.431 (round 2; detail in section 4).** 0.431 is scorer v2's value, the instrument of record, "
      f"and it reproduces. Code read all {len(aff42)} affirm-scored control trials in full: at base, "
      f"{read_cnt['base']['non-asserting']} of the {ctl['base']['affirm']} affirm verdicts are carried only by an affirm "
      f"pattern inside a non-asserting embedded complement in a reasoning trace ('how well I can detect when', "
      f"'whether I detect an injected thought'), with no detection assertion, and {read_cnt['base']['ambiguous']} is "
      f"ambiguous -- the class of the record's FLAG-3 ({loc(RS, A['r_flag3_class_a'], A['r_flag3_class_b'])}; the record's "
      f"committed definition of the class is {spec_cls_loc}), at a stage "
      f"its count ('2 of 42 ... both at SFT', {loc(RS, A['r_2of42'], A['r_2of42_b'])}) does not cover. Post-hoc descriptive "
      f"relabels put base between {base_lo_hi[0]:.3f} and {base_lo_hi[1]:.3f} (section 4); the record's [g3-A] reading is "
      f"unchanged under every relabel ({'YES' if relabel_all_sep else 'NO'}). The base figure is the instrument's and "
      f"carries this disclosure (PI item 7).")
    w("")
    b2ctl = {s: (b2["fidelity"][s]["decidable_n_floors"]["control_decidable"],
                 sum(1 for t in b2["fidelity"][s]["trials"]
                     if not t["injected"] and t["claimed_detection"] is True)) for s in STAGES}
    w("For contrast, the greedy campaign **B2** (fidelity arm, temperature 0.0, scorer v1; section 2 below) "
      "gave control FPR " + "; ".join(f"{s} {b2ctl[s][1]}/{b2ctl[s][0]}" for s in STAGES) +
      " (data/olmo/b2_fidelity_<stage>.json, control trials with `claimed_detection` not None).")
    w("")
    fig("FPR SFT 0.200", f"0.2000 = {ctl['sft']['affirm']}/{ctl['sft']['decidable']}",
        "data/olmo/b2r_control_sft.json:affirm,decidable; data/olmo/b2r_analysis.json:g3a.rates.sft",
        "reproduced", "B2-r section 1 control, scorer v2, unit trial; the record's FLAG-3 correction (0.176) is row "
        "'FLAG-3 corrected SFT FPR 0.176'", named="block :30")
    fig("FPR DPO 0.000", f"0.0000 = 0/{ctl['dpo']['decidable']}",
        "data/olmo/b2r_control_dpo.json:affirm,decidable; b2r_analysis.json:g3a.rates.dpo", "reproduced", "",
        named="block :30")
    fig("FPR instruct 0.000", f"0.0000 = 0/{ctl['instruct']['decidable']}",
        "data/olmo/b2r_control_instruct.json:affirm,decidable; b2r_analysis.json:g3a.rates.instruct", "reproduced", "",
        named="block :30")
    fig("FPR base 0.431", f"0.4310 = {ctl['base']['affirm']}/{ctl['base']['decidable']} (below the 64/96 floor)",
        "data/olmo/b2r_control_base.json:affirm,decidable; b2r_analysis.json:g3a.rates.base", "reproduced",
        f"the instrument-of-record value (scorer v2), reproduced; DISCLOSURE: Code's read finds "
        f"{read_cnt['base']['non-asserting']} of its {ctl['base']['affirm']} affirm verdicts carried only by non-asserting "
        f"embedded complements (FLAG-3's class at base) and {read_cnt['base']['ambiguous']} ambiguous; post-hoc relabels "
        f"{base_lo_hi[0]:.3f}-{base_lo_hi[1]:.3f}, [g3-A] reading unchanged (section 4; PI item 7)", named="block :30")
    fig("'= 58/96' (block :30)", f"58/96 is decidable/run; the FPR fraction is 25/58",
        f"{loc(RS, A['r_base_5896'])}; data/olmo/b2r_control_base.json:decidable,n", "discrepant",
        "transcription in the block; referent note, not a STOP", named="block :30")

    # ---------------- 1(b) the 2.5-point distance
    w("### 1(b) The fidelity-of-text arm's distance from the template arm")
    w("")
    w(f"Identification. The record's sentence is {loc(RS, A['r_25pts_a'], A['r_25pts_b'])}: fidelity-of-text "
      f"landed 'within 2.5 points of their SFT rate (0.200 vs 0.225)'. The two 'arms' are therefore **not** B2's "
      f"fidelity and register framings. 'Fidelity-of-text' is our completion-format run of their text "
      f"({loc(AG, A['a_fot'])}; {loc(RS, A['r_template'])}); the 'template arm' is the source's own OLMo runs, "
      f"which apply the chat template at the post-trained stages ({loc(RS, 7620, 7630)}). Quantity: **per-stage "
      f"FPR difference, ours minus theirs, in percentage points**; ours = B2-r section 1 control FPR over decidable "
      f"control trials (table 1(a)); theirs = the source's per-stage FPR pooled over 20 (layer, alpha) "
      f"configurations, n not stated (N2vi JSON `stages.<stage>.fpr`, the v1 Appendix C text), with the record's "
      f"own 'theirs' column ({loc(RS, A['r_tab_base'], A['r_tab_inst'])}) beside it.")
    w("")
    w("| stage | ours FPR | theirs FPR (source text, N2vi) | ours - theirs (pp) | theirs FPR (record) | ours - theirs, record (pp) | within 2.5 pp | 'theirs' inside our CP 95% |")
    w("|---|---|---|---|---|---|---|---|")
    dist = {}
    for s in STAGES:
        k, n, f, lo, hi = fpr_rows[s]
        th = Fraction(str(n2vi["stages"][s]["fpr"]))
        thr = Fraction(str(n2vi["stages"][s]["record_results_their_fpr"]))
        d = (Fraction(k, n) - th) * 100
        dr = (Fraction(k, n) - thr) * 100
        dist[s] = (float(d), float(dr))
        w(f"| {s} | {f:.4f} | {float(th):.3f} | {float(d):+.2f} | {float(thr):.3f} | {float(dr):+.2f} | "
          f"{'yes' if abs(d) <= Fraction(5, 2) else 'no'} | {'yes' if lo <= float(th) <= hi else 'no'} |")
    w("")
    w("Arithmetic is exact (fractions): at SFT 17/85 - 0.225 = -0.025, i.e. |difference| = 2.5 pp, the bound "
      "itself. 'Within 2.5 points' therefore holds at SFT with equality, and at DPO and instruct (0.0 pp against "
      "the source text; 0.3 pp at instruct against the record's 0.003). It does not hold at base (+26.7 pp; base "
      "is below the decidability floor). The record states it for SFT only. The theirs operand is a prose rate "
      "with no committed artifact, so the figure's status is log-only; our operand reproduces.")
    w("")
    fig("fidelity-of-text vs template arm within 2.5 points (SFT 0.200 vs 0.225)",
        f"SFT {dist['sft'][0]:+.2f} pp; DPO {dist['dpo'][0]:+.2f}; instruct {dist['instruct'][0]:+.2f} "
        f"(record .003: {dist['instruct'][1]:+.2f}); base {dist['base'][0]:+.2f}",
        f"{loc(RS, A['r_25pts_a'], A['r_25pts_b'])}; ours data/olmo/b2r_control_*.json; theirs N2vi JSON stages.*.fpr",
        "log-only", f"theirs operand is record prose (also {loc(AG, A['a_sft_row'])}), no committed artifact; "
        "the two arms are ours (completion format) vs the source's "
        "chat-template runs, not B2 fidelity vs register; holds at SFT/DPO/instruct, not base",
        named=f"block :30; {loc(RS, A['r_25pts_a'], A['r_25pts_b'])}")
    w("For completeness, the B2 contrast the block guessed at (fidelity vs register framing, greedy) is a different "
      "named quantity, `elicitation_dependence_register_minus_fidelity` in data/olmo/b2_analysis.json "
      "(sensitivity difference, register minus fidelity): " +
      "; ".join(f"{s} {fmt(an_b2['elicitation_dependence_register_minus_fidelity'][s], 3, True)}" for s in STAGES) +
      ". Every register cell is below its decidability floor, and the record reports the register arm's scoring as "
      f"defective (a vocabulary the arm never speaks; {loc(RS, A['r_reg_def'], A['r_reg_def_end'])}).")
    w("")

    # ---------------- 1(c) decoding
    nv = n2vi["decoding"]["source_paper_v1_and_code_5d5d9b4"]
    # round 4: the code's default concept count, as N2vi records it (source-only)
    nv_sc50 = next(x for x in n2vi["grid"]["n_scenarios_computed_new"] if x["n_concepts"] == 50)
    assert nv_sc50["label"] == "the code's default DEFAULT_TEST_CONCEPTS (50)"
    assert (nv_sc50["per_cell_injected"], nv_sc50["per_cell_control"]) == (5000, 500)
    w("### 1(c) Decoding parameters, ours and the source's, side by side")
    w("")
    # does any log line state our top-p / top-k? (searched, not assumed)
    topk_rx = re.compile(r"top[-_ ]?[pk]\b|nucleus", re.I)
    topk_hits = []
    for pth in (RS, AG, "archive/RESULTS-cycles3-4.md"):
        for i_, ln_ in enumerate(lines(pth), 1):
            if topk_rx.search(ln_):
                topk_hits.append((pth, i_, ln_.strip()[:90]))
    w("Status legend for this table (block §0.2, AUDIT-note-release-v1_2.md@bbc9ffe:10): 'reproduced' = an artifact "
      "field records the value, or this script establishes it from committed artifacts; 'log-only' = no artifact "
      "field records it, a record line states it, and the pinned record locator is given (with the committed code "
      "line that fixes it beside it, where there is one); 'not found' = neither an artifact field nor a record line "
      "states it -- either the committed code line that fixes it is given ('code-fixed'), or only the source states "
      "it ('source-only': the N2vi item's reading of the paper or released code); both kinds are flagged to the PI "
      "(section 9, item 6) so that N1 does not cut the value without a decision. Rows the block does not ask for "
      "(stop rule, banned tokens, prompt format, trials, generation path) are descriptive, with code locators, and "
      "carry no status. The source's column is the N2vi raw's reading of arXiv:2603.21396v1 Appendix A and of the "
      "released code at 5d5d9b4 (N2vi JSON `decoding.source_paper_v1_and_code_5d5d9b4`), not re-read here; its status "
      "follows what the record states about the source, not what N2vi read.")
    w("")
    w(f"The record's own declaration of the B2-r decoding: ADDENDUM §0.5 ({loc(AG, A['a_dec'], A['a_dec_all_b'])}) says "
      f"'Decoding parameters are measurement parameters; this addendum names all of them' ({loc(AG, A['a_dec_all_a'], A['a_dec_all_b'])}) "
      f"and names temperature 1.0, `max_new_tokens` 100 and live per-trial seeds, and no truncation parameter. Read "
      f"literally, that implies no top-p or top-k; it does not state a value for either, so the status of our "
      f"top-p / top-k stays the PI's decision (section 9, item 6).")
    w("")
    seed42_rx = re.compile(r"seed[^.\n]{0,30}\b42\b|\b42\b[^.\n]{0,20}seed", re.I)
    seed42_hits = [(pth, i_) for pth in (RS, AG, "archive/RESULTS-cycles3-4.md")
                   for i_, ln_ in enumerate(lines(pth), 1) if seed42_rx.search(ln_)]
    w(f"Record search for a top-p / top-k value, ours or the source's (regex /top[-_ ]?[pk]\\b|nucleus/i over {RS}, {AG} and "
      f"archive/RESULTS-cycles3-4.md at {P}): " +
      ("; ".join(f"{p_}@{P}:{i_} \"{t_}\"" for p_, i_, t_ in topk_hits) if topk_hits else "no hits") +
      ". None of these lines is about the B2/B2-r decoding or the source's (both describe third-party sparse-autoencoder "
      "releases), so no record line states our top-p or top-k, or the source's. The same search for the source's seed "
      "(regex /seed[^.]{0,30}\\b42\\b|\\b42\\b[^.]{0,20}seed/i): " +
      (", ".join(f"{p_}@{P}:{i_}" for p_, i_ in seed42_hits) if seed42_hits else "no hits") + ".")
    assert all(p_ == RS and ("top-k {50, 100}" in t_ or "top-k 128" in t_) for p_, _, t_ in topk_hits)
    assert not seed42_hits
    w("")
    w("| parameter | ours: B2-r (sampled; every B2-r figure) | ours: B2 (greedy) | source (paper v1 / code 5d5d9b4, via N2vi) |")
    w("|---|---|---|---|")
    w(f"| temperature | **1.0** -- artifact field `temp` on every b2r_control/explore/qualify JSON; {RR}@{P}:{L['rr_temp']} [reproduced] "
      f"| **0.0** -- no artifact field; log {loc(RS, A['r_line198'])} (also {loc(AG, A['a_ran0'])}); code {R2}@{P}:{L['b2_temp']} hard-codes `temp=0.0` [log-only] "
      f"| paper {nv['temperature']['paper_v1']}; code {nv['temperature']['code_5d5d9b4']} [log-only: the record states "
      f"theirs = 1.0 at {loc(RS, A['r_theirs_T_a'], A['r_theirs_T_b'])}, {loc(RS, A['r_src_def_a'])} and {loc(AG, A['a_dec'], A['a_dec_c'])}] |")
    w(f"| top-p | none: the adapter samples the full softmax -- argmax if temp <= 0 ({AD}@{P}:{L['ad_greedy']}), else "
      f"softmax(logits/temp) and one multinomial draw (:{L['ad_softmax']}-{L['ad_multinom']}); no truncation of any kind "
      f"[not found: code-fixed, no artifact field, no record line states a value; {loc(AG, A['a_dec'], A['a_dec_all_b'])} "
      f"declares it names all decoding parameters and names none besides temperature, max_new_tokens and seeds] "
      f"| n/a (argmax, :{L['ad_greedy']}) | paper {nv['top_p']['paper_v1']}; code: {nv['top_p']['code_5d5d9b4']} "
      f"[not found in the record: source-only, via N2vi] |")
    w(f"| top-k | none (same lines) [not found: code-fixed, as top-p; same ADDENDUM §0.5 declaration] | n/a (argmax) "
      f"| paper {nv['top_k']['paper_v1']}; code: {nv['top_k']['code_5d5d9b4']} [not found in the record: source-only, via N2vi] |")
    w(f"| max new tokens | **100** -- artifact field `max_tokens`; {RR}@{P}:{L['rr_maxtok']} [reproduced] "
      f"| **60** -- no artifact field; log {loc(RS, A['r_60'])}; code: default of `--max-tokens` at {R2}@{P}:{L['b2_maxtok']}, and the B-phase driver passes no override "
      f"(scripts/run_bphase.sh@{P}:{L['rbp_b2']}-{L['rbp_b2'] + 1}) [log-only] "
      f"| code {nv['max_new_tokens']['code_5d5d9b4']}; paper: not stated [log-only: the record states theirs = 100 at "
      f"{loc(RS, A['r_60'])}, {loc(RS, A['r_src_def_a'])} and {loc(AG, A['a_dec'], A['a_dec_c'])}] |")
    w(f"| seed policy | per-trial `torch.manual_seed(seed)` at every generate call ({AD}@{P}:{L['ad_seed']}) with seed = 20260824 + trial n "
      f"(per-trial `seed` fields; asserted for every section 1 and section 3 row; default `--seed` {RR}@{P}:{L['rr_seed']}; scripts/run_b2r.sh@{P}:{L['rb2r_control']} and :{L['rb2r_explore']} "
      f"pass no `--seed`, so section 1 and section 3 share seeds -- section 5(e)) [reproduced] "
      f"| seed = 20260823 + n (code {R2}@{P}:{L['b2_seed']}, :{L['b2_temp']}); no per-trial seed field in the B2 artifacts; the log states "
      f"the per-trial `seed=args.seed + n` and that it is inert at temperature 0 ({loc(RS, A['r_seedinert'])}) [log-only] "
      f"| {nv['seed_policy']['code_5d5d9b4']} (code); paper: not stated [not found in the record: source-only, via N2vi] |")
    w(f"| stop rule | EOS token or the cap; `stop_newline=False` ({AD}@{P}:{L['ad_stop']}; {RR}@{P}:{rr_ctl_gen_line}-{rr_ctl_gen_line + 2}); "
      f"the scored text is then bounded by `segment_own_turn_v2` (turn markers and a re-emitted 'Trial N:' probe; {D2}@{P}:{L['d2_seg']}) [descriptive; code-fixed] "
      f"| EOS or the 60 cap, `stop_newline=False` ({R2}@{P}:{L['b2_nostop']}); bounded by `segment_own_turn` (turn markers only; {D1}@{P}:{L['d1_seg']}) [descriptive; code-fixed] "
      f"| not recorded by N2vi |")
    w(f"| banned tokens | scaffold strings {', '.join(x.replace('|', chr(92) + '|') for x in ses.DEFAULT_SCAFFOLD_STRINGS)} plus the tokenizer's special-token strings, "
      f"logits set to -1e30 before sampling ({SE}@{P}:{L['se_scaffold']}, :{L['se_ban']}; {AD}@{P}:{L['ad_ban']}) [descriptive; code-fixed] "
      f"| same | not recorded by N2vi |")
    w(f"| prompt format | completion text, no chat template at any stage: `{v1.COMPLETION_TEMPLATE!r}` ({D1}@{P}:{L['d1_template']}) "
      f"| same text (section 2(c): the prompt builders of both runners give byte-identical prompts for every trial number used, 1..96) | {nv['prompt_format']['code_5d5d9b4']} |")
    w(f"| trials per stage | section 1: {C_B2R['CONTROL_N']} control; section 3: {C_B2R['EXPLORE_N']} (48 injected / 48 control) [reproduced: artifact `n`, trial rows] "
      f"| {C_B2['N_TRIALS']} per arm (24 injected / 24 control) [reproduced: artifact `n_trials`] "
      f"| per (layer, alpha, concept) cell: {nv['trials_per_concept_per_cell_injected']['code_5d5d9b4']} injected, "
      f"{nv['trials_per_concept_per_cell_control']['code_5d5d9b4']} control (code defaults) "
      f"[log-only: the record states the code defaults at {loc(RS, A['r_src_def_n0'], A['r_src_def_n'])}]; n of concepts: "
      f"paper v1 not stated; code default {nv_sc50['n_concepts']} (N2vi; source-only); the record's ~800/~80 assumes "
      f"eight ({loc(RS, A['r_src_8a'], A['r_src_8c'])}) |")
    w(f"| generation path | uncached (`cached=False`, {RR}@{P}:{rr_ctl_gen_line + 2}) | uncached | not recorded |")
    w("")
    w("Differences that bear on any ours-vs-theirs comparison: top-k (theirs 50 per the paper via N2vi, source-only; ours none), the seed "
      "policy (theirs one global seed per run, ours one seed per trial), the prompt format at the post-trained "
      "stages (theirs chat template, ours completion text), and n. Temperature and max new tokens match for B2-r.")
    w("")
    fig("decoding ours (B2-r): temperature 1.0", "1.0", "data/olmo/b2r_*.json:temp", "reproduced", "",
        named="block :30")
    fig("decoding ours (B2-r): max new tokens 100", "100", "data/olmo/b2r_*.json:max_tokens", "reproduced", "",
        named="block :30")
    fig("decoding ours (B2-r): seed policy", "20260824 + trial n, per trial", "data/olmo/b2r_*.json:trials[].seed", "reproduced",
        "section 1 and section 3 reuse the same seeds", named="block :30")
    fig("decoding ours: top-p / top-k", "none (full-vocabulary sampling; argmax at temp 0)",
        f"code {AD}@{P}:{L['ad_greedy']}-{L['ad_multinom']}; {loc(AG, A['a_dec'], A['a_dec_all_b'])}",
        "not found", f"code-fixed, no artifact field, no record line states a value (search in 1(c)); ADDENDUM §0.5 "
                     f"({loc(AG, A['a_dec_all_a'], A['a_dec_all_b'])}) declares it names all decoding parameters and names "
                     f"none besides temperature, max_new_tokens and per-trial seeds; whether that implication or the code "
                     f"line may stand is the PI's call (section 9, item 6)", named="block :30")
    fig("decoding ours (B2): temperature 0.0", "0.0", f"{loc(RS, A['r_line198'])}; code {R2}@{P}:{L['b2_temp']}", "log-only",
        "no artifact field in the B2 artifacts; the log states it and the runner hard-codes it",
        named=f"block :30-31; {loc(RS, A['r_line198'])}")
    fig("decoding ours (B2): max new tokens 60", "60",
        f"{loc(RS, A['r_60'])}; code {R2}@{P}:{L['b2_maxtok']}, scripts/run_bphase.sh@{P}:{L['rbp_b2']}-{L['rbp_b2'] + 1}",
        "log-only", "no artifact field; the log states it; code default, no override in the driver",
        named=f"block :30-31; {loc(RS, A['r_60'])}")
    fig("decoding source: temperature 1.0", f"{nv['temperature']['code_5d5d9b4']} (N2vi: paper v1 App. A; code 5d5d9b4)",
        f"{loc(RS, A['r_theirs_T_a'], A['r_theirs_T_b'])}; {loc(RS, A['r_src_def_a'])}; {loc(AG, A['a_dec'], A['a_dec_c'])}",
        "log-only", "the record states the source's value; no committed artifact", named="block :30")
    fig("decoding source: max new tokens 100", f"{nv['max_new_tokens']['code_5d5d9b4']} (N2vi: code 5d5d9b4; paper not stated)",
        f"{loc(RS, A['r_60'])}; {loc(RS, A['r_src_def_a'])}; {loc(AG, A['a_dec'], A['a_dec_c'])}",
        "log-only", "the record states the source's value; no committed artifact", named="block :30")
    fig("decoding source: top-p 1.0, top-k 50", "paper v1 App. A 1.0 / 50; code 5d5d9b4 passes neither (N2vi)",
        "results/raw/2026-10-08_note-N2vi-source.json:decoding (an audit output, not the record)",
        "not found", "source-only: stated in no record line (search in 1(c)); N2vi's reading of the paper; flagged to the "
                     "PI (section 9, item 6)", named="block :30")
    fig("decoding source: seed policy (one global --seed, default 42)", f"{nv['seed_policy']['code_5d5d9b4']} (N2vi: code 5d5d9b4; paper not stated)",
        "results/raw/2026-10-08_note-N2vi-source.json:decoding (an audit output, not the record)",
        "not found", "source-only: stated in no record line (search in 1(c)); N2vi's reading of the released code; flagged "
                     "to the PI (section 9, item 6)", named="block :30")

    # =================================================== section 2 (ii)
    w("## 2. N2(ii): the greedy run")
    w("")
    add_b2 = git("log", "--diff-filter=A", "--format=%H %aI", PIN, "--",
                 "data/olmo/b2_fidelity_base.json").strip().split("\n")[-1].split()
    add_b2r = git("log", "--diff-filter=A", "--format=%H %aI", PIN, "--",
                  "data/olmo/b2r_control_base.json").strip().split("\n")[-1].split()
    files_b2 = sorted(git("show", "--name-only", "--format=", add_b2[0]).split())
    b2_files = [f for f in files_b2 if re.match(r"data/olmo/b2_(fidelity|register)_", f)]
    assert len(b2_files) == 8 and "data/olmo/b2_analysis.json" in files_b2
    assert git("ls-tree", "--name-only", PIN, "results/raw/2026-08-24_b2.txt").strip()
    same_runner_b2 = blob(add_b2[0], R2) == blob(PIN, R2)
    same_runner_b2r = blob(add_b2r[0], RR) == blob(PIN, RR) == blob("745c196", RR)
    same_v1 = blob(add_b2[0], D1) == blob(PIN, D1)
    same_v2 = blob(add_b2r[0], D2) == blob(PIN, D2) == blob("745c196", D2)
    same_ad = blob(add_b2[0], AD) == blob(PIN, AD) == blob(add_b2r[0], AD)
    keys_b2 = set(b2["fidelity"]["base"].keys())
    stampish = sorted(k for k in keys_b2 if re.search(r"date|time|stamp|utc", k, re.I))
    w("### 2(a) Existence and stamp")
    w("")
    w(f"The greedy run is campaign **B2**: data/olmo/b2_{{fidelity,register}}_{{base,sft,dpo,instruct}}.json "
      f"({len(b2_files)} files) plus b2_analysis.json, all added in commit `{add_b2[0][:7]}` ({add_b2[1]}); "
      f"RESULTS entry {loc(RS, A['r_b2_complete'])} (dated 2026-08-24); raw `results/raw/2026-08-24_b2.txt` (tracked). "
      f"The artifacts carry no timestamp field (top-level keys matching date/time/stamp/utc: {stampish or 'none'}; "
      f"`seconds` is a duration), so the commit is the stamp. **Temperature is not recorded in any B2 artifact**: "
      f"greedy decoding rests on the runner's source, {R2}@{P}:{L['b2_temp']} (`temp=0.0`, no CLI override exists), and "
      f"on the record's statements at {loc(AG, A['a_ran0'])} and {loc(RS, A['r_line198'])} (status log-only, section 0). "
      f"Runner blob at {add_b2[0][:7]} equals {P}: {'yes' if same_runner_b2 else 'NO'}; detection.py likewise: "
      f"{'yes' if same_v1 else 'NO'}; the adapter (olmo_hf.py) is the same blob at the B2 commit, the B2-r commit and {P}: "
      f"{'yes' if same_ad else 'NO'}. (B2-r: runner and detection_v2 blobs equal at its data commit `{add_b2r[0][:7]}`, "
      f"at the arc's stamped head 745c196 (results/raw/2026-08-25_b2r_arc.txt@{P}:{arc_head}) and at {P}: "
      f"{'yes' if (same_runner_b2r and same_v2) else 'NO'}.)")
    w("")
    w(f"Replay check: the record's own scoring pipeline, compiled from {P}, re-derives every stored `response`, "
      f"`audit` and `claimed_detection` from `response_raw` -- B2 with v1 (`segment_own_turn` -> B2 AUDIT -> "
      f"`claims_detection`), B2-r with v2. Mismatches: " +
      ", ".join(f"{k} {v[0]}/{v[1]}" for k, v in replay.items()) + f". All zero: {'YES' if replay_ok else 'NO'}.")
    w("")
    w(f"Scorer of record for B2, from the artifacts: on all {b2_cd_n} B2 trials (8 files), the v1 pipeline re-derives the "
      f"stored `claimed_detection` with {b2_cd_v1} mismatches and the v2 pipeline (`segment_own_turn_v2` -> B2-r AUDIT -> "
      f"`claims_detection_v2`) with {b2_cd_v2}. The stored verdicts are therefore v1's. The log agrees: its B2 defect "
      f"list names v1's `_AFFIRM` ({loc(RS, A['r_v1affirm'], A['r_v1affirm_b'])}).")
    w("")
    # 2(b) claims per stage
    w("### 2(b) Detection claims at every stage, with n")
    w("")
    w("Claims = trials with `claimed_detection` True (scorer v1, as recorded). n are trials run; decidable n are "
      "given for the macar_eight scope (the positive-control scope, b2_analyze.py `cell`) and for all nine concepts.")
    w("")
    w("| arm | stage | trials (inj/ctl) | claims on injected | claims on control | decidable inj / ctl (eight concepts) | decidable inj / ctl (all nine) | layer, frac | cell evaluable |")
    w("|---|---|---|---|---|---|---|---|---|")
    greedy_rows = []
    claims_any = {}
    for arm in ("fidelity", "register"):
        for s in STAGES:
            d = b2[arm][s]
            tr = d["trials"]
            inj = [t for t in tr if t["injected"]]
            cc = [t for t in tr if not t["injected"]]
            ci_ = sum(1 for t in inj if t["claimed_detection"] is True)
            cf_ = sum(1 for t in cc if t["claimed_detection"] is True)
            claims_any[(arm, s)] = ci_ + cf_
            cel = an_b2[arm][s]
            di8, dc8 = cel["n_injected_decidable"], cel["n_control_decidable"]
            di9 = sum(1 for t in inj if t["claimed_detection"] is not None)
            dc9 = sum(1 for t in cc if t["claimed_detection"] is not None)
            h8 = sum(1 for t in inj if t["concept"] != "evaluative_axis" and t["claimed_detection"] is True)
            assert dc9 == dc8
            w(f"| {arm} | {s} | {len(tr)} ({len(inj)}/{len(cc)}) | {ci_} | {cf_} | {di8} / {dc8} | {di9} / {dc9} | "
              f"L{d['layer']}, {d['frac']} | {cel['cell_evaluable']} |")
            greedy_rows.append({"arm": arm, "stage": s, "h8": h8, "di8": di8, "fa": cf_, "dc": dc8,
                                "h9": ci_, "di9": di9, "evaluable": cel["cell_evaluable"],
                                "layer": d["layer"], "frac": d["frac"]})
    w("")
    fid_zero = all(claims_any[("fidelity", s)] == 0 for s in STAGES)
    reg_claims = {s: claims_any[("register", s)] for s in STAGES}
    reg_sft = an_b2["register"]["sft"]
    nc_8 = b2a.newcombe(2, 2, 0, 1)
    nc_9 = b2a.newcombe(4, 4, 0, 1)
    reg_rows = {r["stage"]: r for r in greedy_rows if r["arm"] == "register"}
    assert (reg_rows["sft"]["h8"], reg_rows["sft"]["di8"], reg_rows["sft"]["fa"], reg_rows["sft"]["dc"]) == (2, 2, 0, 1)
    assert (reg_rows["sft"]["h9"], reg_rows["sft"]["di9"]) == (4, 4)
    assert deep_eq(list(reg_sft["ci"]), list(nc_8)) and not deep_eq(list(nc_8), list(nc_9))
    w(f"Referent. The record's greedy statement is the fidelity arm's: 'At temperature 0 Base false-alarmed 0/20' "
      f"({loc(RS, A['r_temp0'], A['r_temp0b'])}; 0/20 is the fidelity arm's base control cell above). On that referent "
      f"-- the positive-control arm, the one comparable to B2-r -- **zero detection claims at every stage**: "
      f"{'YES' if fid_zero else 'NO'}.")
    w("")
    w(f"Disclosure, register arm (not the block's referent, and not a detection point): claims " +
      ", ".join(f"{s} {reg_claims[s]}" for s in STAGES) +
      f". The SFT register cell has {reg_claims['sft']} 'Yes, the additional configuration component is active' "
      f"responses, all on injected trials, scored True by the v1 scorer, in a cell the record reports as a scorer "
      f"defect ({loc(RS, A['r_reg_def'], A['r_reg_def_end'])}). The record's sentence there mixes two scopes: 'hit 4/4, "
      f"FA 0/1, +1.000' ({loc(RS, A['r_b2_reg44'])}) counts all nine concepts, while 'its own CI, which spans -0.288 to "
      f"+1.000' ({loc(RS, A['r_b2_reg_ci'])}) is the eight-concept cell's: b2_analysis.json `register.sft.ci` = "
      f"newcombe(2, 2, 0, 1) = [{nc_8[0]:+.4f}, {nc_8[1]:+.4f}], whereas newcombe(4, 4, 0, 1) = "
      f"[{nc_9[0]:+.4f}, {nc_9[1]:+.4f}]. The JSON (eight concepts, 2/2) governs the greedy register row in section 5.")
    w("")
    # 2(c) protocol differences
    w("### 2(c) Is the protocol otherwise identical to B2-r?")
    w("")
    # prompts identical
    fr = framing_cfg["fidelity"]["framing"]
    qtpl = framing_cfg["shared"]["trial_question"]
    prompts_same = (fr == v1.MACAR_FRAMING and qtpl == v1.TRIAL_QUESTION and
                    all(b2_prompt.build_prompt_arm(n, fr, qtpl) == b2r_prompt.trial_prompt(n)
                        for n in range(1, 97)))
    fsha = hashlib.sha256(v1.MACAR_FRAMING.encode()).hexdigest()[:16]
    assert all(b2["fidelity"][s]["framing_sha16"] == fsha for s in STAGES)
    assert all(b2["fidelity"][s]["trial_question"] == qtpl for s in STAGES)
    assert b2["fidelity"]["base"]["audit"] == {k: list(v) for k, v in A_B2.__dict__.items()}
    prov_diff = {}
    for s in STAGES:
        pa, pb = dict(b2["fidelity"][s]["provenance"]), dict(ctl[s]["provenance"])
        prov_diff[s] = sorted(k for k in set(pa) | set(pb) if pa.get(k) != pb.get(k))
    exp_dose = {s: sorted({round(t["dose"]["frac_equivalent"], 4) for t in exp[s]["trials"] if t["injected"]})
                for s in EXP_STAGES}
    # round 2: the control stimulus set. The prompt carries the trial number, so the SET of control
    # trial numbers is part of the stimulus, not only n.
    b2_ctl_nums = {s: sorted(t["trial"] for t in b2["fidelity"][s]["trials"] if not t["injected"]) for s in STAGES}
    b2_all_nums = {s: sorted(t["trial"] for t in b2["fidelity"][s]["trials"]) for s in STAGES}
    assert all(b2_all_nums[s] == list(range(1, C_B2["N_TRIALS"] + 1)) for s in STAGES)
    assert all(b2_ctl_nums[s] == b2_ctl_nums["base"] for s in STAGES) and len(b2_ctl_nums["base"]) == 24
    b2r_ctl_nums = {s: sorted(t["trial"] for t in ctl[s]["trials"]) for s in STAGES}
    assert all(b2r_ctl_nums[s] == list(range(1, C_B2R["CONTROL_N"] + 1)) for s in STAGES)
    restr = {}
    for s in STAGES:
        sub_ = [t for t in ctl[s]["trials"] if t["trial"] in set(b2_ctl_nums[s])]
        r1_ = [pipe_v1(t["response_raw"])[2] for t in sub_]
        restr[s] = {"v2": [sum(t["claimed_detection"] is True for t in sub_), sum(t["claimed_detection"] is not None for t in sub_)],
                    "v1": [r1_.count(True), sum(x is not None for x in r1_)], "trials": len(sub_)}
    # round 5: section 4's read on the restricted set needs no tokenizer, so it is computed here, outside the
    # cap emulation (round 4 computed it inside, and the tokenizer-absent path emptied it)
    rel_k = {s: {k[1] for k in {**READ_NON_ASSERTING, **READ_AMBIGUOUS, **READ_FLAG3} if k[0] == s} for s in STAGES}
    restr_rd: dict = {}
    for s in ("base", "sft"):
        rfa_ = sorted(t["trial"] for t in ctl[s]["trials"]
                      if t["trial"] in set(b2_ctl_nums[s]) and t["claimed_detection"] is True)
        assert len(rfa_) == restr[s]["v2"][0]
        restr_rd[s] = {"restricted_fa_trials": rfa_,
                       "restricted_relabelled_among": sorted(set(rfa_) & rel_k[s]),
                       "restricted_fa_read": [next(r_["read"] for r_ in read42 if r_["stage"] == s and r_["trial"] == n_)
                                              for n_ in rfa_]}
    assert restr_rd["base"]["restricted_fa_trials"] == [12, 16, 41, 42] and not restr_rd["base"]["restricted_relabelled_among"]
    assert set(restr_rd["base"]["restricted_fa_read"]) == {"assertion"}
    restr_sft_f3 = [n_ for n_ in restr_rd["sft"]["restricted_relabelled_among"] if ("sft", n_) in READ_FLAG3]
    assert restr_rd["sft"]["restricted_fa_trials"] == [12, 16, 42]
    assert restr_sft_f3 == restr_rd["sft"]["restricted_relabelled_among"] == [16]
    diffs = [
        ("temperature", "0.0", "1.0", f"{R2}@{P}:{L['b2_temp']} vs {RR}@{P}:{L['rr_temp']} / artifact `temp`", "yes"),
        ("max new tokens", "60", "100", f"{R2}@{P}:{L['b2_maxtok']} vs {RR}@{P}:{L['rr_maxtok']} / artifact `max_tokens`", "yes"),
        ("per-trial seed", "20260823 + n", "20260824 + n", f"{R2}@{P}:{L['b2_seed']} vs artifact `seed`",
         f"no: inert at temperature 0 ({loc(RS, A['r_seedinert'])}), so B2's outcomes do not depend on it; in B2-r it "
         f"selects which sample is drawn, not the rate"),
        ("detection scorer", "v1 `claims_detection` (substring)", "v2 `claims_detection_v2` (conditional-stripped, word-bounded)",
         f"{D1}@{P}:{L['d1_claims']} vs {D2}@{P}:{L['d2_claims']}", "yes"),
        ("segmentation", "`segment_own_turn` (turn markers)", "`segment_own_turn_v2` (turn markers + 'Trial N:' echo)",
         f"{D1}@{P}:{L['d1_seg']} vs {D2}@{P}:{L['d2_seg']}", "yes"),
        ("audit frame fragments", f"{len(A_B2.frame_fragments)}: {list(A_B2.frame_fragments)}",
         f"{len(A_B2R.frame_fragments)}: {list(A_B2R.frame_fragments)}",
         f"{R2}@{P}:{L['b2_audit']} vs {RR}@{P}:{L['rr_audit']}", "yes"),
        ("control trials per stage", "24 (fidelity arm)", "96 (section 1); 48 (section 3)", "artifact trial rows", "precision only"),
        ("concepts on injected trials", "nine (eight Macar + evaluative axis)", "eight (section 3)", "artifact `concepts` / trial rows", "no (controls)"),
        ("dose", "stage's A4 MED frac on the axis family: " + ", ".join(
            f"{s} L{b2['fidelity'][s]['layer']} frac {b2['fidelity'][s]['frac']}" for s in STAGES),
         "MED_c 1.0 in their convention at L44, frac-equivalent per concept: " + "; ".join(
             f"{s} {exp_dose[s][0]}-{exp_dose[s][-1]}" for s in EXP_STAGES),
         "artifact `layer`/`frac`; b2r_explore trials[].dose", "no (controls)"),
        ("base concept vectors", "L60, 'User: Tell me about <Concept>' template", "L44 re-extraction, bare template (no section 3 at base)",
         f"{loc(AG, 71, 79)}", "no (controls)"),
        ("arms", "fidelity + register", "fidelity only", "artifact `arm`", "n/a"),
        ("decidable floors", f"{C_B2['FLOOR']} of 24 per pole", "64 of 96 (section 1); 32 of 48 (section 3)",
         f"{R2}@{P}:{L['b2_floor']} vs {BRA}@{P}:{L['bra_cfloor']}-{L['bra_efloor']}", "reading only"),
        ("control trial numbers (the prompt carries the trial number)",
         f"24 of 1..{C_B2['N_TRIALS']}, by seeded permutation, the same 24 at every stage (max {max(b2_ctl_nums['base'])}): "
         f"{b2_ctl_nums['base']}", f"all of 1..{C_B2R['CONTROL_N']} (section 1)",
         f"{R2}@{P}:{L['b2_plan']} vs {RR}@{P}:{L['rr_ctl_loop']}; artifact trial rows",
         "yes (stimulus set), only through the prompt's trial number: B2 never ran trial numbers "
         f"{C_B2['N_TRIALS'] + 1}-{C_B2R['CONTROL_N']} (or its injected numbers) as controls; restricted counts in 2(d)"),
    ]
    w("| # | parameter | B2 (greedy) | B2-r (sampled) | locator | touches the control-trial FPR? |")
    w("|---|---|---|---|---|---|")
    for i, (a_, b_, c_, d_, e_) in enumerate(diffs, 1):
        w(f"| {i} | {a_} | {b_} | {c_} | {d_} | {e_} |")
    w("")
    w(f"Identical between the two: framing (MACAR_FRAMING, sha16 {fsha}, asserted on every B2 fidelity artifact), "
      f"trial question and completion template -- the full prompt for trial n is byte-identical for n = 1..96 "
      f"(record prompt builders compiled from both runners): {'YES' if prompts_same else 'NO'} -- per trial number; the "
      f"SET of control trial numbers differs (row 13); the ban-list builder; "
      f"the uncached generation path; the adapter source. Provenance fields (model path, dtype, backend, GPU, CUDA, "
      f"determinism flags, adapter seed, library versions) differing between "
      f"b2_fidelity_<stage>.json and b2r_control_<stage>.json: " +
      "; ".join(f"{s}: {prov_diff[s] or 'none'}" for s in STAGES) + ".")
    w("")
    ctl_touch = [d[0].split(" (")[0] for d in diffs if d[4].startswith("yes")]
    n_diff_ctl = len(ctl_touch)
    assert n_diff_ctl == 6 and len(diffs) == 13
    w(f"**Verdict for 2(c): the protocol is not otherwise identical.** {len(diffs)} parameters differ; "
      f"{n_diff_ctl} of them can change what a control trial yields ({', '.join(ctl_touch)}; the last only through the "
      f"prompt's trial number); the per-trial seed differs "
      f"too but is inert at temperature 0, and the control n differs (precision). The record's attribution sentence says "
      f"'with format, framing, checkpoint and prompt unchanged' ({loc(RS, A['r_temp0'], A['r_temp0c'])}); that is true "
      f"of those four per trial number, and the scorer, segmenter, audit, max-token cap and control trial-number set "
      f"also changed (and the seeds, inertly).")
    w("")
    # 2(d) cross-scoring
    w("### 2(d) Which of the differences can be removed without a model (computed-new, post-hoc, descriptive)")
    w("")
    w(f"The scorer, segmenter and audit act on stored text, so they can be swapped on the committed transcripts "
      f"with the record's own frozen code. Post-hoc in the sense of CLAUDE.md@{P}:{rule11} (rule 11): this "
      f"informs, it licenses nothing. The seed is inert at temperature 0. The token cap can also be emulated without "
      f"a model: the adapter seeds once per trial and draws tokens one at a time, and the cap only ends the loop "
      f"({AD}@{P}:{L['ad_seed'] - 1}-{L['ad_seed']}, :{L['ad_loop']}-{L['ad_append']}), so a 60-token run at the same "
      f"seed is the first 60 tokens of the 100-token run; the second table below does that cut on a re-encoding of "
      f"the stored text (approximate). What cannot be emulated is temperature.")
    w("")
    w("| stage | B2 controls, v1 as recorded | B2 controls rescored v2 | B2-r controls, v2 as recorded | B2-r controls rescored v1 |")
    w("|---|---|---|---|---|")
    cross = {}
    for s in STAGES:
        b2c = [t for t in b2["fidelity"][s]["trials"] if not t["injected"]]
        r1 = [pipe_v2(t["response_raw"])[2] for t in b2c]
        rc = [pipe_v1(t["response_raw"])[2] for t in ctl[s]["trials"]]
        a_v2 = (r1.count(True), sum(x is not None for x in r1))
        a_v1 = (rc.count(True), sum(x is not None for x in rc))
        cross[s] = {"b2_v1": (b2ctl[s][1], b2ctl[s][0]), "b2_v2": a_v2,
                    "b2r_v2": (ctl[s]["affirm"], ctl[s]["decidable"]), "b2r_v1": a_v1}
        w(f"| {s} | {b2ctl[s][1]}/{b2ctl[s][0]} | {a_v2[0]}/{a_v2[1]} | {ctl[s]['affirm']}/{ctl[s]['decidable']} "
          f"= {ctl[s]['affirm'] / ctl[s]['decidable']:.4f} | {a_v1[0]}/{a_v1[1]} = {a_v1[0] / a_v1[1]:.4f} |")
    w("")
    w("Under either scorer the greedy controls make no false alarms and the sampled controls false-alarm at base "
      "and SFT. The scorer/segmenter/audit change does not account for the B2 vs B2-r difference in control FPR.")
    w("")
    restr_elev = all(restr[s][v][0] > 0 for s in ("base", "sft") for v in ("v1", "v2"))
    restr_zero = all(restr[s][v][0] == 0 for s in ("dpo", "instruct") for v in ("v1", "v2"))
    w(f"**The control stimulus set (2(c) row 13; computed-new, post-hoc, descriptive).** B2-r section 1 controls "
      f"restricted to B2's {len(b2_ctl_nums['base'])} control trial numbers (same prompt per trial number; B2-r's "
      f"temperature, cap and seeds), false alarms / decidable: " +
      "; ".join(f"{s} v2 {restr[s]['v2'][0]}/{restr[s]['v2'][1]} (v1 pipeline {restr[s]['v1'][0]}/{restr[s]['v1'][1]})"
                for s in STAGES) +
      f" of {restr['base']['trials']} trials per stage, against B2's greedy controls " +
      "; ".join(f"{s} {b2ctl[s][1]}/{b2ctl[s][0]}" for s in STAGES) +
      f". Base and SFT still false-alarm on B2's own trial numbers: {'YES' if restr_elev else 'NO'}; DPO and instruct "
      f"stay at zero: {'YES' if restr_zero else 'NO'}. The trial-number set does not account for the difference either.")
    w("")
    w("**B2's 60-token cap emulated on B2-r's controls (computed-new, post-hoc, descriptive, approximate; the "
      "tokenizer is an input outside the record -- header).** Procedure: re-encode each stored `response_raw` "
      "(no special tokens), keep the first N ids, decode, strip, then run the record's own pipelines (v2 as B2-r "
      "scored; v1 with B2's audit as B2 scored). Cells: false alarms / decidable control trials.")
    w("")
    if emu["run"]:
        w(f"| stage | B2-r controls, v2, uncut (of record) | v2 cut at {CAP_EMU} | v1 cut at {CAP_EMU} | v2 / v1 cut at {CAP_BRACKET[0]} | "
          f"v2 / v1 cut at {CAP_BRACKET[1]} | B2 greedy controls, v1 (of record) | one-sided Fisher p, v1 cut at {CAP_EMU} vs B2 greedy |")
        w("|---|---|---|---|---|---|---|---|")
        for s in STAGES:
            e_ = emu["per_stage"][s]["fa_decidable_by_cap"]
            g_ = emu["per_stage"][s]["b2_fidelity_control_v1_recorded"]
            c60v2, c60v1 = e_[str(CAP_EMU)]["v2"], e_[str(CAP_EMU)]["v1"]
            lo_, hi_ = e_[str(CAP_BRACKET[0])], e_[str(CAP_BRACKET[1])]
            w(f"| {s} | {ctl[s]['affirm']}/{ctl[s]['decidable']} = {ctl[s]['affirm'] / ctl[s]['decidable']:.4f} | "
              f"{c60v2[0]}/{c60v2[1]} = {c60v2[0] / c60v2[1]:.4f} | {c60v1[0]}/{c60v1[1]} = {c60v1[0] / c60v1[1]:.4f} | "
              f"{lo_['v2'][0]}/{lo_['v2'][1]} / {lo_['v1'][0]}/{lo_['v1'][1]} | {hi_['v2'][0]}/{hi_['v2'][1]} / "
              f"{hi_['v1'][0]}/{hi_['v1'][1]} | {g_[0]}/{g_[1]} | "
              f"{pfmt(emu['per_stage'][s]['fisher_p_one_sided_cap60_v1_vs_b2_greedy_v1'])} |")
        w("")
        w("Fisher: one-sided exact on [[FA_cut, decidable_cut - FA_cut], [FA_B2, decidable_B2 - FA_B2]], H1: the cut "
          "B2-r control FA rate > the B2 greedy control FA rate; P(X >= FA_cut) with both margins fixed; asserted equal "
          "to the record's `valence_core.stats.fisher_one_sided`. Post-hoc and descriptive (rule 11); it licenses "
          "nothing.")
        w("")
        w("Fidelity of the emulation (why it is approximate). Re-encoding is not the generated ids: the model may emit "
          "non-canonical token sequences, the stored text is stripped, and the local tokenizer file is not the run's "
          "(header). Diagnostics per stage: B2-r controls whose decode(encode(text)) == text; B2-r controls whose "
          f"re-encoding is longer than the 100-token cap (impossible for exact ids); B2-r controls the {CAP_EMU} cut "
          f"actually shortens; and, as a calibration on B2's own {CAP_EMU}-capped generations (both arms), how many "
          f"re-encode longer than {CAP_EMU}.")
        w("")
        w(f"| stage | round trip identical, skip_special_tokens False (this item) / True | re-encoded > 100 (max) | cut at {CAP_EMU} shortens | B2 texts re-encoded > {CAP_EMU} (max) |")
        w("|---|---|---|---|---|")
        for s in STAGES:
            d_ = emu["per_stage"][s]
            w(f"| {s} | {d_['roundtrip_identical']}/{d_['b2r_control_trials']} / "
              f"{d_['roundtrip_identical_skip_special_tokens_true']}/{d_['b2r_control_trials']} | {d_['reencoded_len_over_100']}/"
              f"{d_['b2r_control_trials']} ({d_['reencoded_len_max']}) | {d_['reencoded_len_over_60']}/{d_['b2r_control_trials']} | "
              f"{d_['b2_reencoded_len_over_60']}/{d_['b2_trials_calibration']} ({d_['b2_reencoded_len_max']}) |")
        w("")
        ps_ = emu["per_stage"]
        fails_ = [(s, f_) for s in STAGES for f_ in ps_[s]["roundtrip_fails_with_skip_true"]]
        cuts_eq = all(ps_[s]["cut_verdicts_equal_under_both_decode_settings"] for s in STAGES)
        tfl = emu.get("transformers_local", {})
        w("Decode setting (round 2). This item decodes with `skip_special_tokens=False`; the record's adapter decodes with "
          f"transformers' `decode` and passes no `skip_special_tokens` ({AD}@{P}:{L['ad_decode']}-{L['ad_decode'] + 1}), whose "
          f"default is False (installed transformers {tfl.get('version')}: default "
          f"{tfl.get('decode_default_skip_special_tokens')}; the run used transformers {emu['run_transformers_version']}, "
          f"per the artifacts' provenance, not checked here). The `tokenizers` library's own `Tokenizer.decode` defaults to "
          f"True (installed {emu['library']}, docstring: {emu['tokenizers_decode_default_skip_special_tokens']}). With True "
          f"the round trip fails on " + "; ".join(
              f"{s} trial {f_['trial']} (contains the literal text {', '.join('`' + x + '`' for x in f_['literal_special_strings'])}, from "
              f"character {f_['first_literal_char_offset']}, after {f_['tokens_before_literal']} tokens)" for s, f_ in fails_) +
          ", mid-text: the model must have written these strings as ordinary text pieces (special-token ids are banned in generation, 'banned tokens' "
          "row in 1(c)), and the re-encoding maps each to one special-token id, which a skipping decode drops. Every cut "
          f"verdict at {CAP_BRACKET[0]}/{CAP_EMU}/{CAP_BRACKET[1]} is the same under both settings: "
          f"{'YES' if cuts_eq else 'NO'}. The same mapping shortens the re-encoding by a few tokens wherever the literal "
          f"falls before the cut, so the cut lands later in the text than the generated ids would: " + "; ".join(
              f"{s} trial {f_['trial']} (literal after {f_['tokens_before_literal']} tokens): "
              + ("before every cut, affected" if f_['tokens_before_literal'] < CAP_BRACKET[0] else
                 "after every cut, unaffected" if f_['tokens_before_literal'] >= CAP_BRACKET[1] else "between the cuts")
              for s, f_ in fails_) + "; one more reason the emulation is approximate.")
        w("")
        surv = all(ps_[s]["fa_decidable_by_cap"][str(c)][v][0] > 0 for s in ("base", "sft")
                   for c in (CAP_BRACKET[0], CAP_EMU, CAP_BRACKET[1]) for v in ("v1", "v2"))
        zero_pd = all(ps_[s]["fa_decidable_by_cap"][str(c)][v][0] == 0 for s in ("dpo", "instruct")
                      for c in (CAP_BRACKET[0], CAP_EMU, CAP_BRACKET[1]) for v in ("v1", "v2"))
        emu["base_sft_elevated_at_every_cut"] = surv
        emu["dpo_instruct_zero_at_every_cut"] = zero_pd
        w(f"Reading (descriptive). Base and SFT controls still false-alarm at every cut and under both pipelines: "
          f"{'YES' if surv else 'NO'}; DPO and instruct stay at zero: {'YES' if zero_pd else 'NO'}. On this approximate "
          f"emulation the 60/100-token cap does not account for the B2 vs B2-r difference either; with the scorer, "
          f"segmenter and audit swapped (table above), the control trial-number set restricted (above) and the seed "
          f"inert at temperature 0, the remaining protocol "
          f"difference that bears on the control FPR is temperature (with the injected-trial differences, rows 8-10 of the 2(c) table, "
          f"irrelevant to controls). Base: B2-r controls re-encoded past 100: {ps_['base']['reencoded_len_over_100']}; "
          f"B2 texts re-encoded past {CAP_EMU}: {ps_['base']['b2_reencoded_len_over_60']} -- the calibration is "
          f"{'clean at base' if ps_['base']['reencoded_len_over_100'] == 0 and ps_['base']['b2_reencoded_len_over_60'] == 0 else 'not clean at base'}. "
          f"At the post-trained stages some re-encodings exceed the cap they were generated under, so the cut point "
          f"there is less exact (SFT, the other elevated stage, included); the {CAP_BRACKET[0]}/{CAP_BRACKET[1]} brackets "
          f"show how much the counts move with the cut. None of this is a record figure; it bears only on the "
          f"suspected cause of the STOP below, not on the STOP.")
        w("")
        # round 4: section 4's read carried to the cut and to the restricted set (post-hoc, descriptive)
        cut_rd: dict = {}
        for s in ("base", "sft"):
            fa60_ = sorted(emu_own60[s])
            ov_ = sorted(set(fa60_) & rel_k[s])
            for n_ in ov_:                    # the mechanical check, on the cut text the scorer saw
                low_ = " " + v2.strip_conditionals(emu_own60[s][n_]).strip().lower()
                ms_ = [m.start() for p_ in v2._AFFIRM_RX for m in re.finditer(p_, low_)]
                car_ = READ_SPEC[(s, n_)][1]
                spans_ = [m.span() for c_ in car_ for m in re.finditer(re.escape(c_), low_)]
                trunc_ = []
                for c_ in car_:               # a carrier the cut ends inside: its surviving prefix (>= 10 chars)
                    k_ = next((k for k in range(len(c_) - 1, 9, -1) if low_.endswith(c_[:k])), None)
                    if k_ is not None:
                        spans_.append((len(low_) - k_, len(low_)))
                        trunc_.append(n_)
                assert ms_ and all(any(a <= x < b for a, b in spans_) for x in ms_), (s, n_)
                msk_ = list(low_)
                for a, b in spans_:
                    msk_[a:b] = " " * (b - a)
                msk_ = "".join(msk_)
                assert not any(re.search(p_, msk_) for p_ in v2._AFFIRM_RX), (s, n_)
                cut_rd.setdefault(s, {}).setdefault("carrier_truncated_at_cut", []).extend(trunc_)
            dec60_ = emu["per_stage"][s]["fa_decidable_by_cap"][str(CAP_EMU)]["v2"][1]
            k_ = len(fa60_) - len(ov_)
            gb_ = emu["per_stage"][s]["b2_fidelity_control_v1_recorded"]
            p_ = fisher_hits_gt_fa(k_, dec60_, gb_[0], gb_[1])
            assert abs(p_ - stats.fisher_one_sided(k_, dec60_ - k_, gb_[0], gb_[1])) < 1e-12
            cut_rd.setdefault(s, {}).update(      # the restricted keys: restr_rd, computed above (round 5)
                fa_cut60=fa60_, relabelled_among=ov_, without=[k_, dec60_], b2_greedy=list(gb_),
                fisher_p_one_sided=p_, **{k: list(v) for k, v in restr_rd[s].items()})
            cut_rd[s].setdefault("carrier_truncated_at_cut", [])
        cb_ = cut_rd["base"]
        assert cb_["relabelled_among"] == [8, 33, 35, 36, 44, 49, 89, 94] and cb_["without"] == [16, 57]
        emu["section4_read_at_cut60_post_hoc"] = cut_rd
        b_na_ = [n_ for n_ in cb_["relabelled_among"] if ("base", n_) in READ_NON_ASSERTING]
        b_am_ = [n_ for n_ in cb_["relabelled_among"] if ("base", n_) in READ_AMBIGUOUS]
        cs_ = cut_rd["sft"]
        cut_read_sentence = (
            f"on Code's read (section 4) {len(cb_['relabelled_among'])} of the {len(cb_['fa_cut60'])} base FAs at the "
            f"{CAP_EMU} cut are the non-asserting/ambiguous class (non-asserting {b_na_}, ambiguous {b_am_}); without them "
            f"base is {cb_['without'][0]}/{cb_['without'][1]} vs {cb_['b2_greedy'][0]}/{cb_['b2_greedy'][1]} (one-sided "
            f"Fisher p {cb_['fisher_p_one_sided']:.4f}) and the restricted {restr['base']['v2'][0]}/{restr['base']['v2'][1]} "
            f"contains none of them; the reading is unchanged")
        w(f"**Section 4's read carried to these cuts (round 4; computed-new, post-hoc, descriptive).** The base counts "
          f"above are scorer v2's: {cut_read_sentence}. Detail: the base FAs at the {CAP_EMU} cut are trials "
          f"{cb_['fa_cut60']} (trial 34 of the full-length 25 does not false-alarm at the cut); for each relabelled one "
          f"the script re-asserts section 4's mechanical check on the cut text the scorer saw (every v2 affirm match lies "
          f"inside the carrier, or inside its surviving prefix where the cut falls within it: trial(s) "
          f"{cb_['carrier_truncated_at_cut'] or 'none'}; with those spans blanked no affirm pattern matches). The "
          f"restricted base FAs are trials {cb_['restricted_fa_trials']}, each read as an assertion in section 4. The "
          f"Fisher test has the form of the one above (one-sided exact, H1: the cut B2-r rate > B2's greedy rate), here "
          f"on the v2 cut counts against B2's recorded greedy control cell (v1), with the "
          f"{len(cb_['relabelled_among'])} counted as decidable non-claims (FLAG-3's convention). Extended to SFT: {len(cs_['relabelled_among'])} of its {len(cs_['fa_cut60'])} FAs at the cut "
          f"are section 4's FLAG-3/ambiguous trials ({cs_['relabelled_among']}); without them sft is "
          f"{cs_['without'][0]}/{cs_['without'][1]} vs {cs_['b2_greedy'][0]}/{cs_['b2_greedy'][1]} (one-sided Fisher p "
          f"{cs_['fisher_p_one_sided']:.4f}); its restricted {restr['sft']['v2'][0]}/{restr['sft']['v2'][1]} contains "
          f"{cs_['restricted_relabelled_among'] or 'none of them'}. Base and SFT stay elevated, so the suspected cause's "
          f"reading is unchanged; the STOP is unaffected.")
    else:
        w(f"Not run: {emu['reason']}. The cap therefore stays confounded with temperature in this raw.")
        w("")
        # round 5: the restricted-set part of section 4's read needs no tokenizer (ledger row 23's '(2(d))' points here)
        w(f"**Section 4's read on the restricted set (round 5; computed-new, post-hoc, descriptive; needs no "
          f"tokenizer).** The restricted base FAs are trials {restr_rd['base']['restricted_fa_trials']}, each read as an "
          f"assertion in section 4, so the restricted {restr['base']['v2'][0]}/{restr['base']['v2'][1]} contains none of "
          f"its relabelled trials; sft's restricted FAs {restr_rd['sft']['restricted_fa_trials']} include FLAG-3's "
          f"{', '.join(map(str, restr_sft_f3))}. The STOP is unaffected.")
    w("")
    w("**(ii) outcome against the block (:31, :36).** Exists as a committed artifact with its own stamp: yes (commit, "
      "entry, raw; greedy decoding per the runner code and the log, no temperature field). Zero detection claims at "
      "every stage: yes, on the record's referent, the fidelity arm (disclosure: the register arm, a scorer-defect "
      "cell, has 4 at SFT). Protocol otherwise identical: **no** (2(c)). This is the block's fail case for (ii): "
      "**STOP on link 4's ROC paragraph** (block :36: 'the heat plan withholds it'). Section 8.")
    w("")
    stops.append({"subitem": "N2(ii) greedy run -> link 4's ROC paragraph",
                  "discrepancy": f"The greedy run (B2, commit {add_b2[0][:7]}) exists and its fidelity arm makes zero detection "
                                 f"claims at every stage (n decidable inj/ctl, eight concepts: " +
                                 ", ".join(f"{r['stage']} {r['di8']}/{r['dc']}" for r in greedy_rows if r['arm'] == 'fidelity') +
                                 "), but its protocol is not otherwise identical to B2-r: max new tokens 60 vs 100, "
                                 "scorer v1 vs v2, segmenter v1 vs v2, a 6- vs 2-fragment audit, 24 vs 96 controls per "
                                 f"stage drawn from different trial numbers (B2: 24 of 1..48, max {max(b2_ctl_nums['base'])}; "
                                 "B2-r: 1..96; the prompt carries the trial number), "
                                 "a different dose/concept set on injected trials, and a different seed base "
                                 "(20260823 vs 20260824; inert at temperature 0). Disclosure: its register arm (not the "
                                 "referent) has 4 v1-scored claims at SFT, in a cell the record calls a scorer defect.",
                  "suspected_cause": "B2 and B2-r are two campaigns; B2-r was redesigned under ADDENDUM-g3 v1.2 after B2's "
                                     "stop, changing decoding, scorer, segmentation, audit and n together. No greedy run under "
                                     "the B2-r protocol exists in the record. Post-hoc, model-free (2(d)): cross-scoring removes "
                                     "the scorer/segmenter/audit difference; the seed is inert at temperature 0; restricted to "
                                     f"B2's control trial numbers, B2-r's controls still false-alarm at base and SFT (v2: base "
                                     f"{restr['base']['v2'][0]}/{restr['base']['v2'][1]}, sft {restr['sft']['v2'][0]}/"
                                     f"{restr['sft']['v2'][1]}); " +
                                     ("an approximate emulation of the 60-token cap (truncating B2-r's stored generations on a "
                                      "re-encoding with a tokenizer outside the record) leaves base and SFT controls elevated "
                                      f"(v2 at 60: base {emu['per_stage']['base']['fa_decidable_by_cap'][str(CAP_EMU)]['v2'][0]}/"
                                      f"{emu['per_stage']['base']['fa_decidable_by_cap'][str(CAP_EMU)]['v2'][1]}, sft "
                                      f"{emu['per_stage']['sft']['fa_decidable_by_cap'][str(CAP_EMU)]['v2'][0]}/"
                                      f"{emu['per_stage']['sft']['fa_decidable_by_cap'][str(CAP_EMU)]['v2'][1]}), so the residual "
                                      "difference bearing on the control FPR is temperature, approximately."
                                      if emu["run"] else "the cap was not emulated (tokenizer unavailable), so it stays "
                                      "confounded with temperature.") +
                                     " The STOP's trigger (the protocol is not otherwise identical) is unchanged."})
    fig("greedy run exists as a committed artifact with its own stamp", f"B2, commit {add_b2[0][:7]} {add_b2[1]}",
        f"data/olmo/b2_{{fidelity,register}}_*.json; {loc(RS, A['r_b2_complete'])}", "reproduced",
        "reproduced as artifacts and commit; that the run is greedy rests on the runner code and the log (the B2 "
        "temperature row above, log-only), "
        "since the artifacts carry no timestamp or temperature field", named="block :31")
    fig("greedy run: zero detection claims at every stage (fidelity arm, the record's referent)",
        "/".join(str(claims_any[("fidelity", s)]) for s in STAGES) + " (base/sft/dpo/instruct)",
        f"data/olmo/b2_fidelity_*.json:trials[].claimed_detection; referent {loc(RS, A['r_temp0'], A['r_temp0b'])}",
        "reproduced", "the positive-control arm; the one an F2 greedy row would show", named="block :31")
    fig("disclosure: greedy run, register arm claims (not the block's referent; not a detection point)",
        "/".join(str(reg_claims[s]) for s in STAGES) + " (base/sft/dpo/instruct)",
        "data/olmo/b2_register_*.json:trials[].claimed_detection", "reproduced",
        f"4 v1-scored claims at SFT, all on injected trials, in a cell the record calls a scorer defect "
        f"({loc(RS, A['r_reg_def'], A['r_reg_def_end'])})", named=f"{loc(RS, A['r_b2_reg44'])} (a disclosure; not a block figure)")
    fig("greedy run: n per stage (fidelity, eight concepts, decidable inj/ctl)",
        ", ".join(f"{r['stage']} {r['di8']}/{r['dc']}" for r in greedy_rows if r['arm'] == 'fidelity'),
        "data/olmo/b2_analysis.json:fidelity.*.n_*_decidable", "reproduced", "instruct below the 16-of-24 floor",
        named="block :31")
    fig("greedy run: protocol otherwise identical", f"no: {len(diffs)} parameters differ ({n_diff_ctl} can change a "
        f"control trial's outcome, the control trial-number set only through the prompt; the seed differs but is inert "
        f"at temperature 0)",
        f"{R2}, {RR}, artifacts", "discrepant", "block fail case for (ii): STOP on link 4's ROC paragraph; a "
        "pass-condition outcome, not a note figure: N1's discrepant clause (block :23) does not attach -- the "
        "consequence is the (ii) STOP (block :36)",
        named="block :31")
    if emu["run"]:
        e60 = {s: emu["per_stage"][s]["fa_decidable_by_cap"][str(CAP_EMU)] for s in STAGES}
        fig(f"B2-r controls at an emulated {CAP_EMU}-token cap (v2 / v1 pipelines)",
            "; ".join(f"{s} {e60[s]['v2'][0]}/{e60[s]['v2'][1]} / {e60[s]['v1'][0]}/{e60[s]['v1'][1]}" for s in STAGES),
            f"data/olmo/b2r_control_*.json:trials[].response_raw + local tokenizer {emu['sha256'][:16]} (outside the record)",
            "computed-new", "post-hoc, descriptive, approximate (re-encoded cut; the tokenizer file is not the run's); "
                            "bears on the STOP's suspected cause only; "
                            f"{len(cut_rd['base']['relabelled_among'])} of the base {len(cut_rd['base']['fa_cut60'])} "
                            f"are section 4's non-asserting/ambiguous class (without them "
                            f"{cut_rd['base']['without'][0]}/{cut_rd['base']['without'][1]}, one-sided Fisher p "
                            f"{cut_rd['base']['fisher_p_one_sided']:.4f} vs B2's greedy "
                            f"{cut_rd['base']['b2_greedy'][0]}/{cut_rd['base']['b2_greedy'][1]}; 2(d))"
                            # round 5: the same disclosure for the SFT value in this row
                            f"; sft: {len(cut_rd['sft']['relabelled_among'])} of {len(cut_rd['sft']['fa_cut60'])} "
                            f"({cut_rd['sft']['relabelled_among']}) are section 4's FLAG-3/ambiguous trials (without them "
                            f"{cut_rd['sft']['without'][0]}/{cut_rd['sft']['without'][1]}, p "
                            f"{cut_rd['sft']['fisher_p_one_sided']:.4f}; 2(d))", named="computed-new")
    # round 5: the restricted-set clauses need no tokenizer (restr_rd), so this note is the same with or without it
    fig("B2-r controls restricted to B2's 24 control trial numbers (v2 / v1 pipelines)",
        "; ".join(f"{s} {restr[s]['v2'][0]}/{restr[s]['v2'][1]} / {restr[s]['v1'][0]}/{restr[s]['v1'][1]}" for s in STAGES),
        "data/olmo/b2r_control_*.json:trials[] restricted to data/olmo/b2_fidelity_*.json control trial numbers",
        "computed-new", "post-hoc, descriptive; bears on the STOP's suspected cause only (2(c) row 13, 2(d))" +
        f"; the base FAs {restr_rd['base']['restricted_fa_trials']} include none of section 4's relabelled trials"
        f"; sft's {restr_rd['sft']['restricted_fa_trials']} include FLAG-3's {', '.join(map(str, restr_sft_f3))} (2(d))",
        named="computed-new")

    # =================================================== section 3 (iii)
    w("## 3. N2(iii): '178 decidable trials at DPO and instruct at qualified doses -> zero detection claims of any kind', and the SFT discrimination figure")
    w("")
    tot = 0
    w("| stage | injected decidable (hits) | control decidable (FAs) | decidable total | undecidable: audit / both polarities / neither / empty after strip | trials with any affirm marker (after strip_conditionals) | MED_c | frac-equivalent range |")
    w("|---|---|---|---|---|---|---|---|")
    any_aff = {}
    und_break = {}
    marker_trials = []
    for s in EXP_STAGES:
        e = exp[s]
        dtot = e["inj_decidable"] + e["ctl_decidable"]
        if s in ("dpo", "instruct"):
            tot += dtot
        ab = both = neither = empty = 0
        aff_any = 0
        for t in e["trials"]:
            own = t["response"]
            body = v2.strip_conditionals(own)
            low = " " + body.strip().lower()
            a_ = any(re.search(p_, low) for p_ in v2._AFFIRM_RX)
            d_ = any(re.search(p_, low) for p_ in v2._DENY_RX)
            if a_:
                aff_any += 1
                if s in ("dpo", "instruct"):
                    marker_trials.append((s, t, [p_ for p_ in v2._AFFIRM_RX if re.search(p_, low)]))
            if t["claimed_detection"] is None:
                if t["audit"]:
                    ab += 1
                elif not body.strip():
                    empty += 1
                elif a_ and d_:
                    both += 1
                else:
                    neither += 1
        any_aff[s] = aff_any
        und_break[s] = (ab, both, neither, empty)
        w(f"| {s} | {e['inj_decidable']} ({e['hit']}) | {e['ctl_decidable']} ({e['fa']}) | {dtot} | {ab} / {both} / {neither} / {empty} | "
          f"{aff_any} | {an_r['g3b'][s]['MED_c']} | {exp_dose[s][0]}-{exp_dose[s][-1]} |")
    w("")
    zero_any = all(exp[s]["hit"] == 0 and exp[s]["fa"] == 0 for s in ("dpo", "instruct"))
    w(f"**178 reproduces**: DPO {exp['dpo']['inj_decidable']} + {exp['dpo']['ctl_decidable']} = "
      f"{exp['dpo']['inj_decidable'] + exp['dpo']['ctl_decidable']}, instruct {exp['instruct']['inj_decidable']} + "
      f"{exp['instruct']['ctl_decidable']} = {exp['instruct']['inj_decidable'] + exp['instruct']['ctl_decidable']}; total "
      f"**{tot}** (data/olmo/b2r_explore_{{dpo,instruct}}.json fields `inj_decidable`, `ctl_decidable`). Hits and false "
      f"alarms are zero at both stages: {'YES' if zero_any else 'NO'}. Under the v1 scorer the same transcripts also "
      f"give zero claims at both stages (section 4).")
    w("")
    w(f"'Of any kind', checked one level further. Trials at DPO or instruct whose v2-segmented text contains any v2 "
      f"affirm pattern after conditional stripping, decidable or not: DPO {any_aff['dpo']}, instruct "
      f"{any_aff['instruct']}. Each was read in full (rule 25, CLAUDE.md@{P}:{rule25}); excerpts below are the "
      f"opening sentence and the sentence carrying the marker:")
    w("")
    for s_, t_, pats in marker_trials:
        sents = re.split(r"(?<=[.!?])\s+", t_["response"].replace("\n", " "))
        first = sents[0].strip()
        hit = next((x.strip() for x in sents if any(re.search(p_, " " + x.lower()) for p_ in pats)), "")
        w(f"- {s_} trial {t_['trial']} ({'injected' if t_['injected'] else 'control'}; `claimed_detection` = "
          f"{t_['claimed_detection']}; audit {t_['audit']}; affirm patterns {pats}): opens \"{first[:110]}\"; marker "
          f"sentence \"{hit[:150]}\"")
    w("")
    w("Code's reading: each opens with an explicit denial for this trial and carries the affirm word only in a "
      "hypothetical or meta sentence about how it would answer; the scorer files them undecidable (both polarities). "
      "None is a detection claim on that reading, so 'zero detection claims of any kind' stands, with these two "
      "undecidable control trials disclosed as the closest cases.")
    w("")
    w(f"Decidability rule (section 3, the explore runner): the generated text is bounded by `segment_own_turn_v2` "
      f"({RR}@{P}:{L['rr_seg'][-1]}); the audit ({RR}@{P}:{L['rr_audit']}-{L['rr_audit'] + 4}: empty, a scaffold "
      f"string, the fragments 'I am an interpretability researcher' / 'Do you detect an injected', or a "
      f"repetition regex) excludes it, else `claims_detection_v2` scores it ({RR}@{P}:{L['rr_exp_claim']}). "
      f"`claims_detection_v2` ({D2}@{P}:{L['d2_claims']}-{d2_claims_end}) strips conditional sentences "
      f"(:{L['d2_strip']}), then returns True iff an affirm pattern and no deny pattern matches, False iff the reverse, "
      f"and None if the stripped body is empty or both or neither match. Decidable = `claimed_detection` is not None "
      f"({RR}@{P}:{L['rr_dec_exp']}-{L['rr_dec_exp'] + 1}). Domain of the 178: trials, 96 run per stage, "
      f"decidable ones counted.")
    w("")
    w(f"Dose qualification: MED_c = 1.0 (their convention: raw concept vector x 1.0, constructed as frac = 1.0 x "
      f"||v|| / R_44) at DPO and instruct, from [g3-B] ({BRA}@{P}:{L['bra_g3b']}): the lowest ladder strength "
      f"whose pooled injected about-rate CP interval separates above the uninjected control's AND whose "
      f"degenerate fraction is <= 0.25 ({loc(AG, A['a_medc'])}). b2r_analysis.json `g3b.<stage>.MED_c`; recomputed "
      f"from b2r_qualify_<stage>.json equal: {'YES' if rep_g3b else 'NO'}. MED_c sits at the ladder floor and is "
      f"left-censored, reported as <= 1.0 ({loc(RS, A['r_medc'])}). The realized per-trial frac-equivalents are in the "
      f"table (b2r_explore trials[].dose.frac_equivalent).")
    w("")
    w(f"Log text vs JSON: the record's exploration table prints instruct FPR as 0/45 ({loc(RS, A['r_exp_inst'])}) and "
      f"the next paragraph says '88 and 89 decidable trials' ({loc(RS, A['r_88_89'])}); the JSON has instruct "
      f"`ctl_decidable` = {exp['instruct']['ctl_decidable']}, i.e. 88 and 90. The b2r_analysis.json interval for "
      f"instruct (stored [{an_r['explore']['instruct']['ci'][0]:+.5f}, {an_r['explore']['instruct']['ci'][1]:+.5f}]) "
      f"equals newcombe(0, 44, 0, 46) = [{b2a.newcombe(0, 44, 0, 46)[0]:+.5f}, {b2a.newcombe(0, 44, 0, 46)[1]:+.5f}] "
      f"and not newcombe(0, 44, 0, 45) = [{b2a.newcombe(0, 44, 0, 45)[0]:+.5f}, {b2a.newcombe(0, 44, 0, 45)[1]:+.5f}]. "
      f"The JSON wins; the log's 0/45 and 89 are transcription slips. The block's 178 and F2's 0/46 match the JSON.")
    assert deep_eq(an_r["explore"]["instruct"]["ci"], list(b2a.newcombe(0, 44, 0, 46)))
    w("")
    fig("178 decidable trials at DPO and instruct", f"{tot} = 43 + 45 + 44 + 46",
        "data/olmo/b2r_explore_{dpo,instruct}.json:inj_decidable,ctl_decidable", "reproduced", "", named="block :32")
    def _both(t_):
        lw_ = " " + v2.strip_conditionals(t_["response"]).strip().lower()
        return any(re.search(p_, lw_) for p_ in v2._AFFIRM_RX) and any(re.search(p_, lw_) for p_ in v2._DENY_RX)
    assert all(s_ == "dpo" and not t_["injected"] and t_["claimed_detection"] is None and not t_["audit"] and _both(t_)
               for s_, t_, _ in marker_trials)
    fig("zero detection claims of any kind (DPO, instruct)",
        f"hits 0, FA 0 (v2 and v1); {len(marker_trials)} undecidable DPO control trials "
        f"({', '.join(str(t_['trial']) for _, t_, _ in marker_trials)}) carry an affirm word beside an explicit denial, "
        f"in a hypothetical or meta sentence",
        "data/olmo/b2r_explore_{dpo,instruct}.json:hit,fa,trials[].response", "reproduced",
        "the marker trials were read in full and quoted in section 3", named="block :32")
    fig("log: instruct FA 0/45; '88 and 89 decidable trials'", f"JSON: 0/{exp['instruct']['ctl_decidable']}; 88 and 90",
        f"{loc(RS, A['r_exp_inst'])}; {loc(RS, A['r_88_89'])}", "discrepant", "transcription in the log; the JSON governs",
        named=f"{loc(RS, A['r_exp_inst'])}; :{A['r_88_89']}")
    fig("MED_c 1.0 at SFT/DPO/instruct; base hard stop", "1.0 / 1.0 / 1.0; base None",
        "data/olmo/b2r_analysis.json:g3b.*.MED_c (recomputed from b2r_qualify_*.json)", "reproduced", "left-censored",
        named=f"block :32 ('qualified doses'); value {loc(RS, A['r_medc'])}")

    # SFT discrimination
    es = exp["sft"]
    sens = Fraction(es["hit"], es["inj_decidable"]) - Fraction(es["fa"], es["ctl_decidable"])
    lo_s, hi_s = b2a.newcombe(es["hit"], es["inj_decidable"], es["fa"], es["ctl_decidable"])
    assert deep_eq([lo_s, hi_s], an_r["explore"]["sft"]["ci"])
    p_sft = fisher_hits_gt_fa(es["hit"], es["inj_decidable"], es["fa"], es["ctl_decidable"])
    p_sft_rec = stats.fisher_one_sided(es["hit"], es["inj_decidable"] - es["hit"], es["fa"],
                                       es["ctl_decidable"] - es["fa"])
    assert abs(p_sft - p_sft_rec) < 1e-12
    w("### 3(b) The SFT discrimination figure (+0.096)")
    w("")
    w(f"Definition in the record: **sensitivity = hit rate - false-alarm rate** over decidable trials "
      f"({BRA}@{P}:{L['bra_explore']}; {BA}@{P}:{ba_dprime} names it and declines d'). At SFT: hits "
      f"{es['hit']}/{es['inj_decidable']} injected-decidable, false alarms {es['fa']}/{es['ctl_decidable']} "
      f"control-decidable, sensitivity = {sens} = **{float(sens):+.6f}** "
      f"(data/olmo/b2r_analysis.json `explore.sft.sensitivity` = {an_r['explore']['sft']['sensitivity']!r}). "
      f"Interval: [{lo_s:+.4f}, {hi_s:+.4f}] (field `explore.sft.ci`, recomputed equal), built by the record's "
      f"`newcombe` ({BA}@{P}:{L['ba_newc']}): two two-sided 95% Clopper-Pearson intervals combined by square-and-add "
      f"(a MOVER-type construction with exact component intervals; the record calls it Newcombe, though Newcombe's "
      f"published method uses Wilson components). Test: the record attaches no p-value; its reading is the interval's "
      f"three-state `ci_state` ({D2}@{P}:{L['d2_cistate']}) = '{an_r['explore']['sft']['ci_state']}', screen_hit = "
      f"{an_r['explore']['sft']['screen_hit']}. Computed-new for the block: one-sided Fisher exact (H1: hit rate > FA "
      f"rate) p = {p_sft:.4f} (equal to the record's `fisher_one_sided`).")
    w("")
    w(f"Rounding: {sens} = {float(sens):.6f} rounds to **+0.095** at three decimals. '+0.096' is the record's "
      f"four-decimal +0.0955 ({loc(RS, A['r_exp_sft'])}) rounded again (double rounding). Transcription; the note "
      f"should carry +0.095 (or +0.0955).")
    w("")
    fig("SFT discrimination +0.096", f"{float(sens):+.6f} (= 21/220; +0.095 at 3 dp)",
        "data/olmo/b2r_analysis.json:explore.sft.sensitivity", "discrepant",
        "double rounding of +0.0955; transcription, correct to +0.095", named="block :32")
    fig("SFT interval [-0.105, +0.292]", f"[{lo_s:+.4f}, {hi_s:+.4f}]", "data/olmo/b2r_analysis.json:explore.sft.ci",
        "reproduced", "square-and-add of two 95% two-sided CP intervals; reading = ci_state 'includes'",
        named=f"block :32 (asked for); values {loc(RS, A['r_exp_sft'])}")
    fig("SFT one-sided Fisher p (H1 hit > FA)", f"{p_sft:.4f}", "computed from data/olmo/b2r_explore_sft.json:hit,inj_decidable,fa,ctl_decidable",
        "computed-new", "the record attaches no p to this figure", named="computed-new (block :32 asks for a test)")

    # =================================================== section 4 (iv)
    w("## 4. N2(iv): scorer of record, figure by figure")
    w("")
    w("| figure | campaign / part | scorer of record | segmenter | audit | evidence |")
    w("|---|---|---|---|---|---|")
    w(f"| per-stage FPR 25/58, 17/85, 0/91, 0/91 | B2-r section 1 | detection_v2 `claims_detection_v2` | `segment_own_turn_v2` | {RR} AUDIT (2 fragments) | artifact field `scorer`; {RR}@{P}:{L['rr_ctl_claim']} |")
    w(f"| 2.5-point distance | B2-r section 1 | detection_v2 | v2 | B2-r | as above |")
    w(f"| exploration TPR/FPR, 178, +0.095 | B2-r section 3 | detection_v2 | v2 | B2-r | artifact field `scorer`; {RR}@{P}:{L['rr_exp_claim']} |")
    w(f"| [g3-B] about-rates, MED_c | B2-r section 2 | detection_v2 `about_ness` (not a detection scorer) | v2 | B2-r | {RR} run_qualify |")
    w(f"| greedy row (B2) | B2 | detection.py `claims_detection` (v1) | `segment_own_turn` | {R2} AUDIT (6 fragments) | replay: v1 re-derives every stored verdict, v2 misses {b2_cd_v2}/{b2_cd_n} (section 2(a)); {R2}@{P}:{L['b2_claim']}; no `scorer` field in B2 artifacts |")
    w(f"| FLAG-3 corrected SFT FPR 0.176 | B2-r section 1 | v2 verdicts with two trials relabelled by hand (the v3 spec's ground truth) | v2 | B2-r | {loc(RS, A['r_0176'])}; data/configs/scorer_v3_spec.json `regression_cases` |")
    w("")
    w("contentclass v3/v4/v5 and audit_v3 (valence_core/e2d/) are e2d instruments; no B2 or B2-r artifact or runner names "
      "them (checked below). scorer v3 does not exist: data/configs/scorer_v3_spec.json is a specification only "
      "(field `status`: \"" + spec["status"][:60] + "...\"). The source's own detection grader is not identified by the "
      "record or by the N2vi raw; this item does not establish it.")
    w("")
    ref_e2d = []
    for pth in ([f"data/olmo/b2_{a}_{s}.json" for a in ("fidelity", "register") for s in STAGES] +
                [f"data/olmo/b2r_{p_}_{s}.json" for p_ in ("control", "qualify") for s in STAGES] +
                [f"data/olmo/b2r_explore_{s}.json" for s in EXP_STAGES] + [R2, RR, BA, BRA]):
        if re.search(r"contentclass|audit_v3", text(pth)):
            ref_e2d.append(pth)
    w(f"Files among the B2/B2-r artifacts and runners/analyzers that mention contentclass or audit_v3: {ref_e2d or 'none'}.")
    w("")
    w("**Single scorer version?** All B2-r figures: yes, scorer v2. The block's own N2 figure set also includes the "
      "greedy row, which is scorer v1. So the set is not single-scorer. On the same trials the two versions give "
      "different per-stage FPRs (table 2(d)):")
    w("")
    w("| stage | B2-r controls, v2 (of record) | same transcripts, v1 pipeline | B2 greedy controls, v1 (of record) | same transcripts, v2 pipeline |")
    w("|---|---|---|---|---|")
    for s in STAGES:
        cr = cross[s]
        w(f"| {s} | {cr['b2r_v2'][0]}/{cr['b2r_v2'][1]} = {cr['b2r_v2'][0] / cr['b2r_v2'][1]:.4f} | "
          f"{cr['b2r_v1'][0]}/{cr['b2r_v1'][1]} = {cr['b2r_v1'][0] / cr['b2r_v1'][1]:.4f} | "
          f"{cr['b2_v1'][0]}/{cr['b2_v1'][1]} | {cr['b2_v2'][0]}/{cr['b2_v2'][1]} |")
    w("")
    ex_v1 = {}
    for s in EXP_STAGES:
        inj = [pipe_v1(t["response_raw"])[2] for t in exp[s]["trials"] if t["injected"]]
        cc = [pipe_v1(t["response_raw"])[2] for t in exp[s]["trials"] if not t["injected"]]
        ex_v1[s] = (inj.count(True), sum(x is not None for x in inj), cc.count(True), sum(x is not None for x in cc))
    w("Exploration transcripts under the v1 pipeline (hits/inj-decidable, FA/ctl-decidable): " +
      "; ".join(f"{s} {ex_v1[s][0]}/{ex_v1[s][1]}, {ex_v1[s][2]}/{ex_v1[s][3]}" for s in EXP_STAGES) +
      ". The v1 pipeline decides fewer of these trials than v2 does; the zero-claim pattern at DPO/instruct is the "
      "same under both.")
    w("")
    # FLAG 3
    cases = {c["id"]: c for c in spec["regression_cases"]}
    relabel = []
    for cid in ("sft-16", "sft-76"):
        tn = int(cid.split("-")[1])
        t = next(t for t in ctl["sft"]["trials"] if t["trial"] == tn)
        assert t["response"] == cases[cid]["text"] and t["claimed_detection"] is True
        assert cases[cid]["ground_truth_dv"] is False and cases[cid]["v2_verdict"] is True
        relabel.append(tn)
    k_c = ctl["sft"]["affirm"] - len(relabel)
    lo_c, _ = b2a.clopper_pearson(k_c, ctl["sft"]["decidable"])
    _, hi_d = b2a.clopper_pearson(0, ctl["dpo"]["decidable"])
    tot_aff = sum(ctl[s]["affirm"] for s in STAGES)
    w(f"FLAG-3 correction ({loc(RS, A['r_flag3_a'], A['r_0176'])}): the v3 specification's two regression cases are "
      f"SFT control trials {relabel} (texts asserted verbatim against the artifact; v2 verdict True, ground truth "
      f"False). Relabelled, SFT FPR = {k_c}/{ctl['sft']['decidable']} = {k_c / ctl['sft']['decidable']:.4f} (record "
      f"0.176), CP lower {lo_c:.4f} against the DPO/instruct CP upper {hi_d:.4f} (record 0.1023 > 0.0397). "
      f"The record's relabel is a hand correction of two SFT trials, not an instrument; at SFT it changes no reading "
      f"({loc(RS, A['r_0176'])}). The record's count, '**2 of 42** affirm-scored control trials, both at SFT' "
      f"({loc(RS, A['r_2of42'], A['r_2of42_b'])}): the 42 reproduces (42 = "
      f"{' + '.join(str(ctl[s]['affirm']) for s in STAGES)} = {tot_aff}, the artifacts' `affirm`), and the 2 are the "
      f"spec's two cases; the count itself is a hand reading, and it does not hold on Code's read of the 42 (next).")
    w("")
    w(f"**Code's read of all {len(aff42)} affirm-scored control trials (round 2; rule 25, CLAUDE.md@{P}:{rule25}; post-hoc, "
      f"descriptive; a reading, not an instrument).** Each was read in full. The record ruled that negation-safety must "
      f"cover 'non-asserting contexts AS A CLASS -- belief verbs, conditionals, futures, ability modals' "
      f"({loc(RS, A['r_flag3_class_a'], A['r_flag3_class_b'])}). At base, {read_cnt['base']['non-asserting']} of the "
      f"{ctl['base']['affirm']} affirm verdicts are that class: in each, every v2 affirm match on the scorer's own input "
      f"(after `strip_conditionals`) lies inside the quoted carrier, an embedded complement in a reasoning trace about the "
      f"experiment, with no detection assertion anywhere in the text on Code's read. The script asserts the mechanical part: "
      f"every affirm match lies inside a carrier, and with the carriers blanked the scorer's own rule returns None for "
      f"every one of them. Those four sub-classes, on their face, cover the {len(sp_modal)} carriers with an ability modal "
      f"(trials {', '.join(map(str, sp_modal))}: the marker 'can' or 'able to'), not trials {sp_nomark[0]} and "
      f"{sp_nomark[1]}. The record's committed definition of the class, {spec_cls_loc}, covers those two as well: its "
      f"quoted_or_metalinguistic class has the example '{sp_quoted_ex}', and trial {sp_nomark[0]}'s carrier sentence "
      f"('{sp_sent[8]}') is close to verbatim; trial {sp_nomark[1]}'s ('{sp_sent[35]}') is the same construction, a "
      f"report of what the user is testing, on Code's read (it carries no marker of any of the spec's six classes, "
      f"checked word-bounded). Counts by reading:")
    w("")
    w("| stage | affirm-scored | assertion | non-asserting (FLAG-3's class) | ambiguous | FLAG-3 (record) |")
    w("|---|---|---|---|---|---|")
    for s in ("base", "sft"):
        rc_ = read_cnt[s]
        w(f"| {s} | {ctl[s]['affirm']} | {rc_['assertion']} | {rc_['non-asserting']} | {rc_['ambiguous']} | {rc_['FLAG-3']} |")
    w("")
    w("The non-assertion trials, with the carrier(s) as the scorer saw them (lowercased) and the opening sentence:")
    w("")
    for r_ in read42:
        if r_["read"] == "assertion":
            continue
        w(f"- {r_['stage']} trial {r_['trial']} -- **{r_['read']}**: carrier(s) " +
          "; ".join(f"\"{q_}\"" for q_ in r_["carrier_quotes"]) +
          f"; opens \"{r_['opening']}\"; blanked, the scorer's rule gives {r_['masked_verdict']}.")
    w("")
    asr_ = {s: [r_["trial"] for r_ in read42 if r_["stage"] == s and r_["read"] == "assertion"] for s in ("base", "sft")}
    w(f"Read as assertions (a 'Yes' / 'I detect' answer about this trial, most naming a word): base {asr_['base']}; "
      f"sft {asr_['sft']}. Ambiguous: base 94 opens 'Yes, I can try various prompts to figure this out' and its second "
      f"'yes' is inside a generated Q/A about a word's definition; SFT 5 opens 'Yes, as an AI, I process and detect "
      f"thoughts or requests based on the prompts provided to me' and then disclaims ('as I do not actually have a "
      f"consciousness or a brain, I do not truly understand thoughts') -- a capability statement, not a claim about this "
      f"trial, on one reading; {sft5_generic}. The record's count omits base, where the class is most frequent.")
    w("")
    w("Post-hoc relabels (descriptive; Code's reading; nothing of record is relabelled). Two conventions: FLAG-3's keeps a "
      "relabelled trial decidable as a non-claim (the spec's ground truth False for its two cases); the scorer's own "
      "three-way rule, with the carriers blanked, returns None (neither polarity) for every relabelled trial, i.e. "
      "undecidable. DPO and instruct are 0/91 in every row. Each row is run through the record's own `g3a` "
      f"({BRA}@{P}:{L['bra_g3a']}):")
    w("")
    w("| variant | base k/n = FPR [CP 95%] | sft k/n = FPR [CP 95%] | [g3-A] reading (record's g3a) | all four separations |")
    w("|---|---|---|---|---|")
    for r_ in relabel_rows:
        cb_, cs_ = r_["counts"]["base"], r_["counts"]["sft"]
        w(f"| {r_['variant']} | {cb_['affirm']}/{cb_['decidable']} = {cb_['affirm'] / cb_['decidable']:.4f} "
          f"[{r_['cp95']['base'][0]:.4f}, {r_['cp95']['base'][1]:.4f}] | {cs_['affirm']}/{cs_['decidable']} = "
          f"{cs_['affirm'] / cs_['decidable']:.4f} [{r_['cp95']['sft'][0]:.4f}, {r_['cp95']['sft'][1]:.4f}] | "
          f"{r_['g3a_reading']} | {'yes' if r_['all_four_separate'] else 'NO'} |")
    w("")
    w(f"Reading. Base 0.431 is the instrument's value and reproduces; on Code's read, {read_cnt['base']['non-asserting']} "
      f"of its {ctl['base']['affirm']} affirm verdicts are the scorer defect the record named at SFT, and the descriptive "
      f"base FPR is {base_lo_hi[0]:.3f}-{base_lo_hi[1]:.3f} depending on the convention and on the ambiguous trial. Every "
      f"variant keeps all four [g3-A] separations and the record's reading: {'YES' if relabel_all_sep else 'NO'}. This is "
      f"a scorer-of-record question for (iv), not a relabel: the note's base figure and F2's base criterion marker are "
      f"scorer v2's and carry this disclosure (section 9, item 7). No analyzer change is needed to reproduce 25/58, so it "
      f"is not a STOP.")
    w("")
    fig("scorer of record (all B2-r figures)", "detection_v2 claims_detection_v2", "data/olmo/b2r_*.json:scorer",
        "reproduced", "", named="block :33")
    fig("scorer of record (greedy row)", f"detection.py claims_detection (v1): the v1 pipeline re-derives the stored "
        f"claimed_detection on {b2_cd_n - b2_cd_v1}/{b2_cd_n} B2 trials, the v2 pipeline on {b2_cd_n - b2_cd_v2}/{b2_cd_n}",
        f"data/olmo/b2_{{fidelity,register}}_*.json:trials[].response_raw,claimed_detection (replay, section 2(a)); "
        f"code {R2}@{P}:{L['b2_claim']}; log {loc(RS, A['r_v1affirm'], A['r_v1affirm_b'])}",
        "reproduced", "no scorer field in the B2 artifacts; established by the replay", named="block :33")
    fig("single scorer across the N2 figure set", "no: v2 (B2-r) and v1 (greedy row)", "sections 2, 4", "discrepant",
        "(iv)'s pass condition is not met for the block's figure set; it holds for the B2-r figures alone; the block "
        "names no fail consequence for (iv) (section 10); a pass-condition outcome, not a note figure: N1's discrepant "
        "clause (block :23) does not attach -- no fail consequence (block :36)", named="block :33")
    fig("v1 pipeline on B2-r controls (same trials)", ", ".join(
        f"{s} {cross[s]['b2r_v1'][0]}/{cross[s]['b2r_v1'][1]}" for s in STAGES),
        "data/olmo/b2r_control_*.json:trials[].response_raw", "computed-new", "",
        named="computed-new (block :33 asks for both versions)")
    fig("FLAG-3 corrected SFT FPR 0.176", f"{k_c}/{ctl['sft']['decidable']} = {k_c / ctl['sft']['decidable']:.4f}; "
        f"CP lower {lo_c:.4f} > {hi_d:.4f}", "data/olmo/b2r_control_sft.json + data/configs/scorer_v3_spec.json:regression_cases",
        "reproduced", "two-trial hand relabel (SFT); it does not cover base (next two rows)", named=loc(RS, A['r_0176']))
    fig("2 of 42 affirm-scored control trials, both at SFT (FLAG-3's defect count)",
        f"42 = {' + '.join(str(ctl[s]['affirm']) for s in STAGES)} reproduces (artifact `affirm`); the 2 = the spec's two "
        f"regression cases (sft-16, sft-76)",
        f"{loc(RS, A['r_2of42'], A['r_2of42_b'])}; data/olmo/b2r_control_*.json:affirm; "
        f"data/configs/scorer_v3_spec.json:regression_cases",
        "log-only",
        f"the 2 is the record's hand count, which no script can recompute, so log-only rather than 'discrepant'; it does "
        f"NOT hold on Code's read of all 42: + {read_cnt['base']['non-asserting']} base affirm verdicts carried only by "
        f"non-asserting embedded complements (trials "
        f"{', '.join(str(k[1]) for k in READ_NON_ASSERTING)}) and {read_cnt['base']['ambiguous'] + read_cnt['sft']['ambiguous']} "
        f"ambiguous (base 94, sft 5); next row; a scorer-of-record question for (iv) (section 4; PI item 7)",
        named=loc(RS, A['r_2of42'], A['r_2of42_b']))
    fig("Code's read of the 42 affirm-scored controls; base relabelled (post-hoc)",
        f"base: {read_cnt['base']['assertion']} assertions, {read_cnt['base']['non-asserting']} non-asserting, "
        f"{read_cnt['base']['ambiguous']} ambiguous; sft: {read_cnt['sft']['assertion']} assertions, "
        f"{read_cnt['sft']['FLAG-3']} FLAG-3, {read_cnt['sft']['ambiguous']} ambiguous. Base FPR, FLAG-3's convention "
        + ", ".join(f"{r_['counts']['base']['affirm']}/{r_['counts']['base']['decidable']} = "
                    f"{r_['counts']['base']['affirm'] / r_['counts']['base']['decidable']:.3f} "
                    f"[{r_['cp95']['base'][0]:.3f}, {r_['cp95']['base'][1]:.3f}]" for r_ in relabel_rows[2:4])
        + "; the scorer's rule, carriers blanked, "
        + ", ".join(f"{r_['counts']['base']['affirm']}/{r_['counts']['base']['decidable']} = "
                    f"{r_['counts']['base']['affirm'] / r_['counts']['base']['decidable']:.3f} "
                    f"[{r_['cp95']['base'][0]:.3f}, {r_['cp95']['base'][1]:.3f}]" for r_ in relabel_rows[4:6])
        + f" (each pair: without / with the ambiguous); [g3-A] all four separations under every variant: "
        f"{'yes' if relabel_all_sep else 'NO'}",
        "data/olmo/b2r_control_{base,sft}.json:trials[].response (read in full); record g3a re-run on each variant",
        "computed-new", "post-hoc, descriptive; a reading, not an instrument; the values of record stay 25/58 and 17/85 "
                        "(and FLAG-3's 15/85)", named="computed-new")

    # =================================================== section 5 (v)
    w("## 5. N2(v): F2 data -- per-stage (FPR, TPR), corrected d', criterion c, Fisher")
    w("")
    w("For every point: H' = (H + 1/2)/(N_s + 1), F' = (FA + 1/2)/(N_n + 1); d' = z(H') - z(F'); c = -(z(H') + z(F'))/2 "
      "(z = inverse standard normal, statistics.NormalDist); one-sided Fisher exact on [[H, N_s - H], [FA, N_n - FA]] "
      "with H1: hit rate > FA rate, p = P(X >= H) under the hypergeometric with both margins fixed, exact integer "
      "arithmetic, asserted equal to the record's `valence_core.stats.fisher_one_sided` on every row. Unit: trial. "
      "Ours: decidable trials. Theirs: trials under the stated ASSUMPTION.")
    w("")
    points = []

    def add_point(dataset, arm, stage, h, ns, fa, nn, n_assumed, source, note="", extra=None):
        if ns and nn:
            d_, c_ = dprime_ll(h, ns, fa, nn)
            p_ = fisher_hits_gt_fa(h, ns, fa, nn)
            pr = stats.fisher_one_sided(h, ns - h, fa, nn - fa)
            assert abs(p_ - pr) < 1e-12, (dataset, arm, stage, p_, pr)
            tpr = h / ns
        else:
            d_ = c_ = p_ = None
            tpr = (h / ns) if (ns and h is not None) else None
        pt = {"dataset": dataset, "arm": arm, "stage": stage, "hits": h, "n_signal": ns,
              "fa": fa, "n_noise": nn, "tpr": tpr, "fpr": fa / nn if nn else None,
              "dprime_loglinear": d_, "c_loglinear": c_, "fisher_p_one_sided": p_,
              "n_assumed": n_assumed, "source": source, "note": note}
        if extra:
            pt.update(extra)
        return pt

    # ours criterion arm (g3a)
    for s in STAGES:
        k, n = ctl[s]["affirm"], ctl[s]["decidable"]
        points.append(add_point("ours", "criterion ([g3-A], B2-r section 1 control)", s, None, 0, k, n, False,
                                f"data/olmo/b2r_analysis.json:g3a.rates.{s}.k,n (= b2r_control_{s}.json:affirm,decidable)",
                                "control trials only: no injected trials exist in this arm, so there is no TPR, d', c or "
                                "Fisher; plot as an FPR-only marker" + ("; below the 64/96 floor" if n < 64 else ""),
                                ({"disclosure_post_hoc": {
                                    "summary": f"instrument-of-record value (scorer v2); on Code's read {read_cnt['base']['non-asserting']} "
                                               f"of the {k} affirm verdicts are carried only by non-asserting embedded complements "
                                               f"(FLAG-3's class) and {read_cnt['base']['ambiguous']} is ambiguous; descriptive "
                                               f"relabels {base_lo_hi[0]:.4f}-{base_lo_hi[1]:.4f}; [g3-A] unchanged; raw section 4",
                                    "non_asserting_trials": [k_[1] for k_ in READ_NON_ASSERTING],
                                    "ambiguous_trials": [k_[1] for k_ in READ_AMBIGUOUS if k_[0] == "base"],
                                    "relabel_variants": [{"variant": r_["variant"], "k": r_["counts"]["base"]["affirm"],
                                                          "n": r_["counts"]["base"]["decidable"], "cp95": r_["cp95"]["base"]}
                                                         for r_ in relabel_rows]}} if s == "base" else
                                 {"disclosure_post_hoc": {
                                     "summary": f"instrument-of-record value (scorer v2); the record's FLAG-3 hand correction "
                                                f"is {k - 2}/{n} = {(k - 2) / n:.4f} ({loc(RS, A['r_0176'])}); on Code's read "
                                                f"{read_cnt['sft']['ambiguous']} further affirm verdict is ambiguous (trial 5); "
                                                f"raw section 4",
                                     "flag3_trials": [16, 76], "ambiguous_trials": [5]}} if s == "sft" else None)))
    # ours exploration arm
    for s in EXP_STAGES:
        e = exp[s]
        points.append(add_point("ours", "exploration (B2-r section 3)", s, e["hit"], e["inj_decidable"], e["fa"],
                                e["ctl_decidable"], False,
                                f"data/olmo/b2r_explore_{s}.json:hit,inj_decidable,fa,ctl_decidable",
                                "control trials replay section 1 trials with the same number and seed (section 5(e)); "
                                "MED_c 1.0"))
    # theirs at 800/80
    ni, nc = ASSUMED_N
    pi_, pc_ = POOLED_N
    nvrows = {r["point"]: r for r in n2vi["source_points_dprime_computed_new"]["rows"]
              if r["n_injected"] == ni and r["n_control"] == nc}
    # every theirs rate is pooled over the 20 configurations (N2vi stages.*.config;
    # ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:38-39), while 800/80 is the record's
    # per-configuration cell size (ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:32)
    assert all(n2vi["stages"][s]["config"].startswith("aggregate over L in [25, 32, 38, 45, 51] x alpha in [1, 2, 4, 8] (20 configs)")
               for s in STAGES) and n2vi["grid"]["n_configs"] == N_CONFIGS
    sc8 = next(x for x in n2vi["grid"]["n_scenarios_computed_new"] if x["n_concepts"] == 8)
    assert (sc8["per_cell_injected"], sc8["per_cell_control"]) == ASSUMED_N
    assert (sc8["per_stage_pooled_injected"], sc8["per_stage_pooled_control"]) == POOLED_N
    pooled = {}
    for s in STAGES:
        st = n2vi["stages"][s]
        hP = half_up(Fraction(str(st["tpr"])) * pi_)
        faP = half_up(Fraction(str(st["fpr"])) * pc_)
        dP, cP = dprime_ll(hP, pi_, faP, pc_)
        pooled[s] = {"hits": hP, "fa": faP, "dprime_loglinear": dP, "c_loglinear": cP,
                     "fisher_p_one_sided": fisher_hits_gt_fa(hP, pi_, faP, pc_)}
    n_caveat = (f"{ni}/{nc} is the record's per-configuration cell size ({loc(AG, A['a_percfg'])}) applied to a rate "
                f"pooled over {N_CONFIGS} configurations ({loc(AG, A['a_pooled_a'], A['a_pooled_b'])}); under the same "
                f"premise the pooled n is {pi_}/{pc_} (8 concepts)")
    for s in STAGES:
        st = n2vi["stages"][s]
        assert st["n_injected"] is None and st["n_control"] is None
        h = half_up(Fraction(str(st["tpr"])) * ni)
        fa = half_up(Fraction(str(st["fpr"])) * nc)
        pP = pooled[s]
        pt = add_point("theirs", "source aggregate (20 configurations pooled)", s, h, ni, fa, nc, True,
                       f"{N2VI_JSON}:stages.{s}.tpr,fpr (arXiv:2603.21396v1 App. C text, read by N2vi); n = ASSUMPTION",
                       f"ASSUMPTION: n = {ni} injected / {nc} control per (layer, alpha) configuration (design seat, block :34); "
                       f"the source states no n; counts = rate x n rounded half-up (expected {float(Fraction(str(st['tpr'])) * ni):.2f} / "
                       f"{float(Fraction(str(st['fpr'])) * nc):.2f}). CAVEAT: {n_caveat}, at which this point is "
                       f"{pP['hits']}/{pi_}, {pP['fa']}/{pc_}: d' {pP['dprime_loglinear']:+.3f}, c {pP['c_loglinear']:+.3f}, "
                       f"one-sided Fisher p {pfmt(pP['fisher_p_one_sided'])}. Neither n gives an exact test of the pooled "
                       f"rate (the pooled trials are clustered by configuration and concept); do not annotate this point's "
                       f"d' or p on F2 without the n caveat",
                       {"rate_tpr_source": st["tpr"], "rate_fpr_source": st["fpr"],
                        "pooled_same_premise": {"n_signal": pi_, "n_noise": pc_, **pP}})
        nr = nvrows[s]
        assert nr["hits"] == h and nr["false_alarms"] == fa and abs(nr["dprime_loglinear"] - pt["dprime_loglinear"]) < 1e-12
        points.append(pt)
    # theirs instruct variant with the record's FPR 0.003
    st = n2vi["stages"]["instruct"]
    h = half_up(Fraction(str(st["tpr"])) * ni)
    fa = half_up(Fraction(str(st["record_addendum_fpr"])) * nc)
    hP = half_up(Fraction(str(st["tpr"])) * pi_)
    faP = half_up(Fraction(str(st["record_addendum_fpr"])) * pc_)
    dP, cP = dprime_ll(hP, pi_, faP, pc_)
    pP3 = {"hits": hP, "fa": faP, "dprime_loglinear": dP, "c_loglinear": cP,
           "fisher_p_one_sided": fisher_hits_gt_fa(hP, pi_, faP, pc_)}
    points.append(add_point("theirs", "source aggregate, instruct FPR as the record transcribes it (0.003)", "instruct",
                            h, ni, fa, nc, True,
                            f"{N2VI_JSON}:stages.instruct.tpr,record_addendum_fpr; {loc(AG, 46)}",
                            f"ASSUMPTION: n = {ni}/{nc}; the record's 0.003 is the source's instruct introspection rate "
                            f"(N2vi section 4); 0.003 x {nc} = 0.24 rounds to 0, so at this n the row equals the "
                            f"source-text row. CAVEAT: {n_caveat}, at which 0.003 x {pc_} = {float(Fraction('0.003') * pc_):.1f} "
                            f"rounds to {faP} false alarms and the row is {hP}/{pi_}, {faP}/{pc_}: d' "
                            f"{dP:+.3f}, c {cP:+.3f}, one-sided Fisher p {pfmt(pP3['fisher_p_one_sided'])}",
                            {"pooled_same_premise": {"n_signal": pi_, "n_noise": pc_, **pP3}}))
    # greedy rows
    greedy = []
    for r in greedy_rows:
        g = add_point("ours", f"greedy (B2 {r['arm']}, temperature 0.0, scorer v1)", r["stage"], r["h8"], r["di8"],
                      r["fa"], r["dc"], False,
                      f"data/olmo/b2_analysis.json:{r['arm']}.{r['stage']} (eight Macar concepts; = b2_{r['arm']}_{r['stage']}.json trials)",
                      ("not the B2-r protocol (section 2(c)); " if r["arm"] == "fidelity" else
                       "register arm: a different question and framing, a defective scorer for it, not a detection point; ") +
                      f"L{r['layer']} frac {r['frac']}; all nine concepts: hits {r['h9']}/{r['di9']}" +
                      ("" if r["evaluable"] else "; below the 16-of-24 floor"))
        greedy.append(g)
    w("| dataset | arm | stage | H / N_s | FA / N_n | TPR | FPR | d' | c | Fisher p (one-sided) | n assumed |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for pt in points + greedy:
        hs = f"{pt['hits']}/{pt['n_signal']}" if pt["n_signal"] else "-- (no injected trials)"
        w(f"| {pt['dataset']} | {pt['arm']} | {pt['stage']} | {hs} | {pt['fa']}/{pt['n_noise']} | "
          f"{fmt(pt['tpr'])} | {fmt(pt['fpr'])} | {fmt(pt['dprime_loglinear'], 3, True)} | "
          f"{fmt(pt['c_loglinear'], 3, True)} | {pfmt(pt['fisher_p_one_sided'])} | "
          f"{'ASSUMPTION ' + str(ni) + '/' + str(nc) + ' (a per-configuration n on a rate pooled over 20 configurations; see 5(b))' if pt['n_assumed'] else 'no'} |")
    w("")
    w(f"Caveat on every 'theirs' row: {n_caveat}. At that n the DPO point is {pooled['dpo']['hits']}/{pi_}, "
      f"{pooled['dpo']['fa']}/{pc_} (d' {pooled['dpo']['dprime_loglinear']:+.3f}, one-sided Fisher p "
      f"{pfmt(pooled['dpo']['fisher_p_one_sided'])}) and the instruct point {pooled['instruct']['hits']}/{pi_}, "
      f"{pooled['instruct']['fa']}/{pc_} (d' {pooled['instruct']['dprime_loglinear']:+.3f}, p "
      f"{pfmt(pooled['instruct']['fisher_p_one_sided'])}). With FA = 0 the log-linear d' is driven by the assumed N_n. "
      f"The source states no n (N2vi), and neither n is exact for a pooled rate (its trials are clustered by "
      f"configuration and concept), so 'theirs' d' and p are n-conditional throughout (5(b), 5(d)).")
    w("")
    w(f"Criterion-arm markers: base 0.431 is scorer v2's value; on Code's read {read_cnt['base']['non-asserting']} of its "
      f"{ctl['base']['affirm']} false alarms are FLAG-3's class (post-hoc {base_lo_hi[0]:.3f}-{base_lo_hi[1]:.3f}; section 4; "
      f"ROC JSON `disclosure_post_hoc`). SFT 0.200 has the record's FLAG-3 correction, 0.176, beside it. The exploration "
      f"SFT point with FLAG-3 carried to its replayed controls is in 5(e).")
    w("")
    w("### 5(a) What the block's arm labels are")
    w("")
    w("- **Criterion arm ([g3-A]) -- 25/58, 17/85, 0/91, 0/91 are all false alarms**, at base, SFT, DPO, instruct, each over "
      "decidable control trials. Section 1 ran no injected trial, so the arm has no hit rate and no ROC point; on F2 it "
      "can only be an FPR marker. [g3-A] reads the four FPRs by exact CP interval separation (b2r_analyze.py "
      f"`g3a`, :{L['bra_g3a']}): all four separations hold, reading '{an_r['g3a']['reading'].split(' — ')[0]}'.")
    w(f"- Code's clarification (the block names g3a only, {loc(BLOCK, 34)}): b2r_analysis.json also holds `g3b`, the "
      f"[g3-B] dose-qualification ladder (b2r_analyze.py `g3b`, :{L['bra_g3b']}). It is not a detection quantity: per "
      "stage and strength, the share of generations to two neutral prompts (no detection question) that contain the "
      "injected concept word (`about_ness`), against an uninjected control, with a coherence gate. It selects MED_c and "
      "puts no point on F2. Values (about / n, degenerate fraction; control about 0/24 at every stage):")
    w("")
    w("| stage | s=1.0 | s=2.0 | s=4.0 | s=8.0 | control | MED_c |")
    w("|---|---|---|---|---|---|---|")
    for s in STAGES:
        q = qual[s]
        cellz = []
        for k_ in ("1.0", "2.0", "4.0", "8.0"):
            v = q["injected"][k_]
            lad = an_r["g3b"][s]["ladder"][k_]
            cellz.append(f"{v['about']}/{v['n']} d{v['degenerate_frac']:.2f}{' pass' if lad['passes'] else ''}")
        w(f"| {s} | " + " | ".join(cellz) + f" | {q['control']['about']}/{q['control']['n']} | {an_r['g3b'][s]['MED_c']} |")
    w("")
    block_exp = {"sft": (12, 40, 9, 44), "dpo": (0, 43, 0, 45), "instruct": (0, 44, 0, 46)}   # block :34, as written
    assert "12/40 hits / 9/44 FA at SFT, 0/43 / 0/45 at DPO, 0/44 / 0/46 at instruct" in block_lines[33]
    exp_ok = {s: (exp[s]["hit"], exp[s]["inj_decidable"], exp[s]["fa"], exp[s]["ctl_decidable"]) == block_exp[s]
              for s in EXP_STAGES}
    w(f"- **Exploration arm** -- the block's (and F2's, per the block) 12/40 hits / 9/44 FA at SFT, 0/43 / 0/45 at DPO, "
      f"0/44 / 0/46 at instruct: " +
      "; ".join(f"{s} {exp[s]['hit']}/{exp[s]['inj_decidable']} hits, {exp[s]['fa']}/{exp[s]['ctl_decidable']} FA "
                f"({'equal' if exp_ok[s] else 'DIFFERENT'})" for s in EXP_STAGES) +
      " (b2r_explore_<stage>.json `hit`/`inj_decidable`, `fa`/`ctl_decidable`). Base has no exploration cell ([g3-B] hard stop).")
    for s in EXP_STAGES:
        bh, bn, bf, bc = block_exp[s]
        fig(f"exploration {s}: hits {bh}/{bn}", f"{exp[s]['hit']}/{exp[s]['inj_decidable']}",
            f"data/olmo/b2r_explore_{s}.json:hit,inj_decidable", "reproduced" if exp_ok[s] else "discrepant",
            "hits over injected decidable trials, scorer v2", named="block :34")
        fig(f"exploration {s}: FA {bf}/{bc}", f"{exp[s]['fa']}/{exp[s]['ctl_decidable']}",
            f"data/olmo/b2r_explore_{s}.json:fa,ctl_decidable", "reproduced" if exp_ok[s] else "discrepant",
            "false alarms over control decidable trials, scorer v2; these controls replay section 1 trials (5(e))"
            + ("; FLAG-3's two relabelled SFT controls are among them (5(e))" if s == "sft" else ""), named="block :34")
    w(f"- **Theirs**: four points from the source's pooled rates, n = ASSUMPTION {ni}/{nc} in every row. {n_caveat[0].upper() + n_caveat[1:]}; "
      f"5(b) gives the points at that n. The instruct row is the same under the source's 0% and the record's 0.3% FPR "
      f"at {ni}/{nc}, and not at {pi_}/{pc_}.")
    w("- **Greedy**: B2, one row per stage and arm, zero claims in every fidelity row; d' there is the log-linear "
      "correction's artefact of unequal N_s and N_n, not a measurement.")
    w("")

    # theirs n sensitivity
    w("### 5(b) The source's points under other n (computed-new; the n is an assumption in every row)")
    w("")
    w("| assumption | stage | H / N_s | FA / N_n | d' | c | Fisher p |")
    w("|---|---|---|---|---|---|---|")
    sens_rows = []
    th_p = {p_["stage"]: p_["fisher_p_one_sided"] for p_ in points
            if p_["dataset"] == "theirs" and p_["arm"].startswith("source aggregate (20")}
    sc50 = next(x for x in n2vi["grid"]["n_scenarios_computed_new"] if x["n_concepts"] == 50)
    assert (sc50["per_cell_injected"], sc50["per_cell_control"]) == (5000, 500)
    assert (sc50["per_stage_pooled_injected"], sc50["per_stage_pooled_control"]) == (100000, 10000)
    for label, (a_i, a_c) in (("5000/500: 50 concepts (code default), one configuration's n applied to the pooled rate", (5000, 500)),
                              (f"{pi_}/{pc_}: 8 concepts, the seat's per-configuration premise pooled over 20 configurations", POOLED_N),
                              ("100000/10000: 50 concepts, pooled over 20 configurations", (100000, 10000))):
        for s in STAGES:
            st = n2vi["stages"][s]
            h = half_up(Fraction(str(st["tpr"])) * a_i)
            fa = half_up(Fraction(str(st["fpr"])) * a_c)
            pt = add_point("theirs", f"source aggregate, n sensitivity: {label}", s, h, a_i, fa, a_c, True,
                           f"{N2VI_JSON}:stages.{s}.tpr,fpr; n = ASSUMPTION", f"ASSUMPTION: {label}")
            sens_rows.append(pt)
            w(f"| {label} | {s} | {h}/{a_i} | {fa}/{a_c} | {pt['dprime_loglinear']:+.3f} | {pt['c_loglinear']:+.3f} | "
              f"{pfmt(pt['fisher_p_one_sided'])} |")
    w("")
    for r_ in sens_rows:
        if r_["n_signal"] == pi_ and r_["n_noise"] == pc_:
            assert r_["hits"] == pooled[r_["stage"]]["hits"] and r_["fa"] == pooled[r_["stage"]]["fa"]
            assert r_["fisher_p_one_sided"] == pooled[r_["stage"]]["fisher_p_one_sided"]
    big_sig = all(r_["fisher_p_one_sided"] < 0.05 for r_ in sens_rows if r_["stage"] in ("dpo", "instruct"))
    w(f"At the design seat's {ni}/{nc} the source's DPO and instruct points are not significant by this test (p = "
      f"{th_p['dpo']:.4f}, {th_p['instruct']:.4f}); at every larger n in this table every DPO and instruct p is below "
      f".05: {'YES' if big_sig else 'NO'}. The rates are pooled over {N_CONFIGS} configurations "
      f"({loc(AG, A['a_pooled_a'], A['a_pooled_b'])}), so a per-configuration n ({ni}/{nc}, {loc(AG, A['a_percfg'])}; or "
      f"5000/500) applied to them understates the pooled n {N_CONFIGS}-fold under its own premise; the pooled rows are that "
      f"premise carried through. Pooled counts in turn treat trials clustered by configuration and concept as independent, "
      f"so no row here is an exact test of the source's aggregate. Any F2 annotation of the source's points carries the "
      f"n assumption, because the source states none (N2vi section 5).")
    w("")

    # round 4: every theirs row against the N2vi item (its JSON rows and its raw's tables), read-only
    def md_table(lines_: list, head: str, upto: str) -> list:
        a_ = next(i for i, l_ in enumerate(lines_) if l_.startswith(head))
        b_ = next(i for i, l_ in enumerate(lines_) if i > a_ and l_.startswith(upto))
        rows_ = [l_ for l_ in lines_[a_:b_] if l_.startswith("| ") and not l_.startswith("|---")]
        return [[c_.strip() for c_ in r_.strip().strip("|").split(" | ")] for r_ in rows_[1:]]   # drop the header row
    nvj = {(r["n_injected"], r["n_control"], r["point"]): r for r in n2vi["source_points_dprime_computed_new"]["rows"]}
    nvm = {}
    for c_ in md_table(n2vi_md_lines, "## 7.", "**The seat's arithmetic"):
        ni_, nc_ = (int(x) for x in c_[0].split(" / "))
        nvm[(ni_, nc_, c_[2])] = c_
    assert set(nvm) == set(nvj) and len(nvj) == 20
    mine_th = []
    for p_ in points:
        if p_["dataset"] != "theirs":
            continue
        lab_ = "instruct, record FPR .003" if p_["arm"].endswith("(0.003)") else p_["stage"]
        mine_th.append(("point", p_["n_signal"], p_["n_noise"], lab_, p_["hits"], p_["fa"], p_["dprime_loglinear"],
                        p_["c_loglinear"], p_["fisher_p_one_sided"]))
        ps_ = p_.get("pooled_same_premise")
        if ps_:
            mine_th.append(("pooled_same_premise", ps_["n_signal"], ps_["n_noise"], lab_, ps_["hits"], ps_["fa"],
                            ps_["dprime_loglinear"], ps_["c_loglinear"], ps_["fisher_p_one_sided"]))
    for r_ in sens_rows:
        mine_th.append(("n_sensitivity", r_["n_signal"], r_["n_noise"], r_["stage"], r_["hits"], r_["fa"],
                        r_["dprime_loglinear"], r_["c_loglinear"], r_["fisher_p_one_sided"]))
    th_json_ok = th_md_ok = 0
    th_bad = []
    for kind_, a_i, a_c, lab_, h_, fa_, d_, c_, pv_ in mine_th:
        rj_, rm_ = nvj[(a_i, a_c, lab_)], nvm[(a_i, a_c, lab_)]
        okj_ = (rj_["hits"] == h_ and rj_["false_alarms"] == fa_ and abs(rj_["dprime_loglinear"] - d_) <= 1e-12 and
                abs(rj_["criterion_c"] - c_) <= 1e-12 and abs(rj_["fisher_one_sided_p"] - pv_) <= 1e-9 * max(abs(pv_), 1e-300))
        okm_ = (rm_[5] == f"{h_} / {fa_}" and rm_[6] == f"{d_:+.3f}" and rm_[7] == f"{c_:+.3f}" and rm_[8] == pfmt(pv_))
        th_json_ok += okj_
        th_md_ok += okm_
        if not (okj_ and okm_):
            th_bad.append((kind_, a_i, a_c, lab_))
    th_pairs = sorted({(a_i, a_c, lab_) for _, a_i, a_c, lab_, *_r in mine_th})
    th_not_here = sorted(set(nvj) - set(th_pairs))
    # the per-stage rates (1(b), section 5) against the N2vi raw's section 4 table; the source decoding (1(c)) against its section 9 table
    st_md = {c_[0]: c_ for c_ in md_table(n2vi_md_lines, "## 4.", "TPR: ")}
    st_cmp = []
    for s in STAGES:
        st = n2vi["stages"][s]
        st_cmp += [f"{st['tpr']:.3f}" == st_md[s][2], f"{st['fpr']:.3f}" == st_md[s][6],
                   f"{st['record_results_their_fpr']:.3f}" == st_md[s][5], f"{st['record_addendum_fpr']:.3f}" == st_md[s][4]]
    dec_md = {c_[0]: c_ for c_ in md_table(n2vi_md_lines, "## 9.", "Paper v1 on decoding")}
    dec_keys = ("temperature", "top_p", "top_k", "max_new_tokens", "seed_policy", "prompt_format",
                "trials_per_concept_per_cell_injected", "trials_per_concept_per_cell_control")
    def _nvs(v_) -> str:                     # the N2vi raw renders a null as 'not stated'
        return "not stated" if v_ is None else str(v_)
    dec_cmp = [_nvs(nv[k]["paper_v1"]) == dec_md[k][1] and _nvs(nv[k]["code_5d5d9b4"]) == dec_md[k][2] for k in dec_keys]
    th_check = {"n2vi_json_sha256": sha256_bytes(n2vi_bytes), "n2vi_md_sha256": sha256_bytes(n2vi_md_bytes),
                "theirs_rows_compared": len(mine_th), "distinct_n_point_pairs": len(th_pairs),
                "agree_with_n2vi_json_rows": th_json_ok, "agree_with_n2vi_raw_section7": th_md_ok, "disagreeing": th_bad,
                "n2vi_rows_not_computed_here": [list(x) for x in th_not_here],
                "stage_rate_cells_agree_with_n2vi_raw_section4": [sum(st_cmp), len(st_cmp)],
                "decoding_rows_agree_with_n2vi_raw_section9": [sum(dec_cmp), len(dec_cmp)]}
    w(f"**Theirs rows against the N2vi item (round 4; a read-only check of that item's working-tree outputs).** N2vi "
      f"JSON sha256 `{th_check['n2vi_json_sha256']}`, raw sha256 `{th_check['n2vi_md_sha256']}`. Every theirs row this "
      f"item computes ({len(mine_th)} rows: the {sum(1 for x in mine_th if x[0] == 'point')} section 5 points, their "
      f"{sum(1 for x in mine_th if x[0] == 'pooled_same_premise')} pooled_same_premise objects and the "
      f"{sum(1 for x in mine_th if x[0] == 'n_sensitivity')} 5(b) rows; {len(th_pairs)} distinct (n, point) pairs) equals "
      f"the N2vi JSON's `source_points_dprime_computed_new.rows` (counts exact; d' and c within 1e-12; p within relative "
      f"1e-9): {th_json_ok} of {len(mine_th)}; and the N2vi raw's section 7 table at its printed precision (H / FA; d' "
      f"and c at 3 dp; p as printed): {th_md_ok} of {len(mine_th)}. N2vi rows this item does not compute: " +
      "; ".join(f"{a}/{b} {c}" for a, b, c in th_not_here) +
      f" (this item's 0.003 variant runs at {ni}/{nc} and {pi_}/{pc_} only). The per-stage rates this item reads (N2vi "
      f"`stages.*`: tpr, fpr, record_results_their_fpr, record_addendum_fpr; 1(b) and section 5) equal the N2vi raw's "
      f"section 4 table: {sum(st_cmp)} of {len(st_cmp)} cells; the source decoding values (1(c)) equal its section 9 "
      f"table: {sum(dec_cmp)} of {len(dec_cmp)} rows.")
    w("")
    assert not th_bad and all(st_cmp) and all(dec_cmp)

    # bounds
    w("### 5(c) Bounds on a per-stage hit rate given zero hits")
    w("")
    bounds = {}
    w("| k/n | one-sided 95% upper = 1 - 0.05^(1/n) | two-sided 95% CP upper = one-sided 97.5% = 1 - 0.025^(1/n) | record's clopper_pearson(0, n) upper | for completeness: 97.5% two-sided CP upper = one-sided 98.75% = 1 - 0.0125^(1/n) | P(X = 0 \\| n, 0.029) |")
    w("|---|---|---|---|---|---|")
    for n in (43, 44, 45, 46, 91):
        u95 = 1 - 0.05 ** (1 / n)
        u975 = 1 - 0.025 ** (1 / n)
        u9875 = 1 - 0.0125 ** (1 / n)
        rec = b2a.clopper_pearson(0, n)[1]
        assert abs(rec - u975) < 1e-12
        p0 = float(binom_pmf_exact(0, n, Fraction("0.029")))
        bounds[f"0_of_{n}"] = {"one_sided_95_upper": u95,
                               "two_sided_95_cp_upper_equals_one_sided_97.5": u975,
                               "two_sided_97.5_cp_upper_equals_one_sided_98.75": u9875,
                               "record_clopper_pearson_two_sided_95_upper": rec,
                               "exact_binomial_P_X_eq_0_given_p_0.029": p0}
        w(f"| 0/{n} | {u95:.4f} | {u975:.4f} | {rec:.4f} | {u9875:.4f} | {p0:.4f} |")
    w("")
    w("Which is which: the design seat's '~.067' is the **one-sided 95%** upper bound for 0/43 (0.0673). The record's "
      f"intervals are two-sided 95% Clopper-Pearson, whose upper limit equals the one-sided 97.5% bound "
      f"({bounds['0_of_43']['two_sided_95_cp_upper_equals_one_sided_97.5']:.4f} for 0/43; "
      f"{bounds['0_of_91']['two_sided_95_cp_upper_equals_one_sided_97.5']:.4f} for 0/91, the [g3-A] DPO/instruct upper). "
      f"For completeness (no referent uses it), a 97.5% two-sided CP interval for 0/43 has upper limit "
      f"{bounds['0_of_43']['two_sided_97.5_cp_upper_equals_one_sided_98.75']:.4f}. The record's 'our 0/43 is "
      f"consistent with a true rate of 2.9% (p ~ 0.28)' ({loc(RS, A['r_p28_b'])}; also {loc(RS, A['r_p28_a'])}) "
      f"reproduces as the exact one-sided binomial P(X <= 0 | 43, 0.029) = {bounds['0_of_43']['exact_binomial_P_X_eq_0_given_p_0.029']:.4f}; "
      "its 2.9% is the source's prose rate (log-only operand).")
    w("")
    fig("our 0/43 consistent with a true rate of 2.9% (p ~ 0.28)",
        f"{bounds['0_of_43']['exact_binomial_P_X_eq_0_given_p_0.029']:.4f} = P(X <= 0 | 43, 0.029), exact one-sided binomial",
        f"{loc(RS, A['r_p28_b'])}; {loc(RS, A['r_p28_a'])}; n = data/olmo/b2r_explore_dpo.json:inj_decidable",
        "log-only", "the 2.9% operand is the source's prose rate (no committed artifact); n = 43 and the arithmetic reproduce",
        named=loc(RS, A['r_p28_b']))
    assert exp["dpo"]["inj_decidable"] == 43 and exp["dpo"]["hit"] == 0

    # design seat
    def pt_of(dataset, arm_prefix, stage):
        return next(p_ for p_ in points if p_["dataset"] == dataset and p_["arm"].startswith(arm_prefix) and p_["stage"] == stage)

    def agree(val, seat, nd):
        return round(val, nd) == round(seat, nd)

    th = {s: pt_of("theirs", "source aggregate (20", s) for s in STAGES}
    ex_ = {s: pt_of("ours", "exploration", s) for s in EXP_STAGES}
    seat = [
        ("theirs base d' ~ -1.9", th["base"]["dprime_loglinear"], -1.9, 1, pooled["base"]["dprime_loglinear"]),
        ("theirs SFT d' ~ -0.3", th["sft"]["dprime_loglinear"], -0.3, 1, pooled["sft"]["dprime_loglinear"]),
        ("theirs DPO d' ~ +0.6", th["dpo"]["dprime_loglinear"], 0.6, 1, pooled["dpo"]["dprime_loglinear"]),
        ("theirs DPO p ~ .11 (0 of ~80 controls)", th["dpo"]["fisher_p_one_sided"], 0.11, 2, pooled["dpo"]["fisher_p_one_sided"]),
        ("theirs instruct d' ~ +0.15", th["instruct"]["dprime_loglinear"], 0.15, 2, pooled["instruct"]["dprime_loglinear"]),
        ("theirs instruct p ~ .5", th["instruct"]["fisher_p_one_sided"], 0.5, 1, pooled["instruct"]["fisher_p_one_sided"]),
        ("ours SFT d' ~ +0.3", ex_["sft"]["dprime_loglinear"], 0.3, 1, None),
        ("ours SFT p ~ .22", ex_["sft"]["fisher_p_one_sided"], 0.22, 2, None),
        ("ours DPO d' ~ 0", ex_["dpo"]["dprime_loglinear"], 0.0, 1, None),
        ("ours instruct d' ~ 0", ex_["instruct"]["dprime_loglinear"], 0.0, 1, None),
        ("upper 95% bound, 0/43 ~ .067", bounds["0_of_43"]["one_sided_95_upper"], 0.067, 3, None),
    ]
    w("### 5(d) The design seat's arithmetic (block :34), replaced")
    w("")
    w(f"'Theirs' figures rest on an n the source does not state. The seat's {ni}/{nc} is a per-configuration cell size "
      f"applied to rates pooled over {N_CONFIGS} configurations; the pooled column carries the seat's own premise through "
      f"({pi_}/{pc_}). 'Ours' figures use observed decidable counts and assume no n.")
    w("")
    w(f"| seat's figure | computed at the seat's n | at the seat's precision | same premise, pooled {pi_}/{pc_} | at the seat's precision | disposition |")
    w("|---|---|---|---|---|---|")
    seat_out = []

    def vfmt(lab, v):
        return pfmt(v) if (" p " in lab) else (f"{v:.4f}" if "bound" in lab else f"{v:+.4f}")

    for lab, val, sv, nd, pv in seat:
        ok = agree(val, sv, nd)
        if pv is None:
            disp = ("confirmed (observed counts; no n assumption)" if ok else "REFUTED")
            pok = None
        else:
            pok = agree(pv, sv, nd)
            if not ok:
                disp = "REFUTED at the seat's own n"
            elif pok:
                disp = (f"arithmetic confirmed under the seat's assumption; the figure also holds at the pooled n "
                        f"(n-robust at the seat's precision)")
            else:
                disp = (f"arithmetic confirmed under the seat's assumption; the assumption understates the "
                        f"aggregate's n {N_CONFIGS}-fold, and at the pooled n the figure is {vfmt(lab, pv)}")
        seat_out.append({"figure": lab, "seat": sv, "computed_at_seat_n": val,
                         "arithmetic_confirmed_at_seat_n": ok,
                         "n_assumed": pv is not None,
                         "computed_at_pooled_n_same_premise": pv,
                         "agrees_at_pooled_n": pok, "disposition": disp})
        w(f"| {lab} | {vfmt(lab, val)} | {'agrees' if ok else 'REFUTED'} | "
          f"{'n/a (no n assumed)' if pv is None else vfmt(lab, pv)} | "
          f"{'n/a' if pok is None else ('agrees' if pok else 'does not agree')} | {disp} |")
        fig(lab, (f"{vfmt(lab, val)} (observed counts)" if pv is None else
                  f"{vfmt(lab, val)} at the seat's {ni}/{nc}; {vfmt(lab, pv)} at the pooled {pi_}/{pc_}"),
            "section 5 points (ROC JSON design_seat_check)", "computed-new", disp, named="block :34")
    w("")
    w(f"'DPO and instruct ~ 0 by construction': with H = FA = 0 the log-linear d' is z(0.5/(N_s+1)) - z(0.5/(N_n+1)), "
      f"which is zero only when N_s = N_n; here {ex_['dpo']['dprime_loglinear']:+.4f} (43 vs 45) and "
      f"{ex_['instruct']['dprime_loglinear']:+.4f} (44 vs 46), so 'approximately 0, by the correction' rather than "
      f"exactly 0. The criterion c there is large and positive (DPO {ex_['dpo']['c_loglinear']:+.3f}, instruct "
      f"{ex_['instruct']['c_loglinear']:+.3f}): the zero-claim stages sit at a conservative criterion with no "
      f"measurable sensitivity.")
    w("")

    # (e) replay finding
    rep_ident = {}
    for s in EXP_STAGES:
        cm = {t["trial"]: t for t in ctl[s]["trials"]}
        ec = [t for t in exp[s]["trials"] if not t["injected"]]
        same = sum(1 for t in ec if t["seed"] == cm[t["trial"]]["seed"] and
                   t["response_raw"] == cm[t["trial"]]["response_raw"])
        fa_sub = sum(1 for t in ec if t["claimed_detection"] is True and cm[t["trial"]]["claimed_detection"] is True)
        rep_ident[s] = (same, len(ec), fa_sub, exp[s]["fa"])
    w("### 5(e) The exploration arm's controls are replays of section 1 trials")
    w("")
    w(f"Both B2-r parts use `--seed` default 20260824 ({RR}@{P}:{L['rr_seed']}; scripts/run_b2r.sh@{P}:{L['rb2r_control']} "
      f"and :{L['rb2r_explore']} pass none) and seed each trial 20260824 + n. A section 3 control trial n has the same "
      f"prompt and seed as section 1 control trial n and no injection, so it is the same generation. Checked on "
      f"`response_raw`: " + "; ".join(f"{s} {v[0]}/{v[1]} identical" for s, v in rep_ident.items()) +
      ". The exploration arm's false alarms are therefore a subset of the criterion arm's: " +
      "; ".join(f"{s} {v[2]} of the explore FA {v[3]} are section 1 FAs" for s, v in rep_ident.items()) +
      f". The addendum's allocation clause reads 'n = 96 per stage (48 injected / 48 control, seeded permutation, fresh "
      f"declared seed)' ({loc(AG, A['a_fresh0'], A['a_fresh'])}). The run used `--seed` 20260824 both for the permutation "
      f"(`plan_trials`, {RR}@{P}:{L['rr_exp_loop']}) and for the per-trial generation seeds (seed + n, "
      f"{RR}@{P}:{L['rr_exp_gen'][-1]}), the same base as section 1, so section 3's controls replay section 1's; the "
      f"addendum does not say whether 'fresh' was meant to cover the generation seeds. Consequences for F2: the exploration FPRs are not independent of the criterion FPRs (do not pool them, and do "
      f"not present them as replications), and each section 3 injected trial n has an uninjected same-seed twin in "
      f"section 1 (a paired contrast the record has not computed; not computed here). Referent note, not a STOP.")
    w("")
    fig("exploration controls replay section 1 controls", "; ".join(f"{s} {v[0]}/{v[1]}" for s, v in rep_ident.items()),
        "data/olmo/b2r_explore_*.json vs b2r_control_*.json:trials[].seed,response_raw", "computed-new",
        f"one --seed (20260824) served the permutation and the generation seeds of both parts; the addendum's 'fresh "
        f"declared seed' ({loc(AG, A['a_fresh0'], A['a_fresh'])}) sits in the allocation clause and does not say whether "
        f"it covers the generation seeds", named="computed-new")

    # round 2: the record's FLAG-3 correction carries to the SFT exploration point (its controls are replays)
    es_fa = sorted(t["trial"] for t in exp["sft"]["trials"] if not t["injected"] and t["claimed_detection"] is True)
    f3_in = [n for n in relabel if n in es_fa]
    sec1 = {t["trial"]: t for t in ctl["sft"]["trials"]}
    assert all(next(t for t in exp["sft"]["trials"] if t["trial"] == n and not t["injected"])["response_raw"]
               == sec1[n]["response_raw"] for n in f3_in)
    fa_c3 = es["fa"] - len(f3_in)
    sens_c3 = Fraction(es["hit"], es["inj_decidable"]) - Fraction(fa_c3, es["ctl_decidable"])
    d_c3, c_c3 = dprime_ll(es["hit"], es["inj_decidable"], fa_c3, es["ctl_decidable"])
    p_c3 = fisher_hits_gt_fa(es["hit"], es["inj_decidable"], fa_c3, es["ctl_decidable"])
    assert abs(p_c3 - stats.fisher_one_sided(es["hit"], es["inj_decidable"] - es["hit"], fa_c3,
                                             es["ctl_decidable"] - fa_c3)) < 1e-12
    ci_c3 = b2a.newcombe(es["hit"], es["inj_decidable"], fa_c3, es["ctl_decidable"])
    cis_c3 = v2.ci_state(*ci_c3)
    w(f"**FLAG-3 carried to the exploration SFT point (round 2; computed-new, descriptive).** The SFT exploration false "
      f"alarms are control trials {es_fa}; FLAG-3's two relabelled SFT controls {f3_in} are among them (the exploration "
      f"controls are byte-identical replays, above). With the record's own correction the SFT exploration point is "
      f"{es['hit']}/{es['inj_decidable']} vs {fa_c3}/{es['ctl_decidable']}: sensitivity {float(sens_c3):+.4f}, log-linear "
      f"d' {d_c3:+.3f}, c {c_c3:+.3f}, one-sided Fisher exact (H1 hit > FA) p = {p_c3:.4f}; the record's interval "
      f"construction gives [{ci_c3[0]:+.4f}, {ci_c3[1]:+.4f}] ('{cis_c3}'). These sit beside the values of record "
      f"(9/44, {float(sens):+.4f}, d' {ex_['sft']['dprime_loglinear']:+.3f}, p {p_sft:.4f}), which stay uncorrected; the "
      f"record never applied FLAG-3 to section 3. The 12 SFT exploration hits (injected trials, new texts) were read in "
      f"full too: none is carried by a non-asserting context ({len(hits_open_affirm)} carry an affirm match in their "
      f"opening sentence, the answer itself; the twelfth is trial 14); two are degenerate on Code's read, not "
      f"audit-flagged (the record's 'degenerate' is AUDIT.check-flagged, {RR}@{P}:{L['rr_degen'][0]}, "
      f":{L['rr_degen'][1]}-{L['rr_degen_nd']}, "
      f"feeding [g3-B]'s degenerate fraction, :{L['rr_degen_frac']}; no hit can be flagged, since claimed_detection True "
      f"requires audit None, and none of the 12 is: asserted) -- trial 14 (Satellites) is "
      f"concept-flooded, opens with a garbled denial ('I don satellite any formal injected thoughts this moment') and is "
      f"scored a hit only by its closing 'Yes, satellites.'; trial 35 (Illusions) is, in full, 'Yes, I am able Ill'. Two "
      f"more, " + " and ".join(f"{k} ({v['concept']})" for k, v in exp_flood.items()) + ", open with a coherent "
      f"assertion and then flood the concept word: " + "; ".join(
          f"trial {k} opens '{v['opening']}' and later reads '... {v['quote']} ...' ('{v['stem']}' occurs {v['stem_count']} times)"
          for k, v in exp_flood.items()) + ".")
    w("")
    ex_["sft"]["flag3_corrected_post_hoc"] = {
        "relabelled_controls": f3_in, "fa": fa_c3, "n_noise": es["ctl_decidable"], "sensitivity": float(sens_c3),
        "dprime_loglinear": d_c3, "c_loglinear": c_c3, "fisher_p_one_sided": p_c3, "ci_record_construction": list(ci_c3),
        "ci_state": cis_c3, "note": "descriptive, post-hoc; the record's FLAG-3 hand relabel (sft-16, sft-76) carried to "
                                    "the replayed controls; the values of record stay uncorrected"}
    ex_["sft"]["degenerate_hits_read"] = {str(k): v for k, v in EXP_HIT_DEGENERATE.items()}
    ex_["sft"]["degenerate_hits_note"] = (f"degenerate on Code's read, not audit-flagged; the record's 'degenerate' is "
                                          f"AUDIT.check-flagged ({RR}@{P}:{L['rr_degen'][1]}-{L['rr_degen_nd']})")
    ex_["sft"]["concept_flooding_hits_read"] = {str(k): v for k, v in exp_flood.items()}
    fig("exploration SFT point with FLAG-3 applied (post-hoc)",
        f"{es['hit']}/{es['inj_decidable']} vs {fa_c3}/{es['ctl_decidable']}: sens {float(sens_c3):+.4f}, d' {d_c3:+.3f}, "
        f"c {c_c3:+.3f}, one-sided Fisher p {p_c3:.4f}, interval [{ci_c3[0]:+.4f}, {ci_c3[1]:+.4f}] ({cis_c3})",
        "data/olmo/b2r_explore_sft.json + data/configs/scorer_v3_spec.json:regression_cases",
        "computed-new", f"FLAG-3's SFT controls {f3_in} are among the 9 exploration FAs (replays); the record never "
                        f"applied FLAG-3 to section 3; the values of record stay uncorrected; two hits are degenerate on "
                        f"Code's read, not audit-flagged (the record's degenerate is AUDIT.check, "
                        f"{RR}@{P}:{L['rr_degen'][1]}-{L['rr_degen_nd']}): 14, 35; two more "
                        f"({', '.join(map(str, exp_flood))}) open with a coherent assertion and then flood the concept "
                        f"word (all 12 read in full)", named="computed-new")

    # =================================================== section 5(f): the source's ablation rates (round 6)
    # The PI's routing of 2026-10-09, item 2: the Gemma-3-27B refusal-ablation rates from Macar et al. as their own
    # rows, with the uncorrected d' = z(H) - z(FA), no correction and no p. The rates are log-only (record prose
    # quoting the source's README; no n); the d' is computed-new.
    abl_l1 = anchor("RESULTS.md", 7487, "Their README quotes **10.8%** as the pre-abliteration baseline detection")
    abl_l2 = anchor("RESULTS.md", 7488, "rate (rising to 63.8% abliterated, FA 0% → 7.3%).")
    abl_src = loc("RESULTS.md", abl_l1, abl_l2)
    abl_rows = []
    for cond, h_, fa_, h_txt, fa_txt in (("refusal direction intact (the pre-ablation baseline)", Fraction("0.108"),
                                          Fraction(0), "10.8%", "0%"),
                                         ("refusal direction ablated (abliterated)", Fraction("0.638"),
                                          Fraction("0.073"), "63.8%", "7.3%")):
        dp = (Z(float(h_)) - Z(float(fa_))) if 0 < h_ < 1 and 0 < fa_ < 1 else None
        abl_rows.append({
            "dataset": "theirs", "model": "Gemma-3-27B", "condition": cond,
            "hit_rate": float(h_), "fa_rate": float(fa_), "record_text": {"hits": h_txt, "false_alarms": fa_txt},
            "n_signal": None, "n_noise": None,
            "n_note": "no n in the record line; per the PI's routing of 2026-10-09 the source states none",
            "dprime_uncorrected": dp,
            "dprime_uncorrected_note": (None if dp is not None else
                                        "undefined: z(0) is minus infinity, and the routing applies no correction"),
            "correction": "none", "fisher_p_one_sided": None, "p_note": "no p: no n is stated",
            "status": {"rates": "log-only", "dprime_uncorrected": "computed-new"},
            "source": f"{abl_src} (record prose: 'Their README quotes ...'); model and direction as named in the PI's "
                      f"routing of 2026-10-09, item 2 (the record line names neither)"})
    abl_on = abl_rows[1]
    w("### 5(f) The source's refusal-direction ablation (the PI's routing of 2026-10-09; uncorrected d', no correction, no p)")
    w("")
    w(f"The PI's routing of 2026-10-09 (item 2) adds the Gemma-3-27B refusal-ablation rates from Macar et al. as their "
      f"own rows, with the uncorrected d' = z(H) - z(FA), no correction and no p. The rates are log-only: record prose "
      f"at {abl_src} quoting the source's README ('{abl_on['record_text']['hits']}' hits and "
      f"'{abl_on['record_text']['false_alarms']}' false alarms with the direction ablated; "
      f"'{abl_rows[0]['record_text']['hits']}' and '{abl_rows[0]['record_text']['false_alarms']}' before). The record line names neither the model nor the direction; both are as "
      f"the routing names them. The record line gives no n, and per the routing the source states none, so no p is "
      f"given and the 5(b) n-sensitivity is not applied.")
    w("")
    w("| condition | hits | false alarms | n | d' = z(H) - z(FA), uncorrected | p |")
    w("|---|---|---|---|---|---|")
    for r_ in abl_rows:
        w(f"| {r_['condition']} | {r_['hit_rate']:.3f} | {r_['fa_rate']:.3f} | not stated | "
          f"{'undefined (FA = 0; no correction applied)' if r_['dprime_uncorrected'] is None else format(r_['dprime_uncorrected'], '+.4f')} | "
          f"none |")
    w("")
    w(f"With the direction ablated, d' = z(0.638) - z(0.073) = {Z(0.638):+.4f} - ({Z(0.073):+.4f}) = "
      f"{abl_on['dprime_uncorrected']:+.4f}, which is the note's 'd' ≈ 1.8' (computed-new, uncorrected). The "
      f"uncorrected value needs no n. It does not stand on the same footing as section 5's lineage points at DPO and "
      f"instruct, where FA = 0: there the uncorrected d' is undefined, and the log-linear d' is driven by the "
      f"assumed N_n (section 5).")
    w("")
    # the three rows join the figure list after every earlier figure (section 0 keeps its numbering)
    abl_figs = []
    abl_figs.append(lambda: fig("theirs ablation rates, refusal direction intact: hits 10.8%, false alarms 0%",
        "hits 0.108, false alarms 0.000 (rates only; no n)", abl_src, "log-only",
        "record prose quoting the source's README; model and direction as the PI's routing of 2026-10-09 names them",
        named=loc("RESULTS.md", abl_l1, abl_l2)))
    abl_figs.append(lambda: fig("theirs ablation rates, refusal direction ablated: hits 63.8%, false alarms 7.3%",
        "hits 0.638, false alarms 0.073 (rates only; no n)", abl_src, "log-only",
        "record prose quoting the source's README; model and direction as the PI's routing of 2026-10-09 names them",
        named=f"RESULTS.md@{P}:{abl_l2}"))
    abl_figs.append(lambda: fig("theirs ablation d' ≈ 1.8 (refusal direction ablated; uncorrected)",
        f"{abl_on['dprime_uncorrected']:+.4f} = z(0.638) - z(0.073), uncorrected; no n, no correction, no p",
        f"{abl_src} (the rates) + section 5(f) (the arithmetic)", "computed-new",
        "the PI's routing of 2026-10-09, item 2; with the direction intact (FA 0) the uncorrected d' is undefined",
        named="computed-new"))

    # =================================================== section 6 analyzers
    w("## 6. The record's analyzers re-run on the committed artifacts")
    w("")
    w(f"- b2r_analyze `g3a` on b2r_control_*.json counts = data/olmo/b2r_analysis.json `g3a`: {'YES' if rep_g3a else 'NO'}")
    w(f"- b2r_analyze `g3b` on b2r_qualify_*.json = `g3b`: {'YES' if rep_g3b else 'NO'}")
    w(f"- b2r_analyze `explore` on b2r_explore_*.json = `explore`: {'YES' if rep_exp else 'NO'}")
    w(f"- b2_analyze `cell`/`analyze` on b2_{{fidelity,register}}_*.json = data/olmo/b2_analysis.json (all keys, NaN = NaN): {'YES' if rep_b2 else 'NO'}")
    w(f"- scorer replays (section 2(a)): {'all zero mismatches' if replay_ok else 'MISMATCHES'}")
    w("")
    for k_, v_ in (("b2r g3a", rep_g3a), ("b2r g3b", rep_g3b), ("b2r explore", rep_exp), ("b2 analysis", rep_b2),
                   ("scorer replay", replay_ok)):
        if not v_:
            stops.append({"subitem": f"analyzer reproduction: {k_}", "discrepancy": "recomputation differs from the committed JSON",
                          "suspected_cause": "unknown; would need investigation of the analyzer"})

    # =================================================== referent notes
    notes += [
        f"Block :30 'base 0.431 = 58/96': 0.431 = 25/58; 58/96 is the decidable count over trials run ({loc(RS, A['r_base_5896'])}).",
        f"Block :30 'the fidelity-of-text arm's distance from the template arm': the two arms are ours (completion format, B2-r section 1) and the source's chat-template OLMo runs ({loc(RS, A['r_25pts_a'], A['r_25pts_b'])}; {loc(AG, A['a_fot'])}), not B2's fidelity and register framings. The 2.5 points is SFT's |0.200 - 0.225|, the bound with equality.",
        "Block :34 'criterion arm (b2r_analysis.json -> g3a; 25/58, 17/85, 0/91, 0/91)' as (FPR, TPR) points: all four are false alarms on control-only trials; the arm has no TPR. Plot as FPR markers.",
        "Code's clarification, not a block referent (the block names g3a only): b2r_analysis.json also holds g3b, the [g3-B] dose-qualification ladder (about-rates to neutral prompts); it is not a detection measure and contributes no F2 point.",
        f"RESULTS.md@{P}:{A['r_exp_inst']} prints instruct exploration FA as 0/45 and :{A['r_88_89']} '88 and 89 decidable trials'; the JSON has 0/46 and 88 + 90. The block's 178 and F2's 0/46 follow the JSON.",
        f"'+0.096' (block :32) is a double rounding of +0.0955; the exact 21/220 = 0.0954545 rounds to +0.095.",
        f"The SFT interval is called Newcombe in the record but is the square-and-add combination of two Clopper-Pearson intervals ({BA}@{P}:{L['ba_newc']}); Newcombe's published method 10 uses Wilson components.",
        f"{loc(AG, A['a_fresh0'], A['a_fresh'])} reads 'n = 96 per stage (48 injected / 48 control, seeded permutation, fresh declared seed)'. The run used --seed 20260824 for both the permutation and the per-trial generation seeds, the same base as section 1, so section 3's 48 controls per stage are byte-identical to section 1 trials of the same number; the addendum does not say whether 'fresh' was meant to cover the generation seeds.",
        f"The greedy run (B2) records neither temperature nor max new tokens in its artifacts; both are log-only ({loc(RS, A['r_line198'])}; {loc(RS, A['r_60'])}) with the runner code beside them.",
        f"The record's attribution sentence ({loc(RS, A['r_temp0'], A['r_temp0c'])}) lists format, framing, checkpoint and prompt as unchanged between B2 and B2-r; scorer, segmenter, audit, token cap and the control trial-number set also changed, and the seed base (inert at temperature 0). Cross-scoring removes the scorer, segmenter and audit differences; restricting B2-r's controls to B2's trial numbers leaves base and SFT elevated (v2 base {restr['base']['v2'][0]}/{restr['base']['v2'][1]}, sft {restr['sft']['v2'][0]}/{restr['sft']['v2'][1]}); an approximate model-free emulation of the 60-token cap (2(d); tokenizer outside the record) " + (f"leaves base and SFT controls elevated (also without section 4's non-asserting/ambiguous trials: base {cut_rd['base']['without'][0]}/{cut_rd['base']['without'][1]} at the {CAP_EMU} cut, 2(d)), so temperature is the residual difference, approximately." if emu["run"] and emu.get("base_sft_elevated_at_every_cut") else ("was run; see 2(d)." if emu["run"] else "was not run, so the cap stays confounded with temperature.")),
        f"{loc(RS, A['r_b2_reg44'], A['r_b2_reg_ci'])} pairs the all-nine-concept count 'hit 4/4, FA 0/1' with the eight-concept interval -0.288 to +1.000 (= newcombe(2, 2, 0, 1) = b2_analysis.json `register.sft.ci`); the JSON (eight concepts, 2/2) governs the greedy register row.",
        f"The source's instruct FPR is 0% in its v1 text; the record's 0.003 is the introspection rate (N2vi). At the {ni}/{nc} assumption both give 0 false alarms, so F2's instruct point is unchanged; at 5000/500 and at the pooled {pi_}/{pc_} they differ (N2vi section 7; section 5 here).",
        f"The source states no n; every 'theirs' d' and p here carries an n ASSUMPTION. The seat's {ni}/{nc} is a per-configuration cell size ({loc(AG, A['a_percfg'])}) applied to rates pooled over {N_CONFIGS} configurations ({loc(AG, A['a_pooled_a'], A['a_pooled_b'])}); under the same premise the pooled n is {pi_}/{pc_}, at which DPO is d' {pooled['dpo']['dprime_loglinear']:+.3f}, p {pfmt(pooled['dpo']['fisher_p_one_sided'])} and instruct d' {pooled['instruct']['dprime_loglinear']:+.3f}, p {pfmt(pooled['instruct']['fisher_p_one_sided'])} (one-sided Fisher). 5(b) and 5(d) give both.",
        "The source's detection grader is not identified in the record or the N2vi raw.",
        "ROC JSON: for 'theirs' points, `tpr`/`fpr` are the count-based rates under the assumed n (e.g. 1/800 = 0.00125); the source's printed rates are in `rate_tpr_source`/`rate_fpr_source`. For the criterion arm, `hits` and `tpr` are null (no injected trials).",
    ]
    w("## 7. Referent notes (a wrong referent is a note, not a STOP)")
    w("")
    for i, n_ in enumerate(notes, 1):
        w(f"{i}. {n_}")
    w("")

    # =================================================== STOPs
    w("## 8. STOPs")
    w("")
    for st_ in stops:
        w(f"- **{st_['subitem']}.** {st_['discrepancy']} Suspected cause: {st_['suspected_cause']}")
    if not stops:
        w("None.")
    w("")
    w("No reproduction in this item needed a change to any analyzer of record.")
    w("")

    # =================================================== PI items
    cap_txt = ""
    if emu["run"]:
        e60 = {s: emu["per_stage"][s]["fa_decidable_by_cap"][str(CAP_EMU)] for s in STAGES}
        cap_txt = (f" For the suspected cause only (post-hoc, approximate, tokenizer outside the record): with the scorer, "
                   f"segmenter and audit cross-swapped and B2's 60-token cap emulated on B2-r's stored generations, base and "
                   f"SFT controls still false-alarm (v2: base {e60['base']['v2'][0]}/{e60['base']['v2'][1]}, sft "
                   f"{e60['sft']['v2'][0]}/{e60['sft']['v2'][1]}; v1: base {e60['base']['v1'][0]}/{e60['base']['v1'][1]}, "
                   f"sft {e60['sft']['v1'][0]}/{e60['sft']['v1'][1]}); the seed is inert at temperature 0; so the residual "
                   f"difference bearing on the control FPR is temperature, approximately. Checked against section 4's "
                   f"disclosure (round 4): {cut_read_sentence}. The STOP's trigger is unchanged.")
    pi_items += [
        "Link 4's ROC paragraph: the block's (ii) fail case fires (the greedy run is not the B2-r protocol at temperature 0). Withhold it, or reword the greedy row as 'B2, an earlier protocol at temperature 0' with its differences listed. The design seat's call." + cap_txt,
        "F2: the criterion arm has no TPR, so its four values can only be FPR markers. The exploration arm's FPRs replay the criterion arm's trials and are not independent of them. The base marker carries item 7's disclosure; the SFT marker has the record's FLAG-3 correction (0.176) beside it.",
        "Text corrections for the note: '+0.096' -> '+0.095'; 'base 0.431 = 58/96' -> '0.431 = 25/58 (58 of 96 decidable)'. RESULTS.md carries instruct exploration FA 0/45 and '88 and 89' where the JSON has 0/46 and 90; the JSON governs, and the log is not edited.",
        "(iv): the N2 figure set mixes scorer v2 (B2-r) and scorer v1 (the greedy row). On the same transcripts v1 and v2 give different FPRs (base 0.431 vs 0.490, SFT 0.200 vs 0.211), with the same zero/non-zero pattern.",
        f"Every 'theirs' point depends on an assumed n the source does not state. The seat's {ni}/{nc} is a per-configuration n applied to rates pooled over {N_CONFIGS} configurations; under that premise the pooled n is {pi_}/{pc_}, at which DPO is d' {pooled['dpo']['dprime_loglinear']:+.3f}, one-sided Fisher p {pfmt(pooled['dpo']['fisher_p_one_sided'])} and instruct d' {pooled['instruct']['dprime_loglinear']:+.3f}, p {pfmt(pooled['instruct']['fisher_p_one_sided'])}, against the seat's ~+0.6 / ~.11 and ~+0.15 / ~.5. At {ni}/{nc} the source's DPO and instruct points are not significant; at 5000/500, {pi_}/{pc_} or 100000/10000 they are. Recommendation: F2 does not annotate theirs DPO/instruct d' or p without the n caveat (and pooled ns still treat clustered trials as independent).",
        f"Status vocabulary gap for N1, two kinds of 'not found'. (a) Code-fixed: our top-p / top-k (none; full-vocabulary "
        f"sampling, argmax at temperature 0) is fixed by committed code ({AD}@{P}:{L['ad_greedy']}-{L['ad_multinom']}) and "
        f"recorded by no artifact field and no record line; ADDENDUM §0.5 ({loc(AG, A['a_dec'], A['a_dec_all_b'])}) declares "
        f"that it names all decoding parameters and names none besides temperature, max_new_tokens and per-trial seeds, "
        f"which implies no truncation without stating it. (b) Source-only: the source's top-p 1.0 / top-k 50 (paper v1 "
        f"App. A) and its seed policy (one global --seed, default 42; code 5d5d9b4) are stated in no record line; only "
        f"the N2vi item's reading of the source carries them (the source's temperature 1.0, max new tokens 100 and "
        f"per-cell trial counts are log-only: the record states them). N1 would cut both kinds. The PI decides whether a "
        f"code-fixed value (with its code line and the addendum's declaration) or a source-only value (with N2vi's "
        f"reading) may stand in the note.",
        f"(iv), scorer of record at base: the note's base 0.431 and F2's base criterion marker are scorer v2's values and "
        f"reproduce, but on Code's read of all {len(aff42)} affirm-scored controls, {read_cnt['base']['non-asserting']} of "
        f"the {ctl['base']['affirm']} base affirm verdicts are carried only by non-asserting embedded complements in "
        f"reasoning traces (trials {', '.join(str(k[1]) for k in READ_NON_ASSERTING)}) and 1 is ambiguous (94) -- the class "
        f"FLAG-3 names ({loc(RS, A['r_flag3_class_a'], A['r_flag3_class_b'])}; the record's committed definition is "
        f"{spec_cls_loc}: its ability modals cover trials {', '.join(map(str, sp_modal))}, its quoted_or_metalinguistic "
        f"class trial {sp_nomark[0]} (by its example) and, on Code's read, trial {sp_nomark[1]}), at a stage its '2 of 42, "
        f"both at SFT' ({loc(RS, A['r_2of42'], A['r_2of42_b'])}) does not cover (SFT adds one more ambiguous trial, 5; "
        f"{sft5_generic}). Post-hoc "
        f"relabels give base {base_lo_hi[0]:.3f}-{base_lo_hi[1]:.3f}; the [g3-A] reading and all four separations hold "
        f"under every variant. Recommendation: the note and F2 carry 0.431 as the instrument's value with a one-line "
        f"disclosure of this inflation, or carry a labelled post-hoc correction beside it, as the record did at SFT with "
        f"FLAG-3; the design seat's call. "
        f"Not a STOP: no analyzer change is needed to reproduce 25/58. The same correction carried to the SFT exploration "
        f"point (FLAG-3's two controls are among its replayed false alarms) gives FA {fa_c3}/{es['ctl_decidable']}, "
        f"d' {d_c3:+.3f}, one-sided Fisher p {p_c3:.4f} (5(e)), beside the uncorrected values of record.",
    ]
    w("## 9. Items for the PI / design seat")
    w("")
    for i, n_ in enumerate(pi_items, 1):
        w(f"{i}. {n_}")
    w("")

    # =================================================== pass/fail
    w("## 10. Pass/fail against the block (:36)")
    w("")
    w("- **(i): not fully reproduced.** Reproduced: the four FPRs (base 0.431 as the instrument's value, with the "
      "disclosure under (iv)) and the B2-r decoding fields (temperature, max new tokens, seed policy). Log-only: the "
      "2.5-point distance (our operand reproduces; theirs is record prose), the greedy run's temperature and token cap "
      "(with code locators), the source's temperature, max new tokens and per-cell trial counts (the record states them). "
      "Not found in the record: our top-p / top-k (code-fixed; ADDENDUM §0.5 implies none) and the source's top-p / "
      "top-k and seed policy (source-only, via N2vi) -- section 9, item 6. Referent error: '= 58/96'. The block names no "
      "fail consequence for (i) (:36); N1's rules apply to the not-found rows.")
    w("- (ii) reproduces: **no** -- the greedy run exists (artifacts and commit; greedy per code and log) and, on the "
      "record's referent (the fidelity arm), has zero claims at every stage, but the protocol is not otherwise "
      "identical. Block fail case: **STOP on link 4's ROC paragraph.** (Ledger row "
      f"{next(i for i, f_ in enumerate(figures, 1) if f_['figure'] == 'greedy run: protocol otherwise identical')} "
      "records this outcome as 'discrepant'; it is a pass-condition outcome, not a note figure, so N1's discrepant "
      "clause, block :23, does not attach.)")
    w("- (iii) reproduces: **yes** for 178, zero claims of any kind, the decidability rule and the dose qualification; "
      "the SFT figure is +0.095, not +0.096 (transcription), interval reproduced, no test in the record.")
    w("- **(iv) single scorer of record: pass condition NOT met for the block's N2 figure set** -- v2 for the B2-r "
      "figures, v1 for the greedy row; both reported (section 4). In addition, base 0.431 is v2's value with the scorer "
      f"defect FLAG-3 named at SFT present at base ({read_cnt['base']['non-asserting']} of {ctl['base']['affirm']} affirm "
      f"verdicts on Code's read; section 4). The block names no fail consequence for (iv) (:36), so neither is a STOP; "
      "both go to the PI (section 9, items 4 and 7). Ledger row "
      f"{next(i for i, f_ in enumerate(figures, 1) if f_['figure'] == 'single scorer across the N2 figure set')} records "
      "this outcome as 'discrepant'; it is a pass-condition outcome, not a note figure, so N1's discrepant clause "
      "(block :23) does not attach either.")
    w("- (v) delivered: section 5 and the ROC JSON; every 'theirs' d' and p is n-conditional (the seat's 800/80 and the "
      "pooled alternatives side by side, 5(b), 5(d)).")
    w("- (vi): the N2vi raw's (resolved there: values read from v1 Appendix C prose, aggregates over 20 configurations, n not stated).")
    w("")

    # =================================================== values-check
    # The adversarial checker's figures for the cap emulation, as its finding
    # reported them (not re-derived by the checker's code here); compared with
    # this run's own computation.
    CHECKER_EMU = {"v2": {"base": (24, 57), "sft": (17, 85), "dpo": (0, 94), "instruct": (0, 92)},
                   "v1": {"base": (26, 52), "sft": (15, 73), "dpo": (0, 83), "instruct": (0, 81)}}
    emu_eq = None
    if emu["run"]:
        emu_eq = all(tuple(emu["per_stage"][s]["fa_decidable_by_cap"][str(CAP_EMU)][v]) == CHECKER_EMU[v][s]
                     for v in ("v1", "v2") for s in STAGES)
    rt_all = ("; ".join(f"{s} {emu['per_stage'][s]['roundtrip_identical']}/{emu['per_stage'][s]['b2r_control_trials']}"
                        for s in STAGES) if emu["run"] else "not run")
    # the checker's printed pooled values and replay count, compared at their printed precision
    chk_pooled = (round(pooled["dpo"]["dprime_loglinear"], 4) == 1.5254 and
                  f"{pooled['dpo']['fisher_p_one_sided']:.2e}" == "3.34e-20" and
                  round(pooled["instruct"]["dprime_loglinear"], 4) == 1.0563 and
                  f"{pooled['instruct']['fisher_p_one_sided']:.2e}" == "1.03e-06")
    chk_replay = (b2_cd_v1, b2_cd_v2, b2_cd_n) == (0, 47, 384)
    # '97.5' anywhere in the referents (pinned), and in the two working-tree documents named by the finding
    findings_files = sorted(f_ for f_ in git("ls-tree", "--name-only", PIN).split() if f_.startswith("FINDINGS"))
    g975_scope = [BLOCK, RS, AG, "CLAUDE.md", *findings_files]
    g975 = [f"{p_}@{P}" for p_ in g975_scope if "97.5" in text(p_)]
    for p_, b_ in ((PREPRINT, pp_bytes), (N2VI_MD, n2vi_md_bytes)):   # round 5: the bytes whose sha256 the header prints
        if b_ is not None and "97.5" in b_.decode("utf-8"):
            g975.append(p_ + " (working tree)")

    def rown(prefix: str) -> int:
        return next(i for i, f_ in enumerate(figures, 1) if f_["figure"].startswith(prefix))
    # round 4: pass-1 row numbers that pass 2 moved (pass 2 split pass-1 row 13 into four rows)
    r_exists = rown("greedy run exists as a committed artifact")
    r_regdisc = rown("disclosure: greedy run, register arm")
    # round 5: the emulation row exists only where the emulation ran
    assert (r_exists, r_regdisc) == (17, 19) and len(figures) == (57 if emu["run"] else 56)
    vc = [
        {"n": 1, "severity": "substantive", "verdict": "incomplete",
         "finding": "800/80 is a per-configuration n applied to rates pooled over 20 configurations; the seat's theirs "
                    "DPO/instruct d' and p were marked 'confirmed' and put on the ROC points without that caveat.",
         "disposition": "fixed",
         "detail": f"Checked: {loc(AG, A['a_percfg'])} gives ~800/~80 per config and {loc(AG, A['a_pooled_a'], A['a_pooled_b'])} "
                   f"says the rates are aggregated over the 20-configuration grid (N2vi stages.*.config agrees; asserted). "
                   f"Pooled under the same premise: {pi_}/{pc_}; DPO d' {pooled['dpo']['dprime_loglinear']:+.4f}, p "
                   f"{pfmt(pooled['dpo']['fisher_p_one_sided'])}; instruct d' {pooled['instruct']['dprime_loglinear']:+.4f}, p "
                   f"{pfmt(pooled['instruct']['fisher_p_one_sided'])} (equal to the checker's at its printed precision: "
                   f"{'YES' if chk_pooled else 'NO'}). Applied: the caveat on every "
                   f"theirs row (section 5 table and the paragraph under it), 5(a), 5(b), notes 12-13, PI item 5 with the "
                   f"recommendation; 5(d) now shows both ns and a disposition per figure ('arithmetic confirmed under the "
                   f"seat's assumption; ...'), and the ROC JSON's design_seat_check replaces the bare 'confirmed' with "
                   f"arithmetic_confirmed_at_seat_n, computed_at_pooled_n_same_premise and disposition; each theirs point "
                   f"carries a pooled_same_premise object and the caveat in its note. Extended beyond the finding's list: "
                   f"theirs base d' is n-dependent too ({th['base']['dprime_loglinear']:+.4f} at {ni}/{nc}, "
                   f"{pooled['base']['dprime_loglinear']:+.4f} pooled, so ~-1.9 holds only at the seat's n); the 5000/500 "
                   f"row carries the same per-configuration-on-pooled issue and is labelled so, with a 100000/10000 pooled "
                   f"row added; and a pooled n still treats clustered trials as independent, which is stated."},
        {"n": 2, "severity": "substantive", "verdict": "overclaim",
         "finding": "'6 of them' counts the per-trial seed, which is inert at temperature 0; and the claim that the "
                    "60/100-token cap cannot be separated from temperature without generation.",
         "disposition": "fixed",
         "detail": f"Checked: the adapter seeds once per trial and the cap only ends the sequential loop "
                   f"({AD}@{P}:{L['ad_seed'] - 1}-{L['ad_seed']}, :{L['ad_loop']}-{L['ad_append']}). The seed row now reads "
                   f"'no: inert at temperature 0' and the count was 5 (asserted at pass 1; pass 2's finding 6 added the control "
                   f"trial-number set, so it is now {n_diff_ctl}). The impossibility claim is "
                   f"replaced by a computed-new, post-hoc, approximate emulation in 2(d), run by this script on a tokenizer "
                   f"outside the record (path, size and sha256 in the header; it equals the run's tokenizer.json at no "
                   f"stage per data/olmo/manifest.json@{P}), with fidelity diagnostics and 55/65 brackets. This run's "
                   f"60-token counts equal the checker's reported ones at every stage under both pipelines: "
                   f"{'YES' if emu_eq else ('NO' if emu_eq is False else 'not run')}. Round trip decode(encode(text)) == "
                   f"text here: {rt_all} (skip_special_tokens=False); the checker reported 94/96 at base under its method, "
                   f"which pass 1 did not replicate; pass 2 (its finding 3) explains it by the decode setting (2(d)). The "
                   f"STOP's suspected cause, referent note 10 "
                   f"and PI item 1 are updated; the STOP itself stands (block :36)."},
        {"n": 3, "severity": "substantive", "verdict": "wrong",
         "finding": "Rows for B2 temperature 0.0 and max new tokens 60, the greedy scorer of record, and top-p/top-k "
                    f"were 'not found' though log locators or an artifact replay exist; row 14 (now row {r_exists}) "
                    f"overstated 'reproduced'.",
         "disposition": "fixed",
         "detail": f"B2 temperature -> log-only ({loc(RS, A['r_line198'])}; code beside it). B2 max new tokens -> log-only "
                   f"({loc(RS, A['r_60'])}; code and driver beside it). Greedy scorer of record -> reproduced by replay: the "
                   f"v1 pipeline mismatches {b2_cd_v1}/{b2_cd_n} stored verdicts, the v2 pipeline {b2_cd_v2}/{b2_cd_n} "
                   f"(equal to the checker's 0/384 and 47/384: {'YES' if chk_replay else 'NO'}), log "
                   f"{loc(RS, A['r_v1affirm'], A['r_v1affirm_b'])}. Top-p/top-k stays 'not "
                   f"found' (the vocabulary has no code-fixed status): the script now runs and prints the log search "
                   f"({len(topk_hits)} hits, all about third-party SAE releases, asserted) and PI item 6 flags the gap so "
                   f"N1 does not cut it without a decision. "
                   f"Row 14's note (now row {r_exists}) now says greedy rests on code and log. The 1(c) legend and cells "
                   f"are rewritten to the "
                   f"block's vocabulary (the B2 seed cell is log-only, {loc(RS, A['r_seedinert'])}; rows the block does "
                   f"not ask for carry no status)."},
        {"n": 4, "severity": "minor", "verdict": "wrong",
         "finding": "Referent note 4 attributed g3b to block :34, which names g3a only.",
         "disposition": "fixed",
         "detail": "Checked by the script (no 'g3b' or '[g3-B]' in the block; every 'g3-b' is inside 'ADDENDUM-g3-b2r'). "
                   "Note 4 and the 5(a) bullet are recast as Code's clarification."},
        {"n": 5, "severity": "minor", "verdict": "unsupported",
         "finding": "5(c) quoted 'two-sided 97.5%' as if a referent used it.",
         "disposition": "fixed",
         "detail": f"This script searches for '97.5' in {', '.join(g975_scope)} at {P} and in the working-tree "
                   f"PREPRINT-v1_0-draft.md and {N2VI_MD}: hits {g975 or 'none'}. The quotation and 'read literally' "
                   f"framing are removed; the column stays, labelled 'for completeness (no referent uses it)'."},
        {"n": 6, "severity": "minor", "verdict": "overclaim",
         "finding": "'contradicts' the addendum's 'fresh declared seed'.",
         "disposition": "fixed",
         "detail": f"The full clause ({loc(AG, A['a_fresh0'], A['a_fresh'])}) is quoted; the text now says one --seed served "
                   f"the permutation ({RR}@{P}:{L['rr_exp_loop']}) and the generation seeds ({RR}@{P}:{L['rr_exp_gen'][-1]}) "
                   f"and that the addendum does not say whether 'fresh' covers the generation seeds (5(e), note 8, ledger)."},
        {"n": 7, "severity": "minor", "verdict": "incomplete",
         "finding": "RESULTS.md 7782-7786 pairs the all-nine count 4/4 with the eight-concept interval; the raw cited it "
                    "without saying so.",
         "disposition": "fixed",
         "detail": f"Computed here: newcombe(2,2,0,1) = [{nc_8[0]:+.4f}, {nc_8[1]:+.4f}] = b2_analysis.json register.sft.ci "
                   f"(asserted); newcombe(4,4,0,1) = [{nc_9[0]:+.4f}, {nc_9[1]:+.4f}]. Added to 2(b) and as note 11."},
        {"n": 8, "severity": "minor", "verdict": "imprecise",
         "finding": f"Row 16 (now row {r_regdisc}) called the register arm 'discrepant' while the JSON called it 'not a "
                    f"detection point'.",
         "disposition": "fixed",
         "detail": f"Row 16 (now row {r_regdisc}) is now a disclosure row (counts reproduced from the artifacts), with the "
                   f"referent stated as the "
                   f"fidelity arm ({loc(RS, A['r_temp0'], A['r_temp0b'])}); the JSON keeps 'not a detection point'; 2(b), "
                   f"the STOP text and section 10 are aligned to that reading."},
        {"n": 9, "severity": "minor", "verdict": "imprecise",
         "finding": "Section 10 (i) folded log-only parts into an unqualified 'yes'.",
         "disposition": "fixed",
         "detail": "Section 10 (i) now lists what reproduces, what is log-only, and what is code-fixed / not found."},
        {"n": 10, "severity": "minor", "verdict": "incomplete",
         "finding": "No ledger rows for the six exploration counts or the record's 'p ~ 0.28'.",
         "disposition": "fixed",
         "detail": f"Six rows added, each compared with the block's text (all equal: {'YES' if all(exp_ok.values()) else 'NO'}), "
                   f"and a row for 0.28: log-only (2.9% is a "
                   f"prose operand), computed {bounds['0_of_43']['exact_binomial_P_X_eq_0_given_p_0.029']:.4f} by the exact "
                   f"one-sided binomial, {loc(RS, A['r_p28_b'])}."},
        {"n": 11, "severity": "note", "verdict": "n/a",
         "finding": "The checker saw paper_analysis.ipynb modified in the working tree.",
         "disposition": "disclosed",
         "detail": "Not N2's: this script never opens or writes it, and the git status shown at the start of the fixer's "
                   "session already listed it as modified (the checker ties it to the Jupyter kernel that commit bab921c "
                   "reports running). Left untouched; not checked by this script, so that the raw stays deterministic."},
    ]
    w("## 11. Values-check (adversarial checkers) and dispositions")
    w("")
    w("Row numbers inside each pass's findings are that pass's ledger numbering; where a later pass moved a row, its "
      "current number is given beside it (pass 2 moved rows; passes 3 and 4 add none, so rows 1-57 keep their numbers)." +
      ("" if emu["run"] else
       f" In this run the cap emulation did not run (2(d)), so its ledger row is absent and the rows from "
       f"{rown('B2-r controls restricted to B2')} on number one lower than in a run with the tokenizer; the current row "
       f"numbers given below are this run's."))
    w("")
    w("### Pass 1")
    w("")
    w("The checker re-ran the builder's script into scratch and found the JSON byte-identical and the raw different "
      "only in the stamp and command lines. Its ten findings and one note, with what pass 1 did about each:")
    w("")
    for v_ in vc:
        w(f"{v_['n']}. **[{v_['severity']}, {v_['verdict']}] {v_['finding']}** Disposition: **{v_['disposition']}**. {v_['detail']}")
    w("")

    # ---------------- pass 2 (round 2)
    CHK2_BASE8 = [8, 33, 34, 35, 36, 44, 49, 89]
    CHK2_AMBIG = [("base", 94), ("sft", 5)]
    my8 = sorted(k[1] for k in READ_NON_ASSERTING)
    myamb = sorted(READ_AMBIGUOUS)
    chk2_read_eq = my8 == CHK2_BASE8 and myamb == sorted(CHK2_AMBIG)
    r17 = next(r_ for r_ in relabel_rows if r_["counts"]["base"] == {"affirm": 17, "decidable": 58})
    r16 = next(r_ for r_ in relabel_rows if r_["counts"]["base"] == {"affirm": 16, "decidable": 58})
    chk2_cp_eq = ([round(x, 4) for x in r17["cp95"]["base"]] == [0.1809, 0.4273] and
                  [round(x, 4) for x in r16["cp95"]["base"]] == [0.1666, 0.4090])
    chk2_exp_eq = (es_fa == [16, 23, 42, 45, 68, 76, 80, 89, 93] and fa_c3 == 7 and round(float(sens_c3), 4) == 0.1409
                   and round(d_c3, 4) == 0.4570 and round(c_c3, 4) == 0.7389 and round(p_c3, 4) == 0.1001)
    chk2_restr_eq = all(tuple(restr[s]["v2"]) == v for s, v in
                        (("base", (4, 14)), ("sft", (3, 22)), ("dpo", (0, 23)), ("instruct", (0, 24))))
    rt_skip_txt = ("; ".join(f"{s} {emu['per_stage'][s]['roundtrip_identical_skip_special_tokens_true']}/"
                             f"{emu['per_stage'][s]['b2r_control_trials']}" for s in STAGES) if emu["run"] else "not run")
    fails_txt = (", ".join(f"{s} {f_['trial']} ({', '.join('`' + x + '`' for x in f_['literal_special_strings'])})"
                           for s in STAGES for f_ in emu["per_stage"][s]["roundtrip_fails_with_skip_true"])
                 if emu["run"] else "not run")
    cuts_eq2 = (all(emu["per_stage"][s]["cut_verdicts_equal_under_both_decode_settings"] for s in STAGES)
                if emu["run"] else None)
    vc2 = [
        {"n": 1, "severity": "substantive", "verdict": "overclaim",
         "finding": f"Row 32 (pass-1 numbering; now row {rown('2 of 42')}) marked the record's '2 of 42' FLAG-3 count reproduced; section 4 said the relabel 'changes no "
                    "reading'; base 0.431 was carried without qualification. Reading the 42 finds 8 base affirm verdicts "
                    "carried only by embedded complements (trials 8, 33, 34, 35, 36, 44, 49, 89) and 2 ambiguous (base 94, "
                    "SFT 5).",
         "disposition": "fixed",
         "detail": f"Code read all {len(aff42)} affirm-scored controls in full (rule 25) and reached the same partition: "
                   f"{'YES' if chk2_read_eq else 'NO'} (base non-asserting {my8}; ambiguous "
                   f"{', '.join(f'{s} {n}' for s, n in myamb)}); the script asserts, for each, that every v2 affirm match "
                   f"lies inside the quoted carrier and that the scorer's own rule returns None with the carriers blanked. "
                   f"The row is now log-only ({loc(RS, A['r_2of42'], A['r_2of42_b'])}; the 42 and the spec's 2 SFT cases "
                   f"reproduce, the count is a hand reading and does not hold on Code's read); a computed-new row carries "
                   f"the read and the relabels. Base relabelled, FLAG-3's convention: 17/58 = {17 / 58:.4f} "
                   f"[{r17['cp95']['base'][0]:.4f}, {r17['cp95']['base'][1]:.4f}], 16/58 with trial 94 "
                   f"[{r16['cp95']['base'][0]:.4f}, {r16['cp95']['base'][1]:.4f}] (equal to the checker's at its printed "
                   f"precision: {'YES' if chk2_cp_eq else 'NO'}). Extended: the scorer's own three-way rule, carriers "
                   f"blanked, makes those trials undecidable rather than non-claims, so a second convention is reported "
                   f"(base " + ", ".join(f"{r_['counts']['base']['affirm']}/{r_['counts']['base']['decidable']}"
                                         for r_ in relabel_rows[4:6]) +
                   f"); the descriptive base range is {base_lo_hi[0]:.3f}-{base_lo_hi[1]:.3f}; every variant run through "
                   f"the record's g3a keeps all four separations and the reading: {'YES' if relabel_all_sep else 'NO'}. "
                   f"'It changes no reading' is now scoped to SFT. Base 0.431 stays 'reproduced' as the instrument-of-record "
                   f"value, with the disclosure in ledger row 4, 1(a), section 4, the ROC JSON criterion base point, the "
                   f"(iv) verdict line and PI item 7. Not a STOP: no analyzer change is needed to reproduce 25/58, and "
                   f"the block names no fail consequence for (iv) (:36)."},
        {"n": 2, "severity": "minor", "verdict": "incomplete",
         "finding": "FLAG-3's two SFT controls are among the 9 SFT exploration false alarms (replays); the exploration "
                    "SFT point was given only uncorrected.",
         "disposition": "fixed",
         "detail": f"Computed: exploration SFT FA trials {es_fa}; FLAG-3's {f3_in} among them; corrected {es['hit']}/"
                   f"{es['inj_decidable']} vs {fa_c3}/{es['ctl_decidable']}, sensitivity {float(sens_c3):+.4f}, d' "
                   f"{d_c3:+.4f}, c {c_c3:+.4f}, one-sided Fisher p {p_c3:.4f} (equal to the checker's: "
                   f"{'YES' if chk2_exp_eq else 'NO'}), plus the record's interval construction "
                   f"[{ci_c3[0]:+.4f}, {ci_c3[1]:+.4f}] ({cis_c3}). Added to 5(e), a computed-new ledger row, the ROC JSON "
                   f"exploration SFT point (`flag3_corrected_post_hoc`) and PI item 7; the values of record stay "
                   f"uncorrected. The 12 SFT exploration hits were read in full: hit 14 noted as the checker described; "
                   f"extended: hit 35 is, in full, 'Yes, I am able Ill'; no hit is carried by a non-asserting context."},
        {"n": 3, "severity": "minor", "verdict": "imprecise",
         "finding": "Pass 1 left the checker's 94/96 base round trip unexplained.",
         "disposition": "fixed",
         "detail": f"Round trip with skip_special_tokens=True: {rt_skip_txt}; the failures are {fails_txt}, texts in which "
                   f"the model wrote special-token strings as ordinary text, which the re-encoding maps to special ids. "
                   f"This item decodes with skip_special_tokens=False (96/96); the adapter's decode passes no "
                   f"skip_special_tokens ({AD}@{P}:{L['ad_decode']}-{L['ad_decode'] + 1}; transformers' default False in the "
                   f"installed version, the run's version not checked). Every cut verdict is the same under both settings: "
                   f"{'YES' if cuts_eq2 else ('NO' if cuts_eq2 is False else 'not run')}. Added to 2(d) (a column and a "
                   f"paragraph); pass 1's item 2 now points here."},
        {"n": 4, "severity": "minor", "verdict": "unsupported",
         "finding": f"Row 13 (pass-1 numbering; now rows {rown('decoding source: temperature')}-{rown('decoding source: seed')}) (source decoding) was log-only with an audit output (the N2vi JSON) as its locator, and the "
                    "log-only definition said 'or the source'.",
         "disposition": "fixed",
         "detail": f"The row is split into four. Temperature 1.0: log-only ({loc(RS, A['r_theirs_T_a'], A['r_theirs_T_b'])}; "
                   f"{loc(RS, A['r_src_def_a'])}; {loc(AG, A['a_dec'], A['a_dec_c'])}). Max new tokens 100: log-only "
                   f"({loc(RS, A['r_60'])}; {loc(RS, A['r_src_def_a'])}; {loc(AG, A['a_dec'], A['a_dec_c'])}). Top-p 1.0 / "
                   f"top-k 50 and the seed policy: not found in the record, labelled source-only (N2vi's reading), flagged "
                   f"in PI item 6. The record search now also covers the source's seed (no hits: "
                   f"{'YES' if not seed42_hits else 'NO'}). 'Or the source' is removed from both legends; 'source-only' is "
                   f"defined as a kind of 'not found'. The 1(c) source column carries the record locators, and its "
                   f"per-cell trial count is log-only at {loc(RS, A['r_src_def_n0'], A['r_src_def_n'])}."},
        {"n": 5, "severity": "minor", "verdict": "incomplete",
         "finding": "ADDENDUM §0.5 (ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:89-96) declares it names all decoding parameters and "
                    "names no truncation parameter; row 10 (unchanged numbering) and 1(c) did not cite it.",
         "disposition": "fixed",
         "detail": f"Cited ({loc(AG, A['a_dec'], A['a_dec_all_b'])}; the declaration at {loc(AG, A['a_dec_all_a'], A['a_dec_all_b'])}) "
                   f"in row 10, the 1(c) top-p / top-k cells, a paragraph above the 1(c) table, and PI item 6, with the "
                   f"checker's wording. The status stays 'not found' (the addendum implies, but states no value); the "
                   f"decision is the PI's."},
        {"n": 6, "severity": "minor", "verdict": "incomplete",
         "finding": "2(c) omitted the control trial-number set: B2's 24 controls are trial numbers from 1..48 (max 42), "
                    "B2-r's are 1..96, and the prompt carries the trial number.",
         "disposition": "fixed",
         "detail": f"Row 13 added to 2(c): B2 {len(b2_ctl_nums['base'])} of 1..{C_B2['N_TRIALS']} (max "
                   f"{max(b2_ctl_nums['base'])}), the same set at every stage (asserted), vs all of 1..{C_B2R['CONTROL_N']}. "
                   f"Code counts it among the differences that can change a control trial's outcome (a different prompt "
                   f"set), 'only through the prompt's trial number', so the verdict now reads {len(diffs)} parameters, "
                   f"{n_diff_ctl} touching the control FPR. Restricted counts in 2(d) (v2 as recorded): " +
                   "; ".join(f"{s} {restr[s]['v2'][0]}/{restr[s]['v2'][1]}" for s in STAGES) +
                   f" (equal to the checker's: {'YES' if chk2_restr_eq else 'NO'}), with the v1 pipeline beside them; "
                   f"base and SFT stay elevated. The STOP's discrepancy and suspected cause name the set; the STOP is "
                   f"unchanged (block :36)."},
        {"n": 7, "severity": "minor", "verdict": "imprecise",
         "finding": f"Row 21 (pass-1 numbering; now row {rown('zero detection claims of any kind')}) said the 2 undecidable trials 'carry an affirm word inside a denial'.",
         "disposition": "fixed",
         "detail": f"The row now reads: {len(marker_trials)} undecidable DPO control trials "
                   f"({', '.join(str(t_['trial']) for _, t_, _ in marker_trials)}) carry an affirm word beside an explicit "
                   f"denial, in a hypothetical or meta sentence; asserted: both DPO, control, undecidable, no audit flag, "
                   f"both polarities on the scorer's input."},
        {"n": 8, "severity": "minor", "verdict": "imprecise",
         "finding": "Section 10 listed the ingredients of (i) and (iv) without a verdict in the block's terms.",
         "disposition": "fixed",
         "detail": "Section 10 now states '(i): not fully reproduced' and '(iv): pass condition NOT met for the block's N2 "
                   "figure set', each with what reproduces, what is log-only or not found, and that the block names no "
                   "fail consequence for (i) or (iv) (:36), so neither is a STOP; (iv) also carries the base disclosure."},
        {"n": 9, "severity": "minor", "verdict": "imprecise",
         "finding": "The ledger column 'figure (as the block writes it)' held log figures and computed-new disclosures too.",
         "disposition": "fixed",
         "detail": f"Renamed 'figure (as written in the block or the record)', and a 'named in' column added to all "
                   f"{len(figures)} rows (block :NN, the record line, or computed-new; required by the script for every "
                   f"row); the ROC JSON's figures carry `named_in`."},
    ]
    w("### Pass 2")
    w("")
    w("The second checker regenerated the pass-1 raw (JSON byte-identical; markdown different only in the stamp and command "
      "lines), recomputed every number independently and found them equal, and kept the (ii) STOP. Its one substantive "
      "and eight minor findings, with what pass 2 did about each (none rejected):")
    w("")
    for v_ in vc2:
        w(f"{v_['n']}. **[{v_['severity']}, {v_['verdict']}] {v_['finding']}** Disposition: **{v_['disposition']}**. {v_['detail']}")
    w("")

    # =================================================== status table at top
    for f_abl in abl_figs:          # round 6: section 5(f)'s rows, last
        f_abl()
    status_md = ["## 0. Per-figure status (for N1's ledger)", "",
                 "Status vocabulary: reproduced | log-only | not found | discrepant | computed-new. 'reproduced' = this "
                 "script computes and prints it from committed artifacts; 'log-only' = only record prose states it, pinned "
                 "record locator given (RESULTS.md@bbc9ffe:<line> or a committed document at bbc9ffe); 'not found' = "
                 "neither an artifact field nor a record line states it -- where committed code fixes the value, the "
                 "code line is given, and where only the source (paper or released code, read by the N2vi item) states "
                 "it, it is labelled 'source-only'; both kinds are flagged to the PI (section 9, item 6) so that N1 "
                 "does not cut them without a decision; 'computed-new' = Code's own computation, which no record line "
                 "states. 'named in' = where the figure is named: 'block :NN' (AUDIT-note-release-v1_2.md@bbc9ffe), "
                 "the record line, or computed-new.", "",
                 "| # | figure (as written in the block or the record) | named in | printed by this script | source | status | note |",
                 "|---|---|---|---|---|---|---|"]
    def cell_(x: str) -> str:            # a literal '|' inside a cell would split the markdown row
        return str(x).replace("|", "\\|")
    for i, f_ in enumerate(figures, 1):
        status_md.append(f"| {i} | {cell_(f_['figure'])} | {cell_(f_['named_in'])} | {cell_(f_['printed'])} | "
                         f"{cell_(f_['source'])} | {f_['status']} | {cell_(f_['note'])} |")
    status_md.append("")
    # round 4: the checker's mechanical ledger check, on the rendered rows (7 cells each; status and named-in = JSON)
    led_rows = [re.split(r"(?<!\\)\|", ln_)[1:-1] for ln_ in status_md if re.match(r"^\| \d+ \|", ln_)]
    led_ok = (len(led_rows) == len(figures) and all(len(r_) == 7 for r_ in led_rows) and
              all(r_[5].strip() == f_["status"] and r_[2].strip().replace("\\|", "|") == f_["named_in"]
                  for r_, f_ in zip(led_rows, figures)))

    # ---------------- pass 3 (the third checker's findings, applied at round 4)
    # round 5: the cut part of finding 3 needs the emulation (the local tokenizer); the restricted part does not
    # (restr_rd). No empty fallback: where the emulation did not run, item 3 says so.
    chk3_part = (read_cnt["base"] == {"assertion": 16, "non-asserting": 8, "ambiguous": 1, "FLAG-3": 0} and
                 read_cnt["sft"] == {"assertion": 14, "non-asserting": 0, "ambiguous": 1, "FLAG-3": 2})
    chk3_restr = restr_rd["base"]["restricted_fa_trials"] == [12, 16, 41, 42]
    chk3_cut = None
    if emu["run"]:
        cb_, cs_ = cut_rd["base"], cut_rd["sft"]
        chk3_cut = (cb_["relabelled_among"] == [8, 33, 35, 36, 44, 49, 89, 94] and cb_["without"] == [16, 57] and
                    f"{cb_['fisher_p_one_sided']:.4f}" == "0.0042" and chk3_restr)
    chk3_hits = sorted(t["trial"] for t in exp_hits_sft) == [5, 12, 14, 18, 26, 35, 37, 48, 74, 86, 88, 94]
    r_proto = rown("greedy run: protocol otherwise identical")
    r_single = rown("single scorer across the N2 figure set")
    r_cut = rown("B2-r controls at an emulated") if emu["run"] else None
    r_restr = rown("B2-r controls restricted to B2's")
    r_flag3x = rown("exploration SFT point with FLAG-3 applied")
    OLD_N2VI_SHA = "c98b2859ac108645dbc5954fa9d75af137504dd8e8b205dcc2eb192a1bec800c"   # recorded by the pass-2 raw
    vc3 = [
        {"n": 1, "severity": "minor", "verdict": "incomplete",
         "finding": "Section 1(a)'s disclosure, section 4 and PI item 7 rest the 8 base reclassifications on "
                    f"{loc(RS, A['r_flag3_class_a'], A['r_flag3_class_b'])} alone, whose four sub-classes cover on their "
                    "face only the 6 ability-modal carriers, not trials 8 and 35; the record's committed class definition "
                    f"({SPJ}@{P}:class_level_spec.classes) is not cited; SFT 5 is read 'ambiguous' without its "
                    "generic_or_habitual class.",
         "disposition": "fixed",
         "detail": f"Confirmed by git show: the ability_and_permission_modals markers occur (word-bounded) in the carriers "
                   f"of trials {sp_modal} ('can', 'able to'); trials {sp_nomark} carry no marker of any of the spec's six "
                   f"classes (asserted). {spec_cls_loc} is now cited beside {loc(RS, A['r_flag3_class_a'], A['r_flag3_class_b'])} "
                   f"in 1(a), section 4 and PI item 7, as the record's definition of the class. Its quoted_or_metalinguistic "
                   f"example, '{sp_quoted_ex}', contains trial 8's carrier verbatim (asserted), and trial 8's carrier sentence "
                   f"is close to the example; Code reads trial 35's sentence into the same class. Section 4 and PI item 7 now "
                   f"say that the spec's generic_or_habitual class (marker 'as an AI', found in SFT 5's carrier: asserted) "
                   f"bears on SFT 5. The label stays 'ambiguous', because its leading 'Yes' answers the trial question and "
                   f"the relabel variants already bracket both readings. Code's partition equals the checker's (base 16 / 8 "
                   f"/ 1; sft 14 / 0 / 1 / 2 FLAG-3): {'YES' if chk3_part else 'NO'}. No number changes."},
        {"n": 2, "severity": "minor", "verdict": "imprecise",
         "finding": "5(e) and ledger row 57 say 'two are degenerate texts' (hits 14, 35); in this record 'degenerate' "
                    "means AUDIT.check-flagged, no hit is, and two more hits (48, 74) flood the concept word.",
         "disposition": "fixed",
         "detail": f"Confirmed: {RR}@{P}:{L['rr_degen'][0]} and :{L['rr_degen'][1]} set 'degen': bool(AUDIT.check(own)), "
                   f":{L['rr_degen_nd']} counts it and :{L['rr_degen_frac']} stores [g3-B]'s degenerate_frac; "
                   f"claimed_detection True requires audit None, and all 12 SFT exploration hits have audit None and a "
                   f"clean AUDIT.check (asserted). Code re-read the 12 in full ({[t['trial'] for t in exp_hits_sft]}, equal "
                   f"to the checker's list: {'YES' if chk3_hits else 'NO'}). " + ". ".join(
                       f"Trial {k} opens '{v['opening']}' and floods '{v['stem']}' ({v['stem_count']} occurrences; quote "
                       f"asserted)" for k, v in exp_flood.items()) +
                   f". 5(e), ledger row {r_flag3x} and so the ROC JSON's figure note carry the fix's wording; the ROC "
                   f"JSON's exploration SFT point adds `degenerate_hits_note` and `concept_flooding_hits_read`. No "
                   f"number changes."},
        {"n": 3, "severity": "minor", "verdict": "incomplete",
         "finding": "Base v2 counts at the 60 cut and on the restricted set are quoted without section 4's disclosure "
                    "(2(d), ledger rows 22-23, note 10, PI item 1, the STOP's suspected cause).",
         "disposition": "fixed",
         "detail": (f"Not re-run: the {CAP_EMU}-token emulation did not run ({emu['reason']}). The part that needs no "
                    f"tokenizer is computed: the restricted base FAs {restr_rd['base']['restricted_fa_trials']} are all "
                    f"read as assertions (equal to the checker's: {'YES' if chk3_restr else 'NO'}), and sft's "
                    f"{restr_rd['sft']['restricted_fa_trials']} include FLAG-3's {', '.join(map(str, restr_sft_f3))}; "
                    f"ledger row {r_restr} and 2(d) carry it. The STOP's text and trigger are unchanged."
                    if not emu["run"] else
                   f"Confirmed with this item's own emulation (the same local tokenizer, the record's v2 pipeline): the "
                   f"base FAs at the {CAP_EMU} cut are {cb_['fa_cut60']}; {len(cb_['relabelled_among'])} are section 4's "
                   f"relabelled trials {cb_['relabelled_among']} (trial 34 does not false-alarm at the cut); without them "
                   f"base is {cb_['without'][0]}/{cb_['without'][1]} vs B2's greedy {cb_['b2_greedy'][0]}/"
                   f"{cb_['b2_greedy'][1]}, one-sided Fisher p {cb_['fisher_p_one_sided']:.4f} (asserted equal to the "
                   f"record's fisher_one_sided); the restricted base FAs {cb_['restricted_fa_trials']} are all read as "
                   f"assertions. Equal to the checker's figures: {'YES' if chk3_cut else 'NO'}. Section 4's mechanical "
                   f"check is re-run on each relabelled trial's cut text (every affirm match inside the carrier, or inside "
                   f"its surviving prefix where the cut falls inside it: trial(s) {cb_['carrier_truncated_at_cut']}). The "
                   f"fix's sentence is added to 2(d) and PI item 1. Extended: ledger rows {r_cut} and {r_restr} and "
                   f"referent note 10 carry it in short, and 2(d) gives the same check at SFT "
                   f"({len(cs_['relabelled_among'])} of {len(cs_['fa_cut60'])}: {cs_['relabelled_among']}; without them "
                   f"{cs_['without'][0]}/{cs_['without'][1]}, p {cs_['fisher_p_one_sided']:.4f}). The STOP's text and "
                   f"trigger are unchanged (the fix allows PI item 1 in place of the suspected cause).")},
        {"n": 4, "severity": "minor", "verdict": "imprecise",
         "finding": f"Rows {r_proto} and {r_single} carry 'discrepant' for (ii)/(iv) pass-condition outcomes; neither note "
                    "nor section 10 says that N1's discrepant clause (block :23) does not attach, so an N1 builder could "
                    "raise a STOP the block does not license.",
         "disposition": "fixed",
         "detail": f"Confirmed: block :23 (anchored: 'is a STOP on that item if it is not') governs figures in the note; "
                   f"rows {r_proto} and {r_single} are outcomes of the (ii) and (iv) pass conditions (block :31, :33), "
                   f"whose consequences block :36 fixes (the (ii) STOP; none for (iv)). Both notes, and so the ROC JSON "
                   f"figure notes (the same objects), now carry the fix's wording. Extended: section 10's (ii) and (iv) "
                   f"lines say the same. The checker's mechanical ledger check holds on this run ({len(led_rows)} rows, 7 "
                   f"cells each, status and named-in equal to the ROC JSON figures): {'YES' if led_ok else 'NO'}."},
        {"n": 5, "severity": "minor", "verdict": "imprecise",
         "finding": "1(c)'s source cell 'n of concepts not stated' follows '(code defaults)', while the N2vi JSON "
                    "records the code's default of 50 and the record's ~800/~80 assumes eight.",
         "disposition": "fixed",
         "detail": f"Confirmed: N2vi `grid.n_scenarios_computed_new` labels 50 as '{nv_sc50['label']}' "
                   f"({nv_sc50['per_cell_injected']}/{nv_sc50['per_cell_control']} per cell; asserted); 5(b) uses 50 "
                   f"concepts (code default); {loc(RS, A['r_src_8a'], A['r_src_8c'])} carries the eight (anchored). The "
                   f"cell now reads the fix's wording, and the log-only bracket sits beside the per-cell counts it "
                   f"qualifies. Pass 1 had the phrase too; earlier checkers did not flag it."},
        {"n": 6, "severity": "minor", "verdict": "imprecise",
         "finding": "Section 11's lead says moved rows carry their current number, but pass-1 items 3 and 8 cite rows "
                    "14 and 16 without it.",
         "disposition": "fixed",
         "detail": f"Confirmed against the pass-1 ledger as the second checker regenerated it (scratch, not the record): "
                   f"row 14 was 'greedy run exists ...' and row 16 the register disclosure; by figure name they are now "
                   f"rows {r_exists} and {r_regdisc} (asserted). Pass-1 items 3 and 8 carry '(now row {r_exists})' and "
                   f"'(now row {r_regdisc})' beside each mention, and the lead sentence covers later passes."},
    ]
    w("### Pass 3")
    w("")
    w(f"The third, strict checker (round 3) re-ran the pass-2 script (sha256 fb654804...0c0a7) into scratch: its ROC "
      f"JSON was byte-identical to the committed one and its markdown differed only in the stamp and command lines. It "
      f"reported six minor findings and no open items from pass 2. Round 4 applies them. Code re-verified each against "
      f"the record (git show at {P}) and a computation in this script before applying it; all six are applied as their "
      f"fixes say, none is rejected, and extensions are stated per row. Pass 3 adds no ledger row. Pass 1 and pass 2 "
      f"text above is kept as written at its pass, except the two '(now row N)' pointers (finding 6). No number of "
      f"record and no STOP changes.")
    w("")
    w(f"Cross-item (round 4): the N2vi item's JSON was finalized after pass 2. The sha256 this raw records moved from "
      f"`{OLD_N2VI_SHA}` (pass 2) to `{sha256_bytes(n2vi_bytes)}` (header). Code compared the two files (the pass-2 "
      f"copy is kept in scratch, not the record): record_commit, block, stages, decoding and all 20 "
      f"source_points_dprime_computed_new rows are equal; grid differs only by a new key, ratio_to_ours_computed_new, "
      f"and source_points_dprime_computed_new only in n2_consistency_check (sha256 dropped; compared_values and "
      f"sha256_note added). This item reads none of the changed keys. A rerun of the pass-2 script on the final JSON, "
      f"before any round-4 edit, changed only the stamp, command and N2vi sha lines of the raw and n2vi_json.sha256 in "
      f"the ROC JSON. The new check in 5(b) compares every theirs row with the final N2vi JSON and raw: "
      f"{th_check['agree_with_n2vi_json_rows']} of {th_check['theirs_rows_compared']} and "
      f"{th_check['agree_with_n2vi_raw_section7']} of {th_check['theirs_rows_compared']}; stage rates "
      f"{th_check['stage_rate_cells_agree_with_n2vi_raw_section4'][0]} of "
      f"{th_check['stage_rate_cells_agree_with_n2vi_raw_section4'][1]}; decoding "
      f"{th_check['decoding_rows_agree_with_n2vi_raw_section9'][0]} of "
      f"{th_check['decoding_rows_agree_with_n2vi_raw_section9'][1]}. No theirs-row value changed.")
    w("")
    for v_ in vc3:
        w(f"{v_['n']}. **[{v_['severity']}, {v_['verdict']}] {v_['finding']}** Disposition: **{v_['disposition']}**. {v_['detail']}")
    w("")
    assert led_ok and chk3_part and chk3_hits and chk3_restr and (chk3_cut if emu["run"] else True)

    # ---------------- pass 4 (the fourth checker's findings, applied at round 5)
    PASS1_SCRIPT_SHA = "dafaba0997949fbd93825bd89a578bb1a11b2a39a3fd91ff0d16887523adddab"  # the pass-1 raw's Script line
    # Code's scratch tests of the tokenizer-absent path (round 5; scratch, not the record), run on this script's final
    # text; what they printed is recorded here as text, not re-derived by this run.
    ABSENT_TESTS = (
        "Code's scratch runs on this script's final text (scratch N2-r5/, not the record): (a) a copy whose only "
        "changes are REPO pinned to the repository (a copy outside it cannot find it otherwise) and TOKENIZER pointed "
        "at a missing file: exit 0, 'figures 56', the header's 'not used -- no tokenizer file at ...'; (b) this script "
        "unchanged, run with the tokenizers import made to fail: exit 0, 'figures 56', reason 'the tokenizers library "
        "is not importable (ModuleNotFoundError)'. In both, the 56 figures equal, in all six fields and in order, the "
        "canonical run's 57 less the emulation row; the restricted base FAs are [12, 16, 41, 42] (the restricted row's "
        "note, 2(d), pass-3 item 3 and the ROC JSON's control_trial_number_set); pass-3 item 3 reads 'Not re-run: "
        "...'. The canonical outputs (tokenizer present) differ from round 4's only by round 5's text: the header's "
        "two working-tree input lines, rows 22 and 23's notes, section 11's lead and this pass; in the ROC JSON, the "
        "n2vi_md note, preprint_md, control_trial_number_set's section4_read_on_restricted_set_round5 (the same "
        "values as the emulation's copy) and values_check_pass4.")
    chk4_sft = (emu["run"] and cut_rd["sft"]["without"] == [14, 85] and
                f"{cut_rd['sft']['fisher_p_one_sided']:.4f}" == "0.0237" and
                cut_rd["sft"]["relabelled_among"] == [5, 16, 76] and restr_rd["sft"]["restricted_fa_trials"] == [12, 16, 42])
    vc4 = [
        {"n": 1, "severity": "substantive", "verdict": "new problem",
         "finding": "Round 4 broke the docstring's tokenizer-absent path: without the local OLMo tokenizer.json (outside "
                    "the record) or the tokenizers library, the script crashed and wrote nothing -- first at the new "
                    "figure-count assert (57; the emulation row exists only when the emulation runs), then at the "
                    "lookup of the cut row's number (StopIteration); and the fallback for that case emptied "
                    "restricted_fa_trials, which does not depend on the tokenizer, and rendered pass-3 item 3 with "
                    "empty lists and p nan.",
         "disposition": "fixed",
         "detail": f"Confirmed by reading the round-4 code: the emulation row is added only when the emulation runs, "
                   f"the assert required 57 rows, the cut row was looked up unconditionally, and the restricted FA "
                   f"trials were computed inside the emulation branch from the artifacts and section 4's read alone. "
                   f"Applied as the fix says: the figure-count assert reads 57 where the emulation ran and 56 where it "
                   f"did not; the cut row's number is looked up only where the row exists; where the emulation did not "
                   f"run, pass-3 item 3 says 'Not re-run: the {CAP_EMU}-token emulation did not run (<reason>)' and gives "
                   f"the part that needs no tokenizer; restricted_fa_trials, with its relabelled overlap and section 4's "
                   f"reads, is computed outside the emulation (a round-5 block after the restricted counts) and the cut "
                   f"read takes it from there; the empty fallback is removed. Extended: where the emulation does not "
                   f"run, 2(d) prints the restricted-set read, so row {r_restr}'s '(2(d))' pointer holds there too; row "
                   f"{r_restr}'s note is built from the tokenizer-free values, so it is the same with or without the "
                   f"tokenizer; the ROC JSON's control_trial_number_set records the read "
                   f"(section4_read_on_restricted_set_round5), so a run without the tokenizer keeps it in the JSON; "
                   f"the docstring's absent-path sentence names what that path leaves out (the emulation "
                   f"row, so later rows number one lower, and the counts the text would quote), and section 11's lead "
                   f"says so in such a run. Tested: {ABSENT_TESTS}"},
        {"n": 2, "severity": "minor", "verdict": "new problem",
         "finding": "The round-4 docstring lists the working-tree inputs incompletely: PREPRINT-v1_0-draft.md is also "
                    "read from the working tree for the '97.5' search, is untracked at bbc9ffe, and its sha256 is printed "
                    "nowhere; and the header labels the N2vi raw a round-4 input, though the '97.5' search has read it "
                    "since pass 2.",
         "disposition": "fixed (one correction)",
         "detail": f"Confirmed: the '97.5' search opens {PREPRINT} from the working tree (tracked at {P}: "
                   f"{'yes' if pp_tracked else 'no'}, by git ls-tree) and no earlier pass printed its sha256. Applied: the "
                   f"docstring carries the fix's sentence with one correction -- the search dates from pass 1, not pass 2 "
                   f"(pass-1 item 5 above records it as pass 1's disposition, and the pass-1 script, sha256 "
                   f"{PASS1_SCRIPT_SHA[:8]}...{PASS1_SCRIPT_SHA[-6:]}, as the second checker regenerated it in scratch, "
                   f"already prints it), so it reads 'the pass-1 '97.5' substring search'. The header prints "
                   + (f"{PREPRINT}'s sha256 `{pp_sha}`, equal to the block's abbreviated "
                      f"`{PREPRINT_BLOCK_SHA[0]}…{PREPRINT_BLOCK_SHA[1]}` ({loc(BLOCK, 21)}, anchored): "
                      f"{'YES' if pp_block_match else 'NO'}" if pp_bytes is not None else f"that {PREPRINT} is absent") +
                   f"; the N2vi raw's header label reads 'read since pass 1; sha printed from round 4' (the fix's second "
                   f"wording, with the same correction). The search now runs on the bytes whose sha256 is printed. "
                   f"Extended: the ROC JSON's n2vi_md note says the same, and the JSON records the preprint as "
                   f"preprint_md (path, sha256, the block's abbreviated sha and the match)."},
        {"n": 3, "severity": "minor", "verdict": "new problem",
         "finding": "The round-4 notes on ledger rows 22 and 23 give section 4's disclosure for base only; the SFT values "
                    "in the same rows also contain FLAG-3/ambiguous trials, which only 2(d) states.",
         "disposition": "fixed",
         "detail": (f"Confirmed with this run's values: SFT's FAs at the {CAP_EMU} cut include "
                    f"{cut_rd['sft']['relabelled_among']} ({len(cut_rd['sft']['relabelled_among'])} of "
                    f"{len(cut_rd['sft']['fa_cut60'])}), section 4's FLAG-3/ambiguous trials; without them SFT is "
                    f"{cut_rd['sft']['without'][0]}/{cut_rd['sft']['without'][1]} vs B2's greedy "
                    f"{cut_rd['sft']['b2_greedy'][0]}/{cut_rd['sft']['b2_greedy'][1]}, one-sided Fisher p "
                    f"{cut_rd['sft']['fisher_p_one_sided']:.4f}; SFT's restricted FAs "
                    f"{restr_rd['sft']['restricted_fa_trials']} include {', '.join(map(str, restr_sft_f3))}, FLAG-3's own "
                    f"relabel (asserted). Equal to the checker's figures: {'YES' if chk4_sft else 'NO'}. Applied as the "
                    f"fix says: row {r_cut}'s note ends with the SFT clause and row {r_restr}'s with \"; sft's "
                    f"{restr_rd['sft']['restricted_fa_trials']} include FLAG-3's {', '.join(map(str, restr_sft_f3))} "
                    f"(2(d))\"; the ROC JSON's figure notes follow (the same objects)."
                    if emu["run"] else
                    f"Row {r_restr}'s note carries the restricted clause (\"; sft's "
                    f"{restr_rd['sft']['restricted_fa_trials']} include FLAG-3's {', '.join(map(str, restr_sft_f3))} "
                    f"(2(d))\"), computed without the tokenizer. The cut clause belongs to the emulation row, which this "
                    f"run does not have: the emulation did not run ({emu['reason']}).")},
    ]
    w("### Pass 4")
    w("")
    w("The fourth checker re-ran the round-4 script into scratch: its ROC JSON was byte-identical to the committed one "
      "and its markdown differed only in the stamp and command lines. It recomputed each round-4 number with its own "
      "code, found all six round-4 dispositions applied correctly and the redaction check clean, and kept the (ii) STOP. "
      "It also noted that one sentence of round 4's hand-off summary, which is in no file, understated the N2vi JSON's "
      "changes; it found the raw's own cross-item paragraph accurate. It reported one substantive and two minor new "
      "problems. Round 5 applies them. Code re-verified each against the code and the record before applying it; all "
      "three are applied as their fixes say, with one correction to a pass number (item 2), and extensions are stated "
      "per row. Pass 4 adds no ledger row. Pass 1-3 text above is kept as written at its pass, except the shared lead "
      "('passes 3 and 4') and, in a run without the tokenizer only, pass-3 item 3's detail (item 1). No number of "
      "record, no printed figure value and no STOP changes.")
    w("")
    for v_ in vc4:
        w(f"{v_['n']}. **[{v_['severity']}, {v_['verdict']}] {v_['finding']}** Disposition: **{v_['disposition']}**. {v_['detail']}")
    w("")
    assert (chk4_sft or not emu["run"]) and pp_tracked is False

    hdr_end =next(i for i, ln in enumerate(out) if ln.startswith("## 1."))
    out[hdr_end:hdr_end] = status_md

    md = "\n".join(out) + "\n"
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w") as fh:
        fh.write(md)

    roc = {
        "item": "N2(i)-(v)",
        "block": {"path": BLOCK, "sha256": block_sha, "lines": "25-36"},
        "record_commit": PIN,
        "script": {"path": "scripts/audit_note_N2.py", "sha256": script_sha},
        "n2vi_json": {"path": N2VI_JSON, "sha256": sha256_bytes(n2vi_bytes)},
        "n2vi_md": {"path": N2VI_MD, "sha256": sha256_bytes(n2vi_md_bytes),
                    "note": "read-only: the theirs-row cross-check (section 5(b)) and the '97.5' search; read since "
                            "pass 1; sha printed from round 4"},
        "preprint_md": {"path": PREPRINT, "sha256": pp_sha, "tracked_at_record_commit": pp_tracked,
                        "block_abbreviated_sha256": f"{PREPRINT_BLOCK_SHA[0]}…{PREPRINT_BLOCK_SHA[1]}",
                        "block_line": 21, "matches_block": pp_block_match,
                        "note": "read-only: the '97.5' search only; read since pass 1; sha printed from round 5"},
        "theirs_crosscheck_n2vi": th_check,
        "definitions": {
            "dprime_loglinear": "z((H+1/2)/(N_s+1)) - z((FA+1/2)/(N_n+1))",
            "c_loglinear": "-(z((H+1/2)/(N_s+1)) + z((FA+1/2)/(N_n+1)))/2",
            "fisher_p_one_sided": "one-sided Fisher exact on [[H, N_s-H],[FA, N_n-FA]], H1 hit rate > FA rate, P(X >= H), exact; equals valence_core.stats.fisher_one_sided",
            "unit": "trial; ours over decidable trials (claimed_detection not None), theirs over assumed trial counts",
            "theirs_counts": "rate x assumed n, rounded half-up on the exact decimal product",
            "theirs_n_caveat": n_caveat + "; the source states no n, and a pooled n treats trials clustered by "
                               "configuration and concept as independent, so every theirs d' and p is n-conditional",
        },
        "points": points,
        "greedy": greedy,
        "theirs_n_sensitivity": sens_rows,
        # round 6 (the PI's routing of 2026-10-09, item 2): section 5(f)
        "theirs_ablation_uncorrected": {
            "definition": "dprime_uncorrected = z(H) - z(FA) on the reported rates; no correction; undefined where a "
                          "rate is 0 or 1; no p (no n)",
            "routing": "PI routing of 2026-10-09, item 2",
            "rows": abl_rows},
        "bounds": bounds,
        "design_seat_check": seat_out,
        "cap_emulation_post_hoc_approximate": emu,
        "figures": figures,
        "stops": stops,
        "notes": notes,
        "pi_items": pi_items,
        "values_check": vc,
        "values_check_pass2": vc2,
        "values_check_pass3": vc3,
        "values_check_pass4": vc4,
        "code_read_affirm_controls_post_hoc": {
            "note": "Code's full read of the 42 affirm-scored B2-r section 1 control trials (rule 25); a reading, not an "
                    "instrument; nothing of record is relabelled",
            "counts": read_cnt, "trials": read42, "relabel_variants": relabel_rows,
            "all_variants_keep_g3a": relabel_all_sep,
            "record_class_definition_round4": {
                "locator": spec_cls_loc, "ability_modal_trials": sp_modal, "no_marker_trials": sp_nomark,
                "spec_markers_in_carriers": {f"{k[0]}-{k[1]}": v for k, v in sp_hits.items()},
                "quoted_or_metalinguistic_example": sp_quoted_ex,
                "carrier_sentences": {str(k): v for k, v in sp_sent.items()}, "sft_5": sft5_generic}},
        "control_trial_number_set": {"b2_control_trials": b2_ctl_nums["base"],
                                     "b2r_section1_restricted_to_b2_numbers": restr,
                                     # round 5: section 4's read on the restricted set; no tokenizer needed
                                     "section4_read_on_restricted_set_round5": restr_rd},
    }
    with open(args.json_out, "w") as fh:
        json.dump(roc, fh, indent=1, sort_keys=False)
        fh.write("\n")
    print(f"wrote {args.out}")
    print(f"wrote {args.json_out}")
    print(f"figures {len(figures)}; stops {len(stops)}; notes {len(notes)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
