# The coordinating session's notes on the seat's second sitting of 2026-11-21: the blind values-check, as returned, with every disposition

PI date 2026-11-21. Code (the coordinating session).

**What was checked.** One blind pass by a subagent over the entry's draft (sha256 `326cc97f…62eb`, 130 lines), the three close lines (on `91f0d35`, `2a1adad7…c422`, 17 lines; on `4fdcdcc`, `e9d21488…4488`, 12; on `2ca24e8`, `e078b484…0f8f`, 12), the routing raw (`269fa500…d01d`, 52 lines), and their placement in a draft of the new `RESULTS.md` (`412af727…a340`, 35,370 lines).

**The checker's brief** was a file in the coordinating session's scratch folder, named in its Agent call by path and sha256 (`1d1591d2…9532`, 102 lines). The checker re-hashed it equal before it began. It is not committed, because it names the local roots in full. It:
- named the sources: the seat's raw; the PI's routing message and the PI's "Push" in the coordinating session's transcript; the repository at `101026c`; the coordinating session's sweep file, its other tool calls and its three relays; and its push folder;
- quoted the list of record v2's items 1–5 verbatim, from `2026-11-10_list-of-record-v2_design-to-code_answers.md`, lines 18–22 (equal by `cmp`);
- barred any interpreter but `shasum` and `jq`, any write, any network, `ps` and `pgrep`, a whole-tree `git status`, anything under `data/*/ckpt`, `data/*/reports` or the campaign folder, the memory folder, and the guard markers and the campaign folder's plain name in any command text;
- barred passing any path holding a marker word to a command as an argument: such paths go on stdin only;
- set item 3's pathspec, with the campaign folder's exclusion, on every git command over the tree or a range;
- barred reading the screen script's pod list, and printing any address or port.

**The report** is in §3, extracted verbatim by `jq` from the subagent's one hand-back (516 lines, sha256 `e4e815c5…b669`). It names no local root. Its `<repo>`, `<own>` and `<transcript>` are the repository, the coordinating session's scratch and the coordinating session's transcript. Its two `local_` strings name a kind of string; neither is an id.

**Totals:** 68 items (58 CONFIRMED, 7 IMPRECISE, 1 FAIL, 2 NOT CHECKABLE) and 10 observations.

## 1. Dispositions

