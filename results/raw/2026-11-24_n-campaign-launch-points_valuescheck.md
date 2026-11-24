# n — the N-pod campaign's launch set v1, its points for the seat: the blind values-check, as returned, with every disposition

PI date 2026-11-24. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the drafted texts, at HEAD `e1be6d9`:
- T1, the raw for the seat, `a113c4dc…35a3` (216 lines), committed as
  `results/raw/2026-11-24_n-campaign-launch-points_code-to-design_STOP.md`;
- T2, its entry, `32b53abc…40d1` (128 lines), its five placeholders not to be checked.

**The checker's brief** was a file the checker read itself, as its prompt directed: Code's scratch file
`S/step4b/camp/points/vc_brief.md` (`f067092d…2755`, 127 lines). It:
- named the texts and the sources. In the repository: the files the texts cite, at `e1be6d9`. In Code's scratch, by
  name and sha256: the launch set's files (the launch script, its manifest, the `hashes` file, the plan by its sha256
  and line count only, the pod session's note and the placement script), the launch review's report and Code's
  dispositions, and the two running lists of Code's commands' kinds (the launch set's, and the BUILD's for the
  BUILD's commit). In the sessions' notes folder: the set's note to the coordinating session. In this session's
  transcript: the coordinating session's read of the set and its relay of the PI's answer, and Code's message sending
  the set;
- asked whether T1 carries the set's note's six points and its INTEGRITY readings in full and without change of
  meaning, and which is right where they differ;
- allowed `shasum`, and `jq` on committed JSON and on this session's transcript. It barred any other interpreter
  (`awk` among them), any write, any network, any guard marker in an argv (a grep pattern and the command's own text
  included), and globs over the root, `results/raw/` or a folder of marker-named files;
- barred anything under `data/m[f]3`, any read, listing, size or time of a ckpt or reports file, anything in Code's
  scratch or the notes folder but the named files, and any look for G-TIME-n's two steered cells or any naming of
  their staging folder in an argument;
- asked for a sweep of Code's shell commands from the BUILD entry's final sweep (2026-11-24T04:25:37.015Z, T's UTC
  stamp) to the command that hashed the brief, in four spans with T2's counts, and the kinds after it;
- quoted the list of record v2's items 1–5 verbatim (equal by `diff` to the seat block's check's brief's), and
  required item 3's pathspec and the campaign folder's exclusion on every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq`, the harness's two-space frame
removed (296 lines, sha256 `f94cb0f481a7604e1dc577759c1d911a4a28c19a48fb8bd2fc33cc358bf3f5bc`). It names scratch
files as S/... or L/..., the sessions' notes folder as N and the transcript as T. Its times are T's UTC stamps.

**Totals:** 58 items: 37 CONFIRMED, 15 IMPRECISE, 4 FAIL, 2 NOT CHECKABLE; and 9 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

Each text was edited as a v2 copy of the draft the checker read (S/step4b/camp/points/block_v2.md and entry_v2.md),
by the file tools only, and each edit is replayed by tool in §2. Code checked the lines the fixes cite before
applying them: blk:153–162 and :189–192, drv:6634–6638, and the launch script's check runs by end (its lines
864–899).

**The four FAIL items:**
- **Item 2, the head's line on the PI's word (T1:4–5).** Applied, close to the checker's words: "The push of the
  commit that carries it waits for the PI's word, and the PI then nudges the seat." The run's wait on the PI's word
  stays in the next line.
- **Item 20, "a ruling is a committed raw (CP9, blk:172–206)" (T1:77).** Applied: "a ruling is a committed raw, and
  the resume runs in a fresh sparse copy at its commit (CP8, blk:153–162); the PI's stop cites a committed raw (CP9
  (c), blk:189–192)".
- **Item 51, the launch set's span (T2:54–55).** Applied. The span's head gives 198 commands to the set's sweep 3 and
  19 after it, of which the message that sent the set counted 17, its own count included. It says the values-check
  named the rest. Each kind the item lists is named in the span: the BUILD's running list's reads and its append;
  `wc -c` of three memory notes; `wc -l` of three of the sessions' notes; the recursive `grep -r` over
  `valence_core/` and the driver (observation 8); the glob over `results/raw/`; the sweep-3 draft's checks; the
  second recursive `grep` inside the command moved to the background; the `grep` of the notes for the hash written
  by hand wrong; the `grep` of the post-sweep list; and `wc -l` beside `shasum`.
- **Item 54, this raw's span (T2:87–112).** Applied: 64 commands to the brief's hash; four `git grep`, the fourth
  with its two quoted globs; and every kind the item lists.

**The fifteen IMPRECISE items:**
- **Item 5 (T1:11–12, T2:10–11).** Applied in the checker's words, in both texts.
- **Item 8 (T1:15–16).** Applied, close to the checker's words: "…as the set's note gives them, stated more exactly
  from the set's own files where the note was short (points 1, 3 and 4, and G-VER's readings)…".
  - Its (b), point 3's "where G-READ-n reads them", is restored to T1, marked as Code's reading (step 15, on the
    laptop).
  - Its (e), the note's two routing lines to the coordinating session, needs no place: the PI's answer settled both.
- **Item 11 (T1:21).** Applied in the checker's words.
- **Item 23 (T1:86–93).** Applied. The CP6 line's template now says that the standing pause's kind and the cap's
  `hour_cap_ms` print beside the three fields, and the three lines are those of each run that checks the report
  (observation 4's names mode is apart).
- **Item 25 (T1:97–98).** Applied in the checker's words. LQ2's "at each end" is now "at the ends where it runs".
- **Item 26 (T1:99–101).** Applied in the checker's words.
- **Item 29 (T1:116–119, :123).** Applied in the checker's words.
- **Item 39 (T1:192–196).** Applied: "where the launch would class the stage's own refusal of the package or its
  closure off its pin INTEGRITY (CP12's extension; the launch review's O7)". The stage's refusal names no class
  (drv:6634–6638).
- **Item 42 (T2:8–11).** Applied in the checker's words.
- **Item 44 (T2:26–27).** Applied. The paragraph names each place the raw follows the set's own files: point 1's
  fifth check, point 3's analyzer lines, point 4's two ends, and G-VER's readings in ans22b §1.4's words. It names
  the pod session's note's same sentence, and what the values-check added (point 2's names file, and point 4's crash
  that the copy-in's checks do not catch). Point 3's "where G-READ-n reads them" is back in T1 (item 8), so T2 does
  not name it as left out.
- **Item 47 (T2:32).** Applied in the checker's words.
- **Item 48 (T2:33–35).** Applied in the checker's words.
- **Item 50 (T2:45–53).** Applied: each kind it names is in the span, and `git diff -U0` is of `RESULTS.md` alone.
- **Item 52 (T2:56–84).** Applied:
  - the reads at `098218c` and of `valence_core/m` and the analyzer;
  - memory notes read by `grep`, `sed` and `awk`, and `awk` of the set note's long lines;
  - `jq` for the BUILD window's commands and the review's hand-back;
  - `head`, `tail` and `sed` over the windows' outputs;
  - two background tasks' output files read by `cat`;
  - plain `grep` over the notes folder's notes;
  - the background runs by name: the harness's first run and three mutation-pass runs.
- **Item 53 (T2:85–86).** Applied in the checker's words.

**The two NOT CHECKABLE items** (40 and 58) are Code's reasoning, the questions, and what comes after the check.
Item 58's counts are used: 64 for this raw's span to the brief's hash, and its kinds after the hash in the entry.

**The observations:**
1. **The pod session's note's sentence.** Point 4 now says that it changes nothing the pod session does: the note
   routes a crash to a new launch version, so step 1b does not run after one under v1. LQ4 asks whether the note
   needs a v2. The set stays frozen as sent; any change is a v2 file, on the seat's word.
2. **A crashed resume that wrote only cells the report does not name.** Point 4 states it, and LQ4 asks whether no
   resume may follow a crash, whatever the copy-in's checks show.
3. **The script's crash line.** Point 4 now says it prints where the driver itself ends an invocation as failed
   after G-VER, and that a kill or a restart ends the script itself, the note governing it.
4. **`names.txt`.** Point 2 now names it: the check's names mode, its counts alone printed, and the file copied back
   at a resume and the PI's stop. LQ2 asks about it.
5. **The fresh clone, not shallow.** Point 1 now says so, with the note's box step 4.
6. **G-TIME-n's staging folder.** T1 no longer names it plainly ("its copy-back's folder in the same staging
   folder").
7. **`grep -c` printing 0 and exiting 1.** T2 now says so for every span.
8. **The recursive `grep -r` over `valence_core/` and the driver.** Named in T2's launch-set span, for the seat to
   class.
9. **The two agent ids in an argv.** Named in T2's last span, where the gate's id list is built. The committed texts
   carry neither, and the gate checks that.

**The sweep.** Its counts are T2's: 22, 217 (198 and 19), 3, and 64 to the brief's hash. Its bracketed counts over
316 commands: guard markers 0; Q-F3's folder's plain name 0; G-TIME-n's staging folder 0; the joined form 1 (sweep
1's, declared); the word python in 7 (the six window runs and one printed label).

## 2. The edits, replayed

The edits were made to new versioned copies of the two texts. Each was recovered from this session's transcript by
`jq` and replayed on the draft the checker read, each change's old text found exactly once, by the replay script
`S/step4b/camp/points/edits_check.sh`. The results are byte for byte the revised texts, so nothing else changed
after the check:
- the raw, 15 of 15 edits; the entry, 24 of 24.

They are, in order of time: this check's dispositions; the entry's values-check paragraph and the checker's
departures; the entry's last sweep (its counts and the kinds after the brief); and the entry's closing blank line,
which separates it from the next entry. After the edits, one placeholder was filled by tool in the entry and here:
the count of these edits.

## 3. The report as returned

```text
VALUES-CHECK REPORT: T1 (S/step4b/camp/points/block_src.md) and T2 (S/step4b/camp/points/entry_src.md)

