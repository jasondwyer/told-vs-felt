# n — G-VEC's run entry and STOP block: the blind values-check, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the drafts of G-VEC's run entry and its STOP block for the
seat:
- T1, the entry: `a4076504…5d32` (106 lines), its values-check paragraph a placeholder;
- T2, the STOP block, `results/raw/2026-11-19_n-gvec-v1_code-to-design_STOP.md` here: `899020ff…f55f` (118 lines).

**The checker's brief** (`9fa078f8…2177`, 86 lines, given to the checker as a file, with its sha256 to verify):
- named the texts and the sources: in Code's scratch, by name and sha256, the box's ten copied-back files, the four
  launch files, the launch review's report, Code's departure note and the coordinating session's routing of the STOP
  as received; in the repository, the seat's answers, PROPOSAL-n v0.2, ADDENDUM-n1, the eleven readings' block,
  RESULTS.md's entries of `da7bdec` and `9f64305`, `gvec.py`, `.gitignore`, two earlier values-check raws, and BK's two
  committed analysis files by exact name;
- asked for every factual claim to be checked: each figure, quotation, hash and hash abbreviation, citation, and
  statement of what the run printed, what the record holds, what the launch files and their tests did, what the
  review found, what the routing and the answers say, and each departure; the arithmetic; and whether anything in T2
  weighs a cause, which it must not;
