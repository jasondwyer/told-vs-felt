# n package — BUILD: the blind values-check

*The n-build session (Code), PI date 2026-11-16.*

- **What was checked, in two passes by fresh agents:**
  - **Pass 1** checked three drafts:
    - the BUILD entry (`fa729b21…9686`), whose site-check lines and values-check line were then placeholders;
    - the first review raw (`ff6084e0…5f00`);
    - the second review raw (`92d4453a…e77b`).
  - **Pass 2** checked three things:
    - the edits made after pass 1, as unified diffs;
    - the entry's filled site-check lines and its new "Since the render" block, in full;
    - the second site check's inputs raw.
- **The briefs.** Each quoted the list of record v2's items 1–5 verbatim, with the coordinating session's lines, and
  added: no Python, no guard marker in any argv, no writes, no token id, nothing under `data/mf3`. Pass 2's brief also
  barred reading any file's size or time, and any clock time in the report.
- **The reports** came back as each agent's hand-back message. Code extracted each with `jq`.
  - Pass 1's report: 156 lines, sha256 `71db2656…59d3` as returned.
  - Thirteen clock times in it are masked as "[a clock time]", with one timezone offset removed, under the house
    rule that committed text carries calendar dates only. That changed 6 lines (sha256 `0097067a…7840`).
  - Under the house scrub rule against identifying runs, the session id in one scratch path, in the checker's own
    departures, is also replaced by "<the session folder>". That changed a seventh line.
  - Nothing else is changed. The text reproduced below has sha256 `23130f8f…4494`.
  - Its paths are the checker's: S for Code's scratch build folder, P for the scratch folder.
- **The counts:**
  - pass 1: 147 items: 120 CONFIRMED, 17 IMPRECISE, 3 FAIL and 7 NOT CHECKABLE;
  - pass 2: 80 items: 72 CONFIRMED, 2 IMPRECISE, 0 FAIL and 6 NOT CHECKABLE.
- **The checker's own departures.** Pass 1's report lists its own departures:
  - a write just outside the scratch folder, deleted at once;
  - token ids on its screen, none in the report;
  - a clobbered PATH for one read-only command;
  - file-time reads of scratch files and of the tree's untracked drafts, none under a `ckpt` or `reports` directory;
  - `strings` over the two tars.

  Code records them here. The tree's drafts were read, never written.

## Pass 1: the checker's report, as returned (clock times masked)

## Blind values-check: the BUILD entry draft (E), the first review raw (R1) and the step-3 review raw (R2)

147 items checked: 120 CONFIRMED, 17 IMPRECISE, 3 FAIL, 7 NOT CHECKABLE. The FAILs and the most consequential IMPRECISE items are listed first; the full numbered register follows.

Paths: S = scratchpad/build and P = scratchpad. "n:" means a line of PROPOSAL-n-bk-reconciliation-v0_2.md, and "answers" means results/raw/2026-11-16_n-build_design-to-code_answers.md.

### FAIL and IMPRECISE items, with corrections (most consequential first)

1. **#129, FAIL.** R2's "Drafts vs the render" disposition says the BUILD entry states the render's schema draft. E contains no 33419938…111d, no 0ea39600…0db6, and no statement of any difference from the render's drafts. The render raw committed at d76f34f also owes that statement (Appendix A, :94–96: "its entry states any difference from these").
   - Since the render, these files changed: cells, hftiny, ids (bea4b333…07fa → 0e19723a…a7c8), primitive, probe, runner, verify and schema.
   - Fix: add the statement to E, or change R2's text.
2. **#49, FAIL.** E:136 quotes v0.2 as "40/40 and 41/40", which is not in v0.2.
   - v0.2 says "(40/39 and 41/40)" at n:50 (B5), and "40/40 by `present` order as near as 79/81 allows" at n:92.
   - The misquote comes from Code's own scratch flags.md:36.
3. **#74, FAIL.** R1 disposition 10 says "Cap and alpha stay inputs … (flagged)", and R1:162–163 says each open reading is flagged in E. E has no such flag and never mentions alpha. Fix: add the flag to E, or drop "(flagged)".
4. **#25 and #141, IMPRECISE.** E:83–84 says "20 of 20 killed, each by the check that names the invariant it breaks"; R2:327 says the same.
   - M4 was killed by "ids: its self-test ran to its end" (JSONDecodeError, mut3_out/m04.txt).
   - M12 was killed by "cells: its self-test ran to its end" (m12.txt).
   - R2:328 itself names both as exceptions. Its "as expected for M4" is not the review's prediction: the review predicted the check "ids: a file whose sha256 is not the manifest's is refused".
5. **#7, IMPRECISE.** E:20–21 calls ids.py "the render that produced data/n/ids/ (d76f34f)". The committed ids.py (0e19723a…a7c8) is not the render's code (bea4b333…07fa, render raw :104); R2 dispositions 10 and 12 changed it.
6. **#30, IMPRECISE.** E:96 says 5c0ae6b pinned 5a97527 and the pin moves to d791bd9. It leaves out 2822721, which already moved the pin to 14e65d8: scripts/n_analyze.py:1882 pins 4bed3f9a…4665 ("# 14e65d8"). The coming move is from 14e65d8.
7. **#21, IMPRECISE.** E:76–77 says the DEFECT "went to the seat as Q5". Q5 was committed at 718c48e ([a clock time]) before the review was briefed; the review cites it (R1:45) and R1 disposition 1 says "before the seat". Suggest "matched Q5, already before the seat".
8. **#71, IMPRECISE.** R1:16 says "the drafts it read went to the box's first site check". The box ran the drafts with these dispositions applied: s3review/old equals the site-1 manifest and carries the log-space binomial tail (old/runner.py:533–536).
9. **#78, IMPRECISE.** R1 disposition 4(a) claims "Known answers at n = 3,200 and n = 7,360". At 7,360 the test only checks that the result "is a probability (no overflow)" (runner.py:546–547).
10. **#145, IMPRECISE.** R2's M3 says "The check raised a KeyError on the PASS report it was given." In fact ids.render itself raised the KeyError in its label loop, because it held no N4 base ids; the check caught it (ids.py:404–412). No PASS report was returned.
11. **#43, IMPRECISE.** E:120 says "the schema self-test's first invocation at d76f34f". d76f34f's entry records the second run as the departure (RESULTS.md:1356–1358). Correction: "its second run, a script invocation, not the granted one".
12. **#3 and #68, IMPRECISE.** E:7–8 and :75 ("the drafts at 14e65d8"), and R1:9–10 and :161–162 ("committed v4.4"), have the timing off.
    - The review read v4.4's bytes: its schema line references match blob 4bed3f9a…4665.
    - But it ran before 14e65d8 was committed: brief file dated [a clock time], report [a clock time], commit [a clock time].
    - The reviewer called 5a97527 "the committed" blob (R1:36).
