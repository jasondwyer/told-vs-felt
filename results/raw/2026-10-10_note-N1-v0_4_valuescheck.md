# AUDIT-note-release v1.2 -- N1 round 8 (note v0.4 and the three 2026-10-09 SVGs): process record and values check

- Code stamp: 2026-10-10 13:41:56 UTC (date -u); HEAD `ea47e89aba16e6fe967d341be45289a505027aba` (the later commits on main are the concurrent G-CAL session's)
- Routed: the PI's rulings of 2026-10-09. Note v0.4 (sha256 `c4a05c781113cb2eceea0404d93ae723cc8dd32c2d8793d53cdb6067ee4ba9bc`) and the Digest seat's 2026-10-09 F1a, F1b and F2_post SVGs replace v0.3 and the 2026-10-06 SVGs; N1 and N18 are re-run on them. The rulings' four items (W3 accepted as transcription, not a STOP; the ablation d' routed to N2(v); the N2(ii) STOP resolved by rewording; the N12(i) STOP resolved) bind this round.
- Outputs: `scripts/audit_note_N1.py` (round 8, sha256 `52bfd8d4dff336702ba85c743f80fda26113565e584d37d5bf9a6d3e448af9f3`), `results/raw/2026-10-09_note-N1-v0_4-note-rows.json` (`e3d4f083aad815f53efdfefb045f2561ca4f9528305f21ee384deb73942b2c21`), `results/raw/2026-10-09_note-N1-v0_4-claims-ledger.md` (`e5cb92c00dd2fc502822f593ddf0d49f2f33d348aef7893c0240237878eef1fb`) and `.json` (`5f541463bad2311538eb07f8fe5047b31aa430afdac31f8dda5026a98d37ebff`). The v0.3 final ledger and rows file at `ef5c446` are unchanged. This file records how the round was built and checked; the ledger's section 10e holds every finding with its disposition.

## 1. Method

1. **Carry-over.** Note v0.4 is line-for-line with v0.3: 32 lines changed and the rest are identical. The 291 v0.3 rows on the identical lines were carried unchanged (note file renamed), and N1's own validator passed every one before any mapping began.
2. **Mapping.** Ten chains, one per group of changed lines or per SVG. In each, a mapper wrote the rows, an adversarial checker re-opened every cited source, and the mapper revised. Rows that are the same unit and claim as a v0.3 row keep the v0.3 key.

| chain | scope | final rows | checker findings (substantive) | missed units |
|---|---|---|---|---|
| C1 | note line 3 | 152 | 11 (1) | 0 |
| C2 | note lines 1, 20, 25-27, 29 | 32 | 6 (1) | 0 |
| C3 | note lines 48, 58, 60, 66, 70, 74, 76, 78 | 92 | 6 (1) | 0 |
| C4 | note lines 84-86, 88 | 47 | 6 (0) | 0 |
| C5 | note lines 92, 96, 98, 100 | 85 | 4 (1) | 0 |
| C6 | note lines 111, 136, 142, 144, 146, 170, 172 | 54 | 5 (1) | 0 |
| C7 | note lines 208, 210 | 33 | 9 (2) | 0 |
| C8 | F1a (2026-10-09_F1a_headline-strip.svg) | 39 | 6 (0) | 0 |
| C9 | F1b (2026-10-09_F1b_five-link-panels.svg) | 107 | 4 (0) | 0 |
| C10 | F2 (2026-10-09_F2_macar-lineage-roc_post.svg) | 102 | 6 (0) | 0 |

3. **Script.** `scripts/audit_note_N1.py` was refactored into note-version profiles (v0_3, v0_4), with a `--dev-report` mode. Its acceptance test: the v0_3 profile reproduces the committed v0.3 final ledger (`ef5c446`) byte for byte apart from identity, stamp and HEAD lines, and the two N2 working-tree fields that changed at `e60b633`. The refactor's checker returned 8 findings (5 substantive), all applied before integration. Round 8 adds a declared, sourced path for the four R1 rows (the PI's ruling 1), branch TS, the audit-outcome raw class, parser-bound row tags, and run-level gates for open items, mutations and hashes.
4. **Integration and checks.** The v0_4 profile's tables (discrepant branches, watch-list outcomes, open items, corrections, exemptions, mutations, frozen hashes) were filled from the rows and the chains' span notes. Three adversarial lenses checked every round: row values (every cited line re-opened), ledger content against the rulings and the span notes, and script integrity (mutations, freezes, guard, v0_3 regression).

