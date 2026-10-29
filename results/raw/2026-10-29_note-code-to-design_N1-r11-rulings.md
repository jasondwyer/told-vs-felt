# Code → design seat / PI — N1 round 11: the re-keyed rulings, and what the pass needs ruled (note arc; 2026-10-29)

*Code. This file answers `results/raw/2026-10-28_note-design-to-code_release-block-answers.md` (`908a659`, cited below as "answers :line"), §6 4f and §10 item 3: each ruling whose quoted text changed in note v0.8, with its v0.6 key and its v0.8 candidate, in one list, for the seat to answer in one block (answers :56). Answers §10 item 3 calls this list "the only item that returns before the tag"; §2a and §2b below also need the seat's word before the tag if AUDIT :23's pass is to be met (§7). The list covers what the seat must rule for that pass over `RESEARCH-NOTE-v0_8-draft.md` (`0de15a1`, sha256 `6fcfbfd6…1198d`) and the three 2026-10-22 renders (`0a3f925`). The note is frozen (answers :23), so no item assumes a note edit; a correction would go to a dated correction block on the post (at the flip, the PI's, with the seat: answers :69, :53) or to a ruling. Basis: round 11's integration rows (scratch until the ledger commit: 1,128 rows, 695 figures, sha256 `b2207d70…38ef`), which are the chains' merged rows (sha256 `ce71f7a6…ee1b`) with Code's integration edits E1–E11 (each row edit is recorded in its row's round11 record, and E10's annotations in the span notes' annotations; E1's placement of sixteen chain span notes has no record in the file, which names no edit by number); and their dev report (`--dev-report`, profile v0_8, exit 0), run with `scripts/audit_note_N1.py` as it stands in the working tree with the v0_8 tables applied (uncommitted; sha256 `fd361e5d…cd1f5`), at HEAD `f935864`. "Probe" means Code ran that script's own check on an in-memory copy of a row with the candidate field, and its table entry, set. The pass counts in §0 and §7 were counted the same way; §7 states the method. The probes and counts wrote nothing to the repository; round 11's one write there is the working-tree script's v0_8 tables (uncommitted). A values-check in three parts read the draft of this list against the repository and the round's scratch files, a second, in two parts, read the revision, and a third, in three parts, read the text written for the second round's findings against the lines it cites; every finding of the three is applied below. Code checked the text written for the third round's findings against the lines it cites; no fourth check read it. A point that rests on a chain's report without Code's re-check says "(chain Kn, not re-checked)". Each point that asks for a decision says whose call it is, and gives Code's recommendation where Code has one. None of the tables or rows described here is committed, and no seat answer is assumed: ruling 13's re-key (1b item 1) is applied in the rows but held off in the working tree (V08_RULING13_REKEY_SEAT_CONFIRMED = False, wt :16069), so its two rows do not pass until the seat confirms, and §4's readings stand as Code rowed them until the seat rules. Calendar dates only.*

Notation: v0.8 :N = `RESEARCH-NOTE-v0_8-draft.md@0de15a1:N`; v0.6 :N = `RESEARCH-NOTE-v0_6-draft.md@note-2026-10-v1:N`; "F1a/F2 node N (10-22)" = text node N of the 2026-10-22 render @`0a3f925` under N1's extraction, "(10-10)" the 2026-10-10 render @`98d07bc`; "script :N" = `scripts/audit_note_N1.py@f935864:N` (the v0.6 profile and the round-9/10 tables it carries); "wt :N" = line N of the same script in the working tree, sha256 `fd361e5d…cd1f5` (uncommitted; the numbering moves when it is committed); "v0.6 ledger :N" = `results/raw/2026-10-12_note-N1-v0_6-claims-ledger.md@c18854f:N`; "AUDIT :N" = `AUDIT-note-release-v1_2.md@bbc9ffe:N` (AUDIT :23 is the pass rule N1's ledgers call "block :23"); "release block :N" = `results/raw/2026-10-27_note-design-to-code_release-block.md@2fb0cf0:N`; "Q" = `results/raw/2026-10-27_note-code-to-design_release-block-questions.md@268787f`; "additions :N", "correspondence raw :N" and "Chandaria raw :N" = `results/raw/2026-10-28_note-N1-r11_additions-by-source.md`, `results/raw/2026-10-28_note-N1-r11_correspondence-figures.md` and `results/raw/2026-10-28_note-N1-r11_chandaria-v2-lines.md`, all @`908a659`. Item raws by short name, at the revision each citation gives: N2 = `results/raw/2026-10-08_note-N2-introspection.md`; N2vi = `results/raw/2026-10-08_note-N2vi-source.md`; N2(vii) = `results/raw/2026-10-22_note-N2vii-macar-v5.md`; N3 = `results/raw/2026-10-08_note-N3-echo-robustness.md`; N3c = `results/raw/2026-10-08_note-N3-echo-compute.md`; N4 = `results/raw/2026-10-08_note-N4-e2a.md`; N5 = `results/raw/2026-10-08_note-N5-f1.md`; N7 = `results/raw/2026-10-08_note-N7-olmo.md`; N13 = `results/raw/2026-10-08_note-N13-provenance.md`. "9d", "9e" and "9h" are sections of N1's ledger (v0.6's at `c18854f`; round 11's at its commit).

## 0. Where the pass stands

- **695 figures** (and 433 not-figures): reproduced 256, log-only 187, computed-new 193, not found 40, discrepant 19.
- **637 pass with the v0_8 ruling tables empty:**
  - 443 reproduced or log-only;
  - 193 computed-new under ruling 5 (probe: each of the 193 cites a committed audit raw);
  - S5#38, branch C by its own verified correction (N2@09c3a8c:51).
- **641 pass after Code's steps (1a), and 643 once the seat confirms ruling 13.** Code's integration edit E9 restored three rulings' fields verbatim: R1's on S10#108 and S10#60, ruling 8's on S7#19 and S7#20, and ruling 13's on S11#18 and S11#19. The working-tree script declares the R1 and ruling-8 tables that match, and holds ruling 13. It is held because 4f does not name it: the two F1a rows are reported "open, not passing" until the seat confirms (1b item 1). So Code's steps take the count from 637 to 641 now, and to 643 on the seat's word, not straight to 643.
- **54 do not pass after Code's steps:** 14 discrepant (the ten branch-TS note rows; S5#81 and S5#88 in branch C; the two branch-NT rows), 38 not found, and the two held F1a rows.
- **What the dev report shows on these rows.**
  - 10 unexplained failures, all `scope-corrected-in-note`, on the ten branch-TS note rows (1b items 3 and 4).
  - `corrected_in_note_consistent` is false on S5#81 and S5#88 (1b item 2).
  - 14 explained failures, each exemption declared at its fingerprint. Every other row and table check the report runs is zero; its profile gates and its four hash comparisons do not pass (the next two points).
  - A final run would stop before its branch-C check: first at the profile gates (the unset hashes and sentinel texts, wt :5646-5648), then at the ten TS validation failures (wt :4188-4189, :5687). Once those clear, it stops at its branch-C check (wt :4213-4215) until the seat answers item 2 or Code re-declares the two rows' branch. The dev report ran none of the fixed mutations: it runs them only when no row fails unexplained, every frozen hash matches and no quotation hit is undeclared (wt :16548-16550), so the ten TS failures and the unset hashes keep them off; the sentinel texts and the branch-C check do not gate them.
  - The four frozen hashes and the round-11 sentinel texts are unset. They are Code's, set last.
- **Code's.** The fourteen exemptions are Code's and wait on nothing below: twelve carried or new fingerprints; S4#19's v0.6 exemption (script :14411), restored by E2; and S8#1008, which takes v0.6 S7#73's (script :14421), restored by E3. All fourteen are declared in the working tree's NR_EXEMPT_FP. NR_DISC, NR_T_ROWS, NR_NF_ROWS, the watch lists, NR_OPEN and the span dispositions are Code's too: they are declared in the working tree now (NR_DISC from wt :14880 to NR_SPAN_DISPOSITION from wt :15664) and are revised where the seat's answers move them. The sentinel texts and the hashes are Code's, and are written after the seat answers (the hashes last).
- **Scratch values withdrawn (E11).** Five K5 comments in §2b's group (S5#2055, S5#2056, S5#2057, S5#2059, S5#2060) carried Code's scratch *d*′ and *c* values.
  - E11 withdrew them in round 8's D5 (c) form (script :9241). Each comment now names the committed inputs and the operation and gives none of the computed values. Its round11 record carries a marker in place of the withdrawn clause, as round 8 recorded its D5 withdrawals.
  - The comment field is outside every exemption fingerprint (NR_FP_FIELDS, script :2433-2435). No fingerprint moved, the fourteen exemptions stay declared, and only the text hash's computed value changes.
  - Code's scan of every other row's comment found the same class in six rows: S1#1019 (a ratio), S3#31 (three differences), S5#2061 (a corrected *d*′ range and the products it rests on), S6#1024 and S6#1025 (a five-decimal interval the record prints at four), and S8#1023 (a five-decimal quotient N2 prints at four). It also found the class in span notes S3 4, S5 2 and S6 4; S5 note 1's pointer to the five comments is now stale.
  - Withdrawing these in the same form is Code's, before the ledger commit. None of them moves a status.
