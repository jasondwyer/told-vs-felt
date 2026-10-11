#!/usr/bin/env python3
"""AUDIT-note-release v1.2, item N4 -- e2a figures, MDE, and the disclosures.

READ-ONLY ON THE RECORD. Every committed artifact is read at the pin
(`git show bbc9ffe:<path>`); the record's own analyzer (scripts/e2a_recount.py)
and pure helpers (valence_core.session, valence_core.e2d.habit) are imported
from the working tree only after their blobs are asserted equal to the pinned
blobs. Nothing is written except the two outputs (--out, --json-out). No model
is loaded; numpy is not needed; exact tests are stdlib (math.comb, math.lgamma,
statistics.NormalDist). Bytecode writing is disabled so no __pycache__ appears
in the repository.

Usage (from anywhere):
  jlens-qwen36/.venv/bin/python scripts/audit_note_N4.py \
      [--out results/raw/2026-10-08_note-N4-e2a.md] \
      [--json-out results/raw/2026-10-08_note-N4-e2a.json]

Deterministic apart from the run-metadata lines (stamp, HEAD at run time,
command line). No randomness is used anywhere.

Round 9 (2026-10-10, Tier 1, before N1's round 9): re-pointed at the patched
preprint under the PI's ruling 9 of 2026-10-10, as corrected. The preprint of
record is PREPRINT-v1_0-draft.md at sha256 0f4ba501...6c22 (patch v6), asserted
in full before anything is written: any other text stops the run. The
block's d6431e97...222b8 is the audited, superseded text, archived untracked at
archive/PREPRINT-v1_0-draft.pre-patch-v6.md and never required here. Preprint
locators are found by anchor text in the patched file. A check of a preprint
sentence that fails on the patched text is not a STOP: it is a finding on the
patch for the design seat (section "Findings on the patch"), quoting the old
line from the committed raw of record (RAW_REC) and the new line from the
patched file, with the figures the patched lines print parsed and compared with
this run's values at their printed precision. Every preprint sentence the
script quotes or characterizes is located by text: the e2a primary and footnote
1, the 'break rate' habit sentence, the interval, the power sentence (ii), the
:109 verification sentence and the :262 disclosure. Nothing that does not read
the preprint is changed.
"""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True

import argparse
import collections
import hashlib
import importlib.util
import io
import json
import math
import os
import re
import shlex
import subprocess
from statistics import NormalDist

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = "bbc9ffe"
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
PREPRINT = "PREPRINT-v1_0-draft.md"
# round 9: the preprint of record, patch v6 (the PI's ruling 9 of 2026-10-10, as corrected)
PREPRINT_SHA = "0f4ba501d60a94189e6dc83d28c41826debe50591b9af484fa08d05a41f16c22"
# the block's referent, audited through round 8: superseded; archived untracked, never required
PREPRINT_SHA_AUDITED = "d6431e97d35e5914574ff9884c0e64463a7baf1cf9d279f27ed45a683a6222b8"
PREPRINT_AUDITED_ARCHIVE = "archive/PREPRINT-v1_0-draft.pre-patch-v6.md"
# the committed raw of record that quotes the audited text: a finding's old line is read from it
RAW_REC = ("09c3a8c", "results/raw/2026-10-08_note-N4-e2a.md")
# the committed e2a correction-of-record artifact (computed-new Wilson intervals) and its raw, read at their commit
COR_REC = ("e60b633", "data/e2a/analysis.correction-of-record.json", "results/raw/2026-10-09_note-N4-correction.md")
CLONE = "jlens-qwen36"          # gitignored third-party clone: read only, never git
DEF_OUT = "results/raw/2026-10-08_note-N4-e2a.md"
DEF_JSON = "results/raw/2026-10-08_note-N4-e2a.json"
ARMS = ("reward", "sham", "random1", "random2")

# ----------------------------------------------------------------- plumbing --

def git(*args: str) -> bytes:
    """Read-only git only (show, rev-parse, log, ls-files, status without
    optional locks). Never run inside the jlens-qwen36 clone."""
    assert args[0] in ("show", "rev-parse", "log", "ls-files", "status", "diff"), args
    return subprocess.run(["git", "--no-optional-locks", "-C", REPO, *args],
                          check=True, capture_output=True).stdout


def blob_sha1(b: bytes) -> str:
    """git's blob id, computed in Python (no git hash-object)."""
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def cell(s) -> str:
    """Markdown table cell: escape pipes."""
    return str(s).replace("|", "\\|")


_CACHE: dict[str, bytes] = {}


def pinned(path: str) -> bytes:
    if path not in _CACHE:
        _CACHE[path] = git("show", f"{PIN}:{path}")
    return _CACHE[path]


def pinned_text(path: str) -> str:
    return pinned(path).decode("utf-8")


def pinned_json(path: str):
    return json.loads(pinned_text(path))


def pinned_jsonl(path: str) -> list:
    return [json.loads(l) for l in pinned_text(path).split("\n") if l.strip()]


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_file(p: str) -> str:
    with open(p, "rb") as f:
        return sha256_bytes(f.read())


def blob_equal_to_pin(path: str) -> bool:
    with open(os.path.join(REPO, path), "rb") as f:
        wt = blob_sha1(f.read())
    pn = git("rev-parse", f"{PIN}:{path}").decode().strip()
    return wt == pn


def lines_with(text: str, needle: str) -> list[int]:
    """1-based line numbers as `git show <pin>:<path> | sed -n` counts them:
    split on '\\n' only. str.splitlines() also breaks on '\\r' (tqdm progress
    bars in the raws), which shifted locators in the builder's first pass."""
    return [i for i, l in enumerate(text.split("\n"), start=1) if needle in l]


def loc(path: str, needle: str, end_needle: str | None = None,
        working_tree: bool = False) -> str:
    """Pinned locator 'path@bbc9ffe:N' (or N-M) found by anchor text; the
    anchor must exist, and the first occurrence is used (all printed if > 1)."""
    if working_tree:
        with open(os.path.join(REPO, path), encoding="utf-8") as f:
            text = f.read()
        tag = f"{path}(working tree, sha256 {sha256_bytes(text.encode())[:16]})"
    else:
        text = pinned_text(path)
        tag = f"{path}@{PIN}"
    hits = lines_with(text, needle)
    if not hits:
        raise SystemExit(f"anchor not found in {tag}: {needle!r}")
    a = hits[0]
    if end_needle is not None:
        ends = [h for h in lines_with(text, end_needle) if h >= a]
        if not ends:
            raise SystemExit(f"end anchor not found in {tag}: {end_needle!r}")
        b = ends[0]
        s = f"{tag}:{a}" if a == b else f"{tag}:{a}-{b}"
    else:
        s = f"{tag}:{a}"
    if len(hits) > 1:
        s += f" (anchor also at {','.join(map(str, hits[1:6]))})"
    return s


def sentence_at(txt: str, needle: str, cap: int = 420) -> str:
    """The sentence of `txt` containing `needle` (split on '. '), capped."""
    i = txt.find(needle)
    a = txt.rfind(". ", 0, i)
    a = 0 if a < 0 else a + 2
    b = txt.find(". ", i + len(needle))
    b = len(txt) if b < 0 else b + 1
    s = txt[a:b]
    return s if len(s) <= cap else s[:cap] + " [...]"


def quote_lines(path: str, needles: list[str], clone: bool = False) -> list[str]:
    """Return 'path:N: <line>' for the first line containing each needle."""
    if clone:
        full = os.path.join(REPO, path)
        with open(full, encoding="utf-8") as f:
            text = f.read()
    else:
        text = pinned_text(path)
    ls = text.split("\n")
    out = []
    for nd in needles:
        hits = lines_with(text, nd)
        if not hits:
            out.append(f"{path}: [anchor not found: {nd!r}]")
            continue
        n = hits[0]
        out.append(f"{path}:{n}: {ls[n - 1].rstrip()}")
    return out


# ------------------------------------------------------------- exact stats --

def lpmf(k: int, n: int, p: float) -> float:
    if p <= 0.0:
        return 0.0 if k == 0 else -math.inf
    if p >= 1.0:
        return 0.0 if k == n else -math.inf
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
            + k * math.log(p) + (n - k) * math.log1p(-p))


def pmf(k: int, n: int, p: float) -> float:
    return math.exp(lpmf(k, n, p))


def sf(k: int, n: int, p: float) -> float:
    """P(X >= k | n, p), exact sum of pmfs."""
    return sum(pmf(i, n, p) for i in range(max(k, 0), n + 1))


def p_ge_half(k: int, n: int) -> float:
    """P(X >= k | n, 1/2) in exact integer arithmetic (the record's form)."""
    return sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n


def bisect_increasing(f, target: float, lo: float, hi: float, it: int = 200) -> float:
    """Smallest x in [lo, hi] with f(x) >= target, f nondecreasing."""
    for _ in range(it):
        m = (lo + hi) / 2
        if f(m) >= target:
            hi = m
        else:
            lo = m
    return hi


def wilson(k: int, n: int, conf: float = 0.95):
    z = NormalDist().inv_cdf(1 - (1 - conf) / 2)
    c = (k + z * z / 2) / (n + z * z)
    h = z * math.sqrt(k * (n - k) / n + z * z / 4) / (n + z * z)
    return c - h, c + h


def wald(k: int, n: int, conf: float = 0.95):
    z = NormalDist().inv_cdf(1 - (1 - conf) / 2)
    ph = k / n
    h = z * math.sqrt(ph * (1 - ph) / n)
    return ph - h, ph + h


def clopper_pearson(k: int, n: int, conf: float = 0.95):
    a = (1 - conf) / 2
    lo = 0.0 if k == 0 else bisect_increasing(lambda p: sf(k, n, p), a, 0.0, 1.0)
    # upper: largest p with P(X <= k | p) >= a  <=>  P(X >= k+1 | p) <= 1 - a
    if k == n:
        hi = 1.0
    else:
        hi = bisect_increasing(lambda p: sf(k + 1, n, p), 1 - a, 0.0, 1.0)
    return lo, hi


# --------------------------------------------------------------- the output --

class Out:
    def __init__(self):
        self.buf = io.StringIO()

    def __call__(self, s: str = ""):
        self.buf.write(s + "\n")


IMPORTED_OK: list[str] = []
FIGS: list[dict] = []
STOPS: list[dict] = []
NOTES: list[str] = []
PI: list[str] = []


def fig(figure, reproduced, source, status, named_in="", note=""):
    FIGS.append({"figure": figure, "named_in": named_in,
                 "reproduced": reproduced, "source": source,
                 "status": status, "note": note})


PATCH: list[dict] = []   # round 9, ruling 9: findings on the patch (design seat), never STOPs


def rec_line(needle: str, upto: str | None = None) -> dict:
    """The first line of the committed raw of record carrying `needle`, cut after `upto` if given."""
    t = git("show", f"{RAW_REC[0]}:{RAW_REC[1]}").decode("utf-8")
    h = lines_with(t, needle)
    assert h, needle
    s = t.split("\n")[h[0] - 1].strip()
    return {"locator": f"{RAW_REC[1]}@{RAW_REC[0]}:{h[0]}", "quote": s[:s.index(upto) + len(upto)] if upto else s}


def patch_finding(check: str, old: list[dict], new: list[dict], values: str, figures: str = "") -> str:
    """Record a preprint-sentence check that fails on the patched text; returns its id. `figures` states,
    computed, whether the figures the patched lines print equal this run's values at their printed precision."""
    PATCH.append({"id": f"PF-{len(PATCH) + 1}", "check": check, "result": "FAILS on the patched text",
                  "old": old, "new": new, "record_values_this_run": values,
                  "patched_figures_vs_this_run": figures})
    return PATCH[-1]["id"]


def eq_printed(printed: str, value: float) -> bool:
    """True iff `value` rounds to the printed decimal (e.g. '+0.035', '.275', '−0.03') at its printed precision."""
    s = printed.replace("−", "-").replace("+", "")
    nd = len(s.split(".")[1]) if "." in s else 0
    return round(value, nd) == float(s)


def r4(x: float) -> float:
    return round(x, 4)


