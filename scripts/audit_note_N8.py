#!/usr/bin/env python3
"""AUDIT-note-release v1.2, item N8 -- link 2 (Qwen hijack) via the regression suite.

READ-ONLY ON THE RECORD. What this script does, in order:

  1. Runs the model-free regression suite twice and captures what it prints:
     (a) from the repository root on the working tree -- the command the README
         gives, `python -m valence_core.regression.analysis`, with `-B` added so
         no __pycache__ is written into the repository; TMPDIR points at the
         audit's scratch directory (one suite check makes a temp checkpoint);
     (b) from a `git archive <pin>` extraction of valence_core/, scripts/ and
         data/ in the scratch directory, so the count is also stated AT THE PIN
         (the working tree carries a concurrent session's files). The
         extraction is deleted afterwards.
     The scratch directory is --scratch when given; otherwise a fresh
     directory made with tempfile.mkdtemp(prefix="audit_note_N8_") under
     tempfile.gettempdir() (portability fix, 2026-10-08: the default used to
     be the builder's session scratch, which exists on one machine only).
     Before anything is made, the untracked PREPRINT-v1_0-draft.md is looked
     for; if absent (a fresh clone, unless the PI commits it) the script
     prints '[not run: ... absent]' on stderr and exits 2, writing nothing.
     Since round 10 (below) its sha256 is then asserted in full against the
     preprint of record, also before anything is made: any other text prints
     '[refusing: ...]' on stderr and exits 3, writing nothing.
  2. Maps each link-2 figure of the block (N8, block lines 106-107) to the
     suite checks that hold it, by check name, or says that none does.
  3. Recomputes every link-2 figure it can from committed artifacts, read AT
     THE PIN with `git show <pin>:<path>` (npz loaded from the pinned bytes):
     e0 axis geometry (data/e0/e0_axes.npz + e0_axes.meta.json), the B1
     instrument and G (data/e0/e0_b1_markers.npz, the oracle's model-free
     instrument rebuild ported verbatim, and the oracle's own function called
     for comparison), the B2a/B2b/B2c-a arms (data/e0/e0_b2_*.json,
     e0_b2c_a.json), the S2 re-run of the same arms (data/e0/s2_neighbor_axes.json),
     and the e2d figures (data/e2d/*.json) under the definitions of
     valence_core/e2d/{marks,readability}.py and scripts/e2d_score.py.
     scripts/e2d_closure_verify3.py is read, not run.
  4. Reads the rule-26 oracle record's history (data/regression/oracle_rule26.json)
     with read-only git.
  5. Closes the md with a 'Portability fix and interim re-run' section and the
     JSON with a "portability" key: the work root used, what cleanup left in
     it, and a comparison of this run's outputs (that section and key left
     out) with the committed outputs at --compare-rev (default 09c3a8c),
     read with `git show`; each differing md line and JSON leaf is classed.

Round 9 (2026-10-10): the preprint of record is re-pointed at the patched text,
the PI's ruling 9 of 2026-10-10 as corrected: PREPRINT-v1_0-draft.md at sha256
0f4ba501...16c22 (patch v6 applied). The block's d6431e97...222b8 is recorded as
the audited, superseded text, archived untracked at
archive/PREPRINT-v1_0-draft.pre-patch-v6.md (out of the release, D4); that copy
is never opened or required. Every preprint sentence the script locates or
quotes is checked on the patched text in §0; a sentence not found there no
longer stops the run (loc() used to raise): it is recorded as a finding on the
patch for the design seat (ruling 9), with its line in the audited text and the
patched text's line of the same number. If the root preprint's sha256 was not the
preprint of record's, §0's sha line said STOP, the comparison classed the
preprint lines UNEXPECTED, and the script exited 3 after writing its outputs
(retired at round 10: such a text is refused before anything is made, exit 3,
nothing written).
Note 6's quote of preprint line 141 now runs through '0.30)' (it closed a
parenthesis the text does not close there). The closing comparison classes the
preprint-identity changes, the new §0 lines and note 6's quote. Nothing else
changed.

Round 10 (2026-10-12): the preprint of record is patch v7, the PI's routing of
2026-10-12 (the round-10 inputs): PREPRINT-v1_0-draft.md at sha256
d9635ca2...d1fe6, asserted in full before anything is made (absent: exit 2; a
different text: '[refusing: ...]' on stderr, exit 3; nothing is made or written
either way). Round 9 compared 0f4ba501...16c22 in full but, on a different text,
ran the audit and wrote its outputs before exiting 3 (a finding of round 10's
review: N8 was the one script of the six that did not refuse before writing); that
branch is retired: §0's STOP clause, the comparison's UNEXPECTED gate for
preprint rows (pre_gate) and the not-of-record branches of §0's round-9 lines
could no longer be reached and are removed, and the JSON key
integrity.preprint_of_record keeps its fields (its
not_found_on_a_text_not_of_record is always empty). The patch-v6 text
(0f4ba501...16c22, round 9's preprint of record) is archived untracked at
archive/PREPRINT-v1_0-draft.pre-patch-v7.md (out of the release): recorded, never
required, read only if present and its sha256 matches, to quote a v6 line beside
its v7 line. The audited text's handling (d6431e97...222b8,
archive/PREPRINT-v1_0-draft.pre-patch-v6.md, never opened) is round 9's,
unchanged. §0's round-9 sentence check runs on patch v7; §0's new round-10 lines
give each finding on the patch the raw committed at 84801cb recorded its
disposition on v7 (resolved / unchanged / changed, v6 and v7 quoted; a round-9
locator's line is a patch-v6 line, mapped to its patch-v7 line through the
v6-to-v7 line alignment, or taken at the same number when the patch-v6 copy is
not read) and every new finding v7 introduces (a sentence found on v6 and not on v7; a line this
script reads that v7 changed). The JSON's new key integrity.preprint_round10
carries the same; the closing comparison classes it and the round-10 lines as
new, and its preprint class names patch v7. Nothing else changed.

No model is loaded; no inference. Exact tests are stdlib (math.comb). numpy is
used for array geometry (npz) and is the record's own dependency. Outputs: the
two files named by --out and --json-out, nothing else in the repository.

Usage:
  jlens-qwen36/.venv/bin/python scripts/audit_note_N8.py \
      [--out results/raw/2026-10-08_note-N8-link2.md] \
      [--json-out results/raw/2026-10-08_note-N8-link2.json] \
      [--scratch <dir>]    (default: a fresh tempfile.mkdtemp directory)
      [--compare-rev 09c3a8c]
"""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True

import argparse
import atexit
import difflib
import hashlib
import io
import json
import math
import os
import re
import shlex
import shutil
import statistics
import subprocess
import tarfile
import tempfile

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)       # for the one blob-checked import (oracle.build_instruments)
PIN = "bbc9ffe"
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
PREPRINT = "PREPRINT-v1_0-draft.md"          # untracked; sha-pinned below
# Round 9 (2026-10-10): the preprint of record was the patched text (patch v6),
# the PI's ruling 9 of 2026-10-10 as corrected. The block's reference is the
# audited, superseded text, archived untracked (out of the release, D4); never
# opened or required here.
# Round 10 (2026-10-12): the preprint of record is patch v7, the PI's routing of
# 2026-10-12. The patch-v6 text, round 9's preprint of record, is archived
# untracked (out of the release): recorded, never required; read only if present
# and matching, to quote a v6 line beside its v7 line.
PREPRINT_SHA = "d9635ca24d32dcba193cd9aade273de2679c99c5c2218787b410e793a42d1fe6"
PREPRINT_SHA_V6 = "0f4ba501d60a94189e6dc83d28c41826debe50591b9af484fa08d05a41f16c22"
PREPRINT_V6_COPY = "archive/PREPRINT-v1_0-draft.pre-patch-v7.md"
PREPRINT_ROUTING_R10 = "the PI's routing of 2026-10-12"
R9_RAW_REV = "84801cb"      # the commit whose committed N8 JSON recorded round 9's findings
PREPRINT_SHA_AUDITED = "d6431e97d35e5914574ff9884c0e64463a7baf1cf9d279f27ed45a683a6222b8"
PREPRINT_AUDITED_COPY = "archive/PREPRINT-v1_0-draft.pre-patch-v6.md"
PREPRINT_RULING = "the PI's ruling 9 of 2026-10-10, as corrected"
# Every preprint sentence this script locates (loc(PREPRINT, ...)) or quotes, with
# the line it stood on in the audited text (d6431e97...222b8): for a locator, the
# line the committed raw at 02b6a61 printed; for a quote only, the line of the
# archived audited copy (sha-checked) read once when this list was made.
PREPRINT_SENTENCES = (
    ("define the evaluative direction", 101, "locator"),
    ("‖d‖/R ≈ 0.16 at every layer", 101, "locator"),
    ("up to 0.52", 101, "quoted"),
    ("on the remaining probes", 135, "locator"),
    ("9/12 and 10/12 on the remaining probes", 135, "quoted"),
    ("(G = 0.316) by roughly two-fold", 135, "locator"),
    ("exceeds the natural praise–criticism gap on that instrument (G = 0.316) by "
     "roughly two-fold", 135, "quoted"),
    ("a clean overdose regime at f = .40", 135, "locator"),
    ("a clean overdose regime at f = .40, where both poles read as post-criticism", 135,
     "quoted"),
    ("self-indexed 0.83–0.88", 137, "locator"),
    ("**Purity is not potency.**", 137, "locator"),
    ("coherence degrades monotonically", 141, "locator"),
    ("coherence degrades monotonically (audit-flagged rounds .000/.023/.047 across "
     "0.10/0.20/0.30)", 141, "quoted"),
    ("the marker imprint falls to about a quarter of its short-context value", 141, "quoted"),
)
DEF_OUT = "results/raw/2026-10-08_note-N8-link2.md"
DEF_JSON = "results/raw/2026-10-08_note-N8-link2.json"
# No fixed default scratch (portability fix, 2026-10-08): without --scratch,
# main() makes a fresh tempfile.mkdtemp(prefix=SCRATCH_PREFIX) directory
# under tempfile.gettempdir().
SCRATCH_PREFIX = "audit_note_N8_"
COMPARE_REV = "09c3a8c"     # the commit whose committed N8 raws a re-run is compared with
SUITE_SUMMARY = re.compile(r"^\s+(\d+)/(\d+) reproduced through valence_core\s*$")
SUITE_LINE = re.compile(
    r"^  \[(PASS|FAIL)\] (.+?) {3,}expected (.*?) got (.*?)   \((.*)\)$")

# ------------------------------------------------------------------ plumbing --


def git(*args: str) -> bytes:
    """Read-only git only. Never run inside the jlens-qwen36 clone."""
    assert args[0] in ("show", "rev-parse", "log", "ls-files", "diff",
                       "archive", "cat-file"), args
    return subprocess.run(["git", "--no-optional-locks", "-C", REPO, *args],
                          check=True, capture_output=True).stdout


def blob_sha1(b: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


_CACHE: dict[str, bytes] = {}


def pinned(path: str) -> bytes:
    if path not in _CACHE:
        _CACHE[path] = git("show", f"{PIN}:{path}")
    return _CACHE[path]


def pinned_text(path: str) -> str:
    return pinned(path).decode("utf-8")


def pinned_json(path: str):
    return json.loads(pinned_text(path))


def pinned_npz(path: str):
    return np.load(io.BytesIO(pinned(path)))


def blob_equal_to_pin(path: str) -> bool:
    with open(os.path.join(REPO, path), "rb") as f:
        wt = blob_sha1(f.read())
    return wt == git("rev-parse", f"{PIN}:{path}").decode().strip()


def lines_with(text: str, needle: str) -> list[int]:
    return [i for i, l in enumerate(text.split("\n"), start=1) if needle in l]


def loc(path: str, needle: str, working_tree: bool = False) -> str:
    """'path@<pin>:N' for the first line containing `needle` (must exist)."""
    if working_tree:
        with open(os.path.join(REPO, path), encoding="utf-8") as f:
            text = f.read()
        tag = f"{path}(working tree, untracked, sha256 {sha256_bytes(text.encode())[:8]}...)"
    else:
        text = pinned_text(path)
        tag = f"{path}@{PIN}"
    hits = lines_with(text, needle)
    if not hits and working_tree and path == PREPRINT:
        # round 9 (ruling 9): not a stop; §0's sentence check records the finding
        # (a finding on the patch only when the text read is the preprint of record)
        return (f"{tag}:NOT FOUND (" + ("finding on the patch" if sha256_bytes(text.encode())
                                         == PREPRINT_SHA else "not the preprint of record")
                + ", §0)")
    if not hits:
        raise SystemExit(f"anchor not found in {tag}: {needle!r}")
    s = f"{tag}:{hits[0]}"
    if len(hits) > 1:
        s += f" (also :{','.join(map(str, hits[1:4]))})"
    return s


def loc_range(path: str, start_needle: str, end_needle: str) -> str:
    """'path@<pin>:a-b': first line containing start_needle, through the first
    line at or after it containing end_needle (both must exist)."""
    text = pinned_text(path)
    a = lines_with(text, start_needle)
    if not a:
        raise SystemExit(f"anchor not found in {path}@{PIN}: {start_needle!r}")
    b = [i for i in lines_with(text, end_needle) if i >= a[0]]
    if not b:
        raise SystemExit(f"end anchor not found in {path}@{PIN}: {end_needle!r}")
    return f"{path}@{PIN}:{a[0]}" + (f"-{b[0]}" if b[0] != a[0] else "")


def cell(s) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


def f4(x: float) -> str:
    return f"{x:+.4f}"


# ------------------------------------------------------------ exact stats --

def hyper_pmf(i: int, row1: int, n: int, col1: int) -> float:
    return math.comb(row1, i) * math.comb(n - row1, col1 - i) / math.comb(n, col1)


def fisher(a: int, b: int, c: int, d: int) -> dict:
    """Fisher exact on [[a, b], [c, d]]: one-sided (excess in a) and
    two-sided (sum of tables no more probable than the observed one)."""
    n, row1, col1 = a + b + c + d, a + b, a + c
    lo, hi = max(0, col1 - (n - row1)), min(row1, col1)
    probs = {i: hyper_pmf(i, row1, n, col1) for i in range(lo, hi + 1)}
    obs = probs[a]
    return {"one_sided_greater": sum(p for i, p in probs.items() if i >= a),
            "two_sided": min(1.0, sum(p for p in probs.values()
                                      if p <= obs * (1 + 1e-9)))}


def pct_linear(xs: list[float], q: float) -> float:
    """numpy's default ('linear') percentile, in the stdlib."""
    s = sorted(xs)
    pos = (len(s) - 1) * q / 100.0
    lo = math.floor(pos)
    hi = min(lo + 1, len(s) - 1)
    return s[lo] + (pos - lo) * (s[hi] - s[lo])


# ----------------------------------------------------------- suite runs --

def run_suite(cwd: str, tmpdir: str) -> dict:
    os.makedirs(tmpdir, exist_ok=True)
    env = dict(os.environ)
    env["TMPDIR"] = tmpdir
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    cmd = [sys.executable, "-B", "-m", "valence_core.regression.analysis"]
    p = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
    lines = p.stdout.split("\n")
    checks, summary = [], None
    for l in lines:
        m = SUITE_LINE.match(l)
        if m:
            checks.append({"status": m.group(1), "name": m.group(2).strip(),
                           "expected": m.group(3).strip(),
                           "got": m.group(4).strip(), "source": m.group(5)})
        m2 = SUITE_SUMMARY.match(l)
        if m2:
            summary = (int(m2.group(1)), int(m2.group(2)))
    n_status_lines = sum(1 for l in lines if l.startswith("  [PASS]")
                         or l.startswith("  [FAIL]"))
    return {"cmd": " ".join(shlex.quote(c) for c in cmd), "exit": p.returncode,
            "stdout": p.stdout, "stderr": p.stderr, "checks": checks,
            "n_status_lines": n_status_lines, "summary": summary,
            "stdout_sha256": sha256_bytes(p.stdout.encode())}


def untracked_ignored(paths=("valence_core", "scripts", "data")) -> list[str]:
    out = git("ls-files", "--others", "--ignored", "--exclude-standard",
              "--", *paths).decode().split("\n")
    return sorted(x for x in out if x)


def untracked_plain(paths=("valence_core", "scripts", "data")) -> list[str]:
    out = git("ls-files", "--others", "--exclude-standard", "--", *paths
              ).decode().split("\n")
    return sorted(x for x in out if x)


# ----------------------------------------------- the instrument (ported) --

def instruments_port(Z) -> tuple[list[dict], list[float], float]:
    """Verbatim logic of valence_core/regression/oracle.py build_instruments
    (lines 179-227 at the pin), returning the per-probe natural gaps g_q too.
    g_q = (mean_pos - mean_neg) / pooled sd of the instrument score over the
    VAL-half natural contexts (tasks e25-e48) of probe q; G = mean_q g_q."""
    top_ids, top_vals = Z["top_ids"], Z["top_vals"]
    tid, cond, qidx = Z["task_id"], Z["cond"], Z["probe"]
    fit_ids = sorted({f"e{i:02d}" for i in range(1, 25)})
    in_fit = np.isin(tid, fit_ids)
    is_pos = cond == "self_pos"
    floor = top_vals.min(axis=1) - 2.0
    SEL = 256
    instruments, g_list = [], []
    for qi in range(int(qidx.max()) + 1):
        qm = qidx == qi
        halves = {}
        for label, mask in (("p", qm & in_fit & is_pos),
                            ("n", qm & in_fit & ~is_pos)):
            rows = np.where(mask)[0]
            a = {}
            for i in rows:
                for j, v in zip(top_ids[i], top_vals[i]):
                    a[j] = a.get(j, 0.0) + v
            halves[label] = (a, len(rows), float(floor[mask].mean()))
        (ap, n_p, flp), (an, n_n, fln) = halves["p"], halves["n"]
        keys = set(ap) | set(an)
        diffs = {k: ap.get(k, flp * n_p) / n_p - an.get(k, fln * n_n) / n_n
                 for k in keys}
        sel = sorted(diffs, key=lambda k: -abs(diffs[k]))[:SEL]
        w = np.array([diffs[k] for k in sel], dtype=np.float64)
        w /= np.linalg.norm(w) + 1e-12

        def scores_for(mask, sel=sel, w=w):
            pos_of = {k: t for t, k in enumerate(sel)}
            out = []
            for i in np.where(mask)[0]:
                x = np.full(len(sel), floor[i])
                for j, v in zip(top_ids[i], top_vals[i]):
                    if j in pos_of:
                        x[pos_of[j]] = v
                out.append(float(w @ x))
            return np.array(out)

        sp = scores_for(qm & ~in_fit & is_pos)
        sn = scores_for(qm & ~in_fit & ~is_pos)
        sd = float(np.sqrt((sp.var(ddof=1) + sn.var(ddof=1)) / 2))
        g_list.append(float((sp.mean() - sn.mean()) / (sd + 1e-12)))
        instruments.append({"sigma": sd, "n_val_pos": int(len(sp)),
                            "n_val_neg": int(len(sn))})
    return instruments, g_list, float(np.mean(g_list))


# -------------------------------------------------------------- geometry --

EPS = 1e-12      # valence_core/extract.py EPS at the pin
CNP = "computed-new (post-hoc, descriptive)"   # status label for sub-figures not in the record


def cosine(a, b) -> float:
    """valence_core/extract.py cosine, ported."""
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + EPS))


def residual_fraction(axis, guard) -> float:
    """valence_core/extract.py residual_fraction, ported."""
    g = guard / (np.linalg.norm(guard) + EPS)
    res = axis - np.dot(axis, g) * g
    return float(np.linalg.norm(res) / (np.linalg.norm(axis) + EPS))


# --------------------- attribution of the tracked-differing list (round 3) --

QWEN_SCAN_SKIP = (".git", "__pycache__", "jlens-qwen36", "archive")


def _subject_head(subj: str, n: int = 60) -> str:
    if len(subj) <= n:
        return subj
    cut = subj[:n].rsplit(" ", 1)[0]
    return cut + " ..."


def attribute_changed(changed: list[str], head: str) -> dict:
    """Which commits after the pin touch each file of `changed`; which carry
    uncommitted changes; which the suite's two structural source scans read.
    The scan predicates mirror valence_core/regression/analysis.py at the pin
    (the quarantine offender scan, :809-822; the qwen-helper definition scan,
    :1192-1205)."""
    raw = git("log", "--no-renames", "--name-only", "--date=short",
              "--format=%x00%h%x09%ad%x09%s", f"{PIN}..{head}").decode()
    commits = []
    for chunk in raw.split("\0")[1:]:
        first, _, rest = chunk.partition("\n")
        h_, d_, subj = first.split("\t", 2)
        commits.append((h_, d_, subj, {x for x in rest.split("\n") if x}))
    ch = set(changed)
    by_commit = [{"commit": h_, "date": d_, "subject_head": _subject_head(subj),
                  "files": len(ch & fs)} for h_, d_, subj, fs in commits]
    touched = set().union(*(fs for *_, fs in commits)) if commits else set()
    no_commit = sorted(x for x in changed if x not in touched)
    uncommitted = sorted(x for x in git("diff", "--name-only", head).decode().split("\n")
                         if x)

    def quarantine(f: str) -> bool:
        d = os.path.dirname(f)
        return (f.endswith(".py") and f.startswith("valence_core/")
                and os.path.basename(d) not in ("e2b", "regression")
                and "__pycache__" not in d)

    def qwen(f: str) -> bool:
        return f.endswith(".py") and not any(
            p in QWEN_SCAN_SKIP for p in os.path.dirname(f).split("/"))
    present = [x for x in changed if os.path.isfile(os.path.join(REPO, x))]
    scan_both = [x for x in present if quarantine(x) and qwen(x)]
    scan_qwen_only = [x for x in present if qwen(x) and not quarantine(x)]
    tracked = set(git("ls-files").decode().split("\n"))
    untracked_py = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = sorted(d for d in dirs if d not in QWEN_SCAN_SKIP)
        for f in sorted(files):
            if f.endswith(".py"):
                rel = os.path.relpath(os.path.join(root, f), REPO)
                if rel not in tracked:
                    untracked_py.append(rel)
    return {"commits_after_pin": len(commits), "by_commit": by_commit,
            "no_commit": no_commit, "uncommitted": uncommitted,
            "scan_both": scan_both, "scan_qwen_only": scan_qwen_only,
            "untracked_py_scanned": untracked_py}


