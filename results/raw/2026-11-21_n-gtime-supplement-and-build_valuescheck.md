# n — G-TIME-n's supplement (Q8) and BUILD texts: the blind values-check, as returned, with every disposition

PI date 2026-11-21. Code (the n-build session).

**What was checked.** One blind pass by a subagent over five drafts, at HEAD `2ca24e8`:
- T1, the supplement, sha256 `a51d9139…172d` (92 lines);
- T2, its RESULTS.md entry, `4acbe031…b8ce` (33 lines), with two placeholders not to be checked, for this check's
  tallies and departures;
- T3, the BUILD's RESULTS.md entry, `3e92ff13…e8a4` (128 lines), with four placeholders not to be checked, for this
  check's tallies and the counts of Code's last sweep;
- T4, the BUILD's review raw, `b8a6d845…0f7e` (300 lines): its head and §1, and its §2 only for being byte-equal to
  the review's report;
- T5, the BUILD's self-test raw, `8f999e11…838b` (59 lines).

**The checker's brief** was a file in Code's scratch, `S/step4b/gtime/vc/vc_brief.md` (`ef8ae421…ec32`, 114 lines).
The prompt named it by its path and sha256, for the checker to check and read whole. It:
- named the texts and the sources. In Code's scratch, by name and sha256: draft 4 (the bytes to be committed), draft
  3 and their delta, drafts 1 and 2 for their hashes, the .gitignore draft, the review's brief and report, the three
  self-test outputs, and the seat block's unused third entry. In the repository, the files the texts cite, at HEAD,
  each checked tracked and clean, and the package digest's form;
- barred any interpreter but `shasum` (`awk` among them), any write, any network, any guard marker in an argv (a grep
  pattern included), globs over the root, `results/raw/` or a folder of marker-named files, and Q-F3's folder by its
  plain name in any argv;
