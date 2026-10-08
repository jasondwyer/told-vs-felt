#!/usr/bin/env python3
"""AUDIT-note-release v1.2, item N10 -- Horn-1 calibration R^2 = 0.53.

READ-ONLY ON THE RECORD. Every committed artifact is read at the pin
(`git show bbc9ffe:<path>`, read-only git only). Three local-only files in the
gitignored jlens-qwen36/ clone (the producing scripts and the JSON they wrote)
are opened read-only for a full-precision cross-check and for the regression's
exact definition; git is never run inside that clone. Nothing is written except
--out (and --json-out, only if passed). No model is loaded; no randomness is
used. Arithmetic is stdlib (math, statistics); numpy is not imported.

The block's rule: a figure is `reproduced` only if this script computes it from
committed JSON/JSONL/npz. The figure's only machine-readable artifact is
gitignored and was never committed, so its status is decided below from what
the pin carries; recomputations from the committed raw's printed table and from
the local-only JSON are labeled `computed-new` (post-hoc) and never upgrade it.

Usage (from anywhere):
  jlens-qwen36/.venv/bin/python scripts/audit_note_N10.py \
      [--out results/raw/2026-10-08_note-N10-horn1.md] [--json-out PATH] [--prev PATH]

--prev (optional) is read only: a previous version of this raw, whose numbers are
compared with this run's under a separate heading. It is not part of the run of record:
the run of record passes no --prev, because a --prev file is session-local and is not
committed (values-check round 2, finding 4).

Line numbers in every printed locator count '\\n' only (lines()), as
`git show <pin>:<path> | cat -n` does; str.splitlines() is never used to number lines.
"""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True

import argparse
import collections
import hashlib
import json
import math
import os
import re
import shlex
import statistics
import subprocess
from statistics import NormalDist

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = "bbc9ffe"
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
PREPRINT = "PREPRINT-v1_0-draft.md"          # untracked at the pin; sha-checked
PREPRINT_SHA = "d6431e97d35e5914574ff9884c0e64463a7baf1cf9d279f27ed45a683a6222b8"
CLONE = "jlens-qwen36"                        # gitignored clone: read only, never git
DEF_OUT = "results/raw/2026-10-08_note-N10-horn1.md"

RAW_DIAG = "results/raw/2026-08-06_dv_logit_projection_check.txt"
RAW_POW = "results/raw/2026-08-05_slice3_dv_powered.txt"
ARCH12 = "archive/RESULTS-cycle1-2.md"
LOCAL_JSON = "data/configs/dv_logit_projection_check.json"      # as the record names it
CLONE_JSON = f"{CLONE}/data/configs/dv_logit_projection_check.json"
CLONE_POW_JSON = f"{CLONE}/data/configs/slice3_dv_powered.json"
CLONE_DIAG_PY = f"{CLONE}/scripts/dv_logit_projection_check.py"
CLONE_POW_PY = f"{CLONE}/scripts/slice3_dv_powered.py"
CLONE_FP_PY = f"{CLONE}/jlens_qwen/fingerprint.py"

# ----------------------------------------------------------------- plumbing --

def git(*args: str) -> bytes:
    """Read-only git only, in the lab repo (never inside the clone)."""
    assert args[0] in ("show", "rev-parse", "log", "ls-tree", "check-ignore",
                       "cat-file"), args
    r = subprocess.run(["git", "--no-optional-locks", "-C", REPO, *args],
                       capture_output=True)
    if r.returncode != 0 and args[0] != "check-ignore":
        raise RuntimeError(f"git {args}: {r.stderr.decode()[:300]}")
    return r.stdout


_CACHE: dict[str, bytes] = {}


def pinned(path: str, rev: str = PIN) -> bytes:
    key = f"{rev}:{path}"
    if key not in _CACHE:
        _CACHE[key] = git("show", key)
    return _CACHE[key]


def ptext(path: str, rev: str = PIN) -> str:
    return pinned(path, rev).decode("utf-8")


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def cell(s) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


def lines(text: str) -> list[str]:
    """Lines as `git show <pin>:<path> | cat -n` numbers them: split on '\\n' only.
    str.splitlines() also splits on '\\r' (tqdm progress bars), '\\x0b', '\\x0c', '\\x1c'-'\\x1e',
    '\\x85', U+2028/U+2029, which drifts every later locator in a file that carries one."""
    return text.split("\n")


def find_lines(text: str, needle: str) -> list[int]:
    return [i + 1 for i, ln in enumerate(lines(text)) if needle in ln]


def line_of(text: str, needle: str, path: str) -> int:
    hits = find_lines(text, needle)
    assert len(hits) == 1, (path, needle, hits)
    return hits[0]


def quote(text: str, ln: int, width: int = 200) -> str:
    s = lines(text)[ln - 1].strip()
    return s if len(s) <= width else s[: width - 3] + "..."


# ------------------------------------------------------------- statistics --

def mean(v):
    return sum(v) / len(v)


def pearson(x, y) -> float:
    mx, my = mean(x), mean(y)
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    return sxy / math.sqrt(sxx * syy)


