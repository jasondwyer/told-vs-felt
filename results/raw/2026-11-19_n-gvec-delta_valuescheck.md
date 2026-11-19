# n — G-VEC's delta (second sitting): the blind values-check, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the drafts of the commit's four texts:
- T1, the RESULTS.md entry: `2d8addb9…7f97` (64 lines), its values-check paragraph and the checker's departures
  placeholders;
- T2, the self-test raw, `results/raw/2026-11-19_n-gvec-delta_selftest.txt` here: `a730f699…02da` (46 lines);
- T3, the review raw, `results/raw/2026-11-19_n-gvec-delta_review.md` here: `d20976d7…a703` (186 lines);
- T4, the dated note on `355e3a2`'s entry: `33737dec…e69f` (8 lines).

**The checker's brief** (`5d848b01…6392`, 84 lines, given to the checker as a file, with its sha256 to verify):
- named the texts and the sources: in Code's scratch, by name and sha256, drafts 1 and 2 of the three files, the
  self-test outputs and exit files of runs 1 and 2, and the review's brief and report; in the repository, the seat's
  answers of both sittings, RESULTS.md (`355e3a2`'s entry and the coordinating session's notes entry), the first
  run's record and output raw, `.gitignore`, and the package digest in `package_sha256_of`'s form over HEAD's blobs
  and with draft 2's two package files in place;
- asked for every factual claim to be checked, each numstat and count of checks among them, and for T3's §2 to be
  byte-equal to the review's report;
- barred any interpreter but `shasum`, any write, any network, any guard marker in an argv, anything under
  `data/mf3`, any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the
  named files and the brief itself;
- quoted the list of record v2's items 1–5, verbatim, and required item 3's pathspec and the `data/mf3` exclusion on
  every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (170 lines, sha256
`7bb4e5ff…e1cd`). It names scratch files only by their paths inside the scratch folder. One of its hash
abbreviations is a slip, against the full sha256 its brief gave: "5d848b01…6396", the brief's own, is
`5d848b01…6392`.

**Totals:** 104 items: 84 CONFIRMED, 7 IMPRECISE, 0 FAIL, 13 NOT CHECKABLE; and 8 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class. Its
three `git check-ignore -v` runs used the instrument the brief named.

## 1. Dispositions

- **The IMPRECISE items,** each applied in the checker's words or near them:
  - 2 (T1): the delta's basis is the second sitting's §1.2, §1.3, §1.4 (ii)–(iv) and §1.5, §1.4 (i) being G-CAL-n's;
  - 32 (T1) and 98 (T3): `n_by_position` holds a count beside each `rms_by_position` figure, not beside every
    diagnostic figure;
  - 38 (T1): the refusal before the load is now declared in `gvec.py`'s readings, by draft 3 (observation 8), so T1's
    "(`gvec.py`'s docstring)" holds for it;
  - 76 (T3): of the review's two abbreviations, one carries a five-character tail and one is a slip;
  - 83 (T3): F2's disposition says what the self-test pins, and that `GVEC_STOP_END`'s words are checked only against
    the constant itself (observation 1);
  - 85 (T3): F4 in the reviewer's words, F5 in its substance.
- **The NOT CHECKABLE items** stand: this session's acts and plans (4, 24, 27, 42, 43, 45, 46, 48, 55, 57, 74, 101,
  103).
- **The observations:**
  - 1: met by item 83's wording; the driver's code is not changed for it.
  - 2 and 8, applied in the code, as draft 3: two clauses of `gvec.py`'s readings paragraph, the token counts beside
    each `rms_by_position` figure and the refusal before the load declared (`gvec.py` `e2f7a49e…be94`, 958 lines,
    +7 −5 on draft 2, its module docstring alone); the self-test's run 3; the package digest `d3415b10…a519`. The
    review's scope stays the draft 1 → 2 delta.
  - 3: T3 says F1 is closed for the descriptive figures, R staying a raise, declared; the smoke's order (its record
    written before its R lines print) is not changed.
  - 4: T1's clause reads "no passage of record being that short".
  - 5: T4 says the path is free for the re-run's record.
  - 6: T3's account of the review's brief separates what the delta must do from the texts the new wording was checked
    against.
  - 7: the placeholders are filled.

