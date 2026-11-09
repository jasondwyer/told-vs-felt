# The A-m2 smoke's driver — the values-check of the commit's entry and the review raw's dispositions

*Code's raw, PI date 2026-11-09. Two passes: pass 1 on the drafts, pass 2 on the passages pass 1 corrected.*
- *What was checked:* the entry draft for the driver's commit, and the header and six dispositions of `results/raw/2026-11-09_a-m2-smoke-driver_reviews.md`.
- *How:* a blind agent, read-only. The same agent's Part A, with the report's opening, is in the v0.3 commit's raw, `2026-11-09_a-m2-v03_valuescheck.md`.
- *Then:* Code's disposition of every item not CONFIRMED, each re-checked at source.
- *Nothing ran on a model, and nothing under `data/mf3/ckpt/` was opened.*

## The agent's report: Part B (verbatim; local paths scrubbed)

# PART B — 79 items: 60 CONFIRMED / 10 IMPRECISE / 5 FAIL / 4 NOT CHECKABLE

**ED, the entry**

B1. ED:1–2, the title and its anchors (A-m2 v0.3 §3.2, §4.2; P4 at ans2 §3) — CONFIRMED (D7:3253–3256, :3274–3282; ans2:18).

B2. ED:3, `890084e6…90af` → `c9393a48…4d9b` — CONFIRMED.
- HEAD's and daca8b0's driver is 890084e6c6…028690af.
- D7 and smoke-wt's driver are c9393a4820…0884d9b.

B3. ED:4, what stands — CONFIRMED.
- In smoke-wt, only scripts/mf3_sessions.py differs from daca8b0 under valence_core, scripts and LOCK-m-F3.md.
- daca8b0..2018ffc touches none of those paths.

B4. ED:5–6, F-1's kind, no scoring-stack function touched — CONFIRMED. The diff from HEAD to D7 deletes 0 lines; it only adds (smoke code at D7:530–1175, the self-test at :2035–3211, argparse, and main's branch).

B5. ED:9, a lane of 99 mutants, each killed by a failing check — CONFIRMED.
- L7: 99 lines, 99 KILLED; none survived, was not applied, or crashed; each has at least one fail.
- Every anchor occurs exactly once in D7. m72 and m93–m95 do not apply to driver_r6, so L7 ran on r7's bytes.

B6. ED:10, 0 MAJOR in every round and 7/2/1/1/0/0 MINOR — CONFIRMED (headline lines of R1–R6).

B7. ED:13, P1, P2 and P4 accepted — CONFIRMED (ans2:13–18).

B8. ED:14–16, the forms are constants, checked each run against the committed bytes, the pin and m:258's hygiene — CONFIRMED (D7:550–553, :592–597, :784–808, :1000–1002, :811–815; ST7:169).

B9. ED:17–22, twelve sessions form-major, the cells and item key, the arm key, uncached at cap 60, and `run_session_f3` — CONFIRMED (D7:555–559, :600–632, :1031–1040; ST7:171, :174, :175).

B10. ED:23–24, G-VER's one substitution, restored after each call — CONFIRMED (D7:635–651; ST7:194).

B11. ED:25–29, the counts — CONFIRMED (D7:654–705; ans2:11, :15–16).

B12. ED:30–31, the rule and its stops — CONFIRMED (D7:561–567, :899–910; ST7:186–187).

B13. ED:32–33, counter (b) is a read, and both counters run over all twelve sessions — CONFIRMED (ans2:7; v0.3:48; D7:877–896).

B14. ED:35, the backend STOP — CONFIRMED (D7:1012–1014, for a non-stub adapter; ST7:193).

B15. ED:36–37, the session STOPs, and a reasoning-line fire ends its session only — CONFIRMED (D7:1043–1076; valence_core/mf3/verify.py:231–232; m:265; ST7:191).

B16. ED:37–38, "Every stop a session carries is named on its G-VER, READS or RAW BLOCK line." — IMPRECISE.
- It holds when one of those three lines is the first stop (D7:1059–1073; ST7:202).
- A session whose only stop is a task-round fire stops on a HAIR TRIGGER line (D7:1074–1076).
- A write that fails, is refused by the pin, or does not serialize names only itself (D7:946, :955, :957). ED:78 discloses this for the write.

