# The coordinating session's notes on the seat's second sitting of 2026-11-23: the blind values-check, as returned, with every disposition

2026-11-23. Code (the coordinating session).

**What was checked.** One blind pass by a subagent over the entry's draft (sha256 `72837de7…7161`, 242 lines), the close line on `098218c` (`66fb2205…3c0c`, 13 lines), the routing raw (`bbfbd957…9b94`, 26 lines), the commit message's draft (`0b83f3b6…5cab`, 3 lines), and their placement in a draft of the new `RESULTS.md` (`2848cb43…b18e`, 38,674 lines).

**The checker's brief** was a file in the coordinating session's scratch folder, named in its Agent call by path (sha256 `8345bd0d…5fd1`, 104 lines). It is not committed, because it names the local roots in full. It:
- named the sources: the seat's raw; the PI's "Route as given" and the question it answers, and the PI's two other messages in the span, in the coordinating session's transcript; the repository at `098218c`; the coordinating session's sweep (211 calls, 93 of them shell commands) and its files; the messages in and out; n-build's notes in the notes folder; the files in n-build's scratch that the entry cites, with its two overlays; and the coordinating session's screen, push and window folders;
- quoted the list of record v2's items 1–5 verbatim, from `2026-11-10_list-of-record-v2_design-to-code_answers.md`, lines 18–22 (equal by `cmp` to the last brief's);
- barred any interpreter but `shasum` and `jq`, any write, any network, `ps` and `pgrep`, a whole-tree `git status`, anything under `data/*/ckpt`, `data/*/reports` or the campaign folder, the memory folder, the steered cells' folder, and the guard markers and the campaign folder's plain name in any command text;
- barred passing any path holding a marker word to a command as an argument: such paths go on stdin only; and named n-build's overlays, some of whose paths hold one, to be listed only by the pruned `find` and hashed with the paths on stdin;
- set item 3's pathspec, with the campaign folder's exclusion, on every git command over the tree or a range;
- barred from the report the network volume's server host name, as from the committed record.

**The report** is in §3, extracted verbatim by `jq` from the subagent's one hand-back (328 lines, sha256 `8b135885…5ee6`), byte for byte, with no mask. It names no local root. Its `<repo>`, `<own>`, `<nbuild>`, `<notes>` and `<transcript>` are the repository, the coordinating session's scratch, n-build's scratch, the sessions' shared notes folder and the coordinating session's transcript.

**Totals:** 57 items (40 CONFIRMED, 11 IMPRECISE, 3 FAIL, 3 NOT CHECKABLE) and 12 observations.

## 1. Dispositions

- **Item 40** (FAIL): fixed, in the checker's words: one `shasum -c` whose list named `test_after13.sh` as `after13_test.sh`, one `diff` over a wrong line range, and one `cmp` of n-build's quotation of item N.2, each added to the commands that did not run as meant.
- **Item 43** (FAIL): fixed, in the checker's words: the campaign folder's plain name in tool output twice, the Read of the seat's raw and one `grep` of the routing log, a sub-bullet of its own.
- **Item 44** (FAIL): fixed, in the checker's words: the unpruned `find`s in n-build's overlays, a sub-bullet of its own, with a pointer from the draft-1 group.
- **Item 9** (IMPRECISE): applied: "are owed as the handoff's §5 has them".
- **Item 16** (IMPRECISE): applied, in the checker's words, with observation 1.
- **Item 21** (IMPRECISE): applied, in the checker's words.
- **Item 23** (IMPRECISE): applied: three path substitutions, five tokens, and `9382644b…c9a3`, the note re-hashed by tool (82 lines).
- **Item 25** (IMPRECISE): applied: "+1,291 -30", with the note's ASCII hyphen.
- **Items 30, 32, 35, 41 and 42** (IMPRECISE): applied, in the checker's words.
- **Item 54** (IMPRECISE): applied to the message, in the checker's words, with the three new classes added to its departures.
- **Items 4, 46 and 51** (NOT CHECKABLE): the commit's own claims, met at the commit, and the extractions after the sweep, in the entry's sub-bullet after the checked sweep.
- **Observations 1, 2, 4, 5, 6, 7, 8 and 10:** applied: the message to n-build that said all 23 by `shasum -c`; the two slips in step 13's messages, without effect; the account name through the temporary root's project-folder segment, 82 of 93; git's numstat of draft 1 as n-build's figure at draft 2's window; the tracking ref for "origin" before the push; the pod relay's line on step 14's BUILD; the name-only listings of its scratch in the last group; and the plain stage name in four `pgrep -f`s.
- **Observations 3, 9, 11 and 12:** noted: n-build's departures list changed after the read, and the entry gives the figure at the read, with the checker's and a later one; the three PI records; the routing raw's long lines, which no width rule binds; and the sweep file's `@tsv` form.

## 2. Edits after the check

