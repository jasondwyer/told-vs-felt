# Blind values-check of the three PROPOSAL-m OLMo-{ckpt} -- NOT-RUN entries (draft) and their record files -- the checker's report verbatim, its scratch-folder names normalised to <scratch>/, then Code's dispositions. PI-local date 2026-11-06.

# Blind values-check: the three NOT-RUN draft entries and their record inputs

**What was checked:** the three entries in `<scratch>/<scratch>/notrun_entries_draft.md` (the @@STAMP@@ and @@VC@@ placeholders were skipped) and the content of the three record input files, `data/m/verdicts/OLMo-{sft,dpo,instruct}_not-run-record.json`.

**How:** read-only, against repo HEAD `e0b4f2c730aa…` (the tree is unchanged: the same 36 untracked entries and no tracked edits before and after). I did not run `scripts/m_analyze.py` or import it. Every number was recomputed with my own scripts (`python3 -I -B`, in `<scratch>/vc_notrun/`):
- the sha256 of every file;
- the m package hash, re-implemented from `resume.package_sha256_of` and run over both the tree and the HEAD blobs;
- the misses by item from the checkpoints and, separately, from the read raw at `6ce8b9a`;
- a check that all 384 texts in §5 match the checkpoint records exactly;
- the condition-(4) arithmetic as exact fractions;
- the routing quote, byte for byte;
- the three NOT-RUN outputs, rebuilt from the records by re-implementing `validate_not_run_record` and `run_not_run`'s document. All three rebuilds are byte-identical to the written files.

Line citations for RESULTS.md are at HEAD `e0b4f2c` unless a commit is given.

**Totals: 139 items.** 128 CONFIRMED · 6 CONFIRMED-BY-RELAY-ONLY · 1 NOT CHECKABLE · **4 IMPRECISE** · **0 FAIL**.

---

## The FAIL and IMPRECISE items

There is no FAIL.

- **#7, IMPRECISE (wording).** Draft line 2 says "The record was written through the analyzer's not-run path".
  - The not-run path writes the **output**, `OLMo-sft_NOT-RUN.json`. It only reads and validates the **record**: `m_analyze.py:2571–2575`, and the output's `record` field is the input file's path and sha256.
  - The record input was written by Code, and this same entry calls the input file "The record" a few lines later (draft line 19).
  - The seat's §1 does use "records" in the first sense ("Code writes the three records now … each through the analyzer's not-run path"), but inside this entry the word now means two things.
  - Suggested fix: "The NOT-RUN output was written through the analyzer's not-run path" (or "The record went through …").
- **#30, IMPRECISE (a citation carried over from the seat).** Draft lines 22–23 say "`date` `2026-11-06` (C7's convention, the calendar date of the grader's verdict)". The seat's §1 says the same ("C7's convention: the calendar date of the terminal event, the grader's verdict"), but at its source C7 is a different rule:
  - C7 is the UTC boundary-day rule for the Clock: `results/raw/2026-10-10_m-design-to-code_pre-LOCK-v0.1.md:79`, "committer date, in UTC … ends at 23:59:59 UTC". It is cited the same way at RESULTS.md@18c32df:819 ("the Clock is UTC by R1 C7") and in the step-17 raw `results/raw/2026-10-19_m-design-to-code_step17.md:31` ("the boundary day is C7's — D_O inclusive to 23:59:59 UTC").
  - "The calendar date of the terminal event" is C5's meaning: the same file at `:73`, PIN-43 at `m_analyze.py:511–514`, and `LOCK-m-F0.md:2258`, "as that unit's entry records it".
  - On C7's UTC terms, the grader's verdicts fall on **2026-11-07**: the runs were 02:20:02Z–02:35:53Z UTC on that day (`results/raw/2026-11-06_gcal-olmo.txt:24–29`).
  - On C5's terms, the date is the G-CAL-OLMo entry's, 2026-11-06 (RESULTS.md:216).
  - So the value is right, and matches the seat's §1 as written. The convention named for it is not the one that gives it.
  - Suggested fix: cite C5 / PIN-43, or quote the seat's phrase as the seat's. The record file carries no convention citation, so it is unaffected.