- allowed `shasum` by name (on this machine a Perl script, which the list of record's item 1 permits), and barred any
  other interpreter, any write, any network, any guard marker in an argv (a grep pattern included), anything under
  `data/mf3`, any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the named
  files and the brief itself;
- quoted the list of record v2's items 1–5, verbatim; required item 3's pathspec and the `data/mf3` exclusion on every
  git command over the tree, with `.` as the include for `git ls-files`, that a glob is expanded and read before it is
  looped over, and the `rev-parse` form for a tracked-and-clean check.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (461 lines, sha256
`b79a1efa…2c6f`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 89 items: 71 CONFIRMED, 9 IMPRECISE, 0 FAIL, 9 NOT CHECKABLE; and 11 observations. To the brief's
question, the checker found that T2 weighed a cause in one clause (item 86), and named two juxtapositions a strict
reading would count (observation 2).

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

- **The IMPRECISE items,** each applied in the checker's words or near them:
  - 10 ("checked and frozen"): T1 and T2 now say the launch files were checked, and frozen at the hashes sent to the
    coordinating session, when the answers came. That is the freeze the word meant; the note itself is frozen at the
    relay, which followed the answers;
  - 29: the box's 473 is the laptop's 462 plus 11 more, its 13 HF checks in place of the laptop's two skip lines;
  - 40: the seat's §7 that ruled the step-0 class inert is the one backend-ext-2's entry (`9f64305`) records;
  - 44: the launch reviewer's `git ls-files` runs lacked item 3's full pathspec and the mf3 exclusion, and the last
    printed three names instead of a count;
  - 53: "G-VEC runs as built" is the answers' §0, with G1, G3, G6 and G9 standing at §1.1–§1.4;
  - 62: the longest input, 90 tokens, is over all the ids of record, a context's, in a bullet of its own;
  - 77: the eleven readings' block gives about 1,900 forwards for any capture clause struck but the centring;
  - 81: "Another answer", as the block writes it;
  - 86: BK's scale now states its text bare: 7.6473 at ρ = 0.30, from which n §2.3 takes R ≈ 25.49. The clause that
    drew a conclusion from it is gone.
- **The NOT CHECKABLE items** stand: 13 (the launch's clearing, its quotation marks now dropped by observation 9), 19
  (v1's note), 23 (the launch harness's mutants), 42 (Code's `jq` reads), 47 (the checker's own departures), 50 (this
  commit's plans), 74 and 78 (paths (a), and (a) then (b)), and 87 (the claim on BK's code, which now rests on n
  §0.8's words by observation 8).
- **The observations:**
  - 1 asks for nothing: the close line on `99196e1`'s entry is committed at `1194982`, which this commit sits on.
  - 2, applied: the smoke's R_ℓ no longer stands beside the 2× quotation, and the index's figures no longer stand
    beside the index; both figures stay in the block's §1.
  - 3 holds with items 86 and observation 2 applied.
  - 4, applied: the block writes "the answers' §1.1" at its first use in each section.
  - 5 asks for nothing: the entry follows the review's headline figure, nine.
  - 6, applied: the address and port count was on the text files.
  - 7, applied: the entry names ids.py's manifest constant without writing it.
  - 8, applied: "BK's own capture code, which n §0.8 says BK's repository does not hold".
  - 9, applied: the quotation marks around the launch's clearing are dropped.
  - 10 asks for nothing.
  - 11: the committed close line keeps "checked and frozen", which the entry and the block now give in full; the two
    differ in wording only.

## 2. The text changed after the check, and the edits checked by tool

- **The text changed after the check** by the dispositions above, and in T1 by its values-check paragraph, which
  replaces the placeholder, and by a fuller statement of the checker's departures.
- **The edits, checked by tool:** a fixed-string count over each text unwrapped, for each disposition's new wording
  and each removed wording's absence: 33 of 33.
- **The finals:** the entry `46c4ca6e…d8d6` (125 lines); the STOP block `dfdc97b0…fce6` (120 lines).

## 3. The report as returned

VALUES-CHECK: T1 (S/step4b/gvec/stop/entry_src.md) and T2 (S/step4b/gvec/stop/stop_block.md)

**Hashes and HEAD**
- Every file was hashed with shasum -a 256 and compared in full. The brief (9fa078f8…2177, 86 lines), T1 (a4076504…5d32, 106 lines), T2 (899020ff…f55f, 118 lines) and all 17 named sources in S match the brief's sha256s and line counts.
- HEAD was a33252a at the start. 1194982 landed during the check: n-build's close lines on four entries, plus their values-check raw. HEAD was 1194982 at the end.
- Every named repository file is tracked and clean at both commits (rev-parse HEAD:path against hash-object). Of those files, 1194982 changed only RESULTS.md: 85 lines added in four close-line hunks, none removed.
- RESULTS.md anchors below are at 1194982 (R@1194982:N).
- Hash abbreviations were cut by tool from the full values.

**Short names**
- OUT = S/step4b/gvec/box/out/gvec_v1_out.txt
- RUN = S/step4b/gvec/box/out/run.txt
- SMK = S/step4b/gvec/box/out/smoke.txt
- POD = S/step4b/gvec/box/out/gvec_box_run.txt
- REC = S/step4b/gvec/box/rec/data/n/gvec/gvec.json
- SH = S/step4b/gvec/launch/draft/gvec_v1.sh
- MAN = S/step4b/gvec/launch/draft/gvec_manifest_v1.txt
- NOTE = S/step4b/gvec/launch/draft/gvec_launch_note_v1b.md
- REV = S/step4b/gvec/launch/review_report.md
- DEP = S/step4b/gvec/launch/departures_code.txt
- ROUT = S/step4b/gvec/stop/routing_stop_msg.txt
- ANS = results/raw/2026-11-19_n-starred-twelve_design-to-code_answers.md
- n: = PROPOSAL-n-bk-reconciliation-v0_2.md
- A-n1: = ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md
- ELEVEN = results/raw/2026-11-19_n-starred-eleven_code-to-design_STOP.md
- SL = data/n/bk/experiment_results_json/fixed_text_design/strength_ladder/analysis.json
- RED = data/n/bk/experiment_results_json/fixed_text_design/neutral_passages/reduced.json
- VCs = results/raw/2026-11-16_n-schema_valuescheck.md
- VCg = results/raw/2026-11-06_n-gdata_valuescheck.md

ITEMS

**T1**

1. T1:1–2. G-VEC ran from da7bdec; the smoke held; the run of record STOPPED at the R check, with R within 2% at neither index.
   - Verdict: CONFIRMED.
   - Evidence: OUT:2 (HEAD da7bdec2…0c23), :99–102, :120–122; REC:170–194 (within false at 31 and 32; status STOP).

2. T1:2–3. The quotation n §2.3 "reproduced at G-VEC within 2%, else STOP", and ADDENDUM-n1 §6.1.
   - Verdict: CONFIRMED.
   - Evidence: n:81; A-n1:52.

3. T1:3–4. G-VEC ran as built (the answers' §1.1–§1.4), on the PI's routing: item 1 of "N. n-build (and the pod session on the box)", on "Route as given".
   - Verdict: CONFIRMED.
   - Evidence: ANS:7, :16–22, :78–79; POD:2–4; a33252a's subject.

4. T1:7–8. gvec_v1.sh (f349e17d…a1ad) ended "gvec v1 STOP: …" with exit 2, on pod emw1e4embiwe9b, run by the pod session on the coordinating session's relay.
   - Verdict: CONFIRMED.
   - Evidence: shasum of SH; OUT:135; S/step4b/gvec/box/out/gvec_v1.exit reads "exit 2"; POD:1–6, :9.

5. T1:9–11. The quoted R lines at 31 and 32, and the STOP line.
   - Verdict: CONFIRMED, verbatim.
   - Evidence: OUT:120–122 = RUN:17–19.

6. T1:12–13. The BUILD entry's "Neither is a STOP"; gvec.json (3331da71…ee95) alone, status STOP, site null, exit 2.
   - Verdict: CONFIRMED.
   - Evidence: R@1194982:518; OUT:123–124, :129, :131; REC:185–186, :194; shasum.

7. T1:14–15. The smoke's figures: R 42.62270212364156 at 31 and 43.66884683035452 at 32; R_ℓ 22.23089391504287 and 22.167402391674045; two passages and two contexts.
   - Verdict: CONFIRMED.
   - Evidence: SMK:1, :8–9; OUT:100.

8. T1:16–21. What the STOP block gives; "Nothing is re-run, and Code adjudicates nothing".
   - Verdict: CONFIRMED against T2 §0–§5 and ROUT:18.
   - Its "not weighed" holds only once item 86 is applied.

9. T1:22–23. §1.1's quotation "if the change is cheap … comes from the re-run".
   - Verdict: CONFIRMED.
   - Evidence: ANS:16.

10. T1:23–24, T2:15–16 and T2:63–64. "already checked and frozen when the answers came".
    - Verdict: IMPRECISE.
    - "Checked" is supported. NOTE:24 was written with main at 99196e1, before the answers, which read 89a55c3's entry (ANS:3). REV:5 reviewed at da7bdec.
    - "Frozen" conflicts with the relayed note itself: "DRAFT, not frozen … The files are frozen at the relay under the sha256s it carries" (NOTE:5–7). The relay followed the answers (POD:2–6; T1:27–28).
    - The committed close line (R@1194982:296–297) uses the same words.
    - Wording for T1:23–24: "The launch files were already drafted, tested and reviewed when the answers came, so it was not added (Code's call, recorded in n-build's close line on `99196e1`'s entry)."
    - Wording for T2:15–16: "the launch files were already drafted, tested and reviewed, so G-VEC ran as built".
    - Wording for T2:63–64: "The launch files were drafted, tested and reviewed when the answers came, so G-VEC ran as built (…)".
    - If "frozen" means the hashes sent to the coordinating session, say so: "checked, and frozen at the hashes sent to the coordinating session".

11. T1:24–25 and T2:64–65. Code's call is recorded in n-build's close line on 99196e1's entry.
    - Verdict: CONFIRMED at 1194982.
    - Evidence: R@1194982:290–297: "Code's call (§8 item 1: "if cheap, else as built"): the launch files were already checked and frozen, so G-VEC runs as built."
    - At a33252a the close line was not committed: RESULTS.md@a33252a:186–233 had none.

12. T1:25 and T2:65. The record holds R at both indices alone.
    - Verdict: CONFIRMED.
    - Evidence: REC:170–192.

13. T1:27–28. Relayed at their hashes with "launch cleared" on the PI's routing.
    - Verdict: NOT CHECKABLE.
    - The relay at the hashes is supported (POD:25–26).
    - The quoted "launch cleared" is in none of the sources: grep over POD, ROUT, NOTE and REV found nothing. NOTE:5–6 has "relays the PI's word and clears the launch".

14. T1:28. The script has 272 lines, its commit is da7bdec, and its driver line is fecde87a…3958.
    - Verdict: CONFIRMED.
    - Evidence: wc -l; SH:45–46; rev-parse da7bdec = da7bdec2…0c23; `git show da7bdec:scripts/n_sessions.py | shasum` = fecde87a…3958.

15. T1:28–29. Manifest e05e0b3d…1e2c, 59 files, each asserted equal to da7bdec's blob.
    - Verdict: CONFIRMED.
    - Evidence: shasum; 59 lines; NOTE:14–15. The box's step 1 passed 59 of 59 in the clean copy at da7bdec (OUT:2–3, :5–63).

16. T1:29–30. Hashes file 881b79e7…e493, 13 lines, from a git archive of da7bdec in a battery window.
    - Verdict: CONFIRMED, as NOTE:19–20 states it.
    - Evidence: shasum; cmp equal to S/step4b/gvec/box/out/hashes.txt.

17. T1:30–31. The note v1b (ffb4e035…b273, 136 lines) stays in Code's scratch.
    - Verdict: CONFIRMED.
    - Evidence: shasum; POD:25.

18. T1:32. The quotation "and idle until the PI's word on it".
    - Verdict: CONFIRMED.
    - Evidence: NOTE:112.

19. T1:31–32. v1's note with its line 112 reworded, the coordinating session's one fix.
    - Verdict: NOT CHECKABLE: v1 and the request are not among the sources.

20. T1:33–36. Harness of 230 checks; 38 mutants, all killed at the second pass; Python checks 32 of 32 in a battery window; the .gitignore checked in a throwaway repository.
    - Verdict: CONFIRMED, as NOTE:114–136 states them.

21. T1:36–37. The review (af134d56…0061): 0 BUG; F1–F4 RISK, F5–F10 NIT, M1–M13.
    - Verdict: CONFIRMED.
    - Evidence: shasum; REV:18–125. F3 and F4 are "RISK (low)"; no finding is classed BUG.

22. T1:37. F1–F8 and F10 applied before the relay.
    - Verdict: CONFIRMED in the relayed files.
    - F1: SH:78–80, used at :86, :169, :257.
    - F2: NOTE:133–134.
    - F3: MAN's 59 lines = REV:7's 33 + REV:34–36's 26; SH:14–17.
    - F4: SH:73.
    - F5: SH:55–58, :119, :148, :226.
    - F6: SH:79; NOTE:86–88.
    - F7: SH:67–70.
    - F8: NOTE:68–69.
    - F10: NOTE:39–48, :104.

23. T1:37. F9 and M1–M13 applied.
    - Verdict: NOT CHECKABLE: the harness and its mutant list are not among the sources.
    - NOTE:125–132 reports 38 mutants, all killed at the second pass.

24. T1:38–39. The sync: 732a58f..main with main at a33252a, under refs/bundles/n-site10; the box checkout stayed at ad856f0.
    - Verdict: CONFIRMED.
    - Evidence: POD:30–35. `git rev-list --count 732a58f..a33252a` = 8, as POD:33 says.

25. T1:40–42. The fresh copy.
    - Verdict: CONFIRMED.
    - Evidence: POD:37–44; OUT:2–3.

26. T1:43–46. The versions; the env.sh variables; bf16, deterministic, seed 20260818; the identifier 8264f719efd347a9, backend-ext-2's, bridged to 4ed3f2c70fe8afbf (R6).
    - Verdict: CONFIRMED.
    - Evidence: POD:49–50; REC:105–133; OUT:109; R@1194982:857, :867–868.

27. T1:47. Two loads, 707 of 707 each; 27054 ms and 29614 ms.
    - Verdict: CONFIRMED.
    - Evidence: OUT:92–93, :108–109; REC:156.

28. T1:49–51. "changed set none"; 59 of 59 OK; "473/473 n selftest checks pass" after the two library warnings that backend-ext-2's output also holds; hashes equal to the laptop's.
    - Verdict: CONFIRMED.
    - Evidence: OUT:3, :5–63, :65–69, :85; POD:63–64 ("as at backend-ext-2"); R@1194982:862–863.
    - Only the count of warnings was checked against backend-ext-2; its self-test raw is not among the sources.

29. T1:51. "(the laptop's 462 and the box's 11 HF cases)".
    - Verdict: IMPRECISE.
    - The box has 13 HF checks in place of two skip lines; 11 is the net. Evidence: SH:18–19; R@1194982:493; REV:181–184 (462 − 2 + 13).
    - Wording: "(the laptop's 462 plus the box's 11 more: its 13 HF checks in place of the laptop's two skip lines)".

30. T1:52–53. The smoke's lines once each; its record held, its identity equal to step 3's, the copy unchanged; its record stays on the box.
    - Verdict: CONFIRMED.
    - Evidence: OUT:99–102; POD:66–69.

31. T1:54–56. The run of record's lines; run exit 2.
    - Verdict: CONFIRMED.
    - Evidence: OUT:104–125.

32. T1:57–59. The checks of the outputs.
    - Verdict: CONFIRMED.
    - Evidence: OUT:127–134.

33. T1:60–61. PID 7504; the end-wait on the PID alone; before and after, the GPU idle at 0 MiB.
    - Verdict: CONFIRMED.
    - Evidence: POD:47, :57, :83.

34. T1:62–66. The copy-back, including the first script's stop and the second version.
    - Verdict: CONFIRMED.
    - Evidence: POD:87–97.

35. T1:66–68. Ten files equal to the pod session's values; the identity files compared by cmp.
    - Verdict: CONFIRMED for the equalities.
    - My shasum of the ten equals the brief's values and ROUT:9–15. Both identity files are byte-equal to S/step4b/gvec/box/out/hashes.txt (cmp).
    - Code's own re-hash and reads are not checkable.

36. T1:69–72. The box at the end; up and idle on routing item 5.
    - Verdict: CONFIRMED.
    - Evidence: POD:83, :99–105; ANS:83; ROUT:25.

37. T1:73–75. valence_core/n/gvec.py:26–27 says "starred at the top of LOCK-n v0.1's list", a recommendation pending the PI's word; the seat ruled before the run (a33252a, §1.1–§1.4).
    - Verdict: CONFIRMED.
    - Evidence: gvec.py:26–27 (a620349f…ec71 at HEAD and at da7bdec; MAN:6); R@1194982:531–532; ANS:16–22; POD:30.

38. T1:75–76. The module's bytes move the package digest; the wording is fixed at the next change.
    - Verdict: CONFIRMED for the fact.
    - Evidence: OUT:71; R@1194982:602. ANS:68 accepts wording owed at each file's next change.
    - The plan itself is not checkable.

39. T1:78–80. copy_status()'s form; the review's F1; not item 1's bare form.
    - Verdict: CONFIRMED.
    - Evidence: SH:78–80; REV:18–23.

40. T1:80–81. "It is backend-ext-2's step-0 class, which the seat's §7 ruled inert for the pod session's scripts".
    - Verdict: IMPRECISE.
    - The words are carried from R@1194982:906–908. But the answers this entry cites are a33252a's, whose §7 is ledger (84) (ANS:70–72) and whose departures ruling is §6 (ANS:66–68).
    - Wording: "It is backend-ext-2's step-0 class, which the seat's §7 ruled inert for the pod session's scripts, as backend-ext-2's entry (`9f64305`) records;".

41. T1:82–84. Code's grep with a guard marker in its pattern.
    - Verdict: CONFIRMED.
    - Evidence: DEP:1.

42. T1:85–87. Code's three jq reads.
    - Verdict: NOT CHECKABLE.

43. T1:88–89. The reviewer's grep pattern holding a marker, over three code files, printing code lines.
    - Verdict: CONFIRMED.
    - Evidence: REV:219.

44. T1:89–90. "nine git ls-files runs … without item 3's full pathspec, printing counts, and one of them three file names".
    - Verdict: IMPRECISE.
    - REV:220–224 says "without item 3's full pathspec and the mf3 exclusion" and "All printed counts, except the last, which printed those three names".
    - Wording: "nine `git ls-files` runs over named data folders without item 3's full pathspec and the mf3 exclusion, printing counts, the last of them three file names instead;".

45. T1:90–92. The two git hash-object runs; shasum under Perl.
    - Verdict: CONFIRMED.
    - Evidence: REV:225–226.

46. T1:93. The pod session's record states no departure of its own.
    - Verdict: CONFIRMED.
    - Evidence: grep -c -i depart over POD returns 0.

47. T1:94. The values-checker's departures.
    - Verdict: NOT CHECKABLE (see DEPARTURES below).

48. T1:97. .gitignore line 309 admits gvec.json.
    - Verdict: CONFIRMED.
    - Evidence: .gitignore:309 "!/data/n/gvec/gvec.json", the same at da7bdec.

49. T1:100–101. Each identity file is byte-equal to the hashes file.
    - Verdict: CONFIRMED.
    - Evidence: all three are 881b79e7…e493; cmp.

50. T1:96–105. The raws' names, the home-folder count, "Not pushed", and "Next" (draft 5).
    - Verdict: NOT CHECKABLE: these are plans.
    - Except: "delta and (v)'s render meanwhile" is stated at ROUT:24.

**T2**

51. T2:1. The title.
    - Verdict: CONFIRMED.
    - Evidence: OUT:120–122.

52. T2:3–4. "Nothing is re-run, and Code adjudicates nothing: the figures are as printed".
    - Verdict: CONFIRMED.
    - Evidence: ROUT:18; §1's quotations match RUN and SMK.
    - "no cause below is weighed": see item 86.

53. T2:8. "§1.1–§1.4: "G-VEC runs as built"".
    - Verdict: IMPRECISE.
    - The sentence is the answers' §0 (ANS:7). In §1.1 it appears only inside the conditional (ANS:16). The committed close line cites §0 (R@1194982:294).
    - Wording: "(the seat's answers of 2026-11-19, first sitting, §0: "G-VEC runs as built", with G1, G3, G6 and G9 standing at §1.1–§1.4)".

54. T2:8–9. From da7bdec, on pod emw1e4embiwe9b, STOPPED at its R check.
    - Verdict: CONFIRMED.
    - Evidence: OUT:2, :109, :122.

55. T2:9–10. 44.04 and 45.11; 0.728 and 0.770; about 1.73 and 1.77 times.
    - Verdict: CONFIRMED.
    - Evidence: OUT:120–121, rounded by hand.

56. T2:11–12. The n §2.3 quotation; ADDENDUM-n1 §6.1.
    - Verdict: CONFIRMED.
    - Evidence: n:81; A-n1:52.

57. T2:13–14. The record alone, status STOP, site null; no direction, cosine or R_ℓ of record; the stage stopped before the contexts.
    - Verdict: CONFIRMED.
    - Evidence: OUT:124, :127 ("site 0, contexts 0, R_ell lines 0, cosines 0"), :129; REC; gvec.py:341–343.

58. T2:15–16. Not added; "comes from the re-run" (§1.1).
    - Verdict: CONFIRMED.
    - Evidence: REC:170–192; ANS:16. The "checked and frozen" clause is item 10.

59. T2:17–19. The seat chooses the path; Q1–Q3; G-CAL-n's launch waits for G-VEC's PASS; the box up and idle.
    - Verdict: CONFIRMED.
    - Evidence: ROUT:21, :24–25; ANS:80, :83.

60. T2:24. The passages line.
    - Verdict: CONFIRMED.
    - Evidence: RUN:7.

61. T2:25. "96 passages, min 35, mean 43.36, max 57"; 4,163 neutral tokens.
    - Verdict: CONFIRMED.
    - Evidence: RUN:13; REC:35, :68–73; 96 × 43.364583… = 4,163.

62. T2:26. "the longest input 90 tokens, within the window 4096", placed in the neutral passages' bullet.
    - Verdict: IMPRECISE.
    - The 90 is the longest over all ids of record: RUN:4 "(iv): 544 passages, 1344 contexts, … the longest 90 tokens"; REC:157, :167.
    - No passage is longer than 68 tokens (RUN:8–16) and no neutral passage longer than 57, so the 90 is a context's.
    - Wording, as its own bullet: "- the longest input of the ids of record (the 544 passages and the 1,344 contexts): 90 tokens, within the window 4096 (the inputs line; the record's `longest_input`);".

63. T2:27–29. The R and STOP quotations.
    - Verdict: CONFIRMED.
    - Evidence: RUN:17–19.

64. T2:31. R/25.49 = 1 + the printed figure.
    - Verdict: CONFIRMED.
    - By hand: 1 + 0.727834356223086 = 1.727834356223086, and 1 + 0.7696253488578015 = 1.7696253488578015.
    - Check: 25.49 × 1.727834356223086 = 44.0424977401264…, and 25.49 × 1.7696253488578015 = 45.1077501423853…. These equal the printed R values, so the printed figure is R/25.49 − 1, which is positive at both indices.

65. T2:33–37. The smoke's two lines, on a load of its own before the run's.
    - Verdict: CONFIRMED.
    - Evidence: SMK:1, :7–9; OUT:86–109.

66. T2:39–40. bk.resid_rms 25.491040760519905 and bk.pole_l2 2.319276809692383, from strength_ladder/analysis.json at layer 32.
    - Verdict: CONFIRMED.
    - Evidence: REC:2–5; gvec.py:87–88, :333.
    - SL:10493–10498 is the Instruct member's meta at layer 32 holding both values; the pair recurs in 16 metas.

67. T2:40–41. 7.6473 at ρ = 0.30; injected_l2 7.647312164306641 at |d| = 1; this is 0.30 × 25.491.
    - Verdict: CONFIRMED.
    - RED has 2,400 reads at that value, all the Instruct member's, at point and dose_fraction ±1.0 (240 valenced and 960 random per sign).
    - Also: n:81; VCs:102; VCg:166; 0.30 × 25.491 = 7.6473 by hand.

68. T2:43–47. The apparatus: weights, revision, aggregate 36f05404…0fdb, bf16 on H100 80GB HBM3, the determinism flags, seed, versions, the identifiers, package 882c9217…5ca7, driver fecde87a…3958, ids fdf73d85…ef38, corpus ef6b00dc…3cc3.
    - Verdict: CONFIRMED.
    - Evidence: REC:105–167; OUT:105, :107, :109; R@1194982:857, :867–868.

69. T2:51–52. The n §0.8 quotation, with its ellipsis.
    - Verdict: CONFIRMED.
    - Evidence: n:36.

70. T2:53–54. The n §2.3 quotation.
    - Verdict: CONFIRMED.
    - Evidence: n:81.

71. T2:55–56. The ADDENDUM-n1 §6.1 quotation.
    - Verdict: CONFIRMED.
    - Evidence: A-n1:52.

72. T2:57–59. The capture convention as ruled, quoted.
    - Verdict: CONFIRMED.
    - Evidence: ANS:16.

73. T2:60–63. §1.1's pre-declared sentence, quoted.
    - Verdict: CONFIRMED.
    - Evidence: ANS:16.

74. T2:69–77. Path (a).
    - Verdict: NOT CHECKABLE: it is a plan.
    - The parts ROUT:21 names match. The 96 forwards are the neutral passages (RUN:13).

75. T2:78–79, :88. (b) re-runs G-VEC of record; on a PASS, G-CAL-n's launch files.
    - Verdict: CONFIRMED.
    - Evidence: ROUT:21; ANS:80. "with the smoke" and the delta's contents are plans.

76. T2:82–84. The ADDENDUM-n1 §1.1 quotation; ids rendered on the laptop under data/n/ids/.
    - Verdict: CONFIRMED.
    - Evidence: A-n1:20.

77. T2:86–87. "about 1,900 forwards, as the eleven readings' block put it for any struck clause".
    - Verdict: IMPRECISE.
    - In ELEVEN, striking the centring needs "no box re-run" (:70). The re-run of about 1,900 forwards is for "Any other clause struck" (:74–77). 544 + 1,344 = 1,888.
    - Wording: "as the eleven readings' block put it for any capture clause struck but the centring (`99196e1`, G1);".

78. T2:89. (a) then (b).
    - Verdict: NOT CHECKABLE.

79. T2:90–91. G-CAL-n's launch and LOCK-n v0.1's dose map wait (d_eq uses R); the delta and (v)'s render go on meanwhile; the box up and idle.
    - Verdict: CONFIRMED.
    - Evidence: ANS:80, :63 (O8), :83; n:81; ROUT:24–25.

80. T2:95. The sink position, §1.1's first alternative.
    - Verdict: CONFIRMED.
    - Evidence: ANS:16.

81. T2:96. `(…, G1, "another answer")`.
    - Verdict: IMPRECISE.
    - The source has "*Another answer:*" (ELEVEN:69).
    - Wording: "(`99196e1`, G1, "Another answer")".

82. T2:96–98. The quoted list; G-VEC forwards each passage alone, with no special token and no template.
    - Verdict: CONFIRMED.
    - Evidence: ELEVEN:74–75; ANS:16; gvec.py:5–6, :28–29.

83. T2:99–100. R's form: pooled over 4,163 tokens, not a mean of per-passage RMS.
    - Verdict: CONFIRMED.
    - Evidence: ANS:16; gvec.py:7–8, :128–153; REC:35.

84. T2:101–103. n §2.3's 55.45 and its quotation; the smoke's R_ℓ 22.23 and 22.17.
    - Verdict: CONFIRMED (facts).
    - Evidence: n:81; SMK:8–9.

85. T2:104–105. The index; both indices measured; 1.73 and 1.77.
    - Verdict: CONFIRMED (facts).
    - Evidence: A-n1:52; gvec.py:32–34; OUT:120–121.

86. T2:106–107. "… is 0.30 × BK's `resid_rms` 25.491, so BK's records agree with R ≈ 25.49 within themselves."
    - Verdict: IMPRECISE. The arithmetic is right (item 67), but the "so" clause draws a conclusion about the candidate it lists. That is weighing, against T2:4, §4's heading and ROUT:22 ("without weighing it").
    - Wording: "- **BK's scale:** BK's ‖ṽ(+1)‖ = 7.6473 at ρ = 0.30, from which n §2.3 takes R ≈ 25.49 (n:81); BK's `resid_rms` 25.491 is in §1."

87. T2:108–109. "no text in the repository holds it", plus the n §0.8 quotation.
    - Verdict: NOT CHECKABLE.
    - The quotation is confirmed at n:36. The repository-wide claim was not searched.

88. T2:113–116. Q1–Q3's references.
    - Verdict: CONFIRMED.
    - Evidence: ELEVEN:74–75; ANS:16.

89. T2:118. The box up and idle on routing item 5; whether it stays up is the PI's.
    - Verdict: CONFIRMED.
    - Evidence: ANS:83; ROUT:25; POD:83, :99.

TOTALS: 89 items: 71 CONFIRMED, 9 IMPRECISE, 0 FAIL, 9 NOT CHECKABLE.

**DOES T2 WEIGH A CAUSE: yes, in one clause** (item 86, T2:106–107).
- Two other §4 entries attach evidence to their candidates without stating a conclusion, and a strict reading would count them too:
  - T2:104–105, "Both were measured, and R is about 1.73 and 1.77 times 25.49 at the two", bears against the index as the cause.
  - T2:102–103 sets the smoke's R_ℓ (22.23, 22.17) beside "may differ by 2×", which invites the reader to compute R/R_ℓ ≈ 1.98.
- Nothing in §0–§3 or §5 weighs a cause.

OBSERVATIONS
1. Item 11 holds only at 1194982, which landed during this check. The STOP commit will sit on it.
2. Bare forms for the two juxtapositions:
   - T2:101–103: "- **A capture convention's size:** n §2.3 quotes OLMo-3.1 DPO's 55.45 under A3's span-mean convention "only to show the two conventions may differ by 2×"." The smoke's R_ℓ stays in §1.
   - T2:104–105: "- **The index:** BK's "layer 32" read as adapter index 31 or 32 (ADDENDUM-n1 §6.1; G2); both were measured (§1)."
3. T1:20 ("not weighed") and T2:4 ("no cause below is weighed") hold once item 86 is applied, and observation 2 too if the seat reads juxtaposition as weighing.
4. T2's bare "§1.1" (at :15–16, :57, :60, :99, :114, :116) means the answers' §1.1, while T2:17–18 cite T2's own §3 and §5. Writing "the answers' §1.1" at first use in each section would remove the ambiguity.
5. The review's departure 2 says "Nine" but itemises 3 + 4 + 1 runs (REV:220–223). The totals agree only if its first group's "(3 runs)" leaves out the run with no exclusion. T1 follows the headline figure.
6. T1:63–64: the address and port were counted on the text files only (POD:93). "on the text files" could be added.
7. T1:88 writes ids.py's constant, which holds a guard marker, in full. T1:83 and DEP describe the adapter file without naming it. This is no breach, since the markers bind argv, but a later grep copied from that line would put a marker in an argv. "ids.py's manifest constant" avoids it.
8. T2:108: resting the clause on the quoted text alone would make it checkable: "BK's own capture code, which n §0.8 says BK's repository does not hold".
9. Item 13: cite the relay that carries the words "launch cleared", or drop the quotation marks: "the launch cleared on the PI's routing".
10. ROUT:22 gives "about 1.73 at both indices". T2's 1.73 and 1.77 follow the printed figures, so no change is needed.
11. Item 10: the committed close line (R@1194982:296–297) keeps "checked and frozen". If T1 and T2 are reworded, the two will differ in wording only.

DEPARTURES
- Git commands that walk history without item 3's pathspec. They printed only ids, commit times, subjects, a count or an exit status. Item 1 permits `git log --format` of these over any path; I state them because the brief's pathspec rule names no exception.
  - `git log -8 --format='%h %ci %s'`;
  - one loop of `git log -1 --format='%h %ci %s' <rev>` over seven named commits;
  - `git merge-base --is-ancestor da7bdec HEAD`;
  - `git rev-list --count 732a58f..a33252a`;
  - `git rev-parse` of HEAD and of da7bdec (ids only).
- Reads beyond the brief's named parts. These are not barred; I state them for the seat.
  - RESULTS.md lines 1–25 at a33252a.
  - Greps over RESULTS.md for entry headers, close-line headings, "§7 … inert" and four fixed strings, to locate and re-anchor lines.
  - RESULTS.md lines 903–909, 1160–1168 and 1994–2002 at 1194982.
  - `git diff -U0 a33252a HEAD -- RESULTS.md`: its hunk headers and a count of removed lines.
  - gvec.py beyond lines 20–35: lines 1–157, 300–349, 440–454, 595–606 and 684–694.
  - The neighbouring lines of VCs:102 and VCg:166 (98–106 and 163–169).
  - `git show da7bdec:` of scripts/n_sessions.py and gvec.py into shasum (digests only), and of .gitignore into grep.
- Nothing else:
  - no interpreter but shasum, no file written, no network;
  - no guard marker in any argv;
  - nothing under data/mf3, data/*/ckpt or data/*/reports read or listed, and no git status;
  - in S, only the brief and the named files, each by name.
