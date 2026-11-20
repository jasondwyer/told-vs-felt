# n — G-VEC's re-run (PASS at index 32): the blind values-check, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the drafts of the commit's two texts:
- T1, the RESULTS.md entry: `2aae7452…1afd` (111 lines), with its values-check paragraph and the checker's departures
  as placeholders;
- T2, the launch review's raw, `results/raw/2026-11-19_n-gvec-v2_launch-review.md` here: `bb99af57…aadd` (271 lines).

**The checker's brief** (`afb48d05…c2a2`, 82 lines, given to the checker as a file, with its sha256 to verify):
- named the texts and the sources: in Code's scratch, the run's files as copied back (the script's output, the exit
  file, the work folder's files and the pod session's record; the six outputs of record), the ten raws to be committed,
  the launch files as relayed, the launch review's brief and report, the files as first drafted, and the laptop tests'
  outputs; in the repository, RESULTS.md (the first run's entry, the gvec delta's and the coordinating session's notes
  for the second sitting), the seat's answers of the second sitting, `gvec.py`, `scripts/n_sessions.py`,
  `valence_core/adapters/base.py` and `.gitignore`'s block for `data/n/gvec/`;
- asked for every factual claim to be checked, the 16 rows' sha16s recomputed by shell among them, and for T2's §2 to
  be byte-equal to the review's report;
- warned that several sources hold guard-marker words in their content, never to enter an argv;
- barred any interpreter but `shasum`, any write, any network, any guard marker in an argv, anything under
  `data/mf3`, any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the
  named files and the brief itself; and quoted the list of record v2's items 1–5, verbatim.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (157 lines, sha256
`e5e05490…79f0`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 99 items: 84 CONFIRMED, 5 IMPRECISE, 1 FAIL, 9 NOT CHECKABLE; and 10 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

- **The FAIL,** item 60 (T1): the pod session's reading was quoted in two phrases, "as at v1" and "before they leave
  the box", which no committed text holds: they are the coordinating session's words in its message to n-build. T1
  now quotes the record's own "as at the first run", and says the coordinating session's message gives the reading it
  accepted, in no committed text.
- **The IMPRECISE items,** each applied in the checker's words or near them:
  - 27 (T1): the five files besides `gvec.json` are at the record's `files_sha256`, which cannot hold its own file's;
  - 39 (T1): what was applied before the relay, what the relay met (O8), what stands (O3, borne out by the box's
    571/571) and what asks for nothing;
  - 43 (T1): tokenizers 0.22.2 is the pod session's record's; numpy 2.1.2 the record's `adapter_provenance`'s;
  - 54 (T1): the fourteen files the pod session's record lists, each at its value there, and the record itself,
    `d29bd9d1…53e3`, which cannot list its own hash;
  - 63 (T1): the reviewer's departures in full: `valence_core/n/` twice, the adapters folder's listing without
    `--name-only` (modes, ids and names), and `git cat-file` and `git rev-parse` on named files.
- **The NOT CHECKABLE items** stand: this session's acts and plans, the coordinating session's acceptance, and what
  the laptop tests ran on (8, 59, 61, 65, 67, 84, 88, 94, 99). Item 84's clause (the staging case fails at the
  changed set too) is checked by tool: that case's last line ends "changed set 1", and its output names
  `!! data/n/.gvec.staging/`.
- **The observations:**
  - 1: T1 points the seat to the pod session's record's §7;
  - 2: T1 says the `git log -1 --format=%B` departure is the format as well as the pathspec;
  - 3: T2's §1 heading is "Dispositions", with a line on what came after the run and what the relay met;
  - 4: met by the check by tool above;
  - 5: T2 gives the first-drafted note's 127 lines;
  - 6: T1 gives the +11's arithmetic, the box's 14 HF checks in place of the laptop's three skip lines;
  - 7: T1 names `directions.order` and `directions.alt_order`, and each row's byte range;
  - 8: met by item 54's wording;
  - 9: none of those test outputs is committed; a later commit of one takes the scrub;
  - 10: the two single re-runs print the roster's 82 beside "killed 1"; T1 and T2 say each ran alone.

## 2. The text changed after the check, and the edits checked by tool