- **Code's other edits before the ledger commit** (none moves a status):
  - S5's span note 0 names a scratch file: Code removes the path.
  - S5#81's and S5#88's comments say R1 "is re-keyed at integration (4f)": Code restates them to 1b item 2's routing.
  - The rows file's how_built (chain K1's text) says no ruling field is set, where E9 set six: Code restates it.
  - The comments of S7#19, S7#20, S10#108 and S10#60, and span notes S7 2, S10 4 and S11 2, say their ruling field is not set, and S8 note 3 says S6#26's correction was dropped "as the v0_8 tables are empty", where E9 and E8 set them: Code restates the comments and annotates the notes in E10's form.
  - W8's NR_WATCH outcome calls the lexical-set result on :143 "K6's reading …, not a run", and the probe has since run it (1b item 5): Code restates the outcome.
- If the seat closes every item in §1b, §2a and §2b with a passing route, and §4's readings and kind calls stand as rowed, 695 of 695 pass (§7).

## 1. The re-keyed rulings (4f)

4f reads: "Code re-keys rulings 7, 8, 11, 12 and R1 where they apply verbatim in v0.8; each one whose quoted text changed comes to the seat through the PI with the old key and the v0.8 candidate, and the seat answers in one block" (answers :56). Code reads it conservatively. Code's own steps are the verbatim re-keys of the rulings 4f names. Code applies the same rule to ruling 13, which 4f does not name, and holds it for the seat's confirmation (1a; 1b item 1). Every other re-key, ruling 6's included, is the seat's, and so is R3's carry to a rewritten paragraph (1b item 11).

### 1a. Code's steps: the verbatim re-keys (E9; listed so the seat sees them)

| Ruling | v0.6 key · locus · what the ruling declares | v0.8 key · locus | Change | State | Probe |
|---|---|---|---|---|---|
| R1 | S10#108 '0.000', F2 node 54 (10-10) "(0.000, 0.009)"; S10#60 '0.000', node 90 (script :13385; condition N2vi@09c3a8c:619) | same keys; F2 nodes 54 and 90 (10-22), same text | the file only | applied: corrected_in_note restored; NR_RULED_CORRECTIONS declares both (wt :16052) | pass ×2 |
| Ruling 8 | S7#19 '57.7%', S7#20 '79.7%', v0.6 :142; note_quote "The nearest is the unlabeled-button condition of Tagliabue et al., where the 32B model re-presses an undescribed relief button less often when it worked (57.7%) than when it was fake (79.7%; v1, §4.3)" (script :10809-10812) | same keys; v0.8 :195, the quote verbatim, naming the source and carrying both units | r8_units (142, …) → (195, '57.7%'), (195, '79.7%') | applied: admitted_citation restored; NR_ROUND9['admitted'] declares both (wt :16053-16059) | pass ×2 |
| Ruling 13 | S11#18 '.81', S11#19 '.96', F1a node 17 (10-10); note_quote "≈1.0 · .81–.96 / at first and second label, / from L51." over nodes 17-19; the ruling names both rows (script :12531-12532) | same keys; F1a nodes 17-19 (10-22), same text | the file only | **held**: scope_corrected_in_note restored, but `V08_RULING13_REKEY_SEAT_CONFIRMED` is False (wt :16069), so 9d reports both "open, not passing" until the seat confirms (1b item 1) | pass ×2 (the field's check) |

4f names rulings 7, 8, 11, 12 and R1, not 13 (answers :56). F1a nodes 17-19 are unchanged, so Code applies 4f's verbatim rule to ruling 13 the same way, and holds the result for the seat's confirmation. Setting the constant True passes the two rows with no row change (counted: 641 → 643).

### 1b. The seat answers

1. **Ruling 13 on F1a (S11#18, S11#19).** The seat's: confirm, or say that ruling 13 does not reach the 2026-10-22 render.
   - The re-key is verbatim and prepared (1a). Only the seat's word is missing, because 4f does not name ruling 13.
   - Code recommends confirming.

2. **R1 on S5#81 and S5#88 (the clause changed).** The seat's.
   - **v0.6.** S5#81, v0.6 :92, the instruct '0.000' in "theirs 0.000 and 0.000"; S5#88, v0.6 :98, the second '0%' (script :13385).
   - **v0.8.** Same keys. S5#81 is :93's third '0.000', in "(0/91 and 0/91 vs. 0.000 and 0.000 in the published work)". S5#88 is :99's second '0%', in "false-positive rates of 16.4%, 22.5%, 0% and 0% for base, SFT, DPO and instruct (Macar et al., 2026, v1, Appendix C)".
   - **What changed.** The clause around the unit. R1's condition (N2vi@09c3a8c:619), its figure row (N2vi :26) and its source clause ('source v1 text 0.000') are unchanged.
   - **Code's reading.** R1 declares no note text: its declaration (script :8096-8101) has no note_quote. The unit is the same quantity in the same role. But 4f sends every re-key whose quoted text changed to the seat, so Code has not applied it.
   - **Probe.** With v0.6's corrected_in_note restored and both keys added to NR_RULED_CORRECTIONS: pass ×2 (counted: +2).
   - Until the seat answers, both rows are branch C without their field (§0). If the seat declines, Code re-declares their branch, for example to T in NR_DISC with both rows listed in NR_T_ROWS (both Code's tables; a final run asserts that NR_T_ROWS equals the branch-T rows, wt :4322-4324), so that a final run can complete and record them as failing.
   - Code recommends re-keying.

3. **Ruling 6 on the six branch-TS rows whose probe passes.** The seat's: does ruling 6 reach v0.8's wording? Code recommends yes.
   - Ruling 6 (script :9724-9725) is a class rule, not a keyed table. A TS row must carry scope_corrected_in_note, which nr_check_scope_corrected checks against the routed correction; a TS row without it fails validation (wt :10147-10150). None of the ten note rows carries it yet.
   - 4f does not name ruling 6, and the quotes changed, so the re-keys are the seat's. Chains K1 and K3 sent them here. The chains' rows carry no ruling field (for the S1 rows, chain K1's how_built, which the rows file carries; for S4#10 and S4#11, chain K3's round11 'why': "ruling fields are not set in round 11").

   | v0.6 key · v0.6 note_quote | v0.8 · candidate note_quote | Routed correction | Probe |
   |---|---|---|---|
   | S1#134 '.94', S1#214 '.995', S1#215 '50', S1#216 '63' · v0.6 :26 "at .94–.995 over layers 50–63" | v0.8 :14 (TL;DR item 3) "(.94–.995 over layers 50–63)" · ".94–.995 over layers 50–63" | N3@09c3a8c:370, 'L50-L63' | pass ×4 |
   | S4#10 '.81', S4#11 '.96' (v0.8: '0.81', '0.96') · v0.6 :85 ".81–.96 at the second, both from layer 51 on" | v0.8 :85 · "0.81–0.96 at the second, consistently from layer 51 onward" | N3@09c3a8c:385, 'from L51' | pass ×2 |

   - On a yes, Code sets the six fields: v0.6's locator and quote, with the v0.8 note_quote (counted: +6).
   - On a no, Code re-declares the six rows' branch, for example to T in NR_DISC with the six listed in NR_T_ROWS (both Code's tables; wt :4322-4324), so that a final run can complete and record them as failing.

4. **Ruling 6 on S4#4 '0.94', S4#5 '0.995', S4#38 '50', S4#39 '63'.** The seat's, with Code's script change.
   - **Text.** v0.6 :84 "at AUC .94–.995 over layers 50–63" → v0.8 :83 "(AUC of 0.94 to 0.995 across layers 50 through 63)".
   - **Why it fails.** Probe: fail ×4. The term reader reads "layers 50 through 63" as ('layer', '50') plus a bare ('num', '63'), so it does not find the routed 'L50-L63' (N3@09c3a8c:370), though the domain is stated. On the current reader the count does not move (counted).
   - **Options.**
     - (a) Code teaches the reader "layers N through M" (a script change), and the seat says ruling 6 reaches :83's wording (item 3). No other audited text has "layer(s) N through/to M". A grep finds none in the v0.3, v0.4, v0.5 and v0.7 drafts (working tree), in v0.6 and the 2026-10-10 renders at `note-2026-10-v1`, or in the 2026-10-06 and 2026-10-09 renders. So v0.3–v0.6 should reproduce unchanged, and the regressions would confirm it (rule 26).
     - (b) A ruling that :83 applies the correction as written. It would be mechanised as a declared per-row exception to the term check, so it is a script change too.
     - (c) Left failing. Code then re-declares the four rows' branch, for example to T in NR_DISC with the four listed in NR_T_ROWS (both Code's tables; wt :4322-4324), so that a final run can complete and record them as failing.
   - Code recommends (a), with a yes on item 3.