B17. ED:39–40, a STOP selects nothing, and no tally or rule is printed because summary.json is written first — CONFIRMED (D7:1084–1093 runs before :1096–1107; ST7:198).

B18. ED:40, "A summary that a failed write left on disk is renamed summary.json.stopped." — IMPRECISE.
- `_summary_stopped` (D7:961–988) renames it, or removes it when the rename fails. If both fail, or its presence cannot be examined, the STOP line says it is no selection.
- It treats a leftover summary.json.tmp the same way.
- It runs only while DIR is still the directory made (D7:1090–1093).
- D7:33–36 states all of this exactly.

B19. ED:41, the refusals — CONFIRMED (D7:3275–3277, :750–781). The list is not exhaustive. It also refuses:
- no --smoke-out;
- a path that does not resolve;
- a parent that is not a directory or not writable;
- --smoke-out without --smoke;
- a missing lock flag (ST7:188–189).

B20. ED:42–43, the re-check before mkdir and the pin after — CONFIRMED (D7:1018–1027, :919–932, :942–947; ST7:200, :203).

B21. ED:44, it never names, opens or creates the checkpoint — CONFIRMED (no checkpoint path or function in D7:530–1175; :784–786; ST7:206–207).

B22. ED:45–47, what the raw prints — CONFIRMED (D7:824–854, :1096–1107; ST7:184).

B23. ED:48, what lands under DIR — CONFIRMED (D7:1053–1057, :1086–1088).

B24. ED:50, "The 160 checks of the time wiring pass unchanged" — CONFIRMED.
- ST7 has 202 checks: 160 plus 42.
- The 160 names equal, in order, those in acde2d8's results/raw/2026-11-07_mf3-time-wiring_selftest.txt (160/160). Only temp paths and help text differ.
- All 160 pass.

B25. ED:51–52, 42 smoke checks, including A-m2's text and sha — CONFIRMED (ST7:166–207; :168–169).

B26. ED:53, "the keys, cells and seeds against G-TIME-F3's" — IMPRECISE.
- ST7:171 checks the item key and the cells against G-TIME-F3's.
- The arm key is the smoke's own, and the seeds are "the smoke key's stream in m:159's order". By design they are not G-TIME-F3's (v0.3:44).

B27. ED:54–57, P1 per form, the match and (a), the rule at its bounds, the refusals, and the stub runs — CONFIRMED (ST7:174, :176–181, :186–189).

B28. ED:58, "every STOP, and that it prints no tally or rule" — FAIL. No smoke check exercises:
- the A-m2 STOP inside run_smoke_sessions (D7:1001–1002; every stub run patches addendum_m2_problems to [] at :2430);
- the PROVENANCE STOP (:1005–1009);
- the licence, laptop-preflight or startup STOPs (stubs skip them, and the backend case patches them out at :2819–2821);
- a STOP from the load itself (the Qwen-branch loader is a stand-in, :2755).
- Covered: SNAPSHOT RE-READ and MOVED, MODEL ID, SEAM, BACKEND, OUT DIR, SERIALIZE, G-VER, READS, RAW BLOCK, HAIR TRIGGER, and the summary paths.

B29. ED:59–60, "a failure at each write and at the directory's fsync, and a record that does not serialize" — IMPRECISE.
- ST7:198 fails the first session write, the second, and summary.json's — not each of the thirteen writes. It also covers NaN.
- ST7:199 covers the fsync.

B30. ED:61–62, the directory moved, replaced or removed, and what a failed summary write leaves — CONFIRMED (ST7:203, :204).

B31. ED:64–66, the traps, their controls as built and as installed, the per-site records, and the data/mf3 hash — CONFIRMED (D7:2144–2175, :2189, :2247–2308; ST7:166–167, :207). Notes:
- The loader is "a trap or a stand-in" (D7:2036–2037).
- The hash reads every file under data/mf3, ckpt included, outside the traps (D7:2052, :2180–2189). The entry does not say so.

B32. ED:67–68, how the lane runs — CONFIRMED (lane.py: each mutant written over the driver, then a fresh `-B` subprocess, then the driver restored; L7 "restored: True").

