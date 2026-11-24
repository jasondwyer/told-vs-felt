# n — the N-pod campaign's BUILD: the blind values-check, as returned, with every disposition

PI date 2026-11-23. Code (the n-build session). LOCK-n.md is cited as LOCK-n v1.0 cites it (LOCK-n.md:54–57):
`L:N` is line N of v0.1's text, as `deabf3f` numbers it; a line of the file at `098218c` is `LOCK-n.md:N`.

**What was checked.** One blind pass by a subagent over the BUILD's drafted texts, at HEAD `098218c`:
- T1, the BUILD's entry, `82de4546…768a` (141 lines), its three placeholders not to be checked;
- T2, the review raw's head and dispositions, `05fa5d79…5ddd` (162 lines), with the report to be appended verbatim
  as its §2;
- T3, the self-test raw, `73536a88…2a10` (57 lines);
- T4, draft 2's campaign texts (`7249b88f…d9b5`): the module docstring's `campaign` paragraph and GT11's lines, and
  the campaign section's docstrings and comments;
- T5, the `.gitignore` draft (`fe865233…03ed`): the comment lines of its delta.

**The checker's brief** was a file the checker read itself, as its prompt directed: Code's scratch file
`S/step4b/camp/build/vc_brief.md` (`3a5756b2…be9a`, 152 lines). It:
- named the texts and the sources. In the repository: the files the texts cite, at `098218c`. In Code's scratch, by
  name and sha256: the two drafts (1 and 2) and HEAD's driver as copied, the two deltas, the review's brief and
  report, the run files of runs 1 and 2, the `.gitignore` draft and HEAD's, the seat block's draft, the readings as
  sent, the overlay script, the two overlays (their names, `diff -rq` and the drivers' hashes only) and Code's
  running list of its commands' kinds. In the sessions' notes folder: Code's two window requests. In this session's
  transcript: the window grants and closes;
- allowed `shasum`; `jq` on committed JSON and on this session's transcript; and `sed -n`, `/usr/bin/grep`, `cut`,
  `diff`, `cmp`, `od`, `wc -l`, `tr`, `sort`, `uniq` and `git diff --no-index` on the named scratch files. It barred
  any other interpreter (`awk` among them), any write, any network, any guard marker in an argv (a grep pattern and
  the command's own text included), and globs over the root, `results/raw/` or a folder of marker-named files;
- barred anything under `data/m[f]3`, any read, listing, size or time of a ckpt or reports file, anything in Code's
  scratch but the named files, and any look for G-TIME-n's two steered cells;
- asked for a sweep of Code's shell commands from the seat block's values-check's end (2026-11-24T00:55:07.441Z, T's
  UTC stamp) to the command that hashed the running list, each classed as the seat block's or the BUILD's, and the
  kinds after it to the brief's own hash;
- quoted the list of record v2's items 1–5 verbatim (equal by `diff` to the survey's and the seat check's briefs'),
  and required item 3's pathspec and the campaign folder's exclusion on every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (280 lines, sha256
`cc15f4b090a4d10f2db9ed1034a82d7c667129690d4a5a311b81d57ecd1610e7`). It names scratch files as S/..., the sessions'
notes folder as N and the transcript as T. Its times are T's UTC stamps.

**Totals:** 91 items: 75 CONFIRMED, 10 IMPRECISE, 0 FAIL, 6 NOT CHECKABLE; and 10 observations.

**One error of Code's, in the brief.** The brief said that LOCK-n.md's `L:line` is the file's line. LOCK-n v1.0
makes `L:N` line N of v0.1's text (LOCK-n.md:57), and the checker read the brief's form. Its items 8, 64 and 80
follow from that. Under the lock's own form, the driver's "L:543" is right: v0.1's line 543, G-VER's row, which is
LOCK-n.md:938 at `098218c`. The slip was the texts' "L:106", the file's line written in the lock's form.

**The checker's departures,** as its report states them, are in the BUILD entry's departures, for the seat to class.

## 1. Dispositions

Each text was edited as a v2 copy of the draft the checker read (S/step4b/camp/build/entry_v2.md,
review_head_v2.md and selftest_raw_v2.txt), by the file tools only, and each edit is replayed by tool in §2. The
driver's four corrections, in docstrings and a comment, are draft 3's, with its own self-test window. The focused
values-check of the later edits (results/raw/2026-11-23_n-campaign-starred-eight_valuescheck2.md) read these
dispositions too; its points on them are applied, as its raw gives them.

