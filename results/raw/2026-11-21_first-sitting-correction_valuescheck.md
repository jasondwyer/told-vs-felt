# The coordinating session's correction to its notes on the first sitting of 2026-11-21: the blind values-check, as returned, with every disposition

PI date 2026-11-21. Code (the coordinating session).

**What was checked.** One blind pass by a subagent over the correction entry's draft (sha256 `2f905b14…f140`, 104 lines) and its placement in a draft of the new `RESULTS.md` (`b130cd13…ac97`, 35,104 lines).

**The checker's brief** was a file in the coordinating session's scratch folder, named in its Agent call by path and sha256 (`72ece252…d823`, 107 lines). The checker re-hashed it equal before it began. It is not committed, because it names the local roots in full. It:
- named the sources: the repository at `5f62dd1`; the coordinating session's three sweep files and its transcript; n-build's launch folder; and the coordinating session's screen for the push;
- quoted the list of record v2's items 1–5 verbatim, from `2026-11-10_list-of-record-v2_design-to-code_answers.md`, lines 18–22 (equal by `cmp`);
- barred any interpreter but `shasum` and `jq`, any write, any network, `ps` and `pgrep`, a whole-tree `git status`, anything under `data/*/ckpt`, `data/*/reports`, the campaign folder or n-build's fixture and test folders, the memory folder, and the guard markers and the campaign folder's plain name in any command text;
- barred passing any path that may hold a marker word to a command as an argument: such paths go on stdin only;
- set item 3's pathspec, with the campaign folder's exclusion, on every git command over the tree or a range.

**The report** is in §3, extracted verbatim by `jq` from the subagent's one hand-back (306 lines, sha256 `cde5639f…796e`). It names no local root. Its `<repo>`, `<own>`, `<nb>` and `<transcript>` are the repository, the coordinating session's scratch, n-build's scratch and the coordinating session's transcript. Its one `local_` string is the screen's class name `local_path`.

**Totals:** 71 items (56 CONFIRMED, 7 IMPRECISE, 7 FAIL, 1 NOT CHECKABLE) and 11 observations.

## 1. Dispositions

- **Item 5** (FAIL): fixed, in the checker's words. The overlay loop also passed overlay91's 15 files under the code package named like the campaign folder, so 30 of its `git` processes had the campaign folder's plain name in their argv. The correction and the heading now say so, and that the other two loops' lists hold no such path.
- **Item 7** (IMPRECISE): applied. The first sweep's loops ran over literal lists (of files, name–digest pairs, folders, numbers and line ranges), line numbers from a stream and n-build's commit-window manifests. Inside `pkgsha.sh` they ran over `valence_core/n`'s files, none of them marker-named in its five copies, as the check found.
- **Item 9** (FAIL): fixed. The two later loops are "after `5f62dd1`'s last sweep … one on each side of its commit": the `hashes` loop before the commit, the manifest loop after it.
- **Item 14** (IMPRECISE): applied, in the checker's words. A folder reached by `cd` and a glob serves only where the marker is in a folder's name; a path whose own file name holds one goes on stdin.
- **Item 18** (FAIL): fixed. Ten files for reading, with the snippet test's runner and fixture builder, beside `reviewed_v1/`.
- **Item 41** (IMPRECISE): applied. n-build's unpruned `find -newer` ran over its launch folder, whose test/ holds the harness's ckpt- and reports-shaped copies. It was stopped before it finished and redone with test/ pruned.
- **Items 47 and 48** (IMPRECISE): applied, in the checker's words: the first gate's "ok" on two empty strings, and the second gate's guessed bar of 800 against its count of 774 of the 931.
- **Item 58** (FAIL): fixed. `wc -l` ran in nine commands, the sweep's among them.
- **Items 61 and 65** (IMPRECISE): applied. The `diff` of `RESULTS.md` against its rebuilt draft is added, and so are the calls beside the shell as the check counted them.
- **Items 64, 66 and 67** (FAIL): fixed. The `git log` of the screen's range; the `tail -n 1` read of the memory file; and the `head`, `grep -E` and `grep -c` reads and counts over n-build's files.
- **Item 68** (NOT CHECKABLE): the commit's counts are taken at the commit and stated in its entry.
- **Observations:**
  - 1, applied: "by the next process checks after the loops".
  - 2, applied: run 2's stderr went with its stdout into `run_2.txt`, which holds only its 67 expected lines.
  - 3, met in the entry: the coordinating session's message to n-build said "all twelve you listed" when n-build had listed fourteen. All fourteen are at their sha256s.
  - 4, met by item 58.
  - 5, applied: the command that exited 1 at a `grep -c` with no match.
  - 6, applied: the screen outputs, among its reads.
  - 7, 8 and 10, noted.
  - 9, met by item 47.
  - 11, met by item 7.

## 2. Edits after the check

- The dispositions above; the entry's values-check bullet and the values-checker's departures, from §3; and the last sweep of the coordinating session's own shell commands, made after the check (8 commands after the first sweep's 22), as a sub-bullet of the entry's departures.
- The edits were checked by tool, by `diff` of the checked draft against the final text. Each hunk is a disposition above, a filled placeholder, the last sweep's sub-bullet, or one rewrap after an edit.
- No second full pass was made.

## 3. The report as returned

