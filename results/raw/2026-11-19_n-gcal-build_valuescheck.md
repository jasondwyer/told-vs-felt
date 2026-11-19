# n — G-CAL-n's BUILD: the blind values-check of its texts, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the BUILD's four texts, with draft 3's files beside them:
- T1, the self-test raw, `cdd878cb…eec4` (56 lines);
- T2, the review raw, `9cde7535…75b1` (329 lines): its head and dispositions, and its §2 against the report;
- T3, the entry before its values-check bullet, `609ef824…a91f` (86 lines);
- T4, the commit message, `bc5ef7f9…0b63` (3 lines), its two values-check placeholders marked not to be checked.

**The checker's brief** (`a2763e8b…bafa`, 103 lines, given to the checker as a file, with its sha256 to verify):
- named the texts; the BUILD, draft 3's five files and the `.gitignore` by sha256; and the sources. In Code's scratch
  these were, by name and sha256 only, the earlier drafts, the self-test outputs, the review's brief and report, the
  reviewed `.gitignore` draft and Code's departure note. In the overlay it allowed one pruned count of its files, and
  `cmp` of its named files against draft 3's. In the repository it gave `d7d5e5b`;
- allowed the n package's digest to be recomputed in the shell, with no interpreter, in `package_sha256_of`'s form;
- asked for every factual claim to be checked: each hash, count and citation; what the code does and the earlier
  drafts were; the review's figures and each disposition against draft 3; the readings and the declared departures;
  each listed departure against its source. Plans were to be marked NOT CHECKABLE;