Checked first, by shasum -a 256 and wc -l:
- The brief is f067092d…2755. T1 is a113c4dc…35a3 (216 lines) and T2 is 32b53abc…40d1 (128 lines).
- Every named source is at its stated sha256 and line count: L/camp_v1.sh 939, L/camp_manifest_v1.txt 66, L/camp_hashes_v1.txt 13, L/camp_plan_v1.txt 7,680, L/camp_launch_note_v1.md 302, L/camp_place_v1.sh 136, L/review_report_v1.md 194, L/review_dispositions_v1.md 194, L/departures.md 128, S/step4b/camp/departures.md 232, N/2026-11-24_n-build_camp-launch-set.md 226.
- HEAD is e1be6d9. Every cited repository file is tracked and clean (rev-parse equals hash-object).

ITEMS

1. T1:3–4. Claim: Code, PI date 2026-11-24; for the seat's next sitting, read with fcab1e5's block before the run (n §8 step 14). CONFIRMED. N:3; git log -1 of blk gives fcab1e5; L/camp_launch_note_v1.md:12–13.

2. T1:4–5. Claim: "The PI's word governs only the nudge to the seat." FAIL.
- Evidence: T, user record 2026-11-24T20:20:03.104Z, items 3–4: "No push before the PI's word; after it, the PI nudges the seat." Also: "Nothing goes to the box, and there is no "launch cleared", before the seat's ruling on the eight and the PI's word."
- T1:8–9 itself has the run waiting on the PI's word.
- Put: "The push waits for the PI's word; the PI then nudges the seat."

