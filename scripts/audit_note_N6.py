#!/usr/bin/env python3
"""AUDIT-note-release v1.2, item N6 -- e2b state-present figures.

READ-ONLY ON THE RECORD. Every committed artifact is read at the pin
(`git show bbc9ffe:<path>`). The only record modules imported from the
working tree are the inert ones (valence_core.readout, valence_core.e2b's
records half), and only after their blobs are asserted equal to the pinned
blobs; the quarantined module `valence_core.e2b.statepresent` is never
loaded -- the one import attempt below is the suite's own refusal check, and
the script asserts the module is absent from sys.modules afterwards. No model,
no adapter, no inference. Exact tests are stdlib only (math.comb, math.lgamma,
fractions.Fraction); the record's analyzers use scipy, so every statistic here
is an independent stdlib re-implementation compared against the stored field.
Bytecode writing is disabled so no __pycache__ appears in the repository.
Nothing is written except the two outputs (--out, --json-out).

Usage (from anywhere):
  jlens-qwen36/.venv/bin/python scripts/audit_note_N6.py \
      [--out results/raw/2026-10-08_note-N6-e2b.md] \
      [--json-out results/raw/2026-10-08_note-N6-e2b.json] \
      [--compare-json <a previous run's JSON output; read only; appends a live comparison,
                       so an output written with it is not the canonical raw>]

Deterministic apart from the run-metadata lines (stamp, HEAD at run time,
command line). No randomness is used anywhere.

Round 9 preparation (2026-10-10): re-pointed at the preprint of record, the
patch-v6 text PREPRINT-v1_0-draft.md at sha256 0f4ba501...16c22 (the PI's
ruling 9 of 2026-10-10, as corrected). The block's d6431e97...222b8 is
recorded as the audited, superseded text, archived untracked at
archive/PREPRINT-v1_0-draft.pre-patch-v6.md (out of the release; never
required -- read, if present, only to verify the quoted old :111 line). The
:176 needle re-anchors on the patched text; the :111 needle no longer matches
(patch v6 rewrote that sentence), and the failed check is recorded in §6 as a
finding on the patch for the design seat, not a STOP. The first pass changed
only preprint-tied text. Fix round (2026-10-10): the patch-v6 wording (§6 heading, the finding,
the re-anchor line) is printed only when the working-tree sha256 equals the
text of record, and the rewrite branch fires only when the old needle is absent;
the finding checks each clause of the new sentence (phrase present, and the
computed fact it states); a locator-mismatch list now ends with a full stop.
Second fix round (2026-10-10): the preprint's sha256 is asserted equal to the
text of record in §0, before anything is written (as N5, N7 and N17 do): any
other text exits non-zero with a 'refusing: ... MISMATCH' line and writes
nothing, so a MISMATCH is never credited to 0f4ba501 and never leaves a raw;
the §0 scope clause names both audited-text :111 locators (§6 and the Figures
row, the latter now derived from the committed raw's locator); the gloss
bullet notes that patch v6 rewrites the sentence; the --json-out-following raw
path of the first fix round is reverted (no effect on the default-path run of
record, and not tied to the preprint).

Round 10 preparation (2026-10-12): re-pointed at the preprint of record, the
patch-v7 text PREPRINT-v1_0-draft.md at sha256 d9635ca2...d1fe6 (the PI's
routing of 2026-10-12), asserted in full in §0 before anything is written, as
in round 9 (any other text, or none, refuses the run and writes nothing).
Round 9's text of record, the patch-v6 text 0f4ba501...16c22, is recorded as
archived untracked at archive/PREPRINT-v1_0-draft.pre-patch-v7.md (out of the
release; never required -- read only if present and matching, to quote a v6
line beside its v7 line and to list the lines v7 changes). The audited text's
handling (d6431e97...222b8, archive/PREPRINT-v1_0-draft.pre-patch-v6.md, the
raw @09c3a8c) is as round 9 left it, and a failed check stays a finding on the
patch for the design seat under ruling 9's routing, never a STOP. §6 re-runs
every round-9 check of a preprint sentence on the v7 text and adds round 10:
the v7 disposition of each finding on the patch this item's round-9 raw
(@84801cb) records (unchanged | changed, quoting v6 and v7 | reverted to the
audited sentence -- the audited needle found again on v7, which brings back the
discrepant gloss rather than resolving the finding; the finding's resolution is
the design seat's and N1's call, as round 9 recorded), every check that passed
on v6 and fails on v7, and a screen of the lines v7 changes against the lines
this item reads (on v7, and on v6 per the round-9 raw's locators) and its scope
terms (on both sides of each change, so a deletion or a removed term is caught);
JSON key /preprint/round10 (additive). Fix round (2026-10-12): the v6 side of
each change screened; 'conjunct', 'quarantin' and 'sham envelope' added to the
scope terms (the block's N6 procedure); a disposition's v7 line falls back to
the round-9 raw's v6 line position when the re-anchor fails; the reversion branch
named as such. Nothing not tied to the preprint changed.
"""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True

import argparse
import ast
import collections
import difflib
import hashlib
import importlib
import inspect
import json
import math
import os
import re
import shlex
import subprocess
from fractions import Fraction

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = "bbc9ffe"
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
PREPRINT = "PREPRINT-v1_0-draft.md"
# Round 10: the preprint of record is the patch-v7 text (the PI's routing of 2026-10-12).
PREPRINT_SHA = "d9635ca24d32dcba193cd9aade273de2679c99c5c2218787b410e793a42d1fe6"
PREPRINT_RULING = "the PI's routing of 2026-10-12"
PREPRINT_PATCH = "v7"
# Ruling 9's routing of a failed preprint-sentence check: a finding on the patch for the design seat, not a STOP.
FINDING_RULING = "the PI's ruling 9 of 2026-10-10, as corrected"
# Round 9's text of record, the patch-v6 text (archived untracked; out of the release; never required).
PREPRINT_V6_SHA = "0f4ba501d60a94189e6dc83d28c41826debe50591b9af484fa08d05a41f16c22"
PREPRINT_V6_ARCHIVE = "archive/PREPRINT-v1_0-draft.pre-patch-v7.md"
R9_COMMIT = "84801cb"   # the commit of this item's round-9 raw over the patch-v6 text (DEF_OUT, DEF_JSON)
# Round 10's scope screen: terms of the two e2b sentences this item reads (:111, :176) and of the block's N6
# procedure, searched on both sides of v7's changes.
SCOPE_TERMS = ("e2b", "State-present", "state-present", "Present-tense", "present-tense", "π̂_d", "Δ_first",
               "0.0172", "0.0735", "−0.0104", "47/96", "48/96", "11 of 640", "shadow", "leakage",
               "conjunct", "quarantin", "sham envelope")
# The block's reference: the audited, superseded text (archived untracked; out of the release; never required).
PREPRINT_AUDITED_SHA = "d6431e97d35e5914574ff9884c0e64463a7baf1cf9d279f27ed45a683a6222b8"
PREPRINT_AUDITED_ARCHIVE = "archive/PREPRINT-v1_0-draft.pre-patch-v6.md"
DEF_OUT = "results/raw/2026-10-08_note-N6-e2b.md"
DEF_JSON = "results/raw/2026-10-08_note-N6-e2b.json"
RAW_COMMIT = "09c3a8c"   # the commit of this item's raw over the audited text (DEF_OUT, DEF_JSON)
PRE111_NEEDLE = "(π̂_d = 0.0172 against a 0.0735 bar)"   # the audited text's :111 needle
# The audited text's :111, verbatim: the sentence patch v6 rewrote (its needle and gloss are in the raw at RAW_COMMIT).
PRE111_AUDITED = ("**State-present choice.** For the present-tense cell, in which the state must be live at the "
                  "decision, the read is made with the vector on but only after leakage certification: a "
                  "pre-registered bound on the direct displacement of label logits by the vector (π̂_d = 0.0172 "
                  "against a 0.0735 bar), and counterbalanced maps that turn any residual direct push into noise "
                  "rather than signal.")
QUARANTINED = "valence_core.e2b.statepresent"
# Round 2: the pass-2 run whose Pass-1 comparison paragraph is quoted verbatim in the Values-check
# (that run took --compare-json <session scratch>/builder_N6.json; neither file is in the repository).
PASS2_SCRIPT_SHA = "296ed698ac2aa9fd69a239b3ce4a7f98cf485baa09ad5bd96fc11fa5440108fc"
PASS2_MD_SHA = "9c25f2b8937903e3ef2a32422bec4fd02196defe4806fb26b3be2e717c484cd1"
PASS2_JSON_SHA = "283f0d6d00f5f7fa808bd88e33f7ea1f1054e2c79888aa928553e86a076961ec"
PASS1_JSON_SHA = "9fe16ae8bfbfa133f8426ad4a2089127aa4faaaedfd4464524244302fca288ff"
PASS1_CMP_QUOTE = 'Pass-1 comparison (this run vs the builder\'s JSON, sha256 9fe16ae8bfbfa133, read from the path given by --compare-json; that file is the superseded pass-1 output, kept only in session scratch, so this comparison is a record, not reproducible from the repository): primary same; shadow same; arm_geometry same; marker_forced_end same; envelope_reference same; mde_binomial same; h1 same; bar_derivation same; leak_family same; leak_family_max same; verdict_leak same; menu_a_is_plus_tag same; menu_templates_a_first same; quarantine same; absence_asserting_files same; pinned_sha256 same; wt_equal_pin same; preprint same; stops same; unchanged (pass-1 keys) same. All computed sections the same: True. Figures rows whose value text changed: ["quarantined primitive\'s name (only the locator pinned: \'@bbc9ffe\' inserted)"]; status changes: [\'certification definition (what is displaced, over what set, bounded how): reproduced → computed-new\', "quarantined primitive\'s name: reproduced → computed-new", "what \'quarantined\' enforces: reproduced → computed-new"]; rows new in this pass: [\'47 (state-present) vs 48 (shadow) at the first free read\', \'realised envelope relative to its null\'].'

# ----------------------------------------------------------------- plumbing --

def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    """Read-only git only. Never run inside the jlens-qwen36 clone."""
    assert args[0] in ("show", "rev-parse", "log", "ls-tree", "merge-base",
                       "diff"), args
    if args[0] == "merge-base":
        assert args[1] == "--is-ancestor", args
    if args[0] == "diff":
        assert "--quiet" in args or "-U0" in args, args   # both read-only
    return subprocess.run(["git", "--no-optional-locks", "-C", REPO, *args],
                          check=check, capture_output=True)