B33. ED:69–71, each report verbatim, then the disposition — CONFIRMED (diffs of the six RR sections against R1–R6 show only path scrubs).

B34. ED:72, "Rounds 1 to 5: every item was applied in the next round's bytes, and that round reports on it." — FAIL.
- R2:27–28 records round-1 NOTE 1 "not applied, and harmless" and NOTE 7 "rightly not applied". r2_delta.diff changes neither.
- R1:105 asked of NOTE 1, "Say so in the entry, or reorder"; ED does not say so.
- R3:116 could not map round-2 NOTE 6. r3_delta.diff shows it applied.

B35. ED:73, "on the coordinating session's instruction of 2026-11-09" — NOT CHECKABLE.

B36. ED:73–74, the five NOTEs applied or disclosed, not reviewed again — CONFIRMED (RR:680–701; D7 = driver_r6.py + r7_delta.diff).

B37. ED:74–75, "One change is to production code; the rest are the self-test and wording." — IMPRECISE.
- The production hunks are NOTE 1's guard (D7:1090–1093) and also the pin STOP's message ("nothing written" → "{path.name} not written", r7_delta.diff:15–25, D7:946–947), plus docstrings and a comment.
- There is one behaviour change.

B38. ED:76–79, the three disclosed residuals — CONFIRMED (RR:685, :689, :691; D7:1025–1029, :1050–1057). Note: D7:921–923 also discloses the same window between the pin check and each write, which is not listed.

B39. ED:81, committed by path and nothing ran on a model — NOT CHECKABLE (commit-time).

B40. ED:82–83, the next step (about an hour of Qwen, one process) — CONFIRMED (ans2:47; de729c4's message "~1 h Qwen, announced"; daca8b0's laptop rule). v0.3:66 says ≈ 50 min.

**RR header**

B41. RR:3, "PI date 2026-11-09" — NOT CHECKABLE. It must equal @@PIDATE@@.

B42. RR:4, built model-free in a scratch worktree at daca8b0 — CONFIRMED (smoke-wt and review-wt are both at daca8b03…, detached).

B43. RR:5, each reviewer ran the self-test and its own probes and committed nothing — CONFIRMED.
- Self-tests: R1 187/188, R2 191/192, R3 191/192, R4 194/195, R5 198/199, R6 201/202.
- Both worktrees are still at daca8b0, and R2, R4, R5 and R6 state no commits or git writes.

B44. RR:5, "opened nothing under data/mf3/ckpt" — IMPRECISE.
- R1 makes no such statement.
- R2:9, R3:10, R4:84, R5:80 and R6:73 each disclose that the self-test they ran reads the bytes under data/mf3/ckpt to hash them.
- R6:79 discloses three unpruned find traversals into it.

B45. RR:6, scrubbed to `<scratch>/`, `<repo>/`, `<home>/` and `<id>` — IMPRECISE (minor).
- Verbatim holds.
- Only `<scratch>/` (10 sites) and `<home>/` (RR:79) occur. `<repo>/` and `<id>` appear only on RR:6 itself.

B46. RR:6, "that report is the record that the dispositions were applied" — IMPRECISE. R2 records two round-1 items as not applied, and R3:116 could not map round-2 NOTE 6 (see B53, B55).

B47. RR:7, nothing ran on a model — CONFIRMED (R4:92, R5:88, R6:85).

B48. RR:9–18, the table's shas and tallies — CONFIRMED.
- Round 1, `cc55377c`: its git blob is feebbd2, which matches review_diff.txt's "index 53a58c7..feebbd2" (53a58c7 is daca8b0's driver).
- The other rounds: `b05c07cc`; `9591a418…ac62` (R3:3); `b55c4b36` (R4:3); `0b508640` (R5:3); `4a98f74e` (R6:3).
- R1 and R2 name no sha. The tallies 0/7/8, 0/2/10, 0/1/12, 0/1/6, 0/0/5 and 0/0/5 match.

B49. RR:19, the committed row — CONFIRMED (c9393a48 = r6 + r7_delta). The instruction is not checkable.

B50. RR:21, rounds 5 and 6 had no MAJOR or MINOR — CONFIRMED.

B51. RR:21, the quoted instruction — NOT CHECKABLE.

B52. RR:23–25, the lane covers round 6 — CONFIRMED (as B5 and B32).