- **The text changed after the check** by the dispositions above, and in T1 by its values-check paragraph and the
  checker's departures, which replace the placeholders, and by its departures' second bullet, which names the second
  extraction by `jq`.
- **The edits, checked by tool:** fixed-string counts over each text unwrapped, for each disposition's new wording
  and each removed wording's absence; T2's §2 byte-equal to the launch review's report, and this raw's §3 byte-equal
  to the values-check's report: 27 of 27.
- **No second full pass** was made over the texts.
- **The finals:** the entry `4689a9f7…96e4` (133 lines); the launch review's raw `5169022d…c257` (272 lines).

## 3. The report as returned

BLIND VALUES-CHECK: T1 (S/step4b/gvec2/run2/entry_src.md) and T2 (S/step4b/gvec2/run2/launch_review_raw.md), at HEAD bc50244

Verified first: the brief is afb48d05…c2a2 (82 lines). T1 is 2aae7452…1afd (111 lines). T2 is bb99af57…aadd (271 lines). S/step4b/gvec2/launch/review_report.md is 98dc4465…1fb3 (202 lines). All four match their stated values.

Source short names:
- OUT = S/step4b/gvec2/box/out/gvec_v2_out.txt (626ed5ee…a530, 161 lines)
- REC = S/step4b/gvec2/box/out/gvec2_box_run.txt, the pod session's record (d29bd9d1…53e3, 147 lines)
- GJ = S/step4b/gvec2/box/rec/data/n/gvec/gvec.json
- SH = S/step4b/gvec2/launch/gvec_v2.sh
- NOTE = S/step4b/gvec2/launch/gvec_launch_note_v2.md
- RB = S/step4b/gvec2/launch/review_brief.md
- HAR = S/step4b/gvec2/launch/test/harness_v2r_run2.txt
- MUT = S/step4b/gvec2/launch/test/mutants_v2r_run1.txt, with _n5 and _r9
- SNIP = S/step4b/gvec2/launch/snippet_test/run2.txt
- ANS = results/raw/2026-11-19_n-gvec-stop-lock-opens_design-to-code_answers.md
- ROUT = results/raw/2026-11-19_second-sitting_pi-routing.md

Every repository file I read is tracked and clean at HEAD (git rev-parse HEAD:<path> = git hash-object <path>): RESULTS.md, ANS, ROUT, valence_core/n/gvec.py, scripts/n_sessions.py, valence_core/adapters/base.py, .gitignore, PROPOSAL-n-bk-reconciliation-v0_2.md and ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md.

ITEMS