**The ten IMPRECISE items:**
- **Items 8, 64 and 80, "L:543" (T1:37, T2:145; the driver's docstrings, printed lines and check).** The citation
  stands under LOCK-n v1.0's own form (above); the brief misstated the form. Applied as the checker's other
  remedy:
  - the form is named once in each text: T1's new Citations bullet, T2's head, and one sentence in the driver's
    module docstring (draft 3);
  - "LOCK-n.md:938" stands beside "L:543" in T1 and T2;
  - the driver's self-tested strings are unchanged;
  - the texts' "L:106", the file's line in the lock's form, is now "LOCK-n.md:106" (T1's cap bullet, T2's F9).
- **Items 14 and 81, the PINs' header.** Applied in the checker's words: in T1, and in the driver's module docstring
  (draft 3), "but CP4's DRIVER line as built (the review's F6) and CP8's excerpt as the starred block carries it".
- **Item 24, F2 in T1.** Applied in the checker's words, "a session whose ids failed counted three times among
  G-VER's failed checks", with observation 10 for F1.
- **Item 47, F1's check in T2.** Applied in the checker's words: "a pause of another kind, and a rendering pause with
  no launch index (none for each of the last two)".
- **Item 48, F2's head in T2.** Applied in the checker's words: "over-counted (a session whose ids failed, three
  times)".
- **Item 52, the PI's stop at F4 in T2.** Applied in the checker's words, and in `run_campaign_pi_stop`'s docstring
  (observation 9).
- **Item 54, F6's quotation in T2.** Applied: "the BUILD's driver blob", with draft 3's header beside it.

**The ten observations:**
- **O1, two numberings.** Applied, as items 8, 64 and 80.
- **O2, other "LOCK-n v0.1" mentions.** Applied in T1: each names what ran or was set under v0.1, whose text v1.0
  keeps beneath its own. Code read each by `sed -n` first: the `gtime` and `gver` paragraphs' heads, the backend-ext
  printed line, `lock_fidelity_rule`'s docstring and one `gver` check name. The focused values-check found a ninth,
  which the checker and Code had both missed, `gtime_lock_inputs`'s docstring (v0.1's §3–§4, which v1.0 carries),
  now on the list too.
- **O3, the block's §2 on CP4.** Applied in the block: "the campaign's DRIVER line prints the BUILD's driver's
  sha256 (CP4 as sent said its STAGE line, the driver's blob)".
- **O4, `campaign --selftest`.** Applied in T1: "`--selftest`, which the driver takes before any command, runs the
  self-test."
- **O5, F5 in the "builds in" lists.** Applied: "F1–F5" in T1 and T2, and "F1-F5" in T3's run 2.
- **O6, the glob in `cd`'s argument.** Applied in T3: "no guard marker was in an exec'd process's argv (the glob
  expands in the builtin cd's argument alone)".
- **O7, whose check before each run.** Applied in T3: the coordinating session's grant before each run; Code's own
  check of the temporary folder before run 1, and of both before runs 2 and 3.
- **O8, `CampEnv.committed`.** Applied in draft 3: its comment names the ValueError outside the repository.
- **O9, the PI's stop's failed write.** Applied in draft 3: `run_campaign_pi_stop`'s docstring covers it.
- **O10, F1's reads.** Applied in T1: "on N4-T's told and N4-Ts's sham reads".

**The six NOT CHECKABLE items** (35, 36, 37, 45, 66, 77) are Code's plans. Item 77, the two raw names the driver's
docstring cites, is checked by tool at the seat block's commit, and the review raw's F11 line gives the result.

**The sweep.**
- Its uncovered kinds, (a) to (k), and its two wording slips are in Code's running list now.
- Its class counts set the departures' split: the seat block's 25 commands go to the block's entry, and the BUILD's
  138 to this BUILD's entry.
- Its count of guard markers and of the campaign folder's plain name in the span's commands is 0.

**Draft 3** (`fd643681…26d9`, +6 −3 from draft 2) carries items 14, 80 and 81 and observations 8 and 9. No check
reads them. It passed its self-test, 774/774, in its own window, its output run 2's bytes. Draft 4 (`47abe489…c21a`,
+4 −2 from draft 3), the BUILD's driver, carries the focused values-check's two points on the driver. It passed its
self-test, 774/774, in its own window, its output run 3's bytes.

## 2. The edits, replayed

The edits were made to new versioned copies of the three texts. Each was recovered from this session's transcript by
`jq` and replayed on the draft the checker read, each change's old text found exactly once, by the replay script
`S/step4b/camp/build/edits_check.sh`. The results are byte for byte the revised texts, so nothing else changed after
the check:
- the entry, 21 of 21 edits; the review raw's head, 16 of 16; the self-test raw, 12 of 12.

They are, in order of time: this check's dispositions; run 3's result; the focused values-check's dispositions, with
draft 4 and run 4's result; and the commit-time fills (the seat block's commit, F11's two names, the entry's
values-check paragraph and its departures). After the edits, one placeholder was filled by tool: the entry's count
of these edits.

## 3. The report as returned

