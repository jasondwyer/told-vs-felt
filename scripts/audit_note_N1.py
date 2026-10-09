#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N1: the claims ledger (provisional; FINAL with --note-rows).

The block (AUDIT-note-release-v1_2.md, lines 18-23) wants one row per figure
in RESEARCH-NOTE-v0_2-draft.md and in the Digest seat's F1/F2 SVGs. Neither is
on this machine (results/raw/2026-10-08_note-preflight.md@bbc9ffe:15, :17-18),
so this ledger is built over every numeral the BLOCK quotes as a note figure
(block lines 21-133) and is PROVISIONAL: it is to be re-run with --note
against the note and the SVGs when the PI places them.

What it does, in order:
  1. Reads the block at the record pin (git show bbc9ffe:...), checks its
     sha256 against the routed one, and extracts every numeral token in block
     lines 21-133 by a stated rule (digit runs and number words). Each token is
     either covered by a hand-mapped ledger row (its span), or excluded by a
     hand-declared span or a generic rule (with a category). Unassigned tokens
     are printed; the run asserts there are none.
  2. For each ledger row, reads the item raw that addresses the figure at the
     audit pin (git show 09c3a8c:results/raw/...), carries the printed value,
     the source and the status exactly as the item raw gives them, and gives
     the item raw's own locator (results/raw/...@09c3a8c:<line>).
  3. For each source the item raw names, records the commit at which it
     entered the record: an artifact -> `git log -1 --format=%H bbc9ffe --
     <path>` (last change at or before the pin) and its first-add commit
     (`git log --diff-filter=A`); a line locator -> `git blame -L n,n
     --porcelain <rev> -- <file>` at the locator's revision, per line, each
     cross-checked against one full-file `git blame --porcelain` per file; an
     audit raw -> its commit at the audit pin (computed-new figures only; a
     not-found figure enters no audit commit).
  4. The block's pass check (:23) over the rows; the latest entry commit over
     all rows, twice (record sources only; including audit-raw sources).
  5. With --note PATH (repeatable; .md or .svg text content), extracts every
     numeral from each file with its sign and unit kind (%, pp, x) and matches
     it to ledger rows: 'matched' needs the same unit kind, value and sign AND
     agreeing context words in the clause that holds the unit; a value hit
     without them is a 'candidate (verify context)'; a value several rows share
     is flagged; everything else is 'not in ledger', with loose, rounding and
     item-raw pointers. A watch-list of values the item raws tie to conditional
     STOPs, not-found cuts and non-transcription discrepancies is surfaced in
     its own table, whatever it matches. SVG geometry (plotted positions) is
     not read.

Round 2 (values check of round 1): sign/unit-aware --note matcher with a
context test and the watch-list; rows L162-L166 for numeral-free figure names
(:43, :48, :57, :104, :107) and the numeral-free rule with its no-row list;
N3 status_condition carried; NF/SR branch texts attribute :23 readings to Code;
4a conditions; not-found rows enter no entry commit; per-line blame for every
locator; L089's source is the bet's text; decimals after 'word-' are figures.

Round 3 (integration check of round 2): source names with internal dots
(e0_axes.meta.json) and slash-abbreviated alternatives (d2/d3_scores.json) are
resolved, and any name the parser leaves unresolved is listed in section 3;
section 5's note-locator branch counts each row's carriers at the earliest of
them (a fact enters the record with its first carrier), and the record-only
candidate is stated as conditional on the G-CAL caveat; the same figure in two
item raws with different statuses is tabulated (4f) and named in 4b; wording,
scope and precision corrections the item raws route to note sentences are
collected (4g), primary-row notes are shown on every row, and two watch-list
entries are added; the --note matcher reads context words only in the clause
that holds the unit and flags a value shared by several rows; the 1b list is
labelled as examples and extended; L089's source is cited at the record pin.

Round 4 (N1 final, 2026-10-09). The PI placed RESEARCH-NOTE-v0_3-draft.md (it
supersedes v0.2) and the two SVGs. --note-rows PATH reads the verified mapping
of every numeral unit in the three files (results/raw/2026-10-09_note-N1-note-
rows.json: ten mapper chains, each checked once adversarially and revised) as
data, and: asserts each file's sha256 against the routed one; asserts that every
unit the --note matcher extracts has a row; validates every row (the unit is on
its cited line; a cited source line carries a value the row states, level A tied
to the note's own number or level B another stated value; a cited ledger row
exists and, for a ledger-row map, carries the row's status); any failure without
a 'validation_note' on the row stops the run before anything is written (round 5
narrows this: a note explains only the check it names, see below). It then
adds section 9: the figures one row each, the block's pass check over them
(discrepant rows by the block :23 branch their own cause reads into, asserted),
the watch-list outcome per conditional STOP, the mappers' span notes, the tag
commit over the note's figures, and the open items. With --note-rows the title
reads FINAL for the note's sha256; sections 1-8 are the provisional round's
block-quotation ledger, re-run unchanged.

Round 5 (N1 final fixes, 2026-10-09; the final checker's findings 1-9 and the
PI's N19 routing). Every row's status is its item raw's, checked mechanically
(the status check: JSON figure row, table status cell, quoted status_basis;
record rows log-only, audit-raw-new rows computed-new); corrections N1 reads in
a sentence are recorded beside the status ('correction', section 9i), never as
one. The validator's checks are named (note-line, kind-hash, schema,
locator-value, source-values, status, ledger, ledger-span, double-rounding,
correction, corrected-in-note); a validation_note explains only the check it
names, matched (in round 5) to a substring of its failure message. The unit ->
kind assignment is frozen by NR_KIND_SHA256. Every final run repeats the
validation on in-memory mutations of the rows and on the overwrite guard's
cases, and stops if any is not caught. The guard never writes the committed
provisional ledger, in any mode. Section 10 is the round's values check.

Round 6 (N1 final fixes, round 2, 2026-10-09; the adversarial check of round
5, n1chk2, findings 1-9). New checks: maps-to (item-raw and audit-raw-new rows
cite an item-raw line, record rows a record line), pins (every cited revision
is its path class's pin), unit-stated (an integer unit's number is stated in
the source value), correction-declared (NR_CORRECTIONS); the status check reads
inline '[status: ...]' tags and every cited item-raw line of a record row, and
compares every named ledger row's status; corrected_in_note needs the item
raw's correction wording, a figure row whose quoted figure the note no longer
carries, and NR_DISC's branch C exactly; an exemption equals its whole message
and its row is declared with a fingerprint (NR_EXEMPT_FP); the clauses are
frozen by NR_CLAUSE_SHA256; one-place decimals are checked. The self-test adds
n1chk2's mutations, Code's, five generated families, and three known limits
that must stay uncaught. Section 11 is the round's values check.

Round 7 (N1 final fixes, round 3, 2026-10-09; the strict check of round 6,
r6chk, findings 1-4). The status check binds a status to its figure: a cited
item-raw status line decides only where it carries a value the row states;
a source with several terms decides nothing by itself (the row needs a
status_basis quoting the single-term clause); a status_basis is an item-raw
line and agrees with every value-carrying status line; a 'related row'
ledger field is compared with that related row only. New checks: ledger-bind
(the named ledger row is named in the locator or its item-raw line cited);
pins also require every cited file and line to exist. Frozen by hash:
NR_STATUS_SHA256 (every row's maps_to, status, ledger_row and status_basis,
and a not-found row's locator and source value), NR_TEXT_SHA256 (free text
and change history); NR_CORRECTIONS carries a fingerprint per correction; a
quotation scan over the rows file runs at every run (NR_QUOTE_REVIEWED). The
self-test adds r6chk's mutations, Code's, row-level families F-H and two
levels of known limits. Section 12 is the round's values check.

Read-only on the record. git runs only in this repository (never inside
jlens-qwen36/). Writes only --out and --json-out. No model, no network, no
randomness; stdlib only.

Usage (from the repository root):
  provisional round (its ledger is committed at 6485da2 and never rewritten;
  --out and --json-out are required and may not name it):
  jlens-qwen36/.venv/bin/python scripts/audit_note_N1.py \
      --out <scratch>/ledger.md --json-out <scratch>/ledger.json \
      [--note RESEARCH-NOTE-v0_2-draft.md --note F1.svg --note F2.svg]
  N1 final:
  jlens-qwen36/.venv/bin/python scripts/audit_note_N1.py \
      --note-rows results/raw/2026-10-09_note-N1-note-rows.json \
      --note RESEARCH-NOTE-v0_3-draft.md --note 2026-10-06_F1b_five-link-panels.svg \
      --note 2026-10-06_F2_macar-lineage-roc_post.svg \
      --out results/raw/2026-10-09_note-N1-claims-ledger-final.md \
      --json-out results/raw/2026-10-09_note-N1-claims-ledger-final.json
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import html
import json
import os
import platform
import re
import shlex
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PIN = "bbc9ffe"            # record pin (the block's commit)
AUDIT = "09c3a8c"          # audit-raw pin (the item raws' commit)
BLOCK = "AUDIT-note-release-v1_2.md"
ROUTED_SHA = ("8cd8a9ac", "3841")
BLOCK_RANGE = (21, 133)
N1_LINES = (18, 23)
AUDIT_RAW_PREFIX = "results/raw/2026-10-08_note-"
PREFLIGHT = "results/raw/2026-10-08_note-preflight.md"
NOTE_DEFAULT = "RESEARCH-NOTE-v0_2-draft.md"

RAWS = {
    "N2": ("results/raw/2026-10-08_note-N2-introspection.md", "results/raw/2026-10-08_note-N2-roc.json"),
    "N2vi": ("results/raw/2026-10-08_note-N2vi-source.md", "results/raw/2026-10-08_note-N2vi-source.json"),
    "N3": ("results/raw/2026-10-08_note-N3-echo-robustness.md", "results/raw/2026-10-08_note-N3-echo-robustness.json"),
    "N3c": ("results/raw/2026-10-08_note-N3-echo-compute.md", "results/raw/2026-10-08_note-N3-echo-compute.json"),
    "N4": ("results/raw/2026-10-08_note-N4-e2a.md", "results/raw/2026-10-08_note-N4-e2a.json"),
    "N5": ("results/raw/2026-10-08_note-N5-f1.md", "results/raw/2026-10-08_note-N5-f1.json"),
    "N6": ("results/raw/2026-10-08_note-N6-e2b.md", "results/raw/2026-10-08_note-N6-e2b.json"),
    "N7": ("results/raw/2026-10-08_note-N7-olmo.md", "results/raw/2026-10-08_note-N7-olmo.json"),
    "N8": ("results/raw/2026-10-08_note-N8-link2.md", "results/raw/2026-10-08_note-N8-link2.json"),
    "N9": ("results/raw/2026-10-08_note-N9-weight.md", "results/raw/2026-10-08_note-N9-weight.json"),
    "N10": ("results/raw/2026-10-08_note-N10-horn1.md", None),
    "N11": ("results/raw/2026-10-08_note-N11-smoke.txt", None),
    "N12": ("results/raw/2026-10-08_note-N12-history.md", "results/raw/2026-10-08_note-N12-history.json"),
    "N13": ("results/raw/2026-10-08_note-N13-provenance.md", "results/raw/2026-10-08_note-N13-provenance.json"),
    "N14": ("results/raw/2026-10-08_note-N14-artifacts.md", "results/raw/2026-10-08_note-N14-artifacts.json"),
    "N16": ("results/raw/2026-10-08_note-N16-decoding.md", "results/raw/2026-10-08_note-N16-decoding.json"),
    "N17": ("results/raw/2026-10-08_note-N17-numerics.md", None),
}
# JSON field that carries the printed value, per item
VALUE_KEY = {"N2": "printed", "N2vi": "printed", "N3": "reproduced", "N4": "reproduced",
             "N5": "value", "N6": "value", "N7": "printed", "N8": "value", "N9": "value",
             "N14": "value", "N16": "printed"}
SOURCE_KEY = {"N2vi": "record_locators"}

STATUS_VOCAB = ("reproduced", "log-only", "not found", "discrepant", "computed-new")


# ------------------------------------------------------------------ ledger map
# Each row: id, block line, span (exact substring of that block line; occ = which
# occurrence), item, refs (primary item-raw rows that address the figure as the
# block writes it), related (other item-raw rows on the same figure; shown, not
# used for the pass check). A ref is (item, kind, key[, spec]):
#   ("N2", "fig", "<figure string in the item JSON figures[]>")
#   ("N3", "id", "3a")                       -- N3 rows by id
#   ("N10", "mdrow", "<needle at the start of a markdown/text table row>")
#   ("N3c", "mdline", "<needle in a bullet line>", {"printed":..., "status":..., "source":...})
#       (each value an exact substring of that line, asserted present)
#   ("N19", "notrun", "<reason>")
#   (None, "none", "<what the item raw has instead>")
def F(item, fig):
    return (item, "fig", fig)


ROWS = [
    # ---- N2 (block :30-:34) -------------------------------------------------
    dict(id="L001", line=30, span="SFT 0.200", refs=[F("N2", "FPR SFT 0.200")],
         related=[F("N2", "FLAG-3 corrected SFT FPR 0.176")]),
    dict(id="L002", line=30, span="DPO 0.000", refs=[F("N2", "FPR DPO 0.000")]),
    dict(id="L003", line=30, span="instruct 0.000", refs=[F("N2", "FPR instruct 0.000")]),
    dict(id="L004", line=30, span="base 0.431", refs=[F("N2", "FPR base 0.431")],
         related=[F("N2", "Code's read of the 42 affirm-scored controls; base relabelled (post-hoc)")]),
    dict(id="L005", line=30, span="= 58/96", refs=[F("N2", "'= 58/96' (block :30)")]),
    dict(id="L006", line=30, span="(≤ 2.5 points)",
         refs=[F("N2", "fidelity-of-text vs template arm within 2.5 points (SFT 0.200 vs 0.225)")]),
    dict(id="L007", line=31, span="that it yields zero detection claims at every stage",
         refs=[F("N2", "greedy run: zero detection claims at every stage (fidelity arm, the record's referent)")],
         related=[F("N2", "greedy run: protocol otherwise identical"),
                  F("N2", "greedy run exists as a committed artifact with its own stamp")]),
    dict(id="L008", line=31, span="report n per stage",
         refs=[F("N2", "greedy run: n per stage (fidelity, eight concepts, decidable inj/ctl)")]),
    dict(id="L009", line=32, span="178 decidable trials at DPO and instruct",
         refs=[F("N2", "178 decidable trials at DPO and instruct")],
         related=[F("N2", "log: instruct FA 0/45; '88 and 89 decidable trials'")]),
    dict(id="L010", line=32, span="at qualified doses",
         refs=[F("N2", "MED_c 1.0 at SFT/DPO/instruct; base hard stop")]),
    dict(id="L011", line=32, span="zero detection claims of any kind",
         refs=[F("N2", "zero detection claims of any kind (DPO, instruct)")]),
    dict(id="L012", line=32, span="+0.096", refs=[F("N2", "SFT discrimination +0.096")]),
    dict(id="L013", line=32, span="with its interval", refs=[F("N2", "SFT interval [-0.105, +0.292]")]),
    dict(id="L014", line=32, span="and test", refs=[F("N2", "SFT one-sided Fisher p (H1 hit > FA)")]),
    dict(id="L015", line=34, span="25/58", refs=[F("N2", "FPR base 0.431")],
         note="criterion arm = F2 FPR markers only (no injected trials; N2 raw section 5(a))"),
    dict(id="L016", line=34, span="17/85", refs=[F("N2", "FPR SFT 0.200")],
         note="criterion arm = F2 FPR marker (no TPR)"),
    dict(id="L017", line=34, span="0/91", occ=1, refs=[F("N2", "FPR DPO 0.000")],
         note="criterion arm = F2 FPR marker (no TPR)"),
    dict(id="L018", line=34, span="0/91", occ=2, refs=[F("N2", "FPR instruct 0.000")],
         note="criterion arm = F2 FPR marker (no TPR)"),
    dict(id="L019", line=34, span="12/40 hits", refs=[F("N2", "exploration sft: hits 12/40")]),
    dict(id="L020", line=34, span="9/44 FA at SFT", refs=[F("N2", "exploration sft: FA 9/44")],
         related=[F("N2", "exploration SFT point with FLAG-3 applied (post-hoc)")]),
    dict(id="L021", line=34, span="0/43", occ=1, refs=[F("N2", "exploration dpo: hits 0/43")]),
    dict(id="L022", line=34, span="0/45 at DPO", refs=[F("N2", "exploration dpo: FA 0/45")]),
    dict(id="L023", line=34, span="0/44", refs=[F("N2", "exploration instruct: hits 0/44")]),
    dict(id="L024", line=34, span="0/46 at instruct", refs=[F("N2", "exploration instruct: FA 0/46")],
         related=[F("N2", "log: instruct FA 0/45; '88 and 89 decidable trials'")]),
    dict(id="L025", line=34, span="(zero claims at every stage, with its ns)",
         refs=[F("N2", "greedy run: zero detection claims at every stage (fidelity arm, the record's referent)"),
               F("N2", "greedy run: n per stage (fidelity, eight concepts, decidable inj/ctl)")],
         related=[F("N2", "greedy run: protocol otherwise identical")]),
    dict(id="L026", line=34, span="theirs base d′ ≈ −1.9", refs=[F("N2", "theirs base d' ~ -1.9")],
         related=[F("N2vi", "design seat's N2(v) source points (block :34: d' -1.9 / -0.3 / +0.6 / +0.15; p ~ .11 DPO, ~ .5 instruct, at 800/80 per configuration)")]),
    dict(id="L027", line=34, span="SFT ≈ −0.3", refs=[F("N2", "theirs SFT d' ~ -0.3")]),
    dict(id="L028", line=34, span="DPO ≈ +0.6", refs=[F("N2", "theirs DPO d' ~ +0.6")]),
    dict(id="L029", line=34, span="(p ≈ .11 on 0 of ~80 controls)", refs=[F("N2", "theirs DPO p ~ .11 (0 of ~80 controls)")]),
    dict(id="L030", line=34, span="instruct ≈ +0.15", refs=[F("N2", "theirs instruct d' ~ +0.15")]),
    dict(id="L031", line=34, span="(p ≈ .5)", refs=[F("N2", "theirs instruct p ~ .5")]),
    dict(id="L032", line=34, span="under an assumed 800/80 per configuration",
         refs=[F("N2vi", "~800 injected / ~80 control per configuration, as the source's n, and figures derived from it (~33× ours; the 'theirs, OLMo cell (~800/80)' power row)")],
         related=[F("N2vi", "~800 injected / ~80 control per (layer, alpha) configuration, and its ratio ~33× our 24, as the record's inference (eight concepts x the code's 100 / 10 per concept)")],
         note="N2vi lists the block's premise (AUDIT-note-release-v1_2.md@bbc9ffe:34) among this row's locators"),
    dict(id="L033", line=34, span="ours SFT ≈ +0.3", refs=[F("N2", "ours SFT d' ~ +0.3")]),
    dict(id="L034", line=34, span="(p ≈ .22)", refs=[F("N2", "ours SFT p ~ .22")]),
    dict(id="L035", line=34, span="DPO and instruct ≈ 0 by construction",
         refs=[F("N2", "ours DPO d' ~ 0"), F("N2", "ours instruct d' ~ 0")]),
    dict(id="L036", line=34, span="upper 95% bound on a per-stage hit rate given 0/43 ≈ .067",
         refs=[F("N2", "upper 95% bound, 0/43 ~ .067")]),
    # ---- N2(vi) (block :35) -------------------------------------------------
    dict(id="L037", line=35, span="0.001", refs=[F("N2vi", "source base TPR 0.001")]),
    dict(id="L038", line=35, span="0.149", refs=[F("N2vi", "source sft TPR 0.149")]),
    dict(id="L039", line=35, span="0.029", refs=[F("N2vi", "source dpo TPR 0.029")]),
    dict(id="L040", line=35, span="0.009", refs=[F("N2vi", "source instruct TPR 0.009")]),
    dict(id="L041", line=35, span="L ∈ {25, 32, 38, 45, 51} × α ∈ {1, 2, 4, 8} grid",
         refs=[F("N2vi", "aggregation over L in [25, 32, 38, 45, 51] x alpha in [1, 2, 4, 8] (20 configurations)")],
         related=[F("N2vi", "layer indices from the code's default fractions")]),
    # ---- N3 (block :43-:47) -------------------------------------------------
    dict(id="L042", line=43, span="AUC range (.94–.995)", refs=[("N3", "id", "3a")]),
    dict(id="L043", line=43, span="the primacy profile (.89 first round, .68 fourth)", refs=[("N3", "id", "3b")]),
    dict(id="L044", line=43, span="the binding AUC at the label token (≥ .998, L51–61)", refs=[("N3", "id", "3c")]),
    dict(id="L045", line=43, span="at the decision token (.50–.55)", refs=[("N3", "id", "3d")]),
    dict(id="L046", line=43, span='("nine positions before")', refs=[("N3", "id", "3e")]),
    dict(id="L047", line=43, span="0–3 of 102 sign flips", refs=[("N3", "id", "3f")]),
    dict(id="L048", line=43, span="median |Δ| ≤ .10 logit", refs=[("N3", "id", "3g")]),
    dict(id="L049", line=43, span="pseudo-shift ±.02–.03 toward the first block's label", refs=[("N3", "id", "3h")]),
    # round 2 (values-check finding 2): numeral-free figure names the block lists among the note's figures
    dict(id="L162", line=43, span="the random-direction comparison",
         refs=[("N3", "id", "3i-a1"), ("N3", "id", "3i-a2"), ("N3", "id", "3i-b")],
         note="numeral-free: one of the block's 'leakage figures' (:43); N3 splits it into three rows (added in round 2)"),
    dict(id="L050", line=43, span="sign median .861 against the .90 bar", refs=[("N3", "id", "3j-a")]),
    dict(id="L051", line=43, span="binding .88 → .64", refs=[("N3", "id", "3j-b")]),
    dict(id="L052", line=44, span="(102 sessions, grouped 10-fold, 200 shuffles)",
         refs=[("N3", "mdline", "As stored: n_sessions 102, kfold 10, n_shuffles 200",
                {"printed": "As stored: n_sessions 102, kfold 10, n_shuffles 200",
                 "status": None,
                 "source": "from stageC_analysis.json",
                 "source_line_needle": "## 4. Part (i-b): the stored shuffled-label null"})],
         note="block (i-b) asks for 'the CV scheme and shuffle count as stored'; the item raw states them in section 4 without a per-figure status row; the figure rows ib-1..ib-5 each print the same scheme"),
    dict(id="L053", line=44, span='plots a "shuffle-95 null" at ≈ .57–.59 across layers', refs=[("N3", "id", "ib-1")],
         related=[("N3c", "mdline", "- F1 (block :44, (i-b)) 'shuffle-95 null at ~.57-.59 across layers'",
                   {"printed": "pooled 0.5661-0.5971, i.e. .57-.60 at two decimals",
                    "status": "discrepant (transcription)",
                    "source": "stageC_analysis.json families.*.shuffle95"})]),
    dict(id="L054", line=44, span="binding at the first label ≈ 1.0 from L51 on", refs=[("N3", "id", "ib-2")]),
    dict(id="L055", line=44, span="at the second label .81–.96", refs=[("N3", "id", "ib-3")],
         related=[("N3c", "mdline", "- F1's '.81-.96 at the second label'",
                   {"printed": "label_b over L51-L63 0.8077-0.9642 = .81-.96",
                    "status": "reproduced, over L51-L63",
                    "source": "label_b"})]),
    dict(id="L056", line=44, span="at the choice read .50–.55", refs=[("N3", "id", "ib-4")]),
    dict(id="L057", line=44, span="≈ 1.0 at the first label", refs=[("N3", "id", "ib-2")],
         note="the note's link-3 sentence as the block quotes it"),
    dict(id="L058", line=44, span=".81–.96 at the second", refs=[("N3", "id", "ib-3")],
         related=[("N3c", "mdline", "- F1's '.81-.96 at the second label'",
                   {"printed": "label_b over L51-L63 0.8077-0.9642 = .81-.96",
                    "status": "reproduced, over L51-L63",
                    "source": "label_b"})],
         note="the note's link-3 sentence as the block quotes it; the same label_b series as L055, so N3c's line on F1's "
              "series is shown here too (round 3)"),
    dict(id="L059", line=44, span="below the shuffled-label 95th percentile of ≈ .58", refs=[("N3", "id", "ib-5")],
         related=[("N3c", "mdline", "- The note's link-3 'below the shuffled-label 95th percentile of ~.58'",
                   {"printed": "the read AUC is below its own 95th at every layer under both nulls",
                    "status": "reproduced as a midpoint",
                    "source": "stored 200 draws"})]),
    dict(id="L060", line=45, span="1,000 shuffles at the label tokens and the decision token with the same grouped CV, reporting mean and 95th percentile",
         refs=[("N3c", "mdline", "- N3(ii) 'extended only if cheap",
                {"printed": "extended to 1000 draws at L51-L61 for c1_read_M1M2, c1_label_a_M1M2, c1_label_b_M1M2 (1,000-draw 95th: read 0.5729-0.5865, label_a 0.5700-0.5851, label_b 0.5705-0.5805)",
                 "status": "computed-new",
                 "source": "`data/echo/stageC_resid_s*.npz`, 102 files (local, gitignored)",
                 "source_line_needle": "- Residual arrays: `data/echo/stageC_resid_s*.npz`"})],
         note="computed-new on the local, gitignored Stage C residual arrays (data/echo/*.npz; preflight raw)"),
    dict(id="L061", line=45, span="the stored 200-shuffle null stands",
         refs=[("N3c", "mdline", "- N3(ii) 'extended only if cheap",
                {"printed": "the stored 200-draw null stands at L40, L44, L48, L49, L50, L62, L63",
                 "status": "reproduced",
                 "source": "`data/echo/stageC_analysis.json` at bbc9ffe",
                 "source_line_needle": "- `data/echo/stageC_analysis.json` at bbc9ffe"})]),
    dict(id="L062", line=46,
         span="a small MLP (one hidden layer, width ≤ 64, early stopping) and an RBF kernel classifier, same CV as (i), same layers; report AUC with its permutation 95th percentile",
         refs=[("N3c", "mdline", "- N3(iii): MLP at the read L49-L63",
                {"printed": "MLP at the read L49-L63 0.5950-0.9707, RBF 0.6048-0.7575",
                 "status": "computed-new; magnitude specification-dependent, see (iii-s)",
                 "source": "`data/echo/stageC_resid_s*.npz`, 102 files (local, gitignored)",
                 "source_line_needle": "- Residual arrays: `data/echo/stageC_resid_s*.npz`"})],
         note="computed-new on the local, gitignored Stage C residual arrays"),
    dict(id="L063", line=47, span="Layer sweep at the decision token, linear, L44–L61, to show the .50–.55 is not a one-layer accident",
         refs=[("N3c", "mdline", "- N3(iv) 'the .50-.55' at the decision token",
                {"printed": "L49-L61 0.5014-0.5406; L44-L48 exactly 0.5 by construction",
                 "status": "reproduced at L44 and L48-L61 (stored c1_read_M1M2 auc_kfold); computed-new at L45-L47",
                 "source": "`data/echo/stageC_analysis.json` at bbc9ffe",
                 "source_line_needle": "- `data/echo/stageC_analysis.json` at bbc9ffe"})]),
    dict(id="L163", line=48, span="Random-direction control for the binding read", refs=[("N3", "id", "v-1")],
         note="numeral-free: N3(v), reported, not passed (block :50); a row for the same reason as N3(ii)-(iv)'s L060-L063 (added in round 2)"),
    # ---- N4 (block :54-:59) -------------------------------------------------
    dict(id="L064", line=54, span="the 311/360",
         refs=[F("N4", "311 distinct verified forward passes at KL = 0"), F("N4", "360 (earlier count)")]),
    dict(id="L164", line=57, span="the definition of Δ as the record's field defines it",
         refs=[F("N4", "Δ = share of first free choices toward the state label minus ½ (definition)")],
         note="numeral-free: the definition the note's e2a figures and F1's relabel (:57) rest on (added in round 2)"),
    dict(id="L065", line=57, span="state arm 55 of 102 → +0.0392", refs=[F("N4", "state arm 55 of 102 → +0.0392")]),
    dict(id="L066", line=57, span="one-sided exact-binomial P(X ≥ 55 | 102, ½) = 0.24422, which is the stored p to five decimals",
         refs=[F("N4", "P(X ≥ 55 | 102, ½) = 0.24422 = stored p")]),
    dict(id="L067", line=57, span="sham 19/37 → +0.0135", refs=[F("N4", "sham 19/37 → +0.0135")]),
    dict(id="L068", line=57, span='random-1 15/23 → +0.1522 (the "largest pseudo-Δ")',
         refs=[F("N4", "random-1 15/23 → +0.1522 (largest pseudo-Δ)")]),
    dict(id="L069", line=57, span="random-2 12/22 → +0.0455", refs=[F("N4", "random-2 12/22 → +0.0455")]),
    dict(id="L070", line=57, span='every arm integer under this definition and none under "(approach − avoid)/n"',
         refs=[F("N4", "every arm integer under share − ½, none under (approach − avoid)/n")]),
    dict(id="L071", line=57, span='the preprint\'s "54 of 101 valid sessions"',
         refs=[F("N4", "preprint quotation '54 of 101 valid sessions' (the sentence as the block quotes it)")],
         related=[F("N4", "preprint footnote 1 (:174): '54 of 101, Δ = +0.035, p = 0.275'")]),
    dict(id="L072", line=57, span="neither +0.039", refs=[F("N4", "state arm 55 of 102 → +0.0392")]),
    dict(id="L073", line=57, span="p = 0.244", refs=[F("N4", "P(X ≥ 55 | 102, ½) = 0.24422 = stored p")]),
    dict(id="L074", line=57, span='"Δ_first is half the difference between the state and sham arms\' break rates"',
         refs=[F("N4", "preprint quotation 'Δ_first is half the difference between the state and sham arms' break rates'")],
         related=[F("N4", "the break-rate identity the sentence glosses (definition, gloss or error?)")]),
    dict(id="L075", line=57, span="map-level +0.104 / −0.031", refs=[F("N4", "map-level +0.104 / −0.031 (state arm)")]),
    dict(id="L076", line=57, span="sham-arm map-level +0.111 / −0.079", refs=[F("N4", "sham-arm map-level +0.111 / −0.079")]),
    dict(id="L077", line=57, span="the approach-probability interval ≈ [.44, .64]", refs=[F("N4", "approach-probability interval ≈ [.44, .64]")]),
    dict(id="L078", line=57, span="(Wilson on 55/102 gives it)", refs=[F("N4", "the interval's method (block: 'Wilson on 55/102 gives it')")]),
    dict(id="L079", line=57, span="first-pick habit 83.4%", refs=[F("N4", "first-pick habit 83.4%")]),
    dict(id="L080", line=57, span="the control-arm sizes 37/23/22", refs=[F("N4", "control-arm sizes 37/23/22")]),
    dict(id="L081", line=57, span='F1\'s link-5 y-axis label reads "(approach − avoid)"', refs=[F("N4", "F1 link-5 y-axis '(approach − avoid)'")]),
    dict(id="L082", line=58, span="at n = 101, α as pre-registered, power .80, the minimum detectable first-choice effect under the registered test",
         refs=[F("N4", "MDE at n = 101, α as pre-registered, power .80, registered test")],
         related=[F("N4", "MDE at n = 102 (record's published n)")]),
    dict(id="L083", line=58, span="the same at the sham-envelope criterion", refs=[F("N4", "MDE at the sham-envelope criterion")]),
    dict(id="L084", line=59, span="311 vs 360",
         refs=[F("N4", "311 distinct verified forward passes at KL = 0"), F("N4", "360 (earlier count)")]),
    dict(id="L085", line=59, span='"311 distinct verified forward passes at KL = 0"',
         refs=[F("N4", "311 distinct verified forward passes at KL = 0")]),
    dict(id="L086", line=59, span="why 360 was the earlier count", refs=[F("N4", "360 (earlier count)")]),
    # ---- N11 (block :68, :70) -----------------------------------------------
    dict(id="L087", line=68, span="**103/103**",
         refs=[("N11", "txtrow", "103/103 (N11) | AUDIT-note-release-v1_2.md@bbc9ffe:68 |")],
         related=[F("N8", "regression suite 103/103 (block :107)")]),
    dict(id="L088", line=70, span="103/103 from a fresh clone",
         refs=[("N11", "txtrow", "103/103 (N11) | AUDIT-note-release-v1_2.md@bbc9ffe:70 |")]),
    # ---- N13 (block :91) ----------------------------------------------------
    dict(id="L089", line=91, span="the Q1 bet (timestamped 2026-08-18)",
         refs=[("N13", "mdrow", "| 15 | Q1 bet")],
         note="N13's row 15 uses N13's own status vocabulary (block :93), not N1's; its referent note (section 8) gives the wording correction"),
    # ---- N5 (block :98) -----------------------------------------------------
    dict(id="L090", line=98, span="SOLV +.020 p = .44", refs=[F("N5", "SOLV +.020 p = .44")]),
    dict(id="L091", line=98, span="DIFF −.096 p = .24", refs=[F("N5", "DIFF −.096 p = .24")]),
    dict(id="L092", line=98, span="the valid-n floor", refs=[F("N5", "DIFF valid-n floor")]),
    dict(id="L093", line=98, span="the length-preference deflation test", refs=[F("N5", "DIFF length-preference deflation test (tested and failed)")]),
    dict(id="L094", line=98, span="NOV −.066", refs=[F("N5", "NOV −.066")]),
    dict(id="L095", line=98, span="its map-inconsistency", refs=[F("N5", "NOV map-inconsistency")]),
    dict(id="L096", line=98, span="CORR 0.000", refs=[F("N5", "CORR 0.000")]),
    dict(id="L097", line=98, span="maps +.121/−.130", refs=[F("N5", "CORR maps +.121/−.130")]),
    dict(id="L098", line=98, span="FDBK +.023", refs=[F("N5", "FDBK +.023")]),
    dict(id="L099", line=98, span="the 93% positive delivery rate", refs=[F("N5", "FDBK 93% positive delivery rate")]),
    dict(id="L100", line=98, span="344/344 sessions", refs=[F("N5", "344/344 sessions")]),
    dict(id="L101", line=98, span="zero pauses", refs=[F("N5", "zero pauses")]),
    dict(id="L102", line=98, span="termination attempts ≈ 1% of rounds by arm",
         refs=[F("N5", "termination attempts ≈ 1% of rounds by arm")],
         related=[F("N5", "termination attempts ≈ 1% of rounds (overall)"),
                  F("N5", "33 attempts ≈ 1.0% of rounds (verdict entry; FINDINGS-4)")]),
    dict(id="L103", line=98, span="exploration share ≈ .50 by arm", refs=[F("N5", "exploration share ≈ .50 by arm")],
         related=[F("N5", "FDBK all-picks share toward the verdict config (POST-HOC)")]),
    dict(id="L104", line=98, span="the calibrated accuracies .98/.50 for DIFF", refs=[F("N5", "calibrated accuracies .98/.50 for DIFF (calib.json)")]),
    dict(id="L105", line=98, span='"G-CAL 0.12 artifact"', refs=[F("N5", "CORR dose caveat: known artifact at 0.12? (yes/no)")],
         related=[F("N5", "preprint 'at a dose a later calibration (§8.1) found below its visibility criterion'"),
                  F("N5", "CORR calibration delta in the verdict entry (+.094)")]),
    # ---- N6 (block :101) ----------------------------------------------------
    dict(id="L106", line=101, span="Δ_first = −0.0104 (47/96)", refs=[F("N6", "Δ_first = −0.0104 (47/96)")]),
    dict(id="L107", line=101, span="shadow 48/96", refs=[F("N6", "shadow 48/96")]),
    dict(id="L108", line=101, span="the three conjuncts", refs=[F("N6", "verdict NULL (all three conjuncts fail)")],
         related=[F("N6", "conjunct (i): Δ_first exceeds the realised control ('sham') envelope"),
                  F("N6", "conjunct (ii): sign lock across maps"),
                  F("N6", "conjunct (iii): one-sided exact binomial p = 0.6202, critical k ≥ 57")]),
    dict(id="L109", line=101, span="their sham envelope", refs=[F("N6", "envelope value 0.0833 (sham −0.0833, random −0.0278)")],
         related=[F("N6", "envelope planning reference p90 = 0.167"), F("N6", "realised envelope relative to its null")]),
    dict(id="L110", line=101, span="π̂_d = 0.0172", refs=[F("N6", "π̂_d = 0.0172")],
         related=[F("N6", "π̂_d CI [0.0086, 0.0305]")]),
    dict(id="L111", line=101, span="against 0.0735", refs=[F("N6", "bar 0.0735")]),
    dict(id="L112", line=101, span="the certification's definition in one sentence",
         refs=[F("N6", "certification definition (what is displaced, over what set, bounded how)")],
         related=[F("N6", "preprint :111 gloss 'direct displacement of label logits'")]),
    # ---- N7 (block :104) ----------------------------------------------------
    dict(id="L113", line=104, span="+0.78", refs=[F("N7", "G_c base +0.78")]),
    dict(id="L114", line=104, span="+1.03", refs=[F("N7", "G_c sft +1.03")]),
    dict(id="L115", line=104, span="+1.53", refs=[F("N7", "G_c dpo +1.53")]),
    dict(id="L116", line=104, span="+1.56", refs=[F("N7", "G_c instruct +1.56")]),
    dict(id="L117", line=104, span="sham 0.0", refs=[F("N7", "sham 0.0")]),
    dict(id="L118", line=104, span="the base pass at L60", refs=[F("N7", "base pass at L60")]),
    dict(id="L119", line=104, span="0.05 L60", refs=[F("N7", "MED base 0.05 L60")]),
    dict(id="L120", line=104, span="0.40 L44", refs=[F("N7", "MED sft 0.40 L44")]),
    dict(id="L121", line=104, span="0.05 L44", occ=1, refs=[F("N7", "MED dpo 0.05 L44")]),
    dict(id="L122", line=104, span="0.05 L44", occ=2, refs=[F("N7", "MED instruct 0.05 L44")]),
    dict(id="L123", line=104, span="the Fisher p = .0047 allocation note", refs=[F("N7", "Fisher p = .0047 allocation note")]),
    dict(id="L124", line=104, span="Q3: zero confirmatory triggers", refs=[F("N7", "Q3: four nulls; zero confirmatory triggers")]),
    dict(id="L165", line=104, span="the falsifier", refs=[F("N7", "the falsifier (definition; untriggered)")],
         note="numeral-free: listed among N7's Q3 figures (:104) (added in round 2)"),
    dict(id="L125", line=104, span="the DPO single-map +0.1667", refs=[F("N7", "DPO single-map +0.1667 (with the other map's figure)")]),
    dict(id="L126", line=104, span="the per-stage Q3 Δs with n and map split (the preprint's data placeholder) so the note can carry a four-number line",
         refs=[F("N7", "per-stage Q3 Deltas with n and map split (TAB 2 placeholder)")],
         related=[F("N7", "descriptive exact binomial p per stage (for TAB 2's p column)")]),
    # ---- N8 (block :107) ----------------------------------------------------
    dict(id="L127", line=107, span="run the suite (103/103)", refs=[F("N8", "regression suite 103/103 (block :107)")],
         related=[("N11", "txtrow", "103/103 (N8) | AUDIT-note-release-v1_2.md@bbc9ffe:107 |")]),
    dict(id="L128", line=107, span="are among the 103", refs=[F("N8", "regression suite 103/103 (block :107)")]),
    dict(id="L129", line=107, span="Δ+ = +0.285", refs=[F("N8", "Δ+ = +0.285")]),
    dict(id="L130", line=107, span="Δ− = −0.395", refs=[F("N8", "Δ− = −0.395")]),
    dict(id="L131", line=107, span="bars ±0.158", refs=[F("N8", "bars ±0.158")]),
    dict(id="L132", line=107, span="random ≤ 0.088", refs=[F("N8", "random ≤ 0.088")]),
    dict(id="L133", line=107, span="LOO Δ+ = 0.085", refs=[F("N8", "LOO Δ+ = 0.085")]),
    dict(id="L134", line=107, span="9/12 and 10/12", refs=[F("N8", "9/12 and 10/12")]),
    dict(id="L135", line=107, span="G = 0.316", refs=[F("N8", "G = 0.316")]),
    dict(id="L166", line=107, span="the purity–potency figures",
         refs=[F("N8", "purity–potency: last-position self-indexed 0.83–0.88"),
               F("N8", "purity–potency: last-position sentiment cosine 0.11–0.21"),
               F("N8", "purity–potency: cosine 0.36–0.46 to the span mean"),
               F("N8", "purity–potency: sign-wrong at two of three layers at every dose"),
               F("N8", "purity–potency: max Δ+ = 0.135 (short of criterion at the third layer)")],
         note="numeral-free: listed among 'the note's link-2 figures' (:107); N8 gives five rows (added in round 2)"),
    dict(id="L136", line=107, span="‖d‖/R ≈ 0.16", refs=[F("N8", "‖d‖/R ≈ 0.16")]),
    dict(id="L137", line=107, span="sentiment cosine 0.52", refs=[F("N8", "sentiment cosine 0.52")]),
    dict(id="L138", line=107, span="fictional-character cosine ≈ 0.85", refs=[F("N8", "fictional-character cosine ≈ 0.85")]),
    dict(id="L139", line=107, span="self-indexed residual ≈ 0.51", refs=[F("N8", "self-indexed residual ≈ 0.51")]),
    dict(id="L140", line=107, span="readability .574/.613 vs .70", refs=[F("N8", "e2d readability .574/.613 vs .70")]),
    dict(id="L141", line=107, span="comparator .534", refs=[F("N8", "comparator .534")]),
    dict(id="L142", line=107, span="audit-flagged .000/.023/.047", refs=[F("N8", "audit-flagged .000/.023/.047")]),
    # ---- N9 (block :110) ----------------------------------------------------
    dict(id="L143", line=110, span="oriented cosines 0.476", refs=[F("N9", "oriented cosine 0.476 (replicate A)")]),
    dict(id="L144", line=110, span="0.435", refs=[F("N9", "oriented cosine 0.435 (replicate B)")]),
    dict(id="L145", line=110, span="control ceilings ≈ 0.05", refs=[F("N9", "control ceilings ≈ 0.05")]),
    dict(id="L146", line=110, span="the leakage gate's bound",
         refs=[F("N9", "leakage gate's bound: the bar, 0.10 logit, over n = 32 texts")],
         related=[F("N9", "leakage gate's bound: what it binds (max over texts of |Δ(logit a − logit b)|, adapter ON − OFF, at the choice position)")]),
    dict(id="L147", line=110, span="17×", refs=[F("N9", "17× (replicate A)")]),
    dict(id="L148", line=110, span="10×", refs=[F("N9", "10× (replicate B)")]),
    # ---- N10 (block :112) ---------------------------------------------------
    dict(id="L149", line=112, span="Horn-1 calibration R² = 0.53",
         refs=[("N10", "mdrow", "| Horn-1 calibration R² = 0.53 (block :112) |")]),
    # ---- N14 (block :116) ---------------------------------------------------
    dict(id="L150", line=116, span="the three captures", refs=[F("N14", "three live captures across two models")]),
    dict(id="L151", line=116, span="e2a sham +0.111", refs=[F("N14", "e2a sham +0.111 (map A)")]),
    dict(id="L152", line=116, span="−0.079", refs=[F("N14", "e2a sham −0.079 (map B)")]),
    dict(id="L153", line=116, span="state +0.104", refs=[F("N14", "e2a state +0.104 (map A)")]),
    dict(id="L154", line=116, span="−0.031", refs=[F("N14", "e2a state −0.031 (map B)")]),
    dict(id="L155", line=116, span="f1 CORR +.121", refs=[F("N14", "f1 CORR +.121 (map A)")]),
    dict(id="L156", line=116, span="−.130", refs=[F("N14", "f1 CORR −.130 (map B)")]),
    dict(id="L157", line=116, span="OLMo DPO +0.1667 single map", refs=[F("N14", "OLMo DPO +0.1667 single map")]),
    dict(id="L158", line=116, span="the other map's figure beside it",
         refs=[F("N14", "OLMo DPO other map (block: 'the other map's figure beside it')")]),
    # ---- N19 (block :125) ---------------------------------------------------
    dict(id="L159", line=125, span="reproduce 0.394 (equal credences, optimist vector)",
         refs=[("N19", "notrun", "N19 is not run: cloning github.com/arvomm/cacophony-public-code and running its notebook waits on the PI's permission (preflight raw note 9); block :125: if not run by T, the note's numbers are cut and the qualitative sentence stays")]),
    dict(id="L160", line=125, span="the coupling indicator's stated false-positive rate (0.70)",
         refs=[("N19", "notrun", "N19 is not run (as above)")]),
    # ---- N17 (block :130) ---------------------------------------------------
    dict(id="L161", line=130, span="sub-0.05-cosine label geometry",
         refs=[(None, "none", "N17 has no figure row for the block's wording; its note F3 addresses the wording and its figure rows give the quantities")],
         related=[("N17", "mdrow", "| '0.03-cosine scale' (record's wording of floor 2) |"),
                  ("N17", "mdrow", "| D_cond |"),
                  ("N17", "mdrow", "| max \\|control swing\\| (n = 28) |"),
                  ("N17", "mdline", "- F3 (wording). \"sub-0.05-cosine label geometry\"",
                   {"printed": "what sits under 0.05 is the conditioned swing (+0.0214) and the control-swing maximum (0.0346); the label-pair cosines reach 0.148",
                    "status": None, "source": "the record's phrase is \"the 0.03-cosine scale\""})]),
]

# Hand-declared exclusions: (block line, span, occurrence, category). Tokens in
# these spans are block numerals that are not note figures.
EXCLUDE = [
    (21, "the two were rendered", 1, "block's own prose (the F1/F2 renders)"),
    (21, "the four disagreements", 1, "block's own history (v0.2's applied disagreements); not a figure"),
    (22, "with one row per figure", 1, "procedure wording"),
    (33, "all from one scorer version; if two scorer versions", 1, "pass-condition wording (N2 row 33 records the outcome)"),
    (34, "(H + ½)/(N_s + 1), (FA + ½)/(N_n + 1)", 1, "formula constant (log-linear correction)"),
    (43, "the k arc's three open questions", 1, "scope statement"),
    (44, "Confirm those four series", 1, "procedure count"),
    (50, "a one-line addition", 1, "procedure wording"),
    (57, "Two sentences to reconcile", 1, "procedure count"),
    (59, "state in one sentence", 1, "procedure wording"),
    (60, "one paragraph for the README", 1, "procedure wording"),
    (68, "the one-line fix", 1, "procedure wording"),
    (77, "sk-[A-Za-z0-9]", 1, "regex in a procedure"),
    (77, "AKIA[0-9A-Z]{16}", 1, "regex in a procedure"),
    (81, "over 50 MB (GitHub warns)", 1, "GitHub size threshold in a procedure"),
    (81, "over 100 MB (GitHub refuses)", 1, "GitHub size threshold in a procedure"),
    (81, "(~50 MB each)", 1, "design-seat size expectation; not a note figure (auxiliary table)"),
    (81, "(47.5 MB)", 1, "design-seat size expectation; not a note figure (auxiliary table)"),
    (81, "anything over 100 MB", 1, "GitHub size threshold in a procedure"),
    (85, "nothing over 100 MB untreated", 1, "pass threshold"),
    (91, "one row per pre-registration", 1, "procedure wording"),
    (93, "the recorded one", 1, "pronoun 'one', not a numeral"),
    (98, "the five contrasts", 1, "procedure count (each contrast is its own row)"),
    (101, "§10 item 1", 1, "section reference"),
    (116, "in one table", 1, "procedure wording"),
    (122, "One table.", 1, "procedure wording"),
    (125, "Level 1–2-heavy", 1, "indicator-level name in a procedure"),
    (125, "Level 1 coupling", 1, "indicator-level name in a procedure"),
    (54, "cards 9 and 10", 1, "review-card numbers"),
    (130, "State in one paragraph", 1, "procedure wording"),
    (130, "the two numerics floors", 1, "count of items the README paragraph names"),
]

# Auxiliary: block numerals/identifiers that are not note figures but that an
# item raw checked (shown for the PI; not ledger rows).
AUX = [
    dict(line=81, text="`data/olmo/a4_instrument_*.npz` (~50 MB each)", item="N12",
         needle="| `data/olmo/a4_instrument_base.npz` | 50,681,977 |", kind="design-seat size expectation", n=4),
    dict(line=81, text="`data/e0/e0_b1_markers.npz` (47.5 MB)", item="N12",
         needle="| `data/e0/e0_b1_markers.npz` | 47,508,646", kind="design-seat size expectation"),
    dict(line=91, text="PROPOSAL-g `72b09a9`", item="N13", needle="- `72b09a9` (PROPOSAL-g pre-registration of record)",
         kind="commit anchor (identifier, not a numeral)"),
    dict(line=91, text="PROPOSAL-k v1.1 `e9b5022`", item="N13", needle="- `e9b5022` (PROPOSAL-k v1.1)",
         kind="commit anchor (identifier, not a numeral)"),
    dict(line=91, text="e2d closure `cef728f`", item="N13", needle="- `cef728f` (e2d closure)",
         kind="commit anchor (identifier, not a numeral)"),
]

# Discrepant primary rows: the item raw's own classification, quoted (asserted a substring of its status or
# note), and which branch of block :23 that classification reads into. Code does not re-decide: 'T' = the
# item raw calls it transcription; 'NT' = the item raw says it is not transcription; 'NF' = the item raw says it
# is not a note or record figure; 'SR' = the item raw calls it a stale referent.
DISC = {
    "= 58/96": ("T", "transcription in the block; referent note, not a STOP"),
    "+0.096": ("T", "transcription, correct to +0.095"),
    "AUC range (.94–.995)": ("T", "discrepant (transcription)"),
    "median |Δ| ≤ .10 logit": ("T", "discrepant (transcription)"),
    "pseudo-shift ±.02–.03 toward the first block's label": ("T", "discrepant (transcription)"),
    'plots a "shuffle-95 null" at ≈ .57–.59 across layers': ("T", "discrepant (transcription)"),
    "at the second label .81–.96": ("T", "discrepant (transcription)"),
    ".81–.96 at the second": ("T", "discrepant (transcription)"),
    'every arm integer under this definition and none under "(approach − avoid)/n"':
        ("NF", "the design seat's arithmetic, not a record figure (a note under block :3, not an (i) STOP under :62; the record's figures reproduce)"),
    "(Wilson on 55/102 gives it)":
        ("NF", "the design seat's method claim, not a record figure (a note under block :3, not an (i) STOP under :62, treated like the integrality row)"),
    'F1\'s link-5 y-axis label reads "(approach − avoid)"':
        ("NF", "a figure label, not a record figure; the block (:57) already says the post version is relabeled"),
    "**103/103**": ("SR", "discrepant (stale referent; note 1)"),
    "103/103 from a fresh clone": ("SR", "discrepant (stale referent; note 1)"),
    "termination attempts ≈ 1% of rounds by arm": ("NT", "Not a transcription"),
    "run the suite (103/103)": ("SR", "stale count, not transcription"),
    "are among the 103": ("SR", "stale count, not transcription"),
}
DISC_PATH = {
    "T": "the item raw calls it transcription: block :23 corrects the note to the reproduced value (the item raw's printed value; its correction text where it gives one)",
    "NT": "the item raw says it is not transcription: under block :23 that is a STOP on the item if the note carries the figure; the item raw itself declares no STOP; for the design seat and the PI",
    "NF": "the item raw classes it as a design-seat claim or a figure label, not a record figure: a note under block :3, not an (i) discrepancy under :62 (N4's STOPs line, {n4_stops}). N4 does not address block :23. Code's reading, for the design seat (not the item raw's): block :23 reads the note's figures, and a design-seat claim or a figure label is not one, so :23's correct-or-STOP fork is not applied here. For L081 the correction is the block's own (:57: 'the post version is relabeled to the record's definition'); N4's relabel text is in the cause column",
    "SR": "the item raw calls it a stale referent (the suite prints 154/154, not 103/103) and declares no STOP; N11's pass on N/N is Code's reading in N11, flagged there for the design seat and the PI. N1's reading of block :23 (not the item raws'): if the note carries 103/103, :23's non-transcription branch would read it as a STOP",
}
# Conditions under which a 'not found' row binds, as the item raw states them (each 'quote' asserted present in
# the item raw line found by 'needle'); 'reading' is whose reading the condition is.
NF_COND = {
    "L032": dict(item="N2vi", needle="4. If the note presents ~800 injected / ~80 control per configuration as the source's n:",
                 quote="Stated as an assumption with its premise (eight concepts, per configuration, applied to pooled rates), it is the record's log-only inference",
                 alt=("N2vi", "~800 injected / ~80 control per (layer, alpha) configuration, and its ratio ~33× our 24, as the record's inference (eight concepts x the code's 100 / 10 per concept)"),
                 text="CONDITIONAL (item raw): cut only if the note presents 800/80 as the source's n (N2vi section 12, condition 4, {loc}); "
                      "stated as an assumption with its premise it is N2vi row 12, log-only ({alt}). The block writes 'assumed' without the "
                      "eight-concept premise; N2vi lists block :34 among row 13's locators, so row 13 stays the primary"),
    "L071": dict(item="N4", needle="- None under the block's on-fail rule",
                 quote="a quotation that cannot be located is not a discrepancy, and the figure or identity each carries has its own reproduced or computed-new row",
                 text="CONDITIONAL (Code's reading of :23): a preprint quotation (block :57, 'the preprint's ...'); the cut binds only if the note "
                      "carries the sentence. N4 ({loc}): 'a quotation that cannot be located is not a discrepancy, and the figure or identity each "
                      "carries has its own reproduced or computed-new row'"),
    "L074": dict(item="N4", needle="- None under the block's on-fail rule",
                 quote="a quotation that cannot be located is not a discrepancy, and the figure or identity each carries has its own reproduced or computed-new row",
                 text="CONDITIONAL (Code's reading of :23): a preprint quotation (block :57, 'the preprint's ...'); the cut binds only if the note "
                      "carries the sentence. N4 ({loc}): as for L071"),
}
# Numeral-free spans the block names that get NO row (section 1b), with the reason and the item-raw rows that
# answer them. Rule (section 1): a numeral-free span gets a row when the block lists it among the figures to be
# reproduced for the note (an entry of an item's figure list, a qualifier or definition attached to quoted
# figures, an N3(ii)-(v) result, or a figure label). Requests for an account, a method, a provenance or a table
# get none. The list is EXAMPLES from Code's read of block lines 21-133, not an exhaustive enumeration (round 3:
# the integration check of round 2 found five more; the other requests of the N11-N13 procedures, :68 and :75-:93,
# are not enumerated).
NUMFREE_NOROW = [
    (30, "the decoding parameters used (temperature, top-p, max tokens, seed policy) and Macar's, side by side",
     "decoding parameters: N16's table (block :122), which N2(i) shares; the block quotes no value", "N2 figures[6..15]; N16"),
    (31, "confirm it exists as a committed artifact with its own stamp, that the protocol is otherwise identical",
     "properties of the greedy run, shown as related rows on L007 and L025", "N2 figures[16], [20]"),
    (33, "Name the scorer of record for each figure",
     "provenance of the figures, and N2(iv)'s pass condition; not a figure", "N2 figures[30..32]"),
    (35, "the n injected and n control per cell",
     "the source's n; the block's own figure for it (:34's 800/80) is row L032", "N2vi rows 12-13"),
    (35, "whether the values were read from a table or digitized from a figure",
     "a method statement, not a figure", "N2vi sections 3, 10"),
    (43, "with layer and CV scheme", "attributes of L042, carried in N3's row", "N3 row 3a"),
    (60, "state exactly which cells generated on the cached path",
     "a disclosure paragraph (README; the note's scope sentence), not a figure", "N4 figures[26..37]"),
    (91, "both welfare pre-commitments", "rows of N13's provenance table (a README deliverable, block :137)", "N13 table"),
    (101, "the quarantined primitive's name and what \"quarantined\" enforces",
     "a name and a description, not a figure", "N6 figures[20..21]"),
    (113, "state the regression (what on what, over which tokens and sessions)",
     "the description of L149's figure", "N10 table row"),
    (122, "for every generated-text DV in the note",
     "N16's decoding table (a README deliverable); the block quotes no value", "N16 figures[0..139]"),
    (125, "report computational-level posterior and aggregate under equal credences",
     "N19's sensitivity outputs; N19 is not run", "(none: N19 not run)"),
    (130, "the quantization, what the custom kernel patch changes and where it lives",
     "README paragraph (N17)", "N17"),
    (130, "near-tie argmax flips under high displacement",
     "the first numerics floor, worded without a figure; README paragraph (N17)", "N17"),
    # round 3 (integration check, finding on section 1b): spans of the same class the round-2 list omitted
    (32, "with the decidability rule named",
     "a rule statement attached to L009's count, not a figure", "N2 decidability-rule line (section 3) and figures[23]"),
    (35, "If a per-stage value is a best-of-grid selection, say so",
     "a request for an account of L037-L040's provenance; answered by L041's row", "N2vi row 11 (figures[10])"),
    (57, "state whether it is a definition, a mechanism gloss, or an error",
     "a classification request on L074's sentence, not a figure", "N4 figures[11] (related on L074)"),
    (60, "what \"licensed for first-token identity only\" means operationally, and confirm the choice reads are unaffected",
     "a disclosure paragraph (README; the note's scope sentence), not a figure", "N4 figures[33..37]"),
    (68, "record Python version and the import list that was needed",
     "run provenance for N11, not a note figure", "N11 text rows 'Python version' and 'import list'"),
    (98, "State whether the CORR contrast's dose carries any caveat the note should disclose",
     "a yes/no request; its answer is row L105 ('G-CAL 0.12 artifact', same line)", "N5 figures[24] (L105), section 7d"),
    (125, "record the indicator names as the notebook calls them",
     "N19's provenance output; N19 is not run", "(none: N19 not run)"),
    (130, "what \"verified against an untouched model\" means",
     "README paragraph (N17)", "N17 section 5"),
]
# Watch-list for --note mode: values the item raws tie to a conditional STOP, a not-found cut or a
# non-transcription discrepancy. Every note/SVG unit with one of these values is surfaced in its own table,
# whatever it matches. keys: (class, value[, decimals]) or ("frac", k, n); 'quotes' are asserted substrings of
# the item-raw line found by 'needle'.
WATCH = [
    dict(id="W1", item="N2vi", needle="1. If the note carries the [g3-A] joint power as 0.9642 or 0.964:",
         quotes=["0.9642", "0.964"], keys=[("num", 0.9642, 4), ("num", 0.964, 3)],
         what="[g3-A] joint power: a STOP if the note carries it (cause not identified; exact 0.96455)"),
    dict(id="W2", item="N2vi", needle="2. If the note carries 'single weakest pair (base vs dpo) 0.9825':",
         quotes=["0.9825"], keys=[("num", 0.9825, 4)],
         what="'single weakest pair (base vs dpo)': a STOP if the note carries it"),
    dict(id="W3", item="N2vi", needle="3. If the note or F2 carries the source's instruct FPR as 0.3%",
         quotes=["0.3%", "+0.6 pp"], keys=[("pct", 0.3), ("num", 0.003, 3), ("pp", 0.6), ("pct", 0.6)],
         what="source instruct FPR 0.3% / TPR - FPR +0.6 pp: corrected to 0% / +0.9 pp on Code's transcription reading, a STOP if that reading is not accepted"),
    dict(id="W4", item="N2vi", needle="3. If the note or F2 carries the source's instruct FPR as 0.3%",
         quotes=["0.001 at n = 96", "0.020 at n = 200"], keys=[("num", 0.001, 3), ("num", 0.02, 3)],
         what="retired criterion's Instruct power described as at their own rates: the same fork (source-rate values 0.002 / 0.036)"),
    dict(id="W5", item="N2vi", needle="4. If the note presents ~800 injected / ~80 control per configuration as the source's n:",
         quotes=["~800", "~80", "'~33× ours'"],
         keys=[("frac", 800, 80), ("num", 800), ("num", 80), ("times", 33), ("times", 33.3), ("num", 33.3)],
         what="~800/~80 per configuration and '~33×': cut if presented as the source's n; log-only stated with its premise"),
    dict(id="W6", item="N11", needle="1. Count. ", quotes=["103/103", "154/154"], keys=[("frac", 103, 103), ("num", 103)],
         what="103/103: stale referent (154/154 at the pin); see 4b SR"),
    dict(id="W7", item="N4", needle="- None under the block's on-fail rule", quotes=["'54 of 101 valid sessions'"],
         keys=[("num", 54)], what="preprint '54 of 101 valid sessions': not found (cut if the note carries it)"),
    dict(id="W8", item="N5", needle="| termination attempts ≈ 1% of rounds by arm |", quotes=["termination attempts ≈ 1% of rounds by arm", "sham 7/351 (1.99%)"],
         keys=[("pct", 1)], what="termination ≈ 1% by arm: discrepant, not transcription (sham 1.99%); see 4b NT"),
    # round 3: two transcription corrections the item raws route to note sentences that the block does not quote
    # (related rows of L102 and L105); a bare 33 is a small integer the matcher never matches, so it is watched
    dict(id="W9", item="N5", needle="| 33 attempts ≈ 1.0% of rounds (verdict entry; FINDINGS-4) |",
         quotes=["39 attempts = 1.27% of 3074 rounds", "if the note carries a count it is 39 (1.3%)"],
         keys=[("num", 33)],
         what="termination count '33 attempts ≈ 1.0%': discrepant (transcription, inferred); the count is 39 (1.3%)"),
    dict(id="W10", item="N5", needle="| CORR calibration delta in the verdict entry (+.094) |",
         quotes=["+.094", "the note should carry +.078 if it carries the covariate"],
         keys=[("num", 0.094, 3)],
         what="CORR calibration covariate +.094: discrepant (transcription of the superseded v1 figure); the run's value is +.078"),
]
# STOPs and conditional STOPs the item raws declare that touch ledger rows
STOPS = [
    dict(item="N2", needle="- **N2(ii) greedy run -> link 4's ROC paragraph.**",
         kind="active STOP (block :36)", rows_spans=["that it yields zero detection claims at every stage",
                                                      "report n per stage", "(zero claims at every stage, with its ns)"],
         what="the greedy row's figures reproduce, but the protocol is not otherwise identical to B2-r: STOP on link 4's ROC paragraph"),
    dict(item="N2vi", needle="4. If the note presents ~800 injected / ~80 control per configuration as the source's n:",
         kind="conditional under block :23", rows_spans=["under an assumed 800/80 per configuration"],
         what="cut if presented as the source's n; stated with its premise and unit it is the record's log-only inference (watch-list W5)"),
    dict(item="N2vi", needle="3. If the note or F2 carries the source's instruct FPR as 0.3%",
         kind="conditional under block :23", rows_spans=[],
         what="no ledger row: the block quotes no source FPR. The --note re-run's watch-list (W3, W4; section 7) surfaces any 0.3%, +0.6 pp or 0.001/0.020 in the note's and the SVGs' text; F2's plotted positions are geometry, which --note does not read, so a plotted point needs a human read. If the note or F2 carries it, the fork in this line applies"),
    dict(item="N2vi", needle="1. If the note carries the [g3-A] joint power as 0.9642 or 0.964:",
         kind="conditional under block :23", rows_spans=[],
         what="no ledger row: the block does not quote the joint power; binds only if the note carries it (watch-list W1)"),
    dict(item="N2vi", needle="2. If the note carries 'single weakest pair (base vs dpo) 0.9825':",
         kind="conditional under block :23", rows_spans=[],
         what="no ledger row: the block does not quote it; binds only if the note carries it (watch-list W2)"),
    dict(item="N3", needle="- **N3 (i) and (i-b): the pass condition (block line 50, '(i) reproduces') is met on Code's reading.**",
         kind="pass on Code's reading (no STOP)", rows_spans=["AUC range (.94–.995)", "median |Δ| ≤ .10 logit",
                                                            "pseudo-shift ±.02–.03 toward the first block's label",
                                                            'plots a "shuffle-95 null" at ≈ .57–.59 across layers',
                                                            "at the second label .81–.96", ".81–.96 at the second"],
         what="transcription-class discrepancies are read as corrections under :23, not as '(i) not reproducing' (a STOP on link 3 under :50); the design seat decides"),
]
# Round 3 (section 4f): the same figure addressed by two item raws with different statuses. The primary row is
# fixed by the ROWS map; this says why, from the item raws' own lines (each quote asserted present), for each
# (primary item, other item) pair that occurs.
CROSS_WHY = {
    ("N3", "N3c"): dict(
        lines=[("N3c", "- Referent split (a note, not a STOP)",
                "Parts (i), (i-b), (v) are in `results/raw/2026-10-08_note-N3-echo-robustness.md`"),
               ("N3", "| '.81–.96 at the second' | label_b's token:", "confirmed on L51-L63 (ib-3)")],
        text="the primary row is N3's: block :44 is part (i-b) of N3, and N3c's own referent split puts (i-b) in the "
             "N3 robustness raw ({0}). N3's section 11 confirms the range on L51-L63 and says it needs 'from L51' ({1}) "
             "without reconciling its ib-3 status with N3c's. N1 does not choose between them; the design seat decides"),
}
# Round 3 (section 4g): wording, scope and precision corrections the item raws route to note sentences. Most carry
# no numeral (or only a bare small integer), so the --note matcher cannot surface them; a human reads these at the
# --note run. Each entry: the item-raw line (by JSON figure label 'fig', by figure id 'fid', or by a needle at the
# start of an md line), quotes
# asserted present in that line (or the figure's JSON note), the ledger rows the item raw ties it to (empty: the
# block quotes no figure for it), and Code's one-line summary. Collected by Code's read of the item raws' notes
# sections and primary-row notes; not asserted exhaustive (the item raws' own notes sections are the full source).
WORDING = [
    dict(item="N2", fig="FPR SFT 0.200", quotes=["the record's FLAG-3 correction (0.176)"], rows=["L001", "L016"],
         what="the record's FLAG-3 correction gives SFT FPR 0.176 (N2's related row on L001, reproduced); the block quotes 0.200"),
    dict(item="N2", fig="FPR base 0.431", quotes=["DISCLOSURE: Code's read finds 8 of its 25 affirm verdicts"],
         rows=["L004", "L015"],
         what="disclosure on base FPR: 8 of 25 affirm verdicts carried only by non-asserting embedded complements; post-hoc relabels 0.276-0.340"),
    dict(item="N2", fig="fidelity-of-text vs template arm within 2.5 points (SFT 0.200 vs 0.225)",
         quotes=["holds at SFT/DPO/instruct, not base"], rows=["L006"],
         what="scope: the closeness holds at SFT, DPO and instruct, not at base (+26.70 pp)"),
    dict(item="N3", fid="3c", quotes=["Holds for label_a only; label_b is .81-.96"], rows=["L044"],
         what="'≥ .998' at the label token holds for label_a only; label_b reads .81-.96"),
    dict(item="N3", fid="3e", quotes=["'nine' is label_a (the first-listed menu label) only"], rows=["L046"],
         what="'nine positions before' is label_a's position; label_b is seven before the read"),
    dict(item="N3", fid="ib-2", quotes=["≈ 1.0 through L62; L63 .988"], rows=["L054", "L057"],
         what="'≈ 1.0 at the first label' holds through L62; L63 reads .988"),
    dict(item="N3", fid="ib-5", quotes=["under an every-layer reading it would fail"], rows=["L059"],
         what="'≈ .58' is a midpoint of a per-layer null (.566-.597); 'below' holds at every layer"),
    dict(item="N2vi", needle="3. If the note or F2 carries the source's instruct FPR as 0.3%",
         quotes=["'Reaching conventional power there needs n in the thousands per cell'", "0.80 power at n ≈ 750 per arm"],
         rows=[],
         what="'n in the thousands per cell' (Instruct power) holds only at the transcribed 0.3%: the W3/W4 fork applies to it"),
    dict(item="N5", fig="zero pauses", quotes=["Scope: the 344-session screen run"], rows=["L101"],
         what="scope: zero pauses in the screen run; the f1 smokes before it paused three times"),
    dict(item="N5", needle="**Yes -- there is a known artifact at the 0.12 dose", quotes=["the note should disclose it"],
         rows=["L105"], what="the CORR dose caveat: N5 says the note should disclose it (see section 5's note-locator branch)"),
    dict(item="N5", needle="A wording the record supports (a proposal for the design seat; domains named)",
         quotes=["at a corruption rate (.12) at which 2 of 16 items rendered unchanged"], rows=["L105"],
         what="N5's proposed wording for the caveat, with its domains"),
    dict(item="N5", fig="preprint 'at a dose a later calibration (§8.1) found below its visibility criterion'",
         quotes=["wording, not a number", "suggested replacement in §7d"], rows=["L105"],
         what="the preprint clause credits a calibration whose artifact is post-pin (bab921c): wording, not a number"),
    dict(item="N6", fig="preprint :111 gloss 'direct displacement of label logits'",
         quotes=["a definition error, not a transcription", "Routing is N1's and the design seat's"], rows=["L110", "L111", "L112"],
         what="the gloss on π̂_d is a definition error (a pick-discordance rate, not a logit displacement); routed to N1 and the design seat"),
    dict(item="N7", needle="2. **Failing-conjunct sentence", quotes=["it should say 'below frac 0.40'"], rows=[],
         what="'the negative pole clears its envelope everywhere' holds below frac 0.40 only"),
    dict(item="N7", needle="4. **B3 headline over-generalizes", quotes=["no stage's sign locks in the approach direction"],
         rows=[], what="the B3 headline's sign-lock wording over-generalizes (the reverse sign locks at base and sft)"),
    dict(item="N7", needle="7. **What G_c is", quotes=["it is not measured in units of the residual direction", "Routed to the design seat"],
         rows=["L113", "L114", "L115", "L116"],
         what="G_c is a pooled-SD gap on the A4 readout, on OLMo almost entirely a tail-level gap; not 'direction units' or a marker-token gap"),
    dict(item="N7", needle="9. **'Post-training sharpens the marking it inherits'",
         quotes=["Both sentences are defensible only if 'marking' means G_c"], rows=["L113", "L114", "L115", "L116"],
         what="'sharpens the marking' holds only if 'marking' means G_c; routed to the design seat with note 7"),
    dict(item="N7", needle="10. **'About five times larger at base'", quotes=["names neither pole nor dose"], rows=[],
         what="'about five times larger at base' needs its pole and dose (D+/G_c at frac 0.10)"),
    dict(item="N7", needle="11. **'Sham contrasts are exactly zero'.**", quotes=["the note should say which sham"], rows=["L117"],
         what="'sham 0.0' is the A4 sham; the B3 sham arm's pseudo-Deltas are not all zero"),
    dict(item="N7", needle="13. **For N14.**", quotes=["it is a marker-arm, map-level Delta"], rows=["L125", "L157"],
         what="OLMo DPO +0.1667 is a marker-arm map-level Delta, not a sham-arm statistic"),
    dict(item="N8", needle="3. Wrong referent", quotes=["G is the battery mean"], rows=["L135"],
         what="'the natural gap on that instrument (G = 0.316)' names the battery mean; that instrument's own gap is g_0 = 1.157"),
    dict(item="N8", needle="4. Wording: '9/12 and 10/12 on the remaining probes'", quotes=["the counts are over all 12 probes"],
         rows=["L134"], what="'9/12 and 10/12 on the remaining probes': the counts are over all 12 probes (8/11 and 9/11 over the rest)"),
    dict(item="N8", needle="5. Wording (PREPRINT-v1_0-draft.md", quotes=["holds at L44 only"], rows=[],
         what="'a clean overdose regime at f = .40' holds at L44 only"),
    dict(item="N8", needle="6. Wording (PREPRINT-v1_0-draft.md", quotes=["'monotonically' is the values-check's flagged gloss"],
         rows=["L142"], what="'coherence degrades monotonically' is a flagged gloss: one of four dose steps is resolved"),
    dict(item="N8", needle="7. Beside, same preprint sentence", quotes=["the two are different channels"], rows=[],
         what="'about a quarter of its short-context value' compares two channels"),
    dict(item="N8", needle="8. '≈ 0.51' self-indexed", quotes=["are layer-dependent"], rows=["L136", "L138", "L139"],
         what="'≈ 0.51', '≈ 0.85' and '≈ 0.16 at every layer' are layer-dependent (L48 values; six-layer ranges)"),
    dict(item="N8", needle="9. Precision:", quotes=["i.e. 0.83–0.87 at 2 dp"], rows=["L166"],
         what="'0.83–0.88' is 0.83–0.87 unrounded (double rounding); N8 routes the choice to N1/PI"),
    dict(item="N10", needle="- (a) Wording at", quotes=["'the between-direction variance in the label-choice probability P(keep)'"],
         rows=["L149"], what="R² = 0.53 is of P(keep), not of label logits; state its scope"),
    dict(item="N10", needle="- (b) 'horn-1 calibration'", quotes=["'a cycle-2 diagnostic on Qwen (2026-08-06)'"], rows=["L149"],
         what="'horn-1 calibration' should name the measurement; 'calibration' next to horn 1 names a different statistic"),
    dict(item="N10", needle="- (c) :222 attaches the magnitude", quotes=["Drop the number at :222 or keep it only with its scope"],
         rows=["L149"], what="the 0.53 attached to another group's on/off contrast: drop it there or keep it with its scope"),
    dict(item="N13", needle="- Q1 bet, wording correction for the note", quotes=["What the record supports:"], rows=["L089"],
         what="'timestamped 2026-08-18' is not evidenced in the record; N13 gives the supported wording"),
]
# default data directories for resolving bare artifact names in an item raw's source text
ITEM_DIRS = {"N2": ["data/olmo"], "N2vi": ["data/olmo"], "N3": ["data/echo", "data/k"], "N3c": ["data/echo"],
             "N4": ["data/e2a"], "N5": ["data/f"], "N6": ["data/e2b"], "N7": ["data/olmo"],
             "N8": ["data/e0", "data/e2d"], "N9": ["data/d"], "N14": ["data/e2a", "data/f", "data/olmo"]}

WORDS = r"zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|half"
TOKEN_RE = re.compile(r"\d+(?:[.,]\d+)*|\.\d+|\b(?:" + WORDS + r")\b", re.I)
EXT_RE = re.compile(r"\.(?:md|json|jsonl|npz|py|txt|svg|ipynb|sh)\b")
DIR_RE = re.compile(r"(?:^|[(`'\"])(?:data|results|scripts|valence_core|archive|notebooks|github\.com|jlens-qwen36)/")
HASH_RE = re.compile(r"(?<![0-9A-Za-z])(?=[0-9a-f]*[a-f])(?=[0-9a-f]*\d)[0-9a-f]{7,40}(?![0-9A-Za-z])")
DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
ARXIV_RE = re.compile(r"arXiv:\d{4}\.\d{4,5}|App\. [A-Z] Fig\. \d+|Fig\. \d+")
PREFIX_ID_RE = re.compile(r"(?:\b[Ll]ink[- ]|\bcards? |\bTier |\bStage |\bLevel |\bitem |\bv)$")


# ------------------------------------------------------------------ git helpers
def git(*args: str, binary: bool = False, check: bool = True):
    r = subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, check=check)
    return r.stdout if binary else r.stdout.decode("utf-8", "replace")


def show(rev: str, path: str) -> bytes:
    return git("show", f"{rev}:{path}", binary=True)


_FULL: dict = {}


def full(rev: str) -> str:
    # round 6: cached per process (the mutation self-test repeats the same lookups on every run)
    if rev not in _FULL:
        _FULL[rev] = git("rev-parse", rev + "^{commit}").strip()
    return _FULL[rev]


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


_TOPO: dict = {}


def topo_index(sha: str):
    """Position of a commit in `git rev-list --topo-order <AUDIT>` (0 = newest)."""
    if not _TOPO:
        for i, s in enumerate(git("rev-list", "--topo-order", AUDIT).split()):
            _TOPO[s] = i
    return _TOPO.get(sha)


_DATE: dict = {}


def cdate(sha: str) -> str:
    if sha not in _DATE:
        _DATE[sha] = git("show", "-s", "--format=%cI", sha).strip()
    return _DATE[sha]


_TREE: dict = {}


def tree(rev: str) -> list:
    if rev not in _TREE:
        _TREE[rev] = git("ls-tree", "-r", "--name-only", rev).splitlines()
    return _TREE[rev]


_LAST: dict = {}
_FIRST: dict = {}


def last_change(path: str, rev: str = PIN):
    k = (path, rev)
    if k not in _LAST:
        out = git("log", "-1", "--format=%H", rev, "--", path).strip()
        _LAST[k] = out or None
    return _LAST[k]


def first_add(path: str, rev: str = PIN):
    k = (path, rev)
    if k not in _FIRST:
        out = git("log", "--diff-filter=A", "--format=%H", rev, "--", path).split()
        _FIRST[k] = out[-1] if out else None
    return _FIRST[k]


_BLAME: dict = {}
_BLAME_L: dict = {}


def blame_line(path: str, rev: str, n: int):
    """The entry commit of one line: `git blame -L n,n --porcelain <rev> -- <path>` (the task's command), per line."""
    key = (path, rev, n)
    if key not in _BLAME_L:
        out = git("blame", "-L", f"{n},{n}", "--porcelain", rev, "--", path)
        _BLAME_L[key] = out.split()[0] if out else None
    return _BLAME_L[key]


def full_blame(path: str, rev: str):
    key = (path, rev)
    if key not in _BLAME:
        out = git("blame", "--porcelain", rev, "--", path)
        m = {}
        for ln in out.splitlines():
            mm = re.match(r"^([0-9a-f]{40}) \d+ (\d+)", ln)
            if mm:
                m[int(mm.group(2))] = mm.group(1)
        _BLAME[key] = m
    return _BLAME[key]


def blame_cross_check():
    """Every per-line blame used by the ledger, against one full-file `git blame --porcelain` per file."""
    res = []
    for (path, rev, n), s in sorted(_BLAME_L.items()):
        f = full_blame(path, rev).get(n)
        res.append(dict(path=path, rev=rev, line=n, L=s, full=f, equal=(s == f)))
    return res




# ------------------------------------------------------------------ tokenizing
def backtick_spans(s: str):
    return [(m.start(), m.end()) for m in re.finditer(r"`[^`]*`", s)]


def words(s: str):
    return [(m.start(), m.end(), m.group()) for m in re.finditer(r"\S+", s)]


def tokenize(s: str):
    return [(m.start(), m.end(), m.group()) for m in TOKEN_RE.finditer(s)]


def find_occ(s: str, sub: str, occ: int = 1):
    i = -1
    for _ in range(occ):
        i = s.find(sub, i + 1)
        if i < 0:
            return None
    return i


def generic_category(s: str, st: int, en: int, tok: str):
    """Generic exclusion rules for a token not inside a row or a hand exclusion."""
    for a, b in backtick_spans(s):
        if a <= st and en <= b:
            return "code, path or identifier in backticks"
    for m in DATE_RE.finditer(s):
        if m.start() <= st and en <= m.end():
            return "date"
    for m in HASH_RE.finditer(s):
        if m.start() <= st and en <= m.end():
            return "commit or file hash"
    for m in ARXIV_RE.finditer(s):
        if m.start() <= st and en <= m.end():
            return "source identifier or locator (arXiv id, figure number)"
    for a, b, w in words(s):
        if a <= st and en <= b and (EXT_RE.search(w) or DIR_RE.search(w)):
            return "file name or path"
    if st > 0 and s[st - 1] == "§":
        return "section reference"
    if tok[0].isdigit() and st > 0 and (s[st - 1].isalpha() or s[st - 1] == "_"):
        return "identifier (digits attached to a name: item, objection, campaign, version, layer)"
    if tok[0].isdigit() and "." not in tok and st > 1 and s[st - 1] == "-" and s[st - 2].isalpha():
        # a decimal after 'word-' is a quantity ('sub-0.05-cosine'), not a name; integers stay names (random-1, link-5)
        return "identifier (digits attached to a name: item, objection, campaign, version, layer)"
    if PREFIX_ID_RE.search(s[max(0, st - 7):st]):
        return "identifier (link, card, tier, stage, level, item or version number)"
    if tok.lower() in ("one", "two") and s[en:].startswith("-sided"):
        return "test name (one-/two-sided)"
    return None


def extract_block_tokens(lines):
    lo, hi = BLOCK_RANGE
    toks = []
    for n in range(lo, hi + 1):
        s = lines[n - 1]
        for st, en, t in tokenize(s):
            toks.append(dict(line=n, start=st, end=en, text=t))
    return toks


def classify_tokens(lines, toks):
    spans = {}
    for r in ROWS:
        s = lines[r["line"] - 1]
        i = find_occ(s, r["span"], r.get("occ", 1))
        if i is None:
            raise SystemExit(f"row {r['id']}: span not found at block :{r['line']}: {r['span']!r}")
        r["_span"] = (i, i + len(r["span"]))
        spans.setdefault(r["line"], []).append(("row", r["id"], i, i + len(r["span"])))
    for (ln, sub, occ, cat) in EXCLUDE:
        s = lines[ln - 1]
        i = find_occ(s, sub, occ)
        if i is None:
            raise SystemExit(f"exclusion span not found at block :{ln}: {sub!r}")
        spans.setdefault(ln, []).append(("excl", cat, i, i + len(sub)))
    for t in toks:
        for kind, ident, a, b in spans.get(t["line"], []):
            if (a < t["end"] and t["start"] < b) and not (a <= t["start"] and t["end"] <= b):
                raise SystemExit(f"{kind} {ident}: span cuts token {t['text']!r} at block :{t['line']}")
    out = []
    for t in toks:
        s = lines[t["line"] - 1]
        cls = None
        for kind, ident, a, b in spans.get(t["line"], []):
            if kind == "row" and a <= t["start"] and t["end"] <= b:
                cls = ("row", ident)
                break
        if cls is None:
            for kind, ident, a, b in spans.get(t["line"], []):
                if kind == "excl" and a <= t["start"] and t["end"] <= b:
                    cls = ("excluded (hand)", ident)
                    break
        if cls is None:
            g = generic_category(s, t["start"], t["end"], t["text"])
            cls = ("excluded (generic)", g) if g else ("UNASSIGNED", None)
        t = dict(t)
        t["class"], t["detail"] = cls
        if cls[0] == "row":
            g = generic_category(s, t["start"], t["end"], t["text"])
            t["inside_row_but_identifier"] = bool(g and g.startswith("identifier"))
        out.append(t)
    return out


# ------------------------------------------------------------------ item raws
class ItemRaws:
    def __init__(self):
        self.md = {}
        self.js = {}
        self.sha = {}
        for item, (md, js) in RAWS.items():
            b = show(AUDIT, md)
            self.md[item] = b.decode("utf-8").split("\n")
            self.sha[md] = sha256(b)
            if js:
                jb = show(AUDIT, js)
                self.js[item] = json.loads(jb)
                self.sha[js] = sha256(jb)

    def md_locator(self, item, n):
        return f"{RAWS[item][0]}@{AUDIT}:{n}"

    def figures(self, item):
        return self.js[item].get("figures", [])

    def find_md_line(self, item, needle, prefer_after=None, startswith=False):
        hits = []
        for i, l in enumerate(self.md[item], start=1):
            if (l.startswith(needle) if startswith else needle in l):
                hits.append(i)
        if prefer_after is not None and len(hits) > 1:
            later = [h for h in hits if h > prefer_after]
            if later:
                hits = later
        return hits

    def figures_header_line(self, item):
        for i, l in enumerate(self.md[item], start=1):
            if re.match(r"^#+ .*(Per-figure status|Figures|Figure statuses|^## 7\. Figures)", l) or \
               re.match(r"^## (0\. Per-figure status|Figures|7\. Figures|Figure statuses|8\. Figures|6\. Figures)", l):
                return i
        return None

    def table_row_cells(self, item, n):
        """Split a markdown table row (or an N11 ' | ' text row) into cells, with its header."""
        line = self.md[item][n - 1]
        if line.startswith("|"):
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
            h = n - 1
            while h > 0 and not re.match(r"^\|\s*-", self.md[item][h - 1]):
                h -= 1
            hdr_line = self.md[item][h - 2] if h >= 2 else ""
            hdr = [c.strip() for c in re.split(r"(?<!\\)\|", hdr_line.strip().strip("|"))]
        else:
            cells = [c.strip() for c in line.split(" | ")]
            h = n - 1
            hdr = None
            while h > 0:
                l = self.md[item][h - 1]
                if l.startswith("figure | "):
                    hdr = [c.strip() for c in l.split(" | ")]
                    break
                h -= 1
        if hdr is None or len(hdr) != len(cells):
            raise SystemExit(f"{item} line {n}: table cells {len(cells)} vs header {hdr}")
        return dict(zip(hdr, cells)), hdr

    def resolve(self, ref):
        """Return a dict describing one item-raw row for a ref."""
        item, kind = ref[0], ref[1]
        if kind == "fig":
            figs = self.figures(item)
            idx = [i for i, f in enumerate(figs) if f.get("figure") == ref[2]]
            if len(idx) != 1:
                raise SystemExit(f"{item}: figure {ref[2]!r} found {len(idx)} times")
            i = idx[0]
            f = figs[i]
            hdr = self.figures_header_line(item)
            fig_md = f["figure"].replace("|", "\\|")
            if item in ("N2", "N2vi"):
                needles = [f"| {i + 1} | {f['figure']} |", f"| {i + 1} | {fig_md} |"]
            else:
                needles = [f"| {f['figure']} |", f"| {fig_md} |"]
            hits = []
            for nd in needles:
                hits = self.find_md_line(item, nd, prefer_after=hdr, startswith=True)
                if hits:
                    break
            if len(hits) != 1:
                raise SystemExit(f"{item}: md row for {ref[2]!r}: {hits}")
            n = hits[0]
            return dict(item=item, kind=kind, key=ref[2], json_path=RAWS[item][1], json_index=i,
                        md_line=n, locator=self.md_locator(item, n) + f" (JSON figures[{i}])",
                        figure=f["figure"], printed=f.get(VALUE_KEY[item]),
                        source=f.get(SOURCE_KEY.get(item, "source")), status=f.get("status"),
                        status_condition=f.get("status_condition") or None, note=f.get("note", ""))
        if kind == "id":
            figs = self.figures(item)
            idx = [i for i, f in enumerate(figs) if f.get("id") == ref[2]]
            if len(idx) != 1:
                raise SystemExit(f"{item}: id {ref[2]!r} found {len(idx)} times")
            i = idx[0]
            f = figs[i]
            hits = self.find_md_line(item, f"| {ref[2]} | ", startswith=True)
            if len(hits) != 1:
                raise SystemExit(f"{item}: md row for id {ref[2]!r}: {hits}")
            n = hits[0]
            return dict(item=item, kind=kind, key=ref[2], json_path=RAWS[item][1], json_index=i,
                        md_line=n, locator=self.md_locator(item, n) + f" (JSON figures[{i}], id {ref[2]})",
                        figure=f["figure"], printed=f.get(VALUE_KEY[item]), source=f.get("source"),
                        status=f.get("status"), status_condition=f.get("status_condition") or None,
                        note=f.get("note", ""))
        if kind in ("mdrow", "txtrow"):
            hits = self.find_md_line(item, ref[2], startswith=True)
            if len(hits) != 1:
                raise SystemExit(f"{item}: row {ref[2]!r}: {hits}")
            n = hits[0]
            cells, hdr = self.table_row_cells(item, n)
            fig = cells.get(hdr[0]) if hdr[0] != "#" else cells.get(hdr[1])
            printed = next((cells[h] for h in hdr if h.startswith("value")), None)
            sh = next((h for h in hdr if h.startswith("source") or h.startswith("named in")), None)
            source = cells.get(sh) if sh else None
            if sh and not sh.startswith("source") and source:
                source = f"[{sh}] {source}"
            status = cells.get("status") or cells.get(hdr[-1])
            note = cells.get("note", "")
            if kind == "txtrow" and item == "N11":
                rn = self.find_md_line(item, "1. Count. ", startswith=True)
                if len(rn) == 1:
                    note = (f"N11 referent note 1 ({self.md_locator(item, rn[0])}, quoted): " + self.md[item][rn[0] - 1][3:])
            if item == "N13":
                # row 15 of the provenance table: carry its document cell, commit, and status cell
                fig = cells.get("document (version of record)", cells.get(hdr[1]))
                printed = "; ".join(f"{h}: {cells[h]}" for h in hdr[2:4])
                status = cells.get(hdr[-1])
                rn = self.find_md_line(item, "- Q1 bet, wording correction for the note")
                if len(rn) != 1:
                    raise SystemExit("N13 referent note line not found")
                nl = self.md[item][rn[0] - 1]
                s1 = "the phrase 'timestamped 2026-08-18' occurs at AUDIT-note-release-v1_2.md@bbc9ffe:91; RESULTS.md@bbc9ffe:8195; RESULTS.md@bbc9ffe:9072"
                s2 = ("PROPOSAL-g-ontogeny-of-evaluation.md@72b09a9:32, PROPOSAL-g-ontogeny-of-evaluation.md@72b09a9:33, "
                      "PROPOSAL-g-ontogeny-of-evaluation.md@72b09a9:56")
                for x in (s1, s2):
                    if x not in nl:
                        raise SystemExit(f"N13 referent note lacks {x!r}")
                # N13 row 15 has no source column. The source cell is N1's construction from N13's referent note:
                # the bet's own text (s2). The lines that carry the phrase (s1) are carriers of the wording, not
                # sources of the bet; they stay in the note text and are counted as note locators (section 5).
                # Round 3: N13 cites the bet at 72b09a9 (its first-text pin); the source cell cites the same lines at
                # the record pin, each matched by exact line text (asserted unique), so every record locator in the
                # ledger is @bbc9ffe.
                pg, first = "PROPOSAL-g-ontogeny-of-evaluation.md", "72b09a9"
                old = show(first, pg).decode("utf-8").split("\n")
                new = show(PIN, pg).decode("utf-8").split("\n")
                mapped = []
                for k in (32, 33, 56):
                    hit = [i + 1 for i, l in enumerate(new) if l == old[k - 1]]
                    if len(hit) != 1 or not old[k - 1].strip():
                        raise SystemExit(f"L089: {pg}@{first}:{k} not matched uniquely at {PIN}: {hit}")
                    mapped.append(hit[0])
                between = git("log", "--format=%h", f"{first}..{PIN}", "--", pg).split()
                source = ("[constructed by N1 from N13's referent note; N13 row 15 has no source column] "
                          "the bet's own text and date, at the record pin: "
                          + ", ".join(f"{pg}@{PIN}:{m}" for m in mapped)
                          + f" (N13's referent note cites the same lines at {first}:32, :33, :56, the text's first "
                          f"commit; each line's text equal, found by exact match; the file changed between the two "
                          f"pins only at {', '.join(between) or 'no commit'})")
                note = (f"N13's referent note ({self.md_locator(item, rn[0])}, quoted): " + nl[2:])
            return dict(item=item, kind=kind, key=ref[2], md_line=n, locator=self.md_locator(item, n),
                        figure=fig, printed=printed, source=source, status=status, note=note,
                        header=hdr)
        if kind == "mdline":
            spec = ref[3]
            hits = self.find_md_line(item, ref[2])
            if len(hits) != 1:
                raise SystemExit(f"{item}: line {ref[2]!r}: {hits}")
            n = hits[0]
            l = self.md[item][n - 1]
            for k in ("printed", "status", "source"):
                if k == "source" and spec.get("source_line_needle"):
                    continue
                if spec.get(k) is not None and spec[k] not in l:
                    raise SystemExit(f"{item} :{n}: {k} substring not in line: {spec[k]!r}")
            src = spec.get("source")
            loc = self.md_locator(item, n)
            if spec.get("source_line_needle"):
                sh = self.find_md_line(item, spec["source_line_needle"])
                if len(sh) != 1 or spec["source"] not in self.md[item][sh[0] - 1]:
                    raise SystemExit(f"{item}: source line {spec['source_line_needle']!r}: {sh}")
                loc += f" (source named at :{sh[0]})"
            return dict(item=item, kind=kind, key=ref[2], md_line=n, locator=loc,
                        figure=ref[2], printed=spec.get("printed"), source=src,
                        status=(spec["status"] if spec.get("status") is not None
                                else "(no per-figure status in the item raw)"),
                        note="(values quoted verbatim from the line; asserted present)")
        if kind == "notrun":
            return dict(item=item, kind=kind, key=None, md_line=None, locator="(no item raw: N19 not run)",
                        figure=None, printed=None, source=None, status="not run (pending the PI)", note=ref[2])
        if kind == "none":
            return dict(item=None, kind=kind, key=None, md_line=None, locator="(no item-raw row)",
                        figure=None, printed=None, source=None,
                        status="(no row of its own in the item raw)", note=ref[2])
        raise SystemExit(f"unknown ref kind {kind}")


# ------------------------------------------------------------------ sources
LOC_RE = re.compile(
    r"(?P<path>(?:[A-Za-z0-9_.{},*<>~+\-]+/)*[A-Za-z0-9_.{},*<>~+\-]+\.(?:md|json|jsonl|npz|py|txt|sh|ipynb))"
    r"@(?P<rev>[0-9a-f]{7,40})(?::(?P<lines>\d+(?:-\d+)?(?:,\s?\d+(?:-\d+)?)*))?")
CONT_RE = re.compile(r"^,\s*:(\d+(?:-\d+)?)")
ART_RE = re.compile(
    r"(?<![\w/.@-])(?P<path>(?:data|results/raw|scripts|valence_core|archive)/[A-Za-z0-9_./{},*<>\-]+?"
    r"\.(?:json|jsonl|npz|txt|py|md))(?![\w@])")
# a bare artifact name; internal dots allowed (round 3: 'e0_axes.meta.json')
REL_RE = re.compile(r"(?<![\w/.@{-])(?P<name>[A-Za-z0-9_{},*<>\-]+(?:\.[A-Za-z0-9_{},*<>\-]+)*\.(?:json|jsonl|npz))(?![\w@])")
# round 3: slash-abbreviated alternatives sharing a suffix ('d2/d3_scores.json' = d2_scores.json and d3_scores.json),
# read as alternatives only when the literal is not itself the tail of a tracked path
SLASHALT_RE = re.compile(r"(?<![\w/.@{-])(?P<alts>[A-Za-z0-9]+(?:/[A-Za-z0-9]+)+)(?P<rest>_[A-Za-z0-9_.\-]*\.(?:json|jsonl|npz))(?![\w@])")
# any file-like name in a source text (round 3: names the parser leaves unresolved are listed, section 3)
NAME_SCAN_RE = re.compile(r"[A-Za-z0-9_{},*<>.~+/\-]*[A-Za-z0-9_}*>]\.(?:json|jsonl|npz|md|py|txt|sh|ipynb)(?![\w])")
CLONE_RE = re.compile(r"jlens-qwen36/[\w./\-]+")
ROOTMD_RE = re.compile(r"(?<![\w/.@-])(?P<name>[A-Z][A-Za-z0-9_.\-]*\.md)(?![\w@])")
MODULE_OVERRIDE = {"valence_core.regression.analysis": "valence_core/regression/analysis.py"}


def expand_braces(p: str):
    m = re.search(r"\{([^{}]*)\}", p)
    if not m:
        return [p]
    out = []
    for alt in m.group(1).split(","):
        out += expand_braces(p[:m.start()] + alt + p[m.end():])
    return out


def resolve_paths(p: str, rev: str = PIN, hints=()):
    """Expand braces/placeholders/globs against the tree at rev. A bare name is matched first at the root,
    then under the hint directories (the directories of full paths in the same source text, then the item's
    data directories), then anywhere under data/."""
    pats = [re.sub(r"<[^>]*>", "*", x) for x in expand_braces(p)]
    paths = tree(rev)
    hits = []
    for pat in pats:
        if "/" in pat:
            hits += [x for x in paths if fnmatch.fnmatchcase(x, pat)]
        elif any(fnmatch.fnmatchcase(x, pat) for x in paths):
            hits += [x for x in paths if fnmatch.fnmatchcase(x, pat)]      # a root file (RESULTS.md, LOCK-h.md, ...)
        else:
            got = []
            for d in hints:
                got = [x for x in paths if os.path.dirname(x) == d and fnmatch.fnmatchcase(os.path.basename(x), pat)]
                if got:
                    break
            if not got:
                got = [x for x in paths if x.startswith("data/") and fnmatch.fnmatchcase(os.path.basename(x), pat)]
            hits += got
    seen = []
    for h in hits:
        if h not in seen:
            seen.append(h)
    return seen


def parse_lines(spec: str):
    out = []
    for part in re.split(r",\s?", spec):
        if "-" in part:
            a, b = part.split("-")
            out += list(range(int(a), int(b) + 1))
        elif part:
            out.append(int(part))
    return out


def parse_sources(text: str):
    """Locators and artifact paths named in an item raw's source text."""
    if not text:
        return []
    text = str(text)
    found = []
    taken = []
    for m in LOC_RE.finditer(text):
        path, rev, lines = m.group("path"), m.group("rev"), m.group("lines")
        ln = parse_lines(lines) if lines else []
        j = m.end()
        while True:
            c = CONT_RE.match(text[j:])
            if not c:
                break
            ln += parse_lines(c.group(1))
            j += c.end()
        taken.append((m.start(), j))
        found.append(dict(raw=text[m.start():j], path=path, rev=rev, lines=ln, span=(m.start(), j)))
    def free(a, b):
        return all(not (x <= a < y) for x, y in taken)
    for m in CLONE_RE.finditer(text):
        if free(m.start(), m.end()):
            taken.append((m.start(), m.end()))
            found.append(dict(raw=m.group(), path=m.group(), rev=None, lines=[], kind="clone", span=(m.start(), m.end())))
    for m in ART_RE.finditer(text):
        if free(m.start(), m.end()):
            taken.append((m.start(), m.end()))
            found.append(dict(raw=m.group(), path=m.group("path"), rev=None, lines=[], span=(m.start(), m.end())))
    for m in SLASHALT_RE.finditer(text):
        if free(m.start(), m.end()):
            lit = m.group()
            tails = [x for x in tree(PIN) if x == lit or x.endswith("/" + lit)]
            taken.append((m.start(), m.end()))
            if tails:
                # the literal is the tail of a tracked path: a path, not alternatives
                found.append(dict(raw=lit, path=tails[0] if len(tails) == 1 else "*/" + lit, rev=None, lines=[],
                                  span=(m.start(), m.end())))
            else:
                names = [a + m.group("rest") for a in m.group("alts").split("/")]
                found.append(dict(raw=lit, path="{" + ",".join(names) + "}", rev=None, lines=[], relative=True,
                                  slash_alternatives=names, span=(m.start(), m.end())))
    for m in REL_RE.finditer(text):
        if free(m.start(), m.end()):
            taken.append((m.start(), m.end()))
            found.append(dict(raw=m.group(), path=m.group("name"), rev=None, lines=[], relative=True,
                              span=(m.start(), m.end())))
    for m in ROOTMD_RE.finditer(text):
        if free(m.start(), m.end()):
            taken.append((m.start(), m.end()))
            found.append(dict(raw=m.group(), path=m.group("name"), rev=None, lines=[], rootmd=True,
                              span=(m.start(), m.end())))
    for mod, path in MODULE_OVERRIDE.items():
        i = text.find(mod)
        if i >= 0:
            found.append(dict(raw=mod, path=path, rev=None, lines=[], module=True, span=(i, i + len(mod))))
    return found


def unparsed_names(text: str, found):
    """File-like names in a source text that no parsed source covers (round 3)."""
    if not text:
        return []
    text = str(text)
    spans = [x["span"] for x in found if x.get("span")]
    out = []
    for m in NAME_SCAN_RE.finditer(text):
        a, b = m.start(), m.end()
        if not any(x < b and a < y for x, y in spans):
            out.append(m.group())
    return out


def classify_source(s, hints=()):
    """Attach kind and entry commit(s) to one parsed source."""
    path, rev = s["path"], s.get("rev")
    s = dict(s)
    if s.get("kind") == "clone":
        s.update(kind="outside the record (gitignored clone)", entries=[])
        return s
    if path == BLOCK:
        s.update(kind="the block itself (quotes the note; not a source)", entries=[])
        return s
    if path.startswith(AUDIT_RAW_PREFIX) or os.path.basename(path).startswith("2026-10-08_note-"):
        p = path if "/" in path else "results/raw/" + path
        c = last_change(p, AUDIT)
        s.update(kind="audit raw", resolved=[p], entries=[dict(commit=c, how=f"git log -1 {AUDIT} -- {p}")])
        return s
    if rev and not s["lines"] and not path.startswith("data/") and path.endswith(".md") and "/" not in path.replace("archive/", ""):
        s.update(kind="document reference without a line locator (no entry commit)", entries=[])
        return s
    r = rev or PIN
    paths = resolve_paths(path, r, hints if s.get("relative") else ())
    if s.get("relative") and len(paths) > 1 and not any(ch in path for ch in "*{<"):
        s["ambiguous"] = True
    if s.get("slash_alternatives"):
        miss = [n for n in s["slash_alternatives"] if not resolve_paths(n, r, hints)]
        if miss:
            s["unresolved_alternatives"] = miss
    if not paths:
        tracked_head = path in tree("HEAD")
        on_disk = (REPO / path).exists() if "/" in path or s.get("rootmd") else False
        why = "untracked (absent from any clone)" if on_disk and not tracked_head else "not a tracked path at the pin"
        local = sorted(REPO.glob(path)) if ("/" in path and any(ch in path for ch in "*?[")) else ([REPO / path] if on_disk else [])
        if local and not tracked_head:
            ign = subprocess.run(["git", "-C", str(REPO), "check-ignore", "-q", "--", str(local[0].relative_to(REPO))]).returncode == 0
            if ign:
                why = f"gitignored; local only, {len(local)} file{'s' if len(local) != 1 else ''} on this machine"
        s.update(kind=f"outside the record ({why})", entries=[])
        return s
    ents = []
    if s["lines"]:
        if len(paths) != 1:
            s.update(kind="line locator on an ambiguous path", resolved=paths, entries=[])
            return s
        p = paths[0]
        for n in s["lines"]:
            c = blame_line(p, r, n)
            e = dict(commit=c, how=f"git blame -L {n},{n} --porcelain {r} -- {p}", line=n)
            if p.startswith("archive/"):
                # information only: copy detection across files, since archive files were created by copying
                out = git("blame", "-C", "-L", f"{n},{n}", "--porcelain", r, "--", p)
                e["commit_copy_detected"] = out.split()[0] if out else None
            ents.append(e)
        s.update(kind="line locator", resolved=paths, entries=ents)
        return s
    for p in paths:
        if rev and rev != PIN:
            c = last_change(p, rev)
            ents.append(dict(commit=c, how=f"git log -1 {rev} -- {p} (artifact as cited at {rev})", path=p))
        else:
            c = last_change(p, PIN)
            fa = first_add(p, PIN)
            ents.append(dict(commit=c, first_add=fa, how=f"git log -1 {PIN} -- {p}", path=p))
    s.update(kind="artifact", resolved=paths, entries=ents)
    return s


def latest(commits):
    cs = [c for c in commits if c]
    if not cs:
        return None
    idx = [(topo_index(c), c) for c in cs]
    bad = [c for i, c in idx if i is None]
    if bad:
        raise SystemExit(f"commit(s) not ancestors of {AUDIT}: {bad}")
    return min(idx)[1]


def earliest(commits):
    """The oldest of the commits in `git rev-list --topo-order <AUDIT>` (round 3: a row's first carrier)."""
    cs = [c for c in commits if c]
    if not cs:
        return None
    idx = [(topo_index(c), c) for c in cs]
    bad = [c for i, c in idx if i is None]
    if bad:
        raise SystemExit(f"commit(s) not ancestors of {AUDIT}: {bad}")
    return max(idx)[1]


def newer(a, b):
    """True if commit a is later than commit b in the topo order of the audit pin."""
    return topo_index(a) < topo_index(b)


def short(c):
    return c[:7] if c else "-"


# ------------------------------------------------------------------ status helpers
def base_status(st):
    """The vocabulary term the item raw's status string carries; 'mixed' if it carries more than one."""
    if st is None:
        return None
    s = st.lower()
    if s.startswith("not run"):
        return "not run"
    found = []
    for m in re.finditer(r"reproduced|log-only|not found|discrepant|computed-new", s):
        if m.group() not in found:
            found.append(m.group())
    if len(found) == 1 and s.startswith(found[0]):
        return found[0]
    if len(found) > 1:
        return "mixed"
    return "other"


# ------------------------------------------------------------------ note mode
def note_text(path: Path):
    raw = path.read_bytes()
    t = raw.decode("utf-8", "replace")
    if path.suffix.lower() == ".svg":
        parts = re.findall(r"<(text|tspan|title|desc)\b[^>]*>(.*?)</\1>", t, flags=re.S)
        t = "\n".join(html.unescape(re.sub(r"<[^>]+>", "", p[1])) for p in parts)
    return raw, t


def num_value(tok: str):
    """Decimal value of a numeral token ('.5' = 0.5; '1,000' = 1000), or None."""
    from decimal import Decimal, InvalidOperation
    t = tok.replace(",", "") if re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", tok) else tok
    try:
        return Decimal(t)
    except InvalidOperation:
        return None


FRAC_RE = re.compile(r"(?<![\d.])(\d+)\s*/\s*(\d+)(?!\.?\d)")
# a unit suffix right after a numeral: percent; percentage points ('pp', 'points'); a multiplier attached to the
# numeral ('17×', '33x'; never 'x' with a space, which is multiplication)
SUFFIX_RE = re.compile(r"(\s?%)|(\s?pp\b|\s(?:percentage )?points?\b)|(×|x(?![A-Za-z0-9]))")
SIGNS = {"+": "+", "−": "-", "-": "-", "±": "±"}


def sign_of(s: str, st: int) -> str:
    """'+', '-', '±' or '' (unsigned) for the numeral starting at s[st]. A '-' or '−' right after a letter, digit,
    '.', '_', ')' or ']' is a range dash or an identifier hyphen, not a sign."""
    if st == 0 or s[st - 1] not in SIGNS:
        return ""
    p = s[st - 2] if st >= 2 else " "
    if s[st - 1] in "-−" and (p.isalnum() or p in ".)]_"):
        return ""
    return SIGNS[s[st - 1]]


def units(s: str, lo: int = 0, hi: int = None):
    """Figure units in s[lo:hi]: a fraction k/n is one unit; otherwise each numeral (TOKEN_RE), with its sign
    (sign_of), its unit kind (percent / percentage points / multiplier, from SUFFIX_RE; else a plain number) and
    its decimal places. Tokens that a generic rule excludes (dates, hashes, paths, identifiers, ...) are returned
    with their category in 'excluded'."""
    hi = len(s) if hi is None else hi
    out, used = [], []
    for m in FRAC_RE.finditer(s, lo, hi):
        g = generic_category(s, m.start(1), m.end(1), m.group(1)) or generic_category(s, m.start(2), m.end(2), m.group(2))
        if g:
            continue
        out.append(dict(start=m.start(), end=m.end(), text=m.group(), kind="fraction", cls="frac",
                        val=(int(m.group(1)), int(m.group(2))), sign="", dec=0, isint=True, excluded=None))
        used.append((m.start(), m.end()))
    for st, en, tok in tokenize(s[lo:hi]):
        st, en = st + lo, en + lo
        if any(a <= st and en <= b for a, b in used):
            continue
        g = generic_category(s, st, en, tok)
        v = num_value(tok)
        if v is None:
            kind = "word" if tok[0].isalpha() else "other"
            out.append(dict(start=st, end=en, text=tok, kind=kind, cls=kind, val=tok.lower(), sign="", dec=0,
                            isint=False, excluded=g))
            continue
        plain = tok.replace(",", "") if re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", tok) else tok
        isint = "." not in plain
        dec = 0 if isint else len(plain.split(".")[1])
        m = SUFFIX_RE.match(s, en) if en < len(s) else None
        if m and m.group(1):
            kind, cls, end = "percent", "pct", m.end()
        elif m and m.group(2):
            kind, cls, end = "percentage points", "pp", m.end()
        elif m and m.group(3):
            kind, cls, end = "multiplier", "times", m.end()
        else:
            kind = "decimal" if not isint else ("integer" if v >= 100 else "small integer")
            cls, end = "num", en
        out.append(dict(start=st, end=end, text=s[st:end], kind=kind, cls=cls, val=v, sign=sign_of(s, st),
                        dec=dec, isint=isint, excluded=g))
    return sorted(out, key=lambda x: x["start"])


def sign_class(u):
    if u["cls"] in ("frac", "word", "other") or u["val"] == 0:
        return "0"
    return {"": "pos", "+": "pos", "-": "neg", "±": "pm"}[u["sign"]]


def strict_match(u, x):
    """Same unit kind, same value, same sign class (unsigned = positive; zero is sign-neutral), and both integers
    or both decimals (decimal places may differ: .20 = 0.200)."""
    if u["cls"] != x["cls"]:
        return False
    if u["cls"] in ("frac", "word", "other"):
        return u["val"] == x["val"]
    a, b = sign_class(u), sign_class(x)
    return u["val"] == x["val"] and u["isint"] == x["isint"] and (a == b or "0" in (a, b))


def loose_match(u, x):
    """Same digits or the same proportion, with a different unit kind, sign or integer/decimal form (e.g. 0.3% vs
    -0.3, 0.3% vs 0.003, 0 vs 0.000). Never a match; listed as a candidate to read."""
    if strict_match(u, x):
        return False
    numeric = ("num", "pct", "pp", "times")
    if u["cls"] not in numeric or x["cls"] not in numeric:
        return False
    if u["val"] == x["val"]:
        return True
    if u["cls"] == "pct" and x["cls"] == "num" and u["val"] / 100 == x["val"]:
        return True
    if x["cls"] == "pct" and u["cls"] == "num" and x["val"] / 100 == u["val"]:
        return True
    return False


def rounds_equal(a, b):
    """True if the more precise of two decimal units of the same kind and sign class rounds (half-up) to the less
    precise one (two or more places)."""
    from decimal import Decimal, ROUND_HALF_UP
    if a["cls"] != b["cls"] or a["cls"] not in ("num", "pct", "pp", "times") or a["isint"] or b["isint"]:
        return False
    sa, sb = sign_class(a), sign_class(b)
    if not (sa == sb or "0" in (sa, sb)) or a["dec"] == b["dec"]:
        return False
    hi, lo = (a, b) if a["dec"] > b["dec"] else (b, a)
    if lo["dec"] < 2:          # a one-decimal figure is too coarse to identify a row by rounding
        return False
    q = Decimal(1).scaleb(-lo["dec"])
    return hi["val"].quantize(q, rounding=ROUND_HALF_UP) == lo["val"].quantize(q)


CTX_STOP = set("the a an at of on to in is by with its it as for or and from under per than vs via that this these "
               "those their there be are was were has have not no any every each all which what when where who how "
               "into onto over below above about one two three four five six seven eight nine ten zero half".split())
CTX_WORD_RE = re.compile(r"[^\W\d_][\w′'+−]*")


def ctx_words(text: str) -> set:
    """Context words: word tokens (letters first; may carry digits, primes, signs), lower-cased, primes as
    apostrophes; dropped: stop words and lower-case one-letter tokens."""
    out = set()
    for m in CTX_WORD_RE.finditer(text or ""):
        raw = m.group()
        w = raw.lower().replace("′", "'")
        if w in CTX_STOP:
            continue
        if len(w) < 2 and not raw.isupper():
            continue
        out.add(w)
    return out


COMMON_DF = 5
# round 3: a clause boundary in a note line -- ';', a table bar, a bullet, or a sentence end ('.', '!', '?' followed by
# whitespace or the end of the line; a decimal point is followed by a digit and is never a boundary)
CLAUSE_RE = re.compile(r"[;|•]|[.!?](?=\s|$)")


def clause_bounds(s: str, st: int, en: int):
    """The clause of line s that holds s[st:en]: from the last boundary before st to the first at or after en."""
    lo, hi = 0, len(s)
    for m in CLAUSE_RE.finditer(s):
        if m.end() <= st:
            lo = m.end()
        elif m.start() >= en:
            hi = m.start()
            break
    return lo, hi


def is_bare_small_int(u):
    return u["cls"] == "num" and u["kind"] == "small integer"


def watch_hit(u, key):
    if key[0] == "frac":
        return u["cls"] == "frac" and u["val"] == (key[1], key[2])
    if u["cls"] != key[0]:
        return False
    if u["val"] != num_value(str(key[1])):
        return False
    return len(key) < 3 or (not u["isint"] and u["dec"] == key[2])


def row_label(row):
    sts = sorted({rr["base_status"] or "none" for rr in row["refs"]})
    lab = "/".join(sts)
    if "discrepant" in sts and row["figure"] in DISC:
        lab += " " + DISC[row["figure"]][0]
    return lab


def note_mode(paths, rows, lines_block, raws, watch):
    """Match every numeral unit in each note/SVG against the ledger rows' units.

    A row's units are the non-excluded units of its span; a row whose span has no numeric unit takes the units of
    its primary item-raw rows' figure labels. A note unit is
      'matched'      if a row unit has the same unit kind, value and sign class (strict_match) AND the row's context
                     words (its span and its primary item-raw figure labels) agree with the words of the note
                     unit's own clause (clause_bounds) within 60 characters of it; labelled 'matched; value shared
                     by N rows (verify which)' when more than one row carries the value;
      'candidate'    if a strict match exists but no context word agrees ('verify context'), with the rows' spans;
      'not in ledger' otherwise, listing loose matches (same digits or proportion, other unit kind or sign),
                     rounding matches and item-raw figure rows carrying the same value, as pointers.
    Bare integers below 100 are 'weak only' or 'not in ledger (small integer)' and never counted as matches.
    Separately, every unit whose value is on the watch-list is surfaced, whatever it matches."""
    row_units, row_ctx, row_info = [], {}, {}
    for r in rows:
        s = lines_block[r["line"] - 1]
        a, b = r["_span"]
        us = [dict(u, via="span") for u in units(s, a, b) if not u["excluded"]]
        if not any(u["cls"] in ("num", "pct", "pp", "times", "frac") for u in us):
            for rr in r["refs"]:
                if rr.get("figure"):
                    us += [dict(u, via="item-raw figure label") for u in units(str(rr["figure"])) if not u["excluded"]]
        row_units.append((r["id"], us))
        ctx = ctx_words(r["figure"])
        for rr in r["refs"]:
            ctx |= ctx_words(str(rr.get("figure") or ""))
        row_ctx[r["id"]] = ctx
        row_info[r["id"]] = (r["figure"], row_label(r))
    # a context word in COMMON_DF or more rows' contexts (stage, arm and map names: dpo, sft, label, ...) is common;
    # a match needs one uncommon agreeing word or two agreeing words of any kind
    df = {}
    for ws in row_ctx.values():
        for x in ws:
            df[x] = df.get(x, 0) + 1
    cand = []
    for item in raws.js:
        for i, f in enumerate(raws.figures(item)):
            blob = " ".join(str(f.get(k, "")) for k in ("figure", VALUE_KEY.get(item, "value"), "value", "printed", "reproduced"))
            cand.append((item, i, f.get("figure"), f.get("status"), [u for u in units(blob) if not u["excluded"]]))

    def lab(rid, extra=""):
        sp, st = row_info[rid]
        return f"{rid} '{sp}' [{st}]" + extra

    out = []
    for p in paths:
        path = Path(p)
        if not path.is_absolute():
            path = REPO / path
        raw, text = note_text(path)
        lines = text.split("\n")
        res = dict(path=p, sha256=sha256(raw), n_lines=len(lines), numerals=[], watch_hits=[])
        for n, s in enumerate(lines, start=1):
            for u in units(s):
                # round 3: context words only from the clause that holds the unit, and within 60 characters of it
                lo_, hi_ = clause_bounds(s, u["start"], u["end"])
                ctxs = s[max(lo_, u["start"] - 60):min(hi_, u["end"] + 60)]
                entry = dict(line=n, text=u["text"], kind=u["kind"], sign=u["sign"] or "(none)",
                             context=s[max(0, u["start"] - 40):u["end"] + 40])
                for w in watch:
                    if any(watch_hit(u, k) for k in w["keys"]) and u["excluded"] not in ("date", "commit or file hash"):
                        res["watch_hits"].append(dict(line=n, text=u["text"], kind=u["kind"], context=entry["context"],
                                                      watch=w["id"], locator=w["locator"], what=w["what"],
                                                      excluded=u["excluded"]))
                if u["excluded"]:
                    entry["excluded"] = u["excluded"]
                    res["numerals"].append(entry)
                    continue
                strict = []
                for rid, us in row_units:
                    if any(strict_match(u, x) for x in us) and rid not in strict:
                        strict.append(rid)
                if is_bare_small_int(u):
                    entry["match"] = "weak only" if strict else "not in ledger (small integer)"
                    entry["weak"] = [lab(r) for r in strict]
                    res["numerals"].append(entry)
                    continue
                cw = ctx_words(ctxs)
                matched, candidates = [], []
                for rid in strict:
                    common = sorted(row_ctx[rid] & cw)
                    if len(common) >= 2 or any(df[x] < COMMON_DF for x in common):
                        matched.append(lab(rid, " (context: " + ", ".join(common[:4]) + ")"))
                    else:
                        candidates.append(lab(rid, f" (context: only the common word '{common[0]}')" if common else ""))
                loose = [rid for rid, us in row_units if rid not in strict and any(loose_match(u, x) for x in us)]
                entry["match"] = ("matched" if matched else "candidate (verify context)" if candidates else "not in ledger")
                if matched and len(strict) > 1:
                    # round 3: a value several rows share is flagged even when the context agrees with one of them
                    entry["match"] = f"matched; value shared by {len(strict)} rows (verify which)"
                entry["n_rows_with_value"] = len(strict)
                entry["matched_rows"] = matched
                entry["candidate_rows"] = candidates
                if loose:
                    entry["loose_rows"] = [lab(r) for r in loose]
                if not strict and u["cls"] in ("num", "pct", "pp", "times"):
                    rnd = [rid for rid, us in row_units if any(rounds_equal(u, x) for x in us)]
                    if rnd:
                        entry["rounds_to"] = [lab(r) for r in rnd]
                if not matched:
                    entry["item_raw_candidates"] = [f"{it} figures[{i}] ({fig}; {stt})" for it, i, fig, stt, us in cand
                                                    if any(strict_match(u, x) or loose_match(u, x) for x in us)][:8]
                res["numerals"].append(entry)
        out.append(res)
    return out


# ------------------------------------------------------------------ N1 final: the note's own rows (--note-rows)
# Round 4 (N1 final, 2026-10-09). The PI placed RESEARCH-NOTE-v0_3-draft.md (it supersedes the block's v0.2) and the
# Digest seat's two SVGs at root. Ten mapper chains (a mapper, one adversarial checker, the mapper's revision) mapped
# every numeral unit of the three files -- the --note matcher's units plus the number words it cannot see -- to a
# source and a status: results/raw/2026-10-09_note-N1-note-rows.json. --note-rows reads that mapping as data,
# validates every row mechanically, and adds section 9. The checks are consistency checks on the mapping (the unit is
# on the cited note line; a cited source line carries a value the row says it does; a cited ledger row exists and
# carries the row's status); they re-derive no figure. A row that fails a check fails the run unless it carries a
# 'validation_note' saying why. Round 5 (below, nr_validate_row) adds checks and binds each note to the one check it
# explains.
NOTE_ROUTED = {
    "RESEARCH-NOTE-v0_3-draft.md": ("5a34309ffe402cdeb99d0c60635adac67e08db23d82fc496142c656777d14871", ""),
    "2026-10-06_F1b_five-link-panels.svg": ("192250ca", "0afd"),
    "2026-10-06_F2_macar-lineage-roc_post.svg": ("5e4fc91c", "1fef"),
}
FINAL_NOTE = "RESEARCH-NOTE-v0_3-draft.md"
NR_STATUSES = ("reproduced", "log-only", "computed-new", "discrepant", "not found", "not run")
NR_MAPS = ("ledger-row", "item-raw", "audit-raw-new", "record", "none")
NR_WORDS = dict(zero=0, one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9, ten=10, eleven=11,
                twelve=12, twenty=20, seventy=70, twice=2, second=2, third=3, fourth=4, half=0.5)
NR_S9_RE = re.compile(r"^'(?P<u>.+?)' in node '")
NR_NUM_RE = re.compile(r"(?<![A-Za-z0-9_.])(?:\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?|\.\d+)(?![0-9A-Za-z_])")
NR_SPEC = r"\d+(?:-\d+)?(?:,\s?\d+(?:-\d+)?)*"
NR_ABBR = {k: v[0] for k, v in RAWS.items()}
NR_ABBR["ledger"] = "results/raw/2026-10-08_note-N1-claims-ledger.md"
NR_LOC_RE = re.compile(
    r"(?P<path>(?:[A-Za-z0-9_.\-]+/)*[A-Za-z0-9_.\-]+\.(?:md|json|jsonl|txt|py|svg))@(?P<rev>[0-9a-f]{7,40})"
    r"(?::(?P<spec>" + NR_SPEC + r"))?"
    r"|(?<![\w/.\-])(?P<abbr>N\d+[a-z]*|ledger)@(?P<arev>[0-9a-f]{7,40})(?::(?P<aspec>" + NR_SPEC + r"))?"
    r"|(?<![\w/.])@(?P<rev2>[0-9a-f]{7,40})(?::(?P<spec2>" + NR_SPEC + r"))?"
    r"|(?<=[\s(;,]):(?P<spec3>" + NR_SPEC + r")")
NR_STRIP_RES = [re.compile(r"\w+\[\d+\](?:\[\d+\])*"), re.compile(r"\b\d{1,2}:\d{2}(?::\d{2})?Z?\b"), HASH_RE, ARXIV_RE,
                # round 5: a section sign with a dotted number ('§7.3'), and a version inside a hyphenated name
                # ('OLMo-3.1-32B'), are identifiers, never values
                re.compile(r"§\s*\d+(?:\.\d+)*(?:\s*[-–,]\s*\d+(?:\.\d+)*)*"), re.compile(r"(?<=[A-Za-z])-\d+(?:\.\d+)+"),
                # round 6: a dotted section number ('section 5.6') is stripped whole
                re.compile(r"(?i)\b(?:rows?|sections?|items?|notes?|findings?|conditions?|nodes?|lines?|steps?|tiers?|"
                           r"parts?|appendix|§)\s*\d+(?:\.\d+)*(?:\s*[-–,]\s*\d+(?:\.\d+)*)*")]
# section 9's not-figure summary: the mapper's reason, grouped by the first rule whose pattern it contains
NR_REASON_GROUPS = [
    ("axis tick label (SVG)", r"axis tick"),
    ("commit-hash fragment", r"commit hash|hash"),
    ("date, year or decade", r"\bdate|year|decade"),
    ("citation apparatus (arXiv id, journal, cited section)", r"arxiv|journal|citation|in a cited work"),
    ("section or heading number / reference", r"section|heading"),
    ("link or figure identifier", r"\blink|figure id|figure label|figure identifier|cross-reference"),
    ("model name, version or size label", r"model|version|product"),
    ("identifier, item id, campaign or file name, path", r"identifier|item id|question id|cell|campaign|tier|test name|"
                                                         r"file name|path"),
    ("list ordinal or label", r"ordinal|list label|bullet"),
    ("procedure or plot parameter, method name", r"parameter|procedure|setting|instruction|quantile|plot|method name|"
                                                 r"label pair"),
    ("prose: pronoun, rhetoric, editorial, or a count of the note's own parts", r"."),
]
# span-note markers (section 9f): the upper-case status markers the mappers wrote in their notes, in order of
# appearance (longer forms first, so 'NOT APPLIED' is never also read as 'APPLIED'); lower-case prose is not read
NR_NOTE_MARK_RE = re.compile(r"\b(NOT APPLIED|PARTLY APPLIED|NOT CARRIED|CHOICE NOT MADE|OPEN CONDITIONAL STOP|ACTIVE STOP|"
                             r"POSSIBLE STOP|APPLIED|PARTLY|OPEN|CORRECTED|FIRES|REJECTED)\b")
NR_OPEN_MARKS = ("NOT APPLIED", "PARTLY APPLIED", "PARTLY", "NOT CARRIED", "CHOICE NOT MADE", "OPEN", "OPEN CONDITIONAL STOP",
                 "ACTIVE STOP", "POSSIBLE STOP", "FIRES")
# discrepant note rows (section 9e): the block :23 branch each row's own cause reads into, with a quote from that
# cause (asserted present). Keys are span#seq.
NR_DISC = {
    # round 5 (finding 1): S1#26, S1#27, S1#34, S1#140 and S4#19 are no longer discrepant; they carry their item raws'
    # statuses and their corrections are recorded separately (9i)
    "S1#71": ("T", "Transcription (layer scope)"),
    "S1#72": ("T", "Transcription (layer scope)"), "S1#73": ("C", "The note now carries the raw's correction"),
    "S1#134": ("T", "Transcription (layer scope)"),
    "S4#4": ("T", "Transcription, in the domain"), "S4#5": ("T", "('discrepant (transcription)', domain)"),
    "S4#10": ("T", "Transcription, in the domain"), "S4#11": ("T", "Status carried from L058 (domain; see .81)"),
    "S4#31": ("T", "Transcription (item raw 'discrepant (transcription)', carried)"),
    "S4#32": ("T", "Transcription, in referent and scope"),
    "S4#33": ("T", "Status carried from L049 (referent and scope; see .02)"),
    "S5#13": ("FORK-W3", "Range end, belongs with the next row (0–0.003)"),
    "S5#14": ("FORK-W3", "Transcription on Code's reading"),
    "S5#38": ("C", "the discrepancy is resolved in the note"),
    "S5#57": ("FORK-W3", "Range end, belongs with the next row (0–0.3%)"),
    "S5#58": ("FORK-W3", "Transcription on Code's reading"),
    "S6#68": ("NT", "not transcription (item raw)"),
    "S8#68": ("FORK-W3", "N2vi row 8 is discrepant"), "S8#69": ("FORK-W3", "transcription on Code's reading"),
    "S10#36": ("FORK-W3", "transcription on Code's reading"), "S10#60": ("FORK-W3", "transcription on Code's reading"),
}
NR_DISC_PATH = {
    "T": "transcription (the row's cause): block :23 corrects the note to the reproduced value; not a STOP",
    "C": ("corrected in the note: the item raw's discrepancy was a transcription in an earlier text and the note now "
          "carries the reproduced value (corrected_in_note, verified: the item raw's correction quoted from its line "
          "and the note's figure tied to the source value at level A); the status is carried, not upgraded, and the "
          "row counts as passing (round 5, finding 6)"),
    "NT": ("not transcription (the row's cause): under block :23 a STOP on the item unless the clause is reworded; "
           "Code's reading, the PI and the design seat decide"),
    "FORK-W3": ("the W3 fork (N2vi section 12, condition 3): transcription on Code's reading, and then corrected to 0 "
                "(+0.9 pp wherever TPR - FPR is carried) under block :23; a STOP if that reading is not accepted. The "
                "note carries the value as a range ('0–0.003', '0–0.3%') and F2 as the point 0.003, which settles "
                "neither branch"),
}
# watch-list outcome per conditional STOP (section 9f). 'rows': span#seq of note rows that carry (or collide with) the
# watched value, each with the status asserted; 'quote': a substring asserted in that row's cause/comment or in the
# span note named; 'outcome': Code's one-line summary of the rows and span notes cited.
NR_WATCH = [
    dict(id="W1", rows=[], outcome="not carried: no unit or text match in the note or either SVG"),
    dict(id="W2", rows=[], outcome="not carried: no unit or text match in the note or either SVG"),
    dict(id="W3", rows=[("S5#14", "discrepant"), ("S5#58", "discrepant"), ("S8#69", "discrepant"),
                        ("S10#36", "discrepant"), ("S10#60", "discrepant")],
         note=("S10", "W3 FIRES twice"),
         outcome=("CARRIED, uncorrected: the note gives the source's instruct FPR as the range '0–0.003' (:92, :208) "
                  "and '0–0.3%' (:98); F2 plots it as the point 0.003 (text nodes 46, 73). The fork stays open: "
                  "corrected to 0 on Code's transcription reading, a STOP if that reading is not accepted; the note "
                  "and F2 change together. The +0.6 pp form is not carried")),
    dict(id="W4", rows=[("S6#47", "reproduced"), ("S8#61", "log-only"), ("S10#31", "log-only")],
         outcome=("not carried: the three hits are value collisions (f1 SOLV +.020 at :111; the source's base hit "
                  "rate 0.001 at :208 and in F2 node 40), not the retired criterion's power")),
    dict(id="W5", rows=[("S10#66", "not found"), ("S10#67", "not found")],
         note=("S10", "W5 FIRES at node 79"),
         outcome=("CARRIED in F2 (node 79, '~800 injected and ~80 control trials per stage'): not found, so cut, or "
                  "restated with its premise (eight concepts) and unit. The note does not print 800/80; its derived "
                  "0.6 (:98, :173) falls under the same condition 4 (cut unless the premise is stated; S5 and S7 span "
                  "notes)")),
    dict(id="W6", rows=[("S1#66", "reproduced"), ("S7#73", "reproduced")],
         outcome=("corrected: the note carries 154/154 (:3, :175), not 103/103; N11's PASS is provisional (pre-tag, "
                  "local clone) and is to be re-run with --ref at the tag, a condition on the tag (9g)")),
    dict(id="W7", rows=[("S1#42", "reproduced"), ("S6#5", "reproduced")],
         outcome=("not triggered: the note carries 54 of 101 as the audit-v2 correction of record (reproduced, N4 :362), "
                  "not the not-found quotation '54 of 101 valid sessions'; the third matcher hit (:215) is '54' inside "
                  "the commit hash c54c4e0")),
    dict(id="W8", rows=[("S6#68", "discrepant")],
         outcome=("CARRIED in the STOP-triggering form: ':111 about 1% of rounds, uniformly across arms including "
                  "sham' (L102: not transcription; sham 7/351 = 1.99%). A live conditional STOP unless reworded; N5's "
                  "suggested wording is at N5 :122")),
    dict(id="W9", rows=[], outcome="not carried (no '33 attempts' in the note or either SVG)"),
    dict(id="W10", rows=[], outcome="not carried (no '+.094' in the note or either SVG)"),
]
NR_WATCH_EXTRA = [
    dict(id="d′ 'roughly 1–1.5 at DPO' (block watch item; no matcher key)",
         what="the d′ wording the item raws tie to N2(v)/(vi); no matcher key, searched as text",
         rows=[("S1#26", "computed-new"), ("S1#27", "computed-new"), ("S8#78", "computed-new"), ("S8#79", "computed-new")],
         text="1–1.5",
         outcome=("CARRIED at :3 (the design seat's changelog) and :208 (the PI section), both outside the post body, "
                  "which says 'about 1 and 2' (:98), '≈ 1–2' (:100), 'about 1–2' (:164) and 'roughly 0.6, 1.5 or 2' "
                  "(:173). Round 5: all four rows carry N2 5(b)'s status (computed-new); the range wording is one "
                  "correction, N1's own reading, not an item raw's, recorded on S1#26, S1#27 and S8#79 (9i; S8 records "
                  ":208's range once, on its upper end, so S8#78 carries none; round 6); the design seat decides")),
    dict(id="'n in the thousands' (4g C8; no matcher key)", rows=[], text="n in the thousands",
         what="Instruct power 'n in the thousands per cell' (N2vi; holds only at the transcribed 0.3%, the W3 fork)",
         outcome="not carried"),
]

# open items for the PI and the design seat (section 9h): each names the rows (with their status, asserted) and the
# span notes (a quote, asserted) it rests on; 'text' is Code's one-paragraph summary of those rows and notes.
NR_T_ROWS = ["S1#71", "S1#72", "S1#134", "S4#4", "S4#5", "S4#10", "S4#11", "S4#31", "S4#32", "S4#33"]
NR_NF_ROWS = ["S1#117", "S1#147", "S3#36", "S5#72", "S5#77", "S7#19", "S7#20", "S7#24", "S7#25", "S7#28", "S7#66", "S10#66",
              "S10#67"]
NR_OPEN = [
    dict(id="O1", what="TL;DR :27 'five natural-reinforcer contrasts inside the sham envelope'",
         rows=[("S1#140", "reproduced")], corrections=["S1#140"], notes=[("S1", "POSSIBLE STOP (Code's reading; the PI and design seat decide)")],
         text=("A wording correction, N1's own reading (round 5, finding 1): the row carries N5's status (the DIFF row "
               "reproduces, N5 @09c3a8c:206, :79), and N5 has no 'envelope' wording and classifies nothing here. The "
               "clause does not hold for DIFF, whose |Δ| .0957 exceeds f1's sham pseudo-Δ .0455 (N5 @09c3a8c:79, :74); "
               "a form the record supports is 'five natural-reinforcer contrasts, none passing its screen'. No item "
               "raw raises a STOP on it; whether the wording is a correction or something more is the design seat's "
               "call. The body's f1 bullet (:111) does not make the claim.")),
    dict(id="O2", what="link 5 f1 (:111) 'about 1% of rounds, uniformly across arms including sham' (W8)",
         rows=[("S6#68", "discrepant")], notes=[("S6", "W8 (f1 termination per arm) -- carried in the STOP-triggering form")],
         text=("L102: not a transcription (sham 7/351 = 1.99%); a live conditional STOP unless the clause is reworded; "
               "N5's suggested wording is at N5 @09c3a8c:122.")),
    dict(id="O3", what="the source's instruct false-alarm rate (W3): note :92, :98, :208; F2 text nodes 46 and 73",
         rows=[("S5#14", "discrepant"), ("S5#58", "discrepant"), ("S8#69", "discrepant"), ("S10#36", "discrepant"),
               ("S10#60", "discrepant")], notes=[("S10", "W3 FIRES twice")],
         text=("Carried as a range in the note ('0–0.003', '0–0.3%') and as the single point 0.003 in F2. The fork "
               "(N2vi @09c3a8c:619, condition 3) is the PI's and design seat's: accept Code's transcription reading and "
               "write 0.000 (+0.9 pp wherever TPR − FPR is carried; F2's point at (0.000, 0.009)), or treat it as a STOP. "
               "The note and F2 change together.")),
    dict(id="O4", what="d′ 'roughly 1–1.5 at DPO' at :3 and :208",
         rows=[("S1#26", "computed-new"), ("S1#27", "computed-new"), ("S8#78", "computed-new"), ("S8#79", "computed-new")],
         corrections=["S1#26", "S1#27", "S8#79"],
         notes=[("S1", "POSSIBLE STOP 2"), ("S8", "d′ wording at :208")],
         text=("A wording correction, N1's own reading (round 5, finding 1): all four rows carry N2 5(b)'s status "
               "(computed-new, N2 @09c3a8c:376), and no item raw classifies the wording. The post body says 'about 1 "
               "and 2' (:98), '≈ 1–2' (:100), 'about 1–2' (:164) and 'roughly 0.6, 1.5 or 2' (:173); the computed DPO "
               "d′ by assumed n is +0.611, +1.197, +1.525, +1.995 (N2 @09c3a8c:344, :382, :386, :390). Read as a stale "
               "summary of the body, '1–1.5' is corrected to '1–2' at :3 and :208; read as a claim about which n "
               "premise holds, it would be a STOP on N2 under block :23. That fork is the S1 and S8 mappers' reading, "
               "not an item raw's; the design seat decides. :208's 'must not be tightened' is the PI section's own "
               "instruction. The correction is recorded on S1#26, S1#27 and S8#79 (9i); S8 records :208's range once, on "
               "its upper end, so S8#78 carries none (round 6).")),
    dict(id="O5", what="the π̂ gloss 'direct displacement of the label logits' at :58 and :170 (N6; ledger 4g C13)",
         rows=[("S2#37", "reproduced"), ("S2#38", "reproduced"), ("S7#61", "reproduced")],
         corrections=["S2#37", "S2#38", "S7#61"],
         notes=[("S2", "OPEN CONDITIONAL STOP, NOT APPLIED"), ("S7", "LEAKAGE CERTIFICATION (:170, C13)")],
         text=("Conditional; the design seat's call (round 6, n1chk2 finding 6, which found round 5's 'Not a STOP' "
               "overstated N6). The values reproduce. N6's own row for the gloss is 'discrepant': a definition error, "
               "not a transcription, with no number discrepant (N6 @09c3a8c:493). N6 raises no STOP, reads it as a "
               "sentence correction, and says that whether such a row is a figure STOP or a sentence correction is "
               "N1's and the design seat's call, not N6's (:505). N1 reads it as a sentence correction too: π̂_d is a "
               "pick-discordance rate, not a logit displacement, and N6's note-ready short form is at :249. It is "
               "recorded as a wording correction on the three rows (9i). If the design seat does not accept that "
               "reading, block :23's non-transcription branch makes it a STOP on N6. The S2 span note's conditional "
               "framing stands (its round-6 annotation in 9f).")),
    dict(id="O6", what="the N2(ii) STOP on link 4's ROC paragraph",
         rows=[], notes=[("S1", "N2(ii) 'resolved' (line 3): partly met"), ("S5", "ACTIVE STOP N2(ii)"),
                         ("S10", "ACTIVE STOP carried (N2(ii)")],
         text=("Note :3 and :209 call it resolved by the rewording at :96, which names three of the six "
               "outcome-relevant differences N2 lists (N2 @09c3a8c:190); whether that discharges it is the design "
               "seat's call. F2 still says 'GREEDY — the same protocol at temperature 0.0' (text node 47), so the STOP "
               "stays active on F2's greedy series until F2 is reworded or the series withheld.")),
    dict(id="O7", what="F2 as placed is the 2026-10-06 draft, not the annotated post version",
         rows=[], notes=[("S10", "F2 departs from block :34 and contradicts note v0.3")],
         text=("F2 carries no d′, c or Fisher p annotations, which block :34 directs for the post version and note :13 "
               "and :3 describe. Section 9 covers F2 as placed; an annotated F2 needs its own N1 pass (or :13 and :3 are "
               "reworded).")),
    dict(id="O8", what="not found: cut from the note under block :23",
         rows=[(k, "not found") for k in NR_NF_ROWS], notes=[],
         text=("Thirteen units (9d). Where the figure is an external literature or historical claim ('seventy years', "
               "Tagliabue et al.'s 'five families', 57.7% / 79.7%, 'one of three sizes', the two arms, 'eleven "
               "published designs'), the rows leave to the PI whether block :23's cut covers a citation; the ablation "
               "d′ ≈ 1.8 (:100, twice) has no source at all; F2's ~800 / ~80 is W5 (O11). Round 5 (finding 3) adds "
               "S1#117, 'three months of pre-registered experiments' (:20): no record line carries the duration; the "
               "record states the start (July 2026) and N13's earliest pre-registration is 2026-08-04 (N13 "
               "@09c3a8c:56), 66 days before the note's date. Cut, or reworded to what the record carries.")),
    dict(id="O9", what="N19: the 0.394 and the 0.70 (:144, :210), the clause around them, and TL;DR :29",
         rows=[("S1#145", "computed-new"), ("S7#29", "reproduced"), ("S7#33", "reproduced"), ("S8#84", "reproduced"),
               ("S8#85", "reproduced")], corrections=["S1#145", "S7#33"],
         notes=[("S1", "TL;DR :29 (the two indicators carry most of the optimist-sceptic gap)"), ("S8", ":210 (N19), REVISED")],
         text=("Round 5 (the PI's routing 10): the rows are re-mapped to N19's raw, committed at e0fd85c. The 0.394 and "
               "the 0.70 reproduce there (N19 @e0fd85c:119, :120), so block :125's cut does not apply and the "
               "[verify → N19] brackets at :144 and :210 are discharged (removing them is the design seat's edit). "
               "'Moves nothing' holds (computed-new, :121). The 'because … weakly undemanding (false-positive rate "
               "0.70)' clause does not hold on this vector (computed-new, post-hoc, :122): a demanding false-positive "
               "rate leaves the strike just as inert. TL;DR :29's 'carry most of the gap' is contradicted by N19's "
               "post-hoc section 8: striking both indicators closes 17.8% of the gap under equal credences (14.3% "
               "under the cell-28 credences; at most 35.8%), N19 @e0fd85c:151, :169. Both are sentences for the design "
               "seat and the PI, not verdicts (rule 11).")),
    dict(id="O10", what="link 3 (:88) 'with the re-derived diagnostic pre-registered as the next step'",
         rows=[], notes=[("S4", "Line 88's 'with the re-derived diagnostic pre-registered as the next step'")],
         text=("The record contradicts it: ADDENDUM-k1's Stage 1b was STOPPED twice and is uncommitted "
               "(RESULTS.md@bbc9ffe:1912-1921, :2090-2096). N1's own finding (S4); no item raw routes it.")),
    dict(id="O11", what="W5: F2 text node 79 ('~800 injected and ~80 control trials per stage'); the derived 0.6 at :98 and :173",
         rows=[("S10#66", "not found"), ("S10#67", "not found"), ("S5#61", "computed-new"), ("S7#68", "computed-new")],
         notes=[("S10", "W5 FIRES at node 79")],
         text=("F2's clause is cut, or restated with its premise (eight concepts) and unit (N2vi @09c3a8c:620, condition "
               "4); the note's 0.6 falls under the same condition (cut unless the premise is stated).")),
    dict(id="O12", what="the published e2a pair leads TL;DR :27 and F1b's link-5 bar",
         rows=[("S1#137", "reproduced"), ("S1#138", "reproduced")], notes=[("S1", "TL;DR :27 leads with the published pair")],
         text=("TL;DR :27 (and F1b's state bar) give +0.039 from 55/102, p .24, while note :3 and :108 call 54/101, "
               "+0.035, p .275 the correction of record. Both reproduce (N4 @09c3a8c:355-356, :362); an internal "
               "inconsistency for the design seat, not a figure error (S1; S9's open item 1).")),
    dict(id="O13", what="transcription corrections routed and not applied (block :23 correction branch)",
         rows=[(k, "discrepant") for k in NR_T_ROWS], notes=[("S4", "Transcription corrections routed to this paragraph by N3 (i)")],
         text=("Each row's cause names the correction: 'L50–L63' for '.94' (:26, :84); 'from L51' for label_b's "
               "'.81–.96' (:3, :85; N3 and N3c give this series different statuses); '≈ .10' or '≤ .103' for the leak "
               "median (:86); 'on the mixed random block masks B3x/B4x, toward the first round's label' for the "
               "pseudo-shift (:86), whose 'that a random direction produces too' S4 flags as well (the signed shift was "
               "computed on random masks only). The MLP lower end ('.59', :3, :85) is a precision correction since "
               "round 5 (O17).")),
    dict(id="O14", what="Epistemic status (:20) 'Everything quantitative is from a committed record'",
         rows=[], notes=[("S1", "Epistemic status (:20) says")],
         text=("Holds only if the committed audit raws count as record (the note's computed-new figures live only "
               "there; 9g) and fails for the not-found figures (O8), among them the line's own 'three months' "
               "(S1#117, round 5).")),
    dict(id="O15", what="'committed before data' at :179 (and :166)",
         rows=[], notes=[("S8", "Disclosure at :179")],
         text=("Broader than N13 supports: the cycle-2 'pre-registered rule (|t| < 1)' first appears in its own result "
               "commit, and some amendments inside arcs came after part of their data (N13 @09c3a8c:965, :983, :994). "
               "S8 offers a scoped form tied to the "
               "provenance table.")),
    dict(id="O17", what="precision corrections: double rounding (round 5, findings 1 and 4; the rule in section 10)",
         rows=[("S1#34", "computed-new"), ("S4#19", "computed-new"), ("S3#64", "reproduced")], notes=[],
         corrections=["S1#34", "S4#19", "S3#64"],
         text=("One rule for every double rounding: the item raw's status is carried and the rounding is recorded as a "
               "precision correction (9i). The MLP lower end '.60' (:3, :85) rounds the print 0.5950 of the stored "
               "0.594963, which is '.59' at two decimals (N3 @09c3a8c:479 applies the same rounding to its draft); "
               "the purity–potency upper end '0.88' (:76) rounds the three-decimal 0.875 of 0.8747, which is '0.87' "
               "(N8 @02b6a61:263 leaves the choice to N1 and the PI). Whether the note writes the direct rounding or "
               "keeps the printed one with a precision note is the PI's choice; neither is a STOP.")),
]


def nr_unit(r):
    m = NR_S9_RE.match(r.get("text") or "")
    return m.group("u") if m else (r.get("text") or "")


def nr_dec(tok):
    from decimal import Decimal, InvalidOperation
    t = tok.replace(",", "") if re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", tok) else tok
    try:
        d = Decimal(t)
    except InvalidOperation:
        return None
    return (d, len(t.split(".")[1]) if "." in t else 0, tok)


def nr_tokens(s):
    return [v for v in (nr_dec(m.group()) for m in NR_NUM_RE.finditer(s or "")) if v]


def nr_values(text):
    """The values a row's source_value states: ISO dates (matched literally) and numerals (unsigned; unicode minus,
    '+', '%', thousands separators and a missing leading zero normalised), after removing locators, JSON indexes,
    times, hashes, arXiv ids and 'row 15'-style labels."""
    s = str(text or "")
    dates = DATE_RE.findall(s)
    s = DATE_RE.sub(" ", s)
    s = NR_LOC_RE.sub(" ", s)
    for rx in NR_STRIP_RES:
        s = rx.sub(" ", s)
    return dates, nr_tokens(s)


def nr_same(a, b):
    from decimal import Decimal, ROUND_HALF_UP
    if a[0] == b[0]:
        return "equal"
    hi, lo = (a, b) if a[1] > b[1] else (b, a)
    if lo[1] >= 2 and hi[1] > lo[1] and hi[0].quantize(Decimal(1).scaleb(-lo[1]), rounding=ROUND_HALF_UP) == lo[0]:
        return "rounds"
    return None


def nr_parse_locs(text):
    """Every pinned locator in a locator string: path@rev[:lines], an item abbreviation (N3c@rev:lines, ledger@rev),
    a bare @rev:lines (same path), and a bare :lines after a space, '(' , ';' or ',' (same path and rev)."""
    out, last = [], None
    for m in NR_LOC_RE.finditer(str(text or "")):
        if m.group("path"):
            last, spec = (m.group("path"), m.group("rev")), m.group("spec")
        elif m.group("abbr"):
            last = (NR_ABBR[m.group("abbr")], m.group("arev")) if m.group("abbr") in NR_ABBR else None
            spec = m.group("aspec")
        elif m.group("rev2"):
            last, spec = ((last[0], m.group("rev2")) if last else None), m.group("spec2")
        else:
            spec = m.group("spec3")
        if last is None:
            continue
        out.append(dict(path=last[0], rev=last[1], lines=parse_lines(spec) if spec else [], raw=m.group().strip()))
    return out


_NRSHOW: dict = {}


def nr_lines_at(rev, path):
    k = (rev, path)
    if k not in _NRSHOW:
        r = subprocess.run(["git", "-C", str(REPO), "show", f"{rev}:{path}"], capture_output=True)
        _NRSHOW[k] = r.stdout.decode("utf-8", "replace").split("\n") if r.returncode == 0 else None
    return _NRSHOW[k]


def nr_line(rev, path, n):
    ls = nr_lines_at(rev, path)
    return ls[n - 1] if ls is not None and 1 <= n <= len(ls) else None


NR_CARDINAL = {v: k for k, v in NR_WORDS.items() if k in ("one", "two", "three", "four", "five", "six", "seven", "eight",
                                                         "nine", "ten", "eleven", "twelve", "twenty", "seventy")}


def nr_unit_values(u):
    """The note unit's value, and the words to look for: the unit itself if it is a number word, and the cardinal of
    its value ('third' -> 'three')."""
    w = u.strip().lower()
    if w in NR_WORDS:
        v = NR_WORDS[w]
        return [nr_dec(str(v))], [x for x in dict.fromkeys([w, NR_CARDINAL.get(v)]) if x]
    if u.strip() == "½":
        return [nr_dec("0.5")], ["½"]
    vs = nr_tokens(u)
    return vs, [NR_CARDINAL[int(v[0])] for v in vs if v[1] == 0 and int(v[0]) in NR_CARDINAL]


def nr_ledger_ids(field):
    f = str(field or "").strip()
    if not f or f.lower().startswith("none"):
        return []
    return re.findall(r"L\d{3}", f)


def nr_row_ledger_ids(r):
    """A row's ledger ids: its ledger_row field; for a ledger-row map with no such field, the ids its locator names."""
    ids = nr_ledger_ids(r.get("ledger_row"))
    if not ids and r.get("maps_to") == "ledger-row" and not r.get("ledger_row"):
        return re.findall(r"\bL\d{3}\b", str(r.get("locator") or "")), "locator"
    return ids, "ledger_row"


# round 7 (r6chk finding 1b): 'Lnnn (related row: N2 row 37, computed-new)' names one related row of the ledger row
NR_REL_RE = re.compile(r"\(related row: (?P<item>N\d+[a-z]*) row (?P<n>\d+), (?P<st>reproduced|log-only|not found|"
                       r"discrepant|computed-new|not run)\)")
NR_RELONLY_RE = re.compile(r"\(related only\b")


def nr_related_entry(r, ledger):
    """The related row a 'related row: <item> row <n>, <status>' field names (its entry in the ledger row's 'related'
    list, matched by item and JSON index n-1), or None; and the match."""
    ids, _ = nr_row_ledger_ids(r)
    m = NR_REL_RE.search(str(r.get("ledger_row") or ""))
    if not m or not ids or ids[0] not in ledger:
        return None, m
    ent = [rr for rr in ledger[ids[0]]["related"] if rr.get("item") == m.group("item")
           and f"figures[{int(m.group('n')) - 1}]" in str(rr.get("locator") or "")]
    return (ent[0] if len(ent) == 1 else None), m


def nr_check_ledger(r, ledger):
    ids, frm = nr_row_ledger_ids(r)
    missing = [i for i in ids if i not in ledger]
    if missing:
        return dict(result=f"FAIL: ledger row(s) not in the ledger: {', '.join(missing)}", ids=ids)
    if not ids:
        return dict(result="FAIL: maps_to ledger-row names no ledger row", ids=ids) if r.get("maps_to") == "ledger-row" \
            else dict(result="n/a", ids=ids)
    # round 6 (finding 1): a row that names a ledger row carries that row's status whatever its maps_to (round 5
    # compared only ledger-row maps, so a remap to 'record' skipped the comparison)
    row = ledger[ids[0]]
    st = sorted({rr["base_status"] or "none" for rr in row["refs"]})
    rel = sorted({rr["base_status"] or "none" for rr in row["related"]})
    lr = str(r.get("ledger_row") or "")
    # round 7 (r6chk finding 1b): 'related only' names a ledger row that is context for the figure, not its row (the
    # row's own status check decides); 'related row: <item> row <n>, <status>' compares the status with that related
    # row only (round 6 accepted the primary row's status too, so 'reproduced' passed on S5#20, S5#22 and S5#23)
    if NR_RELONLY_RE.search(lr):
        return dict(result="n/a (related only: the ledger row is context, not the figure's row; the row's own status "
                           "check decides)", ids=ids, ledger_status=st)
    if "related" in lr.lower():
        ent, m = nr_related_entry(r, ledger)
        if m is None:
            return dict(result=f"FAIL: ledger_row mentions a related row in a form the script does not read", ids=ids)
        if ent is None:
            return dict(result=f"FAIL: the related row the field names ({m.group('item')} row {m.group('n')}) is not "
                               f"one of {ids[0]}'s related rows", ids=ids)
        b = ent["base_status"] or "none"
        if m.group("st") != b:
            return dict(result=f"FAIL: ledger_row says the related row is {m.group('st')}; it is {b}", ids=ids)
        if r["status"] != b:
            return dict(result=f"FAIL: status '{r['status']}' vs the related row's {b} ({ids[0]}: {m.group('item')} row "
                               f"{m.group('n')}; only the related row's status counts)", ids=ids, ledger_status=st,
                        related_status=[b])
        return dict(result="pass (via the related row the field names)", ids=ids, ledger_status=st, related_status=[b])
    if r["status"] in st:
        return dict(result="pass" + (" (id from the locator; the row has no ledger_row field)" if frm == "locator" else ""),
                    ids=ids, ledger_status=st)
    return dict(result=f"FAIL: status '{r['status']}' vs {ids[0]}'s {'/'.join(st)}", ids=ids, ledger_status=st,
                related_status=rel)


def nr_check_ledger_bind(r, ledger):
    """Round 7 (r6chk finding 2): the ledger row a row names is bound to the row's figure. Every ledger id the locator
    names is one the ledger_row names; and the first ledger_row id (the one whose status the row carries) is named in
    the locator, or the locator cites one of its item-raw rows' lines (same path and line number, the same text at
    both revisions; for 'related row: …' the related row's line; for 'related only' a primary or related row's)."""
    ids, frm = nr_row_ledger_ids(r)
    if not ids or any(i not in ledger for i in ids):
        return dict(result="n/a")
    loc = str(r.get("locator") or "")
    li = list(dict.fromkeys(re.findall(r"\bL\d{3}\b", loc)))
    extra = [i for i in li if i not in ids]
    if extra:
        return dict(result=f"FAIL: the locator names ledger row(s) {', '.join(extra)} that the row's ledger_row does not "
                           f"({', '.join(ids)})")
    if ids[0] in li:
        return dict(result="pass", how="named in the locator")
    lr = str(r.get("ledger_row") or "")
    if NR_RELONLY_RE.search(lr):
        ents = ledger[ids[0]]["refs"] + ledger[ids[0]]["related"]
    elif "related" in lr.lower():
        e_, _ = nr_related_entry(r, ledger)
        ents = [e_] if e_ else []
    else:
        ents = ledger[ids[0]]["refs"]
    cited = {}
    for l in nr_parse_locs(loc):
        for n in l["lines"]:
            cited[(l["path"], n)] = nr_line(l["rev"], l["path"], n)
    for e_ in ents:
        for l in nr_parse_locs(e_.get("locator")):
            for n in l["lines"]:
                t = nr_line(l["rev"], l["path"], n)
                if t is not None and cited.get((l["path"], n)) == t:
                    return dict(result="pass", how=f"cites {ids[0]}'s item-raw row {l['path']}:{n}")
    return dict(result=f"FAIL: nothing binds {ids[0]} to the row (the locator neither names it nor cites a line of its "
                       f"item-raw rows)")


# ------------------------------------------------------------------ round 5 (N1 final fixes, 2026-10-09)
# The final checker's findings 1-9 (scratch final_result.json, key 'fin') and the PI's N19 routing (10). Every check
# has a name. A failure is explained only by a row whose 'validation_exempts' maps that check (one of NR_EXEMPTABLE)
# to its failure message, and whose 'validation_note' says why. An exemption from 'locator-value' also needs a
# 'validation_quote' asserted on the row's first cited line. No note exempts a row from any other check (round 4's
# notes exempted the whole row). Round 5 matched the exemption as a substring of the message; round 6 (n1chk2
# finding 4) requires the whole message, names the values sought and the lines read in the locator-value message,
# and binds every exempted row to a fingerprint the script declares (NR_EXEMPT_FP), so a change to any of its
# mapping fields leaves the failure unexplained.
NR_EXEMPTABLE = ("locator-value", "source-values", "ledger-status", "ledger-span", "unit-stated")
NR_CORR_KINDS = ("wording", "precision", "scope")
NR_ITEMRAW_RE = re.compile(r"^results/raw/2026-10-0[89]_note-N\d+[a-z]*-[A-Za-z0-9_.\-]+\.(?:md|txt)$")
NR_RAW_MD = {v[0] for v in RAWS.values()}
NR_SEP_RE = re.compile(r"^\|\s*:?-")
# the matcher-unit -> kind assignment, frozen (finding 2): sha256 over one line per row, in file order,
# 'span#seq<TAB>note_file<TAB>note_line<TAB>unit<TAB>kind'. A run whose rows give another hash stops; a deliberate
# change of any row's kind (or of its unit or line) is made here as well, where it shows in the script's diff.
NR_KIND_SHA256 = "88dbdcc6cf021359562267cd7441ec250d807ff57f1d7b8c9fc6a78727bc50e2"

# ------------------------------------------------------------------ round 6 (N1 final fixes, round 2, 2026-10-09)
# The adversarial check of round 5 (n1chk2, scratch) found nine problems; section 11 gives each with its disposition.
# The constants below are the round's frozen declarations: each is asserted at every run, and a deliberate change to
# any of them is a visible change to this script.
NR_TAG_RE = re.compile(r"\[status:([^\]]*)\]")
# finding 7: the revisions a row may cite, by path class (full shas compared)
NR_PIN_RULES = (
    ("the provisional N1 ledger", lambda p: p.startswith("results/raw/2026-10-08_note-N1-claims-ledger"), ("6485da2",)),
    ("an N8 or N11 item raw", lambda p: p in ("results/raw/2026-10-08_note-N8-link2.md",
                                              "results/raw/2026-10-08_note-N11-smoke.txt"), ("09c3a8c", "02b6a61")),
    ("an item raw of 2026-10-08", lambda p: p.startswith("results/raw/2026-10-08_note-"), ("09c3a8c",)),
    ("an audit raw of 2026-10-09 (N19)", lambda p: p.startswith("results/raw/2026-10-09_note-"), ("e0fd85c",)),
    ("the record", lambda p: True, ("bbc9ffe",)),
)
# finding 7: the clause of every row, frozen like the kind assignment ('span#seq<TAB>clause', file order)
NR_CLAUSE_SHA256 = "fe98c899f111c586a3b0a17a3b8d1e9accbe7edc036419313c1be1c6b5b8bcae"
# finding 4: every row that carries an exemption, with a fingerprint of its mapping fields (nr_fingerprint). An
# exemption holds only for the row as it was when the exemption was declared here. Round 7 re-declares seven (S1#51, S4#24, S7#29,
# S7#33, S7#73, S8#84, S8#85), whose locators now name their ledger row (section 12c); their exemptions are unchanged.
NR_FP_FIELDS = ("note_file", "note_line", "text", "kind", "maps_to", "status", "ledger_row", "locator", "source_value",
                "status_basis", "corrected_in_note", "correction", "validation_exempts", "validation_quote",
                "validation_note")
NR_EXEMPT_FP = {
    "S1#51": "6ce2eef6c007fc71", "S1#59": "c91471234461f7c2", "S1#119": "3bb20c8fb9259a39", "S3#11": "fb85afd1b8aee5c6",
    "S3#59": "b1e79dfdb886dc61", "S4#24": "1a85bcd079edd8a8", "S5#47": "b699445a05877816", "S6#54": "c1ec1d332f5df2b1",
    "S6#80": "c8ca7fd470fa3494", "S6#84": "730211522c348e2b", "S7#12": "79bb37b36622b2db", "S7#15": "185af915fc9a34ad",
    "S7#29": "174f7c0af82c6597", "S7#33": "f90fb66e955cbb6f", "S7#73": "1b0578c1075c474a", "S8#84": "933a54de7eac0b7d",
    "S8#85": "1e40765e49368db4", "S9#85": "ebd5df3048ab46ac",
}
# finding 5: every correction (9i), its kind and whose reading it is: 'N1' (N1's own reading or rounding check; the
# 'whose' text starts "N1's") or an item ('whose' starts '<item> (' and the basis cites that item's raw). Round 7
# (r6chk finding 4b): and a fingerprint of the whole correction (nr_corr_fp: kind, text, whose and basis), so an N1-own
# correction's basis, and any correction's text, can change only together with this declaration
NR_CORRECTIONS = {
    "S1#26": ("wording", "N1", "99728e4b8b668778"), "S1#27": ("wording", "N1", "99728e4b8b668778"),
    "S1#34": ("precision", "N1", "2967b2da87a3b422"), "S1#140": ("wording", "N1", "4a5fbd2b0f2bd803"),
    "S1#145": ("wording", "N19", "80eaf0b09c3cc733"), "S2#37": ("wording", "N6", "859a7080cd05be6f"),
    "S2#38": ("wording", "N6", "859a7080cd05be6f"), "S3#64": ("precision", "N8", "84776afd1647dbae"),
    "S4#19": ("precision", "N1", "2967b2da87a3b422"), "S7#33": ("wording", "N19", "8ebbc7b67cd99cfa"),
    "S7#61": ("wording", "N6", "859a7080cd05be6f"), "S8#79": ("wording", "N1", "86a93f88058cdd02"),
}
# finding 2: the wording an item raw uses for its correction, which a corrected_in_note quote must carry, followed by
# the note's value
NR_CORR_WORD_RE = re.compile(r"(?i)\bcorrect(?:ed)?(?:\s+value)?\s*(?:to\b|:)")

# ------------------------------------------------------------------ round 7 (N1 final fixes, round 3, 2026-10-09)
# The strict check of round 6 (r6chk, scratch) raised four findings; section 12 gives each with its disposition. As in
# round 6, the constants below are the round's frozen declarations, asserted at every run; a deliberate change to any
# of them is a visible change to this script.
# finding 2: the fields that decide a row's status, frozen like the kind assignment: one line per row, in file order,
# 'span#seq<TAB>maps_to<TAB>status<TAB>ledger_row<TAB>status_basis' (the basis as sorted JSON); for a not-found row
# also '<TAB>locator<TAB>source_value' (finding 3: what a not-found row says was searched). Any other hash fails
# validation ('status-hash'). The row checks bind a status to its figure only as far as section 12 says; this freeze
# makes every change of a status, a mapping, a ledger row or a status basis a change to this script as well.
NR_STATUS_SHA256 = "35932d8ea485e17fd0c85b6e3f130c09bf917b5b88dfe29b57e450702eacf30e"
# finding 4: the free text and the change history, frozen the same way (nr_text_freeze): the file's item, title,
# how_built, schema and provenance; every span (header, summary, span notes, annotations); and per row its comment,
# cause, not_figure_reason, validation_note and round5/round6/round7 change records. Any other hash fails validation
# ('text-hash'). The text is frozen, not judged.
NR_TEXT_SHA256 = "250ae5d72cdb60a9e2711c069c301e3b2740fc4a9f1f9cfa92f0d2839dd67f68"
NR_TEXT_ROW_FIELDS = ("comment", "cause", "not_figure_reason", "validation_note", "round5", "round6", "round7")
# finding 4 (the quotation rule): every string in the rows file is scanned at each run for a quoted span of fifteen
# words or more ('…', "…", “…”, ‘…’) within 250 characters before or 120 after a name of an external source
# (NR_QUOTE_EXT_RE, the round-6 checker's list). Each hit must be declared here, by the first 16 hex of the span's
# sha256, with Code's reading of it; an undeclared hit fails validation ('quote-scan').
NR_QUOTE_EXT_RE = re.compile(r"arXiv|et al\.|Macar|Sofroniew|Tagliabue|Chua|Anthropic|WebFetch|the source's|source v\d|"
                             r"paper|preprint|PREPRINT|Appendix|github|journal|§\d", re.I)
NR_QUOTE_PAIRS = (('"', '"'), ("“", "”"), ("‘", "’"))
NR_QUOTE_REVIEWED = {
    "20c8d57b6b58ec20": "S1#25's source value quotes N2 @09c3a8c:393, an item raw's own sentence; 'the source's' "
                           "there names the external source, and the words are N2's",
    "80b9105080fa2c4e": "S7#16's source value quotes N14 @09c3a8c:459, a table row of the item raw between quotation "
                           "marks; 'preprint §5.6' is a citation inside the row, and nothing in it quotes the preprint",
}


def nr_freeze_line(r):
    s = (f"{r.get('span')}#{r.get('seq')}\t{r.get('maps_to')}\t{r.get('status')}\t{r.get('ledger_row')}\t"
         + json.dumps(r.get("status_basis"), sort_keys=True, ensure_ascii=False))
    if r.get("status") == "not found":
        s += f"\t{r.get('locator')}\t{r.get('source_value')}"
    return s


def nr_status_freeze(rows):
    return sha256("\n".join(nr_freeze_line(r) for r in rows).encode("utf-8"))


def nr_text_freeze(D):
    out = [json.dumps({k: D.get(k) for k in ("item", "title", "how_built", "schema", "provenance")}, sort_keys=True,
                      ensure_ascii=False)]
    out += [json.dumps(s, sort_keys=True, ensure_ascii=False) for s in D["spans"]]
    out += [f"{r.get('span')}#{r.get('seq')}\t" + json.dumps({k: r.get(k) for k in NR_TEXT_ROW_FIELDS}, sort_keys=True,
                                                             ensure_ascii=False) for r in D["rows"]]
    return sha256("\n".join(out).encode("utf-8"))


def nr_quoted_spans(text):
    out = []
    for o, c in NR_QUOTE_PAIRS:
        rx = re.compile(re.escape(o) + r"([^" + re.escape(o + c) + r"\n]{20,600}?)" + re.escape(c))
        out += [(m.start(), m.group(1)) for m in rx.finditer(text)]
    # single quotes: an opening ' after the start, a space, '(' or '['; a closing ' before a space, punctuation or the end
    out += [(m.start(), m.group(1)) for m in
            re.finditer(r"(?:(?<=^)|(?<=[\s(\[]))'([^'\n]{20,600}?[^\s])'(?=[\s.,;:)\]|]|$)", text, re.M)]
    return out


def nr_quote_scan(D):
    """Every quoted span of fifteen words or more near the name of an external source, in every string of the rows
    file (change records included), with its declaration in NR_QUOTE_REVIEWED (None if undeclared)."""
    strings = []

    def walk(x, where):
        if isinstance(x, str):
            strings.append((where, x))
        elif isinstance(x, dict):
            for k, v in x.items():
                if not str(k).startswith("_"):
                    walk(v, f"{where}.{k}")
        elif isinstance(x, list):
            for i, v in enumerate(x):
                walk(v, f"{where}[{i}]")
    walk(D, "$")
    hits = []
    for where, t in strings:
        for pos, sp in nr_quoted_spans(t):
            nw = len(sp.split())
            if nw < 15 or not NR_QUOTE_EXT_RE.search(t[max(0, pos - 250):pos + len(sp) + 120]):
                continue
            h = sha256(sp.encode("utf-8"))[:16]
            hits.append(dict(where=where, words=nw, sha=h, reviewed=NR_QUOTE_REVIEWED.get(h)))
    return hits


def nr_is_item_raw(path):
    """An item raw (or a later audit raw such as N19's), never the N1 ledger itself."""
    return bool(NR_ITEMRAW_RE.match(path or "")) and "N1-claims-ledger" not in path


def nr_clause_lines(rows):
    return "\n".join(f"{r['span']}#{r['seq']}\t{r.get('clause')}" for r in rows)


def nr_kind_lines(rows):
    return "\n".join(f"{r['span']}#{r['seq']}\t{r['note_file']}\t{r['note_line']}\t{nr_unit(r)}\t{r.get('kind')}"
                     for r in rows)


def nr_table_cells(line):
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def nr_status_cell(path, rev, n):
    """The cell under a 'status' column header for a markdown table row (path@rev:n), or None."""
    ls = nr_lines_at(rev, path)
    if ls is None or not 1 <= n <= len(ls):
        return None
    line = ls[n - 1]
    if not line.startswith("|") and " | " in line and not line.startswith("figure | "):
        # N11's text table: 'figure | named in (locator) | value here | status' rows under a 'figure | ' header
        i = n - 1
        while i >= 1 and " | " in ls[i - 1] and not ls[i - 1].startswith("figure | "):
            i -= 1
        if i < 1 or not ls[i - 1].startswith("figure | "):
            return None
        hdr, cells = [c.strip() for c in ls[i - 1].split(" | ")], [c.strip() for c in line.split(" | ")]
        idx = [k for k, x in enumerate(hdr) if x.lower().startswith("status")]
        return cells[idx[0]] if len(hdr) == len(cells) and len(idx) == 1 else None
    if not line.startswith("|") or NR_SEP_RE.match(line):
        return None
    i = n - 1
    while i >= 1 and ls[i - 1].startswith("|") and not NR_SEP_RE.match(ls[i - 1]):
        i -= 1
    if i < 2 or not NR_SEP_RE.match(ls[i - 1]):
        return None
    hdr, cells = nr_table_cells(ls[i - 2]), nr_table_cells(line)
    idx = [k for k, x in enumerate(hdr) if x.lower().startswith("status")]
    if len(hdr) != len(cells) or len(idx) != 1:
        return None
    return cells[idx[0]]


_NRFIG: dict = {}


def nr_fig_index(raws):
    """(item raw md path, line at the audit pin) -> the item raw's JSON figure row (status, locator)."""
    if not _NRFIG:
        for item in raws.js:
            for i, f in enumerate(raws.figures(item)):
                try:
                    rr = raws.resolve((item, "id", f["id"]) if f.get("id") and item == "N3" else F(item, f.get("figure")))
                except SystemExit:
                    continue
                _NRFIG[(RAWS[item][0], rr["md_line"])] = rr
    return _NRFIG


def nr_terms(s):
    return list(dict.fromkeys(re.findall(r"reproduced|log-only|not found|discrepant|computed-new|not run", s or "")))


def nr_line_status(path, rev, n, figidx):
    """The status a cited item-raw line gives: its JSON figure row's (the line, matched by exact text at the audit
    pin, is a figure row of the item's JSON), else the cell under its table's 'status' column; None if neither, or if
    the cell carries no term of the vocabulary. A cell with several terms gives all of them ('mixed')."""
    t = nr_line(rev, path, n)
    if t is None:
        return None
    if path in NR_RAW_MD:
        al = nr_lines_at(AUDIT, path) or []
        for i in [k + 1 for k, x in enumerate(al) if x == t]:
            if (path, i) in figidx:
                f = figidx[(path, i)]
                b = base_status(f["status"])
                return dict(terms=nr_terms(f["status"]) if b == "mixed" else [b], raw=f["status"],
                            how=f"JSON figure row {f['locator']}")
    c = nr_status_cell(path, rev, n)
    if c is not None:
        b = base_status(c)
        if b in STATUS_VOCAB or b == "not run":
            return dict(terms=[b], raw=c, how=f"status cell of {path}@{rev}:{n}")
        if b == "mixed":
            return dict(terms=nr_terms(c), raw=c, how=f"status cell of {path}@{rev}:{n} (several terms)")
    # round 6 (n1chk2 finding 1b): N3c (and N16) write a figure's status inline as '[status: ...]'; every term of
    # every tag on the line counts ('mixed' when there are several)
    tags = NR_TAG_RE.findall(t)
    ts = list(dict.fromkeys(x for tg in tags for x in nr_terms(tg)))
    if ts:
        return dict(terms=ts, raw="; ".join(x.strip() for x in tags),
                    how=f"status tag on {path}@{rev}:{n}" + (" (several terms)" if len(ts) > 1 else ""))
    return None


# round 7: the levels at which a status line counts as carrying the row's value (level B only where the locator check
# accepts it: integer and word units). Level A alone was tried: it broke five rows and closed few prefix upgrades
# (section 12, finding 2).
NR_CARRY_LEVELS = ("A", "B")


def nr_line_carries(r, path, rev, n):
    """Round 7 (finding 2): does this one cited line carry a value the row states (nr_check_locator on that line
    alone: level A, or level B where B is accepted)?"""
    v = nr_check_locator(r, only=(path, rev, n))
    return v["result"] == "pass" and v.get("level") in NR_CARRY_LEVELS, v.get("level")


def nr_status_lines(r, figidx):
    """Round 7: every cited item-raw line that gives a status (nr_line_status), in the row's order, with whether it
    carries a value the row states. A status line that carries none of the row's values is another figure's row (or
    section) and decides nothing."""
    out = []
    for l in nr_parse_locs(r.get("locator")):
        if not l["lines"] or not nr_is_item_raw(l["path"]):
            continue
        for n in l["lines"]:
            s = nr_line_status(l["path"], l["rev"], n, figidx)
            if s:
                c, lev = nr_line_carries(r, l["path"], l["rev"], n)
                out.append(dict(where=f"{l['path']}@{l['rev']}:{n}", terms=s["terms"], raw=s["raw"], how=s["how"],
                                carries=c, level=lev))
    return out


def nr_check_status(r, figidx):
    """The status of an item-raw, audit-raw-new or record row against what the item raw gives (finding 2 of round 5;
    amended in rounds 6 and 7). Round 7 (r6chk findings 1 and 2) binds the status to the row's figure:
      - only a cited item-raw line that gives a status AND carries a value the row states (nr_status_lines) decides;
        a status line carrying none of the row's values is another figure's and decides nothing;
      - a source that gives several terms (a '[status: …]' tag such as N3c :151, a status cell, a JSON 'mixed'
        status, or a record row's lines together) decides nothing by itself: the row needs a status_basis whose quote
        is the single-term clause that applies;
      - status_basis ({locator, quote}): one line of an item raw the row cites (round 7: never a record line), the
        quote on it; the line's single term decides, or, where the line gives several terms or none, the quote's
        single term (one of the line's terms where it gives several). With a basis, every cited status line that
        carries the row's value must also give the basis's term.
    Without a basis: item-raw / audit-raw-new rows take the first such line's term (an audit-raw-new row with none is
    computed-new by its mapping; an item-raw row with none fails); record rows take their lines' one term, or
    log-only where none carries the row's value."""
    mp, st = r.get("maps_to"), r.get("status")
    if mp not in ("item-raw", "audit-raw-new", "record"):
        return dict(result="n/a (maps_to " + str(mp) + ")")
    locs = [l for l in nr_parse_locs(r.get("locator")) if l["lines"]]
    sl = nr_status_lines(r, figidx)
    own = [x for x in sl if x["carries"]]
    skipped = len(sl) - len(own)
    sb = r.get("status_basis")
    if sb:
        bl = nr_parse_locs(sb.get("locator"))
        if len(bl) != 1 or len(bl[0]["lines"]) != 1:
            return dict(result="FAIL: status_basis needs exactly one line locator")
        p, rv, n = bl[0]["path"], bl[0]["rev"], bl[0]["lines"][0]
        # round 6 (n1chk2 finding 8): the basis is a line of a file the row cites
        if p not in {l["path"] for l in locs}:
            return dict(result=f"FAIL: status_basis names {p}, a file the row's locator does not cite")
        # round 7 (r6chk finding 2, N07): statuses are the item raws'; a record line gives none
        if not nr_is_item_raw(p):
            return dict(result=f"FAIL: status_basis names {p}, which is not an item raw (a record line gives no status)")
        line = nr_line(rv, p, n)
        if line is None or not sb.get("quote") or sb["quote"] not in line:
            return dict(result=f"FAIL: status_basis quote not on {p}@{rv}:{n}")
        ls_ = nr_line_status(p, rv, n, figidx)
        qt = nr_terms(sb["quote"])
        if ls_ and len(ls_["terms"]) == 1:
            bt, how = ls_["terms"][0], ls_["how"]
            if qt and qt != [bt]:
                return dict(result=f"FAIL: status_basis quote carries {'/'.join(qt)}; its line gives {bt} ({how})")
        else:
            if len(qt) != 1:
                return dict(result=f"FAIL: status_basis quote carries {len(qt)} status terms (needs one: the single-term "
                                   f"clause that applies)" + (f"; its line gives several ({'/'.join(ls_['terms'])})"
                                                              if ls_ else ""))
            if ls_ and qt[0] not in ls_["terms"]:
                return dict(result=f"FAIL: status_basis quote's {qt[0]} is not one of its line's terms "
                                   f"({'/'.join(ls_['terms'])})")
            bt = qt[0]
            how = f"status_basis quote on {p}@{rv}:{n}" + (f" (its line gives several terms, {'/'.join(ls_['terms'])}; "
                                                           f"the quoted clause decides)" if ls_ else "")
        if st != bt:
            return dict(result=f"FAIL: status '{st}' vs the status_basis's {bt} ({how})", expected=[bt])
        conflict = [x for x in own if bt not in x["terms"]]
        if conflict:
            return dict(result=f"FAIL: status_basis gives {bt}, but a cited status line that carries the row's value "
                               f"gives {'/'.join(conflict[0]['terms'])} ({conflict[0]['where']})", expected=[bt])
        # a status line that carries none of the row's values decided nothing, unless it is the basis's own line
        sk = sum(1 for x in sl if not x["carries"] and x["where"] != f"{p}@{rv}:{n}")
        return dict(result="pass", expected=[bt], how="status_basis -> " + how, status_lines=len(sl), skipped=sk)
    if mp == "record":
        terms = list(dict.fromkeys(t for x in own for t in x["terms"]))
        if not terms:
            exp = dict(terms=["log-only"], how="record lines only: log-only" + (
                f" ({skipped} cited item-raw status line(s) carry none of the row's values and decide nothing)"
                if skipped else ""))
        elif len(terms) > 1:
            return dict(result=f"FAIL: the cited item-raw lines that carry the row's value give several terms "
                               f"({'/'.join(terms)}); several terms decide nothing: a status_basis quoting the "
                               f"single-term clause is needed")
        else:
            exp = dict(terms=terms, how=own[0]["how"] + (f" (and {len(own) - 1} more cited item-raw line(s) giving the "
                                                         f"same term)" if len(own) > 1 else ""))
    else:
        if own:
            x = own[0]
            if len(x["terms"]) > 1:
                return dict(result=f"FAIL: the deciding line {x['where']} gives several terms ({'/'.join(x['terms'])}); "
                                   f"several terms decide nothing: a status_basis quoting the single-term clause is "
                                   f"needed")
            exp = dict(terms=x["terms"], how=x["how"])
        elif mp == "audit-raw-new":
            exp = dict(terms=["computed-new"], how="audit-raw-new: computed new by the audit raw it cites")
        else:
            return dict(result="FAIL: no cited item-raw line that carries the row's value gives a status, and the row "
                               "has no status_basis" + (f" ({skipped} status line(s) carry none of the row's values)"
                                                        if skipped else ""))
    if st not in exp["terms"]:
        return dict(result=f"FAIL: status '{st}' vs {'/'.join(exp['terms'])} ({exp['how']})", expected=exp["terms"])
    return dict(result="pass", expected=exp["terms"], how=exp["how"], status_lines=len(sl), skipped=skipped)


def nr_unit_class(u):
    """'word' (number words, ordinals, '½'), 'fraction' (k/n), 'decimal' (a decimal point), else 'integer'."""
    s = u.strip()
    if s.lower() in NR_WORDS or s == "½" or not re.search(r"\d", s):
        return "word"
    if FRAC_RE.search(s):
        return "fraction"
    if re.search(r"\d\.\d|(?<!\d)\.\d", s):
        return "decimal"
    return "integer"


def nr_tie(v, u):
    """A source value v ties to the note's value u: equal, or v, stated to more places, rounds (half-up) to u at u's
    places (round 5: 0.6115 -> 0.6, 1.525 -> 1.5, 1.995 -> 2 for the note's 'about 2')."""
    from decimal import Decimal, ROUND_HALF_UP
    if v[0] == u[0]:
        return "equal"
    if v[1] > u[1] and v[0].quantize(Decimal(1).scaleb(-u[1]), rounding=ROUND_HALF_UP) == u[0]:
        return "rounds"
    return None


def nr_line_numbers(r):
    """Integers that are line numbers in the row: every locator spec in its locator and source_value, and every
    ':<digits>' in its source_value (a file:line reference, 'e2a_sessions.py:355', 'LOCK-g:167-171')."""
    out = set()
    for f in ("locator", "source_value"):
        for l in nr_parse_locs(r.get(f)):
            out.update(l["lines"])
    for m in re.finditer(r":(\d+(?:-\d+)?(?:,\s?:?\d+(?:-\d+)?)*)", str(r.get("source_value") or "")):
        try:
            out.update(parse_lines(m.group(1).replace(":", "")))
        except Exception:
            pass
    return out


def nr_check_locator(r, only=None):
    """Does a cited source line carry a value the row's source_value states? Every line of every locator that names
    lines is read, in the order the row gives them ('primary' = the first such locator). Two levels:
      A  a cited line carries a value tied to the note's own number: an ISO date the source_value states; a
         source_value numeral equal to the note unit's value, or rounding to it (half-up at the unit's places; a
         percent unit is also compared as a proportion); for a fraction unit k/n, the same fraction in the
         source_value and on the line; or, where the source_value states no distinctive numeral (a decimal, or an
         integer of 10 or more) and no date, the note unit's value or its number word itself;
      B  no A, but a cited line carries one of the source_value's distinctive numerals (another value the row states,
         such as a denominator or an n). Round 5 (finding 2): B never matches on a year (1900-2099), on a line
         number the row cites, or on 0 or 1; and B is not accepted at all for a decimal or a fraction unit, whose
         value the source_value must state (A).
    Neither: FAIL. A and B are consistency checks on the mapping; neither re-derives a figure.
    Round 7: with 'only' ((path, rev, line)), the same check reads that one line alone (everything else, the values
    sought and the line numbers excluded from B, still comes from the whole row); the status check uses it to ask
    whether a status line carries a value the row states."""
    from decimal import Decimal
    locs = nr_parse_locs(r.get("locator"))
    lls = [l for l in locs if l["lines"]]
    if only is not None:
        lls = [dict(path=only[0], rev=only[1], lines=[only[2]], raw=f"{only[0]}@{only[1]}:{only[2]}")]
    if not lls:
        return dict(result="FAIL: no line locator", locators=[l["raw"] for l in locs])
    unit = nr_unit(r)
    ucls = nr_unit_class(unit)
    sv = str(r.get("source_value") or "")
    dates, vals = nr_values(sv)
    uv, words = nr_unit_values(unit)
    uv = [v for v in uv if v]
    if unit.strip().endswith("%"):
        uv += [(v[0] / Decimal(100), v[1] + 2, v[2]) for v in uv]
    fr_u = [(int(m.group(1)), int(m.group(2))) for m in FRAC_RE.finditer(unit)]
    fr_sv = nr_fracs(nr_strip_locs(sv))
    lnum = nr_line_numbers(r)
    # a leading-zero digit run ('0551224') is an identifier (a commit-hash fragment), never a value
    vals = [v for v in vals if not (v[1] == 0 and len(v[2]) > 1 and v[2][0] == "0")]
    distinct = [v for v in vals if (v[1] > 0 or v[0] >= 10) and v[0] not in (0, 1)
                and not (v[1] == 0 and (1900 <= v[0] <= 2099 or int(v[0]) in lnum))]
    if ucls == "fraction":
        tied = []
        frac_need = [f for f in fr_u if f in fr_sv]
    else:
        tied = [v for v in vals if any(nr_tie(v, u) for u in uv)]
        frac_need = []
    # a fraction k/n the source_value states is also an exact value (15/85 = 0.17647 -> 0.176, where the printed
    # 0.1765 would round to 0.177); it ties at level A when the same k/n is on a cited line
    frac_tied = [f for f in sorted(fr_sv) if f[1] and ucls == "decimal" and any(nr_tie(nr_fracval(f), u) for u in uv)]
    fallback = not distinct and not dates and ucls != "fraction"
    if fallback:
        # the unit's own value, except a bare 0 or 1 (round 5: a lone '1' or '0' on a line ties to nothing; the
        # number word itself still counts)
        tied = tied + [u for u in uv if u[0] not in (0, 1)]
    else:
        words = []
    if not (tied or dates or words or distinct or frac_need or frac_tied):
        return dict(result="FAIL: no value to look for", locators=[l["raw"] for l in lls], unit_class=ucls)
    errors, a_hit, b_hit = [], None, None
    for k, l in enumerate(lls):
        lines = nr_lines_at(l["rev"], l["path"])
        if lines is None:
            errors.append(f"{l['path']}@{l['rev']}: not readable")
            continue
        for n in l["lines"]:
            if not 1 <= n <= len(lines):
                errors.append(f"{l['path']}@{l['rev']}:{n} out of range")
                continue
            s_ = lines[n - 1]
            lt = nr_tokens(s_)
            where = dict(where="primary" if k == 0 else "secondary", locator=f"{l['path']}@{l['rev']}:{n}")
            if a_hit is None:
                d = next((d for d in dates if d in s_), None)
                if d:
                    a_hit = dict(where, value=d, how="date")
                elif frac_need:
                    fl = nr_fracs(s_)
                    if all(f in fl for f in frac_need) and len(frac_need) == len(fr_u):
                        a_hit = dict(where, value=", ".join(f"{a}/{b}" for a, b in frac_need), how="fraction")
                else:
                    for v in tied:
                        how = next((nr_same(v, w) for w in lt if nr_same(v, w)), None)
                        if how:
                            a_hit = dict(where, value=v[2], how=how)
                            break
                    if a_hit is None and frac_tied:
                        fl = nr_fracs(s_)
                        f = next((f for f in frac_tied if f in fl), None)
                        if f:
                            a_hit = dict(where, value=f"{f[0]}/{f[1]}", how="fraction value")
                    if a_hit is None:
                        ww = next((x for x in words if (x in s_ if x == "½" else
                                                        re.search(r"\b" + re.escape(x) + r"\b", s_, flags=re.I))), None)
                        if ww:
                            a_hit = dict(where, value=ww, how="word")
            if b_hit is None:
                for v in distinct:
                    how = next((nr_same(v, w) for w in lt if nr_same(v, w)), None)
                    if how:
                        b_hit = dict(where, value=v[2], how=how)
                        break
    if a_hit:
        return dict(result="pass", level="A", errors=errors, unit_class=ucls, **a_hit)
    if b_hit and ucls in ("decimal", "fraction"):
        return dict(result=f"FAIL: a {ucls} unit needs level A (the source_value states no value tied to the note's "
                           f"number on a cited line); level B would match on {b_hit['value']}", unit_class=ucls,
                    errors=errors)
    if b_hit:
        return dict(result="pass", level="B", errors=errors, unit_class=ucls, **b_hit)
    # round 6 (finding 4): the message names what was looked for and where, so an exemption that must equal it is
    # bound to the row's source_value and locator
    sought = list(dict.fromkeys([v[2] for v in tied + distinct] + dates + words
                                + [f"{a}/{b}" for a, b in frac_need + frac_tied]))
    read = [f"{l['path']}@{l['rev']}:{','.join(str(n) for n in l['lines'])}" for l in lls]
    return dict(result=f"FAIL: no cited line carries a stated value (sought: {', '.join(sought) or 'none'}; read: "
                       f"{'; '.join(read)})", values=sought, locators=[l["raw"] for l in lls], errors=errors,
                unit_class=ucls)


NR_OF_RE = re.compile(r"(?<![\d.])(\d+) of (\d+)(?!\.?\d)")


def nr_fracs(s):
    """The fractions a text states, as (k, n): 'k/n' and 'k of n' (round 5: '14 of 32' is the note's '14/32')."""
    s = str(s or "")
    return {(int(m.group(1)), int(m.group(2))) for rx in (FRAC_RE, NR_OF_RE) for m in rx.finditer(s)}


def nr_fracval(f):
    from decimal import Decimal
    return ((Decimal(f[0]) / Decimal(f[1])).quantize(Decimal(1).scaleb(-12)), 12, f"{f[0]}/{f[1]}")


def nr_strip_locs(s):
    s = NR_LOC_RE.sub(" ", str(s or ""))
    return re.sub(r":\d+(?:-\d+)?(?:,\s?:?\d+(?:-\d+)?)*", " ", s)


def nr_cited_lines(r):
    """The lines a row cites: its locator's, plus the line references inside its source_value (a bare ':n' there is
    read against the locator's first file)."""
    lls = [l for l in nr_parse_locs(r.get("locator")) if l["lines"]]
    out = list(lls)
    if lls:
        for l in nr_parse_locs(f"{lls[0]['path']}@{lls[0]['rev']} " + str(r.get("source_value") or "")):
            if l["lines"]:
                out.append(l)
    return out


def nr_check_source_values(r):
    """Finding 2 (round 5): every value the source_value states to two or more places, and every fraction it states
    ('k/n' or 'k of n'; not '1/2'), is on a cited line (equal, or one rounding to the other at two or more places).
    A source_value that misstates any of its values, not only the one tied to the note's number, fails. Round 6
    (n1chk2 finding 8): one-place decimals too (equal on the line)."""
    sv = str(r.get("source_value") or "")
    _, vals = nr_values(sv)
    decs = [v for v in vals if v[1] >= 1]
    fr = {f for f in nr_fracs(nr_strip_locs(sv)) if f != (1, 2)}
    toks, lfr, unread = [], set(), []
    for l in nr_cited_lines(r):
        for n in l["lines"]:
            t = nr_line(l["rev"], l["path"], n)
            if t is None:
                unread.append(f"{l['path']}@{l['rev']}:{n}")
                continue
            toks += nr_tokens(t)
            lfr |= nr_fracs(t)
    md = [v[2] for v in decs if not any(nr_same(v, w) for w in toks)]
    mf = [f"{a}/{b}" for a, b in sorted(fr) if (a, b) not in lfr]
    if md or mf:
        return dict(result="FAIL: stated value(s) on no cited line: " + ", ".join(md + mf), unreadable=unread)
    return dict(result="pass", n_decimals=len(decs), n_fractions=len(fr))


def nr_check_double_rounding(r):
    """Finding 4: a note figure that rounds from a printed value which is itself a rounding of a more precise value
    the row states, while the more precise value rounds to something else at the note's places (0.594963 -> 0.5950
    -> .60, directly .59; 0.8747 -> 0.875 -> 0.88, directly 0.87). The rule (one for every such row): the item raw's
    status is carried, and the row must record a precision correction ('correction', kind 'precision')."""
    from decimal import Decimal
    unit = nr_unit(r)
    if nr_unit_class(unit) != "decimal":
        return dict(result="n/a")
    _, vals = nr_values(r.get("source_value"))
    uv, _ = nr_unit_values(unit)
    uv = [v for v in uv if v]
    if unit.strip().endswith("%"):
        uv += [(v[0] / Decimal(100), v[1] + 2, v[2]) for v in uv]
    hits = []
    for v in vals:
        for u in uv:
            if not nr_tie(v, u):
                continue
            for a in vals:
                if a[1] > v[1] and nr_tie(a, v) == "rounds" and not nr_tie(a, u):
                    hits.append(f"{a[2]} -> {v[2]} -> {u[2]}")
    hits = list(dict.fromkeys(hits))
    if not hits:
        return dict(result="pass (no double rounding)")
    c = r.get("correction") or {}
    if c.get("kind") == "precision":
        return dict(result="pass (double rounding; precision correction recorded)", chains=hits)
    return dict(result="FAIL: double rounding (" + "; ".join(hits) + ") without a precision correction", chains=hits)


def nr_ledger_values(lrow):
    """The texts a ledger row carries for a figure: its block span, and its primary and related item-raw rows'
    figure labels and printed values."""
    out = [lrow.get("figure") or ""]
    for rr in lrow.get("refs", []) + lrow.get("related", []):
        out += [str(rr.get("figure") or ""), str(rr.get("printed") or "")]
    return [x for x in out if x]


def nr_check_ledger_span(r, ledger):
    """Finding 2: a ledger id the row names must carry the note's number. Pass if any named ledger row's span or
    item-raw figure label or printed value contains the unit's text, a numeral tied to its value (equal, or one
    rounding to the other at two or more places; a fraction as the same k/n), or its number word."""
    from decimal import Decimal
    ids, _ = nr_row_ledger_ids(r)
    if not ids:
        return dict(result="n/a")
    unit = nr_unit(r)
    ucls = nr_unit_class(unit)
    uv, words = nr_unit_values(unit)
    uv = [v for v in uv if v]
    if unit.strip().endswith("%"):
        uv += [(v[0] / Decimal(100), v[1] + 2, v[2]) for v in uv]
    fr_u = {(int(m.group(1)), int(m.group(2))) for m in FRAC_RE.finditer(unit)}
    lit = unit.strip().strip("'").lstrip("+−-")
    for i in ids:
        if i not in ledger:
            continue
        for t in nr_ledger_values(ledger[i]):
            if ucls == "fraction":
                if fr_u and fr_u <= nr_fracs(t):
                    return dict(result="pass", id=i, how="fraction")
                continue
            if ucls == "word":
                if any((x in t if x == "½" else re.search(r"\b" + re.escape(x) + r"\b", t, flags=re.I))
                       for x in words + ([unit.strip()] if unit.strip() == "½" else [])):
                    return dict(result="pass", id=i, how="word")
            if ucls in ("decimal", "integer") and re.search(r"(?<![\d.])" + re.escape(lit) + r"(?![\d])", t):
                return dict(result="pass", id=i, how="text")
            toks = nr_tokens(nr_strip_locs(t))
            if ucls == "decimal":
                toks += [nr_fracval(f) for f in sorted(nr_fracs(nr_strip_locs(t))) if f[1]]
            for w in toks:
                for u in uv:
                    if nr_same(w, u) or nr_tie(w, u):
                        if ucls == "word" and u[0] in (0, 1) and w[1] == 0:
                            continue
                        return dict(result="pass", id=i, how="value")
    return dict(result=f"FAIL: no ledger row named ({', '.join(ids)}) carries '{unit}' or its value", ids=ids)


def nr_check_correction(r):
    c = r.get("correction")
    if c is None:
        return dict(result="n/a")
    if not isinstance(c, dict) or c.get("kind") not in NR_CORR_KINDS or not c.get("text") or not c.get("whose"):
        return dict(result="FAIL: correction needs kind (" + "/".join(NR_CORR_KINDS) + "), text and whose")
    bad = [l["raw"] for l in nr_parse_locs(c.get("basis")) for n in l["lines"]
           if nr_line(l["rev"], l["path"], n) is None]
    if bad:
        return dict(result=f"FAIL: correction basis not readable: {bad}")
    return dict(result="pass")


def nr_fig_row(path, rev, n, figidx):
    """The item raw's JSON figure row for a cited line (matched by exact line text at the audit pin), or None."""
    t = nr_line(rev, path, n)
    if t is None or path not in NR_RAW_MD:
        return None
    al = nr_lines_at(AUDIT, path) or []
    for i in [k + 1 for k, x in enumerate(al) if x == t]:
        if (path, i) in figidx:
            return figidx[(path, i)]
    return None


_NRFULL: dict = {}


def nr_full(rev):
    """A revision's full sha, or None where it names no commit (never raises)."""
    if rev not in _NRFULL:
        r = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--verify", "--quiet", rev + "^{commit}"],
                           capture_output=True, text=True)
        _NRFULL[rev] = r.stdout.strip() if r.returncode == 0 else None
    return _NRFULL[rev]


def nr_check_corrected(r, loc_res, figidx):
    """Finding 6 (round 5): a row the note already corrects carries its item raw's status (discrepant), is marked
    'corrected_in_note' ({locator, quote}: the item raw's correction, quoted from the line), and counts as passing
    when the note's figure ties to the source value at level A (the note now carries the reproduced value).
    Round 6 (n1chk2 finding 2): the quote must carry the item raw's correction wording ('correct to', 'corrected to',
    'Corrected value:') followed by the note's value; the line must be the item raw's figure row, and the note's value
    must differ from the discrepant figure that row quotes; and the corrected rows must be exactly NR_DISC's branch C
    (asserted in final_note_rows)."""
    ci = r.get("corrected_in_note")
    if ci is None:
        return dict(result="n/a")
    if r.get("status") != "discrepant":
        return dict(result="FAIL: corrected_in_note on a row that is not discrepant")
    if not isinstance(ci, dict):
        return dict(result="FAIL: corrected_in_note must be {locator, quote}")
    bl = nr_parse_locs(ci.get("locator"))
    if len(bl) != 1 or len(bl[0]["lines"]) != 1:
        return dict(result="FAIL: corrected_in_note needs exactly one line locator")
    p_, rv_, n_ = bl[0]["path"], bl[0]["rev"], bl[0]["lines"][0]
    cited = {(l["path"], nr_full(l["rev"]), n) for l in nr_parse_locs(r.get("locator")) for n in l["lines"]}
    if nr_full(rv_) is None or (p_, nr_full(rv_), n_) not in cited:
        return dict(result="FAIL: corrected_in_note's line is not one the row cites")
    line = nr_line(rv_, p_, n_)
    q = ci.get("quote")
    if line is None or not q or q not in line:
        return dict(result="FAIL: corrected_in_note quote not on its line")
    uv = [v for v in nr_unit_values(nr_unit(r))[0] if v]
    m = NR_CORR_WORD_RE.search(q)
    if not m:
        return dict(result="FAIL: corrected_in_note's quote carries no correction wording ('correct to', 'corrected "
                           "to', 'Corrected value:')")
    if not any(nr_tie(x, u) for x in nr_tokens(q[m.end():]) for u in uv):
        return dict(result="FAIL: corrected_in_note's quote does not state the note's value after its correction "
                           "wording (the correction it applies)")
    fr = nr_fig_row(p_, rv_, n_, figidx)
    if fr is None:
        return dict(result="FAIL: corrected_in_note's line is not an item-raw figure row, so the discrepant figure it "
                           "corrects cannot be read")
    old = nr_tokens(nr_strip_locs(str(fr.get("figure") or "")))
    if not old:
        return dict(result=f"FAIL: the item raw's figure row ({fr['locator']}) quotes no figure to compare")
    if any(o[0] == u[0] or nr_tie(o, u) or nr_tie(u, o) for o in old for u in uv):
        return dict(result=f"FAIL: the note still carries the discrepant figure the item raw quotes "
                           f"({fr.get('figure')!r}, {fr['locator']})")
    if loc_res.get("level") != "A":
        return dict(result="FAIL: corrected_in_note but the note's figure does not tie to the source value (level A)")
    return dict(result="pass", corrects=fr.get("figure"), figure_row=fr["locator"])


def nr_check_maps_to(r):
    """Round 6 (n1chk2 finding 1a): a row's maps_to names what it cites. item-raw and audit-raw-new: at least one
    cited line of an item raw (or of a later audit raw such as N19's); record: at least one cited record line (a path
    outside the audit outputs, at or before the record pin, readable there); ledger-row: a ledger id (the ledger
    check); none: status not found (the schema check)."""
    mp = r.get("maps_to")
    lls = [l for l in nr_parse_locs(r.get("locator")) if l["lines"]]
    if mp in ("item-raw", "audit-raw-new"):
        if not any(nr_is_item_raw(l["path"]) for l in lls):
            return dict(result=f"FAIL: maps_to {mp} but the locator cites no item-raw line")
        return dict(result="pass")
    if mp == "record":
        if not any(not nr_is_audit_path(l["path"]) and nr_full(l["rev"]) and at_or_before_pin(l["rev"])
                   and nr_lines_at(l["rev"], l["path"]) is not None for l in lls):
            return dict(result="FAIL: maps_to record but the locator cites no record line (a path outside the audit "
                               "outputs, at or before the record pin)")
        return dict(result="pass")
    return dict(result="n/a")


def nr_check_pins(r):
    """Round 6 (n1chk2 finding 7): every revision a row cites (locator, source_value, status_basis, corrected_in_note,
    correction basis) is the pin of its path's class (NR_PIN_RULES): the record at bbc9ffe; item raws at 09c3a8c (N8
    and N11 also at 02b6a61); N19's raw at e0fd85c; the provisional ledger at 6485da2. Round 7 (r6chk finding 3): and
    the cited file exists at that revision, and every cited line is within it (every row, not-found rows included)."""
    fields = [("locator", r.get("locator")), ("source_value", r.get("source_value"))]
    for f in ("status_basis", "corrected_in_note"):
        if isinstance(r.get(f), dict):
            fields.append((f, r[f].get("locator")))
    if isinstance(r.get("correction"), dict):
        fields.append(("correction basis", r["correction"].get("basis")))
    bad, gone, n = [], [], 0
    for f, txt in fields:
        for l in nr_parse_locs(txt):
            n += 1
            name, _, revs = next(x for x in NR_PIN_RULES if x[1](l["path"]))
            if nr_full(l["rev"]) is None or nr_full(l["rev"]) not in {nr_full(x) for x in revs}:
                bad.append(f"{f} {l['path']}@{l['rev']} ({name}: {'/'.join(revs)})")
                continue
            # round 7 (r6chk finding 3): the cited path exists at its revision and every cited line is in range
            ls_ = nr_lines_at(l["rev"], l["path"])
            if ls_ is None:
                gone.append(f"{f} {l['path']}@{l['rev']} (no such file at that revision)")
                continue
            out = [x for x in l["lines"] if not 1 <= x <= len(ls_)]
            if out:
                gone.append(f"{f} {l['path']}@{l['rev']}:{','.join(str(x) for x in out)} (beyond its {len(ls_)} lines)")
    if bad or gone:
        return dict(result="FAIL: " + "; ".join((["revision off its pin: " + "; ".join(bad)] if bad else [])
                                                + (["cited file or line does not exist: " + "; ".join(gone)]
                                                   if gone else [])))
    return dict(result="pass" if n else "n/a", n_locators=n)


def nr_strip_all(text):
    """The source_value text as nr_values reads it (dates, locators, indexes, times, hashes, ids, labels removed)."""
    s = DATE_RE.sub(" ", str(text or ""))
    s = NR_LOC_RE.sub(" ", s)
    for rx in NR_STRIP_RES:
        s = rx.sub(" ", s)
    return s


def nr_check_unit_stated(r, texts):
    """Round 6 (n1chk2 finding 8): an integer unit's value is stated in the source_value -- a numeral tied to it
    (equal, or rounding half-up to it); a value whose integer part it is (a floor, '17×' for 17.500, which those rows'
    comments state); the unit's digits inside a label ('L60', '4bit', 'L49-L63'); or, where the note prints the unit
    as a percentage (a '%' after it or after its range), a proportion tied to it at the percentage scale. Level B
    alone no longer passes an integer unit whose number the source_value does not state."""
    from decimal import Decimal
    unit = nr_unit(r)
    if nr_unit_class(unit) != "integer":
        return dict(result="n/a")
    uv = [v for v in nr_unit_values(unit)[0] if v]
    if not uv:
        return dict(result="n/a")
    s = nr_strip_all(r.get("source_value"))
    vals = nr_tokens(s)
    for u in uv:
        if any(nr_tie(v, u) for v in vals):
            return dict(result="pass", how="tied")
        if any(v[1] > 0 and v[0] >= u[0] and int(v[0]) == int(u[0]) for v in vals):
            return dict(result="pass", how="floor")
        dg = re.sub(r"\D", "", u[2])
        if dg and re.search(r"(?<![\d.,])" + dg + r"(?![\d]|[.,]\d)", s):
            return dict(result="pass", how="label")
        ln = texts.get(r.get("note_file"), [""] * 0)
        line = ln[r["note_line"] - 1] if isinstance(r.get("note_line"), int) and 1 <= r["note_line"] <= len(ln) else ""
        pct = unit.strip().endswith("%") or re.search(re.escape(unit.strip()) + r"\s*(?:[–-]\s*\d+(?:\.\d+)?\s*)?%", line)
        if pct and any(v[1] >= 2 and v[0] < 1 and nr_tie((v[0] * Decimal(100), v[1] - 2, v[2]), u) for v in vals):
            return dict(result="pass", how="percentage")
    return dict(result=f"FAIL: the source_value does not state the note's {unit.strip()!r} (no tied value, floor, "
                       f"label or percentage)")


def nr_check_corr_declared(r):
    """Round 6 (n1chk2 finding 5): the row's correction is the one NR_CORRECTIONS declares for it (kind, and whose
    reading: N1's own, or an item raw's, whose basis then cites that raw); a correction the script does not declare,
    or a declared one that is missing, fails."""
    key = f"{r.get('span')}#{r.get('seq')}"
    c, d = r.get("correction"), NR_CORRECTIONS.get(key)
    if d is None and c is None:
        return dict(result="n/a")
    if d is None:
        return dict(result="FAIL: the row carries a correction the script does not declare (NR_CORRECTIONS)")
    if not isinstance(c, dict):
        return dict(result=f"FAIL: the script declares a {d[0]} correction ({d[1]}'s) and the row carries none")
    if c.get("kind") != d[0]:
        return dict(result=f"FAIL: correction kind {c.get('kind')!r}; the script declares {d[0]!r}")
    whose = str(c.get("whose") or "")
    if d[1] == "N1":
        if not whose.startswith("N1's"):
            return dict(result=f"FAIL: the correction is N1's own reading (NR_CORRECTIONS); 'whose' reads {whose[:60]!r}")
    else:
        if not whose.startswith(d[1] + " ("):
            return dict(result=f"FAIL: the correction is {d[1]}'s (NR_CORRECTIONS); 'whose' reads {whose[:60]!r}")
        rx = re.compile(r"^results/raw/2026-10-0[89]_note-" + re.escape(d[1]) + r"-")
        if not any(rx.match(l["path"]) for l in nr_parse_locs(c.get("basis"))):
            return dict(result=f"FAIL: the correction is {d[1]}'s but its basis cites no line of {d[1]}'s raw")
    # round 7 (r6chk finding 4b): the whole correction as declared (an N1-own correction's basis is bound here)
    fp = nr_corr_fp(c)
    if fp != d[2]:
        return dict(result=f"FAIL: the correction changed after it was declared (fingerprint {fp}, declared {d[2]})")
    return dict(result="pass")


def nr_corr_fp(c):
    return sha256(json.dumps(c, sort_keys=True, ensure_ascii=False).encode("utf-8"))[:16]


def nr_fingerprint(r):
    return sha256(json.dumps({k: r.get(k) for k in NR_FP_FIELDS}, sort_keys=True, ensure_ascii=False)
                  .encode("utf-8"))[:16]


def nr_validate_row(r, texts, ledger, figidx):
    """Every check on one row: [(check, message)] failures and the per-check results."""
    v, bad = {}, []
    key = f"{r.get('span')}#{r.get('seq')}"
    if r.get("note_file") not in texts:
        bad.append(("note-line", f"note_file {r.get('note_file')!r} is not one of the three routed files"))
    else:
        ls = texts[r["note_file"]]
        u = nr_unit(r)
        n = r.get("note_line")
        ok = isinstance(n, int) and 1 <= n <= len(ls) and u in ls[n - 1]
        v["note_line"] = "pass" if ok else f"FAIL: '{u}' not on {r['note_file']}:{n}"
        if not ok:
            bad.append(("note-line", v["note_line"]))
    v["pins"] = nr_check_pins(r)
    if v["pins"]["result"].startswith("FAIL"):
        bad.append(("pins", v["pins"]["result"]))
    kind, st, mp = r.get("kind"), r.get("status"), r.get("maps_to")
    if kind == "figure":
        if st not in NR_STATUSES or mp not in NR_MAPS:
            bad.append(("schema", f"status {st!r} / maps_to {mp!r}"))
        if mp == "none" and st != "not found":
            bad.append(("schema", f"maps_to none with status {st!r}"))
        v["maps_to"] = nr_check_maps_to(r)
        if v["maps_to"]["result"].startswith("FAIL"):
            bad.append(("maps-to", v["maps_to"]["result"]))
        if st in ("reproduced", "log-only", "computed-new", "discrepant"):
            v["locator"] = nr_check_locator(r)
            if v["locator"]["result"] != "pass":
                bad.append(("locator-value", v["locator"]["result"]))
            v["source_values"] = nr_check_source_values(r)
            if v["source_values"]["result"] != "pass":
                bad.append(("source-values", v["source_values"]["result"]))
            v["unit_stated"] = nr_check_unit_stated(r, texts)
            if v["unit_stated"]["result"].startswith("FAIL"):
                bad.append(("unit-stated", v["unit_stated"]["result"]))
        else:
            v["locator"] = dict(result=f"n/a ({st})")
        v["status"] = nr_check_status(r, figidx)
        if v["status"]["result"].startswith("FAIL"):
            bad.append(("status", v["status"]["result"]))
        v["ledger"] = nr_check_ledger(r, ledger)
        if v["ledger"]["result"].startswith("FAIL"):
            bad.append(("ledger-status" if "not in the ledger" not in v["ledger"]["result"] else "ledger-exists",
                        v["ledger"]["result"]))
        # round 7 (r6chk finding 2): the named ledger row is bound to the row's figure
        v["ledger_bind"] = nr_check_ledger_bind(r, ledger)
        if v["ledger_bind"]["result"].startswith("FAIL"):
            bad.append(("ledger-bind", v["ledger_bind"]["result"]))
        v["ledger_span"] = nr_check_ledger_span(r, ledger)
        if v["ledger_span"]["result"].startswith("FAIL"):
            bad.append(("ledger-span", v["ledger_span"]["result"]))
        v["double_rounding"] = nr_check_double_rounding(r)
        if v["double_rounding"]["result"].startswith("FAIL"):
            bad.append(("double-rounding", v["double_rounding"]["result"]))
        v["correction"] = nr_check_correction(r)
        if v["correction"]["result"].startswith("FAIL"):
            bad.append(("correction", v["correction"]["result"]))
        v["correction_declared"] = nr_check_corr_declared(r)
        if v["correction_declared"]["result"].startswith("FAIL"):
            bad.append(("correction-declared", v["correction_declared"]["result"]))
        v["corrected_in_note"] = nr_check_corrected(r, v["locator"], figidx)
        if v["corrected_in_note"]["result"].startswith("FAIL"):
            bad.append(("corrected-in-note", v["corrected_in_note"]["result"]))
    elif kind == "not-figure":
        if st != "n/a":
            bad.append(("schema", f"not-figure with status {st!r}"))
        if not r.get("not_figure_reason"):
            bad.append(("schema", "not-figure without a not_figure_reason"))
        for f in ("correction", "corrected_in_note", "status_basis"):
            if r.get(f) is not None:
                bad.append(("schema", f"not-figure with {f}"))
        if key in NR_CORRECTIONS:
            bad.append(("correction-declared", "FAIL: the script declares a correction on a row that is not a figure"))
    else:
        bad.append(("schema", f"kind {kind!r}"))
    ex = r.get("validation_exempts") or {}
    if not isinstance(ex, dict):
        bad.append(("schema", "validation_exempts must map a check to the failure message it explains"))
        ex = {}
    if ex and not r.get("validation_note"):
        bad.append(("schema", "validation_exempts without a validation_note"))
    if r.get("validation_note") and not ex:
        bad.append(("schema", "validation_note without validation_exempts (round 5: a note names the check it explains)"))
    for e in ex:
        if e not in NR_EXEMPTABLE:
            bad.append(("schema", f"validation_exempts names {e!r}, which no note can exempt"))
    # round 6 (n1chk2 finding 4): an exemption holds only for the row as declared in the script (NR_EXEMPT_FP)
    if ex or key in NR_EXEMPT_FP:
        fp = nr_fingerprint(r)
        v["fingerprint"] = fp
        if key not in NR_EXEMPT_FP:
            bad.append(("exemption-declared", f"an exemption the script does not declare (NR_EXEMPT_FP; fingerprint "
                                              f"{fp})"))
        elif not ex:
            bad.append(("exemption-declared", "the script declares an exemption on this row and the row carries none"))
        elif fp != NR_EXEMPT_FP[key]:
            bad.append(("exemption-declared", f"the row changed after its exemption was declared (fingerprint {fp}, "
                                              f"declared {NR_EXEMPT_FP[key]})"))
    if "locator-value" in ex:
        q = r.get("validation_quote")
        lls = [l for l in nr_parse_locs(r.get("locator")) if l["lines"]]
        first = nr_line(lls[0]["rev"], lls[0]["path"], lls[0]["lines"][0]) if lls else None
        if not q or first is None or q not in first:
            bad.append(("validation-quote", "an exemption from locator-value needs a validation_quote on the row's "
                                            "first cited line"))

    # round 6 (n1chk2 finding 4): an exemption explains a failure only when it equals the whole message
    def is_explained(c, m):
        return c in NR_EXEMPTABLE and isinstance(ex.get(c), str) and ex.get(c) == m
    for e, msg in ex.items():
        if e in NR_EXEMPTABLE and not any(c == e and msg == m for c, m in bad):
            bad.append(("schema", f"validation_exempts names {e!r} with {msg!r}, which equals no failure message of "
                                  f"that check (an unused, stale or partial exemption)"))
    failures = [(c, m) for c, m in bad if not is_explained(c, m)]
    explained = [(c, m) for c, m in bad if is_explained(c, m)]
    return v, failures, explained


_TOPO_H: dict = {}


def topo_h(c):
    """Position of a commit in `git rev-list --topo-order HEAD` (0 = newest); section 9 reaches past the audit pin."""
    if not _TOPO_H:
        for i, s in enumerate(git("rev-list", "--topo-order", "HEAD").split()):
            _TOPO_H[s] = i
    if c and len(c) < 40:
        c = full(c)
    return _TOPO_H.get(c)


def latest_h(cs):
    cs = [c for c in cs if c]
    if not cs:
        return None
    idx = [(topo_h(c), full(c) if len(c) < 40 else c) for c in cs]
    if any(i is None for i, _ in idx):
        raise SystemExit(f"commit(s) not ancestors of HEAD: {[c for i, c in idx if i is None]}")
    return min(idx)[1]


def earliest_h(cs):
    cs = [c for c in cs if c]
    if not cs:
        return None
    idx = [(topo_h(c), full(c) if len(c) < 40 else c) for c in cs]
    if any(i is None for i, _ in idx):
        raise SystemExit(f"commit(s) not ancestors of HEAD: {[c for i, c in idx if i is None]}")
    return max(idx)[1]


_ANC: dict = {}


def at_or_before_pin(rev):
    if rev not in _ANC:
        _ANC[rev] = subprocess.run(["git", "-C", str(REPO), "merge-base", "--is-ancestor", rev, PIN]).returncode == 0
    return _ANC[rev]


def nr_is_audit_path(p):
    return p.startswith("results/raw/2026-10-08_note-") or p.startswith("results/raw/2026-10-09_note-") or p == "README-NOTE.md"


def nr_record_entry_from_locs(locs):
    """Record locators (a revision at or before the record pin, a path that is not an audit output): each locator is
    one carrier entering at its latest line's blamed commit; a row's carriers are alternatives, so the row enters with
    the earliest (the provisional ledger's round-3 rule)."""
    carriers = []
    for l in locs:
        if not l["lines"] or nr_is_audit_path(l["path"]) or not at_or_before_pin(l["rev"]):
            continue
        if nr_lines_at(l["rev"], l["path"]) is None:
            continue
        cs = [blame_line(l["path"], l["rev"], n) for n in l["lines"]]
        carriers.append(dict(locator=f"{l['path']}@{l['rev']}:{','.join(str(n) for n in l['lines'])}",
                             commit=latest_h(cs)))
    return carriers


def final_note_rows(path, ledger, raws, note_res, watch, D=None, raw_bytes=None, stop_after_validation=False):
    """Validate the note rows and compute section 9 (see the block comment above NOTE_ROUTED). D and raw_bytes,
    when given, are the rows data in memory (the round-5 mutation self-test passes mutated copies)."""
    if D is None:
        p = REPO / path if not Path(path).is_absolute() else Path(path)
        raw_bytes = p.read_bytes()
        D = json.loads(raw_bytes)
    rows = D["rows"]
    # 0. round 5 (finding 2): the matcher-unit -> kind assignment is frozen by its hash (a validation failure below)
    kh = sha256(nr_kind_lines(rows).encode("utf-8"))
    # 1. the note files: sha256 against the routed values, and their text (the matcher's extraction)
    files, texts = [], {}
    for f in NOTE_ROUTED:
        b, t = note_text(REPO / f)
        h = sha256(b)
        a, z = NOTE_ROUTED[f]
        ok = (h == a) if not z else (h.startswith(a) and h.endswith(z))
        if not ok:
            raise SystemExit(f"{f}: sha256 {h} does not match the routed {a}...{z}")
        dec = [x for x in D.get("note_files", []) if x["path"] == f]
        if not dec or dec[0]["sha256"] != h:
            raise SystemExit(f"{f}: the rows file declares another sha256 ({dec[0]['sha256'] if dec else None})")
        files.append(dict(path=f, sha256=h, routed=a + ("..." + z if z else ""), match=ok, tracked=bool(
            git("ls-files", "--", f).strip())))
        texts[f] = t.split("\n")
    # 2. coverage: every matcher unit has a row, per file (multiset over (line, unit))
    cover = []
    for res in note_res or []:
        mu = {}
        for x in res["numerals"]:
            mu[(x["line"], x["text"])] = mu.get((x["line"], x["text"]), 0) + 1
        ru = {}
        for r in rows:
            if r["note_file"] == res["path"]:
                k = (r["note_line"], nr_unit(r))
                ru[k] = ru.get(k, 0) + 1
        miss = {f"{k[0]}:{k[1]}": v - ru.get(k, 0) for k, v in mu.items() if ru.get(k, 0) < v}
        extra = {f"{k[0]}:{k[1]}": v - mu.get(k, 0) for k, v in ru.items() if mu.get(k, 0) < v}
        cover.append(dict(path=res["path"], matcher_units=sum(mu.values()), rows=sum(ru.values()),
                          matcher_units_without_row=miss, rows_beyond_matcher=extra))
        if miss:
            raise SystemExit(f"{res['path']}: matcher units without a row: {miss}")
    # 3. per-row validation (round 5: every check named; a note explains only the check it names)
    figidx = nr_fig_index(raws)
    fails, explained = [], []
    if kh != NR_KIND_SHA256:
        nf_ = sum(1 for r in rows if r.get("kind") == "figure")
        fails.append(dict(row="(all rows)", file=None, line=None, unit=None, status=None, validation_note=None,
                          failures=[f"kind-hash: the unit -> kind assignment hashes to {kh[:16]}..., not the frozen "
                                    f"{NR_KIND_SHA256[:16]}... ({nf_} figures, {len(rows) - nf_} other; a deliberate "
                                    f"change is made in NR_KIND_SHA256 too)"]))
    # round 6 (n1chk2 finding 7): the clauses are frozen the same way
    clh = sha256(nr_clause_lines(rows).encode("utf-8"))
    if clh != NR_CLAUSE_SHA256:
        fails.append(dict(row="(all rows)", file=None, line=None, unit=None, status=None, validation_note=None,
                          failures=[f"clause-hash: the clauses hash to {clh[:16]}..., not the frozen "
                                    f"{NR_CLAUSE_SHA256[:16]}... (a deliberate change is made in NR_CLAUSE_SHA256 too)"]))
    # round 6 (n1chk2 finding 4): every exemption the script declares is on a row of the file
    gone = sorted(k for k in NR_EXEMPT_FP if k not in {f"{r['span']}#{r['seq']}" for r in rows})
    if gone:
        fails.append(dict(row="(all rows)", file=None, line=None, unit=None, status=None, validation_note=None,
                          failures=[f"exemption-declared: NR_EXEMPT_FP names rows the file does not have: {gone}"]))
    # round 7 (r6chk findings 2-4): the status and text freezes and the quotation scan, computed on the file as read
    # (before the rows carry this run's own fields) and reported after the rows' own failures
    sth, txh, qhits = nr_status_freeze(rows), nr_text_freeze(D), nr_quote_scan(D)
    for r in rows:
        key = f"{r['span']}#{r['seq']}"
        r["_key"] = key
        v, bad, exp_ = nr_validate_row(r, texts, ledger, figidx)
        r["_validation"] = v
        r["_failures"] = [f"{c}: {m}" for c, m in bad + exp_]
        r["_explained"] = [c for c, _ in exp_]
        if bad:
            fails.append(dict(row=key, file=r.get("note_file"), line=r.get("note_line"), unit=nr_unit(r),
                              status=r.get("status"), failures=[f"{c}: {m}" for c, m in bad],
                              validation_note=r.get("validation_note")))
        if exp_:
            explained.append(dict(row=key, file=r.get("note_file"), line=r.get("note_line"), unit=nr_unit(r),
                                  status=r.get("status"), failures=[f"{c}: {m}" for c, m in exp_],
                                  exempts=r.get("validation_exempts"), validation_note=r.get("validation_note"),
                                  validation_quote=r.get("validation_quote")))
    if sth != NR_STATUS_SHA256:
        fails.append(dict(row="(all rows)", file=None, line=None, unit=None, status=None, validation_note=None,
                          failures=[f"status-hash: the status-deciding fields hash to {sth[:16]}..., not the frozen "
                                    f"{NR_STATUS_SHA256[:16]}... (a deliberate change of a status, maps_to, ledger row "
                                    f"or status basis, or of a not-found row's locator or source value, is made in "
                                    f"NR_STATUS_SHA256 too)"]))
    if txh != NR_TEXT_SHA256:
        fails.append(dict(row="(all rows)", file=None, line=None, unit=None, status=None, validation_note=None,
                          failures=[f"text-hash: the free text and change history hash to {txh[:16]}..., not the "
                                    f"frozen {NR_TEXT_SHA256[:16]}... (a deliberate change is made in NR_TEXT_SHA256 "
                                    f"too)"]))
    qbad = [q for q in qhits if not q["reviewed"]]
    if qbad:
        fails.append(dict(row="(all rows)", file=None, line=None, unit=None, status=None, validation_note=None,
                          failures=[f"quote-scan: {len(qbad)} quoted span(s) of fifteen words or more near the name of "
                                    f"an external source, not declared in NR_QUOTE_REVIEWED: "
                                    + "; ".join(f"{q['where']} ({q['words']} words, {q['sha']})" for q in qbad)]))
    if stop_after_validation and fails:
        return dict(stopped_after_validation=True, validation=dict(failures=fails, explained=explained))
    noted_ok = [f"{r['span']}#{r['seq']}" for r in rows if r.get("validation_note") and not r["_failures"]]
    figs = [r for r in rows if r["kind"] == "figure"]
    byk = {r["_key"]: r for r in rows}
    # the status the pass check reads: the row's own, except where its ledger row's item raw gives no status in N1's
    # vocabulary (base 'other' or 'mixed'); then the ledger row's, as the provisional ledger's note 2 and hard rule 4
    # require (N1 does not assign such a row a status)
    for r in figs:
        ids, _ = nr_row_ledger_ids(r)
        lst = sorted({rr["base_status"] or "none" for rr in ledger[ids[0]]["refs"]}) if ids and ids[0] in ledger else []
        if lst and set(lst) <= {"other", "mixed"} and r["status"] not in lst:
            r["_eff"] = "outside N1's vocabulary (" + "/".join(lst) + f", {ids[0]})"
        else:
            r["_eff"] = r["status"]
    pc = {}
    for r in figs:
        pc.setdefault(r["_eff"], []).append(r["_key"])
    # round 5 (finding 6): a discrepant row the note already corrects (corrected_in_note, verified) passes; round 6
    # (n1chk2 finding 2): the rows marked are exactly NR_DISC's branch C, the rows whose own cause says the note now
    # carries the correction
    corrected = [r["_key"] for r in figs if r["status"] == "discrepant" and r.get("corrected_in_note")
                 and r["_validation"].get("corrected_in_note", {}).get("result") == "pass"]
    c_branch = sorted(k for k, (b_, _) in NR_DISC.items() if b_ == "C")
    marked = sorted(r["_key"] for r in rows if r.get("corrected_in_note") is not None)
    if marked != c_branch or sorted(corrected) != c_branch:
        raise SystemExit(f"corrected_in_note rows {marked} (verified {sorted(corrected)}) are not NR_DISC's branch C "
                         f"{c_branch}")
    passing = [r["_key"] for r in figs if r["_eff"] in ("reproduced", "log-only")] + corrected
    loc_ok = [k for k in passing if byk[k]["_validation"]["locator"]["result"] == "pass"
              or "locator-value" in (byk[k].get("validation_exempts") or [])]
    # 4. discrepant branches (asserted against each row's cause) and the not-found / not-run lists
    disc = []
    for r in figs:
        if r["status"] != "discrepant":
            continue
        if r["_key"] not in NR_DISC:
            raise SystemExit(f"discrepant row {r['_key']} has no NR_DISC entry")
        br, q = NR_DISC[r["_key"]]
        if q not in (r.get("cause") or ""):
            raise SystemExit(f"NR_DISC quote not in {r['_key']}'s cause: {q!r}")
        disc.append(dict(row=r["_key"], file=r["note_file"], line=r["note_line"], unit=nr_unit(r),
                         ledger_row=r.get("ledger_row"), branch=br, quoted=q, cause=r.get("cause"),
                         clause=r.get("clause")))
    stale = [k for k in NR_DISC if k not in byk or byk[k]["status"] != "discrepant"]
    if stale:
        raise SystemExit(f"NR_DISC entries for rows that are not discrepant: {stale}")
    nf = [dict(row=r["_key"], file=r["note_file"], line=r["note_line"], unit=nr_unit(r), clause=r.get("clause"),
               cause=r.get("cause"), comment=r.get("comment"), ledger_row=r.get("ledger_row")) for r in figs
          if r["status"] == "not found"]
    nrun = [dict(row=r["_key"], file=r["note_file"], line=r["note_line"], unit=nr_unit(r), clause=r.get("clause"),
                 comment=r.get("comment"), ledger_row=r.get("ledger_row")) for r in figs if r["status"] == "not run"]
    n19 = []
    for x in sorted((REPO / "results" / "raw").glob("*N19*")):
        rel = str(x.relative_to(REPO))
        d19 = dict(path=rel, sha256=sha256(x.read_bytes()), tracked=bool(git("ls-files", "--", rel).strip()))
        d19["commit"] = last_change(rel, "HEAD") if d19["tracked"] else None
        d19["equal_to_committed"] = (sha256(show("HEAD", rel)) == d19["sha256"]) if d19["tracked"] else None
        if x.suffix == ".md":
            st19 = []
            for i, l in enumerate(x.read_text(encoding="utf-8", errors="replace").split("\n"), start=1):
                for v in ("0.394", "0.70"):
                    if l.startswith(f"| {v} ("):
                        cells = [c.strip() for c in l.strip().strip("|").split("|")]
                        st19.append(dict(value=v, line=i, status=cells[1] if len(cells) > 1 else None))
            d19["status_rows"] = st19
        n19.append(d19)
    # 5. watch-list outcomes: matcher hits per id, text search, and the asserted rows
    hits = {}
    for res in note_res or []:
        for h in res["watch_hits"]:
            hits.setdefault(h["watch"], []).append(dict(file=res["path"], line=h["line"], unit=h["text"],
                                                         excluded=h.get("excluded")))
    wl = {w["id"]: w for w in watch}
    watch_out = []
    for w in NR_WATCH + NR_WATCH_EXTRA:
        for k, s_ in w["rows"]:
            if k not in byk or byk[k]["status"] != s_:
                raise SystemExit(f"NR_WATCH {w['id']}: row {k} is not {s_!r}")
        if w.get("note"):
            sp, q = w["note"]
            spn = [s for s in D["spans"] if s["span"] == sp][0]["span_notes"]
            if not any(q in x for x in spn):
                raise SystemExit(f"NR_WATCH {w['id']}: quote not in {sp}'s span notes: {q!r}")
        found = []
        needles = list(wl[w["id"]]["quotes"]) if w["id"] in wl else [w["text"]]
        for f, ls in texts.items():
            for i, s in enumerate(ls, start=1):
                for nd in needles:
                    nd_ = nd.strip("'")
                    if nd_ and nd_ in s:
                        found.append(dict(file=f, line=i, text=nd_))
        watch_out.append(dict(id=w["id"], matcher_hits=hits.get(w["id"], []), text_hits=found,
                              rows=[dict(row=k, status=s_, file=byk[k]["note_file"], line=byk[k]["note_line"],
                                         unit=nr_unit(byk[k])) for k, s_ in w["rows"]],
                              outcome=w["outcome"],
                              what=wl[w["id"]]["what"] if w["id"] in wl else w.get("what"),
                              locator=wl[w["id"]]["locator"] if w["id"] in wl else None))
    # every matcher watch hit must be accounted for by a listed row (same file, line, unit) or a stated collision
    for wo in watch_out:
        for h in wo["matcher_hits"]:
            rk = [r["_key"] for r in rows if r["note_file"] == h["file"] and r["note_line"] == h["line"]
                  and nr_unit(r) == h["unit"]]
            h["rows"] = rk
            h["listed"] = any(x["row"] in rk for x in wo["rows"])
    # open items (9h), each row's status and each span-note quote asserted
    spn_by = {s_["span"]: s_["span_notes"] for s_ in D["spans"]}
    open_items = []
    for o in NR_OPEN:
        for k, s_ in o["rows"]:
            if k not in byk or byk[k]["status"] != s_:
                raise SystemExit(f"NR_OPEN {o['id']}: row {k} is not {s_!r}")
        # round 6 (n1chk2 finding 5): an item that rests on a correction names it, and the row carries it
        for k in o.get("corrections", []):
            if k not in NR_CORRECTIONS or not isinstance(byk.get(k, {}).get("correction"), dict):
                raise SystemExit(f"NR_OPEN {o['id']}: row {k} carries no declared correction")
        locs_ = []
        for sp, q in o["notes"]:
            hit = [i for i, x in enumerate(spn_by[sp]) if q in x]
            if len(hit) != 1:
                raise SystemExit(f"NR_OPEN {o['id']}: quote not unique in {sp}'s span notes: {q!r} {hit}")
            locs_.append(f"{sp} span note {hit[0]}")
        open_items.append(dict(id=o["id"], what=o["what"], text=o["text"], corrections=o.get("corrections", []),
                               rows=[dict(row=k, status=s_, file=byk[k]["note_file"], line=byk[k]["note_line"],
                                          unit=nr_unit(byk[k])) for k, s_ in o["rows"]], span_notes=locs_))
    t_rows = [x["row"] for x in disc if x["branch"] == "T"]
    if sorted(t_rows) != sorted(NR_T_ROWS):
        raise SystemExit(f"NR_T_ROWS differs from the T-branch rows: {sorted(t_rows)}")
    if sorted(x["row"] for x in nf) != sorted(NR_NF_ROWS):
        raise SystemExit(f"NR_NF_ROWS differs from the not-found rows: {sorted(x['row'] for x in nf)}")
    # 6. entry commits per figure (section 9g)
    fig_index = {}
    for item in raws.js:
        for i, f in enumerate(raws.figures(item)):
            try:
                rr = raws.resolve((item, "id", f["id"]) if f.get("id") and item == "N3" else F(item, f.get("figure")))
            except SystemExit:
                continue
            fig_index[(RAWS[item][0], rr["md_line"])] = rr
    raw_md = {v[0] for v in RAWS.values()}

    def fig_record(rr):
        if rr.get("_rec") is None:
            ps = parse_sources(rr.get("source"))
            hints = [os.path.dirname(x["path"]) for x in ps if "/" in x["path"] and x["path"].startswith("data/")]
            hints += ITEM_DIRS.get(rr.get("item") or "", [])
            srcs = [classify_source(x, hints) for x in ps]
            cs = [e["commit"] for s in srcs if s["kind"] in ("artifact", "line locator") for e in s["entries"]
                  if e.get("commit")]
            rr["_rec"] = (latest_h(cs), base_status(rr.get("status")), [s["raw"] for s in srcs
                                                                         if s["kind"] in ("artifact", "line locator")])
        return rr["_rec"]

    entries = []
    for r in figs:
        st = r["status"]
        e = dict(row=r["_key"], status=st)
        if st in ("not found", "not run"):
            e.update(record=None, audit=None, how="enters no commit (" + st + ")", computed_new=False, basis=None)
            entries.append(e)
            continue
        locs = nr_parse_locs(r.get("locator"))
        ids, _ = nr_row_ledger_ids(r)
        rec, how, aud, fc = None, None, None, None
        al = [l for l in locs if l["lines"] and nr_is_item_raw(l["path"])]
        # computed-new, strictly: the row's own status, its ledger row's or its item-raw figure row's
        computed, basis = st == "computed-new", ("the row's status" if st == "computed-new" else None)
        lrow = ledger.get(ids[0]) if ids else None
        if lrow is not None:
            rec, how = lrow["entry_record"], f"ledger {ids[0]} entry (record sources)"
            fc = lrow.get("entry_note_first_carrier")
            if not computed and any(rr["base_status"] == "computed-new" for rr in lrow["refs"]):
                computed, basis = True, f"ledger {ids[0]}"
        carriers = nr_record_entry_from_locs(locs) + nr_record_entry_from_locs(nr_parse_locs(r.get("source_value")))
        if rec is None and lrow is None and r["maps_to"] == "record" and carriers:
            rec, how = earliest_h([c["commit"] for c in carriers]), "record locators (first carrier)"
        if rec is None and lrow is None and not computed and r["maps_to"] in ("item-raw", "audit-raw-new"):
            for l in locs:
                if l["path"] in raw_md and l["lines"]:
                    same = full(l["rev"]) == full(AUDIT) or all(
                        nr_line(l["rev"], l["path"], n) is not None and
                        nr_line(l["rev"], l["path"], n) == nr_line(AUDIT, l["path"], n) for n in l["lines"])
                    hit = next((fig_index[(l["path"], n)] for n in l["lines"] if same and (l["path"], n) in fig_index),
                               None)
                    if hit:
                        c, bst, srcs = fig_record(hit)
                        if bst == "computed-new":
                            computed, basis = True, f"item-raw figure row {hit['locator']}"
                        elif c:
                            rec, how = c, f"item-raw figure row {hit['locator']} -> its sources ({'; '.join(srcs)[:200]})"
                        break
            if rec is None and not computed and carriers:
                rec, how = earliest_h([c["commit"] for c in carriers]), "record locators named in the row (first carrier)"
        # computed-new, as a fallback where no record entry was found: the row's source value is computed-new by the
        # row's own words or by the first item-raw line it cites (a discrepant row's reproduced value can be one)
        if rec is None and not computed and (
                "computed-new" in str(r.get("source_value") or "") or bool(al and "computed-new" in (
                    nr_line(al[0]["rev"], al[0]["path"], al[0]["lines"][0]) or ""))):
            computed, basis = True, "the row's source value (its words or its cited item-raw line)"
        # round 5 (N19): a figure the audit reproduced from an external source, whose only carrier in the record is an
        # audit raw committed after the audit pin (N19's, at e0fd85c), enters with that raw
        audit_only = bool(rec is None and not computed and al and al[0]["path"] not in raw_md)
        if audit_only:
            basis = f"its only carrier is the audit raw {al[0]['path']} (reproduced there from an external source)"
        if computed or audit_only:
            if al:
                l = al[0]
                aud = latest_h([blame_line(l["path"], l["rev"], n) for n in l["lines"]])
                e["audit_locator"] = f"{l['path']}@{l['rev']}:{','.join(str(n) for n in l['lines'])}"
            elif lrow is not None and lrow.get("entry_with_audit"):
                aud = lrow["entry_with_audit"]
                e["audit_locator"] = f"ledger {ids[0]} entry (+audit)"
        if audit_only:
            how = "reproduced in an audit raw from an external source: enters with that raw"
        e.update(record=rec, how=how or ("computed-new: its only source is an audit raw" if computed else
                                          "UNRESOLVED (no ledger row, record locator or item-raw figure row with "
                                          "record sources)"),
                 audit=aud, first_carrier=fc if fc and rec and topo_h(fc) < topo_h(rec) else None,
                 computed_new=computed, audit_only=audit_only, basis=basis, carriers=carriers)
        entries.append(e)
    rec_rows = [e for e in entries if e["record"]]
    cand_rec = latest_h([e["record"] for e in rec_rows])
    cand_fc = latest_h([e["first_carrier"] or e["record"] for e in rec_rows])
    def with_audit(e):
        return e["audit"] if (e["computed_new"] or e.get("audit_only")) and e["audit"] else e["record"]
    cand_aud = latest_h([with_audit(e) for e in entries if with_audit(e)])
    unresolved = [e for e in entries if not e["record"] and not e.get("computed_new") and not e.get("audit_only")
                  and e["status"] not in ("not found", "not run")]
    head = full("HEAD")
    T = dict(
        record_sources_only=dict(commit=cand_rec, date=cdate(cand_rec) if cand_rec else None,
                                 rows=[e["row"] for e in rec_rows if e["record"] == cand_rec]),
        record_with_first_carriers=dict(commit=cand_fc, date=cdate(cand_fc) if cand_fc else None,
                                        rows=[e["row"] for e in rec_rows if (e["first_carrier"] or e["record"]) == cand_fc]),
        including_audit_raws=dict(commit=cand_aud, date=cdate(cand_aud) if cand_aud else None,
                                  rows=[e["row"] for e in entries if with_audit(e) == cand_aud]),
        first_carrier_rows=[dict(row=e["row"], record=e["record"], first_carrier=e["first_carrier"]) for e in entries
                            if e.get("first_carrier")],
        computed_without_audit=[e["row"] for e in entries if e["computed_new"] and not e["audit"]],
        audit_only_rows=[dict(row=e["row"], audit=e["audit"], locator=e.get("audit_locator")) for e in entries
                         if e.get("audit_only")],
        unresolved_rows=[dict(row=e["row"], status=e["status"]) for e in unresolved],
        head_at_run=head,
        candidate_is_ancestor_of_head=bool(cand_aud) and subprocess.run(
            ["git", "-C", str(REPO), "merge-base", "--is-ancestor", cand_aud, head]).returncode == 0,
        n_figures_entering=len([e for e in entries if e["record"] or e["audit"]]),
    )
    # 7. the not-figure summary, by reason group
    nfig = [r for r in rows if r["kind"] != "figure"]
    groups = {}
    for r in nfig:
        reason = (r.get("not_figure_reason") or "").lower()
        g = next(name for name, pat in NR_REASON_GROUPS if re.search(pat, reason))
        x = groups.setdefault(g, dict(n=0, by_file={}, reasons=set()))
        x["n"] += 1
        x["by_file"][r["note_file"]] = x["by_file"].get(r["note_file"], 0) + 1
        x["reasons"].add(r.get("not_figure_reason"))
    nf_summary = [dict(group=g, n=x["n"], by_file=x["by_file"], n_distinct_reasons=len(x["reasons"]))
                  for g, x in sorted(groups.items(), key=lambda kv: -kv[1]["n"])]
    # 8. span notes with their keyword
    sn = []
    for s in D["spans"]:
        ann = {}
        for a in s.get("span_note_annotations", []):
            if not (0 <= a["index"] < len(s["span_notes"])) or a["quote"] not in s["span_notes"][a["index"]]:
                raise SystemExit(f"span-note annotation for {s['span']} #{a['index']}: quote not in that note")
            ann.setdefault(a["index"], []).append(a["text"])
        for i, t in enumerate(s["span_notes"]):
            marks = list(dict.fromkeys(m.group(1) for m in NR_NOTE_MARK_RE.finditer(t)))
            sn.append(dict(span=s["span"], index=i, markers=marks, stop=bool(re.search(r"\bSTOP\b", t)), text=t,
                           annotations=ann.get(i, [])))
    counts = {}
    for r in figs:
        counts.setdefault(r["note_file"], {})
        counts[r["note_file"]][r["status"]] = counts[r["note_file"]].get(r["status"], 0) + 1
    return dict(
        rows_file=str(path), rows_file_sha256=sha256(raw_bytes), files=files, coverage=cover,
        n_rows=len(rows), n_figures=len(figs), n_not_figures=len(nfig), status_counts_by_file=counts,
        validation=dict(n_rows=len(rows), failures=fails, explained=explained, noted_but_passing=noted_ok,
                        locator_results={k: sum(1 for r in figs if r["_validation"].get("locator", {}).get("result", "")
                                                 .startswith(k)) for k in ("pass", "FAIL", "n/a")},
                        locator_secondary=[r["_key"] for r in figs if r["_validation"].get("locator", {})
                                           .get("where") == "secondary"]),
        pass_check=dict(n_figures=len(figs), by_status={k: len(v) for k, v in pc.items()}, rows_by_status=pc,
                        passing=len(passing), passing_with_a_validated_locator=len(loc_ok),
                        passing_without=[k for k in passing if k not in loc_ok], corrected_in_note=corrected),
        corrections=[dict(row=r["_key"], file=r["note_file"], line=r["note_line"], unit=nr_unit(r), status=r["status"],
                          **{k: r["correction"].get(k) for k in ("kind", "text", "whose", "basis")})
                     for r in figs if r.get("correction")],
        round5=[dict(row=r["_key"], file=r["note_file"], line=r["note_line"], unit=nr_unit(r), status=r.get("status"),
                     kind=r.get("kind"), **r["round5"]) for r in rows if r.get("round5")],
        status_check={k: sum(1 for r in figs if (r["_validation"].get("status", {}).get("how") or
                                                  r["_validation"].get("status", {}).get("result", ""))
                             .startswith(k)) for k in ("JSON figure row", "status cell", "status tag", "status_basis",
                                                       "record lines only", "audit-raw-new", "n/a")},
        kind_sha256=NR_KIND_SHA256, clause_sha256=NR_CLAUSE_SHA256, status_sha256=NR_STATUS_SHA256,
        text_sha256=NR_TEXT_SHA256, quote_scan=qhits,
        check_counts={c: {k: sum(1 for r in figs if str(r["_validation"].get(f, {}).get("result", "n/a"))
                                 .startswith(k)) for k in ("pass", "FAIL", "n/a")}
                      for c, f in (("maps-to", "maps_to"), ("pins", "pins"), ("unit-stated", "unit_stated"),
                                   ("correction-declared", "correction_declared"), ("ledger-bind", "ledger_bind"),
                                   ("ledger-status", "ledger"), ("status", "status"))},
        round6=[dict(row=r["_key"], file=r["note_file"], line=r["note_line"], unit=nr_unit(r), status=r.get("status"),
                     kind=r.get("kind"), **r["round6"]) for r in rows if r.get("round6")],
        round7=[dict(row=r["_key"], file=r["note_file"], line=r["note_line"], unit=nr_unit(r), status=r.get("status"),
                     kind=r.get("kind"), **r["round7"]) for r in rows if r.get("round7")],
        discrepant=disc, not_found=nf, not_run=nrun, n19_raws_present=n19,
        watch=watch_out, entries=entries, tag=T, not_figure_summary=nf_summary, span_notes=sn, open_items=open_items,
        spans=[dict(span=s["span"], header=s["header"], summary=s.get("summary")) for s in D["spans"]],
        provenance=D.get("provenance"), how_built=D.get("how_built"),
        rows=[{k: v for k, v in r.items() if not k.startswith("_")} | dict(
            validation=r["_validation"], failures=r["_failures"], pass_check_status=r.get("_eff")) for r in rows],
    )


# ------------------------------------------------------------------ round 5: the mutation self-test (finding 2)
# Each mutation changes the rows data in memory (never the file) and the run is repeated on it: a mutation is caught
# when the validation reports a failure no named exemption explains, or when the run stops (a frozen hash, coverage,
# or an assertion on a row the script names). 'checker' = the final checker's 29 mutations (its mutate.py, scratch),
# reproduced as written unless the row has since changed (then adapted, and the 'what' says how); 'round 5' = Code's.
def _nr_row(D, key):
    s_, q = key.split("#")
    m = [r for r in D["rows"] if r["span"] == s_ and r["seq"] == int(q)]
    if len(m) != 1:
        raise KeyError(key)
    return m[0]


def _m_set(key, **kv):
    def f(D):
        r = _nr_row(D, key)
        for k, v in kv.items():
            if v is None:
                r.pop(k, None)
            else:
                r[k] = v
    return f


def _m_sub(key, field, old, new):
    def f(D):
        r = _nr_row(D, key)
        assert old in str(r.get(field)), (key, field, old)
        r[field] = r[field].replace(old, new, 1)
    return f


def _m_line(key, d):
    def f(D):
        _nr_row(D, key)["note_line"] += d
    return f


def _m_kind_nf(key):
    def f(D):
        r = _nr_row(D, key)
        r.update(kind="not-figure", status="n/a", not_figure_reason="prose")
    return f


def _m_delete(key):
    def f(D):
        D["rows"].remove(_nr_row(D, key))
    return f


def _m_many(*fs):
    def f(D):
        for x in fs:
            x(D)
    return f


def _m_loc(key, loc, where="prefix"):
    """Round 7: a locator with one more line, before ('prefix') or after ('suffix') the row's own."""
    def f(D):
        r = _nr_row(D, key)
        r["locator"] = (loc + "; " + (r.get("locator") or "")) if where == "prefix" else ((r.get("locator") or "") + "; " + loc)
    return f


def _m_span_note(span, idx, old, new):
    def f(D):
        s_ = [x for x in D["spans"] if x["span"] == span][0]
        assert old in s_["span_notes"][idx], (span, idx, old)
        s_["span_notes"][idx] = s_["span_notes"][idx].replace(old, new, 1)
    return f


def _m_history(key, rnd, new):
    def f(D):
        ch = _nr_row(D, key)[rnd]["changed"]
        assert ch, key
        ch[0]["previous"] = new
    return f


def _m_note_sha(path, new):
    def f(D):
        [x for x in D["note_files"] if x["path"] == path][0]["sha256"] = new
    return f


_N2 = "results/raw/2026-10-08_note-N2-introspection.md"
_N2VI = "results/raw/2026-10-08_note-N2vi-source.md"
_N3 = "results/raw/2026-10-08_note-N3-echo-robustness.md"
_N3C = "results/raw/2026-10-08_note-N3-echo-compute.md"
_N4 = "results/raw/2026-10-08_note-N4-e2a.md"
# round 7: a synthetic sentence of twenty words (no source; it plants a long quotation next to an arXiv id)
_SYN20 = ("amber lanterns drift past the quiet harbour while seven grey herons count the tides beneath a patient "
          "violet moon tonight")


NR_MUTATIONS = [
    ("M01", "checker", "S6#47 note_line +1", _m_line("S6#47", 1)),
    ("M02", "checker", "S6#47 source_value '+0.0200' -> '+0.0300'", _m_sub("S6#47", "source_value", "+0.0200", "+0.0300")),
    ("M03", "checker", "S6#47 locator ':205' -> ':204'", _m_sub("S6#47", "locator", ":205", ":204")),
    ("M04", "checker", "S6#47 status -> log-only", _m_set("S6#47", status="log-only")),
    ("M05", "checker", "S6#47 deleted", _m_delete("S6#47")),
    ("M06", "checker", "S6#47 kind -> not-figure", _m_kind_nf("S6#47")),
    ("M07", "checker", "S1#147 (not found) status -> reproduced", _m_set("S1#147", status="reproduced")),
    ("M08", "checker", "S9#57 note_line +1", _m_line("S9#57", 1)),
    ("M09", "checker", "S1#137 source_value '+0.0392' -> '+0.0492'", _m_sub("S1#137", "source_value", "+0.0392", "+0.0492")),
    ("M10", "checker", "S2#37 source_value '0.0171875' -> '0.0271875'",
     _m_sub("S2#37", "source_value", "0.0171875", "0.0271875")),
    ("M11", "checker", "S1#137 locator ':355' -> ':300'", _m_sub("S1#137", "locator", ":355", ":300")),
    ("M12", "checker", "S5#14 (discrepant) status -> reproduced", _m_set("S5#14", status="reproduced")),
    ("M13", "checker", "S7#29 status -> log-only (adapted: the checker set this N19 row from 'not run' to "
                       "'reproduced', which is its status since round 5)", _m_set("S7#29", status="log-only")),
    ("M14", "checker", "S3#20 source_value '0.8533' -> '0.9533'", _m_sub("S3#20", "source_value", "0.8533", "0.9533")),
    ("M15", "checker", "S1#137 ledger_row -> L999", _m_set("S1#137", ledger_row="L999")),
    ("M16", "checker", "S6#47 ledger_row -> L001 (same status)", _m_set("S6#47", ledger_row="L001")),
    ("M17", "checker", "S10#28 note_line +3", _m_line("S10#28", 3)),
    ("M18", "checker", "S6#5 status -> discrepant", _m_set("S6#5", status="discrepant")),
    ("M19", "checker", "S1#26 kind -> not-figure", _m_kind_nf("S1#26")),
    ("M20", "checker", "S10#28 source_value '0/46' -> '0/47'", _m_sub("S10#28", "source_value", "0/46", "0/47")),
    ("M21", "checker", "S3#20 kind -> not-figure", _m_kind_nf("S3#20")),
    ("M22", "checker", "S3#11 (noted) locator ':12399' -> ':5'", _m_sub("S3#11", "locator", ":12399", ":5")),
    ("M23", "checker", "S3#20 status -> log-only", _m_set("S3#20", status="log-only")),
    ("M24", "checker", "S1#22 (item-raw) status -> log-only", _m_set("S1#22", status="log-only")),
    ("M25", "checker", "S1#22 (item-raw) status -> computed-new", _m_set("S1#22", status="computed-new")),
    ("M26", "checker", "S1#20 (item-raw, log-only) status -> reproduced", _m_set("S1#20", status="reproduced")),
    ("M27", "checker", "S2#36 (item-raw, computed-new) status -> reproduced", _m_set("S2#36", status="reproduced")),
    ("M28", "checker", "S9#57 status -> log-only", _m_set("S9#57", status="log-only")),
    ("M29", "checker", "S1#22 kind -> not-figure", _m_kind_nf("S1#22")),
    ("R01", "round 5", "S1#26 status -> discrepant (N1's round-4 classification)", _m_set("S1#26", status="discrepant")),
    ("R02", "round 5", "S1#140 status -> discrepant", _m_set("S1#140", status="discrepant")),
    ("R03", "round 5", "S1#34 status -> discrepant", _m_set("S1#34", status="discrepant")),
    ("R04", "round 5", "S3#64 correction removed (double rounding unrecorded)", _m_set("S3#64", correction=None)),
    ("R05", "round 5", "S5#14 (W3 fork) given S1#73's corrected_in_note", _m_set(
        "S5#14", corrected_in_note=dict(locator="results/raw/2026-10-08_note-N2-introspection.md@09c3a8c:51",
                                        quote="transcription, correct to +0.095"))),
    ("R06", "round 5", "S1#73 corrected_in_note quote altered", _m_set(
        "S1#73", corrected_in_note=dict(locator="results/raw/2026-10-08_note-N2-introspection.md@09c3a8c:51",
                                        quote="transcription, correct to +0.096"))),
    ("R07", "round 5", "S7#29 (N19) status -> not run", _m_set("S7#29", status="not run")),
    ("R08", "round 5", "S1#145 (audit-raw-new) status -> reproduced", _m_set("S1#145", status="reproduced")),
    ("R09", "round 5", "S5#48 (audit-raw-new) status -> reproduced", _m_set("S5#48", status="reproduced")),
    ("R10", "round 5", "S2#24 (record) status -> reproduced", _m_set("S2#24", status="reproduced")),
    ("R11", "round 5", "S1#36 (status_basis computed-new) status -> reproduced", _m_set("S1#36", status="reproduced")),
    ("R12", "round 5", "S1#22 status_basis quote altered", _m_set(
        "S1#22", status_basis=dict(locator="results/raw/2026-10-08_note-N2-introspection.md@09c3a8c:136",
                                   quote="48 per arm (24 injected / 24 control) [log-only]"))),
    ("R13", "round 5", "S1#117 restored to its round-4 mapping (record, log-only; the year is its only match)",
     _m_set("S1#117", maps_to="record", status="log-only", locator="README.md@bbc9ffe:3-4")),
    ("R14", "round 5", "S3#13 source_value -> 'see notes.md:1344' (a line number as its only value; 1344 is on the "
                       "cited line, so round 4 passed it at level B)", _m_set("S3#13", source_value="see notes.md:1344")),
    ("R15", "round 5", "S5#63 source_value -> '1.0000' (a 1 as its only value; 1.0000 is on a cited line, so round 4 "
                       "passed it at level B)", _m_set("S5#63", source_value="1.0000")),
    ("R16", "round 5", "S1#59 exemption renamed to locator-value", _m_set(
        "S1#59", validation_exempts={"locator-value": "no cited line carries a stated value"})),
    ("R17", "round 5", "S1#59 (exempted from ledger-status) status -> reproduced", _m_set("S1#59", status="reproduced")),
    ("R18", "round 5", "S3#11 (exempted from locator-value) status -> reproduced", _m_set("S3#11", status="reproduced")),
    ("R19", "round 5", "S6#84 validation_quote altered", _m_set("S6#84", validation_quote="four live captures")),
    ("R20", "round 5", "S6#3 ledger_row L164 -> L001 (same status)", _m_set("S6#3", ledger_row="L001")),
    ("R21", "round 5", "S1#137 ledger_row -> L090 (same status)", _m_set("S1#137", ledger_row="L090")),
    ("R22", "round 5", "S1#51 (exempted from ledger-span) ledger_row L084 -> L001", _m_set("S1#51", ledger_row="L001")),
    ("R23", "round 5", "S2#43 (round 5's ordinal row) kind -> not-figure", _m_kind_nf("S2#43")),
    ("R24", "round 5", "S10#17 source_value '9/44' -> '9/45'", _m_sub("S10#17", "source_value", "9/44", "9/45")),
    ("R25", "round 5", "S1#20 given a validation_note and a 'status' exemption, then status -> reproduced",
     _m_many(_m_set("S1#20", validation_note="mutation", validation_exempts={"status": "status"}),
             _m_set("S1#20", status="reproduced"))),
    ("R26", "round 5", "S7#33 correction kind -> 'opinion'", _m_set(
        "S7#33", correction=dict(kind="opinion", text="x", whose="x"))),
    # round 6: n1chk2's mutations that round 5 did not catch (its lib/muts.py, reproduced as written; E05b and C18b
    # are its decoupled twins of E05 and C18), and its two that round 5 caught only through this self-test
    ("E01", "checker 2", "S3#11 (locator-value exempt) source_value fabricated",
     _m_set("S3#11", source_value="NVIDIA H100-SXM5-80GB, eight GPUs")),
    ("E02", "checker 2", "S6#84 (locator-value and ledger-span exempt) source_value fabricated",
     _m_set("S6#84", source_value="three label-artifact classes across the four captures")),
    ("E03", "checker 2", "S9#85 (locator-value exempt) source_value fabricated",
     _m_set("S9#85", source_value="a banner carries five Note: lines")),
    ("E04", "checker 2", "S1#119 (locator-value exempt) source_value fabricated",
     _m_set("S1#119", source_value="two public lineages, Base -> Instruct")),
    ("E05", "checker 2", "S6#47 wrong value, with forged generic exemptions ('FAIL'), a note and a quote", _m_many(
        _m_sub("S6#47", "source_value", "+0.0200", "+0.0300"),
        _m_set("S6#47", validation_exempts={"locator-value": "FAIL", "source-values": "FAIL"}, validation_note="x",
               validation_quote="SOLV"))),
    ("E05b", "checker 2", "S4#34 wrong value 0.8610 -> 0.8710, with forged generic exemptions, a note and a quote",
     _m_many(_m_sub("S4#34", "source_value", "0.8610", "0.8710"), _m_sub("S4#34", "source_value", "0.861006", "0.871006"),
             _m_set("S4#34", validation_exempts={"locator-value": "FAIL", "source-values": "FAIL"}, validation_note="x",
                    validation_quote="3j-a"))),
    ("E06", "checker 2", "S1#51 (ledger-span exempt) status -> log-only", _m_set("S1#51", status="log-only")),
    ("C01", "checker 2", "S5#48 (computed-new) -> maps_to record, log-only", _m_set("S5#48", maps_to="record",
                                                                                     status="log-only")),
    ("C02", "checker 2", "S6#27 (computed-new) -> maps_to record, log-only", _m_set("S6#27", maps_to="record",
                                                                                     status="log-only")),
    ("C03", "checker 2", "S1#32 (ledger-row L062, computed-new) -> maps_to record, log-only",
     _m_set("S1#32", maps_to="record", status="log-only")),
    ("C04", "checker 2", "S8#117 (computed-new) -> maps_to record, log-only", _m_set("S8#117", maps_to="record",
                                                                                      status="log-only")),
    ("C05", "checker 2", "S4#5 (T row) given a corrected_in_note quoting its own cited line", _m_set("S4#5", corrected_in_note=dict(
        locator="results/raw/2026-10-08_note-N3-echo-robustness.md@09c3a8c:370", quote="max 0.9951 -> 0.995"))),
    ("C06", "checker 2", "S6#68 (W8, not transcription) given a corrected_in_note quoting its own cited line",
     _m_set("S6#68", corrected_in_note=dict(locator="results/raw/2026-10-08_note-N5-f1.md@09c3a8c:217",
                                            quote="termination attempts ≈ 1% of rounds by arm"))),
    ("C07", "checker 2", "S5#14 (W3 fork) given a corrected_in_note quoting its own cited line",
     _m_set("S5#14", corrected_in_note=dict(locator="results/raw/2026-10-08_note-N2vi-source.md@09c3a8c:26",
                                            quote="source instruct FPR 0.003"))),
    ("C08", "checker 2", "S1#140 correction removed", _m_set("S1#140", correction=None)),
    ("C09", "checker 2", "S1#26 correction removed", _m_set("S1#26", correction=None)),
    ("C10", "checker 2", "S7#33 correction removed", _m_set("S7#33", correction=None)),
    ("C11", "checker 2", "S1#145 correction removed", _m_set("S1#145", correction=None)),
    ("C12", "checker 2", "S1#20 source_value '60 (B2' -> '67 (B2' (an integer unit misstated)",
     _m_sub("S1#20", "source_value", "60 (B2", "67 (B2")),
    ("C13", "checker 2", "S1#37 source_value '63]' -> '70]' (an integer unit misstated)",
     _m_sub("S1#37", "source_value", "63]", "70]")),
    ("C14", "checker 2", "S2#38 source_value '0.5 ×' -> '1.5 ×' (a one-place decimal)",
     _m_sub("S2#38", "source_value", "0.5 ×", "1.5 ×")),
    ("C15", "checker 2", "S6#47 locator revision 09c3a8c -> e0fd85c (off its pin)",
     _m_sub("S6#47", "locator", "@09c3a8c", "@e0fd85c")),
    ("C16", "checker 2", "S6#47 clause '+.020' -> '+.030'", _m_sub("S6#47", "clause", "+.020", "+.030")),
    ("C18", "checker 2", "S1#36 status -> reproduced, status_basis retargeted to N3c :34 '[status: reproduced]'",
     _m_set("S1#36", status="reproduced", status_basis=dict(
         locator="results/raw/2026-10-08_note-N3-echo-compute.md@09c3a8c:34", quote="[status: reproduced]"))),
    ("C18b", "checker 2", "S1#37 status -> reproduced, status_basis retargeted to N3c :34 '[status: reproduced]'",
     _m_set("S1#37", status="reproduced", status_basis=dict(
         locator="results/raw/2026-10-08_note-N3-echo-compute.md@09c3a8c:34", quote="[status: reproduced]"))),
    ("C20", "checker 2", "S5#38 corrected_in_note removed (a corrected row stops passing)",
     _m_set("S5#38", corrected_in_note=None)),
    ("C21", "checker 2", "S1#140 correction 'whose' -> 'N5 (item raw)' (a misattribution)",
     lambda D: _nr_row(D, "S1#140")["correction"].update(whose="N5 (item raw)")),
    # round 6: Code's
    ("S01", "round 6", "S7#29 ledger-status exemption cut to a substring of its message",
     lambda D: _nr_row(D, "S7#29")["validation_exempts"].update({"ledger-status": "status 'reproduced' vs L159"})),
    ("S02", "round 6", "S5#48 locator without the column header :399 (its '97.5' then on no cited line)",
     _m_sub("S5#48", "locator", "; column header :399", "")),
    ("S03", "round 6", "S1#73 corrected_in_note quote -> '+0.095455' (on its line, without the correction wording)",
     _m_set("S1#73", corrected_in_note=dict(locator="results/raw/2026-10-08_note-N2-introspection.md@09c3a8c:51", quote="+0.095455"))),
    ("S04", "round 6", "S7#12 maps_to record -> audit-raw-new (status kept log-only)", _m_set("S7#12", maps_to="audit-raw-new")),
    ("S05", "round 6", "S1#145 correction 'whose' -> N1's own reading (the declared reading is N19's)",
     lambda D: _nr_row(D, "S1#145")["correction"].update(whose="N1's own reading")),
    ("S06", "round 6", "S3#64 correction basis -> N3's raw (the declared reading is N8's)",
     lambda D: _nr_row(D, "S3#64")["correction"].update(
         basis="results/raw/2026-10-08_note-N3-echo-robustness.md@09c3a8c:479")),
    ("S07", "round 6", "S7#15 locator given back ':174' (the unrelated 'second')",
     _m_sub("S7#15", "locator", "@bbc9ffe:345", "@bbc9ffe:345, :174")),
    ("S08", "round 6", "S6#43 source_value '17.500' -> '18.500' (the floor no longer the note's 17)",
     _m_sub("S6#43", "source_value", "17.500", "18.500")),
    ("S09", "round 6", "S1#20 correction added (not declared in the script)",
     _m_set("S1#20", correction=dict(kind="wording", text="x", whose="N1's own reading", basis=None))),
    ("S10", "round 6", "S8#79 (item-raw, computed-new; L028 related only) -> maps_to record, log-only",
     _m_set("S8#79", maps_to="record", status="log-only")),
    ("S11", "round 6", "S1#140 status_basis locator moved to N5 :79 with the same quote (not on that line)",
     lambda D: _nr_row(D, "S1#140")["status_basis"].update(locator="results/raw/2026-10-08_note-N5-f1.md@09c3a8c:79")),
    # round 7: the strict check of round 6 (r6chk; its lib/muts.py, group N, reproduced as written), the twenty that
    # round 6 did not catch (its N01-N03, N18, N19 and N21-N26, N31 were caught); and Code's
    ("N04", "checker 3", "S2#25 (record, log-only) -> reproduced, locator + an unrelated reproduced N2 figure row (:24)",
     _m_many(_m_loc("S2#25", f"{_N2}@09c3a8c:24", "suffix"), _m_set("S2#25", status="reproduced"))),
    ("N05", "checker 3", "S5#8 (item-raw, log-only) -> reproduced, locator prefixed with an unrelated reproduced N2vi "
                         "row (:34)", _m_many(_m_loc("S5#8", f"{_N2VI}@09c3a8c:34"), _m_set("S5#8", status="reproduced"))),
    ("N06", "checker 3", "S1#146 (ledger-row, log-only) -> reproduced, ledger_row L041 -> L008",
     _m_set("S1#146", status="reproduced", ledger_row="L008")),
    ("N07", "checker 3", "S1#118 (record, log-only) -> reproduced with a status_basis on an unrelated CLAUDE.md line "
                         "('reproduced')", _m_set("S1#118", status="reproduced", status_basis=dict(
                             locator="CLAUDE.md@bbc9ffe:195", quote="reproduced"))),
    ("N08", "checker 3", "S4#23 (item-raw, computed-new) status -> reproduced, one field", _m_set("S4#23", status="reproduced")),
    ("N09", "checker 3", "S5#20 (ledger-row L004 related row, computed-new) status -> reproduced, one field",
     _m_set("S5#20", status="reproduced")),
    ("N10", "checker 3", "S7#51 (item-raw, computed-new) status -> reproduced, one field", _m_set("S7#51", status="reproduced")),
    ("N11", "checker 3", "S5#23 (ledger-row L004 related row, computed-new) status -> reproduced, one field",
     _m_set("S5#23", status="reproduced")),
    ("N12", "checker 3", "S6#28 (audit-raw-new, computed-new) -> reproduced, locator prefixed with an unrelated "
                         "reproduced N4 row (:353)", _m_many(_m_loc("S6#28", f"{_N4}@09c3a8c:353"),
                                                             _m_set("S6#28", status="reproduced"))),
    ("N13", "checker 3", "S1#47 (ledger-row L082, computed-new) -> reproduced, ledger_row -> L097",
     _m_set("S1#47", status="reproduced", ledger_row="L097")),
    ("N14", "checker 3", "S5#35 (item-raw, computed-new) -> reproduced, locator prefixed with an unrelated reproduced N2 "
                         "row (:24)", _m_many(_m_loc("S5#35", f"{_N2}@09c3a8c:24"), _m_set("S5#35", status="reproduced"))),
    ("N15", "checker 3", "S3#7 (item-raw N17, log-only) -> reproduced, locator prefixed with a reproduced row of another "
                         "raw (N2 :24)", _m_many(_m_loc("S3#7", f"{_N2}@09c3a8c:24"), _m_set("S3#7", status="reproduced"))),
    ("N16", "checker 3", "S3#36 (not found) given a fabricated record locator (a real, unrelated RESULTS.md line)",
     _m_set("S3#36", locator="RESULTS.md@bbc9ffe:1912")),
    ("N17", "checker 3", "S5#77 (not found) given a fabricated locator to a nonexistent record line and file",
     _m_set("S5#77", locator="data/olmo/ablation_dprime.json@bbc9ffe:12; RESULTS.md@bbc9ffe:999999",
            source_value="ablation d′ = 1.80 (RESULTS.md@bbc9ffe:999999)")),
    ("N20", "checker 3", "S6#68 (NT) cause rewritten as a transcription, keeping the asserted quote",
     _m_set("S6#68", cause="transcription per the item raw: correct to ≈ 1.3% overall (an earlier mapping read it as "
                           "not transcription (item raw); superseded)")),
    ("N27", "checker 3", "S1#140 correction basis -> an unrelated record line (RESULTS.md :41)",
     lambda D: _nr_row(D, "S1#140")["correction"].update(basis="RESULTS.md@bbc9ffe:41")),
    ("N28", "checker 3", "S7#19 round5 change record 'previous' rewritten (change history)",
     _m_history("S7#19", "round5", "reproduced")),
    ("N29", "checker 3", "S7 span note 4: 'STOP' -> 'pass' (a span note no open item asserts)",
     _m_span_note("S7", 4, "STOP", "pass")),
    ("N30", "checker 3", "S7#73 (exempted) comment rewritten (outside the fingerprint)",
     _m_set("S7#73", comment="Fabricated comment: the block's 103/103 is the count of record.")),
    ("N32", "checker 3", "S5#22 (ledger-row L004 related row, computed-new) status -> reproduced, one field",
     _m_set("S5#22", status="reproduced")),
    ("T01", "round 7", "S9#57 status_basis removed (its cited status line, N2 :90, carries none of its values)",
     _m_set("S9#57", status_basis=None)),
    ("T02", "round 7", "S5#20 ledger_row 'related row' field states the primary row's status, and the row carries it",
     _m_set("S5#20", ledger_row="L004 (related row: N2 row 37, reproduced)", status="reproduced")),
    ("T03", "round 7", "S1#37 locator without its 'L062' (nothing then binds L062 to the row)",
     _m_sub("S1#37", "locator", "; ledger results/raw/2026-10-08_note-N1-claims-ledger.json@6485da2 L062", "")),
    ("T04", "round 7", "S2#34 ledger_row back to 'L085' (its locator names L084)", _m_set("S2#34", ledger_row="L085")),
    ("T05", "round 7", "S4#28 locator back to the bare 'stageC_analysis.json@bbc9ffe' (no such file at that revision)",
     _m_sub("S4#28", "locator", "data/echo/stageC_analysis.json@bbc9ffe", "stageC_analysis.json@bbc9ffe")),
    ("T06", "round 7", "S6#47 source value given a synthetic twenty-word quotation beside an arXiv id",
     lambda D: _nr_row(D, "S6#47").update(source_value=_nr_row(D, "S6#47")["source_value"]
                                          + f" ('{_SYN20}', arXiv:0000.00000)")),
    ("T07", "round 7", "S4#23 status_basis quote -> the line's 'reproduced' clause (status unchanged: computed-new)",
     _m_set("S4#23", status_basis=dict(locator=f"{_N3C}@09c3a8c:151",
                                       quote="which is the stored c1_read_M1M2 auc_kfold (reproduced)"))),
    ("T08", "round 7", "S1#26 correction text edited (an N1-own wording correction)",
     lambda D: _nr_row(D, "S1#26")["correction"].update(text=_nr_row(D, "S1#26")["correction"]["text"] + " (edited)")),
]


def _m_forge_ci(key):
    """A forged corrected_in_note: the first token on a cited line that ties to the note's value, quoted from the
    nearest correction wording before it on that line when there is one (n1chk2's forge_scan, generalised)."""
    def f(D):
        r = _nr_row(D, key)
        uv = [v for v in nr_unit_values(nr_unit(r))[0] if v]
        for l in nr_parse_locs(r.get("locator")):
            for n in l["lines"]:
                line = nr_line(l["rev"], l["path"], n) or ""
                for m in NR_NUM_RE.finditer(line):
                    t = nr_dec(m.group())
                    if t and any(nr_tie(t, u) for u in uv):
                        w = None
                        for mm in NR_CORR_WORD_RE.finditer(line[:m.start()]):
                            w = mm
                        r["corrected_in_note"] = dict(locator=f"{l['path']}@{l['rev']}:{n}",
                                                      quote=line[w.start():m.end()] if w else m.group())
                        return
        raise KeyError(f"{key}: no cited line carries a value tied to the note's")
    return f


def nr_family_mutations(D):
    """Round 6: the mutation families n1chk2 found open, generated from the rows (each member is one run)."""
    out = []
    figs = [r for r in D["rows"] if r.get("kind") == "figure"]
    for r in figs:
        k = f"{r['span']}#{r['seq']}"
        if r.get("status") == "computed-new":
            out.append((f"FA:{k}", "family A", f"{k} (computed-new) -> maps_to record, log-only",
                        _m_set(k, maps_to="record", status="log-only")))
    for r in figs:
        k = f"{r['span']}#{r['seq']}"
        if r.get("status") == "discrepant" and r.get("corrected_in_note") is None:
            out.append((f"FB:{k}", "family B", f"{k} (discrepant, uncorrected) given a forged corrected_in_note",
                        _m_forge_ci(k)))
    for k, (kind_, who, _fp) in NR_CORRECTIONS.items():
        out.append((f"FC:{k}", "family C", f"{k} correction removed", _m_set(k, correction=None)))
        alt = "N6 (item raw)" if who == "N1" else "N1's own reading"
        out.append((f"FD:{k}", "family D", f"{k} correction 'whose' -> {alt!r}",
                    (lambda kk, aa: lambda D_: _nr_row(D_, kk)["correction"].update(whose=aa))(k, alt)))
    for k in NR_EXEMPT_FP:
        out.append((f"FE:{k}", "family E", f"{k} each exemption cut to the first half of its message",
                    (lambda kk: lambda D_: _nr_row(D_, kk).update(validation_exempts={
                        c: m_[:len(m_) // 2] for c, m_ in _nr_row(D_, kk)["validation_exempts"].items()}))(k)))
    return out


# round 6: mutations the validator is known NOT to catch; each is a sentence of 10f, and the self-test fails if one
# is caught (10f would then be wrong). Round 7 adds a level: 'full' limits pass a whole run (10f); 'row' limits pass
# the row checks and are caught only by a round-7 freeze (status-hash), so the self-test requires both, the row checks
# NOT catching them and the whole run catching them. L01 was a 'full' limit in round 6.
NR_LIMIT_MUTATIONS = [
    ("L01", "row", "S1#25 status computed-new -> reproduced, its status_basis moved to another line of the same item raw "
                   "that gives 'reproduced' (N2 :136)", _m_set("S1#25", status="reproduced", status_basis=dict(
                       locator="results/raw/2026-10-08_note-N2-introspection.md@09c3a8c:136",
                       quote="[reproduced: artifact `n`, trial rows]"))),
    ("L02", "full", "S1#143 (a word unit that passes at level A on the word) source_value replaced by a text with no "
                    "number", _m_set("S1#143", source_value="(no number: a fabricated source text)")),
    ("L03", "full", "S1#52 source_value '311 distinct' -> '312 distinct' (an integer that is neither the unit nor in a "
                    "fraction)", _m_sub("S1#52", "source_value", "311 distinct", "312 distinct")),
    ("L04", "row", "S4#23 status computed-new -> reproduced, its status_basis quote moved to the 'reproduced' clause of "
                   "the same N3c :151 tag", _m_set("S4#23", status="reproduced", status_basis=dict(
                       locator=f"{_N3C}@09c3a8c:151",
                       quote="which is the stored c1_read_M1M2 auc_kfold (reproduced)"))),
    ("L05", "row", "S5#20 status computed-new -> reproduced, its ledger_row 'L004 (related row: N2 row 37, "
                   "computed-new)' cut to 'L004' (L004's primary row is reproduced and the locator cites its line)",
     _m_set("S5#20", status="reproduced", ledger_row="L004")),
]


def nr_row_level(D0, D1, texts, ledger, figidx):
    """Round 7: the row checks alone (nr_validate_row, no file-level freeze or hash) on every row a mutation changed;
    rows are validated independently, so this is what a whole run's validation reports for those rows."""
    b0 = {f"{r['span']}#{r['seq']}": r for r in D0["rows"]}
    out, n = [], 0
    for r in D1["rows"]:
        k = f"{r['span']}#{r['seq']}"
        if b0.get(k) != r:
            n += 1
            _, bad, _ = nr_validate_row(json.loads(json.dumps(r)), texts, ledger, figidx)
            out += [(k, c, m) for c, m in bad]
    return out, n


NR_ROW_FAMILIES = ("family F", "family G", "family H")


def nr_round7_families(D, texts, ledger, figidx):
    """Round 7 (r6chk findings 1 and 2): three families, evaluated on the mutated row alone (the row checks, and
    whether the row's status-freeze line changed; for a one-row mutation that is exactly what a whole run's
    validation reports). F: every figure row's status set to each other term, one field (expected caught by the row
    checks themselves). G: every row whose status is computed-new, discrepant, not found or log-only, given a locator
    prefix with a reproduced item-raw figure row and the status 'reproduced' (the first such row, in path and line order, that the
    row checks let through, else the first row). H: the same rows given another ledger row whose item-raw rows are
    all reproduced, and the status 'reproduced' (the first that the row checks let through, else the first). G and H
    are expected caught; the members the row checks let through are caught only by the status freeze (section 12)."""
    figs = [r for r in D["rows"] if r.get("kind") == "figure"]
    out = []

    def ev(r0, m):
        _, bad, _ = nr_validate_row(m, texts, ledger, figidx)
        frozen = nr_freeze_line(m) != nr_freeze_line(r0)
        return bad, frozen

    def rec(mid, fam, what, r0, m, exp_row):
        bad, frozen = ev(r0, m)
        by = (f"row checks [{', '.join(dict.fromkeys(c for c, _ in bad))}]; first: {bad[0][1]}" if bad
              else "status-hash only (the row checks let it through)" if frozen else "NOT CAUGHT")
        out.append(dict(id=mid, origin=fam, what=what, applied=True, caught=bool(bad) or frozen, row_caught=bool(bad),
                        expected=True, expected_row=exp_row, by=by[:300]))
    for r in figs:
        k = f"{r['span']}#{r['seq']}"
        for st in NR_STATUSES:
            if st != r.get("status"):
                m = json.loads(json.dumps(r))
                m["status"] = st
                rec(f"FF:{k}:{st}", "family F", f"{k} status {r.get('status')} -> {st}", r, m, True)
    targets = [r for r in figs if r.get("status") in ("computed-new", "discrepant", "not found", "not run", "log-only")]
    pool = sorted({(p, n) for (p, n), f in figidx.items() if base_status(f["status"]) == "reproduced"})
    lpool = sorted(i for i, L in ledger.items() if L["refs"] and {rr["base_status"] for rr in L["refs"]} == {"reproduced"})
    for r in targets:
        k = f"{r['span']}#{r['seq']}"
        pick = None
        for p, n in pool:
            if not nr_line_carries(r, p, AUDIT, n)[0]:
                continue
            m = json.loads(json.dumps(r))
            m["locator"] = f"{p}@{AUDIT}:{n}; " + (r.get("locator") or "")
            m["status"] = "reproduced"
            if not ev(r, m)[0]:
                pick = (p, n)
                break
        p, n = pick or pool[0]
        m = json.loads(json.dumps(r))
        m["locator"] = f"{p}@{AUDIT}:{n}; " + (r.get("locator") or "")
        m["status"] = "reproduced"
        rec(f"FG:{k}", "family G", f"{k} ({r.get('status')}) locator prefixed with {p.split('note-')[-1]}:{n} (a "
                                   f"reproduced figure row), status -> reproduced", r, m, None)
        pick = None
        for i in lpool:
            m = json.loads(json.dumps(r))
            m["ledger_row"], m["status"] = i, "reproduced"
            if not nr_check_ledger_bind(m, ledger)["result"].startswith("pass"):
                continue
            if not ev(r, m)[0]:
                pick = i
                break
        i = pick or lpool[0]
        m = json.loads(json.dumps(r))
        m["ledger_row"], m["status"] = i, "reproduced"
        rec(f"FH:{k}", "family H", f"{k} ({r.get('status')}) ledger_row -> {i} (reproduced), status -> reproduced", r, m,
            None)
    return out


def nr_self_test(path, raw_bytes, ledger, raws, note_res, watch):
    """Every mutation in NR_MUTATIONS (expected caught), the families (expected caught; a member with nothing to
    mutate is reported as not applicable), NR_LIMIT_MUTATIONS (a 'full' limit expected NOT caught by a whole run; a
    'row' limit expected NOT caught by the row checks and caught by the whole run) and, round 7, families F-H
    (nr_round7_families, evaluated row by row)."""
    out = []
    texts = {f: note_text(REPO / f)[1].split("\n") for f in NOTE_ROUTED}
    figidx = nr_fig_index(raws)
    D0 = json.loads(raw_bytes)
    plan = ([(m, o, w, f, True, None) for m, o, w, f in NR_MUTATIONS]
            + [(m, o, w, f, True, None) for m, o, w, f in nr_family_mutations(json.loads(raw_bytes))]
            + [(m, "limit", w, f, lv == "row", lv) for m, lv, w, f in NR_LIMIT_MUTATIONS])
    for mid, origin, what, fn, expect, lvl in plan:
        D = json.loads(raw_bytes)
        try:
            fn(D)
        except (AssertionError, KeyError) as e:
            out.append(dict(id=mid, origin=origin, what=what, applied=False, caught=None, expected=expect,
                            by=f"not applicable: {e}"))
            continue
        rl, nch = nr_row_level(D0, D, texts, ledger, figidx)
        try:
            res = final_note_rows(path, ledger, raws, note_res, watch, D=D, raw_bytes=raw_bytes,
                                  stop_after_validation=True)
            fl = res["validation"]["failures"]
            checks = list(dict.fromkeys(m.split(":")[0] for x in fl for m in x["failures"]))
            caught, by = ((True, f"validation [{', '.join(checks)}]; first: {fl[0]['row']} {fl[0]['failures'][0]}")
                          if fl else (False, "NOT CAUGHT" + (f" (passing {res['pass_check']['passing']})"
                                                             if "pass_check" in res else "")))
        except SystemExit as e:
            caught, by = True, f"run stops: {e}"
        x = dict(id=mid, origin=origin, what=what, applied=True, caught=caught, expected=expect, by=by[:400],
                 row_caught=(bool(rl) if nch else None),
                 row_by=(f"{rl[0][0]} {rl[0][1]}: {rl[0][2]}"[:300] if rl else None))
        if lvl == "row":
            x["expected_row"] = False
        out.append(x)
    out += nr_round7_families(D0, texts, ledger, figidx)
    return out


# ------------------------------------------------------------------ round 5: the overwrite guard (finding 7)
NR_PROV_PATHS = ("results/raw/2026-10-08_note-N1-claims-ledger.md", "results/raw/2026-10-08_note-N1-claims-ledger.json")
NR_FINAL_PATHS = ("results/raw/2026-10-09_note-N1-claims-ledger-final.md",
                  "results/raw/2026-10-09_note-N1-claims-ledger-final.json")


def nr_output_guard(out, json_out, final_mode):
    """Finding 7: the provisional ledger (committed at 6485da2; README-NOTE.md and the N12 scrub index cite it) is
    never written, in any mode; a provisional run writes only where --out and --json-out say (no default), and never
    over the final ledger either. Paths are compared after resolving symlinks and '..', and by inode where both
    exist. Returns the (out, json_out) to write."""
    def ab(x):
        return REPO / x if not Path(x).is_absolute() else Path(x)
    if final_mode:
        out, json_out = out or NR_FINAL_PATHS[0], json_out or NR_FINAL_PATHS[1]
    elif not out or not json_out:
        raise SystemExit("guard: the provisional round writes nothing by default (its ledger is committed at 6485da2 "
                         "and is never rewritten); give --out and --json-out")
    forbidden = list(NR_PROV_PATHS) + ([] if final_mode else list(NR_FINAL_PATHS))
    for x in (out, json_out):
        for y in forbidden:
            a, b = ab(x), ab(y)
            same = os.path.realpath(a) == os.path.realpath(b)
            if not same and a.exists() and b.exists():
                try:
                    same = os.path.samefile(a, b)
                except OSError:
                    same = False
            if same:
                raise SystemExit(f"guard: refusing to write {x} (it is {y}, which this mode never writes)")
    return out, json_out


NR_GUARD_CASES = [
    ("provisional, no --out/--json-out", None, None, False, "refuse"),
    ("provisional, --out = the provisional ledger", NR_PROV_PATHS[0], "/dev/null/x.json", False, "refuse"),
    ("provisional, --json-out = the provisional JSON via '..'",
     "/dev/null/x.md", "results/raw/../raw/2026-10-08_note-N1-claims-ledger.json", False, "refuse"),
    ("provisional, --out = the final ledger", NR_FINAL_PATHS[0], "/dev/null/x.json", False, "refuse"),
    ("final, --out = the provisional ledger", NR_PROV_PATHS[0], None, True, "refuse"),
    ("final, --json-out = the provisional JSON (absolute)", None, str(REPO / NR_PROV_PATHS[1]), True, "refuse"),
    ("final, defaults", None, None, True, "allow"),
    ("provisional, both outside the repository", "/dev/null/x.md", "/dev/null/x.json", False, "allow"),
]


def nr_guard_self_test():
    res = []
    for what, o, j, fm, want in NR_GUARD_CASES:
        try:
            nr_output_guard(o, j, fm)
            got = "allow"
        except SystemExit:
            got = "refuse"
        res.append(dict(case=what, expected=want, got=got, ok=(got == want)))
    return res


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=None, help="default (with --note-rows only): the final ledger path; the "
                                                "provisional round has no default and never writes the committed "
                                                "provisional ledger")
    ap.add_argument("--json-out", default=None)
    ap.add_argument("--note", action="append", default=[],
                    help="note markdown or F1/F2 SVG to match against the ledger (repeatable)")
    ap.add_argument("--note-rows", default=None,
                    help="N1 final: the verified mapping of every numeral in the note and the SVGs "
                         "(results/raw/2026-10-09_note-N1-note-rows.json); validates it and adds section 9")
    a = ap.parse_args()
    # round 5 (finding 7): the guard runs before anything is computed, in every mode
    a.out, a.json_out = nr_output_guard(a.out, a.json_out, bool(a.note_rows))
    if a.note_rows and not a.note:
        a.note = list(NOTE_ROUTED)

    stamp = subprocess.run(["date", "-u"], capture_output=True, text=True).stdout.strip()
    head = full("HEAD")
    pin_full, audit_full = full(PIN), full(AUDIT)
    script_bytes = Path(__file__).read_bytes()
    block_bytes = show(PIN, BLOCK)
    block_sha = sha256(block_bytes)
    routed_ok = block_sha.startswith(ROUTED_SHA[0]) and block_sha.endswith(ROUTED_SHA[1])
    if not routed_ok:
        raise SystemExit(f"block sha256 {block_sha} does not match the routed {ROUTED_SHA}")
    lines = block_bytes.decode("utf-8").split("\n")
    audit_is_desc = subprocess.run(["git", "-C", str(REPO), "merge-base", "--is-ancestor", PIN, AUDIT]).returncode == 0

    # 1. tokens
    toks = extract_block_tokens(lines)
    ctoks = classify_tokens(lines, toks)
    unassigned = [t for t in ctoks if t["class"] == "UNASSIGNED"]

    # 2. item raws
    raws = ItemRaws()
    wt_equal = {}
    for p, s in raws.sha.items():
        f = REPO / p
        wt_equal[p] = (sha256(f.read_bytes()) == s) if f.exists() else None

    # 3. rows
    rows = []
    for r in ROWS:
        row = dict(id=r["id"], line=r["line"], figure=r["span"], note=r.get("note"), _span=r["_span"])
        row["tokens"] = [t for t in ctoks if t["class"] == "row" and t["detail"] == r["id"]]
        row["refs"] = [raws.resolve(x) for x in r["refs"]]
        row["related"] = [raws.resolve(x) for x in r.get("related", [])]
        for rr in row["refs"] + row["related"]:
            ps = parse_sources(rr.get("source"))
            hints = [os.path.dirname(x["path"]) for x in ps if "/" in x["path"] and x["path"].startswith("data/")]
            hints += ITEM_DIRS.get(rr.get("item") or "", [])
            rr["sources"] = [classify_source(x, hints) for x in ps]
            rr["unparsed_source_names"] = unparsed_names(rr.get("source"), ps)
            rr["base_status"] = base_status(rr.get("status"))
        rows.append(row)

    # entry commits per row
    for row in rows:
        rec, aud = [], []
        for rr in row["refs"]:
            for s in rr["sources"]:
                for e in s.get("entries", []):
                    if s["kind"] == "audit raw":
                        # an audit raw cited by a not-found row records the figure's absence (the preflight's
                        # MISSING lines), not its entry
                        if rr["base_status"] != "not found":
                            aud.append(e["commit"])
                    elif e.get("commit"):
                        rec.append(e["commit"])
            # a figure whose only source is an audit raw (computed-new, or a mixed status with a computed-new part)
            # entered the record with the audit raws. A 'not found' figure entered no record and no audit raw: it
            # contributes only the record lines its item raw names as carriers (if any), never the audit commit.
            if rr["base_status"] == "computed-new" or (rr["base_status"] == "mixed" and "computed-new" in (rr["status"] or "")):
                if rr.get("item") and rr["item"] in RAWS:
                    aud.append(last_change(RAWS[rr["item"]][0], AUDIT))
        row["entry_record"] = latest(rec)
        row["entry_with_audit"] = latest(rec + aud)
        row["audit_sources"] = sorted({c for c in aud if c})

    # secondary: pinned locators cited in the primary rows' NOTE text (carriers, wording checks), not sources.
    # Round 3: each locator is one carrier, entering at its latest line's commit; a row's carriers are
    # alternatives, and a fact enters the record with its first carrier, so the row counts at the earliest.
    for row in rows:
        cs = []
        locs = []
        carriers = []
        for rr in row["refs"]:
            for x in parse_sources(rr.get("note")):
                if not x.get("rev"):
                    continue
                c = classify_source(x)
                if c["kind"] in ("artifact", "line locator"):
                    lc = [e["commit"] for e in c["entries"] if e.get("commit")]
                    cs += lc
                    locs.append(c["raw"])
                    if lc and c["raw"] not in [y["locator"] for y in carriers]:
                        carriers.append(dict(locator=c["raw"], commit=latest(lc)))
        row["note_locators"] = locs
        row["note_carriers"] = carriers
        row["entry_note_locators"] = latest(cs)
        row["entry_note_first_carrier"] = earliest([y["commit"] for y in carriers])
    spot = blame_cross_check()

    # 4. pass check
    prim = [(row, rr) for row in rows for rr in row["refs"]]
    by_status = {}
    for row, rr in prim:
        by_status.setdefault(rr["base_status"] or "none", []).append((row, rr))
    not_found = by_status.get("not found", [])
    discrepant = by_status.get("discrepant", [])
    other = [(row, rr) for row, rr in prim if rr["base_status"] in (None, "other", "not run")
             or (rr["base_status"] is None)]
    passing_rows = [row for row in rows if all(rr["base_status"] in ("reproduced", "log-only") for rr in row["refs"])]
    loc_ok = [row for row in passing_rows if all(rr["base_status"] != "log-only" or any(
        s["kind"] == "line locator" for s in rr["sources"]) for rr in row["refs"])]

    disc_rows = []
    for row, rr in discrepant:
        if row["figure"] not in DISC:
            raise SystemExit(f"discrepant row {row['id']} ({row['figure']!r}) has no DISC entry")
        cat, quote = DISC[row["figure"]]
        if quote not in (rr["status"] or "") + " " + (rr["note"] or ""):
            raise SystemExit(f"DISC quote not in the item raw's status/note for {row['id']}: {quote!r}")
        disc_rows.append(dict(row=row["id"], figure=row["figure"], item_row=rr["locator"], status=rr["status"],
                              status_condition=rr.get("status_condition"),
                              note=rr["note"], classification_quoted=quote, branch=cat, branch_text=DISC_PATH[cat],
                              reproduced_value=rr["printed"]))
    n4h = raws.find_md_line("N4", "- None under the block's on-fail rule", startswith=True)
    if len(n4h) != 1 or "is a note in the raw, not an (i) discrepancy" not in raws.md["N4"][n4h[0] - 1]:
        raise SystemExit("N4 STOPs line not found")
    disc_path = {k: v.format(n4_stops=raws.md_locator("N4", n4h[0])) for k, v in DISC_PATH.items()}
    for x in disc_rows:
        x["branch_text"] = disc_path[x["branch"]]

    # conditions on 'not found' rows (NF_COND), each asserted against its item-raw line
    nf_rows = []
    for row, rr in not_found:
        c = NF_COND.get(row["id"])
        ctext = None
        if c:
            h = raws.find_md_line(c["item"], c["needle"], startswith=True)
            if len(h) != 1 or c["quote"] not in raws.md[c["item"]][h[0] - 1]:
                raise SystemExit(f"NF_COND for {row['id']}: needle or quote not found")
            alt = raws.resolve(F(*c["alt"]))["locator"] + f", status {raws.resolve(F(*c['alt']))['status']}" if c.get("alt") else ""
            ctext = c["text"].format(loc=raws.md_locator(c["item"], h[0]), alt=alt)
        nf_rows.append(dict(row=row["id"], figure=row["figure"], item_row=rr["locator"], status=rr["status"],
                            note=rr["note"], condition=ctext))
    missing_cond = [x["row"] for x in nf_rows if not x["condition"]]
    if missing_cond:
        raise SystemExit(f"not-found rows without a stated condition: {missing_cond}")

    span2id = {}
    for row in rows:
        span2id.setdefault(row["figure"], []).append(row["id"])
    stops = []
    for x in STOPS:
        hits = raws.find_md_line(x["item"], x["needle"], startswith=True)
        if len(hits) != 1:
            raise SystemExit(f"STOP needle not unique: {x['needle']!r}: {hits}")
        ids = []
        for sp in x["rows_spans"]:
            if sp not in span2id:
                raise SystemExit(f"STOP rows_span not a ledger figure: {sp!r}")
            ids += span2id[sp]
        stops.append(dict(item=x["item"], kind=x["kind"], locator=raws.md_locator(x["item"], hits[0]),
                          rows=ids, what=x["what"]))

    # round 3 (4f): the same figure in two item raws -- each primary row against each related row from another
    # item raw that carries a status in the vocabulary (the ROWS map attaches such a related row only when it
    # addresses the same figure)
    # CROSS_WHY's 'block :44 is part (i-b) of N3' is asserted against the block: :44 opens with '(i-b)' and the
    # nearest item header above it is N3's
    hdr44 = [n for n in range(1, 44) if lines[n - 1].startswith("### ")]
    if not lines[43].startswith("(i-b)") or not lines[hdr44[-1] - 1].startswith("### N3."):
        raise SystemExit("block :44 is not N3's part (i-b)")
    cross = []
    for row in rows:
        for rr in row["refs"]:
            if not rr.get("item") or rr["base_status"] not in STATUS_VOCAB:
                continue
            for rel in row["related"]:
                if not rel.get("item") or rel["item"] == rr["item"] or rel["base_status"] not in STATUS_VOCAB:
                    continue
                rel_kind = ("same status" if rel["status"] == rr["status"] else
                            "same base status, qualifier differs" if rel["base_status"] == rr["base_status"] else
                            "STATUSES DIFFER")
                why = None
                w = CROSS_WHY.get((rr["item"], rel["item"]))
                if w and rel_kind == "STATUSES DIFFER":
                    locs = []
                    for it, nd, q in w["lines"]:
                        h = raws.find_md_line(it, nd, startswith=True)
                        if len(h) != 1 or q not in raws.md[it][h[0] - 1]:
                            raise SystemExit(f"CROSS_WHY {it}: needle or quote not found: {nd!r}")
                        locs.append(raws.md_locator(it, h[0]))
                    why = w["text"].format(*locs)
                if rel_kind == "STATUSES DIFFER" and not why:
                    raise SystemExit(f"{row['id']}: statuses differ across {rr['item']}/{rel['item']} with no CROSS_WHY")
                cross.append(dict(row=row["id"], figure=row["figure"], primary_item=rr["item"],
                                  primary_locator=rr["locator"], primary_status=rr["status"],
                                  other_item=rel["item"], other_locator=rel["locator"], other_status=rel["status"],
                                  relation=rel_kind, why_primary=why))

    # round 3 (4g): wording, scope and precision corrections routed to note sentences (WORDING), asserted
    pass_ids = {row["id"] for row in passing_rows}
    row_ids = {row["id"] for row in rows}
    wording = []
    for k, x in enumerate(WORDING, start=1):
        if x.get("fig") or x.get("fid"):
            r_ = raws.resolve(F(x["item"], x["fig"]) if x.get("fig") else (x["item"], "id", x["fid"]))
            n, hay = r_["md_line"], raws.md[x["item"]][r_["md_line"] - 1] + " " + (r_.get("note") or "")
            loc = r_["locator"]
        else:
            h = raws.find_md_line(x["item"], x["needle"], startswith=True)
            if len(h) != 1:
                raise SystemExit(f"WORDING {x['item']}: needle not unique: {x['needle']!r}: {h}")
            n, hay = h[0], raws.md[x["item"]][h[0] - 1]
            loc = raws.md_locator(x["item"], n)
        for q in x["quotes"]:
            if q not in hay:
                raise SystemExit(f"WORDING {x['item']} :{n}: quote not present: {q!r}")
        bad = [r for r in x["rows"] if r not in row_ids]
        if bad:
            raise SystemExit(f"WORDING {x['item']}: unknown rows {bad}")
        wording.append(dict(id=f"C{k}", item=x["item"], locator=loc, quotes=x["quotes"], what=x["what"],
                            rows=[dict(row=r, passes=(r in pass_ids)) for r in x["rows"]]))

    # 5. tag candidate
    rec_all = [row["entry_record"] for row in rows if row["entry_record"]]
    aud_all = [row["entry_with_audit"] for row in rows if row["entry_with_audit"]]
    cand_rec = latest(rec_all)
    cand_aud = latest(aud_all)
    which_rec = [row["id"] for row in rows if row["entry_record"] == cand_rec]
    which_aud = [row["id"] for row in rows if row["entry_with_audit"] == cand_aud]
    cand_rec_pass = latest([row["entry_record"] for row in passing_rows if row["entry_record"]])
    # the round-2 form (latest carrier over all rows), kept for comparison only
    cand_note = latest([row["entry_note_locators"] for row in rows if row["entry_note_locators"]])
    which_note = [row["id"] for row in rows if row["entry_note_locators"] == cand_note]
    note_locs_at_cand = sorted({l for row in rows if row["entry_note_locators"] == cand_note for l in row["note_locators"]})
    # round 3: each row at its first carrier; over rows, the latest
    cand_first = latest([row["entry_note_first_carrier"] for row in rows if row["entry_note_first_carrier"]])
    which_first = [row["id"] for row in rows if row["entry_note_first_carrier"] == cand_first]

    def carrier_list(row):
        return [dict(locator=y["locator"], commit=y["commit"], date=cdate(y["commit"])) for y in
                sorted(row["note_carriers"], key=lambda y: -topo_index(y["commit"]))]
    first_newer = [dict(row=row["id"], figure=row["figure"], first=row["entry_note_first_carrier"],
                        first_date=cdate(row["entry_note_first_carrier"]), carriers=carrier_list(row))
                   for row in rows if row["entry_note_first_carrier"] and cand_rec
                   and newer(row["entry_note_first_carrier"], cand_rec)]
    only_later_newer = [dict(row=row["id"], figure=row["figure"], first=row["entry_note_first_carrier"],
                             first_date=cdate(row["entry_note_first_carrier"]), carriers=carrier_list(row))
                        for row in rows if row["entry_note_locators"] and cand_rec
                        and newer(row["entry_note_locators"], cand_rec)
                        and not newer(row["entry_note_first_carrier"], cand_rec)]
    # block :98's request for the CORR dose caveat, and N5's answer (both asserted), for the conditional on the
    # record-only candidate
    b98 = "State whether the CORR contrast's dose carries any caveat the note should disclose"
    if b98 not in lines[97]:
        raise SystemExit("block :98 request not found")
    n5a = raws.find_md_line("N5", "**Yes -- there is a known artifact at the 0.12 dose", startswith=True)
    if len(n5a) != 1 or "the note should disclose it" not in raws.md["N5"][n5a[0] - 1]:
        raise SystemExit("N5 section 7d answer not found")
    caveat = dict(block_line=98, block_quote=b98, n5_answer_locator=raws.md_locator("N5", n5a[0]),
                  n5_answer_quote="the note should disclose it")
    no_entry = [dict(row=row["id"], statuses=sorted({rr["base_status"] or "none" for rr in row["refs"]}))
                for row in rows if not row["entry_with_audit"]]

    # out-of-record sources named by the primary rows (section 8 note 5, computed)
    oor = {}
    for row in rows:
        for rr in row["refs"]:
            for x in rr["sources"]:
                if x["kind"].startswith("outside the record"):
                    oor.setdefault((x["raw"], x["kind"]), []).append(row["id"])
    out_of_record = [dict(source=k[0], kind=k[1], rows=sorted(set(v))) for k, v in oor.items()]

    # numeral-free spans without rows (section 1b), asserted present in the block
    norow = []
    for ln, sp, why, by in sorted(NUMFREE_NOROW, key=lambda x: x[0]):
        if sp not in lines[ln - 1]:
            raise SystemExit(f"NUMFREE_NOROW span not at block :{ln}: {sp!r}")
        if any(t["line"] == ln and lines[ln - 1].find(sp) <= t["start"] < lines[ln - 1].find(sp) + len(sp) for t in ctoks):
            raise SystemExit(f"NUMFREE_NOROW span carries a numeral token: {sp!r}")
        norow.append(dict(line=ln, span=sp, reason=why, answered_by=by))

    # item-raw figure rows that no ledger row references (completeness; --note offers them as candidates)
    used = set()
    for row in rows:
        for rr in row["refs"] + row["related"]:
            if rr.get("json_index") is not None:
                used.add((rr["item"], rr["json_index"]))
    unref = {}
    for item in raws.js:
        for i, f in enumerate(raws.figures(item)):
            if (item, i) not in used:
                unref.setdefault(item, []).append(dict(index=i, figure=f.get("figure"), status=f.get("status")))

    # watch-list (WATCH), each line and quote asserted against its item raw
    watch = []
    for w in WATCH:
        h = raws.find_md_line(w["item"], w["needle"], startswith=True)
        if len(h) != 1:
            raise SystemExit(f"WATCH {w['id']}: needle not unique: {h}")
        l = raws.md[w["item"]][h[0] - 1]
        for q in w["quotes"]:
            if q not in l:
                raise SystemExit(f"WATCH {w['id']}: quote {q!r} not in {raws.md_locator(w['item'], h[0])}")
        watch.append(dict(w, locator=raws.md_locator(w["item"], h[0])))

    # 6. auxiliary
    aux = []
    for x in AUX:
        hits = raws.find_md_line(x["item"], x["needle"])
        if not hits:
            raise SystemExit(f"aux needle not found: {x}")
        if len(hits) != 1:
            raise SystemExit(f"aux needle not unique: {x['needle']!r}: {hits}")
        n = hits[0]
        k = x.get("n", 1)
        loc = raws.md_locator(x["item"], n) + (f"-{n + k - 1}" if k > 1 else "")
        aux.append(dict(line=x["line"], text=x["text"], kind=x["kind"], item=x["item"],
                        locator=loc, item_line=" // ".join(raws.md[x["item"]][n - 1:n - 1 + k])))

    # 7. note mode
    note_res = note_mode(a.note, rows, lines, raws, watch) if a.note else None

    # 9. N1 final: the note's own rows
    final = None
    if a.note_rows:
        led_ = {row["id"]: row for row in rows}
        # round 5: validation failures are reported before any later assertion (the self-test reads them the same way)
        final = final_note_rows(a.note_rows, led_, raws, note_res, watch, stop_after_validation=True)
        fl = final["validation"]["failures"]
        # round 5 (finding 2): the mutation self-test, in memory, and the guard's own cases
        rb = (REPO / a.note_rows if not Path(a.note_rows).is_absolute() else Path(a.note_rows)).read_bytes()
        st_ = nr_self_test(a.note_rows, rb, led_, raws, note_res, watch) if not fl else []
        gt_ = nr_guard_self_test()
        final["self_test"] = dict(mutations=st_, guard=gt_)
        # round 7: a member that declares what the row checks alone must do (family F: catch; a 'row' limit: not
        # catch) is held to it as well
        miss_ = ([x["id"] for x in st_ if x["applied"] and x["caught"] is not x["expected"]]
                 + [x["id"] for x in st_ if x["applied"] and x.get("expected_row") is not None
                    and x["row_caught"] is not x["expected_row"]]
                 + [x["id"] for x in st_ if not x["applied"] and not x["origin"].startswith("family")]
                 + [x["case"] for x in gt_ if not x["ok"]])
        for x in st_:
            if x["origin"] in NR_ROW_FAMILIES:
                continue
            print(f"SELF-TEST {x['id']} ({x['origin']}): "
                  f"{'not applicable' if not x['applied'] else 'caught' if x['caught'] else 'NOT CAUGHT'}"
                  f"{'' if x['expected'] else ' (a known limit: expected not caught)'}"
                  f"{'' if not x.get('applied') or x.get('row_caught') is None else ' [row checks: ' + ('caught' if x['row_caught'] else 'not caught') + ']'}"
                  f" -- {x['what']}")
        for fam in NR_ROW_FAMILIES:
            xs = [x for x in st_ if x["origin"] == fam]
            print(f"SELF-TEST {fam}: {len(xs)} members; caught {sum(1 for x in xs if x['caught'])}; by the row checks "
                  f"{sum(1 for x in xs if x['row_caught'])}; only by the status freeze "
                  f"{sum(1 for x in xs if x['caught'] and not x['row_caught'])}")
        if miss_:
            raise SystemExit(f"self-test: {len(miss_)} mutation(s) or guard case(s) not caught: {miss_}; nothing written")
        for x in final["validation"]["explained"]:
            print(f"EXPLAINED {x['row']} {x['file']}:{x['line']} {x['unit']!r} [{x['status']}]: "
                  + " | ".join(x["failures"]))
        for x in fl:
            print(f"VALIDATION FAILURE {x['row']} {x['file']}:{x['line']} {x['unit']!r} [{x['status']}]: "
                  + " | ".join(x["failures"]))
        if fl:
            raise SystemExit(f"{len(fl)} note row(s) failed validation that no named exemption explains; nothing written")

    # ------------------------------------------------------------- outputs
    counts = {}
    for t in ctoks:
        k = t["class"] if t["class"] != "row" else ("row (identifier inside a row span)" if t.get("inside_row_but_identifier") else "row (note-figure numeral)")
        counts[k] = counts.get(k, 0) + 1
    cat_counts = {}
    for t in ctoks:
        if t["class"].startswith("excluded"):
            cat_counts[t["detail"]] = cat_counts.get(t["detail"], 0) + 1
    digit_toks = [t for t in ctoks if t["text"][0].isdigit() or t["text"][0] == "."]
    word_toks = [t for t in ctoks if t["text"][0].isalpha()]

    # round 3: names in the primary rows' source text that the parser left unresolved (section 3's completeness)
    unparsed, unres_alt = {}, {}
    for row in rows:
        for rr in row["refs"]:
            for nm in rr.get("unparsed_source_names", []):
                unparsed.setdefault(nm, []).append(row["id"])
            for s in rr["sources"]:
                if s.get("unresolved_alternatives"):
                    unres_alt.setdefault(s["raw"], []).append(row["id"])

    preflight_note = ("results/raw/2026-10-08_note-preflight.md@" + PIN + ":15 (RESEARCH-NOTE-v0_2-draft.md MISSING), "
                      ":17-18 (F1/F2 SVGs MISSING), :16 (FIGURE-REVIEW MISSING), :20 (PREPRINT-v1_1-draft.md MISSING)")
    note_present = (REPO / NOTE_DEFAULT).exists()

    J = dict(
        item="N1", title="claims ledger", provisional=final is None,
        final_for=(dict(note=FINAL_NOTE, note_sha256=[f for f in final["files"] if f["path"] == FINAL_NOTE][0]["sha256"],
                        svgs=[dict(path=f["path"], sha256=f["sha256"]) for f in final["files"] if f["path"] != FINAL_NOTE],
                        rows_file=final["rows_file"], rows_file_sha256=final["rows_file_sha256"])
                   if final else None),
        provisional_basis=("built from the block's quotations of the note (block lines 21-133), because "
                           "RESEARCH-NOTE-v0_2-draft.md and the F1/F2 SVGs are not on this machine; to be re-run with "
                           "--note against the note and the SVGs when the PI places them"),
        code_stamp_utc=stamp, head_at_run=head, record_pin=pin_full, audit_pin=audit_full,
        audit_pin_descends_from_record_pin=audit_is_desc,
        block=BLOCK, block_sha256=block_sha, block_routed_match=routed_ok, block_n1_lines=list(N1_LINES),
        script="scripts/audit_note_N1.py", script_sha256=sha256(script_bytes),
        interpreter=sys.executable, python=platform.python_version(),
        command=" ".join(shlex.quote(x) for x in [sys.executable] + sys.argv),
        note_present_at_root=note_present, note_args=a.note,
        item_raws={p: dict(sha256_at_audit_pin=s, working_tree_equal=wt_equal[p]) for p, s in raws.sha.items()},
        extraction=dict(
            rule=("block lines 21-133 read at the record pin; a numeral token is a maximal digit run with internal "
                  "'.' or ',' groups (regex \\d+(?:[.,]\\d+)*|\\.\\d+) or a number word (zero..twelve, half; case-"
                  "insensitive, word-bounded). Each token is classified in this order: inside a hand-mapped ledger "
                  "row's span -> that row; inside a hand-declared exclusion span -> its category; else a generic rule "
                  "(backticks, date, hash, arXiv/figure locator, file name or path, section sign, digits attached to a "
                  "name, link/card/tier/stage/level/item/version prefix, one-/two-sided); else UNASSIGNED."),
            n_tokens=len(ctoks), n_digit_tokens=len(digit_toks), n_word_tokens=len(word_toks),
            counts=counts, exclusion_categories=cat_counts, unassigned=unassigned,
            n_rows=len(rows), n_hand_exclusions=len(EXCLUDE),
            numeral_free_rule=("a numeral-free span gets a row when the block lists it among the figures to be reproduced "
                               "for the note: an entry of an item's figure list, a qualifier or definition attached to "
                               "quoted figures, an N3(ii)-(v) result, or a figure label; requests for an account, a "
                               "method, a provenance or a table get none (examples in numeral_free_no_row: Code's read "
                               "of block lines 21-133, not an exhaustive enumeration)"),
            numeral_free_no_row=norow,
            item_raw_rows_unreferenced={k: v for k, v in unref.items()},
            n_item_raw_rows_unreferenced=sum(len(v) for v in unref.values())),
        tokens=ctoks,
        rows=rows,
        blame_cross_check=spot,
        pass_check=dict(
            n_rows=len(rows), n_primary_refs=len(prim),
            status_counts={k: len(v) for k, v in by_status.items()},
            rows_all_reproduced_or_log_only=[row["id"] for row in passing_rows],
            rows_passing_with_line_locator_for_every_log_only=[row["id"] for row in loc_ok],
            not_found=nf_rows,
            discrepant=disc_rows,
            other=[dict(row=row["id"], figure=row["figure"], item_row=rr["locator"], status=rr["status"])
                   for row, rr in prim if rr["base_status"] not in STATUS_VOCAB],
            computed_new=[dict(row=row["id"], figure=row["figure"], item_row=rr["locator"], status=rr["status"])
                          for row, rr in by_status.get("computed-new", [])],
            stops_touching_rows=stops,
            same_figure_two_item_raws=cross,
            wording_scope_precision_corrections=wording),
        tag_commit_candidate=dict(
            record_sources_only=dict(commit=cand_rec, date=cdate(cand_rec) if cand_rec else None, rows=which_rec),
            including_audit_raw_sources=dict(commit=cand_aud, date=cdate(cand_aud) if cand_aud else None, rows=which_aud),
            record_sources_only_passing_rows=dict(commit=cand_rec_pass, date=cdate(cand_rec_pass) if cand_rec_pass else None),
            rows_with_no_entry=no_entry,
            item_raw_note_locators=dict(
                rule=("each pinned locator in a primary row's note text is treated as one carrier of the row's figure "
                      "(a few are record checks of the figure rather than carriers of it; every row's carriers are in "
                      "the JSON, rows[].note_carriers), entering at its latest line's blamed commit (artifact: last change at "
                      "or before the pin); a row's carriers are alternatives and a fact enters the record with its "
                      "first carrier, so the row counts at the earliest; over rows, the latest"),
                commit=cand_first, date=cdate(cand_first) if cand_first else None, rows=which_first,
                rows_first_carrier_newer_than_record_candidate=first_newer,
                rows_only_a_later_carrier_newer_than_record_candidate=only_later_newer,
                corr_dose_caveat=caveat,
                round2_latest_carrier_form=dict(commit=cand_note, date=cdate(cand_note) if cand_note else None,
                                                rows=which_note, locators_in_those_rows=note_locs_at_cand))),
        source_names_unresolved=dict(primary_rows=unparsed, slash_alternatives_unresolved=unres_alt),
        auxiliary=aux,
        out_of_record_sources=out_of_record,
        watch_list=[dict(id=w["id"], item=w["item"], locator=w["locator"], quotes=w["quotes"],
                         keys=[list(k) for k in w["keys"]], what=w["what"]) for w in watch],
        note_mode=note_res,
        preflight_locators=preflight_note,
        note_rows_final=final,
    )

    md = render(J, rows, ctoks, lines, raws)
    outp = REPO / a.out if not Path(a.out).is_absolute() else Path(a.out)
    jp = REPO / a.json_out if not Path(a.json_out).is_absolute() else Path(a.json_out)
    for p in (outp, jp):
        if p.is_symlink():
            raise SystemExit(f"refusing to write through a symlink: {p}")
    outp.write_text(md, encoding="utf-8")
    jp.write_text(json.dumps(J, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print(f"tokens {len(ctoks)} (digit {len(digit_toks)}, word {len(word_toks)}); rows {len(rows)}; "
          f"unassigned {len(unassigned)}")
    print("status counts (primary refs):", {k: len(v) for k, v in by_status.items()})
    print("tag candidate, record only:", short(cand_rec), which_rec)
    print("tag candidate, incl. audit raws:", short(cand_aud), len(which_aud), "rows")
    if final:
        P9, T9 = final["pass_check"], final["tag"]
        st5 = final.get("self_test") or {}
        print(f"N1 final: {final['n_rows']} note rows ({final['n_figures']} figures); unexplained validation failures "
              f"{len(final['validation']['failures'])}, rows with a failure a named exemption explains "
              f"{len(final['validation']['explained'])}; self-test: as expected "
              f"{sum(1 for x in st5.get('mutations', []) if x['applied'] and x['caught'] is x['expected'])}/"
              f"{sum(1 for x in st5.get('mutations', []) if x['applied'])} (known limits uncaught "
              f"{sum(1 for x in st5.get('mutations', []) if x['origin'] == 'limit' and x['caught'] is False)}), guard cases "
              f"{sum(1 for x in st5.get('guard', []) if x['ok'])}/{len(st5.get('guard', []))}")
        print("N1 final pass check:", P9["by_status"])
        print("N1 final tag: record only", short(T9["record_sources_only"]["commit"]), "| incl. audit raws",
              short(T9["including_audit_raws"]["commit"]))
    if unassigned:
        for t in unassigned:
            print("UNASSIGNED", t["line"], t["text"], lines[t["line"] - 1][max(0, t["start"] - 30):t["end"] + 30])
        raise SystemExit(2)


# ------------------------------------------------------------------ rendering
def cell(x, limit=None):
    if x is None:
        return ""
    s = re.sub(r"(?<!\\)\|", r"\\|", str(x).replace("\n", " "))
    if limit and len(s) > limit:
        s = s[:limit] + " [...]"
    return s


def src_entries(rr):
    parts = []
    for s in rr.get("sources", []):
        if s["kind"] in ("artifact",):
            for e in s["entries"]:
                parts.append(f"{e['path']}: last {short(e['commit'])}" +
                             (f", first-add {short(e.get('first_add'))}" if e.get("first_add") else "") +
                             (f" (cited at {s['rev']})" if s.get("rev") and s["rev"] != PIN else ""))
        elif s["kind"] == "line locator":
            cs = sorted({e["commit"] for e in s["entries"] if e["commit"]}, key=lambda c: topo_index(c))
            parts.append(f"{s['resolved'][0]}@{s['rev']}:{','.join(str(e['line']) for e in s['entries'])}: blame "
                         + "/".join(short(c) for c in cs))
        elif s["kind"] == "audit raw":
            parts.append(f"{s['resolved'][0]}: {short(s['entries'][0]['commit'])} (audit raw)")
        else:
            parts.append(f"{s['raw']}: {s['kind']}")
    return "; ".join(parts)


def render(J, rows, ctoks, lines, raws):
    o = []
    w = o.append
    FN = J.get("note_rows_final")
    if FN:
        fs = J["final_for"]
        w(f"# AUDIT-note-release v1.2 -- N1: claims ledger (FINAL for {fs['note']} sha256 {fs['note_sha256'][:8]}...)")
        w("")
        w(f"**FINAL** for `{fs['note']}` (sha256 `{fs['note_sha256']}`) and its two SVGs ("
          + "; ".join(f"`{x['path']}` sha256 `{x['sha256']}`" for x in fs["svgs"]) + "), all three hashed at this run "
          "and equal to the routed values. It supersedes, for this note, the provisional ledger "
          "(results/raw/2026-10-08_note-N1-claims-ledger.md@6485da2), which stays as committed because README-NOTE.md "
          "and the N12 scrub index cite it. Sections 1-8 are the provisional round's block-quotation ledger, re-run "
          "here by the same code at the same pins (record bbc9ffe, item raws 09c3a8c); section 7 is now a summary of "
          "the matcher over the three files, and section 8's notes 1 and 6 are updated. **Section 9 is new: one row "
          "for every numeral unit in the note and both SVGs**, read from the verified mapping "
          f"`{fs['rows_file']}` (sha256 `{fs['rows_file_sha256']}`) and validated mechanically at this run. "
          "'FINAL' means the mapping is complete for this note sha; it does not mean the block's pass condition is "
          "met (section 9d says it is not) or that the open items in 9h are settled. Section 10 is the values check "
          "of round 5 (the final checker's findings and the PI's N19 routing, with the mutation self-test); sections "
          "11 and 12 are rounds 6 and 7 (the adversarial check of round 5 and the strict check of round 6). 10f, what "
          "the validator still does not catch, is current at this run.")
        w("")
    else:
        w("# AUDIT-note-release v1.2 -- N1: claims ledger (PROVISIONAL)")
        w("")
        w("**PROVISIONAL.** " + J["provisional_basis"][0].upper() + J["provisional_basis"][1:] + ". Missing referents: " + J["preflight_locators"] + ".")
        w("")
    w(f"- Code stamp: {J['code_stamp_utc']} (date -u)")
    w(f"- HEAD at run (informational): {J['head_at_run']}")
    w(f"- Record pin: {PIN} = {J['record_pin']} (every record read and every record locator below)")
    w(f"- Audit-raw pin: {AUDIT} = {J['audit_pin']} (every item raw read with git show {AUDIT}:<path>; "
      f"descends from the record pin: {J['audit_pin_descends_from_record_pin']})")
    w(f"- Block: `{BLOCK}`@{PIN} sha256 `{J['block_sha256']}` (routed 8cd8a9ac...3841: "
      f"{'MATCH' if J['block_routed_match'] else 'MISMATCH'}); item N1 = block lines {N1_LINES[0]}-{N1_LINES[1]}")
    w(f"- Script: `{J['script']}` sha256 `{J['script_sha256']}`")
    w(f"- Interpreter: {J['interpreter']} (Python {J['python']}); stdlib only; no model, no network")
    w(f"- Command: `{J['command']}`")
    if FN:
        w(f"- Note at root on this run: {NOTE_DEFAULT} (the block's referent) absent; its successor {FINAL_NOTE} and "
          f"both SVGs present (untracked); --note arguments: {J['note_args']}")
    else:
        w(f"- Note at root on this run: {'present' if J['note_present_at_root'] else 'absent'}; --note arguments: "
          f"{J['note_args'] or 'none'}")
    w("- Item raws (read at the audit pin; working tree equal to the pinned blob):")
    for p, d in J["item_raws"].items():
        w(f"  - `{p}` sha256 `{d['sha256_at_audit_pin'][:16]}` working tree equal: {d['working_tree_equal']}")
    moved = [p for p, d in J["item_raws"].items() if d["working_tree_equal"] is False]
    if moved:
        w("  - Working tree not equal: " + ", ".join(f"`{p}`" for p in moved) + ". Each was regenerated in a later audit "
          "commit (" + ", ".join(sorted({short(last_change(p, 'HEAD')) for p in moved})) + ", its last change at HEAD); "
          "every read here is at the audit pin, so the flag records only that the working tree moved on.")
    w("")
    w("Status vocabulary (block :22, plus the item raws' computed-new): reproduced | log-only | not found | discrepant | "
      "computed-new; 'not run' for N19. Every status below is the item raw's, carried verbatim with its cause; this "
      "ledger reclassifies nothing. Where an item raw gives no status in that vocabulary, the row says so.")
    if FN:
        w("")
        w("Section 9 (N1 final): every row's status is its item raw's (or its ledger row's), carried exactly, and the "
          "validator checks each against what the item raw gives (9a; round 5). There are no exceptions of N1's own "
          "since round 5 (finding 1): the five rows that carried N1's own classification (S1#26, S1#27, S1#34, S1#140, "
          "S4#19) now carry their item raws' statuses, and what N1 reads in their sentences is recorded separately as a "
          "wording or precision correction (9i), as S8 does at :208. One row maps a status its item raw does not give "
          "in N1's vocabulary: S1#59 (N13's own vocabulary; its validation_note names the check it explains), which the "
          "pass check reads as its ledger row's, outside the vocabulary (9a, 9d). Where an item raw itself classifies a "
          "discrepancy (N2vi row 8 for W3, N5's L102 for W8, N3's transcription rows), the row carries that.")
    w("")
    # ---------------------------------------------------------------- 1
    E = J["extraction"]
    w("## 1. Extraction: every numeral the block quotes (block lines 21-133)")
    w("")
    w("Rule. " + E["rule"])
    w("")
    w(f"Count: **{E['n_tokens']} numeral tokens** in block lines 21-133 ({E['n_digit_tokens']} digit tokens, "
      f"{E['n_word_tokens']} number words). Classified:")
    w("")
    w("| class | tokens |")
    w("|---|---|")
    for k, v in sorted(E["counts"].items()):
        w(f"| {k} | {v} |")
    w("")
    w(f"Ledger rows: {E['n_rows']} (hand-mapped, each a span of one block line). Hand exclusion spans: "
      f"{E['n_hand_exclusions']}. Unassigned: **{len(E['unassigned'])}**.")
    w("")
    w("Numeral-free rows. Every numeral token above is assigned by the rule. A span without a numeral gets a row by "
      "this rule: " + E["numeral_free_rule"] + ". Examples with rows: 'zero pauses' (L101), 'the three conjuncts' (L108), "
      "'the leakage gate's bound' (L146), F1's link-5 y-axis label (L081), and, added in round 2 after the values "
      "check, 'the random-direction comparison' (L162, :43), N3(v)'s random-direction control (L163, :48), the "
      "definition of Δ (L164, :57), 'the falsifier' (L165, :104) and 'the purity–potency figures' (L166, :107). "
      "Rows L001-L161 keep their round-1 ids; L162-L166 sit in block-line order among them.")
    w("")
    w("Exclusion categories (not note figures):")
    w("")
    w("| category | tokens |")
    w("|---|---|")
    for k, v in sorted(E["exclusion_categories"].items(), key=lambda x: -x[1]):
        w(f"| {k} | {v} |")
    w("")
    w("Every token with its line, offset and class is in the JSON (`tokens`). 'Identifier inside a row span' counts "
      "digits that sit inside a row's span but are names (L60, random-1, F1, link-5, Horn-1); they belong to the row's "
      "wording, not its value, and --note matching ignores them. A decimal after 'word-' is a quantity, not a name "
      "(round 2: 'sub-0.05-cosine' in L161 counts as a figure).")
    w("")
    w("### 1b. Numeral-free spans the block names that get no row (examples)")
    w("")
    w("Each span is asserted present in its block line and free of numeral tokens. The list gives examples from "
      "Code's read of block lines 21-133; it is not an exhaustive enumeration. The integration check of round 2 found "
      "five spans of the same class that the round-2 list omitted (:32, :35, :57, :68, :98); round 3 adds them, with "
      "three more found on Code's re-read (:60, :125, :130). The other requests in the N11-N13 procedures (smoke "
      "test, scrub, provenance table; :68, :75-:93) are not enumerated.")
    w("")
    w("| block | span | why no row | item-raw rows that answer it |")
    w("|---|---|---|---|")
    for x in E["numeral_free_no_row"]:
        w(f"| :{x['line']} | {cell(x['span'])} | {cell(x['reason'])} | {cell(x['answered_by'])} |")
    w("")
    w("### 1c. Item-raw figure rows that no ledger row references")
    w("")
    ur = E["item_raw_rows_unreferenced"]
    w(f"{E['n_item_raw_rows_unreferenced']} figure rows in the item-raw JSONs are referenced by no ledger row (primary "
      "or related): " + "; ".join(f"{k} {len(v)}" for k, v in ur.items()) + ". They are the item raws' own checks "
      "beyond the block's quotations (context figures, record-prose checks, the N16 decoding table, the N14 "
      "map-level breakdowns). The --note re-run offers any of them as an item-raw candidate when a note numeral "
      "carries its value; the full list (index, figure, status) is in the JSON (`extraction.item_raw_rows_unreferenced`).")
    w("")
    # ---------------------------------------------------------------- 2
    w("## 2. The ledger")
    w("")
    w("One row per figure as the block quotes it. 'item raw row' is the item raw's own line at the audit pin. "
      "'printed', 'source' and 'status' are the item raw's, verbatim (long values are cut at 400 characters here; "
      "the JSON carries them whole). 'entry (record)' = the latest commit, over the row's record sources, at which a "
      "source entered the record (artifact: last change at or before the pin; line locator: the blamed commit); "
      "'entry (+audit)' adds the audit raw (results/raw/2026-10-08_note-*) where the figure's only source is an "
      "audit raw (computed-new; source-only). A '(cont.)' line is a second primary item-raw row for the same figure; "
      "a '(see)' line carries N1's note on the row, the primary item-raw row's own note where the status cell does not "
      "already carry it (round 3; cut at 700 characters, whole in the JSON), and related item-raw rows, each with its "
      "own status (shown, not used in the pass check).")
    w("")
    cur = None
    for row in rows:
        items = sorted({rr["item"] or "-" for rr in row["refs"]})
        grp = items[0]
        if grp != cur:
            if cur is not None:
                w("")
            cur = grp
            w(f"### {grp}")
            w("")
            w("| row | block | figure as the block writes it | item raw row | printed (item raw) | source (item raw) | "
              "status (item raw) | source entry commits | entry (record) | entry (+audit) |")
            w("|---|---|---|---|---|---|---|---|---|---|")
        for k, rr in enumerate(row["refs"]):
            first = (k == 0)
            st = rr["status"]
            if rr.get("status_condition"):
                st = f"{st} -- CONDITIONAL (item raw): {rr['status_condition']}"
            if rr["base_status"] in ("discrepant", "not found"):
                st = f"{st} -- cause (item raw): {rr['note']}"
            w("| " + " | ".join([
                row["id"] if first else f"{row['id']} (cont.)",
                f":{row['line']}" if first else "",
                cell(row["figure"]) if first else "",
                cell(rr["locator"]),
                cell(rr["printed"], 400),
                cell(rr["source"], 400),
                cell(st, 900 if rr["base_status"] in ("discrepant", "not found") else 400),
                cell(src_entries(rr), 600),
                short(row["entry_record"]) if first else "",
                short(row["entry_with_audit"]) if first else "",
            ]) + " |")
        extra = []
        if row.get("note"):
            extra.append(f"note: {row['note']}")
        # round 3: the primary item-raw row's own note, on every row where the status cell does not already carry
        # it (discrepant and not-found rows carry it as the cause); cut here at 700 characters, whole in the JSON
        for k, rr in enumerate(row["refs"]):
            if rr["kind"] in ("fig", "id", "mdrow", "txtrow") and rr.get("note") and \
                    rr["base_status"] not in ("discrepant", "not found"):
                lab_ = f"item-raw note ({rr['item']}" + (f", primary row {k + 1}" if len(row["refs"]) > 1 else "") + ")"
                extra.append(f"{lab_}: {cell(rr['note'], 700)}")
        for rr in row["related"]:
            extra.append(f"related: {rr['locator']} -- {rr['figure']} -- {rr['status']}"
                         + (f" -- CONDITIONAL (item raw): {rr['status_condition']}" if rr.get("status_condition") else "")
                         + (f" -- {rr['note']}" if rr["base_status"] in ("discrepant", "not found") else ""))
        if extra:
            # rendered as a one-column continuation row so the table stays one table
            w("| " + row["id"] + " (see) | | " + cell(" // ".join(extra), 3200) + " | | | | | | | |")
    w("")
    # ---------------------------------------------------------------- 3
    w("## 3. Source entry commits (every distinct source the ledger's primary item-raw rows name)")
    w("")
    seen = {}
    st_by_src = {}
    for row in rows:
        for rr in row["refs"]:
            for s in rr["sources"]:
                key = (s["raw"], s["kind"])
                seen.setdefault(key, (s, []))[1].append(row["id"])
                st_by_src.setdefault(key, set()).add(rr["base_status"])
    w("| source as the item raw writes it | kind | resolved path(s) | commit(s) (last change at or before the pin / "
      "first add; or blamed line commits) | committer date of the latest | rows |")
    w("|---|---|---|---|---|---|")
    for (raw, kind), (s, rids) in seen.items():
        ents = s.get("entries", [])
        cs = [e["commit"] for e in ents if e.get("commit")]
        lt = latest(cs) if cs else None
        if kind == "artifact":
            cc = "; ".join(f"{short(e['commit'])}" + (f" / {short(e.get('first_add'))}" if e.get("first_add") else "")
                           for e in ents)
        elif kind == "line locator":
            cc = "; ".join(f":{e['line']} {short(e['commit'])}"
                           + (f" (-C: {short(e['commit_copy_detected'])})" if e.get("commit_copy_detected") else "")
                           for e in ents)
        else:
            cc = "; ".join(short(c) for c in cs)
        if kind == "audit raw" and st_by_src[(raw, kind)] == {"not found"}:
            kind = "audit raw (cited by not-found rows only: it records the note's absence; not counted as an entry, section 5)"
        if s.get("slash_alternatives"):
            kind += " (slash-abbreviated alternatives: " + ", ".join(s["slash_alternatives"]) + ")"
            if s.get("unresolved_alternatives"):
                kind += "; UNRESOLVED: " + ", ".join(s["unresolved_alternatives"])
        w(f"| {cell(raw, 200)} | {kind} | {cell(', '.join(s.get('resolved', [])), 300)} | {cc} | "
          f"{cdate(lt) if lt else ''} | {', '.join(sorted(set(rids)))} |")
    w("")
    U = J["source_names_unresolved"]
    w("Completeness (round 3). Source names are parsed from each primary item-raw row's source text: pinned "
      "locators, data/results/scripts/valence_core/archive paths, bare artifact names (internal dots allowed, e.g. "
      "e0_axes.meta.json, resolved against the tree at the pin, first under the directories the same text names, "
      "then the item's data directories), slash-abbreviated alternatives (d2/d3_scores.json = d2_scores.json and "
      "d3_scores.json, when the literal is not itself the tail of a tracked path), root documents and the suite's "
      "module name. A scan for every file-like name (.json, .jsonl, .npz, .md, .py, .txt, .sh, .ipynb) in the same "
      "texts that no parsed source covers finds: "
      + ("; ".join(f"`{k}` (rows {', '.join(sorted(set(v)))})" for k, v in U["primary_rows"].items()) or "none")
      + ". Slash-abbreviated alternatives with an unresolved member: "
      + ("; ".join(f"`{k}` (rows {', '.join(sorted(set(v)))})" for k, v in U["slash_alternatives_unresolved"].items())
         or "none") + ".")
    w("")
    spot = J["blame_cross_check"]
    w(f"Blame: every line locator's entry commit is `git blame -L n,n --porcelain <rev> -- <file>`, run per line "
      f"({len(spot)} distinct (file, rev, line) entries over the primary and related rows' sources and the note "
      f"locators); each is cross-checked against one full-file `git blame --porcelain` of its file: "
      f"{sum(1 for x in spot if x['equal'])}/{len(spot)} equal.")
    w("")
    # ---------------------------------------------------------------- 4
    P = J["pass_check"]
    w("## 4. The block's pass check (block :23)")
    w("")
    if FN:
        w("*N1 final:* 4a-4g are the provisional round's pass check over the block's quotations, kept as built. Where "
          "they say the note is not on this machine or defer to the --note run, section 9 is that run: 9d is the pass "
          "check over the note's own figures, 9e the watch-list per conditional STOP, and 9f the span notes that read "
          "the 4g corrections against the note's sentences.")
        w("")
    w("*Pass:* every figure is `reproduced` or `log-only` with a locator. *On fail:* a `not found` figure is cut from "
      "the note; a `discrepant` figure is corrected in the note to the reproduced value if the discrepancy is "
      "transcription, and is a STOP on that item if it is not. (AUDIT-note-release-v1_2.md@bbc9ffe:23)")
    w("")
    w(f"Over the {P['n_rows']} provisional rows ({P['n_primary_refs']} primary item-raw rows; a row with two primary "
      f"rows passes only if both do): primary-row statuses {json.dumps(P['status_counts'], ensure_ascii=False)}.")
    w("")
    w(f"- Rows whose every primary row is reproduced or log-only: {len(P['rows_all_reproduced_or_log_only'])} of "
      f"{P['n_rows']}; {len(P['rows_passing_with_line_locator_for_every_log_only'])} of them give a pinned line locator "
      f"for every log-only primary row.")
    nl = [r for r in P["rows_all_reproduced_or_log_only"] if r not in P["rows_passing_with_line_locator_for_every_log_only"]]
    if nl:
        w(f"- Passing rows with a log-only primary row whose source text names no line locator the parser resolved: "
          f"{', '.join(nl)} (see their source cells).")
    wp = sorted({x["row"] for c in P["wording_scope_precision_corrections"] for x in c["rows"] if x["passes"]},
                key=lambda r: [row["id"] for row in rows].index(r))
    w(f"- Passing rows that an item raw ties to a wording, scope or precision correction (4g): {len(wp)} "
      f"({', '.join(wp) or 'none'}). The figure passes; the note's sentence that carries it still needs a human read "
      "against 4g at the --note run, because a correction without a new numeral is invisible to the --note matcher.")
    w("- **The pass condition is not met over the provisional set**: the rows below are not found, discrepant, "
      "computed-new, not run, or carry a status outside the vocabulary. Each consequence is the block's (:23), "
      "applied to the item raw's own classification; Code does not re-decide any of them. Whether a row binds "
      "depends on whether the note carries the figure, which this run cannot read.")
    w("")
    w("### 4a. not found (block :23: cut from the note -- each row binds only under the condition stated)")
    w("")
    w("Every not-found row here is conditional: the cut applies to the note, and the note is not on this machine. The "
      "'condition' column says whose condition it is (the item raw's, or Code's reading of block :23) and quotes or "
      "cites the item-raw line it rests on.")
    w("")
    w("| row | figure (block) | item raw row | status and cause (item raw) | condition |")
    w("|---|---|---|---|---|")
    for x in P["not_found"]:
        w(f"| {x['row']} | {cell(x['figure'])} | {cell(x['item_row'])} | {cell(x['status'])} -- {cell(x['note'], 900)} | "
          f"{cell(x['condition'], 900)} |")
    w("")
    w("### 4b. discrepant (block :23: corrected if transcription; a STOP on the item if not)")
    w("")
    w("'classification' quotes the item raw's own words (asserted to occur in its status or note). 'branch' is the "
      "branch of block :23 that classification reads into: T = the item raw calls it transcription; NT = the item raw "
      "says it is not transcription; NF = the item raw classes it as a design-seat claim or a figure label, not a "
      "record figure; SR = stale referent. The branch texts follow the table. The cause column is the item raw's note.")
    w("")
    w("| row | figure (block) | item raw row | status (item raw) | classification (item raw, quoted) | branch | reproduced value (item raw) | cause (item raw) |")
    w("|---|---|---|---|---|---|---|---|")
    for x in P["discrepant"]:
        stc = x["status"] + (f" -- CONDITIONAL (item raw): {x['status_condition']}" if x.get("status_condition") else "")
        w(f"| {x['row']} | {cell(x['figure'])} | {cell(x['item_row'])} | {cell(stc)} | "
          f"{cell(x['classification_quoted'])} | {x['branch']}{' (conditional)' if x.get('status_condition') else ''} | "
          f"{cell(x['reproduced_value'], 300)} | {cell(x['note'], 1500)} |")
    w("")
    bt = {}
    for x in P["discrepant"]:
        bt.setdefault(x["branch"], x["branch_text"])
    for k in DISC_PATH:
        n = sum(1 for x in P["discrepant"] if x["branch"] == k)
        if k in bt:
            w(f"- **{k}** ({n} row{'' if n == 1 else 's'}): {bt[k]}.")
    cond = [x["row"] for x in P["discrepant"] if x.get("status_condition")]
    if cond:
        w(f"- **Conditional** ({', '.join(cond)}): the item raw makes the status itself conditional on what the note or "
          "figure shows (its status_condition, carried verbatim in the status cell); the T branch applies only on the "
          "discrepant side of that condition.")
    cd = [x for x in P["same_figure_two_item_raws"] if x["relation"] == "STATUSES DIFFER"]
    if cd:
        w(f"- **Two item raws, two statuses** ({', '.join(x['row'] for x in cd)}; table 4f): "
          + "; ".join(f"{x['row']}: {x['primary_item']} gives '{x['primary_status']}' ({x['primary_locator']}), "
                      f"{x['other_item']} gives '{x['other_status']}' ({x['other_locator']})" for x in cd)
          + ". " + " ".join(y[0].upper() + y[1:] + "." for y in dict.fromkeys(x["why_primary"] for x in cd)))
    w("")
    w("### 4c. computed-new (no record line states the figure; its only source is an audit raw)")
    w("")
    w("| row | figure (block) | item raw row | status (item raw) |")
    w("|---|---|---|---|")
    for x in P["computed_new"]:
        w(f"| {x['row']} | {cell(x['figure'])} | {cell(x['item_row'])} | {cell(x['status'])} |")
    w("")
    w("### 4d. not run, mixed, or a status outside N1's vocabulary")
    w("")
    w("| row | figure (block) | item raw row | status as the item raw gives it |")
    w("|---|---|---|---|")
    for x in P["other"]:
        w(f"| {x['row']} | {cell(x['figure'])} | {cell(x['item_row'])} | {cell(x['status'], 600)} |")
    w("")
    w("### 4e. STOPs and conditional STOPs the item raws declare that touch these figures")
    w("")
    w("| item | kind | item raw line | ledger rows | what (Code's summary of the item raw's line) |")
    w("|---|---|---|---|---|")
    for x in P["stops_touching_rows"]:
        w(f"| {x['item']} | {x['kind']} | {cell(x['locator'])} | {', '.join(x['rows']) or '(none)'} | {cell(x['what'])} |")
    w("")
    w("The commit 09c3a8c message also records N12(i)'s literal-grep STOP on the release; it concerns history, not a "
      "figure, and touches no ledger row.")
    w("")
    w("### 4f. The same figure in two item raws (round 3)")
    w("")
    w("Every pair of a primary item-raw row and a related row from another item raw that the ledger attaches to the "
      "same figure, with both statuses verbatim. 'STATUSES DIFFER' means the base status differs; the pass check reads "
      "the primary row only, and N1 does not choose between the two.")
    w("")
    w("| row | figure (block) | primary item raw row | status | other item raw row | status | relation |")
    w("|---|---|---|---|---|---|---|")
    for x in P["same_figure_two_item_raws"]:
        w(f"| {x['row']} | {cell(x['figure'])} | {cell(x['primary_locator'])} | {cell(x['primary_status'])} | "
          f"{cell(x['other_locator'])} | {cell(x['other_status'])} | {x['relation']} |")
    w("")
    w("### 4g. Wording, scope and precision corrections the item raws route to note sentences (round 3)")
    w("")
    w("These carry no new numeral, or only a bare small integer, so the --note matcher (section 7) cannot surface "
      "them; a human reads each against the note at the --note run. Each quote is asserted to occur in the item-raw "
      "line cited (or that row's JSON note). 'rows' are the ledger rows the item raw ties it to, with 'pass' where "
      "the row passes the check above; an entry with no row touches a sentence the block quotes no figure for. "
      "Collected from Code's read of the item raws' notes sections and primary-row notes; not asserted exhaustive "
      "(the item raws' own notes sections are the full source). Two numeric corrections of the same kind are on the "
      "watch-list instead (W9, W10).")
    w("")
    w("| id | item raw line | rows | quoted (item raw) | what (Code's summary) |")
    w("|---|---|---|---|---|")
    for x in P["wording_scope_precision_corrections"]:
        rr_ = ", ".join(f"{y['row']}{' (pass)' if y['passes'] else ''}" for y in x["rows"]) or "(none)"
        w(f"| {x['id']} | {cell(x['locator'])} | {rr_} | {cell(' / '.join(x['quotes']))} | {cell(x['what'])} |")
    w("")
    # ---------------------------------------------------------------- 5
    T = J["tag_commit_candidate"]
    w("## 5. The commit at which the last of the note's figures entered the record (the tag-commit candidate)")
    w("")
    if FN:
        w("*N1 final:* this section is the provisional computation over the block's quotations, kept as built; 9g "
          "computes the tag commit over the note's own figures and states it.")
        w("")
    r1, r2 = T["record_sources_only"], T["including_audit_raw_sources"]
    rn = T["item_raw_note_locators"]
    cv = rn["corr_dose_caveat"]
    fn = rn["rows_first_carrier_newer_than_record_candidate"]
    w(f"- **Over record sources only** (artifacts at their last change at or before the pin; line locators at their "
      f"blamed commit; the block itself and the audit raws excluded): `{r1['commit']}` ({r1['date']}), set by rows "
      f"{', '.join(r1['rows'])}."
      + (f" **Conditional** (round 3): block :{cv['block_line']} asks N5 to '{cv['block_quote']}', and N5 answers "
         f"that '{cv['n5_answer_quote']}' ({cv['n5_answer_locator']}). The note will therefore probably carry the "
         f"caveat; if it carries it as a record statement, the third branch below applies and this candidate does not "
         f"hold." if any(x["row"] == "L105" for x in fn) else ""))
    rp = T["record_sources_only_passing_rows"]
    w(f"  - The same over the rows that pass (every primary row reproduced or log-only): `{rp['commit']}` ({rp['date']}).")
    w(f"- **Including audit-raw sources** (results/raw/2026-10-08_note-*, for rows whose figure entered the record only "
      f"with an audit raw: computed-new, or a mixed status with a computed-new part): `{r2['commit']}` ({r2['date']}), "
      f"set by {len(r2['rows'])} rows ({', '.join(r2['rows'])}).")
    ne = T["rows_with_no_entry"]
    w(f"- **No entry** ({len(ne)} rows): " + ("; ".join(f"{x['row']} ({'/'.join(x['statuses'])})" for x in ne) or "none")
      + ". These rows set no entry commit: no primary item-raw row names a record source for them (only the block "
      "itself, sources outside the record, or nothing), and none is computed-new. A not-found figure entered neither "
      "the record nor an audit raw: the preflight raw that L071 and L074 cite records the note's absence, not the "
      "figure's entry, and is not counted. A not-found row whose item raw names record lines that carry the figure "
      "(L032) keeps those lines' commits.")
    gloss = {"L105": "the G-CAL 0.12 caveat", "L099": "the 93% delivery rate"}

    def gl(x):
        return gloss.get(x["row"], "'" + x["figure"] + "'")

    def carriers_txt(x):
        cs = x["carriers"]
        first = [c for c in cs if c["commit"] == x["first"]]
        later = [c for c in cs if c["commit"] != x["first"]]
        t = "first carrier " + "; ".join(f"{c['locator']} at `{short(c['commit'])}` ({c['date']})" for c in first)
        if later:
            t += "; later carrier(s) " + "; ".join(f"{c['locator']} at `{short(c['commit'])}` ({c['date']})" for c in later)
        return t
    w(f"- For comparison (not a source): the pinned record locators the primary item-raw rows cite in their *note* "
      f"text are other carriers of the row's figure, or record-wording checks. Rule (round 3): {rn['rule']}. Result: "
      f"`{rn['commit']}` ({rn['date']}), set by rows {', '.join(rn['rows'])}. A tag on an earlier commit would not "
      f"hold that carrier.")
    if fn:
        w("- **Third branch.** Rows whose first carrier is later than the record-only candidate: "
          + " ".join(f"{x['row']} ({gl(x)}): {carriers_txt(x)}." for x in fn)
          + " If the note carries " + " or ".join(gl(x) for x in fn) + " as a record statement, the record-only "
          f"candidate is `{short(rn['commit'])}`, not `{short(r1['commit'])}`; a later carrier sets it only if the note "
          "cites that carrier itself"
          + "".join(f" ({x['row']}: `{short(c['commit'])}` if the note cites {c['locator']}"
                    + (" (G-PORT C1)" if c["locator"] == "RESULTS.md@bbc9ffe:161-165" else "") + ")" for x in fn
                    for c in x["carriers"] if c["commit"] != x["first"] and newer(c["commit"], x["first"]))
          + "."
          + "".join(f" N5's note on L105 names both carriers after 'first on record at'; by blame the earlier is "
                    f"{', '.join(c['locator'] for c in x['carriers'] if c['commit'] == x['first'])}."
                    for x in fn if x["row"] == "L105" and any(
                        "first on record at" in (rr.get("note") or "") for row in rows if row["id"] == "L105"
                        for rr in row["refs"])))
    ol = rn["rows_only_a_later_carrier_newer_than_record_candidate"]
    if ol:
        w("- Rows with a carrier later than the record-only candidate whose first carrier is earlier (they do not move "
          "it): " + " ".join(f"{x['row']} ({gl(x)}): {carriers_txt(x)}." for x in ol)
          + f" The round-2 form of this line took each row's latest carrier, which named "
          f"`{short(rn['round2_latest_carrier_form']['commit'])}` for rows "
          f"{', '.join(rn['round2_latest_carrier_form']['rows'])}; it is kept in the JSON for comparison "
          "(`round2_latest_carrier_form`).")
    w("- Which applies depends on whether the note carries the audit's computed-new figures (the d' and Fisher p "
      "arithmetic for F2, the MDEs, the nonlinear-probe and 1,000-draw results of N3c, N3's random-mask medians, the exploration-share and "
      "certification readings): if it does, the figures entered the record only with the audit raws, and the first "
      "statement does not cover them. The tag name, and whether the tag sits on the candidate or on the README/raws "
      "commit above it (block :14), are the PI's.")
    w("- Line locators throughout the item raws and this ledger are pinned to bbc9ffe. RESULTS.md is newest-first, "
      "so at a commit earlier than bbc9ffe the same text sits at other line numbers; a tag placed on an earlier "
      "candidate would need the locators re-pinned to it (or cited @bbc9ffe).")
    w("")
    # ---------------------------------------------------------------- 6
    w("## 6. Auxiliary: block items that are not note figures but that an item raw checked")
    w("")
    w("| block | as the block writes it | kind | item raw line | the item raw's line |")
    w("|---|---|---|---|---|")
    for x in J["auxiliary"]:
        w(f"| :{x['line']} | {cell(x['text'])} | {x['kind']} | {cell(x['locator'])} | {cell(x['item_line'], 400)} |")
    w("")
    # ---------------------------------------------------------------- 7
    w("## 7. --note mode")
    w("")
    w("Matching rule (round 2; the round-1 matcher compared values only and is replaced). Every numeral in each file "
      "(SVG: the text content of text, tspan, title and desc elements) is split into units: a fraction k/n is one "
      "unit; otherwise each numeral, with its sign (+, -, ±, or none; a dash after a letter, digit or bracket is a "
      "range or a hyphen, not a sign), its unit kind (percent; percentage points, written 'pp' or 'points'; a "
      "multiplier attached as '×' or 'x'; else a plain number) and its decimal places. A ledger row's units are those "
      "of its span; a numeral-free row takes the units of its primary item-raw rows' figure labels. A note unit is "
      "**matched** only if a row unit has the same unit kind, the same value, a compatible sign (none = +; zero is "
      "neutral) and the same integer/decimal form, AND the row's context words (its span and its item-raw figure "
      "labels) agree with the words of the note unit's own clause (round 3: bounded by ';', a table bar, a bullet or a "
      "sentence end) within 60 characters of the unit: one agreeing word that occurs in fewer "
      f"than {COMMON_DF} rows' contexts, or two agreeing words of any kind (a lone stage, arm or map name such as "
      "'SFT' or 'DPO' is not enough); the agreeing words are printed. A value hit without such agreement is a "
      "**candidate (verify context)**, printed with the row's span and status. When more than one row carries the "
      "value, a match is labelled **matched; value shared by N rows (verify which)** and every other row with the "
      "value is listed as a candidate (round 3). "
      "A unit with no such value hit is **not in ledger**; it lists loose hits (the same digits or proportion with a "
      "different unit kind, sign or integer/decimal form: 0.3% against −0.3 or 0.003), rounding hits (half-up, two "
      "or more places) and item-raw figure rows carrying the value, as pointers only. Bare integers below 100 are "
      "'weak' and never matched. Units caught by the generic rules (dates, hashes, paths, identifiers, section signs) "
      "are listed as excluded. 'Matched' is a pointer for the reader, not a verification: the context test is a "
      "word overlap.")
    w("")
    w("Limits. An SVG's plotted positions (point coordinates, bar heights) are geometry, not text, and are not read: "
      "F2's plotted (FPR, TPR) points must be checked against their data file (results/raw/2026-10-08_note-N2-roc.json "
      "for ours; N2vi for the source's) by a human or by the Draftsman seat's own export.")
    w("")
    w("Watch-list. Every unit whose value is one of these is surfaced in its own table, whatever it matches (sign "
      "ignored; a decimal key with stated places matches only that many places). Each entry's quotes are asserted "
      "to occur in the item-raw line cited.")
    w("")
    w("| id | item raw line | values (as the item raw writes them) | keys | what it ties to |")
    w("|---|---|---|---|---|")
    for x in J["watch_list"]:
        w(f"| {x['id']} | {cell(x['locator'])} | {cell(' / '.join(x['quotes']))} | "
          f"{cell('; '.join(':'.join(str(v) for v in k) for k in x['keys']))} | {cell(x['what'])} |")
    w("")
    if FN and J["note_mode"]:
        w("The matcher ran over the three files at this run. Its per-unit table (every unit with its kind, sign, "
          "context and match) is in the JSON (`note_mode[].numerals`) and is not repeated here: section 9 replaces it "
          "with the verified mapping. Counts and the watch-list hits:")
        w("")
        w("| file | sha256 | units | matched | shared value | candidate | not in ledger | weak | excluded | watch-list hits |")
        w("|---|---|---|---|---|---|---|---|---|---|")
        for res in J["note_mode"]:
            nn = res["numerals"]
            w(f"| `{res['path']}` | `{res['sha256'][:16]}` | {len(nn)} | "
              f"{sum(1 for x in nn if x.get('match') == 'matched')} | "
              f"{sum(1 for x in nn if str(x.get('match', '')).startswith('matched; value shared'))} | "
              f"{sum(1 for x in nn if x.get('match') == 'candidate (verify context)')} | "
              f"{sum(1 for x in nn if x.get('match') == 'not in ledger')} | "
              f"{sum(1 for x in nn if str(x.get('match', '')).startswith(('weak', 'not in ledger (small')))} | "
              f"{sum(1 for x in nn if 'excluded' in x)} | {len(res['watch_hits'])} |")
        w("")
        w("| file | line | unit | kind | context | watch | what |")
        w("|---|---|---|---|---|---|---|")
        for res in J["note_mode"]:
            for x in res["watch_hits"]:
                w(f"| `{res['path']}` | {x['line']} | {cell(x['text'])} | {x['kind']}"
                  f"{' (excluded: ' + x['excluded'] + ')' if x.get('excluded') else ''} | {cell(x['context'])} | "
                  f"{x['watch']} | {cell(x['what'], 300)} |")
        w("")
        w("What each hit is (carried, corrected, or a value collision) is in 9e.")
        w("")
    elif J["note_mode"] is None:
        w("Not run: no --note given. RESEARCH-NOTE-v0_2-draft.md and the F1/F2 SVGs are not on this machine "
          f"({J['preflight_locators']}). When the PI places them, re-run with `--note RESEARCH-NOTE-v0_2-draft.md "
          "--note <F1.svg> --note <F2.svg>`. The numerals needing a human read are then the candidates, the shared-"
          "value matches, the 'not in ledger' units and the watch-list hits; the sentences needing one are those 4g "
          "lists, which the matcher cannot find.")
        w("")
    else:
        for res in J["note_mode"]:
            nn = res["numerals"]
            k_m = sum(1 for x in nn if x.get("match") == "matched")
            k_ms = sum(1 for x in nn if str(x.get("match", "")).startswith("matched; value shared"))
            k_c = sum(1 for x in nn if x.get("match") == "candidate (verify context)")
            k_n = sum(1 for x in nn if x.get("match") == "not in ledger")
            k_w = sum(1 for x in nn if str(x.get("match", "")).startswith(("weak", "not in ledger (small")))
            k_e = sum(1 for x in nn if "excluded" in x)
            w(f"### `{res['path']}` (sha256 `{res['sha256']}`, {res['n_lines']} lines)")
            w("")
            w(f"units {len(nn)}; matched {k_m}; **matched but the value is shared by several rows {k_ms}; "
              f"candidate (verify context) {k_c}; not in ledger {k_n}**; bare "
              f"integers below 100 (weak) {k_w}; excluded by a generic rule {k_e}; **watch-list hits {len(res['watch_hits'])}**")
            w("")
            w("| line | unit | kind | sign | context | match |")
            w("|---|---|---|---|---|---|")
            for x in nn:
                m = x.get("match") or ("excluded: " + x.get("excluded", ""))
                parts = [m]
                if x.get("matched_rows"):
                    parts.append("matched: " + "; ".join(x["matched_rows"]))
                if x.get("candidate_rows"):
                    parts.append("candidates: " + "; ".join(x["candidate_rows"]))
                if x.get("weak"):
                    parts.append("rows with the same integer: " + "; ".join(x["weak"]))
                if x.get("loose_rows"):
                    parts.append("loose (other unit kind, sign or form): " + "; ".join(x["loose_rows"]))
                if x.get("rounds_to"):
                    parts.append("rounds to: " + "; ".join(x["rounds_to"]))
                if x.get("item_raw_candidates"):
                    parts.append("item-raw rows with the value: " + "; ".join(x["item_raw_candidates"]))
                w(f"| {x['line']} | {cell(x['text'])} | {x['kind']} | {x.get('sign', '')} | {cell(x['context'])} | "
                  f"{cell(' -- '.join(parts), 900)} |")
            w("")
            w(f"Watch-list hits in `{res['path']}`:")
            w("")
            if res["watch_hits"]:
                w("| line | unit | kind | context | watch | item raw line | what |")
                w("|---|---|---|---|---|---|---|")
                for x in res["watch_hits"]:
                    w(f"| {x['line']} | {cell(x['text'])} | {x['kind']}{' (excluded: ' + x['excluded'] + ')' if x.get('excluded') else ''} | "
                      f"{cell(x['context'])} | {x['watch']} | {cell(x['locator'])} | {cell(x['what'])} |")
            else:
                w("none.")
            w("")
    # ---------------------------------------------------------------- 8
    w("## 8. Notes for the PI and the design seat (none is a STOP declared by N1)")
    w("")
    if FN:
        w("1. Basis (updated at N1 final). Sections 1-8 are built from the block's quotations of the note; the note the "
          "block names (v0.2) was superseded by v0.3, which section 9 maps unit by unit. A block-quoted figure the note "
          "no longer carries stays in sections 2-5 as a row of the block's ledger; it binds nothing in the note. Section "
          "9 is the ledger of the note itself.")
    else:
        w("1. Provisional basis. The block's referent for N1 is the note and the SVGs (AUDIT-note-release-v1_2.md@bbc9ffe:21); "
          "neither is here. The rows are the block's quotations of them. A figure the note carries that the block does not "
          "quote is absent from this ledger until the --note re-run; a quoted figure the note no longer carries can be "
          "dropped then.")
    w("2. Rows whose item raw gives no status in N1's vocabulary are listed in 4d with the item raw's own wording: "
      "N13 row 15 (the Q1 bet's date) uses N13's vocabulary (block :93); the N3 CV-scheme row is stated 'as stored' "
      "without a status row; the block's 'sub-0.05-cosine' wording has no N17 figure row of its own (N17's note F3 "
      "addresses it). N1 does not assign them a status.")
    w("3. Discrepant rows carry the item raws' classifications. Some item raws state that a discrepancy is a "
      "pass-condition outcome rather than a note figure and that block :23 does not attach (N2 rows 21 and 33, for "
      "(ii) and (iv)), or that it is a design-seat claim or a figure label, a note under block :3 rather than an (i) "
      "discrepancy under :62 (N4); others give a conditional (N2vi section 12; N3 ib-1's status_condition). Those "
      "statements are the item raws' and are shown in the status and cause columns. Where this ledger states what "
      "block :23 does with them (the NF and SR branch texts, the 4a conditions), it says it is Code's reading.")
    w("4. Record-source entry commits use `git log -1 <pin> -- <path>` for artifacts (the last change at or before the "
      "pin, which may be later than the commit that first wrote the figure if the file changed afterwards) and the "
      "blamed commit for line locators; first-add commits are listed beside artifacts in section 3.")
    oo = J["out_of_record_sources"]
    w("5. Sources outside the record enter no entry commit; rows resting on them show it in section 3. Over the "
      "primary rows (computed from the parsed sources): "
      + ("; ".join(f"{x['source']} ({x['kind']}; rows {', '.join(x['rows'])})" for x in oo) or "none") + ".")
    if FN:
        w("6. N19 (the 0.394 and the 0.70): " + n19_text(FN) + " Section 9 maps the note's N19 figures to that raw "
          "(round 5, the PI's routing 10; 9h O9). Sections 2-5 keep the provisional rows L159/L160 as built ('not run' "
          "at 6485da2).")
    else:
        w("6. N19 rows (0.394, 0.70) are 'not run': cloning the external repository waits on the PI (preflight raw, note 9). "
          "Under block :125 the note's numbers are cut if N19 is not run by T.")
    l105 = [x for x in fn if x["row"] == "L105"]
    l099 = [x for x in ol if x["row"] == "L099"]
    w("7. The G-CAL 0.12 row (L105, the CORR dose caveat) is reproduced by N5 from f1-era artifacts, but N5's note says "
      "the finding is 'first on record at' results/raw/2026-10-04_m-v1.7_referent_check.txt@bbc9ffe:5196-5207 and "
      "RESULTS.md@bbc9ffe:161-165 (G-PORT C1). "
      + ("By blame they enter at " + " and ".join(f"`{short(c['commit'])}` ({c['locator']})" for c in l105[0]["carriers"])
         + f"; a fact enters the record with its first carrier, so section 5's third branch is `{short(l105[0]['first'])}`, "
           "and the later carrier binds only if the note cites it. Block :98 asks whether the CORR dose carries a "
           "caveat the note should disclose, and N5 says it should; section 5 therefore states the record-only "
           "candidate as conditional on the note not carrying the caveat as a record statement." if l105 else
         "Section 5 counts those carriers.")
      + (f" The 93% delivery rate (L099) is on record from its first carrier at `{short(l099[0]['first'])}` "
         f"({l099[0]['first_date']}), before the record-only candidate; its later carrier does not move it (round 2 "
         "counted it at its latest carrier)." if l099 else ""))
    w("8. Archive line locators: `git blame` (the command the ledger uses) attributes a line of archive/RESULTS-cycle1-2.md "
      "or archive/RESULTS-cycles3-4.md to the commit that created the archive file, because those files were made by "
      "copying the log. Section 3 prints, for information, the copy-detecting attribution (`git blame -C`) beside it: "
      "e.g. N10's R² line (archive/RESULTS-cycle1-2.md@bbc9ffe:1788) is c54c4e0 by plain blame and fd7dc3d with -C, the "
      "entry commit the N10 raw names. Both precede every candidate in section 5, so neither changes it.")
    r89 = [row for row in rows if row["id"] == "L089"][0]["refs"][0]
    l89 = [e["line"] for s in r89["sources"] if s["kind"] == "line locator" for e in s["entries"]]
    c89 = sorted({e["commit"] for s in r89["sources"] if s["kind"] == "line locator" for e in s["entries"]})
    w("9. L089 (the Q1 bet's date): N13's row 15 has no source column. Its source cell is N1's construction from N13's "
      f"referent note: the bet's own text, cited at the record pin (PROPOSAL-g at {PIN}, lines "
      f"{', '.join(str(n) for n in l89)}); N13's note cites the same lines at 72b09a9 (lines 32, 33, 56), the text's "
      "first commit, before a status-line amendment shifted them by one (round 3: the source cell now uses the record "
      f"pin, as every other record locator here does). Its entry is the blamed commit of those lines, "
      f"{', '.join(short(c) for c in c89)}. The lines that carry the phrase 'timestamped 2026-08-18' "
      "(RESULTS.md@bbc9ffe:8195, :9072; the block :91) are carriers of the wording, counted as note locators in "
      "section 5, not sources. N13 says the date itself is not evidenced in the record.")
    cdiff = [x for x in P["same_figure_two_item_raws"] if x["relation"] == "STATUSES DIFFER"]
    cqual = [x for x in P["same_figure_two_item_raws"] if x["relation"].startswith("same base")]
    w("10. Two item raws on one figure (4f, round 3): "
      + ("; ".join(f"{x['row']} {x['primary_item']} '{x['primary_status']}' vs {x['other_item']} '{x['other_status']}'"
                   for x in cdiff) or "no pair differs in base status")
      + ". The pass check reads the primary row; N1 does not reconcile the two, and the design seat decides. "
      + ("Pairs that agree in base status but differ in qualifier: "
         + "; ".join(f"{x['row']} ({x['primary_item']} '{x['primary_status']}' vs {x['other_item']} "
                     f"'{x['other_status']}')" for x in cqual) + "." if cqual else ""))
    w(f"11. Corrections the --note matcher cannot surface (4g, round 3): {len(P['wording_scope_precision_corrections'])} "
      "entries from the item raws, several on rows that pass. N1 assigns them no status and decides none of them; they "
      "are listed so that the --note run reads each against the note's sentence. Who decides each is as its item-raw "
      "line says.")
    w("")
    if FN:
        render_final(w, J, FN)
    return "\n".join(o) + "\n"


def n19_text(FN):
    xs = FN["n19_raws_present"]
    if not xs:
        return "results/raw/ holds no N19 file at this run."
    parts = []
    for x in xs:
        t = (f"`{x['path']}` ({'committed at `' + short(x['commit']) + '`' if x['tracked'] else 'untracked: not committed'}"
             + ("" if not x["tracked"] else ", working tree equal to the committed blob" if x.get("equal_to_committed")
                else ", WORKING TREE DIFFERS from the committed blob")
             + f"; sha256 `{x['sha256'][:16]}`)")
        if x.get("status_rows"):
            t += " whose status table gives " + ", ".join(f"{y['value']} '{y['status']}' (:{y['line']})"
                                                           for y in x["status_rows"])
        parts.append(t)
    return "results/raw/ holds " + "; ".join(parts) + "."


NR_ROUND5 = [
    ("1", "MEDIUM", "Five discrepant rows (S1#26, S1#27, S1#140, S1#34, S4#19) were N1's own classification, not the "
                    "item raws'; the status paragraph named only the two '.60' rows, and O1 and O4 rested on N1's "
                    "readings while 9h said N1 declares no STOP.",
     "APPLIED, the first option. No item raw supports keeping them discrepant: N2 gives 5(b) as computed-new (N2 "
     "@09c3a8c:376); N5 gives the DIFF row reproduced (:206, :79) and has no 'envelope' wording; N3c gives L062 "
     "computed-new. N3's R1/R3 rule would call a wording that fails R1 'discrepant (transcription)', but N3 applies it "
     "to its own rows; for the MLP it checks its own draft (N3 @09c3a8c:479), not the note. The five rows now carry "
     "their item raws' statuses (four computed-new, one reproduced). What N1 reads in their sentences is recorded "
     "separately as a wording or precision correction (9i), as S8 does at :208. O1 and O4 say they are N1's own "
     "reading (the S1 and S8 mappers'), not an item raw's, and the status paragraph says there are no exceptions of "
     "N1's own. W8 stays N5's own classification (L102)."),
    ("2", "MEDIUM", "The validator was weaker than claimed. Of the checker's 29 mutations, these passed: status "
                    "changes on item-raw, record and audit-raw-new rows; a figure reclassified as not-figure; a wrong "
                    "source value matched at level B on another number or on '0'; a wrong ledger id with the same "
                    "status; and any change to a row that carried a validation_note. Some level-B passes matched only a "
                    "year or a line number.",
     "APPLIED (rules in 10b). New checks: the status check against the item raw (JSON figure row, table status cell, "
     "or a quoted status_basis; record rows log-only unless an item raw computes them; audit-raw-new rows "
     "computed-new); the kind assignment frozen by a hash; level B never on a year, a cited line number, a leading-zero "
     "identifier, a section number, a version inside a model name, or 0/1; level A required for decimal and fraction "
     "units; a fraction unit matched as the same k/n; every decimal to two or more places and every fraction a "
     "source_value states found on a cited line (the source-values check); the ledger-span check; and exemptions "
     "bound to the check they name and to a substring of its failure message, with a quote asserted on the first "
     "cited line for a value-check exemption. All 29 of the checker's mutations and Code's 26 now fail the run (10d). "
     "[Round 6 corrects this text: round 5's summary said 'every decimal' and 'its exact failure message'; the check "
     "read decimals to two or more places and matched a substring. Round 6 makes the match exact (11a, findings 4 "
     "and 8).]"),
    ("3", "LOW-MEDIUM", "S1#117 'three months of pre-registered experiments' (:20) was log-only on a README line that "
                        "carries only the start; it passed on the year '2026'.",
     "APPLIED: not found (O8). The record states the start (July 2026); N13's earliest pre-registration is 2026-08-04 "
     "(N13 @09c3a8c:56), 66 days before the note's date. Cut, or reworded to what the record carries."),
    ("4", "LOW", "Double rounding was handled two ways: S3#64 '0.88' stayed reproduced with 'choice not made', and the "
                 "MLP '.60' was discrepant.",
     "APPLIED: one rule (10b), checked mechanically. The item raw's status is carried and the rounding is recorded as "
     "a precision correction: S3#64 (reproduced), S1#34 and S4#19 (computed-new). The choice of form is the PI's (O17)."),
    ("5", "LOW", "O5 was listed among the STOPs; N6 raises none and calls it a sentence correction.",
     "APPLIED: O5 is a sentence correction, not a STOP (N6 @09c3a8c:493, :505), recorded on S2#37, S2#38 and S7#61; the "
     "S2 and S7 span notes carry annotations. [Round 6 revises this: N6 leaves the call to N1 and the design seat, so "
     "O5 is conditional, the design seat's call (11a, finding 6).]"),
    ("6", "LOW", "S1#73 and S5#38 could never pass: they carry the item raw's 'discrepant' although the note now "
                 "carries the reproduced value.",
     "APPLIED: the corrected-in-note rule (10b). Both carry 'discrepant', are marked corrected_in_note (the item raw's "
     "'correct to +0.095', quoted from N2 @09c3a8c:51, and the note's 0.095 tied to the source value at level A), and "
     "count as passing."),
    ("7", "LOW", "The overwrite guard worked only in final mode; a provisional run wrote the committed provisional "
                 "ledger by default.",
     "APPLIED: one guard for every mode, before anything is computed (10e). The provisional round has no default "
     "output, and no mode writes the provisional ledger; a provisional run never writes the final ledger either."),
    ("8", "LOW", "9g's tag conditions left out N11's re-run at the tag.",
     "APPLIED: 9g names it (W6: the 154/154 PASS is provisional, pre-tag, from a local clone)."),
    ("9", "nits", "'every fourth' (:58) had no row while 'third' and 'second' did; a span note said a search for the "
                  "cloud provider's name 'returned 0 in each file' while the committed files carried it in that "
                  "sentence; S7#19/S7#20 quoted about 20 words of arXiv:2609.16247v1.",
     "APPLIED: S2#43 'fourth' added (reproduced, N4 @09c3a8c:377); the S3 span note reworded so that it no longer "
     "spells out the strings it says were absent (annotated in 9f); the S7#19/S7#20 comments give the two numbers "
     "and the citation only. [Round 6: the quotation had stayed in round 5's change record for those two rows; it is "
     "removed there too (11a, finding 3).]"),
    ("10", "PI", "The PI's routing 10: re-map the five N19 rows to N19's raw at e0fd85c.",
     "APPLIED: S7#29, S7#33, S8#84 and S8#85 are reproduced (N19 @e0fd85c:119, :120). S1#145, the TL;DR's 'two', is "
     "computed-new (N19's post-hoc section 8) with a correction: 'carry most of the gap' is contradicted (17.8% under "
     "equal credences). 'Moves nothing' holds (computed-new, :121), and the 'because' clause does not "
     "(computed-new, :122). Both are recorded on S7#33. 9g moves to e0fd85c (O9)."),
]

NR_RULES = [
    ("Status (finding 1)", "A row's status is its item raw's (or ledger row's), carried exactly; N1 assigns none of "
     "its own. A wording, scope or precision problem N1 reads in the note's sentence is recorded in the row's "
     "'correction' ({kind, text, whose, basis}, 9i), never as a status. 'whose' says whether the reading is an item "
     "raw's or N1's own."),
    ("Status check (finding 2)", "item-raw and audit-raw-new rows: the first cited item-raw line that gives a status "
     "decides (its JSON figure row's status, matched by exact line text at the audit pin; else the cell under its "
     "table's 'status' column, including N11's text table); where none does, the row's status_basis (a line locator "
     "and a quote asserted on it, whose line gives a status or whose quote carries exactly one term); else an "
     "audit-raw-new row is computed-new by its mapping and an item-raw row fails. record rows: log-only, unless the "
     "row's first line locator is an item-raw line that gives a status. ledger-row rows: the ledger row's status, as "
     "before. No note exempts a row from this check. (Amended in round 6, 11b: record rows read every cited item-raw "
     "line, '[status: …]' tags are read, a status_basis must be in a file the row cites, and every row that names a "
     "ledger row carries its status.)"),
    ("Double rounding (finding 4)", "A note figure that rounds from a printed value which itself rounds a more "
     "precise value the row states, while the precise value rounds to something else at the note's places, is a "
     "double rounding. The item raw's status is carried; the row must carry a precision correction (else the run "
     "fails); the form the note uses is the PI's choice."),
    ("Corrected in the note (finding 6)", "A row whose item raw is discrepant and whose note figure now carries the "
     "item raw's correction keeps the status 'discrepant', is marked corrected_in_note ({locator, quote}: a line the "
     "row cites, quoting the item raw's correction, which states the note's value), and counts as passing when the "
     "note's figure ties to the source value at level A. A mark that fails any of these fails the run. (Amended in "
     "round 6, 11b.)"),
    ("Value check (finding 2)", "Level A: a cited line carries a value the source_value states that is tied to the "
     "note's number (equal, or stated to more places and rounding half-up to it; a fraction k/n, written 'k/n' or "
     "'k of n', is also its exact value; a fraction unit needs the same k/n in the source_value and on the line). "
     "Level B: a cited line carries another distinctive value the row states, never a year (1900-2099), a cited line "
     "number, a leading-zero identifier, a section number ('§7.3'), a version inside a hyphenated name "
     "('OLMo-3.1-32B'), or 0/1. A decimal or fraction unit must pass at level A."),
    ("Stated values (finding 2)", "Every value a source_value states to two or more places, and every fraction it "
     "states ('k/n' or 'k of n', not '1/2'), is on a line the row cites (its locator's lines, and line references "
     "inside the source_value, read against the locator's first file when they name none). A misstated value fails "
     "even when another stated value ties the note's number."),
    ("Ledger span (finding 2)", "A ledger id a row names must carry the note's number: the ledger row's block span, or "
     "its item-raw rows' figure labels or printed values, contain the unit's text, a value tied to it (fractions as "
     "values) or its number word."),
    ("Kind (finding 2)", "The unit -> kind assignment (one line per row: span#seq, file, line, unit, kind) hashes to "
     "NR_KIND_SHA256 in the script; any other assignment stops the run, so a reclassification is a visible change to "
     "the script."),
    ("Exemptions (finding 2)", "A failure is explained only by 'validation_exempts' mapping its check (locator-value, "
     "source-values, ledger-status or ledger-span) to a substring of its message, with a validation_note saying why; "
     "a locator-value exemption also needs a validation_quote on the row's first cited line. An exemption that "
     "explains nothing fails the run. (Amended in round 6, 11b: the whole message, and a fingerprint the script "
     "declares.)"),
]

NR_LIMITS = [
    "Integer and word units can still pass at level B on another distinctive value the row states that is on a cited "
    "line ({nb} rows at level B). Since round 6 an integer unit's own number must be stated in the source_value (the "
    "unit-stated check), but the cited line need not carry it. The source-values check covers every decimal (one "
    "place or more) and every fraction a source_value states; an integer elsewhere in a source_value, neither the "
    "unit nor in a fraction, is not checked (self-test L03).",
    "A word unit ('one', 'two') passes at level A when the word occurs on a cited line, whatever its source_value "
    "says (self-test L02); the word can be a coincidence. S7#12's round-4 pass and S7#15's round-5 pass were; both "
    "rows now carry a locator-value exemption that says what their lines do carry.",
    "Status binding (rewritten in round 7). The status check binds a row's status to the cited item-raw lines that "
    "give a status and carry a value the row states, to its quoted status_basis (an item-raw line; a single-term "
    "clause where its line gives several terms), or to the ledger row it names, which the ledger-bind check ties to "
    "the row. The row checks cannot tell a row's own figure line from another figure's line that carries the same "
    "value, or the clause that applies from another clause of the same line. So a status changed together with one "
    "more field still passes them: a locator prefix with a reproduced figure row that carries one of the row's values "
    "({g} of the {ng} rows whose status is computed-new, discrepant, not found or log-only; family G, 12d), a ledger_row swap to a row the "
    "locator binds ({h} of {nh}; family H), a status_basis moved with the status to another line or clause of a cited "
    "item raw (L01; N3c :151's 'reproduced' clause, L04), and a 'related row' field cut to its ledger row (L05). Since "
    "round 7 every such change also changes the input of the status freeze (NR_STATUS_SHA256: every row's maps_to, "
    "status, ledger_row and status_basis), so the run fails (status-hash) unless the script is changed with it, where "
    "it shows in a diff. The freeze does not judge whether a status is right.",
    "The frozen declarations (NR_KIND_SHA256, NR_CLAUSE_SHA256, NR_STATUS_SHA256, NR_TEXT_SHA256, NR_EXEMPT_FP, "
    "NR_CORRECTIONS with its fingerprints, NR_QUOTE_REVIEWED, NR_DISC, the watch rows and the open items' rows) "
    "freeze; they do not judge. A row edited together with its declaration passes, and both show in a diff. Whether a "
    "unit is a figure, whether a clause is a fair cut of its sentence, and whether a status, a correction or a comment "
    "is right stays the mappers' and their checkers' reading.",
    "Ledger rows (rewritten in round 7). The ledger-span check accepts any named ledger row that carries the value, so "
    "a common value (0.000, 0.5) can pass on a wrong row. Since round 7 the ledger-bind check requires the row's "
    "first ledger id to be named in its locator, or one of that ledger row's item-raw lines to be cited, and every "
    "ledger id the locator names to be in ledger_row; a swap to a ledger row the locator binds passes the row checks "
    "(bullet 3). Every ledger_row change, of any status, fails the status freeze.",
    "Free text is frozen, not judged (rewritten in round 7). NR_TEXT_SHA256 covers every comment, cause, not-figure "
    "reason and validation note, every change record (round5, round6 and round7, their 'why' and 'previous' "
    "included), every span note and annotation, and the file's how_built, schema and provenance; NR_CORRECTIONS' "
    "fingerprints cover each correction's text and basis (an N1-own correction's basis line is bound to the "
    "declaration, not checked against the correction). Beyond that, only the quotes the script asserts (NR_DISC's "
    "causes, the open items' and the watch-list's span notes) and the quotation scan read it.",
    "Not-found rows (round 7). A not-found row's locator and source value are in the status freeze, and every file and "
    "line they cite must exist (pins); whether the search they describe was complete stays the mappers' reading.",
    "The quotation scan (round 7) is a heuristic: a quoted span of fifteen words or more within reach of a name in "
    "NR_QUOTE_EXT_RE, in the rows file only. A long quotation without quotation marks, or with no such name nearby, is "
    "not flagged, and the script's own prose and the rendered ledger are not scanned; the rule on external quotations "
    "stays the author's to keep.",
    "A mutation test run from outside the script that edits a field one of the self-test's own mutations edits makes "
    "that self-test mutation not applicable, and the run stops for that reason, not by validation (n1chk2's E05 and "
    "C18 did). The self-test now runs both, and their decoupled twins, each on a fresh copy.",
    "Every check is a consistency check on the mapping; none re-derives a figure.",
]

NR_ROUND6 = [
    ("1", "MEDIUM-HIGH", "maps_to was never checked: a computed-new row remapped to 'record' with status 'log-only' "
                         "passed end to end (29 of 62 at the row checks, 25 after the script's hard-coded lists). The "
                         "record rule fell back to log-only when the first cited item-raw line gave no status; nothing "
                         "required a record row to cite a record line; N3c's '[status: …]' tags were not read; and a "
                         "ledger-row row remapped to 'record' skipped the ledger-status comparison. 10f did not say so.",
     "APPLIED. A maps-to check: item-raw and audit-raw-new rows must cite an item-raw line, and record rows a record "
     "line (outside the audit outputs, at or before bbc9ffe). The record rule reads every cited item-raw line that "
     "gives a status, and N3c's inline '[status: …]' tags are read. A row that names a ledger row carries that row's "
     "status whatever its maps_to. Five rows differ for a stated reason and carry ledger-status exemptions: the four N19 "
     "rows against the provisional ledger's 'not run' (L159, L160) and S7#73 against L088's stale referent. All 62 "
     "computed-new rows remapped to record and log-only now fail (self-test family A). Every one fails maps-to, and 52 "
     "also fail status or ledger-status. (Round 7, 12a finding 1: the class was not closed. A one-field change from "
     "computed-new to reproduced still passed on five rows, through N3c :151's two-term tag and the 'related row' "
     "fields.)"),
    ("2", "MEDIUM", "The corrected_in_note check verified nothing that mattered. All 19 uncorrected discrepant rows "
                    "passed with a mark quoting the note's own number from their own cited line, and then counted as "
                    "passing. On S6#68 the ledger said both 'passes (corrected in the note)' and that O2 is a live "
                    "STOP. 10f did not say so.",
     "APPLIED, all three of the checker's fixes, the third in adjusted form. The quote must carry the item raw's "
     "correction wording ('correct to', 'corrected to', 'Corrected value:') followed by the note's value. The marked rows "
     "must be exactly NR_DISC's branch C, or the run stops. The cited line must be the item raw's JSON figure row, and "
     "the note's value must differ from the discrepant figure that row quotes: for S1#73 and S5#38, N2 :51 quotes "
     "'+0.096' and the note carries 0.095. The checker asked for a difference from the item raw's printed value. N2's "
     "printed value is the reproduced one, which a corrected note carries by design, so the check compares the quoted "
     "figure instead. All 19 forged marks now fail (family B), and so do C05-C07 and C20. S6#68 is branch NT, so the "
     "contradiction cannot recur."),
    ("3", "MEDIUM (hard rule)", "A 20-word verbatim quotation of arXiv:2609.16247v1 was still in the files. Round 5 cut "
                                "it from the S7#19/S7#20 comments but kept it in round5.changed[].previous: twice in "
                                "the rows file and four times in the final JSON.",
     "APPLIED. The quotation is removed from both rows' change records and replaced by a bracketed statement that a "
     "twenty-word quotation was removed. Round 6's own record names the change without repeating the quotation. Code "
     "re-ran n1chk2's quotation scan (quoted spans of fifteen or more words near an external citation, outside the "
     "script) on the round-5 and the round-6 files: every hit new in round 6 is round 6's own prose, none a "
     "quotation of an external source (n1chk2 had found every other external quotation at fourteen words or "
     "fewer), and neither half of the removed sentence occurs in any of the four files."),
    ("4", "LOW-MEDIUM", "Exemptions were matched by substring, not by the exact message, so a forged 'FAIL' exempted "
                        "anything (E05b). The five locator-value exemptions used the generic message, so their "
                        "source_value could be anything (E01-E04). Round 5's summary ('matched to the exact failure "
                        "message') overclaimed.",
     "APPLIED. An exemption explains a failure only when it equals the whole message, and the locator-value message "
     "names the values sought and the lines read. Every exempted row is declared in the script with a fingerprint of "
     "its mapping fields (NR_EXEMPT_FP, 18 rows), so a change to any of them leaves the failure unexplained. E01-E06 "
     "and E05b now fail, and so does every exemption cut to half its message (family E). 10a's text for round 5's "
     "finding 2 now says that round 5 matched a substring."),
    ("5", "LOW", "Corrections could be deleted (C08-C11) or misattributed (C21) without failing the run; their 9i "
                 "entries disappeared while the hard-coded O-items survived.",
     "APPLIED. NR_CORRECTIONS declares the twelve corrections: row, kind, and whose reading it is (N1's own, or an "
     "item raw's, whose basis must then cite that raw). A missing, undeclared, re-kinded or re-attributed correction "
     "fails. The open items that rest on a correction (O1, O4, O5, O9, O17) name it, and each is asserted. C08-C11 and "
     "C21 now fail, and so do families C and D (every correction removed; every 'whose' swapped)."),
    ("6", "LOW", "O5's 'Not a STOP' overstated N6. N6 @09c3a8c:505 says that whether these rows are figure STOPs or "
                 "sentence corrections is N1's and the design seat's call, not N6's; N6's own reading is a sentence "
                 "correction. The O5 headline and the S2/S7 annotations dropped the design seat.",
     "APPLIED. O5 now says what N6 says. N6's gloss row is 'discrepant' (a definition error, not a transcription; no "
     "number is discrepant, :493). N6 raises no STOP and leaves the call to N1 and the design seat (:505). N1 reads the "
     "row as a sentence correction, as N6 does, and records it on S2#37, S2#38 and S7#61. The design seat rules; if it "
     "does not accept that reading, block :23's non-transcription branch makes it a STOP on N6. The S2 and S7 span "
     "notes carry round-6 annotations that supersede round 5's, and the S2 mapper's conditional framing stands. The "
     "9h preamble lists O5 as conditional."),
    ("7", "LOW", "Two fields were unchecked: a locator revision moved off the pins passed (C15), and so did an altered "
                 "clause (C16).",
     "APPLIED. A pins check requires every revision a row cites (locator, source value, status basis, "
     "corrected_in_note, correction basis) to be its path class's pin. The clauses are frozen by a hash "
     "(NR_CLAUSE_SHA256), like the kind assignment. 98 of the 504 clauses are not verbatim on their note line (the "
     "mappers describe SVG nodes and mark range ends), so a text check would not hold; the hash freezes the clauses "
     "and does not judge them. C15 and C16 now fail."),
    ("8", "LOW (disclosed)", "Confirmed as disclosed in 10f: integers still pass at level B (C12, C13), one-place "
                             "decimals are unchecked (C14), and a status changed together with its basis passes "
                             "(C18b). Round 5's summary 'every stated decimal' left out 'two or more places'.",
     "PARTLY CLOSED; the rest stays disclosed (10f). An integer unit's number must now be stated in the source value "
     "(tied, a floor such as 17.500 for '17×', a label such as 'L60', or a percentage), so C12 and C13 fail. One-place "
     "decimals are checked, so C14 fails; S5#48's '97.5' needed its table's column header (N2 :399) cited, and "
     "'section 5.6' is now stripped whole. A status_basis in a file the row does not cite now fails; C18 and C18b "
     "moved the basis within N3c, the file they cite, and fail instead on the status tag (C18) and the ledger check "
     "(both). Still open, each run in the self-test as a known limit that must "
     "stay uncaught: a status and its basis moved together within one item raw (L01); a word unit whose word is on a "
     "cited line, with any source value (L02); and an integer elsewhere in a source value (L03). 10a's text for round "
     "5's finding 2 now says 'two or more places'."),
    ("9", "nits", "O4 lists S8#78, but 9i records no correction on it (S8#79 has one). S7#15's 'second' passed at "
                  "level A on an unrelated 'second' (PROPOSAL-m :174).",
     "APPLIED. O4 and the d′ watch line now say that the correction is on S1#26, S1#27 and S8#79, because S8 records "
     ":208's range once, on its upper end; the three are asserted. S7#15's :174 and :186 move from its locator to the "
     "source value's context; they support 'the scaffolded cell', not the count. The row carries a locator-value "
     "exemption: the ordinal is the S7 mapper's count of the record's armed clauses, and no line states it."),
]

NR_RULES6 = [
    ("maps-to (finding 1)", "item-raw and audit-raw-new rows cite at least one item-raw line (an item raw of 2026-10-08, "
     "or N19's of 2026-10-09); record rows cite at least one record line (a path outside the audit outputs, at or "
     "before bbc9ffe, readable there). Not exemptable."),
    ("Status check (finding 1; amends 10b)", "record rows: every cited item-raw line that gives a status is read, and "
     "the row's status is one of their terms (log-only where none gives one). An inline '[status: …]' tag on a cited "
     "line gives its terms (several terms: any of them). A status_basis is a line of a file the row's locator cites. A "
     "row that names a ledger row (not 'related only') carries that row's status whatever its maps_to; a row whose "
     "status differs for a stated reason carries a ledger-status exemption. (Amended in round 7, 12b: several terms "
     "decide nothing; a status line decides only where it carries the row's value; a 'related row' field is compared "
     "with that related row only.)"),
    ("Corrected in the note (finding 2; amends 10b)", "The quote carries the item raw's correction wording ('correct to', "
     "'corrected to', 'Corrected value:') followed by the note's value; the line is the item raw's JSON figure row; "
     "the note's value differs from the discrepant figure that row quotes; and the rows marked are exactly NR_DISC's "
     "branch C (else the run stops)."),
    ("Exemptions (finding 4; amends 10b)", "An exemption explains a failure only when it equals the whole message; the "
     "locator-value message names the values sought and the lines read. Every exempted row is declared in "
     "NR_EXEMPT_FP with a fingerprint (the first 16 hex of a sha256) over its note file and line, unit, kind, maps_to, "
     "status, ledger row, locator, source value, status basis, correction, corrected_in_note, exemptions, quote and "
     "note; any change to them, or an undeclared exemption, fails. Exemptable: locator-value, source-values, "
     "ledger-status, ledger-span, unit-stated."),
    ("Corrections (finding 5)", "NR_CORRECTIONS declares each correction: its row, kind, and whose reading it is (N1's "
     "own: 'whose' starts \"N1's\"; an item raw's: 'whose' starts '<item> (' and the basis cites that raw). A missing, "
     "undeclared, re-kinded or re-attributed correction fails; an open item that rests on a correction names it, "
     "asserted."),
    ("Pins and clauses (finding 7)", "Every revision a row cites is its path class's pin: the record at bbc9ffe; item "
     "raws at 09c3a8c (N8 and N11 also at 02b6a61); N19's raw at e0fd85c; the provisional ledger at 6485da2. The "
     "clauses hash to NR_CLAUSE_SHA256 ('span#seq<TAB>clause', file order)."),
    ("Unit stated; one-place decimals (finding 8)", "An integer unit's number is stated in the source_value: a tied "
     "numeral, a value whose integer part it is (a floor), the unit's digits inside a label ('L60', '4bit'), or, where "
     "the note prints it as a percentage, a proportion tied at the percentage scale. The source-values check covers "
     "one-place decimals (equal on a cited line). A dotted section number ('section 5.6') is stripped whole."),
    ("Self-test (all findings)", "Besides round 5's 55, the self-test runs the 27 n1chk2 mutations round 5 did not "
     "catch, or caught only through the self-test's own coupling ('checker 2'), and Code's 11 ('round 6'). It also "
     "runs five families generated from the rows: (A) every computed-new row remapped to record and log-only; (B) "
     "every uncorrected discrepant row given a forged corrected_in_note; (C) every correction removed; (D) every "
     "correction's 'whose' swapped; (E) every exemption cut to half its message. Three known limits must stay "
     "uncaught (10f). A mutation that is not caught, or a limit that is caught, stops the run."),
]


NR_ROUND7 = [
    ("1", "substantive", "A one-field edit changed a computed-new figure to reproduced and passed end to end on five "
                         "rows, and 10f and 11 did not disclose it; 11a reported round 6's finding 1 as closed. Two "
                         "causes: the 'several terms: any of them' rule for '[status: …]' tags let N3c :151's tag "
                         "(computed-new, except one column reproduced) pass 'reproduced' for S4#23 and S7#51; and a "
                         "ledger_row naming a related row ('L004 (related row: N2 row 37, computed-new)') also accepted "
                         "the primary row's status, so S5#20, S5#22 and S5#23 passed as reproduced.",
     "APPLIED. (a) A source that gives several terms (a '[status: …]' tag, a status cell, a JSON 'mixed' status, or a "
     "record row's lines together) decides nothing by itself: the row needs a status_basis whose quote is the "
     "single-term clause that applies, and the quote's term decides. S4#23 and S7#51 already quote N3c :151's "
     "computed-new clause, which now decides. (b) A ledger_row that names a related row is compared with that related "
     "row only (resolved by item and JSON index; the status the field states must be the related row's), and a "
     "'related only' field leaves the status to the row's own check. A new self-test family F sets every figure "
     "row's status to each other term, one field at a time: the row checks alone catch every member (12d); r6chk's "
     "N08-N11 and N32 are in the self-test, each caught by the row checks. What remains, a clause or basis moved with the status (L04, "
     "L01), is in 10f bullet 3. 11a's finding 1 now points here."),
    ("2", "substantive", "Two-field upgrades passed, and 10f's disclosures were narrower than the hole. The status "
                         "check bound a row to whatever item-raw line it cited first, or to whatever ledger row it "
                         "named; nothing checked that the line or ledger row addresses the row's figure. A status "
                         "change plus an unrelated locator line, a swapped ledger_row, or a status_basis on an "
                         "unrelated record line passed (N04-N07, N12-N15). The checker's screen found 44 of the 62 "
                         "computed-new rows and 75 of the 88 log-only rows upgradable with at most two fields.",
     "APPLIED, in two layers. Row checks: a cited item-raw status line decides only where it carries a value the row "
     "states (the locator check, read on that line), so another figure's line decides nothing; a status_basis must be "
     "an item-raw line, and every cited status line that carries the row's value must agree with it; a new "
     "ledger-bind check requires the first ledger id to be named in the locator, or one of its item-raw rows' lines to "
     "be cited, and every ledger id the locator names to be in ledger_row. Fourteen locators now name their ledger "
     "row, and S2#34, S5#61 and S10#62 name their comparison rows (12c). The checker's level-A option for the deciding "
     "line was tried: it broke five rows and closed 10 of the 67 rows Code's screen found open, so level B counts "
     "where the locator check accepts it. Freeze: NR_STATUS_SHA256 over every row's maps_to, status, ledger_row and "
     "status_basis, the checker's simplest robust option, so every status or ledger change is also a script diff. "
     "N04-N07, N12 and N13 now fail the row checks; N14 and N15 fail only the freeze (N2 :24 carries a value S5#35 "
     "and S3#7 state). Families G (a reproduced figure row prefixed) and H (a ledger row swapped) run over the 184 "
     "rows whose status is computed-new, discrepant, not found or log-only: every member is caught, and 12d counts those the row checks let "
     "through. 10f bullets 3 and 5 now say what remains. S10#68, the checker's illustration, carries a status_basis on "
     "N2 :136, its own inline status; S9#57 carries one on N2 :90, whose status cell no longer decides without it."),
    ("3", "minor", "Not-found rows accepted fabricated locators and source values, including nonexistent files and "
                   "lines (N16, N17); the pins check verified only the revision, and the ledger rendered what it "
                   "was given.",
     "APPLIED. The pins check also requires every cited file to exist at its revision and every cited line to be "
     "within it, on every row. S4#28 and S4#32 named 'stageC_analysis.json@bbc9ffe', which is no file at that "
     "revision; they now give the stored analyses' full paths under data/echo/. A not-found row's locator and source "
     "value are in the status freeze. N16 now fails status-hash and N17 fails pins. Whether a not-found row's search "
     "was complete stays the mappers' reading (10f bullet 7)."),
    ("4", "minor", "Two fields were unchecked, and 10f's free-text list did not name them: the change records "
                   "('previous', 'why'; where round 5's twenty-word quotation survived; N28), and the basis of an "
                   "N1-own correction (N27).",
     "APPLIED, beyond naming them. NR_TEXT_SHA256 freezes the free text and the change history: every comment, cause, "
     "not-figure reason, validation note, change record, span note and annotation, and the file's how_built, schema "
     "and provenance. N20, N28, N29 and N30 now fail text-hash. NR_CORRECTIONS carries a fingerprint of each whole "
     "correction (kind, text, whose, basis), so N27 fails correction-declared. The optional scan runs at every run: "
     "quoted spans of fifteen words or more near the name of an external source, in every string of the rows file. "
     "Its two hits (S1#25 and S7#16 quote item-raw lines) are declared with Code's reading, and an undeclared hit "
     "fails validation (T06 plants one). 10f bullets 6 and 8 say what stays open: frozen text is not judged, and the "
     "scan is a heuristic."),
]

NR_RULES7 = [
    ("Status check (findings 1 and 2; amends 10b and 11b)", "A cited item-raw line that gives a status decides only "
     "where it carries a value the row states (nr_line_carries: the locator check read on that line alone, level A, "
     "or B where B is accepted); a status line that carries none decides nothing. A source with several terms (a "
     "'[status: …]' tag, a status cell, a JSON 'mixed' status, a record row's lines together) decides nothing by "
     "itself. A status_basis is a line of an item raw the row cites (never a record line); its line's single term "
     "decides, or, where the line gives several terms or none, its quote's single term (one of the line's where it "
     "gives several); every cited status line that carries the row's value must give the basis's term too. Without "
     "a basis: item-raw and audit-raw-new rows take the first such line's term (an audit-raw-new row with none is "
     "computed-new; an item-raw row with none fails), record rows their lines' single term, or log-only."),
    ("ledger-status (finding 1)", "'Lnnn (related row: <item> row <n>, <status>)' compares the row's status with that "
     "related row only, resolved by item and JSON index n-1, and the stated status must be the related row's; "
     "'(related only …)' leaves the status to the row's own check (the ledger row is context)."),
    ("ledger-bind (finding 2)", "The first ledger id a row names is named in its locator, or the locator cites a line "
     "of one of that ledger row's item-raw rows (same path and line number, the same text at both revisions; the "
     "named related row for 'related row', any for 'related only'); and every ledger id the locator names is in "
     "ledger_row. Not exemptable."),
    ("Pins (finding 3; amends 11b)", "Every cited file exists at its revision and every cited line is within it, on "
     "every row and in every field the pins check reads."),
    ("Freezes (findings 2-4)", "NR_STATUS_SHA256: one line per row, 'span#seq, maps_to, status, ledger_row, "
     "status_basis', and for a not-found row its locator and source value. NR_TEXT_SHA256: the file's item, title, "
     "how_built, schema and provenance, every span, and per row its comment, cause, not_figure_reason, "
     "validation_note and change records. NR_CORRECTIONS: a fingerprint of each whole correction. A mismatch fails "
     "validation; a deliberate change is made in the script too."),
    ("Quotation scan (finding 4)", "Every string of the rows file is scanned for quoted spans of fifteen words or more "
     "within 250 characters before or 120 after a name in NR_QUOTE_EXT_RE (the round-6 checker's list); each hit is "
     "declared in NR_QUOTE_REVIEWED by its sha256 prefix with Code's reading, and an undeclared hit fails validation."),
    ("Self-test (all findings)", "Besides round 6's, the self-test runs r6chk's twenty mutations that round 6 did not "
     "catch ('checker 3'), Code's eight ('round 7'), three families evaluated row by row (F: every figure row's "
     "status set to each other term, expected caught by the row checks alone; G: a reproduced figure row prefixed to "
     "the locator, and H: a ledger row swapped, each with the status 'reproduced', over every row whose status "
     "is computed-new, discrepant, not found or log-only, expected caught; G and H pick the first candidate the row checks let through, so they "
     "report the worst case), and five known limits at two levels: 'full' (L02, L03; uncaught by a whole run) and "
     "'row' (L01, L04, L05; uncaught by the row checks, caught by the status freeze). Each self-test entry also says "
     "whether the row checks alone catch it."),
]


def render_final(w, J, FN):
    """Section 9: the note v0.3 and its two SVGs, row by row (N1 final); section 10: round 5's values check."""
    short_f = {"RESEARCH-NOTE-v0_3-draft.md": "note", "2026-10-06_F1b_five-link-panels.svg": "F1b",
               "2026-10-06_F2_macar-lineage-roc_post.svg": "F2"}
    rows = FN["rows"]
    byk = {f"{r['span']}#{r['seq']}": r for r in rows}
    figs = [r for r in rows if r["kind"] == "figure"]
    ent = {e["row"]: e for e in FN["entries"]}

    def fl(r):
        return f"{short_f[r['note_file']]}:{r['note_line']}"

    def ref(k):
        return f"{k} ({nr_unit(byk[k])}, {fl(byk[k])})"

    w("## 9. Note v0.3 and SVG rows (N1 final)")
    w("")
    w("Block :22 asks for one row per figure in the note and in the F1/F2 SVGs, with its source and a status, and for "
      "the commit at which the last of the note's figures entered the record. Sections 1-8 answered that over the "
      "block's quotations; this section answers it over the files the PI placed. Line numbers are the note's lines; "
      "for an SVG, the text-node index under the matcher's extraction (text, tspan, title and desc content, one node "
      "per line). Locators: the record at bbc9ffe, item raws at 09c3a8c (N8 and N11 also at 02b6a61, where they were "
      "regenerated; S3's rows note that every N8 line they cite is byte-identical at 09c3a8c), N19's raw at e0fd85c, "
      "the provisional ledger at 6485da2 (since round 6 every row's revisions are checked against these pins). Round 5 "
      "(section 10) applied the final checker's findings and the PI's N19 routing; round 6 (section 11) applied the "
      "adversarial check of round 5; round 7 (section 12) applied the strict check of round 6 (since round 7 every "
      "cited file and line must also exist).")
    w("")
    w("| file | sha256 (at this run) | routed | match | tracked at HEAD |")
    w("|---|---|---|---|---|")
    for f in FN["files"]:
        w(f"| `{f['path']}` | `{f['sha256']}` | {f['routed']} | {'MATCH' if f['match'] else 'MISMATCH'} | "
          f"{'yes' if f['tracked'] else 'no (untracked)'} |")
    w("")
    # ---------------------------------------------------------------- 9a
    w("### 9a. Inputs, coverage and validation")
    w("")
    w(f"Input: `{FN['rows_file']}` (sha256 `{FN['rows_file_sha256']}`), {FN['n_rows']} rows: {FN['n_figures']} figures "
      f"and {FN['n_not_figures']} not-figures. How it was built (from the file): {FN['how_built']}")
    w("")
    w("| span | covers | source of the final set (scratch; not committed) | sha256 | round | rows |")
    w("|---|---|---|---|---|---|")
    hdr = {s["span"]: s["header"] for s in FN["spans"]}
    for x in FN["provenance"]:
        w(f"| {x['span']} | {cell(hdr.get(x['span']), 260)} | `{x['source_file']}` | `{x['source_sha256'][:16]}` | "
          f"{x['round']}{(' -- ' + cell(x['integration_note'])) if x.get('integration_note') else ''} | {x['n_rows']} |")
    w("")
    w("The table gives each span's mapper set as it came from scratch; round 5 added one row (S2#43) and edited the "
      "rows listed in 10c.")
    w("")
    w("Coverage. Every unit the matcher (section 7) extracts has a row, per file, as a multiset over (line, unit); a run "
      "with a matcher unit and no row stops. Rows beyond the matcher are units it cannot see (number words above "
      "twelve, ordinals, multiplicative words, '½'):")
    w("")
    w("| file | matcher units | rows | rows beyond the matcher |")
    w("|---|---|---|---|")
    for c in FN["coverage"]:
        w(f"| `{c['path']}` | {c['matcher_units']} | {c['rows']} | "
          f"{', '.join(f'{k} ({v})' for k, v in c['rows_beyond_matcher'].items()) or 'none'} |")
    w("")
    V = FN["validation"]
    nl_pass = sum(1 for r in rows if r["validation"].get("note_line") == "pass")

    def tally(key):
        t = {}
        for r in figs:
            res = r["validation"].get(key, {}).get("result", "n/a")
            k = res.split(":")[0].split(" (")[0]
            if r.get("validation_exempts") and k == "FAIL":
                k = "FAIL, explained by a named exemption"
            t[k] = t.get(k, 0) + 1
        return "; ".join(f"{k} {v}" for k, v in sorted(t.items()))
    lv = {}
    for r in figs:
        lc = r["validation"].get("locator", {})
        k = ("level A" if lc.get("level") == "A" else "level B" if lc.get("level") == "B" else
             "n/a (not found)" if lc.get("result", "").startswith("n/a") else "FAIL, explained by a named exemption")
        lv[k] = lv.get(k, 0) + 1
    w("Validation (every row; each check has a name, and the rules are in 10b and in the script, `nr_validate_row`):")
    w("")
    w(f"- **note-line.** The unit occurs on the cited line of its file: {nl_pass} of {len(rows)} rows.")
    w(f"- **kind-hash.** The unit -> kind assignment hashes to `{FN['kind_sha256']}` (NR_KIND_SHA256): "
      f"{FN['n_figures']} figures, {FN['n_not_figures']} not-figures.")
    w("- **schema.** A figure's status is one of " + ", ".join(NR_STATUSES[:-1]) + "; a not-figure's is n/a and it "
      "carries a reason; maps_to none goes with not found; exemptions and notes come in pairs.")
    w(f"- **locator-value** (figures that are reproduced, log-only, computed-new or discrepant): "
      + "; ".join(f"{k} {v}" for k, v in sorted(lv.items())) + f". Found on a later locator than the first: "
      f"{len(V['locator_secondary'])}.")
    bl = [ref(k) for k in (f"{r['span']}#{r['seq']}" for r in figs)
          if byk[k]["validation"].get("locator", {}).get("level") == "B"]
    w(f"  - Level-B rows ({len(bl)}, every one an integer or word unit): " + "; ".join(bl) + ".")
    sc = FN["status_check"]
    sb = [ref(k) for k in (f"{r['span']}#{r['seq']}" for r in figs) if byk[k].get("status_basis")]
    w(f"- **status** (item-raw, audit-raw-new and record rows; ledger-row rows are checked against their ledger row): "
      f"decided by a JSON figure row {sc.get('JSON figure row', 0)}, a table status cell {sc.get('status cell', 0)}, "
      f"an inline '[status: …]' tag {sc.get('status tag', 0)} (round 6), "
      f"a quoted status_basis {sc.get('status_basis', 0)}, the record rule (log-only) {sc.get('record lines only', 0)}, "
      f"the audit-raw-new rule (computed-new) {sc.get('audit-raw-new', 0)}; n/a (ledger-row maps and not found) "
      f"{sc.get('n/a', 0)}. Every status agrees. Rows with a status_basis ({len(sb)}): " + "; ".join(sb) + ".")
    skp = [ref(k) for k in (f"{r['span']}#{r['seq']}" for r in figs)
           if byk[k]["validation"].get("status", {}).get("skipped")]
    w(f"  - Round 7 (12b): a cited item-raw status line decides only where it carries a value the row states, a source "
      f"with several terms decides nothing by itself, and a status_basis is an item-raw line. Rows citing a status line "
      f"that carries none of their values and is not their status_basis (another figure's row or section; it decided "
      f"nothing) ({len(skp)}): "
      + ("; ".join(skp) or "none") + ".")
    cc = FN.get("check_counts", {})

    def cct(c):
        x = cc.get(c, {})
        return f"pass {x.get('pass', 0)}, FAIL {x.get('FAIL', 0)}, n/a {x.get('n/a', 0)}"
    w(f"- **maps-to** (round 6; item-raw and audit-raw-new rows cite an item-raw line, record rows a record line): "
      f"{cct('maps-to')}.")
    w(f"- **pins** (round 6; every revision a row cites is its path class's pin; round 7: the cited file exists at "
      f"that revision and every cited line is within it): {cct('pins')}.")
    w(f"- **unit-stated** (round 6; an integer unit's number is stated in the source_value): {cct('unit-stated')}.")
    w(f"- **correction-declared** (round 6; corrections as NR_CORRECTIONS declares them; round 7: each with a "
      f"fingerprint of the whole correction): {cct('correction-declared')}.")
    w(f"- **clause-hash** (round 6): the clauses hash to `{FN.get('clause_sha256')}` (NR_CLAUSE_SHA256).")
    w(f"- **exemption-declared** (round 6): every exempted row is declared in NR_EXEMPT_FP with its fingerprint "
      f"({len(NR_EXEMPT_FP)} rows); an exemption equals its whole failure message.")
    w(f"- **source-values** (every decimal, one place or more since round 6, and every fraction the source_value "
      f"states is on a cited line): {tally('source_values')}.")
    w(f"- **ledger** (a named ledger id exists and the row carries its status; round 5 compared only ledger-row maps, "
      f"round 6 every row that names one): {tally('ledger')}.")
    w(f"- **ledger-span** (a named ledger row carries the note's number): {tally('ledger_span')}.")
    w(f"- **ledger-bind** (round 7; the first named ledger row is named in the locator or one of its item-raw rows' "
      f"lines is cited, and every ledger id the locator names is in ledger_row): {cct('ledger-bind')}.")
    w(f"- **status-hash** (round 7): the status-deciding fields (maps_to, status, ledger_row, status_basis; a "
      f"not-found row's locator and source value too) hash to `{FN.get('status_sha256')}` (NR_STATUS_SHA256).")
    w(f"- **text-hash** (round 7): the free text and the change history hash to `{FN.get('text_sha256')}` "
      f"(NR_TEXT_SHA256).")
    qs = FN.get("quote_scan") or []
    w(f"- **quote-scan** (round 7): quoted spans of fifteen words or more near the name of an external source, in every "
      f"string of the rows file: {len(qs)}, each declared in NR_QUOTE_REVIEWED with Code's reading ("
      + ("; ".join(f"{q['where']}, {q['words']} words: {q['reviewed']}" for q in qs) or "none") + ").")
    dr = [ref(k) for k in (f"{r['span']}#{r['seq']}" for r in figs)
          if byk[k]["validation"].get("double_rounding", {}).get("chains")]
    w(f"- **double-rounding**: {len(dr)} rows ({'; '.join(dr) or 'none'}), each with a precision correction.")
    w(f"- **correction** and **corrected-in-note**: {len(FN['corrections'])} corrections (9i), "
      f"{len(FN['pass_check']['corrected_in_note'])} rows corrected in the note "
      f"({', '.join(FN['pass_check']['corrected_in_note']) or 'none'}); all pass their checks.")
    w(f"- **Failures without an exemption: {len(V['failures'])}.** Failures explained by a named exemption "
      f"({len(V['explained'])} rows; each note N1 final's):")
    w("")
    w("| row | file:line | unit | status | check: what it found | exemption (check: its whole failure message) | quote on the first cited line | validation_note |")
    w("|---|---|---|---|---|---|---|---|")
    for x in V["explained"]:
        w(f"| {x['row']} | {short_f[x['file']]}:{x['line']} | {cell(x['unit'])} | {x['status']} | "
          f"{cell(' | '.join(x['failures']), 300)} | "
          f"{cell('; '.join(f'{k}: {v}' for k, v in (x.get('exempts') or {}).items()), 200)} | "
          f"{cell(x.get('validation_quote') or '-', 120)} | {cell(x['validation_note'], 700)} |")
    w("")
    # ---------------------------------------------------------------- 9b
    w("### 9b. Not-figure rows, by reason")
    w("")
    w(f"{FN['n_not_figures']} units are not figures. Each row carries the mapper's reason; here they are grouped by the "
      "first group whose pattern the reason contains (`NR_REASON_GROUPS`; the last group takes the rest). The full "
      "reasons are in the JSON (`note_rows_final.rows[].not_figure_reason`).")
    w("")
    w("| group | rows | note / F1b / F2 | distinct reasons |")
    w("|---|---|---|---|")
    for g in FN["not_figure_summary"]:
        bf = g["by_file"]
        w(f"| {g['group']} | {g['n']} | {bf.get('RESEARCH-NOTE-v0_3-draft.md', 0)} / "
          f"{bf.get('2026-10-06_F1b_five-link-panels.svg', 0)} / {bf.get('2026-10-06_F2_macar-lineage-roc_post.svg', 0)} | "
          f"{g['n_distinct_reasons']} |")
    w("")
    # ---------------------------------------------------------------- 9c
    w("### 9c. The figures, one row each")
    w("")
    w("'status' is the row's (carried from the item raw or the ledger row; 'pass check' differs only where the ledger "
      "row's item raw gives no status in N1's vocabulary, or where a discrepant row is corrected in the note). 'corr.' "
      "names a correction recorded in 9i. 'source' is the row's first locator and its source value (cut here; whole "
      "in the JSON). 'check' = source-line level (A/B), the status check, and the ledger result. 'entry' = the commit "
      "at which the figure entered the record (record sources), and, for a figure whose only carrier is an audit raw, "
      "that raw's commit (9g).")
    w("")
    w("| row | file:line | unit | clause (cut) | status | pass check | corr. | maps to | source (cut) | check | entry (record / audit) |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for r in figs:
        k = f"{r['span']}#{r['seq']}"
        lc = r["validation"].get("locator", {})
        chk = ("A" if lc.get("level") == "A" else "B" if lc.get("level") == "B" else lc.get("result", "")[:24])
        if r.get("validation_exempts"):
            chk += " (exempt: " + ", ".join(r["validation_exempts"]) + ")"
        stc = r["validation"].get("status", {}).get("result", "")
        if stc and not stc.startswith("n/a"):
            chk += "; status " + stc.split(" (")[0]
        lg = r["validation"].get("ledger", {}).get("result", "")
        if lg and lg != "n/a":
            chk += "; ledger " + lg.split(" (")[0]
        e = ent.get(k, {})
        en = f"{short(e.get('record'))} / {short(e.get('audit'))}" if (e.get("record") or e.get("audit")) else "-"
        mp = r["maps_to"] + (f" {r['ledger_row']}" if r.get("ledger_row") else "")
        src = (r.get("locator") or "") + (" -- " + str(r.get("source_value")) if r.get("source_value") else "")
        pcs = r["pass_check_status"] if r["pass_check_status"] != r["status"] else (
            "passes (corrected in the note)" if k in FN["pass_check"]["corrected_in_note"] else "")
        w(f"| {k} | {fl(r)} | {cell(nr_unit(r))} | {cell(r.get('clause'), 140)} | {r['status']} | {pcs} | "
          f"{(r.get('correction') or {}).get('kind', '')} | {cell(mp, 80)} | {cell(src, 260)} | {cell(chk, 140)} | {en} |")
    w("")
    # ---------------------------------------------------------------- 9d
    P = FN["pass_check"]
    w("### 9d. The block's pass check (block :23) over the note's figures")
    w("")
    w("*Pass:* every figure is `reproduced` or `log-only` with a locator. *On fail:* a `not found` figure is cut from "
      "the note; a `discrepant` figure is corrected in the note to the reproduced value if the discrepancy is "
      "transcription, and is a STOP on that item if it is not. (AUDIT-note-release-v1_2.md@bbc9ffe:23)")
    w("")
    w("| pass-check status | note | F1b | F2 | all |")
    w("|---|---|---|---|---|")
    for st in sorted(P["by_status"], key=lambda x: -P["by_status"][x]):
        ks = P["rows_by_status"][st]
        c = {f: sum(1 for k in ks if byk[k]["note_file"] == f) for f in short_f}
        w(f"| {st} | {c['RESEARCH-NOTE-v0_3-draft.md']} | {c['2026-10-06_F1b_five-link-panels.svg']} | "
          f"{c['2026-10-06_F2_macar-lineage-roc_post.svg']} | {len(ks)} |")
    w("")
    met = P["passing"] == P["n_figures"]
    rl = P["rows_by_status"].get("reproduced", []) + P["rows_by_status"].get("log-only", [])
    pv = [k for k in rl if byk[k]["validation"]["locator"].get("result") == "pass"]
    pe = [k for k in rl if k not in pv and byk[k].get("validation_exempts")]
    ci = P["corrected_in_note"]
    w(f"**The pass condition is {'met' if met else 'NOT met'}.** {P['passing']} of {P['n_figures']} figures pass: "
      f"{len(rl)} reproduced or log-only, each with a locator ({len(pv)} pass the value check, {len(pe)} carry a named "
      f"exemption: {', '.join(pe) or 'none'}), and {len(ci)} discrepant rows corrected in the note "
      f"({', '.join(ci) or 'none'}; the rule in 10b). The rest, by the block's branches (each consequence is block "
      ":23's, applied to the row's own classification; Code decides none of them):")
    w("")
    w("**Discrepant**, by the branch each row's cause reads into (`NR_DISC`; the quoted words are asserted to occur in "
      "the cause). Every discrepant row here carries its item raw's own classification (round 5):")
    w("")
    for b, txt in NR_DISC_PATH.items():
        ks = [x["row"] for x in FN["discrepant"] if x["branch"] == b]
        if ks:
            w(f"- **{b}** ({len(ks)}: {', '.join(f'{k} {fl(byk[k])} {nr_unit(byk[k])!r}' for k in ks)}): {txt}.")
    w("")
    w("| row | file:line | unit | branch | quoted from the cause | ledger row | cause (cut) |")
    w("|---|---|---|---|---|---|---|")
    for x in FN["discrepant"]:
        w(f"| {x['row']} | {short_f[x['file']]}:{x['line']} | {cell(x['unit'])} | {x['branch']} | {cell(x['quoted'])} | "
          f"{cell(x.get('ledger_row') or '')} | {cell(x['cause'], 500)} |")
    w("")
    w(f"**Not found** ({len(FN['not_found'])}; block :23: cut from the note; the comment column carries the row's own "
      "condition):")
    w("")
    w("| row | file:line | unit | clause (cut) | cause / comment (cut) |")
    w("|---|---|---|---|---|")
    for x in FN["not_found"]:
        w(f"| {x['row']} | {short_f[x['file']]}:{x['line']} | {cell(x['unit'])} | {cell(x['clause'], 160)} | "
          f"{cell((x.get('cause') or '') + ' // ' + (x.get('comment') or ''), 600)} |")
    w("")
    if FN["not_run"]:
        w(f"**Not run** ({len(FN['not_run'])}: " + ", ".join(f"{x['row']} {short_f[x['file']]}:{x['line']} {x['unit']!r}"
                                                            for x in FN["not_run"]) + "). " + n19_text(FN))
    else:
        w("**Not run**: none. The five N19 rows (S1#145, S7#29, S7#33, S8#84, S8#85) were re-mapped in round 5 to N19's "
          "raw (the PI's routing 10). " + n19_text(FN))
    w("")
    cn = P["rows_by_status"].get("computed-new", [])
    w(f"**Computed-new** ({len(cn)}): no record line states the figure; its only source is an audit raw. Block :23 "
      "names no branch for them; they are in the record from the commit of the audit raw that computes them, which is "
      "why the tag must sit at or after it (9g). Rows: " + ", ".join(ref(k) for k in cn) + ".")
    w("")
    ov = [k for st, ks in P["rows_by_status"].items() if st.startswith("outside") for k in ks]
    if ov:
        w(f"**Status outside N1's vocabulary** ({len(ov)}): " + ", ".join(
            f"{k} ({nr_unit(byk[k])}, {fl(byk[k])}: {byk[k]['pass_check_status']})" for k in ov)
          + ". N1 assigns such a row no status (hard rule 4; provisional ledger note 2).")
        w("")
    lo = P["rows_by_status"].get("log-only", [])
    lo_ok = [k for k in lo if byk[k]["validation"]["locator"].get("result") == "pass"]
    note_txt = (REPO / FINAL_NOTE).read_text(encoding="utf-8")
    w(f"**Log-only** ({len(lo)}) pass, each with a locator ({len(lo_ok)} pass the value check; "
      f"{', '.join(k for k in lo if k not in lo_ok) or 'none'} carry a named exemption). Block :10 adds that the "
      f"note's sentence carrying a log-only figure is downgraded; the note's text contains the string 'log-only' "
      f"{note_txt.count('log-only')} times, so no sentence is marked. The wording is the design seat's (S5's span notes "
      "list its span's carrying sentences).")
    w("")
    # ---------------------------------------------------------------- 9e
    w("### 9e. The watch-list: what the note and the SVGs carry, per conditional STOP")
    w("")
    w("'matcher hits' are section 7's (value keys); 'text hits' are the watch-list's quoted strings searched in the "
      "three files; 'rows' are the note rows that carry or collide with the value, each status asserted at this run. "
      "The outcome is Code's summary of those rows and the mappers' span notes.")
    w("")
    w("| watch | what it ties to | matcher hits | text hits | rows | outcome |")
    w("|---|---|---|---|---|---|")
    for x in FN["watch"]:
        mh = "; ".join(f"{short_f[h['file']]}:{h['line']} {h['unit']!r}" + (f" -> {', '.join(h['rows'])}" if h.get("rows") else "")
                       for h in x["matcher_hits"]) or "none"
        th = "; ".join(f"{short_f[h['file']]}:{h['line']} {h['text']!r}" for h in x["text_hits"]) or "none"
        rr = "; ".join(f"{y['row']} {short_f[y['file']]}:{y['line']} {y['unit']!r} [{y['status']}]" for y in x["rows"]) or "-"
        w(f"| {cell(x['id'])} | {cell(x.get('what') or '', 220)} | {cell(mh, 400)} | {cell(th, 300)} | {cell(rr, 500)} | "
          f"{cell(x['outcome'], 900)} |")
    w("")
    # ---------------------------------------------------------------- 9f
    w("### 9f. Corrections routed to the note, and whether the note applies them (the mappers' span notes)")
    w("")
    w("Every span note, verbatim, by span (one exception: S3's redaction note, reworded in round 5 and annotated). "
      "'markers' lists, in order, the upper-case status markers the mapper wrote in the note (NOT APPLIED, PARTLY "
      "APPLIED, NOT CARRIED, CHOICE NOT MADE, OPEN, APPLIED, CORRECTED, FIRES, ...; `NR_NOTE_MARK_RE`). It is "
      "mechanical: a note can say 'not done' or 'not applied' in lower case and carry no marker, so read the note. "
      "'STOP' marks a note that uses the word, whatever it says about it. The notes are the mappers' (each after one "
      "adversarial check). N1 final's round-5 and round-6 annotations follow the note they qualify, marked 'N1 final'; "
      "where an annotation supersedes the note, the annotation holds, and where a round-6 annotation supersedes a "
      "round-5 one, the round-6 annotation holds.")
    w("")
    tc = {}
    for x in FN["span_notes"]:
        for m in x["markers"] or ["(none)"]:
            tc[m] = tc.get(m, 0) + 1
    w("Notes carrying each marker: " + "; ".join(f"{k} {v}" for k, v in sorted(tc.items(), key=lambda kv: -kv[1])) + ".")
    w("")
    w("| span | # | markers | STOP | note |")
    w("|---|---|---|---|---|")
    for x in FN["span_notes"]:
        w(f"| {x['span']} | {x['index']} | {', '.join(x['markers'])} | {'STOP' if x['stop'] else ''} | {cell(x['text'])} |")
        for a in x.get("annotations", []):
            w(f"| {x['span']} | {x['index']} (N1 final) | | | {cell(a)} |")
    w("")
    # ---------------------------------------------------------------- 9g
    T = FN["tag"]
    w("### 9g. The commit at which the last of the note's figures entered the record (the tag commit)")
    w("")
    w("Rule, per figure (not-found figures enter nothing): a figure mapped to a ledger row takes that row's entry from "
      "sections 2-5; a figure mapped to record lines takes, per record locator, the latest blamed commit of its lines, "
      "and over its locators the earliest (a fact enters with its first carrier); a figure mapped to an item-raw "
      "figure row takes that row's record sources; a computed-new figure (by its own status, its ledger row's or its "
      "item-raw row's; or, where no record entry is found, by the row's source value or the item-raw line it cites) "
      "enters with the audit raw: the blamed commit of the first audit-raw line it cites; and (round 5) a figure the "
      "audit reproduced from an external source, whose only carrier is an audit raw committed after the audit pin "
      "(N19's), enters with that raw. Over figures, the latest. Each figure's entry and how it was found are in the "
      "JSON (`note_rows_final.entries`).")
    w("")
    r1, r2, r3 = T["record_sources_only"], T["record_with_first_carriers"], T["including_audit_raws"]
    w(f"- **Over record sources only:** `{short(r1['commit'])}` ({r1['date']}), set by {', '.join(r1['rows'])}.")
    fcr = T["first_carrier_rows"]
    w(f"- **Counting a ledger-mapped figure at its first record carrier where that is later than its sources** "
      f"(section 5's third branch; the note carries the f1 CORR dose caveat as a statement at :111): "
      f"`{short(r2['commit'])}` ({r2['date']}), set by {', '.join(r2['rows'])}. Figures with such a carrier: "
      + ("; ".join(f"{x['row']} ({nr_unit(byk[x['row']])}, {fl(byk[x['row']])}): sources {short(x['record'])}, first "
                   f"carrier {short(x['first_carrier'])}" for x in fcr) or "none")
      + (". It does not move the candidate." if r2["commit"] == r1["commit"] else "."))
    ao = T.get("audit_only_rows", [])
    w(f"- **Including the audit raws** (the note carries {len(cn)} computed-new figures and {len(ao)} figures whose only "
      f"carrier is N19's raw): `{short(r3['commit'])}` ({r3['date']}), set by {len(r3['rows'])} figures "
      f"({', '.join(r3['rows'][:40])}{' ...' if len(r3['rows']) > 40 else ''}).")
    if ao:
        w("- Figures entering with N19's raw (round 5): " + "; ".join(
            f"{ref(x['row'])} at `{short(x['audit'])}` ({x['locator']})" for x in ao) + ".")
    if T["computed_without_audit"]:
        w(f"- Computed-new figures with no audit-raw line to blame ({', '.join(T['computed_without_audit'])}).")
    if T["unresolved_rows"]:
        ust = sorted({x["status"] for x in T["unresolved_rows"]})
        w(f"- Figures whose record entry the rule does not resolve ({len(T['unresolved_rows'])}; statuses "
          f"{', '.join(ust)}: " + ", ".join(ref(x["row"]) for x in T["unresolved_rows"])
          + "). Each cites an item raw that reproduces or reads it from the record at the pin (or, for a discrepant "
          "row, its reproduced value), so each entered at or before bbc9ffe. That bound is below the including-audit "
          f"candidate, so it cannot move it; the record-only candidate (`{short(r1['commit'])}`) holds only if each "
          "of these entered no later than that, which this rule does not establish.")
    w("")
    w(f"**Stated plainly: the last of the note's figures entered the record at `{r3['commit']}` ({r3['date']}).** "
      "Every figure the note and its SVGs carry is in the record at that commit (not-found figures are not, and are "
      "cut or reworded, 9d). It is an ancestor of HEAD at this run "
      f"(`{T['head_at_run'][:7]}`): {'yes' if T['candidate_is_ancestor_of_head'] else 'NO'}. The PI's resolution "
      "places the tag note-2026-10-v1 on the final audit commit, after N1 and N18; that commit descends from this one, "
      "so the tag holds every figure. Conditions that are the PI's to keep: (1) the tag commit also contains the note "
      "and both SVGs (untracked at this run; N18 hashes the final note); (2) N11's suite is re-run with --ref at the "
      "tag, since the 154/154 the note carries rests on N11's provisional, pre-tag PASS from a local clone (W6; "
      "results/raw/2026-10-08_note-N11-smoke.txt@02b6a61:745); (3) if F2 is re-rendered with d′/c/p annotations "
      "(9h O7), its new numerals get their own N1 pass; (4) if the note is edited after this run (the corrections in "
      "9h and 9i), its sha256 changes and this section covers the edited note only after a re-run against it.")
    w("")
    # ---------------------------------------------------------------- 9h
    w("### 9h. Open items for the PI and the design seat")
    w("")
    w("Each item names the rows it rests on (status asserted at this run), the corrections it rests on (each "
      "asserted to be on its row and declared in NR_CORRECTIONS; round 6) and the span notes it summarises (quote "
      "asserted). N1 declares no STOP of its own. Where an item says STOP, it is an item raw's STOP (O2, W8: N5's L102; "
      "O3, W3: N2vi's condition 3; O6: N2(ii)) or block :23's consequence of an item raw's own classification (O5, "
      "conditional: N6's gloss row, N6 @09c3a8c:493, :505); where a reading is N1's own (O1, O4, O10, and the MLP half "
      "of O17), the item says so.")
    w("")
    items = []
    for o in FN["open_items"]:
        rr = ", ".join(f"{y['row']} ({short_f[y['file']]}:{y['line']} {y['unit']!r}, {y['status']})" for y in o["rows"])
        items.append((int(o["id"][1:]), f"- **{o['id']}. {o['what']}.** {o['text']}" + (f" Rows: {rr}." if rr else "")
                      + (f" Corrections (9i): {', '.join(o['corrections'])}." if o.get("corrections") else "")
                      + (f" Span notes: {', '.join(o['span_notes'])}." if o["span_notes"] else "")))
    nap = sum(1 for x in FN["span_notes"] if any(m in NR_OPEN_MARKS for m in x["markers"]))
    items.append((16, f"- **O16. Wording, scope and disclosure routings the note has not applied.** At least {nap} "
                      "span notes in 9f carry an open marker (NOT APPLIED, PARTLY APPLIED, NOT CARRIED, CHOICE NOT MADE, "
                      "OPEN, ACTIVE or POSSIBLE STOP, FIRES); others say so in lower case (e.g. S10's 'not done in F2'). "
                      "The routings, with or without a marker, include the N4 cached-generation scope sentence, which no "
                      "line of the note carries; C16/C19 on G_c and the sham; C23/C24/C26/C27 on link 2; N17's "
                      "'untouched model' and 'custom kernel patch'; the D3 caveats. Who decides each is as the span note "
                      "says."))
    for _, t in sorted(items):
        w(t)
    w("")
    # ---------------------------------------------------------------- 9i
    w("### 9i. Corrections recorded separately from status (round 5)")
    w("")
    w("A correction is what the note's sentence should say, recorded beside the row's carried status, never as a "
      "status (10b). 'whose' says whether the reading is an item raw's or N1's own. Kind: wording, precision or scope. "
      "Since round 6 the script declares every correction, with its kind and whose reading it is (NR_CORRECTIONS, "
      "11b); the rows here are exactly those.")
    w("")
    w("| row | file:line | unit | status | kind | correction | whose | basis |")
    w("|---|---|---|---|---|---|---|---|")
    for x in FN["corrections"]:
        w(f"| {x['row']} | {short_f[x['file']]}:{x['line']} | {cell(x['unit'])} | {x['status']} | {x['kind']} | "
          f"{cell(x['text'], 900)} | {cell(x['whose'], 200)} | {cell(x.get('basis') or '', 200)} |")
    w("")
    render_round5(w, FN, byk, fl, ref)


def render_round5(w, FN, byk, fl, ref):
    """Section 10: round 5's values check (the final checker's findings, the PI's N19 routing, the rules, the rows
    changed, the mutation self-test and the guard's cases)."""
    ST = FN.get("self_test") or {}
    w("## 10. Values check, round 5 (N1 final fixes, 2026-10-09)")
    w("")
    w("An adversarial check of round 4 (the final checker: a re-run, a 50-row sample against the sources, 29 mutations "
      "of the rows file and a status cross-check over the 413 figures) found no value error and confirmed the tag "
      "result at 09c3a8c; it raised the nine findings below. The PI's routing of 2026-10-09 adds item 10. Each finding "
      "is Code's summary of the checker's; each disposition says what this round changed. The changes are this "
      "script's (the validator, the guard, the sections that render them) and the rows file's (named rows, each with "
      "a 'round5' record).")
    w("")
    w("### 10a. Findings and dispositions")
    w("")
    w("| # | severity | finding (Code's summary) | disposition |")
    w("|---|---|---|---|")
    for n, sev, f, d in NR_ROUND5:
        w(f"| {n} | {sev} | {cell(f)} | {cell(d)} |")
    w("")
    w("### 10b. Rules adopted this round")
    w("")
    for name, txt in NR_RULES:
        w(f"- **{name}.** {txt}")
    w("")
    w("### 10c. Rows changed in round 5")
    w("")
    w("Every row the round edited, with the fields it changed and their previous values (whole in the rows file, "
      "`rows[].round5`).")
    w("")
    w("| row | file:line | unit | status now | finding | fields changed (previous status where it changed) |")
    w("|---|---|---|---|---|---|")
    for x in FN["round5"]:
        chg = []
        for c in x["changed"]:
            chg.append(c["field"] + (f" (was {c['previous']})" if c["field"] in ("status", "maps_to", "kind") else ""))
        w(f"| {x['row']} | {fl(byk[x['row']])} | {cell(x['unit'])} | {x['status']} | {cell(', '.join(x['finding']))} | "
          f"{cell(', '.join(chg), 300)} |")
    w("")
    w("### 10d. Mutation self-test (run in memory at every run; the rows file is never changed)")
    w("")
    ms = ST.get("mutations", [])
    fixed = [x for x in ms if not x["origin"].startswith("family") and x["origin"] != "limit"]
    fam = [x for x in ms if x["origin"].startswith("family") and x["origin"] not in NR_ROW_FAMILIES]
    lim = [x for x in ms if x["origin"] == "limit"]
    lim_full = [x for x in lim if not x.get("expected")]
    nc = sum(1 for x in fixed if x["caught"] is True)
    by_o = {}
    for x in fixed:
        by_o[x["origin"]] = by_o.get(x["origin"], 0) + 1
    w(f"Each mutation changes the rows data in memory and the validation runs again; it is caught when a failure no "
      f"named exemption explains is reported, or when the run stops (a frozen hash, coverage, or an assertion on a row "
      f"the script names). A mutation that is not caught, or a known limit that is caught, stops the run before "
      f"anything is written. At this run: **{nc} of {len(fixed)}** fixed mutations caught ("
      + ", ".join(f"{v} {k}" for k, v in by_o.items()) + f"); **{sum(1 for x in fam if x['caught'] is True)} of "
      f"{sum(1 for x in fam if x['applied'])}** family members caught ({sum(1 for x in fam if not x['applied'])} not "
      f"applicable); **{sum(1 for x in lim_full if x['applied'] and x['caught'] is False)} of {len(lim_full)}** known "
      f"limits uncaught by a whole run, and **{sum(1 for x in lim if x.get('expected') and x['caught'] and not x['row_caught'])} "
      f"of {len(lim) - len(lim_full)}** row-level limits uncaught by the row checks and caught by the status freeze, as 10f "
      f"says. 'checker' = the final checker's 29 (round 5); 'checker 2' = n1chk2's that round 5 did not catch, or caught "
      f"only through this self-test's coupling (round 6); 'checker 3' = r6chk's that round 6 did not catch (round 7); "
      f"'round 7' = Code's. Round 7's families F-H, evaluated row by row, are in 12d. The last column says whether the "
      f"row checks alone catch the mutation (round 7; '-' where it changed no row).")
    w("")
    w("| id | origin | mutation | caught by (the first failure) | row checks |")
    w("|---|---|---|---|---|")
    for x in fixed:
        w(f"| {x['id']} | {x['origin']} | {cell(x['what'])} | {cell(x['by'], 300)} | "
          f"{'-' if x.get('row_caught') is None else 'caught' if x['row_caught'] else 'not caught'} |")
    w("")
    w("Families (round 6; generated from the rows at every run; every member in the JSON, `self_test.mutations`):")
    w("")
    w("| family | what each member does | members | caught | not applicable | checks that fail (members) |")
    w("|---|---|---|---|---|---|")
    fdesc = {"family A": "a computed-new row remapped to record, status log-only",
             "family B": "an uncorrected discrepant row given a forged corrected_in_note (a token tied to the note's "
                         "value on a cited line, quoted from the nearest correction wording before it if any)",
             "family C": "a declared correction removed", "family D": "a correction's 'whose' swapped (N1's <-> an item raw's)",
             "family E": "every exemption on an exempted row cut to the first half of its message"}
    for fname in sorted({x["origin"] for x in fam}):
        xs = [x for x in fam if x["origin"] == fname]
        ck = {}
        for x in xs:
            m = re.match(r"validation \[([^\]]*)\]", x["by"])
            for c in (m.group(1).split(", ") if m else (["run stops"] if x["by"].startswith("run stops") else [])):
                ck[c] = ck.get(c, 0) + 1
        w(f"| {fname[-1]} | {cell(fdesc.get(fname, ''))} | {len(xs)} | {sum(1 for x in xs if x['caught'] is True)} | "
          f"{sum(1 for x in xs if not x['applied'])} | {cell('; '.join(f'{k} {v}' for k, v in sorted(ck.items(), key=lambda kv: -kv[1])))} |")
    w("")
    w("Known limits (round 6; round 7 adds the level). A 'full' limit must stay uncaught by a whole run; a 'row' "
      "limit must stay uncaught by the row checks and be caught by the whole run (the status freeze). Otherwise 10f is "
      "wrong and the run stops:")
    w("")
    w("| id | level | mutation | whole run | row checks |")
    w("|---|---|---|---|---|")
    for x in lim:
        w(f"| {x['id']} | {'row' if x.get('expected') else 'full'} | {cell(x['what'])} | {cell(x['by'], 200)} | "
          f"{'-' if x.get('row_caught') is None else 'caught' if x['row_caught'] else 'not caught'} |")
    w("")
    w("### 10e. The overwrite guard's cases (run in memory; nothing is written)")
    w("")
    w("| case | expected | got |")
    w("|---|---|---|")
    for x in ST.get("guard", []):
        w(f"| {cell(x['case'])} | {x['expected']} | {x['got']}{'' if x['ok'] else ' (MISMATCH)'} |")
    w("")
    w("### 10f. What the validator still does not catch")
    w("")
    nb = sum(1 for r in FN["rows"] if r["kind"] == "figure" and r["validation"].get("locator", {}).get("level") == "B")
    fg = [x for x in ms if x["origin"] == "family G"]
    fh = [x for x in ms if x["origin"] == "family H"]
    w("Current at this run: round 7 rewrote bullets 3, 5 and 6, extended 4, and added 7 and 8 (12a).")
    w("")
    for t in NR_LIMITS:
        w("- " + t.format(nb=nb, g=sum(1 for x in fg if not x["row_caught"]), ng=len(fg),
                          h=sum(1 for x in fh if not x["row_caught"]), nh=len(fh)))
    w("")
    w("Determinism (two runs compared) and the redaction check are run by Code on this script's outputs, outside the "
      "script; their results are reported with the commit, not here.")
    w("")
    render_round6(w, FN, byk, fl)


def render_round6(w, FN, byk, fl):
    """Section 11: round 6 (the adversarial check of round 5, n1chk2): findings, dispositions, rules, rows changed."""
    w("## 11. Values check, round 6 (N1 final fixes, round 2, 2026-10-09)")
    w("")
    w("An adversarial check of round 5 (n1chk2: a re-run, the provisional mode against 6485da2, a 30-row sample "
      "against the sources, 59 mutations each run as its own process, a quotation scan and a redaction check) found "
      "no value error in the sample and confirmed both tag candidates; it found the validator weak (24 of its "
      "mutations passed) and raised the nine findings below. Each finding is Code's summary of the checker's; each "
      "disposition says what this round changed. The self-test (10d) runs every one of the checker's mutations that "
      "round 5 missed; the known limits that remain are in 10f.")
    w("")
    w("### 11a. Findings and dispositions")
    w("")
    w("| # | severity | finding (Code's summary) | disposition |")
    w("|---|---|---|---|")
    for n, sev, f, d in NR_ROUND6:
        w(f"| {n} | {sev} | {cell(f)} | {cell(d)} |")
    w("")
    w("### 11b. Rules adopted or amended this round")
    w("")
    for name, txt in NR_RULES6:
        w(f"- **{name}.** {txt}")
    w("")
    w("### 11c. Rows and span notes changed in round 6")
    w("")
    w("Every row the round edited, with the fields it changed (previous values whole in the rows file, "
      "`rows[].round6`), and the span-note annotations it added (9f, marked 'round 6').")
    w("")
    w("| row | file:line | unit | status now | finding | fields changed |")
    w("|---|---|---|---|---|---|")
    for x in FN.get("round6", []):
        w(f"| {x['row']} | {fl(byk[x['row']])} | {cell(x['unit'])} | {x['status']} | {cell(', '.join(x['finding']))} | "
          f"{cell(', '.join(c['field'] for c in x['changed']), 300)} |")
    w("")
    ann = [(x["span"], x["index"]) for x in FN["span_notes"] for a in x.get("annotations", []) if "round 6" in a]
    w("Span-note annotations added: " + ("; ".join(f"{sp} #{i}" for sp, i in ann) or "none") + ".")
    w("")
    render_round7(w, FN, byk, fl)


def render_round7(w, FN, byk, fl):
    """Section 12: round 7 (the strict check of round 6, r6chk): findings, dispositions, rules, rows changed, and the
    row-level families."""
    ST = FN.get("self_test") or {}
    ms = ST.get("mutations", [])
    w("## 12. Values check, round 7 (N1 final fixes, round 3, 2026-10-09)")
    w("")
    w("A strict check of round 6 (r6chk: 64 mutations, each run as its own process on a scratch copy of the rows file; "
      "an in-memory screen of status upgrades over every figure row; a re-run, the provisional mode against 6485da2, "
      "a 30-row sample against the sources, a quotation scan and a redaction check) found no value error in the "
      "sample and confirmed determinism and the section 10f/11 counts. It returned FAIL on two substantive findings "
      "(status upgrades the validator did not catch and 10f/11 did not disclose) and raised two minor ones. Each "
      "finding is Code's summary of the checker's; each disposition says what this round changed.")
    w("")
    w("### 12a. Findings and dispositions")
    w("")
    w("| # | severity | finding (Code's summary) | disposition |")
    w("|---|---|---|---|")
    for n, sev, f, d in NR_ROUND7:
        w(f"| {n} | {sev} | {cell(f)} | {cell(d)} |")
    w("")
    w("### 12b. Rules adopted or amended this round")
    w("")
    for name, txt in NR_RULES7:
        w(f"- **{name}.** {txt}")
    w("")
    w("### 12c. Rows changed in round 7")
    w("")
    w("Every row the round edited, with the fields it changed (previous values whole in the rows file, "
      "`rows[].round7`). Seven of them carry exemptions; their fingerprints are re-declared in NR_EXEMPT_FP, the "
      "exemptions themselves unchanged.")
    w("")
    w("| row | file:line | unit | status now | finding | fields changed |")
    w("|---|---|---|---|---|---|")
    for x in FN.get("round7", []):
        w(f"| {x['row']} | {fl(byk[x['row']])} | {cell(x['unit'])} | {x['status']} | {cell(', '.join(x['finding']))} | "
          f"{cell(', '.join(c['field'] for c in x['changed']), 300)} |")
    w("")
    w("### 12d. Families F-H (round 7; run at every run, row by row)")
    w("")
    w("Each member mutates one row; the row checks run on that row alone and the status freeze compares the row's "
      "freeze line, which is exactly what a whole run's validation reports for a one-row mutation. F is expected "
      "caught by the row checks alone. G and H are expected caught, and pick for each row the first candidate the row "
      "checks let through (the worst case), so their 'only by the freeze' column is the residue 10f bullet 3 states.")
    w("")
    w("| family | what each member does | members | caught | by the row checks | only by the status freeze |")
    w("|---|---|---|---|---|---|")
    fdesc = {"family F": "a figure row's status set to another term of the vocabulary (one field)",
             "family G": "a row whose status is computed-new, discrepant, not found or log-only given a locator "
                         "prefix with a reproduced item-raw figure row, and the status 'reproduced'",
             "family H": "the same rows given another ledger row whose item-raw rows are all reproduced, and the "
                         "status 'reproduced'"}
    for fam in NR_ROW_FAMILIES:
        xs = [x for x in ms if x["origin"] == fam]
        w(f"| {fam[-1]} | {cell(fdesc[fam])} | {len(xs)} | {sum(1 for x in xs if x['caught'])} | "
          f"{sum(1 for x in xs if x['row_caught'])} | {sum(1 for x in xs if x['caught'] and not x['row_caught'])} |")
    w("")
    for fam in ("family G", "family H"):
        xs = [x for x in ms if x["origin"] == fam and not x["row_caught"]]
        w(f"- {fam[0].upper() + fam[1:]}, rows the row checks let through ({len(xs)}; each caught by the status "
          f"freeze; the members in the JSON, `self_test.mutations`): "
          + (", ".join(x["id"].split(":", 1)[1] for x in xs) or "none") + ".")
    w("")
    w("Determinism (two runs compared), the provisional mode against 6485da2 and the redaction check are run by Code "
      "on this script's outputs, outside the script; their results are reported with the round, not here.")
    w("")


if __name__ == "__main__":
    main()
