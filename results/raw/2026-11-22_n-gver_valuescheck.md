# n — G-VER (n)'s entry and raws: the blind values-check, as returned, with every disposition

PI date 2026-11-22. Code (the n-build session).

**What was checked.** One blind pass by a subagent over three texts, at HEAD `2834c2d`:
- T1, this commit's entry, sha256 `e939f552…6bfc` (262 lines), with four placeholders not to be checked: the final
  sweep, the kinds the check adds, the checker's departures and its summary;
- T2, v1's launch review raw, `f0bb45a8…2130` (331 lines). Its head and §2 are Code's, §1 is the dispositions, and §3
  is the report;
- T3, the other fourteen staged raws, against their copy-back sources, among them v2's pod record with its one masked
  line.

**The checker's brief** was given to the checker as its prompt: Code's scratch file `S/step4b/gver/entry/vc_brief.md`
(`fe4998ba…21be`, 142 lines). It:
- named the texts and the sources:
  - in the repository, the files the texts cite, at `2834c2d`;
  - in Code's scratch, the copy-backs, the launch files and their tests at the sha256s of their two set indexes, the
    reviewed copies, the staging script and its two sources, and the abbreviation check;
  - in the notes folder, three notes;
- allowed `shasum` by name, and `jq` on the sweep record, on this session's transcript, on the staged record and on
  committed JSON outside `data/*/ckpt`, `data/*/reports` and `data/m[f]3`;
- set the transcript's use:
  - a sweep of Code's tool calls from the BUILD's last sweep to the brief's own hash, with Code's extraction of the
    span up to its last record (528 calls) beside it;
  - the coordinating session's and the PI's words checked in the transcript's cross-session messages;
- barred any other interpreter, any write and any network;
- barred any guard marker in an argv: a path, a grep pattern, a variable or glob that expands to one, a loop, and the
  command's own text;
- barred anything under `data/m[f]3` and any whole-tree git status;
- barred any read, listing, size or time of a ckpt or reports file, any `--stat` form over a commit that holds one,
  and anything in Code's scratch but the named files and the files the indexes list;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec and the campaign folder's
  exclusion on every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (168 lines, sha256
`2f9c6c7d…45af`). It names scratch files by their paths inside the scratch folder, the transcript as T and the notes
folder as N.

**Totals:** 86 items: 68 CONFIRMED, 12 IMPRECISE, 1 FAIL, 5 NOT CHECKABLE; and 11 observations. Code counted them
again by tool, by the verdict that follows each item's claim.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

Every FAIL and every IMPRECISE item is applied, in the checker's words or near them. Every observation is applied,
met or noted. §2 gives the edits and their check by tool.

- **Item 64 (FAIL), T1's departures list.** Applied: every kind the checker found missing is listed. They are:
  - the BUILD's commit window: its checks, its steps and its done report;
  - the battery window's three runs, in the window's form;
  - the manifest builder's run;
  - the process checks;
  - a `git diff --cached` without the pathspec, among the narrow pathspecs;
  - the ordinary reads and writes throughout the span, with the BUILD entry's "After it" list for the commands
    before its window.
- **Items 2, 25, 36 and 40, T1.** Applied in the checker's words:
  - N.1 "[as ruled]";
  - the refusal of anything of that name that exists;
  - the pod session's record, written on the laptop, copied last and counted there alone;
  - "renames the staging folder to".
- **Items 53, 55 and 57–61, T1's departures list.** Applied in the checker's words:
  - two `--stat` runs in one command, the figures from `7d01b02`'s list;
  - the battery window's three runs and `jq` among the interpreters;
  - two `git grep`s in one command;
  - one command with three unpruned finds, and the notes folder's `ls -la` whose glob matched nothing;
  - the non-ASCII byte count of v1's set note;
  - the notes folder's writes and reads, and the memory index's `tail`;
  - the removals, three times.
- **Item 73, T2:24.** Applied in the checker's words.
- **O1.** Applied: T1 names the diagnosis note, `3bd8ca91…fce0`, 139 lines.
- **O2.** Applied: T1 says v2's `manifest.txt` is not committed, being byte-equal to v1's manifest raw.
- **O3.** Applied: T1 cites G-CAL-n's out raw, lines 375–377, for its three files and no `.nfs…` name. Code read
  them by tool; G-TIME-n's out raw holds no such name either.
- **O4.** Met: the gate's declared count of the scratch folder's name is 2, the two pod records' mentions, with no
  root and no id.
- **O5.** Applied: the `Monitor` call and the file-tool read of the model manifest are listed, as "not shell
  commands".
