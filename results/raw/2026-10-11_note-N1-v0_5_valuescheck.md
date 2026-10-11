# AUDIT-note-release v1.2 -- N1 round 9 (note v0.5 and the three 2026-10-10 renders): process record and values check

- Code stamp: 2026-10-11 09:34:10 UTC (date -u); HEAD `84801cb5fad5f7bf06b5213fdb8bf9a55e369d6b` (later commits on main than the audit's are the concurrent G-CAL session's)
- Routed: the PI's rulings of 2026-10-10 (items 5-10, ruling 9 as corrected) and the round-9 inputs: note v0.5 (sha256 `4c2810e1f2be012e2a419d9ef3a154c0e1f4abb5dde5caac067d9ec361e4ce5b`) and the Digest seat's 2026-10-10 F1a (`6ffad6cd971aabdc70d7b684a6408988c9a05e5445125d3ce61a78557405cee6`), F1b (`6fcb060f6a2cf2c0ce1f5374c3267c5cec67304994a9967e49a2afaffcf6113e`) and F2 (`81b13e805e64e6a9534e65e6dfeb50d6c6a65cf3d8b02b9cb3a1e36852e5ac4e`), each hashed as filed and equal to the routed value. Each render carries a C2PA content-credentials element (`<c2pa:manifest>`, 7,684 base64 characters, inside `<metadata>`); N1 reads only an SVG's text, tspan, title and desc content, so the element is never a numeral source (the ledger's `note_rows_final.pass_check.round9.c2pa_excluded`).
- Outputs: `scripts/audit_note_N1.py` (round 9, sha256 `0c5a98f04b33221d31b3db1c46a6f3eeae8b69fe425d018acf6e1a145a942400`), `results/raw/2026-10-10_note-N1-v0_5-note-rows.json` (`0af1e9fe6967553d42338abcd1bbcc69f16f90f11008323f96f967acf548da61`), `results/raw/2026-10-10_note-N1-v0_5-claims-ledger.md` (`b52c78bbd456f3a8ed5f752e87b969c4b4bdc0fbc458462e4a132e3b9983e823`) and `.json` (`6593efeee5eafc52aaa851aa7e79ffc99ba008d6be7a0315c90b9a320b57fe58`). Tier 1 is committed at `84801cb`. The v0.3 and v0.4 ledgers (`ef5c446`, `fd2b136`) are unchanged, and the v0_3 and v0_4 profiles still reproduce them apart from identity, stamp and HEAD lines and working-tree fields. The ledger's round-9 values-check section holds every finding with its disposition.

## 1. Method

1. **Tier 1 (ruling 9).** N4, N5, N6, N7, N8 and N17 re-pointed at the patched preprint, each prepared, checked, fixed and rechecked, then run of record and committed at `84801cb` (every figure status unchanged; seven findings on the patch for the design seat).

| script | preparation check (findings, substantive) | recheck (findings, substantive) |
|---|---|---|
| N4 | 6 (1) | 3 (1) -> fixed |
| N5 | 5 (0) | 2 (0) |
| N6 | 6 (0) | 4 (1) -> fixed |
| N7 | 4 (0) | 1 (0) |
| N8 | 7 (2) | 5 (0) |
| N17 | 6 (0) | 3 (0) |

2. **Note v0.5.** Line-for-line with v0.4: the 198 rows on its 176 unchanged lines were carried unchanged; eight chains (D1-D8) mapped the 43 changed lines (mapper, adversarial checker, revision). **Renders.** Three chains (E1 F1a, E2 F1b, E3 F2) mapped every text node against their 2026-10-09 predecessors.

| chain | final rows | checker findings (substantive) | missed units |
|---|---|---|---|
| D1 | 178 | 12 (4) | 0 |
| D2 | 45 | 6 (1) | 0 |
| D3 | 100 | 5 (1) | 1 |
| D4 | 64 | 4 (1) | 0 |
| D5 | 112 | 5 (0) | 0 |
| D6 | 82 | 4 (0) | 0 |
| D7 | 68 | 10 (1) | 1 |
| D8 | 74 | 8 (1) | 0 |
| E1 | 45 | 5 (2) | 0 |
| E2 | 116 | 6 (0) | 0 |
| E3 | 143 | 3 (0) | 0 |

