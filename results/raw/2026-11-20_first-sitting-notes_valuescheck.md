# The coordinating session's notes on the seat's first sitting of 2026-11-20: the blind values-check, as returned, with every disposition

PI date 2026-11-20. Code (the coordinating session).

**What was checked.** One blind pass by a subagent over four drafts:
- T1, the entry (`RESULTS.md`, the Log's head), sha256 `fbc0ec01…05fc`;
- T2a–T2d, the four close lines, on the entries of `ef105f1` (`5554a83f…be0d`), `db00d6d` (`088885ae…c510`), `0744136` (`aa0889ac…2ac2`) and `e3b48ed` (`a501c859…f117`);
- T3, the routing raw `2026-11-20_first-sitting_pi-routing.md`, whole, `a9e47ff2…d793`;
- T4, their placement, in the draft of the new `RESULTS.md`, `c7c55c6b…e350`.

**The checker's brief** (`5bdadf08…bc8c`, 58 lines, given as a file with its sha256 to verify):
- named the sources, among them the coordinating session's first sweep of its own shell commands (142 commands, decoded, `5df9241c…1bb6`) and the pod session's cleanup list, and gave the coordinating session's words and acts that are in no file, (c1)–(c4);
- quoted the list of record v2's items 1–5 verbatim, from `2026-11-10_list-of-record-v2_design-to-code_answers.md`, lines 18–22;
- carried the briefs' two lines, on item 3's pathspec in a check and on globs;
- barred any interpreter but `shasum`, any write, any network, anything under `data/`, and the guard markers and `mf3` in any argv.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (219 lines, sha256 `8c460f4f…4718`). It held no local path. Its "S/" is the coordinating session's scratch folder.

**Totals:** 121 items (97 CONFIRMED, 7 IMPRECISE, 2 FAIL, 15 NOT CHECKABLE) and 12 observations.

## 1. Dispositions

- **Item 15** (IMPRECISE): applied in the checker's words: "The coordinating session told n-build that O6 rides its next change to the schema, "with the wording owed there" (§3), and n-analyzer that O6 is not part of its v7."
- **Item 45** (IMPRECISE): applied in the checker's words: "a copy of 168 of `0744136`'s files, its code and the data files the stage reads, in which a pruned count finds no `ckpt` or `reports` folder".
- **Item 54** (IMPRECISE): applied, with the second sweep's form added: "`wc -c` and `wc -l` of scratch files, of the seat's raw before its commit and of this commit's routing raw, and `wc -l` of a memory file".
- **Item 58** (IMPRECISE): applied in the checker's words: "and `git cat-file --batch-check` in its default form over two commit windows' new paths at their parents, printing the last field ("missing")".
- **Item 60** (IMPRECISE): applied in the checker's words: "`git grep` over named files and over pathspec globs of raws (once with `ADDENDUM-n3*.md`), with `':!data/**'` save one".
- **Item 61** (IMPRECISE): applied, with the second sweep's insertion scripts added: "`awk` and `sed` (line-range prints, and substitution, deletion and insertion scripts) over named files, its scratch files and command output".
- **Item 63** (IMPRECISE): applied in the checker's words: "and one over its subagents' transcripts (`agent-*.jsonl`)".
- **Item 67** (FAIL): fixed; the class is added in the checker's words: "commit-message reads, in forms item 1 does not list: one `git log -1 --format=%B` of `db00d6d` (the class `e3b48ed`'s entry declared) and four `git cat-file commit`, of `db00d6d`, `ef105f1`, `f4b3e73` and `d639bdd`, each through `sed '1,/^$/d'`, compared by `cmp` save `f4b3e73`'s, printed".
- **Item 68** (FAIL): fixed; the class is added in the checker's words, widened by observation 6 and the second sweep: three `git diff --name-only HEAD` naming folders, each printing a count, "the form Code disclosed on 2026-11-18"; one `git diff --quiet HEAD` on `valence_core/n` and `scripts/n_sessions.py`, its exit status only (second sweep); and item 1's name forms over a folder or the tree without the exclusions, `git show --name-only` of `e3b48ed` and `0744136`, `git ls-tree --name-only` of `db00d6d`'s `scripts/` and of `0744136`'s `valence_core/` (second sweep), and `git show --name-status` with `git diff --cached --name-only` and `--name-status` at `d639bdd`'s commit.
- **The NOT CHECKABLE items** (12, 18, 24, 26, 27, 37, 40, 42, 46, 48, 50, 56, 69, 70 and 110) stand: the coordinating session's acts, words and plans, the second sweep, the commit's own facts, and three counts whose outputs the first sweep does not hold. For items 46, 48 and 50, the coordinating session re-ran the counts in item 1's pruned form after the first sweep and before the check began, in commands the second sweep covers: the overlay holds no `ckpt` or `reports` folder, its one `mf3` folder is `valence_core/mf3`, and the lock folder holds no `ckpt` or `reports` folder.
- **The observations:**
  - 1, applied: "Below, "item N" is the paste block's item and "§N" a section of the raw; the raw's own routing block, §7, words the items differently in places.";
  - 2, applied: the box bullet quotes the list, "may also hold files beyond those copied back by name", and names the eight work and copy folders among the 26 (items 3, 9, 13, 14, 18, 19, 24 and 29);
  - 3, applied: the box bullet quotes "The routing calls these leftovers" and gives the holding of the four as the coordinating session's reading, put to the PI again;
  - 4, applied: a line for the process reads in the battery windows' checks (`pgrep -il python` in 25 commands; `ps -o` of the Q-F3 campaign's PID in two; `ps -axo` listings of the processes running from n-build's scratch folder, filtered by `grep`, in two);
  - 5, applied: a line for the string `mf3` in the argv of ten commands, the checker's six and the second sweep's four;
  - 6, applied: joined to item 68's line;
  - 7, applied: the `git cat-file blob` of `gvec.json` into `grep -o -F`, beside the `data/n/ids` reads;
  - 8, applied: the `cat -A` that failed silently;
  - 9, applied: the coordinating session read the command's tool result in its transcript. The loop's glob matched nothing, and its error was silenced by the loop's own `2>/dev/null`; the next command named the files. The entry states three zsh errors: this one, the `*(/N)` qualifier and `echo ===`;
  - 10, applied: T3's head now reads "whose entry and four close lines quote its items 1–7 and its last line" (the raw's sha256 moves to `db8d8db4…ddcc`; its fenced lines still equal the saved copy, by `cmp`);
  - 11, not applied: the run-in of `e3b48ed`'s entry into the next heading is HEAD's, as at `bc50244`'s entry; this commit inserts lines only;
  - 12, met: the second sweep was re-checked for the classes of items 67 and 68 and of observations 4–9.

## 2. Edits after the check

- The box bullet: the cleanup's result, from the pod session's report and checked by tool by the coordinating session (the script's sha256, the output's sha256 and its 26 lines against the cleared list, in order), in place of "The result goes in the coordinating session's next entry.".
- The command count, from the second sweep; the values-check bullet; and the `jq` line's wording for the checker's task output.
- The edits were checked by tool against the dispositions above; no second full pass was made.

## 3. The report as returned

```text
VALUES-CHECK: the coordinating session's notes on the seat's first sitting of 2026-11-20 (T1, the entry; T2a–T2d, the close lines; T3, the routing raw; T4, the placement)

Hashes were checked first with `shasum -a 256`. The brief is 58 lines, 5bdadf08…bc8c. T1, T2a, T2b, T2c, T2d, T3, T4, S/pi_routing_saved.txt and S/sweep1_decoded.txt each match the full sha256 the brief gives. The seat's raw is 001e8c12…bd11 and ADDENDUM-n3 is 7f4a7a75…9313. HEAD is d639bdd, its parent ef105f1, and origin/main is bc50244. The working tree's RESULTS.md equals HEAD's (rev-parse equals hash-object).

Short names used below:
- seat: results/raw/2026-11-20_n-gvec-gcal-reads_design-to-code_answers.md
- saved: S/pi_routing_saved.txt
- list: the pod session's cleanup/list.md
- sweep1:N: line N of S/sweep1_decoded.txt; #n is its command n
- R: RESULTS.md at HEAD
- RN: S/draft/RESULTS_new.md
- c1–c4: the brief's unwritten acts

ITEMS

T1
1. T1:1. Date 2026-11-20, "first sitting". CONFIRMED (seat:3; T3:6).
2. T1:1–2. "the reads committed at `d639bdd`". CONFIRMED. `git show --name-status d639bdd` adds that raw alone.
3. T1:2. "four close lines (item 6)" and "the push to come (item 7)". CONFIRMED (T3:22, T3:25).
4. T1:4. The raw's link path. CONFIRMED; tracked at d639bdd.
5. T1:5. sha256 `001e8c12…bd11`. CONFIRMED.
6. T1:5. 18,696 bytes. CONFIRMED (`wc -c` gives 18696; T3:10).
7. T1:5. "on the entries of e3b48ed, 0744136, db00d6d and ef105f1". CONFIRMED (seat:3).
8. T1:6. "committed by path at d639bdd, re-hashed equal to the paste block first". CONFIRMED. d639bdd's message says so. The shasum is at sweep1:1247 (#126, 14:30:16Z), before the commit at :1267 (#136). d639bdd's commit time is 14:34:29Z.
9. T1:6. "Route as given". CONFIRMED (T3:27; saved:22).
10. T1:6–8. The paste block is committed here as the routing raw. CONFIRMED: the file is present and its fenced lines equal the saved copy. The commit itself is this commit's.
11. T1:8–10. "item N" is the paste block's item; "§7" is the raw's routing block, worded differently in places. CONFIRMED. Compare seat:64–81 with T3:13–25: item 4 has "[stays up; cleanup now]" against "[stays up]", and item 7 has "[yours]" against "[push]".
12. T1:11–12. The relays (N.1–N.4 to n-build, item 4 to the pod session, A.5 to n-analyzer). NOT CHECKABLE (c1); consistent with it.
13. T1:13–14. The quote "O6's p0_count < p0_n assertion at the schema's next change, not its own delta", under n-analyzer. CONFIRMED (T3:18–19).
14. T1:14. "`valence_core/n/schema.py` is n-build's file". CONFIRMED (R:2107: "So n-build commits `schema.py`, and n-analyzer then moves `SCHEMA_SHA256` in its own commit").
15. T1:14–16. "told both sessions that O6 rides n-build's next change …, "with the wording owed there" (§3), and is not part of n-analyzer's v7". The quote is §3's (seat:45). Against c1, though, n-build was told the first part and n-analyzer the second. IMPRECISE. Fix: "The coordinating session told n-build that O6 rides its next change to the schema, "with the wording owed there" (§3), and n-analyzer that O6 is not part of its v7."
16. T1:17–18. Item 3 quote. CONFIRMED (T3:15).
17. T1:18–19. §5.2 quote. CONFIRMED (seat:56).
18. T1:19–22. The placement proposal. NOT CHECKABLE (c1); consistent with it. c1's "n-build's form first" appears as "nothing goes to root before the form is agreed".
19. T1:23. Item 4 quote. CONFIRMED (T3:16).
20. T1:23–24. "The box stays up (§5.3)". CONFIRMED (seat:58).
21. T1:24–25. The list is in scratch and not committed, and names 30 folders under /workspace/nsite and four side refs in the box's repository. CONFIRMED (list:1, :73–78).
22. T1:25–27. Four folders hold data never copied to the laptop, as described. CONFIRMED (list:14–15, :23–25, :55–56, :65–66, :84–89).
23. T1:27–28. "Those stages' reports are on the laptop." CONFIRMED. smoke-report.json was copied back (list:14–15); see also list:28, :60 and :70.
24. T1:28–29. The four were put to the PI with three choices. NOT CHECKABLE (c2); consistent with it and with the sweep's own notes (sweep1:469, :552).
25. T1:29. "Item 4's words do not name them." CONFIRMED (T3:16).
26. T1:29–31. The cleanup's scope: 26 folders, the script read first, the four held, the refs off, the repository untouched. NOT CHECKABLE (c1); consistent with it. 3+3+14+4+2 = 26 = 30 − 4, and list:81–82 says leaving 31–34 off leaves the repository untouched.
27. T1:31–32. The result goes in the next entry. NOT CHECKABLE (a plan).
28. T1:34. The raw committed by path (d639bdd). CONFIRMED.
29. T1:35–36. Close lines on the four entries, each citing the raw, one on each. CONFIRMED (T4).
30. T1:37. "the three marker-in-argv grep processes included". CONFIRMED (T3:22).
31. T1:37–38. §6 quote. CONFIRMED (seat:62).
32. T1:39. Item 6 quote on ADDENDUM-n3's gradings. CONFIRMED (T3:22).
33. T1:39–40. The note is in T2c and the addendum's bytes are unchanged. CONFIRMED (T2c:7–9; working-tree sha256 = 0744136's value, R:370).
34. T1:41. "O4 accepted [as ruled]" is in T2a. CONFIRMED (T3:22; T2a:11).
35. T1:42. "[push]", `bc50244..HEAD`, "behind the amended screen". CONFIRMED (T3:25).
36. T1:42. The amended screen is `screen4.py` with `gl5.py`. CONFIRMED (R:427, R:1347; the brief's git grep found R:388, :427 and :1347).
37. T1:42–43. The push runs in its own battery window after n-analyzer's mutant window. NOT CHECKABLE (c3); consistent with it.
38. T1:43–44. The "4 commits at this writing" are e3b48ed, 0744136, db00d6d and ef105f1. CONFIRMED (`git log bc50244..HEAD`; seat:3).
39. T1:44–45. d639bdd joins the range. CONFIRMED (parent ef105f1; origin bc50244). "This commit" is future.
40. T1:45. The C.5 line goes in the next entry. NOT CHECKABLE.
41. T1:47. "since `0744136`'s commit". CONFIRMED. 0744136 was committed 2026-11-20T03:20:06Z; #1 is at 03:20:28Z (sweep1:1); #142 filters ≥ 03:20:06 (:1279).
42. T1:47–48. The second sweep is made after the values-check. NOT CHECKABLE (future).
43. T1:48. "its first 142 the first sweep's". CONFIRMED: there are 142 headers, #1–#142.
44. T1:50–55. Five unpruned finds. CONFIRMED:
   - :16 (#4): one for `__pycache__` and the `-maxdepth 1` match;
   - :23 (#6): one for `__pycache__`;
   - :293 (#27): the listing;
   - :1104 (#108): the lock folder.
   Every other find in sweep1 is pruned.
45. T1:51. "a copy of `0744136`'s code". The overlay also holds data files the stage reads. Its manifest's 63 paths include "the two of G-VEC's outputs of record the stage reads" (R:226–228), and the manifest was checked present inside the overlay (sweep1:16 #4, :289 #27; the session's note at :370). IMPRECISE. Fix: "a copy of 168 of `0744136`'s files, its code and the data files the stage reads, in which…".
46. T1:51. In the overlay, "a pruned count finds no ckpt or reports folder". NOT CHECKABLE: the method is present (sweep1:16, #4), but the count's output is not in the sweep.
47. T1:52. 168 files. CONFIRMED (R:194, "a scratch copy of the commit's 168 files").
48. T1:52–53. None under ckpt, reports or data/m[f]3 by a count over the list. NOT CHECKABLE: the method is present (sweep1:356–358, #35), but no output is in the sweep.
49. T1:53. The m[f]3 folder is the tracked code package valence_core/m[f]3. CONFIRMED for "tracked" (`git ls-tree --name-only 0744136 valence_core/`). "One" is not checkable.
50. T1:54–55. The lock folder's "pruned count finds no ckpt or reports folder". NOT CHECKABLE: the unpruned find is at :1104, but no pruned count over that folder is in the first sweep.
51. T1:56–58. The jq reads (LAUNCH CLEARED; the first sweep; the subagents' first lines). CONFIRMED (sweep1:336 #32; :1279 #142). The second sweep is outside.
52. T1:59–60. jq over two committed data/n/ids files at 0744136. CONFIRMED (:312 #29; :491 #46).
53. T1:60. One `ls -la`. CONFIRMED (:37 #8; the only long-form ls).
54. T1:60–61. "`wc -c` and `wc -l` of scratch files". There were also `wc -c` and `wc -l` of the seat's raw in the repository before its commit (:1247, #126), and `wc -l` of a memory file (:80, #13). IMPRECISE. Fix: "…of scratch files and of the seat's raw before its commit, and `wc -l` of a memory file;".
55. T1:61–62. The package digest's forms over ef105f1 and over the overlays. CONFIRMED (:1034 #100; :16 #4; :909 #89).
56. T1:62. The package digest over the working tree. NOT CHECKABLE: it is not in the first sweep.
57. T1:63–64. hash-object and batch-check over the overlays against 0744136 and db00d6d. CONFIRMED:
   - against 0744136: #4, #27 :295–296, #47 :501–502;
   - against db00d6d: #68 :713–714, #82 :835–836, #88 :890–891.
58. T1:63–64, scope. `git cat-file --batch-check` also ran in its default form (id, type, size) over two commit windows' new paths at their parents, printing only the last field: the 20 new paths at 0744136 (:603, #55) and three raws at db00d6d (:972, #94). IMPRECISE. Fix: add "…and `git cat-file --batch-check` in its default form over two commit windows' new paths at their parents, printing the last field ("missing");".
59. T1:64–65. `git grep` with `':!data/**'` save one, that one being "amended screen" over RESULTS.md and two raw globs. CONFIRMED (:455 #43, :459–462 #44; the one is :1253, #129).
60. T1:64, "over named files". Four runs were over pathspec globs, each with `':!data/**'`: :439 (#41), :694 (#65, including `ADDENDUM-n3*.md`), :986 (#96) and :1049 (#102). IMPRECISE. Fix: "`git grep` over named files and over pathspec globs of raws (once with `ADDENDUM-n3*.md`), with `':!data/**'` save one, …".
61. T1:65–66, "`awk` and `sed -n`". IMPRECISE.
   - sed also ran substitution and deletion scripts:
     - `sed 's/\x1b\[[0-9;]*m//g'`: :2, :678, :1046;
     - `sed "s|^$O/||"` and `sed -E 's/^[0-9a-f]{64}  //'`: :16;
     - `sed 's|^|0744136:|'`: :296;
     - `sed 's/^+//'`: :641, :1030;
     - `sed '1,/^$/d'`: :652, :1032, :1261, :1267;
     - `sed "s|$HOME|<HOME>|g"`: :817.
   - awk also ran over command output: :75, :139, :364, :1255.
   - Earlier entries separate `sed -n` prints "with no substitution" (R:110).
   Fix: "`awk` and `sed` (line-range prints, and substitution and deletion scripts) over named files, its scratch files and command output;".
62. T1:66–68. Glob loops over scratch names, its own and other sessions'. CONFIRMED (:666 #61, :759 #73, :796/:798 #77, :1003 #97, :1222 #123, :1249 #127).
63. T1:66–68, scope. One glob loop was over its subagents' transcripts, not scratch: `for f in agent-*.jsonl` (:1279, #142). The listing before it (:1277, #141) printed only the last 8 names and a count. IMPRECISE. Fix: "…its own and other sessions', and one over its subagents' transcripts (`agent-*.jsonl`), not each printed whole…".
64. T1:67–68. The brief line quoted. CONFIRMED (vc_brief.md:47).
65. T1:68. The zsh error at `echo ===` after the first part had run. CONFIRMED (:1255 #130; #131 at :1257 reruns the third part).
66. T1:68–70. The memory writes. CONFIRMED:
   - `cat >>`: :6;
   - `printf >>`: :246;
   - `sed -i ''` on MEMORY.md: :14, :378, :690;
   - `rm -f`: :203, :526.
67. T1:46–70 with T1:49 ("knows of no others"). One class is unnamed: commit-message reads in forms item 1 does not list. FAIL.
   - One `git log -1 --format=%B db00d6d` (:644, #58). e3b48ed's entry declared this class (R:581), and a reviewer's `git show -s --format=%B` was declared at R:2391.
   - Four `git cat-file commit`, each through `sed '1,/^$/d'`: db00d6d (:652, #59), ef105f1 (:1032, #100), f4b3e73 (:1261, #133, its message printed) and HEAD = d639bdd (:1267, #136).
   Fix: add "commit-message reads, in forms item 1 does not list: one `git log -1 --format=%B` of `db00d6d` (the class `e3b48ed`'s entry declared) and four `git cat-file commit`, of `db00d6d`, `ef105f1`, `f4b3e73` and `d639bdd`, each through `sed '1,/^$/d'`, compared by `cmp` save `f4b3e73`'s, printed;".
68. T1:46–70. A second class is unnamed: `git diff --name-only HEAD` naming folders without item 3's exclusions or the data/m[f]3 one. FAIL.
   - `-- data/n/gcal valence_core/n` (:1086, #106);
   - `-- valence_core` twice (:1230 #123; :1241 #124);
   - each printed a count.
   This is the form Code disclosed on 2026-11-18 "for the seat to class" (R:2386–2389, in the entry headed at R:2297), and the brief's own line on git commands in a check. Fix: add "three `git diff --name-only HEAD` naming folders (`data/n/gcal` with `valence_core/n` once, `valence_core` twice) without item 3's exclusions or the `data/mf3` one, each printing a count, the form Code disclosed on 2026-11-18;".
69. T1:71. The values-checker's departures. NOT CHECKABLE (this report's own list is below).
70. T1:73–74. Committed by path; home-prefix count 0; nothing on a model; not pushed. NOT CHECKABLE (commit-time facts). The first sweep's only Python is the screen's.

T2a
71. T2a:1. Heading (item 6). CONFIRMED (T3:22).
72. T2a:2–4. Link, sha, d639bdd, "Route as given". CONFIRMED.
73. T2a:4–6. §3 quote. CONFIRMED (seat:41).
74. T2a:7–8. E = 48 and its quote; item 3. CONFIRMED (seat:42; T3:15).
75. T2a:8–9. 1 − 0.99⁴⁸ = 0.3827 (0.38271) and its quote. CONFIRMED (seat:42).
76. T2a:9–10. Power-note quote. CONFIRMED (seat:43).
77. T2a:11–12. O4 quote; item 6's "O4 accepted [as ruled]". CONFIRMED (seat:44; T3:22).
78. T2a:13–14. O6 quote; item 5. CONFIRMED (seat:45; T3:19).
79. T2a:14–15. The schema is n-build's file, so the assertion rides its next change. CONFIRMED (R:2107); consistent with c1.
80. T2a:16–17. Next. CONFIRMED (seat:46; T3:19).
81. T2a:18. Departures inert (§6; item 6). CONFIRMED (seat:62; T3:22).
82. T2a:19. Values-check pointer. CONFIRMED (T1 sits at the Log's head).

T2b
83. T2b:1–2. Heading. CONFIRMED.
84. T2b:2–5. Link, sha, d639bdd; "G-CAL-n PASSED and stands" (§0). CONFIRMED (seat:8).
85. T2b:5. The seat's arithmetic agrees with the record (§2.1, §2.3). CONFIRMED (seat:24, :28).
86. T2b:6–9. Item 2 quote, character for character. CONFIRMED (T3:14).
87. T2b:10–11. GC1 quote. CONFIRMED (seat:30).
88. T2b:11–13. Observations (a)–(d): 11 of 48, three non-words in 48, 240 of 240, banked. CONFIRMED (seat:30–34).
89. T2b:14–15. Both lock quotes. CONFIRMED (seat:28, :34).
90. T2b:16. §2.5 quote. CONFIRMED (seat:37).
91. T2b:17. Departures inert (§6) and the item 6 quote. CONFIRMED (seat:62; T3:22; R:299–304).
92. T2b:18. Pointer. CONFIRMED.

T2c
93. T2c:1–2. Heading. CONFIRMED.
94. T2c:2–5. §4 quote. CONFIRMED (seat:50).
95. T2c:5–6. Item 6 quote. CONFIRMED (T3:22).
96. T2c:7–8. The dated note, in §4's words. CONFIRMED (seat:50). The anchor is at A-n3:81 ("`valence_core/n/directions.py`:10–11 (BK §3.1's sentence)"), and 616e940 modifies directions.py.
97. T2c:8–9. The bytes are unchanged (7f4a7a75…9313). CONFIRMED.
98. T2c:10. Quote. CONFIRMED (seat:50).
99. T2c:11. Departures. CONFIRMED (seat:62).
100. T2c:12. Pointer. CONFIRMED.

T2d
101. T2d:1. Heading. CONFIRMED.
102. T2d:2–5. §0 quote. CONFIRMED (seat:7).
103. T2d:6–8. Item 1 quote, character for character. CONFIRMED (T3:13).
104. T2d:9–10. §1.3 and §1.2 quotes. CONFIRMED (seat:18, :16).
105. T2d:11. §1.4 quote. CONFIRMED (seat:20).
106. T2d:12. Departures. CONFIRMED (seat:62).
107. T2d:13. Pointer. CONFIRMED.

T3
108. T3:1. Title, in the same form as the 2026-11-19 second-sitting and third-sitting raws' line 1. CONFIRMED.
109. T3:3. PI date 2026-11-20. CONFIRMED (T3:6).
110. T3:3. Given "in chat", saved verbatim "on receipt", and the last line is "the PI's own line after the block". NOT CHECKABLE.
111. T3:3. The last line is "PI: Route as given". CONFIRMED (saved:22; T3:27).
112. T3:3. It routes the seat's raw committed at d639bdd. CONFIRMED (T3:9–10; d639bdd).
113. T3:3. The entry and four close lines quote it. CONFIRMED: T1 quotes items 3–7 and "Route as given", and T2a–T2d quote items 1, 2, 6 and "Route as given". The commit itself is pending.
114. T3:3. The 22 lines between the fences are byte-identical, sha256 84eafa04…15b8. CONFIRMED: T3 lines 6–27 match saved under `cmp` (exit 0), and both are 22 lines.
115. T3:5 and :28. The fences, in the earlier raws' form. CONFIRMED.

T4
116. T1 is at the Log's head. CONFIRMED. `diff -U0` shows @@ -23,0 +24,75 @@. RN:22–23 holds the heading and its blank line, RN:24–98 equals T1 under `cmp` (its last line blank), and RN:99 is ef105f1's heading.
117. T2a sits at the end of ef105f1's entry. CONFIRMED (@@ -138,0 +214,19 @@; RN:214–232 equals T2a under `cmp`; :233 is blank and :234 is db00d6d's heading).
118. T2b sits at the end of db00d6d's entry. CONFIRMED (@@ -363,0 +458,18 @@; RN:458–475 equals T2b; :476 is blank and :477 is 0744136's heading).
119. T2c sits at the end of 0744136's entry. CONFIRMED (@@ -476,0 +589,12 @@; RN:589–600 equals T2c; :601 is blank and :602 is e3b48ed's heading).
120. T2d sits at the end of e3b48ed's entry. CONFIRMED (@@ -610,0 +735,13 @@; RN:735–747 equals T2d; RN:748 is the next heading).
121. Nothing else changed. CONFIRMED: there are exactly five hunks, all pure insertions, with no deleted line.

TOTALS
121 items: 97 CONFIRMED, 7 IMPRECISE (15, 45, 54, 58, 60, 61, 63), 2 FAIL (67, 68) and 15 NOT CHECKABLE. There are 12 observations.

OBSERVATIONS
1. T1:9 defines "§7" but T1 never uses it. T1's other "§N" (§3, §4, §5.2, §5.3, §6) are the raw's sections, and that is not stated. Either say "§N is the raw's section, §7 its routing block" or drop "§7".
2. The list also says "The work and copy folders may also hold files beyond those copied back by name; I took no look inside them" (list:90–91). The 26 folders in scope include eight such folders: 3, 9, 13, 14, 18, 19, 24 and 29. The session's own note at sweep1:468 records this, but T1 omits it. It bears on ledger 27.
3. Holding the four folders is the coordinating session's reading of item 4. The list itself says "The routing calls these leftovers" (list:92). T1 could label it as a reading put to the PI, as the second sitting's notes did (R:805).
4. The sweep reads the running Q-F3 campaign's process:
   - `ps -o pid,ppid,etime,lstart,nice -p 8051` (:62, #10);
   - `ps -o pid,nice,etime -p 8051` (:141, #18);
   - `ps -axo …,command` filtered by grep (:137, :139, #18; :170, #19);
   - `pgrep -il python` in 22 commands.
   Item 5 binds the end-wait to the PID and bars reads of the stage's files, so as I read it none of these is a list-of-record departure. The brief's RULES do bar listing that process. T1 names none. The seat may want them stated plainly, as T1 does for the glob line.
5. The string m-f-3 appears literally in the argv of six commands (:356 #35; :362, :364 #36; :592 #54; :627–628, :647 #58; :966 #94; :1019–1020, :1035–1036 #100). It is not one of m's five guard markers (R:7333–7334), and none of those five appears in any first-sweep argv (bracketed scan). The brief's RULES bar it, though. Same reasoning as observation 4.
6. Other item-1 name forms ran over the whole tree or a folder without the exclusions:
   - `git show --name-only --format= e3b48ed 0744136` (:362);
   - `git ls-tree --name-only db00d6d scripts/` (:767);
   - bare `git show --name-status` (:1259, :1267);
   - `git diff --cached --name-only/--name-status` (:1263, :1267).
   Item 1 permits these; the standing pathspec form does not. They could join item 68's line.
7. `git cat-file blob 0744136:data/n/gvec/gvec.json | /usr/bin/grep -o -F …` (:284, #27) reads a data file's content, the same kind of read as the data/n/ids jq reads T1 states plainly. It is not barred, since it is not ckpt or reports. The data digests (:277–281, :632, :1087) are item 1's form.
8. A `cat -A` failed silently (:999, #97; macOS cat has no -A). At :748 it fell back to `cat -v`. A precedent for stating this is R:861.
9. A second zsh error is likely. #61 (:666) loops over `"$S/push13-074"/*.out`, but that folder held only .txt and .json files (#1, :2). Under zsh's default NOMATCH the loop errors, and #62 (:669) reran 3 s later with literal names. The sweep holds no output, so check the transcript.
10. T3's head does not name the items quoted, as both earlier routing raws did (second sitting :3 "its items 1, 2, 3, 5, 6, 7 and 8"; third sitting :3).
11. e3b48ed's entry, now ending with T2d, still runs into the next heading with no blank line (HEAD:R:610–611 → RN:747–748). This was already so at HEAD and is cosmetic.
12. Before writing "knows of no others", re-check the second sweep for the classes in items 67–68 and observations 4–9. Commit-message checks for this commit would recur, for example.

DEPARTURES (mine, plainly)
- One command was denied by the permission system and did not run: a slip that used `awk` (`grep -n '^- 20' RESULTS.md | awk -F: '$1 < 2386' | tail -n 1`), against the brief's no-interpreter rule. I redid it with `head`, `grep` and `tail`.
- `git cat-file commit d639bdd | fold` used the brief's form, but it printed the object's header too: tree and parent ids, and the author and committer lines with name, address and times. Item 1 names commit times only.
- `git ls-tree --name-only 0744136 valence_core/ | /usr/bin/grep -E 'm[f]3'` named a folder without item 3's exclusions. It cannot reach data/. Its one output line holds the m-f-3 string, in output only.
- `wc -c` of the seat's raw (a size, outside data/). `wc -l` of T3, saved, the five draft texts and sweep1. `tail -c 1 | od -c` on T3 and saved.
- I used `diff -U0` with stdin from `git show HEAD:RESULTS.md` in place of `git diff --no-index`.
- `sed -n` line-range prints, with no substitution, of RESULTS.md and the addendum. This is stated in case sed counts as an interpreter.
- Reads beyond the named sources:
  - RESULTS.md lines 1–23, 686–705, 774–885, 2102–2108, 2386–2393 and 7328–7338;
  - whole-file greps of RESULTS.md (close-line heads, guard-marker lines, schema ownership, %B and cat-file forms, entry heads);
  - the addendum's headings.
  Some printed lines held guard-marker words or m-f-3 in their output only (R:600, :7334–7336).
- `git rev-parse HEAD:RESULTS.md` and `git hash-object RESULTS.md`; `git log` of ids and parents, and of `%cd` commit times; and `git show --name-status` of eight commits, each with `-- . ':!data/**' ':!data/m[f]3/**'`.
- I ran no interpreter but shasum and wrote nothing. I used no network. Nothing under data/ was listed, read or hashed. No marker string went literally into any argv. I did not touch, list or signal the Q-F3 process.
```