- The dispositions above, and the rewraps of the bullets they lengthened.
- The entry's sub-bullet after the checked sweep, the checker's departures, the values-check bullet, and the message's fill.
- The edits were checked by tool, by `diff` of each checked draft against its final text. Each hunk is a disposition above, a rewrap, or a fill of a placeholder.
- No second full pass was made.

## 3. The report as returned

# Blind values-check: the coordinating session's notes on the seat's second sitting of 2026-11-23 (after `098218c`)

Scope: I checked `entry.md`, `close_098218c.md`, `routing_raw.md`, `msg_src.txt` and `RESULTS_draft.md` in `<own>/notes8/` against the seat's raw, `<transcript>`, `<repo>` at HEAD `098218c`, the notes in `<notes>`, `<nbuild>` and `<own>`. I did not report on the placeholders.

Numbering convention: "cmd N" is the N-th Bash call in `<own>/notes8/sweep/calls_since.jsonl`, counting from 1. That file holds 93 Bash calls, from 07:59:37Z to 02:52:15Z. Times are UTC from the transcript. The commits carry a −0500 offset, so every time from 08:05Z on 11-23 to 02:52Z on 11-24 falls on PI date 2026-11-23.

## Items

### The seat's raw and the read (entry.md:6–16)

**1. entry.md:7–8.** Claim: the raw is "sha256 `e07fba2c…eba9`, 15,293 bytes, 68 lines".
- **CONFIRMED.**
- Evidence: `shasum -a 256 | cut -c1-8`/`-c61-64` printed e07fba2c / eba9. `wc -c` printed 15293 and `wc -l` printed 68. The file ends with a newline.

**2. entry.md:8–12.** Claim: the seat read `098218c`'s entry, its check raw and `LOCK-n.md` from a new thread picked up from its handoff in the project. The raw was placed untracked after the check that preceded the "Build on the PINs" relay. n-build's seat-block values-checker found it, and n-build reported it and held its request.
- **CONFIRMED.**
- Evidence: raw line 3 and §4. Cmd 46 (00:36:41Z) printed 0 untracked under results/raw, and the relay went at 00:38:10Z. n-build's message at 01:31:40Z says "the seat block's values-checker found it" and "I am holding the block's commit window request".

**3. entry.md:12–13.** Claim: the raw was "re-hashed … read it whole, told n-build that the self-test window it had granted stood, and put the routing to the PI".
- **CONFIRMED.**
- Evidence: cmd 69 printed e07fba2c…eba9, 68, 15293. A Read of the raw ran at 01:32:09Z. The message at 01:33:33Z says "The draft-1 self-test window stands as granted". The wrap-up at 01:33:55Z asked the PI.

**4. entry.md:13–14.** Claim: "It is re-hashed equal before this commit and committed here by path."
- **NOT CHECKABLE**: it describes the future commit.
- For the record, it re-hashed equal at cmd 87 (02:49:55Z) and again in my check.

### What the raw rules and records (entry.md:17–33)

**5. entry.md:18–21.** Claim: LOCK-n v1.0 of record, `59e0b1bc…00aa`, 1453 lines; four edits; v0.1 beneath; the three lines; the root draft gone; "D_n 2026-12-15 met, 22 days off; the three commits pushed".
- **CONFIRMED.**
- Evidence: `git show 098218c:LOCK-n.md | shasum` printed 59e0b1bc…00aa, 1453 lines, and at `221b806` 88d9fe7b…e9d5, 1058 lines. Raw §0 and §1 match. `[ -e LOCK-n-v1.0-draft.md ]` printed no. Origin is 098218c.

**6. entry.md:22–23.** Claim: three dated notes, "not edits: a lock file is never edited after its commit".
- **CONFIRMED** against raw §0, §1.2 and §4.

**7. entry.md:24–27.** Claim: §2's eight points, named so that the PINs can carry them and the ruling is one sitting.
- **CONFIRMED.**
- Evidence: raw §2 items 1–8, the §2 lead line and §0's "so that the ruling is one sitting".

**8. entry.md:28–30.** Claim: §3, `098218c`'s departures inert, and the seat's unfiltered `git status --short`.
- **CONFIRMED** against raw §3.

**9. entry.md:31–33.** Claim: "…and p, q and WORKFLOW v1.1 stand as the handoff's §5 has them."
- **IMPRECISE.** Raw line 47 says "owed as the handoff's §5 has them".
- Fix: "and p, q and WORKFLOW v1.1 are owed as the handoff's §5 has them."

### The routing and relays (entry.md:34–57)

**10. entry.md:34–37.** Claim: the ask "four times on PI date 2026-11-23", the two buttons, the messages, the PI's answer and the reading of the defaults.
- **CONFIRMED.**
- Evidence: jq over the wrap_up calls found the ask exactly four times (01:33:55, 01:39:32, 02:28:06 and 02:32:26Z) with ["Route as given","Hold it"].
- The user record whose whole text is "Route as given" is at 02:49:04Z, which is 21:49 at −0500 on 11-23.
- "defaults in brackets; your words are the record" is raw line 49.