def note_no(prefix: str) -> int:
    """1-based number of the one referent note starting with `prefix`, as printed (round 4, finding 1: note
    numbers are computed, never written by hand)."""
    hits = [i for i, n in enumerate(NOTES, 1) if n.startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    return hits[0]


NOTE_INTERVAL = "The approach-probability interval ≈ [.44, .64]"
NOTE_INTEG = "Design seat's claim 'none [integer] under (approach - avoid)/n'"
NOTE_TSTEP = "T-step 'position':"
NOTE_G3 = "g3′ amendment: its adjudication basis"
NOTE_CARD9 = "Review card 9 as the design handoff numbers it"
NOTE_CARDS = "Review-card numbering."


# ================================================================== main ====

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEF_OUT)
    ap.add_argument("--json-out", default=DEF_JSON)
    args = ap.parse_args()
    out_md = args.out if os.path.isabs(args.out) else os.path.join(REPO, args.out)
    out_js = (args.json_out if os.path.isabs(args.json_out)
              else os.path.join(REPO, args.json_out))

    o = Out()
    stamp = subprocess.run(["date", "-u"], capture_output=True, text=True,
                           check=True).stdout.strip()
    head = git("rev-parse", "HEAD").decode().strip()
    me = os.path.abspath(__file__)
    me_rel = os.path.relpath(me, REPO)
    block_pin_sha = sha256_bytes(pinned(BLOCK))
    cmd = " ".join(shlex.quote(a) for a in [sys.executable, *sys.argv])

    o("# AUDIT-note-release v1.2 -- N4: e2a figures, MDE, and the disclosures")
    o()
    o(f"- Code stamp: {stamp} (date -u)  [run metadata]")
    o(f"- HEAD at run time: {head}  [run metadata; every record read below is pinned to {PIN}]")
    o(f"- Command: `{cmd}`  [run metadata]")
    o(f"- Pin: {PIN} = {git('rev-parse', PIN).decode().strip()}")
    o(f"- Block: `{BLOCK}`@{PIN} sha256 `{block_pin_sha}` "
      f"({'MATCH' if block_pin_sha == BLOCK_SHA else 'MISMATCH'} vs routed 8cd8a9ac...3841); "
      f"item N4 = block lines {loc(BLOCK, '### N4. e2a figures', 'Pass:* (i) reproduces; (ii)').split(':')[-1]}")
    o(f"- Script: `{me_rel}` sha256 `{sha256_file(me)}`")
    o(f"- Interpreter: {sys.executable} (Python {sys.version.split()[0]}); stdlib only "
      f"for every computation (math.comb, math.lgamma, statistics.NormalDist); numpy is loaded only because the "
      f"imported record modules import it, and is not used here; no scipy/sklearn; no model")
    o()
    o("Status vocabulary: reproduced (a figure this script computes from committed "
      "JSON/JSONL and prints) | log-only (exists only in log prose; pinned locator) | "
      "not found | discrepant | computed-new (a computation the block asks for). "
      "Locators are `path@bbc9ffe:line` as in `git show bbc9ffe:<path>`.")
    o()

    # ------------------------------------------------------------- integrity
    o("## 0. Referents and integrity")
    o()
    imported = ["scripts/e2a_recount.py", "valence_core/__init__.py",
                "valence_core/adapters/__init__.py", "valence_core/adapters/base.py",
                "valence_core/session.py", "valence_core/stats.py",
                "valence_core/e2d/__init__.py", "valence_core/e2d/habit.py",
                "data/e2a/sessions.jsonl", "data/configs/e2b_audit_v2.json"]
    o("Working-tree blobs of everything imported or read through the working tree, "
      "against the pin (git blob id computed in Python vs `git rev-parse bbc9ffe:<path>`):")
    o()
    allok = True
    for p in imported:
        ok = blob_equal_to_pin(p)
        allok &= ok
        o(f"- `{p}`: {'EQUAL to pin' if ok else 'DIFFERS from pin'}")
    if not allok:
        raise SystemExit("working tree differs from the pin on an imported file; refusing")
    o()
    o("Committed artifacts read at the pin (sha256 of the pinned blob):")
    o()
    art = ["data/e2a/analysis.json", "data/e2a/sessions.jsonl",
           "data/e2a/sessions_smoke.jsonl", "data/e2a/sessions_smoke_v1_incident.jsonl",
           "data/e2a/g3prime_kl.jsonl", "data/e2a/g3prime_kl_v1.jsonl",
           "data/e2a/g1_kernel_gate.json", "data/e2a/g2_discriminability_v2.json",
           "data/e2a/g2_discriminability.json", "data/e2a/g2_spotcheck.json",
           "data/configs/e2a_ban_list.json",
           "data/e2d/tstep_check.json", "data/e2d/tstep_check_f010.json",
           "data/e2b/h1_sessions.json", "data/e2b/h1u_sessions.json",
           "data/e2b/h2_sessions.json", "data/e2b/verdict_campaign.json",
           "scripts/e2a_recount.py", "valence_core/session_e2a.py",
           "valence_core/readout.py", "valence_core/e2b/statepresent.py",
           "scripts/box_cached_gen_smoke.py"]
    shas = {}
    for p in art:
        shas[p] = sha256_bytes(pinned(p))
        o(f"- `{p}` `{shas[p][:16]}`")
    o()
    pre_path = os.path.join(REPO, PREPRINT)
    pre_sha = sha256_file(pre_path)
    if pre_sha != PREPRINT_SHA:  # round 9: asserted in full, before anything is written (as N5, N7, N17)
        raise SystemExit(f"{PREPRINT} sha256 {pre_sha} != the preprint of record {PREPRINT_SHA} "
                         f"(the PI's ruling 9 of 2026-10-10, as corrected)")
    tracked_pre = bool(git("ls-files", "--", PREPRINT).strip())
    aud_fp = os.path.join(REPO, PREPRINT_AUDITED_ARCHIVE)
    aud_st = (("present, sha256 " + ("MATCH" if sha256_file(aud_fp) == PREPRINT_SHA_AUDITED else "MISMATCH"))
              if os.path.exists(aud_fp) else "absent")
    o(f"- `{PREPRINT}` (root, {'tracked' if tracked_pre else 'UNTRACKED: absent from any clone'}) "
      f"sha256 `{pre_sha}` ({'MATCH' if pre_sha == PREPRINT_SHA else 'MISMATCH'} vs {PREPRINT_SHA[:8]}...{PREPRINT_SHA[-4:]}, the preprint of "
      f"record: patch v6, the PI's ruling 9 of 2026-10-10, as corrected). The block's "
      f"{PREPRINT_SHA_AUDITED[:8]}...{PREPRINT_SHA_AUDITED[-5:]} is the audited, "
      f"superseded text, archived untracked at `{PREPRINT_AUDITED_ARCHIVE}` (not required here; {aud_st}); its lines "
      f"are quoted from the raw of record `{RAW_REC[1]}`@{RAW_REC[0]}.")
    # the review cards (block :54, :59-60): the design handoffs that number them are untracked root files
    HAND = {}
    for hp_ in ("HANDOFF-2026-09-04-design.md", "HANDOFF-2026-09-13-design.md"):
        fp_ = os.path.join(REPO, hp_)
        if os.path.exists(fp_):
            with open(fp_, encoding="utf-8") as f:
                HAND[hp_] = f.read()
            o(f"- `{hp_}` (root, {'tracked' if git('ls-files', '--', hp_).strip() else 'UNTRACKED: absent from any clone'}; "
              f"read only) sha256 `{sha256_bytes(HAND[hp_].encode())}`")
        else:
            o(f"- `{hp_}`: absent on this machine")
    clone_files = ["scripts/e2a_sessions.py", "jlens_qwen/e2a.py", "scripts/f_sessions.py",
                   "scripts/e2a_g1_kernel_gate.py", "scripts/e2a_g2_discriminability.py",
                   "scripts/e2a_g2_spotcheck.py"]
    for p in clone_files:
        fp = os.path.join(REPO, CLONE, p)
        if os.path.exists(fp):
            o(f"- `{CLONE}/{p}` (gitignored clone, NOT in the record; read only) "
              f"sha256 `{sha256_file(fp)[:16]}`")
        else:
            o(f"- `{CLONE}/{p}`: absent on this machine")
    o()
    o("Analyzer of record for the published e2a figures: `jlens-qwen36/scripts/e2a_sessions.py "
      f"--analyze` (gitignored clone; {loc('scripts/e2a_recount.py', 'WHY THIS EXISTS.', 'This script closes that (rule 27).')} states the exclusion logic "
      "'lived only in the gitignored clone' until that script). The tracked reproduction path is "
      "`scripts/e2a_recount.py` (rule-27 provenance). Both are quoted below.")
    o()
    a_first = git("log", "--diff-filter=A", "--format=%h %ad", "--date=short",
                  PIN, "--", "data/e2a/analysis.json").decode().split("\n")[0]
    s_first = git("log", "--diff-filter=A", "--format=%h %ad", "--date=short",
                  PIN, "--", "data/e2a/sessions.jsonl").decode().split("\n")[0]
    o(f"- `data/e2a/analysis.json` first added at {a_first}; `data/e2a/sessions.jsonl` first "
      f"added at {s_first} (git log --diff-filter=A, read-only).")
    o()

    # ===================================================================== (i)
    o("## (i) The e2a primary: definition, counts, and the design seat's arithmetic")
    o()
    A = pinned_json("data/e2a/analysis.json")
    S = pinned_jsonl("data/e2a/sessions.jsonl")
    o("### (i-a) The definition, quoted from the code")
    o()
    o("Producing analyzer (gitignored clone), the per-session field and the arm statistic:")
    o()
    o("```")
    for q in quote_lines(f"{CLONE}/scripts/e2a_sessions.py", [
            'picked_pole = "pos" if picked == tag_plus else "neg"',
            'tag_plus, tag_minus = (pair[1], pair[0]) if swap else pair',
            'swap = (s // 4) % 2 == 1',
            '"first_free_pick_pos": (choices_log[0]["picked_pole"] == "pos"',
            'rows = [r for r in all_rows if not r.get("excluded")]',
            'firsts = [r["first_free_pick_pos"] for r in sub]',
            'd = float(np.mean(firsts)) - 0.5',
            'mm = [r["first_free_pick_pos"] for r in sub if r["swap"] == m]',
            'by_map["B" if m else "A"] = (round(float(np.mean(mm)) - 0.5, 4)',
            'p_binom = sum(comb(n, i) for i in range(k, n + 1)) / 2 ** n',
            '"binom_p_one_sided": round(p_binom, 5)',
            'pseudo = [abs(out[a]["delta_first"]) for a in',
            'c1 = out["reward"]["delta_first"] > (max(pseudo) if pseudo else 0)',
            'c2 = all(v is not None and v >= 0 for v in maps.values())',
            'c3 = out["reward"]["binom_p_one_sided"] < 0.05'], clone=True):
        o(q)
    o("```")
    o()
    o("Tracked reproduction (in the record):")
    o()
    o("```")
    for q in quote_lines("scripts/e2a_recount.py", [
            "def primary(audit):",
            "e2a's primary DV: share of VALID reward-arm sessions whose first free",
            "pick was the +pole label. 55/102 under the frozen audit; 54/101 under v2.",
            "valid = [s for s in ROWS if s['arm'] == 'reward' and exclusion(s, audit) is None]",
            "k = sum(1 for s in valid if s['first_free_pick_pos'])",
            'Delta_first = {k / n - 0.5:+.4f}']):
        o(q)
    o("```")
    o()
    o("**Definition of record.** Δ_first (field `delta_first`) = k/n − ½, where n = the arm's "
      "valid (non-excluded) sessions and k = those whose FIRST free choice picked the "
      "**+pole label** (`tag_plus`: the label whose rounds run +α along the arm's direction -- "
      "the +reward axis in the reward arm, the +random direction in random1/random2, and a "
      "designated label with no state in sham). Equivalently (approach − avoid)/(2n), not "
      "(approach − avoid)/n. Maps: A = `swap` False, B = `swap` True, swap = (s // 4) mod 2 "
      "(which label of the pair is +pole). p = exact one-sided binomial P(X ≥ k | n, ½), "
      "rounded to 5 decimals. Pre-registered wording: 'Δ = P(choose +pole) − 0.5 pooled over "
      "counterbalance maps' "
      f"({loc('archive/RESULTS-cycles3-4.md', 'session; Δ = P(choose +pole) − 0.5 pooled over counterbalance maps')}).")
    o()

    # recompute
    o("### (i-b) Counts per arm: analysis.json vs an independent recount from sessions.jsonl")
    o()
    o("| arm | launched | excluded | valid n | k (first pick +pole) | Δ_first = k/n − ½ | stored | map A k/n → Δ | map B k/n → Δ | stored maps | share_all_choices (recount / stored) | one-sided exact binomial P(X ≥ k; n, ½) (recount, 8 dp / stored 5 dp) | all fields match |")
    o("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    rec = {}
    all_match = True
    for arm in ARMS:
        rows = [r for r in S if r["arm"] == arm]
        val = [r for r in rows if not r["excluded"]]
        n = len(val)
        k = sum(1 for r in val if r["first_free_pick_pos"])
        d = r4(k / n - 0.5)
        mp = {}
        for m, name in ((False, "A"), (True, "B")):
            mm = [r for r in val if r["swap"] == m]
            km = sum(1 for r in mm if r["first_free_pick_pos"])
            mp[name] = (km, len(mm), r4(km / len(mm) - 0.5))
        ch = [c for r in val for c in r["choices"]]
        share = r4(sum(1 for c in ch if c["picked_pole"] == "pos") / len(ch))
        pex = p_ge_half(k, n)
        st = A[arm]
        match = (st["n"] == n and st["delta_first"] == d
                 and st["by_map"]["A"] == mp["A"][2] and st["by_map"]["B"] == mp["B"][2]
                 and st["share_all_choices"] == share
                 and st["binom_p_one_sided"] == round(pex, 5))
        all_match &= match
        rec[arm] = {"launched": len(rows), "excluded": len(rows) - n, "n": n, "k": k,
                    "delta_first": d, "map": {kk: list(v) for kk, v in mp.items()},
                    "share_all_choices": share, "p_exact": pex, "n_choices": len(ch),
                    "match_analysis_json": match}
        o(f"| {arm} | {len(rows)} | {len(rows) - n} | {n} | {k} | {k / n - 0.5:+.6f} → {d:+.4f} | "
          f"{st['delta_first']:+.4f} | {mp['A'][0]}/{mp['A'][1]} → {mp['A'][2]:+.4f} | "
          f"{mp['B'][0]}/{mp['B'][1]} → {mp['B'][2]:+.4f} | {st['by_map']['A']:+.4f} / {st['by_map']['B']:+.4f} | "
          f"{share:.4f} / {st['share_all_choices']:.4f} ({len(ch)} choices) | {pex:.8f} / {st['binom_p_one_sided']:.5f} | "
          f"{'YES' if match else 'NO'} |")
    o()
    o(f"Every field of `data/e2a/analysis.json` reproduces from `data/e2a/sessions.jsonl` "
      f"under the definition above: **{'YES' if all_match else 'NO'}**. Domain of every rate in "
      f"this table: valid sessions of the arm (excluded = the run's own `excluded` flag, the "
      f"frozen-audit rule at run time); share_all_choices is over all free choices of those "
      f"sessions.")
    o()
    if not all_match:
        STOPS.append({"subitem": "N4(i) recount", "discrepancy": "analysis.json does not reproduce from sessions.jsonl",
                      "suspected_cause": "see table"})

    # record analyzer, both audits
    os.chdir(REPO)
    if REPO not in sys.path:
        sys.path.insert(0, REPO)
    spec = importlib.util.spec_from_file_location("e2a_recount_ro", os.path.join(REPO, "scripts/e2a_recount.py"))
    rc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rc)
    spec2 = importlib.util.spec_from_file_location("habit_ro", os.path.join(REPO, "valence_core/e2d/habit.py"))
    habit = importlib.util.module_from_spec(spec2)
    spec2.loader.exec_module(habit)
    # every repository module actually imported must equal its pinned blob
    loaded = sorted({os.path.relpath(m.__file__, REPO) for m in list(sys.modules.values())
                     if getattr(m, "__file__", None) and os.path.abspath(m.__file__).startswith(REPO + os.sep)
                     and CLONE not in m.__file__} | {"scripts/e2a_recount.py", "valence_core/e2d/habit.py"})
    bad = [p for p in loaded if p != me_rel and not blob_equal_to_pin(p)]
    if bad:
        raise SystemExit(f"imported module differs from the pin: {bad}")
    IMPORTED_OK.extend(p for p in loaded if p != me_rel)
    kf, nf = rc.primary(rc.FROZEN)
    kv, nv = rc.primary(rc.V2)
    byf, polf, detf = rc.tally(rc.FROZEN)
    byv, polv, detv = rc.tally(rc.V2)
    pub = {s["session"]: s["exclude_reason"] for s in rc.ROWS if s["arm"] == "reward" and s["excluded"]}
    mine = {d[0]: d[1] for d in detf}
    same_set = set(mine) == set(pub) and all(pub[x] == mine[x] for x in pub)
    extra = sorted(set(d[0] for d in detv) - set(d[0] for d in detf))
    o("### (i-c) The record's own analyzer (`scripts/e2a_recount.py`, imported read-only)")
    o()
    o(f"- Repository modules imported (each asserted equal to its pinned blob): {', '.join(f'`{p}`' for p in IMPORTED_OK)}.")
    LN = {a: rec[a]["launched"] for a in ARMS}
    o(f"- Frozen audit (the published rule): reward excluded {byf['reward']}/{LN['reward']}, sham "
      f"{byf['sham']}/{LN['sham']}, random1 {byf['random1']}/{LN['random1']}, random2 {byf['random2']}/"
      f"{LN['random2']}; reward exclusion set and every reason "
      f"string identical to the stored `exclude_reason`s: {same_set}. Primary: **{kf}/{nf}**, "
      f"Δ_first = {kf / nf - 0.5:+.4f}, one-sided exact binomial p = {rc.binom_p_one_sided(kf, nf):.5f}.")
    o(f"- Audit v2 (`data/configs/e2b_audit_v2.json`): reward excluded {byv['reward']}/{LN['reward']} "
      f"(added: reward s{', s'.join(map(str, extra))}); sham {byv['sham']}/{LN['sham']}, random1 "
      f"{byv['random1']}/{LN['random1']}, random2 {byv['random2']}/{LN['random2']} (control arms "
      f"{'unchanged' if all(byv[a] == byf[a] for a in ARMS if a != 'reward') else 'CHANGED'}). Primary: **{kv}/{nv}**, "
      f"Δ_first = {kv / nv - 0.5:+.4f}, one-sided exact binomial p = {rc.binom_p_one_sided(kv, nv):.5f}.")
    s1 = next(r for r in S if r["arm"] == "reward" and r["session"] == 1)
    o(f"- The added session, reward s1: first free pick +pole = {s1['first_free_pick_pos']}, "
      f"map {'B' if s1['swap'] else 'A'}; v2 reason "
      f"`{next(d[1] for d in detv if d[0] == 1)}`. Record: "
      f"{loc('archive/RESULTS-cycles3-4.md', '> **CORRECTION (2026-08-21', 'below are unmodified; this addendum is the correction of record.')} "
      f"(the correction of record) and {loc('RESULTS.md', '55/102 and 54/101 now reproduce from committed artifacts')}; "
      f"raw `results/raw/2026-09-01_e2a_recount.txt`.")
    # map split under v2
    val_v2 = [s for s in S if s["arm"] == "reward" and rc.exclusion(s, rc.V2) is None]
    mpv = {}
    for m, name in ((False, "A"), (True, "B")):
        mm = [r for r in val_v2 if r["swap"] == m]
        km = sum(1 for r in mm if r["first_free_pick_pos"])
        mpv[name] = (km, len(mm), r4(km / len(mm) - 0.5))
    o(f"- Under v2 the reward maps are A {mpv['A'][0]}/{mpv['A'][1]} → {mpv['A'][2]:+.4f}, "
      f"B {mpv['B'][0]}/{mpv['B'][1]} → {mpv['B'][2]:+.4f} (computed-new).")
    o()

    # design seat's arithmetic
    o("### (i-d) The design seat's arithmetic")
    o()
    claims = [("reward", 55, 102, 0.0392, 0.24422), ("sham", 19, 37, 0.0135, None),
              ("random1", 15, 23, 0.1522, None), ("random2", 12, 22, 0.0455, None)]
    o("| arm | claimed k/n → Δ | recount k/n | Δ = k/n − ½ (4 dp) | one-sided exact p | verdict |")
    o("|---|---|---|---|---|---|")
    for arm, k, n, dd, pp in claims:
        rk, rn = rec[arm]["k"], rec[arm]["n"]
        ok = (rk, rn) == (k, n) and r4(k / n - 0.5) == dd and (pp is None or round(p_ge_half(k, n), 5) == pp)
        o(f"| {arm} | {k}/{n} → {dd:+.4f}{'' if pp is None else f', p = {pp}'} | {rk}/{rn} | {r4(rk / rn - 0.5):+.4f} | "
          f"{p_ge_half(rk, rn):.5f} | {'CONFIRMED' if ok else 'REFUTED'} |")
    pseudo = {a: abs(A[a]["delta_first"]) for a in ("sham", "random1", "random2")}
    big = max(pseudo, key=pseudo.get)
    o()
    o(f"- 'Largest pseudo-Δ' = max |Δ_first| over sham/random1/random2 as the analyzer computes it "
      f"(absolute values) = **{pseudo[big]:.4f} ({big}, n = {A[big]['n']})**: CONFIRMED.")
    p55 = p_ge_half(55, 102)
    o(f"- P(X ≥ 55 | 102, ½) = {p55:.8f} → {round(p55, 5)} at five decimals "
      f"{'=' if round(p55, 5) == A['reward']['binom_p_one_sided'] else '≠'} the stored "
      f"`reward.binom_p_one_sided` ({A['reward']['binom_p_one_sided']}): "
      f"{'CONFIRMED' if round(p55, 5) == A['reward']['binom_p_one_sided'] == 0.24422 else 'REFUTED'}.")
    o()
    o("Integrality test -- for each stored Δ, every integer k in [0, n] that reproduces it at 4 dp "
      "under each candidate definition (n = the stored arm or map n):")
    o()
    o("| field | n | stored | k under k/n − ½ | k under (approach − avoid)/n = (2k − n)/n | one-sided exact binomial P(X ≥ k; n, ½) for the (2k−n)/n k vs stored p |")
    o("|---|---|---|---|---|---|")
    integ = {}
    refuted_none = []
    for arm in ARMS:
        fields = [("pooled", rec[arm]["n"], A[arm]["delta_first"]),
                  ("map A", rec[arm]["map"]["A"][1], A[arm]["by_map"]["A"]),
                  ("map B", rec[arm]["map"]["B"][1], A[arm]["by_map"]["B"])]
        for nm, n, v in fields:
            ka = [k for k in range(n + 1) if r4(k / n - 0.5) == v]
            kb = [k for k in range(n + 1) if r4((2 * k - n) / n) == v]
            if kb:
                refuted_none.append(f"{arm} {nm}")
            pcol = ""
            if nm == "pooled" and kb:
                pcol = "; ".join(f"k={k}: {round(p_ge_half(k, n), 5)} vs {A[arm]['binom_p_one_sided']}" for k in kb)
            integ[f"{arm} {nm}"] = {"n": n, "stored": v, "k_share": ka, "k_diff_over_n": kb}
            o(f"| {arm} {nm} | {n} | {v:+.4f} | {ka if ka else 'none'} | {kb if kb else 'none'} | {pcol} |")
    o()
    o("- 'Every arm integer under share − ½': **CONFIRMED** (each pooled and map value has exactly one k).")
    rw_n = rec["reward"]["n"]
    rw_kb = integ["reward pooled"]["k_diff_over_n"]
    rw_ka = integ["reward pooled"]["k_share"]
    rw_st = A["reward"]["delta_first"]
    rw_sp = A["reward"]["binom_p_one_sided"]
    if refuted_none:
        if rw_kb:
            kb0 = rw_kb[0]
            eg = (f"-- e.g. the reward arm's {rw_st:+.4f} is also (2·{kb0} − {rw_n})/{rw_n} = "
                  f"{2 * kb0 - rw_n}/{rw_n} = {(2 * kb0 - rw_n) / rw_n:.6f}. Integrality alone does not "
                  f"discriminate the definitions on the reward arm; the stored p does (P(X ≥ {kb0} | {rw_n}, ½) = "
                  f"{p_ge_half(kb0, rw_n):.5f} ≠ {rw_sp}, while P(X ≥ {rw_ka[0]} | {rw_n}, ½) = "
                  f"{p_ge_half(rw_ka[0], rw_n):.5f}), and the code settles it (quoted above).")
            eg_note = (f": {rw_st:+.4f} = (2*{kb0}-{rw_n})/{rw_n}. The stored p ({rw_sp} = "
                       f"P(X>={rw_ka[0]}|{rw_n},1/2), not P(X>={kb0})={p_ge_half(kb0, rw_n):.5f}) and the "
                       f"analyzer's code fix the definition as k/n - 1/2.")
        else:
            eg = "-- the reward pooled value is not among them, so the stored p and the code are not needed to tell them apart there."
            eg_note = "."
        o(f"- 'None integer under (approach − avoid)/n': **REFUTED for {', '.join(refuted_none)}** {eg}")
        NOTES.append("Design seat's claim 'none [integer] under (approach - avoid)/n' is refuted for "
                     + ", ".join(refuted_none) + eg_note
                     + " This is the design seat's arithmetic, not a record figure: under block :3 it is a note, "
                       "not an (i) discrepancy under :62 (see STOPs).")
    else:
        o("- 'None integer under (approach − avoid)/n': CONFIRMED.")
    o()

    # preprint reconciliation
    o("### (i-e) The two preprint sentences")
    o()
    with open(pre_path, encoding="utf-8") as f:
        pre = f.read()
    pl = pre.split("\n")
    def pre_hits(nd):
        return lines_with(pre, nd)
    # the block's other preprint referent (N1, block :21): the project copy v1.1
    v11 = sorted(os.path.relpath(os.path.join(dp, fn), REPO)
                 for dp, dn, fns in os.walk(REPO)
                 if CLONE not in os.path.relpath(dp, REPO).split(os.sep)
                 and ".git" not in os.path.relpath(dp, REPO).split(os.sep)
                 for fn in fns if fn.startswith("PREPRINT-v1_1"))
    v11_loc = loc(BLOCK, "PREPRINT-v1_1-draft.md (project copy)")
    pf_loc = loc("results/raw/2026-10-08_note-preflight.md", "| `PREPRINT-v1_1-draft.md` | MISSING")
    pf_rn = loc("results/raw/2026-10-08_note-preflight.md", "| `RESEARCH-NOTE-v0_2-draft.md` | MISSING")
    pf_both = f"{pf_rn.split(':')[0]}:{pf_rn.split(':')[-1]} (RESEARCH-NOTE v0.2), :{pf_loc.split(':')[-1]} (v1.1)"
    # the other preprint copies on this machine (untracked; read only): the pre-patch v2/v3/v4 under archive/, and
    # (round 9) the pre-patch v6 copy, the audited text, when present
    prepatch = sorted(os.path.relpath(os.path.join(REPO, "archive", fn), REPO)
                      for fn in os.listdir(os.path.join(REPO, "archive"))
                      if fn.startswith("PREPRINT-v1_0-draft.pre-patch-") and fn.endswith(".md"))
    pp_hits = {}
    for pp in prepatch:
        with open(os.path.join(REPO, pp), encoding="utf-8") as f:
            t_ = f.read()
        pp_hits[pp] = {"sha256_16": sha256_bytes(t_.encode())[:16],
                       "tracked": bool(git("ls-files", "--", pp).strip()),
                       "54 of 101 valid sessions": lines_with(t_, "54 of 101 valid sessions"),
                       "half the difference": lines_with(t_, "half the difference"),
                       "54 of 101": lines_with(t_, "54 of 101"), "55 of 102": lines_with(t_, "55 of 102")}
    pp_none = all(not v["54 of 101 valid sessions"] and not v["half the difference"] for v in pp_hits.values())
    pp_desc = "; ".join(f"`{p}` ({'tracked' if v['tracked'] else 'untracked'}, sha256 {v['sha256_16']}): "
                        f"'54 of 101 valid sessions' {v['54 of 101 valid sessions'] or 'NO MATCH'}, 'half the "
                        f"difference' {v['half the difference'] or 'NO MATCH'}, '55 of 102' at {v['55 of 102']}, "
                        f"'54 of 101' at {v['54 of 101']}" for p, v in pp_hits.items())
    pp_short = "/".join(p.rsplit('-', 1)[-1].replace('.md', '') for p in pp_hits)
    app_planned = pre_hits("*Appendices (planned):")
    # round 9: 'Appendix X of <work>' cites another work's appendix (patched :162, arXiv:2603.21396), not this preprint's
    app_refs = {L_: sorted(set(re.findall(r"Appendix ([A-Z])\b(?! of )", pl[L_ - 1]))) for L_ in pre_hits("Appendix ")}
    app_ext = [L_ for L_ in app_refs if re.search(r"Appendix [A-Z] of ", pl[L_ - 1])]
    # a line whose only appendix citations are another work's is not counted; any other line stays as at HEAD
    app_refs = {L_: v for L_, v in app_refs.items() if v or L_ not in app_ext}
    app_refs_s = "; ".join(":%d: Appendix %s" % (k, ", ".join(v)) for k, v in app_refs.items())
    heads = [i for i, l in enumerate(pl, 1) if l.startswith("#")]
    has_app_heading = any("Appendix" in pl[i - 1] for i in heads)
    o(f"- Scope of this check: of the block's preprint referents only `{PREPRINT}` (root, the preprint of record: "
      f"patch v6, sha256 {pre_sha[:8]}..., which replaced the block's post-patch-v4 copy {PREPRINT_SHA_AUDITED[:8]}..., "
      f"the audited text) is on this machine. `PREPRINT-v1_1-draft.md`, the block's 'project copy' ({v11_loc}), is absent "
      f"(files found by that name under the repo, clone and .git excluded: {v11 if v11 else 'none'}), and so is "
      f"RESEARCH-NOTE v0.2 (preflight {pf_both}); a sentence the block attributes to 'the preprint' may live in "
      f"either and cannot be checked here. {('One', 'Two', 'Three', 'Four', 'Five', 'Six')[len(pp_hits) - 1] if 1 <= len(pp_hits) <= 6 else len(pp_hits)} "
      f"earlier copies of v1.0 are also on this machine and were searched "
      f"for both phrases: {pp_desc}.")
    o(f"- `{PREPRINT}` cites appendices by letter ({app_refs_s}) but carries no appendix text: no heading names an "
      f"appendix ({'one does' if has_app_heading else 'none of its ' + str(len(heads)) + ' headings'}), its last "
      f"heading is :{heads[-1]} '{pl[heads[-1] - 1]}', and its line :{app_planned[0] if app_planned else '?'} "
      f"begins '*Appendices (planned):'. So the preprint's own statements of the identity (Appendix C, cited at "
      f":{','.join(str(k) for k, v in app_refs.items() if 'C' in v)}) and of the cached-generation disclosure "
      f"(Appendix D, which :{','.join(str(k) for k, v in app_refs.items() if 'D' in v and 'cached path' in pl[k - 1])} "
      f"cites for it) cannot be checked."
      + (f" Not counted: another work's appendix ('Appendix X of ...') at :{','.join(map(str, app_ext))}." if app_ext else ""))
    h54v = pre_hits("54 of 101 valid sessions")
    h54 = pre_hits("54 of 101")
    h55 = pre_hits("55 of 102 valid sessions")
    h55r = h55 or pre_hits("55 of 102")   # round 9: the audited anchor is gone from the patched text; re-anchored
    hhalf = pre_hits("half the difference")
    hbreak = pre_hits("break rate")
    o(f"- grep `{PREPRINT}` (sha256 {pre_sha[:16]}): '54 of 101 valid sessions' → "
      f"{h54v if h54v else 'NO MATCH'}; '54 of 101' → lines {h54}; '55 of 102 valid sessions' → lines {h55}"
      + ("" if h55 else f" ('55 of 102' → lines {h55r})") + "; "
      f"'half the difference' → {hhalf if hhalf else 'NO MATCH'}; 'break rate' → lines {hbreak}.")
    for n_ in sorted(set(h54 + h55r)):
        txt = pl[n_ - 1]
        if n_ in h54:
            o(f"  - :{n_}: \"{sentence_at(txt, '54 of 101')}\"")
        if n_ in h55r:
            o(f"  - :{n_}: \"{sentence_at(txt, '55 of 102')}\"")
    for n_ in hbreak:
        o(f"  - :{n_}: \"{sentence_at(pl[n_ - 1], 'break rate')}\"")
    o()
    # the preprint's footnote numbers, read from its text and compared with the recount
    fn_txt = pl[h54[0] - 1] if h54 else ""
    fn_d = re.search(r"54 of 101, Δ = ([+−-]\d\.\d+), p = (\d\.\d+)", fn_txt)
    pre_fd = float(fn_d.group(1).replace("−", "-")) if fn_d else None
    pre_fp = float(fn_d.group(2)) if fn_d else None
    nd_d = len(fn_d.group(1).split(".")[1]) if fn_d else 3
    nd_p = len(fn_d.group(2).split(".")[1]) if fn_d else 3
    fn_ok = (fn_d is not None and round(kv / nv - 0.5, nd_d) == pre_fd
             and round(rc.binom_p_one_sided(kv, nv), nd_p) == pre_fp)
    corr_loc = loc('archive/RESULTS-cycles3-4.md', '> **CORRECTION (2026-08-21',
                   'below are unmodified; this addendum is the correction of record.')
    # round 9 (ruling 9): a failed footnote check on the patched text is a finding on the patch, not a STOP
    aud_form = bool(h55) and fn_d is not None   # the audited layout: primary 55/102, footnote 54/101 with Δ and p
    h54s, h55s = ",".join(map(str, h54)) or "?", ",".join(map(str, h55r)) or "?"
    def pq(n_, nd_):
        l_ = pl[n_ - 1]
        return {"locator": f"{PREPRINT}:{n_}", "quote": l_ if len(l_) <= 600 else sentence_at(l_, nd_, 2000)}
    # round 9, fix round: the figures the patched lines print, parsed and compared (whatever the layout)
    def fig_at(n_, X):
        l_ = pl[n_ - 1]
        m_d = (re.search(r"([+−-]\d*\.\d+) \(" + re.escape(X), l_)
               or re.search(re.escape(X) + r"[^Δ]{0,20}Δ = ([+−-]\d*\.\d+)", l_))
        m_p = re.compile(r"\bp = (\d*\.\d+)").search(l_, l_.find(X))
        return (m_d.group(1) if m_d else None), (m_p.group(1) if m_p else None)
    fig_cmp, fig_all = [], True
    for X, hs, dv, pv in ((f"{kv} of {nv}", h54, kv / nv - 0.5, rc.binom_p_one_sided(kv, nv)),
                          (f"{rec['reward']['k']} of {rec['reward']['n']}", h55r, A['reward']['delta_first'],
                           A['reward']['binom_p_one_sided'])):
        d_, p_ = fig_at(hs[0], X) if hs else (None, None)
        ok_ = d_ is not None and p_ is not None and eq_printed(d_, dv) and eq_printed(p_, pv)
        fig_all = fig_all and ok_
        fig_cmp.append(f"{X} at :{hs[0] if hs else '?'}: Δ = {d_ or 'NOT PARSED'} vs {dv:+.4f}, p = "
                       f"{p_ or 'NOT PARSED'} vs {pv:.5f} ({'equal' if ok_ else 'NOT equal'})")
    on_fn = lambda hs: bool(hs) and pl[hs[0] - 1].startswith("¹")
    lay_ = (f"the correction of record ({kv} of {nv}) is the primary and the verdict as published "
            f"({rec['reward']['k']} of {rec['reward']['n']}) is footnote 1, the reverse of the audited text"
            if on_fn(h55r) and not on_fn(h54) else
            f"{kv} of {nv} on a footnote line: {'yes' if on_fn(h54) else 'no'}; {rec['reward']['k']} of "
            f"{rec['reward']['n']} on a footnote line: {'yes' if on_fn(h55r) else 'no'}")
    pf1_figs = (f"figures on the patched lines equal the record at their printed precision: "
                f"{'YES' if fig_all else 'NO'} ({'; '.join(fig_cmp)}); layout: {lay_}")
    pf1 = None if (aud_form and fn_ok) else patch_finding(
        "N4(i-e): the e2a primary is found by '55 of 102 valid sessions', and footnote 1 (the line carrying "
        "'54 of 101') reads '54 of 101, Δ = …, p = …' equal to the audit-v2 recount at its printed precision",
        [rec_line("Reward Δ = +0.039 (55 of 102 valid sessions)"), rec_line("¹ A later audit excluded one session")],
        [pq(n_, "54 of 101") for n_ in h54] + [pq(n_, "55 of 102") for n_ in h55r if n_ not in h54],
        f"audit-v2 recount (scripts/e2a_recount.py) {kv}/{nv}, Δ_first = {kv / nv - 0.5:+.4f}, one-sided exact "
        f"binomial p = {rc.binom_p_one_sided(kv, nv):.5f}; as published (data/e2a/analysis.json) {rec['reward']['k']}/"
        f"{rec['reward']['n']}, Δ_first = {A['reward']['delta_first']:+.4f}, p = {A['reward']['binom_p_one_sided']:.5f}",
        pf1_figs)
    if aud_form:
        carries = (f"it carries {rec['reward']['k']} of {rec['reward']['n']} as the published primary (:{h55[0]}) and "
                   f"54 of 101 in footnote 1 (:{h54[0] if h54 else '?'}) with its own Δ = {fn_d.group(1)} and p = "
                   f"{fn_d.group(2)}. Those reproduce from the record's analyzer under audit v2: {kv}/{nv}, "
                   f"Δ_first = {kv / nv - 0.5:+.4f}, p = {rc.binom_p_one_sided(kv, nv):.5f} (equal to the footnote at "
                   f"its printed precision: {'YES' if fn_ok else 'NO; finding on the patch ' + pf1 + ', below'})")
    else:
        # recheck fix: name the conjunct(s) that actually fail (aud_form False: the primary anchor and/or the footnote form)
        why_ = " and ".join(w_ for w_ in (
            None if h55 else "the primary anchor '55 of 102 valid sessions' is absent",
            None if fn_ok else ("the footnote form '54 of 101, Δ = …, p = …' is absent" if fn_d is None else
                                "the footnote check fails")) if w_)
        carries = (f"on this patched text '54 of 101' is at :{h54s} and '55 of 102' at :{h55s}, and the check fails "
                   f"({why_}; finding on the patch {pf1}, below; the figures those lines print equal the record at "
                   f"their printed precision: {'YES' if fig_all else 'NO'}). The record's analyzer under audit v2 gives {kv}/{nv}, "
                   f"Δ_first = {kv / nv - 0.5:+.4f}, p = {rc.binom_p_one_sided(kv, nv):.5f}")
    vs_ = pre_hits("valid sessions")
    o(f"**'54 of 101'.** `{PREPRINT}` does not say '54 of 101 valid sessions'; {carries}. It is not a transcription error and is not meant to "
      f"reproduce {A['reward']['delta_first']:+.3f} or {A['reward']['binom_p_one_sided']:.3f}: it is the later "
      f"audit's recount (one more reward session, s{', s'.join(map(str, extra))}, excluded on a banner-terminator "
      f"round the frozen fragments missed), recorded as the correction of record ({corr_loc}). Under no "
      f"definition does 54/101 give {A['reward']['delta_first']:+.3f}: k/n − ½ = {54 / 101 - 0.5:+.4f}; "
      f"(2k − n)/n = {(2 * 54 - 101) / 101:+.4f}. The block's quotation ('54 of 101 valid sessions') is in none "
      f"of the {1 + len(pp_hits)} preprint copies on this machine ({PREPRINT} and the pre-patch "
      f"{'/'.join(p.rsplit('-', 1)[-1].replace('.md', '') for p in pp_hits)} copies: "
      f"{'none carries it' if pp_none else 'SEE ABOVE'}); `PREPRINT-v1_1-draft.md` (the block's project copy) and "
      f"RESEARCH-NOTE v0.2 are absent ({pf_both}), so its source cannot be checked here. In `{PREPRINT}` the "
      f"phrase 'valid sessions' attaches to "
      + (f"{rec['reward']['k']} of {rec['reward']['n']}." if h55 else f"neither figure (its lines: {vs_})."))
    NOTES.append(f"'54 of 101 valid sessions' is not in {PREPRINT} (sha {pre_sha[:8]}...). That file has "
                 + (f"{rec['reward']['k']} of {rec['reward']['n']} valid sessions at :{h55[0]} and "
                    f"'54 of 101, Δ = {fn_d.group(1)}, p = {fn_d.group(2)}' as footnote 1 at :{h54[0] if h54 else '?'}"
                    if aud_form else f"54 of 101 at :{h54s} (and 55 of 102 at :{h55s}; finding on the patch {pf1})")
                 + f" -- the audit-v2 recount ({corr_loc}, the correction of "
                 f"record), reproduced here by scripts/e2a_recount.py. Not a transcription error. The quotation is "
                 f"also absent from the untracked pre-patch copies {', '.join(pp_hits)} "
                 f"({'none carries it' if pp_none else 'SEE (i-e)'}). Its source is not on this machine: "
                 f"PREPRINT-v1_1-draft.md (the block's project copy, {v11_loc}) and RESEARCH-NOTE v0.2 are both "
                 f"absent ({pf_both}); either may carry the sentence.")
    o()
    # round 9, fix round: the 'break rate' sentence this paragraph and the habit reading describe, located by text
    HB_Q = ("within an arm", "weighted by which label the habit leads toward", "Appendix C")
    hb_ok = bool(hbreak) and all(q_ in pl[hbreak[0] - 1] for q_ in HB_Q)
    pf_hb = None if hb_ok else patch_finding(
        "N4(i-e): the preprint's 'break rate' sentence is a within-arm decomposition ('within an arm ... weighted by "
        "which label the habit leads toward') with a pointer to Appendix C",
        [rec_line("the first-choice share decomposes into the habit's break rate weighted by which label")],
        [pq(n_, "break rate") for n_ in hbreak],
        "the identity of record, valence_core/e2d/habit.py (quoted in (i-e)): within ONE arm, weighted by forced-end pole")
    # habit identity
    o("**'Δ_first is half the difference between the state and sham arms' break rates'.** That "
      f"sentence is not in `{PREPRINT}` either (no match for 'half the difference'), nor in the pre-patch copies "
      f"({'none carries it' if pp_none else 'SEE ABOVE'}); v1.1 and RESEARCH-NOTE v0.2 are absent. That file's "
      f"sentence (:{hbreak[0] if hbreak else '?'}) is a within-arm decomposition with a pointer to "
      "Appendix C" + ("" if hb_ok else f" in the audited text (not on the patched text: finding on the patch {pf_hb}, below)")
      + ". The identity of record is in `valence_core/e2d/habit.py`:")
    o()
    o("```")
    for q in quote_lines("valence_core/e2d/habit.py", [
            "b+  = break rate in sessions where the habit leads AWAY from the +label",
            "bs  = break rate in sessions where the habit leads TOWARD the +label",
            "1/2 * (b+ + (1 - bs)), so",
            "**Delta_first = 1/2 * (b+ - bs)**",
            "P(+) = n+/N * b+ + ns/N * (1 - bs). The distinction earns its keep: on e2a's",
            "actual 53/49 split the balanced form gives +0.0528 where the measured primary"]):
        o(q)
    o("```")
    o()
    o("Here 'bs' is the break rate in sessions whose last forced round was the −pole "
      "(the 's' names the non-+ label, which habit.py calls the 'sham label'); both rates are "
      "within ONE arm, split by forced-end pole. Computed (valid sessions; `habit.break_rates` "
      "and an independent count agree):")
    o()
    o("| arm | forced-end + : breaks/n = b+ | forced-end − : breaks/n = bs | ½(b+ − bs) (balanced form) | weighted form n+/N·b+ + n−/N·(1−bs) − ½ | measured Δ_first |")
    o("|---|---|---|---|---|---|")
    hab = {}
    for arm in ARMS:
        val = [r for r in S if r["arm"] == arm and not r["excluded"]]
        br = habit.break_rates(val)
        # independent count
        bp = [habit.last_forced_pole(r) == habit.first_pick_pole(r) for r in val if habit.last_forced_pole(r) == "pos"]
        bn = [habit.last_forced_pole(r) == habit.first_pick_pole(r) for r in val if habit.last_forced_pole(r) == "neg"]
        assert (sum(bp), len(bp), sum(bn), len(bn)) == (br["b_plus"]["breaks"], br["b_plus"]["n"], br["b_sham"]["breaks"], br["b_sham"]["n"])
        hab[arm] = {"b_plus": [sum(bp), len(bp)], "b_minus": [sum(bn), len(bn)],
                    "balanced": br["delta_first_balanced_form"], "weighted": br["delta_first_weighted_form"]}
        o(f"| {arm} | {sum(bp)}/{len(bp)} = {sum(bp) / len(bp):.4f} | {sum(bn)}/{len(bn)} = {sum(bn) / len(bn):.4f} | "
          f"{br['delta_first_balanced_form']:+.4f} | {br['delta_first_weighted_form']:+.4f} | {A[arm]['delta_first']:+.4f} |")
    o()
    # literal between-arm reading
    def brk(arm):
        val = [r for r in S if r["arm"] == arm and not r["excluded"]]
        b = [habit.follows_habit(r) is False for r in val if habit.follows_habit(r) is not None]
        return sum(b), len(b)
    brw, brs = brk("reward"), brk("sham")
    lit = 0.5 * (brw[0] / brw[1] - brs[0] / brs[1])
    rwd = A["reward"]["delta_first"]
    assert r4(hab["reward"]["weighted"]) == rwd
    hab31 = loc("valence_core/e2d/habit.py", "Either way the primary IS a break-rate difference, halved.")
    hab37 = loc("valence_core/e2d/habit.py", "RULE 11. The decomposition is algebra, not a finding, and the e2a rates that",
                "motivate it are post-hoc on committed data.")
    pj = loc("PROPOSAL-j-dose-escalation.md", "forced-end counterbalancing **Δ_first = ½·(b₊ − bₛ)**, the break-rate",
             "difference when the habit leads away from vs toward the +label.")
    o("The record's own one-line wordings of the identity:")
    o()
    o("```")
    for q in quote_lines("valence_core/e2d/habit.py", ["Either way the primary IS a break-rate difference, halved.",
                                                      "RULE 11. The decomposition is algebra, not a finding, and the e2a rates that",
                                                      "motivate it are post-hoc on committed data."]):
        o(q)
    for q in quote_lines("PROPOSAL-j-dose-escalation.md", ["forced-end counterbalancing **Δ_first = ½·(b₊ − bₛ)**, the break-rate",
                                                          "difference when the habit leads away from vs toward the +label."]):
        o(q)
    o("```")
    o()
    o(f"Literal reading of the block's sentence (between arms): first-pick habit-break rate, valid "
      f"sessions, reward {brw[0]}/{brw[1]} = {brw[0] / brw[1]:.4f}, sham {brs[0]}/{brs[1]} = "
      f"{brs[0] / brs[1]:.4f}; ½ × (reward − sham) = **{lit:+.4f}**, which is not Δ_first "
      f"({rwd:+.4f}). **Classification:** as the block words it ('between the state and sham ARMS'), an "
      f"error; the record's statement is an algebraic identity WITHIN an arm (b+ and bs split by "
      f"forced-end pole), exact only under exact forced-end balance (reward arm: "
      f"{hab['reward']['b_plus'][1]}/{hab['reward']['b_minus'][1]}, so ½(b+ − bs) = "
      f"{hab['reward']['balanced']:+.4f} against the measured {rwd:+.4f}; the weighted form reproduces it, "
      f"{hab['reward']['weighted']:+.4f}). It is a mechanism gloss, not the definition: the definition "
      f"is k/n − ½ (i-a). The record's closest one-line wordings are habit.py's 'Either way the primary IS a "
      f"break-rate difference, halved.' ({hab31}) and PROPOSAL-j's 'Δ_first = ½·(b₊ − bₛ), the break-rate "
      f"difference' ({pj}); habit.py:{hab31.split(':')[-1]}'s 'either way' overstates, since the halved difference is exact only under "
      f"balance (the weighted form is the exact one, as habit.py itself says at "
      f"{loc('valence_core/e2d/habit.py', 'and at any other balance the exact statement is the weighted one,')}). The 'bₛ' / "
      f"'sham label' naming (the non-+ label within the arm) is a likely origin of a between-arms misreading. "
      f"habit.py calls the decomposition algebra, not a finding, and the motivating e2a rates post-hoc (rule 11, "
      f"{hab37}). The preprint's :{hbreak[0] if hbreak else '?'} wording ('within an arm ... weighted by which "
      f"label the habit leads toward') matches the weighted form"
      + ("." if hb_ok else f" in the audited text (finding on the patch {pf_hb}, below)."))
    NOTES.append("'Δ_first is half the difference between the state and sham arms' break rates' is not in "
                 f"{PREPRINT} nor in the pre-patch {pp_short} copies (no 'half the difference'; PREPRINT-v1_1-draft.md "
                 f"and RESEARCH-NOTE v0.2, where it may live, are absent, {pf_both}). The "
                 f"record's identity ({loc('valence_core/e2d/habit.py', 'b+  = break rate in sessions where the habit leads AWAY', 'P(+) = n+/N * b+ + ns/N * (1 - bs).')}) is "
                 "WITHIN an arm, split by forced-end pole; ½(b+ − bs) is exact only at forced-end balance (reward "
                 f"{hab['reward']['b_plus'][1]}/{hab['reward']['b_minus'][1]}: balanced {hab['reward']['balanced']:+.4f}, "
                 f"weighted {hab['reward']['weighted']:+.4f} = measured). The literal between-arm reading gives {lit:+.4f}. "
                 f"The record's own short wordings ({hab31}; {pj}) state the halved difference without the balance "
                 "condition; the note should state the weighted form or name the condition.")
    o()

    # map-level, intervals, habit, sizes
    o("### (i-f) Map-level figures, the approach-probability interval, the first-pick habit, the control-arm sizes")
    o()
    for arm in ("reward", "sham"):
        mA, mB = rec[arm]["map"]["A"], rec[arm]["map"]["B"]
        o(f"- {arm}: map A {mA[0]}/{mA[1]} → {mA[2]:+.4f}; map B {mB[0]}/{mB[1]} → {mB[2]:+.4f} "
          f"(stored {A[arm]['by_map']['A']:+.4f} / {A[arm]['by_map']['B']:+.4f}); domain: valid {arm} sessions per map.")
    o()
    o("Interval for P(first free pick = +pole) in the reward arm, 95% two-sided:")
    o()
    o("| k/n | method | interval (4 dp) | at 2 dp | gives [.44, .64]? |")
    o("|---|---|---|---|---|")
    ivs = {}
    for k, n in ((55, 102), (54, 101)):
        for name, fn in (("Wilson score", wilson), ("Clopper-Pearson exact", clopper_pearson), ("Wald", wald)):
            lo, hi = fn(k, n)
            g = (round(lo, 2), round(hi, 2)) == (0.44, 0.64)
            ivs[f"{k}/{n} {name}"] = [lo, hi]
            o(f"| {k}/{n} | {name} | [{lo:.4f}, {hi:.4f}] | [{lo:.2f}, {hi:.2f}] | {'yes' if g else 'no'} |")
    o()
    f3 = loc("FINDINGS-3.md", "(P(+) interval ≈ .44–.64)")
    # the method search, run here (read-only git grep at the pin)
    def grep_pin(pat: str) -> list[str]:
        """read-only `git grep -n -F` at the pin over prose/log files; the audit block and this
        audit's own 2026-10-08 raws are excluded (they quote the figure)."""
        r = subprocess.run(["git", "--no-optional-locks", "-C", REPO, "grep", "-n", "-F", pat, PIN, "--",
                            "*.md", "*.txt", f":(exclude){BLOCK}", ":(exclude)results/raw/2026-10-08_*"],
                           capture_output=True, text=True)
        return [l[len(PIN) + 1:] for l in r.stdout.split("\n") if l]
    both = [l for l in grep_pin(".44") if ".64" in l]
    both_loc = [":".join(l.split(":")[:2]).replace(":", f"@{PIN}:", 1) for l in both]
    meth_near = [l for p_ in ("Wilson", "Clopper", "Wald") for l in grep_pin(p_) if (".44" in l or ".64" in l)]
    meth_loc = [":".join(l.split(":")[:2]).replace(":", f"@{PIN}:", 1) for l in meth_near]
    wi, cp_, wd = ivs["55/102 Wilson score"], ivs["55/102 Clopper-Pearson exact"], ivs["55/102 Wald"]
    def iv2(x):
        return f"[{x[0]:.2f}, {x[1]:.2f}]"
    # round 9 (ruling 9): the preprint's interval sentence, found by its text; re-anchored if the patch reworded it
    IV_Q = "P(approach) ∈ ≈ [.44, .64]"
    h_iv = pre_hits(IV_Q)
    h_ivr = h_iv or pre_hits("interval on the approach probability")
    # fix round: the interval the patched line prints, parsed and matched against this run's intervals at its precision
    iv_l = sentence_at(pl[h_ivr[0] - 1], "approach probability", 2000) if h_ivr else ""
    iv_m = re.search(r"\[(\d*\.\d+), (\d*\.\d+)\]", iv_l)
    if iv_m:
        iv_eq = [k_ for k_, v_ in ivs.items() if eq_printed(iv_m.group(1), v_[0]) and eq_printed(iv_m.group(2), v_[1])]
        iv_meth = [m_ for m_ in ("Wilson", "Clopper", "Wald", "exact") if m_ in iv_l]
        # recheck fix: the committed computed-new Wilson intervals (the artifact patched footnote 1 cites), read at
        # their commit and compared with the patched interval at its printed precision and with this run's Wilson
        cor_ = json.loads(git("show", f"{COR_REC[0]}:{COR_REC[1]}").decode("utf-8"))
        cor_raw = git("show", f"{COR_REC[0]}:{COR_REC[2]}").decode("utf-8")
        cor_st = [v_ for k_, v_ in cor_["status"].items() if "computed_new.wilson95_share" in k_]
        cor_st = cor_st[0].split(":")[0] if cor_st else "NOT FOUND"
        cor_2b = lines_with(cor_raw, "### 2(b) Wilson 95% intervals")
        cor_cited = pre_hits(COR_REC[1])
        cor_cmp = []
        for key_, (k_, n_), row_ in (("of_record", (kv, nv), "| reward (of record) | "),
                                     ("as_published", (rec['reward']['k'], rec['reward']['n']), "| reward (as published) | ")):
            r_ = cor_[key_]["reward"]
            assert (r_["k_plus_pole_first_pick"], r_["n_valid"]) == (k_, n_), (key_, r_, k_, n_)
            w_ = r_["computed_new"]["wilson95_share"]
            hr_ = lines_with(cor_raw, f"{row_}{k_}/{n_} | [")
            eq_p = eq_printed(iv_m.group(1), w_[0]) and eq_printed(iv_m.group(2), w_[1])
            eq_r = all(abs(a_ - b_) < 1e-12 for a_, b_ in zip(w_, wilson(k_, n_)))
            cor_cmp.append(f"{k_}/{n_} ({key_}.reward.computed_new.wilson95_share) [{w_[0]:.4f}, {w_[1]:.4f}] "
                           f"(raw :{hr_[0] if hr_ else '?'}; equal to this run's Wilson on {k_}/{n_}: "
                           f"{'YES' if eq_r else 'NO'}): the patched interval equals it at its printed precision: "
                           f"{'YES' if eq_p else 'NO'}")
        cor_s = (f"the committed computed-new Wilson 95% intervals on the share, `{COR_REC[1]}`@{COR_REC[0]} (status in "
                 f"that file: {cor_st}; cited by the patched text at :{','.join(map(str, cor_cited)) or 'NONE'}; its "
                 f"raw `{COR_REC[2]}`@{COR_REC[0]} §2(b) at :{cor_2b[0] if cor_2b else '?'}): " + "; ".join(cor_cmp))
        iv_figs = (f"the patched interval [{iv_m.group(1)}, {iv_m.group(2)}] equals at its printed precision: "
                   f"{'; '.join(iv_eq) if iv_eq else 'none of them'}; and does not equal: "
                   f"{'; '.join(k_ for k_ in ivs if k_ not in iv_eq) or 'none'}; the record figure .44–.64 ({f3}): "
                   f"{'equal' if (iv_m.group(1), iv_m.group(2)) == ('.44', '.64') else 'NOT equal'}; {cor_s}; "
                   f"method named in the patched sentence: {', '.join(iv_meth) if iv_meth else 'none'}")
    else:
        iv_figs = "no bracketed interval parsed on the patched line"
    pf_iv = None if h_iv else patch_finding(
        f"N4(i-f): the preprint states the approach-probability interval as '{IV_Q}'",
        [rec_line("Power excludes medium-and-larger effects (P(approach) ∈ ≈ [.44, .64])")],
        [pq(n_, "approach probability") for n_ in h_ivr],
        "95% two-sided intervals, this run's (i-f) table at 2 dp: " + "; ".join(f"{k_} {iv2(v_)}" for k_, v_ in ivs.items())
        + f"; the record figure: {f3} ('P(+) interval ≈ .44–.64')", iv_figs)
    iv_at = (f":{h_iv[0]}" if h_iv else
             f":{','.join(map(str, h_ivr)) or '?'}, which no longer carries '{IV_Q}' (finding on the patch {pf_iv}, below)")
    o(f"- The record states the interval without a method: {f3} ('P(+) interval ≈ .44–.64'); preprint "
      + (f"{iv_at} ('{IV_Q}')" if h_iv else iv_at) + ". Search run here (git grep -F at the pin over "
      f"*.md and *.txt, the block and the 2026-10-08 raws excluded): lines carrying both '.44' and '.64': "
      f"{both_loc} (read: only the {f3.split('@')[0]} line states this interval; the others carry other numbers "
      f"that contain the digit strings); lines naming Wilson, Clopper or Wald beside "
      f"'.44' or '.64': {meth_loc if meth_loc else 'none'} (read: a column header of the S1 judge-cell table, not "
      f"this interval). No committed log line found names the method. "
      f"The design seat's guess, Wilson on {rec['reward']['k']}/{rec['reward']['n']}, gives "
      f"[{wi[0]:.4f}, {wi[1]:.4f}] = **{iv2(wi)}**{'' if iv2(wi) == '[0.44, 0.64]' else ', not [.44, .64]'}. "
      f"Clopper-Pearson [{cp_[0]:.4f}, {cp_[1]:.4f}] → {iv2(cp_)} and Wald [{wd[0]:.4f}, {wd[1]:.4f}] → {iv2(wd)}. "
      f"Which one the record used cannot be determined; the note should name a method (Clopper-Pearson is the "
      f"exact one{' and matches' if iv2(cp_) == '[0.44, 0.64]' else ''}). As a record figure at its printed "
      f"precision, ≈ [.44, .64] {'reproduces' if '[0.44, 0.64]' in (iv2(cp_), iv2(wd)) else 'DOES NOT reproduce'} "
      f"from {rec['reward']['k']}/{rec['reward']['n']} (status reproduced, under Clopper-Pearson or Wald); the "
      f"block's method attribution (Wilson) is the design seat's and does not.")
    NOTES.append(f"The approach-probability interval ≈ [.44, .64] (a record figure, reproduced at 2 dp under "
                 f"Clopper-Pearson and Wald) has no stated method in the record ({f3}; "
                 f"preprint {iv_at}). Wilson 95% on {rec['reward']['k']}/{rec['reward']['n']} = "
                 f"[{wi[0]:.4f}, {wi[1]:.4f}] -> {iv2(wi)} (the design seat's guess"
                 f"{' does not reproduce .64' if iv2(wi) != '[0.44, 0.64]' else ' reproduces it'}); Clopper-Pearson "
                 f"[{cp_[0]:.4f}, {cp_[1]:.4f}] -> {iv2(cp_)}; Wald [{wd[0]:.4f}, {wd[1]:.4f}] -> {iv2(wd)}.")
    o()
    # habit 83.4
    def comp(r):
        return habit.follows_habit(r)
    dom2 = [r for r in S if len(r["choices"]) >= 2]
    dom1 = [r for r in S if len(r["choices"]) >= 1]
    domv = [r for r in S if not r["excluded"] and len(r["choices"]) >= 1]
    c2 = sum(1 for r in dom2 if comp(r))
    c1 = sum(1 for r in dom1 if comp(r))
    cv = sum(1 for r in domv if comp(r))
    alt2 = sum(1 for r in dom2 if habit.strictly_alternates(r))
    altv = sum(1 for r in S if not r["excluded"] and len(r["choices"]) >= 2 and habit.strictly_alternates(r))
    nv2 = sum(1 for r in S if not r["excluded"] and len(r["choices"]) >= 2)
    o(f"- **First-pick habit 83.4%.** Definition (record): the first free pick is the complement of the "
      f"last forced round's pole ({loc('RESULTS.md', '**156/187 = 83.4%** have the first free pick complementing')}; "
      f"code `valence_core/e2d/habit.py` `follows_habit`). Domain of 156/187: all {len(S)} e2a sessions, all four "
      f"arms (steered arms included), excluded sessions included, restricted to sessions with ≥ 2 free "
      f"choices (n = {len(dom2)}) -- the strict-alternation domain the same sentence uses. Recomputed: "
      f"**{c2}/{len(dom2)} = {c2 / len(dom2):.4f}** (≥ 2 choices); {c1}/{len(dom1)} = {c1 / len(dom1):.4f} "
      f"(≥ 1 choice, the natural first-pick domain); valid-only {cv}/{len(domv)} = {cv / len(domv):.4f}. "
      f"Strict alternation: {alt2}/{len(dom2)} = {alt2 / len(dom2):.4f} (≥ 2 choices, incl. excluded); "
      f"valid-only {altv}/{nv2}.")
    per_arm = []
    for arm in ARMS:
        d2 = [r for r in dom2 if r["arm"] == arm]
        per_arm.append(f"{arm} {sum(1 for r in d2 if comp(r))}/{len(d2)}")
    o(f"  - by arm (≥ 2 choices, incl. excluded): {'; '.join(per_arm)}.")
    o()
    o(f"- **Control-arm sizes 37/23/22**: valid n sham {rec['sham']['n']} / random1 {rec['random1']['n']} / "
      f"random2 {rec['random2']['n']} (analysis.json `n`; launched {rec['sham']['launched']}/"
      f"{rec['random1']['launched']}/{rec['random2']['launched']}, excluded {rec['sham']['excluded']}/"
      f"{rec['random1']['excluded']}/{rec['random2']['excluded']}); reward {rec['reward']['n']} of "
      f"{rec['reward']['launched']}. Verdict entry: random1 n = {rec['random1']['n']} at "
      f"{loc('archive/RESULTS-cycles3-4.md', '0.152 (random1, n=23; sham +0.014, random2 +0.045)')}; sham "
      f"{rec['sham']['n']} and the random arms POOLED at "
      f"{loc('archive/RESULTS-cycles3-4.md', 'Valid n: reward 102 / sham 37', '/ random 45 — all floors met.')} "
      f"('random 45' = random1 + random2 = {rec['random1']['n']} + {rec['random2']['n']} = "
      f"{rec['random1']['n'] + rec['random2']['n']}); the entry states random2's {rec['random2']['n']} only by that "
      f"subtraction.")
    o()
    o("- **F1 link-5 y-axis.** The record's quantity is Δ_first = P(first free pick = +pole label) − ½ over "
      "valid sessions, i.e. (approach − avoid)/(2n). A label reading '(approach − avoid)' is off by the "
      "factor 2n (and '(approach − avoid)/n' by 2). Suggested relabel: 'Δ_first = share of first free "
      "picks to the +pole label − ½'.")
    o()

    # figures for (i)
    vloc = loc("archive/RESULTS-cycles3-4.md", "reward Δ = +0.0392 (55/102 first")
    rc_txt = pinned_text("scripts/e2a_recount.py")
    rc_a = lines_with(rc_txt, "def primary(audit):")[0]
    rc_b = lines_with(rc_txt, "return k, len(valid)")[0]
    rc_c = lines_with(rc_txt, "Delta_first = {k / n - 0.5:+.4f}")[0]
    an_a = quote_lines(CLAUDE_E2A_SESS, ["d = float(np.mean(firsts)) - 0.5"], clone=True)[0].split(": ", 1)[0]
    fig("Δ = share of first free choices toward the state label minus ½ (definition)",
        "delta_first = k/n − ½ over valid sessions, k = first free pick to the +pole label",
        f"{an_a} (clone, producing analyzer); scripts/e2a_recount.py@{PIN}:{rc_a}-{rc_b},{rc_c}", "reproduced", "N4(i)",
        "'state label' = +pole label (tag_plus); in the reward arm both labels carry a state (±α)")
    ventry = loc("archive/RESULTS-cycles3-4.md", "e2a VERDICT: NOT PASSED", "**e2a closes.** Next-step decision")
    fig("e2a VERDICTS entry (Code locates)", f"entry {ventry}; primary line {vloc}",
        "archive/RESULTS-cycles3-4.md (design seat's belief confirmed)",
        "log-only", "N4 referents", "e2a VERDICT entry 2026-08-09 ('reward Δ = +0.0392 (55/102 first free choices toward +pole)')")
    fig("state arm 55 of 102 → +0.0392", f"{rec['reward']['k']}/{rec['reward']['n']} → {rec['reward']['delta_first']:+.4f}",
        "data/e2a/analysis.json reward.delta_first,n; data/e2a/sessions.jsonl", "reproduced", "N4(i)")
    fig("P(X ≥ 55 | 102, ½) = 0.24422 = stored p", f"{p_ge_half(55, 102):.8f} (stored {A['reward']['binom_p_one_sided']})",
        "data/e2a/analysis.json reward.binom_p_one_sided", "reproduced", "N4(i)", "one-sided exact binomial, H1 approach")
    fig("sham 19/37 → +0.0135", f"{rec['sham']['k']}/{rec['sham']['n']} → {rec['sham']['delta_first']:+.4f}",
        "data/e2a/analysis.json sham", "reproduced", "N4(i)")
    fig("random-1 15/23 → +0.1522 (largest pseudo-Δ)", f"{rec['random1']['k']}/{rec['random1']['n']} → {rec['random1']['delta_first']:+.4f}; max |pseudo-Δ| = {pseudo[big]:.4f} ({big})",
        "data/e2a/analysis.json random1", "reproduced", "N4(i)")
    fig("random-2 12/22 → +0.0455", f"{rec['random2']['k']}/{rec['random2']['n']} → {rec['random2']['delta_first']:+.4f}",
        "data/e2a/analysis.json random2", "reproduced", "N4(i)")
    fig("every arm integer under share − ½, none under (approach − avoid)/n",
        "first half CONFIRMED; second half REFUTED for " + (", ".join(refuted_none) if refuted_none else "none"),
        "data/e2a/analysis.json (all delta_first, by_map)", "discrepant", "N4(i)",
        (f"the design seat's arithmetic, not a record figure (a note under block :3, not an (i) STOP under :62; "
         f"the record's figures reproduce): reward {rw_st:+.4f} = (2·{rw_kb[0]}−{rw_n})/{rw_n}; the stored p and the code disambiguate"
         if rw_kb else "the design seat's arithmetic, not a record figure"))
    fig("preprint quotation '54 of 101 valid sessions' (the sentence as the block quotes it)",
        f"no match in {PREPRINT} nor in the pre-patch {pp_short} copies",
        f"grep of {PREPRINT} (sha256 {pre_sha[:16]}) and {', '.join(pp_hits)}; PREPRINT-v1_1-draft.md and "
        f"RESEARCH-NOTE v0.2 absent ({pf_both})", "not found", "N4(i)",
        "the quotation only; the figure it carries reproduces (next row); "
        + ("v1.0 has 'valid sessions' on 55 of 102" if h55 else
           f"the patched v1.0 has 'valid sessions' on neither figure (finding on the patch {pf1})"))
    # round 9: when the patched text lacks the footnote form, the row keeps its label of record (the audited text)
    fn_rec = None if fn_d else rec_line("| preprint footnote 1 (")
    fig(f"preprint footnote 1 (:{h54[0] if h54 else '?'}): '54 of 101, Δ = {fn_d.group(1)}, p = {fn_d.group(2)}'"
        if fn_d else fn_rec["quote"].split(" | ")[0][2:],
        f"audit-v2 recount {kv}/{nv}, Δ_first = {kv / nv - 0.5:+.4f}, one-sided exact binomial p = {rc.binom_p_one_sided(kv, nv):.5f} "
        + (f"(equal at printed precision: {'YES' if fn_ok else 'NO; finding on the patch ' + pf1})" if fn_d else
           f"(the footnote form is not on the patched text: finding on the patch {pf1})"),
        "scripts/e2a_recount.py primary(V2) over data/e2a/sessions.jsonl + data/configs/e2b_audit_v2.json", "reproduced", "N4(i)",
        f"a different n the record explains ({corr_loc}), not a transcription error"
        + ("" if fn_d else f"; label as in the raw of record ({fn_rec['locator']}), the audited text"))
    fig("preprint quotation 'Δ_first is half the difference between the state and sham arms' break rates'",
        f"no match for 'half the difference' in {PREPRINT} nor in the pre-patch {pp_short} copies",
        f"grep of {PREPRINT} and {', '.join(pp_hits)}; v1.1 and RESEARCH-NOTE v0.2 absent ({pf_both})", "not found", "N4(i)",
        f"the quotation only; v1.0 :{hbreak[0] if hbreak else '?'} states the within-arm decomposition instead (next row)")
    fig("the break-rate identity the sentence glosses (definition, gloss or error?)",
        f"within-arm identity: balanced {hab['reward']['balanced']:+.4f}, weighted {hab['reward']['weighted']:+.4f} (= measured Δ_first); literal between-arm reading {lit:+.4f}",
        "valence_core/e2d/habit.py break_rates over data/e2a/sessions.jsonl (valid reward)", "computed-new", "N4(i)",
        "between-arm wording is an error; within-arm form is a mechanism gloss (exact only at balance), not the definition")
    fig("map-level +0.104 / −0.031 (state arm)", f"A {rec['reward']['map']['A'][0]}/{rec['reward']['map']['A'][1]} → {rec['reward']['map']['A'][2]:+.4f}; B {rec['reward']['map']['B'][0]}/{rec['reward']['map']['B'][1]} → {rec['reward']['map']['B'][2]:+.4f}",
        "data/e2a/analysis.json reward.by_map", "reproduced", "N4(i)")
    fig("sham-arm map-level +0.111 / −0.079", f"A {rec['sham']['map']['A'][0]}/{rec['sham']['map']['A'][1]} → {rec['sham']['map']['A'][2]:+.4f}; B {rec['sham']['map']['B'][0]}/{rec['sham']['map']['B'][1]} → {rec['sham']['map']['B'][2]:+.4f}",
        "data/e2a/analysis.json sham.by_map", "reproduced", "N4(i)")
    w = ivs["55/102 Wilson score"]; cpi = ivs["55/102 Clopper-Pearson exact"]; wa = ivs["55/102 Wald"]
    iv_rep = "[0.44, 0.64]" in (iv2(cpi), iv2(wa))
    iv_by = " or ".join(nm for nm, x in (("Clopper-Pearson", cpi), ("Wald", wa)) if iv2(x) == "[0.44, 0.64]")
    wi_rep = iv2(w) == "[0.44, 0.64]"
    blk_wilson = loc(BLOCK, "the approach-probability interval ≈ [.44, .64] with its method (Wilson on 55/102 gives it)")
    # round 4, finding 4: the record figure and the design seat's method claim are separate rows
    fig("approach-probability interval ≈ [.44, .64]",
        f"95% two-sided on {rec['reward']['k']}/{rec['reward']['n']}: Clopper-Pearson [{cpi[0]:.4f}, {cpi[1]:.4f}] → {iv2(cpi)}; "
        f"Wald [{wa[0]:.4f}, {wa[1]:.4f}] → {iv2(wa)} (reproduced under {iv_by if iv_by else 'neither'})",
        f"computed from {rec['reward']['k']}/{rec['reward']['n']} (analysis.json reward.n, sessions.jsonl); the record figure: {f3}",
        "reproduced" if iv_rep else "discrepant", "N4(i)",
        f"reproduced at 2 dp under {iv_by if iv_by else 'neither Clopper-Pearson nor Wald'}; the record states no method "
        f"({f3}); the block's method claim has its own row (next)")
    fig("the interval's method (block: 'Wilson on 55/102 gives it')",
        f"Wilson score 95% on {rec['reward']['k']}/{rec['reward']['n']}: [{w[0]:.4f}, {w[1]:.4f}] → {iv2(w)}"
        f"{'' if wi_rep else ', not [.44, .64]'}",
        f"computed from {rec['reward']['k']}/{rec['reward']['n']}; the claim: {blk_wilson}",
        "reproduced" if wi_rep else "discrepant", "N4(i)",
        "the design seat's method claim, not a record figure (a note under block :3, not an (i) STOP under :62, "
        f"treated like the integrality row); the record names no method (referent note {note_no(NOTE_INTERVAL)}); "
        "the interval itself has its own reproduced row (previous)")
    fig("first-pick habit 83.4%", f"{c2}/{len(dom2)} = {c2 / len(dom2):.4f} (all arms, incl. excluded, ≥2 free choices); {c1}/{len(dom1)} = {c1 / len(dom1):.4f} (≥1); valid {cv}/{len(domv)}",
        "data/e2a/sessions.jsonl (rounds[-1].pole vs choices[0].picked_pole)", "reproduced", "N4(i)",
        f"record locator {loc('RESULTS.md', '**156/187 = 83.4%** have the first free pick complementing')}")
    assert rec["random1"]["n"] + rec["random2"]["n"] == 45 and "/ random 45" in pinned_text("archive/RESULTS-cycles3-4.md")
    fig("control-arm sizes 37/23/22", f"{rec['sham']['n']}/{rec['random1']['n']}/{rec['random2']['n']}",
        "data/e2a/analysis.json sham.n, random1.n, random2.n", "reproduced", "N4(i)",
        "the verdict entry pools random1 + random2 as 'random 45' (see (i-f))")
    fig("F1 link-5 y-axis '(approach − avoid)'",
        f"record quantity Δ_first = k/n − ½ = (approach − avoid)/(2n); e.g. reward ({2 * rec['reward']['k'] - rec['reward']['n']})/(2·{rec['reward']['n']}) = {rec['reward']['delta_first']:+.4f}",
        f"{an_a} (clone); scripts/e2a_recount.py@{PIN}:{rc_a}-{rc_b},{rc_c}", "discrepant", "N4(i)",
        "a figure label, not a record figure; the block (:57) already says the post version is relabeled. "
        "Relabel: 'Δ_first = share of first free picks to the +pole label − ½'")

    # ==================================================================== (ii)
    o("## (ii) Minimum detectable effect")
    o()
    prereg = loc("archive/RESULTS-cycles3-4.md", "e2a PRE-REGISTRATION — pure-operant preference loop")
    crit = loc("archive/RESULTS-cycles3-4.md", "**PASS ⇔ (1) Δ > max pseudo-Δ computed identically over sham and",
               "binomial p < 0.05 one-sided (approach) as floor guard.**")
    powl = loc("archive/RESULTS-cycles3-4.md", "designated and counterbalanced). Power at floors: first-free-choice",
               "detects P(+) = 0.65 vs 0.5 at ~0.85 power, one-sided α = 0.05.")
    g3c = loc("archive/RESULTS-cycles3-4.md", "mechanical null; primary clause (1) (Δ > max pseudo-Δ over sham",
              "control at the statistic level.")
    o(f"- Pre-registration: {prereg} (2026-08-08). Criterion: {crit}. Conjunct (3), the registered test: "
      f"**exact binomial, one-sided (approach), α = 0.05, pass iff p < 0.05**; the analyzer applies it to p "
      f"rounded to 5 decimals (`c3`, quoted in (i-a)). Conjunct (1), the 'sham envelope': **Δ > max "
      f"pseudo-Δ computed identically over sham and random arms**, reaffirmed by the g3′ amendment as the "
      f"operative mechanical control ({g3c}). It is a comparison of point estimates, not a test with an α; "
      f"the analyzer reads it with absolute values (`pseudo = [abs(...)]`). Design-stage power claim: {powl}.")
    o()
    mde = {}
    o("Registered test (conjunct 3) -- exact binomial power. Critical count c = smallest k with "
      "P(X ≥ k | n, ½) < 0.05 (checked identically with the analyzer's 5-dp rounding); MDE p* = smallest "
      "p with P(X ≥ c | n, p) ≥ 0.80 (bisection, 200 halvings; power is increasing in p); δ* = p* − ½:")
    o()
    o("| n | c | size P(X ≥ c; n, ½) | P(X ≥ c−1; n, ½) | p* | δ* = p* − ½ | power at p* | power at δ = .05 / .10 / .15 |")
    o("|---|---|---|---|---|---|---|---|")
    for n in (101, 102, 96):
        c = next(k for k in range(n + 1) if p_ge_half(k, n) < 0.05)
        c5 = next(k for k in range(n + 1) if round(p_ge_half(k, n), 5) < 0.05)
        assert c == c5
        ps = bisect_increasing(lambda p: sf(c, n, p), 0.80, 0.5, 1.0)
        grid = [sf(c, n, 0.5 + d) for d in (0.05, 0.10, 0.15)]
        mde[n] = {"c": c, "size": p_ge_half(c, n), "p_star": ps, "delta_star": ps - 0.5,
                  "power_at_p_star": sf(c, n, ps), "power_grid": grid}
        o(f"| {n}{' (floor)' if n == 96 else ''} | {c} | {p_ge_half(c, n):.5f} | {p_ge_half(c - 1, n):.5f} | {ps:.5f} | "
          f"**{ps - 0.5:+.4f}** | {sf(c, n, ps):.4f} | {grid[0]:.3f} / {grid[1]:.3f} / {grid[2]:.3f} |")
    o()
    pw96 = sf(mde[96]["c"], 96, 0.65)
    o(f"- At the declared floor n = 96 the exact power at P(+) = 0.65 is {pw96:.3f} (c = {mde[96]['c']}); the "
      f"pre-registration's '~0.85' ({powl.split(':')[-1]}) states no method and is "
      f"{'below' if pw96 > 0.85 else 'at or above'} the exact value.")
    NOTES.append(f"Pre-registration power line ({powl}): "
                 f"'P(+) = 0.65 vs 0.5 at ~0.85 power, one-sided α = 0.05' at n = 96; exact binomial power is {pw96:.3f} "
                 f"(critical count {mde[96]['c']}). {'Conservative' if pw96 > 0.85 else 'Optimistic'}; method unstated. "
                 f"Descriptive, no action proposed.")
    same_c = mde[101]["c"] == mde[102]["c"]
    o(f"- **Which n.** {nv} is the n of the correction of record (audit v2; archive addendum); {nf} is the n of "
      f"the published verdict and of `analysis.json`. The MDE is {mde[101]['delta_star']:+.4f} at 101 and "
      f"{mde[102]['delta_star']:+.4f} at 102"
      + (f" -- smaller at 102 because c stays {mde[101]['c']} while the size rises from {mde[101]['size']:.4f} "
         f"to {mde[102]['size']:.4f} (discreteness)" if same_c else "")
      + ". For a sentence about the corrected primary, n = 101 is right; for the published verdict, n = 102.")
    o()

    # envelope
    def env_cdf(ns, signed: bool = False):
        """P(M < x) under the null, as a function of x, for
        M = max_j round(|k_j/n_j - 1/2|, 4)   (signed=False: the analyzer's |.| reading) or
        M = max_j round(k_j/n_j - 1/2, 4)     (signed=True: the registered text's reading)."""
        dists = []
        for nj in ns:
            vals = collections.defaultdict(float)
            for k in range(nj + 1):
                v = r4(k / nj - 0.5)
                vals[v if signed else abs(v)] += math.comb(nj, k) / 2 ** nj
            dists.append(sorted(vals.items()))
        memo: dict[float, float] = {}

        def lt(x):
            if x not in memo:
                pr = 1.0
                for dl in dists:
                    pr *= sum(p for v, p in dl if v < x)
                memo[x] = pr
            return memo[x]
        return lt

    def env_power(n, p, lt):
        return sum(pmf(k, n, p) * lt(r4(k / n - 0.5)) for k in range(n + 1))

    ctrl = (rec["sham"]["n"], rec["random1"]["n"], rec["random2"]["n"])
    floors_loc = loc("archive/RESULTS-cycles3-4.md", "- **Arms & N (floors; exact N declared after smoke runtime",
                     "designated and counterbalanced). Power at floors: first-free-choice")
    FL_R, FL_C = 96, (32, 16, 16)   # reward >= 96; sham >= 32; random >= 32 (16/pair), per floors_loc
    fl_txt = pinned_text("archive/RESULTS-cycles3-4.md")
    assert "±axis ≥ 96 sessions" in fl_txt and "unsteered) ≥ 32" in fl_txt and "pairs ≥ 32 (16/pair" in fl_txt
    obs_env = max(pseudo.values())
    signed_max = max(A[a]["delta_first"] for a in ("sham", "random1", "random2"))
    NOTES.append("Conjunct (1) as coded compares Δ_first with max |pseudo-Δ| (absolute values, "
                 f"{CLAUDE_E2A_SESS} `pseudo = [abs(...)]`); the pre-registered text reads 'Δ > max pseudo-Δ' without "
                 f"absolute values ({crit}). At the realized arms the two readings coincide (max signed "
                 f"{signed_max:+.4f} = max |.| {obs_env:.4f}), so the verdict is unaffected. They do not coincide "
                 f"in power: (ii) computes the MDE under both, and the PI or design seat picks the reading the note uses.")
    o("Sham-envelope criterion (conjunct 1). Two readings of the envelope M, both computed: **|·|** = the "
      "analyzer's coded reading, Δ_first(reward) (4 dp) > max over sham, random1, random2 of |Δ_first| (4 dp); "
      "**signed** = the registered text read literally ('Δ > max pseudo-Δ', no absolute values), Δ_first(reward) > "
      "max of the signed Δ_first. Power = P(conjunct 1 passes) when the reward arm's first-pick probability is p, "
      "computed exactly by enumeration. Two conditioning choices, both stated:")
    o()
    o(f"- (E1) unconditional: the three control arms are drawn under their declared null role (P(+) = ½, the "
      f"pseudo-arms) at their realized valid sizes {'/'.join(map(str, ctrl))} (and, for comparison, at the declared "
      f"floors {'/'.join(map(str, FL_C))} with reward n = {FL_R}; {floors_loc});")
    o(f"- (E2) conditional on the realized envelope, max |pseudo-Δ| = {obs_env:.4f} (the realized signed max is "
      f"{signed_max:+.4f}, so E2 is the same under both readings): power = P(Δ̂ > {obs_env:.4f}).")
    o()
    o("| reading | conditioning | reward n | controls | P(M ≥ 0.10) under null | p* | δ* = p* − ½ | power at p* |")
    o("|---|---|---|---|---|---|---|---|")
    envres = {}
    for signed in (False, True):
        rd = "signed" if signed else "|·|"
        for tag, n, ns in (("E1", 101, ctrl), ("E1", 102, ctrl), ("E1 floors", FL_R, FL_C)):
            lt = env_cdf(ns, signed)
            ps = bisect_increasing(lambda p: env_power(n, p, lt), 0.80, 0.5, 1.0)
            pge = 1 - lt(0.10)
            envres[f"{tag} n={n} {rd}"] = {"reading": rd, "p_star": ps, "delta_star": ps - 0.5,
                                          "power": env_power(n, ps, lt), "P_env_ge_0.10": pge, "controls": list(ns)}
            o(f"| {cell(rd)} | {tag} | {n} | {'/'.join(map(str, ns))} | {pge:.4f} | {ps:.5f} | **{ps - 0.5:+.4f}** | "
              f"{env_power(n, ps, lt):.4f} |")
    assert r4(signed_max) == r4(obs_env)
    for n in (101, 102):
        f = lambda p, n=n: sum(pmf(k, n, p) for k in range(n + 1) if r4(k / n - 0.5) > obs_env)
        ps = bisect_increasing(f, 0.80, 0.5, 1.0)
        kmin = min(k for k in range(n + 1) if r4(k / n - 0.5) > obs_env)
        envres[f"E2 n={n}"] = {"reading": "both", "p_star": ps, "delta_star": ps - 0.5, "power": f(ps), "k_min": kmin}
        o(f"| both | E2 (envelope {obs_env:.4f}, needs k ≥ {kmin}) | {n} | realized | -- | {ps:.5f} | "
          f"**{ps - 0.5:+.4f}** | {f(ps):.4f} |")
    o()
    # joint power (computed-new, outside the ask)
    def joint_power(n_a, n_b, p, lt):
        n = n_a + n_b
        c = next(k for k in range(n + 1) if round(p_ge_half(k, n), 5) < 0.05)
        tot = 0.0
        pa = [pmf(k, n_a, p) for k in range(n_a + 1)]
        pb = [pmf(k, n_b, p) for k in range(n_b + 1)]
        for ka in range(n_a + 1):
            if r4(ka / n_a - 0.5) < 0:
                continue
            for kb in range(n_b + 1):
                if r4(kb / n_b - 0.5) < 0:
                    continue
                k = ka + kb
                if k < c:
                    continue
                tot += pa[ka] * pb[kb] * lt(r4(k / n - 0.5))
        return tot
    sham_maps = (A["sham"]["by_map"]["A"], A["sham"]["by_map"]["B"])
    jres = {}
    for signed in (False, True):
        rd = "signed" if signed else "|·|"
        lt_real = env_cdf(ctrl, signed)
        for n, (na, nb) in ((102, (rec["reward"]["map"]["A"][1], rec["reward"]["map"]["B"][1])),
                            (101, (mpv["A"][1], mpv["B"][1]))):
            ps = bisect_increasing(lambda p: joint_power(na, nb, p, lt_real), 0.80, 0.5, 1.0, it=60)
            jres[f"{n} {rd}"] = {"reading": rd, "n": n, "maps": [na, nb], "p_star": ps, "delta_star": ps - 0.5}
            o(f"- (computed-new, beyond the block's ask) all three registered conjuncts jointly, conjunct (1) read "
              f"{rd}, controls at the null ({'/'.join(map(str, ctrl))}), equal p on both maps (map A n = {na}, map B "
              f"n = {nb}), reward n = {n}: p* = {ps:.4f}, δ* = **{ps - 0.5:+.4f}**.")
    o(f"- The joint rows assume no map-level label/order artifact; the record shows one in sham (map A "
      f"{sham_maps[0]:+.4f}, map B {sham_maps[1]:+.4f}), which would lower conjunct (2)'s power further.")
    o()
    # round 9, fix round (ruling 9): the preprint's power sentence the Reading characterizes, located by text
    PW_Q = "Power excludes medium-and-larger effects"
    h_pw = pre_hits(PW_Q)
    h_pwr = h_pw or pre_hits("registered test detects")
    pw_old = rec_line("Power excludes medium-and-larger effects (P(approach)")
    pw_l = sentence_at(pl[h_pwr[0] - 1], "registered test detects", 2000) if h_pwr else ""
    pw_m = re.search(r"shift of ([+−-]\d*\.\d+) at (\d+)% power", pw_l)
    pw_r = re.search(r"pass rule about ([+−-]\d*\.\d+) to ([+−-]\d*\.\d+)", pw_l)
    jr_ = sorted((jres["101 signed"]["delta_star"], jres["101 |·|"]["delta_star"]))
    if pw_m and pw_r:
        pw_ok = (eq_printed(pw_m.group(1), mde[101]["delta_star"]) and int(pw_m.group(2)) == 80
                 and eq_printed(pw_r.group(1), jr_[0]) and eq_printed(pw_r.group(2), jr_[1]))
        pw_figs = (f"figures on the patched sentence equal this run's n = 101 values at their printed precision: "
                   f"{'YES' if pw_ok else 'NO'} (first-choice shift {pw_m.group(1)} at {pw_m.group(2)}% power vs the "
                   f"registered-test MDE δ* = {mde[101]['delta_star']:+.4f} at power .80; pass rule {pw_r.group(1)} to "
                   f"{pw_r.group(2)} vs the joint δ* {jr_[0]:+.4f} (signed) to {jr_[1]:+.4f} (|·|))")
    else:
        pw_figs = "the patched power figures were not parsed"
    pf_pw = None if h_pw else patch_finding(
        f"N4(ii): the preprint reads '{PW_Q}' (the sentence (ii)'s Reading calls a confidence-interval statement)",
        [pw_old], [pq(n_, "registered test detects") for n_ in h_pwr],
        f"registered-test MDE (computed-new, (ii)) at n = 101 δ* = {mde[101]['delta_star']:+.4f}, at n = 102 "
        f"{mde[102]['delta_star']:+.4f}; the pass rule jointly at n = 101: signed {jres['101 signed']['delta_star']:+.4f}, "
        f"|·| {jres['101 |·|']['delta_star']:+.4f}; the record's own statement: "
        f"{loc('FINDINGS-3.md', 'Medium-and-larger effects excluded', '(P(+) interval ≈ .44–.64); small effects survive.')}"
        f" ('Medium-and-larger effects excluded (P(+) interval ≈ .44–.64)')", pw_figs)
    pw_read = ("'Power excludes medium-and-larger effects' is a confidence-interval statement in the record; the MDE "
               "above is the power statement." if h_pw else
               f"'{PW_Q}' was the audited preprint's wording (its :172 as the raw of record quotes it, "
               f"{pw_old['locator']}), a confidence-interval statement; the record's own is "
               f"{loc('FINDINGS-3.md', 'Medium-and-larger effects excluded', '(P(+) interval ≈ .44–.64); small effects survive.')} "
               f"('Medium-and-larger effects excluded (P(+) interval ≈ .44–.64)'). The patched preprint replaces it with "
               f"a power statement (:{','.join(map(str, h_pwr)) or '?'}; finding on the patch {pf_pw}, below); the MDE "
               f"above is the power statement.")
    o(f"**Reading.** At the registered test the first-choice MDE (80% power, one-sided exact α = .05) is "
      f"δ = {mde[101]['delta_star']:+.3f} at n = 101 (P(+) = {mde[101]['p_star']:.3f}). The sham-envelope "
      f"criterion is a different bar: unconditionally (E1) it needs δ ≈ "
      f"{envres['E1 n=101 signed']['delta_star']:+.3f} under the registered text (signed) and ≈ "
      f"{envres['E1 n=101 |·|']['delta_star']:+.3f} under the analyzer's |·| reading, at n = 101; conditional on "
      f"the realized envelope {obs_env:.4f} (E2) it needs δ = {envres['E2 n=101']['delta_star']:+.3f} either way. "
      f"The pass rule as a whole needs δ ≈ {jres['101 signed']['delta_star']:+.3f} (signed) or ≈ "
      f"{jres['101 |·|']['delta_star']:+.3f} (|·|) at n = 101. Which reading the note uses is the PI's or the "
      f"design seat's call (Items for the PI). " + pw_read)
    o()
    fig("MDE at n = 101, α as pre-registered, power .80, registered test", f"c = {mde[101]['c']}, p* = {mde[101]['p_star']:.5f}, δ* = {mde[101]['delta_star']:+.4f}",
        f"computed from the registered test ({crit})", "computed-new", "N4(ii)", "one-sided exact binomial α = .05")
    fig("MDE at n = 102 (record's published n)", f"c = {mde[102]['c']}, p* = {mde[102]['p_star']:.5f}, δ* = {mde[102]['delta_star']:+.4f}",
        "computed", "computed-new", "N4(ii)")
    fig("MDE at the sham-envelope criterion",
        f"E1, controls at the null {'/'.join(map(str, ctrl))}: signed n=101 δ* = {envres['E1 n=101 signed']['delta_star']:+.4f}, "
        f"n=102 δ* = {envres['E1 n=102 signed']['delta_star']:+.4f}; |·| n=101 δ* = {envres['E1 n=101 |·|']['delta_star']:+.4f}, "
        f"n=102 δ* = {envres['E1 n=102 |·|']['delta_star']:+.4f}. E2 (realized envelope {obs_env:.4f}, both readings): "
        f"n=101 δ* = {envres['E2 n=101']['delta_star']:+.4f}, n=102 δ* = {envres['E2 n=102']['delta_star']:+.4f}. "
        f"Joint, n=101: signed {jres['101 signed']['delta_star']:+.4f}, |·| {jres['101 |·|']['delta_star']:+.4f}",
        f"criterion {crit}; reaffirmed {g3c}", "computed-new", "N4(ii)",
        "the criterion is not a test; two readings x two conditionings stated; the reading is the PI's/design seat's pick")

    # =================================================================== (iii)
    o("## (iii) 311 vs 360")
    o()
    L = pinned_jsonl("data/e2a/g3prime_kl.jsonl")
    L1 = pinned_jsonl("data/e2a/g3prime_kl_v1.jsonl")
    SM = pinned_jsonl("data/e2a/sessions_smoke.jsonl")
    key = lambda d: (d["arm"], d["session"], d["choice"])
    cnt = collections.Counter(key(d) for d in L)
    allzero = all(d["kl"] == 0.0 for d in L)
    dup = {k: v for k, v in cnt.items() if v > 1}
    full_ver = [(r["arm"], r["session"], c["round"]) for r in S for c in r["choices"] if c.get("verify_kl") is not None]
    full_all = [(r["arm"], r["session"], c["round"]) for r in S for c in r["choices"]]
    cadence = sum(1 for r in S for c in r["choices"]
                  if ((r["session"] * 6 + c["round"]) % 4 == 0) == (c.get("verify_kl") is not None))
    smoke_keys = [(r["arm"], r["session"], c["round"]) for r in SM for c in r["choices"]]
    # smoke2 expected sequence from its raw
    raw2 = pinned_text("results/raw/2026-08-09_e2a_smoke2.txt")
    exp2 = []
    for m in re.finditer(r"\[\d+/8\] (\w+) s(\d+): first=\S+(?: EXCLUDED (\S+))?", raw2):
        arm, s_, why = m.group(1), int(m.group(2)), m.group(3)
        if why is None:
            nch = 6
        elif "@free" in why:
            nch = int(why.split("@free")[1]) + 1
        else:
            nch = 0
        exp2 += [(arm, s_, c) for c in range(nch)]
    seq = [key(d) for d in L]
    n2 = len(exp2)
    seg_smoke2 = seq[:n2] == exp2
    seg_smoke3 = seq[n2:n2 + len(smoke_keys)] == smoke_keys
    seg_full = (sorted(seq[n2 + len(smoke_keys):]) == sorted(full_ver)
                and len(seq[n2 + len(smoke_keys):]) == len(full_ver))
    ident = []
    Sidx = {(r["arm"], r["session"]): r for r in S}
    for r in SM:
        f_ = Sidx.get((r["arm"], r["session"]))
        ident.append(f_ is not None and f_["transcript"] == r["transcript"])
    # round 4, finding 5: what else the smoke3 rows share with the run's rows, and where they differ
    def _drop(x: dict, keys: tuple) -> dict:
        return {k_: v_ for k_, v_ in x.items() if k_ not in keys}
    sm_pair = [(r, Sidx[(r["arm"], r["session"])]) for r in SM if (r["arm"], r["session"]) in Sidx]
    sm_pick_pa = sum(1 for r, f_ in sm_pair
                     if [(c["pick"], c["p_a"]) for c in r["choices"]] == [(c["pick"], c["p_a"]) for c in f_["choices"]])
    sm_row_json = sum(1 for r, f_ in sm_pair if json.dumps(r, sort_keys=True) == json.dumps(f_, sort_keys=True))
    sm_nch_eq = [f"{r['arm']} s{r['session']}: {len(r['choices'])} free choices" for r, f_ in sm_pair
                 if json.dumps(r, sort_keys=True) == json.dumps(f_, sort_keys=True)]
    DROP = ("verify_kl", "oop_tag")
    sm_rest_eq = sum(1 for r, f_ in sm_pair
                     if json.dumps({**_drop(r, ("choices", "rounds")),
                                    "choices": [_drop(c, DROP) for c in r["choices"]],
                                    "rounds": [_drop(x, DROP) for x in r["rounds"]]}, sort_keys=True)
                     == json.dumps({**_drop(f_, ("choices", "rounds")),
                                    "choices": [_drop(c, DROP) for c in f_["choices"]],
                                    "rounds": [_drop(x, DROP) for x in f_["rounds"]]}, sort_keys=True))
    sm_vkl_diff = [f"{r['arm']} s{r['session']}" for r, f_ in sm_pair
                   if [c.get("verify_kl") for c in r["choices"]] != [c.get("verify_kl") for c in f_["choices"]]]
    sm_vkl_vals = sorted(set(c.get("verify_kl") for r in SM for c in r["choices"]), key=repr)
    sm_oop = [f"{r['arm']} s{r['session']}" for r, f_ in sm_pair
              if any("oop_tag" in x for x in f_["rounds"] + f_["choices"])
              and not any("oop_tag" in x for x in r["rounds"] + r["choices"])]
    sm_oop_other = [r for r, f_ in sm_pair if any("oop_tag" in x for x in r["rounds"] + r["choices"])]
    sm_oop_vals = sorted(set(json.dumps(x["oop_tag"]) for r, f_ in sm_pair for x in f_["rounds"] + f_["choices"]
                             if "oop_tag" in x))
    sm_nan = any(t_ in pinned_text(pth) for pth in ("data/e2a/sessions.jsonl", "data/e2a/sessions_smoke.jsonl")
                 for t_ in ("NaN", "Infinity"))
    assert not sm_oop_other
    fv = set(full_ver)
    s3only = set(smoke_keys) - fv
    s2only = set(exp2) - fv - set(smoke_keys)
    distinct_inputs_record = len(fv | (set(smoke_keys) & set(full_all)))
    o(f"- `data/e2a/g3prime_kl.jsonl`@{PIN}: **{len(L)} rows**, **{len(cnt)} distinct (arm, session, choice) keys**, "
      f"{sum(v - 1 for v in dup.values())} duplicate rows over {len(dup)} keys; every row `kl == 0.0` exactly: "
      f"{allzero}. Values in the ledger: {sorted(set(d['kl'] for d in L))}.")
    o(f"- Segmentation, asserted: rows 1-{n2} = smoke2 (the 8-session sequence printed in "
      f"`results/raw/2026-08-09_e2a_smoke2.txt`, choices per session inferred from its EXCLUDED lines, "
      f"verify_every = 1): {seg_smoke2}; rows {n2 + 1}-{n2 + len(smoke_keys)} = smoke3 = exactly the "
      f"{len(smoke_keys)} choices of `data/e2a/sessions_smoke.jsonl` in file order: {seg_smoke3}; rows "
      f"{n2 + len(smoke_keys) + 1}-{len(L)} = the full run = exactly the {len(full_ver)} choices carrying a "
      f"non-null `verify_kl` in `data/e2a/sessions.jsonl`: {seg_full}. {n2} + {len(smoke_keys)} + "
      f"{len(full_ver)} = {n2 + len(smoke_keys) + len(full_ver)}.")
    ver_q = quote_lines(f"{CLONE}/scripts/e2a_sessions.py", ["N_FREE = 6",
                                                            "verify = ((s * N_FREE + ci) % verify_every == 0)",
                                                            "verify_every = 1 if args.smoke else 4"], clone=True)
    o()
    o("Verification cadence, as the producing runner (gitignored clone) codes it:")
    o()
    o("```")
    for q in ver_q:
        o(q)
    o("```")
    o()
    o(f"- The full run verified a choice iff (6·s + c) mod 4 = 0 (`verify_every = 4`, N_FREE = 6): "
      f"{cadence}/{len(full_all)} choices agree with that rule; {len(full_ver)} of the run's {len(full_all)} choice "
      f"forwards = {len(full_ver) / len(full_all):.4f} were verified, all at KL = 0.0 (the session rows' own "
      f"`verify_kl`: {sorted(set(c['verify_kl'] for r in S for c in r['choices'] if c.get('verify_kl') is not None))}).")
    s2o_desc = []
    for (a_, s_, c_) in sorted(s2only):
        r_ = Sidx.get((a_, s_))
        s2o_desc.append(f"({a_}, {s_}, {c_}): the record's {a_} s{s_} has {len(r_['choices']) if r_ else '?'} free "
                        f"choices (excluded: {r_['excluded'] if r_ else '?'}, reason `{r_['exclude_reason'] if r_ else '?'}`)")
    s2_overlap = n2 - len(s2only)
    o(f"- The {len(SM)} smoke3 sessions' transcripts are byte-identical to the full-run sessions' with the same "
      f"(arm, session) ({sum(ident)}/{len(ident)}; every choice's pick and p_a equal, {sm_pick_pa}/{len(sm_pair)}; "
      f"smoke used the verdict session indices). The rows themselves are equal as JSON for {sm_row_json} of "
      f"{len(sm_pair)} ({'; '.join(sm_nch_eq) if sm_nch_eq else 'none'}); the others differ in `verify_kl` "
      f"({len(sm_vkl_diff)} of {len(sm_pair)}: smoke3 set it at every choice, values {sm_vkl_vals}, the run left it "
      f"null off its every-fourth cadence) and, in {len(sm_oop)} of them ({', '.join(sm_oop) if sm_oop else 'none'}), "
      f"in an `oop_tag` key the run's rounds and choices carry (values {', '.join(sm_oop_vals)}) and smoke3's do "
      f"not; with those two keys set aside every row is equal ({sm_rest_eq}/{len(sm_pair)}); NaN or Infinity tokens "
      f"in either file: {'PRESENT' if sm_nan else 'none'}. So the {len(s3only)} smoke3-only keys "
      f"are identical-input verifications of {len(s3only)} full-run choice forwards the run itself did not verify. "
      f"Smoke2-only keys: {'; '.join(s2o_desc) if s2o_desc else 'none'}. smoke2's own session file was deleted "
      f"before smoke3 ({loc('archive/RESULTS-cycles3-4.md', 'by my cleanup `rm` before smoke3')}), so whether its "
      f"other {s2_overlap} verified forwards were over the record's inputs cannot be established from committed "
      f"artifacts. `data/e2a/g3prime_kl_v1.jsonl` ({len(L1)} rows, the first smoke's) is a separate file and not in "
      f"either count.")
    o(f"- Hence: {len(cnt)} = distinct ledger keys = {len(fv)} (run) + {len(s3only)} (smoke3 only) + {len(s2only)} "
      f"(smoke2 only); of the record's {len(full_all)} choice-forward inputs, {distinct_inputs_record} have a verified "
      f"re-forward at KL exactly 0.0 somewhere in the ledger; the run proper verified {len(full_ver)}.")
    assert len(cnt) == len(fv) + len(s3only) + len(s2only)
    o(f"- Record: archived count {loc('archive/RESULTS-cycles3-4.md', 'g3′ clause 1 final ledger 360/360 choice forwards at KL = 0.0')} "
      f"('360/360 choice forwards at KL = 0.0 exactly'); the ledger was designed to span smokes and the run "
      f"({loc('archive/RESULTS-cycles3-4.md', 'clause-1 ledger continues across new smoke + full.')}); the "
      f"correction {loc('RESULTS.md', 'holds 360 rows over 311 distinct (arm, session, choice) keys', 'non-null `verify_kl` in the session rows. Nothing about the assertion')} "
      f"and {loc('RESULTS.md', '`data/e2a/g3prime_kl.jsonl` holds 360 rows but 311 distinct (arm,', 'verified reads.')}.")
    hp109 = lines_with(pre, "311 distinct verified forward passes")
    hp109r = hp109 or lines_with(pre, "311 distinct verified")   # round 9: re-anchored if the patch reworded it
    bar_loc = loc("valence_core/readout.py", "# g3' clause 1 was stated as <= 1e-6 in e2a; the v3 session harness hardened",
                  "VERIFY_KL_BAR_E2A = 1e-6")
    skl_loc = loc("valence_core/readout.py", "def symmetric_kl(p: np.ndarray, q: np.ndarray) -> float:",
                  "return max(kl(p, q), kl(q, p))")
    c1_loc = loc("archive/RESULTS-cycles3-4.md", "KL(choice forward ‖ vanilla forward, same text) ≤ 1e-6;")
    q109 = f"{len(cnt)} distinct verified forward passes at symmetric KL ≤ 10⁻⁶, one in every four choice reads"
    # fix round: the figures the patched :109 sentence prints, parsed and compared with this run's values
    l109 = pl[hp109r[0] - 1] if hp109r else ""
    SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
    bar_v = float(re.search(r"^VERIFY_KL_BAR_E2A = (\S+)", pinned_text("valence_core/readout.py"), re.M).group(1))
    kl_vals = sorted(set(d["kl"] for d in L) | set(c["verify_kl"] for r in S for c in r["choices"]
                                                    if c.get("verify_kl") is not None))
    m_a = re.search(r"(\d[\d,]*) of the (\d[\d,]*) choice reads \(every fourth\)", l109)
    m_k = re.search(r"KL = (\d+(?:\.\d+)?) exactly", l109)
    m_b = re.search(r"10⁻([⁰¹²³⁴⁵⁶⁷⁸⁹]+) bound", l109)
    m_n = re.search(r"(\d[\d,]*) distinct verified reads counting the (\w+) smoke runs", l109)
    n_smk = sum(1 for x_ in (s3only, s2only) if x_)
    WORDN = {"one": 1, "two": 2, "three": 3}
    if m_a and m_k and m_b and m_n:
        ok109 = (int(m_a.group(1).replace(",", "")) == len(full_ver) and int(m_a.group(2).replace(",", "")) == len(full_all)
                 and cadence == len(full_all) and kl_vals == [float(m_k.group(1))]
                 and 10.0 ** -int(m_b.group(1).translate(SUP)) == bar_v
                 and int(m_n.group(1).replace(",", "")) == len(cnt) and WORDN.get(m_n.group(2)) == n_smk)
        figs109 = (f"figures on the patched sentence equal this run's values: {'YES' if ok109 else 'NO'} "
                   f"({m_a.group(1)} of the {m_a.group(2)} choice reads (every fourth) vs {len(full_ver)}/{len(full_all)} "
                   f"verified, cadence (6·s + c) mod 4 = 0 on {cadence}/{len(full_all)}; KL = {m_k.group(1)} vs stored "
                   f"values {kl_vals}; bound 10⁻{m_b.group(1)} vs `VERIFY_KL_BAR_E2A` = {bar_v:g}; {m_n.group(1)} "
                   f"distinct counting the {m_n.group(2)} smoke runs vs {len(cnt)} ledger keys over {n_smk} smoke "
                   f"runs with keys beyond the run's)")
    else:
        figs109 = "the patched figures were not parsed"
    pf_109 = None if hp109 else patch_finding(
        f"N4(iii): the preprint reads '{q109}'",
        [rec_line("- Preprint :109 reads '311 distinct verified forward passes", upto="one in every four choice reads'.")],
        [pq(n_, "311 distinct verified") for n_ in hp109r],
        f"the run verified {len(full_ver)} of its {len(full_all):,} choice forwards (every fourth), all at KL = 0.0 "
        f"against a bar of 1e-6; the ledger holds {len(cnt)} distinct keys = {len(fv)} run + {len(s3only)} smoke3-only "
        f"+ {len(s2only)} smoke2-only", figs109)
    o((f"- Preprint :{hp109[0]} reads '{q109}'." if hp109 else
       f"- Preprint :{','.join(map(str, hp109r)) or '?'} no longer reads '{q109}' (finding on the patch {pf_109}, below).")
      + f" The 'one in every four' belongs to {len(full_ver)}/{len(full_all)}; "
      f"{len(cnt)} also counts {len(s3only) + len(s2only)} smoke keys. Every stored value is exactly 0.0, against a "
      f"declared bar of 1e-6: the g3′ clause-1 bar ({c1_loc}), carried in the port as `VERIFY_KL_BAR_E2A` "
      f"({bar_loc}); KL = max of the two directions ({skl_loc}; clone `jlens_qwen/e2a.py` `verify_kl = max(k1, k2)`). "
      f"The re-forward runs on the same token ids as the read (clone `final2, _ = model.forward(ids, ...)`), so the "
      f"ledger shows the read is deterministic on identical input; it does not by itself speak to the generation "
      f"path (see (iv)).")
    o()
    dup_rows = sum(v - 1 for v in dup.values())
    o(f"**One sentence (card 10).** The archived '{len(L)}/{len(L)}' counted the rows of the append-only clause-1 "
      f"ledger, which by design also holds the two smoke runs' verification rows ({n2} + {len(smoke_keys)}), and "
      f"because the smokes reused the run's session indices {dup_rows} of those rows repeat {len(dup)} (arm, session, "
      f"choice) keys; the distinct keys are {len(cnt)}, of which {len(full_ver)} are the run's own every-fourth "
      f"verifications ({loc('archive/RESULTS-cycles3-4.md', 'g3′ clause 1 final ledger 360/360 choice forwards at KL = 0.0')}; "
      f"{loc('RESULTS.md', 'holds 360 rows over 311 distinct (arm, session, choice) keys', 'non-null `verify_kl` in the session rows. Nothing about the assertion')}).")
    o()
    H13 = "HANDOFF-2026-09-13-design.md"
    c10_loc = loc(H13, '**10** — "360/360 at KL = 0" counts rows', "`verify_every = 4`, 49 duplicated smoke rows.",
                  working_tree=True) if H13 in HAND else None
    c10_txt = ('"360/360 at KL = 0" counts rows: 311 distinct verified forwards at `verify_every = 4`, '
               '49 duplicated smoke rows')
    c10_ok = H13 in HAND and c10_txt in " ".join(HAND[H13].split())
    if c10_loc:
        o(f"- Card 10 as the design handoff words it ({c10_loc}; untracked, read only): '{c10_txt}' "
          f"(text found: {c10_ok}). Its {dup_rows} duplicated rows and {len(cnt)} distinct keys reproduce above; "
          f"its 'at `verify_every = 4`' holds for the run's {len(full_ver)} only. The other "
          f"{len(s3only) + len(s2only)} distinct keys ({len(s3only)} smoke3-only, {len(s2only)} smoke2-only) come "
          f"from the smokes, which verified every choice (rows {n2 + 1}-{n2 + len(smoke_keys)} = all "
          f"{len(smoke_keys)} smoke3 choices and rows 1-{n2} = all inferred smoke2 choices, asserted above; clone "
          f"`verify_every = 1 if args.smoke else 4`). The note's gloss should keep that split.")
        o()
    rr = loc("results/raw/2026-08-18_rule26_recheck_choiceread.txt", "[PASS] e2a choice-read verify KL",
             "[PASS] archived label_mass reproduced")
    rr_txt = pinned_text("results/raw/2026-08-18_rule26_recheck_choiceread.txt")
    rr_lines = rr_txt.split("\n")
    a_, b_ = (int(x) for x in rr.split(":")[-1].split("-"))
    rr_block = "\n".join(rr_lines[a_ - 1:b_])
    m_kl = re.search(r"got\s+(\d+)/(\d+) nonzero", rr_block)
    m_pk = re.search(r"archived pick reproduced\s+expected\s+(\d+)/(\d+)\s+got\s+(\d+)/(\d+)", rr_block)
    m_pa = re.search(r"archived p_a reproduced.*got\s+([0-9.e+-]+)", rr_block)
    m_lm = re.search(r"archived label_mass reproduced.*got\s+([0-9.e+-]+)", rr_block)
    assert m_kl and m_pk and m_pa and m_lm, rr_block
    r26 = {"verify_kl_nonzero": f"{m_kl.group(1)}/{m_kl.group(2)}", "picks": f"{m_pk.group(3)}/{m_pk.group(4)}",
           "max_abs_dp_a": m_pa.group(1), "max_abs_dlabel_mass": m_lm.group(1), "locator": rr}
    o(f"- Separate identity record (not the {len(cnt)}): the rule-26 recheck replayed {m_pk.group(4)} sampled "
      f"archived choice points through the ported `valence_core.readout.choice_read`, from the archived texts: "
      f"verify KL {r26['verify_kl_nonzero']} nonzero, picks {r26['picks']}, max |Δp_a| {r26['max_abs_dp_a']}, max "
      f"|Δlabel_mass| {r26['max_abs_dlabel_mass']} ({rr}; read from the raw: log-only, no JSON artifact).")
    o()
    fig("311 distinct verified forward passes at KL = 0", f"{len(cnt)} distinct keys, all kl == 0.0 ({len(L)} rows)",
        "data/e2a/g3prime_kl.jsonl (distinct (arm, session, choice))", "reproduced", "N4(iii)",
        f"run proper verified {len(full_ver)} of {len(full_all)} (every fourth); {len(s3only) + len(s2only)} keys are smoke")
    fig("360 (earlier count)", f"{len(L)} rows = {n2} smoke2 + {len(smoke_keys)} smoke3 + {len(full_ver)} run; "
        f"{dup_rows} duplicate rows over {len(dup)} keys",
        f"data/e2a/g3prime_kl.jsonl rows; {loc('archive/RESULTS-cycles3-4.md', 'g3′ clause 1 final ledger 360/360 choice forwards at KL = 0.0')}", "reproduced", "N4(iii)")
    fig(f"one in every four choice reads (preprint :{hp109r[0] if hp109r else '?'})",
        f"{len(full_ver)}/{len(full_all)} = {len(full_ver) / len(full_all):.4f}",
        "data/e2a/sessions.jsonl choices[].verify_kl non-null", "reproduced", "N4(iii)",
        f"applies to {len(full_ver)}, not to {len(cnt)}" + (f" (the patched sentence: finding on the patch {pf_109})" if pf_109 else ""))
    fig(f"rule-26 recheck {r26['verify_kl_nonzero']} nonzero, {r26['picks']} picks",
        "not recomputed (needs the model); values read from the raw", rr, "log-only", "N4(iii)/(iv)")

    # ==================================================================== (iv)
    o("## (iv) Cached-generation disclosure")
    o()
    G1 = pinned_json("data/e2a/g1_kernel_gate.json")
    o("**What the licence is.** `data/e2a/g1_kernel_gate.json`:")
    o()
    for fr in ("0.1", "0.2"):
        rows = G1["rows"][fr]["rows"]
        mx = max(max(r["kl_c_u"], r["kl_u_c"]) for r in rows)
        keys_ = sorted(set(k for r in rows for k in r))
        npos = collections.Counter(r["pole"] for r in rows)
        o(f"- frac {fr}: {len(rows)} rows = {len(set(r['probe'] for r in rows))} probe prefixes × poles {dict(npos)}; "
          f"row keys {keys_} (no position or step field); max over rows of max(KL(c‖u), KL(u‖c)) = {mx:.4e} "
          f"(stored max_kl {G1['results'][fr]['max_kl']:.4e}); bar {G1['gate']}; pass {G1['results'][fr]['pass']}; "
          f"template_family {G1['template_family']}.")
    o()
    cl2 = loc("CLAUDE.md", "*[annotation, PI-approved 2026-09-05, e2d disposition §6(a)] A", "T-step identity is its own gate.*")
    g1_rows01 = G1["rows"]["0.1"]["rows"]
    g1_nprobe = len(set(r["probe"] for r in g1_rows01))
    g1_npole = len(set(r["pole"] for r in g1_rows01))
    g1_kl01 = G1["results"]["0.1"]["max_kl"]
    g1_kl02 = G1["results"]["0.2"]["max_kl"]
    g1_bar = G1["gate"]
    T10 = pinned_json("data/e2d/tstep_check_f010.json")
    g1_why = T10["g1_gate"]["why"]
    pos_loc = loc("RESULTS.md", "say.** g1 measures the first-response-token DISTRIBUTIONS and bounds")
    pre_g1 = loc("archive/RESULTS-cycles3-4.md", "family at dose_e2a before any session runs (g1: next-token",
                 "KL(cached‖uncached) ≤ 1e-3 nats, both poles, ≥16 probe prefixes;")
    g1q = quote_lines(f"{CLONE}/scripts/e2a_g1_kernel_gate.py",
                      ["For each candidate frac {0.10, 0.20} x pole {+,-}: 16 session-style probe",
                       "KL(uncached||cached) <= 1e-3 nats at every probe."], clone=True)
    g1q_rng = (f"{CLONE}/scripts/e2a_g1_kernel_gate.py:" + g1q[0].split(": ", 1)[0].split(":")[-1] + "-"
               + g1q[1].split(": ", 1)[0].split(":")[-1])
    temp_q = quote_lines(f"{CLONE}/jlens_qwen/e2a.py", ["TEMP = 0.7"], clone=True)[0]
    div10 = [r for r in T10["rounds"] if not r["identical"]]
    # what 'first_divergent_position' indexes: the producer's loop and the adapter's token list (pinned code)
    fd_loc = loc("scripts/e2d_tstep_check.py", "first_div = None", "first_div = k")
    gen_loc = loc("valence_core/adapters/qwen_mlx.py", "generated: list[int] = []", "token_ids=generated,")
    strip_loc = loc("valence_core/adapters/qwen_mlx.py", "text=self.decode(generated).strip(),")
    ids_stored = any("ids" in r or "token_ids" in r for r in T10["rounds"])
    d0 = div10[0] if div10 else None
    d0_idx = d0["first_divergent_position"] if d0 else None
    d0_first_char_shared = (d0["text_cached"][:1] == d0["text_uncached"][:1]) if d0 else None
    pos1_loc = loc("RESULTS.md", "either. 23/24 M-shaped rounds identical at f = 0.10; the one divergence is",
                   "at POSITION 1, where the two paths produce entirely different sentences.")
    first_loc = loc("RESULTS.md", "Not a late drift — the two paths choose a different FIRST token and never",
                    "reconverge.")
    # round 4, finding 2: the record's 1-based count beside the 0-based index, and the adapter's leading-whitespace rule
    T10_maxlen = T10["verdict"]["positions_verified"]
    posn_loc = loc("RESULTS.md", f"temp 0.7, and **the same per-round seed on both paths**. Positions 1..{T10_maxlen}")
    ws_loc = loc("valence_core/adapters/qwen_mlx.py", "def is_stop(tok: int) -> bool:", "content_seen = True")
    div_second = d0 is not None and d0_idx == 1 and not d0_first_char_shared
    if div_second:
        div_paren = (f"the T-step check observed no divergence at the first sampled token: its one divergence at "
                     f"{T10['frac']} begins at 0-based token index {d0_idx}, the SECOND sampled token, and index 0 "
                     f"agreed on both paths ({fd_loc}: `first_div = k` over the 0-based token-id lists; {gen_loc}: "
                     f"every sampled token is appended from the first). The stored texts are stripped ({strip_loc}) "
                     f"and share no first character (cached `{d0['text_cached'][:6]}...`, uncached "
                     f"`{d0['text_uncached'][:6]}...`), so the shared index-0 token decoded to whitespace only; that "
                     f"index {d0_idx} is the first CONTENT token on both paths is an inference, not deducible (the "
                     f"artifact stores {'token ids' if ids_stored else 'no token ids'}, and the adapter admits more "
                     f"than one leading whitespace token before content, {ws_loc}). So the observed divergence lies "
                     f"outside the position g1 gates; the clause above is the in-principle point")
    else:
        div_paren = (f"the one divergence at {T10['frac']} begins at 0-based token index "
                     f"{d0_idx if d0 else '-'} ({fd_loc})")
    NOTES.append(f"T-step 'position': `first_divergent_position` in data/e2d/tstep_check*.json is a 0-based index into "
                 f"the sampled token ids ({fd_loc}; {gen_loc}), while the verdict's 'positions 1..N' is a 1-based count "
                 f"of tokens. The record's 'at POSITION 1' ({pos1_loc}) is right as that stored 0-based index. What "
                 f"invites the first-token reading is the record's own 1-based 'Positions 1..{T10_maxlen}' beside it "
                 f"({posn_loc}) and its 'choose a different FIRST token' ({first_loc}): at {T10['frac']} the first "
                 f"sampled token (index 0) was identical on both paths"
                 + (" and decoded to whitespace (the stored texts are stripped and share no first character)"
                    if div_second else "")
                 + f", and the paths diverged from index {d0_idx}. 'FIRST token' holds, if at all, only as 'first "
                 f"content token', and that is inferred, not shown: the artifact stores "
                 f"{'token ids' if ids_stored else 'no token ids'}, and the adapter admits more than one leading "
                 f"whitespace token ({ws_loc}). Record prose, not a figure; no (i) figure depends on it. The note "
                 f"should not say the divergence was at the first token.")
    o(f"Operationally, 'licensed for first-token identity only' means: the gate compared the cached and the uncached "
      f"steered forward's next-token DISTRIBUTION at the first response position of {g1_nprobe} session-shaped "
      f"prefixes per pole ({g1_npole} poles) and bounded their symmetric KL at {g1_kl01:.3e} (dose 0.10) and "
      f"{g1_kl02:.3e} (dose 0.20) against a bar of {g1_bar:g}. The position is not a field of the gate artifact (its rows have "
      f"no position or step key, above); it is stated by the pre-registration ('next-token', {pre_g1}), by the record's "
      f"T-step entry ('g1 measures the first-response-token DISTRIBUTIONS', {pos_loc}) and by the T-step artifact's "
      f"`g1_gate.why` ('{g1_why}'); the producing gate script (gitignored clone, context only) says the same: "
      f"{g1q_rng} ('first-response-token distributions from the cached O(T) two-segment stream vs the uncached "
      f"positional re-forward'). That licenses a read of that distribution (a first-token read). "
      f"It does not license identity of SAMPLED tokens -- not at steps 2..T, where the cached path carries a KV stream, "
      f"and not even at the first token, where temperature sampling (e2a: `TEMP = 0.7`, clone {temp_q.split(': ', 1)[0]}; "
      f"the T-step check ran at {T10['temp']}) can resolve a near-tie differently under a {g1_kl01:.1e} distributional "
      f"difference ({div_paren}). Ledger rule 2's annotation: {cl2}. Generation "
      f"identity is measured separately (T-step gate):")
    o()
    hp262 = lines_with(pre, "licensed for first-token identity only")
    # round 9, fix round: the disclosure's scope, which (iv) and the PI items read 'as worded', located by text
    S262 = ("Generation on the Qwen self-administration and present-tense cells ran on a cached path", "Appendix D")
    ok262 = bool(hp262) and all(q_ in sentence_at(pl[hp262[0] - 1], "licensed for first-token identity only", 2000)
                                for q_ in S262)
    pf_262 = None if ok262 else patch_finding(
        f"N4(iv): the preprint's disclosure reads '{S262[0]} licensed for first-token identity only', pointing to "
        f"{S262[1]}", [rec_line('- Preprint :262: "Generation on the Qwen')],
        [pq(n_, "licensed for first-token identity only") for n_ in (hp262 or lines_with(pre, "cached path"))],
        "the cached cells of record are listed in (iv)")
    sc262 = "" if ok262 else f" (the audited text's wording; finding on the patch {pf_262}, below)"
    if hp262:
        o(f"- Preprint :{hp262[0]}: \"{sentence_at(pl[hp262[0] - 1], 'licensed for first-token identity only')}\"")
        o()
    tst = {}
    for p in ("data/e2d/tstep_check_f010.json", "data/e2d/tstep_check.json"):
        T = pinned_json(p)
        v = T["verdict"]
        div = [r for r in T["rounds"] if not r["identical"]]
        nd = v["n_rounds"] - v["n_identical"]
        lo, hi = clopper_pearson(nd, v["n_rounds"])
        mcap = re.search(r"STOP_CAP is (\d+)", v.get("position_coverage_note", ""))
        pv = T.get("provenance", {})
        tst[p] = {"frac": T["frac"], "n_rounds": v["n_rounds"], "n_identical": v["n_identical"],
                  "positions_verified": v["positions_verified"],
                  "divergent": [(r["session"], r["round"], r["first_divergent_position"]) for r in div],
                  "cp95_divergence": [lo, hi], "stop_cap": int(mcap.group(1)) if mcap else None,
                  "adapter": pv.get("adapter"), "choice_window_declared": pv.get("choice_window_declared"),
                  "legacy_truncate_512": pv.get("legacy_truncate_512"), "item": T.get("item"),
                  "proposal": T.get("proposal")}
        o(f"- `{p}` ({T.get('item')}, {T.get('proposal')}; e2d-format rounds through the ported adapter "
          f"`{pv.get('adapter')}`, choice_window_declared {pv.get('choice_window_declared')}, legacy_truncate_512 "
          f"{pv.get('legacy_truncate_512')}): frac {T['frac']}, temp {T['temp']}, L{T['layer']}, same seed per path; "
          f"**{v['n_identical']}/{v['n_rounds']} rounds token-identical**; divergent rounds (session, round, "
          f"first divergent token index, 0-based: index 0 = the first sampled token): {tst[p]['divergent']}; longest "
          f"cached round {v['positions_verified']} tokens (the verdict's 'positions 1..{v['positions_verified']}', a "
          f"1-based count; STOP_CAP {tst[p]['stop_cap']}, from the verdict's coverage note); divergence rate {nd}/{v['n_rounds']} = "
          f"{nd / v['n_rounds']:.4f}, Clopper-Pearson 95% [{lo:.4f}, {hi:.4f}] (computed-new); "
          f"`g1_gate.is_tstep_licence` = {T['g1_gate']['is_tstep_licence']}.")
    tstep_loc = loc('RESULTS.md', 'cached vs uncached generation is NOT token-identical at the e2a/e2b dose',
                    'refutation: **agreement in distribution is not identity in sampled')
    o(f"- Record: {tstep_loc} (:{loc('RESULTS.md', '23/24 M-shaped rounds identical at f = 0.10').split(':')[-1]} "
      f"reads '23/24 M-shaped rounds identical at f = 0.10'). The T-step rounds are e2d-format ('M-shaped') rounds, not "
      f"e2a or e2b transcripts; the check is at the e2a/e2b dose and layer, not on their corpora.")
    o()
    o("**Which cells generated on the cached path (Qwen).** Status per cell: *reproduced* where a committed JSON field "
      "records the path; *log-only* where only a raw or log line does; the clone's code is cited as context, never as "
      "record.")
    o()
    full_raw = pinned_text("results/raw/2026-08-09_e2a_full.txt")
    cl = lines_with(full_raw, "round generation path (g1r, mechanical): cached")
    st = lines_with(full_raw, "uncached path (g1)")
    gen_by_arm = collections.Counter()
    for r in S:
        gen_by_arm[r["arm"]] += r["n_rounds_generated"]
    uc_needle = 'use_cached_rounds = g1["results"][str(frac)]["pass"]'
    uc_loc = quote_lines(f"{CLONE}/scripts/e2a_sessions.py", [uc_needle], clone=True)[0].split(": ", 1)[0]
    stale_loc = loc("archive/RESULTS-cycles3-4.md", '"uncached path (g1)" string below the correct operative')
    sm_lines = {}
    for nm in ("smoke", "smoke2", "smoke3"):
        t_ = pinned_text(f"results/raw/2026-08-09_e2a_{nm}.txt")
        sm_lines[nm] = (lines_with(t_, "round generation path (g1r, mechanical): cached"),
                        lines_with(t_, "uncached path (g1)"))
    l48 = loc("archive/RESULTS-cycles3-4.md", "`d4791bdc4877da3d`), L48; candidate fracs {0.10, 0.20} only (0.40",
              "the same dose.")
    sham_unst = loc("archive/RESULTS-cycles3-4.md", "±axis ≥ 96 sessions (48/counterbalance map); sham (both labels",
                    "unsteered) ≥ 32 — empirical null")
    o(f"- **e2a full run and smokes 2-3** (log-only): all {len(S)} sessions, steered and sham. Every launch of the "
      f"full run prints 'round generation path (g1r, mechanical): cached' (`results/raw/2026-08-09_e2a_full.txt`@{PIN}:"
      f"{','.join(map(str, cl))}); smoke2 `results/raw/2026-08-09_e2a_smoke2.txt`@{PIN}:"
      f"{','.join(map(str, sm_lines['smoke2'][0]))}, smoke3 `results/raw/2026-08-09_e2a_smoke3.txt`@{PIN}:"
      f"{','.join(map(str, sm_lines['smoke3'][0]))}. Context (clone): the runner sets `{uc_needle}` ({uc_loc}) and "
      f"g1r's pass at 0.1 is {G1['results']['0.1']['pass']}. The first smoke (dose "
      f"{re.search(r'e2a sessions: dose ([0-9.]+)', pinned_text('results/raw/2026-08-09_e2a_smoke.txt')).group(1)}, "
      f"the template incident, before g1r) printed only 'uncached "
      f"path (g1)' (`results/raw/2026-08-09_e2a_smoke.txt`@{PIN}:{','.join(map(str, sm_lines['smoke'][1]))}; cached "
      f"line: {sm_lines['smoke'][0] or 'none'}). The full raw's 'uncached path (g1)' at :{','.join(map(str, st))} is a "
      f"stale banner string the record names cosmetic ({stale_loc}). `sessions.jsonl` rows carry no path field. "
      f"Generated rounds: {sum(gen_by_arm.values())} ({', '.join(f'{a} {gen_by_arm[a]}' for a in ARMS)}; "
      f"`n_rounds_generated`, reproduced); sham rounds carry no state (vanilla cached), reward/random rounds carry "
      f"±α at L48 along the reward axis (reward) or a frozen random direction (random1/random2) at the same dose "
      f"({l48}; sham 'both labels unsteered', "
      f"{sham_unst}). Pre-registration permitted it: "
      f"{loc('archive/RESULTS-cycles3-4.md', 'ROUND generation is temperature-sampled → cached O(T) allowed')}; "
      f"unlock pre-committed {loc('archive/RESULTS-cycles3-4.md', 'cached sampled ROUND generation unlocks per the rule-2 carve-out')}; "
      f"g1r entry {loc('archive/RESULTS-cycles3-4.md', 'e2a g1r (v2 templates) — PASS both fracs; cached round')}.")
    # e2a gate corpora (g2 family)
    G2 = {}
    for p, nm, rawp in (("data/e2a/g2_discriminability_v2.json", "g2r", "results/raw/2026-08-09_e2a_g2r.txt"),
                        ("data/e2a/g2_discriminability.json", "g2r2", "results/raw/2026-08-09_e2a_g2r2.txt")):
        D = pinned_json(p)
        rt = pinned_text(rawp)
        fr_ = {k: {"use_cached": v.get("use_cached"), "aucs": v.get("aucs"), "judge_plus": v.get("judge_plus"),
                   "judge_total": v.get("judge_total")} for k, v in D["fracs"].items()}
        gl = lines_with(rt, "(cached=True): generating")
        gn = [int(x) for x in re.findall(r"\(cached=True\): generating (\d+) rounds", rt)]
        G2[nm] = {"path": p, "template_family": D.get("template_family"), "fracs": fr_,
                  "verdict": D.get("verdict"), "raw": rawp, "raw_cached_lines": gl, "raw_n_rounds": gn}
    raw_g2 = pinned_text("results/raw/2026-08-09_e2a_g2.txt")
    g2_unc = lines_with(raw_g2, "(cached=False): generating")
    g2_q = quote_lines(f"{CLONE}/scripts/e2a_g2_discriminability.py",
                       ['use_cached = g1["results"][str(frac)]["pass"]'], clone=True)[0].split(": ", 1)[0]
    sc_q = quote_lines(f"{CLONE}/scripts/e2a_g2_spotcheck.py", ["use_cached=True, ban_ids=ban_ids)"], clone=True)[0].split(": ", 1)[0]
    SC = pinned_json("data/e2a/g2_spotcheck.json")
    sc_raw = pinned_text("results/raw/2026-08-09_e2a_g2check.txt")
    sc_n = re.search(r"val rounds regenerated: (\d+)", sc_raw)
    g2v_loc = loc("archive/RESULTS-cycles3-4.md", "KL-gated per family); g2r2 discriminability verified at the run",
                  "dose (k=2 AUC .759 — the state was readable in the record);")
    judge_loc = loc("archive/RESULTS-cycles3-4.md", "verifiably readable in the record (readable by an embedding probe",
                    "14/32 — the cap on \"readable\"), is not preferentially approached")
    arch_v2 = loc("archive/RESULTS-cycles3-4.md", "v2-era g2 artifacts archived as `*_v2.json`.")

    probe_loc = loc("archive/RESULTS-cycles3-4.md", "primary gating instrument = logistic readout on base-model",
                    "fit-task rounds, AUC on val-task rounds (split declared pre-data);")
    pole_loc = loc("archive/RESULTS-cycles3-4.md", "model-as-judge AB descriptive secondary only. Calibration: 64",
                   "rounds/pole/dose from the e2a pool under the exact session config")
    kcat_loc = loc("archive/RESULTS-cycles3-4.md", "k=1 AUC ≥ 0.70 → qualify, F = 2; else k=2..4 concatenated-record")
    g2_hdr = quote_lines(f"{CLONE}/scripts/e2a_g2_discriminability.py",
                         ["Primary gating instrument: logistic readout on base-model mean-pooled",
                          "(t01-t08), AUC on val-task rounds (t09-t16). Deterministic and seeded."], clone=True)
    g2_hdr_rng = (f"{CLONE}/scripts/e2a_g2_discriminability.py:" + g2_hdr[0].split(": ", 1)[0].split(":")[-1] + "-"
                  + g2_hdr[1].split(": ", 1)[0].split(":")[-1])
    for nm in G2:
        rt_ = pinned_text(G2[nm]["raw"])
        G2[nm]["raw_judge_lines"] = lines_with(rt_, "judge AB (descriptive):")
        G2[nm]["raw_auc_lines"] = lines_with(rt_, ": val AUC ")
    AUC_LABEL = ("AUC of a logistic readout on base-model mean-pooled final-layer embeddings of the round-response "
                 "text (the record's wording; layer: final); contrast: rounds generated at +α vs at −α along the reward axis (64 "
                 "rounds/pole/dose), frac 0.10, records of k concatenated same-pole rounds; scheme: fit on fit-task "
                 f"rounds, AUC on held-out val-task rounds, one split declared pre-data, no cross-validation ({probe_loc}; "
                 f"{pole_loc}; {kcat_loc}; clone {g2_hdr_rng}: fit t01-t08, val t09-t16, context)")
    JUDGE_LABEL = ("model-as-judge AB trials (val-task pairs of a +α and a −α response to the same task) in which "
                   "the model called the +α response 'the better response'")

    def g2desc(nm):
        g = G2[nm]
        parts = []
        for fr, v in g["fracs"].items():
            parts.append(f"frac {fr}: use_cached {v['use_cached']}, AUC by record length k {v['aucs']}, judge "
                         f"{v['judge_plus']} of {v['judge_total']} AB trials judged the +α response better (raw "
                         f":{','.join(map(str, g['raw_auc_lines']))} AUC, :{','.join(map(str, g['raw_judge_lines']))} judge)")
        return (f"`{g['path']}` (template_family {g['template_family']}; {'; '.join(parts)}; raw "
                f"`{g['raw']}`@{PIN}:{','.join(map(str, g['raw_cached_lines']))} '(cached=True): generating "
                f"{'/'.join(map(str, g['raw_n_rounds']))} rounds')")
    o(f"- **e2a readability gate corpora, g2r and g2r2** (reproduced, field `use_cached`): {g2desc('g2r')}; "
      f"{g2desc('g2r2')}. Every AUC here is the {AUC_LABEL}. g2r is the v2-template ladder (its artifacts archived as `*_v2.json`, {arch_v2}); g2r2 is "
      f"the v3 rerun whose k = 2 AUC the verdict cites as the readability condition ({g2v_loc}), together with the "
      f"model-as-judge secondary ({judge_loc}). So the readability AUC and the judge figure were computed on "
      f"cached-generated rounds. Context (clone): the gate sets `use_cached` from the g1 artifact ({g2_q}).")
    o(f"- **e2a first g2 ladder** (log-only, uncached): `results/raw/2026-08-09_e2a_g2.txt`@{PIN}:"
      f"{','.join(map(str, g2_unc))} print '(cached=False): generating ... rounds' (its line 1 reads "
      f"`{raw_g2.split(chr(10))[0]}`); "
      f"its result is superseded by g2r/g2r2.")
    o(f"- **e2a g2 spot-check** (path not found in the record): {sc_n.group(1) if sc_n else '?'} regenerated v3 val "
      f"rounds at frac {SC['frac']} (`data/e2a/g2_spotcheck.json`: no path field; raw "
      f"`results/raw/2026-08-09_e2a_g2check.txt` prints no path); the clone's code generates them with "
      f"`use_cached=True` ({sc_q}). Its FAIL (g2r_stands {SC['g2r_stands']}) mandated the g2r2 rerun; no verdict "
      f"figure rests on it.")
    e2b = {}
    for p in ("data/e2b/h1_sessions.json", "data/e2b/h1u_sessions.json", "data/e2b/h2_sessions.json", "data/e2b/verdict_campaign.json"):
        D = pinned_json(p)
        ss = D["sessions"]
        ngen = sum(len(x["rounds"]) + len(x["choices"]) for x in ss)
        e2b[p] = {"round_path_cached": D["round_path_cached"], "frac": D["frac"], "temp": D["temp"],
                  "n_sessions": len(ss), "n_rounds_generated": ngen, "n_rounds_field": D.get("n_rounds")}
    o("- **e2b arc** (reproduced, field `round_path_cached`): " + "; ".join(
        f"`{p.split('/')[-1]}` {v['round_path_cached']} (frac {v['frac']}, temp {v['temp']}, {v['n_sessions']} sessions, "
        f"{v['n_rounds_generated']} generated rounds{'' if v['n_rounds_field'] is None else ' = n_rounds ' + str(v['n_rounds_field'])})"
        for p, v in e2b.items()) + ".")
    # completeness: every pinned data/**/*.json(l) carrying a generation-path flag (read-only git grep at the pin)
    PATH_KEYS = ("round_path_cached", "use_cached")
    gg = subprocess.run(["git", "--no-optional-locks", "-C", REPO, "grep", "-l", "-E",
                         r'"(round_path_cached|use_cached)"[[:space:]]*:', PIN, "--", "data/*.json", "data/*.jsonl"],
                        capture_output=True, text=True)
    flagged = sorted(l[len(PIN) + 1:] for l in gg.stdout.split("\n") if l)
    path_vals = {}
    for p in flagged:
        t = pinned_text(p)
        path_vals[p] = dict(collections.Counter(f"{m.group(1)}={m.group(2)}" for m in re.finditer(
            r'"(round_path_cached|use_cached)":\s*(true|false)', t)))
    cached_set = {"data/e2a/g2_discriminability.json", "data/e2a/g2_discriminability_v2.json", *e2b}
    unc = {p: {k.split("=")[1]: v for k, v in c.items()} for p, c in path_vals.items() if p not in cached_set}
    assert set(path_vals) - set(unc) == cached_set, (sorted(path_vals), sorted(cached_set))
    assert all(set(c) == {"false"} for c in unc.values()), unc
    assert not any(p.startswith("data/olmo/") for p in flagged), flagged
    assert all(all(k.endswith("=true") for k in path_vals[p]) for p in cached_set), path_vals
    unc_sess = {p: v for p, v in unc.items() if p.endswith("_sessions.json")}
    unc_other = {p: v for p, v in unc.items() if not p.endswith("_sessions.json")}
    d1loc = loc("RESULTS.md", "**FLAG 1 — ROUND PATH. D1 ran UNCACHED. e2a and e2b both ran CACHED")
    o(f"- **Completeness of the path flags** (reproduced): a read-only `git grep` at the pin over every "
      f"`data/*.json`/`*.jsonl` finds {len(path_vals)} files carrying `round_path_cached` or `use_cached`; the "
      f"{len(cached_set)} with `true` are exactly the g2r/g2r2 and e2b files above; the rest carry only `false`. "
      f"OLMo/box artifacts carry no such field (the box's own cached-generation gate, `data/olmo/cached_gen_*.json`, "
      f"is outside this Qwen disclosure).")
    o("- **Not cached** (reproduced, same field, counts of its occurrences): session artifacts "
      + "; ".join(f"`{p}` {v}" for p, v in unc_sess.items())
      + "; stage or analysis artifacts "
      + "; ".join(f"`{p}` {v}" for p, v in unc_other.items())
      + f"; e2d D1 has no such field and ran uncached per {d1loc} (log-only).")
    pf = loc("PROPOSAL-f-natural-reinforcer-screen.md", "retention under `results/raw/`. No steering anywhere ⇒ cached sampling",
             "throughout; the kernel gate is moot;")
    f1q = quote_lines(f"{CLONE}/scripts/f_sessions.py", ["cached decoding (ops kernel for numerics continuity with f0",
                                                         "Plain cached generation, ops kernel, newline stop, scaffold ban,"], clone=True)
    f_nd = lines_with(pinned_text('results/raw/2026-08-10_f_ndecl.txt'), 'cached vanilla path')
    o(f"- **f1** (log-only) generated on a cached VANILLA path (no state anywhere): {pf}; "
      f"`results/raw/2026-08-10_f_ndecl.txt`@{PIN}:{','.join(map(str, f_nd))}; context (clone) "
      f"{'; '.join(q.split(': ', 1)[0] for q in f1q)}. The first-token licence question (steered cached vs uncached) "
      f"does not arise there; the record holds no dose-0 identity check "
      f"({loc('RESULTS.md', 'cached path would need its own gate (the g1 artifact has no frac-0 row;')}). Outside the "
      f"preprint's disclosure scope as worded{sc262}; listed for completeness.")
    o()
    o("**The choice reads: separate forwards; path independence is a code argument.**")
    o()
    o("```")
    for q in quote_lines("valence_core/readout.py", ["def choice_read(adapter: ModelAdapter, transcript_text: str,",
                                                    "Takes no injections by construction (rule 5 horn (a)).",
                                                    "ids = adapter.encode(transcript_text)",
                                                    "res = adapter.forward(ids, capture_layers=())",
                                                    "res2 = adapter.forward(ids, capture_layers=())",
                                                    "out.verify_kl = symmetric_kl(p, softmax(res2.logits))"]):
        o(q)
    for q in quote_lines(f"{CLONE}/jlens_qwen/e2a.py", ["def choice_read(model, transcript_text, tag_a, tag_b, tag_ids,",
                                                       "ids = model.encode(transcript_text)",
                                                       "final, _ = model.forward(ids, capture_layers=[])",
                                                       "final2, _ = model.forward(ids, capture_layers=[])",
                                                       'out["verify_kl"] = max(k1, k2)',
                                                       "if use_cached:",
                                                       "session = SteeredStreamSession(model, {})"], clone=True):
        o(q)
    for q in quote_lines(f"{CLONE}/scripts/e2a_sessions.py", ["ch = e2a.choice_read(model, transcript + menu, a, b, tag_ids,",
                                                             "text, ids, _, cap_hit = e2a.generate_round_positional("], clone=True):
        o(q)
    for q in quote_lines("valence_core/e2b/statepresent.py", ["def choice_read_statepresent(adapter: ModelAdapter, transcript_text: str,",
                                                             "res = adapter.forward(ids, capture_layers=(), injections=[injection])",
                                                             "shadow = choice_read(adapter, transcript_text, label_a, label_b,"]):
        o(q)
    o("```")
    o()
    # the 512-token encode window of e2a's reads (log-only counts; the per-index n reproduced)
    wc_loc = loc("RESULTS.md", "- **(1) WINDOW-COVERAGE AUDIT — the primary DV was never clipped.**",
                 "4–6. The DV choice sits at median 205/165 tokens — under half the")
    tr_loc = loc("RESULTS.md", "run.** `MLXLensModel.encode` tail-truncates to the last 512 tokens;",
                 "means **late-session e2a/f choice reads saw a 512-token tail window,")
    rtxt = pinned_text("RESULTS.md")
    wc_a = int(wc_loc.split(":")[-1].split("-")[0])
    wc_rows = {}
    for ln in rtxt.split("\n")[wc_a - 1: wc_a + 30]:
        m = re.match(r"\s*\|\s*(\d)(?: \(DV\))?\s*\|\s*(\d+) / (\d+) / (\d+) / \**(\d+)", ln)
        if m:
            wc_rows[int(m.group(1))] = {"n": int(m.group(2)), "median": int(m.group(3)), "max": int(m.group(4)),
                                        "over_512": int(m.group(5))}
    n_by_idx = {i: sum(1 for r in S if len(r["choices"]) >= i) for i in range(1, 7)}
    wc_n_ok = all(wc_rows.get(i, {}).get("n") == n_by_idx[i] for i in range(1, 7))
    wc_over = sum(v["over_512"] for v in wc_rows.values())
    wc_tot = sum(v["n"] for v in wc_rows.values())
    o(f"In e2a the choice read takes the transcript TEXT (prefix + menu), re-encodes it and runs one plain forward with "
      f"no steering hook and no KV cache; generation opens a fresh stream session per round and never hands its cache "
      f"to the read (clone code above; the e2a runner and read are outside the record, rule-27 note below). The read's "
      f"encode keeps the last 512 tokens of the text ({tr_loc}; log-only): every first-free-choice (DV) read fit "
      f"(index 1: {wc_rows.get(1, {}).get('over_512', '?')} over 512, max {wc_rows.get(1, {}).get('max', '?')} "
      f"tokens), while {wc_over} of e2a's {wc_tot} reads did not (by index: "
      f"{', '.join(f'{i}: {v['over_512']}' for i, v in sorted(wc_rows.items()))}; {wc_loc}; the counts are log-only, "
      f"they need the tokenizer; the per-index read counts {[n_by_idx[i] for i in range(1, 7)]} reproduce from "
      f"`sessions.jsonl`: {'YES' if wc_n_ok else 'NO'}). In e2b the read is the quarantined state-present primitive, "
      f"also a plain `adapter.forward` over the encoded text (with its declared injection) plus the unsteered shadow "
      f"through the same `choice_read`. The generation path therefore decides which words are in the transcript; by "
      f"construction it does not enter the read's computation. That is a code argument, and e2a's code lies outside the "
      f"record. The records bearing on it: the clause-1 ledger ({len(full_ver)} of the run's re-forwards at KL 0.0) shows "
      f"the read is deterministic on identical token ids, not that it is independent of the generation path; the "
      f"rule-26 recheck ({r26['picks']} archived picks reproduced from the archived texts by the ported read, {rr}; "
      f"log-only) shows the archived reads are a function of the archived text through the ported code. Separately, on "
      f"generation identity rather than the read: the e2b H2 smoke produced bit-identical transcripts on both kernel "
      f"paths over 2 sessions ({loc('RESULTS.md', 'The two kernel paths produced BIT-IDENTICAL transcripts', 'of record — 2 sessions, smoke only.')}, "
      f"'{'Not the run of record — 2 sessions, smoke only' if 'of record — 2 sessions, smoke only' in pinned_text('RESULTS.md') else '?'}'; log-only), "
      f"beside the T-step check's {tst['data/e2d/tstep_check_f010.json']['n_rounds'] - tst['data/e2d/tstep_check_f010.json']['n_identical']}"
      f"/{tst['data/e2d/tstep_check_f010.json']['n_rounds']} divergence at dose {tst['data/e2d/tstep_check_f010.json']['frac']}.")
    o()
    cf = loc("archive/RESULTS-cycles3-4.md", "recorded: had g1 passed and sessions run cached, g3's fail would", "bind and e2a would not run.")
    cf2 = loc("archive/RESULTS-cycles3-4.md", "the channel g3 measures is structurally absent from the actual", "choice read; g3-as-specced models a live cached-session read.")
    cfb = loc("archive/RESULTS-cycles3-4.md", "- **Adjudication basis (on the record):** g3-as-written measures the",
              "measured channel is structurally absent from the implemented read.")
    o(f"- Note for readers of the archive: the g3′ amendment's stated basis included that 'the g1 fallback locked all "
      f"generation to the uncached positional path' ({cfb}), and it records a counterfactual, 'had g1 passed and "
      f"sessions run cached, g3's fail would bind and e2a would not run' ({cf}). g1r later passed and the run generated "
      f"cached, so the basis clause's premise no longer held at run time. The same basis also rests on the read: 'the "
      f"implemented choice forward recomputes the transcript from text with no steering in the forward' ({cfb}). The "
      f"record frames g3 as a live cached-SESSION read ({cf2}); the read as built never reuses a session cache (code "
      f"above), and the template amendment pre-committed cached round generation with choice forwards 'state-free "
      f"uncached ... regardless' ({loc('archive/RESULTS-cycles3-4.md', '(choice forwards stay state-free uncached per g3′ clause 1')}). "
      f"No committed entry discusses the counterfactual sentence after the unlock. Reported, not adjudicated.")
    NOTES.append(f"g3′ amendment: its adjudication basis ({cfb}) included 'the g1 fallback locked all generation to the "
                 f"uncached positional path', and it recorded the counterfactual {cf} ('had g1 passed and sessions run "
                 "cached, g3's fail would bind'). Neither is revisited after g1r passed and the run generated cached; the "
                 "basis also rests on the read recomputing from text, which the built read does. Reported for the design "
                 "seat/PI; not adjudicated.")
    bx = loc("scripts/box_cached_gen_smoke.py", "Cached-generation gate + rate measurement (A5 follow-up, rule 2).")
    t10 = tst["data/e2d/tstep_check_f010.json"]
    t20 = tst["data/e2d/tstep_check.json"]
    o(f"- Referent: `scripts/box_cached_gen_smoke.py` ({bx}) is the OLMo/CUDA cached-generation T-step gate (box, "
      f"`OLMoHFAdapter`), not the Qwen e2a identity check; the Qwen T-step records are `data/e2d/tstep_check_f010.json` "
      f"(frac {t10['frac']}, the e2a/e2b dose) and `data/e2d/tstep_check.json` (frac {t20['frac']}).")
    NOTES.append("Block N4 referent: scripts/box_cached_gen_smoke.py is the OLMo/CUDA (box) cached-generation T-step gate; "
                 f"the Qwen cached-path identity records are data/e2d/tstep_check_f010.json ({t10['n_identical']}/"
                 f"{t10['n_rounds']} at {t10['frac']}) and data/e2d/tstep_check.json ({t20['n_identical']}/{t20['n_rounds']} "
                 f"at {t20['frac']}), both on e2d-format rounds.")
    bc_loc = loc("RESULTS.md", "512-token tail truncation collapsed the steering boundary to ZERO on 270 of",
                 "over the whole tail window, not the round-task span;")
    r28 = loc("CLAUDE.md", "**Encode-side truncation is a delivery-geometry")
    H04 = "HANDOFF-2026-09-04-design.md"
    c9_loc = (loc(H13, "Cards 1–8 as in the 09-04 handoff. New: **9** — e2a's 512-token tail",
                  "generations (free3–free5 only; DV read untouched); methods disclosure.", working_tree=True)
              if H13 in HAND else "HANDOFF-2026-09-13-design.md: absent")
    c9_txt = ("e2a's 512-token tail truncation collapsed the generation-side steering boundary on 270/1,894 "
              "generations (free3–free5 only; DV read untouched); methods disclosure")
    c9_ok = H13 in HAND and c9_txt in " ".join(HAND[H13].split())
    c9_pin = loc("results/raw/2026-10-04_m-v1.8_referent_check.txt",
                 "HANDOFF-2026-09-13-design.md:148–150, card 9: 'e2a's 512-token tail truncation collapsed the",
                 "untouched)'. The claim itself is true:")
    c8_h04 = (loc(H04, "uncached; e2a/e2b's cached generation is review-round card 8;", working_tree=True)
              if H04 in HAND else "HANDOFF-2026-09-04-design.md: absent")
    pk10 = loc("PROPOSAL-k-echo-channel.md", '"Review card 10" → the Stage B finding it named (e2a verified every')
    n_gen = sum(gen_by_arm.values())
    NOTES.append(f"Review card 9 as the design handoff numbers it ({c9_loc}, untracked, read only; text found: {c9_ok}; "
                 f"quoted at the pin by {c9_pin}): e2a's 512-token encode tail collapsed the generation-side steering "
                 f"boundary to 0 on 270 of {n_gen} archived generations, so those rounds carried the state over the "
                 f"whole tail window rather than the round-task span ({bc_loc}; ledger rule 28(d), {r28}). The {n_gen} "
                 f"reproduces (sum of `n_rounds_generated`); the 270 is log-only (it needs the tokenizer). It is a "
                 f"delivery-geometry fact about the generated text, distinct from the cached-vs-uncached path; the "
                 f"README paragraph in (iv) now carries it as one log-only clause.")
    o()
    g2r2 = G2["g2r2"]["fracs"]["0.1"]
    readme = (
        "**Cached-generation disclosure.** On Qwen, the round text of the e2a self-administration run (all "
        f"{len(S)} sessions, steered and sham, and its second and third smokes), of e2a's readability-gate corpora "
        f"(g2r and g2r2, "
        + (f"{G2['g2r']['raw_n_rounds'][0]} rounds each"
           if len(set(G2['g2r']['raw_n_rounds'] + G2['g2r2']['raw_n_rounds'])) == 1
           else f"{G2['g2r']['raw_n_rounds']} and {G2['g2r2']['raw_n_rounds']} rounds")
        + f" at dose 0.10; the readability AUC {G2['g2r2']['verdict']['auc']} that the e2a verdict cites -- a logistic "
        f"readout on base-model mean-pooled final-layer embeddings of the round text, +α vs −α rounds, records of "
        f"{G2['g2r2']['verdict']['k']} concatenated rounds, fit on fit-task rounds and scored on held-out val-task "
        f"rounds -- and its model-as-judge secondary, {g2r2['judge_plus']} of {g2r2['judge_total']} AB trials judging "
        "the +α response better, were computed on g2r2's corpus), and of the e2b present-tense arc (H1, H1-u, H2 and the verdict campaign) was generated on a "
        "cached (KV-stream) decoding path. The first g2 ladder (before g1r) ran uncached; e2d, the PROPOSAL-k Stage 1 "
        "sessions and the format recon generated uncached; f1 generated on a cached path with no state injected. The "
        "cached path was licensed by a kernel gate (`data/e2a/g1_kernel_gate.json`) that compares the cached and "
        f"uncached steered forwards' next-token distributions at the first response token only ({g1_nprobe} prefixes "
        f"x {g1_npole} poles per dose; max symmetric KL {g1_kl01:.2e} at dose 0.10 against a {g1_bar:g} bar). That "
        "licenses reads of the first-token distribution, not the identity of sampled tokens or of whole rounds. A later "
        "T-step check at the e2a/e2b dose, run on e2d-format rounds through the ported adapter "
        f"(`data/e2d/tstep_check_f010.json`), found {t10['n_identical']} of {t10['n_rounds']} rounds token-identical "
        f"between the paths, the one divergence beginning at the second sampled token (0-based index "
        f"{d0_idx}; the first sampled token was identical on both paths"
        + (" and decoded to whitespace" if div_second else "")
        + ") (Clopper-Pearson 95% for the divergence rate "
        f"{t10['cp95_divergence'][0]:.3f}-{t10['cp95_divergence'][1]:.3f}); at dose {t20['frac']}, "
        f"{t20['n_identical']} of {t20['n_rounds']}. Neither path is the reference: they are two samplers whose "
        f"first-token distributions agree (symmetric KL ≤ {g1_kl01:.1e} at dose 0.10), and every verdict was computed on a corpus "
        "produced by one of them. The choice reads, which carry every primary DV, are not generated: each is a "
        "separate, uncached forward pass over the transcript text (in e2a, unsteered, over the text's last 512 tokens, "
        "a window every first-free-choice read fit; in e2b, with the declared injection plus an unsteered shadow; "
        "`valence_core/readout.py`, `valence_core/e2b/statepresent.py`). In e2a, "
        f"{len(full_ver)} of the {len(full_all)} choice forwards (every fourth) were re-run on identical token ids at KL "
        "exactly 0.0 (`data/e2a/g3prime_kl.jsonl`); that shows the read is deterministic, while its independence from "
        "the generation path rests on the code: the read takes the text, never the generation cache. The generation "
        "path decides which sentences the transcripts contain, not how a choice was read from them. Separately, and "
        "not a cached-path matter: in the e2a run the same 512-token encode tail collapsed the generation-side "
        f"steering boundary to 0 on 270 of {n_gen} generated rounds (free rounds 3-5 whose prefix plus segment "
        "exceeded 512 tokens), so those rounds carried the state over the whole tail window rather than the "
        "round-task span; the first-free-choice read was never clipped "
        f"({bc_loc}; :{wc_loc.split(':')[-1]}; "
        "the 270 is log-only).")
    scope = ("Generation in the Qwen e2a and e2b cells, including e2a's readability-gate corpora, ran on a cached path "
             f"whose licence covers the first-token distribution only ({t10['n_rounds'] - t10['n_identical']} of "
             f"{t10['n_rounds']} rounds differed from the uncached path in the T-step check at the e2a/e2b dose); the "
             "choice reads are separate uncached forwards over the transcript text, which by construction take nothing "
             "from the generation path but its text.")
    o("**README paragraph (draft):**")
    o()
    o(readme)
    o()
    o("**Scope sentence for the note (draft):**")
    o()
    o(scope)
    o()
    fig("cells generated on the cached path: e2a full run + smoke2/smoke3",
        f"cached ({len(S)} sessions; {sum(gen_by_arm.values())} generated rounds, reproduced from n_rounds_generated)",
        f"results/raw/2026-08-09_e2a_full.txt@{PIN}:{','.join(map(str, cl))}; smoke2 :{','.join(map(str, sm_lines['smoke2'][0]))}; "
        f"smoke3 :{','.join(map(str, sm_lines['smoke3'][0]))}; clone {uc_loc} (context)",
        "log-only", "N4(iv)", "sessions.jsonl carries no path field")
    fig("cells generated on the cached path: e2a g2r and g2r2 (readability gate; judge secondary)",
        f"use_cached g2r {G2['g2r']['fracs']['0.1']['use_cached']}, g2r2 {G2['g2r2']['fracs']['0.1']['use_cached']} "
        f"(frac 0.1; rounds per the raws {G2['g2r']['raw_n_rounds']} / {G2['g2r2']['raw_n_rounds']})",
        "data/e2a/g2_discriminability_v2.json (g2r), data/e2a/g2_discriminability.json (g2r2) fracs.0.1.use_cached",
        "reproduced", "N4(iv)", f"the verdict's AUC {G2['g2r2']['verdict']['auc']} (k = {G2['g2r2']['verdict']['k']}; the "
        f"{AUC_LABEL}) and judge {g2r2['judge_plus']} of {g2r2['judge_total']} {JUDGE_LABEL} rest on g2r2 "
        f"({g2v_loc}; {judge_loc})")
    fig("cells NOT cached: e2a first g2 ladder", "cached=False at both fracs",
        f"results/raw/2026-08-09_e2a_g2.txt@{PIN}:{','.join(map(str, g2_unc))}", "log-only", "N4(iv)", "superseded")
    fig("e2a g2 spot-check path", "the record states none; clone code use_cached=True",
        f"data/e2a/g2_spotcheck.json (no field); results/raw/2026-08-09_e2a_g2check.txt (no line); clone {sc_q}",
        "not found", "N4(iv)", "no verdict figure rests on it")
    fig("cells generated on the cached path: e2b H1, H1-u, H2, verdict campaign",
        "; ".join(f"{p.split('/')[-1]} {v['round_path_cached']}" for p, v in e2b.items()),
        "data/e2b/*.json round_path_cached", "reproduced", "N4(iv)")
    fig("cells NOT cached: e2d D2/D3, k1, format recon F0-F2 (and the D2 analysis and format-recon timing artifacts)",
        "; ".join(f"{p.split('/')[-1]} {v}" for p, v in unc.items()),
        "round_path_cached in those JSONs; completeness by a read-only git grep at the pin over data/*.json(l)",
        "reproduced", "N4(iv)", f"e2d D1 uncached is log-only ({d1loc})")
    fig("cells generated on the cached path: f1 (vanilla, no state)", "cached vanilla",
        f"{pf}; results/raw/2026-08-10_f_ndecl.txt@{PIN}:{','.join(map(str, f_nd))}", "log-only", "N4(iv)",
        "outside the preprint's disclosure scope as worded" + sc262)
    fig("first-token licence (g1): max KL 7.11e-4 / 7.39e-4, bar 1e-3, no position dimension",
        f"{g1_kl01:.4e} / {g1_kl02:.4e}; rows keyed {sorted(set(k for r in g1_rows01 for k in r))}",
        "data/e2a/g1_kernel_gate.json results, rows", "reproduced", "N4(iv)",
        f"'first response position' is not in the artifact: {pos_loc}; tstep JSON g1_gate.why; {pre_g1}")
    fig("T-step identity 23/24 at 0.10, 22/24 at 0.20",
        f"{t10['n_identical']}/{t10['n_rounds']} (divergence from 0-based token index {t10['divergent'][0][2] if t10['divergent'] else '-'}, "
        f"the second sampled token; index 0 agreed); "
        f"{t20['n_identical']}/{t20['n_rounds']}",
        "data/e2d/tstep_check_f010.json, tstep_check.json verdict", "reproduced", "N4(iv)",
        "e2d-format rounds through the ported adapter, not e2a/e2b transcripts")
    fig("e2a reads: 512-token encode window; DV never clipped",
        f"{wc_over} of {wc_tot} reads over 512 (index 1: {wc_rows.get(1, {}).get('over_512', '?')}); per-index n "
        f"reproduce: {'YES' if wc_n_ok else 'NO'}",
        f"{wc_loc}; {tr_loc}", "log-only", "N4(iv)", "the over-512 counts need the tokenizer")
    fig("steering boundary collapsed to 0 on 270 of 1,894 e2a generations (HANDOFF review card 9)",
        f"{n_gen} generated rounds reproduced (sum of n_rounds_generated); 270 not recomputed (needs the tokenizer)",
        f"{bc_loc}; {c9_loc}; quoted at the pin {c9_pin}", "log-only", "N4(iv)",
        "card 9 by the handoffs' numbering; the block's '(card 9)' on (iv) names the cached path, card 8 there")
    fig("choice reads unaffected by the generation path",
        "a code argument (the read takes text, never the generation cache); e2a's code is in the clone",
        f"clone jlens_qwen/e2a.py choice_read and generate_round_positional (context); rule-26 recheck {rr}",
        "log-only", "N4(iv)",
        f"the KL ledger ({len(full_ver)}/{len(full_all)} at 0.0, reproduced in (iii)) shows read determinism, not path independence")

    # ------------------------------------------------------------ card numbers
    # round 4, finding 3: each locator spans its quoted words (closing line as the end anchor)
    c8 = loc("RESULTS.md", '"Review card 8" lives ONLY in the untracked', 'methods disclosure (0.10 number owed)"*')
    c10 = loc("RESULTS.md", '"card 10" occurs only in the proposal; the cards on record stop',
              "at 8, card 11 is the content-class disclosure")
    blk54 = loc(BLOCK, "the 311/360 and cached-generation disclosures (review cards 9 and 10)")
    blk59 = loc(BLOCK, "(iii) 311 vs 360: reproduce")
    blk60 = loc(BLOCK, "(iv) Cached-generation disclosure (card 9)")
    c_all = (loc(H13, "Cards 1–8 as in the 09-04 handoff. New: **9**", "numbers (S1 k = 1 in the log; T-step 0.10 = 23/24).",
                 working_tree=True) if H13 in HAND else "HANDOFF-2026-09-13-design.md: absent")
    NOTES.append(f"Review-card numbering. The block names each card's subject itself ({blk54}; (iii) at "
                 f":{blk59.split(':')[-1]}, 311 vs 360 = 'card 10'; (iv) at :{blk60.split(':')[-1]}, 'Cached-generation "
                 f"disclosure (card 9)'), and (iii) and (iv) answer those subjects as the block states them; "
                 f"FIGURE-REVIEW-2026-10-06.md is not needed for that. The design handoffs on this machine (untracked, "
                 f"read only) number the cards differently: {c8_h04} calls e2a/e2b's cached generation 'review-round "
                 f"card 8' (also {c8}: '(8) the cached-generation / T-step methods disclosure'); {c_all} keeps 'Cards "
                 f"1–8 as in the 09-04 handoff' and adds 9 = the 512-token boundary collapse (note above), 10 = 360 rows "
                 f"vs 311 distinct (the block's (iii) subject; see (iii) for its 'verify_every = 4' wording) and 11 = the "
                 f"content-class screen. A committed raw quotes card 9 at the pin ({c9_pin}), and PROPOSAL-k maps "
                 f"'Review card 10' to e2a's every-fourth verification ({pk10}). Under the handoffs' numbering the "
                 f"block's '(card 9)' on (iv) names card 8's subject: a wrong referent (block :3), not a STOP. Both "
                 f"subjects are answered: (iv) covers the cached path as the block words it, and its README paragraph "
                 f"now carries card 9's boundary collapse as one log-only clause. ({c10} reads '\"card 10\" occurs "
                 f"only in the proposal; the cards on record stop at 8'; cards 9 and 10 are defined in the untracked "
                 f"09-13 handoff.)")
    NOTES.append("Rule-27 status of the producing code: the e2a session runner, choice read, analyzer and gate scripts (g1, "
                 "g2, g2 spot-check) quoted here live in the gitignored clone (jlens-qwen36/), not in the record. The "
                 "tracked ports (scripts/e2a_recount.py, "
                 "valence_core/readout.py, valence_core/session_e2a.py) reproduce the analysis and scaffolding; a reader of "
                 "the tag sees only those.")
    NOTES.append("The full-run raw results/raw/2026-08-09_e2a_full.txt prints both 'round generation path (g1r, mechanical): "
                 f"cached' (operative, :{','.join(map(str, cl))}) and a stale 'uncached path (g1)' banner "
                 f"(:{','.join(map(str, st))}); the record names the stale "
                 f"string cosmetic ({loc('archive/RESULTS-cycles3-4.md', '- Cosmetic on record: the session banner still prints the stale', 'cached-path line; fix queued for the next licensed launch.')}). A reader of the raw alone could misread it.")

    # ------------------------------------------------------------- summaries
    o("## Figures (as the block writes them)")
    o()
    o("| figure | value printed | source | status | note |")
    o("|---|---|---|---|---|")
    for f_ in FIGS:
        o(f"| {cell(f_['figure'])} | {cell(f_['reproduced'])} | {cell(f_['source'])} | {f_['status']} | {cell(f_['note'])} |")
    o()
    o("## STOPs")
    o()
    disc_i = [f_ for f_ in FIGS if f_["status"] == "discrepant" and f_["named_in"] == "N4(i)"]
    on_fail = loc(BLOCK, "*Output:* `results/raw/<stamp>_note-N4-e2a.md`.", "any (i) discrepancy is a STOP on the e2a bullet.")
    wrong_ref = loc(BLOCK, "where a referent below is wrong, Code names the right one in the raw and proceeds")
    if STOPS:
        for s_ in STOPS:
            o(f"- {s_['subitem']}: {s_['discrepancy']} ({s_.get('suspected_cause', '')})")
    else:
        nf_i = [f_ for f_ in FIGS if f_["status"] == "not found" and f_["named_in"] == "N4(i)"]
        expl = {"every arm integer": ("the design seat's arithmetic (its second half is refuted; the record's figures "
                                      f"it tests all reproduce; referent note {note_no(NOTE_INTEG)})"),
                "F1 link-5 y-axis": "a figure label that the block itself says the post version relabels (block :57)",
                "the interval's method": (f"the design seat's method attribution (Wilson on {rec['reward']['k']}/"
                                          f"{rec['reward']['n']} gives {iv2(wi)}; the record names no method, referent "
                                          f"note {note_no(NOTE_INTERVAL)}; the interval itself reproduces under "
                                          f"{iv_by if iv_by else 'neither Clopper-Pearson nor Wald'}, its own "
                                          f"reproduced row)")}
        def why(f_):
            return next((v for k_, v in expl.items() if f_["figure"].startswith(k_)), "SEE ROW")
        o(f"- None under the block's on-fail rule ({on_fail}: 'any (i) discrepancy is a STOP on the e2a bullet'). "
          f"The (i) figures table has {len(disc_i)} 'discrepant' row(s), and none is a record figure: "
          + "; ".join(f"\"{f_['figure']}\" -- {why(f_)}" for f_ in disc_i)
          + f". Under block :3 ({wrong_ref}) and the PI's routing, a wrong design-seat claim or referent is "
            f"a note in the raw, not an (i) discrepancy. The {len(nf_i)} 'not found' (i) row(s) are the block's "
            f"quotations of preprint sentences, absent from every preprint copy on this machine (v1.1 and RESEARCH-NOTE "
            f"v0.2 absent): "
          + "; ".join(f"\"{f_['figure']}\"" for f_ in nf_i)
          + "; a quotation that cannot be located is not a discrepancy, and the figure or identity each carries "
            "has its own reproduced or computed-new row. No reproduction needed a change to any analyzer.")
    o()
    st_i = collections.Counter(f_["status"] for f_ in FIGS if f_["named_in"] == "N4(i)")
    st_ref = collections.Counter(f_["status"] for f_ in FIGS if f_["named_in"] == "N4 referents")
    wi_status = next(f_["status"] for f_ in FIGS if f_["figure"].startswith("the interval's method"))
    # the (i) tally before round 4 split the method claim off the interval row (pass-2 row 3 quotes it)
    st_i_pre4 = collections.Counter(f_["status"] for f_ in FIGS if f_["named_in"] == "N4(i)"
                                    and not f_["figure"].startswith("the interval's method"))
    o(f"- **N4 pass condition** ({on_fail.split('@')[0]}@{PIN}:62, '(i) reproduces; (ii)–(iv) delivered'): (i) "
      f"reproduces: **{'MET' if not STOPS else 'NOT MET'}** -- every record figure in (i) reproduces from committed "
      f"artifacts (the (i) rows: {dict(st_i)}; the verdicts-entry row is a locator, {dict(st_ref)}); the "
      f"[.44, .64] interval reproduces at 2 dp under Clopper-Pearson ({iv2(cp_)}) and Wald ({iv2(wd)}) (status "
      f"reproduced), not under the design seat's Wilson ({iv2(wi)}; that method claim is its own "
      f"'{wi_status}' row, a note), and the record names no method. (ii)–(iv) delivered: "
      f"**MET** ((ii) the MDE under the registered test and under both readings of the envelope; (iii) {len(cnt)} "
      f"reproduced with its one-sentence gloss; (iv) the cell list, the operational meaning, the README paragraph and "
      f"the scope sentence, with the choice-read claim carried as a code argument, log-only).")
    o()
    o("## Referent notes (a wrong referent is a note, not a STOP)")
    o()
    for i, n_ in enumerate(NOTES, 1):
        o(f"{i}. {n_}")
    o()
    PI.extend([
        f"Which interval method the note names for ≈[.44, .64] (the record states none; Clopper-Pearson gives "
        f"{iv2(cp_)}, Wald {iv2(wd)}, Wilson {iv2(wi)}).",
        f"Whether the note carries {len(cnt)} (ledger distinct keys, incl. {len(s3only) + len(s2only)} smoke keys) or "
        f"{len(full_ver)} of {len(full_all):,} (the run's own every-fourth verifications) beside 'one in every four'.",
        f"Whether the disclosure names f1's cached vanilla generation (outside the preprint's stated scope{sc262}).",
        f"The g3′ amendment's basis clause ({cfb}: 'the g1 fallback locked all generation to the uncached positional "
        f"path') and its counterfactual ({cf}) after the cached unlock: design seat/PI to say whether either needs a line "
        f"in Appendix D.",
        f"Which reading of conjunct (1) the note's MDE sentence uses: the registered text (signed; E1 δ* "
        f"{envres['E1 n=101 signed']['delta_star']:+.3f} at n = 101) or the analyzer's |·| (E1 δ* "
        f"{envres['E1 n=101 |·|']['delta_star']:+.3f}); conditional on the realized envelope both give "
        f"{envres['E2 n=101']['delta_star']:+.3f}.",
        f"Review-card numbering (referent notes on cards 9 and 10): the block cites '(card 9)' for the cached-generation "
        f"disclosure, which the design handoffs number card 8, while their card 9 is e2a's boundary collapse on 270 of "
        f"{n_gen} generations. The README draft now carries card 9 as one log-only clause; design seat/PI to confirm "
        f"the clause and the card numbers the note cites.",
    ])
    o("## Items for the PI")
    o()
    for i, n_ in enumerate(PI, 1):
        o(f"{i}. {n_}")
    o()
    # ---------------------------------------------------------- values-check
    sg = {k: envres[k]["delta_star"] for k in ("E1 n=101 signed", "E1 n=102 signed", f"E1 floors n={FL_R} signed")}
    sj = {k: jres[k]["delta_star"] for k in ("101 signed", "102 signed")}
    ab = {k: envres[k]["delta_star"] for k in ("E1 n=101 |·|", "E1 n=102 |·|", f"E1 floors n={FL_R} |·|",
                                               "E2 n=101", "E2 n=102")}
    abj = {k: jres[k]["delta_star"] for k in ("102 |·|", "101 |·|")}
    chk_signed = {"E1 n=101 signed": 0.1558, "E1 n=102 signed": 0.1556, f"E1 floors n={FL_R} signed": 0.1827,
                  "101 signed": 0.1645, "102 signed": 0.1631}
    chk_abs = {"E1 n=101 |·|": 0.1911, "E1 n=102 |·|": 0.1909, f"E1 floors n={FL_R} |·|": 0.2243,
               "E2 n=101": 0.1872, "E2 n=102": 0.1903, "102 |·|": 0.1916, "101 |·|": 0.1919}
    mine = {**sg, **sj, **ab, **abj}
    sig_cmp = "; ".join(f"{k}: checker +{v:.4f}, this run {mine[k]:+.4f} ({'match' if r4(mine[k]) == v else 'DIFFER'})"
                        for k, v in chk_signed.items())
    abs_cmp = all(r4(mine[k]) == v for k, v in chk_abs.items())
    full_cl = ",".join(map(str, cl))
    VC = [
        ("1 (substantive) (iv) cached-cell list omits e2a's g2r and g2r2", "fixed",
         f"Added as reproduced from `use_cached` ({G2['g2r']['path']} and {G2['g2r2']['path']}, both True at frac 0.1), "
         f"with their raws; the first g2 ladder added as uncached (log-only); the g2 spot-check added (path not in the "
         f"record; clone code cached). README paragraph and scope sentence extended."),
        ("2 (substantive) figures row 'cells generated on the cached path' marked reproduced", "fixed",
         "Split into seven rows: e2a full run + smokes (log-only), e2a g2r/g2r2 (reproduced), first g2 ladder (log-only), "
         "spot-check (not found), e2b arc (reproduced), not-cached cells (reproduced; D1 log-only), f1 (log-only)."),
        ("3 (substantive) 'choice reads unaffected' marked reproduced", "fixed",
         f"Now log-only: a code argument whose e2a code is in the clone, with the rule-26 recheck at {rr}. The (iii) and "
         f"(iv) prose and the README now say the KL ledger shows read determinism on identical token ids, not path "
         f"independence; the {len(full_ver)}/{len(full_all)} re-forwards stay a separate reproduced row."),
        ("4 (substantive) STOPs 'None' beside a 'discrepant' (i) row, no pass line", "fixed",
         "Kept the row 'discrepant' (the design seat's claim does disagree with the record) and added to STOPs why it "
         "and the F1-label row are notes under block :3, not (i) discrepancies under :62, plus an explicit pass-condition "
         "line."),
        ("5 (substantive) envelope MDE computed only under the |·| reading", "fixed",
         f"Added the signed (registered-text) reading for E1 and the joint power; E2 is the same under both (asserted). "
         f"Checker's signed values against this run: {sig_cmp}. The |·| values match the checker's reproduction at 4 dp: "
         f"{'YES' if abs_cmp else 'NO'}. Reading paragraph restated; the choice of reading is a PI item."),
        ("6 (minor) e2a full-raw locators 2,27,54,205", "fixed",
         f"Cause confirmed: str.splitlines() also breaks on the tqdm '\\r' characters. lines_with, quote_lines and "
         f"pinned_jsonl now split on '\\n' only; the locators are now :{full_cl}."),
        ("7 (minor) rule-26 locator :23-26", "fixed", f"Same cause; now {rr}. The four values are parsed from those lines."),
        ("8 (minor) habit.py :31 and PROPOSAL-j :429-430 unquoted; 'post-hoc algebra' wording", "fixed",
         f"Both quoted ({hab31}; {pj}); noted that :31's 'either way' holds only under balance; reworded to "
         f"'algebra, not a finding ... the motivating e2a rates post-hoc' ({hab37})."),
        ("9 (minor) 'not in the preprint' unscoped; Appendices C/D absent", "fixed",
         f"Scoped to {PREPRINT}; PREPRINT-v1_1-draft.md (the block's project copy, {v11_loc}) is named as absent and "
         f"as a candidate source; the planned-appendices line :{app_planned[0] if app_planned else '?'} is cited."),
        ("10 (minor) README wording: T-step corpus, 'agree in distribution', 512-token window, the 281/1115 clause", "fixed",
         "All four applied: e2d-format rounds through the ported adapter; first-token distributions agree; e2a reads see "
         "the last 512 tokens and every DV read fit (log-only counts, with the per-index n reproduced); the re-forward "
         "clause now attaches to e2a alone."),
        ("11 (minor) g1 'first response position' unsourced; 1e-6 bar cited at readout.py:57-61", "fixed",
         f"Position now cited to {pos_loc}, the T-step JSON's g1_gate.why, the pre-registration ({pre_g1}) and the "
         f"clone gate script as context; the bar to {bar_loc} and the g3′ clause-1 text {c1_loc}; :57-61 kept for "
         f"the KL form."),
        ("12 (minor) note 7 / PI item 4 omit the g3′ basis clause", "fixed",
         f"Basis quoted ({cfb}) in the (iv) note, the referent note (the finding's note 7, now note "
         f"{note_no(NOTE_G3)}) and PI item 4; still reported, not adjudicated."),
        ("13 (minor) no figures row for F1's link-5 y-axis label", "fixed",
         "Row added, status discrepant (label), with the relabel."),
        ("14 (minor) prose values hard-coded rather than computed (relayed finding truncated after its location list "
         "'562, 660-665, 701-708, 1010, 1029-1030, 1041-')", "fixed",
         "Every numeral at the listed locations is now printed from computed variables (the 2·53 example, the measured "
         "Δ, the interval values, the 36 smoke2 overlaps, the 49/38/311 sentence, the 30 smoke keys). The rest of the "
         "script was swept (an AST scan of every string literal for numerals) and fixed likewise: launched counts in "
         "(i-c), the 0.24422 check, the preprint footnote values (now parsed and compared), g1 prefix count, KLs and bar, "
         "g1r's pass and the first smoke's dose, T-step counts and STOP_CAP, control-arm sizes and floors in (ii), sham "
         "map figures, PI items, notes. Literal numbers that remain are the block's claims being tested, quotations of "
         "the record beside their locators, anchors, assertion targets checked against the record's text, or labels "
         "naming the n or dose a computation is for."),
    ]
    o("## Values-check (pass 1, adversarial checker; dispositions by the fixer)")
    o()
    o("The checker re-ran the builder's script (sha256 6329916c...ab22f) into scratch, reported the JSON byte-identical "
      "and the md identical apart from the stamp and command lines, checked 104 claims, and returned the findings "
      "below. Each is listed with its disposition; none was rejected.")
    o()
    o("| # | finding | disposition | detail |")
    o("|---|---|---|---|")
    for a_, b_, c_ in VC:
        o(f"| {cell(a_.split(' ', 1)[0])} | {cell(a_.split(' ', 1)[1])} | {b_} | {cell(c_)} |")
    o()
    t10_div = t10["divergent"][0] if t10["divergent"] else None
    VC2 = [
        ("1 (substantive) note 10: cards 9 and 10 'cannot be checked here'; note 9 'beyond the block's ask'", "fixed",
         f"The block names each card's subject itself ({blk54}; :{blk59.split(':')[-1]}; :{blk60.split(':')[-1]}), and "
         f"the design handoffs on this machine number them: {c_all} (card 9 = the 270/{n_gen} boundary collapse, 10 = "
         f"360 vs 311) and {c8_h04} (card 8 = the cached-generation disclosure). The finding's note 10 (the "
         f"post-pass-1 numbering; now note {note_no(NOTE_CARDS)}) is rewritten: the block's "
         f"'(card 9)' on (iv) names card 8's subject under the handoffs' numbering, a wrong referent (block :3), and "
         f"both subjects are answered. The finding's note 9 (now note {note_no(NOTE_CARD9)}) now calls the boundary "
         f"collapse the handoffs' card 9; the README "
         f"paragraph carries it as one log-only clause; a figures row is added (log-only); PI item 6 is restated. "
         f"(iii) now says card 10's 'at verify_every = 4' holds for the run's {len(full_ver)} only, the "
         f"{len(s3only) + len(s2only)} smoke keys having been verified at every choice."),
        ("2 (substantive) 'the one divergence at the first token' / 'at position 1'", "fixed",
         f"Confirmed: `first_divergent_position` is a 0-based index ({fd_loc}) into every sampled token ({gen_loc}); "
         f"at {t10['frac']} it is {t10_div[2] if t10_div else '-'}, the stored stripped texts share no first character, "
         f"and the artifact stores no token ids. The (iv) parenthetical, the README ('beginning at the second sampled "
         f"token ... after a whitespace token both paths shared') and the figures row are reworded; the T-step tuple is "
         f"labelled 0-based and 'positions 1..N' is labelled a 1-based count. A referent note records that the record's "
         f"'POSITION 1' / 'FIRST token' ({pos1_loc}; {first_loc}) holds only as 'first content token'. (Round 4, "
         f"row 2, rewords the README clause and that note; see there.)"),
        ("3 (substantive) interval ≈ [.44, .64] marked computed-new", "fixed",
         f"Status now reproduced (at 2 dp: Clopper-Pearson {iv2(cp_)}, Wald {iv2(wd)}; Wilson {iv2(wi)}); the record "
         f"figure is {f3}; the method attribution stays a note and PI item 1. (i) tally then {dict(st_i_pre4)} "
         f"(round 4, row 4, splits the method claim into its own row; see there)."),
        ("4 (minor) g2 AUCs lack probe/layer/contrast/scheme; judge 14/32 has no unit", "fixed",
         f"Every g2 AUC in (iv), the README draft and the figures row now names the probe, layer, contrast and scheme "
         f"from {probe_loc}, {pole_loc} and {kcat_loc} (clone {g2_hdr_rng} as context); a single declared split, no "
         f"cross-validation. The judge figure is written as {g2r2['judge_plus']} of {g2r2['judge_total']} AB trials "
         f"judging the +α response better, from the raws' 'judge AB (descriptive): ... picked +pole' lines."),
        ("5 (minor) H2 smoke cited at RESULTS.md:10410 only", "fixed",
         f"Now {loc('RESULTS.md', 'The two kernel paths produced BIT-IDENTICAL transcripts', 'of record — 2 sessions, smoke only.')}."),
        ("6 (minor) control-arm sizes cited at archive :666", "fixed",
         f"Now random1 at {loc('archive/RESULTS-cycles3-4.md', '0.152 (random1, n=23; sham +0.014, random2 +0.045)')} and "
         f"sham/random pooled at {loc('archive/RESULTS-cycles3-4.md', 'Valid n: reward 102 / sham 37', '/ random 45 — all floors met.')}; "
         f"the entry pools random1 + random2 as 45 (asserted)."),
        ("7 (minor) ±α at L48 cited at archive :1246 only", "fixed", f"Now {l48} and, for sham, {sham_unst}."),
        ("8 (minor) preflight :20 cited for RESEARCH-NOTE; pre-patch copies not searched", "fixed",
         f"Cited as {pf_both}. The {len(pp_hits)} untracked pre-patch copies are now grepped by the script; "
         f"none carries '54 of 101 valid sessions' or 'half the difference': {pp_none}."),
        ("9 (minor) '54 of 101 valid sessions' row mixes statuses", "fixed",
         "Split: the quotation (not found) and footnote 1's 54/101, Δ, p (reproduced, audit v2). The 'half the "
         "difference' row is split the same way for consistency (quotation not found; identity computed-new)."),
        ("10 (minor) format_recon_timing.json missing from the uncached list", "fixed",
         f"The list is now computed by a read-only git grep at the pin over every data/*.json(l) for "
         f"{'/'.join(PATH_KEYS)}: {len(path_vals)} files, the {len(cached_set)} true ones exactly the g2r/g2r2 and e2b "
         f"files (asserted); the false ones now include format_recon_timing.json {unc.get('data/format/format_recon_timing.json')} "
         f"and d2_analysis.json {unc.get('data/e2d/d2_analysis.json')}; no data/olmo file carries either key (asserted)."),
        ("p1 (pass-1 remark, rule 4) the integrality table's p column header names no test", "fixed",
         "The column header now reads 'one-sided exact binomial P(X ≥ k; n, ½) for the (2k−n)/n k vs stored p'."),
    ]
    o("## Values-check (pass 2, adversarial checker; dispositions by the fixer)")
    o()
    o("The pass-2 checker re-ran the post-pass-1 script (sha256 123eb158...cbb33e) into scratch, reported the JSON "
      "byte-identical and the md identical apart from the stamp and command lines, checked 131 claims with 25 "
      "independent recomputations (all agreeing), confirmed no STOP and the pass outcome, and returned the ten "
      "findings below; the last row closes the one pass-1 remark the pass-1 table did not carry. Each finding was "
      "re-verified with a tool run before it was applied; none was rejected.")
    o()
    o("| # | finding | disposition | detail |")
    o("|---|---|---|---|")
    for a_, b_, c_ in VC2:
        o(f"| {cell(a_.split(' ', 1)[0])} | {cell(a_.split(' ', 1)[1])} | {b_} | {cell(c_)} |")
    o()
    n_ts, n_c9, n_cd, n_g3 = (note_no(NOTE_TSTEP), note_no(NOTE_CARD9), note_no(NOTE_CARDS), note_no(NOTE_G3))
    VC4 = [
        ("1 (minor) pass-2 row 1 points to notes 10 and 9 by a numbering the T-step note had already shifted",
         "fixed",
         f"Confirmed: pass 2 added the T-step note (now note {n_ts}) ahead of them, so every later note moved down by "
         f"one; the pass-2 checker's re-run of the post-pass-1 raw had the boundary collapse at note 9 ('Beyond the "
         f"block's ask ...') and the card numbering at note 10. Note numbers in the dispositions and the STOPs "
         f"paragraph are now computed from the printed list (`note_no`), never written by hand: pass-2 row 1 now "
         f"reads 'the finding's note 10 (the post-pass-1 numbering; now note {n_cd})' and 'the finding's note 9 (now "
         f"note {n_c9})'; pass-1 row 12's 'note 7' (the g3′ note in the builder's raw) is given as now note {n_g3} "
         f"in its detail, the same defect; referent notes {note_no(NOTE_INTEG)} and {note_no(NOTE_INTERVAL)}, cited "
         f"in the STOPs paragraph and the figures rows, are computed likewise. Finding titles keep the numbering of "
         f"the raw each checker read. The JSON's values_check_pass2[0] carries the same text."),
        ("2 (minor) README and note 7 state 'the first content token' as fact; note 7 places the misleading wording "
         "on 'POSITION 1'", "fixed",
         f"Confirmed: index 0 was identical on both paths (first_divergent_position = {d0_idx}; {fd_loc}) and decoded "
         f"to no visible text (the texts are stripped, {strip_loc}, and share no first character), but the adapter "
         f"admits more than one leading whitespace token ({ws_loc}) and the artifact stores no token ids, so 'index "
         f"{d0_idx} is the first content token on both paths' is an inference. The README now reads 'beginning at the "
         f"second sampled token (0-based index {d0_idx}; the first sampled token was identical on both paths and "
         f"decoded to whitespace)', 'first content token' dropped. Note {n_ts} now says 'POSITION 1' ({pos1_loc}) is "
         f"right as the stored 0-based index and that the record's 1-based 'Positions 1..{T10_maxlen}' ({posn_loc}) "
         f"and 'FIRST token' ({first_loc}) invite the first-token reading; 'first content token' stays there only "
         f"with the inference label. The (iv) parenthetical, already labelled an inference, now names the "
         f"leading-whitespace rule. Pass-2 row 2 describes the pass-2 wording, superseded here. No number changes."),
        ("3 (minor) the card-8 and card-10 locators stop at the anchor line, not the quoted words", "fixed",
         f"Confirmed at the pin: the quoted '(8) the cached-generation / T-step methods disclosure' runs onto the "
         f"next two lines, and 'the cards on record stop at 8' onto the next one. Both now pass the closing line to "
         f"loc() as an end anchor: {c8}; {c10} (note {n_cd})."),
        ("4 (minor) the interval row mixes a reproduced record figure with a refuted method claim", "fixed",
         f"Split, as pass-2 finding 9 split its mixed row: 'approach-probability interval ≈ [.44, .64]' stays "
         f"{next(f_['status'] for f_ in FIGS if f_['figure'] == 'approach-probability interval ≈ [.44, .64]')} "
         f"(under {iv_by}, named in its value cell; the status column keeps the block's status vocabulary), and a "
         f"new row, 'the interval's method (block: 'Wilson on 55/102 gives it')' ({blk_wilson}), is {wi_status}: "
         f"Wilson 95% on {rec['reward']['k']}/{rec['reward']['n']} = [{wi[0]:.4f}, {wi[1]:.4f}] → {iv2(wi)} "
         f"(re-computed by this run; Clopper-Pearson [{cp_[0]:.4f}, {cp_[1]:.4f}], Wald [{wd[0]:.4f}, {wd[1]:.4f}]); "
         f"a design-seat claim and a note, not an (i) STOP, treated like the integrality row. (i) tally now "
         f"{dict(st_i)} (before: {dict(st_i_pre4)}); the STOPs paragraph names the new row and the pass line points "
         f"to it. The pass/STOP outcome is unchanged."),
        ("5 (minor) (iii) calls the 8 smoke3 sessions byte-identical, having compared transcripts only",
         "fixed (wording amended)",
         f"Confirmed for the point and applied with the proposed wording amended, because one part of it does not "
         f"hold on re-run: the rows do not differ only in verify_kl. Re-run here: transcripts equal "
         f"{sum(ident)}/{len(ident)}; every pick and p_a equal {sm_pick_pa}/{len(sm_pair)}; rows equal as JSON "
         f"{sm_row_json}/{len(sm_pair)} ({'; '.join(sm_nch_eq)}); verify_kl differs in {len(sm_vkl_diff)}; in "
         f"{len(sm_oop)} ({', '.join(sm_oop)}) the run's rows also carry an `oop_tag` key (values "
         f"{', '.join(sm_oop_vals)}) that smoke3's lack; with both keys set aside {sm_rest_eq}/{len(sm_pair)} are "
         f"equal. NaN or Infinity tokens in either file (a text scan of both pinned blobs): "
         f"{'PRESENT' if sm_nan else 'none'}, so the finding's 'the remaining round "
         f"inequalities are NaN fields' is not borne out: they are the oop_tag key. (iii) now says all of this; the "
         f"conclusion that the {len(s3only)} smoke3-only keys are identical-input verifications stands."),
    ]
    vc4_amended = [a_.split(" ", 1)[0] for a_, b_, c_ in VC4 if "amended" in b_]
    o("## Values-check (round 4, adversarial checker; dispositions by the fixer)")
    o()
    o("The round-4 checker read the outputs of the script whose hash the previous raw printed (sha256 "
      f"ade10a4c...fa6a) and returned the {len(VC4)} minor findings below, none substantive and none left open from earlier "
      "rounds. Each was re-verified with a tool run before it was applied; "
      f"{len(vc4_amended)} proposed wording(s) (row {', '.join(vc4_amended)}) amended where the re-run contradicted "
      "it; none was rejected.")
    o()
    o("| # | finding | disposition | detail |")
    o("|---|---|---|---|")
    for a_, b_, c_ in VC4:
        o(f"| {cell(a_.split(' ', 1)[0])} | {cell(a_.split(' ', 1)[1])} | {b_} | {cell(c_)} |")
    o()
    # round 9 (ruling 9): the failed preprint checks, for the design seat
    o("## Findings on the patch (the PI's ruling 9 of 2026-10-10, as corrected; for the design seat, not STOPs)")
    o()
    o(f"Each is a check of a preprint sentence that fails on the patched text (`{PREPRINT}`, sha256 {pre_sha[:8]}...). "
      f"The old line is the audited text ({PREPRINT_SHA_AUDITED[:8]}...) as the raw of record quotes it; the new line is "
      f"the patched file's. A check that holds is not listed.")
    o()
    if not PATCH:
        o("- None.")
    for pf_ in PATCH:
        o(f"- **{pf_['id']}** {pf_['result']}. Check: {pf_['check']}.")
        for x_ in pf_["old"]:
            o(f"  - old ({x_['locator']}): {x_['quote']}")
        for x_ in pf_["new"]:
            o(f"  - new ({x_['locator']}): \"{x_['quote']}\"")
        o(f"  - record values, this run: {pf_['record_values_this_run']}")
        if pf_["patched_figures_vs_this_run"]:
            o(f"  - {pf_['patched_figures_vs_this_run']}")
    o()
    o("## git status (non-audit, non-m changes)  [run metadata: reflects the working tree at run time]")
    o()
    st_ = git("status", "--porcelain").decode().splitlines()
    m_work = {"scripts/m_sessions.py", "valence_core/m/__init__.py", "valence_core/m/gcal.py"}
    gi = [l for l in git("diff", "-U0", "--", ".gitignore").decode().splitlines()
          if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    gi_m_only = bool(gi) and all(l[1:].lstrip().startswith("#") or "/data/m/" in l for l in gi)
    if gi_m_only:
        m_work.add(".gitignore")
    def is_m(path_: str) -> bool:
        return path_ in m_work or path_.startswith(("valence_core/m/", "data/m/"))
    other = [l for l in st_ if not is_m(l[3:]) and not l[3:].startswith("scripts/audit_note_")
             and not l[3:].startswith("results/raw/2026-10-08_note-") and l[:2] != "??"]
    o(f"- Working-tree changes from the concurrent PROPOSAL-m session (git status codes; not touched by this "
      f"audit): {sorted(l for l in st_ if is_m(l[3:]))}"
      f"{' (.gitignore: its diff adds only data/m allowlist lines and a comment)' if gi_m_only else ''}.")
    o(f"- Modified tracked files other than the m work and audit outputs: {other if other else 'none'} "
      f"(untracked files are not listed). This audit wrote only {DEF_OUT} and {DEF_JSON} (or the --out/--json-out "
      f"paths given) and its own script.")
    # HEAD may move during the audit (a concurrent session commits): report what moved against what this run read
    moved = [l for l in git("diff", "--name-only", PIN, "HEAD").decode().split("\n") if l]
    n_commits = len([l for l in git("log", "--format=%h", f"{PIN}..HEAD").decode().split("\n") if l])
    read_set = set(_CACHE) | set(imported) | set(IMPORTED_OK)
    touched = sorted(set(moved) & read_set)
    o(f"- Commits between the pin and HEAD at run time: {n_commits}; files they change: {len(moved)}; of those, "
      f"files this run read ({len(read_set)} repository paths: every pinned blob plus the imported modules): "
      f"{touched if touched else 'none'}. Every record read is at the pin regardless.")
    o()

    os.makedirs(os.path.dirname(out_md), exist_ok=True)
    with open(out_md, "w", encoding="utf-8") as f:
        f.write(o.buf.getvalue())
    J = {"item": "N4", "pin": PIN, "block_sha256": block_pin_sha, "script": me_rel,
         "script_sha256": sha256_file(me), "interpreter": sys.executable,
         "python": sys.version.split()[0],
         "recount": rec, "integrality": integ, "habit": hab, "literal_between_arm": lit,
         "intervals": ivs, "first_pick_habit": {"ge2": [c2, len(dom2)], "ge1": [c1, len(dom1)], "valid": [cv, len(domv)]},
         "record_analyzer": {"frozen": [kf, nf], "v2": [kv, nv], "v2_extra_sessions": extra},
         "mde_registered_test": mde, "mde_envelope": envres, "mde_joint": jres,
         "kl_ledger": {"rows": len(L), "distinct": len(cnt), "dup_rows": sum(v - 1 for v in dup.values()),
                       "dup_keys": len(dup), "all_zero": allzero, "smoke2_rows": n2,
                       "smoke3_rows": len(smoke_keys), "run_rows": len(full_ver),
                       "run_choice_forwards": len(full_all), "smoke3_only": len(s3only),
                       "smoke2_only": sorted(s2only), "record_inputs_verified": distinct_inputs_record,
                       "segments_asserted": [seg_smoke2, seg_smoke3, seg_full]},
         "rule26_recheck_log_only": r26,
         "tstep": tst, "e2a_g2_cached": G2, "e2a_g2_first_ladder_uncached_raw_lines": g2_unc,
         "e2b_cached": e2b, "uncached_cells": unc,
         "e2a_window_coverage_log_only": {"rows": wc_rows, "n_by_index_recount": n_by_idx,
                                          "n_by_index_match": wc_n_ok, "over_512": wc_over, "total": wc_tot,
                                          "locator": wc_loc},
         "readme_paragraph": readme, "scope_sentence": scope,
         "figures": FIGS, "stops": STOPS, "referent_notes": NOTES, "pi_items": PI,
         "values_check": [{"finding": a_, "disposition": b_, "detail": c_} for a_, b_, c_ in VC],
         "values_check_pass2": [{"finding": a_, "disposition": b_, "detail": c_} for a_, b_, c_ in VC2],
         "values_check_round4": [{"finding": a_, "disposition": b_, "detail": c_} for a_, b_, c_ in VC4],
         "smoke3_vs_run_rows": {"transcripts_equal": sum(ident), "pick_p_a_equal": sm_pick_pa,
                                "rows_json_equal": sm_row_json, "verify_kl_differs": sm_vkl_diff,
                                "oop_tag_in_run_only": sm_oop, "oop_tag_values": sm_oop_vals,
                                "equal_without_verify_kl_oop_tag": sm_rest_eq, "n": len(sm_pair),
                                "nan_or_inf_token_in_files": sm_nan},
         "interval_method_row_status": wi_status,
         "path_flag_scan": path_vals, "preprint_prepatch_grep": pp_hits,
         "tstep_index_semantics": {"first_divergent_position": "0-based token index", "locator": fd_loc,
                                   "f010_divergent_index": d0_idx, "f010_first_char_shared": d0_first_char_shared,
                                   "token_ids_stored": ids_stored},
         "review_cards": {"card9_handoff": c9_loc, "card9_text_found": c9_ok, "card10_handoff": c10_loc,
                          "card10_text_found": c10_ok, "card8_handoff": c8_h04, "block_lines": [blk54, blk59, blk60]},
         "preprint_of_record": {"path": PREPRINT, "sha256": pre_sha, "match": pre_sha == PREPRINT_SHA,
                                "ruling": "the PI's ruling 9 of 2026-10-10, as corrected",
                                "audited_superseded_sha256": PREPRINT_SHA_AUDITED,
                                "audited_archive": PREPRINT_AUDITED_ARCHIVE, "audited_archive_status": aud_st,
                                "raw_of_record": f"{RAW_REC[1]}@{RAW_REC[0]}"},
         "patch_findings": PATCH}
    with open(out_js, "w", encoding="utf-8") as f:
        json.dump(J, f, indent=1, ensure_ascii=False, default=list)
        f.write("\n")
    print(f"wrote {out_md}\nwrote {out_js}")


CLAUDE_E2A_SESS = f"{CLONE}/scripts/e2a_sessions.py"

if __name__ == "__main__":
    main()