```text
VALUES-CHECK REPORT: the coordinating session's correction entry after `5f62dd1`

Text checked: `<own>/s2026-11-21/notes2/entry.md` (104 lines, `2f905b14…f140`). Placement checked: `<own>/s2026-11-21/notes2/RESULTS_draft.md` (35,104 lines, `b130cd13…ac97`). I read the brief whole and checked it at `72ece252…d823` (107 lines) before starting. Abbreviations below were made by `cut -c1-8` and `cut -c61-64`. "The 35" means `<own>/s2026-11-21/notes/bash_after_s100.tsv`. "The 22" means `bash_after_last.tsv`. "The 100" means `bash_since_c9d35e2.tsv`. Numbers like "the 22's 8th" are command positions. I give no clock times. The order comes from transcript timestamps and git's committer time.

Base check of the sweep files. I used `jq` over `<transcript>` to pull main-thread `Bash` tool_use calls (`isSidechain` not true) from the first file's first timestamp on. That gives 161 calls. The first 157 equal the three files concatenated, by `cmp`, both in file order and sorted by timestamp. The 22nd of the last file is the sweep that wrote it, and that file still has the digest the sweep printed (`532e3bbb…8425`). Four calls follow the sweep.

## Items

1. L1–2: "a guard marker in the argv of 58 non-Python processes, from three per-file loops over lists holding marker-named paths". **CONFIRMED.** The three loops give 40 + 1 + 17 = 58 (items 4, 11, 12). Every one is a `git` or `grep` process.

2. L4–5: "`5f62dd1`'s entry says of the 35 commands after its first sweep: "No guard marker and no plain campaign name was in any of them (a bracketed sweep)"". **CONFIRMED.** I joined `git show 5f62dd1:RESULTS.md` lines 24–306 and ran `grep -c -F`: the sentence matches once, and so does "the 35 commands after the first sweep,".

3. L5–6: "That sweep read the commands' text, not the paths a loop expands into arguments." **CONFIRMED.** The 35's 35th command (the last sweep) runs `grep -c -E` with the bracketed marker pattern and `m[f]3` over the sweep file's text. My own bracketed count over the 35's texts prints 0 markers and 0 plain names.

4. L7–9: "One of the 35, the check of overlay91 … looped over overlay91's 173 files and passed each path to `git hash-object` and to `git rev-parse 91f0d35:<path>`. Twenty of the paths hold a guard marker, so 40 `git` processes had one in their argv." **CONFIRMED.**
   - The 35's 23rd command does a find pruned at ckpt and reports, then runs `git hash-object "$O/$f"` and `git rev-parse -q --verify "91f0d35:$f"` per file. It printed "equal 173, differ 0, not in the commit 0".
   - My pruned `find` over overlay91, counted from the stream: 173 files, 0 pruned folders, 20 marker-named by the bracketed pattern (20 with `-i` and 20 without).

5. L10: "The sentence holds for the commands' text alone. It is corrected here; the committed text is not rewritten." **FAIL.** The correction fixes only the guard-marker half of the sentence.
   - The same find stream shows 15 paths that hold the plain name. All 15 are overlay91's copy of the code package named like the campaign folder (`valence_core/m[f]3/`). `91f0d35` has the same 15 files there (`git ls-tree --name-only`, counted). None of the 15 is also marker-named.
   - The loop's `find` did not prune that folder. So 30 `git` processes had the plain name in their argv.
   - `5f62dd1`'s own entry counts this package's name as the plain name ("in the code package's name under `valence_core/`").
   - The other two loops' lists hold no such path (0 and 0).
   - Fix: replace L10 with "The sentence holds for the commands' text alone. The same loop also passed overlay91's 15 files under the code package named like the campaign folder, so 30 of its `git` processes had the campaign folder's plain name in their argv; the sentence's plain-name half is corrected with it, and the other two loops' lists hold no such path. It is corrected here; the committed text is not rewritten." In the heading, after "marker-named paths", add "; and the campaign folder's plain name in 30 more `git` processes of the first loop".

6. L11: "The first sweep's 100 commands held no loop over such paths." **CONFIRMED.**
   - The 100 contain no `xargs`, no `-exec`, and no unquoted glob that expands to paths.
   - Their loops run over literal lists, line numbers, and n-build's two commit-window manifests (2 and 5 lines; 0 marker-named, 0 plain).
   - `pkgsha.sh` (7 runs in 6 commands) loops over `*.py` names in `valence_core/n`. There are 16 names in the index and 16 in each of the five copies (`<nb>/gtime/overlay1`, `overlay3`, `overlay4`, `overlay5`, launch `overlay91`). None is marker-named.
   - The verified commits' file lists (`git show --name-only` with the full pathspec) hold 0 marker-named paths.

7. L11–12: "Their loops ran over literal lists of named files, the verified commits' manifests and `valence_core/n`, as a check by tool after the commit found." **IMPRECISE.**
   - Some loops ran over things that are not files: numbers and line ranges (`for n in 1162 1381`, `for r in "24 112" …`), name–digest pairs, folder names, and line numbers piped from `grep -n` (the 100's 51st and 91st).
   - The after-commit check (the 22's 21st) matched only `for`/`while` in the commands' own text. It cannot see the loop inside `pkgsha.sh`.
   - Fix: "Their loops ran over literal lists (of files, name–digest pairs, folders, numbers and line ranges), line numbers from a stream and n-build's commit-window manifests, as a check by tool after the commit found; and, inside `pkgsha.sh`, over `valence_core/n`'s files, none marker-named in any of its five copies."

8. L12–13: "That entry's statement that no guard marker reached an argv in them stands." **CONFIRMED.** The statement is in `5f62dd1`'s entry ("no guard marker reached an argv (a bracketed sweep of the same commands)": 1 match). Item 6 found no expanding form in the 100. The 100's texts hold 0 markers, and the plain name once (its 19th command, already declared).

9. L14: "After `5f62dd1`'s commit, two more loops of the kind:" **FAIL.** The hashes loop ran before the commit:
   - the hashes loop is the 22's 8th command;
   - `git commit` is the 22's 14th (it printed `5f62dd1`, and git's committer time falls in that call's second);
   - the manifest loop is the 22's 19th.

   Fix: replace L14 with "After `5f62dd1`'s last sweep, two more loops of the kind, one on each side of its commit:". Start L15's bullet with "before the commit, the check of …" and L17's with "after it, the check of …".

10. L15–16: the `hashes` check, "a `grep -F` per pair, put the adapter module's path into one `grep`'s argv". **CONFIRMED.** The 22's 8th loops `while read -r k p d` and runs one `git show 91f0d35:scripts/n_sessions.py | grep -q -F -e "\"$p\": \"$d\""` per `imported_sha256` line, so 12 greps. Of the 12 closure paths (`sed -n '2,13p' | cut -d' ' -f2`, bracketed count), 1 holds a marker, in its own file name.

11. L17–18: the manifest check, "a `git rev-parse 91f0d35:<path>` per file, put marker-named paths into 17 more `git` processes' argv." **CONFIRMED.** The 22's 19th runs one `git rev-parse -q --verify "91f0d35:$p"` per file, then `git cat-file blob "$b"`, which takes a blob id, not a path. The manifest has 17 marker-named paths (`cut -c67-`, bracketed count, with and without `-i`).

12. L19: "None of the 58 processes was Python." **CONFIRMED.** They are 57 `git` processes and 1 `grep`.

13. L19–20: "The Q-F3 campaign's process (PID 8051) ran on, by the process checks after each loop." **CONFIRMED.** These are the transcript's tool results; per the rules I ran no process check.
   - After the overlay loop, the next check is the 22's 4th command.
   - The hashes loop's own command ends with `pgrep -il python`.
   - After the manifest loop, the 20th has the check.

   Each printed "8051 python3.12". That this PID is the campaign's rests on the session's record (observation 1).

14. L21–23: "From here … passes the paths on stdin … or runs inside the folder, reached by `cd` and a glob; never with the path as an argument." **IMPRECISE.** Running inside the folder only helps when the marker is in a folder name. Some markers are in the file's own name:
   - 4 of overlay91's 20 marker-named paths (16 have it in a folder name only);
   - 1 of the manifest's 17;
   - the one closure path.

   Fix: "From here, a per-file check over a list that may hold marker-named paths passes the paths on stdin (for example `git cat-file --batch-check`, or `grep -f` over a file); running inside a folder reached by `cd` and a glob serves only where the marker is in a folder's name, and a path whose own file name holds one goes on stdin. Never with the path as an argument."

15. L24: "read and accepted as the set to relay, and held." **CONFIRMED.** The coordinating session's last message to n-build says: "read, ACCEPTED as the set to relay, and HELD".

16. L25–26: "The relay to the pod session waits for the seat's answers on Q1–Q8 and for the PI's word; nothing is staged on the box." **CONFIRMED.** The same message says so, adding "Stage nothing on the box." No box or pod call appears among the 22, the four after them, or the non-shell calls since then.

17. L27–29: the four box files' digests and line counts. **CONFIRMED.** Each `shasum` equals n-build's full digest: `eeee8c2e…39b6`, `84550072…957b`, `a853932b…522b`, `036968c0…2369`. `wc -l` gives 519, 66, 13 and 237.

18. L29–31: "Eight more files are for reading: the review's brief, report and dispositions, the harness, the stand-in, the mutation pass, the manifest's builder and n-build's departures log. Each is at the sha256 n-build sent." **FAIL.** n-build's message with the set lists ten files for reading, plus `reviewed_v1/`. The entry leaves out `snippet/run_snippet_test_v2.sh` and `snippet/make_fixtures_v2.sh`. All ten match n-build's digests by `shasum`.
   - Fix: "Ten more files are for reading: the review's brief, report and dispositions, the harness, the stand-in, the mutation pass, the snippet test's runner and fixture builder, the manifest's builder and n-build's departures log, beside `reviewed_v1/`, the files as reviewed. Each is at the sha256 n-build sent."

19. L31–32: "The four box files hold no IPv4-like string, no "port" or "ssh" word, no local root and no user name." **CONFIRMED.** `grep -c` over each of the four files found 0 for each of: an IPv4-like string; `-i -w port`, `ports`, `ssh` and `scp`; the home, private and tmp prefixes; `~/`; and the user-name pattern. A wider pod-address pattern matched only an environment variable's name and the cuBLAS setting.

20. L33–34: "Its 66 files each equal their blob at `91f0d35`, and none is under a ckpt, reports or campaign path." **CONFIRMED.**
   - I fed `91f0d35:<path>` lines into `git cat-file --batch-check` on stdin (from `sed` over the manifest): 66 blobs.
   - Then `git cat-file blob <id> | shasum` for each, compared with the manifest's digest column: 66 equal.
   - A path pattern for ckpt, reports and `m[f]3`: 0 matches. No duplicate paths.

21. L35: "The script, the note and the review's dispositions (F1–F12, M1–M8, O1–O13) were read whole." **CONFIRMED.**
   - The transcript's Read calls cover the dispositions and the note with no offset or limit (100 and 237 lines).
   - The script was read in three calls: lines 173–260 before `5f62dd1`'s last sweep, and lines 1–172 and 261–519 after.
   - The dispositions hold F1–F12 and M1–M8 as items, and O1–O13 as "O1–O3, O5–O8, O10–O12", O4, O6, O9 and O13.

22. L36: "B1, B2 and the copy-back in Q8's default (ii) are as routed." **CONFIRMED.**
   - The routing: "B1, B2 and B6 as you list them, and the copy-back in the BUILD's default for Q8: the report, the shadow cell's JSON, the artifact and the raw". n-build's list: "create and name --bench-dir on the volume (B1), clean a killed benchmark's leftover folder (B2)".
   - In the script, B1 is `mkdir "$W/bench"` followed by the line "the benchmark's folder (B1): … new, on the volume beside the copy".
   - B2 is `bench_clean`: an `n-gtime-bench-*` leftover is named and removed; anything else fails as "BENCH FOLDER FAIL" and is left in place. The note's killed-run section has the pod session remove such a folder by name.
   - The note's copy-back sends the report, the artifact and the shadow cell to `rec/` under "§2 (ii)". The steered cells and arrays stay on the box. The raw is the out file.

23. L36–37: the respawn statement. **CONFIRMED.** The note says the two checks are for a new or replacement box, "and this is neither, so neither runs before this launch". It also says: "If the pod has been restarted or replaced since G-CAL-n's run, both respawn steps run first, and this launch waits for them."

24. L38–40: B6's form. **CONFIRMED.**
   - The script runs `2> "$W/smoke.err" | tee "$W/smoke.txt"` and `2> "$W/run.err" | tee "$W/run.txt"`. Each is followed by `if [ -s … ]` and a `cat` of the stderr file.
   - The note says the raw "is the out file".
   - The acceptance message accepts this form as meeting B6.

25. L41–43: the smoke's two ends. **CONFIRMED.**
   - The script header (lines 50–54) describes them.
   - Lines 431–432 set `VD=PAUSE; WH=" (the smoke)"` at exit 3 (with SMID 0), and `VD=STOP` at exit 2, both only when the smoke's checks held.
   - Then it prints "RUN NOT STARTED: … its checks held: for the seat".
   - The end line is `gtime $V $VD$WH` with `V=v1`. PAUSE exits 3 and STOP exits 2.
   - The dispositions' F3 has the same two ends.

26. L43: "The BUILD's entry did not name these two ends." **CONFIRMED.** In `91f0d35`'s RESULTS.md, the BUILD entry (its lines 24–249) uses "smoke" only for a smoke's paths, checks at a smoke, and F10. It gives the stage's exits (0, 3, 1, and 2 at G-VER's STOP) but names no smoke end for the launch.

27. L43–44: "On this deterministic backend a PAUSE or a STOP would fire at the smoke first. A refusal at the smoke is a FAIL." **CONFIRMED.** The script header says the same, and also "FAIL (exit 1): anything else, a refusal or the run not started included". n-build's message agrees.

28. L45–46: m32. **CONFIRMED.**
   - `run_2.txt` has "m32: killed by a_ccells".
   - n-build's close report: by `and`/`or` precedence, m32 also drops the cells-sum test, and `a_crec` isolates the recomputations test by construction.
   - The close message: "m32: leave it declared".

29. L47–48: "What could need a v2". **CONFIRMED.** The acceptance message's last answer says this in the same terms. The note says "If Q8's answer is another option, the copy-back follows it (a v2 of this note)."

30. L49–50: "model-free: `hashes` from a `git archive` of `91f0d35`, then the snippet test v2." **CONFIRMED.** n-build's request: run 1 is `hashes` "from a `git archive` of `91f0d35`" in overlay91, and run 2 is "the snippet test v2". Both are laptop Python runs with no model load.

31. L52: "the window's files at their sha256s;" **CONFIRMED.** The 35's 22nd printed "ok … at its sha256" for five files: the overlay driver, the runner, the script, the fixture builder and the fixtures' listing. It also confirmed the six outputs were absent. My `shasum` gives the same digests.

32. L53: "every overlay file against its blob at `91f0d35` (173 of 173), and the package digest by shell;" **CONFIRMED.** See item 4. The 35's 22nd printed "package by shell: 06b55761…1d39".

33. L54: "the two snippets, extracted at n-build's sha256s and read whole (standard library only);" **CONFIRMED.**
   - The 35's 24th printed `49c95fdb…b595` (6 lines) and `f1725204…8ecd` (74 lines), which are n-build's digests.
   - My `sed -n '175,180p'` and `sed -n '186,259p'` of the script, piped to `shasum`, give the same.
   - Their imports are json and sys; and hashlib, json, sys and pathlib.
   - A Read of lines 173–260 came before the grant.

34. L55: "the `hashes` command's code;" **CONFIRMED.** The 35's 25th read `cmd_hashes` in overlay91's driver with `grep` and `sed`.

35. L56: "the laptop (only PID 8051)." **CONFIRMED.** The 35's 22nd ends with `pgrep -il python`, which printed "8051 python3.12".

36. L58: "It did not read the fixture files, whose paths mimic `data/n/ckpt` and `data/n/reports`." **CONFIRMED** for "did not read". No command in the 35 or the 22 names a path under `cases_1`, `cases_2`, a folder in `test/`, `reviewed_v1` or `statussim` (`grep -c`: 0). The three `test/` files that were hashed sit directly in `test/`. The paths' shape: see observation 8.

37. L60: "the six run files at n-build's sha256s, both exits 0, stderr empty;" **CONFIRMED.** The 22's 8th printed "ok" for all six, "exits: exit 0 / exit 0", and 0 bytes for `hashes_run1.err`. My `shasum` equals n-build's digests, `cat -v` shows "exit 0" twice, and `wc -c` of the stderr file is 0. On run 2's stderr, see observation 2.

38. L61–62: "`gtime_hashes_v1.txt`, 13 lines: its package line the lock's `06b55761…1d39`, its 12 closure pairs in the committed driver;" **CONFIRMED.**
   - The file has 13 lines: 12 `imported_sha256` and 1 `package_sha256`.
   - Its line 1 equals the quoted package line.
   - That digest is the driver's `LOCK_PACKAGE_SHA256` at `91f0d35` (1 match) and appears in `LOCK-n.md` at `91f0d35` twice.
   - I ran `grep -o -F -f`, with the 12 pairs built as `"path": "digest"` patterns in a process substitution, over `git show 91f0d35:scripts/n_sessions.py`: 12 distinct matches.

39. L63: "the snippet test: 95 of 95 fixtures, identity_of's three lines, 62 of 62 mutants killed;" **CONFIRMED.** `run_2.txt` (67 lines) has these lines:
   - "check_outputs: 95 of 95 fixtures as wanted"
   - "identity_of: its three lines, as wanted"
   - "mutants: 62; killed 62, survived 0 (), not applied 0"
   - last line: "snippet test: fixtures 95/95, identity_of 0, mutants 62/62"

40. L64: "the tree unchanged, and PID 8051 alone." **CONFIRMED.** The 22's 8th printed "HEAD 91f0d35; tracked diffs 0; staged 0" (by item 3's pathspec plus the campaign's) and "8051 python3.12".

41. L65–67: "… a `ps` that printed two command lines, and an unpruned `find -newer` over its test folder, which it stopped." **IMPRECISE.**
   - n-build's close report says the find ran "over the launch folder. Its test/ holds the harness's fake copies…". It was stopped before it finished and redone with `test/` pruned.
   - The other three departures are as n-build gives them: one `grep`, one `zsh` heredoc, and `ps -o args=` printing two command lines. They are also in its departures log for the next entry.
   - Fix: "… and an unpruned `find -newer` over its launch folder, whose test/ holds the harness's ckpt- and reports-shaped copies; it stopped it before it finished and redid it with test/ pruned."

42. L68–69: "(`c9d35e2..5f62dd1`, in the coordinating session's own window): 4 commits, 17 file-diffs, 5,092 added lines (messages included), every class CLEAR." **CONFIRMED.**
   - `screen15.txt` reads "4 commits, 17 file-diffs, 5092 added lines (messages included)". Its six classes (url_host, ipv4, email, port, pod_token, local_path) all show "0 distinct; inside: 0 -> CLEAR", and "screen4 exit=0".
   - My `git log --name-only` over the range with the full pathspec: 4 commits, 17 names.

43. L69–70: "gitleaks 8.30.1 found one item, the known file digest at `scripts/n_sessions.py`:3787 in `91f0d35`; gl5 classed it a file digest, exit 0. No halts." **CONFIRMED.**
   - `gl15_run.txt`: "4 commits scanned", "leaks found: 1", "gitleaks exit=1".
   - `jq` over `gl15.json`: 1 finding, generic-api-key, at line 3787 of that file, commit `91f0d35`, with a 64-character hex secret.
   - `gl5_15.txt`: "('outside', 'generic-api-key', 'digest:file') x 1", "gl5 exit=0".
   - `gitleaks version` prints 8.30.1. The session's own version check in the 100 printed the same binary.
   - No "inside" matches, so no halts.

44. L70–71: "The push waits for the PI's word (item 4 of the raw's routing block)." **CONFIRMED.** The seat's raw at `5f62dd1`, line 46: "4. Nothing to push at this read; the next push after the spec raw's commit [yours]."

45. L73–74: "22 commands, the last of them the sweep; the commands after it are this commit's own." **CONFIRMED.** See the base check above. The four commands after the sweep build this entry's draft and brief, and append to the memory folder.

46. L76–77: "`5f62dd1`'s own commands: the placement's asserts and three `cp`, the staging, three gate runs, the commit and its verification." **CONFIRMED.**
   - placement: the 22's 6th and 9th (the 9th has the three `cp`);
   - staging: the 10th (`git add`);
   - gates: the 11th–13th;
   - commit: the 14th;
   - verification: the 15th, which ended "VERIFY PASS".

47. L78–79: "The first gate run named a loop variable `path`, which zsh ties to `PATH`. Every later command in that run failed to find `git`, and the gate ended FAIL." **IMPRECISE.** The 11th printed ten "command not found: git" lines and one "command not found: pgrep". Its four index checks still printed "ok index … = its source", because both sides were empty strings. It then printed "FAIL HEAD" and "GATE FAIL", and exited 1.
   - Fix: "The first gate run named a loop variable `path`, which zsh ties to `PATH`. Every later `git` in that run, and its `pgrep`, was not found; its four index checks printed "ok" on two empty strings, and the gate ended FAIL."

48. L80: "The second ended FAIL at a guessed count of added lines, which left out blank lines." **IMPRECISE.** The 12th counted added lines with `grep -c -E '^\+[^+]'`, then tested `[ "$al" -gt 800 ]`. It printed "added lines 774" and "FAIL the staged diff looks empty". My recount of `git diff 91f0d35 5f62dd1` (full pathspec): 931 added, 774 by that pattern, 157 blank, and none starting "++". So the guess was the bar of 800; the count itself was computed and left out the blank lines.
   - Fix: "The second ended FAIL at a guessed bar, more than 800 added lines: its count, by a pattern that left out blank lines, was 774 of the 931."

49. L81–82: "The third, with exact counts (931 added, 0 removed, by `git diff --cached` and `--numstat` with item 3's pathspec), passed. Then came the commit." **CONFIRMED.** The 13th printed "added lines 931 (want 931 = 314 + 46 + 48 + 523), removed lines 0 (want 0)", then numstat lines of 314, 523, 48 and 46, then "GATE PASS (counts)". The 14th is the commit. My numstat of `91f0d35..5f62dd1` matches.

50. L83–84: "the screen: `/usr/bin/python3 -I` running `screen4.py` and `gl5.py`, with `gitleaks`; and `jq` over gitleaks' report in two commands;" **CONFIRMED** as far as it goes. The 22's 16th has `nice -n 19 /usr/bin/python3 -I` for both scripts, `gitleaks git … --report-format json` and `jq 'length'`. The 17th is the second `jq`. Its `git log` is a missing class (item 64).

51. L86: "`shasum`, `cat` of the exit files, and a name-only `ls` of the snippet test's output folder, counted;" **CONFIRMED.** The 8th and 18th use `chk` (`shasum`) and `cat` of both exit files. The 8th also has `ls "$L/snippet/run_2" | wc -l`, which printed 67.

52. L87: "`git show 91f0d35:scripts/n_sessions.py`, piped to `grep` per closure pair (the loop above);" **CONFIRMED.** These are the 8th's twelve pipes.

53. L88–89: "the manifest's paths by `awk` and `sed`, and the manifest check (the loop above), with `git cat-file blob` of each blob;" **CONFIRMED.** The 19th runs `awk '{print $2}' | sed | sort | uniq -c | sort -rn | head -n 20`, then the loop.

54. L90: "one pruned `find` over overlay91, its marker-named paths counted from its output by a bracketed pattern;" **CONFIRMED.** The 20th runs the pruned `find` into `grep -c -i -E` with the bracketed pattern. It printed 20.

55. L91–93: "git forms in checks: `git cat-file commit` and `-p` of the commit, `git cat-file blob` …, and `git diff` of it against its parent with item 3's pathspec, its patch piped to `grep -c` for the counts;" **CONFIRMED.** These are the 15th's forms.

56. L94: "`pgrep -il python` in seven commands;" **CONFIRMED.** `grep -c` over the 22's texts gives 7: the 4th, 8th, 11th, 12th, 15th, 16th and 20th.

57. L94: "`awk` in four;" **CONFIRMED.** The 2nd, 4th, 5th and 19th.

58. L94: "`wc -l` in eight". **FAIL.** There are nine: the 2nd, 4th, 5th, 6th, 8th, 15th, 18th, 19th and 22nd. The sweep (the 22nd) also runs `wc -l`. Fix: "`wc -l` in nine".

59. L94: "`wc -c` in two;" **CONFIRMED.** The 6th and 8th.

60. L94: "`cmp` in three;" **CONFIRMED.** The 5th, 9th and 15th.

61. L94–95: "and `diff` of the checked drafts against their final texts;" **IMPRECISE.** The 2nd and 4th diff four draft–final pairs. The 6th also runs `diff "$R" "$N/RESULTS_new.md" | grep -E '^[0-9]'`, which printed the four insertion points.
   - Fix: "and `diff` of the checked drafts against their final texts, and of `RESULTS.md` against its rebuilt draft for the insertion points;"

62. L96: "`jq` over its transcript in one command, the sweep;" **CONFIRMED.** Of the 22, only the 22nd runs `jq` over the transcript. The 16th and 17th run it over gitleaks' report.

63. L96–97: "reads of its own sweep files and drafts; writes in its own scratch; and one append to its memory folder by `cat >>`;" **CONFIRMED** as far as it goes. Writes by `>` and `mkdir -p` in the 5th, 6th, 15th, 16th and 22nd all land in its own scratch. There is one `cat >>` heredoc, in the 7th. Its read of the memory file is a missing class (item 66).

64. Missing class: `git log` without item 3's pathspec. **FAIL.** The 22's 16th runs `git log --format='%h %s' c9d35e2..5f62dd1 | cut -c1-90` with no pathspec, and it printed the four subjects. `5f62dd1`'s entry declares this same form for its own commands.
   - Fix: in L83–84, after "with `gitleaks`;", add "`git log --format='%h %s'` of the range, item 1's form without item 3's pathspec;".

65. L98–99: "beside the shell: two messages to n-build (the window's close and the set's acceptance), and the Read tool on the launch script, the note and the dispositions;" **IMPRECISE.** `jq` over the non-shell calls between the two sweeps finds:
   - SendMessage 2;
   - Read 5 (the script twice, the note, the dispositions, and its own entry draft);
   - Edit 7 (its entry draft);
   - Write 1 (the commit message);
   - update_plan 2;
   - wrap_up 1.

   Fix: "beside the shell: two messages to n-build (the window's close and the set's acceptance); the Read tool on the launch script (twice), the note, the dispositions and its own entry draft; the Edit tool on that draft seven times and the Write tool once (the commit message); and two plan calls and one wrap-up call;"

66. Missing class: a read in the memory folder. **FAIL.** In the 7th, after the `cat >>` heredoc, `tail -n 1` of the same memory file was piped to `cut -c1-60`. It printed the appended line's head. `5f62dd1`'s entry declared the like ("one `grep` read of a memory file").
   - Fix: "and one append to its memory folder by `cat >>`, with a `tail -n 1` read of the appended file (60 characters);"

67. Missing class: reads and counts over n-build's files beyond the forms listed.
   - **FAIL.** The 8th runs `head -n 1` of the hashes file, which printed the package line.
   - It also runs `grep -E '^(snippets:|check_outputs:|identity_of:|mutants:|snippet test:)'` over `run_2.txt`, which printed five lines.
   - The 18th has 20 `grep -c` counts over the four box files.
   - The 19th runs `grep -c -E` for ckpt, reports and campaign lines, plus four `grep -c -F` for named paths over the manifest.
   - The 20th runs `grep -c -i -E` (bracketed) over the manifest, which printed 17.
   - Fix: under "the checks of n-build's window close and launch set", add "- `head -n 1` of the hashes file and `grep -E` of `run_2.txt` for its summary lines; counts by `grep -c` over the four box files (IPv4-like strings, "port", "ssh", local roots and the user name: 20) and over the manifest (its ckpt, reports and campaign lines, four named paths and its marker-named paths);".

68. L102–103: "Committed by path … The commit-time count of the home-folder prefix over the staged diff is 0. Nothing ran on a model. Not pushed." **NOT CHECKABLE.** The commit has not been made yet. At this check HEAD is `5f62dd1` and origin is `c9d35e2`. No model process appears in the 22 or the four after them; the only Python is the two screen scripts.

69. Placement: "this entry … after line 23 and nothing else changed". **CONFIRMED.** I ran `cmp` of `{ git show 5f62dd1:RESULTS.md | sed -n '1,23p'; cat entry.md; git show 5f62dd1:RESULTS.md | sed -n '24,$p'; }` (a process substitution) against the draft: equal. Line counts: 35,000 + 104 = 35,104. The entry ends with an empty line (`tail -c 2 | od -c` shows `\n \n`).

70. Line lengths. **CONFIRMED.** `grep -c -E '^.{121,}'` over the entry prints 0 in a UTF-8 locale and 0 in the C locale.

71. Hash abbreviations and figures. **CONFIRMED.** I re-made all five abbreviations in the entry with `cut` (`eeee8c2e…39b6`, `84550072…957b`, `a853932b…522b`, `036968c0…2369`, `06b55761…1d39`). Every count not covered above checks too: 173, 20, 40, 1, 17, 58, 66, 12, 13, 95, 62, 4, 17, 5,092, 3787, 931, 0 and PID 8051.

## Observations

1. After the overlay loop, the next process check came only at the 22's 4th command, after the last sweep. The 35 have no check after their 23rd: `pgrep` ran in their 20th and 22nd, and the other three "pgrep" hits are count patterns. That PID 8051 is the Q-F3 campaign rests on the coordinating session's record; I ran no process read, by rule.
2. Run 2's stderr went into `run_2.txt` (`2>&1`, as n-build's request writes it). So "stderr empty" rests on `hashes_run1.err` (0 bytes) plus `run_2.txt` holding only its 67 expected lines: 3 summary lines, 43 m-mutants, 19 b-mutants (each "killed by …"), and 2 closing lines.
3. The acceptance message to n-build says "all twelve you listed are at your sha256s". n-build listed fourteen. All fourteen check, and this is not committed text.
4. "Eight" `wc -l` commands is the count over the first 21 of the 22. That is the coordinating session's `bash_after_last_21.tsv`, made after the sweep, which equals the 22's first 21 lines by `cmp`. The 22nd adds one more `wc -l`.
5. The 22's 5th exited 1 at a `grep -c` with no match (it printed 0). `5f62dd1`'s entry declared the same kind of exit for its 35; this entry does not.
6. The screen command's `cat` and `sed` of its own four push15 files fall under no class in the list.
7. The script's header and the note's box section name the pod only by its id, never by an address or port. That fits the routing's "no pod IP or port".
8. I did not check the fixture paths' shape, because the brief forbids listing them. n-build's close report gives that shape for `test/`'s copies. For the fixtures, the claim rests on the coordinating session's own grant message.
9. The first gate compared two command substitutions, so it passed vacuously when `git` was missing. The second gate added a 40-character check on the index id, which closes that hole.
10. The coordinating session rebuilt the draft from the working tree's `RESULTS.md`, after asserting it equals HEAD's blob. My rebuild from `git show 5f62dd1:RESULTS.md` matches it.
11. The after-commit loop check (the 22's 21st) cannot see loops inside scripts. The `pkgsha.sh` loop needed a separate check of `valence_core/n`'s names (item 6).

## My own departures

- **The transcript:** `jq` over `<transcript>` in 24 commands, 79 calls. They printed:
  - main-thread shell commands, rebuilt and compared with the sweep files by `cmp`;
  - tool results by id (4 of the 35, 21 of the 22, 1 of the 100);
  - n-build's three afternoon messages, whole, and an earlier message's B-lines;
  - the coordinating session's messages to n-build and one to the earlier checker;
  - its Read inputs, non-shell call tallies and error flags;
  - the 3 commands before the first sweep and the 4 after this sweep.

  Also one `wc -l` of the transcript (55,631) and one `grep -n -F` of it for the cross-session tag, which printed line numbers.
- **The sweep files:** read in about 23 commands, by `sed`, `cut`, `grep -c/-n/-o`, `head`, `tail`, `sort -c`, `cmp`, `wc -l` and `shasum`. Also `bash_after_last_21.tsv`, which is not a named source, compared once by `cmp`.
- **git forms:**
  - `git show <rev>:<path>` naming one file outside `data/`, in 10 commands: `RESULTS.md` at `5f62dd1` and `91f0d35`; the driver and `LOCK-n.md` at `91f0d35`; the seat's raw at `5f62dd1`.
  - `git cat-file --batch-check` twice, fed on stdin, and `git cat-file blob` of 66 blob ids, in one command.
  - The `git diff 91f0d35 5f62dd1` patch with the full pathspec, piped to six `grep -c` counts, plus `--numstat`, in one command.
  - `git ls-tree -r --name-only 91f0d35 -- valence_core` once, without item 3's pathspec; a count.
  - Item 1 forms with the full pathspec: `git log --format` (ids, subjects, a commit time) in two commands, `git ls-files`, and `git show --name-only` of five commits.
  - Also `git rev-parse` and `git --version`.
- **n-build's files:**
  - `shasum` of 21 launch-folder files. One command shortened them with `sed`, against the brief's `cut` rule; I redid it with `cut`.
  - `cat -v` of the two exit files; `wc -c` of the stderr file.
  - Reads by `sed`, `grep`, `head`, `tail` and `cut` of the script, the note, the dispositions, the manifest, the hashes file and `run_2.txt`.
  - `grep -c` counts over the four box files (36 counts).
  - Outside the launch folder: `cat -n` of `<nb>/schema/pkgsha.sh`; `wc -l` and `grep -c` of two commit-window manifests; name-only `ls` of `valence_core/n` in the four earlier overlays.
- **Listings:** name-only `ls` of `<own>`'s notes, notes2 and push15 folders; n-build's launch and snippet folders; five copies of `valence_core/n` (counted); and the snippet run folder, piped to a count (67). Nothing in `test/`, `cases_1`, `cases_2` or `reviewed_v1`.
- **Pruned `find`s** over overlay91: 8 in 2 commands, counted from the stream. They also walked overlay91's copy of the code package named like the campaign folder, counted with the name masked.
- **Counts:** `wc -l` and `grep -c` in many commands; `cmp` in three.
- **Other programs:** `gitleaks version` and `command -v gitleaks`, once each; `od -c`, `paste` and `TZ=UTC`, once each.
- **Shell incidents:** one heredoc, which zsh may back with a temporary file; one output sent to the null device; three BSD `grep` errors (a repetition count over 255) in one command; and `grep -c` exiting 1 at 0 in three commands.
- **The memory folder's path** appeared as a masking `sed` pattern in four commands. Nothing in it was listed, globbed or read.
- **Read tool:** the brief and the entry.
- **In my own tool output only, and not here:** local roots with the user name, session ids, n-build's session id, the pod's id, agent ids, folder names holding a marker, and gitleaks' install path.

By my account:
- I wrote no file, apart from the heredoc noted above.
- I used no interpreter but `shasum` and `jq`, and no network.
- I ran no `ps`, `pgrep` or `stat`, and no whole-tree `git status`.
- No command text held a marker word or the plain campaign name; I used bracketed forms only.
- I passed no marker-named path as an argument.
- I listed and read nothing under `data/m[f]3`, `data/*/ckpt`, `data/*/reports`, the fixture folders or `test/`'s folders.

## Tallies

71 items: 56 CONFIRMED, 7 IMPRECISE (7, 14, 41, 47, 48, 61, 65), 7 FAIL (5, 9, 18, 58, 64, 66, 67), 1 NOT CHECKABLE (68). 11 observations.
```