- **Item 39** (FAIL): fixed, in the checker's words: the class of `awk` over the coordinating session's own scratch files, in five more commands, with `tail -c` and `od -c` of the PI's extracted message and `grep -c` counts over the drafts and the sweep files.
- **Item 13** (IMPRECISE): applied, in the checker's words: the order went to n-build in full; the pod session was sent the box's part.
- **Item 27** (IMPRECISE): applied: the check read the span's second sweep, the 35th command; an earlier one, the 28th, swept the first 28.
- **Item 35** (IMPRECISE): applied: the pod id's `git grep` ran twice in one command, once counted and once with five names printed.
- **Item 38** (IMPRECISE): applied: four `pgrep`s, in three commands.
- **Item 42** (IMPRECISE): applied: the Read tool once on the memory index.
- **Item 45** (IMPRECISE): applied: the re-screen's four outputs among the scratch writes.
- **Item 64** (IMPRECISE): applied, in the checker's words, to the close line on `2ca24e8`: Code's and the values-checker's departures are inert, and §3 does not name the survey's own (the spec raw's §4), which the seat lists among its reads.
- **Items 4 and 47** (NOT CHECKABLE): the commit's own facts, met at the commit.
- **Observations:**
  - 1, applied: the quotation follows "both read in full", as the seat's "second sitting; the first sitting of a fresh thread".
  - 2, met: the entry names the bracket "[yours]" of the seat's routing block, which leaves the push the PI's.
  - 3, applied: a departures line for the outputs that name the account.
  - 4, applied: (g) stands apart from the inert classes in the close line on `91f0d35`.
  - 5, applied: "the closing message of that turn".
  - 6, applied: `git rev-list` is marked as a range form without the pathspec.
  - 7, met: the last sweep's file holds one JSON string per command, which reverses.
  - 8, met: the entry's counts are of what ran.
  - 9 and 10, noted.

## 2. Edits after the check

- The dispositions above; the entry's values-check bullet and the values-checker's departures, from §3; and the last sweep of the coordinating session's own shell commands, made after the check, as a sub-bullet of the entry's departures. That sub-bullet also says what the commands after the check were for, among them the reading of G-TIME-n's launch files v2 and their relay to the pod session on the PI's answer on the folder.
- The edits were checked by tool, by `diff` of each checked draft against its final text. Each hunk is a disposition above, a filled placeholder, the last sweep's sub-bullet, or a rewrap after an edit.
- No second full pass was made.

## 3. The report as returned

```text
# Blind values-check: the coordinating session's notes on the seat's second sitting of 2026-11-21 (after `101026c`)

I re-hashed the brief with `shasum -a 256 | cut -c1-8` and `cut -c61-64`. It gives `1d1591d2` … `9532`, as stated.

The coordinating session's commands are cited as #1–#35, in their order in `bash_sweep1.tsv`; item 68 checks that file against the transcript. Times are the transcript's UTC stamps. "raw:N" is line N of the seat's raw. "RESULTS.md line N" is a line of `git show 101026c:RESULTS.md`.

## Items

1. **entry.md:1–3** – "the PI's routing, "PI: route as given"; three close lines (item 6); the relays; push #15's line (item 9)"
   - **CONFIRMED.**
   - jq over `<transcript>` finds one user record (string content) that starts with "PI date 2026-11-21 — design seat, second sitting.". It ends "PI: route as given".
   - Its item 6 names close lines on 2ca24e8, 4fdcdcc and 91f0d35. Its item 9 names push #15 and its C.5 line.

2. **entry.md:6** – "(sha256 `813de3db…6157`, 32,674 bytes, 84 lines)"
   - **CONFIRMED.**
   - `shasum -a 256` gives `813de3db` by `cut -c1-8` and `6157` by `cut -c61-64`. The full digest equals the one in the PI's message.
   - `wc -c` gives 32674 and `wc -l` gives 84.

3. **entry.md:6–7** – "the seat's ruling on the blocks of `2ca24e8` (Q1–Q7) and `4fdcdcc` (Q8), each read in full ("second sitting; the first sitting of a fresh thread")"
   - **CONFIRMED.**
   - raw:3 names both blocks, "both in full".
   - The quotation is verbatim at raw:3 (`grep -c -F` gives 1). See observation 1.

4. **entry.md:7–8** – "It was placed untracked over the bridge and is committed here by path, re-hashed equal before the commit."
   - **NOT CHECKABLE.** The commit-time re-hash has not happened yet.
   - What can be checked holds:
     - raw:3 says "Placed untracked over the bridge".
     - `git ls-files` finds no tracked file at the path; `--others --exclude-standard` lists it.
     - #23 printed "sha EQUAL to the PI's", 32674 bytes, 84 lines. My re-hash is also equal.
   - Fix: none; the commit's gate re-hashes.

5. **entry.md:8–10** – "The PI's message routing it, which ends "PI: route as given", is committed as [`2026-11-21_second-sitting_pi-routing.md`](…)"
   - **CONFIRMED.**
   - "PI: route as given" is the last line of the record's text.
   - The target path is free: `git ls-files` and `--others` print nothing for it.

6. **entry.md:10–11** – ""item N" is item N of that message, whose items follow the raw's routing block (§6)"
   - **CONFIRMED.**
   - The PI's items 1–9, under N, A, C and D, follow the numbering and sections of raw:69–84.

7. **entry.md:13–14** – "Q1–Q7 stand as built (§1.1–§1.7). In §0's words: "No PIN moves the driver, so the BUILD at `91f0d35` is the driver of record and no v2 script or manifest is needed.""
   - **CONFIRMED.**
   - The quotation is raw:7, in §0 (`grep -c -F` gives 1).
   - raw:7 also has "Q1–Q7 stand as Code built them (§1.1–§1.7)".

8. **entry.md:15–18** – Q8 is option (iii), amended. The two steered cells' JSON are copied back by hash to a laptop folder outside the repository that the launch files name, held under item 2. They are committed with the campaign's cells at step 14's close, before the pod stops. The shadow cell, the report and the artifact go with G-TIME-n's entry.
   - **CONFIRMED.**
   - raw:8 and raw:29–33.

9. **entry.md:19–20** – "The smoke's two ends, as the coordinating session named them at `101026c`, are accepted (§2). The seat adjudicates either on the smoke's report, identity and out file."
   - **CONFIRMED.**
   - raw:39.
   - RESULTS.md lines 71–74, in 101026c's entry: "For the seat: the smoke's two ends (the launch review's F3)".

10. **entry.md:21–22** – after COMPLETE, G-VER's launch files follow without waiting; the cap is set at LOCK-n v1.0 (§1.7).
    - **CONFIRMED.**
    - raw:10 and raw:27.

11. **entry.md:23** – "(a)–(g) inert, and (h) the seat's own, with ledger (87) (§3, §5)"
    - **CONFIRMED.**
    - raw:43, raw:52 and raw:61–63.

12. **entry.md:24–31** – "Items 1–4 (N), relayed verbatim to n-build and the pod session, as the PI gave them", with the quotations "[as ruled]", "No change to the driver at 91f0d35; no new BUILD.", "Q8 = option (iii), amended" and "[go]"
    - **CONFIRMED.**
    - jq takes the PI's 17-line block from "N. n-build (and the pod session)" to item 4's "[as ruled]". It is a substring of the SendMessage texts of 00:35:40 and 00:35:50 (true, true), and not of 00:35:53.
    - By the session names in the transcript, the recipients are n-build, the pod session (its name begins "Pod watch") and n-analyzer.
    - Each quotation is found once in the PI's text, reading line breaks as spaces.
    - What each relay carried:
      - n-build: "PI: route as given"; the raw's hash, bytes and lines; items 1–4; the form note of (c); §3 (d)'s classing; items 7 and 8; D.9; the order; and two window rules.
      - The pod session: "PI: route as given"; the raw's hash and lines; items 1–4; item 8; "Nothing runs on the box yet…"; §1.8's line.
      - n-analyzer: "PI: route as given"; item 5; the raw's hash and lines.

13. **entry.md:33–35** – "With them went the order. This commit comes first. Launch note v2, and any other changed file, comes to the coordinating session first, which reads the set and then relays it to the pod session; nothing goes to the box before that relay."
    - **IMPRECISE.**
    - The order in this form is in n-build's message alone:
      - "My commit comes first (C.6)…"
      - "Launch note v2, and any other changed file, comes to me first…"
      - "Nothing goes to the box before that relay."
    - The pod session's message has only the box part ("Nothing runs on the box yet. … I read the set, then relay it to you."). It does not say "This commit comes first".
    - Fix: "With them went the order, to n-build in full: this commit comes first; launch note v2, and any other changed file, comes to the coordinating session first, which reads the set and then relays it to the pod session; nothing goes to the box before that relay. The pod session was sent the box's part: nothing runs on the box until that relay."

14. **entry.md:35–36** – "The pod session was also sent §1.8's line…: "no session lists, opens or hashes them before the campaign's cells are committed, the copy-back's own hash check excepted""
    - **CONFIRMED.**
    - The quotation is raw:31 (`grep -c -F` gives 1).
    - It is in the pod session's message (true), and in neither of the other two.

15. **entry.md:37–38** – item 5 relayed verbatim to n-analyzer: "Nothing; v7 of record; v1.0's lock: line and the gate line verbatim at step 13. [as ruled]"
    - **CONFIRMED.**
    - The quotation is in the PI's text (1).
    - n-analyzer's message carries "5. Nothing; … [as ruled]" (true).

16. **entry.md:39–43** – the quotation of item 6
    - **CONFIRMED.**
    - I extracted it with `sed -n '39,43p' | tr | sed` (526 characters).
    - It is found in the PI's text, reading line breaks as spaces. `grep -c -F -f` with the pattern on a `/dev/fd` file gives 1.

17. **entry.md:44–46** – "The two standing lines are the coordinating session's, from `5f62dd1` and `101026c`, and it keeps both."
    - **CONFIRMED.**
    - RESULTS.md lines 261–262, in 5f62dd1's entry: "now reads every new untracked seat raw that such a listing names before it relays a PI decision…"
    - RESULTS.md line 50, in 101026c's entry: "From here, a per-file check over a list that may hold marker-named paths passes the paths on stdin".
    - raw:45 (a) and raw:46 (b).

18. **entry.md:47–48** – the form note "an index check that prints "ok" on two empty operands is vacuous; it asserts non-empty operands first.", "relayed to n-build for the kit's next version, Code's call"
    - **CONFIRMED.**
    - The note is raw:47 (1).
    - n-build's message quotes it with its lead-in, "One form note for the kit's next version, Code's call:" (true). It is in neither other message.

19. **entry.md:49** – "The coordinating session's own gates assert non-empty operands, as its gate for `101026c` already did." (earlier-work claim)
    - **CONFIRMED.**
    - #6, the gate, tests `[ -n "$got" ]` before it compares the staged name-status.
    - It tests `[ ${#a} -eq 40 ]` before each index comparison `[ "$a" = "$b" ]`.
    - Its result has two "ok … = its source" lines, "added 556 (want 556 = 199 + 357)" and "GATE PASS".

20. **entry.md:50–51** – "§5's fix names a line in the seat-handoff skill's pickup step; no item of the routing assigns it."
    - **CONFIRMED.**
    - raw:63 has "the seat-handoff skill's pickup step says so in one line" (1).
    - A jq scan of the PI's text for skill or handoff finds neither; it finds only "ledger (87)".
    - raw:65–84 has no line with "skill".

21. **entry.md:52–53** – the quotation of item 7; "Relayed to n-build; not yet asked."
    - **CONFIRMED.**
    - The quotation is in the PI's text (1) and in n-build's message (true).
    - No request came in the span. n-build's later message (00:48:26, after the entry was drafted) says it will ask for gread-bench's window after the run.

22. **entry.md:54–55** – the quotation of item 8; "Relayed to n-build and the pod session."
    - **CONFIRMED.**
    - It is in both messages: n-build's without "8.", the pod session's with it.

23. **entry.md:56–58** – the quotation of item 9; "The next push waits for this commit, G-TIME-n's entry and the PI's word, behind the pre-push screen."
    - **CONFIRMED.** The quotation is found once. See observation 2.

24. **entry.md:59–61** – the C.5 line
    - **CONFIRMED.**
    - The PI's "Push":
      - One user record's whole text is "Push", at 2026-11-21T22:27:24Z (PI date 2026-11-21).
      - That is before #14 (22:30:10Z). #14 printed "c9d35e2..101026c … -> main" and "push exit=0".
    - Commits: `git log --format='%h'` of the range, with the full pathspec, gives 5 ids.
    - The screen: `screen15b.txt` and #10's result show six classes, each "inside: 0 -> CLEAR".
    - gitleaks:
      - #16 printed "gitleaks: 8.30.1".
      - jq over `gl15b.json` gives one finding: generic-api-key at `scripts/n_sessions.py`:3787, commit 91f0d35.
      - `gl5_15b.txt` has "('outside', 'generic-api-key', 'digest:file') x 1" and "gl5 exit=0".
    - Default rules: no `.gitleaks.toml` or `.gitleaksignore` is tracked or untracked, and neither GITLEAKS_CONFIG variable is set in this shell.

25. **entry.md:62–63** – "5 commits, 19 file-diffs and 5,652 added lines (messages included), every class CLEAR. The screen in `101026c`'s entry covered `c9d35e2..5f62dd1`, as §4 notes."
    - **CONFIRMED.**
    - The figures are in `screen15b.txt` line 1 and in #10's result.
    - `git log --name-only` of the range, with the full pathspec, lists 19 file-diffs. So none is in an excluded path.
    - RESULTS.md line 100: "The screen for the push (`c9d35e2..5f62dd1`, …): 4 commits, 17 file-diffs, 5,092 added lines".
    - raw:56.

26. **entry.md:64–65** – before the push, origin was c9d35e2 by `git ls-remote`, no hook could run, and no new seat raw was under results/raw; after it, origin is 101026c by `git ls-remote`, the tracking ref equal.
    - **CONFIRMED.**
    - #12's result: "remote: c9d35e2…"; "hooksPath []"; no non-sample hook; the results/raw untracked and modified lists are empty.
    - #15's result: remote, tracking ref and HEAD are all 101026c…; "0 0".

27. **entry.md:67–69** – "That is 35 commands to the first sweep, which the values-check read, itself the 35th"
    - **IMPRECISE.**
    - 35 is right:
      - `cmp` of the transcript's first 35 main-thread Bash calls after 17:45:48.378Z, written in the file's own form, against `bash_sweep1.tsv` is equal.
      - There were 41 such calls at my read, and none is a sidechain call.
      - The threshold is the first field of line 8 of `notes2/bash_after_22.tsv`, and is itself a main-thread Bash call.
    - The ordinal is wrong:
      - #28 ("Sweep my shell commands since 101026c's last sweep into scratch") was an earlier sweep. It printed "commands since 101026c's last sweep: 28" and marker and name counts of 0.
      - So the 35th is the second sweep. The entry's own "the sweeps", at line 106, says as much.
    - Fix: "That is 35 commands to the sweep that the values-check read, itself the 35th; an earlier one, the 28th, swept the first 28. The commands after the last sweep are this commit's own."

28. **entry.md:69–70** – "No guard marker and no plain campaign name was in their text (a bracketed sweep)."
    - **CONFIRMED.**
    - jq `test` over the 35 texts, with bracketed patterns, gives 0 and 0. #35 printed 0 and 0.

29. **entry.md:70–71** – "Six looped, each over a literal list (of scratch files, raws, name pairs or search words), none holding a path with either"
    - **CONFIRMED.**
    - The six:
      - #6, over name pairs.
      - #13, #16 and #34, over scratch files.
      - #22, over raws.
      - #35, over search words.
    - One more pattern match, #17, is "(for the next entry)" inside an `echo` string.

30. **entry.md:72–76** – 101026c's own commands: `grep -c` counts, `awk` widths, `diff`, and `tail -c` with `od -c`; a `sed -n` read; the builds with `cat`, `printf`, `awk`, `cmp` and `sed -n` ranges; the asserts and two `cp`; the staging, the gate, the commit and its verification.
    - **CONFIRMED.** These are #1–#9.

31. **entry.md:77–78** – the `"$C:results/…"` run failed by zsh's :r modifier; a second run with `${C}` passed.
    - **CONFIRMED.**
    - #8's result: "fatal: Not a valid object name 101026c…dbesults/raw/…", then "FAIL vc raw" and "VERIFY FAIL".
    - #9's result: "ok … (671137b8…84b4); VERIFY PASS (all checks)".

32. **entry.md:79–81** – the re-screen; `git log --format='%h %s'` without item 3's pathspec; jq over gitleaks' report twice in that command and once in a later one
    - **CONFIRMED.**
    - #10 has jq `'length'` and `jq -r '.[] …'`. #16 has one jq.

33. **entry.md:82–90** – push #15's checks before it, the push, the checks after it, and the push record with `shasum` and `gitleaks version`
    - **CONFIRMED.**
    - These are #12–#17.
    - `push_record15.txt` (26 lines) equals #17's printed form by `cmp`.

34. **entry.md:91–94** – `cat-file -p` and `commit`; `cat-file blob`; `diff --cached` and `diff`, with item 3's pathspec, piped to `grep -c`; `hash-object` against `rev-parse` in three commands; `ls-remote` in three
    - **CONFIRMED.**
    - `cat-file` forms are in #8 and #9. The `diff` forms are in #6 and #8.
    - `hash-object` ran in #3, #4 and #6.
    - `ls-remote` ran in #12, #15 and #23. Its name also appears in #17's echo strings and #21's heredoc, which did not run it.

35. **entry.md:94–96** – "one content search with item 3's pathspec, `git grep -l -F` of the box's pod id over the working tree, counted (69 files) and its first five names printed"
    - **IMPRECISE.**
    - #31 ran the search twice: once piped to `wc -l` (printed 69), and once to `head -n 5` (printed five names).
    - Fix: "and one content search with item 3's pathspec, `git grep -l -F` of the box's pod id over the working tree, run twice in one command: once counted (69 files), once with its first five names printed;"

36. **entry.md:97–101** – jq over its transcript in eight commands; "`5f62dd1`'s entry (observation 8) says its next message to the PI corrects the two times; that message did, by these reads, and no committed text carries them" (earlier-work claim)
    - **CONFIRMED.**
    - jq ran over the transcript in #18, #19, #24, #28, #30, #32, #33 and #35: eight. (#10 and #16 ran jq over gitleaks' report.)
    - RESULTS.md lines 493–496: "Observation 8 is met: … the coordinating session's next message to the PI corrects them."
    - The real times: the PI's "Build on the PINs" is stamped 07:40:50Z (02:40:50 EST), and its relay 07:43:58Z.
    - The 13:43:31Z message says "came at 02:42" and "at 03:37".
    - The 16:56:42Z message says "about 02:40, not 02:42" and "about 02:43, not 03:37".
    - `git grep -c -E` of the time strings at HEAD, with the full pathspec, finds no 2026-11-21 text. RESULTS.md's four hits are other events, in entries of 2026-09-27 and 2026-11-09.
    - See observation 5.

37. **entry.md:102** – "its earlier relay to n-build, for the relays' form"
    - **CONFIRMED.** #24 printed one SendMessage to n-build, of 15:50:19Z.

38. **entry.md:103–105** – "… and the process lines that its three `pgrep`s printed"
    - **IMPRECISE.**
    - There were four pgrep invocations in three commands; #10 had two.
    - #33 printed "8051 python3.12" for #6 and for #8, and "8051 python3.12 | 8051 python3.12" for #10.
    - The rest of the bullet is confirmed: the extract, the user turns and the other tool calls in #30 and #32, and the messages in between in #33.
    - Fix: "… and the process lines that its `pgrep`s printed (four, in three commands);"

39. **entry.md:107** – "**reads by name:** of its own scratch files and screen outputs; …", and the departures list as a whole
    - **FAIL: a missing class.**
    - `awk` ran in eight of the 35 commands: #1, #3, #27, #28, #29, #31, #34 and #35. The entry names it for three: #1 and #3 (the widths and builds) and #31 (the pod list).
    - The five not named:
      - #27: fields and line heads of `notes2/bash_after_22.tsv`.
      - #28 and #35: each sweep file's field count and listing.
      - #29: the print of commands 1–11 from the first sweep's file.
      - #34: the routing raw's fenced block extracted into `routing_block.txt`, and the close lines' widths.
    - Two more forms are named only among 101026c's checks:
      - `tail -c` with `od -c`, also run on the PI's extract in #30.
      - `grep -c` counts, also run over this commit's drafts in #34 and over the sweep files in #28 and #35.
    - Fix: add after the reads by name: "- **`awk` over its own scratch files, in five more commands:** the sweep files' fields and listings (`101026c`'s last sweep file once, and each of this span's two sweeps), the print of the first sweep's commands 1–11, and the routing raw's checks (its fenced block extracted into scratch, and the close lines' widths); with `tail -c` and `od -c` of the PI's extracted message, and `grep -c` counts over the drafts and the sweep files;"

40. **entry.md:107–110** – committed files: `RESULTS.md` by `head`, `sed -n` ranges, `grep -n` and the Read tool; four seat-facing raws by `shasum`, with `git log --format='%h'` of their paths; the list of record's raw and the first sitting's routing raw by the Read tool; the seat's raw by `shasum`, `wc` and the Read tool
    - **CONFIRMED.**
    - RESULTS.md: #25, #26, #3's `sed -n` ranges, and the Read tool twice.
    - The four raws: #22.
    - The list of record's raw and the routing raw: Reads at 22:29:24Z and 00:34:33Z.
    - The seat's raw: #23, and a Read at 00:33:52Z.

41. **entry.md:110–111** – "of its screen script's pod list, by `grep -n` and `awk`, which printed the pods' addresses and ports in its own tool output only"
    - **CONFIRMED**, by count, printing none of them.
    - #31's output before its git grep part has 5 lines. Three of them hold 5 quoted dotted-quad tokens and 7 quoted 2–5-digit numbers.
    - None of the five drafts holds a dotted quad (count 0 each).

42. **entry.md:111–112** – "and of its memory files (`wc -l`, `tail`, `sed -n`, `cut` and `rev`)"
    - **IMPRECISE.**
    - It omits the Read tool on the memory index (22:31:56Z), one of the seven Reads at line 121.
    - Fix: "and of its memory files (`wc -l`, `tail`, `sed -n`, `cut` and `rev`, and the Read tool once on its index);"

43. **entry.md:113–114** – "`wc -c` in four commands (…); `wc -l` in 14; `cmp` in four"
    - **CONFIRMED.** Counting what ran:
      - `wc -c`: #4, #23, #30, #34.
      - `wc -l`: #1, #3, #4, #8, #17, #20, #21, #23, #27, #28, #30, #31, #34, #35.
      - `cmp`: #3, #4, #8, #34.
    - #35's matches for `wc -c` and `cmp` are loop words.

44. **entry.md:115–116** – `pgrep -il python` in three commands, twice in the re-screen, each printing PID 8051 alone
    - **CONFIRMED.**
    - The results of #6 and #8 show "8051 python3.12", and #10's shows it twice. No `ps` ran.
    - "pgrep" in #33 and #35 is an echo string and a loop word.

45. **entry.md:117–119** – "**writes outside the repository:** in its own scratch (the drafts, the builds, the push record, the sweep files and the extracts, and two folders made by `mkdir -p`); …"
    - **IMPRECISE.**
    - It omits the re-screen's four output files, written by #10 into `push15b/`: `screen15b.txt`, `gl15b_run.txt`, `gl15b.json` and `gl5_15b.txt`.
    - The rest is confirmed:
      - `mkdir -p` in #10 and #28.
      - `cat >>` in #11 and #21, each with `tail -n 1`.
      - The Edit tool on the memory index at 22:32:00Z.
    - Fix: "in its own scratch (the drafts, the builds, the re-screen's four outputs, the push record, the sweep files and the extracts, and two folders made by `mkdir -p`)".

46. **entry.md:120–124** – the tool calls beside the shell
    - **CONFIRMED.**
    - jq lists the non-shell calls after 17:45:48.378Z and before #35:
      - SendMessage: 3.
      - ReadNotifications: 1 (result "No queued notifications.").
      - ToolSearch: 1 (SendMessage's schema).
      - Read: 7.
      - Edit: 5 (four on `notes2/entry.md`, one on the memory index).
      - Write: 6 (`vc_raw_head.md`, `msg.txt`, `routing_head.md` and the three close lines).
      - update_plan: 7. wrap_up: 2.

47. **entry.md:127–129** – committed by path; the commit-time home-prefix count is 0; nothing ran on a model; not pushed
    - **NOT CHECKABLE.** The commit is in the future.
    - Now: the five drafts hold no home-folder prefix, account name, temp root, UUID, `local_` string, dotted quad or email (each count 0).
    - Among the 35 commands, the only Python is #10's screen and gl5.
    - Fix: none.

48. **The placement** in `RESULTS_draft.md`
    - **CONFIRMED.**
    - I rebuilt the draft from `git show 101026c:RESULTS.md` with `sed -n` ranges 1–23, 24–730, 731–788, 789–877 and 878–end, inserting the entry and the three close lines between them. `cmp` against the draft is equal.
    - The draft has 35,370 lines, which is 35,199 + 130 + 17 + 12 + 12. RESULTS.md has no diff from 101026c.
    - Lines 730, 788 and 877 are the last text lines of the entries of 91f0d35, 4fdcdcc and 2ca24e8, each followed by a blank line.
    - Line 22 is "## Log — Phase 2" and line 23 is blank.

49. **The widths**
    - **CONFIRMED.**
    - Counting UTF-8 characters with `wc -m`, only link lines are over 120: entry.md:5 and line 3 of each close file, 139 each.
    - The widest other lines are 119 (entry.md), 118 (close_91f.md), 119 (close_4fd.md) and 115 (close_2ca.md).

50. **The entry's end**
    - **CONFIRMED.** `tail -c 3 | od -c` gives ". \n \n"; line 130 is empty.

51. **close_91f.md:2–5** – the raw's link, `813de3db…6157` and "PI: route as given"
    - **CONFIRMED.**

52. **close_91f.md:6–7** – "`91f0d35`'s BUILD, its self-test (634 of 634) and its two values-checks stand as the driver of record, and no new BUILD, script or manifest is owed." (§2)
    - **CONFIRMED.** The quotation is raw:41, in §2 (1).

53. **close_91f.md:8–9** – GT2 … GT17 stand as this entry declares them, none struck; GT11 is Q8, option (iii), amended
    - **CONFIRMED.**
    - raw:38: "… stand as the BUILD entry declares them; none is struck". raw:29 makes GT11 Q8.

54. **close_91f.md:10–11** – the review's items
    - **CONFIRMED.** raw:40.

55. **close_91f.md:12** – a v2 note for §1.8's copy-back and §2's two ends (item 3)
    - **CONFIRMED.** raw:41 and PI item 3.

56. **close_91f.md:13–16** – the quotation of (d), with (e) and (g)
    - **CONFIRMED.**
    - The quotation (182 characters, extracted by `sed`) is in raw:48, under (d). `grep -c -F -f` gives 1.
    - raw:49 ends (e) with "Inert."; raw:51 ends (g) with "Accepted, all four".
    - See observation 4.

57. **close_4fd.md:1–5**
    - **CONFIRMED.**

58. **close_4fd.md:6–9** – Q8 …, "as the `.gitignore` at `91f0d35` admits them"
    - **CONFIRMED.** raw:8 and raw:30–32 (the phrase gives 1).

59. **close_4fd.md:10** – "The supplement's two corrections (its §4: F8 and F10) are accepted (§2)."
    - **CONFIRMED.**
    - RESULTS.md line 749: "§4: two corrections to the block, GT9's re-keying (the review's F8) and GT4's "For a run of record" (F10)".
    - raw:40.

60. **close_4fd.md:11** – "this entry's are inert (§3 (d) and (e); item 6)"
    - **CONFIRMED.**
    - 4fdcdcc's entry puts Code's departures in the BUILD's entry, which is (d), and declares the values-checker's, which is (e).

61. **close_2ca.md:1–5**
    - **CONFIRMED.**

62. **close_2ca.md:6–9** – the 18 reads on runs 0, 32, 64, 95, 127 and 159; the identity with no cap; T at the medians; option (i)'s benchmark; 403,620 fits; a zero line at v1.0; no STOP after COMPLETE
    - **CONFIRMED.** raw:7 and §1; `grep -c -F` gives 1 for each phrase.

63. **close_2ca.md:10**
    - **CONFIRMED.**

64. **close_2ca.md:11** – "**Departures:** this entry's are inert (§3 (d) and (e); item 6)."
    - **IMPRECISE.**
    - 2ca24e8's entry (RESULTS.md lines 832–868) declares four classes:
      - Code's of 2026-11-20 and of 2026-11-21, which are n-build's, under (d).
      - The survey's own, in the spec raw's §4 (line 857).
      - The values-checker's, under (e).
    - §3 names no survey item. The raw names the survey once, in its header: "§4 the survey's report and its departures".
    - Fix: "- **Departures:** Code's and the values-checker's are inert (§3 (d) and (e); item 6). §3 does not name the survey's own (the spec raw's §4), which the seat lists among its reads."

65. **routing_raw.md:1 and :3** – the title; the raw's path and `813de3db…6157`; Q1–Q7 and Q8; "whose entry cites this raw and whose three close lines quote its last line"
    - **CONFIRMED.**

66. **routing_raw.md:5** – "(3,141 bytes, sha256 `d883d4bc…9789`), a departure its entry declares…"
    - **CONFIRMED.**
    - The record's text, by `jq -j`: 3141 bytes (jq's utf8bytelength is also 3141). `shasum | cut` gives d883d4bc … 9789.
    - `cmp` against `pi_routing_msg.txt` is equal (3141 bytes, the same digest).
    - entry.md:103 declares the extraction.

67. **routing_raw.md:9–52** – the fenced block
    - **CONFIRMED.**
    - `cmp` of the record's text plus "\n" against `sed -n '10,51p'` is equal.
    - Line 9 is "```text", line 52 is "```", and the file has 52 lines.

68. **`bash_sweep1.tsv`**, the source for the departures
    - **CONFIRMED.**
    - It has 35 lines of 2 fields. By `cmp` it equals the transcript's first 35 main-thread Bash calls after 17:45:48.378Z.
    - Its form is timestamp, tab, then the command with newlines and tabs escaped. No command holds a tab or CR.
    - See observation 7.

## Observations

1. **entry.md:6–7: the quotation sits after the wrong phrase.**
   - "second sitting; the first sitting of a fresh thread" follows "each read in full", which it does not support. The raw's words for that are "both in full".
   - Suggested: "…and `4fdcdcc` (Q8), both read in full, at the seat's "second sitting; the first sitting of a fresh thread"."

2. **entry.md:57–58: "the PI's word" is not in item 9.**
   - Item 9 gives "[yours]" and names no PI word. "and the PI's word" is the coordinating session's own practice; push #15 waited for the PI's "Push".
   - Suggested: "…G-TIME-n's entry and, by the coordinating session's practice, the PI's word, …".

3. **Outputs that name the account.**
   - #14's push output printed origin's URL, which holds the account name.
   - #17 wrote that URL into the push record in scratch and printed it.
   - #12's command text held it in a `grep -c` pattern, which printed a count only.
   - It is in no draft. raw:50 (f) counted a `%an` print of the author's name in the session's own output as a form, so a line here would follow that precedent.

4. **close_91f.md:13–16: (g) reads as this entry's own departure.**
   - (g)'s four answers are recorded in 5f62dd1's entry, at RESULTS.md line 308 ("The coordinating session's answers to n-build on forms since `c9d35e2`"). They are on forms that 91f0d35's texts use, and the raw classes them "accepted", not inert.
   - As placed, "this entry's are inert (… and (g) …, accepted …)" reads them as 91f0d35's own.
   - Suggested: "this entry's are inert (§3 (d), n-build's: "…"; and (e), the reviewer's and the checkers'; item 6); (g), the coordinating session's four answers to n-build on forms (at `5f62dd1`), which bear on this entry's forms, are accepted."

5. **Observation 8's "next message".**
   - The sentence was written at 16:51:41Z (Edit) and 16:52:17Z (Write).
   - Three progress texts in the same turn followed, at 16:52:27Z, 16:54:13Z and 16:55:20Z; none carries the times.
   - The correction is the turn's closing message, at 16:56:42Z, before 5f62dd1's commit at 16:58:35Z.
   - The claim holds if "message" means the turn's closing message.

6. **`rev-list` is not marked as lacking the pathspec.**
   - #15's `git rev-list --left-right --count refs/remotes/origin/main...HEAD` is a range form without item 3's pathspec, though it prints counts only.
   - The entry marks the two `git log` forms "without item 3's pathspec", but not this one.

7. **The sweep file's form is not reversible.**
   - `bash_sweep1.tsv` escapes newlines and tabs but not backslashes, so a literal `\n` in a command and a real line break print the same. A rebuild with jq's `@tsv` differs from it at line 1, character 295.
   - `@tsv`, or one JSON string per line, would be reversible.

8. **#35's own class table counts substrings, not runs.**
   - It printed pgrep 5, ls-remote 6, wc -c 5, cmp 5, hash-object 4, mkdir 3, cat >> 3, cp 2, python3 2 and for 8.
   - These include echo strings, heredocs, jq patterns and its own loop words.
   - The entry gives counts of what ran (3, 3, 4, 4, 3, 2, 2, 1, 1 and 6), and they match the texts.

9. **The re-screen and the push were hours apart.**
   - The re-screen (#10) ran 4 h 41 min before the push (#14).
   - #12 shows HEAD at 101026c and origin at c9d35e2 in between, so the screen of record covers the pushed range.

10. **The routing raw has long lines.**
    - routing_raw.md:3 and :5 are single-line paragraphs over 120 characters, and not link lines.
    - The brief's width rule names only the entry and the close lines. #34 itself printed "over 120 (not link lines): 2" for this raw.

## My own departures

1. **The brief's re-hash.** One command, `shasum -a 256 | cut`. It printed `1d1591d2` and `9532`.

2. **jq over `<transcript>`: 37 commands.**
   - They printed:
     - the coordinating session's command texts #1–#35 in full, including its memory appends' text in #11 and #21;
     - the tool results of selected commands, masked with `sed` for dotted quads and ports where a result could hold one;
     - the relays, the PI's messages and the user turns, cut;
     - lists of tool calls, and counts.
   - That output showed local roots and the account name inside paths, `local_` session ids in one tool-call list, and the pod's id. None is in this report.

3. **jq over no file: one command.** It had two `jq -rn` runs converting literal timestamps to local time. They printed "2026-11-21 17:29 EST" and "2026-11-21 19:32 EST". This is outside the brief's rule that jq runs only over the transcript and the gitleaks JSON.

4. **jq over `<own>/push15b/gl15b.json`: one command**, which the brief allows. It printed the one finding's rule, file and line, commit, and the start of its description.

5. **git commands naming one file or folder outside data/.**
   - `git show 101026c:RESULTS.md` in 11 commands (28 runs), piped to `sed -n` ranges, `grep -n`, `wc -l` and `cmp`. They printed line ranges and line-number hits of RESULTS.md, and 35199.
   - `git diff --name-only 101026c -- RESULTS.md` and `git ls-files --modified -- RESULTS.md`, in one command. Both printed nothing.
   - `git ls-files`, and its `--others --exclude-standard` form, of single named paths, in 4 commands (8 runs):
     - the seat's raw (its name, as untracked);
     - the spec raw (its name);
     - `.gitleaks.toml` and `.gitleaksignore` (nothing);
     - the routing raw's target path (nothing);
     - `results/raw` (the seat's raw's name).
   - `git log --format='%h %cI' -n 6 101026c -- RESULTS.md`. It printed six ids with commit times.

6. **git over a range or the tree**, each with `-- . ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/m[f]3/**'`.
   - `git log --format` of ids, and `--name-only`, over `c9d35e2..101026c`: three runs in one command. They printed 5 ids, the count 19 and the 19 paths.
   - One content search, `git grep -c -E` of two time patterns at 101026c. It printed 20 file names with counts.

7. **`git rev-parse --short` of HEAD and origin/main.** One command, reading the local refs only. It printed `101026c` twice.

8. **Content reads of named files, none under data/.**
   - The Read tool 7 times: the brief, the five drafts and the seat's raw.
   - `sed -n`, `cat`, `head`, `cut`, `tr`, `rev`, `cat -v`, `cat -n`, and `tail -c` with `od -c`, over the drafts, the sweep files, the routing raw, the seat's raw, the spec raw and `push15b/`'s text files.
   - `/usr/bin/grep` counts and searches over those files and over jq's output.

9. **Sizes and counts, none under data/.**
   - `wc -c` in 4 commands: the seat's raw (32674); the PI's text from jq and the extract (3141 each); the 35 line sizes of `bash_sweep1.tsv`; the routing raw (3989).
   - `wc -m` in 1 command, for the drafts' line widths.
   - `wc -l` in 13 commands.
   - `cmp` in 5 commands (6 runs). Five were equal; the first sweep rebuild, in `@tsv` form, differed.

10. **Name-only listings.** `ls -1` of `push15b/` and of `notes3/`, in two commands. They printed 5 and 14 names.

11. **Environment.** `printenv` of the two gitleaks config variable names, in one command. Neither is set.

12. **Loops: 14 commands.**
    - They looped over literal lists (timestamps, line ranges, draft names, heredoc patterns), or over lines read on stdin.
    - No list held a guard marker or the campaign's plain name.
    - In three of them, file text holding the campaign folder's plain name (the drafts' and the PI's quotations) passed through zsh's builtin `printf`, which starts no process. In one, it reached `grep` only as a `/dev/fd` pattern file.

13. **The pod list.**
    - I counted by pattern over the coordinating session's pod-list output as the transcript holds it.
    - I made one masked shape print of those five lines: digits shown as 9, letters as a, cut at 60 characters. It printed no address, port or name.
    - I made one masked print of the screen script's two `pod_token` lines as #30's output holds them.
    - I did not read the screen script itself.

14. **One command exited 1.** Its last `grep -c` printed 0.

15. **Beside the shell.**
    - One tool-schema load, for Monitor, which I did not use.
    - The 7 Reads counted in departure 8.

16. **Not done at all:**
    - no file writes, no redirects into files, no `tee`, and no git writes;
    - no network, no `ps` or `pgrep`, and no `stat` or listing with sizes or times;
    - no Python, no `awk`, and no interpreter but `shasum` and `jq`;
    - no whole-tree `git status`;
    - no guard marker and no plain campaign name in any command text;
    - the memory folder was not listed, globbed or read;
    - nothing under `data/m[f]3/`, `data/*/ckpt/` or `data/*/reports/` was listed or read.

## Tallies

- Items: 68 in all.
  - CONFIRMED: 58.
  - IMPRECISE: 7 (items 13, 27, 35, 38, 42, 45 and 64).
  - FAIL: 1 (item 39).
  - NOT CHECKABLE: 2 (items 4 and 47).
- Observations: 10.
```