3. T1:8 (also T2:6). Claim: the BUILD e1be6d9 is on origin. CONFIRMED. `git rev-parse origin/main HEAD` gives e1be6d929bb9… twice. The relay says "HEAD e1be6d9 = origin".

4. T1:8–10 (also T2:6–7). Claim: the run waits for the ruling on the eight and the PI's word, then "launch cleared"; rt23a item 3's quote. CONFIRMED. T 12:13:30.925Z: "Nothing goes to the box before my "launch cleared", which waits on the seat's ruling on the eight and the PI's word". The quote is at results/raw/2026-11-23_first-sitting_pi-routing.md:27–31 (wrapped at :30–31).

5. T1:11–12 and T2:10–11. Claim: "…read it whole, checked it by tool, and holds it frozen as sent." IMPRECISE.
- T 12:13:30.925Z: "launch set v1 received, read whole and checked by tool". It then tells Code: "Hold the set frozen as sent."
- T 20:20:03.104Z, item 4: "launch set v1 stays frozen as sent".
- Put: "The coordinating session read it whole and checked it by tool; at its word the set stays frozen as sent."

6. T1:11–12. Claim: the set went to the coordinating session first, on 2026-11-24; nothing has gone to the box; nothing ran on a model. CONFIRMED. The SendMessage record is at 12:07:38.227Z. Both coordinating-session records agree. N:112–131 lists the six window runs, none on a model.

7. T1:13–14 and T2:12–15. Claim: the question put to the PI, the answer "Commit a raw" relayed verbatim, and the chosen option. CONFIRMED. T 20:20:03.104Z has the question, the verbatim answer and the option text. T2 leaves out the option's "verify and screen it", which is an omission, not an alteration.

8. T1:15–16. Claim: "It carries the six points and the readings, both sides, as the set's note gives them". IMPRECISE. Against N:66–110, T1 carries every point and both sides of the readings, but it differs in these places:
- (a) Point 1. N:67–72 lists "four things". T1:67–71 lists five, adding "the ruling, or the PI's raw, is a file at HEAD's committed bytes". The script makes that check (L/camp_v1.sh:536–543; header :32). T1 is right and the note is short.
- (b) Point 3, first part. T1 drops the note's "where G-READ-n reads them" (N:80; also in L/review_dispositions_v1.md:45, L/camp_launch_note_v1.md:220–221 and L/camp_place_v1.sh:19). The clause is a planning fact, consistent with results/raw/2026-11-23_n-campaign_spec.md:228–230 (G-READ-n is step 15's, on the laptop). Neither text is wrong.
- (b) Point 3, second part. T1 replaces the note's "refuses only files no cell names (n_analyze.py:3165–3205)" with :3161, :3199–3203 and :3167. T1's version is the more exact: the loader also refuses other defects (scripts/n_analyze.py:3162–3166).
- (c) Point 4. This is T2's declared place. T1 is right (L/camp_v1.sh:571; L/review_report_v1.md:69–71, F11).
- (d) G-VER's three readings (N:92–96). T1:175–181 states them in ans22b §1.4's words. It adds the fourth reading §1.4 accepted (Code's reading in G-VER's BUILD entry) and §1.4's correction (ans22b:24). T1 is right.
- (e) The note's two routing lines to the coordinating session (N:75–76 and N:105) are left out. The PI's answer settled both.
- Put: "…as the set's note gives them, stated from the set's own files where the note was short (points 1, 3 and 4, and G-VER's readings), with the texts each rests on…"

9. T1:17. Claim: each point is put to the seat, not ruled; point 2 bears on CP6, the eight's Q2. CONFIRMED. The relay's item 1 uses the same words; blk:321–323.

10. T1:20–27 and :31. Claim: the set's files by name, sha256 and line count; side by side in one folder; four modes. CONFIRMED.
- Every abbreviation in T1 and T2 equals its full hash cut to the first 8 and last 4 characters: 16485a25…58f5, de1f52c1…be71, a853932b…522b, 551eb1bf…a658, 42b3efd0…bb14, 2127906a…9ce7, de0604cf…dc7c, fb36e13f…223c, ba220eab…a7d7, 505f373a…1ae6, ee0345a7…8788.
- The modes are at L/camp_v1.sh:6–16 and :196–203; the folder at L/camp_launch_note_v1.md:22.

