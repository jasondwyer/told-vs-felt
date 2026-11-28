# The coordinating session's notes on the PI's routing of three seat raws (raws (D), (E) and (C), PI date 2026-11-27): the blind values-check, as returned, with every disposition

2026-11-27. Code (the coordinating session).

**What was checked.** One blind pass by a subagent over these drafts:
- the entry's draft (sha256 `d10c0e5a…7f2c`, 191 lines);
- the coordinating session's two close lines, on `e114b3a`'s entry (`1c241337…0be8`, 13 lines) and on `5ceb8dd`'s entry (`9c67354c…682f`, 11 lines);
- the other sessions' three close lines, placed verbatim: n-build's on the entry `G-READ-n` (`f1a742df…ffca`, 24 lines), f3-build's on the Q-F3 campaign entry (`0cb36dbd…1c28`, 56 lines) and the dpo VERDICTS session's on its VERDICTS entry (`e5727365…574b`, 52 lines);
- f3-build's values-check raw on its close line (`e0e1ed9e…b610`, 295 lines), for its identity and the public-repository screens only;
- the routing raw (`3e569ab7…6b66`, 52 lines);
- the commit message's draft (`61cea58b…dc77`, 3 lines);
- their placement in a draft of the new `RESULTS.md` (`50e24bef…1544`, 42,403 lines).

No run was live on the laptop. The check was read-only and ran no Python.

**The checker's brief** was a file in the coordinating session's scratch folder, named in its Agent call by path (sha256 `68355db4…9fc5`, 144 lines). It is not committed, because it names the local roots in full. It:
- named the sources:
  - the three seat raws, each to be read whole;
  - the PI's message in the coordinating session's transcript, with its extraction and the block;
  - the relays (five first sends by name that failed, and the same five texts by session id), with their files, and the later messages to f3-build, n-build and the dpo session;
  - the sessions' messages with their close lines, and f3-build's two questions;
  - the coordinating session's own checks in its transcript;
  - the repository at `7ab1cf6`: the five entries the close lines join, the instruct session's close line whose form the sessions' lines follow, `git show` of `5ceb8dd` and `e114b3a` for the two lines that promise a full hash, and the list of record v2 and the pinned files as a claim needs them;