**RR dispositions**

B53. RR:163, round 1: "All 15 items were applied in round 2's bytes." — FAIL.
- 15 = 7 + 8, and R2 does report on each item.
- But it records NOTE 1 "not applied, and harmless" (R2:27) and NOTE 7 "rightly not applied" (R2:28). r2_delta.diff has neither.
- So 13 of 15 were applied.

B54. RR:243, round 2: "All 12 … applied … NOTE 6's three wording items included" — CONFIRMED (12 = 2 + 10; r3_delta.diff:104–108, :135–140, :270–274).

B55. RR:243, "Round 3's 'Round-2 items' reports each one." — IMPRECISE. R3:116 says "I can't map NOTE 6 to a specific hunk without its text".

B56. RR:243, the residuals became round 3's items — CONFIRMED (R3:112–115).

B57. RR:369, round 3: all 13 applied — CONFIRMED (13 = 1 + 12; R4:67–80. The mkdir half of MINOR-1 and the installation half of NOTE 3 carry over as R4's NOTEs 4 and 1).

B58. RR:370, NOTEs 5 and 6 were "not live" and applied anyway — CONFIRMED (R3:64, :69; D7:737–748, :771–779; ST7:188).

B59. RR:371, NOTE 12 was applied to the lane, outside the driver — CONFIRMED (lane.py:4; R4:80).

B60. RR:371, "had never matched, so every earlier lane count was one too high" — FAIL.
- The old substring "A-m2 is committed at HEAD" (lane_r3.py:64) did match the check's name in driver_orig.py:1836, driver_pre_iii.py:1837 and round 1's bytes (driver_pre_r2.py:1833).
- lane_final, lane_final2, lane_final3 and lane_v02 all exclude it.
- It stopped matching only after round 2 renamed the check "A-m2 v0.2 is committed at HEAD" (driver_pre_r3.py:1927). Only lane_r2, lane_r3 and lane_r3b counted it.
- What was one too high was each mutant's fail count, not the number killed (R3:101).

B61. RR:371, "No mutant was falsely reported killed." — CONFIRMED. lane_r2 and lane_r3b show at least 2 fails per mutant. In lane_r3, one mutant shows "1 fail(s), crashed", so the crash killed it.

B62. RR:372, round 4 reports on each round-3 item — CONFIRMED (R4:67–80).

B63. RR:474, round 4: all 7 applied, and round 5 reports each — CONFIRMED (R5:69–76).

B64. RR:475, MINOR-1 was a regression, now back inside the try, with its cases — CONFIRMED (r4_delta.diff:95–98; r5_delta.diff:7–12; ST7:188; R5:70).

B65. RR:573, round 5: all 5 applied — CONFIRMED (R6:64–69). NOTE 5's sentence was "reworded but is false again", which became R6's NOTE 5.

B66. RR:680, "One production change: NOTE 1's guard. Everything else is the self-test or wording." — IMPRECISE (as B37; the message change is listed at RR:700).

B67. RR:682, NOTE 1's guard — CONFIRMED (D7:1087–1093).

B68. RR:683, os.unlink and os.remove trapped, with live controls — CONFIRMED (D7:2173–2174, :2291–2292; ST7:167).

B69. RR:684, the decoy summary.json is left untouched — CONFIRMED (D7:3094, :3101, :3125–3127).

B70. RR:685, the swap window is disclosed and O_DIRECTORY/dir_fd is not built — CONFIRMED (neither O_DIRECTORY nor fstat appears in D7).

B71. RR:687, NOTE 2's two cases — CONFIRMED (r7_delta.diff:206–249; ST7:202).

B72. RR:688, the comment and the check's headline are narrowed — CONFIRMED (D7:1057–1059).

B73. RR:689, the disclosure on a failed session write — CONFIRMED (D7:1050–1057; R6:23–25).

B74. RR:690, NOTE 3's removed-directory case — CONFIRMED (D7:3106–3111; ST7:203).

B75. RR:691, the disclosure on the os.stat after mkdir — CONFIRMED (D7:1025–1029; R6:34).

B76. RR:693–695, NOTE 4: 35 entries, 24 stub runs, and inspect.signature(...).bind() — CONFIRMED (D7:3205 asserts `== 24` and `== 35`; ST7:207 "(0, [], [], 0, 24, 35)"; D7:2253–2260).

B77. RR:697–700, NOTE 5's items — CONFIRMED.
- r7_delta.diff hunks 1, 2, 5 and :66–90.
- The smoke's only removals are `_summary_stopped`'s at D7:983 and m's temp-file unlink (R5:44–45).

B78. RR:701, three unpruned find traversals that printed no name from ckpt — CONFIRMED (R6:79).

B79. RR:701, "That is within O2-3's name-only allowance, and nothing there was opened." — FAIL.
- One of the three traversals was "a newer-than filter", which is `find -newer`.
- O2-3's own text names that form among the forbidden ones: "no size or time metadata of … data/m/ckpt … (ls -l/-t/-s, stat, du, wc -c, find -newer, …)" (RESULTS.md@2018ffc:3072–3074, added at 0fa8539).
- The seat recorded the same kind of traversal as "O2-3, departed from … accepted, inert" (results/raw/2026-10-19_m-design-to-code_VERDICTS_read.md:86).
- Q-F3's carried form allows only name-only listings, with "no size or time metadata of data/mf3/ckpt" (D7:46–48).
- In mitigation, the traversals printed nothing, in a worktree copy. "Nothing there was opened" holds for the traversals, but R6's self-test did read those bytes to hash them (R6:73).

**Placeholders, Part B:**
- @@PIDATE@@, @@RDATE@@, @@ST@@ (ED:8, :49), @@VC@@, @@STAMP@@, @@VCDETAIL@@ and @@ST-SITE@@ (RR:24) were skipped.
- ED:49's "(… on this commit's base, A-m2 v0.3 committed)" and RR:24 depend on a run not yet made. The only run on file, ST7, is 201/202 in the worktree, where the A-m2-at-HEAD check fails.
- B41 also depends on @@PIDATE@@.

