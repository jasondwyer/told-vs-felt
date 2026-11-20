# The coordinating session's notes on the seat's second sitting of 2026-11-20: the blind values-check, as returned, with every disposition

PI date 2026-11-20. Code (the coordinating session).

**What was checked.** One blind pass by a subagent over four drafts:
- A, the entry (`RESULTS.md`, the Log's head), sha256 `b8970eae…6ed1`, 132 lines;
- B1–B4, the four close lines, on the entries of `411b15c` (`911a201a…8dac`), `1641948` (`8f05803a…acf5`), `b6ea27f` (`de81061c…a50d`) and `bc85386` (`cfda7574…ad5f`);
- C, the routing raw `2026-11-20_second-sitting_pi-routing.md`, whole, `5e721902…6dfc`;
- P, their placement, in the draft of the new `RESULTS.md`, `264882ab…6c8d`.

**The checker's brief** (given inline in the coordinating session's Agent call; extracted afterwards from its own transcript by `jq`, `05706edd…35bf`, 74 lines, 9,387 bytes, the list of record's five items in it verbatim by `grep -x -F`; a first extraction, with a time bound that missed the call, wrote an empty file):
- named the sources, among them the coordinating session's transcript and two sweeps of its shell commands (62 and 108 commands), n-build's notes and scratch, and the first sitting's push record;
- quoted the list of record v2's items 1–5 verbatim, from `2026-11-10_list-of-record-v2_design-to-code_answers.md`, lines 18–22;
- carried the briefs' two lines, on item 3's pathspec in a check and on globs;
- barred any interpreter but `shasum`, any write, any network, `pgrep` and `ps`, anything under `data/*/ckpt` or `data/*/reports`, and the guard markers and the campaign folder's plain name in any argv.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (213 lines, sha256 `22e146c5…2313`). It held no local path. Its "W/", "T", "N/", "NB/" and "S/" are the coordinating session's scratch folder, its transcript, the shared notes folder, n-build's scratch folder and the coordinating session's scratch root.

**Totals:** 80 items (61 CONFIRMED, 10 IMPRECISE, 7 FAIL, 2 NOT CHECKABLE) and 9 observations.

## 1. Dispositions

- **Item 10** (IMPRECISE): applied; the entry quotes edit 3 from its capital: "The coordinating session's routing of the draft is committed as a raw in the lock's commit".
- **Item 21** (IMPRECISE): applied: "read the request note, the entry, the message, the pre-check and the kit's new `kit_place_v2.sh` whole and the manifest's seven lines (one printed cut short, at 220 characters)".
- **Item 30** (IMPRECISE): applied: the elision is "[…]", and the bullet says that the sentences in §5 and §21 that say the seat has not ruled stay as the lock had them, declared in `deabf3f`'s entry.
- **Item 36** (IMPRECISE): applied: "each through `sed '1,/^$/d'` and compared by `cmp`, the first three also counted for non-ASCII bytes (`deabf3f`'s count was taken on its message file before the commit)".
- **Item 37** (FAIL): fixed; the two forms are added: `git diff -U0` of each verified commit against its parent on `RESULTS.md`, three in each of four verifications, and `git show --format= -U0` of `bc85386` on `RESULTS.md`, twice.
- **Item 38** (FAIL): fixed; the counts are taken from the last sweep, `added.txt`'s two `git ls-files` and its `git diff --cached --name-only` among them: seven commands and four.
- **Item 40** (FAIL): fixed; "No guard marker reached an argv" is replaced by the declaration, first in the list: two `grep` processes over a glob of the memory folder (`-- *.md`) carried the names of four marker-named memory files. The coordinating session confirmed by tool that 4 of its 98 memory files' names carry a marker word, and that the Q-F3 campaign's process (PID 8051) was still running.
- **Item 42** (IMPRECISE): applied: the brief's two extractions are added to the `jq` line, with the stopped task's `wc -c` and `wc -l` beside its `cat -v`.
- **Item 43** (IMPRECISE): applied: "one `jq` of selected fields of `data/n/gates/G-ANL-n.json`, one `wc -c` of it and one `cmp -s` against n-analyzer's copy".
- **Item 45** (FAIL): fixed; the zsh error is added: a glob with no match in a name-only `ls -d`, so that `ls` did not run.
- **Item 46** (IMPRECISE): applied: "two `grep` processes over a glob of n-analyzer's mutant outputs, and two over a glob of its memory folder".
- **Item 48** (IMPRECISE): applied: the forms `od`, `fold`, `head`, `tail` (once `tail -c 1500` of a memory file), `git show <rev>:<path>`, `git cat-file blob` and the build script's zsh runs are added, and the objects its memory files and scratch outputs.
- **Item 49** (IMPRECISE): applied: "rerun with it, one name still missing in that folder".
- **Item 54** (FAIL): fixed; a line for byte and line counts is added, its counts from the last sweep: `wc -c` of files in 13 commands and of piped bytes in eight more, and `wc -l` in 49.
- **Item 55** (FAIL): fixed; the recursive grep is added, with the pruned find that followed it.
- **Item 61** (IMPRECISE): applied in B1: "the twelve files at §18's sha256s".
- **Item 78** (FAIL): fixed; the entry now quotes items 2 and 3 whole, in a bullet that also records G-TIME-n's state: n-build found its stage command not yet built (the driver's line 182, read by tool), and its PINs GT1–GT17 were put to the PI. C's head stands as written.
- **The NOT CHECKABLE items** (34 and 56) stand: the last sweep and the commit's own facts come after the check. The last sweep holds 134 commands; the checker's 128 are its first.
- **The observations:**
  - 1, applied: "`S` being n-build's scratch folder, as the raw writes it";
  - 2, applied: the bullet's head is "The first sitting's push (its item 7)";
  - 3, applied: "it is in no committed text but this account of it";
  - 4, applied: the line on `added.txt` adds the command's failed reads and its false "added = …" line;
  - 5, met: this raw cites the brief from its second extraction;
  - 6, applied: a bullet records the verifications and screens of `b6ea27f`, `1641948` and `411b15c`;
  - 7, applied: "1,649 added lines (messages included)";
  - 8, met: the counts are filled from the last sweep (134 commands; `jq` over the transcript in nine, `pgrep` in 14);
  - 9, applied: a line lists the calls beside the shell.