def blob_sha1(b: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


_CACHE: dict[str, bytes] = {}


def pinned(path: str) -> bytes:
    if path not in _CACHE:
        _CACHE[path] = git("show", f"{PIN}:{path}").stdout
    return _CACHE[path]


def pinned_text(path: str) -> str:
    return pinned(path).decode("utf-8")


def pinned_json(path: str):
    return json.loads(pinned_text(path))


def blob_equal_to_pin(path: str) -> bool:
    with open(os.path.join(REPO, path), "rb") as f:
        wt = blob_sha1(f.read())
    pn = git("rev-parse", f"{PIN}:{path}").stdout.decode().strip()
    return wt == pn


def lines_with(text: str, needle: str) -> list[int]:
    """1-based line numbers as `git show <pin>:<path> | sed -n` counts them
    (split on '\\n' only)."""
    return [i + 1 for i, l in enumerate(text.split("\n")) if needle in l]


LOCATORS: dict[str, dict] = {}


def loc(path: str, needle: str, key: str | None = None, expect: int = 1,
        text: str | None = None, tag: str = PIN) -> str:
    """Pinned locator for a needle; records the match count. A count other
    than `expect` is recorded as a locator warning (printed in §0)."""
    t = pinned_text(path) if text is None else text
    ls = lines_with(t, needle)
    k = key or f"{path}::{needle[:40]}"
    LOCATORS[k] = {"path": path, "needle": needle, "lines": ls,
                   "expect": expect, "ok": len(ls) == expect}
    if not ls:
        return f"{path}@{tag}: NOT FOUND"
    return f"{path}@{tag}:" + ",".join(str(x) for x in ls)


def L_of(key: str) -> str:
    v = LOCATORS[key]
    return f"{v['path']}@{PIN}:" + ",".join(str(x) for x in v["lines"])


def excerpt(path: str, a: int, b: int, text: str | None = None) -> list[str]:
    t = (pinned_text(path) if text is None else text).split("\n")
    return [f"{path}:{i}: {t[i - 1]}" for i in range(a, b + 1)]


def ancestor(a: str, b: str) -> bool:
    return git("merge-base", "--is-ancestor", a, b, check=False).returncode == 0


def cell(s) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


# ------------------------------------------------------------- exact stats --

def sf_half(k: int, n: int) -> Fraction:
    """P(X >= k | n, 1/2), exact."""
    return Fraction(sum(math.comb(n, i) for i in range(max(k, 0), n + 1)), 2 ** n)


def cdf_half(k: int, n: int) -> Fraction:
    """P(X <= k | n, 1/2), exact."""
    return Fraction(sum(math.comb(n, i) for i in range(0, min(k, n) + 1)), 2 ** n)


def logpmf(i: int, n: int, p: float) -> float:
    if p <= 0.0:
        return 0.0 if i == 0 else -math.inf
    if p >= 1.0:
        return 0.0 if i == n else -math.inf
    return (math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
            + i * math.log(p) + (n - i) * math.log1p(-p))


def pmf_vec(n: int, p: float) -> list[float]:
    return [math.exp(logpmf(i, n, p)) for i in range(n + 1)]


def sf(k: int, n: int, p: float) -> float:
    return math.fsum(math.exp(logpmf(i, n, p)) for i in range(max(k, 0), n + 1))


def cdf(k: int, n: int, p: float) -> float:
    return math.fsum(math.exp(logpmf(i, n, p)) for i in range(0, min(k, n) + 1))


def bisect(f, lo: float, hi: float, it: int = 200) -> float:
    """Root of a monotone f on [lo, hi] (f(lo) and f(hi) of opposite sign)."""
    flo = f(lo)
    for _ in range(it):
        mid = (lo + hi) / 2.0
        fm = f(mid)
        if (fm < 0) == (flo < 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2.0


def clopper_pearson(k: int, n: int, conf: float = 0.95) -> tuple[float, float]:
    """Exact (Clopper-Pearson) interval by bisection on the binomial tails:
    lower solves P(X >= k | p) = a/2, upper solves P(X <= k | p) = a/2."""
    a = (1.0 - conf) / 2.0
    lo = 0.0 if k == 0 else bisect(lambda p: sf(k, n, p) - a, 0.0, 1.0)
    hi = 1.0 if k >= n else bisect(lambda p: cdf(k, n, p) - a, 0.0, 1.0)
    return lo, hi


def critical_k(n: int, alpha: float) -> int:
    for k in range(n + 2):
        if sf_half(k, n) <= Fraction(alpha).limit_denominator(10 ** 9):
            return k
    return n + 1


def np_arange_values(start: float, stop: float, step: float) -> list[float]:
    """numpy.arange's float fill (start + i*delta, delta = (start+step)-start),
    reproduced so the grid the lock arithmetic scanned is the grid scanned
    here, value for value."""
    delta = (start + step) - start
    n = int(math.ceil((stop - start) / step))
    return [start + i * delta for i in range(n)]


def mde_one_sided(n: int, alpha: float, power: float) -> tuple[float, int, int]:
    k = critical_k(n, alpha)
    for i, p1 in enumerate(np_arange_values(0.5, 1.0, 0.0005)):
        if sf(k, n, p1) >= power:
            return p1, k, i
    return 1.0, k, -1


def folded_half(n: int) -> dict[Fraction, Fraction]:
    """Exact distribution of |k/n - 1/2| under Binomial(n, 1/2)."""
    out: dict[Fraction, Fraction] = collections.defaultdict(Fraction)
    for k in range(n + 1):
        out[abs(Fraction(k, n) - Fraction(1, 2))] += Fraction(math.comb(n, k), 2 ** n)
    return dict(out)


def exact_envelope(n_sham: int, n_rand: int) -> dict:
    """max |pseudo-Delta| over two independent null families, exactly."""
    fs, fr = folded_half(n_sham), folded_half(n_rand)
    support = sorted(set(fs) | set(fr))
    cdf_s = {v: sum((p for m, p in fs.items() if m <= v), Fraction(0)) for v in support}
    cdf_r = {v: sum((p for m, p in fr.items() if m <= v), Fraction(0)) for v in support}
    c = {v: cdf_s[v] * cdf_r[v] for v in support}

    def q(alpha: float) -> Fraction:
        for v in support:
            if float(c[v]) >= alpha - 1e-12:
                return v
        return support[-1]
    return {"support": support, "cdf": c, "p50": q(0.50), "p90": q(0.90),
            "p95": q(0.95)}


def conjunctive_power(delta: float, k_binom: int, env_thresh: float,
                      n_map: int = 48, p0: float = 0.5) -> float:
    """P(all three verdict conjuncts fire) at true share p0 + delta, both maps
    at n_map (the lock arithmetic's design point), by exact convolution."""
    pm = pmf_vec(n_map, p0 + delta)
    n_tot = 2 * n_map
    k_env = int(math.floor(n_tot * (p0 + env_thresh) + 1e-9)) + 1
    k_sign = int(math.ceil(p0 * n_map - 1e-9))
    tot = 0.0
    for k1 in range(n_map + 1):
        if k1 < k_sign:
            continue
        for k2 in range(n_map + 1):
            if k2 < k_sign:
                continue
            t = k1 + k2
            if t >= k_binom and t >= k_env:
                tot += pm[k1] * pm[k2]
    return tot


def mde_conjunctive(k_binom: int, env_thresh: float, power: float = 0.80) -> tuple[float, int]:
    for i, d in enumerate(np_arange_values(0.0, 0.5 + 0.0005, 0.0005)):
        if conjunctive_power(d, k_binom, env_thresh) >= power:
            return d, i
    return 0.5, -1


def leak_at_fvr(k_binom: int, env_thresh: float, rate: float = 0.025) -> tuple[float, float, int]:
    prev, prev_r = 0.0, conjunctive_power(0.0, k_binom, env_thresh)
    for i, d in enumerate(np_arange_values(0.0, 0.5 + 0.0005, 0.0005)):
        r = conjunctive_power(d, k_binom, env_thresh)
        if r > rate:
            return prev, prev_r, i - 1
        prev, prev_r = d, r
    return prev, prev_r, -1


def close(a: float, b: float, tol: float = 1e-9) -> bool:
    return a is not None and b is not None and abs(float(a) - float(b)) <= tol


# ------------------------------------------------------------------- output --

OUT: list[str] = []
FIG: list[dict] = []
NOTES: list[str] = []
STOPS: list[dict] = []


def P(s: str = "") -> None:
    OUT.append(s)


def fig(figure: str, value: str, source: str, status: str, note: str = "") -> None:
    FIG.append({"figure": figure, "value": value, "source": source,
                "status": status, "note": note})


def f4(x) -> str:
    return f"{float(x):+.4f}"


def pct(x: float, bar: float) -> str:
    return f"{100.0 * x / bar:.1f}%"


# ---------------------------------------------------------------------- main --

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEF_OUT)
    ap.add_argument("--json-out", default=DEF_JSON)
    ap.add_argument("--compare-json", default=None,
                    help="optional: a previous pass's JSON output to compare the computed sections against")
    args = ap.parse_args()
    out_md = os.path.join(REPO, args.out) if not os.path.isabs(args.out) else args.out
    out_js = (os.path.join(REPO, args.json_out) if not os.path.isabs(args.json_out)
              else args.json_out)

    stamp = subprocess.run(["date", "-u"], capture_output=True, text=True).stdout.strip()
    head = git("rev-parse", "HEAD").stdout.decode().strip()
    pin_full = git("rev-parse", PIN).stdout.decode().strip()
    me = os.path.abspath(__file__)
    with open(me, "rb") as fh:
        me_sha = sha256_bytes(fh.read())
    block_pin_sha = sha256_bytes(pinned(BLOCK))
    cmd = " ".join(shlex.quote(x) for x in [sys.executable, os.path.relpath(me, REPO)]
                   + sys.argv[1:])
    J: dict = {"item": "N6", "pin": pin_full, "head_at_run": head, "stamp": stamp,
               "block_sha256": block_pin_sha, "script_sha256": me_sha,
               "interpreter": sys.executable, "python": sys.version.split()[0],
               "command": cmd}

    P("# AUDIT-note-release v1.2 -- N6: e2b state-present figures")
    P("")
    P(f"- Code stamp: {stamp} (date -u)  [run metadata]")
    P(f"- HEAD at run time: {head}  [run metadata; every record read below is pinned to {PIN}]")
    P(f"- Command: `{cmd}` (cwd: repository root)  [run metadata"
      + ("; no session-scratch input]" if not args.compare_json else
         "; --compare-json given: this output carries a live comparison and is not the canonical raw]"))
    P(f"- Pin: {PIN} = {pin_full}")
    P(f"- Block: `{BLOCK}`@{PIN} sha256 `{block_pin_sha}` "
      f"({'MATCH' if block_pin_sha == BLOCK_SHA else 'MISMATCH'} vs routed 8cd8a9ac...3841); "
      f"item N6 = block lines {','.join(map(str, lines_with(pinned_text(BLOCK), '### N6.')))}-"
      f"{','.join(map(str, lines_with(pinned_text(BLOCK), '*Defends:* link 5 e2b')))}")
    P(f"- Script: `scripts/audit_note_N6.py` sha256 `{me_sha}`")
    P(f"- Interpreter: {sys.executable} (Python {sys.version.split()[0]}); every statistic "
      "is stdlib (math.comb, math.lgamma, fractions.Fraction); no numpy call is made "
      "here (the imported record modules import numpy); no scipy/sklearn; no model")
    P("")
    P("Status vocabulary: reproduced (this script computes it from committed JSON and "
      "prints it) | log-only (prose only; pinned locator) | not found | discrepant | "
      "computed-new (a computation or a code reading the block asks for -- a definition, "
      "a name, what code enforces -- or a post-hoc check labelled as such; numbers inside "
      "a computed-new row are reproduced in their own rows). 'discrepant' on a row whose "
      "every number reproduces means the gloss or characterisation is discrepant, and the "
      "row's note says so. Locators are `path@bbc9ffe:line` as `git show bbc9ffe:<path>` numbers "
      "them. The record's analyzers (scripts/e2b_verdict_analyze.py, "
      "scripts/e2b_h1_gate.py, scripts/h1_power.py) import scipy, which this "
      "interpreter does not have; they are not run. Their statistics are re-implemented "
      "here in the stdlib and compared with the stored fields they wrote.")
    P("")

    # ------------------------------------------------------- §0 integrity --
    P("## 0. Referents and integrity")
    P("")
    data_paths = ["data/e2b/verdict_campaign.json", "data/e2b/verdict_analysis.json",
                  "data/e2b/h1_sessions.json", "data/e2b/h1_gate.json",
                  "data/e2b/h1_power.json", "data/e2b/h1u_sessions.json",
                  "data/e2b/h2_sessions.json", "data/e2b/h2_read_stability.json",
                  "data/e2b/lockh_verify.json", "data/e2b/lockh_verify_nd200.json",
                  "data/e2b/lockh_verify_v11.json", "data/e2b/lockh_v2_valuescheck.json"]
    code_paths = ["scripts/e2b_verdict_analyze.py", "scripts/e2b_h1_gate.py",
                  "scripts/h1_power.py", "scripts/e2b_h1_sessions.py",
                  "scripts/e2b_verdict_campaign.py", "valence_core/e2b/__init__.py",
                  "valence_core/e2b/statepresent.py", "valence_core/e2b/records.py",
                  "valence_core/readout.py", "valence_core/regression/analysis.py",
                  "valence_core/session_e2a.py",
                  "PROPOSAL-h-state-present-choice.md", "LOCK-h.md", "CLAUDE.md",
                  "FINDINGS-5.md", "RESULTS.md",
                  "results/raw/2026-08-22_verdict_analysis.txt",
                  "results/raw/2026-08-21_h1_gate_eval.txt"]
    P("Committed artifacts and texts read at the pin (sha256 of the pinned blob, first 16):")
    P("")
    J["pinned_sha256"] = {}
    for p in data_paths + code_paths:
        h = sha256_bytes(pinned(p))
        J["pinned_sha256"][p] = h
        P(f"- `{p}` `{h[:16]}`")
    P("")
    imported = ["valence_core/__init__.py", "valence_core/adapters/__init__.py",
                "valence_core/adapters/base.py", "valence_core/readout.py",
                "valence_core/e2b/__init__.py", "valence_core/e2b/records.py",
                "valence_core/e2b/statepresent.py"]
    P("Working-tree blobs of every module this script imports (or attempts to import), "
      "against the pin (git blob id computed in Python vs `git rev-parse bbc9ffe:<path>`):")
    P("")
    eq_all = True
    J["wt_equal_pin"] = {}
    for p in imported:
        e = blob_equal_to_pin(p)
        eq_all &= e
        J["wt_equal_pin"][p] = e
        P(f"- `{p}`: {'EQUAL to pin' if e else 'DIFFERS from pin'}")
    P("")
    if not eq_all:
        P("**Working tree differs from the pin for an imported module; live checks in §5 "
          "describe the working tree, not the pin.**")
        P("")
    with open(os.path.join(REPO, PREPRINT), "rb") as fh:
        pre_bytes = fh.read()
    pre_sha = sha256_bytes(pre_bytes)
    pre_text = pre_bytes.decode("utf-8")
    tracked_pre = git("ls-tree", PIN, PREPRINT).stdout.decode().strip() != ""
    pre_match = pre_sha == PREPRINT_SHA
    if not pre_match:   # round 9: asserted in full, before anything is written (as N5, N7, N17)
        raise SystemExit(f"refusing: `{PREPRINT}` sha256 {pre_sha} is not the preprint of record "
                         f"{PREPRINT_SHA} ({PREPRINT_RULING}); MISMATCH: the working-tree file is not "
                         "credited to the text of record, and nothing is written")
    # Past the gate pre_match is True; the pre_match conditions below are kept as guards.
    # the rewrite branch: the working tree IS the text of record and the audited needle is absent from it
    pre111_patched = pre_match and lines_with(pre_text, PRE111_NEEDLE) == []
    P(f"- `{PREPRINT}` (root, {'tracked' if tracked_pre else 'UNTRACKED: absent from any clone'}) "
      f"sha256 `{pre_sha}` ({'MATCH' if pre_match else 'MISMATCH'} vs the preprint of "
      f"record {PREPRINT_SHA[:8]}...{PREPRINT_SHA[-5:]}, patch {PREPRINT_PATCH}, {PREPRINT_RULING}; round 9's "
      f"text of record, the patch-v6 text {PREPRINT_V6_SHA[:8]}...{PREPRINT_V6_SHA[-5:]}, is archived untracked "
      f"at {PREPRINT_V6_ARCHIVE} (out of the release; read only if present and matching, §6); the block's "
      f"{PREPRINT_AUDITED_SHA[:8]}...{PREPRINT_AUDITED_SHA[-5:]} is the audited, superseded text, archived "
      f"untracked at {PREPRINT_AUDITED_ARCHIVE} and not required here). Its locators below are "
      "working-tree lines of that file"
      + (f", except the audited-text :111 locators (§6 and the Figures row), which are read from this "
         f"item's committed raw {DEF_JSON}@{RAW_COMMIT}." if pre111_patched else "."))
    J["preprint"] = {"sha256": pre_sha, "match": pre_match, "tracked": tracked_pre,
                     "of_record_sha256": PREPRINT_SHA, "of_record_ruling": PREPRINT_RULING,
                     "audited_sha256": PREPRINT_AUDITED_SHA, "audited_archive": PREPRINT_AUDITED_ARCHIVE}
    P("")

    # provenance order (read-only git)
    order = [("34eb7ee", "PROPOSAL-h committed (pre-registration of record)"),
             ("6897b67", "quarantine built: statepresent.py, records.py, suite checks"),
             ("8a97513", "LOCK-h v1.1 committed (bar_leak 0.0735 fixed)"),
             ("d94e281", "LOCK-h v1.4 committed (steered-rounds clarification, LOCK-h.md@bbc9ffe:248; "
                         "also carries h1u_sessions.json)"),
             ("7527270", "H1 gate run of record: h1_sessions.json + h1_gate.json"),
             ("b400083", "PROPOSAL-h interpretive note appended (steered rounds); criteria lines unchanged"),
             ("f030cdd", "LOCK-h v2.0 committed (licenses the verdict tier)"),
             ("a2f074d", "scripts/e2b_verdict_analyze.py committed"),
             ("485cc94", "verdict_campaign.json + verdict_analysis.json committed")]
    P("Commit order (`git merge-base --is-ancestor`, read-only), and dates as git records them:")
    P("")
    P("| commit | what | ancestor of next | author date |")
    P("|---|---|---|---|")
    J["commit_order"] = []
    for i, (c, what) in enumerate(order):
        nxt = order[i + 1][0] if i + 1 < len(order) else None
        anc = ancestor(c, nxt) if nxt else None
        date = git("log", "-1", "--format=%ad", "--date=iso-strict", c).stdout.decode().strip()
        J["commit_order"].append({"commit": c, "what": what, "ancestor_of_next": anc, "date": date})
        P(f"| `{c}` | {what} | {'' if nxt is None else ('YES -> ' + nxt if anc else 'NO -> ' + nxt)} | {date} |")
    P("")
    an_same = git("diff", "--quiet", "a2f074d", PIN, "--", "scripts/e2b_verdict_analyze.py",
                  check=False).returncode == 0
    sp_same = git("diff", "--quiet", "6897b67", PIN, "--", "valence_core/e2b/statepresent.py",
                  "valence_core/e2b/records.py", check=False).returncode == 0
    gate_same = git("diff", "--quiet", "7527270", PIN, "--", "scripts/e2b_h1_gate.py",
                    "data/e2b/h1_gate.json", "data/e2b/h1_sessions.json",
                    check=False).returncode == 0
    P(f"- `scripts/e2b_verdict_analyze.py` at a2f074d == at {PIN}: {an_same} "
      "(the analyzer of record is the committed-before-data one, unchanged since)")
    P(f"- `valence_core/e2b/statepresent.py` + `records.py` at 6897b67 == at {PIN}: {sp_same} "
      "(the code cited in §5 is the code H1 and the verdict campaign ran)")
    P(f"- `scripts/e2b_h1_gate.py` + `data/e2b/h1_gate.json` + `h1_sessions.json` at 7527270 == "
      f"at {PIN}: {gate_same}")
    ro_same = {c_: git("diff", "--quiet", c_, PIN, "--", "valence_core/readout.py",
                       check=False).returncode == 0 for c_ in ("6897b67", "485cc94")}
    P(f"- `valence_core/readout.py` (the insulated `choice_read`, the shadow's primitive) at 6897b67 "
      f"== at {PIN}: {ro_same['6897b67']}; at 485cc94 == at {PIN}: {ro_same['485cc94']}")
    # round 2 (R2-F2): the H1 runner and the menu-template module, at the data commits
    H1R = "scripts/e2b_h1_sessions.py"
    h1r_same = git("diff", "--quiet", "7527270", PIN, "--", H1R, check=False).returncode == 0
    h1r_commits = [c_ for c_ in git("log", "--format=%h", f"7527270..{PIN}", "--", H1R)
                   .stdout.decode().split("\n") if c_]
    _d0 = git("diff", "-U0", "7527270", PIN, "--", H1R).stdout.decode("utf-8").split("\n")
    _hunks_s: list[list[tuple[str, str]]] = []
    for l_ in _d0:
        if l_.startswith("@@"):
            _hunks_s.append([])
        elif _hunks_s and l_[:1] in ("+", "-") and not l_.startswith(("+++", "---")):
            _hunks_s[-1].append((l_[0], l_[1:]))
    _hunks = [[x_ for _s, x_ in h] for h in _hunks_s]
    _ldr = ("_new_qwen_adapter", "QWEN_PY", "qwen_or_explain")

    def _hunk_kind(h: list[str]) -> str:
        if any(m_ in x_ for x_ in h for m_ in _ldr):
            return "adapter loader"
        if h and h[0].lstrip().startswith(("from ", "import ")) and all(
                x_.lstrip().startswith(("from ", "import ")) or (x_.startswith(" ") and x_.strip())
                for x_ in h):
            return "imports"
        return "other"
    h1r_kinds = collections.Counter(_hunk_kind(h) for h in _hunks)
    # the moved import block: removed (e2b.session) vs added (session_e2a), module name aside
    _imp_rm = [x_ for h in _hunks_s if _hunk_kind([t for _s, t in h]) == "imports"
               for s_, x_ in h if s_ == "-"]
    _imp_add = [x_ for h in _hunks_s if _hunk_kind([t for _s, t in h]) == "imports"
                for s_, x_ in h if s_ == "+" and "qwen_or_explain" not in x_]
    h1r_import_moved_same = bool(_imp_rm) and [x_.replace("valence_core.e2b.session ", "valence_core.session_e2a ")
                                               for x_ in _imp_rm] == _imp_add
    h1_old_t = git("show", f"7527270:{H1R}").stdout.decode("utf-8").split("\n")
    h1_pin_t = pinned_text(H1R).split("\n")
    h1r_slices = []
    for (a_, b_) in [(171, 174), (213, 225), (210, 215)]:
        sl = h1_pin_t[a_ - 1:b_]
        hits = [i_ + 1 for i_ in range(len(h1_old_t) - len(sl) + 1) if h1_old_t[i_:i_ + len(sl)] == sl]
        h1r_slices.append({"pin": [a_, b_], "at_7527270": ([hits[0], hits[0] + b_ - a_] if len(hits) == 1
                                                           else None), "n_hits": len(hits)})
    h1r_slices_ok = all(s_["n_hits"] == 1 for s_ in h1r_slices)

    def _menu_tuple(commit: str, path: str):
        src_ = git("show", f"{commit}:{path}").stdout.decode("utf-8")
        for node in ast.parse(src_).body:
            if (isinstance(node, ast.Assign) and len(node.targets) == 1
                    and isinstance(node.targets[0], ast.Name) and node.targets[0].id == "MENU_TEMPLATES"):
                return ast.literal_eval(node.value), node.lineno
        return None, None
    mt = {c_: _menu_tuple(c_, p_) for c_, p_ in (("7527270", "valence_core/e2b/session.py"),
                                                   ("485cc94", "valence_core/e2b/session.py"),
                                                   (PIN, "valence_core/session_e2a.py"))}
    mt_equal = len({mt[c_][0] for c_ in mt}) == 1 and mt[PIN][0] is not None
    mt_ab = sum(1 for t_ in mt[PIN][0] if "{a}, {b}" in t_) if mt[PIN][0] else 0
    _ns = git("show", "-M", "--name-status", "--format=", "1465b34").stdout.decode("utf-8").split("\n")
    mt_renamed = any(l_.startswith("R") and "valence_core/e2b/session.py" in l_
                     and "valence_core/session_e2a.py" in l_ for l_ in _ns)
    P(f"- `{H1R}` (the H1 runner §3b quotes and §4 cites) at 7527270 == at {PIN}: {h1r_same}. "
      f"It changed after the H1 data in {len(h1r_commits)} commit(s), {', '.join(h1r_commits)} (the "
      f"2026-08-22 consolidation; `git log 7527270..{PIN}`), whose {len(_hunks)} diff hunks are "
      f"imports {h1r_kinds.get('imports', 0)} and the adapter loader {h1r_kinds.get('adapter loader', 0)} "
      f"(the loader's own import counted with the loader; other: {h1r_kinds.get('other', 0)}); the moved import block is the same text apart from the "
      f"module name (`valence_core.e2b.session` → `valence_core.session_e2a`): {h1r_import_moved_same}. "
      "The lines quoted and cited are byte-identical at the H1 "
      "data commit: " + "; ".join(f"{PIN}:{s_['pin'][0]}-{s_['pin'][1]} = 7527270:"
                                   f"{s_['at_7527270'][0]}-{s_['at_7527270'][1]}" if s_["at_7527270"]
                                   else f"{PIN}:{s_['pin'][0]}-{s_['pin'][1]} NOT FOUND at 7527270"
                                   for s_ in h1r_slices) + ".")
    P(f"- `MENU_TEMPLATES` (§4) lived in `valence_core/e2b/session.py` at the H1 and verdict data commits "
      f"(7527270:{mt['7527270'][1]}, 485cc94:{mt['485cc94'][1]}); 1465b34 renamed that file to "
      f"`valence_core/session_e2a.py` (rename in its name-status: {mt_renamed}); the tuple is identical at "
      f"all three commits: {mt_equal} ({len(mt[PIN][0]) if mt[PIN][0] else 0} templates, {mt_ab} listing "
      "`{a}, {b}`).")
    J["h1_runner_drift"] = {"same_as_7527270": h1r_same, "commits_after_7527270": h1r_commits,
                            "hunks": len(_hunks), "hunk_kinds": dict(h1r_kinds),
                            "import_block_moved_same": h1r_import_moved_same,
                            "slices": h1r_slices, "slices_identical": h1r_slices_ok,
                            "menu_templates_lines": {c_: mt[c_][1] for c_ in mt},
                            "menu_templates_equal": mt_equal, "menu_templates_renamed_1465b34": mt_renamed}
    # PROPOSAL-h: the pinned text is the 34eb7ee text plus an appended note (b400083)
    PH = "PROPOSAL-h-state-present-choice.md"
    ph_old = git("show", f"34eb7ee:{PH}").stdout.decode("utf-8").split("\n")
    ph_pin = pinned_text(PH).split("\n")
    ph_hist = [l_ for l_ in git("log", "--format=%h", PIN, "--", PH).stdout.decode().split("\n") if l_]
    n_keep = len(ph_old) - (1 if ph_old and ph_old[-1] == "" else 0)
    ph_prefix_equal = ph_pin[:n_keep] == ph_old[:n_keep]
    ph_added = len(ph_pin) - len(ph_old)
    ph_b4_eq_pin = git("diff", "--quiet", "b400083", PIN, "--", PH, check=False).returncode == 0
    ph_cited = sorted(set(
        lines_with(pinned_text(PH), "counterbalanced Δ_first exceeds the campaign's own control envelope")
        + lines_with(pinned_text(PH), "`choice_read_statepresent` is a distinct function in the e2b")
        + lines_with(pinned_text(PH), "**Verdict criteria [LOCK-h formula], conjunctive")
        + lines_with(pinned_text(PH), "(max pseudo-Δ across sham and random families)")))
    ph_cited_in_prefix = bool(ph_cited) and all(x <= n_keep for x in ph_cited)
    P(f"- `{PH}` history at the pin: {ph_hist} (newest first). The pinned text's first {n_keep} lines "
      f"== the 34eb7ee text: {ph_prefix_equal}; b400083 appends {ph_added} lines (the interpretive "
      f"note dated 2026-08-21 in its text); b400083 == pin: {ph_b4_eq_pin}. The PROPOSAL-h criteria "
      f"and name lines this raw cites ({', '.join(':' + str(x) for x in ph_cited)}) lie in the "
      f"unchanged prefix: {ph_cited_in_prefix}; its one other PROPOSAL-h locator (§3b) is the "
      f"appended note itself. Ordering questions about the note belong to N13.")
    J["unchanged"] = {"analyzer_a2f074d": an_same, "statepresent_records_6897b67": sp_same,
                      "h1_gate_7527270": gate_same, "readout_6897b67": ro_same["6897b67"],
                      "readout_485cc94": ro_same["485cc94"]}
    J["proposal_h_history"] = {"commits": ph_hist, "prefix_lines_equal_34eb7ee": n_keep,
                               "prefix_equal": ph_prefix_equal, "lines_appended_b400083": ph_added,
                               "b400083_equals_pin": ph_b4_eq_pin, "cited_lines": ph_cited,
                               "cited_lines_in_prefix": ph_cited_in_prefix}
    P("")

    # ---------------------------------------------- §1 the VERDICTS entry --
    R = "RESULTS.md"
    P("## 1. The e2b VERDICTS entry (Code locates)")
    P("")
    l_entry = loc(R, "e2b VERDICT CAMPAIGN: NULL. All three conjuncts fail.", "R.verdict_entry")
    l_disp = loc(R, "e2b DISPOSITION (design instance): the NULL is", "R.disposition")
    l_h1 = loc(R, "H1 GATE RUN OF RECORD: reached its declared exit at", "R.h1_entry")
    P(f"- Verdict entry (Code, 2026-08-22): {l_entry} (the entry runs to the next dated "
      "bullet; its conjunct table and descriptives are located figure by figure below).")
    P(f"- Disposition (design instance, 2026-08-22): {l_disp}.")
    P(f"- H1 gate run of record (Code, 2026-08-21): {l_h1}.")
    P("- The block names these referents correctly; `data/e2b/verdict_analysis.json` "
      "(written by the analyzer) and `data/e2b/verdict_campaign.json` (the per-session "
      "record it reads) are the figures' artifacts.")
    P("")

    # ------------------------------------------------- §2 the primary --
    P("## 2. Δ_first, the three conjuncts, and the control envelope")
    P("")
    A = "scripts/e2b_verdict_analyze.py"
    P("### 2a. Definitions, quoted from the analyzer of record (committed a2f074d, before the campaign)")
    P("")
    P("```")
    for (a_, b_) in [(12, 19), (61, 72), (104, 118), (221, 231)]:
        for line in excerpt(A, a_, b_):
            P(line)
        P("...")
    P("```")
    P("")
    l_lockprim = loc("LOCK-h.md", "**Primary criterion (values in place):**", "L.primary")
    l_lockenv = loc("LOCK-h.md", "campaign's own realised control envelope (max |pseudo-Δ| across the",
                    "L.envelope")
    l_proph = loc("PROPOSAL-h-state-present-choice.md",
                  "counterbalanced Δ_first exceeds the campaign's own control envelope", "Ph.criteria")
    P(f"Registered text: PROPOSAL-h §3 {l_proph}; LOCK-h v2.0 §2 {l_lockprim} (envelope "
      f"{l_lockenv}). In words: Δ_first = (first free picks to the map's +tag)/n − ½ over "
      "the marker family's valid sessions (pooled over both label maps); (i) Δ_first must "
      "STRICTLY exceed the realised control envelope = max(|pseudo-Δ_sham|, |pseudo-Δ_random|), "
      "each pseudo-Δ computed identically (sham: no state anywhere, the +tag nominal, the "
      "read through the untouched `readout.choice_read`; random: a norm-matched random "
      "direction at the same layer and |α|, live per the identical delivery schedule); "
      "(ii) Δ ≥ 0 in BOTH label maps; (iii) one-sided exact binomial P(X ≥ k | n, ½) ≤ .05, "
      "direction pre-registered as approach. The block's \"sham envelope\" is this "
      "envelope; the record defines it over the sham AND random families (the realised "
      "maximum happened to come from sham).")
    P("")
    # round 2 (R2-F1): where the |.| comes from; filled in once dm/ds/dr are computed (below)
    i_abs = len(OUT)
    P("<abs-sentence>")
    P("")

    V = pinned_json("data/e2b/verdict_campaign.json")
    VA = pinned_json("data/e2b/verdict_analysis.json")
    S = V["sessions"]
    valid = {arm: [s for s in S if s["arm"] == arm and s["valid"]] for arm in ("marker", "sham", "random")}

    # integrity of the per-session field against the per-read record
    ffp_ok = 0
    ffp_n = 0
    for arm, ss in valid.items():
        for s in ss:
            ch0 = s["choices"][0]
            ffp_n += 1
            ffp_ok += int(s["first_free_pick_pos"] == (ch0["pick"] == s["stratum"]["tag_plus"])
                          == (ch0["picked_pole"] == "pos"))
    pick_src_ok = 0
    pick_src_n = 0
    for arm, ss in valid.items():
        for s in ss:
            for ch in s["choices"]:
                pr = ch["paired_read"]
                pick_src_n += 1
                if arm == "sham":
                    pick_src_ok += int(pr.get("state_present") is None and ch["pick"] == pr["shadow"]["pick"])
                else:
                    pick_src_ok += int(pr["state_present"] is not None
                                       and ch["pick"] == pr["state_present"]["pick"])

    def dfirst(ss):
        k = sum(1 for s in ss if s["choices"][0]["pick"] == s["stratum"]["tag_plus"])
        n = len(ss)
        return k, n, Fraction(k, n) - Fraction(1, 2)

    km, nm, dm = dfirst(valid["marker"])
    ks, ns_, ds = dfirst(valid["sham"])
    kr, nr, dr = dfirst(valid["random"])
    env = max(abs(ds), abs(dr))
    env_src = "sham" if abs(ds) >= abs(dr) else "random"
    maps = {}
    for m in (0, 1):
        maps[m] = dfirst([s for s in valid["marker"] if s["stratum"]["map"] == m])
    p_one = sf_half(km, nm)
    p_rev = cdf_half(km, nm)
    kcrit = critical_k(nm, 0.05)
    c1 = dm > env
    c2 = all(maps[m][2] >= 0 for m in (0, 1))
    c3 = p_one <= Fraction(1, 20)
    rev = dm < 0 and p_rev <= Fraction(1, 20)
    verdict = "SCREEN-TIER PASS" if (c1 and c2 and c3) else (
        "UNEXPECTED-DIRECTION FINDING" if rev else "NULL")

    # R2-F1: the absolute value's provenance, and the signed reading of PROPOSAL-h's words
    l_ph_defer = loc(PH, "**Verdict criteria [LOCK-h formula], conjunctive", "Ph.defer")
    l_ph_signed = loc(PH, "(max pseudo-Δ across sham and random families)", "Ph.env_signed")
    ph_env_lines = LOCATORS["Ph.env_signed"]["lines"] + [x_ - 1 for x_ in LOCATORS["Ph.env_signed"]["lines"]]
    ph_env_has_abs = any("|" in ph_pin[x_ - 1] for x_ in ph_env_lines)
    ph_env_in_prefix = all(x_ <= n_keep for x_ in ph_env_lines)
    lk_hist = [c_ for c_ in git("log", "--format=%h", PIN, "--", "LOCK-h.md").stdout.decode().split("\n") if c_]
    lk_pseudo = {}
    for c_ in lk_hist:
        t_ = git("show", f"{c_}:LOCK-h.md").stdout.decode("utf-8")
        lk_pseudo[c_] = {"pseudo": len(lines_with(t_, "pseudo")), "abs": lines_with(t_, "|pseudo-Δ|")}
    lk_first_abs = [c_ for c_ in reversed(lk_hist) if lk_pseudo[c_]["abs"]][:1]
    lk_first_abs = lk_first_abs[0] if lk_first_abs else None
    lk_before = [c_ for c_ in reversed(lk_hist) if c_ != lk_first_abs and ancestor(c_, lk_first_abs)] \
        if lk_first_abs else []
    lk_before_none = all(lk_pseudo[c_]["pseudo"] == 0 for c_ in lk_before)
    lk_first_before_an = bool(lk_first_abs) and ancestor(lk_first_abs, "a2f074d") and ancestor("a2f074d", "485cc94")
    env_signed = max(ds, dr)
    c1_signed = dm > env_signed
    OUT[i_abs] = (
        f"The absolute value is LOCK-h v2.0's formula ({L_of('L.envelope')}; first present at "
        f"{lk_first_abs}; lines containing 'pseudo' in the earlier LOCK-h versions: "
        + ", ".join(f"{c_} {lk_pseudo[c_]['pseudo']}" for c_ in lk_before)
        + f"; {lk_first_abs} precedes the analyzer a2f074d and the data 485cc94: "
        f"{lk_first_before_an}, §0), to which PROPOSAL-h defers ('[LOCK-h formula]', {l_ph_defer}); "
        f"PROPOSAL-h's own words at {PH}@{PIN}:{LOCATORS['Ph.criteria']['lines'][0]}-"
        f"{LOCATORS['Ph.env_signed']['lines'][0]} (unchanged since 34eb7ee: {ph_env_in_prefix and ph_prefix_equal}) "
        f"are 'max pseudo-Δ across sham and random families', with no absolute value (a '|' on those "
        f"lines: {ph_env_has_abs}). 'Null on all three conjuncts' holds under the operative lock; read "
        f"literally (signed), PROPOSAL-h's envelope would be max({f4(ds)}, {f4(dr)}) = {f4(env_signed)}, "
        f"Δ_first = {f4(dm)} would exceed it ({c1_signed}) and (i) would pass, while (ii) and (iii) still "
        f"fail ({c2}, {c3}), so the verdict is {verdict} either way.")
    J["envelope_abs_provenance"] = {
        "proposal_h_defer": LOCATORS["Ph.defer"]["lines"], "proposal_h_signed_words": LOCATORS["Ph.env_signed"]["lines"],
        "proposal_h_abs_on_lines": ph_env_has_abs, "lock_h_history": lk_hist, "lock_h_pseudo": lk_pseudo,
        "lock_h_first_abs": lk_first_abs, "lock_h_before_without_pseudo": lk_before_none,
        "first_abs_before_analyzer_and_data": lk_first_before_an,
        "signed_envelope": float(env_signed), "c1_signed": c1_signed,
        "verdict_signed_reading": "SCREEN-TIER PASS" if (c1_signed and c2 and c3) else (
            "UNEXPECTED-DIRECTION FINDING" if rev else "NULL")}

    pr_ = VA["primary"]
    st = {
        "delta": close(pr_["delta_first"]["delta"], float(dm)) and pr_["delta_first"]["k"] == km
                 and pr_["delta_first"]["n"] == nm,
        "sham": pr_["sham"]["k"] == ks and pr_["sham"]["n"] == ns_ and close(pr_["sham"]["delta"], float(ds)),
        "random": pr_["random"]["k"] == kr and pr_["random"]["n"] == nr and close(pr_["random"]["delta"], float(dr)),
        "env": close(pr_["control_envelope"], float(env)),
        "map0": pr_["by_map"]["0"]["k"] == maps[0][0] and pr_["by_map"]["0"]["n"] == maps[0][1],
        "map1": pr_["by_map"]["1"]["k"] == maps[1][0] and pr_["by_map"]["1"]["n"] == maps[1][1],
        "p": close(pr_["p_one_sided"], float(p_one), 1e-12),
        "kcrit": pr_["critical_k"] == kcrit,
        "c": (pr_["conjunct_envelope"], pr_["conjunct_sign_lock"], pr_["conjunct_binomial"]) == (c1, c2, c3),
        "verdict": pr_["verdict"] == verdict,
    }
    P("### 2b. Recomputed from `data/e2b/verdict_campaign.json` (per-read records), compared with `verdict_analysis.json`")
    P("")
    excl_reads_v = sum(len(s["choices"]) for s in S if not s["valid"])
    excl_n_v = sum(1 for s in S if not s["valid"])
    P(f"- Valid sessions: marker {len(valid['marker'])}, sham {len(valid['sham'])}, random "
      f"{len(valid['random'])} (targets 96/36/36); run: marker {V['ran']['marker']}, sham "
      f"{V['ran']['sham']}, random {V['ran']['random']}; reads in the {excl_n_v} excluded "
      f"sessions: {excl_reads_v}.")
    P(f"- Per-session `first_free_pick_pos` agrees with the first read's pick vs the map's "
      f"+tag and with `picked_pole` in {ffp_ok}/{ffp_n} valid sessions; every recorded pick is "
      f"the state-present pick (marker, random) or the vanilla read's pick (sham) in "
      f"{pick_src_ok}/{pick_src_n} reads.")
    P("")
    P("| quantity | recomputed | stored (verdict_analysis.json) | match |")
    P("|---|---|---|---|")
    P(f"| Δ_first, marker | {km}/{nm} → {f4(dm)} ({float(dm):+.10f}) | {pr_['delta_first']['k']}/{pr_['delta_first']['n']} → {pr_['delta_first']['delta']:+.10f} | {st['delta']} |")
    P(f"| pseudo-Δ, sham (no state; nominal +tag) | {ks}/{ns_} → {f4(ds)} | {pr_['sham']['k']}/{pr_['sham']['n']} → {pr_['sham']['delta']:+.4f} | {st['sham']} |")
    P(f"| pseudo-Δ, random (norm-matched random direction) | {kr}/{nr} → {f4(dr)} | {pr_['random']['k']}/{pr_['random']['n']} → {pr_['random']['delta']:+.4f} | {st['random']} |")
    P(f"| realised control envelope max(\\|sham\\|, \\|random\\|) | {float(env):.4f} (from {env_src}) | {pr_['control_envelope']:.4f} | {st['env']} |")
    P(f"| (i) Δ_first > envelope (strict) | {f4(dm)} > {float(env):.4f}: {c1} → {'PASS' if c1 else 'fail'} | conjunct_envelope {pr_['conjunct_envelope']} | {st['c']} |")
    P(f"| (ii) map 0 | {maps[0][0]}/{maps[0][1]} → {f4(maps[0][2])} | {pr_['by_map']['0']['k']}/{pr_['by_map']['0']['n']} → {pr_['by_map']['0']['delta']:+.4f} | {st['map0']} |")
    P(f"| (ii) map 1 | {maps[1][0]}/{maps[1][1]} → {f4(maps[1][2])} | {pr_['by_map']['1']['k']}/{pr_['by_map']['1']['n']} → {pr_['by_map']['1']['delta']:+.4f} | {st['map1']} |")
    P(f"| (ii) sign lock (Δ ≥ 0 in both maps) | {c2} → {'PASS' if c2 else 'fail'} | conjunct_sign_lock {pr_['conjunct_sign_lock']} | {st['c']} |")
    P(f"| (iii) one-sided exact binomial P(X ≥ {km} \\| {nm}, ½) | {float(p_one):.10f} (exact sum of C(96, i)/2^96, i ≥ {km}) | {pr_['p_one_sided']:.10f} | {st['p']} |")
    P(f"| (iii) critical k at α = .05, n = {nm} | {kcrit} (P(X ≥ {kcrit}) = {float(sf_half(kcrit, nm)):.5f}; P(X ≥ {kcrit - 1}) = {float(sf_half(kcrit - 1, nm)):.5f}) | {pr_['critical_k']} | {st['kcrit']} |")
    P(f"| (iii) p ≤ .05 | {c3} → {'PASS' if c3 else 'fail'} | conjunct_binomial {pr_['conjunct_binomial']} | {st['c']} |")
    P(f"| reverse-direction check P(X ≤ {km} \\| {nm}, ½) ≤ .05 (analyzer :230-231) | {float(p_rev):.5f} → {rev} | (not stored) | -- |")
    P(f"| verdict | {verdict} | {pr_['verdict']} | {st['verdict']} |")
    P("")
    J["primary"] = {"marker": [km, nm, float(dm)], "sham": [ks, ns_, float(ds)],
                    "random": [kr, nr, float(dr)], "envelope": float(env), "envelope_from": env_src,
                    "map0": [maps[0][0], maps[0][1], float(maps[0][2])],
                    "map1": [maps[1][0], maps[1][1], float(maps[1][2])],
                    "p_one_sided": float(p_one), "p_reverse": float(p_rev), "critical_k": kcrit,
                    "conjuncts": [c1, c2, c3], "verdict": verdict, "matches_stored": st,
                    "ffp_consistency": [ffp_ok, ffp_n], "pick_source_consistency": [pick_src_ok, pick_src_n]}
    for k_, v_ in st.items():
        if not v_:
            STOPS.append({"subitem": f"primary:{k_}",
                          "discrepancy": "recomputed value differs from verdict_analysis.json"})

    # the record's log for the primary
    l_d = loc(R, "| Δ_first, marker | **−0.0104** (47/96)", "R.delta_row")
    l_i = loc(R, "| (i) exceeds realised envelope | envelope **0.0833**", "R.c1_row")
    l_ii = loc(R, "| (ii) sign locks across maps | map0 −0.0106 (n=47), map1 −0.0102 (n=49)", "R.c2_row")
    l_iii = loc(R, "| (iii) one-sided exact binomial | **p = 0.6202**, critical k ≥ 57", "R.c3_row")
    l_raw = loc("results/raw/2026-08-22_verdict_analysis.txt", "Delta = -0.0104  (47/96)", "raw.delta")
    P(f"Log locators: Δ_first row {l_d}; (i) {l_i}; (ii) {l_ii}; (iii) {l_iii}; analyzer raw {l_raw} "
      "(and the three conjunct lines after it).")
    P("")

    # arm geometry: the choice delivers the state; first read on forced_end
    geo = {}
    for arm in ("marker", "random"):
        ok_first = ok_deliv = ok_sign = n_s = n_r = 0
        for s in valid[arm]:
            ch = s["choices"]
            n_s += 1
            ok_first += int(ch[0]["live_state_at_read"] == s["stratum"]["forced_end"])
            for i in range(len(ch)):
                n_r += 1
                sign = ch[i]["paired_read"]["state_present"]["provenance"]["sign"]
                ok_sign += int((sign == 1) == (ch[i]["live_state_at_read"] == "pos"))
                if i + 1 < len(ch):
                    ok_deliv += int(ch[i + 1]["live_state_at_read"] == ch[i]["picked_pole"])
        geo[arm] = {"first_on_forced_end": [ok_first, n_s], "delivered_by_choice": [ok_deliv, n_s * 5],
                    "provenance_sign_matches_live": [ok_sign, n_r]}
    fe = collections.Counter(s["stratum"]["forced_end"] for s in valid["marker"])
    P(f"Arm geometry (the state at read i+1 is the pole the pick at read i delivered; the first "
      f"read sits on the forced-phase end state): marker first-read-on-forced-end "
      f"{geo['marker']['first_on_forced_end'][0]}/{geo['marker']['first_on_forced_end'][1]}, "
      f"delivered-by-choice {geo['marker']['delivered_by_choice'][0]}/{geo['marker']['delivered_by_choice'][1]}, "
      f"provenance sign = live state {geo['marker']['provenance_sign_matches_live'][0]}/"
      f"{geo['marker']['provenance_sign_matches_live'][1]}; random "
      f"{geo['random']['first_on_forced_end'][0]}/{geo['random']['first_on_forced_end'][1]}, "
      f"{geo['random']['delivered_by_choice'][0]}/{geo['random']['delivered_by_choice'][1]}, "
      f"{geo['random']['provenance_sign_matches_live'][0]}/{geo['random']['provenance_sign_matches_live'][1]}. "
      f"Marker first-read live state (valid sessions): pos {fe['pos']}, neg {fe['neg']}.")
    P("")
    J["arm_geometry"] = geo
    J["marker_forced_end"] = dict(fe)

    # ------------------------------------------------- §2c shadow --
    P("### 2c. The shadow reads: 48/96")
    P("")
    k_sh = sum(1 for s in valid["marker"]
               if s["choices"][0]["paired_read"]["shadow"]["pick"] == s["stratum"]["tag_plus"])
    n_sh = sum(1 for s in valid["marker"] if s["choices"][0]["paired_read"].get("shadow"))
    d_sh = Fraction(k_sh, n_sh) - Fraction(1, 2)
    shs = VA["descriptives"]["shadow_delta_first"]
    sh_ok = shs["k"] == k_sh and shs["n"] == n_sh and close(shs["delta"], float(d_sh))
    # first-read flips
    fr_b = fr_c = 0
    for s in valid["marker"]:
        pr0 = s["choices"][0]["paired_read"]
        if pr0["state_present"]["pick"] != pr0["shadow"]["pick"]:
            if pr0["state_present"]["pick"] == s["stratum"]["tag_plus"]:
                fr_b += 1
            else:
                fr_c += 1
    prefix_ok = sum(1 for s in valid["marker"] for ch in s["choices"]
                    if ch["paired_read"].get("prefix_sha"))
    P(f"- Definition (analyzer :104-118): at the FIRST free read of each valid marker session, the "
      "vanilla state-free `readout.choice_read` forward over the byte-identical prefix that the "
      "state-present read used (one extra forward, `statepresent.py:149-151`); share of those "
      "shadow picks on the map's +tag − ½. This is e2a's insulated design run inside e2b.")
    P(f"- Recomputed: {k_sh}/{n_sh} → {f4(d_sh)}; stored {shs['k']}/{shs['n']} → {shs['delta']:+.4f}; "
      f"match {sh_ok}. Every marker read carries a prefix_sha: {prefix_ok}/{6 * len(valid['marker'])}.")
    P(f"- Why 47 vs 48 (computed-new): at the first read the live state flipped {fr_b + fr_c} of 96 "
      f"picks relative to the shadow, {fr_b} toward the +tag and {fr_c} toward the −tag; "
      f"{k_sh} + {fr_b} − {fr_c} = {k_sh + fr_b - fr_c} = the state-present count {km}.")
    l_sh = loc(R, "give **Δ_first = +0.0000 (48/96)**", "R.shadow")
    P(f"- Log locator: {l_sh}.")
    P("")
    J["shadow"] = {"k": k_sh, "n": n_sh, "delta": float(d_sh), "match": sh_ok,
                   "first_read_flips_b_c": [fr_b, fr_c]}
    if not sh_ok:
        STOPS.append({"subitem": "shadow", "discrepancy": "shadow recount differs from stored"})

    # ------------------------------------------------- §2d envelope reference, MDE --
    P("### 2d. The envelope's planning reference, critical k and MDE (LOCK-h v2.0 §2 constants)")
    P("")
    HP = pinned_json("data/e2b/h1_power.json")
    lv = HP["lockh_v1"]
    E = exact_envelope(36, 36)
    p90 = E["p90"]
    cdf_at_real = E["cdf"].get(env)
    p_ge_real = 1 - (E["cdf"][max(v for v in E["support"] if v < env)] if any(v < env for v in E["support"]) else 0)
    mde_p1, mde_k, mde_i = mde_one_sided(96, 0.05, 0.80)
    env_ok = close(float(p90), lv["envelope_exact"]["p90"], 1e-9) and \
        close(float(E["p50"]), lv["envelope_exact"]["p50"], 1e-9) and \
        close(float(E["p95"]), lv["envelope_exact"]["p95"], 1e-9)
    mde_ok = close(mde_p1 - 0.5, HP["mde_verdict_share"], 1e-12) and mde_k == HP["critical_k"]
    P(f"- Exact null distribution of the envelope (two independent Binomial(36, ½) families, "
      f"max of |k/36 − ½|; exact Fractions): p50 {float(E['p50']):.4f}, p90 {float(p90):.4f} "
      f"(= {p90}), p95 {float(E['p95']):.4f}; stored `h1_power.json` lockh_v1.envelope_exact "
      f"p50/p90/p95 {lv['envelope_exact']['p50']}/{lv['envelope_exact']['p90']}/"
      f"{lv['envelope_exact']['p95']}: match {env_ok}. "
      f"{loc('LOCK-h.md', 'sham and random families; planning reference: p90 = 0.167 from the', 'L.p90')} "
      "quotes p90 = 0.167 as the planning reference.")
    P(f"- The realised envelope {float(env):.4f} = {env} sits at null CDF {float(cdf_at_real):.4f} "
      f"(P(envelope ≥ {float(env):.4f}) = {float(p_ge_real):.4f}) -- i.e. at the null median, "
      "not in its tail (computed-new).")
    P(f"- Critical k (one-sided exact, α = .05, n = 96): {mde_k}; stored `h1_power.json` critical_k "
      f"{HP['critical_k']}. Binomial-only MDE at 80% power (exact power scan over numpy's "
      f"0.0005 grid, index {mde_i}): true share {mde_p1:.6f} → MDE {mde_p1 - 0.5:.6f}; stored "
      f"mde_verdict_share {HP['mde_verdict_share']}: match {mde_ok}. "
      f"{loc('LOCK-h.md', 'MDE 0.130 at 80% power).', 'L.mde')} quotes 'MDE 0.130 at 80% power'.")
    P("")
    J["envelope_reference"] = {"p50": float(E["p50"]), "p90": float(p90), "p95": float(E["p95"]),
                               "cdf_at_realised": float(cdf_at_real), "p_ge_realised": float(p_ge_real),
                               "match_stored": env_ok}
    J["mde_binomial"] = {"k_crit": mde_k, "p1": mde_p1, "mde": mde_p1 - 0.5, "grid_index": mde_i,
                         "match_stored": mde_ok}

    # ------------------------------------------------- §3 leak certification --
    P("## 3. π̂_d = 0.0172 against 0.0735: the leakage certification")
    P("")
    H = pinned_json("data/e2b/h1_sessions.json")
    HG = pinned_json("data/e2b/h1_gate.json")
    HS = H["sessions"]
    N = nd = b = c = 0
    b_field = c_field = 0
    reads_by_session = []
    excl_reads = 0
    for s in HS:
        if s["excluded"]:
            excl_reads += len(s["choices"])
        if s["choices"]:
            reads_by_session.append(len(s["choices"]))
        for ch in s["choices"]:
            pr = ch["paired_read"]
            N += 1
            if pr["state_present"]["pick"] != pr["shadow"]["pick"]:
                nd += 1
                if pr["state_present"]["pick"] == s["stratum"]["tag_plus"]:
                    b += 1
                else:
                    c += 1
            if ch["flipped"]:
                if ch["flip_direction"] == "b":
                    b_field += 1
                else:
                    c_field += 1
    n_valid = sum(1 for s in HS if not s["excluded"])
    excl_phase = collections.Counter((s["exclude_reason"] or "").split("@")[-1].rstrip("0123456789")
                                     for s in HS if s["excluded"])
    last = [s for s in HS if s["choices"]][-1]
    pi = Fraction(nd, N)
    Lh = Fraction(b - c, N)
    p_lo, p_hi = clopper_pearson(b, nd)
    L_lo, L_hi = (2 * p_lo - 1) * float(pi), (2 * p_hi - 1) * float(pi)
    pil, pih = clopper_pearson(nd, N)
    bar = HG["bar_leak"]
    inside = L_lo > -bar and L_hi < bar
    by_cor = float(pi) < bar
    h1_ok = {
        "budget": (H["budget"]["N"], H["budget"]["n_d"], H["budget"]["b"], H["budget"]["c"]) == (N, nd, b, c),
        "fields": (b_field, c_field) == (b, c),
        "gate": (HG["N"], HG["n_d"], HG["b"], HG["c"]) == (N, nd, b, c),
        "pi": close(HG["pi_hat_d"], float(pi), 1e-15),
        "L": close(HG["L_hat"], float(Lh), 1e-15),
        "p_ci": close(HG["p_flip_ci"][0], p_lo, 1e-9) and close(HG["p_flip_ci"][1], p_hi, 1e-9),
        "L_ci": close(HG["L_ci"][0], L_lo, 1e-10) and close(HG["L_ci"][1], L_hi, 1e-10),
        "pi_ci": close(HG["pi_hat_d_ci"][0], pil, 1e-9) and close(HG["pi_hat_d_ci"][1], pih, 1e-9),
        "verdict": HG["verdict"] == ("PASS" if inside else "not PASS"),
        "low_disc": HG["certified_by_low_discordance"] == (inside and by_cor),
    }
    P("### 3a. Recomputed from `data/e2b/h1_sessions.json` (per-read records), compared with `h1_gate.json`")
    P("")
    P(f"- H1 sessions run {len(HS)}, excluded {len(HS) - n_valid} (exclusion phase: "
      f"{dict(excl_phase)}; reads in excluded sessions: {excl_reads}); sessions with reads "
      f"{len(reads_by_session)}; reads per session {dict(collections.Counter(reads_by_session))}; "
      f"stop at session {last['session'] + 1}, read {len(last['choices'])} (1-indexed; "
      f"truncated_by_stop {last.get('truncated_by_stop')}).")
    P("")
    P("| quantity | recomputed | stored | match |")
    P("|---|---|---|---|")
    P(f"| N paired reads | {N} | budget {H['budget']['N']}; gate {HG['N']} | {h1_ok['budget'] and h1_ok['gate']} |")
    P(f"| n_d discordant pairs (state-present pick ≠ shadow pick) | {nd} | {HG['n_d']} | {h1_ok['gate']} |")
    P(f"| b (flip to the map's +tag) / c (to the −tag) | {b} / {c} (per-read `flip_direction`: {b_field} / {c_field}) | {HG['b']} / {HG['c']} | {h1_ok['gate'] and h1_ok['fields']} |")
    P(f"| π̂_d = n_d/N | {nd}/{N} = {float(pi):.7f} → 0.0172 | {HG['pi_hat_d']} | {h1_ok['pi']} |")
    P(f"| π̂_d exact 95% CI (Clopper–Pearson, {nd}/{N}) | [{pil:.4f}, {pih:.4f}] ([{pil:.10f}, {pih:.10f}]) | [{HG['pi_hat_d_ci'][0]:.10f}, {HG['pi_hat_d_ci'][1]:.10f}] | {h1_ok['pi_ci']} |")
    P(f"| L̂ = (b − c)/N | {b - c}/{N} = {float(Lh):+.7f} → +0.00156 | {HG['L_hat']:+.7f} | {h1_ok['L']} |")
    P(f"| exact 95% CI on p_flip = b/n_d = {b}/{nd} | [{p_lo:.4f}, {p_hi:.4f}] | [{HG['p_flip_ci'][0]:.4f}, {HG['p_flip_ci'][1]:.4f}] | {h1_ok['p_ci']} |")
    P(f"| mapped L CI = [(2p_lo − 1)π̂_d, (2p_hi − 1)π̂_d] | [{L_lo:+.5f}, {L_hi:+.5f}] | [{HG['L_ci'][0]:+.5f}, {HG['L_ci'][1]:+.5f}] | {h1_ok['L_ci']} |")
    P(f"| PASS iff mapped CI ⊂ (−{bar}, +{bar}) | {inside} → {'PASS' if inside else 'not PASS'} | {HG['verdict']} | {h1_ok['verdict']} |")
    P(f"| certified by low discordance (π̂_d < bar, so CI ⊂ [−π̂_d, +π̂_d] whatever b/c) | {inside and by_cor} | {HG['certified_by_low_discordance']} | {h1_ok['low_disc']} |")
    P(f"| π̂_d / bar | {pct(float(pi), bar)} (point), {pct(pih, bar)} (upper 95%, unrounded {pih:.6f}); "
      f"{pct(round(pih, 4), bar)} from the rounded 0.0305 | log: 23.4% / 41.5% (from the rounded bound) | -- |")
    P(f"| L̂ / bar | {pct(float(Lh), bar)} | log: 2.1% | -- |")
    P("")
    J["h1"] = {"N": N, "n_d": nd, "b": b, "c": c, "pi_hat_d": float(pi), "pi_ci": [pil, pih],
               "L_hat": float(Lh), "p_flip_ci": [p_lo, p_hi], "L_ci": [L_lo, L_hi], "bar": bar,
               "pass": inside, "low_discordance": inside and by_cor, "matches_stored": h1_ok,
               "sessions_run": len(HS), "sessions_valid": n_valid,
               "reads_per_session": dict(collections.Counter(reads_by_session)),
               "pi_over_bar": float(pi) / bar, "pi_hi_over_bar": pih / bar, "L_over_bar": float(Lh) / bar}
    for k_, v_ in h1_ok.items():
        if not v_:
            STOPS.append({"subitem": f"h1:{k_}", "discrepancy": "recomputed H1 value differs from h1_gate.json"})
    P("Log and lock locators: "
      f"H1 entry {loc(R, 'π̂_d = 0.0172, L̂ = +0.00156; mapped L CI [−0.00915, +0.01143] against a', 'R.h1_vals')}; "
      f"π̂_d CI {loc(R, 'certifies. π̂_d', 'R.h1_ci')}; "
      f"raw {loc('results/raw/2026-08-21_h1_gate_eval.txt', 'N = 640, n_d = 11 (b = 6, c = 5), pi_hat_d = 0.0172', 'raw.h1')}; "
      f"LOCK-h v2.0 §1 {loc('LOCK-h.md', 'π̂_d = 0.0172, exact 95% CI [0.0086, 0.0305]; L̂ = +0.00156;', 'L.h1')}; "
      f"disposition {loc(R, '(PASS by low-discordance certification, π̂_d .0172, CI', 'R.disp_pi')}; "
      f"23.4%/41.5%: 41.5% {loc(R, '0.0735 = 41.5%**, not a fifth.', 'R.ratio')}, the pair "
      f"'23.4% < 25% and 41.5% < 50%' {loc(R, '**23.4% < 25%** and **41.5% < 50%**', 'R.ratio2')}.")
    P("")

    P("### 3b. The certification's definition (code of record, pinned; the H1 runner's lines are "
      "byte-identical at the H1 data commit 7527270, §0)")
    P("")
    P("```")
    for line in (excerpt("scripts/e2b_h1_sessions.py", 171, 174) + ["..."]
                 + excerpt("scripts/e2b_h1_sessions.py", 213, 225) + ["..."]
                 + excerpt("scripts/e2b_h1_gate.py", 97, 100) + ["..."]
                 + excerpt("scripts/e2b_h1_gate.py", 114, 118) + ["..."]
                 + excerpt("scripts/e2b_h1_gate.py", 125, 125)):
        P(line)
    P("```")
    P("")
    P(f"Lock text: unit and flip {loc('LOCK-h.md', 'Unit: a **paired read**', 'L.unit')}; "
      f"L̂ {loc('LOCK-h.md', 'π_d = discordance rate; leak L̂ = (b − c)/N.', 'L.Lhat')}; "
      f"gate {loc('LOCK-h.md', 'the null, mapped through π̂_d = n_d/N. **PASS iff the CI lies', 'L.gate')}; "
      f"feasibility corollary {loc('LOCK-h.md', '**Feasibility corollary, recorded for interpretation:**', 'L.feas')}; "
      f"H1 sessions identical to verdict sessions including steered post-choice rounds (the "
      f"identity clause of the sentence below) "
      f"{loc('LOCK-h.md', '**Clarification (v1.4):** H1 sessions are identical to verdict sessions', 'L.v14')} "
      f"(LOCK-h v1.4, d94e281, an ancestor of the H1 data commit 7527270, §0), restated in "
      f"PROPOSAL-h's appended interpretive note "
      f"{loc('PROPOSAL-h-state-present-choice.md', '**INTERPRETIVE NOTE (2026-08-21, design instance):**', 'Ph.note')} "
      f"(b400083, §0).")
    P("")
    rps = collections.Counter(reads_by_session)
    rps_txt = " + ".join(f"{v_} × {k_}" if v_ > 1 else f"{k_}" for k_, v_ in sorted(rps.items(), reverse=True))
    short = (f"π̂_d = {nd}/{N} = {float(pi):.4f} is the share of H1's {N} paired choice reads "
             f"({len(reads_by_session)} valid sessions, {rps_txt} free reads, the state scheduled "
             "and never selected by the pick) in which injecting the reward axis changed the pick "
             "relative to a vanilla read of the byte-identical prefix -- a pick-discordance rate, "
             "not a logit displacement -- and it certifies the leak because the directional leak "
             f"L = (b − c)/N can be no larger than π̂_d, so the exact 95% interval on L, "
             f"[{L_lo:+.5f}, {L_hi:+.5f}], lies inside the pre-registered ±{bar} whatever the "
             f"direction of the {nd} flips.")
    defn = (f"π̂_d = n_d/N = {nd}/{N} = {float(pi):.4f} is the share of H1's {N} paired choice "
            f"reads (all six free-choice reads of each of the {len(reads_by_session)} valid H1 "
            "sessions pooled, the last cut at the read-level stop N_max = 640; sessions "
            "identical to the verdict tier's except that no pick selects a state "
            f"[{L_of('L.v14')}] -- the state "
            "at each read and in each following round is scheduled, alternating from the "
            "forced-phase end state) in which the live state changed the PICK, i.e. the "
            "state-present read (the reward axis added at L48, frac 0.10, |α| = 10.301) chose "
            "a different label from the vanilla shadow read of the byte-identical prefix -- a "
            "pick-discordance rate, not a logit or probability displacement -- and it certifies "
            "the leak because the directional leak L = (b − c)/N (flips toward the map's +tag "
            "minus flips toward its −tag) cannot exceed the discordance carrying it "
            f"(|L| ≤ π̂_d < {bar}), so the exact Clopper–Pearson 95% interval on b | n_d ~ "
            f"Binomial(n_d, ½), mapped through π̂_d to [{L_lo:+.5f}, {L_hi:+.5f}], lies "
            f"inside ±{bar} whatever the b/c split (certification by low discordance, not a "
            "powered directional test).")
    P("**One sentence, short form (note-ready):** " + short)
    P("")
    P("**One sentence, long form (README; every clause pinned above):** " + defn)
    P("")
    J["certification_definition"] = defn
    J["certification_definition_short"] = short

    # bar derivation
    P("### 3c. Where 0.0735 comes from (LOCK-h v1.1 §2; recomputed in the stdlib)")
    P("")
    v0 = lv["variants"][0]
    env_t = lv["envelope_threshold_used"]
    t1 = conjunctive_power(0.0, v0["k_binom"], env_t)
    mc, mci = mde_conjunctive(v0["k_binom"], env_t)
    lk, lk_r, lki = leak_at_fvr(v0["k_binom"], env_t)
    barv = min(0.5 * mc, lk)
    bar_ok = {"type1": close(t1, v0["power_at_delta_zero"], 1e-12),
              "mde_conj": close(mc, v0["mde_conjunctive"], 1e-9),
              "half": close(0.5 * mc, v0["half_mde"], 1e-9),
              "leak": close(lk, v0["leak_at_false_verdict_rate"], 1e-9),
              "fvr": close(lk_r, v0["false_verdict_rate_at_that_leak"], 1e-12),
              "bar": close(barv, lv["bar_leak"], 1e-9)}
    P(f"- Conjunction power model (h1_power.py :163-184, re-implemented): two maps of 48, "
      f"k_binom = {v0['k_binom']}, envelope conjunct at its exact p90 = {env_t} (Δ must exceed it "
      "strictly), sign lock ≥ 24 per map.")
    P(f"- P(full conjunction fires | Δ = 0) = {t1:.6g} (stored {v0['power_at_delta_zero']:.6g}; "
      f"{loc('LOCK-h.md', 'Type-I of the full verdict conjunction at Δ = 0 is 0.00034', 'L.type1')}).")
    P(f"- Conjunctive MDE at 80% power = {mc:.4f} (grid index {mci}; stored {v0['mde_conjunctive']}); "
      f"0.5 × MDE_conj = {0.5 * mc:.4f} (stored {v0['half_mde']}).")
    P(f"- Largest systematic leak whose false-verdict rate stays ≤ 2.5% = {lk:.4f} (rate there "
      f"{lk_r:.6f}; stored {v0['leak_at_false_verdict_rate']} at {v0['false_verdict_rate_at_that_leak']:.6f}).")
    P(f"- bar_leak = min({0.5 * mc:.4f}, {lk:.4f}) = {barv:.4f}, binding branch: "
      f"{'leak at ≤ 2.5% FVR' if lk < 0.5 * mc else 'half-MDE'} (stored {lv['bar_leak']}; "
      f"{loc('LOCK-h.md', '**bar_leak = 0.0735** (share units).', 'L.bar')}). All match: "
      f"{all(bar_ok.values())} {bar_ok}.")
    P("- What the bar is in words (from h1_power.py :196-205 and LOCK-h :167-178): the largest "
      "systematic shift in the marker family's first-free-choice +tag share that would make the "
      "full verdict conjunction fire on a campaign with no coupling at most 2.5% of the time. It "
      "bounds L (a share shift), not π̂_d; π̂_d < bar certifies only through |L| ≤ π̂_d. Fixed at "
      "LOCK-h v1.1 (8a97513), an ancestor of the H1 data commit 7527270 (§0).")
    P("")
    J["bar_derivation"] = {"type1": t1, "mde_conj": mc, "half_mde": 0.5 * mc, "leak_at_fvr": lk,
                           "fvr_at_leak": lk_r, "bar": barv, "matches_stored": bar_ok}
    for k_, v_ in bar_ok.items():
        if not v_:
            STOPS.append({"subitem": f"bar:{k_}", "discrepancy": "recomputed bar arithmetic differs from h1_power.json"})

    # ------------------------------------------------- §4 leak family (post-hoc) --
    P("## 4. The in-campaign leak and the 'directional-leak family' (descriptive; the family check is post-hoc)")
    P("")

    def halfgap(reads):
        pos = [r["leak"]["d_p_a"] for r in reads if r["leak"]["sign"] == 1]
        neg = [r["leak"]["d_p_a"] for r in reads if r["leak"]["sign"] == -1]
        mp, mn = math.fsum(pos) / len(pos), math.fsum(neg) / len(neg)
        return (mp - mn) / 2.0, (mp + mn) / 2.0, len(pos), len(neg)

    def bc_session(sessions, valid_only=True):
        n_ = d_ = b_ = c_ = 0
        for s in sessions:
            if valid_only and s.get("excluded"):
                continue
            for ch in s["choices"]:
                pr = ch["paired_read"]
                if pr.get("state_present") is None:
                    continue
                n_ += 1
                if pr["state_present"]["pick"] != pr["shadow"]["pick"]:
                    d_ += 1
                    if pr["state_present"]["pick"] == s["stratum"]["tag_plus"]:
                        b_ += 1
                    else:
                        c_ += 1
        return n_, d_, b_, c_

    def mapped(b_, d_, n_):
        if d_ == 0:
            return (0.0, 0.0)
        lo, hi = clopper_pearson(b_, d_)
        p_ = d_ / n_
        return ((2 * lo - 1) * p_, (2 * hi - 1) * p_)

    mk_reads = [ch["paired_read"] for s in valid["marker"] for ch in s["choices"]]
    rd_reads = [ch["paired_read"] for s in valid["random"] for ch in s["choices"]]
    mk_hg = halfgap(mk_reads)
    rd_hg = halfgap(rd_reads)
    mk_bc = bc_session(valid["marker"])
    rd_bc = bc_session(valid["random"])
    ml = VA["descriptives"]["marker_leak"]
    rl = VA["descriptives"]["random_leak"]
    vl_ok = (close(ml["state_reversing_half_gap"], mk_hg[0], 1e-12)
             and close(ml["flip_rate"], mk_bc[1] / mk_bc[0], 1e-15)
             and close(rl["flip_rate"], rd_bc[1] / rd_bc[0], 1e-15)
             and close(rl["state_reversing_half_gap"], rd_hg[0], 1e-12))
    cps = V["checkpoints"]
    P(f"- Verdict tier, marker arm: flip rate {mk_bc[1]}/{mk_bc[0]} = {mk_bc[1] / mk_bc[0]:.4f}; "
      f"state-reversing half-gap of d_p_a = {mk_hg[0]:+.5f} ({pct(mk_hg[0], bar)} of bar; common mode "
      f"{mk_hg[1]:+.5f}); random arm flip rate {rd_bc[1]}/{rd_bc[0]} = {rd_bc[1] / rd_bc[0]:.4f}, "
      f"half-gap {rd_hg[0]:+.5f} (stored in the JSON, not printed in the raw). Match to "
      f"verdict_analysis.json descriptives: {vl_ok}. Log: "
      f"{loc(R, 'rate 0.0191, state-reversing half-gap **+0.00198 = 2.7% of bar_leak**', 'R.v_leak')}.")
    # the monitor's pooling is the runner's, not the lock's: recount from the data which reads
    # the runner's counter admits (it skips reads whose `flipped` is None)
    mon_pool = collections.Counter()
    for s in S:
        for ch in s["choices"]:
            if ch["flipped"] is not None:
                mon_pool[s["arm"]] += 1
    mon_pool_ok = (sum(mon_pool.values()) == V["n_paired_reads"]
                   and mon_pool.get("sham", 0) == 0)
    VR = "scripts/e2b_verdict_campaign.py"
    vr485 = git("show", f"485cc94:{VR}").stdout.decode()
    _mon_needles = ('n_pr = n_d = 0', 'if ch["flipped"] is None:', 'n_pr += 1', 'while n_pr >= next_cp:')
    mon_l485 = [lines_with(vr485, n_) for n_ in _mon_needles]
    mon_lpin = [lines_with(pinned_text(VR), n_) for n_ in _mon_needles]
    _fmt_l = lambda ls: ",".join(str(x[0]) if len(x) == 1 else "?" + str(x) for x in ls)
    lock_mon_text = pinned_text("LOCK-h.md").split("\n")
    _lm = lines_with(pinned_text("LOCK-h.md"), "**In-campaign leak monitor (declared):**")
    lock_mon_block = " ".join(lock_mon_text[_lm[0] - 1:_lm[0] + 5]) if _lm else ""
    lock_states_pool = any(w_ in lock_mon_block.lower() for w_ in ("pool", "random", "marker"))
    P(f"- Verdict tier, in-campaign monitor (declared at "
      f"{loc('LOCK-h.md', '**In-campaign leak monitor (declared):**', 'L.monitor')}; it counts the "
      f"marker and random arms' paired reads pooled, next point): "
      f"{len(cps)} checkpoints, π̂_d " + " → ".join(f"{cp['pi_hat_d']:.4f}" for cp in cps)
      + f"; max |L̂| {max(abs(cp['L_hat']) for cp in cps):.4f} vs pause threshold bar/2 = "
      f"{bar / 2:.5f} (LOCK-h prints 0.0368); any pause {any(cp['pause'] or cp['stability_pause'] for cp in cps)}; "
      f"campaign totals n_d {V['n_d']} (b {V['b']}, c {V['c']}) over {V['n_paired_reads']} paired reads "
      f"(recount: marker {mk_bc[1]} = {mk_bc[2]}+{mk_bc[3]}, random {rd_bc[1]} = {rd_bc[2]}+{rd_bc[3]}).")
    P(f"- The pooling is the runner's implementation, not the lock's text. The declaration's six "
      f"lines name no arm (any of the words 'pool'/'random'/'marker' present: {lock_states_pool}). "
      f"The runner's counter admits every read whose `flipped` is not None: "
      f"scripts/e2b_verdict_campaign.py@485cc94:{_fmt_l(mon_l485)} "
      f"(scripts/e2b_verdict_campaign.py@{PIN}:{_fmt_l(mon_lpin)}). Data recount of the reads it "
      f"admits: {dict(mon_pool)} = {sum(mon_pool.values())} vs stored n_paired_reads "
      f"{V['n_paired_reads']}, sham 0: {mon_pool_ok}. Code's reading: sham reads carry no "
      "state-present half, so they are not paired reads, and pooling the two state-bearing arms "
      "is the plain reading of the lock's '128-paired-read checkpoint'.")
    P("")
    def menu_share(sessions, valid_only=True):
        k_ = n_ = 0
        for s in sessions:
            if valid_only and (s.get("excluded") or s.get("valid") is False):
                continue
            for ch in s["choices"]:
                n_ += 1
                k_ += int(ch["menu_a"] == s["stratum"]["tag_plus"])
        return k_, n_
    msh = {"H1": menu_share(HS), "H1-u": menu_share(pinned_json("data/e2b/h1u_sessions.json")["sessions"]),
           "H2": menu_share(pinned_json("data/e2b/h2_sessions.json")["sessions"]),
           "verdict marker": menu_share(valid["marker"]), "verdict random": menu_share(valid["random"])}
    J["menu_a_is_plus_tag"] = {k: list(v) for k, v in msh.items()}
    J["monitor_pool"] = {"admitted_by_arm": dict(mon_pool), "total": sum(mon_pool.values()),
                         "stored_n_paired_reads": V["n_paired_reads"], "ok": mon_pool_ok,
                         "runner_lines_485cc94": mon_l485, "runner_lines_pin": mon_lpin,
                         "lock_declaration_names_arms": lock_states_pool}
    se2a = pinned_text("valence_core/session_e2a.py")
    mt_block = se2a[se2a.index("MENU_TEMPLATES = ("):se2a.index(")", se2a.index("Config choice (one word):\",\n)", se2a.index("MENU_TEMPLATES = (")) + 30)]
    n_ab = mt_block.count("{a}, {b}")
    J["menu_templates_a_first"] = n_ab
    P(f"- The four menu templates ({loc('valence_core/session_e2a.py', 'MENU_TEMPLATES = (', 'SE2A.menu')}) "
      f"list `{{a}}, {{b}}` in that order: {n_ab}/4; `label_a` = `a` is therefore the first-listed label. "
      f"At the H1 and verdict data commits the tuple lived in `valence_core/e2b/session.py` "
      f"(7527270:{mt['7527270'][1]}, 485cc94:{mt['485cc94'][1]}) and is identical: {mt_equal}; the H1 "
      "runner lines cited below are byte-identical at 7527270 (§0).")
    P("- Menu order in the data (share of reads whose first-listed label is the map's +tag): "
      + "; ".join(f"{k} {a}/{n_} = {a / n_:.3f}" for k, (a, n_) in msh.items())
      + ". Code: H1 `scripts/e2b_h1_sessions.py`@bbc9ffe:210-211; verdict runner "
      f"{loc(VR, 'a, b = ((tag_plus, tag_minus) if rng.integers(2) == 0', 'VR.menu')} "
      f"(at the campaign commit 485cc94: {VR}:{','.join(map(str, lines_with(vr485, 'a, b = ((tag_plus, tag_minus) if rng.integers(2) == 0')))}); "
      f"sham rounds and reads carry no injection: {loc(VR, 'injs = [] if inj is None else [inj[pole]]', 'VR.sham_forced')}, "
      f"{loc(VR, '# sham: no state anywhere, so the untouched state-free primitive.', 'VR.sham_read')}, "
      f"{loc(VR, 'injs = [] if inj is None else [inj[picked_pole]]', 'VR.sham_round')} "
      f"(485cc94: {','.join(str(lines_with(vr485, n_)[0]) for n_ in ('injs = [] if inj is None else [inj[pole]]', '# sham: no state anywhere, so the untouched state-free primitive.', 'injs = [] if inj is None else [inj[picked_pole]]'))}; "
      "the runner was edited after the campaign by the consolidation and adjudication commits; these lines are in both).")
    P("")
    P("**Two different quantities are in the record's 'directional-leak family'.** "
      "`records.py:150-174` defines the per-pair leak as `d_p_a` = state-present minus shadow "
      "renormalised probability of `label_a`, and `label_a` is the FIRST-LISTED menu label "
      "(menu order is randomised per read in H1, H2 and the verdict tier: "
      "`e2b_h1_sessions.py:210-215`; in the read-half precursor it is a fixed tag of the pair). "
      "The 'state-reversing half-gap' (`records.py:209-213`) is therefore a push toward the "
      "first-listed label that reverses with the injected sign -- it is not a push toward the "
      "+tag. The gate's L̂ = (b − c)/N (LOCK-h §3) is the +tag-directional pick shift, the "
      "quantity bar_leak bounds. The record's five members mix the two (post-hoc check, "
      "computed-new; nothing here changes a label):")
    P("")
    H1U = pinned_json("data/e2b/h1u_sessions.json")
    H2 = pinned_json("data/e2b/h2_sessions.json")
    RS = pinned_json("data/e2b/h2_read_stability.json")
    rows = []
    # read half
    rs_hg = halfgap(RS["per_read"])
    SHORT = {"read-half precursor (archived e2a prefixes, prism/slate)": "read half",
             "H2 proper (state through rounds and reads)": "H2 proper",
             "H1-u (unsteered post-choice rounds; descriptive only)": "H1-u",
             "H1 gate run of record": "H1", "verdict tier, marker arm": "verdict marker"}
    rows.append(("read-half precursor (archived e2a prefixes, prism/slate)", "+0.00084",
                 "half-gap", rs_hg[0], len(RS["per_read"]),
                 sum(int(r["leak"]["flipped"]) for r in RS["per_read"]), None, None,
                 "data/e2b/h2_read_stability.json per_read"))
    h2_reads = [ch["paired_read"] for s in H2["sessions"] if not s["excluded"] for ch in s["choices"]]
    h2_hg = halfgap(h2_reads)
    h2_bc = bc_session(H2["sessions"])
    rows.append(("H2 proper (state through rounds and reads)", "+0.00220", "half-gap", h2_hg[0],
                 h2_bc[0], h2_bc[1], h2_bc[2], h2_bc[3], "data/e2b/h2_sessions.json sessions"))
    h1u_reads = [ch["paired_read"] for s in H1U["sessions"] for ch in s["choices"]]
    h1u_hg = halfgap(h1u_reads)
    h1u_bc = bc_session(H1U["sessions"])
    rows.append(("H1-u (unsteered post-choice rounds; descriptive only)", "0.00000", "L̂ = (b−c)/N",
                 h1u_hg[0], h1u_bc[0], h1u_bc[1], h1u_bc[2], h1u_bc[3], "data/e2b/h1u_sessions.json sessions"))
    h1_reads = [ch["paired_read"] for s in HS for ch in s["choices"]]
    h1_hg = halfgap(h1_reads)
    rows.append(("H1 gate run of record", "+0.00156", "L̂ = (b−c)/N", h1_hg[0], N, nd, b, c,
                 "data/e2b/h1_sessions.json sessions"))
    rows.append(("verdict tier, marker arm", "+0.00198", "half-gap", mk_hg[0], mk_bc[0], mk_bc[1],
                 mk_bc[2], mk_bc[3], "data/e2b/verdict_campaign.json sessions"))
    P("| campaign | value in the family | which quantity it is | half-gap of d_p_a (recomputed) | N | n_d | b / c | L̂ = (b−c)/N (recomputed) | gate-form mapped CI on L | \\|half-gap\\|/bar | \\|L̂\\|/bar |")
    P("|---|---|---|---|---|---|---|---|---|---|---|")
    fam = []
    for (name, val, which, hgv, n_, d_, b_, c_, src) in rows:
        if b_ is None:
            lstr, cistr, lpct = "n/a (no +tag per read in the artifact)", "n/a", "n/a"
            lval = None
        else:
            lval = (b_ - c_) / n_
            ci = mapped(b_, d_, n_)
            lstr = f"{b_ - c_}/{n_} = {lval:+.5f}"
            cistr = f"[{ci[0]:+.4f}, {ci[1]:+.4f}]"
            lpct = pct(abs(lval), bar)
        P(f"| {name} | {val} | {which} | {hgv:+.5f} | {n_} | {d_} | "
          f"{'n/a' if b_ is None else f'{b_} / {c_}'} | {lstr} | {cistr} | {pct(abs(hgv), bar)} | {lpct} |")
        fam.append({"campaign": SHORT[name], "family_value": val, "quantity": which, "half_gap": hgv,
                    "N": n_, "n_d": d_, "b": b_, "c": c_, "L_hat": lval, "source": src})
    P("")
    stored_ok = (close(RS["leak_summary"]["state_reversing_half_gap"], rs_hg[0], 1e-12)
                 and close(H2["summary"]["leak_summary"]["state_reversing_half_gap"], h2_hg[0], 1e-12)
                 and (H1U["budget"]["b"], H1U["budget"]["c"], H1U["budget"]["N"]) == (h1u_bc[2], h1u_bc[3], h1u_bc[0]))
    P(f"- Each family value reproduces from its artifact under the quantity named in column 3 "
      f"(stored-field cross-check: {stored_ok}). Log locators: LOCK-h v2.0 §1 "
      f"{loc('LOCK-h.md', 'measurements: +0.00084 / +0.00220 / 0.00000 / +0.00156 — never above', 'L.family')}; "
      f"verdict entry {loc(R, 'members across every configuration tested — +0.00084, +0.00220, 0.00000,', 'R.family')}; "
      f"H1 entry {loc(R, 'now been measured four times — read half +0.00084, H2 +0.00220, H1-u', 'R.family4')}; "
      f"FINDINGS-5 {loc('FINDINGS-5.md', 'directional-leak (L) family — a distinct quantity from the discordance', 'F5.family')}; "
      f"the values-check that calls all five 'L (half-gap) values' "
      f"{loc(R, '**+0.00084, +0.00220, 0.00000, +0.00156, +0.00198** — all L (half-gap)', 'R.family_desc')}.")
    max_hg = max(abs(r["half_gap"]) for r in fam)
    max_L = max(abs(r["L_hat"]) for r in fam if r["L_hat"] is not None)
    _hga = max(fam, key=lambda r: abs(r["half_gap"]))["campaign"]  # short label
    _La = max((r for r in fam if r["L_hat"] is not None), key=lambda r: abs(r["L_hat"]))
    P(f"- Under the half-gap applied to all five, the maximum |half-gap| is {max_hg:.5f} "
      f"({pct(max_hg, bar)} of bar, {_hga}); under L̂ applied to the four where it is computable, "
      f"the maximum |L̂| is {max_L:.5f} ({pct(max_L, bar)} of bar, {_La['campaign']}, n_d = {_La['n_d']}: "
      f"b {_La['b']} / c {_La['c']}). The record's '≤ 3% of the bar' holds for the mixed list "
      "as printed and for neither quantity applied uniformly. Every gate-form mapped CI above "
      "lies inside ±0.0735, so the certification by low discordance holds for every "
      "campaign; what does not hold uniformly is the '≤ 3%' characterisation.")
    P("")
    J["leak_family"] = fam
    J["leak_family_max"] = {"half_gap": max_hg, "L_hat": max_L}
    J["verdict_leak"] = {"marker_half_gap": mk_hg[0], "marker_common": mk_hg[1],
                         "marker_flip": [mk_bc[1], mk_bc[0]], "marker_b_c": [mk_bc[2], mk_bc[3]],
                         "random_half_gap": rd_hg[0], "random_flip": [rd_bc[1], rd_bc[0]],
                         "random_b_c": [rd_bc[2], rd_bc[3]], "match_stored": vl_ok,
                         "checkpoints_pi": [cp["pi_hat_d"] for cp in cps],
                         "max_abs_L_checkpoint": max(abs(cp["L_hat"]) for cp in cps)}
    hg_arg = max(fam, key=lambda r: abs(r["half_gap"]))
    L_arg = max((r for r in fam if r["L_hat"] is not None), key=lambda r: abs(r["L_hat"]))
    J["leak_family_max"].update({"half_gap_campaign": hg_arg["campaign"], "L_campaign": L_arg["campaign"]})
    NOTES.append("Leak family: the five-member 'directional-leak (L) family' (LOCK-h v2.0 §1, the "
                 "verdict entry, FINDINGS-5 §3) mixes the d_p_a state-reversing half-gap (read half, "
                 "H2, verdict) with L̂ = (b−c)/N (H1-u, H1); "
                 f"{L_of('R.family_desc')} calls all five "
                 f"'L (half-gap)'. Uniformly: half-gap max {hg_arg['half_gap']:+.5f} "
                 f"({pct(abs(hg_arg['half_gap']), bar)} of bar, {hg_arg['campaign']}); |L̂| max "
                 f"{abs(L_arg['L_hat']):.5f} ({pct(abs(L_arg['L_hat']), bar)} of bar, {L_arg['campaign']}, "
                 f"n_d = {L_arg['n_d']}). All gate-form CIs inside ±{bar}. Post-hoc; "
                 "a wording note for the note's O-leakage sentence, not a STOP.")

    # ------------------------------------------------- §5 quarantine --
    P("## 5. The quarantined primitive: name, and what 'quarantined' enforces (ledger 5(e))")
    P("")
    l_5e = loc("CLAUDE.md", "(e) [h-amendment, PROPOSAL-h §0.4, design-instance authored, applied", "C.5e")
    l_name = loc("valence_core/e2b/statepresent.py", "def choice_read_statepresent(adapter", "SP.def")
    P(f"- **Name:** `choice_read_statepresent` in `valence_core/e2b/statepresent.py` ({l_name}); "
      f"rule 5(e) text {l_5e} (to :278); PROPOSAL-h §0.1 "
      f"{loc('PROPOSAL-h-state-present-choice.md', '`choice_read_statepresent` is a distinct function in the e2b', 'Ph.name')}. "
      "Its insulated sibling, never modified, is `readout.choice_read` "
      f"({loc('valence_core/readout.py', 'def choice_read(adapter', 'RO.def')}).")
    P("")
    P("What the code enforces, clause by clause (pinned file:line; the lines are excerpted after the table):")
    P("")
    SP = "valence_core/e2b/statepresent.py"
    RC = "valence_core/e2b/records.py"
    AN = "valence_core/regression/analysis.py"
    enf = [
        ("import guard: the first non-import-machinery frame must be a file inside `valence_core/e2b/` or a file whose basename matches `e2b_*.py`; otherwise ImportError before any adapter/readout import executes",
         f"{loc(SP, 'def _importer_is_sanctioned', 'SP.guard')}; "
         f"{loc(SP, 'return base.startswith(\"e2b_\") and base.endswith(\".py\")', 'SP.basename')}; "
         f"{loc(SP, 'if not _importer_is_sanctioned():', 'SP.raise')}; "
         f"{loc(SP, 'from ..adapters.base import Injection, ModelAdapter', 'SP.late_import')}"),
        ("not re-exported: `from valence_core.e2b import *` yields only the inert records names",
         f"{loc('valence_core/e2b/__init__.py', 'from .records import (InjectionProvenance', 'I.export')}; "
         f"{loc('valence_core/e2b/__init__.py', '__all__ = [', 'I.all')}"),
        ("per-read injection provenance: only a declared `Injection` (built via `Injection.at_frac`, rule 1) is accepted; 7 fields required; null dose and bad sign refused; validated at record construction",
         f"{loc(SP, 'if not isinstance(injection, Injection):', 'SP.inj')}; "
         f"{loc(RC, 'if inj.frac is None or inj.r_layer is None:', 'RC.atfrac')}; "
         f"{loc(RC, 'REQUIRED_PROVENANCE = (', 'RC.req')}; "
         f"{loc(RC, 'if float(d[\"frac\"]) <= 0 or float(d[\"alpha\"]) == 0:', 'RC.null')}; "
         f"{loc(RC, '        assert_provenance_complete(self.provenance)', 'RC.post', 1)}"),
        ("paired shadow reads: the function returns a `PairedRead` or nothing; the shadow is `readout.choice_read` itself over the identical text; a pair without a shadow, or with a 'shadow' carrying provenance, cannot be constructed",
         f"{loc(SP, 'res = adapter.forward(ids, capture_layers=(), injections=[injection])', 'SP.fwd')}; "
         f"{loc(SP, 'shadow = choice_read(adapter, transcript_text, label_a, label_b,', 'SP.shadow')}; "
         f"{loc(SP, 'return PairedRead(state_present=sp, shadow=shadow,', 'SP.ret')}; "
         f"{loc(RC, 'if self.shadow is None:', 'RC.noshadow')}; "
         f"{loc(RC, 'if getattr(self.shadow, \"provenance\", None) is not None:', 'RC.steered')}"),
        ("the insulated primitive is never modified: `choice_read` takes no injection-shaped parameter and its forward passes none",
         f"{loc('valence_core/readout.py', 'res = adapter.forward(ids, capture_layers=())', 'RO.fwd')}; "
         f"{loc(RC, 'def assert_choice_read_uninjectable', 'RC.unin')}"),
        ("suite (every run): importing the primitive from the suite raises; no `.py` under `valence_core/` outside `e2b/` and `regression/` names it; `choice_read` still cannot inject and its signature has not grown",
         f"{loc(AN, 'def check_e2b_quarantine', 'AN.def')}; "
         f"{loc(AN, 'lambda: importlib.import_module(\"valence_core.e2b.statepresent\"),', 'AN.import')}; "
         f"{loc(AN, 'if \"choice_read_statepresent\" in fh.read():', 'AN.scan')}; "
         f"{loc(AN, 'got, ok = _raises(assert_choice_read_uninjectable, AssertionError)', 'AN.unin')}; "
         f"{loc(AN, 'checks += check_e2b_quarantine()', 'AN.reg')}"),
        ("the other direction -- insulated harnesses refuse to run with the primitive loaded (`assert_modules_absent` / `assert_statepresent_absent`)",
         f"{loc('valence_core/session.py', 'def assert_modules_absent', 'SE.def')}; "
         f"{loc('valence_core/e2d/runner.py', 'FORBIDDEN_MODULES = (\"valence_core.e2b.statepresent\",)', 'E2D.forb')}; "
         f"{loc('valence_core/e2d/runner.py', 'assert_modules_absent(FORBIDDEN_MODULES)', 'E2D.call', 2)}; "
         f"{loc('valence_core/echo/maskedprefix.py', 'FORBIDDEN_MODULES = (\"valence_core.e2b.statepresent\",)', 'MP.forb')}; "
         f"{loc('valence_core/echo/maskedprefix.py', 'def assert_statepresent_absent', 'MP.def')}"),
        ("NOT enforced in code: clause 4, 'leakage-budget gate has passed' -- a campaign precondition carried by commit order (§0: 7527270 → f030cdd → 485cc94); the verdict runner never reads h1_gate.json",
         f"{loc(SP, 'leakage-budget gate passed    -> H1; a campaign precondition, not a code', 'SP.clause4')}; "
         f"`h1_gate` occurrences in scripts/e2b_verdict_campaign.py at 485cc94: "
         f"{git('show', '485cc94:scripts/e2b_verdict_campaign.py').stdout.decode().count('h1_gate')}, at {PIN}: "
         f"{pinned_text('scripts/e2b_verdict_campaign.py').count('h1_gate')}"),
    ]
    P("| clause | pinned locators |")
    P("|---|---|")
    for a_, b_ in enf:
        P(f"| {cell(a_)} | {cell(b_)} |")
    P("")
    P("```")
    for (p_, a_, b_) in [(SP, 53, 89), (SP, 127, 155), (RC, 59, 60), (RC, 129, 139), (RC, 229, 238),
                         ("valence_core/readout.py", 90, 93), ("valence_core/readout.py", 106, 107),
                         (AN, 795, 837)]:
        for line in excerpt(p_, a_, b_):
            P(line)
        P("...")
    P("```")
    P("")

    # live checks (model-free)
    sys.path.insert(0, REPO)
    import_msg = None
    try:
        importlib.import_module(QUARANTINED)
        import_res = "IMPORTED (guard did not fire)"
    except ImportError as e:
        import_res = "ImportError"
        import_msg = str(e)[:150]
    absent_after = QUARANTINED not in sys.modules
    from valence_core.e2b import records as _records  # inert half only
    from valence_core import readout as _readout
    try:
        _records.assert_choice_read_uninjectable()
        unin = "accepted"
    except AssertionError as e:
        unin = f"AssertionError: {e}"
    sig = list(inspect.signature(_readout.choice_read).parameters)
    absent_end = QUARANTINED not in sys.modules
    # structural scan at the pin
    tree = git("ls-tree", "-r", "--name-only", PIN).stdout.decode().split("\n")
    core_py = [p for p in tree if p.startswith("valence_core/") and p.endswith(".py")]
    offenders, scope_n = [], 0
    for p in core_py:
        parts = p.split("/")[:-1]
        if os.path.basename("/".join(parts)) in ("e2b", "regression"):
            continue
        scope_n += 1
        if "choice_read_statepresent" in pinned_text(p):
            offenders.append(p)
    other = [p for p in tree if p.endswith(".py") and not p.startswith("valence_core/")
             and p.split("/")[0] != "jlens-qwen36" and "choice_read_statepresent" in pinned_text(p)]
    importers = [p for p in tree if p.endswith(".py")
                 and "from valence_core.e2b.statepresent import" in pinned_text(p)]
    # provenance completeness on the artifacts, with the record's own validator
    prov_checked = prov_bad = shadow_bad = 0
    for sess, arms_ok in ((V["sessions"], ("marker", "random")), (HS, None)):
        for s in sess:
            if arms_ok is not None and s["arm"] not in arms_ok:
                continue
            for ch in s["choices"]:
                pr = ch["paired_read"]
                prov_checked += 1
                try:
                    _records.assert_provenance_complete(pr["state_present"]["provenance"])
                except ValueError:
                    prov_bad += 1
                sh = pr.get("shadow")
                if not sh or "provenance" in sh or not pr.get("prefix_sha"):
                    shadow_bad += 1
    sham_reads = [ch["paired_read"] for s in V["sessions"] if s["arm"] == "sham" for ch in s["choices"]]
    sham_ok = sum(1 for pr in sham_reads if pr.get("state_present") is None and pr.get("shadow")
                  and "provenance" not in pr["shadow"])
    provs = collections.defaultdict(set)
    for s in V["sessions"]:
        if s["arm"] == "sham":
            continue
        for ch in s["choices"]:
            p_ = ch["paired_read"]["state_present"]["provenance"]
            provs[s["arm"]].add((p_["axis"], p_["layer"], p_["frac"], round(abs(p_["alpha"]), 6),
                                 p_["r_layer"], p_["direction_sha"]))
    absent_markers = ("FORBIDDEN_MODULES", "assert_modules_absent", "assert_statepresent_absent",
                      "not in sys.modules", "not in _sys.modules")
    absence_files = []
    for p in tree:
        if not p.endswith(".py") or p.startswith("valence_core/e2b/") or p.startswith("valence_core/regression/") \
                or p.startswith("scripts/audit_note_") or p.startswith("scripts/e2b_"):
            continue
        t_ = pinned_text(p)
        if (("valence_core.e2b.statepresent" in t_ or "valence_core.e2b\" + \".statepresent" in t_
             or "\"valence_core.e2b.\" + \"statepresent\"" in t_)
                and any(m_ in t_ for m_ in absent_markers)):
            absence_files.append(p)
    J["absence_asserting_files"] = absence_files
    # R2-F5: split the 14 by where the absence check runs (AST at the pin): a runtime assertion
    # (any absence call/compare outside a function named *selftest*) vs a self-test check only.
    _ASSERT_FNS = {"assert_modules_absent", "assert_statepresent_absent", "assert_insulated"}

    def _absence_kinds(src_: str) -> dict:
        tr = ast.parse(src_)
        par: dict = {}
        for nd in ast.walk(tr):
            for ch_ in ast.iter_child_nodes(nd):
                par[ch_] = nd
        mod_names = {t_.id for nd in ast.walk(tr) if isinstance(nd, ast.Assign)
                     and "statepresent" in (ast.get_source_segment(src_, nd.value) or "")
                     for t_ in nd.targets if isinstance(t_, ast.Name)}

        def _stmt_src(nd):
            while nd in par and not isinstance(nd, ast.stmt):
                nd = par[nd]
            return ast.get_source_segment(src_, nd) or ""

        def _fns(nd):
            out_ = []
            while nd in par:
                nd = par[nd]
                if isinstance(nd, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    out_.append(nd.name)
            return out_
        hits = []
        for nd in ast.walk(tr):
            is_abs = False
            if isinstance(nd, ast.Call):
                f_ = nd.func
                nm = f_.id if isinstance(f_, ast.Name) else (f_.attr if isinstance(f_, ast.Attribute) else None)
                is_abs = nm in _ASSERT_FNS
            elif isinstance(nd, ast.Compare) and any(isinstance(o_, ast.NotIn) for o_ in nd.ops):
                cmp_ = nd.comparators[-1]
                if (isinstance(cmp_, ast.Attribute) and cmp_.attr == "modules"
                        and isinstance(cmp_.value, ast.Name) and cmp_.value.id in ("sys", "_sys")):
                    ss = _stmt_src(nd)
                    is_abs = ("statepresent" in ss or "FORBIDDEN_MODULES" in ss
                              or any(isinstance(x_, ast.Name) and x_.id in mod_names for x_ in ast.walk(nd.left)))
            if is_abs:
                fn_ = _fns(nd)
                hits.append({"line": nd.lineno, "functions": fn_,
                             "selftest": any("selftest" in f_ for f_ in fn_)})
        rt = sorted({h_["line"] for h_ in hits if not h_["selftest"]})
        stl = sorted({h_["line"] for h_ in hits if h_["selftest"]})
        return {"runtime_lines": rt, "selftest_lines": stl, "hits": hits,
                "kind": "runtime" if rt else ("self-test only" if stl else "none found")}
    absence_split = {p: _absence_kinds(pinned_text(p)) for p in absence_files}
    abs_runtime = [p for p in absence_files if absence_split[p]["kind"] == "runtime"]
    abs_selftest = [p for p in absence_files if absence_split[p]["kind"] == "self-test only"]
    abs_none = [p for p in absence_files if absence_split[p]["kind"] == "none found"]
    named_no_marker = []
    for p in tree:
        if not p.endswith(".py") or p.startswith("valence_core/e2b/") or p.startswith("valence_core/regression/") \
                or p.startswith("scripts/audit_note_") or p.startswith("scripts/e2b_") or p in absence_files:
            continue
        t_ = pinned_text(p)
        if ("valence_core.e2b.statepresent" in t_ or "valence_core.e2b\" + \".statepresent" in t_
                or "\"valence_core.e2b.\" + \"statepresent\"" in t_):
            named_no_marker.append(p)
    J["absence_split"] = {"by_file": absence_split, "runtime": abs_runtime, "selftest_only": abs_selftest,
                          "none_found": abs_none, "named_without_marker": named_no_marker}
    P("Live checks (model-free; this run):")
    P("")
    P(f"- `importlib.import_module('{QUARANTINED}')` from this script: **{import_res}** "
      f"(message begins: \"{import_msg}\"); absent from sys.modules after the attempt: "
      f"{absent_after}; still absent at the end of the checks: {absent_end}.")
    P(f"- `records.assert_choice_read_uninjectable()`: {unin}; `readout.choice_read` parameters: {sig}.")
    P(f"- Structural scan at the pin: {scope_n} `.py` files under `valence_core/` outside `e2b/` and "
      f"`regression/`; offenders naming the primitive: {len(offenders)} {offenders}. Files outside "
      f"`valence_core/` naming it: {other}; of those, module-level importers: {importers} "
      "(the four sanctioned `scripts/e2b_*.py` runners).")
    P(f"- Tracked `.py` files at the pin (outside `valence_core/e2b/`, `regression/`, the e2b runners and "
      f"these audit scripts) that name the quarantined module beside an absence assertion: "
      f"{len(absence_files)} {absence_files}. This is a string-marker heuristic (the file names the "
      "module and carries one of the markers " + ", ".join(f"`{m_}`" for m_ in absent_markers) + "). "
      f"Split by where the check runs (AST at the pin; a call to "
      + "/".join(f"`{f_}`" for f_ in sorted(_ASSERT_FNS)) + " or a `not in sys.modules` naming the "
      "module, inside or outside a function named `*selftest*`): runtime assertion (startup, before a "
      f"read, or in a read path) {len(abs_runtime)} {abs_runtime}; self-test check only "
      f"{len(abs_selftest)} {abs_selftest}" + (f"; neither found {len(abs_none)} {abs_none}" if abs_none else "")
      + ". Runtime lines per file: " + "; ".join(f"{p_.split('/')[-1]} :{','.join(map(str, absence_split[p_]['runtime_lines']))}"
                                                 for p_ in abs_runtime)
      + ". Self-test lines: " + "; ".join(f"{p_.split('/')[-1]} :{','.join(map(str, absence_split[p_]['selftest_lines']))}"
                                         for p_ in abs_selftest)
      + f". Files that name the module but carry no marker (excluded by the heuristic): {named_no_marker}.")
    P(f"- Every state-present read in `verdict_campaign.json` (marker + random, all sessions) and "
      f"`h1_sessions.json` passes the record's own `assert_provenance_complete`: {prov_checked - prov_bad}"
      f"/{prov_checked}; every one has a provenance-free shadow and a prefix_sha: "
      f"{prov_checked - shadow_bad}/{prov_checked}. Sham reads: {sham_ok}/{len(sham_reads)} carry "
      "no state-present half (they go through the untouched `choice_read`).")
    P(f"- Provenance sets in the verdict campaign (axis, layer, frac, |α|, R_48, direction sha16): "
      f"marker {sorted(provs['marker'])}; random {sorted(provs['random'])} -- the random family is "
      "norm-matched (same layer, frac, |α|) on a different direction.")
    P("")
    J["quarantine"] = {"name": "choice_read_statepresent", "module": SP,
                       "import_from_unsanctioned": import_res, "absent_after": absent_after,
                       "absent_end": absent_end, "uninjectable": unin, "choice_read_params": sig,
                       "scan_scope": scope_n, "offenders": offenders, "named_outside_core": other,
                       "importers": importers, "provenance_checked": prov_checked,
                       "provenance_bad": prov_bad, "shadow_bad": shadow_bad,
                       "sham_ok": [sham_ok, len(sham_reads)],
                       "provenance_sets": {k: sorted(map(list, v)) for k, v in provs.items()}}
    P("What 'quarantined' does not mean (the record's own words and Code's reading of the guard):")
    P("")
    P(f"- The guard is declared not a security boundary "
      f"({loc(SP, 'It is not a security boundary and is not claimed as one', 'SP.honest')}): anything "
      "that can import a sanctioned runner inherits the capability. The structural suite checks "
      "are the stated guarantee.")
    P(f"- The guard sanctions by basename, not by directory: the prose says `scripts/e2b_*.py` "
      f"({loc(SP, 'package, and `scripts/e2b_*.py` runners). It stops the accident it is meant', 'SP.prose')}), "
      f"the code accepts any file named `e2b_*.py` in any directory ({LOCATORS['SP.basename']['path']}"
      f"@{PIN}:{','.join(map(str, LOCATORS['SP.basename']['lines']))}). Code reading only; not exercised "
      "here (writing an `e2b_*.py` file to load the capability would be an unlicensed import).")
    # the sanctioned direction: explicit check logged at the consolidation; implicit in every
    # campaign run (each runner imports the primitive at module level at its data commit)
    camp_runs = [("read half", "data/e2b/h2_read_stability.json", "scripts/e2b_h2_readstability.py"),
                 ("H2 proper", "data/e2b/h2_sessions.json", "scripts/e2b_h2_sessions.py"),
                 ("H1-u", "data/e2b/h1u_sessions.json", "scripts/e2b_h1_sessions.py"),
                 ("H1", "data/e2b/h1_sessions.json", "scripts/e2b_h1_sessions.py"),
                 ("verdict", "data/e2b/verdict_campaign.json", "scripts/e2b_verdict_campaign.py")]
    camp_imports = []
    for name_, art_, runner_ in camp_runs:
        hist_ = [x for x in git("log", "--format=%h", PIN, "--", art_).stdout.decode().split("\n") if x]
        per_c = {}
        for c0 in hist_:
            rtext = git("show", f"{c0}:{runner_}", check=False).stdout.decode()
            per_c[c0] = [i + 1 for i, l_ in enumerate(rtext.split("\n"))
                         if l_.startswith("from valence_core.e2b.statepresent import")]
        camp_imports.append({"campaign": name_, "artifact": art_, "commits": hist_,
                             "runner": runner_, "module_level_import_lines": per_c,
                             "ok": bool(per_c) and all(per_c.values())})
    camp_all_import = all(ci_["ok"] for ci_ in camp_imports)
    _ci_txt = lambda ci_: f"{ci_['campaign']} {ci_['runner']} " + ", ".join(
        f"@{c_}:{','.join(map(str, v_)) or 'NONE'}" for c_, v_ in ci_["module_level_import_lines"].items())
    J["sanctioned_direction_campaigns"] = camp_imports
    l_consol = loc("results/raw/2026-08-22_consolidation.txt",
                   "-- sanctioned scripts/e2b_*.py runners (module-level statepresent import):", "raw.consol")
    l_consol_tab = loc(R, "| sanctioned `scripts/e2b_*.py` runners still import it | 4/4 clean |", "R.consol_tab")
    l_consol_hdr = loc(R, "CONSOLIDATION ACCEPTANCE EVENT: GREEN.", "R.consol_hdr")
    P(f"- The suite pins only the refusal direction "
      f"({LOCATORS['AN.import']['path']}@{PIN}:{','.join(map(str, LOCATORS['AN.import']['lines']))}). The "
      "sanctioned direction (the runners import cleanly) is checked explicitly at the 2026-08-22 "
      f"consolidation: raw {l_consol} and its RESULTS entry ({l_consol_hdr}; the row at {l_consol_tab}), "
      "both log-only. It was also exercised implicitly by every e2b campaign run: each campaign's "
      "runner imports the primitive at module level at every commit in its artifact's history at "
      "the pin (newest first: "
      + "; ".join(_ci_txt(ci_) for ci_ in camp_imports)
      + f"; all five: {camp_all_import}), so a run that wrote state-present reads had loaded it "
      "through a sanctioned runner (inference from the import lines and the artifacts' provenance, "
      f"§5 live checks; the runs' stdout is not re-read here). The 2026-08-20 entry's \"Both "
      f"directions are suite-pinned\" ({loc(R, 'Both directions are', 'R.both', 1)}) is not borne out "
      "by the suite: `valence_core/regression/analysis.py` at 6897b67 and at the pin carries only "
      "the refusal check (read-only grep at both commits, next point; no `scripts/e2b_*.py` runner "
      "existed at 6897b67).")
    P("")
    an_6897 = git("show", "6897b67:valence_core/regression/analysis.py").stdout.decode()
    _body = lambda t: t.split("def check_e2b_quarantine")[1].split("\ndef ")[0]
    _probe = ("scripts/e2b", "subprocess", "e2b_h1", "e2b_verdict")
    J["suite_directions_6897b67_sanctioned"] = any(t in _body(an_6897) for t in _probe)
    J["suite_directions"] = {
        "refusal_at_pin": "importlib.import_module(\"valence_core.e2b.statepresent\")" in pinned_text(AN),
        "sanctioned_direction_at_pin": any(t in pinned_text(AN).split("def check_e2b_quarantine")[1].split("\ndef ")[0]
                                           for t in ("scripts/e2b", "subprocess", "e2b_h1", "e2b_verdict")),
        "refusal_at_6897b67": "importlib.import_module(\"valence_core.e2b.statepresent\")" in an_6897,
    }
    runners_6897 = [p_ for p_ in git("ls-tree", "-r", "--name-only", "6897b67").stdout.decode().split("\n")
                    if p_.startswith("scripts/e2b_") and p_.endswith(".py")]
    suite_files_6897 = [p_ for p_ in git("ls-tree", "-r", "--name-only", "6897b67").stdout.decode().split("\n")
                        if p_.startswith("valence_core/regression/") and p_.endswith(".py")]
    suite_naming_6897 = [p_ for p_ in suite_files_6897
                         if "statepresent" in git("show", f"6897b67:{p_}").stdout.decode()]
    J["suite_directions"]["scripts_e2b_at_6897b67"] = runners_6897
    J["suite_directions"]["suite_files_naming_statepresent_6897b67"] = suite_naming_6897
    P(f"- Grep result behind the last point: refusal check in `check_e2b_quarantine` at the pin "
      f"{J['suite_directions']['refusal_at_pin']}, at 6897b67 {J['suite_directions']['refusal_at_6897b67']}; "
      f"any sanctioned-direction probe (strings {list(_probe)}) in its body at the pin "
      f"{J['suite_directions']['sanctioned_direction_at_pin']}, at 6897b67 "
      f"{J['suite_directions_6897b67_sanctioned']}; suite files at 6897b67 naming `statepresent` at "
      f"all: {suite_naming_6897} (of {suite_files_6897}); `scripts/e2b_*.py` files at 6897b67: "
      f"{runners_6897}.")
    P("")
    NOTES.append("Quarantine: the guard admits any importer file named e2b_*.py in any directory "
                 "(statepresent.py:75-76) where its prose says scripts/e2b_*.py (:24-25); the suite pins "
                 "only the refusal direction; the sanctioned direction was checked explicitly at the "
                 f"2026-08-22 consolidation (raw {L_of('raw.consol')}; {L_of('R.consol_tab')}; log-only) "
                 "and exercised implicitly by every e2b campaign run (each runner imports the primitive "
                 "at module level at its data commit). The 2026-08-20 claim 'both directions are "
                 "suite-pinned' is not borne out by the suite. Clause 4 (gate passed) is commit order, "
                 "not code. None is a STOP; the README can say exactly this.")

    # ------------------------------------------------- §6 preprint --
    P("## 6. The preprint's two e2b sentences ("
      + (f"patch-{PREPRINT_PATCH} text of record, untracked)" if pre_match else
         f"working-tree copy, untracked, sha256 {pre_sha[:8]}...{pre_sha[-5:]}: MISMATCH vs the "
         f"patch-{PREPRINT_PATCH} text of record)"))
    P("")
    l111 = loc(PREPRINT, PRE111_NEEDLE, "PRE.111", text=pre_text, tag="wt")
    l176 = loc(PREPRINT, "Δ_first = −0.0104 (47/96; shadow passes 48/96 exactly)", "PRE.176",
               text=pre_text, tag="wt")
    # Round 9: the audited text's locators, as this item's committed raw recorded them (read-only git).
    raw_js = json.loads(git("show", f"{RAW_COMMIT}:{DEF_JSON}").stdout.decode("utf-8"))
    raw_md = git("show", f"{RAW_COMMIT}:{DEF_OUT}").stdout.decode("utf-8")
    aud_loc = {k_: raw_js["locators"][k_]["lines"] for k_ in ("PRE.111", "PRE.176")}
    aud_short = f"{PREPRINT_AUDITED_SHA[:8]}...{PREPRINT_AUDITED_SHA[-5:]}"
    rec_short = f"{PREPRINT_SHA[:8]}...{PREPRINT_SHA[-5:]}"
    pre_lines = pre_text.split("\n")
    q176 = "Δ_first = −0.0104 (47/96; shadow passes 48/96 exactly), null on all three conjuncts"
    # written only on a MATCH (the §0 gate refuses any other text), so 'patched' names the text of record
    J["preprint"]["reanchored"] = {
        "PRE.176": {"audited_lines": aud_loc["PRE.176"], "patched_lines": LOCATORS["PRE.176"]["lines"],
                    "quoted_phrase_in_patched_line": LOCATORS["PRE.176"]["ok"]
                    and q176 in pre_lines[LOCATORS["PRE.176"]["lines"][0] - 1]}}
    P(f"- {l176}: \"Δ_first = −0.0104 (47/96; shadow passes 48/96 exactly), null on all three "
      "conjuncts\" -- every number reproduces (§2b, §2c); 'null on all three conjuncts' holds under "
      "the operative LOCK-h v2.0 envelope (|·|), and under PROPOSAL-h's literal signed wording (i) "
      f"would pass ({c1_signed}) while the verdict stays {verdict} (§2a).")
    assert pre111_patched == (pre_match and LOCATORS["PRE.111"]["lines"] == [])   # same test as §0
    l111_wt = l111
    if pre111_patched:   # the audited sentence, located as the committed raw located it
        l111 = (f"{PREPRINT}:" + ",".join(map(str, aud_loc["PRE.111"]))
                + f" (audited text {aud_short}, superseded; locator from {DEF_JSON}@{RAW_COMMIT})")
        LOCATORS["PRE.111"]["note"] = (f"the audited text's needle, absent from the patch-{PREPRINT_PATCH} text of record: "
                                       "a finding on the patch (§6; /preprint/patch_findings), not a "
                                       "locator defect; the sentence re-anchors as PRE.111.v6")
    P(f"- {l111}: the numbers reproduce (π̂_d = 0.0172, bar 0.0735), but the gloss \"a "
      "pre-registered bound on the direct displacement of label logits by the vector\" is not "
      "what the record measures: π̂_d is a pick-discordance rate (state-present pick ≠ shadow "
      "pick over the same prefix), and the pre-registered bound (0.0735) is on the +tag-"
      "directional leak L, which π̂_d bounds through |L| ≤ π̂_d. The probability displacement "
      "(`d_p_a`, `d_label_mass`) is recorded per read but is descriptive, not the certified "
      "quantity. Replace the gloss with §3b's short form"
      + (" (patch v6 rewrites this sentence: the finding on the patch below; whether the rewrite "
         "discharges this is the design seat's and N1's call)" if pre111_patched else "")
      + ". A definition error, not a transcription of a number.")
    PATCH_F: list[dict] = []
    if pre111_patched:   # round 9: the failed check is a finding on the patch (ruling 9), not a STOP
        n_old = aud_loc["PRE.111"][0]
        l111v6 = loc(PREPRINT, "π̂_d = 0.0172 (11 of 640 paired reads)", "PRE.111.v6", text=pre_text, tag="wt")
        new_ln = LOCATORS["PRE.111.v6"]["lines"]
        new_line = pre_lines[new_ln[0] - 1] if len(new_ln) == 1 else None
        gloss = "a pre-registered bound on the direct displacement of label logits by the vector"
        prov = {"raw_audited_sha_match": raw_js["preprint"]["sha256"] == PREPRINT_AUDITED_SHA
                and raw_js["preprint"]["match"] is True,
                "raw_needle_in_old_line": raw_js["locators"]["PRE.111"]["needle"] in PRE111_AUDITED,
                "raw_md_gloss_in_old_line": f"the gloss \"{gloss}\"" in raw_md and gloss in PRE111_AUDITED}
        arch = os.path.join(REPO, PREPRINT_AUDITED_ARCHIVE)
        if os.path.exists(arch):   # optional; never required
            with open(arch, "rb") as fh:
                arch_b = fh.read()
            prov["archive_sha_match"] = sha256_bytes(arch_b) == PREPRINT_AUDITED_SHA
            prov["archive_line_equal"] = (prov["archive_sha_match"] and
                                          arch_b.decode("utf-8").split("\n")[n_old - 1] == PRE111_AUDITED)
        else:
            prov["archive_sha_match"] = prov["archive_line_equal"] = "not checked (archived copy absent)"
        chk = None
        pi_in = -bar < pil and pih < bar
        cp_level = round(100 * inspect.signature(clopper_pearson).parameters["conf"].default)
        if new_line is not None:
            nums_ = lambda s_: list(dict.fromkeys(re.findall(r"\d+(?:\.\d+)?", s_)))
            new_nums = [x_ for x_ in nums_(new_line) if x_ not in nums_(PRE111_AUDITED)]
            ph_in = f"exact 95% interval lies inside the pre-registered ±{bar}"
            ph_van = "a vanilla read of the byte-identical prefix"
            chk = {"π̂_d = 0.0172 equals the reproduced value": f"π̂_d = {float(pi):.4f}" in new_line,
                   "'11 of 640 paired reads' equals n_d/N": f"({nd} of {N} paired reads)" in new_line,
                   "'±0.0735' equals the bar": f"±{bar}" in new_line,
                   f"phrase '{ph_in}' present": ph_in in new_line,
                   f"computed: the mapped exact 95% CI on L, [{L_lo:+.5f}, {L_hi:+.5f}], inside ±{bar}": inside,
                   f"computed: π̂_d's exact 95% CI, [{pil:.4f}, {pih:.4f}], inside ±{bar} ('whose' may "
                   "attach to the rate rather than to L)": pi_in,
                   "phrase 'bounds the directional leak' present": "bounds the directional leak" in new_line,
                   f"computed: |L̂| = {abs(float(Lh)):.5f} ≤ π̂_d = {float(pi):.4f}": abs(Lh) <= pi,
                   f"phrase '{ph_van}' present, as in §3b's short form": ph_van in new_line and ph_van in short,
                   "'pick-discordance rate' present": "pick-discordance rate" in new_line,
                   "the logit-displacement gloss absent": "displacement of label logits" not in new_line,
                   f"numbers new to the line {new_nums} are n_d = {nd}, N = {N} and the exact interval's "
                   f"level {cp_level} (Clopper–Pearson conf default)": new_nums == [str(nd), str(N), str(cp_level)]}
        PATCH_F.append({"check": "PRE.111", "needle": LOCATORS["PRE.111"]["needle"],
                        "routing": f"a finding on the patch for the design seat ({FINDING_RULING}); not a STOP",
                        "old": {"sha256": PREPRINT_AUDITED_SHA, "line": n_old, "text": PRE111_AUDITED},
                        "new": {"sha256": pre_sha, "locator": l111v6, "text": new_line},
                        "old_line_provenance": prov, "new_line_checks": chk})
        P(f"- **Finding on the patch** ({FINDING_RULING}; for the design seat; not a STOP): the audited "
          f":{n_old} needle \"{LOCATORS['PRE.111']['needle']}\" is not found in the patched text "
          f"({l111_wt}): patch v6 rewrote the sentence, which re-anchors at {l111v6} "
          f"(same line, new sentence). Old (audited text, sha256 {aud_short}, :{n_old}): "
          f"\"{PRE111_AUDITED}\" New (patched text, sha256 {pre_sha[:8]}...{pre_sha[-5:]}, :{','.join(map(str, new_ln))}): "
          f"\"{new_line}\" The new sentence against this run's reproduced values (§3a): "
          + ("; ".join(f"{k_}: {v_}" for k_, v_ in chk.items()) if chk else "not checked (no unique re-anchor)")
          + ((". Either reading of 'whose' (the directional leak L, as §3b's short form has it, or the rate "
              "π̂_d) is true by the computed intervals; every number new to the line is a reproduced one"
              if all(chk.values()) else ". At least one check above is False: the sentence is not "
              "fully supported by this run's values") if chk else "")
          + f". Old line's provenance: {DEF_JSON}@{RAW_COMMIT} records the audited sha with MATCH "
          f"({prov['raw_audited_sha_match']}) and this needle at :{n_old} (needle in the old line: "
          f"{prov['raw_needle_in_old_line']}); {DEF_OUT}@{RAW_COMMIT} quotes the gloss (in the old line: "
          f"{prov['raw_md_gloss_in_old_line']}); byte-equal to :{n_old} of the archived copy: "
          f"{prov['archive_line_equal']}. The Figures row for the gloss is the audited text's and keeps its "
          "status, carried unchanged; whether the patched sentence discharges it is the design seat's and "
          "N1's call.")
    J["preprint"]["patch_findings"] = PATCH_F
    # Round 10 (2026-10-12): every check above ran on the patch-v7 text of record. Each finding on the patch
    # this item's round-9 raw records, disposed on v7; every check that passed on v6 and fails on v7; a screen
    # of the lines v7 changes. A failed check is a finding on the patch (ruling 9's routing), never a STOP.
    r9_js = json.loads(git("show", f"{R9_COMMIT}:{DEF_JSON}").stdout.decode("utf-8"))
    r9_pre = r9_js["preprint"]
    v6_short = f"{PREPRINT_V6_SHA[:8]}...{PREPRINT_V6_SHA[-5:]}"
    r10_prov = {"r9_raw_records_v6_as_of_record": r9_pre["sha256"] == PREPRINT_V6_SHA
                and r9_pre["match"] is True and r9_pre["of_record_sha256"] == PREPRINT_V6_SHA}
    v6_lines = None
    arch6 = os.path.join(REPO, PREPRINT_V6_ARCHIVE)
    if os.path.exists(arch6):   # optional; never required
        with open(arch6, "rb") as fh:
            arch6_b = fh.read()
        r10_prov["archive_sha_match"] = sha256_bytes(arch6_b) == PREPRINT_V6_SHA
        if r10_prov["archive_sha_match"]:
            v6_lines = arch6_b.decode("utf-8").split("\n")
    else:
        r10_prov["archive_sha_match"] = "not checked (archived copy absent)"
    nc = "not checked (archived patch-v6 copy absent or not matching)"
    DISP: list[dict] = []
    for f9 in r9_pre["patch_findings"]:
        k9, k9r = f9["check"], f9["check"] + ".v6"   # the audited needle; the patch-v6 sentence's re-anchor
        v6_txt, v6_ln = f9["new"]["text"], r9_js["locators"][k9r]["lines"]
        v7_ln = LOCATORS[k9r]["lines"] if k9r in LOCATORS else []
        if len(v7_ln) == 1:
            v7_at, v7_from = v7_ln[0], f"the re-anchor {k9r} on v7"
        elif len(v6_ln) == 1 and v6_ln[0] <= len(pre_lines):   # re-anchor fails: quote v7 at v6's position
            v7_at, v7_from = v6_ln[0], f"the round-9 raw's v6 line position (the re-anchor {k9r} matches {v7_ln} on v7)"
        else:
            v7_at, v7_from = None, f"none (the re-anchor {k9r} matches {v7_ln} on v7; no round-9 position)"
        v7_txt = pre_lines[v7_at - 1] if v7_at else None
        chk9 = f9["new_line_checks"] or {}
        chk10 = next((p_["new_line_checks"] for p_ in PATCH_F if p_["check"] == k9), None) or {}
        # The audited needle found again on v7 is the discrepant audited sentence back, not the finding resolved:
        # the finding's resolution is the design seat's and N1's call, as round 9 recorded.
        aud_found = bool(LOCATORS[k9]["lines"])
        disp = ("reverted to the audited sentence" if aud_found
                else ("unchanged" if v7_txt == v6_txt else "changed"))
        d_ = {"check": k9, "disposition": disp,
              "audited_needle_found_on_v7": aud_found,
              "v6": {"sha256": f9["new"]["sha256"], "lines": v6_ln, "raw": f"{DEF_JSON}@{R9_COMMIT}"},
              "v7": {"sha256": pre_sha, "lines": v7_ln, "quoted_line": v7_at, "quoted_line_from": v7_from},
              "v7_line_equal_to_v6_text_in_r9_raw": v7_txt == v6_txt,
              "v6_text_in_r9_raw_equal_to_archived_v6_line": (v6_lines[v6_ln[0] - 1] == v6_txt
                                                             if v6_lines is not None and len(v6_ln) == 1 else nc),
              "new_line_checks_on_v7_all_true": bool(chk10) and all(v_ is True for v_ in chk10.values()),
              "new_line_checks_same_as_r9": chk10 == chk9,
              "new_line_checks_true_on_v6_not_true_on_v7": [k_ for k_, v_ in chk9.items()
                                                            if v_ is True and chk10.get(k_) is not True]}
        if disp != "unchanged":   # quote v6 and v7
            d_["v6_text"], d_["v7_text"] = v6_txt, v7_txt
        DISP.append(d_)
    # every round-9 check of a preprint sentence, v6 (the raw @R9_COMMIT) against v7 (this run)
    REG: list[str] = []
    for k_, v_ in r9_js["locators"].items():
        if k_.startswith("PRE.") and v_["ok"] is True and not LOCATORS.get(k_, {}).get("ok"):
            REG.append(f"locator {k_} (\"{v_['needle']}\") matched {v_['expect']} line(s) on v6 and "
                       f"{LOCATORS.get(k_, {}).get('lines')} on v7")
    if (r9_pre["reanchored"]["PRE.176"]["quoted_phrase_in_patched_line"] is True
            and J["preprint"]["reanchored"]["PRE.176"]["quoted_phrase_in_patched_line"] is not True):
        REG.append(f"PRE.176: the quoted phrase \"{q176}\" is in the v6 line, not in the v7 line")
    for d_ in DISP:
        REG += [f"{d_['check']}.v6 new-line check \"{k_}\": True on v6, not True on v7"
                for k_ in d_["new_line_checks_true_on_v6_not_true_on_v7"]]
    read_v7 = sorted(set(LOCATORS["PRE.176"]["lines"]) | set(LOCATORS.get("PRE.111.v6", {}).get("lines", []))
                     | set(LOCATORS["PRE.111"]["lines"]) | {d_["v7"]["quoted_line"] for d_ in DISP
                                                           if d_["v7"]["quoted_line"]})
    # the lines this item read on v6, as the round-9 raw located them
    read_v6 = sorted({x_ for k_, v_ in r9_js["locators"].items() if k_.startswith("PRE.") for x_ in v_["lines"]})

    def touched(line: str, lo: int, hi: int) -> list[str]:
        # scope terms with an occurrence overlapping [lo, hi), or split by an insertion at lo when lo == hi
        out = []
        for t_ in SCOPE_TERMS:
            k_ = line.find(t_)
            while k_ != -1:
                if (k_ < lo < k_ + len(t_)) if lo == hi else (k_ < hi and k_ + len(t_) > lo):
                    out.append(t_)
                    break
                k_ = line.find(t_, k_ + 1)
        return out

    SCREEN: list[dict] | str = nc
    if v6_lines is not None:
        SCREEN = []
        for tag_, i1, i2, j1, j2 in difflib.SequenceMatcher(a=v6_lines, b=pre_lines, autojunk=False).get_opcodes():
            if tag_ == "equal":
                continue
            if tag_ == "delete" or (i2 - i1) != (j2 - j1):   # whole lines on each side
                a_, b_ = "\n".join(v6_lines[i1:i2]), "\n".join(pre_lines[j1:j2])
                SCREEN.append({"v6_lines": list(range(i1 + 1, i2 + 1)), "v7_lines": list(range(j1 + 1, j2 + 1)),
                               "kind": tag_, "read_by_this_item": any(j1 < x_ <= j2 for x_ in read_v7),
                               "read_by_this_item_on_v6": any(i1 < x_ <= i2 for x_ in read_v6),
                               "scope_terms_in_changed_text": [t_ for t_ in SCOPE_TERMS if t_ in b_],
                               "scope_terms_in_v6_text_changed": [t_ for t_ in SCOPE_TERMS if t_ in a_],
                               "scope_terms_fewer_on_v7": [t_ for t_ in SCOPE_TERMS if b_.count(t_) < a_.count(t_)]})
                continue
            for o_ in range(j2 - j1):   # 1:1 replacement: screen the text the change touches on each side
                a_, b_ = v6_lines[i1 + o_], pre_lines[j1 + o_]
                p_ = len(os.path.commonprefix([a_, b_]))
                s_ = len(os.path.commonprefix([a_[p_:][::-1], b_[p_:][::-1]]))
                t7, t6 = touched(b_, p_, len(b_) - s_), touched(a_, p_, len(a_) - s_)
                SCREEN.append({"v6_lines": [i1 + o_ + 1], "v7_lines": [j1 + o_ + 1], "kind": tag_,
                               "read_by_this_item": (j1 + o_ + 1) in read_v7,
                               "read_by_this_item_on_v6": (i1 + o_ + 1) in read_v6,
                               "scope_terms_in_changed_text": t7,
                               "scope_terms_in_v6_text_changed": t6,
                               "scope_terms_fewer_on_v7": [t_ for t_ in SCOPE_TERMS if b_.count(t_) < a_.count(t_)],
                               # descriptive only: terms in the line's text carried from v6, outside the change
                               "scope_terms_in_text_carried_from_v6": [t_ for t_ in SCOPE_TERMS if t_ in
                                                                       b_[:p_] + "\n" + b_[len(b_) - s_:]]})
    NEWF: list[dict] = [{"finding": r_, "kind": "a check that passed on v6 fails on v7"} for r_ in REG]
    if isinstance(SCREEN, list):
        NEWF += [{"finding": f"v7 changes v6 :{','.join(map(str, c_['v6_lines'])) or '-'} to v7 "
                             f":{','.join(map(str, c_['v7_lines'])) or '- (deleted)'}"
                             + (", a line this item reads on v7" if c_["read_by_this_item"] else "")
                             + (", a line this item read on v6" if c_["read_by_this_item_on_v6"] else "")
                             + (f", in text carrying this item's scope terms on v7 {c_['scope_terms_in_changed_text']}"
                                if c_["scope_terms_in_changed_text"] else "")
                             + (f", in v6 text it changes carrying this item's scope terms "
                                f"{c_['scope_terms_in_v6_text_changed']} (fewer on v7: {c_['scope_terms_fewer_on_v7']})"
                                if c_["scope_terms_in_v6_text_changed"] else "")
                             + "; not verified against this item's record sources by this screen",
                  "kind": "a v7 change in this item's scope"}
                 for c_ in SCREEN if c_["read_by_this_item"] or c_["read_by_this_item_on_v6"]
                 or c_["scope_terms_in_changed_text"] or c_["scope_terms_in_v6_text_changed"]]
    for f_ in NEWF:
        f_["routing"] = f"a finding on the patch for the design seat ({FINDING_RULING}); not a STOP"
    J["preprint"]["round10"] = {"of_record": {"sha256": PREPRINT_SHA, "patch": PREPRINT_PATCH,
                                              "ruling": PREPRINT_RULING},
                                "round9_of_record": {"sha256": PREPRINT_V6_SHA, "archive": PREPRINT_V6_ARCHIVE,
                                                     "required": False, "raw": f"{DEF_JSON}@{R9_COMMIT}"},
                                "provenance": r10_prov, "lines_read_on_v7": read_v7,
                                "lines_read_on_v6": read_v6,
                                "dispositions": DISP, "checks_true_on_v6_failing_on_v7": REG,
                                "v7_changes_screen": {"scope_terms": list(SCOPE_TERMS), "changes": SCREEN},
                                "new_findings": NEWF}
    ch_v7 = (sorted({x_ for c_ in SCREEN for x_ in c_["v7_lines"]}) if isinstance(SCREEN, list) else None)
    ch_v6 = (sorted({x_ for c_ in SCREEN for x_ in c_["v6_lines"]}) if isinstance(SCREEN, list) else None)
    r10_carried = bool(DISP) and all(d_["disposition"] == "unchanged" for d_ in DISP)
    P(f"- **Round 10** (patch {PREPRINT_PATCH}, sha256 {rec_short}, {PREPRINT_RULING}; round 9's text of "
      f"record was the patch-v6 text {v6_short}, which {DEF_JSON}@{R9_COMMIT} records as of record with "
      f"MATCH: {r10_prov['r9_raw_records_v6_as_of_record']}; archived copy {PREPRINT_V6_ARCHIVE}, sha256 "
      f"match: {r10_prov['archive_sha_match']}): every check of a preprint sentence above ran on the v7 "
      "text. Round 9's findings on the patch, disposed on v7: "
      + ("; ".join(
          f"{d_['check']}: {d_['disposition']} -- the audited needle found on v7: "
          f"{d_['audited_needle_found_on_v7']}; v7 :{d_['v7']['quoted_line']}"
          + ("" if d_["v7"]["lines"] == [d_["v7"]["quoted_line"]] else f" ({d_['v7']['quoted_line_from']})")
          + f" byte-equal to "
          f"the patch-v6 sentence the round-9 raw records at :{','.join(map(str, d_['v6']['lines']))}: "
          f"{d_['v7_line_equal_to_v6_text_in_r9_raw']} (that text byte-equal to the archived copy's line: "
          f"{d_['v6_text_in_r9_raw_equal_to_archived_v6_line']}); its new-line checks above all True on v7: "
          f"{d_['new_line_checks_on_v7_all_true']}, the same as round 9's: {d_['new_line_checks_same_as_r9']}"
          + (f"; v6: \"{d_['v6_text']}\" v7: \"{d_['v7_text']}\"" if d_["disposition"] != "unchanged" else "")
          for d_ in DISP) if DISP else "none recorded")
      + ". Checks that passed on v6 and fail on v7: " + ("; ".join(REG) if REG else "none")
      + ". Lines v7 changes against the patch-v6 text: "
      + (("none" if not ch_v7 else ":" + ", :".join(map(str, ch_v7)))
         + " (v6 lines: " + ("none" if not ch_v6 else ":" + ", :".join(map(str, ch_v6))) + ")"
         + f"; lines this item reads on v7 (:{', :'.join(map(str, read_v7))}) among them: "
         + (", ".join(f":{x_}" for x_ in read_v7 if x_ in ch_v7) or "none")
         + f"; lines it read on v6 per the round-9 raw (:{', :'.join(map(str, read_v6))}) among the v6 lines: "
         + (", ".join(f":{x_}" for x_ in read_v6 if x_ in ch_v6) or "none")
         + f"; this item's scope terms in the text v7 changes, v7 side: "
         + (", ".join(f":{','.join(map(str, c_['v7_lines']))} {c_['scope_terms_in_changed_text']}"
                      for c_ in SCREEN if c_["scope_terms_in_changed_text"]) or "none")
         + "; v6 side: "
         + (", ".join(f"v6 :{','.join(map(str, c_['v6_lines']))} {c_['scope_terms_in_v6_text_changed']}"
                      for c_ in SCREEN if c_["scope_terms_in_v6_text_changed"]) or "none")
         + " (descriptive: in text the changed lines carry from v6 unchanged, "
         + (", ".join(f":{','.join(map(str, c_['v7_lines']))} {c_['scope_terms_in_text_carried_from_v6']}"
                      for c_ in SCREEN if c_.get("scope_terms_in_text_carried_from_v6")) or "none") + ")"
         if ch_v7 is not None else nc)
      + ". New findings on the patch: "
      + ("; ".join(f"{f_['finding']} ({f_['routing']})" for f_ in NEWF) if NEWF else "none")
      + (". Round 9's finding stands on v7 as recorded above; the Figures row for the gloss keeps its "
         "status, carried unchanged." if r10_carried else "."))
    P("")
    NOTES.append("Preprint :111 " + (f"(the audited text, sha256 {aud_short}) " if pre111_patched else "")
                 + "glosses π̂_d as 'a pre-registered bound on the direct displacement of "
                 "label logits'; the record's π̂_d is a pick-discordance rate and the bar bounds L. Numbers "
                 "reproduce; the gloss is the discrepancy (definition, not transcription)."
                 + (" Patch v6 rewrites the line: a finding on the patch (§6)." if pre111_patched else ""))

    # ------------------------------------------------- figures --
    P("## Figures (as the block writes them)")
    P("")
    VC = "data/e2b/verdict_campaign.json"
    fig("e2b VERDICTS entry (Code locates and pins)",
        f"verdict {L_of('R.verdict_entry')}; disposition {L_of('R.disposition')}; H1 gate {L_of('R.h1_entry')}",
        "RESULTS.md (Phase-2 log)", "log-only",
        "entry prose; every figure in it that the block names is reproduced from JSON in the rows below")
    fig("Δ_first = −0.0104 (47/96)", f"{km}/{nm} → {f4(dm)}",
        f"{VC} sessions (valid marker, first read pick vs stratum.tag_plus); data/e2b/verdict_analysis.json primary.delta_first",
        "reproduced" if st["delta"] else "discrepant",
        f"log {L_of('R.delta_row')}; share of first free picks to the map's +tag − ½")
    fig("shadow 48/96", f"{k_sh}/{n_sh} → {f4(d_sh)}",
        f"{VC} choices[0].paired_read.shadow.pick; verdict_analysis.json descriptives.shadow_delta_first",
        "reproduced" if sh_ok else "discrepant",
        f"vanilla choice_read over the identical prefix at the first free read; first-read flips b {fr_b} / c {fr_c} explain 48 → 47")
    fig("47 (state-present) vs 48 (shadow) at the first free read", f"{fr_b + fr_c} of {nm} first-read picks flipped: "
        f"{fr_b} toward the +tag, {fr_c} toward the −tag; {k_sh} + {fr_b} − {fr_c} = {k_sh + fr_b - fr_c}",
        f"{VC} choices[0].paired_read (state_present.pick vs shadow.pick vs stratum.tag_plus)",
        "computed-new", "descriptive only (§2c); not a block figure")
    fig("conjunct (i): Δ_first exceeds the realised control ('sham') envelope", f"{f4(dm)} > {float(env):.4f}? {c1} → fail",
        "verdict_analysis.json primary.control_envelope, conjunct_envelope",
        "reproduced" if (st["env"] and st["c"]) else "discrepant",
        "envelope = max(|pseudo-Δ_sham|, |pseudo-Δ_random|), strict >; defined over sham AND random (analyzer :14-16, :221, :227); "
        f"the |·| is LOCK-h v2.0's ({lk_first_abs}, before the analyzer and the data); under PROPOSAL-h's literal signed "
        f"wording (i) would pass ({f4(dm)} > {f4(env_signed)}), and the verdict is {verdict} either way (§2a)")
    fig("envelope value 0.0833 (sham −0.0833, random −0.0278)",
        f"sham {ks}/{ns_} → {f4(ds)}; random {kr}/{nr} → {f4(dr)}; envelope {float(env):.4f} (from {env_src})",
        "verdict_analysis.json primary.sham, primary.random, primary.control_envelope",
        "reproduced" if (st["sham"] and st["random"] and st["env"]) else "discrepant",
        f"realised envelope sits at the exact null median (CDF {float(cdf_at_real):.4f})")
    fig("realised envelope relative to its null", f"{float(env):.4f} = {env}: exact null CDF {float(cdf_at_real):.4f}; "
        f"P(envelope ≥ {float(env):.4f}) = {float(p_ge_real):.4f}",
        "exact distribution of max(|k_s/36 − ½|, |k_r/36 − ½|), k_s, k_r ~ Binomial(36, ½) independent (§2d)",
        "computed-new", "the realised envelope was at the null median, not in its tail; not a block figure")
    fig("envelope planning reference p90 = 0.167", f"{float(p90):.4f} (= {p90}, exact)",
        "data/e2b/h1_power.json lockh_v1.envelope_exact.p90",
        "reproduced" if env_ok else "discrepant", "LOCK-h v2.0 §2 planning reference, not the criterion")
    fig("conjunct (ii): sign lock across maps", f"map0 {maps[0][0]}/{maps[0][1]} → {f4(maps[0][2])}; map1 {maps[1][0]}/{maps[1][1]} → {f4(maps[1][2])}; → fail",
        "verdict_analysis.json primary.by_map, conjunct_sign_lock",
        "reproduced" if (st["map0"] and st["map1"] and st["c"]) else "discrepant",
        "Δ ≥ 0 required in BOTH maps (analyzer :17, :228)")
    fig("conjunct (iii): one-sided exact binomial p = 0.6202, critical k ≥ 57",
        f"P(X ≥ {km} | {nm}, ½) = {float(p_one):.4f}; k_crit {kcrit}; → fail",
        "verdict_analysis.json primary.p_one_sided, critical_k, conjunct_binomial",
        "reproduced" if (st["p"] and st["kcrit"] and st["c"]) else "discrepant",
        f"one-sided (approach), α = .05; reverse tail P(X ≤ {km}) = {float(p_rev):.4f}, not an unexpected-direction finding")
    fig("verdict NULL (all three conjuncts fail)", verdict, "verdict_analysis.json primary.verdict",
        "reproduced" if st["verdict"] else "discrepant", "")
    fig("MDE 0.130 at 80% power (n = 96, binomial-only)", f"{mde_p1 - 0.5:.4f}",
        "data/e2b/h1_power.json mde_verdict_share", "reproduced" if mde_ok else "discrepant",
        "LOCK-h v2.0 §2 constant; the conjunctive MDE is 0.211 (§3c)")
    fig("π̂_d = 0.0172", f"{nd}/{N} = {float(pi):.7f}",
        "data/e2b/h1_sessions.json sessions[].choices[].paired_read; data/e2b/h1_gate.json pi_hat_d",
        "reproduced" if h1_ok["pi"] else "discrepant",
        "pick-discordance rate over H1's 640 paired reads (definition §3b)")
    fig("π̂_d CI [0.0086, 0.0305]", f"[{pil:.4f}, {pih:.4f}] (Clopper–Pearson 95%)",
        "data/e2b/h1_gate.json pi_hat_d_ci", "reproduced" if h1_ok["pi_ci"] else "discrepant",
        f"{pct(float(pi), bar)} / {pct(pih, bar)} of bar (the log's 41.5% divides the rounded 0.0305; both under half)")
    fig("bar 0.0735", f"min(0.5 × {mc:.4f}, {lk:.4f}) = {barv:.4f}",
        "data/e2b/h1_power.json lockh_v1.bar_leak, variants[0]",
        "reproduced" if all(bar_ok.values()) else "discrepant",
        "leak at ≤ 2.5% false-verdict rate binds; a bound on L (share shift), fixed at LOCK-h v1.1 8a97513 before H1 data")
    fig("L̂ = +0.00156; mapped L CI [−0.00915, +0.01143]; PASS by low discordance",
        f"{float(Lh):+.5f}; [{L_lo:+.5f}, {L_hi:+.5f}]; PASS={inside}, low-discordance={inside and by_cor}",
        "data/e2b/h1_gate.json L_hat, L_ci, verdict, certified_by_low_discordance",
        "reproduced" if (h1_ok["L"] and h1_ok["L_ci"] and h1_ok["verdict"] and h1_ok["low_disc"]) else "discrepant",
        f"b {b} / c {c} of n_d {nd}; CP on p_flip [{p_lo:.4f}, {p_hi:.4f}]")
    fig("certification definition (what is displaced, over what set, bounded how)",
        f"the pick (state-present vs shadow) over H1's {N} paired reads; |L| ≤ π̂_d; exact CP CI on b|n_d mapped inside ±{bar}",
        f"scripts/e2b_h1_sessions.py@{PIN}:171-174,213-225; scripts/e2b_h1_gate.py@{PIN}:97-100,114-118,125; "
        f"LOCK-h.md@{PIN}:" + ",".join(str(LOCATORS[k_]['lines'][0]) for k_ in ('L.unit', 'L.Lhat', 'L.gate', 'L.feas', 'L.v14')),
        "computed-new",
        "a code reading at pinned locators, not a figure computed from JSON; every number inside it "
        "(11/640, b 6 / c 5, the mapped CI, the bar) is reproduced in its own row; short and long "
        "forms of the sentence in §3b")
    fig("preprint :111 gloss 'direct displacement of label logits'", "π̂_d is a pick-discordance rate, not a logit displacement",
        # round 9: when patched, the line is the audited text's, as the committed raw located it (§0)
        (f"PREPRINT-v1_0-draft.md:{','.join(map(str, aud_loc['PRE.111']))} (untracked, sha d6431e97...)"
         f" as audited (superseded; patch v6, sha {v6_short}, rewrites "
         f":{','.join(map(str, aud_loc['PRE.111']))}"
         + (f", carried unchanged into patch {PREPRINT_PATCH}, sha {rec_short}" if r10_carried
            else f"; patch {PREPRINT_PATCH}, sha {rec_short}: round 10") + ": §6)" if pre111_patched
         else "PREPRINT-v1_0-draft.md:111 (untracked, sha d6431e97...)"),
        "discrepant",
        "values reproduced (π̂_d 0.0172 and bar 0.0735, rows above); the gloss is discrepant -- a "
        "definition error, not a transcription; no number in this row is discrepant. For N1 "
        "(block :23): a sentence correction; replace the gloss with §3b's short form. Routing is "
        "N1's and the design seat's; N6 raises no STOP"
        + ("; the status is the audited text's, carried unchanged; the rewrite is a finding on the patch "
           "for the design seat (§6)" if pre111_patched else ""))
    fig("verdict in-campaign leak: half-gap +0.00198 = 2.7% of bar; flip rate 0.0191",
        f"{mk_hg[0]:+.5f} ({pct(mk_hg[0], bar)}); {mk_bc[1]}/{mk_bc[0]} = {mk_bc[1] / mk_bc[0]:.4f}",
        "verdict_analysis.json descriptives.marker_leak", "reproduced" if vl_ok else "discrepant",
        f"half-gap is a menu-position quantity; the like-for-like L̂ for the marker arm is {(mk_bc[2] - mk_bc[3]) / mk_bc[0]:+.5f} ({pct(abs((mk_bc[2] - mk_bc[3]) / mk_bc[0]), bar)} of bar)")
    fig("directional-leak family +0.00084/+0.00220/0.00000/+0.00156/+0.00198, '≤ 3% of bar'",
        f"each value reproduces under its own quantity; uniformly: |half-gap| max {pct(J['leak_family_max']['half_gap'], bar)} ({J['leak_family_max']['half_gap_campaign']}), |L̂| max {pct(J['leak_family_max']['L_hat'], bar)} ({J['leak_family_max']['L_campaign']})",
        "h2_read_stability.json, h2_sessions.json, h1u_sessions.json, h1_sessions.json, verdict_campaign.json",
        "discrepant",
        f"values reproduced: each of the five family values reproduces from its artifact under its own "
        f"quantity, and '≤ 3%' holds for the list as printed (max "
        f"{100.0 * max(abs(float(r_['family_value'])) for r_ in J['leak_family']) / bar:.2f}% of bar); the characterisation is "
        f"discrepant -- {L_of('R.family_desc')} calls all five 'L (half-gap)', but two are L̂ = (b−c)/N "
        f"and three are the d_p_a half-gap. Not a transcription; no number is discrepant. Post-hoc. "
        f"For N1 (block :23): a wording correction to the O-leakage sentence; routing is N1's and the "
        f"design seat's; N6 raises no STOP. Every gate-form CI inside ±{bar}")
    fig("quarantined primitive's name", f"choice_read_statepresent ({SP}@{PIN}:{','.join(map(str, LOCATORS['SP.def']['lines']))})",
        f"{SP}@{PIN}", "computed-new",
        f"a code reading at a pinned locator (not a JSON figure); live: import refused from an "
        f"unsanctioned file ({import_res}); 0 offenders in valence_core")
    fig("what 'quarantined' enforces", "import guard; no re-export; per-read provenance; mandatory paired shadow; choice_read uninjectable; suite structural scan; insulated harnesses assert absence; clause 4 by commit order only",
        "§5 table (statepresent.py, records.py, readout.py, regression/analysis.py, session.py, e2d/runner.py, echo/maskedprefix.py; all @bbc9ffe)",
        "computed-new",
        f"a code reading at pinned locators plus model-free live checks (not a JSON figure); "
        f"provenance complete on {prov_checked - prov_bad}/{prov_checked} state-present reads "
        f"(verdict marker + random, H1); guard is basename-based (any e2b_*.py); the suite pins "
        f"only the refusal direction")
    P("| figure | value printed | source | status | note |")
    P("|---|---|---|---|---|")
    for r_ in FIG:
        P(f"| {cell(r_['figure'])} | {cell(r_['value'])} | {cell(r_['source'])} | {r_['status']} | {cell(r_['note'])} |")
    P("")

    # ------------------------------------------------- locator warnings, stops, notes --
    bad_loc = {k: v for k, v in LOCATORS.items() if not v["ok"]}
    P("## Locator self-check")
    P("")
    P(f"{len(LOCATORS)} needles searched in pinned blobs (preprint: working tree); "
      f"{len(LOCATORS) - len(bad_loc)} matched their expected count"
      + ("." if not bad_loc else "; mismatches: " + "; ".join(
          f"{k} expected {v['expect']} got {v['lines']}" for k, v in bad_loc.items()))
      + (" (PRE.111 is the audited text's needle, gone from the patched text: a finding on the patch, "
         "§6, not a locator defect; the sentence re-anchors as PRE.111.v6)." if pre111_patched
         else ("." if bad_loc else ""))
      + (" Preprint re-anchored to the patched text" if pre_match else
         f" Preprint working-tree copy (MISMATCH vs the patch-{PREPRINT_PATCH} text of record)")
      + f": PRE.176 at :"
        f"{','.join(map(str, LOCATORS['PRE.176']['lines']))} (audited :"
        f"{','.join(map(str, aud_loc['PRE.176']))}, from {DEF_JSON}@{RAW_COMMIT}).")
    P("")
    P("## STOPs")
    P("")
    if STOPS:
        for s_ in STOPS:
            P(f"- {s_['subitem']}: {s_['discrepancy']}")
    else:
        n_disc = sum(1 for r_ in FIG if r_["status"] == "discrepant")
        P("None raised by N6. Every figure the block names reproduces from committed JSON; no "
          "reproduction needed an analyzer change. "
          f"{n_disc} Figures rows carry status 'discrepant' (the preprint :111 gloss"
          + (" (the audited text's; patch v6 rewrites the line, §6)" if pre111_patched else "")
          + "; the leak-family characterisation): in both, every number reproduces and the discrepancy is a gloss or a "
          "characterisation, not a transcription of a number. Block :23 routes a non-transcription "
          "'discrepant' figure to a STOP on that item at N1; whether these two rows (no number "
          "discrepant) are figure STOPs or sentence corrections is N1's and the design seat's call, "
          "not N6's. N6's reading: sentence corrections.")
    P("")
    NOTES.append("Envelope wording (round 2): PROPOSAL-h's criterion text (:136-137) says 'max pseudo-Δ "
                 "across sham and random families', signed, and defers to '[LOCK-h formula]'; the absolute "
                 f"value is LOCK-h v2.0's ({lk_first_abs}, committed before the analyzer and the data). The "
                 "note's 'null on all three conjuncts' is right under the operative lock; under PROPOSAL-h's "
                 f"literal signed words (i) would pass and the verdict is still {verdict} ((ii) and (iii) fail). "
                 "A sentence-level note, not a STOP.")
    NOTES.append("For N1 and the README (round 2): ingest this raw's JSON "
                 "(results/raw/2026-10-08_note-N6-e2b.json), not a routing summary of an earlier pass (the "
                 "verifier's summary carried a stale script sha and pass-1 statuses). If the README reuses "
                 f"§5's '{len(absence_files)} files' line, keep the raw's phrasing ('name the quarantined module "
                 f"beside an absence assertion') or the computed split: {len(abs_runtime)} carry a runtime "
                 f"absence assertion and {len(abs_selftest)} (m-package files) check it only in a self-test.")
    P("## Code's notes (none is a STOP; the block's rule: a wrong referent or gloss is a note)")
    P("")
    for i, n_ in enumerate(NOTES, 1):
        P(f"{i}. {n_}")
    P("")

    # ------------------------------------------------- values-check (pass 1) --
    fig_status = {r_["figure"]: r_["status"] for r_ in FIG}
    relabelled = ["certification definition (what is displaced, over what set, bounded how)",
                  "quarantined primitive's name", "what 'quarantined' enforces"]
    disc_rows = [r_ for r_ in FIG if r_["status"] == "discrepant"]
    disc_notes_ok = all("values reproduced" in r_["note"].lower()
                        and "not a transcription" in r_["note"].lower()
                        and "no number" in r_["note"].lower() for r_ in disc_rows)
    n_sp_h2 = h2_bc[0]
    VCHK = [
        {"finding": "F1 (minor): three non-numeric Figures rows (certification definition; the "
                    "primitive's name; what 'quarantined' enforces) were labelled 'reproduced', which "
                    "rule 4 reserves for figures computed from committed JSON",
         "disposition": "fixed",
         "evidence": "statuses now: " + "; ".join(f"'{f_}' → {fig_status.get(f_)}" for f_ in relabelled)
                     + ". The status vocabulary line now defines computed-new to include a code reading "
                       "the block asks for; each row's note says the numbers inside it are reproduced "
                       "in their own rows."},
        {"finding": "F2 (minor): the two 'discrepant' rows (preprint :111 gloss; leak-family "
                    "characterisation) beside 'STOPs: None' could be read by N1 under block :23 as "
                    "figure STOPs",
         "disposition": "fixed, wording adapted",
         "evidence": f"both rows' notes now state 'values reproduced', 'not a transcription' and 'no "
                     f"number ... is discrepant' (check over the {len(disc_rows)} discrepant rows: "
                     f"{disc_notes_ok}); the STOPs section says the same. Adapted: N6 does not write "
                     "'not a figure STOP' as a ruling -- block :23 makes that N1's and the design "
                     "seat's routing; N6 states the facts and its reading (sentence corrections)."},
        {"finding": "F3 (minor): 'marker + random pooled, as declared at LOCK-h.md@bbc9ffe:83' -- "
                    "the lock declares the monitor but not the pooling",
         "disposition": "fixed",
         "evidence": f"LOCK-h's six-line declaration names no arm ('pool'/'random'/'marker' present: "
                     f"{lock_states_pool}); the runner's counter admits every read whose `flipped` is "
                     f"not None (scripts/e2b_verdict_campaign.py@485cc94:{_fmt_l(mon_l485)}); data "
                     f"recount of the admitted reads {dict(mon_pool)} = {sum(mon_pool.values())} = "
                     f"stored n_paired_reads {V['n_paired_reads']}: {mon_pool_ok}. §4 now attributes "
                     "the pooling to the runner, with Code's reading that it is the plain reading of "
                     "'128-paired-read'."},
        {"finding": "F4 (minor): §5 said the sanctioned import direction 'is logged once, in' the "
                    "consolidation raw; it is also in the consolidation RESULTS entry, and every "
                    "campaign exercised it implicitly",
         "disposition": "fixed",
         "evidence": f"added {L_of('R.consol_tab')} (row) under {L_of('R.consol_hdr')} (entry); module-level "
                     "imports in each campaign's runner at every commit of its artifact's history: "
                     + "; ".join(_ci_txt(ci_) for ci_ in camp_imports)
                     + f" (all: {camp_all_import}). The core point stands: the suite pins only refusal "
                       f"(suite files naming `statepresent` at 6897b67: {suite_naming_6897}; e2b runners "
                       f"there: {runners_6897}). One correction to the finding's evidence: the "
                       f"{prov_checked} provenance-complete state-present reads of §5 are the verdict "
                       f"campaign's (marker + random) and H1's only; H2 proper's {n_sp_h2} valid-session "
                       "reads (and H1-u's, read half's) are not in that count."},
        {"finding": "F5 (minor): §3b's identity clause ('sessions identical to the verdict tier's "
                    "except that no pick selects a state') was uncited, and the sentence is long",
         "disposition": "fixed",
         "evidence": f"identity clause now cites {L_of('L.v14')} (LOCK-h v1.4, d94e281; ancestor of the "
                     f"H1 data commit 7527270: {J['commit_order'][3]['ancestor_of_next']}) and PROPOSAL-h's "
                     f"note {L_of('Ph.note')} (b400083); a one-sentence short form "
                     f"({len(short.split())} words) is printed beside the long form "
                     f"({len(defn.split())} words); both carry only values reproduced in §3a."},
        {"finding": "F6 (minor): §0's commit-order table omits b400083, which appended an "
                    "interpretive note to PROPOSAL-h after the H1 data and before LOCK-h v2.0",
         "disposition": "fixed",
         "evidence": f"rows added for b400083 and (fixer's addition, it carries the clause F5 cites) "
                     f"d94e281; chain verified ancestor-by-ancestor: "
                     f"{all(r_['ancestor_of_next'] for r_ in J['commit_order'][:-1])}. PROPOSAL-h at "
                     f"the pin = the 34eb7ee text's first {n_keep} lines unchanged ({ph_prefix_equal}) "
                     f"+ {ph_added} appended lines; the cited lines {ph_cited} lie in the unchanged "
                     f"prefix: {ph_cited_in_prefix}. No N6 locator or figure moves."},
    ]
    P("## Values-check (pass 1: adversarial checker, 130 claims, 6 minor findings; fixer's dispositions)")
    P("")
    P("The checker reports that it re-ran the pass-1 script into scratch (identical outputs apart "
      "from run metadata), found the redaction check clean, and independently recomputed every "
      "figure the block names for N6 (all agree). Its six findings, all minor, and the fixer's "
      "dispositions (the evidence column is computed by this run):")
    P("")
    P("| finding | disposition | evidence (this run) |")
    P("|---|---|---|")
    for v_ in VCHK:
        P(f"| {cell(v_['finding'])} | {v_['disposition']} | {cell(v_['evidence'])} |")
    P("")
    P("Fixer's own additions (no new statistic): the two computed-new rows '47 vs 48' and 'realised "
      "envelope relative to its null' are surfaced in the Figures table from §2c and §2d's prose; "
      "§0 states readout.py's blob identity at 6897b67 and 485cc94 (the checker noted it unstated); "
      "§0 adds the d94e281 row.")
    P("")
    P(f"Pass-1 comparison, quoted verbatim (text, not recomputed here). It was written by the pass-2 run "
      f"(script sha256 {PASS2_SCRIPT_SHA[:16]}, raw sha256 {PASS2_MD_SHA[:16]}, JSON sha256 "
      f"{PASS2_JSON_SHA[:16]}), which took `--compare-json` on the builder's pass-1 JSON (sha256 "
      f"{PASS1_JSON_SHA[:16]}); all of those files are session scratch, not in the repository, so this "
      "paragraph is a record of that run. Round 2 (below) moved the canonical raw to a run without the "
      "flag:")
    P("")
    P("> " + PASS1_CMP_QUOTE)
    P("")

    # ------------------------------------------------- values-check (round 2) --
    h1p = "scripts/h1_power.py"
    h1p_abs = lines_with(pinned_text(h1p), "np.abs(")
    h1p_same = git("diff", "--quiet", "7302384", PIN, "--", h1p, check=False).returncode == 0
    h1p_anc = ancestor("7302384", "8a97513")
    st_rows = {f_: fig_status.get(f_) for f_ in relabelled}
    guard_p = "valence_core/m/guard.py"
    guard_ins = lines_with(pinned_text(guard_p), "def assert_insulated")
    _gh = absence_split.get(guard_p, {}).get("hits", [])
    guard_body = sorted({h_["line"] for h_ in _gh if h_["functions"][:1] == ["assert_insulated"]})
    guard_call = sorted({h_["line"] for h_ in _gh if h_["functions"][:1] == ["insulated_read"]})
    guard_self = sorted({h_["line"] for h_ in _gh if h_["selftest"]})
    guard_read = lines_with(pinned_text(guard_p), "def insulated_read(")
    R2 = [
        {"finding": "R2-F1 (minor): §2a cites PROPOSAL-h §3 and LOCK-h v2.0 §2 together, but "
                    "PROPOSAL-h:136-137 says 'max pseudo-Δ' with no absolute value and defers to "
                    "'[LOCK-h formula]'; the |·| first appears in LOCK-h v2.0 (f030cdd). Read signed, "
                    "(i) would pass; the verdict is NULL either way",
         "disposition": "fixed",
         "evidence": f"§2a now carries the sentence; computed: PROPOSAL-h '[LOCK-h formula]' "
                     f"{L_of('Ph.defer')}, signed words {L_of('Ph.env_signed')} ('|' on :136-137: "
                     f"{ph_env_has_abs}; in the 34eb7ee prefix: {ph_env_in_prefix}); LOCK-h history "
                     f"(newest first) {lk_hist}, lines with 'pseudo': "
                     + ", ".join(f"{c_} {lk_pseudo[c_]['pseudo']}" for c_ in lk_hist)
                     + f"; '|pseudo-Δ|' first at {lk_first_abs} (line {lk_pseudo[lk_first_abs]['abs']}); "
                     f"{lk_first_abs} → a2f074d → 485cc94 ancestors: {lk_first_before_an}. Signed envelope "
                     f"max({f4(ds)}, {f4(dr)}) = {f4(env_signed)}; Δ_first {f4(dm)} > it: {c1_signed}; "
                     f"(ii) {c2}, (iii) {c3}; verdict under the signed reading "
                     f"{J['envelope_abs_provenance']['verdict_signed_reading']}, under the lock {verdict}. "
                     f"Code's addition: the power model behind the planning reference p90 = 0.167 and "
                     f"bar_leak folds with np.abs ({h1p}@{PIN}:{','.join(map(str, h1p_abs))}; unchanged since "
                     f"7302384: {h1p_same}; 7302384 an ancestor of LOCK-h v1.1 8a97513: {h1p_anc}). The "
                     "Figures row for (i) and §6 point to §2a."},
        {"finding": "R2-F2 (minor): §3b quotes scripts/e2b_h1_sessions.py@bbc9ffe as 'code of record' "
                    "and §4 cites session_e2a.py:78, but the H1 runner changed after 7527270 (1465b34) "
                    "and MENU_TEMPLATES then lived in valence_core/e2b/session.py; §0 said nothing of "
                    "either",
         "disposition": "fixed",
         "evidence": f"§0 now carries both lines: runner == at 7527270: {h1r_same}; commits after "
                     f"7527270: {h1r_commits}; {len(_hunks)} hunks, kinds {dict(h1r_kinds)}; moved import "
                     f"block identical apart from the module name: {h1r_import_moved_same}; slices "
                     + "; ".join(f"{s_['pin'][0]}-{s_['pin'][1]} → 7527270:{s_['at_7527270'][0]}-{s_['at_7527270'][1]}"
                                 for s_ in h1r_slices if s_["at_7527270"])
                     + f" (all unique and identical: {h1r_slices_ok}); MENU_TEMPLATES at 7527270:"
                     f"{mt['7527270'][1]}, 485cc94:{mt['485cc94'][1]} (valence_core/e2b/session.py) and "
                     f"{PIN}:{mt[PIN][1]} (valence_core/session_e2a.py) identical: {mt_equal}; renamed by "
                     f"1465b34: {mt_renamed}. §3b's heading and §4's template bullet point to §0."},
        {"finding": "R2-F3 (minor): '23.4%/41.5% RESULTS.md@bbc9ffe:6795' -- :6795 carries only 41.5%; "
                    "the pair is at :6798",
         "disposition": "fixed",
         "evidence": f"§3a now cites 41.5% at {L_of('R.ratio')} and the pair at {L_of('R.ratio2')}."},
        {"finding": "R2-F4 (minor): the header's command took --compare-json on a session-scratch file, "
                    "so it cannot be re-run from the repository",
         "disposition": "fixed (the fix's first option)",
         "evidence": f"this raw was written without the flag (flag given to this run: "
                     f"{args.compare_json is not None}); the pass-1 comparison above is now quoted text "
                     "with its provenance, emitted on every run; when --compare-json is given, a live "
                     "comparison is appended under its own heading after this table, and that output is "
                     "not the canonical raw. The command in the header needs no session-scratch input; it "
                     f"reads the untracked {PREPRINT} at the root (§0), so a checkout without that file "
                     "cannot re-run it."},
        {"finding": "R2-F5 (minor): the routing summary handed to the verifier was stale (script sha256 "
                    "cb87babd...; 'reproduced' for three rows); the '14 harnesses' line, if reused, should "
                    "keep the raw's phrasing or be split 9 harness/runtime + 5 m-package self-test checks",
         "disposition": "staleness noted for N1; the raw's phrasing kept and the split computed; the "
                        "finding's 9/5 split rejected (10/4)",
         "evidence": f"this run's script sha256 begins {me_sha[:8]} (begins cb87babd: "
                     f"{me_sha.startswith('cb87babd')}); the three rows' statuses here: "
                     + "; ".join(f"'{k_}' → {v_}" for k_, v_ in st_rows.items())
                     + ". N1 should ingest this raw's JSON (results/raw/2026-10-08_note-N6-e2b.json), not a "
                       f"routing summary (Code's note {len(NOTES)}). AST split of the {len(absence_files)} files "
                       f"(§5): runtime assertion {len(abs_runtime)}, self-test only {len(abs_selftest)} "
                       f"{abs_selftest}. The finding's 9/5 counts {guard_p} as self-test only, but it carries "
                       f"a runtime assertion: `assert_insulated` ({guard_p}@{PIN}:{','.join(map(str, guard_ins))}) "
                       f"calls `assert_modules_absent(FORBIDDEN_MODULES)` (:{','.join(map(str, guard_body))}), and "
                       f"`insulated_read` (:{','.join(map(str, guard_read))}) calls it before every read "
                       f"(:{','.join(map(str, guard_call))}); its self-test exercises it too "
                       f"(:{','.join(map(str, guard_self))}). Files naming the module without a marker "
                       f"(excluded by the heuristic): {named_no_marker}."},
    ]
    P("### Round 2 (verifier: 5 minor findings; Code's dispositions)")
    P("")
    P("Each finding was checked by a tool run before it was applied; the evidence column is computed by "
      "this run. No Figures value, status or verdict changes (one Figures note gains a pointer). The edits: "
      "a sentence in §2a (pointed to from the (i) Figures row, §6 and Code's note 4); two provenance lines "
      "in §0 (pointed to from §3b's heading and §4); a locator in §3a; the raw's canonical command; a "
      "computed split in §5 (with Code's note 5).")
    P("")
    P("| finding | disposition | evidence (this run) |")
    P("|---|---|---|")
    for v_ in R2:
        P(f"| {cell(v_['finding'])} | {v_['disposition']} | {cell(v_['evidence'])} |")
    P("")

    cmp_res = None
    if args.compare_json:
        with open(args.compare_json, "rb") as fh:
            prev_bytes = fh.read()
        prev = json.loads(prev_bytes.decode("utf-8"))
        rt = lambda x: json.loads(json.dumps(x, ensure_ascii=False, default=str))
        keys = ["primary", "shadow", "arm_geometry", "marker_forced_end", "envelope_reference",
                "mde_binomial", "h1", "bar_derivation", "leak_family", "leak_family_max",
                "verdict_leak", "menu_a_is_plus_tag", "menu_templates_a_first", "quarantine",
                "absence_asserting_files", "pinned_sha256", "wt_equal_pin", "preprint", "stops"]
        cur = dict(J, stops=STOPS)  # J["stops"] is assigned after this section
        cmp_res = {k_: (rt(cur.get(k_)) == prev.get(k_)) for k_ in keys}
        un_prev = prev.get("unchanged", {})
        cmp_res["unchanged (previous keys)"] = all(rt(J["unchanged"]).get(k_) == v_ for k_, v_ in un_prev.items())
        prev_fig = {r_["figure"]: r_ for r_ in prev.get("figures", [])}
        val_changed = [r_["figure"] for r_ in FIG
                       if r_["figure"] in prev_fig and prev_fig[r_["figure"]]["value"] != r_["value"]]
        note_changed = [r_["figure"] for r_ in FIG
                        if r_["figure"] in prev_fig and prev_fig[r_["figure"]]["note"] != r_["note"]]
        stat_changed = [f"{r_['figure']}: {prev_fig[r_['figure']]['status']} → {r_['status']}" for r_ in FIG
                        if r_["figure"] in prev_fig and prev_fig[r_["figure"]]["status"] != r_["status"]]
        new_rows = [r_["figure"] for r_ in FIG if r_["figure"] not in prev_fig]
        all_stats_same = all(cmp_res.values())
        P("### Live comparison with --compare-json (this run; not part of the canonical raw)")
        P("")
        P(f"This run vs the JSON given by --compare-json (sha256 {sha256_bytes(prev_bytes)[:16]}): "
          + "; ".join(f"{k_} {'same' if v_ else 'CHANGED'}" for k_, v_ in cmp_res.items())
          + f". All computed sections the same: {all_stats_same}. Figures rows whose value changed: "
            f"{val_changed if val_changed else 'none'}; whose note changed: "
            f"{note_changed if note_changed else 'none'}; status changes: "
            f"{stat_changed if stat_changed else 'none'}; rows new in this run: {new_rows if new_rows else 'none'}.")
        P("")
        cmp_res = {"sections_same": cmp_res, "value_changed": val_changed, "note_changed": note_changed,
                   "status_changed": stat_changed, "new_rows": new_rows,
                   "compared_sha256": sha256_bytes(prev_bytes)}
    J["values_check"] = {"findings": VCHK,
                         "pass1_comparison_quoted": {"text": PASS1_CMP_QUOTE,
                                                     "pass2_script_sha256": PASS2_SCRIPT_SHA,
                                                     "pass2_md_sha256": PASS2_MD_SHA,
                                                     "pass2_json_sha256": PASS2_JSON_SHA,
                                                     "pass1_json_sha256": PASS1_JSON_SHA},
                         "round2": R2, "live_comparison": cmp_res}
    J["figures"] = FIG
    J["stops"] = STOPS
    J["notes"] = NOTES
    J["locators"] = LOCATORS

    os.makedirs(os.path.dirname(out_md), exist_ok=True)
    with open(out_md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(OUT) + "\n")
    with open(out_js, "w", encoding="utf-8") as fh:
        json.dump(J, fh, indent=1, ensure_ascii=False, default=str)
    print(f"wrote {os.path.relpath(out_md, REPO)} and {os.path.relpath(out_js, REPO)}; "
          f"stops {len(STOPS)}; locator mismatches {len(bad_loc)}"
          + (" (PRE.111: the audited text's needle, a finding on the patch, §6; not a STOP)"
             if pre111_patched else "")
          + f"; round 10 (patch {PREPRINT_PATCH}): dispositions "
          + (", ".join(f"{d_['check']} {d_['disposition']}" for d_ in DISP) or "none")
          + f"; new findings on the patch {len(NEWF)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
