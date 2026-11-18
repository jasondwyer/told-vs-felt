# n step 4 — driver v2f's commit texts: the blind values-check, as returned, with every disposition

PI date 2026-11-18. Code (the n-build session).

**What was checked.** One blind pass by a subagent over four drafts:
- T1, the entry (`RESULTS.md`, the Log's head), sha256 `fd9f0db1…71f6`;
- T2, n-build's close line on `6df2131`'s entry, `3bfd7f9d…608b`;
- T3, the self-test raw, `7ac49976…af17`;
- T4, the review raw's head and dispositions, `f47db66f…409f`.

**The checker's brief:**
- named the sources:
  - the seat's answers of the third sitting, the ruling raw and ADDENDUM-n2 at root;
  - `RESULTS.md`'s entries of `6df2131` and `ad856f0`, HEAD's driver, the package modules and git history;
  - in Code's scratch, by name only: the two driver drafts, the two self-test outputs, and the review's report and
    brief;
  - the coordinating session's words and n-analyzer's, which are in no file, quoted verbatim;
- quoted the list of record v2's items 1–5, verbatim;
- required item 3's pathspec and the `data/mf3` exclusion on every git command over the tree, and that a glob is
  expanded and read before it is looped over;
- required tracked status to be read by `rev-parse` against `hash-object`, per the coordinating session's `ls-files`
  finding;
- barred any interpreter, any write, any network and any guard marker in an argv; anything under `data/mf3`,
  `data/*/ckpt` or `data/*/reports`; and, in Code's scratch, anything but the named files.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (127 lines, sha256
`d21803d6…732b`). It names no local path.

**Totals:** 95 items — 79 CONFIRMED, 5 IMPRECISE, 1 FAIL, 10 NOT CHECKABLE — and 12 observations.

**The checker's departures,** as its report states them, for the seat to class. All were model-free and read-only: no
interpreter, write or network, no guard marker in any argv, and nothing under `data/mf3` listed or read.
- (a) Two `git log` commands without item 3's pathspec and the mf3 exclusion. They printed ids and subjects only.
- (b) `git check-attr diff --` and `git check-ignore -v --no-index` on named paths under `data/n/ckpt` and
  `data/n/reports`: backend-ext-2's cell and report, neither on disk, and backend-ext's committed cell for check-ignore.
  They ran without item 3's pathspec and printed only attributes, ignore rules and the given names. check-ignore is not
  in item 1's list.
- (c) `git rev-parse --verify -q HEAD:<path>` on named data paths outside ckpt, reports and mf3, and `git ls-files` on
  two quoted globs over the model folder, without item 3's pathspec.
- (d) A `git diff --no-index` between the two named drafts, piped to a grep for hunk headers. The grep ran over the
  diff's output, not over a scratch folder.

## 1. Dispositions