# ------------------------------------------- portability fix / re-run check --

TEMP_TOKEN = "<tempfile.gettempdir()>"


def tempdir_display(path: str) -> str:
    """`path` with this machine's tempfile.gettempdir() prefix (as given or as
    its realpath) written <tempfile.gettempdir()>: the per-user temp directory
    is machine-specific, so the outputs do not print it."""
    t = tempfile.gettempdir()
    for base in sorted({t.rstrip(os.sep), os.path.realpath(t).rstrip(os.sep)},
                       key=len, reverse=True):
        if path == base or path.startswith(base + os.sep):
            return TEMP_TOKEN + path[len(base):]
    return path


def flatten(x, pre: str = "") -> dict:
    """JSON leaves by path; a list of scalars is one leaf."""
    if isinstance(x, dict):
        if not x:
            return {pre: {}}
        out = {}
        for k, v in x.items():
            out.update(flatten(v, f"{pre}.{k}" if pre else str(k)))
        return out
    if isinstance(x, list) and any(isinstance(v, (dict, list)) for v in x):
        out = {}
        for i, v in enumerate(x):
            out.update(flatten(v, f"{pre}[{i}]"))
        return out
    return {pre: x}


def head_norm(s: str, heads: set[str]) -> str:
    """Every full and 7-character form of the given HEAD shas -> <HEAD>."""
    for h in sorted(heads, key=len, reverse=True):
        s = s.replace(h, "<HEAD>")
    return s


PRE_CLASS = (f"preprint of record re-pointed to the patched text ({PREPRINT_RULING}; "
             f"patch v7 since round 10, {PREPRINT_ROUTING_R10})")
NEW_R9 = "new in this version (round 9: preprint sentences checked on the patched text)"
NEW_R10 = ("new in this version (round 10: patch v7; round 9's findings on the patch disposed "
           "of, and new findings on the patch)")
# round 9: note 6's quote of preprint line 141, before and after it ran through '0.30)'
NOTE6_OLD = "'coherence degrades monotonically (audit-flagged rounds .000/.023/.047)'"
NOTE6_NEW = ("'coherence degrades monotonically (audit-flagged rounds .000/.023/.047 across "
             "0.10/0.20/0.30)'")
NOTE6_CLASS = ("note 6's quote of preprint line 141 now runs through '0.30)' (round 9; it "
               "closed a parenthesis the text does not close there)")


def pre_norm(s: str) -> str:
    """The patched (v7; since round 10 also v6) and the audited preprint sha (full and
    8-character forms) -> <PREPRINT>."""
    for h in (PREPRINT_SHA, PREPRINT_SHA_V6, PREPRINT_SHA_AUDITED, PREPRINT_SHA[:8],
              PREPRINT_SHA_V6[:8], PREPRINT_SHA_AUDITED[:8]):
        s = s.replace(h, "<PREPRINT>")
    return s


def note6_cls(o_, n_):
    """NOTE6_CLASS (with PRE_CLASS when the preprint sha moved too) if undoing note 6's
    quote change, and normalising the preprint sha, makes the two values equal."""
    def u(v):
        return (v.replace(NOTE6_NEW, NOTE6_OLD) if isinstance(v, str) else
                [x.replace(NOTE6_NEW, NOTE6_OLD) if isinstance(x, str) else x for x in v]
                if isinstance(v, list) else v)
    def pn(v):
        return (pre_norm(v) if isinstance(v, str) else
                [pre_norm(x) if isinstance(x, str) else x for x in v]
                if isinstance(v, list) else v)
    un = u(n_)
    if un == n_:
        return None
    if un == o_:
        return NOTE6_CLASS
    if pn(un) == pn(o_):
        return NOTE6_CLASS + "; " + PRE_CLASS
    return None


# md line prefixes / JSON paths of the run-dependent outputs, with their class
MD_CLASSES = (
    (f"- `{PREPRINT}` (untracked) sha256", PRE_CLASS),
    ("- Code stamp:", "stamp"),
    ("- Script:", "script sha256"),
    ("- Command:", "command echo (with --scratch given, it carried the work root)"),
    ("- Tracked files whose working-tree content differs from the pin",
     "tracked files differing from the pin (moves with HEAD and the working tree)"),
    ("  Attribution (computed from the list at run start)",
     "attribution sentence (moves with HEAD and the working tree)"),
)
# a paired line whose old and new forms differ by design: (old prefix, new prefix, class)
MD_PAIR_CLASSES = (
    ("  These are the concurrent PROPOSAL-m session's",
     "  Attribution (computed from the list at run start)",
     "attribution sentence, computed since values-check round 3 (was fixed text)"),
)
NEW_R3 = "new in this version (values-check round 3)"
NEW_ATTR = "new in this version (attribution of the list, values-check round 3)"
JSON_NEW_PREFIXES = {
    "values_check_round3": NEW_R3,
    "integrity.tracked_files_differing_from_pin_attribution": NEW_ATTR,
    "integrity.preprint_of_record": NEW_R9,
    "integrity.preprint_round10": NEW_R10,
}
MD_SIDE = ("    repository side effects:",
           "working-tree state: counts of untracked / ignored paths (machine state)")
JSON_CLASSES = {
    "meta.stamp_date_u": "stamp",
    "meta.script_sha256": "script sha256",
    "meta.command": "command echo (with --scratch given, it carried the work root)",
    "meta.head_at_start": "HEAD (the source repository's HEAD moved)",
    "meta.head_at_end": "HEAD (the source repository's HEAD moved)",
    "suite.head_at_wt_run_end": "HEAD (the source repository's HEAD moved)",
    "integrity.tracked_files_differing_from_pin":
        "tracked files differing from the pin (moves with HEAD and the working tree)",
    "integrity.preprint_sha256": PRE_CLASS,
}
HEAD_CLASS = "HEAD (the source repository's HEAD moved)"
UNEXPECTED = "UNEXPECTED"
# Round 9's pre_gate (a preprint row UNEXPECTED when the root preprint was not the
# preprint of record) is retired at round 10: such a text is refused before
# anything is made, so every run that reaches the comparison read the preprint of
# record.


