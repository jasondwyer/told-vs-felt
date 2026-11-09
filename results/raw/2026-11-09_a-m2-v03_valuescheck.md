# ADDENDUM-m2 v0.3 — the values-check of the commit's entry and the referent raw's dispositions

*Code's raw, PI date 2026-11-09. Two passes: pass 1 on the drafts, pass 2 on the passages pass 1 corrected.*
- *What was checked:* the entry draft for the v0.3 commit, and the header and dispositions of `results/raw/2026-11-09_a-m2-v03_referent-check.md`.
- *How:* a blind agent, read-only. One agent checked this commit's drafts (Part A) and the smoke driver's (Part B, in that commit's raw, `2026-11-09_a-m2-smoke-driver_valuescheck.md`). The report's opening and Part A are given here.
- *Then:* Code's disposition of every item not CONFIRMED, each re-checked at source.
- *Nothing ran on a model, and nothing under `data/mf3/ckpt/` was opened.*

## The agent's report: its opening and Part A (verbatim)

BLIND VALUES-CHECK: two drafts for the A-m2 v0.3 commit (Part A) and two for the smoke-driver commit (Part B). Read-only.

## Tallies
- **Part A** (entry_v03.md and the v0.3 referent raw's header and dispositions): 43 items. 36 CONFIRMED, 3 IMPRECISE, 0 FAIL, 4 NOT CHECKABLE.
- **Part B** (entry_driver.md and the reviews raw's header and six dispositions): 79 items. 60 CONFIRMED, 10 IMPRECISE, 5 FAIL, 4 NOT CHECKABLE.
- **The 5 FAILs, all in Part B:**
  - B28: "every STOP" is tested.
  - B34 and B53: round 1's items were "all applied".
  - B60: the lane exclusion "had never matched".
  - B79: the find traversals were "within O2-3's name-only allowance".

## How I worked
- Nothing under data/mf3/ckpt was opened, listed or hashed in any tree. Every git command was limited to paths outside data/.
- No git writes, no files written, no self-test or lane run.
- The only Python was `python3 -I` with the standard library, parsing lane.py's mutant list with ast without running it.

## Abbreviations
- E3 = S/entry_v03.md. R3 = S/2026-11-09_a-m2-v03_referent-check.md.
- ED = S/entry_driver.md. RR = S/2026-11-09_a-m2-smoke-driver_reviews.md.
- D7 = S/mut/driver_r7.py. ST7 = S/selftest_r7.txt (the smoke checks are its lines 166–207). L7 = S/mut/lane_r7.txt.
- R1–R6 = S/review_r1_body.md … review_r6_body.md.
- block = the OPEN #50 raw at 2018ffc.
- v0.2, v0.3, ans2, ans3, m:N, lock: as in the brief.

# PART A — 43 items: 36 CONFIRMED / 3 IMPRECISE / 0 FAIL / 4 NOT CHECKABLE

A1. E3:1 "ADDENDUM-m2 v0.3 — COMMITTED (A-m2 §6 item 2)" — CONFIRMED (v0.3:72). Flag: v0.3:72 asks for "the routing blocks of 2026-11-08 verbatim", and E3 has @@RDATE@@ and @@ROUTING@@.

A2. E3:2–3, sha256 83093812afdd…55d9fa67 — CONFIRMED in full by shasum. The file is untracked at root now; "tracked" is what the commit does.

A3. E3:4–5, v0.1 `cdcc8e86…53f0` and v0.2 `69e23212…cb47`, to archive/ uncommitted "as v0.3's header and §6 item 2 have it" — CONFIRMED.
- Both shas recomputed; v0.3:3 and :72 say so.
- `git log --all` shows no commit of any A-m2 version.
- Both files are still at root; the move happens at the commit.

A4. E3:6–7, the check is v0.3 §6 item 1's, against the answer on #50 — CONFIRMED (v0.3:71).

A5. E3:7, "HEAD at 2018ffc at the start and the end" — NOT CHECKABLE.
- The agent's report (S/v03ref_report_extracted.md) does not state HEAD at start or end. The v0.2 report did (v0.2 referent raw @2018ffc:3).
- HEAD is 2018ffc now, which is consistent.

A6. E3:7–8, "8 items: 6 CONFIRMED, 2 IMPRECISE (three findings), 0 OPEN, 0 FAIL" — CONFIRMED (R3:13; item headings R3:29–101; findings 3a, 8a, 8b).

A7. E3:8–9, "No item moves a form, a figure, a bar, a key or the rule" — CONFIRMED (R3:13, :45–58, :102–103: wording and anchors only).

A8. E3:9–12, the three findings as listed — IMPRECISE.
- Bullets 2 and 3 match 8a and 8b.
- Bullet 1 is only one of 3a's points. 3a's disposition (R3:129–134) also records:
  - ans3 and v0.3 word the second half differently;
  - the "what changed" list understates the change, since it does not mention that "reported at each stage's entry and at VERDICTS" was struck;
  - ans3's "G-ID-F3 … is unaffected" is not in v0.3.
- 8a (R3:137) also records that the anchors paragraph has no ganl anchor.

A9. E3:13, "Next: the smoke driver's commit, then the smoke" — CONFIRMED (v0.3:72; ans3:18). Note: E3 has a second "Next" at :44–48.

A10. E3:17–19, ans2 at `de729c4`, `09d856ef…ea29` — CONFIRMED (the blob at de729c4 equals the working copy; de729c4 adds it).

A11. E3:20–21, ans3 `d6296d44…2b97`, §1 — CONFIRMED (ans3:5–10).
- Flag @@ANS3AT@@: ans3 is untracked and was never committed (`git log --all` is empty), and E3:42's path list does not include it.

A12. E3:22–23, "(its own list; the rest of v0.2 stands, §3.1's forms, §3.2's design and §3.3's rule and stops included)" — IMPRECISE.
- True: §3.1 (:37–42), §3.2 (:44) and §3.3's rule and stops are unchanged.
- But the diff also changes text outside "its own list":
  - :3, the header;
  - :5, the anchors (`(de729c4)` and a new `ans3:` anchor);
  - :7;
  - §6 items 1–2 (:71–72).

A13. E3:24–32, the §3.4 paraphrase and "Code's sentence adopted in the text" — CONFIRMED (v0.3:48, :7; ans3:7 "Code's §4 sentence, verbatim in substance … goes into the committed text").

A14. E3:33–34, §3.3's stopped smoke (#49) — CONFIRMED (v0.3:46, last sentence; ans3:10).

A15. E3:35–36, §4.2's pin (#48) — CONFIRMED (v0.3:56; ans3:9).

A16. E3:37–38, "#48, #49 and #50 are answered in ans3 §1 and written into v0.3, so none is carried" — CONFIRMED.
- These were the v0.2 check's only OPENs (v0.2 referent raw @2018ffc:19, :201, :206, :210).
- ans3:7, :9, :10 answer them; v0.3:48, :46, :56 carry them.

A17. E3:38, the v0.2 check and its IMPRECISE items stay as committed at 2018ffc — CONFIRMED (2018ffc --stat; that raw's :241 "12 distinct").

A18. E3:39–40, the referent raw is the report verbatim, then Code's disposition of every item not CONFIRMED — CONFIRMED.
- The diff against S/v03ref_report_extracted.md shows one path → `<repo>/` and one trailing blank line.
- Dispositions cover 3a, 8a and 8b, the only items not CONFIRMED.

A19. E3:42–43, "Committed by path: …; nothing ran on a model" — NOT CHECKABLE (commit-time). See A11 for ans3.

A20. E3:44–46, the driver pinned to v0.3's sha, its commit next, and the standing laptop rule — CONFIRMED (D7:545–547; v0.3:72; daca8b0's message "the standing laptop rule (model runs announced to the coordinating session and serialized) [adopted]").

A21. R3:3, "PI date 2026-11-09" — NOT CHECKABLE. Flag: R3 hard-codes the date while E3:1 is @@PIDATE@@.

A22. R3:4, the v0.3 sha, "untracked at root", ans3's path and sha, "§1 and §3 item 1", and the block at 2018ffc — CONFIRMED (ans3 §1 = :5–10, §3 item 1 = :18; the block's blob at 2018ffc equals the working copy, `794112…82a6`).

A23. R3:5, HEAD at 2018ffc — NOT CHECKABLE (as A5).

A24. R3:6, "verbatim (one local path scrubbed to `<repo>/`)" — CONFIRMED (the one substitution is at R3:15).

A25. R3:7, nothing ran on a model and nothing under ckpt was opened — CONFIRMED for the agent (R3:25). Code's own part is not checkable.

A26. R3:117–120, none moves a form, bar, key, cell, rule, a figure, or what an entry prints before VERDICTS — CONFIRMED (the scope's first half equals ans3's; see A30).

A27. R3:122, "as PROPOSAL-p's v0.2 was (18b0111) and as A-m2 v0.2's dispositions had it (2018ffc)" — CONFIRMED.
- 18b0111's message: "v0.2 is committed as delivered; the items go to the seat as dated notes".
- The v0.2 referent raw @2018ffc:231: "If the PI rules no STOP, v0.2 is committed as delivered, as at PROPOSAL-p's v0.2 commit (18b0111)".

A28. R3:124–125, 3a's anchors (v0.3:48, ans3:7) and "the block's §4 wording (:44)" — CONFIRMED (block:44's list equals v0.3:48's).

A29. R3:125, the stage that falls outside both the scope and the list is the G-TIME-F3 re-run, under F-6 (54bbfe5, line 29; LOCK-m-F3 :436, :513–515) — CONFIRMED.
- 54bbfe5 adds results/raw/2026-11-06_ganl-f3_design-to-code_answers.md; its :29 is F-6.
- The lock is unchanged since 1e79955 (`377c5d60…6ce7`); :436 is F-6 and :513–515 its ruling.
- Inventory of the other stages: G-F3 reports first lines by class (F60, lock:505); G-ID-F3 is all sham; the campaign falls under "the rest".

A30. R3:127–128, the v0.3 quotes, and "the first half matches ans3's sentence word for word" — CONFIRMED (identical from "before the unit's VERDICTS entry" through "the campaign's looks report neither;").

A31. R3:130–131, the ans3 and v0.3 quotes, and "in the block's wording" — CONFIRMED (verbatim; block:46 and block:44).

A32. R3:132, "m:271 releases the withheld events there" — CONFIRMED (m:271: "are withheld to the unit's VERDICTS entry or NOT-RUN record").

A33. R3:133, "gains", the struck clause, and the VERDICTS sentence unchanged — CONFIRMED (v0.3:7; v0.2:48 against v0.3:48).

A34. R3:134, ans3's "G-ID-F3 … is unaffected" is not in v0.3, and G-ID-F3 is all sham — CONFIRMED (ans3:7; v0.3:44).

A35. R3:136, 8a, "F-6 (LOCK-m-F3 :436, :510–518) or F60 (:505)" — IMPRECISE.
- The content is right: v0.3:78 lists only §9 PINs F25, F28 and F29, and F60 is at lock:505.
- F-6's span here (:510–518) differs from the :513–515 that 3a and the agent use in the same raw. :510–518 is the dated note, which also covers F-7, F59 and e0b4f2c.

A36. R3:137, no anchor for the G-ANL-F3 answers (54bbfe5) — CONFIRMED (v0.3:5's anchor list).

A37. R3:138, "the agent's item 3b quotes them" — CONFIRMED (R3:64–65). "Code verified … at source" is not checkable.

A38. R3:139, 8b's quote of v0.3:65 and "§5 says the routing block is the record" — CONFIRMED (v0.3:62, :65).
- Flag: "the routing quoted in the commit entry carries them" depends on @@ROUTING@@. ans3:18 proposes "#50's sentence, #48, #49 [confirmed]".

A39. R3:141, the header drops v0.2's path for the pre-read — CONFIRMED (diff :3).

A40. R3:142, the header does not record that v0.2's STOP fired — CONFIRMED (v0.3:3; ans3:7).

A41. R3:143, daca8b0's message has `f3f0`; its RESULTS text and v0.3 have `53f0` — CONFIRMED (the message reads "cdcc8e86...f3f0"; the RESULTS hunk reads "cdcc8e86…53f0"; v0.3:3; the real sha ends 53f0).

A42. R3:144, v0.3 takes up none of v0.2's IMPRECISE notes — CONFIRMED.
- Inventory: the diff touches only :3, :5, :7, :46, :48, :56, :71, :72.
- Examples still unchanged: :7 still credits §4.3 with the counters' VERDICTS path (item 3); :78 still lists m:159 (item 12); :58 still places the six modules in LAZY_F3_MODULES (item 41).

A43. R3:145, how the driver parses §3.1 — CONFIRMED.
- The bullet pattern at D7:571 is anchored on "- **F-"; the lead-in at v0.3:37 begins "**3.1 Forms.**".
- D7:2313–2325 asserts `addendum_m2_problems() == []`, asserts `addendum_m2_text_problems(am2, check_sha=False) == []`, and refuses an extra bullet.

**Placeholders, Part A:**
- @@PIDATE@@, @@RDATE@@, @@STAMP@@, @@ROUTING@@, @@ANS3AT@@ and @@VC@@ were skipped.
- Claims that depend on them: A1, A11, A21 and A38.

**Omissions (no verdict):**
- E3 does not carry two items from v0.3:72's list: "the G-TIME-F3 entry's dated correction was made at daca8b0" and "the class correction is applied to lines.py only with the selected form".

## Code's dispositions (Part A)

- **A8 (IMPRECISE), applied.** The entry now lists each finding's points:
  - 3a's four: the list after "the rest", the two halves' wording, "gains", and ans3's G-ID-F3 line;
  - 8a's two: F-6 and F60, and the anchor for the G-ANL-F3 answers;
  - 8b.
- **A12 (IMPRECISE), applied.** The entry now says that, beside the list, the header, the anchors and §6's items 1 and 2 also change.
- **A35 (IMPRECISE), applied.** 8a's F-6 span in the referent raw is now :513–515, as 3a has it.
- **A5 and A23 (NOT CHECKABLE), reworded.** The report does not state HEAD. The entry and the raw now say HEAD was `2018ffc` before and after the agent ran, by Code's `git log`.
- **A19 and A21 (NOT CHECKABLE)** depend on the commit. The date and the path list are filled at write time.
- **The placeholders** (A1, A11, A38): the routing quote and the dates are filled at write time, from the routing as relayed. As A1's flag asks, the entry also quotes the routing blocks of 2026-11-08 verbatim (v0.3 §6 item 2), from the close lines of `daca8b0` and `de729c4`. ans3 is untracked, and `d215d5b`'s message says it awaits the PI's routing. The entry cites ans3's record commit once it is made; if ans3 is not committed when v0.3 is, Code asks the coordinating session before committing. It was committed at `6b63973`, the coordinating session's record commit of the PI's routing, before this commit, and the entry cites it.
- **The omission, applied.** The entry now carries v0.3 §6 item 2's two items:
  - the G-TIME-F3 entry's dated correction, at `daca8b0`;
  - §1's class correction, left for the build.

## Pass 2 (the corrected passages): its opening, its rule-breach disclosure, and its Part A items (verbatim; local paths scrubbed)

## Second-pass blind values-check: A-m2 v0.3 and smoke-driver drafts (read-only)

**Tallies (82 items):** 61 CONFIRMED, 17 IMPRECISE, 0 FAIL, 4 NOT CHECKABLE.

The findings worth acting on first:
- **#63:** ans3 has never been committed, so the "ans3's commit … from git log" fill has nothing to read.
- **#24 and #66:** the list of STOPs "a stub run does not reach" leaves out the in-run renders and schedules STOPs.
- **#14 and #52:** "the raw … carries the rest" is not true for a line-read error.
- **#30:** round 3's NOTE 12 was applied outside the driver's bytes, but the entry doesn't list it as an exception.

Abbreviations:
- E3 = `S/entry_v03.md`; R3 = the v0.3 referent raw.
- ED = `S/entry_driver.md`; RR = the reviews raw.
- VA and VB = the v0.3 and smoke-driver values-check raws.
- D7 = `S/mut/driver_r7.py`, whose sha256 I re-checked as `c9393a48…4d9b`; ST7 = `S/selftest_r7.txt`.
- stg = `valence_core/mf3/stages.py`.

### Rule breaches during this check
- By mistake, I wrote two temporary check-name lists (`vc2p_a.txt` and `vc2p_b.txt`) in the scratchpad root, outside `am2/` and outside the repository. I deleted them straight away. That breaks the no-file-writes rule.
- I ran `git status --short` three times in the main repository: on `valence_core/ scripts/`, on `LOCK-m-F3.md` and on ans3's path. Under m's finding R4 this can rewrite `.git/index`'s stat cache.
- Otherwise:
  - no git writes and no Python;
  - no self-test or lane run;
  - nothing under `data/` listed, opened, hashed or stat'ed in any tree.
- The git commands that could name paths were scoped to exclude `data/`, or (acde2d8) touched no data path; the round-6 `tree.sha` manifests were not opened.

### Passage 1: E3
1. E3:6–7, the check's scope and "a blind agent": CONFIRMED (v0.3:71).
2. E3:7, HEAD was 2018ffc before and after the run: CONFIRMED by timestamps. 2018ffc is 11-08 23:26:24 -0500. ans3 and v0.3 were written at 23:56:47. The extracted report is dated 00:34. The next commit, d215d5b, is 11-09 02:54:29. The report itself names no commit; its only mention is "unchanged at HEAD".
   - Note: HEAD is now d215d5b, another session's commit. It touches none of the driver, valence_core/mf3, valence_core/m or LOCK-m-F3.md.
3. E3:7–8, the tally 6/2/0/0 with three findings: CONFIRMED (R3:13).
4. E3:8–9, "no item moves…", committed as delivered, dated notes: CONFIRMED (R3:117–122).
5. E3:10–14, 3a's four points: CONFIRMED (R3:46–58).
6. E3:15, 8a: CONFIRMED (v0.3:78 lists only F25/F28/F29; v0.3:5 has no anchor for the G-ANL-F3 answers).
7. E3:16, 8b: CONFIRMED (v0.3:65).
8. E3:26–27, the "What v0.3 changes" intro: CONFIRMED.
   - The diff touches lines 3, 5, 7, 46, 48, 56, 71 and 72: :7 is the list, :46/:48/:56 are its three items, and the others are the header, the anchors and §6 items 1–2.
   - :46 only appends the stopped-smoke sentence; §3.1 and §3.2 are unchanged.
9. E3:43, "Already done … at daca8b0": CONFIRMED (daca8b0's message has "the dated correction on its entry"; v0.3:72).
10. E3:44–45, "Left for the build": CONFIRMED (v0.3:72 verbatim in substance; §1 is "The echo class, corrected", v0.3:23).

### Passage 2: R3
11. R3:5, the How line: CONFIRMED (as #2).
12. R3:136, F-6 at ":436, :513–515" and F60 at ":505": CONFIRMED. LOCK-m-F3.md is unchanged at sha256 `377c5d60…6ce7`; :436 is F-6, :513–515 is its ruling, :505 is F60.

### Passage 5: VA and VB (items 57–64, VA)
57. VA:3–7, the header: CONFIRMED. The verbatim part matches the extracted report, apart from separators.
58. VA:166–169, A8: CONFIRMED.
59. VA:170, A12: CONFIRMED.
60. VA:171, A35: CONFIRMED.
61. VA:172, A5/A23: IMPRECISE (minor). Only the raw says "by Code's `git log`"; E3:7 gives no source.
62. VA:173, A19/A21: NOT CHECKABLE. Note: the date in R3, RR and both VC raws is hard-coded as 2026-11-09, not a placeholder.
63. VA:174, the placeholders: IMPRECISE.
   - `git log --all` has no commit of ans3; it is untracked (`??`), and d215d5b's message calls it "untracked … awaits the PI's routing".
   - E3:49's path list leaves it out.
   - So @@ANS3AT@@ can't be filled from git log unless ans3 is committed before or with this entry. Pass 1's A11 flag is still unresolved.
64. VA:175–177, the omission: CONFIRMED.

## Code's dispositions (pass 2, Part A)

- **#61 (IMPRECISE), applied.** The entry now gives the source, Code's `git log`.
- **#62 (NOT CHECKABLE).** The raws carry the PI date 2026-11-09. If the routing's date differs, the raws and the entry are aligned at write time. The routing is of 2026-11-09.
- **#63 (IMPRECISE), as the placeholders' disposition above now says.** ans3's record commit waited for the PI's routing. It is `6b63973`, and the entry cites it.
- **#2's note.** HEAD has since moved to `d215d5b`, the p session's step-6 build, and then to `6b63973`, the record commit of ans3 (RESULTS.md and ans3 only). Neither touches A-m2, mf3, m or the lock.
- **The agent's rule-breach disclosure.** Nothing to apply.
  - It wrote two temporary lists in the scratchpad root, outside the repository, and deleted them at once.
  - It ran three pathspec-limited `git status --short` runs in the main tree, on `valence_core/` and `scripts/`, on `LOCK-m-F3.md`, and on ans3's path. None touched `data/`, and O2-3 allows a bare `git status`.
