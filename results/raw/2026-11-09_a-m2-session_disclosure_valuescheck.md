# The A-m2 session's O2-3 disclosure — the values-check of the block and its entry, in two passes

*Code's raw, PI date 2026-11-09.*
- *What was checked:* the drafts of `2026-11-09_a-m2-session_code-to-design_disclosure.md` (D1) and of its RESULTS.md
  entry (D2).
- *How:* two blind agents, read-only, each under a brief that states §1.3 of the seat's answer of 2026-11-09 and
  permits only a bare `git status --porcelain`, a name-only `ls` and `git ls-files` on the blinded directories.
  - Each parsed the session's transcripts itself, and viewed every output concerning a blinded directory masked, with
    every run of digits replaced by `N`.
  - Each discloses its own commands at the end of its report.
- *The reports:* each agent returned its report as its hand-back. Code extracted the text from the agent's transcript
  by script, byte for byte.
  - Local paths are scrubbed (`<tmp>`, `<tmp-session>`, `<session-dir>`, `<repo>`, `<home>`) and the session id is
    shown as `<id>`.
  - The temp directory's name, `claude-501`, stays where the reports quote it as a search term.
- *Nothing ran on a model.*

## Code's dispositions

- **Pass 1** (71 items: 45 PASS, 17 IMPRECISE, 9 FAIL, 0 NOT CHECKABLE; 13 calls missing, plus one listing).
  - The FAILs were the sweep's coverage and the block's claims of completeness:
    - 29 of 39 subagents swept;
    - `--stat` calls dropped when the command did not name `data/`;
    - the reviewers' worktrees;
    - the sweep's own repository commands;
    - "none printed a name";
    - A1′ missing.
  - Code re-swept all 40 transcripts with output-based detection and a per-invocation `git grep` check, and
    reproduced the check's list.
  - D1 was rewritten, adding M1–M6, Q1–Q7 and A1′, and fixing every IMPRECISE item. Each added fact was checked
    against its transcript, masked.
- **Pass 2** (68 items: 49 PASS, 17 IMPRECISE, 2 FAIL, 0 NOT CHECKABLE; five calls missing, none of them in an O2-3
  form).
  - Both FAILs were the rewrite's claim that the sweep found nothing beyond pass 1's list. That claim is withdrawn.
  - The five calls are now in D1: three `git log` calls that printed commit ids (§4) and two greps of named report
    files (§3). Code checked each against its transcript, masked.
  - Every IMPRECISE item was applied:
    - the exclusions in §1;
    - the HEADs and worktree commits of A2, M2, M4 and M6;
    - Q1's `git log` part;
    - C's scalar values;
    - the sweep's own commands in §5;
    - the brief bullets in §6;
    - §7 items 1 and 5;
    - D2's brief nuance, its `ckpt` directory row and its hashes.
- **Not run:** a third pass. The applied changes are wording and the five additions, each checked by tool.

## Pass 1's report (verbatim; paths scrubbed)

# Blind values-check of D1 (disclosure block) and D2 (entry)

**Result: 71 items. 45 PASS, 17 IMPRECISE, 9 FAIL, 0 NOT CHECKABLE.**

The stamps, commit ids, HEADs, windows and quotations hold. The completeness claims do not. 13 calls that reached blinded directories inside their open windows are missing from D1. Four of them printed a checkpoint's own size, which D1 never mentions for Q-F3.

**Method.**
- I parsed every Bash call since 2026-11-06T05:00Z myself, not with the author's scripts: the main JSONL and all 39 other subagent transcripts in `<session-dir>/subagents/agent-*.jsonl`. My own transcript, `aa3d77d08f3554296`, was excluded.
- Every output line naming ckpt or reports was viewed with each digit run replaced by `N`.
- Commit times come from `git log -1 --format`, ancestry from `merge-base --is-ancestor`.

## D1

**Header**
1. "Under: §1.3 … committed at `2853e66`": **PASS.** `2853e66` added the answers file, 2026-11-09T22:29:34Z.
2. The §1.3 quotation: **PASS.** Verbatim with answers.md:32.
3. "no size, time or line count that printed": **PASS.** D1 reproduces none.
4. "Code's checks … printed only paths, stamps and shapes, with every run of digits replaced by N": **IMPRECISE.** sweep.py's run at 23:04:00 printed six stat lines unmasked, as D1 §1 itself says. Fix: "Code's later checks …".

**§1 How they were found**
5. `353502f` at 2026-11-09 22:55:04 UTC, and the relay coming after it: **PASS.** The relay message arrived at 22:55:54Z.
6. "every shell call this session made from 2026-11-06 (05:00 UTC)": **PASS.** sweep.py ran from `2026-11-06T05:00:00` over the main JSONL; the transcript itself begins at 2026-11-06T20:56:04Z.
7. "every shell call of the 29 subagents it launched in that time": **FAIL.**
   - The session launched 39 subagents before the sweep (2026-11-06T22:01:32Z to 2026-11-09T20:44:14Z), 40 counting this check.
   - `tasks/a*.output` links only the 29 launched from 2026-11-07T18:48:59Z.
   - The other ten were never swept: `a0745e2a`, `ae175a5b`, `aebb18af`, `a40f6ac1`, `ab59c8c4`, `a79e1a12`, `a4bd7951`, `a6af4087`, `a3dc0223`, `ab2a2438`. Their transcripts are at `<session-dir>/subagents/agent-<id>.jsonl`.
   - Three of those ten (`a4bd7951`, `a6af4087`, `a3dc0223`) printed G-CAL OLMo metadata inside m OLMo's window (M1–M5 below).
