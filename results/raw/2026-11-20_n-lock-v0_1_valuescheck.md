# n: LOCK-n v0.1's placement — one blind values-check of draft 8, the read raw and the entry (Code's)

*Code, PI date 2026-11-20. One blind values-check, by a subagent Code launched on a brief in its scratch
(`vc_brief.md`, sha256 `1da437ec7b2e487cf49ca3466417c12a45f9374409c818050d9698e067e4c0d1`, 102 lines), of three texts
at HEAD `1641948`: LOCK-n v0.1's draft 8 (`4d16aee3…a925`, 994 lines; its T1), the code-to-design read raw as drafted
(`1e2cb326…375d`, 107 lines; T2) and this commit's entry as drafted (`380525ab…cfde`, 114 lines; T3). Its report
follows whole, as it handed it back, with one scrub: on its item 25's line, a scratch root's folder name that it
quoted as a search string. Its totals: 66 items, 48 CONFIRMED, 10 IMPRECISE, 3 FAIL, 5 NOT CHECKABLE; 8 observations.
The entry gives each finding's disposition. Draft 9 (`5acca00f…586a`, 1010 lines), placed as LOCK-n.md, is draft 8
with the findings on the lock applied; the committed read raw and entry carry theirs.*

---

VALUES-CHECK — LOCK-n v0.1 draft 8 (T1), the code-to-design read raw (T2), the entry (T3)

I verified the brief first: S/step4b/lock/commit/vc_brief.md has sha256 1da437ec…c0d1 and 102 lines. HEAD is 1641948 (unmoved). T1, its template, T2 and T3 match the brief's sha256s and line counts (994, 994, 107, 114). Every repository source I used is tracked and clean at HEAD; I checked each with `git rev-parse HEAD:<path>` against `git hash-object`.

ITEMS

A. T3 and T2

1. T3:1–3, :6–8; T2:4–6. Claim: LOCK-n.md is draft 8, sha256 4d16aee3…a925, 994 lines, placed on the PI's routing of 2026-11-20 (first sitting), item 3. CONFIRMED. Evidence: shasum and `wc -l` on S/step4b/lock/LOCK-n-v0_1-draft8.md; results/raw/2026-11-20_first-sitting_pi-routing.md:15 is item 3.

2. T3:2–3. Claim: holes 1–17 are filled, 18 is v1.0's, and there is one question (the closure). CONFIRMED. Evidence: draft 8 has no `- **HOLE**` bullet; the word appears only in the opening note at :7. T1 §16 carries hole 18. T2 §4 asks only Q1.

3. T3:4–5, :112–113. Claim: LOCK-n.md is not committed; n v0.2 §8 step 10 commits it. CONFIRMED. Evidence: PROPOSAL-n-bk-reconciliation-v0_2.md:159 reads "10. Commit LOCK-n v0.1"; `git log -- LOCK-n.md` is empty; `[ -e LOCK-n.md ]` is false.

4. T3:5. Claim: model-free; nothing ran on a model or on the box. CONFIRMED as far as the sweeps can show. Evidence: python appears only in the two model-free windows (S/step4b/lock/commit/sweep/cmds_all.jsonl:24 and :93). No pod or ssh command appears. MCP calls are outside the sweeps.

5. T3:8–10; T2:13–15. Claim: the rt20:15 quotation. CONFIRMED. Evidence: verbatim with the routing raw's line 15 (committed at bc85386).

6. T3:12–16. Claim: the read raw is 1e2cb326…375d with the stated contents; the seat reads against ans20, ADDENDUM-n3 and n:117 in one sitting (§5.2). CONFIRMED. Evidence: shasum of T2; results/raw/2026-11-20_n-gvec-gcal-reads_design-to-code_answers.md:56 is §5.2.