13. **#69, IMPRECISE.** R1:10–11 has two problems:
    - The committed drafts also carry the step-3 changes and the second review's fixes, not only these dispositions.
    - E gives the package sha256, not each draft's sha256s.
14. **#98, IMPRECISE.** R1:260 says "Nothing listed a directory", but load_sessions lists the skeleton folder (sessions.py:100 and :107, `iterdir`).
15. **#52, IMPRECISE (minor).** E:140 says the fidelity sample is not bound in the identity. The identity does bind `fidelity_rule.sample_key` (schema.py:476, :829), and keys.py's FID_FRACTION through package_sha256. What is unbound is a digest of the realized sample.
16. **#102, IMPRECISE.** R1's m01 quote is cut mid-parenthesis. The full check name ends "(a known answer on the double: labels bound to cues)" (runner.py:716).
17. **#101, IMPRECISE (minor).** R1:271 says each kill was "by a check naming its own invariant". m04 died first on "runner: a small run completes and obtains its plan", which names no invariant.
18. **#122, IMPRECISE (minor).** R2 disposition 8 lists the sources of a non-mismatch G-VER-STOP and omits the session-count line (verify.py:76–77).

### Departures of mine
- **A write.** One shell redirect wrote a 15-line file of sha256 lines for the tree's n drafts to `…/<the session folder>/scratchpad_vc_tree_hashes.txt`, just outside the scratchpad. I deleted it at once and confirmed it was gone; nothing else was written.
- **Token ids on screen.** My tool output displayed token ids twice: the tiny config's default eos_token_id inside a transformers warning in site_check_out.txt, and the recorded re-split ids in sessions.py's docstring. None appears in this report.
- **A clobbered PATH.** A zsh loop variable named `path` overwrote PATH for one read-only command (git was not found); I re-ran it with another variable name.
- **Other reads.** I read file times (stat, `ls -lT`) of scratch files and of the tree's untracked drafts, none under data/*/ckpt or data/*/reports. I ran `strings` over the two drafts tars to look for AppleDouble data.
- No Python ran, no network was used, and no command line contained a guard marker.

### The numbered register

**E (S/entry_build2.md)**
1. E:4–5, :61 — package sha256 60d892dc…cc66, m's form, 14 modules, schema.py and `__init__.py` as committed. **CONFIRMED.** pkg_hashes9.txt:1. I recomputed it with shell tools in package_sha256_of's form (m/resume.py:328–350) over S's 14 .py files and got the same value; S's schema.py and `__init__.py` equal HEAD's blobs.
2. E:6, :68–70 — 217/217 on the laptop; hftiny skipped for want of torch. **CONFIRMED.** pkg_st9.txt; mut3_out/m00.txt; hftiny.py:55–57; the render raw's output shows "PyTorch was not found" in the jlens venv. The venv, nice level and window are not visible in the one-line output.
3. E:7–8, :75 — first review "of the drafts at 14e65d8". **IMPRECISE** (FAIL/IMPRECISE list, item 12).
4. E:93–94 — the session-count quote. **CONFIRMED** verbatim at 2026-11-15_campaign-go…answers.md:60.
5. E:10 — no weights loaded anywhere. **CONFIRMED** for every run so far (STOP block :9–11; the render was model-free).
6. E:12–19 — the primitive's features. **CONFIRMED.** primitive.py:60–64, 86–99, 174–194, 213–222, 237–240, 145–159, 356–364, 76.
7. E:20–23 — ids.py. **IMPRECISE** (list item 5). Its load checks and ids_of/label_ids are ✓ (ids.py:254–291).
8. E:25 — the box tokenizes nothing for n's inputs. **CONFIRMED.** answers:7–8; n_sessions.py:127–141 decodes only.
9. E:26–27 — the renderer. **CONFIRMED.** sessions.py: the two recorded splits; the CHOICE_SPLIT join.
10. E:28–35 — G-VER's checks. **CONFIRMED.** verify.py:52–61, 76–100, 113–137.
11. E:36–37 — directions and keyed draws. **CONFIRMED.** keys.py:51–64.
12. E:38–44 — the runner. **CONFIRMED.** runner.py:137, 177–233, 391–433, 337–346.
13. E:45–49 — the cells. **CONFIRMED.** cells.py:16–21, 185–197, 236–248.
14. E:50–53 — the probe. **CONFIRMED.** probe.py:63–71, 78–83, 116–135.
15. E:54–58 — guard, test doubles, driver commands; what is not built. **CONFIRMED.** n_sessions.py:26, 178–201; n §8 steps 7–15.
16. E:59–60 — the scratch overlay. **CONFIRMED:** all 93 tracked valence_core files equal HEAD's blobs, with 12 drafts on top. The overlay's data/ also holds the model manifest folder.
17. E:62–64 — the 11 closure files. **CONFIRMED.** pkg_hashes9.txt:2–12.
18. E:66 — closure lines equal the first site check's. **CONFIRMED.** Identical to site/out/_box_hashes.txt and to step 5 of site_check_out.txt.
19. E:72–74 — both briefs say no Python and quote items 1–5. **CONFIRMED;** each item is hash-equal to the list-of-record raw, lines 18–22.
20. E:76 — 21 findings, 2 DEFECT. **CONFIRMED.** Findings 1 and 5; finding 8 is "RISK, with a doc DEFECT".
21. E:76–77 — "went to the seat as Q5". **IMPRECISE** (list item 7).
22. E:78 — 24 of 25 killed on the laptop; m05 at the box. **CONFIRMED.** S/mutants_out.txt; site_check_out.txt step 3.
23. E:79–81 — 1 BUG, 6 RISK, 6 NIT; the BUG fixed with a test; each RISK applied or flagged. **CONFIRMED.** cells.py:190–191, 229–231, 428–447.
24. E:82 — by the reviewer's reading, 8 killed and 12 surviving, a test for each survivor. **CONFIRMED.**
25. E:83–84 — "each by the check that names" its invariant. **IMPRECISE** (list item 4). The 217/217 baseline is ✓.
26. E:84–85 — m05 and b02 at the box. **CONFIRMED.** site2/site_check.sh:93–96.
27. E:87–88 — the first site check, on 14e65d8: 166/166, m05 killed, hashes equal. **CONFIRMED.** The committed raws equal the scratch copies (485c4fcf…9650, 6fc4212a…dce6, 65d0a53d…1209).
28. E:89–91 — transformers 5.15.0; Q1 (b); d76f34f. **CONFIRMED.**
29. E:95 — the schema's three commits. **CONFIRMED.**
30. E:96 — the analyzer's pin. **IMPRECISE** (list item 6).
31. E:98–99 — 11 untracked modules plus the driver, after 5a97527. **CONFIRMED.** git status; file times [a clock time]–[a clock time], after 5a97527's [a clock time].
32. E:99–100 — verify.py replaced with 36b4d0cd…. **CONFIRMED.** The tree's file is 36b4d0cd…4bb7 and carries G-2; it is dated [a clock time], before 645bd3f's [a clock time].
33. E:101–102 — from step 3 on, drafts stayed in scratch. **CONFIRMED.** No step-3 draft is in the tree.
34. E:103–104 — the early self-test from the tree. **NOT CHECKABLE;** no committed record exists.
35. E:105 — mutant batch 1 void. **CONFIRMED.**
36. E:106–108 — the wrong sha256 (7c42cb4b…17a8) and the file's e115d4d9…6291. **CONFIRMED.** STOP block :162–167; shasum of the file.
37. E:109–110 — AppleDouble twins. **CONFIRMED.** The new tar has 13 members and no com.apple data (the first tar has 42 hits). The COPYFILE_DISABLE flag itself cannot be observed.
38. E:111–112 — five shasum processes, two with guard markers. **CONFIRMED.** stop_valuescheck raw, item 64.
39. E:113–114 — m's guard counts only Python processes. **CONFIRMED.** guard.py:917–919 exactly; the valuescheck raw :184–185.
40. E:115 — paths reached by `cd` since. **CONFIRMED** as far as recorded (valuescheck raw, item 66).
41. E:116–117 — the `~/Downloads` search. **NOT CHECKABLE;** no source in the repo or scratch.
42. E:119 — two `--version` calls at 14e65d8. **CONFIRMED.** RESULTS.md:1909–1910.
43. E:120 — "first invocation" at d76f34f. **IMPRECISE** (list item 11).
44. E:121–122 — the PI's routing, N.9. **CONFIRMED.** p-verdicts-decisions answers raw :69.
45. E:124–126 — what is no longer a flag. **CONFIRMED.** answers:9–10, 31–50; RESULTS.md:483–485.
46. E:129–130 — ORDER. **CONFIRMED.** runner.py:18–22, 133–142.
47. E:131–133 — SCOPE and its quote. **CONFIRMED.** runner.py:290–296; answers:50.
48. E:134–135 — the fidelity binomial. **CONFIRMED.** runner.py:33–41, 206–233, 496–509.
49. E:136 — the v0.2 quote. **FAIL** (list item 2).
50. E:137–138 — the retention interval and its quote. **CONFIRMED.** CLAUDE.md 5(f)(iii).
51. E:139 — N2-E at f = 0.20 against "below dose 0.20". **CONFIRMED.** CLAUDE.md 5(f)(iv).
52. E:140–141 — the fidelity sample's binding. **IMPRECISE** (list item 15).
53. E:142–143 — the label-mass floor written null. **CONFIRMED.** runner.py:351.
54. E:144–145 — loads_ms. **CONFIRMED.** runner.py:48–52, 524.
55. E:146–147 — the non-mismatch G-VER-STOP, NIT 8. **CONFIRMED.** schema.py:1457–1461.
56. E:148–149 — addendum_sha256 beside proposal_sha256. **CONFIRMED.** schema.py:433–434.
57. E:150–151 — G-READ-n's fits in the cap. **CONFIRMED.** ADDENDUM-n1 §6.3.
58. E:152–153 — comparator medians over 40 sessions against 160. **CONFIRMED.** runner.py:136; N_FLOOR = 40.
59. E:154–155 — 31–32 row writes with fsync per read; the JSON rewritten per append. **CONFIRMED.** cells.py:244–248.
60. E:156–157 — `cache.crop` deprecated in 5.15.0, removal in 5.18. **CONFIRMED.** primitive.py:341; the box's warning.
61. E:158 — the schema's own flagged readings stand. **CONFIRMED.** RESULTS.md:482.
62. E:161–163 — the load_cell PIN and PIN-n-31. **CONFIRMED.** cells.py:135–174; RESULTS.md:489.
63. E:164 — the rendering_id PIN. **CONFIRMED** as declared (schema.py:444–446); not yet wired.
64. E:165 — one cv_seed for both calls. **CONFIRMED.** probe.py:86–87, 116–117; the result table has no cv_seed field.
65. E:168 — 13 drafts. **CONFIRMED.** site_check.sh:41–53 lists the same 13.
66. E:173–174 — next, step 4. **CONFIRMED.** answers:63.

