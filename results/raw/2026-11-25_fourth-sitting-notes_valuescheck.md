# The coordinating session's notes on the seat's sitting of 2026-11-25 (the thread's fourth): the blind values-check, as returned, with every disposition

2026-11-25. Code (the coordinating session).

**What was checked.** One blind pass by a subagent over the entry's draft (sha256 `c9e21289…54bc`, 294 lines), the close line on `95cd461`'s entry (`62640334…5205`, 14 lines), the routing raw (`ce82b3d2…fac4`, 46 lines), the commit message's draft (`f4569803…cfa3`, 3 lines), and their placement in a draft of the new `RESULTS.md` (`88501fd8…1aaa`, 40,276 lines), with the coordinating session's sweep of its own tool calls (files in a sweep folder of its scratch) as the source of the entry's departures.

**The checker's brief** was a file in the coordinating session's scratch folder, named in its Agent call by path (sha256 `5fe05fa6…fe25`, 101 lines). It is not committed, because it names the local roots in full. It:
- named the sources: the seat's raw; the PI's message in the coordinating session's transcript, with its extraction; the three relays, with their files; the coordinating session's own checks in its transcript; the part held at `78cd6eb`, against the transcript and the repository (`c26b117`, `fcab1e5`, `e1be6d9`, `9792e14`, `78cd6eb` and `95cd461`, with the push records), `95cd461`'s data paths taken from the verify's outputs alone; the sweep's files, with a blind second check for any departure class missing; the `78cd6eb` values-check raw's own departures; and the repository at `95cd461`;
- quoted the list of record v2's items 1–5 verbatim, from `2026-11-10_list-of-record-v2_design-to-code_answers.md`, taken from the last brief (the section equal by `cmp` to the last brief's lines 55–62, its five items to the coordinating session's copy);
- barred any interpreter but `shasum` and `jq`, any write, any network, `ps` and `pgrep`, a whole-tree `git status`, anything under `data/*/ckpt`, `data/*/reports` or the campaign folder, the memory folder, other sessions' folders, the side-session notes folder, the staging folder, and the guard markers and the campaign folder's plain name in any command text;
- barred passing any path holding a marker word to a command as an argument: such paths go on stdin only;
- set item 3's pathspec, with the campaign folder's exclusion, on every git command over the tree or a range;
- barred from the report the network volume's server host name, as from the committed record.

An addendum, sent to the checker while it ran, barred clock times from its report.

**The report** is in §3, extracted verbatim by `jq` from the subagent's one hand-back (400 lines as `jq -r` wrote them, the last ended by the newline `jq` adds; sha256 `a0bfa695…48cf`), byte for byte, with no mask. It names no local root. Its `<repo>`, `<own>`, `<transcript>` and `<sweep>` are the repository, the coordinating session's scratch, its transcript and its sweep folder. Its account of its own calls is its own: its transcript holds 172 `Bash` and 21 `Read` tool calls, against the report's 148 and 12, by a count of the tool names alone.

**Totals:** 73 items (53 CONFIRMED, 15 IMPRECISE, 4 FAIL, 1 NOT CHECKABLE) and 10 observations.

## 1. Dispositions

- **Item 40** (FAIL): fixed in the checker's words: a bullet "task outputs, by the shell", five commands.
- **Item 45** (FAIL): fixed: "printed by `grep` and `awk`".
- **Item 49** (FAIL): fixed in the checker's words: the volume host's name in an `-E` alternation in three more leak counts and in a form-count pattern in a tenth; the user's name once typed plain as a fixed pattern.
- **Item 52** (FAIL): fixed in the checker's words: four anchor asserts whose `cut -c` prefixes split a multibyte dash; the count over absolute paths and its re-run; the `head -0`.
- **Item 7** (IMPRECISE): applied in the checker's words, in the entry (§3's points 3 and 6) and in the message ("the chain's route, as the campaign's").
- **Item 16** (IMPRECISE): applied: "ans24 §1.5 (5)" twice, "ans24 §1.7 (b)" and "ans24 §1.8"; by the same reading, "ans24 §1.7 (a)" in the relay bullet and "ans24 §1.8" in the screens' bullet; and "ans24 §N" defined in the read bullet (observation 2).
- **Item 22** (IMPRECISE): applied: "none on four rechecks".
- **Items 29, 39, 41, 43, 44, 47, 48, 53 and 56** (IMPRECISE): applied in the checker's words or near them.
- **Item 46** (IMPRECISE): applied, joined to the bullet's clause on the messages' results.
- **Item 54** (IMPRECISE): applied: the RunPod read moved beside the shell.
- **Item 55** (IMPRECISE): applied: "no other Python ran".
- **Item 59** (NOT CHECKABLE): the commit's own count, met at the commit by its gate.
- **Observations 1, 2, 3, 4, 5, 7 and 9:** applied:
  - the stop's order: the item-5 bullet gives it as the transcript has it, after the verify and before push #25, and records that the seat's raw places it after the push (§0, §5) (1);
  - "ans24 §N" defined (2);
  - the spec raw's content (two marker-word lines and the campaign folder's plain name, as content) noted in the `fcab1e5` bullet, its sections written "its §N" (3);
  - the name-only listings (34 commands) and n-build's scratch by the shell (82 commands) given bullets of their own, counted by tool (4, 5);
  - the `tail`'s wrong path (7);
  - the relays' heading, "Items 1–2 (N) and 5 (C)", each message carrying all six items (9).
- **Observations 6, 8 and 10:** noted:
  - the sweep's script counts mentions; the counts it left uncorrected are corrected through items 41 and 53 (6);
  - the `:s` misfire's `cut` error is part of the listed misfire (8);
  - the calls after the sweep are in the entry's bullet "after the checked sweep, to the last", from a last sweep (10).

## 2. Edits after the check

- The dispositions above, the rewraps of the bullets they changed, and the fills of the four placeholders: `@AFTER@` from a last sweep of the calls after the checked one, `@VCCHK@` with this checker's departures as its report states them, `@VC@` with the values-check bullet, and `@VCMSG@` in the message.
- The edits were checked by tool, by `diff` of each checked draft against its final text. Each hunk is a disposition above, a rewrap, or a fill.
- No second full pass was made.

## 3. The report as returned

# Blind values-check: the coordinating session's notes on the seat's fourth sitting (PI date 2026-11-25), after `95cd461`