T1:
1. T1:1. The re-run is from the gvec delta's commit `616e940`. CONFIRMED. OUT:2 prints "HEAD 616e9407c724…9103"; git log shows 616e940 as the gvec delta; REC:2.
2. T1:1. PASS at index 32. CONFIRMED. OUT:131, :147, :155, :161; GJ status PASS, site.site 32.
3. T1:1–3. R over 1..n is within 2% of 25.49 at both indices, and the site rule took the nearer, 32. CONFIRMED. OUT:127–128 give rel 0.013933525466854002 and 0.002158027120846784, each "within 2%"; GJ :867–878; gvec.py:262–271 (`choose_site` takes the nearer by rel).
4. T1:3. n §2.3. CONFIRMED. PROPOSAL-n-bk-reconciliation-v0_2.md:81: "R ≈ 25.49 there [C] — reproduced at G-VEC within 2%, else STOP".
5. T1:3. ADDENDUM-n1 §6.1. CONFIRMED. ADDENDUM-n1-…:52: "If indices 31 and 32 both reproduce R within 2%, the nearer is the site".
6. T1:3. The seat's answers, second sitting, §1.2–§1.5. CONFIRMED. ANS:16–33.
7. T1:3–4. The PI's routing, item N.1, on "Route as given". CONFIRMED. ROUT:12–13 and :28.
8. T1:4–5, :29, :108. The outputs and raws enter the repository at this commit. NOT CHECKABLE: the commit is still to come.
9. T1:7. `gvec_v2.sh` is `e5f76f5b…c49e`. CONFIRMED. shasum of SH; REC:25.
10. T1:7. It ended "gvec v2 PASS: …", exit 0. CONFIRMED. OUT:161; S/step4b/gvec2/box/out/gvec_v2.exit reads "exit 0".
11. T1:7. Pod `emw1e4embiwe9b`. CONFIRMED. OUT:95, :115; GJ :820; REC:1.
12. T1:7–8. Run by the pod session on the relay ("LAUNCH CLEARED", item N.1 [go]). CONFIRMED. REC:3–5 ("item 1 [go]"; "G-VEC v2: LAUNCH CLEARED"); ROUT:13 ends "[go]".
13. T1:9–10. The quoted R count line. CONFIRMED. OUT:126, verbatim.
14. T1:10–12. The quoted "R at index 31/32" lines. CONFIRMED. OUT:127–128, verbatim.
15. T1:12. "site: index 32 (ADDENDUM-n1 §6.1)", then "G-VEC PASS". CONFIRMED. OUT:131 and :147.
16. T1:13. `gvec.json` is `03467e75…53b0`. CONFIRMED. shasum of GJ; OUT:145 and :159.
17. T1:13–14. Of record: site 32, R 25.54500811131038, R_ℓ 21.98789170395024 over A3's 1,344 contexts, Route B. CONFIRMED. GJ :680–691 and :142; OUT:132, :134, :154.
18. T1:14–15. The four sha16s at index 32. CONFIRMED. GJ :639–644 and :684–687.
19. T1:16. §1.3: "none a decision". CONFIRMED. ANS:24.
20. T1:16–17. R_all 44.04249774012646 and 45.107750142385356, each printed "equal" to the first run's R. CONFIRMED. OUT:129–130 and :156–157; GJ :545 and :570; RESULTS.md:543–544.
21. T1:17–19. RMS at position 0, and the range over positions 1–4 and 5..n from 22.96714802957467 to 26.005746614723453. CONFIRMED. OUT:129–130; GJ :560–567 and :585–592. The minimum is index 32's position 3 and the maximum is index 31's position 4.
22. T1:19–20. The max norms and R_mean_of_passage_rms. CONFIRMED. OUT:129–130; GJ :546–550 and :571–575.
23. T1:20–21. Counts 96 at positions 0–4 and 3,683 over 5..n; no figure null. CONFIRMED. OUT:129–130 carry no null suffix, and OUT:156–157 read "not finite: []"; GJ nonfinite is [] at both indices.
24. T1:22–24. The smoke's R, R_ℓ and R_all are "equal" to the first run's smoke R. CONFIRMED. OUT:96–97 and :104–106; RESULTS.md:548–549.
25. T1:25–28. The six cosines. CONFIRMED. OUT:135–140; S/…/gvec_cosines.json; GJ :534–541.
26. T1:29. The six files are admitted by the BUILD's `.gitignore`. CONFIRMED. .gitignore:307–314 admits exactly the six. The block is absent at `da7bdec^` and present at `da7bdec`.
27. T1:29–30. "each at the sha256 its file line prints and the record's `files_sha256` holds". IMPRECISE. Each file matches its file line (OUT:141–146). But GJ :647–653 `files_sha256` holds only five files. It cannot hold gvec.json's own hash (gvec.py `write`, :551–552). Replace with: "each at the sha256 its file line prints, the five besides `gvec.json` also at the record's `files_sha256`:".
28. T1:30–32. The six sha256 abbreviations. CONFIRMED. shasum of each file, abbreviated by `cut`; OUT:141–146; REC:129–134.
29. T1:32–33. Four float32 rows of 5120, header '<f4', shape (4, 5120). CONFIRMED. `head -c 128 | od -c` of each file shows NPY 1.0, header length 118, {'descr': '<f4', 'fortran_order': False, 'shape': (4, 5120), }. Each file is 82,048 bytes, which is 128 + 4·20,480.
30. T1:33–34. Each row's sha16, recomputed by shell, equals the record's: 16 of 16. CONFIRMED.
    - Command: `tail -c +$((129+20480*i)) | head -c 20480 | shasum -a 256 | cut -c1-16`, for i = 0..3 of each file.
    - L31: ce2d7e787647adc2, e7703d0c03e0683b, e60bf94143dd1159, 5c0122f326e633a0.
    - L32: ba4da67fb717b5bb, 8f32921fcd1798db, f4136430145a2960, 006f5174a82193f9.
    - alt_L31: 02e3ec4d03542b94, bdcb57cd53a4f35d, 4603e0a64fa41df7, 583d9d34391a65c9.
    - alt_L32: 8b6ba0c9abdc671b, 2205bf41be4d3cad, df75054cb09f27ab, 6eba5931100b81fd.
    - Each equals GJ :606–618 and :632–644, row by row in `order` and `alt_order`. base.py:34–40 defines `sha16_arr` the same way.