5. **Ruling 7 (W8, branch NT).** The seat's.
   - **v0.6.** S6#102 '0.8' and S6#103 '2.0%' at v0.6 :111, with note_quote "session-termination attempts occur at about 1% of rounds overall (0.8–2.0% by arm, the sham arm highest, with no detectable heterogeneity on a post-hoc exact test, p = .72)" (script :11170-11173, carried at :13354).
   - **v0.8.** New keys S8#3074 '0.8' and S8#3075 '2.0%' (v0_6_row S6#102, S6#103) at :250 ‖(c): "Session-termination attempts occur at about 1% of rounds overall (0.8–2.0% by arm, the sham arm highest, with no detectable heterogeneity on a post-hoc exact test, *p* = .72)".
     - The clause moved into the footnote (span S6 → S8). It now has a capital S and an italic *p*.
     - Probe with that quote: pass ×2 (counted: +2). The clause states the overall rate and the per-arm range (both W8 states read true on :250), and :250 carries no W8 wording.
   - **New at :143.** "Session-termination attempts were rare (about 1% of rounds) and did not differ by arm. Menu behavior was exploration-dominant in every arm.‖"
     - Its '1%' is S6#101, reproduced on the overall row (N5@09c3a8c:216, 39/3074).
     - Code reads "did not differ by arm" as the by-arm uniformity that N5 :217 marks discrepant, not transcription (sham 7/351 = 1.99%). N5 :219 supports it only as "no detectable heterogeneity" (post-hoc p = 0.7173).
     - W8's lexical set (NR_ROUND9['w8']['absent'], script :10777-10783) does not fire on :143, and neither W8 state reads true there (probe). So no check fails on the wording. :143's 1% (S6#101) appears in 9e as a W8 matcher hit and as a listed W8 row (wt :15021), but no check tests its "did not differ by arm". W8's outcome is Code's NR_WATCH declaration (working tree), which leaves this question to the seat. This is a known limit, not a ruling.
     - The ‖ on :143 points to ‖(c) at :250.
   - **The seat answers two questions.**
     - (a) Re-key ruling 7 to S8#3074 and S8#3075 with the :250 clause? Code recommends yes. On that answer Code also restates NR_DISC_PATH's NT text, which names v0.6's ":111", for :250.
     - (b) Which reading holds for :143?
       - Either ruling 7's discharge reaches it through its ‖ pointer to :250, and the wording goes to the correction block in N5 :122's form, for example "with no detectable heterogeneity by arm (post-hoc exact test, *p* = .72)".
       - Or W8's conditional STOP reopens on :143. AUDIT :23 makes that a STOP on the item. On Code's reading, a frozen note clears it only by a ruling.
       - Precedent is thin. Code's ruling-7 table once declared a second locus, v0.4's line 3 ("W8 reworded (termination 0.8–2.0% by arm)"), but only in the scratch-only dry run v0_4_r9 (script :10785-10796). No committed ledger applied ruling 7 outside :111, and the PI's ruling names no locus (`README-NOTE.md@f935864:121`: "W8 (O2) is discharged by the rewording"). That locus also stated the per-arm range, while :143 states neither the range nor the overall rate in the form the check reads (probe).
       - Code recommends the first reading.

6. **Ruling 8, S7#28 'two'.** The seat's.
   - **v0.6.** :142, cited_source "my next-experiments list", note_quote "The two arms that would settle it are specified in my next-experiments list" (script :10820-10821).
   - **v0.8.** :202: "Our next-experiments list specifies two arms on their released code, …".
   - **Candidate.** cited_source "Our next-experiments list"; note_quote "Our next-experiments list specifies two arms on their released code"; unit (202, 'two'). Probe: pass (counted: +1).
   - **Record-line alternative.** `results/raw/2026-10-04_m-v1.7_referent_check.txt@bbc9ffe:7782-7784` quotes the then-untracked draft's §8.2 heading. Round 4's precedent closes it as a carrier: `results/raw/2026-10-09_note-N1-v0_4-note-rows.json@fd2b136`, row S1#172, the C1 checker's finding 4, "The count's only committed carrier quotes the untracked preprint".
   - Code recommends the candidate.

7. **Ruling 8, S7#25 'three'.** The seat's.
   - **v0.6.** :142: one note_quote ran from "The nearest is …" to "…the 32B of the three sizes tested" (script :10813-10819).
   - **v0.8.** The list is now split. The unit is on :200 ("4. The label-free evidence is limited to the 32B of the three sizes tested.‖‖"). The source is named on :195 (also :27, :216, :258).
   - **Why it fails.** nr_check_admitted needs one verbatim note_quote that names the source and carries the unit. No v0.8 line has both 'Tagliabue' and 'three' (probe). With :195's quote the check fails: "admitted_citation's note_quote does not carry the row's unit 'three'".
   - **Options.**
     - (a) A ruling that admits it with the source named on :195. This needs a check change, and v0.3–v0.6 must still reproduce.
     - (b) Not admitted: it stays not found and fails the pass.
   - Code recommends (a).

8. **Ruling 11, S7#91 → S8#3143 'ten'.** The seat's.
   - **v0.6.** S7#91, the 'ten' in :142's "separately from the ten", an occurrence of (172, 'ten'), the admitted S7#82 "table in the preprint" (script :13162-13168).
   - **v0.8.** S8#3143 (v0_6_row S7#91) at :258 ‖‖(b): "…scored as told with the manipulation on at the read, separately from the ten."
   - **Why nothing reaches it.** The citation it was an occurrence of is gone (1c). No v0.8 line states the count of scored designs: :195 gives none, :214 promises "the scored audit table with per-study sources" without a count, and :216's "Full list in the preprint." closes the key-references list. So ruling 11 has nothing to reach.
   - **Options.**
     - (a) A new ruling admitting it as the preprint table's count. No v0.8 line names that source with the unit (probe: no line has both 'preprint' and 'ten'), so this needs a check change, as item 7 does.
     - (b) It stays not found and fails the pass.
   - Either way, "the ten" has no antecedent. The line's first 'ten' ("a set of ten norm-matched random directions", correspondence raw :27) is a different quantity (§5 #34).
   - Code has no recommendation between (a) and (b).

9. **Ruling 11's not-figures, S8#3100, S8#3101, S8#3102 (outside the 695).** The seat's.
   - **v0.6.** S7#86 '2026', S7#87 '09', S7#88 '25': context '2026-09-25' on v0.6 :142, occurrence 1 each, comment_quote 'the v2 date' (script :13169-13181).
   - **v0.8.** S8#3100–S8#3102 (v0_6_row S7#86–S7#88) at :258 ‖‖(a): "The counts and the v2 (2026-09-25) figures below are as the authors reported them to us on 2026-10-26". The context occurs once on the line.
   - **Three declared fields change.**
     - note_line goes from 142 to 258.
     - '2026''s occurrence goes from 1 to 2: the date is the second of four '2026' tokens on :258.
     - comment_quote goes from 'the v2 date' to 'the v2 posting date 2026-09-25', the words the rows' comments now carry.
   - **Probe.** With the three changes, ruling 11's run check finds no problems. With v0.6's comment_quote and occurrence it fails on both.
   - The rows' own comments send the re-key to the seat. Code recommends re-keying with the three changes.

10. **Ruling 12, 'fifty'.** The seat's (4f: "the ruling is re-keyed by the seat, not assumed").
    - **v0.6 keys.** S5#106 (:98 "5,000/500 (one fifty-concept configuration)"), S7#97 (:164) and S10#137 (F2 node 98, 10-10). The ruling text is at script :12529-12530 and its table at :13184-13188.
    - **v0.8.** The note now names fifty as the source's count:
      - :101 S5#2003: "to the twenty configurations at the source's fifty concepts (100,000/10,000)";
      - :236 S8#2070: "5,000/500 is one configuration at the source's fifty concepts" (v0_6_row S5#106);
      - :236 S8#2079: "100,000/10,000 is fifty over the twenty";
      - :236 S8#2082: "The two at fifty concepts are the premises consistent with the source";
      - F2 node 101 (10-22) S10#137: "5,000/500 (one fifty-concept configuration)". The phrase is verbatim, but the caption was rewritten and the node moved from 98 to 101.
    - **The '50' rows.** 4f flags F2 node 99 (S10#1009, "v5 gives 50 concepts"; answers :56). v0.8 :236's S8#2052 states the same v5 count, which 4b confirms ("50 for OLMo (Figure 5; ‡(f))", answers :52). Both rest on N2(vii)@8d68b0b:63-65 under 4b.
    - S7#97 is gone (1c).
    - **Count.** All seven rows are computed-new and pass under ruling 5 now (counted), so the answer moves no count.
    - **The seat answers.**
      - (a) Re-key ruling 12 to the five 'fifty' rows. Each keeps N2 5(b)'s label (@09c3a8c:376) as its status basis, and the two '50' rows rest on 4b alone. Probe: ruling 12's run check passes on all five.
      - (b) Retire ruling 12 as overtaken by 4b.
    - Code recommends (a). Whether S10#137 also cites N2(vii) :64 (chain K12's question) is Code's call, after the answer.

11. **R3, the N2(ii) STOP on link 4's ROC paragraph** (`README-NOTE.md@f935864:115`). The seat's: does R3's closure carry to v0.8's rewritten paragraph?
    - **v0.6.** :96, unchanged from v0.5, kept v0.4's rewording: B2 named with its differences, the comparison "confounded", and the rescoring said to license "nothing, because it's post hoc".
    - **v0.8.** :118 names no B2 and drops "confounded": "Despite it differing from the sampled run in more than temperature, a post-hoc rescoring indicates temperature as the driver." Some of the differences move to ‡(k) at :246 ("a 60-token cap, a legacy scorer, and other differences").
    - **Code's reading.** N2's STOP asked for the greedy row to be withheld or reworded as "'B2, an earlier protocol at temperature 0' with its differences listed" (N2@09c3a8c:469). The working tree keeps O6 CLOSED on Code's reading of :118 and ‡(k) (wt :15135-15142). The text changed, so the carry is the seat's (§1).
    - **Effect.** No figure moves. A "no" reopens N2(ii)'s STOP; on Code's reading a frozen note clears it only by a ruling or the correction block. :118's other point is §5 #4.
    - Code recommends confirming.

### 1c. Gone — no v0.8 successor

| Ruling | v0.6 key · locus | Evidence it is gone |
|---|---|---|
| 6 | S4#31 '.10', S4#32 '.02', S4#33 '.03' (v0.6 :86, the leakage bullet) | v0.8 has no "pseudo-shift", "alternating ±" or "logit on" (grep) |
| 8 | S3#129 '25' (v0.6 :70, "…across 25 open-weight models") | no "open-weight", "base-model" or "comparable to instruct", and no '25' on v0.8 :61-76 (grep) |
| 8 | S7#82 'ten' (v0.6 :172, "the ten published designs (table in the preprint;") | no "ten published" or "published designs" (grep) |
| 11 | S7#89, the second 'two' in "the first of the two arms" (v0.6 :142) | context absent (grep) |
| 12 | S7#97 (v0.6 :164, "(1.2 at one fifty-concept configuration's n)") | absent: no v0.8 sentence restates :164's parenthetical. v0.8 gives 1.2 as one of the four premises' *d*′ (:101) and as the low end of :112's "*d*′ ≈ 1.2–2.0 at DPO on the source-consistent premises", which ‡(f) :236 calls "the two at fifty concepts"; neither line carries a "fifty" with the 1.2. :101's "fifty" is S5#2003's (the 100,000/10,000 premise), and no row has v0_6_row S7#97 |
| R1 | S8#119 (v0.6 :208, "on Code's reading of the v1 prose — the record's 0.003 is the instruct introspection rate transcribed into the wrong column") | no "Code's reading", "wrong column" or "instruct introspection rate" (grep) |

Code recommends that they retire with v0.6 and its ledger at `note-2026-10-v1`, as 4g did for ‖‖(c)'s rows (answers :57). The seat confirms.

### 1d. Not keyed

Rulings 5, 9 and 10, R2 and R4 are not keyed tables and need no re-key. R3 closed a STOP by a rewording that v0.8 rewrote, so it is 1b item 11. Ruling 10's '.59' (the direct rounding of 0.594963) is why S9#108 carries the ledger-span exemption, and why S4#19 takes it back (Code's E2; §0).

## 2. The not-found figures (40), by cause

Forty figures are not found. Two pass as admitted citations under ruling 8's verbatim re-key (S7#19, S7#20; 1a); 38 do not. AUDIT :23 cuts a not-found figure from the note. With the note frozen, Code reads a cut as an item for the post's correction block (the seat's call).

### 2a. Readings of Macar et al. v5 that no committed raw transcribes (11; chains K1, K5, K9)

| Row | v0.8 line · the unit in its clause | Reading |
|---|---|---|
| S1#1012 | :15 'zero': "…our replication, which ran at a strength where the source's own curves also show near-zero detection" | (1) |
| S5#2028, S5#2029, S5#2030 | :101 'zero', '2', '4': "the source's own unpooled OLMo curves also put detection near zero at DPO and instruct, rising at α ≥ 2–4" | (1), (2), (2) |
| S8#2009, S8#2011, S8#2012 | :228 'zero', '2', '4': "The source's unpooled OLMo curves show detection near zero at α = 1 at DPO and instruct, rising at α ≥ 2–4 (v5 Figure 5 at *L* = 25; Figure 22 at *L* = 19 and 22; …)" | (1), (2), (2) |
| S8#2020 | :228 '45': "Figure 20's baseline at *L* = 45" | (3) |
| S5#2048 | :110 '0%': DPO "the first stage to achieve ∼0% FPR with moderate true detection" (v5, §3.3) | (4) |
| S8#2057, S8#2058 | :236 '10', '10': "the 10 injected and 10 control per concept of its §6 are the learned vector's training set" | (5) |

**The five readings a transcription would have to carry.**
1. On v5's unpooled OLMo curves (Figure 5 at *L* = 25; Figure 22 at *L* = 19 and 22), detection near zero at α = 1 at DPO and instruct.
2. On the same curves, detection rising at α ≥ 2–4.
3. Figure 20's baseline layer, *L* = 45.
4. §3.3's sentence on DPO, "the first stage to achieve ∼0% FPR with moderate true detection".
5. §6's 10 injected and 10 control trials per concept, as the learned vector's training set.

**Which version reading (5) means is open.** On :236 the sentence follows "The paper's v1 also does not state an evaluation control count", so "its §6" can read as v1's. K9's rows say only "the source's section 6". No committed file transcribes §6 of any version: `git grep` at `f935864` finds "learned vector" only in the note. A transcription would read §6 in v1 and in v5, or the seat says which version the note means.

**What was searched.** Each row's locator and source_value record the search. Code re-checked the lines named:
- N2(vii)@8d68b0b:63-65 reads Figures 5 and 22 for their captions, concept counts and α grid. :89 places Figure 20 (Appendix C.2) with no layer. No section transcribes §3.3's sentence (two §3.3 paragraphs are cited at :80-81, only as stating no trial count), none reads §6, and no curve value is read.
- N2vi@09c3a8c:401-406 reads v2–v5 as giving the per-stage rates in figures only (:406), with "no numeric per-stage TPR/FPR in text" (:404). :606 says no figure image was fetched.
- `ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:99` says "no per-config OLMo numbers exist in the release".
- Neither the release block (:31-38) nor the additions raw lists these readings. Release block :32's 'the source's "45"' is the caption's label for the 0.7-depth layer (S8#2024's unit), not Figure 20's baseline (Code's reading).
- `git grep` at `f935864`, outside the note drafts, finds no "moderate true detection" and no "rising at". It finds "unpooled" only as unpooled-variance *z* (`RESULTS.md@f935864:8293` and the e2d closure files). The nearest miss is Chandaria raw :14, which quotes Chandaria et al.'s account of Macar ("moderate true positive rates with 0% false positive rates …"). That is not v5 §3.3, so it does not carry S5#2048.