- allowed `shasum` by name (on this machine a Perl script, which the list of record's item 1 permits), and barred any
  other interpreter, any write, any network, any guard marker in an argv (a grep pattern included), anything under
  `data/mf3`, any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the named
  files and the brief itself;
- quoted the list of record v2's items 1–5, verbatim; required item 3's pathspec and the `data/mf3` exclusion on every
  git command over the tree, with `.` as the include for `git ls-files`, that a glob is expanded and read before it is
  looped over, and the `rev-parse` form for a tracked-and-clean check.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (159 lines, sha256
`a4823a0b…2340`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 128 items: 106 CONFIRMED, 7 IMPRECISE, 1 FAIL, 14 NOT CHECKABLE; and 9 observations.

**The checker's departure,** as its report states it, is in the entry's departures, for the seat to class.

## 1. Dispositions

- **The FAIL** (72) **and the IMPRECISE items** (24, 29, 65, 73, 89, 111 and 112), each applied in the checker's words
  or near them.
- **The NOT CHECKABLE items** stand: plans, acts recorded in no file, and what the pruned count cannot see.
- **The observations:**
  1. and 2. Declared in the entry as wording owed at each file's next change: the driver's docstring for the `gcal`
     command (GC1–GC22, and the failed-run folder left out of its refusals), and `gcal.py`'s "on every end". Draft 3's
     self-tested bytes stay the BUILD's, as at G-VEC's own owed wording.
  3. Not applied: the mid-run check's count could be pinned from the run's own turns. That is for the driver's next
     change; the self-test raw words the check to what it asserts (item 24).
  4. Applied: the self-test raw names `d7d5e5b`'s versions, the same bytes at `99196e1` and `1185e15`.
  5. Applied: the entry lists the `.gitignore` block's blank line last, as G-VEC's entry did.
  6. Applied: the entry says GC23 is stated in the supplement's §1 and its routing quoted in its §5.
  7. Applied: the review raw lists the two bars it had left out.
  8. Applied: the build's step, the adapter's own uncached forward, is declared in the entry as departure (9) from
     GC9's words, and owed to `gcal.py`'s docstring at its next change.
  9. Applied: B2's disposition says which stop counts are printed and which are recorded.

## 2. The texts changed after the check, and the edits checked by tool

- **The texts changed after the check** by the dispositions above. The entry also changed by its values-check bullet,
  the checker's departure, and Code's note of the BUILD's first commit window, whose gate failed.
- **The edits, checked by tool:** a fixed-string search over the unwrapped final texts, each edit's new wording present
  and the wording it replaced absent, 31 of 31.
- **The finals:** the self-test raw `4a112625…23d9`, the review raw `47756de0…80e3`, the entry `3ef78c1d…5989`.

## 3. The report as returned

```text
VALUES-CHECK: G-CAL-n's BUILD texts (T1–T4), against draft 3, the earlier drafts, the review and the repository at d7d5e5b

Preliminaries. The brief's sha256 matched (a2763e8b…abfa). Every named S file matched its stated sha256: T1 cdd878cb…eec4 (56 lines), T2 9cde7535…75b1 (329 lines), T3 609ef824…af20a91f (86 lines), T4 bc5ef7f9…0b63 (3 lines; it states no hash of its own). Draft 3's five files and S/step4b/gcal/commit/gitignore_v2 matched, and so did the four earlier-draft files, S/step4b/gcal/review_brief.md (406f111d…488b), S/step4b/gcal/review_report.md (75d4200f…cd5e) and S/step4b/gcal/commit/gitignore (e1e73d76…6408). S/step4b/gcal/departures_code.txt is 178e3ed5…71d8. HEAD is d7d5e5b. Before any delta was taken, each changed path (scripts/n_sessions.py, valence_core/n/ids.py, keys.py, guard.py, .gitignore) was checked tracked and clean (rev-parse HEAD:<path> = hash-object). Each path's blob is the same at da7bdec, 1185e15, 99196e1 and d7d5e5b. Every hash and abbreviation in T1–T4 was matched by tool against the computed full sha256s (cut first 8 … last 4). None of them is stray.

ITEMS

T1 (S/step4b/gcal/build/selftest.txt)
1. T1:1–2. Refs: n v0.2 s8 step 8, the G-CAL-n paragraph of n s3, ADDENDUM-n1 s1.1, s1.2 (v) and s1.4. CONFIRMED. PROPOSAL-n-bk-reconciliation-v0_2.md:159 reads "7. G-VEC. 8. G-CAL-n. 9. G-ANL-n". n:113 sits in §3 (:105–123). The ADDENDUM-n1 sections are at :20, :22 ((v) gcal_prompts.jsonl) and :26.
2. T1:4. "On 99196e1's versions of these paths (each the same bytes at 1185e15)." CONFIRMED by blob ids, and the same at d7d5e5b (see O4).
3. T1:5. gcal.py aba3700c… is new and 738 lines. CONFIRMED by shasum, `wc -l` 738, and no HEAD:valence_core/n/gcal.py.
4. T1:6. n_sessions.py 37b8268d… (+948 −5). CONFIRMED (`git diff --no-index --numstat` gives 948 5).
5. T1:7. ids.py cc614c75… (+254 −15). CONFIRMED (254 15).
6. T1:8. keys.py 6a0f9ad3… (+28 −1). CONFIRMED (28 1).
7. T1:9. guard.py ef3a7e5b… (+1 −1). CONFIRMED (1 1).
8. T1:10–12. The digest moves 882c9217…5ca7 → 8f785fba…0152. CONFIRMED. I recomputed both in the shell in package_sha256_of's form (valence_core/m/resume.py:328–350: path, newline, byte count, newline, bytes, in path order). HEAD's 15 clean valence_core/n/*.py give 882c9217cc3f…55ca7. The same set with draft 3's gcal.py, guard.py, ids.py and keys.py gives 8f785fba0fa8…0152. The overlay's 16 files also give 8f785fba…0152.
9. T1:11. "(da7bdec's, unchanged at 99196e1)." CONFIRMED. `git diff --name-only` da7bdec..1185e15 touches only scripts/n_analyze.py, RESULTS.md and raws. 1185e15..d7d5e5b touches only RESULTS.md and five raws.
10. T1:13–14. Both digests are by shell in that form, and HEAD's clean files reproduce the first, "as da7bdec's entry records it". CONFIRMED. RESULTS.md:292 (`git show da7bdec:RESULTS.md` :37) records "`f09898ee…b8f9` to `882c9217…5ca7`".
11. T1:14. "The self-test prints no digest." CONFIRMED. Each run's output is the one count line.
12. T1:14–15. `hashes` runs when the launch files are made. NOT CHECKABLE (a plan).
13. T1:17–19. The HF cases run only where torch and transformers are present, are otherwise skipped and counted, and the schema module's cases are one line. CONFIRMED. hftiny.available() imports both (valence_core/n/hftiny.py:27–33), and its skip line is at :55–57. The vanilla branch is at scripts/n_sessions.py:1490 (draft 3 :1516). G-CAL-n's branch, draft 3 n_sessions.py:3427–3450, has one chk each way. The schema's single chk is at scripts/n_sessions.py:215–216.
14. T1:20–22. The overlay has 161 files: 1185e15's 160 on G-VEC's self-test paths (that raw lists them), four files replaced and gcal.py added. CONFIRMED. The brief's pruned find gives 161. `git ls-files` under item 3's and mf3's exclusions, filtered to the paths at results/raw/2026-11-19_n-gvec-build_selftest.txt:20–23, gives 158 outside the model folder. With that folder's two files (S/step4b/gcal/departures_code.txt:3) the total is 160. By cmp, the overlay's gcal.py, ids.py, keys.py, guard.py and scripts/n_sessions.py are draft 3's, and its other twelve valence_core/n/*.py are the repository's.
15. T1:20–21. The archive's method, and "so that no checkpoint or report file entered it". NOT CHECKABLE: the pruned count cannot see such files.
16. T1:23–28. The command, the battery windows, the re-hash before each run, and the empty temporary folder. NOT CHECKABLE.
17. T1:30–33. Run 1 is draft 1 be63ef41…1f5e and 5258bcfc…6a02 ("the bytes the blind review read"), with ids.py, keys.py and guard.py as above. CONFIRMED. The hashes match. S/step4b/gcal/review_brief.md:10–16 gives the same hashes, its keys, ids and guard equal to draft 3's. The report's first paragraph says all eight files matched.
18. T1:33–35. Run 1: exit 0, output b91e86ed…fe22, 524/524, indented five spaces. CONFIRMED. selftest_run1.exit reads "exit 0" and the sha matches. The output has two leading spaces and T1:35 has seven (od -c). The code agrees: 462 + gcal 24 + keys 3 + ids 19 + driver 16 = 524.
19. T1:37. Draft 2 applies the findings, all but F1. CONFIRMED. Draft 2's driver holds same_g, gcal.GENERATION_WINDOW, prompt_template, flags_differ, foreign_d, RecordingAdapter and cases x39–x45, x14b and x14c, none of them in draft 1. It has no OUT_PARTIAL and no .gcal.failed, and still rmtree's the staging folder.
20. T1:37–39. Twelve checks more: nine in gcal's own, and three in the driver's (committed_bytes, the HF seams over a recording stand-in, the hftiny skip line). CONFIRMED. gcal.py chk lines go 24 → 33. The driver goes 139 → 143 lines: committed_bytes, RecordingAdapter, and the hftiny if/else (two lines, one executed).
21. T1:40–44. Run 2 hashes 5cd43ea0…fdaf and 34c5f037…bee5, exit 0, output b8ddd286…b8b8, 536/536. CONFIRMED. The total is consistent: 462 + 33 + 3 + 19 + 19 = 536. Draft 2's own ids, keys and guard copies are not named in this brief.
22. T1:46–47. Draft 3 is draft 2 with GC23 (a)–(d), as the coordinating session routed it. CONFIRMED by the draft 2→3 diffs and the supplement §5 (results/raw/2026-11-19_n-starred-eleven-supplement_code-to-design_STOP.md:134–151).
23. T1:47–48. The two new checks in gcal's own: the order of generation with each turn handed on, and the log's line form. CONFIRMED: gcal.py:630–649, chk lines 33 → 35.
24. T1:48–49. The two new checks in the driver's: "a failure mid-run, whose failed-run folder must hold exactly the turns generated before it, and a non-finite arrival, whose folder must hold all 192". IMPRECISE. The mid-run check (draft 3 n_sessions.py:3152–3170) asserts len(logged) >= 1, the log a prefix of the order of generation, and each logged turn the run of record's own with arrival None. It never asserts the count generated before the 61st forward. The 192 check (:3171–3182) is exact. Replace with: "two in the driver's: a failure mid-run, whose failed-run folder's log must hold the turns generated before it as a non-empty prefix of the order of generation, each the run of record's own turn, and a non-finite arrival, whose folder's log must hold all 192".
25. T1:49–51. Run 3: exit 0, output 84c5abf2…0a3c, 540/540. CONFIRMED (selftest_run3.exit "exit 0"; sha; content; 462 + 35 + 3 + 19 + 21 = 540).
26. T1:53. "The box has not run this BUILD." NOT CHECKABLE.
27. T1:53–55. The box count of 551 is 540 + 11, the 13 HF checks in place of two skip lines as at da7bdec's entry, and G-CAL-n's HF line adds nothing. CONFIRMED. `git show da7bdec:RESULTS.md` :47 reads "473, the 462 plus the box's 11 checks more (its 13 HF checks in place of the laptop's two skip lines)". hftiny.py is unchanged (overlay cmp), and G-CAL-n's branch has one chk at either site.
28. T1:56. "G-CAL-n's launch files restate the count." NOT CHECKABLE.

T2 (S/step4b/gcal/build/review.md)
29. T2:5–6. "…from HEAD `1185e15`". IMPRECISE. That is the brief's HEAD (review_brief.md:7), but the report's O1 (T2:253–256) found HEAD at 99196e1, with the five FROM files unchanged. Replace with: "…from the brief's HEAD `1185e15` (HEAD was `99196e1` when it ran, the five FROM files the same bytes: the report's O1):".
30. T2:7. gcal.py is new, be63ef41…1f5e, 519 lines, read in full. CONFIRMED (`wc -l` 519; review_brief.md:10–11).
31. T2:8–9. The four deltas' hashes. CONFIRMED (review_brief.md:13–16).
32. T2:10. The .gitignore draft e1e73d76…6408 is HEAD's with one block. CONFIRMED (numstat 10 0 against HEAD's).
33. T2:11. Draft 1's 524/524 ran before the brief went out. CONFIRMED (review_brief.md:20–21).
34. T2:13. The brief is 406f111d…488b, 86 lines. CONFIRMED (`wc -l` 86).
35. T2:14–23. The brief's contents. CONFIRMED: files and diff form at :9–19, the specification at :25–37, the code at :38–44, the two known departures at :45–47, the report form at :49–60, the bars at :64–80. Its items 1–5 (:82–86) are byte-equal (2373155c…c185) to results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md:18–22 and to this brief's copy (see O7).
36. T2:25. §2 is the report: 221 lines, 75d4200f…cd5e. CONFIRMED. `sed -n '108,328p'` of T2 hashes to the report file's sha, and the file has 221 lines. The jq extraction itself is not checkable.
37. T2:25–26. "It names no local path." CONFIRMED (/usr/bin/grep -E for /Users/, /private/, /tmp/ and /home/ finds 0).
38. T2:26–27. Its line numbers are draft 1's, which Code's scratch keeps unchanged. CONFIRMED (draft 1's hashes match).
39. T2:29–30. Totals: 0 BUG, 12 findings (5 RISK, 6 NIT, 1 NIT/RISK), 16 mutants, 6 box risks, 13 observations, 3 departures. CONFIRMED by counting the report: F1–F4 and F9 are RISK; F5–F7 and F10–F12 are NIT; F8 is NIT/RISK.
40. T2:34–35. Draft 2: every finding but F1; gcal.py 5cd43ea0…fdaf (685 lines) and n_sessions.py 34c5f037…bee5; keys, ids and guard draft 1's; 536/536. CONFIRMED (see items 19–21).
41. T2:35–37. Draft 3 adds F1 as GC23, routed as a PIN declared in the BUILD entry; aba3700c…a3a0 (738 lines) and 37b8268d…f030; 540/540; the BUILD's bytes. CONFIRMED (supplement :136 and :150).
42. T2:37–38. The .gitignore block is the reviewed draft's, its comment naming the failed-run folder too (908f447b…2f2c). CONFIRMED. The diff between the two drafts is that one comment line.
43. T2:41–42. F1 is applied as GC23 and goes to the seat before the run (Q12). CONFIRMED (supplement :28 and :124–127).
44. T2:43. F1 (a). CONFIRMED. gcal.append_turn writes, flushes and fsyncs (gcal.py:405–412). compute hands each row to on_turn as it is made (:365–366). The driver logs to stage/gcal_turns.partial.jsonl (draft 3 n_sessions.py:2803–2808).
45. T2:44–45. F1 (b). CONFIRMED. `except BaseException` does os.replace(stage, failed) and nothing removes it (:2812–2818). The run refuses while the failed folder exists (:2721–2724).
46. T2:46. F1 (c). CONFIRMED (arrival_score raises, gcal.py:277–278; the driver's nanarr check asserts all 192 kept).
47. T2:47. F1 (d). CONFIRMED (GENERATION_ORDER at gcal.py:126; the generation loop sorts by it at :349; the result keeps the batches' order).
48. T2:48–49. F2. CONFIRMED (gcal.py:554–568).
49. T2:50–52. F3. CONFIRMED (gcal.py:601–612).
50. T2:53–55. F4. CONFIRMED (gcal.py:669–672 pins seven constants; :673–695 checks each bar from both sides).
51. T2:56–58. F5. CONFIRMED (gcal.py:15–23, 134–140, 704–707).
52. T2:59–60. F6. CONFIRMED (gcal.py:77–83; T3:59–67; the hftiny check at n_sessions.py:3427–3449).
53. T2:61–63. F7. CONFIRMED (gcal.py:120 and 182–184; run_gcal's window refusal before the load; the provenance holds generation_window and longest_forward, the constants hold generation_window).
54. T2:64–65. F8. CONFIRMED (gcal_prompts_check at :2660–2686; cases x14b and x14c).
55. T2:66–68. F9. CONFIRMED (gcal_decode_compare and cmd_gcal_decode).
56. T2:69–70. F10. CONFIRMED (gcal.py:294–307 and 288–291; stops recorded for every batch at :381).
57. T2:71–72. F11. CONFIRMED (the parse sits inside the try; except (schema.SchemaError, ValueError) at :2762; cases x42–x45 are new in draft 2).
58. T2:73–74. F12. CONFIRMED (foreign_g has 9 flags, foreign_d 10, plus the other argvs).
59. T2:77. M1–M5. CONFIRMED by reasoning on draft 3's checks. M1 makes log_e ≠ [3,4,5]. M2 makes log_c ≠ [3,4,5,6]. M3 and M4 break the baseline and +ρ equalities. M5 breaks the t re-derivation.
60. T2:78. M6–M11. CONFIRMED. The single-score case kills M6. k36, hi, four, nine and low kill M7–M11.
61. T2:79–80. M12. CONFIRMED (the RecordingAdapter's call equality; on the box the hftiny ls_t ≠ lu_t check and steering_check).
62. T2:81. M13–M15. CONFIRMED (absent-selftest.json; x39; x32, x40 and x41, one per clause).
63. T2:82–83. M16 and the sampler mutant. CONFIRMED (all nine flags; gcal.py:459–471).
64. T2:86–87. B1. CONFIRMED (:3369–3383: CUBLAS ":16:8", RUNPOD_POD_ID popped, same_g asserted; ":16:8" is not the characterized ":4096:8").
65. T2:88–89. B2, "…and each batch's stops are printed". IMPRECISE. The batch line with stop counts prints only at d ≠ 0 (gcal.py:383–387). The baseline's counts are recorded only (figures.baseline.stops), and every turn's stop is on its turn line. Replace with: "- B2: applied. A steering check runs before each batch at a positive dose (the smoke's +ρ included), and each steered batch's stop counts (eos, cap, empty) are printed on its batch line; the baseline's are recorded in the figures, and every turn's stop is printed on its turn line."
66. T2:90. B3, B4 and O13 go to the launch files, as routed. CONFIRMED (supplement :144).
67. T2:91. B5 is F9 and B6 is F1. CONFIRMED.
68. T2:94–96. O1 and O2 noted; O3, O5 and O6 in the supplement §2; O7, O8 and O12 in §3. CONFIRMED (supplement :87–106 and :108–120).
69. T2:97. O4 and O9 applied. CONFIRMED (the exact-draws check; departure (5); exposure "draws" at gcal.py:390–391).
70. T2:98. O10 and O11 go to (v)'s render commit. NOT CHECKABLE (a plan).
71. T2:100. The BUILD entry carries the departures. CONFIRMED (T3:73–75; supplement :146).
72. T2:101. "it read `valence_core/n/runner.py:270–309` and grepped runner.py and schema.py, neither in the brief's list". FAIL. schema.py is in the brief's list (review_brief.md:38). The report's "Neither file" means runner.py and primitive.py, and the `wc -l` over both is dropped (T2:320). Replace with: "- it read `valence_core/n/runner.py:270–309`, grepped runner.py and schema.py once, and ran `wc -l` over runner.py and primitive.py; runner.py and primitive.py are not in the brief's list (schema.py is);"
73. T2:102. "…printing lines outside the reader the brief named". IMPRECISE. The brief named the `--dose-map` reader and DoseMap (review_brief.md:39), and the report says lines fell outside both (T2:321). Replace with: "- it grepped all of `scripts/n_analyze.py` once, printing lines outside the `--dose-map` reader and DoseMap, which the brief named;"
74. T2:103. The tool-results read. CONFIRMED (T2:322).

T3 (S/step4b/gcal/build/entry.md)
75. T3:1–3. The title, refs, the module, and the commands gcal, gcal-decode and render-ids-v on GC1–GC23 as routed. CONFIRMED (main() choices at draft 3 n_sessions.py:3457–3458; spec raw :79; supplement §5).
76. T3:4. "Nothing has run on the box." NOT CHECKABLE.
77. T3:4–5. The run waits for the twelve, G-VEC's committed PASS, (v)'s render and the PI's word. CONFIRMED. The starred-eleven raw says so at :242–243, and the supplement's :34 reads "all twelve answers". The code refuses without (v) (gcal_prompts_check) and without a committed G-VEC PASS (gcal_gvec_inputs).
78. T3:7. Six paths, against d7d5e5b's numstat. CONFIRMED.
79. T3:8–12. The five code paths' abbreviations and numstats. CONFIRMED (items 3–7).
80. T3:13–14. .gitignore 908f447b…2f2c (+10): a blank line, a four-line comment, the folder admitted, its contents ignored, three admits; the staging and failed folders stay ignored. CONFIRMED. The block is 1 + 4 + 1 + 1 + 3 lines. .gitignore:263's /data/n/* still covers .gcal.staging and .gcal.failed. The line order is covered in O5.
81. T3:15–16. The digest move, by shell, with HEAD reproducing 882c9217…5ca7. CONFIRMED (item 8).
82. T3:16–17. "Neither has yet been printed by the package's own `hashes`…" NOT CHECKABLE. RESULTS.md holds 882c9217 only in da7bdec's entry.
83. T3:18–20. 540/540 after 524/524 and 536/536, and 551 on the box. CONFIRMED (items 18, 21, 25, 27). The raw's link target is a path still to be created.
84. T3:21–22. No weights were used; battery windows; nice -n 19. NOT CHECKABLE (T1:25 shows nice -n 19).
85. T3:23–26. Review totals, every finding applied (F1 as GC23), each mutant meeting a check, B3, B4 and O13 to the launch files. CONFIRMED (items 39, 43–63, 66).
86. T3:27–28. Specification sources: GC1–GC22 and the routing verbatim in the spec raw (99196e1); GC23 and its routing in the supplement (d7d5e5b). CONFIRMED (spec raw §1 at :29–74 and §2 at :76–88; supplement §1 and §5). Wording is covered in O6.
87. T3:29. "Given in full in the module's and the driver's docstrings." CONFIRMED with O1: the driver's command block is stale.
88. T3:31–32. Refusals: out, staging or failed folder; pod; cuBLAS; stream known answer; weights; driver for a run of record. CONFIRMED (run_gcal :2706–2745; weights_of_record at scripts/n_sessions.py:554–566).
89. T3:33–34. "…each the plan's prompt, its two texts' sha256s and the v block's template `gcal.prompt_parts`', its ids re-derived, and `gen_start` the user turn's count;" IMPRECISE. The check (:2678–2685) compares user_sha256 = sha256(user turn) and text_sha256 = sha256(user turn + generation prompt). It re-derives ids_sha from the ids, and the box encodes nothing. Replace with: "- the ids of record and (v)'s 48 prompts: each the plan's prompt, its user turn's and whole text's sha256s and the v block's template `gcal.prompt_parts`', its `ids_sha` re-derived from its ids, and `gen_start` the user turn's count;"
90. T3:35–36. The generation window, 4,096. CONFIRMED (gcal.py:120 and 182–184; schema.MAX_WINDOW 4096).
91. T3:37–38. G-VEC's outputs. CONFIRMED (:2621–2657).
92. T3:39. The dose map with a fold into 0 refused, and the R6 bridge. CONFIRMED (valence_core/n/schema.py:772 raises SchemaError, caught at :2762; the bridge check precedes the load).
93. T3:40–41. Refusals after the load. CONFIRMED (they precede stage.mkdir; the self-test asserts nothing is written).
94. T3:42–45. Generation: 4×48 turns, ids-in, uncached, TEMP 0.7, cap 80, eos stop; d·ρ·R·v from gen_start; order +ρ, +ρ/2, baseline, −ρ; record in n:113's order; a steering check before each positive dose; each turn logged. CONFIRMED (gcal.py:105–126, 177–206, 330–369; the adapter's forward uses use_cache=False and returns the last position's logits, valence_core/adapters/olmo_hf.py:170–188).
95. T3:46–48. Hurdles at every dose; STOP exits 2, PAUSE 3, PASS 0 with the map pinnable. CONFIRMED (gcal.py:294–316; run_gcal's returns; write's pinnable).
96. T3:49–50. Outputs through .gcal.staging; .gcal.failed on a failure. CONFIRMED.
97. T3:51–52. `--smoke` 1..4. CONFIRMED (GCAL_SMOKE_MAX 4; SMOKE_BATCHES; out outside the repository).
98. T3:53–54. gcal-decode. CONFIRMED.
99. T3:55–56. render-ids-v writes outside the repository, and the manifest of record is unchanged. CONFIRMED. cmd_render_ids_v refuses an in-repository out. MANIFEST_OF_RECORD is fdf73d85… in both HEAD's ids.py:74 and draft 3's :86. The future commit itself is a plan.
100. T3:57–58. The starred eight (seven in 99196e1, GC23 in d7d5e5b); GC1 and GC2 on the list; GC14 a PAUSE. CONFIRMED (spec raw :79; starred-eleven raw :249–254; supplement :124–127).
101. T3:60. Departure (1). CONFIRMED (gcal.py:74–75, 255–264, 300).
102. T3:61. Departure (2). CONFIRMED (gcal.py:75–76, 271–272, 298).
103. T3:62. Departure (3). CONFIRMED (gcal.py:77, 223–229; GC11's words at spec raw :47).
104. T3:63. Departure (4), against GC2's "the record alone". CONFIRMED (spec raw :38; write runs on every status).
105. T3:64. Departure (5), against GC9's "mirrors the adapter's". CONFIRMED (spec raw :45; gcal.py:168–174). See O8.
106. T3:65. Departure (6), against GC15's order. CONFIRMED (spec raw :55; "dose map:" prints at :2768, before make_adapter at :2787).
107. T3:66. Departure (7), against GC19's 2 prompts. CONFIRMED (spec raw :59).
108. T3:67. Departure (8), GC21. CONFIRMED (spec raw :61; testing.py unchanged by overlay cmp; gcal.py:459–471).
109. T3:68. "Nothing ran on a model." NOT CHECKABLE.
110. T3:70–72. Code's ls departure. CONFIRMED (S/step4b/gcal/departures_code.txt:1–5).
111. T3:73–74. "it read `valence_core/n/runner.py` and grepped runner.py and schema.py, outside the brief's list". IMPRECISE. schema.py is in the brief's list, and the `wc -l` over runner.py and primitive.py is omitted. Replace with: "it read `valence_core/n/runner.py`, grepped runner.py and schema.py, and ran `wc -l` over runner.py and primitive.py, the two files outside the brief's list;"
112. T3:74–75. "…once beyond the reader named". IMPRECISE (same as item 73). Replace with: "it grepped `scripts/n_analyze.py` once beyond the `--dose-map` reader and DoseMap the brief named;"
113. T3:75. The tool-results read. CONFIRMED.
114. T3:76–78. The survey's three departures. CONFIRMED (spec raw :455–457, and its head at :17; starred-eleven raw :255–256).
115. T3:79–81. Committed by path. NOT CHECKABLE (a plan).
116. T3:83. The home-folder count is 0. NOT CHECKABLE at this point. A precheck finds 0 local-path matches in T1–T4 and in all six BUILD files.
117. T3:83–85. Not pushed, and the Next list. NOT CHECKABLE (plans). Only "its launch files held for the PI's answer on its run order" is on record (supplement :9–10).

T4 (S/step4b/gcal/build/commit_msg_src.txt)
118. T4 has 3 lines (the message, a blank, the attribution). CONFIRMED.
119. T4:1. Refs, module, commands, hashes and numstats. CONFIRMED (items 1–7, 75).
120. T4:1. ids.py is the (v) render and load, keys.py G-CAL-n's seeds, guard.py gcal in PRODUCTION, .gitignore +10 with the three admits and the folders ignored. CONFIRMED (the diffs: render_v, _FORMS and load; gcal_key and gcal_seed; PRODUCTION gains "gcal").
121. T4:1. GC1–GC23 as PINs; the starred eight, seven in 99196e1 and GC23 in d7d5e5b. CONFIRMED.
122. T4:1. The stage summary. CONFIRMED (items 92–96).
123. T4:1. The digest move by shell. CONFIRMED.
124. T4:1. The self-test counts and 551. CONFIRMED. The battery windows are not checkable.
125. T4:1. The review summary. CONFIRMED.
126. T4:1. The departures list. CONFIRMED (items 110–114).
127. T4:1. Committed by path, the home-folder count, nothing on a model, not pushed, Next. NOT CHECKABLE.
128. T4:3. The attribution line. CONFIRMED (it matches the session's line).

TOTALS: 128 items. 106 CONFIRMED, 7 IMPRECISE (24, 29, 65, 73, 89, 111, 112), 1 FAIL (72), 14 NOT CHECKABLE.

OBSERVATIONS
1. Draft 3's driver docstring, in the gcal command block at scripts/n_sessions.py:155–159, is stale in two places. It still says "Code's readings GC1-GC22", where gcal.py:2 says GC1-GC23. Its refusal list ("the out folder and its staging folder, the pod, …") omits the failed-run folder that run_gcal refuses (:2721–2724) and keeps (:2812–2818). Suggest "GC1-GC23" and "the out folder, its staging folder and its failed-run folder".
2. gcal.py:66 says the outputs are "renamed into data/n/gcal/ by the driver, on every end". A failure renames the folder to data/n/.gcal.failed instead, as :70–72 say. Suggest "on every PASS, STOP and PAUSE".
3. The mid-run failure check (n_sessions.py:3152–3170) could pin the count, so that its name's "every turn generated before it" and T1's "exactly" hold as written. The count is derivable from turns1: two steering-check forwards, then n_tok + [stop == "eos"] forwards per +ρ turn, with the 61st forward failing.
4. T1:4 and T1:11 name 99196e1, but the BUILD's parent is d7d5e5b (T3:7), and the bytes are the same at all three commits. Suggest "d7d5e5b's versions of these paths (each the same bytes at 99196e1 and 1185e15)" and "unchanged at d7d5e5b".
5. T3:13 lists the blank line first. git's diff places the added blank line last, and G-VEC's entry ordered its own that way (RESULTS.md:290–291). Immaterial.
6. T3:27–28: the supplement states GC23 in its §1 and quotes only the routing verbatim (§5). Suggest "GC23 in the supplement's §1, and the coordinating session's routing of it, verbatim, in its §5 (`d7d5e5b`)".
7. T2:21–23 omits two bars the review brief also set: "no model or adapter code run" (:65) and "no whole-tree git status" (:71).
8. GC9 reads "on the unchanged adapter's hooks (primitive.HFBackend's pattern)". The build's step is the adapter's own uncached forward (n_sessions.py:2591–2596), which is G-VEC's _hf_forward pattern, not HFBackend's direct _make_hooks/_model calls. The substance holds, and the reviewer's O2 marks GC9 met, but (1)–(8) do not mention it if every departure from a reading's words is to be declared.
9. The baseline's stop counts are recorded but not printed. For the smoke entry that the review's B2 fix asks for, they come from its gcal.json (figures.baseline.stops), or the batch print could include the baseline.

DEPARTURES
1. One `cmp` loop compared the overlay's twelve unchanged valence_core/n/*.py, each named (__init__, cells, directions, gvec, hftiny, primitive, probe, runner, schema, sessions, testing, verify), against the repository's copies. The brief allows `cmp` of overlay files only with draft 3's. The same twelve files were read in full by the digest recompute the brief permits. Nothing else in the overlay was named, listed or read, and no argv held a marker.

Not departures, stated for the record. The exit files were read as S/step4b/gcal/selftest_run{1,2,3}.exit, which the brief names as "their .exit files"; the first names tried were right. results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md:18–22 was read by hash for T2's "verbatim" claim. valence_core/adapters/olmo_hf.py was read with the file-reading tool only. One shell `echo ======` failed in zsh's equals expansion and ran nothing. No interpreter but shasum ran, nothing was written, nothing used the network, and nothing under data/mf3, ckpt or reports was touched.
```
