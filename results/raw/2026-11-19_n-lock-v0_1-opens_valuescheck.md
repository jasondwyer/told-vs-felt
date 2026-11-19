# n — the OPENs block on LOCK-n v0.1's draft: the blind values-check, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the drafts of the block and its entry:
- T1, the block, `results/raw/2026-11-19_n-lock-v0_1-opens_code-to-design_STOP.md` here: `fc59dbc0…32bf` (129 lines);
- T2, the RESULTS.md entry: `c6adf0ba…9dd8` (24 lines), its values-check paragraph a placeholder.

**The checker's brief** (`1278fd4c…c7d0`, 66 lines, given to the checker as a file, with its sha256 to verify):
- named the texts and the sources: in Code's scratch, by name and sha256, the lock's draft (`c29fabed…c039`), the
  drafting survey's report and the coordinating session's routing of the draft; in the repository, PROPOSAL-n v0.2,
  ADDENDUM-n1, CLAUDE.md's rule 5, the seat's answers the block quotes, the schema, runner and analyzer code it cites,
  and RESULTS.md at `516b60f`;
- asked for every factual claim to be checked, the 18 holes and the OPENs' readings against the draft's, and whether
  the block chooses anywhere between an OPEN's readings, which it must not;
- barred any interpreter but `shasum`, any write, any network, any guard marker in an argv, anything under
  `data/mf3`, any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the
  named files and the brief itself; quoted the list of record v2's items 1–5, verbatim.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (207 lines, sha256
`8064426b…2e7a`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 87 items: 62 CONFIRMED, 9 IMPRECISE, 2 FAIL, 14 NOT CHECKABLE; and 14 observations. To the brief's
question, the checker found that the block chooses between no OPEN's readings.

block, verbatim in Code's scratch (`cefa9463…8c97`, 10 lines): "Send the five OPENs to the seat now, rather than at
step 10. Write a short code→design block, …, so that one sitting can rule on them with G-VEC's STOP (355e3a2) …";
"One values-check pass, then ask me for a commit window."
values-check pass, then ask me for a commit window."

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

- **The FAILs:** 58, rule 5(f)(iv) quoted as "below dose 0.20"; 62, R-L1 gives n's part of the box line as the draft
  fills it, "n on H100 SXM pod `emw1e4embiwe9b`, identifier `4ed3f2c70fe8afbf` (`d5d08fa`)", with n's own
  identifier, `8264f719efd347a9`, in the next bullet.
- **The IMPRECISE items,** each applied in the checker's words or near them: 20 (OPEN 1 (a)'s construction marked as
  Code's), 21 (its changes: both seat sentences and the schema's docstring), 29 (OPEN 2 (a)'s changes: G-READ-n's fits
  in no cap the build computes, and the crashed invocation's load), 39 (`check_stage_identity` cited), 46 (OPEN 4
  (a): the interval varies on the S-span arms, N1-P's 39 on all 160), 59 (OPEN 5 (b)'s second branch in full), 65
  (R-L1's reading the survey's, adopted), 66 (PIN-n-26's register line cited) and 78 (the entry's list of what the
  answers change).
- **The NOT CHECKABLE items** stand: Code's assessments, readings and plans, and the routing (item 3, settled by the
  routing's text above).