31. T1:35–36. Next (item N.1's PASS branch): holes 1–7; G-CAL-n's launch files after ADDENDUM-n3's commit. CONFIRMED. ROUT:13 and :14; ANS:33. "In Code's scratch draft" and "drafted now" are Code's plans.
32. T1:38–39. Relayed at their hashes and cleared on the PI's routing. CONFIRMED. REC:3–5 and :23–31.
33. T1:39. The script is 352 lines; its commit is `616e940`; its driver line is `2728146e…570c`. CONFIRMED. `wc -l`; SH:54–55; `git show 616e940:scripts/n_sessions.py | shasum` gives 2728146e…570c; RESULTS.md:127.
34. T1:40. The manifest is `00180e67…6a3e`, 61 files, each asserted equal to `616e940`'s blob. CONFIRMED. shasum; 61 lines; OUT:5–65 are 61 "OK"; NOTE:22–23. Two manifest lines equal `git show 616e940:<path>` by shasum.
35. T1:40–41. The hashes file is `c40ed07b…7368`, 13 lines, made from a `git archive` in a battery window. CONFIRMED. shasum and `wc -l`; NOTE:25–26; OUT:87.
36. T1:41–42. The note is `125b1541…23fe`, 154 lines, and stays in scratch. CONFIRMED. shasum and `wc -l`; REC:30.
37. T1:43–45. Harness 418; mutation pass 82, all killed; 73 fixtures, 90 of 90, 23 mutants killed. CONFIRMED. HAR:126; MUT:83 (82 mutants, 80 killed, 2 not applied); _n5:1 and _r9:1; SNIP:1, :92, :116; NOTE:138–149.
38. T1:45–46. 0 BUG; 8 findings (5 RISK, 3 NIT); 8 surviving mutants; 11 observations. CONFIRMED. T2:74.
39. T1:46–47. "each applied before the relay". IMPRECISE. T2:56–61 shows six observations ask for nothing, O3 is borne out only after the run, and O8 is met by the relay itself. Replace with: "…; 11 observations. Before the relay every finding was applied and every surviving mutant met by a case that kills it; O7, O9 and O10 were applied and O8 met by the relay; O3 stands, borne out by the box's 571/571; the other six ask for nothing."
40. T1:47–48. The link to the review raw. CONFIRMED. S/…/run2/raws/2026-11-19_n-gvec-v2_launch-review.md is byte-equal to T2.
41. T1:49–50. The sync. CONFIRMED. REC:36–42.
42. T1:51–54. The fresh copy. CONFIRMED. REC:44–54 and :58; OUT:2–3.
43. T1:55–56. The versions, attributed to "(the record's `adapter_provenance`)". IMPRECISE. GJ :765–791 holds python, torch, transformers and numpy 2.1.2 but no tokenizers version. tokenizers 0.22.2 comes from REC:60. Replace with: "python 3.12.3, torch 2.8.0+cu128, transformers 5.15.0 and tokenizers 0.22.2 (the pod session's record), and numpy 2.1.2 (the record's `adapter_provenance`, which also holds the first three)".
44. T1:56–57. The env.sh variables; bf16, deterministic, seed 20260818. CONFIRMED. REC:59; GJ :773, :775, :777, :790.
45. T1:57–58. `8264f719efd347a9` is backend-ext-2's, bridged to `4ed3f2c70fe8afbf` (R6). CONFIRMED. OUT:95 and :115; GJ :792–793; RESULTS.md:1603–1605.
46. T1:59. Two loads, 707 of 707, 119470 ms and 28510 ms. CONFIRMED. OUT:94–95 and :114–115; GJ :816.
47. T1:61. "changed set none"; manifest 61 of 61. CONFIRMED. OUT:2–3 and :5–65.
48. T1:62–63. 571/571 after two warnings (560 plus 11); the hashes equal. CONFIRMED. OUT:67–71 and :87; RESULTS.md:129–130.
49. T1:64–65. Smoke lines once each; record held; identity equal; copy unchanged; record stays on the box. CONFIRMED. OUT:103–108; REC:87.
50. T1:66–69. The run of record's lines. CONFIRMED. OUT:110–148, with the quote at :116.
51. T1:70–73. The outputs step and the eleven record checks. CONFIRMED. OUT:151–160; the check names match OUT:153 one for one.
52. T1:74–75. PID 9048; the end-wait on the PID; idle before and after, 0 MiB. CONFIRMED. REC:57, :69, :108.
53. T1:76–78. The copy-back: by explicit name, sha256 equal at all three places, no folder listed, address and port count 0. CONFIRMED. REC:112–119 and :136–138.
54. T1:78–79. "Code re-hashed the fifteen files …, each equal to the pod session's value". IMPRECISE. My re-hash equals the fourteen values REC:121–134 lists. The fifteenth file, the record itself (d29bd9d1…53e3), cannot list its own hash, and no source I may read gives one. Replace with: "Code re-hashed the fifteen files on the laptop: the fourteen the record lists, each equal to its value there, and the record itself, `d29bd9d1…53e3`".
55. T1:79–82. The cmp relations. CONFIRMED as relations. hashes.txt and both identity files are c40ed07b…7368. By `cmp` against line ranges of OUT: selftest.txt equals OUT:67–69, hashes.txt equals :73–85, smoke.txt equals :89–101, and run.txt equals :110–147. Code's own reading is not checkable.
56. T1:83–86. The box at the end; item N.4. CONFIRMED. REC:108 and :140–147; ROUT:16.
57. T1:87–90. The raws and their sources. CONFIRMED. Every file in S/…/run2/raws/ equals its source by sha256. _stage equals the work folder's run.txt (b46b59de…b33b), and _run equals REC. _valuescheck is absent, as expected.
58. T1:92–94. The pod session's two acts, as its record states them. CONFIRMED. REC:116–117 and :136–138. The record does not call either one a departure.
59. T1:92. "accepted by the coordinating session". NOT CHECKABLE.
60. T1:94–95. "(its reading of the routing's "as at v1" over "before they leave the box")". FAIL. Neither phrase is in REC (which says "as at the first run", :137), ROUT, NOTE, SH or any tracked file. `git grep -F` over the tree in item 3's form finds no "before they leave the box" anywhere, and "as at v1" only in unrelated files. Replace with: "…not on the box ("as at the first run", its record says);". If the words are the coordinating session's relay's, say so: "(its reading of the coordinating session's relay, "as at v1" over "before they leave the box", in no committed text)".
61. T1:96–98. Code's three departures. NOT CHECKABLE: Code's own acts.
62. T1:98–99. `check-ignore` is "a command item 1 does not list"; ab72d0f's was of this class. CONFIRMED. Item 1 names `git check-attr`; RESULTS.md:234–236.
63. T1:100–105. The reviewer's departures "as its report states them". IMPRECISE. The text leaves out departure 4's last bullet (T2:265, `git cat-file` and `git rev-parse` on named files, data files among them). It also drops "twice" and the adapters folder's ls-tree "which printed modes, ids and names" (T2:262–263). Replace with: "`git ls-tree` over folders or `.` instead of item 3's pathspec (`valence_core/n/`, twice; the adapters folder, without `--name-only`, printing modes, ids and names; and the BK skeleton folder reached by a glob `cd`), and `git cat-file` and `git rev-parse` on named files, data files among them, none under ckpt, reports or mf3; and, stated plainly …".
64. T1:108. "the eleven raws". CONFIRMED as a count: T1:87–90 names eleven.
65. T1:110. Home-folder count 0; nothing ran on a model; not pushed. NOT CHECKABLE.
66. T1:111. Next. CONFIRMED, as item 31.

