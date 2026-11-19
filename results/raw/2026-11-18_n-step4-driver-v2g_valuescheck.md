# n step 4 — driver v2g's commit texts: the blind values-check, as returned, with every disposition

PI date 2026-11-18. Code (the n-build session).

**What was checked.** One blind pass by a subagent over four drafts:
- T1, the entry (`RESULTS.md`, the Log's head). The brief named `cd95f2c6…8048`; the checker read `e914b2ff…2cb5`
  from its first hash to its last (see "Two texts moved under the check" below);
- T2, n-build's close line on `6e3474d`'s entry, `391e686b…07fb`;
- T3, the self-test raw, `39a441c7…6771`;
- T4, the review raw's head and dispositions: `44ae31d5…25dc` at the checker's first hash, `ab23da79…147f` after an
  edit during the check.

**The checker's brief** (`1fad9b1d…89f5`, 101 lines):
- named the sources:
  - the seat's answers of the fourth sitting, the conditional ruling raw and the PI-routing raw of that sitting;
  - the resume's committed output, v2f's self-test raw, and `RESULTS.md`'s entries of `6e3474d` and `1272702`;
  - HEAD's driver, the package modules, `data/n/ids/labels.json`, BK's `reduced.json` (its member selected by
    `startswith("ol")`), BK's session skeletons (reached by `cd` and a glob, their names listed by `echo` first) and
    git history;
  - in Code's scratch, by name only: v2g's final bytes, the two self-test outputs, and the review's report and brief;
  - the coordinating session's words, which are in no file, quoted verbatim;
- quoted the list of record v2's items 1–5, verbatim;
- required item 3's pathspec and the `data/mf3` exclusion on every git command over the tree, that a glob is expanded
  and read before it is looped over, and the `rev-parse` form for a tracked-and-clean check;
- barred any interpreter, any write, any network and any guard marker in an argv (jq filters included); anything
  under `data/mf3`, `data/*/ckpt` or `data/*/reports`; and, in Code's scratch, anything but the named files.

The prompt that launched the checker pointed to the brief by path and misnamed its hash prefix ("dde0…", the review
brief's); the checker hashed the brief itself and reported both.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (234 lines, sha256
`5fbaf64a…b246`). It names no local path.

**Totals:** 116 items — 94 CONFIRMED, 7 IMPRECISE, 0 FAIL, 15 NOT CHECKABLE — and 12 observations.

**The checker's departures:** none barred, by its report. Its disclosures, for the seat to class, are in v2g's entry's
departures, as its report states them.

## 1. Dispositions

**Two texts moved under the check.**
- T1 was edited after the brief named its bytes and before the checker first hashed it: F3's line in the review
  bullet, its quotation made exact to the driver's words. Rebuilt by reversing that one edit, the briefed bytes hash
  to `cd95f2c6…8048`, as the brief named them; with it, to `e914b2ff…2cb5`, the bytes the checker read.
- T4 was edited during the check: its local-path sentence, in the form item 103 asks for. Item 104 confirms the new
  sentence on `ab23da79…147f`.

**The IMPRECISE items, all applied:**
- **22** (T1): the message "names the session (for two reads, the cell and run) and quotes no value".
- **41** (T1): the scope of the check on the committed `reduced.json`, in the checker's words.
- **48** (T1): the resumes' checks, in the checker's words.
- **76** (T2): the citation, "(§2.2; the ruling's header and item 2)".
- **77** (T2): item 5 of the conditional ruling, in the checker's words, lightly edited.
- **103** (T4, the briefed bytes): resolved by the edit during the check (item 104).
- **110** (T4): F3's disposition now quotes each place in its own words.

**The NOT CHECKABLE items** (8, 9, 12, 14, 15, 17, 31, 64, 65, 69, 87, 89, 93, 94, 107) stand as declared. They are:
- files, a run and a commit still to come;
- the two drafts not kept (the first draft and the reviewed draft), and the numstat against the reviewed draft;
- Code's own conduct (its reads in full, the overlay's making, the command as typed, the count's method).

**The observations:**
1. Applied: the final hashes of every text go with the commit-window request.
2. Applied in T3: HEAD moved to `8038c63` and then to `ecf349d` after the overlay was made; neither changed any of
   the overlay's paths.
3. Applied in T3: the box's measured "389/389 n selftest checks pass" for v2f at the resume (the resume's output,
   line 36), beside the arithmetic 408.