- **O6.** Applied: the `ps -o etime=` of Q-F3's campaign process is in the process checks, for the seat to class.
- **O7.** Applied: "at once" cites N.2, and "untracked at the root" N.3, "as routed yesterday", the third sitting's
  item 4.
- **O8.** Applied in T2's head: the report's own hash abbreviations are kept as it wrote them, five-character tails
  among them.
- **O9.** Applied: T1 says this entry is not pushed, and that the BUILD, `2834c2d`, is on origin.
- **O10.** Noted: `copyback15.sh`'s `e3eb14bf…72fb` is the pod session's own abbreviation; its full sha256 is on no
  laptop file.
- **O11.** Noted: nothing staged or committed holds the host name's fragment that one of the coordinating session's
  messages holds.

**Beside the checker's items:** the entry's four placeholders. The checker's summary and its departures are written
in, and the kinds it added take their own bullets in place of their placeholder. Code's final sweep, of its commands
after the brief's hash, is written in last but one, and the edit count last, by tool.

## 2. The edits, checked by tool

The edits were made to new versioned copies of the two texts. Each was recovered from this session's transcript by
`jq` and replayed on the text the checker read, each change's old text found exactly once, by the replay script
`S/step4b/gver/entry/edits_check.sh`. The results are byte for byte the revised texts, so nothing else changed after
the check: the entry, 21 of 21 edits; the launch review raw, 2 of 2.

The entry's 21 include its placeholders, filled with this check's summary, the checker's departures, the kinds it
added and Code's final sweep. After the edits, one placeholder was filled by tool: the entry's count of these edits.

## 3. The report, as returned