```text
BLIND VALUES-CHECK — the N-pod campaign's BUILD texts (T1–T5). Read-only. The only interpreters run were shasum and jq.

Hashes checked first, all equal to the brief:
- T1–T5 (with line counts 141, 162, 57, 7,831 and 421).
- Draft 1 (7,570 lines) and HEAD's copied driver. That copy's blob 83716a92 is HEAD's and the working tree's.
- The two delta diffs, the review brief (125 lines) and the review report (180 lines).
- The run files: both .exit files read "exit 0"; both .err files are empty.
- The head copy of .gitignore (blob ef284ae9 is HEAD's), block_v2 (338 lines), cp_readings_v1 and the overlay script.
- departures.md (147 lines) and the untracked seat raw (e07fba2c…eba9).
- N/2026-11-23_n-build_camp-selftest-window-draft2.md (cbebd433…3fd2). N's first request note, which the brief gives no hash for, is b961d826…96e7; that is the hash the coordinating session's grant names.

HEAD is 098218c. LOCK-n.md is 59e0b1bc…00aa. `git diff --name-only HEAD` over valence_core, the driver, .gitignore and LOCK-n.md is empty.

ITEMS
1. T1:1–4. Step 14's BUILD; `campaign` on CP1–CP20 as PINs on the PI's "Build on the PINs"; the pin moved; cap 14,400,000 ms; the driver alone; not run. CONFIRMED.
   - n:159 is step 14.
   - T's cross-session message at 2026-11-24T00:38:11Z (2026-11-23 PI-local) reads: The PI's word on step 14's route: "Build on the PINs".
   - S/step4b/camp/draft2/n_sessions.py (drv2):3891 and :6161.
2. T1:5. valence_core/n/ stays at 06b55761…1d39 (L §18). CONFIRMED.
   - LOCK-n.md:1176.
   - valence_core/n was last changed at ef105f1.
   - Both overlay builds printed "package by shell 06b55761…1d39" (T, 01:25:17 and 02:23:23).
3. T1:6–8. One pin, 59e0b1bc…00aa, read by every stage's lock check; LOCK_VERSION "v1.0". CONFIRMED.
   - drv2:3891–3892.
   - The checks are at drv2:3986 and :5241; the campaign uses the second at :6603 and :6801.
4. T1:8–9. Two lock refusals, four printed lines, nine docstrings or comments, five check names, two asserted values. CONFIRMED.
   - S/step4b/camp/delta2_from_head.diff:111–301, each hunk counted.
   - Docstrings and comments: the module's gtime step 3; the pin comment; gtime_lock_inputs; gtime_identity; GtimeEnv; run_gtime; _gtime_selftest's docstring and its comment; gver_lock_check.
5. T1:9–10. The GT and GV readings' lines keep "LOCK-n v0.1". CONFIRMED (drv2:212, 265, 268). See observation 2.
6. T1:11–13. The cap is held to v1.0 §2's span "(L:106)" and passed as hour_cap_ms; a resume keeps it (runner:412–416); no cap field. CONFIRMED.
   - LOCK-n.md:106.
   - drv2:6162, :6759, :6966.
   - runner.py:413–414 (the cap) and :415–416 (alpha).
7. T1:14–35. The refusals and their order. CONFIRMED.
   - drv2:6563–6666, in the stated order.
   - LOCK-n.md:1165–1169 (weights), :699–708 (L §3), :801–812 (L §5), :1163 (tokenizers 0.22.2), :859–862 (7,680 reads and 7f7d7301…).
   - n_sessions.py:1032 for prior_state: "The runner's own checks of what is on disk".
   - INTEGRITY wording at drv2:6225 and :6244.
8. T1:37. "left to G-VER (L:543)". IMPRECISE.
   - At 098218c, LOCK-n.md:543 is a blank line. G-VER's row is LOCK-n.md:938, which is v0.1's own line 543 (deabf3f:LOCK-n.md:543).
   - T1:12's "L:106" uses the file's line, so the two citations use different numberings.
   - Instead: "…and left to G-VER (L:938, G-VER's row; v0.1's L:543)".
9. T1:37–40. The identity's fields; rendering_id is the manifest's pin (O4). CONFIRMED.
   - drv2:6279–6295, :6640–6642.
   - n_sessions.py:3944–3963.
10. T1:42–44. G-VER: the tokenizer from the weights folder, local files only; verify.verify; each step timed; the record checked by check_gver. CONFIRMED.
    - drv2:6698–6715.
    - n_sessions.py:5349–5351 (local_files_only=True) and :5278–5291 (gver_record calls check_gver).
11. T1:45–49. At the start, both files or neither; at a resume, nothing written and the record printed whole; at PASS, the load. CONFIRMED (drv2:6655, :6716–6761).
12. T1:51–57. Exits 0, 3 (or one line per F3), 5, 6 and 1 (B7); 2 is argparse's. CONFIRMED (drv2:6182, :6669–6673, :6694–6780).
13. T1:58–61. --resume/--ruling; --pi-stop exits 7, citing the committed raw's sha256; no smoke and no --out. CONFIRMED (drv2:6388–6433, :6783–6813, :7707–7723). See observation 4.
14. T1:62–63. "as sent in the spec raw's §1, but CP8's excerpt as the starred block carries it". IMPRECISE.
    - The docstring's CP4 (drv2:323–324, "DRIVER line printing this driver's sha256") is as built.
    - CP4 as sent reads "The campaign's STAGE line prints the BUILD's driver blob" (S/step4b/camp/spec/cp_readings_v1.md:64–65).
    - Instead: "…as sent in the spec raw's §1, but CP4's DRIVER line as built (the review's F6) and CP8's excerpt as the starred block carries it."
15. T1:63–64. The eight starred readings. CONFIRMED (cp_readings_v1 ★s; S/step4b/camp/seat/block_v2.md:1).
16. T1:65–69. The line counts:
    - draft 2: 7249b88f…d9b5, 7,831 lines, +1,640 −33 from 55885e65…385f;
    - draft 1: 9b51bb18…64c0, 7,570 lines, +1,377 −31;
    - the coordinating session's +1,376 −30 is "another form's";
    - draft 1 to draft 2: +377 −116.
    CONFIRMED.
    - shasum, wc -l and `git diff --no-index --numstat`.
    - T's grant of 01:37:39: "the delta is +1,376 −30 … a '^+[^+]' count skips them".
17. T1:70–73. .gitignore fe865233…03ed, +19 −3; G-TIME-n's comment corrected and two lines added; committed at the close (LOCK-n v1.0 §13). CONFIRMED.
    - numstat.
    - S/step4b/camp/build/gitignore_v1:335–339 and :343–344.
    - LOCK-n.md:381–388.
18. T1:74–76. The campaign block admits the root, N*.json, the report and G-VER's STOP record; arrays, temporaries and ._* files stay ignored. CONFIRMED.
    - gitignore_v1:363–367.
    - m/resume.py atomic_write_json writes "path.tmp".
    - schema.py:525–537 for the cell and array names.
19. T1:77–79. The dry-run adds in two throwaway repositories; exactly the intended files; HEAD's file admits only the shadow cell and time.json. CONFIRMED.
    - T at 01:36:38 and 01:36:45, outputs with digits masked.
    - With the draft: the three N*.json stand-ins, the shadow and two steered time cells, campaign.json, campaign_gver_stop.json and time.json. None of the .npy, ._*, x.json, .tmp or other.json stand-ins.
    - With HEAD's: the shadow cell and time.json only.
20. T1:81–83. 764/764 = 717 + 46 + 1; 774/774, 10 more. CONFIRMED.
    - od -c of both run files.
    - draft 1's _camp_selftest has 35 chk( sites, one in a loop of 12 argvs. drv2 has 43 sites and 14 argvs.
    - The environment check is at drv2:535.
    - results/raw/2026-11-22_n-gver-build_selftest.txt:82.
21. T1:84–86. Exit 0 and empty stderr; windows granted for each draft's bytes; run as background tasks; TMPDIR empty before and after; no n_sessions process; closed on the coordinating session's word. CONFIRMED.
    - T's grants at 01:37:39 and 02:31:03 name 9b51bb18…64c0 and 7249b88f…d9b5 and say "TMPDIR … empty, and no selftest_runN file".
    - Both runs had run_in_background.
    - The checks at 01:38:21 and 02:31:43 found TMPDIR with 0 entries and "no n_sessions process".
    - The closes at 01:40:12 and 02:33:58: "Battery window CLOSED on my word".
22. T1:87. 785 by arithmetic. CONFIRMED: 774 + (728 − 717), from results/raw/2026-11-22_n-gver-v2_selftest.txt:3.
23. T1:88–92. The review's counts: 2 BUG, 3 RISK, 6 NIT, 13 mutants, 9 box risks, 11 observations. CONFIRMED (S/step4b/camp/review_report.md).
24. T1:91. "G-VER's failed checks counted twice". IMPRECISE.
    - review_report.md:16: "one bad sequence gives rendering_mismatches = 3".
    - Instead: "F2, low, a session whose ids failed counted three times among G-VER's failed checks".
25. T1:93–94. Draft 2 builds in F1–F4, F8–F10, F11's docstring, B7, O4 and O6, with kills by reading. CONFIRMED (S/step4b/camp/delta2_from_draft1.diff). See observation 5.
26. T1:95–96. The block carries F1, F3, F4, O2, O4, O6 and B7, and O3/O5 as questions. CONFIRMED (block_v2:134–154, :168–177, :224–229, :313–315, :324–327).
27. T1:100–102. The twelve unstarred readings; the block's §2 names CP4's driver of record and CP15. CONFIRMED (block_v2:293–299).
28. T1:103–105. CP4's "the BUILD's driver blob"; the DRIVER line; the mF3ans:43 quotation. CONFIRMED (cp_readings_v1:64–66; drv2:6602; mF3ans:43).
29. T1:106–108. F7: the two lines come now, not "at step 14's close" (ans21b:32). CONFIRMED (ans21b:32).
30. T1:109–113. The runner is a seam; F5's resume case; _report and _pause; "Fresh". CONFIRMED.
    - drv2:6527, :7478–7490, :6380.
    - :7107 is the only runner._pause use; :6655 for "fresh".
31. T1:114–115. The PI's stop only while a pause stands; the schema allows more (Q4). CONFIRMED (drv2:6420; schema.py:208–213; block_v2:322).
32. T1:116–117. B3. CONFIRMED (runner.py:467–469 and :505–519; schema.py:208–212).
33. T1:118–119. O9. CONFIRMED.
    - jq: gtime.json's lock_sha256 and gver.json's pins.lock_sha256 are both 88d9fe7b…e9d5, each clean at HEAD.
    - drv2:4230 and :5337 compare against the pin. The campaign's path calls neither on those files.
34. T1:120–129. The cited sources. CONFIRMED (ans22b:22 and :24; ans23a:44; review_report.md:98–118).
35. T1:120–129 and T2:118–139. Carrying these into the launch files and the close's script. NOT CHECKABLE (plan).
36. T1:131–133. The gate's id list. NOT CHECKABLE.
37. T1:134–140. The commits, the kit's verify, the prefix count, not pushed. NOT CHECKABLE. The digest named is L §18's.
38. T2:5–8. What was reviewed, its hashes and line counts. CONFIRMED (shasum; S/step4b/camp/review_brief.md:10–21).
39. T2:10. 764/764 in a window. CONFIRMED (item 21).
40. T2:12–23. The brief was given as the prompt (aebb58a4…6004, 125 lines); its contents. CONFIRMED.
    - T: the review Agent call's prompt plus a newline hashes to aebb58a4…6004.
    - review_brief:33–34 gives the block as 033ecaf1…4a60, 320 lines, as T's hash of 01:39:06 shows.
    - Eleven declared bullets (:62–81); the asks (:83–96); the bars and items 1–5 (:100–125).
41. T2:25–28. Extracted by jq; 180 lines; be059ba1…e572; S-relative names only; the …2a60 slip. CONFIRMED.
    - T at 02:06:16: "handback blocks: 1", 180 lines, the sha256, local-root count 0.
    - review_report.md:3.
42. T2:30–37. "In sum" and the reviewer's departures. CONFIRMED (review_report.md).
43. T2:39–42. 10 checks more = 8 chk( calls + 2 argv cases. CONFIRMED (delta2_from_draft1.diff: added chk( lines at its lines 485, 620, 629, 654, 671, 699, 709 and 720; argv cases 12→14).
44. T2:44–46. The changes to the block's CP8, CP9 and CP12; Q3 and Q4. CONFIRMED (item 26). departures.md:122–123 names eleven edits after the values-check.
45. T2:46 "replayed by tool at its commit" and T2:98 "checked at the commit". NOT CHECKABLE (plan).
46. T2:50–56. F1's fix: the plan by launch index; told/sham line (runner:472–474); "as found now"; ids._problem. CONFIRMED (drv2:6481–6505, :6772; runner.py:472–474; ids.py:148–151).
47. T2:57–59. "…and two pauses that are not rendering pauses". IMPRECISE.
    - drv2:7064–7065 test a nonfinite pause and a rendering pause with no launch index.
    - Instead: "…a launch index past the plan, a pause of another kind, and a rendering pause with no launch index (none for each of the last two)."
48. T2:60. "G-VER's failed checks double-counted". IMPRECISE.
    - Instead: "G-VER's failed checks over-counted (a session whose ids failed, three times)".
49. T2:60–68. F2's terms; the cases of 1 and 7; fixtures at 159. CONFIRMED (drv2:6320–6330, :6997–7008, :7161; verify.py:94–105).
50. T2:69–71. F3. CONFIRMED (drv2:6770–6776, :7441–7445).
51. T2:72–76, F4's code and check. CONFIRMED (drv2:6333–6360, :6719–6727, :7446–7477).
52. T2:76. "The PI's stop (new=False) leaves the PAUSE report it would have replaced." IMPRECISE.
    - drv2:6356–6359 remove nothing when new is False.
    - After os.replace, a failed directory fsync or a failed read-back leaves the PI-STOP bytes.
    - Instead: "The PI's stop (new=False) removes nothing: the file stays as the failed write left it (the PAUSE report unless the replace had happened), for the seat."
53. T2:79–88. F5 (i)–(vi). CONFIRMED (drv2:7478–7490, :7495–7514, :7373–7377, :7515–7526, :7412–7440, :7552–7554).
54. T2:89. F6 quotes CP4's "the driver blob". IMPRECISE.
    - The words are "the BUILD's driver blob" (cp_readings_v1:65; review_report:47). grep finds "the driver blob" in neither.
    - Instead: "F6 (NIT), CP4's "the BUILD's driver blob"."
55. T2:89–93. The rest of F6, and F7. CONFIRMED (mF3ans:43; drv2:323–324; ans21b:32).
56. T2:94–97. F8, F9 (od -c of LOCK-n.md:106 and drv2:6162 both show 303 227 = C3 97) and F10. CONFIRMED (drv2:6445, :7026, :6879, :6875).
57. T2:98–100. F11's wording. CONFIRMED (drv2:223–227 against HEAD's 223–226).
58. T2:101–108. M1–M13 and their kills. CONFIRMED against review_report.md:68–80 and the cases named. "No mutant has been run" is Code's statement.
59. T2:109–113. B1 and B2. CONFIRMED (drv2:7213–7215, :7435, :7469; n_sessions.py:2762–2767, where relative_to raises before git runs).
60. T2:114–127. B3–B6. CONFIRMED (cells.py done_read_ids reads cell JSONs only; drv2:6579–6588).
61. T2:128–131. B7: four handlers plus a tokenizer/decode handler; the cases. CONFIRMED.
    - delta2_from_draft1.diff:278–375: draft 1's four `isinstance(e.code, str)` handlers.
    - drv2:6698–6707, :7348–7349, :7497–7503, :7555.
62. T2:132–139. B8's rule and anl:3172–3203; B9. CONFIRMED (drv2:6308–6317; scripts/n_analyze.py:3172–3203).
63. T2:140–148. O1–O5, including anl:6677–6679. CONFIRMED (block_v2:168–170, :313–315, :176–177, :324–327).
64. T2:145. O4's "(L:543)". IMPRECISE, as item 8. Instead: "(L:938)".
65. T2:149–158. O6–O11; the quotation "on the excerpt, in its own raw"; the raw put to the PI. CONFIRMED.
    - results/raw/2026-11-23_n-lock-v1_0-committed-close_design-to-code_answers.md:27.
    - T's closes: "held for the PI's routing of the seat's second sitting".
66. T2:152–153. Code's reading of O7's point. NOT CHECKABLE.
67. T3:1–7. Header; the driver's last change 2834c2d; +1640 −33; +19 −3. CONFIRMED (git log -1; numstat).
68. T3:8–11. The package digest by shell over both overlays; the self-test's own check. CONFIRMED (T's overlay outputs; drv2:4688–4690).
69. T3:13–16. Model-free; HF cases skipped; the schema as one line; the campaign's cases on doubles. CONFIRMED (drv2 cmd_selftest's schema chk; :7178–7216).
70. T3:17–21. Overlays of 098218c with LOCK-n.md and the manifest; exclusions; 175 files each; builder f8cdbccb… unchanged; differ only in the driver. CONFIRMED.
    - My pruned find counted 175 and 175.
    - `diff -rq` printed one line, the drivers. Their sha256s are 9b51bb18… and 7249b88f….
    - make_overlay_gver_v1.sh:13–16; results/raw/2026-11-22_n-gver-build_selftest.txt:21.
71. T3:22–25. The command. CONFIRMED (T at 01:37:53 and 02:31:17; the N notes). See observation 6.
72. T3:26–29. The windows; waited for exit notices (01:38:14, 02:31:38); state before and after. CONFIRMED (item 21). See observation 7.
73. T3:31–38. Run 1. CONFIRMED.
74. T3:40–51. Run 2 and the list of 8 single checks. CONFIRMED.
75. T3:53–57. The box: 728/728 with HEAD's driver, 717, 785. CONFIRMED. 55885e65… is in results/raw/2026-11-22_n-gver-v2_out.txt and _stage.txt.
76. T4 drv2:285–289. The n:159 quotation; CP4; the PI's word of 2026-11-23; the starred eight. CONFIRMED.
77. T4 drv2:289 and :315. The two raw names. NOT CHECKABLE until the seat block's commit (T2's @F11NAMES@). The spec raw's name matches block_v2:22.
78. T4 drv2:290–313. Steps 1–5 and the exits. CONFIRMED (drv2:6551–6813), apart from item 80.
79. T4 drv2:317–346. CP1–CP20 in short. CONFIRMED against cp_readings_v1, apart from item 81.
80. T4, every "L:543": drv2:295, :301, :6555, the printed strings :6609 and :6741, and the check :7532/:7537. IMPRECISE.
    - Under the brief's and the seat's numbering (the file's line at 098218c), line 543 is blank; the row is L:938.
    - Instead, "(L:938)" in the docstrings. Or keep the self-tested strings and add one line to the module docstring: "L:543 is LOCK-n v0.1's own line 543 (LOCK-n v1.0 §0's L:N), LOCK-n.md:938 at 098218c."
81. T4 drv2:315–316. "but CP8's excerpt as the starred block carries it". IMPRECISE, as item 14.
    - Instead: "(as sent in results/raw/2026-11-23_n-campaign_spec.md §1, but CP4's DRIVER line as built, the review's F6, and CP8's excerpt as the starred block carries it)".
82. T4 GT11, drv2:223–227. CONFIRMED (ans21b:29–32; LOCK-n.md:381–388; n:148 "No looks (§2.5)."; results/raw/2026-11-21_n-gtime-build_review.md:286 for O2).
83. T4 drv2:6153–6182, the comments: v1.0 §2; runner.py:412–416; L §3 holes 3–4; L §5's forms; CP12. CONFIRMED (LOCK-n.md:104–108, :699–708, :801–812).
84. T4 drv2:6185–6305, docstrings, including the ans20b:32 quotation and "L §21's keys". CONFIRMED.
    - schema.py:302–312, :322; gvec.py:114, :386–389; LOCK-n.md:1260.
    - results/raw/2026-11-20_n-lock-v0_1-read_design-to-code_answers.md:32; runner.py:17–22, :140–166.
85. T4 drv2:6308–6385, citing verify.py:94–105, schema.py:1533–1537, runner.py:363 and schema.py:1195–1199. CONFIRMED: each line says it ("continue"; the G-VER-STOP rule; "stop": None; STOP_FIELDS). runner.py:552 uses atomic_write_json.
86. T4 drv2:6388–6505, citing schema.py:208–210 (the quotation), :1197, n:130, ids.py:688 and runner.py:470–479. CONFIRMED.
87. T4 drv2:6508–6548, CampEnv's comments. CONFIRMED. See observation 8.
88. T4 drv2:6551–6813, docstrings. CONFIRMED apart from item 80. See observation 9.
89. T4 drv2:6822–7661, the self-test's docstring, comments and cited figures. CONFIRMED.
    - The figures: 59e0b1bc…00aa; 5,120; C 0.25; 33..63; 'space'; 4,096; 7,680; 3,637; 138 cells (120×40 + 18×160); 4,416 names; verify.py:94–105.
    - Sources: LOCK-n.md and n_sessions.py:625 and :3848; the run passed.
90. T5, gitignore_v1:335–339 (the G-TIME-n comment). CONFIRMED.
    - ans21b:29–32, the second sitting of 2026-11-21 per LOCK-n.md:60.
    - LOCK-n.md:381–388 names the two cells of lines 343–344.
91. T5, gitignore_v1:357–362 (the campaign comment). CONFIRMED.
    - n:159 and ledger 27.
    - The 138 cells (item 89); names start with the arm (schema.py:282, :525–529).
    - 31 layers (LOCK-n.md:869).
    - ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md:54: "copied to the laptop with its hashes … never committed to git".

TOTALS: CONFIRMED 75, IMPRECISE 10, FAIL 0, NOT CHECKABLE 6.

OBSERVATIONS
1. The texts mix two line numberings for LOCK-n.md.
   - L:106 (T1:12, T2:95) is the file's line.
   - L:543 is v0.1's own line, LOCK-n v1.0 §0's L:N.
   - cp_readings_v1:10–11 uses LOCK:N for the file and L:k for v0.1's line. Under that form, L:106 would be LOCK:106.
   - The seat's newest raw (§0) and this brief read L:N as the file's line.
   - Name the form once in T1, T2 and the module docstring.
2. Besides the GT and GV readings, draft 2 keeps "LOCK-n v0.1" in the gtime and gver paragraph heads (drv2:182 and :240, "on the box, under LOCK-n v0.1"), lock_fidelity_rule's docstring (:3930), a backend-ext printed line (:1094) and a gver check name (:5649). T1:9–10 could name them as history too.
3. block_v2:296–297 (§2) still says "the campaign's STAGE line prints the BUILD's driver". The build prints it on the DRIVER line (F6), but only the entry declares F6.
4. T1:61 "every other option is refused": `campaign --selftest` is not refused. --selftest is dispatched before any command (drv2:7699–7700).
5. F5's disposition is "Applied" (T2:79), but the "builds in" lists (T1:93, T2:40) do not name it. Consider "F1–F5".
6. T3:22–23 "no guard marker was in any argv": `cd jl*/.venv/bin` expands a glob to a marker-named folder as the argument of the builtin `cd`. No exec'd process takes it, but this brief's own rule counts such a glob as a breach. Consider "in any exec'd process's argv".
7. For run 1, Code's commands checked only that TMPDIR was empty (01:25:17, 12 minutes before the run). The absence of run-1 files was checked by the coordinating session's grant. For run 2, Code checked too (02:24:02). T3 could say whose check.
8. CampEnv `committed` (drv2:6514) says "or None". committed_bytes raises ValueError for a path outside the repository; both callers catch it (drv2:6404, :6584).
9. run_campaign_pi_stop's docstring (drv2:6785–6786) says "1 on a refusal, with nothing written". A write failure after the replace exits 1 with the PI-STOP bytes on disk (item 52).
10. T1:91 "on N4's told reads": F1 covers N4-T's told reads and N4-Ts's sham reads.

THE SWEEP (T; assistant Bash tool_use items after 00:55:07.441Z through 02:37:54.319Z, the loop that hashed departures.md 55faff31…05c5, 147 lines): 163 commands.

Not covered by the list, by time and kind:
- (a) The list's own upkeep, 10 commands:
  - `cat >>` heredoc appends to S/step4b/camp/departures.md at 01:26:49, 01:37:05, 01:41:43, 02:24:15, 02:28:30, 02:30:51, 02:31:57 (with wc -l of the list and a width count), 02:33:47 and 02:37:47;
  - its read by wc -l and sed -n at 02:24:07.
- (b) Draft 1's drafting reads, which the "driver's draft" bullet does not name; the same kinds are named only for the spec head's and the block's checks:
  - 00:56:14–01:02:59 (23 commands), 01:08:08, 01:11:20, 01:17:29, 01:17:34, 01:24:05, 01:25:02 and 01:25:05;
  - sed -n and /usr/bin/grep (-n, -o, -c, -A, -B, into cut, head, sort and uniq) over schema, runner, keys, ids, gvec, cells, testing, guard, sessions, gcal and m/resume.py;
  - two greps over the glob valence_core/n/*.py (00:57:37, 01:17:34);
  - greps over HEAD's driver, one a for-loop over twelve function names (00:59:52);
  - reads of LOCK-n.md lines, and of two fidsample raws with a quoted-glob git ls-files;
  - jq over data/n/gvec/gvec.json for its keys, site and a count (01:08:08).
- (c) Draft 1's checks:
  - 01:10:06 `git show HEAD:scripts/n_sessions.py` into grep -c;
  - 01:21:15 a trailing-blank grep;
  - 01:22:07 a bracketed marker count over the draft;
  - 01:22:55 grep -c of the status line, and a loop of grep -c -F per sha16 over LOCK-n.md;
  - 01:24:17 the chk and argv counts by sed -n|grep -c, and git show HEAD:… into grep -c;
  - 01:24:22 a grep over RESULTS.md.
- (d) Draft 1's overlay and request:
  - 01:24:33 cat of make_overlay_gver_v1.sh;
  - 01:24:42 cat of G-VER's draft-4 window note in N;
  - 01:25:17 wc -l and grep -c of the delta's +/− lines;
  - 01:26:01 a grep of the delta's removed lines.
- (e) 01:34:57 (seat): a grep -c for local roots and ids over the readings' addendum draft.
- (f) 01:35:39 and 01:35:42: grep -n -E/-F and sed -n over the working tree's .gitignore, and its wc -l.
- (g) 02:06:16: jq over the review subagent's own transcript into S/step4b/camp/review_report.md, with a hand-back count, wc -l and shasum; a grep -c for local roots and ids over the report; sed -n of valence_core/n/verify.py 90–126. The list names only "read by the file tool".
- (h) 02:21:19: awk printing draft 2 from line 6149 into a non-ASCII grep.
- (i) 02:23:32: the two full `git diff --no-index` outputs into scratch (the delta2 files).
- (j) 02:32:29: cat of run 2's output. The list names run 1's.
- (k) 02:37:54: wc -l beside shasum in the 22-file loop. departures_pending.md names it later.

Wording slips in the list:
- "two ranges read" of RESULTS.md at 2834c2d: three sed -n ranges were read (02:34:19, :24, :28).
- "three time ranges": the jq at 02:36:47 selected by pattern, not by time.

By class:
- Seat block's: 25 (00:55:54; 01:27:02–01:35:28, 17; 02:25:51–02:28:10, 7).
- BUILD's: 138, including the 10 upkeep commands.

Guard markers in the commands' text: [m]lx 0, [j]lens 0, [q]wen 0, [o]lmo 0, [i]pykernel 0. The campaign folder's plain name ([m]f3, any case): 0. Also 0 in the two later commands.

After the hash, up to the brief's own hash: one command, at 02:38:59. Its kinds:
- cat of S/step4b/camp/build/vc_brief_head.md written into S/step4b/camp/build/vc_brief.md (cat >);
- sed -n of the seat's brief appended (>>);
- two diffs over process substitutions (sed -n, tail -n), with echo;
- wc -l;
- a bracketed marker count (2);
- shasum | cut, giving 3a5756b2…be9a.
Beyond that: the Agent call at 02:39:13, and at 02:39:21 printf >> into gate_v16_new_ids.txt, wc -l, cat > departures_pending.md and cat | wc -l.

DEPARTURES
- cat -n, head, tail -n and echo, which are not among the brief's named tools, were used only as filters on piped output. No file was read with them.
- One `git show deabf3f:LOCK-n.md | sed -n`: a read of LOCK-n.md at v0.1's commit, to check its numbering.
- From T, beyond the window grants and closes:
  - the tool_result outputs of eleven of Code's commands: overlay builds, the pre- and post-run checks, the dry-run adds with digits masked, the review hand-back and brief-preparation hashes, and the two hash commands;
  - the review Agent call's prompt, hashed only;
  - three jq searches of user records for the PI's relay, the window messages and the seat raw's routing.
  Each printed only lines a finding uses.
- Otherwise none:
  - no other interpreter, write or network;
  - no marker in any argv, with bracketed patterns only;
  - nothing under data/m[f]3, ckpt or reports read or listed;
  - in S, only the named files, this brief, and the overlays by pruned find (names filtered by grep), diff -rq and shasum.
```
