# n — the seat's block on the N-pod campaign's eight starred readings: the blind values-check, as returned, with every disposition

PI date 2026-11-23. Code (the n-build session).

**What was checked.** One blind pass by a subagent over three drafts, at HEAD `098218c`:
- T1, the block, sha256 `ef8b64e7…4e5b` (305 lines);
- T2, the head of the campaign's spec raw, `cc1b2427…8bfd` (48 lines), and the raw built from it, `233b4173…832e`
  (724 lines): the head's claims, and each fenced section against its source;
- T3, this commit's entry, `be927cc3…deae` (134 lines), its three placeholders (the values-check's summary, the
  checker's departures, and Code's commands after the check) not to be checked.

**The checker's brief** was given to the checker as its prompt: Code's scratch file `S/step4b/camp/seat/vc_brief.md`
(`8916cd5c…aed3`, 116 lines). It:
- named the texts and the sources. In the repository, the files the texts cite, at `098218c`, each checked tracked and
  clean. In Code's scratch, by name and sha256 only: the readings as sent, the routing, the survey's brief in both
  forms, and its report;
- allowed `shasum` by name; `jq` on committed JSON outside `data/*/ckpt`, `data/*/reports` and `data/m[f]3`; and `jq`
  on this session's transcript, for a sweep of Code's shell commands from step 13's entry's final sweep to the brief's
  own hash, in four spans with their counts. It barred any other interpreter (`awk` among them), any write, any
  network, any guard marker in an argv (a grep pattern and the command's own text included), and globs over the root,
  `results/raw/` or a folder of marker-named files;
- barred anything under `data/m[f]3`, any read, listing, size or time of a ckpt or reports file, anything in Code's
  scratch but the named files, and any look for G-TIME-n's two steered cells;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec and the campaign folder's
  exclusion on every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (251 lines, sha256
`86bb0ff0…6a02`), with one change: its item 100 lists the strings it counted to find no local path in the raw,
three of which a commit here may not carry. They are written "the home root", "the temp root's user folder" and "the
scratch folder's name"; nothing else is changed. It names scratch files only by their paths inside the scratch
folder, and the transcript as T. Its times are T's UTC stamps, Code's own, which the brief asked for.

**Totals:** 124 items: 97 CONFIRMED, 18 IMPRECISE, 4 FAIL, 5 NOT CHECKABLE; and 12 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

Every FAIL and every IMPRECISE item is applied, in the checker's words or the words below. Every observation is
applied or met. §2 gives the edits and their check by tool.

**The four FAILs:**
- **Item 89, T2:7–10.** Applied in the checker's words: the readings went to the coordinating session as a note in the
  sessions' notes folder, a byte copy of Code's scratch file checked by `cmp`, named in Code's message by its name,
  its sha256's abbreviation and its line count.
- **Item 107, T3:50.** Applied: two memory notes, `cat` of one, `wc -l`, `tail` and `grep -o` of the other.
- **Item 112, T3:83–85.** Applied: the `printf >>` to the memory index, outside scratch, with `tail` and `wc -l`
  after it; and, in scratch, the campaign folder's `mkdir -p` and the two files made by redirects.
- **Item 115, T3:97–103.** Applied: fifteen committed raws; five commands with the working folder in `results/raw/`;
  the second narrow glob, in `results/raw/`; the `grep` over `valence_core/n/*.py`; `wc -c` of one line of
  PROPOSAL-m.

**The eighteen IMPRECISE items:**
- **Item 5, T1:8.** Applied: the previous thread read v1.0's draft (ans23a). The new thread's read of the commit is
  observation 1's.
- **Items 7 and 8, T1:10–11.** Applied in the checker's words: the pin is the lock's sha256, `LOCK_SHA256`; `gtime`
  and `gver` refuse by LOCK:356–361, and the self-test fails on the same checks (drv:4562, :5549).
- **Item 41, T1:134–135.** Applied: the renderer's own message in the package's masked form (ids:148–151, its token
  ids masked), never a token id; the claim of "no position" is dropped there. The driver's own docstrings for the
  excerpt (`camp_excerpt`, `_camp_rendering`) said the same "never a position"; the BUILD's draft 2 corrected them
  ("never a token id"), and passed its self-test in its own window.
- **Item 54, T1:166–167.** Applied in the checker's words: by Code's design only while a pause stands; the schema
  names that case and asks only for the stop record (schema:213).
- **Item 63, T1:211–213.** Applied: "the record on disk (ans22a:25, the supplement's F5), here the report".
- **Item 64, T1:214–217.** Applied in the checker's words: the ruled kinds named, and Code's additions named as
  Code's.
- **Item 68, T1:222–223.** Applied: drv:4384–4385, :4391–4405 and :4448.
- **Item 71, T1:233–234.** Applied in the checker's words: Code's reading, beside the respawn protocol's two steps.
- **Items 106, 108, 110, 111, 114, 116, 119 and 122, T3's departures.** Applied: each missing command kind is named in
  its span, in the checker's words where it gave them.
- **Item 121, T3:117–119.** Applied: the outputs that printed Q-F3's folder's short name are named, the `sed -n` of
  ans18c:32 and the five file-tool reads among them.

**The twelve observations:**
- **O1, the new seat raw.** Met by the routing. Code told the coordinating session at once and held the block's
  window request. The coordinating session put the raw to the PI, whose word was "Route as given" (rt23b); the raw is
  committed, with its close line on `098218c`'s entry, at `c26b117`, this block's parent. Its §2's eight points (N.2)
  are carried into the PINs by Code's addendum to the readings, the spec raw's §3. The block cites the raw as ans23b:
  its §2 item 4 in CP8 (each excerpt in its own raw) and in Q3; its item 5 in CP12; its item 8 is the spec raw's and
  the block's one commit. The parent moved to `c26b117`: R: stays `RESULTS.md` at `098218c`, as the block's short
  form now says with `c26b117` named as its parent, and the spec raw's head keeps every file:line at `098218c`.
- **O2, after13's output.** Applied: it is committed with this entry as its own raw, verbatim, and the entry gives its
  provenance.
- **O3, CP2 against CP9 (a).** Applied: CP2's build line names G-VER's record, written beside the report at a G-VER STOP
  at the start.
- **O4 and O5, Q4.** Applied: Q4 asks what follows a ruled G-VER STOP at the start, and whether the PI's stop is open
  with no pause standing.
- **O6, Q7.** Applied: CP13's texts quote m:251's clause on a restart, and Q7 asks which governs a restart for n.
- **O7, CP8's file alternative.** Applied: m keeps its file beside the checkpoint; here it would sit under
  `data/n/reports/`, since the analyzer refuses a file beside the cells that no cell names (anl:3199–3203).
- **O8, T1:201.** Applied: "nothing in the driver; the BUILD adds the `.gitignore` lines (CP10)".
- **O9, the G-VER precedent.** Met: the block's claim is that each block went in before its BUILD, which holds for
  both; the rulings' order is not claimed.
- **O10, the file tools.** Applied: one bullet names the file tools' reads and writes in every span.
- **O11, CP12 and CP9 (b).** Applied: CP12 says that at a G-VER STOP at a resume the exit and the last line name the
  STOP, while the report keeps the last invocation's end state by design.
- **O12, words a scan might flag.** Met: they are the survey's brief and report, verbatim; the commit gate's scan of
  the added lines counts local roots, IPv4 forms, the scratch folder's name and session-id runs, none of which they
  hold.

## 2. The edits, checked by tool

The edits were made to new versioned copies of the three drafts. Each was recovered from this session's transcript by
`jq` and replayed on the draft the checker read, each change's old text found exactly once, by the replay script
`S/step4b/camp/seat/edits_check.sh`. The results are byte for byte the revised drafts, so nothing else changed after
the check:
- the block, 48 of 48 edits; the spec raw's head, 11 of 11; the entry, 40 of 40.

They are, in order of time: this check's dispositions; the changes the BUILD's blind review made to what the block
says Code will build, with two of its questions for the seat; the PI's routing of the seat's new raw (ans23b) and the
addendum's place as the spec raw's §3; the focused values-check's dispositions, its raw committed beside this one;
and the rebase onto `c26b117`. The entry's edits include its placeholders, filled with this check's summary, the
focused check's, and the departures' final sweep. After the edits, one placeholder was filled by tool: the entry's
count of these edits.

## 3. The report, as returned

```text
BLIND VALUES-CHECK: T1 (S/step4b/camp/seat/block_src.md), T2 (S/step4b/camp/seat/spec_head_src.md and S/step4b/camp/seat/spec_v1.md) and T3 (S/step4b/camp/seat/entry_src.md), at HEAD 098218c

Inputs checked first. All nine named S files match their sha256s. Line counts: T1 305, spec_head_src 48, spec_v1 724, T3 134, cp_readings_v1 190, routing_camp.txt 19, both briefs 105, report 342. HEAD and origin/main are both 098218c07c67… . Every cited repository file is tracked and clean (`git rev-parse HEAD:<path>` equals `git hash-object`).

Totals: 124 items, 97 CONFIRMED, 18 IMPRECISE, 4 FAIL, 5 NOT CHECKABLE.

The FAILs:
- **Item 89 (T2:7–10).** How the readings reached the coordinating session is misstated.
- **Item 107 (T3:50).** Span B read two memory notes, not "one".
- **Item 112 (T3:83–85).** Span C's memory bullet leaves out an append to MEMORY.md, which is outside scratch.
- **Item 115 (T3:97–103).** "Twelve" committed raws should be fifteen, "four" commands should be five, and two globs are not declared.

The most important finding is Observation 1. A new, untracked seat raw that bears on the block now sits in results/raw/.

## ITEMS

### T1 (the block)

1. T1:1, :16, :285–305. The starred eight are CP2, CP6, CP8, CP9, CP11, CP12, CP13 and CP16, with Q1–Q8 one per reading. CONFIRMED: cp_readings marks ★ on exactly these (spec_v1:79, 128, 143, 161, 183, 192, 202, 221), and routing_camp.txt item 4 names the same eight.
2. T1:3–4. "The PI's word governs only the nudge to the seat." CONFIRMED by routing_camp.txt item 2.
3. T1:7 (also T3:6). LOCK-n v1.0 is at 098218c, sha256 59e0b1bc…00aa, and is on origin. CONFIRMED: shasum gives 59e0b1bcb364…9900aa; `git log -1 -- LOCK-n.md` gives 098218c; origin/main is 098218c.
4. T1:7. The quote "the lock the N-pod campaign follows" (LOCK:3–4). CONFIRMED.
5. T1:8. "The seat's last thread read it and then handed off (ans22b:31; rt23a:37–38)". IMPRECISE. ans22b:31 plans the handoff "after the v1.0 read", and rt23a:37–38 records it. But that thread read the draft (ans23a), not the committed file, and a new thread has since read the commit (Observation 1).
   - Put instead: "The seat's last thread read v1.0's draft (ans23a) and handed off (ans22b:31; rt23a:37–38)". Also cite the new raw if it is routed first.
6. T1:9 (also T3:8–9). The drv:285 quote. CONFIRMED.
7. T1:10. "The driver's one lock pin is still LOCK-n v0.1's (drv:3820)". IMPRECISE. drv:3816 heads a whole block of "LOCK-n v0.1's pins" (LOCK_PATH :3819, LOCK_SHA256 :3820, LOCK_SITE :3821 and the other LOCK_* values). Only the sha256 pin is at :3820.
   - Put instead: "The driver's pin of the lock's sha256, `LOCK_SHA256`, is still LOCK-n v0.1's (drv:3820)".
8. T1:10–11. "its self-test, `gtime` and `gver` refuse … (LOCK:356–361)". IMPRECISE. LOCK:356–361 covers only the G-TIME-n and G-VER commands (drv:3913–3914, :5167–5168). The self-test failure comes from the code: `_gtime_selftest` calls `gtime_lock_inputs(work)` at drv:4562, which raises at :3913–3914 and is caught as a FAIL at :457–460; drv:5549 calls `gver_lock_check`.
   - Put instead: "so `gtime` and `gver` refuse at this HEAD until the BUILD moves it (LOCK:356–361), and the self-test fails on the same checks (drv:4562, :5549)".
9. T1:12. "19 open questions". CONFIRMED (spec_v1:691–711).
10. T1:14–15 (also T3:10–12). The PI's answer "Build on the PINs", relayed verbatim on PI date 2026-11-23, with the BUILD in the driver alone. CONFIRMED by routing_camp.txt lines 1, 3 and item 1.
11. T1:16–17, :51 (also T3:13–15). The quote from rt23a item 3 (rt23a:27–31). CONFIRMED.
12. T1:17–18 (also T3:15–16). The blocks went in before their BUILDs: 2ca24e8 (2026-11-21T03:47:59) before 91f0d35 (06:36:37), and d92500b (2026-11-22T10:55:29) before 2834c2d (14:35:02). CONFIRMED by commit times and subjects. See Observation 9.
13. T1:21–25. The spec raw's path, §1 (fd80cf43…23b0, 190 lines) and §4 (7f728f96…43d1, 342 lines, at 098218c). CONFIRMED.
14. T1:26–28. v1.0's part is lines 1–395, with v0.1 beneath. CONFIRMED: LOCK:393–394 close the v1.0 part, LOCK:396 is v0.1's title, and the file is 1453 lines.
15. T1:31–40. All ten cited raws exist. CONFIRMED: each is tracked and clean.
16. T1:42–44. The driver last changed at 2834c2d and the package at ef105f1. CONFIRMED (`git log -1`).
17. T1:58–60, :135 (also T3:21–23). CP8 as sent says "the first differing position and its two token ids" (spec_v1:152). The ids:688 citation is a self-test check, "a problem line never quotes a token id". CONFIRMED.
18. T1:61–65. The dependencies, including "[stays up]" (rt23a:39). CONFIRMED by routing items 4–5 and rt23a:39.
19. T1:73. ans22b:22 (i). CONFIRMED.
20. T1:77. runner:397–410, the refusals before the first launch. CONFIRMED.
21. T1:81–82. The n:97 and n:159 quotes. CONFIRMED.
22. T1:83. ans21b:39, the smoke's two ends. CONFIRMED.
23. T1:83–84. "No option and no smoke (GV8)" (drv:260). CONFIRMED.
24. T1:85–87. The ans21b:29 quote, plus ans21b §1.8 and rt21b item 2. CONFIRMED (ans21b:31–32; rt21b:23–26).
25. T1:88–89. "it writes only its root and its report". NOT CHECKABLE: this is the plan. See Observation 3.
26. T1:95–96. The ORDER PIN quote (LOCK:1252). CONFIRMED.
27. T1:98–100. The runner's per-read line. CONFIRMED. runner:475 holds the index, `bk_run`, arm, direction and dose; :509–511 hold `fid` (rel against TAU) and ms. No margin appears.
28. T1:101–102. The report holds no margin. CONFIRMED by REPORT_FIELDS (schema.py:1151–1168). Its cells carry only json_sha256, capture_sha256 and a record count.
29. T1:103. ans22b:22 (ii). CONFIRMED.
30. T1:106–108. n:148 "No looks (§2.5)." and the n:130 quote. CONFIRMED.
31. T1:110. The survey's 3.5. CONFIRMED (spec_v1:617).
32. T1:118. LOCK:933–934. CONFIRMED.
33. T1:119–120. The pause record's fields (schema:1169–1184). CONFIRMED.
34. T1:121. ans22b:32 and ans23a:53, "its pauses to the seat on the excerpt". CONFIRMED.
35. T1:122–124. m:271's last sentence, m:318's exception (1), and the stages.py:272 quote. CONFIRMED.
36. T1:124–125. "excerpt" is not in m's text, and the survey's m:330 is corrected. CONFIRMED: a case-insensitive grep count in PROPOSAL-m is 0, and m:330 is about the cadence of looks.
37. T1:125–126. n:16. CONFIRMED ("Every campaign read is one forward over a fixed token sequence").
38. T1:130–131. The binomial figure (k, n, p0, alpha) is in the pause's record. CONFIRMED (schema.py:1178–1180, :1185–1194).
39. T1:131–132. `absdiff` against C = 0.25 (schema:416, :428). CONFIRMED by schema.py:416 and :428–429 and LOCK:946–947.
40. T1:133–134. The rendering pause's figure by digest (runner:477–479). CONFIRMED.
41. T1:134–135. "the renderer's message in the package's masked form (ids:148), with no position and no token id". IMPRECISE. ids.py:148–151 masks only bracketed lists. A position stays in the message: ids.py:143 reads "tokens {at}-{at + 1} are not the recorded split's", and the case at ids.py:688–690 keeps "tokens 482-483".
   - Put instead: "or the renderer's message in the package's masked form (ids:148–151), its token ids masked and any position it names dropped from the excerpt".
42. T1:136–138. The conditional ruling raw was given before backend-ext-2 ran. CONFIRMED: the raw's line 3 says so, it was committed at c7d0009 (2026-11-18T22:32), and backend-ext-2 came at 9f64305 (2026-11-19T01:13).
43. T1:138. 0.3827 (LOCK:1070–1074). CONFIRMED.
44. T1:139–141. R:7842–7847's form, a fresh sparse copy with the report, cell and arrays copied by name and checked by sha256. CONFIRMED.
45. T1:141. runner:420–421. CONFIRMED.
46. T1:142. ans21c:33, "one load and one G-VER each". CONFIRMED.
47. T1:143–145. The n:148 quote and runner:418–428. CONFIRMED.
48. T1:154–155. runner:363 (`"stop": None`) and runner:331 ("nothing resumes after a STOP"). CONFIRMED.
49. T1:156–159. The G-VER-STOP report form, with `detail` at most 200 characters (schema:1195–1199, :1533–1537). CONFIRMED.
50. T1:159–160. anl:6710–6719 (NO_ARM_CAUSE at anl:6238). CONFIRMED.
51. T1:161, :170–171. The LOCK:938 quote. CONFIRMED.
52. T1:162–163. A G-VER-STOP report may hold no record. CONFIRMED: schema.py:1534–1535 fail if any arm obtained a read.
53. T1:163–164. G-VER's report is printed whole at G-TIME-n (drv:4345–4346). CONFIRMED.
54. T1:166–167. PI-STOP "only while a pause stands (schema:208–210: …)". IMPRECISE. The quote is exact, but the schema does not require a standing pause. schema.py:213 needs only the stop record, and :1520–1524 allow PI-STOP with no pause standing. The restriction is Code's.
   - Put instead: "`campaign --pi-stop RAW` writes end state PI-STOP, by Code's design only while a pause stands (the schema names that case, schema:208–210: "the PI may stop a unit whose pause stands", and asks only for the stop record, schema:213)".
55. T1:167–168. schema:1197, n:134, and "nothing writes one now". CONFIRMED: the driver mentions PI-STOP 0 times, and the runner only in a self-test string (runner:752).
56. T1:172–173. GV7 stands (ans22a:39), and the quote from results/raw/2026-11-22_n-gver_spec.md:136–138. CONFIRMED.
57. T1:175. The drv:4348 quote. CONFIRMED.
58. T1:183–187. n:159; 138 cells (drv:4654); 31 arrays per cell (LOCK:855–857); `schema.capture_filename` (schema.py:532); `json_sha256` (schema.py:1159–1161). CONFIRMED.
59. T1:188–189. `data/n/ckpt/time/` (drv:3796; .gitignore:338–340) and the two hashes at LOCK:386. CONFIRMED.
60. T1:191. LOCK:385–388. CONFIRMED.
61. T1:193–194, :197–200. The ans21b:31 and :32 quotes, rt21b:23–26, ans23a:44 (edit 2), m:251 and n:103. CONFIRMED.
62. T1:209–211. "2 is left to Python's usage errors (argparse exits 2)". CONFIRMED: the driver uses argparse (drv:289, :6091–6092), and ans22a:25 notes "argparse's exit 2".
63. T1:211–213. "the exit, the last line and the report (ans22a:25 …)". IMPRECISE. ans22a:25's third item is "the record on disk".
   - Put instead: "the exit, the last line and the record on disk (ans22a:25, the supplement's F5), here the report".
64. T1:214–217. The INTEGRITY list "as ruled for G-VER of record". IMPRECISE: the claim is stronger than its source. The rulings name the weights folder's files (a missing folder included), one of the eight non-shard files, and an ids file or MANIFEST.json's hash or count (ans22a:27; ans22b:24). The model manifest, the lock, G-VEC's and G-CAL-n's files, the package and its closure, and a direction's sha16 are Code's extension. The ids' files are dropped.
   - Put instead: "The classes, as ruled for G-VER of record (ans22a:26–29; ans22b:24) and extended by Code to the campaign: a refusal on a file's hash or byte count is INTEGRITY (ruled for the weights folder's files, a missing folder included, the eight non-shard files and the ids' files; Code adds the model manifest, the lock, G-VEC's and G-CAL-n's files, the package and its closure, and a direction's sha16)".
65. T1:217. The ans22a:27 and :28 quotes. CONFIRMED.
66. T1:218–219. runner:12–15 and the A-n3:60 quote. CONFIRMED.
67. T1:220–221. The ans22a:8 quote, ruled for G-VER of record. CONFIRMED.
68. T1:222–223. G-TIME-n's exits "(drv:4391–4405 …)". IMPRECISE. Those lines hold exit 2 (at :4397 and :4400), 3 and 1 (at :4405). Exit 0 is at drv:4448, and the docstring at :4384–4385 states all four.
   - Put instead: "(drv:4384–4385, :4391–4405 and :4448: …)".
69. T1:230–231. The schema:458–459 quote. CONFIRMED.
70. T1:231–233. gvrun:42–63. CONFIRMED: gvrun:45 shows the same pod id, and :46–48 show PID 1 started before the state check, which came before v1's launch.
71. T1:233–234. "nothing runs until they rule (CLAUDE.md's respawn protocol)". IMPRECISE. The protocol requires its INTEGRITY and BACKEND steps on a new or replacement box, "Both PASS before anything runs". It says nothing of a report to the seat and the PI, or of a ruling.
   - Put instead: "… until they rule (Code's reading; the respawn protocol has its two steps PASS before anything runs on a new or replacement box)".
72. T1:235–237. The m:251 quote (which n:101 carries), LOCK:191–194, and ans22a:33. CONFIRMED.
73. T1:238. "n:152 dates v1.0 alone". CONFIRMED.
74. T1:239–241. The n:101 and LOCK:1164 quotes. CONFIRMED.
75. T1:242. The pod pin refuses another pod. CONFIRMED (drv:630, :1187–1188). The exit 1 is plan, since gtime's refusals exit 2.
76. T1:249–251. ans21b:29, list item 4's halt, and "origin is public". CONFIRMED (ans18c:32 says "the public origin").
77. T1:252–254. The three ans18c:32 quotes, about backend-ext's cell. CONFIRMED.
78. T1:262. The package at 06b55761…1d39. CONFIRMED (LOCK:163–165; routing item 1).
79. T1:263–268. The BUILD and run sequence. CONFIRMED against routing items 1 and 3–5. The rest is plan.
80. T1:273–275. The twelve unstarred readings. CONFIRMED (8 + 12 = 20).
81. T1:276–277. mF3ans:43 and the quote "the seat's to confirm for n" from CP4 as sent (spec_v1:118). CONFIRMED. Note that m-F3's line is its DRIVER line, while n's plan uses the STAGE line.
82. T1:278–279. A-n3:60's "committed at step 14". CONFIRMED.
83. T1:280–281. The survey's departures are four items. CONFIRMED (spec_v1:715–721).
84. T1:41. "R … 098218c, this block's parent". NOT CHECKABLE (plan). See Observation 1.
85. The "As Code will build it" and "Another answer" lines (T1:88–92, 111–114, 146–151, 176–180, 201–205, 224–226, 242–246, 255–257). NOT CHECKABLE, except as in items 25 and 75 and Observations 3, 7 and 8.

### T2 (the spec raw)

86. The assembled raw. CONFIRMED: `sed -n` ranges 1–48, 53–242, 248–266, 272–376 and 382–723 of spec_v1.md hash to spec_head_src, cp_readings_v1, routing_camp, brief_scrubbed and survey_report_v1, byte for byte.
87. T2:13–14. brief_scrubbed.md differs from the survey brief in one place only. CONFIRMED: `diff` gives one hunk, 2c2, where the full repository path becomes `<repo>`.
88. routing_camp.txt against the transcript. CONFIRMED. T's line 74133 is a "user" record whose content is a string of 24 lines (timestamp 2026-11-24T00:38:11Z). Its lines 3–21 hash to 90769590…58b8. Lines 1–2 and 22–24 are the wrapper, which names a session by its id.
89. T2:7–10. "as a file in Code's scratch folder, named by its path and sha256, with a byte copy in the sessions' notes folder". FAIL. Code's message (SendMessage at 23:22:30Z) names the readings only as the notes-folder note "2026-11-23_n-build_campaign-pins.md (fd80cf43...23b0, 190 lines)". The scratch path appears 0 times and the full sha256 0 times. The note is the byte copy made by `cp` and checked by `cmp` at 23:22:14Z.
   - Put instead: "They went to the coordinating session as a note in the sessions' notes folder (`2026-11-23_n-build_campaign-pins.md`), a byte copy of Code's scratch file checked by `cmp`, named in Code's message by its name, sha256 abbreviation and line count; the coordinating session re-hashed it equal before it routed them (§2)."
90. T2:9–12. §1 and §2 are "in no other repository file". CONFIRMED: `git grep -l -F` of distinctive phrases over the tree, with item 3's pathspec, finds 0 files.
91. T2:11–18. §2 to §4: hashes, line counts, compiled at 098218c, and extracted from the hand-back by `jq` on 2026-11-23. CONFIRMED (T at 23:16:39Z).
92. T2:20–21. Every file:line is at 098218c and no cited file has changed. CONFIRMED (HEAD unmoved, cited files clean).
93. T2:25–27. The note on CP8's pause record: `arms_in_scope` (schema.py:1174–1175) and the binomial batch (:1178–1180). CONFIRMED.
94. T2:28–30. The note on CP8's ceiling figure: `absdiff` (schema.py:416), `rel` (:418), runner.py:509–511. CONFIRMED.
95. T2:31–32. The note on CP12: ans22a:26 is the §1.4 text (§1.4 heads at ans22a:23), and ans22a:8 is the summary line that §4 quotes. CONFIRMED.
96. T2:33–34. The note on §4's 2.3: drv:4654 gives "120 of 40 rows and 18 of 160", drv:4653–4657 hold no 4,278, and 138 × 31 = 4,278. CONFIRMED.
97. T2:35–37. The note on §4's 3.6, m:330. CONFIRMED.
98. T2:38–41. CP8's correction: ids.py:688, ans22a:24 ("no token id"), runner.py:477–479. CONFIRMED.
99. T2:43–45. How §2 was taken (T at 00:45:37Z and 00:45:44Z). CONFIRMED.
100. T2:47–48. No home path and no full scratch path in the raw. CONFIRMED: counts of 0 for the home root, /private/, the temp root's user folder, the scratch folder's name, the home name and ~/. There are no session or agent ids in any of the three texts.

### T3 (the entry)

101. T3:1–4, :29–30. The title and both raw paths. CONFIRMED.
102. T3:17–28. The summary of the block. CONFIRMED against T1 §0–§3.
103. T3:31–38. The summary of the spec raw, including "which the block carries correctly". CONFIRMED.
104. T3:39. "nothing ran on a model". CONFIRMED: no python, node, perl or model command appears among the 137 swept commands.
105. T3:44, :66, :86. The span counts 16, 32, 25 and 52. CONFIRMED by `jq` over T (spans A–D exactly; nothing between 23:30Z and 00:30Z).
106. T3:45–49, span A. IMPRECISE: commands are missing (see THE SWEEP).
   - Add: "in the first jq command, also `jq` over this session's transcript through a `while read` loop; `rm`/`rm -r` of the provisional set in scratch; `mkdir`, `mv` and `rm` keeping the checked set in `v1/`, and `make_raw13.sh` rebuilding the check raw; `fill_window13.sh`, which wrote the window request in the sessions' notes folder; `bash -n` of the build, fill and delta scripts".
107. T3:50. "one memory note". FAIL: there were two.
   - Put instead: "two memory notes (`cat` of one; `wc -l`, `tail` and `grep -o` of the other)".
108. T3:50–56, span B. IMPRECISE: commands are missing (see THE SWEEP).
   - Add: "`git show HEAD:RESULTS.md` into `sed -n` and `grep -n -E` (the quote style of the PI's words), with `grep -c -F` of the accepted entry; `git status --porcelain` of four named paths before the window too; `grep -n -E` of the gate script; `diff`, `LC_ALL=C tr -d` into `wc -c` and `shasum` of the values file".
109. T3:57–65. The after-commit list, the two `jq` passes over T, and one `awk`. CONFIRMED. The two records were indeed a user tool_result and an api-request-blob copy, equal by `cmp`.
110. T3:67–74. IMPRECISE.
   - Put instead: "two name-only `ls -1` of the root" and add "`wc -l` and `sed -n` of PROPOSAL-n's lines 155–163 through `fold`".
111. T3:76–81. IMPRECISE: `valence_core/m/stages.py` (lines 272–290, read at 23:21:00) is missing from the `sed -n` list. Add it.
112. T3:83–85. FAIL: the 22:55:47 command appended one line to the memory index (MEMORY.md, outside scratch) with `printf >>`, then ran `tail` and `wc -l`. The departures file's creation and the gate id file (22:55:13, by redirect) and `mkdir -p` (22:53:58) are also unnamed.
113. T3:87–88. The state checks. CONFIRMED.
114. T3:89–96. IMPRECISE. `--name-only` was run on d92500b only; 2ca24e8 got `--name-status`. Also missing: `wc -c` of the three memory notes (00:38:45, which Code's own running departures file had), and `cat` of the departures file and the gate id file (00:39:50).
115. T3:97–103. FAIL.
   - "twelve committed raws" should be fifteen: ans21b, ans22a, ans22b, ans23a, rt23a, rt21b, ans21c, ans20b, box, ans18c, mF3ans, the conditional ruling, gvrun, results/raw/2026-11-22_n-gver_spec.md and gtrun.
   - "four of these commands" in results/raw/ should be five: 00:46:44 also ran there.
   - A second narrow glob is undeclared: `2026-11-22_n-gver-*_design-to-code_answers.md`, run in results/raw/ (two names, no marker).
   - Also undeclared: a grep over the glob `valence_core/n/*.py` (16 names, no marker), and `wc -c` of one line of PROPOSAL-m.
116. T3:104–107. IMPRECISE. The `jq` fields also included isMeta. Also unnamed: `git ls-files` with a quoted glob under results/raw/ (`2026-11-23_n-campaign*`) into `wc -l`, and a `while read` loop.
117. T3:108–112. The brief's scrub, the assembly and the sweep. CONFIRMED. The view was written at 00:51:38, after the sweep command.
118. T3:113–114. "writes in scratch alone" for span D. CONFIRMED: redirects, `mkdir -p`, the zsh build, and file-tool Write and Edit, all under S.
119. T3:86–114, span D as a whole. IMPRECISE: the checks of the block draft at 00:50:45 are missing (`wc -l`, a width `grep`, a `grep -c` of local roots and ids, and `grep -o` of CP names into `sort -u`).
120. T3:116–117. No guard marker and no plain Q-F3 folder name in any argv. CONFIRMED: 0 hits in the 137 commands from A to E, and 0 in the file-tool paths.
121. T3:117–119, the outputs. IMPRECISE. Q-F3's short name was also printed by:
   - one `sed -n` of ans18c:32 (00:40:54);
   - the `git grep -c` (two file names that hold it, outside the folder);
   - five file-tool Reads (pruned-traversal-rule note at 22:39:43, ans23a at 22:51:22, the n-gtime-wiring note at 22:51:43 and 00:38:47, and the survey report at 00:39:25).
   - Add these.
122. T3:120–123, the survey's departures. IMPRECISE: item 4's "also used" is dropped. Add "`wc -l` of 15 named non-data files, `git log` with a commit date and bracketed `/usr/bin/grep` patterns".
123. T3:125–126, the gate id list. NOT CHECKABLE (plan). T shows the survey's id written to S/step4b/camp/gate_v15_new_ids.txt at 22:55:13, and the values-checker's id appended at 00:55:54, after this brief's hash.
124. T3:127–133, the commit by path, the home-prefix count and "Not pushed". NOT CHECKABLE (plan).

## THE SWEEP

These are the commands outside item 1's forms that T3 does not cover. A–D are as framed in the brief.

**Span A**
- 08:07:52: `jq` over T (tool results to the step-13 sweep's end, looking for Q-F3's plain name), with a `while read` loop of `jq` calls.
- 08:11:20, 08:12:46, 08:19:45: `bash -n` of the build, window-fill and delta scripts.
- 08:11:31: `rm` and `rm -r` in scratch.
- 08:12:46: `fill_window13.sh` wrote the window request into the sessions' notes folder; `grep -c` and `grep -n` of it.
- 08:18:30: `mkdir -p`, `mv` and `rm` in scratch, then `make_raw13.sh` rebuilding the check raw.

**Span B**
- 22:39:56 and 22:45:03 (plus 22:45:30): a second memory note, read with `wc -l`, `tail` and `grep -o`.
- 22:40:45: `git status --porcelain` of four named paths, before the window.
- 22:40:50: `git show HEAD:RESULTS.md` into `sed -n` and `grep -n -E`; `grep -c -F` of the accepted entry.
- 22:41:06: `grep -n -E` of the gate script.
- 22:41:30: `diff`, `LC_ALL=C tr -d`, `wc -c` and `shasum` on the values file.

**Span C**
- 22:52:20: a second `ls -1` of the root.
- 22:52:23: `wc -l`, `sed -n` and `fold` of PROPOSAL-n.
- 22:53:58: `mkdir -p` in scratch.
- 22:55:13: `printf >` and a `cat >` heredoc creating two scratch files.
- 22:55:47: `printf >>` to MEMORY.md, then `tail` and `wc -l`.
- 23:21:00: `sed -n` of `valence_core/m/stages.py`.

**Span D**
- 00:38:45: `wc -c` of three memory notes.
- 00:39:50: `cat` of two scratch files.
- 00:41:01: `wc -c` of one line of PROPOSAL-m.
- 00:44:32: `grep` over the glob `valence_core/n/*.py`.
- 00:45:29: `git ls-files` with a quoted glob under results/raw/ into `wc -l`, and a `while read` loop.
- 00:46:44: a fifth command with the working folder in results/raw/, holding a narrow glob there, plus `grep -c -i -F` of three named raws.
- 00:50:45: checks of the block draft.

**Not in T3's list at all:** file-tool writes outside scratch in spans A–C (Edits of memory notes and MEMORY.md at 08:13–08:21 and 22:45–22:50; a Write of a memory note at 22:55:43 and Edits at 23:22:48 and 23:24:13) and Reads of the shared notes. See Observation 10.

**Guard markers and the campaign folder's name in command text:** [0] markers and [0] plain names of the folder in all 137 commands (A–E). [0] in the file-tool paths. The only case-insensitive hit was the label "mF3ans" in a printed tag (00:40:54), which is not the folder name.

**@FINAL@: the 12 commands from 00:51:38 to 00:55:07, by kind**
- `jq` over the sweep's record file in scratch, with `sed` shortening paths, into a view file in scratch; `wc -l`, `cut` and `sed -n` of it.
- `sed -n` of the working tree's RESULTS.md (lines 24–161 and 105–150) into `grep -n -i -E` and `cut`.
- `cut`, `sed -n`, `grep -E` and `fold` views of the view file.
- Per-span counts by `grep -c`, and `jq` over the record file into bracketed `grep -c`.
- `wc -l` and `cat` of G-VER's seat values-check brief in scratch.
- A loop of `wc -l`, width `grep -v`/`grep -c` and `shasum` over the three texts; `rm` of spec_v1.md and `zsh build_spec.sh` rebuilding it; a `grep -c` of roots and ids in the entry; `tail -c 2 | od -c | head`.
- `grep -n -F` over T into `head`, `tail` and `cut`, then `sed -n` of the record into `jq -r` (type, content type, timestamp).
- `diff` of the list of record's items 1–5 between the survey brief and this brief (`sed -n` process substitutions); `wc -l`, `shasum` and a bracketed `grep -c` of this brief.
- None of these 12 holds a marker or the plain name. At 00:55:54, after this brief's hash and so outside the sweep, a `printf >>` added this checker's id to the gate's id file.

## OBSERVATIONS

1. **A new seat raw is in the tree and none of the texts accounts for it.** results/raw/2026-11-23_n-lock-v1_0-committed-close_design-to-code_answers.md is untracked (sha256 e07fba2c…eba9, 68 lines). It is the seat's second sitting of 2026-11-23, the first sitting of a new thread, reading 098218c's commit.
   - Its §2 gives "eight points … so that n-build's PINs can carry them", and its routing item 2 says "§2's eight points carried into the PINs".
   - Its §2 item 4, "Every pause comes to the seat on the excerpt, in its own raw", bears on Q3.
   - Its item 5, "Every end but PASS of any stage on the box goes to the seat and the PI", bears on Q6's extension.
   - Its item 8 sets the route: the spec raw first, then the block.
   - Its routing item 5 commits the raw with a close line on 098218c's entry. If that commit lands first, then "098218c, this block's parent" (T1:41) and "this raw's parent" (T2:20) become wrong, and the R: anchors shift (R:7842–7847).
   - The routing message's "no untracked file under results/raw" was checked before this raw existed.
   - T1:3, :8 and :16 frame the "next thread" as if the old thread were the last to read. Code's standing rule is to read new design-to-code raws before relaying.
2. **after13's output is owed and T3 does not place it.** 098218c's entry (R:100–101) says it goes "into the next entry's raw", and the new raw (§4, item 3) says "n-build's next entry's raw". T3 is n-build's next entry, but it neither carries that raw nor says where it will go.
3. **T1 contradicts itself on what the campaign writes.** CP2 says "writes only its root and its report" (T1:88–89), but CP9 (a) writes `data/n/reports/campaign_gver_stop.json`, and CP11 step 2 and CP10 name that file too.
4. **Q4 does not ask what follows a G-VER STOP at the start.** A G-VER-STOP report written there blocks any resume of that root (runner:330–331), and VERDICTS reads it as no-arm:gver-stop (anl:6710–6719). Q4 should ask what happens once such a STOP is cleared: a new root, the report moved aside, or a new lock version. The survey raised this in its 3.7.
5. **Q4 does not ask about a PI stop with no pause standing.** The schema permits it (schema.py:213, :1520–1524), and n:134's "a PI stop" is not tied to a pause, for example a decision on spend.
6. **Q7 does not cite the nearest text.** m:251's last clause reads: "after a restart the new BACKEND entry's identifier is the campaign's backend of record and supersedes the lock's field, which is not rewritten; the resume identity carries the new identifier". n:101 says m:251 is carried, yet this differs from LOCK:191–194's "new lock version".
7. **The "file in m's form under `data/n/reports/`" alternative in CP8 is internally mixed.** m's adjudication file sits beside the checkpoint in its ckpt folder and is tracked and -diff like it (stages.py:274–276), not under reports.
8. **Wording, T1:201.** "nothing in the driver but the `.gitignore` lines": the .gitignore is not part of the driver. Better: "nothing in the driver; the BUILD adds the `.gitignore` lines (CP10)".
9. **The G-VER precedent differs from G-TIME-n's.** The seat's rulings on G-VER's starred seven (5ad19de, 2026-11-22T14:27) were committed before G-VER's BUILD (2834c2d, 14:35), whose subject cites them. G-TIME-n's (b40ce59) came after its BUILD. The parallel T1 and T3 draw holds for block-before-BUILD only.
10. **File-tool writes outside scratch in spans A–C are unlisted.** T3 covers file tools only in span D. 098218c's entry, as the new seat raw §3 reads it, did list "memory files by name" and "the shared notes read and written".
11. **CP12's "three things together" needs an answer for CP9 (b).** At a G-VER STOP on a resume, the exit (6) and the report's end state (the last invocation's, for example PAUSE) disagree by design.
12. **The spec raw carries words a scan might flag.** §4 line 491 names Q-F3's folder by its short name ("the … exclusion"), and §3/§4 hold 2 marker-word lines. All are verbatim content and inert in a commit. Worth knowing if a staged-diff scan looks for these words.

## DEPARTURES (mine)

1. One `git ls-files -o -- results/raw` piped into `grep -c` (count 0). It used a narrow positive pathspec, not '.' with the exclusions. Names only were read, and only the count was printed.
2. Three redirects to /dev/null (one `diff -q`, two discarded `jq` passes). No file was written.
3. `sed` used as a filter and for line ranges, including one line of T taken by number. It is not among the named interpreters; noted for the seat to class.
4. The file-reading tool read one untracked raw in results/raw/ that no text cites (no marker in its name). `git status --porcelain` was scoped to that one named file, and `shasum` and `wc -l` were run on it.

Nothing else: no marker and no plain folder name in any argv; nothing under data/ read, listed, sized or timed; no listing or glob in S; no file written.
```
