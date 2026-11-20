# n — G-CAL-n's delta (second sitting): the blind values-check, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the drafts of the commit's three texts, as they stood at draft
2:
- T1, the RESULTS.md entry: `3dd97245…fd81` (57 lines), with its values-check paragraph and the checker's departures
  as placeholders;
- T2, the self-test raw, `results/raw/2026-11-19_n-gcal-delta2_selftest.txt` here: `ac6ffacb…9ccf` (38 lines);
- T3, the review raw, `results/raw/2026-11-19_n-gcal-delta2_review.md` here: `be63e464…82df` (266 lines).

**The checker's brief** (`ed82f6de…aae1`, 77 lines, given to the checker as a file, with its sha256 to verify):
- named the texts and the sources: in Code's scratch, by name and sha256, drafts 1 and 2 of the two files, the
  self-test's output and exit file, and the review's brief and report; in the repository, the seat's answers of both
  sittings, RESULTS.md (the gvec delta's entry, `035947e`'s entry and the coordinating session's notes entries),
  `schema.py`, `runner.py`, `gvec.py` and `directions.py`, and the package digest in `package_sha256_of`'s form over
  HEAD's blobs and with draft 2's `gcal.py` in place;
- asked for every factual claim to be checked, each numstat and count of checks among them, and for T3's §2 to be
  byte-equal to the review's report;
- barred any interpreter but `shasum`, any write, any network, any guard marker in an argv, anything under
  `data/mf3`, any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the
  named files and the brief itself;
- quoted the list of record v2's items 1–5, verbatim, and required item 3's pathspec and the `data/mf3` exclusion on
  every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (152 lines, sha256
`307b1056…4efd`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 81 items: 65 CONFIRMED, 5 IMPRECISE, 0 FAIL, 11 NOT CHECKABLE; and 7 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

- **The IMPRECISE items,** each applied in the checker's words or near them:
  - 24 (T1): the review's O6, restated as its own "should split out or drop": a pooled summary of `arrival_all` at
    the read should split those turns out or drop them;
  - 27 (T1): the self-tests' main flows reach every batch by construction, and three flows run on non-empty
    incoherent turns;
  - 50 (T2): one check, `gcal.py`'s O7 flow check, is rewritten as the early PAUSE's (O2), beside the extensions;
  - 56 (T3): the driver's rebase onto `616e940`, "+129 −54 there, by numstat", in place of "the same 181 changed
    lines";
  - 78 (T3): B3 in the review's own figures, 240 turns instead of 192, up to 3,840 more uncached forwards plus 2.
- **The NOT CHECKABLE items** stand: this session's acts and plans (19, 31, 32, 34, 40, 42, 43, 45, 52, 57). Item 13,
  "the line n-analyzer pins at v7", is replaced in T1 and T3 by §2.5's own words: the lock pins the coherence result,
  and n-analyzer's delta after G-CAL-n's run reads "the lock's line, not `gcal.json`".
- **The observations:**
  - 1 and 2, applied in the code, as draft 3: the wording owed at the driver's next change, which the seat's §3 says
    "rides with this delta" (`run_gcal`'s docstring, the `gcal` command's docstring and the exits check's name name
    the dose map beside the record and the turns; `run_gcal`'s docstring names the gate's batch and the early PAUSE),
    the exits check extended to assert the three files in each exit's folder, and the command's docstring reflowed;
  - 3: B2's second clause, the smoke running the gate's two-forward check with no turn, goes to the seat in T1, and T3's
    disposition of B2 says so;
  - 4: T1 quotes §2.5's "may be built on this raw and runs on nothing before the addendum's commit", and says the
    self-test is model-free and nothing of the delta runs on the box before ADDENDUM-n3's commit;
  - 5: T1 says the slot's "Go" is the coordinating session's reading, put to the PI;
  - 6: applied in the code, as draft 3: the driver's print-order check pins the gate's line after the exposure line;
  - 7: applied in the code, as draft 3: `gcal.py`'s docstring says "every valence dose generated", the gate's batch
    scored on coherence alone, and the shift carried by each steered valence batch's figures.
- **Draft 3** is `gcal.py` `2b99902b…a430` (+8 −8 on draft 2, its module docstring alone) and `scripts/n_sessions.py`
  `593a140d…a549` (+22 −17 on draft 2: two docstrings, one check's name and two checks extended, none added or
  removed); the self-test's run 2, 570/570; the package digest `e40c9871…9523`. The review's scope stays draft 1 → 2.

## 2. The text changed after the check, and the edits checked by tool

- **The text changed after the check** by the dispositions above; by draft 3's hashes, numstats and run 2, in T1, T2
  and T3; and in T1 by its values-check paragraph and the checker's departures, which replace the placeholders, and by
  its departures' first bullet, which now names the two extractions by `jq`.
- **The edits, checked by tool:** fixed-string counts over each text unwrapped, for each disposition's new wording
  and each removed wording's absence, and for draft 3's hashes and run 2's count in T1 and T2; T2's run-2 verbatim
  line equal to its output, T3's §2 byte-equal to the review's report, and this raw's §3 byte-equal to the
  values-check's report: 42 of 42.
- **No second full pass** was made over the texts.
- **The finals:** the entry `5633277f…9290` (81 lines); the self-test raw `12b7cd94…fc5c` (48 lines); the review raw
  `9a18cfe5…347d` (270 lines).

## 3. The report as returned

BLIND VALUES-CHECK: G-CAL-n's delta on the seat's second sitting (T1 entry, T2 self-test raw, T3 review raw)

Inputs, verified first
- Brief S/step4b/gcal2/vc_brief.md: sha256 ed82f6de…aae1, 77 lines.
- T1 3dd97245…fd81 (57 lines), T2 ac6ffacb…9ccf (38 lines) and T3 be63e464…82df (266 lines) each equal the brief's hash.
- review_report.md 44dbda82…3c30 (190 lines), review_brief.md bc23af8e…eacc, d1/gcal.py 17defa3f…21db, d1/n_sessions.py 47b12b3e…737b, d2/gcal.py 4bd8f8bf…c376 and d2/n_sessions.py 313aa240…8e96 each equal the brief's hash.
- HEAD is 616e940: the newest commit by `git log` with the pathspec.
- These repository sources are tracked and clean, checked by rev-parse against hash-object: valence_core/n/gcal.py, scripts/n_sessions.py, both answers raws, RESULTS.md, schema.py, runner.py, gvec.py, directions.py and valence_core/m/resume.py.
- Every full hash and every first-8…last-4 abbreviation in T1–T3 was matched by tool (`grep -F` against each shasum output). All are present and correct.

ITEMS

1. T1:1-3. Title, and the citation of §1.4 (i), §2.5 and §3 committed at f4b3e73. CONFIRMED. Answers raw :31 (§1.4), :47-52 (§2.5), :56-63 (§3); `git log` shows f4b3e73 as "The seat's answers … (second sitting)".
2. T1:3-4. The PI's routing item N.2, on "Route as given", with "Go" in the batch's slot. CONFIRMED. RESULTS.md:105-106 ("Route as given"), :110 (N.1–N.4 relayed to n-build), :112-114 (the slot "…: Go]"); answers §8 :89.
3. T1:4-5. "It runs on nothing on the box before ADDENDUM-n3's commit (§2.5)". CONFIRMED: it follows from §2.5 :51, "runs on nothing before the addendum's commit". See observation 4.
4. T1:7-8. The arrival is the mean over positions 1..n of the projection on the unit valence row, with ARRIVAL_FROM = directions.CAPTURE_FROM as one constant. CONFIRMED. d2 gcal.py:182 and :335-351; directions.py:49-59 (CAPTURE_FROM = 1, used by G-VEC's means and R); §1.4 (i).
5. T1:8-9. `arrival_all` is recorded per turn beside it, descriptive. CONFIRMED. d2 gcal.py:347, :481, :489.
6. T1:9-11. A one-id turn has no score and is left out of the t; `one_id` is counted beside `empty` in every batch's stops, as departure (2) treats the end-of-turn-first turn; the baseline alike. CONFIRMED. d2 gcal.py:348, :360-365, :378, :506, :517 (every batch, the baseline included), :527 (the gate's), :101-103.
7. T1:12-14. The early PAUSE: exit 3; the record, turns and dose map written; `early_pause` recorded; no +ρ/2, gate or −ρ turn; a STOP first (O1); `stage_status` unchanged. CONFIRMED.
   - Seat: §3 :58-59.
   - Code: d2 gcal.py:491-504 (STOP tested at :495 before PAUSE at :500, then break), :534, :576; d2 n_sessions.py:2858-2864 (write) and :2893-2899 (return 3).
   - `stage_status`: d2 :390-397 is identical to HEAD :333-340.
8. T1:15-17. The gate's batch: the 48 prompts and seeds, TEMP 0.7, cap 80, the whole turn from position 0, span_reward's unit row of record at the site, 0.20·R_ℓ. CONFIRMED. §2.5 :49; d2 gcal.py:263, :428, :474; d2 n_sessions.py:2790 (CAP unless env.cap) and :2860.
9. T1:16-18. `gate_injection` uses runner._injection's arithmetic for N2-E at f0.20, its alpha is `expected_alpha`'s, and the row is checked against of_record before the load. CONFIRMED.
   - runner.py:278-300 against d2 gcal.py:419-432.
   - schema.py:290 (`"f0.20": ("program", 1, 0.20)`), :301 and :541-550.
   - d2 n_sessions.py:2706 (the row's sha16 check), with gcal_gvec_inputs at :2813 before make_adapter at :2841.
10. T1:18-20. The steering check is printed; the batch comes after +ρ/2 and before −ρ; it is scored on coherence alone against the one bar, with no arrival; a fail is neither a STOP nor a PAUSE. CONFIRMED. d2 gcal.py:175, :468-471, :172, :487, :525-529, :534.
11. T1:20. The record carries the count, pass and stops; the turns file carries 48 turns; the exposure line stays −ρ's. CONFIRMED. d2 gcal.py:526-529, :173, :546-548, :535-537.
12. T1:20-22. After the exposure line the stage prints "reward axis 5(d) gate, coherence: k of 48, PASS" (or FAIL), in the lock's form. CONFIRMED. d2 n_sessions.py:2877-2883; §2.5 :50 ("k of 48, PASS or FAIL").
13. T1:22 and T3:60-61. "The line n-analyzer pins at v7". NOT CHECKABLE.
   - Supporting evidence: §2.5 :50 says n-analyzer's delta after G-CAL-n's run reads "the lock's line, not gcal.json", and d85fc34's subject lists "the analyzer's v7 hash" among the lock's holes.
   - No source states that v7 is the version that pins this line.
14. T1:23. Schema `n-gcal-v2`, `early_pause`, and the constants `arrival_from` and `gate`. CONFIRMED. d2 gcal.py:141, :576, :582-584.
15. T1:24. gcal.py 4bd8f8bf…c376 (+371 −128). CONFIRMED by shasum and numstat 371/128 against HEAD.
16. T1:24. n_sessions.py 313aa240…8e96 (+180 −70). CONFIRMED by shasum and numstat 180/70.
17. T1:24-25. The digest moves from d3415b10…a519 to 7cf47aa0…1ffa, by shell. CONFIRMED: I recomputed both by shell in resume.py:328-350's form, and both are exact.
18. T1:26. 570/570. CONFIRMED. S/step4b/gcal2/selftest_run1.txt; the exit file reads "exit 0".
19. T1:26. "In a battery window the coordinating session granted, under nice -n 19". NOT CHECKABLE (Code's acts).
20. T1:26-27. 581 on the box by arithmetic. CONFIRMED: 570 + 11. The box's 11 matches RESULTS.md:49 (571 against 560), :328-329 (556 = 545 + 11) and :699 (551 = 540 + 11).
21. T1:28-33. Code's readings as gcal.py's docstring gives them. CONFIRMED. d2 gcal.py:115-122, clause by clause.
22. T1:31. The gate's sign +1 comes from schema.DOSES for f0.20, and §2.5 names no sign. CONFIRMED. schema.py:290; §2.5 :47-52 names none.
23. T1:34-36. The review's O5, restated. CONFIRMED. T3:246.
24. T1:36-37. The review's O6, restated as "…would split those turns out". IMPRECISE: O6 (T3:248) says "should split out or drop n_tok = 1". Put instead: "so a pooled summary of `arrival_all` at the read should split those turns out or drop them."
25. T1:38. 0 BUG; 10 findings (5 RISK, 5 NIT); 4 surviving mutants; 4 box risks; 8 observations. CONFIRMED. T3 §2: F1–F5 RISK, F6–F10 NIT, M1–M4, B1–B4, O1–O8, "I found no BUG".
26. T1:38-39. Every finding is applied in draft 2, and each mutant meets a check. CONFIRMED by items 66-76. See observation 2.
27. T1:39-40. "The self-tests' flows now reach every batch by construction, and three of them run on non-empty incoherent turns". IMPRECISE.
   - Only the main flows reach every batch.
   - Two of the three named flows (b35, and the driver's env8) end at the early read by design.
   - Put instead: "F1 and F2: the self-tests' main flows now reach every batch by construction, and three flows run on non-empty incoherent turns".
28. T1:40-41. Three flows run on non-empty incoherent turns, so "coherent" and "has an id" are told apart. CONFIRMED. d2 gcal.py:961-984 (b35) and :926-947 (gm); d2 n_sessions.py:3366-3395 (env8, on the plain decode).
29. T1:41. F3: R and R_ell are apart in the fake G-VEC record. CONFIRMED. d2 n_sessions.py:3059: `R_t, Rl_t = 3.0, 4.0`.
30. T1:41. B3 goes to G-CAL-n's launch files. CONFIRMED. T3:67-68.
31. T1:42 and :44. The two raws' paths. NOT CHECKABLE (to be committed); the names match the brief's.
32. T1:46. Code's one `jq` read. NOT CHECKABLE.
33. T1:47-49. The reviewer's departures. CONFIRMED. T3:254-264: two rev-parse runs; the saved diff, read and counted with `grep -c`; reads beyond its brief, one `git grep -l` with the exclusions.
34. T1:52-55. Committed by path; the commit-time count of 0; nothing ran on a model; not pushed. NOT CHECKABLE (commit-time).
35. T1:56. Next: the launch files after G-VEC's PASS and ADDENDUM-n3's commit, with the time at 240 turns. CONFIRMED. Answers §8 :89 and §2.5 :51; B3 at T3:191-193.
36. T2:1. Cites s1.4 (i), s2.5 and s3. CONFIRMED.
37. T2:4-6. 616e940's versions, the two hashes and both numstats. CONFIRMED (as items 15-16).
38. T2:7-10. Both digests in full, both computed by shell in package_sha256_of's form. CONFIRMED. resume.py:328-350; both recomputed exactly.
39. T2:10. "The self-test prints no digest". CONFIRMED. The output is one line; d2 n_sessions.py:236-362 prints only FAIL lines and the total.
40. T2:10-11. `hashes` runs at the launch files, in its own window. NOT CHECKABLE (plan; it matches the precedent at RESULTS.md:695-696).
41. T2:13-14. HF cases are skipped and counted where torch and transformers are absent; the schema module's cases count as one aggregated line. CONFIRMED. d2 n_sessions.py:9, :246-247, :3643 and :3671.
42. T2:15-16. The overlay of 162 files, joined on hash-object. NOT CHECKABLE: the overlay is not among my sources.
43. T2:17-22. The command, the window, the re-hashes and the empty temporary folder. NOT CHECKABLE.
44. T2:24-27. Run 1: both hashes, 1117 and 3772 lines, exit 0, output 1 line, sha256 b3898c6e…13e0. CONFIRMED by shasum, `wc -l` and the exit file.
45. T2:24. "Draft 1 did not run". NOT CHECKABLE.
46. T2:28. The verbatim output line. CONFIRMED: byte-equal to selftest_run1.txt by `cmp`, leading spaces included.
47. T2:29. Ten checks added to 616e940's 560. CONFIRMED.
   - RESULTS.md:48 records 560/560 at 616e940.
   - Lines holding `chk(`: gcal.py 39 → 46, the driver 148 → 151.
   - The total is 570.
48. T2:29-31. The seven gcal.py checks as named. CONFIRMED: the new chk calls at d2 gcal.py :717, :817, :851, :921, :940, :948 and :1099.
49. T2:31-32. The three driver checks as named. CONFIRMED. d2 n_sessions.py:3176 (the gate's batch), :3192 (M4, the tie to G-VEC's rows) and :3385 (the early PAUSE).
50. T2:32-33. "No other check is added or removed: the other self-test changes extend existing checks." IMPRECISE.
   - The count holds: gcal.py loses 11 `chk(` lines and gains 18; the driver loses 1 and gains 4.
   - But gcal.py's "the seat's O7 in the flow" check is rewritten, not extended. At HEAD :731-737 it asserted a PAUSE with all four batches; at d2 :908-918 it asserts the early PAUSE with two.
   - Put instead: "No other check is added or removed: the other self-test changes extend existing checks, and one, gcal.py's O7 flow check, is rewritten as the early PAUSE's (O2)."
51. T2:35-37. 581 is 570 plus the box's 11, as at the BUILD and at 616e940, and the gate's steering check sits inside the one HF-path check. CONFIRMED. RESULTS.md:49, :328-329, :699; d2 n_sessions.py:3643-3671 (:3665 inside the one check, :3671 the skip).
52. T2:37-38. "Restated at G-CAL-n's launch files". NOT CHECKABLE (plan).
53. T3:5-6. One blind pass over draft 1, from 616e940's bytes to the seat's three changes. CONFIRMED. review_brief.md:1-3 and :7-14.
54. T3:7. gcal.py from 61bcafc9…14fc to 17defa3f…21db, 1091 lines, read in full. CONFIRMED by shasum, `wc -l` and the report at T3:93.
55. T3:8-9. The driver from 2728146e…570c to 47b12b3e…737b, 3737 lines; G-CAL-n's section and its self-test read in full. CONFIRMED. T3:94 (D:2608-3637 plus D:1-370).
56. T3:10. "The same 181 changed lines on both bases". IMPRECISE.
   - On 616e940's base, `git diff --no-index --numstat` gives +129 −54, which is 183 lines; it is 181 only if the two added blank lines are left out. All four diff algorithms agree.
   - G-VEC's draft 1 is not among my sources.
   - Put instead: "Draft 1's driver changes were built on G-VEC's draft 1 and rebased onto `616e940`'s driver (+129 −54 there, by numstat)."
57. T3:10-11. Draft 1's self-test did not run. NOT CHECKABLE.
58. T3:13. The brief, bc23af8e…eacc, 91 lines. CONFIRMED.
59. T3:14-17. What the brief gave. CONFIRMED. review_brief.md:11-15 and :20-38.
60. T3:18-22. What the brief asked, the count of 569 included. CONFIRMED. review_brief.md:39-53 (569 at :51).
61. T3:23. It asked for findings, mutants, box risks, observations and departures. CONFIRMED. review_brief.md:55-66.
62. T3:24-26. The quoted list of record and the bars. CONFIRMED. review_brief.md:70-91.
63. T3:28-29. The report in §2: 190 lines, 44dbda82…3c30, scratch files named only as S/ paths. CONFIRMED. The `jq` extraction itself is Code's act and not checkable.
64. T3:31. The totals. CONFIRMED (as item 25).
65. T3:35-36. Draft 2: 1117 lines with +63 −37 on draft 1, and 3772 lines with +64 −29. CONFIRMED by numstat of draft 2 against draft 1.
66. T3:38-41. F1. CONFIRMED.
   - d2 gcal.py:678-683.
   - d2 n_sessions.py:3115-3121 and :3133.
   - The flaky step (:3288-3296) and the recording step (:3343-3347) use `base_step`; :3322-3326 asserts the kept turns are the run of record's.
67. T3:42-48. F2's three flows. CONFIRMED. d2 gcal.py:961-984 (b35: 35 coherent, all non-empty, early PAUSE), :926-947 (gm: 0 of 48, 48 one-id stops, baseline 48 coherent, PASS); d2 n_sessions.py:3366-3395 (env8: rc 3).
68. T3:49. F3. CONFIRMED (as item 29).
69. T3:50-52. F4. CONFIRMED. d2 gcal.py:686-687, :767 and :823; the driver's M4 check at :3192 regenerates turn 0 under `injection_for(1.0, rows[0], site, R_t, v_sha)` and recomputes the mean over [1:].
70. T3:53-54. F5. CONFIRMED. d2 gcal.py:182 and :720; "built alike" at answers :8.
71. T3:55-56. F6. CONFIRMED. d2 gcal.py:29-30 and :97-98.
72. T3:57-58. F7, its line quoted exactly. CONFIRMED. d2 n_sessions.py:2898-2899; `stage_status` unchanged (item 7).
73. T3:59-61. F8. CONFIRMED. d2 gcal.py:530-533; d2 n_sessions.py:2879-2883 and :3184. "At v7" is as item 13.
74. T3:62. F9. CONFIRMED. d2 gcal.py:141 and :121-122; HEAD :112 was "n-gcal-v1".
75. T3:63-64. F10. CONFIRMED. d2 n_sessions.py:3023-3029; the two cited breaks are gone from :158-176. See observation 2.
76. T3:65. M1–M4 each killed. CONFIRMED.
   - M1: the gate check's alpha against expected_alpha at Rl_t 4.0 (:3176-3184), and the canned check's `g_["R_ell"] == Rl_t`.
   - M2: b35's `early_pause` and its count of 35; gm's gate count of 0.
   - M3: d2 gcal.py:767 and :823.
   - M4: :3192.
77. T3:66-67. B1 and B4 ask for nothing; B2 is applied. CONFIRMED. T3:176-182 and :196-199; d2 n_sessions.py:3649 and :3665.
78. T3:67-68. B3: "240 turns, up to 3,840 more uncached forwards than 192". IMPRECISE: the report at T3:192 says "up to 3,840 more uncached forwards plus 2". Put instead: "240 turns instead of 192, up to 3,840 more uncached forwards plus 2".
79. T3:69-72. O1–O4 and O7 ask for nothing in the code; O5 and O6 go to the seat; O8 stands. CONFIRMED. T3:203-252, and T1:34-37.
80. T3:73. The reviewer's departures are in the entry. CONFIRMED. T1:47-49.
81. T3:75-266. §2 is byte-equal to S/step4b/gcal2/review_report.md. CONFIRMED: `head -n 266 | tail -n 190 | cmp` exits 0, and both sha256s are 44dbda82…3c30.

TOTALS
81 items: 65 CONFIRMED, 5 IMPRECISE (items 24, 27, 50, 56, 78), 0 FAIL, 11 NOT CHECKABLE (items 13, 19, 31, 32, 34, 40, 42, 43, 45, 52, 57).

OBSERVATIONS
1. The wording owed at the driver's next change is not applied in draft 2, and T1 does not mention it. This should be applied or declared in the entry.
   - The owed item, from 035947e's entry (RESULTS.md:387-388): `run_gcal`'s docstring, the `gcal` command's docstring and the exits check's name say "the record and the turns" without the dose map.
   - The seat's §3 (answers :61) says this wording "rides with this delta", and the close line at RESULTS.md:445-446 repeats it.
   - Draft 2 leaves all three as they were: d2 n_sessions.py:2748-2749 ("each with its record and turns, for the seat"), :174-176 ("each with its record and turns, for the seat; the gate's batch is neither") and :3246-3247 ("each with its record and turns written, for the seat").
   - `run_gcal`'s docstring also names neither the gate's batch nor the early PAUSE.
2. F10's reflow leaves one short line in the command's docstring: d2 n_sessions.py:172, "-rho and the gate's line in the lock's form. ``--smoke N`` (1..4): N".
3. B2's second clause (T3:189, "For the seat: the smoke could run the gate's two-forward check with no turn") is not handled anywhere. T3 §1 applies only the cheap cover, and T1:34 carries only O5 and O6 to the seat.
4. T1:4-5 narrows §2.5's "runs on nothing before the addendum's commit" (answers :51) to the box, while the model-free laptop self-test ran before that commit. Possible wording: 'it "runs on nothing before the addendum's commit" (§2.5): the self-test is model-free, and nothing runs on the box before it.'
5. The "Go" in T1:3-4 is the coordinating session's reading, put to the PI (RESULTS.md:112-117). T1 could say so.
6. The gate line's place after the exposure line (T1:20-21, T3:60) is by construction (d2 n_sessions.py:2877-2883) and no check pins it. The print-order heads at :3211-3213 end at "exposure at -rho", and :3184 pins only the line's form and count.
7. d2 gcal.py:65-66, "Both hurdles are computed at every dose generated", reads as covering the gate's f0.20 batch, which is scored on coherence alone. CONVENTIONS["arrival"] at :213 says "every valence dose generated"; the docstring could say the same.

DEPARTURES
1. One `awk` run, which the brief bars. It filtered `/usr/bin/grep -n -E 'self-test|on the box' RESULTS.md` through `awk -F: '$1>=313 && $1<=840'` into `head -0`. `head` refused the count ("illegal line count -- 0"), so nothing awk produced was printed. No marker or data path was involved.

For the seat to class (not barred by my reading):
- RESULTS.md beyond the named entries: the G-CAL-n BUILD entry, :694-701, for the box's 11 at the BUILD; and grep listings over RESULTS.md for self-test counts and for `\bv7\b`.
- valence_core/m/resume.py:300-359 (package_sha256_of, whose form the brief names).
- One `git log -1 --format='%h %s' d85fc34` with the pathspec and the mf3 exclusion, cut by `grep -o` to the words around "the analyzer's v7 hash".
- One `git ls-files` with that pathspec, counted by `grep -c`, with no name printed.
- Numstats of draft 1's driver against HEAD's under four diff algorithms and `--ignore-blank-lines`, with `-U0` line counts.
- HEAD was found by `git log -5` with the pathspec, not by `git rev-parse HEAD`.

Otherwise:
- No interpreter but `shasum`; nothing written; no network; no guard marker in any argv.
- Nothing under data/ was listed or read; no whole-tree status.
- In S, only the brief and the files it names, each by name.