7. T3:17–28. Claim: holes 1–18 with their sources. CONFIRMED.
   - The hole list is results/raw/2026-11-19_n-lock-v0_1-opens_code-to-design_STOP.md:17–37 (§1, at d85fc34).
   - Hole 10 is plan_sha_run1.txt line 3.
   - Hole 11: 7680/160 = 48, remainder 0. Exact shell limb arithmetic gives 1 − 0.99^48 = 0.38270985905771181466…, which rounds to the stated value.
   - Hole 12: scripts/n_analyze.py sha256 is 735da934…a7a8.
   - Hole 13: data/n/gates/G-ANL-n.json is e775cbb4…6088, committed at 1641948. By sed/grep: "verdict" PASS (:461); analyzer sha256 735da934…a7a8 (:14–17); d_eq and d_20 (:343–344); all seven points have `"merged": []`; reach PASS has shape a, 28 triples, 225 tuples; reach FAIL has shape b, 25 and 201; `agrees_with_hand` is true for both.
   - Hole 14: the shell digest is 06b55761…1d39 at ef105f1, at b6ea27f, at 1641948 and in the worktree.
   - Hole 15 is rt19b:23; hole 16 is ans20:30 (§2.4); hole 17 is A-n3:64; hole 18 is ans19b:43.

8. T3:30–31; T2:51–53. Claim: ans20 §5.1 lists holes 10 and 17 as still open; drafts 4b and 5 had already filled them; the quotation. CONFIRMED. Evidence: ans20:54. Draft 4:347 still has the read_plan_sha256 HOLE, which is gone in 4b. Draft 4b:719 still has the standing-lines HOLE, which is gone in draft 5.

9. T2:52. Claim: "The drafts filled both before that raw was written". NOT CHECKABLE. No source dates when the raw was written. The sweep shows only that drafts 4b (cmds_all:26–27) and 5 (:56–65) came before Code's first read of the raw (:67). Suggested wording: "The drafts had filled both before that raw reached Code".

10. T3:32–33. Claim: the coordinating session's words, "drafted in scratch in parallel with n-analyzer's v7, on the coordinating session's word of 2026-11-20". NOT CHECKABLE. No listed source holds those words. They are verbatim T1's own Draft 4 note (T1:19–20).