8. "…and every call naming `data/`": **IMPRECISE.** Only scan.py selected every call naming `data/`, and it ran only from `2026-11-09T05:00:00` (the 22:57:19 and 22:58:00 calls). The sweep from 2026-11-06 selected form calls only.
9. "How each hit was checked: against its own result": **FAIL.**
   - sweep.py flagged 33 calls whose output named a ckpt/reports path. I reproduced the same 33.
   - Its view (`grep -A6 … | head -80`) showed only main-session calls.
   - The 23:04:31 filter missed calls whose command did not name `data/` within its 230-character cut.
   - Five flagged calls that printed blinded metadata are absent from D1: Q1–Q5 below.
10. m OLMo window, `6ce8b9a` 2026-11-07 03:14:07 to `0f35954` 05:11:57: **PASS.**
11. Q-F3 launched 2026-11-08 03:41:55, `acc3b52` 04:35:06, window open: **PASS.** The raw header reads "Code stamp at launch: 2026-11-08 03:41:55 UTC".
12. p: `b6ef939` 2026-11-08 05:10:23 and `2258c52` 2026-11-09 18:51:56, both open: **PASS.**
13. Q-F0 closed at its VERDICTS, 2026-10-19: **PASS.** `bfc179c` and `0fa8539`, both 2026-10-19 UTC.
14. "Hits not listed below: each reached no ckpt or reports directory, or ran while that directory held nothing blinded": **FAIL.** See "Missing from D1".
15. "`--stat` calls on commits that touch none": **PASS** as a class.
16. "recursive greps limited to files of other kinds": **PASS.** Every in-window `grep -r` from `.` used `--include` for `*.md`, `*.txt` or `*.py`. The five blinded directories hold only `.json`/`.jsonl` names (name-only `ls`).
17. "finds over scratch directories and worktrees made before Q-F3's run or `b6ef939`": **FAIL.**
   - `ganl-wt` was made at `273ca8f`.
   - It was then checked out at `0415438` (03:56:52) and on `e7e070f` (04:32:17). Both descend from `6ce8b9a` and hold `data/m/ckpt/G-CAL_olmo-*`.
   - `a6af4087`'s finds over it at 04:35:10 fall inside m OLMo's window (M4).
18. "It read transcripts, not the repository": **FAIL.** The sweep also ran git on the repository:
   - E5, at 22:57:43 and 22:59:03 (§5 itself calls it "for this sweep");
   - `git log --diff-filter=A … -- data/mf3/ckpt` etc. at 23:06:14;
   - a `git grep … ':!data/**'` at 23:06:49;
   - `git log --before` at 23:08:28;
   - `git log`/`merge-base` at 23:09:30.
19. "Its first pass printed the three G-CAL sizes of A1 again, unmasked": **IMPRECISE.**
   - The pass was sweep.py at 23:04:00. scan.py and show_calls.py ran earlier and printed no sizes.
   - It printed six lines: A1's three and A2's three, the same sizes twice.
   - "After `0f35954`" is right.
20. "Every later pass masked digits": **PASS.** No later output shows a digit-bearing ckpt/reports metadata row. The 23:05:35 rewrite of `sweep_all.txt` kept digit counts (`#`), but that file was not printed afterwards.

**§2 Metadata printed while a window was open**
21. A1 (03:22:19, `git diff --stat 54bbfe5 HEAD`) and A2 (03:56:31, `git diff --stat 273ca8f 0415438`), HEAD `0415438`: **PASS.**
22. "The rest were gate and manifest lines": **IMPRECISE.** The rest also included `results/raw` lines (four in A1; nine plus `RESULTS.md` in A2) and the summary line.
23. A1/A2's window, and "no verdict": **PASS.**
24. B (`a37a150c`, "Referent check of ADDENDUM-m2 v0.1"): HEAD `daca8b0`, 07:25:04, the command: **PASS.**
25. B, what printed: **PASS.** Masked rows for `.`, `..`, `ckpt`, `gates`, `reports` and `schedules`; the two report files; the schedules rows.
26. C (`a95333e0`): HEAD `c9acd66`, its brief said "HEAD daca8b0", 07:54:36, `wc -c`: **PASS.** The literal command was `wc -c $R` with `R=data/mf3/reports/Q-F3_time_reads.json`.
27. C "printed the structure of its JSON": **IMPRECISE.** The walk printed keys, types, list lengths and scalar values (repr cut at 100 characters).
28. D (`a5974ae2`): HEAD `c9acd66`, 08:20:35, the command, line counts: **PASS.**
29. E: 08:21:36, `ls -la data/mf3/reports/`, sizes and times: **PASS.** It also printed the directory's own `.`/`..` rows, and its `json.load` printed the reads file's keys.
30. "They are O2-3's named forms", and the docstring quote and anchor `scripts/mf3_sessions.py:46–48` at `9c7062e`: **PASS.** The sentence spans lines 46–48 verbatim.
31. "ran on the run's own files in the main checkout": **PASS.**
32. "The briefs … barred opening `data/mf3/ckpt`": **PASS.**
33. "They said nothing about the metadata of `data/mf3/reports`": **IMPRECISE.** True as worded, but:
   - C's brief: "Commits cited (`fb742e4`, `18b0111`, `daca8b0`, `acc3b52`, `acde2d8`, `1e79955` …) can be checked with `git show --stat` or `git log`."
   - D's brief asked it to confirm "that the first run's report and reads were committed at `acc3b52`".
   - So the briefs pointed at the form that printed the checkpoint's size and the reports' line counts.