T2:
67. T2:3. PI date; Code. NOT CHECKABLE.
68. T2:5–6. One blind pass at 616e940, before the relay. CONFIRMED. RB:6; T2:70.
69. T2:7. `d0d154d7…6402`, 323 lines. CONFIRMED. S/…/prereview/gvec_v2.sh; RB:9.
70. T2:7–8. The manifest (61 lines), the hashes file (13 lines) and note `eb63ab79…9430`. CONFIRMED. RB:11, :13, :15; shasums.
71. T2:9–10. Harness, stand-in (286 of 286) and snippet test (53 of 53 on 48). CONFIRMED. RB:17–21; prereview shasums; T2:254.
72. T2:11–12. `gvec_v1.sh` `f349e17d…a1ad` and the v1 out raw. CONFIRMED. RB:22–24; RESULTS.md:541; the raw is tracked.
73. T2:14. The brief is `f6898d67…a4ec`, 105 lines. CONFIRMED.
74. T2:15–17. What the brief named. CONFIRMED. RB:8 and :26–38. "A3's code" means box_e0_corpus.py and extract.py (GJ :756–759).
75. T2:18–20. The ten questions. CONFIRMED. RB:46–70.
76. T2:21–22. What the brief asked for and quoted. CONFIRMED. RB:72–105.
77. T2:24–25. §2 is 202 lines and `98dc4465…1fb3`, and names scratch files only by S paths. CONFIRMED. `sed -n 70,271p` of T2 into shasum gives 98dc4465…, and `cmp` is equal. T2:70–271 has 0 matches for /private, /Users or /tmp/. The `jq` extraction is Code's act.
78. T2:27. The totals. CONFIRMED. T2:74.
79. T2:31–32. The relayed bytes; the manifest and hashes file unchanged. CONFIRMED. shasums and `wc -l`; RB; REC:25–31.
80. T2:34–37. F1 applied, with its cases. CONFIRMED. SH:67, :164–166, :242–243; HAR:31–33, :43, :64–66, :84. What each case prints is not in the sources.
81. T2:38–39. F2 applied as `os.fsencode`; the note says so. CONFIRMED. SH:179 and :286; NOTE:103–104 and :151–152.
82. T2:40–43. F3: the re-derivation, its fixtures and its cases. CONFIRMED. SH:299–307 uses the same arithmetic as gvec.py:266–271. Fixtures at SNIP:41, :51–61, :81; cases at HAR:81–83 and :90.
83. T2:44–45. F4: `--ignored` and its three cases. CONFIRMED. SH:99; HAR:9, :41, :87.
84. T2:45. "the staging case now also fails at the changed set". NOT CHECKABLE. HAR:85 is cut off before the changed-set field.
85. T2:46. F5 and the workmodels case. CONFIRMED. SH:65 and :89; HAR:119.
86. T2:47. F6. CONFIRMED. SH:309.
87. T2:48–49. F7, in the note. CONFIRMED. NOTE:73–75, :84–85, :112–114.
88. T2:50. F8 applied. NOT CHECKABLE: the relayed builder is not among the sources. The premise holds: S/…/prereview/make_manifest3.sh:9–10 names make_manifest2.sh.
89. T2:51–55. M1–M8 are each met by a case and killed. CONFIRMED.
    - Cases: stwarn HAR:17 (M1); the ten stop* print cases HAR:100–109 (M2); runtail* :64–66 (M3); smokemkstaging and smokemkgvec :39–40 (M4); statusfail :8, smokeindex :42 and runindex :88 (M5); rundot :68 (M6); optlocks :7 (M8).
    - M7: SNIP:116, 23 of 23 killed.
    - MUT's R1–R11 are 30 mutants, absent from the first draft's mutants.sh, with no R7, and all killed. The R-to-M mapping is by name only.