**The FAIL, applied in T1.**
- **33** (R7's last clause). It now quotes n-analyzer's own words: n-analyzer, told of R7: "backend-ext-2 never reaches
  the reader, so R7 needs nothing from me: load_campaign and verdicts refuse any identity whose stage is not
  "campaign"."

**The IMPRECISE items, all applied:**
- **36** (T1, the resume's copy-in). Code's reading differs from the checker's on `cmp`, because the checker had no
  source for it: the coordinating session's later words allow it. They are "per-file cmp or shasum on names taken from
  a committed record, or one aggregate digest", and, of the fresh copy, "by digest or cmp, never by a listing (§7)".
  T1 now cites the first, names `cmp -s` (which prints nothing), and quotes §7.
- **42** (T1). "The kind's place is after non-finite, as ADDENDUM-n2 §2.1 has it; directly after it, ahead of
  identity-bound in `schema.PAUSE_KINDS`' order, is Code's reading, for the seat."
- **43** (T1). The departure now says "non-Python, model-free and read-only", c4's words. The loop's detail is Code's
  own account.
- **87** (T4, O3), in the checker's words. "The seat's §4 names backend-ext's cell and report as what is pushed, and
  words the screen's clearance over `data/n/ckpt/**`; whether it reaches backend-ext-2's cell and report is for the
  seat."
- **90** (T4, O6). It now reads "Taken in part". The cells are hashed, and the report's sha256 is printed on a line of
  its own before G-VER, not on the STAGE line. The ruling-sha check is not taken, and the reason is given: a COMPLETE
  report holds no standing pause, and the printed sha256 names the report that records the ruling's.

**The NOT CHECKABLE items** (9, 10, 13, 19, 41, 45, 48, 61, 62, 65) stand as declared, with no change. They are:
- files and a commit still to come;
- the box's plan;
- Code's own conduct;
- the agreed names, which are in no file.

**The observations:**
1. Applied in T1's order item 3. The launch files go to the coordinating session, which relays them, in the same box
   session on the same characterized backend.
2. Applied in T2. The two §1.4 rulings are quoted there: "The extension's entry carries the pause, the ruling's sha256
   and the figures", and R3's acceptance, "the lock's bound is ADDENDUM-n2's C".
3. Answered with item 36. `cmp -s` reads the arrays' bytes, as `shasum` does, and prints nothing. Whether it falls
   under item 1's digest form is the seat's to class; the coordinating session's form names it.
4. Applied in T1's R8. The p90 is the coordinating session's line ("Keeping p90 is fine if you declare it"); label's
   median and the two counts go beyond it, declared for the seat to strike.
5. Applied. The repeated "for one call" is gone.
6. Applied in T1's item 3: backend-ext-2's own lines are named.
7. Applied in T3: the box's count by arithmetic, 389.
8. Applied in T1's headline. Both runs were in windows granted one at a time across sessions, so no other battery ran
   in them, under Q-F3's standing rules for the laptop. Code states nothing about Q-F3's campaign process then, which
   it did not observe.
9. Applied in T1's "Why (b)": the coordinating session's "v2e" and "v2e's commit" are v2f and this commit.
10. Applied in T4's F3. The check asserts the PAUSE; that it falls at the run's end follows from p0 = 0 and a cadence
    of 160 reads against 24.
11. Applied in T1's item 3. A run of record writes the stage's own root and report; a smoke writes where `--root` and
    `--report` name, outside the repository.
12. Item 33's, applied with it.

## 2. The edits after the check, checked by tool

- **The diffs.** `diff -U0` of each final text against its checked draft holds only the dispositions above, and Code
  read each diff in full.
  - T1 has 14 hunks:
    - items 33 and 42;
    - item 36 with observation 3, in one hunk;
    - item 43 with observation 5, in one hunk;
    - observations 1, 4, 6, 8, 9 and 11, with the coordinating session's sentence (below) in observation 9's hunk;
    - two placeholders filled: the ADDENDUM-n2 commit, and this check's departures and lines;
    - two in "Committed by path": the close line on ADDENDUM-n2's entry named, and the commit-time count stated.
  - T2, T3 and T4: T2 has 1 hunk (observation 2), T3 has 1 (observation 7), and T4 has 3 (items 87 and 90, and
    observation 10).
- **The quotes.** Every quote in T1 and T2 is found, joined across wrapped lines, in its source: 19 of 19. The sources
  are the seat's answers, v2f, and the coordinating session's and n-analyzer's words as filed in Code's scratch. This
  raw's own quotes are found in theirs, 8 of 8.
- **A text written after the check.** n-build's close line on ADDENDUM-n2's entry was written once the addendum's
  commit, `7a54eb9`, landed. The blind pass did not read it. It was checked by tool:
  - its one quotation, "the pin moving as before" (§6.3 (3)), is found in the addendum;
  - the addendum's sha256 at `7a54eb9` is `41f76c49…bb3f`;
  - the commit is in HEAD's history.
- **A sentence added after the check,** at the coordinating session's request, to T1's "Why (b)": v2f is the driver
  the committed texts at `7a54eb9` and `f3e7190` call v2e. It was checked by tool against four mentions of v2e in
  ADDENDUM-n2's "What runs now", three in the pod session's close line on `6df2131`'s entry, and v2d following v2c in
  the delta review's raw at `ad856f0`.
- **The finals:**
  - T1, the entry, sha256 `77bca3ea…0ab0`, 113 lines;
  - T2, `ea884060…ef89`, 27 lines;
  - the close line on ADDENDUM-n2's entry, `27910920…ffab`, 12 lines;
  - T3, `e5c82685…944a`, 35 lines;
  - the review raw (T4 with the report), `284fafe4…8369`, 273 lines.
- **The commit's gate** re-runs these checks on the staged blobs. It also checks:
  - the package digest;
  - the driver's numstat;
  - that `RESULTS.md` is HEAD's with the entry and the close line alone;
  - the ADDENDUM-n2 commit's bytes of the addendum;
  - the commit-time count of the home-folder prefix, as a count.

## 3. The report as returned

```text
BLIND VALUES-CHECK: T1 entry.md, T2 close.md, T3 selftest_raw.txt, T4 review_head.md

The hashes of all four texts match the brief, recomputed with shasum. HEAD is 3b2b855. Every repository source I read is equal to its HEAD blob (git hash-object compared with git rev-parse HEAD:path).

The result: 1 FAIL (T1:53, the n-analyzer attribution), 5 IMPRECISE, 10 NOT CHECKABLE and 79 CONFIRMED, over 95 items. There are 12 observations. My departures, all model-free and read-only, are listed in DEPARTURES at the end.

ITEMS

1. T1:1–4. Headline: v2f committed by path before the resume, §1.4's distribution printed whole, backend-ext-2 wired to ADDENDUM-n2 §4.1, third sitting §1.4. CONFIRMED. Evidence: v2f :594–634 and :881–1016; answers :20; ADDENDUM-n2 :34.
2. T1:2–3. "the coordinating session's choice (b), declared for the seat to strike". CONFIRMED by c1 ("The choice is Code's (mine). Declare it … for the seat to strike"). The letter (b) appears in no source, but T1–T4 use it consistently.
3. T1:4. "Nothing in the read path changes". CONFIRMED. In the HEAD-to-v2f diff the first stage keeps label_ids=cands[conv] with conv = "bare" (v2f :898, :992). Its label_convention is "bare" (v2f :583). The runner and primitive are unchanged.
4. T1:4, :7. "the n package is unchanged at f927608c…3c03". CONFIRMED. git log ad856f0..HEAD -- valence_core is empty, and the last commit touching valence_core/n is b523f6a. The digest is package_sha256 over valence_core/n/*.py (guard.py:40–41). The same value is in run3_out step 3 and the v2d raw.
5. T1:6. v2f `e29839c8…1152`. CONFIRMED by shasum.
6. T1:6–7. "on ad856f0's scripts/n_sessions.py (18f19b8e…4f5c), which no commit since has changed". CONFIRMED. The shasum of HEAD and of ad856f0:path both equal 18f19b8e…4f5c, and git log ad856f0..HEAD on the path is empty.
7. T1:7. numstat +421 −45. CONFIRMED by git diff --no-index --numstat (421 45).
8. T1:8. 378/378 for v2f, and 356/356 for v2e before the review. CONFIRMED by selftest_run2.txt and selftest_run1.txt. The review brief (:29) already cites 356/356.
9. T1:9, :13. The raw names. NOT CHECKABLE: neither file exists yet. ls shows no name collision in results/raw.
10. T1:9–10. "The box runs it at the resume's step 3". NOT CHECKABLE: no source holds the resume's box script.
11. T1:11. Review of v2e (43a01b36…090d): 0 BUG, 7 RISK, 3 NIT, 12 mutants, 10 observations. CONFIRMED. review_returned.md has F1–F7 RISK, F8–F10 NIT, M1–M12 and O1–O10, and :5 says "no BUG". The brief's TO hash is v2e's.
12. T1:12. Every finding is applied in v2f, and every mutant has a killing test. CONFIRMED: the v2e-to-v2f delta carries F1–F10 and tests for M1–M12 (items 73–83).
13. T1:14. Nothing of v2e or v2f ran on a checkpoint's weights. NOT CHECKABLE. It is consistent with the only runs named, the model-free laptop self-tests.
14. T1:15–16. The c1 quote, and "v2f is v2e with the review's fixes". CONFIRMED: c1 is verbatim, and every hunk of the delta is a disposition.
15. T1:17–19. The §1.4 quote. CONFIRMED verbatim (answers :20).
16. T1:17, :19–20. "§1.4 names the quartiles and the min. The committed driver printed the absdiff's min, median, p90 and max, and the rel's median and max." CONFIRMED by HEAD driver :583–585, where the key is "margin".
17. T1:21–22. The absdiff's per-read values are printed nowhere else, and the rel's are in the fid lines to six decimals. CONFIRMED. runner.py :484–486 prints only rel with :.6f (run3_out read lines). The diagnostic output prints only summaries.
18. T1:23–24. The committed driver fixes the stage's name, root and report and the convention "bare". CONFIRMED by HEAD :395–403, :554 and :892.
19. T1:25–26. Option (a)'s launch files were drafted, frozen and not relayed. NOT CHECKABLE.
20. T1:28–30. The distribution line: absdiff and rel, each as min, q1, median, q3 and max (numpy linear); p90 beside; label's median and max, the max being R3's bound; the TAU and TAU/4 counts; the reads and finite counts. CONFIRMED by v2f :594–625 and :1013. The self-test's key check is at :1146–1149.
21. T1:30–31. The key "margin" becomes "absdiff", the seat's word. CONFIRMED: HEAD :583 against v2f :614, and §1.4 says "absdiff in nats".
22. T1:31–33. The prefix quote, and backend-ext-2 has no bound clause. CONFIRMED by v2f :631–634 and :1004.
23. T1:34. A STAGE line before the weights, naming the stage, its convention, root and report. CONFIRMED by v2f :932–933.
24. T1:35–38. `backend-ext-2 --convention NAME`, and the c2 quote. CONFIRMED: the command is in v2f main :1710–1750, and c2 is verbatim apart from list markup.
25. T1:39–40. The stage writes data/n/ckpt/backend-ext-2/ and data/n/reports/backend-ext-2.json, and prints the distribution alone on COMPLETE. CONFIRMED by v2f :429–431, :913–914 and :1008–1009.
26. T1:41. It refuses "bare" and any non-candidate. CONFIRMED by v2f :894–897; the self-test cases are at :1544–1548.
27. T1:42–45. The first-stage check (on disk, valid, COMPLETE, 24 of 24 planned and obtained, "bare", identity equal but for the convention, cells hashing to their record) and the printed sha256. CONFIRMED by v2f :796–827 and :961–965. It runs before G-VER and the load (:974, :981).
28. T1:46. A smoke is not checked against the first stage. CONFIRMED by v2f :961.
29. T1:47. --convention is taken only by backend-ext-2, which requires it. CONFIRMED by v2f :1735–1742.
30. T1:49–50. R7: the stage stays "backend-ext" and only label_convention differs. CONFIRMED by v2f :571–591; the self-test check is at :1402–1409.
31. T1:50–51. STAGES is ("campaign", "time", "backend-ext"), and only backend-ext may carry a null lock, dose map and bound. CONFIRMED by schema.py:239 and :815–818 ("is null exactly at backend-ext").
32. T1:51–53. A new stage moves the digest; the resume needs the digest its report was written under; "backend-ext-2" names the root, report and command. CONFIRMED by guard.py:40–41, prior_state at v2f :784–786, and v2f :429–431 with main's choices.
33. T1:53. "n-analyzer was told: backend-ext-2 never reaches its reader." FAIL. a1 is n-analyzer's own words, not something it was told; T4:89–90 attributes it correctly. Replace with: n-analyzer, told of R7: "backend-ext-2 never reaches the reader, so R7 needs nothing from me: load_campaign and verdicts refuse any identity whose stage is not "campaign"."
34. T1:54–55. R8. CONFIRMED by v2f docstring :100–102.
35. T1:57. "the resume from this commit, in a fresh sparse copy at it". CONFIRMED by c3.
36. T1:57–59. "…byte copies of the run copy's stage report, cell file and 31 capture arrays, … each compared by `cmp`, with the report and cell at their committed sha256s, and no listing (the answers' §7)". IMPRECISE. The count 31 is right: 6df2131's commit message says "31 capture arrays", and the capture layers are 33–63. But c3 says "checked by digest", not cmp (see observation 3). Replace with: The stage root and report are byte-copied into it from the run copy (the report, the cell file and the 31 capture arrays, taken by name from the committed record) and checked by digest without a listing, the report and the cell at their committed sha256s (the answers' §7: "a listing over a copied ckpt or report is pruned or not run").
37. T1:59–60. The run copy stays untouched as the run of record's copy. CONFIRMED by c3.
38. T1:61. The outputs are read in full. CONFIRMED by c2.
39. T1:62–63. backend-ext-2 only on exactly one other candidate; none for "bare"; none or several is a STOP. CONFIRMED by c2.
40. T1:64. The schema follow-up comes after both and is settled with n-analyzer. CONFIRMED by answers §3 (:28) and ADDENDUM-n2 §6.3(3) (:48).
41. T1:64–66. The three field names, and p0 entered as (k + 1, n + 2), "agreed so far". NOT CHECKABLE. No source holds the names; a2 says only "my draft already uses your names and order". The p0 form is consistent with ADDENDUM-n2 §1.1 and the schema's p0_count/p0_n.
42. T1:66. "the kind's place directly after non-finite is Code's reading". IMPRECISE. ADDENDUM-n2 §2.1 (:24) already puts the kind "after `non-finite` in the precedence"; only "directly" is Code's. Replace with: the kind's place: after non-finite, as ADDENDUM-n2 §2.1 has it; directly after it, ahead of identity-bound in schema.PAUSE_KINDS' order, is Code's reading, for the seat. (PAUSE_KINDS is at schema.py:1085.)
43. T1:68–71. Code's departure. IMPRECISE. c4 says "non-Python, model-free and read-only", and T1 drops "non-Python". The loop detail is not in c4 and is NOT CHECKABLE. Logging it for Q-F3 is confirmed by c4. Replace with: …held a guard marker in its argv, in a loop checking the first resume draft's manifest against `ad856f0`'s blobs. It was non-Python, model-free and read-only, and touched nothing under `data/mf3`, `data/*/ckpt` or `data/*/reports`. The coordinating session logged it for Q-F3's run list;
44. T1:72–73. The reviewer's departures. CONFIRMED by review_returned.md :140–146.
45. T1:76–80. The list of files committed by path. NOT CHECKABLE until the commit is made. It is consistent with T2–T4.
46. T1:80, :82. The close line goes on 6df2131's entry, and the next step is the launch files to the coordinating session. CONFIRMED. RESULTS.md :157–213 has no close line yet, and c2/c3 make the coordinating session the relay.
47. T2:1. Close-line header and PI date. CONFIRMED: the answers' header says "PI date 2026-11-18 (third sitting)", and the form matches RESULTS.md:596.
48. T2:1–6. "read … in full". NOT CHECKABLE.
49. T2:3–5. The two paths and `d51279ec…0bf4` and `e2b1c77a…2a8a`. CONFIRMED by shasum. The files are 14,167 B and 2,515 B.
50. T2:6. Committed both by path at 3b2b855. CONFIRMED: git show --name-only 3b2b855 lists exactly those two.
51. T2:6–7. "Route as given", as relayed. CONFIRMED by c6 and 3b2b855's subject.
52. T2:8–10. Q1 quotes, the ruling raw as the file, and what the resume prints. CONFIRMED by answers :7 (§0) and :20 (§1.4).
53. T2:11–12. Q2 quote and the fresh pair's cost. CONFIRMED by answers :8 and :24.
54. T2:13–14. ADDENDUM-n2 (§3): p0, C, the second row, figures of record, backend-ext-2 if not "bare". CONFIRMED by answers :28.
55. T2:15–17. The push ruled (§4) with the push the PI's word; Code's find and the checker's departures inert (§7). CONFIRMED by answers :32 and :48–49.
56. T2:18–25. This session's order. CONFIRMED by c1–c3, ADDENDUM-n2 §6.3(3) and (5), and answers §3.
57. T3:1–3. Header, citations and PI date. CONFIRMED; the form matches the v2d raw.
58. T3:5–7. The driver's full sha256, and the package unchanged since b523f6a with the full digest. CONFIRMED: the digest is identical in the v2d raw and run3_out.
59. T3:9–10. The HF cases and the HF-path vanilla score are skipped and counted where torch and transformers are absent ("the driver's docstring"). CONFIRMED by v2f :6–9, _bext_selftest's docstring :1035, the code at :1273–1286, and hftiny.available at hftiny.py:27–33.
60. T3:11–15. HEAD 3b2b855; every named path present at HEAD; the exclusion form is item 3's plus mf3's. CONFIRMED with git rev-parse and git ls-files on quoted globs. The self-test reads the characterization's artifact and raw (v2f CHARACTERIZED_*).
61. T3:11–16. That the overlay was built this way, that no ckpt or report file entered it, "cmp-equal", and "package digest, measured in it". NOT CHECKABLE.
62. T3:17–20. The command. NOT CHECKABLE; its form matches the v2d raw.
63. T3:22–25. Run 1: v2e's full sha256, the output's sha256 383b54e1…1e, the output text, and the c5 window. CONFIRMED. "exit 0" and "re-hashed just before" are not observable, though exit 0 is the docstring's contract for all-pass (v2f :6–7).
64. T3:27–30. Run 2: v2f's sha256, the output's sha256 6d67d967…a2, the text, and the second c5 window. CONFIRMED, with the same note as item 63.
65. T3:32–33. The box plan. NOT CHECKABLE.
66. T4:1, :3. Title and header. CONFIRMED; the form matches 2026-11-18_n-step4-driver-v2_review.md.
67. T4:6. FROM 18f19b8e…4f5c, committed at ad856f0 and unchanged since. CONFIRMED.
68. T4:7–8. TO 43a01b36…090d, and what it does. CONFIRMED.
69. T4:10–19. The brief's contents. CONFIRMED by review_brief_final.md :5–65. Its items 1–5 are byte-identical to the list ruling raw (results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md :18–22): both hash to sha256 2373155c…c185.
70. T4:21–22. 152 lines, `8192136c…6f2a`, and "names no local path". CONFIRMED by wc -l, shasum and a full read. "by `jq`" is NOT CHECKABLE.
71. T4:24. Totals 0/7/3/12/10. CONFIRMED.
72. T4:28. V2F e29839c8…1152 is V2E +219 −47, every line a disposition. CONFIRMED: the numstat is 219 47, and every hunk maps to F1–F10 or O6.
73. T4:29–32. F1. CONFIRMED by v2f :1329–1342 and :1696–1698.
74. T4:33–40. F2. CONFIRMED by v2f :1674–1695, :1019–1022 and main.
75. T4:41–47. F3. CONFIRMED by v2f :1430–1452. Token 9 is the space S label's second token ([6, 9, 17] at :1294 and :1405).
76. T4:48–50. F4. CONFIRMED by v2f :1481–1492.
77. T4:51–58. F5, including the seven identity fields and the 23/24 and 24/25 cases. CONFIRMED by v2f :1494–1523, :1558–1580 and :813–822.
78. T4:59–61. F6. CONFIRMED by v2f :1164–1167.
79. T4:62–65. F7: the cached path is made non-finite. CONFIRMED by v2f :1453–1480; primitive.py:219 is prefill (the cached path) and :238–239 is full (the fresh path).
80. T4:66–69. F8: label values 0.1/0.2/0.3/0.4 give a median of 0.25. CONFIRMED by v2f :1130–1133 and :1153–1156.
81. T4:70–77. F9 (a)–(d). CONFIRMED by v2f :44–48, :75–114 and :796–800.
82. T4:78–80. F10. CONFIRMED by v2f :628–634 and :929–931.
83. T4:82–83. The mutant-to-test map. CONFIRMED. "not run" is NOT CHECKABLE.
84. T4:86–87. O1. CONFIRMED by git log and guard.py.
85. T4:88–90. O2. CONFIRMED: a1 paraphrased correctly, and v2f :579.
86. T4:91–92. O3's .gitignore and .gitattributes facts. CONFIRMED. .gitignore :289–294 admits only backend-ext. git check-ignore puts backend-ext-2's cell and report under /data/n/ckpt/* and /data/n/reports/*. git check-attr gives the backend-ext-2 cell "diff: unset".
87. T4:92. "The seat's §4 clearance names backend-ext's cell only." IMPRECISE. §4 (:32) names the cell and the report, and words the halt's clearance over `data/n/ckpt/**`. Replace with: The seat's §4 names backend-ext's cell and report as what is pushed, and words the screen's clearance over `data/n/ckpt/**`; whether it reaches backend-ext-2's cell and report is for the seat.
88. T4:93–94. O4. CONFIRMED by v2f :804–806.
89. T4:95–96. O5. CONFIRMED.
90. T4:97–98. O6, "Taken, as above". IMPRECISE. The reviewer's O6 had three parts (review_returned.md :118–121). v2f takes the cell hash, and prints the sha256 on its own line rather than on the STAGE line (:963). It does not take the ruling-sha check (:796–827). Replace with: **O6.** Taken in part, as above: the first stage's cells are hashed against its report's record, and its report's sha256 is printed on a line of its own before G-VER (not on the STAGE line), since the report is rewritten at each resume. The check of p01's ruling sha256 is not taken.
91. T4:99–100. O7. CONFIRMED by the v2f dict keys and ADDENDUM-n2 §4.1 and §2.1.
92. T4:101–102. O8. CONFIRMED.
93. T4:103. O9. CONFIRMED.
94. T4:104–105. O10. CONFIRMED by v2f :966–973, which come before G-VER.
95. T4:107–111. The reviewer's departures and "(the seat classed the same act inert at `6df2131`, the answers' §7)". CONFIRMED by answers :49.

TOTALS: CONFIRMED 79, IMPRECISE 5 (items 36, 42, 43, 87, 90), FAIL 1 (item 33), NOT CHECKABLE 10 (items 9, 10, 13, 19, 41, 45, 48, 61, 62, 65). 95 items, 12 observations.

OBSERVATIONS

1. T1:62–63 does not carry c2's "in the same box session on the same characterized backend" or the relay ("send me … and I relay them"). ADDENDUM-n2 §4.1 also says "in the same session", and CLAUDE.md bars splicing a campaign across backends.
2. T2 omits two §1.4 rulings that bear on n-build: "Code's R3 … is accepted as a printed measurement; the lock's bound is ADDENDUM-n2's C", and "The extension's entry carries the pause, the ruling's sha256 and the figures". The precedent close line (RESULTS.md:608–610) carried the seat's word on Code's declared items.
3. On item 36: list-of-record item 2 lets data/*/ckpt files be read only by the stage's own code, G-VER, the analyzer and the pre-push screen. Item 1 permits digests that print no byte, size or time. cmp is in neither, and on a mismatch it prints a byte offset. c3's "checked by digest" is item 1's form. If the launch files keep cmp, it needs the coordinating session's word.
4. T1 R8 and item 1: the coordinating session's line, as the brief quotes it (review_brief_final.md:20–21: "exactly §1.4's list … Keeping p90 is fine if you declare it"), licensed p90 alone. label.median and the two counts are declared in R8 too. The entry could say they go beyond that line, so the seat can strike them.
5. T1:68: "for one call," repeats "one … call".
6. T1 "What changes" item 3 omits backend-ext-2's own lines: its PAUSE line (v2f :997), its SMOKE line without floor sessions (:930–931), its non-finite wording (:1006), and the first-stage line's form (:963–965). T4 covers them.
7. T3:32–33 could give the box figure as arithmetic. The v2d raw explains the box's +11 checks, so if the HF cases are unchanged, v2f gives 389/389 at the box.
8. Neither T1 nor T3 says whether another laptop process ran beside the two self-test windows. bfc869f's entry (RESULTS.md:152–153) states Q-F3's campaign ran beside its runs.
9. c3 calls the resume's commit "v2e's commit", while T1 says "this commit" and T2 "v2f's commit". It is the same commit; this is harmless, but a relay following c3's words may look for "v2e".
10. T4 F3's "at the run's end" comes from the check's label, not its assertions. It holds by reasoning (p0 = 0, cadence 160 > 24, identity_bound null).
11. T1:39's root and report hold for a run of record; a smoke writes where --root and --report name, outside the repository (v2f :900–914).
12. T1:53 and T4:89–90 currently give n-analyzer's word two ways. Applying item 33 aligns them.

DEPARTURES (model-free, read-only, no interpreter, no write, no network, no guard marker in any argv, nothing under data/mf3 listed or read)

(a) Two git log commands without item 3's pathspec and the mf3 exclusion: `git log --format='%h %s' ad856f0..HEAD` and `git log -1 --format='%H %s'`. They printed ids and subjects only.
(b) `git check-attr diff --` and `git check-ignore -v --no-index` on named paths under data/n/ckpt and data/n/reports: backend-ext-2's cell and report (neither on disk), plus backend-ext's committed cell for check-ignore. They were run without item 3's pathspec and printed only attributes, ignore rules and the names I gave; no content, size or time. check-ignore is not in item 1's list and may lstat a named path internally.
(c) `git rev-parse --verify -q HEAD:<path>` on named data paths (data/n, data/corpus/e0_tasks.jsonl, data/corpus/e2a_tasks.jsonl, data/configs/e0_frames.json, data/configs/e0_probes.json), and `git ls-files` on two quoted globs 'data/ol*/…', without item 3's pathspec. These paths are outside ckpt, reports and mf3. The output was present/absent and two names, with the folder masked.
(d) Borderline: a `git diff --no-index` between the two named drafts, piped to `/usr/bin/grep -n -e '^@@'` for hunk headers. This was a grep over the diff's output, not over any folder in S.
```