11. T1:21. Claim: the script "checks its three siblings by sha256 before anything else". IMPRECISE.
- L/camp_v1.sh:197–250 first refuses bad arguments and resolves the copy, work and run-copy folders. Line :251 makes the work folder, and :253–255 export the environment.
- The sibling check is step 0's first act (:516–523). N:13 and L/camp_launch_note_v1.md:22–23 use the same words.
- Put: "which checks its three siblings by sha256 as its first step, after its argument checks and the new work folder".

12. T1:22–23. Claim: the manifest lists the files the copy must hold, each at e1be6d9's blob. CONFIRMED where checkable.
- The 49 entries whose paths hold no marker each equal `git show e1be6d9:<path> | shasum -a 256`: 49 match, 0 off.
- The 17 marker-named entries were not checked (the argv rule).
- T 12:13:30.925Z reports all 66 OK.

13. T1:23–24. Claim: the hashes file holds the package's digest and its closure's files, byte for byte G-TIME-n's and G-VER's. CONFIRMED. L/camp_hashes_v1.txt:1–13 holds the digest and 12 closure files. It is cmp-equal to `git show e1be6d9:` of results/raw/2026-11-21_n-gtime-v1_hashes.txt, 2026-11-22_n-gver-v2_hashes.txt and 2026-11-22_n-gver-v1_hashes.txt.

14. T1:24–25. Claim: the plan has 7,680 lines, one line a read. CONFIRMED. L/camp_v1.sh:70 and :738; L/camp_launch_note_v1.md:29–31.

15. T1:28–30. Claim: the review report and dispositions; findings F, B and O; the BUILD review raw is the one committed with the BUILD. CONFIRMED. git log -1 of results/raw/2026-11-23_n-campaign-build_review.md gives e1be6d9.

16. T1:33–41. Claim: the cited forms. CONFIRMED.
- blk and spec last changed at fcab1e5.
- LOCK-n.md has the same blob (2f865790…5f8e) at 098218c and e1be6d9.
- RESULTS.md:28–30 uses the same `LOCK-n.md:N` convention.

17. T1:45–59. Claim: the short form and its counts; "None changes the driver". CONFIRMED. The short form matches §1–§3. The set holds launch files only, and L/camp_v1.sh:59 and :532–533 pin the driver to the BUILD's blob. What each point "binds" is Code's framing.

18. T1:63–75. Claim: point 1's copy (named by the coordinating session), its five checks, one script version, and the copy-in by name (B4). CONFIRMED.
- Copy: L/camp_launch_note_v1.md:44–46.
- Checks: L/camp_v1.sh:528, :531, :532–534, :536–543, and :552–564 (exit 4 for a file off its bytes, exit 1 for a missing one).
- Copy-in: :580–613.
- B4: results/raw/2026-11-23_n-campaign-build_review.md:130–132.

19. T1:76–77. Claim: the stage takes each ruling at HEAD's committed bytes and runs HEAD's driver (R:47, :49). CONFIRMED. RESULTS.md:47 and :49, within the BUILD entry's refusals before any read (:42–60).

20. T1:77. Claim: "a ruling is a committed raw (CP9, blk:172–206)". FAIL.
- CP9 (blk:172–205) covers the STOP forms and the PI's stop.
- The ruling's committed raw is CP8's route: blk:153–155 and :160–162 ("the driver refuses a ruling that is not a repository file at HEAD's committed bytes, the route's committed raw").
- The PI's raw is CP9 (c), blk:189–192.
- Put: "a ruling is a committed raw (CP8, blk:153–162), and the PI's stop cites one (CP9 (c), blk:189–192)".

21. T1:82–83. Claim: CP6 as starred (blk:120–121) and its three fields. CONFIRMED. blk:120–121 (wrapped) and :110–111.

22. T1:84–86. Claim: the Python check is camp_v1.sh:299–509, bytes 505f373a…1ae6, tested in two windows. CONFIRMED. `sed -n '299,509p' L/camp_v1.sh | shasum -a 256` gives 505f373a…1ae6, and the heredoc extracted by pattern gives the same. L/camp_launch_note_v1.md:297–300. "Code does not know that the box has jq" is NOT CHECKABLE.

23. T1:86–93. Claim: "it prints three lines and nothing else of the report". IMPRECISE.
- The three line forms are right: L/camp_v1.sh:396–400, :505–508, :407–408.
- But the CP6 line also prints two more fields of the report: the cap's hour_cap_ms ("… of …") and each standing pause's kind (:398–400). T1's own template shows both.
- Put: "it prints three lines and nothing else of the report: CP6's three fields (with the cap's hour_cap_ms and the standing pause's kind beside them), counts, and each check's verdict".

24. T1:95–96. Claim: an exception gives one line; the counts and verdicts are O3(2); none is a field or a margin. CONFIRMED.
- Exception line: L/camp_v1.sh:501–504.
- O3(2): L/review_report_v1.md:174.
- Not report fields: N:76–77.
- No margin: none of the printed forms holds one (:396–408, :506–507), and the check holds the barred keys absent (:312–314, :375).

