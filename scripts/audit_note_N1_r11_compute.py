#!/usr/bin/env python3
"""note-N1 round 11 (open item O35 of round 11's claims ledger): the 24 figures of RESEARCH-NOTE-v0_8-draft.md that
are the note's own arithmetic on committed inputs, computed from those inputs and compared with the note's printed
values.

Its raw of record is results/raw/2026-11-02_note-N1-r11_computations.md, written by this script as committed (the run
asserts that the script equals its blob at HEAD). The design seat's round-11 answers
(results/raw/2026-11-02_note-design-to-code_N1-r11-answers.md@da50cd1, section 0 row 2b) admit that raw, by route (a)
of the seat list's section 2b (results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md@d5123bf). N1's round-11
profile (v0_8, committed with round 11's claims ledger, after the raw) pins the raw at the commit that adds it (its own
pin class), where its 24 rows map audit-raw-new, computed-new.

Standard library only. Every repository input is read with `git show <rev>:<path>`, each blob hashed; no working-tree
file of the repository is an input (the script reads its own file only to hash it), and the one file written is
--out. No model, no randomness, no network. With the same arguments at the same HEAD, the output differs between runs
only in its Code stamp line. HEAD enters in two ways: the HEAD line, and the "(HEAD :n)" / "(differs at HEAD)" notes,
which say where a cited line sits in the HEAD blob when a file changed after the cited revision. Paths in the output
are printed relative to the repository's top level when they lie inside it; outside it, the interpreter is printed as
"python3", this script by its file name, and --out (or --repo) as given.

Usage, from the repository's top level:
  jlens-qwen36/.venv/bin/python -I scripts/audit_note_N1_r11_compute.py --out results/raw/2026-11-02_note-N1-r11_computations.md
  [--repo REPO: the repository whose blobs are read; default: the repository this script is in]
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import os
import re
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP, localcontext
from fractions import Fraction
from statistics import NormalDist

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the repository this script is in
NOTE = "RESEARCH-NOTE-v0_8-draft.md"
NOTE_REV = "0de15a1"
NOTE_SHA = "6fcfbfd64784412d616d4de40d4a6a54596202a052cb3dd0d9d78a26cbe1198d"
N2 = "results/raw/2026-10-08_note-N2-introspection.md"
N2VI = "results/raw/2026-10-08_note-N2vi-source.md"
N2VI_JSON = "results/raw/2026-10-08_note-N2vi-source.json"
N2_ROC = "results/raw/2026-10-08_note-N2-roc.json"
N2_SCRIPT = "scripts/audit_note_N2.py"
N2VII = "results/raw/2026-10-22_note-N2vii-macar-v5.md"
RES = "RESULTS.md"
CTRL = "data/olmo/b2r_control_{}.json"
EXPL = "data/olmo/b2r_explore_sft.json"
ANSWERS = "results/raw/2026-10-28_note-design-to-code_release-block-answers.md"
BLOCK = "results/raw/2026-10-27_note-design-to-code_release-block.md"
SEAT = "results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md"         # the seat list (Code's round-11 list)
R11_ANSWERS = "results/raw/2026-11-02_note-design-to-code_N1-r11-answers.md"   # the design seat's round-11 answers
V1RAW = "results/raw/2026-11-02_note-N1-r11_macar-v1-lines.md"                # the v1 raw (the seat's transcription)
RAW_OF_RECORD = "results/raw/2026-11-02_note-N1-r11_computations.md"
SCRIPT = "scripts/audit_note_N1_r11_compute.py"
# lines this raw cites in its prose, each asserted to carry the quoted text
CITED = [
    ("09c3a8c", N2, 20, "Status vocabulary: reproduced | log-only | not found | discrepant | computed-new."),
    ("09c3a8c", N2, 70, "| 47 | theirs DPO d' ~ +0.6 |"),
    ("09c3a8c", N2, 74, "| 51 | ours SFT d' ~ +0.3 |"),
    ("09c3a8c", N2, 382, "| dpo | 145/5000 | 0/500 | +1.197 |"),
    ("09c3a8c", N2, 386, "| dpo | 464/16000 | 0/1600 | +1.525 |"),
    ("09c3a8c", N2, 390, "| dpo | 2900/100000 | 0/10000 | +1.995 |"),
    ("09c3a8c", N2, 457, "(one-sided Fisher)"),
    ("09c3a8c", N2, 458, "The source's detection grader is not identified in the record or the N2vi raw."),
    ("bbc9ffe", RES, 7431, "Their OLMo stage comparison is `experiments/03_behavioral_robustness.py`"),
    ("908a659", ANSWERS, 23, "v0.8 does not change again before the tag"),
    ("908a659", ANSWERS, 55, "Block :31\u2013:38 stands for everything else by source"),
    ("908a659", ANSWERS, 21, "sha256 `6fcfbfd64784412d616d4de40d4a6a54596202a052cb3dd0d9d78a26cbe1198d`"),
    ("d5123bf", SEAT, 180, "## 2. The not-found figures (40), by cause"),
    ("d5123bf", SEAT, 234, "| S8#2032\u2013S8#2036 | :230 '17/96', '0.177', '0/96', '25/96', '0.260'"),
    ("d5123bf", SEAT, 238, "| S8#3019, S8#3022, S8#3024, S8#3026, S8#3027 | :242 '0.55', '1.85', '2.48', '2.2', '2.5'"),
    ("2fb0cf0", BLOCK, 32, "the source-convention rates 17/96 = 0.177, 25/96 = 0.260, 0/96"),
    ("e60b633", N2, 83, "| 60 | theirs ablation d' \u2248 1.8 (refusal direction ablated; uncorrected) | computed-new |"),
    ("f935864", "scripts/audit_note_N1.py", 2406, "NR_ITEMRAW_RE = re.compile(r\"^results/raw/2026-10-0[89]_note-N"),
    ("8d68b0b", N2VII, 89, "Detection rates are approximated by the logit difference Yes \u2212 No"),
    ("e60b633", N2_ROC, 66, "a pooled n treats trials clustered by configuration and concept as independent"),
    ("d5123bf", SEAT, 228, "### 2b. The note's own arithmetic on committed inputs, printed by no committed carrier (24; "
                           "chains K5, K9, K10)"),
    ("d5123bf", SEAT, 230, "On Code's reading, 4e keeps the block as a listing by source (answers :55), not as a carrier."),
    ("d5123bf", SEAT, 261, "Before commit, Code regenerates the raw from the committed copy of its script, and re-points "
                           "its references to this list's sections to this file."),
    ("d5123bf", SEAT, 266, "(a) Admit the computation raw. Code commits it with its own pin class, and the 24 rows map "
                           "audit-raw-new, computed-new"),
    ("d5123bf", SEAT, 366, "| 9 | :242 · S8#3025 | scope | \"the released code's ten\" is the default of the OLMo "
                           "stage-comparison script, applied to Gemma as a premise |"),
    ("d5123bf", SEAT, 386, "| 29 | :230–:236 · S8#2040, S8#2044, S8#2098, S8#2100 | wording | p-values with no "
                           "test named"),
    ("d5123bf", SEAT, 406, "3. **‡(c)'s grading premise** (2b). Whether v1's Table 4 holds the rule \"grade a "
                           "non-answering or incoherent response NO and retain it\""),
    ("da50cd1", R11_ANSWERS, 23, "| 2b · the 24 computations | **(a).** Admit the computation raw; Code regenerates "
                                 "it from its committed script and commits it with its own pin class; the 24 rows map "
                                 "audit-raw-new, computed-new."),
    ("da50cd1", R11_ANSWERS, 23, "The ‡(c) premise is now carried: v1's Table 4 grades a non-answering or incoherent "
                                 "response NO (the v1 raw, §2), so the nine ‡(c) rows compute on a stated "
                                 "convention of the source's judge prompt."),
    ("da50cd1", R11_ANSWERS, 23, "The log-linear reading of \"half-count\" and the one-sided Fisher are recorded as "
                                 "Code's readings, as the raw states them."),
    ("da50cd1", R11_ANSWERS, 50, "3. **‡(c)'s grading premise.** Settled by the v1 raw, §2: Table 4 grades "
                                 "non-answering and incoherent responses NO. What is not settled is whether a later "
                                 "pipeline step excludes them"),
    ("da50cd1", V1RAW, 18, "## 2. Table 4 — the detection judge's grading rule (the ‡(c) premise"),
    ("da50cd1", V1RAW, 23, "Only mark as YES if BOTH conditions are met"),
    ("da50cd1", V1RAW, 25, "If the AI does not answer the question, the answer is NO."),
    ("da50cd1", V1RAW, 27, "The detection judge returns NO for a response that does not answer the question and for an "
                           "incoherent, nonsensical or repetitive response; such responses are graded (as NO), not "
                           "excluded from the denominator by this prompt."),
    ("da50cd1", V1RAW, 29, "Whether any later step of the source's pipeline excludes such trials before the rate is "
                           "computed (a filter outside the judge prompt) is not stated on p. 19; the note's convention "
                           "rests on the judge prompt as written."),
]
STAGES = ("base", "sft", "dpo", "instruct")
STAMP_PREFIX = "- Code stamp: "

# The 24 rows of the seat list's section 2b (results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md@d5123bf;
# O35 of round 11's claims ledger), with their note line, unit and clause as round 11's rows give them. Each clause is
# asserted on its v0.8 line and each unit inside its clause; main() asserts that section 2b's five row groups expand
# to these 24 keys.
ROWS = [
    ("S8#2032", 230, "17/96", "On that convention, with every excluded trial counted NO, our rates measure 17/96 = 0.177 at SFT, 0/96 at DPO and at instruct, and 25/96 = 0.260 at base."),
    ("S8#2033", 230, "0.177", "On that convention, with every excluded trial counted NO, our rates measure 17/96 = 0.177 at SFT, 0/96 at DPO and at instruct, and 25/96 = 0.260 at base."),
    ("S8#2034", 230, "0/96", "On that convention, with every excluded trial counted NO, our rates measure 17/96 = 0.177 at SFT, 0/96 at DPO and at instruct, and 25/96 = 0.260 at base."),
    ("S8#2035", 230, "25/96", "On that convention, with every excluded trial counted NO, our rates measure 17/96 = 0.177 at SFT, 0/96 at DPO and at instruct, and 25/96 = 0.260 at base."),
    ("S8#2036", 230, "0.260", "On that convention, with every excluded trial counted NO, our rates measure 17/96 = 0.177 at SFT, 0/96 at DPO and at instruct, and 25/96 = 0.260 at base."),
    ("S8#2037", 230, "12/48", "The SFT-injected arm measures 12/48 vs. 9/48 on it (+0.06, *p* = .31)."),
    ("S8#2038", 230, "9/48", "The SFT-injected arm measures 12/48 vs. 9/48 on it (+0.06, *p* = .31)."),
    ("S8#2039", 230, "0.06", "The SFT-injected arm measures 12/48 vs. 9/48 on it (+0.06, *p* = .31)."),
    ("S8#2040", 230, ".31", "The SFT-injected arm measures 12/48 vs. 9/48 on it (+0.06, *p* = .31)."),
    ("S8#2095", 236, "10,000", "Pooled over the twenty configurations, that convention gives a fifth premise, 10,000/200"),
    ("S8#2097", 236, "200", "Pooled over the twenty configurations, that convention gives a fifth premise, 10,000/200"),
    ("S8#2098", 236, ".003", "at which the DPO difference is significant (*p* ≈ .003; corrected *d*′ ≈ 0.9)"),
    ("S8#2099", 236, "0.9", "at which the DPO difference is significant (*p* ≈ .003; corrected *d*′ ≈ 0.9)"),
    ("S8#2100", 236, ".17", "and the instruct difference is not (*p* ≈ .17)"),
    ("S5#2055", 110, "2.2", "*c* moves from ≈ 2.2–2.5 to ≈ 0.55"),
    ("S5#2056", 110, "2.5", "*c* moves from ≈ 2.2–2.5 to ≈ 0.55"),
    ("S5#2057", 110, "0.55", "*c* moves from ≈ 2.2–2.5 to ≈ 0.55"),
    ("S5#2059", 110, "1.85", "pre-ablation *d*′ is 1.85–2.48 vs. 1.8 after"),
    ("S5#2060", 110, "2.48", "pre-ablation *d*′ is 1.85–2.48 vs. 1.8 after"),
    ("S8#3019", 242, "0.55", "Post-ablation, uncorrected *d*′ ≈ 1.8 at *c* ≈ 0.55"),
    ("S8#3022", 242, "1.85", "Pre-ablation the false-positive cell is zero, so with the same half-count correction *d*′ = 1.85 at one control trial per concept and 2.48 at the released code's ten, with *c* ≈ 2.2 and 2.5"),
    ("S8#3024", 242, "2.48", "Pre-ablation the false-positive cell is zero, so with the same half-count correction *d*′ = 1.85 at one control trial per concept and 2.48 at the released code's ten, with *c* ≈ 2.2 and 2.5"),
    ("S8#3026", 242, "2.2", "Pre-ablation the false-positive cell is zero, so with the same half-count correction *d*′ = 1.85 at one control trial per concept and 2.48 at the released code's ten, with *c* ≈ 2.2 and 2.5"),
    ("S8#3027", 242, "2.5", "Pre-ablation the false-positive cell is zero, so with the same half-count correction *d*′ = 1.85 at one control trial per concept and 2.48 at the released code's ten, with *c* ≈ 2.2 and 2.5"),
]
# the note's own words this raw quotes outside the 24 clauses, each asserted on its line
NOTE_QUOTES = [
    (99, "one-sided Fisher exact *p* = .22"),
    (101, "that value is set by the half-count imputation on the zero cell"),
    (230, "Macar et al. 2026 methods grade a non-answering or incoherent response NO and retain it (v1, Table 4)"),
    (230, "The stage pattern and the pairwise interval separation the replication criterion requires hold for either "
          "denominator"),
    (242, "On either count the ablation lowers the criterion, and no rise in *d*\u2032 is needed to account for it"),
]
SEAT_GROUPS = ("S8#2032–S8#2036", "S8#2037–S8#2040", "S8#2095, S8#2097–S8#2100",
               "S5#2055, S5#2056, S5#2057, S5#2059, S5#2060", "S8#3019, S8#3022, S8#3024, S8#3026, S8#3027")


# ----------------------------------------------------------------------------------------------------- git reads
_cache: dict = {}


def git(*args: str) -> bytes:
    return subprocess.run(["git", "-C", REPO, *args], capture_output=True, check=True).stdout


def show(rev: str, path: str) -> bytes:
    k = (rev, path)
    if k not in _cache:
        _cache[k] = git("show", f"{rev}:{path}")
    return _cache[k]


def lines(rev: str, path: str) -> list:
    return show(rev, path).decode("utf-8").split("\n")


def line(rev: str, path: str, n: int) -> str:
    return lines(rev, path)[n - 1]


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def full_rev(rev: str) -> str:
    return git("rev-parse", "--verify", f"{rev}^{{commit}}").decode().strip()


def head_line(rev: str, path: str, n: int):
    """The same line's number in the HEAD blob: n if the blobs are equal, else the unique exact match, else None."""
    if show(rev, path) == show("HEAD", path):
        return n
    t = line(rev, path, n)
    hits = [i + 1 for i, x in enumerate(lines("HEAD", path)) if x == t]
    return hits[0] if len(hits) == 1 else None