**11. entry.md:38–41.** Claim: items 1–3 relayed verbatim to n-build and the pod session, with the quotes.
- **CONFIRMED.**
- Evidence: each numbered line of the 02:50:19Z and 02:50:24Z messages matched a raw line by `grep -x -F`. Section heads were sent without bold.

**12. entry.md:43–48.** Claim: what went with the items (5–7 and the next-sitting line to n-build, 6 to the pod session, the close-lines sentence to both), the order n-build proposed, and the pod session's lines.
- **CONFIRMED.**
- Evidence: the message texts. n-build had written "I would rebase the texts onto your commit". The next-sitting line differs from the raw only by its bold label.

**13. entry.md:49–50.** Claim: item 4 relayed verbatim to n-analyzer.
- **CONFIRMED.**
- Evidence: the 02:50:28Z message line equals raw line 59. The recipient's label is n-analyzer's.

**14. entry.md:51–57.** Claim: items 5, 6, 7 and the next sitting.
- **CONFIRMED** against raw lines 62, 63, 66 and 68.

### Since `221b806` (entry.md:58–146)

**15. entry.md:59–72.** Claim: `221b806`'s close: the mask at 267, the 449-line raw, the fills, the build, 38,281 = 37,949 + 318 + 14, "A A A M", 899 = 73+45+449+318+14, GATE PASS, one parent `6912d6e`, `2276c5a9…f371`, VERIFY PASS, the screen (1 commit, 4 file-diffs, 903 lines, CLEAR, gitleaks 0, gl5 0), and n-build told.
- **CONFIRMED.**
- Evidence: the outputs of cmds 2–11; the message at 08:04:42Z.
- My own git checks: `rev-list --parents` gives 6912d6e. `git diff --numstat` gives 332/449/45/73 added, 0 removed. RESULTS.md is 38281 lines at 221b806 (2276c5a9…f371) and 37949 at 6912d6e.

**16. entry.md:73–74.** Claim: "its 23 inputs at their sha256s by `shasum -c` against the coordinating session's list".
- **IMPRECISE.**
- Evidence: cmd 13 printed "OK count: 22 of 23" and "lock13/after13_test.sh: FAILED open or read". The list named the file wrongly. Cmd 14 then checked `test_after13.sh` by its own shasum (4b3d2385…387b, 48 lines).
- Fix: "its 23 inputs at their sha256s, 22 by `shasum -c` against the coordinating session's list and the 23rd, `test_after13.sh` (listed there as `after13_test.sh`), by its own `shasum` in the next command (`4b3d2385…387b`);"

**17. entry.md:74–86.** Claim: draft 11 against §3, edits.diff `564c6cd6…1994`, after13 read, the 625-line dry run with GATE PASS, the rulings, the two changes, and the delta.
- **CONFIRMED.**
- The delta details: `8e5545e4…8667`, 219 lines; `db6282c9…023a`, 109 lines; 8 of 8; `ff8cc031…e1bb`; `e991092d…c7ef`, 138 lines; `80362c5c…8fc0`; `9c908c13…214e`, which `patch -R` turns into `4b3d2385…387b`; 19 of 19; 642 GATE PASS.
- Evidence: cmds 14, 16, 18–20; the 08:16:37Z and 08:21:27Z messages; the delta note's lines 217–218; my shasum of each file; `cat` of the gate_dry.txt files.

**18. entry.md:87–96.** Claim: the question asked three times; "Go: commit step 13" saved (`6d16ddc0…6c72`, 18 bytes) and relayed; the fill (`4129ee67…db4c`, 98 lines); entry `078e5339…2a92` (138 lines, 11,925 bytes); message `2a404b1a…2674` (3 lines, 1,920 bytes, ASCII); 26/26 and 5/5; 18c18 and 1c1; the tree; the grant.
- **CONFIRMED.**
- Evidence: the wrap_up calls (three); the user record at 22:36:54Z; `od -c` and shasum of the saved word; outputs of cmds 32 and 34–36; my own diff (18c18, 1c1), shasum and `wc -c`.

**19. entry.md:97–103.** Claim: `098218c` verified: one parent, the hashes, 38,419 = 38,281 + 138, `6d025f17…af4c`, 642 = 395 + 138 + 109, VERIFY PASS; the screen (3 commits, 11 file-diffs, 2,486 lines, CLEAR, gitleaks 8.30.1 0, gl5 exit 0).
- **CONFIRMED.**
- Evidence: cmds 37, 38 and 40; my `rev-list`, `git show | shasum | wc -l` and numstat over the named paths (395/138/109, 0 removed).

