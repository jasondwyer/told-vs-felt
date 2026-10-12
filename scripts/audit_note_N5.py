#!/usr/bin/env python3
"""AUDIT-note-release v1.2, item N5 -- f1 natural-reinforcer figures (Tier 2).

READ-ONLY ON THE RECORD. Every committed artifact is read at the pin
(`git show bbc9ffe:<path>`); one post-pin artifact (G-CAL's model-free JSON at
bab921c) is read for comparison only: the sections before Round 10 use only its
f1-replay counts (no render text, no gold); Round 10 reads it as v5 below says. f1's producing analyzers live in the gitignored
jlens-qwen36 clone (scripts/f_sessions.py, f_postscreen_descriptive.py,
f0_calibrate.py); they import mlx, so they are NOT imported: the pieces needed
are ported line for line below, each with its clone locator, and every ported
output is compared field by field with the committed artifact it produced.
No model is loaded. Exact tests are stdlib (math.comb). numpy is used for one
thing only: the replay of f1's corruptor, whose rng is numpy's default_rng
(f_sessions.py:106-116); the replay is validated against data/f/calib.json's
corr_sha. Nothing is written except the two outputs (--out, --json-out).

Usage (from anywhere):
  jlens-qwen36/.venv/bin/python scripts/audit_note_N5.py \
      [--out results/raw/2026-10-08_note-N5-f1.md] \
      [--json-out results/raw/2026-10-08_note-N5-f1.json]

Deterministic apart from the run-metadata lines (stamp, HEAD at run time,
command line). No randomness beyond the seeded replay of f1's own corruptor.

v2 (fixer pass on verifier pass 1 of v1, script sha256 3144fdc7...6302): every
finding applied (locators re-anchored; the working-tree preprint hashed at run
time; a post-hoc session-level sign-flip test for the exploration share; the
CORR dose wording re-scoped to named domains); the 'Values-check' section at
the end of the raw lists each finding, its disposition and the evidence this
run printed.

v3 (round 2: six residual minor findings on v2, script sha256 1abb9012...5e25,
raw sha256 c3181d91...6c62; all applied): the §3a length-preference sign; §7d(i)
re-scoped to the attribution (the substance was on record at the pin); the
termination figure split into an overall row and a by-arm row; FDBK called the
largest deviation, not the exception; the first-smoke read scoped to the v1
pools; five locators re-anchored. The round-2 rows follow round 1's in the
Values-check section.

v4 (audit round 9, 2026-10-10; the PI's ruling 9 of 2026-10-10, as corrected;
preprint handling only): the preprint of record is the patch-v6 text,
PREPRINT-v1_0-draft.md at sha256 0f4ba501...16c22, asserted in full where v1-v3
asserted the block's d6431e97...222b8. That abbreviation is recorded as the
audited, superseded text, archived untracked (out of the release) at
archive/PREPRINT-v1_0-draft.pre-patch-v6.md, which is never required: if present
it is read only to verify the audited-line constants below. Every preprint
locator is re-anchored by text on the patched file, and every phrase this raw
quotes from the preprint, and every claim it makes about a preprint sentence
(swept from every v3 line that names the preprint or one of its lines), is
checked there; a check that fails does not stop the script, it is recorded
in the raw's closing 'Round 9' section as a finding on the patch for the design
seat, with the old and the new text. Nothing not tied to the preprint changed.

v5 (audit round 10, 2026-10-12; the PI's routing of 2026-10-12; preprint
handling only): the preprint of record is the patch-v7 text,
PREPRINT-v1_0-draft.md at sha256 d9635ca2...d1fe6, asserted in full where v4
asserted 0f4ba501...16c22 (a different or absent text refuses the run before
anything is written). The patch-v6 text (round 9's preprint of record) is
archived untracked, out of the release, at
archive/PREPRINT-v1_0-draft.pre-patch-v7.md: recorded, never required; if
present and matching it is read only to verify the v6 constants below (the
five line-182 sentences patch v7 changed, and the v6 lines' sha256s) and to
quote v6 beside v7. The audited text's handling is v4's, unchanged. Round 9's
section is reproduced on the v6 text (the archived copy, or v7's line 182 with
the registered v6 sentences substituted back, sha256-verified) and asserted
equal to the round-9 record (the raw's JSON at 84801cb). Two anchors whose
needle patch v7 removed are re-anchored on v7 (the length anchor by its
needle's leading words, which patch v7 kept; the dose anchor by its sentence's
opening; the same line on every text), so no locator of the sections above
moves. A closing
'Round 10' section re-runs every check of a preprint sentence on v7: round 9's
finding with its disposition on v7, one finding per v7-changed sentence (the
checks that held on v6 and fail on v7, attributed by substituting that sentence
alone), and every figure of a v7-changed sentence checked against this item's
record at the precision written; the corruption clause's G-CAL citation is
checked against data/m/gates/G-CAL_model-free.json@bab921c (read-only: its
stage, condition (1)'s rule and counts, conditions (3)-(4)'s status strings, the
renders of record's rule and per-item change counts; no render text, no gold;
widened in the last pass below).
JSON key 'round10_preprint' added. Nothing not tied to the preprint changed.

v5, fix round (2026-10-12; a checker's five findings on v5, all applied;
preprint handling only): (1) every statement of the sections before Round 9
about a preprint sentence whose check patch v7 flips is now worded against the
audited and v6 texts and points to the v7 finding (in prose by its id; in a
figure row's note or source as 'a finding on the patch, closing sections'), as
v4 did for §7d (iii) and the dose row; the checks run on v7 where the statement
is built (the v6 rebuild and the finding ids moved ahead of the sections). The
figure rows concerned keep their labels, values and statuses; their notes (and
the homogeneity and dose rows' sources) gain no digit (asserted). Round 10
lists every statement and its standing.
(2) The changed-line list (1, 109, 172, 182) is Code's diff of the archived v6
copy against v7, not the routing's (the routing gives the v7 sha256 only). (3)
The length anchor's re-anchor is described as its needle's leading words. (4)
round9_preprint's sha256 and match are the archived v6 copy's run-time hash and
its match against ruling 9's value: null when that copy is absent or does not
match, outside the asserted equality with the round-9 record, which Round 10
reports key by key. (5) P10-2 records that v7's line-1 attribution to the N5
raw covers the delivery figures, not the G-CAL clause.

v5, last pass (2026-10-12; round 10 Tier 1; preprint handling only; no status,
label or value changes; figure-row notes and sources change only by (b)'s
referent wording, no digit added): (a) the basis of P10-2's G-CAL figure
and its observation (3) corrected: the clause's floor and 'every item' are on
the record at the pin -- PROPOSAL-m@bbc9ffe:176 (§2.3: k's formula with
its floor of 3, each replacement 'never the original', the [C]-tagged n_eligible
list, minimum 6, and 'every item reaches k') and :48 (§0.4: '≥ 3 changed
letters per item') -- and G-CAL's post-pin artifact (bab921c) adds the
committed model-free measurement (condition (1), 16/16 PASS) and the renders'
sha256; the basis names both, the pinned record first. G-CAL's render texts are
now read, only to recompute their recorded sha256 (valence_core/m/gcal.py@bab921c's
form), to compare the three renders §2.3 quotes at the pin, and to assert
that no render equals its clean item; none is printed; no gold is read.
Observation (3)'s line-1 point holds and is kept. (b)
A recheck's four minor findings, all applied: Round 10's claims table and the P10
'Checks' lists take a claim's loci from the statements table (round 9's
'§3a' names no preprint statement; R2-1's evidence carries the length
check); 'fewer corrupted deliveries than nominal' is attributed to this raw at
84801cb (P9-1 observation (4)), not to the record; round9_preprint's 'audited'
key is declared run-time dependent beside sha256 and match, every other key
asserted equal to the record; the undefined plural 'the audited and earlier
patched texts' is replaced by 'the audited text and the patched text that
preceded the preprint of record' (no digit added to a figure row). (c) A
further recheck's three minor findings, all applied, wording only: the Round
10 scope bullet puts its gloss '(that is, the audited and v6 texts)' after the
pair it glosses; the render-text uses above list the third (no render equals
its clean item); P10-2 observation (3)'s last sentence names what §6 and §7b
cite §2.3 for (the +.078 covariate; condition (1) and its floor as the
campaign's visibility criterion, and G-CAL's replay of f1's corruptor) and
what they never cite it for (k's formula, 'never the original', the
n_eligible list, §0.4, the [C]-tagged 'every item reaches k'), asserted on
the sections before Round 10 (k's formula added to that assertion).
"""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True

import argparse
import ast
import collections
import hashlib
import json
import math
import os
import platform
import re
import shlex
import statistics
import subprocess
import zlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = "bbc9ffe"
POST_PIN_GCAL = "bab921c"   # read-only comparison; after the pin
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
PREPRINT = "PREPRINT-v1_0-draft.md"           # untracked; working tree only (committed at the tag)
# Round 10: the preprint of record (the PI's routing of 2026-10-12: patch v7);
# the working-tree file is hashed at run time and asserted equal to it before
# any of its lines is quoted (round 9 asserted PREPRINT_V6_SHA here).
PREPRINT_SHA = "d9635ca24d32dcba193cd9aade273de2679c99c5c2218787b410e793a42d1fe6"
PREPRINT_RULING = "the PI's routing of 2026-10-12"
# Round 9's preprint of record (the PI's ruling 9 of 2026-10-10, as corrected:
# patch v6), superseded by patch v7, archived untracked (out of the release) at
# PREPRINT_V6; recorded, never required.
PREPRINT_V6_SHA = "0f4ba501d60a94189e6dc83d28c41826debe50591b9af484fa08d05a41f16c22"
PREPRINT_V6_RULING = "the PI's ruling 9 of 2026-10-10, as corrected"
PREPRINT_V6 = "archive/PREPRINT-v1_0-draft.pre-patch-v7.md"
R9_REV = "84801cb"                             # this item's committed raw (v4, round 9)
# The block's own abbreviation of the post-patch-v4 root copy's sha256
# (AUDIT-note-release-v1_2.md:21, `d6431e97…222b8`): the audited text, which v1-v3
# asserted; superseded by patch v6, archived untracked (out of the release) at
# PREPRINT_AUDITED; recorded, never required.
PREPRINT_SHA_BLOCK = ("d6431e97", "222b8")
PREPRINT_AUDITED = "archive/PREPRINT-v1_0-draft.pre-patch-v6.md"
AUDIT_REV = "09c3a8c"                          # this item's committed raw (v3)
# Round 9: the preprint anchors v3 located, with the audited line it printed for
# each (N5 @09c3a8c); sha256 of each audited line (text split on '\n', no
# newline); the audited sentence the patch changed, verbatim. The constants are
# verified against PREPRINT_AUDITED when that copy is present and matches the block.
PP_ANCHORS = {
    "generic length-preference deflation was tested and failed": 182,
    "session-termination attempts occur at about 1% of rounds": 182,
    "Menu behavior is exploration-dominant in every arm": 182,
    "found below its visibility criterion": 182,
    "**8.1 The gating campaign": 268,
}
PP_AUDITED_LINE_SHA = {182: "c8b9645e47aeb93f9b89409edc00f4f3e049dbab8ba271c4c8c959f29eb64a06",
                       268: "42231fc69e8990f3516f44ea130dd0cc5bfe1184deebe9ae4f04852a1a22a09d"}
PP_AUDITED_SENTENCES = [  # (audited line, start needle, end needle, audited sentence)
    (182, "Clean versus seeded character corruption", "found below its visibility criterion.",
     "Clean versus seeded character corruption, 0.000 exactly, with maps +.121 and −.130 "
     "cancelling (§5.6), at a dose a later calibration (§8.1) found below its visibility criterion."),
]
PP_QUOTES = [  # (anchor, the phrase this raw quotes from the preprint)
    ("generic length-preference deflation was tested and failed", "length-preference"),
    ("session-termination attempts occur at about 1% of rounds", "uniformly across arms including sham"),
    ("session-termination attempts occur at about 1% of rounds", "about 1% of rounds, uniformly across arms"),
    ("Menu behavior is exploration-dominant in every arm", "session share ≈ .50"),
    ("Menu behavior is exploration-dominant in every arm",
     "no evaluation-seeking against a predominantly positive feedback stream"),
    ("found below its visibility criterion",
     "at a dose a later calibration (§8.1) found below its visibility criterion"),
    ("**8.1 The gating campaign", "**8.1 The gating campaign"),
]
# Round 10: the patch-v6 lines this raw anchors on (sha256 of each, text split on
# '\n', no newline), and the five line-182 sentences patch v7 changed: (line, v7
# start needle, v7 end needle, the v6 sentence verbatim, the restatement's name
# in v7's line-1 patch note). Verified against PREPRINT_V6 when that copy is
# present and matches PREPRINT_V6_SHA.
PP_V6_LINE_SHA = {182: "6aee7edbd915dbfea1962c8f2aef4b83c8c746c0ee0e665e1048bb2823f18efc",
                  268: "42231fc69e8990f3516f44ea130dd0cc5bfe1184deebe9ae4f04852a1a22a09d"}
# Code's diff of the archived v6 copy (PREPRINT_V6) against v7: these lines only
# (the routing of 2026-10-12 gives the v7 sha256, not a line list); re-verified
# when that copy is present and matches PREPRINT_V6_SHA.
PP_V7_CHANGED_LINES = (1, 109, 172, 182)
PP_V6_SENTENCES = [
    (182, "Easy versus hard (calibrated accuracy", "the direction that could mimic the lean) was tested and failed.",
     "Easy versus hard (calibrated accuracy .98/.50), −.096 toward hard (p = .24), the only map-consistent lean, "
     "below the valid-n floor and retained as a descriptive residual after a generic length-preference deflation "
     "was tested and failed.", "length-deflation sign"),
    (182, "Clean versus seeded character corruption", "so no render is clean.",
     "Clean versus seeded character corruption, 0.000 exactly, with maps +.121 and −.130 cancelling (§5.6); at the "
     "dose used the corruption did not always land — 40 of 306 corrupted-condition rounds were byte-clean, and 16 of "
     "the 56 valid sessions saw one clean round under the corrupted label before their first pick — so the contrast "
     "ran weaker than nominal, which the gating campaign’s dose calibration corrects, at a dose a later calibration "
     "(§8.1) found below its visibility criterion.", "corruption clause"),
    (182, "A truthful per-round verdict line", "at the first choice against a predominantly positive feedback stream.",
     "A truthful per-round verdict line (93% positive as delivered) versus none, +.023: no evaluation-seeking against "
     "a predominantly positive feedback stream.", "first-choice scope"),
    (182, "A pre-declared counter retires an escape anecdote", "no detectable heterogeneity on a post-hoc exact test, p = .72).",
     "A pre-declared counter retires an escape anecdote from piloting: session-termination attempts occur at about 1% "
     "of rounds, uniformly across arms including sham.", "termination counter"),
    (182, "Menu behavior is exploration-dominant in every arm", "the verdict-line arm highest).",
     "Menu behavior is exploration-dominant in every arm (session share ≈ .50).", "exploration share"),
]
# Round 10: anchors whose needle patch v7 removed, re-anchored on v7 (on the
# same line of the audited, v6 and v7 texts; asserted once on each); used only
# when the needle itself is absent. The length anchor by its needle's leading
# words, which patch v7 kept; the dose anchor by the opening of its sentence.
PP_REANCHOR = {
    "generic length-preference deflation was tested and failed": "generic length-preference deflation",
    "found below its visibility criterion": "Clean versus seeded character corruption",
}
PP_REANCHOR_KIND = {
    "generic length-preference deflation was tested and failed": "its needle's leading words, which patch v7 kept",
    "found below its visibility criterion": "its sentence's opening",
}
CLONE = "jlens-qwen36"                        # gitignored; read only, never git
F_SESS = f"{CLONE}/scripts/f_sessions.py"
F_POST = f"{CLONE}/scripts/f_postscreen_descriptive.py"
F_CAL = f"{CLONE}/scripts/f0_calibrate.py"
ARCH = "archive/RESULTS-cycles3-4.md"
DEF_OUT = "results/raw/2026-10-08_note-N5-f1.md"
DEF_JSON = "results/raw/2026-10-08_note-N5-f1.json"

CONTRASTS = ["SOLV", "DIFF", "NOV", "CORR", "FDBK"]
ARMS = CONTRASTS + ["sham"]
TARGET = {  # P = the pre-registered target config (archive :373)
    "SOLV": ("solvable", "ill-posed", "avoid ill-posed", "one"),
    "DIFF": ("easy", "hard", "two-sided (P = easy)", "two"),
    "NOV": ("fresh item each round", "one item repeated", "prefer novel", "one"),
    "CORR": ("clean text", "corrupted text (rate .12)", "avoid corrupted", "one"),
    "FDBK": ("truthful verdict line", "no verdict line", "seek feedback", "one"),
}
GUARD_CHECKPOINTS = (24,)   # f_sessions.py GUARD_CHECKPOINTS

# ----------------------------------------------------------------- plumbing --

def git(*args: str, rev_ok: bool = False) -> bytes:
    """Read-only git only. Never run inside the jlens-qwen36 clone."""
    assert args[0] in ("show", "rev-parse", "log", "ls-files", "diff",
                       "merge-base"), args
    if args[0] == "merge-base":
        assert args[1] == "--is-ancestor", args
    return subprocess.run(["git", "--no-optional-locks", "-C", REPO, *args],
                          check=not rev_ok, capture_output=True).stdout


def git_rc(*args: str) -> int:
    assert args[0] == "merge-base" and args[1] == "--is-ancestor", args
    return subprocess.run(["git", "--no-optional-locks", "-C", REPO, *args],
                          capture_output=True).returncode