34. "one of them named the reads file as a source": **FAIL.** Two did:
   - B's: "the reads file data/mf3/reports/Q-F3_time_reads.json, which is pick-free and readable".
   - C's: "The reads file = `data/mf3/reports/Q-F3_time_reads.json`. It is sham-redacted and allowed."
35. R3 (`a9501347`): smoke worktree at `daca8b0` (made 2026-11-08 07:42:45), 04:58:55, command, what it reached, printed nothing: **PASS.** Note that `-newer` follows `-name`, so it was evaluated only on entries named `__pycache__`.
36. R6b: 07:00:57, `review-wt` at `daca8b0`, pruned `ckpt` only, written to `after_status.txt` and diffed, "STATUS SAME": **PASS.**
37. "counted only the traversals into `data/mf3/ckpt` ('Every later traversal pruned ckpt')": **IMPRECISE.** The quote is verbatim. But the same 07:00:57 call ran an unpruned `find . -name __pycache__ -not -path './.git/*' -print 2>/dev/null | grep -v '^./data/mf3/ckpt' | head`, so the quoted sentence was itself inaccurate. See Q6.

**§3 Content searches**
38. P: 04:52:38, HEAD `e0b4f2c`, the command, read G-CAL ckpts in the window: **PASS.**
39. P "What printed: one name, under data/olmo": **IMPRECISE.** Thirty names printed (cut by `| head -30`), one of them under `data/` (`data/olmo/lockg_valuescheck.json`). `data/m/ckpt` sorts before it, so no ckpt file matched.
40. E1: 21:10:14, HEAD `2258c52`, two `git grep -l` over every tracked file (a third was limited to `results/raw`), the session id's prefix: **PASS.**
41. "the temp directory's user name": **IMPRECISE.** The term was `claude-501`, the temp directory's name (uid-keyed), not a user name.
42. "They read `data/mf3/ckpt`, `data/mf3/reports` and `data/p/ckpt`/`reports`": **PASS.**
43. "first matched nothing; second listed five `results/raw` names; path order": **PASS.** The output was cut by `| head -5`.

