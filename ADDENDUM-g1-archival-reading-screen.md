# ADDENDUM-g1 — per-stage archival-reading screen (appended to PROPOSAL-g B3)

**Status:** DRAFT v1.0, 2026-08-20, design instance. A registered
addition to a locked pre-registration (`72b09a9`); binds only when
Jason commits it, and changes nothing upstream of B3. Runs AFTER B3
completes, on B3's own session records; no new stimuli, no new
sessions.

## Purpose

S1 located the Qwen break at recognition. B3's verdicts on the OLMo
series should therefore ship with each stage's recognition status
attached, so that any pattern of nulls (or a positive) arrives
localized rather than ambiguous.

## Design

After B3's last session, per stage: the S1 ladder's four most
informative cells — detection framing × {k=1, k=2} × {zero-shot,
few-shot(m=8, fit-half exemplars)} — run as logit-level 2AFC over
that stage's own B3 records, both position orders, all reads vanilla
state-free forwards (two-horns satisfied trivially, as in S1).

- **n per cell:** the maximum the stage's B3 corpus supports,
  **declared before scoring** (the S1 lesson, kept).
- **Resolution statement, pre-declared:** at B3-scale corpora the
  screen may separate only the extremes (chance vs probe-parity
  analog); intermediate results report as the localization curve and
  adjudicate nothing.
- **Probe-side anchor:** the stage-matched embedding probe (A3/A4
  lineage) is trained on that stage's fit-half records and scored on
  the same val items the judge sees, so judge and probe are compared
  on identical materials per stage.

## Registered readings

| B3 outcome | g1 outcome | Reading |
|---|---|---|
| Null at stage s | Reading absent at s | Recognition-blind null — localized, S1-consistent. |
| Null at stage s | Reading PRESENT at s | That stage reads and does not act: "reads but doesn't care," resurrected per-stage — the sharpest dissociation available to this program. |
| Positive at stage s | Reading present at s | Coupling story coherent; recognition feeds valuation feeds choice. |
| Positive at stage s | Reading absent at s | Apparatus flag first (a preference without a discriminative channel is a two-horns alarm, not a finding). |

## Cost and reporting

Minutes of forwards per stage on the box (or laptop over synced
records); `data/olmo/g1_archival_{stage}.json`; raw logs; dated
entries; one table for the Draftsman.

## Approval

Commit = approval. No CLAUDE.md change required; B3's verdict
criteria are untouched (this screen is attached reporting, never a
verdict input).