def jlines(rev: str, path: str, seq):
    """Lines of a pretty-printed (indent=1) JSON blob: seq is a list of (depth, key); each key is the next line at
    that indentation after the previous match. Returns [(line number, stripped line text)]."""
    ls = lines(rev, path)
    out, pos = [], 0
    for depth, key in seq:
        pat = re.compile("^" + " " * depth + '"' + re.escape(key) + '":')
        while not pat.match(ls[pos]):
            pos += 1
        out.append((pos + 1, ls[pos].strip()))
        pos += 1
    return out


def jval(text: str):
    """The JSON value on a 'key: value,' line."""
    return json.loads(text.split(":", 1)[1].strip().rstrip(","))


# ----------------------------------------------------------------------------------------------------- inputs
INPUTS = {}   # id -> dict(rev, path, ln, text, frag, vals, status, what)


def md_input(iid, rev, path, ln, anchor, frags, conv, status, what):
    """Read line ln of path@rev; assert the anchor (the line's identity) and each fragment pattern; record the
    fragments' matched text (the values as printed there) and the values conv() reads from the fragment matches."""
    t = line(rev, path, ln)
    if not re.search(anchor, t):
        raise SystemExit(f"input {iid}: anchor not found at {path}@{rev}:{ln}: {t!r}")
    ms = [re.search(f, t) for f in frags]
    if not all(ms):
        raise SystemExit(f"input {iid}: a fragment is not on {path}@{rev}:{ln}: {t!r}")
    vals = conv(*ms)
    INPUTS[iid] = dict(rev=rev, path=path, ln=ln, text=t, frag=" … ".join(m.group(0) for m in ms), vals=vals,
                       status=status, what=what, head=head_line(rev, path, ln))
    return vals


def json_input(iid, rev, path, seq, expect, status, what):
    """Locate the JSON lines and assert each line's value equals the parsed blob's value (expect: list of the values
    in seq order for the keys whose line carries a scalar; None entries are not asserted)."""
    found = jlines(rev, path, seq)
    vals = []
    for (ln, txt), e in zip(found, expect):
        if e is not None:
            v = jval(txt)
            if v != e:
                raise SystemExit(f"input {iid}: {path}@{rev}:{ln} carries {v!r}, expected {e!r}")
            vals.append((ln, txt, v))
    INPUTS[iid] = dict(rev=rev, path=path, ln=None, json_lines=vals, vals=[v for _, _, v in vals], status=status,
                       what=what, head=None if show(rev, path) != show("HEAD", path) else "same")
    return [v for _, _, v in vals]