- barred anything under `data/m[f]3`, any whole-tree git status, any read, listing, size or time of a ckpt or reports
  file, any transcript, and anything in Code's scratch but the named files;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec with `':!data/m[f]3/**'` on every
  git command over the tree.

**The report** is in §3, extracted verbatim by `jq` from the hand-back in the subagent's own transcript (223 lines,
sha256 `d8d53dc003a8bb7d4f30cde00c8e756518c100839d47495f1c1313e4af0c0ec2`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 128 items: 97 CONFIRMED, 7 IMPRECISE, 5 FAIL, 19 NOT CHECKABLE; and 9 observations.

**The checker's departures,** as its report states them, are in the supplement's entry, for the seat to class.

## 1. Dispositions

Every IMPRECISE item and every FAIL is applied or met, in the words below or the checker's. Every observation is
applied or met. The five FAILs are one finding, M8 (item 108), and it is met in the build, not only in the text.
Dispositions on T1 and T2 are in this commit's texts; §2 gives their check by tool. Dispositions on T3–T5 are applied
in the BUILD's texts, whose entry gives their check.

- **Item 108 (FAIL), T4:84–86, with items 6, 64, 95 and 126.** M8 survived draft 4. Its case called
  `same_filesystem` directly, and no case ran the stage's own call to it, so the guard (draft 4:4221) changed to
  `if False:` passed every check.
  - Met in the build: draft 5 (`4616f9c3…2553`, 5,208 lines; +17 −2 on draft 4) adds the stage-level case of
    observation 1. `same_filesystem` is patched to return False for one run of the stage, and restored. The run must
    refuse before any read, with exit 2, no weights loaded and no report, on a REFUSED line that names the stage
    root's filesystem. With the guard changed to `if False:` that run would not refuse, so the case kills M8.
  - Draft 5's self-test runs in a battery window of its own before the BUILD's commit. Its count, by arithmetic, is
    634 on the laptop and 645 on the box.
  - The BUILD's texts then say: the seven findings built in by draft 4, and a kill for every mutant in draft 5, M8's
    by its new case. T1 (item 6) no longer states the BUILD's dispositions, mutants or self-test count. It says the
    BUILD's commit carries the review's report whole, with every disposition and the self-test of the driver it
    commits.
- **Item 47 (IMPRECISE), T3:5–18.** Applied in the checker's words: the refusals in `_gtime_prepare`'s order, with
  the `--ruling` refusal added. Observation 8 is met: `check_stage_identity`'s SchemaError exits 1 and is not in the
  list.
- **Item 51 (IMPRECISE), T3:21–22.** Applied in the checker's words: after the load, the loaded adapter's
  provenance is checked again, and the checkpoint's shape against the identity's.
- **Items 70 and 111 (IMPRECISE), T3:65–66 and T4:96–99.** Applied in the checker's words: a re-run of record after
  a box change must first move the committed outputs aside. The stage moves nothing; it refuses while its artifact
  is on disk.
- **Item 72 (IMPRECISE), T3:69–71.** Met in the build. Draft 5's docstring introduces the PINs as listed in short,
  as sent but for GT9's benchmark and GT11's outputs, which are as built. The BUILD's entry drops the owed-wording
  bullet and says what draft 5 changed.
- **Item 98 (IMPRECISE), T4:49–56.** Applied: "Applied, with a case for each". The `same_filesystem` bullet says
  draft 4's case tested the helper alone, and draft 5's runs the stage's own call (item 108).
- **Item 127 (IMPRECISE), T5:56–58.** Applied in the checker's words: the 14/3 split as G-VEC's box self-test
  recorded it, and G-CAL-n's, the last, the same 11.
- **O1 (M8's two fixes).** The second is taken, as item 108.
- **O2 (four runs or three).** Applied in T3: the transcript reads confirmed the window steps of runs 1, 3 and 4.
- **O3 (the sweep's start).** Applied in T3: `2ca24e8`'s entry gave its sweep from `deabf3f`'s window on, and the
  sweep as carried ran from `411b15c`'s, as the unused third entry had it.
- **O4 (the .gitignore reviewed and the one committed).** Applied in T3 and T4. Both name gitignore_v2's sha256 and
  say its block changed after the review, on O2. The reviewed draft admitted all three cells.
- **O5 (T1's cited forms).** Applied: "F and O numbers are the review's."
- **O6 (the precedent's form).** Applied: T1 opens with §0, the short form, and cites the report's §2 by sha256.
- **O7 (F2's "six").** Met with item 98: the title keeps the report's word, and each bullet says what its case is.
- **O8 (`check_stage_identity` exits 1).** Met with item 47.
- **O9 (schema.py:154–155).** Applied in T1: the report's "no margin or other per-read model output" is quoted from
  it.

## 2. The edits, checked by tool

The edits to T1 and T2 were made to new versioned copies. Each was recovered from this session's transcript by `jq`
and replayed on the draft the checker read, each change's old text found exactly once. The results are byte for byte
the revised drafts, so nothing else changed after the check:
- the supplement, 5 of 5 edits; its entry, 4 of 4.

Besides the findings, the edits carry three things:
- the nudge's wording, in T1's head and T2, on the coordinating session's correction of 2026-11-21: the PI has not
  decided to hold the nudge, and the coordinating session has recommended that one nudge carry Q1–Q8;
- one rewrap of a line over 120 characters;
- T2's values-check paragraph and the checker's departures, in place of their placeholders.

After the edits, one placeholder was filled by tool: the entry's count of these edits.

## 3. The report, as returned

```text
BLIND VALUES-CHECK: the G-TIME-n supplement (T1, T2) and G-TIME-n's BUILD texts (T3, T4 head and §1, T5)

Checked first, by tool:
- The brief's sha256 matched (shasum), and the brief was read whole. HEAD is 2ca24e8, whose parent is c9d35e2.
- Every named repository file is tracked and clean (rev-parse equals hash-object). That covers all 16 valence_core/n/*.py and data/n/gcal/gcal.json.
- All 17 named scratch files matched their sha256s. Line counts: T1 92, T2 33, T3 128, T4 300, T5 59, draft 4 5,193, draft 3 5,057, review brief 93, report 189, commit_v3 entry 97. Drafts 1 and 2 are 4,996 and 5,034.
- S/step4b/gtime/draft4/delta_from_draft3.diff is byte-equal to `diff` of draft 3 against draft 4.
- Numstat from the repository root:
  - HEAD's driver to draft 4: +1422 −6;
  - draft 3 to draft 4: +156 −20;
  - HEAD's .gitignore (383 lines) to S/step4b/gtime/commit/gitignore_v2 (397 lines): +14 −0, one block at :331–344.
- The package digest over HEAD's blobs (16 files from `git ls-tree`, in package_sha256_of's form) is 06b55761052508f93fb67993b4b4c7574483aa38d2168b8254b3c0b7417a1d39.
- T1:35–40, joined, equals the report's O2 line byte for byte. T4 from line 112 is `cmp`-equal to S/step4b/gtime/review_report.md.
- Check counts:
  - draft 4 has 193 `chk(` lines against draft 3's 185;
  - check_gtime's tamper loop has 8 cases against draft 3's 6;
  - a static count of draft 4's _gtime_selftest gives 54 executed checks, plus 1 environment check in cmd_selftest, which is 55 = 633 − 578.

Names used below:
- draft 4 = S/step4b/gtime/draft4/n_sessions.py;
- B = the block;
- the report = S/step4b/gtime/review_report.md. It is equal to T4:112–300, so it is cited by T4 lines;
- "spec raw" = results/raw/2026-11-21_n-gtime_spec.md;
- n = PROPOSAL-n-bk-reconciliation-v0_2.md.

ITEMS

T1 (S/step4b/gtime/supp/supp_v1.md)

1. T1:3–4. The block, results/raw/2026-11-21_n-gtime-starred-seven_code-to-design_STOP.md, is committed at 2ca24e8. CONFIRMED. `git show --name-status 2ca24e8` (item 3's pathspec plus `':!data/m[f]3/**'`) shows A for the block, the spec raw and the values-check raw, and M for RESULTS.md.
2. T1:8. The seven are GT1, GT4, GT8, GT9, GT10, GT12 and GT16 (Q1–Q7). CONFIRMED. B:1, B:351–374.
3. T1:9. The BUILD is drafted on GT1–GT17 as PINs, in the driver alone. CONFIRMED. Draft 4:181–232. Only the driver and .gitignore change, and the package digest does not move.
4. T1:9. The review of draft 3 found no BUG. CONFIRMED. T4:123.
5. T1:10. Seven of the review's eleven findings are built in. CONFIRMED. F1, F2, F3, F5, F6, F7 and F9 of F1–F11 (items 97–105).
6. T1:10. "a kill for each of its 13 surviving mutants". FAIL: M8 survives (item 108). Replace with: "Draft 4 builds in seven of the review's eleven findings and a kill for twelve of its 13 surviving mutants (M8's device comparison is tested inside `same_filesystem`, but no case runs the stage's guard that calls it), and passed its self-test, 633/633."
7. T1:10–11. 633/633. CONFIRMED. S/step4b/gtime/selftest_run4.txt; its .exit reads "exit 0" and its .err is 0 bytes.
8. T1:11–12. The BUILD's commit carries the report whole, as results/raw/2026-11-21_n-gtime-build_review.md. CONFIRMED. `cmp` equality (above); the path is the brief's path for T4.
9. T1:13–14. O2 raises Q8 on GT11, and the default is the safer form, §2 (ii). CONFIRMED. T4:281; gitignore_v2:337–343.
10. T1:16–18. The cited forms: B at 2ca24e8; n:line is v0.2 (n:2); C is CLAUDE.md; the spec raw is committed with the block. CONFIRMED. Same git show as item 1.
11. T1:24. The quotation of GT11 as routed. CONFIRMED. Spec raw:153.
12. T1:25–28. The three cells, named by schema.cell_filename: six shadows at d = 0, and twelve steered reads at +1 and +1/2 on runs 0, 32, 64, 95, 127 and 159. CONFIRMED. valence_core/n/schema.py:525–529 and DOSE_SLUGS at :297; B:65–71; draft 4:3748–3749.
13. T1:29–31. RECORD_FIELDS holds logprob_S, logprob_U, margin, restricted with its pick, and fidelity. CONFIRMED. schema.py:341 ff., RESTRICTED_FIELDS "pick", and FIDELITY_FIELDS.
14. T1:31–32. .gitattributes:19–21 and its quotation. CONFIRMED. .gitattributes:19–20 holds the quotation (wrapped) and :21 the `-diff` line.
15. T1:35–40. O2, verbatim. CONFIRMED. Byte-equal to T4:281.
16. T1:41–43. The campaign reads the same six sessions at +1 and +1/2 in N1-V, and the quotation of n:148, "No looks (§2.5)." CONFIRMED. schema.py:303 (ARM_CELLS) and :139–141; B:112–113; n:146–148.
17. T1:44–46. The shadow cell holds d = 0 reads alone; the BACKEND extension's two admitted cells are at d = 0; .gitignore:294 and :300. CONFIRMED. Both lines are as cited, and gitignore_v2 has them at the same lines.
18. T1:47–49. The report and the artifact hold no margin and no log-probability; the projection needs only durations; GT13. CONFIRMED. schema.py:154–155; draft 4:4064–4067, :4116 and the margin tamper case at :4797; draft 4:4031–4061; spec raw:159–162.
19. T1:53. The coordinating session gave three facts. NOT CHECKABLE.
20. T1:54–55. `-diff` at .gitattributes:21 and item 2; m's and p's checkpoints, which carry picks, are committed that way. CONFIRMED. .gitattributes:6, :14 and :21; .gitignore:221, :239–242 and :369–372 (not listed, since listing is barred).
21. T1:56–57. The quotation of C:359. CONFIRMED. CLAUDE.md:359.
22. T1:58 and T1:75. The BACKEND extension's committed cells were d = 0 only, and the shadow cell is committed as theirs were. CONFIRMED. RESULTS.md:3357–3358; schema.py:146–150.
23. T1:60–61. The capture arrays stay on the box in every option, as at the BACKEND extension. CONFIRMED. .gitignore:285–286; spec raw:154; gitignore_v2:331–336.
24. T1:62–67. Option (i) is two lines. Option (ii) is the default: it admits the shadow cell, the report and the artifact, and the report's `cells` hold json_sha256 and capture_sha256. CONFIRMED. gitignore_v2:337–343; schema.py:1159–1161.
25. T1:68–73. Options (iii) and (iv). NOT CHECKABLE: these are plans.
26. T1:79–81. Q8; the BUILD commits with (ii). CONFIRMED. gitignore_v2:337–343.
27. T1:85–86. GT9 at B:203–246, and its quotation. CONFIRMED. The quotation is at B:238.
28. T1:86–89. What rekeyed moves; every other field the template's; the CROSS-RECORD PROPERTIES paragraph; timing unaffected; F8. CONFIRMED. Draft 4:3945–3958; schema.py:115–119; T4:166.
29. T1:90. GT4 at B:109–159, and its quotation. CONFIRMED. The quotation is at B:144.
30. T1:91–92. Every pin is checked at every invocation, a smoke's too (F10). CONFIRMED. Draft 4:4241–4290; only the driver check, at :4248, depends on smoke. T4:170.

T2 (S/step4b/gtime/supp/entry_v1.md)

31. T2:1–4. The heading and the block's link. CONFIRMED. The link is the brief's commit path for T1.
32. T2:6. The seven are committed at 2ca24e8. CONFIRMED. Item 1.
33. T2:6–7. By the coordinating session's word, the PI has not yet nudged the seat. NOT CHECKABLE.
34. T2:8–9. One review, no BUG; O2 is Q8; seven of eleven; 633/633. CONFIRMED. Items 4, 5, 7 and 9.
35. T2:10. The BUILD is not committed, and its commit follows with the report whole. CONFIRMED. HEAD's driver is 593a140d…a549, not 24b0cd44…22aa.
36. T2:12–17. The summary of T1 §1–§4. CONFIRMED. T1:22–92.
37. T2:18–19. The run waits for Q1–Q8, and (ii) is the default. CONFIRMED. T1:14 and T1:80.
38. T2:20. Nothing ran on a model. NOT CHECKABLE.
39. T2:21–22. The values-check's scope. CONFIRMED. The brief's T1–T5.
40. T2:24. The path of the values-check raw. NOT CHECKABLE: the file is not yet written.
41. T2:26. Code's departures are in the BUILD's entry. CONFIRMED. T3:91–118.
42. T2:28–30. Committed by path. CONFIRMED. The brief's account of the supplement's commit.
43. T2:32. The commit-time count is 0, and nothing is pushed. NOT CHECKABLE.

T3 (S/step4b/gtime/build/entry_v2.md)

44. T3:1–3. The `gtime` and `gread-bench` commands; n §8 step 11; "Build on the PINs"; not run. CONFIRMED. Draft 4:5076–5077 and :5098–5117; n:159 ("11. G-TIME-n; the PI sets the cap."); spec raw:191.
45. T3:4. valence_core/n/ stays at 06b55761…1d39 (LOCK-n v0.1 §18). CONFIRMED. The computed digest; LOCK-n.md:781; draft 4:3775.
46. T3:5–6. The stage refuses before any read, with exit 2 and a REFUSED line. CONFIRMED. Draft 4:4338–4345.
47. T3:5–18. The list of what must hold, in the order given. IMPRECISE. The list's content holds, but the order is not _gtime_prepare's, and one refusal is missing.
    - The code's order: the weights (:4244), then the driver (:4248), then the rendering (:4255), then LOCK-n v0.1's inputs (:4257), then the R6 bridge, n's backend identifier and the package/closure (:4264–4274), then the read plan (:4285), then prior_state (:4290).
    - T3 puts the driver and the lock's inputs after the package.
    - A `--ruling` that is not a file is also refused (:4234–4236), and the list omits it.
    - Replace T3:6–18 with: "unless all of these hold, in this order:
      - the paths are the stage's own, or a smoke's (1–18 reads, no resume) new folder outside the repository, and the artifact is not yet written;
      - the bench folder exists outside the repository, on the stage root's filesystem;
      - the pod, the cuBLAS setting and the stream's known answer are the characterized ones, and each `--ruling` names a file;
      - the weights are the lock's;
      - a run of record runs HEAD's committed driver;
      - the rendering is the render of record's;
      - LOCK-n v0.1's inputs are the lock's (`gtime_lock_inputs`): [T3:14–16 as written];
      - the environment's provenance bridges to the characterization's identifier (R6), and n's backend identifier, the package and its twelve-file closure are the lock's;
      - the campaign's read plan under the stage's identity is the lock's (`campaign_counts`);
      - a second run finds no records or report of its own unless it resumes, and a resume's rulings match its standing pauses (`prior_state`)."
48. T3:14–16. What gtime_lock_inputs checks. CONFIRMED. Draft 4:3858–3883; HEAD's gcal_gvec_inputs (scripts/n_sessions.py:2666 ff., which requires a G-VEC PASS).
49. T3:20. Every check but the driver's holds at a smoke too. CONFIRMED. Draft 4:4248.
50. T3:20–21. G-VER runs before the load, and its STOP exits 2. CONFIRMED. Draft 4:4291–4299 and :4346–4347.
51. T3:21–22. "the provenance and the checkpoint's shape are checked again". IMPRECISE. The provenance is checked again (:4301), but the shape is first checked after the load (:4303), against env.shape, which is taken unchecked at :4262. Replace with: "After the load, and before any read, the loaded adapter's provenance is checked again, and the checkpoint's shape against the identity's."
52. T3:22–24. The 18 reads go through the runner. On COMPLETE: the records are read back, io_bench re-keys the first +1 record, and the artifact data/n/gtime/gtime.json (n-gtime-v1) is checked by check_gtime. CONFIRMED. Draft 4:4349–4377, :3745–3747 and :4082.
53. T3:24–25. Exits 0, 3 and 1. CONFIRMED. Draft 4:4343–4352 and :4395.
54. T3:26. gread-bench runs on the laptop, model-free, and is refused on a pod. CONFIRMED. Draft 4:4449–4459; the self-test's case at :5048–5056.
55. T3:27–29. The docstring lists GT1–GT17 in short. CONFIRMED. Draft 4:205–232; B:351–374.
56. T3:30–34. The .gitignore: +14; what is admitted and what is kept on the box; O2; GT11's form two lines away. CONFIRMED. Numstat 14 0; gitignore_v2:331–343; spec raw:153.
57. T3:35. Tested by dry-run adds. NOT CHECKABLE.
58. T3:37–38. "621/621", HEAD's 578 plus 43; "623/623"; "633/633". CONFIRMED. The three run outputs; RESULTS.md:1251 records 578/578. HEAD's driver blob is ef105f1's.
59. T3:39. Each run had exit 0 and an empty stderr. CONFIRMED. The three .exit files read "exit 0" and the three .err files are 0 bytes.
60. T3:39–40. The battery windows, the empty temporary folder, and PID 8051. NOT CHECKABLE.
61. T3:41. The box count is 644. CONFIRMED. 633 + 11; RESULTS.md:1785–1786 and :1470–1471.
62. T3:43–45. The review raw's link; no BUG; 11 findings (5 RISK, 6 NIT), 13 mutants, 7 box risks, 6 observations; no departures. CONFIRMED. T4:123–291.
63. T3:46. F1, F2, F3, F5, F6, F7 and F9 are built in. CONFIRMED. The delta.
64. T3:46. "and a kill for every mutant". FAIL: item 108. Replace with: "draft 4 builds in F1, F2, F3, F5, F6, F7 and F9, and a kill for every mutant but M8: `same_filesystem` is tested directly, but no case runs the stage with a bench folder on another device, so the guard at draft 4:4221 changed to `if False:` still passes."
65. T3:50–53. F4. CONFIRMED. Draft 4:4815–4821 (two loads); valence_core/n/runner.py:548.
66. T3:54–59. F8's three wordings. CONFIRMED. Spec raw:69–70 and :123; B:174–175; T4:163–166.
67. T3:60–61. F10. CONFIRMED. Item 30.
68. T3:62. F11 is not adopted. CONFIRMED. T4:172; the two traps at draft 4:4940–4951.
69. T3:63–64. B5. CONFIRMED. Draft 4:4271 (exact) and :4563–4564 (inclusion only).
70. T3:65–66. B7: "a re-run ... first moves the committed outputs aside". IMPRECISE. The stage moves nothing; it refuses while its artifact is on disk (:4213–4214). The review wrote "must first move" (T4:260). Replace with: "**B7:** `GTIME_ROOT` is fixed, so a re-run of record after a box change must first move the committed outputs aside. Whether it re-runs is the PI's (GT16)."
71. T3:67–68. B1, B2 and B6 are carried to the launch files. CONFIRMED. T4:231–238 and :252–255.
72. T3:69–71. The owed wording names GT11's line alone. IMPRECISE. The docstring's GT9 line (draft 4:218–220, "the stage's first +1 record re-keyed 160 times") is also not as sent: GT9 as sent "appends 160 example records" (spec raw:127). Replace with: "the docstring introduces the PINs as "each as sent" in the spec raw's §1, but two of its lines are the build's forms: GT9's, whose benchmark re-keys the stage's first +1 record where GT9 as sent appends "160 example records", and GT11's, the steered cells kept on the box with O2 named."
73. T3:73–79. The kit's pathspec, and which windows fell under each kit. NOT CHECKABLE. The eleven commits exist and fall in that order (`git log --no-walk`).
74. T3:82–84. The deabf3f window's seven kit commands and Code's four; the overlay script's six; the two sed commands 2ca24e8's entry declares. CONFIRMED. RESULTS.md:83–87.
75. T3:80–82. The sweep ran from 411b15c's window on, with its counts there. NOT CHECKABLE. It matches S/step4b/gtime/seat/commit_v3/entry.md:58–63, but 2ca24e8's entry says "from deabf3f's commit window on" (RESULTS.md:81–82). See observation 3.
76. T3:86. 2ca24e8's entry named the survey's id alone. CONFIRMED. RESULTS.md:103–104.
77. T3:85–86. The gate's id list held both ids. NOT CHECKABLE.
78. T3:87–90. The seat block's grants. NOT CHECKABLE. Consistent with commit_v3/entry.md:73–75.
79. T3:92–109. The session's commands. NOT CHECKABLE.
80. T3:101–108. The rules cited: item 1 names commit times, `--name-only`/`--name-status` and `git ls-files`; the briefs bar listings under data/*/ckpt and awk. CONFIRMED. List of record item 1; review brief:3 and :79–80.
81. T3:111–113. Neither 2ca24e8's entry nor its unused third version declares the two jq listings, and the quotation "once to find the two departures above". CONFIRMED. RESULTS.md:73–76; commit_v3/entry.md:50–53.
82. T3:113–114. "was two calls"; the first .gitignore's dry-run adds. NOT CHECKABLE.
83. T3:115. The reviewer's departures: none. CONFIRMED. T4:291.
84. T3:116–120. The non-shell activities, and the gate's new version. NOT CHECKABLE.
85. T3:121–124. Committed by path. CONFIRMED. The brief's account of the BUILD's commit.
86. T3:126–127. The count, nothing pushed, and what comes next. NOT CHECKABLE.