def avg_ranks(v):
    order = sorted(range(len(v)), key=lambda i: v[i])
    r = [0.0] * len(v)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
            j += 1
        for k in range(i, j + 1):
            r[order[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def n_tied(v) -> int:
    c = collections.Counter(v)
    return sum(m for m in c.values() if m > 1)


def logit(p: float) -> float:
    p = min(max(p, 1e-6), 1 - 1e-6)           # the producing script's clip
    return math.log(p / (1 - p))


def ols1(x, y):
    """Simple OLS y = a + b x; returns a, b, in-sample R^2, residuals, h_ii."""
    n = len(x)
    mx, my = mean(x), mean(y)
    sxx = sum((a - mx) ** 2 for a in x)
    b = sum((a - mx) * (c - my) for a, c in zip(x, y)) / sxx
    a = my - b * mx
    res = [c - (a + b * xi) for xi, c in zip(x, y)]
    sst = sum((c - my) ** 2 for c in y)
    r2 = 1 - sum(e * e for e in res) / sst
    h = [1 / n + (xi - mx) ** 2 / sxx for xi in x]
    return a, b, r2, res, h, sst


def loo_q2(x, y) -> tuple[float, float]:
    """Leave-one-out predictive R^2: by PRESS and by explicit refits."""
    a, b, r2, res, h, sst = ols1(x, y)
    press = sum((e / (1 - hi)) ** 2 for e, hi in zip(res, h))
    press2 = 0.0
    for i in range(len(x)):
        xs = x[:i] + x[i + 1:]
        ys = y[:i] + y[i + 1:]
        ai, bi, *_ = ols1(xs, ys)
        press2 += (y[i] - (ai + bi * x[i])) ** 2
    return 1 - press / sst, 1 - press2 / sst


def partial_r(y, s, x) -> float:
    """corr(y, s | x): residualize both on [1, x]."""
    _, _, _, ry, _, _ = ols1(x, y)
    _, _, _, rs, _, _ = ols1(x, s)
    return pearson(ry, rs)


def _betacf(a, b, x):
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1, a - 1
    c, d = 1.0, 1 - qab * x / qap
    d = 1 / (d if abs(d) > tiny else tiny)
    h = d
    for m in range(1, 400):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1 + aa * d
        d = 1 / (d if abs(d) > tiny else tiny)
        c = 1 + aa / c
        c = c if abs(c) > tiny else tiny
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1 + aa * d
        d = 1 / (d if abs(d) > tiny else tiny)
        c = 1 + aa / c
        c = c if abs(c) > tiny else tiny
        dl = d * c
        h *= dl
        if abs(dl - 1) < 1e-15:
            break
    return h


def betai(a, b, x):
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
                  + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return bt * _betacf(a, b, x) / a
    return 1 - bt * _betacf(b, a, 1 - x) / b


def t_two_sided_p(t: float, df: int) -> float:
    return betai(df / 2, 0.5, df / (df + t * t))


def fisher_ci(r: float, n: int, level=0.95):
    z = math.atanh(r)
    se = 1 / math.sqrt(n - 3)
    zc = NormalDist().inv_cdf(0.5 + level / 2)
    return math.tanh(z - zc * se), math.tanh(z + zc * se)


# ------------------------------------------------------------------ parse --

ROW_DIAG = re.compile(
    r"^\s*-(\d+)\s+strain=\s*([\d.]+) pkeep=([\d.]+) geoN=\s*([+-][\d.]+) "
    r"geoL=\s*([+-][\d.]+) empDL=\s*([+-][\d.]+) empPK=([\d.]+)")
ROW_POW = re.compile(r"^\s*-(\d+)\s+strain=\s*([\d.]+) pkeep=([\d.]+) conf=([\d.]+)")
REG = re.compile(r"^\s{2}(.+?)\s+r=([+-][\d.]+)\s+R\^2=([\d.]+)\s+log-odds r=([+-][\d.]+)"
                 r"\s+spearman=([+-][\d.]+)")


def parse_diag(text: str):
    rows, regs, partial, lowstrain = [], {}, None, None
    for i, ln in enumerate(lines(text), 1):
        m = ROW_DIAG.match(ln)
        if m:
            rk, st, pk, gn, gl, ed, ep = m.groups()
            rows.append(dict(rank=int(rk), strain=float(st), pkeep=float(pk),
                             geoN=float(gn), geoL=float(gl), empDL=float(ed),
                             empPK=float(ep), line=i, s_pkeep=pk, s_strain=st))
            continue
        m = REG.match(ln)
        if m:
            regs[m.group(1).strip()] = dict(r=float(m.group(2)), R2=float(m.group(3)),
                                            lo_r=float(m.group(4)), rho=float(m.group(5)),
                                            line=i)
            continue
        m = re.match(r"^\s*partial corr\(P\(keep\), strain \| (.+?)\) = ([+-][\d.]+)", ln)
        if m:
            partial = dict(given=m.group(1), value=float(m.group(2)), line=i)
            continue
        m = re.match(r"^\s*low-strain subgroup \(strain<=([\d.]+), n=(\d+)\): P\(keep\) "
                     r"SD=([\d.]+); r\(P\(keep\), (.+?)\)=([+-][\d.]+)", ln)
        if m:
            lowstrain = dict(cut=float(m.group(1)), n=int(m.group(2)), sd=float(m.group(3)),
                             pred=m.group(4), r=float(m.group(5)), line=i)
    return rows, regs, partial, lowstrain


def parse_pow(text: str):
    out = {}
    for i, ln in enumerate(lines(text), 1):
        m = ROW_POW.match(ln)
        if m:
            out[int(m.group(1))] = dict(strain=m.group(2), pkeep=m.group(3), line=i)
    return out


# ----------------------------------------------------------------- search --

RSQ_VAL = re.compile(r"(R²|R\^2|R2)\s*(?:[=≈:]|of)\s*[-+]?\d*\.\d+")
HAS_53 = re.compile(r"(?<![\d.])0?\.53(?:0)?(?![\d])|(?<![\d.])53\s?%")   # 0.53 / .53 / .530 / 53%
RSQ_TOK = re.compile(r"R²|R\^2|\bR2\b|r_squared|rsquared|\br2\b")


def search_docs(paths):
    """Lines with an R^2 carrying a value; and lines with 0.53/.530/53% next to an
    R^2 token, 'variance', 'horn' or 'contamination'; and horn+calib lines."""
    rsq_lines, l53, horn_cal = [], [], []
    for p in paths:
        try:
            t = ptext(p)
        except Exception:
            continue
        for i, ln in enumerate(lines(t), 1):
            if RSQ_VAL.search(ln):
                rsq_lines.append((p, i, ln.strip()))
            if HAS_53.search(ln) and re.search(r"R²|R\^2|\bR2\b|variance|horn|contaminat|calibrat",
                                              ln, re.I):
                l53.append((p, i, ln.strip()))
            if re.search(r"horn", ln, re.I) and re.search(r"calib", ln, re.I):
                horn_cal.append((p, i, ln.strip()))
    return rsq_lines, l53, horn_cal


CALIB_NEAR = re.compile(r"(?<![\d.])0?\.53(?!\d)|R²|R\^2|dv_logit|DV DIAGNOSTIC|two-horns|horn|post-mortem",
                        re.I)


def calib_window_scan(paths, half=5):
    """Paragraph-level: every line with 'calibrat' whose +-half-line window
    also carries 0.53 / R² / dv_logit / the DV diagnostic / horn / post-mortem."""
    hits = []
    for p in paths:
        try:
            t = lines(ptext(p))
        except Exception:
            continue
        for i, ln in enumerate(t):
            if re.search(r"calibrat", ln, re.I):
                win = " ".join(t[max(0, i - half): i + half + 1])
                if CALIB_NEAR.search(win):
                    hits.append((p, i + 1, ln.strip()))
    return hits


KEY_RSQ = re.compile(r"(^|_)(r2|rsq|r_squared|rsquared)($|_)|calib|horn", re.I)


def walk_json(o, path, keys_hit, num53):
    if isinstance(o, dict):
        for k, v in o.items():
            if KEY_RSQ.search(k):
                keys_hit[path + "." + k] += 1
            walk_json(v, path + "." + k, keys_hit, num53)
    elif isinstance(o, list):
        for v in o:
            walk_json(v, path + "[]", keys_hit, num53)
    elif num53 is not None and isinstance(o, float) and 0.525 <= o < 0.535:
        num53[path] += 1


# ------------------------------------------------------------------- main --

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEF_OUT)
    ap.add_argument("--json-out", default="",
                    help="optional; not written unless given (N10's assigned output is the .md)")
    ap.add_argument("--prev", default="",
                    help="optional, read-only: a previous version of this raw; the values-check compares "
                         "its numbers with this run's")
    args = ap.parse_args()

    O: list[str] = []
    w = O.append
    J: dict = {}

    stamp = subprocess.run(["date", "-u"], capture_output=True, text=True).stdout.strip()
    head = git("rev-parse", "HEAD").decode().strip()
    pin_full = git("rev-parse", PIN).decode().strip()
    block = pinned(BLOCK)
    block_sha = sha256(block)
    me = os.path.abspath(__file__)
    my_sha = sha256(open(me, "rb").read())
    cmd = " ".join(shlex.quote(a) for a in [sys.executable, os.path.relpath(me, REPO)] + sys.argv[1:])
    btext = block.decode()
    n10_lo = line_of(btext, "### N10. Horn-1 calibration", BLOCK)

    w("# AUDIT-note-release v1.2 -- N10: Horn-1 calibration R² = 0.53")
    w("")
    w(f"- Code stamp: {stamp} (date -u)  [run metadata]")
    w(f"- HEAD at run time: {head}  [run metadata; every record read below is pinned to {PIN}]")
    w(f"- Command: `{cmd}`  [run metadata; cwd-independent]")
    w(f"- Pin: {PIN} = {pin_full}")
    w(f"- Block: `{BLOCK}`@{PIN} sha256 `{block_sha}` "
      f"({'MATCH' if block_sha == BLOCK_SHA else 'MISMATCH'} vs routed 8cd8a9ac...3841); "
      f"item N10 = block lines {n10_lo}-{n10_lo + 1}")
    w(f"- Script: `scripts/audit_note_N10.py` sha256 `{my_sha}`")
    w(f"- Interpreter: {sys.executable} (Python {sys.version.split()[0]}); stdlib only "
      f"(math, statistics, statistics.NormalDist); numpy not imported; no scipy/sklearn; no model; no randomness")
    w("")
    w("Status vocabulary: reproduced (computed here from committed JSON/JSONL/npz) | log-only "
      "(exists in the record only as log prose or printed stdout; pinned locator) | not found | "
      "discrepant | computed-new (a computation this item adds; post-hoc, labeled). Locators are "
      f"`path@{PIN}:line` as in `git show {PIN}:<path>`.")
    w("")
    w("The block's N10 text (verbatim, for the record):")
    w("")
    for ln in lines(btext)[n10_lo - 1: n10_lo + 1]:
        w(f"> {ln}")
    w("")
    assert block_sha == BLOCK_SHA

    # ------------------------------------------------------ 1. search ------
    w("## 1. Locating the figure (search over the pinned record)")
    w("")
    tree = git("ls-tree", "-r", "--name-only", PIN).decode().splitlines()
    docs = [p for p in tree if (p.endswith(".md") and "/" not in p)
            or (p.startswith("archive/") and p.endswith(".md"))]
    raws = [p for p in tree if p.startswith("results/raw/") and p.endswith((".txt", ".md"))]
    jsons = [p for p in tree if (p.startswith("data/e2b/") or p.startswith("data/e2d/"))
             and p.endswith(".json")]
    all_json = [p for p in tree if p.endswith((".json", ".jsonl"))]
    all_text = [p for p in tree if p.endswith((".md", ".txt"))]
    w(f"Search scope at {PIN}: {len(docs)} tracked markdown files at root and in archive/ "
      f"(includes RESULTS.md, archive/RESULTS-cycle1-2.md, archive/RESULTS-cycles3-4.md, FINDINGS*.md, "
      f"PROPOSAL-*.md, LOCK-h.md, ADDENDUM-g1-archival-reading-screen.md); {len(raws)} tracked "
      f"results/raw/*.txt|*.md. Patterns: an R²/R^2/R2 token followed by a value (`{RSQ_VAL.pattern}`); "
      f"0.53/.53/.530 or 53% (`{HAS_53.pattern}`) on a line that also carries R², 'variance', 'horn', "
      f"'contamination' or 'calibration'. Line numbers count '\\n' only, as `git show {PIN}:<path> | cat -n` "
      f"does. "
      f"The 'calibration' term (1c) is searched at paragraph level over every tracked *.md|*.txt at the pin "
      f"({len(all_text)} files). JSON (1d): R²-like keys (r2/rsq/r_squared/calib*/horn*) over every tracked "
      f"*.json|*.jsonl at the pin ({len(all_json)} files); floats in [0.525, 0.535) by key path over the "
      f"{len(jsons)} tracked data/e2b/*.json and data/e2d/*.json (the h arc's and e2d's artifacts).")
    w("")
    for p in ("ADDENDUM-g1-archival-reading-screen.md", "PROPOSAL-h-state-present-choice.md", "LOCK-h.md"):
        assert p in tree, p
    rsq, l53, hc = search_docs(docs + raws)
    w(f"### 1a. Every line in scope with an R² carrying a value ({len(rsq)} lines)")
    w("")
    w("| locator | text (truncated) |")
    w("|---|---|")
    for p, i, s in rsq:
        w(f"| {p}@{PIN}:{i} | {cell(s[:170])} |")
    w("")
    w(f"### 1b. Lines with 0.53 or 53% beside R²/variance/horn/contamination/calibration ({len(l53)} lines)")
    w("")
    w("| locator | text (truncated) |")
    w("|---|---|")
    for p, i, s in l53:
        w(f"| {p}@{PIN}:{i} | {cell(s[:170])} |")
    w("")
    w(f"### 1c. The term 'calibration' near horn 1, R² or the diagnostic")
    w("")
    w(f"Line-level, 'horn' and 'calib' on one line: {len(hc)} "
      + "; ".join(f"`{p}@{PIN}:{i}`" for p, i, _ in hc)
      + " (the block's own heading only). A line-level search misses paragraphs, so the term is also "
        "searched at paragraph level: every line with 'calibrat' whose ±5-line window carries 0.53, R², "
        "dv_logit, 'DV DIAGNOSTIC', 'horn' or 'post-mortem'.")
    w("")
    cw = calib_window_scan(all_text)
    w(f"Paragraph-level hits: {len(cw)} lines.")
    w("")
    w("| locator | text (truncated) |")
    w("|---|---|")
    for p, i, s_ in cw:
        w(f"| {p}@{PIN}:{i} | {cell(s_[:150])} |")
    w("")
    # pinned needles for the reading below (each asserted unique at the pin)
    ph_t = ptext("PROPOSAL-h-state-present-choice.md")
    lh_t = ptext("LOCK-h.md")
    f5_t = ptext("FINDINGS-5.md")
    pe_t = ptext("PROPOSAL-e-reward-axis-hijack.md")
    ho_t = ptext("HANDOFF-2026-08-22.md")
    f2_t = ptext("FINDINGS-2.md")
    a12_t = ptext(ARCH12)
    C = dict(
        ph_tier=line_of(ph_t, "## 2. H-calibration tier", "PROPOSAL-h"),
        ph_h1=line_of(ph_t, "in-vivo quantification of horn 1", "PROPOSAL-h"),
        lh_136=line_of(lh_t, "# The v1.x record (H-calibration tier)", "LOCK-h"),
        lh_153=line_of(lh_t, "H-calibration tier. A v2 follows H-cal", "LOCK-h"),
        f5_6=line_of(f5_t, "the PROPOSAL-h calibration arc", "FINDINGS-5"),
        f5_99=line_of(f5_t, "## 3. The h-calibration", "FINDINGS-5"),
        f5_103=line_of(f5_t, "the entire calibration arc", "FINDINGS-5"),
        f5_pid=line_of(f5_t, "of record passed by low-discordance certification: N = 640, π̂_d =", "FINDINGS-5"),
        f5_horn=line_of(f5_t, "**Horn 1 is quantified and de minimis under shields**", "FINDINGS-5"),
        ho_32=line_of(ho_t, "the whole PROPOSAL-h/e2b H-calibration", "HANDOFF-2026-08-22"),
        pe_gate=line_of(pe_t, "the empirical variant of the logit-projection", "PROPOSAL-e"),
        pe_pm=line_of(pe_t, "fixed; threshold set from the (b) post-mortem", "PROPOSAL-e"),
        pe_247=line_of(pe_t, "**Two-horns leakage.** Standing gate above; (b)'s post-mortem is the", "PROPOSAL-e"),
        pe_248=line_of(pe_t, "calibration source.", "PROPOSAL-e"),
    )
    assert lines(f5_t)[C["f5_pid"]].startswith("0.0172, CI [.0086, .0305]")
    # e2a's g3 KV-leakage gate: the two-horns standing gate's instance on the reward axis (round-2 finding 3)
    a34_t = ptext("archive/RESULTS-cycles3-4.md")
    v2_t = ptext("archive/CLAUDE-v2-cycles3-4.md")
    f3_t = ptext("FINDINGS-3.md")
    cm_t = ptext("CLAUDE.md")
    G3 = dict(
        v2_rule5=line_of(v2_t, "5. **Two-horns standing gate for any choice readout:**", "CLAUDE-v2"),
        v2_rule5b=line_of(v2_t, "empirical logit-projection leakage check (choice-token logit shift from",
                          "CLAUDE-v2"),
        v2_rule5_src=line_of(v2_t, "*(FINDINGS-2, (b) post-mortem + two-horns finding.)*", "CLAUDE-v2"),
        drug=line_of(a34_t, "**Drug (fixed):** span-mean reward axis (`e0_axes.npz`, sha", "RESULTS-cycles3-4"),
        drug_L=line_of(a34_t, "`d4791bdc4877da3d`), L48; candidate fracs {0.10, 0.20} only (0.40",
                       "RESULTS-cycles3-4"),
        prereg=line_of(a34_t, "**g3 — KV-leakage gate (rule 5) at dose_e2a:**", "RESULTS-cycles3-4"),
        prereg_bar=line_of(a34_t, "choice position; **max |Δ| ≤ 0.10** (≈ ≤2.5% choice-probability",
                           "RESULTS-cycles3-4"),
        entry=line_of(a34_t, "2026-08-09 — **e2a g3 — KV-LEAKAGE GATE FAIL.", "RESULTS-cycles3-4"),
        value=line_of(a34_t, "**max |Δ(logit_A − logit_B)| = 0.5368 (gate ≤ 0.10; 5.4× over);",
                      "RESULTS-cycles3-4"),
        f3=line_of(f3_t, "disqualified for this axis at dose ≥ 0.20 (measured 0.537-logit", "FINDINGS-3"),
        rule5d=line_of(cm_t, "(d) **persistent-KV session readouts disqualified** at dose ≥ 0.20", "CLAUDE.md"),
    )
    g3j = json.loads(pinned("data/e2a/g3_kv_leakage.json"))
    g3_rows = g3j["rows"]
    g3_max = max(abs(r_["delta"]) for r_ in g3_rows)
    g3_mean = mean([abs(r_["delta"]) for r_ in g3_rows])
    assert len(g3_rows) == 32 and abs(g3_max - g3j["max_abs"]) < 1e-5 and abs(g3_mean - g3j["mean_abs"]) < 1e-5
    assert g3j["dose"] == 0.2 and g3j["gate"] == 0.1 and g3j["pass"] is False
    J["g3_homonym"] = dict(locators=G3, max_abs=g3j["max_abs"], mean_abs=g3j["mean_abs"],
                           recomputed_max=g3_max, recomputed_mean=g3_mean, n_rows=len(g3_rows),
                           dose=g3j["dose"], gate=g3j["gate"])
    pe_date = git("log", "--diff-filter=A", "--format=%h %ad", "--date=short", PIN, "--",
                  "PROPOSAL-e-reward-axis-hijack.md").decode().strip()
    ph_date = git("log", "--diff-filter=A", "--format=%h %ad", "--date=short", PIN, "--",
                  "PROPOSAL-h-state-present-choice.md").decode().strip()
    e_lo = line_of(a12_t, "2026-08-06 — **(b) DV DIAGNOSTIC: the keep/switch retention DV is", ARCH12)
    e_hi = line_of(a12_t, "saved `data/configs/dv_logit_projection_check.json` (local).", ARCH12)
    n_cal_f2 = len(re.findall(r"calibration", f2_t, re.I))
    n_cal_entry = sum(1 for ln in lines(a12_t)[e_lo - 1: e_hi] if re.search(r"calibrat", ln, re.I))
    J["calibration_term"] = dict(window_hits=[f"{p}:{i}" for p, i, _ in cw], pinned=C,
                                 findings2_calibration_count=n_cal_f2, entry_calibrat_count=n_cal_entry)
    w("Reading (Code): the record attaches 'calibration' to two different things.")
    w(f"- **The PROPOSAL-h H-calibration tier** (the h arc; PROPOSAL-h added {ph_date}): "
      f"`PROPOSAL-h-state-present-choice.md@{PIN}:{C['ph_tier']}` ('## 2. H-calibration tier'), with "
      f"H1's paired-shadow per-read leak called 'the direct in-vivo quantification of horn 1' (:{C['ph_h1']}); "
      f"`LOCK-h.md@{PIN}:{C['lh_136']}`, `:{C['lh_153']}`; `FINDINGS-5.md@{PIN}:{C['f5_6']}` ('the PROPOSAL-h "
      f"calibration arc'), `:{C['f5_99']}` ('## 3. The h-calibration'), `:{C['f5_103']}` ('the entire "
      f"calibration arc exists to bound that horn'), `:{C['f5_pid']}-{C['f5_pid'] + 1}` (π̂_d = 0.0172), "
      f"`:{C['f5_horn']}` "
      f"('Horn 1 is quantified and de minimis under shields'); `HANDOFF-2026-08-22.md@{PIN}:{C['ho_32']}`. "
      f"That tier's horn-1 quantities are paired-shadow statistics on the reward axis at frac 0.10 (π̂_d, a "
      f"pick-discordance rate, and the directional-leak family), N6's domain "
      f"(`results/raw/2026-10-08_note-N6-e2b.md` §3). The horn-1 figures FINDINGS-5 gives there (π̂_d = "
      f"0.0172 and 0.0208; the L family at ≤ 3% of the bar) are rates, not R² values.")
    w(f"- **The cycle-2 diagnostic as a calibration source.** `PROPOSAL-e-reward-axis-hijack.md@{PIN}:"
      f"{C['pe_247']}-{C['pe_248']}` (added {pe_date}): 'Two-horns leakage. Standing gate above; (b)'s "
      f"post-mortem is the calibration source.' The standing gate it points to is 'the empirical variant of "
      f"the logit-projection check ... threshold set from the (b) post-mortem' (:{C['pe_gate']}-{C['pe_pm']}). "
      f"So the record does use the term for this diagnostic, as the source a later gate's threshold is set from. "
      f"That standing gate has an instance with a value near 0.53. The v2 operative rule 5 is the 'Two-horns "
      f"standing gate for any choice readout', whose part (b) is 'the empirical logit-projection leakage check "
      f"(choice-token logit shift from steered context, content held fixed)', sourced to '(b) post-mortem + "
      f"two-horns finding' (`archive/CLAUDE-v2-cycles3-4.md@{PIN}:{G3['v2_rule5']}-{G3['v2_rule5_src']}`). "
      f"e2a pre-registered it as 'g3 — KV-leakage gate (rule 5)', with max |Δ| ≤ 0.10 "
      f"(`archive/RESULTS-cycles3-4.md@{PIN}:{G3['prereg']}-{G3['prereg_bar'] + 1}`), on the span-mean reward axis "
      f"at L48 (`:{G3['drug']}-{G3['drug_L']}`). g3 measured max |Δ(logit_A − logit_B)| = 0.5368 "
      f"(`:{G3['value']}`). That value is stored in committed JSON, `data/e2a/g3_kv_leakage.json`@{PIN} "
      f"`max_abs` = {g3j['max_abs']!r}; the max |delta| over its {len(g3_rows)} rows recomputes to "
      f"{g3_max:.5f} (rows stored at 5 d.p.), at dose {g3j['dose']}. FINDINGS-3 banks it as a '0.537-logit "
      f"live-KV leak' (`FINDINGS-3.md@{PIN}:{G3['f3']}`), and the current ledger carries it as rule 5(d) "
      f"(`CLAUDE.md@{PIN}:{G3['rule5d']}`). It is a logit difference from steered KV context at the choice "
      f"position, not an R², and it is not the diagnostic's number. A reader who follows 'the calibration "
      f"source' thread lands on this ≈ 0.54 two-horns figure. The §1d float scan would not catch it: it "
      f"covers e2b/e2d only, over [0.525, 0.535). It is listed in the Figures table as a homonym.")
    w(f"- The diagnostic's own entry (`{ARCH12}@{PIN}:{e_lo}-{e_hi}`) uses 'calibrat' on {n_cal_entry} lines, "
      f"and `FINDINGS-2.md@{PIN}` uses 'calibration' {n_cal_f2} times. They call it the '(b) DV DIAGNOSTIC' / "
      f"route (b)'s post-mortem.")
    other_w = [f"{p}@{PIN}:{i}" for p, i, _ in cw
               if not (p in ("AUDIT-note-release-v1_2.md", "FINDINGS-5.md", "PROPOSAL-e-reward-axis-hijack.md",
                             "PROPOSAL-h-state-present-choice.md"))]
    assert [x.split("@")[0] for x in other_w] == ["archive/RESULTS-cycles3-4.md",
                                                  "results/raw/2026-10-05_m-v1.9_referent_check.txt"], other_w
    w(f"- The other paragraph-level hits are unrelated uses of the word: {', '.join(f'`{x}`' for x in other_w)} "
      f"(control tags that 'cannot calibrate' the weight-channel leak; a runtime projection 'calibrated to "
      f"reproduce' a wall-clock).")
    w("- Consequence: 'horn-1 calibration' (the block's heading, the preprint's :192) reads naturally as the "
      "h arc's tier, which is the record's measurement of horn 1 (PROPOSAL-h §2; FINDINGS-5 §3). The number "
      "is the cycle-2 one (§2). A reader who follows 'calibration' into the record lands on the H-calibration "
      "tier, whose horn-1 result is a different statistic. N1 keeps this row apart from N6's horn-1 figures.")
    w("")
    keys_hit, num53 = collections.Counter(), collections.Counter()
    for p in jsons:
        walk_json(json.loads(pinned(p)), p + ":", keys_hit, num53)
    keys_all = collections.Counter()
    unparsed = []
    for p in all_json:
        try:
            b_ = pinned(p)
            if p.endswith(".jsonl"):
                for ln in lines(b_.decode("utf-8")):
                    if ln.strip():
                        walk_json(json.loads(ln), p + ":", keys_all, None)
            else:
                walk_json(json.loads(b_), p + ":", keys_all, None)
        except Exception as e:  # report, never hide
            unparsed.append((p, str(e)[:80]))
    by_file_leaf = collections.Counter()
    for k, c in keys_all.items():
        by_file_leaf[(k.split(":")[0], k.split(".")[-1])] += c
    L_rmask = line_of(ptext("RESULTS.md"), "(c) RETENTION — single-round masks, target = that round's pole.",
                      "RESULTS.md")
    w(f"### 1d. JSON")
    w("")
    w(f"- R²-like keys over every tracked *.json|*.jsonl at {PIN} ({len(all_json)} files, "
      f"{sum(p.endswith('.jsonl') for p in all_json)} of them JSONL; unparsed: {unparsed}): "
      f"{sum(keys_all.values())} occurrences, all under data/echo/: "
      + ", ".join(f"`{f}` :: `{k}` x{c}" for (f, k), c in sorted(by_file_leaf.items())) + ".")
    w(f"  They are homonyms. 'R2' there is round 2 of the echo recon's single-round masks R1-R4 "
      f"(`RESULTS.md@{PIN}:{L_rmask}`): per-session masks and distances, `.leak.R2` "
      f"({{pi_d, n_flips, n, ...}}), `.retention.R2`, and the probe families named for it (c_R2_roundpole, "
      f"cb_R2_roundpole_TEXTONLY_shadow; their R1/R3/R4 siblings do not match the pattern). None is a "
      f"coefficient of determination. Outside data/echo/: "
      f"{sum(c for (f, _), c in by_file_leaf.items() if not f.startswith('data/echo/'))}.")
    J["json_keys_all"] = {f"{f}::{k}": c for (f, k), c in by_file_leaf.items()}
    w(f"- data/e2b + data/e2d ({len(jsons)} files), R²-like keys: {sum(keys_hit.values())}"
      + (f" {dict(keys_hit)}" if keys_hit else ""))
    leaf = collections.Counter()
    for k, c in num53.items():
        leaf[re.sub(r"\[\]$", "", k.split(".")[-1])] += c
    nfiles = len({k.split(":")[0] for k in num53})
    w(f"- Floats in [0.525, 0.535): {sum(num53.values())} in {nfiles} files under {len(num53)} key paths; "
      f"by leaf key: " + ", ".join(f"`{k}` x{c}" for k, c in leaf.most_common()) + ".")
    w("  Full key-path list:")
    for k, c in num53.most_common():
        w(f"  - `{k}` x{c}")
    w("")
    w("Reading of the search (Code): every line in 1a/1b that carries R² = 0.53 (or '~53% of its variance') belongs to ONE "
      "measurement -- the cycle-2 `(b) DV DIAGNOSTIC` of 2026-08-06 (`dv_logit_projection_check`) -- "
      "and its downstream citations (FINDINGS-2, PROPOSAL-h §1). Neither ADDENDUM-g1 nor any other "
      "PROPOSAL-h-arc document (PROPOSAL-h beyond its one citation, LOCK-h) computes it; no tracked JSON/JSONL "
      "carries an R² field (1d: the only R²-like keys are data/echo's round-2 mask names), and the e2b/e2d "
      "0.53-valued floats are per-read label probabilities "
      "(p_a / p_b / label_mass), stored-classifier parameters (mu / sd), AUCs, split fractions and "
      "per-probe values -- none is an R²; homonyms. The other R² lines in 1a are this block's own heading or "
      "different quantities: the 2026-08-04 slice-2 gating regressions on strain (think_instr, fact_struct, "
      "conf; cycle 2) and the geometric arms of the same diagnostic. "
      "archive/RESULTS-cycles3-4.md's 'mean 0.53' (the (d) leak's mean |Δ|, 2026-08-10) is a "
      "homonym found in exploration and is listed in the Figures table so N1 does not pick it up; so is "
      "e2a g3's max |Δ(logit_A − logit_B)| = 0.5368 (§1c).")
    w("")
    J["search"] = dict(rsq_lines=[f"{p}:{i}" for p, i, _ in rsq], l53=[f"{p}:{i}" for p, i, _ in l53],
                       horn_calib=[f"{p}:{i}" for p, i, _ in hc], json_keys=dict(keys_hit),
                       json_num53=dict(num53))

    # -------------------------------------------- 2. record locators -------
    w("## 2. The figure's record of entry")
    w("")
    a12 = ptext(ARCH12)
    L_emp = line_of(a12, "**Empirical final-position-only arm (decisive): r = +0.728, R² = 0.530.**", ARCH12)
    L_head = line_of(a12, "2026-08-06 — **(b) DV DIAGNOSTIC: the keep/switch retention DV is", ARCH12)
    L_geo = line_of(a12, "**Geometric (linearized J-lens) arms: r ≈ +0.25, R² ≈ 0.06**", ARCH12)
    L_alpha = line_of(a12, "full-norm vector (α = R ≈ 102, ≈ the whole residual stream) at the decision", ARCH12)
    L_n33 = line_of(a12, "(`scripts/dv_logit_projection_check.py`, n=33 stored powered-DV records;", ARCH12)
    L_recon = line_of(a12, "(reconstructed final-pos-only P(keep) vs stored: r = +0.725; Spearman", ARCH12)
    L_low = line_of(a12, "+0.68; log-odds r +0.72). In the motivating low-strain subgroup,", ARCH12)
    L_part = line_of(a12, "partial corr(P(keep), strain |", ARCH12)
    L_47 = line_of(a12, "Honest residual: the ~47% unexplained is the all-positions-minus-final-pos", ARCH12)
    L_json = line_of(a12, "saved `data/configs/dv_logit_projection_check.json` (local).", ARCH12)
    L_sum = line_of(a12, "R² = 0.53 of stored P(keep) (r = +0.71 in the low-strain subgroup); the", ARCH12)
    L_pow = line_of(a12, "2026-08-05 — **§5 covariate route (b), POWERED DV estimate (n=33): clean,", ARCH12)
    L_pow2 = line_of(a12, "confidence profiled across 33 strain-spanning English configs (frac=1.0, −2", ARCH12)
    L_tail = line_of(a12, "(tail-PCA directions at L48).", ARCH12)
    L_smoke = line_of(a12, "decision → not the propagation-failure case), P(keep) over 5 contexts × both", ARCH12)
    L_horns = line_of(a12, "DV faces two horns — state active at the readout → direct logit", ARCH12)
    f2 = ptext("FINDINGS-2.md")
    F2_title = 1
    F2_129 = line_of(f2, "instrument — final-position contamination, R² = 0.53", "FINDINGS-2.md")
    F2_175 = line_of(f2, "state never present over the context — reproduces r = +0.728, R² = 0.530**", "FINDINGS-2.md")
    F2_244 = line_of(f2, "the decision logits directly (route (b): R² = 0.53 from the final", "FINDINGS-2.md")
    F2_horns = line_of(f2, "1. **The two-horns result.**", "FINDINGS-2.md")
    ph = ptext("PROPOSAL-h-state-present-choice.md")
    PH_65 = line_of(ph, "(C2: R² = .53)", "PROPOSAL-h")
    ph_c2 = [i for i, ln in enumerate(lines(ph), 1) if re.search(r"\bC2\b", ln)]
    F2_51 = line_of(f2, "but a diagnostic showed **~53% of its variance is reproduced by injecting", "FINDINGS-2.md")
    F2_its = line_of(f2, "- **(b) Covariate-route retention DV** (P(keep) with the config active at", "FINDINGS-2.md")
    assert F2_its == F2_51 - 2, (F2_its, F2_51)
    rd = ptext(RAW_DIAG)
    RD_50 = line_of(rd, "empirical dlogit (final-pos)   r=+0.728  R^2=0.530", RAW_DIAG)
    rp = ptext(RAW_POW)
    entry_commit = git("log", "--diff-filter=A", "--format=%H %ad", "--date=iso", PIN, "--",
                       RAW_DIAG).decode().split()
    ec = entry_commit[0]
    ec_date = " ".join(entry_commit[1:])
    ec_results = ptext("RESULTS.md", ec)
    EC_L = find_lines(ec_results, "**Empirical final-position-only arm (decisive): r = +0.728, R² = 0.530.**")
    same_text = (quote(ec_results, EC_L[0], 999) == quote(a12, L_emp, 999)) if EC_L else False
    pow_commit = git("log", "--diff-filter=A", "--format=%h %ad", "--date=short", PIN, "--",
                     RAW_POW).decode().strip()
    w(f"- **Primary locator:** `{ARCH12}@{PIN}:{L_emp}` -- \"{quote(a12, L_emp)}\" "
      f"(entry header :{L_head}; dated 2026-08-06; cycle 2).")
    w(f"- **Printed stdout of the run:** `{RAW_DIAG}@{PIN}:{RD_50}` -- \"{quote(rd, RD_50)}\".")
    w(f"- **Entered the record at** commit `{ec[:7]}` ({ec_date}), which added the raw and the RESULTS.md "
      f"entry (then `RESULTS.md:{EC_L[0] if EC_L else '?'}` at `{ec[:7]}`; text identical to the archive "
      f"line: {same_text}). RESULTS.md was later moved to `{ARCH12}` by the restructure.")
    w(f"- **Summary carriers:** `{ARCH12}@{PIN}:{L_sum}` (\"{quote(a12, L_sum, 120)}\"); "
      f"`FINDINGS-2.md@{PIN}:{F2_51}`, `:{F2_129}`, `:{F2_175}`, `:{F2_244}` (the two-horns result, :{F2_horns}); "
      f"`PROPOSAL-h-state-present-choice.md@{PIN}:{PH_65}` (\"{quote(ph, PH_65, 120)}\").")
    w(f"- **FINDINGS-2:{F2_51}** carries the figure as a percentage: \"{quote(f2, F2_51, 120)}\". The "
      f"variance is the DV's, not a logit's: 'its' is the '(b) Covariate-route retention DV (P(keep) with the "
      f"config active at' the decision (`FINDINGS-2.md@{PIN}:{F2_its}-{F2_its + 1}`). That reading supports PI "
      f"note (a) below.")
    F2_win = line_of(f2, "line on this model. 2026-08-07. Covers the `RESULTS.md` entries from", "FINDINGS-2.md")
    assert "second design cycle" in lines(f2)[F2_title - 1]
    assert "through 2026-08-06" in lines(f2)[F2_win]
    w(f"- **'C2' in PROPOSAL-h:{PH_65}** is not defined anywhere in PROPOSAL-h (lines with a bare `C2` token: "
      f"{ph_c2}). Code reads it as 'cycle 2': FINDINGS-2's title calls it the 'second design cycle' "
      f"(`FINDINGS-2.md@{PIN}:{F2_title}`), and its window, 2026-08-01 through 2026-08-06 "
      f"(`FINDINGS-2.md@{PIN}:{F2_win}-{F2_win + 1}`), contains the diagnostic. "
      f"This is Code's reading, not a record statement.")
    w(f"- **The design seat's belief, checked:** the number is not computed in the PROPOSAL-h arc "
      f"(PROPOSAL-h:{PH_65} cites it; LOCK-h does not compute it) nor in ADDENDUM-g1 (no R²/0.53 line, §1). "
      f"It is a cycle-2 measurement on Qwen3.6-27B (`FINDINGS-2.md@{PIN}:{F2_title}`), before Phase 2 and "
      f"the reward axis. The belief does have a basis in the term. In the record, 'calibration' next to "
      f"horn 1 names the PROPOSAL-h H-calibration tier (§1c), and that tier's horn-1 result is a different "
      f"statistic (N6). The record also calls this cycle-2 post-mortem 'the calibration source' for a later "
      f"gate (PROPOSAL-e, §1c). So the term points at the h arc, and the number comes from cycle 2.")
    w("")
    J["locators"] = dict(primary=f"{ARCH12}@{PIN}:{L_emp}", raw=f"{RAW_DIAG}@{PIN}:{RD_50}",
                         entry_commit=ec, entry_date=ec_date, summary=f"{ARCH12}@{PIN}:{L_sum}",
                         findings2=[F2_51, F2_129, F2_175, F2_244], proposal_h=PH_65)

    # ------------------------------------------- 3. artifact status --------
    w("## 3. Is there a committed machine-readable artifact?")
    w("")
    in_tree = [p for p in tree if "dv_logit_projection_check" in p or "slice3_dv" in p
               or "usable_strain" in p]
    hist = git("log", "--all", "--format=%h", "--name-only", "--",
               "*dv_logit_projection_check*", "*slice3_dv*", "*usable_strain*").decode()
    hist_files = sorted({ln for ln in hist.splitlines() if "/" in ln})
    # check-ignore reads the working tree's .gitignore; the rule it names is then verified AT THE PIN
    ign = git("check-ignore", "-v", "--no-index", LOCAL_JSON).decode().strip()
    m_ign = re.match(r"^(.+?):(\d+):(.+?)\t(.+)$", ign)
    assert m_ign and m_ign.group(1) == ".gitignore" and m_ign.group(4) == LOCAL_JSON, ign
    ign_ln, ign_pat = int(m_ign.group(2)), m_ign.group(3)
    gi_pin = lines(ptext(".gitignore"))
    gi_wt = lines(open(os.path.join(REPO, ".gitignore"), encoding="utf-8").read())
    assert gi_pin[ign_ln - 1] == ign_pat == gi_wt[ign_ln - 1], (ign_ln, ign_pat)
    gi_pin_dv = [i for i, ln in enumerate(gi_pin, 1) if "dv_logit" in ln or "slice3_dv" in ln]
    assert gi_pin_dv == [], gi_pin_dv           # no allowlist entry re-includes it at the pin
    gi_clone = gi_pin.index(f"/{CLONE}/") + 1
    gi_pin_n = len(gi_pin) - (1 if gi_pin[-1] == "" else 0)      # lines as `wc -l` / `cat -n` count them
    gi_wt_n = len(gi_wt) - (1 if gi_wt[-1] == "" else 0)
    gi_first_diff = next((i for i, (a_, b_) in enumerate(zip(gi_pin, gi_wt), 1) if a_ != b_),
                         min(len(gi_pin), len(gi_wt)) + 1)
    J["gitignore"] = dict(rule_line=ign_ln, pattern=ign_pat, pin_lines=gi_pin_n, wt_lines=gi_wt_n,
                          same_line_at_pin_and_wt=True, clone_line=gi_clone)
    w(f"- Paths at {PIN} matching dv_logit_projection_check / slice3_dv / usable_strain: {in_tree}")
    w(f"- Every path ever committed on any ref matching those names: {hist_files}")
    w(f"- `{LOCAL_JSON}` (the record's own name for the saved JSON, `{ARCH12}@{PIN}:{L_json}`, "
      f"marked '(local)') is gitignored in this repo: `.gitignore@{PIN}:{ign_ln}` (`{cell(ign_pat)}`). "
      f"`git check-ignore -v` names that rule from the working tree; the same line reads the same at {PIN}. No "
      f"line of the pinned .gitignore names dv_logit or slice3_dv, so no allowlist entry re-includes the file "
      f"({gi_pin_n} lines at {PIN}, {gi_wt_n} in the working tree). The producing scripts ran from the "
      f"gitignored `{CLONE}/` clone, whose files are never in this repository (`.gitignore@{PIN}:{gi_clone}`, "
      f"`/{CLONE}/`).")
    w("- **Consequence under the block's rule 2:** no committed JSON/JSONL/npz carries the per-direction "
      "values, so R² = 0.53 cannot be `reproduced`; it is **log-only**. What the pin does carry is the "
      "run's printed stdout, with all 33 per-direction (strain, stored P(keep), empirical Δlogit) rows at "
      "print precision; §4 recomputes from those as a post-hoc consistency check.")
    w("")
    J["artifact"] = dict(in_tree=in_tree, ever_committed=hist_files, gitignore=f".gitignore@{PIN}:{ign_ln}")

    # ------------------------------------------- 4. recompute (raw) --------
    rows, regs, partial, lowstrain = parse_diag(rd)
    prow = parse_pow(rp)
    assert len(rows) == 33, len(rows)
    w("## 4. Post-hoc recomputation from the committed raw's printed table (computed-new)")
    w("")
    w(f"Input: the 33 per-direction lines of `{RAW_DIAG}@{PIN}:{rows[0]['line']}-{rows[-1]['line']}` "
      f"(stored P(keep) and empirical final-position Δlogit printed to 3 decimals, strain to 2). "
      f"This is printed stdout, not JSON: these numbers check the log's arithmetic at print precision; "
      f"they do not upgrade the figure's status.")
    w("")
    mism = [r["rank"] for r in rows if r["rank"] not in prow
            or prow[r["rank"]]["pkeep"] != r["s_pkeep"] or prow[r["rank"]]["strain"] != r["s_strain"]]
    w(f"- Stored-DV column cross-check: the diagnostic's printed `pkeep` and `strain` against the powered "
      f"DV run's own printout (`{RAW_POW}@{PIN}:{min(v['line'] for v in prow.values())}-"
      f"{max(v['line'] for v in prow.values())}`, commit {pow_commit}): {len(prow)} rows there, "
      f"{33 - len(mism)}/33 rank-matched rows string-identical; mismatching ranks: {mism}.")
    y = [r["pkeep"] for r in rows]
    x = [r["empDL"] for r in rows]
    xp = [r["empPK"] for r in rows]
    s = [r["strain"] for r in rows]
    gN = [r["geoN"] for r in rows]
    gL = [r["geoL"] for r in rows]
    n = len(rows)
    preds = [("geometric-normed", gN, False), ("geometric-linear", gL, False),
             ("empirical dlogit (final-pos)", x, False), ("empirical P(keep) (final-pos)", xp, True)]
    w("")
    w("| predictor of stored P(keep) (n = 33 directions) | r (log) | r (recomputed) | R² (log) | "
      "R² (recomputed) | log-odds r (log / recomputed) | Spearman (log / recomputed, avg ranks) |")
    w("|---|---|---|---|---|---|---|")
    rec = {}
    for name, v, both_logit in preds:
        r = pearson(v, y)
        lo = pearson([logit(a) for a in y], [logit(b) for b in v] if both_logit else v)
        rho = pearson(avg_ranks(y), avg_ranks(v))
        g = regs[name]
        rec[name] = dict(r=r, R2=r * r, lo_r=lo, rho=rho)
        w(f"| {name} (raw :{g['line']}) | {g['r']:+.3f} | {r:+.4f} | {g['R2']:.3f} | {r*r:.4f} | "
          f"{g['lo_r']:+.3f} / {lo:+.4f} | {g['rho']:+.3f} / {rho:+.4f} |")
    w("")
    w(f"Print precision of the inputs: pkeep, empDL, geoN, empPK 3 d.p.; geoL 1 d.p. (so the geometric-linear "
      f"row moves most); strain 2 d.p. Ties (avg ranks used; the producing script ranked full-precision values "
      f"by argsort): stored P(keep) {n_tied(y)} tied values, empirical Δlogit {n_tied(x)}.")
    a, b, r2_ols, res, h, sst = ols1(x, y)
    q2_press, q2_refit = loo_q2(x, y)
    r_emp = rec["empirical dlogit (final-pos)"]["r"]
    df = n - 2
    t = r_emp * math.sqrt(df) / math.sqrt(1 - r_emp ** 2)
    p_t = t_two_sided_p(t, df)
    assert abs(t_two_sided_p(2.0395134464, 31) - 0.05) < 1e-4  # t_{.975,31}
    lo95, hi95 = fisher_ci(r_emp, n)
    pc = partial_r(y, s, x)
    t_pc = pc * math.sqrt(n - 3) / math.sqrt(1 - pc * pc)
    p_pc = t_two_sided_p(t_pc, n - 3)
    low = [i for i in range(n) if s[i] <= lowstrain["cut"]]
    r_low = pearson([y[i] for i in low], [x[i] for i in low])
    sd_low = statistics.pstdev([y[i] for i in low])
    d_r = r_emp - regs["empirical dlogit (final-pos)"]["r"]
    w("")
    w("The decisive arm, in full (stored P(keep) on empirical final-position Δlogit):")
    w("")
    w(f"- OLS with intercept, in-sample: P(keep) = {a:.4f} + {b:.4f} · Δlogit; in-sample R² = {r2_ols:.4f} "
      f"(= r² = {r_emp*r_emp:.4f}; the record's R² is r·r of a Pearson r, which is this in-sample R²).")
    w(f"- Recomputed r = {r_emp:+.4f} vs printed +0.728: Δr = {d_r:+.4f} "
      f"({'within' if abs(d_r) <= 0.002 else 'OUTSIDE'} the ±0.002 print-precision tolerance declared in this script); "
      f"R² {r_emp*r_emp:.4f} vs printed 0.530.")
    w(f"- Post-hoc inference (computed-new, not in the record): t = {t:.3f} on df = {df}, two-sided "
      f"Student-t p = {p_t:.2e} (H0: ρ = 0; normal-theory); Fisher-z 95% CI for r [{lo95:+.3f}, {hi95:+.3f}] "
      f"-> R² in [{lo95**2:.3f}, {hi95**2:.3f}]. The sampling model is notional: the 33 units are a "
      f"rule-selected set of tail-PCA directions (§6), not a random sample of directions, and the test and "
      f"interval treat them as i.i.d.")
    w(f"- Post-hoc held-out (computed-new): leave-one-direction-out predictive R² (Q²) = {q2_press:.4f} by "
      f"PRESS, {q2_refit:.4f} by 33 explicit refits.")
    w(f"- Low-strain subgroup (strain ≤ {lowstrain['cut']}, from the printed 2-decimal strain): n = {len(low)} "
      f"(log n = {lowstrain['n']}); r = {r_low:+.4f} (log {lowstrain['r']:+.3f}, raw :{lowstrain['line']}); "
      f"P(keep) population SD {sd_low:.4f} (log {lowstrain['sd']:.3f}).")
    w(f"- Partial corr(P(keep), strain | Δlogit) = {pc:+.4f} (log {partial['value']:+.3f}, raw :{partial['line']}); "
      f"t = {t_pc:.3f} on df = {n-3}, two-sided p = {p_pc:.3f} (the log's 't ≈ 0.8, ns', "
      f"`{ARCH12}@{PIN}:{L_part}`; strain at 2 decimals).")
    w(f"- Unexplained share 1 − R²: {1 - r_emp*r_emp:.4f} (log '~47%', `{ARCH12}@{PIN}:{L_47}`).")
    L_sd = line_of(a12, "P(keep) range (subgroup SD 0.252 > full-sample 0.229) at test-retest", ARCH12)
    ylow = [y[i] for i in low]
    w(f"- Adjacent SD figures (motivating observation, `{ARCH12}@{PIN}:{L_sd}`: 'subgroup SD 0.252 > "
      f"full-sample 0.229'; the raw :{lowstrain['line']} prints SD=0.239 for the same subgroup): low-strain "
      f"P(keep) SD {statistics.stdev(ylow):.4f} with n−1, {statistics.pstdev(ylow):.4f} with n; full set "
      f"{statistics.stdev(y):.4f} with n−1, {statistics.pstdev(y):.4f} with n. "
      + ("The two record values are the same data under the two denominators (0.252 = n−1 SD, 0.239 = n SD; "
         "full set 0.229 = n−1 SD), not a discrepancy."
         if (f"{statistics.stdev(ylow):.3f}", f"{statistics.pstdev(ylow):.3f}", f"{statistics.stdev(y):.3f}")
         == ("0.252", "0.239", "0.229")
         else "The record's 0.252 / 0.239 / 0.229 are NOT all matched by either denominator: see the values."))
    J["sd_check"] = dict(low_sd1=statistics.stdev(ylow), low_sd0=statistics.pstdev(ylow),
                         all_sd1=statistics.stdev(y), all_sd0=statistics.pstdev(y))
    w("")
    J["recompute_raw"] = dict(n=n, r=r_emp, R2=r_emp * r_emp, intercept=a, slope=b, t=t, p_t=p_t,
                              fisher_ci_r=[lo95, hi95], q2_press=q2_press, q2_refit=q2_refit,
                              r_low=r_low, n_low=len(low), partial=pc, p_partial=p_pc,
                              per_predictor=rec, pkeep_mismatch=mism)

    # ------------------------------------- 5. local-only cross-check -------
    w("## 5. Full-precision cross-check against the local-only JSON (computed-new; not a reproduction)")
    w("")
    cj = os.path.join(REPO, CLONE_JSON)
    local = None
    if os.path.isfile(cj):
        raw_b = open(cj, "rb").read()
        local = json.loads(raw_b)
        ly = [d["pkeep"] for d in local]
        lx = [d["emp_dlogit"] for d in local]
        ls = [d["strain"] for d in local]
        lr = pearson(lx, ly)
        llo = pearson([logit(v) for v in ly], lx)
        lpc = partial_r(ly, ls, lx)
        lq2, _ = loo_q2(lx, ly)
        llow = [i for i in range(len(local)) if ls[i] <= 0.15]
        lr_low = pearson([ly[i] for i in llow], [lx[i] for i in llow])
        ranks_ok = [d["rank"] for d in local] == [r["rank"] for r in rows]
        print_ok = all(f"{d['pkeep']:.3f}" == r["s_pkeep"] and f"{d['emp_dlogit']:+.3f}" ==
                       f"{r['empDL']:+.3f}" for d, r in zip(local, rows))
        pj = os.path.join(REPO, CLONE_POW_JSON)
        pow_ok = None
        pow_keys = None
        if os.path.isfile(pj):
            pl = json.loads(open(pj, "rb").read())
            pow_ok = [d["pkeep"] for d in pl] == ly and [d["rank"] for d in pl] == [d["rank"] for d in local]
            pow_keys = sorted({k for d in pl for k in d})
        # the archive parenthetical (L_recon..+1): both candidate rows at full precision
        lxp = [d["emp_pkeep"] for d in local]
        par = {
            "dlogit": dict(r=lr, rho=pearson(avg_ranks(ly), avg_ranks(lx)), lo=llo),
            "recon": dict(r=pearson(lxp, ly), rho=pearson(avg_ranks(ly), avg_ranks(lxp)),
                          lo=pearson([logit(v) for v in ly], [logit(v) for v in lxp])),
        }
        ties_full = (n_tied(ly), n_tied(lx), n_tied(lxp))
        w(f"- `{CLONE_JSON}`: present on this machine, sha256 `{sha256(raw_b)}`, {len(local)} records; "
          f"gitignored clone, never committed (§3); identified here by sha256 only.")
        w(f"- Its rank order equals the committed raw's: {ranks_ok}; every record rounds to the raw's printed "
          f"pkeep (3 d.p.) and empDL (+3 d.p.): {print_ok}; its pkeep column equals the local "
          f"`{CLONE_POW_JSON}` (the stored DV) exactly: {pow_ok}.")
        w(f"- Full precision: r = {lr:+.6f}, R² = {lr*lr:.6f} (prints as 0.530: {f'{lr*lr:.3f}' == '0.530'}); "
          f"log-odds r = {llo:+.6f} -> R² of logit(8-prompt-mean P(keep)) on Δlogit = {llo*llo:.6f}; "
          f"low-strain (≤ 0.15) n = {len(llow)}, r = {lr_low:+.6f}; partial corr = {lpc:+.6f}; "
          f"LOO Q² = {lq2:.6f}.")
        w(f"- The archive parenthetical (`{ARCH12}@{PIN}:{L_recon}-{L_recon + 1}`: 'r = +0.725; Spearman +0.68; "
          f"log-odds r +0.72'), both candidate rows at full precision (ties at full precision in y / Δlogit / "
          f"reconstructed P(keep): {ties_full}): Δlogit row r {par['dlogit']['r']:+.6f}, Spearman "
          f"{par['dlogit']['rho']:+.6f}, log-odds r {par['dlogit']['lo']:+.6f}; reconstructed-P(keep) row r "
          f"{par['recon']['r']:+.6f}, Spearman {par['recon']['rho']:+.6f}, log-odds r {par['recon']['lo']:+.6f}. "
          f"At 2 d.p.: Δlogit {par['dlogit']['rho']:+.2f} / {par['dlogit']['lo']:+.2f}; reconstructed "
          f"{par['recon']['rho']:+.2f} / {par['recon']['lo']:+.2f}.")
        n_logit_pow = sum(1 for ln in lines(rp) if re.search(r"logit", ln, re.I))
        n_logit_smoke = sum(1 for ln in lines(ptext("results/raw/2026-08-04_slice3_dv_smoke.txt"))
                            if re.search(r"logit", ln, re.I))
        w(f"- Keys of the local `{CLONE_POW_JSON}` records (the stored DV): {pow_keys}; the diagnostic's JSON "
          f"keys: {sorted({k for d in local for k in d})} (its Δlogit is the final-position-only arm). Lines "
          f"containing 'logit' in the committed DV raws `{RAW_POW}` and "
          f"`results/raw/2026-08-04_slice3_dv_smoke.txt`: {n_logit_pow} and {n_logit_smoke}. So no artifact "
          f"carries per-prompt label logits under the all-positions vector, only the 8-prompt mean of the "
          f"two-label P(keep).")
        J["local_json"] = dict(path=CLONE_JSON, sha256=sha256(raw_b), n=len(local), r=lr, R2=lr * lr,
                               lo_r=llo, lo_R2=llo * llo, r_low=lr_low, partial=lpc, q2=lq2,
                               ranks_ok=ranks_ok, print_ok=print_ok, pow_ok=pow_ok, parenthetical=par,
                               pow_keys=pow_keys)
    else:
        w(f"- `{CLONE_JSON}` is not present on this machine (expected on any fresh clone): cross-check not run "
          f"(nor the parenthetical's full-precision rows, nor the stored DV's key list).")
        J["local_json"] = None
    w("")

    # ------------------------------------------- 6. the regression ---------
    w("## 6. The regression, stated exactly")
    w("")
    clone_info = {}
    for p in (CLONE_DIAG_PY, CLONE_POW_PY, CLONE_FP_PY):
        fp = os.path.join(REPO, p)
        clone_info[p] = sha256(open(fp, "rb").read()) if os.path.isfile(fp) else None
    dpy = open(os.path.join(REPO, CLONE_DIAG_PY)).read() if clone_info[CLONE_DIAG_PY] else ""
    ppy = open(os.path.join(REPO, CLONE_POW_PY)).read() if clone_info[CLONE_POW_PY] else ""
    fpy = open(os.path.join(REPO, CLONE_FP_PY)).read() if clone_info[CLONE_FP_PY] else ""

    def cl(text, needle, path):
        hits = find_lines(text, needle)
        return f"{path}:{hits[0]}" if hits else f"{path}:(not found)"
    loc_last = cl(dpy, "return h + v if p == last else h", CLONE_DIAG_PY)
    loc_delta = cl(dpy, "deltas.append((k - s) - (bk - bs))", CLONE_DIAG_PY)
    loc_mean = cl(dpy, "emp_dlogit = float(np.mean(deltas))", CLONE_DIAG_PY)
    loc_r2 = cl(dpy, 'R^2={r*r:.3f}', CLONE_DIAG_PY)
    loc_R = cl(dpy, "R = float(np.mean(np.linalg.norm(X, axis=1)))", CLONE_DIAG_PY)
    loc_ncorp = cl(dpy, "N_CORPUS = 50", CLONE_DIAG_PY)
    loc_powR = cl(ppy, 'R = data["R"]', CLONE_POW_PY)
    us = os.path.join(REPO, CLONE, "data/configs/usable_strain.json")
    usR = json.loads(open(us, "rb").read()).get("R") if os.path.isfile(us) else None
    loc_alpha = cl(dpy, "alpha = 1.0 * R", CLONE_DIAG_PY)
    loc_tmpl = cl(ppy, "TEMPLATE = (", CLONE_POW_PY)
    loc_pk = cl(ppy, "vals.append(pk / (pk + ps) if (pk + ps) > 0 else np.nan)", CLONE_POW_PY)
    loc_ind = cl(ppy, "fns = make_induce_fns({LAYER: [(mx.array(Vt[-r[\"rank\"]]), alpha)]})", CLONE_POW_PY)
    loc_sel = cl(ppy, "if r[\"nonascii\"] <= 0.1 and r[\"rank\"] != 2 and r[\"accuracy\"] >= 0.33]", CLONE_POW_PY)
    loc_every = cl(fpy, "applies induce_fns[i] to every position's", CLONE_FP_PY)
    w("Committed-record statements first; the producing code (local-only, gitignored clone; sha256 below) "
      "fills in what the record's prose does not state.")
    w("")
    L_model = line_of(a12, "Model: `mlx-community/Qwen3.6-27B-4bit` via `jlens-qwen36` (MLX port), running", ARCH12)
    w(f"- **Model.** `mlx-community/Qwen3.6-27B-4bit` via the jlens-qwen36 MLX port (`{ARCH12}@{PIN}:{L_model}`; "
      f"`FINDINGS-2.md@{PIN}:1`); steering at layer 48 (`{ARCH12}@{PIN}:{L_tail}`; raw :4).")
    ranks = [r["rank"] for r in rows]
    w(f"- **Unit of analysis: 33 directions, not tokens or sessions.** Each row is one tail-PCA direction of "
      f"the L48 residual stream (`{ARCH12}@{PIN}:{L_tail}`), the '33 strain-spanning English configs "
      f"(frac=1.0, −2 excluded)' (`{ARCH12}@{PIN}:{L_pow2}`; raw :3); printed ranks {min(ranks)}-{max(ranks)}, "
      f"absent {sorted(set(range(min(ranks), max(ranks) + 1)) - set(ranks))} (raw :11-43); selection rule in "
      f"code: nonascii ≤ 0.1, rank ≠ 2, accuracy ≥ 0.33 ({loc_sel}). No sessions and no generation: every "
      f"quantity is a single next-token forward.")
    w(f"- **Dose.** α = 1.0 × R with R = 102.385 (raw :5), the mean L48 residual norm over every token "
      f"position of 50 corpus prompts ({loc_R}; {loc_ncorp}; {loc_alpha}); `{ARCH12}@{PIN}:{L_alpha}`: "
      f"'α = R ≈ 102, ≈ the whole residual stream'. Full norm: frac = 1.0. The stored DV took R from the "
      f"local usable_strain.json ({loc_powR}): R = {usR} there "
      f"(equal to the diagnostic's 102.385 at 3 d.p.: {usR is not None and f'{usR:.3f}' == '102.385'}).")
    w(f"- **Read token and prompts.** The final token of 8 fixed completion-style prompts (raw :8): 4 task "
      f"contexts × 2 question orders ('Keep ... or switch ...?' / 'Switch ... or keep ...?'), ending "
      f"'Answer with one word.\\nAnswer:' ({loc_tmpl}); labels ' keep' (id 2426) and ' switch' (id 3289), "
      f"raw :2. (The 2026-08-04 smoke used 5 contexts, `{ARCH12}@{PIN}:{L_smoke}`; the powered DV and the "
      f"diagnostic used these 8 prompts.)")
    w(f"- **Dependent variable (y): the stored DV, P(keep).** From the 2026-08-05 powered run "
      f"(`{ARCH12}@{PIN}:{L_pow}`; `{RAW_POW}`): α·d added at L48 at EVERY position of the prompt "
      f"({loc_ind}; {loc_every}), then per prompt P(keep)/(P(keep)+P(switch)) at the read token, averaged "
      f"over the 8 prompts ({loc_pk}). A probability renormalized over the two labels, not a logit.")
    w(f"- **Predictor (x): empirical final-position Δlogit.** α·d added at L48 at the FINAL position only "
      f"({loc_last}) -- 'the state never present over the context' (`FINDINGS-2.md@{PIN}:{F2_175}`) -- and "
      f"Δ = (logit_keep − logit_switch)_steered − (logit_keep − logit_switch)_unsteered per prompt "
      f"({loc_delta}), averaged over the 8 prompts ({loc_mean}).")
    w(f"- **Fit.** Pearson r between y and x over the 33 directions; the printed R² is r·r ({loc_r2}), "
      f"identical to the in-sample R² of a one-predictor OLS with intercept (§4). **In-sample; no "
      f"cross-validation, no held-out directions, and no test or interval on r or R² in the record** (the only "
      f"test it reports is the partial correlation's 't ≈ 0.8, ns', `{ARCH12}@{PIN}:{L_part}`). The pre-registered "
      f"read (raw :60-66) maps 'high R²' to 'invalid instrument' without a numeric bar.")
    w(f"- **What the 0.53 is a fraction of.** Between-direction variance of the 8-prompt-mean P(keep) of a "
      f"full-context-steered readout -- not within-prompt, not per-token, not across sessions. The record "
      f"also prints a log-odds r = +0.715 (raw :{RD_50}), i.e. R² = 0.715² = {0.715 ** 2:.3f} (Code's "
      f"arithmetic; the record states no log-odds R²). That is the log-odds of the prompt-averaged "
      f"probability, logit(mean_i σ(ℓ_i)), where ℓ_i = logit_keep − logit_switch in prompt i "
      f"({loc_pk}: the two-label renormalization, then the mean). It is not the mean label-logit "
      f"difference mean_i ℓ_i, which is a different quantity; no record artifact carries ℓ_i under the "
      f"all-positions vector (§5). There is no exact 'R² of label logits' in the record.")
    w(f"- **Companion arms in the same run** (raw :{regs['geometric-normed']['line']}-"
      f"{regs['empirical P(keep) (final-pos)']['line']}): geometric J-lens projections R² 0.058 / 0.064 "
      f"(`{ARCH12}@{PIN}:{L_geo}`, 'pre-registered as non-decisive'); reconstructed final-position-only "
      f"P(keep) r = +0.725, R² 0.526 (`{ARCH12}@{PIN}:{L_recon}`).")
    w("")
    w("Local-only producing files read (gitignored clone; never committed; read-only; sha256):")
    for p, hsh in clone_info.items():
        w(f"- `{p}`: {hsh if hsh else 'absent'}")
    w("")
    J["clone_files"] = clone_info

    # ------------------------------------------- 7. carriers vs record -----
    w("## 7. The sentences that carry it, against the record")
    w("")
    pre_path = os.path.join(REPO, PREPRINT)
    pre_b = open(pre_path, "rb").read() if os.path.isfile(pre_path) else b""
    pre_ok = sha256(pre_b) == PREPRINT_SHA
    pre = pre_b.decode("utf-8") if pre_b else ""
    CARRIER = re.compile(r"R²\s?=\s?0?\.53(?!\d)")
    PC = [i + 1 for i, ln in enumerate(lines(pre)) if CARRIER.search(ln)]
    PCAL = [i + 1 for i, ln in enumerate(lines(pre)) if re.search(r"calibrat", ln, re.I)]
    P31 = find_lines(pre, "a steering vector active at the readout accounting for R² = 0.53 of decision-logit variance")
    P192 = find_lines(pre, "In a horn-1 calibration on Qwen, the decision token alone accounts for R² = 0.53")
    P222 = find_lines(pre, "(R² = 0.53 in our calibration)")
    assert sorted(P31 + P192 + P222) == PC, (P31, P192, P222, PC)
    m222 = re.search(r"so the contrast is the on/off contrast of §5\.6 \(R² = 0\.53 in our calibration\)",
                     lines(pre)[P222[0] - 1]) if P222 else None
    other_cal = [L for L in PCAL if L not in PC]
    m_oc = {}
    for L in other_cal:
        ln_ = lines(pre)[L - 1]
        m_oc[L] = [ln_[max(0, m.start() - 45): m.start() + 45].strip()
                   for m in re.finditer(r"calibrat", ln_, re.I)]
    pp_glob = sorted(p for p in os.listdir(os.path.join(REPO, "archive"))
                     if p.startswith("PREPRINT-v1_0-draft.pre-patch-v") and p.endswith(".md"))
    pp = {}
    for p in pp_glob:
        tx = open(os.path.join(REPO, "archive", p), encoding="utf-8").read()
        pp[p] = [i + 1 for i, ln in enumerate(lines(tx)) if CARRIER.search(ln)]
    pp_tracked = {p: f"archive/{p}" in tree for p in pp_glob}
    w(f"`{PREPRINT}` (untracked; working-tree sha256 {'MATCHES' if pre_ok else 'DOES NOT MATCH'} the block's "
      f"d6431e97...222b8). The note itself (`RESEARCH-NOTE-v0_2-draft.md`, whose §2 P3 this defends) is not on "
      f"this machine (preflight note 1), so its sentence is not checked here. The preprint's carriers are "
      f"found by the pattern `{CARRIER.pattern}` over the whole file: lines {PC}.")
    w("")
    for L in P31 + P192:
        w(f"- `{PREPRINT}:{L}`: \"{quote(pre, L, 400)}\"")
    for L in P222:
        w(f"- `{PREPRINT}:{L}` (a paragraph on another group's published experiment; the clause that carries "
          f"the figure): \"... {m222.group(0) if m222 else '(clause not matched)'} ...\"")
    w("")
    w(f"Same three lines in the untracked pre-patch copies: "
      + "; ".join(f"`archive/{p}` {v} (tracked: {pp_tracked[p]})" for p, v in pp.items()) + ".")
    w(f"Other preprint lines using 'calibrat' (none carries the 0.53): "
      + "; ".join(f":{L} " + " / ".join(f"\"...{e}...\"" for e in m_oc[L]) for L in other_cal) + ".")
    if pre_ok:
        assert other_cal == [25, 152, 182, 268], other_cal
        w("They are other uses of the word: sham arms that calibrate noise (:25), a bar calibrated on ± "
          "contrasts (:152), the DIFF arm's calibrated accuracy and the CORR dose that 'a later calibration "
          "(§8.1)' found below its visibility criterion (:182), and the corruption dose recalibrated for "
          "PROPOSAL-m (§8.1, :268). N1 should not attach any of them to this figure.")
    w("")
    w("Against the record:")
    w("")
    w(f"1. **The number** 0.53 at :{', :'.join(map(str, PC))} equals the record's 0.530 (empirical arm, "
      f"`{ARCH12}@{PIN}:{L_emp}`). Not discrepant.")
    w("2. **'the decision token alone'** (:31, :192) -- matches: the predictor injects at the final (read) "
      "position only.")
    w("3. **'of the variance in label logits' (:192) / 'of decision-logit variance' (:31)** -- the record's y is "
      "the stored P(keep), a two-label-renormalized probability averaged over 8 prompts, not a logit; the "
      "logit-valued quantity in the regression is the predictor. A wording imprecision, not a numeric "
      "discrepancy. The faithful form is 'accounts for R² = 0.53 of the between-direction variance in the "
      "label-choice probability P(keep)'. The log-odds figure (0.715² = "
      f"{0.715 ** 2:.3f}, §6) is the log-odds of the prompt-averaged probability, not a label-logit quantity, "
      "so it is not offered as a substitute for 'label logits'.")
    w("4. **'under the vector'** -- the stored DV had α·d at every position at full norm (frac 1.0, ‖αd‖ ≈ "
      "R ≈ 102 at L48) along 33 tail-PCA 'strain' directions. The figure holds at that dose and that "
      "direction family only: not the reward axis, not the Phase-2 doses, not OLMo. Later designs carry their "
      "own leakage measurements (e.g. e2b H1, item N6), which this item does not audit.")
    w(f"5. **'horn-1 calibration' (:192) / 'our calibration' (:222)** -- 'horn 1' matches FINDINGS-2's two-horns "
      f"result (horn 1 = state active at the readout, `FINDINGS-2.md@{PIN}:{F2_244}`; `{ARCH12}@{PIN}:{L_horns}`). "
      f"'Calibration' is ambiguous (§1c). The record does call this diagnostic's post-mortem 'the calibration "
      f"source' for a later gate (`PROPOSAL-e-reward-axis-hijack.md@{PIN}:{C['pe_247']}-{C['pe_248']}`). But "
      f"'calibration' next to horn 1 names the PROPOSAL-h H-calibration tier "
      f"(`PROPOSAL-h-state-present-choice.md@{PIN}:{C['ph_tier']}`; `FINDINGS-5.md@{PIN}:{C['f5_99']}`), whose "
      f"horn-1 result, 'quantified and de minimis under shields' (`FINDINGS-5.md@{PIN}:{C['f5_horn']}`), is a "
      f"different statistic (N6). Naming the measurement removes the ambiguity: 'a cycle-2 diagnostic on Qwen "
      f"(2026-08-06)'.")
    w(f"6. **Scope at :222** -- the sentence attaches the 0.53 to another group's vector-on/off contrast. The "
      f"record supports the qualitative claim: a vector active at the read writes into the decision "
      f"(`FINDINGS-2.md@{PIN}:{F2_244}`; `{ARCH12}@{PIN}:{L_horns}`). The magnitude is from one design: the "
      f"in-sample, between-direction R² across 33 tail-PCA strain directions at full norm (α = R ≈ 102), at "
      f"L48 on Qwen3.6-27B-4bit, of an all-positions-steered P(keep) on the final-position-only Δlogit. It is "
      f"not the share of any single vector-on/off contrast that the readout explains, and it was not measured "
      f"on another model, direction or dose. The furthest stretch of the three carriers.")
    w("7. **In-sample** -- the record reports no held-out figure and no interval; §4 adds a post-hoc LOO Q² and "
      "a Fisher-z interval, which the note may cite as post-hoc if it wants an interval.")
    w("")
    J["preprint"] = dict(sha_ok=pre_ok, carriers=PC, calib_lines=PCAL, prepatch=pp)

    # ------------------------------------------------- figures table -------
    rr = J["recompute_raw"]
    lo_raw2 = rec["empirical dlogit (final-pos)"]["lo_r"] ** 2
    lj = J["local_json"] or {}
    lr2 = f"{lj['R2']:.4f}" if lj else "not run"
    lr_ = f"{lj['r']:+.4f}" if lj else "not run"
    llo2 = f"{lj['lo_R2']:.4f}" if lj else "not run"
    w("## Figures (as the block writes them, plus the record figures the sentence leans on)")
    w("")
    w("| figure | value printed | source | status | note |")
    w("|---|---|---|---|---|")
    ylow_ = [y[i] for i in range(n) if s[i] <= lowstrain["cut"]]
    sdc = J["sd_check"]
    par_ = lj.get("parenthetical") if lj else None
    gD, gP = regs["empirical dlogit (final-pos)"], regs["empirical P(keep) (final-pos)"]
    paren_note = (
        f"Adjacent, not the block's figure. The parenthetical's r is the reconstructed-P(keep) row's. Its "
        f"Spearman +0.68 matches the Δlogit row (printed {gD['rho']:+.3f}), not the reconstructed row "
        f"(printed {gP['rho']:+.3f}). Its log-odds +0.72 is the Δlogit row's printed {gD['lo_r']:+.3f} rounded "
        f"half up")
    if par_:
        assert f"{par_['dlogit']['lo']:+.2f}" != "+0.72" and f"{par_['recon']['lo']:+.2f}" != "+0.72", par_
        paren_note += (
            f"; at full precision that row is {par_['dlogit']['lo']:+.4f} → {par_['dlogit']['lo']:+.2f}, and "
            f"the reconstructed row is {par_['recon']['lo']:+.4f} → {par_['recon']['lo']:+.2f}, so neither row "
            f"gives +0.72 at full precision")
    paren_note += (". Looks like transcription (a double rounding and a row mix-up); matters only if a "
                   "carrier quotes them.")
    assert f"{gD['rho']:+.2f}" == "+0.68" or f"{gD['rho']:+.3f}" == "+0.675"
    rows_out = [
        ("Horn-1 calibration R² = 0.53 (block :112)",
         f"record 0.530; recomputed from the committed raw's printed table {rr['R2']:.4f}; full precision (local-only JSON) {lr2}",
         f"{ARCH12}@{PIN}:{L_emp}; {RAW_DIAG}@{PIN}:{RD_50}",
         "log-only",
         f"Entered at {ec[:7]} ({ec_date[:10]}), cycle 2. Scope: Qwen3.6-27B-4bit; L48; frac 1.0 (α = R = 102.385); "
         f"unit = 33 tail-PCA directions (ranks {min(ranks)}-{max(ranks)}); y = stored P(keep) (α·d at every "
         f"position; two-label probability averaged over 8 prompts); x = final-position-only Δlogit; Pearson r², "
         f"in-sample, no CV. The only machine-readable artifact is the gitignored, never-committed {LOCAL_JSON}. "
         f"The log's arithmetic is consistent at print precision (§4). The record's 'calibration' term is "
         f"ambiguous (§1c); keep apart from N6's H-calibration horn-1 figures."),
        ("r = +0.728 (the correlation under the R²)",
         f"recomputed {rr['r']:+.4f} (raw table); {lr_} (local-only JSON)",
         f"{ARCH12}@{PIN}:{L_emp}; {RAW_DIAG}@{PIN}:{RD_50}", "log-only", "Pearson, n = 33 directions (scope as above)"),
        ("preprint: 'R² = 0.53 of the variance in label logits' (:192) / 'of decision-logit variance' (:31)",
         "0.53 (= record 0.530)",
         f"{PREPRINT}:{','.join(map(str, P31 + P192))} (untracked, sha-checked); record {ARCH12}@{PIN}:{L_emp}",
         "log-only",
         "Number matches; wording does not: the record's y is P(keep), a two-label probability, not a logit. "
         "Say 'of the between-direction variance in the label-choice probability P(keep)' and state the scope. "
         "'horn-1 calibration' (:192): name the measurement instead, 'a cycle-2 diagnostic on Qwen (2026-08-06)' (§7.5)."),
        ("preprint: 'the on/off contrast of §5.6 (R² = 0.53 in our calibration)' (:222)",
         "0.53 (= record 0.530)",
         f"{PREPRINT}:{','.join(map(str, P222))} (untracked, sha-checked); record {ARCH12}@{PIN}:{L_emp}",
         "log-only",
         "Number matches; scope does not. The sentence applies a between-direction R² (33 tail-PCA directions, "
         "full norm, L48, Qwen, in-sample) to another group's vector-on/off contrast. The record supports the "
         "qualitative horn-1 claim, not this magnitude for that contrast (§7.6). Same wording item as :192."),
        ("R² of the log-odds of the prompt-averaged two-label P(keep) on final-position Δlogit",
         f"{0.715 ** 2:.4f} from the logged log-odds r +0.715; {lo_raw2:.4f} from the raw table; full precision {llo2}",
         f"{RAW_DIAG}@{PIN}:{RD_50} (log-odds r); local-only JSON for full precision",
         "computed-new",
         "r² of logit(mean over 8 prompts of P(keep)/(P(keep)+P(switch))) on Δlogit; in-sample. Not an R² of "
         "label logits: logit of a prompt mean is not the mean label-logit difference, and no artifact carries "
         "per-prompt label logits under the all-positions vector (§5, §6). Not stated as an R² in the record."),
        ("subgroup SD 0.252 > full-sample 0.229 (and the raw's SD=0.239)",
         f"low-strain {sdc['low_sd1']:.4f} (n−1) / {sdc['low_sd0']:.4f} (n), n = {len(ylow_)}; full set "
         f"{sdc['all_sd1']:.4f} (n−1) / {sdc['all_sd0']:.4f} (n), n = {n}",
         f"{ARCH12}@{PIN}:{L_sd}; {RAW_DIAG}@{PIN}:{lowstrain['line']}", "log-only",
         "Adjacent (the motivating observation). SD of stored P(keep) over directions, low-strain = strain ≤ 0.15 "
         "at 2 d.p. 0.252 and 0.239 are the same data under the two denominators; not a discrepancy."),
        ("C2: R² = .53 (PROPOSAL-h §1)", "0.53",
         f"PROPOSAL-h-state-present-choice.md@{PIN}:{PH_65}", "log-only",
         "citation of the same figure; 'C2' undefined in PROPOSAL-h, read by Code as cycle 2"),
        ("R² = 0.53 (FINDINGS-2 summary, table, finding text, two-horns)", "~53% / 0.53 / 0.530",
         f"FINDINGS-2.md@{PIN}:{F2_51},{F2_129},{F2_175},{F2_244}", "log-only",
         f"citations of the same figure; :{F2_51} gives it as '~53% of its variance', the variance of the (b) DV, "
         f"P(keep) (:{F2_its}-{F2_its + 1})"),
        ("R² = 0.53 of stored P(keep) (cycle-2 summary)", "0.53",
         f"{ARCH12}@{PIN}:{L_sum}", "log-only", "summary of the same entry"),
        ("low-strain subgroup r = +0.712 (n = 10)",
         f"recomputed {rr['r_low']:+.4f}, n = {rr['n_low']}" + (f"; {lj['r_low']:+.4f} full precision" if lj else ""),
         f"{RAW_DIAG}@{PIN}:{lowstrain['line']}; {ARCH12}@{PIN}:{L_low}-{L_low + 1}", "log-only", "strain ≤ 0.15"),
        ("partial corr(P(keep), strain | Δlogit) = +0.147, t ≈ 0.8 ns",
         f"recomputed {rr['partial']:+.4f}; t-test two-sided p = {rr['p_partial']:.3f} (df 30)",
         f"{RAW_DIAG}@{PIN}:{partial['line']}; {ARCH12}@{PIN}:{L_part}", "log-only", ""),
        ("geometric arms R² ≈ 0.06",
         f"recomputed {rec['geometric-normed']['R2']:.4f} / {rec['geometric-linear']['R2']:.4f}",
         f"{RAW_DIAG}@{PIN}:{regs['geometric-normed']['line']}-{regs['geometric-linear']['line']}; {ARCH12}@{PIN}:{L_geo}",
         "log-only", "context (pre-registered non-decisive)"),
        ("~47% unexplained", f"{1 - rr['R2']:.4f}", f"{ARCH12}@{PIN}:{L_47}", "log-only", "1 − R²"),
        ("post-hoc: 95% CI on r / R² (Fisher z)",
         f"r [{rr['fisher_ci_r'][0]:+.3f}, {rr['fisher_ci_r'][1]:+.3f}]; R² [{rr['fisher_ci_r'][0]**2:.3f}, {rr['fisher_ci_r'][1]**2:.3f}]",
         f"this script over {RAW_DIAG}@{PIN} printed table", "computed-new",
         f"post-hoc; normal theory; n = 33. The units are a rule-selected direction set ({loc_sel}); the "
         f"interval treats them as i.i.d. (notional)"),
        ("post-hoc: test of ρ = 0",
         f"t = {rr['t']:.3f}, df 31, two-sided p = {rr['p_t']:.1e}",
         f"this script over {RAW_DIAG}@{PIN} printed table", "computed-new",
         "post-hoc; Student t, two-sided. Same notional i.i.d. sampling model as the CI row"),
        ("post-hoc: held-out (leave-one-direction-out) Q²",
         f"{rr['q2_press']:.4f}" + (f" (full precision {lj['q2']:.4f})" if lj else ""),
         f"this script over {RAW_DIAG}@{PIN} printed table", "computed-new", "post-hoc; the record's 0.53 is in-sample"),
        ("'(reconstructed final-pos-only P(keep) vs stored: r = +0.725; Spearman +0.68; log-odds r +0.72)'",
         f"raw :{regs['empirical P(keep) (final-pos)']['line']} (reconstructed P(keep)): r "
         f"{regs['empirical P(keep) (final-pos)']['r']:+.3f}, Spearman {regs['empirical P(keep) (final-pos)']['rho']:+.3f}, "
         f"log-odds r {regs['empirical P(keep) (final-pos)']['lo_r']:+.3f}; raw :{RD_50} (Δlogit): Spearman "
         f"{regs['empirical dlogit (final-pos)']['rho']:+.3f}, log-odds r {regs['empirical dlogit (final-pos)']['lo_r']:+.3f}"
         + (f"; full precision: Δlogit Spearman {par_['dlogit']['rho']:+.4f}, log-odds {par_['dlogit']['lo']:+.4f}; "
            f"reconstructed Spearman {par_['recon']['rho']:+.4f}, log-odds {par_['recon']['lo']:+.4f}" if par_ else ""),
         f"{ARCH12}@{PIN}:{L_recon}-{L_recon + 1}", "log-only",
         paren_note),
        ("homonym: H-calibration tier's horn-1 result, 'quantified and de minimis under shields' (π̂_d = 0.0172)",
         "not an R²; not this figure",
         f"FINDINGS-5.md@{PIN}:{C['f5_pid']}-{C['f5_pid'] + 1},{C['f5_horn']}; PROPOSAL-h-state-present-choice.md@{PIN}:{C['ph_tier']},{C['ph_h1']}",
         "log-only",
         "N6's domain (results/raw/2026-10-08_note-N6-e2b.md §3). Listed so N1 does not attach the note's "
         "'horn-1 calibration' to it, or this R² to the h arc."),
        ("homonym: '(d) leak ... mean 0.53'", "not an R²",
         f"archive/RESULTS-cycles3-4.md@{PIN}:{find_lines(ptext('archive/RESULTS-cycles3-4.md'), 'max |Δ| = 1.06, mean 0.53')[0]}",
         "log-only", "the weight-channel leak's mean |Δ| (N9's domain); not N10's figure"),
        ("homonym: e2a g3 KV-leakage max |Δ(logit_A − logit_B)| = 0.5368",
         f"max_abs {g3j['max_abs']:.4f} (recomputed max |delta| over {len(g3_rows)} rows {g3_max:.5f}; mean "
         f"{g3_mean:.4f}); not an R²; not this figure",
         f"data/e2a/g3_kv_leakage.json@{PIN}:max_abs; archive/RESULTS-cycles3-4.md@{PIN}:{G3['value']}; "
         f"FINDINGS-3.md@{PIN}:{G3['f3']}",
         "reproduced",
         f"Not an R². The two-horns standing gate's e2a instance (v2 rule 5(b), archive/CLAUDE-v2-cycles3-4.md@{PIN}:"
         f"{G3['v2_rule5']}-{G3['v2_rule5_src']}; prereg archive/RESULTS-cycles3-4.md@{PIN}:{G3['prereg']}-"
         f"{G3['prereg_bar'] + 1}, bar max |Δ| ≤ {g3j['gate']}). Reward axis (span-mean), L48, dose {g3j['dose']}, "
         f"steered KV context at task-round positions, text held identical, logit difference at the choice "
         f"position. Banked as rule 5(d) (CLAUDE.md@{PIN}:{G3['rule5d']}). PROPOSAL-e:{C['pe_247']}-{C['pe_248']} "
         f"names the (b) post-mortem as this gate's calibration source, so a reader can land here from the "
         f"note's 'calibration'. N1 must not attach it to the note's horn-1 0.53."),
    ]
    for r_ in rows_out:
        w("| " + " | ".join(cell(c) for c in r_) + " |")
    w("")
    w("## Verdict for N1's ledger")
    w("")
    w(f"R² = 0.53 is **log-only**: `{ARCH12}@{PIN}:{L_emp}` with its printed stdout at `{RAW_DIAG}@{PIN}:{RD_50}`, "
      f"entered at `{ec[:7]}`. It is not reproducible from committed JSON/JSONL/npz because the per-direction "
      f"values were saved only to the gitignored `{LOCAL_JSON}` in the clone. It is not discrepant: the committed "
      f"raw's printed table recomputes it at print precision, and the local-only JSON gives it at full precision.")
    w("")
    w("Notes for the PI, none of them a STOP:")
    w(f"- (a) Wording at `{PREPRINT}` :{', :'.join(map(str, P31 + P192))} and any equivalent sentence in the "
      f"note (P3): "
      f"'label logits' / 'decision-logit variance' should read 'the between-direction variance in the "
      f"label-choice probability P(keep)', with the scope stated (33 tail-PCA directions at full norm, L48, "
      f"Qwen3.6-27B-4bit, cycle 2, in-sample).")
    w("- (b) 'horn-1 calibration' (:192) and 'our calibration' (:222) should name the measurement, 'a cycle-2 "
      "diagnostic on Qwen (2026-08-06)'. In the record, 'calibration' next to horn 1 names the PROPOSAL-h "
      "H-calibration tier, whose horn-1 result is a different statistic (§1c, N6). N1 keeps this row apart from "
      "N6's horn-1 figures, and from e2a g3's max |Δ| = 0.5368, the two-horns gate instance that PROPOSAL-e's "
      "'calibration source' leads to (§1c).")
    w(f"- (c) :{', :'.join(map(str, P222))} attaches the magnitude to another group's on/off contrast (§7.6). "
      f"The record supports the qualitative horn-1 claim there, not the 0.53 for that contrast. Drop the number "
      f"at :{', :'.join(map(str, P222))} or keep it only with its scope.")
    w("- (d) If the PI wants the figure to be `reproduced`, the two local JSONs (the diagnostic's and the "
      "powered DV's) would need to be committed with a .gitignore allowlist entry. That is the PI's decision "
      "and is outside this audit's write scope.")
    w("")

    # ------------------------------------------------- values-check --------
    w("## Values-check")
    w("")
    w("### Round 1 (fixer pass over the checker's findings)")
    w("")
    w("One checker pass over the builder's script and raw (script sha256 67a4c415...61ca). The checker reported "
      "58 claims checked, a re-run identical apart from the stamp and command lines, a clean redaction check, "
      "and two substantive and six minor findings. Code (the fixer) verified each finding with its own tool run "
      "before applying or rejecting it. The evidence column cites values this run computed.")
    w("")
    pe_has = (C["pe_247"], C["pe_248"])
    vc = [
        ("1 (substantive)",
         "§7.5's 'the term is a gloss, consistent with use' and the §2 belief bullet: in the record, "
         "'calibration' next to horn 1 names PROPOSAL-h's H-calibration tier, whose horn-1 quantity is the "
         "paired-shadow leak (N6), not R² = 0.53; the line-level §1c search missed it.",
         "FIXED, with one correction to the finding.",
         f"The h-arc locators are confirmed (§1c: PROPOSAL-h :{C['ph_tier']}, :{C['ph_h1']}; LOCK-h "
         f":{C['lh_136']}, :{C['lh_153']}; FINDINGS-5 :{C['f5_6']}, :{C['f5_99']}, :{C['f5_103']}, "
         f":{C['f5_horn']}; HANDOFF-2026-08-22 :{C['ho_32']}). §1c is now paragraph-level, with "
         f"{len(cw)} hits. The diagnostic's entry has {n_cal_entry} 'calibrat' lines and FINDINGS-2 has "
         f"{n_cal_f2} 'calibration', as the finding says. The correction: the paragraph-level scan also finds "
         f"`PROPOSAL-e-reward-axis-hijack.md@{PIN}:{pe_has[0]}-{pe_has[1]}`, where the record calls "
         f"'(b)'s post-mortem' 'the calibration source' for the two-horns leakage gate. So the record attaches "
         f"the term to this diagnostic too, and 'the design seat was right about where the term lives' holds "
         f"only in part. §1c, §2, §7.5, a Figures homonym row and PI note (b) now say both."),
        ("2 (substantive)",
         "A third preprint carrier at :222, '(R² = 0.53 in our calibration)', applying the figure to another "
         "group's on/off contrast, was missed: the script searched two fixed needles.",
         "FIXED.",
         f"The carriers now come from the pattern `{CARRIER.pattern}` over the whole preprint, which gives lines "
         f"{PC}, asserted equal to the three needles. The untracked pre-patch copies carry the same lines "
         f"({', '.join(f'{p}: {v}' for p, v in pp.items())}). Added: a Figures row for :222, §7.6 (scope) and PI "
         f"notes (a)-(c)."),
        ("3 (minor)",
         "The row label 'R² on the log-odds scale of y (what label logits would carry)' overclaims: it is the "
         "log-odds of the 8-prompt-mean P(keep), not a label-logit quantity.",
         "FIXED.",
         f"Confirmed in the producing code ({loc_pk}: per-prompt P(keep)/(P(keep)+P(switch)), then the mean; "
         f"{cl(dpy, 'r_lo = pearson(logit(pk)', CLONE_DIAG_PY)}: the logit of that mean). No artifact carries per-prompt label logits under the all-positions vector: the stored "
         f"DV's keys are {lj.get('pow_keys') if lj else 'not read'}. The row is relabeled, §6 states the "
         f"difference, and the PI wording no longer offers the log-odds value for 'label logits'. The value is "
         f"unchanged ({llo2} full precision)."),
        ("4 (minor)",
         "The Figures table lacked the SD row that the builder summary listed, and the headline row lacked "
         "layer, dose and model (rule 6).",
         "FIXED.",
         f"Added the SD row (low-strain {sdc['low_sd1']:.4f} n−1 / {sdc['low_sd0']:.4f} n; full {sdc['all_sd1']:.4f} "
         f"n−1). The headline row's note now gives model, L48, frac 1.0 (α = R = 102.385), the 33 tail-PCA "
         f"directions (ranks {min(ranks)}-{max(ranks)}), in-sample, no CV."),
        ("5 (minor)",
         "The FINDINGS-2 window was cited at :1; it is at :8-9.",
         "FIXED.",
         f"Now `FINDINGS-2.md@{PIN}:{F2_title}` for 'second design cycle' (the title, asserted) and "
         f":{F2_win}-{F2_win + 1} for the window (asserted to contain 'through 2026-08-06')."),
        ("6 (minor)",
         "The archive parenthetical's log-odds +0.72 is a double rounding; 'read as the decisive arm's values "
         "they are right' overstates it.",
         "FIXED.",
         (f"Full precision from the local JSON: Δlogit row log-odds {par_['dlogit']['lo']:+.6f}, Spearman "
          f"{par_['dlogit']['rho']:+.6f}; reconstructed row log-odds {par_['recon']['lo']:+.6f}, Spearman "
          f"{par_['recon']['rho']:+.6f}. The row note is reworded: Spearman matches the Δlogit row; +0.72 is the "
          f"printed {gD['lo_r']:+.3f} rounded up; neither row gives +0.72 at full precision.") if par_ else
         "Reworded; the full-precision check was not run (local JSON absent)."),
        ("7 (minor)",
         "§1d's JSON search covered only data/e2b and data/e2d, narrower than the claim it supports.",
         "FIXED.",
         f"The key scan now covers every tracked *.json|*.jsonl at the pin ({len(all_json)} files, "
         f"unparsed {len(unparsed)}): {sum(keys_all.values())} R²-like key occurrences, all under data/echo/, "
         f"all round 2 of the echo recon's single-round masks or probe families named for it "
         f"(RESULTS.md@{PIN}:{L_rmask}). None outside data/echo/. The float scan stays on e2b/e2d, stated as "
         f"such."),
        ("8 (minor)",
         "The Fisher-z CI and the t-test treat 33 rule-selected directions as an i.i.d. sample.",
         "FIXED.",
         f"§4 and both Figures rows now say the sampling model is notional and cite the selection rule "
         f"({loc_sel}). The arithmetic was confirmed by the checker and is unchanged: t = {rr['t']:.3f}, "
         f"p = {rr['p_t']:.2e}, R² CI [{rr['fisher_ci_r'][0]**2:.3f}, {rr['fisher_ci_r'][1]**2:.3f}]."),
    ]
    w("| # | finding | disposition | evidence (this run) |")
    w("|---|---|---|---|")
    for num, fnd, disp, ev in vc:
        w(f"| {num} | {cell(fnd)} | {cell(disp)} | {cell(ev)} |")
    w("")
    w("The checker reported 18 independent recomputations, all agreeing with the builder's raw.")
    w("")
    w("Comparison with the builder's raw, as round 1 ran it (static text): round 1 passed `--prev` with the "
      "builder's raw, sha256 `1feef1bc8e871b956020d87b5f2119892b66b39ea297060aa2d5e9452afef776`, header lines "
      "excluded. Result: Figures rows 16 -> 19. No number in the builder's 'value printed' column was missing. "
      "One number anywhere in the builder's raw was missing, '0.51': the '≈ 0.51 on the log-odds scale' offered "
      "for 'label logits', withdrawn under finding 3. That file is a session-local scratch file, not committed, "
      "so the comparison cannot be re-run from the repository. The run of record therefore does not pass "
      "`--prev` (round 2, finding 4).")
    w("")
    J["values_check"] = [dict(n=a_, finding=b_, disposition=c_, evidence=d_) for a_, b_, c_, d_ in vc]

    # ----------------------------------------- values-check, round 2 -------
    # Evidence computed by this run.
    # (1) '\n'-only numbering: which tracked text files drift under str.splitlines(), and which of them this
    #     raw cites; the affected locators under both numberings.
    drift = []
    for p in all_text:
        t_ = ptext(p)
        if len(t_.splitlines()) != len(lines(t_)) - (1 if t_.endswith("\n") else 0):
            drift.append(p)
    SL2 = "results/raw/2026-08-04_slice2_gating_checks.txt"
    body_so_far = "\n".join(O)
    cited = sorted(set(re.findall(r"([A-Za-z0-9_./-]+\.(?:md|txt|json|jsonl|py))`?@" + PIN, body_so_far)))
    cited_drift = sorted(set(cited) & set(drift))
    sl2_t = ptext(SL2)
    sl2_new = [i for p, i, _ in rsq if p == SL2]
    sl2_old = [i for i, ln in enumerate(sl2_t.splitlines(), 1) if RSQ_VAL.search(ln)]
    pow_new = (min(v["line"] for v in prow.values()), max(v["line"] for v in prow.values()))
    pow_old_l = [i for i, ln in enumerate(rp.splitlines(), 1) if ROW_POW.match(ln)]
    pow_old = (min(pow_old_l), max(pow_old_l))
    sl2_cat = [lines(sl2_t)[i - 1].strip()[:60] for i in sl2_new]
    fig_start = O.index("## Figures (as the block writes them, plus the record figures the sentence leans on)")
    fig_end = O.index("## Verdict for N1's ledger")
    fig_hits = sum(1 for l_ in O[fig_start:fig_end] if SL2 in l_ or RAW_POW in l_)
    # (2) what the '53%' alternation adds to 1b
    HAS_53_OLD = re.compile(r"(?<![\d.])0?\.53(?:0)?(?![\d])")
    l53_new_only = [f"{p}:{i}" for p, i, s_ in l53 if not HAS_53_OLD.search(s_)]
    # (3) g3's own bar rationale; does the cycles-3/4 log mention the post-mortem at all?
    g3_bar_txt = " ".join(ln.strip() for ln in lines(a34_t)[G3["prereg_bar"] - 1: G3["prereg_bar"] + 1])
    m_rat = re.search(r"\(≈ ≤2\.5% choice-probability shift, an order below the effect bar\)", g3_bar_txt)
    assert m_rat, g3_bar_txt
    g3_rat = m_rat.group(0)
    n_pm_34 = sum(1 for ln in lines(a34_t) if re.search(r"post-mortem", ln, re.I))
    # (4) does this run pass --prev?
    prev_given = bool(args.prev)
    vc2 = [
        ("R2-1 (minor)",
         "§1a's slice-2 locators (:28, :29, :34) and §4's powered-DV range (:10-42) are wrong. The script numbered "
         "lines with str.splitlines(), which also splits on '\\r', and both raws carry tqdm '\\r's.",
         "FIXED, as the fix says.",
         f"Every locator-producing split now goes through `lines()` (split on '\\n' only). {len(drift)} of the "
         f"{len(all_text)} tracked *.md|*.txt at the pin number differently under the two splits. This raw cites "
         f"{len(cited)} distinct paths with an @{PIN} locator, and only {len(cited_drift)} of them are among the "
         f"{len(drift)}: {cited_drift}. Slice-2 R² lines are now :{', :'.join(map(str, sl2_new))} (splitlines "
         f"gave :{', :'.join(map(str, sl2_old))}): {sl2_cat}. The powered-DV table is now :{pow_new[0]}-"
         f"{pow_new[1]} (splitlines gave :{pow_old[0]}-{pow_old[1]}). Figures-table lines citing either raw: "
         f"{fig_hits}, so N1's ledger rows are unaffected."),
        ("R2-2 (minor)",
         "FINDINGS-2.md@bbc9ffe:51 carries the figure as '~53% of its variance' and is missing from the "
         "summary carriers. The 1b pattern needed an R² token or 0.53 / .53 / .530.",
         "FIXED, as the fix says.",
         f"1b's pattern now has a '53%' alternation (`{HAS_53.pattern}`). 1b has {len(l53)} lines, and the "
         f"alternation adds exactly {l53_new_only}. FINDINGS-2:{F2_51} is now in §2's summary carriers, with "
         f"its 'its' resolved to the (b) DV, P(keep), at :{F2_its}-{F2_its + 1}. It is also in the FINDINGS-2 "
         f"Figures row (:{F2_51}, :{F2_129}, :{F2_175}, :{F2_244})."),
        ("R2-3 (minor)",
         "A closer homonym was missed: e2a's g3 KV-leakage gate, the two-horns standing gate's instance. It "
         "measured max |Δ(logit_A − logit_B)| = 0.5368 (data/e2a/g3_kv_leakage.json:max_abs).",
         "FIXED, as the fix says. Its link to the two-horns gate is taken from the record.",
         f"Read at the pin: max_abs {g3j['max_abs']!r} and mean_abs {g3j['mean_abs']:.4f}; recomputed over "
         f"{len(g3_rows)} rows, {g3_max:.5f} and {g3_mean:.4f}; dose {g3j['dose']}, gate {g3j['gate']}, "
         f"pass {g3j['pass']}. The JSON has no layer or axis key. Reward axis and L48 come from the e2a "
         f"pre-registration's drug line (archive/RESULTS-cycles3-4.md@{PIN}:{G3['drug']}-{G3['drug_L']}). The "
         f"two-horns link is in the record: g3 is pre-registered as 'KV-leakage gate (rule 5)' (:{G3['prereg']}), "
         f"and v2 rule 5 is the 'Two-horns standing gate', sourced to the (b) post-mortem "
         f"(archive/CLAUDE-v2-cycles3-4.md@{PIN}:{G3['v2_rule5']}-{G3['v2_rule5_src']}). PROPOSAL-e:"
         f"{C['pe_pm']} says the standing gate's threshold is 'set from the (b) post-mortem'. g3's "
         f"pre-registration gives its 0.10 bar its own rationale, '{g3_rat}' (:{G3['prereg_bar']}), and "
         f"archive/RESULTS-cycles3-4.md has {n_pm_34} lines with 'post-mortem'. So this raw does not claim the "
         f"0.10 bar was set from the post-mortem. Added a Figures "
         f"homonym row (status reproduced: the value is read from committed JSON) and the §1c second-bullet "
         f"text; PI note (b) and the §1 reading mention it."),
        ("R2-4 (minor)",
         "The header command passed `--prev` with an uncommitted scratch path, so the closing comparison could "
         "not be reproduced from the repository.",
         "FIXED (the fix's second option).",
         f"This run passes --prev: {prev_given}. Round 1's comparison is kept above as static text, with the "
         f"builder raw's sha256 and the statement that the file is session-local and uncommitted. `--prev` "
         f"still works. When it is passed, its comparison is printed under a separate heading marked as not "
         f"part of the run of record."),
        ("R2-5 (minor)",
         "§3's '.gitignore:113:/data/configs/*' came from a working-tree `git check-ignore` and was not pinned; "
         ".gitignore changed after bbc9ffe.",
         "FIXED, as the fix says.",
         f"Now `.gitignore@{PIN}:{ign_ln}` ('{ign_pat}') and `.gitignore@{PIN}:{gi_clone}` ('/{CLONE}/'). The "
         f"script reads the rule's line number from check-ignore and asserts that the pinned and working-tree "
         f"lines are equal. The pinned file has {gi_pin_n} lines and the working tree {gi_wt_n}; the working "
         f"tree's first line that differs from the pin is :{gi_first_diff}, after :{ign_ln}. It also asserts "
         f"that no pinned line names "
         f"dv_logit or slice3_dv (found: {gi_pin_dv})."),
    ]
    w("### Round 2 (residual findings)")
    w("")
    w(f"One residual-findings pass over round 1's script and raw (script sha256 769e9dda...4cbb). Five minor "
      f"findings, none substantive. Code verified each with its own tool run before applying it, and all five "
      f"are applied. The evidence column cites values this run computed.")
    w("")
    w("| # | finding | disposition | evidence (this run) |")
    w("|---|---|---|---|")
    for num, fnd, disp, ev in vc2:
        w(f"| {num} | {cell(fnd)} | {cell(disp)} | {cell(ev)} |")
    w("")
    J["values_check_round2"] = [dict(n=a_, finding=b_, disposition=c_, evidence=d_) for a_, b_, c_, d_ in vc2]
    J["values_check_round2_data"] = dict(drift_files=drift, cited=cited, cited_drift=cited_drift,
                                         slice2_new=sl2_new, slice2_old=sl2_old, powered_new=pow_new,
                                         powered_old=pow_old, l53_new_only=l53_new_only, prev_given=prev_given)
    if args.prev:
        w("### Optional `--prev` comparison (not part of the run of record; the --prev file is session-local)")
        w("")
        prev_lines = open(args.prev, encoding="utf-8").read().splitlines()
        prev_sha = sha256(open(args.prev, "rb").read())
        NUM = re.compile(r"[-+−]?\d+\.\d+(?:e-?\d+)?")

        def fig_values(lns):
            out, on = [], False
            for l_ in lns:
                if l_.startswith("## Figures"):
                    on = True
                    continue
                if l_.startswith("## Verdict"):
                    on = False
                if on and l_.startswith("| ") and not l_.startswith("| figure"):
                    out.append([c.strip() for c in re.split(r"(?<!\\)\|", l_)[1:-1]])
            return out
        cur_lines = "\n".join(O).splitlines()
        pv, cv = fig_values(prev_lines), fig_values(cur_lines)
        lost_val = sorted({t for r in pv for t in NUM.findall(r[1])} - {t for r in cv for t in NUM.findall(r[1])})
        lost_doc = sorted(set(NUM.findall("\n".join(prev_lines[9:]))) - set(NUM.findall("\n".join(cur_lines[9:]))))
        w(f"Comparison with the `--prev` file (sha256 `{prev_sha}`; header lines excluded): Figures rows "
          f"{len(pv)} -> {len(cv)}; numbers in its 'value printed' column missing here: {lost_val}; numbers "
          f"anywhere in it missing here: {lost_doc}.")
        J["prev_compare"] = dict(prev_sha=prev_sha, lost_values=lost_val, lost_doc=lost_doc)
        w("")

    out = args.out if os.path.isabs(args.out) else os.path.join(REPO, args.out)
    with open(out, "w") as f:
        f.write("\n".join(O))
    if args.json_out:
        jo = args.json_out if os.path.isabs(args.json_out) else os.path.join(REPO, args.json_out)
        with open(jo, "w") as f:
            json.dump(J, f, indent=2, default=str)
    print(f"wrote {os.path.relpath(out, REPO)} ({len(O)} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