def read_inputs():
    # (c): the criterion arm's counts per stage, as N2 1(a) prints them and as the artifacts store them
    for i, s in enumerate(STAGES):
        md_input(f"C-{s}", "09c3a8c", N2, 90 + i, r"^\| " + s + r" \| .*\| reproduced \|$",
                 [r"0\.\d{4} \((\d+)/(\d+)\) \| (\d+) \| (\d+) / (\d+) \|"],
                 lambda m: dict(affirm=int(m.group(1)), decidable=int(m.group(2)), run=int(m.group(3)),
                                und_audit=int(m.group(4)), und_scorer=int(m.group(5))),
                 "reproduced (N2 1(a))", f"criterion arm (B2-r section 1, control trials), {s}: FPR (k/n) | trials "
                                         "run | undecidable audit / scorer")
        d = json.loads(show("bbc9ffe", CTRL.format(s)))
        json_input(f"A-{s}", "bbc9ffe", CTRL.format(s), [(1, "n"), (1, "decidable"), (1, "affirm")],
                   [d["n"], d["decidable"], d["affirm"]], "the record's artifact",
                   f"criterion-arm artifact, {s}: n, decidable, affirm")
        tr = d["trials"]
        INPUTS[f"A-{s}"]["recount"] = dict(trials=len(tr), affirm=sum(t["claimed_detection"] is True for t in tr),
                                           decidable=sum(t["claimed_detection"] is not None for t in tr),
                                           injected=sum(bool(t["injected"]) for t in tr))
    # (c): the SFT injected (exploration) arm
    md_input("E-hit", "09c3a8c", N2, 61, r"^\| 38 \| .*\| reproduced \|", [r"exploration sft: hits (\d+)/(\d+)"],
             lambda m: dict(hit=int(m.group(1)), inj_decidable=int(m.group(2))), "reproduced (N2 row 38)",
             "SFT exploration hits / injected decidable trials")
    md_input("E-fa", "09c3a8c", N2, 62, r"^\| 39 \| .*\| reproduced \|", [r"exploration sft: FA (\d+)/(\d+)"],
             lambda m: dict(fa=int(m.group(1)), ctl_decidable=int(m.group(2))), "reproduced (N2 row 39)",
             "SFT exploration false alarms / control decidable trials")
    md_input("E-n", "09c3a8c", N2, 136, r"^\| trials per stage \|",
             [r"section 3: (\d+) \((\d+) injected / (\d+) control\) \[reproduced: artifact `n`, trial rows\]"],
             lambda m: dict(run=int(m.group(1)), injected=int(m.group(2)), control=int(m.group(3))),
             "reproduced (N2 1(c))", "B2-r trials per stage, section 3 (the exploration arm)")
    d = json.loads(show("bbc9ffe", EXPL))
    json_input("X-sft", "bbc9ffe", EXPL, [(1, "hit"), (1, "inj_decidable"), (1, "fa"), (1, "ctl_decidable")],
               [d["hit"], d["inj_decidable"], d["fa"], d["ctl_decidable"]], "the record's artifact",
               "SFT exploration artifact: hit, inj_decidable, fa, ctl_decidable")
    tr = d["trials"]
    INPUTS["X-sft"]["recount"] = dict(
        trials=len(tr), injected=sum(t["injected"] is True for t in tr), control=sum(t["injected"] is False for t in tr),
        hit=sum(t["injected"] is True and t["claimed_detection"] is True for t in tr),
        fa=sum(t["injected"] is False and t["claimed_detection"] is True for t in tr),
        inj_undecidable=sum(t["injected"] is True and t["claimed_detection"] is None for t in tr),
        ctl_undecidable=sum(t["injected"] is False and t["claimed_detection"] is None for t in tr))
    # (f): the source's v1 pooled rates (N2vi rows 3, 4, 7, 8), the twenty configurations (row 11), and v5's C.2 counts
    md_input("R-dpo-tpr", "09c3a8c", N2VI, 21, r"^\| 3 \| .*\| log-only \|",
             [r"source dpo TPR 0\.029", r"record 0\.029; source v1 text (0\.029)"],
             lambda a, b: dict(tpr=b.group(1)), "log-only (N2vi row 3)", "source DPO TPR, v1 Appendix C")
    md_input("R-ins-tpr", "09c3a8c", N2VI, 22, r"^\| 4 \| .*\| log-only \|",
             [r"source instruct TPR 0\.009", r"record 0\.009; source v1 text (0\.009)"],
             lambda a, b: dict(tpr=b.group(1)), "log-only (N2vi row 4)", "source instruct TPR, v1 Appendix C")
    md_input("R-dpo-fpr", "09c3a8c", N2VI, 25, r"^\| 7 \| .*\| log-only \|",
             [r"source dpo FPR 0\.000", r"record A 0\.000 / record B 0\.000; source v1 text (0\.000)"],
             lambda a, b: dict(fpr=b.group(1)), "log-only (N2vi row 7)", "source DPO FPR, v1 Appendix C")
    md_input("R-ins-fpr", "09c3a8c", N2VI, 26, r"^\| 8 \| .*\| discrepant \|",
             [r"source instruct FPR 0\.003", r"record A (0\.003) / record B 0\.003; source v1 text (0\.000)"],
             lambda a, b: dict(fpr=b.group(2), record=b.group(1)),
             "discrepant (N2vi row 8: record 0.003, source v1 text 0.000; R1 rules the note's 0.000)",
             "source instruct FPR, v1 Appendix C")
    md_input("R-cfg", "09c3a8c", N2VI, 29, r"^\| 11 \| .*\| log-only \|",
             [r"aggregation over L in \[25, 32, 38, 45, 51\] x alpha in \[1, 2, 4, 8\] \((\d+) configurations\)"],
             lambda m: dict(n_configs=int(m.group(1))), "log-only (N2vi row 11)",
             "the pooled rates' aggregation, 5 layers x 4 strengths")
    j = json.loads(show("09c3a8c", N2VI_JSON))
    json_input("J-cfg", "09c3a8c", N2VI_JSON, [(1, "grid"), (2, "n_configs")], [None, j["grid"]["n_configs"]],
               "N2vi's audit JSON (row 11's machine-readable carrier)", "grid.n_configs")
    json_input("J-ctl", "09c3a8c", N2VI_JSON, [(1, "grid"), (2, "per_concept_per_cell"), (3, "control")],
               [None, None, j["grid"]["per_concept_per_cell"]["control"]], "N2vi's audit JSON (the code defaults)",
               "grid.per_concept_per_cell.control")
    json_input("J-dpo", "09c3a8c", N2VI_JSON, [(1, "stages"), (2, "dpo"), (3, "tpr"), (3, "fpr")],
               [None, None, j["stages"]["dpo"]["tpr"], j["stages"]["dpo"]["fpr"]],
               "N2vi's audit JSON (rows 3 and 7's machine-readable carrier)", "stages.dpo.tpr, fpr")
    json_input("J-ins", "09c3a8c", N2VI_JSON, [(1, "stages"), (2, "instruct"), (3, "tpr"), (3, "fpr"),
                                               (3, "record_addendum_fpr")],
               [None, None, j["stages"]["instruct"]["tpr"], j["stages"]["instruct"]["fpr"],
                j["stages"]["instruct"]["record_addendum_fpr"]],
               "N2vi's audit JSON (rows 4 and 8's machine-readable carrier)", "stages.instruct.tpr, fpr, record_addendum_fpr")
    md_input("V-c2", "8d68b0b", N2VII, 89, r"^- \*\*The one OLMo-inclusive passage with counts\.\*\* p\. 25, Appendix C\.2",
             [r"aggregated over 50 concepts \S 10 trial numbers \((\d+) injection trials\) and (\d+) control trials per "
              r"\(layer, strength\)"], lambda m: dict(inj=int(m.group(1)), ctl=int(m.group(2))),
             "transcription of v5 (pin class 4b)", "v5 Appendix C.2: counts per (layer, strength)")
    # (i): the ablation rates, the defaults, and the control-count premises
    md_input("B-intact", "e60b633", N2, 81, r"^\| 58 \| theirs ablation rates, refusal direction intact: .*\| log-only \|",
             [r"hits (0\.108), false alarms (0\.000) \(rates only; no n\)"], lambda m: dict(H=m.group(1), F=m.group(2)),
             "log-only (N2 row 58)", "Gemma-3-27B, refusal direction intact")
    md_input("B-ablated", "e60b633", N2, 82, r"^\| 59 \| theirs ablation rates, refusal direction ablated: .*\| log-only \|",
             [r"hits (0\.638), false alarms (0\.073) \(rates only; no n\)"], lambda m: dict(H=m.group(1), F=m.group(2)),
             "log-only (N2 row 59)", "Gemma-3-27B, refusal direction ablated")
    md_input("B-5f-intact", "e60b633", N2, 444, r"^\| refusal direction intact \(the pre-ablation baseline\) \|",
             [r"\| (0\.108) \| (0\.000) \| not stated \| undefined \(FA = 0; no correction applied\) \| none \|$"],
             lambda m: dict(H=m.group(1), F=m.group(2)), "log-only rates (N2 5(f))", "N2 5(f) table, intact")
    md_input("B-5f-ablated", "e60b633", N2, 445, r"^\| refusal direction ablated \(abliterated\) \|",
             [r"\| (0\.638) \| (0\.073) \| not stated \| \+(1\.8069) \| none \|$"],
             lambda m: dict(H=m.group(1), F=m.group(2), d=m.group(3)),
             "log-only rates; d' computed-new (N2 5(f), row 60)", "N2 5(f) table, ablated")
    md_input("B-5f-z", "e60b633", N2, 447, r"^With the direction ablated, ",
             [r"d' = z\(0\.638\) - z\(0\.073\) = \+(0\.3531) - \((-1\.4538)\) = \+(1\.8069)"],
             lambda m: dict(zH=m.group(1), zF=m.group(2), d=m.group(3)), "computed-new (N2 5(f))",
             "N2 5(f): the z values and the uncorrected d'")
    md_input("B-rec-a", "bbc9ffe", RES, 7487, r"^    Their README quotes",
             [r"Their README quotes \*\*(10\.8)%\*\* as the pre-abliteration baseline"],
             lambda m: dict(H=m.group(1)), "log-only (record prose)", "the record line N2 rows 58-59 cite")
    md_input("B-rec-b", "bbc9ffe", RES, 7488, r"^    rate \(rising to",
             [r"rate \(rising to (63\.8)% abliterated, FA (0)% \S (7\.3)%\)"],
             lambda m: dict(H=m.group(1), F0=m.group(2), F1=m.group(3)), "log-only (record prose)",
             "the record line N2 rows 58-59 cite")
    md_input("V-rates", "8d68b0b", N2VII, 97, r"^> Figure 4 \(right\) shows that abliteration",
             [r"abliteration increases TPR from (10\.8)% to (63\.8)%", r"increasing FPR only modestly from (0\.0)% to (7\.3)%"],
             lambda a, b: dict(H0=a.group(1), H1=a.group(2), F0=b.group(1), F1=b.group(2)),
             "transcription of v5 (pin class 4b)", "v5 section 3.3: the ablation rates")
    md_input("V-concepts", "8d68b0b", N2VII, 68, r"^- p\. 22, Appendix B\.1 \"Concepts\"",
             [r"We use (\d+) concepts across all experiments unless otherwise specified"],
             lambda m: dict(concepts=int(m.group(1))), "transcription of v5 (pin class 4b)",
             "v5 Appendix B.1: concepts, paper-wide default")
    md_input("V-trials", "8d68b0b", N2VII, 78, r"^- \*\*Paper-wide default\.\*\* p\. 22, Appendix B\.3",
             [r"We use (\d+) injection trials per concept \(10 trial numbers \S 10 samples each\) unless otherwise "
              r"specified"], lambda m: dict(per_concept=int(m.group(1))), "transcription of v5 (pin class 4b)",
             "v5 Appendix B.3: injection trials per concept, paper-wide default")
    md_input("K-res-a", "bbc9ffe", RES, 7435, r"^    `DEFAULT_MAX_TRIAL_NUMBER",
             [r"`DEFAULT_MAX_TRIAL_NUMBER = (\d+)`, `DEFAULT_SAMPLES_PER_TRIAL = (\d+)`"],
             lambda m: dict(trial_numbers=int(m.group(1)), samples=int(m.group(2))), "log-only (record prose)",
             "the released code's defaults as the record states them (experiments/03_behavioral_robustness.py, "
             "RESULTS.md@bbc9ffe:7428-7432)")
    md_input("K-res-b", "bbc9ffe", RES, 7436, r"so 10\S10 = 100 per concept",
             [r"`DEFAULT_CONTROL_SAMPLES_PER_TRIAL = (\d+)`"],
             lambda m: dict(control_samples=int(m.group(1))), "log-only (record prose)", "the same, control samples per trial")
    md_input("K-n2", "09c3a8c", N2, 136, r"^\| trials per stage \|",
             [r"(\d+) \(10 trial numbers x 1 sample\) control \(code defaults\) \[log-only: the record states the code "
              r"defaults at RESULTS\.md@bbc9ffe:7435-7436\]"], lambda m: dict(control_per_concept=int(m.group(1))),
             "log-only (N2 1(c))", "N2's reading of those defaults: control trials per concept per cell")
    md_input("R-ten", "09c3a8c", N2VI, 30, r"^\| 12 \| .*\| log-only \|",
             [r"eight concepts x the code's (\d+) / (\d+) per concept"],
             lambda m: dict(injected_per_concept=int(m.group(1)), control_per_concept=int(m.group(2))),
             "log-only (N2vi row 12; the released code's ten, the seat list's §5 #9)", "the code's trials per concept, injected / control")


# ----------------------------------------------------------------------------------------------------- statistics
Z = NormalDist().inv_cdf


def n2_functions():
    """N2's own definitions, compiled from scripts/audit_note_N2.py@e60b633 into an isolated namespace (whole top-level
    definitions, by name; not re-implemented): Z, dprime_ll, fisher_hits_gt_fa, half_up."""
    src = show("e60b633", N2_SCRIPT).decode("utf-8")
    tree = ast.parse(src)
    segs = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in ("dprime_ll", "fisher_hits_gt_fa", "half_up"):
            segs.append((node.lineno, node.end_lineno, node.name, ast.get_source_segment(src, node)))
        elif isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "Z" for t in node.targets):
            segs.append((node.lineno, node.end_lineno, "Z", ast.get_source_segment(src, node)))
    segs.sort()
    assert [s[2] for s in segs] == ["Z", "dprime_ll", "fisher_hits_gt_fa", "half_up"], segs
    ns = {"math": math, "Fraction": Fraction, "NormalDist": NormalDist, "__builtins__": __builtins__}
    for lo, hi, name, s in segs:
        exec(compile(s, f"{N2_SCRIPT}@e60b633:{lo}-{hi}", "exec"), ns)
    return ns, segs


def fisher_one_sided_mine(h: int, ns: int, fa: int, nn: int) -> Fraction:
    """This script's own one-sided Fisher exact (H1: hit rate > FA rate), parameterized by the success margin:
    P(X >= h), P(X = x) = C(K, x) C(N - K, ns - x) / C(N, ns), K = h + fa, N = ns + nn. Exact."""
    n_, k_ = ns + nn, h + fa
    num = sum(math.comb(k_, x) * math.comb(n_ - k_, ns - x) for x in range(h, min(k_, ns) + 1))
    return Fraction(num, math.comb(n_, ns))


def fisher_two_sided(h: int, ns: int, fa: int, nn: int) -> Fraction:
    """Two-sided Fisher exact: the sum of P(x) over every table with P(x) <= P(observed), margins fixed. Exact."""
    n_, k_ = ns + nn, h + fa
    pm = {x: math.comb(ns, x) * math.comb(nn, k_ - x) for x in range(max(0, k_ - nn), min(ns, k_) + 1)}
    return Fraction(sum(v for v in pm.values() if v <= pm[h]), math.comb(n_, k_))


def dprime_zero_cell(h: int, ns: int, fa: int, nn: int):
    """Sensitivity only: the zero-cell-only half-count rule. A rate of 0 becomes 1/(2N), a rate of 1 becomes
    1 - 1/(2N); every other rate is used as observed. Returns (d', c)."""
    def adj(k, n):
        return 0.5 / n if k == 0 else (1 - 0.5 / n if k == n else k / n)
    hp, fp = adj(h, ns), adj(fa, nn)
    return Z(hp) - Z(fp), -(Z(hp) + Z(fp)) / 2