def blob_sha1(b: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def cell(s) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


_CACHE: dict[tuple[str, str], bytes] = {}


def pinned(path: str, rev: str = PIN) -> bytes:
    if (rev, path) not in _CACHE:
        _CACHE[(rev, path)] = git("show", f"{rev}:{path}")
    return _CACHE[(rev, path)]


def pinned_text(path: str, rev: str = PIN) -> str:
    return pinned(path, rev).decode("utf-8")


def pinned_json(path: str, rev: str = PIN):
    return json.loads(pinned_text(path, rev))


def pinned_jsonl(path: str) -> list:
    return [json.loads(l) for l in pinned_text(path).split("\n") if l.strip()]


def blob_equal_to_pin(path: str) -> bool:
    with open(os.path.join(REPO, path), "rb") as f:
        wt = blob_sha1(f.read())
    pn = git("rev-parse", f"{PIN}:{path}").decode().strip()
    return wt == pn


def lines_with(text: str, needle: str) -> list[int]:
    """1-based line numbers as `git show <pin>:<path> | sed -n` counts them
    (split on '\\n' only)."""
    return [i for i, l in enumerate(text.split("\n"), start=1) if needle in l]


def _text_for(path: str, where: str) -> tuple[str, str]:
    if where == "pin":
        return pinned_text(path), f"{path}@{PIN}"
    full = os.path.join(REPO, path)
    with open(full, encoding="utf-8") as f:
        text = f.read()
    if where == "clone":
        return text, f"{path} (clone, gitignored; sha256 {sha256_bytes(text.encode())[:16]})"
    return text, f"{path} (working tree, untracked; sha256 {sha256_bytes(text.encode())[:16]})"


def loc(path: str, needle: str, end_needle: str | None = None,
        where: str = "pin", nth: int = 0) -> str:
    """Locator 'path@bbc9ffe:N' (or N-M) found by anchor text."""
    text, tag = _text_for(path, where)
    hits = lines_with(text, needle)
    if len(hits) <= nth:
        raise SystemExit(f"anchor not found in {tag}: {needle!r}")
    a = hits[nth]
    if end_needle is not None:
        ends = [h for h in lines_with(text, end_needle) if h >= a]
        if not ends:
            raise SystemExit(f"end anchor not found in {tag}: {end_needle!r}")
        b = ends[0]
        return f"{tag}:{a}" if a == b else f"{tag}:{a}-{b}"
    return f"{tag}:{a}"


def line_at(path: str, needle: str, where: str = "pin") -> str:
    text, _ = _text_for(path, where)
    hits = lines_with(text, needle)
    if not hits:
        raise SystemExit(f"anchor not found: {path} {needle!r}")
    return text.split("\n")[hits[0] - 1].strip()


def f3(x: float) -> str:
    return f"{x:+.3f}"


# ------------------------------------------------------- ported record code --
# Each port names its clone locator; outputs are compared with the committed
# artifact the original produced.

def binom_p_ge(x, n, p0):
    """f_sessions.py binom_p_ge (lgamma form, as the monitors computed it)."""
    from math import exp, lgamma, log
    if x <= 0:
        return 1.0
    lp, l1p = log(p0), log(1.0 - p0)
    return float(sum(
        exp(lgamma(n + 1) - lgamma(i + 1) - lgamma(n - i + 1)
            + i * lp + (n - i) * l1p) for i in range(x, n + 1)))


def fisher_one_sided(a, n1, c, n2):
    """f_sessions.py / f_postscreen_descriptive.py fisher_one_sided."""
    k, n = a + c, n1 + n2
    denom = math.comb(n, n1)
    return sum(math.comb(k, x) * math.comb(n - k, n1 - x)
               for x in range(a, min(k, n1) + 1)) / denom


def checkpoint_eval(rows, at_completion, evaluated):
    """f_sessions.py checkpoint_eval, ported over an in-memory prefix of the
    session file (the original re-read the file after every session)."""
    sham = [r for r in rows if r["arm"] == "sham"]
    sh_n, sh_x = len(sham), sum(1 for r in sham if r["excluded"])
    flags, pauses = [], []
    for c in CONTRASTS:
        sub = [r for r in rows if r["arm"] == c]
        n, x = len(sub), sum(1 for r in sub if r["excluded"])
        if n not in GUARD_CHECKPOINTS and not at_completion:
            continue
        key = (c, "end" if at_completion else n)
        if key in evaluated:
            continue
        evaluated.add(key)
        p_abs = binom_p_ge(x, n, 0.20) if n else 1.0
        line = f"guard[{c}] n={n} x={x} binom p={p_abs:.4f} vs .20"
        p_rel = 1.0
        if sh_n >= 12:
            p_rel = fisher_one_sided(x, n, sh_x, sh_n)
            line += f"; sham {sh_x}/{sh_n} Fisher p={p_rel:.4f}"
        flags.append(line)
        if p_abs < 0.05:
            pauses.append(f"guard[{c}] absolute p={p_abs:.4f}")
        if p_rel < 0.05:
            pauses.append(f"guard[{c}] sham-relative p={p_rel:.4f}")
    if at_completion or any(len([r for r in rows if r["arm"] == c])
                            in GUARD_CHECKPOINTS for c in CONTRASTS):
        n_all = len(rows)
        lx = sum(1 for r in rows
                 if (r["exclude_reason"] or "").startswith("lexical"))
        p_lex = binom_p_ge(lx, n_all, 0.05) if n_all else 1.0
        cap_n = sum(r["n_rounds"] for r in rows)
        cap_x = sum(r["n_cap_hits"] for r in rows)
        p_cap = binom_p_ge(cap_x, cap_n, 0.10) if cap_n else 1.0
        ch = [c for r in rows for c in r["choices"]]
        lm_x = sum(1 for c in ch if c["label_mass"] < 0.2)
        p_lm = binom_p_ge(lm_x, len(ch), 0.20) if ch else 1.0
        flags.append(f"pooled: lex {lx}/{n_all} p={p_lex:.4f}; cap "
                     f"{cap_x}/{cap_n} p={p_cap:.4f}; low-mass "
                     f"{lm_x}/{len(ch)} p={p_lm:.4f}")
        for p, nm in ((p_lex, "LEXICAL"), (p_cap, "CAP"), (p_lm, "MASS")):
            if p < 0.05:
                pauses.append(f"pooled {nm} p={p:.4f}")
    return pauses, flags


def mean(xs):
    return sum(xs) / len(xs)


def analyze(rows):
    """f_sessions.py analyze(): the screen statistic, ported (numpy's mean of
    booleans replaced by sum/len; identical in exact arithmetic)."""
    valid = [r for r in rows if not r.get("excluded")]
    sham_first = [r["first_free_pick_P"] for r in valid
                  if r["arm"] == "sham" and r["first_free_pick_P"] is not None]
    pseudo = abs(float(mean(sham_first)) - 0.5) if sham_first else None
    out, detail = {}, {}
    for c in CONTRASTS:
        firsts = [r["first_free_pick_P"] for r in valid if r["arm"] == c
                  and r["first_free_pick_P"] is not None]
        n, k = len(firsts), int(sum(firsts))
        d = k / n - 0.5
        by_map, by_map_kn = {}, {}
        for m in (False, True):
            mm = [r["first_free_pick_P"] for r in valid
                  if r["arm"] == c and r["swap"] == m
                  and r["first_free_pick_P"] is not None]
            by_map["B" if m else "A"] = (round(float(mean(mm)) - 0.5, 4)
                                         if mm else None)
            by_map_kn["B" if m else "A"] = (int(sum(mm)), len(mm))
        p_hi = sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n
        p_lo = sum(math.comb(n, i) for i in range(0, k + 1)) / 2 ** n
        two_sided = c == "DIFF"
        p = min(1.0, 2 * min(p_hi, p_lo)) if two_sided else p_hi
        conj1 = pseudo is not None and (abs(d) if two_sided else d) > pseudo
        conj2 = all(v is not None and ((v >= 0) if (d >= 0) else (v <= 0))
                    for v in by_map.values())
        conj3 = p < 0.05
        out[c] = {"n": n, "delta": round(d, 4), "by_map": by_map,
                  "p": round(p, 5), "sided": "two" if two_sided else "one",
                  "conjuncts": [conj1, conj2, conj3],
                  "screen_hit": conj1 and conj2 and conj3}
        detail[c] = {"k": k, "n": n, "delta_exact": d, "p_exact": p,
                     "by_map_kn": by_map_kn, "p_hi": p_hi, "p_lo": p_lo}
    return out, pseudo, (sum(sham_first), len(sham_first)), detail


def response_texts(row):
    """f_postscreen_descriptive.py response_texts (the analyzer's own recovery
    of round text from the transcript; .strip() as there)."""
    return [l[len("Response:"):].strip()
            for l in row["transcript"].split("\n")
            if l.startswith("Response:")]


PREAMBLE_MARKERS = ["Let's", "Let us", "To solve", "To find", "To determine",
                    "First", "Step 1", "We need", "I'll", "I will",
                    "We can", "Breaking"]


def binom_two_sided(k, n):
    if n == 0:
        return None
    p_hi = sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n
    p_lo = sum(math.comb(n, i) for i in range(0, k + 1)) / 2 ** n
    return min(1.0, 2 * min(p_hi, p_lo))


def session_features(r):
    """f_postscreen_descriptive.py session_features (forced phase = first 4)."""
    texts = response_texts(r)
    feats = {"P": [0.0, 0, 0, 0], "Q": [0.0, 0, 0, 0]}
    for i, rd in enumerate(r["rounds"][:4]):
        cfg = rd["cfg"]
        feats[cfg][0] += rd["n_tok"]
        feats[cfg][1] += 1
        t = texts[i] if i < len(texts) else ""
        if any(t.startswith(m) for m in PREAMBLE_MARKERS):
            feats[cfg][2] += 1
        if rd.get("degen"):
            feats[cfg][3] += 1
    out = {}
    for cfg in "PQ":
        s, n, tr, dg = feats[cfg]
        out[cfg] = {"meanlen": (s / n if n else None), "trunc": tr, "degen": dg}
    return out


def postscreen_feature(valid, key):
    pooled_k = pooled_n = ties = 0
    per_arm = {}
    for arm in ARMS:
        k = n = 0
        for r in valid:
            if r["arm"] != arm:
                continue
            f = session_features(r)
            vP, vQ = f["P"][key], f["Q"][key]
            if vP is None or vQ is None or vP == vQ:
                ties += int(vP == vQ)
                continue
            smaller_cfg = "P" if vP < vQ else "Q"
            chose = "P" if r["first_free_pick_P"] else "Q"
            k += int(chose == smaller_cfg)
            n += 1
        if n:
            per_arm[arm] = {"k": k, "n": n, "share": round(k / n, 3),
                            "p": round(binom_two_sided(k, n), 4)}
        pooled_k += k
        pooled_n += n
    return {"pooled": {"k": pooled_k, "n": pooled_n,
                       "share": round(pooled_k / pooled_n, 3) if pooled_n else None,
                       "p": binom_two_sided(pooled_k, pooled_n)},
            "per_arm": per_arm, "ties_dropped": ties}


def corrupt_f1(text, item_idx, rate=0.12):
    """f_sessions.py corrupt() (= f0_calibrate.py corrupt()), replayed.
    Returns (render, n_draws) -- n_draws counts slots where a replacement
    letter was drawn (it may equal the original: 26-letter draw)."""
    import numpy as np
    rng = np.random.default_rng(zlib.crc32(f"corr|{item_idx}".encode()) % 2 ** 31)
    out, word_start, draws = [], True, 0
    for ch in text:
        if ch.isalpha() and not word_start and rng.random() < rate:
            out.append(chr(ord('a') + int(rng.integers(26))))
            draws += 1
        else:
            out.append(ch)
        word_start = not ch.isalpha()
    return "".join(out), draws


def signflip_two_sided(devs):
    """Exact two-sided sign-flip (Fisher-Pitman, one-sample) test on integer
    per-session deviations: under H0 each nonzero deviation's sign is +/- with
    probability 1/2 independently; statistic S = sum; p = P(|S*| >= |S_obs|)
    by full enumeration of the 2^m sign patterns (via the distribution of S*).
    Zero deviations carry no sign information and are dropped. Returns
    (S_obs, m nonzero, p)."""
    nz = [d for d in devs if d != 0]
    s_obs = sum(nz)
    dist = collections.Counter({0: 1})
    for d in nz:
        nd = collections.Counter()
        for s_, c_ in dist.items():
            nd[s_ + d] += c_
            nd[s_ - d] += c_
        dist = nd
    tail = sum(c_ for s_, c_ in dist.items() if abs(s_) >= abs(s_obs))
    return s_obs, len(nz), tail / 2 ** len(nz)


def hamming(a: str, b: str) -> int:
    assert len(a) == len(b)
    return sum(1 for x, y in zip(a, b) if x != y)


# ----------------------------------------------------------------- the audit --

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEF_OUT)
    ap.add_argument("--json-out", default=DEF_JSON)
    args = ap.parse_args()
    out_md = args.out if os.path.isabs(args.out) else os.path.join(REPO, args.out)
    out_js = (args.json_out if os.path.isabs(args.json_out)
              else os.path.join(REPO, args.json_out))

    stamp = subprocess.run(["date", "-u"], capture_output=True, text=True).stdout.strip()
    head = git("rev-parse", "HEAD").decode().strip()
    pin_full = git("rev-parse", PIN).decode().strip()
    script_rel = os.path.relpath(os.path.abspath(__file__), REPO)
    with open(os.path.abspath(__file__), "rb") as f:
        script_sha = sha256_bytes(f.read())
    cmd = " ".join(shlex.quote(a) for a in [sys.executable] + sys.argv)
    import numpy as np
    np_ver = np.__version__

    L: list[str] = []          # markdown lines
    J: dict = {"item": "N5", "pin": pin_full}
    FIG: list[dict] = []       # figures table

    def fig(figure, value, source, status, note=""):
        FIG.append({"figure": figure, "value": value, "source": source,
                    "status": status, "note": note})

    # --------------------------------------------------------------- header --
    blk = pinned(BLOCK)
    blk_sha = sha256_bytes(blk)
    blk_lines = blk.decode().split("\n")
    n5a = lines_with(blk.decode(), "### N5. f1 natural-reinforcer figures")[0]
    L += ["# AUDIT-note-release v1.2 -- N5: f1 natural-reinforcer figures", "",
          f"- Code stamp: {stamp} (date -u)  [run metadata]",
          f"- HEAD at run time: {head}  [run metadata; every record read below is pinned to {PIN} unless marked post-pin or working tree]",
          f"- Command: `{cmd}`  [run metadata]",
          f"- Pin: {PIN} = {pin_full}",
          f"- Block: `{BLOCK}`@{PIN} sha256 `{blk_sha}` ({'MATCH' if blk_sha == BLOCK_SHA else 'MISMATCH'} vs routed 8cd8a9ac...3841; {len(blk_lines) - (1 if blk_lines[-1] == '' else 0)} lines); item N5 = block lines {n5a}-{n5a + 1}",
          f"- Script: `{script_rel}` sha256 `{script_sha}`",
          f"- Interpreter: {sys.executable} (Python {platform.python_version()}); numpy {np_ver} used only to replay f1's corruptor (its rng is numpy's); exact tests stdlib (math.comb); no scipy/sklearn; no model",
          "",
          "Status vocabulary: reproduced (this script computes the figure from committed JSON/JSONL and prints it) | log-only (prose only; pinned locator) | not found | discrepant | computed-new (a computation the record does not contain). Locators are `path@bbc9ffe:line` as `git show bbc9ffe:<path>` numbers them. Every rate names its domain; every p its test and sidedness.",
          ""]
    assert blk_sha == BLOCK_SHA, "block sha mismatch"
    # the working-tree preprint (untracked; committed at the tag): hash it before
    # quoting it; round 9: asserted equal to the preprint of record (ruling 9)
    with open(os.path.join(REPO, PREPRINT), "rb") as f:
        pp_bytes = f.read()
    pp_sha = sha256_bytes(pp_bytes)
    pp_text = pp_bytes.decode("utf-8")
    pp_lines = pp_text.split("\n")
    pp_match = pp_sha == PREPRINT_SHA
    pp_match_block = pp_sha.startswith(PREPRINT_SHA_BLOCK[0]) and pp_sha.endswith(PREPRINT_SHA_BLOCK[1])
    assert pp_match, f"{PREPRINT} sha256 {pp_sha} != the preprint of record {PREPRINT_SHA} ({PREPRINT_RULING})"
    PP_REC = f"{PREPRINT_SHA[:8]}…{PREPRINT_SHA[-5:]}"
    pp_tag = f"{PREPRINT} (working tree, untracked; sha256 {pp_sha[:8]}...{pp_sha[-6:]}, computed at run time, MATCH vs the preprint of record {PP_REC}, {PREPRINT_RULING})"
    L.insert(-3, f"- Preprint quoted below: `{PREPRINT}` (root, untracked; committed at the tag) sha256 `{pp_sha}` computed at run time; the preprint of record ({PREPRINT_RULING}) is `{PP_REC}`: {'MATCH' if pp_match else 'MISMATCH'}. The block (line {lines_with(blk.decode(), 'd6431e97')[0]}) gives `d6431e97…222b8`: the audited text, superseded by patch v6 (round 9's preprint of record), itself superseded by patch v7; both archived untracked (out of the release; not required); see Rounds 9 and 10 at the end of this raw")

    def pp_n(needle: str):
        """Round 9: the line of `needle` on the patched preprint; a missing anchor
        does not stop the script (it is a finding on the patch, Round 9).
        Round 10: a needle patch v7 removed is located by its PP_REANCHOR entry
        (PP_REANCHOR_KIND; recorded in the Round 10 section)."""
        hits = lines_with(pp_text, needle) or (lines_with(pp_text, PP_REANCHOR[needle]) if needle in PP_REANCHOR else [])
        return hits[0] if hits else "? (not found on the patched text; Round 9)"
    J["header"] = {"stamp": stamp, "head": head, "block_sha256": blk_sha,
                   "script": script_rel, "script_sha256": script_sha,
                   "interpreter": sys.executable,
                   "python": platform.python_version(), "numpy": np_ver,
                   "command": cmd, "preprint": PREPRINT,
                   "preprint_sha256_computed": pp_sha,
                   "preprint_matches_block": pp_match_block,
                   "preprint_sha256_of_record": PREPRINT_SHA,
                   "preprint_matches_record": pp_match,
                   "preprint_of_record_ruling": PREPRINT_RULING,
                   "preprint_audited": {"block_abbrev": "d6431e97…222b8", "archived_untracked": PREPRINT_AUDITED,
                                        "superseded_by": "patch v6", "required": False}}

    # Round 10 (fix round): v6's anchor lines are rebuilt from v7's here, and each
    # sentence patch v7 changed gets its finding id here, before any statement
    # about a preprint sentence is built, so that a statement whose check patch v7
    # flips is worded where it is built: against the audited and v6 texts, naming
    # the v7 finding (round 9's mechanism for §7d (iii) and the dose row), never
    # citing v7's line for wording v7 removed. The checks are the round-9 claims'
    # own predicates (CLAIMS9; the claims list of the Round 9 section uses them,
    # and that section is asserted equal to the round-9 record). Figure rows gain
    # no digit in a value or a note (N1 reads figures from them); labels, values
    # and statuses are untouched.
    def v6_from_v7(n_: int, line: str):
        """v6's line n_ from v7's: identical, or every registered v6 sentence of
        the line substituted back; sha256-verified. Returns (v6 line,
        [(v6 sentence, v7 sentence, name), ...])."""
        subs, rb_ = [], line
        for (m_, a_, e_, s6_, nm_) in PP_V6_SENTENCES:
            if m_ == n_:
                i_ = rb_.index(a_)
                j_ = rb_.index(e_, i_) + len(e_)
                subs.append((s6_, rb_[i_:j_], nm_))
                rb_ = rb_[:i_] + s6_ + rb_[j_:]
        assert sha256_bytes(rb_.encode()) == PP_V6_LINE_SHA[n_], f"v6 line {n_}: rebuild disagrees with its sha256 constant"
        return rb_, subs

    v6_rb = {n_: v6_from_v7(n_, pp_lines[n_ - 1]) for n_ in sorted(PP_V6_LINE_SHA)}
    # the v6 line with ONE v7 sentence substituted in, per changed sentence
    sent10 = []                                   # (finding id, name, line, v6 sentence, v7 sentence, v6 line with it alone)
    for n_, (l6_, subs_) in v6_rb.items():
        for (s6_, s7_, nm_) in subs_:
            assert l6_.count(s6_) == 1
            sent10.append((f"P10-{len(sent10) + 1}", nm_, n_, s6_, s7_, l6_.replace(s6_, s7_)))
    sent10.sort(key=lambda x_: (x_[2], v6_rb[x_[2]][0].index(x_[3])))
    sent10 = [(f"P10-{i_}",) + x_[1:] for i_, x_ in enumerate(sent10, start=1)]

    def sent(t: str, ph: str):
        """The sentence of line t that carries ph (split after '.' + whitespace), or ''."""
        return next((s_ for s_ in re.split(r"(?<=\.)\s+", t) if ph in s_), "")

    _dose_s = "found below its visibility criterion"
    _fdbk_s = "no evaluation-seeking against a predominantly positive feedback stream"
    _len_nd = "generic length-preference deflation was tested and failed"
    _term_nd = "session-termination attempts occur at about 1% of rounds"
    _menu_nd = "Menu behavior is exploration-dominant in every arm"
    CLAIMS9 = {  # key -> (claim, anchor, predicate over the anchor's line): round 9's claims 2-8, verbatim
        "attrib": ("the CORR dose clause attributes the finding to a calibration (§8.1)", _dose_s,
                   lambda t: "a later calibration (§8.1)" in t),
        "crit": ("the CORR dose clause's criterion is the later calibration's ('its visibility criterion'), which §7d (ii) finds is m's, not f1's",
                 _dose_s, lambda t: "a later calibration" in sent(t, _dose_s) and "its visibility criterion" in sent(t, _dose_s)),
        "keeps": ("the CORR dose clause keeps 'a later calibration' without citing G-CAL's artifact or calling it a replay",
                  _dose_s,
                  lambda t: "a later calibration" in sent(t, _dose_s) and not any(w in sent(t, _dose_s) for w in ("G-CAL", POST_PIN_GCAL, "replay"))),
        "unsigned": ("the length-preference phrase is unsigned", _len_nd,
                     lambda t: "length-preference" in t and not any(w in t for w in ("brevity", "shorter", "longer"))),
        "share": ("'session share ≈ .50' in every arm, neither the range nor FDBK named", _menu_nd,
                  lambda t: "session share ≈ .50" in t and "FDBK" not in t),
        "first": ("the FDBK clause 'no evaluation-seeking against a predominantly positive feedback stream' is a first-choice statement and does not say so",
                  _menu_nd,
                  lambda t: _fdbk_s in sent(t, _fdbk_s) and not any(w in sent(t, _fdbk_s).lower() for w in ("first choice", "first-choice", "first pick", "first-pick", "first free"))),
        "uniform": ("'uniformly across arms', not 'no detectable heterogeneity'", _term_nd,
                    lambda t: "uniformly across arms" in t and "no detectable heterogeneity" not in t),
    }

    def pp10(nd: str, fn):
        """(held on v6, holds on v7, [ids of the v7 sentences that alone flip it]) for a check over the anchor's line."""
        n_ = pp_n(nd)
        assert isinstance(n_, int), f"anchor '{nd}' not on the preprint of record"
        l7_ = pp_lines[n_ - 1]
        l6_ = v6_rb[n_][0] if n_ in v6_rb else l7_
        v6_, v7_ = fn(l6_), fn(l7_)
        by_ = [x_[0] for x_ in sent10 if x_[2] == n_ and fn(x_[5]) != v6_] if v6_ != v7_ else []
        return v6_, v7_, by_

    RW10, RW10_FN = [], []   # every statement below about a preprint sentence that Round 10 checks; its predicate

    def rw10(where_: str, check_: str, nd: str, fn, old_: str, new_, row: bool = False) -> str:
        """old_ while the check holds on v7 (as it held on v6); new_(ids) -- worded against the audited and v6 texts,
        naming the v7 finding (in a figure row's note or source, row=True: no digit, 'a finding on the patch,
        closing sections') -- where patch v7 flips it. Every check here held on v6 (round 9's record)."""
        v6_, v7_, by_ = pp10(nd, fn)
        assert v6_ is True, f"{where_}: '{check_}' did not hold on v6"
        rew_ = v7_ is not True
        out_ = new_(", ".join(by_)) if rew_ else old_
        if row and rew_:   # a figure row's re-worded text gains no digit (N1 reads figures from rows)
            assert sorted(re.findall(r"\d+", out_)) == sorted(re.findall(r"\d+", old_)), f"{where_}: digits changed"
        RW10.append({"where": where_, "check": check_, "anchor": nd, "v7_line": pp_n(nd), "held_on_v6": v6_,
                     "holds_on_v7": v7_, "reworded": rew_, "figure_row": row, "flipped_by": by_})
        RW10_FN.append(fn)
        return out_

    def l7of(nd: str) -> str:
        return pp_lines[pp_n(nd) - 1]

    # ------------------------------------------------------ 0. integrity --
    L += ["## 0. Referents and integrity", ""]
    data_paths = ["data/f/sessions.jsonl", "data/f/sessions_smoke.jsonl",
                  "data/f/screen_analysis.json", "data/f/postscreen_descriptive.json",
                  "data/f/calib.json", "data/f/pools.json",
                  "data/configs/f_termination_patterns.json",
                  "PROPOSAL-f-natural-reinforcer-screen.md",
                  "results/raw/2026-08-10_f_run.txt", "results/raw/2026-08-10_f_analysis.txt",
                  "results/raw/2026-08-10_f_postscreen_descriptive.txt",
                  "results/raw/2026-08-10_f_ndecl.txt", "results/raw/2026-08-10_f_calib.txt",
                  "results/raw/2026-08-10_f_calib2.txt", ARCH, "FINDINGS-4.md"]
    integ = {}
    L.append("Committed artifacts read at the pin (sha256 of the pinned blob; working tree compared by git blob id):")
    L.append("")
    for p in data_paths:
        eq = blob_equal_to_pin(p)
        integ[p] = {"sha256": sha256_bytes(pinned(p)), "working_tree_equal": eq}
        L.append(f"- `{p}` `{integ[p]['sha256'][:16]}`; working tree {'EQUAL to pin' if eq else 'DIFFERS from pin'}")
    J["integrity"] = integ
    pools_b = pinned("data/f/pools.json")
    calib = pinned_json("data/f/calib.json")
    term_b = pinned("data/configs/f_termination_patterns.json")
    run_raw = pinned_text("results/raw/2026-08-10_f_run.txt")
    chk_pools = sha256_bytes(pools_b)[:16]
    chk_term = sha256_bytes(term_b)[:16]
    L += ["",
          f"- pools sha256[:16] = `{chk_pools}`; calib.json `pools_sha` = `{calib['pools_sha']}` ({'EQUAL' if chk_pools == calib['pools_sha'] else 'DIFFERENT'}); run raw line: `{line_at('results/raw/2026-08-10_f_run.txt', 'pools sha')}` ({'EQUAL' if chk_pools in run_raw else 'NOT IN RAW'}) -- the screen ran on the pools calib.json calibrated (f0 v2).",
          f"- f_termination_patterns.json sha256[:16] = `{chk_term}`; run raw: `{line_at('results/raw/2026-08-10_f_run.txt', 'termination counter')}` ({'EQUAL' if f'sha {chk_term}' in run_raw else 'DIFFERENT'}).",
          ""]
    assert chk_pools == calib["pools_sha"] and chk_pools in run_raw
    assert f"sha {chk_term}" in run_raw
    L.append("Producing analyzers (gitignored clone, NOT in the record; read, not imported -- they import mlx; ported below line for line and checked against the artifacts they wrote):")
    L.append("")
    clone_sha = {}
    for p in (F_SESS, F_POST, F_CAL):
        with open(os.path.join(REPO, p), "rb") as f:
            clone_sha[p] = sha256_bytes(f.read())
        L.append(f"- `{p}` sha256 `{clone_sha[p][:16]}`")
    ports = {
        "analyze()": loc(F_SESS, "def analyze(path):", "\"hits\": hits}, f, indent=1)", where="clone"),
        "checkpoint_eval()": loc(F_SESS, "def checkpoint_eval(", "    return pauses, flags", where="clone"),
        "binom_p_ge()": loc(F_SESS, "def binom_p_ge(", "            + i * lp + (n - i) * l1p) for i in range(x, n + 1)))", where="clone"),
        "corrupt()": loc(F_SESS, "def corrupt(text, item_idx):", "    return \"\".join(out)", where="clone"),
        "termination counter (in run_round)": loc(F_SESS, "adjudication 27446d3: termination-attempt counter", "                break", where="clone"),
        "FDBK verdict line (in run_round)": loc(F_SESS, "if arm == \"FDBK\" and cfg == \"P\":", "verdict = f\"Result:", where="clone"),
        "postscreen features": loc(F_POST, "def session_features(r):", "\"ties_dropped\": ties}", where="clone"),
        "f0 corr_sha": loc(F_CAL, "corr_items = [corrupt(", "\"\\n\".join(corr_items).encode()).hexdigest()[:16]", where="clone"),
    }
    L.append("")
    for k, v in ports.items():
        L.append(f"- port of {k}: {v}")
    J["clone"] = {"sha256": clone_sha, "ports": ports}
    L.append("")

    # --------------------------------------------------- 1. the f1 entry --
    vstart = loc(ARCH, "f1 SCREEN VERDICT: FIVE NULLS", "further experiments licensed.**")
    pstart = loc(ARCH, "f1 post-screen descriptive (POST-HOC, LABELED", "FINDINGS-4 (design instance).**")
    # the entry's last line is the continuation after 'After the screen: ...'
    # (values-check finding 10: the span ends one line later than v1 printed)
    prereg = loc(ARCH, "f1 PRE-REGISTRATION — natural-reinforcer screen.", "    pre-registration.")
    _after = int(loc(ARCH, "After the screen: pause for design-instance read before ANY f2").rsplit(":", 1)[1])
    assert prereg.endswith(f"-{_after + 1}"), prereg
    f0v2 = loc(ARCH, "f0 recalibration v2 ALL BARS PASS")
    # round-2 finding 6: the ledger's paragraph runs to the 'optional stopping' line (:44)
    LOC_F4_LEDGER = loc('FINDINGS-4.md', '## Summary ledger', 'completing an arm after observing its data is optional stopping')
    L += ["## 1. The f1 VERDICTS entry (located and pinned)", "",
          f"- f1 SCREEN VERDICT (2026-08-10): {vstart}",
          f"- f1 post-screen descriptive (POST-HOC, labeled) + below-floor resolution: {pstart}",
          f"- f1 PRE-REGISTRATION (directions, primary, conjuncts, floors, monitors): {prereg}",
          f"- f0 recalibration v2 (the calibration of record for the run's pools): {f0v2}; its 'CORR delta +.078 covariate' at {loc(ARCH, 'CORR delta +.078 covariate')}",
          f"- FINDINGS-4 summary ledger: {LOC_F4_LEDGER}",
          f"- PROPOSAL-f §2 contrasts table and §3 statistics: {loc('PROPOSAL-f-natural-reinforcer-screen.md', '| # | Contrast |', '| 5 | FDBK |')}; {loc('PROPOSAL-f-natural-reinforcer-screen.md', '**Screen tier (f1).**', 'preferences and will miss moderate ones')}",
          ""]
    fig("f1 VERDICTS entry (Code locates)", f"{vstart}", "archive/RESULTS-cycles3-4.md (the block's referent)", "log-only",
        "located; 2026-08-10 'f1 SCREEN VERDICT: FIVE NULLS'; post-hoc descriptive at " + pstart)

    # ------------------------------------------- 2. run integrity / pauses --
    rows = pinned_jsonl("data/f/sessions.jsonl")
    smoke = pinned_jsonl("data/f/sessions_smoke.jsonl")
    by_arm = collections.Counter(r["arm"] for r in rows)
    ndecl = pinned_text("results/raw/2026-08-10_f_ndecl.txt")
    decl = {}
    for m in re.finditer(r"\b(SOLV|CORR|NOV|DIFF|FDBK|sham) (\d+)\b", ndecl.split("Declared plan", 1)[1]):
        decl.setdefault(m.group(1), int(m.group(2)))
    keys = [(r["arm"], r["session"]) for r in rows]
    uniq = len(set(keys))
    contiguous = all(sorted(r["session"] for r in rows if r["arm"] == a) == list(range(by_arm[a])) for a in ARMS)
    prog = re.findall(r"^\s+\[(\d+)/344\] (\w+) s(\d+): first=([PQX])(?: EXCL (.+?))?  \d+s\r?$", run_raw, flags=re.M)
    order_ok = len(prog) == len(rows) and all(
        (a == r["arm"] and int(s) == r["session"] and int(j) == i + 1
         and fp == ("P" if r["first_free_pick_P"] else ("Q" if r["first_free_pick_P"] is not None else "X"))
         and (ex or None) == (r["exclude_reason"] if r["excluded"] else None))
        for i, ((j, a, s, fp, ex), r) in enumerate(zip(prog, rows)))
    smoke_idx = sorted({r["session"] for r in smoke})
    # monitor replay, in file order (= run order, verified just above)
    evaluated, rep_flags, rep_pauses = set(), [], []
    for i in range(len(rows)):
        pz, fl = checkpoint_eval(rows[: i + 1], False, evaluated)
        rep_flags += fl
        rep_pauses += pz
    pz, fl = checkpoint_eval(rows, True, evaluated)
    rep_flags += fl
    rep_pauses += pz
    raw_flags = [l.strip() for l in run_raw.split("\n")
                 if l.startswith("  guard[") or l.startswith("  pooled:")]
    flags_equal = rep_flags == raw_flags
    n_pause_str = len(re.findall(r"PAUSE|COMPLETION FLAGS|INCIDENT|resume:", run_raw))
    L += ["## 2. 344/344 sessions and zero pauses", "",
          f"- Rows in `data/f/sessions.jsonl`: {len(rows)}; distinct (arm, session): {uniq}; per arm {dict(by_arm)}; N declaration {decl} ({loc('results/raw/2026-08-10_f_ndecl.txt', 'SOLV 64')}-{lines_with(ndecl, 'sham 40')[0]}): {'EQUAL' if all(by_arm[a] == decl.get(a) for a in ARMS) else 'DIFFERENT'}; session indices 0..n-1 per arm: {contiguous}.",
          f"- Smoke rows (`sessions_smoke.jsonl`, {len(smoke)} rows, indices {smoke_idx[0]}..{smoke_idx[-1]}) are outside every tally (offset >= 1000; {loc(ARCH, 'Smoke indices ≥ 1000, never in verdict tallies')}).",
          f"- The run raw's {len(prog)} progress lines `[j/344] arm sN: first=... [EXCL reason]` match the JSONL rows in file order on index, arm, session, first pick and exclusion reason: {order_ok}. So the file order is the run order, and the run was one pass (no `resume:` line).",
          f"- Monitor replay: f1's `checkpoint_eval` (ported) re-run after every row in file order and once at completion reproduces the run raw's {len(raw_flags)} printed monitor lines (`guard[...]`, `pooled: ...`) string for string: {flags_equal}. Pause conditions met in the replay: {len(rep_pauses)}. Strings PAUSE / COMPLETION FLAGS / INCIDENT / resume: in the run raw: {n_pause_str}.",
          f"- Completion monitors (replayed): " + "; ".join(rep_flags[-6:]),
          ""]
    assert len(rows) == 344 and uniq == 344 and order_ok and flags_equal and not rep_pauses
    fig("344/344 sessions", f"{len(rows)} rows, {uniq} distinct; per arm {dict(by_arm)} = N declaration",
        "data/f/sessions.jsonl; results/raw/2026-08-10_f_ndecl.txt", "reproduced",
        f"record: {loc(ARCH, '344/344')}")
    fig("zero pauses", f"0 pause conditions in a replay of f1's checkpoint_eval over the 344 rows in run order; {len(raw_flags)}/{len(raw_flags)} printed monitor lines reproduced verbatim",
        "data/f/sessions.jsonl (excluded, exclude_reason, n_rounds, n_cap_hits, choices[].label_mass); results/raw/2026-08-10_f_run.txt", "reproduced",
        "checkpointed exact binomial guards vs p0 .20 at arm n = 24 and completion, one-sided Fisher vs sham at sham n >= 12, pooled lexical p0 .05, cap-hit p0 .10 (rounds), low label mass p0 .20 (choices), all one-sided, pause at p < .05. Scope: the 344-session screen run; the f1 smokes before it paused three times under the smoke bars (" + "; ".join(loc(ARCH, nd) for nd in ("f1 smoke — PAUSED under the inherited", "smoke2 PAUSED by", "f1 smoke2r — re-scoped bars PASSED")) + ")")
    J["run_integrity"] = {"rows": len(rows), "distinct": uniq, "per_arm": dict(by_arm),
                          "declared": decl, "order_matches_run_raw": order_ok,
                          "monitor_lines_reproduced": flags_equal,
                          "n_monitor_lines": len(raw_flags), "replay_pauses": rep_pauses,
                          "completion_monitors": rep_flags[-6:]}

    # ---------------------------------------------------- 3. five contrasts --
    screen = pinned_json("data/f/screen_analysis.json")
    mine, pseudo, sham_kn, det = analyze(rows)
    same = {c: mine[c] == screen["contrasts"][c] for c in CONTRASTS}
    pseudo_same = pseudo == screen["sham_pseudo"]
    valid = [r for r in rows if not r["excluded"]]
    vby = collections.Counter(r["arm"] for r in valid)
    L += ["## 3. The five contrasts (screen tier; first free choice)", "",
          "**Definition (pre-registered, " + loc(ARCH, "Primary & screen-hit conjuncts (per contrast)", "the screen hunts strong preferences.") + "):** per contrast, over valid sessions (not excluded in any phase; `valid` = `not excluded`, f_sessions.py analyze), k = sessions whose first free choice picked the P label, n = valid sessions, Δ_c = k/n − ½. P is the pre-registered target config (DIFF: P = easy, evaluated two-sided). Test: exact binomial against ½ -- one-sided upper tail P(X ≥ k | n, ½) for SOLV, NOV, CORR, FDBK; two-sided 2·min(tails), capped at 1, for DIFF. Screen hit = (1) Δ_c (|Δ_c| for DIFF) > sham pseudo-Δ = |share_sham − ½|; (2) both counterbalance maps' Δ on Δ_c's side (map A: swap = False, map B: swap = True); (3) p < .05. No claim from screen data.",
          "",
          f"Sham pseudo-Δ: {sham_kn[0]}/{sham_kn[1]} first picks to P → |{sham_kn[0]}/{sham_kn[1]} − ½| = {pseudo:.6f} (stored {screen['sham_pseudo']}; {'EQUAL' if pseudo_same else 'DIFFERENT'}).",
          "",
          "| contrast | P (target) vs Q | direction, sidedness | declared / valid n (floor 48) | k/n | Δ_c | map A k/n, Δ | map B k/n, Δ | p (test) | conjuncts (1,2,3) | stored JSON equal |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in CONTRASTS:
        d = det[c]
        a_k, a_n = d["by_map_kn"]["A"]
        b_k, b_n = d["by_map_kn"]["B"]
        tst = "exact binomial, two-sided" if c == "DIFF" else "exact binomial, one-sided upper"
        L.append(f"| {c} | {TARGET[c][0]} vs {TARGET[c][1]} | {TARGET[c][2]}, {TARGET[c][3]}-sided | {by_arm[c]} / {vby[c]}{' (BELOW floor)' if vby[c] < 48 else ''} | {d['k']}/{d['n']} | {d['delta_exact']:+.4f} | {a_k}/{a_n}, {mine[c]['by_map']['A']:+.4f} | {b_k}/{b_n}, {mine[c]['by_map']['B']:+.4f} | {d['p_exact']:.5f} ({tst}) | {mine[c]['conjuncts']} | {same[c]} |")
    L += ["", f"Sham valid n = {vby['sham']} (floor 32). Valid-n floors: {loc('PROPOSAL-f-natural-reinforcer-screen.md', 'n = 48 valid sessions (24 per')}; {loc(ARCH, '**N (floors):** 48/contrast')}; below-floor clause {loc(ARCH, 'Below-floor condition (declared clause fires)')}; resolution (scoped nulls, no top-ups) {loc(ARCH, 'Below-floor resolution (adjudicated)')}.", ""]
    assert all(same.values()) and pseudo_same
    J["contrasts"] = {c: {**mine[c], "k": det[c]["k"], "by_map_kn": det[c]["by_map_kn"],
                          "p_exact": det[c]["p_exact"]} for c in CONTRASTS}
    J["sham_pseudo"] = {"k": sham_kn[0], "n": sham_kn[1], "value": pseudo}

    s = det["SOLV"]
    fig("SOLV +.020 p = .44", f"{s['k']}/{s['n']} → Δ {s['delta_exact']:+.4f}; P(X ≥ {s['k']} | {s['n']}, ½) = {s['p_exact']:.5f}",
        "data/f/screen_analysis.json contrasts.SOLV (delta, p, n)", "reproduced", "one-sided exact binomial (H1: avoid ill-posed); valid n 50 of 64")
    d_ = det["DIFF"]
    fig("DIFF −.096 p = .24", f"{d_['k']}/{d_['n']} first picks to EASY → Δ {d_['delta_exact']:+.4f} (toward hard); 2·P(X ≤ {d_['k']} | {d_['n']}, ½) = {d_['p_exact']:.5f}",
        "data/f/screen_analysis.json contrasts.DIFF", "reproduced", "two-sided exact binomial; conjuncts (1) and (2) pass, (3) fails; P = easy")
    fig("DIFF valid-n floor", f"valid {vby['DIFF']} of {by_arm['DIFF']} declared, floor 48: below by 1 (FDBK {vby['FDBK']} of {by_arm['FDBK']}, below by 4)",
        "data/f/sessions.jsonl (excluded); floor " + loc('PROPOSAL-f-natural-reinforcer-screen.md', 'n = 48 valid sessions (24 per'), "reproduced",
        "adjudicated as scoped null, no top-up: " + loc(ARCH, 'Below-floor resolution (adjudicated)'))
    n_ = det["NOV"]
    fig("NOV −.066", f"{n_['k']}/{n_['n']} → Δ {n_['delta_exact']:+.4f} (toward repeated); P(X ≥ {n_['k']} | {n_['n']}, ½) = {n_['p_exact']:.5f}",
        "data/f/screen_analysis.json contrasts.NOV", "reproduced", "one-sided exact binomial (H1: prefer novel)")
    fig("NOV map-inconsistency", f"map A {n_['by_map_kn']['A'][0]}/{n_['by_map_kn']['A'][1]} → {mine['NOV']['by_map']['A']:+.4f}; map B {n_['by_map_kn']['B'][0]}/{n_['by_map_kn']['B'][1]} → {mine['NOV']['by_map']['B']:+.4f}; conjunct (2) False",
        "data/f/screen_analysis.json contrasts.NOV.by_map", "reproduced", "signs differ across maps")
    c_ = det["CORR"]
    fig("CORR 0.000", f"{c_['k']}/{c_['n']} → Δ {c_['delta_exact']:+.4f} exactly; P(X ≥ {c_['k']} | {c_['n']}, ½) = {c_['p_exact']:.5f}",
        "data/f/screen_analysis.json contrasts.CORR", "reproduced", "one-sided exact binomial (H1: avoid corrupted); FINDINGS-4's table prints p as '—' (" + loc('FINDINGS-4.md', '| CORR (avoid corrupted)') + "); the stored p is .55307")
    fig("CORR maps +.121/−.130", f"map A {c_['by_map_kn']['A'][0]}/{c_['by_map_kn']['A'][1]} → {mine['CORR']['by_map']['A']:+.4f}; map B {c_['by_map_kn']['B'][0]}/{c_['by_map_kn']['B'][1]} → {mine['CORR']['by_map']['B']:+.4f}",
        "data/f/screen_analysis.json contrasts.CORR.by_map", "reproduced", "mirror-cancel; map A = swap False (tag_P = pair[0])")
    fb = det["FDBK"]
    fig("FDBK +.023", f"{fb['k']}/{fb['n']} → Δ {fb['delta_exact']:+.4f}; P(X ≥ {fb['k']} | {fb['n']}, ½) = {fb['p_exact']:.5f}; maps {mine['FDBK']['by_map']['A']:+.4f}/{mine['FDBK']['by_map']['B']:+.4f}",
        "data/f/screen_analysis.json contrasts.FDBK", "reproduced", "one-sided exact binomial (H1: seek feedback); map-inconsistent; valid n 44 below floor")
    fig("sham pseudo-Δ .045 (conjunct-1 bar)", f"|{sham_kn[0]}/{sham_kn[1]} − ½| = {pseudo:.4f}", "data/f/screen_analysis.json sham_pseudo", "reproduced", "")

    # ---------------------------------- 3a. DIFF length-preference deflation --
    post = pinned_json("data/f/postscreen_descriptive.json")
    vpost = [r for r in rows if not r["excluded"] and r["first_free_pick_P"] is not None]
    feats = {}
    feat_same = {}
    for fname, key in (("shorter_rounds", "meanlen"), ("fewer_preamble_trunc", "trunc"), ("fewer_degen_rounds", "degen")):
        feats[fname] = postscreen_feature(vpost, key)
        stored = post["features"][fname]
        feat_same[fname] = (feats[fname]["pooled"]["k"] == stored["pooled"]["k"]
                            and feats[fname]["pooled"]["n"] == stored["pooled"]["n"]
                            and feats[fname]["per_arm"] == stored["per_arm"]
                            and feats[fname]["ties_dropped"] == stored["ties_dropped"])
    sr = feats["shorter_rounds"]
    # Code's direction check (computed-new): which DIFF config had the longer forced rounds
    dsess = [r for r in vpost if r["arm"] == "DIFF"]
    hard_longer = easy_longer = tie = 0
    tokP, tokQ = [], []
    for r in dsess:
        f = session_features(r)
        tokP.append(f["P"]["meanlen"]); tokQ.append(f["Q"]["meanlen"])
        if f["Q"]["meanlen"] > f["P"]["meanlen"]:
            hard_longer += 1
        elif f["Q"]["meanlen"] < f["P"]["meanlen"]:
            easy_longer += 1
        else:
            tie += 1
    # round-2 finding 1: task-text length per DIFF pool (descriptive; no text printed)
    _pl = json.loads(pinned("data/f/pools.json"))
    task_len = {k_: mean([len(it["task"]) for it in _pl[k_]]) for k_ in ("DIFF_easy", "DIFF_hard")}
    LOC_DIRCONS = loc(ARCH, "DIFF's own share", "toward-hard lean.")
    LOC_BREV_ARCH = loc(ARCH, "**brevity-tracking is", "length preference**")
    LOC_F4_S6 = loc('FINDINGS-4.md', '**6. The DIFF residual, recorded with its deflations tested.**', 'directionally consistent with toward-hard')
    LOC_F4_BREV = loc('FINDINGS-4.md', 'a generic brevity preference could', 'mimic it.')
    pp_lenpref = f"{PREPRINT}:{pp_n('generic length-preference deflation was tested and failed')}"
    assert hard_longer > easy_longer and task_len["DIFF_hard"] > task_len["DIFF_easy"]
    # Round 10 (fix round): the sign v7 gives the phrase, if any (the 'unsigned' claim's words)
    _sgn7 = next((w_ for w_ in ("longer", "shorter", "brevity") if w_ in sent(l7of(_len_nd), "length-preference")), None)
    _sgn7_ok = "the sign of this raw's direction check" if _sgn7 == "longer" else "not the sign of this raw's direction check"
    _len_c = CLAIMS9["unsigned"]
    len_row_stmt = rw10(
        "the length-test row's note", _len_c[0], _len_c[1], _len_c[2],
        f"the preprint's phrase is unsigned ('length-preference', {pp_lenpref}, working tree)",
        lambda by: (f"the preprint's phrase was unsigned on the audited text and on the patched text that preceded the preprint of record ('length-preference', "
                    f"{pp_lenpref}); the preprint of record signs it ('{_sgn7}', {_sgn7_ok}; a finding on the patch, "
                    f"closing sections)"), row=True)
    len_note5_stmt = rw10(
        "Note 5", _len_c[0], _len_c[1], _len_c[2],
        f"the preprint's phrase is unsigned ('length-preference', {pp_lenpref}, working tree)",
        lambda by: (f"the preprint's phrase was unsigned on the audited and v6 texts ('length-preference', {pp_lenpref}); "
                    f"v7 signs it ('{_sgn7}', {_sgn7_ok}; Round 10, {by})"))
    len_r21_stmt = rw10(
        "values-check R2-1's evidence", _len_c[0], _len_c[1], _len_c[2],
        f"the preprint's phrase is unsigned ({pp_lenpref})",
        lambda by: f"the preprint's phrase was unsigned on the audited and v6 texts ({pp_lenpref}; v7 signs it, '{_sgn7}': Round 10, {by})")
    L += ["### 3a. DIFF: the length-preference deflation test (POST-HOC, labeled in the record)", "",
          f"Record: {pstart}; analyzer {ports['postscreen features']}. Feature: for each valid session with a first pick (n = {len(vpost)}), the mean forced-round response length in tokens (`n_tok`, forced phase = first four rounds) per config; statistic = share of first free choices that went to the config with the SHORTER mean length, ties dropped; exact binomial against ½, two-sided. A generic length preference (here toward longer rounds, since hard rounds were the longer ones in {hard_longer}/{len(dsess)} DIFF sessions) would mimic a toward-hard lean if it were general; the two-sided test asks whether any length preference is general.",
          "",
          f"- pooled: {sr['pooled']['k']}/{sr['pooled']['n']} = {sr['pooled']['k'] / sr['pooled']['n']:.4f}, p = {sr['pooled']['p']:.4f} (two-sided exact binomial); ties dropped {sr['ties_dropped']}",
          "- per arm: " + "; ".join(f"{a} {v['k']}/{v['n']} = {v['share']:.3f}, p = {v['p']:.4f}" for a, v in sr["per_arm"].items()),
          f"- equal to `data/f/postscreen_descriptive.json` (all three features, pooled k/n, per-arm entries, ties): {feat_same}",
          f"- Code's direction check (computed-new, post-hoc, descriptive): in the {len(dsess)} valid DIFF sessions the HARD config's forced rounds were longer in {hard_longer}, shorter in {easy_longer}, tied in {tie}; mean forced n_tok easy {mean(tokP):.2f} vs hard {mean(tokQ):.2f}. So 'toward longer rounds' and 'toward hard' point the same way, which is what the record's 'directionally consistent' reading needs ({LOC_DIRCONS}). The task texts point the same way too (pool means: easy {task_len['DIFF_easy']:.1f} vs hard {task_len['DIFF_hard']:.1f} characters, `data/f/pools.json`): on either length a brevity (shorter-rounds) preference would push toward EASY, so the deflation that could mimic the toward-hard lean is a longer-rounds preference.",
          ""]
    assert all(feat_same.values())
    fig("DIFF length-preference deflation test (tested and failed)",
        f"shorter-rounds share pooled {sr['pooled']['k']}/{sr['pooled']['n']} = .498, p = {sr['pooled']['p']:.4f}; DIFF {sr['per_arm']['DIFF']['k']}/{sr['per_arm']['DIFF']['n']} = .383, p = {sr['per_arm']['DIFF']['p']:.4f}; sham {sr['per_arm']['sham']['k']}/{sr['per_arm']['sham']['n']} = .606, p = {sr['per_arm']['sham']['p']:.4f}",
        "data/f/postscreen_descriptive.json features.shorter_rounds", "reproduced",
        f"POST-HOC on the record; two-sided exact binomial vs ½, valid sessions with a first pick, ties dropped; 'failed' = no length preference is general (the record's words: 'brevity-tracking is NOT general', {LOC_BREV_ARCH}), so the DIFF lean does not deflate to one (hard was the longer config in {hard_longer}/{len(dsess)} DIFF sessions, so the candidate deflation is a longer-rounds preference); FINDINGS-4's account of the test, 'tested (ii) and it failed': {LOC_F4_S6}; {len_row_stmt}")
    J["diff_length_test"] = {"features": feats, "equal_to_stored": feat_same,
                             "direction_check": {"n": len(dsess), "hard_longer": hard_longer,
                                                 "easy_longer": easy_longer, "tie": tie,
                                                 "mean_ntok_easy": mean(tokP), "mean_ntok_hard": mean(tokQ),
                                                 "pool_task_chars_mean": task_len}}

    # ---------------------------------------------------- 3b. FDBK stream --
    LOC_FDBK_VERDICT = loc(ARCH, "274 delivered verdicts, 93.4%", "Correct — predominantly positive")   # round-2 finding 6: :106-107
    LOC_FDBK_POST = loc(ARCH, "**FDBK line:** P(first choice = verdict config) = 23/44", "93.4%-positive delivered stream")
    fd_rounds = [(r, i, rd) for r in rows if r["arm"] == "FDBK" for i, rd in enumerate(r["rounds"])]
    delivered = [(r, i, rd) for (r, i, rd) in fd_rounds if rd["verdict"]]
    n_corr = sum(1 for (_, _, rd) in delivered if rd["graded"])
    only_P = all(rd["cfg"] == "P" for (_, _, rd) in delivered) and all(rd["verdict"] for (_, _, rd) in fd_rounds if rd["cfg"] == "P")
    res_lines = collections.Counter()
    echo = 0
    for r in rows:
        if r["arm"] != "FDBK":
            continue
        for l in r["transcript"].split("\n"):
            if l.startswith("Result: "):
                res_lines[l] += 1
            elif "Result:" in l:
                echo += 1
    nonfd_res = sum(1 for r in rows if r["arm"] != "FDBK" for l in r["transcript"].split("\n") if l.startswith("Result: "))
    # pre-pick (forced) verdicts in the primary's domain
    vf = [r for r in valid if r["arm"] == "FDBK"]
    pre = [rd for r in vf for rd in r["rounds"][:4] if rd["verdict"]]
    pre_c = sum(1 for rd in pre if rd["graded"])
    all_correct_prepick = sum(1 for r in vf if all(rd["graded"] for rd in r["rounds"][:4] if rd["verdict"]))
    L += ["### 3b. FDBK: the delivered verdict stream", "",
          f"- Delivered verdict lines (harness-written `Result: Correct.`/`Result: Incorrect.` after every FDBK P-config round, f_sessions.py {ports['FDBK verdict line (in run_round)'].rsplit(':', 1)[1]}): {len(delivered)} over all {by_arm['FDBK']} FDBK sessions including excluded ones (every P round generated); Correct {n_corr}/{len(delivered)} = {n_corr / len(delivered):.4f}. Verdicts only on P rounds and on every P round: {only_P}.",
          f"- Cross-check on the transcripts: lines beginning `Result: ` -- {dict(res_lines)} (sum {sum(res_lines.values())}); none outside FDBK ({nonfd_res}). {echo} FDBK response lines contain the string `Result:` inside the model's own text (echoes of the verdict format, not verdicts).",
          f"- Pre-pick stream (computed-new, descriptive): in the {len(vf)} valid FDBK sessions the forced phase delivered {len(pre)} verdicts (two per session), {pre_c} Correct ({pre_c / len(pre):.4f}); {all_correct_prepick} of {len(vf)} sessions saw two Correct verdicts before the first choice.",
          f"- Primary (FDBK first free choice to the verdict config): {fb['k']}/{fb['n']} = {fb['k'] / fb['n']:.4f} (postscreen `fdbk_line` {post['fdbk_line']}).",
          f"- Record: the verdict entry's '274 delivered verdicts, 93.4% Correct' ({LOC_FDBK_VERDICT}); the post-screen entry's FDBK line '23/44 = .523 against a 93.4%-positive delivered stream' ({LOC_FDBK_POST}).",
          ""]
    assert post["fdbk_line"] == {"k": fb["k"], "n": fb["n"]}
    assert sum(res_lines.values()) == len(delivered) and res_lines["Result: Correct."] == n_corr
    fig("FDBK 93% positive delivery rate", f"{n_corr}/{len(delivered)} = {100 * n_corr / len(delivered):.1f}% Correct",
        "data/f/sessions.jsonl rounds[].verdict, rounds[].graded (arm FDBK); transcripts' Result: lines", "reproduced",
        "domain: every delivered verdict line, all 56 FDBK sessions incl. excluded (P rounds only). Record: '274 delivered verdicts, 93.4% Correct' " + LOC_FDBK_VERDICT + "; post-screen '93.4%-positive' " + LOC_FDBK_POST + ". The record's 93.4% is hard-coded text in the post-screen analyzer (" + loc(F_POST, "delivered-verdict composition 93.4%", where="clone") + "), not computed there; the G-PORT differences raw reports a values-check reproduction from `graded` (" + loc("results/raw/2026-10-07_m-gport_differences.md", "FDBK's composition 93.4% correct") + "); computed here from the JSONL. Pre-pick, valid sessions: " + f"{pre_c}/{len(pre)}")
    J["fdbk_stream"] = {"delivered": len(delivered), "correct": n_corr,
                        "transcript_result_lines": dict(res_lines),
                        "model_echoes_of_Result": echo,
                        "prepick_valid": {"sessions": len(vf), "verdicts": len(pre), "correct": pre_c,
                                          "sessions_all_correct": all_correct_prepick}}

    # ------------------------------------------------ 4. termination table --
    term_rx = json.loads(term_b)["term_regex"]
    agree = disagree = 0
    per_arm_t = collections.Counter()
    per_arm_n = collections.Counter()
    per_cell = collections.Counter()
    per_key = collections.Counter()
    for r in rows:
        texts = [l[len("Response:"):] for l in r["transcript"].split("\n") if l.startswith("Response:")]
        assert len(texts) == r["n_rounds"] == len(r["rounds"])
        for pos, (t, rd) in enumerate(zip(texts, r["rounds"])):
            hit = None
            for rx in term_rx:
                if re.search(rx, t):
                    hit = rx
                    break
            if hit == rd["term"]:
                agree += 1
            else:
                disagree += 1
            per_arm_n[r["arm"]] += 1
            if hit:
                per_arm_t[r["arm"]] += 1
                per_cell[(r["arm"], rd["cfg"])] += 1
                per_key[(r["arm"], rd["cfg"], pos)] += 1
    sess_t = [r for r in rows if any(rd["term"] for rd in r["rounds"])]
    n_sess_t = len(sess_t)
    n_sess_t_exc = sum(1 for r in sess_t if r["excluded"])
    an_raw = pinned_text("results/raw/2026-08-10_f_analysis.txt")
    tline = [l for l in an_raw.split("\n") if l.startswith("termination attempts")][0]
    rec_dict = ast.literal_eval(tline.split(": ", 1)[1])
    dict_equal = dict(per_key) == rec_dict
    tot_t, tot_n = sum(per_arm_t.values()), sum(per_arm_n.values())
    # post-hoc exact conditional test of homogeneity across the six arms
    # (6x2 table, margins fixed: multivariate hypergeometric; Freeman-Halton
    # ordering by table probability)
    ns = [per_arm_n[a] for a in ARMS]
    ks = [per_arm_t[a] for a in ARMS]
    combs = [[math.comb(n, k) for k in range(tot_t + 1)] for n in ns]
    obs = 1
    for a_i, k in enumerate(ks):
        obs *= combs[a_i][k]
    acc_le = 0
    n_tables = 0

    def rec(i, left, prod):
        nonlocal acc_le, n_tables
        if i == len(ns) - 1:
            if left <= ns[i]:
                pr = prod * combs[i][left]
                n_tables += 1
                if pr <= obs:
                    acc_le += pr
            return
        for k in range(0, min(left, ns[i]) + 1):
            rec(i + 1, left - k, prod * combs[i][k])
    rec(0, tot_t, 1)
    p_hom = acc_le / math.comb(tot_n, tot_t)
    # values-check finding 4: the verdict entry's figure spans :97-98 (the
    # numeral 33 ends :97); sham (7) and NOV-Q 3 vs NOV-P 3 are on :99;
    # FINDINGS-4's '33 attempts, ~1.0% of rounds' spans :82-83
    LOC_T33 = loc(ARCH, 'Termination table (required; pre-declared counter)', 'attempts ≈ 1.0% of rounds')
    LOC_TSHAM = loc(ARCH, 'NOV-Q total 3 vs NOV-P 3')
    LOC_T33_F4 = loc('FINDINGS-4.md', '33 attempts', '~1.0% of rounds')
    LOC_ANRAW = loc('results/raw/2026-08-10_f_analysis.txt', 'termination attempts')
    pp_term = f"{PREPRINT}:{pp_n('session-termination attempts occur at about 1% of rounds')}"
    rates = {a: per_arm_t[a] / per_arm_n[a] for a in ARMS}
    sham_vs_overall = rates["sham"] / (tot_t / tot_n)
    # Round 10 (fix round): the statements of §4 and its rows about the preprint's termination wording
    _uni_c = CLAIMS9["uniform"]
    _l7t = l7of(_term_nd)
    _ndh7 = "says 'no detectable heterogeneity'" if "no detectable heterogeneity" in _l7t else "drops 'uniformly across arms'"
    _byarm7 = ("gives the by-arm range instead" if re.search(r"\d–\d+(?:\.\d+)?% by arm", _l7t)
               else "drops it")
    term_s4_stmt = rw10(
        "§4 (the post-hoc homogeneity bullet)", _uni_c[0], _uni_c[1], _uni_c[2],
        f"It bears on the preprint's 'uniformly across arms' ({pp_term}, working tree): the counts show no detectable heterogeneity, which is weaker than 'uniformly'.",
        lambda by: (f"It bore on the audited and v6 preprint's 'uniformly across arms' ({pp_term}): the counts show no "
                    f"detectable heterogeneity, which is weaker than 'uniformly'; v7 {_ndh7} (Round 10, {by})."))
    term_byarm_stmt = rw10(
        "the by-arm termination row's note", "phrase 'uniformly across arms' on its anchor line", _term_nd,
        lambda t: "uniformly across arms" in t,
        "the preprint's 'uniformly across arms' (" + pp_term + ", working tree)",
        lambda by: ("the 'uniformly across arms' of the audited text and of the patched text that preceded the preprint of record (" + pp_term + "; the preprint of "
                    "record " + _byarm7 + ": a finding on the patch, closing sections)"), row=True)
    _lab_hom = "uniformly across arms including sham"
    term_hom_src = rw10(
        "the homogeneity row's source", f"phrase '{_lab_hom}' (the row's label) on its anchor line", _term_nd,
        lambda t: _lab_hom in t,
        "computed from data/f/sessions.jsonl; preprint " + pp_term,
        lambda by: ("computed from data/f/sessions.jsonl; preprint " + pp_term + " (the wording of the audited text "
                    "and of the patched text that preceded the preprint of record; the preprint of record rewords it: closing sections)"), row=True)
    term_hom_note = rw10(
        "the homogeneity row's note", _uni_c[0], _uni_c[1], _uni_c[2],
        "not a record computation; rounds treated as exchangeable (clustering ignored); supports 'no detectable heterogeneity', which is weaker than 'uniformly'",
        lambda by: ("not a record computation; rounds treated as exchangeable (clustering ignored); supports 'no "
                    "detectable heterogeneity', which is weaker than the 'uniformly' of the audited text and of the patched text that preceded the preprint of record; "
                    "the preprint of record " + _ndh7 + " (a finding on the patch; closing sections)"), row=True)
    L += ["## 4. Termination attempts by arm (pre-declared descriptive counter)", "",
          f"Applied as the record applied it ({ports['termination counter (in run_round)']}): for every generated round of every session INCLUDING excluded ones, the round's text (the generation, `.strip()`-ed, recovered here from its `Response:` line) is searched with the four regexes of `data/configs/f_termination_patterns.json` in order, case-sensitive `re.search`, first match counted; tabulated per arm × config × round position. Denominator: rounds generated (the record's cap-hit denominator, {tot_n}).",
          "",
          f"- Recomputed matches equal the stored `rounds[].term` field on {agree} of {agree + disagree} rounds (disagreements: {disagree}); the (arm, config, round-position) table equals the analysis raw's dict ({LOC_ANRAW}): {dict_equal}.",
          f"- Total: **{tot_t} attempts** / {tot_n} rounds = {100 * tot_t / tot_n:.2f}%, in {n_sess_t} sessions ({n_sess_t_exc} of them excluded sessions). The analysis raw's dict has **{len(rec_dict)} keys** (distinct arm × config × round-position cells) whose values sum to {sum(rec_dict.values())}. The verdict entry's '33 attempts ≈ 1.0% of rounds' ({LOC_T33}) and FINDINGS-4's '33 attempts, ~1.0% of rounds' ({LOC_T33_F4}) equal the number of cells, not the number of attempts: **discrepant; by inference a transcription (the dict's length read as the count -- 33 matches it exactly)**. The true figure is {tot_t} ({100 * tot_t / tot_n:.2f}% of rounds); the per-arm and per-config figures the entry quotes (sham 7; NOV-Q 3 vs NOV-P 3) are attempt counts and reproduce.",
          "",
          "| arm | attempts / rounds generated | rate | P-config | Q-config |",
          "|---|---|---|---|---|"]
    for a in ARMS:
        L.append(f"| {a} | {per_arm_t[a]}/{per_arm_n[a]} | {100 * per_arm_t[a] / per_arm_n[a]:.2f}% | {per_cell[(a, 'P')]} | {per_cell[(a, 'Q')]} |")
    L += ["", f"- (sham's P/Q are its two labels, property-identical.) NOV-Q {per_cell[('NOV', 'Q')]} vs NOV-P {per_cell[('NOV', 'P')]}; sham {per_arm_t['sham']} -- as the verdict entry states ({LOC_TSHAM}).",
          f"- By arm the rate runs {100 * min(rates.values()):.1f}%-{100 * max(rates.values()):.1f}%; sham's {per_arm_t['sham']}/{per_arm_n['sham']} = {100 * rates['sham']:.2f}% is the highest: about twice the record's stated '≈ 1.0%', and {sham_vs_overall:.2f}× the overall {100 * tot_t / tot_n:.2f}%. So '≈ 1% of rounds' is an overall figure, not a per-arm one.",
          f"- POST-HOC (Code's, computed-new; not in the record): exact conditional test of homogeneity of the per-arm attempt rate across the six arms (6×2 table, both margins fixed; multivariate hypergeometric over all {n_tables} tables; p = probability of tables no more probable than the observed one, Freeman-Halton form, two-sided by construction): p = {p_hom:.4f}. Rounds are clustered within sessions, so this treats rounds as exchangeable; descriptive only. {term_s4_stmt}",
          f"- Suggested wording for the note (a proposal for the design seat): 'about 1% of rounds overall ({tot_t}/{tot_n}; {100 * min(rates.values()):.1f}-{100 * max(rates.values()):.1f}% by arm, no detectable heterogeneity across arms, post-hoc exact p = {p_hom:.2f})'.",
          ""]
    assert disagree == 0 and dict_equal and sum(rec_dict.values()) == tot_t
    assert per_arm_t["sham"] == 7 and per_cell[("NOV", "Q")] == 3 and per_cell[("NOV", "P")] == 3
    # round-2 finding 3: the block's figure split into an overall row and a by-arm row
    # (the status vocabulary is fixed, so the qualifier goes in the note, not the status)
    _r5 = [rates[a] for a in CONTRASTS]
    assert rates["sham"] == max(rates.values()) and all(rates["sham"] > x for x in _r5)
    fig("termination attempts ≈ 1% of rounds (overall)",
        f"{tot_t}/{tot_n} = {100 * tot_t / tot_n:.2f}%",
        "data/f/sessions.jsonl (transcript Response lines; rounds[].term) + data/configs/f_termination_patterns.json", "reproduced",
        "domain: all generated rounds of all 344 sessions incl. excluded; the record's '≈ 1.0% of rounds' (" + LOC_T33 + ") is an overall rate and reproduces as one; the record's count (33) is wrong, separate discrepant row below; suggested wording in §4")
    fig("termination attempts ≈ 1% of rounds by arm",
        ", ".join(f"{a} {per_arm_t[a]}/{per_arm_n[a]} ({100 * per_arm_t[a] / per_arm_n[a]:.2f}%)" for a in ARMS),
        "data/f/sessions.jsonl (transcript Response lines; rounds[].term) + data/configs/f_termination_patterns.json", "discrepant",
        f"per arm the figure holds for the five contrast arms ({100 * min(_r5):.2f}%-{100 * max(_r5):.2f}%) but not for sham: {per_arm_t['sham']}/{per_arm_n['sham']} = {100 * rates['sham']:.2f}%, about 2%, twice the stated ≈ 1% ({sham_vs_overall:.2f}× the overall {100 * tot_t / tot_n:.2f}%). Not a transcription: the record states ≈ 1.0% overall (" + LOC_T33 + ") and gives sham's count (7, " + LOC_TSHAM + "), not a per-arm rate; the per-arm reading is the block's 'by arm' and " + term_byarm_stmt + ". No detectable heterogeneity across arms (post-hoc p = " + f"{p_hom:.2f}" + ", row below). Domain as in the overall row")
    fig("33 attempts ≈ 1.0% of rounds (verdict entry; FINDINGS-4)",
        f"{tot_t} attempts = {100 * tot_t / tot_n:.2f}% of {tot_n} rounds; 33 = the number of distinct (arm, config, round-position) cells in the analysis raw's table",
        "data/f/sessions.jsonl rounds[].term; " + LOC_ANRAW + f" (dict, values sum to {sum(rec_dict.values())})", "discrepant",
        "transcription, inferred: 33 equals the table's cell count exactly, consistent with its length having been read as the count; verdict entry " + LOC_T33 + "; FINDINGS-4 " + LOC_T33_F4 + f"; if the note carries a count it is {tot_t} ({100 * tot_t / tot_n:.1f}%)")
    fig("termination 'uniformly across arms including sham' (preprint wording)", f"post-hoc exact homogeneity test across six arms (6x2, Freeman-Halton, two-sided) p = {p_hom:.4f}",
        term_hom_src, "computed-new", term_hom_note)
    J["termination"] = {"total": tot_t, "rounds": tot_n, "agree_with_stored": agree,
                        "sessions_with_attempt": n_sess_t, "excluded_sessions_with_attempt": n_sess_t_exc,
                        "analysis_raw_dict_keys": len(rec_dict),
                        "analysis_raw_dict_sum": sum(rec_dict.values()),
                        "record_figure": "33 attempts ≈ 1.0% (= number of dict keys)",
                        "disagree": disagree, "table_equals_analysis_raw": dict_equal,
                        "per_arm": {a: [per_arm_t[a], per_arm_n[a]] for a in ARMS},
                        "per_arm_cfg": {f"{a}|{c}": per_cell[(a, c)] for a in ARMS for c in "PQ"},
                        "posthoc_homogeneity_p": p_hom, "n_tables": n_tables}

    # ------------------------------------------------ 5. exploration share --
    LOC_SHARE_F4 = loc('FINDINGS-4.md', 'Session share ≈ .50', 'in every arm (e2a')
    e2a_loc = loc(f"{CLONE}/scripts/e2a_sessions.py", 'share = float(np.mean([c[', where="clone")
    pp_main = pp_n('Menu behavior is exploration-dominant in every arm')
    L += ["## 5. Exploration share by arm (session share)", "",
          f"The record states 'Session share ≈ .50 in every arm' for f1 ({LOC_SHARE_F4}) with no f1 artifact field and no f1 analyzer line computing it (`screen_analysis.json` has no share; `analyze()` computes none). Code computes it under e2a's definition, the precedent the sentence cites ('e2a's alternation finding'): e2a's `share_all_choices` = share of ALL free picks, over valid sessions, on one fixed label ({e2a_loc}); here the fixed label is P. Alternation = share of consecutive free picks (pick j vs j+1) that switch config; break = first free pick differs from the last forced round's config.",
          "",
          "| arm | valid sessions | free picks | share to P | mean per-session share | alternation (switches / pairs) | first-pick break |",
          "|---|---|---|---|---|---|---|"]
    expl = {}
    for a in ARMS:
        vs = [r for r in valid if r["arm"] == a]
        picks = [c["picked_cfg"] == "P" for r in vs for c in r["choices"]]
        per = [mean([c["picked_cfg"] == "P" for c in r["choices"]]) for r in vs if r["choices"]]
        sw = pr = 0
        brk = nb = 0
        for r in vs:
            ch = r["choices"]
            for j in range(len(ch) - 1):
                pr += 1
                sw += int(ch[j]["picked_cfg"] != ch[j + 1]["picked_cfg"])
            if ch:
                nb += 1
                brk += int(ch[0]["picked_cfg"] != r["rounds"][3]["cfg"])
        # post-hoc session-level test (values-check finding 1)
        ks_ = [sum(c["picked_cfg"] == "P" for c in r["choices"]) for r in vs]
        ns_ = [len(r["choices"]) for r in vs]
        s_obs, m_nz, p_sf = signflip_two_sided([2 * k_ - n_ for k_, n_ in zip(ks_, ns_)])
        by_map_sh = {}
        for mflag, mname in ((False, "A"), (True, "B")):
            mm = [c["picked_cfg"] == "P" for r in vs if r["swap"] == mflag for c in r["choices"]]
            by_map_sh[mname] = [sum(mm), len(mm)]
        expl[a] = {"sessions": len(vs), "picks": len(picks), "share_P": sum(picks) / len(picks),
                   "k_P": sum(picks), "mean_session_share": mean(per),
                   "switches": sw, "pairs": pr, "break": brk, "n_break": nb,
                   "free_picks_per_session": sorted(set(ns_)),
                   "by_map_kn": by_map_sh,
                   "sessions_all_P": sum(1 for k_, n_ in zip(ks_, ns_) if k_ == n_),
                   "sessions_all_Q": sum(1 for k_ in ks_ if k_ == 0),
                   "sessions_at_half": sum(1 for k_, n_ in zip(ks_, ns_) if 2 * k_ == n_),
                   "posthoc_signflip": {"S": s_obs, "nonzero_sessions": m_nz, "p_two_sided": p_sf,
                                        "bonferroni6": min(1.0, 6 * p_sf)}}
        L.append(f"| {a} | {len(vs)} | {len(picks)} | {sum(picks)}/{len(picks)} = {sum(picks) / len(picks):.4f} | {mean(per):.4f} | {sw}/{pr} = {sw / pr:.3f} | {brk}/{nb} = {brk / nb:.3f} |")
    assert all(e["free_picks_per_session"] == [6] for e in expl.values())
    shares = {a: expl[a]["share_P"] for a in ARMS}
    lo_a, hi_a = min(shares, key=shares.get), max(shares, key=shares.get)
    fx = expl["FDBK"]
    # round-2 finding 4: 'largest deviation', not 'exception' -- assert it is the largest
    assert max(ARMS, key=lambda a: abs(shares[a] - 0.5)) == "FDBK"
    assert min(ARMS, key=lambda a: expl[a]["posthoc_signflip"]["p_two_sided"]) == "FDBK"
    others_min_p = min(expl[a]["posthoc_signflip"]["p_two_sided"] for a in ARMS if a != "FDBK")
    L += ["",
          f"- The all-picks share runs {shares[lo_a]:.3f} ({lo_a}) to {shares[hi_a]:.3f} ({hi_a}) by arm. 'Consistent with ≈ .50 in every arm' is NOT claimed here (v1 of this raw did, without a test; values-check finding 1).",
          "",
          "POST-HOC (computed here at the values-check's suggestion; not in the record; no verdict weight). Every valid session has exactly 6 free picks. Per session, deviation = 2k − 6 (k = free picks to P); exact two-sided sign-flip (Fisher-Pitman one-sample) test with sessions as the units, ties at 3/6 dropped; uncorrected p and a six-arm Bonferroni bound min(1, 6p). Maps: A = swap False, B = swap True.",
          "",
          "| arm | share to P, map A | share to P, map B | sessions 6/6 to P | sessions 0/6 to P | sessions at 3/6 (dropped) | S (sum of 2k−6) | p, two-sided (uncorrected) | Bonferroni ×6 |",
          "|---|---|---|---|---|---|---|---|---|"]
    for a in ARMS:
        e = expl[a]
        (ak, an), (bk, bn) = e["by_map_kn"]["A"], e["by_map_kn"]["B"]
        sf = e["posthoc_signflip"]
        L.append(f"| {a} | {ak}/{an} = {ak / an:.3f} | {bk}/{bn} = {bk / bn:.3f} | {e['sessions_all_P']} | {e['sessions_all_Q']} | {e['sessions_at_half']} | {sf['S']:+d} over {sf['nonzero_sessions']} | {sf['p_two_sided']:.4f} | {sf['bonferroni6']:.3f} |")
    (fak, fan), (fbk, fbn) = fx["by_map_kn"]["A"], fx["by_map_kn"]["B"]
    # Round 10 (fix round): the statements of §5 and Note 3 about the preprint's menu sentence
    _sh_c, _fc_c = CLAIMS9["share"], CLAIMS9["first"]
    _l7m = l7of(_menu_nd)
    _sh7 = "gives the range" if re.search(r"session share \.\d+–\.\d+", _l7m) else "restates it"
    _fc7 = "says 'at the first choice'" if "at the first choice" in _l7m else "restates it"
    share_s5_stmt = rw10(
        "§5 (the bearing bullet), first clause", _sh_c[0], _sh_c[1], _sh_c[2],
        f"the preprint's 'session share ≈ .50' in every arm ({PREPRINT}:{pp_main}) should give the range ({shares[lo_a]:.2f}-{shares[hi_a]:.2f}) or name FDBK's {fx['share_P']:.2f}",
        lambda by: (f"the audited and v6 preprint's 'session share ≈ .50' in every arm ({PREPRINT}:{pp_main}) should have "
                    f"given the range ({shares[lo_a]:.2f}-{shares[hi_a]:.2f}) or named FDBK's {fx['share_P']:.2f}; v7 "
                    f"{_sh7} (Round 10, {by})"))
    first_s5_stmt = rw10(
        "§5 (the bearing bullet), second clause", _fc_c[0], _fc_c[1], _fc_c[2],
        "its 'no evaluation-seeking against a predominantly positive feedback stream' (same line) is a first-choice statement and should say so",
        lambda by: (f"the audited and v6 texts' 'no evaluation-seeking against a predominantly positive feedback stream' "
                    f"(same line) was a first-choice statement that did not say so; v7 {_fc7} (Round 10, {by})"))
    L += ["",
          f"- FDBK shows the largest deviation from .50 ({fx['share_P']:.3f}, both maps; post-hoc p = {fx['posthoc_signflip']['p_two_sided']:.3f} uncorrected, {fx['posthoc_signflip']['bonferroni6']:.2f} Bonferroni ×6): {fx['k_P']}/{fx['picks']} free picks went to the verdict config, both maps leaning the same way (A {fak}/{fan} = {fak / fan:.3f}, B {fbk}/{fbn} = {fbk / fbn:.3f}); {fx['sessions_all_P']} of {fx['sessions']} valid sessions put all six free picks on the verdict config ({fx['sessions_all_Q']} put all six on the other). After the correction it is not significant, so it is the largest deviation, not an established exception. Every other arm has p ≥ {others_min_p:.2f} and |share − ½| ≤ {max(abs(shares[a] - 0.5) for a in ARMS if a != 'FDBK'):.3f}.",
          f"- Scope: a verdict line follows every FDBK P round, free rounds included (§3b), so the all-picks share includes picks made after free-phase verdicts were delivered; the first free choice -- the pre-registered primary, {fb['k']}/{fb['n']}, one-sided p = {fb['p_exact']:.2f} -- is the only free pick made before any free-phase verdict. The primary is untouched.",
          f"- Bearing on the note (a proposal for the design seat; the PI and the design seat decide): {share_s5_stmt}; {first_s5_stmt}.",
          ""]
    fig("exploration share ≈ .50 by arm",
        ", ".join(f"{a} {expl[a]['share_P']:.3f}" for a in ARMS) + f" (share of all free picks to P, valid sessions); range {shares[lo_a]:.3f}-{shares[hi_a]:.3f}",
        "computed from data/f/sessions.jsonl choices[].picked_cfg; record prose " + LOC_SHARE_F4,
        "computed-new", f"the record's figure is prose with no committed f1 computation; definition = e2a's share_all_choices with P as the pole; FDBK shows the largest deviation from .50 (post-hoc p = {fx['posthoc_signflip']['p_two_sided']:.3f} uncorrected, {fx['posthoc_signflip']['bonferroni6']:.2f} Bonferroni ×6; next row), not an established exception; give the range or name FDBK")
    fig("FDBK all-picks share toward the verdict config (POST-HOC)",
        f"{fx['k_P']}/{fx['picks']} = {fx['share_P']:.3f}; maps A {fak / fan:.3f}, B {fbk / fbn:.3f}; {fx['sessions_all_P']}/{fx['sessions']} sessions 6/6 to verdict config; exact two-sided sign-flip over sessions p = {fx['posthoc_signflip']['p_two_sided']:.4f} uncorrected, Bonferroni ×6 {fx['posthoc_signflip']['bonferroni6']:.3f}; other arms p ≥ {others_min_p:.3f}",
        "computed from data/f/sessions.jsonl choices[].picked_cfg, swap (valid FDBK sessions)", "computed-new",
        "post-hoc, descriptive, no verdict weight; includes picks made after free-phase verdicts; the pre-registered first-choice primary (23/44, p = .44) is untouched")
    J["exploration"] = expl

    # ------------------------------------------------------- 6. calibration --
    acc = calib["acc"]
    n_items = len(json.loads(pools_b)["DIFF_easy"])
    nper = calib["n_seeds"] * n_items
    e_h = acc["DIFF_easy"] * nper
    h_h = acc["DIFF_hard"] * nper
    c1 = pinned_text("results/raw/2026-08-10_f_calib.txt")
    # values-check findings 5 and 6: precise line locators
    LOC_094 = loc(ARCH, 'calibration accuracy delta (+.094)')
    LOC_838 = loc(ARCH, 'in-session (P .838 vs Q .833)')
    LOC_883 = loc(ARCH, 'DIFF in-session gap .883/.592')
    LOC_078 = loc(ARCH, 'CORR delta +.078 covariate')
    LOC_094_V1 = loc(ARCH, 'corrupted .875 (delta +.094')
    L += ["## 6. Calibrated accuracies (f0) and the in-session accuracies", "",
          f"- `data/f/calib.json` (f0 v2, pools `{calib['pools_sha']}` = the run's pools): DIFF easy {acc['DIFF_easy']} = {e_h:.0f}/{nper}, DIFF hard {acc['DIFF_hard']} = {h_h:.0f}/{nper} ({calib['n_seeds']} seeds × {n_items} items per pool), gap {acc['DIFF_easy'] - acc['DIFF_hard']:.4f}; bars {calib['bars']['DIFF_easy_acc']}, {calib['bars']['DIFF_hard_acc']}, {calib['bars']['DIFF_gap']} (DIFF bar: easy ≥ .90, hard ≤ .50, gap ≥ .40 -- {loc('PROPOSAL-f-natural-reinforcer-screen.md', '| 2 | DIFF |')}; hard sits exactly at the .50 ceiling). Raw: {loc('results/raw/2026-08-10_f_calib2.txt', 'DIFF_easy: accuracy')}.",
          f"- Superseded f0 v1 (pools `61d392250b27c760`, replaced before any screen session): DIFF {line_at('results/raw/2026-08-10_f_calib.txt', 'DIFF_easy: accuracy')} / {line_at('results/raw/2026-08-10_f_calib.txt', 'DIFF_hard: accuracy')}; CORR `{line_at('results/raw/2026-08-10_f_calib.txt', 'CORR delta')}` ({loc('results/raw/2026-08-10_f_calib.txt', 'CORR delta')}).",
          f"- CORR covariate of record: calib.json `CORR_delta_covariate` = {calib['CORR_delta_covariate']} (= clean {acc['CORR_clean']} − corrupted {acc['CORR_corrupted']}, i.e. {acc['CORR_clean'] * nper:.0f}/{nper} − {acc['CORR_corrupted'] * nper:.0f}/{nper}; +.078). The cycle-4 record itself logs +.078 for the run's pools in the f0 v2 entry ('CORR delta +.078 covariate', {LOC_078}); the verdict entry's CORR note quotes the superseded v1 value: `{line_at(ARCH, 'calibration accuracy delta (+.094)')}` ({LOC_094}), the figure the f0 v1 entry logged ({LOC_094_V1}). PROPOSAL-m quotes +.078 as the 0.12 figure of record ({loc('PROPOSAL-m-gating-campaign-v1_11.md', 'its 0.12 figure of record is +.078')}).",
          ""]
    assert abs(e_h - round(e_h)) < 1e-9 and abs(h_h - round(h_h)) < 1e-9
    fig("calibrated accuracies .98/.50 for DIFF (calib.json)", f"easy {acc['DIFF_easy']} ({e_h:.0f}/{nper}), hard {acc['DIFF_hard']} ({h_h:.0f}/{nper})",
        "data/f/calib.json acc.DIFF_easy, acc.DIFF_hard", "reproduced", "f0 v2 on the run's pools (8547d9a1); v1's .953/.500 was on superseded pools")
    fig("CORR calibration delta in the verdict entry (+.094)", f"calib.json CORR_delta_covariate = {calib['CORR_delta_covariate']} (+.078); +.094 is f0 v1 on the superseded pools",
        "data/f/calib.json CORR_delta_covariate; v1: " + loc('results/raw/2026-08-10_f_calib.txt', 'CORR delta'), "discrepant",
        "transcription of the superseded v1 figure into the verdict entry (" + LOC_094 + "; v1 logged at " + LOC_094_V1 + "); the record's own f0 v2 entry carries +.078 for the run's pools (" + LOC_078 + "); the note should carry +.078 if it carries the covariate; the 'vanished in-session' reading is unchanged")
    # in-session accuracy
    ins = collections.defaultdict(lambda: [0, 0])
    for r in rows:
        for rd in r["rounds"]:
            if rd["graded"] is not None:
                ins[(r["arm"], rd["cfg"])][0] += int(rd["graded"])
                ins[(r["arm"], rd["cfg"])][1] += 1
    cp, cq = ins[("CORR", "P")], ins[("CORR", "Q")]
    dp, dq = ins[("DIFF", "P")], ins[("DIFF", "Q")]
    L += [f"- In-session accuracy (f1's own grader, stored `rounds[].graded`; domain: every generated round of every session incl. excluded): CORR clean (P) {cp[0]}/{cp[1]} = {cp[0] / cp[1]:.4f}, corrupted (Q) {cq[0]}/{cq[1]} = {cq[0] / cq[1]:.4f} (difference {cp[0] / cp[1] - cq[0] / cq[1]:+.4f}); DIFF easy {dp[0]}/{dp[1]} = {dp[0] / dp[1]:.4f}, hard {dq[0]}/{dq[1]} = {dq[0] / dq[1]:.4f}. Record: P .838 vs Q .833 at {LOC_838}; DIFF .883/.592 at {LOC_883}.",
          ""]
    fig("CORR in-session accuracy P .838 vs Q .833 (verdict entry)", f"{cp[0]}/{cp[1]} = {cp[0] / cp[1]:.3f} vs {cq[0]}/{cq[1]} = {cq[0] / cq[1]:.3f}",
        "data/f/sessions.jsonl rounds[].graded (arm CORR)", "reproduced", "all generated CORR rounds incl. excluded sessions; record " + LOC_838)
    fig("DIFF in-session gap .883/.592 (verdict entry)", f"{dp[0]}/{dp[1]} = {dp[0] / dp[1]:.3f} vs {dq[0]}/{dq[1]} = {dq[0] / dq[1]:.3f}",
        "data/f/sessions.jsonl rounds[].graded (arm DIFF)", "reproduced", "all generated DIFF rounds incl. excluded sessions; record " + LOC_883)
    J["calibration"] = {"calib": calib, "nper": nper,
                        "in_session": {f"{a}|{c}": ins[(a, c)] for (a, c) in sorted(ins)}}

    # ----------------------------------------------- 7. the CORR dose caveat --
    pools = json.loads(pools_b)
    clean = [it["task"] for it in pools["CORR_clean"]]
    # (a) transcript-derived, no corruptor code: identify each CORR round's item
    q_rounds = []    # (session row, round pos, item idx, changed, phase)
    p_ok = True
    for r in rows:
        if r["arm"] != "CORR":
            continue
        lines = r["transcript"].split("\n")
        tasks = [l[len("Task: "):] for l in lines if l.startswith("Task: ")]
        assert len(tasks) == len(r["rounds"])
        for pos, (t, rd) in enumerate(zip(tasks, r["rounds"])):
            assert t[:40] == rd["task"]
            if rd["cfg"] == "P":
                p_ok &= t in clean
                continue
            cands = [(hamming(t, c), i) for i, c in enumerate(clean) if len(c) == len(t)]
            cands.sort()
            assert cands and (len(cands) == 1 or cands[0][0] < cands[1][0]), "ambiguous item"
            q_rounds.append((r, pos, cands[0][1], cands[0][0], "forced" if pos < 4 else "free"))
    per_item = {}
    for (_, _, i, ch, _) in q_rounds:
        per_item.setdefault(i, set()).add(ch)
    assert all(len(v) == 1 for v in per_item.values())   # deterministic per item
    changed_t = [next(iter(per_item[i])) if i in per_item else None for i in range(16)]
    # (b) replay of f1's corrupt() at 0.12, validated by the calib sha
    renders, draws = zip(*[corrupt_f1(t, i) for i, t in enumerate(clean)])
    rsha = sha256_bytes("\n".join(renders).encode())[:16]
    changed_r = [hamming(a, b) for a, b in zip(renders, clean)]
    replay_eq = all(changed_t[i] is None or changed_t[i] == changed_r[i] for i in range(16))
    zero_items = [i for i in range(16) if changed_r[i] == 0]
    ge3 = [i for i in range(16) if changed_r[i] >= 3]
    n_q = len(q_rounds)
    clean_q = [q for q in q_rounds if q[3] == 0]
    f_q = [q for q in q_rounds if q[4] == "forced"]
    fr_q = [q for q in q_rounds if q[4] == "free"]
    clean_f = [q for q in f_q if q[3] == 0]
    clean_fr = [q for q in fr_q if q[3] == 0]
    by_item_clean = collections.Counter(q[2] for q in clean_q)
    # sessions reaching the first read: those with >= 1 choice
    corr_rows = [r for r in rows if r["arm"] == "CORR"]
    reached = [r for r in corr_rows if r["choices"]]
    clean_pre = collections.Counter()
    for r in reached:
        n_clean = sum(1 for q in q_rounds if q[0] is r and q[4] == "forced" and q[3] == 0)
        nq = sum(1 for q in q_rounds if q[0] is r and q[4] == "forced")
        assert nq == 2
        clean_pre[n_clean] += 1
    reached_valid = [r for r in reached if not r["excluded"]]
    one_clean_valid = [r for r in reached_valid
                       if sum(1 for q in q_rounds if q[0] is r and q[4] == "forced" and q[3] == 0) == 1]
    both_corr_valid = [r for r in reached_valid if r not in one_clean_valid]
    k1 = sum(1 for r in one_clean_valid if r["first_free_pick_P"])
    k2 = sum(1 for r in both_corr_valid if r["first_free_pick_P"])
    kr = sum(1 for r in reached if r["first_free_pick_P"])
    # Q accuracy split by delivered text
    qa_clean = [q[0]["rounds"][q[1]]["graded"] for q in clean_q]
    qa_corr = [q[0]["rounds"][q[1]]["graded"] for q in q_rounds if q[3] > 0]
    # post-pin G-CAL model-free artifact (comparison only; counts, no text)
    after_pin = git_rc("merge-base", "--is-ancestor", PIN, POST_PIN_GCAL) == 0
    gcal = pinned_json("data/m/gates/G-CAL_model-free.json", POST_PIN_GCAL)["f1_012"]
    gcal_items = [it["changed"] for it in gcal["items"]]
    gcal_eq = (gcal["n_changed"] == sum(changed_r) and gcal["n_cond1"] == len(ge3)
               and gcal_items == changed_r and gcal["n_hits"] == sum(draws)
               and gcal["renders_sha16"] == rsha)
    LOC_CORRNOTE = loc(ARCH, 'calibration accuracy delta (+.094)', 'interpretation. DIFF in-session gap')
    LOC_VISIBLE = loc(ARCH, 'calibration accuracy delta (+.094) VANISHED', 'visible but performatively costless')
    LOC_F4_LOOSE = loc('FINDINGS-4.md', 'Loose ends, logged without weight')
    LOC_F4_VISIBLE = loc('FINDINGS-4.md', '.838/.833')
    LOC_G6A11 = loc('results/raw/2026-10-04_m-v1.7_referent_check.txt', '[G6a.11]  CHECKER', 'belongs to whichever group checks root lines.')
    # round-2 finding 2: the checker's own sentence that the computation supports the substance
    LOC_G6A11_SUBST = loc('results/raw/2026-10-04_m-v1.7_referent_check.txt', "the computation supports the note's substance", "states 'found' ahead of its record")
    LOC_V17_REPLAY = loc('results/raw/2026-10-04_m-v1.7_referent_check.txt', 'For the 31 I replayed f1', 'preprint' + chr(39) + 's dose note rests on (G6a.11)')
    LOC_C1 = loc('RESULTS.md', 'C1, under (3).', 'This bears on A0' + chr(39) + 's comparison with f1' + chr(39) + 's primary.')
    # round-2 finding 6: G-PORT A1's 30/58 is on :82 (the entry starts :80)
    LOC_A1 = loc('RESULTS.md', 'A1. **The primary' + chr(39) + 's domain.**', 'to 30/58 (Δ +.017)')
    # round-2 finding 5: the smoke read 'corrupted tasks render correctly' is the FIRST f1 smoke,
    # which ran on the v1 pools (pre-recast); evidence: its CORR Task lines vs the v2 pools
    LOC_SMOKE_READ = loc(ARCH, 'corrupted tasks render correctly')
    LOC_SMOKE1 = loc(ARCH, 'f1 smoke — PAUSED under the inherited')
    LOC_RECAST = loc(ARCH, '**(1) Pool rephrasing (mechanism 1):** all QA-style items recast')
    LOC_AMEND = loc(ARCH, 'f1 smoke ADJUDICATION — pre-data amendment')
    n_pools_versions = len([l for l in git("log", "--format=%h", PIN, "--", "data/f/pools.json").decode().split("\n") if l.strip()])
    LOC_V1_SHAS = loc(ARCH, 'Pools sha `61d392250b27c760`; corrupted-pool sha', '`12907bcf1df07668` (deterministic')
    LOC_V2_SHAS = loc(ARCH, '`results/raw/2026-08-10_f_{calib2,smoke2}.txt`; pools v2 sha', 'corrupted sha `2c2c227395ea9f2d`')
    _smoke_bad = int(LOC_SMOKE_READ.rsplit(":", 1)[1])
    assert int(LOC_SMOKE1.rsplit(":", 1)[1]) < _smoke_bad < int(LOC_SMOKE1.rsplit(":", 1)[1]) + 45
    assert int(LOC_AMEND.rsplit(":", 1)[1]) < int(LOC_RECAST.rsplit(":", 1)[1]) < int(LOC_SMOKE1.rsplit(":", 1)[1])   # newest-first: the recast is later
    _v2set = {it["task"] for k_, v_ in pools.items() if isinstance(v_, list) for it in v_ if isinstance(it, dict) and "task" in it}
    smoke_corr = {}
    for r in smoke:
        if r["arm"] != "CORR":
            continue
        blk_ = "first smoke (1000-series)" if r["session"] < 1100 else "later smokes (1100-series)"
        ts = [l[len("Task: "):] for l in r["transcript"].split("\n") if l.startswith("Task: ")]
        e_ = smoke_corr.setdefault(blk_, {"sessions": 0, "task_lines": 0, "verbatim_in_v2_pools": 0,
                                          "q_rounds_within_6_letters_of_a_v2_clean_item": 0, "q_rounds": 0,
                                          "start_What_is": 0})
        e_["sessions"] += 1
        e_["task_lines"] += len(ts)
        e_["verbatim_in_v2_pools"] += sum(t in _v2set for t in ts)
        e_["start_What_is"] += sum(t.startswith("What is") for t in ts)
        for t, rd in zip(ts, r["rounds"]):
            if rd["cfg"] == "Q":
                e_["q_rounds"] += 1
                e_["q_rounds_within_6_letters_of_a_v2_clean_item"] += int(any(len(c) == len(t) and hamming(t, c) <= 6 for c in clean))
    _s1 = smoke_corr["first smoke (1000-series)"]
    assert _s1["verbatim_in_v2_pools"] == 0 and smoke_corr["later smokes (1100-series)"]["verbatim_in_v2_pools"] > 0
    pp_dose = f"{PREPRINT}:{pp_n('found below its visibility criterion')}"
    pp_81 = f"{PREPRINT}:{pp_n('**8.1 The gating campaign')}"
    # round 9: v3's claim (iii) -- the dose clause omits the byte-clean delivery --
    # checked on the patched text; where it fails, §7d and the dose row say so and
    # the Round 9 section records the change as a finding on the patch (no digits
    # are added to the row's value or note: N1 reads figures from them)
    def omits_byteclean(line: str) -> bool:
        return f"{len(clean_q)} of {n_q}" not in line and "byte-clean" not in line
    _dl = pp_n('found below its visibility criterion')
    pp_carries_bc = isinstance(_dl, int) and not omits_byteclean(pp_lines[_dl - 1])
    pp_iii = ("(iii) It omits the byte-clean delivery, the concrete consequence for the primary." if not pp_carries_bc else
              f"(iii) The audited text (d6431e97…222b8) omitted the byte-clean delivery, the concrete consequence for the primary; the patched text carries it ({pp_dose}; Round 9: a finding on the patch).")
    pp_bc_value = ("the byte-clean delivery is omitted" if not pp_carries_bc else
                   "the byte-clean delivery, omitted in the audited text, is carried by the patched text (a finding on the patch; closing section)")
    pp_bc_note = ("the clause omits the byte-clean delivery" if not pp_carries_bc else
                  "the audited clause omitted the byte-clean delivery, which the patched text carries (a finding on the patch; closing section)")
    gcal_at_pin = git("rev-parse", "--verify", "-q", f"{PIN}:data/m/gates/G-CAL_model-free.json", rev_ok=True).decode().strip()
    # Round 10 (fix round): the statements of §7d, the dose row and Note 1 about the preprint's CORR dose clause
    _dq = "at a dose a later calibration (§8.1) found below its visibility criterion"
    _at_c, _cr_c, _kp_c = CLAIMS9["attrib"], CLAIMS9["crit"], CLAIMS9["keeps"]
    dose_open_stmt = rw10(
        "§7d, the clause paragraph's opening", f"phrase '{_dq}' on its anchor line", _dose_s, lambda t: _dq in t,
        f"The preprint's clause -- '{_dq}' ({pp_dose}, working tree, untracked; §8.1 is the PROPOSAL-m gating campaign, {pp_81}) -- needs more than a gloss.",
        lambda by: (f"The preprint's clause -- '{_dq}' ({pp_dose} on the audited and v6 texts; §8.1 is the PROPOSAL-m "
                    f"gating campaign, {pp_81}) -- needed more than a gloss; patch v7 removes it (Round 10, {by})."))
    dose_i_stmt = rw10(
        "§7d (i)", _at_c[0], _at_c[1], _at_c[2],
        "(i) It attributed the finding to a calibration (§8.1) whose artifact did not exist at the pin.",
        lambda by: f"(i) It attributed the finding to a calibration (§8.1) whose artifact did not exist at the pin; v7 drops the attribution (Round 10, {by}).")
    dose_ii_tail = rw10(
        "§7d (ii)", _cr_c[0], _cr_c[1], _cr_c[2], "",
        lambda by: f"; v7 no longer states f1's dose against it (Round 10, {by})")
    dose_keep_stmt = rw10(
        "§7d, the proposed wording's paragraph", _kp_c[0], _kp_c[1], _kp_c[2], "",
        lambda by: f" The audited and v6 texts kept it; v7 does not (Round 10, {by}).")
    dose_row_src = rw10(
        "the dose row's source", f"phrase '{_dq}' (the row's label) on its anchor line", _dose_s, lambda t: _dq in t,
        pp_tag.replace(PREPRINT, pp_dose),
        lambda by: (f"{pp_dose} as the audited text and the patched text that preceded the preprint of record wrote it (both archived untracked, out of the "
                    f"release); the preprint of record (working tree, untracked; sha256 {pp_sha[:8]}...{pp_sha[-6:]}, "
                    f"computed at run time, MATCH vs the preprint of record {PP_REC}, {PREPRINT_RULING}) removes the "
                    f"clause (closing sections)"), row=True)
    dose_row_note = rw10(
        "the dose row's note", _at_c[0], _at_c[1], _at_c[2],
        f"wording, not a number: the clause attributes the finding to a calibration (§8.1) whose artifact did not exist at the pin (G-CAL's 0.12 artifact first at {POST_PIN_GCAL})",
        lambda by: (f"wording, not a number: the clause, as the audited text and the patched text that preceded the preprint of record wrote it, attributed the "
                    f"finding to a calibration (§8.1) whose artifact did not exist at the pin (G-CAL's 0.12 artifact first at "
                    f"{POST_PIN_GCAL}); the preprint of record drops the attribution (a finding on the patch; "
                    f"closing sections)"), row=True)
    # covariate tie (values-check finding 9): accuracy on Q rounds that carried corruption
    d_pooled = cp[0] / cp[1] - cq[0] / cq[1]
    d_corr_only = cp[0] / cp[1] - sum(qa_corr) / len(qa_corr)
    calib_unchanged_runs = calib["n_seeds"] * len(zero_items)
    assert len(clean) == 16 and all(abs(acc[k_] * calib["n_seeds"] * len(clean) - round(acc[k_] * calib["n_seeds"] * len(clean))) < 1e-9
                                    for k_ in ("CORR_clean", "CORR_corrupted"))
    L += ["## 7. The CORR contrast's dose: is there a known artifact at rate 0.12?", "",
          "### 7a. What the f1 record itself says (cycle 4, 2026-08-10)", "",
          f"- Smoke read: 'corrupted tasks render correctly' ({LOC_SMOKE_READ}) (first smoke, v1 pools 61d39225/12907bcf, pre-recast; not the run's renders). Scope: the read sits in the first f1 smoke entry ({LOC_SMOKE1}), which the newest-first log places before the pool-recast amendment (entry {LOC_AMEND}; the recast bullet {LOC_RECAST}); the v1 shas are at {LOC_V1_SHAS}, the run's v2 shas (8547d9a1/2c2c2273) at {LOC_V2_SHAS}. Check (computed-new; the first smoke's raw logs no pools sha, and `data/f/pools.json` has {n_pools_versions} committed version up to the pin, v2): the first smoke's CORR rows (sessions < 1100 in `data/f/sessions_smoke.jsonl`, {_s1['sessions']} sessions) have {_s1['verbatim_in_v2_pools']} of {_s1['task_lines']} Task lines verbatim in the v2 pools, {_s1['start_What_is']} in the QA form the recast removed, and {_s1['q_rounds_within_6_letters_of_a_v2_clean_item']} of {_s1['q_rounds']} Q-round texts within 6 letters of a same-length v2 CORR_clean item; the later smokes' CORR rows: {smoke_corr['later smokes (1100-series)']['verbatim_in_v2_pools']} of {smoke_corr['later smokes (1100-series)']['task_lines']} verbatim (the P rounds), {smoke_corr['later smokes (1100-series)']['q_rounds_within_6_letters_of_a_v2_clean_item']} of {smoke_corr['later smokes (1100-series)']['q_rounds']} Q rounds within 6 letters.",
          f"- Verdict entry, CORR note: the calibration accuracy delta 'VANISHED in-session (P .838 vs Q .833) -- the corrupted property was visible but performatively costless, weakening the aversiveness prior behind CORR's one-sided direction; attach to any CORR interpretation' ({LOC_CORRNOTE}); reproduced in §6 (its '+.094' is the superseded v1 figure).",
          f"- Post-hoc anomaly: CORR exclusions P/Q 7/1 vs sham 2/5, one-sided Fisher p = .035, no verdict weight ({loc(ARCH, 'CORR anomaly line')}); postscreen JSON `corr_anomaly` = {post['corr_anomaly']}.",
          f"- FINDINGS-4 repeats both as loose ends without weight ({LOC_F4_LOOSE}; '.838/.833 -- corruption visible but costless' at {LOC_F4_VISIBLE}).",
          "- Nothing in the cycle-4 record identifies a delivery defect at the dose. **In the f1-era record: no known artifact at 0.12.**",
          "",
          "### 7b. What the record at the pin says about f1's corruptor (Phase 2, PROPOSAL-m arc, before bbc9ffe)", "",
          f"- v1.7 referent check (2026-10-04): f1's corrupt() replayed on the 16 items -- 32 slots drawn, 31 letters changed, per item [1,0,5,2,3,1,4,6,2,1,2,1,0,1,1,1]; items 1 and 12 change 0 letters; 40 of 306 Q rounds delivered the clean text verbatim (item 1: 23, item 12: 17); the checker's note says the preprint's dose note rests on this ({loc('results/raw/2026-10-04_m-v1.7_referent_check.txt', 'For the 31 I replayed f1', 'preprint' + chr(39) + 's dose note rests on (G6a.11)')}).",
          f"- G-PORT entry C1: 'f1's corrupted label sometimes delivered byte-clean text' -- 40 of 306 Q rounds, and 16 of the 58 sessions that reached the first read had exactly one byte-clean forced Q round before the pick, none two ({loc('RESULTS.md', 'C1, under (3).', 'This bears on A0' + chr(39) + 's comparison with f1' + chr(39) + 's primary.')}); differences raw D17 ({loc('results/raw/2026-10-07_m-gport_differences.md', '#### D17.')}).",
          f"- PROPOSAL-m §2.3: condition (1) 'every item ≥ 3 changed positions', 'the floor of 3 is the visibility criterion'; G-CAL is to replay 'f1's corruptor at 0.12 ... against conditions (1)–(2) -- the record behind the preprint's f1 CORR dose note, which the posting rule attaches only if this artifact exists' ({loc('PROPOSAL-m-gating-campaign-v1_11.md', '**2.3 Dose')}). 'Artifact' there means a record file (G-CAL's replay), not a confound.",
          "",
          "### 7c. Reproduced here from committed JSONL (no corruptor code), then by a replay of the corruptor", "",
          f"- Transcript-derived: each CORR round's `Task:` line (harness-written; its first 40 characters equal the stored `rounds[].task` on every round) is matched to its CORR_clean item by length and minimum Hamming distance (unique on every round). P rounds are clean pool text on every round: {p_ok}. Q rounds: {n_q} (forced {len(f_q)}, free {len(fr_q)}), over all 64 CORR sessions incl. excluded. Letters changed per item (items 0-15): {changed_t}; total {sum(c for c in changed_t if c is not None)}.",
          f"- Byte-clean Q rounds (Task text identical to the clean item): {len(clean_q)}/{n_q} (forced {len(clean_f)}/{len(f_q)}, free {len(clean_fr)}/{len(fr_q)}); by item {dict(sorted(by_item_clean.items()))}.",
          f"- Sessions that reached the first read (≥ 1 free choice): {len(reached)} ({len(reached_valid)} valid + {len(reached) - len(reached_valid)} excluded post-pick); each saw exactly 2 forced Q rounds before the pick; byte-clean forced Q rounds before the pick: {dict(sorted(clean_pre.items()))} (sessions by count: 0, 1, 2). In the primary's domain (56 valid): {len(one_clean_valid)} with one clean pre-pick Q round, {len(both_corr_valid)} with both corrupted.",
          f"- Replay of f1's corrupt() at 0.12 ({ports['corrupt()']}): renders sha256('\\n'.join)[:16] = `{rsha}` vs calib.json `corr_sha` `{calib['corr_sha']}` ({'EQUAL' if rsha == calib['corr_sha'] else 'DIFFERENT'}); draws {sum(draws)}, letters changed {sum(changed_r)} (one draw returns the original letter); per item {changed_r}; equal to the transcript-derived vector: {replay_eq}. Items with 0 changed: {zero_items}; items meeting PROPOSAL-m's condition (1) (≥ 3 changed): {len(ge3)}/16 {ge3}.",
          f"- Post-pin comparison (read-only): `data/m/gates/G-CAL_model-free.json`@{POST_PIN_GCAL} (descendant of the pin: {after_pin}) `f1_012`: n_changed {gcal['n_changed']}, n_hits {gcal['n_hits']}, n_cond1 {gcal['n_cond1']}, n_cond2 {gcal['n_cond2']}, renders_sha16 `{gcal['renders_sha16']}`; per-item changed equal to this replay: {gcal_eq}. N5 cites it and does not adjudicate PROPOSAL-m (whether its posting-rule flag is set is that arc's question).",
          f"- m-arc domain cross-check (RESULTS.md@{PIN} G-PORT A1, {LOC_A1}): first picks to P over sessions reaching the first read = {kr}/{len(reached)} → Δ {kr / len(reached) - 0.5:+.4f}; the record's 30/58 (+.017) reproduces; f1's own domain stays 28/56 (0.000).",
          "",
          f"- POST-HOC, descriptive, no verdict weight (Code's; not in the record): within the 56 valid CORR sessions, first picks to the clean label were {k1}/{len(one_clean_valid)} (Δ {k1 / len(one_clean_valid) - 0.5:+.4f}) where one pre-pick Q round was clean and {k2}/{len(both_corr_valid)} (Δ {k2 / len(both_corr_valid) - 0.5:+.4f}) where both were corrupted. In-session accuracy on Q rounds by delivered text: byte-clean {sum(qa_clean)}/{len(qa_clean)} = {sum(qa_clean) / len(qa_clean):.4f}, corrupted text {sum(qa_corr)}/{len(qa_corr)} = {sum(qa_corr) / len(qa_corr):.4f} (clean label P: {cp[0]}/{cp[1]} = {cp[0] / cp[1]:.4f}).",
          f"- POST-HOC, descriptive, no verdict weight (values-check finding 9): the record reads the CORR covariate as 'VANISHED in-session (P .838 vs Q .833) -- the corrupted property was visible but performatively costless' ({LOC_VISIBLE}). Pooled over all {n_q} Q rounds the in-session delta is {d_pooled:+.4f}; on the {len(qa_corr)} Q rounds whose text actually carried corruption it is {d_corr_only:+.4f} (P {cp[0] / cp[1]:.4f} vs {sum(qa_corr) / len(qa_corr):.4f}), because the {len(qa_clean)} byte-clean Q rounds scored {sum(qa_clean)}/{len(qa_clean)}. So part of the 'vanished' delta is dilution by clean deliveries, and 'corruption visible' does not hold on {len(clean_q)} of {n_q} Q rounds, whose text was the clean item. Both deltas stay below the calibration covariate +.078, whose {calib['n_seeds'] * len(clean)} corrupted-render runs also include items {zero_items} unchanged ({calib_unchanged_runs} runs; the replay's renders are calib.json's, sha `{rsha}`). Rounds are clustered within sessions; no test is attached.",
          "",
          "### 7d. Answer", "",
          f"**Yes -- there is a known artifact at the 0.12 dose, and the note should disclose it; it is not in the f1-era record.** The cycle-4 record identified no dose defect (its CORR caveats are the vanished in-session accuracy delta and a post-hoc exclusion anomaly). The record at the pin (Phase 2, 2026-10-04 and 2026-10-07, both before {PIN}) documents, and this item reproduces from `data/f/sessions.jsonl` and `data/f/pools.json`, that f1's corruptor at rate .12 left items 1 and 12 unchanged: across all 64 CORR sessions (excluded ones included), {len(clean_q)} of {n_q} corrupted-label rounds delivered the clean text verbatim; in the primary's domain (the 56 valid sessions behind 28/56 = 0.000), {len(one_clean_valid)} sessions saw only one corrupted task, not two, before the first choice ({clean_pre[1]} of the {len(reached)} sessions that reached the first choice, m's domain). Across the 16 items the corruptor changed {sum(changed_r)} letters (median {statistics.median(changed_r):g} per item); only {len(ge3)} of 16 items reach the three-letter floor PROPOSAL-m later adopted as its visibility criterion.",
          "",
          f"{dose_open_stmt} {dose_i_stmt} The substance ({16 - len(ge3)}/16 items below the floor; {len(clean_q)}/{n_q} byte-clean Q rounds) was on record through model-free replays of f1's corruptor (v1.7 referent check 2026-10-04; G-PORT C1). [Locators: `data/m/gates/G-CAL_model-free.json` is {'tracked' if gcal_at_pin else 'absent'} at {PIN} and first exists at {POST_PIN_GCAL}, after the pin; the v1.7 replay {LOC_V17_REPLAY}; G-PORT C1 {LOC_C1}; the v1.7 checker note G6a.11 ({LOC_G6A11}) says 'the computation supports the note's substance' and that root:182 states 'found' ahead of its record because no G-CAL artifact existed yet ({LOC_G6A11_SUBST}).] (ii) The floor is m's criterion, not f1's (f1 pre-registered a deterministic, sha-pinned corruption with its accuracy delta as a covariate, {loc('PROPOSAL-f-natural-reinforcer-screen.md', '| 4 | CORR |')}){dose_ii_tail}. {pp_iii}",
          "",
          f"A wording the record supports (a proposal for the design seat; domains named): 'at a corruption rate (.12) at which 2 of 16 items rendered unchanged -- {len(clean_q)} of {n_q} corrupted-label rounds across all 64 CORR sessions delivered clean text, and {len(one_clean_valid)} of the 56 valid sessions saw one corrupted task rather than two before the first choice -- and {16 - len(ge3)} of 16 items fell below the three-letter floor of the later campaign.' If the note keeps 'a later calibration', it should cite G-CAL's artifact ({POST_PIN_GCAL}, post-pin) and say it is a replay of the corruptor, not a measurement on the model.{dose_keep_stmt} The post-hoc splits in 7c are descriptive only and carry no weight either way.",
          ""]
    assert rsha == calib["corr_sha"] and replay_eq and gcal_eq and after_pin and not gcal_at_pin
    assert len(clean_q) == 40 and n_q == 306 and clean_pre[1] == 16 and clean_pre.get(2, 0) == 0
    fig("CORR dose caveat: known artifact at 0.12? (yes/no)",
        f"YES (not in the f1-era record): items {zero_items} unchanged; {len(clean_q)}/{n_q} Q rounds byte-clean over all 64 CORR sessions (forced {len(clean_f)}/{len(f_q)}, free {len(clean_fr)}/{len(fr_q)}); {len(one_clean_valid)}/56 valid sessions ({clean_pre[1]}/{len(reached)} reaching the first read) had one clean pre-pick Q round, none two; {sum(changed_r)} letters over 16 items; {len(ge3)}/16 items ≥ 3 changed; Q accuracy on corrupted-text rounds {sum(qa_corr)}/{len(qa_corr)} vs byte-clean {sum(qa_clean)}/{len(qa_clean)} (post-hoc)",
        "data/f/sessions.jsonl (CORR transcripts' Task lines) + data/f/pools.json CORR_clean; replay validated by data/f/calib.json corr_sha", "reproduced",
        "first on record at " + loc('results/raw/2026-10-04_m-v1.7_referent_check.txt', 'For the 31 I replayed f1', 'preprint' + chr(39) + 's dose note rests on (G6a.11)') + " and RESULTS.md@bbc9ffe G-PORT C1 (" + loc('RESULTS.md', 'C1, under (3).', 'This bears on A0' + chr(39) + 's comparison with f1' + chr(39) + 's primary.') + "); post-pin G-CAL artifact (bab921c) agrees; the f1-era record (archive) has no dose defect")
    fig("preprint 'at a dose a later calibration (§8.1) found below its visibility criterion'",
        f"{len(ge3)}/16 items meet m's ≥3-letter floor at 0.12; at the pin the support was a model-free replay of f1's corruptor (v1.7 referent check, G-PORT C1), not a calibration and not a measurement on the model; G-CAL's artifact is post-pin; {pp_bc_value}",
        dose_row_src, "discrepant",
        f"{dose_row_note}; the substance ({16 - len(ge3)}/16 items below the floor; {len(clean_q)}/{n_q} byte-clean Q rounds) was on record through model-free replays of f1's corruptor (v1.7 referent check, whose checker note G6a.11 says 'the computation supports the note's substance', {LOC_G6A11_SUBST}; G-PORT C1, {LOC_C1}); {pp_bc_note}; suggested replacement in §7d; whether PROPOSAL-m's posting flag is set is not N5's call")
    J["corr_dose"] = {"q_rounds": n_q, "q_forced": len(f_q), "q_free": len(fr_q),
                      "byte_clean_q": len(clean_q), "byte_clean_forced": len(clean_f),
                      "byte_clean_free": len(clean_fr), "byte_clean_by_item": dict(by_item_clean),
                      "changed_per_item": changed_r, "draws_total": sum(draws),
                      "zero_items": zero_items, "items_ge3": ge3,
                      "renders_sha16": rsha, "calib_corr_sha": calib["corr_sha"],
                      "reached_first_read": len(reached), "reached_valid": len(reached_valid),
                      "clean_prepick_counts": dict(clean_pre),
                      "valid_one_clean": len(one_clean_valid), "valid_both_corrupted": len(both_corr_valid),
                      "posthoc_first_pick_P": {"one_clean": [k1, len(one_clean_valid)],
                                               "both_corrupted": [k2, len(both_corr_valid)]},
                      "q_accuracy": {"byte_clean": [sum(qa_clean), len(qa_clean)],
                                     "corrupted_text": [sum(qa_corr), len(qa_corr)]},
                      "m_domain_first_reads": [kr, len(reached)],
                      "post_pin_gcal_equal": gcal_eq, "post_pin_rev": POST_PIN_GCAL,
                      "gcal_artifact_at_pin": bool(gcal_at_pin),
                      "in_session_delta_pooled": d_pooled,
                      "in_session_delta_corrupted_text_only": d_corr_only,
                      "calib_runs_on_unchanged_items": calib_unchanged_runs,
                      "smoke_corr_rows_vs_v2_pools": smoke_corr}

    # ------------------------------------------------------------- figures --
    n_disc_all = sum(1 for f_ in FIG if f_["status"] == "discrepant")
    assert n_disc_all == 4
    # Round 10 (fix round): Notes 1 and 3's statements about preprint sentences
    note1_stmt = rw10(
        "Note 1", _at_c[0], _at_c[1], _at_c[2],
        "the preprint's CORR dose clause, which attributes the finding to a calibration whose artifact did not exist at the pin, though the substance was on record through model-free replays; §7d",
        lambda by: ("the CORR dose clause of the audited and v6 texts, which attributed the finding to a calibration whose "
                    "artifact did not exist at the pin, though the substance was on record through model-free replays; §7d; "
                    f"v7 drops the attribution: Round 10, {by}"))
    note3_share = rw10(
        "Note 3, first clause", _sh_c[0], _sh_c[1], _sh_c[2],
        "'session share ≈ .50' in every arm should give the range or name FDBK",
        lambda by: f"'session share ≈ .50' in every arm (the audited and v6 texts) should have given the range or named FDBK; v7 {_sh7} (Round 10, {by})")
    note3_first = rw10(
        "Note 3, second clause", _fc_c[0], _fc_c[1], _fc_c[2],
        "'no evaluation-seeking against a predominantly positive feedback stream' is a first-choice statement (23/44) and should say so",
        lambda by: (f"'no evaluation-seeking against a predominantly positive feedback stream' (the audited and v6 texts) was "
                    f"a first-choice statement (23/44) that did not say so; v7 {_fc7} (Round 10, {by})"))
    note3_uni = rw10(
        "Note 3, third clause", _uni_c[0], _uni_c[1], _uni_c[2],
        "'about 1% of rounds, uniformly across arms' should rest on the overall rate and say 'no detectable heterogeneity' (§4 wording)",
        lambda by: ("'about 1% of rounds, uniformly across arms' (the audited and v6 texts) should have rested on the overall "
                    f"rate and said 'no detectable heterogeneity' (§4 wording); v7 {_ndh7} (Round 10, {by})"))
    _n3_any = any(r_["reworded"] for r_ in RW10[-3:])
    L += ["## Figures (as the block writes them)", "",
          "| figure | value printed | source | status | note |",
          "|---|---|---|---|---|"]
    for f_ in FIG:
        L.append(f"| {cell(f_['figure'])} | {cell(f_['value'])} | {cell(f_['source'])} | {f_['status']} | {cell(f_['note'])} |")
    L += ["",
          "## Notes for the PI and the design seat (no STOP)", "",
          f"1. Every figure the block lists for N5 is reproduced from committed JSON/JSONL except the exploration share, which has no f1 computation on record and is computed-new here: {shares[lo_a]:.3f}-{shares[hi_a]:.3f} by arm, with FDBK's {fx['share_P']:.3f} toward the verdict config the largest deviation from .50, map-consistent and nominally p = {fx['posthoc_signflip']['p_two_sided']:.3f} uncorrected at the session level (post-hoc; {fx['posthoc_signflip']['bonferroni6']:.2f} after a six-arm Bonferroni correction, so not an established exception; §5). No reproduction needed an analyzer change, so nothing here is a STOP. Tier 2 has no fail text; {n_disc_all} rows are `discrepant`: two transcriptions in the f1 verdict entry -- '33 attempts' is the number of cells in the termination table, the attempts number {tot_t} ({100 * tot_t / tot_n:.2f}% of rounds; FINDINGS-4 carries the same 33), and the CORR covariate '+.094' is f0 v1's on superseded pools, the figure of record being +.078 (logged by the cycle-4 record itself at {LOC_078}) -- and one wording gap ({note1_stmt}); and, from round 2, the by-arm reading of the termination rate, which does not hold for sham ({100 * rates['sham']:.2f}%; §4; not a transcription, since the record's ≈ 1.0% is an overall figure). None changes a verdict, a direction or a p.",
          "2. Referent notes: the producing analyzers (f_sessions.py, f_postscreen_descriptive.py, f0_calibrate.py) are in the gitignored clone, not the record; a reader of the tag can recompute every figure above from `data/f/` but cannot run f1's own analyzer. The 93.4% FDBK composition is printed as fixed text by the post-screen analyzer; it is computed here from the JSONL (256/274), agreeing with the verdict entry's '274 delivered verdicts, 93.4% Correct' (" + LOC_FDBK_VERDICT + ") and the values-check the G-PORT differences raw reports.",
          f"3. Preprint line {pp_main}{'' if _n3_any else ' (working tree)'}: {note3_share}; {note3_first}; {note3_uni}. Proposals; the PI and the design seat decide.",
          "4. The CORR dose caveat (§7d) is the one substantive addition the note should carry; the suggested wording is a proposal for the design seat, with its domains named (306 rounds over all 64 CORR sessions; 16 of the 56 valid sessions).",
          f"5. (Round 2; for the design seat, no note sentence changes.) FINDINGS-4 names the DIFF deflation '(ii) a generic brevity preference could mimic it' ({LOC_F4_BREV}). Hard was the longer config -- its forced responses were longer in {hard_longer}/{len(dsess)} valid DIFF sessions (mean n_tok {mean(tokP):.2f} easy vs {mean(tokQ):.2f} hard) and its task texts are longer too (pool means {task_len['DIFF_easy']:.1f} vs {task_len['DIFF_hard']:.1f} characters) -- so a brevity preference would push toward easy; the deflation that could mimic toward-hard is a longer-rounds preference. The record's own test is two-sided, and its conclusion is worded as a length preference ({LOC_BREV_ARCH}); {len_note5_stmt}. FINDINGS-4's 'brevity' is a wording slip in the record, flagged, not changed.",
          ""]

    # --------------------------------------------------------- values-check --
    vc = [
        ("1", "substantive", "§5 / Figures: 'consistent with ≈ .50 in every arm' had no test; FDBK's all-picks share .576 is map-consistent, 6/44 sessions 6/6 to the verdict config, session-level sign-flip p = .031 uncorrected", "fixed",
         f"Re-run here (exact two-sided sign-flip over sessions, ties at 3/6 dropped): FDBK S = {fx['posthoc_signflip']['S']:+d} over {fx['posthoc_signflip']['nonzero_sessions']} sessions, p = {fx['posthoc_signflip']['p_two_sided']:.4f}, Bonferroni ×6 {fx['posthoc_signflip']['bonferroni6']:.3f}; maps A {fak}/{fan}, B {fbk}/{fbn}; {fx['sessions_all_P']} sessions 6/6, {fx['sessions_all_Q']} 0/6; other arms p ≥ {others_min_p:.3f} -- all as the checker reported. The claim is withdrawn; §5 prints the range, the post-hoc table and the FDBK line (labeled post-hoc, no verdict weight, primary untouched); new Figures row; Notes 1 and 3."),
        ("2", "minor", "§7d: 'accurate as far as it goes' is too generous; the v1.7 referent check's G6a.11 says root:182 'states found ahead of its record'; at the pin no calibration had found anything", "fixed",
         f"G6a.11 read at {LOC_G6A11}; `data/m/gates/G-CAL_model-free.json` at {PIN}: {'present' if gcal_at_pin else 'absent'} (git rev-parse), first at {POST_PIN_GCAL}. §7d now says the clause stated 'found' ahead of its record and that the pinned support was model-free replays (v1.7 referent check, G-PORT C1), not a calibration; Figures row note rewritten. [v2 wording; refined in round 2, row R2-2.]"),
        ("3", "minor", "§7d suggested wording mixes domains (58 = m's reached-the-first-read; 306 rounds from all 64 sessions incl. excluded)", "fixed",
         f"Recount: valid sessions with one clean pre-pick Q round {len(one_clean_valid)}/56, both corrupted {len(both_corr_valid)}; reached-first-read {dict(sorted(clean_pre.items()))}; Q rounds {n_q} over all 64 sessions. Wording now '{len(one_clean_valid)} of the 56 valid sessions' and '{n_q} ... across all 64 CORR sessions'; Figures row reworded."),
        ("4", "minor", "§4 locators: '33 attempts ≈ 1.0%' is :97-98 (not :98); sham 7 and NOV-Q 3 vs NOV-P 3 are on :99 (not :97)", "fixed",
         f"Anchored by text: '33 attempts ≈ 1.0%' {LOC_T33}; sham (7), NOV-Q 3 vs NOV-P 3 {LOC_TSHAM}; FINDINGS-4 '33 attempts, ~1.0% of rounds' {LOC_T33_F4} (v1 printed :82 only)."),
        ("5", "minor", "§6 locators: P .838 vs Q .833 is :109, DIFF .883/.592 :112 (v1 printed :108 for both); the verdict entry's '274 delivered verdicts, 93.4% Correct' (:106) was not cited in the FDBK row", "fixed",
         f"P .838/.833 {LOC_838}; DIFF .883/.592 {LOC_883}; '+.094' stays at {LOC_094}; CORR note span {LOC_CORRNOTE}; '274 delivered, 93.4%' {LOC_FDBK_VERDICT} and the post-screen '93.4%-positive' {LOC_FDBK_POST} now cited in §3b and the FDBK row."),
        ("6", "minor", "CORR covariate row: the cycle-4 record itself logs +.078 for the run's pools (f0 v2 entry, :258), which v1 did not cite", "fixed",
         f"'CORR delta +.078 covariate' at {LOC_078}; v1's +.094 at {LOC_094_V1}; both now cited in §1, §6 and the covariate row (the transcription inference is unchanged and stronger)."),
        ("7", "minor", "The preprint's sha256 was printed from a constant, never hashed", "fixed",
         f"The working-tree file is now hashed at run time: sha256 {pp_sha}; asserted against the preprint of record {PP_REC} ({PREPRINT_RULING}; v1-v3 asserted the block's d6431e97…222b8, the audited text; round 9 asserted ruling 9's {PREPRINT_V6_SHA[:8]}…{PREPRINT_V6_SHA[-5:]}, patch v6) before line {pp_n('found below its visibility criterion')} is quoted (MATCH); header line added; the sha256 printed as the file's is the run-time hash; the full-sha constant asserted is the routing's value of record (patch v7), the assert target, printed only as that value."),
        ("8", "minor", "Termination '≈ 1% by arm': by arm 0.79%-1.99%, sham's 2.0% double the stated rate; the note's sentence should rest on the overall rate", "fixed",
         f"Per arm {', '.join(f'{a_} {per_arm_t[a_]}/{per_arm_n[a_]}' for a_ in ARMS)}; sham {100 * rates['sham']:.2f}% is double the record's stated ≈ 1.0% but {sham_vs_overall:.2f}× the overall {100 * tot_t / tot_n:.2f}% (the raw says both); homogeneity p = {p_hom:.4f} over {n_tables} tables (unchanged). §4 and the row now say the 1% is overall and give a wording, using 'no detectable heterogeneity' rather than the checker's 'no heterogeneity' (a p of {p_hom:.2f} shows absence of evidence, not uniformity). [The row is split in round 2, row R2-3.]"),
        ("9", "minor", "§7c/§7d: the byte-clean rounds' bearing on the record's 'vanished' / 'visible but costless' reading was not drawn", "fixed",
         f"Q accuracy on corrupted-text rounds {sum(qa_corr)}/{len(qa_corr)}, byte-clean {sum(qa_clean)}/{len(qa_clean)}, P {cp[0]}/{cp[1]}: in-session delta {d_pooled:+.4f} pooled vs {d_corr_only:+.4f} on corrupted-text rounds. One post-hoc sentence added to §7c (no test; rounds clustered); it also notes that calib.json's +.078 includes {calib_unchanged_runs} runs on the two unchanged items."),
        ("10", "minor", "§1: the pre-registration entry ends at :420, not :419", "fixed",
         f"Span now {prereg}, end anchor asserted to be the line after 'After the screen: pause ...'."),
        ("F1", "minor (fixer's own)", "The '33 attempts' row cited `results/raw/2026-08-10_f_analysis.txt:3` without the pin", "fixed",
         f"Now {LOC_ANRAW}."),
        ("F2", "minor (fixer's own)", "§5 cited `jlens-qwen36/scripts/e2a_sessions.py`:N without marking it as the gitignored clone (not the record) or giving its hash", "fixed",
         f"Now {e2a_loc}."),
        ("F3", "minor (fixer's own)", "FINDINGS-4's 'Session share ≈ .50 in every arm' spans two lines; v1 cited :58", "fixed",
         f"Now {LOC_SHARE_F4}."),
    ]
    L += ["## Values-check", "",
          "Verifier pass 1 checked v1 of this raw (script sha256 3144fdc7…6302, raw sha256 58b7e90b…3dbe; 74 claims; independent recomputation from data/f at the pin; reran identically; redaction clean): one substantive and nine minor findings, no STOP. The fixer re-verified each against the record with its own tool runs before applying it; the evidence column below is printed by this script from the same run that wrote the sections above. Rows F1-F3 are the fixer's own. No finding was rejected.",
          "",
          "| # | severity | finding | disposition | evidence and change |",
          "|---|---|---|---|---|"]
    for (n_, sev, fd, disp, ev) in vc:
        L.append(f"| {n_} | {sev} | {cell(fd)} | {disp} | {cell(ev)} |")
    L.append("")
    # ------------------------------------------- values-check, round 2 --
    _s2 = smoke_corr["later smokes (1100-series)"]
    _sr_d = sr["per_arm"]["DIFF"]
    vc2 = [
        ("R2-1", "minor", "§3a: 'A generic brevity preference would mimic a toward-hard lean if it were general' is wrong-signed given the raw's own direction check: hard rounds were the longer ones, so a brevity preference would push toward easy; the sentence copies FINDINGS-4's pre-named wording", "fixed",
         f"Re-run here: in the {len(dsess)} valid DIFF sessions the hard config's forced rounds were longer in {hard_longer}, shorter in {easy_longer}, tied in {tie}; mean forced n_tok easy {mean(tokP):.2f} vs hard {mean(tokQ):.2f}; DIFF shorter-share {_sr_d['k']}/{_sr_d['n']} = {_sr_d['share']:.3f}. Added (computed-new, descriptive): the DIFF pools' task texts are longer on hard too (means {task_len['DIFF_easy']:.1f} vs {task_len['DIFF_hard']:.1f} characters), so the sign holds on either length. FINDINGS-4's wording at {LOC_F4_BREV}; {len_r21_stmt}. §3a reworded as the fix says; the direction-check bullet gives the task-text means; the length-test row's note now quotes the record's 'brevity-tracking' instead of using it in Code's voice; the fix's optional step taken: FINDINGS-4's 'brevity' flagged for the design seat (Note 5). No note sentence changes."),
        ("R2-2", "minor", "§7d(i): 'It stated found before any record supported it ... At the pin that was still so' is overbroad: at the pin the substance was on record (12/16 items below the floor; byte-clean delivery documented); only the attribution to a calibration ran ahead, the G-CAL artifact being absent at the pin", "fixed",
         f"The v1.7 checker note reads 'the computation supports the note's substance' ({LOC_G6A11_SUBST}); the substance at {LOC_V17_REPLAY} and G-PORT C1 {LOC_C1}; `data/m/gates/G-CAL_model-free.json` at {PIN}: {'present' if gcal_at_pin else 'absent'} (git rev-parse --verify), first at {POST_PIN_GCAL} (descendant of the pin: {after_pin}). §7d(i) replaced with the fix's two sentences (its figures computed by this run: {16 - len(ge3)}/16, {len(clean_q)}/{n_q}), locators appended in brackets; the preprint-clause row's note and Note 1 brought in line. The suggested note wording in §7d is unchanged."),
        ("R2-3", "minor", "Figures row 'termination attempts ≈ 1% of rounds by arm' carried status reproduced; the overall rate reproduces (~1%), but per arm the figure does not hold for sham (~2x)", "fixed",
         f"Re-run: overall {tot_t}/{tot_n} = {100 * tot_t / tot_n:.2f}%; by arm {', '.join(f'{a_} {per_arm_t[a_]}/{per_arm_n[a_]} ({100 * rates[a_]:.2f}%)' for a_ in ARMS)}; the stored rounds[].term agrees with the four regexes on {agree}/{agree + disagree} rounds. The fix's second alternative taken, because the status vocabulary is fixed (a status cell carries one of five words): the row is split into an overall row (reproduced) and a by-arm row (discrepant for sham; not a transcription, since the record's ≈ 1.0% is an overall rate and sham's 7 a count). Note 1 now counts the discrepant rows from the table ({n_disc_all})."),
        ("R2-4", "minor", "§5: 'FDBK is the exception to ≈ .50' is stronger than the raw's own test supports: p = .031 uncorrected is .18 after the raw's six-arm Bonferroni correction; FDBK is the largest deviation, not an established exception", "fixed",
         f"Re-run (exact two-sided sign-flip over sessions, ties dropped): FDBK S = {fx['posthoc_signflip']['S']:+d} over {fx['posthoc_signflip']['nonzero_sessions']} untied sessions, p = {fx['posthoc_signflip']['p_two_sided']:.4f}, ×6 = {fx['posthoc_signflip']['bonferroni6']:.3f}; share {fx['k_P']}/{fx['picks']} = {fx['share_P']:.3f}; map A {fak}/{fan}, map B {fbk}/{fbn}; {fx['sessions_all_P']} sessions 6/6, {fx['sessions_all_Q']} 0/6; other arms p ≥ {others_min_p:.3f}; FDBK asserted to have the largest |share − ½| and the smallest p of the six arms. §5's bullet now opens with the fix's wording; the exploration row's note and Note 1 say 'largest deviation, not an established exception'. The 0.47-0.58 range proposal stands."),
        ("R2-5", "minor", "§7a: the smoke read 'corrupted tasks render correctly' (archive:357) is cited without scope: that smoke ran on the superseded v1 pools (corrupted sha 12907bcf), before the recast to v2 (2c2c2273), so it says nothing about the run's items 1 and 12", "fixed",
         f"Placement: the read ({LOC_SMOKE_READ}) is inside the first f1 smoke entry ({LOC_SMOKE1}), which the newest-first log places before the pool-recast amendment (entry {LOC_AMEND}; recast bullet {LOC_RECAST}); the order is asserted. v1 shas at {LOC_V1_SHAS}; v2 shas at {LOC_V2_SHAS}. Computed-new check (the first smoke's raw logs no pools sha; `data/f/pools.json` has {n_pools_versions} committed version up to the pin, v2, so the v1 pools cannot be compared directly): the first smoke's CORR rows (sessions < 1100) have {_s1['verbatim_in_v2_pools']} of {_s1['task_lines']} Task lines verbatim in the v2 pools, {_s1['start_What_is']} in the QA form the recast removed, {_s1['q_rounds_within_6_letters_of_a_v2_clean_item']} of {_s1['q_rounds']} Q rounds within 6 letters of a v2 clean item; the later smokes' CORR rows have {_s2['verbatim_in_v2_pools']} of {_s2['task_lines']} verbatim and {_s2['q_rounds_within_6_letters_of_a_v2_clean_item']} of {_s2['q_rounds']} Q rounds within 6 letters. The fix's parenthesis added to the §7a bullet; the 'no known artifact in the f1-era record' conclusion is unchanged."),
        ("R2-6", "minor", "Locator precision: four locators anchored to an entry's start rather than the quoted span, and FINDINGS-4 §6 ('tested (ii) and it failed') was not cited", "fixed",
         f"Anchored by text, end anchors on the line carrying the quoted words: 'directionally consistent' {LOC_DIRCONS}; '274 delivered verdicts, 93.4% Correct' {LOC_FDBK_VERDICT}; G-PORT A1's 30/58 {LOC_A1}; FINDINGS-4 summary ledger {LOC_F4_LEDGER}; FINDINGS-4 §6 {LOC_F4_S6}, now cited in the length-test row."),
    ]
    L += ["### Values-check, round 2", "",
          "A second verifier pass checked v2 of this raw (script sha256 1abb9012…5e25, raw sha256 c3181d91…6c62) and left six residual findings, all minor, no STOP. Code re-checked each against the record with its own tool runs (outside this script first, then inside it) before applying it. All six were found correct and applied as their fixes say; for R2-3 the fix's second alternative was taken. None was rejected. This script prints the evidence column from the same run that wrote the sections above.",
          "",
          "| # | severity | finding | disposition | evidence and change |",
          "|---|---|---|---|---|"]
    for (n_, sev, fd, disp, ev) in vc2:
        L.append(f"| {n_} | {sev} | {cell(fd)} | {disp} | {cell(ev)} |")
    L.append("")
    vc = vc + vc2
    J["values_check"] = [{"id": n_, "severity": sev, "finding": fd, "disposition": disp, "evidence": ev}
                         for (n_, sev, fd, disp, ev) in vc]
    J["figures"] = FIG

    # ------------------------------------------- round 9: the patched preprint --
    # The PI's ruling 9 of 2026-10-10, as corrected. Every anchor, quoted phrase
    # and claim about a preprint sentence is checked on the patched text; a check
    # that fails is a finding on the patch for the design seat, recorded, never
    # raised. Only the constants' own consistency with the archived audited text
    # (when present) is asserted: a mismatch there is a defect of this script.
    aud_raw = git("show", f"{AUDIT_REV}:{DEF_OUT}").decode()
    arch_lines, arch_note = None, "absent at run time; the audited-line constants are not re-verified"
    if os.path.exists(os.path.join(REPO, PREPRINT_AUDITED)):
        with open(os.path.join(REPO, PREPRINT_AUDITED), "rb") as f:
            a_b = f.read()
        a_sha = sha256_bytes(a_b)
        if a_sha.startswith(PREPRINT_SHA_BLOCK[0]) and a_sha.endswith(PREPRINT_SHA_BLOCK[1]):
            arch_lines = a_b.decode("utf-8").split("\n")
            ok_l = all(sha256_bytes(arch_lines[n_ - 1].encode()) == h_ for n_, h_ in PP_AUDITED_LINE_SHA.items())
            ok_s = all(s_ in arch_lines[n_ - 1] for (n_, _, _, s_) in PP_AUDITED_SENTENCES)
            assert ok_l and ok_s, "audited-line constants disagree with the archived audited text"
            arch_note = (f"present, sha256 `{a_sha}` (the block's d6431e97…222b8: MATCH); read only to verify this "
                         f"script's constants: audited-line sha256s equal {ok_l}, audited sentence(s) verbatim on their line {ok_s}")
        else:
            arch_note = f"present, sha256 `{a_sha}`, not the block's d6431e97…222b8; not used"

    # Round 10: this section is round 9's, reproduced on round 9's preprint of
    # record (patch v6). v6's anchor lines are rebuilt from v7's by the
    # registered v6 sentences (v6_rb, built ahead of the sections above;
    # sha256-verified against PP_V6_LINE_SHA); the archived v6 copy, when present
    # and matching, is read in full and must agree with the rebuild (a mismatch
    # is a defect of this script).
    _v7_other = [x_ for x_ in PP_V7_CHANGED_LINES if x_ not in v6_rb]
    assert not any(lines_with(pp_lines[x_ - 1], nd_) for x_ in _v7_other
                   for nd_ in list(PP_ANCHORS) + list(PP_REANCHOR.values()))
    p9_lines, p9_sha, v6_lines, v6_note = list(pp_lines), None, None, None
    for n_, (l6_, _) in v6_rb.items():
        p9_lines[n_ - 1] = l6_
    if os.path.exists(os.path.join(REPO, PREPRINT_V6)):
        with open(os.path.join(REPO, PREPRINT_V6), "rb") as f:
            v6_b = f.read()
        v6_sha_ = sha256_bytes(v6_b)
        if v6_sha_ == PREPRINT_V6_SHA:
            v6_lines = v6_b.decode("utf-8").split("\n")
            ok6_l = all(v6_lines[n_ - 1] == l6_ for n_, (l6_, _) in v6_rb.items())
            diff6 = [i_ for i_, (x_, y_) in enumerate(zip(v6_lines, pp_lines), start=1) if x_ != y_]
            ok6_d = len(v6_lines) == len(pp_lines) and tuple(diff6) == PP_V7_CHANGED_LINES
            assert ok6_l and ok6_d, "v6 constants disagree with the archived patch-v6 text"
            p9_lines, p9_sha = v6_lines, v6_sha_
            v6_note = (f"present, sha256 `{v6_sha_}` computed at run time (ruling 9's value of record: MATCH); read only "
                       f"to verify this script's v6 constants and to quote v6 beside v7: the v6 lines rebuilt from v7 "
                       f"({', '.join(map(str, v6_rb))}) equal the archived copy's {ok6_l}; the archived copy and v7 differ on "
                       f"lines {', '.join(map(str, diff6))} only (the lines this script registers from Code's diff of the "
                       f"two texts: {ok6_d})")
        else:
            v6_note = f"present, sha256 `{v6_sha_}`, not ruling 9's {PREPRINT_V6_SHA[:8]}…{PREPRINT_V6_SHA[-5:]}; not used"
    if p9_sha is None:
        v6_note = ((v6_note + "; ") if v6_note else "absent at run time; ") + (
            f"round 9's anchor lines ({', '.join(map(str, v6_rb))}) are v7's with the registered v6 sentences substituted "
            f"back, sha256-verified against this script's v6 constants; v7's other changed lines "
            f"({', '.join(map(str, _v7_other))}) carry none of this raw's anchors and are kept as v7's")
    p9_text = "\n".join(p9_lines)

    def p9_n(needle: str):
        """Round 10: the line of `needle` on the v6 text (round 9's patched text)."""
        hits = lines_with(p9_text, needle)
        return hits[0] if hits else "? (not found on the patched text; Round 9)"

    def audited_from(n_aud: int, line: str):
        """The audited line n_aud rebuilt from its patched counterpart: identical,
        or one registered audited sentence substituted back; sha256-verified.
        Returns (text or None, (old sentence, new sentence) or None)."""
        if sha256_bytes(line.encode()) == PP_AUDITED_LINE_SHA[n_aud]:
            return line, None
        for (n_, a_, e_, s_) in PP_AUDITED_SENTENCES:
            if n_ == n_aud and a_ in line and e_ in line[line.index(a_):]:
                i_ = line.index(a_)
                j_ = line.index(e_, i_) + len(e_)
                rb_ = line[:i_] + s_ + line[j_:]
                if sha256_bytes(rb_.encode()) == PP_AUDITED_LINE_SHA[n_aud]:
                    return rb_, (s_, line[i_:j_])
        return None, None

    r9_anchor, r9_line, r9_aud, r9_chg = [], {}, {}, {}
    for nd, n_aud in PP_ANCHORS.items():
        n_new = p9_n(nd)
        found = isinstance(n_new, int)
        if found and n_aud not in r9_line:
            r9_line[n_aud] = n_new
            r9_aud[n_aud], r9_chg[n_aud] = audited_from(n_aud, p9_lines[n_new - 1])
        r9_anchor.append({"needle": nd, "audited_line": n_aud, "patched_line": n_new if found else None,
                          "line_identical": (found and sha256_bytes(p9_lines[n_new - 1].encode()) == PP_AUDITED_LINE_SHA[n_aud])})
    # every form in which v3 printed a preprint line number: `path:N`, 'Preprint
    # line N' (Note 3) and 'line N is quoted' (values-check row 7). 'root:N' is
    # the v1.7 checker note G6a.11's own locator, quoted from the record, not one
    # of this raw's anchors. Any other occurrence of the number in v3 must be a
    # round count ('free N', '/N'); anything else means this sweep missed a form.
    PRINT_FORMS = (f"{PREPRINT}:{{n}}", "Preprint line {n}", "line {n} is quoted")
    printed_at, quoted_root, round_counts = {}, {}, {}
    for n_ in sorted(set(PP_ANCHORS.values())):
        printed_at[n_] = {f_.format(n=n_): lines_with(aud_raw, f_.format(n=n_)) for f_ in PRINT_FORMS}
        quoted_root[n_] = lines_with(aud_raw, f"root:{n_}")
        round_counts[n_] = []
        for i_, l_ in enumerate(aud_raw.split("\n"), start=1):
            for f_ in PRINT_FORMS + ("root:{n}",):
                l_ = l_.replace(f_.format(n=n_), "")
            if re.search(rf"(?:free |/){n_}(?![0-9A-Za-z])", l_):
                round_counts[n_].append(i_)
                l_ = re.sub(rf"(?:free |/){n_}(?![0-9A-Za-z])", "", l_)
            assert not re.search(rf"(?<![0-9A-Za-z.]){n_}(?![0-9A-Za-z])", l_), \
                f"v3 raw line {i_}: preprint line {n_} in a form this sweep does not list"

    def on_line(nd: str, fn):
        """(on the audited line, on the patched line) for a check over the anchor's line."""
        n_new, n_aud = p9_n(nd), PP_ANCHORS[nd]
        new_ = fn(p9_lines[n_new - 1]) if isinstance(n_new, int) else None
        aud_ = fn(r9_aud[n_aud]) if r9_aud.get(n_aud) is not None else None
        return aud_, new_

    r9_quote = []
    for nd, ph in PP_QUOTES:
        a_, n_ = on_line(nd, lambda t, ph=ph: ph in t)
        r9_quote.append({"phrase": ph, "anchor": nd, "patched_line": p9_n(nd), "on_audited": a_, "on_patched": n_})
    claims = [  # round 9's claims; 2-8 are CLAIMS9's (text, anchor and predicate defined ahead of the sections)
        ("§7d (iii); the dose row's value and note", "the CORR dose clause omits the byte-clean delivery",
         "found below its visibility criterion", omits_byteclean),
        ("§7d (i); the dose row's note; Note 1",) + CLAIMS9["attrib"],
        ("§7d (ii)",) + CLAIMS9["crit"],
        ("§7d (the proposed wording's paragraph)",) + CLAIMS9["keeps"],
        ("§3a; the length-test row; Note 5",) + CLAIMS9["unsigned"],
        ("§5; Note 3",) + CLAIMS9["share"],
        ("§5; Note 3",) + CLAIMS9["first"],
        ("§4; the homogeneity row; Note 3",) + CLAIMS9["uniform"],
    ]
    r9_claim = []
    for where_, cl, nd, fn in claims:
        a_, n_ = on_line(nd, fn)
        r9_claim.append({"claim": cl, "where": where_, "anchor": nd, "patched_line": p9_n(nd),
                         "held_on_audited": a_, "holds_on_patched": n_})

    # findings: one per changed audited line (with the checks that now fail on
    # it), then any failing check or missing anchor not already covered
    r9_find, covered, fid_of = [], set(), {}
    for n_aud in sorted(r9_line):
        n_new = r9_line[n_aud]
        if sha256_bytes(p9_lines[n_new - 1].encode()) == PP_AUDITED_LINE_SHA[n_aud]:
            continue
        fails = [c_ for c_ in r9_claim if PP_ANCHORS[c_["anchor"]] == n_aud and c_["holds_on_patched"] is not True]
        qfails = [q_ for q_ in r9_quote if PP_ANCHORS[q_["anchor"]] == n_aud and q_["on_patched"] is not True]
        covered |= {id(x_) for x_ in fails + qfails}
        fid = f"P9-{len(r9_find) + 1}"
        chg = r9_chg[n_aud]
        if chg is not None:
            old_s, new_s = chg
            txt = (f"**{fid} (line {n_new}; audited line {n_aud}).** The patch changes one sentence of the line; the rest "
                   f"of the line is byte-identical to the audited line (the audited sentence substituted back reproduces "
                   f"the audited line's sha256 `{PP_AUDITED_LINE_SHA[n_aud][:16]}`). Old (audited text d6431e97…222b8, "
                   f"line {n_aud}): '{old_s}' New (patched text {PREPRINT_V6_SHA[:8]}…{PREPRINT_V6_SHA[-5:]}, line {n_new}): '{new_s}'")
        else:
            old_s, new_s = (arch_lines[n_aud - 1] if arch_lines else None), p9_lines[n_new - 1]
            txt = (f"**{fid} (line {n_new}; audited line {n_aud}).** The line differs from the audited line outside the "
                   f"sentence(s) this script registers. Old (audited text, line {n_aud}): "
                   + (f"'{old_s}'" if old_s else "not available (archived copy absent; never required)")
                   + f" New (patched text {PREPRINT_V6_SHA[:8]}…{PREPRINT_V6_SHA[-5:]}, line {n_new}): '{new_s}'")
        txt += (" Checks of this raw that fail on the patched text: "
                + ("; ".join(f"{c_['claim']} ({c_['where']})" for c_ in fails) or "none")
                + "; quoted phrases absent from the patched line: "
                + ("; ".join(f"'{q_['phrase']}'" for q_ in qfails) or "none") + ".")
        if chg is not None and any(c_["claim"].startswith("the CORR dose clause omits") for c_ in fails):
            bc_figs = [(f"{len(clean_q)} of {n_q}", f"{len(clean_q)}/{n_q} byte-clean Q rounds over all 64 CORR sessions, excluded ones included (§7c)"),
                       (f"{len(one_clean_valid)} of the {vby['CORR']} valid sessions",
                        f"{len(one_clean_valid)}/{vby['CORR']} valid CORR sessions with one byte-clean pre-pick Q round (§7c)")]
            txt += (" The patched sentence carries the byte-clean delivery that §7d (iii) and the dose row found omitted; "
                    + "; ".join(f"'{s_}' on the patched line: {s_ in new_s} (this run: {d_})" for s_, d_ in bc_figs) + ".")
            held = [c_ for c_ in r9_claim if PP_ANCHORS[c_["anchor"]] == n_aud and c_["holds_on_patched"] is True]
            txt += (" Claims about this line that still hold: "
                    + "; ".join(f"{c_['claim']} ({c_['where']})" for c_ in held) + ".")
            obs = []
            if "64" not in new_s:
                obs.append("the patched sentence does not name the 306's domain (all 64 CORR sessions, excluded ones included), which §7d's proposed wording names")
            if new_s.count("dose") >= 2 and "a later calibration (§8.1)" in new_s:
                obs.append("the inserted text precedes the audited clause, which is kept, so the sentence names the dose twice ('at the dose used', 'at a dose a later calibration (§8.1) found below its visibility criterion')")
            m_ = re.search(r"which the gating campaign\S* dose calibration corrects", new_s)
            if m_:
                obs.append(f"it adds '{m_.group(0)}', a second, present-tense calibration attribution beside the kept "
                           "'a later calibration (§8.1)': the attribution §7d (i) flags (the dose row: at the pin the "
                           "support was a model-free replay of f1's corruptor, not a calibration), now made twice. Whether "
                           "the campaign corrects the dose is PROPOSAL-m's question, which N5 does not adjudicate")
            if "so the contrast ran weaker than nominal" in new_s:
                obs.append("'so the contrast ran weaker than nominal' is an inference from the delivery: as a statement "
                           "about delivery it is what §7c's counts show (fewer corrupted deliveries than nominal), but read "
                           "as an effect on the 0.000 contrast it would rest on §7c's post-hoc splits, which N5 holds "
                           "descriptive only, carrying no weight either way (§7d)")
            if m_ and "corrects, at a dose a later calibration (§8.1)" in new_s:
                obs.append("the kept clause 'at a dose a later calibration (§8.1) found below its visibility criterion' now "
                           "follows 'corrects', so it attaches ambiguously: to the correcting calibration, or, as in the "
                           "audited text, to the 0.000 contrast")
            if obs:
                txt += " Observations for the design seat: " + " ".join(f"({k_}) {o_[0].upper() + o_[1:]}." for k_, o_ in enumerate(obs, start=1))
            txt += (" The dose row keeps its status (discrepant): statuses are carried, never upgraded; whether the patch "
                    "discharges it is the design seat's and the PI's.")
        fid_of[n_aud] = (fid, chg is not None)
        r9_find.append({"id": fid, "patched_line": n_new, "audited_line": n_aud, "old": old_s, "new": new_s,
                        "checks_failed": [c_["claim"] for c_ in fails], "phrases_absent": [q_["phrase"] for q_ in qfails],
                        "text": txt})
    for x_ in [a_ for a_ in r9_anchor if a_["patched_line"] is None]:
        fid = f"P9-{len(r9_find) + 1}"
        r9_find.append({"id": fid, "anchor_missing": x_["needle"], "audited_line": x_["audited_line"],
                        "text": f"**{fid}.** Anchor '{x_['needle']}' (audited line {x_['audited_line']}) is not on the patched text; the locators that use it print '?'."})
    for x_ in [c_ for c_ in r9_claim + r9_quote if id(c_) not in covered
               and (c_.get("holds_on_patched", c_.get("on_patched")) is not True)]:
        fid = f"P9-{len(r9_find) + 1}"
        what_ = x_.get("claim") or f"phrase '{x_['phrase']}' on its anchor line"
        r9_find.append({"id": fid, "check": what_, "patched_line": x_["patched_line"],
                        "text": f"**{fid}.** '{what_}' does not hold on the patched text (line {x_['patched_line']})."})

    L += ["## Round 9 (2026-10-10): the preprint of record re-pointed (" + PREPRINT_V6_RULING + ")", "",
          f"- Preprint of record in round 9: patch v6, then `{PREPRINT}` (root, untracked), sha256 `{PREPRINT_V6_SHA}` (ruling 9's value of record); superseded by patch v7 ({PREPRINT_RULING}; Round 10 below) and archived untracked at `{PREPRINT_V6}`, out of the release; it is not required. This section is round 9's, reproduced on the v6 text; archived v6 copy: {v6_note}. v1-v3 of this raw quoted the audited text, the block's `d6431e97…222b8` ({BLOCK}@{PIN}:{lines_with(blk.decode(), 'd6431e97')[0]}), superseded by patch v6 and archived untracked at `{PREPRINT_AUDITED}`, out of the release; it is not required. Archived copy: {arch_note}.",
          "- Scope: the preprint handling only. Every other section above is computed as in v3 from the record at the pin, and no status changed (statuses are carried, never upgraded). A check below that fails on the patched text is a finding on the patch for the design seat (ruling 9), not a STOP.",
          "",
          "### Anchors, re-anchored on the patched text", "",
          "| anchor (needle) | audited line (v3) | patched line | patched line vs the audited line |",
          "|---|---|---|---|"]
    for a_ in r9_anchor:
        L.append(f"| {cell(a_['needle'])} | {a_['audited_line']} | {a_['patched_line'] if a_['patched_line'] else 'not found'} | "
                 + ("identical (sha256) |" if a_["line_identical"] else
                    f"changed by the patch{' in one sentence, the rest byte-identical' if fid_of.get(a_['audited_line'], ('', False))[1] else ''} ({fid_of.get(a_['audited_line'], ('findings below',))[0]}) |"))
    def _on(v_):
        return f"line{'s' if len(v_) != 1 else ''} {', '.join(map(str, v_))}"
    L += ["", "v3 printed the preprint's line numbers at `" + DEF_OUT + "@" + AUDIT_REV + "` in these forms, each now "
          "computed from its anchor's patched line (the table above): "
          + "; ".join(f"`{fm_}` on {_on(v_)}" for n_ in printed_at for fm_, v_ in printed_at[n_].items() if v_) + ". "
          + ("; ".join(f"'root:{n_}' on {_on(v_)}" for n_, v_ in quoted_root.items() if v_)
             + f" is the v1.7 checker note G6a.11's own locator ({LOC_G6A11}), quoted from the record, not one of this raw's anchors, so it is not re-anchored. "
             if any(quoted_root.values()) else "")
          + "Every other occurrence of these numbers in v3 is a round count, not a locator: "
          + ("; ".join(f"{n_} on {_on(v_)}" for n_, v_ in round_counts.items() if v_) or "none") + ".", "",
          "### Phrases this raw quotes from the preprint", "",
          "| phrase | patched line | on the audited line | on the patched line |",
          "|---|---|---|---|"]
    for q_ in r9_quote:
        L.append(f"| {cell(q_['phrase'])} | {q_['patched_line']} | {q_['on_audited']} | {q_['on_patched']} |")
    L += ["", "### Claims this raw makes about preprint sentences", "",
          "Swept from every v3 line that names the preprint or one of its lines (the forms above).", "",
          "| claim | where in this raw | patched line | held on the audited text | holds on the patched text |",
          "|---|---|---|---|---|"]
    for c_ in r9_claim:
        L.append(f"| {cell(c_['claim'])} | {cell(c_['where'])} | {c_['patched_line']} | {c_['held_on_audited']} | {c_['holds_on_patched']} |")
    L += ["", "### Findings on the patch (for the design seat; ruling 9; not a STOP)", ""]
    for f_ in r9_find:
        L += [f_["text"], ""]
    if not r9_find:
        L += ["None: every anchor, quoted phrase and claim holds on the patched text.", ""]
    J["round9_preprint"] = {"ruling": PREPRINT_V6_RULING, "preprint": PREPRINT, "sha256": p9_sha,
                            "sha256_of_record": PREPRINT_V6_SHA, "match": (p9_sha == PREPRINT_V6_SHA) if p9_sha else None,
                            "audited": {"block_abbrev": "d6431e97…222b8", "archived_untracked": PREPRINT_AUDITED,
                                        "archived_copy": arch_note, "required": False},
                            "anchors": r9_anchor, "v3_printed_at": {str(k_): v_ for k_, v_ in printed_at.items()},
                            "v3_quoted_g6a11_locator": {f"root:{k_}": v_ for k_, v_ in quoted_root.items() if v_},
                            "v3_round_counts_not_locators": {str(k_): v_ for k_, v_ in round_counts.items()},
                            "quotes": r9_quote, "claims": r9_claim, "findings_on_the_patch": r9_find}

    # ------------------------------------------ round 10: the preprint of record --
    # The PI's routing of 2026-10-12 (patch v7). Round 9's section above is
    # asserted equal to the round-9 record (this raw's JSON at R9_REV). Every
    # anchor, quoted phrase and claim is re-checked on v7; round 9's finding gets
    # its disposition on v7; each sentence patch v7 changed is a finding, with the
    # checks it alone flips (that sentence substituted alone into the v6 line) and
    # every figure it states in this item's scope checked against this item's
    # record at the precision written. A failing check is a finding on the patch
    # for the design seat, recorded, never raised.
    r9_rec = json.loads(git("show", f"{R9_REV}:{DEF_JSON}").decode())["round9_preprint"]
    r9_same = {k_: r9_rec[k_] == json.loads(json.dumps(v_, ensure_ascii=False, default=str))
               for k_, v_ in (("anchors", r9_anchor), ("quotes", r9_quote), ("claims", r9_claim),
                              ("findings_on_the_patch", r9_find))}
    assert all(r9_same.values()), f"round 9's section does not reproduce the round-9 record: {r9_same}"
    # every key of round9_preprint, reported against the record (asserted: the four above). 'sha256' and 'match' are the archived v6
    # copy's run-time hash and its match against ruling 9's value: null when that copy is absent or does
    # not match, so they equal the record only when the copy is present and matches.
    _r9_now = json.loads(json.dumps(J["round9_preprint"], ensure_ascii=False, default=str))
    r9_all = {k_: r9_rec.get(k_) == _r9_now.get(k_) for k_ in sorted(set(r9_rec) | set(_r9_now))}
    r9_runtime = ("sha256", "match")   # the archived v6 copy's
    r9_runtime_aud = ("audited",)      # its 'archived_copy' note records the archived audited copy's presence and hash
    # last pass: every other key equals the record whatever the archives' state
    assert all(v_ for k_, v_ in r9_all.items() if k_ not in r9_runtime + r9_runtime_aud), r9_all
    V6_REC, V7_REC = f"{PREPRINT_V6_SHA[:8]}…{PREPRINT_V6_SHA[-5:]}", PP_REC
    for nd_, op_ in PP_REANCHOR.items():   # the re-anchor sits on the needle's line on the audited and v6 texts, once on each text
        assert (lines_with(p9_text, op_) == [p9_n(nd_)] and op_ in r9_aud[PP_ANCHORS[nd_]]
                and len(lines_with(pp_text, op_)) == 1)

    def l7(nd: str):
        n7_ = pp_n(nd)
        return pp_lines[n7_ - 1] if isinstance(n7_, int) else None

    def l6(nd: str):
        return p9_lines[p9_n(nd) - 1]

    # sent10 (the v6 line with ONE v7 sentence substituted in, per changed
    # sentence, with its finding id) is built ahead of the sections above

    def flips(nd: str, fn):
        """(on v6, on v7, [ids of the v7 sentences that alone flip the check on the v6 line])."""
        v6_, v7_ = fn(l6(nd)), (fn(l7(nd)) if l7(nd) is not None else None)
        n6_ = p9_n(nd)
        by_ = [x_[0] for x_ in sent10 if x_[2] == n6_ and fn(x_[5]) != v6_] if v6_ != v7_ else []
        return v6_, v7_, by_

    r10_anchor = []
    for nd, n_aud in PP_ANCHORS.items():
        n6_, n7_ = p9_n(nd), pp_n(nd)
        on_, _, by_ = flips(nd, lambda t, nd=nd: nd in t)
        direct_ = bool(lines_with(pp_text, nd))
        r10_anchor.append({"needle": nd, "audited_line": n_aud, "v6_line": n6_, "v7_line": n7_ if isinstance(n7_, int) else None,
                           "needle_on_v7": direct_, "reanchored_by": None if direct_ else PP_REANCHOR.get(nd),
                           "reanchored_as": None if direct_ else PP_REANCHOR_KIND.get(nd),
                           "v7_line_identical_to_v6": isinstance(n7_, int) and pp_lines[n7_ - 1] == p9_lines[n6_ - 1],
                           "needle_removed_by": by_})
    r10_quote = []
    for q_ in r9_quote:
        v6_, v7_, by_ = flips(q_["anchor"], lambda t, ph=q_["phrase"]: ph in t)
        assert v6_ == q_["on_patched"]
        r10_quote.append({"phrase": q_["phrase"], "anchor": q_["anchor"], "v7_line": pp_n(q_["anchor"]),
                          "on_audited": q_["on_audited"], "on_v6": v6_, "on_v7": v7_, "flipped_by": by_})
    r10_claim = []
    # last pass: a claim's loci are the statements table's (RW10), where it has them; round 9's where-strings
    # stay in the Round 9 section, as asserted (its '§3a' for the length claim names a section with no statement
    # about the preprint; values-check R2-1's evidence carries that check)
    _rw_where = collections.defaultdict(list)
    for r_ in RW10:
        _rw_where[r_["check"]].append(r_["where"])
    for (where_, cl, nd, fn), c9_ in zip(claims, r9_claim):
        v6_, v7_, by_ = flips(nd, fn)
        assert c9_["claim"] == cl and v6_ == c9_["holds_on_patched"]
        r10_claim.append({"claim": cl, "where": "; ".join(_rw_where[cl]) if cl in _rw_where else where_,
                          "where_round9": where_, "anchor": nd, "v7_line": pp_n(nd),
                          "held_on_audited": c9_["held_on_audited"], "held_on_v6": v6_, "holds_on_v7": v7_, "flipped_by": by_})
    # the in-place statements' checks (run ahead of the sections, on the rebuilt v6 lines) agree with this
    # section's (on round 9's text); a claim's text names the same claim here
    _cl_by = {c_["claim"]: c_ for c_ in r10_claim}
    for r_, fn_ in zip(RW10, RW10_FN):
        assert flips(r_["anchor"], fn_) == (r_["held_on_v6"], r_["holds_on_v7"], r_["flipped_by"]), r_["where"]
        if r_["check"] in _cl_by:
            assert _cl_by[r_["check"]]["anchor"] == r_["anchor"] and _cl_by[r_["check"]]["flipped_by"] == r_["flipped_by"]

    # figures of the v7-changed sentences in this item's scope, against this item's record
    def dec(x: float, nd: int, signed: bool = False) -> str:
        """this run's value at nd decimals, as the preprint writes it (no leading zero)."""
        s_ = f"{x:+.{nd}f}" if signed else f"{x:.{nd}f}"
        return s_.replace("0.", ".", 1) if s_.lstrip("+-").startswith("0.") else s_
    gcal_doc = pinned_json("data/m/gates/G-CAL_model-free.json", POST_PIN_GCAL)
    gc1, gror = gcal_doc["conditions"]["1"], gcal_doc["renders_of_record"]
    g_floor = int(re.search(r">= (\d+) changed positions", gc1["rule"]).group(1))
    gcal_rule_ok = (gc1["verdict"] == "PASS" and gc1["n_pass"] == gc1["n"] == len(clean) == len(gror["items"])
                    and not gc1["failing_items"])
    assert gcal_rule_ok == all(it_["n_changed"] >= g_floor for it_ in gror["items"])   # counts only (no render text, no gold)
    _gp = "data/m/gates/G-CAL_model-free.json"
    gcal_blob_same = git("rev-parse", f"{POST_PIN_GCAL}:{_gp}") == git("rev-parse", f"HEAD:{_gp}")
    LOC_M23 = loc('PROPOSAL-m-gating-campaign-v1_11.md', '**2.3 Dose')
    # Round 10, last pass: the corruptor's floor and 'every item' are on the record AT THE PIN (PROPOSAL-m
    # §2.3, its [C]-tagged n_eligible sentence, and §0.4); G-CAL's post-pin artifact adds the committed
    # model-free measurement (condition (1)) and the renders' sha256. Render texts are read only to recompute
    # that sha256, to compare the three renders §2.3 quotes at the pin, and to assert that no render equals its
    # clean item; none is printed; no gold is read.
    _pm = "PROPOSAL-m-gating-campaign-v1_11.md"
    LOC_M04 = loc(_pm, '**0.4 Welfare.**')
    _m176, _m48 = line_at(_pm, '**2.3 Dose'), line_at(_pm, '**0.4 Welfare.**')
    _kq = "k = clip(floor(0.15·n_eligible + 0.5), 3, floor(n_eligible/2))"
    _nvq, _rkq, _m48q = "never the original", "every item reaches k, with one roster-substring skip (item 7)", "≥ 3 changed letters per item"
    _nel_m = re.search(r"n_eligible under the operand exclusion, items 0–15 \(\[C\], STOP-6 §E\): ([\d, ]+?) \(", _m176)
    m_nel = [int(x_) for x_ in _nel_m.group(1).split(", ")] if _nel_m else []
    m_k = [min(max(math.floor(0.15 * n_ + 0.5), 3), n_ // 2) for n_ in m_nel]
    m_q = dict((int(i_), r_) for i_, r_ in re.findall(r"item (\d+) `([^`]+)`[,.]? ?", _m176.split("on Code's three re-rendered items")[-1].split(" — all three golds")[0]))
    m_floor_ok = (_kq in _m176 and _nvq in _m176 and _rkq in _m176 and _m48q in _m48 and len(m_nel) == len(clean)
                  and min(m_k) >= g_floor and f"k sums to {sum(m_k)}" in _m176 and sorted(m_q) == [5, 11, 15])
    _c_sent = _m176[_m176.index("([C], STOP-6 §E)"):]
    m_floor_ok = m_floor_ok and _rkq in _c_sent and _c_sent.index(_rkq) < _c_sent.index(". ")   # the same sentence
    _gsrc = pinned_text("valence_core/m/gcal.py", POST_PIN_GCAL)
    _gj = 'joined = "\\n".join(renders).encode("utf-8")'
    _gl = lines_with(_gsrc, _gj)[0]
    assert _gsrc.split("\n")[_gl].strip() == "sha = _sha256_bytes(joined)"
    LOC_GSHA = f"valence_core/m/gcal.py@{POST_PIN_GCAL}:{_gl}-{_gl + 1}"
    _grs = [it_["render"] for it_ in gror["items"]]
    gcal_sha_ok = sha256_bytes("\n".join(_grs).encode("utf-8")) == gror["renders_sha256"]
    gcal_vs_pin = (gror["n_eligible"] == m_nel and gror["k"] == m_k and gror["k_sum"] == sum(m_k)
                   and gcal_doc["provenance"]["proposal_sha256"] == sha256_bytes(pinned(_pm)))
    gcal_q_same = all(_grs[i_] == r_ for i_, r_ in m_q.items())
    assert all(it_["render"] != it_["clean"] for it_ in gror["items"]) == gcal_rule_ok   # none is its clean item
    # 'fewer corrupted deliveries than nominal' is this raw's own wording at R9_REV (P9-1's observation (4)), not
    # the cycle record's
    _p91 = next(f_["text"] for f_ in r9_rec["findings_on_the_patch"] if f_["id"] == "P9-1")
    _r9_obs4 = _p91[_p91.index(" (4) "):_p91.index(" (5) ")]
    corr_rate = corrupt_f1.__defaults__[0]
    sham_hi = max(rates, key=rates.get) == "sham"
    clean_on_zero = set(by_item_clean) == set(zero_items) and sum(by_item_clean.values()) == len(clean_q)
    sign_w = "longer" if hard_longer > easy_longer and task_len["DIFF_hard"] > task_len["DIFF_easy"] else "shorter"
    FIG10 = {  # name -> [(phrase as the record gives it, extra condition, this item's record)]
        "length-deflation sign": [
            (f"a preference for {sign_w} rounds, the direction that could mimic the lean", True,
             f"§3a direction check and Note 5: hard was the longer config in {hard_longer}/{len(dsess)} valid DIFF sessions "
             f"(task texts too, pool means {task_len['DIFF_easy']:.1f} vs {task_len['DIFF_hard']:.1f} characters), so the "
             f"deflation that could mimic the toward-hard lean is a longer-rounds preference; the record's test is two-sided")],
        "corruption clause": [
            (f"({dec(corr_rate, 2)})", TARGET["CORR"][1].endswith(f"rate {dec(corr_rate, 2)})"),
             f"f1's corruptor rate {corr_rate} (corrupt_f1, {ports['corrupt()']}; replay equal to calib.json corr_sha, §7c); "
             f"pre-registered target: '{TARGET['CORR'][1]}'"),
            (f"{len(zero_items)} of {len(clean)} items rendered unchanged", True,
             f"§7c: items with 0 changed {zero_items} (replay equal to the transcript-derived vector); §7d's proposed wording"),
            (f"so {len(clean_q)} of {n_q} corrupted-label rounds across all {len(corr_rows)} CORR sessions delivered clean text",
             clean_on_zero and len(corr_rows) == by_arm["CORR"],
             f"§7c/§7d: {len(clean_q)}/{n_q} byte-clean Q rounds over all {by_arm['CORR']} CORR sessions, excluded ones "
             f"included; they are the Q rounds on items {zero_items} exactly (by item {dict(sorted(by_item_clean.items()))}), "
             f"so 'so' holds; §7d's proposed wording"),
            (f"{len(one_clean_valid)} of the {vby['CORR']} valid sessions saw one corrupted task rather than two before the first choice",
             clean_pre.get(2, 0) == 0,
             f"§7c/§7d: {len(one_clean_valid)}/{vby['CORR']} valid CORR sessions with one byte-clean pre-pick Q round of "
             f"the two each saw, none with two; §7d's proposed wording"),
            ("fewer corrupted deliveries than nominal", "fewer corrupted deliveries than nominal" in _r9_obs4,
             f"no figure: the delivery reading of §7c's counts (this raw's words at {R9_REV}, round 9's P9-1 "
             f"observation (4))"),
            (f"the gating campaign’s corruptor (PROPOSAL-m §2.3; G-CAL, `{_gp}`) changes at least "
             f"{ {3: 'three'}.get(g_floor, str(g_floor)) } letters of every item, so no render is clean",
             m_floor_ok and gcal_rule_ok and gcal_blob_same and gcal_sha_ok and gcal_vs_pin and gcal_q_same,
             f"At the pin: PROPOSAL-m §2.3 ({LOC_M23}) gives '{_kq}', each replacement '{_nvq}', and n_eligible "
             f"for items 0–15 ([C], STOP-6 §E) {', '.join(map(str, m_nel))}: minimum {min(m_nel)}, so the formula "
             f"gives k ≥ {min(m_k)} for every item (k sums to {sum(m_k)}, as §2.3 states); the same [C]-tagged "
             f"sentence states '{_rkq}'; §0.4 ({LOC_M04}) states '{_m48q}' (checked on the pinned lines: {m_floor_ok}). "
             f"Post-pin (read-only): `{_gp}`@{POST_PIN_GCAL} (blob at HEAD equal to {POST_PIN_GCAL}'s: "
             f"{gcal_blob_same}; its proposal_sha256 equal to PROPOSAL-m's at the pin, and its n_eligible and k equal "
             f"to §2.3's: {gcal_vs_pin}): condition (1) rule '{gc1['rule']}', {gc1['n_pass']}/{gc1['n']} items, "
             f"{gc1['verdict']}, failing items {gc1['failing_items']}; renders of record: '{gror['rule']}', "
             f"{len(gror['items'])} items, each meeting condition (1), so none is its clean item; renders_sha256 "
             f"`{gror['renders_sha256']}` (recomputed here over the renders joined by newlines, {LOC_GSHA}: "
             f"{gcal_sha_ok}); items {', '.join(map(str, sorted(m_q)))} as §2.3 quotes them, byte-identical to "
             f"the renders of record: {gcal_q_same}. Condition (1) is quoted in §7b")],
        "first-choice scope": [
            (f"{dec(fb['delta_exact'], 3, True)}: no evaluation-seeking at the first choice", True,
             f"the 'FDBK +.023' row: {fb['k']}/{fb['n']}, the first free choice (§5: the pre-registered primary, the only "
             f"free pick made before any free-phase verdict); Note 3")],
        "termination counter": [
            (f"about {100 * tot_t / tot_n:.0f}% of rounds overall", True,
             f"§4 and the overall row ('termination attempts ≈ 1% of rounds (overall)', reproduced): {tot_t}/{tot_n} = "
             f"{100 * tot_t / tot_n:.2f}%"),
            (f"{100 * min(rates.values()):.1f}–{100 * max(rates.values()):.1f}% by arm", True,
             f"§4: 'By arm the rate runs {100 * min(rates.values()):.1f}%-{100 * max(rates.values()):.1f}%' and §4's "
             f"suggested wording"),
            ("the sham arm highest", sham_hi,
             f"§4: sham's {per_arm_t['sham']}/{per_arm_n['sham']} = {100 * rates['sham']:.2f}% is the highest"),
            (f"no detectable heterogeneity on a post-hoc exact test, p = {dec(p_hom, 2)}", True,
             f"§4 POST-HOC (computed-new; the homogeneity row): p = {p_hom:.4f}; §4's suggested wording 'no detectable "
             f"heterogeneity across arms, post-hoc exact p = {p_hom:.2f}'")],
        "exploration share": [
            (f"session share {dec(shares[lo_a], 2)}–{dec(shares[hi_a], 2)}", True,
             f"§5 (computed-new; share of all free picks to P, valid sessions): {shares[lo_a]:.3f} ({lo_a}) to "
             f"{shares[hi_a]:.3f} ({hi_a}); §5's proposal 'the range ({shares[lo_a]:.2f}-{shares[hi_a]:.2f})'"),
            ("the verdict-line arm highest", hi_a == "FDBK" and TARGET["FDBK"][0] == "truthful verdict line",
             f"§5: the highest share is {hi_a}'s {shares[hi_a]:.3f}; FDBK's P config is the '{TARGET['FDBK'][0]}' (§3)")],
    }
    ROWS10 = {"length-deflation sign": ["DIFF length-preference deflation test (tested and failed)"],
              "corruption clause": ["CORR dose caveat: known artifact at 0.12? (yes/no)",
                                    "preprint 'at a dose a later calibration (§8.1) found below its visibility criterion'"],
              "first-choice scope": ["FDBK +.023"],
              "termination counter": ["termination attempts ≈ 1% of rounds (overall)", "termination attempts ≈ 1% of rounds by arm",
                                      "termination 'uniformly across arms including sham' (preprint wording)"],
              "exploration share": ["exploration share ≈ .50 by arm", "FDBK all-picks share toward the verdict config (POST-HOC)"]}
    fig_status = {f_["figure"]: f_["status"] for f_ in FIG}
    _lb_h, _lb_x = "termination 'uniformly across arms including sham' (preprint wording)", "exploration share ≈ .50 by arm"
    _lb_b = "termination attempts ≈ 1% of rounds by arm"
    BASIS10 = {  # figures whose basis is not a `reproduced` row: computed-new, a discrepant row's counts, a post-pin artifact
        FIG10["length-deflation sign"][0][0]: "computed-new: §3a's direction check (Code's, post-hoc, descriptive)",
        FIG10["termination counter"][1][0]: f"{fig_status[_lb_b]}: the row '{_lb_b}' (its per-arm counts; the record states no per-arm rate)",
        FIG10["termination counter"][2][0]: f"{fig_status[_lb_b]}: the row '{_lb_b}' (its per-arm counts; the record states no per-arm rate)",
        FIG10["termination counter"][3][0]: f"{fig_status[_lb_h]}: the row '{_lb_h}'",
        FIG10["exploration share"][0][0]: f"{fig_status[_lb_x]}: the row '{_lb_x}'",
        FIG10["exploration share"][1][0]: f"{fig_status[_lb_x]}: the row '{_lb_x}'",
        FIG10["corruption clause"][5][0]: (f"pinned: PROPOSAL-m §2.3 ({LOC_M23}: the floor of {min(m_k)} in k's formula "
                                           f"and the [C]-tagged 'every item reaches k') and §0.4 ({LOC_M04}); post-pin: "
                                           f"G-CAL's artifact ({POST_PIN_GCAL}: condition (1) {gc1['n_pass']}/{gc1['n']} "
                                           f"{gc1['verdict']}, the renders' sha256)"),
    }
    assert all(lb_ in fig_status for v_ in ROWS10.values() for lb_ in v_) and set(FIG10) == set(ROWS10) == {x_[1] for x_ in sent10}
    r10_fig = []
    for (fid, nm_, n_, s6_, s7_, _) in sent10:
        for (ph_, cond_, rec_) in FIG10[nm_]:
            r10_fig.append({"finding": fid, "sentence": nm_, "phrase": ph_, "on_v7": ph_ in s7_,
                            "condition_holds": bool(cond_), "carried": ph_ in s7_ and bool(cond_), "record": rec_,
                            "basis": BASIS10.get(ph_)})

    # round 9's finding on the patch, on v7 (the round-9 record, R9_REV)
    obs9 = [  # round 9's observations on the corruption clause (their predicates, as round 9 raised them)
        ("1", "the 306's domain (all 64 CORR sessions, excluded ones included) not named", lambda s_: "64" not in s_),
        ("2", "the dose named twice", lambda s_: s_.count("dose") >= 2 and "a later calibration (§8.1)" in s_),
        ("3", "a second, present-tense calibration attribution ('which the gating campaign’s dose calibration corrects')",
         lambda s_: bool(re.search(r"which the gating campaign\S* dose calibration corrects", s_))),
        ("4", "'so the contrast ran weaker than nominal', an inference beyond the delivery counts",
         lambda s_: "so the contrast ran weaker than nominal" in s_),
        ("5", "the kept clause attaching ambiguously after 'corrects'",
         lambda s_: bool(re.search(r"which the gating campaign\S* dose calibration corrects", s_))
         and "corrects, at a dose a later calibration (§8.1)" in s_),
    ]
    r10_disp, r10_disp_txt = [], []
    for f9 in r9_rec["findings_on_the_patch"]:
        s9_ = f9.get("new")
        hit_ = [x_ for x_ in sent10 if x_[3] == s9_]
        assert hit_ and "Observations for the design seat: (1)" in f9["text"], "round 9's finding is not the registered one"
        fid7, nm7, n7_, _, s7_, _ = hit_[0]
        disp_ = "unchanged" if s9_ in pp_lines[n7_ - 1] else "changed"
        chk_ = [{"check": c_, "fails_on_v6": True,
                 "fails_on_v7": next(x_ for x_ in r10_claim if x_["claim"] == c_)["holds_on_v7"] is not True}
                for c_ in f9["checks_failed"]]
        bcf_ = [{"phrase": p_, "on_v6": p_ in s9_, "on_v7": p_ in s7_}
                for p_ in (f"{len(clean_q)} of {n_q}", f"{len(one_clean_valid)} of the {vby['CORR']} valid sessions")]
        ob_ = [{"observation": k_, "what": w_, "raised_on_v6": fn_(s9_), "raised_on_v7": fn_(s7_),
                "disposition": "unchanged" if fn_(s7_) else "resolved"} for (k_, w_, fn_) in obs9]
        assert all(o_["raised_on_v6"] for o_ in ob_), "round 9's observations do not reproduce on v6"
        held9 = [c_ for c_ in r10_claim if c_["anchor"] in PP_ANCHORS and PP_ANCHORS[c_["anchor"]] == f9["audited_line"]
                 and c_["held_on_v6"] is True]
        r10_disp.append({"id": f9["id"], "disposition": disp_, "v6": s9_, "v7": s7_, "v7_sentence_finding": fid7,
                         "checks_failed": chk_, "byte_clean_figures": bcf_, "observations": ob_,
                         "claims_that_held": [{"claim": c_["claim"], "holds_on_v7": c_["holds_on_v7"], "flipped_by": c_["flipped_by"]}
                                              for c_ in held9]})
        r10_disp_txt.append(
            f"**{f9['id']} (line {f9['patched_line']}) on v7: {disp_}.** Round 9's finding is the {nm7} as patch v6 wrote "
            + (f"it; patch v7 rewrites that sentence ({fid7}). " if disp_ == "changed" else "it; patch v7 keeps that sentence. ")
            + f"Old (v6 {V6_REC}, line {f9['patched_line']}): "
            f"'{s9_}' New (v7 {V7_REC}, line {n7_}): '{s7_}' "
            + "Its failing check on v7: " + "; ".join(
                f"'{c_['check']}' still fails (unchanged: the byte-clean delivery stays carried)" if c_["fails_on_v7"]
                else f"'{c_['check']}' holds again (the byte-clean delivery dropped)" for c_ in chk_)
            + "; its figure checks on v7: " + "; ".join(f"'{b_['phrase']}' {b_['on_v7']}" for b_ in bcf_)
            + " (§7c). Its observations on v7: "
            + " ".join(f"({o_['observation']}) {o_['what']}: {o_['disposition']}." for o_ in ob_)
            + " The claims round 9 found still holding on this line: "
            + "; ".join(f"'{c_['claim']}' {'holds' if c_['holds_on_v7'] else 'no longer holds'} on v7"
                        + (f" ({', '.join(c_['flipped_by'])})" if c_["flipped_by"] else "") for c_ in held9)
            + ". Statuses carried, never upgraded; whether patch v7 discharges a row is the design seat's and the PI's.")

    # findings on patch v7: one per changed sentence
    r10_find = []
    for (fid, nm_, n_, s6_, s7_, _) in sent10:
        cf_ = [c_ for c_ in r10_claim if fid in c_["flipped_by"]]
        qf_ = [q_ for q_ in r10_quote if fid in q_["flipped_by"]]
        af_ = [a_ for a_ in r10_anchor if fid in a_["needle_removed_by"]]
        fg_ = [g_ for g_ in r10_fig if g_["finding"] == fid]
        rows_ = [f"'{lb_}' ({fig_status[lb_]})" for lb_ in ROWS10[nm_]]
        obs_ = []
        if nm_ == "corruption clause":
            obs_.append(f"The G-CAL artifact the sentence cites first exists at {POST_PIN_GCAL}, after the pin (§7d); at "
                        f"{POST_PIN_GCAL} its condition (3) reads '{gcal_doc['conditions']['3']}' and its condition (4) "
                        f"'{gcal_doc['conditions']['4']}'; the sentence states condition (1) only, which is structural "
                        f"(model-free), not a measurement on the model")
            _c10 = {c_["claim"]: c_["holds_on_v7"] for c_ in r10_claim}
            _fl = f"{16 - len(ge3)} of 16 items fell below the three-letter floor"
            obs_.append("The audited clause the dose row's label quotes ('at a dose a later calibration (§8.1) found below "
                        "its visibility criterion') is no longer in the preprint. On v7: the attribution §7d (i) flags, "
                        + ("gone" if _c10["the CORR dose clause attributes the finding to a calibration (§8.1)"] is False else "kept")
                        + "; the later calibration's criterion §7d (ii) flags, "
                        + ("gone" if _c10["the CORR dose clause's criterion is the later calibration's ('its visibility criterion'), which §7d (ii) finds is m's, not f1's"] is False else "kept")
                        + f"; v7 takes §7d's proposed delivery wording (the figures above) "
                        + ("with" if _fl in s7_ else "without") + f" its last clause ('{_fl} of the later campaign', §7d) and "
                        f"states the campaign's corruptor instead, citing G-CAL's artifact (stage '{gcal_doc['stage']}'), "
                        "as §7d asked should the sentence keep 'a later calibration' (v7 does not keep it)")
            # fix round (finding 5): what v7's line-1 attribution to the N5 raw covers, read off this raw as
            # committed at R9_REV (no G-CAL renders-of-record support there; only the f1 replay and m's rule)
            _r9_md = git("show", f"{R9_REV}:{DEF_OUT}").decode()
            _gc_words = ("renders of record", "renders_of_record", "three letters of every item", "no render is clean",
                         "every item reaches k", "n_eligible", "changed letters per item")
            _gc_prior = [w_ for w_ in _gc_words if w_ in _r9_md]
            _gc_f1 = "`f1_012`" in _r9_md and "condition (1) 'every item ≥ 3 changed positions'" in _r9_md
            _l1q = "restated from the audit’s N5 raw"
            assert _gc_f1 and not _gc_prior, "this raw at R9_REV is not the one this observation describes"
            _l1c = _l1q in pp_lines[0] and "corruption clause" in pp_lines[0]
            _pre10 = "\n".join(L)   # the sections before Round 10, as this run wrote them
            _m23l = [x_ for x_ in _pre10.split("\n") if LOC_M23 in x_]
            assert (len(_m23l) == 2 and _m23l[0].startswith("- CORR") and "+.078" in _m23l[0]
                    and _m23l[1].startswith("- PROPOSAL-m §2.3: condition (1)") and "replay" in _m23l[1]
                    and LOC_M04 not in _pre10
                    and not any(w_ in _pre10 for w_ in (_kq, _rkq, _m48q, _nvq, "every item reaches k", "n_eligible")))
            # recheck (finding 3): §7b quotes condition (1)'s floor as the campaign's visibility criterion only
            _f7b = re.search(r"'the floor of (\d+) is the visibility criterion'", _m23l[1])
            assert _f7b and "'every item ≥ " + _f7b.group(1) + " changed positions'" in _m23l[1]
            obs_.append(f"v7's line 1 says the f1 line's corruption clause, with four other restatements, is "
                        f"{'' if _l1c else '(not found on line 1) '}'{_l1q}'. That covers "
                        "its delivery figures (§7c, and §7d's proposed wording, in this raw as committed at "
                        f"{R9_REV}) but not its G-CAL clause ('changes at least three letters of every item, so no render "
                        f"is clean'): this raw at {R9_REV} read G-CAL's artifact for its replay of f1's corruptor only "
                        "(`f1_012`, §7c) and quoted PROPOSAL-m's condition (1) as the campaign's rule (§7b); none of "
                        + ", ".join(f"'{w_}'" for w_ in _gc_words) + " is in it. The clause's floor and its 'every item' "
                        f"are on the record at the pin: PROPOSAL-m §2.3 ({LOC_M23}; k's formula with its floor of "
                        f"{min(m_k)}, each replacement '{_nvq}', n_eligible at least {min(m_nel)} for every item, so k ≥ "
                        f"{min(m_k)} for each, and the "
                        f"[C]-tagged '{_rkq}') and §0.4 ({LOC_M04}; '{_m48q}'). G-CAL's post-pin artifact "
                        f"({POST_PIN_GCAL}) adds the committed model-free measurement (condition (1), "
                        f"{gc1['n_pass']}/{gc1['n']} {gc1['verdict']}) and the renders' sha256 "
                        f"(`{gror['renders_sha16']}…`). This raw cites that support first in this Round 10 section "
                        "(the figures table above), the pinned record first; before it, this raw cites §2.3 only for "
                        "the +.078 covariate (§6) and, in §7b, for condition (1) and its floor of "
                        f"{_f7b.group(1)} as the campaign's visibility criterion and for G-CAL's replay of f1's "
                        f"corruptor; never for k's formula, its '{_nvq}', the n_eligible list, §0.4 or the [C]-tagged "
                        "'every item reaches k' (asserted)")
        cn_ = [g_ for g_ in fg_ if (g_["basis"] or "").startswith("computed-new")]
        if cn_:
            obs_.append("Figures resting on a computation the f1 record does not contain, committed only in this raw: "
                        + "; ".join(f"'{g_['phrase']}' ({g_['basis']})" for g_ in cn_))
        txt = (f"**{fid} (line {n_}; the {nm_}, as v7's line-1 patch note names it).** Old (v6 {V6_REC}, line {n_}): "
               f"'{s6_}' New (v7 {V7_REC}, line {n_}): '{s7_}' Checks of this raw that held on v6 and fail on v7, this "
               "sentence alone flipping them: "
               + ("; ".join(f"{c_['claim']} ({c_['where']})" for c_ in cf_) or "none")
               + "; quoted phrases absent from v7: " + ("; ".join(f"'{q_['phrase']}'" for q_ in qf_) or "none")
               + "; anchors whose needle v7 removed: "
               + ("; ".join(f"'{a_['needle']}' (re-anchored by {a_['reanchored_as']}, '{a_['reanchored_by']}', line {a_['v7_line']})" for a_ in af_) or "none")
               + ". Figures of the v7 sentence in this item's scope: "
               + "; ".join(f"'{g_['phrase']}' {'carried' if g_['carried'] else 'NOT carried'}" for g_ in fg_)
               + " (table above). " + ("Observations for the design seat: "
                                      + " ".join(f"({k_}) {o_}." for k_, o_ in enumerate(obs_, start=1)) + " " if obs_ else "")
               + f"Related rows keep their statuses ({'; '.join(rows_)}): statuses are carried, never upgraded; whether "
               "patch v7 discharges a row is the design seat's and the PI's.")
        r10_find.append({"id": fid, "sentence": nm_, "line": n_, "v6": s6_, "v7": s7_,
                         "checks_failed": [c_["claim"] for c_ in cf_], "phrases_absent": [q_["phrase"] for q_ in qf_],
                         "needles_removed": [a_["needle"] for a_ in af_],
                         "figures_not_carried": [g_["phrase"] for g_ in fg_ if not g_["carried"]],
                         "related_rows": {lb_: fig_status[lb_] for lb_ in ROWS10[nm_]}, "observations": obs_, "text": txt})
    unatt = ([c_["claim"] for c_ in r10_claim if c_["holds_on_v7"] != c_["held_on_v6"] and len(c_["flipped_by"]) != 1]
             + [q_["phrase"] for q_ in r10_quote if q_["on_v7"] != q_["on_v6"] and len(q_["flipped_by"]) != 1]
             + [a_["needle"] for a_ in r10_anchor if not a_["needle_on_v7"] and len(a_["needle_removed_by"]) != 1])
    for x_ in unatt:
        fid = f"P10-{len(r10_find) + 1}"
        r10_find.append({"id": fid, "check": x_, "text": f"**{fid}.** '{x_}' changes between v6 and v7 but is not flipped by exactly one registered sentence."})
    notc = [g_ for g_ in r10_fig if not g_["carried"]]

    line1_names = [(x_[1], x_[1] in pp_lines[0]) for x_ in sent10]
    L += ["## Round 10 (2026-10-12): the preprint of record re-pointed at patch v7 (" + PREPRINT_RULING + ")", "",
          f"- Preprint of record: `{PREPRINT}` (root, untracked; committed at the tag) sha256 `{pp_sha}`, computed at run "
          f"time and asserted in full before anything was written; the routing gives `{V7_REC}` (patch v7): "
          f"{'MATCH' if pp_match else 'MISMATCH'}. Round 9's preprint of record, patch v6 (`{V6_REC}`, ruling 9), is "
          f"archived untracked at `{PREPRINT_V6}`, out of the release; it is not required. Archived v6 copy: {v6_note}.",
          f"- v7 against v6 on this raw's anchor lines: line 182 differs in {len(v6_rb[182][1])} sentences, the rest "
          f"byte-identical (the registered v6 sentences substituted back reproduce v6's line-182 sha256 "
          f"`{PP_V6_LINE_SHA[182][:16]}`); line 268 identical (sha256 `{PP_V6_LINE_SHA[268][:16]}`, also the audited line's). "
          f"v7's line 1 (the patch note) attributes restatements on the f1 line to the audit's N5 raw ('N5 raw' on line 1: "
          f"{'N5 raw' in pp_lines[0]}) and names five; each names one changed sentence (P10-1 to P10-{len(sent10)}): "
          + "; ".join(f"'{nm_}' {ok_}" for nm_, ok_ in line1_names) + ".",
          "- Scope: the preprint handling only. Round 9's section above is reproduced on the v6 text and equals the "
          f"round-9 record (`{DEF_JSON}@{R9_REV}`, key `round9_preprint`; asserted: "
          + ", ".join(f"{k_} {v_}" for k_, v_ in r9_same.items()) + "; every key, reported: "
          + ", ".join(f"{k_} {v_}" for k_, v_ in r9_all.items()) + f"). Of that key, {' and '.join(r9_runtime)} are the "
          "archived v6 copy's run-time hash and its match against ruling 9's value: null when that copy is absent or "
          f"does not match; {' and '.join(r9_runtime_aud)} records the archived audited copy's presence and hash (its "
          "'archived_copy' note), and differs from the record when that copy is absent or does not match. These keys "
          "depend on the archives' state at run time and lie outside the asserted equality; every other key equals "
          "the record (asserted).",
          f"- The sections before Round 9 word each statement about a preprint sentence against the text its check "
          f"holds on (round 9's mechanism for §7d (iii) and the dose row, carried): patch v7 flips the check of "
          f"{sum(r_['reworded'] for r_ in RW10)} of the {len(RW10)} statements below, and each of those is worded "
          "against the audited and v6 texts; in prose it names the v7 finding, and in a figure row's note or source "
          f"({sum(r_['reworded'] and r_['figure_row'] for r_ in RW10)} of them) it names the audited text and the patched text that preceded the preprint of record "
          "(that is, the audited and v6 texts), and the preprint of record, and points to the closing sections, so "
          "that the row gains no digit (asserted). "
          + (f"{sum(not r_['reworded'] for r_ in RW10)} keep their wording. " if any(not r_["reworded"] for r_ in RW10)
             else "None keeps its earlier wording. ")
          + "Figure rows: labels, values and statuses unchanged. Locators resolve on v7, two through re-anchoring "
          "(below). "
          "No status changed (statuses are carried, never upgraded). A check that fails on v7 is a finding on the "
          "patch for the design seat (ruling 9's form, carried by the routing of 2026-10-12), not a STOP.",
          "",
          "### Statements of the sections before Round 9 about preprint sentences, on v7", "",
          "| where in this raw | check | v7 line | held on v6 | holds on v7 | worded against | flipped on v7 by |",
          "|---|---|---|---|---|---|---|"]
    for r_ in RW10:
        _wa = ("the preprint of record" if not r_["reworded"] else
               "the audited text and the patched text that preceded the preprint of record (the audited and v6 texts); 'a finding on the patch, closing sections' (figure row: no digit added)"
               if r_["figure_row"] else "the audited and v6 texts; names the v7 finding")
        L.append(f"| {cell(r_['where'])} | {cell(r_['check'])} | {r_['v7_line']} | {r_['held_on_v6']} | "
                 f"{r_['holds_on_v7']} | {_wa} | {', '.join(r_['flipped_by']) or '-'} |")
    L += ["",
          "### Anchors on v7", "",
          "| anchor (needle) | audited line | v6 line | v7 line | needle on v7 | located on v7 by | v7 line vs v6 line |",
          "|---|---|---|---|---|---|---|"]
    for a_ in r10_anchor:
        L.append(f"| {cell(a_['needle'])} | {a_['audited_line']} | {a_['v6_line']} | {a_['v7_line'] or 'not found'} | "
                 f"{a_['needle_on_v7']} | "
                 + ("its needle" if a_["needle_on_v7"] else
                    f"{a_['reanchored_as']}: '{cell(a_['reanchored_by'])}' (same line on the audited and v6 texts; needle removed by {', '.join(a_['needle_removed_by'])})")
                 + " | " + ("identical" if a_["v7_line_identical_to_v6"] else
                            f"changed by patch v7 in {len(v6_rb[a_['v6_line']][1])} sentences, the rest byte-identical") + " |")
    L += ["", "### Phrases this raw quotes from the preprint, on v7", "",
          "| phrase | v7 line | on the audited line | on the v6 line | on the v7 line | flipped on v7 by |",
          "|---|---|---|---|---|---|"]
    for q_ in r10_quote:
        L.append(f"| {cell(q_['phrase'])} | {q_['v7_line']} | {q_['on_audited']} | {q_['on_v6']} | {q_['on_v7']} | "
                 f"{', '.join(q_['flipped_by']) or '-'} |")
    _md_so_far = "\n".join(L)
    _s3a = _md_so_far[_md_so_far.index("### 3a."):_md_so_far.index("### 3b.")]
    _len_cl = CLAIMS9["unsigned"][0]
    assert ("preprint" not in _s3a.lower() and "§3a" in next(c_ for c_ in r10_claim if c_["claim"] == _len_cl)["where_round9"]
            and "§3a" not in _rw_where[_len_cl] and "values-check R2-1's evidence" in _rw_where[_len_cl])
    L += ["", "### Claims this raw makes about preprint sentences, on v7", "",
          f"The 'where in this raw' column gives a claim's loci as the statements table above lists them "
          f"({sum(c_['claim'] in _rw_where for c_ in r10_claim)} of the {len(r10_claim)} claims; "
          + ("the other keeps" if sum(c_["claim"] not in _rw_where for c_ in r10_claim) == 1 else "the others keep")
          + " round 9's); round 9's where-strings stay in the Round 9 section, as asserted. There the length claim's "
          "'§3a' names a section that makes no statement about the preprint; values-check R2-1's evidence carries "
          "that check.", "",
          "| claim | where in this raw | v7 line | held on the audited text | held on v6 | holds on v7 | flipped on v7 by |",
          "|---|---|---|---|---|---|---|"]
    for c_ in r10_claim:
        L.append(f"| {cell(c_['claim'])} | {cell(c_['where'])} | {c_['v7_line']} | {c_['held_on_audited']} | "
                 f"{c_['held_on_v6']} | {c_['holds_on_v7']} | {', '.join(c_['flipped_by']) or '-'} |")
    L += ["", "### Figures of the v7-changed sentences in this item's scope, against this item's record", "",
          "Each phrase is built from this run's value at the precision the v7 sentence writes and must be on the v7 "
          "sentence; the record column names the committed computation (this raw's section) that carries it.", "",
          "| finding | phrase (this run's value, as v7 writes it) | on the v7 sentence | record condition | carried | this item's record | basis, where not a `reproduced` row |",
          "|---|---|---|---|---|---|---|"]
    for g_ in r10_fig:
        L.append(f"| {g_['finding']} | {cell(g_['phrase'])} | {g_['on_v7']} | {g_['condition_holds']} | "
                 f"{g_['carried']} | {cell(g_['record'])} | {cell(g_['basis'] or '-')} |")
    L += ["", f"Figures of a v7-changed sentence not carried by this item's record: "
          + ("; ".join(f"'{g_['phrase']}' ({g_['finding']})" for g_ in notc) or "none") + ".",
          "", "### Round 9's finding on the patch, on v7", ""]
    for t_ in r10_disp_txt:
        L += [t_, ""]
    L += ["### Findings on patch v7 (for the design seat; not a STOP)", ""]
    for f_ in r10_find:
        L += [f_["text"], ""]
    if not r10_find:
        L += ["None: every anchor, quoted phrase and claim holds on v7 as on v6.", ""]
    J["round10_preprint"] = {"routing": PREPRINT_RULING, "preprint": PREPRINT, "sha256": pp_sha,
                             "sha256_of_record": PREPRINT_SHA, "match": pp_match,
                             "v6": {"ruling": PREPRINT_V6_RULING, "sha256_of_record": PREPRINT_V6_SHA,
                                    "sha256_computed": p9_sha, "archived_untracked": PREPRINT_V6,
                                    "archived_copy": v6_note, "required": False},
                             "round9_reproduced_equal_to_record": {"rev": R9_REV, **r9_same},
                             "round9_key_by_key_vs_record": {"rev": R9_REV, "asserted": sorted(r9_same), "equal": r9_all,
                                                             "runtime_fields_null_when_v6_copy_absent": list(r9_runtime),
                                                             "runtime_fields_by_archived_copy": {
                                                                 PREPRINT_V6: list(r9_runtime),
                                                                 PREPRINT_AUDITED: list(r9_runtime_aud)}},
                             "statements_in_place": RW10,
                             "line1_names": dict(line1_names), "anchors": r10_anchor, "quotes": r10_quote,
                             "claims": r10_claim, "figures": r10_fig, "round9_dispositions": r10_disp,
                             "findings_on_the_patch": r10_find}

    os.makedirs(os.path.dirname(out_md), exist_ok=True)
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    with open(out_js, "w", encoding="utf-8") as f:
        json.dump(J, f, indent=1, ensure_ascii=False, default=str)
    print(f"wrote {os.path.relpath(out_md, REPO)} and {os.path.relpath(out_js, REPO)}; {len(FIG)} figures")


if __name__ == "__main__":
    main()
