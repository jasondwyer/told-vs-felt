#!/usr/bin/env python3
"""AUDIT-note-release v1.2, item N7 -- OLMo Q1/Q3 and the dose ladder.

READ-ONLY ON THE RECORD. Every committed artifact is read at the pin
(`git show bbc9ffe:<path>`); the record's own pure helpers
(scripts/box_a4_instrument.build_instruments, scripts/b3_analyze.analyze,
valence_core.stats) are imported from the working tree only after their blobs
(and the blobs of everything they import from the repository) are asserted
equal to the pinned blobs. Nothing is written except the two outputs
(--out, --json-out). No model is loaded. numpy is used only to open the
committed instrument stores (data/olmo/a4_instrument_*.npz) and inside the
record's own build_instruments; every exact test is stdlib (math.comb).
Bytecode writing is disabled so no __pycache__ appears in the repository.

What it does (block AUDIT-note-release-v1_2.md:103-104):
  1. G_c per stage, three ways: the stored field; the mean of the stored
     per-probe g_q; a full rebuild from the committed top-4,096 marker stores
     through the record's own build_instruments (plus an independent,
     tie-agnostic numpy rebuild as a robustness line, computed-new). Pass 2
     adds the instrument's anatomy (computed-new, post-hoc): which tokens the
     stored selections hold, how much of the val-half readout is imputed
     floor, how closely the score tracks the context floor, a floor-only gap,
     a true per-row floor-imputed rebuild, and the same construction on the
     pinned Qwen B1 store (data/e0/e0_b1_markers.npz) as a cross-reference
     for N8.
  2. A4: layer selection (fit half), the dose ladder (val half), the envelope
     conjunction recomputed from the stored deltas and controls, MEDs, sham,
     D+/G_c, the V1-lineage context rule, and B1's registered mapping.
  3. The Fisher p = .0047 allocation note: its table, its test, and the
     registered [g3-B] criterion it sits beside.
  4. Q3: the screen recomputed from session records (independently and via
     the committed analyzer), confirm triggers, the falsifier, the welfare
     extension, the DPO single-map figure, and the per-stage four-number line
     with n and map split (descriptive exact p's labelled post-hoc).

Usage (from anywhere):
  jlens-qwen36/.venv/bin/python scripts/audit_note_N7.py \
      [--out results/raw/2026-10-08_note-N7-olmo.md] \
      [--json-out results/raw/2026-10-08_note-N7-olmo.json]

Deterministic apart from the run-metadata lines (stamp, HEAD at run time,
command line, wall-clock). No randomness is used anywhere.

Round 9 (2026-10-10; Tier 1, before N1 round 9): re-pointed at the patched
preprint per the PI's ruling 9 of 2026-10-10, as corrected. The preprint of
record is PREPRINT-v1_0-draft.md at sha256 0f4ba501...16c22 (patch v6),
asserted where the block's d6431e97...222b8 was; that value is recorded as the
audited, superseded text, archived untracked at
archive/PREPRINT-v1_0-draft.pre-patch-v6.md (out of the release; this script
never reads or requires it). Every preprint locator, quoted preprint
sentence and figure label taken from the preprint's words is re-anchored on
the patched text and tabulated against its round-1 line, and every preprint
line or section number written into this raw's text is checked (section
'Preprint of record (round 9)', appended at the end of the raw so that every
round-1 line keeps its number); a sentence no longer found is recorded there
once, as a finding on the patch for the design seat, not a STOP. Nothing not
tied to the preprint changed.

Round 10 (2026-10-12; Tier 1, before N1 round 10): re-pointed at patch v7 per
the PI's routing of 2026-10-12. The preprint of record is PREPRINT-v1_0-draft.md
at sha256 d9635ca2...d1fe6 (patch v7), asserted where round 9 asserted
0f4ba501...16c22, before anything is written (a different or absent text
refuses the run). Round 9's preprint of record (patch v6, 0f4ba501...16c22) is
recorded, never required: it is archived untracked at
archive/PREPRINT-v1_0-draft.pre-patch-v7.md (out of the release) and is read
only if present and matching, to list the lines v7 changed and to quote a v6
line beside its v7 line. The audited text's handling (d6431e97...222b8,
archive/PREPRINT-v1_0-draft.pre-patch-v6.md, the round-1 raw @09c3a8c) is as
round 9 left it. Round 9's section re-runs every check of a preprint sentence on
the v7 text; its subsection 'Round 10 (patch v7)' reads round 9's raw at 84801cb
and gives, per check, its result on v6 (as committed) and on v7, the
disposition on v7 of each finding on the patch that raw recorded, and every new
finding v7 introduces (a check that passed on v6 and fails on v7); a checked
sentence on a line v7 changed is flagged in its disposition and quoted
v6-beside-v7, not counted as a finding. JSON: one new key, preprint_round10.
Nothing not tied to the preprint changed.
"""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True

import argparse
import hashlib
import importlib
import io
import json
import math
import os
import platform
import re
import shlex
import subprocess
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = "bbc9ffe"
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
PREPRINT = "PREPRINT-v1_0-draft.md"     # untracked; sha-checked, working tree
# Round 9: the preprint of record is the patched text (patch v6), the PI's ruling 9 of
# 2026-10-10 as corrected. The block's d6431e97...222b8 is the audited, superseded text,
# archived untracked at PREPRINT_ARCHIVED; recorded, never read or required.
# Round 10: the preprint of record is patch v7 (the PI's routing of 2026-10-12). Round 9's
# patch-v6 text is archived untracked at PREPRINT_ARCHIVED_V6, out of the release: recorded,
# never required; read only if present and matching.
PREPRINT_SHA = "d9635ca24d32dcba193cd9aade273de2679c99c5c2218787b410e793a42d1fe6"
PREPRINT_SHA_V6 = "0f4ba501d60a94189e6dc83d28c41826debe50591b9af484fa08d05a41f16c22"
PREPRINT_ARCHIVED_V6 = "archive/PREPRINT-v1_0-draft.pre-patch-v7.md"
PREPRINT_ROUTING = "the PI's routing of 2026-10-12"
ROUND9_COMMIT = "84801cb"          # round 9's raws (patch v6), read at this commit
PREPRINT_SHA_AUDITED = "d6431e97d35e5914574ff9884c0e64463a7baf1cf9d279f27ed45a683a6222b8"
PREPRINT_ARCHIVED = "archive/PREPRINT-v1_0-draft.pre-patch-v6.md"
PREPRINT_RULING = "the PI's ruling 9 of 2026-10-10, as corrected"
# Every preprint sentence this script locates (loc), quotes, or takes a figure label's words
# from ("label"), with its round-1 line on the audited text as the committed round-1 raw
# cites it (09c3a8c:results/raw/2026-10-08_note-N7-olmo.md; () = no line locator there).
PREPRINT_R1 = {
    "rises across the lineage (+0.78 base": ("located", (101,)),
    "(G_c: +0.78 → +1.03 → +1.53 → +1.56)": ("located", (129,)),
    "the base model passes at layer 60": ("located", (129,)),
    "Sham contrasts are exactly zero at every stage": ("located", (129,)),
    "about five times larger at base": ("located", (129,)),
    "The registered criterion was a conjunction of envelope conditions": ("located", (127,)),
    "Per-stage minimum effective doses qualify at f = 0.05 (base, L60)": ("located", (139,)),
    "[TAB 2: every cell": ("located", (170,)),
    "Four nulls; zero confirmatory triggers": ("located", (184,)),
    "In the OLMo DPO screen one map returned +0.1667": ("located", (190,)),
    "feedback-driven training sharpens the marking of evaluation": ("located", (244,)),
    "in direction units": ("quoted", (101, 129)),
    "the direction's separation of praise from criticism contexts": ("quoted", (127,)),
    "sharpens the marking it inherits": ("quoted", (129,)),
    "feedback-driven training sharpens the marking of evaluation (G_c rises monotonically)":
        ("quoted", (244,)),
    "TAB 2 carries the per-stage figures": ("quoted", ()),
    "ratio of steering displacement to natural contrast": ("label", ()),   # cited by §5.1
    "All four stages pass the conjunction": ("label", ()),
    "doses of 1.0 or below": ("label", ()),
}
# Preprint line or section numbers written as literals into this raw's text:
# (as written, where, sentence it names, lines | section number).
PREPRINT_HARD = (
    ("§5.1", "figure label 'ratio of steering displacement to natural contrast ~5x larger at "
     "base (preprint §5.1)'", "ratio of steering displacement to natural contrast", "5.1"),
    (":244", "Values-check pass 1 #9: 'PREPRINT :244 missing from the 'sharpens' note'",
     "feedback-driven training sharpens the marking of evaluation", (244,)),
    (":129/:244", "Values-check pass 2 #1: ':129/:244's 'sharpens the marking''",
     "sharpens the marking", (129, 244)),
)
PRE_SEEN: dict[str, list[int]] = {}      # round 9: sentence -> its lines in the patched text
PRE_FINDINGS: list[dict] = []            # round 9: sentences not found (findings on the patch)
DEF_OUT = "results/raw/2026-10-08_note-N7-olmo.md"
DEF_JSON = "results/raw/2026-10-08_note-N7-olmo.json"
STAGES = ("base", "sft", "dpo", "instruct")
FRACS = ("0.05", "0.1", "0.2", "0.4")
CP_NEEDLE = "CP upper 0.1425 while s=2's CP"   # next line: 'lower is 0.1260'

# Everything imported from the working tree; each blob must equal the pin.
IMPORTED = ("scripts/box_a4_instrument.py", "scripts/box_e0_corpus.py",
            "scripts/b3_analyze.py", "valence_core/__init__.py",
            "valence_core/adapters/__init__.py", "valence_core/adapters/base.py",
            "valence_core/discrim.py", "valence_core/extract.py",
            "valence_core/stats.py")
# Producer/analyzer scripts named by the block: read, not run.
READ_ONLY_CODE = ("scripts/b1_verdict.py", "scripts/b3_analyze.py",
                  "scripts/box_a4_hijack.py", "scripts/box_b3_sessions.py",
                  "scripts/box_a4_instrument.py", "scripts/b2r_analyze.py",
                  "valence_core/regression/oracle.py", "valence_core/session.py")


# ----------------------------------------------------------------- plumbing --
def git(*args: str) -> bytes:
    """Read-only git only."""
    assert args[0] in ("show", "rev-parse", "ls-tree", "ls-files"), args
    return subprocess.run(["git", "--no-optional-locks", "-C", REPO, *args],
                          check=True, capture_output=True).stdout


_CACHE: dict[str, bytes] = {}


def pinned(path: str) -> bytes:
    if path not in _CACHE:
        _CACHE[path] = git("show", f"{PIN}:{path}")
    return _CACHE[path]


def pinned_text(path: str) -> str:
    return pinned(path).decode("utf-8")