T4 (S/step4b/gtime/build/review_v1.md, head and §1)

87. T4:5–7. HEAD 2ca24e8; 593a140d…a549 to f4e2c8b9…d608, 5,057 lines; 1f2461bd…58b8. CONFIRMED. shasum; review brief:10–16; T4:115–119.
88. T4:9. Draft 3 passed 623/623. CONFIRMED. selftest_run3.txt.
89. T4:11–12. The brief is 9ab6524c…afeb, 93 lines, checked by sha256. CONFIRMED. T4:115.
90. T4:13–22. What the brief named, asked and barred. CONFIRMED. Review brief:1–93.
91. T4:24–26. §2: 189 lines and its sha256; scratch files named S/... only. CONFIRMED. `cmp`, `wc`, `shasum`; no full path in the report (grep).
92. T4:24. Extracted verbatim by `jq`. NOT CHECKABLE.
93. T4:28–34. In sum. CONFIRMED. T4:123–291.
94. T4:36. 24b0cd44…22aa, 5,193 lines; F1, F2, F3, F5, F6, F7 and F9 are built in. CONFIRMED.
95. T4:36. "and a kill for every mutant". FAIL: item 108. Replace with: "builds in F1, F2, F3, F5, F6, F7 and F9 and a kill for every mutant but M8, whose guard (draft 4:4221) has no case through the stage."
96. T4:36–37. 633/633. CONFIRMED.
97. T4:42–48. F1. CONFIRMED. Draft 4:4320, :4165 and :4176–4181; runner.py:274; draft 4:4703–4705 and :4761–4775. These kill M2–M5 and M12.
98. T4:49–56. F2: "Applied, one case each", with "(M8)". IMPRECISE.
    - The cases are built as said: :4875–4886, :3961–3966 with :4651–4663, :4910–4916, :4887–4897 and :4532–4552.
    - But the site/valence guard has two cases.
    - And the same_filesystem case tests the helper, not the stage's call at :4221.
    - Replace T4:49 with "**F2 (RISK), six guards without a case. Applied, with a case for each:**".
    - Replace T4:51 with "`same_filesystem`, the device check factored out with its stat injectable, failing for another device (M8's comparison only: no case runs the stage's own call to it, draft 4:4221);".
