#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N1: the claims ledger (PROVISIONAL).

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

Read-only on the record. git runs only in this repository (never inside
jlens-qwen36/). Writes only --out and --json-out. No model, no network, no
randomness; stdlib only.

Usage (from the repository root):
  jlens-qwen36/.venv/bin/python scripts/audit_note_N1.py \
      [--out results/raw/2026-10-08_note-N1-claims-ledger.md] \
      [--json-out results/raw/2026-10-08_note-N1-claims-ledger.json] \
      [--note RESEARCH-NOTE-v0_2-draft.md --note F1.svg --note F2.svg]
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


def full(rev: str) -> str:
    return git("rev-parse", rev + "^{commit}").strip()


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


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="results/raw/2026-10-08_note-N1-claims-ledger.md")
    ap.add_argument("--json-out", default="results/raw/2026-10-08_note-N1-claims-ledger.json")
    ap.add_argument("--note", action="append", default=[],
                    help="note markdown or F1/F2 SVG to match against the ledger (repeatable)")
    a = ap.parse_args()

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
        item="N1", title="claims ledger", provisional=True,
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
    w(f"- Note at root on this run: {'present' if J['note_present_at_root'] else 'absent'}; --note arguments: "
      f"{J['note_args'] or 'none'}")
    w("- Item raws (read at the audit pin; working tree equal to the pinned blob):")
    for p, d in J["item_raws"].items():
        w(f"  - `{p}` sha256 `{d['sha256_at_audit_pin'][:16]}` working tree equal: {d['working_tree_equal']}")
    w("")
    w("Status vocabulary (block :22, plus the item raws' computed-new): reproduced | log-only | not found | discrepant | "
      "computed-new; 'not run' for N19. Every status below is the item raw's, carried verbatim with its cause; this "
      "ledger reclassifies nothing. Where an item raw gives no status in that vocabulary, the row says so.")
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
    if J["note_mode"] is None:
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
    return "\n".join(o) + "\n"


if __name__ == "__main__":
    main()