4. Applied in T3: the box runs the self-test "in the copy the launch files name".
5. Not applied: the driver's own docstring for `bk_d0_reads` carries item 22's wording. Changing it would move the
   self-tested bytes; it waits for the next driver change, and T1 alone is corrected.
6. Applied: the two `git diff --name-only` commands over the package's folder without the exclusions are disclosed as
   Code's departure in T1.
7. Applied in T1: the reviewer's and the checker's departures sit under "Departures", before "Values-check", as in
   `1272702`'s entry; the count sentence cites "(the third sitting's answers, §5.2)"; "Committed by path" is a list,
   with **Next** inside it.
8. Applied in T2: it calls itself n-build's line of the routing's item 4, and ends with "Values-check and
   departures: with driver v2g's entry."
9. Applied in T1: the check that runs twice is named (the non-finite case's, once per stage).
10. Applied in T1: item 3 names the module's docstring and those of `run_backend_ext` and the self-test.
11. Applied in T4: the record is keyed "by the environment's tag".
12. Applied in T4: the review brief quoted (b)'s instruction "without its last sentence".

## 2. The edits after the check, checked by tool

- **The checked drafts, rebuilt.** No draft was kept as the checker read it, so each was rebuilt from its final text
  by reversing Code's edits, and confirmed by sha256 against the checker's own hashes: T1 `e914b2ff…2cb5`, T2
  `391e686b…07fb`, T3 `39a441c7…6771`, T4 `ab23da79…147f`, and the briefed T1 `cd95f2c6…8048` and T4
  `44ae31d5…25dc`.
- **The diffs.** `diff -U0` of each final against its checked draft holds only the dispositions above, and Code read
  each diff in full:
  - T1 has 8 hunks: items 22, 41 and 48; observations 9 and 10; the reviewer's departures moved out of the review
    bullet, with the values-check line's placeholder; the departures and the values-check line (observations 6 and
    7, and the placeholder filled); and the count sentence with **Next** (observation 7);
  - T2 has 3 hunks: observation 8's two lines, and items 76 and 77 in one hunk;
  - T3 has 2 hunks: observation 2, and observations 3 and 4 in one hunk;
  - T4 has 3 hunks: item 110 and observations 11 and 12.
- **The quotes.** Every quote in T1, T2 and T4 is found, joined across wrapped lines, in its source: 19 of 19. The
  sources are the seat's answers, the PI-routing raw, v2g's final bytes, and the coordinating session's words as filed
  in Code's scratch.
- **The finals:**
  - T1, the entry, `83756493…448c`, 126 lines (spliced with the blank line that ends it);
  - T2, `f128bf1f…80d0`, 40 lines;
  - T3, `6896a066…4e33`, 42 lines;
  - the review raw (T4 with the report), `e9d98009…c9ce`, 180 lines.
- **The commit's gate** re-runs these checks on the staged blobs. It also checks:
  - the driver's sha256 and the two self-test outputs' sha256s and lines;
  - that `RESULTS.md` is HEAD's with the entry at the Log's head and the close line at the end of `6e3474d`'s entry,
    and nothing else;
  - that nothing under `data/` or `valence_core/` is staged;
  - the commit-time count of the home-folder prefix, as a count.

## 3. The report as returned