99. T4:57–59. F3. CONFIRMED. Draft 4:5026–5047.
100. T4:60–63. F4. CONFIRMED. Item 65.
101. T4:64–66. F5. CONFIRMED. Draft 4:3993 and :4003–4004. No case induces a cleanup failure.
102. T4:67. F6. CONFIRMED. Draft 4:3750.
103. T4:68–70. F7. CONFIRMED. Draft 4:4087–4092, :4113, :4128, :3791 and :4789–4796; LOCK-n.md:464.
104. T4:71–78. F8. CONFIRMED. T4:163–166.
105. T4:79. F9. CONFIRMED. Draft 4:4646–4649.
106. T4:80–81. F10. CONFIRMED.
107. T4:82–83. F11. CONFIRMED. T4:172.
108. T4:84–86. "Each is killed in draft 4 by the case its row names ... M6–M9 by F2's cases". FAIL.
    - M8 (T4:206–209) is the guard changed to `if False:`. In draft 4 that guard is :4221, `if not same_filesystem(bench, root_p):`.
    - Its only case (:4660–4663) calls same_filesystem directly. No case runs run_gtime with a bench folder on another device, and no check expects "not on the stage root's filesystem", which occurs only at :4222.
    - So `if False:` at :4221 passes every check. The other twelve mutants are killed as stated.
    - Replace with: "**M1–M13.** M1 by F2's re-run case; M2–M5 and M12 by F1's literals; M6, M7 and M9 by F2's cases; M10 by F3's spy; M11 by a check that the production environment's benchmark appends 160 records; M13 by F9's text. M8 is not killed: F2's case tests `same_filesystem` itself, and no case runs the stage with a bench folder on another device, so the guard at draft 4:4221 changed to `if False:` passes every check."