## 2. The text changed after the check, and the edits checked by tool

- **The text changed after the check** by the dispositions above; by draft 3's hashes and run 3, in T1, T2 and T3;
  and in T1 by its values-check paragraph and the checker's departures, which replace the placeholders, and by its
  departures' first bullet, which now names the two extractions by `jq`.
- **The edits, checked by tool:** fixed-string counts over each text unwrapped, for each disposition's new wording and
  each removed wording's absence, and for draft 3's hashes and run 3's count in T1 and T2; T2's run-3 verbatim line
  equal to its output, and T3's §2 byte-equal to the review's report: 37 of 37.
- **No second full pass** was made over the texts.
- **The finals:** the entry `3e269075…d89a` (76 lines); the self-test raw `3ef90ba6…4315` (56 lines); the review raw
  `8d3399f3…3694` (191 lines); the note `f842ca88…08cd` (8 lines).

## 3. The report as returned

BLIND VALUES-CHECK: G-VEC's delta on the second sitting (T1 entry, T2 self-test raw, T3 review raw, T4 dated note)

Setup checks:
- Brief S/step4b/gvec2/vc_brief.md: 5d848b01…6396, 84 lines.
- HEAD is ab72d0f.
- Every text and source matched its stated sha256 and line count: T1 2d8addb9…7f97 (64 lines), T2 a730f699…02da (46), T3 d20976d7…a703 (186), T4 33737dec…e69f (8), the six drafts, review_brief.md (c0c50e1f…8729, 92 lines) and review_report.md (e5bffcd5…4724, 113 lines).
- Every named repository source is tracked and clean (rev-parse HEAD:<path> = hash-object).
- T3 §2 (review_raw.md:74–186) is byte-equal to S/step4b/gvec2/review_report.md (cmp equal, same sha256, 113 lines).

ITEMS