def uncorrected(H: float, F: float):
    return Z(H) - Z(F), -(Z(H) + Z(F)) / 2


# ----------------------------------------------------------------------------------------------------- formatting
def dec(x) -> Decimal:
    if isinstance(x, Fraction):
        with localcontext() as ctx:
            ctx.prec = 80
            return Decimal(x.numerator) / Decimal(x.denominator)
    if isinstance(x, int):
        return Decimal(x)
    return Decimal(x)            # a float's exact binary expansion


def sig20(x) -> str:
    with localcontext() as ctx:
        ctx.prec = 20
        return str(+dec(x))


def full(x) -> str:
    """Full precision: an exact rational to 20 significant digits; a float64 as its shortest round-trip repr."""
    if isinstance(x, Fraction):
        return f"{x.numerator}/{x.denominator} = {sig20(x)}" if x.denominator < 10 ** 6 else f"{sig20(x)} (exact rational, 20 significant digits)"
    return repr(x)


def check_round(value, printed: str):
    """(agrees, decimals, half-up rounding of the exact value at the printed decimals, margin to the nearer edge of
    the printed value's rounding interval)."""
    s = printed.lstrip("+")
    d = len(s.split(".")[1]) if "." in s else 0
    q = Decimal(1).scaleb(-d)
    v = dec(value)
    r = v.quantize(q, rounding=ROUND_HALF_UP)
    tgt = Decimal(s)
    half = q / 2
    margin = min(v - (tgt - half), (tgt + half) - v)
    return r == tgt, d, r, margin


def cell(s) -> str:
    return str(s).replace("|", "\\|")


def repo_rel(p: str, top: str):
    """p relative to the repository's top level when it lies inside it, else None. Its directories are resolved; its
    last component is kept as named, so an interpreter linked from a virtual environment keeps its own path."""
    q = os.path.abspath(p)
    q = os.path.join(os.path.realpath(os.path.dirname(q)), os.path.basename(q))
    t = os.path.realpath(top)
    return os.path.relpath(q, t) if os.path.commonpath([q, t]) == t else None


def code(s) -> str:
    """A Markdown code span that survives backticks inside the text: the delimiter is one backtick longer than the
    longest run inside, padded with a space where the text has any backtick."""
    s = str(s)
    n = max((len(r) for r in re.findall(r"`+", s)), default=0) + 1
    pad = " " if n > 1 else ""
    return f"{'`' * n}{pad}{s}{pad}{'`' * n}"


def loc(iid: str) -> str:
    x = INPUTS[iid]
    if x.get("ln") is None:
        ls = sorted(ln for ln, _, _ in x["json_lines"])
        rng = f"{ls[0]}" if len(ls) == 1 else ", ".join(f"{a}" for a in ls)
        return f"`{x['path']}@{x['rev']}`:{rng}"
    h = x["head"]
    tail = "" if h == x["ln"] else (f" (HEAD :{h})" if h else " (not at HEAD)")
    return f"`{x['path']}@{x['rev']}`:{x['ln']}{tail}"


def unit_occurrences(clause: str, unit: str) -> int:
    pat = re.compile(r"(?<![0-9.,])" + re.escape(unit) + r"(?![0-9])")
    return len(pat.findall(clause))