def compare_md(old: list[str], new: list[str], heads: set[str],
               new_ranges=()) -> list[dict]:
    """new_ranges: (start, end, class) blocks of `new` (0-based, end exclusive)
    that are new in this version; a blank line just outside one counts with it
    (the aligner may pair blank lines either way)."""
    def in_new(j):
        for a_, b_, c_ in new_ranges:
            if a_ <= j < b_ or (new[j] == "" and j in (a_ - 1, b_)):
                return c_
        return None
    rows = []
    # aligned on HEAD-normalised lines (values-check round 3: once round 3's
    # block is inserted, 'HEAD at run end' no longer pairs by position), and
    # since round 9 on preprint-sha-normalised lines too
    sm = difflib.SequenceMatcher(None, [pre_norm(head_norm(x, heads)) for x in old],
                                 [pre_norm(head_norm(x, heads)) for x in new],
                                 autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                o_, n_ = old[i1 + k], new[j1 + k]
                if o_ != n_:
                    rows.append({"line_new": j1 + k + 1, "line_old": i1 + k + 1,
                                 "class": HEAD_CLASS if head_norm(o_, heads) ==
                                 head_norm(n_, heads) else PRE_CLASS if pre_norm(o_) ==
                                 pre_norm(n_) else HEAD_CLASS + "; " + PRE_CLASS})
            continue
        if tag == "replace" and i2 - i1 == j2 - j1:
            for k in range(i2 - i1):
                o_, n_ = old[i1 + k], new[j1 + k]
                if in_new(j1 + k):
                    rows.append({"line_new": None, "line_old": i1 + k + 1, "class":
                                 UNEXPECTED + " (line only at the compared commit)"})
                    rows.append({"line_new": j1 + k + 1, "line_old": None,
                                 "class": in_new(j1 + k)})
                    continue
                cls = next((c for p, c in MD_CLASSES
                            if o_.startswith(p) and n_.startswith(p)), None)
                if cls is None:
                    cls = next((c for po, pn, c in MD_PAIR_CLASSES
                                if o_.startswith(po) and n_.startswith(pn)), None)
                if cls is None and o_.startswith(MD_SIDE[0]) and n_.startswith(MD_SIDE[0]):
                    cls = MD_SIDE[1]
                if cls is None and head_norm(o_, heads) == head_norm(n_, heads):
                    cls = HEAD_CLASS
                if cls is None and pre_norm(o_) == pre_norm(n_):
                    cls = PRE_CLASS
                if cls is None:
                    cls = note6_cls(o_, n_)
                rows.append({"line_new": j1 + k + 1, "line_old": i1 + k + 1,
                             "class": cls or UNEXPECTED})
            continue
        js = [j for j in range(j1, j2) if not in_new(j)]
        if tag == "replace" and len(js) == i2 - i1:
            # round 9: §0's round-9 lines sit next to the per-run lines (tracked
            # files differing, attribution sentence), which makes that replace block
            # unequal; the new lines are classed as new, and the remaining lines are
            # paired in order under the same rules as the equal-size branch above
            pair = dict(zip(js, range(i1, i2)))
            for j in range(j1, j2):
                if j not in pair:
                    rows.append({"line_new": j + 1, "line_old": None, "class": in_new(j)})
                    continue
                o_, n_ = old[pair[j]], new[j]
                cls = next((c for p, c in MD_CLASSES
                            if o_.startswith(p) and n_.startswith(p)), None)
                if cls is None:
                    cls = next((c for po, pn, c in MD_PAIR_CLASSES
                                if o_.startswith(po) and n_.startswith(pn)), None)
                if cls is None and o_.startswith(MD_SIDE[0]) and n_.startswith(MD_SIDE[0]):
                    cls = MD_SIDE[1]
                if cls is None and head_norm(o_, heads) == head_norm(n_, heads):
                    cls = HEAD_CLASS
                if cls is None and pre_norm(o_) == pre_norm(n_):
                    cls = PRE_CLASS
                if cls is None:
                    cls = note6_cls(o_, n_)
                rows.append({"line_new": j + 1, "line_old": pair[j] + 1,
                             "class": cls or UNEXPECTED})
            continue
        for i in range(i1, i2):
            rows.append({"line_new": None, "line_old": i + 1,
                         "class": UNEXPECTED + " (line only at the compared commit)"})
        for j in range(j1, j2):
            rows.append({"line_new": j + 1, "line_old": None,
                         "class": in_new(j) or UNEXPECTED + " (line only in this run)"})
    return rows


def compare_json(old, new, heads: set[str]) -> list[dict]:
    fo, fn = flatten(old), flatten(new)
    rows = []
    for k in list(fo) + [k for k in fn if k not in fo]:
        if k in fo and k in fn and fo[k] == fn[k]:
            continue
        if k not in fn or k not in fo:
            newc = (next((c for p, c in JSON_NEW_PREFIXES.items()
                          if k == p or k.startswith((p + ".", p + "[")))
                         , None) if k not in fo else None)
            rows.append({"path": k, "class": newc or UNEXPECTED + (
                " (only at the compared commit)" if k not in fn else " (only in this run)")})
            continue
        cls = JSON_CLASSES.get(k)
        if (cls is None and isinstance(fo[k], str) and isinstance(fn[k], str)
                and head_norm(fo[k], heads) == head_norm(fn[k], heads)):
            cls = HEAD_CLASS
        def _pn(v):
            return (pre_norm(v) if isinstance(v, str) else
                    [pre_norm(x) if isinstance(x, str) else x for x in v]
                    if isinstance(v, list) else v)
        if cls is None and _pn(fo[k]) == _pn(fn[k]):
            cls = PRE_CLASS
        if cls is None:
            cls = note6_cls(fo[k], fn[k])
        rows.append({"path": k, "class": cls or UNEXPECTED})
    return rows


# ================================================================== main ==

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEF_OUT)
    ap.add_argument("--json-out", default=DEF_JSON)
    ap.add_argument("--scratch", default=None,
                    help="work root for the suite TMPDIRs and the git-archive "
                         "extraction (default: a fresh tempfile.mkdtemp "
                         f"directory, prefix {SCRATCH_PREFIX!r}, under "
                         "tempfile.gettempdir())")
    ap.add_argument("--keep-tree", action="store_true",
                    help="keep the git-archive extraction (debugging only)")
    ap.add_argument("--compare-rev", default=COMPARE_REV,
                    help="commit whose committed N8 md/JSON this run's outputs "
                         f"are compared with (default {COMPARE_REV})")
    args = ap.parse_args()
    # Checked before anything is made (values-check round 3, finding 5): the
    # untracked preprint is an input this script cannot run without; a fresh
    # clone does not carry it unless the PI commits it.
    if not os.path.isfile(os.path.join(REPO, PREPRINT)):
        print(f"[not run: {PREPRINT} absent] this script reads the untracked preprint "
              f"(sha256 {PREPRINT_SHA[:8]}...{PREPRINT_SHA[-5:]}) for its integrity check and "
              "its wording locators; a fresh clone does not carry it unless it is committed. "
              "Nothing was made or written.", file=sys.stderr)
        return 2
    # Round 10: the preprint of record is asserted in full here, before anything
    # is made (as N4, N5, N6, N7, N17); round 9 compared it in §0 and, on any
    # other text, wrote its outputs before exiting 3.
    with open(os.path.join(REPO, PREPRINT), "rb") as f:
        pre_b = f.read()
    pre_sha = sha256_bytes(pre_b)
    if pre_sha != PREPRINT_SHA:
        print(f"[refusing: {PREPRINT} sha256 {pre_sha} is not the preprint of record "
              f"{PREPRINT_SHA} (patch v7; {PREPRINT_ROUTING_R10}). Nothing was made or "
              "written.]", file=sys.stderr)
        return 3
    scratch_made = args.scratch is None
    scratch_existed = (not scratch_made) and os.path.isdir(args.scratch)
    if scratch_made:
        args.scratch = tempfile.mkdtemp(prefix=SCRATCH_PREFIX)

        def _scratch_at_exit(path=args.scratch):
            # a work root this run made is removed at exit only if empty (a
            # run that stops before the suite runs); otherwise it stays, as
            # the cleanup bullet of the closing section says
            try:
                os.rmdir(path)
            except OSError:
                pass
        atexit.register(_scratch_at_exit)
    print(f"work root: {args.scratch}", file=sys.stderr)

    L: list[str] = []          # markdown lines
    J: dict = {"item": "N8", "pin": PIN}
    P = L.append

    stamp = subprocess.run(["date", "-u"], capture_output=True, text=True).stdout.strip()
    head0 = git("rev-parse", "HEAD").decode().strip()
    pin_full = git("rev-parse", PIN).decode().strip()
    block_pin = sha256_bytes(pinned(BLOCK))
    with open(os.path.join(REPO, BLOCK), "rb") as f:
        block_wt = sha256_bytes(f.read())
    with open(os.path.abspath(__file__), "rb") as f:
        script_sha = sha256_bytes(f.read())
    script_rel = os.path.relpath(os.path.abspath(__file__), REPO)
    cmdline = " ".join(shlex.quote(x) for x in [sys.executable, script_rel] + sys.argv[1:])
    blk_lines = lines_with(pinned_text(BLOCK), "### N8. Link 2")
    J["meta"] = {"stamp_date_u": stamp, "head_at_start": head0, "pin": pin_full,
                 "block_sha256_pin": block_pin, "block_sha256_wt": block_wt,
                 "script": script_rel, "script_sha256": script_sha,
                 "interpreter": sys.executable,
                 "python": sys.version.split()[0], "numpy": np.__version__,
                 "command": cmdline}

    P("# AUDIT-note-release v1.2 -- N8: link 2 (Qwen hijack) via the regression suite")
    P("")
    P(f"- Code stamp: {stamp} (date -u)  [run metadata]")
    P(f"- HEAD at run start: {head0}  [run metadata; every record read below is pinned to {PIN}]")
    P(f"- Pin: {PIN} = {pin_full}")
    P(f"- Block: `{BLOCK}`@{PIN} sha256 `{block_pin}` "
      f"({'MATCH' if block_pin == BLOCK_SHA else 'MISMATCH'} vs routed 8cd8a9ac...3841; "
      f"working tree {'equal' if block_wt == block_pin else 'DIFFERENT'}); item N8 = block lines "
      f"{blk_lines[0]}-{blk_lines[0] + 1}")
    P(f"- Script: `{script_rel}` sha256 `{script_sha}`")
    P(f"- Interpreter: {sys.executable} (Python {sys.version.split()[0]}, numpy {np.__version__}); "
      "no scipy/sklearn; exact tests in the stdlib (math.comb); no model loaded, no inference")
    P(f"- Command: `{cmdline}`  [run metadata]")
    P("")
    P("Status vocabulary: reproduced (this script computes the figure from committed JSON/npz at the "
      "pin and prints it) | log-only (exists only in log prose; pinned locator) | not found | "
      "discrepant | computed-new. Locators are `path@bbc9ffe:line` as `git show bbc9ffe:<path>` "
      "numbers them. The note itself (RESEARCH-NOTE-v0_2-draft.md) is not on this machine "
      "(preflight raw, note 1); where a figure's wording matters, the untracked "
      f"`{PREPRINT}` (sha256 checked below) is the nearest carrier of the same sentences.")
    P("")

    # ------------------------------------------------------------ integrity
    P("## 0. Integrity")
    P("")
    pre_match = pre_sha == PREPRINT_SHA     # asserted above, before anything was made
    P(f"- `{PREPRINT}` (untracked) sha256 `{pre_sha}`: "
      f"{'MATCH' if pre_match else 'MISMATCH'} vs the preprint of record "
      f"{PREPRINT_SHA[:8]}...{PREPRINT_SHA[-5:]}, the patched text (patch v7; "
      f"{PREPRINT_ROUTING_R10}; findings on the patch under {PREPRINT_RULING}). "
      f"The patch-v6 text {PREPRINT_SHA_V6[:8]}...{PREPRINT_SHA_V6[-5:]}, round 9's preprint "
      f"of record, is archived untracked at `{PREPRINT_V6_COPY}` (out of the release; never "
      "required; read only if present and matching, see round 10 below). "
      f"The block's {PREPRINT_SHA_AUDITED[:8]}...{PREPRINT_SHA_AUDITED[-5:]} is the audited, "
      f"superseded text, archived untracked at `{PREPRINT_AUDITED_COPY}` (out of the release; "
      "not opened or required here). Asserted in full before anything was made: any "
      "other root text is refused (exit 3, nothing written).")
    imported = ["valence_core/__init__.py", "valence_core/adapters/__init__.py",
                "valence_core/adapters/base.py", "valence_core/readout.py",
                "valence_core/regression/__init__.py",
                "valence_core/regression/oracle.py",
                "valence_core/regression/analysis.py", "valence_core/extract.py",
                "valence_core/stats.py", "data/e0/e0_b1_markers.npz",
                "data/e0/e0_axes.npz", "data/e0/e0_axes.meta.json",
                "scripts/e2d_closure_verify3.py", "valence_core/e2d/marks.py",
                "valence_core/e2d/readability.py", "scripts/e2d_score.py"]
    integ = {p: blob_equal_to_pin(p) for p in imported}
    P("- Working-tree blobs vs the pin, for the one function imported from the working tree "
      "(`valence_core.regression.oracle.build_instruments`, which reads "
      "`data/e0/e0_b1_markers.npz` from the working tree), its import chain, and the files whose "
      "definitions are ported here:")
    for p, ok in integ.items():
        P(f"    - `{p}`: {'EQUAL to pin' if ok else 'DIFFERENT from pin'}")
    if not all(integ.values()):
        P("  STOP-relevant: a referent differs from the pin; figures below read the pin, the "
          "imported function does not.")
    changed = [x for x in git("diff", "--name-only", PIN).decode().split("\n") if x]
    J["integrity"] = {"preprint_sha256": pre_sha, "blobs_equal_to_pin": integ,
                      "tracked_files_differing_from_pin": changed}
    P(f"- Tracked files whose working-tree content differs from the pin (`git diff --name-only "
      f"{PIN}`), at run start: {len(changed)} -- " + ", ".join(f"`{c}`" for c in changed))
    # Attribution, computed from the list (values-check round 3, finding 2: this
    # was a fixed sentence written at the first run's HEAD, stale at any later one).
    attr = attribute_changed(changed, head0)
    J["integrity"]["tracked_files_differing_from_pin_attribution"] = attr

    def fl(xs, k=6):
        xs = list(xs)
        return (", ".join(f"`{x}`" for x in xs[:k]) +
                (f" and {len(xs) - k} more" if len(xs) > k else "")) if xs else "none"
    P("  Attribution (computed from the list at run start): by the commits after the pin that "
      f"touch them (`git log {PIN}..HEAD`; a file counts under each commit that touches it): " +
      "; ".join(f"{c['commit']} {c['date']} '{c['subject_head']}': {c['files']}"
                for c in attr["by_commit"]) +
      f"; touched by none of them (working-tree change only): {len(attr['no_commit'])} "
      f"({fl(attr['no_commit'])}); with uncommitted working-tree changes against HEAD: "
      f"{len(attr['uncommitted'])} ({fl(attr['uncommitted'])}). The suite's two structural "
      "source scans read .py files by directory walk (the quarantine offender scan every .py "
      "under valence_core/ outside e2b/ and regression/; the qwen-helper definition scan every "
      ".py outside .git, __pycache__, jlens-qwen36 and archive, untracked and ignored files "
      f"included): of the listed files, {len(attr['scan_both'])} are read by both scans "
      f"({fl(attr['scan_both'])}) and {len(attr['scan_qwen_only'])} by the qwen-helper scan "
      f"only ({fl(attr['scan_qwen_only'])}); .py files the qwen-helper scan reads that are "
      f"not tracked at HEAD: {len(attr['untracked_py_scanned'])} "
      f"({fl(attr['untracked_py_scanned'])}). Which listed files the suite opens otherwise is "
      "not computed here. Run (b) below runs the suite on the pin's own tree, where none of "
      "these changes exists.")
    P("")
    # Round 9 (ruling 9): every preprint sentence this script locates or quotes,
    # checked on the patched text; one not found is a finding on the patch for
    # the design seat, never a stop (the root preprint is the preprint of record:
    # since round 10 any other text is refused before anything is made).
    pre_lines = pre_b.decode("utf-8").split("\n")
    pre_rows, pre_find = [], []
    for s_, old_ln, use in PREPRINT_SENTENCES:
        hits = lines_with("\n".join(pre_lines), s_)
        pre_rows.append({"sentence": s_, "use": use, "audited_line": old_ln,
                         "patched_lines": hits,
                         "state": ("same line" if hits and hits[0] == old_ln else
                                   "re-anchored" if hits else "NOT FOUND")})
        if not hits:
            pre_find.append({"sentence": s_, "use": use,
                             "old": f"{PREPRINT}@{PREPRINT_SHA_AUDITED[:8]}:{old_ln}",
                             "new": f"{PREPRINT}@{pre_sha[:8]}:{old_ln}",
                             "new_line_text": (pre_lines[old_ln - 1]
                                               if old_ln <= len(pre_lines) else None)})
    J["integrity"]["preprint_of_record"] = {
        "ruling": PREPRINT_RULING, "sha256": PREPRINT_SHA,
        "measured_sha256": pre_sha, "match": pre_match,
        "audited_superseded_sha256": PREPRINT_SHA_AUDITED,
        "audited_copy_untracked_not_opened": PREPRINT_AUDITED_COPY,
        "sentences": pre_rows,
        "findings_on_the_patch": pre_find,
        # kept for the key's stability; always empty since round 10 (a text not
        # of record is refused before anything is made)
        "not_found_on_a_text_not_of_record": []}
    r9_start = len(L)
    P(f"- Round 9 ({PREPRINT_RULING}): the {len(pre_rows)} preprint sentences this script "
      "locates or quotes, checked on the patched text: " +
      f"{sum(r['state'] == 'same line' for r in pre_rows)} on the line they stood on in the "
      f"audited text, {sum(r['state'] == 're-anchored' for r in pre_rows)} re-anchored, "
      f"{len(pre_find)} not found (" + "; ".join(
          f"'{r['sentence']}' :{r['audited_line']}->" +
          (",".join(map(str, r['patched_lines'])) or "none") for r in pre_rows) + ").")
    if pre_find:
        P("  Findings on the patch, for the design seat (ruling 9; not a STOP): " + "; ".join(
            f"'{f_['sentence']}' ({f_['use']}) stood at {f_['old']} and is not in the patched "
            f"text; its line {f_['new']} now reads: '{cell(f_['new_line_text'])}'"
            for f_ in pre_find) + ".")
    else:
        P("  Findings on the patch (ruling 9): none.")
    P("")
    r9_end = len(L)
    # Round 10 (the PI's routing of 2026-10-12): the sentence check above ran on
    # patch v7. The patch-v6 text is read only if present and matching (never
    # required). Round 9's findings on the patch are read from the raw committed at
    # R9_RAW_REV, each disposed of on v7 (resolved: found on v7; unchanged: not
    # found and its line as round 9 quoted it; changed: not found, line quoted v6
    # and v7). New findings: a sentence round 9 found and v7 does not carry, and a
    # line this script reads that v7 changed (its figures to be checked against
    # this script's record sources). The root preprint is the preprint of record
    # (any other text was refused before anything was made); a finding on the
    # patch is never a stop (ruling 9).
    v6_lines, v6_state = None, "absent (not required)"
    if os.path.isfile(os.path.join(REPO, PREPRINT_V6_COPY)):
        with open(os.path.join(REPO, PREPRINT_V6_COPY), "rb") as f:
            v6_b = f.read()
        if sha256_bytes(v6_b) == PREPRINT_SHA_V6:
            v6_lines, v6_state = v6_b.decode("utf-8").split("\n"), "present, sha256 matching, read"
        else:
            v6_state = (f"present, sha256 {sha256_bytes(v6_b)[:8]}... NOT matching "
                        f"{PREPRINT_SHA_V6[:8]}...{PREPRINT_SHA_V6[-5:]}, not read")
    chg_v6, chg_v7, v7_to_v6, v6_to_v7 = [], [], {}, {}
    if v6_lines is not None:
        for tag_, i1_, i2_, j1_, j2_ in difflib.SequenceMatcher(
                None, v6_lines, pre_lines, autojunk=False).get_opcodes():
            # 1-based line alignment both ways: an equal block maps line for line; a
            # changed block maps by position within it (None past its shorter side)
            for i_ in range(i1_, i2_):
                v6_to_v7[i_ + 1] = (j1_ + (i_ - i1_) + 1
                                    if j1_ + (i_ - i1_) < j2_ else None)
            if tag_ != "equal":
                chg_v6 += list(range(i1_ + 1, i2_ + 1))
                chg_v7 += list(range(j1_ + 1, j2_ + 1))
                for j_ in range(j1_, j2_):
                    v7_to_v6[j_ + 1] = (i1_ + (j_ - j1_) + 1
                                        if i1_ + (j_ - j1_) < i2_ else None)
    def nlines(xs):
        # newline-terminated lines (wc -l): split("\n") leaves '' after the final newline
        return len(xs) - (1 if xs and xs[-1] == "" else 0)
    read_v7 = sorted({h for r in pre_rows for h in r["patched_lines"]})
    read_chg = [ln for ln in read_v7 if ln in chg_v7]
    r9_src = f"{R9_RAW_REV}:{DEF_JSON}"
    try:
        r9_por = json.loads(git("show", r9_src))["integrity"]["preprint_of_record"]
        r9_find, r9_sent = r9_por["findings_on_the_patch"], r9_por["sentences"]
        r9_err = None
    except (subprocess.CalledProcessError, KeyError, ValueError) as e:
        r9_find, r9_sent, r9_err = [], [], type(e).__name__
    disp = []
    for f_ in r9_find:
        ln = int(f_["new"].rsplit(":", 1)[1])      # a patch-v6 line number
        v6_l = (v6_lines[ln - 1] if v6_lines is not None and ln <= len(v6_lines)
                else f_.get("new_line_text"))
        # its patch-v7 line through the alignment; the same number when v6 is not read
        ln7 = v6_to_v7.get(ln) if v6_lines is not None else ln
        v7_l = pre_lines[ln7 - 1] if ln7 and ln7 <= len(pre_lines) else None
        hits7 = lines_with("\n".join(pre_lines), f_["sentence"])
        disp.append({"sentence": f_["sentence"], "use": f_["use"], "round9": f_["new"],
                     "v7_lines": hits7, "v6_line": ln, "v7_line": ln7,
                     "disposition": ("resolved" if hits7 else
                                     "unchanged" if v7_l == v6_l else "changed"),
                     "v6_line_text": v6_l, "v7_line_text": v7_l})
    r9_found = {r["sentence"] for r in r9_sent if r.get("patched_lines")}
    new_find = []
    for r in pre_rows:
        if not r["patched_lines"] and r["sentence"] in r9_found:
            new_find.append({"kind": "found on patch v6 (round 9), not found on patch v7",
                             "sentence": r["sentence"], "use": r["use"],
                             "v6_lines": next(x["patched_lines"] for x in r9_sent
                                              if x["sentence"] == r["sentence"])})
    for ln in read_chg:
        new_find.append({"kind": "a line this script reads changed from patch v6 to patch v7 "
                                 "(its figures to be checked against this script's record "
                                 "sources)",
                         "line": ln, "sentences": [r["sentence"] for r in pre_rows
                                                   if ln in r["patched_lines"]],
                         "v6_line_text": (v6_lines[v7_to_v6[ln] - 1] if v7_to_v6[ln]
                                          else None),
                         "v7_line_text": pre_lines[ln - 1]})
    J["integrity"]["preprint_round10"] = {
        "routing": PREPRINT_ROUTING_R10, "sha256": PREPRINT_SHA,
        "measured_sha256": pre_sha, "match": pre_match,
        "patch_v6_sha256": PREPRINT_SHA_V6,
        "patch_v6_copy_untracked_never_required": PREPRINT_V6_COPY,
        "patch_v6_copy_state": v6_state,
        "line_counts": {"v6": nlines(v6_lines) if v6_lines is not None else None,
                        "v7": nlines(pre_lines)},
        "lines_changed_v6_to_v7": ({"v6": chg_v6, "v7": chg_v7} if v6_lines is not None
                                   else None),
        "lines_read_by_this_script_v7": read_v7,
        "lines_read_changed_by_v7": read_chg if v6_lines is not None else None,
        "round9_findings_source": r9_src + " integrity.preprint_of_record.findings_on_the_patch",
        "round9_findings_read_error": r9_err,
        "round9_findings_recorded": len(r9_find),
        "round9_findings_dispositions": disp,
        "new_findings_on_the_patch": new_find}
    r10_start = len(L)
    r10_here = "patch v7"
    P(f"- Round 10 ({PREPRINT_ROUTING_R10}): the sentence check above ran on {r10_here} "
      f"({pre_sha[:8]}...). The patch-v6 text ({PREPRINT_SHA_V6[:8]}...{PREPRINT_SHA_V6[-5:]}) at "
      f"`{PREPRINT_V6_COPY}`: {v6_state}" +
      (f"; lines changed from it to {r10_here} ({nlines(v6_lines)} lines there, "
       f"{nlines(pre_lines)} here): {', '.join(map(str, chg_v7)) or 'none'}"
       if v6_lines is not None else "") +
      f". Lines of {r10_here} this script reads (its {len(pre_rows)} sentences): "
      f"{', '.join(map(str, read_v7)) or 'none'}; of them changed: " +
      (", ".join(map(str, read_chg)) or "none" if v6_lines is not None else
       "not computed (the patch-v6 copy was not read)") + ".")
    P(f"  Round 9's findings on the patch (`git show {r9_src}`, "
      "integrity.preprint_of_record.findings_on_the_patch): " +
      (f"NOT READ ({r9_err})" if r9_err else f"{len(r9_find)} recorded") +
      (": " + "; ".join(
          f"'{d['sentence']}' ({d['use']}, {d['round9']}): {d['disposition']}" +
          (f" ({r10_here} :{','.join(map(str, d['v7_lines']))})" if d["v7_lines"] else
           f"; v6 :{d['v6_line']} read: '{cell(d['v6_line_text'])}'; v7 :{d['v7_line']} "
           f"reads: '{cell(d['v7_line_text'])}'"
           if d["disposition"] == "changed" else "")
          for d in disp) + "." if disp else
       ("." if r9_err else f", so none to dispose of on {r10_here}.")))
    if new_find:
        P(f"  New findings on the patch at round 10, for the design seat ({PREPRINT_RULING}; not "
          "a STOP): " + "; ".join(
            f"{x['kind']}: " + (f"'{x['sentence']}' ({x['use']}; patch v6 :"
                                f"{','.join(map(str, x['v6_lines']))})" if "sentence" in x else
                                f"line {x['line']} ({'; '.join(repr(s) for s in x['sentences'])}); "
                                f"v6 read: '{cell(x['v6_line_text'])}'; v7 reads: "
                                f"'{cell(x['v7_line_text'])}'") for x in new_find) + ".")
    else:
        P("  New findings on the patch at round 10: none (no sentence round 9 found is missing "
          "from patch v7" + ("; no line this script reads changed)." if v6_lines is not None
                             else "; changed lines not computed, the patch-v6 copy not read)."))
    P("")
    r10_end = len(L)

    # ------------------------------------------------------------ suite runs
    P("## 1. The model-free regression suite")
    P("")
    os.makedirs(args.scratch, exist_ok=True)
    before_ign = untracked_ignored()
    before_unt = untracked_plain()
    wt = run_suite(REPO, os.path.join(args.scratch, "tmp-wt"))
    after_ign = untracked_ignored()
    after_unt = untracked_plain()
    head1 = git("rev-parse", "HEAD").decode().strip()

    tree = os.path.join(args.scratch, f"tree-{PIN}")
    if os.path.exists(tree):
        shutil.rmtree(tree)
    os.makedirs(tree)
    tar_bytes = git("archive", "--format=tar", PIN, "--", "valence_core", "scripts", "data")
    with tarfile.open(fileobj=io.BytesIO(tar_bytes)) as tf:
        members = tf.getmembers()
        n_files = sum(1 for m in members if m.isfile())
        tf.extractall(tree, filter="data")
    pn = run_suite(tree, os.path.join(args.scratch, "tmp-pin"))
    if not args.keep_tree:
        shutil.rmtree(tree)

    def summ(r):
        return f"{r['summary'][0]}/{r['summary'][1]}" if r["summary"] else "NO SUMMARY LINE"

    same_stdout = wt["stdout"] == pn["stdout"]
    J["suite"] = {
        "working_tree": {k: wt[k] for k in ("cmd", "exit", "summary", "n_status_lines",
                                            "stdout_sha256", "stderr")},
        "pinned_tree": {k: pn[k] for k in ("cmd", "exit", "summary", "n_status_lines",
                                           "stdout_sha256", "stderr")},
        "pinned_tree_files_extracted": n_files,
        "stdout_identical": same_stdout, "head_at_wt_run_end": head1,
        "repo_untracked_ignored_before_after_equal": before_ign == after_ign,
        "repo_untracked_before_after_equal": before_unt == after_unt,
        "checks": wt["checks"]}
    P(f"(a) Working tree, from the repository root (HEAD {head0[:7]} at start, {head1[:7]} at the "
      f"end of the run): `{wt['cmd']}` with TMPDIR=<scratch>/tmp-wt and PYTHONDONTWRITEBYTECODE=1.")
    P(f"    exit {wt['exit']}; summary line `{summ(wt)} reproduced through valence_core`; "
      f"[PASS]/[FAIL] lines {wt['n_status_lines']} (parsed {len(wt['checks'])}); "
      f"stderr {'empty' if not wt['stderr'] else repr(wt['stderr'][:200])}; "
      f"stdout sha256 {wt['stdout_sha256'][:16]}")
    P(f"    repository side effects: untracked-and-ignored paths under valence_core/, scripts/, data/ "
      f"{'unchanged' if before_ign == after_ign else 'CHANGED'} ({len(before_ign)} before, "
      f"{len(after_ign)} after); untracked-not-ignored "
      f"{'unchanged' if before_unt == after_unt else 'CHANGED'} ({len(before_unt)} before, "
      f"{len(after_unt)} after).")
    P(f"(b) At the pin: `git archive --format=tar {PIN} -- valence_core scripts data` extracted to "
      f"<scratch>/tree-{PIN} ({n_files} files; deleted after the run), same command from its root, "
      "TMPDIR=<scratch>/tmp-pin.")
    P(f"    exit {pn['exit']}; summary line `{summ(pn)} reproduced through valence_core`; "
      f"[PASS]/[FAIL] lines {pn['n_status_lines']}; stderr "
      f"{'empty' if not pn['stderr'] else repr(pn['stderr'][:200])}; stdout sha256 "
      f"{pn['stdout_sha256'][:16]}; byte-identical to (a): {'yes' if same_stdout else 'NO'}")
    n_fail = sum(1 for c in wt["checks"] if c["status"] == "FAIL")
    P("")
    # Values-check finding 6: scan the FULL commit message (subject + body),
    # not the subject only -- 6897b67 names 103 -> 125 in its body, and
    # da71287 / c593579 name "SUITE IS NOW 136/137" in theirs.
    count_rx = re.compile(
        r"(?:[Ss]uite|SUITE)(?: IS NOW| now| stays at| to| --)? ?(?:(\d+) ?(?:->|→) ?)?(\d+)(?:/(\d+))?"
        r"|(?:[Ss]uite) -> (\d+)")
    chain, chain_full = [], []
    hashes = git("log", "--format=%h", PIN, "--",
                 "valence_core/regression/analysis.py").decode().split()
    for h in hashes:
        d = git("log", "-1", "--format=%ad", "--date=short", h).decode().strip()
        body = git("log", "-1", "--format=%B", h).decode()
        subj = git("log", "-1", "--format=%s", h).decode()   # git's subject (first paragraph, joined)
        hits = []
        for m in count_rx.finditer(body):
            if m.group(4):
                hits.append(f"-> {m.group(4)}")
            elif m.group(1):
                hits.append(f"{m.group(1)} -> {m.group(2)}")
            elif m.group(3):
                hits.append(f"{m.group(2)}/{m.group(3)}")
            else:
                hits.append(f"{m.group(0).strip()}")
        first = hits[0] if hits else None
        where = ("subject" if first and count_rx.search(subj) else
                 "body" if first else "-")
        chain_full.append({"commit": h, "date": d, "first_count_named": first,
                           "in": where, "all_named": hits})
        chain.append(f"{h} {d}: " + (f"{first} ({where})" if first else "no count named"))
    J["suite"]["count_history_from_commit_messages"] = chain_full
    # Round 2, finding 6: every '103/103' in the block, located at the pin
    # (§6 README-NOTE item (3) at :137 is where the stale count would reach
    # the release README).
    blk103 = lines_with(pinned_text(BLOCK), "103/103")
    assert blk103 == [68, 70, 107, 137], blk103
    J["suite"]["block_lines_with_103"] = blk103
    P(f"**What it prints: {summ(pn)} at {PIN} (and {summ(wt)} on the working tree at "
      f"{head0[:7]}), {n_fail} FAIL.** The block's \"103/103\" (block :107, also :68/:70 for N11 "
      "and :137 for §6 README-NOTE item (3)) is "
      "the count after the S2 build: " + loc("RESULTS.md", "Suite 83 → 103") +
      " (\"Suite 83 → 103\"), still printed in " + loc("README.md", "must print **103/103**") +
      ". Every commit touching valence_core/regression/analysis.py (`git log` at the pin, "
      f"newest first, {len(chain)} commits), with the first suite count its full message "
      "(subject + body) names and where: " +
      "; ".join(chain) + ". Steps a message does not name are not inferred. A stale count, "
      "not a transcription error and not a regression; N11 reports the same 154/154 from a "
      "fresh clone of the pin.")
    P("")

    # ---------------------------------------------------- oracle-tier status
    P("### 1b. The oracle tier (needs the model; NOT run here) and its committed record")
    P("")
    log = git("log", "--format=%h %ad", "--date=short", PIN, "--",
              "data/regression/oracle_rule26.json").decode().strip().split("\n")
    hist = []
    for row in log:
        h, d = row.split()
        doc = json.loads(git("show", f"{h}:data/regression/oracle_rule26.json"))
        hist.append({"commit": h, "date": d,
                     "rows": [(r["name"], r["got"], r["ok"]) for r in doc["results"]],
                     "has_check_key": "check" in doc})
    J["oracle_record_history"] = hist
    P("The oracle tier (`valence_core/regression/oracle.py`) holds Δ+/Δ− and the V1 verdict as "
      "criterion (ii): it re-runs 1,152 forwards per arm on the laptop Qwen stack and compares "
      "with `data/e0/e0_b2_b2b.json`. No inference is run in this audit. Its canonical artifact "
      "`data/regression/oracle_rule26.json`, by commit (read-only `git log`/`git show`):")
    for h in hist:
        P(f"- {h['commit']} ({h['date']}): {len(h['rows'])} rows -- " +
          "; ".join(f"{n} = {g} ({'ok' if ok else 'FAIL'})" for n, g, ok in h["rows"]))
    P("At the pin the canonical record holds only criterion (iii)'s four rows. The B2b rows "
      "(exact reproduction, 5/5: D+ +0.2848, D- -0.3946, paired TOST CI [0.0000, 0.0000]) "
      "exist at 9f3148c in this file's history and in the committed raw " +
      loc("results/raw/2026-08-12_rule26_b2b_tightened.txt", "5/5 criteria reproduced") +
      "; the kernel-gate rows and the earlier 128-context B2b rows are at db0d177 and in " +
      loc("results/raw/2026-08-12_rule26_oracle.txt", "8/8 criteria reproduced") +
      ". The two later versions each hold one criterion's rows only, consistent with subset runs "
      "(their commit subjects name a criterion (ii) re-run and a criterion (iii) re-verification), "
      "which `oracle.main()` then wrote to the canonical path unconditionally, as the docstring "
      "of the suite's write-guard check records; the guard added after the 2026-09-01 incident "
      "now refuses that (" +
      loc("valence_core/regression/analysis.py", "def check_oracle_write_guard") +
      "). Nothing is wrong with the figures; the README's account of what the oracle record "
      "covers should name these commits. Status of 'the oracle reproduced Δ± exactly': "
      "log-only (raw + history), not reproducible model-free.")
    P("")

    # ======================================================= reproductions
    P("## 2. Reproductions from committed artifacts (read at the pin)")
    P("")
    meta = pinned_json("data/e0/e0_axes.meta.json")
    Z = pinned_npz("data/e0/e0_axes.npz")
    layers = [int(x) for x in Z["layers"]]
    Rl = {int(k): float(v) for k, v in meta["R_per_layer_spanmean"].items()}
    stack = np.stack([Z["span_reward"], Z["span_sentiment"], Z["span_character"]])
    axes_sha = hashlib.sha256(np.ascontiguousarray(stack, dtype=np.float32).tobytes()
                              ).hexdigest()[:16]
    geo = {}
    for var in ("span", "last"):
        rows = []
        rep = {r["layer"]: r for r in meta["report"][var]}
        for li, Lr in enumerate(layers):
            rw = Z[f"{var}_reward"][li].astype(np.float64)
            se = Z[f"{var}_sentiment"][li].astype(np.float64)
            ch = Z[f"{var}_character"][li].astype(np.float64)
            r = {"layer": Lr, "norm_reward": float(np.linalg.norm(rw)), "R": Rl[Lr],
                 "norm_over_R": float(np.linalg.norm(rw)) / Rl[Lr],
                 "cos_sent": cosine(rw, se), "cos_char": cosine(rw, ch),
                 "v2_self_resid": residual_fraction(rw, ch),
                 "v3_eval_resid": residual_fraction(rw, se)}
            m = rep[Lr]
            r["meta_match"] = (round(r["norm_over_R"], 4) == m["reward_over_R"]
                               and round(r["cos_sent"], 3) == m["cos_reward_sentiment"]
                               and round(r["cos_char"], 3) == m["cos_reward_character"]
                               and round(r["v2_self_resid"], 3) == m["v2_self_residual_frac"]
                               and round(r["v3_eval_resid"], 3) == m["v3_eval_residual_frac"])
            rows.append(r)
        geo[var] = rows
    b2c = pinned_json("data/e0/e0_b2c_a.json")
    cos_span_last = {}
    for li, Lr in enumerate(layers):
        c = cosine(Z["span_reward"][li].astype(np.float64), Z["last_reward"][li].astype(np.float64))
        cos_span_last[Lr] = (c, b2c["cos_span_last_per_layer"][str(Lr)])
    # Round 2, finding 9: 1,344 is the whole capture (48 tasks x 7 frames x 4
    # paraphrases); each direction is the difference of two frames' means.
    n_frames = meta["n_contexts"] // (meta["n_tasks"] * meta["n_paraphrases"])
    per_frame = meta["n_tasks"] * meta["n_paraphrases"]
    assert n_frames * per_frame == meta["n_contexts"] == 1344 and n_frames == 7, (n_frames, per_frame)
    J["geometry"] = {"axes_sha16": axes_sha, "per_variant": geo,
                     "cos_span_last": {str(k): v for k, v in cos_span_last.items()},
                     "extraction_counts": {"n_contexts": meta["n_contexts"], "n_tasks": meta["n_tasks"],
                                           "n_paraphrases": meta["n_paraphrases"],
                                           "n_frames": n_frames, "contexts_per_frame": per_frame}}

    P("### 2a. Axis geometry (e0 extraction, Qwen3.6-27B 4-bit, workspace layers, span-mean "
      "primary and last-position variant)")
    P("")
    P(f"Source: `data/e0/e0_axes.npz` (frozen sha16 recomputed from the pinned bytes: `{axes_sha}`, "
      f"expected d4791bdc4877da3d: {'MATCH' if axes_sha == 'd4791bdc4877da3d' else 'MISMATCH'}); "
      "R_l = `e0_axes.meta.json` R_per_layer_spanmean (the per-layer norm the dose rule "
      "frac x R_l uses; 'S2: dose is frac x R_layer' checks 0.10 x R_48 = 10.3010). "
      "Each direction is the mean difference between two frames' means of raw-residual "
      f"activations ({per_frame} contexts each: {meta['n_tasks']} tasks x {meta['n_paraphrases']} "
      f"paraphrases) from the {meta['n_contexts']:,}-context extraction ({meta['n_tasks']} x "
      f"{n_frames} frames x {meta['n_paraphrases']}, `e0_axes.meta.json` n_contexts / n_tasks / "
      "n_paraphrases; " + loc("archive/RESULTS-cycles3-4.md", "1344 contexts (48 × 7 × 4)") +
      "); reward is praise minus criticism (" + loc(PREPRINT, "define the evaluative direction", True) +
      "); the constructs as `data/e0/s2_neighbor_axes.json` table[].construct states them: reward = "
      "self-directed evaluative feedback, sentiment = sentiment-matched, externally targeted "
      "valence, character = the identical feedback sentence addressed to a fictional third party. "
      "Cosines are plain cosines between the two difference vectors at one layer; V2 = fraction "
      "of the reward vector's norm orthogonal to the character vector, V3 = the same against "
      "sentiment (`valence_core/extract.py` definitions, ported). No CV: these are geometric "
      "quantities of fixed vectors.")
    P("")
    P("| variant | layer | ‖d‖ | R_l | ‖d‖/R | cos(d, sentiment) | cos(d, character) | V2 self-residual | V3 eval-residual | equals meta report |")
    P("|---|---|---|---|---|---|---|---|---|---|")
    for var in ("span", "last"):
        for r in geo[var]:
            P(f"| {var} | L{r['layer']} | {r['norm_reward']:.3f} | {r['R']:.2f} | "
              f"{r['norm_over_R']:.4f} | {r['cos_sent']:.4f} | {r['cos_char']:.4f} | "
              f"{r['v2_self_resid']:.4f} | {r['v3_eval_resid']:.4f} | "
              f"{'yes' if r['meta_match'] else 'NO'} |")
    P("")
    P("cos(span reward, last reward) per layer, recomputed vs `e0_b2c_a.json` "
      "cos_span_last_per_layer: " + ", ".join(
          f"L{k} {v[0]:.4f} (stored {v[1]})" for k, v in cos_span_last.items()))
    P("")
    sp, la = geo["span"], geo["last"]

    def rng_(rows, key, nd=3):
        v = [r[key] for r in rows]
        return min(v), max(v)

    span_nr = rng_(sp, "norm_over_R")
    off16 = [r for r in sp if f"{r['norm_over_R']:.2f}" != "0.16"]   # layers not .16 at 2 dp
    span_cs = rng_(sp, "cos_sent")
    span_cc = rng_(sp, "cos_char")
    span_v2 = rng_(sp, "v2_self_resid")
    last_cs = rng_(la, "cos_sent")
    last_v2 = rng_(la, "v2_self_resid")
    csl = [v[0] for v in cos_span_last.values()]
    L48 = next(r for r in sp if r["layer"] == 48)
    cc_mean = statistics.fmean(r["cos_char"] for r in sp)

    # ------------------------------------------------------------ instrument
    P("### 2b. The B1 instrument and G")
    P("")
    B1 = pinned_npz("data/e0/e0_b1_markers.npz")
    b1_shape = {"n_rows": int(B1["task_id"].shape[0]),
                "n_tasks": int(len(set(B1["task_id"].tolist()))),
                "n_probes": int(len(set(B1["probe"].tolist()))),
                "conds": sorted(set(B1["cond"].tolist())),
                "n_paras": int(len(set(B1["para"].tolist()))),
                "top_k": int(B1["top_ids"].shape[1])}
    inst, g_list, G_port = instruments_port(B1)
    from valence_core.regression import oracle as ORA   # blob-checked above
    _, G_oracle = ORA.build_instruments()
    b2b = pinned_json("data/e0/e0_b2_b2b.json")
    probes = pinned_json("data/configs/e0_probes.json")["probes"]
    G_stored = float(b2b["G"])
    J["instrument"] = {"G_port": G_port, "G_oracle_function": G_oracle, "G_stored_b2b": G_stored,
                       "g_per_probe": g_list,
                       "sigma_per_probe": [i["sigma"] for i in inst],
                       "n_val_per_probe": [(i["n_val_pos"], i["n_val_neg"]) for i in inst]}
    J["instrument"]["b1_shape"] = b1_shape
    P(f"Recomputed from `data/e0/e0_b1_markers.npz` ({b1_shape['n_rows']} natural contexts: "
      f"{b1_shape['n_tasks']} tasks x {b1_shape['n_probes']} probes x {'/'.join(b1_shape['conds'])} x "
      f"{b1_shape['n_paras']} paraphrases, top-{b1_shape['top_k']} next-token log-probs per "
      "context; no injection). Per probe q, an instrument is "
      "a unit weight vector over the 256 next-token log-probabilities whose fit-half "
      "(tasks e01-e24) post-praise minus post-criticism mean differs most; its natural gap g_q "
      "is (mean_pos - mean_neg) / pooled sd of the instrument score on the val half (tasks "
      "e25-e48). G = mean_q g_q; the V1 bar is 0.5·G, in the same σ units as every Δ "
      "(Δ_q = (mean steered score - mean unsteered score)/σ_q on the val-half contexts).")
    P("")
    P(f"- G (port, from the pinned bytes) = {G_port:.15f}; G (the oracle's own "
      f"`build_instruments()`, working tree, blob-equal) = {G_oracle:.15f}; stored in "
      f"`e0_b2_b2b.json` G = {G_stored:.15f}; all three equal: "
      f"{'yes' if G_port == G_oracle == G_stored else 'NO'}. 0.5·G = {0.5 * G_port:.6f}.")
    P("")
    P("| probe | text (first 48 chars) | val n pos/neg | σ_q | natural g_q |")
    P("|---|---|---|---|---|")
    for q, (i, g) in enumerate(zip(inst, g_list)):
        P(f"| {q} | {cell(probes[q][:48])} | {i['n_val_pos']}/{i['n_val_neg']} | "
          f"{i['sigma']:.4f} | {g:+.4f} |")
    P("")
    g_sorted = sorted(range(12), key=lambda q: -g_list[q])
    weak = [q for q in range(12) if g_list[q] <= 0.17]
    P(f"Strongest instrument: probe {g_sorted[0]} (g = {g_list[g_sorted[0]]:.3f}); probes with "
      f"g ≤ 0.17: {weak} ({len(weak)} of 12). (" +
      loc("archive/RESULTS-cycles3-4.md", "natural g = 1.157") + " says film-title g = 1.157; "
      + loc("archive/RESULTS-cycles3-4.md", "(g ≤ .17)") + " says weak instruments g ≤ .17.)")
    P("")

    # ------------------------------------------------------------------ B2b
    P("### 2c. B2b confirmatory arms (L48, frac 0.10, val half, 1,152 contexts/arm)")
    P("")
    arms = b2b["arms"]
    rows_b2b = {}
    for a in ("axis_pos", "axis_neg", "rand_pos", "rand_neg", "part_pos", "part_neg"):
        pp = arms[a]["per_probe"]
        d = statistics.fmean(pp)
        npos = sum(1 for x in pp if x > 0)
        nneg = sum(1 for x in pp if x < 0)
        rows_b2b[a] = {"delta_recomputed": d, "delta_stored": arms[a]["delta"],
                       "n_pos": npos, "n_neg": nneg,
                       "loo_drop_probe0": statistics.fmean(pp[1:]),
                       "probe0": pp[0]}
    halfG = 0.5 * G_port
    dpos, dneg = rows_b2b["axis_pos"]["delta_recomputed"], rows_b2b["axis_neg"]["delta_recomputed"]
    mrand = max(abs(rows_b2b["rand_pos"]["delta_recomputed"]),
                abs(rows_b2b["rand_neg"]["delta_recomputed"]))
    v1 = dpos >= halfG and dneg <= -halfG and min(dpos, abs(dneg)) > 2 * mrand
    v3 = (rows_b2b["part_pos"]["delta_recomputed"] >= 0.5 * dpos
          and rows_b2b["part_neg"]["delta_recomputed"] <= 0.5 * dneg)
    am_pos = max(range(12), key=lambda q: abs(arms["axis_pos"]["per_probe"][q]))
    am_neg = max(range(12), key=lambda q: abs(arms["axis_neg"]["per_probe"][q]))
    am_g = max(range(12), key=lambda q: g_list[q])
    assert am_pos == am_neg == am_g == 0, (am_pos, am_neg, am_g)
    top_shift = arms["axis_pos"]["per_probe"][0]
    top_g = g_list[0]
    pp_pos, pp_neg = arms["axis_pos"]["per_probe"], arms["axis_neg"]["per_probe"]
    rest_pos = sum(1 for x in pp_pos[1:] if x > 0)
    rest_neg = sum(1 for x in pp_neg[1:] if x < 0)
    G_loo = statistics.fmean(g_list[1:])
    J["b2b"] = {"arms": rows_b2b, "half_G": halfG, "max_abs_rand": mrand, "V1_pass": v1,
                "V1_pass_stored": b2b["criterion"]["V1_PASS"], "V3_retains": v3,
                "V3_stored": b2b.get("v3_secondary_retains"),
                "top_probe_shift_pos": top_shift, "top_probe_g": top_g,
                "top_shift_over_g": top_shift / top_g, "top_shift_over_G": top_shift / G_port,
                "signs_remaining_11": {"pos": rest_pos, "neg": rest_neg},
                "post_hoc_G_without_probe0": G_loo}
    # Round 2, finding 5: the sub-figures that are not in the record carry
    # their status where they are printed (8/11, 9/11, LOO Δ−, 2.14x, 7.9x).
    L_2x = loc("archive/RESULTS-cycles3-4.md", "exceeding its own natural gap ~2×")
    # Round 2, finding 7: FINDINGS-3's two carriers, pinned.
    L_f3_else = loc("FINDINGS-3.md", "9/12 and 10/12 elsewhere")
    L_f3_od = loc("FINDINGS-3.md", "overdose regime at 4× (all displacement reads as criticism")
    J["b2b"]["computed_new_post_hoc"] = {
        "signs_remaining_11": [rest_pos, rest_neg],
        "loo_dneg": rows_b2b["axis_neg"]["loo_drop_probe0"],
        "top_shift_over_g0": top_shift / top_g, "top_shift_over_G": top_shift / G_port,
        "record_has": f"'~2×' only ({L_2x}); 'without the top probe, Δ+ ≈ 0.085'"}
    P("Source: `data/e0/e0_b2_b2b.json` (the per-probe Δ_q are outputs of model forwards stored "
      "at 4 dp; this script recomputes every pooled figure from them). Δ = mean over the 12 "
      "probes of Δ_q.")
    P("")
    P("| arm | Δ recomputed | stored | probes > 0 | probes < 0 | Δ without probe 0 (post-hoc) |")
    P("|---|---|---|---|---|---|")
    for a, r in rows_b2b.items():
        P(f"| {a} | {r['delta_recomputed']:+.6f} | {r['delta_stored']:+.4f} | {r['n_pos']}/12 | "
          f"{r['n_neg']}/12 | {r['loo_drop_probe0']:+.4f} |")
    P("")
    # Round 2, finding 3: 2 x the unrounded 0.088358 is 0.1767; the record
    # doubles the 4-dp 0.0884 and writes 0.1768.
    mrand_st = float(b2b["criterion"]["max_abs_D_rand"])
    L_2rand = loc("archive/RESULTS-cycles3-4.md", "2×rand = 0.1768")
    two_rand_txt = (f"2·{mrand:.6f} = {2 * mrand:.4f} (record: 2×{mrand_st:.4f} = "
                    f"{2 * mrand_st:.4f}, {L_2rand})")
    J["b2b"]["two_x_rand"] = {"unrounded": 2 * mrand, "from_stored_4dp": 2 * mrand_st,
                              "record_locator": L_2rand}
    P(f"- V1 (pre-registered): Δ+ {dpos:+.4f} ≥ {halfG:.4f}; Δ− {dneg:+.4f} ≤ {-halfG:.4f}; "
      f"min(Δ+, |Δ−|) {min(dpos, abs(dneg)):.4f} > 2·max|Δ_rand| = {two_rand_txt} "
      f"-> {'PASS' if v1 else 'FAIL'} (stored V1_PASS {b2b['criterion']['V1_PASS']}).")
    P(f"- V3 secondary (sentiment-partialed axis): part_pos {rows_b2b['part_pos']['delta_recomputed']:+.4f} "
      f"≥ 0.5·Δ+ = {0.5 * dpos:+.4f}; part_neg {rows_b2b['part_neg']['delta_recomputed']:+.4f} ≤ "
      f"0.5·Δ− = {0.5 * dneg:+.4f} -> {'retains' if v3 else 'does NOT retain'} (stored "
      f"v3_secondary_retains {b2b.get('v3_secondary_retains')}).")
    P(f"- Leave-one-out: probe 0 (the film-title probe, the largest |Δ_q| in both axis arms and "
      f"the largest natural g) dropped -> Δ+ = {rows_b2b['axis_pos']['loo_drop_probe0']:+.4f}, "
      f"Δ− = {rows_b2b['axis_neg']['loo_drop_probe0']:+.4f} (LOO Δ−: {CNP}); post-hoc beside: G "
      f"over the other 11 probes = {G_loo:.4f}, half {0.5 * G_loo:.4f}; LOO Δ+ is below either bar.")
    P(f"- Sign consistency over all 12 probes: axis_pos {rows_b2b['axis_pos']['n_pos']}/12 > 0, "
      f"axis_neg {rows_b2b['axis_neg']['n_neg']}/12 < 0; over the 11 probes other than probe 0: "
      f"{rest_pos}/11 and {rest_neg}/11 ({CNP}). rand arms: {rows_b2b['rand_pos']['n_pos']}/12 and "
      f"{rows_b2b['rand_neg']['n_pos']}/12 positive.")
    P(f"- Top-probe amplification: Δ_0 = {top_shift:+.4f} σ against that instrument's own natural "
      f"gap g_0 = {top_g:.4f} -> {top_shift / top_g:.2f}x ({CNP}; the record says '~2×', "
      f"{L_2x}); against the battery mean G = {G_port:.4f} it would be {top_shift / G_port:.2f}x "
      f"({CNP}).")
    P("")

    # S2 replication
    s2 = pinned_json("data/e0/s2_neighbor_axes.json")
    s2c = {}
    for sa, ba in (("reward_pos", "axis_pos"), ("reward_neg", "axis_neg"),
                   ("rand_pos", "rand_pos"), ("rand_neg", "rand_neg")):
        x = s2["arms"][sa]["per_probe"]
        y = arms[ba]["per_probe"]
        diffs = [abs(a - b) for a, b in zip(x, y)]
        mism = [q for q, (a, b) in enumerate(zip(x, y)) if round(a, 4) != b]
        s2c[sa] = {"s2_delta": s2["arms"][sa]["delta"], "b2b_delta": arms[ba]["delta"],
                   "max_abs_diff": max(diffs), "probes_not_rounding_to_b2b": mism}
    J["s2_vs_b2b"] = s2c
    s2_first = git("log", "--format=%h %ad", "--date=short", "--diff-filter=A", PIN, "--",
                   "data/e0/s2_neighbor_axes.json").decode().strip()
    # Round 2, finding 4: S2 ran the same 4-bit MLX model; its values are
    # stored unrounded. 'Full precision' in this project means bf16.
    s2prov = s2["provenance"]
    J["s2_provenance"] = {"model_id": s2prov.get("model_id"), "dtype": s2prov.get("dtype"),
                          "backend": s2prov.get("backend")}
    P(f"S2 (a later model run; the artifact entered the record at {s2_first}; same instrument, "
      f"L48, frac 0.10, {s2['n_contexts_per_arm']} contexts per arm, {s2['n_arms']} arms, "
      "`data/e0/s2_neighbor_axes.json`) carried the reward and random arms again: a separate "
      f"re-run on the same 4-bit MLX stack (provenance model_id `{s2prov.get('model_id')}`, dtype "
      f"'{s2prov.get('dtype')}'), stored unrounded -- not a precision-robustness replication. "
      "Against B2b's 4-dp per-probe vectors:")
    for k, v in s2c.items():
        P(f"- {k}: S2 Δ {v['s2_delta']:+.6f} vs B2b {v['b2b_delta']:+.4f}; max |per-probe diff| "
          f"{v['max_abs_diff']:.2e}; probes whose S2 value does not round to B2b's 4-dp value: "
          f"{v['probes_not_rounding_to_b2b'] or 'none'}")
    rd = s2["reading"]
    adj = s2["adjudication_2026-08-21"]
    J["s2_adjudication_fields_quoted"] = {
        "corrected_reading_of_record": adj["corrected_reading_of_record"],
        "scope": adj["scope"], "queued_apparatus_note": adj["queued_apparatus_note"]}
    P(f"S2's registered reading at the same dose: reward amplitude {rd['reference_amplitude_G']:.4f} G, "
      f"strongest neighbour `{rd['strongest_neighbour']}` {rd['strongest_neighbour_amplitude_G']:.4f} G "
      f"(ratio {rd['ratio']:.4f}), branch '{rd['branch']}'. The design adjudication of 2026-08-21 "
      "in the same file (`adjudication_2026-08-21`), quoted, not paraphrased: "
      f"corrected_reading_of_record \"{adj['corrected_reading_of_record']}\"; scope "
      f"\"{adj['scope']}\"")
    P("")

    # ------------------------------------------------------------- B2a / B2c
    def grid(doc):
        out = []
        for key, a in doc["arms"].items():
            Lr, fr = key.split("_f")
            dp = statistics.fmean(a["pos"]["per_probe"])
            dn = statistics.fmean(a["neg"]["per_probe"])
            q = dp > 0 and dn < 0 and dp >= halfG
            out.append({"cell": key, "layer": int(Lr[1:]), "frac": float(fr),
                        "dpos": dp, "dneg": dn, "dpos_stored": a["pos"]["delta"],
                        "dneg_stored": a["neg"]["delta"], "qualifies_recomputed": q,
                        "qualifies_stored": a["qualifies"]})
        return out

    def select(g):
        qual = [c for c in g if c["qualifies_recomputed"]]
        if not qual:
            return None
        fmin = min(c["frac"] for c in qual)
        tied = [c for c in qual if c["frac"] == fmin]
        pick = next((c for c in tied if c["layer"] == 48), tied[0])
        return {"layer": pick["layer"], "frac": pick["frac"], "tied_layers": [c["layer"] for c in tied]}

    b2a = pinned_json("data/e0/e0_b2_b2a.json")
    ga, gc = grid(b2a), grid(b2c)
    sel_a, sel_c = select(ga), select(gc)
    J["b2a"] = {"grid": ga, "selected_recomputed": sel_a, "selected_stored": b2a["selected_dose"]}
    J["b2c_a"] = {"grid": gc, "selected_recomputed": sel_c, "selected_stored": b2c["selected_dose"]}
    P("### 2d. B2a dose-finding (span axis) and B2c-a (last-position variant), fit half, 192 contexts/arm")
    P("")
    P("Dose rule as pre-registered (" + loc("archive/RESULTS-cycles3-4.md", "Dose rule identical to B2a (smallest") +
      "): a cell qualifies iff Δ+ > 0, Δ− < 0 and Δ+ ≥ 0.5·G; the smallest qualifying frac is "
      "selected, ties to L48.")
    P("")
    P("Δ± are recomputed as the mean of the stored 4-dp per-probe values; the stored Δ was "
      "computed from unrounded values, so agreement is to within 1e-4 (the mean of 4-dp-rounded "
      "values can move the 4th decimal).")
    P("")
    P("| variant | cell | Δ+ recomputed | Δ+ stored | Δ− recomputed | Δ− stored | max abs diff ≤ 1e-4 | qualifies (recomputed / stored) |")
    P("|---|---|---|---|---|---|---|---|")
    for name, g in (("span (B2a)", ga), ("last (B2c-a)", gc)):
        for c in g:
            dmax = max(abs(c["dpos"] - c["dpos_stored"]), abs(c["dneg"] - c["dneg_stored"]))
            c["max_abs_diff_vs_stored"] = dmax
            P(f"| {name} | {c['cell']} | {c['dpos']:+.5f} | {c['dpos_stored']:+.4f} | "
              f"{c['dneg']:+.5f} | {c['dneg_stored']:+.4f} | {'yes' if dmax <= 1e-4 else 'NO'} "
              f"({dmax:.1e}) | {c['qualifies_recomputed']} / {c['qualifies_stored']} |")
    P("")
    P(f"- B2a selection recomputed: {sel_a} (stored {b2a['selected_dose']}).")
    P(f"- B2c-a selection recomputed: {sel_c} (stored {b2c['selected_dose']}).")
    wrong = {L_: all(c["dpos"] < 0 for c in gc if c["layer"] == L_) for L_ in (44, 48, 52)}
    l52 = max(c["dpos"] for c in gc if c["layer"] == 52)
    l52_signs = all(c["dpos"] > 0 and c["dneg"] < 0 for c in gc if c["layer"] == 52)
    J["b2c_a"]["dpos_negative_at_every_frac"] = {str(k): v for k, v in wrong.items()}
    J["b2c_a"]["L52_max_dpos"] = l52
    P(f"- B2c-a Δ+ < 0 at every frac: L44 {wrong[44]}, L48 {wrong[48]}, L52 {wrong[52]}; at L52 both "
      f"signs correct at every frac: {l52_signs}; L52 max Δ+ = {l52:+.4f} vs bar {halfG:.4f}.")
    od = [c for c in ga if c["frac"] == 0.4]
    P("- Overdose cells (frac 0.40, span axis): " + "; ".join(
        f"L{c['layer']} Δ+ {c['dpos']:+.4f} / Δ− {c['dneg']:+.4f}" for c in od) +
      ". Δ+ turns negative (both poles read as post-criticism) at L44 only; at L48 Δ+ plateaus "
      "(+0.4076 at 0.20 -> +0.3999 at 0.40) and at L52 it still rises; Δ− balloons at all three.")
    P("")

    # ------------------------------------------------------------------ e2d
    P("### 2e. e2d (dose escalation at session scale, Qwen, L48, f = 0.10 / 0.20 / 0.30)")
    P("")
    vraw = "results/raw/2026-09-05_e2d_closure_verify.txt"
    P("Read, not run: `scripts/e2d_closure_verify3.py` (it prints and runs read-only `git grep`; "
      "it checks the third-pass figures R7-R15, none of which is .574/.613/.534 or the audit "
      "trio). The record's own check of these four figures is the earlier, frozen "
      "`scripts/e2d_closure_verify.py` (read, not run): " +
      loc("scripts/e2d_closure_verify.py", 'chk("R4 rates audit .000/.023/.047"') + ", " +
      loc("scripts/e2d_closure_verify.py", 'for t, med, p10 in (("d2", .574, .524)') + ", " +
      loc("scripts/e2d_closure_verify.py", 'chk("D2 AUC_R .534"') + "; its committed raw shows them "
      "PASS at " + loc(vraw, "R4 rates audit .000/.023/.047") + ", " +
      loc(vraw, "d2 readability median 0.574") + ", " + loc(vraw, "d3 readability median 0.613") +
      ", " + loc(vraw, "D2 AUC_R .534") + ". This script recomputes them independently. The "
      "definitions used below are the producing code's: `MRK.audit_rates` "
      "(valence_core/e2d/marks.py, called by scripts/e2d_score.py over ALL sessions of the tier, "
      "excluded included) and `resampled_auc` / `gate` (valence_core/e2d/readability.py).")
    P("")
    sess = {t: pinned_json(f"data/e2d/{t}_sessions.json")["sessions"] for t in ("d1", "d2", "d3")}
    scores = {t: pinned_json(f"data/e2d/{t}_scores.json") for t in ("d2", "d3")}
    d1doc = pinned_json("data/e2d/d1_sessions.json")
    dose = {"d1": 0.10, "d2": 0.20, "d3": 0.30}

    def audit_counts(ss, arm):
        k = n = 0
        for s in ss:
            if s["arm"] != arm:
                continue
            for r in list(s["rounds"]) + list(s["choices"]):
                k += int(bool(r["degen"]))
                n += 1
        return k, n

    def stored_arm(sc, arm):
        t = sc["audit_rates_by_round_class"]
        cls = {"M": ("+axis", "sham(M)"), "R": ("random", "sham(R)"), "S": ("sham(S)",)}[arm]
        k = sum(t[c][kd]["degenerate"] for c in cls if c in t for kd in t[c])
        n = sum(t[c][kd]["rounds"] for c in cls if c in t for kd in t[c])
        return k, n

    aud = {}
    for t in ("d1", "d2", "d3"):
        for arm in ("M", "R", "S"):
            k, n = audit_counts(sess[t], arm)
            if n == 0:
                continue
            st = stored_arm(scores[t], arm) if t in scores else None
            aud[f"{t}|{arm}"] = {"k": k, "n": n, "rate": k / n, "stored": st}
    J["e2d_audit"] = aud
    tiers_meta = {}
    for t in ("d1", "d2", "d3"):
        d = pinned_json(f"data/e2d/{t}_sessions.json")
        tiers_meta[t] = {"audit_of_record": d.get("audit_of_record"), "frac": d.get("frac"),
                         "layer": d.get("layer"), "n_sessions": len(d["sessions"])}
    J["e2d_tiers"] = tiers_meta
    P("Tier metadata as stored in the sessions files: " + "; ".join(
        f"{t}: layer {m['layer']}, frac {m['frac']}, {m['n_sessions']} sessions, audit_of_record "
        f"{m['audit_of_record']['file']} sha16 {m['audit_of_record']['sha16']}"
        for t, m in tiers_meta.items()) + ".")
    P("")
    P("Audit-degenerate rounds (that audit, as stored per round in the `degen` field), every "
      "round (forced + free, steered + unsteered) of every session of the arm, excluded sessions "
      "included:")
    P("")
    P("| tier (dose) | arm | degenerate / rounds | rate | stored table (audit_rates_by_round_class) |")
    P("|---|---|---|---|---|")
    for key, v in aud.items():
        t, arm = key.split("|")
        st = v["stored"]
        P(f"| {t} ({dose[t]:.2f}) | {arm} | {v['k']}/{v['n']} | {v['rate']:.4f} | "
          f"{('%d/%d' % st) if st else 'none stored (D1 scored no table; counters.audit_degenerate total ' + str(d1doc['counters']['counters']['audit_degenerate']['total']) + ')'} |")
    P("")
    rm = {}
    for t in ("d2", "d3"):
        rb = scores[t]["read_mark_rates"]["rates_by_arm"]
        k = sum(rb[kd]["M"]["marked"] for kd in rb)
        n = sum(rb[kd]["M"]["rounds"] for kd in rb)
        rm[t] = (k, n)
    J["e2d_readmarks_M_stored"] = {t: list(v) for t, v in rm.items()}
    # Values-check findings 2 and 9: D1 HAS a marks file (it marks arm S only);
    # recount every tier from its marks file with marks.tabulate's domain
    # (ALL rounds, forced + free, of ALL sessions of the arm, excluded included).
    rm_re, mk_meta = {}, {}
    for t in ("d1", "d2", "d3"):
        mdoc = pinned_json(f"data/e2d/{t}_read_marks.json")
        mset = {f"{m['arm']}|{m['session']}|{m['phase']}" for m in mdoc["marks"]}
        k = n = 0
        for s in sess[t]:
            if s["arm"] != "M":
                continue
            for r in list(s["rounds"]) + list(s["choices"]):
                n += 1
                k += int(f"M|{s['session']}|{r['phase']}" in mset)
        rm_re[t] = (k, n)
        arms_marked = {}
        for m in mdoc["marks"]:
            arms_marked[m["arm"]] = arms_marked.get(m["arm"], 0) + 1
        mk_meta[t] = {"n_marks": len(mdoc["marks"]), "marks_by_arm": arms_marked,
                      "provisional": mdoc.get("provisional"), "tier": mdoc.get("tier")}
    d1_marks_first = git("log", "--format=%h %ad", "--date=short", "--diff-filter=A", PIN, "--",
                         "data/e2d/d1_read_marks.json").decode().strip()
    rm_equal = all(rm_re[t] == rm[t] for t in ("d2", "d3"))
    J["e2d_readmarks_M_recount"] = {"recount": {t: list(v) for t, v in rm_re.items()},
                                     "stored_d2_d3_equal": rm_equal, "marks_files": mk_meta,
                                     "d1_marks_file_entered": d1_marks_first}
    rm = rm_re
    J["e2d_readmarks_M"] = rm
    P("Read-marked rounds, M arm (provisional reader). Domain: every round (forced + free, "
      "steered + unsteered) of every M-arm session of the tier, excluded sessions included "
      "(`marks.tabulate`'s domain, rule 23). Recounted here from each tier's marks file "
      "(`data/e2d/{d1,d2,d3}_read_marks.json`) against the sessions: " +
      ", ".join(f"{t} {k}/{n} = {k / n:.4f}" for t, (k, n) in sorted(rm.items())) +
      f"; equal to the stored `read_mark_rates` at D2 and D3: {'yes' if rm_equal else 'NO'}. "
      f"D1's marks file (entered at {d1_marks_first}) holds {mk_meta['d1']['n_marks']} marks, by "
      f"arm {mk_meta['d1']['marks_by_arm']}: it marks no M round, so M is "
      f"{rm['d1'][0]}/{rm['d1'][1]}.")
    steps = {}
    for lab, (a, b) in {"audit .10->.20": (aud["d1|M"], aud["d2|M"]),
                        "audit .20->.30": (aud["d2|M"], aud["d3|M"])}.items():
        steps[lab] = fisher(b["k"], b["n"] - b["k"], a["k"], a["n"] - a["k"])
    for lab, (a, b) in {"read .10->.20": (rm["d1"], rm["d2"]),
                        "read .20->.30": (rm["d2"], rm["d3"])}.items():
        steps[lab] = fisher(b[0], b[1] - b[0], a[0], a[1] - a[0])
    r_vs_m = fisher(aud["d2|R"]["k"], aud["d2|R"]["n"] - aud["d2|R"]["k"],
                    aud["d2|M"]["k"], aud["d2|M"]["n"] - aud["d2|M"]["k"])
    J["e2d_steps_fisher"] = steps
    J["e2d_R_vs_M_d2"] = r_vs_m
    # Values-check finding 3: these p values are record figures; state where.
    L_close = loc_range("RESULTS.md", "resolved step (read .10→.20, Fisher exact two-sided p = .021",
                        ".20; both ≥ .10 one-sided")
    L_vc = loc_range("RESULTS.md", "read .10→.20 **p = .011**; audit .10→.20 p = .41",
                     "p = .10, read .20→.30 p = .10.")
    L_rm = loc("RESULTS.md", "carries no axis (R > M one-sided p = .16")
    L_rm4 = loc("results/raw/2026-09-04_e2d_closure_valuescheck.txt",
                f"R > M one-sided Fisher p = {r_vs_m['one_sided_greater']:.4f}")
    # Round 2, finding 1: the record's R4 Fisher table prints all eight dose-step
    # p values at 4 dp (results/raw/2026-09-05_e2d_closure_verify.txt), including
    # audit .10->.20 two-sided 1.0000 (also its PASS line). Parse that table and
    # require equality at 4 dp with the values computed here.
    vtxt = pinned_text(vraw).split("\n")
    r4h = next(i for i, l in enumerate(vtxt) if "FISHER TABLE OF RECORD" in l)
    r4c = next(i for i in range(r4h, r4h + 6)
               if vtxt[i].strip().startswith("step") and "two-sided" in vtxt[i])
    assert vtxt[r4c].index("two-sided") < vtxt[r4c].index("one-sided"), vtxt[r4c]
    r4 = {}
    for i in range(r4c + 1, r4c + 5):
        m4 = re.match(r"^\s+(audit|read)\s+(\.\d\d->\.\d\d)\s+(\d\.\d{4})\s+(\d\.\d{4})\s*$", vtxt[i])
        assert m4, vtxt[i]
        r4[f"{m4.group(1)} {m4.group(2)}"] = {"line": i + 1, "two_sided": m4.group(3),
                                              "one_sided": m4.group(4)}
    assert sorted(r4) == sorted(steps), (sorted(r4), sorted(steps))
    r4_vals = [(lab, t, r4[lab][t] == f"{steps[lab][k]:.4f}")
               for lab in steps for t, k in (("two_sided", "two_sided"),
                                             ("one_sided", "one_sided_greater"))]
    r4_eq = {lab: all(ok for l_, _, ok in r4_vals if l_ == lab) for lab in steps}
    assert all(ok for _, _, ok in r4_vals), r4_vals
    L_r4 = f"{vraw}@{PIN}:{r4c + 2}-{r4c + 5}"
    L_r4pass = loc(vraw, "R4 audit .10->.20 two-sided (unresolved)")

    def l4(lab):
        return f"{vraw}@{PIN}:{r4[lab]['line']}"

    rec2dp = {  # (one-sided, two-sided) as RESULTS.md rounds them; None = not in RESULTS.md
        "audit .10->.20": (".41 [" + L_vc + "]", None),
        "audit .20->.30": (".10 [" + L_vc + "]", ".15 [" + L_close + "]"),
        "read .10->.20": (".011 [" + L_close + "; " + L_vc + "]", ".021 [" + L_close + "]"),
        "read .20->.30": (".10 [" + L_vc + "]", ".20 [" + L_close + "]"),
    }
    record_p = {}
    for lab, (o2, t2) in rec2dp.items():
        o4 = f"{r4[lab]['one_sided']} [{l4(lab)}]"
        t4 = f"{r4[lab]['two_sided']} [{l4(lab)}" + (
            f"; PASS line {L_r4pass}]" if lab == "audit .10->.20" else "]")
        record_p[lab] = (f"{o2}; 4 dp {o4}", (f"{t2}; 4 dp {t4}" if t2 else f"4 dp {t4}"))
    J["e2d_steps_record_locators"] = {"closure_text": L_close, "values_check": L_vc,
                                       "r_vs_m": L_rm, "per_step": record_p,
                                       "fisher_table_4dp": {"rows": L_r4, "per_step": r4,
                                                            "equal_to_computed_at_4dp": r4_eq,
                                                            "audit_10_20_two_sided_pass_line": L_r4pass}}
    P("")
    P("Dose steps, M arm, same domain as the rates above (all rounds of all sessions, excluded "
      "included). Test: Fisher exact on [[higher-dose flagged, unflagged], [lower-dose flagged, "
      "unflagged]]; one-sided = excess at the higher dose; two-sided = sum of the probabilities of "
      "tables no more probable than the observed. These p values are RECORD figures, reproduced "
      "here (the record's rounded value and locator beside each); a p the record does not carry "
      "is marked computed-new:")
    for lab, f in steps.items():
        r1, r2 = record_p[lab]
        P(f"- {lab}: one-sided p = {f['one_sided_greater']:.4f} (record {r1}: reproduced), "
          f"two-sided p = {f['two_sided']:.4f} " +
          (f"(record {r2}: reproduced)" if r2 else "(not in the record: computed-new)"))
    P(f"- D2 (0.20), R arm vs M arm, audit: {aud['d2|R']['k']}/{aud['d2|R']['n']} = "
      f"{aud['d2|R']['rate']:.4f} vs {aud['d2|M']['k']}/{aud['d2|M']['n']} = {aud['d2|M']['rate']:.4f}; "
      f"one-sided (R > M) Fisher exact p = {r_vs_m['one_sided_greater']:.4f} (record .16 [{L_rm}]; "
      f"4 dp {r_vs_m['one_sided_greater']:.4f} [{L_rm4}]: reproduced); two-sided p = {r_vs_m['two_sided']:.4f} (not in the record: computed-new); "
      f"S arm {aud['d2|S']['k']}/{aud['d2|S']['n']}.")
    P("")

    rdb = {}
    for t, sc in (("d1", d1doc), ("d2", scores["d2"]), ("d3", scores["d3"])):
        R = sc["readability"]
        sets = ({"k2_resampled (D1, n = 4 M sessions)": R["k2_resampled"]} if t == "d1" else
                {"v2_and_read_clean k2 (set of record)": R["v2_and_read_clean"]["k2"],
                 "v2_clean_only k2": R["v2_clean_only"]["k2"],
                 "all_rounds k2": R["all_rounds_degeneracy_included"]})
        if t == "d2":
            sets["AUC_R k2 (arm R, displacement comparator)"] = R["AUC_R"]
        for name, s in sets.items():
            au = [a for a in s["aucs"] if a is not None]
            med_np, p10_np = float(np.median(au)), float(np.percentile(au, 10))
            med_sl, p10_sl = statistics.median(au), pct_linear(au, 10)
            rdb[f"{t}|{name}"] = {
                "n_resamples": len(s["aucs"]), "n_evaluable": len(au),
                "median": med_np, "p10": p10_np, "median_stdlib": med_sl, "p10_stdlib": p10_sl,
                "stored_median": s["median"], "stored_p10": s["p10"],
                "equal_to_stored": (abs(med_np - s["median"]) < 1e-12
                                    and abs(p10_np - s["p10"]) < 1e-12),
                "n_pos": s.get("n_pos"), "n_neg": s.get("n_neg"),
                "gate_passes": med_np >= 0.70 and p10_np >= 0.60}
    # the clean-round domain, recomputed from the sessions + marks (port of clean_rounds)
    def marked_keys(t):
        mk = pinned_json(f"data/e2d/{t}_read_marks.json")   # d1 has one too (arm S only)
        return {f"{m['arm']}|{m['session']}|{m['phase']}" for m in mk["marks"]}

    def clean_counts(ss, arm, marked):
        pos = neg = 0
        for s in ss:
            if s["arm"] != arm:
                continue
            for r in list(s["rounds"]) + list(s["choices"]):
                if r["degen"] or r.get("lexical") or not r["text"].strip():
                    continue
                if marked is not None and f"{arm}|{s['session']}|{r['phase']}" in marked:
                    continue
                if r["steered"]:
                    pos += 1
                else:
                    neg += 1
        return pos, neg

    dom = {}
    for t in ("d2", "d3"):
        mk = marked_keys(t)
        dom[f"{t}|M|v2+read"] = clean_counts(sess[t], "M", mk)
        dom[f"{t}|M|v2"] = clean_counts(sess[t], "M", None)
    dom["d2|R|v2+read"] = clean_counts(sess["d2"], "R", marked_keys("d2"))
    dom["d1|M|v2"] = clean_counts(sess["d1"], "M", None)
    J["e2d_readability"] = rdb
    J["e2d_clean_domain_counts"] = {k: list(v) for k, v in dom.items()}
    P("Readability (Q2): probe = logistic regression (`discrim.logistic_auc`: standardize on the "
      "fit half, full-batch GD, seed 7, 300 iterations, lr 0.1, l2 0.01) on the model's embedding "
      "of a record (mean over positions of the post-norm final residual, Qwen3.6-27B 4-bit); "
      "record = k = 2 audit-clean rounds concatenated; contrast = rounds generated with the state "
      "live (+axis, L48, frac = the tier's dose) vs unsteered rounds of the same arm; CV = "
      "task-disjoint fit/val halves, B = 20 resamples; figure = median over resamples (gate: "
      "median ≥ .70 AND 10th percentile ≥ .60). The 20 per-resample AUCs are model outputs stored "
      "in the artifact; this script recomputes the median and 10th percentile from them (numpy "
      "and a stdlib linear percentile) and the clean-round counts from the sessions.")
    P("")
    P("| tier | set | evaluable | median | p10 | stdlib median / p10 | equals stored | n_pos/n_neg stored | gate |")
    P("|---|---|---|---|---|---|---|---|---|")
    for key, v in rdb.items():
        t, name = key.split("|", 1)
        P(f"| {t} ({dose[t]:.2f}) | {name} | {v['n_evaluable']}/{v['n_resamples']} | {v['median']:.4f} | "
          f"{v['p10']:.4f} | {v['median_stdlib']:.4f} / {v['p10_stdlib']:.4f} | "
          f"{'yes' if v['equal_to_stored'] else 'NO'} | {v['n_pos']}/{v['n_neg']} | "
          f"{'pass' if v['gate_passes'] else 'fail'} |")
    P("")
    P("Clean-round counts recomputed from the sessions (pos = state-live rounds, neg = unsteered): "
      + "; ".join(f"{k} {v[0]}/{v[1]}" for k, v in dom.items()) +
      ". D3 has no R arm (M-only under ADDENDUM-j1), hence no comparator at 0.30.")
    P("")
    # Values-check finding 4: the task-disjointness caveat at D3.
    cov = {}
    for t in ("d2", "d3"):
        c = pinned_json(f"data/e2d/{t}_sessions.json")["task_id_coverage"]
        cov[t] = {"arm": c.get("arm"), "n_sessions": c.get("n_sessions"),
                  "distinct_pos": c["distinct_task_ids"]["pos"],
                  "distinct_neg": c["distinct_task_ids"]["neg"], "floor": c.get("floor"),
                  "meets_floor": c.get("meets_floor"), "below_d2_floor": c.get("below_d2_floor")}
    L_d3cav = loc_range("RESULTS.md", "D3's readability lacks D2's", "task-disjointness guarantee.")
    L_d3cov = loc_range("RESULTS.md", "**Coverage shortfall, recorded in the artifact.**",
                        "guarantee.**")
    L_d3entry = loc("RESULTS.md", "**e2d D3 — all 24 sessions RAN")
    J["e2d_task_id_coverage"] = {"per_tier": cov, "closure_caveat": L_d3cav,
                                 "coverage_bullet": L_d3cov, "d3_run_entry": L_d3entry}
    P("Task-disjointness of the readability CV, from each tier's `task_id_coverage` (M arm): "
      + "; ".join(f"{t}: distinct task ids pos {v['distinct_pos']} / neg {v['distinct_neg']} "
                  f"against floor {v['floor']}, meets_floor {v['meets_floor']}"
                  + (f", below_d2_floor {v['below_d2_floor']}" if v['below_d2_floor'] is not None else "")
                  for t, v in cov.items()) +
      ". The floor is a D2 precondition; D3 (0.30, n = 24 sessions) cannot reach it, and the "
      f"record says so: the closure text \"D3's readability lacks D2's task-disjointness "
      f"guarantee\" ({L_d3cav}); the D3 run entry ({L_d3entry}) gives the coverage shortfall and "
      f"why it is unreachable at n = 24 ({L_d3cov}). So the .613 at 0.30 carries that caveat; the .574 at 0.20 does not.")
    P("")
    # the closure text of record (design-authored blockquote), read at the pin
    rtxt = pinned_text("RESULTS.md").split("\n")
    anchor = "**e2d CLOSURE — TEXT OF RECORD (values-checked)."
    st = next(i for i, l in enumerate(rtxt) if l.startswith("- ") and anchor in l)
    en = next((i for i in range(st + 1, len(rtxt)) if rtxt[i].startswith("- 20")), len(rtxt))
    qidx = [i for i in range(st, en) if rtxt[i].startswith("  > ")]
    quoted = " ".join(rtxt[i][4:] for i in qidx)
    ctext = {
        "has '.574 / .524 at 0.20 and .613 / .526 at 0.30'": ".574 / .524 at 0.20 and .613 / .526 at 0.30" in quoted,
        "has 'displacement comparator at .534'": "displacement comparator at .534" in quoted,
        "has '(audit .000 / .023 / .047'": "(audit .000 / .023 / .047" in quoted,
        "has 'ordered across three doses'": "ordered across three doses" in quoted,
        "has 'single resolved step'": "single resolved step" in quoted,
        "has 'not axis-specific'": "not axis-specific" in quoted,
        "has 'monotonic' (any form)": "monotonic" in quoted,
        "has 'quarter'": "quarter" in quoted,
    }
    q_in_closure = ctext["has 'quarter'"]
    mk_d2 = scores["d2"]["marker"]["primary_paired_within_M"]["delta"]
    v1_l48_f02 = statistics.fmean(b2a["arms"]["L48_f0.2"]["pos"]["per_probe"])
    J["e2d_closure_text_checks"] = {"entry": f"RESULTS.md@{PIN}:{st + 1}-{en}",
                                    "blockquote": f"RESULTS.md@{PIN}:{qidx[0] + 1}-{qidx[-1] + 1}",
                                    **ctext}
    J["e2d_marker_quarter"] = {"d2_excised_primary_delta": mk_d2,
                               "b2a_L48_f0.2_dpos": v1_l48_f02, "ratio": mk_d2 / v1_l48_f02}
    P(f"The closure text of record (the design-authored blockquote, RESULTS.md@{PIN}:"
      f"{qidx[0] + 1}-{qidx[-1] + 1}, of the entry at RESULTS.md@{PIN}:{st + 1}), string checks "
      "(the same unwrapping as scripts/e2d_closure_verify3.py's quoted_text): " +
      "; ".join(f"{k}: {v}" for k, v in ctext.items()) + ".")
    P(f"Beside (preprint's 'about a quarter of its short-context value'): D2 primary within-M "
      f"paired marker Δ+ (excised context) {mk_d2:+.4f} / B2a L48 f 0.20 Δ+ {v1_l48_f02:+.4f} "
      f"(recomputed from per-probe) = {mk_d2 / v1_l48_f02:.4f}; arithmetic holds, channels differ "
      "(see note 7).")
    P("")

    # ===================================================== suite mapping
    names = [c["name"] for c in wt["checks"]]

    def suite(pat):
        rx = re.compile(pat)
        return [c for c in wt["checks"] if rx.search(c["name"])]

    def fmt_checks(cs):
        return "; ".join(f"'{c['name']}' expected {c['expected']} got {c['got']} [{c['status']}]"
                         for c in cs) or "none"

    m_sent = suite(r"^L\d\d cos reward\.sentiment$")
    m_char = suite(r"^L\d\d cos reward\.character$")
    m_v2 = suite(r"^L\d\d V2 self-residual$")
    m_s2guard = suite(r"neighbour axes are the published guards")
    m_bar = suite(r"bar 0\.5\*G")
    m_v1fix = suite(r"V1 rule applied unchanged|weaker neighbour can still clear V1|sub-0\.5G neighbour fails V1")
    m_sha = suite(r"^e0 axes sha$|^e0 random-dirs sha$|^workspace layers$")
    m_c1r3 = suite(r"^c1r3 ")
    m_dose = suite(r"dose is frac x R_layer|every axis carries one dose")
    m_e2d = suite(r"^e2d Q2|^e2d Q1|^e2d run-dose")
    m_v3 = suite(r"^L\d\d V3 eval-residual$")
    J["suite_mapping"] = {
        "sentiment_cos": [c["name"] for c in m_sent], "character_cos": [c["name"] for c in m_char],
        "self_residual": [c["name"] for c in m_v2], "s2_guard": [c["name"] for c in m_s2guard],
        "bar_constant": [c["name"] for c in m_bar], "v1_fixture": [c["name"] for c in m_v1fix],
        "frozen_shas": [c["name"] for c in m_sha], "c1r3": [c["name"] for c in m_c1r3],
        "dose": [c["name"] for c in m_dose], "e2d_criteria": [c["name"] for c in m_e2d],
        "v3_eval_residual": [c["name"] for c in m_v3]}

    P("## 3. Which link-2 figures the suite holds")
    P("")
    P(f"Of the {len(names)} checks printed, the ones that bear on link 2 (names as printed, run (a); "
      "run (b) printed the same):")
    P("")
    P(f"- Frozen artifacts every dose was computed from: {fmt_checks(m_sha)}.")
    P(f"- Axis geometry (24 checks, e0_axes.meta.json report, span variant only): sentiment cosines "
      f"{fmt_checks(m_sent)}.")
    P(f"- character cosines: {fmt_checks(m_char)}.")
    P(f"- V2 self-residual: {fmt_checks(m_v2)}.")
    P(f"- V3 eval-residual (not a note figure; same family): {fmt_checks(m_v3)}.")
    P(f"- S2 guard identity at L48: {fmt_checks(m_s2guard)}.")
    P(f"- Dose arithmetic (frac x R_l, equal norm): {fmt_checks(m_dose)}.")
    P(f"- The 0.1578 bar appears only as a pinned constant of the e2d analyzer: {fmt_checks(m_bar)}; "
      f"and as V1-rule fixtures with G hard-coded to 0.3156 and synthetic arms: {fmt_checks(m_v1fix)}. "
      "No analysis-tier check derives G or the bar from the B1 instrument; the oracle tier does "
      "(build_instruments, model-free, asserted |G − 0.3156| ≤ 1e-3), and section 2b runs it.")
    P(f"- e2d criteria (pre-registration constants and branch logic, not the e2d figures): {fmt_checks(m_e2d)}.")
    P(f"- c1r3 gate (`data/configs/c1r3_gate_rep{{A,B}}.json`, a block referent): {fmt_checks(m_c1r3)}. "
      "These hold FINDINGS-2 finding 3 (the cycle-2 matched-pair association test), not a link-2 "
      "figure.")
    P("")
    P("Not in the analysis tier: Δ+, Δ−, max|Δ_rand|, LOO Δ+, 9/12 and 10/12, G, ‖d‖/R, every "
      "last-position (purity) figure, the B2a/B2c-a grids, and the e2d readability, comparator and "
      "audit-rate figures. Δ± and the V1 verdict are oracle-tier criterion (ii) (section 1b).")
    P("")

    # ====================================================== figures table
    P("## Figures (as the block writes them)")
    P("")
    P("| figure | value printed | source | status | note |")
    P("|---|---|---|---|---|")
    F = []

    def row(fig, val, src, status, note=""):
        F.append({"figure": fig, "value": val, "source": src, "status": status, "note": note})
        P(f"| {cell(fig)} | {cell(val)} | {cell(src)} | {status} | {cell(note)} |")

    row("regression suite 103/103 (block :107)",
        f"{summ(pn)} at {PIN} (git-archive tree); {summ(wt)} on the working tree at {head0[:7]}",
        "python -B -m valence_core.regression.analysis (stdout)", "discrepant",
        "stale count, not transcription: 103 was the count after the S2 build "
        f"({loc('RESULTS.md', 'Suite 83 → 103')}); README.md@{PIN} still says 103; 0 FAIL")
    row("Δ+ = +0.285", f"{dpos:+.6f} (stored +0.2848)",
        "data/e0/e0_b2_b2b.json arms.axis_pos.per_probe (mean of 12)", "reproduced",
        "per-probe Δ_q are stored model outputs; S2's separate re-run on the same 4-bit MLX stack, "
        "stored unrounded (same axis, dose, instrument), gives "
        f"{s2c['reward_pos']['s2_delta']:+.6f}; oracle exact re-run is log-only (section 1b); not an analysis-tier check")
    row("Δ− = −0.395", f"{dneg:+.6f} (stored −0.3946)",
        "data/e0/e0_b2_b2b.json arms.axis_neg.per_probe", "reproduced",
        f"S2 run {s2c['reward_neg']['s2_delta']:+.6f}; not an analysis-tier check")
    row("bars ±0.158", f"0.5·G = {halfG:.6f}",
        "data/e0/e0_b1_markers.npz -> G (instrument rebuild); e0_b2_b2b.json criterion.half_G 0.1578",
        "reproduced", "analysis tier holds 0.1578 only as a pinned constant ('e2d Q3: bar 0.5*G = 0.1578...')")
    rp4, rn4 = arms["rand_pos"]["delta"], arms["rand_neg"]["delta"]
    s2rp, s2rn = s2["arms"]["rand_pos"]["delta"], s2["arms"]["rand_neg"]["delta"]
    J["rand_asymmetry_ratio"] = {"b2b_stored_4dp": abs(rn4) / abs(rp4),
                                 "b2b_recomputed_means": mrand / abs(rows_b2b['rand_pos']['delta_recomputed']),
                                 "s2_unrounded": abs(s2rn) / abs(s2rp)}
    row("random ≤ 0.088", f"max(|{rows_b2b['rand_pos']['delta_recomputed']:+.4f}|, "
        f"|{rows_b2b['rand_neg']['delta_recomputed']:+.4f}|) = {mrand:.4f} (rand_neg)",
        "data/e0/e0_b2_b2b.json arms.rand_{pos,neg}.per_probe", "reproduced",
        "norm-matched random direction (frozen sha b6bd2f5f580ee13e), same dose; 2x = "
        f"{two_rand_txt}. The record names the |rand−|/|rand+| asymmetry in S2's adjudication "
        f"(s2_neighbor_axes.json adjudication_2026-08-21.queued_apparatus_note, quoted: "
        f"\"{adj['queued_apparatus_note']}\"); ratio recomputed: {abs(rn4) / abs(rp4):.3f} from "
        f"B2b's stored 4-dp Δs, {mrand / abs(rows_b2b['rand_pos']['delta_recomputed']):.3f} from "
        f"the per-probe means, {abs(s2rn) / abs(s2rp):.3f} from S2's unrounded arms")
    row("LOO Δ+ = 0.085", f"{rows_b2b['axis_pos']['loo_drop_probe0']:+.4f} (probe 0 dropped)",
        "data/e0/e0_b2_b2b.json axis_pos.per_probe[1:]", "reproduced",
        f"probe 0 = film-title probe, top by |Δ_q| and by natural g; LOO Δ− = "
        f"{rows_b2b['axis_neg']['loo_drop_probe0']:+.4f} ({CNP}; the record carries LOO Δ+ only). "
        f"Provenance: a descriptive honesty note in "
        f"the B2b verdict entry ({loc('archive/RESULTS-cycles3-4.md', 'probe, Δ+ ≈ 0.085')}); LOO was "
        f"made a REQUIRED descriptive report only in the later B2c pre-registration "
        f"({loc('archive/RESULTS-cycles3-4.md', 'pooled Δ± with leave-one-out on the')}), for B2c-b, "
        f"which never ran -- so for B2b it is descriptive, not pre-declared")
    row("9/12 and 10/12", f"axis_pos {rows_b2b['axis_pos']['n_pos']}/12 > 0; axis_neg "
        f"{rows_b2b['axis_neg']['n_neg']}/12 < 0 (over the other 11: {rest_pos}/11, {rest_neg}/11 -- "
        f"{CNP})",
        "data/e0/e0_b2_b2b.json per_probe signs", "reproduced",
        "counts are over ALL 12 probes (record: " + loc("archive/RESULTS-cycles3-4.md", "axis_pos sign-consistent") +
        "); the preprint's 'on the remaining probes' (" + loc(PREPRINT, "on the remaining probes", True) +
        f") would be {rest_pos}/11 and {rest_neg}/11 -- a wording slip; FINDINGS-3's '9/12 and 10/12 "
        f"elsewhere' ({L_f3_else}) has the same ambiguity")
    row("G = 0.316", f"{G_port:.6f}", "data/e0/e0_b1_markers.npz (port + oracle.build_instruments); "
        "e0_b2_b2b.json G", "reproduced",
        f"G is the 12-probe MEAN natural gap. The preprint's 'exceeds the natural praise–criticism gap "
        f"on that instrument (G = 0.316) by roughly two-fold' names the wrong referent: that "
        f"instrument's own gap is g_0 = {top_g:.3f}, and {top_shift:.3f}/{top_g:.3f} = "
        f"{top_shift / top_g:.2f}x ({CNP}; the record says '~2×', {L_2x}; 'roughly two-fold' "
        f"holds); against G it is {top_shift / G_port:.1f}x ({CNP})")
    # Values-check finding 1: the upper end .88 exists only via the meta
    # report's 3-dp value; unrounded, the npz rounds to .87. (Round 2: "unrounded",
    # not "full precision" -- the vectors come from the 4-bit model; the term means bf16 here.)
    meta_last_v2 = {r["layer"]: r["v2_self_residual_frac"] for r in meta["report"]["last"]}
    lv2_argmax = max(la, key=lambda r: r["v2_self_resid"])
    lv2_argmin = min(la, key=lambda r: r["v2_self_resid"])
    full_2dp = (f"{lv2_argmin['v2_self_resid']:.2f}", f"{lv2_argmax['v2_self_resid']:.2f}")
    meta_2dp = (f"{min(meta_last_v2.values()):.2f}", f"{max(meta_last_v2.values()):.2f}")
    J["purity_v2_precision"] = {
        "unrounded_range": [lv2_argmin["v2_self_resid"], lv2_argmax["v2_self_resid"]],
        "argmax_layer": lv2_argmax["layer"], "meta_report_last_v2_3dp": meta_last_v2,
        "unrounded_range_2dp": list(full_2dp), "meta_3dp_range_2dp": list(meta_2dp)}
    row("purity–potency: last-position self-indexed 0.83–0.88",
        f"{last_v2[0]:.4f}–{last_v2[1]:.4f} (L40–L60)",
        "data/e0/e0_axes.npz last_reward vs last_character (V2); e0_axes.meta.json report.last "
        "v2_self_residual_frac (3 dp)", "reproduced",
        f"PRECISION: the upper end is {lv2_argmax['v2_self_resid']:.4f} at L{lv2_argmax['layer']}, "
        f"computed unrounded from the npz's float32 vectors, stored as {meta_last_v2[lv2_argmax['layer']]:.3f} in the meta report's 3 dp; "
        f"the unrounded range rounds to {full_2dp[0]}–{full_2dp[1]} at 2 dp, and "
        f"{meta_2dp[0]}–{meta_2dp[1]} only via the 3-dp value (double rounding). The record carries "
        "'.83–.88' at " + loc("archive/RESULTS-cycles3-4.md", "self-residual frac .83–.88") + ", " +
        loc("FINDINGS-3.md", "0.83–0.88 (vs ≈ 0.51)") + " and " +
        loc(PREPRINT, "self-indexed 0.83–0.88", True) + f"; the note may write {full_2dp[0]}–"
        f"{full_2dp[1]} or footnote it (N1/PI). The block names 'the purity–potency figures' "
        "collectively; these five rows take the numbers from " +
        loc(PREPRINT, "**Purity is not potency.**", True) + " and FINDINGS-3. Span variant "
        f"beside: {span_v2[0]:.3f}–{span_v2[1]:.3f}")
    row("purity–potency: last-position sentiment cosine 0.11–0.21",
        f"{last_cs[0]:.4f}–{last_cs[1]:.4f}", "data/e0/e0_axes.npz last_reward vs last_sentiment",
        "reproduced", "")
    row("purity–potency: cosine 0.36–0.46 to the span mean",
        f"{min(csl):.4f}–{max(csl):.4f}", "data/e0/e0_axes.npz span_reward vs last_reward; "
        "e0_b2c_a.json cos_span_last_per_layer", "reproduced", "")
    row("purity–potency: sign-wrong at two of three layers at every dose",
        f"Δ+ < 0 at every frac: L44 {wrong[44]}, L48 {wrong[48]}, L52 {wrong[52]}",
        "data/e0/e0_b2c_a.json arms.*.pos.per_probe", "reproduced",
        "'sign-wrong' = Δ+ < 0 (Δ− is negative everywhere); 3 fracs (.05/.10/.20) per layer")
    row("purity–potency: max Δ+ = 0.135 (short of criterion at the third layer)",
        f"L52 max Δ+ = {l52:+.4f} vs {halfG:.4f}; no cell qualifies (selected_dose {sel_c})",
        "data/e0/e0_b2c_a.json L52_f0.2", "reproduced", "")
    # Round 2, finding 2: '0.16' is not 'one significant figure' (every layer is
    # 0.2 at 1 sf). The finding's '±0.01' is exceeded at L52 by 3.3e-05, so the
    # largest deviation is printed instead of a round bound.
    nr_dev = max(sp, key=lambda r: abs(r["norm_over_R"] - 0.16))
    nr_dev_v = nr_dev["norm_over_R"] - 0.16
    J["norm_over_R_wording"] = {"range": [span_nr[0], span_nr[1]],
                                "max_abs_dev_from_0.16": abs(nr_dev_v), "at_layer": nr_dev["layer"],
                                "layers_0.17_at_2dp": [r["layer"] for r in off16],
                                "all_layers_at_1sf": sorted({f"{r['norm_over_R']:.1g}" for r in sp})}
    nr_wording = (f"holds to within about ±0.01 ({span_nr[0]:.3f}–{span_nr[1]:.3f}; the largest "
                  f"deviation is L{nr_dev['layer']}'s {nr_dev['norm_over_R']:.6f}, {nr_dev_v:+.6f} from "
                  f"0.16, so a strict ±0.01 is exceeded there by {abs(nr_dev_v) - 0.01:.1e}); at 2 dp, "
                  f"{len(off16)} of {len(sp)} layers give " +
                  "/".join(sorted({f"{r['norm_over_R']:.2f}" for r in off16})) + " (" +
                  ", ".join(f"L{r['layer']} {r['norm_over_R']:.4f}" for r in off16) + "). At one "
                  "significant figure every layer is " +
                  "/".join(sorted({f"{r['norm_over_R']:.1g}" for r in sp})) + ", so '0.16' is a "
                  "2-significant-figure claim")
    row("‖d‖/R ≈ 0.16", f"{span_nr[0]:.4f}–{span_nr[1]:.4f} across L40–L60 (L48 {L48['norm_over_R']:.4f})",
        "data/e0/e0_axes.npz ‖span_reward‖ / e0_axes.meta.json R_per_layer_spanmean", "reproduced",
        "R_l as stored under R_per_layer_spanmean; not an analysis-tier check (the suite checks frac "
        "x R_l dose arithmetic, not ‖d‖/R). Wording: the preprint's '≈ 0.16 at every layer' (" +
        loc(PREPRINT, "‖d‖/R ≈ 0.16 at every layer", True) + ") " + nr_wording)
    row("sentiment cosine 0.52", f"max {span_cs[1]:.4f} at L48; range {span_cs[0]:.4f}–{span_cs[1]:.4f}",
        "data/e0/e0_axes.npz span_reward vs span_sentiment", "reproduced",
        "suite: 'L48 cos reward.sentiment' (0.522) and five sibling layer checks; the preprint says 'up to 0.52'. "
        "Beside: the archive's '.44–.52' (" + loc("archive/RESULTS-cycles3-4.md", "sentiment cos .11–.21 vs .44–.52") +
        f") is L40–L52 only; L56/L60 are {sp[4]['cos_sent']:.3f}/{sp[5]['cos_sent']:.3f}")
    row("fictional-character cosine ≈ 0.85", f"{span_cc[0]:.4f}–{span_cc[1]:.4f} (L48 "
        f"{L48['cos_char']:.4f}; six-layer mean {cc_mean:.4f})",
        "data/e0/e0_axes.npz span_reward vs span_character", "reproduced",
        "suite: 'L{40..60} cos reward.character' (6 checks); '≈ 0.85' fits the layer range/mean; at the dose layer it is .86")
    row("self-indexed residual ≈ 0.51", f"L48 {L48['v2_self_resid']:.4f}; range "
        f"{span_v2[0]:.4f}–{span_v2[1]:.4f}", "data/e0/e0_axes.npz (V2, character guard)", "reproduced",
        "suite: 'L48 V2 self-residual' (0.509) and five sibling checks; '≈ 0.51' is the L48 value "
        "(L40 is .550; the extraction entry says '≈ .51–.55', " +
        loc("archive/RESULTS-cycles3-4.md", "V2 self-indexed residual fraction ≈ .51–.55") + ")")
    r2 = rdb["d2|v2_and_read_clean k2 (set of record)"]
    r3 = rdb["d3|v2_and_read_clean k2 (set of record)"]
    rR = rdb["d2|AUC_R k2 (arm R, displacement comparator)"]
    # Round 2, finding 8: the comparator row names its own contrast and CV.
    rR_doc = scores["d2"]["readability"]["AUC_R"]
    L_aucR = loc("scripts/e2d_score.py", 'rounds_R = RD.clean_rounds(sessions, "R", marked=marked)')
    assert (rR_doc["k"], rR_doc["b"]) == (2, 20), (rR_doc["k"], rR_doc["b"])
    row("e2d readability .574/.613 vs .70",
        f"{r2['median']:.4f} (0.20) / {r3['median']:.4f} (0.30); p10 {r2['p10']:.4f} / {r3['p10']:.4f} vs .60; gate fails both conjuncts at both doses",
        "data/e2d/d2_scores.json, d3_scores.json readability.v2_and_read_clean.k2.aucs", "reproduced",
        f"median/p10 recomputed from the 20 stored per-resample AUCs (model outputs). Probe: "
        f"logistic (seed 7, 300 it., lr .1, l2 .01) on the mean-pooled post-norm final residual; "
        f"contrast: state-live (+axis, L48) vs unsteered rounds of the M arm, k = 2 records; CV: "
        f"task-disjoint halves, B = 20. Clean domain recomputed "
        f"{dom['d2|M|v2+read'][0]}/{dom['d2|M|v2+read'][1]} and {dom['d3|M|v2+read'][0]}/{dom['d3|M|v2+read'][1]} "
        f"(state-live/unsteered rounds). D3 (0.30) carries the record's caveat that it lacks D2's "
        f"task-disjointness guarantee (M-arm task-id coverage pos {cov['d3']['distinct_pos']} / neg "
        f"{cov['d3']['distinct_neg']} against floor {cov['d3']['floor']}; {L_d3cav}, {L_d3cov}). D1 "
        f"(0.10) beside: {rdb['d1|k2_resampled (D1, n = 4 M sessions)']['median']:.4f}, which the "
        f"artifact itself labels (d1_sessions.json readability._descriptive, quoted): "
        f"\"{d1doc['readability']['_descriptive']}\"")
    row("comparator .534", f"{rR['median']:.4f} (p10 {rR['p10']:.4f}) at 0.20 only",
        "data/e2d/d2_scores.json readability.AUC_R.aucs", "reproduced",
        f"arm R (norm-matched random direction, same dose). Contrast: random-direction-live vs "
        f"unsteered rounds of arm R; probe and CV as the readability row (the same "
        f"`resampled_auc`, k = {rR_doc['k']}, B = {rR_doc['b']}, task-disjoint halves; {L_aucR}). "
        f"Clean domain (audit- and read-clean) {dom['d2|R|v2+read'][0]}/{dom['d2|R|v2+read'][1]} "
        f"recomputed (= stored {rR['n_pos']}/{rR['n_neg']}); no comparator at 0.30 (D3 ran M-only)")
    row("audit-flagged .000/.023/.047",
        f"{aud['d1|M']['k']}/{aud['d1|M']['n']} = {aud['d1|M']['rate']:.4f}, "
        f"{aud['d2|M']['k']}/{aud['d2|M']['n']} = {aud['d2|M']['rate']:.4f}, "
        f"{aud['d3|M']['k']}/{aud['d3|M']['n']} = {aud['d3|M']['rate']:.4f}",
        "data/e2d/d{1,2,3}_sessions.json rounds+choices `degen` (M arm, all rounds, all sessions); "
        "d2/d3_scores.json audit_rates_by_round_class", "reproduced",
        "equals the stored tables at D2/D3. Domain: every round (forced + free, steered + unsteered) "
        "of every M-arm session, excluded sessions included. "
        f"Only one of four dose steps is resolved (read .10->.20, Fisher exact one-sided p = "
        f"{steps['read .10->.20']['one_sided_greater']:.4f}, two-sided {steps['read .10->.20']['two_sided']:.4f}); "
        f"audit .20->.30 Fisher exact one-sided p = {steps['audit .20->.30']['one_sided_greater']:.4f}, "
        f"two-sided {steps['audit .20->.30']['two_sided']:.4f} (record figures, see the dose-step row); the R arm at 0.20 is "
        f"{aud['d2|R']['k']}/{aud['d2|R']['n']} = {aud['d2|R']['rate']:.3f}, so the preprint's 'coherence degrades "
        "monotonically' is the gloss the values-check flagged (" + loc("RESULTS.md", "**\"coherence degrades monotonically with dose\"**") +
        "); the closure text of record says 'ordered ... a single resolved step ... not axis-specific'")
    row("read-marked .000/.113/.155 (context; in the closure text, not a block figure)",
        ", ".join(f"{rm[t][0]}/{rm[t][1]} = {rm[t][0] / rm[t][1]:.4f}" for t in ("d1", "d2", "d3")),
        "data/e2d/d{1,2,3}_read_marks.json against d{1,2,3}_sessions.json (M arm); "
        "d2/d3_scores.json read_mark_rates", "reproduced",
        "Domain: every round (forced + free, steered + unsteered) of every M-arm session, excluded "
        f"sessions included. Provisional reader. D1's marks file marks arm S only "
        f"({mk_meta['d1']['marks_by_arm']}), so D1 M is {rm['d1'][0]}/{rm['d1'][1]}. Closure text: " +
        loc("RESULTS.md", "(audit .000 / .023 / .047; read-marked .000 / .113 / .155"))
    row("dose-step p values (context; record figures, not block figures)",
        "; ".join(f"{lab}: one-sided {f['one_sided_greater']:.4f} / two-sided {f['two_sided']:.4f}"
                  for lab, f in steps.items()) +
        f"; D2 R > M one-sided {r_vs_m['one_sided_greater']:.4f} / two-sided {r_vs_m['two_sided']:.4f}",
        "Fisher exact on the counts above (stdlib math.comb); M arm, all rounds, all sessions",
        "reproduced",
        f"record: closure text {L_close} (read .10->.20 two-sided .021, one-sided .011; .20->.30 "
        f"two-sided audit .15, read .20); values-check {L_vc} (one-sided .011/.41/.10/.10) and "
        f"{L_rm} (R > M one-sided .16); at 4 dp, all eight dose-step values in the R4 Fisher table "
        f"of record {L_r4} (equal to the values computed here at 4 dp: "
        f"{'yes' if all(r4_eq.values()) else 'NO'}), audit .10->.20 two-sided "
        f"{steps['audit .10->.20']['two_sided']:.4f} at {l4('audit .10->.20')} and again in its PASS "
        f"line {L_r4pass}, and R > M one-sided {r_vs_m['one_sided_greater']:.4f} at {L_rm4}. "
        f"computed-new (not in the record): R vs M two-sided {r_vs_m['two_sided']:.4f} only")
    row("oracle tier reproduced Δ± exactly (context for Δ±; not a block figure)",
        "D+ +0.2848, D- -0.3946, max|D_rand| 0.0884, 5/5", loc("results/raw/2026-08-12_rule26_b2b_tightened.txt",
                                                             "5/5 criteria reproduced") + "; oracle_rule26.json@9f3148c",
        "log-only", "needs the model; the canonical record at the pin no longer carries these rows (section 1b)")
    J["figures"] = F
    P("")

    # ====================================================== notes
    P("## Notes for N1 and the PI (none is a STOP)")
    P("")
    notes = [
        "Suite count: the suite prints " + summ(pn) + f" at {PIN}, not 103/103. Every '103' "
        "(block :68/:70/:107/:137 -- :137 is §6 README-NOTE item (3), 'how to run the regression "
        "suite and what 103/103 covers', where the stale count would reach the release README -- "
        "and " + loc("README.md", "must print **103/103**") + ") is the post-S2 count of 2026-08-20.",
        "Rule-26 record: `data/regression/oracle_rule26.json` at the pin carries only criterion "
        "(iii) (four e2a choice-read rows, 2026-08-18). The B2b exact reproduction (the oracle's "
        "hold on Δ+/Δ−/V1) is at 9f3148c and in results/raw/2026-08-12_rule26_b2b_tightened.txt; "
        "the kernel-gate rows at db0d177 and in results/raw/2026-08-12_rule26_oracle.txt. The README should say so rather than imply one "
        "artifact holds all oracle criteria.",
        "Wrong referent (preprint §5.2, " + loc(PREPRINT, "(G = 0.316) by roughly two-fold", True) +
        f"): 'the natural praise–criticism gap on that instrument (G = 0.316)'. G is the battery "
        f"mean; the film-title instrument's own gap is g_0 = {top_g:.3f} and the 'roughly two-fold' "
        f"is {top_shift:.3f}/{top_g:.3f} = {top_shift / top_g:.2f}x ({CNP}; the record's own "
        f"wording is '~2×' against that instrument's gap, {L_2x}). Suggested wording: '(its own "
        f"natural gap g = {top_g:.2f}; battery mean G = 0.316)'.",
        f"Wording: '9/12 and 10/12 on the remaining probes' -- the counts are over all 12 probes; "
        f"over the 11 remaining after the LOO they are {rest_pos}/11 and {rest_neg}/11 ({CNP}). "
        f"FINDINGS-3 carries the same counts as '9/12 and 10/12 elsewhere' ({L_f3_else}), with "
        "the same ambiguity.",
        "Wording (" + loc(PREPRINT, "a clean overdose regime at f = .40", True) + "): 'a clean "
        "overdose regime at f = .40, where both poles read as post-criticism' holds at L44 only "
        "(Δ+ " + "; ".join(f"L{c['layer']} {c['dpos']:+.4f}" for c in od) + " at f = .40, "
        "recomputed in 2d). The archive's B2a entry states it as 'L44 Δ+ sign flip' (" +
        loc("archive/RESULTS-cycles3-4.md", "overdose signature at frac .40 (L44 Δ+ sign flip") +
        "). A second carrier of the overgeneralization: FINDINGS-3's 'an overdose regime at 4× "
        "(all displacement reads as criticism' (" + L_f3_od + "); at 4× the selected frac 0.10, "
        "i.e. f = .40, Δ+ is still positive at " + " and ".join(f"L{c['layer']}" for c in od if c["dpos"] > 0) + " (above).",
        "Wording (" + loc(PREPRINT, "coherence degrades monotonically", True) + "): 'coherence "
        "degrades monotonically (audit-flagged rounds .000/.023/.047 across 0.10/0.20/0.30)' -- the "
        "figures reproduce; 'monotonically' is the values-check's flagged gloss (of the four dose "
        "steps only read .10->.20 is resolved, one-sided Fisher p = "
        f"{steps['read .10->.20']['one_sided_greater']:.4f}; the R arm degrades at "
        f"{aud['d2|R']['rate'] / aud['d2|M']['rate']:.2f}x M's rate at 0.20). The closure text of "
        "record has the hedged form ('ordered', 'a single resolved step', 'not axis-specific').",
        "Beside, same preprint sentence (not in the block's list): 'the marker imprint falls to "
        "about a quarter of its short-context value' (ratio recomputed above: "
        f"{mk_d2 / v1_l48_f02:.3f}) -- the values-check (" +
        loc("RESULTS.md", "a quarter of its short-context value (excised +.103 vs V1's") +
        ") found the arithmetic holds (.103/.408) but the two are different channels (a state-live "
        "read vs a no-injection read of generated text); the closure text of record has no "
        f"'quarter' (string check: 'quarter' in the blockquote = {q_in_closure}).",
        "'≈ 0.51' self-indexed and '≈ 0.85' character cosine are layer-dependent: L48 gives .509 and "
        f".861; the six-layer ranges are {span_v2[0]:.3f}–{span_v2[1]:.3f} and {span_cc[0]:.3f}–{span_cc[1]:.3f}. "
        f"Likewise ‖d‖/R is {span_nr[0]:.3f}–{span_nr[1]:.3f}: the preprint's '≈ 0.16 at every layer' "
        + nr_wording + ".",
        f"Precision: the last-position self-indexed range '0.83–0.88' is {last_v2[0]:.4f}–"
        f"{last_v2[1]:.4f} unrounded, i.e. {full_2dp[0]}–{full_2dp[1]} at 2 dp; '.88' comes "
        f"from the meta report's 3-dp {meta_last_v2[lv2_argmax['layer']]:.3f} at L{lv2_argmax['layer']} "
        "rounded again. Not a transcription error; the note may write the unrounded range or "
        "footnote it (N1/PI).",
        "No figure needed an analyzer change; nothing here is a STOP. Post-hoc items (LOO beyond "
        "Δ+, G over 11 probes) are labelled post-hoc; the dose-step Fisher p values are record "
        "figures reproduced here (all eight at 4 dp in the R4 Fisher table of record, " + L_r4 +
        "), and only R vs M two-sided is computed-new; the sub-figures 8/11, 9/11, LOO Δ−, 2.14x "
        "and 7.9x are marked " + CNP + " where they are printed; none licenses anything.",
    ]
    for i, n in enumerate(notes, 1):
        P(f"{i}. {n}")
    J["notes"] = notes
    P("")

    # ====================================================== values-check
    vc_l1570 = loc("archive/RESULTS-cycles3-4.md", "V2 self-indexed residual fraction ≈ .51–.55")
    named = {c["commit"]: c["first_count_named"] for c in chain_full}
    vc = [
        ("1", "borderline substantive",
         "'last-position self-indexed 0.83–0.88' marked reproduced with no comment, though the "
         "full-precision upper end rounds to .87",
         "FIXED",
         f"Confirmed: npz unrounded {last_v2[0]:.4f}–{last_v2[1]:.4f} -> {full_2dp[0]}–"
         f"{full_2dp[1]} at 2 dp; meta report.last L{lv2_argmax['layer']} = "
         f"{meta_last_v2[lv2_argmax['layer']]:.3f}. Status kept 'reproduced' with a PRECISION note in "
         "the row (the record's three carriers of '.83–.88' located there) and a new note for "
         "N1/PI."),
        ("2", "minor",
         "'D1 has no marks file' is false; the script hard-coded D1's read-marked count",
         "FIXED",
         f"Confirmed: data/e2d/d1_read_marks.json exists at the pin (entered {d1_marks_first}), "
         f"{mk_meta['d1']['n_marks']} marks by arm {mk_meta['d1']['marks_by_arm']}. The script now "
         "reads all three marks files and recounts M (port of marks.tabulate's domain): "
         + ", ".join(f"{t} {k}/{n}" for t, (k, n) in sorted(rm.items())) +
         f"; D2/D3 equal to stored: {'yes' if rm_equal else 'NO'}. The figure is unchanged."),
        ("3", "minor",
         "dose-step Fisher p values labelled computed-new, though the record carries them",
         "FIXED",
         f"Confirmed at {L_close}, {L_vc}, {L_rm}. Relabelled 'reproduced' with each record value "
         "and locator beside it; only audit .10->.20 two-sided "
         f"({steps['audit .10->.20']['two_sided']:.4f}) and R vs M two-sided "
         f"({r_vs_m['two_sided']:.4f}, now printed) stay computed-new. The audit row names the test "
         "(Fisher exact, one- and two-sided); a context row carries the p values for N1's ledger. "
         "[Superseded in round 2, finding 1: audit .10->.20 two-sided is in the record too, at 4 dp; "
         "only R vs M two-sided stays computed-new.]"),
        ("4", "minor",
         "the readability row omits the record's caveat that D3 lacks D2's task-disjointness "
         "guarantee",
         "FIXED",
         f"Confirmed: d3_sessions.json task_id_coverage pos {cov['d3']['distinct_pos']} / neg "
         f"{cov['d3']['distinct_neg']}, meets_floor {cov['d3']['meets_floor']}, below_d2_floor "
         f"{cov['d3']['below_d2_floor']} (D2: {cov['d2']['distinct_pos']}/{cov['d2']['distinct_neg']}, "
         f"meets_floor {cov['d2']['meets_floor']}); caveat at {L_d3cav} and {L_d3cov}. Added to §2e "
         "(printed from the artifact) and to the row."),
        ("5", "minor", "'≈ .51–.55' quoted without a pinned locator", "FIXED",
         f"Locator added: {vc_l1570}."),
        ("6", "minor",
         "the suite-count history from commit subjects omits 136 and 137 and leaves 103->125 "
         "unexplained",
         "FIXED",
         "The script now scans each full commit message (subject + body) of every commit touching "
         f"analysis.py ({len(chain_full)} commits). 6897b67 names '{named.get('6897b67')}' in its "
         f"body; da71287 '{named.get('da71287')}'; c593579 '{named.get('c593579')}'; 1465b34 "
         f"'{named.get('1465b34')}'. Conclusions unchanged (103 = post-S2; 154 since a9e6a74)."),
        ("7", "minor",
         "three glosses read as the record's wording: 'causal counterpart', 'n = 4, noise', "
         "'one-sided asymmetry'",
         "FIXED",
         "(a) 'causal counterpart' dropped; the S2 paragraph now quotes corrected_reading_of_record "
         "and its scope field ('DESCRIPTION ONLY') verbatim. (b) D1 readability now quotes "
         "d1_sessions.json readability._descriptive. (c) the random-arm note quotes "
         "queued_apparatus_note verbatim; ratio recomputed three ways ("
         f"{J['rand_asymmetry_ratio']['b2b_stored_4dp']:.3f} / "
         f"{J['rand_asymmetry_ratio']['b2b_recomputed_means']:.3f} / "
         f"{J['rand_asymmetry_ratio']['s2_unrounded']:.3f})."),
        ("8", "minor", "'‖d‖/R ≈ 0.16 at every layer' wording not flagged (checker: L52 and L56 "
         "round to .17)", "FIXED (with a correction to the finding)",
         f"Range {span_nr[0]:.4f}–{span_nr[1]:.4f}; layers rounding off .16 at 2 dp: " +
         ", ".join(f"L{r['layer']} {r['norm_over_R']:.4f}" for r in off16) +
         f" -- {len(off16)} of {len(sp)}; beyond the finding's L52 and L56, also " +
         ", ".join(f"L{r['layer']} ({r['norm_over_R']:.4f} -> {r['norm_over_R']:.2f})"
                   for r in off16 if r["layer"] not in (52, 56)) + ". "
         "Flagged in the row and in note 8. [Round 2, finding 2 corrects the wording of that flag.]"),
        ("9", "minor", "the read-marked rates' domain is not stated", "FIXED",
         "Stated in §2e and in the new read-marked context row: every round (forced + free, "
         "steered + unsteered) of every M-arm session, excluded included (marks.tabulate, rule 23)."),
    ]
    J["values_check"] = [{"finding": a, "severity": b, "claim": c, "disposition": d, "detail": e}
                         for a, b, c, d, e in vc]
    P("## Values-check (adversarial pass 1 of script sha256 73e02f02...89fa; dispositions)")
    P("")
    P("An independent checker reported re-running the script, recomputing every block figure with "
      "its own code from the pinned artifacts (all agreeing) and opening the pinned locators. It "
      "raised nine findings and reported no wrong number and no STOP. Code verified each finding "
      "against the pin with its own tool run before applying it; none was rejected, and one (8) was "
      "applied with a correction. The fixes change wording, labels, locators and one hard-coded "
      "input (D1's marks); no figure's value changed.")
    P("")
    P("| # | severity | finding | disposition | evidence / what changed |")
    P("|---|---|---|---|---|")
    for a, b, c, d, e in vc:
        P(f"| {a} | {b} | {cell(c)} | {d} | {cell(e)} |")
    P("")
    # ------------------------------------------- values-check, round 2
    L_gc3 = loc("data/e2d/closure_glosscheck3.json", "audit10-20 (1.0000, 0.4129)")
    L_f3_50 = L_f3_od
    vc2 = [
        ("1", "substantive",
         "audit .10->.20 two-sided p = 1.0000 labelled 'not in the record: computed-new' (§2e, the "
         "dose-step row, note 10, round-1 row 3), though the record carries it",
         "FIXED",
         f"Confirmed: the R4 FISHER TABLE OF RECORD prints it at {l4('audit .10->.20')} and its PASS "
         f"line at {L_r4pass}; {L_gc3} has it too. The script now parses that table (rows {L_r4}) and "
         f"asserts 4-dp equality with its own Fisher values: "
         f"{sum(ok for _, _, ok in r4_vals)}/{len(r4_vals)} values (four steps x two tests) "
         "equal. Relabelled reproduced (with its 4-dp locator) in "
         "§2e, the dose-step row and note 10; the 4-dp locator is added beside every RESULTS.md "
         "2-dp locator; round-1 row 3 carries a superseded pointer. R vs M two-sided "
         f"{r_vs_m['two_sided']:.4f} confirmed absent as this p (git grep at the pin over RESULTS.md, "
         "results/raw/ and data/e2d/ for 0.2535 / .2535 / .254 finds only unrelated values: a CI "
         "bound on the e2d marker Δ+, " +
         loc("data/e2d/closure_valuescheck.json", "a normal 95% CI on +.103 is [-0.0475, +0.2535]") +
         ", a per-resample array value 0.253559, " + loc("data/e2d/d2_scores.json", "0.2535593303442291") +
         ", and +0.254 values in two earlier raws), so it alone stays computed-new. Beside: the "
         "record's R > M "
         f"one-sided {r_vs_m['one_sided_greater']:.4f} at 4 dp ({L_rm4}) is now cited."),
        ("2", "minor",
         "‖d‖/R: 'the preprint's \"≈ 0.16 at every layer\" holds to one significant figure' is "
         "wrong wording (at 1 sf every layer is 0.2)",
         "FIXED (with a correction to the fix)",
         f"Confirmed: at 1 sf every layer is "
         f"{'/'.join(J['norm_over_R_wording']['all_layers_at_1sf'])}. The fix's 'within ±0.01' is "
         f"itself false at L{nr_dev['layer']}: {nr_dev['norm_over_R']:.6f} − 0.16 = {nr_dev_v:+.6f}, "
         f"over 0.01 by {abs(nr_dev_v) - 0.01:.1e}. The row and note 8 now say 'within about ±0.01' "
         "with the range and the largest deviation printed, and that at 2 dp "
         f"{len(off16)} of {len(sp)} layers give 0.17 (" +
         ", ".join(f"L{r['layer']} {r['norm_over_R']:.4f}" for r in off16) + ")."),
        ("3", "minor",
         "'2·max|Δ_rand| = 2·0.0884 = 0.1767' is inconsistent as written (2 × 0.0884 = 0.1768)",
         "FIXED",
         f"Confirmed: unrounded max|Δ_rand| = {mrand:.6f} (rand_neg, mean of the 12 per-probe "
         f"values), 2x = {2 * mrand:.4f}; stored criterion.max_abs_D_rand {mrand_st:.4f}, 2x = "
         f"{2 * mrand_st:.4f}, the record's '2×rand = 0.1768' at {L_2rand}. §2c's V1 line and the "
         "random row now print both. The verdict is unchanged (PASS either way)."),
        ("4", "minor",
         "'S2's separate full-precision re-run' / 'again at full precision' -- S2 ran the same "
         "4-bit MLX model; 'full precision' means bf16 in this project",
         "FIXED (and extended to the same term in Code's wording elsewhere)",
         f"Confirmed: s2_neighbor_axes.json provenance model_id {s2prov.get('model_id')}, dtype "
         f"'{s2prov.get('dtype')}', backend {s2prov.get('backend')}. §2c and the Δ+ row now say "
         "'a separate re-run on the same 4-bit MLX stack, stored unrounded'. The same collision in "
         "Code's own wording -- the purity row, note 9, round-1 row 1's evidence, the random row's "
         "ratio -- now says 'unrounded'; JSON keys renamed rand_asymmetry_ratio.s2_full_precision "
         "-> s2_unrounded and purity_v2_precision.full_precision_range(_2dp) -> unrounded_range(_2dp) "
         "(no script under scripts/ reads them: grep). Round-1 row 1's claim column (the checker's "
         "words) is left as it was."),
        ("5", "minor",
         "the Figures rows carry 8/11, 9/11, LOO Δ− = -0.1898, 2.14x and 7.9x as plain values, "
         "though none is in the record",
         "FIXED",
         "Confirmed: git grep at the pin over RESULTS.md, archive/RESULTS-cycles3-4.md, "
         "FINDINGS-3.md, data/e0/ and results/raw/*e0* finds 8/11 and 9/11 only as substrings of "
         "unrelated figures (e.g. 18/112) and a date, -0.1898 only as part_neg's probe-7 "
         "per-probe value (" + loc("data/e0/e0_b2_b2b.json", "-0.1898,") + "), 2.14 only as an "
         "unrelated label and an unrelated per-probe value (2.1429 in e0_b2c_a.json), and no "
         "7.86 / 7.9x; the record has "
         f"'~2×' ({L_2x}) and 'Δ+ ≈ 0.085'. Marked '{CNP}' in the three rows, in §2c's bullets "
         "and in notes 3, 4 and 10. Values unchanged."),
        ("6", "minor",
         "note 1's list of '103' omits block :137 (§6 README-NOTE item (3))",
         "FIXED",
         f"Confirmed: '103/103' at block lines {', '.join(':' + str(x) for x in blk103)} (asserted "
         "in the script); in README.md only at " + loc("README.md", "must print **103/103**") +
         ". Added to note 1 and to §1's sentence."),
        ("7", "minor",
         "note 5 misses FINDINGS-3's carrier of the overdose overgeneralization; FINDINGS-3's "
         "'elsewhere' is cited without a locator",
         "FIXED",
         f"Confirmed: {L_f3_50} 'an overdose regime at 4× (all displacement reads as criticism'; "
         f"{L_f3_else} '9/12 and 10/12 elsewhere'. Note 5 cites the first as a second carrier; the "
         "unpinned mention was in the 9/12 row (not note 4), which now carries the locator, and "
         "note 4 now names it as well."),
        ("8", "minor",
         "the comparator row names neither its contrast nor its CV",
         "FIXED",
         f"Confirmed: d2_scores.json readability.AUC_R k {rR_doc['k']}, b {rR_doc['b']}, "
         f"n_evaluable {rR_doc['n_evaluable']}, n_pos/n_neg {rR_doc['n_pos']}/{rR_doc['n_neg']}; "
         f"{L_aucR} builds it with RD.resampled_auc on clean_rounds(sessions, 'R', marked=marked), "
         "the same function, k and B as the M-arm set of record. The row now states the contrast "
         "(random-direction-live vs unsteered rounds of arm R), probe and CV, and the audit- and "
         "read-clean domain; its stored n_pos/n_neg is read from the artifact, no longer typed."),
        ("9", "minor",
         "§2a: 'mean differences ... over the 1,344 extraction contexts' is imprecise",
         "FIXED",
         f"Confirmed: e0_axes.meta.json n_contexts {meta['n_contexts']}, n_tasks {meta['n_tasks']}, "
         f"n_paraphrases {meta['n_paraphrases']} -> {n_frames} frames x {per_frame} contexts "
         "(asserted); " + loc("archive/RESULTS-cycles3-4.md", "1344 contexts (48 × 7 × 4)") +
         ". Reworded to 'the mean difference between two frames' means (192 contexts each) from "
         "the 1,344-context extraction'."),
        ("10", "minor", "the JSON has no 'stops' key", "FIXED", "The JSON now carries \"stops\": []."),
    ]
    J["values_check_round2"] = [{"finding": a, "severity": b, "claim": c, "disposition": d,
                                 "detail": e} for a, b, c, d, e in vc2]
    P("### Round 2 (adversarial pass 2, on the outputs of script sha256 a5478765...2d36f; dispositions)")
    P("")
    P("A second independent checker raised ten findings on those outputs (one substantive, nine "
      "minor); none is a STOP item. Code verified each against the pin with its own "
      "tool run before applying it; none was rejected. One (2) was applied with a correction to "
      "its fix, and one (4) was applied and extended to the same term in Code's wording elsewhere. "
      "One status changed (audit .10->.20 two-sided: computed-new -> reproduced) and five "
      "sub-figures gained a computed-new (post-hoc, descriptive) label; no figure's value changed.")
    P("")
    P("| # | severity | finding | disposition | evidence / what changed |")
    P("|---|---|---|---|---|")
    for a, b, c, d, e in vc2:
        P(f"| {a} | {b} | {cell(c)} | {d} | {cell(e)} |")
    P("")
    # Round 3: the adversarial check of the portability fix (its findings 2, 5
    # and 6 bear on this script; 1, 3 and 4 on scripts/audit_note_N11.py).
    r3_start = len(L)
    n_aud = sum(c["files"] for c in attr["by_commit"]
                if c["subject_head"].startswith("AUDIT-note-release"))
    vc3 = [
        ("1", "minor (the check's finding 2)",
         "§0's sentence after the tracked-differing list was fixed text written at the first "
         "run's HEAD: at 6485da2 it still called the 84 listed files the concurrent PROPOSAL-m "
         "session's commits and the PI's notebook edit, though 63 come from the audit's own "
         "commits 09c3a8c and 6485da2, and it called scripts/audit_note_*.py untracked, though "
         "21 are tracked and in the list",
         "FIXED",
         "Confirmed (`git log --name-only 09c3a8c^..6485da2`). The sentence is now computed "
         "from the list at run start: per commit after the pin, the listed files it touches; "
         "the files no commit touches; those with uncommitted changes; and which .py files the "
         "suite's two structural source scans read (their predicates ported from "
         "valence_core/regression/analysis.py at the pin), with the untracked .py files the "
         "qwen-helper scan also reads. Here: " +
         "; ".join(f"{c['commit']} {c['files']}" for c in attr["by_commit"]) +
         f" (commits whose subject starts 'AUDIT-note-release': {n_aud} file-touches); "
         f"no commit {len(attr['no_commit'])}; uncommitted {len(attr['uncommitted'])}; both "
         f"scans {len(attr['scan_both'])}, qwen-helper scan only {len(attr['scan_qwen_only'])}; "
         f"untracked .py read {len(attr['untracked_py_scanned'])}. The claim that only "
         "valence_core/m/*.py and scripts/m_sessions.py are visible to the suite is dropped: "
         "which other listed files the suite opens is not computed here. The JSON carries "
         "integrity.tracked_files_differing_from_pin_attribution."),
        ("2", "minor (this script's half of the check's finding 5)",
         "in a fresh clone the script stops with FileNotFoundError on the untracked "
         f"{PREPRINT}, and the closing section did not name that dependency",
         "FIXED (README-NOTE.md flagged, not edited)",
         "Confirmed: the version at 09c3a8c opens it unguarded "
         "(scripts/audit_note_N8.py@09c3a8c:361), and the previous version (sha256 "
         "9d33aee3...0595) did so after making its mkdtemp work root. "
         f"The script now looks for {PREPRINT} before it makes anything; if it is absent it "
         f"prints '[not run: {PREPRINT} absent] ...' on stderr and exits 2 without writing "
         "either output (the committed raws are not overwritten by a not-run). With the file "
         "present nothing changes. The closing section's 'Still needed' bullet names it. "
         "README-NOTE.md's dependency list says N8 opens the file 'with no existence check'; "
         "after this change that clause no longer holds for N8, while the need for the file "
         "does: for the PI. Code's check, a separate run of this script before these check "
         "sentences were added (sha256 d17d801d...ba2b), copied alone into an empty directory "
         "(so no preprint), TMPDIR a scratch directory: exit 2 with that line; nothing in "
         "TMPDIR, no output written."),
        ("3", "minor (the check's finding 6)",
         "the closing section's 'This run' line printed 'made by this run: no, --scratch given' "
         "even when the --scratch directory did not exist and the run created it",
         "FIXED",
         "The line now records whether the work root was made by mkdtemp and, for --scratch, "
         "whether it existed beforehand (here: " +
         ("mkdtemp, default" if scratch_made else
          f"--scratch, existed beforehand: {'yes' if scratch_existed else 'no'}") + "). "
         "Code's check, separate runs of the same version (sha256 d17d801d...ba2b), outputs "
         "not committed: --scratch at a new path printed 'existed beforehand: no, made by "
         "os.makedirs in this run'; a second run at the same path 'existed beforehand: yes'."),
    ]
    J["values_check_round3"] = [{"finding": a, "severity": b, "claim": c, "disposition": d,
                                 "detail": e} for a, b, c, d, e in vc3]
    P("### Round 3 (adversarial check of the portability fix, on the outputs of script sha256 "
      "9d33aee3...0595; dispositions)")
    P("")
    P("A third independent check re-ran this script and scripts/audit_note_N11.py under a "
      "sandbox (the session scratch unreadable, the repository unwritable, TMPDIR redirected; "
      "in second runs HOME and XDG_CONFIG_HOME too), from the repository and from a scratch "
      "clone, and recounted the outputs from git. Of its six findings, three bear on this "
      "script (all minor; its finding 5 covers both scripts) and four on "
      "scripts/audit_note_N11.py, disposed in that script's raw. It found no figure, status "
      "or verdict here that moved. Code verified each finding with its own tool run before "
      "applying it; none was rejected.")
    P("")
    P("| # | severity | finding | disposition | evidence / what changed |")
    P("|---|---|---|---|---|")
    for a, b, c, d, e in vc3:
        P(f"| {a} | {b} | {cell(c)} | {d} | {cell(e)} |")
    P("")
    P("Also changed by Code in round 3 (not findings): a default run that stops after making "
      "its mkdtemp work root and before writing into it now removes that empty directory at "
      "exit (the defect class of the check's finding 4 on N11; reproduced with the previous "
      "version, sha256 9d33aee3...0595, copied into an empty directory: it made its work "
      "root, stopped at its first git call and left the directory empty); the closing section's "
      "comparison classes the computed attribution sentence, its JSON key, this subsection "
      "and the \"values_check_round3\" key as new.")
    P("")
    r3_end = len(L)
    J["stops"] = []
    head_end = git("rev-parse", "HEAD").decode().strip()
    J["meta"]["head_at_end"] = head_end
    P(f"HEAD at run end: {head_end}  [run metadata]")
    P("")
    P("## Appendix: suite stdout, run (b) at the pin (verbatim)")
    P("")
    for l in pn["stdout"].rstrip("\n").split("\n"):
        P("    " + l)
    P("")

    # ---------------------------------------- portability fix + re-run check
    # Compared first, on the outputs as they stand (this section and the JSON's
    # "portability" key are not part of the comparison).
    left = sorted(os.listdir(args.scratch)) if os.path.isdir(args.scratch) else []
    left_n = {d: (len(os.listdir(os.path.join(args.scratch, d)))
                  if os.path.isdir(os.path.join(args.scratch, d)) else None)
              for d in ("tmp-wt", "tmp-pin")}
    other_left = [x for x in left if x not in ("tmp-wt", "tmp-pin")]
    tree_gone = not os.path.exists(tree)
    cmp_rev = args.compare_rev
    port = {"fix": "default --scratch: tempfile.mkdtemp(prefix=%r) under "
                   "tempfile.gettempdir(); was a fixed builder-session path" % SCRATCH_PREFIX,
            "work_root": tempdir_display(os.path.realpath(args.scratch)),
            "work_root_made_by_this_run": scratch_made,
            "scratch_given_existed_beforehand": None if scratch_made else scratch_existed,
            "tree_removed": tree_gone, "keep_tree": args.keep_tree,
            "left_in_work_root": {"tmp-wt_entries": left_n["tmp-wt"],
                                  "tmp-pin_entries": left_n["tmp-pin"],
                                  "other_top_level_entries": len(other_left)},
            "compare_rev": cmp_rev}
    try:
        cmp_full = git("rev-parse", "--verify", cmp_rev + "^{commit}").decode().strip()
        old_md = git("show", f"{cmp_full}:{DEF_OUT}").decode("utf-8").split("\n")
        old_js = json.loads(git("show", f"{cmp_full}:{DEF_JSON}"))
    except subprocess.CalledProcessError as e:
        cmp_full, old_md, old_js = None, None, None
        port["compare_error"] = (e.stderr or b"").decode(errors="replace").strip()[:300]
    if old_md is not None:
        if old_md and old_md[-1] == "":
            old_md = old_md[:-1]               # the file's final newline
        om = old_js.get("meta", {})
        nm = J["meta"]
        heads = set()
        for h in (om.get("head_at_start"), om.get("head_at_end"),
                  old_js.get("suite", {}).get("head_at_wt_run_end"),
                  nm.get("head_at_start"), nm.get("head_at_end"),
                  J["suite"].get("head_at_wt_run_end")):
            if isinstance(h, str) and re.fullmatch(r"[0-9a-f]{40}", h):
                heads |= {h, h[:7]}
        md_rows = compare_md(old_md, L, heads,
                             new_ranges=[(r3_start, r3_end, NEW_R3),
                                         (r9_start, r9_end, NEW_R9),
                                         (r10_start, r10_end, NEW_R10)])
        new_js = json.loads(json.dumps(J, default=float, ensure_ascii=False))
        js_rows = compare_json(old_js, new_js, heads)
        o_tr = old_js.get("integrity", {}).get("tracked_files_differing_from_pin") or []
        n_tr = J["integrity"]["tracked_files_differing_from_pin"]
        added, removed = sorted(set(n_tr) - set(o_tr)), sorted(set(o_tr) - set(n_tr))
        o_head, n_head = om.get("head_at_start"), nm.get("head_at_start")
        between = []
        if o_head and n_head and o_head != n_head:
            between = [x for x in git("diff", "--name-only", o_head, n_head
                                      ).decode().split("\n") if x]
        between_vsd = [x for x in between
                       if x.split("/")[0] in ("valence_core", "scripts", "data")]
        added_vsd = []
        if o_head and n_head and o_head != n_head:
            added_vsd = [x for x in git("diff", "--name-only", "--diff-filter=A", o_head,
                                        n_head, "--", "valence_core", "scripts", "data"
                                        ).decode().split("\n") if x]
        side_rx = re.compile(r"\((\d+) before, (\d+) after\)")
        side_old = next((side_rx.findall(x) for x in old_md if x.startswith(MD_SIDE[0])), [])
        side_new = next((side_rx.findall(x) for x in L if x.startswith(MD_SIDE[0])), [])
        port.update({
            "compare_rev_full": cmp_full,
            "md_lines_compared": {"old": len(old_md), "new": len(L)},
            "md_differing": md_rows, "json_differing": js_rows,
            "tracked_differing": {"old": len(o_tr), "new": len(n_tr),
                                  "added": len(added), "removed": len(removed),
                                  "added_changed_between_heads":
                                      sum(1 for x in added if x in between)},
            "heads": {"old": o_head, "new": n_head},
            "files_changed_between_heads": len(between),
            "of_which_under_valence_core_scripts_data": len(between_vsd),
            "added_under_valence_core_scripts_data": len(added_vsd),
            "gitignore_changed_between_heads": ".gitignore" in between,
            "working_tree_state_counts": {
                "old": {"ignored_before_after": side_old[0] if side_old else None,
                        "untracked_before_after": side_old[1] if len(side_old) > 1 else None},
                "new": {"ignored_before_after": side_new[0] if side_new else None,
                        "untracked_before_after": side_new[1] if len(side_new) > 1 else None}},
            "unexpected": sum(1 for r in md_rows + js_rows
                              if r["class"].startswith(UNEXPECTED))})
    sec = []
    S_ = sec.append
    S_("## Portability fix and interim re-run (2026-10-08), with the round-9 preprint "
       "re-point (2026-10-10) and round 10's (2026-10-12)")
    S_("")
    S_(f"- Fix: at `{COMPARE_REV}` the `--scratch` default was a fixed path in the builder's "
       "session scratch directory, which exists on one machine only (the committed run passed "
       "`--scratch` explicitly, as its command line shows). Without `--scratch` the script now "
       f"makes a fresh directory with `tempfile.mkdtemp(prefix='{SCRATCH_PREFIX}')` under "
       "`tempfile.gettempdir()`; an explicit `--scratch <dir>` is used as before (made if absent). "
       "Also changed, by the values-check's round 3 (above): §0's attribution sentence after the "
       "tracked-differing list is computed from the list (it was fixed text); a missing "
       f"`{PREPRINT}` stops the run before anything is made; the line below records whether "
       "`--scratch` existed. Nothing else above this section is computed differently; round 3, "
       "this section and the JSON's \"values_check_round3\", \"portability\" and "
       "integrity.tracked_files_differing_from_pin_attribution keys are new. Round 9 "
       f"(2026-10-10): the preprint of record is the patched text ({PREPRINT_RULING}); §0's "
       "preprint line, its sentence check and the JSON's integrity.preprint_of_record key "
       "are new or re-worded, and the comparison below classes them; a preprint locator "
       "whose sentence is missing now reads ':NOT FOUND (..., §0)' where it used to stop the "
       "run; a root preprint whose sha256 was not the preprint of record's made §0's sha "
       "line say STOP, its preprint lines UNEXPECTED below, and the exit status 3 (after the "
       "outputs were written); note 6's quote of preprint line 141 runs through '0.30)'. "
       f"Round 10 (2026-10-12): the preprint of record is patch v7 ({PREPRINT_ROUTING_R10}), "
       "its sha256 asserted in full before anything is made: any other root text is refused "
       "(exit 3, nothing written), which retires round 9's STOP clause, its UNEXPECTED gate "
       "for preprint lines and the write before exit 3; §0's sha line names patch v7 and the "
       f"archived patch-v6 text (`{PREPRINT_V6_COPY}`, never required); §0's round-10 lines "
       "and the JSON's integrity.preprint_round10 key are new; the comparison's preprint "
       "class names patch v7 and its sha normalisation covers the patch-v6 sha too.")
    S_(f"- Still needed off this laptop: the untracked `{PREPRINT}` (sha256 "
       f"{PREPRINT_SHA[:8]}...{PREPRINT_SHA[-5:]}) at the repository root, which a fresh clone does "
       "not carry unless the PI commits it (README-NOTE.md's dependency list asks for that); "
       "without it the script exits 2 before making anything, with '[not run: ... absent]' on "
       "stderr (a root text with any other sha256 is refused the same way: exit 3, "
       "'[refusing: ...]'). The suite runs under the interpreter that runs this script, which needs numpy. "
       "The round-3 check's run from a scratch clone, with the preprint copied in, exited 0 "
       "and reproduced every figure.")
    S_("- Cleanup, unchanged: the git-archive extraction `<scratch>/tree-" + PIN + "` is deleted "
       "after run (b) unless --keep-tree is given; the suite runs' TMPDIRs `<scratch>/tmp-wt` and "
       "`<scratch>/tmp-pin` (with the suite's leftover temp directories) stay in the work root, "
       "as before the fix.")
    masked = port["work_root"].startswith(TEMP_TOKEN)
    S_(f"- This run: work root `{port['work_root']}` ("
       + ("made by tempfile.mkdtemp in this run" if scratch_made else
          "--scratch given; existed beforehand: " + ("yes" if scratch_existed else
                                                      "no, made by os.makedirs in this run"))
       + (f"; this machine's temp-directory prefix is written `{TEMP_TOKEN}`, and the full "
          "path goes to stderr only" if masked else "") + "); extraction removed: "
       f"{'yes' if tree_gone else 'NO'}; left in the work root: tmp-wt {left_n['tmp-wt']} "
       f"entr(ies), tmp-pin {left_n['tmp-pin']} entr(ies), other top-level entries "
       f"{len(other_left)}.")
    if old_md is None:
        S_(f"- Comparison with the committed outputs at `{cmp_rev}`: not made "
           f"({port.get('compare_error') or 'not readable'}).")
    else:
        S_(f"- Interim re-run, compared with the committed outputs at `{cmp_full[:10]}` "
           f"(`git show {cmp_full[:7]}:{DEF_OUT}` and `:{DEF_JSON}`; this section and the "
           "\"portability\" key left out): md "
           f"{len(md_rows)} differing line(s) of {len(old_md)} there / {len(L)} here; JSON "
           f"{len(js_rows)} differing leaf path(s). Unexpected (in no class below): "
           f"{port['unexpected']}. Consecutive lines or leaves that are new in this version are "
           "listed as one range or one key.")
        grp = []
        for r in md_rows:
            if (grp and r["line_old"] is None and grp[-1]["line_old"] is None
                    and r["line_new"] and grp[-1]["hi"] and grp[-1]["class"] == r["class"]
                    and r["line_new"] == grp[-1]["hi"] + 1):
                grp[-1]["hi"] = r["line_new"]
            else:
                grp.append(dict(r, lo=r["line_new"], hi=r["line_new"]))
        for r in grp:
            here_ = ("-" if not r["lo"] else
                     f"{r['lo']}" if r["lo"] == r["hi"] else f"{r['lo']}-{r['hi']}")
            S_(f"    - md line{'s' if r['lo'] != r['hi'] else ''} {here_} here / "
               f"{r['line_old'] if r['line_old'] else '-'} at {cmp_full[:7]}: {r['class']}")
        newj = {}
        for r in js_rows:
            pre = next((p for p, c in JSON_NEW_PREFIXES.items() if c == r["class"]), None)
            if pre:
                newj[pre] = newj.get(pre, 0) + 1
                continue
            S_(f"    - JSON `{r['path']}`: {r['class']}")
        for pre, n_ in newj.items():
            S_(f"    - JSON `{pre}` ({n_} leaf path(s)): {JSON_NEW_PREFIXES[pre]}")
        S_(f"- HEAD at the compared run's start {(o_head or '?')[:10]}, here {(n_head or '?')[:10]}; "
           f"files changed between them (`git diff --name-only`): {len(between)}, of which under "
           f"valence_core/, scripts/ or data/: {len(between_vsd)}. Tracked files differing from "
           f"the pin: {len(o_tr)} there, {len(n_tr)} here ({len(added)} added, {len(removed)} "
           f"removed; of the added, {port['tracked_differing']['added_changed_between_heads']} "
           "are among the files changed between the two HEADs).")
        def bf(x):
            return f"{x[0]}/{x[1]}" if x else "?"
        S_("- The working-tree-state line counts untracked-and-ignored and untracked-not-ignored "
           "paths under valence_core/, scripts/ and data/ before/after run (a): there "
           f"{bf(side_old[0] if side_old else None)} and "
           f"{bf(side_old[1] if len(side_old) > 1 else None)}, here "
           f"{bf(side_new[0] if side_new else None)} and "
           f"{bf(side_new[1] if len(side_new) > 1 else None)}. Files added under those "
           f"directories by the commits between the two HEADs: {len(added_vsd)}; .gitignore "
           f"changed between them: {'yes' if '.gitignore' in between else 'no'}. The committed "
           "raw records the counts, not the paths, so a change in them is attributed only as "
           "far as these figures go; the line's own claim (the suite run leaves both sets "
           "unchanged) is evaluated afresh on each run.")
    S_("")
    L.extend(sec)
    J["portability"] = port

    out = os.path.join(REPO, args.out) if not os.path.isabs(args.out) else args.out
    jout = os.path.join(REPO, args.json_out) if not os.path.isabs(args.json_out) else args.json_out
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    with open(jout, "w", encoding="utf-8") as f:
        json.dump(J, f, indent=1, default=float, ensure_ascii=False)
        f.write("\n")
    print(f"wrote {os.path.relpath(out, REPO)} and {os.path.relpath(jout, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
