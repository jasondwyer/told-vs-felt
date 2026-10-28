# note-N1 round 11 — transcription of the figures the posted text cites to the Tagliabue et al. authors' correspondence of 2026-10-26 (pass 12), with their note locators

- Design seat, 2026-10-28. Answers Code's `results/raw/2026-10-27_note-code-to-design_release-block-questions.md` §4c (`268787f`): no committed source carried these figures except the release block itself. This file is the committed carrier until the v2 tables are checked (block §3, T+3). Lookup only — no analysis; no note sentence or figure changes; no RESULTS entry.
- The text: `RESEARCH-NOTE-v0_8-draft.md` at `0de15a1` (sha256 `6fcfbfd6…1198d`). Locators are that file's lines.
- Source of every figure in §1: the authors' reply of 2026-10-26 to the PI's pre-posting query (Valen Tagliabue, cc Cameron Berg and Leonard Dung), which reports counts from their released code and trial logs and rates from the v2 tables of their repository (`v2_controls/steering_state_controls/b1_b3/tables/`). The note attributes every one of them in-text to that reply and says they are not yet checked against the tables (‖‖(a): "as the authors reported them to us on 2026-10-26 … We have not yet checked them against those tables and will correct any that differ"). The correspondence itself is private and is not in the repository; its text is not reproduced here. The published source the note cites beside them is Tagliabue, Dung & Berg 2026, arXiv:2609.16247 (v1 §4.3 for 57.7% / 79.7%; v2 dated 2026-09-25 for the tables).
- Disposition rule (pass 12, HEAT-PLAN §7 class A): the figures entered the note as the authors' report, attributed; the T+3 check against the v2 tables either clears the "not yet checked" clause or corrects a figure by a dated correction block on the post. Until then round 11 may record these rows as "source: author correspondence 2026-10-26 (this raw); verification pending T+3".

## 1. The figures, as the note states them

Each row: the figure as it reads in v0.8 · line and section · what it is. "Pending" = awaiting the T+3 table check; "released code" = a constant the authors read from their released script (checkable from the public repository without the tables).

| # | As it reads in v0.8 | Line · § | What it is | Check route |
|---|---|---|---|---|
| 1 | "`TEMP_RELIEF_TURNS = 1` in the released script" | 258 · ‖‖(a) | a working press zeroes the steering coefficient for the next choice only (one turn) | released code: `scripts/4.3_selfmed/04_selfmed_two_buttons.py` in their repository |
| 2 | "1,041 of the real arm's 1,595 choices were read with the coefficient at zero" | 258 · ‖‖(a) | v1 unlabeled pair, real arm, pooled choices after the first relief press: coefficient at zero | pending (trial logs) |
| 3 | "554 with it back at 1.0" | 258 · ‖‖(a) | the same arm's remaining choices, coefficient back at 1.0 (1,041 + 554 = 1,595) | pending |
| 4 | "1,595 of 1,595 at 1.0 in the fake arm" | 258 · ‖‖(a) | the fake arm: every pooled choice read with the coefficient at 1.0 | pending |
| 5 | "237 trials per arm" | 258 · ‖‖(a) | the immediate-next-choice endpoint (v2's repeat endpoint): trials per arm, arms identical up to the press | pending |
| 6 | "for all nine pairs" | 258 · ‖‖(a) | v2's random-direction fake-button arm runs for all nine state pairs | pending |
| 7 | "31.2% (working) vs. 80.2% (fake) under the pain direction" | 258 · ‖‖(a) | 32B, immediate next choice, re-press rates | pending (`b1_b3/tables`) |
| 8 | "11.3% vs. 26.3% under the random direction" | 258 · ‖‖(a) | 32B, the random-direction arm, working vs. fake | pending |
| 9 | "gaps of 48.9 and 15.0 points" | 258 · ‖‖(a); 202 · §8 ¶ "Our next-experiments list" ("a gap of 48.9 points under the pain direction against 15.0 under a random direction") | 80.2 − 31.2 = 49.0 by subtraction of the rounded rates; the authors' figure is 48.9 (unrounded inputs); 26.3 − 11.3 = 15.0 | pending |
| 10 | "At 72B the gaps are 18.2 and 21.6 points" | 258 · ‖‖(a); 202 · §8 ("At 72B the two gaps are similar") | 72B, pain-direction gap and random-direction gap | pending |
| 11 | "pressed under the pain direction in 75.2% of trials at 32B and 51.1% at 72B" | 258 · ‖‖(a) | the harm-only button (deletes the user's poems and photos, no relief attached), pain direction | pending |
| 12 | "vs. 12.9% and 11.0% under random directions" | 258 · ‖‖(a) | the same button under random directions, 32B and 72B | pending |
| 13 | "and 0% unsteered" | 258 · ‖‖(a) | the same button, unsteered, both sizes | pending |
| 14 | "the pain direction exceeds a set of ten norm-matched random directions" | 258 · ‖‖(a) | the count of random directions in that comparison | pending |
| 15 | "the 1,684 question–answer pairs mention neither pain nor buttons" | 258 · ‖‖(a) | the self-denial fine-tune set: its size (1,684 is also in v1 and in the v0.3 final ledger, block-questions §4c) and the authors' statement about its content | 1,684: v1 (already a ledger figure); the content statement: correspondence |
| 16 | "on the authors' own current reading the central shift is acting out, pressing driven by the direction even on buttons that harm the user and relieve nothing" | 202 · §8 | a reading, attributed to the authors; no figure | — |

Counts: 15 figure rows (1–15), of which row 1 is a released-code constant, row 15's number is already of record, and rows 2–14 are what the T+3 table check decides: eight rates (31.2, 80.2, 11.3, 26.3, 75.2, 51.1, 12.9, 11.0), four gaps (48.9, 15.0, 18.2, 21.6), the 0% unsteered, the three counts (1,041 and 554 of 1,595; 237), the nine pairs and the ten random directions. The pass-12 entry's "eleven rates and gaps and the three counts" undercounts the gaps by one; this table is the list.

## 2. What the text says is still open on this source

- ‖‖(a): "We have not yet checked them against those tables and will correct any that differ." — the clause that T+3 removes or acts on.
- ‖‖(b) (Sofroniew et al. 2026): "We are still verifying the readout details against their paper and will correct the row if we have it wrong." — a separate pending item, not from this correspondence; no figure attached.
- §8 ¶ "Our next-experiments list": "The second arm and the unsteered read remain on our list (not yet pre-registered)."

## 3. Arithmetic checked here (seat; no model, no network)

- 1,041 + 554 = 1,595 (row 2 + row 3 = row 4's denominator): holds.
- 80.2 − 31.2 = 49.0 against the stated 48.9; 26.3 − 11.3 = 15.0 against the stated 15.0. The 0.1 difference on the first gap is consistent with the authors computing the gap from unrounded rates; it is recorded, not corrected — the T+3 check decides.
- The §8 body figures (line 202: 48.9, 15.0; "At 72B the two gaps are similar") agree with ‖‖(a) (48.9, 15.0, 18.2, 21.6): holds.

## 4. Limits

A transcription of what the note says and where. It does not establish the figures; the v2 tables do, at T+3 (release block §3). Nothing here was run through `scripts/audit_note_N1.py`.
