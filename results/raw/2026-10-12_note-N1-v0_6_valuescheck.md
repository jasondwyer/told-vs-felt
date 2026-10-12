# AUDIT-note-release v1.2 -- N1 round 10 (note v0.6 and the unchanged 2026-10-10 renders): process record and values check

- Code stamp: 2026-10-12 10:38:29 UTC (date -u); HEAD `d6bb7905855021432cc59e1538e3599a1c8d5d2a` (later commits on main than the audit's are the concurrent G-CAL session's)
- Routed: the PI's rulings 11-13 of 2026-10-12 and the round-10 inputs: note v0.6 (sha256 `2c7e1cf526f6dfe737c6246cf137f1ae9bc18816846e8329de2f9c3c04426fbb`, hashed as filed and equal to the routed value; line-for-line with v0.5, lines 1, 3, 60, 98, 111 and 208 changed) and the preprint PREPRINT-v1_0-draft.md, patch v7 (sha256 `d9635ca24d32dcba193cd9aade273de2679c99c5c2218787b410e793a42d1fe6`, equal to the routed value; lines 1, 109, 172 and 182 changed against patch v6, whose copy archive/PREPRINT-v1_0-draft.pre-patch-v7.md hashes to round 9's 0f4ba501...6c22). The three 2026-10-10 renders are unchanged and still hash to the values the PI routed on 2026-10-10.
- Outputs: `scripts/audit_note_N1.py` (round 10, sha256 `1daefe30844f213c40229100ee6cf36b4e040070fd9b8f880a8d63061dec661f`), `results/raw/2026-10-12_note-N1-v0_6-note-rows.json` (`deab5fb40e5d2a153a4b93f7c8611a584a40474a594ff25728f87060dcf3938b`), `results/raw/2026-10-12_note-N1-v0_6-claims-ledger.md` (`460c6f71e4dbbc1cd671c4b72b8bb308f7854cb4b5384aa6002de386f0b2da81`) and `.json` (`e746ecd8aa87c8270a2856139c68b2b5aac4bfcd7010c7cc84de61cc41094b5c`). Round 10's Tier 1 is committed at `d6bb790`. The v0.3, v0.4 and v0.5 ledgers (`ef5c446`, `fd2b136`, `fa1b41e`) are unchanged, and the v0_3, v0_4 and v0_5 profiles still reproduce them apart from identity, stamp and HEAD lines and working-tree fields. The ledger's round-10 values-check section (10e) holds every finding with its disposition.

## 1. Method