- **#113, IMPRECISE.** Draft line 72 says "The three outputs are the NOT-RUN coordinates the v1 posting needs".
  - A coordinate is the unit's state value in the posting's tuple input (`m_analyze.py:2861–2868`; PIN-23 at `:4693`).
  - The outputs are what PIN-23's cross-check requires *beside* a NOT-RUN coordinate (`crosscheck_coordinate`, `:2660–2686`).
  - The seat's words are "The three outputs are also inputs the v1 posting cannot run without" (answers :9).
  - The parenthetical quote after it is exact (#114).
- **#129, IMPRECISE (minor; this is in the record files, so in the outputs too).** Each record's `detail` cites "(RESULTS.md, the G-CAL-OLMo entry, 6ce8b9a)" for its run window, pod and backend identifier.
  - The entry gives the pod (RESULTS.md:239), the backend identifier (:254) and only the **overall** window "02:20:02Z → 02:35:53Z" (:246).
  - The per-checkpoint boundaries in the records (02:25:14Z, 02:30:37Z) come from the run raw `results/raw/2026-11-06_gcal-olmo.txt:24–29`. That raw was committed in `6ce8b9a` and is linked from the entry.
  - The values are correct.
  - The `detail` string is copied verbatim into the three written NOT-RUN outputs, which are write-once (PIN-37) but still untracked. Changing the record means regenerating the outputs before the commit. Disclosing it instead is the other option.

## Observations (not verdicts; for the author to weigh or route)

- **O1. Decision (16)'s date (items #42 and #133, both CONFIRMED as written).** The record dates it 2026-11-06, which follows the seat's rule ("dated as its commit entry is") and the commit entry's header (RESULTS.md:1141, "- 2026-11-06 — **ADDENDUM-m1 v0.1 COMMITTED (routed by the PI, PI date 2026-11-05)"). Other parts of the record disagree:
  - The PI's routing that adopted (16) is dated "PI date 2026-11-05 (I confirm the date)" (RESULTS.md:1162).
  - Code's list in that entry reads "The date is 2026-11-05, confirmed. (16) is adopted." (:1192).
  - The analyzer at HEAD has `ADDENDUM_M1_DATE = "2026-11-05"`, commented "A-m1's commit day (f26bc59; the PI's routing date)" (`m_analyze.py:141`).
  - The entry's 2026-11-06 is f26bc59's committer date in UTC (2026-11-05 21:10:55 −0500 = 2026-11-06T02:10:55Z).
  - If the seat meant the date the decision was taken, the value would be 2026-11-05. That is the seat's call; the draft states its basis accurately.
- **O2. The routing block and the answers file.** The relayed routing block names neither the answers file nor its sha256, unlike the morning's routing (RESULTS.md@54bbfe5:233–235). The link between the block and `2026-11-06_gcal-olmo_design-to-code_answers.md` rests on its items matching the seat's §6 items 1–3 one for one, which they do (answers :33–35).
- **O3. Beside the scope.** The run raw `results/raw/2026-11-06_m-olmo-not-run.txt` was also checked. Its §1 equals the scratch capture `<scratch>/notrun_run.txt` with the local paths replaced by `<repo>`. Its §2 equals `<scratch>/notrun_misses.txt` and my own recomputation. Its header shas are all correct.

---

## Part A: the draft text

### Entry 1 (OLMo-sft): header

1. **CONFIRMED-BY-RELAY-ONLY.** Entry date 2026-11-06.
   - Source: routing item 1, "Date: [2026-11-06]".
   - Consistent with the run stamps 2026-11-07T04:51:13Z–04:51:14Z (23:51 −0500 on 2026-11-06; raw :15–23).
2. **CONFIRMED.** Title form "PROPOSAL-m OLMo-sft — NOT-RUN".
   - Sources: m:358 step 17 ("`PROPOSAL-m <unit> — NOT-RUN`"); answers :9; p :130 ("`PROPOSAL-m OLMo-{ckpt} — NOT-RUN` (×3, m's)").
3. **CONFIRMED.** "m:358 step 17".
   - m:358 holds steps 5–18. Step 17's last clause is the NOT-RUN record rule.
4. **CONFIRMED.** "m:176, m:302, m:324".
   - m:176: "G-CAL-OLMo: … failure → that checkpoint NOT-RUN with reason "dose not completable"".
   - m:302: "failure → NOT-RUN "dose not completable"".
   - m:324: "(OLMo) its G-CAL-OLMo failed condition (4) ("dose not completable"; …)".
5. **CONFIRMED.** Reason "dose not completable".
   - Sources: m:176/302/324; `NOT_RUN_CAUSES["dose-not-completable"]["phrase"]` (`m_analyze.py:449–450`); output `reason`.
6. **CONFIRMED.** "at G-CAL-OLMo-sft's condition (4) of 2026-11-06".
   - The artifact's `condition_4.verdict` is FAIL. The G-CAL-OLMo entry header is dated 2026-11-06 (RESULTS.md:216).
7. **IMPRECISE.** "The record was written through the analyzer's not-run path". See the section above.
8. **CONFIRMED-BY-RELAY-ONLY.** "on the PI's routing of the seat's G-CAL-OLMo answers".
   - Routing item 1 "The three m NOT-RUN records: [go]" answers the seat's §6 item 1 (answers :33).

### Entry 1: the routing

9. **CONFIRMED-BY-RELAY-ONLY.** The three-line quote is verbatim.
   - Byte comparison against the relayed text: identical, 416 bytes, including both "§" characters (`diff` empty).
10. **CONFIRMED-BY-RELAY-ONLY.** "(chat, the parent thread, relayed by the routing session)".
11. **CONFIRMED.** "The seat's answers it routes".
    - Every bracketed choice in the block matches an option the seat's §6 offers (answers :33–35): letter p, the frame-word rule as written, D_p 2026-12-15, the 12 h budget, G-CAL-p first, the §5 posting rule and its two sentences, the pod staying up. See O2.
12. **CONFIRMED.** "committed with this entry, as placed: `results/raw/2026-11-06_gcal-olmo_design-to-code_answers.md`".
    - The file is at that path, untracked. The commit is pending.
13. **CONFIRMED.** sha256 `4c3f57d4ec4c1404026bceb2dc2f07141ef36e3d1af66705a5f383dff148bf82`. The full hash matches (`shasum -a 256`).
14. **CONFIRMED.** "Its §1 gives the three records' content".
    - Answers :9 gives schema, cause, also, date, detail and decisions.
15. **CONFIRMED.** "PROPOSAL-p v0.1's §8 step 1 repeats it" (p :122).
    - Note: step 1 restates schema, cause, `also`, date and detail. It gives the decisions only by reference ("as the seat's answers §1 list them"), and its detail line omits the word "covariate".
16. **CONFIRMED.** PROPOSAL-p sha256 `1821a235…9953`. Full: `1821a23521cf…f692069953`.
17. **CONFIRMED.** "stays untracked until its §8 step 3".
    - `git status` shows `??`. p :124 reads "Commit `PROPOSAL-p v0.1 — COMMITTED`: this file tracked at root".
18. **CONFIRMED.** "Items 2 and 3 are not these entries' work". p :122: "m's step first, independent of p".
19. **NOT CHECKABLE.** "Another session reads PROPOSAL-p".
    - Routing item 2 routes p for Code's pre-read. No available source says which session does it.
20. **CONFIRMED-BY-RELAY-ONLY.** "the pod stays up". Routing item 3: "[stays up]".
21. **CONFIRMED (forward-looking).** "nothing runs on it until the PI's go for G-CAL-p (p §8 step 5)".
    - p :126: "G-CAL-p, per checkpoint, on the PI's go for the box".
    - Routing item 2: "order on the pod [G-CAL-p first, …]".
    - Answers :29: "Nothing else runs on the box until the PI's word on p".

### Entry 1: the record

22. **CONFIRMED.** Path `data/m/verdicts/OLMo-sft_not-run-record.json`. The file exists.
23. **CONFIRMED.** sha256 `a30df61c…1be7`.
    - Full: `a30df61c01d5…472701be7`. It equals the output's `record.sha256` and raw :5.
24. **CONFIRMED.** Schema `m-not-run-v1`. Record field; `NOT_RUN_RECORD_SCHEMA` at `m_analyze.py:147`.
25. **CONFIRMED.** "validated by `m_analyze.validate_not_run_record` before the run".
    - `run_not_run` calls it (`m_analyze.py:2573`) before anything is written, and the run exited 0.
    - My re-implementation of all its checks passes for all three records: exactly seven keys, schema, unit, cause, an ISO date, `also` as a list, `detail` as a string, and each decision's four keys, ISO date, other unit and Q5 state.
    - A separate pre-run invocation is attested only by the raw's header line 4.
26. **CONFIRMED.** `cause` `dose-not-completable`. Matches answers :9 and p :122.
27. **CONFIRMED.** `also` `[]`. Matches answers :9 and p :122.
28. **CONFIRMED.** "no Clock cause: D_O′ = 2026-11-30 has not passed".
    - D_O′ is 2026-11-30 (ADDENDUM-m1 :28; `D_O_PRIME` at `m_analyze.py:139`). 2026-11-06 is before it.
    - Answers :9: "no Clock cause holds: D_O′ has not passed".
29. **CONFIRMED.** `date` `2026-11-06`. Matches answers :9 and p :122.
30. **IMPRECISE.** "(C7's convention, the calendar date of the grader's verdict)". See the section above.
31. **CONFIRMED.** "so `date_is_clock_of_record` is false".
    - Output field `false`. `m_analyze.py:2644` compares the date with `clock_of_record`, which is D_O′ for OLMo units (`:548–556`).
32. **CONFIRMED.** Clean 62/64. Artifact `accuracy.CORR_clean.hits` = 62; RESULTS.md:250; my recount from the checkpoint.
33. **CONFIRMED.** Corrupted 42/64. Artifact hits = 42; RESULTS.md:250; recount.
34. **CONFIRMED.** "against 7/10". m:176 ("≥ .70 absolute"); artifact `abs_bar` "7/10".
35. **CONFIRMED.** "¾ × clean = 93/128". Exact: 3/4 × 31/32 = 93/128. Artifact `rel_bar` "93/128".
36. **CONFIRMED.** Covariate +5/16. 31/32 − 21/32 = 5/16; artifact covariate `fraction` "5/16".
37. **CONFIRMED.** The detail carries the artifact's and the checkpoint's sha256.
    - `799b3c3f…7617` and `1f16f732…2b72` equal both the files and the blobs at `6ce8b9a`.
38. **CONFIRMED.** The detail carries "the run": window, pod and backend identifier (items #127–#128).
39. **CONFIRMED.** The detail carries the pointer to the full read (#130).
40. **CONFIRMED.** "`decisions_with_other_outcomes_known` (PIN-35)". PIN-35 is at `m_analyze.py:657–664`; answers :9.
41. **CONFIRMED.** "both with `other_unit` Q-F0 and `other_state` PASS (m:318)".
    - Both decisions carry these values. `Q-F0_VERDICTS.json` has `tuple.Q-F0` "PASS" and `arm.state` "PASS".
    - m:318's last sentence is the recording rule.
42. **CONFIRMED.** "ADDENDUM-m1's decision (16), dated 2026-11-06 as its commit entry is".
    - The entry header at RESULTS.md:1141 is 2026-11-06, and answers :9 says "dated as its commit entry is". See O1.
43. **CONFIRMED.** "the PI's go for this G-CAL run, 2026-11-06".
    - RESULTS.md@54bbfe5:233 "PI date 2026-11-06"; :237 "Go for G-CAL-OLMo on sft, dpo and instruct, smoke first."
44. **CONFIRMED.** "The file name is Code's". Answers :9 gives only "--record PATH"; p :122 gives "--record …".
45. **CONFIRMED.** "in Q-F0's input style (`{U}_decisions.json`, `{U}_olmo-states.json`)".
    - `data/m/verdicts/Q-F0_decisions.json` and `Q-F0_olmo-states.json` exist.
46. **CONFIRMED.** "inside the repo so the output records its path relative to the root".
    - `_file_rec` and `_repo_rel` (`m_analyze.py:1974–1975`, `:1849–1853`) return the repo-relative path. The output records `data/m/verdicts/OLMo-sft_not-run-record.json`.

### Entry 1: the output

47. **CONFIRMED.** Command `scripts/m_analyze.py not-run --unit OLMo-sft --record …`. Raw :3 and :16.
48. **CONFIRMED.** "(no `--time` / `--qual`: no gate-stage checkpoint exists)".
    - `data/m/ckpt/` holds only `G-CAL_olmo-*` for OLMo, in the tree and at HEAD. Answers :9 says the same.
49. **CONFIRMED.** "at HEAD `e0b4f2c`". Raw :2 and :14 give `e0b4f2c730aa…`. Current HEAD is the same.
50. **CONFIRMED.** "G-ANL-F3's extended analyzer". The e0b4f2c subject: "G-ANL-F3 -- BUILD … scripts/m_analyze.py extended in place".
51. **CONFIRMED.** Analyzer sha256 `6ec3222b…93d9`.
    - It matches the file, the blob at `e0b4f2c`, the output's `analyzer_sha256`, and RESULTS.md:57.
52. **CONFIRMED.** Package `60199b36…feec`.
    - Independently recomputed over `valence_core/m/*.py` (18 files), on the tree and on the HEAD blobs.
    - It matches the output's `package_sha256` and RESULTS.md:58.
53. **CONFIRMED.** "identical to HEAD".
    - `git log -1 -- scripts/m_analyze.py` gives e0b4f2c. `git diff e0b4f2c -- scripts/m_analyze.py` is empty, and `git status` on `scripts/` and `valence_core/` is empty.
54. **CONFIRMED.** Exit 0. Raw :18.
55. **CONFIRMED.** Output path `data/m/verdicts/OLMo-sft_NOT-RUN.json`. The file exists.
56. **CONFIRMED.** Output sha256 `72745cb4…b5b0`. Raw :9 agrees, and my independent rebuild is byte-identical.
57. **CONFIRMED.** State NOT-RUN. Output `state`.
58. **CONFIRMED.** Reason "dose not completable". Output `reason`.
59. **CONFIRMED.** Row "concluded, not answered — the told control at this stage was not run: dose not completable".
    - Exact string match with `rows["olmo-sft"]`, including the em dash.
60. **CONFIRMED.** Raw link `results/raw/2026-11-06_m-olmo-not-run.txt`. Exists, untracked, commit pending.

### Entry 1: the full read

61. **CONFIRMED.** "its 128 generations". 128 checkpoint records and 128 generation lines in the block.
62. **CONFIRMED.** The m:358 quote "carrying the full read of those sessions and their contrast picks". Exact substring of m:358.
63. **CONFIRMED.** "G-CAL has no picks".
    - Answers :9: "G-CAL has no picks to release". The checkpoint records have no pick field: their keys are cap_hit, hit, i, n_tok, pool, seed, seed_index, stop_reason, task and text.
64. **CONFIRMED.** "m:318 exception (4) admits the read for a unit with no verdict left to bias".
    - m:318 (4): "… the reads a NOT-RUN record or a PENDING closure performs under §3, for a unit with no verdict left to bias".
65. **CONFIRMED.** "Every text is in [`_gcal-olmo_read`] §5, block OLMo-sft (lines 62–222 at `6ce8b9a`)".
    - The header is at line 62 and the last generation at 222.
    - All 384 texts in §5 equal the checkpoint texts, token counts and stop reasons exactly.
    - The HEAD copy is byte-identical to the `6ce8b9a` blob.
66. **CONFIRMED.** "Code read them all at the G-CAL-OLMo entry". RESULTS.md:269: "Code read all 384 generations".
67. **CONFIRMED.** Clean misses 2: item 2 seed 3 and item 4 seed 0. Checkpoint recount, read §5 recount, and raw :30 agree.
68. **CONFIRMED.** Corrupted misses 22, by item: 1 (2), 2 (4), 4 (1), 5 (2), 7 (1), 8 (1), 9 (3), 11 (3), 13 (2), 14 (1), 15 (2).
    - Both recounts and raw :31 agree; the counts sum to 22.
69. **CONFIRMED.** R1 A6 (i) = 3. RESULTS.md:265; read raw §2 (3 do not state the answer).
70. **CONFIRMED.** (ii) = 0. RESULTS.md:265; read raw §2 and §6.
71. **CONFIRMED.** (iii) = 0. RESULTS.md:265; G-CAL run raw :171.
72. **CONFIRMED.** (iv) = 12 (9 graded hits). RESULTS.md:265; G-CAL run raw :172.

### Entry 2 (OLMo-dpo)

73. **CONFIRMED.** Header: date, title, the m:358/176/302/324 citations, the reason, "condition (4) of 2026-11-06", and "through the analyzer's not-run path". Same sources as #1–#6.
74. **CONFIRMED.** Record path `data/m/verdicts/OLMo-dpo_not-run-record.json`.
75. **CONFIRMED.** Record sha256 `4ed8576b…fde8`. Full: `…bb088cfde8`. It equals the output's `record.sha256` and raw :6.
76. **CONFIRMED.** "the same form as OLMo-sft's". Same keys, schema, cause, `also` and date. Passes the re-implemented validator.
77. **CONFIRMED.** Clean 61/64. Artifact; RESULTS.md:251; recount.
78. **CONFIRMED.** Corrupted 44/64. Artifact (11/16); RESULTS.md:251; recount.
79. **CONFIRMED.** "against 7/10 and ¾ × clean = 183/256". 3/4 × 61/64 = 183/256; artifact `rel_bar`.
80. **CONFIRMED.** Covariate +17/64. 61/64 − 44/64; artifact.
81. **CONFIRMED.** "The decisions are the same two". The decision lists are identical across the three records (same canonical hash).
82. **CONFIRMED.** Output path `data/m/verdicts/OLMo-dpo_NOT-RUN.json`.
83. **CONFIRMED.** Output sha256 `94869b83…8e96`. Raw :10 agrees; the rebuild is byte-identical.
84. **CONFIRMED.** Exit 0. Raw :22.
85. **CONFIRMED.** "the same analyzer, HEAD and row". Same `analyzer_sha256`; HEAD e0b4f2c (raw :14); `rows["olmo-dpo"]` has the same label text.
86. **CONFIRMED.** "its 128 generations: … block OLMo-dpo (lines 223–383 at `6ce8b9a`)". Header at 223, last generation at 383, 128 generations.
87. **CONFIRMED.** Clean misses 3: item 7 seed 1, item 10 seed 2, item 13 seed 0. Both recounts and raw :33.
88. **CONFIRMED.** Corrupted misses 20, by item: 1 (1), 2 (4), 5 (1), 8 (2), 9 (3), 11 (3), 13 (1), 14 (2), 15 (3). Both recounts and raw :34; the counts sum to 20.
89. **CONFIRMED.** (i) = 4. RESULTS.md:266; read raw §2.
90. **CONFIRMED.** (ii) = 0. RESULTS.md:266.
91. **CONFIRMED.** (iii) = 0. RESULTS.md:266; G-CAL run raw :316.
92. **CONFIRMED.** (iv) = 6 (4). RESULTS.md:266; G-CAL run raw :317.

### Entry 3 (OLMo-instruct)

93. **CONFIRMED.** Header, as #73.
94. **CONFIRMED.** Record path `data/m/verdicts/OLMo-instruct_not-run-record.json`.
95. **CONFIRMED.** Record sha256 `e633b2ac…c829`. It equals the output's `record.sha256` and raw :7.
96. **CONFIRMED.** "the same form". As #76.
97. **CONFIRMED.** Clean 59/64. Artifact; RESULTS.md:252; recount.
98. **CONFIRMED.** Corrupted 42/64. Artifact (21/32); RESULTS.md:252; recount.
99. **CONFIRMED.** "against 7/10 and ¾ × clean = 177/256". 3/4 × 59/64 = 177/256; artifact `rel_bar`.
100. **CONFIRMED.** Covariate +17/64. 59/64 − 42/64; artifact.
101. **CONFIRMED.** "The decisions are the same two". As #81.
102. **CONFIRMED.** Output path `data/m/verdicts/OLMo-instruct_NOT-RUN.json`.
103. **CONFIRMED.** Output sha256 `e2ecef56…87e8`. Raw :11 agrees; the rebuild is byte-identical.
104. **CONFIRMED.** Exit 0. Raw :26.
105. **CONFIRMED.** "the same analyzer, HEAD and row". As #85.
106. **CONFIRMED.** "its 128 generations: … block OLMo-instruct (lines 384–544 at `6ce8b9a`)". Header at 384, last generation at 544; line 545 is blank and §6 starts at 546.
107. **CONFIRMED.** Clean misses 5: item 2 seed 0, item 7 seed 1, item 10 seeds 0 and 2, item 13 seed 0. Both recounts and raw :36.
108. **CONFIRMED.** Corrupted misses 22, by item: 1 (1), 2 (4), 5 (1), 7 (2), 8 (2), 9 (4), 11 (3), 14 (2), 15 (3). Both recounts and raw :37; the counts sum to 22.
109. **CONFIRMED.** (i) = 2. RESULTS.md:267; read raw §2.
110. **CONFIRMED.** (ii) = 0. RESULTS.md:267.
111. **CONFIRMED.** (iii) = 0. RESULTS.md:267; G-CAL run raw :461.
112. **CONFIRMED.** (iv) = 9 (5). RESULTS.md:267; G-CAL run raw :462.

### "For all three"

113. **IMPRECISE.** "The three outputs are the NOT-RUN coordinates the v1 posting needs". See the section above.
114. **CONFIRMED.** "(the seat's §1: PIN-23's cross-check accepts a NOT-RUN coordinate only beside a NOT-RUN output of the same reason)".
    - Exact substring of answers :9. The code is `crosscheck_coordinate` (`m_analyze.py:2660–2686`); PIN-23's text is at `:4693`.
115. **CONFIRMED.** "The A-m1 §2.4 (b) status sentence is the PI's at the posting".
    - ADDENDUM-m1 :42 ("one sentence, the PI's words"); answers :9 ("the PI's words at the posting").
116. **CONFIRMED.** "Nothing ran on the box".
    - Raw :1 says "Laptop; nothing on the box.", and the invocations use laptop paths (scratch capture `notrun_run.txt`).
117. **CONFIRMED-BY-RELAY-ONLY.** "the pod stays up (routing item 3)".
118. **CONFIRMED (state now).** "Nothing is pushed".
    - `origin/main` is `273ca8f`, HEAD is 7 commits ahead, and the new files are untracked.

## Part B: the three record input files' content

119. **CONFIRMED.** Each record has exactly `also, cause, date, decisions_with_other_outcomes_known, detail, schema, unit`, with schema `m-not-run-v1` and a `unit` that matches its file name.
    - Source: `validate_not_run_record`'s key list (`m_analyze.py:634–637`).
120. **CONFIRMED.** `cause` `dose-not-completable`, `also` `[]` and `date` `2026-11-06` in all three. Matches answers :9 and p :122 as written.
121. **CONFIRMED.** The detail opens "G-CAL-OLMo-{ckpt} (m:176, m:302): condition (4) FAIL at the dose of record."
    - Artifact `condition_4.verdict` FAIL; answers :7 ("at the dose of record").
122. **CONFIRMED.** Pool figures: sft "Clean pool 62/64 (31/32); corrupted pool 42/64 (21/32)", dpo "61/64; … 44/64 (11/16)", instruct "59/64; … 42/64 (21/32)".
    - Artifact `accuracy` fractions; exact reductions.
123. **CONFIRMED.** "corrupted >= 7/10: no" and "corrupted >= 3/4 x clean (93/128 | 183/256 | 177/256): no".
    - Artifact `abs_pass` and `rel_pass` are false; the exact-fraction check agrees.
124. **CONFIRMED.** "covariate (clean minus corrupted, f0's sign) +5/16 | +17/64 | +17/64".
    - Artifact `covariate.definition` and `fraction`; m:176 ("f0's sign").
125. **CONFIRMED.** The artifact paths and sha256s: `799b3c3f…7617`, `ed89aaf5…ca08` and `62ed6d03…35c1` match the files and the blobs at `6ce8b9a`.
126. **CONFIRMED.** The checkpoint paths and sha256s: `1f16f732…2b72`, `239f6bd6…e8c2` and `724897d7…58a6` match the files and the blobs at `6ce8b9a`.
127. **CONFIRMED.** Run windows: sft 02:20:02Z–02:25:14Z, dpo 02:25:14Z–02:30:37Z and instruct 02:30:37Z–02:35:53Z, all on 2026-11-07. Source: `results/raw/2026-11-06_gcal-olmo.txt:24–29`.
128. **CONFIRMED.** Pod `qny1x4v8padeke` and backend identifier `641ee466f4553b6a`.
    - Artifact `provenance[0].pod_id` and `identity.backend_identifier`; RESULTS.md:239 and :254.
129. **IMPRECISE.** The detail's citation "(RESULTS.md, the G-CAL-OLMo entry, 6ce8b9a)" for those run facts. See the section above.
130. **CONFIRMED.** "The full read of its 128 generations: results/raw/2026-11-06_gcal-olmo_read.txt section 5, block OLMo-{ckpt} (lines 62-222 | 223-383 | 384-544 at 6ce8b9a)". As #65, #86 and #106.
131. **CONFIRMED.** "G-CAL has no picks to release." Answers :9, word for word.
132. **CONFIRMED.** The decision (16) text: "the three OLMo units re-registered once, under a new Clock date D_O' = 2026-11-30 (ADDENDUM-m1 v0.1, committed at f26bc59)".
    - ADDENDUM-m1 :24 ("may be re-registered once") and :28 (2026-11-30); f26bc59's subject is "ADDENDUM-m1 v0.1 COMMITTED"; RESULTS.md:1145–1146.
133. **CONFIRMED.** Decision (16)'s date, 2026-11-06. It follows the seat's rule against RESULTS.md:1141. See O1.
134. **CONFIRMED.** The G-CAL go decision: "the PI's go for G-CAL-OLMo on sft, dpo and instruct, smoke first (the PI's routing of 2026-11-06, quoted at RESULTS.md@54bbfe5:237)".
    - Line 237 at 54bbfe5 is "> Go for G-CAL-OLMo on sft, dpo and instruct, smoke first."
135. **CONFIRMED.** The G-CAL go decision's date, 2026-11-06. RESULTS.md@54bbfe5:233.
136. **CONFIRMED.** Both decisions have `other_unit` "Q-F0" and `other_state` "PASS". As #41.
137. **CONFIRMED.** Against the seat's §1 field list (answers :9), every specified field is present and matches.
    - The detail adds the artifact and checkpoint sha256, the run window, the pod and the backend identifier. These are Code's additions, and the draft discloses them (draft line 24).
138. **CONFIRMED.** Against p §8 step 1 as written (p :122), schema, cause, `also`, date, detail ("condition-(4) figures and the pointer to the read raw's §5") and decisions ("as the seat's answers §1 list them") all match.
139. **CONFIRMED.** The three outputs follow from these records exactly.
    - An independent rebuild matches byte for byte (`json.dumps(sort_keys, ensure_ascii=False, indent=1)` plus a newline).
    - It covers the record's path and sha256, the `rows`, `date_is_clock_of_record` false, `gate_release`/`release` null, and the proposal sha256 (`42ab36ec…6c6b`, PROPOSAL-m v1.11's), along with the analyzer, package and closure sha256s.

---

## Code's dispositions (2026-11-06)

- **#7, applied.** The headline now reads "The analyzer's not-run path wrote the output from Code's record file"; "the record" names only the input file.
- **#30, applied as an attribution.** The entry quotes the seat's §1 ("C7's convention: the calendar date of the terminal event, the grader's verdict") and adds a dated citation residue: the rule it states is the one PIN-43 records from the seat's C5 (scripts/m_analyze.py:510-513). The value 2026-11-06 is unchanged.
- **#113, applied.** The closing bullet uses the seat's words, "inputs the v1 posting cannot run without", with PIN-23's cross-check beside them.
- **#129, disclosed, not regenerated.** Each record's detail cites its per-checkpoint run times to "the G-CAL-OLMo entry, 6ce8b9a"; the entry gives the overall window and the per-checkpoint times are in the same commit's run raw (results/raw/2026-11-06_gcal-olmo.txt). The values are right; the records and the write-once outputs stand as written, and the entries carry the note.
- **#19 (not checkable), reworded.** "PROPOSAL-p's pre-read is another session's (the routing session's word)".
- **O1, not raised.** The decision (16) date follows the seat's "dated as its commit entry is" (the entry's header, RESULTS.md:1141). Under the record's dates convention, PI-local dates and Code's stamps that differ by a day near midnight are recorded as given and not corrected; nothing in the record turns on the day, since Q-F0's VERDICTS (2026-10-19) precede the decision either way.
- **The routing's file link.** The relayed block names neither the answers file nor its sha256; the file and its sha256 (4c3f57d4...bf82) were named in the routing session's message, and the block's items match the seat's §6 one for one.
