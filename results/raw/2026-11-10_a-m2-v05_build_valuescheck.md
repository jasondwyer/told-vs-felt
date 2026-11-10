# ADDENDUM-m2 v0.5's build — the values-check, one blind pass

*Code's raw, PI date 2026-11-10.*
- *What was checked:* the drafts of the BUILD entry (all of it), the review raw's header and both rounds' dispositions, and the header lines of the battery, self-test and site-check raws.
- *How:* one blind agent, read-only, under a brief quoting the list of record v2's items 1–5 as written.
  - By its report, the main checkout's HEAD was `ba89279` when it started and `585df45` when it ended. The commits between are the pod session's p chain, and none touches a file the drafts cite.
  - The brief allowed `scripts/mf3_sessions.py hashes`. The checker did not run it, because the command also digests `data/mf3/schedules/manifest.json` and the brief's own working limit said to open nothing under `data/`. It recomputed the same digests another way. That limit was the brief's, wider than the list's item 2, which covers `ckpt` and `reports` only; nothing to rule.
- *Outcome:* 131 items: 109 CONFIRMED, 10 IMPRECISE, 0 FAIL, 12 NOT CHECKABLE. Each IMPRECISE item is applied (below). No second pass was run: none was a FAIL, and each fix is either the checker's own wording or a citation it checked.
- *This raw:* Code's dispositions, then the report verbatim (extracted by script from the agent's hand-back; it holds no local path).
- *Nothing ran on a model.*

## Code's dispositions

- **8, IMPRECISE: "before v0.4's commit", though v0.4 was never committed.** Agreed. Applied: "before the addendum's commit (v0.4's, then pending; v0.4 was never committed)".
- **19, IMPRECISE: the driver's sha256 and blob attributed to the `hashes` output, which does not hold them.** Agreed. Applied: the package and the m files cite `hashes` (the site-check raw); the driver cites `shasum -a 256` and `git hash-object`.
- **30, IMPRECISE: the "no integer cap" refusal placed under `require_real`.** Agreed: it is in the stub branch, which re-computes the cap from the prior's checkpoint. Applied in the entry. The code is not changed.
- **47, IMPRECISE: `m_analyze.py:11035` cited for "runs at 60".** Agreed. Applied: the group at `:11035`, its stub chain's 60 at `:10722`.
- **58 and 80, IMPRECISE: round 2's grade for finding 11 is NOT RESOLVED (deferred), not "recorded".** Agreed. Applied in the entry and the review raw's header.
- **63 and 91, IMPRECISE: "the review's alternative" was one bullet of round 1's fix.** Agreed. Applied: "round 1's further proposed fix, which round 2 judged unneeded".
- **67, IMPRECISE: "the driver's self-test, unchanged since `acde2d8`".** Agreed: only its `tree_state` is unchanged; the build edits the self-test. Applied.
- **86, IMPRECISE: "each reports … before and after its time cases".** Agreed. Applied: "hashes every file … and prints only the comparison (round 1: sha256, before and after the run)".
- **NOT CHECKABLE 71: "the four raws".** Applied: five, with this raw.
- **NOT CHECKABLE 12, 45, 46, 116 and 118:** Code's own stamps and its record of the background command (the start and end times, exit 0, the first bytes). They are stated as Code's in the raws' headers. Nothing to apply.
- **NOT CHECKABLE 3, 53, 69, 73, 82 and 84:** placeholders, a prediction, the commit's own state, and process claims. Nothing to apply.
- **After this check:** the main checkout's HEAD moved to `585df45`. Code moved the worktree onto it, edits carried byte for byte, and re-ran the site check there before the commit (the BUILD entry).

## The checker's report (verbatim)

**Values-check report: the A-m2 v0.5 BUILD drafts** (blind; read-only)