```text
BLIND VALUES-CHECK: G-VER (n) entry draft (T1), v1 launch-review raw (T2) and staged raws (T3)

SETUP
- HEAD is 2834c2d, and it did not move while I worked. Every named file is at its stated sha256: T1 e939f552…6bfc (262 lines), T2 f0bb45a8…2130 (331), stage_raws.sh, lr_head_src.md, lr_tests_src.md, both set indexes (v1 has 28 rows, v2 has 21), check_abbrev.sh, sweep.jsonl (528 lines) and sweep_view.txt (219 lines).
- Each copy-back source matches the staging script's want value and the pod records' §8 lists.
- Each indexed file matches its row (sha256 and line count), checked by tool. The eight copies in G/launch/reviewed_v1/ match the brief's sha256s and line counts.
- Repository files cited are tracked and clean (rev-parse = hash-object): scripts/n_sessions.py (55885e65…385f), ids.py, cells.py, gcal.py, verify.py, m/resume.py, LOCK-n.md (88d9fe7b…e9d5), RESULTS.md, .gitignore (81f5f227…b610), CLAUDE.md, the seat raw (c66cb2f7…650b) and the PI routing raw.
- Every hash abbreviation in T1 and in T2's own text matches its file's full sha256. The one exception is copyback15.sh's e3eb14bf…72fb, which only ever appears abbreviated (in the pod record).

ITEMS
1. T1:1–5. Heading facts: PASS, 160 of 160; v1 a FAIL of the launch at its self-test, caused by an NFS silly-rename on the volume; the fix in v2 alone; the seat raw at 5ad19de; "Launch it". CONFIRMED. Evidence: v2 out 115 and 130; v1 out 79 and 106; git log of the seat raw → 5ad19de; T user record 2026-11-23T00:22:09Z.
2. T1:4. "the PI's routing, items N.1 and N.2 [go]". IMPRECISE: N.1 is "[as ruled]" and only N.2 is "[go]" (routing raw 17–28). Write instead: "the PI's routing, items N.1 [as ruled] and N.2 [go]".
3. T1:7. gver_v2.sh 07938072…3b56 ended "gver v2 PASS: …", exit 0, on pod emw1e4embiwe9b. CONFIRMED (v2 index; out 130; exit file "exit 0").
4. T1:8–9. The relay quote and "launch as announced", as the pod record quotes them. CONFIRMED (pod v2 record 6–8).
5. T1:10–13. The last line, verbatim (line 130). CONFIRMED.
6. T1:14. The stage's end line, last of its stdout (line 118). CONFIRMED (out 118 = the stage file's last line).
7. T1:15–17. Record sha256 d1dcc337…de90a, schema n-gver-v1, at lines 117 and 125, each present once. CONFIRMED (grep: exactly those two lines; jq .schema).
8. T1:18–20. verify's report, verbatim (line 115). CONFIRMED.
9. T1:21–24. Durations 14719 / 264 ms and the quoted phrase (line 116); 18041 ms (line 120); 78573 ms (line 129). CONFIRMED.
10. T1:25–27. "PASS is no STOP (N.2)"; the seat reads the entry, record and out raw first, then the draft, both before step 13's commit (§1.7). CONFIRMED (routing 27–28; seat §1.7).
11. T1:25. LOCK-n v1.0's draft follows at once, untracked at the root (N.3). NOT CHECKABLE (plan).
12. T1:28–29. data/n/gver/gver.json, admitted alone by .gitignore; the changed set is data/n/gver/ alone, nothing ignored (line 128). CONFIRMED (.gitignore 349–351; out 128).
13. T1:30–40. The record's fields: status, verify, manifest pin = sha256 and equal true, eight hashed_files, pins (lock, package, 12-file closure, driver, both identifiers, pod, weights), environment (8 versions), durations_ms. CONFIRMED. Evidence: jq of the staged record; hashed_files equal to out 106–113 by diff; imported_sha256 equal to out 82–93 by diff.
14. T1:42. Thirteen checks (line 126) and the figures (line 127). CONFIRMED.
15. T1:43–44. The §1.4 quote. CONFIRMED (seat raw line 28).
16. T1:45–50. v1: 34103c35…6f63, "launch cleared", same pod, its end line, exit 1, 106 lines; 726/728 (line 79); STAGE NOT STARTED (101); no record (104); 90824 ms (105); not of the INTEGRITY kind. CONFIRMED (v1 out; exit file; T 22:18:17Z; v1 pod record 18–21).
17. T1:51–55. The two failed checks, verbatim (lines 77–78). CONFIRMED.
18. T1:56–59. The diagnosis's route and the silly-rename description. CONFIRMED (N diagnosis §1; T 22:51:38Z, which reads the note at 3bd8ca91…fce0, 139 lines).
19. T1:60–63. v1's TMPDIR under the work folder on /workspace; the partial log gcal_turns.partial.jsonl (gcal.py:161); n_sessions.py lines 3284, 2982, 2983 and 3281. CONFIRMED (code at 2834c2d).
20. T1:64–65. ids.py:934 and ids.py:485 (shutil.rmtree, ignore_errors=True); five files in the staging folder. CONFIRMED: FILES_I_III has 3 and FILES_IV has 2 (ids.py:74–75), and MANIFEST.json is the sixth (476–478).
21. T1:66–68. G-CAL-n 581/581 and G-TIME-n 645/645, same self-test form, same box; 726+2 = 728. CONFIRMED: committed selftest raws; both out raws print "== 2 selftest, its temporary directory under the work folder" and pod emw1e4embiwe9b. The race reading itself is Code's.
22. T1:69–70. Driver and package unchanged; a fix to check 1 would move LOCK-n v0.1 §18's pin; check 2's path is G-CAL-n's production path. CONFIRMED (LOCK-n.md §18 at 776/781; the record's pins).
23. T1:71. 502 lines; 10 lines removed, 22 added, 11 of them code. CONFIRMED (my diff and count: 11 comment lines, 11 code lines; the delta file is that diff by cmp).
24. T1:72–73. LOCAL_TMP=/tmp resolved, and /tmp/gver-v2-selftest-work-gver-v2 (line 74). CONFIRMED.
25. T1:73–75. "it refuses a folder of that name that exists, a LOCAL_TMP that resolves under /workspace, and one that is not a folder". IMPRECISE: the script refuses anything at that name (test -e or -L, gver_v2.sh:163; note 58: "a folder, a file, or a symlink"). The "before the work folder is made" part holds (163 runs before the mkdir at 164). Write instead: "Before the work folder is made, it refuses anything of that name that exists (a folder, a file or a symlink, dangling or not), a LOCAL_TMP that resolves under /workspace, and a LOCAL_TMP that is not a folder."
26. T1:75–77. rmdir once empty; every other check, end and print is v1's; check_record's Python and bash function equal v1's by cmp, the Python at 2e697088…5c34; manifest 69fa4ec4…0fb6 and hashes a853932b…522b. CONFIRMED. Evidence: v1 227–303 vs v2 239–315 by cmp, sha 2e697088…; function 223–305 vs 235–317 by cmp; snippet/run_1.txt line 2.
27. T1:78–80. Note v2 86502c94…9225, 409 lines: the df -T step, 728/728 kept, the procedure as agreed, a fresh copy and new folders. CONFIRMED (note 123–163, 181, 299–310).
28. T1:81–84. Harness 709/709 (first run 708/709, the mkdir shim; the script unchanged); null mutant 709/709; 22 mutants, all killed; replay 130/130; no blind review of the delta. CONFIRMED. Evidence: run1/run2 and null outputs; lanes 6+6+5+5; the last script edit was 22:53:35Z and the harness was edited at 23:07:19Z, between the runs at 23:03:40Z and 23:07:26Z; T 22:51:38Z.
29. T1:85–88. Set note 266a8670…5e6c and index 7532f855…cca7; checked by tool and cleared; "Launch it" and the question, both quoted. CONFIRMED (shasum of N's v2 note; T 00:22:09Z).
30. T1:89–90. "  728/728 …" (line 77) in that folder; removed; no note line; test -e and -L exit 1 after the run. CONFIRMED (pod v2 record §6).
31. T1:92–98. Provenance: model, revision, aggregate, 22 files (100); driver and LOCK-n (101–102); ids (103); identifiers (104); package (105); hashes (81–93). CONFIRMED.
32. T1:99–103. Python and library versions; env.sh values; :4096:8 re-exported (line 2); git 2.43.0 (4); bash 5.2.21; overlay /tmp and nfs4 /workspace (§3). CONFIRMED (pod v2 record §2, §3, §5).
33. T1:104–109. Read whole (130, 214, 106 and 178 lines); each work file byte-equal to its out-raw lines; v2's manifest.txt equals v1's; v2's hashes.txt equals gver_hashes_v1.txt; gver.err is empty. CONFIRMED (cmp of every range).
34. T1:111–115. CUBLAS was :4096:8 before the script at both launches; two warnings before the count line, as at G-TIME-n and G-CAL-n; labels both 4. CONFIRMED. "No counter was declared" is Code's statement.
35. T1:116–127. The run: files at the relayed sha256s; no restart or replacement; no new sync (n-site14 at 2834c2d); GPU at 0 MiB; the df outputs; the fresh copy (clone flags, sparse form, clean three ways, pins); command 27e95ab3…6a4b under nohup; PID 15808, alive at +3 s, ended before +30 min. CONFIRMED (pod v2 record §1–§5).
36. T1:128–131. All nine files "each sha256 equal at the box, in staging and at the destination"; address and port "counted on every file copied back, on the box and again in staging". IMPRECISE: the pod session's record was written on the laptop, copied last, and "counted on the laptop alone, where it was written" (pod v2 record 166–167, 185). Write instead: "… the work folder's five and the record, each sha256 equal at the box, in staging and at the destination, and the pod session's record, written on the laptop and copied last, with no folder listed and nothing on the box removed. The address and port were counted on every file copied back, on the box and again in staging (the pod session's record on the laptop alone, where it was written): 0 each time."
37. T1:131–133. The coordinating session's shasum -c, and the names under the folder; Code's sha256 and cmp checks. CONFIRMED (T 00:46:52Z; Code's commands 00:47:41Z and 00:49:00Z).
38. T1:134–137. The box at the end; C.7. CONFIRMED (pod v2 record §9; routing 41).
39. T1:140–142. G-VER's record folder is not exposed at PASS or STOP; the cleanup's unlink at a failure; the changed-set check would show the entry. CONFIRMED. Evidence: n_sessions.py:5302–5324; resume.py:220–235 (tmp, then os.replace onto a name 5302 refuses if it exists); .gitignore 350 ignores any other name in data/n/gver/, which --ignored lists.
40. T1:143–146. "renames the staging folder into data/n/gcal/". IMPRECISE: the code is os.replace(stage, out_p) with out_p = data/n/gcal (n_sessions.py:2884–2887, 2983; GCAL_OUT 3262). The rest is confirmed: 2982, 2992–2993; the outputs are committed by name (git ls-files: gcal.json, dose_map.json, gcal_turns.jsonl); §1.6 names no G-CAL-n re-run. Write instead: "renames the staging folder to data/n/gcal/".
41. T1:147–149. A cell's JSON is rewritten on each append over the existing file (cells.py:248). CONFIRMED (code).
42. T1:149–151. G-TIME-n's launch checked its cells by name and digest and never listed a root; which checks would be exposed. NOT CHECKABLE (G-TIME-n's launch files are outside this check's read list; the NFS behaviour is Code's reading).
43. T1:152–153. The campaign's launch files. NOT CHECKABLE (recommendation).
44. T1:154–155. check_weights_folder lists exactly (n_sessions.py:694); a .nfs name would be refused, and the launch classes that INTEGRITY. CONFIRMED (694–697; gver_v2.sh:122).
45. T1:156–167. The three readings and their quote; "none fired"; F2's "a missing folder"; the coordinating session's call. CONFIRMED (gver_v2.sh 57–65, 119–130, 196–200; ids.py:314–315 gives the quoted text for b=iv; seat §1.4; T 22:18:17Z).
46. T1:168–175. The raws' names. CONFIRMED (stage_raws.sh 32–47, 65). The values-check raw's name is future.
47. T1:176–181. The mask on line 73, as <the volume server>; bfcacae9…9d57 → e1a343c6…7424; the quote "Commit them as they are or masked, your call". CONFIRMED (diff: 73c73, 2 lines; T 00:46:52Z).
48. T1:182–185. Link targets. CONFIRMED (names).
49. T1:187–196. The pod session's v2 §10. CONFIRMED.
50. T1:197–202. The pod session's v1 §10. CONFIRMED.
51. T1:203–204. "528 calls, 219 of them shell commands". CONFIRMED: jq over T in (19:26:47.885Z, 00:58:14.034Z] gives 528 tool_use items, 219 of them Bash; sweep.jsonl equals T's span item for item (time, tool, command length).
52. T1:207–211. Two marker greps. CONFIRMED (2026-11-22T19:39:45.563Z over ids.py; 19:56:11.577Z after the awk; the v1 set note says "None put a guard marker in an argv").
53. T1:212–215. "one git show --stat of two committed run entries". IMPRECISE: these were two git show --stat runs in one command (2026-11-23T00:48:05.766Z). The output, viewed masked, shows one ckpt byte size and one report line count, both from 7d01b02. Write instead: "two git show --stat runs in one command, of two committed run entries (7d01b02 and db00d6d), … printed (from 7d01b02's list) the byte size …".
54. T1:216–219. The cd glob, not in a subshell, then the cd back; the harness's form. CONFIRMED (19:45:34.505Z and 19:45:41.954Z; departures.md item 1; v2 set note 112–113).
55. T1:220–222. "an interpreter other than shasum: the awk above … and one awk …". IMPRECISE: this omits the battery window's three runs (Python, at 22:09:18.749Z and 22:09:43.548Z directly, and at 22:10:15.385Z through the snippet script) and jq over Code's sweep files in scratch. Write instead: "an interpreter other than shasum: the battery window's three runs, on the coordinating session's grant (Python, twice directly and once through the snippet test's script); jq over Code's sweep files in scratch and over the two transcripts (below); the awk above … and one awk …; and one environment assignment …".
56. T1:223–224. The pgrep with Q-F3's script name, before the window request, matching 8051 alone. CONFIRMED (22:06:07.131Z; masked output shows 8051 only; the request was written at 22:07:12Z).
57. T1:225. "one git grep over valence_core/n and two named files". IMPRECISE: one command (22:47:45.509Z) held two such git greps. Write instead: "two git greps in one command, over valence_core/n with resume.py and the driver, and over valence_core/n with resume.py, in place of item 3's form;".
58. T1:226–232. Finds and listings. IMPRECISE: the "one unpruned find ." was three unpruned finds in one command (00:47:41.414Z). Also missing: an ls -la in N with a trailing glob that matched nothing, so zsh did not run it (23:20:32.613Z). The rest is confirmed: the pruned find at 00:49:33Z; scratch ls -la at 19:48:38, 19:51:26, 22:56:37, 23:03:49, 23:08:21, 23:20:38, 00:49:20, 00:51:24 and 00:52:37; N at 23:10:02Z; T at 00:57:57Z; the subagents' folder counted at 20:55:54Z; /tmp at 23:18:30Z; the root test at 23:18:35Z. Write instead: "… one command with three unpruned finds over the v2 copy-back folder …; and in the notes folder, one ls -la of the v2 set note's name with a trailing glob that matched nothing, so that zsh did not run it;".
59. T1:233–234. Byte counts. IMPRECISE: also a non-ASCII byte count (tr into wc -c) of v1's set note in N (22:15:16.398Z). Add: "and the non-ASCII bytes of v1's set note in the notes folder".
60. T1:235–240. Shell reads and writes outside the repository and scratch. IMPRECISE. It omits:
    - a tail -n 2 of the memory index after the append (20:18:25.856Z);
    - the shell writes into N: the window request (22:07:12.909Z) and v1's set note (22:15:16.398Z) by redirect, and v2's set note by fill_v2.sh, which writes its .tmp in N, rm's it on failure (fill_v2.sh 54–58; two failed runs at 23:20:13Z and 23:20:44Z) and renames it into place (23:20:54Z, 23:21:27Z);
    - reads in N by /usr/bin/grep -c, sed -n, tr and cmp (22:07:12Z, 22:15:16Z), and existence tests (23:20:38Z).
    Write instead: "… one shell append to the memory index by printf >>, with a tail -n 2 of it; the notes folder: the window request and v1's set note written there by redirect, and v2's set note by the fill tool (its temporary written, removed on its two failed runs, renamed into place on the next two); reads there by cat, shasum, wc -l, /usr/bin/grep -c, sed -n, tr and cmp; existence tests; a name-only ls; and one rm of the v2 set note's first output, unsent, before its regeneration; …".
61. T1:241–242. "the note and the index of two failed fills". IMPRECISE: they were removed three times (23:20:44Z and 23:20:54Z after the failed fills, and 23:21:27Z after the good third fill, together with N's set note; regenerated byte-identical). Write instead: "the v2 note and index, three times (after the two failed fills, and once more with the set note after the third, regenerated byte-identical), and the first staging of these raws (00:55:54Z), each regenerated after;".
62. T1:243–245. Throwaway repositories: the harness's fake copies; the overlay by git archive into tar. CONFIRMED (20:24:16Z; the recipe's lines 17–21 as printed in T's tool result at 01:00:40Z).
63. T1:246. Tool checks. CONFIRMED (19:53:10.088Z).
64. T1:203–247. The list as complete ("Code knows of no others"; every kind outside item 1). FAIL. Uncovered, by time:
    (a) 2834c2d's commit window:
        - pre-window checks at 19:32:59.239Z (git show HEAD:RESULTS.md into wc -l and cmp, sed -n of RESULTS.md, git rev-parse origin/main);
        - kit place v4 at 19:34:35Z, git add --pathspec-from-file at 19:34:41Z, gate v11 at 19:34:49Z, the message check at 19:34:56Z, git commit at 19:35:02Z, verify v3 at 19:35:11Z;
        - the done report at 19:35:23.248Z: git show HEAD:<path> into shasum and wc -l for seven paths; git diff -U0 and git diff --numstat of RESULTS.md; the package-digest script; git cat-file commit HEAD into cmp; git diff --name-only with the pathspecs; git rev-parse origin/main; pgrep -i python.
    (b) The battery window's three runs (22:09:18.749Z, 22:09:43.548Z, 22:10:15.385Z): ( cd <repo> && cd jl*/.venv/bin && … nice -n 19 ./python -I -B … ). This is a glob at the repository root that zsh's builtin cd expanded to the marker-named venv folder, which holds 2 marker words, inside a subshell; no process argv held it.
    (c) The manifest builder's run, bash make_manifest_gver_v1.sh (19:56:21.346Z). Inside it:
        - the model's data folder is entered by a cd glob in a command substitution, and by a variable holding its name in subshells (builtins);
        - git ls-tree -r runs over the adapters folder and BK's skeletons, and the marker-holding names it prints are read by redirects in a while loop.
    (d) Process checks:
        - pgrep -i python at 19:31:10Z and 19:35:23Z;
        - pgrep -x python3, and ps -p 8051 -o pid= -o etime=, at 22:06:07Z (it printed the elapsed time of Q-F3's campaign process);
        - ps -p 8051 with pgrep -f n_sessions at 22:09:13Z, 22:09:31Z, 22:09:55Z and 22:11:21Z;
        - pgrep -f of the harness and mutation tool at 23:09:36Z, 23:18:51Z and 23:19:05Z (the last in a background wait loop).
    (e) git diff --cached --name-only without item 3's pathspec, into wc -l (22:06:07Z).
    (f) Ordinary reads and writes in the repository and scratch, throughout the span: sed -n, /usr/bin/grep, cat, cmp, diff and git diff --no-index, git show <rev>:<path>, jq over scratch sweep files, mkdir/cp/mv and redirects, bash of Code's scratch scripts (harness, mutation tool, staging, fill, index, abbreviation check, edits replay, package digest), zsh of the commit build script, date, od -c, xargs. The BUILD's entry listed kinds like these. The span 19:27:25Z–19:32:05Z is covered by that entry's "After it" list (RESULTS.md:333–335).
    Add these as bullets in T1's list: (a)–(d) as their own items, (e) under narrow pathspecs, and (f) as one "throughout" bullet in the BUILD entry's form (RESULTS.md:262–265).
65. T1:248–251. The launch reviewer's departures. CONFIRMED (report DEPARTURES; T2 §1's last part).
66. T1:254–255. Gate v12 and the commit-time count. NOT CHECKABLE (plan).
67. T1:255–256. Nothing ran on a model, and no Python after the window's three runs. CONFIRMED through 2026-11-23T01:07:00.290Z: no python in any command after 22:10:15Z, and the grant describes the runs as model-free.
68. T1:256–257. The push needs the PI's word; "D.8's range ended at the BUILD". CONFIRMED for the reading (routing 44; T 00:22:09Z; origin/main is 2834c2d). The push itself is a plan.
69. T1:258–261. Next. NOT CHECKABLE (plan). The citations are consistent: N.3, §1.5, §1.7, D_n 2026-12-15 (§1.3).
70. T2:1–3. Title, PI date, Code. CONFIRMED.
71. T2:5–20. The reviewed files' sha256s, line counts and notes. CONFIRMED. Evidence:
    - reviewed_v1/ hashed and counted (cb17ca22 449, 3cc8b74f 280, 8a486f21 303, 28e7eb9a 230, ff83a872 260, 0706ae6e 163, cda637b4 147, 21bcfe98 54);
    - brief 9–32;
    - the builder's own comment ("G-TIME-n's builder … unchanged but for this comment and its name").
72. T2:22. Kept in scratch. CONFIRMED: the eight in reviewed_v1/; the manifest and builder at the index; harness_run1 and dry_1 at the brief's sha256s per Code's 00:53:19Z output. G-TIME-n's files were not checked.
73. T2:24–36. The brief "named those files by sha256, to be verified and read in full". IMPRECISE: the brief says "Verify each sha256 before you read it", asks for the box script whole, and G-TIME-n's files "read where they help" (brief 8–10, 30). The rest is confirmed (brief items 1–6 and the rules). Write instead: "named those files by sha256, each to be verified before it was read (the box script whole, G-TIME-n's files where they help), and the code they must match at 2834c2d:".
74. T2:38–39. 30 refusals stated; 27 made (O6); 28 since O2. CONFIRMED (brief 38; report O6; dispositions 7–8; gen_run1 32 cases).
75. T2:41–42. Report by jq from the hand-back, 171 lines, 0ab03938…6107, naming scratch files as S/ only. CONFIRMED (20:55:54Z; shasum; 0 local roots).
76. T2:44. Totals. CONFIRMED (report).
77. T2:47–137. §1 equals the dispositions (fe32ad76…e781, 95 lines) from line 10 on, headings one level down. CONFIRMED: cmp; spot checks of every case and mutant name in the harness and mutation tool; .gitignore 349 and 351; G-TIME-n's run-of-record block is 52 lines (out raw 161–212).
78. T2:141. 34103c35…6f63, 490 lines, ASCII. CONFIRMED (0 non-ASCII bytes).
79. T2:142–146. Harness 677/677 (da871f03…c91a); null mutant 677/677 (mut3_d; the first pass's null was 649, as §1 says); 141 mutants, 129 killed and 12 surviving; the 11 killed on re-run; G39; 140 listed. CONFIRMED.
80. T2:147–150. hashes: 13 lines, a853932b…522b, byte for byte equal to results/raw/2026-11-21_n-gtime-v1_hashes.txt; generator 32/32, exit 0, empty stderr; snippet test 90/90 and 54/54. CONFIRMED (cmp; gen_run1; run_1; T 22:11:59Z).
81. T2:151–152. Replay 128/128; 1 PASS, 2 STOP, 10 INTEGRITY, 19 FAIL. CONFIRMED (counts by rc).
82. T2:154–157. Set note eee0e3de…5ed4 and index 64407bfa…f3cc; the FAIL at 726/728; v2's change; no review. CONFIRMED.
83. T2:159–331. §3 is the report, byte for byte. CONFIRMED (tail -n 171 into shasum = 0ab03938…6107; cmp).
84. T3. The 13 raws (v2 out, exit, selftest, hashes, stage, run-err; v1 out, exit, selftest, manifest, hashes, run; gver.json) are byte-equal to their sources. CONFIRMED (cmp; each source at its sha256).
85. T3. v2's run differs from its source in line 73 alone: diff "73c73", 2 changed lines, 214 lines each, the line starting "<the volume server>:/runpodfs/networkvolumes/", sha256 e1a343c6…7424. CONFIRMED.
86. T3 and T1 screen, counts only. All 15 staged raws and T1 hold 0 local roots, 0 of the user's name, 0 session ids, 0 agent ids, 0 IPv4-like strings and 0 ssh, port or root@ forms. The host name appears 0 times outside the source's line 73 (pattern validated: 1 match in the source, 0 in the staged run). CONFIRMED.

TOTALS: 86 items. 68 CONFIRMED, 12 IMPRECISE, 1 FAIL, 5 NOT CHECKABLE.

THE SWEEP
- Span: (2026-11-22T19:26:47.885Z, 2026-11-23T01:07:00.290Z], where the closing command is the one that hashes G/entry/vc_brief.md. That is 237 Bash commands: 219 up to Code's extraction and 18 after it.
- Guard markers in a command's text: [2], both declared (19:39:45.563Z and 19:56:11.577Z).
- The campaign folder's plain name: [1], declared (22:06:07.131Z).
- Globs or variables that passed a marker-named path to a command, all to the builtin cd (no process argv):
  - 19:45:34.505Z, declared;
  - 22:09:18.749Z, 22:09:43.548Z and 22:10:15.385Z, undeclared (item 64b);
  - inside the builder at 19:56:21.346Z, undeclared (item 64c);
  - the harness and mutants, declared.
- No loop passed a marker-named path to a process argv.
- The commands after the extraction (jq over sweep.jsonl, sed and grep in scratch, the abbreviation script, the entry edits, the brief's hash) hold no departure kind beyond those already listed. The awk_free=1 assignment at 00:59:46Z is among them and is declared.

OBSERVATIONS
1. T1 never names the diagnosis note or its sha256 (3bd8ca91…fce0, 139 lines), although the coordinating session read and cleared it by that hash (T 22:51:38Z). My brief says each note's sha256 is in T1, T2 or the v2 index; this one is in none. Add it to T1:56.
2. v2's manifest.txt is not committed. Say so in "The raws" (it is byte-equal to v1's manifest raw).
3. "Its run of record held" (T1:145) could cite results/raw/2026-11-20_n-gcal-v1_out.txt 375–377: exactly three files and no .nfs name. The G-TIME-n out raw holds no .nfs name either.
4. Each pod record holds one "n-build's scratchpad/step4b/gver/launch/" fragment (no root, no id). The commit's leak screen should expect 2.
5. Not shell commands, but the BUILD's entry listed this kind: a Monitor call on the v2 mutation lanes' scratch outputs (23:17:43Z), and a file-tool read of the model manifest (19:45:20Z).
6. ps -o etime= at 22:06:07Z printed the elapsed time of Q-F3's campaign process. The letter of items 2 and 5 does not bar it, but the seat may want it classed.
7. For "untracked at the root", T1:25 cites N.3. "At once" is N.2's wording; "untracked at the root" comes from the third sitting's item 4, which N.3 carries ("as routed yesterday").
8. The report's O4 and O5 use 5-character hash tails (…a522b, …47ac9). These are the reviewer's own forms, kept verbatim; a line in T2's head could say so.
9. "Not pushed" (T1:257) refers to this entry. The BUILD itself is on origin (origin/main = 2834c2d, pushed per T 19:37:06Z), which the entry could state.
10. check_abbrev.sh accepts an abbreviation "as written in a reference" (line 24). copyback15.sh's e3eb14bf…72fb passes only that way, because its full sha256 is on no laptop file.
11. A coordinating-session message in T holds the opening fragment of the volume server's host name. Nothing staged holds it.

DEPARTURES
- One command's text held the environment assignment awk_free=1 before sed. No awk ran.
- sed was used as a filter and for masking, alongside cut, tr, od, diff, cmp, sort and uniq. sed is a script language outside the two named exceptions; declared for classing.
- One git check-ignore -v --no-index on three named paths under data/n/gver/ (two of them not files). This is a git form outside item 1; it printed only .gitignore line numbers, patterns and the names.
- Git forms without item 3's pathspec:
  - git log -3 --format of ids, commit times and subjects, with no path;
  - git log --format=%h -1 over one named data path;
  - git log --format over two named raws;
  - git rev-parse origin/main.
- More of T printed than a finding needed, in tool output only:
  - the coordinating session's messages after the BUILD's sweep, in full; one held the host-name fragment (not repeated here);
  - truncated, masked views of all 237 swept commands.
- Masked tool-result lines (digits as N) named one ckpt file and one report path, from the --stat output.
- wc -c of derived streams: non-ASCII counts of scratch files and the length of the masked host pattern. None under ckpt or reports.
- Otherwise none:
  - no Python, no write, no network;
  - no guard marker in any argv or command text;
  - nothing under data/*/ckpt, data/*/reports or data/m[f]3 read, listed or sized;
  - no whole-tree git status;
  - no listing, find or glob in S;
  - in N, only the three named notes read.
```