## 2. Edits after the check

- The dispositions above, and the counts from the last sweep of the coordinating session's own shell commands, with one class it found after the check: two `jq` over the values-checker's task output, for this report.
- The entry's values-check bullet and the values-checker's departures, from §3.
- The edits were checked by tool against the dispositions above; no second full pass was made.

## 3. The report as returned

```text
VALUES-CHECK: the coordinating session's notes on the seat's second sitting of 2026-11-20 (A, the entry; B1–B4, the close lines; C, the routing raw; P, the placement)

Counts: 80 items. 61 CONFIRMED, 10 IMPRECISE, 7 FAIL, 2 NOT CHECKABLE. 9 observations.

Texts checked, by sha256 (shasum, abbreviated with cut). Each equals its copy in W/checked/:
- A b8970eae…6ed1 (132 lines)
- B1 911a201a…8dac (19), B2 8f05803a…acf5 (11), B3 de81061c…a50d (15), B4 cfda7574…ad5f (8)
- C 5e721902…6dfc (27)
- P 264882ab…6c8d (34,241)
HEAD is deabf3f. Its RESULTS.md has 34,056 lines.

Short names:
- raw:N is line N of <repo>/results/raw/2026-11-20_n-lock-v0_1-read_design-to-code_answers.md at HEAD.
- paste:N is line N of W/pi-routing-received.txt.
- R:N is line N of RESULTS.md at HEAD. L:N is line N of LOCK-n.md at HEAD.
- s2:N is line N of W/sweep2_cmds.txt. I checked that file against T: it is T's first 108 Bash commands since bc85386's commit, byte for byte.
- pN is T's Nth Bash command after sweep2. p1–p16 came before this check started; p17–p20 ran during it.
- I give no clock times. Transcript events are cited by these indices.

ITEMS

A, the entry
1. A:1–3, the heading (the lock's read in deabf3f; four close lines, item 5; the push to come, item 6). CONFIRMED. deabf3f's name-status adds the raw; paste:16 and paste:19.
2. A:5–6, the raw's path, 794ee42f…f084, 15,217 bytes. CONFIRMED. HEAD blob by shasum; wc -c gives 15217; paste:5.
3. A:6–7, the raw reads LOCK-n.md and the entries of 411b15c, 1641948, b6ea27f and bc85386. CONFIRMED. raw:3.
4. A:7–8, "The PI placed it untracked, and the coordinating session re-hashed it equal to the paste block first." CONFIRMED. paste:3. s2:141 printed 794ee42f…f084 with "??" status. It ran after the PI's routing message and before the Write of the saved copy and the three relays.
5. A:8–9, deabf3f carries it by path; "commit by path on my routing, in the lock's commit". CONFIRMED. paste:3, exact; deabf3f's name-status.
6. A:9–12, "Route as given"; the block's raw; "item N" and "§N"; §8 words the items differently. CONFIRMED. paste:21. Compare raw:69–81 with paste:7–19 (for example raw:75 against paste:13).
7. A:13–14, items 1–4 relayed verbatim (1–3 with item 5 and its two parts to n-build; 2 and 3 to the pod session; 4 with item 5 to n-analyzer). CONFIRMED. In T's three relay messages, every relayed line equals its paste line by grep -x -F: 5 of 5, 3 of 3 and 3 of 3. The n-build message names "Two of its parts".
8. A:15–16, "the BUILD's flags as §4 rules them", "One sentence in §10's G-VER row." and "the G-VER sentence into §10". CONFIRMED. paste:16; raw:41; raw:78.
9. A:16–18, n-build told that this is a change beside §2's seven, in the raw's words, with nothing ruled; n-build read §4 the same way; the sentence is in the G-VER row at deabf3f. CONFIRMED.
   - The relay says: "That sentence is a change to the lock beside §2's seven. These are the raw's words; the coordinating session rules nothing."
   - N/…_riders-window.md §2; L:543.
10. A:19–21, edit 3 names "the coordinating session's routing of the draft"; the copy is 9fc5cd6d…b7d0, 16 lines, "byte for byte as saved"; lines 1 and 16 are the wrapper, and line 1 names the sender by id. IMPRECISE.
   - raw:20 reads "The coordinating session's routing…", with a capital T; the quotation changes the case.
   - The rest holds. NB/step4b/lock/routing_lock.txt hashes to 9fc5cd6d…b7d0 and has 16 lines. Its line 1 is a cross-session-message tag with from="local_<id>"; line 16 is the closing tag.
11. A:21–24, the answer: lines 2–15 byte for byte, no session id (checked by tool), committed as …_routing.txt at deabf3f with the drop declared. CONFIRMED.
   - s2:198 found 0 id shapes in lines 2–15; the riders' grant message gives the answer.
   - The committed _routing.txt equals lines 2–15 by cmp; L:6–9 declares the drop.
12. A:24–25, the first sitting's copy was committed at bc85386. CONFIRMED. bc85386 adds results/raw/2026-11-20_first-sitting_pi-routing.md.
13. A:26–30, n-build's defaults, with no objection: the square brackets; three sentences (§5, §21, §24) left and declared in deabf3f's entry on the ground given; the note on "the rest as the lock has them" (§0, item 5); a Draft 10 note; the shell re-check. CONFIRMED.
   - N/…_riders-window.md §4 and …_commit-window.md §2; the two grant messages.
   - R:74–81; L:430, L:870, L:995 (the three sentences), L:660 (the brackets), L:90–103 (the note); raw:9; paste:16.
14. A:31–32, the box: this morning's ruling restated; up and idle; nothing runs on it before G-TIME-n's files are relayed. CONFIRMED. The pod relay says "Item 3 restates this morning's ruling. The box stays up and idle." and "Nothing runs on the box before that relay."
15. A:33–35, the riders' window granted at HEAD 411b15c; the note and the three scripts and two data files read whole; the seven files at their sha256s; only 8051 running; five calls, model-free. CONFIRMED.
   - Read calls of the note, precheck.sh, fidsample.py, aftercheck.sh, hashes_expected.txt and sums.txt, with no offset or limit.
   - s2:188: shasum -c, 7 OK. s2:200: "8051 python3.12" and HEAD 411b15c.
   - The grant message, and the note's five calls.
16. A:37, the six run files at the reported sha256s, both exits 0, both stderr files empty. CONFIRMED. s2:207's output.
17. A:38, rider 1's 13 lines byte for byte §18's claim (06b55761…1d39 and twelve files); Q1, no STOP. CONFIRMED. s2:207's cmp says yes. Here, HEAD's _hashes_out.txt equals draft 9's §18 hole-14 line and table, and L's table, by tool.
18. A:39–40, rider 2: 15 of 160 (6 floor, 9 neutral), the cell rule, ascending runs, digest 3c70f5ff…a81d re-derived by shell. CONFIRMED.
   - s2:207: "my digest" equals "printed", "all 15 ok", "6 9".
   - I re-derived the same here from HEAD's _fidsample_out.txt. The rule matches schema.py:583.
19. A:41–42, the tree after the window. CONFIRMED. s2:209's output.
20. A:44–46, the two forms named for n-build's entry, with the session's own pruned find. CONFIRMED. The grant message's "Forms to declare"; s2:196 printed 0; NB/…/r10/aftercheck.sh:46 and precheck.sh:13 and :16.
21. A:47–48, the commit window granted after reading "the request note, the manifest, the entry, the message, the pre-check and … kit_place_v2.sh whole". IMPRECISE.
   - The manifest was printed through cut -c1-220 (s2:218). Its line 2 is 235 characters as printed, so the last 15 characters of its untr= hash were cut.
   - The other five were read whole with the Read tool.
22. A:48–52, the checks before the grant: sources at their sha256s; outputs, routing raw and embedded scripts and outputs by cmp; draft 10 against draft 9 in 15 hunks; no home prefix, user name, temp path or session id. CONFIRMED.
   - s2:218, :220, :242, :226, :230.
   - I re-derived the 15 hunks: status line; header; the Draft 10 note (2 hunks); Conventions; §3; §5 (2); §10; §13; §18; §22; §23; Sources (2).
23. A:53–54, parent 411b15c; the eight paths; the seven non-RESULTS paths at the manifest's sha256s. CONFIRMED. git log %P; name-status; shasum here against NB/…/commit10/manifest.txt.
24. A:55, the message equals its source; its one non-ASCII character is the em dash of the PI's name. CONFIRMED. cmp-equal to commit10/commit_msg.txt; 3 non-ASCII bytes; "LOCK-n v0.1 — COMMITTED" (paste:8).
25. A:56, RESULTS.md's one hunk, +102 −0, equal to the entry. CONFIRMED. diff gives 23a24,125: 102 lines added, 0 removed, equal to commit10/entry_v1.md.
26. A:57–58, LOCK-n.md 88d9fe7b…e9d5, 1058 lines, clean; the package digest by shell 06b55761…1d39; the home count 0. CONFIRMED.
   - Here: shasum, wc -l, and rev-parse equal to hash-object.
   - s2:255's output gives the digest and the count. deabf3f touches nothing under valence_core/.
27. A:60–61, the screen of 411b15c..deabf3f: 1 commit, 8 file-diffs, 1,649 lines, every class CLEAR, no leaks, gl5 0. CONFIRMED. s2:257's output (see observation 7).
28. A:62–65, the raw in deabf3f; the close lines committed here, one on each entry. CONFIRMED. deabf3f; P (item 80).
29. A:66–67, "the departures of §7 and both parallel starts inert"; "Inert, every one; the standing lines stand"; "inert" and "likewise inert". CONFIRMED. paste:16; raw:63; raw:51.
30. A:68, "the BUILD's flags as §4 rules them (…)": in the lock at deabf3f, with §4's sentence in the G-VER row. IMPRECISE.
   - The lock carries §4's sentence (L:543) and names the raw (L:984).
   - But L:430 (§5) and L:870 (§21) still say the seat has not ruled. Those sentences were left and declared (A:27–28).
   - The elision is written "(…)", not "[…]".
31. A:69–71, the first sitting's push. CONFIRMED. With the bullet's head and backticks dropped, it equals the C.5 line, S/push13/push_record13.txt:22. git log bc50244..bc85386 lists 6 commits. The push's output is in T, and the first sitting's item 7 ends "[push]".
32. A:72–75, "Keep them" after the first sitting's routing; items 4, 8, 23 and 28; the cleanup complete at 26; the refs stay off; relayed to the pod session. CONFIRMED.
   - The PI's "Keep them" came after bc85386's commit and the push.
   - The relay names the four items, "complete at v1's 26" and the refs; R:776.
   - I did not read the pod session's list itself.
33. A:76–78, item 6, "behind the amended screen, after step 10's commit"; the range holds b6ea27f, 1641948, 411b15c, deabf3f and this commit. CONFIRMED. paste:19; git log bc85386..HEAD. The window and the next entry's C.5 line are plans.
34. A:80–81, two sweeps, "the second made after the values-check (SWEEP_COUNT)"; "knows of no others". NOT CHECKABLE: the final sweep is still to come. Today's W/sweep2_cmds.txt was made at s2:272, before this check. Items 37, 38, 40, 45, 54 and 55 list what the list misses as of p20.
35. A:82–85, (a) four pruned finds. CONFIRMED.
   - s2:100 was moved to the background at the time limit and stopped with TaskStop; its output reads "[killed]" (s2:184).
   - The others are s2:108, :196 and :209. There is no other find.
36. A:86–88, (b) git cat-file commit of four commits, "each … compared by cmp and counted for non-ASCII bytes", and the 300-commit loop. IMPRECISE.
   - For deabf3f (s2:255) the stored message was compared by cmp only. Its count (3) was taken on commit_msg.txt before the commit (s2:220).
   - The loop read 300 messages, 19 with non-ASCII bytes (s2:224).
37. A:89–93, (c) git commands in checks without item 3's pathspec. FAIL: the list leaves out two forms.
   - git diff -U0 <c>^ <c> -- RESULTS.md, three times in each verification: b6ea27f (s2:57), 1641948 (s2:89), 411b15c (s2:129) and deabf3f (s2:255). Twelve in all.
   - git show --format= -U0 bc85386 -- RESULTS.md (s2:154, s2:156).
   - The counts the list does give hold up to sweep2.
38. A:90–92, (c) "git ls-files -- naming one file, twice" and "git diff --cached --name-only counts in six commands". FAIL.
   - The check's preparation added git ls-files -- added.txt (p3, p4) and git diff --cached --name-only -- added.txt (p3).
   - That makes four ls-files calls and seven --cached commands without item 3's pathspec.
39. A:94–95, (d) the m-f-3 string in the argv of six grep processes, from adjacent quoted strings. CONFIRMED. s2:232: five in the loop and one on 411b15c's entry. No command text holds the plain string except a heredoc to memory (s2:246).
40. A:95–96, (d) "No guard marker reached an argv". FAIL.
   - s2:222 ran cd <memory folder> && grep -l -i -F 'ascii' -- *.md, then grep -h -i -o -E … -- *.md.
   - That folder holds four .md files whose names carry guard markers: one with j-lens and q-wen, two with o-l-m-o, one with q-wen.
   - So the glob put markers in the argv of both grep processes. The first sitting declared its own marker-in-argv greps (R:782).
41. A:97–98, (e) the string python in two grep patterns. CONFIRMED. s2:39 and s2:82. Its other appearances are pgrep's argument, the screens' interpreter path and heredoc text (s2:30).
42. A:99–101, (f) jq reads of the session's own transcript, and the cat -v of its task output. IMPRECISE.
   - The list of purposes leaves out the extraction of this check's brief: p15 (empty) and p16.
   - The cat -v printed "[killed]" (s2:184). s2:182 had taken the file's bytes and lines first (item 54).
43. A:102–103, (g) "one jq" of G-ANL-n.json's fields before its commit. IMPRECISE. The same file was also sized with wc -c (32,018 B, s2:73) and compared with cmp -s against n-analyzer's copy (s2:80), both before its commit.
44. A:104–105, (h) pgrep in the windows' checks; none read the campaign's files. CONFIRMED. 14 commands with 18 pgrep processes, each in a window's check or a screen. No command names a campaign path.
45. A:107–111, (i) name-only ls, including "a glob of its kit folders". FAIL: a slip is missing from the list.
   - At s2:106, zsh stopped ls -d "$NB"/*/kit* "$NB"/kit* with "no matches found" for the second glob, so that ls never ran.
   - The list has no zsh error, though bc85386's entry declared its three (R:840).
   - The rest of (i) holds; v7's tmp and r10's test folder were also listed. The ls -l of T is at s2:166.
46. A:112–113, (j) one grep -l over each of two globs. IMPRECISE. Each glob fed two grep processes: s2:24 ran two grep -l; s2:222 ran a grep -l and a grep -h -o. For the memory glob see item 40. The 49 mutant-output names hold no marker.
47. A:114–115, (k) the three diffs. CONFIRMED. s2:26 and s2:28 (paths masked), s2:226, s2:230.
48. A:116–118, (l) reads by name "by sed, grep, awk, cat, cmp and the Read tool". IMPRECISE. The list leaves out:
   - Forms: od (s2:46); fold (s2:48, :80, :102, :104, :106, :110); head and tail, including tail -c 1500 of a memory file (s2:147); git show <rev>:<path> and git cat-file blob (s2:57, :89, :129, :232, :234, :255); a zsh run of its own build script (p2, p5, p7).
   - Objects: its memory files (s2:8, :10, :17, :147, p17) and its own scratch outputs.
49. A:119, (m) one loop without its cd, rerun with it. IMPRECISE. The rerun (s2:118) also failed on one name: 2026-11-20_n-lock-v0_1_valuescheck.md is not in that folder. The first run is s2:116.
50. A:120–122, (n) added.txt at the root: untracked, never staged, removed after a check. CONFIRMED.
   - p2: the build script failed its first check, so the chain with the cd was skipped.
   - p3: "0 bytes; tracked: 0; staged: 0". p4: removed. See observation 4.
51. A:123–124, (o) the tail written by eye. CONFIRMED.
   - The riders' close confirmation wrote f91b8b5b…e1ee8; the note's sha256 is f91b8b5b…eee8.
   - n-build's reply caught it; the memory note was fixed at s2:253, and the next message corrected it.
52. A:125–126, (p) memory writes, and the empty heredoc file removed after a check. CONFIRMED. s2:30, s2:37, and the cat >> and sed -i '' commands.
53. A:127, (q) TaskStop of its own background find. CONFIRMED. The single TaskStop, after s2:100.
54. Missing from the list: byte and line counts. FAIL.
   - wc -c of files appears in 11 commands: s2:37, :73 (the artifact, 32,018 B, and ganl.err), :141 (the seat's raw before its commit), :143, :182, :198, :207, :255 (inside the package digest), p3, p15 and p16.
   - wc -l appears in 44 commands.
   - bc85386's entry declared both forms (R:825–828).
55. Missing from the list: a recursive grep. FAIL. s2:190 ran /usr/bin/grep -rn -F 'fid_sampled' valence_core/n scripts/n_sessions.py, a recursive content search without item 3's exclusion form. The pruned find showing no ckpt or reports folder under valence_core/ ran after it (s2:196).
56. A:130–131, committed by path, count 0, nothing on a model, not pushed. NOT CHECKABLE: the commit is still to come. Today the six drafts hold no home prefix, user name, temp path, session id or marker word (by grep).

B1–B4, the close lines
57. B1:1–5, the head and "The lock stands." (§0). CONFIRMED. raw:7, bold dropped.
58. B1–B4, lines 3–4 of each: the raw's link, 794ee42f…f084, committed in deabf3f on "Route as given". CONFIRMED. See items 2, 5 and 6.
59. B1:6–9, item 1's quotation with […]. CONFIRMED. Both parts are in paste:8 by grep -F.
60. B1:10, "Code's reading of the diff is sound and is not the instrument". CONFIRMED. raw:30.
61. B1:10–12, "printed 06b55761…1d39 and the twelve files at this entry's sha256s, byte for byte §18's claim: no STOP". IMPRECISE. 411b15c's entry gives no sha256s for the twelve files; it says "the twelve files of 516b60f's closure at the same sha256s" (R:149–150). The sha256s are §18's (raw:30: "at §18's sha256s").
62. B1:12–13, 15 of 160 and 3c70f5ff…a81d; both outputs at deabf3f, cited by the lock (§5, §18). CONFIRMED. L:412, L:798.
63. B1:14–16, item 5's flags quotation; §4's sentence; the sentence in that row at deabf3f. CONFIRMED. paste:16; raw:41; L:543.
64. B1:17–18, the 411b15c quotation from §7. CONFIRMED. raw:63.
65. B2:4–7, the G-ANL-n quotation from §5. CONFIRMED. raw:52, bold dropped.
66. B2:8, item 4, "G-ANL-n's PASS accepted, e775cbb4…6088 to hole 13". CONFIRMED. paste:13.
67. B2:9–10, the 1641948 quotation from §7. CONFIRMED. raw:63.
68. B3:4–6, the two quotations from §5. CONFIRMED. raw:50, bold dropped.
69. B3:7–8, item 4's quotation with […]. CONFIRMED. paste:13.
70. B3:9–12, the parallel-start quotation from §5, and "both parallel starts inert". CONFIRMED. raw:51; paste:16.
71. B3:13–14, the b6ea27f quotation from §7. CONFIRMED. raw:63.
72. B4:4–5, §7's "`bc85386`: the coordinating session's forms as stated." and item 5's "the departures of §7 […] inert". CONFIRMED. raw:63; paste:16.
73. B4:6–7, the announced push (its item 7) and the folders, recorded in A. CONFIRMED. R:741–742 (bc85386's heading); A:69–75.
74. B1:19, B2:11, B3:15, B4:8, the values-check given in A. CONFIRMED. A:129 holds it (a placeholder).

C, the routing raw
75. C:3, "saved verbatim by the coordinating session on receipt". CONFIRMED. W/pi-routing-received.txt is the PI's routing message in T plus a final newline (cmp). Its Write came before the relays.
76. C:3, "Its last line, "PI: Route as given", is the PI's own line after the block." CONFIRMED. It is the message's last line, after a blank line; the first sitting's raw has the same sentence.
77. C:3, the block routes the seat's read, which deabf3f carries. CONFIRMED.
78. C:3, "whose entry and four close lines quote its items 1–6 and its last line". FAIL.
   - Items 2 and 3 are not quoted in A or in B1–B4. None of these phrases occurs: "launch files under v0.1", "D_n 2026-12-15", "go, after step 10", "up through G-TIME-n", "backend-ext leftovers", "as ruled this morning". A:31–32 paraphrases the two items.
   - Items 1, 4, 5 and 6, paste:3 and the last line are quoted.
79. C:3 and C:5–27, the 21 lines between the fences are byte-identical to the saved copy, ae88a386…4d95. CONFIRMED. sed -n 6,26p into cmp; shasum; the fences are at C:5 and C:27.

P, the placement
80. P is HEAD's RESULTS.md with A at the Log's head and B1–B4 at the ends of the right entries, and nothing else changed. CONFIRMED.
   - diff shows five pure insertions: 23a24,155; 283a416,434; 460a612,622; 739a902,916; 869a1047,1054. That is 185 lines added (132 + 19 + 11 + 15 + 8) and none removed.
   - Each inserted block equals its draft by cmp. R:22 is "## Log — Phase 2" and R:23 is blank.
   - B1–B4 follow the last lines of the entries of 411b15c (R:126–284), 1641948 (R:285–461), b6ea27f (R:462–740) and bc85386 (R:741–870), each before the entry's trailing blank line.
   - W/results_head.md equals HEAD's RESULTS.md.

OBSERVATIONS
1. A:20 uses "S/", the raw's name for n-build's scratch root, without defining it.
2. A:69 gives "[push]" twice in one bullet; the C.5 line already carries it.
3. A:123–124: once this entry is committed, it carries the wrong tail as the quoted slip. "It is in no committed text" needs "but this account of it". No text at HEAD holds "f91b8b5b" (git grep with item 3's pathspec).
4. The (n) incident's command, p2, also printed "added = entry + the four close lines, in order". That was cmp of two empty inputs: a cat of draft/ paths missing at the repository root, and the empty added.txt. Its reads of new.diff and of the drafts also failed on missing names. One clause in (n) would cover it.
5. p15's time bound fell after the Agent call. It wrote an empty brief.txt and printed "list items verbatim in the brief: 0". p16 reran it: 05706edd…35bf, 74 lines, 9,387 bytes, five items verbatim. Cite p16's result.
6. A records deabf3f's verification and screen only. In this span the coordinating session also verified and screened three more commits, each with six classes CLEAR, no gitleaks findings and gl5 0:
   - b6ea27f (s2:57, s2:59): 1 commit, 5 file-diffs, 2,657 added lines;
   - 1641948 (s2:89, s2:91): 1, 5, 1,122;
   - 411b15c (s2:129, s2:131): 1, 8, 1,254.
   No committed text records these.
7. A:60's "1,649 lines" is the screen's "1649 added lines (messages included)".
8. The placeholders, counted through p20:
   - SWEEP_COUNT: 128 commands (sweep2's 108, then p1–p16, then p17–p20 during this check);
   - JQ_COUNT: 8 (s2:166, :168, :174, :178, :180, :272, p15, p16);
   - PGREP_COUNT: 14 commands, 18 processes.
   p17–p20 add a memory read with sed; shasum and wc -l of n-build's G-TIME-n PINs note; a cp of that note into W with cmp and grep -c; and a memory write with cat >> and tail. In the same span the session also sent two messages, read the note with Read, sent the PI a file (SendUserFile) and called the pod API (get-pod). The final sweep should include all of these.
9. Non-shell calls since the cutoff fall outside the list's stated scope of shell commands: two list_events of n-analyzer's session, two list_sessions, one ReadNotifications and one pod get-pod. None is a departure under the quoted rules; listed for completeness.

MY DEPARTURES
- I used two tools outside the brief's tool list:
  - od -c, once (the PI message's last bytes, from jq);
  - fold -w 200, twice (LOCK-n.md's G-VER row; the text of one transcript command).
- I read committed blobs in forms item 1 does not list:
  - git show <rev>:<path>, and git -C <repo> show HEAD:<path> inside loops. These covered RESULTS.md at HEAD, 411b15c and deabf3f; LOCK-n.md; the raw; the six new raws; the first sitting's routing raw and values-check raw; and valence_core/n/schema.py lines 279 and 576–583.
  - git cat-file commit deabf3f | sed '1,/^$/d', four times. The header was deleted before anything printed.
- Some git commands ran without item 3's pathspec: git log --format='%h' bc50244..bc85386 and bc85386..HEAD, both piped to tr; git rev-parse; git hash-object LOCK-n.md.
- I ran git grep -c -F twice over HEAD's tree with item 3's pathspec. The first printed a match count for one file under data/, outside ckpt and reports: data/echo/stageC_reads.json, a coincidental hex fragment.
- Sizes and counts:
  - wc -c of the raw at HEAD (15,217), and of piped bytes;
  - wc -l of HEAD's LOCK-n.md, RESULTS.md and hashes output, of W's drafts, of P, of the saved block, of NB's routing copy, and of listings;
  - tail -c 30.
- I ran diff and cmp with git show on process substitution, and diff of NB's draft 9 and draft 10.
- I made about 35 jq calls over T (entries, commands, messages, tool results, error scans), with most output masked by sed. One printed part of the compaction summary; it showed three session ids and the home path, in my tool output only. None of them is in this report.
- I read beyond the named sources:
  - HEAD's first-sitting values-check raw, for this report's form;
  - schema.py's lines;
  - NB's draft 9 and draft 10;
  - W/build_results.sh, W/results_head.md, W/d9_d10.diff, W/checked/, W/checked.sha256, and the head of W/sweep1_cmds.txt.
- I ran name-only ls of folders outside the named sources:
  - the memory folder, with the marker-named names filtered and masked by sed before printing, plus a count of its .md files;
  - n-analyzer's scratch folder …/n9/v7/mut/out, as a count and a bracketed marker count.
  I also listed NB/step4b/lock, r10, r10/tmp and commit10, and N filtered by name.
- I read file contents with cat, cat -n, sed -n (some with s/// masking), head, tail, awk, tr, cut, sort, uniq and non-recursive /usr/bin/grep (-c, -n, -o, -F, -x, and -f with process substitution). I used the Read tool for A and two ranges of W/sweep2_cmds.txt.
- I redirected output to /dev/null twice, by mistake: one sed and one jq whose output I discarded. I held file text in shell variables and used zsh's ${=pair} split.
- I used the A and B quotations as grep patterns in argv, after a bracketed check found no marker word in them.
- None of my commands had a marker word, or the campaign folder's plain name, in its argv: patterns were bracketed and the masking seds used hyphenated replacements. I ran no pgrep or ps and no whole-tree git status. Nothing under data/*/ckpt, data/*/reports or the campaign folder was opened, listed or hashed; git grep excluded them by item 3's form. I ran no interpreter but shasum (jq, awk and sed as listed), used no network, and wrote no file.
```