Scope: `entry.md`, `close.md`, `routing_raw.md`, `msg_src.txt` and `RESULTS_draft.md` in `<own>/s2026-11-25/fourth-sitting/`. I checked them against the seat's raw, the PI's typed record of 2026-11-25 in `<transcript>`, the three relays, the sweep files in `<sweep>`, the repository at HEAD `95cd461` and the values-check raw from `78cd6eb`. The brief re-hashed equal (`5fe05fa6…fe25`, 101 lines). "Call N" means the window index `i` in `<sweep>/calls_since.jsonl` (the same `i` as in `bash.jsonl`). I did not check the placeholders `@AFTER@`, `@VCCHK@`, `@VC@` and `@VCMSG@`. Hash abbreviations were checked by `cut -c1-8` / `cut -c61-64`.

## Items

### The entry: the read, the raw, the routing and the relays

1. entry.md:1–6: "the N-pod campaign's run of record and its close accepted as committed at `95cd461`, G-READ-n's BUILD (step 15) a go, and the network volume kept until G-READ-n's artifact is committed; the raw committed here by path on the PI's "route as given" (item 4) … (pushes #21–#25, "launch cleared", the campaign's run and its close)". **CONFIRMED.** These match PI items 1, 2, 4 and 5 and the message's last line. Each of the five pushes printed exit 0 (calls 79, 129, 287, 395, 614).

2. entry.md:9: "(sha256 `7f5020b9…37f4`, 17,389 bytes, 65 lines)". **CONFIRMED.** `shasum -a 256` gave `7f5020b9…37f4`, `wc -c` gave 17389 and `wc -l` gave 65. `git status --porcelain -- results/raw` shows it as `??`.

3. entry.md:9–12: "its entry whole, the report under item 2 (…), the start's and names' out raws (the 7,680 read lines by tool), the close list by structure and by name, and both pod records; nothing under `data/n/ckpt/` was opened or hashed by the seat. It was placed untracked over the bridge." **CONFIRMED.** Line 3 of the raw (its header) and lines 5–7 of the PI's message say the same.

4. entry.md:12–15: "re-hashed it equal …, found it untracked with HEAD, origin's tracking ref and `ls-remote` at `95cd461`, and read it whole." **CONFIRMED.** The session's first shell call after the PI's record printed the full sha256, 17389, 65 and `??`, with HEAD, `origin/main` and `ls-remote` all at `95cd461`. Its Read of the raw had no offset or limit (66 result lines).

5. entry.md:19–25, the run and its close (§0–§1; item 1): COMPLETE in one invocation, 7,680 of 7,680, no pause and no STOP, `used_ms` 3,786,451 of 14,400,000, G-VER PASS, 0 fires over 3,637, figures re-derived, the close as ans24 §1.5 ordered it, and the seat finding nothing wrong. **CONFIRMED.** Raw title, §0 (lines 7–9) and §1.1.

6. entry.md:26–29, the observations (§2): there are four; the slow load is "125,924 ms against G-TIME-n's 12,365 and 12,375 ms", outside the cap by the lock's accounting; `exceed_tau4` is 707 of 3,637; the first tile was the shadows. **CONFIRMED.** Raw lines 20–25.

7. entry.md:33–34: "(3) the form, A-n1 §6.2–§6.4 as the lock carries them". entry.md:38–39: "(6) the route the campaign's: Code's survey and PINs, …". msg_src.txt:1: "the campaign's route". **IMPRECISE.** Raw §3.3 (line 31) reads "A-n1 §6.2–§6.4 and PIN-n's probe readings as the lock carries them". Raw §3.6 (line 34) reads "The route is the chain's: …, as the campaign's were". Points (1), (2), (4) and (5) match raw lines 29–33.
   - Fix (entry, point 3): "(3) the form, A-n1 §6.2–§6.4 and PIN-n's probe readings as the lock carries them, …"
   - Fix (entry, point 6): "(6) the route the chain's, as the campaign's was: Code's survey and PINs, …"
   - Fix (message): "the chain's route, as the campaign's".

8. entry.md:40–42, the departures (§4; item 4): "Code's six spans (94 commands), the pod session's §11 and §12, and the checker's, as `95cd461`'s entry declares them, …; the seat's own, inert." **CONFIRMED.** Raw lines 36–40. RESULTS.md:218 reads "in six spans, 94 commands in all".

9. entry.md:43–49, record hygiene (§5). **CONFIRMED.** Raw lines 44–47.

10. entry.md:50–53: "named the raw with its sha256, bytes and lines, gave six items in four groups, filled the one blank … (item 5) with "keep", and ended "PI: route as given". No question from the coordinating session came before it." **CONFIRMED.** The record is a plain string with origin "human". The groups are N (1–2), A (3), C (4–5) and D (6). Just before it come the session's closing text (statements only, ending "… each wait for your word"), a wrap-up holding a recap and no question, a session notice, and the session's reply (statements).

11. entry.md:54–56: each message carried the PI's message whole between two lines of dashes; each block equals it by `cmp`; each sent text, read back by `jq`, equals its relay file by `cmp`. **CONFIRMED.**
    - The three SendMessage inputs after the record, extracted by `jq -r`, equal `relay_nbuild.txt`, `relay_pod.txt` and `relay_nanalyzer.txt` by `cmp`.
    - Lines 8–43 of the first two equal `pi_msg_raw.txt` by `cmp`, each between two "----------" lines.
    - The session's own outputs read "BLOCKS PASS" and "SENT PASS".

12. entry.md:57–62, the message to n-build. **CONFIRMED.** relay_nbuild.txt lines 46–56.

13. entry.md:63–66, the message to the pod session. **CONFIRMED.** relay_pod.txt lines 46–52. The pod session's own message gives "re-touch by 2026-11-29".

14. entry.md:67–69: the block equals "the message's lines 23–24: "3. Nothing; v7 of record; VERDICTS after G-READ-n on the PI's word, --gread the committed artifact. [as ruled]", with §3's first point for its record; nothing asked of it." **CONFIRMED.** relay_nanalyzer.txt lines 8–9 equal pi_msg_raw.txt lines 23–24 by `cmp`; the quote's space stands for a line break plus a three-space indent. Line 12 carries §3.1, and line 1 says "it asks nothing of you now".

15. entry.md:70–71, item 4. **CONFIRMED.**