**§4 Name-only traversals**
44. §1.2 ruled one of this kind "not O2-3's form; inert": **PASS.** answers.md:22–23 reads "Not O2-3's form; inert."
45. "None printed a name from `data/`": **FAIL.** E2, in this same section, printed 15 names under `data/p`.
46. R4: five stamps; two `__pycache__` searches pruning only `.git`, two pruning nothing, one counted with `wc -l`; one symlink search: **PASS.**
47. R5: three unpruned searches at 06:03:20, 06:26:29 and 06:30:27: **PASS.**
48. R6's partly pruned traversals: **IMPRECISE.**
   - The hashing pass read every file under `data/mf3/reports` and `data/p/ckpt` in `review-wt`. That is a content digest (§1.2's hash bullet), not a name-only traversal.
   - Two traversals are omitted: Q6 and Q7.
49. E2: 21:10:49, HEAD `2258c52`, 19 names, six under `data/p/ckpt` and nine under `data/p/reports`: **PASS.**

**§5 After the rule**
50. `2853e66` at 22:29:34, "after Code was told": **PASS.** The relay arrived at 22:55:54.
51. E5: HEAD `353502f`, 22:57:43 and 22:59:03; three commits, then seven with `-- data/`, then `git ls-files`: **PASS.**
52. E5's `data/` names: `web2.txt` and three `.md` files (`data/m/gates/G-CAL_seat_read_of_record.md`, `…_request.md`, `data/n/bk/SOURCE.md`): **PASS.**
53. "`git ls-files` is on §1.3's list. `git show --name-only` is not.": **PASS.**
54. §5's completeness: **FAIL.** It omits the 23:06:14 `git log` (A1′ below).

**§6 Briefs and §7 For the seat**
55. "No brief Code gave before §1.3 stated it": **PASS.**
56. Q4 and the shared forms: **PASS.** 353502f's raw, §6 Q4: "Which list governs for Q-F3 before its VERDICTS?"
57. The `':!data/**'` pathspec: **PASS.**
58. §7 item 1, "on Q-F3's G-TIME reports": **IMPRECISE.** The same checkers also printed the checkpoint's own size (Q2, Q3).
59. §7 item 2: **IMPRECISE.** It needs M1–M5.
60. §7 item 5, "the whole set": **FAIL.**

## D2

61. Title line: **PASS.**
62. Link-text convention: **PASS.** It matches RESULTS.md lines 29 and 54.
63. A1/A2: **PASS.**
64. B–E summary: **IMPRECISE.** It is correct for the four calls listed, but the same checkers printed the checkpoint's size (Q2, Q3).
65. "said nothing about the reports' metadata": **IMPRECISE.** As item 33.
66. "R3 and R6b … in the review worktrees' copies … reached `data/mf3/reports` and `data/p/ckpt`": **IMPRECISE.**
   - R3 ran in the smoke worktree, not a review worktree.
   - R3 also reached `data/mf3/ckpt`.
67. P and E1: **PASS.**
68. "name-only traversals … (rounds 4, 5 and 6, and E2), and after it (E5)": **IMPRECISE.** Round 6's pass hashed contents, and A1′ is missing.
69. The four "For the seat" bullets: **PASS.**
70. "every brief Code writes states §1.3": **IMPRECISE.** D1 says briefs handed to blind reviewers. "git grep excludes data/": **PASS.**
71. "Nothing ran on a model or the box": **PASS.** No such call between 22:29 and 23:10Z.

## Missing from D1

**m OLMo window** (`6ce8b9a` to `0f35954`). None of these four agents was swept.
- **M1.** `a4bd7951`, 2026-11-07 03:19:50, main checkout, HEAD `0415438`.
  - Command: `git show --stat 6ce8b9a | tail -15`.
  - Printed: `data/m/ckpt/G-CAL_olmo-{dpo,instruct,sft}.json | Bin N -> N bytes`.
- **M2.** `a6af4087`, 03:59:30.
  - Command: `git -C <S>/ganl-wt diff --stat 5f9a696 bcd15c9` (also against `0415438` and `54c9d64`).
  - `bcd15c9` descends from `6ce8b9a`; `5f9a696` and `54c9d64` do not.
  - Printed: the same three G-CAL stat lines.
- **M3.** `a6af4087`, 04:19:28, main checkout, HEAD `e7e070f`.
  - Command: `git show --stat --format= 6ce8b9a | /usr/bin/grep 'ckpt'`.
  - Printed: the same three G-CAL stat lines.
- **M4.** `a6af4087`, 04:35:10, over `ganl-wt` (a scratch commit on `e7e070f`, holding the G-CAL OLMo files).
  - Commands: `find $WT -name '__pycache__' -type d -maxdepth 4` and `find $WT -name '*.pyc' -newer $WT/scripts/m_analyze.py`.
  - Unpruned traversals, the second a newer-than filter like R3's.
  - Printed nothing from `data/`.
- **M5.** `a3dc0223`, 04:59:54, main checkout, HEAD `e0b4f2c`.
  - Command: `ls -la data/m/ckpt/ | head`. It printed the sizes and modification times of the three G-CAL OLMo checkpoints, among other rows.
  - The same call opened `data/m/ckpt/G-CAL_olmo-dpo.json` with `json.load` and printed its top-level keys and its first record (up to 600 characters).
  - m:271 says G-CAL-OLMo generations "carry no pick".
- **M6** (name-only, for §4's set). `a6af4087`, 04:01:29: `git ls-tree -r --name-only HEAD data/m/ckpt`.

**Q-F3 / p windows**
- **Q1.** `a37a150c` (B's agent), 2026-11-08 07:23:54, HEAD `daca8b0`.
  - Command: `ls -la results/raw/… data/mf3/reports/Q-F3_time_reads.json`.
  - Printed: the reads file's size and modification time.
- **Q2.** `a37a150c`, 07:29:38, HEAD `daca8b0`.
  - Command: `git show --stat --format='%h %s' acc3b52 | head -14`.
  - Printed: `data/mf3/ckpt/Q-F3_time.json | Bin N -> N bytes` (the checkpoint's size) and both reports' line counts.
- **Q3.** `a95333e0` (C's agent), 08:00:37, HEAD `c9acd66`.
  - Command: a loop over nine commits including `acc3b52`, each `git show --stat --format= $c | tail -8`.
  - Printed: the same three stat lines.
- **Q4.** `ab35e9ab` ("Referent check of ADDENDUM-m2 v0.2"), 2026-11-09 03:30:06, HEAD `de729c4`.
  - Command: a loop over ten commits including `acc3b52`, each `git show --stat --format= $c | head -12`.
  - Printed: the same three stat lines.
- **Q5.** `ab2e7350` ("Blind referent check of A-m2 v0.3"), 05:23:19, HEAD `2018ffc`.
  - Command: `git show --stat=200 … acc3b52 -- . ':(exclude)data/mf3/ckpt' …`.
  - Printed: both reports' line counts.
- **Q6.** R6 (`acc4e37d`), 07:00:57, `review-wt` at `daca8b0`.
  - Command: an unpruned `find . -name __pycache__ -not -path './.git/*' -print | grep -v '^./data/mf3/ckpt' | head`.
  - It descended into `data/mf3/ckpt`, `data/mf3/reports` and `data/p/ckpt`, and printed nothing.
  - It contradicts round 6's "Every later traversal pruned ckpt".
- **Q7.** R6, 07:01:13, over `review-wt` at `daca8b0`.
  - Command: `find review-wt \( -path review-wt/.git -o -path review-wt/data/mf3/ckpt \) -prune -o -name __pycache__ -print | head`.
  - It reached `data/mf3/reports` and `data/p/ckpt`, and printed nothing.

**After the rule**
- **A1′.** Main session, 2026-11-09 23:06:14, HEAD `353502f`.
  - Command: for each of `data/mf3/ckpt`, `data/mf3/reports`, `data/p/ckpt` and `data/p/reports`, `git log --diff-filter=A --format='%h %cI' -- "$p" | tail -1`.
  - Printed: each directory's first-add commit id and commit time.
  - It is not on §1.3's list, and D1 §1's windows rest on it.

Round 6's own 06:40:36 and 06:40:42 traversals were disclosed and ruled at §1.1–§1.2, so they are not counted as missing.

## Tallies

71 items: 45 PASS, 17 IMPRECISE, 9 FAIL (7, 9, 14, 17, 18, 34, 45, 54, 60), 0 NOT CHECKABLE. Missing: 13 calls (M1–M5, Q1–Q7, A1′), plus M6 for completeness.

**Aside.** HEAD moved to `ddd95b0` (the pod session's §1.3 sweep, 23:12:04Z) after the drafts were written; place D2 against the current HEAD.

## Disclosure of my own commands

No departure from the rule, by my reading.
- **Commands on the repository** (`<repo>`):
  - `git log -1 --format` on the cited commits;
  - `git log` with no pathspec, or with `results/raw` paths only;
  - `git merge-base --is-ancestor`;
  - `git cat-file -e <commit>^{commit}` on three scratch commits;
  - `git show 9c7062e:scripts/mf3_sessions.py | sed`;
  - `git ls-files` on the five blinded directories (names, and once per-directory name counts);
  - a name-only `ls` of those directories piped through `grep -v` on `.json`/`.jsonl` (it printed only the directory headers);
  - a bare `git status --porcelain` (nothing tracked was modified);
  - reads of two `results/raw` raws, the G-TIME-F3 raw header, PROPOSAL-m line 271 and RESULTS.md link lines.
- No `git grep`, `find`, `du`, `stat`, `ls -l`, `wc -c` or `--stat` touched a blinded path.
- **Transcript outputs** about ckpt/reports were viewed only digit-masked. Those masked views showed:
  - `a3dc0223`'s printed keys and first record of `G-CAL_olmo-dpo.json` (key names, a pool name and booleans visible);
  - C's JSON walk of the reads file.
- **Files.** I edited no existing file. I created three helper scripts (`tx.py`, `cats.py`, `win.py`) in `<tmp>/blindvc/`. The harness saved three oversized masked outputs under the session's `tool-results` directory.
- The checkout was at `353502f` for most of the check; `ddd95b0` appeared at 23:12:04Z.

## Pass 2's report (verbatim; paths scrubbed)

# Second-pass values-check of D1 (disclosure block) and D2 (entry)

**Result: 68 items. 49 PASS, 17 IMPRECISE, 2 FAIL, 0 NOT CHECKABLE.**

The rewrite fixes every first-pass FAIL. All M1–M6, Q1–Q7 and A1′ are now in D1, with correct roles, stamps, forms and masked shapes. Every O2-3-form call (`ls -l*`, `wc -c`, `--stat`, `find -newer`) that reached a blinded directory inside its open window is in D1. No O2-3-form call is missing.

What remains:
- **Two FAILs.** Both are the new claim that the final sweep "finds nothing beyond" the first pass's list (D1 §1; D2 "adds nothing to it").
- **Three `git log` calls over blinded paths** are not in D1 (Missing 1–3).
- **Two greps of named report files** are not in D1 (Missing 4).
- **Some missing HEADs, and incomplete brief bullets.**

**Method.**
- I parsed every tool call since 2026-11-06T05:00Z myself: the main JSONL and all 40 other subagent transcripts (39, plus the first pass's for §5 only). I used only `type: assistant/user` records. The `api-request-blob` records replay tool_use blocks with no timestamp.
- Every output touching a blinded directory was viewed with each digit run replaced by `N`.
- HEADs come from main's linear commit times and from the worktree add/checkout commands; ancestry from `git merge-base --is-ancestor`.

## A. The first pass's FAIL and IMPRECISE items

1. (#4) Header, "Code's later checks … The one exception is the first pass of this sweep (§5)": **PASS.** No post-rule output after 23:04:00 carries a digit-bearing blinded row.
2. (#7) 39 subagents; 29 also linked from `tasks/`: **PASS.** There are 39 Agent launches from 2026-11-06T22:01:32Z to 2026-11-09T20:44:14Z. `tasks/` holds 31 `a*.output` symlinks into `subagents/`, 29 of them without the two values-checks.
3. (#8) What the sweep searched: **PASS** as a description of sweep2.py. Its limits are item 28.
4. (#9) Each hit checked against its result: **PASS.** Q1–Q5 are now listed.
5. (#14) "Not listed below": **IMPRECISE.** It still does not account for:
   - three `git log` calls over blinded paths (Missing 1–3);
   - reads of the Q-F3 reports' content: 43 `json.load` calls (Code 15; a37a150c 4, a95333e0 5, a5974ae2 7, ab35e9ab 4, abde282e 8) and two greps of named report files (Missing 4). Only C's bullet gives the reason;
   - round 6's own 06:40:36 and 06:40:42 traversals, already ruled at §1.1–§1.2.

   It also says hashes are not listed, while §4 lists round 6's. **Fix:** add "git log over a blinded path printing commit ids only", "reads of the reports' content, which the stage writes to be read (m:271)" and "round 6's traversals ruled at §1.2", or list them.
6. (#17) Finds over worktrees: **PASS.** It now says "held nothing blinded (ganl-wt before 0415438)", and M4 is listed.
7. (#18) "read transcripts, not the repository": **PASS.** The leftover omissions are in item 50.
8. (#19) 23:04:00 printed A1's and A2's six G-CAL rows unmasked: **PASS.** Rows with digits after the bar: 6, all six G-CAL rows; the seventh flagged line was command text.
9. (#22) A1's other rows "not under a ckpt or reports directory": **PASS.**
10. (#27) C printed "keys, types, list lengths and short scalar values": **IMPRECISE.** The walk printed every scalar's repr cut at 100 characters; the banner and transcript strings were cut, not short. **Fix:** "and scalar values, each cut at 100 characters".
11. (#33) Briefs pointed to `--stat`, and D's asked about acc3b52: **PASS** in D1 §6. The new gap is item 53.
12. (#34) B's and C's briefs named the reads file: **PASS** for B and C. The new gap is item 54.
13. (#37) Round 6's "Every later traversal pruned ckpt" does not hold for Q6: **PASS.**
14. (#39) P printed thirty names, one under `data/` (`data/olmo/lockg_valuescheck.json`): **PASS.** There were 30 names before `----`, in sorted order.
15. (#41) "temp directory's name (claude-501)": **PASS.**
16. (#45) §4 is now "printed no size or time", and E2's names are stated: **PASS.**
17. (#48) R6 hashes as a content digest; Q6 and Q7 added: **PASS.**
18. (#54) A1′ added: **PASS.**
19. (#58) §7 item 1, "Q2, Q3 and Q4 printed the checkpoint's size": **PASS.**
20. (#59) §7 item 2 names M1–M6: **PASS.**
21. (#60) §7 item 5, "the whole set": **IMPRECISE.** It still lacks Missing 1–3. These are not O2-3 forms and printed no size or time, but they are §4's kind (M6, E2).
22. (#64) D2, "in three calls the checkpoint's size": **PASS.** A new gap is in item 62.
23. (#65) D2, "said nothing about metadata": **IMPRECISE, still open.** D1 §6 got the nuance; D2 did not. **Fix:** add "though C's and Q5's briefs directed `git show --stat` on acc3b52, and D's asked to confirm the reports were committed there".
24. (#66) D2's R3 worktree wording: **PASS.**
25. (#68) D2, "name-only traversals … (rounds 4–6 …)": **IMPRECISE, partly fixed.** A1′ is added. Round 6 also hashed every file outside .git and data/mf3/ckpt at 06:40:52 and 07:00:57, a content digest, as D1 §4 says.
26. (#70) D2, "hands a blind reviewer": **PASS.**

## B. Claims the rewrite added or changed

27. §1 When and Sources: **PASS.**
    - `353502f` committed 22:55:04Z; the relay arrived 22:55:54Z.
    - The main transcript's first record is 2026-11-06T20:56:04Z.
28. §1, "every git log over such a path": **IMPRECISE.**
    - sweep2.py's GITLOGD regex needs the path written out after `--`. It cannot match Code's 04:10:32 loop `git log … -- $f`.
    - Non-recursive greps of named files were outside the search.
29. §1, how each hit was checked: **PASS.** This matches the masked checks at 23:41–23:43. Whether every hit got a disposition cannot be shown (see 30).
30. §1, "reproduces that list exactly and finds nothing beyond it": **FAIL.**
    - The sweep's own output, `audit/sweep2.txt` line 88, flags GITLOGD at a37a150c 2026-11-08T07:28:29 (`git log --oneline -2 -- data/mf3/reports/Q-F3_time_reads.json`). That call is neither listed nor excluded.
    - Line 85 flags the same kind inside Q1's call, which D1 describes only as an `ls -la`.
31. §1 windows: **PASS.**
    - 6ce8b9a 2026-11-07T03:14:07Z to 0f35954 05:11:57Z.
    - G-TIME-F3 launched 03:41:55 (raw line 2, "Code stamp at launch: 2026-11-08 03:41:55 UTC"); acc3b52 04:35:06Z.
    - b6ef939 2026-11-08T05:10:23Z; 2258c52 2026-11-09T18:51:56Z. A1′'s output shapes are `accNbN` ×2, `bNefN` and `NcN`.
    - Q-F0 closed: bfc179c and 0fa8539, both 2026-10-19.
32. §2 m OLMo preamble (six calls; the m:271 quote "they carry no pick"): **PASS.**
33. M1: **PASS.**
    - a4bd7951, main checkout, HEAD 0415438, 03:19:50, `git show --stat 6ce8b9a | tail -15`.
    - Printed three `data/m/ckpt/G-CAL_olmo-* | Bin N -> N bytes` rows.
34. A2's checkout and HEAD: **IMPRECISE** (minor). They are unstated. **Fix:** "(main checkout, HEAD 0415438)".
35. M2: **IMPRECISE.** The worktree's commit is missing.
    - ganl-wt was detached at scratch commit `bcd15c9` (parent 0415438, created 03:56:52Z). The same call's `git -C $WT log --oneline -6` shows it.
    - The rest PASSes: the three rows come from the 5f9a696..bcd15c9 pair only.
36. M3: **PASS.** Main checkout, HEAD e7e070f, 04:19:28, three rows.
37. M5: **PASS.**
    - a3dc0223, main checkout, HEAD e0b4f2c, 04:59:54.
    - The `ls -la data/m/ckpt/ | head` printed the `.` and `..` rows and the three G-CAL rows among the others.
    - The `json.load` printed the top-level keys and `records[0]` (≤600 characters).
38. Q1: **IMPRECISE.**
    - The `ls -la` part is right: a37a150c, main checkout, HEAD daca8b0, 07:23:54, the reads file's size and mtime.
    - The same call also ran `git log --oneline -3 --` over four results/raw files and `data/mf3/reports/Q-F3_time_reads.json`. It printed three ids with subjects (`dacaNbN …`, `accNbN …`, `dcNffeN …`). Add it.
39. Q2: **PASS.** `git show --stat --format='%h %s' acc3b52 | head -14` at 07:29:38 printed the ckpt row (`Bin N -> N bytes`) and two report rows (`| N +++`).
40. Q3: **PASS.** a95333e0, HEAD c9acd66, 08:00:37, nine commits with `tail -8`, the same three rows.
41. Q4: **PASS.** ab35e9ab, HEAD de729c4, 2026-11-09 03:30:06, ten commits with `head -12`, the same three rows.
42. Q5: **PASS.** ab2e7350, HEAD 2018ffc, 05:23:19, `--stat=200 … -- . ':(exclude)data/mf3/ckpt'`, two report rows.
43. "What Q1–Q5 and B–E share": **PASS.** This covers the docstring at 9c7062e:46–48 and the coordinating session's D1/Q1 being the same kind.
44. M4: **IMPRECISE** (minor). ganl-wt was at scratch commit `8e2cec3` ("final bytes on e7e070f", created 04:32:18Z), not at e7e070f itself. The first draft's values-check said "a scratch commit". The commands and "printed nothing" PASS.
45. Q6: **PASS.**
46. Q7: **PASS.**
47. R6's hashes, directory lists and symlink lists: **PASS.** At 07:00:57 the hash and directory lists were only diffed ("TREE SAME", "DIRS SAME").
48. M6: **IMPRECISE.** The checkout and HEAD are missing: main checkout, HEAD e7e070f. It printed eight names: three G-CAL_olmo, G-CAL_qwen and four Q-F0.
49. A1′: **PASS.** 23:06:14, HEAD 353502f; it printed each directory's first-add id and time.
50. §5, the sweep's own repository commands: **IMPRECISE.**
    - "(one call over a G-CAL checkpoint's path, inside the closed window)": the call is 23:05:35 `git log --diff-filter=A --format='%h %cI' -- data/m/ckpt/G-CAL_olmo-dpo.json`. It ran after m OLMo's window had closed. **Fix:** "on a path whose window had closed".
    - The list omits `git status --porcelain --untracked-files=no` at 22:59:50. That is not the bare form; it printed nothing.
    - It also omits `git show 9c7062e:scripts/mf3_sessions.py` at 23:00:51, which reaches no blinded path.
51. §5, the first pass's brief stated §1.3: **PASS.**
52. §5, "by its own account … only git ls-files and a name-only ls": **IMPRECISE** (minor). Its account also lists a bare `git status --porcelain`, run at 23:33:20.
53. §6, "C's brief pointed to git show --stat": **IMPRECISE.** Incomplete: Q5's brief (ab2e7350) said "Check that each named commit exists … (`git show --stat <hash>`)" for seven commits, acc3b52 among them.
54. §6, "B's and C's briefs named the reads file": **IMPRECISE.** Incomplete: Q4's brief (ab35e9ab) did too ("the reads file = data/mf3/reports/Q-F3_time_reads.json (sham-redacted; …").
55. §6, all five Q-F3 briefs barred opening data/mf3/ckpt and none mentions metadata: **PASS.**
56. §6, D's brief "that the first run's report and reads were committed at acc3b52": **PASS.**
57. §7 item 1: **IMPRECISE** (minor). B (07:25:04) also printed `data/mf3/ckpt`'s own directory row, with its size and modification time. That is the only time datum about the ckpt directory in this set. §2 has it; §7 does not.
58. §7 items 2–4: **PASS.**
59. D2's sweep bullet (39 subagents; first pass 29, `--stat` filter): **PASS.**
60. D2, "reproduces the check's list and adds nothing to it": **FAIL.** Same source as item 30 (sweep2.txt lines 85 and 88).
61. D2, "nine calls by five checkers", the roles, and the forms: **PASS.** The nine are Q1, B, Q2, C, Q3, D, E, Q4 and Q5.
62. D2, "reports' sizes, modification times and line counts, and in three calls the checkpoint's size": **IMPRECISE.** **Fix:** add "and in one (B) the ckpt directory's size and modification time".
63. D2 m OLMo bullet (two `git diff --stat`; four calls by three subagents, three `--stat` and one `ls -la`; one `json.load`): **PASS.**
64. D2, three newer-than filters (M4, R3, R6b), none printing from `data/`: **PASS.**
65. D2 `git grep` counts (P one, E1 two): **PASS.**
66. D2, after the rule: name listings plus A1′: **PASS.**
67. D2 "For the seat", "From now on", and "Nothing ran on a model or the box": **PASS.** No such call between 22:29 and 23:46Z.
68. Unchanged entries re-verified: **PASS.**
    - A1, B, C, D, E, R3, R4, R5, R6b, P, E1, E2 and E5.
    - The §1.2 quote, the docstring anchor, the m:271 quote, and the link and stamp convention (RESULTS.md :28–29, :53–54).

## First-pass items still open
- D1: #14 (item 5), #27 (item 10), #60 (item 21).
- D2: #65 (item 23), #68 (item 25).

## Missing from D1
None of these is an O2-3 form, and none printed a size, time or line count.

1. **Code, 2026-11-07 04:10:32 UTC** (main checkout, HEAD e7e070f), inside m OLMo's window.
   - Kind: `git log --format=%h -1 --diff-filter=A -- $f` over the three G-CAL checkpoint paths, plus one gates file.
   - Printed: `NceNbNa data/m/ckpt/G-CAL_olmo-{sft,dpo,instruct}.json`, the first-add id with no time. It is A1′'s kind without the time. Place: §4.
2. **a37a150c, 2026-11-08 07:23:54** (HEAD daca8b0). This is the `git log --oneline -3` part of Q1's own call (see item 38).
3. **a37a150c, 2026-11-08 07:28:29** (main checkout, HEAD daca8b0).
   - Kind: `git log --oneline -2 -- data/mf3/reports/Q-F3_time_reads.json`, beside a hash of the reads file and a JSON walk of it.
   - Printed: one id with its subject (`accNbN G-TIME-FN …`). Place: §4.
4. **Content searches of named Q-F3 report files**, all reading the readable product:
   - a37a150c, 2026-11-08 07:29:09 (HEAD daca8b0): `grep -c <backend id>` on the reads file printed `N`; `grep -o '"backend…"'` on Q-F3_time_report.json printed `"backend_identifier": "aNdadecNfNceNb"`, which RESULTS.md also carries.
   - ae6bed75 (blind code review of the smoke driver), 2026-11-09 03:47:15 (main checkout, HEAD 9624f70): `grep -c <backend id>` on the report.
   - List them, or add reads of the reports' content to §1's exclusions (item 5).

**Not counted as missing:**
- round 6's 06:40:36 and 06:40:42 traversals, ruled at §1.1–§1.2;
- head-wt's gcal precheck at 04:09:38 and 04:09:48, an existence check that printed only the paths `CHECKPOINT EXISTS at …/data/m/ckpt/G-CAL_olmo-{sft,instruct}.json`;
- abde282e's 04:21:34 mtime walk, which pruned all of `data/mf3` and ran before b6ef939.

## Tallies
68 items: 49 PASS, 17 IMPRECISE, 2 FAIL (30, 60), 0 NOT CHECKABLE. Missing: 4 entries (5 calls), none of an O2-3 form.

## My own commands
No departure, by my reading.
- **Repository, git:**
  - `git log` with no pathspec (main since 2026-11-06: ids, UTC times, parents), and `git log -1 --format` on single commits;
  - `git cat-file -t` on four scratch commits, and `git rev-parse daca8b0`;
  - `git merge-base --is-ancestor`. One first attempt failed on zsh word-splitting and printed git's usage text only;
  - `git ls-files` on the five blinded directories (names only), and a bare `git status --porcelain`;
  - `git show 9c7062e:scripts/mf3_sessions.py | sed -n 40,52p`.
- **Repository, reads:**
  - name-only `ls results/raw | grep`;
  - the answers raw; the o23-sweep raw (4+-digit runs masked); the G-TIME-F3 raw's first lines; PROPOSAL-m line 271; RESULTS.md link and stamp lines.
- No `git grep`, `find`, `du`, `stat`, `ls -l/-t/-s`, `wc -c`, `--stat`, or path-scoped `git log`/`git show` on any blinded path.
- **Transcripts:**
  - Every output concerning blinded directories was viewed with digit runs replaced by `N`. That includes M5's G-CAL record and the reads-file walks.
  - I printed some calls' commands (inputs) with digits intact. One (a95333e0 08:00:50) contains sums of G-TIME-F3 session seconds from the stage record: content figures, not a file size or time.
  - I printed counts of tool-output lines for some calls. None is a blinded file's line count.
- **Other:** `ls -l` of the session's `tasks/` directory, which is not blinded, to confirm the links.
- **Files:** I created new helpers and masked scan files only, in `<tmp>/vc2/`, and edited only my own `txlib.py` there. No existing file was edited.