**Omissions (no verdict):**
- ED does not address round-1 NOTE 1 (R1:105).
- ED does not disclose that the self-test's data/mf3 hash reads the ckpt bytes (the self-test's docstring does, at D7:2052).

All files cited are under <repo> and <scratch>/am2/ (S/).

## Code's dispositions (Part B)

**The five FAILs**, each re-checked at source and applied:
- **B28.** "every STOP" was wrong. The entry now lists the STOPs the self-test exercises after the load: those before any session, and those checked to print no tally or rule. It also names those no case reaches: the in-run startup, licence, laptop-checklist, A-m2, PROVENANCE, renders and schedules STOPs, and a failing load.
- **B34 and B53.** Round 1's NOTEs 1 and 7 were not applied, as round 2's report says under "Round-1 NOTEs". The entry and the review raw now say so.
  - NOTE 1 asked that the order after the load be stated, and the entry states it.
  - NOTE 7's `git status` comparison is barred by `stages._git`. The write traps, from round 4's bytes, cover the guarded writes it was after. rmdir, shutil, links, truncation and io.FileIO stay outside them.
- **B60.** The lane's exclusion did match until round 1's fixes renamed the check. `driver_pre_r2.py` has "A-m2 is committed at HEAD" and `driver_r2.py` has "A-m2 v0.2 is committed at HEAD". Only the lanes of rounds 2 and 3 counted the check. The review raw now says so.
- **B79.** The `find -newer` traversal is a departure from O2-3, not within its allowance. The entry and the review raw now report it as a departure for the seat, with the mitigation and the precedent: the 2026-10-19 VERDICTS read, item 5, "accepted, inert".

**The IMPRECISE items**, applied:
- **B16:** the hair naming is stated as the code does it.
  - When the first stop is G-VER, READS or RAW BLOCK, that line names the session's other stops.
  - A task-round fire alone stops on HAIR TRIGGER.
  - A failed write names only itself.
- **B18:** what a failed summary write leaves, as the code does it.
  - The summary or its temp file is renamed, or removed if the rename fails.
  - This happens only while DIR is unmoved; otherwise the STOP line says so.