90. T2:56. O1, O2, O4, O5, O6 and O11 ask for nothing. CONFIRMED. T2:172–228 and :254.
91. T2:56. O3: the box printed 571/571. CONFIRMED. OUT:69.
92. T2:56–58. O7 and the workbeside case. CONFIRMED. SH:90; HAR:118; NOTE:50–52.
93. T2:58. O8. CONFIRMED. REC:30–31. The relayed note has no `@MUT` slot; the first draft had one.
94. T2:58–59. O9, the stand-in's changes. NOT CHECKABLE: the relayed stand-in is not among the sources.
95. T2:59–61. O10's cases. CONFIRMED. HAR:125, :122, :123, :124, :8, :34, :70; SH:266–276.
96. T2:62. The reviewer's departures are in the run's entry. CONFIRMED: T1:100–105, subject to item 63.
97. T2:64–66. The tests after. CONFIRMED. HAR:126; MUT:39, :80, :83; _n5:1; _r9:1; NOTE:143–146; SNIP:1, :92, :116.
98. T2:64. The snippet test ran "on the relayed bytes". CONFIRMED. SH:140–145, :173–207 and :279–327 hash to 1922c60c, 5e843169 and d20bc1c0, which are SNIP:1's prefixes.
99. T2:64. The harness and the mutation pass ran "on the relayed bytes". NOT CHECKABLE: neither output prints the script's hash.