- told the checker that the transcript's compaction summary, and a later tool result quoting another session's transcript, are not sources;
- quoted the list of record v2's items 1–5 verbatim, from `2026-11-10_list-of-record-v2_design-to-code_answers.md` (its lines 18–22, equal by `cmp` to the last brief's);
- barred:
  - any interpreter but `shasum` and `jq`, any write and any network;
  - a whole-tree `git status`;
  - anything under `data/*/ckpt`, `data/*/reports` or the campaign folder, and the Q-F3 campaign's raw;
  - the memory folder, other sessions' folders and the side-session notes folder;
  - the guard markers (the p unit's name among them, written bracketed) and the campaign folder's plain name in any command text, and any path holding a marker word passed as an argument (such paths go on stdin only);
  - the forms the seat ruled on 2026-11-27: no `ls -1t` or time-ordered or long listing; the volume's host name and the email domain by class only; a transcript search printing the record a finding needs and no other;
- set item 3's pathspec, with the campaign folder's and the gate artifacts' exclusions, on every git command over the tree or a range;
- barred from the report local paths, session ids, the user's name, email and the email domain, any address or port, the network volume's server host name or any fragment of it, and clock times.

The Agent call's prompt restated the brief's main bars.

**The report** is in §3, extracted verbatim by `jq` from the subagent's one hand-back (325 lines as `jq -r` wrote them, the last ended by the newline `jq` adds; sha256 `75b36c34…bc59`), byte for byte, with no mask. It is equal by `cmp` to the hand-back as the coordinating session's transcript records it, with the harness's two-space indent stripped.
- It names no local root. Its `<repo>`, `<own>` and `<transcript>` are the repository, the coordinating session's scratch and its transcript.
- Its 17 Read calls agree with its transcript, by a count of the tool names (89 `Bash` and 17 `Read`).

**Totals:** 52 items (39 CONFIRMED, 7 IMPRECISE, 1 FAIL, 5 NOT CHECKABLE) and 6 observations.

## 1. Dispositions

- **Items 12 and 13** (IMPRECISE): applied in the checker's words: "item 4 deferred", in the entry's head and in the message.
- **Item 15** (IMPRECISE): applied: "five places", and a fifth bullet in the checker's words on the two dropped clauses, raw (E) item 4's "citing this raw by path and sha256" and raw (C) item 3's "no re-analysis". The routing raw's "the differences are stated in the notes' entry" then holds.
- **Item 17** (IMPRECISE): applied in the checker's words: raw (E) item 7's "Code commits this raw by path" (the block's "Code commits raw (E) by path").
- **Item 20** (FAIL): a working file's. `sent_nbuild.txt` is re-extracted by the relay's first words: 28 lines, its two blocks equal by `cmp` to the block's lines 7–15 and 30 again. No committed text changes.
- **Item 22** (IMPRECISE): applied in the checker's words, and a correction sent to n-analyzer after the check: raw (D) §5 item 4 gives the n-analyzer session §2 items 3 and 6 to carry into the VERDICTS entry, and ledger (91) is the seat's own record (raw (D) §2 item 5; routing item 3, "[record]"). The entry's bullet records the relay as it was and the correction.
- **Item 26** (IMPRECISE): applied: "stood in argvs and outputs in that window, and in argvs since the end".
- **Item 46** (IMPRECISE): applied in the routing raw's head, in the checker's words: "placed on 2026-11-26, unchanged and not yet routed, and routed here in section B ("re-routed unchanged from the 11-26 block")".
- **Items 3, 32, 34 and 45** (NOT CHECKABLE): the commit's own checks and what follows it. The gate and the verify meet the first and third; the rest are owed after the commit.
- **Item 40** (NOT CHECKABLE): f3-build's own record, declared in its line for the seat to class.
- **Observation 1:** applied. The two older close lines, R:23937 and R:24560 at `7ab1cf6`, were checked by `git blame -l` (last changed at `dc1ffe1` and `79d462b`) and by a fixed-string count of each full hash in RESULTS.md (0 each); the entry names both commits in full beside `5ceb8dd` and `e114b3a`.
- **Observation 2:** noted. The entry's routing bullet states item 15's dropped clause, and the dpo session's line quotes section B's heading as the PI's words.
- **Observation 3:** passed to the seat in the entry's observations. Raw (E) is committed unchanged.
- **Observation 4:** passed to the seat in the entry, beside the dpo session's observation (a). Raw (C) is committed unchanged.
- **Observation 5:** noted, not raised: a clock time in n-build's entry at `7ab1cf6`, outside this commit's texts, is Code's own stamp.
- **Observation 6:** held. The four forms it names in the coordinating session's own commands go to the held sweep (item 18), which declares them with the rest of that span.
- **The checker's own departures,** as its report states them: for the seat to class.

## 2. Edits after the check

- The edits are the dispositions above, the rewraps of the bullets they changed, and the fills of the two placeholders: `@VC@` with the values-check bullet, and `@VCMSG@` in the message.
- The edits were checked by tool, by `diff` of each checked draft against its final text. Each hunk is a disposition above, a rewrap, or a fill.
- No second full pass was made.

## 3. The report as returned

# Blind values-check: the coordinating session's notes on the PI's routing of raws (D), (E) and (C), after `7ab1cf6`

Brief read whole (144 lines). Its sha256 `68355db4…9fc5` matches. Every text checked is in `<own>/s2026-11-27/sitting-d-e-c/`, cited by file name and line. "R:N" means RESULTS.md at HEAD `7ab1cf6`. "The block" is the PI's routing block: `pi_block.txt`, lines 4–39 of the PI's routing record in `<transcript>` (PI date 2026-11-27).

## Items

1. **Claim.** `checked_entry.md`:9–21 and `checked_routing_raw.md`:3 give the raws as (D) `6b5be7a3…e420`, 23,716 bytes, 81 lines; (E) `69522ee8…a441`, 14,427, 58; (C) `14da65a9…0593`, 38,962, 111.
   - **CONFIRMED.**
   - **Evidence.** `shasum -a 256`, `wc -c` and `wc -l` on each raw in `<repo>/results/raw` printed these figures. The abbreviations were checked by `cut -c1-8`/`-c61-64`. In `pi_block.txt`, `grep -c -F` finds each file name followed by its full sha256 once, and each byte figure once.

2. **Claim.** `checked_entry.md`:24–26: "All three were placed untracked over the bridge. The coordinating session re-hashed each equal … found them untracked with HEAD and origin at `7ab1cf6`, and read each whole."
   - **CONFIRMED.**
   - **Evidence.**
     - Each raw's header says "Placed untracked over the bridge".
     - `git status --porcelain -- results/raw` lists all three as `??`. `git rev-parse HEAD origin/main` gives 7ab1cf6… twice.
     - In `<transcript>`, the coordinating session's first check after the PI's record printed HEAD and origin/main at 7ab1cf6, the three files untracked, and each sha256, byte count and line count equal.
     - Its three Read calls carry `file_path` only. They returned 82, 59 and 112 numbered lines: each file's lines plus the tool's empty last line.

3. **Claim.** `checked_entry.md`:26, "Each is re-hashed equal before this commit and committed here by path, unchanged"; and each session close line's "That commit is the raw's first commit".
   - **NOT CHECKABLE** (commit time).
   - **Evidence.** All three raws are equal now. `git log --all --format=%h -- <path>` prints nothing for any of the five new paths. The routing raw and f3-build's values-check raw are not yet placed.

4. **Claim.** `checked_entry.md`:30–33, the run of record accepted, with every figure recounting equal "by one scratch script of the seat's outside the repository".
   - **CONFIRMED.**
   - **Evidence.** Raw (D)'s §0 first bullet, §1 items 2–5 and its header. `378f9972…f519` matches raw (D)'s full hash by `cut`.

5. **Claim.** `checked_entry.md`:34–40, valence +1's FAIL.
   - **CONFIRMED.**
   - **Evidence.**
     - Raw (D) §0, §2 items 1, 3 and 4; raw (D)'s routing block (§6) item 2 cites "(§2 items 1–4, 7)".
     - Anchors opened: probe.py:82 reads `… bm >= AUC_BAR and bm > comp_max`, and :162 "a comparator at the axis's level fails it".
     - A-n1:58 is "6.4 PASS iff … above the largest of the comparator's 24 band medians". n:136 ends "… *concluded, not answered* (§0.6)".
     - anl:813–818 is `label(…)`, and :982 opens `GREAD_SECTION5`.

6. **Claim.** `checked_entry.md`:41–45, ledger (91) and Appendix D.
   - **CONFIRMED.**
   - **Evidence.** Raw (D) §2 items 5 and 6 (the ledger's text, the fix, "N-pod's rule stands as locked, and its FAIL as computed"); block items 3 and 4.

7. **Claim.** `checked_entry.md`:46–49, VERDICTS.
   - **CONFIRMED.**
   - **Evidence.** Raw (D) §5 items 1–2 and block item 5 "[go]". `shasum` of `scripts/n_analyze.py` gives `735da934…a7a8`.

8. **Claim.** `checked_entry.md`:50–55, observation 1 and the box, including the quotation "[PI's word on the folders: ___; the volume: keep]".
   - **CONFIRMED.**
   - **Evidence.** Raw (D) §3 and §5 item 3; block item 7, verbatim.

9. **Claim.** `checked_entry.md`:56–61, the departures.
   - **CONFIRMED.**
   - **Evidence.** Raw (D) §0 fourth bullet and §4: the two departures, inert with their form notes; the launch reviewer's "none"; the values-checker's six; the line for the next brief.

10. **Claim.** `checked_entry.md`:63–82, what raw (E) rules.
    - **CONFIRMED.**
    - **Evidence.** Raw (E) §1 item 1's form note, item 5's form note, item 3's departures, class, fix and disclosure, and item 4; §2's class and its notes (a) and (b); §3; §4.

11. **Claim.** `checked_entry.md`:84–102, what raw (C) rules.
    - **CONFIRMED.**
    - **Evidence.**
      - §1: Δ_c = 19/40 = +0.4750; E = 5/32 from 11/32; map 0 40/40, map 1 38/40; 3,241/2^80 ≈ 2.68 × 10^-21.
      - §2: .975, then 67/80, 70/80, 76/80, 61/80, 71/80, which are .84, .875, .95, .76, .89.
      - §1 and §3.1: two sham first reads tied at .500, the first such ties in p's campaigns; PASS does not turn on them.
      - §3's totals, §4 item 1 ("the words do not fit"), §5's six disclosures, §6.

12. **Claim.** `checked_entry.md`:2–3: "… `5ceb8dd`'s departures classed (item 3 a strike in form, the rest inert)".
    - **IMPRECISE.**
    - **Evidence.** Raw (E) §1 item 4 is "owed after VERDICTS … not ruled here", and block item 11 is "[defer]". The entry's own :76 has "after VERDICTS, as owed". Item 4 is deferred, not inert.
    - **Fix.** "(item 3 a strike in form, item 4 deferred, the rest inert)".

13. **Claim.** `checked_msg_src.txt`:1: "item 3 a strike in form, nothing rewritten; the rest inert."
    - **IMPRECISE**, as in item 12.
    - **Fix.** "item 3 a strike in form, nothing rewritten; item 4 deferred; the rest inert."

14. **Claim.** `checked_entry.md`:103–106, the routing block: "nineteen items in five groups … ending "PI:" … "Route as given"", with "most items carrying words from the raws' bodies".
    - **CONFIRMED.**
    - **Evidence.** `grep -c` counts 19 items and 5 groups in `pi_block.txt`. The block's last line is "PI:", and the message's last line is " Route as given". Thirteen of the nineteen items carry words from the raws' bodies.

15. **Claim.** `checked_entry.md`:106–107: "Against those blocks it differs in four places:".
    - **IMPRECISE.** Two dropped clauses are missed.
    - **Evidence.**
      - Raw (E) §5 item 4 ends "…entry, citing this raw by path and sha256 [route]"; block item 12 ends "…entry [route]".
      - Raw (C) §7 item 3 has "carried as a disclosure for Appendix D, no rule change, no re-analysis [carry]"; block item 15 has "an Appendix-D disclosure, no rule change [carry]".
      - The other changes are rewordings or anchors: item 2's "(§2 items 1–4, 7)" becomes "(§2)", item 5's "(§5 items 1–2)" is dropped, and item 13's "the seat's read of record" becomes "the read of record".
    - **Fix.**
      - Make it "five places".
      - End :118 with ";" and add this bullet: "items 12 and 15 each drop a clause: raw (E) item 4's "citing this raw by path and sha256", and raw (C) item 3's "no re-analysis"."
      - With that change, `checked_routing_raw.md`:5's "the differences are stated in the notes' entry" holds.

16. **Claim.** `checked_entry.md`:108–110 and :114–118, the bullets on group N, item 18 and item 14 with raw (C)'s items 4–5, including the quotations "This commit's push with the next commit or on its own" and "These commits' push".
    - **CONFIRMED.**
    - **Evidence.**
      - The block's items 1–8 map to raw (D) items 1–5, 7, 6 and 9, and block item 17 is raw (D) item 8.
      - Block item 18 is raw (E) item 6 without "The seat's own (§4) inert", with "[wait]" for "[inert; wait]".
      - No block item mentions raw (C) §6's departures. Both quotations are verbatim.

17. **Claim.** `checked_entry.md`:111–113: "…a clause of raw (E)'s item 7: the f3 session's close line on `b449ed6`'s entry with "Code commits raw (E) by path"…".
    - **IMPRECISE.**
    - **Evidence.** Raw (E) item 7 reads "Code commits this raw by path". The quoted words are block item 12's, not raw (E)'s.
    - **Fix.** `with raw (E) item 7's "Code commits this raw by path" (the block's "Code commits raw (E) by path")`.

18. **Claim.** `checked_entry.md`:119–121 (and the message): each relay verbatim between dash lines, each block equal by `cmp`, and "The first sends, by session name, reached no one; each text went again unchanged by session id".
    - **CONFIRMED.**
    - **Evidence.**
      - The by-id texts, taken from `<transcript>` by `jq`, have dash lines at 7/17/19 (n-build), 7/17 (n-analyzer), 7/13 (f3-build), 7/12 (dpo) and 5/7 (pod).
      - Their blocks are lines 8–16 and 18, 8–16, 8–12, 8–11 and 6. Each is `cmp`-equal to `pi_block.txt` lines 7–15 and 30, 7–15, 17–21, 23–26 and 14.
      - All five by-name sends returned "success":false: two "No agent is named '…' exactly" and three "No agent named '…' is reachable".
      - Each by-name text is sha256-equal to its by-id resend, and the five by-id sends returned "success":true.

19. **Claim.** The working files `sent_nanalyzer.txt`, `sent_f3build.txt`, `sent_pdpo.txt`, `sent_pod.txt`, `blk1_*.txt`, `blk2_nbuild.txt` and `sl_*.txt`.
    - **CONFIRMED.**
    - **Evidence.** The four sent files are `cmp`-equal to the transcript's texts. Each `blk` file equals its slice, and each `sl_*` file equals its `pi_block.txt` lines.

20. **Claim.** `sent_nbuild.txt` as "the sent text" to n-build.
    - **FAIL.**
    - **Evidence.**
      - The file is 29 lines and 4,584 bytes. Its first line (440 bytes) is the earlier push-#29 notice to n-build. Lines 2–29 are `cmp`-equal to the relay, which is 28 lines.
      - Cause: the extraction selected sends to n-build by `contains("PI date 2026-11-27")`, which the notice also holds. The relay check printed "nbuild: 29 lines".
      - The blocks lie inside the dashes and are unaffected (item 18).
    - **Fix.** If the file is kept, re-extract the relay alone (the send whose text begins "The PI's routing of the seat's G-READ-n record read") and re-run the block check. No committed text changes.

21. **Claim.** `checked_entry.md`:122–125, the relay to n-build.
    - **CONFIRMED**, against the relay's text: items 1–8 and 17 its, item 8's close line in the instruct form, item 17's form notes, item 5 n-analyzer's, and the folders' word blank with the volume kept.

22. **Claim.** `checked_entry.md`:126–129, the relay to n-analyzer: "…; ledger (91) and the dated note in its entry; …".
    - **IMPRECISE.**
    - **Evidence.**
      - The relay says: "You carry ledger (91) (raw (D) §2 item 5) and … a dated note in raw (D) §2 item 6's figures (raw (D) §5 item 4)".
      - Raw (D) §5 item 4 says "the n-analyzer session carries §2 items 3 and 6 into the VERDICTS entry".
      - §5 item 1's list of the VERDICTS entry's contents has no ledger. The ledger is the seat's ("Ledger — design seat, (91)"), recorded under routing item 3.
      - n-build's line (`checked_close_nbuild.md`:15–16) states §2 items 3 and 6, which is correct.
      - The rest of the bullet matches the relay: launch files first, the window after they are checked, no commit while it is open, and its own commit window.
    - **Fix.** Replace the phrase with: "§2 item 3's label and §2 item 6's dated note in its entry (raw (D) §5 item 4), and ledger (91), which the relay also gave it though raw (D) assigns it only §2 items 3 and 6;". Consider a one-line correction to n-analyzer before its launch files arrive.

23. **Claim.** `checked_entry.md`:130–137, the relays to f3-build, the dpo session and the pod session.
    - **CONFIRMED**, against the relays.
    - **Evidence.** The answer to f3-build's two questions reads "keep the declarations in the close line, and your values-check raw goes into my commit … as a sixth path".

24. **Claim.** `checked_entry.md`:139–143, n-build's line: "`f1a742df…ffca`, 24 lines, and copied cmp-equal", in the instruct form, with its quotations and its Next.
    - **CONFIRMED.**
    - **Evidence.**
      - n-build's message gives the full sha256, equal to the file's, and 24 lines.
      - The copy call printed "ok close_nbuild.md: 24 lines, 2581 bytes, at the sha256 sent" and "ok copies cmp-equal to the notes".
      - The quotations are checked in item 36.

25. **Claim.** `checked_entry.md`:144–145 and :156–157, the coordinating session's two lines.
    - **CONFIRMED** (see items 37–38).

26. **Claim.** `checked_entry.md`:146–151, f3-build's line: "…and the campaign folder's plain name stood in argvs and outputs in that window and since the end."
    - **IMPRECISE.**
    - **Evidence.** The line declares outputs only in the window ("It printed in the gate's output lines …"). Since the end it declares argvs only. Everything else in :146–151 is CONFIRMED: the sha256 and 56 lines match f3-build's final message, and the copy came from the notes folder at that sha256 ("ok close_f3.md: 56 lines, … at the sha256 sent").
    - **Fix.** "…stood in argvs and outputs in that window, and in argvs since the end."

27. **Claim.** `checked_entry.md`:151–155, f3-build's values-check: "one pass of 39 items (25 CONFIRMED, 7 IMPRECISE, 1 FAIL, 6 NOT CHECKABLE) and 7 observations … (sha256 `e0e1ed9e…b610`, 295 lines)".
    - **CONFIRMED.**
    - **Evidence.**
      - The raw's tally line has exactly these figures. It has 39 numbered items and observations O1–O7.
      - The sha256 and 295 lines match f3-build's message. The copy printed "ok vc_f3.md: 295 lines, … at the sha256 sent".
      - "every FAIL and IMPRECISE item applied" is f3-build's own word.

28. **Claim.** `checked_entry.md`:158–163, the dpo session's line: "`e5727365…574b`, 52 lines, and copied cmp-equal".
    - **CONFIRMED.**
    - **Evidence.** The message matches (52 lines, 5,350 bytes). The copy call printed "ok close_dpo.md: 52 lines, 5350 bytes, at the sha256 sent" and cmp-equal. The line's content is checked in item 41.

29. **Claim.** `checked_entry.md`:164: "Each session's line is placed as sent. Nothing else on any entry moves."
    - **CONFIRMED** (item 48).

30. **Claim.** `checked_entry.md`:166–173, the observations passed to the seat.
    - **CONFIRMED.**
    - **Evidence.**
      - n-build's matches its message: "out of every argv … the Read tool, or the name on stdin … I won't rename the note".
      - The dpo session's (a) recounts from raw (C) §0: 0 + 0, 5 + 1 and 7 + 2 sum to 15, while the raw says "twelve of the sixteen", with four missed.
      - The dpo session's (b) recounts from raw (C) §5: items 2, 3 and 5 cite the sft read's §5 items 2–4, item 4 is "(new", and items 1 and 6 are neither.
      - Neither sentence appears in the dpo session's line.

31. **Claim.** `checked_entry.md`:174–177 and the message: the two close lines promise a full hash, "no entry since has", and the full hashes are given.
    - **CONFIRMED.**
    - **Evidence.**
      - `git show 5ceb8dd -- RESULTS.md` and `git show e114b3a -- RESULTS.md` carry "A commit cannot name its own hash; the next RESULTS entry names it in full." 5ceb8dd's line is the sft VERDICTS session's ("the sft VERDICTS session's, drafted on the relay"), and e114b3a's says "This line is the instruct VERDICTS session's".
      - `grep -c -F` finds neither full hash, nor either 8-character prefix, in RESULTS.md at HEAD.
      - The entry's two hashes equal `git rev-parse`.

32. **Claim.** `checked_entry.md`:178–182, the plans under items 5 and 19.
    - **NOT CHECKABLE** (future).
    - **Evidence.** The quoted parts check: the entry name is in raw (D) §5 item 1, and "[yours]" is block item 19. No n-analyzer message has arrived since the PI's record (the session messages since are f3-build's two, n-build's and the dpo session's), so no window has opened.

33. **Claim.** `checked_entry.md`:183–186, the held part.
    - **CONFIRMED.**
    - **Evidence.** The parenthetical equals raw (E) §3's list and matches R:447–450.

34. **Claim.** `checked_entry.md`:188–190 and the message: committed by path, the home-folder count of 0, not pushed.
    - **NOT CHECKABLE** (commit time).

35. **Claim.** "The coordinating session ran nothing on a model." (entry :190, message)
    - **CONFIRMED** as far as its commands show.
    - **Evidence.** Among its Bash commands since the PI's record, one matches an interpreter or model pattern. It is a marker-word count, not a run (observation 6).

36. **Claim.** `checked_close_nbuild.md`, whole.
    - **CONFIRMED.**
    - **Evidence.**
      - Its six quotations ("Ruling: …", "A ceiling tie.", "N1 REPLICATED or PARTIAL — …", "A comparator-relative bar …", "N-pod's rule stands …", "a transcript search prints …") are each found once in raw (D) and in the line with its line breaks joined.
      - The routing's brackets match the block: 1–2 "[accept]", 3 "[record]", 5 "[go]", 8 "[route]", 17 "[inert]".
      - "§2 items 3 and 6 … (§5 item 4)" matches raw (D). The Next agrees with R:140–142.
      - Only line 3 is over 120 characters, at 134. It has no blank line and ends with one newline.

37. **Claim.** `checked_close_e114b3a.md`, whole.
    - **CONFIRMED.**
    - **Evidence.**
      - Raw (A) (`cd6ba27f…0209`) cites probe:29–33 at its line 8 (§0) and line 27 (§2 item 1), and "the lock, which pins probe:29–34" at line 29 (§2 item 3).
      - LOCK-n.md:1261 reads "(probe.py:29–34)". probe.py:29 is the docstring's head, 30–31 CONTRASTS, 32–33 COMPARATOR, and 34 the docstring's close (`"""`).
      - "Held for the next notes entry" is at R:447. Raw (D)'s full sha256 appears once.
      - Only the link line is over 118 characters.

38. **Claim.** `checked_close_5ceb8dd.md`, whole.
    - **CONFIRMED.**
    - **Evidence.** "Class: inert, no strike." and the two form notes, joined, are each found once in raw (E) §2. The counts 111, 46, 102 and nine are raw (E) §2's. "Departures, for the seat to class" is at R:1436. Raw (E)'s full sha256 appears once. Only the link line is over 118 characters.

39. **Claim.** `checked_close_f3.md`: its quotations and the first declaration.
    - **CONFIRMED.**
    - **Evidence.**
      - Lines 10–19, with "> " removed and joined, equal block lines 18–21 joined. Lines 33–36, joined, equal raw (E) §1 item 3's fix.
      - The quotations of item 2, of items 1 and 5's notes, of §0's "inert as to the verdict" and "no re-run, nothing rewritten", and of "not ruled here" are all in raw (E).
      - For the first declaration, f3-build's report of the gate's stop in `<transcript>` reads: "GATE STOP at pre (v1)", "holds `@@` five times, all quoted verbatim, on four lines", and "Nothing is staged". Gate v2 went out as a new file with its sha256 sent, and the coordinating session replied "Go ahead with gate v2 on the placed state."
      - `git grep` with a bracketed one-file pathspec on `b449ed6`'s values-check raw prints `@@RUNLIST@@` ×2, `@@VCRAW@@` ×1 and `@@VCTALLY@@` ×2, on 4 lines.
      - The file is 56 lines, only line 4 is over 120 characters, and it has no trailing blank.

40. **Claim.** `checked_close_f3.md`:47–53, the plain-name declaration beyond v1's refusal: argvs of shasum, git, grep and cp; the place and staged phases' lines; the session's own argvs and its values-checkers' since the end.
    - **NOT CHECKABLE.**
    - **Evidence.** v1's refusal printing the name is confirmed (it is quoted in f3-build's stop report). The rest lives in f3-build's own records and gate script, in folders the rules bar.

41. **Claim.** `checked_close_dpo.md`, whole.
    - **CONFIRMED.**
    - **Evidence.**
      - The §6 quotation equals raw (C):92, and the §3 totals equal raw (C):65 (both checked as strings).
      - The short form, §0's window sentence, the strict and wider definitions, the third register, "Reported; no bar; nothing reclassified.", §1's two tie quotations, §4 items 1 and 9, and §2's picks and seconds are all in raw (C).
      - The `counters_beside` figures are R:14818–14820, "not owed here" is R:14820–14826, and the release is R:14806.
      - Items 13–15's brackets and section B's heading quotation match the block. Raw (C)'s full sha256 appears once.
      - Only line 4 is over 118 characters, at 122. It has no blank line.

42. **Claim.** The three sessions' lines are "in the instruct session's form".
    - **CONFIRMED.**
    - **Evidence.** Each follows R:13945–13983: committed by path in the commit that adds the line, the `git log --diff-filter=A --` pointer, the link with its full sha256, "A commit cannot name its own hash; the next RESULTS entry names it in full.", the routing's items, and "Route as given". n-build names itself in its bold head rather than in a closing sentence.

43. **Claim.** `checked_routing_raw.md`:9–46 and :50–52, the fenced blocks.
    - **CONFIRMED** byte for byte.
    - **Evidence.** Lines 10–45 are `cmp`-equal to the record's lines 4–39, and line 51 is `cmp`-equal to its line 42 (" Route as given").

44. **Claim.** `checked_routing_raw.md`:5, the head's claims.
    - **CONFIRMED.**
    - **Evidence.**
      - The content is a plain string. Lines 4–39 (36) lie between the markup's lines 3 and 40, each followed by a newline.
      - The last line has no newline of its own: `jq -j` ends "…given".
      - Lines 1–2 and 41 are blank. The markup carries a client id.
      - The extraction was by `jq`. The item and group counts are 9/2, 7/2 and 5/3.

45. **Claim.** `checked_routing_raw.md`:5: "a departure that the coordinating session declares … in the notes entry that carries that span".
    - **NOT CHECKABLE** (future).

46. **Claim.** `checked_routing_raw.md`:3: "(C) … placed on 2026-11-26 and re-routed here unchanged."
    - **IMPRECISE.**
    - **Evidence.** The block's own line for (C) reads "placed 2026-11-26, unchanged, not yet routed". "re-routed unchanged from the 11-26 block" is section B's heading, about the seat's block, not the raw.
    - **Fix.** "placed on 2026-11-26, unchanged and not yet routed, and routed here in section B ("re-routed unchanged from the 11-26 block")".

47. **Claim.** `pi_msg_raw.txt` is the record's `jq -r` extraction, and `pi_block.txt` is its block.
    - **CONFIRMED.**
    - **Evidence.** Both are `cmp`-equal to the transcript: the whole message (42 lines) and its lines 4–39.

48. **Claim.** `checked_RESULTS_draft.md` is HEAD's RESULTS.md with six insertions.
    - **CONFIRMED.**
    - **Evidence.** HEAD's lines 1–23, the entry, 24–319, n-build's line, 320–467, e114b3a's line, 468–1084, f3-build's line, 1085–1571, 5ceb8dd's line, 1572–14882, the dpo line and 14883 to the end, piped into `cmp`, are equal. RESULTS.md equals HEAD by `git diff --quiet`. The line count is 42,056 + 347 = 42,403.

49. **Claim.** Widths and endings.
    - **CONFIRMED.**
    - **Evidence.** `LC_ALL=en_US.UTF-8 grep '.\{119,\}'` finds, in the entry, only link lines 10, 15, 20 and 154, and in each coordinating close line only its link line 3. The entry ends "Not pushed.\n\n". Each close-line file ends with a single newline after text.

50. **Claim.** The message is ASCII only, with the co-author line last.
    - **CONFIRMED.**
    - **Evidence.** `tr -d '\000-\177' | wc -c` gives 0. The last line is the co-author line, ending in a newline. `@VCMSG@` appears once.

51. **Claim.** The message's other claims: paths and abbreviations, the five lines and their places, the relay item ranges (n-analyzer 1–8 is group N), item 7's blank, and the held part.
    - **CONFIRMED.**

52. **Claim.** Public-repository rules for all nine texts to be committed (entry, five close lines, routing raw, message, `checked_vc_f3.md`).
    - **CONFIRMED.**
    - **Evidence.** `grep -c` finds 0 roots, 0 ids or UUID forms, 0 user name (bracketed patterns), 0 IP forms, 0 clock-time or UTC forms, 0 ssh or port forms, 0 non-family guard words and 0 campaign plain name. The only email or domain hit is the message's co-author address. `checked_vc_f3.md` is f3-build's named file (sha256 and 295 lines).

## Observations

1. Two older close lines make the same promise: R:23937 (last changed at `dc1ffe1`) and R:24560 (`79d462b`), by `git blame`. A one-line search finds neither commit's full hash in RESULTS.md at HEAD. This is outside the entry's claim, for the coordinating session to weigh.
2. Section B's heading says "re-routed unchanged from the 11-26 block", but items 13–15 differ from raw (C) §7 items 1–3 in wording (item 14 spells out the tallies; item 15 drops "no re-analysis"). The dpo session's line quotes the heading accurately, as the PI's words.
3. Raw (E) §0 gives items 1, 2 and 5 "a form note each", but §1 item 2 carries none. The entry follows §1 and gives two notes.
4. On the dpo session's observation (a): raw (C) §3.3 calls G-F0m's s = 1 round 2 a clarification request "in the register of §3.1". It may be the sixteenth response. This is for the seat; not checked further.
5. R:144 at HEAD (the entry `G-READ-n`) carries a clock time in UTC in its departures span. It is outside this commit's texts and is not reproduced here.
6. For the coordinating session's held sweep, these forms appear in its own commands since the PI's record:
   - its slicing call's `grep -E` pattern held the dpo unit's name unbracketed (`[O]LMo-dpo` written plain);
   - one pre-screen command's count pattern held all five marker words unbracketed;
   - its extraction call ran `ls -l` on the transcript, printing the file's size and modification time;
   - its relay-check selector caught the push-#29 notice (item 20).

## My own departures

- **Transcript.** 39 Bash calls touched `<transcript>`. Each ran `/usr/bin/grep -F` (or `-c -F`) first and then `jq`; one also ran a `wc -l` of it. Six printed more than a finding needed:
  - one search printed three of the coordinating session's commands, two of them not needed, with five session ids unmasked in the tool output;
  - one printed two lines of an unrelated record (a close-commit notice and an Edit's input);
  - one printed a session-context attachment's type and size;
  - the session-message list printed two empty heads;
  - the first-send list and its results printed target session names, one holding a guard marker (output only);
  - the re-hash call's result included the coordinating session's earlier scratch listing.
  - Two `jq` calls ended in errors and printed nothing else. None of the above is reproduced here.
- **The campaign folder's plain name.** It was typed in 13 commands' text, as the search side of a `sed` substitution meant to bracket it in outputs, so it stood in `sed`'s argv. It was never used as a path, and nothing under the folder was named, listed or read. `b449ed6`'s values-check raw was reached only by a bracketed git pathspec.
- **Git forms without item 3's pathspec** (one file outside `data/` each):
  - `git diff --quiet HEAD -- RESULTS.md` ×1;
  - `git show <commit> -- RESULTS.md` ×6, filtered;
  - `git blame -l -s -L` (five ranges) `-- RESULTS.md` ×1;
  - `git ls-files` ×1, `git grep -c -F` ×1 and `git grep -h -o -E` ×1, all on one bracketed file pathspec (printed counts and three tokens).
  - Item 1 forms also ran: `git rev-parse` (2 calls), `git log -1 --format` ×2, `git log --all --format=%h -- <path>` ×5, and `git status --porcelain -- results/raw` ×1.
- **Counts and sizes** (all outside `data/`): `wc -l`/`wc -c` of the raws, the checked texts, the brief, `pi_msg_raw.txt`, `sent_nbuild.txt`, RESULTS.md and the transcript; `tail -c | od -c` of file ends; `tr -d | wc -c`; UTF-8 width greps; `grep -c` screens.
- **Listings.** One name-only `ls` of the checked folder, and one name-only `ls` of `<repo>`'s root, filtered.
- **Reads.**
  - 17 Read-tool reads: the brief, eight checked texts, the three raws and five `sent_*.txt`.
  - `sed -n`/`grep` of RESULTS.md, raw (A), LOCK-n.md, probe.py, n_analyze.py, the ADDENDUM-n1 and PROPOSAL-n v0.2 files, and `checked_vc_f3.md` (headings, tally and observation lines only).
  - `shasum` of the brief, the raws, the checked texts and copies, and n_analyze.py.
- **Other.** `cmp` with process substitution (pipes; no file written). The roots were typed in full in command text, and once the account name appeared in a bracketed screen pattern.
- **Not done.** No file written, no git write, no interpreter but `shasum` and `jq` (`jq` only over the transcript), no network, no marker word plain in any command, no marker-named path passed, nothing under `data/` read or hashed, and nothing touched in another session's folder, the notes folder or the memory folder.

## Tallies

52 items: 39 CONFIRMED, 7 IMPRECISE, 1 FAIL, 5 NOT CHECKABLE. 6 observations.