- **B26:** the cells and the item key are G-TIME-F3's; the arm key and seeds are the smoke's own.
- **B29:** the write-path cases are named: the first and second session writes, summary.json's, the fsync, and a record that does not serialize.
- **B37 and B66:** there is one behaviour change in production code. Beside it are a STOP message's wording, docstrings and a comment.
- **B44:** the header now says rounds 2 to 6 disclose the self-test's hash of the checkpoint's bytes, and round 6 the traversals.
- **B45:** the scrub placeholders are named as they occur: `<scratch>/` and `<home>/`.
- **B46:** "the record of what was applied", with round 1's two exceptions.
- **B55:** round 3 could not map round 2's NOTE 6 to a hunk; round 3's delta applies it.

**Notes and omissions**, applied:
- **B38:** the window between the pin and the write it guards is added to the disclosed residuals.
- **B31 and the omission:** the entry now says the self-test's `data/mf3` hash reads the checkpoint's bytes, outside the traps.

**NOT CHECKABLE:**
- B35 and B51: the coordinating session's instruction, quoted from its message of 2026-11-09.
- B39 and B41: filled at write time.

## Pass 2 (the corrected passages): its Part B items (verbatim; local paths scrubbed)

The pass's opening and its rule-breach disclosure are in the v0.3 commit's raw, `2026-11-09_a-m2-v03_valuescheck.md`.

### Passage 3: ED
13. ED:39–40, a G-VER/READS/RAW BLOCK line names the session's other stops, and a task-round fire alone stops on HAIR TRIGGER: CONFIRMED (D7:1057–1076).
14. ED:40–41, "the raw, printed before the write, carries the rest": IMPRECISE.
   - When the line reads raise, `reads` is None, so the block's lines part is skipped (D7:868). `lines_error` goes only into the JSON (D7:1054–1056).
   - So a READS error plus a failed write leaves that error in neither stdout nor DIR.
   - If the block's record part raises (D7:863–867), the G-VER status and the round lines with their scaffold hits are not printed either.
15. ED:42–43, "A STOP selects nothing"; the summary is written before the prints: CONFIRMED (D7:1086–1106).
16. ED:44–47, the sub-bullets: CONFIRMED (D7:961–988, 1092–1093; ST7:204).
17. ED:52–56, the three-step order: CONFIRMED (D7:997–1017).
18. ED:52, "is the stage's own (`_begin`, then `_licensed`)": IMPRECISE. Only step 1 follows the stage.
   - The stage's `_begin` runs `_start_provenance` before the startup checks (stg:670–672).
   - `run_gate_stage` builds the renders and schedules before f3_startup (stg:934–941).
   - The smoke runs PROVENANCE after the licence (D7:1005) and f3_startup before the renders and schedules (D7:1015–1017).
   - The A-m2 and BACKEND STOPs have no stage counterpart. R1 NOTE 1 used the phrase only for where the licence falls.
19. ED:57, P4's order differs, NOTE 1 asked, not reordered: CONFIRMED (pre:167–173; RR:136).
20. ED:63, the 160 time checks pass unchanged: CONFIRMED.
   - ST7 has 202 checks: 42 smoke and 160 others.
   - None of the 160 fails.
   - Their names match acde2d8's selftest raw in order, apart from one temp path.
21. ED:64, 42 smoke checks: CONFIRMED (ST7:166–207).
22. ED:66, the cells and keys: CONFIRMED (D7:2334–2358; ST7:171, 174).
23. ED:71–72, the STOPs exercised, each with no tally or rule: CONFIRMED.
   - Note: SNAPSHOT RE-READ/MOVED and MODEL ID (ST7:190) assert exit 4 and no session; `run_smoke_sessions` is a stand-in there, so "no tally" holds by construction, not by a `no_rule` check.
24. ED:72–73, the list of STOPs a stub run does not reach: IMPRECISE (incomplete). Two post-load STOPs that no case triggers are missing:
   - the renders STOP: `_renders_of_record`, D7:1016, raising "RENDERS MISMATCH" (stg:622–624);
   - the schedules STOPs: `load_committed`, D7:1017, raising SCHEDULES NOT CLEAN / MANIFEST UNREADABLE / SHA MISMATCH / FILE MALFORMED (stg:515–535).
   - Every stub run passes the correct renders sha (D7:2448).