25. T1:97–98. Claim: "The check runs after each invocation…" IMPRECISE.
- After the stage it runs only at COMPLETE, PAUSE, CAP, the start's G-VER STOP and the PI's stop (L/camp_v1.sh:865–886).
- It does not run after a resume's G-VER STOP (:877–881), a refusal or a failure (:887–899). L/camp_launch_note_v1.md:193–194 says so.
- The runs on the copied-in report, the second CP6 line and the run in `names` are right (:605–606, :628; note :186–188).
- LQ2's "at each end" (T1:204) has the same reach.
- Put: "The check runs after an invocation that ends COMPLETE, PAUSE, CAP, at the start's G-VER STOP or at the PI's stop (not after a resume's G-VER STOP, a refusal or a failure); …"

26. T1:99–101. Claim: the two counts and their uses, and "At a resume, the copied-in report's file is among the files copied back." IMPRECISE (the last sentence only).
- The counts and their uses are right: :432, :434, :498, :614, :863, :870.
- The file copied back is the counts file prior.txt (note :195–196). The copied-in report and its work copy prior_report.json (:606) stay on the box (note :199).
- Put: "At a resume, that work file for the copied-in report (prior.txt) is among the files copied back."

27. T1:102–103. Claim: n:130's quote, items 2 and 5, CP6 at blk:103–124. CONFIRMED. PROPOSAL-n-bk-reconciliation-v0_2.md:130 (exact); blk:103–123 and :118.

28. T1:108–115. Claim: point 3's close list, the copy-back by that list into the campaign-v1 staging folder checked by shasum -c, the arrays kept there, the JSONs-only placement and the one close commit. CONFIRMED. L/camp_v1.sh:14–16 and :621–636; L/camp_launch_note_v1.md:209–239; L/camp_place_v1.sh:103–123.

29. T1:116–119 and :123. Claim: F10; ~4.9–5.0 GB (LOCK-n.md:92–93); after B8; spec:192's quote; a second copy spared; "the repository's ignored data/n/ckpt/campaign/". IMPRECISE (the folder's description only).
- Everything else is confirmed: L/review_report_v1.md:64–67; LOCK-n.md:92–93; the BUILD review raw :144–148; spec:192; L/review_dispositions_v1.md:44–48.
- The BUILD's .gitignore ignores the folder's arrays but admits its N*.json cells (`git show e1be6d9:.gitignore`, lines 363–365).
- Put: "into the repository's data/n/ckpt/campaign/, where the BUILD's .gitignore ignores the arrays". At :123, put "into the repository's campaign root as well, ignored there".

30. T1:120–122. Claim: CP10 (spec:186–193), CP11 (blk:207–231), and anl:3161, :3199–3203, :3167. CONFIRMED. scripts/n_analyze.py:3161 (`load_campaign(cdir…)`), :3166–3167 ("an absent array is no refusal") and :3199–3203.

31. T1:127–131. Claim: a crash leaves the records; the runner replays them (runner:12–15); after a crash at the start the copy-in ends FAIL "no report"; after a crash in a resume it ends INTEGRITY. CONFIRMED.
- valence_core/n/runner.py:12–15; :14 says "an invocation that ended before its report was written".
- L/camp_v1.sh:571 (exit 1) and :605–611 (exit 4).
- F11: L/review_report_v1.md:69–71.

32. T1:133–136. Claim: the script's line and drv:6767's quote; the note's kill paragraph. CONFIRMED. L/camp_v1.sh:895; scripts/n_sessions.py:6767; L/camp_launch_note_v1.md:182 and :201–205.

33. T1:137–139. Claim: CP12 (blk:232–257) and its quote; A-n3:60's quote; F11. CONFIRMED. blk:235 and :245–246; ADDENDUM-n3-capture-convention-reward-gate-and-interval-v0_1.md:60.

34. T1:145–155. Claim: point 5's check in G-VER v2's form; a restart stops everything; the script does not check for a restart; the pod pin refuses another pod before any read (exit 1); CP13 and Q7; CLAUDE.md's quote. CONFIRMED.
- Check and stop: L/camp_launch_note_v1.md:50–57; results/raw/2026-11-22_n-gver-v2_run.txt:42–58.
- The script has no restart check; it only requires RUNPOD_POD_ID (:671).
- Pod pin: scripts/n_sessions.py:6571–6575 and RESULTS.md:42–45.
- blk:258–279 and :348–351; CLAUDE.md "Both PASS before anything runs."

35. T1:160–166. Claim: point 6, the excerpt's form and count. CONFIRMED.
- L/camp_v1.sh:132, :764–767 and :447–455.
- scripts/n_sessions.py:6449 and :6777.
- L/camp_launch_note_v1.md:143–144 and :158–159.
- ans23b:27 (exact quote); L/review_report_v1.md:178.

36. T1:171–173. Claim: the last line names each end; the exits; INTEGRITY 4; every other refusal a FAIL, verbatim, no retry. CONFIRMED. L/camp_v1.sh:930–939, :43–50 and :152; L/camp_launch_note_v1.md:155–180. The quoted words are the launch's; ans22b:24 says "stop, touch nothing, escalate".