1. **Tier 1 (the PI's routing of 2026-10-12).** N4, N5, N6, N7, N8 and N17 re-pointed at patch v7, each prepared, checked, fixed and (where the check was substantive) rechecked; a last pass gave N5's P10-2 the pinned carrier of the three-letter clause and applied the rechecks' minors; then run of record and committed at `d6bb790` (every figure status unchanged).

| script | check (findings, substantive) | recheck (findings, substantive) | last pass check |
|---|---|---|---|
| N4 | 4 (0) -> fixed | not needed | - |
| N5 | 5 (1) -> fixed | 4 (0) | 3 (0) -> fixed |
| N6 | 3 (0) -> fixed | not needed | - |
| N7 | 1 (0) -> fixed | not needed | - |
| N8 | 2 (1) -> fixed | 1 (0) | 0 (0) |
| N17 | 3 (0) -> fixed | not needed | - |

2. **Note v0.6.** Line-for-line with v0.5: the rows on its 213 unchanged lines and every render row were carried unchanged (note_file renamed); three chains mapped the six changed lines (G1 line 3; G2 lines 1, 60, 98; G3 lines 111, 208), each mapped, checked adversarially, revised and, where the check was substantive, rechecked.

| chain | final rows | check (findings, substantive) | missed units | recheck (findings, substantive) |
|---|---|---|---|---|
| G1 | 209 | 7 (0) | 0 | not needed |
| G2 | 67 | 7 (1) | 0 | 6 (1) |
| G3 | 69 | 8 (1) | 0 | 5 (1) |

3. **Machinery (rulings 11-13).** A v0_6 profile with ruling 11's reach (S7#91 admitted; the second 'two' and the v2 date recorded as not-figures), ruling 12's table for the three 'fifty' rows, and ruling 13's extension of the scope check to the renders; v0_3, v0_4 and v0_5 untouched. Checked (6 findings, 0 substantive), fixed. A dry run on v0.5's committed rows under the round-10 rules passes 606 of 615, Code's projection.
4. **Integration and checks.** Three adversarial lenses each round: row values, ledger content, script integrity.

| round | row values | ledger content | script integrity |
|---|---|---|---|
| 1 (integration) | PASS: 5 (0 substantive) | PASS: 6 (0 substantive) | PASS: 5 (0 substantive) |
| 2 | PASS: 2 (0 substantive) | FAIL: 5 (1 substantive) | PASS: 4 (0 substantive) |
| 3 | PASS: 4 (0 substantive) | PASS: 7 (0 substantive) | PASS: 1 (0 substantive) |
| 4 | PASS: 1 (0 substantive) | PASS: 6 (0 substantive) | PASS: 2 (0 substantive) |

Round 1 passed with 0 substantive findings; its 16 minor findings were applied in fix round 1 (they included cross-references, a false sentence and stale pairings in text that is committed). Round 2 found one substantive point: :60's 'the shortest' holds over N13's declared verdict-cell set, and one of the tier calls N13 leaves to the PI (O15) would add a cell whose printed gap is shorter; fix round 2 recorded it (9h O32: the wording the design seat's, the scope the PI's through O15; non-blocking, no figure's pass depends on it). Round 3 passed with 0 substantive findings; its minor findings were applied in fix round 3, and the later rounds recheck it. Each fix round is recorded in the ledger's 10e.

## 2. Outcome

- Rows 1274 (632 figures). Validation: 0 unexplained failures; the self-test and the guard cases all as expected (the ledger's 9a and 10a).
- **Block :23's pass condition is met: 632 of 632 figures pass.** By status: computed-new 157, log-only 131, reproduced 314, discrepant 23, not found 7.
  - Under the PI's rulings: ruling 5, 157 rows (ruling 12 the basis of 3: S5#106, S7#97, S10#137); ruling 6, 13; ruling 13, 2 (S11#18, S11#19); ruling 7, 2 (S6#102, S6#103); rulings 8 and 11, 7 (ruling 11's occurrence S7#91 among them; and ruling 11's 4 not-figures outside the count: S7#86, S7#87, S7#88, S7#89); and 6 corrected rows in branch C (R1 among them).
  - Not passing: 0. Open, not ruled: 0. Held: 0.
- The commit at which the last of the note's figures entered the record, including audit raws: `fa1b41e` (set by S1#407, S1#408); over record sources only, `05c4636`.
- Open items: 33 in 9h, each with its disposition and whose call it is; none blocks the pass.

## 3. Residual minors from the final check, carried open (not applied)

All three lenses of the last check returned PASS, with 9 minor findings. They were not applied, to avoid another rebuild of the frozen rows file; none changes a status, a value, a branch, a pass or a verdict:

- [Rows file, the comments of S6#112 and S1#423. S6#112: 'That is a preprint-sentence check under the PI's ruling 9, not a status for this note row, so the row kee] Both comments state Code's reading (e) without a label. The reading is that S6#112 and S1#423 pass log-only at the pin, and that N5 P10-2 is a preprint check and not a status. Fix round 3 labelled readings (a) and (b) on every comment that states them (S7#86–S7#89, S7#97, S10#137, S5#106), under round 3's finding 4. For (e), the 'Code's reading (e)' label exists only in 9h O33, in 10e and in S6#112's round10.why. In S6#112 the conclusion ('so the row keeps its locator … and its status') directly follows 'the PI's ruling 9', so a reader can take it as that ruling's consequence rather than Code's reading. No status, value, locator or pass depends on the label.
- [Code's reading (c), as stated in 9h O32 (out/ledger.md:2164: 'E1 being the later decision; the earlier withdrawals, round 8's fix round 5 ... and round 9's D3 r] The chronology is backwards for D3 round 2. E1 is round 8's fix round 6, committed at fd2b136 (2026-10-10). Round 9's D3 round 2 was committed at fa1b41e (2026-10-11), so it is later than E1, and it cites E1. Its first withdrawal marker at fa1b41e:1835 reads "Code's D7 (i) and E1". So 'E1 is the later decision' is true only against fix round 5. The reading's substance still holds: E1 keeps extremes, and both withdrawals were of an ordering, not of an extreme. But the stated reason for E1's precedence misdates a committed decision.
- [9h O30 (out/ledger.md:2162): 'The rows the question reached through their premise keep their status and pass under ruling 5, as in round 9: S5#103, ..., the val] Round 9 did not pass three of these rows. S8#78, S5#116 and S5#117 were held 'Open, not ruled' in round 9's 9d (v0.5 ledger @fa1b41e:1688). v0.5's own O30 says they were 'held open on O11's readings, not on O30's'. The same 9h contradicts it: O11 (a) says 'the five rows round 9 held (S8#136, S8#137, S8#78, S8#139, S8#122) pass under ruling 5', and O11 (b) passes S5#116 and S5#117 only now. The round-10 verdict (pass) is the same in both places. Only the history is misstated.
- [9h O21 (f) (out/ledger.md:2153): 'v0.5's (e), the :114 edit named only through a span note, stands in the restated text (S1 note 14)'] v0.5's O21 (e) had two parts. One was the :114 edit, named only through a span note. The other was that S4's list 'understates note 12 and omits note 7' (S4 note 5). The restated 'Previous (v0.5)' text still carries 'the numerics disclosure corrected for the MLP (S4 note 12)' without note 7. S4 note 5 is still 'carried' with O21 in the cross-check, and it is in O21's span-note list. But O21's text restates only the :114 half, so the item's description omits a residue it carries. Nothing live is dropped at table level.
- [9h O25 (out/ledger.md:2157), its enumerated list of stale README-NOTE.md@fa1b41e lines outside §4] Fix round 3 added :4 (Tier-1 raws at 84801cb), :76, :77, :83 and :186 (note v0.5). Three lines of the same classes, also outside §4 (§4 is :85-164), are still missing:
- :172 says the Tier-1 raws were 'regenerated in place at `84801cb`', which is :4's class; round 10 regenerated them at d6bb790.
- :217's condition (4) says :181 'holds only at a tag commit at or after `fd2b136`', which is :216's class; 9g now gives fa1b41e.
- :1, the header comment, cites 'N1 final ledger for note v0.5', which is :83's class.
The catch-all ('the lines outside §4 are Code's to re-sync then') covers them, so nothing is dropped. But the list is still incomplete by its own criteria.
- [9f S8 note 20 (carried v0.5 S8 note 12; out/ledger.md:2031-2034) and its round-10 annotation ('(a) is settled ...; (b), (d) and (e) stand')] Part (b) of the carried note says, in the present tense: 'Under ruling 9 the patched preprint is committed at the tag; its root copy hashes to 0f4ba501…6c22.' Since the PI's routing of 2026-10-12, the root copy is patch v7 (d9635ca2…1fe6), and 0f4ba501 is archive/…pre-patch-v7.md (O29). The round-10 annotation says '(b) ... stand[s]' and does not qualify the hash. Fix round 1 annotated S7#89's and S7#91's carried comments for exactly this pairing. The table residue in (b) still holds on v7, whose :206 is unchanged.
- [10e, Code's readings bullet, reading (a) (out/ledger.md:2814): '...the ruling's reach is recorded in NR_ROUND9['r11_not_figures'], and S7#91 'ten' passes as adm] In the routed reading, '(Code told the PI so on 2026-10-12)' follows 'the ruling's reach is recorded in the v0_6 table built for it', and 'S7#91 'ten' passes as admitted' comes after it. The ledger moves the parenthetical to after S7#91's pass. That changes the record of what Code told the PI.
- [10e, fix round 3's Ledger 1 bullet in the script text (audit_note_N1.py fix-round-3 record): 'The table builder now asserts this direction too ... so 9h's intro] The direction that fix round 3 repaired is bound by nothing that runs. That direction is: a span note whose disposition names an item is in that item's span-note list.
- The builder does not assert it. It appends the problems to open_disp_probs.json and prints them, exits normally, and nothing reads the file (rebuild.sh does not).
- The committed script's nr_span_crosscheck checks only the other direction (an item's cited note names the item).
- An in-memory probe confirms the gap. Removing S5 note 29 from O32's notes, or S1 note 20 from O7's (reverting the fix-round-3 edit itself), gives nr_span_crosscheck 0 problems, so a final run would pass.
- On the current candidate both directions hold: my independent check finds no exception apart from O16, which is stored separately. No row is affected.
- 10e's 'asserts' overstates what the builder does, and 10d does not state the limit.
- [Rows file, round10 history records:
- S1#428: finding has 4 entries, why has 5.
- S7#91: finding 1, why 2.
- S1#303 (G1's record): finding 1, why 2.
Related: sc] The committed v0.5 rows file has 536 list-form history records, and every one keeps finding and why parallel, one reason per finding. Three v0.6 records break that.
- On S1#428, fix round 2 contributed one finding and two whys. Fix round 3's finding therefore sits at index 3 while its why sits at index 4.
- Read by index, the record attributes fix round 2's 'one wording in 9a, 10e and on the row' to fix round 3, and fix round 3's fold to no finding.
- nr_history_schema does not bind the pairing, and the schema text does not say the lists are unpaired.
- This is history bookkeeping only. No status, value, key or pass is affected. The text hash freezes the records as they stand.

## 4. For the PI

- The pass condition is met. Code's readings this round (stated as Code's in the ledger): ruling 11's not-figures keep their kind; :60's 'the shortest' is a reading under round 8's E1; line 3's reference to :98 meets W5; :111's 'three' passes log-only on PROPOSAL-m at the pin. The tag waits on the N12 pre-flip re-scan decisions and on whether the tag commit holds the note and the renders.