25. ED:74–75, the write path: CONFIRMED (ST7:198–199).
26. ED:76–77, the directory moved, replaced or removed, and what a failed summary write leaves: CONFIRMED (ST7:203–204).
27. ED:79, the loader, checkpoint functions, ckpt opens and guarded writes are trapped: CONFIRMED.
   - Note: in `qwen_case` the loader is a stand-in, not a trap (D7:2745–2755), as the docstring says (D7:2036–2037).
28. ED:80–81, positive controls as built and installed, every site records, hash before and after: CONFIRMED.
   - There are 24 stub runs and 35 `traps()` entries over 7 sites (D7:3205; ST7:207).
29. ED:81–82, the hash reads every file there, ckpt included, outside the traps: CONFIRMED (D7:2180–2189, 3202).
30. ED:88–89, "every item was applied in the next round's bytes … two exceptions from round 1": IMPRECISE.
   - Round 3's NOTE 12 was applied to lane.py, not the driver; R4 says "closed outside the driver" (RR:465).
   - Note: RR:246 treats round 2's NOTE 6 as an exception ("can't map", RR:369). The entry doesn't, though r3_delta does apply it.
31. ED:90, the NOTE 1 sub-bullet: CONFIRMED.
32. ED:91, "The write traps cover that ground": IMPRECISE (minor).
   - `_git` does bar status (stg:197).
   - But the traps cover guarded writes only: D7:2043–2044 puts rmdir, shutil, links, truncation and FileIO outside them, where a `git status` comparison would see any change.
33. ED:92, the coordinating session's instruction: NOT CHECKABLE.
34. ED:92–94, one behaviour change, plus wording, docstrings and a comment; the rest is the self-test: CONFIRMED.
   - r7_delta's production hunks are the module docstring, the pin STOP's wording, the comment, NOTE 1's guard and run_smoke's docstring. All later hunks are in `_selftest_smoke` (starting at r6:2025).
35. ED:95–98, the residuals: CONFIRMED (D7:921–923, 1025–1029, 1059–1061; RR:692).
36. ED:99–102, the three traversals, O2-3 naming `find -newer`, and Q-F3's form: CONFIRMED (RESULTS.md@2018ffc:3072–3074; D7:46–48).
   - Note: R6 says only "a newer-than filter" (RR:665). The `-newer` flag is Code's reading.
37. ED:103, "nothing there was opened": IMPRECISE (minor).
   - R6 says only "None printed a name from there."
   - The traversals listed ckpt's entries.
   - The same round's self-test opened and hashed the bytes there (RR:659).
38. ED:104, a fresh checkout with checkout-time files: CONFIRMED. `git worktree list` shows review-wt at daca8b0; its root, `.git` and CLAUDE.md were created at 11-09 00:28:02. Nothing under `data/` was examined.
39. ED:105–106, the precedent: CONFIRMED (the 2026-10-19 VERDICTS read, :86, item 5, "accepted, inert").
   - Note: that ruling also relied on "the metadata window … closed at the VERDICTS line". Q-F3's window is still open.

### Passage 4: RR
40. RR:5, the How line: CONFIRMED.
   - Note: round 1's NOTE 7 (RR:155) also states that its self-test hashed `data/` including ckpt.
41. RR:6, the This-raw line: CONFIRMED.
   - All six reports match `review_rN_body.md` after the `<scratch>/` and `<home>/` substitutions.
   - No `/private/` or `/Users/` path is left.
42. RR:163, 13 of 15 applied: CONFIRMED (RR:189–200).
43. RR:164, "The order after the load is the stage's own": IMPRECISE (minor), as #18. Note that R1 and R2 (RR:198) said the same.
44. RR:165, "the write traps added in rounds 3 to 6 now cover what NOTE 7 asked": IMPRECISE (minor).
   - The traps first appear in round 4's bytes: `wrote_repo` occurs 0 times in `driver_pre_r4` and 10 times in `driver_r4b`.
   - They cover guarded writes only, as #32.