**20. entry.md:104–109.** Claim: push #20's item quote, the range, the pre-push checks, exit 0, 0 ahead and 0 behind, and the record `fcbc7c47…2b0e` (24 lines).
- **CONFIRMED.**
- Evidence: cmds 39 and 40; rt23a line 42 at HEAD; my shasum and `wc -l` of `<own>/push20/push_record20.txt`.

**21. entry.md:110–112.** Claim: "survey brief (`c940d92d…6f02`, 105 lines), report (`7f728f96…43d1`, 342) and departures list (`1d5e68dd…b6e2`, 32), each hashed in n-build's scratch at the sha256 the note gives".
- **IMPRECISE.** The note gives only the brief's and the report's sha256s; its lines 4–5 hold no departures entry. n-build's message calls departures.md "a running list", with no hash. Cmd 42 printed 1d5e68dd…b6e2, 32 lines at 23:23Z.
- Fix: "with its survey brief (`c940d92d…6f02`, 105 lines) and report (`7f728f96…43d1`, 342), each hashed in n-build's scratch at the sha256 the note gives, and its departures list hashed there at the read (`1d5e68dd…b6e2`, 32 lines; a running list the note does not hash)".

**22. entry.md:112–123.** Claim: the anchors opened; the starred eight; the question asked once; the word saved (`2232e004…a989`, 17 bytes); the checks before the relay; the relay's contents.
- **CONFIRMED.**
- Evidence: cmds 44–46 and 49; ★ lines CP2, CP6, CP8, CP9, CP11, CP12, CP13 and CP16 in the note; one wrap_up; the 00:38:10Z message.

**23. entry.md:124–125.** Claim: "its command G-VER run 4's with exactly three paths changed (a token `diff` against G-VER's draft-4 note, `9382644b…`)".
- **IMPRECISE**, on two counts:
  - The abbreviation lacks its last four characters. My shasum gives 9382644b…c9a3, and the note is 82 lines.
  - The token diff in cmd 64 shows five changed path tokens: the temporary folder, the overlay's driver, and the run's .txt, .err and .exit. Cmd 63 printed "CMD EQUAL after the three substitutions".
- Fix: "its command G-VER run 4's with exactly three path substitutions — the temporary folder, the overlay's driver and the run files' stem — five tokens by a token `diff` against G-VER's draft-4 note, `9382644b…c9a3`."

**24. entry.md:125–132.** Claim: draft 1 `9b51bb18…64c0` (7,570 lines) equal to its overlay copy and to HEAD's driver `55885e65…385f` (6,224 lines) plus the delta `c9cd183d…03f7` (1,590 lines, 24 hunks); the delta's content; the overlay of 175 files, 174 HEAD blobs, `LOCK-n.md` v1.0; the count 764 (35, a loop of 12, 46, 1, 717).
- **CONFIRMED.**
- Evidence: cmds 64–66; `RESULTS.md:1485` at HEAD reads "717/717".
- My own check: a pruned find inside each overlay, `git hash-object --stdin-paths` with paths on stdin, and `comm` against `git ls-files -s` under the pathspec. Only scripts/n_sessions.py differs from HEAD. `LOCK-n.md` is 59e0b1bc…00aa.
- My `sed -n`/`grep -c` over `_camp_selftest` counted 35 static checks and 12 loop cases. 24 hunks; the pin moves to 59e0b1bc….

**25. entry.md:132–134.** Claim: `its "+1,291 −30" counted the non-blank added lines`.
- **IMPRECISE.** The quotation is not byte-exact. n-build's note (line 20) has an ASCII hyphen-minus: "+1,291 -30". The entry uses U+2212 (`od -c` shows 342 210 222). The figures are right: cmd 65 counted 1291 non-blank and 85 blank added lines.
- Fix: `its "+1,291 -30" counted the non-blank added lines`.

**26. entry.md:134–136.** Claim: closed at 764/764; `cbfeff64…40f9`, `e3b0c442…b855` (empty), `28d3b9e8…c320` ("exit 0"); the temporary folder empty; unchanged; no "campaign" name under data/n.
- **CONFIRMED.**
- Evidence: cmds 74–76; my shasum; `ls -A camp/tmp | wc -l` printed 0.

**27. entry.md:137–146.** Claim: draft 2: `cbebd433…3fd2` (118 lines), `7249b88f…d9b5` (7,831), `12aa2015…4bf6` (1,863), `84745a7f…b178` (771), the numstat figures, the restores asserted, `committed_bytes`, the overlay, 774 (43, a loop of 14, 56), and the close at `5aa33ca8…def0`.
- **CONFIRMED.**
- Evidence: cmds 78–82 and 84–85.
- My own check: a grep of the diff shows `cells.load_cell` and `m_resume.atomic_write_json` restored in `finally` and asserted. My counts were 43 and 14.

### Departures (entry.md:147–233)