**S5#2048 is also a verification question.** Its quotation gives a per-stage FPR in v5's text, where N2vi :404 reads v5 as giving none. The v5 PDF that N2(vii) read (sha256 `90c0af74…0f92`, N2(vii) :7) settles which is wrong. The chains did not use the v1 carrier (N2vi :25, DPO FPR 0.000), because it is another version's figure (chain K5, map and check).

**Options (the seat's).**
- (a) **The seat writes an N2(vii)-style transcription** of the five readings, if it holds a copy of v5.
  - No committed record says that it does. 4d's raw came from the Chandaria PDF in the seat's project (Chandaria raw :4). N2(vii)'s v5 copy was Code's, kept in a session scratchpad and not committed (N2(vii) :7).
- (b) **Code acquires arXiv:2603.21396v5** (and v1 for §6, if the seat wants both versions read) and transcribes what its text layer and figures state, as N2(vii) did.
  - The download needs the PI's approval, as N2(vii)'s did (:7). The copy is identified against N2(vii)'s sha256.
  - §3.3's sentence and §6's counts are text and can be transcribed.
  - The curve readings may not be recoverable as numbers. N2(vii) found Figure 5's legend raster (:9, :55). A raster curve gives "near zero" and "rising at α ≥ 2–4" only as a reading by eye on a render, which the raw would label as such. Figure 20's baseline layer is recoverable only if the figure states it in text or in its labels.
- Either raw's rows map audit-raw-new, computed-new, and pass under ruling 5 once a pin class admits its commit, as 4b's did for N2(vii) (answers :52).
- (c) **An admission ruling**, in ruling 8's form but with its own table. Ruling 8's machinery caps at nine units, the PI's nine, in note spans only (Q §4c(iii), `268787f`:121; `README-NOTE.md@f935864:122`), so this needs its own table.
  - Probe: nr_check_admitted passes on each of the 11 with one candidate per line, declared one at a time in memory. The candidates are cited_source "the source" (:15, :101), "v5 Figure 5" (:228; "Figure 20" also passes for S8#2020), "v5, §3.3" (:110) and "§6" (:236). Each note_quote is verbatim on its line and carries the unit.
  - The run-level table checks were not run on such a table.
- (d) **Left not found:** fails the pass.

**Code recommends (b),** with (a) as good if the seat holds a copy. Either settles S5#2048. The version for reading (5) is settled only if §6 is read in both v1 and v5, or the seat names the version. For a curve reading that the figures give only by eye, Code recommends (c) for that row, rather than a number read by eye.

### 2b. The note's own arithmetic on committed inputs, printed by no committed carrier (24; chains K5, K9, K10)

All 24 are on the release block's pass 3–11 list (:32), which prints every one of them. That list is not a carrier: no pin class reaches the release block. On Code's reading, 4e keeps the block as a listing by source (answers :55), not as a carrier.

| Rows | v0.8 line · units | Committed inputs |
|---|---|---|
| S8#2032–S8#2036 | :230 '17/96', '0.177', '0/96', '25/96', '0.260' (‡(c), every excluded trial counted NO) | affirm counts 25/17/0/0 over 96 trials run per stage, N2@09c3a8c:90-93, and the criterion-arm artifacts `data/olmo/b2r_control_{base,sft,dpo,instruct}.json@bbc9ffe` |
| S8#2037–S8#2040 | :230 '12/48', '9/48', '0.06', '.31' (the SFT injected arm, same convention) | 12 hits and 9 false alarms (N2 :61-62) over 48 per arm (N2 :136); `data/olmo/b2r_explore_sft.json@bbc9ffe` |
| S8#2095, S8#2097–S8#2100 | :236 '10,000', '200', '.003', '0.9', '.17' (‡(f), the fifth premise and its tests) | v1 pooled rates, N2vi@09c3a8c:21-22, :25-26 (rows 3, 4, 7, 8); the twenty configurations, N2vi :29 (row 11); 500 injection and 10 control trials per (layer, strength), N2(vii)@8d68b0b:89. The instruct test is taken at the v1 text's 0% FPR, R1's reading of N2vi row 8 (:26: record 0.003, source v1 text 0.000) |
| S5#2055, S5#2056, S5#2057, S5#2059, S5#2060 | :110 '2.2', '2.5', '0.55', '1.85', '2.48' (*c* and the pre-ablation *d*′) | rates 0.108/0.000 → 0.638/0.073, N2@e60b633:81-82, :444-447 (pre-ablation *d*′ "undefined", no *c* printed); 500 concepts and 100 injection trials per concept, N2(vii)@8d68b0b:68, :78; one control trial per concept (the note's premise) or the released code's ten (`RESULTS.md@bbc9ffe:7435-7436`; N2@09c3a8c:136) |
| S8#3019, S8#3022, S8#3024, S8#3026, S8#3027 | :242 '0.55', '1.85', '2.48', '2.2', '2.5' (‡(i), the same values) | the same |

**Code's scratch arithmetic is not a carrier** (ledger 27; round 8's D1 and D5, script :9363, :9241), and this list prints none of the values it gives for these 24. Five K5 comments in this group carried such values; Code withdrew them at integration (E11, §0). The chains' checks (K5, K9, K10) agree with the note at its printed precision.

**A computation raw is ready (option (a)).** Code has drafted (not committed) a computation raw: 24 of 24 agree with the note as printed. If the seat admits it, Code commits it with its own pin class, and the 24 rows become audit-raw-new, computed-new. Its date (2026-10-29) falls outside N1's item-raw pattern, which admits 2026-10-08 and 2026-10-09 only (script :2406). It needs a pin class, as 4b gave N2(vii). Its method, as the raw states it:
- **Inputs read at their revisions.**
  - Every read is `git show <rev>:<path>`, and each blob is hashed. No working-tree file is read.
  - Each input line is asserted to carry the text quoted from it.
  - The inputs are cross-checked against one another: N2's tables against the record's artifacts and their trial recounts; N2vi's rows against its JSON; the ablation rates against v5's sentence (N2(vii) :97) and the record line.
  - It uses the standard library only, with no model, no randomness and no network. Two runs differ only in their stamp line.
- **N2's own functions.** z, the log-linear *d*′, the one-sided Fisher test and half-up rounding are compiled from `scripts/audit_note_N2.py@e60b633` (:98, :214-217, :220-227, :230-231), not re-implemented. They reproduce 20 committed outputs of `results/raw/2026-10-08_note-N2-roc.json@e60b633` exactly.
- **One-sided Fisher.** Each *p* is the one-sided Fisher exact test, H1 hit rate > false-alarm rate. That is the test the note names at :99 for the same SFT comparison on decidable trials, and the test N2 applies to the source's points at every premise (N2@09c3a8c:457). The note names no test at :230 or :236 (§5 #29). The two-sided values do not round to the printed ones.
- **The log-linear reading of "half-count".**
  - The note's "half-count correction" (‡(i)) and "corrected *d*′" (‡(f)) are read as N2's log-linear rule: *H*′ = (*h* + ½)/(*N*s + 1) and *F*′ = (*f* + ½)/(*N*n + 1), applied to every cell (`results/raw/2026-10-08_note-N2-roc.json@e60b633:61-62`).
  - That is Code's reading, and it rests on provenance: the note's other corrected *d*′ values (:99, :101) map to N2's log-linear outputs.
  - The note's precision cannot tell this rule from the zero-cell-only rule, and every corrected figure agrees under both. The post-ablation values are the note's uncorrected ones.
- **The agreement rule.**
  - An exact count or fraction agrees only if it is equal.
  - A decimal printed with *d* places agrees only if the computed value, rounded half-up at *d* places on its exact decimal expansion, equals it. "≈" changes nothing.
  - Each row prints its margin to the nearer edge of its rounding interval, so an agreement that rests on a near-tie would show.
- **Premises.**
  - The premises are computed as the note states them, not adjudicated: ‡(f)'s 500/10 per (layer, strength) from v5's C.2, pooled over twenty configurations; and ‡(i)'s one control trial per concept (stated by no source) or the released code's ten (the OLMo stage-comparison script's default, applied to Gemma; §5 #9).
  - The raw records, without adjudicating, that C.2 says its detection rates "are approximated by the logit difference Yes − No" (N2(vii) :89). It also records that pooled counts treat clustered trials as independent (`results/raw/2026-10-08_note-N2-roc.json@e60b633:66`).
- Before commit, Code regenerates the raw from the committed copy of its script, and re-points its references to this list's sections to this file.

**‡(c)'s premise has no committed carrier either:** "Macar et al. 2026 methods grade a non-answering or incoherent response NO and retain it (v1, Table 4)". N2@09c3a8c:458 says the source's grader is not identified (§6 item 3). A related record, `results/raw/2026-10-08_note-N12-licenses.md@09c3a8c:60`, reads Table 4 of v5's HTML Appendix A as the task's full prompt, which bears on the note's "(v1, Table 4)". The raw computes the nine ‡(c) rows on the note's convention as stated; whether the convention is the source's stays open.

**Options (the seat's).**
- (a) Admit the computation raw. Code commits it with its own pin class, and the 24 rows map audit-raw-new, computed-new, and pass under ruling 5.
- (b) A ruling instead, for example one admitting the release block's listing as their source. That goes beyond 4e. For pass 12, the seat chose a committed transcription (4c, answers :53) over Q's "(i) admit the block as the carrier" (Q §4c, `268787f`:119).
- (c) Left not found: fails the pass.

**Code recommends (a):** one raw on committed inputs, and one pin class. It is not on answers §10's list, so it needs the seat's word and room in the PI's timeline (answers :24).

### 2c. The five Tagliabue and preprint units

S7#19 and S7#20 pass as admitted citations (1a). S7#28, S7#25 and S8#3143 are 1b items 6, 7 and 8. Between them, their locators record the search: `git grep` at `f935864` and `908a659`; the record at `bbc9ffe`; and `PREPRINT-v1_0-draft.md`, which no pin class reaches (it is tracked only from `98d07bc`).

## 3. The discrepant figures (19)

The branches are as v0.6's NR_DISC_PATH defines them (script :13314-13322: T and C come from v0_4 through v0_5, :8128-8144 and :11137-11138; TS is v0_4_r9's text, :10846-10851, with v0.6's render clause; NT is v0.6's own). The v0_8 profile carries them unchanged (working tree).
- **T**: transcription not yet corrected where the row sits. AUDIT :23 calls for the correction; with the note frozen, Code reads that as the correction block. Not a STOP.
- **C**: corrected in the note: the item raw's correction quoted from its figure row (corrected_in_note), or R1's.
- **TS**: transcription whose scope, bound or referent correction the note applies (ruling 6; ruling 13 on a render).
- **NT**: not transcription; a STOP on the item unless reworded (ruling 7). Its text names v0.6's ":111", and Code restates it for :250 when ruling 7 is re-keyed.

| Row | File:line | Unit | The note vs the carrier | Branch | Reached by | Probe |
|---|---|---|---|---|---|---|
| S1#134, S1#214, S1#215, S1#216 | note:14 | .94, .995, 50, 63 | ".94–.995 over layers 50–63" vs N3@09c3a8c:370: 0.941–0.995 on L50–L63; the source's "every layer above 48" includes L49 = .695 | TS | ruling 6, the seat's re-key (1b item 3) | pass |
| S4#4, S4#5, S4#38, S4#39 | note:83 | 0.94, 0.995, 50, 63 | the same range and carrier, written "across layers 50 through 63" | TS | ruling 6, only with 1b item 4 | fail |
| S4#10, S4#11 | note:85 | 0.81, 0.96 | "0.81–0.96 … from layer 51 onward" vs N3 :385: 0.808–0.964 on L51–L63, L49/L50 .536/.534 | TS | ruling 6, the seat's re-key (1b item 3) | pass |
| S11#18, S11#19 | F1a:17 | .81, .96 | "≈1.0 · .81–.96 / at first and second label, / from L51." vs N3 :385 | TS | ruling 13, Code's verbatim re-key, held for the seat (1a; 1b item 1) | pass (held in 9d) |
| S5#38 | note:99 | 0.095 | +0.095 vs N2@09c3a8c:51: +0.095455, "transcription, correct to +0.095" (AUDIT :32's +0.096) | C | none needed | passes now |
| S5#81, S5#88 | note:93, :99 | 0.000, 0% | 0 vs N2vi@09c3a8c:26: record 0.003, source v1 text 0.000 | C | R1, the seat's re-key (1b item 2) | pass |
| S10#108, S10#60 | F2:54, :90 | 0.000 | as S5#81 | C | R1, Code's verbatim re-key (1a) | pass (applied) |
| S8#3074, S8#3075 | note:250 | 0.8, 2.0% | "0.8–2.0% by arm" vs N5@09c3a8c:217: 0.79–1.99% by arm, sham highest; the discrepant figure is AUDIT :98's "termination attempts ≈ 1% of rounds by arm" | NT | ruling 7, the seat's re-key (1b item 5) | pass |

No discrepant row reads as branch T (the dev report's T-row list is empty). Each NR_DISC quote that Code declares is in its row's cause (asserted).

## 4. Units the blocks list, and units mapped by a reading

### 4a. "Seven days" (pass 23; the seat's)

- **Rows.** S1#1000 (:3), S1#1020 (:23), S8#1002 (:214).
- **Sources.**
  - Their only sources are the answers block (answers :22, :55) and the additions raw (additions :80, "the PI's choice of N on 2026-10-27").
  - Both are pinned with `908a659`, because the working-tree script applies 4c's pin class to that commit (wt :14629-14631, :14692; Code's mechanization).
  - Neither is an item raw or a record line, so on that mechanization neither carries a figure.
- **As rowed.** All three are not-figures, a release commitment. The precedents are v0.6's S1#141 (a design description) and S2#42 (the program describing itself).
- **If ruled figures.** They become three not-found figures. Their passing routes would be admission, or a committed carrier with its own pin class. At the flip, the three sentences return to link form on the post (answers :23).
- Code has aligned S8#1002's not_figure_reason to S1#1000's (chain K1's) text (E6), so all three group as prose. The kind is the seat's to rule (O36). Code recommends not-figure.

### 4b. Listed only by the release block

- The 24 rows of §2b.
- The 4/48 and 2/48 at :114 (S5#2064–S5#2067).
  - These are listed as an addition only by the release block (:32), but they have a carrier.
  - They map record, log-only, on `RESULTS.md@bbc9ffe:7072-7073` and :7085-7087, where the record prints them; N2vi@09c3a8c:175 quotes them too.
  - Code's reading is that this stands.

### 4c. Readings the seat may want to confirm (Code's recommendation in each)

- **W5's condition 4 on :101** (N2vi@09c3a8c:620).
  - Four rows name a premise that :101 does not spell out: S5#113 (1.5 at 16,000/1,600), S5#2000 and S5#2005 ('four'), and S5#122 ('three').
  - :101's ‡ marks point to the ‡ section (:224, items (a)–(k) at :226–:246), whose (f) at :236 states the premise. Code reads that pointer as meeting condition 4.
  - The analogy is Code's round-10 reading (d) of line 3's by-line reference (v0.6 ledger 9e W5, :1777; 9h O11 (c), :2143). Reading (d) was applied as Code's reading, not ruled (:1801).
- **S5#2034 'zero'** (:106, "hits above a zero false-positive rate").
  - It is mapped to DPO's 0% (N2vi row 7, log-only). If the seat reads it as covering instruct too, it maps to N2vi row 8, and R1 would have to be keyed to it as well.
  - S5#122's instruct half already rests on R1 (N2vi :539 vs :540).
  - Code reads it as DPO only.
- **A0 carriers outside 4a.**
  - The additions raw names files outside 4a's class: LOCK-m-F0@`d474406` and the extractions raw @`0fa8539` (additions :10), and the G-CAL JSONs (additions :21, :33).
  - The rows cite `RESULTS.md@0fa8539` (its lines 1-383 are identical at `79d462b`, which no row cites), the verdicts raw `results/raw/2026-10-19_m-verdicts-qf0.txt@bfc179c` or `PROPOSAL-m-gating-campaign-v1_11.md@bbc9ffe` instead. For example, S1#1014 and S6#92 cite :326 for the pre-registered α = .01.
  - Code reads these as sufficient. The seat widens 4a only if it wants the named files cited.
- **4a's scope.**
  - The class is path-and-revision wide: every line of RESULTS.md at `0fa8539` and `79d462b` counts as record. No row's locator, source value or status basis cites a line outside the VERDICTS entry (Code's re-check: the 48 such citations over the rows of chains K1, K3, K6, K7, K10 and K11 all fall in :24-383); two comments do: S8#3072's (:4553-4556, below) and S8#3085's scope note (:3673, the seat's E4).
  - S8#3072's measured 16/16 sits in the G-CAL entry (`RESULTS.md@0fa8539:4553-4556`). Citing it needs no script change. Chain K10 left it out because 4a names the VERDICTS entry. The seat says whether 4a extends past that entry.
  - Code recommends no change.
- **:177's "79 of 80"** (S7#1001, S7#1002).
  - It is mapped under 4a (`RESULTS.md@0fa8539:25`, :112, :127-128), though the additions raw's A0 list names only :17 and :161 (additions :14, :25).
  - Code reads 4a as covering it.

### 4d. Kind calls (the kind hash freezes at integration)

| Row · line · unit | As rowed | The alternative | Code's recommendation |
|---|---|---|---|
| S7#1021 · :204 · 'three' ("Its authors attach three caveats") | not-figure (chain K7's check, by v0.6 S7#21 'Four' and S2#29) | figure, computed-new on Chandaria raw :17 (row 6), the mapper's reading; the raw's §2 lists no count of the caveats (:27-33) | not-figure |
| S5#1007 · :97 · 'zero' ("what a zero false-positive rate reveals … depends on sample size") | not-figure | figure on L002/L003 (K4); compare S5#2034 at :106, a figure | not-figure |
| S5#1000 · :93 · 'two' ("two arms per stage") | figure, record log-only | not-figure, as S5#2021 at :101 ("two LoRA-DPO controls") | figure (it states the design; its scope is §5 #3) |
| S8#2010 · :228 · '1' (α = 1) | figure, computed-new (Figure 5's plotted strength, N2(vii) :64) | — ; '2' and '4' in the same clause are not found (2a) | as rowed |
| S8#2002 '0' (:228 "0-based"), S8#2045 'four' (:234 heading), S8#2081 'two', S8#2087 'three' (:236) | figures | not-figures | as rowed (chain K9's calls, contestable) |
| S6#1005 'Two' (:145 guardrails), S6#1000 and S6#1007 'three' (:122, :151), S6#1006 and S6#1028 'one' (:145, :161, "one … the other") | not-figures | figures; v0.6 S6#80 read "one map returned +0.1667" as a figure | as rowed |
| all 38 row-less ordinal hints in S1–S8 (S1 1, S2 6, S4 6, S5 2, S6 8, S7 7, S8 8: Code's count of the matcher's outside hints) | no rows (round 10's rule) | not-figure rows | as rowed |

## 5. Correction candidates for the post-flip correction block

The note does not change. None of these changes a ledger status as recorded. #37 may change a printed value at T+3, and #23 assumes the first reading of 1b item 5 (b). "Rows" are the rows carrying the point. "N1" marks a correction N1 records itself (NR_CORRECTIONS, Code's; only #32). Each point is Code's reading of the carrier, or a chain's where marked. The wording is the seat's.

| # | v0.8 line · rows | Kind | What the note says → what the carrier supports | Evidence |
|---|---|---|---|---|
| 1 | :41 · S2#17, S2#102, S2#103, S2#124 | scope | The R² = 0.53 calibration drops "cycle 2", and "our calibration" is not renamed | `results/raw/2026-10-08_note-N10-horn1.md@09c3a8c:292` (a), :293 (b) |
| 2 | :49 · S2#1009 | scope | "first-pick habit 83.4%" now stands in §3 for all sessions. It is e2a's figure: 156/187 over all arms, excluded sessions included | N4@09c3a8c:369 |
| 3 | :93 · S5#1000 (S5#1001, S5#1002, S5#1005) | scope | "two arms per stage": base ran the criterion arm only | N2@09c3a8c:372; `ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:205`; `results/raw/2026-10-08_note-N16-decoding.md@09c3a8c:36` |
| 4 | :118 · S5#30 | scope | "no detection claims at any stage" holds for the fidelity arm; the register arm had 4 v1-scored claims at SFT | N2@09c3a8c:42 |
| 5 | :145 · S6#71 | scope | "One stage, DPO, showed a shift on one label map" holds within the marker arm: 17 of 22 arm-campaign cells have a map with \|Δ_map\| ≥ 0.10. Not applied since v0.4 | `results/raw/2026-10-08_note-N14-artifacts.md@09c3a8c:418`, :454 |
| 6 | :228 · S8#2005, S8#2006 | scope | "0.35–0.57 … across stages" means the three stages that ran the injected arm (chain K9; base fraction not re-checked) | N2@09c3a8c:372 |
| 7 | :228 · S8#2024, S8#2027 | scope | "rounding 64 × 0.7 = 44.8": neither int() nor round() yields the caption's list, and this is not adjudicated | N2vi@09c3a8c:467-468 |
| 8 | :236 · S8#2060, S8#2061, S8#2081 | scope | "In every premise, the 100 injection and 10 control trials … are the released code's defaults": not at the fifth premise, which is C.2's 500/10 per (layer, strength) | N2(vii)@8d68b0b:89 |
| 9 | :242 · S8#3025 | scope | "the released code's ten" is the default of the OLMo stage-comparison script, applied to Gemma as a premise | `RESULTS.md@bbc9ffe:7431-7436` |
| 10 | :256 · S8#3085 | scope | "Fourteen small differences …, none touching the read": items (9), (10) and (12) bear on reads. The claim holds for the first-choice read | `PROPOSAL-m-gating-campaign-v1_11.md@bbc9ffe:267` |
| 11 | :89 · S4#1000 | scope | "a binding that no linear probe finds at any layer through 63": only one linear estimator was tested | N3c@09c3a8c:171; N3@09c3a8c:443 |
| 12 | :85, F1a node 17 · S4#8, S11#17 | scope | "≈ 1.0 at the first label" holds through L62; L63 reads .988 (v0.6 ledger 4g C6, carried) | N3@09c3a8c:384 |
| 13 | :250 · S8#3072 | wording | "(G-CAL)" names the calibration gate as the corruptor (O33's residue; chain K10, not re-checked) | v0.6 ledger :2165 |
| 14 | :14 · S1#1009 | wording | "AUC up to .97" quotes the MLP peak with no specification caveat, and the parity reading lacks :87's "post hoc" | N3c@09c3a8c:207 |
| 15 | :87 · S4#17–S4#20 | wording | The RBF grid caveat and the MLP specification caveat are dropped, and "performed post hoc" drops the computed-new label. F1a node 21 keeps "(grid floor)" | N3c@09c3a8c:203, :207; N3@09c3a8c:478 |
| 16 | :17, :159 · S1#1013 | wording | "two truthful banner lines naming which label is which and which to prefer": only TOLD-MAP names them; COMMON announces the choice phase. :159 states both correctly | `PROPOSAL-m-gating-campaign-v1_11.md@bbc9ffe:254-255`, :258 |
| 17 | :65 · S3#14, S3#15 | wording | "Paraphrasing included …": that list is the seven frame conditions, each in four paraphrases | `archive/RESULTS-cycles3-4.md@bbc9ffe:1603-1607` |
| 18 | :69 · S3#31–S3#34 | wording | "attenuating step-wise growth": the successive differences of N7's four printed values (:302-305) do not shrink at each step (Code's arithmetic, not a carrier; its values are not printed here), and N7 says strictly increasing. G_c's pooled-SD unit and tail-level qualifier are dropped (C16) | N7@09c3a8c:84, :289, :302-305; `RESULTS.md@bbc9ffe:8727-8728` |
| 19 | :73 · S3#53 | wording, disclosure | Δ+ = +0.285 names no readout or unit (N7 note 14). It is restored without v0.6's honesty notes (v0.6 :74): leave-one-out Δ+ is 0.085, and the top probe's shift is about twice its natural gap | N7@09c3a8c:296; `results/raw/2026-10-08_note-N8-link2.md@02b6a61:234`; `archive/RESULTS-cycles3-4.md@bbc9ffe:1442-1450` |
| 20 | :114 · S5#79 | wording | Qwen "classifies" which pole: the judge is an A/B read of which response is better | N4@09c3a8c:380 |
| 21 | :99 · S5#1009 | wording | "base is higher still at 0.431 here, 16.4% in the source's pooled rates" reads as base above SFT in the source, where 16.4% < 22.5% | N2vi@09c3a8c:23-24 |
| 22 | :99 · S5#47, S5#48 | wording | "exclude per-stage hit rates only above roughly 7–8%" drops v0.6's "(exact binomial upper bounds)" | v0.6 :98 |
| 23 | :143 · S6#101 | wording | "did not differ by arm" → "no detectable heterogeneity by arm (post-hoc exact test, *p* = .72)" (1b item 5) | N5@09c3a8c:217, :219, :122 |
| 24 | :145 (no unit) | wording | "a stop rule would have stopped the run": the declared monitors PAUSE to a design-instance disposition | `LOCK-g.md@bbc9ffe:146-150`; `RESULTS.md@bbc9ffe:8321-8326` |
| 25 | :145 (no unit) | wording | "The order of the runs was fixed in advance": scheduling is outcome-blind within a stage, but no cross-stage order was found (chain K6's search of LOCK-g §4-§5 and PROPOSAL-g §1, §4, not re-checked) | `LOCK-g.md@bbc9ffe:143-145`; `RESULTS.md@bbc9ffe:8315` |
| 26 | :177 · S7#1005 | wording | "the binding is one nonlinear step from it" lacks the post-hoc label that :87 carries | v0.8 :87 |
| 27 | :191 · S7#15 | wording | "established before the OLMo screen … A second": the pattern was first armed before e2b (PROPOSAL-h §5 at `34eb7ee`, before the e2b verdict campaign `485cc94`) | N13@09c3a8c:73 |
| 28 | :222 · S8#1019 | wording | "come from non-asserting clauses" is looser than N2's "carried only by" | N2@09c3a8c:27 |
| 29 | :230–:236 · S8#2040, S8#2044, S8#2098, S8#2100 | wording | p-values with no test named (Code's reading of AUDIT :12's rule 4, "every p its test") | AUDIT :12 |
| 30 | :234, F2 node 98 · S8#2049, S10#1007 | wording | "presented in figures at one configuration" → "in figures at *L* = 25 in the main text (Figure 5, α ∈ {1, 2, 4, 8}; Appendix D.1 adds *L* = 19 and 22)" | N2vi@09c3a8c:401-406; N2(vii)@8d68b0b:64-65 |
| 31 | :228 · S8#2101 | wording | "the next rung was incoherent at SFT and DPO": instruct's 2.0 rung is also marked incoherent (degenerate 0.2917 against the 0.25 bar), though the record's prose names only SFT and DPO | `data/olmo/b2r_analysis.json@bbc9ffe` (g3b ladders); `RESULTS.md@bbc9ffe:7050` |
| 32 | :248 · S8#3056 | wording (N1; v0.6 S6#26, O31) | "depending on how its map-consistency conjunct is read": the endpoints differ in conjunct (1), the sham envelope | N4@09c3a8c:238, :255; v0.6 ledger :2163 |
| 33 | :250 · S8#3061 | wording | (a)'s "44 of 56" is FDBK's declared 56; (b)'s "the 56 valid sessions" is CORR's | N5@09c3a8c:81-82 |
| 34 | :258 · S8#3143 | wording | "separately from the ten" has no antecedent (1b item 8) | — |
| 35 | :258 ‖‖(c) | wording | "reproduces every output stored in the notebook" → "every stored printed output" (O9's residue) | `results/raw/2026-10-09_note-N19-cacophony.md@e0fd85c:34` |
| 36 | :240 · S8#3008 | wording | v5 cites Table 3 as a whole for "which component of DPO is responsible" (chain K10) | N2(vii)@8d68b0b:15 |
| 37 | :202, :258 · S7#1015, S8#3125 | precision, pending T+3 | 48.9 against 80.2 − 31.2 = 49.0 from the rounded rates; the T+3 table check decides | correspondence raw :22, :42 |

## 6. Other items for the seat and the PI

1. **O14 and AUDIT :10** (the PI's and the seat's; STILL OPEN in v0.6, v0.6 ledger :2146).
   - AUDIT :10 asks that a log-only figure's sentence be downgraded.
   - v0.8 has no epistemic-status line. :214 says only that the claims ledger "maps all figures in this post to their sources". So the 187 log-only figures carry no in-text downgrade. Block :10's downgrade, which v0.6 carried by one weight sentence (PARTLY APPLIED, v0.6 ledger :1936), is NOT APPLIED as written in v0.8 (Code's O14 text, wt :15294-15300; the S5 span disposition, wt :15692).
   - Whether one blanket sentence discharges AUDIT :10's per-sentence downgrade is the PI's reading (O14 (e), v0.6 ledger :2146). On Code's reading the same question now covers :214's pointer.
   - Code recommends that the PI rule on (e), or that the seat put a sentence in the correction block.
2. **Render items for the Digest seat, through the PI.** The renders posted as filed (release block :3).
   - **F1a nodes 42-43 (10-22).** They give "the OLMo dose escalation" as a link-2 "concluded, not answered" cell; that cell is Qwen's e2d (`results/raw/2026-10-08_note-N8-link2.md@09c3a8c:161`). It and "the first echo confirmatory stage" have no counterpart in v0.8 (grep: no "dose escalation", "e2d" or "confirmatory stage"; O23 (j)).
   - **F1b (10-22).** O24's four wording items are still open: no MDE line is drawn; "first picks" lacks "free"; the note says "every RBF fit"; the MLP's "specification-dependent" caveat is missing (v0.6 ledger :2156; chain K11, not re-checked). Code re-keys O24 to the 10-22 file.
3. **‡(c)'s grading premise** (2b). Whether v1's Table 4 holds the rule "grade a non-answering or incoherent response NO and retain it" is unverified (N2@09c3a8c:458). `results/raw/2026-10-08_note-N12-licenses.md@09c3a8c:60` reads Table 4 of v5's HTML as the task's full prompt. The premise conditions the nine ‡(c) rows, S8#2032–S8#2040.
4. **The tag.**
   - v0.8 :214 and the footers of all three renders (F1a node 45, F1b node 222, F2 node 103) name `note-2026-10-v2`. It does not exist at `f935864` (`git tag`), so the release must cut exactly that name (answers :66).
   - S8#1008's "prints 154/154 from a fresh clone at the tag" rests on `results/raw/2026-10-08_note-N11-smoke.txt@02b6a61:742`, which predates the tag.
   - The release-commit run is owed (answers :87, §10 item 4). It becomes a correction only if it prints something else.
5. **The additions raw** (the seat's file; where it and release block :32 overlap, 4e keeps the block's listing as the source, answers :55).
   - §2 row 11 says the "7/44, +0.14, .10 forms" are "not in v0.6". v0.6 :98 carries "12/40 against 7/44, +0.14, p = .10" (additions :57).
   - §2 row 10 says "the 25/58 fraction is new in v0.7". v0.6 :92 already reads "25 of 58 decidable" (additions :56).
   - §1 omits :177's "79 of 80" (4c).
6. **Pass-12 rows.** The 28 computed-new rows on the correspondence raw each say "verification pending T+3" in their comment. Code holds none of them (no cn_held) unless the seat asks.
7. **Link 3 (information only).** v0.8 drops v0.6's random-direction comparison (v0.6 :85; N3@09c3a8c:388, "not axis-specific in presence"). v0.6 S4#40–S4#47 and S4#51–S4#59 retire. None of the retiring rows was discrepant.
8. **The PI's items that stay open in 9h.** On Code's reading, none of them needs an answer before the tag, and none moves a status unless the PI rules on it.
   - O28: :214's Q1-bet date (`72b09a9` (2026-08-20)), rowed not-figure (S8#111–S8#113); L089's status is outside N1's vocabulary (v0.6 ledger :2160).
   - O15: N13's order-test domain, verdict-cell definition and tier calls (v0.6 ledger :2147). Also :59's unscoped "All criteria, stop rules, and outcomes were collected with pre-registrations committed before data collection", against :212's verdict-tier scope ("Every verdict-tier gate, criterion and outcome wording was committed before its data"). That is Code's own re-reading; no chain raised it.
   - O9: whether N19's row :122 should read discrepant (v0.6 ledger :2141).

## 7. The pass arithmetic (695 figures)

**Method.** Each state is counted, not added, wherever it can be built in memory.
- A byte copy of the working-tree script (sha256 `fd361e5d…cd1f5`) is loaded as a module.
- `main()` runs as for `--dev-report` on the integration rows. The report function is replaced by a counter that receives `main()`'s own inputs: the provisional ledger and the item raws.
- The counter re-states `final_note_rows`'s pass part: nr_validate_row on every row, the effective status, the verified branch-C corrections, and nr_r9_pass (rulings 5–8 and 11–13). Only `final_note_rows`'s stop at its branch-C consistency check is left out, because S5#81 and S5#88 are branch C without their field until the seat answers.
- Each seat-answer state sets its candidate fields and table entries in memory, as the probes do.
- Steps marked "rows" need a script change, a new ruling or a committed raw that does not exist yet, so they are added by row count.
- One state applies every runnable answer together (ruling 13 confirmed, R1 on S5#81/S5#88, the six ruling-6 rows, ruling 7, S7#28). It counts 654, the sum of those steps. With ruling 13 still held, the same state counts 652.

| Step | Rows | Whose | Moves | Passing after | How |
|---|---|---|---|---|---|
| Now: v0_8 ruling tables empty, no ruling field | — | — | — | 637 | counted |
| 1a: R1 on S10#108, S10#60; ruling 8 on S7#19, S7#20 (applied, E9) | 4 | Code (4f) | +4 | 641 | counted |
| 1a / 1b item 1: ruling 13 on S11#18, S11#19 (applied, held) | 2 | Code's step; the seat confirms | +2 | 643 | counted |
| 1b item 2: R1 on S5#81, S5#88 | 2 | seat | +2 | 645 | counted |
| 1b item 3: ruling 6 on S1#134, S1#214–S1#216, S4#10, S4#11 | 6 | seat | +6 | 651 | counted |
| 1b item 5: ruling 7 on S8#3074, S8#3075 | 2 | seat | +2 | 653 | counted |
| 1b item 6: ruling 8 on S7#28 | 1 | seat | +1 | 654 | counted (the joint state counts 654) |
| 1b item 4: ruling 6 on S4#4, S4#5, S4#38, S4#39 | 4 | seat, with Code's reader change | +4 | 658 | rows (on the current reader: +0, counted) |
| 1b item 7: ruling 8 on S7#25 (check change) | 1 | seat | +1 | 659 | rows |
| 1b item 8: S8#3143 (new ruling, check change) | 1 | seat | +1 | 660 | rows |
| 1b item 9: ruling 11's not-figures S8#3100–S8#3102 | outside the 695 | seat | 0 | 660 | — |
| 1b item 10: ruling 12 | 7 rows, already passing | seat | 0 | 660 | counted (in the 637) |
| 1b item 11: R3 | no figure | seat | 0 | 660 | — |
| 2a: the 11 v5 readings | 11 | seat (a download needs the PI's approval) | +11 | 671 | rows |
| 2b: the 24 computations | 24 | seat | +24 | 695 | rows |

Code's steps reach 641 now, and 643 with ruling 13, which Code has applied but holds for the seat. Every step after that needs the seat's answer.

On Code's reading of answers :32 ("Round 11 runs at round 10's standard"; round 10's ledger: "The pass condition is met. 632 of 632 figures pass", v0.6 ledger :1694), the pass is met only at 695 of 695. Every item in §1b that has failing rows (items 1-8), §2a and §2b would then need a passing answer before the tag; items 9-11 move no figure. No committed ruling makes AUDIT :23's pass a precondition of the tag. If the seat picks an option that leaves figures failing, the round-11 ledger records the pass as not met and lists them, and whether the tag waits is then the PI's and the seat's call.

What could move the count the other way:

- **The seat declining a 1b answer.** Each item among 1-8 that the seat declines (a re-key, or for items 7 and 8 the admission ruling) leaves its rows failing; items 9-11 move no figure.
  - If ruling 13 is not confirmed, the two F1a rows stay open.
  - Declining R1 on S5#81 and S5#88 leaves those two rows failing.
  - Declining ruling 6 leaves the six rows failing, and S4's four with them.
- **W8 at :143** (1b item 5 (b)). If the seat reads :143's '1%' as W8's by-arm figure, S6#101 maps to N5 :217's discrepant row (branch NT). Ruling 7 cannot pass it, because :143 states neither W8 state (probe). That is one passing figure fewer, and a STOP on the item.
- **S5#2048** (2a). A v5 transcription may not carry its quotation, given the conflict with N2vi :404. The row then stays not found, or reads discrepant against the transcription.
- **S5#2034 read as covering instruct** (4c). It maps to N2vi row 8 (discrepant) and passes only if R1 is keyed to it too.
- **Kind calls** (4d), each changing the denominator:
  - each 'seven' ruled a figure: +1 figure, not found, which passes only by admission or a committed carrier with its own pin class;
  - S5#1000 (log-only) made a not-figure: −1 figure and −1 passing;
  - S8#2002 and S8#2045 (log-only), and S8#2081 and S8#2087 (computed-new), made not-figures: −1 figure and −1 passing each;
  - S6#1000, S6#1005, S6#1006, S6#1007 or S6#1028 made figures: +1 figure each, with no mapping yet, so not passing until mapped;
  - S7#1021 ruled a figure: +1 figure, which passes only if the mapper's reading holds (computed-new on Chandaria raw :17, row 6). Code doubts that reading, because the raw's §2 lists no count of the caveats (:27-33), so on Code's reading it adds a failing figure.

One kind call would add a passing figure instead, so it is not "the other way": S5#1007 ruled a figure adds one that passes (reproduced, on chain K4's mapping).