37. T1:175–181. Claim: ans22b §1.4's accepted readings and its correction, all carried; CP12's extension is before the seat as Q6. CONFIRMED. ans22b:24; L/camp_v1.sh:154–166, :188 and :555–561; blk:241–245 and :345–347.

38. T1:182–191. Claim: the campaign's five readings on the safer side. CONFIRMED.
- (1) L/camp_v1.sh:585–589 and :593–602.
- (2) :609–610.
- (3) :188 and :924–925.
- (4) :180–185 (F1 BUG, L/review_report_v1.md:10–18).
- (5) :169–173 (F2, :20–29). The G-VEC texts are scripts/n_sessions.py:2851–2892, reached through the lock inputs at :6613 before the directions at :6618.

39. T1:192–196. Claim: the two readings that go the other way. IMPRECISE (one clause).
- The G-VEC parse FAIL is right: scripts/n_sessions.py:2866 checks the bytes, then :2868–2875 raises a text no INTEGRITY pattern holds (dispositions :24).
- The step-3 hashes FAIL is right: L/camp_v1.sh:649–654, :667–668, :916. Both stop "before any load".
- But "the stage would class … INTEGRITY" is not quite so: the stage's refusal names no class (scripts/n_sessions.py:6637–6638). The launch classes it (L/camp_v1.sh:179) under CP12's extension (blk:243–245).
- Put: "where the launch would class the stage's refusal of the package or its closure INTEGRITY (CP12's extension; the launch review's O7)".

40. T1:78–79, :104–105, :123–124, :140–142, :156–157, :167, and LQ1–LQ8 (:200–216). The "another answer" lines and the questions. NOT CHECKABLE. Their facts are covered in items 18–39.

41. T2:1–4. Claim: the entry's head and the block's path. CONFIRMED. The path matches the brief.

42. T2:8–11. Claim: the note of 226 lines (ba220eab…a7d7) and its parts, ending "…and the blind launch review's dispositions". IMPRECISE. The set also holds the review's report (N:151; T1:28). Put: "…and the blind launch review's report with Code's dispositions of it." For "holds it frozen", see item 5.

43. T2:16–24. Claim: what the raw holds. CONFIRMED against T1.

44. T2:26–27. Claim: point 4's two ends, and the note's sentence "so step 1b stops INTEGRITY". IMPRECISE as the only declared difference.
- The quote is at N:86, and T1's ends are right (item 31).
- T1 also differs from the note at point 1, point 3 and G-VER's readings (item 8).
- The pod session's note in the frozen set carries the same sentence (L/camp_launch_note_v1.md:204–205).
- Put, after the sentence: "T1 also states point 1's fifth check (the ruling or raw at HEAD's committed bytes, camp_v1.sh:536–543), which the note's four left out; leaves out point 3's "where G-READ-n reads them"; and gives G-VER's readings in ans22b §1.4's words, with the fourth it accepted and its correction. The pod session's note carries the set's note's sentence (camp_launch_note_v1.md:204–205)."

45. T2:29–30. Claim: the review counts. CONFIRMED. BUG F1 and F5; RISK F2, F3 and F6–F9; NIT F4 and F10–F14; mutants M1–M15; box risks B1–B9; observations O1–O7.

46. T2:31. Claim: the harness, 787 of 787, with a stand-in python "(bash, git and jq)". CONFIRMED. N:116–117. The parenthetical comes from L/camp_launch_note_v1.md:263–264, not from the set's note.