**28. entry.md:148–150.** Claim: "211 calls … 93 of them shell commands, the sweep itself the last … No guard marker".
- **CONFIRMED.**
- Evidence: my own jq over the transcript (assistant tool_use after the boundary, up to 02:52:15.961Z) gave 211 calls, 93 of them Bash, none sidechain.
- A bracketed, case-insensitive marker count over all 211 inputs printed 0.

**29. entry.md:151–190.** Claim: group counts 11, 9, 16, 5, 4, 13, 10, 5, 4, 6, 3 and 7.
- **CONFIRMED.** They sum to 93, and each group maps onto consecutive commands: 1–11, 12–20, 21–36, 37–41, 42–45, 46–58, 59–68, 69–73, 74–77, 78–83, 84–86 and 87–93.

**30. entry.md:166–167.** Claim: "the note's and the three scratch files' sha256s, with the routing log's lines by `sed -n`; the log's precedent lines;".
- **IMPRECISE.** Cmd 42 read the routing log with `grep -n -o`. The `sed -n` read is cmd 43, the precedent lines.
- Fix: "the note's and the three scratch files' sha256s, with the routing log's lines by `grep -n -o`; the log's precedent lines by `sed -n`;".

**31. entry.md:192–194.** Claim: `pgrep -l python`/`-il python` in three commands (each printing the PID and name); `kill -0 8051` in two; `ps -p 8051 -o pid=` in five; `pgrep -f` in six, counts only.
- **CONFIRMED.**
- Evidence: cmds 7, 36 and 37 printed "8051 python3.12". `kill -0` ran in cmds 36 and 37. `ps -p` ran in cmds 49, 65, 75, 82 and 85; the heredoc mentions in cmds 58, 68, 77, 83 and 86 are prose. `pgrep -f … | wc -l` ran in cmds 36, 37, 65, 75, 82 and 85.

**32. entry.md:195–196.** Claim: "its transcript, read in 11 commands … and its tool calls and their outputs".
- **IMPRECISE.** The count of 11 is right: cmds 22, 23, 24, 29, 30, 31, 55 and 90–93. But no command in the span printed a tool output from the transcript; none selects tool_result records. The outputs were extracted only after the sweep, at 02:53:17Z.
- Fix: "printing record texts: the PI's messages and their times, its own relays and asks, and its earlier commands and their times;".

