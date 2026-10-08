#!/usr/bin/env python3
"""AUDIT-note-release v1.2, item N3, parts (i), (i-b) and (v): the echo-probe
figures the Research Note carries, reproduced from COMMITTED JSON only.

No model, no residual array, no refit. Every input is read with
`git show <PIN>:<path>` (PIN = bbc9ffe, the commit that placed the block), so
every figure and every locator is pinned to one commit; the working-tree copy
of each input is hashed beside its blob. Parts (ii)-(iv) (refits on the local
residual arrays) are assigned to a sibling item (N3c), whose raw is
results/raw/2026-10-08_note-N3-echo-compute.md (+ .json). Sections 0-10 of
this raw do not depend on it. Section 11 (the link-3 sentence and a proposed
nonlinear line, for the design seat) reads the sibling's JSON from the WORKING
TREE (it is uncommitted at the pin), prints its sha256, quotes its figures as
N3c's, and cross-checks the ones that can be checked against the committed
artifacts; if that JSON is absent or unreadable, section 11 says so and quotes
nothing. Section 11 also reads the sibling's raw .md from the working tree
(uncommitted) for three strings that are not in the JSON -- N3c's two status
tags (F1's band, '~.58') and its advice on which nonlinear figure to quote --
and prints that .md's sha256 and the line each string came from.

Every status in section 7 is computed by one stated rule (section 7's header):
quoted ranges at the quote's own precision, bounds at full precision, on the
domain the quote or its source states.

Stdlib only; nothing from the repository is imported; the only files written
are --out and --json-out.

    python -I scripts/audit_note_N3.py [--out PATH] [--json-out PATH]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shlex
import statistics
import subprocess
import sys
from decimal import ROUND_FLOOR, ROUND_HALF_UP, Decimal

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = "bbc9ffe"
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA_ROUTED = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
DEF_OUT = "results/raw/2026-10-08_note-N3-echo-robustness.md"
DEF_JSON = "results/raw/2026-10-08_note-N3-echo-robustness.json"
SIBLING = "results/raw/2026-10-08_note-N3-echo-compute.md"
SIBLING_JSON = "results/raw/2026-10-08_note-N3-echo-compute.json"
SCRIPT_REL = "scripts/audit_note_N3.py"

DATA_INPUTS = [
    "data/echo/stageA_analysis.json", "data/echo/stageA_posthoc_lastround.json",
    "data/echo/stageA_posthoc2_labelpole.json", "data/echo/stageA_reads.json",
    "data/echo/stageB_analysis.json", "data/echo/stageB_analysis_samefolds.json",
    "data/echo/stageB_reads.json", "data/echo/stageC_analysis.json",
    "data/echo/stageC_reads.json", "data/echo/timing.json",
    "data/k/k1_analysis.json", "data/k/k1_reads.json", "data/e2a/sessions.jsonl",
    "results/raw/2026-09-06_recon_echo_stageC_analysis.txt",
]
TEXT_INPUTS = [
    "RESULTS.md", "PROPOSAL-k-echo-channel.md", "scripts/recon_echo.py",
    "valence_core/echo/probe.py", "valence_core/discrim.py",
    "valence_core/k/analysis.py", "scripts/k1_analyze.py", "CLAUDE.md",
]

L_ALL = [40, 44, 48] + list(range(49, 64))       # the stored probe layers
L_ABOVE = list(range(49, 64))
LE48 = [40, 44, 48]


# --------------------------------------------------------------------------- io
def git(*args) -> bytes:
    return subprocess.run(["git", "-C", REPO, *args], capture_output=True, check=True).stdout


_blob: dict = {}


def blob(path: str) -> bytes:
    if path not in _blob:
        _blob[path] = git("show", f"{PIN}:{path}")
    return _blob[path]


def jload(path: str):
    return json.loads(blob(path).decode("utf-8"))


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


_lines: dict = {}
LOC_MISSES: list = []


def loc(path: str, needle: str, after: str | None = None) -> str:
    """`path@PIN:line` of the first line containing `needle` (after the first
    line containing `after`, if given). A miss is recorded and printed."""
    if path not in _lines:
        _lines[path] = blob(path).decode("utf-8").split("\n")
    ls = _lines[path]
    start = 0
    if after is not None:
        a = [i for i, l in enumerate(ls) if after in l]
        if not a:
            LOC_MISSES.append((path, after))
            return f"{path}@{PIN}:NOT-FOUND"
        start = a[0]
    hits = [i + 1 for i, l in enumerate(ls) if i >= start and needle in l]
    if not hits:
        LOC_MISSES.append((path, needle))
        return f"{path}@{PIN}:NOT-FOUND"
    return f"{path}@{PIN}:{hits[0]}"


def loc_range(path: str, first: str, last: str, after: str | None = None) -> str:
    """`path@PIN:a-b`: a = the line of `first` (after `after`), b = the first line at
    or after a that contains `last`. A miss is recorded as in loc()."""
    a = loc(path, first, after)
    if a.endswith("NOT-FOUND"):
        return a
    la = int(a.rsplit(":", 1)[1])
    ls = _lines[path]
    hits = [i + 1 for i, l in enumerate(ls) if i + 1 >= la and last in l]
    if not hits:
        LOC_MISSES.append((path, last))
        return f"{path}@{PIN}:{la}-NOT-FOUND"
    return f"{path}@{PIN}:{la}" + (f"-{hits[0]}" if hits[0] != la else "")


# ------------------------------------------------------------------- statistics
def binom_cdf(k: int, n: int, p: float) -> float:
    if k < 0:
        return 0.0
    if k >= n:
        return 1.0
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k + 1))


def clopper_pearson(k: int, n: int, alpha: float = 0.05) -> tuple:
    """Exact two-sided (1 - alpha) interval by bisection on the binomial CDF."""
    def bis(f):
        lo, hi = 0.0, 1.0
        for _ in range(80):
            mid = (lo + hi) / 2
            if f(mid):
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    lower = 0.0 if k == 0 else bis(lambda p: 1 - binom_cdf(k - 1, n, p) < alpha / 2)
    upper = 1.0 if k == n else bis(lambda p: binom_cdf(k, n, p) > alpha / 2)
    return lower, upper


def f3(x):
    return "n/a" if x is None else f"{x:.3f}"


def f4(x):
    return "n/a" if x is None else f"{x:.4f}"


def fs(x):
    return f"{x:+.4f}"


# ---------------------------------------------------- the status rule (section 7)
def _dec(q: str) -> Decimal:
    return Decimal("0" + q if q.startswith(".") else q)


def _places(q: str) -> int:
    return len(q.split(".")[1]) if "." in q else 0


def qr(x, q: str) -> Decimal:
    """x rounded half-up to the number of decimals the quote `q` writes."""
    return Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-_places(q)), rounding=ROUND_HALF_UP)


def _n(x) -> str:
    return str(x) if isinstance(x, int) else f"{x:.4f}"


def chk_range(vals, lo: str, hi: str):
    """R1, range: min and max rounded to the quote's decimals must equal the quoted endpoints."""
    mn, mx = min(vals), max(vals)
    ok = qr(mn, lo) == _dec(lo) and qr(mx, hi) == _dec(hi)
    return ok, f"min {_n(mn)} -> {qr(mn, lo)}, max {_n(mx)} -> {qr(mx, hi)} against {lo}-{hi}: {'holds' if ok else 'FAILS'}"


def chk_bound(vals, op: str, x: str):
    """R1, bound: an inequality, checked at full precision."""
    xv = float(_dec(x))
    if op == "<=":
        ext, ok, nm = max(vals), all(v <= xv for v in vals), "max"
    else:
        ext, ok, nm = min(vals), all(v >= xv for v in vals), "min"
    return ok, f"{nm} {ext:.4f} {op} {x} at full precision: {'holds' if ok else 'FAILS'}"


def chk_single(v, q: str):
    """R1, a single value for a single stored quantity."""
    ok = qr(v, q) == _dec(q)
    return ok, f"{_n(v)} -> {qr(v, q)} against {q}: {'holds' if ok else 'FAILS'}"


def chk_central(vals, q: str):
    """R1, a single '≈ x' for a per-layer series: mean and median must both round to x."""
    m, md = statistics.fmean(vals), statistics.median(vals)
    ok = qr(m, q) == _dec(q) and qr(md, q) == _dec(q)
    return ok, (f"mean {m:.4f} -> {qr(m, q)}, median {md:.4f} -> {qr(md, q)} against ≈ {q}: {'holds' if ok else 'FAILS'} "
                f"(per-value {min(vals):.4f}-{max(vals):.4f})")


def status_of(ok: bool, stored_ok: bool = True) -> str:
    """R3: wording-only failure on exactly reproduced stored values = transcription class."""
    if ok:
        return "reproduced"
    return "discrepant (transcription)" if stored_ok else "discrepant"


# ------------------------------------------------------------------ the report
class Out:
    def __init__(self):
        self.lines: list = []

    def __call__(self, s: str = ""):
        self.lines.append(s)

    def table(self, header, rows):
        self("| " + " | ".join(header) + " |")
        self("|" + "---|" * len(header))
        for r in rows:
            self("| " + " | ".join(str(c) for c in r) + " |")
        self()


FIGS: list = []
REF_NOTES: list = []
STOPS: list = []
PI_ITEMS: list = []


def fig(fid, figure, value, source, status, note="", domain="", check="", condition=""):
    FIGS.append({"id": fid, "figure": figure, "reproduced": value, "source": source,
                 "status": status, "note": note, "domain": domain, "check": check, "status_condition": condition})


def Ls(layers) -> str:
    return ",".join(f"L{l}" for l in layers)


def fam_series(fam: dict, layers, key="auc_kfold"):
    return {l: fam[str(l)][key] for l in layers}


def rng_of(fam: dict, layers, key="auc_kfold"):
    s = fam_series(fam, layers, key)
    lo = min(s.values()); hi = max(s.values())
    return lo, hi, [l for l in layers if s[l] == lo], [l for l in layers if s[l] == hi]


def leak_from_reads(reads: dict, mask: str):
    sess = sorted(reads["per_session"].values(), key=lambda r: r["session"])
    flips, shifts = [], []
    for r in sess:
        st, sh = r["masks"][mask]["state"], r["masks"][mask]["shadow"]
        flips.append(int(st["pick"] != sh["pick"]))
        shifts.append(abs((st["logit_a"] - st["logit_b"]) - (sh["logit_a"] - sh["logit_b"])))
    k, n = sum(flips), len(flips)
    lo, hi = clopper_pearson(k, n)
    return {"n_flips": k, "n": n, "pi_d": k / n, "cp95": [lo, hi],
            "median": statistics.median(shifts), "mean": statistics.fmean(shifts), "max": max(shifts)}


def signed_from_reads(reads: dict, mask: str, kind: str):
    """kind 'rplus': toward the label whose rounds carried r+ (M3: tag_plus's
    rounds; M4: the other's) -- recon_echo.signed_pseudo_shift; kind 'start':
    toward round 1's tag (B1x..B4x); kind 'label_a': toward the first-listed
    menu label (M5/M6/M5x/M6x label-differential); kind 'firstblock': k1 G4,
    toward the first block's label."""
    sess = sorted(reads["per_session"].values(), key=lambda r: r["session"])
    vals = []
    for r in sess:
        st, sh = r["masks"][mask]["state"], r["masks"][mask]["shadow"]
        da = (st["logit_a"] - st["logit_b"]) - (sh["logit_a"] - sh["logit_b"])
        if kind == "rplus":
            toward_tagplus = da if r["menu_a"] == r["tag_plus"] else -da
            vals.append(toward_tagplus if mask == "M3" else -toward_tagplus)
        elif kind == "start":
            vals.append(da if r["menu_a"] == r["spans"][0]["tag"] else -da)
        elif kind == "label_a":
            vals.append(da)
        elif kind == "firstblock":
            vals.append(da if r["a_is_first_block"] else -da)
        else:
            raise ValueError(kind)
    return {"mean": statistics.fmean(vals), "sd": statistics.stdev(vals),
            "n_pos": sum(1 for v in vals if v > 0), "n_neg": sum(1 for v in vals if v < 0), "n": len(vals)}


def _r(x, places: int) -> str:
    """x rounded half-up (R1's rounding) to `places` decimals, printed without the leading zero."""
    s = str(qr(x, "." + "0" * places))
    return s[1:] if s.startswith("0.") else s


def _floor(x, places: int) -> str:
    """x rounded DOWN to `places` decimals (a lower bound that holds at full precision), without the leading zero."""
    s = str(Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-places), rounding=ROUND_FLOOR))
    return s[1:] if s.startswith("0.") else s


def _json_strings(x):
    """Every string key and string value in a parsed JSON document."""
    if isinstance(x, dict):
        for k, v in x.items():
            yield str(k)
            yield from _json_strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from _json_strings(v)
    elif isinstance(x, str):
        yield x