11. T3:33–35. Claim: draft 5 carried "…§1.2's two R's, §5.2's interval distribution". IMPRECISE. A-n3:79's step (5) names "§5.2's declaration". Draft 5 carried the declaration; the distribution stayed a HOLE (draft 5:747; T1:40–41) until draft 6b. Replace the parenthesis with: "(draft 5: §6's texts as the second sitting ruled them, §1.2's two R's, §5.2's declaration with §5.3's departure, the distribution left a HOLE for a battery window)".

12. T3:35–36. Claim: §8.3 lists (4) before (5). CONFIRMED. Evidence: A-n3:79.

13. T3:36–37. Claim: "Code asked first (one question) and did none of it before the answer." NOT CHECKABLE. No source states it.

14. T3:38. Claim: "draft 6, on item 3, the five things the answers of 2026-11-20 name for the lock". IMPRECISE. T1's Draft 6 note (T1:46–49) lists seven changes. ans20 names for the lock the cosines (:16), the gate line (:28, already placed at draft 4), cap 48 of 48 per batch (:34), E (:42) and the power note (:43). "Five" matches neither list. Replace with: "draft 6, on item 3, from the answers of 2026-11-20: hole 16, the power sentence with E's acceptance, the six cosines, each batch's coherence count and stops, N2's decision point in the seat's words, and holes 12, 14 and 17 as §5.1 names them".

15. T3:39, :43. Claim: draft 6b added §21's distribution; draft 8, at 1641948, filled hole 13. CONFIRMED. Evidence: the HOLE at draft 6:792 is gone in 6b; the HOLE at draft 7:474 is gone in 8.

16. T3:40–42. Claim: draft 7's contents, including "the arrival's form (§1.4)". CONFIRMED. Evidence: the normalized 6b→7 diff has hunks in §9, §10, §13, §15, §18, §21 and §23; ans19b:71.

17. T3:40–41. Claim: the quotation "no Python, nothing at root". NOT CHECKABLE. It appears only in Code's scratch notes (cmds_all:160).

18. T3:45–46. Claim: the seven draft sha256s. CONFIRMED. Evidence: shasum of each draft file.

19. T3:46–47. Claim: nothing was committed before v7 landed. CONFIRMED. Evidence: no `git commit` appears in the 193 swept commands (the only match is the sweep's own pattern at :193); LOCK-n.md has no history.

20. T3:47–49; T2:25–29. Claim: placement waited because verdicts_precheck resolves (stats) the lock path; G-ANL-n's run found no LOCK-n.md (R:48–49); Code has placed none. CONFIRMED.
   - scripts/n_analyze.py:6625–6640 applies `Path(x).expanduser().resolve()` to the lock path.
   - The analyzer's battery calls it on `REPO / "LOCK-n.md"` at :5826–5830.
   - RESULTS.md:47–49 records the check.
   - No swept command writes into the repository.
   - The order itself, as "the coordinating session's", is NOT CHECKABLE beyond R:44–46 (v7 verified).

21. T3:50–56; T2:61–64. Claim: the anchor counts and the nine hand re-citations. CONFIRMED, except for item 60.
   - Draft 6b holds 506 prefix anchors, 2 back-ticked anchors and the bare ":310": 509 in all.
   - 173 point into the seven cited files: 83 + 43 + 16 + 9 + 4 + 9 + 9.
   - 19 occurrences keep their numbers, and each of those blocks is byte-equal at 516b60f and 1641948.
   - Nine cited blocks differ between 516b60f and b6ea27f: gcal.py 50–61, 54–58, 59–61 and 134–136; runner.py 30–32, 33–48, 33–42 and 38–39; schema.py 489–492. These match T2's list of what was re-cited by hand.
   - Second hop: b6ea27f..1641948 (with the pathspec) changed only .gitignore and RESULTS.md and added three files. The change is one 177-line insertion at RESULTS.md:24. All 94 R anchors of draft 7 appear at +177 in draft 8, checked pair by pair.

22. T3:58. Claim: "The re-pinned drafts differ from their parents only in anchor numbers". IMPRECISE. With anchors normalized by `sed -E`, draft 6b→7 still differs in 155 lines and draft 7.pre→8.pre in 27. All of those lie in the rewritten sections:
   - 6b→7: the header, §1's MANIFEST bullet, §6, §9, §10, §13, §15, §18, §21, §23, §24 and Sources.
   - 7.pre→8.pre: the header, §9, §24 and Sources.
   The intermediate re-pinned files are not among the sources. Replace with: "Outside the sections each pass rewrote, draft 7 differs from draft 6b, and draft 8's template from draft 7's, only in anchor numbers (compared with every anchor normalized)."

23. T3:59. Claim: 550 anchors; 69 witness rows. CONFIRMED. Evidence: 546 prefix + 3 back-ticked + ":310" = 550. All 69 phrases in S/step4b/lock/repin/witness8.txt are found in their cited lines at 1641948.

24. T3:60–70; T2:96–101. Claim: the two windows and their riders. CONFIRMED.
   - Script hashes: plan_sha.py f8c840ef…6a4c; interval.py 6d143dc0…a766.
   - Both exit files read "exit 0".
   - plan_sha_run1.txt equals plan-sha_out.txt (cc1dd781…8e26, 3 lines, "reads 7680, distinct 7680").
   - interval_run1.txt equals interval_expected.txt and interval_out.txt (ad82c1b7…7660, 178 lines); the diff file is empty.
   - Rider hashes: 1a897671…f62c and 170300f4…5487.
   - Each window ran once under `nice -n 19` (cmds_all:24 and :93), after its shell derivation (:13 and :45).

25. T3:72–73. Claim: the re-runs reproduce their outputs; the riders show <repo>, <scratch> and <venv>. CONFIRMED. Evidence: rerun_plan/plan_shell.txt equals plan_shell.txt (1d1dc4a1…eee1); rerun_interval/interval_expected.txt equals ad82c1b7…7660. None of the seven files to be committed contains "/Users/", "/private/" or "<a scratch root's folder name>".

26. T3:74–80. Claim: the check raw and the four checks. CONFIRMED. Evidence: check raw 0ee8c2c0…86c3. Check8: exit 0 (raw :33); check8_out.txt has 72 "ok" lines. Check7: exit 0 (:113). Check6: one FAIL, the HOLE count (:194, :215). Check5: exit 0 (:220).

27. T3:84–88. Claim: two guard-marker breaches while drafting draft 6; no Python then. CONFIRMED. Evidence:
   - cmds_all:69 is `ls -1 LOCK-* …`; LOCK-* at the root includes p's three marker-named lock files (`git ls-files` filtered).
   - :73 is a loop that names one of those files to `git log` and `sed`.
   - Both fall between draft 5 (:56–65) and draft 6 (:84–).
   - No python in :66–:83.
   - "Disclosed then" is NOT CHECKABLE.

28. T3:89–91. Claim: "eight jq reads of Code's own transcript … three sweeping … A ninth failed". IMPRECISE. The sweeps hold seven successful reads:
   - recovering: :151, :152, :153, :155;
   - finding: :177;
   - sweeping: :190, :193;
   - plus the failed one at :154.
   A third sweep made after :193 would not be in the files. Replace with: "seven jq reads of Code's own transcript in the swept commands (four recovering the commands the riders quote verbatim, one finding the interval cross-check's invocation, two sweeping Code's commands for this list), and the last sweep's; an eighth failed before reading: …". Or say "eight" and state that the last sweep is counted.

29. T3:93–94. Claim: the jq reads over the records. IMPRECISE: the list is incomplete. The sweeps also show:
   - jq over data/n/gcal/dose_map.json (:7);
   - jq over the first record of data/n/ids/sessions.jsonl and of one BK skeleton file (:42);
   - the interval cross-check's first run (:45), whose jq reads MANIFEST.json, sessions.jsonl and the 14 skeleton files.
   Replace with: "jq over data/n/gvec/gvec.json, data/n/gvec/gvec_cosines.json, results/raw/2026-11-19_n-gvec-v1_gvec.json, data/n/gcal/gcal.json, data/n/gcal/dose_map.json and data/n/gates/G-ANL-n.json (the last one's byte count by `wc -c`), and over the first record of data/n/ids/sessions.jsonl and of one BK skeleton file". In the re-runs bullet, write "the two shell cross-checks, run and re-run".

30. T3:95–96. Claim: "schema.py also at 516b60f through git show". IMPRECISE. cmds_all:118 copied all seven cited files at both 516b60f and b6ea27f into scratch with `git show`, read there at :119–:138. :164 piped RESULTS.md at 1641948 through `git show`. Replace with: "…; the seven cited files at 516b60f and b6ea27f, and RESULTS.md at 1641948, through `git show`".

31. T3:97–98. Claim: git reads "with item 3's pathspec wherever a command traverses the tree". FAIL. cmds_all:70 ran `git show --stat --format=%h d85fc34 | head -20`: a whole-commit `--stat` (a form item 1 does not list) with no pathspec. Also, `git grep` and `git ls-files` (:9) are not named in the list, and `ls-tree` and `cat-file` appear in no swept command (they could only be inside scripts). Replace with: "`git show`, `diff`, `log`, `grep`, `ls-files`, `hash-object` and `rev-parse` over committed files, with item 3's pathspec wherever a command traverses the tree but one: `git show --stat --format=%h d85fc34`, a whole-commit `--stat` with no pathspec".

32. T3:99–103. Claim: the heads read, the `ls | grep -c`, the closure hashing and the re-runs. CONFIRMED. Evidence: cmds_all :77, :78, :50, :182, :90, :115, :174, :178.

33. T3:104. Claim: "`ls` of scratch folders". IMPRECISE. The listings include `ls -la` (:43) and `ls -A` (:25, :94); ef105f1's entry called this class "scratch metadata". Replace with: "`ls`, `ls -p`, `ls -A` and `ls -la` of scratch folders (scratch metadata); memory writes; the shared notes."

34. T3:82–83, with the list as a whole. Claim: "Code's sweeps …, @SWEEPS@, found no others". FAIL. The sweeps show four classes the list does not name:
   - (a) awk, run directly in 33 commands: the memory edit (:2), the plan cross-check (:13), the anchor tools (:117–:140, :158), and line-numbered reads of RESULTS.md (:164) and the routing raw (:182). It also runs inside the check scripts. T3:50 says "Code's awk tools", and ef105f1's entry stated awk plainly.
   - (b) `bc -l` (:14), which T1:633 and T2's table cite.
   - (c) a `cd` through a glob into BK's marker-named skeleton folder, then `ls` and jq there (:42). This is the class ans20:62 ruled inert at db00d6d. The windows' `cd jl*/.venv/bin` (:24, :93) has the same form, though the riders disclose it.
   - (d) the kit's verify of ef105f1 (:1).
   Add: "awk (Code's anchor and check tools, the plan cross-check, one memory edit, line-numbered reads of RESULTS.md and the routing raw); one `bc -l` for 1 − 0.99^48; one `cd` through a glob into BK's skeleton folder, with `ls` and a jq read there, and the windows' `cd` through a glob as their riders state; the kit's verify of ef105f1".

35. T3:107–109. Claim: the files committed by path. CONFIRMED. Evidence: the six named files exist in S/step4b/lock/commit/; `_valuescheck.md` is to come.

36. T3:111–112. Claim: the home-folder count at commit time is 0. NOT CHECKABLE (it describes the future commit). The files to be committed hold no "/Users/" today.

37. T2:3–9. Claim: the header's routing, hash, line count and rt20's commit. CONFIRMED. "The placement's form, agreed with the coordinating session" is NOT CHECKABLE.

38. T2:17–20. Claim: the ans20:56 quotation. CONFIRMED, verbatim.

39. T2:21–22. Claim: "the name the analyzer binds in VERDICTS (n_analyze.py:4901, n_analyze.py:5534)". IMPRECISE. Both cited lines are battery expectations. VERDICTS itself binds `Path(lock).name` of its `--lock` argument (scripts/n_analyze.py:6699). Replace with: "the name the analyzer's battery expects VERDICTS to bind (n_analyze.py:4901, n_analyze.py:5534; VERDICTS binds its `--lock` file's name, n_analyze.py:6699), at 1641948".

40. T2:33–49. Claim: the holes table. CONFIRMED. Evidence:
   - The "what" column matches the STOP raw :20–37.
   - The "filled at" column matches the HOLE bullets per draft: 4b fills 10; 5 fills 15 and 17; 6 fills 16; 7 fills 12 and 14; 8 fills 13.
   - "Draft 3" for holes 1–7 rests only on T1:11–17; draft 3 is not a source, but draft 4 already has them filled.

41. T2:58–77. Claim: §3's list of what the last pass changed. CONFIRMED. Evidence: A-n3:79; ans19b:58, :59, :71; A-n3:26, :28, :30, :48; ans20:44–45; the 6b→7 diff (the v6 line is dropped from §9).

42. T2:81–91. Claim: Q1's facts. CONFIRMED.
   - Over 516b60f's blobs, the shell digest is 1bb0daea…af51, equal to idsv:195.
   - At 616e940, bc50244 and ef105f1 it is d3415b10…a519, e40c9871…9523 and 06b55761…1d39.
   - Nothing under valence_core/ outside n/ changed since 516b60f.
   - The only import changes are `directions` (in gcal.py) and `import shutil` (in runner.py).
   - The twelve closure files hash, by the brief's cd-and-glob loop, to idsv:196–207's values; their blob ids are equal at 516b60f, at 1641948 and in the worktree.

B. T1, the parts this pass wrote

43. T1:57–65, the Draft 7 note. CONFIRMED, except that "Every anchor is re-pinned" misses ":310" (item 60). Evidence: R:44–46; draft 6b's hash.

44. T1:67–72, the Draft 8 note. CONFIRMED.

45. T1:154–160, §1's MANIFEST bullet. CONFIRMED. Evidence: the file is clean, sha256 53a8cd74…99d8; ids.py:78–86; R:1602–1606; MANIFEST read with `tr`: schema, pi_dates and base_manifest_sha256s all match.

46. T1:424–430, §6's read_plan_sha256 bullet. CONFIRMED.

47. T1:448–450, §7's p0 bullet. CONFIRMED. Evidence: A-n2:18; ans19:42; schema.py:494–498; R:15409.

48. T1:472–488, §9 whole. CONFIRMED. Evidence: R:24–35, :208–216, :288–292; n_analyze.py:70–77 and :3049–3050; schema.py's sha256 is 1cab28df…edff (ef105f1's); ans16g:59; the artifact's fields.

49. T1:502–505 and :518–523, §10's four rows and the G-CAL-n inputs bullet. CONFIRMED. Evidence: gcal.py:43–46, 56–70, 145, 169–178; A-n3:26–30, :48, :64; ans19:24–38; ans19b:58–59; R:1690–1696, :1976–1977; rt19:15; rt19b:23.

50. T1:619–623, §13's alpha bullet. CONFIRMED. Evidence: ans18d:39; schema.py:500–501; runner.py:46–47.

51. T1:624–631, §13's "The runner as built". IMPRECISE in one quotation: ans19:51 reads "A runner change, …". The rest is CONFIRMED (R:616–626; ans20:41; runner.py:35–45, with the quote at :40–41; runner.py:51–54; R:2852–2855). Replace with: R12 made the tile "[a] runner change, self-tested and reviewed on the delta, before G-TIME-n" (ans19:51).

52. T1:666–683, §15's GC14, O7 and F5 bullets. CONFIRMED. Evidence: gcal.py:67–70; R:1697–1699, :1714–1717, :627–630, :288–292; ans19b:58–59; schema.py:876–878; ans20:45.

53. T1:733–771, §18 whole. CONFIRMED. Evidence: all digests recomputed by shell; the closure is 12 of 12; the moves at R:1289–1290, :1372–1376, :1876–1879, :640–643; guard.py:4–10; resume.py:328–335; ans20:54.

54. T1:808–829, §21's runner PINs and flags bullets. CONFIRMED. Evidence: runner.py:17–70; ans20:44; ans18c:44; ans19:50; ans16b:48 and :50; R:5372–5407; A-n3:60.

55. T1:830–872, §21's interval bullet. CONFIRMED. Evidence: interval_out.txt lines 1–17; the rows sha256 recomputed as 93f37a05…0100; schema.py:315–316, :366, :372, :979–982; A-n3:54 and :56 verbatim; C:297–298; rt19b:15; ans19b:45.

56. T1:873–894, §21's gate and N2 bullets. CONFIRMED. Evidence: gcal.json figures.reward_f020; results/raw/2026-11-20_n-gcal-v1_out.txt:379; A-n3:36–42; ans20:28.

57. T1:915–933, §23 whole. CONFIRMED. Evidence: all seven sha256s, the commits, R:223–233, :990–993, :3618–3619, :3635, :6789–6804, :15432–15433, :15471–15478; rt19:10.

58. T1:935–943, §24. CONFIRMED. Evidence: git log subjects; ans15:62; R:2852–2855 and :5262–5263.

59. T1:945–994, Sources. CONFIRMED.

C. T1's other anchors

60. T1:193. Claim: "N1-P steers every `turn_spans` entry of both zones (n:89; schema.py:58–61, :310)". FAIL. The bare ":310" was never re-pinned. At 516b60f, schema.py:310 is `ARM_SPAN_KIND`. At 1641948, line 310 is the `"N2-C"` row of `ARM_CELLS`, and `ARM_SPAN_KIND` is at :315: schema.py's first change since 516b60f is a 5-line insertion at :180, and T1:844 already cites 315–316. Replace ":310" with ":315". Until this is fixed, each of these claims has this one exception: T1:58, :68, :74; T2:23, :61–62; T3:2, :50–51.

61. Sample of re-pinned anchors. CONFIRMED. I read every one of draft 8's 98 R: anchors at 1641948. I also read about 100 code anchors (schema.py, runner.py, gcal.py, n_analyze.py, n_sessions.py, gvec.py, ids.py, keys.py, verify.py, probe.py, guard.py, sessions.py, resume.py). I also read about 80 anchors into the raws, A-n1/A-n2/A-n3, n: and C:. Each says what its citing sentence says, with the quotes compared verbatim, except items 51, 60 and 62.

62. T1:195–196. Claim: "The six S spans average 616.919 tokens here, Fig. A8's 616.91875 (R:15395)". IMPRECISE. R:15395 reads "The six S spans total 616.919 tokens per session on average … One span averages 102.82." Replace with: "The six S spans total 616.919 tokens per session on average, Fig. A8's 616.91875 (R:15395)."

63. The re-pin changed nothing but anchor numbers outside the rewritten sections. CONFIRMED (evidence as in item 22). §7's only change is a re-cited anchor.

D. T1's remaining figures

64. §3 against data/n/gvec/. CONFIRMED.
   - The site block: R values, rel, within, site 32; of_record.
   - The sha16s at index 32; the 24 random sha16s, diffed against gvec.json.
   - files_sha256, and the six files' sha256 by shasum.
   - The six cosines: gvec_cosines.json equals gvec.json's `cosines.named`.
   - The first run's site block, at 616e940, is byte-equal to 355e3a2's record.
   - The R_all diagnostics; n_layers 64, so the capture band is 33–63.
   - The "site: index 32 (ADDENDUM-n1 §6.1)" quote is at results/raw/2026-11-19_n-gvec-v2_out.txt:131.

65. §4 against data/n/gcal/. CONFIRMED.
   - The dose map is the same in gcal.json and dose_map.json.
   - d_eq recomputed with doubles in zsh gives the same double, and so does 2·d_eq.
   - The distances 0.07383401114716737 and 0.21308299442641632 check.
   - files_sha256 match; status PASS; pinnable true.
   - All five batch rows match the stated coherent counts and stops.
   - gcal_turns.jsonl has 240 lines.

66. §5–§8, §12 and §17 against their cited lines. CONFIRMED. Evidence: PIN-n-12 verbatim (n_analyze.py:151–155); keys.py:4–21; probe.py:44–49; the MANIFEST n4 hash; A-n2:18–40; bx2:3, :57, :59, :64, :90–92, :99; bx2id:1; rs4id:1; n_sessions.py:516–531; box:27, :30, :31; R:1845–1847, :2889–2891, :4547–4633, :14805, :14837, :14871–14879, :15361.

TOTALS
- 66 items: 48 CONFIRMED, 10 IMPRECISE, 3 FAIL, 5 NOT CHECKABLE.
- Coverage: A, B, C and D are all complete. In C, I checked far more than 40 anchors (all of R:, plus code and raw anchors). Both normalized comparisons ran.

OBSERVATIONS
1. Item 60's ":310" is the only bare continuation anchor in draft 8; the anchor tools did not match that form. The only other odd forms are inside quotations: "(n :117)" in box:30, "CG:62; BX:18" in ans19:61, and "`schema.py`:64–66" in A-n3:54.
2. T1's Conventions do not define `m:N`, though T1:359 uses "m:159's key-to-generator function".
3. In T1 §5, the n-gcal row's "the same in all four batches" follows keys.py:7–8, which was written before the gate's batch. Under A-n3:38, reward_f020 uses the same prompts and seeds, so there are five batches.
4. In T1 §3, the quote "site: index 32 (ADDENDUM-n1 §6.1)" has no anchor, and its raw is not in Sources.
5. T1's Draft 7 note names the hand re-citations at a coarser grain than T2:63–64; T2 adds gcal.py's status and runner.py's alpha. Both are consistent with the nine blocks. Aligning the two wordings would help the seat.
6. The phrase "The seven files changed since" leaves out valence_core/n/directions.py, which also changed but is not cited. "The seven cited files changed since" is exact.
7. cmds_all:103 and :162 used item 3's pathspec without the mf3 exclusion. Item 3 does not require it, but this pass's own rule does.
8. The check raw names awk and jq among its tools (check.txt:1–2). This fits item 34's fix.

DEPARTURES
- One `git log --format='%h %an' -1` on 1641948 and on b6ea27f printed author names. Item 1 lists only ids, subjects and commit times.
- `git ls-tree` without `--name-only`, on valence_core, valence_core/adapters, valence_core/echo and valence_core/m at 1641948 and 516b60f, printed blob ids with mode and type and no size. Item 1 lists `--name-only`.
- `git log --format=%h -- <path>` and the clean check named data files outside ckpt, reports and mf3 (data/n/gvec, data/n/gcal, data/n/gates, data/n/ids) without item 3's pathspec. The brief's exception names only "non-data files".
- One `echo ===` failed in zsh ("== not found"); nothing ran and nothing was written.
- One command had a stray environment assignment, `awk_unused=1`, before `cut`; no awk ran.
- Otherwise: no interpreter but shasum and the shell's own arithmetic; no file written (process substitution only); no guard marker in any argv (bracketed patterns, and the brief's cd-and-glob form for the closure); nothing under data/mf3, ckpt or reports read or listed; no listing or glob in S.