3. **Machinery (rulings 5-8).** Checks for scope_corrected_in_note (ruling 6), discharged (ruling 7) and admitted_citation (ruling 8), and the pass logic of ruling 5, in a v0_5 profile; v0_3 and v0_4 untouched. Checked (8 findings, 4 substantive), fixed, rechecked (4, 1), fixed. A dry run on v0.4's committed rows under the round-9 rules passes 535 of 545, Code's projection.
4. **Integration and checks.** Three adversarial lenses each round: row values, ledger content, script integrity.

| round | row values | ledger content | script integrity |
|---|---|---|---|
| 1 (integration) | FAIL: 9 (3 substantive) | FAIL: 9 (3 substantive) | PASS: 5 (0 substantive) |
| 2 | FAIL: 5 (2 substantive) | FAIL: 9 (3 substantive) | PASS: 3 (0 substantive) |
| 3 | PASS: 1 (0 substantive) | PASS: 4 (0 substantive) | PASS: 3 (0 substantive) |

## 2. Outcome

- Rows 1225 (615 figures). Validation: 0 unexplained failures; the self-test and the guard cases all as expected (the ledger's 9a and 10a).
- **Block :23's pass condition is not met: 600 of 615 figures pass.** By status: computed-new 145, not found 9, reproduced 314, log-only 124, discrepant 23.
  - Passing under the PI's rulings of 2026-10-10: ruling 5 135; ruling 6 13 (S1#134, S1#214, S1#215, S1#216, S4#4, S4#5, S4#38, S4#39, S4#10, S4#11, S4#31, S4#32, S4#33); ruling 7 2 (S6#102, S6#103); ruling 8 6 (S3#129, S7#19, S7#20, S7#25, S7#28, S7#82); and 6 corrected rows in branch C (R1 among them).
  - Not passing, not found (3): S1#260; S2#130; S7#91 (the ledger's 9h O8).
  - Open, not ruled (12): S5#106; S5#116; S5#117; S7#97; S8#136; S8#137; S8#78; S8#139; S8#122; S11#18; S11#19; S10#137. Each row's reason is in the ledger's 9d and JSON (`note_rows_final.pass_check.round9.open_not_ruled`): O30 (the status reading of 'fifty'), O11 (W5 at :98 and :208) and O13 (whether ruling 6 reaches a render's TS rows).
- The commit at which the last of the note's figures entered the record, including audit raws: `fd2b1364dea83a3433791cf4a751f05966f9aaf5` (set by S1#236, S1#237); over record sources only, `05c4636`.
- Open items: 31 (9h), each naming whose call it is.

## 3. Residual minors from the final check, carried open (not applied)

All three lenses of the last check returned PASS, with 8 minor findings. They were not applied, to avoid another rebuild of the frozen rows file; none changes a status, a value, a branch, a pass or a verdict:

- [row values] S8#136's comment still states, in the present tense, the 2026-10-09 render's precedent that F2 states no eight-concept premise; the 2026-10-10 render states it (nodes 97-98). S8#137 was corrected in fix round 2, S8#136 was not.
- [ledger content] S7 span notes 0 and 14 say all 23 computed-new rows pass ruling 5, but S7#97 ('fifty') is held open under O30; neither note is annotated, and O30's list of span notes omits them.
- [ledger content] S5 span note 24 (OPEN) still describes the 2026-10-09 F2 (R1's point at 0.003; the ~800/~80 rows S10#66 and S10#67), which the 2026-10-10 render resolves; it is not annotated.
- [ledger content] O25's list of README-NOTE lines stale against round 9 omits section 8's figures-commit line and its tag conditions; README-NOTE is regenerated in the commit that adds this file.
- [ledger content] O30 does not state the W5 consequence for :164's '1.2': if 'fifty' is cut, that figure's only stated premise goes with it.
- [script integrity] On a case-insensitive volume the overwrite guard compares realpath prefixes case-sensitively, so a path typed in another case counts as outside the repository; a forged-input edge, no real run affected.
- [script integrity] Section 10b's family column prints '6', '7' and '8' for families R6-R8 (the name's last character).
- [script integrity] No v0_5 self-test member exercises the ruling-7 check's branch for the field on a non-NT row, because v0.5 has no branch-T row; the check rejects it when exercised directly.

## 4. For the PI

- The 15 figures not passing need rulings, not more audit work: the three not-found units (O8), the reading of 'fifty' (O30), the W5 readings at :98 and :208 (O11), and whether ruling 6 reaches F1a's two TS rows (O13). The tag waits on them and on the N12 pre-flip re-scan decisions.