16. entry.md:72–73: "stopped on the coordinating session's word after the close commit's verify (§1.5 (5))". Likewise line 146 "§1.7 (b)'s two parts", line 183 "under §1.8's cleared halt" and line 185 "(§1.5 (5))". **IMPRECISE.**
    - The facts hold: the stop message (call 590) came after the verify (calls 575–578) and before push #25 (call 614), and get-pod read "EXITED" (call 601).
    - But lines 16–17 define "§N" as "a section of the seat's raw". That raw's §1.5 is "The PI's words of record" and has no (5).
    - The rule cited is ans24's: "(5) the pod stops only after that commit's verify" (ans24 raw, line 31). Line 22 of the entry already writes it as "ans24 §1.5".
    - Fix: "(ans24 §1.5 (5))" at lines 73 and 185; "ans24 §1.7 (b)'s two parts" at line 146; "under ans24 §1.8's cleared halt" at line 183.

17. entry.md:76–77, item 6: "… as `78cd6eb`'s entry read that bracket." **CONFIRMED.** PI item 6; RESULTS.md:404–408.

### The entry: the part held at `78cd6eb`

18. entry.md:79–82, `c26b117`'s close. **CONFIRMED.** Calls 1–22 show GATE PASS (call 14) and the commit `c26b117` (call 15). The verify (call 16) printed "one parent 098218c" and VERIFY PASS. The screen (call 18) printed 1 commit, 4 file-diffs, six classes "-> CLEAR", gitleaks 0 and gl5 0. Message 21 to n-build says "Rebase the seat block onto it".

19. entry.md:83–95, `fcab1e5` and push #21. **CONFIRMED.**
    - The request has 110 lines (call 27). Call 30 printed "OK count: 16 of 16".
    - The five sections match their sources by `cmp`, §4 differing only in its path line (call 37). Each fenced report differs by one declared line (call 39). Leaks are 0 in all eight texts (call 40).
    - The held question was the find's root (call 44). The re-check printed 117 paths with 0 marker words (call 62).
    - The verify (call 73) shows one parent `c26b117`, "added 2119, removed 0" (my `git diff --numstat` also sums to 2119) and VERIFY PASS. The screen (call 75) shows 2 commits, 10 file-diffs, CLEAR, gitleaks 0, gl5 0.
    - The three push attempts: call 77 stopped at the range test (the trailing colon, fixed in call 78 by `tr -d ':'`); call 78 printed "src refspec …efs/heads/main does not match any"; call 79 used `REFSPEC="${C}:refs/heads/main"` and printed "PUSH OK".
    - Push #20 is recorded in `c26b117`'s entry (RESULTS.md:1237, 1291) and `78cd6eb`'s (406–408).

20. entry.md:96–100, draft 4's battery window. **CONFIRMED.**
    - The note has 59 lines (call 49).
    - Call 53: `47abe489…c21a`, 7836 lines; a 24-line delta; "draft3 + delta4_from_draft3 = draft4 (cmp)"; "HEAD's driver + delta4_from_head = draft4 (cmp)"; overlay4 175 files.
    - Call 68: 774/774; "= run 3's bytes (cmp)"; names and blobs equal to the pre-run listing; PID 8051.
    - The delta (read at call 51) has two hunks: a docstring clause and an error-message string.

21. entry.md:101–107, `e1be6d9`. **CONFIRMED.**
    - The request has 102 lines (call 88). Call 91: 15 of 15 inputs; the driver equals draft 4; "added lines scanned: 2755", "GATE PASS (dry run)".
    - The two fenced reports match their pinned sources by `cmp` (calls 95–96), and the added lines hold "markers 0, plain campaign 0" (call 96).
    - The verify (call 104): one parent `fcab1e5`, "added 2755, removed 36" (numstat agrees), VERIFY PASS.
    - The screen (call 106): 1 commit, 6 file-diffs, CLEAR, gitleaks 0, gl5 0.

22. entry.md:108–117, the launch windows and push #22: "A transient `n_sessions` process match at its first check, none on three rechecks, …". **IMPRECISE.**
    - The rest holds:
      - The note has 147 lines (call 112). Run 1's hashes file equals the committed raw by `cmp` (call 138).
      - Run 2: 29 cases, 7680 plan lines, 3637 marked R, "indices 0..7679 in order: yes" (calls 140–141). Run 3: 54 fixtures (call 143).
      - Run 4: "fixtures 54 of 54, mutants 33 of 33"; the overlay equals its listing; PID 8051 alone (call 146).
      - Push #22 printed exit 0 (call 129), on the PI's word of 2026-11-24.
      - The second note has 77 lines (call 153). The second window shows 58 fixtures; 58 of 58, 33 of 33 and 8 of 8 (calls 166, 168).
      - n-build answered: "the final mutation pass's bash stand-in".
    - But after the first check ("n_sessions 1", call 156) there were four empty rechecks: call 157's loop over `pgrep -f '[n]_sessions'` printed no PID, and call 158 printed three empty "n_sessions matches:" lines.
    - Fix: "none on four rechecks".

23. entry.md:118–120, the mutation pass. **CONFIRMED.** The report was read by list_events (call 175), and the two scripts were hashed (call 177). Call 178 printed "venv pythons: 8051 …; n_sessions matches: 4", each "comm /bin/bash". The log line (call 181) reads "52 of 177 mutants al…".

24. entry.md:121–128, launch set v1. **CONFIRMED.**
    - Call 184: 226 lines, "= the sent sha256". Call 187: "rows 50; sha256 and lines as the note: 50", error files 0 bytes, exits 0.
    - Call 188: harness 787 passed, replay 155 passed, null mutant 787. Call 189: killed 44+42+43+43 = 172; declared equivalents surviving 1+2+1+1 = 5.
    - Call 205: "OK lines 66".
    - Reads at calls 193–203: `camp_v1.sh` in four slices, the note, `camp_place_v1.sh`, the dispositions and the departures.
    - The constants all printed "equal" (call 215).

25. entry.md:129–130, the PI's "Commit a raw". **CONFIRMED.** ReadNotifications ran (call 220); HEAD equalled origin and there was no new raw (call 222). The relay (call 226) reads "verbatim: "Commit a raw"".

26. entry.md:131–138, `9792e14` and push #23. **CONFIRMED.**
    - The request has 159 lines (call 235). Call 237: 12 OK; the block has 239 lines.
    - Verdicts: 37 CONFIRMED and 4 FAIL in call 252; the grant's tally is "58 items, 37 CONFIRMED, 15 IMPRECISE" (call 263).
    - Each of the 12 abbreviations matched a named file (call 260). v17 differs from v16 only in its header and two ids (call 245).
    - The verify (call 275): three paths, RESULTS.md equal to the splice, 875 added, VERIFY PASS. The screen (call 278): 1 commit, 3 file-diffs, CLEAR, gitleaks 0, gl5 0.
    - The push printed exit 0 (call 287). The grant says "Two observations; no change asked" (call 263).