def pinned_json(path: str):
    return json.loads(pinned_text(path))


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def blob_sha1(b: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def blob_equal_to_pin(path: str) -> bool:
    with open(os.path.join(REPO, path), "rb") as f:
        wt = blob_sha1(f.read())
    return wt == git("rev-parse", f"{PIN}:{path}").decode().strip()


def lines_of(text: str) -> list[str]:
    return text.split("\n")          # as `git show | sed -n` counts them


def loc(path: str, needle: str, working_tree: bool = False, extra: int = 0) -> str:
    """'path@bbc9ffe:N' (or N-(N+extra)) for the first line containing needle
    (asserted)."""
    if working_tree:
        with open(os.path.join(REPO, path), encoding="utf-8") as f:
            text = f.read()
    else:
        text = pinned_text(path)
    hits = [i for i, l in enumerate(lines_of(text), 1) if needle in l]
    if working_tree and path == PREPRINT:      # round 9: never a STOP on the preprint
        PRE_SEEN.setdefault(needle, hits)
        if not hits:
            return preprint_finding(needle, lines_of(text))
    if not hits:
        raise SystemExit(f"LOCATOR NOT FOUND: {needle!r} in {path}")
    tag = f"{path}{'' if working_tree else '@' + PIN}:{hits[0]}"
    if extra:
        tag += f"-{hits[0] + extra}"
    return tag if len(hits) == 1 else tag + f" (+{len(hits) - 1} more)"


def preprint_finding(needle: str, plines: list[str]) -> str:
    """Round 9 (ruling 9): a preprint sentence this script checks is not on the patched
    text. Recorded as a finding on the patch (old line: round-1 locator on the audited
    text, with the sentence as checked; new line: the patched text at that line number),
    routed to the design seat; the run continues. A sentence checked more than once is
    recorded once (its existing P-number is returned). Round 10: the patched text is
    patch v7, so these are findings on patch v7, numbered afresh."""
    for i, p in enumerate(PRE_FINDINGS, 1):
        if p["sentence_as_checked"] == needle:
            return f"{PREPRINT}:NOT FOUND (finding on patch v7 P{i})"
    r1 = PREPRINT_R1.get(needle, ("unlisted", ()))[1]
    PRE_FINDINGS.append({
        "sentence_as_checked": needle,
        "old": {"sha256": PREPRINT_SHA_AUDITED, "round1_lines": list(r1)},
        "new": {"sha256": PREPRINT_SHA,
                "line_text_at_round1_lines": {str(n): plines[n - 1] for n in r1
                                              if n <= len(plines)}},
        "routed_to": "the design seat (a finding on the patch; " + PREPRINT_RULING + ")"})
    return f"{PREPRINT}:NOT FOUND (finding on patch v7 P{len(PRE_FINDINGS)})"


def cell(s) -> str:
    return str(s).replace("|", "\\|")


def f4(x: float) -> str:
    return f"{x:+.4f}"


# ------------------------------------------------------- stdlib exact tests --
def binom_pmf(k: int, n: int, p: float) -> float:
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def binom_sf(k: int, n: int, p: float) -> float:
    """P(X >= k)."""
    return sum(binom_pmf(i, n, p) for i in range(max(k, 0), n + 1))


def binom_cdf(k: int, n: int, p: float) -> float:
    """P(X <= k)."""
    return sum(binom_pmf(i, n, p) for i in range(0, min(k, n) + 1))


def binom_half_exact(k: int, n: int) -> tuple[float, float]:
    """(one-sided upper P(X>=k), two-sided 2*min tail capped at 1) at p=1/2,
    exact in integers."""
    up = sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n
    lo = sum(math.comb(n, i) for i in range(0, k + 1)) / 2 ** n
    return up, min(1.0, 2 * min(up, lo))


def fisher_upper(a: int, b: int, c: int, d: int) -> float:
    """One-sided Fisher exact for [[a, b], [c, d]]: P(X >= a) under the
    hypergeometric with both margins fixed."""
    n, r1, c1 = a + b + c + d, a + b, a + c
    hi = min(r1, c1)
    return sum(math.comb(r1, i) * math.comb(n - r1, c1 - i)
               for i in range(a, hi + 1)) / math.comb(n, c1)


def clopper_pearson(k: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    """Exact two-sided interval by bisection (stdlib; same construction as
    the record's b2_analyze.clopper_pearson, written independently)."""
    lo, hi = 0.0, 1.0
    if k > 0:
        a, b = 0.0, 1.0
        for _ in range(200):
            m = (a + b) / 2
            if binom_sf(k, n, m) < alpha / 2:
                a = m
            else:
                b = m
        lo = (a + b) / 2
    if k < n:
        a, b = 0.0, 1.0
        for _ in range(200):
            m = (a + b) / 2
            if binom_cdf(k, n, m) > alpha / 2:
                a = m
            else:
                b = m
        hi = (a + b) / 2
    return lo, hi


# ------------------------------------- instrument anatomy (computed-new) --
def instrument_anatomy(np, top_ids, top_vals, qidx, in_fit, is_pos, sels, ws,
                       stored_gq=None, sel_n: int = 256) -> dict:
    """Computed-new, post-hoc, model-free: what a set of per-probe A4-style
    instruments (sel ids + weights) select, and what their val-half score
    tracks. Reads only the top-4,096 store. Per probe:
      - presence of each selected id among the fit-half contexts of each pole
        (a context 'holds' an id when the id is in its stored top-4,096);
      - weight signs and the coefficient of variation of |w|;
      - the fit-half and val-half mean floor per pole (floor = min kept - 2.0);
      - on the val half, the share of instrument cells (selected id x context)
        that are floor-imputed, the instrument score (scored as the record
        does: each context's floor for an id outside its top-4,096), its
        Pearson r with the context's floor, g_q, and a floor-only gap (the
        context floor oriented by the sign of the probe's mean weight);
      - a true per-row floor-imputed rebuild: per-pole fit means in which a
        context lacking the id contributes that context's own floor; top-256
        by |difference| (ties by ascending id); same val scoring.
    """
    ids = np.asarray(top_ids).astype(np.int64)
    vals = np.asarray(top_vals)
    srt = np.sort(ids, axis=1)
    assert (np.diff(srt, axis=1) != 0).all(), "a stored row repeats an id"
    floor32 = vals.min(axis=1) - 2.0          # float32, as the record computes it
    floor = floor32.astype(np.float64)
    V = int(ids.max()) + 1

    def val_scores(rows, sel, wv):
        pos_of = np.full(V, -1, dtype=np.int64)
        pos_of[sel] = np.arange(len(sel))
        X = np.repeat(floor[rows][:, None], len(sel), axis=1)
        imp = np.ones(X.shape, dtype=bool)
        t = pos_of[ids[rows]]
        rr, cc = np.where(t >= 0)
        X[rr, t[rr, cc]] = vals[rows][rr, cc].astype(np.float64)
        imp[rr, t[rr, cc]] = False
        return X @ wv, imp

    def gap(a, b):
        sd = float(np.sqrt((a.var(ddof=1) + b.var(ddof=1)) / 2))
        return float((a.mean() - b.mean()) / (sd + 1e-12))

    per = []
    neg_hold_hist: dict[int, int] = {}
    pos_hold_hist: dict[int, int] = {}
    for q, (sel, wv) in enumerate(zip(sels, ws)):
        sel = np.asarray(sel, dtype=np.int64)
        wv = np.asarray(wv, dtype=np.float64)
        qm = qidx == q
        rp = np.where(qm & in_fit & is_pos)[0]
        rn = np.where(qm & in_fit & ~is_pos)[0]
        cp = np.zeros(V, dtype=np.int64)
        cn = np.zeros(V, dtype=np.int64)
        np.add.at(cp, ids[rp].ravel(), 1)
        np.add.at(cn, ids[rn].ravel(), 1)
        for t in sel:
            neg_hold_hist[int(cn[t])] = neg_hold_hist.get(int(cn[t]), 0) + 1
            pos_hold_hist[int(cp[t])] = pos_hold_hist.get(int(cp[t]), 0) + 1
        rv = np.where(qm & ~in_fit)[0]
        isp = is_pos[rv]
        sc, imp = val_scores(rv, sel, wv)
        g = gap(sc[isp], sc[~isp])
        if stored_gq is not None:
            assert abs(g - stored_gq[q]) < 1e-9, (q, g, stored_gq[q])
        fo = floor[rv] * float(np.sign(wv.mean()))
        # true per-row floor-imputed rebuild
        sp_, sn_ = np.zeros(V), np.zeros(V)
        np.add.at(sp_, ids[rp].ravel(), vals[rp].ravel().astype(np.float64))
        np.add.at(sn_, ids[rn].ravel(), vals[rn].ravel().astype(np.float64))
        fp_, fn_ = np.zeros(V), np.zeros(V)
        np.add.at(fp_, ids[rp].ravel(), np.repeat(floor[rp], ids.shape[1]))
        np.add.at(fn_, ids[rn].ravel(), np.repeat(floor[rn], ids.shape[1]))
        keys = np.where((cp > 0) | (cn > 0))[0]
        # the record's own per-token difference (absent context -> 0; whole-pole absence ->
        # that pole's mean floor), recomputed here to locate the selection cut
        d_rec = (np.where(cp[keys] > 0, sp_[keys], floor[rp].mean() * len(rp)) / len(rp)
                 - np.where(cn[keys] > 0, sn_[keys], floor[rn].mean() * len(rn)) / len(rn))
        a_rec = np.sort(np.abs(d_rec))[::-1]
        shared = (cp[keys] > 0) & (cn[keys] > 0)
        d_true = ((sp_[keys] + floor[rp].sum() - fp_[keys]) / len(rp)
                  - (sn_[keys] + floor[rn].sum() - fn_[keys]) / len(rn))
        o = np.lexsort((keys, -np.abs(d_true)))[:sel_n]
        sel_t = keys[o]
        w_t = d_true[o] / (np.linalg.norm(d_true[o]) + 1e-12)
        sc_t, _ = val_scores(rv, sel_t, w_t)
        absw = np.abs(wv)
        per.append({
            "probe": q, "n_fit_pos": int(len(rp)), "n_fit_neg": int(len(rn)),
            "n_val": int(len(rv)),
            "sel_absent_all_pos_present_neg": int(((cp[sel] == 0) & (cn[sel] > 0)).sum()),
            "sel_absent_all_neg_present_pos": int(((cn[sel] == 0) & (cp[sel] > 0)).sum()),
            "sel_present_both": int(((cp[sel] > 0) & (cn[sel] > 0)).sum()),
            "w_all_negative": bool((wv < 0).all()), "w_all_positive": bool((wv > 0).all()),
            "cv_abs_w": float(absw.std() / absw.mean()),
            "fit_mean_floor_pos": float(floor[rp].mean()),
            "fit_mean_floor_neg": float(floor[rn].mean()),
            "val_mean_floor_pos": float(floor[rv][isp].mean()),
            "val_mean_floor_neg": float(floor[rv][~isp].mean()),
            "val_share_cells_floor_imputed": float(imp.mean()),
            "r_score_floor": float(np.corrcoef(sc, floor[rv])[0, 1]),
            "g_q": g, "g_floor_only": gap(fo[isp], fo[~isp]),
            "g_true_floor_rebuild": gap(sc_t[isp], sc_t[~isp]),
            "true_floor_selection_differs": set(sel_t.tolist()) != set(sel.tolist()),
            "cut_abs_diff_256th": float(a_rec[sel_n - 1]),
            "max_abs_diff_shared": float(np.abs(d_rec[shared]).max()) if shared.any() else 0.0,
            "n_shared_tokens": int(shared.sum())})
    nq = len(per)
    r = [p["r_score_floor"] for p in per]
    sh = [p["val_share_cells_floor_imputed"] for p in per]
    cv = [p["cv_abs_w"] for p in per]
    return {
        "per_probe": per, "n_probes": nq, "n_selected": nq * sel_n,
        "sel_absent_all_pos_present_neg": sum(p["sel_absent_all_pos_present_neg"] for p in per),
        "sel_absent_all_neg_present_pos": sum(p["sel_absent_all_neg_present_pos"] for p in per),
        "sel_present_both": sum(p["sel_present_both"] for p in per),
        "neg_fit_contexts_holding_selected_id": dict(sorted(neg_hold_hist.items())),
        "pos_fit_contexts_holding_selected_id": dict(sorted(pos_hold_hist.items())),
        "fit_contexts_per_pole": sorted({(p["n_fit_pos"], p["n_fit_neg"]) for p in per}),
        "n_val_per_probe": sorted({p["n_val"] for p in per}),
        "probes_w_all_negative": sum(p["w_all_negative"] for p in per),
        "probes_w_all_positive": sum(p["w_all_positive"] for p in per),
        "cv_abs_w_range": [min(cv), max(cv)],
        "probes_fit_floor_lower_post_praise": sum(p["fit_mean_floor_pos"] < p["fit_mean_floor_neg"]
                                                  for p in per),
        "probes_val_floor_lower_post_praise": sum(p["val_mean_floor_pos"] < p["val_mean_floor_neg"]
                                                  for p in per),
        "mean_fit_floor_pos": float(np.mean([p["fit_mean_floor_pos"] for p in per])),
        "mean_fit_floor_neg": float(np.mean([p["fit_mean_floor_neg"] for p in per])),
        "val_share_floor_imputed_mean": float(np.mean(sh)),
        "val_share_floor_imputed_range": [min(sh), max(sh)],
        "r_score_floor_mean": float(np.mean(r)),
        "abs_r_score_floor_mean": float(np.mean(np.abs(r))),
        "abs_r_score_floor_weakest": float(np.min(np.abs(r))),
        "G": float(np.mean([p["g_q"] for p in per])),
        "G_floor_only": float(np.mean([p["g_floor_only"] for p in per])),
        "G_true_floor_rebuild": float(np.mean([p["g_true_floor_rebuild"] for p in per])),
        "true_floor_selection_differs_probes": sum(p["true_floor_selection_differs"] for p in per),
        "min_cut_abs_diff_256th": min(p["cut_abs_diff_256th"] for p in per),
        "max_abs_diff_shared": max(p["max_abs_diff_shared"] for p in per),
        "probes_cut_above_every_shared": sum(p["cut_abs_diff_256th"] > p["max_abs_diff_shared"]
                                             for p in per),
        "min_margin_cut_minus_shared": min(p["cut_abs_diff_256th"] - p["max_abs_diff_shared"]
                                           for p in per)}


# ------------------------------------------------------------------- main --
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEF_OUT)
    ap.add_argument("--json-out", default=DEF_JSON)
    args = ap.parse_args()
    t_start = time.time()

    md: list[str] = []
    J: dict = {"item": "N7", "title": "OLMo Q1/Q3 and dose ladder"}
    FIG: list[dict] = []
    NOTES: list[str] = []
    CHECKS: dict[str, bool] = {}      # each 'reproduced' status is licensed by one of these
    STOPS: list[str] = []             # a reproduction that would need an analyzer change
    w = md.append

    def fig(figure, printed, source, status, note=""):
        FIG.append({"figure": figure, "printed": printed, "source": source,
                    "status": status, "note": note})

    # ---------------------------------------------------------- header --
    stamp = subprocess.run(["date", "-u"], check=True, capture_output=True,
                           text=True).stdout.strip()
    head = git("rev-parse", "HEAD").decode().strip()
    pin_full = git("rev-parse", PIN).decode().strip()
    block_pin = pinned(BLOCK)
    block_sha_pin = sha256(block_pin)
    with open(os.path.join(REPO, BLOCK), "rb") as f:
        block_sha_wt = sha256(f.read())
    blines = lines_of(block_pin.decode())
    n7 = [i for i, l in enumerate(blines, 1) if l.startswith("### N7.")][0]
    script_rel = "scripts/audit_note_N7.py"
    with open(os.path.join(REPO, script_rel), "rb") as f:
        script_sha = sha256(f.read())
    import numpy as np                       # opens the committed npz stores
    # The echo is runnable from anywhere: cwd made explicit, script path
    # absolute (REPO is resolved from __file__, so outputs land the same).
    cmd = (f"cd {shlex.quote(REPO)} && "
           + shlex.join([sys.executable, os.path.abspath(sys.argv[0])] + sys.argv[1:]))
    run_cwd = os.getcwd()
    with open(os.path.join(REPO, PREPRINT), "rb") as f:
        pre_sha = sha256(f.read())
    assert pre_sha == PREPRINT_SHA, "preprint sha mismatch"
    tracked_pre = git("ls-files", PREPRINT).decode().strip()

    w("# AUDIT-note-release v1.2 -- N7: OLMo Q1/Q3 and the dose ladder")
    w("")
    w(f"- Code stamp: {stamp} (date -u)  [run metadata]")
    w(f"- HEAD at run time: {head}  [run metadata; every record read below is pinned to {PIN}]")
    w(f"- Pin: {PIN} = {pin_full}")
    w(f"- Block: `{BLOCK}`@{PIN} sha256 `{block_sha_pin}` "
      f"({'MATCH' if block_sha_pin == BLOCK_SHA else 'MISMATCH'} vs routed 8cd8a9ac...3841; "
      f"working tree {'equal' if block_sha_wt == block_sha_pin else 'DIFFERS'}); "
      f"{len(blines) - (1 if blines[-1] == '' else 0)} lines; item N7 = block lines {n7}-{n7 + 1}")
    w(f"- Script: `{script_rel}` sha256 `{script_sha}`")
    w(f"- Interpreter: {sys.executable} (Python {platform.python_version()}, numpy {np.__version__}); "
      f"no scipy/sklearn; exact tests stdlib (math.comb); no model")
    w(f"- Command: `{cmd}`  [run metadata; working directory at run: "
      f"{'the repository root' if os.path.realpath(run_cwd) == os.path.realpath(REPO) else run_cwd}]")
    w("")
    w("Status vocabulary: reproduced (this script computes and prints it from committed "
      "JSON/npz) | log-only (prose only; pinned locator) | not found | discrepant | "
      "computed-new (a computation the block asks for that the record does not hold). "
      f"Locators are `path@{PIN}:line` as in `git show {PIN}:<path>`; the preprint is untracked "
      f"and is cited from the working tree at sha256 `{PREPRINT_SHA[:8]}...{PREPRINT_SHA[-5:]}`"
      f" (verified; tracked: {'yes' if tracked_pre else 'NO'})."
      f" Round 10: that is the preprint of record, {PREPRINT_ROUTING} (patch v7); round 9's, "
      f"patch v6 `{PREPRINT_SHA_V6[:8]}...{PREPRINT_SHA_V6[-5:]}` ({PREPRINT_RULING}), is "
      f"archived untracked at `{PREPRINT_ARCHIVED_V6}` (out of the release; not required); the "
      f"block's `{PREPRINT_SHA_AUDITED[:8]}...{PREPRINT_SHA_AUDITED[-5:]}` is the audited, "
      f"superseded text, archived untracked at `{PREPRINT_ARCHIVED}` (out of the release; not "
      "read); see 'Preprint of record (round 9)' and its subsection 'Round 10 (patch v7)' at "
      "the end of this raw.")
    w("")
    J["header"] = {"stamp": stamp, "head": head, "pin": pin_full,
                   "block_sha256": block_sha_pin,
                   "block_match": block_sha_pin == BLOCK_SHA,
                   "block_lines_n7": [n7, n7 + 1], "script": script_rel,
                   "script_sha256": script_sha, "interpreter": sys.executable,
                   "python": platform.python_version(), "numpy": np.__version__,
                   "command": cmd, "cwd_at_run": run_cwd, "preprint_sha256": pre_sha,
                   "preprint_tracked": bool(tracked_pre),
                   "preprint_ruling": PREPRINT_ROUTING,
                   "preprint_sha256_audited_superseded": PREPRINT_SHA_AUDITED,
                   "preprint_audited_archived_untracked": PREPRINT_ARCHIVED}

    # ------------------------------------------------------- referents --
    w("## 0. Referents and integrity")
    w("")
    w("Working-tree blobs imported (record helpers) or named as code referents, against the pin:")
    w("")
    integ = {}
    for p in sorted(set(IMPORTED) | set(READ_ONLY_CODE)):
        ok = blob_equal_to_pin(p)
        integ[p] = ok
        w(f"- `{p}`: {'EQUAL to pin' if ok else 'DIFFERS from pin'}"
          f"{' (imported)' if p in IMPORTED else ' (read, not run)'}")
    if not all(integ[p] for p in IMPORTED):
        raise SystemExit("an imported record helper differs from the pin -- STOP")
    w("")
    arts = ([f"data/olmo/a4_instrument_{s}.json" for s in STAGES]
            + [f"data/olmo/a4_instrument_{s}.npz" for s in STAGES]
            + [f"data/olmo/a4_hijack_{s}.json" for s in STAGES]
            + [f"data/olmo/a3_axes_{s}.json" for s in STAGES]
            + ["data/olmo/b1_verdict.json", "data/olmo/lockg_arith.json",
               "data/olmo/a5_budget.json"]
            + [f"data/olmo/b3_screen_{s}.json" for s in STAGES]
            + [f"data/olmo/b3_analysis_{s}.json" for s in STAGES]
            + [f"data/olmo/b2r_qualify_{s}.json" for s in STAGES]
            + ["data/olmo/b2r_analysis.json", "data/e0/e0_b1_markers.npz"])
    w("Committed artifacts read at the pin (sha256 of the pinned blob, first 16):")
    w("")
    J["artifacts"] = {}
    for p in arts:
        h = sha256(pinned(p))
        J["artifacts"][p] = h
        w(f"- `{p}` `{h[:16]}`")
    w("")
    w("Documents read at the pin: `RESULTS.md`, `LOCK-g.md`, `PROPOSAL-g-ontogeny-of-evaluation.md`, "
      "`ADDENDUM-g3-b2r-v1.2.md`; preprint from the working tree as above.")
    w("")
    tree = git("ls-tree", "-r", "--name-only", PIN, "data/olmo/").decode().split("\n")
    confirm_files = [t for t in tree if "b3_confirm" in t]
    J["confirm_artifacts_at_pin"] = confirm_files

    sys.path.insert(0, REPO)
    sys.path.insert(0, os.path.join(REPO, "scripts"))
    box_inst = importlib.import_module("box_a4_instrument")
    b3a = importlib.import_module("b3_analyze")
    vstats = importlib.import_module("valence_core.stats")
    from box_e0_corpus import FIT_IDS, VAL_IDS

    # ============================================== 1. G_c (A4 part 1) ==
    w("## 1. Q1 currency G_c (A4 part 1)")
    w("")
    w("**Definition, as the producing script computes it** (`scripts/box_a4_instrument.py`@"
      f"{PIN}:125-184, 241-242): 4,608 unsteered contexts per stage = 48 tasks x "
      "{self_pos, self_neg} reviewer frame x 4 paraphrases x 12 held-out probes, DV = the "
      "next-token distribution at `Response:` (top-4,096 log-probs stored per context, floor = min "
      "kept - 2.0). Per probe, on the FIT half (tasks e01-e24; 96 contexts per pole), each "
      "pole's per-token value is the sum of the token's stored log-probs over the contexts "
      "whose top-4,096 holds it, divided by ALL n contexts of the pole: a context where the "
      "token is absent contributes 0 (log-prob 0). The pole's mean floor is imputed only when "
      "the token is absent from EVERY context of that pole "
      f"(`scripts/box_a4_instrument.py`@{PIN}:142-153). The 256 token ids with the largest "
      "|post-praise value - post-criticism value| are selected and the difference vector, "
      "normalised, is the weight vector. On the VAL half (e25-e48; 96 contexts per pole per "
      "probe) each context is scored with its own floor imputed for every selected id outside "
      f"its top-4,096 (:159-168), sigma is the pooled SD of the two poles, and "
      "g_q = (mean_pos - mean_neg)/sigma. **G_c = the mean of g_q over the 12 probes.** It is a "
      "standardized gap in a next-token log-prob readout at `Response:`, in pooled-SD units; it "
      "is not a projection on the residual direction. What that readout holds on OLMo is "
      "computed in section 1b (computed-new; post-hoc).")
    w("")
    gc_rows, gc = [], {}
    tie_rows = []
    anat_rows: dict[str, dict] = {}
    t0 = time.time()
    for s in STAGES:
        meta = pinned_json(f"data/olmo/a4_instrument_{s}.json")
        z = np.load(io.BytesIO(pinned(f"data/olmo/a4_instrument_{s}.npz")))
        assert list(meta["fit_ids"]) == list(FIT_IDS)
        assert list(meta["val_ids"]) == list(VAL_IDS)
        stored = float(meta["G_c"])
        mean_gq = float(np.mean([meta["per_probe"][str(q)]["g_q"]
                                 for q in range(meta["n_probes"])]))
        store = {k: z[k] for k in ("top_ids", "top_vals", "task_id", "cond", "probe")}
        insts, pp = box_inst.build_instruments(store, list(FIT_IDS),
                                               meta["sel_per_probe"])
        sel_differ = sum(0 if np.array_equal(z[f"sel_{i}"], insts[i]["sel_ids"]) else 1
                         for i in range(len(insts)))
        w_maxdiff = max(float(np.max(np.abs(z[f"w_{i}"] - insts[i]["w"])))
                        for i in range(len(insts)))
        sig_maxdiff = max(abs(float(z["sigma"][i]) - insts[i]["sigma"])
                          for i in range(len(insts)))
        gq_maxdiff = max(abs(pp[q]["g_q"] - meta["per_probe"][str(q)]["g_q"])
                         for q in pp)
        rebuilt = float(np.mean([v["g_q"] for v in pp.values()]))
        nval = sorted({(v["n_val_pos"], v["n_val_neg"]) for v in pp.values()})
        # --- independent tie-agnostic numpy rebuild (computed-new) -------
        top_ids, top_vals = store["top_ids"], store["top_vals"]
        tid, cond, qidx = store["task_id"], store["cond"], store["probe"]
        in_fit = np.isin(tid, list(FIT_IDS))
        is_pos = cond == "self_pos"
        floor = top_vals.min(axis=1) - 2.0
        V = int(top_ids.max()) + 1
        g_ind, set_differ, exact_ties_at_cut = [], 0, 0
        for q in range(int(qidx.max()) + 1):
            qm = qidx == q
            A, C, N, FL = {}, {}, {}, {}
            for lab, mask in (("p", qm & in_fit & is_pos), ("n", qm & in_fit & ~is_pos)):
                rows = np.where(mask)[0]
                a = np.zeros(V)
                c = np.zeros(V, dtype=np.int64)
                np.add.at(a, top_ids[rows].ravel().astype(np.int64),
                          top_vals[rows].ravel().astype(np.float64))
                np.add.at(c, top_ids[rows].ravel().astype(np.int64), 1)
                A[lab], C[lab], N[lab], FL[lab] = a, c, len(rows), float(floor[mask].mean())
            keys = np.where((C["p"] > 0) | (C["n"] > 0))[0]
            dpos = np.where(C["p"][keys] > 0, A["p"][keys], FL["p"] * N["p"]) / N["p"]
            dneg = np.where(C["n"][keys] > 0, A["n"][keys], FL["n"] * N["n"]) / N["n"]
            diffs = dpos - dneg
            order = np.argsort(-np.abs(diffs), kind="stable")
            absd = np.abs(diffs[order])
            if absd[255] == absd[256]:
                exact_ties_at_cut += 1
            order = order[:256]
            sel = keys[order]
            wv = diffs[order] / (np.linalg.norm(diffs[order]) + 1e-12)
            if set(sel.tolist()) != set(z[f"sel_{q}"].tolist()):
                set_differ += 1
            pos_of = np.full(V, -1, dtype=np.int64)
            pos_of[sel] = np.arange(len(sel))

            def score(mask):
                out = []
                for i in np.where(mask)[0]:
                    x = np.full(len(sel), floor[i], dtype=np.float64)
                    t = pos_of[top_ids[i]]
                    m = t >= 0
                    x[t[m]] = top_vals[i][m].astype(np.float64)
                    out.append(float(wv @ x))
                return np.array(out)
            sp, sn = score(qm & ~in_fit & is_pos), score(qm & ~in_fit & ~is_pos)
            sd = float(np.sqrt((sp.var(ddof=1) + sn.var(ddof=1)) / 2))
            g_ind.append(float((sp.mean() - sn.mean()) / (sd + 1e-12)))
        G_ind = float(np.mean(g_ind))
        # --- instrument anatomy from the STORED sel/w (computed-new; post-hoc) --
        anat_rows[s] = instrument_anatomy(
            np, top_ids, top_vals, qidx, in_fit, is_pos,
            [z[f"sel_{i}"] for i in range(meta["n_probes"])],
            [z[f"w_{i}"] for i in range(meta["n_probes"])],
            stored_gq=[meta["per_probe"][str(i)]["g_q"] for i in range(meta["n_probes"])])
        tie_rows.append({"stage": s, "G_c_tie_agnostic": G_ind,
                         "abs_diff_vs_stored": abs(G_ind - stored),
                         "probes_with_exact_tie_at_256_cut": exact_ties_at_cut,
                         "probes_whose_top256_set_differs": set_differ})
        floors = meta["declared_floors"]
        gc[s] = stored
        gc_rows.append({"stage": s, "G_c_stored": stored, "mean_gq_stored": mean_gq,
                        "G_c_rebuilt_record_path": rebuilt,
                        "abs_diff_rebuilt": abs(rebuilt - stored),
                        "abs_diff_mean_gq": abs(mean_gq - stored),
                        "probes_sel_differ": sel_differ, "w_maxdiff": w_maxdiff,
                        "sigma_maxdiff": sig_maxdiff, "gq_maxdiff": gq_maxdiff,
                        "n_contexts": meta["n_contexts"], "n_probes": meta["n_probes"],
                        "n_val_per_pole": nval, "floors_met": floors["all_floors_met"],
                        "n_decidable_probes": floors["n_decidable_probes"],
                        "half_G_c": meta["half_G_c"],
                        "mean_val_auc": float(np.mean([meta["per_probe"][str(q)]["val_auc"]
                                                       for q in range(meta["n_probes"])])),
                        "val_auc_range": [float(min(meta["per_probe"][str(q)]["val_auc"]
                                                    for q in range(meta["n_probes"]))),
                                          float(max(meta["per_probe"][str(q)]["val_auc"]
                                                    for q in range(meta["n_probes"])))],
                        "val_auc_rebuilt_maxdiff": max(
                            abs(pp[q]["val_auc"] - meta["per_probe"][str(q)]["val_auc"])
                            for q in pp)})
    t_gc = time.time() - t0
    w("| stage | G_c stored (`a4_instrument_<s>.json:G_c`) | mean of stored per-probe g_q | "
      "G_c rebuilt from the npz store (record's build_instruments) | max abs diff | probes whose "
      "rebuilt sel differs from stored | contexts | val n per pole per probe | floors met "
      "(decidable probes) | mean val AUC [per-probe min, max] | rounded |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for r in gc_rows:
        w(f"| {r['stage']} | {r['G_c_stored']:+.6f} | {r['mean_gq_stored']:+.6f} | "
          f"{r['G_c_rebuilt_record_path']:+.6f} | "
          f"{max(r['abs_diff_rebuilt'], r['abs_diff_mean_gq']):.1e} | {r['probes_sel_differ']}/12 "
          f"(w maxdiff {r['w_maxdiff']:.1e}; sigma {r['sigma_maxdiff']:.1e}; g_q {r['gq_maxdiff']:.1e}) | "
          f"{r['n_contexts']} | {r['n_val_per_pole']} | {r['floors_met']} "
          f"({r['n_decidable_probes']}/12) | {r['mean_val_auc']:.3f} [{r['val_auc_range'][0]:.3f}, "
          f"{r['val_auc_range'][1]:.3f}] | {r['G_c_stored']:+.2f} |")
    w("")
    w("**The 'mean val AUC' column, defined (rule 4).** Per probe, the Mann-Whitney AUC (ties "
      f"score 0.5; `valence_core/discrim.py`@{PIN}:47) of the instrument score -- the weight "
      "vector fit on the FIT half (tasks e01-e24) dotted with the context's floored log-probs on "
      "that probe's 256 selected token ids -- with positives = the self_pos (post-praise) "
      "contexts and negatives = the self_neg (post-criticism) contexts of the VAL half (tasks "
      "e25-e48; 96 per pole per probe), as `build_instruments` computes it "
      f"(`scripts/box_a4_instrument.py`@{PIN}:177-178); then the mean over the 12 probes. There "
      "is no layer (it is a next-token log-prob readout at `Response:`, not a residual-stream "
      "probe) and no cross-validation: one fixed fit/val split by task, the val half held out. "
      "The rebuild reproduces every stored per-probe val_auc (max abs diff "
      f"{max(r['val_auc_rebuilt_maxdiff'] for r in gc_rows):.1e}). Descriptive; decides nothing.")
    w("")
    mono = all(gc[a] < gc[b] for a, b in zip(STAGES, STAGES[1:]))
    w(f"G_c is strictly increasing base -> sft -> dpo -> instruct: **{mono}**. Rebuild time "
      f"{t_gc:.0f} s.  ")
    w("Robustness line (computed-new; post-hoc; decides nothing): an independent numpy rebuild "
      "that breaks exact |difference| ties by ascending token id (the record's path breaks them "
      "by Python set-iteration order) gives:")
    w("")
    w("| stage | G_c tie-agnostic | abs diff vs stored | probes with an exact |diff| tie at the 256 cut | probes whose top-256 set differs |")
    w("|---|---|---|---|---|")
    for r in tie_rows:
        w(f"| {r['stage']} | {r['G_c_tie_agnostic']:+.6f} | {r['abs_diff_vs_stored']:.1e} | "
          f"{r['probes_with_exact_tie_at_256_cut']}/12 | {r['probes_whose_top256_set_differs']}/12 |")
    w("")
    w("Reading: the stored G_c values are exactly what the record's own path rebuilds from the "
      "committed stores; the tie-break is an implementation detail that moves G_c in the fifth "
      "decimal at most, so the two-decimal figures do not depend on it.")
    w("")
    # ------------------------------------------- 1b. instrument anatomy --
    t1 = time.time()
    zq = np.load(io.BytesIO(pinned("data/e0/e0_b1_markers.npz")))
    assert list(FIT_IDS) == sorted({f"e{i:02d}" for i in range(1, 25)})
    store_q = {k: zq[k] for k in ("top_ids", "top_vals", "task_id", "cond", "probe")}
    insts_q, pp_q = box_inst.build_instruments(store_q, list(FIT_IDS), 256)
    G_qwen = float(np.mean([pp_q[k]["g_q"] for k in sorted(pp_q)]))
    anat_q = instrument_anatomy(
        np, zq["top_ids"], zq["top_vals"], zq["probe"], np.isin(zq["task_id"], list(FIT_IDS)),
        zq["cond"] == "self_pos", [i["sel_ids"] for i in insts_q], [i["w"] for i in insts_q],
        stored_gq=[pp_q[k]["g_q"] for k in sorted(pp_q)])
    t_anat = time.time() - t1
    l_floorimp = loc("RESULTS.md", "floor-imputed over top-4,096 sparse storage")
    l_qwen_g = loc("RESULTS.md", "G = 0.3156 made that bar 0.158")
    l_oracle = loc("valence_core/regression/oracle.py",
                   "diffs = {k: ap.get(k, flp * n_p) / n_p - an.get(k, fln * n_n) / n_n")
    l_inst = loc("scripts/box_a4_instrument.py",
                 "diffs = {k: ap.get(k, flp * n_p) / n_p - an.get(k, fln * n_n) / n_n")
    g_floor_only = {s: anat_rows[s]["G_floor_only"] for s in STAGES}
    g_true = {s: anat_rows[s]["G_true_floor_rebuild"] for s in STAGES}
    true_mono = all(g_true[a] < g_true[b] for a, b in zip(STAGES, STAGES[1:]))
    all_one_pole = all(anat_rows[s]["sel_absent_all_pos_present_neg"] == anat_rows[s]["n_selected"]
                       for s in STAGES)
    w("### 1b. What the instrument holds on OLMo (computed-new; post-hoc; decides nothing)")
    w("")
    w("Computed by this script from the committed top-4,096 stores and the STORED per-probe "
      "selections and weights (`a4_instrument_<s>.npz:sel_<q>, w_<q>`); every per-probe g_q "
      "recomputed from them equals the stored g_q (asserted, abs diff < 1e-9). Model-free. No "
      "number, status or STOP elsewhere in this raw changes because of it.")
    w("")
    w("| stage | selected ids absent from every post-praise fit context and held by >= 1 "
      "post-criticism one (of 3,072) | post-criticism fit contexts (of 96) holding a selected id: "
      "{contexts: ids} | probes with all 256 weights < 0 | CV of \\|w\\| per probe [min, max] | "
      "probes whose post-praise mean floor is lower (fit; val) | mean fit floor post-praise / "
      "post-criticism | val cells floor-imputed: mean [min, max] | r(score, floor): mean "
      "[weakest \\|r\\|] | floor-only gap | G_c | true per-row floor-imputed rebuild G (probes "
      "whose selection changes) |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for s in STAGES:
        a_ = anat_rows[s]
        w(f"| {s} | {a_['sel_absent_all_pos_present_neg']}/{a_['n_selected']} | "
          f"{a_['neg_fit_contexts_holding_selected_id']} | {a_['probes_w_all_negative']}/12 | "
          f"[{a_['cv_abs_w_range'][0]:.5f}, {a_['cv_abs_w_range'][1]:.5f}] | "
          f"{a_['probes_fit_floor_lower_post_praise']}/12; {a_['probes_val_floor_lower_post_praise']}/12 | "
          f"{a_['mean_fit_floor_pos']:.3f} / {a_['mean_fit_floor_neg']:.3f} | "
          f"{a_['val_share_floor_imputed_mean']:.4f} [{a_['val_share_floor_imputed_range'][0]:.4f}, "
          f"{a_['val_share_floor_imputed_range'][1]:.4f}] | {a_['r_score_floor_mean']:+.4f} "
          f"[{a_['abs_r_score_floor_weakest']:.4f}] | {a_['G_floor_only']:+.4f} | {gc[s]:+.4f} | "
          f"{a_['G_true_floor_rebuild']:+.3f} ({a_['true_floor_selection_differs_probes']}/12) |")
    w("")
    w("Domains (rule 4): a 'fit context' is one of the 96 fit-half contexts of a pole for that "
      "probe (24 tasks x 4 paraphrases); a context 'holds' an id when the id is in its stored "
      "top-4,096. Floor = the context's smallest stored log-prob - 2.0, the record's "
      "definition. 'Val cells' = 256 selected ids x 192 val-half contexts per probe (96 per "
      "pole); a cell is floor-imputed when the id is outside that context's top-4,096. "
      "r = Pearson correlation, per probe over its 192 val-half contexts (both poles), between "
      "the instrument score and the context's floor; mean over the 12 probes, and the smallest "
      "|r|. Floor-only gap = per probe, (mean_pos - mean_neg)/pooled SD of the val-half context "
      "floor multiplied by the sign of the probe's mean weight (negative at every OLMo probe), "
      "then the mean over probes. True per-row floor-imputed rebuild = the fit-half per-pole "
      "means recomputed with each context that lacks an id contributing that context's own "
      "floor (instead of 0), top-256 by |difference| with ties by ascending id, the same val-half "
      "scoring and g_q; mean over probes. CV = SD/mean of |w| within a probe.")
    w("")
    praise_lower_all = all(anat_rows[s]["probes_fit_floor_lower_post_praise"] == 12 for s in STAGES)
    w_neg_all = all(anat_rows[s]["probes_w_all_negative"] == 12 for s in STAGES)
    multi = {s: {k: v for k, v in anat_rows[s]["neg_fit_contexts_holding_selected_id"].items()
                 if k != 1} for s in STAGES}
    multi_txt = "; ".join(f"{s}: " + ", ".join(f"{v} ids held by {k}" for k, v in m.items())
                          for s, m in multi.items() if m)
    pole_floors = [anat_rows[s][k] for s in STAGES for k in ("mean_fit_floor_pos", "mean_fit_floor_neg")]
    shares = [anat_rows[s]["val_share_floor_imputed_mean"] for s in STAGES]
    cut_ok = all(anat_rows[s]["probes_cut_above_every_shared"] == 12 for s in STAGES)
    w("Reading. Because a context lacking a token contributes 0 to its pole's fit mean while a "
      "token missing from a whole pole receives that pole's mean floor (pole mean floors "
      f"{min(pole_floors):.1f} to {max(pole_floors):.1f} here), a token absent from one pole and "
      "rare in the other has |difference| near that floor's magnitude. Within each probe the "
      "256th-ranked |difference| exceeds that of every token both poles hold "
      + ("at 12/12 probes per stage" if cut_ok else "NOT at every probe (CHECK)")
      + " (smallest per-probe margin per stage "
      + ", ".join(f"{s} {anat_rows[s]['min_margin_cut_minus_shared']:.2f}" for s in STAGES)
      + " log-prob units). On OLMo the pole with the lower mean floor fills all 256 slots, and "
      "that pole is post-praise "
      + ("at every probe and stage" if praise_lower_all else "NOT at every probe and stage (CHECK)")
      + ": " + ("all " if all_one_pole else "NOT all (CHECK) ")
      + "3,072 selected ids per stage are absent from the top-4,096 of every post-praise fit "
      "context and held by 1 post-criticism fit context"
      + (f" (except {multi_txt})" if multi_txt else "") + ". "
      + ("Every weight is negative and near-uniform" if w_neg_all
         else "NOT every weight is negative (CHECK)")
      + f", {min(shares):.1%}-{max(shares):.1%} of val cells (stage means) are imputed floor, "
      "and the score tracks the context's floor at |r| >= "
      f"{min(anat_rows[s]['abs_r_score_floor_weakest'] for s in STAGES):.4f} at every probe. A "
      "floor-only gap gives " + " / ".join(f"{g_floor_only[s]:.4f}" for s in STAGES)
      + " against G_c " + " / ".join(f"{gc[s]:.4f}" for s in STAGES) + ". On OLMo, G_c "
      "therefore measures, almost entirely, the post-praise vs post-criticism difference in "
      "the tail level of the next-token distribution at `Response:` (the 4,096th-largest "
      "log-prob, which sits lower after praise); it is not a gap in the probability of "
      "particular marker tokens. RESULTS.md's description of the selection as 'floor-imputed' "
      f"({l_floorimp}) holds only for the all-absent case. A true per-row floor-imputed rebuild "
      "changes the selection at "
      + ", ".join(f"{anat_rows[s]['true_floor_selection_differs_probes']}/12" for s in STAGES)
      + " probes and gives G " + " / ".join(f"{g_true[s]:.3f}" for s in STAGES)
      + "; the stage ordering "
      + ("survives (strictly increasing)." if true_mono else "does NOT survive.")
      + " The interpretation is the design seat's (PI note 7).")
    w("")
    w("Cross-reference for N8 (computed-new; post-hoc; outside N7's own scope). The Qwen B1 "
      f"instrument has the same construction ({l_oracle}; {l_inst}). The record's A4 path "
      "(`build_instruments`, blob equal to the pin) applied to the pinned Qwen store "
      f"`data/e0/e0_b1_markers.npz` returns G = {G_qwen:.4f} (published 0.3156, {l_qwen_g}; "
      f"oracle G_EXPECTED 0.3156). Its selections, too, hold only one-pole-absent ids: "
      f"{anat_q['sel_absent_all_pos_present_neg']} absent from every post-praise fit context, "
      f"{anat_q['sel_absent_all_neg_present_pos']} absent from every post-criticism one, "
      f"{anat_q['sel_present_both']} held by both. The floor explains less there: floor-only "
      f"gap {anat_q['G_floor_only']:.4f}, mean |r(score, floor)| "
      f"{anat_q['abs_r_score_floor_mean']:.4f}, weakest |r| {anat_q['abs_r_score_floor_weakest']:.4f}; "
      f"probes with all weights negative {anat_q['probes_w_all_negative']}/12; val cells "
      f"floor-imputed {anat_q['val_share_floor_imputed_mean']:.4f}. Same domains as above. "
      f"Anatomy time {t_anat:.0f} s.")
    w("")
    J["G_c"] = {"rows": gc_rows, "monotone_increasing": mono,
                "tie_agnostic_rebuild_computed_new": tie_rows,
                "instrument_anatomy_computed_new": {
                    s: {k: v for k, v in anat_rows[s].items() if k != "per_probe"} for s in STAGES},
                "instrument_anatomy_per_probe_computed_new": {
                    s: anat_rows[s]["per_probe"] for s in STAGES},
                "true_floor_rebuild_monotone": true_mono,
                "qwen_cross_reference_for_N8_computed_new": {
                    "artifact": "data/e0/e0_b1_markers.npz", "G_record_path": G_qwen,
                    "anatomy": {k: v for k, v in anat_q.items() if k != "per_probe"}}}
    l_lock_gc = loc("LOCK-g.md", "G_c per stage = +0.7824 / +1.0279 /")
    l_a4ran = loc("RESULTS.md", "A4 RAN ON ALL FOUR STAGES. The currency G_c rises")
    l_pre101 = loc(PREPRINT, "rises across the lineage (+0.78 base", working_tree=True)
    l_pre129 = loc(PREPRINT, "(G_c: +0.78 → +1.03 → +1.53 → +1.56)", working_tree=True)
    for r, lab in zip(gc_rows, ("+0.78", "+1.03", "+1.53", "+1.56")):
        ok = (f"{r['G_c_stored']:+.2f}" == lab and r["abs_diff_rebuilt"] < 1e-9
              and r["abs_diff_mean_gq"] < 1e-9)
        CHECKS[f"G_c_{r['stage']}"] = ok
        fig(f"G_c {r['stage']} {lab}",
            f"{r['G_c_stored']:+.6f} (rebuilt {r['G_c_rebuilt_record_path']:+.6f})",
            f"data/olmo/a4_instrument_{r['stage']}.json:G_c; .npz rebuild",
            "reproduced" if ok else "discrepant",
            f"also {l_lock_gc}; {l_a4ran}; {l_pre101}; {l_pre129}")

    # ======================================= 2. A4 hijack and the ladder ==
    w("## 2. Q1 causal qualification (A4 part 2), the dose ladder, and B1")
    w("")
    w("**Statistic, as the producing script computes it** (`scripts/box_a4_hijack.py`@"
      f"{PIN}:119-128, 339-347): D = mean over the 12 probes of (mean instrument score in the arm "
      "- mean in the no-injection baseline)/sigma_probe, over the hijack contexts (no Reviewer "
      "turn; the injection stands in for it). Controls at every frac: 3 norm-matched random "
      "directions x 2 signs + a sham arm (a second no-injection pass); envelope = max |D| over "
      "those 7. Potency = D+ > envelope AND D- < -envelope AND (D+ > 0 and D- < 0). Layer "
      "selection on the FIT half at frac 0.10 (largest min(D+, |D-|) among sign-correct "
      "candidates {32, 44, 52, 60}); ladder and verdict on the VAL half. MED = smallest passing "
      "frac. Dose = frac x R_l (this stage's own A3 residual norm).")
    w("")
    # what the committed A4 artifacts store (for the readout caveat)
    def _all_keys(d, acc):
        if isinstance(d, dict):
            for k_, v_ in d.items():
                acc.add(k_)
                _all_keys(v_, acc)
        elif isinstance(d, list):
            for v_ in d:
                _all_keys(v_, acc)
        return acc
    hij_keys: set = set()
    for s in STAGES:
        _all_keys(pinned_json(f"data/olmo/a4_hijack_{s}.json"), hij_keys)
    score_named = sorted(k_ for k_ in hij_keys
                         if any(t in k_.lower() for t in ("score", "baseline", "logprob", "log_prob")))
    npz_arrays = sorted({re.sub(r"_\d+$", "_<q>", k_) for s in STAGES
                         for k_ in np.load(io.BytesIO(pinned(f"data/olmo/a4_instrument_{s}.npz"))).keys()})
    sel_score_is_min = all(
        (v_["score_min_abs"] is None) if not v_["sign_correct"]
        else v_["score_min_abs"] == min(v_["delta_pos"], abs(v_["delta_neg"]))
        for s in STAGES for v_ in pinned_json(f"data/olmo/a4_hijack_{s}.json")["selection"].values())
    readout_unstored = (score_named == ["score_min_abs"] and sel_score_is_min
                        and npz_arrays == ["cond", "probe", "sel_<q>", "sigma", "task_id",
                                           "top_ids", "top_vals", "w_<q>"])
    share_lo = min(anat_rows[s]["val_share_floor_imputed_mean"] for s in STAGES)
    share_hi = max(anat_rows[s]["val_share_floor_imputed_mean"] for s in STAGES)
    l_hij_score = loc("scripts/box_a4_hijack.py", "        lp = log_probs(res.logits)", extra=2)
    READOUT_CAVEAT = (
        "D's numerator is read on full-vocabulary log-probs (`w @ log_softmax(logits)[sel_ids]`, "
        f"{l_hij_score}), while sigma_probe and G_c are read on the top-4,096 store with each "
        "context's floor imputed for every selected id outside its top-4,096 "
        f"(`scripts/box_a4_instrument.py`@{PIN}:159-176; {share_lo:.1%}-{share_hi:.1%} of cells, "
        "section 1b). D/G_c, the V1-lineage bar D+ >= 0.5 G_c, and any reading of D 'in sigma "
        "units' as comparable to G_c therefore divide readings from two versions of the "
        "instrument, and cross-stage ratios in G_c units inherit the mismatch. Its size is "
        "unmeasured: "
        + ("no committed A4 artifact stores an unsteered full-log-prob score (the hijack JSONs' "
           "only score-named key is `selection.<L>.score_min_abs` = min(D+, |D-|), a "
           "displacement; the instrument npz holds " + ", ".join(npz_arrays) + "), so measuring "
           "it needs model inference."
           if readout_unstored else "CHECK: a committed A4 artifact may store raw scores ("
           + ", ".join(score_named) + ")."))
    w("**Readout caveat (round-2 finding; post-hoc; no status changes).** " + READOUT_CAVEAT
      + " The registered potency criterion is not affected: D and every control D are "
      "full-log-prob readouts with the same per-probe 1/sigma weights, so the envelope "
      "comparison is like with like.")
    w("")
    a4, b1_recomp = {}, {}
    sel_rows, lad_rows, sham_cells, sham_zero = [], [], 0, 0
    fail_conj_pattern = set()
    v1_any = False
    for s in STAGES:
        h = pinned_json(f"data/olmo/a4_hijack_{s}.json")
        a3 = pinned_json(f"data/olmo/a3_axes_{s}.json")
        G = gc[s]
        assert abs(float(h["inputs"]["G_c"]) - G) == 0.0
        assert not h["smoke"] and not h["selftest"]
        # selection
        best, best_score = None, -math.inf
        for L, v in sorted(h["selection"].items(), key=lambda kv: int(kv[0])):
            ok = v["delta_pos"] > 0 and v["delta_neg"] < 0
            sc = min(v["delta_pos"], abs(v["delta_neg"])) if ok else -math.inf
            assert ok == v["sign_correct"]
            if sc > best_score:
                best, best_score = int(L), sc
            sel_rows.append({"stage": s, "layer": int(L), "D+": v["delta_pos"],
                             "D-": v["delta_neg"], "sign_correct": ok,
                             "score": sc if ok else None, "R_l": v["R_layer"],
                             "alpha": v["alpha"]})
        assert best == h["selected_layer"]
        # ladder
        passing = []
        n_ctx = h["procedure"]["forwards_planned"] / (
            (2 * len(h["procedure"]["candidate_layers"]) + 1)
            + (1 + len(h["procedure"]["dose_ladder"]) * (2 + 2 * h["procedure"]["n_random"] + 1)))
        for fr in FRACS:
            v = h["ladder"][fr]
            dpos = float(np.mean(v["per_probe_pos"]))
            dneg = float(np.mean(v["per_probe_neg"]))
            ctl = v["controls"]
            assert len(ctl) == 7
            env = max(abs(c["delta"]) for c in ctl.values())
            env_src = max(ctl, key=lambda k: abs(ctl[k]["delta"]))
            conj = {"pos_exceeds_envelope": dpos > env,
                    "neg_exceeds_envelope_opposite": dneg < -env,
                    "sign_locks": dpos > 0 and dneg < 0}
            pot = all(conj.values())
            v1 = (dpos >= 0.5 * G and dneg <= -0.5 * G
                  and min(dpos, abs(dneg)) > 2 * max(abs(c["delta"]) for k, c in ctl.items()
                                                       if k != "sham"))
            v1_any |= v1
            assert conj == v["potency_conjuncts"] and pot == v["potency"]
            assert dpos == v["delta_pos"] and dneg == v["delta_neg"], (s, fr)
            assert env == v["control_envelope"] and v1 == v["v1_lineage"]
            sham_cells += 1
            sham_zero += int(ctl["sham"]["delta"] == 0.0)
            if not pot:
                fail_conj_pattern.add(tuple(k for k, b in conj.items() if not b))
            if pot:
                passing.append(float(fr))
            lad_rows.append({"stage": s, "layer": h["selected_layer"], "frac": float(fr),
                             "alpha": v["alpha"], "R_l": v["R_layer"], "D+": dpos, "D-": dneg,
                             "envelope": env, "envelope_set_by": env_src,
                             "sham": ctl["sham"]["delta"], "conjuncts": conj,
                             "potency": pot, "D+/G_c": dpos / G, "D-/G_c": dneg / G,
                             "v1_lineage": v1,
                             "rand_max": max(abs(c["delta"]) for k, c in ctl.items() if k != "sham")})
            # stored descriptive fields the ratio and V1 lines rely on
            assert lad_rows[-1]["rand_max"] == v["max_abs_delta_random"], (s, fr)
            assert abs(lad_rows[-1]["D+/G_c"] - v["delta_pos_in_Gc"]) < 1e-15, (s, fr)
            assert abs(lad_rows[-1]["D-/G_c"] - v["delta_neg_in_Gc"]) < 1e-15, (s, fr)
            lad_rows[-1]["v1_conjuncts_stored"] = v["v1_lineage_conjuncts"]
        med = min(passing) if passing else None
        assert med == h["minimum_effective_dose"]
        g3 = next(r for r in a3["report"]["span"] if r["layer"] == h["selected_layer"])
        b1_recomp[s] = {"selected_layer": h["selected_layer"], "passing_fracs": passing,
                        "minimum_effective_dose": med,
                        "verdict": "PASS" if passing else "FAIL",
                        "conjuncts_at_med": (h["ladder"][str(med)]["potency_conjuncts"]
                                             if passing else None),
                        "G_c": G,
                        "v1_lineage_any_frac": any(r["v1_lineage"] for r in lad_rows
                                                   if r["stage"] == s),
                        "guard_profile_at_selected_layer": {
                            "cos_char": g3["cos_span_character"],
                            "v2_self_residual_frac": g3["v2_self_residual_frac"],
                            "v3_eval_residual_frac": g3["v3_eval_residual_frac"]}}
        a4[s] = {"selected_layer": h["selected_layer"], "med": med, "passing": passing,
                 "n_val_contexts_derived": n_ctx, "random_seed_note": "box_a4_hijack.py RANDOM_SEED 20260822"}
    w("### 2a. Layer selection (fit half, frac 0.10; from `a4_hijack_<s>.json:selection`)")
    w("")
    w("| stage | L32 min(D+,\\|D-\\|) | L44 | L52 | L60 | selected (recomputed = stored) |")
    w("|---|---|---|---|---|---|")
    n_sign_correct = {}
    for s in STAGES:
        rr = {r["layer"]: r for r in sel_rows if r["stage"] == s}
        n_sign_correct[s] = sum(1 for L in rr if rr[L]["sign_correct"])
        cells = [(f"not sign-correct (D+ {f4(rr[L]['D+'])}, D- {f4(rr[L]['D-'])})"
                  if rr[L]["score"] is None else f"{rr[L]['score']:.4f}") for L in (32, 44, 52, 60)]
        w(f"| {s} | " + " | ".join(cells) + f" | L{a4[s]['selected_layer']} |")
    w("")
    w("A cell reads 'not sign-correct' where the stored fit-half D+ <= 0 or D- >= 0 "
      "(`selection.<L>.sign_correct` = False); such a layer is not a candidate. Sign-correct "
      "candidates per stage: " + ", ".join(f"{s} {n_sign_correct[s]}/4" for s in STAGES)
      + ". " + " ".join(
          f"At {s} only L{a4[s]['selected_layer']} is sign-correct (the others fail on "
          + ("D+ <= 0" if all(r["D+"] <= 0 for r in sel_rows if r["stage"] == s and not r["sign_correct"])
             else "D+ <= 0 or D- >= 0")
          + "), so its layer 'selection' is by elimination."
          for s in STAGES if n_sign_correct[s] == 1)
      + " Descriptive; decides nothing.")
    w("")
    w(f"Hijack contexts per arm on the val half, derived from the stored plan "
      f"(`procedure.forwards_planned` = 9 n_fit + 37 n_val with n_fit = n_val): "
      f"{', '.join(f'{s} {a4[s]['n_val_contexts_derived']:.0f}' for s in STAGES)} "
      "(= 24 val tasks x 12 probes x 1 repeat; 24 contexts per probe per arm).")
    w("")
    w("### 2b. Dose ladder (val half), envelope conjunction recomputed from stored per-probe deltas and controls")
    w("")
    w("| stage | L | frac | \\|alpha\\| | D+ | D- | envelope (set by) | sham D | pos>env | neg<-env | sign lock | potency | D+/G_c | V1-lineage |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in lad_rows:
        c = r["conjuncts"]
        w(f"| {r['stage']} | L{r['layer']} | {r['frac']:.2f} | {r['alpha']:.4f} | {f4(r['D+'])} | "
          f"{f4(r['D-'])} | {r['envelope']:.4f} ({r['envelope_set_by']}) | {r['sham']:.1f} | "
          f"{c['pos_exceeds_envelope']} | {c['neg_exceeds_envelope_opposite']} | {c['sign_locks']} | "
          f"**{'PASS' if r['potency'] else 'fail'}** | {r['D+/G_c']:.3f} | {r['v1_lineage']} |")
    w("")
    w("Every recomputed conjunct, potency flag, envelope, D+ (as the mean of the 12 stored "
      "per-probe values), D- and V1-lineage flag equals the stored field, as do D+/G_c and D-/G_c "
      "(`delta_pos_in_Gc`, `delta_neg_in_Gc`), max |D_rand| (`max_abs_delta_random`) and the V1 "
      "conjunct flags (`v1_lineage_conjuncts`) (all asserted).")
    w("")
    w("### 2c. MEDs, sham, and the descriptives")
    w("")
    w("| stage | selected layer | passing fracs | MED | \\|alpha\\| at MED | R_l | verdict |")
    w("|---|---|---|---|---|---|---|")
    for s in STAGES:
        m = a4[s]["med"]
        rr = next(r for r in lad_rows if r["stage"] == s and r["frac"] == m)
        w(f"| {s} | L{a4[s]['selected_layer']} | {a4[s]['passing']} | {m:.2f} | "
          f"{rr['alpha']:.4f} | {rr['R_l']:.4f} | **{'PASS' if a4[s]['passing'] else 'FAIL'}** |")
    w("")
    w(f"- Sham (second no-injection pass) D = 0.0 exactly in **{sham_zero}/{sham_cells}** "
      "(stage x frac) cells. What it certifies: the apparatus floor (bit-for-bit determinism of a "
      "repeated unsteered pass), so the envelope is set by the random directions. It is not a "
      "praise-vs-criticism contrast, and it is not the B3 sham arm (a separate session arm with "
      "its own pseudo-Deltas; section 4a and PI note 11).")
    matched = {r["stage"]: r for r in lad_rows if r["frac"] == 0.10}
    m_pass = [s for s in STAGES if matched[s]["potency"]]
    ratios = {s: matched["base"]["D+/G_c"] / matched[s]["D+/G_c"] for s in STAGES[1:]}
    w(f"- Matched dose (frac 0.10) passes: {m_pass}. D+/G_c at 0.10: "
      + ", ".join(f"{s} {matched[s]['D+/G_c']:.4f}" for s in STAGES)
      + "; base over each later stage: "
      + ", ".join(f"{s} {ratios[s]:.2f}x" for s in STAGES[1:])
      + " (readout caveat above: the numerator and G_c are read on two versions of the "
      "instrument; the mismatch's size is unmeasured).")
    dpos_all = [r["D+"] for r in lad_rows]
    neg_fail = [(r["stage"], r["frac"]) for r in lad_rows
                if not r["conjuncts"]["neg_exceeds_envelope_opposite"]]
    lock_fail = [(r["stage"], r["frac"]) for r in lad_rows if not r["conjuncts"]["sign_locks"]]
    neg_fail_stages_pass_lower = all(
        any(r["potency"] and r["frac"] < fr for r in lad_rows if r["stage"] == st_)
        for st_, fr in neg_fail)
    w(f"- Failing conjuncts over every failing (stage, frac) cell: {sorted(fail_conj_pattern)}. "
      f"`pos_exceeds_envelope` fails in every failing cell; `neg_exceeds_envelope_opposite` "
      f"also fails at {neg_fail} (|D-| below a random-direction envelope at the top rung); "
      f"`sign_locks` fails in {len(lock_fail)} cells {lock_fail}. "
      + ("No MED and no verdict depends on a negative-pole failure: each of those stages passes "
         "at a lower frac." if neg_fail_stages_pass_lower else
         "CHECK: a stage with a negative-pole failure has no lower pass."))
    dpos_med = {s: next(r["D+"] for r in lad_rows if r["stage"] == s and r["frac"] == a4[s]["med"])
                for s in STAGES}
    dpos_pass = [r["D+"] for r in lad_rows if r["potency"]]
    min_all_cell = min(lad_rows, key=lambda r: r["D+"])
    l_v1_a4 = loc("RESULTS.md", "The V1-lineage rule fails at every stage and every frac", extra=2)
    l_v1_b1 = loc("RESULTS.md", "The V1-lineage rule passes at NO stage and NO frac", extra=3)
    w(f"- D+ by domain (the record's 'displacements 0.02-0.28' sits in sentences framed over "
      f"every stage and every frac: {l_v1_a4}; {l_v1_b1}): at each stage's MED "
      + ", ".join(f"{s} {dpos_med[s]:+.4f}" for s in STAGES)
      + f" -> range {min(dpos_med.values()):.4f} .. {max(dpos_med.values()):.4f}; over the "
      f"{len(dpos_pass)} potency-passing cells {min(dpos_pass):.4f} .. {max(dpos_pass):.4f}; over all "
      f"16 cells {min(dpos_all):.4f} .. {max(dpos_all):.4f} (the low end is {min_all_cell['stage']} "
      f"at frac {min_all_cell['frac']:.2f}, a failing cell). |D-| over all 16 cells: "
      f"{min(abs(r['D-']) for r in lad_rows):.4f} .. {max(abs(r['D-']) for r in lad_rows):.4f}.")
    # V1-lineage, conjunct by conjunct (context only; LOCK-g)
    v1_rows = []
    for r in lad_rows:
        G = gc[r["stage"]]
        rmax = r["rand_max"]
        v1_rows.append({"stage": r["stage"], "frac": r["frac"],
                        "pos_ge_half_Gc": r["D+"] >= 0.5 * G,
                        "neg_le_minus_half_Gc": r["D-"] <= -0.5 * G,
                        "min_gt_2_max_rand": min(r["D+"], abs(r["D-"])) > 2 * rmax,
                        "half_Gc": 0.5 * G, "two_max_rand": 2 * rmax})
        cs = r["v1_conjuncts_stored"]
        assert (v1_rows[-1]["pos_ge_half_Gc"], v1_rows[-1]["neg_le_minus_half_Gc"],
                v1_rows[-1]["min_gt_2_max_rand"]) == (cs["pos_ge_half_Gc"], cs["neg_le_neg_half_Gc"],
                                                      cs["min_gt_2x_max_rand"]), (r["stage"], r["frac"])
    v1_neg_only = [(x["stage"], x["frac"]) for x in v1_rows if x["neg_le_minus_half_Gc"]]
    v1_pos_any = [(x["stage"], x["frac"]) for x in v1_rows if x["pos_ge_half_Gc"]]
    w(f"- V1-lineage rule (D+ >= 0.5 G_c, D- <= -0.5 G_c, min(D+, |D-|) > 2 max|D_rand|; context "
      f"only, {loc('LOCK-g.md', 'The V1-lineage')}) passes anywhere: {v1_any}. By conjunct: "
      f"D+ >= 0.5 G_c holds in {len(v1_pos_any)}/16 cells; D- <= -0.5 G_c holds at {v1_neg_only}"
      + "".join(f" ({s} {fr:.2f}: D- {f4(next(r['D-'] for r in lad_rows if r['stage'] == s and r['frac'] == fr))} "
                f"vs -0.5 G_c {-next(x['half_Gc'] for x in v1_rows if x['stage'] == s and x['frac'] == fr):+.4f}; "
                f"min-vs-random holds: {next(x['min_gt_2_max_rand'] for x in v1_rows if x['stage'] == s and x['frac'] == fr)})"
                for s, fr in v1_neg_only)
      + "; the rule fails there on its other conjuncts. Its bar D+ >= 0.5 G_c compares a "
      "full-log-prob displacement with a floor-dominated natural gap (readout caveat above).")
    w("")
    # ratio sensitivity (computed-new, post-hoc): pole and dose
    ratio_tab = {}
    for fr in (0.05, 0.10, 0.20, 0.40):
        rows_f = {r["stage"]: r for r in lad_rows if r["frac"] == fr}
        ratio_tab[f"{fr:.2f}"] = {
            "Dpos": {s: rows_f["base"]["D+/G_c"] / rows_f[s]["D+/G_c"] for s in STAGES[1:]},
            "absDneg": {s: (abs(rows_f["base"]["D-/G_c"]) / abs(rows_f[s]["D-/G_c"])) for s in STAGES[1:]}}
    w("Ratio sensitivity (computed-new; post-hoc; descriptive): base's displacement per unit G_c "
      "divided by each later stage's, by pole and by frac (the record's statistic, "
      "RESULTS.md's 'D+/G_c at matched dose', is the D+ row at 0.10). Every ratio inherits the "
      "readout caveat above (displacements read on full-vocabulary log-probs, G_c on the "
      "floor-imputed top-4,096 store; size of the mismatch unmeasured):")
    w("")
    w("| frac | D+/G_c ratio base/sft | base/dpo | base/instruct | \\|D-\\|/G_c ratio base/sft | base/dpo | base/instruct |")
    w("|---|---|---|---|---|---|---|")
    for fr, v in ratio_tab.items():
        w(f"| {fr} | " + " | ".join(f"{v['Dpos'][s]:.2f}x" for s in STAGES[1:]) + " | "
          + " | ".join(f"{v['absDneg'][s]:.2f}x" for s in STAGES[1:]) + " |")
    w("")
    def rng(fr, key):
        vals = ratio_tab[fr][key].values()
        return f"{min(vals):.1f}-{max(vals):.1f}x"
    r40 = ratio_tab["0.40"]["Dpos"]["sft"]
    w(f"Reading: the positive-pole ratio is {rng('0.05', 'Dpos')} at frac 0.05 and "
      f"{rng('0.10', 'Dpos')} at 0.10 (the record's statistic); on the negative pole at 0.10 it is "
      f"{rng('0.10', 'absDneg')}; at 0.20 the D+ ratio is {rng('0.20', 'Dpos')}; at 0.40 it is "
      f"{rng('0.40', 'Dpos')}, with base/sft {r40:.2f}x"
      + (" (below 1: SFT's D+/G_c exceeds base's at the top rung)." if r40 < 1 else "."))
    w("")
    # B1 mapping
    b1 = pinned_json("data/olmo/b1_verdict.json")
    b1_equal = all(b1["per_stage"][s] == json.loads(json.dumps(b1_recomp[s])) for s in STAGES)
    base_pass = b1_recomp["base"]["verdict"] == "PASS"
    branch = ("base_pass" if base_pass else
              "base_fail_later_pass" if any(b1_recomp[s]["verdict"] == "PASS" for s in STAGES[1:])
              else "all_fail")
    w("### 2d. B1 -- the Q1 verdict mapping, re-applied")
    w("")
    w(f"Registered mapping ({loc('PROPOSAL-g-ontogeny-of-evaluation.md', 'bet confirmed (marking is a pretraining acquisition). Base FAIL with')}; "
      f"{loc('LOCK-g.md', 'Verdict per stage = the registered A4 potency criterion at ANY')}): "
      f"Base PASS -> bet confirmed. Recomputed branch: **{branch}**; stored "
      f"`b1_verdict.json:branch` = `{b1['branch']}`; per-stage blocks (layer, passing fracs, MED, "
      f"verdict, conjuncts at MED, G_c, V1 flag, guard profile from `a3_axes_<s>.json`) equal to "
      f"the stored ones: **{b1_equal}**.")
    w("")
    J["A4"] = {"selection": sel_rows, "ladder": lad_rows, "per_stage": a4,
               "sham_zero_cells": [sham_zero, sham_cells], "matched_dose_pass": m_pass,
               "Dpos_over_Gc_ratio_base_vs_later_at_0.10": ratios,
               "failing_conjunct_patterns": sorted(fail_conj_pattern),
               "Dpos_range": [min(dpos_all), max(dpos_all)],
               "Dpos_at_MED": dpos_med, "Dpos_range_at_MEDs": [min(dpos_med.values()), max(dpos_med.values())],
               "Dpos_range_passing_cells": [min(dpos_pass), max(dpos_pass)],
               "sign_correct_candidates": n_sign_correct,
               "v1_lineage_by_conjunct": v1_rows,
               "ratio_sensitivity_computed_new": ratio_tab,
               "v1_lineage_any": v1_any,
               "B1_branch_recomputed": branch, "B1_branch_stored": b1["branch"],
               "B1_per_stage_equal": b1_equal}
    l_b1 = loc("RESULTS.md", "B1 — Q1 VERDICT: the registered bet is CONFIRMED")
    # per-stage row locators (the B1 table and LOCK-g §1's MED table)
    l_b1tab = {s: loc("RESULTS.md", f"| {s} | L{a4[s]['selected_layer']} | "
                      f"{', '.join(f'{x:.2f}' for x in a4[s]['passing'])} | {a4[s]['med']:.2f} | **PASS** |")
               for s in STAGES}
    l_lockmed = {s: loc("LOCK-g.md", f"| {s} | L{a4[s]['selected_layer']} | {a4[s]['med']:.2f} |")
                 for s in STAGES}
    l_lock_sham = loc("LOCK-g.md", "sham realised 0.0 bit-for-bit everywhere")
    l_pre139 = loc(PREPRINT, "Per-stage minimum effective doses qualify at f = 0.05 (base, L60)",
                   working_tree=True)
    l_pre129b = loc(PREPRINT, "the base model passes at layer 60", working_tree=True)
    # Every status below is conditioned on the check that licenses it.
    status_of = lambda ok: "reproduced" if ok else "discrepant"
    CHECKS["sham_all_zero"] = sham_zero == sham_cells
    fig("sham 0.0", f"{sham_zero}/{sham_cells} cells exactly 0.0",
        "data/olmo/a4_hijack_<s>.json:ladder.<frac>.controls.sham.delta", status_of(CHECKS["sham_all_zero"]),
        f"A4 sham = repeated unsteered pass (determinism floor); {l_lock_sham}; "
        f"{loc('RESULTS.md', 'Sham is exactly 0.0 at every frac at every stage')}; "
        f"{loc(PREPRINT, 'Sham contrasts are exactly zero at every stage', working_tree=True)}")
    CHECKS["base_pass_L60"] = (a4["base"]["selected_layer"] == 60 and bool(a4["base"]["passing"])
                               and b1_equal)
    fig("base pass at L60", f"selected L{a4['base']['selected_layer']} (fit-half score "
        f"{max(r['score'] for r in sel_rows if r['stage'] == 'base' and r['score'] is not None):.4f}); "
        f"passes at {a4['base']['passing']}",
        "data/olmo/a4_hijack_base.json:selection, selected_layer, ladder; b1_verdict.json",
        status_of(CHECKS["base_pass_L60"]), f"{l_b1}; {l_pre129b}")
    for s, lab in zip(STAGES, ("0.05 L60", "0.40 L44", "0.05 L44", "0.05 L44")):
        got = f"{a4[s]['med']:.2f} L{a4[s]['selected_layer']}"
        CHECKS[f"MED_{s}"] = got == lab and b1_equal
        fig(f"MED {s} {lab}", got,
            f"data/olmo/a4_hijack_{s}.json:minimum_effective_dose, selected_layer",
            status_of(CHECKS[f"MED_{s}"]), f"{l_b1tab[s]}; {l_lockmed[s]}; {l_pre139}")
    CHECKS["ratio_record_statistic"] = (f"{matched['base']['D+/G_c']:.3f}" == "0.110"
                                        and all(0.0215 <= matched[s]["D+/G_c"] < 0.0265
                                                for s in STAGES[1:]))
    fig("ratio of steering displacement to natural contrast ~5x larger at base (preprint §5.1)",
        "D+/G_c at frac 0.10: base {:.4f} vs {:.4f}/{:.4f}/{:.4f} -> {:.2f}x/{:.2f}x/{:.2f}x".format(
            matched["base"]["D+/G_c"], matched["sft"]["D+/G_c"], matched["dpo"]["D+/G_c"],
            matched["instruct"]["D+/G_c"], ratios["sft"], ratios["dpo"], ratios["instruct"]),
        "data/olmo/a4_hijack_<s>.json:ladder.0.1.delta_pos_in_Gc", status_of(CHECKS["ratio_record_statistic"]),
        f"'about five' = {min(ratios.values()):.1f}-{max(ratios.values()):.1f}x on the record's statistic "
        f"(positive pole, matched dose 0.10); the preprint sentence names neither: |D-| at 0.10 gives "
        f"{min(ratio_tab['0.10']['absDneg'].values()):.1f}-{max(ratio_tab['0.10']['absDneg'].values()):.1f}x "
        f"and D+ at 0.40 gives {min(ratio_tab['0.40']['Dpos'].values()):.2f}-"
        f"{max(ratio_tab['0.40']['Dpos'].values()):.2f}x (section 2c, PI note 10); readout caveat "
        f"(section 2): D is read on full-vocabulary log-probs, G_c and sigma on the floor-imputed "
        f"top-4,096 store, so the ratio mixes two versions of the instrument and the mismatch's "
        f"size is unmeasured; status kept; "
        f"{loc('RESULTS.md', 'D+/G_c at matched dose is 0.110 at Base against 0.022–0.026')}; "
        f"{loc(PREPRINT, 'about five times larger at base', working_tree=True)}")
    CHECKS["Q1_all_pass_base_pass"] = (b1_equal and branch == b1["branch"] == "base_pass"
                                       and all(a4[s]["passing"] for s in STAGES))
    fig("Q1: all four stages pass the conjunction; bet confirmed (branch base_pass)",
        f"PASS x4; branch {branch}", "data/olmo/b1_verdict.json:per_stage, branch (recomputed)",
        status_of(CHECKS["Q1_all_pass_base_pass"]), l_b1)
    if not b1_equal or branch != b1["branch"]:
        STOPS.append("Q1/B1: the registered mapping re-applied to the stored A4 artifacts does not "
                     "return the stored b1_verdict.json; reproducing it would need an analyzer change")
    fig("ratio sensitivity by pole and dose (sec. 2c table)",
        "; ".join(f"{fr}: D+ {min(v['Dpos'].values()):.2f}-{max(v['Dpos'].values()):.2f}x, |D-| "
                  f"{min(v['absDneg'].values()):.2f}-{max(v['absDneg'].values()):.2f}x"
                  for fr, v in ratio_tab.items()),
        "computed here from a4_hijack_<s>.json:ladder.<frac>.delta_pos_in_Gc, delta_neg_in_Gc",
        "computed-new", "post-hoc, descriptive; base over sft/dpo/instruct; decides nothing; "
        "inherits the section-2 readout caveat (full-log-prob displacement over a G_c read on the "
        "floor-imputed store; mismatch size unmeasured)")

    # ============================================ 3. Fisher p = .0047 ==
    w("## 3. The Fisher p = .0047 allocation note")
    w("")
    q = pinned_json("data/olmo/b2r_qualify_base.json")
    b2r = pinned_json("data/olmo/b2r_analysis.json")
    ctl = q["control"]
    ctl_about = sum(1 for r in ctl["rows"] if r.get("about_any"))
    assert ctl_about == ctl["about"] and len(ctl["rows"]) == ctl["n"]
    ladder3 = []
    for st in sorted(q["injected"], key=float):
        v = q["injected"][st]
        k = sum(1 for r in v["rows"] if r["about"])
        dg = sum(1 for r in v["rows"] if r["degen"])
        assert k == v["about"] and len(v["rows"]) == v["n"]
        assert abs(dg / v["n"] - v["degenerate_frac"]) == 0.0
        lo, hi = clopper_pearson(k, v["n"])
        _, chi = clopper_pearson(ctl["about"], ctl["n"])
        st_rec = b2r["g3b"]["base"]["ladder"][st]
        p_f = fisher_upper(k, v["n"] - k, ctl["about"], ctl["n"] - ctl["about"])
        p_rec = vstats.fisher_one_sided(k, v["n"] - k, ctl["about"], ctl["n"] - ctl["about"])
        ladder3.append({"strength": float(st), "about": k, "n": v["n"], "degenerate": dg,
                        "degenerate_frac": dg / v["n"], "coherent": dg / v["n"] <= 0.25,
                        "cp_lower": lo, "cp_upper": hi, "control_cp_upper": chi,
                        "separates": lo > chi, "passes": (lo > chi) and dg / v["n"] <= 0.25,
                        "stored_ci": st_rec["ci"], "stored_separates": st_rec["separates"],
                        "stored_passes": st_rec["passes"],
                        "fisher_one_sided_p": p_f, "fisher_record_helper": p_rec,
                        "cp_lower_minus_control_upper": lo - chi})
    w(f"**Referent.** Not the A4 ladder: the figure belongs to B2-r's [g3-B] concept-family dose "
      f"qualification at Base (ADDENDUM-g3 v1.2 §2, "
      f"{loc('ADDENDUM-g3-b2r-v1.2.md', '**Potency [g3-B]:** injected about-rate CP interval separates from the')}"
      f"), artifact `data/olmo/b2r_qualify_base.json` (layer {q['layer']}, temperature {q['temp']}, "
      f"max_tokens {q['max_tokens']}, strengths in Macar et al.'s convention = multiples of the raw "
      f"concept-vector norm; 4 concepts x 2 prompts x 3 seeds = 24 injected generations per "
      f"strength, pooled). The DV is 'about-ness' (any occurrence of the injected concept's lemma "
      f"in a free generation); control = {ctl['n']} uninjected generations (2 prompts x 12 seeds) "
      f"scored 'about' if any of the four concepts' lemmas occurs (`about_any`): "
      f"{ctl['about']}/{ctl['n']}.")
    w("")
    w("| strength | about k/n (recounted from rows) | degenerate | coherent (<= 0.25) | CP 95% [lo, hi] (recomputed; stored) | control CP upper | separates (lo > ctl hi) | passes | one-sided Fisher p (injected about > control) |")
    w("|---|---|---|---|---|---|---|---|---|")
    for r in ladder3:
        w(f"| {r['strength']:.1f} | {r['about']}/{r['n']} | {r['degenerate']}/{r['n']} "
          f"({r['degenerate_frac']:.3f}) | {r['coherent']} | [{r['cp_lower']:.5f}, {r['cp_upper']:.5f}]; "
          f"[{r['stored_ci'][0]:.5f}, {r['stored_ci'][1]:.5f}] | {r['control_cp_upper']:.5f} | "
          f"{r['separates']} (stored {r['stored_separates']}) | {r['passes']} (stored "
          f"{r['stored_passes']}) | {r['fisher_one_sided_p']:.5f} |")
    w("")
    s2 = next(r for r in ladder3 if r["strength"] == 2.0)
    assert abs(s2["fisher_one_sided_p"] - s2["fisher_record_helper"]) < 1e-15
    assert all(abs(a - b) < 1e-12 for a, b in zip((s2["cp_lower"], s2["cp_upper"]), s2["stored_ci"]))
    w(f"**The test and the table.** One-sided Fisher exact test (hypergeometric upper tail, both "
      f"margins fixed) on the 2x2 table rows = (injected s = 2.0, uninjected control), columns = "
      f"(about, not about): [[{s2['about']}, {s2['n'] - s2['about']}], [{ctl['about']}, "
      f"{ctl['n'] - ctl['about']}]]; with a 0 in the control cell the p is the single extreme "
      f"table, C(24,7)/C(48,7) = {math.comb(24, 7)}/{math.comb(48, 7)} = "
      f"**p = {s2['fisher_one_sided_p']:.5f}** (the record's `valence_core.stats.fisher_one_sided` "
      f"returns {s2['fisher_record_helper']:.5f}). s = 2.0 is coherent ({s2['degenerate']}/24 "
      f"degenerate = {s2['degenerate_frac']:.3f} <= 0.25) and fails the registered criterion only "
      f"on interval separation: CP lower {s2['cp_lower']:.5f} vs control CP upper "
      f"{s2['control_cp_upper']:.5f}, a miss of {-s2['cp_lower_minus_control_upper']:.4f}. "
      f"Base therefore has no MED_c (stored `b2r_analysis.json:g3b.base.MED_c` = "
      f"{b2r['g3b']['base']['MED_c']}; hard_stop {b2r['g3b']['base']['hard_stop']}).")
    w("")
    # MED_c at every stage, recounted from the qualify rows (not echoed from the analyzer field)
    medc = {}
    for s_ in STAGES:
        qs = pinned_json(f"data/olmo/b2r_qualify_{s_}.json")
        cs = qs["control"]
        ck = sum(1 for r in cs["rows"] if r.get("about_any"))
        assert ck == cs["about"] and len(cs["rows"]) == cs["n"]
        _, c_hi = clopper_pearson(ck, len(cs["rows"]))
        rows_ = []
        for st_ in sorted(qs["injected"], key=float):
            v = qs["injected"][st_]
            k = sum(1 for r in v["rows"] if r["about"])
            n = len(v["rows"])
            dg = sum(1 for r in v["rows"] if r["degen"])
            lo, hi = clopper_pearson(k, n)
            sep, coh = lo > c_hi, dg / n <= 0.25
            rec = b2r["g3b"][s_]["ladder"][st_]
            ok = (sep == rec["separates"] and coh == rec["coherent"]
                  and (sep and coh) == rec["passes"]
                  and abs(lo - rec["ci"][0]) < 1e-12 and abs(hi - rec["ci"][1]) < 1e-12
                  and k == v["about"] and n == v["n"])
            rows_.append({"strength": float(st_), "about": k, "n": n, "degenerate": dg,
                          "cp_lower": lo, "separates": sep, "coherent": coh,
                          "passes": sep and coh, "equals_stored": ok})
        med_ = next((r["strength"] for r in rows_ if r["passes"]), None)
        medc[s_] = {"control": [ck, len(cs["rows"])], "control_cp_upper": c_hi, "ladder": rows_,
                    "MED_c_recount": med_, "MED_c_stored": b2r["g3b"][s_]["MED_c"],
                    "hard_stop_stored": b2r["g3b"][s_]["hard_stop"],
                    "equal": (med_ == b2r["g3b"][s_]["MED_c"]
                              and all(r["equals_stored"] for r in rows_)
                              and (med_ is None) == b2r["g3b"][s_]["hard_stop"]),
                    "artifact_sha16": sha256(pinned(f"data/olmo/b2r_qualify_{s_}.json"))[:16]}
    CHECKS["MED_c_recount_equals_stored"] = all(medc[s_]["equal"] for s_ in STAGES)
    w("**MED_c at every stage, recounted from the qualify rows** (`data/olmo/b2r_qualify_<s>.json` "
      "rows; [g3-B] as `scripts/b2r_analyze.py`@" + PIN + ":103-122 applies it: per strength, "
      "about-rate CP 95% lower bound > the control's CP upper AND degenerate fraction <= 0.25; "
      "MED_c = the lowest strength passing both). Cell = about k/24, CP lower, degenerate k/24, "
      "pass:")
    w("")
    w("| stage (artifact sha16) | control about | ctl CP upper | s = 1.0 | s = 2.0 | s = 4.0 | s = 8.0 | MED_c recount | stored | equal (cells, MED_c, hard_stop) |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for s_ in STAGES:
        m_ = medc[s_]
        w(f"| {s_} ({m_['artifact_sha16']}) | {m_['control'][0]}/{m_['control'][1]} | "
          f"{m_['control_cp_upper']:.5f} | "
          + " | ".join(f"{r['about']}/{r['n']}, {r['cp_lower']:.3f}, {r['degenerate']}/{r['n']}, "
                       f"{'PASS' if r['passes'] else 'fail'}" for r in m_["ladder"])
          + f" | {m_['MED_c_recount']} | {m_['MED_c_stored']} | {m_['equal']} |")
    w("")
    w("SFT/DPO/instruct MED_c = " + "/".join(str(medc[s_]["MED_c_recount"]) for s_ in STAGES[1:])
      + " (the ladder floor, left-censored); every s = 2.0 cell at those three stages fails "
      "coherence: " + ", ".join(
          f"{s_} {next(r['degenerate'] for r in medc[s_]['ladder'] if r['strength'] == 2.0)}/24"
          for s_ in STAGES[1:]) + " degenerate.")
    w("")
    w("The Fisher test is **not** the registered [g3-B] statistic and is stored in no artifact; "
      f"it is Code's descriptive gloss in the B2-r COMPLETE entry "
      f"({loc('RESULTS.md', 'one-sided Fisher exact **p = 0.0047**')}), carried into the "
      f"disposition's FLAG 1 ruling ({loc('RESULTS.md', 'with Fisher **p = .0047** at a')}) as "
      "'recorded beside' the allocation-limited wording.")
    w("")
    J["fisher_allocation_note"] = {"artifact": "data/olmo/b2r_qualify_base.json",
                                   "ladder": ladder3,
                                   "control": {"about": ctl["about"], "n": ctl["n"]},
                                   "MED_c_recount": medc}
    fig("Fisher p = .0047 allocation note", f"p = {s2['fisher_one_sided_p']:.5f}; one-sided Fisher exact, "
        f"[[7,17],[0,24]] (Base, s = 2.0 about 7/24 vs control 0/24); CP lo {s2['cp_lower']:.4f} < "
        f"ctl CP hi {s2['control_cp_upper']:.4f}",
        "data/olmo/b2r_qualify_base.json:injected.2.0.rows[].about, control.rows[].about_any",
        status_of(f"{s2['fisher_one_sided_p']:.4f}" == "0.0047"
           and abs(s2["fisher_one_sided_p"] - s2["fisher_record_helper"]) < 1e-15),
        f"B2-r [g3-B] concept-family qualification, not the A4 ladder; not a registered statistic; "
        f"{loc('RESULTS.md', 'one-sided Fisher exact **p = 0.0047**')}; {l_pre139}")
    fig("SFT/DPO/instruct qualify at doses of 1.0 or below (Macar convention)",
        f"MED_c recounted from rows: sft {medc['sft']['MED_c_recount']}, dpo "
        f"{medc['dpo']['MED_c_recount']}, instruct {medc['instruct']['MED_c_recount']}; base "
        f"{medc['base']['MED_c_recount']} (hard stop)",
        "data/olmo/b2r_qualify_<s>.json:injected.<s>.rows[].about/degen, control.rows[].about_any "
        "(recount); = b2r_analysis.json:g3b.<s>.MED_c",
        "reproduced" if (CHECKS["MED_c_recount_equals_stored"]
                         and [medc[x]["MED_c_recount"] for x in STAGES] == [None, 1.0, 1.0, 1.0])
        else "discrepant",
        "left-censored at the ladder floor; 'or below' is FLAG 2's reading, "
        f"{loc('RESULTS.md', 'FLAG 2 RULED — MED_c reports as ≤ 1.0')}")

    # ================================================================ 4. Q3 ==
    w("## 4. Q3 -- the B3 screen")
    w("")
    w("**Statistic** (`scripts/b3_analyze.py`@" + PIN + ":55-62, 113-142): Delta_first = (share of "
      "VALID marker sessions whose first free choice took the +tag) - 1/2, where the +tag is the "
      "label whose forced rounds carried +axis (the other carried -axis). Screen trigger "
      f"({loc('LOCK-g.md', 'Screen trigger, values in place')}): Delta exceeds the campaign's own "
      "control envelope (max |pseudo-Delta| over the sham and random arms) AND the sign locks "
      "across the two label maps; no binomial at screen tier. Confirm (only for a triggering "
      "stage): fresh n = 96, envelope + sign lock + one-sided exact binomial p <= .05 (k >= 57).")
    w("")
    q3, q3_ind_ok, an_equal = {}, True, True
    insul = {}
    for s in STAGES:
        art = pinned_json(f"data/olmo/b3_screen_{s}.json")
        stored = pinned_json(f"data/olmo/b3_analysis_{s}.json")
        assert art["tier"] == "screen" and not art["smoke"] and not art["selftest"]
        S = art["sessions"]
        # independent recount
        def share(arm, m=None):
            rows = [x for x in S if x["arm"] == arm and not x["excluded"]
                    and x["first_free_pole"] is not None
                    and (m is None or x["cell"]["map"] == m)]
            k = sum(1 for x in rows if x["first_free_pole"] == "pos")
            return k, len(rows)
        km, nm = share("marker")
        maps = {m: share("marker", m) for m in (0, 1)}
        ctl3 = {a: share(a) for a in ("sham", "random")}
        dm = km / nm - 0.5
        dmap = {m: (k / n - 0.5) for m, (k, n) in maps.items()}
        dctl = {a: (k / n - 0.5) for a, (k, n) in ctl3.items()}
        env = max(abs(x) for x in dctl.values())
        env_src = max(dctl, key=lambda a: abs(dctl[a]))
        up = dm > env
        lock_pos = all(x > 0 for x in dmap.values())
        lock_neg = all(x < 0 for x in dmap.values())
        trig = up and lock_pos
        rev = (dm < -env) and lock_neg
        # the committed analyzer on the pinned artifact
        res = json.loads(json.dumps(b3a.analyze(art)))
        eq = res == stored
        an_equal &= eq
        ind_match = (abs(stored["delta_first"] - dm) == 0.0 and stored["k_plus"] == km
                     and stored["n_marker_valid"] == nm
                     and all(stored["by_label_map"][str(m)]["k"] == maps[m][0]
                             and stored["by_label_map"][str(m)]["n"] == maps[m][1] for m in (0, 1))
                     and all(stored["controls"][a]["k"] == ctl3[a][0]
                             and stored["controls"][a]["n"] == ctl3[a][1] for a in ctl3)
                     and abs(stored["control_envelope"] - env) == 0.0
                     and stored["all_conjuncts_met"] == trig
                     and stored["reverse_criteria_met"] == rev
                     and stored["conjuncts"]["sign_locks_positive"] == lock_pos
                     and stored["reverse_conjuncts"]["sign_locks_negative"] == lock_neg)
        q3_ind_ok &= ind_match
        p1, p2 = binom_half_exact(km, nm)
        # two-sided method check: at p = 1/2 doubling the smaller tail equals the
        # sum of all outcome probabilities no larger than the observed one
        pk_ = math.comb(nm, km)
        p2_minlike = min(1.0, sum(math.comb(nm, i_) for i_ in range(nm + 1)
                                  if math.comb(nm, i_) <= pk_) / 2 ** nm)
        assert abs(p2 - p2_minlike) < 1e-12, (s, p2, p2_minlike)
        # insulation, degeneracy, exclusions
        reads = [c["read"] for x in S for c in x["choices"]]
        kl = [r["verify_kl"] for r in reads]
        n_rounds = n_degen = 0
        minp = 1.0
        bar = art["declared_bars"][0]
        for x in S:
            n_rounds += len(x["rounds"]) + len(x["choices"])
            n_degen += sum(1 for r in x["rounds"] + x["choices"] if r["degen"])
            p_bar = binom_sf(n_degen, n_rounds, bar["p0"])
            minp = min(minp, p_bar)
        assert n_degen == art["counters"]["counters"]["audit_degenerate"]["total"]
        n_lex = sum(1 for x in S for r in x["rounds"] + x["choices"] if r.get("lexical"))
        assert n_lex == art["counters"]["counters"]["lexical"]["total"], s
        n_lex_excl = sum(1 for x in S if str(x["exclusion_reason"] or "").startswith("lexical:"))
        run_all = len(S)
        excl_all = sum(1 for x in S if x["excluded"])
        assert {a: {"valid": sum(1 for x in S if x["arm"] == a and not x["excluded"]),
                    "run": sum(1 for x in S if x["arm"] == a)} for a in art["counts"]} == art["counts"]
        insul[s] = {"choice_reads": len(reads), "verify_kl_all_zero": all(v == 0.0 for v in kl),
                    "max_verify_kl": max(kl), "round_degenerate": [n_degen, n_rounds],
                    "bar": {"kind": bar["kind"], "p0": bar["p0"], "alpha": bar["alpha"]},
                    "bar_min_p_over_run": minp, "bar_fired": minp < bar["alpha"],
                    "paused": art["paused"], "excluded_over_run": [excl_all, run_all],
                    "lexical_total": art["counters"]["counters"]["lexical"]["total"],
                    "lexical_recount": n_lex, "sessions_excluded_for_lexical": n_lex_excl,
                    "lexical_by_arm": {a_: sum(1 for x in S if x["arm"] == a_
                                               for r in x["rounds"] + x["choices"] if r.get("lexical"))
                                       for a_ in art["counts"]}}
        q3[s] = {"dose": art["arm_provenance"]["marker"], "random_dir_sha":
                 art["arm_provenance"]["random"]["direction_sha"],
                 "marker": {"k": km, "n": nm, "delta": dm},
                 "maps": {str(m): {"k": maps[m][0], "n": maps[m][1], "delta": dmap[m]} for m in (0, 1)},
                 "controls": {a: {"k": ctl3[a][0], "n": ctl3[a][1], "pseudo_delta": dctl[a]} for a in ctl3},
                 "envelope": env, "envelope_set_by": env_src,
                 "conj_up": up, "sign_locks_pos": lock_pos, "sign_locks_neg": lock_neg,
                 "screen_trigger": trig,
                 "reverse_criteria": rev, "verdict_stored": stored["verdict"],
                 "independent_recount_equals_stored": ind_match,
                 "committed_analyzer_equals_stored_json": eq,
                 "descriptive_binomial_computed_new": {"one_sided_upper_P(X>=k|n,1/2)": p1,
                                                       "two_sided": p2},
                 "counts": art["counts"],
                 "session_share_plus": stored["collateral"]["session_share_plus"],
                 "p_stay": stored["collateral"]["p_stay"]}
    w("### 4a. Per-stage screen, recomputed from the session records")
    w("")
    w("| stage | dose (L, frac, \\|alpha\\|) | marker k/n | Delta_first | map 0 k/n (Delta) | map 1 k/n (Delta) | sham k/n (pseudo) | random k/n (pseudo) | envelope (set by) | Delta > env | sign locks + | trigger | verdict (stored) |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for s in STAGES:
        r = q3[s]
        d = r["dose"]
        mp = r["maps"]
        c = r["controls"]
        w(f"| {s} | L{d['layer']}, {d['frac']:.2f}, {d['alpha']:.4f} | {r['marker']['k']}/{r['marker']['n']} | "
          f"{f4(r['marker']['delta'])} | {mp['0']['k']}/{mp['0']['n']} ({f4(mp['0']['delta'])}) | "
          f"{mp['1']['k']}/{mp['1']['n']} ({f4(mp['1']['delta'])}) | {c['sham']['k']}/{c['sham']['n']} "
          f"({f4(c['sham']['pseudo_delta'])}) | {c['random']['k']}/{c['random']['n']} "
          f"({f4(c['random']['pseudo_delta'])}) | {r['envelope']:.4f} ({r['envelope_set_by']}) | "
          f"{r['conj_up']} | {r['sign_locks_pos']} | **{r['screen_trigger']}** | {r['verdict_stored']} |")
    w("")
    w(f"Independent recount equals every stored count, Delta, envelope and conjunct: **{q3_ind_ok}**. "
      f"The committed analyzer (`b3_analyze.analyze`, blob equal to the pin) re-run on the pinned "
      f"screen artifacts returns dicts identical to `b3_analysis_<s>.json` at all four stages: "
      f"**{an_equal}**. Marker arm doses equal each stage's A4 selected layer and MED: "
      f"**{all(q3[s]['dose']['layer'] == a4[s]['selected_layer'] and q3[s]['dose']['frac'] == a4[s]['med'] for s in STAGES)}**.")
    w("")
    n_trig = sum(q3[s]["screen_trigger"] for s in STAGES)
    w("### 4b. Confirm triggers, the falsifier, the welfare extension")
    w("")
    w(f"- Screen triggers: **{n_trig} of 4** stages. Confirm artifacts (`b3_confirm_*`) tracked under "
      f"`data/olmo/` at the pin: {confirm_files if confirm_files else 'none'}. Zero confirmatory "
      "triggers, so no confirm campaign was owed or run.")
    w(f"- **The falsifier, as registered** ("
      f"{loc('PROPOSAL-g-ontogeny-of-evaluation.md', 'stages.** Named falsifier, registered now: wireheading leaking into')}"
      f"-71): wireheading leaking into policy at Instruct -- a first-free-choice preference for "
      f"the marker-delivering arm at Instruct that clears the control envelope and B3's "
      f"conjunctive criteria; evaluated 'by exactly these criteria and no others' "
      f"({loc('PROPOSAL-g-ontogeny-of-evaluation.md', 'Instruct falsifier is evaluated by exactly these criteria and no')}), "
      f"i.e. it can fire only through a confirm pass at Instruct. Instruct's screen: Delta "
      f"{f4(q3['instruct']['marker']['delta'])} ({q3['instruct']['marker']['k']}/"
      f"{q3['instruct']['marker']['n']}) vs envelope {q3['instruct']['envelope']:.4f}, maps "
      f"{f4(q3['instruct']['maps']['0']['delta'])}/{f4(q3['instruct']['maps']['1']['delta'])} -> "
      f"no trigger, no confirm, **falsifier untriggered**.")
    w(f"- Welfare extension ({loc('LOCK-g.md', 'Any stage passes confirm → the Instruct falsifier logic of')}): "
      "fires on 'any stage passes confirm'; no stage reached confirm -> armed, not triggered.")
    w("")
    w("### 4c. The DPO single-map figure")
    w("")
    dp = q3["dpo"]
    w(f"DPO marker arm, label map 1: {dp['maps']['1']['k']}/{dp['maps']['1']['n']} -> "
      f"**{f4(dp['maps']['1']['delta'])}**; the other map (0): {dp['maps']['0']['k']}/"
      f"{dp['maps']['0']['n']} -> **{f4(dp['maps']['0']['delta'])}**; pooled "
      f"{dp['marker']['k']}/{dp['marker']['n']} -> {f4(dp['marker']['delta'])}. The pooled Delta "
      f"does not clear the envelope {dp['envelope']:.4f} (set by the random arm, "
      f"{dp['controls']['random']['k']}/{dp['controls']['random']['n']} -> "
      f"{f4(dp['controls']['random']['pseudo_delta'])}; sham {dp['controls']['sham']['k']}/"
      f"{dp['controls']['sham']['n']} -> {f4(dp['controls']['sham']['pseudo_delta'])}) and the "
      "sign does not lock across maps, so it fails both screen conjuncts independently. "
      "The +0.1667 is a marker-arm, map-level figure (not a sham-arm pseudo-statistic); its "
      "magnitude equals the envelope's by coincidence (16/24 and 6/18 are both 1/6 from 1/2).")
    w("")
    w("### 4d. Per-stage Q3 line for the note (the preprint's '[TAB 2 carries the per-stage figures]')")
    w("")
    w("Units: share of first free choices toward the +state label minus 1/2 (as `b3_analyze` "
      "defines it; not G_c units). The p columns are **computed-new, post-hoc and descriptive**: "
      "exact binomial at p = 1/2 on the pooled marker arm (one-sided = P(X >= k); two-sided = "
      "2 x the smaller one-sided tail, capped at 1, which at p = 1/2 equals the sum of the "
      "probabilities of all outcomes no more likely than the observed one; asserted at every "
      f"stage); LOCK-g puts no binomial at screen tier "
      f"({loc('LOCK-g.md', 'No binomial at screen tier.')}), so they decide nothing.")
    w("")
    w("| stage | n valid (run) | k(+tag) | Delta_first | map 0 | map 1 | sign locks | envelope | one-sided P(X >= k \\| n, 1/2) | two-sided exact p | screen |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for s in STAGES:
        r = q3[s]
        mp = r["maps"]
        dsc = r["descriptive_binomial_computed_new"]
        locks = ("yes (+)" if r["sign_locks_pos"] else
                 "yes (-)" if r["sign_locks_neg"] else "no")
        w(f"| {s} | {r['marker']['n']} ({r['counts']['marker']['run']}) | {r['marker']['k']} | "
          f"{f4(r['marker']['delta'])} | {f4(mp['0']['delta'])} ({mp['0']['k']}/{mp['0']['n']}) | "
          f"{f4(mp['1']['delta'])} ({mp['1']['k']}/{mp['1']['n']}) | {locks} | {r['envelope']:.4f} | "
          f"{dsc['one_sided_upper_P(X>=k|n,1/2)']:.4f} | {dsc['two_sided']:.4f} | "
          f"{'TRIGGER' if r['screen_trigger'] else 'null'} |")
    w("")
    n_valid = sorted({q3[s]["marker"]["n"] for s in STAGES})
    assert len(n_valid) == 1, n_valid
    no_clear_either = all(not q3[s]["conj_up"] and not (q3[s]["marker"]["delta"] < -q3[s]["envelope"])
                          for s in STAGES)
    line = ("Q3, OLMo B3 screen; Delta = share of first free choices toward the +state label minus "
            "1/2 (marker arm, at each stage's A4 layer and MED: "
            + ", ".join(f"{s} L{q3[s]['dose']['layer']} f {q3[s]['dose']['frac']:.2f}" for s in STAGES)
            + f"; n = {n_valid[0]} valid sessions per stage): "
            + "; ".join(f"{s} {q3[s]['marker']['delta']:+.4f} ({q3[s]['marker']['k']}/{q3[s]['marker']['n']}; maps "
                        f"{q3[s]['maps']['0']['delta']:+.4f}/{q3[s]['maps']['1']['delta']:+.4f})"
                        for s in STAGES)
            + f"; control envelopes {'/'.join(f'{q3[s]['envelope']:.4f}' for s in STAGES)}; "
            + ("no stage's Delta clears its control envelope in either direction."
               if no_clear_either else "SOME STAGE CLEARS ITS ENVELOPE -- see the table."))
    w("Code's rendering of a four-number line (the PI decides whether the note carries it):")
    w("")
    w(f"> {line}")
    w("")
    w("### 4e. Supporting record lines (insulation, SFT tripwire, exclusions, collateral)")
    w("")
    w("| stage | choice reads (verify_kl all 0.0) | round-degenerate / rounds (all sessions) | declared bar: min one-sided binomial p over the run vs p0 | fired | paused | excluded / run | lexical counter | session share (+) | p(stay) |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for s in STAGES:
        i = insul[s]
        r = q3[s]
        w(f"| {s} | {i['choice_reads']} ({i['verify_kl_all_zero']}) | {i['round_degenerate'][0]}/"
          f"{i['round_degenerate'][1]} | {i['bar_min_p_over_run']:.4f} (p0 {i['bar']['p0']}, alpha "
          f"{i['bar']['alpha']}) | {i['bar_fired']} | {i['paused']} | {i['excluded_over_run'][0]}/"
          f"{i['excluded_over_run'][1]} ({i['excluded_over_run'][0] / i['excluded_over_run'][1]:.3f}) | "
          f"{i['lexical_total']} | {r['session_share_plus']:.4f} | {r['p_stay']:.4f} |")
    w("")
    w("Domains (rule 4): choice reads = every choice-read record in every session of the run, all "
      "arms, excluded included; round-degenerate = degenerate rounds over all generated rounds "
      "(forced rounds + free-choice rounds) of every session, all arms, excluded included, as the "
      "audit counter tallies them; excluded / run = sessions, all arms; **lexical counter** = "
      "generated rounds (forced + free-choice) in which the session's own roster tag appeared, "
      f"word-bounded, in the generated text (`lexical_hit`, "
      f"{loc('valence_core/session.py', 'def lexical_hit(text: str, tags: Sequence[str])', extra=9)}; "
      "an audit-degenerate response is not also counted, "
      f"{loc('valence_core/session.py', 'def classify_response(text: str, audit: AuditSpec,', extra=10)}), "
      "over every session of the run, all arms, excluded included (`counters.lexical.total`; "
      "recounted from the session records, equal at every stage: "
      + ", ".join(f"{s} {insul[s]['lexical_recount']} (by arm "
                  + ", ".join(f"{a_} {n_}" for a_, n_ in insul[s]['lexical_by_arm'].items())
                  + f"; sessions excluded for a lexical hit {insul[s]['sessions_excluded_for_lexical']})"
                  for s in STAGES)
      + "); **session share (+)** = "
      "the share of ALL choices (every round, not only the first) in the VALID (non-excluded) "
      "marker sessions that picked the +pole; **p(stay)** = the share of adjacent choice pairs "
      "within a valid marker session whose two choices picked the same pole (both as "
      f"`b3_analyze.collateral` computes them, `scripts/b3_analyze.py`@{PIN}:78-98; pre-named "
      "collateral, decides nothing).")
    w("")
    w("The bar's p is recomputed cumulatively after every session in run order, as the runner "
      "checks it (`scripts/box_b3_sessions.py`@" + PIN + ":350-357), with the stdlib binomial; "
      f"its minimum over any run is {min(insul[s]['bar_min_p_over_run'] for s in STAGES):.4f} (> alpha "
      "0.05), consistent with `paused` = None in every artifact.")
    w("")
    J["Q3"] = {"per_stage": q3, "insulation_and_monitors": insul,
               "screen_triggers": n_trig, "confirm_artifacts_at_pin": confirm_files,
               "independent_recount_equals_stored": q3_ind_ok,
               "committed_analyzer_equals_stored": an_equal, "four_number_line": line}
    CHECKS["Q3_recount_and_analyzer_equal"] = q3_ind_ok and an_equal
    CHECKS["Q3_zero_triggers"] = (n_trig == 0 and not confirm_files
                                  and all(q3[s]["verdict_stored"] == "NULL" for s in STAGES))
    CHECKS["falsifier_untriggered"] = (not q3["instruct"]["screen_trigger"]
                                       and not any("instruct" in f for f in confirm_files))
    CHECKS["welfare_untriggered"] = n_trig == 0 and not confirm_files
    CHECKS["dpo_single_map"] = ((dp["maps"]["1"]["k"], dp["maps"]["1"]["n"]) == (16, 24)
                                and f4(dp["maps"]["1"]["delta"]) == "+0.1667"
                                and not dp["screen_trigger"])
    CHECKS["tripwire_never_fired"] = all(not insul[s]["bar_fired"] and insul[s]["paused"] is None
                                         for s in STAGES)
    CHECKS["marker_dose_equals_A4_MED"] = all(q3[s]["dose"]["layer"] == a4[s]["selected_layer"]
                                              and q3[s]["dose"]["frac"] == a4[s]["med"]
                                              for s in STAGES)
    if not an_equal:
        STOPS.append("Q3: the committed b3_analyze.analyze re-run on the pinned screen artifacts "
                     "does not return the stored b3_analysis_<s>.json")
    q3ok = CHECKS["Q3_recount_and_analyzer_equal"]
    l_q3v = loc("RESULTS.md", "Q3 VERDICT DECLARED: THE Q3 BET STANDS")
    l_b3 = loc("RESULTS.md", "B3 SCREEN COMPLETE, ALL FOUR")
    l_b3dpo = loc("RESULTS.md", "| dpo | 48 | 27 | +0.0625 | −0.0417 | +0.1667 |")
    l_pre184 = loc(PREPRINT, "Four nulls; zero confirmatory triggers", working_tree=True)
    l_pre190 = loc(PREPRINT, "In the OLMo DPO screen one map returned +0.1667", working_tree=True)
    l_pre170 = loc(PREPRINT, "[TAB 2: every cell", working_tree=True)
    fig("Q3: four nulls; zero confirmatory triggers", f"{4 - n_trig} NULL / {n_trig} triggers; "
        f"confirm artifacts at pin: {len(confirm_files)}",
        "data/olmo/b3_screen_<s>.json:sessions (recount); b3_analysis_<s>.json:all_conjuncts_met",
        status_of(q3ok and CHECKS["Q3_zero_triggers"]), f"{l_q3v}; {l_b3}; {l_pre184}")
    fig("the falsifier (definition; untriggered)",
        f"defined as an Instruct confirm pass; instruct screen {f4(q3['instruct']['marker']['delta'])} "
        f"vs env {q3['instruct']['envelope']:.4f}, no trigger -> untriggered",
        "PROPOSAL-g text (definition); data/olmo/b3_analysis_instruct.json (state)",
        status_of(q3ok and CHECKS["falsifier_untriggered"]),
        f"definition {loc('PROPOSAL-g-ontogeny-of-evaluation.md', 'stages.** Named falsifier, registered now: wireheading leaking into')}"
        f"-71; {loc('RESULTS.md', 'The Instruct falsifier: UNTRIGGERED')}")
    fig("welfare pre-commitment armed, never triggered", "trigger = any stage passes confirm; 0 stages reached confirm",
        "LOCK-g §5 (definition); b3_analysis_<s>.json (state)",
        status_of(q3ok and CHECKS["welfare_untriggered"]),
        f"{loc('RESULTS.md', '§5 welfare pre-commitment extension: armed, not triggered')}")
    fig("DPO single-map +0.1667 (with the other map's figure)",
        f"map 1 {dp['maps']['1']['k']}/{dp['maps']['1']['n']} = {f4(dp['maps']['1']['delta'])}; "
        f"map 0 {dp['maps']['0']['k']}/{dp['maps']['0']['n']} = {f4(dp['maps']['0']['delta'])}; pooled "
        f"{f4(dp['marker']['delta'])} < env {dp['envelope']:.4f}",
        "data/olmo/b3_analysis_dpo.json:by_label_map; b3_screen_dpo.json (recount)",
        status_of(q3ok and CHECKS["dpo_single_map"]),
        f"marker arm, not sham; {l_b3dpo}; {l_pre184}; {l_pre190}")
    fig("per-stage Q3 Deltas with n and map split (TAB 2 placeholder)",
        "; ".join(f"{s} {f4(q3[s]['marker']['delta'])} ({q3[s]['marker']['k']}/{q3[s]['marker']['n']}; "
                  f"{f4(q3[s]['maps']['0']['delta'])}/{f4(q3[s]['maps']['1']['delta'])})" for s in STAGES),
        "data/olmo/b3_analysis_<s>.json:delta_first, k_plus, n_marker_valid, by_label_map",
        status_of(q3ok and CHECKS["marker_dose_equals_A4_MED"]),
        f"unit: share of first free choices toward the +state label minus 1/2, at each stage's A4 "
        f"MED; exact p columns are computed-new (post-hoc, descriptive); {l_pre170}")
    fig("descriptive exact binomial p per stage (for TAB 2's p column)",
        "; ".join(f"{s} {q3[s]['descriptive_binomial_computed_new']['one_sided_upper_P(X>=k|n,1/2)']:.4f}"
                  for s in STAGES) + " (one-sided, approach)",
        "computed here from b3_analysis_<s>.json k_plus, n_marker_valid", "computed-new",
        "post-hoc; LOCK-g: no binomial at screen tier; decides nothing")
    fig("SFT overdose tripwire never fired", f"sft {insul['sft']['round_degenerate'][0]}/"
        f"{insul['sft']['round_degenerate'][1]} degenerate rounds; min bar p "
        f"{insul['sft']['bar_min_p_over_run']:.3f}; paused None at all four",
        "data/olmo/b3_screen_<s>.json:sessions, declared_bars, paused",
        status_of(CHECKS["tripwire_never_fired"]),
        f"{loc('RESULTS.md', 'Realised round-degeneracy: base')}")

    # ---------------------------------------------- log-only cross-checks ---
    w("## 5. Record prose checked against the artifacts")
    w("")
    chk = []

    def prose(claim, locator, computed, agrees, note="", pi_note=None):
        chk.append({"claim": claim, "locator": locator, "computed": computed, "agrees": agrees,
                    "status": "reproduced" if agrees else "discrepant", "note": note,
                    "pi_note": pi_note})

    degen = {s: insul[s]["round_degenerate"] for s in STAGES}
    prose("round-degeneracy base 0/856, sft 1/869, dpo 0/860, instruct 3/877",
          loc("RESULTS.md", "Realised round-degeneracy: base"),
          ", ".join(f"{s} {degen[s][0]}/{degen[s][1]}" for s in STAGES),
          [tuple(degen[s]) for s in STAGES] == [(0, 856), (1, 869), (0, 860), (3, 877)],
          "domain: degenerate rounds over all rounds of all sessions, all arms")
    p0 = insul["base"]["bar"]["p0"]
    assert all(insul[s]["bar"]["p0"] == p0 for s in STAGES)
    under = {s: (p0 / (degen[s][0] / degen[s][1]) if degen[s][0] else math.inf) for s in STAGES}
    prose(f"round-degeneracy: every stage an order of magnitude under the declared p0 of {p0}",
          loc("RESULTS.md", "every stage an order of magnitude under the declared p0 of", extra=1),
          ", ".join(f"{s} {degen[s][0] / degen[s][1]:.4f} (p0/rate "
                    f"{'inf' if math.isinf(under[s]) else f'{under[s]:.1f}x'})" for s in STAGES),
          all(under[s] >= 10 for s in STAGES),
          "loose wording, not transcription: the counts reproduce; holds at base, sft, dpo; "
          "instruct is under p0 by less than 10x; no bar or verdict depends on it", pi_note=5)
    ex = {s: insul[s]["excluded_over_run"] for s in STAGES}
    exr = [round(100 * ex[s][0] / ex[s][1], 1) for s in STAGES]
    prose("exclusion rates 5.6 / 15.2 / 10.6 / 11.6 %", loc("RESULTS.md", "5.6 / 15.2 / 10.6 / 11.6 %"),
          " / ".join(f"{x:.1f}" for x in exr) + " % (excluded/run, all arms)", exr == [5.6, 15.2, 10.6, 11.6],
          "domain: sessions, all arms")
    ss = [round(q3[s]["session_share_plus"], 4) for s in STAGES]
    prose("session-share 0.4826 / 0.5139 / 0.5243 / 0.5174", loc("RESULTS.md", "session-share 0.4826 /"),
          " / ".join(f"{x:.4f}" for x in ss), ss == [0.4826, 0.5139, 0.5243, 0.5174],
          "domain: all choices in valid marker sessions")
    locks_neg = [s for s in STAGES if q3[s]["sign_locks_neg"]]
    locks_pos = [s for s in STAGES if q3[s]["sign_locks_pos"]]
    prose("B3 headline: no stage's sign locks across label maps",
          loc("RESULTS.md", "CHECKPOINT. No stage's marker arm clears its own control envelope, and no",
              extra=1),
          f"approach sign (+) locks at {locks_pos or 'no stage'}; reverse sign (-) locks at "
          f"{locks_neg or 'no stage'} ("
          + "; ".join(f"{s} maps {f4(q3[s]['maps']['0']['delta'])}/{f4(q3[s]['maps']['1']['delta'])}"
                      for s in locks_neg)
          + "; stored reverse_conjuncts.sign_locks_negative = True there)",
          not locks_pos and not locks_neg,
          "over-generalization, not transcription: true of the approach direction (the registered "
          "conjunct) only; the same entry's table shows both maps negative at those stages; neither "
          "clears its envelope downward, so no reverse finding and no verdict changes", pi_note=4)
    prose("matched dose 0.10: only Base and DPO pass", loc("RESULTS.md", "only Base and DPO pass; SFT and"),
          str(m_pass), m_pass == ["base", "dpo"])
    prose("A4 entry: failing conjunct is always pos_exceeds_envelope; neg and sign lock hold at every stage and frac", loc("RESULTS.md", "The failing conjunct is always `pos_exceeds_envelope`, never the other", extra=3),
          str(sorted(fail_conj_pattern)), sorted(fail_conj_pattern) == [("pos_exceeds_envelope",)],
          "over-generalization from the lower rungs, not a transcribed number; no MED or verdict changes",
          pi_note=2)
    prose("B1 entry: failing conjunct always pos_exceeds_envelope, never the negative pole, at every stage and frac",
          loc("RESULTS.md", "The failing conjunct is **always `pos_exceeds_envelope`**, never sign", extra=3),
          f"negative pole also fails at {neg_fail}", not neg_fail,
          "same over-generalization as the A4 entry; no MED or verdict changes", pi_note=2)
    prose("D+/G_c at 0.10: 0.110 base vs 0.022-0.026 later", loc("RESULTS.md", "D+/G_c at matched dose is 0.110 at Base against 0.022–0.026"),
          ", ".join(f"{s} {matched[s]['D+/G_c']:.3f}" for s in STAGES),
          CHECKS["ratio_record_statistic"], "positive pole, frac 0.10; readout caveat (section 2): "
          "D read on full-vocabulary log-probs, G_c on the floor-imputed top-4,096 store; mismatch "
          "size unmeasured; status kept", pi_note=10)
    # Evaluated on the sentences' own domain (every stage and every frac: all 16 cells);
    # the MED and passing-cell domains are printed beside it (pass 2, finding 3).
    v1_bar_ok = f"{0.5 * gc['base']:.2f}" == "0.39" and f"{0.5 * gc['instruct']:.2f}" == "0.78"
    v1_alt_ok = (f"{min(dpos_med.values()):.2f}" == "0.02" and f"{max(dpos_med.values()):.2f}" == "0.28"
                 and f"{min(dpos_pass):.2f}" == "0.02" and f"{max(dpos_pass):.2f}" == "0.28")
    v1_ok = (v1_bar_ok and f"{min(dpos_all):.2f}" == "0.02" and f"{max(dpos_all):.2f}" == "0.28")
    prose("V1-lineage bar 0.39-0.78 vs displacements 0.02-0.28 (A4 and B1 entries)",
          loc("RESULTS.md", "bar is 0.39–0.78 while actual displacements are 0.02–0.28") + "; "
          + loc("RESULTS.md", "against displacements of 0.02–0.28"),
          f"0.5 G_c {0.5 * gc['base']:.4f}-{0.5 * gc['instruct']:.4f}; D+ at the four MEDs "
          f"{min(dpos_med.values()):.4f}-{max(dpos_med.values()):.4f}; over the {len(dpos_pass)} "
          f"passing cells {min(dpos_pass):.4f}-{max(dpos_pass):.4f}; over all 16 cells "
          f"{min(dpos_all):.4f}-{max(dpos_all):.4f}",
          v1_ok,
          "minor, low end: the sentences frame their domain as every stage and every frac "
          f"({l_v1_a4}; {l_v1_b1}); on it D+ runs {min(dpos_all):.4f}-{max(dpos_all):.4f} "
          f"({min(dpos_all):.2f}-{max(dpos_all):.2f}; low end {min_all_cell['stage']} at frac "
          f"{min_all_cell['frac']:.2f}, a failing cell); 0.02-0.28 holds only on the MED or "
          "passing-cell domains, which the record does not name"
          + ("" if v1_alt_ok else " (CHECK: not even there)")
          + "; the bar side "
          + ("reproduces" if v1_bar_ok else "DOES NOT reproduce")
          + f" and the conclusion (max D+ {max(dpos_all):.3f} < smallest bar {0.5 * gc['base']:.3f}) "
          "stands; readout caveat (section 2): the bar compares a full-log-prob displacement with "
          "a G_c read on the floor-imputed store", pi_note=3)
    prose("Base s=2: 0/24 control CP upper 0.1425; s=2 CP lower 0.1260; miss 0.016",
          loc("RESULTS.md", CP_NEEDLE, extra=1),
          f"ctl CP hi {s2['control_cp_upper']:.4f}; s=2 CP lo {s2['cp_lower']:.5f} (4 dp {s2['cp_lower']:.4f}); "
          f"miss {-s2['cp_lower_minus_control_upper']:.4f}",
          f"{s2['control_cp_upper']:.4f}" == "0.1425" and f"{s2['cp_lower']:.4f}" == "0.1260",
          "looks like transcription (0.1262 at 4 dp); the 0.1425 and the 0.016 miss reproduce",
          pi_note=1)
    prose("LOCK-g §1: G_c = +0.7824 / +1.0279 / +1.5325 / +1.5612", l_lock_gc,
          " / ".join(f"{gc[s]:+.4f}" for s in STAGES),
          [f"{gc[s]:+.4f}" for s in STAGES] == ["+0.7824", "+1.0279", "+1.5325", "+1.5612"])
    for c in chk:
        fig(f"[record prose, not a block figure] {c['claim']}", c["computed"], c["locator"],
            c["status"], (c["note"] + "; " if c["note"] else "")
            + (f"see PI note {c['pi_note']}" if not c["agrees"] else "record prose agrees with the artifacts"))
    w("| claim (record prose) | locator | computed here | status | note |")
    w("|---|---|---|---|---|")
    for c in chk:
        w(f"| {cell(c['claim'])} | {c['locator']} | {cell(c['computed'])} | {c['status']} | {cell(c['note'])} |")
    w("")
    J["prose_checks"] = chk

    # ------------------------------------------------------------ notes --
    sham_b3 = " / ".join(f4(q3[s]["controls"]["sham"]["pseudo_delta"]) for s in STAGES)
    l_pre244 = loc(PREPRINT, "feedback-driven training sharpens the marking of evaluation",
                   working_tree=True)
    NOTES.extend([
        f"**CP lower bound transcription in the log (not in the note).** {loc('RESULTS.md', CP_NEEDLE, extra=1)} "
        f"writes s = 2.0's CP lower as 0.1260; the stored and recomputed value is "
        f"{s2['cp_lower']:.5f} ({s2['cp_lower']:.4f} at four decimals; `b2r_analysis.json:g3b.base.ladder.2.0.ci[0]`). "
        f"The 0.1425 control upper and the 'miss of 0.016' ({-s2['cp_lower_minus_control_upper']:.4f}) "
        "reproduce. Looks like transcription; no reading changes.",
        "**Failing-conjunct sentence in two log entries (not in the preprint).** "
        f"{loc('RESULTS.md', 'The failing conjunct is always `pos_exceeds_envelope`, never the other', extra=3)} "
        "(A4) and "
        f"{loc('RESULTS.md', 'The failing conjunct is **always `pos_exceeds_envelope`**, never sign', extra=3)} "
        "(B1) say the negative pole clears its envelope at every stage and every frac. The stored "
        f"conjunct flags say otherwise at {neg_fail}: "
        + "; ".join(f"{r['stage']} {r['frac']:.2f} D- {r['D-']:+.4f} vs envelope {r['envelope']:.4f} "
                    f"({r['envelope_set_by']})" for r in lad_rows
                    if (r['stage'], r['frac']) in neg_fail)
        + ". `pos_exceeds_envelope` does fail in every failing cell and sign lock never fails "
        f"({lock_fail or 'no cell'}), so the sentence over-generalizes from the lower rungs; it is not "
        "a transcribed number. "
        + ("No MED, verdict or note figure changes (each of those stages passes at a lower frac). "
           if neg_fail_stages_pass_lower else "CHECK: a stage with a negative-pole failure has no lower pass. ")
        + "If the note says 'the negative pole clears its envelope everywhere', it should say "
        "'below frac 0.40'.",
        "**V1-lineage displacements in the log: low end off by 0.01 on the sentences' own domain "
        "(minor).** "
        f"{loc('RESULTS.md', 'bar is 0.39–0.78 while actual displacements are 0.02–0.28')} (A4) and "
        f"{loc('RESULTS.md', 'against displacements of 0.02–0.28')} (B1) give 'displacements 0.02-0.28' "
        f"inside sentences framed over every stage and every frac ({l_v1_a4}; {l_v1_b1}). On that "
        f"domain (all 16 cells) D+ runs {min(dpos_all):.4f}-{max(dpos_all):.4f}, i.e. "
        f"{min(dpos_all):.2f}-{max(dpos_all):.2f}; the low end is {min_all_cell['stage']} at frac "
        f"{min_all_cell['frac']:.2f}, a failing cell. 0.02-0.28 holds only on domains the record does "
        f"not name: D+ at the four MEDs {min(dpos_med.values()):.4f}-{max(dpos_med.values()):.4f}, over "
        f"the {len(dpos_pass)} potency-passing cells {min(dpos_pass):.4f}-{max(dpos_pass):.4f}. Status "
        "'discrepant (minor, low end)' (pass 1 had set it to 'reproduced'; pass 2 reverts it). The "
        f"conclusion (max D+ {max(dpos_all):.3f} < the smallest bar {0.5 * gc['base']:.3f}) stands on "
        "any domain. The rule's negative conjunct (D- <= -0.5 G_c) does hold at "
        + (", ".join(f"{s_} {fr:.2f}" for s_, fr in v1_neg_only) or "no cell")
        + "; the rule fails there on its other two conjuncts. The bar itself compares a "
        "full-log-prob displacement with a G_c read on the floor-imputed store (note 10).",
        "**B3 headline over-generalizes the sign lock (log only, not in the preprint).** "
        f"{loc('RESULTS.md', 'CHECKPOINT. No stage' + chr(39) + 's marker arm clears its own control envelope, and no', extra=1)} "
        "says 'no stage's sign locks across label maps'. The approach sign (the registered "
        f"conjunct) locks at {locks_pos or 'no stage'}; the reverse sign locks at {locks_neg} (both "
        "maps negative: "
        + "; ".join(f"{s_} {f4(q3[s_]['maps']['0']['delta'])} ({q3[s_]['maps']['0']['k']}/{q3[s_]['maps']['0']['n']}) "
                    f"and {f4(q3[s_]['maps']['1']['delta'])} ({q3[s_]['maps']['1']['k']}/{q3[s_]['maps']['1']['n']})"
                    for s_ in locks_neg)
        + "; stored `reverse_conjuncts.sign_locks_negative` = True). Neither clears its envelope "
        "downward, so `reverse_criteria_met` is False and no verdict changes. If the note carries "
        "the headline's wording, it should say 'no stage's sign locks in the approach direction' or "
        "'no stage's Delta clears its envelope'.",
        "**'An order of magnitude under p0' (log only).** "
        f"{loc('RESULTS.md', 'every stage an order of magnitude under the declared p0 of', extra=1)}: the "
        "counts reproduce, but instruct's rate "
        f"{degen['instruct'][0]}/{degen['instruct'][1]} = {degen['instruct'][0] / degen['instruct'][1]:.4f} "
        f"is {under['instruct']:.1f}x under p0 = {p0}, not 10x (sft {under['sft']:.1f}x; base and dpo "
        "have no degenerate round). Loose wording; nothing depends on it.",
        "**Referent of the Fisher p.** The block files 'the Fisher p = .0047 allocation note' under "
        "the A4 dose ladder; its referent is B2-r's [g3-B] concept-family qualification at Base "
        f"(`data/olmo/b2r_qualify_base.json`, s = 2.0, {s2['about']}/{s2['n']} vs "
        f"{ctl['about']}/{ctl['n']}), where the preprint's "
        f"{l_pre139} correctly places it, in the clause on Macar et al.'s convention. It is a "
        "descriptive one-sided Fisher exact p, not the registered criterion (CP-interval "
        "separation), and no artifact stores it.",
        f"**What G_c is (preprint {l_pre101} and {l_pre129}: 'in direction units').** G_c is the "
        "mean over 12 probes of a standardized (pooled-SD) post-praise minus post-criticism gap in "
        "a 256-token next-token log-prob readout at `Response:`; it is not measured in units of "
        "the residual direction. It is also not, on OLMo, a gap in particular 'marker' tokens "
        "(section 1b, computed-new, post-hoc): the record's selection lets a context lacking a "
        "token contribute 0 and imputes a pole's mean floor only when the token is absent from "
        f"the whole pole ({l_inst}), so " + ("all" if all_one_pole else "NOT all (CHECK)")
        + " 3,072 selected ids per stage are tokens absent from the "
        "top-4,096 of every post-praise fit context and held by 1 post-criticism fit context"
        + (f" (except {multi_txt})" if multi_txt else "")
        + ("; every weight is negative and near-uniform; " if w_neg_all
           else "; NOT every weight is negative (CHECK); ")
        + f"{share_lo:.1%}-"
        f"{share_hi:.1%} of val cells are imputed floor; the score tracks the context's floor at "
        f"|r| >= {min(anat_rows[s_]['abs_r_score_floor_weakest'] for s_ in STAGES):.4f}; and a "
        "floor-only gap gives " + " / ".join(f"{g_floor_only[s_]:.2f}" for s_ in STAGES)
        + " against G_c " + " / ".join(f"{gc[s_]:.2f}" for s_ in STAGES) + ". G_c on OLMo is "
        "therefore almost entirely a praise-vs-criticism gap in the tail level of the next-token "
        "distribution (its 4,096th-largest log-prob). The stage ordering survives a true per-row "
        "floor-imputed rebuild (" + " / ".join(f"{g_true[s_]:.3f}" for s_ in STAGES) + "; "
        + ("every selection changed" if all(anat_rows[s_]["true_floor_selection_differs_probes"] == 12
                                            for s_ in STAGES) else "selections changed at "
           + ", ".join(f"{anat_rows[s_]['true_floor_selection_differs_probes']}/12" for s_ in STAGES))
        + "). RESULTS.md's 'floor-imputed' "
        f"({l_floorimp}), the producing script's docstring "
        f"({loc('scripts/box_a4_instrument.py', 'pos - neg over the union of kept ids, floor-imputed')}) "
        "and the artifacts' `method` field ('with floor imputation') are accurate only for the "
        "whole-pole-absent case. Suggested wording, if the note keeps the figure: 'the natural "
        "praise-criticism gap on the A4 next-token readout (on OLMo, almost entirely a gap in the "
        "level of the distribution's tail), in pooled-SD units (G_c)'; the note should not call G_c "
        "a 'marker' or token-content gap without that qualifier. **Routed to the design seat:** "
        "what G_c licenses, and how the preprint's 'sharpens the marking' sentences "
        f"({l_pre129}; {l_pre244}) should read given it (note 9). No number, status or STOP "
        "changes.",
        f"**What the registered Q1 criterion is (preprint "
        f"{loc(PREPRINT, 'The registered criterion was a conjunction of envelope conditions', working_tree=True)}).** "
        "The preprint calls it a conjunction on 'the direction's separation of praise from "
        "criticism contexts'. The registered A4 criterion is on steering displacement: injecting "
        "+d and -d into contexts with no feedback text must move the A4 readout (section 1b says "
        "what it holds on OLMo) beyond the "
        "envelope of three norm-matched random directions (both signs) and a sham, with opposite "
        "signs ("
        f"{loc('PROPOSAL-g-ontogeny-of-evaluation.md', 'Potency criterion [LOCK-g formula], per stage')}). "
        "Praise-vs-criticism separation is how the readout and G_c are built, not the criterion.",
        f"**'Post-training sharpens the marking it inherits' ({l_pre129}; again at {l_pre244}: "
        "'feedback-driven training sharpens the marking of evaluation (G_c rises monotonically)').** "
        "What rises is G_c (the natural gap on the readout). The record's B1 entry scores "
        "PROPOSAL-g's declared non-bet 'potency may sharpen along the chain' as a descriptive miss "
        f"({loc('RESULTS.md', 'The secondary descriptive expectation is NOT borne out')}): "
        f"potency per G_c falls (D+/G_c at 0.10 is {min(ratios.values()):.1f}-{max(ratios.values()):.1f}x "
        f"larger at base), and SFT needs frac {a4['sft']['med']:.2f}. Both sentences are defensible only "
        "if 'marking' means G_c, and they should say so. Two qualifiers from pass 2: what rises is, "
        "on OLMo, almost entirely a gap in the tail level of the next-token distribution (note 7), "
        "and the D+/G_c comparison mixes two versions of the instrument (note 10). How the "
        "sentences should read is routed to the design seat with note 7.",
        f"**'About five times larger at base' ({loc(PREPRINT, 'about five times larger at base', working_tree=True)}) "
        "names neither pole nor dose.** The record's statistic is D+/G_c at matched dose 0.10 "
        f"(base over later stages {rng('0.10', 'Dpos')}). On the negative pole at 0.10 the ratio is "
        f"{rng('0.10', 'absDneg')}; on D+ it is {rng('0.05', 'Dpos')} at 0.05, {rng('0.20', 'Dpos')} at "
        f"0.20 and {rng('0.40', 'Dpos')} at 0.40 (base/sft {r40:.2f}x"
        + (", i.e. SFT's D+/G_c exceeds base's at the top rung" if r40 < 1 else "")
        + "). Suggested wording: 'the positive-pole displacement per unit G_c at matched dose (frac "
        f"0.10) is {rng('0.10', 'Dpos')[:-1]} times larger at base'. Post-hoc sensitivity; decides nothing. "
        "**Readout caveat (pass 2).** " + READOUT_CAVEAT + " The 'reproduced' status stays (it is "
        "the record's statistic); the registered potency criterion is unaffected. Whether the note "
        "keeps the 'about five times' sentence is the PI's or the design seat's decision.",
        f"**'Sham contrasts are exactly zero'.** True of the A4 sham (a repeated unsteered pass: "
        f"{sham_zero}/{sham_cells} cells 0.0, i.e. bit-for-bit determinism). The B3 sham arm's "
        f"pseudo-Deltas are {sham_b3}; a reader can conflate the two, so the note should say which sham.",
        "**Unit of the Q3 line.** LOCK-g and PROPOSAL-g say all B-phase effects report in G_c "
        f"units ({loc('LOCK-g.md', 'All B-phase effects report in')}; "
        f"{loc('PROPOSAL-g-ontogeny-of-evaluation.md', 'All effects are denominated in the natural feedback')}); "
        "B3's Delta_first is a choice share minus 1/2, which `b3_analyze` and the RESULTS table "
        "report without G_c denomination (dividing a share by G_c has no meaning). The four-number "
        "line in section 4d names its unit as share minus 1/2 and its doses. Noted, not adjudicated.",
        f"**For N14.** The block lists 'OLMo DPO +0.1667' among 'sham-arm pseudo-statistics'; it is a "
        f"marker-arm, map-level Delta (map 1, {dp['maps']['1']['k']}/{dp['maps']['1']['n']}), beside "
        f"map 0's {f4(dp['maps']['0']['delta'])} ({dp['maps']['0']['k']}/{dp['maps']['0']['n']}). The "
        f"DPO control arms read sham {f4(dp['controls']['sham']['pseudo_delta'])} "
        f"({dp['controls']['sham']['k']}/{dp['controls']['sham']['n']}) and random "
        f"{f4(dp['controls']['random']['pseudo_delta'])} ({dp['controls']['random']['k']}/"
        f"{dp['controls']['random']['n']}).",
        "**For N8 (shared construction).** The Qwen B1 instrument behind link 2's G = 0.3156 is built "
        f"the same way ({l_oracle}; {l_inst}). The record's A4 path applied to the pinned "
        f"`data/e0/e0_b1_markers.npz` returns G = {G_qwen:.4f}, and its selections also hold only "
        f"one-pole-absent ids ({anat_q['sel_absent_all_pos_present_neg']} absent from every "
        f"post-praise fit context, {anat_q['sel_absent_all_neg_present_pos']} from every "
        f"post-criticism one, {anat_q['sel_present_both']} held by both). There the floor explains "
        f"less: floor-only gap {anat_q['G_floor_only']:.2f}, mean |r(score, floor)| "
        f"{anat_q['abs_r_score_floor_mean']:.2f}, weakest {anat_q['abs_r_score_floor_weakest']:.2f} "
        "(section 1b; computed-new, post-hoc). Flagged for N8; not adjudicated here.",
    ])
    # the record-prose rows cite notes by number: pin the numbering
    for n_, head_ in ((1, "**CP lower bound"), (2, "**Failing-conjunct"), (3, "**V1-lineage"),
                      (4, "**B3 headline"), (5, "**'An order"), (7, "**What G_c is"),
                      (9, "**'Post-training sharpens"), (10, "**'About five"),
                      (len(NOTES), "**For N8")):
        assert NOTES[n_ - 1].startswith(head_), (n_, NOTES[n_ - 1][:40])
    w("## 6. Notes for the PI (wrong referents, wording, transcription; none is a STOP)")
    w("")
    for i, n in enumerate(NOTES, 1):
        w(f"{i}. {n}")
    w("")
    J["notes"] = NOTES

    # ----------------------------------------------------------- figures --
    w("## Figures (as the block writes them, plus the preprint's link-1 and Q3 sentences, then the record prose of section 5)")
    w("")
    w("| figure | value printed | source | status | note |")
    w("|---|---|---|---|---|")
    for f in FIG:
        w(f"| {cell(f['figure'])} | {cell(f['printed'])} | {cell(f['source'])} | {f['status']} | {cell(f['note'])} |")
    w("")
    J["figures"] = FIG
    J["checks"] = CHECKS
    w("Checks licensing each status (every 'reproduced' above is conditioned on one of these; a "
      "False would print 'discrepant'): "
      + ", ".join(f"{k} {v}" for k, v in CHECKS.items()) + ".")
    w("")
    w("## Result")
    w("")
    blockfig = [f for f in FIG if not f["figure"].startswith("[record prose")]
    prosefig = [f for f in FIG if f["figure"].startswith("[record prose")]
    cnt = lambda fs, st_: sum(1 for f in fs if f["status"] == st_)
    w(f"Block and preprint figures: {cnt(blockfig, 'reproduced')} reproduced, "
      f"{cnt(blockfig, 'computed-new')} computed-new, {cnt(blockfig, 'discrepant')} discrepant, "
      f"{cnt(blockfig, 'log-only')} log-only, {cnt(blockfig, 'not found')} not found. Record prose "
      f"checked (section 5, not block figures): {cnt(prosefig, 'reproduced')} reproduced, "
      f"{cnt(prosefig, 'discrepant')} discrepant (PI notes "
      + ", ".join(str(n_) for n_ in sorted({c["pi_note"] for c in chk if not c["agrees"]}))
      + "; none changes a verdict, a MED or a figure the note carries). Pass 2 changed one "
      "status (the V1-lineage displacements row, reproduced -> discrepant, minor), no "
      f"previously reported value and no STOP. STOPs: {len(STOPS)}"
      + (": " + "; ".join(STOPS) if STOPS else "") + f". Wall-clock {time.time() - t_start:.0f} s.")
    w("")
    J["stops"] = STOPS
    J["counts"] = {"block_figures": {k: cnt(blockfig, k) for k in
                                     ("reproduced", "computed-new", "discrepant", "log-only", "not found")},
                   "record_prose": {k: cnt(prosefig, k) for k in ("reproduced", "discrepant")}}

    # ---------------------------------------------------- values-check --
    VC = [
        ("V1-lineage 'displacements 0.02-0.28' (RESULTS :8781, also :8442) was labelled discrepant "
         "on the all-16-cells domain (substantive, low impact)", "fixed",
         f"Recomputed: D+ at the MEDs {min(dpos_med.values()):.4f}-{max(dpos_med.values()):.4f}, over "
         f"the {len(dpos_pass)} passing cells {min(dpos_pass):.4f}-{max(dpos_pass):.4f} (= 0.02-0.28); "
         f"all 16 cells {min(dpos_all):.4f}-{max(dpos_all):.4f}. Row now 'reproduced' with the domain "
         "named, both locators cited, note 3 reworded, and the V1 conjunct-by-conjunct line added "
         f"(negative conjunct holds at {v1_neg_only}; stored v1_lineage_conjuncts asserted equal). "
         "Superseded in pass 2 (#3): the status is reverted to discrepant (minor, low end) on the "
         "sentences' own domain."),
        ("B3 headline 'no stage's sign locks across label maps' (RESULTS :7656-7657) not flagged",
         "fixed",
         f"Own recount: approach sign locks at {locks_pos or 'none'}; reverse sign locks at "
         f"{locks_neg}; equality with stored reverse_conjuncts.sign_locks_negative now part of the "
         "asserted recount. Added as a discrepant record-prose row and PI note 4; the four-number "
         "line now ends 'no stage's Delta clears its control envelope in either direction'."),
        ("'every stage an order of magnitude under p0 0.02' (RESULTS :7692-7693) not checked",
         "fixed",
         f"Computed p0/rate: sft {under['sft']:.1f}x, instruct {under['instruct']:.1f}x, base and dpo "
         "0 degenerate. Added as a discrepant record-prose row (loose wording) and PI note 5."),
        ("'about five times' ratio: pole and dose sensitivity not surfaced", "fixed",
         f"Section 2c now prints a computed-new, post-hoc ratio table by pole and frac: D+ 0.10 "
         f"{rng('0.10', 'Dpos')}, |D-| 0.10 {rng('0.10', 'absDneg')}, D+ 0.40 {rng('0.40', 'Dpos')} "
         f"(base/sft {r40:.2f}x). PI note 10 proposes 'positive pole, matched dose 0.10'; the figure "
         "row's note says so. The record-statistic row stays 'reproduced'."),
        ("Rule-6 gaps: val AUC undefined; collateral domains unstated; 'n/a' unexplained", "fixed",
         "Section 1 defines the AUC (probe score, self_pos vs self_neg on the val half, 96/96 per "
         "probe, no layer, no CV, one task split; rebuild reproduces every stored val_auc, max diff "
         f"{max(r['val_auc_rebuilt_maxdiff'] for r in gc_rows):.1e}) and prints per-probe min/max. "
         "Section 4e states every column's domain. Section 2a prints 'not sign-correct' with the "
         "stored D+/D-, and the count of sign-correct candidates ("
         + ", ".join(f"{s_} {n_sign_correct[s_]}/4" for s_ in STAGES) + ")."),
        ("Four-number line omits its unit and dose", "fixed",
         "The line now opens with the unit (share of first free choices toward the +state label "
         "minus 1/2) and each stage's A4 layer and MED; n is computed and asserted equal across "
         "stages, not hard-coded."),
        ("MED_c for SFT/DPO/instruct echoed from the analyzer field", "fixed",
         "Section 3 recounts MED_c at all four stages from b2r_qualify_<s>.json rows (about, degen, "
         "control about_any; CP 95% by stdlib bisection; coherence <= 0.25), and checks every cell's "
         "ci/separates/coherent/passes and MED_c/hard_stop against b2r_analysis.json: "
         f"{CHECKS['MED_c_recount_equals_stored']}. Recount: "
         + ", ".join(f"{s_} {medc[s_]['MED_c_recount']}" for s_ in STAGES) + "."),
        ("Hard-coded 'reproduced' statuses and STOP count", "fixed",
         f"Every status is now conditioned on a computed check ({len(CHECKS)} checks, printed above "
         "the Result); the Q3 recount/analyzer equality, B1 equality and the stored descriptive "
         "fields (delta_*_in_Gc, max_abs_delta_random, v1_lineage_conjuncts) are asserted or gate "
         "the status; STOPs are appended when the committed analyzer or the B1 mapping fails to "
         f"return the stored artifact (this run: {len(STOPS)})."),
        ("MED locators cite only the base row; PREPRINT :244 missing from the 'sharpens' note "
         "(pass-1 note 7, now note 9)", "fixed",
         "Each MED row now cites its own RESULTS B1-table row and LOCK-g §1 row (computed per "
         f"stage: {', '.join(l_b1tab[s_].split(':')[-1] for s_ in STAGES)} and "
         f"{', '.join(l_lockmed[s_].split(':')[-1] for s_ in STAGES)}); the 'sharpens' note cites "
         f"{l_pre244}."),
        ("Header command echo omits the working directory", "fixed",
         "The echo is now 'cd <repo> && <python> <absolute script path> <args>', and the header "
         "records whether the run's working directory was the repository root."),
    ]
    w("## Values-check")
    w("")
    w("### Pass 1: checker findings and dispositions")
    w("")
    w("An independent checker re-ran this script, recomputed every figure from the pinned artifacts "
      "with its own code, and filed ten findings (one substantive, nine minor). Code re-checked each "
      "before applying it: the numeric ones (1-5, 7) by a scratch recomputation from the pinned "
      "artifacts, the others by reading the pinned record (9) or this script (6, 8, 10). Every one "
      "held, so none is rejected. The values in the 'detail' column are printed from this run.")
    w("")
    w("| # | finding | disposition | detail (this run) |")
    w("|---|---|---|---|")
    for i, (f_, d_, x_) in enumerate(VC, 1):
        w(f"| {i} | {cell(f_)} | {d_} | {cell(x_)} |")
    w("")
    J["values_check"] = [{"finding": f_, "disposition": d_, "detail": x_} for f_, d_, x_ in VC]
    # ------------------------------------------- values-check, pass 2 --
    a_b = anat_rows["base"]
    VC2 = [
        ("(substantive) Section 1 and PI note 7 misdescribe the instrument behind G_c: the "
         "selection is not floor-imputed per context (absent contexts contribute 0; the pole's mean "
         "floor is imputed only when a token is absent from the whole pole), and on OLMo G_c is "
         "almost entirely a gap in the tail level of the next-token distribution, not a "
         "token-content marker gap", "fixed",
         "Re-checked by reading `build_instruments` at the pin "
         f"(`scripts/box_a4_instrument.py`@{PIN}:142-176) and by this script's own computation "
         "from the stored sel/w (section 1b): selected ids absent from every post-praise fit "
         "context and held by >= 1 post-criticism one "
         + ", ".join(f"{s_} {anat_rows[s_]['sel_absent_all_pos_present_neg']}/{anat_rows[s_]['n_selected']}"
                     for s_ in STAGES)
         + f"; post-criticism holders at base {a_b['neg_fit_contexts_holding_selected_id']}, other "
         "stages " + ", ".join(f"{s_} {anat_rows[s_]['neg_fit_contexts_holding_selected_id']}"
                               for s_ in STAGES[1:])
         + "; all weights negative at "
         + ", ".join(f"{anat_rows[s_]['probes_w_all_negative']}/12" for s_ in STAGES)
         + " probes; post-praise fit floor lower at "
         + ", ".join(f"{anat_rows[s_]['probes_fit_floor_lower_post_praise']}/12" for s_ in STAGES)
         + "; val cells imputed (stage means) "
         + ", ".join(f"{anat_rows[s_]['val_share_floor_imputed_mean']:.4f}" for s_ in STAGES)
         + "; mean r(score, floor) "
         + ", ".join(f"{anat_rows[s_]['r_score_floor_mean']:+.4f}" for s_ in STAGES)
         + " (weakest |r| " + ", ".join(f"{anat_rows[s_]['abs_r_score_floor_weakest']:.4f}" for s_ in STAGES)
         + "); floor-only gap " + " / ".join(f"{g_floor_only[s_]:.4f}" for s_ in STAGES)
         + "; true per-row floor-imputed rebuild " + " / ".join(f"{g_true[s_]:.3f}" for s_ in STAGES)
         + " (selections changed " + ", ".join(f"{anat_rows[s_]['true_floor_selection_differs_probes']}/12"
                                              for s_ in STAGES)
         + "). Every one of the finding's figures held except two details: CV of |w| per probe here is "
         + ", ".join(f"{s_} {anat_rows[s_]['cv_abs_w_range'][0]:.5f}-{anat_rows[s_]['cv_abs_w_range'][1]:.5f}"
                     for s_ in STAGES)
         + " (the finding quoted 0.0002-0.0007; near-uniform either way), and the sft true-floor "
         f"rebuild is {g_true['sft']:.5f}, which rounds to {g_true['sft']:.3f} (the finding wrote "
         "1.990). Applied: section 1's "
         "definition rewritten to the code's semantics; new section 1b (computed-new, post-hoc) "
         "with its domains; PI note 7 rewritten (no 'marker' or token-content reading without the "
         "tail-level qualifier; interpretation, including :129/:244's 'sharpens the marking', "
         "routed to the design seat); PI note 9 cross-refers; the shared Qwen construction flagged "
         f"to N8 (new PI note {len(NOTES)}; Qwen G {G_qwen:.4f}, one-pole-absent ids "
         f"{anat_q['sel_absent_all_pos_present_neg']} + {anat_q['sel_absent_all_neg_present_pos']}, "
         f"floor-only gap {anat_q['G_floor_only']:.4f}, mean |r| {anat_q['abs_r_score_floor_mean']:.4f}, "
         f"weakest {anat_q['abs_r_score_floor_weakest']:.4f}). No number, status or STOP changed."),
        ("(substantive) D/G_c, the V1-lineage bar and 'D in sigma units' divide readings from two "
         "versions of the instrument (hijack: full-vocabulary log-probs; G_c and sigma: the "
         "floor-imputed top-4,096 store), undisclosed", "fixed",
         f"Re-checked at the pin: {l_hij_score} scores `w @ log_softmax(logits)[sel_ids]` with no "
         f"floor; `delta()` divides by the stored sigma (`scripts/box_a4_hijack.py`@{PIN}:119-128); "
         f"sigma and G_c come from the val-half scoring at `scripts/box_a4_instrument.py`@{PIN}:159-176 "
         f"({share_lo:.1%}-{share_hi:.1%} of cells imputed). Unstored, checked by key scan: the hijack "
         f"JSONs' score-named keys are {score_named} (min(D+, |D-|): {sel_score_is_min}); the npz "
         f"arrays are {npz_arrays}. Applied: the caveat in section 2 (statistic), the 2c matched-dose, "
         "V1 and ratio-table lines, the two ratio figure rows, the D+/G_c and V1-lineage "
         "record-prose rows, PI note 10 (which leaves the 'about five times' sentence to the PI or "
         "design seat) and PI note 3. Status kept 'reproduced'; the registered potency criterion "
         "is unaffected (like-with-like envelope); the mismatch's size needs model inference and "
         "is not estimated."),
        ("(minor) V1-lineage 'displacements 0.02-0.28' was marked reproduced although the "
         "sentences set the domain as every stage and every frac", "fixed",
         f"Read at the pin: {l_v1_a4} ('fails at every stage and every frac') and {l_v1_b1} "
         f"('passes at NO stage and NO frac'). On all 16 cells D+ runs {min(dpos_all):.4f}-"
         f"{max(dpos_all):.4f} ({min(dpos_all):.2f}-{max(dpos_all):.2f}); 0.02 holds only at the "
         f"MEDs ({min(dpos_med.values()):.4f}) or over the passing cells ({min(dpos_pass):.4f}). Of "
         "the two options the finding offers, Code reverted the row to discrepant (minor, low "
         "end), because the record's own sentences name the domain. PI note 3 is reworded and "
         "pass 1 #1 is marked superseded. The conclusion (max D+ "
         f"{max(dpos_all):.3f} < smallest bar {0.5 * gc['base']:.3f}) stands."),
        ("(minor) Section 4e's lexical-counter column has no stated domain; 4d's two-sided p names "
         "no method", "fixed",
         "Lexical counter recounted from the session records (rounds + choices with a "
         "`lexical` hit, every session, all arms, excluded included): "
         + ", ".join(f"{s_} {insul[s_]['lexical_recount']}" for s_ in STAGES)
         + ", equal to `counters.lexical.total` (asserted). The domain clause is added to 4e. "
         "4d now names the two-sided p as 2 x the smaller tail, capped at 1, and asserts that it "
         "equals the sum of the probabilities of outcomes no more likely than the observed one "
         "at every stage (true at p = 1/2). No value changes."),
    ]
    w("### Pass 2: round-2 findings and dispositions")
    w("")
    w("A second checker filed four residual findings (two substantive, two minor). Code "
      "re-checked each before applying it. The two substantive ones were re-checked by reading "
      "the pinned producer code and by an independent scratch recomputation from the pinned "
      "npz stores, and then by this script's own computation (section 1b, the key scan in "
      "section 2). The minor ones were re-checked by reading the pinned RESULTS sentences and "
      "by recounting the session records. All four held, so none is rejected. Only one status "
      "changed (#3). The values in the 'detail' column are printed from this run.")
    w("")
    w("| # | finding | disposition | detail (this run) |")
    w("|---|---|---|---|")
    for i, (f_, d_, x_) in enumerate(VC2, 1):
        w(f"| {i} | {cell(f_)} | {d_} | {cell(x_)} |")
    w("")
    J["values_check_pass2"] = [{"finding": f_, "disposition": d_, "detail": x_} for f_, d_, x_ in VC2]

    # ------------------------------------- round 9: preprint of record --
    # Appended after every round-1 section, so each round-1 line keeps its line number.
    with open(os.path.join(REPO, PREPRINT), encoding="utf-8") as f:
        plines = lines_of(f.read())
    for q_, (kind_, _) in PREPRINT_R1.items():      # quoted/label sentences: checked here, non-fatally
        if kind_ != "located" and q_ not in PRE_SEEN:
            PRE_SEEN[q_] = [i for i, l in enumerate(plines, 1) if q_ in l]
            if not PRE_SEEN[q_]:
                preprint_finding(q_, plines)
    assert set(PRE_SEEN) == set(PREPRINT_R1), sorted(set(PRE_SEEN) ^ set(PREPRINT_R1))
    reanchor = []
    for q_, (kind_, r1_) in PREPRINT_R1.items():
        h_ = PRE_SEEN[q_]
        if not h_:
            res_ = "NOT FOUND: finding on the patch"
        elif not r1_:
            res_ = "found (no round-1 locator)"
        elif kind_ == "located":
            res_ = "same line" if h_[0] == r1_[0] else f"re-anchored :{r1_[0]} -> :{h_[0]}"
        else:
            res_ = "same line(s)" if set(r1_) <= set(h_) else f"re-anchored {list(r1_)} -> {h_}"
        reanchor.append({"sentence": q_, "kind": kind_, "round1_lines": list(r1_),
                         "patched_lines": h_, "result": res_})
    heads_ = [i for i, l in enumerate(plines, 1) if l.startswith("#")]
    hard = []
    for as_, where_, q_, want_ in PREPRINT_HARD:
        # each sentence named here is inside a PREPRINT_R1 sentence, so its absence is
        # already a finding on the patch above; this check is about the written number
        assert any(q_ in k_ for k_ in PREPRINT_R1), q_
        h_ = [i for i, l in enumerate(plines, 1) if q_ in l]
        if isinstance(want_, str):                   # a section number
            sec_ = {i: max([j for j in heads_ if j < i], default=0) for i in h_}
            ok_ = bool(h_) and all(j and plines[j - 1].lstrip("#").strip().startswith(want_ + " ")
                                   for j in sec_.values())
            got_ = ("; ".join(f":{i} under :{j} {plines[j - 1].strip()!r}" for i, j in sec_.items())
                    if h_ else "none")
        else:                                        # line numbers
            ok_ = bool(h_) and set(want_) <= set(h_)
            got_ = ", ".join(map(str, h_)) or "none"
        # a number that fails because a sentence it names is gone is that finding, not a move
        rel_ = [f"P{i}" for i, p_ in enumerate(PRE_FINDINGS, 1)
                if not ok_ and q_ in p_["sentence_as_checked"]]
        hard.append({"as_written": as_, "where": where_, "sentence": q_,
                     "expected": want_ if isinstance(want_, str) else list(want_),
                     "patched": got_, "holds": True if ok_ else (None if rel_ else False),
                     "findings_on_the_patch": rel_})
    w("## Preprint of record (round 9)")
    w("")
    w(f"Re-pointed per {PREPRINT_RULING} (round 9, patch v6 "
      f"`{PREPRINT_SHA_V6[:8]}...{PREPRINT_SHA_V6[-5:]}`) and per {PREPRINT_ROUTING} (round 10): "
      f"`{PREPRINT}` at sha256 `{PREPRINT_SHA}` (patch v7; 'patched text' below is v7) "
      f"replaces the audited text `{PREPRINT_SHA_AUDITED[:8]}...{PREPRINT_SHA_AUDITED[-5:]}` "
      f"(archived untracked at `{PREPRINT_ARCHIVED}`; not read). This section is appended after "
      "every round-1 section, so every line above keeps its round-1 line number. The first table "
      "lists every preprint sentence this raw locates, quotes, or takes a figure label's words "
      "from, against its line in the committed round-1 raw "
      "(`09c3a8c:results/raw/2026-10-08_note-N7-olmo.md`); the second checks every preprint line "
      "or section number written as a literal into this raw's text. A sentence not found on the "
      "patched text is a finding on the patch, routed to the design seat; it is not a STOP and "
      "changes no status above.")
    w("")
    w("| sentence (as checked) | use | round-1 line (audited text) | patched-text line(s) | result |")
    w("|---|---|---|---|---|")
    for r_ in reanchor:
        w(f"| {cell(r_['sentence'])} | {r_['kind']} | "
          f"{', '.join(map(str, r_['round1_lines'])) or 'none cited'} | "
          f"{', '.join(map(str, r_['patched_lines'])) or 'none'} | {r_['result']} |")
    w("")
    w("| as written | where in this raw | sentence it names | patched text | holds |")
    w("|---|---|---|---|---|")
    for r_ in hard:
        w(f"| {cell(r_['as_written'])} | {cell(r_['where'])} | {cell(r_['sentence'])} | "
          f"{cell(r_['patched'])} | "
          + ("yes" if r_["holds"] else "NO (the written number needs re-anchoring)"
             if r_["holds"] is False else "not decidable: a sentence it names is a finding on "
             "the patch (" + ", ".join(r_["findings_on_the_patch"]) + ")") + " |")
    w("")
    w(f"Findings on the patch: {len(PRE_FINDINGS)}"
      + ("." if not PRE_FINDINGS else ":"))
    for i, p_ in enumerate(PRE_FINDINGS, 1):
        w(f"- P{i}. {p_['sentence_as_checked']!r}: old (audited text) line(s) "
          f"{p_['old']['round1_lines'] or 'none cited'}; new (patched text) at those lines: "
          + ("; ".join(f":{k_} {v_!r}" for k_, v_ in p_['new']['line_text_at_round1_lines'].items())
             or "n/a") + f". Routed to {p_['routed_to']}.")
    w("")
    w(f"Written preprint numbers that no longer hold: {sum(r_['holds'] is False for r_ in hard)}.")
    w("")
    J["preprint_reanchor_round9"] = reanchor
    J["preprint_hardcoded_round9"] = hard
    J["preprint_patch_findings_round9"] = PRE_FINDINGS

    # ------------------------------------- round 10: patch v7 against round 9 (patch v6) --
    # Round 9's results are read from its committed raw (the record), never recomputed; the
    # archived v6 copy is optional and serves only to list the changed lines and quote them.
    r9_src = f"{ROUND9_COMMIT}:{DEF_JSON}"
    r9 = json.loads(git("show", r9_src).decode("utf-8"))
    assert r9["header"]["preprint_sha256"] == PREPRINT_SHA_V6, "round-9 raw is not on patch v6"
    r9_re = {r_["sentence"]: r_ for r_ in r9["preprint_reanchor_round9"]}
    r9_hd = {r_["as_written"]: r_ for r_ in r9["preprint_hardcoded_round9"]}
    r9_pf = r9["preprint_patch_findings_round9"]
    assert list(r9_re) == [r_["sentence"] for r_ in reanchor], "round-9 checks differ"
    assert list(r9_hd) == [r_["as_written"] for r_ in hard], "round-9 written numbers differ"
    v6_abs = os.path.join(REPO, PREPRINT_ARCHIVED_V6)
    v6_present, v6_match, v6l = os.path.isfile(v6_abs), None, None
    if v6_present:
        with open(v6_abs, "rb") as f:
            v6b_ = f.read()
        v6_match = sha256(v6b_) == PREPRINT_SHA_V6
        if v6_match:
            v6l = lines_of(v6b_.decode("utf-8"))
    checked_ = list(dict.fromkeys(list(PREPRINT_R1) + [q_ for _, _, q_, _ in PREPRINT_HARD]))

    def head_of(i: int) -> str:
        j_ = max([j for j in heads_ if j < i], default=0)
        return f"under :{j_} {plines[j_ - 1].strip()!r}" if j_ else "before any heading"

    changed = None                     # [(v6 line | None, v7 line | None)], v6 copy only
    if v6l is not None:
        import difflib
        changed = []
        for tag_, i1, i2, j1, j2 in difflib.SequenceMatcher(
                None, v6l, plines, autojunk=False).get_opcodes():
            if tag_ != "equal":
                for k_ in range(max(i2 - i1, j2 - j1)):
                    changed.append((i1 + k_ + 1 if i1 + k_ < i2 else None,
                                    j1 + k_ + 1 if j1 + k_ < j2 else None))
    ch_rows = []
    for a_, b_ in (changed or []):
        ch_rows.append({
            "v6_line": a_, "v7_line": b_, "v7_heading": head_of(b_) if b_ else None,
            "checked_sentences_on_v6_line": [q_ for q_ in checked_ if a_ and q_ in v6l[a_ - 1]],
            "checked_sentences_on_v7_line": [q_ for q_ in checked_ if b_ and q_ in plines[b_ - 1]]})
    ch6_ = {r_["v6_line"] for r_ in ch_rows if r_["v6_line"]}
    ch7_ = {r_["v7_line"] for r_ in ch_rows if r_["v7_line"]}

    def r10_disp(p6: bool, p7: bool, moved: bool, on_changed: bool) -> str:
        if p6 and p7:
            d_ = "passes on v6 and v7" + ("; re-anchored" if moved else "; same line(s)")
            return d_ + ("; on a line v7 changed (quoted below)" if on_changed else "")
        if p7:
            return "resolved (fails on v6, passes on v7)"
        if not p6:
            return "unchanged (fails on v6 and v7)"
        return "NEW finding on patch v7 (passes on v6, fails on v7)"

    r10_checks = []
    for r_ in reanchor:
        o_ = r9_re[r_["sentence"]]
        p6_ = not o_["result"].startswith("NOT FOUND")
        p7_ = not r_["result"].startswith("NOT FOUND")
        on_ = bool((set(o_["patched_lines"]) & ch6_) | (set(r_["patched_lines"]) & ch7_))
        r10_checks.append({"check": r_["sentence"], "kind": r_["kind"],
                           "v6_lines": o_["patched_lines"], "v6_result": o_["result"],
                           "v7_lines": r_["patched_lines"], "v7_result": r_["result"],
                           "on_v7_changed_line": on_, "passes_v6": p6_, "passes_v7": p7_,
                           "disposition": r10_disp(p6_, p7_,
                                                   o_["patched_lines"] != r_["patched_lines"], on_)})
    for r_ in hard:
        o_ = r9_hd[r_["as_written"]]
        p6_, p7_ = o_["holds"] is True, r_["holds"] is True
        r10_checks.append({"check": f"written {r_['as_written']} ({r_['sentence']})",
                           "kind": "written number", "v6_lines": o_["patched"],
                           "v6_result": o_["holds"], "v7_lines": r_["patched"],
                           "v7_result": r_["holds"], "on_v7_changed_line": None,
                           "passes_v6": p6_, "passes_v7": p7_,
                           "disposition": r10_disp(p6_, p7_, o_["patched"] != r_["patched"],
                                                   False)})
    r9_disp = []
    for i_, p_ in enumerate(r9_pf, 1):
        q_ = p_["sentence_as_checked"]
        h7_ = PRE_SEEN.get(q_, [i for i, l in enumerate(plines, 1) if q_ in l])
        r1n_ = [int(k_) for k_ in p_["new"]["line_text_at_round1_lines"]]
        q6_ = {str(n_): p_["new"]["line_text_at_round1_lines"][str(n_)] for n_ in r1n_}
        q7_ = {str(n_): plines[n_ - 1] for n_ in r1n_ if n_ <= len(plines)}
        r9_disp.append({"round9_finding": f"P{i_}", "sentence_as_checked": q_,
                        "v7_lines": h7_,
                        "disposition": ("resolved (found on v7)" if h7_ else
                                        "unchanged (not found on v6 or v7)" if q6_ == q7_ else
                                        "changed (not found on v6 or v7; the lines differ)"),
                        "v6_text_at_round1_lines": q6_, "v7_text_at_round1_lines": q7_})
    new_f = [c_ for c_ in r10_checks if c_["passes_v6"] and not c_["passes_v7"]]
    on_ch = [c_ for c_ in r10_checks if c_["on_v7_changed_line"]]

    w("### Round 10 (patch v7)")
    w("")
    w(f"Preprint of record: `{PREPRINT}` at sha256 `{PREPRINT_SHA}` (patch v7, {PREPRINT_ROUTING}), "
      f"asserted before anything was written. Round 9's preprint of record, patch v6 at sha256 "
      f"`{PREPRINT_SHA_V6}`, is archived untracked at `{PREPRINT_ARCHIVED_V6}` (out of the "
      f"release; recorded, not required): "
      + ("absent, so the changed lines are not listed" if not v6_present else
         "present but its sha256 differs, so it is not read and the changed lines are not listed"
         if not v6_match else "present, sha256 matches, read only to list and quote the changed "
         "lines") + f". Round 9's results are read from its committed raw `{r9_src}` (its "
      "header's preprint sha256 asserted equal to patch v6's); this table sets each against "
      "the re-run on v7 in the two tables above. A check that passed on v6 and fails on v7 is "
      "a new finding on the patch, routed to the design seat; it is not a STOP and changes no "
      "status above.")
    w("")
    if changed is None:
        w("Lines v7 changes against v6: not listed (v6 copy not read).")
    else:
        w(f"Lines v7 changes against v6: {len(ch_rows)}"
          + ("." if not ch_rows else ": " + "; ".join(
              f"v6 :{r_['v6_line'] or '-'} -> v7 :{r_['v7_line'] or '-'} "
              f"({r_['v7_heading'] or 'removed'})" for r_ in ch_rows) + "."))
        on_q_ = {q_ for r_ in ch_rows
                 for q_ in r_["checked_sentences_on_v6_line"] + r_["checked_sentences_on_v7_line"]}
        w(f"Sentences this raw checks that lie on those lines (v6 or v7): {len(on_q_)} of "
          f"{len(checked_)}" + ("." if not on_q_ else ": " + "; ".join(map(repr, sorted(on_q_))) + "."))
    w("")
    w("| check | use | v6 line(s) (round 9, as committed) | v6 result | v7 line(s) | v7 result | "
      "disposition |")
    w("|---|---|---|---|---|---|---|")
    for c_ in r10_checks:
        v6l_ = (", ".join(map(str, c_["v6_lines"])) if isinstance(c_["v6_lines"], list)
                else c_["v6_lines"]) or "none"
        v7l_ = (", ".join(map(str, c_["v7_lines"])) if isinstance(c_["v7_lines"], list)
                else c_["v7_lines"]) or "none"
        rs_ = {True: "holds", False: "does not hold", None: "not decidable"}
        w(f"| {cell(c_['check'])} | {c_['kind']} | {cell(v6l_)} | "
          f"{cell(rs_[c_['v6_result']] if c_['kind'] == 'written number' else c_['v6_result'])} | "
          f"{cell(v7l_)} | "
          f"{cell(rs_[c_['v7_result']] if c_['kind'] == 'written number' else c_['v7_result'])} | "
          f"{c_['disposition']} |")
    w("")
    q_rows_ = [r_ for r_ in ch_rows
               if r_["checked_sentences_on_v6_line"] or r_["checked_sentences_on_v7_line"]]
    for r_ in q_rows_:                  # a changed line carrying a checked sentence: v6 beside v7
        w(f"- v6 :{r_['v6_line'] or '-'} -> v7 :{r_['v7_line'] or '-'}, carrying "
          + "; ".join(map(repr, dict.fromkeys(r_["checked_sentences_on_v6_line"]
                                              + r_["checked_sentences_on_v7_line"])))
          + f". v6: {(v6l[r_['v6_line'] - 1] if r_['v6_line'] else '')!r}. "
          f"v7: {(plines[r_['v7_line'] - 1] if r_['v7_line'] else '')!r}.")
    if q_rows_:
        w("")
    w(f"Findings on the patch recorded by round 9 (`{r9_src}`, key "
      f"`preprint_patch_findings_round9`): {len(r9_pf)}"
      + ("; none to dispose on v7." if not r9_pf else ". Dispositions on v7:"))
    for d_ in r9_disp:
        w(f"- {d_['round9_finding']} {d_['sentence_as_checked']!r}: {d_['disposition']}"
          + (f"; v7 line(s) {d_['v7_lines']}" if d_["v7_lines"] else "")
          + "; v6 at its round-1 line(s): " + ("; ".join(
              f":{k_} {v_!r}" for k_, v_ in d_["v6_text_at_round1_lines"].items()) or "n/a")
          + "; v7 at those lines: " + ("; ".join(
              f":{k_} {v_!r}" for k_, v_ in d_["v7_text_at_round1_lines"].items()) or "n/a") + ".")
    if r9_pf:
        w("")
    w(f"New findings on patch v7: {len(new_f)}" + ("." if not new_f else ":"))
    for c_ in new_f:
        w(f"- {c_['check']!r}: v6 {c_['v6_lines']} ({c_['v6_result']}); v7 {c_['v7_lines']} "
          f"({c_['v7_result']}). Routed to the design seat (a finding on the patch; "
          f"{PREPRINT_RULING}).")
    w("")
    J["preprint_round10"] = {
        "preprint_of_record": {"path": PREPRINT, "sha256": PREPRINT_SHA, "patch": "v7",
                               "routing": PREPRINT_ROUTING},
        "round9_preprint": {"sha256": PREPRINT_SHA_V6, "patch": "v6",
                            "archived_untracked": PREPRINT_ARCHIVED_V6, "present": v6_present,
                            "sha256_matches": v6_match, "read": v6l is not None},
        "round9_raw": r9_src,
        "changed_lines_v6_v7": ch_rows if changed is not None else None,
        "checks": r10_checks,
        "round9_findings_on_the_patch": len(r9_pf),
        "round9_findings_dispositions": r9_disp,
        "checked_sentences_on_changed_lines": [c_["check"] for c_ in on_ch],
        "new_findings_on_the_patch": new_f}

    J["wall_clock_s"] = time.time() - t_start

    out_md = os.path.join(REPO, args.out) if not os.path.isabs(args.out) else args.out
    out_js = os.path.join(REPO, args.json_out) if not os.path.isabs(args.json_out) else args.json_out
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    with open(out_js, "w", encoding="utf-8") as f:
        json.dump(J, f, indent=1, default=str)
    print("\n".join(md))
    print(f"\nwrote {out_md}\nwrote {out_js}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