**33. entry.md:197–199.** Claim: `ls -t` in two commands (scratch's top folder, first 25, plus one dated folder; the notes folder, first 5) and `ls -l` of two scratch folders.
- **CONFIRMED.**
- Evidence: cmds 27, 87 and 28. The ls -l output shows sizes, dates and the owner field.

**34. entry.md:200–201.** Claim: the campaign folder's plain name in two heredocs.
- **CONFIRMED.**
- Evidence: a bracketed count gave cmds 73 and 77, both inside `cat >> "$F" <<'EOF'` prose.

**35. entry.md:202–203.** Claim: the memory folder in 19 commands, by "`grep`, `sed -n`, `wc -l`, `tail -c` into `od -c`, and 7 appends".
- **IMPRECISE.** The counts of 19 and 7 are right: cmds 21, 26, 41–43, 47, 48, 56–58, 60, 61, 68, 70, 73, 77, 83, 86 and 88, with appends in cmds 58, 68, 73, 77, 83, 86 and 88. But `tail -n 2` also read the log in cmds 56 and 58.
- Fix: "`grep`, `sed -n`, `wc -l`, `tail -n` (in two commands) and `tail -c` into `od -c`, and 7 appends to its routing log by heredoc."

**36. entry.md:204–206.** Claim: line counts by git (`git show --numstat` with the pathspec; `git diff --numstat 6912d6e 221b806` without it; `--no-index` over the drivers).
- **CONFIRMED.**
- Evidence: cmds 37, 89 and 79. Cmd 89 printed RESULTS.md and three raws.

**37. entry.md:207–208.** Claim: `git ls-files --others -- data/n` into `grep -c` in the two closes, printing 0.
- **CONFIRMED.** Cmds 75 and 85.

**38. entry.md:209–212.** Claim: the user's name in bracketed patterns in seven commands, and the host pattern once in a sed.
- **CONFIRMED.**
- Evidence: bracketed name patterns in cmds 5, 7, 9, 16, 19, 35 and 37. The host pattern is in those seven plus cmd 2's sed mask.

**39. entry.md:213–215.** Claim: home root 65, temporary root 49, session ids 56, the notes folder's path 13.
- **CONFIRMED** by fixed-string counts.

**40. entry.md:216–218.** Claim: "commands that did not run as meant, with no effect: one `awk` … and one `grep` …".
- **FAIL**: the list is incomplete. 221b806's entry lists "`cmp`s at wrong offsets" under this class, so these belong here too:
  - (a) Cmd 13's `shasum -c` named `after13_test.sh` and printed "22 of 23" with one FAILED open. The file was re-checked in cmd 14.
  - (b) Cmd 19 ran a `diff` over a wrong line range. It compared the new raw's lines 2–11 and 14–94 with v1's 2–11 and 13–94, which is one line short after the 12c12,13 hunk. It printed "DIFFER".
  - (c) Probably also cmd 16's `cmp` of n-build's quotation of N.2 against rt23a:24–26. It printed "differ" because of the continuation indent and was re-run in cmd 17 with whitespace folded. Whether this one counts is the seat's call.
- Fix: append "; one `shasum -c` in step 13's window whose list named `test_after13.sh` as `after13_test.sh` (22 of 23 OK, the 23rd checked by its own `shasum` next); one `diff` in the delta's check over a wrong line range (the new raw's 14–94 against v1's 13–94), which printed "DIFFER", the change being checked by the hunk headers in the same command; and one `cmp` of n-build's quotation of item N.2 against rt23a:24–26 after stripping `    > `, which printed "differ", re-run with whitespace folded".

**41. entry.md:219–221.** Claim: "its scratch (the check lists, the three words, the verify, screen and push-#20 folders, the self-test windows' listings, HEAD's driver patched into copies, and this commit's drafts and sweep files)".
- **IMPRECISE**, on two counts:
  - It leaves out the shell writes of `221b806`'s build and verify files in notes7: vc_report_masked.md (cmd 2), entry_final.md, msg.txt and vc_raw.md (cmds 3 and 5), RESULTS_new.md and R_head.md (cmd 6), and V_parent.md and V_commit.md (cmd 9).
  - "This commit's drafts" were written after the sweep (from 02:56Z). In the span, notes8 holds only the three words and calls_since.jsonl.
- Fix: "its scratch (`221b806`'s build and verify files in its notes7 folder, step 13's check lists and diffs, the three words, the verify, screen and push-#20 folders, the self-test windows' listings, HEAD's driver patched into copies, and the sweep's `calls_since.jsonl`)".

**42. entry.md:222–225.** Claim: the counts and tools, including "`git cat-file` in four (`-p` into a parent count, `commit` into `cmp`, `blob` into `shasum`)".
- **IMPRECISE**, minor. Every count checks out:
  - `wc -c` ran in 11 commands. `wc -m` ran in one, cmd 81 (seven lines: 121 121 122 122 120 121 120); the mention in cmd 83 is a heredoc.
  - The non-ASCII counts ran in seven commands, `od -c` in three, `cat -et` in one, `awk` in six (cmds 65, 66, 79, 80, 81 and 92; the mentions in cmds 68 and 83 are heredocs) and `/dev/null` in nine.
- But `blob` also went into `wc -l` (cmd 11) and into scratch files compared by `cmp` (cmd 9).
- Fix: "`git cat-file` in four (`-p` into a parent count, `commit` into `cmp`, `blob` into `shasum`, `wc -l` and two scratch files compared by `cmp`)".

**43. entry.md:226–227.** Claim: "its tool output showed local roots and the account name inside paths, the `ls -l` output's owner field, and session ids".
- **FAIL**: a missing class. Two tool outputs in the span named the campaign folder plainly:
  - the Read of the seat's raw at 01:32:09Z, whose lines 3, 35 and 37 name it;
  - cmd 60's `grep` of its routing log, whose matched line names it in prose.
- The seat's §3 lists exactly this class among `098218c`'s departures ("the three tool outputs that named the campaign folder plainly").
- Fix: add "**the campaign folder's plain name in tool output** twice: the Read of the seat's raw, whose head and §3 name it, and one `grep` of its routing log in draft 1's window, whose matched line names it in prose; nothing under it was listed, read or hashed;".

**44. Missing class: unpruned `find`s (entry.md:172–177 and 191–227).**
- **FAIL.** Cmds 65, 75, 80 and 85 ran unpruned finds in n-build's overlays: `find . -type l | wc -l` in cmds 65 and 80, and `find . -name '__pycache__' | wc -l` in all four. Each printed 0.
- Item 1 permits only the pruned form. The entry says only "the overlay by the pruned `find`".
- Precedent: cmd 60's output shows the routing log recording an earlier "UNPRUNED find over n-build's overlay … in place of item 1's pruned form" as a departure.
- Neither overlay holds a ckpt or reports directory: the pruned count is 0, by cmds 65 and 80 and by my own check.
- Fix: add "**unpruned `find`s** in n-build's overlays, outside item 1's pruned form: `find . -type l` in two commands and `find . -name '__pycache__'` in four (draft 1's window and close, draft 2's window and close), each into `wc -l`, counts printed (0); neither overlay holds a `ckpt` or `reports` directory;". In the draft-1 group, add "(with unpruned symlink and `__pycache__` counts, below)" after "the pruned `find`".

**45. entry.md:228–233.** Claim: the calls beside the shell: 16 messages (14/1/1), four schema loads, two notification reads (none queued), two event reads, Read 26 (4/6/10/5/1), Edit 20 (4/16), Write 2.
- **CONFIRMED.**
- Evidence: per-call targets from the transcript. The recipient labels are n-build, the pod-watch session and n-analyzer. Both ReadNotifications printed "No queued notifications."

**46. entry.md:239–241.** Claim: committed by path; the commit-time home-prefix count is 0; "ran nothing on a model"; not pushed.
- **NOT CHECKABLE**: these describe the future commit.
- "Ran nothing on a model" holds for the span: the only Python was `/usr/bin/python3 -I` running the screens.

### The close line

**47. close_098218c.md:1–5.** Claim: the heading, the link and `e07fba2c…eba9`, on "Route as given".
- **CONFIRMED.**

**48. close_098218c.md:6–13.** Claim: the readings of §1/item 1, §1.2, §4/item 3, §2/item 2 and §3/item 5.
- **CONFIRMED** against raw lines 7–8, 16, 42, 54–56 and 62.

### The routing raw

**49. routing_raw.md:1–3.** Claim: the header, the raw's sha256, 15,293 bytes and 68 lines, and the cites.
- **CONFIRMED.**

**50. routing_raw.md:5.** Claim: no block pasted; §5 is lines 49–68; the box ask four times with the same words and buttons; bold in four messages in the two forms; plain words in four short replies; the PI's line is the first button's words.
- **CONFIRMED.**
- Bold messages: 01:34:07Z (form 1, after a list of the routing items with their defaults), then 01:39:36, 02:28:11 and 02:32:29Z (form 2).
- Short replies: 01:38:18, 01:41:54, 02:31:29 and 02:39:45Z.
- The only PI record is the 14-character "Route as given".

**51. routing_raw.md:5.** Claim: "extracted by `jq` … a departure its entry declares".
- **NOT CHECKABLE.** The jq extractions are real: post-sweep commands at 02:54:33Z (the asks) and 02:54:57Z (the texts and the PI's record). But because they ran after the sweep, they fall to the entry's @AFTER@ text, which I did not review.

**52. routing_raw.md:9–26.** Claim: the three quoted lines and "Route as given".
- **CONFIRMED** word for word against the wrap_up asks, the text blocks (bold stripped) and the user record.

### The commit message

**53. msg_src.txt.** Form.
- **CONFIRMED.** It is ASCII only (0 non-ASCII lines), line 2 is empty, the co-author line is last, and the one placeholder is @VCMSG@.

**54. msg_src.txt:1.** Claim: "…two ls -t listings and one ls -l of scratch…"
- **IMPRECISE**, minor. One `ls -t` listed the notes folder, not scratch. The message's other claims match the entry.
- Fix: "two ls -t listings (its scratch and the notes folder) and one ls -l of scratch".

### Placement and sweep files

**55. RESULTS_draft.md.**
- **CONFIRMED.** `cmp` of {HEAD 1–23; entry.md; HEAD 24–160; close; HEAD 161–} against the draft printed equal.
- 38,419 + 242 + 13 = 38,674. HEAD line 23 is blank, line 160 is the last text line of `098218c`'s entry and line 161 is blank. R_head.md equals HEAD's RESULTS.md.

**56. Widths and endings.**
- **CONFIRMED.** Only the link line is over 120 characters in the entry (line 7) and in the close (line 3), under UTF-8. The entry ends "\n\n" and the close ends ".\n".

**57. The sweep files.**
- **CONFIRMED.**
  - calls_since.jsonl equals a fresh jq extraction from the transcript.
  - bash_ids.txt equals its ids.
  - bash_since.tsv equals `[time, command with "\n"→" ⏎ "] | @tsv`.
  - bash_results_full.jsonl equals the transcript's tool results for those ids.
  - The last line of notes7/calls_last.jsonl carries 07:59:27.110Z.

## Observations

1. The 08:16:37Z message to n-build already said "all 23 … by `shasum -c`", the same overstatement as item 16.
2. The relay of the step-13 word (22:38:53Z) quoted the question as "should step 13's commit go ahead, or wait?", which is not the box's words. The grant (22:46:46Z) wrote the manifest's abbreviation with five tail characters ("…bb1bb"). Neither is in the entry.
3. `camp/departures.md` has changed since the read. It is now 55faff31…05c5, 147 lines. The entry's figure is the one at the read (item 21's fix says so).
4. The account name stands in 82 of the 93 commands' text: 65 through the home root and 17 more through the temporary root's project-folder segment. The entry's counts of 65 and 49 are right as worded.
5. The git numstat figure "+1,377 −31" sits in draft 1's paragraph, but it came from draft 2's request and window (cmd 79). It is fine as narrative.
6. "Origin" before the push (the grant's tree check and the "Build" relay's checks) means the tracking ref, not `ls-remote`. Only the push used `ls-remote`.
7. The pod relay also said step 14's BUILD is in progress with two model-free laptop self-tests passed. The entry's summary omits this, which is harmless.
8. Cmd 88 also ran name-only `ls` of scratch (its top folder, notes7 and notes8). This is permitted but not described.
9. The three PI words in the span are the only PI records in it. The other user records are cross-session messages, six side-session events and two compaction summaries.
10. In cmds 65, 75, 82 and 85, `pgrep -f n_sessions` was unbracketed. It printed 0 each time.
11. The routing raw's lines 3 and 5 exceed 120 characters. No width rule binds raws, and rt23a's lines do the same.
12. bash_since.tsv uses jq's @tsv form (backslashes doubled, tabs escaped) with " ⏎ " spaced. Read raw, it is not the bare-⏎ form the brief describes.

## My own departures

- **Transcript.** I ran 27 commands of `/usr/bin/grep -F`/`-o` into `jq` over `<transcript>`, and one `wc -l` of it, which printed 65,880.
  - Printed: the PI's three messages and their times; the 13 wrap-up asks and buttons; the assistant text blocks of the routing span; all 16 SendMessage inputs (eight in full); n-build's incoming messages (heads, five in full or part); user-record heads; the post-sweep calls and the 02:54:57Z extraction's output.
  - The output also showed session labels (one holding a guard marker, in output only), session ids and the memory folder's path inside command texts.
- **jq beyond the named files.** Once over `bash_results.jsonl` (keys) and once over `bash_ids.txt` (as an id list). jq over `notes7/calls_last.jsonl` and the two `gl.json` (length 0 each).
- **git without item 3's pathspec**, each on single files or narrow paths outside `data/`:
  - `git rev-list --parents -n 1` of three commits;
  - `git show <rev>:<file>` of LOCK-n.md, RESULTS.md (into `sed -n` and `cmp`), four raws and rt23a;
  - `git diff --numstat` over seven named paths of `098218c` and `221b806` (printed 395/138/109 and 332/449/45/73, 0 removed);
  - `git diff --name-only ef105f1 HEAD -- valence_core/n/` and `2834c2d HEAD -- scripts/n_sessions.py` (0 each);
  - `git hash-object` of three working files, and `git rev-parse`.
  - `git log -3 --format` and `git diff --name-status` ran with the pathspec.
- **Counts beside item 1.**
  - `wc -c` in four commands: the seat's raw 15,293; the words 18/17/14; n-build's filled entry 11,925 and message 1,920; the first sitting's seat raw 12,654.
  - `wc -l` in about 20 commands, `od -c` in four, non-ASCII line counts in two (0 each) and widths under `LC_ALL=en_US.UTF-8` in one.
  - `ls -A camp/tmp | wc -l` printed 0.
- **Listings.**
  - Name-only `ls` of my own scratch folders: notes8, sweep, push20, two screen folders, step13-window, step13-verify, camp-st1 and d2.
  - Name-only `ls` of n-build's lock13 (with raws, commit, v1, v1/commit, v2 and v2/commit) and camp.
  - The pruned `find` run inside each overlay, its output piped.
- **Overlays.** I ran `shasum` of each overlay's `LOCK-n.md` and `scripts/n_sessions.py` with the path as an argument, not on stdin; neither path holds a marker. That was 8 invocations in one command. Blobs were hashed only by `git hash-object --stdin-paths` with paths on stdin. I opened no overlay file.
- **Command text.**
  - The home root with the account name appeared in most commands, as paths and as `sed` mask patterns. The temporary root, which holds the account name, and session ids (the scratch roots, the transcript's path, the notes folder's id) appeared in many.
  - The account name and those ids were fixed-string count patterns in two commands. Bracketed name patterns appeared in one.
  - The volume host's name was a plain fixed-string count pattern in one command, together with `runpod`, IPv4 and port regexes; the bracketed form was in one. Bracketed email-domain patterns were in one, and bracketed marker words in two.
  - The campaign folder appeared only as quoted `m[f]3`.
- **Output to `/dev/null`** in eight commands. **`date`** once, which printed the local time and offset.
- **Commands that did not run as meant**, each with no effect:
  - my first transcript selection matched every record holding the phrase (printed empty texts) and was refined;
  - my first form of bash_since.tsv's rebuild mismatched and was re-derived in three more commands;
  - one compare ended with exit 1 because its second variant was unequal, as expected;
  - one `grep -o -b` gave contexts shifted by multibyte characters;
  - one command carried a stray environment assignment before `tr` (no awk ran).
- **Tool output** showed local roots with the account name, session ids, a marker word in one session label, and the campaign folder's plain name once, in my Read of the seat's raw.
- **Read tool** six times: the brief, the four drafted texts and the seat's raw.
- I wrote no file, used no network, ran no `ps`, `pgrep` or Python, and read nothing under ckpt, reports, the campaign's folder, the steered cells' folder or the memory folder.

## Tallies

57 items: 40 CONFIRMED, 11 IMPRECISE, 3 FAIL (items 40, 43 and 44), 3 NOT CHECKABLE. 12 observations.