47. T2:32. Claim: "the driver's 29 real outputs". IMPRECISE. N:118 says "29 own outputs (the first window's generator)", and L/camp_launch_note_v1.md:275 says "29 cases over doubles". The dispositions' F8 (:40) does say "real". Put: "the replay of the driver's 29 own outputs (the first window's generator, over doubles) through the script with the real pins, 155 of 155".

48. T2:33–35. Claim: the mutation pass, and "…52 survivors and no defect of the script, met by 76 checks added to the harness". IMPRECISE. The figures 177, 172 and five are right (N:120–121). But N:122–124 has 47 of the 52 killed by the 76 checks and 5 declared equivalent. Put: "Its first run left 52 survivors and no defect of the script: 47 killed by 76 checks added to the harness, and the five declared equivalent."

49. T2:36–40. Claim: placement 49 of 49 and 14 of 14; the six window runs; nothing on a model. CONFIRMED. N:125–131 and :181–186.

50. T2:45–53. Claim: span 1, 22 commands, and their kinds. IMPRECISE.
- The count is confirmed: 22 commands, 04:25:58.579Z to 04:32:30.423Z.
- Not named: at 04:25:58Z and 04:26:36Z, checks of the BUILD departures draft and of the entry with four sources (placeholders by grep -c and grep -n -o, widths, wc -l, head -c and tail -c into od -c, and a cd into scratch).
- Not named: at 04:29:42Z, a cd into the sessions' notes folder that stayed for the next call, and a printf append of the pending departures line.
- At 04:32:30Z, git diff -U0 covered RESULTS.md alone; --numstat covered three paths.
- Put these kinds in the list.

51. T2:54–55. Claim: span 2, 217 commands, "each kind in the set's departures file … and in the message that sent the set". FAIL (the second claim).
- The count is confirmed: 198 commands up to sweep 3 at 11:57:53.165Z (sweep 1 at 05:32:01Z is the 81st, sweep 2 at 05:57:40Z the 115th), then 19. The message counts 17 "this count included"; 12:06:46Z and 12:07:13Z come after it.
- In neither text:
  - 04:34:23Z: tail -n, wc -l and shasum of the BUILD's departures list. 04:34:53Z: its append by cat >>. Both are declared in S/step4b/camp/departures.md:231–232, not in the set's file.
  - 04:35:32Z: wc -c of three memory notes.
  - 04:39:44Z: wc -l of three notes-folder notes.
  - 05:29:19Z: a recursive /usr/bin/grep -r over valence_core/ and the driver, without item 3's form. It read that folder's four marker-named files by process, with no marker in argv; nothing there is under ckpt or reports.
  - 05:35:12Z: a shell glob over results/raw/ by a G-TIME-n name prefix (25 tracked names, 0 marker-named). L/departures.md names the grep, not the glob.
  - 11:59:53Z: the sweep-3 draft's checks (placeholders by grep -c, widths by awk, its ending).
  - 12:01:58Z: a second recursive grep, over the whole sessions' notes folder, inside the command the tool moved to the background. Both texts name only "one recursive grep of scratch".
  - 12:04:18Z: a grep of the notes folder's notes for the hash after the cd. The cd is named; the grep is not.
  - 12:06:46Z: grep -n -o of the post-sweep list for python.
  - 12:07:13Z: wc -l beside shasum of the set note and eight set files.

52. T2:56–84. Claim: span 2's summary. IMPRECISE. Besides item 51:
- "git show … at e1be6d9" misses one read at 098218c (RESULTS.md:7836–7850, 04:38:55Z), the analyzer (06:15:10Z) and valence_core/m (05:29:22Z).
- Reads of memory notes by grep, sed and awk (04:35:00Z–04:39:31Z, 09:27:45Z) and awk of the note's long lines (11:56:35Z) are in L/departures.md but not in T2.
- jq over the transcript also ran for the BUILD window's commands (04:34:32Z, 04:34:40Z) and the review's hand-back (06:14:29Z), not only "for the sweeps".
- The windows' outputs were also read with head, tail and sed.
- Two background tasks' output files in the session's temporary folder were read by cat (09:09:06Z, 11:55:00Z).
- Plain grep also read the notes folder (09:17:46Z, grep -l over its notes by a glob); L/departures.md:101 says "and the notes folder".
- "two of them in the background": the harness's first run and three mutation-pass runs went to the background. That fits only if "two" means two of the four kinds.

53. T2:85–86. Claim: span 3, 3 commands, and their kinds. IMPRECISE. The count is confirmed. At 12:07:52Z Code also printed a second memory note whole by cat. Put: "…the memory index, and cat of a second memory note; …".

54. T2:87–112. Claim: span 4, this raw. FAIL.
- @DCOUNT@ is 64: 20:20:56.415Z to the brief's hash at 20:35:57.706Z, inclusive.
- "three git grep … with item 3's pathspec" is wrong: there were four. The fourth (20:25:28Z) is a git grep -n -w over two quoted pathspec globs under results/raw/ (G-VER v2's and G-TIME-n's raws: 32 tracked names, 0 marker-named).
- Kinds not named:
  - 20:26:25Z: name-only ls of two more scratch folders, filtered by grep.
  - 20:29:56Z: plain cat (not cat -n) of the set's departures file.
  - 20:30:18Z and 20:30:26Z: jq lists of commands from 03:40Z, before the final sweep, numbered by awk.
  - 20:31:15Z: the set message by jq into grep, and a python grep of the sweep file.
  - 20:31:21Z: sed -n of that file.
  - 20:32:11Z: wc -l and grep -n of three earlier check briefs.
  - 20:33:58Z: git ls-files of results/raw/ into a bracketed marker count, and width checks of the two drafts.
  - 20:34:02Z and 20:34:08Z: a cd into scratch, widths, and sed -n of the block draft.
  - 20:34:27Z: the abbreviation check (shasum, grep -h -o in fill_v1.sh, cut, sort -u into scratch, comm -23) and a width re-check.
  - 20:34:54Z: wc -l beside shasum of 13 files.
  - 20:35:00Z: line-range hashes of the launch script, grep -n of fill_v1.sh, and sed -n of its lines.
  - 20:35:57Z: diff of the earlier seat brief's lines 112–116 with this brief's last five lines, then wc -l and shasum of this brief.
- The rest of the list is confirmed:
  - The two root globs (20:27:59Z): 1 match, 0 marker-named.
  - The ls of results/raw/ (20:21:01Z): 15 names dated 2026-11-23/24, 0 marker-named; 41 raws in results/raw/ are marker-named.
  - The grep -c that printed 0 and exited 1 (20:29:29Z).
- Put: "four git grep: three over the tree with item 3's pathspec and the campaign folder's exclusion, one -w over two quoted pathspec globs under results/raw/", and add the kinds above.

55. T2:113–114. Claim: the file tools in every span. CONFIRMED. Since 04:25:37.015Z the file tools wrote and edited only in scratch, the notes folder and memory. The 12 repository reads include none under ckpt or reports.

56. T2:115–117. Claim: the bracketed counts, the one joined argv, and Python only in the six runs. CONFIRMED. Over all 316 commands up to 20:37:17Z:
- guard markers [0]
- Q-F3's folder's plain name [0]
- G-TIME-n's staging folder's name [0]
- the joined form [1], at 05:32:01Z (sweep 1)
- "python" named in [7]: the six window runs and one printed label (12:06:36Z)

57. T2:118–120. Claim: the reviewer's departures, as its report states them. CONFIRMED. L/review_report_v1.md:189–194. "(item 1 permits it)" is the dispositions' gloss (:190).

58. T2:122–128 and the placeholders. The gate, the commit by path, the screen count, "Not pushed" and the run's wait are NOT CHECKABLE (they come later). The placeholder values:
- @DCOUNT@ = 64.
- @TOTAL@ = 306 up to the brief's hash (22 + 217 + 3 + 64); 316 with the commands after it so far.
- @FINAL@: 10 Bash commands from 20:36:09Z to 20:37:17Z, as of T's last record at 20:38:06Z:
  - wc -l, sed -n and grep -n -E of gate v16 with ids masked, cut, and diff of gates v15 and v16, ids masked (20:36:09Z, 20:36:12Z, 20:36:16Z).
  - test ! -e, cp of gate v16 to v17, and cmp (20:36:26Z).
  - bash -n of v17, diff of v16 and v17 with ids masked, a loop of grep -c -F per agent id over v17 (two agent ids in argv, printed by their first three characters), and shasum of v17 (20:36:41Z).
  - sed -E of the seat kit's manifest with paths masked, cat of its paths file, and sed -n of the BUILD window note in the notes folder (20:36:51Z).
  - git log -1 --format=%B of fcab1e5 and e1be6d9 into wc -l, tail -n 2 and cut: commit bodies, beyond item 1's ids, subjects and times. Also sed -E of check_msg.sh, masked (20:36:59Z).
  - wc -l, grep -n and sed -n of the committed BUILD values-check raw (20:37:04Z).
  - wc -l and sed -E of the BUILD's edits-replay and commit-build scripts in scratch (20:37:10Z, 20:37:17Z).
  - File tools since then: Reads, Writes and Edits in scratch, and one memory-note Edit.

TOTALS: CONFIRMED 37, IMPRECISE 15, FAIL 4, NOT CHECKABLE 2. 58 items.

OBSERVATIONS

1. The pod session's note in the frozen set (L/camp_launch_note_v1.md:201–205) says a crash at the start "would stop INTEGRITY". The script ends that case FAIL "no report" (L/camp_v1.sh:571). The pod session reads that note, not T1. The seat may need to say whether the raw's correction is enough or the note needs a v2.

2. Point 4's INTEGRITY after a crash in a resume holds only if a cell the copied-in report names has moved.
- If the crashed resume wrote only into cells the report does not name, the copy-in's checks pass, because only named files are copied and checked (L/camp_v1.sh:584–617). A new `resume` with the same ruling would then run from the copied-in report.
- A question for the seat: must no resume follow a crash, whatever the checks show?

3. The script's crash line (L/camp_v1.sh:895) prints only at the driver's own "FAILED after G-VER" end (:852, :892–895). A kill or a container restart, which are point 4's crashes, never reaches it; the note's kill paragraph governs those. T1:133 is right as worded, but it may read as if it covers a kill.

4. For LQ2: in names mode the Python check writes every cell and array name the report names to names.txt (L/camp_v1.sh:575), and that file is copied back at a resume (note :195). It holds no margin, but it is more of the report than the three fields.

5. Point 1's ancestor check needs each resume copy to be a fresh, non-shallow clone with the history back to the BUILD, not a worktree (L/camp_launch_note_v1.md:71–73). T1 does not say so; the seat may want it beside LQ1.

6. T1:112 names G-TIME-n's staging folder in plain text, as the launch note does (:226). Once committed, any search for that string must keep its pattern bracketed.

7. A grep -c that prints 0 and exits 1 with no effect is declared only for span 4 (T2:110). It also happens in spans 1–2, for example at 04:28:30Z, 04:30:19Z, 04:34:53Z, 05:06:46Z, 05:36:39Z and 05:58:03Z.

8. The 05:29:19Z recursive grep read four marker-named files by process with no marker in argv. Whether the guard rule reaches it is for the seat to class; T2 should name it either way.

9. Code's 20:36:41Z command put two agent ids in argv. No rule bars that, but the committed texts must carry neither; that is what T2:122–123's gate checks.

DEPARTURES (mine)

1. One git grep whose pathspec named three files plus a quoted glob over the repository root, 'ADDENDUM-n*' (3 tracked matches, none marker-named), instead of named files or item 3's form.

2. One `git check-ignore --no-index -v --stdin` of two hypothetical names under data/n/ckpt/campaign/ (strings on stdin; nothing listed, sized, timed or read). Its output, and a grep of `git show e1be6d9:.gitignore`, printed ckpt path names with their digit runs unmasked.

3. Not departures, for the record:
- I viewed Code's command texts in every span, masked, and the three records the brief names in full.
- I read T's last timestamp with tail into jq.
- I ran no interpreter but shasum and jq, wrote nothing and used no network.
- No marker or barred folder name appeared in any argv.
- Nothing under data/m[f]3, ckpt or reports was read or listed.
- In S and N I read only the named files.
```