TOTALS: 99 items. 84 CONFIRMED, 5 IMPRECISE (items 27, 39, 43, 54, 63), 1 FAIL (item 60), 9 NOT CHECKABLE.

OBSERVATIONS
1. REC has no section titled "departures". Both acts are in its §7 (:112–119 and :136–138). Writing "as its record's §7 states the acts" would point the seat to them.
2. T1:96–97: `git log -1 --format=%B` prints the whole message. Item 1 permits `--format` only "of ids, subjects and commit times", so the departure is the format as well as the missing pathspec.
3. T2:29's heading, "applied before the relay", also covers O3's after-the-run result and O8, which is met by the relay itself.
4. Item 84: HAR cuts each line at 160 characters. Check the staging-case clause by tool before the commit, or drop it.
5. T2:8 gives no line count for the first-draft note; it has 127 lines.
6. T1:62: the first run's entry gave its +11's arithmetic (RESULTS.md:586). Here the +11 is 14 checks in place of three skip lines (T2:209–210), which the text could state.
7. T1:33–34: naming `order` and `alt_order` would make "16 of 16" reproducible from the entry alone.
8. T1:76–79: the copy-back sentence names fourteen files, so "fifteen" doesn't add up within the paragraph. The record itself is named only in the departures.
9. The laptop test outputs (HAR:119, :124, :126; MUT:83; _n5:2; _r9:2; SNIP:1, :92) print full paths with the home-folder prefix. None is among the eleven raws; any later commit of them needs the scrub.
10. _n5:2 and _r9:2 print "mutants: 82; killed 1". The 82 is the roster, not the number of mutants that run.

DEPARTURES
1. One `jq -r 'keys_unsorted | join(", ")'` over S/step4b/gvec2/box/rec/data/n/gvec/gvec.json, which printed its 18 top-level key names. jq runs its own filter language; if "no interpreter of any kind but shasum" covers it, this is a departure. After it I used only the Read tool, grep and sed on that file.
2. Two `git log` runs whose `--format` held `%ad` (author dates) where item 1 names commit times. One ran over the tree with item 3's pathspec and the mf3 exclusion; the other ran on the named file .gitignore. Each printed ids, author dates and subjects.
3. Stated plainly; the brief's rules do not bar these:
   - Reads beyond the named sources: RESULTS.md outside the three named entries (a grep printing 30 entry head lines; a grep for the backend id; backend-ext-2's entry at :1561–1563, :1592–1595 and :1603–1606); PROPOSAL-n-bk-reconciliation-v0_2.md:81; ADDENDUM-n1-…:52; and ROUT in full.
   - `git show` of .gitignore at da7bdec and its parent, and of scripts/n_sessions.py and valence_core/n/gvec.py at 616e940, piped into grep or shasum.
   - Two `git grep -F` runs in item 3's form with the mf3 exclusion. Their matches printed tracked lines, some holding a guard-marker word in the output only. None was under ckpt, reports or mf3.
   - `wc -c` and `od -c` on the four .npy scratch copies.

No argv held a guard marker. Nothing under data/mf3, data/*/ckpt or data/*/reports was read, listed, sized or timed. I ran no git status, wrote no file and used no network. I read nothing in S beyond the brief's named files; one existence test was on the absent `_valuescheck.md`, a name T1 lists.