T1, the entry
1. T1:3–4, the answers committed at `f4b3e73`. CONFIRMED. RESULTS.md:29 says "committed by path at `f4b3e73`".
2. T1:4, "§1.2–§1.5" as the delta's basis. IMPRECISE. The delta implements §1.2, §1.3, §1.4 (ii)–(iv) and §1.5. §1.4 (i), the arrival score, belongs to a later gcal delta (seat raw :31, :63; review O8). T2:1 and T3:6 already use the narrower form. Replace with: "second sitting, §1.2, §1.3, §1.4 (ii)–(iv) and §1.5, committed at `f4b3e73`".
3. T1:4, "the PI's routing, item N.1, on "Route as given"". CONFIRMED. RESULTS.md:29–30 (the PI's word), :34 ("N.1–N.4 verbatim to n-build"), :44 (item 1 is G-VEC's STOP path); seat raw :88.
4. T1:4–5, "Model-free, on the laptop". NOT CHECKABLE.
5. T1:7–8, position 0 is left out of the mean (`passage_mean` over rows 1..n) and out of R (squared norms and count both). CONFIRMED. Seat raw :18; draft2 directions.py:53–64; gvec.py:186–194, :204–207.
6. T1:9, `directions.CAPTURE_FROM` = 1. CONFIRMED. directions.py:50.
7. T1:9, every other clause of G1 stands and nothing is re-rendered. CONFIRMED. Seat raw :7 (§0) and :17 (§1.2).
8. T1:9–10, such a passage is refused before the load and again at `passage_captures`. CONFIRMED. n_sessions.py:2205–2208 refuses before make_adapter at :2233; gvec.py:172–174.
9. T1:11–13, the diagnostic block's figures, at both indices, over the 96 neutral passages, descriptive, on a STOP as on a PASS. CONFIRMED. Seat raw :24–29; gvec.py:210–247, :452–458; the STOP record's block is checked at :935–939.
10. T1:13, R_all is the first run's R by the same arithmetic in the same order. CONFIRMED. HEAD gvec.py:141, :145, :153 match draft 2 :177, :188, :241; rms_norm's body is unchanged (directions.py:70–73).
11. T1:13–15, the review found bit-for-bit reproduction of 44.04249774012646 and 45.107750142385356 on identical forwards. CONFIRMED. Report O1 (review_raw.md:152–155); the figures are at RESULTS.md:386–387 and seat raw :14.
12. T1:15, the smoke prints the same lines. CONFIRMED. n_sessions.py:2264–2265; seat raw :24.
13. T1:16, schema `n-gvec-v2`. CONFIRMED. gvec.py:103.
14. T1:16–17, the passages block carries the token counts and `neutral_tokens_in_R`, with the quote "the count entering R beside". CONFIRMED. gvec.py:443; seat raw :22.
15. T1:17, the site block names the convention. CONFIRMED. gvec.py:448.
16. T1:18–19, a STOP goes to the PI with the diagnostic block, on the seat's stated default (§1.5), and the printed lines say so. CONFIRMED. Seat raw :33; gvec.py:126–127; n_sessions.py:2040–2041.
17. T1:20, gvec.py:26–27's stale sentence is corrected (§1.4 (ii)), as 355e3a2's entry owed. CONFIRMED. HEAD :26–27 becomes draft 2 :31–34; "starred at the top" now occurs 0 times; RESULTS.md:452–455; seat raw :31.
18. T1:20–21, directions.py's readings are reworded (§1.4 (iii)). CONFIRMED. HEAD :8–14 becomes draft 2 :8–16; seat raw :31.
19. T1:22, gvec.py 939c9f9c…5b69 (+303 −41). CONFIRMED by shasum and `git diff --no-index --numstat`.
20. T1:22, directions.py c63c8ea8…e527 (+39 −11). CONFIRMED.
21. T1:23, n_sessions.py 2728146e…570c (+58 −20). CONFIRMED.
22. T1:23–24, the package digest moves 1bb0daea…af51 → 58d7ad40…cf82. CONFIRMED. I computed both by shell in the form resume.py:328–350 states, using the 16 names from `git ls-tree --name-only HEAD valence_core/n/`.
23. T1:25, draft 1 555/555 and draft 2 560/560. CONFIRMED. selftest_run1 and run2 .txt and .exit files.
24. T1:25–26, battery windows and `nice -n 19`. NOT CHECKABLE.
25. T1:26, 571 on the box by arithmetic. CONFIRMED. 560 + 11; the +11 is at RESULTS.md:252–253 (035947e) and :428–429 (the BUILD).
26. T1:27, data/n/gvec/gvec.json is the first run's STOP record, 3331da71…ee95. CONFIRMED. shasum; `"status": "STOP"` at gvec.json:194.
27. T1:27–28 and :31, the `git mv` byte for byte on the coordinating session's word; the seat reads it; a later mv reverses it. NOT CHECKABLE (these are plans). The destination is absent (`ls`) and is not ignored (`git check-ignore -v`: no output, exit 1).
28. T1:28–29, a fresh copy at the commit holds no data/n/gvec/. CONFIRMED. `git ls-files` with item 3's pathspec, filtered: data/n/gvec/gvec.json is the only tracked file there.
29. T1:29–30, G7: the stage never resumes and the driver refuses an existing out folder. CONFIRMED. n_sessions.py:2160–2161; gvec.py:58.
30. T1:30–31, a dated note gives the new path. CONFIRMED. T4:3–4.
31. T1:33, Code's reading that the schema is n-gvec-v2 and its R is not the first run's quantity. CONFIRMED. gvec.py:79–80.
32. T1:34, "beside each diagnostic figure its token count, `n_by_position`". IMPRECISE. n_by_position is keyed by DIAG_KEYS and holds one count per `rms_by_position` figure only (gvec.py:229–239, :253). R_all, max_norm and R_mean_of_passage_rms have no entry. Replace with: "beside each `rms_by_position` figure its token count, `n_by_position`: a count, not a figure, so §1.3's "Nothing else" is not read against it;".
33. T1:34–35, a count, not a figure, so "Nothing else" is not read against it. CONFIRMED. gvec.py:80–81; seat raw :29.
34. T1:35–36, an unreached position is null, and the shortest passage has 35 tokens. CONFIRMED. gvec.py:233–234 and :82; out raw :116 (neutral min 35), :111–119 (every other state ≥ 38).
35. T1:37–38, a non-finite figure is recorded as null and listed; the §1.3 quote "none a decision"; R still raises. CONFIRMED. gvec.py:83–84, :222–227, :246, :444–445; seat raw :24.
36. T1:39–40, the convention, the count line, the token counts on each diagnostic line, and the R lines before the block. CONFIRMED. gvec.py:84–86, :435–455.
37. T1:41, the smoke record carries the block, two counts and the convention (the driver's docstring). CONFIRMED. n_sessions.py:146–149, :2256–2258.
38. T1:42, the pre-load refusal (the review's O7) is listed under "(`gvec.py`'s docstring)". IMPRECISE. gvec.py's docstring does not state it; its passage_captures docstring (:165–166) says "refused before its forward". The pre-load refusal is stated only in run_gvec's docstring (n_sessions.py:2136–2137) and coded at :2205–2208. Replace with: "the refusal, before the load, of a passage with no token at positions 1..n (the review's O7; `run_gvec`'s docstring, in the driver)."
39. T1:43, the review's totals: 0 BUG, 8 findings (1 RISK, 7 NIT), 6 mutants, 3 box risks, 9 observations. CONFIRMED. review_raw.md:76–180.
40. T1:44, every finding is applied and each mutant meets a new or extended check. CONFIRMED (see items 79–96).
41. T1:44–46, F1: a non-finite descriptive figure would have ended the run with no record; it is now null and listed, and the R lines print first. CONFIRMED. review_raw.md:81–86; gvec.py:435–455.
42. T1:46, B3 goes to launch files v2. NOT CHECKABLE (a plan).
43. T1:50, Code's `jq` read. NOT CHECKABLE.
44. T1:51–53, the reviewer's departures. CONFIRMED. review_raw.md:183–185.
45. T1:56–60, the committed-by-path list, the home-folder count of 0, nothing on a model, not pushed. NOT CHECKABLE.
46. T1:61–62, the Next steps (launch files v2, the `hashes` window, the relay, the smoke, then the run of record). NOT CHECKABLE. They match seat raw :88.
47. T1:62–63, a PASS fills holes 1–7 and opens G-CAL-n's launch files, which also wait for ADDENDUM-n3. CONFIRMED. Seat raw :33, :51, :71.
48. T1:63, the gcal delta is built meanwhile. NOT CHECKABLE (a plan; seat raw :51 permits it).

T2, the self-test raw
49. T2:1–2, the citations s1.2, s1.3, s1.4 (ii)–(iv), s1.5. CONFIRMED.
50. T2:4, f4b3e73's versions are the same bytes at ab72d0f. CONFIRMED. Blobs 058e4829…, 9b3dca95… and a4d36c36… are equal at f4b3e73, 516b60f and HEAD.
51. T2:5–7, the full sha256s and numstats. CONFIRMED.
52. T2:8–10, both full digests; "516b60f's, unchanged at every commit since". CONFIRMED. RESULTS.md:183; valence_core/n's tree is bc9f748e… at 516b60f, d85fc34, f4b3e73 and ab72d0f; no commit in 516b60f..HEAD touches the folder.
53. T2:11, the form valence_core/m/resume.py's package_sha256_of states. CONFIRMED by my reproduction.
54. T2:11, "The self-test prints no digest". CONFIRMED (each output is one line).
55. T2:11–12, `hashes` runs at launch files v2 in its own window. NOT CHECKABLE.
56. T2:14–15, HF cases are skipped and counted where torch and transformers are absent; the schema module counts as one aggregated line. CONFIRMED. n_sessions.py:6–9, :244–245, :1537, :3561.
57. T2:16–23, the 162-file overlay, the command, the windows, the re-hash and the temporary folder. NOT CHECKABLE.
58. T2:25–28, run 1's three hashes and line counts (878, 162, 3644). CONFIRMED.
59. T2:29–30, run 1: exit 0, one line, e216c32f…0314, the verbatim line. CONFIRMED.
60. T2:31–32, draft 1 adds ten checks to HEAD's 545: seven in gvec.py, two in directions.py, one in the driver's G-VEC self-test. CONFIRMED.
    - RESULTS.md:185 gives 545/545 for the same code.
    - chk-call lines: gvec.py 32 → 40, with two replaced in place and the one-id check's two sites in a try/except of which one runs, so +7.
    - directions.py 9 → 11.
    - driver 147 → 148: the smoke check in _gvec_selftest.
    - 545 + 10 = 555 = run 1.
61. T2:34–37, run 2's hashes and line counts (956, 163, 3662). CONFIRMED.
62. T2:38–39, run 2: exit 0, one line, 13a28d93…edc0, the verbatim line. CONFIRMED.
63. T2:40–42, draft 2 adds five checks, all in gvec.py: M5, M4, M2/M3, F1, F2. CONFIRMED. gvec.py:658, :661, :718, :729, :922; chk lines go 40 → 45, 11 → 11 and 148 → 148; 555 + 5 = 560.
64. T2:42–43, no other check is added or removed. CONFIRMED.
    - The M6 clause sits inside an existing check (directions.py:139).
    - gvec.py's F7 change (:749–753) and M1 clause (:760) extend existing checks.
    - The driver's STOP and SMOKE clauses (:2436–2441, :2452–2453) extend existing checks.
    - The one-id case (:2536–2537) goes inside the single refusal check (:2552–2553).
65. T2:45–46, 571 = 560 + 11, as at the BUILD and at 035947e. CONFIRMED. RESULTS.md:252–253, :428–429.

T3, the review raw
66. T3:5–6, the delta from f4b3e73's bytes, and its citations. CONFIRMED. review_brief.md:7, :10–13, :24–33.
67. T3:7–10, the FROM and TO hashes, line counts, and what was to be read in full. CONFIRMED. Hashes and line counts by shasum and wc; the reading scope from review_brief.md:19–21.
68. T3:11, draft 1 ran 555/555. CONFIRMED. The timing claim is NOT CHECKABLE.
69. T3:13, the brief is c0c50e1f…8729, 92 lines. CONFIRMED.
70. T3:14–16, what the brief gave. CONFIRMED. review_brief.md:10–18, :24–37 (see observation 6).
71. T3:17–21, what the brief asked. CONFIRMED. review_brief.md:38–67.
72. T3:22–24, the list of record items 1–5 quoted verbatim, and the bars. CONFIRMED. review_brief.md:72–80, :87–92; its items 1–5 hash equal to this brief's copy (2373155c…c185 both).
73. T3:26–27, §2 is the report: 113 lines, e5bffcd5…4724. CONFIRMED (byte-equal).
74. T3:26, extracted by `jq` from the hand-back. NOT CHECKABLE.
75. T3:27, the report names scratch files only by S/ paths. CONFIRMED. There is no full local path in the report; S/ appears at review_raw.md:78.
76. T3:27–29, two hash-abbreviation "slips". IMPRECISE.
    - "e6ff066d…5d5a" is wrong: the sha256 ends …636d5a.
    - "f9d0114c…a2db4" is the correct five-character tail of …638aa2db4. It breaks the 8…4 form but gives no wrong value.
    - Replace with: "Two of its hash abbreviations depart from the first-8…last-4 form, against the full sha256s its brief gave and it checked: "f9d0114c…a2db4" carries a five-character tail (`f9d0114c…2db4`), and "e6ff066d…5d5a" is a slip for `e6ff066d…6d5a`."
77. T3:31, the totals. CONFIRMED.
78. T3:35–36, draft 2's hashes and line counts. CONFIRMED.
79. T3:38–40, F1: no raise; null; a sorted `nonfinite` list; the line's suffix; R still raises. CONFIRMED. gvec.py:222–227, :246, :257, :444–445.
80. T3:40–42, compute's print order. CONFIRMED. gvec.py:433–455.
81. T3:42–43, positions are counted by token counts, not the absence marker. CONFIRMED. gvec.py:230–233 uses `reach = nt > p`; draft 1 used ~isnan.
82. T3:43–44, the new infinite-position-0 case. CONFIRMED. gvec.py:724–736.
83. T3:45–47, F2. IMPRECISE. Two problems:
    - Wording: "on the seat's stated default (the second sitting, §1.5)" appears verbatim only in STOP_LINE. GVEC_STOP_END reads "(n §2.3; ADDENDUM-n1 §6.1; the second sitting, §1.5)". The module docstring says "goes to the PI". choose_site's docstring lacks "with the diagnostic block".
    - Pinning: STOP_LINE is pinned only for "for the PI" and "§1.5" (gvec.py:924). GVEC_STOP_END is only compared with itself (n_sessions.py:2441).
    - Replace with: "**F2** (NIT), applied: the STOP's printed lines (`gvec.STOP_LINE`; the driver's `GVEC_STOP_END`) and the docstrings now send the STOP to the PI, with the diagnostic block, on the seat's stated default (the second sitting, §1.5). The self-test checks each line printed (`STOP_LINE` last of `compute`'s lines on a STOP, `GVEC_STOP_END` last of the driver's) and pins "for the PI" and "§1.5" in `STOP_LINE`'s text; `GVEC_STOP_END`'s words are checked only against the constant itself."
84. T3:48–49, F3. CONFIRMED. n_sessions.py:2179–2180, :2452–2453.
85. T3:50, F4 and F5 "applied as the reviewer wrote them". IMPRECISE. F4 is verbatim (gvec.py:422). F5 is reworded: directions.py:68–69 reads "for R, G-VEC passes the sums and counts over positions 1..n (``passage_rows``); for the diagnostic block's R_all, every position's". Replace with: "**F4**, **F5** (NIT), applied: F4 in the reviewer's words; F5 in its substance, in the docstring's own sentence."
86. T3:51–53, F6. CONFIRMED. gvec.py:84–86; n_sessions.py:146–149.
87. T3:54–55, F7. CONFIRMED. gvec.py:748–753.
88. T3:56–57, F8. CONFIRMED. gvec.py:35–38.
89. T3:58, M1. CONFIRMED. gvec.py:760.
90. T3:58–60, M2 and M3 (position 0 ×0.01, last row ×50, checked against a computation apart). CONFIRMED. gvec.py:708–722.
91. T3:60, M4. CONFIRMED. gvec.py:661–663.
92. T3:60–61, M5. CONFIRMED. gvec.py:656–660.
93. T3:61, M6. CONFIRMED. directions.py:139.
94. T3:62–63, the B1/B2/B3 dispositions. CONFIRMED as against the report (review_raw.md:135–149); see observation 3.
95. T3:64, O1–O6, O8 and O9 ask for nothing in the code; O1 and O6 give the read its checks. CONFIRMED. review_raw.md:152–180.
96. T3:65–66, O7 is applied and the refusals gain the case. CONFIRMED. n_sessions.py:2205–2208, :2489–2490, :2536–2537.
97. T3:67–68, `neutral_tokens_in_R` is the seat's §1.2 item, no longer a reading. CONFIRMED. gvec.py:76–77; it is absent from :79–86, where draft 1 listed it. The coordinating session's point itself is not in my sources.
98. T3:68–69, "`n_by_position` is a count beside each §1.3 figure". IMPRECISE, as item 32. Replace with: "`n_by_position` is a count beside each `rms_by_position` figure, not a figure."
99. T3:70, the reviewer's departures are in the entry. CONFIRMED. T1:51–53.

T4, the dated note
100. T4:1–3, 355e3a2's entry names data/n/gvec/gvec.json, sha256 3331da71…ee95, status STOP. CONFIRMED. RESULTS.md:390, :493; shasum; gvec.json:194.
101. T4:1–5, the gvec commit (its entry at the Log's head) moves it byte for byte, on the coordinating session's word. NOT CHECKABLE (a plan).
102. T4:5–6, G7 and the out-folder refusal. CONFIRMED. n_sessions.py:2160–2161; gvec.py:58.
103. T4:6–7, "From that commit on … is the path of the re-run's record". NOT CHECKABLE (prospective; see observation 5).
104. T4:7–8, the sha256 identifies the record where those texts name the old path. CONFIRMED where checked: the entry (RESULTS.md:390), the out raw (:123) and the seat's answers (:3) each give 3331da71…. The STOP block is not among my sources.

TOTALS: 104 items. 84 CONFIRMED, 7 IMPRECISE, 0 FAIL, 13 NOT CHECKABLE.

OBSERVATIONS
1. GVEC_STOP_END's words are pinned by no check: n_sessions.py:2441 compares the printed line only with the constant, so a one-word change survives. If T3's "pinned" should stand as written, the driver's STOP check would need clauses such as "for the PI", "with the diagnostic block" and "§1.5" in GVEC_STOP_END. That is a code change, so new hashes and a re-run; otherwise use item 83's wording.
2. The source of items 32 and 98 is draft 2 gvec.py:80 ("beside each diagnostic figure, its token count"). diagnostic_at's own docstring (:213–214) has it right ("the token count of each" rms figure). If the bytes stay, :80 is wording owed at the module's next change.
3. F1's closure covers the descriptive figures only.
   - A non-finite R or rel still raises at gvec.py:444–445 (declared: "R stays a raise"). That ends the run with no record, after the token, count and R lines print.
   - In the smoke, the record is written with allow_nan=False (n_sessions.py:2259) before the SMOKE R lines print (:2261–2263). A non-finite smoke R would end the smoke with no R line at all.
   - T3:62's "now closed" could add "for the descriptive figures; R stays a raise, declared".
4. T1:35–36, "which no passage of record meets", reads oddly. gvec.py:82's wording ("no passage of record is that short, the shortest having 35 tokens") is clearer.
5. T4:6–7: nothing sits at data/n/gvec/gvec.json until the re-run writes it. "is free for the re-run's record" states what is true at the commit.
6. T3:14–16: in the review brief, "Check every claim of the new wording … against those texts" (:36–37) covers its item 2's texts: the first sitting's answers and the "Wording owed" bullet. The second sitting's answers are its item 1, what the delta must do. T3's relative clause reads as covering all three.
7. The placeholders @VCDEP@ (T1:54) and @VC@ (T1:55) remain to be filled.
8. No line in the code declares the pre-load refusal (O7) as a reading for the seat; run_gvec's docstring only states it. If it is one, a docstring clause would declare it, as was done for F6's items.

DEPARTURES
- One `git log --format='%h %s' 516b60f..HEAD -- valence_core/n`, piped to cut. Its pathspec was a named non-data folder, not item 3's form with the mf3 exclusion. It printed nothing (no commits). I read the brief's parenthetical as allowing it; stated for the seat.
- Three `git check-ignore -v` runs, the brief's own instrument:
  - on results/raw/2026-11-19_n-gvec-v1_gvec.json, without `--no-index`;
  - on the same path, with `--no-index`;
  - on the two new raw paths.
  Item 1 of the list of record names `git check-attr`, not `git check-ignore`. Each printed nothing, exit 1.
- One zsh-form loop for the package digest was refused by the harness's safety check and ran nothing. I recomputed with a POSIX `while read` loop.
- Not barred by my reading:
  - `git rev-parse HEAD`.
  - Reads beyond the named sources: valence_core/m/resume.py:320–364 (the form the brief cites); RESULTS.md beyond the two named entries (lines 107–376, for the 545 and 556 figures); `git diff --name-only 516b60f HEAD` with item 3's pathspec and the exclusion.
  - `cut`, `tr`, `od`, `head`, `tail`, `wc -l` and `cmp` on printed lines or named files.
- Otherwise none:
  - no interpreter but shasum, no file written, no network;
  - no guard marker in any argv;
  - nothing under data/mf3, data/*/ckpt or data/*/reports read, listed, sized or timed, and no whole-tree git status;
  - in S, only the brief and the named files (selftest_run1.exit and selftest_run2.exit read as the brief's ".exit").