**R1 (S/review_raw_draft.md)**
67. R1:3–7 — the header's counts and brief. **CONFIRMED:** 21 findings, 20 mutants, m21–m25 Code's own; the brief matches.
68. R1:9–10, :161–162 — "committed v4.4". **IMPRECISE** (list item 12).
69. R1:10–11 — the committed drafts and their sha256s. **IMPRECISE** (list item 13).
70. R1:23–157 — the reproduced report is byte-equal to S/review_report.md. **CONFIRMED.**
71. R1:16 — "the drafts it read went to" the box. **IMPRECISE** (list item 8).
72. R1:16–20 — m05 killed at the box; the step-3 changes. **CONFIRMED.**
73. R1:162 — schema.py unchanged. **CONFIRMED** (site-1 manifest: 4bed3f9a…4665).
74. R1:162–163 and disposition 10 — "(flagged)". **FAIL** (list item 3).
75–77. Dispositions 1, 2 and 3. **CONFIRMED.** Q5 at the questions raw :176; runner.py:712–718; primitive.py:484–489; mut/m01.log and m03.log.
78. Disposition 4(a) — known answers at 3,200 and 7,360. **IMPRECISE** (list item 9).
79–92. Dispositions 4(b) through 21. **CONFIRMED.** Each kill is shown in the mut/mXX.log files; code sites checked in runner, cells, primitive, keys and verify; the 5(f)(iv) quote is verbatim; n:48 and n:81 support the reading.
93–95. R1:238–251 — the harness, the mutant set, batch 1. **CONFIRMED.** S/run_mutants.sh, S/mutants.tsv; batch 1 shows 150/156 per mutant against 155/156.
96. R1:253 — the `ln -s` line. **NOT CHECKABLE;** the harness now copies data with `cp -R`.
97. R1:254–256 — the overlay's data held data/n/bk alone. **CONFIRMED.** Its n/ folder is dated [a clock time], 14e65d8's commit time; the manifest folder is dated [a clock time], after the batches.
98. R1:260 — "Nothing listed a directory". **IMPRECISE** (list item 14).
99–100. R1:262–270 — nothing written; batch 2. **CONFIRMED.**
101. R1:271 — each kill by a check naming its invariant. **IMPRECISE** (list item 17).
102. R1:277 — the m01 quote. **IMPRECISE** (list item 16).
103. R1:278–301 — the other 24 mutants. **CONFIRMED.** The m05 box line (164/166 and the two hftiny checks) matches site_check_out.txt.