```text
BLIND VALUES-CHECK: v2g's four texts (T1–T4)

Bytes checked (sha256, abbreviated with `cut`):
- T1 entry.md is e914b2ff…2cb5 at both my first and my last hash. That is NOT the brief's cd95f2c6…8048, and I never saw the cd95f2c6 bytes. Every T1 item below is on e914b2ff.
- T2 close_6e3474d.md is 391e686b…07fb, as the brief states.
- T3 selftest_raw.txt is 39a441c7…6771, as the brief states.
- T4 review_head.md was 44ae31d5…25dc (as the brief states) at my first hash and read. It CHANGED during the check and is now ab23da79…147f. Its old lines 23–24 became lines 23–25, a new "local path" sentence; the rest is identical by my reading. T4 line numbers below are the 44ae31d5 ones; after L24 the new file runs one line later.
- The brief itself is 1fad9b1d…89f5: 101 lines, first line as stated. "dde0…" is review_brief_final.md (dde0ef29…3555).

ITEMS

T1 (entry.md, e914b2ff…2cb5)
1. L1–4. The heading: v2g committed before backend-ext-2; §2.3's two lines after the distribution line; nothing in the read path; "§2.3"; "route as given". CONFIRMED. answers L29; routing raw L26; v2g L1094–1096.
2. L3–4, L7. The n package is unchanged, at f927608c…3c03. CONFIRMED.
   - `git diff --name-only b523f6a HEAD -- . ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/mf3/**'` lists nothing under valence_core/.
   - The v2f raw (L7) and the resume output (L39) both give the full digest.
   - guard.py L40–41 hashes PACKAGE_DIR.
3. L6. The driver 7aefd06b…5b67 (v2g). CONFIRMED. shasum.
4. L6–7. On 1272702's scripts/n_sessions.py (v2f, e29839c8…1152), unchanged since. CONFIRMED.
   - shasum.
   - `git rev-parse HEAD:` equals `git hash-object` (ecd94ed6…).
   - The newest commit on the path is 1272702.
5. L7. numstat +283 −22. CONFIRMED. `git diff --no-index --numstat` gives 283 22.
6. L8. 397/397 on the laptop. CONFIRMED. selftest_run2.txt.
7. L8. The reviewed draft at 394/394. CONFIRMED. selftest_run1.txt; review brief L29; report L12 (378 + 16).
8. L9. The self-test raw's name. NOT CHECKABLE: a future file, not tracked and not present.
9. L10. "The box runs it at backend-ext-2's start". NOT CHECKABLE: a future act.
10. L11. The review of b8ebc595…66b5: 0 BUG, 2 RISK, 3 NIT, 6 mutants, 5 observations. CONFIRMED. review brief L8; report F1–F5, M1–M6, O1–O5.
11. L12. Every finding is applied in v2g. CONFIRMED.
   - F1: v2g L1530 and L1540–1542, with checks at L1593–1594, L1740–1742 and L1792–1795.
   - F2: L719 and L1339–1350.
   - F3: L72 and L697.
   - F4: L82–83.
   - F5: L121–125.
12. L12. "+52 −30 on the reviewed draft". NOT CHECKABLE (per the brief).
13. L12–13. Every surviving mutant has a killing test, except M5, whose line the fix removed. CONFIRMED.
   - M1: the two smoke pins.
   - M2: L1339 (cue_U).
   - M3: L1340 (random).
   - M4: L1343 (-Infinity).
   - M6: L1749.
   - M5: bk_d0_reads (L716–721) has no try/except left.
14. L14. The review raw's name. NOT CHECKABLE: a future file.
15. L15. Nothing of v2g ran on a checkpoint's weights. NOT CHECKABLE. Consistent with the model-free self-test (v2g L6–9, L1458–1471).
16. L15–16. Each run was in a window granted for its bytes. CONFIRMED. (c5), for b8ebc595…66b5 and for 7aefd06b…5b67.
17. L16–17. No other battery ran in them; Q-F3's laptop rules (model-free, nice -n 19). NOT CHECKABLE. T3 shows nice -n 19; the wording matches RESULTS.md L381–383.
18. L18. One code path for both stages; nothing in the read path. CONFIRMED. L1095–1096 run before `if second: return 0` (L1100); the diff leaves the plan, StageInputs and runner.run untouched.
19. L19–20. Step 3, before G-VER and the load; the new BextEnv seam bk_reads. CONFIRMED. Docstring L53–56; seam L928; wiring L965; the call (L1057) comes before G-VER (L1064) and the load (L1071).
20. L20–22. Each session's own (cell, run) d = 0 "none" read with its cues, in any cell; margin, logprob_S and logprob_U taken. CONFIRMED. L701–722.
21. L22–24. These refuse: two reads for one (cell, run); a session without its read; a value absent, not a JSON number (a string or boolean) or not finite. CONFIRMED. L707–708, L713–715, L718–720.
22. L24. "the message names the session and quotes no value". IMPRECISE.
   - L708's message is "BK records two d = 0 reads for {key}", where key is (cell, run).
   - It fires for any duplicated (cell, run) at point 0, ste_* cells included.
   - Put instead: "…refuses the stage; the message names the session (for two reads, the cell and run) and quotes no value."
23. L25. On COMPLETE, directly after the distribution line. CONFIRMED. L1085–1090, L1094–1096.
24. L26–27. Line (a) "BK's d = 0 margins": |cached margin − BK's|, median, max, compared, of. CONFIRMED. L745, L750–755, L762–764. The record's margin is the cached path's (schema.py L27, L363).
25. L28–29. Line (b): S and U each with median, max, compared and of; the pooled figure beside, over twice the reads. CONFIRMED. L746–748, L754–755, L765–766.
26. L31–32. Aggregates only; a non-finite value is not compared and is counted; the medians are np.median's. CONFIRMED. L737–738, L750–752.
27. L33–34. The docstring's step 3, step 7, backend-ext-2 paragraph and readings parenthetical change, and R8 gains one sentence. CONFIRMED. The diff's module-docstring hunks.
28. L34. The seat accepted R7 and R8 at its fourth sitting, §5. CONFIRMED. answers L43.
29. L34–35. The two quotes, "beside §2.3 (b)'s per-label figures" and "a printed figure that binds nothing". CONFIRMED. v2g L110–112.
30. L35. The sentence is pending the seat. CONFIRMED, as declared at v2g L83.
31. L36. The first draft printed (b) pooled and declared R9. NOT CHECKABLE. Its bytes are not kept; (c2) is consistent.
32. L37–39. The (c2) quotation, including "the same per label". CONFIRMED. (c2), apart from its list marker; answers L29.
33. L39. v2g takes the split, with the pooled figure beside. CONFIRMED. L754–755, L761–766.
34. L39–40. The first draft's grant lapsed unused; R9 is gone. CONFIRMED. (c5); the readings are R1–R8 only (L85–112), and the file has no "R9".
35. L41. §1.3; the coordinating session agreed no new render is needed. CONFIRMED. (c3); answers L19.
36. L43. labels.json (HEAD's) keeps "space", with 12 labels of 3 tokens. CONFIRMED. The file is clean; jq gives kept true, 12 labels, lengths [3].
37. L44. 160 skeletons, 12 distinct cues, 0 lacking "space". CONFIRMED.
   - By cd plus glob, then echo: 14 files, floor_b0–b7 with 5 each and neu_b0–b5 with 20 each, so 160 records.
   - cue_S and cue_U together take 12 values, the same 12 as the space candidate's label keys.
38. L45. The prompt ids do not depend on the convention. CONFIRMED.
   - (c3).
   - sessions.jsonl records carry no convention field.
   - Every candidate has prefix_kept 960 of 960.
39. L46–47. labels_ok 4 at the resume. CONFIRMED. resume output L58.
40. L48. 19 new checks at run time, 18 in the source. CONFIRMED.
   - There are 18 new chk calls; the non-finite loop's check (L1719) runs twice.
   - 378 + 19 = 397.
41. L49–50. The scope of the reduced.json check. IMPRECISE.
   - Finiteness and |margin − (S − U)| ≤ 1e-9 are asserted over the 24 rows only (L1308–1316).
   - Put instead: "on the committed `reduced.json`: a row for each of backend-ext's 24 sessions, floor sessions and others among them, each value finite and the recorded margin equal to S − U to within 1e-9; and a row for each of the set's 160 sessions;"
42. L51. The session's own d = 0 read only, in any cell. CONFIRMED. L1317–1324.
43. L51–54. 13 refusals as listed, no message quoting a value. CONFIRMED. L1339–1350.
44. L55–56. The known answer. CONFIRMED. L1351–1366, recomputed by hand:
   - medians 12.5, 25, 37.5 and 30 /1024 (pooled: the 24th and 25th of 48 are both 30/1024);
   - maxima 0.5, 1.0, 1.5 and 1.5;
   - the fresh values (99.0 and 0.0) are not read.
45. L56–57. Non-finite values not compared; nothing compared gives nulls; a read outside the table is refused. CONFIRMED. L1367–1379.
46. L58. The lines' form and production's two BK seams. CONFIRMED. L1380–1393.
47. L59–61. 0.0, directly after the distribution line: in the first stage before in-band, in backend-ext-2 as its last two lines. CONFIRMED. p1 at L1587–1592; p7 at L1647–1651.
48. L61. "and again on their resumes". IMPRECISE.
   - backend-ext-2's resume after COMPLETE: only the count of printed pairs is checked (L1659).
   - Its resume after a PAUSE: printed once, directly after the distribution line, values not checked (L1686–1688).
   - Each stage's resume after the non-finite pause: counts only (L1718–1723).
   - The first stage's resume after COMPLETE (L1606) is not checked for the lines, and no resume check asserts 0.0.
   - Put instead: "…in the first stage (before the in-band count) and in backend-ext-2 (its last two lines); backend-ext-2's printed again on its resume after COMPLETE, and once, directly after the distribution line, on its resume after a PAUSE; no line on a PAUSE; on each stage's resume after a non-finite pause, the finite reads alone compared (23 of 24 margins, 23 of 24 per label, 46 of 48 pooled); …"
49. L61–62. No line on a PAUSE; 23/24, 23/24 and 46/48. CONFIRMED. L1677–1678, L1718–1723.
50. L62. A smoke's lines over its 2 reads. CONFIRMED. L1737–1739.
51. L62–63. BK's values asked for once, for the plan's sessions in launch order (24; 2 per smoke, in both stages). CONFIRMED. L1593–1594, L1740–1742, L1792–1795.
52. L63–64. A table missing a session is refused before G-VER and the load. CONFIRMED. L1743–1749.
53. L65. One pass over v2f → b8ebc595…66b5. CONFIRMED. review brief L5–9.
54. L66. No interpreter run, nothing written. CONFIRMED, by its report (L109).
55. L66. The brief quoted items 1–5 and the standing lines. CONFIRMED. Review brief L65–70 are byte-identical to results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md L18–22 (sed piped to shasum: 2373155c…c185 for both). The standing lines are at L60–64.
56. L67–70. F1/M1. CONFIRMED.
   - report L27–33.
   - testing.py L110: runs below 40 are floor sessions.
   - v2g L1314 asserts non-floor sessions among the 24.
57. L70–71. The seam records its argument; three checks; the smokes kill M1. CONFIRMED. L1540–1542. In the flow, floor_all and the plan are the same 24.
58. L72–74. F2/M2–M5; the type check the reviewer offered; 7 cases to 13. CONFIRMED. report L44; v2g L719, L1339–1348.
59. L75–76. M6 killed. CONFIRMED. L1743–1749.
60. L77–78. The F3 quotes. CONFIRMED. Docstring L72–73.
61. L79–80. O1: 240 reads at point 0, all "none", one per (cell, run), none non-finite. CONFIRMED. My own jq (startswith("ol")): 240, ["none"], 240 distinct, 0 non-finite.
62. L81–84. The reviewer's departures and four disclosures. CONFIRMED. report L103–107.
63. L87–90. Code's ls departure, and the forward form. CONFIRMED. (c4).
64. L87, L90. The literal `ls "$SK"/*`, and "this entry's counts used it". NOT CHECKABLE. My cd-plus-glob reads gave the same counts.
65. L91–94. The commit, its count, "Not pushed". NOT CHECKABLE: future.
66. L95. Next: the launch files, through the coordinating session. CONFIRMED. Routing raw L16; RESULTS.md L316–317.

T2 (close_6e3474d.md)
67. L1. "this entry's STOP". CONFIRMED. answers L3.
68. L4, L6. c265797f…61a5 and ba9f9632…cc32. CONFIRMED. shasum; routing raw L10, L12.
69. L6. "in full". NOT CHECKABLE.
70. L6. Both committed by path at c7d0009 by the coordinating session. CONFIRMED.
   - c7d0009 touched exactly those two files, and `--diff-filter=A` gives c7d0009.
   - Routing item 7; RESULTS.md L310.
71. L6–9. "route as given", relayed; the block committed at 8038c63. CONFIRMED. Routing raw L26; (c6); `--diff-filter=A` gives 8038c63.
72. L10–11. The Q1 quote and its rendering (§1.2). CONFIRMED. answers L17.
73. L11–12. The lock, and space+eot as the near-tie. CONFIRMED. answers L17.
74. L13–14. §1.3's ids. CONFIRMED. Items 36–38; (c3).
75. L15–16. Q2 (§2.1, §2.3). CONFIRMED. answers L25, L29.
76. L16–17. "mechanically", and "holds"/"fails", cited to (§2.2). IMPRECISE (the citation).
   - "mechanically" is the ruling raw's header (L3); "holds"/"fails" is its item 2 (L8).
   - §2.2 says "each printed with the resume's line".
   - Put instead: "…prints it with the resume as "holds" or "fails" (§2.2; the ruling's header and item 2)."
77. L17–19. "the stage's entry cites it … (its item 5)". IMPRECISE.
   - Item 5 (ruling L15) says it "is committed with the stage's entry as the record of what would have applied".
   - Put instead: "If no pause fires, the file is not used; its item 5 has it committed with the stage's entry as the record of what would have applied, and as §2.2 had it committed before the run (at `c7d0009`), the stage's entry cites it."
78. L20–21. The Q3 quotes and the lock's statement. CONFIRMED. answers L35.
79. L22–23. Alpha. CONFIRMED. answers L39.
80. L24–27. §5, with its quote. CONFIRMED. answers L43.
81. L28. §7. CONFIRMED. answers L55–57.
82. L29–36. This session's part, in order. CONFIRMED.
   - (c1) and routing item 2: v2g, self-test, review, values-check, commit.
   - RESULTS.md L316–317: the launch files go through the coordinating session.
   - §5 and routing item 5: the follow-up comes after COMPLETE.
   - 1272702's entry L444: "settled with n-analyzer".
   - §2.4 (L31): the LOCK-n v0.1 draft.
   - "the extension's entry" and the order are Code's plan.

T3 (selftest_raw.txt)
83. L1–3. The heading. CONFIRMED.
84. L5–6. The full sha256 of v2g. CONFIRMED.
85. L7–9. Unchanged since b523f6a; the digest v2f's raw records. CONFIRMED. Item 2; v2f raw L7.
86. L11–12. The HF cases run only with torch and transformers, and are otherwise skipped and counted. CONFIRMED. v2g L6–9, L1458–1471; hftiny.py L27–33.
87. L13–18. The overlay at c7d0009. NOT CHECKABLE. Same path list and form as v2f raw L11–16.
88. L18–19. 8038c63 changed none of the overlay's paths. CONFIRMED. It touched RESULTS.md and three results/raw files. When the overlay was made is not checkable.
89. L20–23. The command. NOT CHECKABLE. Same form as v2f raw L17–20.
90. L25–29. Run 1: b8ebc595…, its window, output 225dc44f…, 394/394. CONFIRMED. Review brief L8; (c5); shasum. The re-hash and the exit code are not checkable.
91. L31–34. Run 2: 7aefd06b…, output 1df0a04d…, 397/397. CONFIRMED. (c5); shasum.
92. L36–37. The first draft was granted a window, never ran, and its grant lapsed; the hash's ends match. CONFIRMED. (c5).
93. L36. The middle of the full hash, and "pooled S and U". NOT CHECKABLE.
94. L39–40. The box runs it in the fresh copy at this commit. NOT CHECKABLE: future (see observation 4).
95. L40–41. 408 = 397 + 11 (v2f's raw: 389 against 378); v2g touches no HF case. CONFIRMED.
   - v2f raw L33.
   - The box printed 389/389 at the resume (resume output L36).
   - The diff leaves hftiny and the HF check at L1458–1471 unchanged.

T4 (lines of 44ae31d5…25dc)
96. L6. e29839c8…1152 (v2f, at 1272702, unchanged since). CONFIRMED.
97. L7–8. b8ebc595…66b5; (b) per label with the pooled figure under R8's kind. CONFIRMED. Review brief L8; report L18.
98. L11–14. What the reviewer's brief held. CONFIRMED. Review brief L5–29.
99. L15. The code it named. CONFIRMED. Review brief L31–35.
100. L16–18. Items 1–5 verbatim, plus the standing lines. CONFIRMED. Item 55.
101. L19–21. What the brief barred. CONFIRMED. Review brief L49–59.
102. L23–24. 109 lines, 0561eed3…fb33. CONFIRMED. shasum; `wc -l` gives 109 and the file ends in a newline. The jq extraction is not checkable.
103. L24 (44ae31d5). "It names no local path." IMPRECISE. Report L104 names "~/.claude/projects/…/tool-results/". Put instead: "It names no local path but one generic, elided folder, `~/.claude/projects/…/tool-results/`, in its first disclosure."
104. L24–25 (ab23da79, the bytes after the mid-check edit). That same sentence. CONFIRMED. Report L104; the report holds no other local path.
105. L26. The totals. CONFIRMED.
106. L30. 7aefd06b…5b67. CONFIRMED.
107. L30–31. "+52 −30", "every one a disposition". NOT CHECKABLE.
108. L32–39. The F1/M1 disposition, including the `ss` variant. CONFIRMED. report L33; v2g L1530, L1540–1542, and the three checks.
109. L40–45. The F2/M2–M5 disposition. CONFIRMED. report L42–44, L66; v2g L716–721, L1339–1350.
110. L46–47. F3: "the docstring's step 7 and bk_d0_reads now say … "of any cell, floor or not"". IMPRECISE.
   - bk_d0_reads (L697) reads "of any cell (floor or not)".
   - Put instead: "Applied: the docstring's step 7 now says a session "of any cell, floor or not", and `bk_d0_reads` "of any cell (floor or not)"; in both, its read is the one for "the session's own cell and run"."
111. L48–49. The F4 quote. CONFIRMED. v2g L82–83.
112. L50. F5 reflowed. CONFIRMED. L121–125.
113. L51–52. M6. CONFIRMED.
114. L53–56. O1's counts, and margin = S − U exactly over the 160. CONFIRMED by my jq (max |dev| 0 over all 240). "before the draft" is not checkable.
115. L57–59. O2 to O5. CONFIRMED. v2g L698–700, step 3, step 7, L110–112.
116. L60–64. The departures. CONFIRMED. report L103–107.

TOTALS: 116 items.
- CONFIRMED 94.
- IMPRECISE 7: items 22, 41, 48, 76, 77, 103, 110. Item 103 is on the briefed bytes; the current bytes resolve it (item 104).
- FAIL 0.
- NOT CHECKABLE 15: items 8, 9, 12, 14, 15, 17, 31, 64, 65, 69, 87, 89, 93, 94, 107.

OBSERVATIONS
1. Hash discipline.
   - T1 is not the bytes the brief names: e914b2ff…2cb5, not cd95f2c6…8048.
   - T4 was edited during this pass (44ae31d5…25dc → ab23da79…147f).
   - Re-send the final hashes for all four with the commit-window request.
2. T3 §1 names 8038c63. HEAD is now ecf349d (its parent is 8038c63), which also changed none of the overlay's paths (RESULTS.md and a fourth-sitting values-check raw). Name it if it landed before run 2 or the commit.
3. T3 §2 cites v2f's arithmetic 389. The box actually printed "389/389 n selftest checks pass" (bext-resume4_out.txt L36; 6e3474d's entry L147). Citing that grounds 408 in a measured count.
4. T3 §2's "in the fresh copy at this commit" presumes a choice. The pod session's close line (RESULTS.md L318–321) leaves it to the launch files: copy-resume4-1272702 (at v2f) or a new copy at v2g. Suggest "in the copy the launch files name".
5. The bk_d0_reads docstring (v2g L698–700) carries item 22's wording. Fixing it would change the driver's bytes, so it is Code's call; T1 can be fixed alone.
6. T3 L7 quotes `git diff --name-only b523f6a HEAD -- valence_core/n`: a positive pathspec with none of the three exclusions. That is the reviewer's disclosure 3, made wider; disclose it or quote the form actually run.
7. Style against 1272702's entry:
   - its Departures bullet lists the reviewer's and the values-checker's departures (L448–459);
   - its count sentence cites "(the answers' §5.2)" (L478; 6e3474d's L216); T1 L94 does not;
   - its "Committed by path" is a sub-list with Next inside it.
8. T2 has no values-check line and no departures line. The pod session's close lines end with both (RESULTS.md L288–302, L347–366). Suggest "Values-check and departures: with driver v2g's entry." T2 could also call itself item 4's close line, as L313–315 does.
9. T1 L48 could name the check that runs twice (L1719, once per stage). Cross-check, nothing to fix: 397 − 394 = 3, which are F1's three pins.
10. T1 item 3 names only the module docstring; v2g also edits the docstrings of run_backend_ext (L971–976) and _bext_selftest (L1124–1128).
11. T4 L33 says "by environment". The record is keyed by the environment's tag, and some tags are shared ("run", "refuse2"). No check is affected.
12. T4 L12 says "quoted". The review brief quoted (c1) and (c2) in part: (c2) without "That way nothing waits on an R9 for the seat to strike."

DEPARTURES: none that a rule bars, by my reading. Disclosures:
- Every digest used shasum, which is a Perl script on macOS. The list of record's item 1 permits it and the caller directed it.
- /usr/bin/grep on single named repository files: RESULTS.md, guard.py, hftiny.py, schema.py, testing.py, sessions.py, and the list-of-record raw.
- One `git grep -l -F` taking item 3's exclusions plus the mf3 exclusion.
- Reads beyond the named sources: guard.py, hftiny.py and sessions.py (by grep); the first record's keys of data/n/ids/sessions.jsonl; the list-of-record raw, L18–22; RESULTS.md L1–130.
- In S, named files only:
  - `sed -n` ranges of review_brief_final.md and of the brief, piped to shasum;
  - `wc -l`, and `tail -c 1 | od`, on review_report.md;
  - `wc -l` on review_head.md.
- git log formats with %ad (a short date).
- `git diff --no-index -U1` piped to head.
- The skeletons were reached by cd plus glob, then echo, then jq on the 14 names (no marker). zsh's builtins showed no chpwd, precmd or preexec hooks.
- A name-only ls and `git ls-files` on two named raw paths that do not exist yet.

Nothing under data/mf3, data/*/ckpt or data/*/reports was touched. No whole-tree git status, no write, no network, and no guard marker in any argv.
```