- **The observations:** 1 (n:159's order cited in OPEN 1), 2 (the report's and G-READ-n's records of the hashes), 3
  (box:31 in OPEN 2), 5 (the routing's hole list in OPEN 3), 6 (the meaning of "cell", as a note for the ruling), 7
  (OPEN 4 (a)'s declaration through both hashes, or the 160 intervals), 8 (OPEN 5 (b)'s gate in a form the seat names,
  n:48's valence gate beside it), 9 (N2-S and N2-C at `f0.20`; "dose label" for "keys"), 10 ("the route line"), 12
  (the survey's departures in this entry, for this sitting), 13 (§1's holes grouped by step, four abridged) and 14
  (the routing, above) are applied. Observations 4 (the draft's list of the BUILD's flags) and 11 (three PI routing
  raws missing from the draft's sources) go to the draft's next pass.

## 2. The text changed after the check, and the edits checked by tool

- **The text changed after the check** by the dispositions above, and in T2 by its values-check paragraph, which
  replaces the placeholder, and its fuller departures.
- **The edits, checked by tool:** a fixed-string count over each text unwrapped, for each disposition's new wording
  and each removed wording's absence: 27 of 27. Each new quotation was found in its source by `git grep -F`.
- **The finals:** the block `6c02b096…fdcf` (154 lines); the entry `5dea128b…cd77` (41 lines).

## 3. The report as returned

The brief hash-checked at 1278fd4c…c7d0 (66 lines). So did T1 (fc59dbc0…32bf, 129 lines), T2 (c6adf0ba…9dd8, 24 lines), the draft (c29fabed…c039, 688 lines), the survey report (9c16f9f3…5985) and the routing (9fc5cd6d…b7d0). I abbreviated each hash by tool. HEAD is 516b60f. All 11 named repository sources are tracked and clean there (`git rev-parse HEAD:<path>` equals `git hash-object <path>`). I wrote no file.

ITEMS

T1
1. T1:3, "PI date 2026-11-19." NOT CHECKABLE: the PI's calendar. It matches this session's date.
2. T1:3–4, `355e3a2` is G-VEC's STOP. CONFIRMED: `git log -1 --format='%h %s' 355e3a2` gives "n -- G-VEC on n's box (n v0.2 s8 step 7): … STOPPED at the R check …".
3. T1:3–4, "For the seat, through the coordinating session, in the sitting that rules on G-VEC's STOP". NOT CHECKABLE (routing). S/step4b/lock/routing_lock.txt routes the draft and one values-check and names no block (obs. 14).
4. T1:4, "Code chooses nothing." CONFIRMED (item 72).
5. T1:4–5, the draft stays uncommitted and "PROPOSAL-n v0.2 §8 step 10 commits LOCK-n v0.1". CONFIRMED: n:154 is "## §8 Code's block, in order"; n:159 has "10. Commit LOCK-n v0.1."; routing_lock.txt:15 has "No commit until the seat has the full v0.1 (step 10)".
6. T1:5, anchors at `516b60f`. CONFIRMED: `git rev-parse HEAD` gives 516b60f3…, and RESULTS.md is clean.
7. T1:9, the draft's sha256 `c29fabed…c039`, 688 lines, in Code's scratch. CONFIRMED: shasum, and `wc -l` gives 688.
8. T1:9–10, "It carries n:117's list and the items the coordinating session added, every fixed value cited to its source". CONFIRMED:
   - draft:41–57 carry n:117's list, and draft:59–65 the coordinating session's items;
   - "every fixed value cited" is the draft's own statement (draft:6–7). I spot-checked §§3, 6, 11, 16, 17, 20 and 21, not line by line.
9. T1:10–11, "18 holes each naming the step that fills it … and five OPENs". CONFIRMED: `grep -c '^- \*\*HOLE\*\*'` gives 18, each "— filled by …"; `grep -c '^- \*\*OPEN\*\*'` gives 5.
10. T1:11, "where two texts disagree or a word is undefined". CONFIRMED. OPEN 2 is the undefined word. OPENs 3–5 each set two texts against each other. OPEN 1 sets A-n1:54 and ans16b:41 against n:159's order (obs. 1).
11. T1:12–13, OPENs 4 and 5 "flagged at the n package's BUILD and unruled since (R:3717–3719)". CONFIRMED:
   - R:3540 opens the entry "n package — BUILD …";
   - R:3707 heads the list "Open:";
   - R:3717–3718 is the retention flag, and R:3719 the N2-E flag;
   - `git grep -l -i` for retention / 5(f)(iii) / 5(f)(iv) over the tree, with item 3's pathspec plus the mf3 exclusion, finds no seat answer, ruling or routing raw dated 2026-11-15 to 11-19;
   - RESULTS.md at 516b60f has no match before R:3717.
12. T1:12–13, the quotations (iii) "declared and held fixed within a cell" and (iv) "below dose 0.20 for the reward axis". CONFIRMED: CLAUDE.md:297–299.
13. T1:13–14, "They bear on the campaign's design, not only on the lock's text." NOT CHECKABLE: Code's assessment. It is consistent with T1's (b) readings.
14. T1:15, Q1–Q7 in §4. CONFIRMED: T1:125–127.
15. T1:19–37, the 18 holes, each with its step "as the draft writes it". CONFIRMED. They match the draft's HOLE bullets one to one (draft:183–187, 212–214, 280–281, 321, 327, 451, 466, 499, 559, 625–626), and every step is the draft's. They are grouped by step, and four are abridged (obs. 13).
16. T1:41, OPEN 1 is "the draft's §6". CONFIRMED: draft:282.
17. T1:42–44, the A-n1:54 (§6.2) quotation. CONFIRMED.
18. T1:44–45, the ans16b:41 quotation "The lock pins the per-cell hash lists." CONFIRMED.
19. T1:45–46, the hashes exist only once the cells are written, and each cell file records them as `capture_sha256` (schema.py:438–440). CONFIRMED: schema.py:438–440 reads "sha256 of that layer's written rows [0, capture_rows) … when this file was written".
20. T1:47–48, OPEN 1 (a)'s reading. IMPRECISE.
   - Evidence: the draft's (a) (draft:282–284) is only "a value no pre-campaign lock can hold". T1 adds a resolution without marking it as Code's.
   - Its "committed cell files" is supported: n:159 step 14 says "raws and checkpoints committed before the pod stops", and schema.py:129–130 puts the cell files in the stage's checkpoint directory.
   - Instead: "*(a)* No pre-campaign lock can hold the lists (the draft's reading). Code's construction of it: the lock states where they are recorded, the campaign's committed cell files, and A-n1:54's "the lock pins" is read, or amended, as that record."
21. T1:48–49, OPEN 1 (a)'s "*Changes:* A-n1's sentence (the seat's) and the lock's text; nothing in the build." IMPRECISE.
   - Evidence: ans16b:41, also the seat's, carries the same sentence, and schema.py:85–86's docstring repeats "the lock pins the per-cell hash lists".
   - Instead: "*Changes:* A-n1:54's sentence and ans16b:41's (both the seat's) and the lock's text; in the build, only the docstring at schema.py:85–86, which repeats "the lock pins the per-cell hash lists"."
22. T1:50–52, OPEN 1 (b), and "the lock's text only; nothing in the build". CONFIRMED: it matches draft:284–286, and the build already writes that form (schema.py:438–440). "Copied … before the pod stops" is A-n1:54's.
23. T1:54, OPEN 2 is "the draft's §11. No text read defines the word." CONFIRMED: draft:390. `git grep -i` for "budget's split", "split of the budget" and "budget split" over the tree, with the pathspec, matches n:117 only.
24. T1:55, the n:117 quotation. CONFIRMED.
25. T1:55–58, n:101's §2.7, "planning values", "G-TIME-n governs", the forwards "≈ 0.9–1.8 h; the two extractions … minutes; …; cold loads 130–200 s each", and "Pod budget proposed: 8 h for N-pod, the cap set by the PI at LOCK-n v1.0". CONFIRMED. The ellipsis stands for "(BK's 544 passages; our 1,344 contexts)".
26. T1:58–59, the ans16b:50 quotation "the lock says: the cap counts …". CONFIRMED; "the same raw" is ans16b.
27. T1:59–60, A-n1:56's "counted in the cap where it runs on the box". CONFIRMED.
28. T1:61–62, OPEN 2 (a)'s reading. CONFIRMED: draft:390–392.
29. T1:62–63, "the build already counts this way (schema.py:192–195; runner.py:60–64)". IMPRECISE.
   - Evidence: true for the reads' and re-computations' model time, with loads reported beside the cap. Reading (a) also puts G-READ-n's fits inside the cap, but they are in no cap the build computes:
     - `used_ms` is "the sum of the stage's records' duration_ms" (schema.py:1196);
     - G-READ-n's artifact has no timing field (schema.py:1217–1222);
     - this is the BUILD's open flag at R:3734–3735: "G-READ-n's timing and cap clause are for its stage and the lock".
   - Also, `loads_ms` lacks a crashed invocation's load (R:3728–3729; runner.py:62–64).
   - Instead: "*Changes:* the lock states the clause. The build already counts the reads' and re-computations' model time in the cap and reports each reporting invocation's load beside it (schema.py:192–195; runner.py:60–64); G-READ-n's fits are in no cap the build computes (schema.py:1217–1222; the BUILD's open flag, R:3734–3735), and a crashed invocation's load is absent from `loads_ms` (R:3728–3729)."
30. T1:64–65, OPEN 2 (b), with G-TIME-n's projections revising it at v1.0. CONFIRMED: draft:393–395; n:101; n:120 ("Projections, the cap"); box:31.
31. T1:66, "The two readings do not exclude each other; the seat may name both." NOT CHECKABLE: Code's reading. It adds an option and chooses neither reading.
32. T1:68, OPEN 3 is "the draft's §16". CONFIRMED: draft:500.
33. T1:69–71, the ans19:64 quotation. CONFIRMED. The line lies in ans19 §5 (:59–65).
34. T1:71–72, the n:159 (§8) quotation, steps 10–13. CONFIRMED.
35. T1:72, n:120's "LOCK-n v1.0. Projections, the cap, D_n, …". CONFIRMED.
36. T1:73–74, schema.py:448's `lock_sha256` "the lock in force; null only at backend-ext (before LOCK-n v0.1)". CONFIRMED.
37. T1:74, ans19 §3 (R14, :50), "binds at G-TIME-n, whose identity carries the lock's C". CONFIRMED; §3 is :47–52.
38. T1:75–76, OPEN 3 (a), "so G-TIME-n runs before step 10". CONFIRMED: draft:500–501, and the consequence follows from n:159.
39. T1:76–77, "which the schema refuses outside backend-ext (schema.py:448)". IMPRECISE.
   - Evidence: :448 gives the field's meaning. The refusal is in `check_stage_identity`, schema.py:839–842 ("is null exactly at backend-ext").
   - Instead: "which the schema refuses outside backend-ext (schema.py:448; `check_stage_identity`, schema.py:839–842)".
40. T1:78–80, OPEN 3 (b): "its identity carrying v0.1's sha256 and C", and the lock's text only. CONFIRMED:
   - draft:501–504;
   - schema.py:448, 474–475 and 839–842: the `time` stage needs a non-null lock and bound;
   - ans19:50.
41. T1:82, OPEN 4 is "the draft's §21". CONFIRMED: draft:610.
42. T1:83–84, the n:79 (§2.2) quotation. CONFIRMED.
43. T1:84–85, the rule 5(f)(iii) quotation. CONFIRMED: CLAUDE.md:297–298.
44. T1:85–89, the schema.py:64–68 quotation. CONFIRMED, verbatim.
45. T1:89, "The BUILD's flag: R:3717–3718." CONFIRMED.
46. T1:90–91, OPEN 4 (a): "each session's interval is fixed by its skeleton, the same at every dose and on every S-span arm, and varies across a cell's sessions". IMPRECISE.
   - Evidence: N1-P's interval is "39 tokens on all 160" (schema.py:65–66), so it varies only on the S-span arms. The "same at every dose …" clause is schema.py:65's, not n:79's.
   - Instead: "*(a)* n:79's: each session's interval is fixed by its skeleton (and its arm's span set, schema.py:64–65), the same at every dose and on every S-span arm; on the S-span arms it varies across a cell's sessions, while N1-P's is 39 tokens on all 160 (schema.py:65–66). Code's construction of it: the lock declares …"
47. T1:91–93, "The lock declares the intervals by the session set's hash, and the seat rules …". NOT CHECKABLE: Code's construction. It is not in draft:610–611 (obs. 7).
48. T1:92–93, (a)'s "the lock's text and a ruling; nothing in the build". CONFIRMED: the per-read interval is already recorded (schema.py:63–64, 361).
49. T1:94, OPEN 4 (b) as rule 5(f)(iii)'s reading. CONFIRMED: draft:611–612.
50. T1:94–96, (b)'s changes and means. NOT CHECKABLE: Code's plan. It is consistent with the read position being fixed at `seq_len - 1` (schema.py:34, 367).
51. T1:98, OPEN 5 is "the draft's §21". CONFIRMED: draft:614.
52. T1:99–100, the n:81 (§2.3) quotation. CONFIRMED.
53. T1:100–101, the n:48 (B3) quotation. CONFIRMED.
54. T1:101–102, the rule 5(f)(iv) quotation. CONFIRMED: CLAUDE.md:298–300.
55. T1:102, "The BUILD's flag: R:3719." CONFIRMED.
56. T1:103, (a)'s "never above 0.20", and N2-E reads at f = 0.10 and 0.20 as built, with no 5(d) gate. CONFIRMED: n:81; schema.py:289–290 and 301; STAGES at schema.py:251 has no gate stage.
57. T1:103–104, (a)'s "nothing in the build". CONFIRMED: the build already reads `f0.20`.
58. T1:105, '*(b)* The rule's: "below 0.20".' FAIL.
   - Evidence: the quotation is not in CLAUDE.md (`grep 'below 0\.20'` finds no match). CLAUDE.md:299 reads "below dose 0.20".
   - Instead: '*(b)* The rule's: "below dose 0.20".'
59. T1:105–107, (b)'s second branch, "its dose points, keys and read plan rebuilt, and that point no longer d_20". IMPRECISE.
   - Evidence: it leaves out what the texts and the code tie to f = 0.20:
     - n §5's decision point, n:140 "N2 (state), at f = 0.20 (f = 0.10 beside)", which A-n1:48 keeps;
     - G-READ-n's `span_reward` f0.20 result and its comparator at +d_20 (schema.py:218–219, 224–226);
     - the analyzer's f0.20 label (n_analyze.py:5730).
   - "Keys" is ambiguous (obs. 9).
   - Instead: "or N2-E's top point below 0.20: its dose label and value (schema.py:289–293, 301), the read plan, G-READ-n's `span_reward` f0.20 result and its comparator at +d_20 (schema.py:218–219, 224–226) and the analyzer's f0.20 label (n_analyze.py:5730) rebuilt; n §5's "N2 (state), at f = 0.20 (f = 0.10 beside)" (n:140; A-n1:48) amended; and that point no longer d_20 (n:48's "f = 0.20 (d_20)")."
60. T1:105–106, (b)'s first branch, "as a new stage before the campaign". NOT CHECKABLE: Code's plan (obs. 8).
61. T1:111–113, the seat's box answers of 2026-11-18 (:30) add the line, and the quotation. CONFIRMED: box:30 verbatim; the raw's header has "PI date 2026-11-18".
62. T1:113–115, "The draft fills n's part with the H100 SXM pod `emw1e4embiwe9b`, the backend identifier `8264f719efd347a9` bridged to the characterization's `4ed3f2c70fe8afbf`". FAIL.
   - Evidence: the draft's filled line (draft:512–513) is "n on H100 SXM pod `emw1e4embiwe9b`, identifier `4ed3f2c70fe8afbf` (`d5d08fa`)". `8264f719efd347a9` is in the next bullet, box:27 (draft:518–520).
   - The identifiers themselves are right: R:247–249, R:1225–1226, R:2882–2886. `d5d08fa` is "BACKEND -- characterization (2026-11-18) for n's box, pod emw1e4embiwe9b" (git log).
   - Instead: "The draft fills n's part as "n on H100 SXM pod `emw1e4embiwe9b`, identifier `4ed3f2c70fe8afbf` (`d5d08fa`)", the characterization's identifier and entry, and keeps p's as written; n's own identifier under its 4,096 window, `8264f719efd347a9`, bridged by R6 to `4ed3f2c70fe8afbf`, is in the next bullet (box:27)."
63. T1:115, "keeps p's as written". CONFIRMED: draft:512–513 matches box:30's p part.
64. T1:116, "Pod ids are already in committed texts throughout." CONFIRMED. In RESULTS.md at 516b60f, `emw1e4embiwe9b` is at R:209, 247, 1200, 1225, 2883 and more, and `m43y3deb1gq3rp` at R:2911, 3178, 6507 and more. Both are also in box:30.
65. T1:116–117, "*Code's reading:* the draft's bar on session ids covers …". IMPRECISE.
   - Evidence: the draft states no bar (`grep -i` for "session id", "session ids" and "pod id" finds none). The bar is the drafting brief's, and the reading is the survey's (survey_report:7, :65).
   - Instead: "*Code's reading* (the drafting survey's, adopted): the drafting brief's bar on session ids covers the harness's session ids and BK's per-session ids, not pod ids."
66. T1:118, PIN-n-26: "Code's form for the lock is two whole lines". IMPRECISE (no anchor).
   - Evidence: the words are in PIN-n-26's register line, R:5322. The analyzer's own PIN-n-26 text (n_analyze.py:2443–2445) ends "(Code's form for the lock)".
   - Instead: 'PIN-n-26 (its register line, R:5322): "Code's form for the lock is two whole lines"'.
67. T1:118–120, the ans16g:50 quotation. CONFIRMED.
68. T1:120, v0.1's lines `lock: LOCK-n v0.1` and `direction of record: Route B`. CONFIRMED as the draft's lines (draft:582–585; the survey's reading, survey_report:66). Route B is R:13808–13809's. The reading itself is not checkable.
69. T1:120–121, `verdicts` checks `lock: LOCK-n v1.0` and reads the route from the second line, so v1.0 writes its own. CONFIRMED: n_analyze.py:2443–2445, 5727 (`LOCK_V10_LINE`) and 5734–5745 (`lock_route`, "so no earlier lock passes for it"); obs. 10.
70. T1:125–127, Q1–Q5 cover OPENs 1–5 and Q6/Q7 cover R-L1/R-L2. CONFIRMED.
71. T1:129, "Nothing ran for this block. …" NOT CHECKABLE.
72. T1 overall: does it choose between an OPEN's readings? CONFIRMED that it does not. Every OPEN gives (a) and (b) with their changes, and Q1–Q5 ask "(a), (b), or another reading". OPEN 2's "the seat may name both" adds an option. OPEN 3's texts lean to (b) in number, which is presentation, not a choice.

T2
73. T2:1–3, the title, and `355e3a2` is G-VEC's STOP. CONFIRMED: it matches T1:1, and git log.
74. T2:2–3, "committed by path … on the coordinating session's routing". NOT CHECKABLE (obs. 14).
75. T2:3, "The draft itself stays uncommitted until PROPOSAL-n v0.2 §8 step 10." CONFIRMED: n:159; routing_lock.txt:15.
76. T2:5, the block's path and link. CONFIRMED: it is the brief's commit path, and the link text and target agree.
77. T2:6–7, the draft's hash `c29fabed…c039`, 688 lines, and its 18 holes with their steps. CONFIRMED: items 7, 9 and 15.
78. T2:7–8, "what each answer changes in the lock or the build". IMPRECISE.
   - Evidence: T1's changes also touch:
     - the seat's texts (OPEN 1 (a));
     - the step order (OPEN 3 (a));
     - the design (OPEN 4 (b));
     - a new stage (OPEN 5 (b)).
   - Instead: "what each answer changes in the lock, the texts, the step order, the design or the build".
79. T2:8–9, the two readings (pod ids in the box line; the lock's two lines in PIN-n-26's form), Q1–Q7, and "Code chooses nothing". CONFIRMED.
80. T2:10–12, OPENs 4 and 5, flagged at the BUILD and unruled since, with the two quotations. CONFIRMED: items 11–12. The last sentence is item 13's.
81. T2:13–14, "one drafting-survey subagent from n:117's list, the coordinating session's routing, and every seat answer and addendum that routes an item into LOCK-n v0.1". CONFIRMED:
   - survey_report:1 says "I wrote one file";
   - the draft's Sources (draft:650–688) hold every n seat answer or ruling raw dated 2026-11-15 to 11-19 (`git ls-files`, filtered);
   - they also hold both addenda, and every n seat raw that `git grep -l` finds naming "LOCK-n v0.1" or "LOCK v0.1";
   - the routings are a separate point (obs. 11).
82. T2:14–15, "every fixed value cited, and nothing chosen where texts disagree". CONFIRMED: draft:5–9, spot-checked as in item 8.
83. T2:15, "Its sources and the survey's departures go to the lock's entry at step 10." NOT CHECKABLE: a plan (obs. 12).
84. T2:16–17, Code's one `jq` read, with the routing "given verbatim to the survey". NOT CHECKABLE: Code's own command. The survey hash-checked the routing file at 9fc5cd6d…b7d0, 16 lines (survey_report:1). That is the file's sha256 and line count here.
85. T2:20, "Committed by path: the block, its values-check raw and this entry." NOT CHECKABLE: a plan.
86. T2:22, the home-folder prefix count of 0, "Nothing ran on a model", "Not pushed". NOT CHECKABLE until commit time. Both drafts hold no "/Users" and no "/private" (`grep -c` gives 0 and 0), and no clock time.
87. T2:23, "Next: …". NOT CHECKABLE: a plan.

TOTALS: 87 items.
- CONFIRMED 62.
- IMPRECISE 9: items 20, 21, 29, 39, 46, 59, 65, 66, 78.
- FAIL 2: items 58 and 62.
- NOT CHECKABLE 14.

OBSERVATIONS
1. OPEN 1's texts leave out what A-n1:54 is set against: n:159's order. That order puts LOCK-n v0.1 at step 10 and v1.0 at step 13, both before the campaign at step 14, whose "raws and checkpoints [are] committed before the pod stops". That is what makes "no pre-campaign lock" true and the cell files committed. Cite it beside A-n1:54.
2. OPEN 1: after the campaign, the build also records every cell's per-layer `capture_sha256` in two other places:
   - the stage report's `cells` (schema.py:1148: "{json_sha256, capture_sha256, records}, every cell file");
   - G-READ-n's artifact, `campaign.cells` (schema.py:1226).
   Either reading could name them beside the cell files.
3. OPEN 2's texts leave out box:31, which the draft quotes (draft:382–384): "n §2.7's 8 h proposal was at the A100's rate; G-TIME-n projects on the new box". It bears on (b): n:101's split is an A100-rate plan (n:101 names "A100-SXM4-80GB").
4. The draft's list of the BUILD's open flags (draft:604–609) leaves out "G-READ-n's fits in the cap" (R:3734–3735). That is the flag that bears on OPEN 2 (a).
5. OPEN 3: the draft's (a) also rests on the routing's hole list (S/step4b/lock/routing_lock.txt:14, "Mark as holes … G-TIME-n's figures"). T1 gives only ans19:64.
6. OPEN 4: schema.py:64 says "Cell" in the schema "names a file grouping", one per (arm, direction, dose point) (schema.py:129). 5(f)(iii)'s "within a cell" may mean that grouping or a design condition. Under the first, every S-span cell holds varying intervals and N1-P's cells hold one. The ruling may need to say which.
7. OPEN 4 (a)'s "by the session set's hash": the interval is a token count, "read_position - (last span end - 1)" (schema.py:361). It is computed from each read's ids and spans, which the lock pins through MANIFEST.json's sha256 (draft §1) as well as through the session set's hash. The lock could name both, or list the 160 intervals per span kind.
8. OPEN 5 (b), first branch: n:48 already declares one 5(d) gate, the valence direction's: "G-LEAK-n plus G-CAL-n's coherence hurdle, declared here (the seat's reading; the PI may require more)". "A new stage before the campaign" is one form among others; the seat names the form.
9. OPEN 5 (b), second branch: moving only N2-E's top point leaves N2-S and N2-C at `f0.20` (schema.py:302–303), so the guards would no longer be read at N2-E's point. The seat may want to say whether they move too. Separately, "keys" can be read as n:117's "the keys", the keyed streams (draft §5), none of which is per dose; "dose labels" says what moves.
10. R-L2: `lock_route` (n_analyze.py:5734–5745) accepts the two lines anywhere in the lock, with exactly one route line. "The second line" is the second of PIN-n-26's two lines, not a position; "the route line" would be exact.
11. Three PI routing raws also route items into LOCK-n v0.1, and the draft's Sources hold none of them (only rt19):
   - results/raw/2026-11-16_second-sitting_pi-routing.md:32;
   - results/raw/2026-11-18_third-sitting_pi-routing.md:19;
   - results/raw/2026-11-18_fourth-sitting_pi-routing.md:15–16.
   T2's "every seat answer and addendum" still holds, because these are routings and their items are the seat's answers as adopted.
12. The survey's own departures are held for step 10 (T1:129, T2:15). Per survey_report:69–70, they are two greps with a guard-marker path in their argv, and one `git grep` with a folder pathspec and no exclusions. This commit is the first that rests on the survey's work, so the seat may want them classed at this sitting. Separately, survey_report:1 abbreviates its brief's hash as "59088ee4…3b9", with 3 trailing characters instead of 4; re-abbreviate it by tool if it is quoted at step 10.
13. T1 §1 orders the holes by the step that fills them. The capture band (draft §6) moves up among G-VEC's holes, and G-TIME-n's (draft §16) moves to the end. Four are abridged: "as G-VEC records them", "(gvec.json's `of_record`, …)", "(31 or 32 layers)" and "(pending)". "Grouped by the step that fills it" would say so.
14. The routing basis for T1:3–4 and T2:2–3: the only routing among the sources is about the draft. It asks for one values-check "when the holes are few" and says "No commit until the seat has the full v0.1 (step 10)". It does not route a STOP block or a commit of one; if a later message does, the entry could name it. This check is not that routed values-check of the draft: it read the draft only where T1 cites it.

DEPARTURES
Barred:
- One pipeline ran `awk -F: '$1>3400 && $1<3800'` on the output of `git show 516b60f:RESULTS.md | /usr/bin/grep -n '^- 2026-'`. awk is an interpreter the brief bars. Its output went to `head -0`, which refused its argument, so nothing awk produced was printed. I redid the step with `sed -n` and grep. The same command line sent another grep's output to the null device; no file was written.

Possibly barred:
- Three `git log -1 --format='%h %s' <commit>` runs (d5d08fa, 355e3a2, 7ab4d2f) had no item-3 pathspec. They printed ids and subjects only, which item 1 permits over any path. I read them as outside "every git command over the tree", but the seat may class them otherwise.

Not barred as I read the rules; for the seat to class:
- Text filters, used throughout: `sed -n` to print lines, `cut`, `sort`, `head`, `wc -l` and /usr/bin/grep.
- `git grep` content searches over the tree, always with item 3's pathspec plus the mf3 exclusion:
  - for retention and 5(f)(iii)/(iv);
  - for "f = 0.20", "held fixed" and the flags' wording;
  - for "LOCK-n v0.1" and "LOCK v0.1";
  - for "budget's split" and similar wording. One of these searches printed matched lines from raws outside the named sources, including p's raws and the analyzer's pin-move raws.
- One `git ls-files`, with `.` plus the exclusions, filtered to November seat raws; it printed names only.
- Reads beyond the named sources or lines:
  - three PI routing raws, grepped;
  - one grep of results/raw/2026-11-06_ganl-f3_design-to-code_answers.md;
  - RESULTS.md at 516b60f beyond the named anchors (3690–3750, 205–212, 244–250, 1222–1238, 2880–2887, 2962–2972, 5228–5238, 5318–5326, 13806–13810, and greps);
  - PROPOSAL-n's headings and :132–145 and :154;
  - ADDENDUM-n1's head and :20–52;
  - CLAUDE.md:270–302;
  - schema.py beyond the named lines;
  - runner.py:1–75;
  - n_analyze.py greps, :2440–2447 and :5724–5748;
  - the answer raws' heads, ans19's headings, and box:27 and box:31.

Otherwise:
- No guard marker was in any argv.
- I ran no whole-tree `git status`.
- Nothing under data/mf3, data/*/ckpt or data/*/reports was read, listed, sized or timed.
- In S, I read only the brief and the five named files, by name, and grepped only single named files.
- I wrote nothing and used no network.
