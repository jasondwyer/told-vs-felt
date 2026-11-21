# n — G-TIME-n's BUILD texts: the second blind values-check, as returned, with every disposition

PI date 2026-11-21. Code (the n-build session).

**What was checked.** One blind pass by a subagent over three texts after their edits, at HEAD `4fdcdcc`, on the
coordinating session's routing. It was a second check of the BUILD's texts before the commit request, and it covered
the entry's list of Code's departures, which the first check saw only in an earlier draft:
- T1, the BUILD's RESULTS.md entry, `7e83d278…dc8c` (156 lines), with four placeholders not to be checked;
- T2, the review raw, `15a2548b…2f64` (305 lines): its head and §1, and its §2 only for being byte-equal to the
  review's report;
- T3, the self-test raw, `06bba6f3…c257` (69 lines).

**The checker's brief** was a file in Code's scratch, `S/step4b/gtime/vc2/vc2_brief.md` (`5cf60b36…e7f3`, 147 lines).
The prompt named it by its path and sha256, for the checker to check and read whole. It:
- named the texts and the sources. In Code's scratch, by name and sha256: the versions the first check read, drafts 5
  and 4 and their delta, both .gitignore drafts, the four self-test runs' outputs, the review's brief and report, the
  seat block's unused third entry, and Code's extraction of the commands for the departures check. In the
  repository, the files the texts cite, at HEAD, the first check's committed raw among them, each checked tracked and
  clean;
- set the departures check: this session's main transcript, read only with `jq`, and only its shell commands and their
  outputs from `2ca24e8`'s commit to the command that wrote Code's extraction, masked, with no session id, agent id or
  local path in the report;
- allowed `shasum` by name, and `jq` only for that check. It barred any other interpreter, any write, any network, any
  guard marker in an argv, globs over the root, `results/raw/` or a folder of marker-named files, and Q-F3's folder
  by its plain name in any argv;
- barred anything under `data/m[f]3`, any whole-tree git status, any read, listing, size or time of a ckpt or reports
  file, anything in Code's scratch but the named files, and anything outside the repository and the scratch but that
  transcript;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec with `':!data/m[f]3/**'` on every
  git command over the tree.

**The report** is in §3, extracted verbatim by `jq` from the checker's second hand-back in its own transcript (221
lines, sha256 `f0f98c01201b0d13e36887131fafac49cb880100e7788551dbe767e53ba445e5`).
- The first hand-back (`ab5476d5…9a1e`, 221 lines) differed in one sentence, item 72's evidence, which named the
  local-root prefixes literally. The commit gate refuses those.
- At Code's request the checker returned the report again with only that sentence reworded, to "R has 0 lines naming
  a local root.". The two hand-backs differ in that line alone, by `diff`.
- The report names scratch files by their paths inside the scratch folder, and cites commands by their transcript
  times, in UTC.

**Totals:** 111 items: 92 CONFIRMED, 4 IMPRECISE, 3 FAIL, 12 NOT CHECKABLE; and 7 observations.

**The checker's departures,** as its report states them, are in the BUILD's entry, for the seat to class.

## 1. Dispositions

Every FAIL and every IMPRECISE item is applied, in the checker's words without its command times (the entry gives
none) or as below. Every observation is applied or met. The edits were made to new versioned copies of T1–T3, and §2
gives their check by tool.

- **Items 57, 58 and 59 (FAIL), T1's departures.** Applied: three omissions, now listed:
  - the two globs at the repository's root in one command, an `ls` and a `grep` over `PROPOSAL-n*`;
  - Code's reads of its own memory files in the shell, in four commands;
  - Code's reads of its notes in the app's shared notes folder in the shell, in three commands.

  The "beside the shell" line now says that its shell reads of them are listed above.
- **Item 18 (IMPRECISE), T1:47 and T3:61.** Applied in the checker's words: the docstring's two lines introducing the
  PINs reworded, three in draft 5.
- **Item 27 (IMPRECISE), T1:65–66.** Applied in the checker's words: the first check read the departures only in an
  earlier draft, its counts placeholders, with no transcript to check them against.
- **Item 46 (IMPRECISE), T1:110–114.** Applied in the checker's words: `jq` over this session's transcript in 19
  commands, the replay check's six reads in its three runs, and several of the sixteen direct commands running `jq`
  over it more than once.
- **Item 56 (IMPRECISE), T1:134.** Applied in the checker's words, with "two commands" for its times: every other
  `python` in a command is `pgrep -l python` (eight commands) or a word in the sweep's own `jq` patterns.