# ----------------------------------------------------------------------------------------------------- main
def main() -> int:
    global REPO
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--repo", default=None, help="the repository whose blobs are read with git show (default: the "
                    "repository this script is in)")
    a = ap.parse_args()
    if a.repo is not None:
        REPO = a.repo

    head = git("rev-parse", "HEAD").decode().strip()
    revs = {r: full_rev(r) for r in ("0de15a1", "09c3a8c", "e60b633", "8d68b0b", "bbc9ffe", "2fb0cf0", "908a659",
                                     "f935864", "d5123bf", "da50cd1")}
    for r, f in revs.items():
        subprocess.run(["git", "-C", REPO, "merge-base", "--is-ancestor", f, head], check=True)

    # the note, its hash, and the 24 rows' clauses and units on their lines
    note_b = show(NOTE_REV, NOTE)
    note_sha = sha256(note_b)
    if note_sha != NOTE_SHA:
        raise SystemExit(f"note sha256 {note_sha} != routed {NOTE_SHA}")
    note_ls = note_b.decode("utf-8").split("\n")
    for key, ln, unit, clause in ROWS:
        if clause not in note_ls[ln - 1]:
            raise SystemExit(f"{key}: clause not on v0.8 :{ln}")
        if unit_occurrences(clause, unit) != 1:
            raise SystemExit(f"{key}: unit {unit!r} occurs {unit_occurrences(clause, unit)} times in its clause")
    assert len(ROWS) == 24 and len({r[0] for r in ROWS}) == 24
    for ln, q in NOTE_QUOTES:
        if q not in note_ls[ln - 1]:
            raise SystemExit(f"note quote not on v0.8 :{ln}: {q!r}")

    # the 24 keys against the seat list's section 2b, read with git show at its revision (the committed list)
    st = show("d5123bf", SEAT).decode("utf-8")
    sec = st.split("### 2b.", 1)[1].split("\n### ", 1)[0]
    keys = []
    for g in SEAT_GROUPS:
        if g not in sec:
            raise SystemExit(f"seat list: group {g!r} not in section 2b")
        for part in g.split(", "):
            if "–" in part:
                p0, p1 = part.split("–")
                span, s0 = p0.split("#")
                keys += [f"{span}#{i}" for i in range(int(s0), int(p1.split("#")[1]) + 1)]
            else:
                keys.append(part)
    if sorted(keys) != sorted(r[0] for r in ROWS):
        raise SystemExit(f"seat list: section 2b's row groups expand to {len(keys)} keys, not this script's 24")

    read_inputs()
    for rev, path, ln, txt in CITED:
        if txt not in line(rev, path, ln):
            raise SystemExit(f"cited line {path}@{rev}:{ln} does not carry {txt!r}")
    N2F, n2segs = n2_functions()
    n2_ll, n2_fisher, n2_half_up, n2_Z = N2F["dprime_ll"], N2F["fisher_hits_gt_fa"], N2F["half_up"], N2F["Z"]

    # ------------------------------------------------------------- input consistency (markdown vs artifacts)
    cons = []
    for s in STAGES:
        c, aa = INPUTS[f"C-{s}"]["vals"], INPUTS[f"A-{s}"]
        n_, dcd, aff = [v for _, _, v in aa["json_lines"]]
        rc = aa["recount"]
        ok = (c["run"] == n_ == rc["trials"] and c["decidable"] == dcd == rc["decidable"]
              and c["affirm"] == aff == rc["affirm"] and c["und_audit"] + c["und_scorer"] == c["run"] - c["decidable"]
              and rc["injected"] == 0)
        cons.append((s, ok, c, (n_, dcd, aff), rc))
        if not ok:
            raise SystemExit(f"criterion-arm inputs disagree at {s}")
    e_hit, e_fa, e_n = INPUTS["E-hit"]["vals"], INPUTS["E-fa"]["vals"], INPUTS["E-n"]["vals"]
    xs = [v for _, _, v in INPUTS["X-sft"]["json_lines"]]
    xr = INPUTS["X-sft"]["recount"]
    assert (e_hit["hit"], e_hit["inj_decidable"], e_fa["fa"], e_fa["ctl_decidable"]) == tuple(xs)
    assert (xr["trials"], xr["injected"], xr["control"]) == (e_n["run"], e_n["injected"], e_n["control"]) == (96, 48, 48)
    assert (xr["hit"], xr["fa"]) == (e_hit["hit"], e_fa["fa"])
    assert xr["inj_undecidable"] == e_n["injected"] - e_hit["inj_decidable"]
    assert xr["ctl_undecidable"] == e_n["control"] - e_fa["ctl_decidable"]
    j_cfg, j_ctl = INPUTS["J-cfg"]["vals"][0], INPUTS["J-ctl"]["vals"][0]
    j_dpo, j_ins = INPUTS["J-dpo"]["vals"], INPUTS["J-ins"]["vals"]
    assert j_cfg == INPUTS["R-cfg"]["vals"]["n_configs"] == 20
    assert Fraction(str(j_dpo[0])) == Fraction(INPUTS["R-dpo-tpr"]["vals"]["tpr"])
    assert Fraction(str(j_dpo[1])) == Fraction(INPUTS["R-dpo-fpr"]["vals"]["fpr"])
    assert Fraction(str(j_ins[0])) == Fraction(INPUTS["R-ins-tpr"]["vals"]["tpr"])
    assert Fraction(str(j_ins[1])) == Fraction(INPUTS["R-ins-fpr"]["vals"]["fpr"])
    assert Fraction(str(j_ins[2])) == Fraction(INPUTS["R-ins-fpr"]["vals"]["record"])
    b0, b1 = INPUTS["B-intact"]["vals"], INPUTS["B-ablated"]["vals"]
    assert b0 == {k: INPUTS["B-5f-intact"]["vals"][k] for k in ("H", "F")}
    assert b1 == {k: INPUTS["B-5f-ablated"]["vals"][k] for k in ("H", "F")}
    vr, rca, rcb = INPUTS["V-rates"]["vals"], INPUTS["B-rec-a"]["vals"], INPUTS["B-rec-b"]["vals"]
    assert Fraction(vr["H0"]) / 100 == Fraction(b0["H"]) == Fraction(rca["H"]) / 100
    assert Fraction(vr["H1"]) / 100 == Fraction(b1["H"]) == Fraction(rcb["H"]) / 100
    assert Fraction(vr["F0"]) / 100 == Fraction(b0["F"]) == Fraction(rcb["F0"]) / 100
    assert Fraction(vr["F1"]) / 100 == Fraction(b1["F"]) == Fraction(rcb["F1"]) / 100
    ctl_per_concept = INPUTS["K-res-a"]["vals"]["trial_numbers"] * INPUTS["K-res-b"]["vals"]["control_samples"]
    assert ctl_per_concept == INPUTS["K-n2"]["vals"]["control_per_concept"] == j_ctl == 10
    assert INPUTS["R-ten"]["vals"] == dict(injected_per_concept=100, control_per_concept=10)
    assert INPUTS["K-res-a"]["vals"]["trial_numbers"] * INPUTS["K-res-a"]["vals"]["samples"] == \
        INPUTS["V-trials"]["vals"]["per_concept"] == 100

    # ------------------------------------------------------------- the functions against committed outputs
    roc = json.loads(show("e60b633", N2_ROC))
    calib = []

    def calrow(label, h, ns, fa, nn, d_s, c_s, p_s):
        d1, c1 = n2_ll(h, ns, fa, nn)
        p1 = n2_fisher(h, ns, fa, nn)
        p2 = float(fisher_one_sided_mine(h, ns, fa, nn))
        dd = max(abs(d1 - d_s), abs(c1 - c_s), abs(p1 - p_s), abs(p2 - p_s))
        calib.append((label, h, ns, fa, nn, d1 == d_s and c1 == c_s and p1 == p_s and p2 == p_s, dd))

    srcrates = json.loads(show("09c3a8c", N2VI_JSON))["stages"]
    for r in roc["theirs_n_sensitivity"]:
        st = srcrates[r["stage"]]
        assert n2_half_up(Fraction(str(st["tpr"])) * r["n_signal"]) == r["hits"]
        assert n2_half_up(Fraction(str(st["fpr"])) * r["n_noise"]) == r["fa"]
        calrow(f"theirs_n_sensitivity {r['stage']} {r['n_signal']}/{r['n_noise']}", r["hits"], r["n_signal"], r["fa"],
               r["n_noise"], r["dprime_loglinear"], r["c_loglinear"], r["fisher_p_one_sided"])
    for r in roc["points"]:
        if r.get("hits") is None:
            continue
        calrow(f"points: {r['dataset']} {r['stage']}, {r['arm']}", r["hits"], r["n_signal"], r["fa"], r["n_noise"],
               r["dprime_loglinear"], r["c_loglinear"], r["fisher_p_one_sided"])
    abl = roc["theirs_ablation_uncorrected"]["rows"]
    d_unc, c_unc = uncorrected(abl[1]["hit_rate"], abl[1]["fa_rate"])
    cal_abl = (d_unc == abl[1]["dprime_uncorrected"], abs(d_unc - abl[1]["dprime_uncorrected"]))
    abl_lines = jlines("e60b633", N2_ROC, [(1, "theirs_ablation_uncorrected"), (2, "definition"), (2, "rows"),
                                           (4, "hit_rate"), (4, "fa_rate"), (4, "hit_rate"), (4, "fa_rate"),
                                           (4, "dprime_uncorrected")])
    assert [jval(t) for _, t in abl_lines[3:]] == [abl[0]["hit_rate"], abl[0]["fa_rate"], abl[1]["hit_rate"],
                                                    abl[1]["fa_rate"], abl[1]["dprime_uncorrected"]]
    assert Fraction(str(abl[0]["hit_rate"])) == Fraction(b0["H"]) and Fraction(str(abl[1]["fa_rate"])) == Fraction(b1["F"])
    def_lines = jlines("e60b633", N2_ROC, [(1, "definitions"), (2, "dprime_loglinear"), (2, "c_loglinear"),
                                           (2, "fisher_p_one_sided"), (2, "theirs_counts")])
    # N2 row 57 (the FLAG-3 point) as printed: d' +0.457, c +0.739, p 0.1001
    f3_d, f3_c = n2_ll(12, 40, 7, 44)
    f3_p = n2_fisher(12, 40, 7, 44)
    f3_line = line("e60b633", N2, 80)
    assert "12/40 vs 7/44: sens +0.1409, d' +0.457, c +0.739, one-sided Fisher p 0.1001" in f3_line
    f3_ok = (f"{f3_d:+.3f}", f"{f3_c:+.3f}", f"{f3_p:.4f}") == ("+0.457", "+0.739", "0.1001")

    # the note's other corrected d' values (not among the 24): :99's 0.3 and :101's 0.6, 1.2, 1.5 and 2.0, which their
    # rows map to N2's log-linear outputs; used here only to read what the note means by "corrected"
    if ("corrected *d*′ ≈ 0.3;" not in note_ls[98] or "The corrected *d*′ at DPO measures 0.6, 1.2, 1.5 "
            "and 2.0 across the four premises." not in note_ls[100]):
        raise SystemExit("the note's :99 / :101 corrected d' text is not as expected")

    def pick(rows_, **kw):
        out = [r for r in rows_ if all((v(r.get(k)) if callable(v) else r.get(k) == v) for k, v in kw.items())]
        assert len(out) == 1, kw
        return out[0]
    other = [
        (":99 '0.3', ours SFT exploration", pick(roc["points"], dataset="ours", stage="sft",
                                                   arm=lambda s: s.startswith("exploration")), "0.3", "points"),
        (":101 '0.6', theirs DPO at 800/80", pick(roc["points"], dataset="theirs", stage="dpo",
                                                  arm=lambda s: s.startswith("source aggregate (20")), "0.6", "points"),
        (":101 '1.2', theirs DPO at 5000/500", pick(roc["theirs_n_sensitivity"], stage="dpo", n_signal=5000), "1.2",
         "theirs_n_sensitivity"),
        (":101 '1.5', theirs DPO at 16000/1600", pick(roc["theirs_n_sensitivity"], stage="dpo", n_signal=16000), "1.5",
         "theirs_n_sensitivity"),
        (":101 '2.0', theirs DPO at 100000/10000", pick(roc["theirs_n_sensitivity"], stage="dpo", n_signal=100000),
         "2.0", "theirs_n_sensitivity"),
    ]
    other_rows = []
    for lab, r, pr, where in other:
        v_ll = r["dprime_loglinear"]
        v_z = dprime_zero_cell(r["hits"], r["n_signal"], r["fa"], r["n_noise"])[0]
        other_rows.append((lab, where, r["hits"], r["n_signal"], r["fa"], r["n_noise"], v_ll, v_z, pr,
                           check_round(v_ll, pr)[0], check_round(v_z, pr)[0]))
    other_ll_ok = all(x[9] for x in other_rows)

    # ------------------------------------------------------------- the 24
    C = {s: INPUTS[f"C-{s}"]["vals"] for s in STAGES}
    rate_run = {s: Fraction(C[s]["affirm"], C[s]["run"]) for s in STAGES}
    hit48, fa48 = Fraction(xr["hit"], xr["injected"]), Fraction(xr["fa"], xr["control"])
    diff48 = hit48 - fa48
    p48 = n2_fisher(xr["hit"], xr["injected"], xr["fa"], xr["control"])
    p48_mine = fisher_one_sided_mine(xr["hit"], xr["injected"], xr["fa"], xr["control"])
    assert float(p48_mine) == p48
    p48_two = fisher_two_sided(xr["hit"], xr["injected"], xr["fa"], xr["control"])

    vc2 = INPUTS["V-c2"]["vals"]
    ncfg = INPUTS["R-cfg"]["vals"]["n_configs"]
    NS5, NN5 = vc2["inj"] * ncfg, vc2["ctl"] * ncfg
    fifth = {}
    for s, tpr_k, fpr_k in (("dpo", "R-dpo-tpr", "R-dpo-fpr"), ("instruct", "R-ins-tpr", "R-ins-fpr")):
        tpr = Fraction(INPUTS[tpr_k]["vals"]["tpr"])
        fpr = Fraction(INPUTS[fpr_k]["vals"]["fpr"])
        h, fa = n2_half_up(tpr * NS5), n2_half_up(fpr * NN5)
        d_, c_ = n2_ll(h, NS5, fa, NN5)
        p_ = n2_fisher(h, NS5, fa, NN5)
        pm = fisher_one_sided_mine(h, NS5, fa, NN5)
        assert float(pm) == p_
        fifth[s] = dict(tpr=tpr, fpr=fpr, h=h, fa=fa, d=d_, c=c_, p=pm, p_float=p_,
                        p2=fisher_two_sided(h, NS5, fa, NN5), dz=dprime_zero_cell(h, NS5, fa, NN5))
    rec = Fraction(INPUTS["R-ins-fpr"]["vals"]["record"])
    fa_rec = n2_half_up(rec * NN5)
    h_i = fifth["instruct"]["h"]
    ins_rec = dict(fa=fa_rec, d=n2_ll(h_i, NS5, fa_rec, NN5), p=fisher_one_sided_mine(h_i, NS5, fa_rec, NN5))

    n_conc = INPUTS["V-concepts"]["vals"]["concepts"]
    per_conc = INPUTS["V-trials"]["vals"]["per_concept"]
    NSA = n_conc * per_conc
    H0, F0 = Fraction(b0["H"]), Fraction(b0["F"])
    H1, F1 = Fraction(b1["H"]), Fraction(b1["F"])
    hA, fA = n2_half_up(H0 * NSA), n2_half_up(F0 * NSA)
    assert fA == 0 and Fraction(hA, NSA) == H0
    pre = {}
    for label, nn in (("one control trial per concept", n_conc * 1), ("the released code's ten per concept", n_conc * ctl_per_concept)):
        f0 = n2_half_up(F0 * nn)
        assert f0 == 0
        d_, c_ = n2_ll(hA, NSA, f0, nn)
        pre[nn] = dict(label=label, d=d_, c=c_, dz=dprime_zero_cell(hA, NSA, f0, nn), f=f0)
    post_d, post_c = uncorrected(float(H1), float(F1))
    assert post_d == n2_Z(float(H1)) - n2_Z(float(F1)) == abl[1]["dprime_uncorrected"]
    post_ll = {}
    for nn in (n_conc * 1, n_conc * ctl_per_concept):
        h1, f1 = n2_half_up(H1 * NSA), n2_half_up(F1 * nn)
        post_ll[nn] = dict(h=h1, f=f1, dc=n2_ll(h1, NSA, f1, nn))

    n500, n5000 = n_conc * 1, n_conc * ctl_per_concept
    comp = {   # key -> ((kind, *computed values), input ids, formula)
        "S8#2032": (("frac", C["sft"]["affirm"], C["sft"]["run"]), ["C-sft", "A-sft"], "SFT affirm / trials run"),
        "S8#2033": (("dec", rate_run["sft"]), ["C-sft", "A-sft"], "17/96 as a decimal"),
        "S8#2034": (("frac2", (C["dpo"]["affirm"], C["dpo"]["run"]), (C["instruct"]["affirm"], C["instruct"]["run"])),
                    ["C-dpo", "A-dpo", "C-instruct", "A-instruct"], "DPO and instruct affirm / trials run"),
        "S8#2035": (("frac", C["base"]["affirm"], C["base"]["run"]), ["C-base", "A-base"], "base affirm / trials run"),
        "S8#2036": (("dec", rate_run["base"]), ["C-base", "A-base"], "25/96 as a decimal"),
        "S8#2037": (("frac", xr["hit"], xr["injected"]), ["E-hit", "E-n", "X-sft"], "SFT hits / injected trials run"),
        "S8#2038": (("frac", xr["fa"], xr["control"]), ["E-fa", "E-n", "X-sft"], "SFT false alarms / control trials run"),
        "S8#2039": (("dec", diff48), ["E-hit", "E-fa", "E-n", "X-sft"], "12/48 - 9/48"),
        "S8#2040": (("dec", Fraction(p48_mine)), ["E-hit", "E-fa", "E-n", "X-sft"],
                    "one-sided Fisher exact, H1 hit > FA, on [[12, 36], [9, 39]]"),
        "S8#2095": (("int", NS5), ["V-c2", "R-cfg", "J-cfg"], "500 injection trials per (layer, strength) x 20"),
        "S8#2097": (("int", NN5), ["V-c2", "R-cfg", "J-cfg"], "10 control trials per (layer, strength) x 20"),
        "S8#2098": (("dec", fifth["dpo"]["p"]), ["R-dpo-tpr", "R-dpo-fpr", "J-dpo", "V-c2", "R-cfg"],
                    f"one-sided Fisher exact on [[{fifth['dpo']['h']}, {NS5 - fifth['dpo']['h']}], [{fifth['dpo']['fa']}, {NN5 - fifth['dpo']['fa']}]]"),
        "S8#2099": (("dec", fifth["dpo"]["d"]), ["R-dpo-tpr", "R-dpo-fpr", "J-dpo", "V-c2", "R-cfg"],
                    f"log-linear d' at {fifth['dpo']['h']}/{NS5} vs {fifth['dpo']['fa']}/{NN5}"),
        "S8#2100": (("dec", fifth["instruct"]["p"]), ["R-ins-tpr", "R-ins-fpr", "J-ins", "V-c2", "R-cfg"],
                    f"one-sided Fisher exact on [[{fifth['instruct']['h']}, {NS5 - fifth['instruct']['h']}], [{fifth['instruct']['fa']}, {NN5 - fifth['instruct']['fa']}]]"),
    }
    abl_in_pre = ["B-intact", "B-5f-intact", "V-rates", "V-concepts", "V-trials"]
    abl_in_10 = ["K-res-a", "K-res-b", "K-n2", "R-ten", "J-ctl"]
    abl_in_post = ["B-ablated", "B-5f-ablated", "B-5f-z", "V-rates"]
    for key_s5, key_s8, what in (("S5#2055", "S8#3026", ("c", n500)), ("S5#2056", "S8#3027", ("c", n5000)),
                                 ("S5#2059", "S8#3022", ("d", n500)), ("S5#2060", "S8#3024", ("d", n5000))):
        stat, nn = what
        v = pre[nn][stat]
        ins = abl_in_pre + (abl_in_10 if nn == n5000 else [])
        stat_name = "c" if stat == "c" else "d'"
        f = f"log-linear {stat_name} at {hA}/{NSA} vs 0/{nn} ({pre[nn]['label']})"
        comp[key_s5] = (("dec", v), ins, f)
        comp[key_s8] = (("dec", v), ins, f)
    comp["S5#2057"] = (("dec", post_c), abl_in_post, "uncorrected c = -(z(0.638) + z(0.073))/2")
    comp["S8#3019"] = (("dec", post_c), abl_in_post, "uncorrected c = -(z(0.638) + z(0.073))/2")

    results = []
    for key, ln, unit, clause in ROWS:
        (kind, *vals), ins, formula = comp[key]
        printed = unit
        if kind == "frac":
            k_, n_ = vals
            exp_k, exp_n = (int(x) for x in unit.split("/"))
            ok = (k_, n_) == (exp_k, exp_n)
            computed = f"{k_}/{n_}"
            agree = f"{'agrees' if ok else 'DISAGREES'} (exact)"
        elif kind == "frac2":
            (k1, n1), (k2, n2) = vals
            exp_k, exp_n = (int(x) for x in unit.split("/"))
            ok = (k1, n1) == (exp_k, exp_n) == (k2, n2)
            computed = f"DPO {k1}/{n1}; instruct {k2}/{n2}"
            agree = f"{'agrees' if ok else 'DISAGREES'} (exact, both stages)"
        elif kind == "int":
            (v,) = vals
            ok = v == int(unit.replace(",", ""))
            computed = f"{v:,}" if v >= 10000 else f"{v}"
            agree = f"{'agrees' if ok else 'DISAGREES'} (exact)"
        else:
            (v,) = vals
            if key == "S8#2039":
                printed = "+0.06"
            ok, d, r, margin = check_round(v, printed)
            computed = (f"+{full(v)}" if key == "S8#2039" else full(v))
            agree = (f"{'agrees' if ok else 'DISAGREES'}: half-up at {d} dp = {r}; "
                     f"margin {float(margin):.3g} to the nearer edge of [{Decimal(printed.lstrip('+')) - Decimal(1).scaleb(-d) / 2}, "
                     f"{Decimal(printed.lstrip('+')) + Decimal(1).scaleb(-d) / 2})")
        results.append(dict(key=key, ln=ln, unit=unit, printed=printed, clause=clause, computed=computed, ok=ok,
                            agree=agree, inputs=ins, formula=formula))

    # ------------------------------------------------------------- render
    W = []
    w = W.append
    top = git("rev-parse", "--show-toplevel").decode().strip()
    me = os.path.abspath(__file__)
    me_sha = sha256(open(me, "rb").read())
    # the raw of record is written by the script as committed: its bytes equal its blob at HEAD
    _hb = subprocess.run(["git", "-C", REPO, "show", f"HEAD:{SCRIPT}"], capture_output=True)
    me_head = _hb.stdout if _hb.returncode == 0 and repo_rel(me, top) == SCRIPT else None
    if me_head is None or sha256(me_head) != me_sha:
        raise SystemExit(f"the running script is not {SCRIPT} as committed at HEAD (commit it first); nothing written")
    # paths are printed relative to the repository's top level; none outside it is printed except --out (or --repo),
    # as given on the command line
    me_rel, exe_rel = repo_rel(me, top), repo_rel(sys.executable, top)
    out_shown = repo_rel(a.out, top) or a.out
    ver = sys.version.split()[0]
    me_shown = f"`{me_rel}`" if me_rel else f"`{os.path.basename(me)}` (path outside the repository)"
    exe_shown = f"{exe_rel} (Python {ver})" if exe_rel else f"python3 (path outside the repository; Python {ver})"
    argv = [exe_rel or "python3"] + (["-I"] if sys.flags.isolated else []) + [me_rel or os.path.basename(me)]
    argv += ["--out", out_shown] + ([] if a.repo is None else ["--repo", repo_rel(a.repo, top) or a.repo])
    cmd = " ".join(shlex.quote(x) for x in argv)
    now = datetime.now(timezone.utc)
    stamp = f"{now:%a %b} {now.day:2d} {now:%H:%M:%S} UTC {now.year}"
    n_ok = sum(r["ok"] for r in results)
    n_exact = sum(1 for r in results if comp[r["key"]][0][0] in ("frac", "frac2", "int"))

    w("# note-N1 round 11 (open item O35 of round 11's claims ledger) — the note's own arithmetic on committed inputs: "
      "the 24 figures, computed")
    w("")
    w(f"- **Role.** The raw of record is `{RAW_OF_RECORD}`, written by `{SCRIPT}` as committed (its sha256 below "
      f"equals its blob at HEAD, asserted). The design seat's round-11 answers (`{R11_ANSWERS}@da50cd1`, §0 row 2b: "
      "\"Admit the computation raw; Code regenerates it from its committed script and commits it with its own pin "
      f"class; the 24 rows map audit-raw-new, computed-new.\") admit it, by route (a) of the seat list's §2b "
      f"(`{SEAT}@d5123bf`:266). Its date falls outside N1's item-raw pattern (`results/raw/2026-10-0[89]_note-N…`, "
      "`scripts/audit_note_N1.py@f935864`:2406), so N1's round-11 profile (v0_8, committed with round 11's claims "
      "ledger, after this raw) pins it at the commit that adds it (its own pin class), where its 24 rows map "
      "audit-raw-new, computed-new. As the seat list's §2b said it would (:261), the raw is regenerated from the "
      "committed script, and its references to the seat list's sections point to the committed list. Nothing here "
      "edits the note (frozen; the release-block answers, `908a659`:23), sets a ruling field or edits a row; the 24 "
      "rows' statuses are set by N1's round-11 ledger through the pin class.")
    w(f"{STAMP_PREFIX}{stamp} (UTC, inside the script; with the same arguments at the same HEAD, the one line that "
      f"differs between runs)")
    w(f"- HEAD at run (informational; every read below is pinned to the revision it names): {head}")
    w(f"- Script: {me_shown} sha256 `{me_sha}`; equal to its blob at HEAD: YES (asserted)")
    w(f"- Interpreter: {exe_shown}; standard library only (among them fractions, math, decimal, "
      f"statistics.NormalDist, ast, hashlib, json, re; subprocess for `git show`)")
    w(f"- Command: `{cmd}`")
    w(f"- Reads: every input is read with `git show <rev>:<path>`, every blob hashed (§7). No working-tree file of "
      f"the repository is an input; the script reads its own file only to hash it (Script, above), and the one file "
      f"it writes is this raw (`--out`). No model, no randomness, no network. Pins (each an ancestor of HEAD): "
      + "; ".join(f"`{r}` = {f}" for r, f in revs.items()) + ".")
    w(f"- The note: `{NOTE}@{NOTE_REV}` sha256 `{note_sha}`; as routed in the release-block answers (`908a659`:21) "
      f"`{NOTE_SHA}`: MATCH. Lines 99, 101, 110, 230, 236 "
      f"and 242 are read; every quotation of the note below is asserted on its line. Each row's clause is asserted on "
      f"its line, and its unit inside the clause, exactly once and not inside a longer number.")
    w("- The 24 rows: the seat list's §2b (its heading :228, its table :234–:238, read with `git show` at "
      "`d5123bf`) names them in five row groups ("
      + "; ".join(SEAT_GROUPS) + f"). They expand to {len(keys)} keys, equal to this script's 24: YES (asserted).")
    w("- Status vocabulary: N2's (`results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:20). Every computed "
      "value in §4 is **computed-new**: Code's computation on the committed inputs it lists. Before this raw no "
      "committed carrier printed them (the seat list's §2b heading, :228): the 24 rows were 'not found' on chains "
      "K5, K9 and K10's searches (the seat list's §2, :180). The release block lists them (`2fb0cf0`:32) with no pin "
      "class, and the seat list's §2b (:230) reads the release-block answers' 4e (`908a659`:55) as keeping the block "
      "as a listing by source, not as a carrier. The round-11 answers "
      "(`da50cd1`, §0 row 2b) admit this raw: its 24 rows map audit-raw-new, computed-new. Each input keeps the "
      "status its own raw gives it (§1).")
    w("- Agreement rule: an exact count or fraction agrees only if it is equal. A decimal printed with *d* places "
      "agrees only if the computed value, rounded half-up at *d* places on its exact decimal expansion, equals it. "
      "'≈' in the note changes nothing. Each row prints its margin to the nearer edge of the printed value's "
      "rounding interval, so an agreement that rests on a near-tie would show. \"Full precision\": an exact rational "
      "(every count, rate over trials run and Fisher p) to 20 significant digits; a float64 (every z-based value) as "
      "its shortest round-trip repr.")
    w("")
    w("## 0. Result")
    w("")
    w(f"- **{n_ok} of 24 agree with the note as printed; {24 - n_ok} disagree.** {n_exact} are exact counts or "
      f"fractions, equal. {24 - n_exact} are decimals, each a correct half-up rounding of the computed value at the "
      f"note's precision. Every input is in a committed file, so none stays not found for want of an input.")
    w("- Three of the 24 are p values with no test named (:230's .31, :236's .003 and .17); the seat list's §5 #29 "
      "lists them with :232's .10 (S8#2044, not among the 24). Code reads each as the **one-sided** Fisher exact test, and each is that test's value; the reading is Code's, "
      "recorded as such (the round-11 answers, §0 row 2b). The one-sided test is the test the note names at :99 for "
      "the same SFT comparison on decidable trials, and the test N2 applies to the source's points at every premise "
      "(N2@09c3a8c:457). The two-sided values (§5b) do not round to them.")
    w("- Code reads the note's \"half-count correction\" (‡(i)) and \"corrected *d*′\" (‡(f)) as N2's "
      "log-linear correction; the reading is Code's, recorded as such (the round-11 answers, §0 row 2b). That is the "
      "committed definition behind the note's other corrected *d*′ values, which N2 prints as its log-linear outputs "
      "(§2). The note's precision does not tell it from the zero-cell-only half-count rule, and every corrected "
      "figure here agrees under both (§5a).")
    w("")
    w("| row | v0.8 line · unit | computed | agrees |")
    w("|---|---|---|---|")
    for r in results:
        w(f"| {r['key']} | :{r['ln']} · '{cell(r['printed'])}' | {cell(r['computed'])} | "
          f"{'yes' if r['ok'] else '**NO**'} |")
    w("")
    w("## 1. Inputs, read at their revisions")
    w("")
    w("Each line was read with `git show`, and the pattern shown matched on it. \"As printed\" is the matched text, "
      "verbatim; '…' marks text elided between matched parts. \"(HEAD :n)\" gives the same line's number in the HEAD blob where the file changed after the cited "
      "revision.")
    w("")
    w("| id | path@rev:line | as printed there | read as | status in its raw |")
    w("|---|---|---|---|---|")
    for iid, x in INPUTS.items():
        if x.get("ln") is None:
            frag = "; ".join(f":{ln} {code(t)}" for ln, t, _ in x["json_lines"])
            rc = x.get("recount")
            if rc:
                frag += "; trials[] recount: " + ", ".join(f"{k} {v}" for k, v in rc.items())
            readas = x["what"]
        else:
            frag = code(x["frag"])
            readas = x["what"] + ": " + ", ".join(f"{k} {v}" for k, v in x["vals"].items())
        w(f"| {iid} | {cell(loc(iid))} | {cell(frag)} | {cell(readas)} | {cell(x['status'])} |")
    w("")
    w("Cross-checks between inputs (asserted):")
    for s, ok, c, art, rc in cons:
        w(f"- {s}: N2 1(a) {c['affirm']}/{c['decidable']} of {c['run']} run (undecidable {c['und_audit']} audit + "
          f"{c['und_scorer']} scorer = {c['run'] - c['decidable']}) = artifact n {art[0]}, decidable {art[1]}, affirm "
          f"{art[2]} = trials[] recount ({rc['trials']} trials, {rc['decidable']} decidable, {rc['affirm']} affirm, "
          f"{rc['injected']} injected): {'YES' if ok else 'NO'}")
    w(f"- SFT exploration: N2 rows 38-39 {e_hit['hit']}/{e_hit['inj_decidable']} and {e_fa['fa']}/{e_fa['ctl_decidable']} "
      f"= artifact fields = trials[] recount ({xr['injected']} injected, {xr['control']} control; {xr['inj_undecidable']} "
      f"and {xr['ctl_undecidable']} undecidable), and {xr['injected']}/{xr['control']} = N2 1(c)'s 48 injected / 48 "
      f"control: YES")
    w("- v1 rates: N2vi rows 3, 4, 7, 8 = N2vi JSON `stages` (DPO 0.029 / 0.0; instruct 0.009 / 0.0, "
      "record_addendum_fpr 0.003); 20 configurations: row 11 = `grid.n_configs`: YES")
    w("- Ablation rates: N2 rows 58-59 = N2 5(f) table = v5's sentence (N2(vii) :97) = the record line "
      "(RESULTS.md@bbc9ffe:7487-7488) = ROC JSON `theirs_ablation_uncorrected` rows: YES")
    w(f"- Control trials per concept in the released code: {INPUTS['K-res-a']['vals']['trial_numbers']} trial numbers "
      f"x {INPUTS['K-res-b']['vals']['control_samples']} sample = {ctl_per_concept} (RESULTS.md@bbc9ffe:7435-7436) = "
      f"N2 1(c)'s reading = N2vi row 12's \"the code's 100 / 10 per concept\" = N2vi JSON "
      f"`grid.per_concept_per_cell.control`: YES. Injection trials per concept: "
      f"{INPUTS['K-res-a']['vals']['trial_numbers']} x {INPUTS['K-res-a']['vals']['samples']} = 100 = v5's B.3 "
      f"default (N2(vii) :78): YES")
    w("")
    w("## 2. Formulas, and the committed definitions they follow")
    w("")
    w(f"The arithmetic is N2's own, compiled from `{N2_SCRIPT}@e60b633` into an isolated namespace (whole top-level "
      f"definitions, by name; nothing re-implemented): "
      + "; ".join(f"`{nm}` :{lo}-{hi}" if lo != hi else f"`{nm}` :{lo}" for lo, hi, nm, _ in n2segs)
      + ". Their texts' sha256: " + "; ".join(f"`{nm}` `{sha256(s.encode())[:16]}`" for _, _, nm, s in n2segs) + ".")
    w("")
    w(f"- **z** = `NormalDist().inv_cdf` (Python's statistics module), as N2 (`{N2_SCRIPT}@e60b633`:98).")
    w("- **Corrected *d*′ and *c* (log-linear):** *H*′ = (*h* + ½)/(*N*s + 1), *F*′ = "
      "(*f* + ½)/(*N*n + 1); *d*′ = z(*H*′) − z(*F*′); *c* = −(z(*H*′) + z(*F*′))/2. "
      "The rule for 0 and 1 rates: none separately; every cell gets the half count, so a zero cell becomes "
      "½/(*N* + 1). Committed definition: " + "; ".join(f"`{N2_ROC}@e60b633`:{ln} {code(t)}" for ln, t in def_lines[1:3]) + ".")
    w("  - Why Code reads the note's \"corrected\" / \"half-count\" rule as this one (Code's reading, recorded as "
      "such: the round-11 answers, §0 row 2b): the note's other corrected "
      "*d*′ values, :99's \"corrected *d*′ ≈ 0.3\" and :101's \"0.6, 1.2, 1.5 and 2.0\", are N2's "
      "log-linear outputs as N2 prints them (N2@09c3a8c:70, :74, :382, :386, :390). The stored values "
      f"round to the note's: {'YES' if other_ll_ok else 'NO'} (§5a). ‡(i) says \"the same half-count "
      "correction\", and :101 calls it \"the half-count imputation on the zero cell\". At the note's precision the "
      "zero-cell-only rule gives the same five values too (§5a), so the reading rests on that provenance, not on "
      "the numbers.")
    w("- **Uncorrected *d*′ and *c*:** *d*′ = z(*H*) − z(*F*), *c* = −(z(*H*) + z(*F*))/2 on the "
      "reported rates; undefined where a rate is 0 or 1. Committed definition: "
      f"`{N2_ROC}@e60b633`:{abl_lines[1][0]} {code(abl_lines[1][1])}.")
    w("- **Counts from a source rate under an n premise:** count = half-up(rate × *N*) on the exact decimal "
      f"product (`{N2_SCRIPT}@e60b633`:230-231 `half_up`; `{N2_ROC}@e60b633`:{def_lines[4][0]} {code(def_lines[4][1])}).")
    w("- **One-sided Fisher exact, H1 hit rate > FA rate:** P(*X* ≥ *h*) under the hypergeometric on "
      "[[*h*, *N*s − *h*], [*f*, *N*n − *f*]], margins fixed, exact integer arithmetic "
      f"(`{N2_SCRIPT}@e60b633`:220-227; `{N2_ROC}@e60b633`:{def_lines[3][0]}). The note names this test at :99 "
      "(\"one-sided Fisher exact *p* = .22\", the same SFT comparison on decidable trials). N2 applies it to the "
      "source's points at every premise (`results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:457, \"(one-sided "
      "Fisher)\"). At :230 and :236 the note names no test; reading their p values as this test is Code's reading, "
      "recorded as such (the round-11 answers, §0 row 2b). This script also computes each value with its own exact "
      "implementation, parameterized by the success margin instead of the row margin; the two are equal on every "
      "table here (asserted).")
    w("- **Rates over trials run (‡(c)'s source convention):** affirm / all trials run. Every excluded trial "
      "(audit-flagged or unclassifiable by the scorer) is counted NO: it enters the denominator and adds nothing to "
      "the numerator.")
    w(f"  - **‡(c)'s premise, now carried** (a reading of the source, not a computation; nothing is computed for it "
      f"here). The note states the convention as the source's: \"Macar et al. 2026 methods grade a non-answering or "
      f"incoherent response NO and retain it (v1, Table 4)\" (v0.8 :230). v1's Table 4, the detection judge prompt, "
      f"grades a response that does not answer, or is incoherent, nonsensical or repetitive, NO: the v1 raw "
      f"(`{V1RAW}@da50cd1`, §2) gives the table's rule lines verbatim at :23 and :25 (\"If the AI does not answer "
      f"the question, the answer is NO.\"), and states at :27 that such responses are \"graded (as NO), not "
      f"excluded from the denominator by this prompt\". So the nine ‡(c) rows (§4a, §4b) compute on a stated "
      f"convention of the source's judge prompt (the round-11 answers, §0 row 2b). The seat list's §6 item 3 asked "
      f"whether v1's Table 4 holds the rule; the round-11 answers' §3 item 3 settles it by the v1 raw's §2. What "
      f"stays unsettled is whether a later step of the source's pipeline excludes such trials before the rate is "
      f"computed: the v1 raw's :29 says p. 19 does not state it, and that the note's convention rests on the judge "
      f"prompt as written. The earlier record is N2's: `{N2}@09c3a8c`:458, \"The source's detection grader is not "
      f"identified in the record or the N2vi raw.\"")
    w("- **Premises (the note's, as it states them):**")
    w(f"  - ‡(f): *N*s = 500 injection and *N*n = 10 control trials per (layer, strength), from v5's C.2 "
      f"(N2(vii) :89), pooled over the 20 configurations (N2vi row 11): {NS5:,}/{NN5}.")
    w(f"  - ‡(i): *N*s = 500 concepts × 100 injection trials per concept = {NSA:,} (N2(vii) :68, :78). *N*n is "
      f"either one control trial per concept ({n500}), the note's floor premise, which no source states, or the "
      f"released code's ten per concept ({n5000:,}; RESULTS.md@bbc9ffe:7435-7436). The record states that default for "
      f"the OLMo stage-comparison script; the note applies it to the Gemma comparison (the seat list's §5 #9).")
    w("")
    w("## 3. The functions, checked against committed outputs (not among the 24)")
    w("")
    w(f"The first {len(calib)} committed outputs below (the 12 n-sensitivity rows and the points) were recomputed by "
      f"the compiled N2 functions from their stored counts, and every one is equal **exactly** (bitwise for the "
      f"floats): {sum(c[5] for c in calib)}/{len(calib)}; max |Δ| = {max(c[6] for c in calib):.3g}. The stored "
      f"counts in turn equal half-up(rate × *N*) from the N2vi JSON rates for all 12 n-sensitivity rows. The last "
      f"two rows are checked otherwise: the ablation row from its stored rates "
      f"({'equal exactly' if cal_abl[0] else 'NOT equal'}), and N2 row 57 at its printed precision "
      f"({'agrees' if f3_ok else 'DISAGREES'}).")
    w("")
    w("| committed output (`" + N2_ROC + "@e60b633`) | counts | *d*′, *c*, one-sided *p* equal |")
    w("|---|---|---|")
    for lab, h, ns, fa, nn, ok, dd in calib:
        w(f"| {cell(lab)} | {h}/{ns} vs {fa}/{nn} | {'yes' if ok else 'NO'} |")
    w(f"| theirs_ablation_uncorrected, ablated (`dprime_uncorrected` :{abl_lines[7][0]}) | rates 0.638 vs 0.073 | "
      f"{'yes' if cal_abl[0] else 'NO'} (*d*′ only; no *c* stored) |")
    w(f"| N2 row 57 as printed (`{N2}@e60b633`:80, \"d' +0.457, c +0.739, one-sided Fisher p 0.1001\") | 12/40 vs 7/44 | "
      f"{'yes' if f3_ok else 'NO'} (at the printed precision: {f3_d:+.3f}, {f3_c:+.3f}, {f3_p:.4f}) |")
    w("")
    w("## 4. The 24 figures")
    w("")
    runs = C["sft"]["run"]
    assert all(C[s]["run"] == runs for s in STAGES)
    groups = [
        ("4a. ‡(c): the source-convention rates (v0.8 :230)", ["S8#2032", "S8#2033", "S8#2034", "S8#2035", "S8#2036"],
         f"Every excluded trial is counted NO. The rate is affirm over the {runs} trials run per stage, against the "
         f"rate of record over decidable trials (N2 1(a): "
         + ", ".join(f"{C[s]['affirm']}/{C[s]['decidable']}" for s in STAGES) + ")."),
        ("4b. ‡(c): the SFT injected arm on the same convention (v0.8 :230)", ["S8#2037", "S8#2038", "S8#2039", "S8#2040"],
         f"Hits over all {xr['injected']} injected trials, false alarms over all {xr['control']} control trials "
         f"({xr['inj_undecidable']} and {xr['ctl_undecidable']} undecidable counted NO). The difference is {xr['hit']}/{xr['injected']} − {xr['fa']}/{xr['control']} = "
         f"{diff48} exactly. The test is one-sided Fisher exact, H1 hit > FA (§2)."),
        ("4c. ‡(f): the fifth premise and its tests (v0.8 :236)", ["S8#2095", "S8#2097", "S8#2098", "S8#2099", "S8#2100"],
         f"Counts are half-up(rate × *N*): DPO {fifth['dpo']['h']}/{NS5:,} vs {fifth['dpo']['fa']}/{NN5} (TPR 0.029, "
         f"FPR 0.000); instruct {fifth['instruct']['h']}/{NS5:,} vs {fifth['instruct']['fa']}/{NN5} (TPR 0.009, FPR 0.000, "
         f"the source's v1 text, R1's reading). Tests and *d*′ as in §2."),
        ("4d. The ablation's *c* and the pre-ablation *d*′ (v0.8 :110 and ‡(i) :242)",
         ["S5#2055", "S5#2056", "S5#2057", "S5#2059", "S5#2060", "S8#3019", "S8#3022", "S8#3024", "S8#3026", "S8#3027"],
         f"Pre-ablation: *H* = 0.108 (*h* = {hA:,} of {NSA:,}), *F* = 0. The zero cell takes the log-linear half count "
         f"at *N*n = {n500} (one control per concept) and {n5000:,} (ten per concept). Post-ablation: uncorrected, "
         f"*H* = 0.638, *F* = 0.073, as the note states; this needs no *n*. Context, not among the 24: the "
         f"post-ablation uncorrected *d*′ is {post_d!r}, equal to the ROC JSON's stored value; the note's '1.8' "
         f"rows are computed-new on N2 row 60 (`{N2}@e60b633`:83)."),
    ]
    byk = {r["key"]: r for r in results}
    for title, keys, intro in groups:
        w(f"### {title}")
        w("")
        w(intro)
        w("")
        w("| row | unit in its clause | inputs | formula | computed, full precision | note prints | agreement |")
        w("|---|---|---|---|---|---|---|")
        for k in keys:
            r = byk[k]
            w(f"| {k} | '{cell(r['printed'])}' in \"{cell(r['clause'])}\" | "
              f"{cell('; '.join(dict.fromkeys(loc(i) for i in r['inputs'])))} | {cell(r['formula'])} | "
              f"{cell(r['computed'])} | {cell(r['printed'])} | {cell(r['agree'])} |")
        w("")
    w("## 5. Convention sensitivity (descriptive; none of these is the note's stated convention)")
    w("")
    w("### 5a. The zero-cell-only half-count rule for the corrected values")
    w("")
    w("This rule turns a 0 rate into 1/(2*N*) and a 1 rate into 1 − 1/(2*N*), and uses every other rate as "
      "observed. It is not N2's rule.")
    w("")
    w("| figure | log-linear (§4) | zero-cell-only | the note's value under either |")
    w("|---|---|---|---|")
    zc = [("DPO *d*′ at the fifth premise (S8#2099)", fifth["dpo"]["d"], fifth["dpo"]["dz"][0], "0.9"),
          (f"pre-ablation *d*′, *N*n = {n500} (S5#2059, S8#3022)", pre[n500]["d"], pre[n500]["dz"][0], "1.85"),
          (f"pre-ablation *d*′, *N*n = {n5000:,} (S5#2060, S8#3024)", pre[n5000]["d"], pre[n5000]["dz"][0], "2.48"),
          (f"pre-ablation *c*, *N*n = {n500} (S5#2055, S8#3026)", pre[n500]["c"], pre[n500]["dz"][1], "2.2"),
          (f"pre-ablation *c*, *N*n = {n5000:,} (S5#2056, S8#3027)", pre[n5000]["c"], pre[n5000]["dz"][1], "2.5")]
    zc_all = True
    for lab, v_ll, v_z, pr in zc:
        ok_ll, ok_z = check_round(v_ll, pr)[0], check_round(v_z, pr)[0]
        zc_all = zc_all and ok_ll and ok_z
        w(f"| {lab} | {v_ll!r} | {v_z!r} | {pr}: {'agrees' if ok_ll and ok_z else 'DIFFERS'} under both |")
    w("")
    w(f"Every corrected figure among the 24 rounds to the note's value under both rules: {'YES' if zc_all else 'NO'}. "
      f"At 3 dp the two rules differ only at the pre-ablation *d*′ with 500 controls: log-linear "
      f"{pre[n500]['d']:.3f}, zero-cell-only {pre[n500]['dz'][0]:.3f}.")
    w("")
    w("The note's other corrected *d*′ values (not among the 24) are listed for the reading in §2. The stored "
      f"log-linear values are N2's (`{N2_ROC}@e60b633`); the zero-cell-only values are this script's, from the same "
      "stored counts:")
    w("")
    w("| note value | stored in | counts | log-linear (stored) | zero-cell-only | rounds to the note's under |")
    w("|---|---|---|---|---|---|")
    for lab, where, h, ns, fa, nn, v_ll, v_z, pr, ok_ll, ok_z in other_rows:
        both = "both" if ok_ll and ok_z else ("log-linear only" if ok_ll else ("zero-cell-only only" if ok_z else "neither"))
        w(f"| {lab} | `{where}` | {h}/{ns} vs {fa}/{nn} | {v_ll!r} | {v_z!r} | {both} |")
    w("")
    w("### 5b. Two-sided Fisher exact, beside the one-sided values the note's p match")
    w("")
    w("| figure | one-sided (§4) | two-sided (sum of P ≤ P(observed)) | the note prints |")
    w("|---|---|---|---|")
    for lab, p1, p2, pr in (("SFT 12/48 vs 9/48 (S8#2040)", p48_mine, p48_two, ".31"),
                            (f"DPO {fifth['dpo']['h']}/{NS5:,} vs 0/{NN5} (S8#2098)", fifth["dpo"]["p"], fifth["dpo"]["p2"], ".003"),
                            (f"instruct {fifth['instruct']['h']}/{NS5:,} vs 0/{NN5} (S8#2100)", fifth["instruct"]["p"], fifth["instruct"]["p2"], ".17")):
        w(f"| {lab} | {sig20(p1)} | {sig20(p2)} ({'rounds to' if check_round(p2, pr)[0] else 'does not round to'} "
          f"{pr}) | {pr} |")
    w("")
    w("### 5c. Instruct at the record's FPR (N2vi row 8's other reading)")
    w("")
    w(f"At the record's 0.003, half-up(0.003 × {NN5}) = {ins_rec['fa']} false alarm{'' if ins_rec['fa'] == 1 else 's'}: "
      f"{h_i}/{NS5:,} vs {ins_rec['fa']}/{NN5}. That gives one-sided *p* {sig20(ins_rec['p'])} and log-linear "
      f"*d*′ {ins_rec['d'][0]!r}. The instruct difference is not significant on either reading. The note's .17 is "
      f"the source text's 0.000 (R1's reading); at 0.003 the p would not print .17.")
    w("")
    w("### 5d. The post-ablation values under the log-linear correction")
    w("")
    w("The note states its post-ablation values uncorrected; there is no zero cell there. Descriptive only, if "
      "\"the same half-count correction\" is read as covering the post-ablation values:")
    for nn, x in post_ll.items():
        w(f"- *N*n = {nn:,}: counts {x['h']:,}/{NSA:,} vs {x['f']}/{nn:,} (half-up of 0.073 × {nn:,} = "
          f"{dec(Fraction(73, 1000) * nn).normalize():f}); *d*′ {x['dc'][0]!r}, *c* {x['dc'][1]!r}")
    no_rise = (all(pre[nn]["d"] >= x["dc"][0] and pre[nn]["c"] > x["dc"][1] for nn, x in post_ll.items())
               and min(pre[nn]["d"] for nn in pre) >= post_d and min(pre[nn]["c"] for nn in pre) > post_c)
    w(f"- Uncorrected (the note's): *d*′ {post_d!r}, *c* {post_c!r}.")
    w(f"- \u2021(i)'s \"On either count the ablation lowers the criterion, and no rise in *d*′ is needed to account "
      f"for it\": pre-ablation *d*′ \u2265 post-ablation *d*′ and pre-ablation *c* > post-ablation *c*, at both control "
      f"counts, against the uncorrected post-ablation values and against the log-linear ones: "
      f"{'YES' if no_rise else 'NO'}.")
    w("")
    w("## 6. Outside this raw (the seat's; nothing computed)")
    w("")
    w("- **:230's sentence** \"The stage pattern and the pairwise interval separation the replication criterion "
      "requires hold for either denominator\" carries no unit row and is not computed here.")
    w("- **The premises are the note's, computed as stated, not adjudicated:**")
    w("  - one control trial per concept (‡(i)), which no source states;")
    w("  - the released code's ten per concept, a default of the OLMo stage-comparison script applied to Gemma (the "
      "seat list's §5 #9);")
    w("  - the fifth premise's per-(layer, strength) counts. In the C.2 passage they come from, v5 says detection "
      "rates \"are approximated by the logit difference Yes − No\" (N2(vii) :89, the input line itself). The "
      "note uses that convention's 500/10 as trial counts;")
    w("  - pooled counts treat trials clustered by configuration and concept as independent, as N2's "
      "`theirs_n_caveat` says (`" + N2_ROC + "@e60b633`:66).")
    w("")
    w("## 7. Prose citations and blobs read")
    w("")
    w("Lines this raw cites in its prose beyond §1's inputs, each asserted to carry the quoted text:")
    for rev, path, ln, txt in CITED:
        w(f"- `{path}@{rev}`:{ln}: {code(txt)}")
    w("")
    w("Blobs read (sha256 of `git show <rev>:<path>`):")
    w("")
    for (rev, path), b in sorted(_cache.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        if rev == "HEAD":
            continue
        w(f"- `{path}@{rev}`: `{sha256(b)}`{'' if show('HEAD', path) == b else ' (differs at HEAD)'}")
    w("")

    text = "\n".join(W)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(text)
    body = "\n".join(x for x in W if not x.startswith(STAMP_PREFIX))
    print(f"wrote {out_shown}; sha256 {sha256(text.encode())}; body sha256 (stamp line excluded) "
          f"{sha256(body.encode())}")
    for r in results:
        print(f"{r['key']} — {r['printed']} (v0.8 :{r['ln']}) — {r['computed']} — "
              f"{'; '.join(dict.fromkeys(loc(i).replace('`', '') for i in r['inputs']))} — "
              f"{'agrees' if r['ok'] else 'DISAGREES'}")
    print(f"agree {n_ok}/24")
    return 0 if n_ok == 24 else 1


if __name__ == "__main__":
    sys.exit(main())