- **Main checkout HEAD:** `ba89279` at start, `585df45` at end. Another session committed `585df45` while I worked. It changes only LOCK-p-OLMo-{sft,dpo,instruct}.md, RESULTS.md and a p values-check raw, none of which these drafts cite.
- **Brief:** sha256 `562fdab77155fd6c…`, 37 lines, as expected.
- **Worktree W:** HEAD `7589c1d`, with exactly 11 files modified and uncommitted.

**How I checked, and one departure from the brief's wording.** I did not run `scripts/mf3_sessions.py hashes` as the brief says. That command also opens `data/mf3/schedules/manifest.json` to digest it (mf3_sessions.py:166–168), and the brief's working limit says to open nothing under `data/`. Instead I recomputed the same digests another way:
- the package hash, with a stdlib replica of `m_resume.package_sha256_of` (valence_core/m/resume.py:328–350) over W/valence_core/mf3/*.py;
- the eleven m files, with `shasum`;
- the driver, with `shasum` and `git hash-object` (no `-w`).

No claim depends on the manifest or WEIGHTS lines.

Besides the named drafts, I read only these files in S:
- the two review briefs, for the claim that each quotes items 1–5;
- Code's extracted report copies and the unscrubbed outputs (`battery_v05_1.txt`, `selftest_v05_5.txt`, `sitecheck_v05_1.txt`), for "nothing else changed";
- file modification times, for timing corroboration.

I read none of Code's other analyses.

---

### A. `entry_build.md` (L = line in the draft)

1. L1 title and scope: CONFIRMED. v0.5 §4.2 (ADDENDUM:73); W's diff is the 10 mf3 modules plus the driver; ruling (a) is at ans5:7, 13.
2. L2 "525/525 on the unchanged analyzer": CONFIRMED. The battery raw has 525 PASS, 0 FAIL and ends "525/525". The analyzer blob `84979ad5` is the same at HEAD, `7589c1d` and in W (sha256 `d347ea0c…`).
3. L3 @@STAMP@@: NOT CHECKABLE (placeholder).
4. L4 "A5 (verbatim in the close line at `0516832`)": CONFIRMED. That commit's RESULTS.md close line carries "The PI's routing of 2026-11-10, section A, verbatim", A1–A5.
5. L4–6 the quote: CONFIRMED. It is an exact substring of A5, character for character.
6. L6 "v0.5 §6 item 4 gives the same order": CONFIRMED (ADDENDUM:93, which adds the self-tests and values-check).
7. L7 sources (`ans5:` §6; STOP Q6): CONFIRMED (ans5:41; STOP:159–171).
8. L8 "started … before v0.4's commit": IMPRECISE.
   - The phrase is the STOP's own (STOP:27, :162), but v0.4 was never committed (ADDENDUM:3 says "untracked"; ans5:29 says "v0.4 was never committed").
   - Fix: "before the addendum's commit (v0.4's, then pending; v0.4 was never committed; v0.5 was, at `7589c1d`)".
9. L8–9 declaration at 2026-11-10T03:26:42Z: CONFIRMED against STOP:162, ADDENDUM:93 and ans5:41. The time itself comes from Code's transcript (v0.4 values-check :43).
10. L9 "accepted on the p step-3 precedent, the rule standing": CONFIRMED (ans5:41, ans5:54).
11. L10 "The text committed first: v0.5 at `7589c1d`": CONFIRMED (`git show --name-status 7589c1d`).
12. L10 "resumed after that commit (Code's stamp, 07:27:55 UTC)": NOT CHECKABLE.
    - 07:27:55 appears in no committed text (`git grep` at HEAD with `':!data/**'`).
    - It is consistent with the commit time, 02:27:09 −0500 = 07:27:09 UTC.
13. L11 "Nothing of the build was committed before this entry": CONFIRMED. `git log 7589c1d..HEAD -- valence_core/mf3 scripts/mf3_sessions.py` is empty at both HEADs.
14. L11 "no gate or stage of record ran before `7589c1d`": CONFIRMED. Of the commits from `50fea90` to `7589c1d`, none is an F3 gate or stage; STOP:170 says the same.
15. L11–12 "156/160 … not of record": CONFIRMED (STOP:169; ans5:41).
16. L13–15 the files that move, "v0.5 §4.2's list, and only they": CONFIRMED. `git -C W diff --name-status` gives exactly these 10 plus the driver, matching ADDENDUM:73.
17. L16–17 `--smoke` retired and the wiring restored to `acde2d8`'s bytes: CONFIRMED.
    - "smoke" appears only in the retirement note (mf3_sessions.py:43–44).
    - `git diff acde2d8 -- scripts/mf3_sessions.py` shows only the build's edits.
18. L18 `valence_core/m/` and `m_analyze.py` (`d347ea0c…`) not edited: CONFIRMED. W's diff over them is empty; the analyzer's sha256 is `d347ea0c9b69…`.
19. L19 and L76 cite "the hashes" as the `hashes` output in the site-check raw: IMPRECISE.
    - That output (sitecheck:1971–1987) has the package and the eleven m files.
    - It does not have the driver's sha256 or blob. `1b593ba0` and `9d54d25f` appear in none of the four raws.
    - Fix: attribute the driver's two values to `shasum -a 256` / `git hash-object` on the final bytes.
20. L20 package `098455d9…dda13`, 15 files: CONFIRMED (my recomputation is identical; sitecheck:1973).
21. L20–21 "It was `f30ad505…` (LOCK-m-F3.md:96)": CONFIRMED. LOCK:96 says so, and recomputing from `7589c1d`'s blobs gives `f30ad5053904…` over 15 files.
22. L22 driver sha256 `1b593ba0…87c6`: CONFIRMED (`shasum` on W's driver).
23. L22 git blob `9d54d25f…`: CONFIRMED (`git -C W hash-object`).
24. L22–23 "the DRIVER line's new value": CONFIRMED. The DRIVER line prints the sha256 of the committed blob's bytes (mf3_sessions.py:377–380, :511).
25. L24 the eleven m files unchanged: CONFIRMED. All 11 match LOCK-m-F3.md:106–116 and sitecheck:1974–1984.
26. L26 `CAP_OF_RECORD`, 120: CONFIRMED (scaffold.py:55).
27. L27 `_extra` refuses any other cap on a non-stub run: CONFIRMED (stages.py:624).
28. L28 `Identity` admits 60 only on `STUB_WEIGHTS`: CONFIRMED (resume.py:50, :196–201).
29. L29–30 `prior_gate` with `require_real` fixes 120, refuses a prior at another cap, and is declared as a PIN: CONFIRMED (stages.py:493–505).
30. L30 "…and refuses a prior identity with no integer cap" (placed under `require_real`): IMPRECISE.
    - The dedicated refusal, "PRIOR STAGE MALFORMED", is in the `require_real`-off (stub) branch (stages.py:506–509). That is where round 2's residual 8 lay ("reachable only through a stub prior", review:285).
    - On a run on a model, a prior with no cap is refused as "AT ANOTHER CAP" (stages.py:502–505), and a non-int value equal to 120 would pass that test.
    - Fix: "…with `require_real` off (the stub path) it recomputes the cap from the prior's checkpoint and refuses a prior identity with no integer cap".
31. L31 the driver validates `time` as a run on a model: CONFIRMED (mf3_sessions.py:106, :286).
32. L33–34 `STAGE_REASONING_CAPS` holds m:174's pair at every stage: CONFIRMED (scaffold.py:61, :149–151; PROPOSAL-m:174 gives 60 → 120).
33. L35–36 `cap_trigger`: CONFIRMED. `cap` is a required keyword; 120 fixes 120; 60 is fixed by the count (stages.py:1030, :1048).
34. L37 `REASONING_CAPS` unchanged: CONFIRMED. Only the comment at scaffold.py:52 changed.
35. L39 the checkpoint is `Q-F3_time-r2.json`, with report and reads named after it: CONFIRMED (mf3_sessions.py:107, :299–306, :532–534; stages.py:114–117, :976).
36. L40–41 the precheck refuses an existing or ENDED checkpoint, and the first-run name, a link included: CONFIRMED (mf3_sessions.py:303–305, :337–345, :1225–1228, :1257).
37. L42 the stage library keeps m's stem: CONFIRMED (stages.py:100–111).
38. L44 F-b's bytes come from banner's constants, with m's header by import: CONFIRMED (banner.py:60–61, :130–137).
39. L45 pinned at `f27505c5…5354` and checked with §4.2's stub sentence: CONFIRMED (banner.py:64, :73; the file's sha256 matches).
40. L45–47 where the check runs: CONFIRMED.
    - It runs at every start, the stub's included, on the working tree's bytes (stages.py:194, via `_begin` :717, called at :978, :1251 and :1468).
    - The licence's (h) requires the file committed on non-stub starts (:383–386; `_licence` returns on the stub at :402).
    - G-SHAPE-F3 checks it too.
41. L48–49 one builder and ws-normalized equality: CONFIRMED.
    - The builder is lines.py:49, used by runner.py:172 and verify.py:129.
    - The read rule reaches it through `counter_a_of_record`.
    - The match is lines.py:136–140.
42. L50 counters per §3.4, with its blinding scope: CONFIRMED (lines.py:182–251; readrule `line_counts`; stages.py:1143–1152).
43. L51 "(A5; v0.5 §4.3), before the review rounds": CONFIRMED (ADDENDUM:75). Timing corroborates: the battery output was last written 07:45:40 UTC and the round-1 report copy 08:25:20.
44. L52–53 525/525 in the worktree, and the raw's name: CONFIRMED.
45. L52 "exit 0": NOT CHECKABLE. The cited raw records no exit status. It is consistent with m_analyze.py:11301, and the site check's second run shows "(exit 0)".
46. L52 "07:42:55–07:45:40 UTC": NOT CHECKABLE from the raw's body; only its header carries the times. The unscrubbed output's modification time, 07:45:40 UTC, corroborates the end.
47. L54 "reader group, whose stub chain runs at 60 (`m_analyze.py:11035`), passes": IMPRECISE.
    - The group passes (battery:481–486).
    - But :11035 registers the group; the 60 is at :10722, in `_bt_f3_chain` (:10713).
    - Fix: "The Q-F3 reader group (`:11035`), whose stub chain runs at 60 (`:10722`), passes", as ADDENDUM:73 anchors it.
48. L54–55 no analyzer edit, so no STOP: CONFIRMED.
49. L56 525/525 again in the site check: CONFIRMED (sitecheck:1768).
50. L57 180/182: CONFIRMED (self-test raw: 180 PASS, 2 FAIL; line 191).
51. L58–59 the two red checks are finding 11, each failing on one problem: CONFIRMED.
    - Raw:162 prints the single problem, naming `098455d91d1ae323…`.
    - Raw:161 is printed truncated, but its only conjunct that can fail is "nothing for (f)" (mf3_sessions.py:733–736).
    - Review:94–96 and :301–307 agree.
52. L60 the re-issue comes after this commit: CONFIRMED (ADDENDUM:75; explicitly at :93).
53. L60 "They pass at the re-issue … Code re-runs the self-test there": NOT CHECKABLE. It is a prediction and a plan, and it holds only under review:101–102's conditions.
54. L61 "202, less 42, plus 22": CONFIRMED, exact.
    - The baseline is 202/202, with 42 "mf3_sessions smoke" checks that are absent in the build.
    - The build adds 22 checks (5 new, 17 net from rewritten checks), and no non-smoke check was removed.
    - No mf3 change lies between `9eed029` and `7589c1d`.
55. L62 two blind rounds: CONFIRMED.
56. L63 round 1: 11 findings, 0/3/8: CONFIRMED (review:249).
57. L64–67 the three MAJORs and their fixes: CONFIRMED (review:108–139; lines.py:225, :245, :210–220; readrule.py:632–646).
58. L68 "Round 2 found … 11 recorded": IMPRECISE.
    - Round 2 graded finding 11 "NOT RESOLVED (deferred to the BUILD entry, as the author declared)" (review:288, :352).
    - Findings 1–10 resolved, 3 new MINOR, and "applied" are all correct.
    - Fix: "11 NOT RESOLVED by design (deferred to this entry; its single-problem failure verified)".
59. L69–73 the ten suites and their counts: CONFIRMED (sitecheck:162, :232, :257, :281, :333, :354, :391, :1240, :1768, :1959).
60. L74–75 the G-SHAPE-F3 trial figures: CONFIRMED (sitecheck:1960–1970).
61. L77 "none moves a form, a bar, a key or the cap": CONFIRMED in substance.
62. L78 Code's `qwen_ends` reading: CONFIRMED (PIN at lines.py:202–209; :217).
63. L78–79 "the review's alternative, which would touch ruling (h)'s report form": IMPRECISE.
    - Round 1 gave the stage-written domain as one bullet of its fix (review:128–132). Round 2 calls it "Round 1's other bullet … not needed" (review:296).
    - The ruling-(h) point is a fair reading: ruling (h) is committed, and G-TIME-F3's contrast keys are fixed.
    - Fix: "round 1's further proposed fix (the stage writing (b)'s domain), which round 2 judged unneeded".
64. L80 Code's reading of F6: CONFIRMED (stages.py:493–505).
65. L81–82 the five PINs revised in place: CONFIRMED (review:341–348; e.g. `_extra`'s docstring PIN, declared at v0.1, now carries v0.5 text).
66. L83 "the list's item 8": CONFIRMED (list ruling:25).
67. L83–85 "the driver's self-test, unchanged since `acde2d8`, sha256-hashes…": IMPRECISE.
    - `tree_state` (mf3_sessions.py:672–678) is identical to `acde2d8`'s (:643–649).
    - The self-test itself is not unchanged: this build edits it, including that very check (:1427–1434, loader reaches 4 → 5).
    - The scope, the before/after timing (:687–688, :1427) and the printout (`(5, 1, [], [])`) are as stated.
    - Fix: "the driver's self-test, whose `tree_state` is unchanged since `acde2d8`, …".
68. L85 Code reads it as item 1's digest form: CONFIRMED (stated as a reading).
69. L86 @@VC@@: NOT CHECKABLE (placeholder).
70. L87–88 Next (re-runs, then the lock's re-issue, then the G-TIME-F3 re-run, announced): CONFIRMED (A5; ADDENDUM:93).
71. L89 "the four raws": NOT CHECKABLE yet. Four raws are named now, but by precedent the values-check raw is committed with the entry (`7589c1d` and `50fea90` each added one, and `7589c1d`'s entry lists it). If @@VC@@ is filled that way, the count is five.
72. L89 "Nothing ran on a model": CONFIRMED. Every invocation in the raws is a model-free self-test, the gshape trial or `hashes`.
73. L89 "Not pushed": NOT CHECKABLE (a state at commit time).

### B. Review raw: header (L1–17) and dispositions (L19–74)

74. L3 PI date: CONFIRMED.
75. L4 W at `7589c1d` with 11 named files: CONFIRMED (both reports say so; W's diff confirms).
76. L5 two blind, read-only agents, each brief quoting items 1–5 as written: CONFIRMED. Both briefs contain ruling lines 18–22 verbatim; both reports say they wrote nothing.
77. L6 round 1's scope: CONFIRMED (brief_review_v05.md:24–25).
78. L7 round 2's task: CONFIRMED (review:274–333).
79. L9 round 1: 11 findings, 0/3/8: CONFIRMED (review:249).
80. L10 round 2: "finding 11 recorded by design, and verified": IMPRECISE. The grade is NOT RESOLVED (review:288, :352); use the same fix as item 58.
81. L11 every finding applied, or recorded (11): CONFIRMED. Every fix, the residuals included, is present in W (items 89–110).
82. L11 "each re-checked at source": NOT CHECKABLE (a process claim).
83. L12 180/182 after round 2's fixes: CONFIRMED. The raw includes N2's and N3's checks, and all 182 check names exist in W's code.
84. L13 "verbatim, extracted by script from each agent's hand-back": NOT CHECKABLE (the hand-backs are not among the sources). Corroborated: the round-1 section equals review1_report.md byte for byte; round 2's equals review2_report.md with its one local root replaced by `<scratch>`.
85. L14 "each reports no departure": CONFIRMED (review:361; round 1's compliance section names none).
86. L15 "Each reports … sha256-hashes … before and after its time cases": IMPRECISE.
    - Round 1 says sha256, "before and after the run" (review:255). Round 2 says "hashes", with no timing (review:360).
    - "Time cases" is true of the code but is in neither report.
    - Fix: "Each reports that `tree_state` hashes every file under W's `data/mf3` … and prints only the comparison (round 1: sha256, before and after the run)".
87. L16 Code's reading, disclosed under item 8: CONFIRMED (review:57–59).
88. L17 nothing ran on a model: CONFIRMED.
89. D1: CONFIRMED (lines.py:225, :236–245; self-test :444–451).
90. D2, the core of the disposition: CONFIRMED (lines.py:202–220; self-test :452–470).
91. D2, "the reviewer's alternative" (L28–29): IMPRECISE (same point as item 63).
92. D3: CONFIRMED (readrule.py:632–646). It uses the COMMON line where the reviewer suggested the banner, and it states what was applied.
93. D4: CONFIRMED (mf3_sessions.py:91).
94. D5: CONFIRMED (lines.py:263–266).
95. D6: CONFIRMED (scaffold.py:180–183).
96. D7: CONFIRMED (stages.py:181–196, :383–386; sitecheck:1768).
97. D8: CONFIRMED (stages.py:1030).
98. D9: CONFIRMED (testing.py:110, :139; runner.py:260, :274–279).
99. D10: CONFIRMED. The refused table requires exit 2 and an unchanged root (mf3_sessions.py:1257, :1296–1302); the first-run-beside case passes with `rf["same"]` (:1365–1372).
100. D11: CONFIRMED (review:94–96, :180–181).
101. The re-issue note: CONFIRMED (review:101–104).
102. The compliance note: CONFIRMED (review:255; `tree_state` is unchanged).
103. Round 2, findings 1–10 RESOLVED: CONFIRMED.
104. Residual 3: CONFIRMED. The old conjunct is gone; the fixed-count check is readrule.py:640–646.
105. Residual 4: CONFIRMED (mf3_sessions.py:91–94).
106. Residual 8: CONFIRMED (stages.py:506–510, the stub branch).
107. Finding 11, recorded and verified: CONFIRMED (review:301–307).
108. N1: CONFIRMED (banner.py:55–59).
109. N2: CONFIRMED (stages.py:2076–2088).
110. N3: CONFIRMED. It covers 3 contrast sessions plus 1 excluded at its second forced round (readrule.py:661–671).
111. Notes on the PINs revised in place: CONFIRMED (review:341–348).
112. Note that the G-SHAPE-F3 artifact is write-once (lock:97): CONFIRMED (LOCK-m-F3.md:97; review:349).
113. L74 180/182: CONFIRMED.

### C. The raws' header lines

114. Battery header: "(A5; v0.5 §4.3; ans5 §1)" and "before the review rounds": CONFIRMED (ans5:14).
115. Battery header: `m_analyze.py --selftest` from W at `7589c1d`: CONFIRMED (INVOCATION line).
116. Battery header: "the build's first bytes (before the review's fixes)": NOT CHECKABLE. Nothing in the body identifies the mf3 bytes. Timing corroborates (07:45:40 UTC against 08:25:20).
117. Battery header: analyzer unchanged, `d347ea0c…`, HEAD's: CONFIRMED.
118. Battery header: stamps 07:42:55–07:45:40: NOT CHECKABLE from the body; the end time is corroborated by the output file's modification time.
119. Battery header: "No model": CONFIRMED.
120. Battery header: scrub, "nothing else changed": CONFIRMED. One line differs from the unscrubbed output (the path is replaced by `<repo>`), and no local path remains.
121. Self-test header: "of record on the final bytes", W plus the build: CONFIRMED. The FAIL line names `098455d9…`, and the output equals the site check's run.
122. Self-test header: 180/182; the FAILs are finding 11; they read the committed lock's pre-build hash until the re-issue: CONFIRMED.
123. Self-test header: "No model": CONFIRMED.
124. Self-test header: scrub: CONFIRMED. 6 lines differ, all path replacements, two of them truncated temp-path fragments (raw:135, :174).
125. Site-check header: "the final bytes (the self-test raw's)": CONFIRMED.
126. Site-check header: W plus the build, with the jlens venv: CONFIRMED.
127. Site-check header: "the ten model-free suites of the F3 build's site check": CONFIRMED. 2026-11-06_mf3-build_sitecheck.txt has the same ten.
128. Site-check header: the battery among them, on the final bytes: CONFIRMED.
129. Site-check header: G-SHAPE-F3 trial (never of record) and the hashes: CONFIRMED.
130. Site-check header: "No model and no pod": CONFIRMED.
131. Site-check header: scrub: CONFIRMED.
    - 62 lines differ, all path replacements (3 of them truncated temp fragments: :1209, :1903, :1942).
    - The original's modification time, 09:04:26 UTC, equals the raw's end stamp.
    - `<home>` occurs in none of the three raws; this is harmless.

### Tally

131 items: **109 CONFIRMED, 10 IMPRECISE, 0 FAIL, 12 NOT CHECKABLE.**

### Everything not CONFIRMED

- **IMPRECISE (10):**
  - 8: "before v0.4's commit", though v0.4 was never committed.
  - 19: the `hashes` output and site-check raw are cited for the driver's sha256 and blob, which they don't contain (entry L19/L76).
  - 30: the "no integer cap" refusal is placed under `require_real`; it is in the stub branch.
  - 47: `m_analyze.py:11035` is cited for "runs at 60"; the 60 is at :10722.
  - 58 and 80: round 2's grade for finding 11 is NOT RESOLVED (deferred), not "recorded".
  - 63 and 91: "the review's/reviewer's alternative" was one bullet of round 1's fix.
  - 67: "the driver's self-test, unchanged since `acde2d8`"; only `tree_state` is unchanged.
  - 86: "Each reports … before and after its time cases"; the two reports say different things, and neither says that.
- **NOT CHECKABLE (12):**
  - 3, 69: the two placeholders.
  - 12: the 07:27:55 stamp.
  - 45: the battery's "exit 0".
  - 46, 118: the battery's times.
  - 53: "they pass at the re-issue; Code re-runs".
  - 71: "the four raws" will be five if a values-check raw is committed, as precedent suggests.
  - 73: "Not pushed".
  - 82: "each re-checked at source".
  - 84: "extracted by script from each agent's hand-back".
  - 116: "the build's first bytes".

No draft states a rule or precedent that no committed record holds. The ruling-(a) description matches W's code except for item 30.

**Compliance under list of record v2.** I opened, read, listed, sized and traversed nothing under `data/` in W or the main checkout. Every content search carried `':!data/**'`; I used no recursive grep and no `--stat`, `--numstat` or `--shortstat` form. I made no git writes, wrote no files and ran no model. The one deviation from the brief is the `hashes` substitution described at the top. Nothing printed from `data/`.