**R2 (S/r2/raw.md)**
104–108. R2:3–26 — header, file list, HEAD d791bd9 (as the brief states), the rules, counts. **CONFIRMED.** Note: p's commit 9662468 landed ([a clock time]) before the report was saved ([a clock time]); schema.py is identical at both.
109. R2:28–29 — who implemented and checked the fixes. **NOT CHECKABLE.**
110. R2:31–33 — 217/217, "it was 187", 60d892dc…cc66. **CONFIRMED.** The 187/187 (pkg_st8b) ran on package 45c70818…6a98, the render's drafts.
111–114. R2:35–39, 43–203. **CONFIRMED.** Lines 43–199 are byte-equal to review_returned.md (both 8259b7a7…cffe1); the reviewer's line numbers are those of s3review/pre_fix.
115–121. Dispositions 1–7. **CONFIRMED.**
122. Disposition 8. **IMPRECISE** (list item 18).
123–128. Dispositions 9–13, and the "plan check is circular" observation. **CONFIRMED.**
129. The "Drafts vs the render" observation. **FAIL** (list item 1). The claim that the ids-relevant constants are unchanged between the two schema drafts is ✓.
130. The n_analyze observation — "its step-2 draft reads no capture file". **NOT CHECKABLE.**
131–134. The I/O, comparator and overlay-guard observations; mutants.tsv ed881b58…a4d4; run_mutants.sh 3615cdbe…12bb. **CONFIRMED.**
135. The pre-change harness hash 5db8cc90…c9c4. **NOT CHECKABLE;** no copy survives.
136–137. R2:310–323 — baseline gate, data/ copied, the run steps. **CONFIRMED.**
138. R2:322 — "PYTHONDONTWRITEBYTECODE=1". **NOT CHECKABLE;** the harness does not set it and the invocation is not recorded.
139–140. R2:325, :327 — nothing in the tree; the KILLED definition. **CONFIRMED.**
141. R2:327–329 — each mutant killed by the check naming its invariant. **IMPRECISE** (list item 4).
142–144. The result line; M1–M20 edits; every count and first check except M3's sentence. **CONFIRMED** against mut3_run.txt and mut3_out/m01–m20.txt.
145. M3's KeyError sentence. **IMPRECISE** (list item 10).
146–147. M10's equivalence note; "At the box". **CONFIRMED.**

## Pass 1: Code's dispositions

Every FAIL and IMPRECISE item is applied, in the order of the report's list (its register numbers in brackets). Code
checked each correction against its source before applying it.