def link3_section(w, SJ, sj_sha, sj_err, SMD, smd_sha, smd_err, la, lb, rd, RC, rd_below, rd_margin, all_nulls, n_over,
                  loc_4402, rec5760) -> dict:
    """Section 11. The link-3 sentence's values (confirmed or corrected) and a PROPOSED one-line nonlinear addition,
    for the design seat. Figures from N3c are quoted from its JSON (working tree, uncommitted), labelled as N3c's
    computed-new figures, and the ones that can be are cross-checked against the committed artifacts. Three N3c strings
    that are not in its JSON (two status tags and one advice sentence) are quoted from N3c's raw .md (working tree,
    uncommitted), with that file's sha256 and the line each came from."""
    out: dict = {"for": "the design seat; not adopted by Code", "sibling_json": SIBLING_JSON, "sibling_json_sha256": sj_sha,
                 "sibling_raw_md": SIBLING, "sibling_raw_md_sha256": smd_sha}
    loc_46 = loc(BLOCK, "(iii) Nonlinear read at the decision token")
    loc_50 = loc(BLOCK, "if (iii) finds the binding at the decision token above its permutation ceiling")
    loc_l11 = loc_range("CLAUDE.md", "11. Post-hoc analyses labeled post-hoc; they license", "pre-registrations, never verdicts")
    w(f"Block line 50 ({loc_50}): if (iii) finds the binding at the decision token above its permutation ceiling, link 3's sentence "
      "stays ('in any linear functional') and a one-line addition states the nonlinear result. N3(iii) is the sibling item N3c's. "
      "This section (a) gives the link-3 sentence's values, confirmed or corrected, and (b) proposes the one-line addition with exact "
      "figures and the post-hoc label. Both are for the design seat, which writes the note; Code adopts nothing here.")
    w()
    if SJ is None:
        w(f"N3c's JSON (`{SIBLING_JSON}`) was not read at this run ({sj_err}); no N3c figure is quoted and no line is proposed.")
        out["status"] = f"not run: sibling JSON {sj_err}"
        return out
    try:
        P2, P3, P4, PH, P3S = SJ["part_ii"], SJ["part_iii"], SJ["part_iv"], SJ["posthoc_composition"], SJ["part_iii_s"]
        mlp, rbf = P3["results"]["mlp"], P3["results"]["rbf"]
    except (KeyError, TypeError) as e:
        w(f"N3c's JSON lacks an expected field ({type(e).__name__}: {e}); no N3c figure is quoted and no line is proposed.")
        out["status"] = f"not run: sibling JSON field missing {e}"
        return out
    L15 = list(range(49, 64)); L11 = list(range(51, 62)); C1F = (("c1_label_a_M1M2", la), ("c1_label_b_M1M2", lb), ("c1_read_M1M2", rd))
    # ---- N3c's three strings that are NOT in its JSON (two status tags, one advice sentence): from its raw .md, with line numbers
    sj_strings = list(_json_strings(SJ))
    md_status, md_line = {}, {}
    advice, advice_line, nonull_line = None, None, None
    if SMD is not None:
        md_ls = SMD.splitlines()
        for key, needle in (("F1 band", "'shuffle-95 null at ~.57-.59 across layers'"), ("≈ .58", "'below the shuffled-label 95th percentile of ~.58'")):
            hit = [(i + 1, ln) for i, ln in enumerate(md_ls) if needle in ln]
            m_ = re.search(r"\[status: ([^\]]*)\]", hit[0][1]) if hit else None
            md_status[key] = m_.group(1) if m_ else "not found in N3c's raw"
            md_line[key] = hit[0][0] if m_ else None
        hit = [(i + 1, ln) for i, ln in enumerate(md_ls) if "safer quotation than the MLP peak" in ln]
        m_ = re.search(r"(For the note's nonlinear line,[^\n]*?than the MLP peak\.)", hit[0][1]) if hit else None
        if m_:
            advice, advice_line = m_.group(1), hit[0][0]
        hit = [i + 1 for i, ln in enumerate(md_ls) if "no null (point estimates only)" in ln and "Identity, asserted" in ln]
        nonull_line = hit[0] if hit else None
    else:
        md_status = {"F1 band": f"N3c raw not read ({smd_err})", "≈ .58": f"N3c raw not read ({smd_err})"}
    md_strings = ([md_status["F1 band"]] if md_line.get("F1 band") else []) + ([md_status["≈ .58"]] if md_line.get("≈ .58") else []) \
        + ([advice] if advice else [])
    n_in_json = sum(1 for s in md_strings if any(s in js for js in sj_strings))
    out["n3c_raw_sha256"] = smd_sha
    out["n3c_status_quoted"] = md_status
    out["n3c_raw_lines"] = {"F1 band status": md_line.get("F1 band"), "≈ .58 status": md_line.get("≈ .58"), "advice": advice_line,
                            "subgroup reads 'no null (point estimates only)'": nonull_line}
    out["n3c_advice_quoted"] = advice
    out["n3c_raw_strings_found_in_json"] = [n_in_json, len(md_strings), len(sj_strings)]
    w(f"**Provenance.** `{SIBLING_JSON}` read from the working tree (uncommitted at {PIN}), sha256 `{sj_sha}`; its own header: "
      f"script `{SJ.get('script')}` sha256 `{str(SJ.get('script_sha256'))[:16]}...`, stamp '{SJ.get('code_stamp')}', HEAD at its run "
      f"`{str(SJ.get('head_at_run'))[:7]}`, pin `{str(SJ.get('pin'))[:7]}`. Every N3c figure below is N3c's computation on the local "
      "Stage C residual arrays (status in N3c: computed-new, except where N3c reproduces a stored value), quoted here, not recomputed; "
      "the cross-checks in (a0) are this script's, against the committed stageC_analysis.json and stageC_reads.json.")
    if SMD is not None:
        w(f"- N3c's raw `{SIBLING}` read from the working tree (uncommitted at {PIN}), sha256 `{smd_sha}`. Three strings in this "
          "section come from it, not from the JSON: N3c's status tag on F1's band (its line "
          f"{md_line.get('F1 band') or 'not found'}) and on '≈ .58' (its line {md_line.get('≈ .58') or 'not found'}), both quoted in (a), "
          f"and N3c's advice on which nonlinear figure to quote (its line {advice_line or 'not found'}), quoted in (b). A search of every "
          f"string key and value of N3c's JSON ({len(sj_strings):,} strings) finds {n_in_json} of these {len(md_strings)}. Like the "
          "JSON, the .md may be rewritten by N3c's own round; the strings quoted are those of the .md whose sha256 is printed here.")
    else:
        w(f"- N3c's raw `{SIBLING}` was not read at this run ({smd_err}); N3c's status tags and its advice sentence, which are not in "
          "its JSON, are not quoted.")
    _sp = os.path.join(REPO, str(SJ.get("script")))
    _cur = sha256(open(_sp, "rb").read()) if os.path.isfile(_sp) else None
    w(f"- N3c's script on disk at this run: sha256 `{(_cur or 'absent')[:16]}...`, "
      + ("the same as the one that wrote the JSON." if _cur == SJ.get("script_sha256") else
         "DIFFERENT from the one that wrote the JSON (N3c's own round may be in progress); the figures quoted here are those of the "
         "JSON whose sha256 is printed above. If N3c's raw is regenerated later, re-running this script refreshes section 11 "
         "(everything else in this raw is unchanged by it)."))
    w()
    out["n3c_script_sha256_on_disk_at_run"] = _cur
    # ---- (a0) cross-checks of N3c against the committed artifacts
    n_eq_null, n_eq_auc, n_cells, bad = 0, 0, 0, []
    for fname, fam in C1F:
        for l in L_ALL:
            s_ = P2["families"][fname][str(l)]
            n_cells += 1
            eq_n = s_["null200_p95"] == fam[str(l)]["shuffle95"]
            eq_a = s_["auc_kfold"] == fam[str(l)]["auc_kfold"]
            n_eq_null += eq_n; n_eq_auc += eq_a
            if not (eq_n and eq_a):
                bad.append((fname, l))
    sess = sorted(RC["per_session"].values(), key=lambda r: r["session"])
    sp_ok = all((r["spans"][0]["tag"] == r["tag_plus"]) == r["start_plus"] for r in sess)
    ident = sum(1 for r in sess if (r["menu_a"] == r["tag_plus"]) == ((r["menu_a"] == r["spans"][0]["tag"]) == r["start_plus"]))
    # M2 row: target = not [label_a is tag_plus]; round 1 carries + under M2 iff not start_plus
    ident2 = sum(1 for r in sess if (r["menu_a"] != r["tag_plus"]) == ((r["menu_a"] == r["spans"][0]["tag"]) == (not r["start_plus"])))
    n_r1 = sum(1 for r in sess if r["menu_a"] == r["spans"][0]["tag"])
    w("**(a0) Cross-checks of N3c's JSON against the committed artifacts (computed here).**")
    w()
    w(f"- N3c's stored-draw 95th (`part_ii.families.*.null200_p95`) equals the committed `stageC_analysis.json` shuffle95 at "
      f"{n_eq_null}/{n_cells} (family, layer) cells, and its linear 10-fold AUC equals the committed auc_kfold at {n_eq_auc}/{n_cells} "
      f"(the three C1 M1vM2 families x 18 layers; exact float equality){'; differing: ' + str(bad[:10]) if bad else ''}. [reproduced]")
    w(f"- The post-hoc identity, from committed `stageC_reads.json` (102 sessions): `start_plus` equals [round 1's tag is tag_plus] in "
      f"every session: {sp_ok}; the read target of the M1 row, [label_a is tag_plus], equals [label_a is the round-1 tag] XNOR "
      f"[round 1 carried + under M1] in {ident}/{len(sess)} sessions. With two labels this holds by construction (it is a truth-table "
      f"identity, not a finding); label_a is the round-1 tag in {n_r1} sessions and not in {len(sess) - n_r1} (N3c: "
      f"{PH.get('n_label_a_is_round1_tag')}). On the M2 row (target = [label_a is not tag_plus]; round 1 carries + under M2 iff not "
      f"start_plus) the same identity holds in {ident2}/{len(sess)}. [computed-new; POST-HOC as N3c labels it]")
    w()
    out["cross_checks"] = {"null200_p95_equal": [n_eq_null, n_cells], "auc_kfold_equal": [n_eq_auc, n_cells], "differing": bad,
                           "start_plus_consistent": sp_ok, "identity_sessions": [ident, len(sess)], "identity_sessions_M2_row": [ident2, len(sess)], "label_a_is_round1_tag": n_r1,
                           "n3c_label_a_is_round1_tag": PH.get("n_label_a_is_round1_tag")}
    # ---- (a) the sentence, value by value
    rii = P2["summary_L51_61"]["c1_read_M1M2"]
    p4 = P4["summary"]
    SUBK = ("label_a_is_round1_tag", "label_a_is_not_round1_tag")
    sub = [PH["per_layer"][str(l)][k]["auc_kfold"] for l in L11 for k in SUBK]
    # the same subgroup reads over L49-L63 (the nonlinear clause's range), to show why the subgroup clause names its own domain
    sub15 = {l: tuple(PH["per_layer"][str(l)][k]["auc_kfold"] for k in SUBK) for l in L15}
    sub15_all = [v for t in sub15.values() for v in t]
    sub_out = sorted(l for l in L15 if l not in L11)
    # does N3c store any null for the post-hoc reads? (field names of every post-hoc cell)
    sub_keys = sorted({kk for l in L15 for k in SUBK + ("first_round_sign_all",) for kk in PH["per_layer"][str(l)][k]})
    sub_nonull = not any(t in kk for kk in sub_keys for t in ("null", "p95", "perm", "shuffle"))
    frs = [PH["per_layer"][str(l)]["first_round_sign_all"]["auc_kfold"] for l in L11]
    la_51 = [la[str(l)]["auc_kfold"] for l in range(51, 64)]
    lb_51 = [lb[str(l)]["auc_kfold"] for l in range(51, 64)]
    lb_5161 = [lb[str(l)]["auc_kfold"] for l in L11]
    rd_49 = [rd[str(l)]["auc_kfold"] for l in L15]
    rdn_49 = [rd[str(l)]["shuffle95"] for l in L15]
    w(f"**(a) The link-3 sentence (block line 44's quotation; the note itself is not on this machine), value by value.** Linear "
      "figures: the stored C1 families (stageC_analysis.json; standardized L2 logistic regression, M1 v M2 rows, 102 sessions, grouped "
      "10-fold, 200 shuffles), reproduced in sections 3-4; N3c's 1,000-draw null and layer sweep quoted beside.")
    w()
    rows = [
        ["'≈ 1.0 at the first label'", f"label_a's token: {min(la_51):.4f}-{max(la_51):.4f} at L51-L63 (L49/L50 {la['49']['auc_kfold']:.4f}/"
         f"{la['50']['auc_kfold']:.4f}); N3c's 1,000-draw 95th at L51-L61 {P2['summary_L51_61']['c1_label_a_M1M2']['p95_min']:.4f}-"
         f"{P2['summary_L51_61']['c1_label_a_M1M2']['p95_max']:.4f}, label_a above it at "
         f"{P2['summary_L51_61']['c1_label_a_M1M2']['n_layers_above_p95']}/{P2['summary_L51_61']['c1_label_a_M1M2']['n_layers']} layers, "
         f"one-sided permutation p {P2['summary_L51_61']['c1_label_a_M1M2']['p_min']:.6f}-{P2['summary_L51_61']['c1_label_a_M1M2']['p_max']:.6f} "
         f"(1/1001 = {1 / 1001:.6f}, the smallest attainable)",
         "confirmed from L51 (ib-2); needs 'from L51' if the sentence's elided text does not carry it"],
        ["'.81–.96 at the second'", f"label_b's token: {min(lb_51):.4f}-{max(lb_51):.4f} at L51-L63; {min(lb_5161):.4f}-{max(lb_5161):.4f} "
         f"at L51-L61 (= {_r(min(lb_5161), 2)}-{_r(max(lb_5161), 2)}); L49/L50 {lb['49']['auc_kfold']:.4f}/{lb['50']['auc_kfold']:.4f}",
         "confirmed on L51-L63 (ib-3); on L51-L61 it reads '.82–.96'; needs 'from L51' as above"],
        ["(the choice read) '.50–.55'", f"read position: {min(rd_49):.4f}-{max(rd_49):.4f} at L49-L63; N3c (iv) L49-L61 "
         f"{p4['auc_min_L49_61']:.4f}-{p4['auc_max_L49_61']:.4f}; L44-L48 (including N3c's new L45-L47) exactly "
         f"{' / '.join(str(v) for v in p4['auc_values_le48'])} by construction; sweep layers above their own 95th: "
         f"{p4['layers_above_p95'] or 'none'}", "confirmed (ib-4; N3c (iv))"],
        ["'below the shuffled-label 95th percentile of ≈ .58'", f"read AUC below its stored 200-draw 95th at every one of 18 layers: "
         f"{rd_below} (smallest gap above L48 {rd_margin:.4f}); that 95th is {min(rdn_49):.4f}-{max(rdn_49):.4f} over L49-L63 (mean "
         f"{statistics.fmean(rdn_49):.4f}); N3c's 1,000-draw 95th at L51-L61 {rii['p95_min']:.4f}-{rii['p95_max']:.4f}, read above it at "
         f"{rii['n_layers_above_p95']}/{rii['n_layers']} layers, one-sided permutation p {rii['p_min']:.4f}-{rii['p_max']:.4f}",
         f"confirmed as a midpoint (ib-5: mean and median round to .58); the 95th is per layer, so an exact form is 'below its per-layer "
         f"shuffled-label 95th percentile ({_r(min(rdn_49), 3)}–{_r(max(rdn_49), 3)}, 200 shuffles; {_r(rii['p95_min'], 3)}–"
         f"{_r(rii['p95_max'], 3)} at 1,000, L51–L61)'. N3c's status (its raw .md, line {md_line.get('≈ .58') or 'n/a'}; not in its "
         f"JSON): {md_status.get('≈ .58')}"],
        ["F1's band '≈ .57–.59'", f"the stored 200-draw 95th across the three C1 families: {min(all_nulls):.4f}-{max(all_nulls):.4f} over "
         f"all 18 layers and {min(f[str(l)]['shuffle95'] for _, f in C1F for l in L15):.4f}-{max(f[str(l)]['shuffle95'] for _, f in C1F for l in L15):.4f} "
         f"over L49-L63; outside .57-.59 at two decimals only at " + ", ".join(f"{nm} L{l} {v}" for nm, l, v in n_over),
         f"corrected to {rec5760}, conditional on F1's series (ib-1). N3c's status (its raw .md, line {md_line.get('F1 band') or 'n/a'}; "
         f"not in its JSON): {md_status.get('F1 band')}"],
        ["'in any linear functional' (block line 50)", f"what was tested is ONE linear estimator, the stored probe: (ii) read AUC "
         f"{rii['auc_min']:.4f}-{rii['auc_max']:.4f} at L51-L61, above its own 1,000-draw 95th at {rii['n_layers_above_p95']}/11; (iv) no "
         f"layer of L44-L61 above its own 95th. POST-HOC (N3c): the same estimator reads the first-round sign at {min(frs):.4f}-{max(frs):.4f} "
         f"and the target within each menu-order subgroup at {min(sub):.4f}-{max(sub):.4f} (L51-L61; "
         + ("point estimates, no null: N3c's JSON stores only " + ", ".join(sub_keys) + " per post-hoc cell" if sub_nonull
            else "N3c's JSON stores a null field per post-hoc cell: " + ", ".join(sub_keys))
         + (f"; N3c's raw .md, line {nonull_line}: 'no null (point estimates only)'" if nonull_line else "") + ")",
         "stays, per block line 50. Flag for the seat: the wording is wider than what was tested, and the post-hoc reads show the "
         "target is linearly read within each menu order (two functionals), not by one functional pooled"],
    ]
    w.table(["sentence part", "values (exact)", "confirmed or corrected"], rows)
    out["sentence"] = [dict(zip(("part", "values", "verdict"), r_)) for r_ in rows]
    # ---- (b) the nonlinear result and the proposed line
    def col(cls, pos, key):
        return {l: P3["results"][cls][pos][str(l)][key] for l in L15}
    m_auc, m_p95, m_max, m_p = col("mlp", "read", "auc"), col("mlp", "read", "null_p95"), col("mlp", "read", "null_max"), col("mlp", "read", "perm_p")
    r_auc, r_p95, r_max, r_p = col("rbf", "read", "auc"), col("rbf", "read", "null_p95"), col("rbf", "read", "null_max"), col("rbf", "read", "perm_p")
    m_n, r_n = mlp["read"]["51"]["n_null"], rbf["read"]["51"]["n_null"]
    m_ab = [l for l in L15 if m_auc[l] > m_p95[l]]; r_ab = [l for l in L15 if r_auc[l] > r_p95[l]]
    m_abx = [l for l in L15 if m_auc[l] > m_max[l]]; r_abx = [l for l in L15 if r_auc[l] > r_max[l]]
    pc_m = min(mlp["label_a"][str(l)]["auc"] for l in L11); pc_r = min(rbf["label_a"][str(l)]["auc"] for l in L11)
    w(f"**(b) The nonlinear result (N3c, N3(iii); block line 46, {loc_46}).** Read position, same rows (M1 v M2, 204), target "
      f"(label_a's pole under the mask) and grouped 10-fold folds as the linear family; MLP = one hidden layer of "
      f"{P3['mlp_config'].get('H')} ReLU units, early stopping on an inner 20% session split (patience {P3['mlp_config'].get('patience')}, "
      f"up to {P3['mlp_config'].get('max_epochs')} epochs), null {m_n} shuffles; RBF = kernel ridge classifier, median-heuristic gamma, "
      f"lambda by inner grouped 5-fold CV on {P3['rbf_config'].get('lambdas')}, null {r_n} shuffles; shuffles permute the target across "
      "all rows on the same folds; p = (1 + #{null >= observed}) / (1 + n), one-sided permutation test. Per layer (AUC / null 95th / "
      "null max / p):")
    w()
    w.table(["layer", "MLP", "RBF"], [[l, f"{m_auc[l]:.4f} / {m_p95[l]:.4f} / {m_max[l]:.4f} / {m_p[l]:.4f}",
                                       f"{r_auc[l]:.4f} / {r_p95[l]:.4f} / {r_max[l]:.4f} / {r_p[l]:.4f}"] for l in L15])
    w(f"- MLP {min(m_auc.values()):.4f}-{max(m_auc.values()):.4f} over L49-L63, above its own 95th at {len(m_ab)}/15 layers; RBF "
      f"{min(r_auc.values()):.4f}-{max(r_auc.values()):.4f}, above at {len(r_ab)}/15. Positive control at label_a's token (N3c's bar "
      f"{P3.get('positive_control_bar')} at every layer L51-L61): MLP min {pc_m:.4f}, RBF min {pc_r:.4f} "
      f"(N3c: {'PASS' if P3['positive_control'].get('mlp_pass') and P3['positive_control'].get('rbf_pass') else 'not both PASS'}).")
    w(f"- 'Ceiling': block line 50 says 'permutation ceiling'; line 46 asks for 'its permutation 95th percentile', which is the reading "
      f"above. Against each null's MAXIMUM instead: MLP above at {Ls(m_abx) or 'none'}; RBF above at {Ls(r_abx) or 'none'} "
      f"(so neither at L49{', and RBF not at L50' if 50 not in r_abx else ''}).")
    w(f"- Robustness (N3c, POST-HOC (iii-s)): the spec MLP over 5 seed pairs reads L51 "
      f"{P3S['summary']['mlp_seed_range_per_layer']['51'][0]:.4f}-{P3S['summary']['mlp_seed_range_per_layer']['51'][1]:.4f}, L56 "
      f"{P3S['summary']['mlp_seed_range_per_layer']['56'][0]:.4f}-{P3S['summary']['mlp_seed_range_per_layer']['56'][1]:.4f}, L61 "
      f"{P3S['summary']['mlp_seed_range_per_layer']['61'][0]:.4f}-{P3S['summary']['mlp_seed_range_per_layer']['61'][1]:.4f}; an Adam-trained "
      f"MLP {', '.join(f'L{k} {v:.4f}' for k, v in P3S['summary']['adam_auc'].items())} (above its own 50-draw 95th at "
      f"{P3S['summary']['adam_layers_above_p95']}); the RBF chose the grid's lowest lambda in "
      f"{P3['summary']['rbf_read_obs_fits_at_grid_lower_edge']['n']}/{P3['summary']['rbf_read_obs_fits_at_grid_lower_edge']['of']} fits, "
      f"and on an extended grid reads {P3S['summary']['rbf_x_auc_range'][0]:.4f}-{P3S['summary']['rbf_x_auc_range'][1]:.4f} "
      f"(above its 95th at {len(P3S['summary']['rbf_x_layers_above_p95'])}/15; {P3S['summary']['rbf_x_obs_fits_at_new_edge']['n']}/"
      f"{P3S['summary']['rbf_x_obs_fits_at_new_edge']['of']} fits at the new edge); against a per-session label-flip null the RBF is above "
      f"its 95th at {len(P3S['summary']['rbf_flip_layers_above_p95'])}/15 and the MLP at {len(P3S['summary']['mlp_flip_layers_above_p95'])}/15. "
      "So the exceedance held in every check; the MLP's level depends on its training specification, and the RBF's is grid-limited.")
    w("- Multiplicity (descriptive): 15 correlated layers per classifier, uncorrected per-layer tests.")
    w()
    # The drafts lead with the exceedance (N3c's advice, quoted below) and tag each AUC level with its caveat: the MLP's level is
    # one training specification's (it moves with seed and optimizer, the robustness line above); the RBF's is grid-limited when
    # its lambda sat at the grid's lower edge.
    _edge = P3["summary"]["rbf_read_obs_fits_at_grid_lower_edge"]
    rbf_tag = "grid-limited" if _edge["n"] > 0 else "lambda inside its grid"
    _ex4 = ("each read it above their own shuffled-label 95th percentile at all 15 layers L49–L63" if len(m_ab) == len(r_ab) == 15 else
            f"read it above their own shuffled-label 95th percentile at {len(m_ab)} and {len(r_ab)} of 15 layers L49–L63")
    _ex2 = ("each read it above their shuffled-label 95th at every layer L49–L63" if len(m_ab) == len(r_ab) == 15 else
            f"read it above their shuffled-label 95th at {len(m_ab)} and {len(r_ab)} of 15 layers L49–L63")
    _sub_lbl = "point estimates, no null" if sub_nonull else "with N3c's stored null"
    prop4 = (f"A nonlinear read does recover the binding at the decision token: a one-hidden-layer MLP and an RBF kernel classifier "
             f"{_ex4} ({m_n} and {r_n:,} shuffles; same rows, target and grouped 10-fold CV as the linear probe; 102 sessions), at AUC "
             f"{_r(min(m_auc.values()), 4)}–{_r(max(m_auc.values()), 4)} for the MLP (one training specification) and "
             f"{_r(min(r_auc.values()), 4)}–{_r(max(r_auc.values()), 4)} for the RBF ({rbf_tag}), while both read label_a's token at "
             f"≥ {_floor(min(pc_m, pc_r), 4)} (L51–L61); post hoc, the target is the first-round sign XNOR whether label_a is the round-1 "
             f"tag, which the same linear probe reads within each menu order ({_r(min(sub), 4)}–{_r(max(sub), 4)}, L51–L61; {_sub_lbl}) "
             "but not pooled.")
    prop2 = (f"A nonlinear read does recover it at the decision token: an MLP and an RBF kernel classifier {_ex2} ("
             f"MLP AUC {_r(min(m_auc.values()), 2)}–{_r(max(m_auc.values()), 2)}, one training specification; RBF "
             f"{_r(min(r_auc.values()), 2)}–{_r(max(r_auc.values()), 2)}, {rbf_tag}); post hoc, the target is the first-round sign "
             f"XNOR menu order relative to round 1, linearly readable within each menu order ({_r(min(sub), 3)}–{_r(max(sub), 3)}, "
             f"L51–L61; {_sub_lbl}) but not pooled.")
    # R1 self-check of the two drafts against the values they quote, each on the domain the draft names for it
    ck2 = [chk_range(list(m_auc.values()), _r(min(m_auc.values()), 2), _r(max(m_auc.values()), 2)),
           chk_range(list(r_auc.values()), _r(min(r_auc.values()), 2), _r(max(r_auc.values()), 2)),
           chk_range(sub, _r(min(sub), 3), _r(max(sub), 3))]
    ck_sub15 = chk_range(sub15_all, _r(min(sub), 3), _r(max(sub), 3))
    w("**Proposed one-line addition (Code's draft for the design seat; NOT adopted; the seat writes the line).** Exact form:")
    w()
    w(f"> {prop4}")
    w()
    w(f"Short form (AUCs at two decimals, the within-subgroup range at three, since {_r(max(sub), 4)} would print as {_r(max(sub), 2)}):")
    w()
    w(f"> {prop2}")
    w()
    w(f"- Labels the line needs if used: the nonlinear figures are N3c's computed-new figures (N3(iii)), not pre-registered, and they "
      "change no label (block line 46: 'neither changes a label'); the XNOR clause is POST-HOC, descriptive, and under ledger 11 "
      f"({loc_l11}: post-hoc analyses 'license pre-registrations, never verdicts') it licenses at most a pre-registered follow-up. "
      + (f"N3c's own advice (its raw .md, line {advice_line}; not in its JSON): '{advice}' " if advice else
         "N3c's advice sentence on which nonlinear figure to quote was not found in its raw .md at this run. ")
      + "Both forms follow that advice: they lead with the exceedance, and each AUC level carries its caveat in parentheses (the "
      f"MLP's is one training specification's, which moves with seed and optimizer per the robustness line above; the RBF's is "
      f"{rbf_tag}, its lambda at the grid's lower edge in {_edge['n']}/{_edge['of']} fits).")
    w(f"- R1 check of the short form against the values it quotes, each on the domain the form names for it: MLP, L49-L63, "
      f"{ck2[0][1]} (the MLP minimum is {min(m_auc.values()):.6f}: {_r(min(m_auc.values()), 4)} at four decimals, "
      f"{_r(min(m_auc.values()), 2)} at two); RBF, L49-L63, {ck2[1][1]}; within-subgroup linear, L51-L61, {ck2[2][1]}. 'At every "
      f"layer' = {len(m_ab)}/15 and {len(r_ab)}/15 above the 95th. The subgroup clause names L51-L61 because over L49-L63 the same "
      f"reads are {min(sub15_all):.4f}-{max(sub15_all):.4f} ({ck_sub15[1]}; outside L51-L61, label_a the round-1 tag / not: "
      + ", ".join(f"L{l} {sub15[l][0]:.4f}/{sub15[l][1]:.4f}" for l in sub_out)
      + f"). Both forms label the subgroup reads '{_sub_lbl}'.")
    w(f"- Status: the line is a draft, not a figure of this raw; its numbers are N3c's (quoted from N3c's JSON, sha256 {sj_sha[:16]}...), "
      "the positive control's and the subgroup reads likewise; the identity is checked here from committed stageC_reads.json (a0).")
    out["nonlinear"] = {"mlp_auc": m_auc, "mlp_null_p95": m_p95, "mlp_null_max": m_max, "mlp_perm_p": m_p, "mlp_n_null": m_n,
                        "rbf_auc": r_auc, "rbf_null_p95": r_p95, "rbf_null_max": r_max, "rbf_perm_p": r_p, "rbf_n_null": r_n,
                        "above_p95": {"mlp": m_ab, "rbf": r_ab}, "above_null_max": {"mlp": m_abx, "rbf": r_abx},
                        "positive_control_min_L51_61": {"mlp": pc_m, "rbf": pc_r},
                        "posthoc_within_subgroup_L51_61": [min(sub), max(sub)], "posthoc_first_round_sign_L51_61": [min(frs), max(frs)],
                        "posthoc_within_subgroup_L49_63": [min(sub15_all), max(sub15_all)],
                        "posthoc_within_subgroup_outside_L51_61": {str(l): list(sub15[l]) for l in sub_out},
                        "posthoc_cell_fields": sub_keys, "posthoc_has_null": not sub_nonull,
                        "status": "computed-new in N3c (quoted, not recomputed here)"}
    out["proposed_line"] = {"exact": prop4, "short": prop2,
                            "short_form_r1_checks": {"mlp_L49_L63": ck2[0][1], "rbf_L49_L63": ck2[1][1], "within_subgroup_L51_L61": ck2[2][1],
                                                     "within_subgroup_over_L49_L63_for_comparison": ck_sub15[1]},
                            "leads_with": "the exceedance (N3c's advice)", "mlp_level_tag": "one training specification",
                            "rbf_level_tag": rbf_tag, "subgroup_tag": _sub_lbl,
                            "label": "POST-HOC clause (ledger 11); draft for the design seat; not adopted"}
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=DEF_OUT)
    ap.add_argument("--json-out", default=DEF_JSON)
    args = ap.parse_args()
    out_md = args.out if os.path.isabs(args.out) else os.path.join(REPO, args.out)
    out_js = args.json_out if os.path.isabs(args.json_out) else os.path.join(REPO, args.json_out)

    w = Out()
    J: dict = {"item": "N3 (i), (i-b), (v)", "pin": PIN}

    # ------------------------------------------------------------- header
    stamp = subprocess.run(["date", "-u"], capture_output=True, text=True, check=True).stdout.strip()
    head = git("rev-parse", "HEAD").decode().strip()
    pin_full = git("rev-parse", PIN).decode().strip()
    block_bytes = open(os.path.join(REPO, BLOCK), "rb").read()
    block_sha = sha256(block_bytes)
    block_pin_sha = sha256(blob(BLOCK))
    script_bytes = open(os.path.abspath(__file__), "rb").read()
    cmd = shlex.join([sys.executable] + sys.orig_argv[1:]) if hasattr(sys, "orig_argv") else shlex.join([sys.executable] + sys.argv)
    w("# AUDIT-note-release v1.2 -- N3 (i), (i-b), (v): echo-probe figures from committed JSON")
    w()
    w(f"- Code stamp: {stamp} (`date -u`, run inside the script)")
    w(f"- HEAD at run: {head}")
    w(f"- Pinned commit for every input and locator: {PIN} = {pin_full}")
    w(f"- Block: `{BLOCK}`, sha256 `{block_sha}` (working tree); at {PIN}: `{block_pin_sha}`; "
      f"routed `8cd8a9ac...3841`: {'MATCH' if block_sha == BLOCK_SHA_ROUTED == block_pin_sha else 'MISMATCH'}; "
      f"{len(block_bytes.decode('utf-8').splitlines())} lines")
    w(f"- Script: `{SCRIPT_REL}`, sha256 `{sha256(script_bytes)}`")
    w(f"- Interpreter: {sys.executable} (Python {sys.version.split()[0]}); stdlib only (argparse, decimal, hashlib, json, math, os, re, "
      f"shlex, statistics, subprocess, sys); numpy not imported; nothing imported from the repository")
    w(f"- Command line: `{cmd}`")
    shown = lambda p: os.path.relpath(p, REPO) if os.path.abspath(p).startswith(REPO + os.sep) else os.path.abspath(p)
    w(f"- Outputs: `{shown(out_md)}`, `{shown(out_js)}`")
    sib_present = os.path.exists(os.path.join(REPO, SIBLING))
    # the sibling's JSON (uncommitted; working tree): read once, hashed, parsed; used by section 11 only
    sib_js_path = os.path.join(REPO, SIBLING_JSON)
    SJ, sj_sha, sj_err = None, None, None
    if os.path.exists(sib_js_path):
        try:
            _sjb = open(sib_js_path, "rb").read()
            sj_sha = sha256(_sjb)
            SJ = json.loads(_sjb.decode("utf-8"))
        except Exception as e:     # absent mid-write, truncated, etc.: section 11 says so
            SJ, sj_err = None, f"{type(e).__name__}: {e}"
    else:
        sj_err = "absent"
    # the sibling's raw .md (uncommitted; working tree): read once, hashed; section 11 takes from it only the three strings
    # that are not in the JSON (N3c's two status tags and its advice on which nonlinear figure to quote)
    sib_md_path = os.path.join(REPO, SIBLING)
    SMD, smd_sha, smd_err = None, None, None
    if sib_present:
        try:
            _smb = open(sib_md_path, "rb").read()
            smd_sha = sha256(_smb)
            SMD = _smb.decode("utf-8")
        except Exception as e:
            SMD, smd_err = None, f"{type(e).__name__}: {e}"
    else:
        smd_err = "absent"
    w("- Run-dependent lines: the stamp; HEAD / command line / outputs if those differ between runs; the sibling-raw "
      "presence test (the Scope line, section 10 item 6, section 12 round-1 finding 3); section 11, whose quoted figures "
      "come from the sibling's uncommitted JSON as it stood at this run, and whose three N3c strings not in that JSON (two status "
      "tags and one advice sentence) come from the sibling's uncommitted raw .md as it stood at this run (both sha256s are printed "
      "there and in the Scope line); and the section 12 rows that quote section 11 (round 2's C-a and C-b; round 4's R4-1, R4-2 "
      "and R4-5). Everything else is a deterministic function of the pinned blobs (no random draw anywhere).")
    w(f"- Scope: N3 parts (i), (i-b), (v) from committed JSON only (sections 0-10). Parts (ii)-(iv) (refits on the local "
      f"`data/echo/*.npz` arrays) are the sibling item N3c's, raw `{SIBLING}` (+ `.json`); that raw "
      f"{'is present' if sib_present else 'is NOT present'} at this run. Sections 0-10 do not read it. Section 11 (the link-3 "
      f"sentence and a proposed nonlinear line, for the design seat; not adopted) reads N3c's JSON "
      f"({'read, sha256 ' + sj_sha[:16] + '...' if SJ is not None else 'NOT read: ' + str(sj_err)}) and, for N3c's two status "
      f"tags and its advice sentence only, N3c's raw .md "
      f"({'read, sha256 ' + smd_sha[:16] + '...' if SMD is not None else 'NOT read: ' + str(smd_err)}).")
    w()
    J["header"] = {"stamp": stamp, "head": head, "pin": pin_full, "block_sha256": block_sha,
                   "block_sha256_at_pin": block_pin_sha, "block_routed_match": block_sha == BLOCK_SHA_ROUTED == block_pin_sha,
                   "script_sha256": sha256(script_bytes), "interpreter": sys.executable,
                   "python": sys.version.split()[0], "command": cmd, "sibling_raw_for_ii_iv": SIBLING,
                   "sibling_raw_present_at_run": sib_present, "sibling_json": SIBLING_JSON,
                   "sibling_json_sha256_at_run": sj_sha, "sibling_json_read_error": sj_err,
                   "sibling_json_used_by": "section 11 only (working-tree file, uncommitted at the pin)",
                   "sibling_raw_md_sha256_at_run": smd_sha, "sibling_raw_md_read_error": smd_err,
                   "sibling_raw_md_used_by": "section 11 only, for three strings not in the sibling JSON (N3c's status tags on F1's "
                                             "band and on '~.58', and its advice sentence); working-tree file, uncommitted at the pin"}

    # ------------------------------------------------------------- inputs
    w("## 0. Inputs (read with `git show " + PIN + ":<path>`)")
    w()
    rows = []
    J["inputs"] = {}
    for p in DATA_INPUTS + TEXT_INPUTS:
        b = blob(p)
        wt_path = os.path.join(REPO, p)
        wt = sha256(open(wt_path, "rb").read()) if os.path.exists(wt_path) else None
        same = (wt == sha256(b))
        rows.append([f"`{p}`", f"`{sha256(b)[:16]}`", "identical" if same else ("ABSENT" if wt is None else "DIFFERS (pinned blob used)")])
        J["inputs"][p] = {"blob_sha256": sha256(b), "working_tree_identical": same}
    w.table(["input", f"sha256 at {PIN} (16)", "working tree"], rows)

    A = jload("data/echo/stageA_analysis.json")
    Aph = jload("data/echo/stageA_posthoc_lastround.json")
    Aph2 = jload("data/echo/stageA_posthoc2_labelpole.json")
    B = jload("data/echo/stageB_analysis.json")
    Bs = jload("data/echo/stageB_analysis_samefolds.json")
    C = jload("data/echo/stageC_analysis.json")
    RA = jload("data/echo/stageA_reads.json")
    RB = jload("data/echo/stageB_reads.json")
    RC = jload("data/echo/stageC_reads.json")
    TM = jload("data/echo/timing.json")
    K = jload("data/k/k1_analysis.json")
    KR = jload("data/k/k1_reads.json")
    e2a = [json.loads(l) for l in blob("data/e2a/sessions.jsonl").decode("utf-8").splitlines() if l.strip()]
    rawC = blob("results/raw/2026-09-06_recon_echo_stageC_analysis.txt").decode("utf-8")

    RE = "RESULTS.md"
    RC_HDR = "**RECON — ECHO CHANNEL (k-candidate), STAGE C."
    RB_HDR = "**RECON — ECHO CHANNEL (k-candidate), STAGE B."
    RA_HDR = "**RECON — ECHO CHANNEL (k-candidate). Apparatus characterization"
    K1_HDR = "**PROPOSAL-k STAGE 1 — CHANNEL STUDY."
    K11_HDR = "**PROPOSAL-k v1.1 COMMITTED"
    # the record's own figure check of the recon figures (the PROPOSAL-k v1.1 COMMITTED entry, Appendix B check)
    FC = {
        "B1": loc_range(RE, '(B1) ".94–.995 above L48"', "L49 reads .695, the range holds L50–L63", after=K11_HDR),
        "B4_flips": loc_range(RE, "(B4) 0–3/102 over every family", "families' flips (0–1/102) live in the artifacts", after=K11_HDR),
        "B4_median": loc_range(RE, 'tables; "median .04–.10" is the record', "realised medians run .033–.103 (R3 .0327)", after=K11_HDR),
        "B4_pseudo": loc_range(RE, "the pseudo-shift ±.02–.03 is the MIXED block masks", "read +.008/−.002, a scoping", after=K11_HDR),
        "B4_max": loc_range(RE, "per-family max |Δ| .11–.20, the largest M5x", ".2012 and M5 .1913", after=K11_HDR),
        # the clause the max sits in, from its subject: 'not the R / M++ arms the memo names for the gate (0–1/102 there, per-family
        # max |Δ| .11–.20, the largest M5x .2012 and M5 .1913)'
        "B4_RMpp": loc_range(RE, "not the R / M++ arms the memo names for", ".2012 and M5 .1913", after=K11_HDR),
    }
    RX = "scripts/recon_echo.py"
    PRB = "valence_core/echo/probe.py"
    KA = "valence_core/k/analysis.py"
    PK = "PROPOSAL-k-echo-channel.md"

    # ---------------------------------------------------------- definitions
    w("## 1. Definitions, from the code and artifacts of record")
    w()
    cfg = RC["config_of_record"]
    valid_reward = sorted(r["session"] for r in e2a if r["arm"] == "reward" and not r["excluded"])
    arm_counts = {}
    for r in e2a:
        key = f"{r['arm']}{' (excluded)' if r['excluded'] else ''}"
        arm_counts[key] = arm_counts.get(key, 0) + 1
    roster_ok = (RB["sessions"] == valid_reward == RC["sessions"])
    w(f"- **Sessions.** Stages B and C read the {len(valid_reward)} valid e2a reward-arm sessions "
      f"(`valid_reward`, {loc(RX, 'def valid_reward(rows):')}); the roster in both reads artifacts equals the valid reward "
      f"sessions of `data/e2a/sessions.jsonl`: {roster_ok}. Stage A read 24 of them ({RA['roster']}). The e2a archive's own arms: "
      + ", ".join(f"{k} {v}" for k, v in sorted(arm_counts.items())) + ". The recon read no sham, random1 or random2 session.")
    w(f"- **Read position.** The first free choice: the transcript prefix through the first `Config choice (one word):`; "
      f"the read position is the prefix's last token (`n_tok - 1`; capture positions `(n_tok - 1, label_a, label_b)`, "
      f"{loc(RX, 'positions = (n_tok - 1, lp[a][')}).")
    w(f"- **Label positions.** For each label, the LAST occurrence before the read of the first token of `\" \" + tag` "
      f"(`label_positions`, {loc(RX, 'def label_positions(')}); asserted to lie after the last forced span (the menu line of the first free choice).")
    w(f"- **Config of record (Stage C reads artifact):** layer {cfg['layer']}, frac {cfg['frac']}, alpha {cfg['alpha']:.4f} "
      f"(R_48 {cfg['R_48']}), axis sha16 `{cfg['axis_direction_sha_f64']}`, random direction `{cfg['random_direction']}` "
      f"sha16 `{cfg['random_direction_sha']}`; the two injections asserted equal-norm ({loc(RX, 'assert_equal_norm(axis, rand)')}).")
    w(f"- **Masks** (over the four forced-round token spans of the first-choice prefix; the read position and every label "
      f"position unsteered): M1 as generated (+alpha on pos-pole rounds, -alpha on neg-pole rounds, axis); M2 flipped; "
      f"M3 / M4 the random direction with M1's / M2's sign pattern (direction: {loc(RX, 'if mask in (\"M3\", \"M4\") or mask.endswith(\"x\"):')}; "
      f"sign pattern: `signs_for`, {loc(RX, 'def signs_for(spans, mask):')}); "
      f"Stage B adds M5/M6 (all +/all -, axis), M5x/M6x (random), R1-R4 (one round at its as-generated pole, axis), R1x-R4x (random); "
      f"Stage C adds block masks B1 ++--, B2 --++, B3 +--+, B4 -++- (absolute signs, axis) and B1x-B4x (random) "
      f"({loc(RX, 'BLOCK_SIGNS = {')}). e2a's forced order alternates labels, so rounds 1 and 3 are the start label's and 2 and 4 the other's.")
    w(f"- **Classifier.** Standardized L2 logistic regression, full-batch gradient descent, seed 7, 300 iterations, rate 0.1, "
      f"L2 1e-2 ({loc(PRB, 'LR_SEED, LR_ITERS, LR_RATE, LR_L2 = 7, 300, 0.1, 1e-2')}); AUC = Mann-Whitney with ties at 0.5 "
      f"(`auc_from_scores`, {loc('valence_core/discrim.py', 'def auc_from_scores(')}).")
    w(f"- **CV schemes.** *Grouped 10-fold* (Stages B, C): sessions assigned to 10 folds by a seeded permutation, every row of a "
      f"session in one fold ({loc(PRB, 'def grouped_folds(')}); the 200-shuffle null permutes the targets across ALL rows and is "
      f"scored on the SAME folds (`kfold_shuffle_null`, {loc(PRB, 'def kfold_shuffle_null(')}; called with fold_seed = the family "
      f"seed, perm_seed = family seed + layer, {loc(RX, 'perm_seed=seed + l)')}); family seed 80260905 + 1000*fi in Stage B "
      f"({loc(RX, '80260905 + 1000 * fi')}), 90260905 + 1000*fi in Stage C ({loc(RX, '90260905 + 1000 * fi')}). "
      f"*LOSO* (leave-one-session-out, all rows of a session held out together; {loc(PRB, 'def loso_scores(')}): the Stage A statistic "
      f"and null; in Stages B and C a point estimate beside each 10-fold figure, with no null of its own; in PROPOSAL-k Stage 1 the "
      f"statistic and its 200-shuffle null (seed {20260909} + 1000*fi, the same permutation stream at every layer of a family, "
      f"{loc(KA, 'jobs.append((name, l, X, y, g, n_shuffles, seed + 1000 * fi))')}). 'Above null' = AUC > the null's 95th percentile.")
    w(f"- **Stage B's two analysis artifacts.** `stageB_analysis.json` (the Stage B entry's) and `stageB_analysis_samefolds.json` "
      f"(re-run after the same-fold correction to the null; the record's correction: {loc(RE, '**CORRECTION to the STAGE B entry (which stands as written):** every')}). "
      f"The statistic is identical in the two; only the nulls move (checked below). This raw uses the samefolds nulls and prints the original beside.")
    w()
    J["definitions"] = {"n_valid_reward_sessions": len(valid_reward), "roster_matches_reads": roster_ok,
                        "e2a_arm_counts": arm_counts, "config_of_record": cfg}

    # --------------------------------------------------- stored-artifact checks
    d_auc = max(abs(B["families"][f][str(l)]["auc_kfold"] - Bs["families"][f][str(l)]["auc_kfold"])
                for f in B["families"] for l in L_ALL)
    d_loso = max(abs(B["families"][f][str(l)]["auc_loso"] - Bs["families"][f][str(l)]["auc_loso"])
                 for f in B["families"] for l in L_ALL)
    d_null = max(abs(B["families"][f][str(l)]["shuffle95"] - Bs["families"][f][str(l)]["shuffle95"])
                 for f in B["families"] for l in L_ALL)
    flips_b = [(f, l) for f in B["families"] for l in L_ALL
               if B["families"][f][str(l)]["above_null"] != Bs["families"][f][str(l)]["above_null"]]
    w(f"Stage B original vs samefolds: max |delta AUC (10-fold)| = {d_auc}, max |delta AUC (LOSO)| = {d_loso}, "
      f"max |delta shuffle95| = {d_null:.4f}; above-null verdicts that differ: {flips_b}.")
    w()
    J["stageB_original_vs_samefolds"] = {"max_abs_d_auc_kfold": d_auc, "max_abs_d_auc_loso": d_loso,
                                         "max_abs_d_shuffle95": d_null, "above_null_flips": flips_b}

    # ====================================================================== ≤48
    w("## 2. Construction fact: layers <= 48 (the steering layer) carry no state")
    w()
    le_b, le_c = B["le48_control"], C["le48_control"]
    w(f"- Stage B `le48_control`: {le_b['cells_checked']:,} (session, stored key, layer <= 48) cells, all bit-identical to the shadow: "
      f"{le_b['all_identical_to_shadow']}; `stop_clause.fired` = {B['stop_clause']['fired']} (samefolds: {Bs['stop_clause']['fired']}).")
    w(f"- Stage C `le48_control`: {le_c['cells_checked']:,} (session, stored key, layer <= 48, position) cells, all bit-identical to the shadow: "
      f"{le_c['all_identical_to_shadow']}; `stop_clause.fired` = {C['stop_clause']['fired']}; "
      f"`probe_layers_le48_above_null` = {C['stop_clause']['probe_layers_le48_above_null']}.")
    w(f"- Stage A: `stop_clause` = {A['stop_clause']['fired']} (layers <= 48 above null: {A['stop_clause']['layers_le_48_above_null']}).")
    # every state family at <=48 exactly 0.5, both CV schemes; text-only families not
    def le48_check(an, stage):
        res = {}
        for f, fam in an["families"].items():
            v = [(fam[str(l)]["auc_kfold"], fam[str(l)]["auc_loso"]) for l in LE48]
            res[f] = all(a == 0.5 and b == 0.5 for a, b in v)
        return res
    lc_b, lc_c = le48_check(Bs, "B"), le48_check(C, "C")
    state_b = [f for f in lc_b if "TEXTONLY" not in f]
    state_c = [f for f in lc_c if "TEXTONLY" not in f]
    text_b = [f for f in lc_b if "TEXTONLY" in f]
    paired_b = [f for f in state_b if not f.startswith("c_R") and not f.startswith("cc_R")]
    single_b = [f for f in state_b if f not in paired_b]
    n_half_b = sum(lc_b.values())
    w(f"- Stored AUC at L40/L44/L48 exactly 0.5 under both 10-fold and LOSO: Stage C, every state-carrying family "
      f"({sum(lc_c[f] for f in state_c)}/{len(state_c)}); Stage C text-only (shadow-row) families "
      f"({sum(lc_c[f] for f in lc_c if 'TEXTONLY' in f)}/{sum(1 for f in lc_c if 'TEXTONLY' in f)}); "
      f"Stage B paired families (a1, a1c, a2, a2c, b, bc) ({sum(lc_b[f] for f in paired_b)}/{len(paired_b)}); "
      f"Stage B single-round families R1-R4 / R1x-R4x ({sum(lc_b[f] for f in single_b)}/{len(single_b)} single-round); "
      f"Stage B text-only families cb_R1-R4 ({sum(lc_b[f] for f in text_b)}/{len(text_b)} text-only); Stage B in all "
      f"{n_half_b}/{len(lc_b)} (e.g. c_R1_roundpole L40 {f3(Bs['families']['c_R1_roundpole']['40']['auc_kfold'])}, "
      f"c_R4_roundpole L44 {f3(Bs['families']['c_R4_roundpole']['44']['auc_kfold'])}).")
    w("- Why .5 by construction in the paired families: each session contributes two (or four) rows that are bit-identical "
      "at layers <= 48 and carry opposite (balanced) targets inside one fold, so every positive score is tied with a negative "
      "score from the same session and the tie-at-0.5 AUC is exactly .5. The single-round families (one row per session, target = "
      "the round's pole) and the text-only families (the shadow rows) are not paired: their <= 48 values are ordinary fits on "
      "state-free rows, not .5 by construction (printed in sections 3b and 5).")
    loc_4752 = loc(RE, "the 40/44/48 probes are exactly 0.500 for every family", after=RB_HDR)
    REF_NOTES.append(f"Section 2: the Stage B entry's 'the 40/44/48 probes are exactly 0.500 for every family' ({loc_4752}) "
                     f"holds for the {len(paired_b)} paired families only ({sum(lc_b[f] for f in paired_b)}/{len(paired_b)}); the "
                     f"{len(single_b)} single-round and {len(text_b)} text-only Stage B families are ordinary fits on state-free rows at "
                     f"L40-L48 (e.g. c_R1_roundpole L40 {f3(Bs['families']['c_R1_roundpole']['40']['auc_kfold'])}), so the artifact "
                     f"contradicts that sentence for {len(lc_b) - n_half_b} of {len(lc_b)} families. The STOP clause it reports "
                     "(every layer <= 48 cell bit-identical to the shadow) holds as stored. A note sentence 'layers <= 48 read exactly "
                     ".500' should be scoped to paired contrasts.")
    w("- Which of the note's ranges include such layers (each figure's row in section 7 repeats it):")
    w("  - sign at the first free choice .94-.995 (3a): no; the range holds on L50-L63 (the record's domain 'every layer above 48' "
      "starts at L49, where the value is .695; see 3a).")
    w("  - retention peaks .89 / .68 (3b): no; L52 / L51.")
    w("  - binding at the label token >= .998 (3c, ib-2) and .81-.96 at the second label (ib-3): no; L51-L61 / L51-L63.")
    w("  - binding at the decision token .50-.55 (3d, ib-4): YES if the range is read over all 18 stored layers: L40/L44/L48 are .500 "
      "exactly by construction. The range is the same without them (L49-L63 gives .501-.545).")
    def _nb(fname, layers):
        v = [C["families"][fname][str(l)]["shuffle95"] for l in layers]
        return f"{min(v):.3f}-{max(v):.3f}"
    _c1 = ("c1_label_a_M1M2", "c1_label_b_M1M2", "c1_read_M1M2")
    w("  - the shuffle-95 null band (ib-1, ib-5): YES if F1 plots L40-L48; those layers' nulls are ordinary shuffle nulls of state-free "
      f"rows (not .5); the band is {' / '.join(_nb(f, L_ALL) for f in _c1)} with them and {' / '.join(_nb(f, L_ABOVE) for f in _c1)} "
      "over L49-L63 (label_a / label_b / read). F1 itself is not on this machine (preflight, N1), so neither its layer range nor "
      "which family's null it plots is checked here (section 4 states the band by family and by domain).")
    w("  - PROPOSAL-k Stage 1 .861 (L51-L62) and .88 -> .64 (L51-L61): no.")
    w()
    J["le48"] = {"stageB": le_b, "stageC": le_c, "stageB_stop": B["stop_clause"], "stageC_stop": C["stop_clause"],
                 "stageC_families_exact_half_at_le48": lc_c, "stageB_families_exact_half_at_le48": lc_b}

    # ================================================================ (i)
    w("## 3. Part (i): the figures the block quotes")
    w()

    # ---- 3a sign at the first free choice ---------------------------------
    w("### 3a. Sign at the first free choice (block: \".94-.995\")")
    w()
    a1 = Bs["families"]["a1_lastsign_M1M2"]; a1o = B["families"]["a1_lastsign_M1M2"]
    a1c = Bs["families"]["a1c_lastsign_M3M4_random"]; a2 = Bs["families"]["a2_lastsign_M5M6"]
    a2c = Bs["families"]["a2c_lastsign_M5xM6x_random"]
    w("Family `a1_lastsign_M1M2` (stageB_analysis_samefolds.json -> families): rows M1 and M2 at the READ position, 2 rows per "
      f"session x {Bs['n_sessions']} sessions; target = the injected sign of the LAST forced round (+1 for (M1, last pole pos) and "
      f"(M2, last pole neg)); grouped {Bs['kfold']}-fold, {Bs['n_shuffles']} shuffles on the same folds; LOSO beside "
      f"({loc(RX, 'fams[\"a1_lastsign_M1M2\"]')}). Comparators: a1c (M3/M4, random), a2 (M5/M6 all-same sign, axis), a2c (M5x/M6x).")
    w()
    rows = []
    for l in L_ALL:
        s = str(l)
        rows.append([l, f3(a1[s]["auc_kfold"]), f3(a1[s]["shuffle95"]), f3(a1o[s]["shuffle95"]),
                     "*" if a1[s]["above_null"] else "", f3(a1[s]["auc_loso"]), f3(a1c[s]["auc_kfold"]),
                     f3(a1c[s]["shuffle95"]), f3(a2[s]["auc_kfold"]), f3(a2c[s]["auc_kfold"])])
    w.table(["layer", "a1 M1vM2 10-fold", "null95 (samefolds)", "null95 (original)", "above", "a1 LOSO",
             "a1c random 10-fold", "a1c null95", "a2 M5vM6", "a2c M5xvM6x"], rows)
    lo50, hi50, llo50, lhi50 = rng_of(a1, range(50, 64))
    lo49, hi49, llo49, _ = rng_of(a1, range(49, 64))
    above_all = all(a1[str(l)]["above_null"] for l in range(49, 64))
    w(f"Range L50-L63: {f3(lo50)} ({Ls(llo50)}) to {f3(hi50)} ({Ls(lhi50)}); L49 = {f3(a1['49']['auc_kfold'])}; "
      f"so over L49-L63 the range is {f3(lo49)}-{f3(hi49)}. Above its null at every layer L49-L63: {above_all}. "
      f"LOSO over L50-L63: {f3(rng_of(a1, range(50, 64), 'auc_loso')[0])}-{f3(rng_of(a1, range(50, 64), 'auc_loso')[1])}.")
    w()
    loc_3a = loc(RE, 'linearly readable at every layer above 48 — AUC .94–.995 (M1/M2, grouped', after=RB_HDR)
    src_3a = f"data/echo/stageB_analysis_samefolds.json (and stageB_analysis.json) -> families.a1_lastsign_M1M2[L].auc_kfold; record {loc_3a}"
    ok_3a, ck_3a = chk_range([a1[str(l)]["auc_kfold"] for l in L_ABOVE], ".94", ".995")
    ok_3a50, ck_3a50 = chk_range([a1[str(l)]["auc_kfold"] for l in range(50, 64)], ".94", ".995")
    fig("3a", "sign-at-first-free-choice AUC range .94-.995",
        f"{f3(lo50)}-{f3(hi50)} over L50-L63 (min at {Ls(llo50)}, max at {Ls(lhi50)}); L49 {f3(a1['49']['auc_kfold'])}; "
        f"family a1_lastsign_M1M2, read position, target = injected sign of the last forced round, M1 v M2 rows, grouped 10-fold, "
        f"n = 102 sessions (204 rows), 200 shuffles; includes <= 48? no",
        src_3a, status_of(ok_3a),
        f"the quote states no layers; its source states 'every layer above 48' ({loc_3a}), i.e. L49-L63, where L49 reads .695 "
        f"(above its null .61); the range holds on L50-L63 ({ck_3a50}). Correction: 'L50-L63' in place of 'every layer above 48'. "
        f"The record's own figure check already states this ({FC['B1']})",
        domain=f"L49-L63 (the source's 'every layer above 48', {loc_3a})",
        check=f"L49-L63: {ck_3a}; L50-L63: {ck_3a50}")
    REF_NOTES.append("3a: the Stage B entry's header says the last-round sign is readable 'at every layer above 48 — AUC .94–.995' "
                     f"({loc_3a}); the stored family gives .941-.995 over L50-L63 and {f3(a1['49']['auc_kfold'])} at L49 (above null at "
                     "every layer L49-L63). Under section 7's rule (domain = the source's, since the quote states none) the row is "
                     "'discrepant (transcription)': the stored values reproduce exactly and the range needs 'L50-L63'. If the note "
                     "carries the record's 'every layer above 48', that wording is the one to correct. The record's own figure check "
                     f"already states this correction ('L49 reads .695, the range holds L50–L63', {FC['B1']}); this audit's "
                     "recomputation agrees with it. The quantity is the sign of the "
                     "LAST forced round (registered target (a)), read at the first free choice; it is not a 'first-round' sign.")
    # Stage A post-hoc and k1 G3 for context
    ph = Aph["per_layer"]
    ph_lo, ph_hi = min(ph[str(l)]["auc_reward_lastround_sign"] for l in range(50, 64)), max(ph[str(l)]["auc_reward_lastround_sign"] for l in range(50, 64))
    ph_lo58 = min(ph[str(l)]["auc_reward_lastround_sign"] for l in range(50, 59)); ph_hi58 = max(ph[str(l)]["auc_reward_lastround_sign"] for l in range(50, 59))
    w(f"Beside: Stage A post-hoc #1 (same target, n = 24 sessions, LOSO statistic and LOSO 200-shuffle null; "
      f"stageA_posthoc_lastround.json -> per_layer.auc_reward_lastround_sign; rule-11 post-hoc): {f3(ph_lo)}-{f3(ph_hi)} over L50-L63, "
      f"{f3(ph_lo58)}-{f3(ph_hi58)} over L50-L58 (the Stage A entry's '.87–.98 over L50–L58', "
      f"{loc(RE, 'of the last forced round IS readable at AUC .87–.98 over L50–L58', after=RA_HDR)}); L49 {f3(ph['49']['auc_reward_lastround_sign'])}.")
    w()
    J["3a"] = {"a1_lastsign_M1M2": a1, "a1_shuffle95_original": {l: a1o[l]["shuffle95"] for l in a1o},
               "a1c_lastsign_M3M4_random": a1c, "a2_lastsign_M5M6": a2, "a2c_lastsign_M5xM6x_random": a2c,
               "range_L50_L63": [lo50, hi50], "L49": a1["49"]["auc_kfold"],
               "stageA_posthoc_lastround": ph}

    # ---- 3b primacy profile --------------------------------------------------
    w("### 3b. Primacy profile (block: \".89 first round, .68 fourth\")")
    w()
    w("Families `c_R1_roundpole` .. `c_R4_roundpole` (stageB_analysis_samefolds.json): the single-round masks R1..R4 (one forced round "
      "steered at its as-generated pole, axis, the other three unsteered), READ position, ONE row per session (102 rows), target = "
      f"that round's pole; grouped 10-fold, 200 shuffles; LOSO beside ({loc(RX, 'fams[f\"c_R{rr + 1}_roundpole\"]')}). "
      "Random comparators `cc_R*x_roundpole_random`; text-only baseline `cb_R*_roundpole_TEXTONLY_shadow` (shadow rows, same target).")
    w()
    ret = Bs["retention"]
    rows = []
    J["3b"] = {"retention_distance": ret, "families": {}}
    peaks = {}
    for rr in range(1, 5):
        fa = Bs["families"][f"c_R{rr}_roundpole"]; fx = Bs["families"][f"cc_R{rr}x_roundpole_random"]
        ft = Bs["families"][f"cb_R{rr}_roundpole_TEXTONLY_shadow"]; fo = B["families"][f"c_R{rr}_roundpole"]
        lo, hi, _, lhi = rng_of(fa, L_ABOVE)
        _, hix, _, lhix = rng_of(fx, L_ABOVE)
        above = [l for l in L_ALL if fa[str(l)]["above_null"]]
        above_o = [l for l in L_ALL if fo[str(l)]["above_null"]]
        tmax = max(ft[str(l)]["auc_kfold"] for l in L_ALL)
        t_above = [l for l in L_ALL if ft[str(l)]["above_null"]]
        dist = ret[f"R{rr}"]["tokens_last_steered_to_read"]
        peaks[rr] = (hi, lhi)
        rows.append([f"R{rr}", f"{dist['mean']:.1f} ({dist['min']}-{dist['max']})", f"{f3(hi)} ({Ls(lhi)})",
                     f3(fa["63"]["auc_kfold"]), f"{len(above)}: {above}", f"{len(above_o)}", f"{f3(hix)} ({Ls(lhix)})",
                     f"{f3(tmax)}; above null at {t_above}"])
        J["3b"]["families"][f"R{rr}"] = {"axis": fa, "random": fx, "textonly": ft, "peak": [hi, lhi],
                                         "layers_above_null_samefolds": above, "layers_above_null_original": above_o}
    w.table(["round", "tokens last steered -> read, mean (min-max)", "axis peak 10-fold (layer)", "axis L63",
             "layers above null (samefolds)", "n above (original nulls)", "random peak (layer)", "text-only max over 18 layers"], rows)
    w("Per layer (10-fold AUC; * = above the samefolds null, marked on the axis columns only; the random and text-only columns' own above-null flags are in the JSON):")
    w()
    rows = []
    for l in L_ALL:
        s = str(l); r_ = [l]
        for rr in range(1, 5):
            fa = Bs["families"][f"c_R{rr}_roundpole"]
            r_ += [f"{f3(fa[s]['auc_kfold'])}{'*' if fa[s]['above_null'] else ''}",
                   f3(Bs["families"][f"cc_R{rr}x_roundpole_random"][s]["auc_kfold"]),
                   f3(Bs["families"][f"cb_R{rr}_roundpole_TEXTONLY_shadow"][s]["auc_kfold"])]
        rows.append(r_)
    w.table(["layer"] + [x for rr in range(1, 5) for x in (f"R{rr}", f"R{rr}x", "text")], rows)
    pk_all = {rr: max(Bs["families"][f"c_R{rr}_roundpole"][str(l)]["auc_kfold"] for l in L_ALL) for rr in range(1, 5)}
    ck_3b = [chk_single(peaks[rr][0], q) for rr, q in ((1, ".89"), (4, ".68"))]
    ck_3b_rec = [chk_single(peaks[rr][0], q) for rr, q in ((2, ".66"), (3, ".83"))]
    ok_3b = all(c[0] for c in ck_3b)
    fig("3b", "primacy profile .89 first round, .68 fourth",
        f"R1 peak {f3(peaks[1][0])} at {Ls(peaks[1][1])}; R4 peak {f3(peaks[4][0])} at {Ls(peaks[4][1])} "
        f"(R2 {f3(peaks[2][0])} {Ls(peaks[2][1])}, R3 {f3(peaks[3][0])} {Ls(peaks[3][1])}); families c_R1..c_R4_roundpole, "
        "single-round masks, read position, target = that round's pole, 102 rows (1/session), grouped 10-fold, 200 shuffles; "
        "peaks at different layers; includes <= 48? no (peaks are above 48)",
        f"data/echo/stageB_analysis_samefolds.json -> families.c_R{{1,4}}_roundpole[L].auc_kfold; record {loc(RE, 'but not ordered by distance — R1 at 157 tokens .89, R3 at 67 .83, R4 at', after=RB_HDR)}",
        status_of(ok_3b),
        "per-round PEAK AUCs at different layers (R1 L52, R4 L51); a retention curve over single-round masks, "
        "not a decorrelated primacy test (that is Stage C's C2, below). The record's R2 .66 and R3 .83 check too: "
        + "; ".join(c[1] for c in ck_3b_rec),
        domain="each round's peak over L49-L63 (the source states no layers; the peak over all 18 stored layers is the same: "
               + ", ".join(f"R{rr} {f4(pk_all[rr])}" for rr in range(1, 5)) + ")",
        check="R1: " + ck_3b[0][1] + "; R4: " + ck_3b[1][1])
    # C2 decorrelated primacy
    c2f = C["families"]["c2_firstsign_B1-4"]; c2l = C["families"]["c2_lastsign_B1-4"]
    c2fx = C["families"]["c2_firstsign_B1-4x_random"]; c2lx = C["families"]["c2_lastsign_B1-4x_random"]
    f_lo, f_hi, _, _ = rng_of(c2f, range(51, 63))
    l_pk, l_pkl = rng_of(c2l, L_ABOVE)[1], rng_of(c2l, L_ABOVE)[3]
    l_tail = rng_of(c2l, range(59, 64))
    w(f"Beside, the decorrelated version (Stage C C2, block masks B1-B4, rows at the READ position, 4 rows per session, 408 rows, "
      f"grouped 10-fold, 200 shuffles): FIRST-round sign {f3(f_lo)}-{f3(f_hi)} over L51-L62 ({f3(c2f['63']['auc_kfold'])} at L63); "
      f"LAST-round sign peaks {f3(l_pk)} at {Ls(l_pkl)} and reads {f3(l_tail[0])}-{f3(l_tail[1])} at L59-L63. Random (B1x-B4x): "
      f"first-round {f3(rng_of(c2fx, range(51, 59))[0])}-{f3(rng_of(c2fx, range(51, 59))[1])} at L51-L58, "
      f"{f3(rng_of(c2fx, range(59, 64))[0])}-{f3(rng_of(c2fx, range(59, 64))[1])} at L59-L63; last-round peak "
      f"{f3(rng_of(c2lx, L_ABOVE)[1])} at {Ls(rng_of(c2lx, L_ABOVE)[3])}.")
    w()
    J["3b"]["c2"] = {"firstsign_axis": c2f, "lastsign_axis": c2l, "firstsign_random": c2fx, "lastsign_random": c2lx}
    REF_NOTES.append("3b: '.89 first round, .68 fourth' are the PEAK AUCs of Stage B's single-round retention families "
                     f"(R1 .888 at L52, R4 .683 at L51; R1's last steered token is 156.6 tokens from the read on average, R4's 22.0), not values at one layer. "
                     "The record calls this 'retention ... not ordered by distance', and its own caveat holds: round position, "
                     "label parity (rounds 1/3 vs 2/4) and span length are confounded in the single-round design "
                     f"({loc(RE, 'Rounds 1 and 3 are the start-pole label', after=RB_HDR)}). The decorrelated primacy figure is "
                     "Stage C's C2 (first-round sign .98-.99 at L51-L62 vs last-round peak .924 at L54 falling to .65-.69).")

    # ---- 3c binding at the label token --------------------------------------
    w("### 3c. Binding at the label token (block: \">= .998, L51-61\")")
    w()
    la = C["families"]["c1_label_a_M1M2"]; lb = C["families"]["c1_label_b_M1M2"]; rd = C["families"]["c1_read_M1M2"]
    w(f"Family `c1_label_a_M1M2` (stageC_analysis.json): rows M1 and M2 at label_a's position (the first-listed menu label's last "
      f"token before the read), 2 rows per session x {C['n_sessions']} sessions; target = +1 iff label_a's rounds carried + under the "
      f"mask (M1: label_a == tag_plus; M2: the reverse); grouped {C['kfold']}-fold, {C['n_shuffles']} shuffles on the same folds; "
      f"LOSO beside ({loc(RX, 'fams[f\"c1_{pn}_M1M2\"]')}; targets as stored: \"{C['targets']['c1_label_a_*']}\").")
    w()
    band = list(range(51, 62))
    mn, mx_, lmn, _ = rng_of(la, band)
    n1000_3dp = [l for l in band if f"{la[str(l)]['auc_kfold']:.3f}" == "1.000"]
    n_exact = [l for l in band if la[str(l)]["auc_kfold"] == 1.0]
    w(f"Over L51-L61: min {f4(mn)} ({Ls(lmn)}), max {f4(mx_)}; prints as 1.000 (3 decimals) at {len(n1000_3dp)} of 11 layers {n1000_3dp}; "
      f"exactly 1.0 at {len(n_exact)} of 11 {n_exact}; L62 {f4(la['62']['auc_kfold'])}, L63 {f4(la['63']['auc_kfold'])}, "
      f"L50 {f4(la['50']['auc_kfold'])} ({'above' if la['50']['above_null'] else 'not above'} null), L49 {f4(la['49']['auc_kfold'])} "
      f"({'above' if la['49']['above_null'] else 'not above'} null). LOSO over L51-L61: {f4(rng_of(la, band, 'auc_loso')[0])}-{f4(rng_of(la, band, 'auc_loso')[1])}.")
    w()
    ok_3c, ck_3c = chk_bound([la[str(l)]["auc_kfold"] for l in band], ">=", ".998")
    fig("3c", "binding AUC at the label token >= .998, L51-61",
        f"{f4(mn)}-{f4(mx_)} over L51-L61 (min {Ls(lmn)}); 1.000 at 3 dp at {len(n1000_3dp)}/11, exactly 1.0 at {len(n_exact)}/11; "
        f"family c1_label_a_M1M2, label_a's token (read - 9), M1 v M2 rows, grouped 10-fold, n = 102 sessions (204 rows), 200 shuffles; "
        "includes <= 48? no",
        f"data/echo/stageC_analysis.json -> families.c1_label_a_M1M2[L].auc_kfold; record {loc(RE, 'reads at **AUC ≥ .998 (1.000 at nine of the eleven layers', after=RC_HDR)}",
        status_of(ok_3c),
        f"'1.000 at nine of eleven' (the record's) is a 3-decimal statement: {len(n1000_3dp)} of 11 print 1.000, {len(n_exact)} of 11 "
        "are exactly 1.0. Holds for label_a only; label_b is .81-.96",
        domain="L51-L61 (the quote's)", check=ck_3c)

    # ---- 3d binding at the decision token -----------------------------------
    w("### 3d. Binding at the decision token (block: \".50-.55\")")
    w()
    bl = Bs["families"]["b_labelpole_M1M2"]
    r_lo, r_hi, rl_lo, rl_hi = rng_of(rd, L_ABOVE)
    r_lo_all, r_hi_all, _, _ = rng_of(rd, L_ALL)
    r_above = [l for l in L_ALL if rd[str(l)]["above_null"]]
    b_lo, b_hi, _, _ = rng_of(bl, L_ABOVE)
    d_loso_cb = max(abs(rd[str(l)]["auc_loso"] - Bs["families"]["b_labelpole_M1M2"][str(l)]["auc_loso"]) for l in L_ALL)
    d_k_cb = max(abs(rd[str(l)]["auc_kfold"] - bl[str(l)]["auc_kfold"]) for l in L_ALL)
    w(f"Family `c1_read_M1M2` (stageC_analysis.json): the same rows and target as 3c ('label_a's rounds carried +') at the READ "
      f"position (the prefix's last token), grouped 10-fold, 200 shuffles, LOSO beside. L49-L63: {f3(r_lo)} ({Ls(rl_lo)}) to {f3(r_hi)} "
      f"({Ls(rl_hi)}); all 18 stored layers: {f3(r_lo_all)}-{f3(r_hi_all)} (L40/L44/L48 exactly .500 by construction, section 2); "
      f"above null at {r_above if r_above else 'no layer'}. Stage B's (b) `b_labelpole_M1M2` (the same target on the Stage B read rows; "
      f"the Stage C entry records the read-position rows as bit-identical to Stage B's stored rows in 102/102 sessions, "
      f"{loc(RE, 'the M1–M4 and shadow rows at the read position are bit-identical to Stage B', after=RC_HDR)}): {f3(b_lo)}-{f3(b_hi)} at L49-L63; LOSO identical to Stage C's "
      f"(max |delta| {d_loso_cb}); 10-fold differs by at most {d_k_cb:.4f} (different family seed).")
    w()
    ok_3d, ck_3d = chk_range([rd[str(l)]["auc_kfold"] for l in L_ABOVE], ".50", ".55")
    ok_3d18, ck_3d18 = chk_range([rd[str(l)]["auc_kfold"] for l in L_ALL], ".50", ".55")
    fig("3d", "binding AUC at the decision token .50-.55",
        f"{f3(r_lo)}-{f3(r_hi)} over L49-L63 ({f3(r_lo_all)}-{f3(r_hi_all)} over all 18 stored layers); below null at every layer; "
        "family c1_read_M1M2, read position (prefix's last token), M1 v M2 rows, target = label_a's rounds carried +, grouped 10-fold, "
        "n = 102 sessions (204 rows), 200 shuffles; includes <= 48? yes if read over all 18 stored layers (L40/44/48 = .500 by construction); "
        "the range is unchanged without them",
        f"data/echo/stageC_analysis.json -> families.c1_read_M1M2[L].auc_kfold; record {loc(RE, '(.50–.55) — reads at **AUC ≥ .998', after=RC_HDR)}",
        status_of(ok_3d and ok_3d18), "",
        domain="L49-L63 (neither the quote nor its source states layers); all 18 stored layers beside",
        check=f"L49-L63: {ck_3d}; all 18: {ck_3d18}")
    J["3c_3d"] = {"c1_label_a_M1M2": la, "c1_label_b_M1M2": lb, "c1_read_M1M2": rd, "b_labelpole_M1M2_stageB": bl}

    # ---- 3e positions --------------------------------------------------------
    w("### 3e. The positions (block: \"nine positions before\")")
    w()
    lpd = C["label_position_distance_to_read"]
    da_ = [v["read"] - v["label_a"] for v in C["label_positions"].values()]
    db_ = [v["read"] - v["label_b"] for v in C["label_positions"].values()]
    rr_a = [r["read_position"] - r["label_positions"][r["menu_a"]]["position"] for r in RC["per_session"].values()]
    rr_b = [r["read_position"] - r["label_positions"][r["menu_b"]]["position"] for r in RC["per_session"].values()]
    occ = sorted({(r["label_positions"][r["menu_a"]]["n_occurrences_before_read"], r["label_positions"][r["menu_b"]]["n_occurrences_before_read"]) for r in RC["per_session"].values()})
    cap_ok = all(r["capture_positions"] == [r["read_position"], r["label_positions"][r["menu_a"]]["position"], r["label_positions"][r["menu_b"]]["position"]] for r in RC["per_session"].values())
    npos = [r["n_positions"] for r in RC["per_session"].values()]
    kd_a = [r["read_position"] - r["label_positions"][r["menu_a"]]["position"] for r in KR["per_session"].values()]
    kd_b = [r["read_position"] - r["label_positions"][r["menu_b"]]["position"] for r in KR["per_session"].values()]
    w(f"- Stored `label_position_distance_to_read`: label_a min {lpd['label_a']['min']} max {lpd['label_a']['max']} mean {lpd['label_a']['mean']}; "
      f"label_b min {lpd['label_b']['min']} max {lpd['label_b']['max']} mean {lpd['label_b']['mean']} (token-index differences, read - label).")
    w(f"- Recomputed per session from stageC_analysis.json -> label_positions: read - label_a in {sorted(set(da_))} over {len(da_)} sessions; "
      f"read - label_b in {sorted(set(db_))}. From stageC_reads.json -> per_session: {sorted(set(rr_a))} / {sorted(set(rr_b))}; capture positions "
      f"= (read, label_a, label_b) in every session: {cap_ok}; (occurrences of label_a, label_b before the read) = {occ} (the earlier two are round headers); "
      f"prefix lengths {min(npos)}-{max(npos)} tokens.")
    w(f"- PROPOSAL-k Stage 1 (k1_reads.json): read - label_a in {sorted(set(kd_a))}, read - label_b in {sorted(set(kd_b))} over {len(kd_a)} sessions.")
    w()
    ok_3e = set(da_) == {9} and set(rr_a) == {9}
    fig("3e", "'nine positions before' (label token vs decision token)",
        f"label_a = read - {sorted(set(da_))[0]} in {len(da_)}/{len(da_)} sessions; label_b = read - {sorted(set(db_))[0]} in {len(db_)}/{len(db_)}",
        f"data/echo/stageC_analysis.json -> label_position_distance_to_read and label_positions; record {loc(RE, 'its paraphrase), 9 (label_a) and 7 (label_b) tokens before the read', after=RC_HDR)}",
        status_of(ok_3e),
        "'nine' is label_a (the first-listed menu label) only; label_b, where the binding reads .81-.96, is seven tokens before the read",
        domain="every one of the 102 sessions, label_a (the label the quoted .998 binding is read at)",
        check=f"read - label_a = 9 exactly in every session (count, exact): {'holds' if ok_3e else 'FAILS'}")
    J["3e"] = {"stored": lpd, "read_minus_label_a": sorted(set(da_)), "read_minus_label_b": sorted(set(db_)),
               "k1_read_minus_label_a": sorted(set(kd_a)), "k1_read_minus_label_b": sorted(set(kd_b)),
               "occurrences_before_read": occ, "prefix_tokens": [min(npos), max(npos)]}

    # ---- 3f-3i leakage ---------------------------------------------------------
    w("### 3f-3i. Leakage (block: \"0-3 of 102 sign flips; median |delta| <= .10 logit; pseudo-shift +/-.02-.03 toward the first block's label; the random-direction comparison\")")
    w()
    w("Recomputed from the reads artifacts (per session, the paired state and shadow restricted reads at the first free choice): "
      "pi_d = (sessions whose state pick differs from the shadow pick) / (sessions), unit = session, n = 102; "
      "|delta| = |(logit_a - logit_b)_state - (logit_a - logit_b)_shadow| in raw next-token logits of each label's first token, "
      "summarised over the 102 sessions; 95% interval = Clopper-Pearson exact two-sided (computed here, stdlib). "
      "The stored analysis values are printed beside and compared.")
    w()
    rows = []
    J["leak"] = {"reward": {}, "random_computed_new": {}, "signed": {}}
    reward_specs = [("B", m) for m in ("M1", "M2", "M5", "M6", "R1", "R2", "R3", "R4")] + [("C", m) for m in ("B1", "B2", "B3", "B4")]
    mism = []
    for st, m in reward_specs:
        reads, an = (RB, Bs) if st == "B" else (RC, C)
        v = leak_from_reads(reads, m)
        s_ = an["leak"][m]
        ok = (v["n_flips"] == s_["n_flips"] and abs(v["median"] - s_["abs_logit_diff_shift"]["median"]) < 1e-12
              and abs(v["max"] - s_["abs_logit_diff_shift"]["max"]) < 1e-12)
        if not ok:
            mism.append((st, m))
        rows.append([f"Stage {st}", m, f"{v['n_flips']}/{v['n']} = {v['pi_d']:.3f}", f"[{v['cp95'][0]:.3f}, {v['cp95'][1]:.3f}]",
                     f4(v["median"]), f4(v["mean"]), f4(v["max"]), f"{s_['n_flips']} / {f4(s_['abs_logit_diff_shift']['median'])}", "yes" if ok else "NO"])
        J["leak"]["reward"][f"{st}:{m}"] = v
    # Stage C M1/M2 equal Stage B's
    cm = {m: leak_from_reads(RC, m) for m in ("M1", "M2")}
    bm = {m: leak_from_reads(RB, m) for m in ("M1", "M2")}
    same_mc = all(cm[m]["n_flips"] == bm[m]["n_flips"] and cm[m]["median"] == bm[m]["median"] for m in ("M1", "M2"))
    w("**Axis masks** (the reward-axis direction; the twelve masks the record tables as its unsigned leak: Stage B "
      f"M1, M2, M5, M6, R1-R4, {loc(RE, '**LEAK (unsigned) and the signed quantities the block allows.**', after=RB_HDR)}; Stage C B1-B4, "
      f"{loc(RE, '**C3 — LEAK.** Unsigned on every reward mask.', after=RC_HDR)}). Unsigned here. The record's PROHIBITION, as the code "
      f"states it: a signed quantity toward a label is computable only for SIGNED_OK = M3, M4, M5, M6, M5x, M6x, B1x-B4x, and "
      f"`signed_pseudo_shift` refuses every reward mask M1, M2, R1-R4, B1-B4 ({loc(RX, 'PROHIBITION (§3.1), enforced in code')}; "
      f"SIGNED_OK {loc(RX, 'SIGNED_OK = {')}; the Stage A entry: {loc(RE, '**PROHIBITION, honoured in code.**', after=RA_HDR)}). "
      "The same-pole axis masks M5/M6 are in SIGNED_OK; their signed label-differential is in the signed table below.")
    w()
    w.table(["stage", "mask", "pi_d (pick flips / sessions)", "CP 95%", "median |delta|", "mean", "max", "stored n_flips / median", "match"], rows)
    flips = [J["leak"]["reward"][k]["n_flips"] for k in J["leak"]["reward"]]
    meds = {k: J["leak"]["reward"][k]["median"] for k in J["leak"]["reward"]}
    kmax = max(meds, key=meds.get)
    w(f"Stage C's M1/M2 leak equals Stage B's (same forwards): {same_mc}. Over the twelve axis masks: flips {min(flips)}-{max(flips)} of 102; "
      f"median |delta| {f4(min(meds.values()))}-{f4(max(meds.values()))}, the largest {kmax} {f4(meds[kmax])}; the alternating masks M1/M2 "
      f"{f4(meds['B:M1'])}/{f4(meds['B:M2'])}; every non-alternating axis mask (M5, M6, R1-R4, B1-B4) "
      f"{f4(min(v for k, v in meds.items() if k not in ('B:M1', 'B:M2')))}-{f4(max(v for k, v in meds.items() if k not in ('B:M1', 'B:M2')))}. "
      f"Stored-vs-recomputed mismatches: {mism if mism else 'none'}.")
    al = A["leak"]
    w(f"Beside, Stage A (n = 24, stored stageA_analysis.json -> leak): M1 {al['M1']['n_flips']}/24, median {f4(al['M1']['abs_logit_diff_shift']['median'])}; "
      f"M2 {al['M2']['n_flips']}/24, median {f4(al['M2']['abs_logit_diff_shift']['median'])}.")
    w()
    leak_stored_ok = not mism
    # pick flip vs sign flip, and where the flips sit (computed-new; every stored read of Stages B and C)
    n_reads, n_exc, flip_list = 0, 0, []
    for st, R in (("B", RB), ("C", RC)):
        for r in sorted(R["per_session"].values(), key=lambda r: r["session"]):
            for m, mm in r["masks"].items():
                for side in ("state", "shadow"):
                    x = mm[side]
                    n_reads += 1
                    if (x["pick"] == mm["label_a"]) != (x["logit_a"] >= x["logit_b"]):
                        n_exc += 1
                if mm["state"]["pick"] != mm["shadow"]["pick"]:
                    flip_list.append({"stage": st, "mask": m, "session": r["session"],
                                      "shadow_diff": mm["shadow"]["logit_a"] - mm["shadow"]["logit_b"],
                                      "state_diff": mm["state"]["logit_a"] - mm["state"]["logit_b"]})
    # Stage C's M1-M4 reads are Stage B's forwards: checked here read by read; each (session, mask) is then counted once
    same_m14 = all(RC["per_session"][s_]["masks"][m]["state"][k] == RB["per_session"][s_]["masks"][m]["state"][k]
                   and RC["per_session"][s_]["masks"][m]["shadow"][k] == RB["per_session"][s_]["masks"][m]["shadow"][k]
                   for s_ in RC["per_session"] for m in ("M1", "M2", "M3", "M4") for k in ("logit_a", "logit_b", "pick"))
    distinct = {}
    for f_ in flip_list:
        key = (f_["mask"], f_["session"])
        if key not in distinct:
            distinct[key] = f_
    tie_sess = sorted({r["session"] for R in (RB, RC) for r in R["per_session"].values()
                       if any(mm["shadow"]["logit_a"] == mm["shadow"]["logit_b"] for mm in r["masks"].values())})
    on_tie = [k for k, f_ in distinct.items() if f_["shadow_diff"] == 0.0]
    untied = [(k, f_) for k, f_ in distinct.items() if f_["shadow_diff"] != 0.0]
    TIES = {"n_reads": n_reads, "n_pick_vs_sign_exceptions": n_exc, "n_distinct_flips": len(distinct), "stageC_M1_M4_equal_stageB": same_m14,
            "distinct_flips": [{"mask": k[0], "session": k[1], **{kk: vv for kk, vv in f_.items() if kk not in ("mask", "session")}}
                               for k, f_ in sorted(distinct.items(), key=lambda kv: (kv[0][1], kv[0][0]))],
            "sessions_with_tied_shadow": tie_sess, "n_flips_on_tied_shadow": len(on_tie),
            "untied_flips": [{"mask": k[0], "session": k[1], "shadow_diff": f_["shadow_diff"], "state_diff": f_["state_diff"]} for k, f_ in untied],
            "status": "computed-new"}
    J["leak"]["tie_analysis"] = TIES
    ties_line = (f"A pick flip is a sign flip of (logit_a - logit_b), ties going to label_a: pick == label_a iff logit_a >= logit_b in "
                 f"{n_reads - n_exc:,} of {n_reads:,} stored reads (Stages B and C, state and shadow; {n_exc} exceptions). Over the 24 "
                 f"distinct masks (Stage B's 16 and Stage C's B1-B4, B1x-B4x; Stage C's M1-M4 reads equal Stage B's in every session, "
                 f"logits and picks: {same_m14}, so each (session, mask) is counted once) there are {len(distinct)} distinct flips; "
                 f"{len(on_tie)} of them sit in the {len(tie_sess)} sessions whose shadow read is an EXACT tie (logit_a = logit_b; sessions "
                 f"{', '.join(str(s) for s in tie_sess)}): " + ", ".join(f"{k[0]} s{k[1]}" for k in sorted(on_tie, key=lambda k: (k[1], k[0]))) +
                 ". " + ("The only untied flip" + ("s are " if len(untied) > 1 else " is ") +
                         "; ".join(f"s{k[1]} under {k[0]} (shadow {f_['shadow_diff']:+.4f} -> state {f_['state_diff']:+.4f})" for k, f_ in untied)
                         if untied else "No flip comes from an untied shadow") +
                 ". Per axis mask with a flip: " +
                 "; ".join(f"{m} {sum(1 for k in distinct if k[0] == m)}/102 = {sum(1 for k in distinct if k[0] == m and distinct[k]['shadow_diff'] != 0.0)} "
                           f"untied + {sum(1 for k in distinct if k[0] == m and distinct[k]['shadow_diff'] == 0.0)} tie-break(s)"
                           for m in ("M1", "M2", "M5", "M6", "R1", "R2", "R3", "R4", "B1", "B2", "B3", "B4") if any(k[0] == m for k in distinct)) +
                 ". [computed-new]")
    TIES["per_axis_mask"] = {m: {"n": sum(1 for k in distinct if k[0] == m),
                                 "untied": sum(1 for k in distinct if k[0] == m and distinct[k]["shadow_diff"] != 0.0)}
                             for m in ("M1", "M2", "M5", "M6", "R1", "R2", "R3", "R4", "B1", "B2", "B3", "B4")}
    ok_3f, ck_3f = chk_range(flips, "0", "3")
    fig("3f", "leakage: 0-3 of 102 sign flips",
        f"{min(flips)}-{max(flips)} of 102 pick flips over the 12 axis masks (M2 3/102 = .029, CP95 "
        f"[{J['leak']['reward']['B:M2']['cp95'][0]:.3f}, {J['leak']['reward']['B:M2']['cp95'][1]:.3f}]; M1, M6, B3 1/102; the rest 0/102)",
        "data/echo/stageB_reads.json, stageC_reads.json -> per_session[*].masks[m].{state,shadow}.pick (recomputed); "
        f"stored stageB_analysis*.json / stageC_analysis.json -> leak[m].n_flips; record {loc(RE, '| M2 | 3/102 = 0.029 | 0.1027 | 0.1042 | 0.2429 |', after=RB_HDR)}",
        status_of(ok_3f, leak_stored_ok),
        f"state pick != shadow pick per session (the record's pi_d); a pick flip is exactly a sign flip of (logit_a - logit_b), ties to "
        f"label_a ({n_exc} exceptions in {n_reads:,} stored reads), so the block's 'sign flips' (block line 43) is accurate. "
        f"Computed-new: {len(on_tie)} of the {len(distinct)} distinct (session, mask) flips over all 24 masks sit on the {len(tie_sess)} "
        f"exactly tied shadow reads (sessions {', '.join(str(s) for s in tie_sess)}); the untied: "
        + ("; ".join(f"s{k[1]} under {k[0]} ({f_['shadow_diff']:+.4f} -> {f_['state_diff']:+.4f})" for k, f_ in untied) or "none")
        + " (section 3f-3i)",
        domain="the 12 axis masks of the record's two leak tables, n = 102 sessions each",
        check=f"counts (exact): {ck_3f}; n = {sorted({J['leak']['reward'][k]['n'] for k in J['leak']['reward']})}")
    med_vals = list(meds.values())
    ok_3g, ck_3g = chk_bound(med_vals, "<=", ".10")
    ok_3g103, ck_3g103 = chk_bound(med_vals, "<=", ".103")
    n_le10 = sum(1 for v in med_vals if v <= 0.10)
    fig("3g", "leakage: median |delta| <= .10 logit",
        f"max median {f4(meds[kmax])} ({kmax}); M1 {f4(meds['B:M1'])}; non-alternating axis masks "
        f"{f4(min(v for k, v in meds.items() if k not in ('B:M1', 'B:M2')))}-{f4(max(v for k, v in meds.items() if k not in ('B:M1', 'B:M2')))}; "
        "unit logit (label first-token logit difference, state minus shadow), median over 102 sessions",
        "recomputed from stageB_reads.json / stageC_reads.json; stored leak[m].abs_logit_diff_shift.median; record "
        f"{loc(RE, '|Δ| ≈ .10 vs M5/M6 and R1–R4 ≈ .04; π_d 1–3/102 vs 0–1/102) —', after=RB_HDR)}",
        status_of(ok_3g, leak_stored_ok),
        f"a bound is an inequality (section 7, R1): M2's median {f4(meds['B:M2'])} > .10, so '<= .10' fails at {12 - n_le10} of 12 masks "
        f"(it prints .10 at two decimals, which is why the overrun is easy to miss); the record itself writes '≈ .10'. "
        f"Correction: '≈ .10' or '<= .103' ({ck_3g103}). The record's own figure check already states it: realised medians "
        f".033–.103, 'exact would read .03–.10' ({FC['B4_median']}). Stage A's n = 24 M1 median was .108",
        domain="the 12 axis masks of the record's two leak tables (the same domain as 3f), median over 102 sessions each",
        check=ck_3g)
    REF_NOTES.append(f"3g: 'median |delta| <= .10' is exceeded by M2 (.1027, Stage B/C, n = 102; "
                     f"{loc(RE, '| M2 | 3/102 = 0.029 | 0.1027 | 0.1042 | 0.2429 |', after=RB_HDR)}); the record's own wording is "
                     f"'≈ .10' ({loc(RE, '|Δ| ≈ .10 vs M5/M6 and R1–R4 ≈ .04; π_d 1–3/102 vs 0–1/102) —', after=RB_HDR)}). "
                     "Under section 7's rule (a bound is checked at full precision) the row is 'discrepant (transcription)', not a "
                     "reproduction failure: the stored medians reproduce exactly, and the sentence should read '≈ .10' or '<= .103'. "
                     "The record's own figure check already states this: 'realised medians run .033–.103 (R3 .0327), so exact would "
                     f"read .03–.10' ({FC['B4_median']}); this audit's recomputation agrees with it.")

    # random-direction comparison: the record's TABLES carry no random-mask flip or |delta| figure; its prose states the flips and the max
    w("**Random-direction masks** (norm-matched random direction, same spans and sign patterns). The record's tables carry no "
      f"random-mask flips or |delta| (the k Stage 1 entry: 'the recon tables no flip figure on its random masks', "
      f"{loc(RE, 'same-pole, single-round and block REWARD masks — the recon tables no', after=K1_HDR)}); its prose states the random "
      f"families' flips 0–1/102 ({FC['B4_flips']}) and, for the R / M++ arms (axis and random; {FC['B4_RMpp']}), the largest "
      "per-family max |Δ|, M5x .2012, which is also the largest on the 12 random masks (the clause's domain is computed below the "
      "table); both are checked below (row 3i-a1). The medians are new here (row 3i-a2, computed-new).")
    w()
    rows = []
    rand_specs = [("B", m) for m in ("M3", "M4", "M5x", "M6x", "R1x", "R2x", "R3x", "R4x")] + [("C", m) for m in ("B1x", "B2x", "B3x", "B4x")]
    for st, m in rand_specs:
        reads = RB if st == "B" else RC
        v = leak_from_reads(reads, m)
        rows.append([f"Stage {st}", m, f"{v['n_flips']}/{v['n']} = {v['pi_d']:.3f}", f"[{v['cp95'][0]:.3f}, {v['cp95'][1]:.3f}]",
                     f4(v["median"]), f4(v["mean"]), f4(v["max"])])
        J["leak"]["random_computed_new"][f"{st}:{m}"] = v
    w.table(["stage", "mask", "pi_d (pick flips / sessions)", "CP 95%", "median |delta|", "mean", "max"], rows)
    rf = [J["leak"]["random_computed_new"][k]["n_flips"] for k in J["leak"]["random_computed_new"]]
    rmed = {k: J["leak"]["random_computed_new"][k]["median"] for k in J["leak"]["random_computed_new"]}
    rmax = {k: J["leak"]["random_computed_new"][k]["max"] for k in J["leak"]["random_computed_new"]}
    kmx = max(rmax, key=rmax.get)
    # The record's max clause ({FC['B4_RMpp']}) is about 'the R / M++ arms the memo names for the gate', not the random masks alone:
    # it names M5x (random) and M5 (axis). The record does not list which recon masks it means, so the candidate domains are computed.
    _allmask = {**{k: v for k, v in J["leak"]["reward"].items()}, **{k: v for k, v in J["leak"]["random_computed_new"].items()}}
    loc_pk_r = loc(PK, "`R+A` : +r on A's block")
    loc_pk_mpp = loc(PK, "`M++` : +d on both blocks")
    RMPP_DOMAINS = [
        ("A", f"PROPOSAL-k's naming (R = the arms on the random direction r, {loc_pk_r}; M++ = +d on both blocks, {loc_pk_mpp}): the 12 "
              "random masks and the same-pole axis masks M5/M6", sorted(rmax) + ["B:M5", "B:M6"]),
        ("B", "Stage B's same-pole and single-round masks, axis and random (M5, M6, R1-R4, M5x, M6x, R1x-R4x; the values-checker's reading)",
         [f"B:{m}" for m in ("M5", "M6", "R1", "R2", "R3", "R4", "M5x", "M6x", "R1x", "R2x", "R3x", "R4x")]),
        ("C", "every mask but the alternating reward masks M1/M2 (22 masks)", sorted(k for k in _allmask if k not in ("B:M1", "B:M2"))),
    ]
    RMPP = {}
    for dn, desc, ks in RMPP_DOMAINS:
        mx = {k: _allmask[k]["max"] for k in ks}
        fl = [_allmask[k]["n_flips"] for k in ks]
        top = max(mx, key=mx.get); bot = min(mx, key=mx.get)
        ok_r, ck_r_ = chk_range(list(mx.values()), ".11", ".20")
        ok_f, ck_f_ = chk_range(fl, "0", "1")
        RMPP[dn] = {"description": desc, "masks": ks, "max_by_mask": mx, "largest": top, "smallest": bot,
                    "m5x_largest": top == "B:M5x", "range_11_20": [ok_r, ck_r_], "flips_0_1": [ok_f, ck_f_]}
    rmpp_le11 = sorted((k for k in _allmask if k not in ("B:M1", "B:M2") and qr(_allmask[k]["max"], ".11") <= _dec(".11")),
                       key=lambda k: _allmask[k]["max"])
    ok_m5, ck_m5 = chk_single(_allmask["B:M5"]["max"], ".1913")
    J["leak"]["record_RMpp_clause"] = {"locator": FC["B4_RMpp"], "domains": RMPP, "M5_max_check": [ok_m5, ck_m5],
                                       "non_M1M2_masks_with_max_rounding_to_le_11": rmpp_le11,
                                       "status": "computed-new (the record names no mask list for this clause)"}
    rmpp_txt = "; ".join(f"({dn}) {d['description']}: largest {d['largest'].split(':')[1]} {f4(d['max_by_mask'][d['largest']])}, "
                         f"smallest {d['smallest'].split(':')[1]} {f4(d['max_by_mask'][d['smallest']])}; '.11–.20': {d['range_11_20'][1]}; "
                         f"'0–1/102 there': {d['flips_0_1'][1]}; M5x the largest: {d['m5x_largest']}"
                         for dn, d in RMPP.items())
    w(f"**The record's max clause and its domain.** {FC['B4_RMpp']} reads the flips and the max of the two-horns memo as coming "
      "'from the alternating reward masks M1/M2, not the R / M++ arms the memo names for the gate (0–1/102 there, per-family max "
      "|Δ| .11–.20, the largest M5x .2012 and M5 .1913)'. Its domain is the R / M++ arms, axis and random (it names M5x, random, "
      "and M5, axis), not the random masks alone; the record lists no recon masks for it, so three candidate domains are computed "
      f"here from the committed reads: {rmpp_txt}. M5's max: {ck_m5}. [computed-new]")
    w()
    w(f"Random masks: flips {min(rf)}-{max(rf)} of 102; median |delta| {f4(min(rmed.values()))}-{f4(max(rmed.values()))}; "
      f"M3/M4 (the random analogs of M1/M2) {f4(rmed['B:M3'])}/{f4(rmed['B:M4'])} against M1/M2 {f4(meds['B:M1'])}/{f4(meds['B:M2'])}; "
      f"largest max |delta| {kmx} {f4(rmax[kmx])}.")
    w()
    w(ties_line)
    w()
    ok_ia1, ck_ia1 = chk_range(rf, "0", "1")
    ok_ia1m, ck_ia1m = chk_single(rmax[kmx], ".2012")
    fig("3i-a1", "leakage: the random-direction comparison (unsigned flips; the record's prose '0–1/102' and 'the largest M5x .2012')",
        f"random masks flips {min(rf)}-{max(rf)} of 102 ("
        + ", ".join(f"{k.split(':')[1]} {J['leak']['random_computed_new'][k]['n_flips']}/102" for k in J["leak"]["random_computed_new"]
                    if J["leak"]["random_computed_new"][k]["n_flips"]) + "; the rest 0/102); "
        f"largest per-mask max |delta| {kmx} {f4(rmax[kmx])}",
        "recomputed from stageB_reads.json / stageC_reads.json (random masks); no stored analysis field; record "
        f"{FC['B4_flips']} (flips, the random families) and {FC['B4_RMpp']} (max; that clause's domain is the R / M++ arms, axis and "
        "random)",
        status_of(ok_ia1 and ok_ia1m and kmx == "B:M5x" and RMPP["A"]["m5x_largest"] and RMPP["B"]["m5x_largest"]),
        "the record's tables carry no random-mask flips or |delta|; its prose states the random families' flips 0–1/102 and, for "
        "the R / M++ arms (axis and random), M5x's max .2012, which reproduce here from the committed reads: M5x is the largest on "
        f"the 12 random masks and on both readings of the R / M++ domain (A: {RMPP['A']['m5x_largest']}; B: "
        f"{RMPP['B']['m5x_largest']}), not over every non-M1/M2 mask (C: largest {RMPP['C']['largest'].split(':')[1]} "
        f"{f4(RMPP['C']['max_by_mask'][RMPP['C']['largest']])}, an axis block mask; on that reading M5x is not the largest). Referent note: the same "
        "clause's '.11–.20' holds on reading A and reads "
        + (f"'{_r(RMPP['B']['max_by_mask'][RMPP['B']['smallest']], 2)}–.20' on reading B" if not RMPP['B']['range_11_20'][0]
           else "'.11–.20' on reading B too")
        + " (section 3f-3i)",
        domain="the 12 random-direction masks (Stage B M3, M4, M5x, M6x, R1x-R4x; Stage C B1x-B4x), n = 102 sessions each; for the "
               "max, also the record clause's R / M++ domain (readings A and B, section 3f-3i)",
        check=f"flips (counts, exact): {ck_ia1}; largest max on the random masks is {kmx}: {ck_ia1m}; M5x the largest on R / M++ "
              f"reading A: {RMPP['A']['m5x_largest']}, reading B: {RMPP['B']['m5x_largest']}")
    REF_NOTES.append(f"3i-a1: the record's '(0–1/102 there, per-family max |Δ| .11–.20, the largest M5x .2012 and M5 .1913)' "
                     f"({FC['B4_RMpp']}) is about 'the R / M++ arms the memo names for the gate', axis and random, and lists no recon "
                     "masks; section 3f-3i defines the candidate readings. On reading A (the 12 random masks and M5/M6, PROPOSAL-k's "
                     f"naming) the check is: {RMPP['A']['range_11_20'][1]}. On reading B (Stage B's same-pole and single-round masks, "
                     f"axis and random, the values-checker's reading) it is: {RMPP['B']['range_11_20'][1]}, i.e. "
                     f"'{_r(RMPP['B']['max_by_mask'][RMPP['B']['smallest']], 2)}–{_r(RMPP['B']['max_by_mask'][RMPP['B']['largest']], 2)}' "
                     f"there, since the smallest per-mask max there is {RMPP['B']['smallest'].split(':')[1]} "
                     f"{f4(RMPP['B']['max_by_mask'][RMPP['B']['smallest']])}; of the 22 non-M1/M2 masks, the ones whose max rounds to "
                     ".11 or below at two decimals are "
                     + (", ".join(f"Stage {k.split(':')[0]}'s {k.split(':')[1]} {f4(_allmask[k]['max'])}" for k in rmpp_le11) or "none")
                     + ". M5x .2012 is the largest on both readings. A record-wording point, not a block figure.")
    fig("3i-a2", "leakage: the random-direction comparison (unsigned median |delta|)",
        f"median |delta| {f4(min(rmed.values()))}-{f4(max(rmed.values()))} over the 12 random masks; M3/M4 {f4(rmed['B:M3'])}/{f4(rmed['B:M4'])} "
        f"vs M1/M2 {f4(meds['B:M1'])}/{f4(meds['B:M2'])}; unit logit, median over 102 sessions",
        "recomputed from stageB_reads.json / stageC_reads.json (random masks); no stored analysis field",
        "computed-new",
        "no random-mask median in the record (its prose states only maxima: M5x .2012, row 3i-a1); the medians are new here",
        domain="the 12 random-direction masks, n = 102 sessions each",
        check="no quoted value to check (a new computation)")

    # signed (random / same-pole masks only)
    w("**Signed quantities, random and same-pole masks only** (recomputed; stored beside):")
    w()
    rows = []
    signed_specs = [("B", "M3", "rplus", Bs["pseudo_shift"]), ("B", "M4", "rplus", Bs["pseudo_shift"]),
                    ("C", "M3", "rplus", C["pseudo_shift"]), ("C", "M4", "rplus", C["pseudo_shift"]),
                    ("C", "B1x", "start", C["pseudo_shift"]), ("C", "B2x", "start", C["pseudo_shift"]),
                    ("C", "B3x", "start", C["pseudo_shift"]), ("C", "B4x", "start", C["pseudo_shift"]),
                    ("B", "M5", "label_a", Bs["label_differential"]), ("B", "M6", "label_a", Bs["label_differential"]),
                    ("B", "M5x", "label_a", Bs["label_differential"]), ("B", "M6x", "label_a", Bs["label_differential"])]
    sdef = {"rplus": "toward the label whose rounds carried r+", "start": "toward the START label (round 1's tag)",
            "label_a": "toward the first-listed menu label (label-differential)"}
    smism = []
    for st, m, kind, stored in signed_specs:
        v = signed_from_reads(RB if st == "B" else RC, m, kind)
        s_ = stored[m]
        ok = abs(v["mean"] - s_["mean"]) < 1e-12 and v["n_pos"] == s_["n_pos"] and v["n_neg"] == s_["n_neg"]
        if not ok:
            smism.append((st, m))
        rows.append([f"Stage {st}", m, sdef[kind], fs(v["mean"]), f4(v["sd"]), f"{v['n_pos']}/{v['n_neg']}", f"{fs(s_['mean'])} {s_['n_pos']}/{s_['n_neg']}", "yes" if ok else "NO"])
        J["leak"]["signed"][f"{st}:{m}"] = {"definition": sdef[kind], **v}
    w.table(["stage", "mask", "signed toward", "mean (logit)", "sd", "pos/neg of 102", "stored mean pos/neg", "match"], rows)
    w(f"Stored-vs-recomputed mismatches: {smism if smism else 'none'}.")
    # k1 G4 signed toward the first block's label
    kg4 = K["evaluation"]["G4"]
    krows = []
    for m in ("R+A", "R+B", "R++"):
        v = signed_from_reads(KR, m, "firstblock")
        s_ = kg4[m]["signed_shift_toward_first_block_label"]
        krows.append([m, fs(v["mean"]), f4(v["sd"]), f"{v['n_pos']}/{v['n_neg']}", f"{fs(s_['mean'])} {s_['n_pos']}/{s_['n_neg']}",
                      f"{kg4[m]['n_flips']}/{kg4[m]['n']}"])
        J["leak"]["signed"][f"k1:{m}"] = {"definition": "toward the first block's label (k1 G4)", **v}
    w()
    w(f"PROPOSAL-k Stage 1 G4 (k1_reads.json recomputed; k1_analysis.json -> evaluation.G4 beside), n = {len(KR['per_session'])} sessions, "
      "signed toward the FIRST BLOCK's label (the k format has label blocks; e2a's has alternating rounds):")
    w()
    w.table(["mask", "mean (logit)", "sd", "pos/neg", "stored mean pos/neg", "pi_d stored"], krows)
    b3, b4 = J["leak"]["signed"]["C:B3x"], J["leak"]["signed"]["C:B4x"]
    loc_3h = loc(RE, 'the random block masks a mechanical signed pseudo-shift of ±.02–.03 toward', after=RC_HDR)
    sh_stored_ok = not smism
    ok_3h, ck_3h = chk_range([abs(J["leak"]["signed"][f"C:{m}"]["mean"]) for m in ("B1x", "B2x", "B3x", "B4x")], ".02", ".03")
    ok_3h34, ck_3h34 = chk_range([abs(J["leak"]["signed"][f"C:{m}"]["mean"]) for m in ("B3x", "B4x")], ".02", ".03")
    fig("3h", "pseudo-shift +/-.02-.03 toward the first block's label",
        f"Stage C B3x {fs(b3['mean'])} (sd {f4(b3['sd'])}, {b3['n_pos']}/{b3['n_neg']}), B4x {fs(b4['mean'])} (sd {f4(b4['sd'])}, "
        f"{b4['n_pos']}/{b4['n_neg']}), toward the START label (round 1's tag), mean over 102 sessions; B1x "
        f"{fs(J['leak']['signed']['C:B1x']['mean'])}, B2x {fs(J['leak']['signed']['C:B2x']['mean'])}",
        f"recomputed from stageC_reads.json; stored stageC_analysis.json -> pseudo_shift.B3x/B4x; record {loc_3h}",
        status_of(ok_3h, sh_stored_ok),
        f"the quote states no masks; its source says 'on the random block masks' ({loc_3h}), i.e. B1x-B4x, where the pure blocks "
        f"B1x/B2x give +.008/-.002; the range holds on the two MIXED random block masks B3x/B4x only ({ck_3h34}). In the recon the "
        "referent is the first ROUND's label (e2a alternates labels round by round); 'first block's label' is PROPOSAL-k's wording, "
        "where Stage 1's R masks gave +.013/+.005/+.008. Correction: 'on the mixed random block masks B3x/B4x, toward the first "
        f"round's label'. The record's own figure check already states this scoping ({FC['B4_pseudo']})",
        domain=f"|mean| over B1x-B4x (the source's 'the random block masks', {loc_3h})",
        check=f"B1x-B4x: {ck_3h}; B3x/B4x: {ck_3h34}")
    REF_NOTES.append("3h: '±.02–.03 toward the first block's label' — in the recon the quantity is toward the START label (round 1's "
                     f"tag), and it is ±.02–.03 on the random block masks B3x (+.0265, 74/28) and B4x (-.0218, 37/65) only "
                     f"({loc(RE, 'B3x (r+ on round 1, the start label', after=RC_HDR)}); B1x/B2x are +.0077/-.0017, so the Stage C "
                     f"entry's 'on the random block masks' ({loc_3h}) covers two of the four. Under section 7's rule the row is "
                     "'discrepant (transcription)'. 'First block's "
                     f"label' is PROPOSAL-k's term ({loc(PK, 'label on the R masks (recon: ±.02–.03).')}); in PROPOSAL-k Stage 1 the "
                     "signed shift toward the first block's label on R+A/R+B/R++ was +.013/+.005/+.008. The note should say 'toward the "
                     "first round's label, on the mixed random block masks' for the recon figure. The record's own figure check already "
                     "states this: 'the pseudo-shift ±.02–.03 is the MIXED block masks B3x/B4x (+.027/−.022) toward the first ROUND's "
                     f"label — the pure-block masks B1x/B2x ... read +.008/−.002' ({FC['B4_pseudo']}); this audit's recomputation agrees with it.")
    ps3, ps4 = J["leak"]["signed"]["B:M3"], J["leak"]["signed"]["B:M4"]
    ck_3ib = [chk_single(ps3["mean"], "0.0161"), chk_single(ps4["mean"], "0.0076")]
    fig("3i-b", "leakage: the random-direction comparison (signed pseudo-shift, random analogs of M1/M2)",
        f"M3 {fs(ps3['mean'])} (sd {f4(ps3['sd'])}, {ps3['n_pos']}/{ps3['n_neg']}), M4 {fs(ps4['mean'])} (sd {f4(ps4['sd'])}, "
        f"{ps4['n_pos']}/{ps4['n_neg']}) toward the label whose rounds carried r+, n = 102",
        f"recomputed from stageB_reads.json; stored stageB_analysis*.json -> pseudo_shift.M3/M4; record {loc(RE, 'Signed pseudo-shift toward the r+ label (random masks): M3 mean +0.0161', after=RB_HDR)}",
        status_of(all(c[0] for c in ck_3ib), sh_stored_ok),
        "the block's quote carries no number; the row is checked against the record's M3 +0.0161 / M4 +0.0076",
        domain="M3, M4 (the record's), n = 102 sessions",
        check="M3: " + ck_3ib[0][1] + "; M4: " + ck_3ib[1][1])

    # ---- 3j PROPOSAL-k Stage 1 -------------------------------------------------
    w()
    w("### 3j. PROPOSAL-k Stage 1 figures (block: \"sign median .861 against the .90 bar; binding .88 -> .64\")")
    w()
    k_npz = sorted({r["npz"] for r in KR["per_session"].values()})
    k_tracked = set(git("ls-tree", "-r", "--name-only", PIN, "data/k").decode().split())
    k_npz_tracked = [p for p in k_npz if p in k_tracked]
    k_npz_local = [p for p in k_npz if os.path.exists(os.path.join(REPO, p))]     # existence only; no array is opened
    _abs_demo = os.path.join("/repo/data", "k", "/elsewhere/x.json")
    w("Re-implemented here from the stored per-layer probe values; `scripts/k1_analyze.py` was not run or imported. What binds: block "
      f"N3(i) asks for these figures 'From committed JSON' ({loc(BLOCK, '(i) From committed JSON: reproduce')}), and block rule 5 permits "
      f"probe refits only in N3(ii)-(iv) ({loc(BLOCK, '5. **No model inference in Tier 1**')}). k1_analyze.py's modes are `--selftest` "
      f"(a synthetic battery) and `--run`, its only non-synthetic mode, which re-loads the per-session residual arrays named in "
      f"k1_reads.json ({len(k_npz)} files `data/k/k1_resid_s*.npz`; tracked at {PIN}: {len(k_npz_tracked)}; present on this machine, "
      f"untracked: {len(k_npz_local)}; `load_stacks`, {loc(KA, 'z = np.load(os.path.join(REPO, r[\"npz\"]))')}) and refits every probe; "
      f"so running it would be a refit, which (i) does not ask for and rule 5 does not license. `data/k/k1_analysis.json` is its "
      "committed `--run` output, so reading its fields is reading the figures as k1_analyze.py produced them; the gate arithmetic "
      "of `gate_g1` / `gate_g3` is re-applied to them below. Secondary: `--run` writes "
      f"`os.path.join(DATA, \"k\", args.out_name)` ({loc('scripts/k1_analyze.py', 'path = os.path.join(DATA, \"k\", args.out_name)')}; "
      f"write at {loc('scripts/k1_analyze.py', 'json.dump(out, fh, indent=1, default=float)')}); an absolute `--out-name` would redirect "
      f"that write outside data/ (os.path.join discards the prefix: os.path.join('/repo/data', 'k', '/elsewhere/x.json') = "
      f"'{_abs_demo}'), so the write location alone would not have forbidden the run. Also secondary: k1_analyze.py inserts the "
      "repository into `sys.path` and imports "
      "`valence_core.k.analysis`, which in turn imports `valence_core.adapters.base`, `valence_core.e2d.habit`, "
      "`valence_core.e2d.config` (and through it `valence_core.session`), `valence_core.echo.probe` and `valence_core.stats`; this "
      "audit imports nothing from the repository. The two gate computations are small: a median of "
      "`auc_loso` over a band plus an every-layer above-null check "
      f"(`gate_g1`, {loc(KA, 'def gate_g1(')}; `gate_g3`, {loc(KA, 'def gate_g3(')}). Bars as stored in k1_analysis.json -> bars "
      f"and as registered ({loc(PK, '`M+A`/`M+B` rows. **PASS** iff the median AUC over L51–L61 is ≥ .90 at')}; "
      f"{loc(PK, 'the read position. **PASS** iff median AUC over L51–L62 ≥ .90 and above')}). The k arc's open questions are not touched.")
    w()
    KP = K["probes"]
    ev = K["evaluation"]
    g3 = KP["g3_firstsign_read_M"]; g1a = KP["g1_labelA_token_M"]; g1b = KP["g1_labelB_token_M"]; g2 = KP["g2_read_M"]
    g3_band = list(range(51, 63)); g1_band = list(range(51, 62)); g2_band = list(range(49, 64))
    g3_med = statistics.median(g3[str(l)]["auc_loso"] for l in g3_band)
    g1a_med = statistics.median(g1a[str(l)]["auc_loso"] for l in g1_band)
    g1b_med = statistics.median(g1b[str(l)]["auc_loso"] for l in g1_band)
    g3_above = all(g3[str(l)]["above_null"] for l in g3_band)
    g1a_above = all(g1a[str(l)]["above_null"] for l in g1_band)
    g1b_null = [l for l in g1_band if not g1b[str(l)]["above_null"]]
    g2_above = [l for l in g2_band if g2[str(l)]["above_null"]]
    g2_max = max(g2[str(l)]["auc_loso"] for l in g2_band)
    w(f"n = {K['n_sessions_valid']} valid sessions (of {K['n_sessions']} read; k1_reads.json n_sessions_without_first_choice = "
      f"{KR['n_sessions_without_first_choice']}, n_eligible_excluded_under_run_scope = {KR['n_eligible_excluded_under_run_scope']}), "
      f"2 rows per session (86), grouped LOSO, {K['n_shuffles']} shuffles; domain as stored: \"{ev['domain']}\".")
    w()
    w(f"- G3 (target 'the FIRST block carried +', rows M+A / M+B at the READ position): median over L51-L62 of `auc_loso` = "
      f"{g3_med:.6f} (stored evaluation.G3.median_auc {ev['G3']['median_auc']:.6f}; equal: {g3_med == ev['G3']['median_auc']}); "
      f"bar {K['bars']['G3'][0]}; above null at every band layer: {g3_above}; verdict stored {ev['G3']['verdict']}. "
      f"Per layer L50-L58 {f3(min(g3[str(l)]['auc_loso'] for l in range(50, 59)))}-{f3(max(g3[str(l)]['auc_loso'] for l in range(50, 59)))}, "
      f"L59-L63 {f3(min(g3[str(l)]['auc_loso'] for l in range(59, 64)))}-{f3(max(g3[str(l)]['auc_loso'] for l in range(59, 64)))}.")
    w(f"- G1 at label A's token (rows M+A v M+B): L51 {f3(g1a['51']['auc_loso'])}, L52 {f3(g1a['52']['auc_loso'])}, ..., L61 "
      f"{f3(g1a['61']['auc_loso'])} (L62 {f3(g1a['62']['auc_loso'])}, L63 {f3(g1a['63']['auc_loso'])}); median over L51-L61 = "
      f"{g1a_med:.6f} (stored {ev['G1']['median_auc_labelA']:.6f}); bar {K['bars']['G1'][0]}; above null at every band layer: {g1a_above}.")
    w(f"- G1 at label B's token: L51 {f3(g1b['51']['auc_loso'])}; median over L51-L61 = {g1b_med:.6f} (stored {ev['G1']['median_auc_labelB']:.6f}); "
      f"bar {K['bars']['G1'][1]}; band layers at or below null: {g1b_null}. G1 verdict stored {ev['G1']['verdict']}.")
    w(f"- G2 (binding at the READ position, L49-L63): layers above null {g2_above if g2_above else 'none'}; max {f3(g2_max)} "
      f"(stored {f3(ev['G2']['max_auc'])}); verdict stored {ev['G2']['verdict']}. Branch stored: {ev['branch']}.")
    w()
    rows = []
    for l in L_ALL:
        s = str(l)
        rows.append([l] + [f"{f3(KP[f][s]['auc_loso'])}{'*' if KP[f][s]['above_null'] else ''} / {f3(KP[f][s]['shuffle95'])}"
                           for f in ("g1_labelA_token_M", "g1_labelB_token_M", "g1_labelA_token_R_comparator", "g2_read_M",
                                     "g2_read_R_comparator", "g3_firstsign_read_M", "g3_firstsign_read_R_comparator")])
    w("Per layer, LOSO AUC (* above null) / null 95th percentile:")
    w()
    w.table(["layer", "G1 A token axis", "G1 B token axis", "A token random", "G2 read axis", "G2 read random", "G3 read axis", "G3 read random"], rows)
    fig("3j-a", "PROPOSAL-k Stage 1: sign median .861 against the .90 bar",
        f"{g3_med:.4f} (median of auc_loso over L51-L62) vs bar {K['bars']['G3'][0]}; above null at every band layer; G3 FAIL; "
        f"family g3_firstsign_read_M, read position, target = first block carried +, rows M+A/M+B, grouped LOSO, n = 43 valid sessions "
        f"(86 rows), 200 shuffles; includes <= 48? no",
        f"data/k/k1_analysis.json -> probes.g3_firstsign_read_M[L].auc_loso, evaluation.G3.median_auc; record {loc(RE, '.68–.71 at L59–L63 (median over the registered L51–L62 band .861', after=K1_HDR)}",
        status_of(chk_single(g3_med, ".861")[0] and K["bars"]["G3"][0] == 0.9),
        domain="median over L51-L62 (the registered G3 band, stored bars.G3)",
        check=f"{chk_single(g3_med, '.861')[1]}; bar stored {K['bars']['G3'][0]} against .90: {'holds' if K['bars']['G3'][0] == 0.9 else 'FAILS'}")
    ck_3jb = [chk_single(g1a["51"]["auc_loso"], ".88"), chk_single(g1a["61"]["auc_loso"], ".64")]
    fig("3j-b", "PROPOSAL-k Stage 1: binding .88 -> .64",
        f"label A's token {f3(g1a['51']['auc_loso'])} at L51 -> {f3(g1a['61']['auc_loso'])} at L61 (band end; L62 {f3(g1a['62']['auc_loso'])}); "
        f"median {g1a_med:.4f} vs bar .90; label B {f3(g1b['51']['auc_loso'])} at L51, median {g1b_med:.4f} vs .75; family g1_labelA_token_M, "
        "label A's token (read - 9), rows M+A v M+B, grouped LOSO, n = 43 (86 rows), 200 shuffles",
        f"data/k/k1_analysis.json -> probes.g1_labelA_token_M[L].auc_loso, evaluation.G1; record {loc(RE, 'against the .90 bar); the binding at label A', after=K1_HDR)}",
        status_of(all(c[0] for c in ck_3jb)),
        "'.88 -> .64' is label A's token only, L51 to L61 (the G1 band's end). The k masks are +/0 (M+A v M+B), the recon's are "
        f"+/-; the record's ledger slip (18) discusses the bars' calibration ({loc(RE, 'Design ledger slip (18), quoted from ADDENDUM-k1', after=K1_HDR)}); not adjudicated here",
        domain="label A's token at L51 and at L61 (the record's '.88 at L51 then .76 → .64'; L61 is the G1 band's end)",
        check="L51: " + ck_3jb[0][1] + "; L61: " + ck_3jb[1][1])
    J["3j"] = {"bars": K["bars"], "G3_median_recomputed": g3_med, "G1_labelA_median_recomputed": g1a_med,
               "G1_labelB_median_recomputed": g1b_med, "G2_layers_above_null": g2_above, "G2_max": g2_max,
               "stored_evaluation": {k: ev[k] for k in ("branch", "G1", "G2", "G3")}, "probes": KP}

    # ================================================================ (i-b)
    w("## 4. Part (i-b): the stored shuffled-label null, Stage C C1, from stageC_analysis.json")
    w()
    w(f"As stored: n_sessions {C['n_sessions']}, kfold {C['kfold']}, n_shuffles {C['n_shuffles']}; procedure: \"{C['procedure']}\". "
      "Three M1 v M2 families (rows M1 and M2, 2 per session, 204 rows), one per capture position; target at label_x's position = "
      "+1 iff label_x's rounds carried + under the mask; at the read, label_a's target. 'null95' = the 95th percentile of the 200 "
      "label-shuffled 10-fold AUCs on the same folds; LOSO has no null of its own.")
    w()
    rows = []
    for l in L_ALL:
        s = str(l)
        rows.append([l, f"{f3(la[s]['auc_kfold'])}{'*' if la[s]['above_null'] else ''}", f3(la[s]["shuffle95"]), f3(la[s]["auc_loso"]),
                     f"{f3(lb[s]['auc_kfold'])}{'*' if lb[s]['above_null'] else ''}", f3(lb[s]["shuffle95"]), f3(lb[s]["auc_loso"]),
                     f"{f3(rd[s]['auc_kfold'])}{'*' if rd[s]['above_null'] else ''}", f3(rd[s]["shuffle95"]), f3(rd[s]["auc_loso"])])
    w.table(["layer", "label_a 10-fold", "label_a null95", "label_a LOSO", "label_b 10-fold", "label_b null95", "label_b LOSO",
             "read 10-fold", "read null95", "read LOSO"], rows)
    # raw-text comparison
    tables = {}
    cur = None
    for line in rawC.splitlines():
        m = re.match(r"\s*C1 BINDING at the (\w+) position", line)
        if m:
            cur = m.group(1); tables[cur] = {}; continue
        if line.strip().startswith("C2 BLOCK"):
            cur = "C2"; tables[cur] = {}; continue
        m = re.match(r"\s+(\d+)\s+(.*)$", line)
        if cur and m and m.group(1).isdigit() and int(m.group(1)) in L_ALL:
            cells = re.findall(r"(\d\.\d{3})/(\d\.\d{2})(\*?)", m.group(2))
            if cells:
                tables[cur][int(m.group(1))] = cells
    fam_of = {"read": ["c1_read_M1M2", "c1_read_M3M4_random", "c1_read_TEXTONLY_shadow"],
              "label_a": ["c1_label_a_M1M2", "c1_label_a_M3M4_random", "c1_label_a_TEXTONLY_shadow"],
              "label_b": ["c1_label_b_M1M2", "c1_label_b_M3M4_random", "c1_label_b_TEXTONLY_shadow"],
              "C2": ["c2_firstsign_B1-4", "c2_firstsign_B1-4x_random", "c2_lastsign_B1-4", "c2_lastsign_B1-4x_random"]}
    n_cells = 0; raw_mism = []
    for t, fams in fam_of.items():
        for l in L_ALL:
            cells = tables.get(t, {}).get(l)
            if cells is None or len(cells) != len(fams):
                raw_mism.append((t, l, "row missing")); continue
            for (a, nl, star), fname in zip(cells, fams):
                n_cells += 1
                e = C["families"][fname][str(l)]
                if f"{e['auc_kfold']:.3f}" != a or f"{e['shuffle95']:.2f}" != nl or (star == "*") != bool(e["above_null"]):
                    raw_mism.append((fname, l, a, nl, star, e["auc_kfold"], e["shuffle95"], e["above_null"]))
    m_lp = re.search(r"label positions: label_a (\d+)-(\d+) tokens before the read, label_b (\d+)-(\d+)", rawC)
    lp_raw_ok = bool(m_lp) and (int(m_lp.group(1)), int(m_lp.group(2)), int(m_lp.group(3)), int(m_lp.group(4))) == (
        lpd["label_a"]["min"], lpd["label_a"]["max"], lpd["label_b"]["min"], lpd["label_b"]["max"])
    w(f"JSON vs `results/raw/2026-09-06_recon_echo_stageC_analysis.txt` (the 13 families' tables, AUC at 3 decimals, null at 2, the star): "
      f"{n_cells} cells compared, {len(raw_mism)} disagreements{': ' + str(raw_mism[:10]) if raw_mism else ''}; the raw's label-position line "
      f"agrees with the JSON: {lp_raw_ok}. The raw's header line 'grouped 10-fold, 200 shuffles' "
      f"({loc('results/raw/2026-09-06_recon_echo_stageC_analysis.txt', 'probes done in')}) agrees with the stored kfold/n_shuffles.")
    w()
    # series ranges
    def nrange(f, layers):
        v = [f[str(l)]["shuffle95"] for l in layers]
        return min(v), max(v), statistics.fmean(v), statistics.median(v)
    rows = []
    J["i_b"] = {"families": {}, "null_ranges": {}}
    for name, f in (("c1_label_a_M1M2", la), ("c1_label_b_M1M2", lb), ("c1_read_M1M2", rd)):
        for lab, layers in (("all 18 (L40-L63)", L_ALL), ("L49-L63", L_ABOVE), ("L51-L63", list(range(51, 64)))):
            lo, hi, mean, med = nrange(f, layers)
            rows.append([name, lab, f"{lo:.4f}", f"{hi:.4f}", f"{mean:.4f}", f"{med:.4f}"])
            J["i_b"]["null_ranges"][f"{name}|{lab}"] = [lo, hi, mean, med]
        J["i_b"]["families"][name] = f
    w("Shuffle-95 null, per family:")
    w()
    w.table(["family", "layers", "min null95", "max null95", "mean", "median"], rows)
    all_nulls = [f[str(l)]["shuffle95"] for f in (la, lb, rd) for l in L_ALL]
    la_51_62 = rng_of(la, range(51, 63)); la_51_63 = rng_of(la, range(51, 64))
    lb_51_63 = rng_of(lb, range(51, 64))
    rd_below = all(rd[str(l)]["auc_kfold"] < rd[str(l)]["shuffle95"] for l in L_ALL)
    rd_margin = min(rd[str(l)]["shuffle95"] - rd[str(l)]["auc_kfold"] for l in L_ABOVE)
    # ---- the four series, each checked by section 7's rule on its domain(s)
    L51_63 = list(range(51, 64))
    nul = lambda layers: [f[str(l)]["shuffle95"] for f in (la, lb, rd) for l in layers]
    ok_n18, ck_n18 = chk_range(nul(L_ALL), ".57", ".59")
    ok_n49, ck_n49 = chk_range(nul(L_ABOVE), ".57", ".59")
    ok_n51, ck_n51 = chk_range(nul(L51_63), ".57", ".59")
    n_over = [(nm, l, f"{f[str(l)]['shuffle95']:.4f}") for nm, f in (("label_a", la), ("label_b", lb), ("read", rd))
              for l in L_ALL if qr(f[str(l)]["shuffle95"], ".59") > _dec(".59") or qr(f[str(l)]["shuffle95"], ".57") < _dec(".57")]
    # per family, per domain (R2: F1 plots several series and its band does not say which; F1 is not on this machine)
    fam_ck = {}
    for nm, f in (("label_a", la), ("label_b", lb), ("read", rd)):
        for dn, layers in (("all 18", L_ALL), ("L49-L63", L_ABOVE), ("L51-L63", L51_63)):
            fam_ck[(nm, dn)] = chk_range([f[str(l)]["shuffle95"] for l in layers], ".57", ".59")
    over_by_fam = {nm: [l for (n_, l, _) in n_over if n_ == nm] for nm in ("label_a", "label_b", "read")}
    loc_4402 = loc(RE, ".50–.55 against nulls .57–.60", after=RC_HDR)
    # the record's '.57–.60' is stated for the READ position's nulls ('At the read position the pole of label_a stays null —
    # .50–.55 against nulls .57–.60'); compare it with the pooled range it is used for here
    _rdn18 = [rd[str(l)]["shuffle95"] for l in L_ALL]
    _rd4, _pool4 = (f"{min(_rdn18):.4f}", f"{max(_rdn18):.4f}"), (f"{min(all_nulls):.4f}", f"{max(all_nulls):.4f}")
    _rd2_ok = chk_range(_rdn18, ".57", ".60")[0]; _pool2_ok = chk_range(all_nulls, ".57", ".60")[0]
    rec_read_eq_pooled = ("at four decimals" if _rd4 == _pool4 else ("at two decimals" if _rd2_ok and _pool2_ok else None))
    rec5760_paren = (f"the record's figure for the read nulls, {loc_4402}, "
                     + (f"which equals the pooled range {rec_read_eq_pooled}: read {_rd4[0]}-{_rd4[1]}, pooled {_pool4[0]}-{_pool4[1]}, "
                        "all 18 layers" if rec_read_eq_pooled else
                        f"which is NOT the pooled range: read {_rd4[0]}-{_rd4[1]}, pooled {_pool4[0]}-{_pool4[1]}, all 18 layers"))
    rec5760 = f"'.57–.60' ({rec5760_paren})"
    # the record's Stage C tables (one per position) print every C1 M1vM2 family's null per layer at two decimals: parse them
    _tabs = {}
    for nm, hdr in (("read", "**At the read position** (Stage B's (b) re-run"), ("label_a", "**At label_a's token** (the first-listed"),
                    ("label_b", "**At label_b's token** (the second-listed")):
        _lt = loc(RE, hdr, after=RC_HDR)
        _rows = {}
        if not _lt.endswith("NOT-FOUND"):
            _i0 = int(_lt.rsplit(":", 1)[1])
            for _ln in _lines[RE][_i0:_i0 + 25]:
                _m = re.match(r"\s*\| (\d+) \| [0-9.]+\*? \| ([0-9.]+) \|", _ln)
                if _m and int(_m.group(1)) in L_ALL:
                    _rows[int(_m.group(1))] = _m.group(2)
        _fam = {"read": rd, "label_a": la, "label_b": lb}[nm]
        _agree = sum(1 for l, v in _rows.items() if f"{_fam[str(l)]['shuffle95']:.2f}" == v)
        _tabs[nm] = {"locator": _lt, "n_rows": len(_rows), "agree_with_json_2dp": _agree,
                     "min": min(_rows.values(), key=float) if _rows else None, "max": max(_rows.values(), key=float) if _rows else None}
    rec_tables = "; ".join(f"{nm} {t['min']}–{t['max']} ({t['locator']}, {t['n_rows']} layers, {t['agree_with_json_2dp']}/{t['n_rows']} equal "
                           "to the JSON at two decimals)" for nm, t in _tabs.items())
    J.setdefault("i_b", {})["record_57_60"] = {"locator": loc_4402, "record_scope": "the read position's nulls",
                                               "record_tables_null_95th": _tabs,
                                               "read_null95_all18": [min(_rdn18), max(_rdn18)],
                                               "pooled_null95_all18": [min(all_nulls), max(all_nulls)],
                                               "read_equals_pooled": rec_read_eq_pooled or "no",
                                               "read_rounds_to_57_60": _rd2_ok, "pooled_rounds_to_57_60": _pool2_ok}
    v_la = lambda layers: [la[str(l)]["auc_kfold"] for l in layers]
    v_lb = lambda layers: [lb[str(l)]["auc_kfold"] for l in layers]
    v_rd = lambda layers: [rd[str(l)]["auc_kfold"] for l in layers]
    ok_b1, ck_b1 = chk_central(v_la(L51_63), "1.0")
    ok_b1e, ck_b1e = chk_range(v_la(L51_63), "1.0", "1.0")
    ok_b1_49, ck_b1_49 = chk_central(v_la(L_ABOVE), "1.0")
    ok_b2, ck_b2 = chk_range(v_lb(L_ABOVE), ".81", ".96")
    ok_b2_51, ck_b2_51 = chk_range(v_lb(L51_63), ".81", ".96")
    ok_r, ck_r = chk_range(v_rd(L_ABOVE), ".50", ".55")
    ok_r18, ck_r18 = chk_range(v_rd(L_ALL), ".50", ".55")
    ok_r51, ck_r51 = chk_range(v_rd(L51_63), ".50", ".55")
    ok_c, ck_c = chk_central([rd[str(l)]["shuffle95"] for l in L_ABOVE], ".58")
    ok_c18, ck_c18 = chk_central([rd[str(l)]["shuffle95"] for l in L_ALL], ".58")
    ck_cevery = chk_range([rd[str(l)]["shuffle95"] for l in L_ABOVE], ".58", ".58")[1]
    w("F1's four series, confirmed from the JSON and checked by section 7's rule (the domain is the quote's; F1 itself is not on this "
      "machine, so where the quote states no layers the check is over L49-L63, the stored layers above the steering layer, with the "
      "other domains beside):")
    w()
    w(f"1. **Shuffle-95 null 'at ≈ .57–.59 across layers'** -- the stored 200-draw 95th, by domain. Three families pooled: "
      f"L49-L63 {ck_n49}; all 18 {ck_n18}; L51-L63 {ck_n51}. Per family: "
      + "; ".join(f"{nm} " + ", ".join(f"{dn} {fam_ck[(nm, dn)][1]}" for dn in ("all 18", "L49-L63", "L51-L63")) for nm in ("label_a", "label_b", "read"))
      + f". The (family, layer) cells whose null rounds outside .57-.59 at two decimals: {n_over}. 'Across layers' is F1's plotted "
      "domain, and F1 is not on this machine, so neither its layer range nor which family's null it draws is known here; the block's "
      "own description of the same panel ('≈ 1.0 from L51 on') implies, but does not say, that F1 plots layers below L51. Under a "
      f"pooled band the quote holds only if F1 omits L{', L'.join(str(l) for l in sorted({l for (_, l, _) in n_over}))}; "
      + ("for label_a's null alone it holds at every layer" if not over_by_fam["label_a"]
         else f"for label_a's alone only if F1 omits L{', L'.join(str(l) for l in over_by_fam['label_a'])}")
      + f"; for the read's alone only if F1 omits L{', L'.join(str(l) for l in over_by_fam['read'])}; for label_b's alone only if "
      f"F1 omits L{', L'.join(str(l) for l in over_by_fam['label_b'])}. The record's own prose gives the read nulls as '.57–.60' ({loc_4402}).")
    w(f"2. **Binding at the first label '≈ 1.0 from L51 on'** (domain stated, L51-L63): {ck_b1}; every value: {ck_b1e}. "
      f"{f4(la_51_62[0])}-{f4(la_51_62[1])} over L51-L62; L63 {f4(la['63']['auc_kfold'])}; L49 {f4(la['49']['auc_kfold'])}, "
      f"L50 {f4(la['50']['auc_kfold'])} (outside the stated domain).")
    w(f"3. **Binding at the second label '.81–.96'** (no layers in its own clause): L49-L63 {ck_b2}; L51-L63 {ck_b2_51}. "
      f"{f4(lb_51_63[0])} ({Ls(lb_51_63[2])}) to {f4(lb_51_63[1])} ({Ls(lb_51_63[3])}) over L51-L63; L49/L50 "
      f"{f4(lb['49']['auc_kfold'])}/{f4(lb['50']['auc_kfold'])} (not above null). The range holds if the first clause's 'from L51 on' "
      "governs this clause too; the block's wording does not say so.")
    w(f"4. **Choice read '.50–.55'** (no layers): L49-L63 {ck_r}; all 18 {ck_r18}; (L51-L63 alone: {ck_r51}). "
      f".500 exactly at L40/L44/L48 by construction; below its own null at every one of 18 layers: {rd_below}; smallest gap "
      f"(null95 - AUC) above L48 = {rd_margin:.4f}.")
    w()
    w("The note's link-3 sentence, value by value (the block quotes it with elisions, line 44, and the note is not on this machine, "
      "so a layer range in the elided text cannot be seen; each part is checked on L49-L63 and on L51-L63):")
    w()
    rd_null = nrange(rd, L_ALL)
    sent_rows = [
        ["'≈ 1.0 at the first label'", f"{f4(la_51_62[0])}-{f4(la_51_62[1])} at L51-L62 (L63 {f3(la['63']['auc_kfold'])}; "
         f"L49/L50 {f3(la['49']['auc_kfold'])}/{f3(la['50']['auc_kfold'])}); 10-fold, c1_label_a_M1M2",
         f"L51-L63: {ck_b1}; L49-L63: {ck_b1_49}. Holds from L51; needs 'from L51' unless the elided text carries it"],
        ["'.81–.96 at the second'", f"{f3(lb_51_63[0])}-{f3(lb_51_63[1])} at L51-L63; 10-fold, c1_label_b_M1M2",
         f"L51-L63: {ck_b2_51}; L49-L63: {ck_b2}. Holds from L51; needs 'from L51' unless the elided text carries it"],
        ["(the choice read)", f"{f3(r_lo)}-{f3(r_hi)} at L49-L63; c1_read_M1M2", f"below its null at all 18 layers: {rd_below}"],
        ["'below the shuffled-label 95th percentile of ≈ .58'",
         f"read family's null95 {rd_null[0]:.4f}-{rd_null[1]:.4f} (mean {rd_null[2]:.4f}, median {rd_null[3]:.4f}) over the 18 layers",
         f"L49-L63: {ck_c}; all 18: {ck_c18}. A per-layer null between .566 and .597, not one number; each layer rounded: {ck_cevery}"],
    ]
    w.table(["sentence part", "value from the JSON (layers)", "check (section 7's rule)"], sent_rows)
    STORED_IB = not raw_mism   # the four series are read from stored fields; the raw text F1 reads agrees cell for cell
    _fr = lambda f, layers: f"{min(f[str(l)]['shuffle95'] for l in layers):.4f}-{max(f[str(l)]['shuffle95'] for l in layers):.4f}"
    fig("ib-1", "F1 link-3 'shuffle-95 null' ≈ .57-.59 across layers",
        f"the stored 200-draw 95th, by domain. Pooled over the three C1 M1vM2 families: L49-L63 {min(nul(L_ABOVE)):.4f}-{max(nul(L_ABOVE)):.4f}; "
        f"all 18 {min(nul(L_ALL)):.4f}-{max(nul(L_ALL)):.4f}; L51-L63 {min(nul(L51_63)):.4f}-{max(nul(L51_63)):.4f}. Per family (all 18 / L49-L63 / "
        f"L51-L63): label_a {_fr(la, L_ALL)} / {_fr(la, L_ABOVE)} / {_fr(la, L51_63)}; label_b {_fr(lb, L_ALL)} / {_fr(lb, L_ABOVE)} / "
        f"{_fr(lb, L51_63)}; read {_fr(rd, L_ALL)} / {_fr(rd, L_ABOVE)} / {_fr(rd, L51_63)}; grouped 10-fold, 102 sessions, 200 shuffles, "
        "per (family, layer); includes <= 48? yes if F1 plots L40-L48 (those layers' nulls are real nulls on state-free rows)",
        f"data/echo/stageC_analysis.json -> families.c1_{{label_a,label_b,read}}_M1M2[L].shuffle95; record prose '.57–.60' for the read "
        f"position's nulls ({loc_4402})",
        status_of(ok_n49 and ok_n18, STORED_IB),
        "the band rounds outside .57-.59 only at "
        + ", ".join(f"{nm} L{l} {v}" for nm, l, v in n_over)
        + "; '.57–.59' is label_a's range at every layer and the pooled range on L51-L63. Correction: '.57–.60' across layers "
        f"(exact {min(all_nulls):.3f}-{max(all_nulls):.3f}; {rec5760_paren}), or '.57–.59' if F1 draws label_a's null "
        "alone or starts at L51. The record's prose gives a null range for the read position only; its Stage C tables print each "
        f"family's null per layer at two decimals: {rec_tables}. N3c's status for the same figure is compared in section 11",
        domain="F1's plotted layers and series ('across layers'; F1 not on this machine); per R2, the three plotted C1 families pooled, "
               "on L49-L63 and all 18, L51-L63 and each family beside",
        check=f"pooled L49-L63: {ck_n49}; pooled all 18: {ck_n18}; pooled L51-L63: {ck_n51}; label_a all 18: {fam_ck[('label_a', 'all 18')][1]}; "
              f"read all 18: {fam_ck[('read', 'all 18')][1]}; label_b all 18: {fam_ck[('label_b', 'all 18')][1]}",
        condition=("on what F1 plots, which is not checkable here: reproduced if F1's band is label_a's null alone "
                   f"({fam_ck[('label_a', 'all 18')][1].split(': ')[-1]} over all 18); discrepant (transcription) if the band pools the families, "
                   f"or is the read's and F1 plots L{', L'.join(str(l) for l in over_by_fam['read'])}, or is label_b's and F1 plots "
                   f"L{' or L'.join(str(l) for l in over_by_fam['label_b'])}. Status of record here: discrepant (transcription), the pooled reading"))
    fig("ib-2", "F1 binding at the first label ≈ 1.0 from L51 on",
        f"{f4(la_51_62[0])}-{f4(la_51_62[1])} at L51-L62; L63 {f4(la['63']['auc_kfold'])} (c1_label_a_M1M2, M1 v M2 rows, label_a's token = read - 9, "
        "grouped 10-fold, 102 sessions, 200 shuffles)",
        "data/echo/stageC_analysis.json -> families.c1_label_a_M1M2[L].auc_kfold", status_of(ok_b1, STORED_IB),
        "≈ 1.0 through L62; L63 .988",
        domain="L51-L63 (the quote's 'from L51 on')", check=f"{ck_b1}; every value: {ck_b1e}")
    fig("ib-3", "F1 binding at the second label .81-.96",
        f"{f3(lb_51_63[0])}-{f3(lb_51_63[1])} at L51-L63; L49/L50 {f3(lb['49']['auc_kfold'])}/{f3(lb['50']['auc_kfold'])} "
        "(c1_label_b_M1M2, M1 v M2 rows, label_b's token = read - 7, grouped 10-fold, 102 sessions, 200 shuffles)",
        "data/echo/stageC_analysis.json -> families.c1_label_b_M1M2[L].auc_kfold", status_of(ok_b2, STORED_IB),
        "holds on L51-L63; the clause states no layers of its own, and at L49/L50 the second-label binding is .53-.54 (not above "
        "null). Correction: 'from L51' on this series too, unless the first clause's 'from L51 on' is meant to cover it",
        domain="L49-L63 (the clause states no layers); L51-L63 beside",
        check=f"L49-L63: {ck_b2}; L51-L63: {ck_b2_51}")
    fig("ib-4", "F1 binding at the choice read .50-.55",
        f"{f3(r_lo)}-{f3(r_hi)} at L49-L63; .500 at L40/44/48 by construction; below null at all 18 layers (c1_read_M1M2, M1 v M2 rows, "
        "read position, grouped 10-fold, 102 sessions, 200 shuffles)",
        "data/echo/stageC_analysis.json -> families.c1_read_M1M2[L].auc_kfold", status_of(ok_r and ok_r18, STORED_IB),
        f"on L51-L63 alone the series is .53-.55 ({ck_r51}); relevant only if 'from L51 on' were read as governing this clause",
        domain="L49-L63 (no layers stated); all 18 beside",
        check=f"L49-L63: {ck_r}; all 18: {ck_r18}")
    fig("ib-5", "link-3 sentence: 'below the shuffled-label 95th percentile of ≈ .58'",
        f"read null95 {rd_null[0]:.3f}-{rd_null[1]:.3f}, mean {rd_null[2]:.3f}; read AUC below it at every layer (min gap {rd_margin:.3f} above L48); "
        "c1_read_M1M2, grouped 10-fold, 102 sessions, 200 shuffles",
        "data/echo/stageC_analysis.json -> families.c1_read_M1M2[L].{auc_kfold,shuffle95}", status_of(ok_c and ok_c18 and rd_below, STORED_IB),
        f"a single '≈ .58' for a per-layer series (section 7, R1): its mean and median round to .58; the per-layer null is "
        f".566-.597, so under an every-layer reading it would fail ({ck_cevery}); the sentence's claim that the read AUC is below "
        "the null holds at every layer either way",
        domain="the read family's per-layer null, L49-L63; all 18 beside",
        check=f"L49-L63: {ck_c}; all 18: {ck_c18}; read AUC below its null at all 18 layers: {rd_below}")
    J["i_b"]["raw_text_comparison"] = {"cells": n_cells, "disagreements": raw_mism, "label_position_line_agrees": lp_raw_ok}
    if raw_mism:
        REF_NOTES.append(f"(i-b): the raw text disagrees with the JSON at {len(raw_mism)} cells; the JSON is used: {raw_mism[:10]}")

    # ================================================================ (v)
    w("## 5. Part (v): random-direction control for the binding read")
    w()
    w("**What the random arms are.** There are NO random-direction SESSIONS in the recon set: Stages A-C read only the valid e2a "
      f"reward-arm sessions (section 1; e2a's random1 / random2 sessions, {arm_counts.get('random1', 0)} and {arm_counts.get('random2', 0)} valid, were not read). "
      "The random-direction control is a set of MASKS re-forwarded over the same 102 reward-arm texts: M3 / M4 inject the "
      f"norm-matched random direction `{cfg['random_direction']}` (sha16 `{cfg['random_direction_sha']}`, alpha {cfg['alpha']:.4f} at L{cfg['layer']}, "
      "equal norm to the axis injection asserted) with M1's / M2's sign pattern over the same four forced-round spans. The C1 random "
      "families take the same target with r+ as '+' (stored: \"" + C["targets"]["*_M3M4_random"] + "\"). The text-only families are "
      "the shadow rows (mask off, no injection), one row per session, with the as-generated target (stored: \""
      + C["targets"]["*_TEXTONLY_shadow"] + "\"); they are not paired, so their AUCs are not .5 by construction at any layer.")
    w()
    rows = []
    J["v"] = {"families": {}}
    for l in L_ALL:
        s = str(l)
        r_ = [l]
        for pn in ("label_a", "label_b", "read"):
            fr = C["families"][f"c1_{pn}_M3M4_random"]; ft = C["families"][f"c1_{pn}_TEXTONLY_shadow"]
            r_ += [f"{f3(fr[s]['auc_kfold'])}{'*' if fr[s]['above_null'] else ''} / {f3(fr[s]['shuffle95'])} / {f3(fr[s]['auc_loso'])}",
                   f"{f3(ft[s]['auc_kfold'])}{'*' if ft[s]['above_null'] else ''} / {f3(ft[s]['shuffle95'])} / {f3(ft[s]['auc_loso'])}"]
        rows.append(r_)
    w("Per layer, 10-fold AUC (* above null) / null95 / LOSO; 102 sessions; random families 204 rows (M3, M4), text-only 102 rows (shadow):")
    w()
    w.table(["layer", "label_a random", "label_a text-only", "label_b random", "label_b text-only", "read random", "read text-only"], rows)
    for pn in ("label_a", "label_b", "read"):
        for kind in ("M3M4_random", "TEXTONLY_shadow"):
            J["v"]["families"][f"c1_{pn}_{kind}"] = C["families"][f"c1_{pn}_{kind}"]
    ra = C["families"]["c1_label_a_M3M4_random"]; rb = C["families"]["c1_label_b_M3M4_random"]; rr_ = C["families"]["c1_read_M3M4_random"]
    t_above = [(pn, l) for pn in ("label_a", "label_b", "read") for l in L_ALL if C["families"][f"c1_{pn}_TEXTONLY_shadow"][str(l)]["above_null"]]
    t_cells = 3 * len(L_ALL)
    tmax_above50 = max(C["families"][f"c1_{pn}_TEXTONLY_shadow"][str(l)]["auc_kfold"] for pn in ("label_a", "label_b", "read") for l in range(51, 64))
    w(f"- Random, label_a: {f3(ra['51']['auc_kfold'])}/{f3(ra['52']['auc_kfold'])} at L51/L52 ({f4(ra['51']['auc_kfold'])}/{f4(ra['52']['auc_kfold'])}), "
      f"{f3(ra['53']['auc_kfold'])} at L53, {f3(rng_of(ra, range(54, 64))[0])}-{f3(rng_of(ra, range(54, 64))[1])} at L54-L63; "
      f"L49/L50 {f3(ra['49']['auc_kfold'])}/{f3(ra['50']['auc_kfold'])}; above null at {sum(ra[str(l)]['above_null'] for l in L_ABOVE)}/15 layers L49-L63.")
    w(f"- Random, label_b: {f3(rb['51']['auc_kfold'])}/{f3(rb['52']['auc_kfold'])} at L51/L52, {f3(rng_of(rb, range(53, 64))[0])}-{f3(rng_of(rb, range(53, 64))[1])} at L53-L63; "
      f"above null at {sum(rb[str(l)]['above_null'] for l in L_ABOVE)}/15.")
    w(f"- Random, read: {f3(rng_of(rr_, L_ABOVE)[0])}-{f3(rng_of(rr_, L_ABOVE)[1])} at L49-L63; above null at {sum(rr_[str(l)]['above_null'] for l in L_ALL)}/18.")
    w(f"- Text-only: above its null at {len(t_above)} of {t_cells} (position, layer) cells {t_above}; the largest text-only AUC above L50 is {f3(tmax_above50)}.")
    bc = Bs["families"]["bc_labelpole_M3M4_random"]
    w(f"- Stage B's random comparator for the read-position binding (`bc_labelpole_M3M4_random`): {f3(rng_of(bc, L_ABOVE)[0])}-{f3(rng_of(bc, L_ABOVE)[1])} at L49-L63, "
      f"above null at {sum(bc[str(l)]['above_null'] for l in L_ALL)}/18.")
    w(f"- PROPOSAL-k Stage 1 random comparators (R+A / R+B, LOSO, n = 43): label A's token median over L51-L61 "
      f"{statistics.median(KP['g1_labelA_token_R_comparator'][str(l)]['auc_loso'] for l in g1_band):.4f}, label B's "
      f"{statistics.median(KP['g1_labelB_token_R_comparator'][str(l)]['auc_loso'] for l in g1_band):.4f}; read position max "
      f"{f3(max(KP['g2_read_R_comparator'][str(l)]['auc_loso'] for l in g2_band))}, above null at "
      f"{[l for l in g2_band if KP['g2_read_R_comparator'][str(l)]['above_null']] or 'no layer'}.")
    w()
    # the record's random-binding figures (Stage C body): 1.000 at L51-L52 and .83-.90 from L54 at label_a; .93 / .86 at L51-L52
    # and .69-.80 after at label_b; the read's random .50-.51
    _v = lambda f, layers: [f[str(l)]["auc_kfold"] for l in layers]
    ck_v1 = []
    for lab, (ok_, txt) in (("label_a L51 '1.000'", chk_single(ra["51"]["auc_kfold"], "1.000")),
                            ("label_a L52 '1.000'", chk_single(ra["52"]["auc_kfold"], "1.000")),
                            ("label_a L54-L63 '.83–.90'", chk_range(_v(ra, range(54, 64)), ".83", ".90")),
                            ("label_b L51 '.93'", chk_single(rb["51"]["auc_kfold"], ".93")),
                            ("label_b L52 '.86'", chk_single(rb["52"]["auc_kfold"], ".86")),
                            ("label_b L53-L63 '.69–.80'", chk_range(_v(rb, range(53, 64)), ".69", ".80")),
                            ("read L49-L63 'random .50–.51'", chk_range(_v(rr_, L_ABOVE), ".50", ".51"))):
        ck_v1.append((ok_, f"{lab}: {txt}"))
    ok_v1 = all(o for o, _ in ck_v1)
    fig("v-1", "random-direction control for the binding read (label tokens and read), per layer",
        f"label_a random {f3(ra['51']['auc_kfold'])}/{f3(ra['52']['auc_kfold'])} at L51/L52, {f3(ra['53']['auc_kfold'])} at L53, "
        f"{f3(rng_of(ra, range(54, 64))[0])}-{f3(rng_of(ra, range(54, 64))[1])} at L54-L63; "
        f"label_b random {f3(rb['51']['auc_kfold'])} at L51, {f3(rb['52']['auc_kfold'])} at L52, "
        f"{f3(rng_of(rb, range(53, 64))[0])}-{f3(rng_of(rb, range(53, 64))[1])} at L53-L63; "
        f"read random {f3(rng_of(rr_, L_ABOVE)[0])}-{f3(rng_of(rr_, L_ABOVE)[1])} at L49-L63, never above null; text-only above null at "
        f"{len(t_above)}/{t_cells} cells; families c1_*_M3M4_random and c1_*_TEXTONLY_shadow, grouped 10-fold, 102 sessions, 200 shuffles",
        "data/echo/stageC_analysis.json -> families.c1_{label_a,label_b,read}_{M3M4_random,TEXTONLY_shadow}[L]"
        f"; record {loc(RE, '1.000 at L51–L52 at label_a and .83–.90 from L54 on', after=RC_HDR)}",
        status_of(ok_v1),
        "the random arms are masks on the reward-arm texts, not random-direction sessions; the random direction's binding is read at "
        "the label tokens too (not axis-specific in presence) and, like the axis's, not at the read",
        domain="L49-L63 per series (all 18 in section 5's table); the record's sentence names L51-L52, 'from L54 on' (label_a) and "
               "'after' L52 (label_b, i.e. L53-L63)",
        check="block line 48 asks for a report (no quoted value); the record's random-binding figures checked: " + "; ".join(c for _, c in ck_v1))
    REF_NOTES.append("Referent availability: the note (RESEARCH-NOTE-v0_2-draft.md) and the F1/F2 SVGs are not on this machine "
                     "(results/raw/2026-10-08_note-preflight.md, N1 rows, MISSING). Every 'figure as written' in this raw is the block's "
                     "quotation of it (AUDIT-note-release-v1_2.md lines 43-44), not the note's own text; a figure the note words "
                     "differently is not checked here.")
    REF_NOTES.append("(v): the block asks for 'the random-direction sessions, if those exist in the recon set'. They do not: the recon "
                     "read only e2a's valid reward-arm sessions. The random-direction control exists as masks (M3/M4 in Stages A-C, "
                     "M5x/M6x and R1x-R4x in B, B1x-B4x in C) over the same texts; section 5 reports those.")

    # ================================================================ misc
    w("## 6. Other referents read")
    w()
    w(f"- `data/echo/timing.json`: session {TM['session']}, {TM['n_tokens_first_choice_prefix']} tokens in its first-choice prefix, "
      f"{TM['n_tokens_full']} in the full session; no N3 figure rides on it.")
    a_reg = [A["per_layer"][str(l)]["auc_reward_M1vM2"] for l in L_ABOVE]
    a_reg_above = [l for l in L_ABOVE if A["per_layer"][str(l)]["reward_above_shuffle95"]]
    ok_areg, ck_areg = chk_range(a_reg, ".42", ".51")
    loc_areg = loc(RE, 'polarity is NOT readable above null at any layer (AUC .42–.51 above 48;', after=RA_HDR)
    p2_layers = sorted(int(l) for l in Aph2["per_layer"])
    p2_49 = [Aph2["per_layer"][str(l)]["auc_reward_labelpole"] for l in L_ABOVE]
    p2_all = [Aph2["per_layer"][str(l)]["auc_reward_labelpole"] for l in p2_layers]
    p2_above = [l for l in p2_layers if Aph2["per_layer"][str(l)]["reward_above_shuffle95"]]
    bal = Aph2["label_a_is_tag_plus_balance"]
    w(f"- Stage A registered readout (stageA_analysis.json -> per_layer.auc_reward_M1vM2; probe as stored: \"{A['probe']}\"; "
      f"{A['n_sessions']} sessions, 2 rows each at the read position, {A['n_shuffles']}-shuffle LOSO null): "
      f"{f4(min(a_reg))}-{f4(max(a_reg))} at L49-L63, above null at {a_reg_above or 'no layer'}. The Stage A entry's '.42–.51 above 48' "
      f"({loc_areg}): {ck_areg}."
      + ("" if ok_areg else f" The minimum {f4(min(a_reg))} rounds to {qr(min(a_reg), '.42')} at two decimals, so the entry's lower "
         "endpoint is off in the second decimal; a record-wording note, not a block figure.")
      + (" The entry's claim that the polarity is not readable above null at any layer holds." if not a_reg_above
         else " The entry's claim that the polarity is not readable above null at any layer FAILS at the layers listed."))
    w(f"- Stage A post-hoc #2 (stageA_posthoc2_labelpole.json -> per_layer.auc_reward_labelpole; rule-11 post-hoc, as stored: "
      f"\"{Aph2['rule_11']}\"; target = the pole of label_a under the mask, +1 iff label_a's rounds carried + (M1: label_a == tag_plus; "
      f"M2: the reverse); M1 and M2 state rows at the read position, {len(RA['per_session'])} sessions ({2 * len(RA['per_session'])} rows; label_a is tag_plus in "
      f"{bal['yes']}, not in {bal['no']}); LOSO statistic with both rows of a session held out, {Aph2['n_shuffles']}-shuffle LOSO "
      f"label-shuffle null ({loc(RX, 'auc = PR.loso_auc(X, y, g)', after='def _relabel_job(args):')}-"
      f"{int(loc(RX, 'auc = PR.loso_auc(X, y, g)', after='def _relabel_job(args):').rsplit(':', 1)[1]) + 1}; `shuffle_null` is the "
      f"LOSO null, {loc(PRB, 'def shuffle_null(')})): {f4(min(p2_49))}-{f4(max(p2_49))} over L49-L63; over all {len(p2_layers)} stored "
      f"layers {f4(min(p2_all))}-{f4(max(p2_all))}; above null at {p2_above or 'no layer'}.")
    w()
    J["v"]["families"]["stageB_bc_labelpole_M3M4_random"] = bc
    J["v"]["k1_comparators"] = {f: KP[f] for f in ("g1_labelA_token_R_comparator", "g1_labelB_token_R_comparator", "g2_read_R_comparator", "g3_firstsign_read_R_comparator")}
    J["other"] = {"timing": {"session": TM["session"], "n_tokens_first_choice_prefix": TM["n_tokens_first_choice_prefix"]},
                  "stageA_per_layer": A["per_layer"], "stageA_posthoc2_labelpole_per_layer": Aph2["per_layer"],
                  "stageA_registered_range_L49_L63": [min(a_reg), max(a_reg)],
                  "stageA_registered_record_check": {"quoted": ".42-.51 above 48", "locator": loc_areg, "holds": ok_areg, "check": ck_areg},
                  "stageA_posthoc2_range_L49_L63": [min(p2_49), max(p2_49)], "stageA_posthoc2_layers_above_null": p2_above}

    if not ok_areg:
        REF_NOTES.append(f"Stage A (section 6): the entry's '.42–.51 above 48' ({loc_areg}) has a stored minimum of {f4(min(a_reg))} "
                         f"over L49-L63, {qr(min(a_reg), '.42')} at two decimals; '.41–.51' is the reproduced wording. Not a block figure.")

    # ================================================================ summary
    if LOC_MISSES:
        REF_NOTES.append(f"locator misses (the script could not find these anchors at {PIN}): {LOC_MISSES}")
    stored_fail = bool(mism or smism or raw_mism)
    if mism or smism:
        STOPS.append({"subitem": "leak recomputation", "discrepancy": f"stored vs recomputed mismatch {mism + smism}",
                      "suspected_cause": "see the tables"})
    if raw_mism:
        STOPS.append({"subitem": "(i-b) raw text vs JSON", "discrepancy": f"{len(raw_mism)} cells", "suspected_cause": "see section 4"})
    w("## 7. Figures: as the block writes them, the value printed, source, status")
    w()
    STATUS_RULE = [
        "One rule, applied to every row below and computed by the script (each row's 'check' column prints it). It is Code's rule, "
        "stated here because the block gives a status vocabulary but no rounding or domain convention.",
        "(R1) Precision. A quoted range 'a–b' holds iff the stored minimum and maximum over its domain, each rounded half-up to the "
        "decimals the quote writes for that endpoint, equal a and b. A quoted bound ('≤ x', '≥ x') is an inequality and is checked "
        "at full precision. A single quoted value for a single stored quantity holds iff the stored value rounds to it. A single "
        "'≈ x' for a per-layer series holds iff the series' mean and median both round to x, with the per-layer spread printed. "
        "'≈' adds no tolerance beyond this rounding. Counts are exact.",
        "(R2) Domain. The domain is the one the quote states; where the quote states none, the one its source (the record sentence "
        "named in the row) states; where neither does, L49-L63 (the stored layers above the steering layer; layers <= 48 carry no "
        "state, section 2), with all 18 stored layers beside. A figure that fails on its domain is not called reproduced on the "
        "strength of a narrower domain where it holds; that narrower domain is named as the correction. Where a quote gives one "
        "band for a panel that plots several series and does not say which (F1's null band), the domain is the plotted series "
        "pooled, each series' own result is printed beside, and, because F1 is not on this machine, the status is stated as "
        "conditional on what F1 plots (the 'status' column says 'conditional' and the condition is printed with the row).",
        "(R3) Class. When the stored values behind a row reproduce exactly (stored fields printed; recomputations equal to the stored "
        "analysis fields; JSON equal to the raw text F1 reads) and only the quoted wording fails R1 or R2, the status is 'discrepant "
        "(transcription)'. Block line 23 (N1's on-fail) corrects a transcription discrepancy in the note to the reproduced value; it "
        "is not a reproduction failure under block line 50. A row whose stored values did not reproduce would be 'discrepant' "
        f"without the qualifier and a STOP on link 3; at this run there is {'one or more' if stored_fail else 'none'}.",
    ]
    for s_ in STATUS_RULE:
        w(s_)
        w()
    w.table(["id", "figure (block)", "value printed here", "source", "domain (R2)", "check (R1)", "status", "note"],
            [[f["id"], f["figure"], f["reproduced"], f["source"], f["domain"], f["check"],
              f["status"] + (f" -- conditional: {f['status_condition']}" if f["status_condition"] else ""), f["note"]] for f in FIGS])
    n_by = {}
    for f in FIGS:
        n_by[f["status"]] = n_by.get(f["status"], 0) + 1
    disc_t = [f["id"] for f in FIGS if f["status"] == "discrepant (transcription)"]
    disc_hard = [f["id"] for f in FIGS if f["status"] == "discrepant"]
    cond_ids = [f["id"] for f in FIGS if f["status_condition"]]
    w(f"Status counts over {len(FIGS)} rows: " + ", ".join(f"{k} {v}" for k, v in sorted(n_by.items()))
      + (f"; of these, conditional on F1: {', '.join(cond_ids)}" if cond_ids else "") + ".")
    w()
    w("## 8. Referent notes (a wrong or loose referent is a note, not a STOP)")
    w()
    for i, n in enumerate(REF_NOTES, 1):
        w(f"{i}. {n}")
    w()
    w("## 9. Pass condition and STOPs")
    w()
    pass_met = not stored_fail and not disc_hard
    PASS = {
        "N3_i_and_i_b": ("met" if pass_met else "NOT met") + " on Code's reading",
        "reading": "transcription-class discrepancies (block line 23, N1's on-fail: corrected in the note to the reproduced value) "
                   "are not '(i) not reproducing' (block line 50); this reading is Code's, and the design seat decides",
        "condition": "block line 50: 'Pass: (i) reproduces.' On fail: '(i) not reproducing is a STOP on link 3.'",
        "transcription_discrepancies": disc_t,
        "conditional_rows": cond_ids,
        "hard_discrepancies": disc_hard,
        "v": "reported, not passed (block line 50)",
    }
    w(f"- **N3 (i) and (i-b): the pass condition (block line 50, '(i) reproduces') is {PASS['N3_i_and_i_b']}.** "
      f"Every stored value behind the quoted figures is printed from committed JSON; the leak figures are recomputed from the committed "
      f"reads artifacts and equal the stored analysis fields ({len(mism) + len(smism)} mismatches); the C1 tables equal the raw text F1 "
      f"reads ({n_cells} cells, {len(raw_mism)} disagreements). {len(disc_t)} rows are 'discrepant (transcription)' ({', '.join(disc_t)}): "
      "in each the stored values reproduce exactly and only the quoted wording fails section 7's rule. Block line 23 (N1's on-fail) "
      "has such a figure corrected in the note to the reproduced value; none is a reproduction failure, so none is a STOP on link 3. "
      + (f"{', '.join(cond_ids)}'s status is conditional on what F1 plots (section 7's row; reproduced if F1 draws label_a's null "
         "alone). " if cond_ids else "")
      + f"{len(disc_hard)} rows are 'discrepant' without the qualifier. The 'met' rests on that reading of block lines 23 and 50; "
      "the JSON's `pass` carries the same qualifier and its `reading` field.")
    w("- **(v): reported, not passed** (block line 50).")
    w(f"- Code reports the condition's state; it does not adjudicate (CLAUDE.md@{PIN}: 'Code escalates fired gates, never "
      f"self-adjudicates', {loc('CLAUDE.md', 'Code escalates fired gates, never self-adjudicates')}). The corrections are the note's "
      "and the design seat's to make.")
    w("- **STOPs:** " + ("none. No figure in parts (i), (i-b) or (v) needed a change to any analyzer to reproduce." if not STOPS
                         else "; ".join(str(s) for s in STOPS)))
    w()
    w("## 10. For the PI")
    w()
    try:
        _s3 = SJ["part_iii"]["summary"]
        _nm, _nr = len(_s3["mlp_read_layers_above_p95"]), len(_s3["rbf_read_layers_above_p95"])
        _pi7 = (f"Link 3's nonlinear line: per N3c's JSON, N3(iii)'s MLP and RBF reads at the decision token are above their own "
                f"permutation 95th at {_nm} and {_nr} of 15 layers (L49-L63), so block line 50's case applies; section 11 gives the "
                "link-3 sentence's values (confirmed or corrected) and a PROPOSED one-line addition with exact figures and the post-hoc "
                "label, for the design seat to adopt, rewrite or drop. Code has not adopted it.")
    except (KeyError, TypeError):
        _pi7 = (f"Link 3's nonlinear line: N3c's JSON was not usable at this run ({sj_err or 'field missing'}); section 11 proposes "
                "nothing; re-run this script once N3c's raw is in place.")
    PI_ITEMS.extend([
        "The note's leak sentence: 'median |Δ| ≤ .10' should read '≈ .10' or '≤ .103' (M2 .1027); a wording fix, no data question (3g). "
        f"The record's own figure check already says so ('exact would read .03–.10', {FC['B4_median']}).",
        "The last-round sign range '.94–.995' holds on L50-L63; the record's 'at every layer above 48' is wrong at L49 (.695). If the "
        f"note carries the record's domain, it should read 'L50-L63' (3a). The record's own figure check already says so ({FC['B1']}).",
        "The note's pseudo-shift sentence: the recon figure is ±.02–.03 on the MIXED random block masks B3x/B4x only (B1x/B2x "
        "+.008/-.002), toward the first ROUND's label; 'first block's label' is PROPOSAL-k's term (3h). The record's own figure "
        f"check already says so ({FC['B4_pseudo']}).",
        f"F1's link-3 null band: '.57–.59' is label_a's range at every layer ({_fr(la, L_ALL)}); pooled over the three plotted C1 families "
        f"the stored 200-draw 95th is {min(all_nulls):.3f}-{max(all_nulls):.3f}, i.e. {rec5760}, "
        "and as a pooled band '.57–.59' holds only if F1 omits "
        + ", ".join(f"L{l}" for l in sorted({l for (_, l, _) in n_over})) + " ("
        + ", ".join(f"{nm} {v} at L{l}" for nm, l, v in n_over) + "). The status is conditional on F1's series and layer range "
        "(ib-1); confirm both once the SVG is available.",
        "F1's second-label binding '.81–.96' holds from L51 (L49/L50 .53-.54); it needs 'from L51' unless the first clause's "
        "'from L51 on' already covers it (ib-3). The same holds for the note's '≈ 1.0 at the first label' and '.81–.96 at the second' "
        "if the elided sentence does not carry a layer range (section 4's sentence table).",
        f"Parts (ii)-(iv) are the sibling item N3c's, raw {SIBLING} ({'present' if sib_present else 'not present'} when this raw "
        "was generated); sections 0-10 of this raw do not depend on it; section 11 quotes its JSON and, for three strings not in "
        "the JSON (two status tags and one advice sentence), its raw .md.",
        _pi7,
    ])
    for i, p in enumerate(PI_ITEMS, 1):
        w(f"{i}. {p}")
    w()

    # ================================================================ link 3 (reads the sibling's JSON)
    w("## 11. Link 3: the sentence's values, and a proposed nonlinear line (for the design seat; not adopted)")
    w()
    try:
        J["link3"] = link3_section(w, SJ, sj_sha, sj_err, SMD, smd_sha, smd_err, la, lb, rd, RC, rd_below, rd_margin, all_nulls,
                                   n_over, loc_4402, rec5760)
    except (KeyError, TypeError, IndexError, ValueError) as e:   # a sibling JSON of another shape: say so, keep the rest of the raw
        w()
        w(f"**Section 11 is INCOMPLETE at this run:** N3c's JSON (sha256 {sj_sha}) lacks a field this section reads "
          f"({type(e).__name__}: {e}); whatever is printed above this line in section 11 stands, and nothing further is quoted or proposed.")
        J["link3"] = {"status": f"incomplete: {type(e).__name__}: {e}", "sibling_json_sha256": sj_sha}
    w()

    # ================================================================ values-check
    w("## 12. Values-check")
    w()
    w("### Round 1")
    w()
    w("An adversarial values-checker reviewed the builder's raw (per the checker's report: builder script sha256 080f49b0...6721b, "
      "278 claims checked, the script re-ran identically apart from the stamp, command line and output paths). Its ten findings and "
      "Code's disposition of each, then the items Code found on its own re-read. Every 'fixed' below is in this raw as regenerated.")
    w()
    VC = [
        ("1", "minor, imprecise", "ib-1 ('≈ .57–.59', called reproduced) and 3g ('≤ .10', called discrepant) followed different, unstated rules.",
         "fixed",
         "One rule now stated in section 7 (R1 precision, R2 domain, R3 class) and computed per row by the script. Under it ib-1 is "
         "'discrepant (transcription)' (L49-L63 and all 18 layers fail; holds on L51-L63 only) and 3g stays discrepant, now "
         "'discrepant (transcription)'. Applying the same rule to every row also moved 3a (the source's 'every layer above 48' fails "
         "at L49), 3h (the source's 'the random block masks' fails at B1x/B2x) and ib-3 (no layers in its clause; fails at L49/L50) "
         "to 'discrepant (transcription)'. That extension is Code's, made so no row breaks the stated rule. [ib-1's status made "
         "conditional on F1's series in round 2, R2-2.]"),
        ("2", "minor, incomplete", "Section 9 never stated the N3 (i) pass outcome or squared 3g with the on-fail line.",
         "fixed", "Section 9 now states the pass condition's state, the transcription rows, why none is a STOP (block lines 23 and 50), "
         "that (v) is reported, not passed, and that Code does not adjudicate; JSON key 'pass'."),
        ("3", "minor, unsupported", "'Parts (ii)-(iv) ... are in results/raw/2026-10-08_note-N3-echo-compute.md' when that file did not exist.",
         "fixed", "Reworded in the docstring, the Scope line and section 10; the script tests the path at run time and prints the result "
                  f"(this run: {'present' if sib_present else 'not present'}); the test is listed as a run-dependent line."),
        ("4", "minor, rule-violation", "Stage A's '.42–.51 above 48' quoted without a pinned locator.",
         "fixed", f"Locator added ({loc_areg}). Code's own addition: at four decimals the stored minimum is {f4(min(a_reg))}, which the "
                  f"builder printed as 0.415; it rounds to {qr(min(a_reg), '.42')} at two decimals, so the entry's '.42' does not "
                  "reproduce under R1 (section 6 and a referent note; not a block figure)."),
        ("5", "minor, incomplete", "Post-hoc #2's AUC range named no layer range, target rows or CV scheme.",
         "fixed", "Section 6 now names the target, rows, n, LOSO statistic, the 200-shuffle LOSO null with its locators, the layer "
                  "ranges (L49-L63 and all stored layers) and the above-null count."),
        ("6", "minor, rule-violation", "3d cited 'C entry' with no pinned locator.",
         "fixed", f"Replaced by {loc(RE, 'the M1–M4 and shadow rows at the read position are bit-identical to Stage B', after=RC_HDR)}."),
        ("7", "minor, imprecise", "3f attributed 'sign flips' to the note, which is not on this machine.",
         "fixed", "Now 'the block's wording (block line 43, quoting the note)'. [Superseded in round 2, R2-4: a pick flip is exactly "
                  "a sign flip, so the block's wording is accurate.]"),
        ("8", "minor, incomplete", "3j gave the import chain as the reason k1_analyze.py was not run.",
         "fixed", "Section 3j now gives the binding reason: no read-only mode; --run refits from the local data/k npz arrays and writes "
                  "data/k/<out-name> (locators given), which block rule 1 forbids; k1_analysis.json is its committed --run output. The "
                  "import chain is kept as secondary. [Superseded in round 2, R2-5: the binding reason is block N3(i) and rule 5; the "
                  "write path is secondary.]"),
        ("9", "minor, incomplete", "(v)'s summary skipped L53 for the label_a random series.",
         "fixed", f"L53 ({f3(ra['53']['auc_kfold'])}) now printed in section 5 and the v-1 row. Code found the same omission for "
                  f"label_b random at L52 ({f3(rb['52']['auc_kfold'])}) in the v-1 row; fixed."),
        ("10", "minor, imprecise", "The masks' sign pattern was cited to injection_for (the direction choice).",
         "fixed", "Both cited: direction at injection_for, sign pattern at signs_for."),
    ]
    OWN = [
        ("own-1", "The leak table's heading said the record's PROHIBITION forbids 'nothing signed toward a label on a reward mask', "
                  "while the same table carried M5/M6 and the signed table printed M5/M6.",
         "fixed", "Heading now 'Axis masks', with the PROHIBITION as the code states it (SIGNED_OK includes M5/M6; the refused set is "
                  "M1, M2, R1-R4, B1-B4) and its locators; '12 reward masks' is now '12 axis masks' throughout."),
        ("own-2", "The header's stdlib list omitted modules the script imports.", "fixed", "Listed in full."),
        ("own-3", "Rows had no printed domain or check, so a reader could not see why a status was given.",
         "fixed", "Section 7 now has 'domain (R2)' and 'check (R1)' columns, and the JSON carries both per figure."),
    ]
    w.table(["#", "severity (checker's)", "finding", "disposition", "detail"], [list(v) for v in VC])
    w.table(["#", "found on Code's re-read", "disposition", "detail"], [list(v) for v in OWN])
    w("No checker finding was rejected. Each disposition above was applied by editing this script and regenerating the raw and the JSON.")
    w()
    # ---------------------------------------------------------------- round 2
    w("### Round 2")
    w()
    w("The values-checker's second pass reviewed the round-1 regeneration (script sha256 ccb7bef5...c386; HEAD bbc9ffe at that run). "
      "Its summary: every value it recomputed with its own code from the committed artifacts agrees with the raw (1,116 table cells, "
      "0 mismatches; the C1 JSON against the stageC raw text 234/234); no STOP is warranted. It raised 8 findings (2 substantive, "
      "6 minor). Code's disposition of each, then the two coordination items routed with this round (N3c's figures). Every "
      "'fixed' below is in this raw as regenerated.")
    w()
    _sc = lambda st: n_by.get(st, 0)
    VC2 = [
        ("R2-1", "substantive, wrong", "Row 3i-a called the random-mask leak computed-new and said the record carries no random-mask leak "
         "figure but the signed pseudo-shift; the record's prose states the random families' flips 0–1/102 and M5x's max .2012.",
         "fixed", f"Verified at {FC['B4_flips']} and {FC['B4_max']}. Row split: 3i-a1 (flips {min(rf)}-{max(rf)}/102 and the largest "
         f"max {kmx} {f4(rmax[kmx])}, checked against the record's prose: {[f for f in FIGS if f['id'] == '3i-a1'][0]['status']}) and 3i-a2 "
         "(the medians, computed-new: no random-mask median in the record). The random-masks heading now says the record's TABLES carry "
         "none and its prose states the flips and the max. Status counts now: " + ", ".join(f"{k} {v}" for k, v in sorted(n_by.items())) + "."
         " [The max clause's domain, the R / M++ arms (axis and random), restated in round 4, R4-4.]"),
        ("R2-2", "substantive, overclaim", "ib-1's 'discrepant (transcription)' and the PI item rested on pooling the three families' "
         "nulls, a rule R1/R2 never stated; per family, label_a's null is .569-.590 at all 18 layers; section 4 said the block 'says' "
         "F1 plots below L51.", "fixed",
         "R2 now states the pooled-band clause (one band for a multi-series panel whose series is unstated: the plotted series pooled, "
         "each beside, the status conditional on F1). ib-1 keeps 'discrepant (transcription)' as the pooled reading, now marked "
         f"conditional: reproduced if F1 draws label_a's null alone ({_fr(la, L_ALL)}), discrepant if the band pools the families or is "
         f"the read's with L{', L'.join(str(l) for l in over_by_fam['read'])} or label_b's with "
         f"L{' or L'.join(str(l) for l in over_by_fam['label_b'])}. Section 4 item 1 now gives the band per family and per domain and "
         f"says 'implies'; PI item 4 reworded; the record's '.57–.60' cited ({loc_4402}). [That '.57–.60' scoped to the read "
         "position's nulls in round 4, R4-3.]"),
        ("R2-3", "minor, incomplete", "The 3a, 3g and 3h corrections are already in the record's own figure check, uncited.",
         "fixed", f"Verified and cited in rows 3a/3g/3h, referent notes and PI items 1-3: {FC['B1']} (3a), {FC['B4_median']} (3g), "
         f"{FC['B4_pseudo']} (3h). Each note now says this audit's recomputation agrees with the record's own check."),
        ("R2-4", "minor, incomplete", "8 of the 9 distinct pick flips sit on exactly tied shadow reads; a pick flip is a sign flip.",
         "fixed", f"Recomputed here: pick == label_a iff logit_a >= logit_b in all {n_reads:,} stored reads ({n_exc} exceptions); "
         f"{len(distinct)} distinct (session, mask) flips, {len(on_tie)} on the tied shadows of sessions "
         f"{', '.join(str(x) for x in tie_sess)}; untied: " + "; ".join(f"s{k[1]} {k[0]} ({f_['shadow_diff']:+.4f} -> {f_['state_diff']:+.4f})"
                                                                 for k, f_ in untied) +
         ". A computed-new line under the leak tables and JSON leak.tie_analysis; 3f's note no longer implies a pick/sign distinction."),
        ("R2-5", "minor, imprecise", "3j's stated binding reason (no read-only mode; --run writes under data/k) is not what binds: an "
         "absolute --out-name redirects the write, and the arrays are local.", "fixed",
         f"Verified: os.path.join('/repo/data', 'k', '/elsewhere/x.json') = '{_abs_demo}'; {len(k_npz_local)} of {len(k_npz)} k1 arrays "
         "present on this machine (existence test only), none tracked. 3j now gives block N3(i)'s 'From committed JSON' and block rule 5 "
         "(refits only in N3(ii)-(iv)) as the binding reason, --run as the only non-synthetic mode (a refit), and the write path as "
         "secondary."),
        ("R2-6", "minor, incomplete", "The record's 'the 40/44/48 probes are exactly 0.500 for every family' holds for 6 of 18 Stage B "
         "families; section 2's '(0/8)' omitted the 4 text-only families.", "fixed",
         f"Section 2 now prints {sum(lc_b[f] for f in paired_b)}/{len(paired_b)} paired, {sum(lc_b[f] for f in single_b)}/{len(single_b)} "
         f"single-round, {sum(lc_b[f] for f in text_b)}/{len(text_b)} text-only ({n_half_b}/{len(lc_b)} in all); a referent note cites "
         f"{loc_4752} and scopes a note sentence 'layers <= 48 read exactly .500' to paired contrasts."),
        ("R2-7", "minor, incomplete", "Row v-1 neither cited nor checked the record's random-binding figures.", "fixed",
         f"Source now cites {loc(RE, '1.000 at L51–L52 at label_a and .83–.90 from L54 on', after=RC_HDR)}; seven checks "
         f"({sum(1 for o, _ in ck_v1 if o)}/{len(ck_v1)} hold), status {[f for f in FIGS if f['id'] == 'v-1'][0]['status']}."),
        ("R2-8", "minor, imprecise", "The JSON's pass key dropped 'on Code's reading'.", "fixed",
         f"JSON pass.N3_i_and_i_b = '{PASS['N3_i_and_i_b']}', with a `reading` field (block lines 23 and 50; the design seat decides) "
         "and `conditional_rows`."),
    ]
    COORD = [
        ("C-a", "Shuffle-95 band: state the stored 200-draw 95th exactly by layer domain and give the note's '≈ .57–.59' / '≈ .58' a "
         "status consistent with N3c.", "done",
         f"ib-1's value now gives it by domain (pooled L49-L63 {min(nul(L_ABOVE)):.4f}-{max(nul(L_ABOVE)):.4f}, all 18 "
         f"{min(nul(L_ALL)):.4f}-{max(nul(L_ALL)):.4f}, L51-L63 {min(nul(L51_63)):.4f}-{max(nul(L51_63)):.4f}; each family beside). "
         f"'≈ .57–.59': {[f for f in FIGS if f['id'] == 'ib-1'][0]['status']} (conditional on F1); '≈ .58': "
         f"{[f for f in FIGS if f['id'] == 'ib-5'][0]['status']} (as a midpoint). N3c's own statuses are quoted in section 11 "
         f"(F1 band: '{J['link3'].get('n3c_status_quoted', {}).get('F1 band', 'n/a')}'; ≈ .58: "
         f"'{J['link3'].get('n3c_status_quoted', {}).get('≈ .58', 'n/a')}')."),
        ("C-b", "Read N3c's JSON; add a section with the link-3 sentence values confirmed or corrected, and the proposed one-line "
         "nonlinear addition with exact figures and the post-hoc label, for the design seat, not adopted (block line 50).", "done",
         "Section 11. " + (f"N3c's JSON read (sha256 {sj_sha[:16]}...); its stored-draw nulls and linear AUCs equal the committed ones "
                           f"at {J['link3']['cross_checks']['null200_p95_equal'][0]}/{J['link3']['cross_checks']['null200_p95_equal'][1]} and "
                           f"{J['link3']['cross_checks']['auc_kfold_equal'][0]}/{J['link3']['cross_checks']['auc_kfold_equal'][1]} cells; the "
                           "proposed line is printed in an exact and a two-decimal form, with its labels."
                           if SJ is not None and "cross_checks" in J["link3"] else f"N3c's JSON not read ({sj_err}).")),
    ]
    w.table(["#", "severity (checker's)", "finding", "disposition", "detail"], [list(v) for v in VC2])
    w.table(["#", "coordination item (routed with round 2)", "disposition", "detail"], [list(v) for v in COORD])
    _pcm = min(J["link3"].get("nonlinear", {}).get("positive_control_min_L51_61", {"x": float("nan")}).values())
    OWN2 = [
        ("own2-1", "The proposed line's positive-control bound would have printed the half-up rounding of the minimum "
                   + (f"({_pcm:.6f} -> {_r(_pcm, 4)})" if _pcm == _pcm else "(not computed at this run)")
                   + ", which can fail R1's full-precision check of a bound.", "fixed",
         "A lower bound is now printed rounded down (`_floor`)" + (f": '≥ {_floor(_pcm, 4)}'." if _pcm == _pcm else ".")),
        ("own2-2", "The short form's within-subgroup range printed '.96–1.00' (0.9959 rounds to 1.00 at two decimals).", "fixed",
         "Printed at three decimals ('.958–.996'), with its R1 check."),
        ("own2-3", "The tie analysis counted each (session, mask) once on the assumption that Stage C's M1-M4 reads are Stage B's.",
         "fixed", "Checked read by read (logits and picks; result printed in the tie line and in JSON leak.tie_analysis)."),
        ("own2-4", "Section 11 reads an uncommitted sibling file that N3c's own round may rewrite.", "fixed",
         "It prints the JSON's sha256, compares N3c's script on disk with the one that wrote the JSON, and on an absent, unreadable "
         "or differently shaped JSON prints 'not read' / 'INCOMPLETE' instead of failing (both fallbacks run in scratch: absent JSON, "
         "empty JSON)."),
    ]
    w.table(["#", "found on Code's re-read (round 2)", "disposition", "detail"], [list(v) for v in OWN2])
    w("No round-2 finding was rejected: each was checked with a tool run before it was applied (the locators by reading RESULTS.md at "
      f"{PIN}; the tie analysis, the Stage B family counts and the random-binding checks by this script; the os.path.join behaviour "
      "by a one-line run). Each disposition was applied by editing this script and regenerating the raw and the JSON.")
    w()
    # ---------------------------------------------------------------- round 4
    w("### Round 4")
    w()
    w("The workflow's round 4. This item had no round-3 fix: the values-checker's third pass reviewed the round-2 regeneration "
      "(script sha256 d889e046...8825, raw 62a03458...9fa2, JSON fbaf6146...191db; Code hashed the three files with shasum before "
      "this round's edits, and they match the checker's). Its summary: the round-2 fix holds; its scratch re-run differed from the "
      "files at their committed locations only in the declared run-dependent lines (stamp, command line, output paths, section 11's "
      "N3c-script line, the JSON's link3.n3c_raw_sha256); the redaction check passed; no number, status or STOP/pass outcome "
      "changes; no STOP is missing. It raised 5 minor findings and none open from earlier rounds. Code's disposition of each, then "
      "the items Code found on its own re-read. Every 'fixed' below is in this raw as regenerated.")
    w()
    _lk = J.get("link3", {}) or {}
    _nl = _lk.get("nonlinear", {}) or {}
    _pl = _lk.get("proposed_line", {}) or {}
    _rl = _lk.get("n3c_raw_lines", {}) or {}
    _sj_in = _lk.get("n3c_raw_strings_found_in_json")
    _ib57 = J["i_b"]["record_57_60"]
    try:
        _s3s = SJ["part_iii_s"]["summary"]; _s3 = SJ["part_iii"]["summary"]
        _rob = (f"spec MLP over 5 seed pairs L56 {_s3s['mlp_seed_range_per_layer']['56'][0]:.4f}-{_s3s['mlp_seed_range_per_layer']['56'][1]:.4f}, "
                f"L61 {_s3s['mlp_seed_range_per_layer']['61'][0]:.4f}-{_s3s['mlp_seed_range_per_layer']['61'][1]:.4f}; Adam-trained MLP "
                + ", ".join(f"L{k} {v:.4f}" for k, v in _s3s["adam_auc"].items())
                + f"; RBF lambda at the grid's lower edge in {_s3['rbf_read_obs_fits_at_grid_lower_edge']['n']}/"
                f"{_s3['rbf_read_obs_fits_at_grid_lower_edge']['of']} fits, extended grid {_s3s['rbf_x_auc_range'][0]:.4f}-"
                f"{_s3s['rbf_x_auc_range'][1]:.4f}; exceedance on the shuffle null {len(_nl.get('above_p95', {}).get('mlp', []))}/15 (MLP) and "
                f"{len(_nl.get('above_p95', {}).get('rbf', []))}/15 (RBF), on the per-session flip null {len(_s3s['mlp_flip_layers_above_p95'])}/15 "
                f"and {len(_s3s['rbf_flip_layers_above_p95'])}/15")
    except (KeyError, TypeError):
        _rob = "N3c's (iii-s) summary not readable at this run"
    _sub = _nl.get("posthoc_within_subgroup_L51_61"); _sub15 = _nl.get("posthoc_within_subgroup_L49_63")
    _subo = _nl.get("posthoc_within_subgroup_outside_L51_61", {})
    _nn_line = _rl.get("subgroup reads 'no null (point estimates only)'")
    VC4 = [
        ("R4-1", "minor, incomplete (provenance)", "Section 11 presented its N3c quotes as read from N3c's JSON; the two status strings "
         "(F1's band, '≈ .58') come from N3c's raw .md, whose sha256 the raw never printed and which no provenance text named.", "fixed",
         "Verified: a search of every string key and value of N3c's JSON finds "
         + (f"{_sj_in[0]} of the {_sj_in[1]} strings section 11 takes from N3c's .md ({_sj_in[2]:,} strings searched)" if _sj_in else
            "(not run: N3c's JSON or .md not read)")
         + "; the strings are the two status tags and, found on Code's re-read (own4-1), N3c's advice sentence. The .md is now read "
         "once in main() and hashed; it is named in the Scope line (with its sha256), the run-dependent-lines note, section 11's "
         f"provenance (with its sha256 and the .md line of each string: F1 band {_rl.get('F1 band status')}, '≈ .58' "
         f"{_rl.get('≈ .58 status')}, advice {_rl.get('advice')}) and the docstring; JSON header.sibling_raw_md_sha256_at_run, link3.n3c_raw_sha256 and "
         "link3.n3c_raw_lines. Each status quote in section 11's table now says 'its raw .md, line N; not in its JSON'."),
        ("R4-2", "minor, incomplete (domain omitted)", "The short form's subgroup clause '(.958–.996)' and its R1 check named no domain; "
         "over L49–L63, the only layer range the short form names, the subgroup reads fall to .6691.", "fixed",
         ("Verified from N3c's JSON (posthoc_composition.per_layer): " + (f"{_sub[0]:.4f}-{_sub[1]:.4f} over L51-L61, " if _sub else "")
          + (f"{_sub15[0]:.4f}-{_sub15[1]:.4f} over L49-L63 (" if _sub15 else "")
          + ", ".join(f"L{l} {v[0]:.4f}/{v[1]:.4f}" for l, v in _subo.items()) + (")" if _sub15 else "")
          + ". Both forms now carry 'L51–L61' in the subgroup clause and the optional label '"
          + str(_pl.get("subgroup_tag")) + "' (N3c's JSON stores only " + ", ".join(_nl.get("posthoc_cell_fields", [])) + " per post-hoc cell; "
          f"N3c's .md line {_nn_line} says 'no null (point estimates only)'); the R1 check names each quoted range's domain (MLP and RBF L49-L63, subgroup L51-L61) and prints the "
          "L49-L63 subgroup range beside; the 'in any linear functional' row of (a) carries the same label.")),
        ("R4-3", "minor, imprecise (referent scope)", "PI item 4, ib-1's correction and section 11's F1-band row presented '.57–.60' "
         "as the record's own prose for the band pooled over the three C1 families.", "fixed",
         f"Verified at {loc_4402}: 'At the read position the pole of label_a stays null — .50–.55 against nulls .57–.60'. The read "
         f"family's null95 over all 18 layers is {_ib57['read_null95_all18'][0]:.4f}-{_ib57['read_null95_all18'][1]:.4f}, the pooled "
         f"{_ib57['pooled_null95_all18'][0]:.4f}-{_ib57['pooled_null95_all18'][1]:.4f} ("
         + (f"equal {_ib57['read_equals_pooled']}" if _ib57['read_equals_pooled'] != "no" else "not equal") + "), so no number "
         f"changes. The three places now read {rec5760}; ib-1's source says 'for the read position's nulls'. One part of the checker's "
         "evidence does not hold: 'The record says nothing about label_a's or label_b's nulls'. The Stage C entry's three per-position "
         f"tables print each family's null per layer at two decimals ({rec_tables}); ib-1's note now says so. Section 11's quoted N3c "
         "status keeps N3c's own wording ('the record's own prose says .57-.60'), which is N3c's file and is not edited here."),
        ("R4-4", "minor, imprecise (record domain); status unaffected", "Row 3i-a1 and the random-masks heading cited the record's "
         "'the largest M5x .2012' as a random-mask figure; the clause is about 'the R / M++ arms', axis and random, and its '.11–.20' "
         "reads .12–.20 under R1 on the checker's domain.", "fixed (the optional note applied with a second reading of the domain)",
         f"Verified at {FC['B4_RMpp']} (the max locator now starts at the clause's subject; it was {FC['B4_max']}). The heading and the row "
         "now give the domain as the R / M++ arms (axis and random) and say M5x is the largest there and on the 12 random masks. The "
         "record lists no recon masks for 'R / M++', so the script computes the candidate domains (section 3f-3i, JSON "
         f"leak.record_RMpp_clause): (A) PROPOSAL-k's own naming, R = the arms on the random direction ({loc_pk_r}) and M++ = +d on "
         f"both blocks ({loc_pk_mpp}), i.e. the 12 random masks and M5/M6: '.11–.20' {RMPP['A']['range_11_20'][1].split(': ')[-1]}; "
         f"(B) the checker's: {RMPP['B']['range_11_20'][1]}; (C) every non-M1/M2 mask: largest {RMPP['C']['largest'].split(':')[1]} "
         f"{f4(RMPP['C']['max_by_mask'][RMPP['C']['largest']])}, an axis block mask: on a domain that includes it M5x is not the largest, so "
         "the clause's 'the largest M5x' does not fit that reading. The referent note "
         "gives A and B, not B alone: under PROPOSAL-k's naming B1x belongs to the R arms, and on that reading '.11–.20' holds. 3i-a1's "
         f"status is unchanged ({[f for f in FIGS if f['id'] == '3i-a1'][0]['status']})."),
        ("R4-5", "minor, imprecise (draft contradicts the advice printed beside it)", "The exact and short draft lines opened with the "
         "MLP and RBF AUC levels, while the bullet after them quoted N3c's advice to quote the exceedance or the RBF figure with its "
         "grid caveat rather than the MLP peak.", "fixed",
         f"Verified from N3c's JSON: {_rob}. Both forms now lead with the exceedance and carry each level in parentheses, tagged "
         f"'{_pl.get('mlp_level_tag')}' (MLP) and '{_pl.get('rbf_level_tag')}' (RBF); the labels bullet quotes N3c's advice verbatim "
         "(own4-1) and says both forms follow it."),
    ]
    OWN4 = [
        ("own4-1", "Section 11's bullet 'N3c's own advice: quote the exceedance, or the RBF figure with its grid caveat, rather than the "
         "MLP peak' paraphrased a sentence of N3c's raw .md with no source; it is not in N3c's JSON either.", "fixed",
         f"Quoted verbatim from N3c's .md (line {_rl.get('advice')}) and counted in R4-1's search."),
        ("own4-2", "The run-dependent-lines note did not list the section 12 rows that quote section 11's N3c values (round 2's C-a "
         "and C-b).", "fixed", "Listed, with this round's R4-1, R4-2 and R4-5."),
    ]
    w.table(["#", "severity (checker's)", "finding", "disposition", "detail"], [list(v) for v in VC4])
    w.table(["#", "found on Code's re-read (round 4)", "disposition", "detail"], [list(v) for v in OWN4])
    w("No round-4 finding was rejected. Each was verified with a tool run before it was applied: N3c's JSON searched for the three "
      ".md strings, and its stored post-hoc reads taken over both layer domains (this script); RESULTS.md and PROPOSAL-k-echo-channel.md read "
      f"at {PIN} for the two clauses and the mask names; the per-mask maxima recomputed from the committed reads (this script). Two "
      "parts were applied in corrected form, as stated: the label_a/label_b clause of R4-3's evidence, and R4-4's optional note, "
      "which now carries both readings of the domain. Each disposition was applied by editing this script and regenerating the raw "
      "and the JSON.")
    w()
    J["figures"] = FIGS; J["referent_notes"] = REF_NOTES; J["stops"] = STOPS; J["pi_items"] = PI_ITEMS
    J["locator_misses"] = LOC_MISSES
    J["status_rule"] = STATUS_RULE
    J["pass"] = PASS
    J["values_check"] = {"checker_findings": [dict(zip(("n", "severity", "finding", "disposition", "detail"), v)) for v in VC],
                         "code_own": [dict(zip(("n", "finding", "disposition", "detail"), v)) for v in OWN],
                         "round2_checker_findings": [dict(zip(("n", "severity", "finding", "disposition", "detail"), v)) for v in VC2],
                         "round2_coordination": [dict(zip(("n", "item", "disposition", "detail"), v)) for v in COORD],
                         "round2_code_own": [dict(zip(("n", "finding", "disposition", "detail"), v)) for v in OWN2],
                         "round4_checker_findings": [dict(zip(("n", "severity", "finding", "disposition", "detail"), v)) for v in VC4],
                         "round4_code_own": [dict(zip(("n", "finding", "disposition", "detail"), v)) for v in OWN4]}

    os.makedirs(os.path.dirname(out_md), exist_ok=True)
    os.makedirs(os.path.dirname(out_js), exist_ok=True)
    with open(out_md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(w.lines).rstrip("\n") + "\n")
    with open(out_js, "w", encoding="utf-8") as fh:
        json.dump(J, fh, indent=1, ensure_ascii=False, default=str)
        fh.write("\n")
    print(f"wrote {out_md}\nwrote {out_js}\nfigures {len(FIGS)}; referent notes {len(REF_NOTES)}; stops {len(STOPS)}; locator misses {len(LOC_MISSES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