- **O1 (item 47's added sentence).** Met by saying so. T1's account of the first check now says that item 47's last
  bullet goes beyond the first checker's words: it adds `prior_state`'s two other refusals of a resume, another
  identity's report and a STOP. The first check's raw, committed at `4fdcdcc`, says the item was applied in its words;
  this raw records the difference.
- **O2 (the re-print of two names).** Applied: the `git ls-files` bullet says that one of the sweeps re-printed those
  two names from the transcript.
- **O3 (`jq` and `sed` over scratch).** Applied as stated plainly: `jq` over scratch files (the sweep's extractions,
  in six commands, and the replay script's edit lists) and `sed` (line prints, substitutions and one in-place edit of
  a scratch draft). Neither is in the briefs' lists of interpreters.
- **O4 (for classing).** Applied as stated plainly: the `grep -rn` over named code files, the `git rev-list --children
  HEAD`, and the `ls -la` over three scratch folders.
- **O5 (the plain name in outputs).** Applied as stated plainly: outputs, not argvs, printed Q-F3's folder's plain name
  three times.
- **O6 (the gate's third id).** Applied: the gate bullet says that the survey's and the seat block's values-checker's
  ids are there among earlier sessions' and subagents' ids.
- **O7 (the reviewer's items for classing).** Applied in T1 and T2. T1 lists the reviewer's five items for classing
  after its "none", and T2's summary says that they follow its departures.

## 2. The edits, checked by tool

Each of the BUILD's three texts went through two version steps, one per check. Each edit was recovered from this
session's transcript by `jq` and replayed on the version before it, each change's old text found exactly once. The
results are byte for byte each next version:
- the first check's dispositions, with draft 5's run: the entry 12 of 12, the review raw 5 of 5, the self-test raw 3
  of 3;
- the second check's: the entry 11 of 11, the review raw 1 of 1, the self-test raw 1 of 1.

That is 33 edits in all. Besides the findings, they carry the counts of Code's sweep, in the first step. In the
second they carry the second check's tallies and departures, in place of their placeholders, and one departure Code
found after the check. The kit's gate script runs `awk` in its check of the manifest's removals, at every non-dry run,
`4fdcdcc`'s among them, and the sweeps, which read commands, did not see it. After the edits, three placeholders were
filled by tool: the two counts of edits, and the commands after Code's last sweep.

## 3. The report, as returned

```text
BLIND VALUES-CHECK (the second): G-TIME-n's BUILD texts after their edits. T1 = S/step4b/gtime/build/entry_v3.md; T2 = S/step4b/gtime/build/review_v2.md (head and §1, with §2 checked by cmp); T3 = S/step4b/gtime/build/selftest_v2.txt.

Checked first, by tool:
- The brief's sha256 matched (shasum), and I read it whole. HEAD is 4fdcdcc. 2ca24e8's commit time is 2026-11-21T03:47:59-05:00, which is 08:47:59Z.
- All 19 named scratch files match their sha256s. Line counts: T1 156, T2 305, T3 69, draft 5 5,208, sweep file 147.
- Every named repository file is tracked and clean (rev-parse equals hash-object). That covers the driver, .gitignore, the first check's raw (bec84764…9c10), the supplement, the block, the spec raw, RESULTS.md, PROPOSAL-n v0.2, LOCK-n.md (88d9fe7b…e9d5), CLAUDE.md, .gitattributes, resume.py, keys.py and all 16 valence_core/n/*.py.
- The package digest over HEAD's blobs, in package_sha256_of's form (valence_core/m/resume.py:328–350), is 06b55761052508f93fb67993b4b4c7574483aa38d2168b8254b3c0b7417a1d39.
- Numstat from the repository root:
  - HEAD's driver to draft 5: +1437 −6;
  - draft 4 to draft 5: +17 −2;
  - HEAD's .gitignore (383 lines) to gitignore_v2 (397 lines): +14 −0;
  - gitignore_v1 to gitignore_v2: +5 −5.
- The delta file is byte-equal to `diff` of draft 4 against draft 5.
- HEAD's driver blob (93951020…) is the same at c9d35e2, 2ca24e8, 4fdcdcc and ef105f1, and its sha256 is 593a140d…a549.
- T2 from line 117 is cmp-equal to S/step4b/gtime/review_report.md (189 lines, 004f9c8e…0915).
- S/step4b/gtime/sweep_final.jsonl is byte-equal to the first 147 Bash calls after 08:47:59Z, as `jq -c` {t, c} from the transcript. The 147th call (10:46:25) is the one that wrote the file. So the window is 147 commands, from 08:48:08 to 10:46:25.
- Draft 5's _gtime_selftest has 41 `chk(` lines. Two of them run in loops of eight (the tamper cases and main()'s argv cases), so 55 checks execute. With cmd_selftest's environment check that is 56, and 56 = 634 − 578. So 634 = 633 + 1 holds, and so does 645 = 634 + 11.

Names used below:
- d5 = S/step4b/gtime/draft5/n_sessions.py;
- R = S/step4b/gtime/review_report.md (R:n is T2:n+116);
- V1 = results/raw/2026-11-21_n-gtime-supplement-and-build_valuescheck.md;
- SP = the supplement; B = the block; spec = the spec raw;
- HD = scripts/n_sessions.py at HEAD;
- c3 = S/step4b/gtime/seat/commit_v3/entry.md;
- n = PROPOSAL-n-bk-reconciliation-v0_2.md.
Times are the transcript's, in UTC.

ITEMS

T1
1. T1:1–3. The gtime and gread-bench commands; n §8 step 11; "Build on the PINs"; the driver alone; the package at the lock's digest. CONFIRMED. d5:5091–5092 and :5113–5132; n:159; RESULTS.md:91–92; only the driver and .gitignore change, and the package digest does not move.
2. T1:4. valence_core/n/ stays at 06b55761…1d39 (LOCK-n v0.1 §18). CONFIRMED. The computed digest above; LOCK-n.md:781, inside §18 (:776–820).
3. T1:5–6. It refuses before any read, with exit 2 and a REFUSED line. CONFIRMED. d5:4339–4345.
4. T1:6–22. The list of conditions in _gtime_prepare's order (item 47 applied), with the --ruling refusal. CONFIRMED. The code's order is: paths and artifact d5:4194–4215; the bench folder :4216–4223; pod, cuBLAS, known answer and rulings :4224–4237; weights :4245; driver :4249; rendering :4256; the lock's inputs :4258 (gtime_lock_inputs :3842–3889, whose G-VEC PASS is HD:2691); R6, backend, package and closure :4264–4275; the read plan :4286; prior_state :4291 (HD:917–945, unchanged in d5). Observation 8 is met: the identity check (:4276–4278 into :3910) exits 1 and is not in the list.
5. T1:24. Every check but the driver's holds at a smoke too (F10). CONFIRMED. d5:4249 is the only pin that depends on the smoke flag; R:59.
6. T1:24–25. G-VER runs before the load, and its STOP exits 2. CONFIRMED. d5:4292–4297 and :4347–4348.
7. T1:25–26. After the load, the provenance is checked again, and the shape against the identity's (item 51, verbatim). CONFIRMED. d5:4301–4305; the identity takes env.shape (:4263 and :4276–4278).
8. T1:26–29. The 18 reads go through the runner. On COMPLETE: the records are read back, io_bench re-keys the first +1 record, and data/n/gtime/gtime.json (n-gtime-v1) is checked by check_gtime. Exits are 0, 3 and 1. CONFIRMED. d5:4350–4396, :3743–3748 and :4083.
9. T1:30. gread-bench runs on the laptop, model-free, and is refused on a pod. CONFIRMED. d5:4450–4475 (:4459–4460) and :5063–5071.
10. T1:31–32. The PINs are listed in short, as sent except GT9's benchmark and GT11's outputs (item 72). CONFIRMED. Compared d5:205–233 with spec:42–186. Only GT9 departs (re-keyed, against spec:127's "160 example records") and GT11 departs (steered cells on the box, against spec:153). The owed-wording bullet is gone.
11. T1:32–34. The seven are with the seat (Q1–Q7), Q8 is in the supplement at 4fdcdcc, and the run waits. CONFIRMED. B:349–372; SP:13–14 and :87–89; `git show --name-status` of 4fdcdcc and of 2ca24e8.
12. T1:35. +14 lines, the second draft dee52f42…b272. CONFIRMED. Numstat and shasum.
13. T1:36–39. What is admitted and what is kept on the box; O2; GT11's form is two lines away. CONFIRMED. gitignore_v2:331–344 admits the shadow cell, the report and the artifact by name. R:170 is O2; spec:153 is GT11. The v1-to-v2 diff removes exactly the two steered-cell lines.
14. T1:40–41. The block changed after the review, on O2; the review read 1f2461bd…58b8, which admitted all three cells (observation 4). CONFIRMED. shasum of gitignore_v1; the v1-to-v2 diff; review brief:15–16.
15. T1:42. The draft was tested by dry-run adds in a throwaway repository. CONFIRMED for the second draft at 09:28:19 (`git init -q` and `git add --dry-run -- .` under S). The output added only the .gitignore, the report, the shadow cell, the artifact and the BACKEND extension's cell. The first draft's test ran before the window.
16. T1:44–45. 621/621 (578 + 43), 623/623 and 633/633. CONFIRMED. The outputs of runs 1, 3 and 4; RESULTS.md:1309 has 578/578 for ef105f1, whose driver blob is HEAD's.
17. T1:46–47. Draft 5 is 4616f9c3…2553, 5,208 lines, ran 634/634, and has one check more, M8's. CONFIRMED. shasum and wc; run 5's output (400a47ca…8b17); the delta adds one chk (4886a4888,4901); the static count above.
18. T1:46–47 and T3:61. "the docstring's PIN line reworded". IMPRECISE. The delta rewords the two docstring lines that introduce the PINs (draft 4:205–206, which become three lines, d5:205–207). No GT line changes, and "PIN line" reads as one PIN. Put instead:
    - at T1:47: "and the docstring's two lines introducing the PINs reworded (three in draft 5)";
    - at T3:61: "and the docstring's two lines introducing the PINs reworded, three in draft 5 (the values-check raw committed at 4fdcdcc, s1)".
19. T1:48. Each run had exit 0 and an empty stderr. CONFIRMED. All four .exit files read "exit 0", and all four .err files are 0 bytes (runs 1, 3, 4 and 5).
20. T1:48–49 (runs 3, 4 and 5). The temporary folder was empty before and after each run, and PID 8051 was the only Python process after it. CONFIRMED.
    - Before (08:50:51, 09:32:28, 10:37:53): each printed the overlay driver's sha256 (drafts 3, 4 and 5), a temporary folder count of 0, no prior output file and no n_sessions process.
    - After (08:51:48, 09:33:06, 10:38:05): each printed "exit 0", a 0-byte stderr, a count of 0, and one `pgrep -l python` line, 8051 (Q-F3's campaign, RESULTS.md:212 and :681).
21. T1:48–49. The battery windows were granted, and run 1's steps. NOT CHECKABLE. The grants are messages, and run 1 ran before the window.
22. T1:50. The box count is 645. CONFIRMED. 634 + 11; RESULTS.md:1529 and :1843–1844.
23. T1:51–54. The review's link and tallies. CONFIRMED. R:12 (no BUG), :14–61 (F1–F5 RISK, F6–F11 NIT), :63–116 (M1–M13), :118–149 (B1–B7), :151–178 (O1–O6), :180 (none).
24. T1:55–57. Seven built in; a kill for every mutant but M8; M8 found alive; draft 5 adds the case, so every mutant is killed (items 64 and 108). CONFIRMED.
    - d5:4888–4901 expects rc 2, no load, no report, and a REFUSED line containing "is not on the stage root's filesystem". That text is printed only at :4223, under the guard at :4222.
    - With that guard changed to `if False:`, the fsdev run would pass, load and complete, so the check would fail.
    - The other twelve kills are present: M1 :4926–4931; M2–M5 and M12 :4762–4776; M6 :4902–4912; M7 :4876–4887; M9 :4541–4553; M10 :5040–5062; M11 :4974–4977; M13 :4647–4650.
25. T1:58–63. The first check's scope, raw and tallies; the five FAILs are one finding. CONFIRMED. V1:5–13, :32 (97 + 7 + 5 + 19 = 128; 9 observations) and :38–49; git show of 4fdcdcc (A for V1 and SP).
26. T1:63–64. Each disposition is applied as V1 §1 states. CONFIRMED.
    - Item 47: T1:6–22. Item 51: T1:25–26. Items 64 and 108: T1:55–57. Item 70: T1:83–84, verbatim. Item 72: the owed bullet is dropped, with T1:31–32 and :46–47.
    - Items 95 and 108: T2:36–39. Item 98: T2:50–54. Item 108: T2:87–90. Item 111: T2:102–103, verbatim.
    - Item 126: T3:50–52, verbatim. Item 127: T3:66–68, with 634 and 645.
    - Observation 2: T1:111–112. Observation 3: T1:95–96. Observation 4: T1:35 and :40–41, and T2:105–107. Observation 7: T2:50. Observation 8: met.
    - One nuance is observation 1 below.
27. T1:65–66. "this entry's departures among them, which the first never saw". IMPRECISE. V1's items 41 and 79–84 read entry_v2's departures section, with its counts as placeholders: items 80, 81 and 83 are CONFIRMED, and 79 and 82 are NOT CHECKABLE. Put instead: "this entry's departures among them, which the first read only in an earlier draft, its counts placeholders, with no transcript to check them against. @VC2@"
28. T1:67. Nothing ran on a model. CONFIRMED for the window. The only Python processes were the three `--selftest` runs, whose HF cases skip on the laptop (HD:8–9, :1539, :3676).
29. T1:69–71. F4. CONFIRMED. G-VER and the load run once prior_state passes a resume (d5:4291–4300). d5:4815–4822 checks two loads in loads_ms. R:36–41.
30. T1:72–77. F8, all three points. CONFIRMED. R:52–55; campaign_counts d5:3914–3930; the line marks :4311–4317 and :4363–4364; SP:93–97.
31. T1:78–79. F10, corrected in the supplement's §4. CONFIRMED. d5:4249; SP:98–100.
32. T1:80. F11. CONFIRMED. R:61; the traps at d5:4955–5021.
33. T1:81–82. B5. CONFIRMED. d5:4272 (exact closure) and :4565 (inclusion only); R:139.
34. T1:83–84. B7 (item 70, verbatim). CONFIRMED. R:149; d5:3744 and :4214–4215.
35. T1:85–86. B1, B2 and B6. CONFIRMED as the review's risks (R:120–127, :141–144). The carry to the launch files is a plan.
36. T1:88–90. The kit's pathspec named the folder plainly in both kit versions. NOT CHECKABLE. The grep at 08:53:19 shows the first kit's kit_gate.sh and kit_lib.sh hold the bare name. Kit2's first version was not printed in the window.
37. T1:90–93. The two lists of windows. CONFIRMED.
    - Kit2: the outputs at 08:52:54 show verify runs on parents ab72d0f, 616e940, bc50244, 0744136, db00d6d, 1641948 and 411b15c.
    - First kit: the outputs at 08:53:40 map parents to the children 355e3a2, 035947e, 516b60f and d85fc34.
    - `git log --no-walk` gives each listed commit those parents, in that order.
    - "and earlier ones before them" is not checkable.
38. T1:95–96. The sweep's start (observation 3). CONFIRMED. RESULTS.md:139–140; c3:58–59.
39. T1:96–99. The sweep's counts as carried. CONFIRMED against c3:60–69 and RESULTS.md:141–145.
40. T1:99. "The other windows were not swept, and windows before the kit were not checked." NOT CHECKABLE.
41. T1:99–100. Kit2's v-next scripts use the bracketed form. CONFIRMED. Outputs: 09:57:40 (kit_lib_v2's pathspec array is bracketed); 09:41:45 (the overlay script's pathspec is bracketed); 09:57:00 (the fourth gate script names the plain form only in a comment).
42. T1:101–102. The id list held both ids at 2ca24e8. NOT CHECKABLE. See observation 6. Consistent with c3:88–89.
43. T1:102. 2ca24e8's entry named the survey's id alone. CONFIRMED. RESULTS.md:161–162.
44. T1:103–106. The seat block's grants. NOT CHECKABLE. Consistent with c3:73–75. The third entry is unused: the committed entry differs from it (26 of 26 edits against 29 of 29, RESULTS.md:121; the deabf3f start against 411b15c's).
45. T1:108–109. The window and its 147 commands. CONFIRMED (see "Checked first").
46. T1:110–114. "`jq` over this session's own transcript ... 22 times". IMPRECISE.
    - The members hold. Five: 09:39:08, 09:39:22 (it printed four call-id lines only, the word-splitting slip), 09:39:30, 09:40:14 and 09:40:24. One: 09:44:11. Six reads in three runs: 10:29:38, 10:30:14 and 10:31:39, two texts a run. Ten: 09:45:48, 09:46:02, 09:47:01, 09:47:15, 09:48:05, 09:48:31, 09:48:54, 10:39:52, 10:40:37 and 10:46:25.
    - But "22" counts sixteen commands and six reads. By command the total is 19. By jq process it is more than 22: 09:39:22 ran jq on the transcript twice, 09:47:01 four times, 09:47:15 and 09:48:31 three times each, and 09:39:30 and 09:40:24 once more per call id.
    - Put instead: "`jq` over this session's own transcript, outside the repository, the HF cache and the scratch folders, in 19 commands: five to confirm the window steps of runs 1, 3 and 4 for the self-test raw (one of them printed only call ids, a zsh word-splitting slip); one to check the coordinating session's framing of Q8 as sent; three runs of the replay check of the supplement's edits, which read it six times, one read per text a run; and ten to sweep this session's shell commands for this list. Several of the sixteen direct commands ran `jq` over it more than once;"
47. T1:115–116. jq over the two subagents' transcripts, once each. CONFIRMED. 09:24:25 and 10:26:32 each select the hand-back. The outputs were 189 lines, 004f9c8e…, and 223 lines, d8d53dc0….
48. T1:117–118. One grep with the bare name. CONFIRMED. At 08:53:19, `grep -l '<the bare name>' S/step4b/kit/*.sh`. It is the window's only plain naming (a jq regex over all 147 commands). RESULTS.md:138–139, committed before the window, already cites the note of 2026-11-21.
49. T1:119–120. One git log with %ad. CONFIRMED. 08:53:02, `--format='%h %p %ad %s' --date=format:'%m-%d' … -- . <pathspec with data/m[f]3>`.
50. T1:121–122. Two git show --stat runs. CONFIRMED. 08:53:57 (89a55c3) and 09:45:31 (d7d5e5b), each with the pathspec.
51. T1:123–124. One git ls-files of data/n/ckpt/*. CONFIRMED. 09:32:59. It printed two names, masked: data/n/ckpt/backend-ext/NN-V__none__N.json and data/n/ckpt/backend-ext-N/NN-V__none__N.json.
52. T1:125–126. awk three times. CONFIRMED. At 09:44:59 there are two: `awk 'NR<=148 && /^#/ …'` over n, and `awk -F: '$1<=160'` over grep's heading list. At 09:45:48 there is one: `awk '$1 >= "2026-11-21"'`. There is no other awk.
53. T1:127–128. The second .gitignore draft's git init and dry-run adds. CONFIRMED. 09:28:19.
54. T1:129–132. Eight index checks, one ls-files and one find. CONFIRMED.
    - `git diff --cached --name-only | wc -l` ran at 08:48:18, 08:49:11, 08:51:48, 09:29:47, 09:33:06, 10:32:30, 10:36:31 and 10:38:05, and printed 0 each time.
    - At 10:27:55 the overlay folder's `git ls-files` printed nothing, and `find …/overlay5 -type f | wc -l` printed 173, after the overlay script's "no ckpt or reports entry".
55. T1:133–134. No guard marker in any argv, and no Python but runs 3, 4 and 5. CONFIRMED.
    - No command holds a marker (a jq regex over all 147, in any case).
    - The globs that could expand to one: `cd jl*/.venv/bin` inside a subshell at 08:50:59, 09:32:35 and 10:38:02, which is the approved form; and the root glob at 09:44:52, whose only match is PROPOSAL-n-bk-reconciliation-v0_2.md (git ls-files: tracked, untracked and ignored).
    - Python ran only as `./python -I -B … --selftest`, at those three times.
56. T1:134. "Every other `python` in a command is `pgrep -l python`". IMPRECISE. Eight commands hold `pgrep -l python`. The sweep commands at 10:40:37 and 10:40:49 also hold the word, in jq patterns and an echo label: `test("python") and (test("\\./python -I -B") | not)`. Put instead: "Every other `python` in a command is `pgrep -l python` (eight commands) or a word in the sweep's own `jq` patterns (10:40:37 and 10:40:49);"
57. T1:107–134, an omission. FAIL. At 09:44:52 there are two globs at the repository's root in an argument: `ls PROPOSAL-n* 2>/dev/null` and `/usr/bin/grep -n 'No looks' PROPOSAL-n*.md`. The briefs bar this form (review brief:75–77), and 2ca24e8's entry declared its own root globs (RESULTS.md:135–137). Add: "- two globs at the repository's root in an argument, both at 09:44:52: one `ls` and one `grep` over `PROPOSAL-n*`. The briefs bar that form. Each expanded to `PROPOSAL-n-bk-reconciliation-v0_2.md` alone, whose name holds no guard marker;"
58. T1:107–134 and :143–145, an omission. FAIL. There are shell reads of Code's memory folder, which is outside the repository, the HF cache and the scratch folders. That is T1's own criterion at :110 and check (c).
    - 09:38:50: `wc -l $M; /usr/bin/grep -n '…' $M`, where M is one memory note.
    - 09:38:53: `sed -n 60,126p $M`.
    - 09:58:14: `grep -n` over the memory index.
    - 10:39:28: `cat` of one memory note.
    T1:143 places memory reads "beside the shell". Add: "- reads of Code's own memory files in the shell, outside the repository, the HF cache and the scratch folders, four times: a `wc -l` and a `grep`, then a `sed` line print, of one memory note (09:38:50, 09:38:53); a `grep` over the memory index (09:58:14); and a `cat` of one memory note (10:39:28);". Also put at T1:143: "beside the shell (its shell reads of them are listed above), listed for completeness: …".
59. T1:107–134 and :143–145, an omission. FAIL. There are shell reads of the app's shared notes folder, which is also outside those three places.
    - 09:29:47: `shasum -a 256 "$N" …; wc -l < "$N"` on one note.
    - 09:42:21: `/usr/bin/grep -o 'TMPDIR=[^ ]*\|…' "$N/$f"` over two notes.
    - 10:33:25: `shasum` and `wc -l` over two notes.
    Add: "- reads of Code's notes in the app's shared notes folder in the shell, three times: `shasum` and `wc -l` of one note (09:29:47) and of two (10:33:25), and a `grep -o` over two (09:42:21);"
60. T1:136–139. Neither entry declares the two jq listings, and the quotation is exact. CONFIRMED. RESULTS.md:131–134 and c3:50–53. The quotation is at RESULTS.md:132.
61. T1:136–139. The two jq calls, and "was two calls". NOT CHECKABLE (before the window).
62. T1:140. The first .gitignore draft's dry-run adds. NOT CHECKABLE (before the window).
63. T1:141–142. The reviewer's departures are none, by its report, and the first checker's are in 4fdcdcc's entry. CONFIRMED. R:180; RESULTS.md:61–75.
64. T1:146–147. The two ids have been in the gate's list since its fifth version, which 4fdcdcc ran. CONFIRMED.
    - At 09:57:15, the fifth version was written from the fourth with two ids added. They are the subagents whose transcripts were read at 09:24:25 and 10:26:32.
    - The fifth version ran at 10:31:52 (dry) and at 10:36:05, before 4fdcdcc's commit at 10:36:13.
65. T1:147–148. The sixth version, and whose the other ids are. NOT CHECKABLE.
66. T1:149–152. Committed by path. CONFIRMED against the brief's account of the BUILD's commit.
67. T1:154–155. The count, the push and the next step. NOT CHECKABLE. The wait on Q1–Q8 matches SP:13–14.

T2
68. T2:1–7. HEAD 2ca24e8; 593a140d…a549 to f4e2c8b9…d608 (5,057 lines); 1f2461bd…58b8. CONFIRMED. Review brief:7–16; HD's shasum; R:4 and :7.
69. T2:9. Draft 3 passed 623/623. CONFIRMED. selftest_run3.txt; review brief:19–20.
70. T2:11–12. The brief is 9ab6524c…afeb, 93 lines, checked by sha256. CONFIRMED. shasum and wc; R:4.
71. T2:13–22. What the brief named, asked and barred. CONFIRMED. Review brief:7–43, :44–52 (the five things), :54–65 and :68–93. Its items 1–5 are cmp-equal to this brief's. Both the block and the spec raw are at 2ca24e8 (git show).
72. T2:24–26. The report was extracted by jq from the hand-back (189 lines, 004f9c8e…), and it names scratch files only as S/.... CONFIRMED. 09:24:25's command and output; cmp; R has 0 lines naming a local root.
73. T2:28–34. In sum. CONFIRMED. R:12–180.
74. T2:36–39. Draft 4 (24b0cd44…22aa, 5,193 lines), the seven built in, all kills but M8, 633/633; draft 5 (4616f9c3…2553, 5,208 lines) with the case through the stage, 634/634. CONFIRMED (items 95 and 108).
75. T2:43–49. F1. CONFIRMED. d5:4321 (clock=env.clock); :4166 and runner.py:274 (perf_counter); :4704–4706 (the 1 ms tick); :4762–4776 (18,997 ms; 2.0 ms on reads 1–17; five *_h figures).
76. T2:50–59. F2 (item 98 and observation 7). CONFIRMED. d5:4876–4887; :4652–4664 and :4888–4901; :4926–4931; :4902–4912; :4541–4553.
77. T2:60–62. F3. CONFIRMED. d5:5040–5062.
78. T2:63–66. F4. CONFIRMED. d5:4291–4300 and :4815–4822; R:36–41.
79. T2:67–69. F5. CONFIRMED. d5:3994 and :4004–4005. No case in d5:4478–5071 induces a cleanup failure.
80. T2:70. F6. CONFIRMED. d5:3751.
81. T2:71–73. F7. CONFIRMED. d5:4088–4093, :4114, :4129 and :3792; LOCK-n.md:464 (§6); the tampers at :4790–4797.
82. T2:74–81. F8. CONFIRMED. R:52–55; d5:3914–3930, :4311–4317 and :3946–3959; SP:93–97.
83. T2:82. F9. CONFIRMED. d5:4647–4650; valence_core/n/guard.py:84–87.
84. T2:83–84. F10. CONFIRMED. d5:4249; SP:98–100.
85. T2:85–86. F11. CONFIRMED. R:61.
86. T2:87–90. M1–M13 (item 108). CONFIRMED, as in item 24.
87. T2:91–94. B1, B2, B6 and B3. CONFIRMED. R:120–129 and :141–144.
88. T2:95–96. B4. CONFIRMED. R:131–137.
89. T2:97–99. B5. CONFIRMED. R:139; d5:4272 and :4565.
90. T2:100–103. B7 (item 111, verbatim). CONFIRMED. R:146–149; d5:4075–4077; valence_core/n/schema.py:1159–1161.
91. T2:104. O1. CONFIRMED. R:153–168.
92. T2:105–107. O2 (observation 4). CONFIRMED. R:170; SP:87–89; the gitignore v1-to-v2 diff.
93. T2:108–113. O3–O6. CONFIRMED. R:172, :174, :176 and :178.
94. T2:117–305. §2 equals the report. CONFIRMED (cmp).

T3
95. T3:1–2. n §8 step 11, and n §3's G-TIME-n paragraph. CONFIRMED. n:159 and n:118.
96. T3:4–5. The same bytes at three commits; 4616f9c3…; +1437 −6. CONFIRMED. One blob id at all three; shasum; numstat.
97. T3:6. The .gitignore lines do not enter the self-test. CONFIRMED. V1 item 115 shows draft 4 never names gitignore, and the delta adds no mention.
98. T3:7–11. The digest is unmoved; LOCK-n v0.1 §18's full sha256; computed by shell over HEAD; the self-test's check (GT3). CONFIRMED. My computation; the overlay script's "package by shell 06b55761…" at 09:28:51 and 10:27:55; d5:4561–4566.
99. T3:9. "over every overlay below", for the overlays of runs 1 and 3. NOT CHECKABLE (built before the window).
100. T3:13–15. The HF cases skip and are counted, and the schema's cases are one line. CONFIRMED. HD:8–9, :246–247, :1539 and :3676.
101. T3:16–19. The overlays of runs 4 and 5. CONFIRMED. At 09:28:51 and 10:27:55 the bracketed v2 script printed "overlay: 173 files from c9d35e2 (archive names; no ckpt or reports entry); LOCK-n.md 88d9fe7b…" and the draft's sha256 as the driver. At 10:27:55 the overlay's driver cmp-equals draft 5.
102. T3:16–19. The overlays of runs 1 and 3, "G-CAL-n's BUILD self-test paths", and "the only change". NOT CHECKABLE.
103. T3:20–23. The command. CONFIRMED. At 08:50:59, 09:32:35 and 10:38:02: `( cd <repo> && cd jl*/.venv/bin && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TMPDIR=S/step4b/gtime/tmp nice -n 19 ./python -I -B S/step4b/gtime/overlayN/scripts/n_sessions.py --selftest ) > ….txt 2> ….err; echo "exit $?" > ….exit`.
104. T3:24–26. The before and after steps of runs 3, 4 and 5. CONFIRMED, as in item 20.
105. T3:24–26. The grants, and run 1's steps. NOT CHECKABLE.
106. T3:28–33. Run 1. CONFIRMED.
     - Draft 1's sha256 5c063ae2…c03d (4,996 lines) was printed at 09:55:28 for S/step4b/gtime/draft/n_sessions.py.
     - The output's sha256 matches, and T3:32 with its five leading spaces cut cmp-equals the output. Exit 0.
     - 578 is at RESULTS.md:1309. The environment check follows _gtime_selftest (the hunk at 351/408). V1 item 122 gives the 42.
107. T3:35–37. Draft 2. CONFIRMED. ed9da846…6ea8 (5,034 lines) was printed at 09:55:28. Observation 4 is at RESULTS.md:117–120, and the template is at d5:4366–4370. "never ran on its own" is not checkable.
108. T3:39–45. Run 3. CONFIRMED. f4e2c8b9… is at review brief:11 and was re-hashed in the overlay at 08:50:51. The traps are at d5:4955–4973. Exit 0, the output's sha256, and the line (cmp).
109. T3:47–55. Run 4 (item 126, verbatim). CONFIRMED.
     - The sha256 matches (shasum). +156 −20 is V1:111.
     - draft 4:4221 is d5:4222, since the delta shifts lines after 206 by one.
     - 633 − 623 = 10: eight checks more plus two tamper cases, the eight-case loop at d5:4794–4803.
     - Exit 0, the output's sha256, and the line (cmp).
110. T3:57–64. Run 5. CONFIRMED, except the wording in item 18. The sha256 matches; +17 −2; the one check at d5:4888–4901 (exit 2, no load, no report); exit 0, the output's sha256, and the line (cmp).
111. T3:66–69. The box (item 127). CONFIRMED. 634 + 11 = 645. G-VEC's box self-test has its 14 HF checks in place of three skip lines (RESULTS.md:1843–1844). G-CAL-n's, the last box run in the Log, has the same 11 (RESULTS.md:1529). _gtime_selftest has no branch on the site. The launch files' restatement is a plan.

TOTALS: 111 items: 92 CONFIRMED, 4 IMPRECISE, 3 FAIL, 12 NOT CHECKABLE.

OBSERVATIONS
1. T1:21–22 adds a sentence to item 47's replacement (V1:197): "A resume's report is the same identity's and did not end in a STOP". It is accurate: HD:936–940, and prior_state lies outside the HEAD-to-d5 hunks. But V1:56 says the item is applied "in the checker's words". Either say so, or drop the sentence.
2. At 09:48:31, one of the ten sweep commands re-printed from the transcript 09:32:59's output, including its two names under data/n/ckpt. These are names only and no new listing. T1:123–124 could note the re-print.
3. This check's brief excepts jq by name beside shasum, so it treats jq as an interpreter. If the seat does too, Code's jq over scratch files is undeclared:
   - 10:40:37, 10:40:49, 10:41:07, 10:41:54 and 10:41:59, over S/step4b/gtime/sweep_cmds.jsonl;
   - 10:46:25, over S/step4b/gtime/sweep_final.jsonl;
   - the replay script's jq over its edit lists.
   sed also ran often: line prints, substitutions, and one in-place edit of S/step4b/gtime/supp/supp_v1.md at 09:54:36. The briefs' lists name only python, python3, ipython, node, perl and awk.
4. For classing, not barred by my reading:
   - `grep -rn` over valence_core/n/*.py and scripts/n_sessions.py at 09:43:26. No tree or data path was in scope; the first checker's analogous `git grep` is declared;
   - `git rev-list --children HEAD` at 08:53:40, which prints ids only, with no pathspec;
   - `ls -la` over three scratch folders at 09:37:29.
5. Outputs, not argvs, printed Q-F3's folder's plain name: at 09:41:45 and 09:57:00 (script comments) and at 09:57:26 (a draft head's text; the committed V1 has the bracketed form).
6. The fourth gate version listed three ids before the two added at 09:57:15. T1:101–102 and :148 name two of them. If the third is another subagent's, the entry could say whose.
7. After "DEPARTURES: none.", R:182–187 lists five items "For classing" (sed -n, grep -o over data/n/gcal/gcal.json and data/n/gvec/gvec.json, wc -l, a counting loop). T1:141 and T2:34 say "none". 4fdcdcc's entry carries its own checker's for-classing list (RESULTS.md:69–73), so the BUILD's entry could point to the reviewer's.

DEPARTURES
- One `grep -n` over S/step4b/gtime/draft5/n_sessions.py with a `^def ` pattern printed the file's def lines (about 95). That goes beyond the docstring, the G-TIME-n section and main(), which the brief names for reading draft 5.
- I ran one `jq` over S/step4b/gtime/sweep_final.jsonl, printing its five largest command lengths. The brief allows jq on the transcript only.
- I made two transcript reads outside the window, by jq. One printed the timestamps of the five Bash calls in the minute before 08:47:59Z, to place the window's start. The other counted Bash calls to the transcript's end (151) and printed a masked fragment of the call at 10:46:57, to find the window's end.
- Several transcript prints were whole tool results of window commands, masked, rather than only the lines a finding needs. Among them was 09:44:52's output, which held the block's first 41 lines.
- I used `git diff --no-index` with -U2, -U0 or -U1 instead of -U3 for the review and self-test raws' diffs and the two .gitignore diffs.
- For classing, not barred by my reading:
  - greps of RESULTS.md beyond the two entries (the self-test counts, PID 8051 and the entry headings);
  - reads of HD at prior_state, gcal_gvec_inputs and the selftest's head;
  - T2:117–120, read with its head (the same bytes as the report);
  - `git ls-files -c -o` and `-o -i --directory`, with the pathspec, filtered to root names beginning PROPOSAL-n;
  - `git log --no-walk` over named commits;
  - one zsh `=` expansion error (`echo ======`) that stopped a command line before its second diff, which then ran on its own.
- No guard marker reached any argv. Q-F3's folder appeared only as data/m[f]3 or inside bracketed regexes. Nothing under data/m[f]3, data/*/ckpt or data/*/reports was read, listed, sized or timed, and no whole-tree git status ran. In S I read only the brief and the named files, with no listing, find or glob. Outside the repository and S I read only the transcript, by jq. No interpreter but shasum and jq ran, nothing was written, and there was no network use.
```