1. **[#129] FAIL: the render's drafts.** Applied. The entry has a new block, "Since the render", stating every
   difference from the drafts the render ran (the render raw's Appendix A, `d76f34f`):
   - the package hash;
   - schema's two drafts;
   - the six files the second review's fixes changed;
   - `ids.py`'s two hashes;
   - the driver, which also changed (`5082ac24…6481` to `aa0b5404…e05f`). The checker's list left it out.
   - the six unchanged files.

   The block also says why the committed ids stand: the schema constants they depend on are unchanged, and G-VER, in
   the BUILD's code, PASSed on them at the box. The second review raw's observation now says the entry states every
   difference.
2. **[#49] FAIL: the v0.2 quote.** Applied. The flag now states Code's schedule (told-S 40 in each present-order
   group, told-U 39 and 41) against v0.2's B5, "(40/39 and 41/40)", and its N4-T row, "40/40 by `present` order as
   near as 79/81 allows".
3. **[#74] FAIL: "(flagged)" with no flag.** Applied by adding the flag to the entry: "Cap and alpha".
   - Reading `runner.py`:386–389 narrowed its wording: a resume is refused under another cap than the report's, or
     under an alpha other than any recorded binomial pause's.
4. **[#25, #141] each mutant "by the check that names" its invariant.** Applied in the entry and the second raw.
   - 18 mutants were killed by the named check, and M4 and M12 by their module's self-test raising.
   - The raw now says M12 went as the review predicted. For M4 the review had predicted the sha256 check's own line,
     but the tampered file was parsed instead and `ids`' self-test raised. Pass 2 found "as the harness's notes
     expected" not checkable, so it was struck.
5. **[#7] `ids.py` as "the render".** Applied. It is the render's code, changed since only by the second review's
   dispositions 6, 10 and 12.
   - Code adds 6 (`MANIFEST_OF_RECORD`) to the checker's 10 and 12.
   - None of them changes what a PASS render writes. `session_set_sha256` is now measured, but `load_sessions`
     refuses any set other than the one of record (`sessions.py`:110–112).
6. **[#30] the analyzer's pin.** Applied: `2822721` moved it to `14e65d8`, and the next move is to `d791bd9`.
7. **[#21] "went to the seat as Q5".** Applied: the DEFECT "matched Q5 of `718c48e`, already before the seat".
8. **[#71] "the drafts it read went to" the box.** Applied: the drafts, with the dispositions applied, went there.
9. **[#78] known answers at 7,360.** Applied: a known answer at 3,200; at 7,360, a check that the tail is a
   probability.
10. **[#145] M3's KeyError.** Applied. `ids.render` raised it in its label loop, which had no N4 base ids, and the
    check caught it. No report was returned. Code read `ids.py`:147–200 and :400–412.
11. **[#43] the schema self-test at `d76f34f`.** Applied: the departure recorded there is the script invocation, not
    the granted one.
12. **[#3, #68] "the drafts at `14e65d8`" and "committed v4.4".** Applied in the entry and the first raw: schema
    v4.4, `4bed3f9a…4665`, the bytes `14e65d8` committed while the review ran.
13. **[#69] the committed drafts and their sha256s.** Applied. They carry these dispositions, then the step-3 changes
    and the second review's fixes. The entry gives the package sha256; the inputs raw gives each draft's.
14. **[#98] "Nothing listed a directory".** Applied: nothing but BK's skeleton folder, which `load_sessions` lists.
15. **[#52] the fidelity sample's binding.** Applied. The identity binds the sample's key, and the package hash its
    fraction; no digest of the realized sample is bound.
16. **[#102] the m01 quote.** Applied: completed from `runner.py`:716.
17. **[#101] each kill "by a check naming its own invariant".** Applied: 23 were first caught by such a check; m04 was
    first caught by the runner's small run, which names none.
18. **[#122] the sources of a non-mismatch G-VER-STOP.** Applied: the session count is added.

The NOT CHECKABLE items stand as stated, each on Code's or another session's record:
- [#34] the early self-test from the tree, which the coordinating session noted;
- [#41] the `~/Downloads` search;
- [#96] batch 1's `ln -s` line, from a script since replaced;
- [#109] who implemented and checked the fixes;
- [#130] n-analyzer's statement that its step-2 draft reads no capture file;
- [#135] the harness's pre-change hash, of which no copy survives;
- [#138] `PYTHONDONTWRITEBYTECODE=1`, now recorded in the second raw with the run's invocation.

**One edit before pass 2 that pass 1 did not ask for.** At the coordinating session's request, the second raw states
the copy's scope: the overlay is Code's scratch copy, outside the repository, and no path under the repository's
`data/` was copied. Pass 2 checked it.

## Pass 2: the checker's report, as returned

*140 lines, sha256 `446d7ab9…60b7`, extracted with `jq` and reproduced unedited. It holds no clock time; its one
time-like string is the line citation "v0.2:50". Its short names are its own: E, R1 and R2 are the three drafts, and
IR is the inputs raw.*

Second-pass values-check of the BUILD entry, the two review raws and the site-check inputs raw. Result: 80 claims checked; 72 CONFIRMED, 2 IMPRECISE, 0 FAIL, 6 NOT CHECKABLE. Both IMPRECISE items are attribution or wording slips. No number, hash or commit id is wrong.

Short names used below:
- **E** = scratchpad/build/entry_build2.md
- **R1** = scratchpad/build/review_raw_draft.md
- **R2** = scratchpad/build/r2/raw.md
- **IR** = scratchpad/site2/inputs_raw.txt
- **OUT2 / RUN2** = scratchpad/site2/out/site_check_{out,run}.txt
- **OUT1 / RUN1** = 645bd3f's results/raw/2026-11-16_n-build_sitecheck_{out,run}.txt
- **App.A** = results/raw/2026-11-16_n-ids_render.md:98–113
- **pre_fix** = build/s3review/pre_fix/*

Every pre_fix file's digest equals its Appendix A line, so pre_fix is the code the render ran.

## Items

1. E:6 — 217/217 laptop, 228/228 box, second site check PASSed. **CONFIRMED.** pkg_st9.txt:1; OUT2:28 and :62; site_check.exit = 0.
2. E:7–8 — two blind reviews (step-6 drafts with v4.4; the step-3 changes), every finding disposed. **CONFIRMED.** R1 dispositions 1–21 (R1:166–235); R2 dispositions 1–13 (R2:205–288).
3. E:21–22 — the render code changed only as dispositions 6, 10 and 12 state, and a PASS render writes the same bytes. **CONFIRMED.**
   - In render(): the caught RenderingMismatch (disp 10); note()/FIRST_PROBLEMS, the measured session_set_sha256 and the fsync (disp 12). MANIFEST_OF_RECORD is a module constant (disp 6).
   - The measured set hash equals the constant on any PASS render, because load_sessions asserts it (sessions.py:111).
   - Observation: the driver's render-ids also changed (render_out, disp 11), as stated at E:76; it also leaves a PASS render's bytes unchanged.
4. E:60–61 — the hashes were measured from an overlay of HEAD's valence_core, data/n/bk and the model manifest, drafts on top. **CONFIRMED.** scratchpad/overlay holds valence_core, scripts, data/n/bk and the manifest's folder; its n/*.py and driver are digest-equal to build/'s.
5. E:67 — each closure file's sha256 equals the line both box checks printed. **CONFIRMED.** The 11 imported_sha256 lines are digest-equal across pkg_hashes9.txt, OUT1:34–44 and OUT2:50–60.
6. E:67–68 — the second check printed the same package hash and 11 closure lines as the laptop. **CONFIRMED.** OUT2:49–60 is digest-equal to all of pkg_hashes9.txt.
7. E:69–70 — App.A lists the render's drafts and says the entry states any difference. **CONFIRMED.** Render raw :92–95.
8. E:70 — package 45c70818…6a98 → 60d892dc…cc66. **CONFIRMED.** App.A:98; pkg_hashes9.txt:1.
9. E:71 — schema 33419938…111d → 0ea39600…0db6, committed at d791bd9. **CONFIRMED.** App.A:109; `git show d791bd9:valence_core/n/schema.py | shasum`.
10. E:72 — six files changed by the second review's fixes. **CONFIRMED.**
    - cells 03c13928…5252 → 8cc7d405…1c76
    - hftiny c61ea751…82be → 7594f815…c08c
    - primitive bae61d60…4069 → 7e7bb0a0…0b0c
    - probe cfd269dd…3772 → 5fe409d8…54aa
    - runner 6e1760d5…3457 → 69d73d77…d896
    - verify 627ae4b6…c2a3 → ee32a71f…b33b
    - The diffs map to the review's dispositions and survivor tests.
11. E:73 — the step-3 changes were already in the drafts the render ran. **CONFIRMED.** pre_fix equals App.A; the reviewer found every draft equal to App.A except schema.py (R2:194).
12. E:74–75 — ids.py bea4b333…07fa → 0e19723a…a7c8, changed by dispositions 6, 10 and 12. **IMPRECISE.** The hashes are right, but the attribution is incomplete (correction below).
13. E:76 — the driver changed by disposition 11. **CONFIRMED.** 5082ac24…6481 → aa0b5404…e05f. The diff holds render_out, the is-dir check with local_files_only, --selftest dispatched first, three driver checks, and one docstring line naming disposition 6's pin.
14. E:77 — six files unchanged. **CONFIRMED.** App.A equals the n_manifest lines for `__init__`, directions, guard, keys, sessions and testing.
15. E:79–80 — the six schema constants are unchanged between the two drafts. **CONFIRMED.** build/s5check/schema_v5.py (= 33419938…111d) against the draft has identical lines for TOLD_LINE, SHAM_LINE, N_SESSIONS, N_FLOOR, BK_CELLS and SESSION_SET_SHA256; the whole diff is 58 lines of docstrings, comments and messages.
16. E:80–81 — G-VER, in the BUILD's code, PASSed at the box. **CONFIRMED.** OUT2:46–47.
17. E:86 — 228/228, temp folder on /workspace (nfs4). **CONFIRMED.** OUT2:24–29; site_check.sh:65–67.
18. E:86–87 — cells' in-place writes, flushes, fsyncs and reloads pass on the stage root's volume (RISK 3). **CONFIRMED.** The driver uses TemporaryDirectory under TMPDIR (n_sessions.py:88); cells.py:185–197; R2:72–77 and :220–223.
19. E:88 — hftiny's 12 checks replace the laptop's one skip line. **CONFIRMED.** 12 chk calls on the torch path (hftiny.py:71–124) and 1 on the skip path (:56); 217 − 1 + 12 = 228.
20. E:92–93, R1:9–10 and R1:162–163 — v4.4 = 4bed3f9a…4665 = 14e65d8's bytes. **CONFIRMED.** `git show 14e65d8:valence_core/n/schema.py | shasum`; build/_schema_v44.py has the same digest.
21. Same three places — "committed while the review ran". **NOT CHECKABLE.** No source dates the review's start or end against that commit. The report only shows it began before 14e65d8 (R1:37, "not the committed 5a97527 blob").
22. E:94 — 21 findings, 2 of them DEFECT. **CONFIRMED.** DEFECT headings at findings 1 and 5. Finding 8 is headed "RISK, with a doc DEFECT" and is classed RISK at R1:191.
23. E:94–95 — the DEFECT matched Q5 of 718c48e, already before the seat, since ruled: the band. **CONFIRMED.** Questions raw :41; R1:46; answers raw :9 and :39–43.
24. E:101–102 — 20 of 20 killed; 18 by their named check; M4 and M12 by their module's self-test raising. **CONFIRMED.** mut3_run.txt:2–23; m04.txt; m12.txt.
25. E:103 — m05 and b02 ran at the box, where only the HF path can kill them. **CONFIRMED.** OUT2:30–43; hftiny.py:55–57 (skipped without torch).
26. E:110–111 — the three raw names; HEAD 9662468; PASS. **CONFIRMED.** OUT2:2 and :62; the names match IR:2–3.
27. E:112 — the copy's changed set was exactly the 13 drafts; manifest 19/19. **CONFIRMED.** OUT2:3 and :5–23.
28. E:113 — 228/228 with the temp folder on /workspace. **CONFIRMED** (as item 17).
29. E:114 — m05 killed at 226/228 with the first run's values. **CONFIRMED.** OUT2:34–36 against OUT1:24–25.
30. E:114–115 — b02 killed at 227/228 by "AT THE SITE (layer 1)". **CONFIRMED.** OUT2:41–43.
31. E:116–117 — G-VER trial PASS, the BUILD's trial and never of record; 160/160 ids, spans and N4; 4 of 4 labels; the manifest. **CONFIRMED.** OUT2:45–46.
32. E:118 — the hashes equal the laptop's. **CONFIRMED** (as item 6).
33. E:119–120 — Python 3.12.3, torch 2.8.0+cu128, transformers 5.15.0, tokenizers 0.22.2. **CONFIRMED.** RUN2:36–37.
34. E:121–122 — two warnings, word for word as at the first check, once in the self-test and once in each mutant. **CONFIRMED.** Two distinct lines, three times each, in OUT2 (:26–27, :32–33, :39–40); the distinct set is digest-equal to OUT1's.
35. E:123 — the tiny OLMo-2 config's eos_token_id lies outside its 128-token vocabulary. **CONFIRMED.** hftiny.py:36 and :42 (vocab_size=128).
36. E:123–124 — hftiny never generates. **CONFIRMED.** No generate call in hftiny.py, primitive.py or testing.py.
37. E:125 — `crop` with a positive value is deprecated, flagged below. **CONFIRMED.** OUT2:27; primitive.py:341 `cache.crop(n)`; flag at E:200–201.
38. E:127 — Code's request named "a library message" as unexpected. **CONFIRMED** against site2/request_draft.md:27. That file is a draft with placeholders; the request as sent is not among the sources.
39. E:128 — the pod session, finding the warnings to be the first run's, did not stop. **CONFIRMED.** RUN2:61–64.
40. E:132–133 — 5c0ae6b pinned 5a97527; 2822721 moved the pin to 14e65d8. **CONFIRMED.** 5c0ae6b's n_analyze.py:1852 = 77c12d6d…94bc; 2822721's :1853 = 4bed3f9a…; HEAD's :1882 still pins 14e65d8.
41. E:137 — the verify.py draft carrying G-2's span fix is 36b4d0cd…4bb7. **CONFIRMED.** The tree's untracked verify.py hashes to it; 645bd3f's STOP values-check raw :106 and :135 record it.
42. E:148–149 — the tar was packed with COPYFILE_DISABLE=1, --no-mac-metadata and --no-xattrs. **NOT CHECKABLE** as to the command: it is recorded nowhere, and request_draft.md:7 names only COPYFILE_DISABLE=1. The effect is confirmed by tool:
    - 13 members;
    - no "Mac OS X" magic and no "._" member names;
    - no xattr or PaxHeader records;
    - RUN2:13 and :31–32 report the same.
43. E:159 — at d76f34f, the schema self-test's script invocation was not the granted one. **CONFIRMED.** RESULTS.md:1357–1358.
44. E:175 — told-S 40 per present-order group, told-U 39 and 41, 80/80. **CONFIRMED.** keys.py:15–18 and its self-test checks.
45. E:175–176 — the quotes "(40/39 and 41/40)" and "40/40 by `present` order as near as 79/81 allows". **CONFIRMED** word for word: PROPOSAL-n v0.2:50 and :92.
46. E:180–181 — the identity binds sample_key, the package hash binds the fraction, and no digest of the realized sample is bound. **CONFIRMED.** schema.py:458, :476 and :829; keys.py:30; no field holds a sample digest.
47. E:183–184 — cap and alpha are runner inputs read from the lock (the first review's disposition 10). **CONFIRMED.** runner.py:246–247; R1:202–204.
48. E:184–185 — a resume is refused under another cap, or another alpha than a binomial pause records. **CONFIRMED.** runner.py:386–389.
49. R1:10–11 — the BUILD drafts carry the first review's dispositions, then the step-3 changes and the second review's fixes. **CONFIRMED.** Spot-checked in the final drafts: the labels-to-cues known answer, TAU 0.0178835444, the stream known answer, the redaction, read_window, the cap refusal, the shadow scope and the cadence in reads.
50. R1:11–12 — the entry gives the package sha256; the inputs raw gives each draft's. **CONFIRMED.** E:4 and :62; IR:13–25.
51. R1:17 — the drafts, with the dispositions applied, went to the first site check; 645bd3f's three raws. **CONFIRMED.**
    - build/s3review/old/* is digest-equal to site/n_manifest.txt (1fe92878…ec34, RUN1's stated value) and carries the dispositions (old runner.py:533–536; OUT1:24).
    - 645bd3f added _diag, _out and _run.
52. R1:163 — schema.py unchanged by the dispositions. **CONFIRMED.** RUN1:28–29.
53. R1:178 — a known answer at n = 3,200, and a probability check at n = 7,360. **CONFIRMED.** runner.py:544–547 (old :533–536).
54. R1:261–263 — "Nothing listed a directory but BK's skeleton folder". **IMPRECISE** (correction below).
55. R1:273–274 — batch 3: 24 of 25 killed; 23 first caught by a named check; m04 by the runner's small run. **CONFIRMED.** build/mutants_out.txt; first FAIL lines of scratchpad/mut/m01–m25.log.
56. R1:280 — m01's first check, as quoted. **CONFIRMED** word for word (mut/m01.log).
57. R2:265–266 — a non-mismatch G-VER-STOP comes from the session count, the manifest, the pin, the decoder or a label check. **CONFIRMED.** verify.py:76–77, :80–84, :85–88, :89–90 and :126–137 (also n_kept = 0 at :139–140).
58. R2:294–296 — the entry states every difference; the schema drafts named; the constants unchanged. **CONFIRMED.** E:69–81; item 15.
59. R2:316 — the overlay is Code's scratch copy, asserted outside the repository. **CONFIRMED.** run_mutants.sh:102–103.
60. R2:317–318 — the harness first asserts what the overlay's data/ and the manifest's folder hold. **CONFIRMED.** run_mutants.sh:114–117, before the baseline at :183.
61. R2:318 — no path under the repository's data/ was copied. **CONFIRMED.** run_mutants.sh:179 copies only from the overlay.
62. R2:328 — the runs used one window the coordinating session granted. **NOT CHECKABLE** (no record in the sources).
63. R2:328 — nothing in the tree. **CONFIRMED.** run_mutants.sh:102, :128, :143 and :149; the outputs are in scratchpad/mut3_out.
64. R2:328–330 — the exact invocation. **NOT CHECKABLE** (the command line is recorded nowhere). Its form matches the usage at run_mutants.sh:5, and build/mut3/run_mutants.sh, overlay and mut3_out exist as named.
65. R2:330 — each self-test inherits the environment variable. **CONFIRMED.** Only TMPDIR is prefixed (run_mutants.sh:188 and :286), and nothing unsets the variable.
66. R2:332 — the definition of KILLED. **CONFIRMED.** run_mutants.sh:27 and :290–301.
67. R2:332–333 — 18 killed by their named check. **CONFIRMED.** M1–M3, M5–M11 and M13–M20 each fail their named check; for M8 it is the third of six FAIL lines.
68. R2:333–334 — M4 and M12 killed by their module's self-test raising; M12 as the review predicted. **CONFIRMED.** m04.txt; m12.txt; review table at R2:160.
69. R2:334 — M4 "as the harness's notes expected". **NOT CHECKABLE.** Neither mutants.tsv (M4's intent field) nor run_mutants.sh records an expected kill for M4; the harness writer's notes are not available.
70. R2:334–335 — for M4 the review predicted the sha256 check's own line. **CONFIRMED.** R2:156.
71. R2:355–356 — M3: a KeyError in the label loop, caught by the check, no report returned. **CONFIRMED.** m03.txt:1; ids.py:173 (the clause dropped) and :184 (the N4 base lookup); the check's try/except around rep_n4.
72. IR:1–2 — the seat's answers, second sitting, §5 step 3. **CONFIRMED.** Answers raw :58 and :62.
73. IR:2–3 — the run and out raw names; the output unedited. **CONFIRMED** as far as checkable. The names match E:110; RUN2:3–4 says "unedited, 62 lines" and the out file has 62 lines. The committed copies do not exist yet.
74. IR:5 — tar 8379566e…a1bd held the 13 drafts this BUILD commits. **CONFIRMED** (shasum; members equal build/'s drafts).
75. IR:6 — the packing flags. **NOT CHECKABLE** (as item 42; the effect is confirmed).
76. IR:6–7 — the members' sha256s are the manifest's first 13 lines. **CONFIRMED.** `tar -xOf` per member piped to shasum; the composed list is digest-equal to n_manifest lines 1–13.
77. IR:7–9 — manifest 92a587de…6bb8 and its order (13 drafts, then schema.py and `__init__.py` as committed, then the 4 ids files). **CONFIRMED.** Lines 14–19 pass `shasum -c` against the tree's committed files, which are clean.
78. IR:9–10 — site_check.sh 6fef5e6a…5f24. **CONFIRMED.**
79. IR:13–31 equals n_manifest.txt byte for byte. **CONFIRMED** (`sed -n 13,31p | shasum` = 92a587de…6bb8).
80. IR:33–141 equals site_check.sh byte for byte. **CONFIRMED** (`sed -n 33,141p | shasum` = 6fef5e6a…5f24; 109 lines).

## Counts
CONFIRMED 72, IMPRECISE 2, FAIL 0, NOT CHECKABLE 6.

## IMPRECISE, most consequential first
1. **E:74–75.** ids.py's change is attributed only to dispositions 6, 10 and 12. The diff from pre_fix/ids.py (= App.A's bea4b333…07fa) also adds the self-test cases the review gave its surviving mutants:
   - M5: the record count;
   - M3: the N4 clause;
   - M2: a tail that differs between contexts;
   - M1: a recorded split in the label loop.

   Correction: "Changed by the second review's dispositions 6, 10 and 12, and by the tests for its surviving mutants M1, M2, M3 and M5: `ids.py`, …". E:21–22 stays correct, since the render code itself changed only under 6, 10 and 12.
2. **R1:261–263.** Read literally, "Nothing listed a directory but BK's skeleton folder" overstates. In the drafts of that time:
   - guard's self-test hashes the copy's valence_core/n/ (guard.py:109 → m/resume.py:339 `d.glob("*.py")`);
   - cells' self-test lists its own temporary folder (old cells.py:238).

   Neither is under data/, the repository or the overlay. Correction: "Under data/, nothing listed a directory but BK's skeleton folder…", or name those two listings.

## NOT CHECKABLE
Items 21, 42, 62, 64, 69 and 75: no source in scope records the review's timing against 14e65d8, the tar's packing command, the window grant, the mutant run's command line, or the harness writer's notes on M4.

## My own departures
No Python ran, no network was used, and nothing was written. Three things to disclose:
- `diff -u` on scratch files printed their modification times in the diff headers. No time appears here.
- One recursive name-only grep (`grep -rln 'no-mac-metadata'`) over the whole scratch folder read, without printing anything from them, the render's copies of the ids files in scratchpad/ids_out and the tokenizer files there. It printed only three matching names, none of those files.
- Listing the batch-3 mutant logs' first FAIL lines printed m07's detail. It includes two synthetic token ids of the self-test's toy double, not any tokenizer's ids; they are not quoted here.

Otherwise none.

## Pass 2: Code's dispositions

Both IMPRECISE items are applied:
1. **E:74–75, `ids.py`'s attribution.** Applied. The bullet now reads: "Changed by the second review's dispositions 6,
   10 and 12, and by the tests for its surviving mutants M1, M2, M3 and M5". The bullet on the other six changed
   files now names "the tests for its surviving mutants" beside the fixes.
2. **R1:261–263, "Nothing listed a directory".** Applied. The sentence now opens "Under any `data/`", so it no longer
   claims more than it covers. Guard's hash of the package folder and cells' listing of its own temporary folder lie
   outside every `data/`.

The NOT CHECKABLE items:
- **21, "committed while the review ran".** It stands. Pass 1 established the order from the files' times: its
  items #3 and #68, with the times masked here.
- **42 and 75, the tar's packing flags.** The inputs raw now records the command. Pass 2 confirmed its effect by
  tool (items 42 and 76).
- **62, the window grant.** It stands on the coordinating session's grant.
- **64, the mutant run's command line.** It stands as Code's record in the second raw.
- **69, M4 "as the harness's notes expected".** Struck. The second raw now says what happened instead: the
  tampered file was parsed, and `ids`' self-test raised.

**The checker's own departures**, as it reports them:
- `diff -u` headers put scratch files' times on its screen, though none are in its report;
- one recursive name-only grep over the scratch folder read, without printing anything, the render's copies of the
  id and tokenizer files;
- m07's detail put two synthetic ids of the self-test's toy double on its screen, not any tokenizer's, and none are
  in its report.

Code records them here.

## The edits after pass 2, checked by tool

The edits after pass 2, as `git diff --no-index -U0` from Code's copies taken before them. This form prints no file
times. The diffs cover:
- the entry;
- the first and second review raws;
- the inputs raw;
- the pass-1 dispositions above.

The entry's diff also fills its values-check line.

```diff
diff --git a/vc/pre2/E.md b/entry_build2.md
index 5719943..2aabb4b 100644
--- a/vc/pre2/E.md
+++ b/entry_build2.md
@@ -72,4 +72,5 @@
-    - Changed by the second review's fixes: `cells.py`, `hftiny.py`, `primitive.py`, `probe.py`, `runner.py` and
-      `verify.py`. The step-3 changes themselves were already in the drafts the render ran.
-    - Changed by the second review's dispositions 6, 10 and 12: `ids.py`, from `bea4b333…07fa` to
-      `0e19723a…a7c8`.
+    - Changed by the second review's fixes and the tests for its surviving mutants: `cells.py`, `hftiny.py`,
+      `primitive.py`, `probe.py`, `runner.py` and `verify.py`. The step-3 changes themselves were already in the
+      drafts the render ran.
+    - Changed by the second review's dispositions 6, 10 and 12, and by the tests for its surviving mutants M1, M2, M3
+      and M5: `ids.py`, from `bea4b333…07fa` to `0e19723a…a7c8`.
@@ -210 +211,7 @@
-  - **Values-check:** VALUESCHECK_LINE
+  - **Values-check** (`results/raw/2026-11-16_n-build_valuescheck.md`). It ran as two blind passes by fresh agents,
+    each briefed with the list of record v2's items 1–5:
+    - **Pass 1** covered this entry and the two review raws. Of 147 claims: 120 CONFIRMED, 17 IMPRECISE, 3 FAIL,
+      7 NOT CHECKABLE. Every FAIL and IMPRECISE item was applied.
+    - **Pass 2** covered the edits after pass 1, the site-check lines, the "Since the render" block and the inputs
+      raw. Of 80 claims: 72 CONFIRMED, 2 IMPRECISE, 0 FAIL, 6 NOT CHECKABLE. Both IMPRECISE items were applied.
+    - The edits after pass 2 were checked by tool.
@@ -214 +221,2 @@
-    - the site-check raws;
+    - the second site check's three raws (inputs, run, output);
+    - the values-check raw;
diff --git a/vc/pre2/R1.md b/review_raw_draft.md
index 565d413..e0bb577 100644
--- a/vc/pre2/R1.md
+++ b/review_raw_draft.md
@@ -261,3 +261,3 @@ jlens venv at nice 19, in battery windows the coordinating session granted. KILL
-    exist under the overlay. Nothing listed a directory but BK's skeleton folder, which `load_sessions` lists (here
-    the overlay's copy), and nothing read `data/mf3`, a `ckpt` or a `reports` directory, in the repository or the
-    overlay.
+    exist under the overlay. Under any `data/`, nothing listed a directory but BK's skeleton folder, which
+    `load_sessions` lists (here the overlay's copy), and nothing read `data/mf3`, a `ckpt` or a `reports` directory,
+    in the repository or the overlay.
diff --git a/vc/pre2/R2.md b/r2/raw.md
index e2610cb..ad825f0 100644
--- a/vc/pre2/R2.md
+++ b/r2/raw.md
@@ -334,2 +334,2 @@ killed by the check that names the invariant they break. M4 and M12 were killed
-M12 as the review predicted, and M4 as the harness's notes expected. For M4 the review had predicted the sha256
-check's own line.
+M12 as the review predicted. For M4 the review had predicted the sha256 check's own line; the tampered file was
+parsed instead, and `ids`' self-test raised (JSONDecodeError).
diff --git a/vc/pre2/IR.txt b/../site2/inputs_raw.txt
index 320ea64..43598a7 100644
--- a/vc/pre2/IR.txt
+++ b/../site2/inputs_raw.txt
@@ -6,2 +6,3 @@ The tar, n_drafts.tar (sha256 8379566e08cba016f7cf607b116c35a2bd3b7ccbc2a3c77242
-this BUILD commits, packed on the laptop with COPYFILE_DISABLE=1, --no-mac-metadata and --no-xattrs; its members'
-sha256s are the manifest's first 13 lines. Below, verbatim, between the marker lines: n_manifest.txt (sha256
+this BUILD commits, packed on the laptop from Code's scratch build folder as `COPYFILE_DISABLE=1 tar
+--no-mac-metadata --no-xattrs -cf n_drafts.tar <the 13 paths, in the manifest's order>`; its members' sha256s are
+the manifest's first 13 lines. Below, verbatim, between the marker lines: n_manifest.txt (sha256
diff --git a/vc/pre2/disp1.md b/vc/raw_disp1.md
index 1a9b974..86c0ec3 100644
--- a/vc/pre2/disp1.md
+++ b/vc/raw_disp1.md
@@ -27,2 +27,3 @@ checked each correction against its source before applying it.
-   - The raw now says M12 went as the review predicted, and M4 as the harness's notes expected; for M4 the review
-     had predicted the sha256 check's own line.
+   - The raw now says M12 went as the review predicted. For M4 the review had predicted the sha256 check's own line,
+     but the tampered file was parsed instead and `ids`' self-test raised. Pass 2 found "as the harness's notes
+     expected" not checkable, so it was struck.
```

The checks, as run, with their output:

```text
$ grep -c -F (the two reports count lines)
1
1
$ the four survivor tests in ids.py: in the BUILD draft / in the render draft (s3review/pre_fix)
a recorded split applies to the label loop: 1 / 0
a candidate whose tail differs between contexts: 1 / 0
N4 sequences that move a token before n_pre STOP the render: 1 / 0
a manifest whose record count is not its file's: 2 / 0
$ M4 kill line (mut3_out/m04.txt)
1
$ "harness's notes" left in the second raw
0
$ "Under any `data/`" in the first raw
1
$ the entry lists the values-check raw among the committed paths
1
$ placeholders left in the entry
0
$ lines over 120 characters outside verbatim parts (entry, raw-2 parts, values-check parts)
0
```