| round | row values | ledger content | script integrity |
|---|---|---|---|
| 1 (integration) | FAIL: 8 (2 substantive) | FAIL: 15 (6 substantive) | FAIL: 5 (2 substantive) |
| 2 | FAIL: 8 (1 substantive) | FAIL: 10 (2 substantive) | FAIL: 6 (1 substantive) |
| 3 | FAIL: 3 (1 substantive) | FAIL: 10 (2 substantive) | FAIL: 6 (2 substantive) |
| 4 | FAIL: 3 (1 substantive) | FAIL: 6 (1 substantive) | PASS: 3 (0 substantive) |
| 5 | FAIL: 3 (1 substantive) | FAIL: 4 (2 substantive) | PASS: 2 (0 substantive) |
| 6 | FAIL: 4 (1 substantive) | FAIL: 5 (1 substantive) | FAIL: 3 (1 substantive) |
| 7 | PASS: 2 (0 substantive) | FAIL: 3 (1 substantive) | PASS: 3 (0 substantive) |
| 8 | (not run: passed in round 7) | PASS: 3 (0 substantive) | PASS: 1 (0 substantive) |

Round numbers are the ledger's (10e): round 1 is the integration's first check, rounds 2-8 are the fix rounds, each followed by its recheck.

## 2. Code's decisions during the round (each recorded in 10e with its effect)

- D1: no figure that only a scratch computation supports appears in the rows, tables or ledger (ledger 27); the :98 scope correction rests on N2's tabulated rows only.
- D2: the R1 path binds to the source's own clause on N2vi row 8 ('source v1 text 0.000'), declared per row.
- D3: W5's condition 4 (N2vi @09c3a8c:620) is applied to F2 as well as the note; F2 states no eight-concept premise, so its 800/80-derived figures stay with O18 (the Digest seat's).
- D4: every span note is mapped to a disposition (closed, or carried by an open item), built and asserted by the script.
- D5 (fix round 4): D1 extended to every figure scratch arithmetic derives from committed values when no committed file prints it.
- D6 (fix rounds 4-5): condition 4 reaches every figure computed at an assumed n; a figure meets it when it holds at every premise its sentence admits.
- D7 / E1 (fix rounds 5-6): widths, bounds, means, medians, ratios, conversions, quotients and partial counts that no committed line prints are withdrawn and restated from printed values.
- E2-E5 (fix round 6): one W5 test stated once; O16 stored in the JSON; whitelists (not blacklists) for the R1 clause and the row tags; JSON carriers cited by entry and field.
- F1-F4 (fix round 7): the remaining derived figures withdrawn; tags bound through the locator parser; forged-input edges either closed or declared in 10d.
- G1 (fix round 8): W5 reads 'at the precision written'. Line 3's and :208's '1-2' therefore meet condition 4 (800/80's +0.611 is 1 at whole-number precision); their low-end scope residue stays N1's correction under O4.

## 3. Outcome

- Rows: 1034 (545 figures). Validation: 0 unexplained failures; the self-test and the guard cases all as expected (the ledger's 9a and 10a).
- The block's pass condition (:23) is not met: 397 of 545 figures pass (the reproduced and log-only rows, and 6 corrected rows in branch C, four of them under the PI's ruling 1). By status: computed-new 108, log-only 109, not found 11, discrepant 34, reproduced 282, outside N1's vocabulary (other, L089) 1.
  The rest are computed-new, discrepant in branches T, TS and NT, or not found (to be cut, or admitted by the PI as citations, 9h O8). The ledger's 9d gives every list.
- The commit at which the last of the note's figures entered the record: `e60b633142f0ff5ec574da022a7117d18711e32b` (set by S1#173, S5#72, S5#77: the ablation d' of the PI's ruling 2); over record sources only, `05c4636`.
- Open items: 27 (9h), each naming whose call it is.

## 4. Residual minors from the final verification, carried open (not applied)

Both lenses of the last verification returned PASS. Their minor findings were not applied, to avoid another rebuild of the frozen rows file; none changes a status, a value, a branch or a verdict:

- History record (ledger lens): three statements in 10e (the D6 bullet, fix round 5's Ledger 3 bullet, and one sentence of fix round 6's E2 bullet) still give the superseded verdict on line 3's and :208's '1-2' without a fix-round-8 marker. The live verdicts in 4e, 9e, 9f, 9h and the rows are consistent with G1.
- Wording (ledger lens): S6#19's source value calls +0.013514 'exact'; it is 19/37 - 1/2 at six decimals, as N4 prints it (results/raw/2026-10-08_note-N4-e2a.md@09c3a8c:109).
- Wording (ledger lens): 10e's G1 bullet calls F2's '+0.15 to +1.5' a case G1 does not settle; G1 does settle it (it names F2's far ends, read end by end), and the bullet's '(+0.2 to +1.5)' rounds a written end. The verdict is the same either way.
- Forged inputs (script lens): HTML entities, inline HTML and Markdown emphasis that render as a row key pass the row-tag check when a forger writes them into a field; the nine real fields that check reads carry none, and 10d does not yet declare them.

## 5. For the PI

- The v0_3 profile keeps v0.3's behaviour for a partial `--note` run (it can still write a final ledger without checking SVG coverage); the v0_4 profile refuses such a run. Changing v0_3 would change a committed round's behaviour, so it is left as it was.
- The ledger's 9g conditions on the tag are the PI's: the tag commit holds the note and the three SVGs; N11 is re-run at the tag; a re-rendered SVG or an edited note gets its own N1 pass first.