27. entry.md:139–141, the third sitting and `78cd6eb`. **CONFIRMED.** The verify (call 379) printed VERIFY PASS and 786 added lines; numstat gives 158+94+480+54 = 786 added, 0 removed. The screen (call 380) shows CLEAR, gitleaks 0, gl5 0. A Write created the new memory note on the bracket.

28. entry.md:142–147, push #24 and "launch cleared". **CONFIRMED** (for the §1.7 (b) reference, see item 16).
    - PREPUSH PASS (call 393); the push printed exit 0 (call 395); "behind/ahead 0 0" (call 397); 6 of 6 OK (call 405).
    - Message 414 carries the six paths with full sha256s and line counts, steps 1–5 with the no-restart check first, the announce and launch on the coordinating session's word, §1.7 (b)'s two parts, LQ4, and "Every end but COMPLETE goes to the seat and the PI".

29. entry.md:150–152: "the announce file in the pod session's notes folder was looked for and not found, and the message was checked instead". **IMPRECISE.**
    - The other claims of the sub-bullet hold:
      - The command's sha256 `c6811f22…2710` is equal (call 435).
      - The driver blob equals DRIVER_BLOB (call 437, after call 436's misfire), and the driver's, `LOCK-n.md`'s and the ids' MANIFEST sha256s were printed (calls 436–437).
      - "LAUNCH AS ANNOUNCED" was sent (call 438). The printed command equals the announced one by `cmp` (call 446), and the PID is 17386.
    - But the search (calls 424–433) looked in three places: the pod session's expected scratch folder ("no scratchpad folder at that path"), the memory folder ("absent under"), and the session scratch folders by a pruned `find` (no output). No call from 424 to 437 names the shared notes folder, which is where the pod session keeps its notes.
    - Fix: "the announce file was looked for by name in the pod session's expected scratch folder (absent), in the memory folder and, by a pruned find, in the session scratch folders, and not found; the message was checked instead".

30. entry.md:154–158, the start's end and copy-back. **CONFIRMED.**
    - Call 467 printed "cap used: … 26.29% of the cap" and the stage's wall time, both by `awk`. BLOCK EQUAL (call 469); SENT EQUAL (call 472).
    - Call 483: "NINE EQUAL (abbreviated, in order)"; the hashes file is `a853932b…522b`. BLOCK EQUAL and SENT EQUAL again (calls 485, 488).

31. entry.md:159–165, names. **CONFIRMED.**
    - Calls 493 and 501: 348 bytes, CMD EQUAL, `0e9811f8…3e90`. Call 500: "pod record: 77e3f8e5…ba2a, 227 lines".
    - The go (call 499) carries the step-3 change. The pod session reported "Holding the names launch…". The re-send says "the same go and not a second one" (call 512).
    - PRINTED CMD EQUAL (call 516); PID 19402; `42682630…fe6d` (call 522); N = 4,417 in the relay (call 526).

32. entry.md:166–170, the report before step 4. **CONFIRMED.**
    - Call 535: 7 names; six files equal plus the pod record; LIST EQUAL; "list lines 4417; … json paths 139; first path: data/n/reports/campaign.json; gver record lines 0"; LIST PATHS = close_paths.txt, in order.
    - Call 537: `2127906a…9ce7`, 136 lines. The script's usage and programs were read (call 536).
    - The relay (call 541) invites the window request and says the staging and holding folders were not opened.

33. entry.md:171–177, the close's commit window. **CONFIRMED.**
    - Call 556: the pin is `48b438eb…2b4f`; "NOTE SHA EQUAL"; 132 lines. Call 559: "inputs OK 24".
    - Call 561: HEAD equals origin at `78cd6eb`; tracked changes 0; four hunks, each equal to its source.
    - Call 562: 13 files with 0 lines holding the home root, the temporary root or the name; GATE PASS (dry run).
    - Calls 565 and 568: step 2 failed `bash -n`; the correction parses ("GRANT STEP 2 = FIXED").

34. entry.md:178–185, `95cd461`'s verify and screen, and the pod stop. **CONFIRMED** (for the § references, see item 16).
    - One parent: call 575 prints "parents count 2", which is the commit plus one parent. My `git rev-list --parents -n 1 95cd461 | wc -w` also gives 2.
    - "paths 150 …; npy: 0" (call 575). "raws equal (sha256 + lines): 8 of 8", with RESULTS.md and the message equal (call 576).
    - "BLOB IDS: commit = working tree, 141 of 141", and the steered cells at their pins (call 577). "OK 139" (call 578). "staged under data/n: 0" (call 576).
    - The screen (call 587): 1 commit, 150 file-diffs, six classes CLEAR with inside and outside counts; one gitleaks finding in `data/n/reports`, classed a digest by gl5.
    - The dry pre-push printed PREPUSH PASS (call 588). The stop message is call 590. Call 600: "STOP RECORD SHA EQUAL", 62 lines. Get-pod read "EXITED" (call 601).

35. entry.md:186–187, push #25. **CONFIRMED.** PREPUSH PASS (call 612); "push exit=0" (call 614); ls-remote, the tracking ref and HEAD at `95cd461`, "behind/ahead 0 0" (call 616); messages 631 and 632.

### The entry: departures

36. entry.md:189–191: "672 calls to the sweep, 299 of them shell commands, the sweep itself the last of them. No guard marker was in their text (a bracketed count)." **CONFIRMED.**
    - Between `c26b117`'s last sweep call (2026-11-24, "Check widths and sweep the calls after the checked sweep") and the call that wrote `calls_all.jsonl`, the transcript's assistant records hold 672 tool-use ids. That is the same set as `calls_since.jsonl` (checked by `sort -u` and `diff`), and `all_ids.txt` matches.
    - 299 of them are Bash calls, and call 672 is "Extract every tool call…".
    - A bracketed, case-insensitive marker test over all 672 inputs found 0.

37. entry.md:191–197, the 18 spans' counts. **CONFIRMED.** Each count is a contiguous run of `bash.jsonl` at a natural boundary: ordinals 1–15, 16–43, 44–52, 53–78, 79–82, 83–94, 95–96, 97–126, 127–176, 177–189, 190–203, 204–216, 217–236, 237–242, 243–257, 258–274, 275–282 and 283–299. They sum to 299.

38. entry.md:199–202, process reads. **CONFIRMED.**
    - Of the 23 commands matching `pgrep`, 19 run it; calls 2, 70, 163 and 177 hold it only in patterns or log text.
    - Counts only, with `ps -p 8051 -o pid=`, in 13: calls 14, 18, 40, 54, 68, 75, 96, 106, 115, 146, 156, 260, 278.
    - PIDs printed in six: calls 157, 158, 168, 178, 246, 261.
    - `comm=` in calls 157, 158 and 178; the parents in call 157.

39. entry.md:203: "its transcript, read in 43 commands by `/usr/bin/grep -F` and `jq`". **IMPRECISE.** 43 commands name the transcript, and no other command reads it. But seven of them read it by `/usr/bin/grep -o` with a pattern, not `-F`: calls 326, 355, 425, 426, 549, 550 and 582. Those printed re-touch phrases, the paths of the pod session's and n-build's notes, and the screen tool's names. Fix: "in 43 commands by `/usr/bin/grep` (`-F`, or `-o` with a pattern in seven) and `jq`".

40. Not in the entry: task outputs read by the shell. **FAIL** (a departure class that is not listed).
    - Five commands name a file in the session's tasks folder.
    - Call 255 read the background hash check's output so far.
    - Calls 356, 357, 358 and 367 read the `78cd6eb` values-checker's task output (its transcript) by `jq`. They printed its tool names and its hand-back's fields and lengths, extracted its report whole into scratch, and printed its last bytes by `od -c` with a `wc -c`.
    - None of these is among the 43 transcript reads, and the Read tool's "task outputs 3" are other files.
    - Fix: add after line 205: "- **task outputs, by the shell,** in five commands: the `78cd6eb` values-checker's (its transcript) by `jq` in four (its tool names, its hand-back's fields and lengths, its report extracted whole for the raw, and its last bytes by `od -c`), and the background hash check's output so far in one;"

41. entry.md:206–208: "its memory folder, by the shell, in 58 commands: 36 appends …, one pointer line … by `printf`, and 21 reads by `grep`, `sed -n`, `tail`, `tail -c` into `od -c` and `wc -l`, among them two `grep`s over named notes there". **IMPRECISE.**
    - Call 2 counts in the 58 but names `/memory/` only as a count pattern over the earlier sweep's file, so 57 commands touch the folder.
    - The 36 heredoc appends to the routing log hold, and so does the `printf` index line (call 387).
    - Of the other 20, 19 are reads (by `grep`, `cat` into `sed -n` at call 359, `tail` and `wc -l`). The 20th (call 429) is an existence test (`[ -f ]`, printing "absent under").
    - The `tail -c` looks, one of them into `od -c`, sit inside four of the appends (calls 382, 421, 443, 449).
    - Greps over named notes other than the routing log and the index ran in five commands (calls 254, 409, 424, 466, 554), several of them other sessions' notes.
    - Fix: "in 57 commands (a 58th names the folder only in a count pattern): 36 appends to its routing log by heredoc, four of them with a `tail -c` look at its end (into `od -c` in one); one pointer line appended to its memory index by `printf`; 19 reads by `grep`, `cat` into `sed -n`, `tail` and `wc -l`; and one existence test of a file there; among the reads, greps over named notes in five, some of them other sessions'".

42. entry.md:209–212, the unpruned finds. **CONFIRMED.** Calls 244 (each file hashed by `shasum` on stdin) and 256 (a `wc -l` count) ran over `camp/launch` and `camp/points/commit2` in n-build's scratch. Both moved to the background and were stopped by TaskStop (calls 258, 259), and neither printed a path.

43. entry.md:213–215, the five background commands. **IMPRECISE.**
    - The five are calls 244, 256, 426 (stopped at call 428), 548 and 550.
    - But the backgrounded pruned `find` (call 548) searched n-build's scratch folder only. The depth-limited search of the session scratch folders (call 552) did not go to the background.
    - Call 550's output was read once while it ran (empty, call 553) and again when it ended (call 555).
    - Fix: "a pruned `find` by name for n-build's window note in n-build's scratch folder, which found nothing; and a transcript `grep` for the notes folder's path, read once while it ran (empty) and again when it ended".

44. entry.md:216–217: "a recursive `grep -r -l` over it for a hash prefix, printing file names". **IMPRECISE.** The count of 20 commands holds. But call 254 ran two recursive greps over the notes folder: `grep -r -l -F` for the prefix, which printed one file name, and `grep -r -h -o -E` for the gate script's name, which printed two fragments holding full sha256s. Fix: "two recursive `grep`s over it in one command: `grep -r -l` for a hash prefix, printing a file name, and `grep -r -h -o -E` for the gate script's name, printing two fragments with full sha256s;".

45. entry.md:218–221: "and in four tool outputs: those two labels, a RESULTS.md ledger line, and a line of the third sitting's seat raw, printed by `grep` and `sed`". **FAIL.** The two labels (calls 358, 375) and the four outputs (calls 302, 358, 375, 466) hold. The ledger line was printed by `/usr/bin/grep -n` (call 302). But the seat raw's line was printed by `awk 'NR==31||NR==33||NR==40'` (call 466); no `sed` printed it. Fix: "printed by `grep` and `awk`".

46. entry.md:222–224, a marker word in tool output. **IMPRECISE.**
    - The three Bash outputs (calls 304, 466, 640) and the ten SendMessage results to the pod session hold.
    - A bracketed test over every tool result in the window finds more:
      - two Read results: n-build's generator script (call 118) and a memory note (call 279);
      - the pod session's title in two get_session results (calls 432, 507), two list_events results (calls 454, 455) and one list_sessions result (call 465);
      - the pod's name in the get-pod result (call 601).
    - Fix: append "; and, beside the shell, the pod session's title in two get_session, two list_events and one list_sessions result, two Read results (n-build's generator script and a memory note), and the pod's name in the get-pod result".

47. entry.md:230–231: "and `git ls-files --others -- data/n` into `grep -c`, a count printed (0)". **IMPRECISE.**
    - It ran in three battery-window checks (calls 68, 146, 168), each `| /usr/bin/grep -c 'campaign'`, each printing 0.
    - The other reads under `data/n` hold: call 215's `git show e1be6d9:data/n/reports/time.json | jq` for the two pins; calls 577–578; call 585's `git check-attr` of three paths; call 575's counts by class; and the existence tests in calls 115, 146, 156 and 168.
    - Fix: "and `git ls-files --others -- data/n` into `grep -c` in three battery-window checks, each printing a count (0)".

48. entry.md:233–237, git forms without item 3's pathspec. **IMPRECISE.**
    - These hold: four screens (calls 18, 75, 106, 278); blame in two (calls 280, 356); the no-index numstat (call 53); every status and grep scoped.
    - But one of the three `git log -1 --format` calls (call 280) names a raw, not a commit (`--date=short -- <raw>`).
    - And `git show <rev>:<file>` also showed `.gitignore` (calls 91, 93, 96), `LOCK-n.md` (calls 215, 436) and two root design documents, ADDENDUM-n3 and PROPOSAL-n (call 243).
    - Fix: "`git log -1 --format` of named commits in two commands and of one named raw in a third, which printed its commit's date by `--date=short`; `git show <rev>:<file>` of RESULTS.md, raws, scripts, `.gitignore`, `LOCK-n.md`, two root design documents and `data/n/ids/MANIFEST.json` (into `shasum`);".

49. entry.md:238–241, leak-count patterns. **FAIL.**
    - These hold: the volume host's name as a fixed string in six (calls 14, 16, 73, 104, 358, 375); the user's name bracketed, and an email-domain pattern, in 13 each; an IPv4 pattern in eight.
    - Missing (a): the account name was typed once plain, unbracketed, as a fixed pattern (call 562, the close window's count, "…: 0 lines").
    - Missing (b): the volume host's name also appears unbracketed in an `-E` alternation in three more leak counts: call 10 (`c26b117`'s values-check raw assembly), call 40 (the `fcab1e5` grant's counts) and call 95 (the `e1be6d9` window's counts). It is also a form-count pattern in call 2.
    - Fix: "the volume host's name, unbracketed, as a fixed string in six commands (…) and in an `-E` alternation in three (`c26b117`'s values-check raw assembly and the leak counts of the `fcab1e5` and `e1be6d9` windows), and in a form-count pattern in a tenth; the user's name, bracketed, in 13, and once typed plain as a fixed pattern (the close window's count, 0 lines); an email-domain pattern in 13; …".

50. entry.md:242–243, the command-text counts. **CONFIRMED.** By `jq` over `bash.jsonl`: account name 281, home root 176, temporary root 203, session-id forms 227.

51. entry.md:244–248, writes outside the repository. **CONFIRMED.**
    - Call 38's `diff` printed "No such file or directory" for `fence_<pid>.txt` under another temporary path.
    - Call 39's name-only `ls` found it under the temporary root; `head -c 60 | od -c | head -2` printed 32 bytes; then `rm -f` removed it.
    - Edit ran 31 times (24 memory, 7 scratch) and Write 31 times (30 scratch, one new memory note).

52. entry.md:249–258, commands that did not run as meant. **FAIL.**
    - These hold: calls 38–39; 77–79; 95→96; 140→141; 250–251→252; 436→437; 528→529→532; 577→578; and calls 253 and 345 ending with exit 1 on a `grep -c` of 0.
    - Wrong: "two anchor asserts in the third sitting's draft that compared whole entry heads". Call 334 printed four failing asserts, at lines 222, 469, 709 and 711 (three entry heads and one entry's last line). Each compared a `cut -c` prefix, which counts bytes and split a multibyte dash. Call 335 re-checked all four by prefix and two lines whole.
    - Missing (a): call 61 counted the find's paths over absolute paths, and the pattern matched every path through the temporary root's `tmp` segment ("117 under an overlay, tmp or gitest folder"). It was re-run on relative paths in call 62 (0). The session's own log (call 66) recorded it as a slip "for the next entry".
    - Missing (b): a `head -0` in call 250 printed "illegal line count -- 0", without effect.
    - Fix: replace "two anchor asserts … re-checked by prefix" with "four anchor asserts in the third sitting's draft (three entry heads and an entry's last line) whose `cut -c` prefixes, counted in bytes, split a multibyte dash, re-checked by prefix". Then add: "one count at the seat-block window's re-check of n-build's find, run over absolute paths, which matched every path through the temporary root (117), re-run on relative paths (0); a `head -0` that printed an error, without effect;".

53. entry.md:259–262, counts and tools beside item 1. **IMPRECISE.**
    - These hold: `wc -c` in 25; `od` in 7; `awk` in 33; `bash -n` in 2 (calls 565, 568); `date +%F` once (call 610, with a TZ prefix).
    - But `git cat-file` ran in seven (calls 14, 16, 73, 96, 104, 275, 576); call 593's match is log text.
    - Output went to `/dev/null` in 22; calls 2 and 3 hold it only in count patterns.
    - The list omits `git diff --quiet`, which ran in ten calls (40, 54, 68, 91, 115, 146, 156, 168, 376, 588): seven with item 3's pathspec, one on `.gitignore`, one on RESULTS.md and one with the pathspec in an array.
    - It also omits one `git diff --numstat` with item 3's pathspec at `9792e14`'s verify (call 275), which printed per-file line counts of RESULTS.md and two raws.
    - Fix: "`git cat-file` in seven; … output to `/dev/null` in 22; `git diff --quiet` in ten, seven with item 3's pathspec; and one `git diff --numstat` with item 3's pathspec (line counts of RESULTS.md and two raws)".

54. entry.md:263: "network: the pushes and `ls-remote` to origin; one RunPod API read (`get-pod`)". **IMPRECISE.** The get-pod read (call 601) is an MCP call, not a shell command, but it sits in the list of shell forms. Fix: drop it here and add "one RunPod API read (`get-pod`);" to the beside-the-shell list (lines 268–274).

55. entry.md:264–265: "… no other interpreter ran;". **IMPRECISE.** The six screens hold (calls 18, 75, 106, 278, 380, 587, each `nice -n 19 /usr/bin/python3 -I` running `screen4.py` and `gl5.py`). No other Python ran; the other "python" matches are patterns, log text and a rebuilt command's text. But `awk` ran in 33 commands, as line 260 itself says. Fix: "no other Python ran".

56. entry.md:266–267: "…; none is in any committed text;". **IMPRECISE.**
    - Committed text does hold the home root: `git grep -l` at HEAD with the full pathspec finds it in 252 files, 248 of them raws. RESULTS.md line 22727 already held it at `098218c`.
    - It also holds the temporary root, in 44 files.
    - None of this was added in the window: every gate and verify count over the added lines was 0 (calls 14, 16, 73, 104, 275, 379, 562). No linked-session id is committed.
    - Fix: "none entered any text committed in this window (each gate's and verify's count over the added lines: 0);".

57. entry.md:268–274, the calls beside the shell. **CONFIRMED.**
    - SendMessage 43 (31 to n-build, 10 to the pod session, 2 to n-analyzer); ToolSearch 13; ReadNotifications 5; list_events 6; get_session 2; list_sessions 1; TaskStop 3; Agent 1 (call 341).
    - Read 71: memory 20, n-build's scratch 21, notes folder 8, own scratch 10, task outputs 3, repository 9; the size refusal at call 621 was re-read by offset.
    - Edit 31 (24/7); Write 31 (30/1).
    - With update_plan 127, wrap_up 38 and get-pod 1, the total is 672.

58. entry.md:276–288, the `78cd6eb` values-checker's departures. **CONFIRMED.** The checker's raw says each of them at lines 404–471. `78cd6eb`'s entry (RESULTS.md:410–415) holds the session's own departures but not the checker's.

59. entry.md:292–293 and msg_src.txt:1: "The commit-time count of the home-folder prefix over the staged diff is 0." **NOT CHECKABLE.** Nothing is staged yet.

60. entry.md:293 and msg_src.txt:1: "The coordinating session ran nothing on a model." **CONFIRMED.** For the window and for its shell calls after the sweep, the only interpreter runs are the six screens; no driver, analyzer or model process ran.

### The close line

61. close.md:1–5, its head and the raw's sha256. **CONFIRMED.**
62. close.md:6–8, the run and its close. **CONFIRMED.** PI item 1; raw §0–§1.
63. close.md:9, §2's observations. **CONFIRMED.** PI item 1.
64. close.md:10–13, what follows. **CONFIRMED.** PI items 2 and 5; raw §3.4–§3.5 and §5.
65. close.md:14, this commit's departures. **CONFIRMED.** PI item 4.

### The routing raw

66. routing_raw.md:1 and 3, its title and lead. **CONFIRMED.**

67. routing_raw.md:5: "2,327 bytes …; sha256 `58c9074a…eef3`", no paste markers, no question before the message, the six items compared with §6, and a 36-line fence. **CONFIRMED.**
    - The record extracted by `jq -r` is 2327 bytes and 36 lines with sha256 `58c9074a…eef3`. The string has no trailing newline; `jq` adds the last.
    - The content is a plain string with origin "human", and 0 paste-marker matches.
    - Against §6 (raw lines 49–65), items 1, 2 and 5 are longer, and items 3, 4 and 6 are reworded or equal.

68. routing_raw.md:9–46, the fenced block. **CONFIRMED.** `sed -n '10,45p'` equals the `jq -r` extraction by `cmp`, with the fences at lines 9 and 46.

### The message

69. msg_src.txt: ASCII only, with the co-author line last. **CONFIRMED.** `LC_ALL=C grep -c '[^ -~]'` gives 0. The file has 3 lines: line 2 is empty and line 3 is the co-author line, ending in a newline.

70. msg_src.txt:1, its other claims: the raw by path and `7f5020b9...37f4`, the routing raw, the run's figures, items 1–3 and 5, and "672 calls, 299 shell commands". **CONFIRMED** against the entry and the raw; see items 7 and 59 for the rest.

### The placement

71. RESULTS_draft.md: HEAD's RESULTS.md with the entry after line 23 and `close.md` after line 319. **CONFIRMED.**
    - The working RESULTS.md equals `git show HEAD:RESULTS.md` by `cmp`.
    - Line 22 is the Log heading and line 23 is blank; line 319 is the last text line of `95cd461`'s entry and line 320 is blank.
    - Rebuilt from `sed -n` ranges plus the two files, it equals the draft by `cmp`: 39968 + 294 + 14 = 40276 lines.

72. entry.md and close.md: no line over 118 characters except link lines. **CONFIRMED.** `LC_ALL=en_US.UTF-8 /usr/bin/grep -n '.\{119,\}'` finds only entry line 8 and close line 3, both link lines. The longest other line is 118.

73. entry.md ends with a blank line and close.md does not. **CONFIRMED.** By `tail -c 4 | od -c`, the entry ends ") . \n \n" and the close line ends "r t . \n".

## Observations

1. The seat's raw puts the pod's stop after the close commit's push. §0 (line 8) says "the pod stopped after the commit's verify and the push (§5)", and §5 (line 45) says "stopped after the close commit and its push". In the transcript, the stop message (call 590) and get-pod's "EXITED" (call 601) come before push #25 (call 614). The entry's item 5 gives the transcript's order. The raw is committed unchanged, so the seat may want to know.
2. The entry uses "ans24" (line 22) without defining it; the seat's raw defines it in its header.
3. At the `fcab1e5` window, call 40 printed "markers 2; plain campaign 1" for the spec raw (located at call 41). So the committed `results/raw/2026-11-23_n-campaign_spec.md` holds two marker-word lines and the campaign folder's plain name, as content, not argv. The entry's "leak counts 0 in all eight texts" is right, but it is silent on these.
4. `78cd6eb`'s entry (RESULTS.md:412–415) held "a name-only listing of n-build's launch folder" for this entry. This entry names no listing. A name-only `ls` is an item 1 form, and the window lists n-build's folders by name in about a dozen calls.
5. Shell reads of n-build's scratch have no class of their own: hashes by `shasum -c`, line counts, `cmp`, `sed`, `grep` and pruned finds. The Read tool's 21 reads there are listed for completeness.
6. `forms.sh` counts mentions, so log text and count patterns inflate it. The entry corrected several counts (pgrep 23→19, python 25→6, find 29→2 unpruned, awk 35→33, od 9→7, wc -c 26→25). It did not correct the memory folder (58), `git cat-file` (8) or `/dev/null` (24); see items 41 and 53. A next sweep could count runs instead.
7. The `tail` misfire (call 95) came from a wrong path, `camp/build/` for `camp/`, as the session's own log says (call 100). The entry gives its effect, an empty offset, which is accurate.
8. Call 436's zsh `:s` misfire also printed a `cut` error ("values may not include zero"). It is part of the listed misfire.
9. The heading "Items 1–2 (N), relayed verbatim to n-build and the pod session" undersells the relays: the pod session's sub-bullet covers item 5, and both messages carried all six items whole.
10. The session kept working after the sweep, with shell calls such as re-hashing n-build's PINs, survey report and brief, and printing lock, probe and cells lines. Those calls fall under `@AFTER@` and are not checked here.

## My own departures

- **Read tool, 12 calls:**
  - the brief;
  - `entry.md`, `close.md`, `routing_raw.md`, `msg_src.txt` and the three relay files;
  - `forms.sh` and `forms_out.txt` in `<sweep>`;
  - the seat's raw in `<repo>/results/raw` (whole);
  - the third sitting's values-check raw (lines 404–480).
- **Bash, 148 calls.**
  - **`<transcript>`, 31 calls.**
    - One `wc -l` of the whole file (72,124 lines).
    - One `/usr/bin/grep -n -F` of the PI record's timestamp, printing a line number.
    - `sed -n` ranges around the PI's record, piped into `jq`.
    - `/usr/bin/grep -F` over the whole file, piped into `jq`, for:
      - the window's tool-use ids, in three passes compared with the sweep's by `sort -u` and `diff`;
      - the size refusal, error results, the PI's typed records, "Push it" records and plain-text user records;
      - tool results holding a marker word (bracketed pattern);
      - five background task ids by `grep -c -F`, and their notification statuses;
      - chosen tool results (three task-output Reads, the delta Read, get-pod);
      - the pod session's re-touch and "Holding" messages, n-build's "stand-in" answer, and the session's shell calls after the sweep.
    - These printed record texts:
      - the PI's messages and the records just before the routing message;
      - the session's closing text and wrap-up input;
      - its tool calls with commands and outputs, Read inputs and SendMessage inputs (for `cmp`);
      - fragments of the pod session's and n-build's messages.
  - **`<sweep>` files, 98 calls:**
    - `jq` over its `.jsonl` files;
    - `head -c 600` of `calls_since.jsonl`, `head -3` of `view.tsv` and `sed` of `errors.tsv`;
    - `wc -l` of the sweep files.
    - These printed commands and outputs, mostly with the roots masked by `gsub`, but some outputs showed local roots, session ids and n-build's scratch paths.
  - **Other `<own>` files:**
    - a name-only `ls` of the folder and of `sweep/`;
    - `shasum` and `wc -l` of the brief;
    - `cmp` of the relays, blocks, side files and the fence against `pi_msg_raw.txt`;
    - `wc -c` and `wc -l` of the relays;
    - `tail -c` into `od -c` of the entry, the close line and the message;
    - character widths by `LC_ALL=en_US.UTF-8 /usr/bin/grep` and a zsh `${#l}` loop;
    - `LC_ALL=C /usr/bin/grep -c` for non-ASCII.
  - **Repository, outside `data/`:**
    - `shasum`, `wc -c` and `wc -l` of the seat's raw.
    - `git status --porcelain -- results/raw` (scoped).
    - `git rev-parse HEAD` and `git rev-parse origin/main`.
    - `git show HEAD:RESULTS.md` into `cmp`, `wc -l` and `sed -n` (one file, three times in one call).
    - `sed -n` slices of RESULTS.md into `cmp` for the rebuild.
    - RESULTS.md by `/usr/bin/grep -n` and `sed -n` ranges (402–410, 424–428, 1236–1240, 1289–1294, 24–319, 321–480, 410–424).
    - The third sitting's values-check raw: `git ls-files --error-unmatch`, `wc -l` and `grep -n` of its headings.
    - The third sitting's seat raw: `grep -n -E`, and `sed -n 31p | grep -o`.
    - `git diff --numstat` of three commit pairs with the full pathspec (per-file line counts).
    - `git rev-list --parents -n 1 95cd461 | wc -w` (printed 2; no pathspec).
    - `git grep -l` over HEAD with the full pathspec: five counts, and one grouping by folder (folder names with counts).
    - `git diff --name-only` for six commits with the full pathspec. Each of the 32 changed files was shown by `git show <commit>:<file>` into `grep -c`, printing counts only.
    - `git show 098218c:RESULTS.md` and `git show HEAD:RESULTS.md` into `grep -c`, and one `grep -n | cut` that printed a line number.
- **Counts outside item 1:**
  - `wc -c` in three calls;
  - about 15 `wc -l`, the transcript's among them;
  - many `grep -c`;
  - `od -c` in two;
  - one `git rev-list | wc -w`.
- **Redirects:** `>/dev/null` in two calls (four redirects). No file was written anywhere.
- **Patterns:**
  - guard markers only in bracketed form;
  - the user's account name and the volume host's name only in bracketed form;
  - one email-domain word typed plainly in one call's pattern;
  - an IPv4-shaped regex in one call;
  - the campaign folder only as `m[f]3`;
  - the words `pgrep`, `ps -p`, `kill -0` and `ssh` typed only inside `jq` patterns (none of them run);
  - an 8-hex prefix of n-build's scratch-folder id typed in masking patterns in about eight calls;
  - a bracketed fragment of the coordinating session's id in one `git grep`.
- **Command text:** the account name and the coordinating session's id appear in nearly every Bash call, through the `<own>`, `<transcript>` and `<repo>` paths.
- **Tool output:**
  - Outputs showed local roots, the account name, session ids and n-build's scratch paths.
  - Marker words appeared in outputs: the pod session's title in listed records, RESULTS.md's head line, a memory-note line, a raw's file name, and the pod's name in get-pod.
  - The volume host's name and the campaign folder's plain name appeared in outputs (the coordinating session's command and output texts).
  - None of these is copied here.
- **Failures without effect:**
  - In two calls zsh read `echo ====` (and `echo ======`) as `==`. Each printed "not found" and exited 1, so the rest of the call did not run; I re-ran it in the next call.
  - One `jq` select on a key the file lacks printed nothing.
  - One `git grep -F` with a bracketed pattern was read literally (0) and was re-run as `-E` in the same call (44).
  - Several `grep -c` counts printed 0, with no effect on exit status.
- **Not done:**
  - no write, no network, no git write;
  - no `ps`, `pgrep` or `stat` run;
  - no interpreter but `shasum` and `jq`, and `jq` only over `<transcript>` (directly, or through `sed -n` or `/usr/bin/grep -F` of it) and `<sweep>`'s `.jsonl` files;
  - nothing under `data/*/ckpt`, `data/*/reports` or `data/m[f]3` listed, read or hashed;
  - the staging folder, the memory folder, n-build's scratch, the pod session's folders and the notes folder not touched (their names appear only in my outputs and in masking patterns).

## Tallies

- Items: 73. CONFIRMED 53; IMPRECISE 15 (items 7, 16, 22, 29, 39, 41, 43, 44, 46, 47, 48, 53, 54, 55, 56); FAIL 4 (items 40, 45, 49, 52); NOT CHECKABLE 1 (item 59).
- Observations: 10.