45. RR:245–247, round 2: CONFIRMED. r3_delta applies NOTE 6's three wording items.
46. RR:373, "All 13 items were applied in round 4's bytes": IMPRECISE (minor). This contradicts the disposition's own RR:375 on NOTE 12.
47. RR:374, NOTEs 5 and 6: CONFIRMED (D7:737–781, 2644/2672).
48. RR:375–378, the lane history: CONFIRMED.
   - `driver_pre_r2` has "A-m2 is committed at HEAD"; `driver_r2` has "A-m2 v0.2 …".
   - In lane_r2, lane_r3 and lane_r3b, every first-fail is that check, and every mutant has at least 2 fails, except lane_r3's m44 ("1 fail(s), crashed").
   - lane.py:4 now matches the check by pattern.
49. RR:379, round 4 reports on each item: CONFIRMED.
50. RR:687, round 6's opening: CONFIRMED (as #34).
51. RR:688–692, NOTE 1: CONFIRMED (D7:1087–1094, 2173–2174, 2291–2292, 3087–3128). There is no `O_DIRECTORY` or `fstat` in D7.
52. RR:693–696, NOTE 2: IMPRECISE. The "raw carries the rest" disclosure has the same gap as #14.
53. RR:697–698, "That is a double fault": IMPRECISE (minor). R6's exp_S reached it with a single injected EIO (RR:620).
54. RR:699–702, NOTE 4 (35, 24, `.bind()`): CONFIRMED.
55. RR:703–707, NOTE 5: CONFIRMED. The longest line is now 131 columns (D7:90); the old 153-column line is gone.
56. RR:708–712, the O2-3 disposition: IMPRECISE (minor). "Nothing there was opened" has the same problem as #37. The quote, the checkout and the precedent are CONFIRMED.

### Passage 5: VA and VB (items 65–82, VB)
65. VB:3–7, the header: CONFIRMED.
66. VB:252, B28: IMPRECISE (as #24).
67. VB:253–255, B34/B53: IMPRECISE.
   - Round 1's part is true.
   - "The write traps now cover it" overstates (#32).
   - The entry's NOTE 12 exception is still missing (#30).
68. VB:256, B60: CONFIRMED.
69. VB:257, B79: CONFIRMED.
70. VB:260–263, B16: CONFIRMED.
71. VB:264–266, B18: IMPRECISE (minor). The entry's sub-bullets don't carry "otherwise the STOP line says so" for a moved directory; RR:689 does.
72–80. B26, B29, B37/B66, B44, B45, B46, B55, B38, and B31 with its omission: each CONFIRMED against ED and RR.
81. VB:280, B35/B51: NOT CHECKABLE.
82. VB:281, B39/B41: NOT CHECKABLE (the same note as #62 applies to RR:3).

## Code's dispositions (pass 2, Part B)

Every IMPRECISE item was re-checked at source and applied:
- **#14 and #52:** the entry and the review raw now disclose the two gaps in "the raw carries the rest". Each needs a second fault:
  - a line-read error is kept in the session's JSON only;
  - a block part that raises drops its own lines.

  If the write then fails, those are lost.
- **#18 and #43:** the order after the load is stated as it is. Only step 1 follows the stage. The stage records provenance earlier, and builds the renders and schedules before `f3_startup`.
- **#23 and #24, #66:** the STOPs are now listed by kind:
  - those before any session;
  - those checked to print no tally or rule;
  - those no case reaches, now including the in-run renders and schedules STOPs.
- **#30 and #67:** the exceptions to "every item applied" are now listed: round 1's NOTEs 1 and 7, round 2's NOTE 6, and round 3's NOTE 12.
- **#32, #44 and #67:** the write traps are dated to round 4's bytes. They cover guarded writes only; rmdir, shutil, links, truncation and io.FileIO stay outside them.
- **#36:** the `find -newer` form is marked as Code's reading of the report.
- **#37 and #56:** "None printed a name from there or read a file's contents; the same round's self-test hashed those bytes".
- **#39's note:** the precedent's closed-window point is stated. Q-F3's window is still open.
- **#40's note:** every round's report says the self-test's hash reads the checkpoint's bytes, round 1 in its NOTE 7.
- **#46:** round 3's disposition now reads "12 of the 13 items were applied in round 4's bytes, and NOTE 12 to the mutation lane".
- **#53:** "a double fault" is replaced by round 6's own probe, which reached it with one injected EIO.
- **#71:** the entry now carries the moved-directory clause.

**NOT CHECKABLE:** #33, #81 and #82, the instruction and the write-time fills, as in pass 1.