109. T4:87–92. B1, B2, B6, B3 and B4. CONFIRMED. T4:231–255.
110. T4:93–95. B5. CONFIRMED. data/n/gcal/gcal.json names exactly LOCK_CLOSURE's twelve module paths (`grep -o`); draft 4:4271 and :4563–4564.
111. T4:96–99. B7. IMPRECISE. The copy-back sentence holds (draft 4:4074–4075; schema.py:1159–1161), but "moves the committed outputs aside first" reads as something the stage does; see item 70. Replace with: "`GTIME_ROOT` is fixed, so a re-run of record after a box change must first move the committed outputs aside. Whether it re-runs is the PI's (GT16)."
112. T4:100–108. O1–O6. CONFIRMED. T4:264–289; gitignore_v2:337–343.

T5 (S/step4b/gtime/build/selftest_v1.txt)

113. T5:1–2. n §8 step 11, and n §3's G-TIME-n paragraph. CONFIRMED. n:159 and n:118.
114. T5:4–5. The same bytes at c9d35e2 and 2ca24e8; the sha256; +1422 −6. CONFIRMED. Both rev-parse to blob 93951020…
115. T5:6. The .gitignore's +14 lines do not enter the self-test. CONFIRMED. Draft 4 never mentions gitignore.
116. T5:7–9. The digest 06b55761…1d39, in package_sha256_of's form, over HEAD's clean files. CONFIRMED. Computed; valence_core/m/resume.py:328–350; LOCK-n.md:781.
117. T5:9. "over every overlay below". NOT CHECKABLE.
118. T5:10–11. The self-test holds the measured digest to the lock's. CONFIRMED. Draft 4:4560–4565.
119. T5:13–15. The HF cases are skipped and counted as skipped, and the schema's cases are one line. CONFIRMED. scripts/n_sessions.py:9, :246–247, :1539 and :3676; valence_core/n/hftiny.py:56.
120. T5:16–26. The overlays (173 files), the scripts, the command, the windows, and PID 8051. NOT CHECKABLE.
121. T5:28–32. Run 1: its sha256s, exit 0 and its line. CONFIRMED. `shasum`; T5:32 with its five leading spaces cut `cmp`-equals selftest_run1.txt.
122. T5:33. 578 + 43, where 43 is 42 in _gtime_selftest and 1 environment check. CONFIRMED. RESULTS.md:1251; draft 4:410–414; draft 4's 54 checks less 1 (draft 2), 1 (draft 3) and 10 (draft 4) leaves 42.
123. T5:35–37. Draft 2: its sha256, observation 4, one check more. CONFIRMED. results/raw/2026-11-21_n-gtime-starred-seven_valuescheck.md:248; RESULTS.md:60–62. "Never ran on its own" is not checkable.
124. T5:39–45. Run 3: the second trap and one check more. CONFIRMED. Draft 4:4940–4958 lies outside the delta, so it is draft 3's code; `cmp`.
125. T5:47–54. Run 4: +156 −20, the F list, eight checks plus two tamper cases (ten), and its output. CONFIRMED. Draft 4:4793–4802; `cmp`.
126. T5:50–51. "with a kill for each surviving mutant, M1-M13". FAIL: item 108. Replace with: "F1, F2, F3, F5, F6, F7 and F9, with a kill for each surviving mutant but M8 (M1-M13; M8's comparison is tested in same_filesystem, but the stage's guard at draft 4:4221 has no case)."
127. T5:56–58. "as the box's last self-test recorded them". IMPRECISE. The last box self-test (G-CAL-n's, RESULTS.md:1470–1471) records only "the laptop's 570 plus the box's 11 more". The 14/3 split is G-VEC's record (RESULTS.md:1785–1786). Replace with: "644, the laptop's 633 plus the box's 11 checks more (its 14 HF checks in place of the laptop's three skip lines, as G-VEC's box self-test recorded them; G-CAL-n's, the last, recorded the same 11)."
128. T5:58–59. G-TIME-n's checks are model-free and count the same at either site. CONFIRMED. Draft 4:4477–5056 has no site-dependent branch, and its loops are fixed.

TOTALS: 128 items. 97 CONFIRMED, 7 IMPRECISE, 5 FAIL, 19 NOT CHECKABLE.

OBSERVATIONS
1. M8 can be fixed two ways.
   - Reword the five FAIL places as given above.
   - Or add a stage-level case. For example, patch globals()["same_filesystem"] to return False for one run_gtime call (as :4532–4548 patches gcal_gvec_inputs), and expect rc 2, no load, no report, and a REFUSED line containing "not on the stage root's filesystem". The counts would then become 634 on the laptop and 645 on the box, and T1:10–11, T2:9, T3:38 and :41, T4:36–37 and T5:47–58 would follow, after a new self-test run.
2. T3:95 says "the four self-test runs", but T5 records three (runs 1, 3 and 4) and says draft 2 never ran on its own. One of the two should change.
3. T3:80 says the sweep ran from 411b15c's window, but 2ca24e8's committed entry says "from deabf3f's commit window on" (RESULTS.md:81–82). If T3 is correcting that entry, it should say so.
4. The .gitignore to be committed (gitignore_v2, dee52f42…b272) is not the one reviewed (gitignore_v1, 1f2461bd…58b8). The reviewed one admitted all three cells (T4:274 and :281). No text names v2's sha256 or says that its block changed after the review. T5 names only the driver's hash.
5. T1:18 says "F, M, B and O numbers are the review's". T1 uses no M or box-risk B numbers, and "B" collides with T1's own B:line.
6. The precedent supplement cites the review it draws on by sha256 and opens with a "## 0. The short form". T1 quotes O2 and cites F8/F10 by the report's future path only. Adding 004f9c8e…0c915 (189 lines) would let the seat check the quotation at T1's commit.
7. The report's F2 says "six" guards, but its bullets name seven checks. T4:49 repeats "six".
8. schema.check_stage_identity raises SchemaError, a ValueError (schema.py:330), so a failure there exits 1, not 2. It should not be added to T3's exit-2 list.
9. schema.py:154–155 is the direct source for T1:47–48's list of what the report holds.

DEPARTURES
- The brief names drafts 1 and 2 for their sha256s and line counts only, but I also ran:
  - `grep -c 'chk('` over each of them;
  - `git diff --no-index --numstat` of HEAD's driver against draft 1, draft 1 against draft 2, and draft 2 against draft 3.
  They printed counts only. The rules do not bar them, but they go beyond the brief's stated use of those files.
- One `git grep -n -i` with the quoted pathspecs 'valence_core/n/*.py' 'valence_core/m/*.py', in place of item 3's pathspec with Q-F3's exclusion. No data path was in its scope.
- One `git diff --no-index -U3` of HEAD's driver against draft 4, run from S/step4b/gtime rather than the repository root, filtered by `grep -n '^@@'`.
- For classing, not barred by my reading:
  - `grep -o` over data/n/gcal/gcal.json (not under ckpt or reports; tracked and clean);
  - reads of RESULTS.md outside 2ca24e8's entry, of HEAD's driver outside the delta, and of valence_core/n/hftiny.py;
  - `wc -c` for the digest's byte counts and on S's .err files;
  - one name-only `ls valence_core/n/`;
  - one zsh "bad substitution" that stopped a loop before its `git rev-parse` ran;
  - two .gitignore reads whose output (not any argv) printed Q-F3's folder's plain name.
- No guard marker reached any argv. Q-F3's folder appeared only as data/m[f]3. Nothing under data/m[f]3, data/*/ckpt or data/*/reports was read, listed, sized or timed, and no whole-tree git status was run. In S, only the brief and the named files were read, with no listing, find or glob. No interpreter but shasum ran, and nothing was written.
```
