# Values-check of the BUILD (F3) pre-build STOP block and its entry (before push)

*Code's raw. §1 is a blind values-checker's report, run as a subagent of this session (2026-11-06 UTC) over the first
drafts in the local commit `4574b9e`. It was given the sources, not Code's conclusions. It is copied verbatim. Its line
numbers refer to those drafts. §2 gives Code's disposition of each item. Each was re-verified at source before it was
applied, and the corrected block and entry replace the drafts in the commit that is pushed.*

## 1. The checker's report (verbatim)

# Values-check: the F3 pre-build STOP block and its RESULTS entry (HEAD `4574b9e`)

**Texts checked**
- **B**: `results/raw/2026-11-06_f3-build_code-to-design_prebuild.md`, cited as B:line.
- **R**: RESULTS.md:24–47, the entry dated 2026-11-06 that begins "m package — BUILD (F3)", cited as R:line.

**How they were checked.** Read-only, against the tree at HEAD `4574b9e`. No tracked file is modified, and HEAD's `valence_core/m/*.py` blobs match the working tree. Recomputed:
- `package_sha256`, by resume.py:296–328's formula, over the working tree and over HEAD's blobs. Both give `5f646db6e82c…d771` (18 files).
- The sha256 of the proposal, the addendum, the analyzer, the schedules' manifest, R1 and R2.
- The m modules the analyzer loads. These were found by importing its module-level set, then `stages`, in the jlens venv (`-I -B`).

Seat rulings were read in `results/raw/*design-to-code*`, LOCK-m-F0.md and RESULTS.md. Code's three scratch maps (`f3build/maps/{spec,code,records}.md`) were used only to check the counts that B attributes to them.

## Result

**128 claims checked: 2 FAIL, 14 IMPRECISE (one of them occurs in both texts), 1 note on a seat quote, and 3 claims not verifiable from the listed sources. All other claims are verified.**

---

## FAIL

**F1. R:28–29** (the same sentence is in `4574b9e`'s commit message): "Whichever lands second, the F3 code or an OLMo lock, makes the other's stages refuse until a lock revision names the new hash."
- **What refuses a stage.** `licence_problems` (stages.py:530–608) does it in two steps:
  - (e) it compares the recomputed `resume.package_sha256()` with identity_extra's `package_sha256`;
  - (f) it requires the committed lock text to name that value.
- **A lock cannot move the hash.** A lock commit changes no `valence_core/m/*.py` byte, so it cannot move `package_sha256`.
- **The OLMo-lock-second order refuses nothing.** If the F3 code lands first and an OLMo lock second, the lock names the current hash, which already includes F3.
- **Only a package edit after a lock makes stages refuse.** Both of B's own examples for (ii) are in the order "F3 code second, OLMo stages refuse" (B:46–47: "an OLMo lock committed before the F3 code, or the F3 code merged after OLMo stages are licensed").
- **The OLMo side could make Q-F3's stages refuse only by editing the package** after LOCK-m-F3 names its hash (see I4). A lock cannot do it.
- **Suggested:** "An OLMo lock committed before the F3 code makes the OLMo stages refuse once the F3 code lands, until a lock revision names the new hash."

**F2. B:113** (R:37 inherits the list): "#87 and #116 offer "the A1, A2 and A3 sessions' forced rounds reported beside"".
- **#87 offers no fix text.** #87 (`results/raw/2026-10-06_m-v1.11_step3_notes.md:97`, D8C2.104) reads in full: "PARTIAL, as D8C2.70. '@free' is still printed on a contrast session (now `excluded@free`). G-TIME-F3 (m:293) and G-F3 (m:297) still report contrast sessions without the forced-round scope. Weak channel, no tag."
- **The full checker and refuter notes have none either** (`2026-10-06_m-v1.11_referent_check.txt:15934–15960`).
- **The quoted words are #116's alone** (step3_notes.md:126: "Fix: 'the A1, A2 and A3 sessions' forced rounds reported beside', and 'over the 16 sham sessions and the contrast sessions' forced rounds'").
- **Suggested:** "#87 notes that m:293 and m:297 lack the forced-round scope; #116 offers '…'".

---

## IMPRECISE

**I1. B:44–45 and B:62: consequence (i), "G-SHAPE-F0 re-runs first (R1 D3)".** B treats it as following from any placement that moves `package_sha256`, and (B) inherits it ("so the same consequences").
- **What D3 says.** R1 D3 (`2026-10-10_m-design-to-code_pre-LOCK-v0.1.md:94`): "G-SHAPE-F0's sources map is compared with the lock's tree (PIN-S10). `stages.py` is not in its scoring-stack map, so the D2 edit does not re-run it and the lock states that diff; any other difference re-runs G-SHAPE-F0 first."
- **The trigger is the 28-file sources map, not the hash.** PIN-S10 (gshape.py:233–236) and LOCK-m-F0:2400 tie the re-run to the sources map (`SCORING_STACK_FILES` + `TOOLING_FILES`). The D2 edit moved the package without a re-run.
- **How each option falls under it:**
  - (A) triggers it, because scaffold, runner_qwen, audit, keys and banner are in the map.
  - (B) triggers it only if its "small edits" touch a map file.
  - New modules, and edits to resume, readrule, bars or stages, do not trigger it.
- **B states the rule correctly elsewhere**, at B:26–27.
- **The record is not uniform.** The step-10 read's Q5 (`…G-TIME-F0_read.md:51`) says loosely that binding the snapshot in stages.py "moves `package_sha256` and re-runs G-SHAPE-F0". But B cites D3, whose words exclude stages.py.

**I2. B:46–47 (ii): "Whichever lands second makes the other's stages refuse".** The lead sentence is symmetric, but its two examples are the same order (F3 code second, OLMo stages refuse). See F1. Suggested fix: state the one direction.

**I3. B:50–51 (iv).** B lists it as a consequence of placing F3 in `valence_core/m`, so by B:59–62 (C) appears to avoid it.
- **The embedded shas are right.** `Q-F0_VERDICTS.json` carries `analyzer_sha256` 655e0f7f…, `package_sha256` 5f646db6… and `closure_sha256` a3bc7bb9…. `Q-F0_secondary.json` carries none.
- **The analyzer field differs under every placement, (C) included.** G-ANL-F3 extends `m_analyze.py` in place (B:88; A-m1 §2.5; m:291).
- **(A) and (B) do not move the closure.** F3 code inside `valence_core/m` is excluded from it (`m_analyze.py:1714`).
- **(C) moves the closure** if the extended analyzer loads `valence_core.mf3` (B:72–73).
- **Only the package field is specific to the placement.**

**I4. B:151–152: "The OLMo track … waits only on the runpod re-authorisation and the PI's go".** The track still needs code.
- **G-CAL-OLMo, its first m stage (m:302), is not built.**
  - gcal.py:39–40: "G-CAL-OLMo (per checkpoint, b3's banner and generation path) is the OLMo track's and is not built here".
  - gcal's identity is hard-coded `"stage": "G-CAL", "substrate": "qwen"` (gcal.py:692).
  - The driver's `gcal completability` runs on Qwen only (m_sessions.py:405–445).
- **Its stage subcommands are not wired.** B:38 says so itself; the refusal is at m_sessions.py:241–245.
- **The driver is a file LOCK-m-F0 names** (v1.0 §6, LOCK-m-F0.md:423).
- **Why it matters.** If this OLMo-side code lands under `valence_core/m`, it moves `package_sha256` too. That bears on (ii) and on Q1(C)'s "There is no lock revision … the OLMo track and Q-F3 run in parallel on `main`" (B:69–70), because (C)'s F3 licence also names `valence_core/m`'s `package_sha256` (B:71–72).
- **Context.** A-m1 §0.1 says "the units are build-complete", which gcal.py:39–40 contradicts for G-CAL-OLMo.

**I5. B:111–112 and R:37–38: the four step-3 notes "were graded minor and never dispositioned".**
- **Graded minor: correct.** See the notes file's header; D8C2.104 and X2.18 are both `severity=minor`.
- **No ruling names these notes by number: correct.**
- **The seat has ruled on part of their substance:**
  - The step-14 read's Q5 (`2026-10-13_m-design-to-code_G-F0m-Qwen_read.md:46`: "m:263's form stands unchanged at every Qwen stage") settles #87's `excluded@free` half for every Qwen stage, G-TIME-F3 included.
  - Ruling (h) (seat, 2026-10-06; LOCK-m-F0.md:2411: "at any G-TIME stage the contrast session's forced rounds are reported as counts only — rounds generated, and excluded yes/no — with no class and no round position") governs contrast reporting at G-TIME stages, which is #116's subject.
- **Still open:** m:293's "lines … beside", the cap-trigger count (#130), and the order of #10's blind read.

**I6. B:79–80, Q2(i): "This delays the OLMo stages behind the build, against the routing's "OLMo units first" pod order."**
- **The routing's line** is "Pod order: [OLMo units first, then PROPOSAL-n's N-pod]" (RESULTS.md:163). It answers A-m1 §3 item 5: "The order of pod work: the OLMo units before PROPOSAL-n's N1 … or N1 first".
- **It ranks pod work against the N-pod**, not against the F3 build on the laptop.
- **The text that places the OLMo track against Q-F3** is A-m1 §4 step 4: "in parallel with 5".

**I7. B:59–61, (A): "rewrites the self-tests that assert today's Q-F3 refusals: `keys.py:204–214`; `banner.py:238–254` (…); the driver's step-19 refusals."**
- **The list omits four package self-tests** that also assert a Q-F3 refusal: guard.py:1502–1505, resume.py:1158, schedule.py:812–815 and stages.py:2683–2695. All four are listed in Code's own spec map (its "Orientation" section).
- **The anchors that are given are correct.**

**I8. B:60: "refuses A1" is in quotation marks but is not verbatim.**
- The check's text is "banner: refuses clause 2/bool, A1, base, P == Q, non-lowercase/brace/empty labels" (banner.py:253).
- "TOLD_OBJ never used" is verbatim (banner.py:239).

**I9. B:25–26: "The lock's own words (LOCK-m-F0.md:1186–1188, :2397–2398) are: "An edit under `valence_core/m` moves `package_sha256` … every non-stub stage refuses until a lock revision names the new hash"".**
- **The quote is verbatim (with its ellipsis) only at :2397–2398.**
- **:1186–1188 says it in other words:** "A later edit to the package or the analyzer moves a hash this file names." / "Every non-stub stage then refuses until a lock revision names the new hash."
- **The lock labels its :2396–2406 block "(Code's statement, from the record)".**

**I10. B:32–33: "So a package edit changes the analyzer's behaviour without moving its own sha".** Only an edit to a module the analyzer loads does that.
- **At module level it loads** audit, bars, keys, readrule and resume.
- **With `stages`, it also loads** banner, corr, guard, runner_olmo, runner_qwen, scaffold, schedule and verify.
- **The verdict path never loads** gcal, gshape or testing, nor a new module the analyzer does not import.
- **The other half is correct:** every package edit moves `package_sha256`, which PIN-14 asserts.
- **Suggested:** "can change".

**I11. B:35: `verify_schedule_dir` "rejects any unlisted file".** It rejects only unlisted `*.json` files (schedule.py:647, `d.glob("*.json")`).

**I12. B:36: "two self-tests pin its 26-file count"**, where "its" is the manifest (B:34).
- **The manifest lists 25 files.** manifest.json's `files` has 25 entries, and LOCK-m-F0.md:416 says "25 files".
- **The two self-tests pin the directory's 26 files**, manifest.json included (schedule.py:953–954; m_sessions.py:3470).
- **The anchors are correct.**

**I13. B:41: "a different scaffold (block order, and a reasoning-line seed before each menu order, m:159)".**
- **The seed is at m:159:** "per free choice [F3 only] one reasoning-line seed … then the menu order".
- **The block order is at m:174:** "F2 block order (first, first, second, second; …)".

**I14. B:119–121, Q6: "Carry-overs addressed to "the next unit's step 4" or "driver edit"".**
- **One item is addressed elsewhere.** The listing commands under O2-3 are addressed to "the next unit's README" and "the next unit's checklist" (`2026-10-19_m-design-to-code_VERDICTS_read.md:86`).
- **The other items are addressed as B says:**
  - `CHECKPOINT STATE INCONSISTENT`: "the next unit's step 4" (step-14 read Q3, `…G-F0m-Qwen_read.md:42`).
  - O1-3, RM4-1 and O4-1: "the next unit's driver edit" (`2026-10-19_m-design-to-code_step17.md:86`).
  - VC4-1 and VC4-2: "for the driver's next edit" (RESULTS.md:980).
  - The weights snapshot: "a later unit may add it at its step 4" (step-10 read Q5, `…G-TIME-F0_read.md:51`).

---

## Notes (not graded against the texts)

- **N1. B:97–99 (Q4).** The seat's quote is verbatim (VERDICTS_read.md:94), including its parenthetical "(m:267's set is e2a's by sha)". But m:267 does not define the scaffold set; m:261 does ("Qwen `scaffold_absorption` string set = the e2a ban list as `e2d.config` loads it (pinned at LOCK-m-F0 v0.1 by sha)"), and m:279 lists "the Qwen scaffold set's sha". The seat's wrong anchor passes through unmarked.
- **N2.** The message of `4574b9e`, which is unpushed (main is ahead of origin by 1), repeats F1's sentence.
- **N3. Not verifiable from the listed sources:**
  - the PI's word "Yes, start here" and Code's question (B:5–6; R:24), which exist only in the session;
  - "Every anchor below was re-read by Code at HEAD" (B:14–15);
  - "Each fact in its §1 was re-read at source by Code" (R:45–46).

  The last two are process claims; the anchors and facts themselves were checked below.

---

## All claims, with verdicts (verified unless marked)

**B, header**
1. B:1: ADDENDUM-m1 §4 step 5 is `m package — BUILD (F3)` (A-m1 §4 step 5).
2. B:3: written 2026-11-06 UTC. The commit is 03:27:48 UTC on 2026-11-06.
3. B:3: HEAD `24ebeae` = origin. It is `4574b9e`'s parent, and origin/main is `24ebeae`.
4. B:5–6: the PI's word and Code's question. **Not verifiable (N3).**
5. B:6–7: three read-only maps exist in scratch: `f3build/maps/spec.md`, `code.md`, `records.md`.
6. B:7–8: no package or driver code is written, and no file LOCK-m-F0 names is edited. The commit touches RESULTS.md and the raw only; RESULTS.md is not hash-bound by the lock.
7. B:11: the step-10 read §2 item 5 quote is verbatim and the seat's (`…G-TIME-F0_read.md:36`).
8. B:12: the R1 A2 quote is verbatim and the seat's (`…pre-LOCK-v0.1.md:21`; R1's sha256 is `b4c69f5d…f125`, as the step-10 read names it).
9. B:14: the proposal's sha256 is `42ab36ec…6c6b`.
10. B:14: A-m1's commit is `f26bc59`.
11. B:14–15: "every anchor re-read". **Not verifiable (N3).**

**B §1**
12. B:20: `package_sha256` hashes `*.py` directly in `valence_core/m`, non-recursively (resume.py:296–328; the glob is at :307).
13. B:21: its value is `5f646db6…`, recomputed over the working tree and over HEAD's blobs.
14. B:21: LOCK-m-F0 v1.0 names it (LOCK-m-F0.md:148).
15. B:22: stages.py:530–608 is `licence_problems`.
16. B:22: every non-stub stage runs it at start. `_licensed` (:1134–1139) is called from run_gate_stage (:1472), run_gid_pair (:1736) and run_campaign (:2040); see also LOCK-m-F0:1159.
17. B:23: (e) recomputes the hash.
18. B:24: (f) requires the lock's committed text to name it.
19. B:25–26: the lock quote and its anchors. **IMPRECISE (I9).**
20. B:26–27: the :2400 quote is verbatim; the ellipsis elides "(`gshape.py:92–104`)".
21. B:27–28: `SCORING_STACK_FILES` includes keys, banner, schedule, scaffold, runner_qwen, audit and corr (gshape.py:92–104; runner_olmo is in it too).
22. B:29–30: `verdicts` asserts the analyzer, package and closure shas against the lock (PIN-14; m_analyze.py:1934–1944).
23. B:30: "a worktree of the lock commit" is verbatim, and that path is not implemented (:1939–1941, "not implemented at step 8"; there is no worktree code).
24. B:31: `posting` records the three shas and does not refuse on them. `analyzer_binding` (:2370–2387) refuses only on the proposal sha or an uncommitted analyzer.
25. B:32: the module-level imports are audit, bars, keys, readrule and resume (m_analyze.py:79).
26. B:32: `stages` is imported lazily (`LAZY_VERDICT_MODULES`, :99; `production_env`).
27. B:33: "a package edit changes the analyzer's behaviour". **IMPRECISE (I10).**
28. B:33: PIN-14 binds the analyzer's behaviour through `package_sha256`.
29. B:34: the manifest's sha256 is `8c89636a…`.
30. B:34: LOCK-m-F0 pins it as a record (v1.0 §6, LOCK-m-F0.md:416; also :1151).
31. B:35: `verify_schedule_dir` runs at every stage start (`load_committed` :894–907, called at :1475, :1738 and :2042).
32. B:35: "rejects any unlisted file". **IMPRECISE (I11).**
33. B:36: the two self-test anchors pin 26 (schedule.py:953–954; m_sessions.py:3470).
34. B:36: "its 26-file count". **IMPRECISE (I12).**
35. B:37: the writer refuses unless `overwrite=True` (schedule.py:596–605).
36. B:38: the OLMo track has no lock; no `LOCK-m-OLMo*` file exists.
37. B:38: the OLMo stages are not wired in the driver (m_sessions.py:241–245).
38. B:38: "the step-9 track's refusal" is verbatim (m_sessions.py:491–492).
39. B:39: the OLMo locks will name their stages' package hash, as licence (f) requires.
40. B:41: a reasoning-line seed comes before each menu order (m:159).
41. B:41: "block order" anchored to m:159. **IMPRECISE (I13).**
42. B:42: a runner with the reasoning block (m:174).
43. B:42: the reasoning-line classes (m:265).
44. B:42: a resume identity carrying the line cap (m:174, "the cap enters the resume identity"; m:267, "cap").
45. B:43–44: any F3 code placed in `valence_core/m/*.py` moves `package_sha256`.
46. B:44: there are four consequences.
47. B:45: consequence (i). **IMPRECISE (I1).**
48. B:46–47: consequence (ii). **IMPRECISE (I2).**
49. B:48: (iii) `verdicts` refuses at HEAD for a lock naming the old hash (:1943–1944).
50. B:48–49: that would hit the OLMo units if their locks predate the build.
51. B:50: A-m1 §2.5 (3) is a byte-for-byte regression of `Q-F0_VERDICTS.json`.
52. B:50–51: that file embeds the analyzer, package and closure shas.
53. B:50–51: (iv) as a consequence of placement. **IMPRECISE (I3).**
54. B:53: a subdirectory is outside the package hash (the glob is non-recursive).
55. B:53–54: it is outside the closure, which is the loaded `valence_core.*` modules outside `valence_core/m` (m_analyze.py:1714; gshape.py:334).

**B §2 Q1**
56. B:58: "module homes" is in LOCK-m-F3 v0.1 (m:292; step-10 read §2 item 2).
57. B:60: keys.py:204–214 asserts the Q-F3 refusal (`item_key("Q-F3", 0)`, :207 and :213).
58. B:60: "TOLD_OBJ never used" is verbatim (banner.py:239).
59. B:60: "refuses A1". **IMPRECISE (I8).**
60. B:61: the driver's step-19 refusal self-tests exist (m_sessions.py:3497, :4438, :4921).
61. B:59–61: whether the self-test list is complete. **IMPRECISE (I7).**
62. B:63–65: the shared pieces exist: corr; `corrupt_m` (corr.py:212); the audit's task-round classes; bars; the banner constants; schedule's cells (`campaign_cells`, :207); and `keys.stream` (keys.py:27). They match m:54's list of shared modules.
63. B:68–69: (C) would leave the package `5f646db6…`, the manifest `8c89636a…`, G-SHAPE-F0's sources map and the driver blob untouched by F3. True of F3's effect; see I4.
64. B:71: an F3 package hash can be computed "the same way" (`package_sha256_of(root)` takes any root).
65. B:72–73: the closure binds `valence_core.mf3` only in runs that import it.

**B Q2**
66. B:79–80: "against the routing's … pod order". **IMPRECISE (I6).**
67. B:80: "OLMo units first" is verbatim (RESULTS.md:163).

**B Q3**
68. B:87: the R1 C7 quote is verbatim (`…pre-LOCK-v0.1.md:82`).
69. B:88: G-ANL-F3 extends `m_analyze.py` in place (A-m1 §2.5; m:291).
70. B:88–89: LOCK-m-F3 v0.1 names the extended analyzer (m:292).
71. B:89: each unit's analyzer of record is the one its own LOCK v1.0 hashes (PIN-14; :1936–1937).
72. B:90: `655e0f7f…` is the analyzer's sha256 at HEAD and in LOCK v1.0.
73. B:90–91: the worktree path is needed and is not implemented.
74. B:93: round 2's "text correction at the next hash-moving round" is verbatim and the seat's (`…round2.md:19`; LOCK-m-F0:2197).
75. B:93–94: A-m1 §2.5's "No other change to the analyzer is licensed by this addendum" is verbatim.
76. B:95: C7 defers the versioning to "before step 19".

**B Q4**
77. B:97–99: the seat's read §5 item 2 quote is verbatim, with ellipses (VERDICTS_read.md:94).
78. B:99: the anchor in the seat's parenthetical. **NOTE (N1).**
79. B:100: each string occurred in Q-F0's sessions (A0s s = 25; G-F0m-Qwen A0s s = 9; A0 s = 16).
80. B:101: rules 21 and 23 are applied as CLAUDE.md states them.

**B Q5**
81. B:108: the m:174 quote is verbatim.
82. B:109: the two m:293 quotes are verbatim.
83. B:110: m:271 withholds contrast sessions' free-round events to VERDICTS (or to the NOT-RUN record).
84. B:110: lines 2–6 follow the picks (N_FREE = 6; m:174).
85. B:111: the notes file's path and its date, 2026-10-06.
86. B:111: the notes were graded minor.
87. B:111–112: "never dispositioned". **IMPRECISE (I5).**
88. B:113: what #87 offers. **FAIL (F2).**
89. B:113: what #116 offers is verbatim (step3_notes.md:126).
90. B:114: the #130 quote is verbatim (:140).
91. B:115–116: #10 is counter (c)'s blind read, and its quote is verbatim (:20).

**B Q6**
92. B:119: `CHECKPOINT STATE INCONSISTENT` is addressed to "the next unit's step 4".
93. B:120: O1-3, RM4-1 and O4-1 are options, addressed to "the next unit's driver edit".
94. B:120: VC4-1 and VC4-2 are Code's declared limits (RESULTS.md:980).
95. B:120–121: "a later unit may add it at its step 4" is verbatim.
96. B:121: the README item. **IMPRECISE (I14).**

**B Q7**
97. B:125: the m:298 quote is verbatim.
98. B:126: m:73 builds and hashes v2's sentence table at LOCK-m-F3 v1.0.
99. B:126–127: (10′) at A-m1 §2.3 lets LOCK-m-F3 v1.0 precede the v1 posting; the preprint written from scratch is A-m1 §2.2's.
100. B:127–128: m:302's "preprint of record pending" is verbatim, and m:298 has no such fallback.

**B Q8**
101. B:130: there are thirty-two open readings (the spec map's §(B), B1–B32).
102. B:131–139: each listed example is among them (B1, B2, B3, B14, B13, B6–B7, B32, B31).
103. B:133: "cap reached without a newline" is verbatim (m:265, m:293).
104. B:135: "by property" is in m:314.
105. B:137: rule 28(d)'s boundary assertion is as CLAUDE.md states it.
106. B:138–139: m:361 names the runner, the verifier and the line classes; LOCK-m-F3 v0.1 also needs keys, schedules, gate files and the bar table (m:292, m:172).
107. B:142: "as at Q-F0's build": Code's PINs were declared at LOCK v0.1 and the build flags (a)–(s) listed (`54e41c9`).

**B §3**
108. B:149: nothing has been written into `valence_core/m/`, `scripts/m_sessions.py` or `data/m/`.
109. B:151: the OLMo track is A-m1 §4 step 4.
110. B:151–152: "waits only on …". **IMPRECISE (I4).**
111. B:152: the routing gives the go after re-authorisation (RESULTS.md:159, "Pod start: [go, after runpod MCP re-auth]").

**R, the RESULTS entry**
112. R:24: §4 step 5 and the PI's word. Consistent with B; the quote itself is **not verifiable (N3)**.
113. R:25: one placement question and seven others (Q1, then Q2–Q8).
114. R:26–27: the inputs are mapped read-only in scratch, and the three subjects match the three maps.
115. R:27–28: every F3 module placed in `valence_core/m/*.py` moves `package_sha256` (`5f646db6…`).
116. R:28: LOCK-m-F0 names it, and every non-stub stage checks it at start.
117. R:28–29: "Whichever lands second, the F3 code or an OLMo lock". **FAIL (F1).**
118. R:29–30: an edit to a `SCORING_STACK_FILES` entry re-runs G-SHAPE-F0 first (R1 D3; LOCK-m-F0:2400).
119. R:30–31: the step-10 read §2 item 5 rule.
120. R:32–33: the sibling package with its own driver and schedule directory, and bindings byte-identical. This restates B Q1.
121. R:35: "before step 19" is a verbatim substring of R1 C7.
122. R:37–38: "never dispositioned". **IMPRECISE (I5, repeated).**
123. R:34–41: the list of questions matches B's Q2–Q8.
124. R:42–43: no package, driver or schedule file is written, and nothing a lock names is edited.
125. R:43: the stamp is "Fri Nov  6 03:27:48 UTC 2026". The date is a Friday, and the stamp equals the commit time (22:27:48 −0500).
126. R:45: the block's path exists.
127. R:45–46: "§1 re-read at source". **Not verifiable (N3).**
128. R:47: the work done meanwhile is in scratch (`f3build/design_draft.md`).

## 2. Code's dispositions

- **F1, fixed; it reverses part of the draft's analysis.** The rule is one-directional: an edit under `valence_core/m`
  after a lock names the old hash makes that lock's stages refuse, and a lock written after an edit names the new hash. The
  block's §1 states it that way.
- **F2, fixed.** #87 only records the missing forced-round scope. The quoted fix is #116's.
- **I1, fixed.** G-SHAPE-F0 re-runs only for an edit to a `SCORING_STACK_FILES` entry. New modules alone do not trigger it.
- **I2.** Merged with F1.
- **I3, fixed.** §1 now says the regression's analyzer-sha field collides under every placement, its package field only if
  `valence_core/m` moves, and its closure field under (C) only if the extended analyzer imports the new package on Q-F0's
  path. The handling is G-ANL-F3's.
- **I4, fixed, and it changes the questions.** It was verified at `gcal.py:39–40` and `:692` and
  `scripts/m_sessions.py:491–492`. G-CAL-OLMo is not built and the OLMo stages are not wired, so the OLMo track has its own
  pending build.
  - This corrects A-m1 §0.1's "the units are build-complete", which Code's referent check at `f26bc59` passed without
    testing.
  - Q1 now distinguishes (C1), which binds all of `valence_core/m`, from (C2), which binds the modules Q-F3 imports. Q2 now
    asks where the OLMo track's own build goes and proposes "builds before locks" under the other placements.
- **I5, fixed.** The notes are "never dispositioned by number". Ruling (h) (LOCK:2411) and the step-14 read's Q5
  (`2026-10-13_m-design-to-code_G-F0m-Qwen_read.md:46`, "m:263's form stands unchanged at every Qwen stage") cover part of
  their substance. Neither reaches #130's cap trigger or the contrast sessions' reasoning lines.
- **I6, fixed.** The "OLMo units first" clause is removed. Q2 cites A-m1 §4 step 4's "in parallel with 5".
- **I7, fixed.** The four added refusal self-tests are listed.
- **I8, fixed.** The quotation is now verbatim: "refuses clause 2/bool, A1, base, …".
- **I9, fixed.** :1186–1188 is quoted as the lock's §1. :2396–2400 is quoted as "(Code's statement, from the record)".
- **I10, fixed.** The word is now "can change".
- **I11, fixed.** The text now reads "any unlisted `*.json`" (`schedule.py:647`).
- **I12, fixed.** The manifest lists 25 files, and the self-tests pin the directory's 26, manifest included.
- **I13, fixed.** Block order is cited as m:174, and the reasoning-line seed as m:159.
- **I14, fixed.** O2-3 is addressed to "the next unit's README/checklist".
- **N1, fixed.** Q4 notes that the set is defined at m:261, while the seat's anchor reads m:267.
- **The unverifiable claims** (the PI's word and Code's question, which are in the session only; "re-read at source", a
  process claim) stand as Code's statements.

## 3. The second pass, over the rewritten block and entry (verbatim)

*A second blind checker ran after §2's fixes were applied, with the first report and Code's dispositions in hand.*

# Values-check, pass 2: the F3 pre-build STOP block and its RESULTS entry (working tree on HEAD `4574b9e`)

**Texts checked**
- **B**: `results/raw/2026-11-06_f3-build_code-to-design_prebuild.md` (working tree, 180 lines), cited as B:line.
- **R**: `RESULTS.md:24–51` (working tree), the entry dated 2026-11-06 that begins "m package — BUILD (F3)", cited as R:line.

**How they were checked.** Read-only, against the tree at HEAD `4574b9e`. main is ahead of origin by 1, and `valence_core/`, `scripts/` and `data/` are clean against HEAD. Recomputed:
- `package_sha256`, by the formula in `resume.py:296–328`: `5f646db6e82c…d771` over 18 files;
- the sha256s of the proposal (`42ab36ec…6c6b`), the addendum (`ea08322d…9001`), the analyzer (`655e0f7f…c16f`) and the manifest (`8c89636a…d6bb`, 25 `files`; the directory holds 26).

Also read:
- every cited anchor, and pass 1's report and dispositions;
- the `m-v1.11` step-3 notes, the A-m1 referent-check raw, and the seat's raws;
- Code's scratch spec map, for Q8's count only.

For (C2), I imported the m modules in fresh `-I -B` interpreters (jlens venv) and listed which `valence_core.m.*` modules each set loads.

## Result

**154 claims checked: 0 FAIL, 13 IMPRECISE, 5 notes (2 not verifiable). All other claims are verified.**

## The focus items, in brief

- **The one-directional rule is verified for the package hash, with two qualifiers.**
  - `licence_problems` (e) compares the recomputed `resume.package_sha256()` with identity_extra's value (stages.py:595–600). (f) requires the lock's committed text to name it (:601–607).
  - The hash covers `*.py` directly in `valence_core/m/` only (`resume.py:307`). The lock states the rule at :1187–1188 and :2397–2398. A lock written after an edit names the new hash, and (e) and (f) pass.
  - Qualifier 1 (I1): the same function binds the analyzer's sha256 the same way, and the texts leave that half out.
  - Qualifier 2 (I12): "under `valence_core/m`" is looser than the glob.
- **G-CAL-OLMo is not built, and the OLMo stages are not wired: verified.**
  - gcal.py:39–40 is quoted verbatim, and gcal.py:692 has `"substrate": "qwen"`. No other G-CAL-OLMo code exists in `valence_core/` or `scripts/`. `gcal completability` runs on Qwen only (`m_sessions.py:405–445`).
  - `_run_stage` refuses every unit but Q-F0 (`m_sessions.py:1197–1199` → `refusal`, :241–245). "the step-9 track's refusal" is verbatim at :491–492.
  - A-m1 line 10 (§0.1) says "the units are build-complete" (also at :16 and :52). B's word "corrects" needs scoping (I6).
- **(C2): verified for the reuse set; the claim needs a qualifier (I3).**
  - The reuse set is corr, audit, bars, banner, schedule and keys. Importing it loads only those six m modules. Adding guard, resume and readrule, or runner_qwen, loads no `gcal`, `runner_olmo` or `stages`.
  - `stages` (stages.py:135) and `gshape` (gshape.py:51, :54, :57) do import them, and so does the analyzer as built. The analyzer's `production_env` imports `stages` (m_analyze.py:1783–1784), and PIN-14 asserts the whole `package_sha256`.
- **The regression fields: verified in part (I4).**
  - `Q-F0_VERDICTS.json` embeds `analyzer_sha256` 655e0f7f…, `package_sha256` 5f646db6… and `closure_sha256` a3bc7bb9….
  - m_analyze.py:1714 excludes `valence_core/m` and its subdirectories from the closure (`pkg in p.parents`, path-based, so `valence_core/mf3` is not excluded).
  - The analyzer and package halves are right. The closure half misdescribes how the closure is computed.
- **Anchors and quotes: verified.**
  - Ruling (h) (LOCK:2411) and the step-14 read's Q5 (`…G-F0m-Qwen_read.md:46`) are verbatim.
  - Notes #10, #87, #116 and #130 (:20, :97, :126, :140) are as B states them. #87 only records the gap; the fix text is #116's.
  - Every refusal self-test anchor is right, and so are `schedule.py:596–605`, `:647` and `:953–954`, `m_sessions.py:3470`, `m_analyze.py:79` and `:1934–1944`, and the 25-file manifest.
  - Every `m:N` citation and the three A-m1 citations check out, including "in parallel with 5" (A-m1:59). Exceptions: I2, I7, I8 and I13.

---

## IMPRECISE

**I1. The texts leave out the analyzer half of the stage-start rule.** This affects B:23–25, B:44–46, B:106–108 and B:113–114, and R:27–29.
- **What the function checks.** `licence_problems` checks (a)–(f), not "two things".
  - Besides (e) and (f)'s package half, (d) requires the working-tree analyzer (`ANALYZER_PATH = REPO/scripts/m_analyze.py`, stages.py:149) to hash to identity_extra's `analyzer_sha256` (:586–594).
  - (f) requires the lock's committed text to name that value as well (:601–607).
  - The driver takes both values as operator flags (`--analyzer-sha256`, m_sessions.py:6664). So after an analyzer edit, either (d) or (f) refuses.
- **What the lock says.**
  - "A later edit to the package **or the analyzer** moves a hash this file names. Every non-stub stage then refuses until a lock revision names the new hash" (LOCK-m-F0.md:1187–1188, which B itself quotes at B:26–27).
  - "An edit to the analyzer moves its sha256. Either way, every non-stub stage refuses until a lock revision names the new hash" (:2397–2398).
  - m:302 has each OLMo lock hash the "analyzer". Clause (f) makes even v0.1 name it, as LOCK-m-F0 v0.1 named `66fb5214…` (:2276).
- **The consequence the texts do not state.** G-ANL-F3 extends `m_analyze.py` in place (B:69, B:111; m:291). Under every placement, (C2) included, its commit after an OLMo lock names `655e0f7f…` makes that unit's remaining non-stub stages refuse (G-TIME-OLMo, G-F0m-OLMo, the campaign). They refuse until a revision names the extended analyzer, and not only that unit's VERDICTS, which is all B:113–114 names.
- **What follows for B's other sentences.**
  - B:108, "Under (C2), only an edit to a shared module Q-F3 imports needs sequencing", holds for package edits only; Q3 itself sequences the analyzer edit.
  - B:106–107's "names the final hash" covers the package hash only.
  - B:23–25's "checks two things" omits (d) and (f)'s analyzer half.
- **Suggested.** State the rule for both hashes, and add the stage-level analyzer consequence to Q2 and Q3.

**I2. B:67, and (B) at B:89–90: "G-SHAPE-F0 re-runs only if a `SCORING_STACK_FILES` entry is edited."** The record gives a sufficient condition, not "only if".
- **PIN-S10's map includes the tooling files.** `TOOLING_FILES` are `valence_core/m/gshape.py` and `scripts/m_sessions.py` (gshape.py:105). PIN-S10's text is "any difference re-runs G-SHAPE-F0 first" (gshape.py:233–236). R1 D3 says the same: "any other difference re-runs G-SHAPE-F0 first" (`…pre-LOCK-v0.1.md:94`).
- **The lock's next bullet, after the :2400 line B quotes, leaves the tooling case open.** "Whether D3's ruling reaches a tooling-map change made after this lock is the seat's question" (LOCK-m-F0.md:2401–2403).
- **The seat answered for one kind of edit only:** a driver edit that wires a subcommand, with no change under `valence_core/m` (step-10 read Q2, `…G-TIME-F0_read.md:45`). LOCK v0.2 §6 adds: "An edit of another kind is outside that answer; by §2 item 5 it 'is put to the seat before Code acts on it'" (LOCK-m-F0.md:903–908).
- **The record is not uniform.** The step-10 read's Q5 says that binding the snapshot in `stages.py` "moves `package_sha256` and re-runs G-SHAPE-F0" (`…G-TIME-F0_read.md:51`), the passage B quotes in Q6.
- **Pass 1's finding was narrowed.** Pass 1's I1 named the trigger as the 28-file sources map. The applied text narrows it to the 26 scoring-stack files.
- **Suggested:**
  - "G-SHAPE-F0 re-runs on an edit to a `SCORING_STACK_FILES` entry (R1 D3).
  - A driver edit that only wires a subcommand does not re-run it (step-10 read Q2).
  - Any other tooling-map edit, `gshape.py` among them, goes to the seat (LOCK v0.2 §6)."

**I3. B:100–102, (C2): "`gcal.py`, `runner_olmo.py` and the driver are not among them" needs a qualifier.**
- **Verified for the reuse set.** Importing corr, audit, bars, banner, schedule and keys loads exactly those six m modules (plus `valence_core.m`). Adding guard, resume and readrule, or runner_qwen, still loads none of gcal, runner_olmo or stages.
- **It fails if Q-F3 imports either of two modules:**
  - `stages`, which imports runner_olmo at module level (`from .runner_olmo import …`, stages.py:135);
  - `gshape`, which imports gcal, runner_olmo and stages (gshape.py:51, :54, :57). G-SHAPE-F3 is "As G-SHAPE-F0" (m:290).
- **It fails on Q-F3's VERDICTS through the analyzer as built.**
  - Every production command imports `stages` (`production_env`, m_analyze.py:1783–1784; `LAZY_VERDICT_MODULES`, :99), and with it runner_olmo.
  - PIN-14 asserts the whole `valence_core/m` `package_sha256` against the unit's lock (`env.package_sha256 = resume.package_sha256()`, :1786; the check at :1934–1944).
  - So "OLMo-side edits collide with Q-F3 only if they touch a module Q-F3 imports" holds at VERDICTS only if G-ANL-F3 changes both of those for Q-F3.
- **"The driver"** is not a `valence_core.m` module, so its exclusion holds by definition.
- **Suggested:** "For the reused modules none of these is loaded. Importing `stages` or `gshape`, or the analyzer as built (stages lazily; PIN-14 on the whole package hash), brings them back."

**I4. B:71–72: "the closure sha under (C) only if the extended analyzer imports the new package on Q-F0's path".**
- **The closure does not depend on the unit.** `closure()` runs a fresh `python -I -B` that imports the analyzer file and `LAZY_VERDICT_MODULES`. It hashes every loaded `valence_core.*` module outside `valence_core/m`, plus every repository non-`.py` file opened during those imports (m_analyze.py:1681–1719, :1723–1734). `production_env` computes it once per command (:1787).
- **When it moves.** It moves whenever the extended analyzer's module-level imports or lazy list load `valence_core.mf3`, any other new non-m module, or a new data file at import, whichever unit is regressed. There is no "Q-F0's path" in the computation.
- **(A) and (B) can move it too.** New m modules are excluded, but non-m modules or data files they load at import enter the closure. G-ANL-F3 "fixes counter (c)'s scorer and lexicons" (m:291), and LOCK-m-F3 v0.1 names "G-ANL-F3's analyzer and lexicon hashes" (m:292). Pass 1's I3 ("(A) and (B) do not move the closure") was also too strong on this.
- **Suggested:** "the closure sha whenever the extended analyzer's import closure (module level and `LAZY_VERDICT_MODULES`) gains a non-m module or a data file: `valence_core.mf3` under (C), or a lexicon read at import under any placement."

**I5. B:63–64: "Whichever track's code moves the package after the other track's first lock forces a revision of that lock."**
- **It holds only where that lock binds `package_sha256`:** the OLMo locks, and LOCK-m-F3 under (A), (B) or (C1).
- **Under (C2),** B's own recommendation, an OLMo-side package move forces a Q-F3 revision only if it touches an imported module (B:100–101).
- **Its scope is wider than "first lock".** The revision is owed for every lock of the other track written before the move, while that lock's stages or VERDICTS remain to run.
- **Suggested:** add "where that lock binds `package_sha256`".

**I6. B:54–61 and R:29–31: "This corrects A-m1 §0.1's 'the units are build-complete'".**
- **The facts are right.** G-CAL-OLMo has no code, and the OLMo stage subcommands refuse.
- **§0.1 states "build-complete" of step 4's build.** It reads: "…were built at §8 step 4 (entry `m package — BUILD (Q-F0 subset)`); the units are build-complete" (A-m1:10). m:357's step-4 list names neither G-CAL nor stage wiring.
- **The record's precedent puts both outside the build step:**
  - On Q-F0, G-CAL's tooling was built at step 6 (`c75d4d8`; `valence_core/m/__init__.py`: "step 6 adds `gcal`"). gcal.py:39–40 assigns G-CAL-OLMo to "the OLMo track".
  - Each stage subcommand is wired at its own step. The driver PIN says "the stage subcommands refuse with exit 2 until their step" (m_sessions.py:221–222); LOCK-m-F0.md:2488 says "each subcommand is wired at its own step".
  - `stages.py` already carries the OLMo stages (stage names :202–203, `olmo_startup` :950, `run_session_olmo` :1176). So the wiring is a driver edit of the step-10 read's Q2 kind, which moves neither hash.
- **What the facts contradict is the readiness reading.** A-m1 §0.4 says "The units are build-complete at ≈ 1.0–1.4 h … plus G-CAL-OLMo's 128 generations" (:16), and §3 item 5 says "build-complete and short" (:52).
- **"Code's referent check at `f26bc59`".**
  - The check ran at HEAD `18c32df` (`results/raw/2026-11-06_m1-v0_1_referent-check.md` §1) and was committed in `f26bc59`.
  - Its scope was §5's referents, "only what this document quotes" (A-m1:65). Within that scope it confirmed only that `runner_olmo.py` exists (raw :149).
- **The same precedent bears on B:177–178,** "Before its first stage it needs … its stage wiring". Only G-CAL-OLMo's code and its entry point precede the first stage; the gate stages follow LOCK v0.1 (m:302).
- **Suggested:** "A-m1 §0.1–§0.4 read the units as needing only pod time. G-CAL-OLMo's tooling (built for Qwen at step 6) and the per-step stage wiring are still to be written."

**I7. B:145–147, Q6: VC4-1 and VC4-2 are not addressed to "the next unit".**
- **Their own text:** "VC4-1 and VC4-2, for the driver's next edit" and "VC4-1 and VC4-2 wait for the driver's next edit" (RESULTS.md:984, :1003). No unit is named.
- **Whose phrase "driver edit" is.** "The next unit's driver edit" is the step-17 read's phrase for O1-3, RM4-1 and O4-1 (`…step17.md:86`).
- **Why it matters.** It bears on Code's reading at B:150. "The driver's next edit" may be the OLMo wiring whichever unit comes next, and under (C) Q-F3's build does not edit `scripts/m_sessions.py`.
- **Suggested:** list VC4-1 and VC4-2 separately, as "for the driver's next edit".

**I8. B:149, Q6: "the next unit's README/checklist" is a composite inside quotation marks.**
- **The source has two phrases:** "For the next unit's README, with O1-3, RM4-1 and O4-1" and "the next unit's checklist should name the listing forms" (`…VERDICTS_read.md:86`). The README line also covers O1-3, RM4-1 and O4-1.
- **Suggested:** quote the two phrases separately.

**I9. R:43–44: "Both FAILs reversed parts of the draft's analysis."**
- **F2 reversed nothing in the analysis.** It corrected which note offers a quoted fix (#87 or #116).
- **Code's own dispositions say so.** "F1, fixed; it reverses part of the draft's analysis" and "F2, fixed. #87 only records the missing forced-round scope. The quoted fix is #116's." (`…prebuild_valuescheck.md:303–306`).
- **The other item that changed the analysis is I4:** "fixed, and it changes the questions" (:312).
- **Suggested:** "F1 and I4 changed parts of the draft's analysis."

**I10. B:92–96, (C): "Q-F3's code then never moves `valence_core/m`."**
- **The list of what (C) adds omits two pieces that refuse Q-F3 in the package today:**
  - Q-F3's keys: `keys.py:66–67` raises `NotImplementedError`, and m:292 puts keys in LOCK-m-F3 v0.1.
  - The cached-path source guard: `guard.py:160–162` refuses Q-F3 through `keys.templates`, and m:267 requires it for Q-F3's cached reasoning lines.
- **The analyzer refuses Q-F3 too.** Its V1 refuses any unit outside `keys.UNITS_BUILT` (m_analyze.py:1921; keys.py:19).
- **So "never moves" depends on two conditions:** mf3 reimplements the keys and the guard, and G-ANL-F3 does not extend `keys.UNITS_BUILT`.
- **Suggested:** add keys and the source guard to (C)'s own list, and name the `UNITS_BUILT` check as G-ANL-F3's.

**I11. B:26: "The lock's §1 (LOCK-m-F0.md:1186–1188, …)".**
- **These lines are in the retained v0.1 text.** They sit in its §1 ("## 1. Binding identity and the licence by file", :1121, under "# The v0.1 text", :988).
- **LOCK-m-F0 v1.0's §1 is a different section** (:140, "The analyzer of record, the package and G-ANL-F0"), and B's preceding bullet names v1.0.
- **Suggested:** "LOCK-m-F0 v0.1 §1 (kept in the file, :1186–1188)".

**I12. B:44, R:27, and B:60–61: "an edit under `valence_core/m`".**
- **The hash is narrower than "under".** Only `*.py` files directly in `valence_core/m/` move it (the non-recursive glob, `resume.py:307`). A file in `valence_core/m/f3/` is "under" it and moves nothing, as B:74–75 says.
- **Low severity.** The record uses the same idiom (LOCK-m-F0.md:2397; step-10 read Q2).
- **Suggested:** "an edit to a `*.py` file directly in `valence_core/m/`".

**I13. B:158, Q8: "Thirty-two places where the spec leaves a reading open".**
- **One of the 32 is not spec text.** B32 in Code's map is labelled "build hazard, not spec text" (`f3build/maps/spec.md:410`). It is among Q8's listed examples (the `"\n\n"` against rule 28(d)).
- **Suggested:** "thirty-one open readings and one build hazard".

---

## Notes (not graded against the texts)

- **N1.** Two stamps date from the first draft:
  - B:3's "HEAD `24ebeae` = origin";
  - R:46's stamp, "Fri Nov  6 03:27:48 UTC 2026".

  At this revision HEAD is `4574b9e` (main ahead of origin by 1). Both files were last written at about 03:58 UTC (mtimes). Not graded, under the stamp convention.
- **N2. Not verifiable from the sources:**
  - the PI's word "Yes, start here" and Code's question (B:5–6; R:24);
  - R:49–50's "the report verbatim", a process claim. The file's structure (§1 the report, §2 the dispositions) is as stated.
- **N3.** A-m1 says "build-complete" also at §0.4 (:16) and §3 item 5 (:52), not only at §0.1.
- **N4.** The seat's sentence quoted in Q6 continues: "flagged for the next unit's step 4, where the package moves anyway" (`…G-F0m-Qwen_read.md:42`). It presumes a package move that (C) avoids. This is relevant to Q1 and Q6; it is not an error in B.
- **N5.** Every item graded in pass 1 is addressed in the texts. I2 and I4 concern the forms in which pass 1's I1 and I3 were applied.

---

## All claims, with verdicts (verified unless marked)

**B, header**
1. B:1: BUILD (F3) is A-m1 §4 step 5 (A-m1:60).
2. B:3: written 2026-11-06 UTC.
3. B:3: HEAD `24ebeae` = origin. **N1.**
4. B:5–6: the PI's word and Code's question. **N2.**
5. B:6–7: the three read-only maps exist in scratch (`f3build/maps/{spec,code,records}.md`).
6. B:7–8: no package or driver code is written, and no file LOCK-m-F0 names is edited.
7. B:11: the step-10 read §2 item 5 quote is verbatim (`…G-TIME-F0_read.md:36`).
8. B:12: the R1 A2 quote is verbatim (`…pre-LOCK-v0.1.md:21`).
9. B:14: the proposal's sha256 is `42ab36ec…6c6b`.
10. B:14: A-m1 is `f26bc59`.
11. B:15: pass 1's counts (128; 2 FAIL; 14 IMPRECISE).
12. B:15–16: every item was re-verified and applied (N5).

**B §1**
13. B:21: `*.py` directly in `valence_core/m`, non-recursive (resume.py:296–328; the glob at :307).
14. B:22: `5f646db6…`, 18 files (recomputed).
15. B:22: LOCK-m-F0 v1.0 names it (:148).
16. B:23: every non-stub stage start runs `licence_problems` (`_licensed`, :1134–1139, from :1472, :1736 and :2040; LOCK:1159).
17. B:23–25: "checks two things". **IMPRECISE (I1).**
18. B:24: (e) recomputes the hash and compares it (:595–600).
19. B:25: (f) requires the lock to name it (:601–607).
20. B:26: "the lock's §1" for :1186–1188. **IMPRECISE (I11).**
21. B:26: attributed to the D2 round entry's "To the seat" (:1186).
22. B:26–27: the quote is verbatim (:1187–1188).
23. B:28: :2396 carries the label "(Code's statement, from the record)".
24. B:29: the :2400 quote is verbatim.
25. B:29–31: the list includes the eight m modules named (gshape.py:93–95).
26. B:31: a new module alone is not on it.
27. B:32–33: `verdicts` asserts the three shas against the unit's lock (PIN-14; :1934–1944).
28. B:33: "a worktree of the lock commit" is declared and not implemented (:1939–1941).
29. B:34: `posting` records the three shas and does not refuse on them (:2370–2387).
30. B:35: the module-level imports (:79).
31. B:35: `stages` is imported lazily (:99; `production_env`, :1784).
32. B:36–37: a package edit can change the analyzer's behaviour without moving its sha; PIN-14 binds it through `package_sha256`.
33. B:39: `verify_schedule_dir` runs at every stage start (stages.py:904, via :1475, :1738 and :2042).
34. B:39: it rejects any unlisted `*.json` (schedule.py:647; "unlisted" means outside this machine's regeneration, :625).
35. B:40: the manifest is `8c89636a…`.
36. B:40: LOCK-m-F0 pins it as a record (:416).
37. B:40: it lists 25 files.
38. B:41: two self-tests pin 26 files, manifest included (schedule.py:953–954; m_sessions.py:3470).
39. B:42: the writer refuses unless `overwrite=True` (schedule.py:596–605).
40. B:44–45: an edit after a lock names the old hash makes that lock's stages refuse until a revision; verified for the package. **Qualified by I1 and I12.**
41. B:45–46: a lock written after the edit names the new hash, and nothing refuses (the hash checks).
42. B:50: F2 block order (m:174).
43. B:50: a reasoning-line seed before each menu order (m:159).
44. B:51: the runner's reasoning block (m:174).
45. B:51: the reasoning-line classes (m:265).
46. B:52: the resume identity carries the line cap (m:174, "the cap enters the resume identity"; m:267, "cap").
47. B:53: F3 read rules, bars, stage drivers and schedules are pending (no Q-F3 schedule files; keys, readrule and resume refuse Q-F3).
48. B:55: G-CAL-OLMo is not built; the quote is verbatim (gcal.py:39–40; no other G-CAL-OLMo code exists).
49. B:56: gcal.py:692 has `"substrate": "qwen"`.
50. B:57: the OLMo stages are not wired (m_sessions.py:1197–1199).
51. B:57: "the step-9 track's refusal" is verbatim (:491–492).
52. B:58: A-m1 §0.1 says "the units are build-complete" (A-m1:10).
53. B:58: "This corrects". **IMPRECISE (I6).**
54. B:58–59: "Code's referent check at `f26bc59` passed that sentence without testing it". **IMPRECISE (I6).**
55. B:60: the OLMo track has its own build step before its first stage (m:302; G-CAL-OLMo comes first).
56. B:60–61: code placed in the package moves `package_sha256` (see I12 on "under").
57. B:63: both tracks hold code that would land in, or bind to, `valence_core/m`.
58. B:63–64: "Whichever … forces a revision of that lock". **IMPRECISE (I5).**
59. B:67: "G-SHAPE-F0 re-runs only if …". **IMPRECISE (I2).**
60. B:68: A-m1 §2.5 (3) is a byte-for-byte regression of `Q-F0_VERDICTS.json` (A-m1:44; `Q-F0_secondary.json` too).
61. B:68: the file embeds the analyzer, package and closure shas.
62. B:69: the analyzer field moves under every placement (m:291; A-m1 §2.5).
63. B:70: the package field moves only if `valence_core/m` moves.
64. B:71–72: the closure field "under (C) only if … on Q-F0's path". **IMPRECISE (I4).**
65. B:72: m_analyze.py:1714 excludes `valence_core/m`.
66. B:74: a subdirectory lies outside the package hash (:307) and outside the closure (:1714, `pkg in p.parents`).
67. B:75: it would run unbound (the licence binds only the package and the analyzer).

**B Q1**
68. B:79: "module homes" is in LOCK-m-F3 v0.1 (m:292).
69. B:83: (A) moves the hash and re-runs G-SHAPE-F0, because scoring-stack files are edited.
70. B:85: keys.py:204–214.
71. B:86: banner.py:239 ("TOLD_OBJ never used") and :253 (a verbatim prefix).
72. B:87: guard.py:1502–1505.
73. B:87: resume.py:1158.
74. B:87: schedule.py:812–815.
75. B:87: stages.py:2683–2695.
76. B:88: the driver's step-19 refusals exist (m_sessions.py:3495–3497, :4438–4450, :4921–4937).
77. B:89: (B) moves the hash.
78. B:89–90: (B)'s G-SHAPE condition. **IMPRECISE (I2).**
79. B:92–93: (C)'s reused pieces exist (corr.py:212; keys.py:27; schedule.py:207; banner's TOLD_OBJ and reasoning-block constants).
80. B:94–96: what (C) adds, and "never moves". **IMPRECISE (I10).**
81. B:98–99: (C1)'s reverse collision.
82. B:100–102: (C2). **IMPRECISE (I3).**

**B Q2**
83. B:104: "in parallel with 5" is verbatim (A-m1:59).
84. B:105: placing the OLMo code in `valence_core/m` moves the hash.
85. B:106–107: "builds before locks … names the final hash". **IMPRECISE (I1).**
86. B:108: "Under (C2), only …". **IMPRECISE (I1).**

**B Q3**
87. B:110: the R1 C7 quote is verbatim (`…pre-LOCK-v0.1.md:82`).
88. B:111: G-ANL-F3 extends the analyzer in place (A-m1 §2.5; m:291).
89. B:112: LOCK-m-F3 v0.1 names the extended blob (m:292).
90. B:112: PIN-14's analyzer of record (:1936–1937).
91. B:113: `655e0f7f…` is the analyzer at HEAD and in LOCK v1.0.
92. B:113–114: the OLMo VERDICTS need the unimplemented worktree path. Verified, but incomplete (I1).
93. B:114: the alternative.
94. B:116: round 2's quote is verbatim (`…round2.md:19`).
95. B:117: A-m1 §2.5's quote is verbatim (A-m1:44).

**B Q4**
96. B:120–122: the seat's quote is verbatim, with ellipses (`…VERDICTS_read.md:94`).
97. B:122: the set is defined at m:261; the seat's anchor reads m:267.
98. B:123: each string occurred in Q-F0's sessions (A0s s = 25; G-F0m-Qwen A0s s = 9; A0 s = 16).
99. B:124: rule 21, as CLAUDE.md states it.
100. B:125–126: rule 23's descriptive counter.

**B Q5**
101. B:131: the m:174 quote.
102. B:132: the m:293 quotes.
103. B:133: m:271 withholds contrast sessions' free-round events (to VERDICTS or the NOT-RUN record).
104. B:133: lines 2–6 follow the picks (m:174; `N_FREE` = 6).
105. B:134: the notes' path and date.
106. B:134: graded minor (the file's header).
107. B:134: never dispositioned by number (R1 E6 names #25, not #10, #87, #116 or #130).
108. B:136: #87 (:97).
109. B:137: #116 (:126).
110. B:138: #130 (:140).
111. B:139: #10 (:20).
112. B:140: ruling (h) (LOCK:2411).
113. B:140–141: the step-14 read's Q5 (`…G-F0m-Qwen_read.md:46`).
114. B:141–142: neither reaches #130's trigger or the reasoning lines.

**B Q6**
115. B:146–147: the `CHECKPOINT STATE INCONSISTENT` message is addressed to "the next unit's step 4" (`…G-F0m-Qwen_read.md:42`).
116. B:146–147: O1-3, RM4-1 and O4-1 are options addressed to "the next unit's driver edit" (`…step17.md:86`; RESULTS.md:1004–1005).
117. B:146–147: VC4-1 and VC4-2 are Code's declared limits (RESULTS.md:967, :984).
118. B:146–147: VC4-1 and VC4-2's addressee. **IMPRECISE (I7).**
119. B:148: the weights-snapshot quote is verbatim (`…G-TIME-F0_read.md:51`).
120. B:149: "README/checklist". **IMPRECISE (I8).**

**B Q7**
121. B:153: the m:298 quote is verbatim.
122. B:154: m:73 builds and hashes v2's sentence table at LOCK-m-F3 v1.0.
123. B:154–155: (10′) at A-m1 §2.3; the preprint written from scratch is A-m1 §2.2's.
124. B:155–156: m:302's "preprint of record pending"; m:298 has no such fallback.

**B Q8**
125. B:158: "Thirty-two". **IMPRECISE (I13).**
126. B:160–167: each example is among them (B1, B2, B3, B14, B13, B6–B7, B32, B31).
127. B:161: "cap reached without a newline" (m:265).
128. B:163: "by property" (m:314).
129. B:165: rule 28(d)'s boundary assertion.
130. B:166–167: m:361's list, and LOCK-m-F3 v0.1's needs (m:292, m:172).
131. B:169–170: "as at Q-F0's build" (`54e41c9`'s flags (a)–(s)).

**B §3**
132. B:174–175: nothing is written in `valence_core/m/`, `scripts/m_sessions.py`, `data/m/` or any file a lock names.
133. B:177: the OLMo track is A-m1 §4 step 4.
134. B:178: "its stage wiring" before the first stage. **IMPRECISE (I6, sub-point).**
135. B:179: the runpod re-authorisation (A-m1:59; m:358).
136. B:180: the routing gives the go after re-authorisation (RESULTS.md:163).

**R, the RESULTS entry**
137. R:24: §4 step 5, and the PI's word. **N2.**
138. R:25: a placement question and seven others.
139. R:26–27: the inputs are mapped, read-only, in scratch.
140. R:27–29: the rule. Verified for the package; **qualified by I1 and I12.**
141. R:28: `5f646db6…`.
142. R:29–30: both tracks have code pending.
143. R:30: G-CAL-OLMo is not built (gcal.py:39–40).
144. R:30: the OLMo stages are not wired.
145. R:30–31: "This corrects …" and the referent check. **IMPRECISE (I6).**
146. R:32–33: the step-10 read §2 item 5 rule.
147. R:34–35: the recommendation (C2) matches B.
148. R:36–42: Q2–Q8 match B; "before step 19" is a substring of R1 C7.
149. R:43: values-checked blind before the push; the counts.
150. R:43–44: "Both FAILs reversed parts of the draft's analysis". **IMPRECISE (I9).**
151. R:44: every item is applied (N5).
152. R:45: what is not done.
153. R:46: the stamp. **N1.**
154. R:48–51: the two paths exist, and the work meanwhile is in scratch (`f3build/design_draft.md`).

## 4. Code's dispositions of the second pass (applied before the push)

Code re-verified each item at source.

- **I1, applied.** It was verified at `stages.py:586–594`. The licence's analyzer half (d) now appears in §1, in "What
  follows", in Q2 and in Q3: G-ANL-F3's in-place analyzer edit after an OLMo lock makes the OLMo stages refuse at start
  under every placement.
- **I2, applied.** It was verified at `gshape.py:233–236` and `:105`. PIN-S10's "any difference" over scoring-stack and
  tooling files is quoted, the seat's clearance of subcommand-wiring driver edits is named, and what else re-runs G-SHAPE-F0
  is left to the seat.
- **I3, applied.** It was verified at `stages.py:135`, `gshape.py:51` and `:54`, and `m_analyze.py:1783–1784` and
  `:1934–1944`. (C2) now states its proviso (no import of `stages` or `gshape`) and that it decouples stage-time licences
  only.
- **I4, applied.** The closure field is described as unit-independent (`m_analyze.py:1681–1734`).
- **I5, applied.** The text now reads "a lock that binds `package_sha256` … and of every earlier such lock".
- **I6, applied.** It was verified at `c75d4d8` (Q-F0's G-CAL tooling, step 6), LOCK-m-F0.md:2488 and A-m1 :10, :16 and
  :52. "Build-complete" is true of step 4's list, and what fails is the readiness reading; the referent check's scope is
  named.
- **I7, applied.** VC4-1 and VC4-2 wait for "the driver's next edit".
- **I8, applied.** The two quotations are kept separate.
- **I9, applied.** The entry now names F1's reversal and I4's change of the questions.
- **I10, applied.** It was verified at `guard.py:160–162` and `m_analyze.py:1921`. Q-F3's own keys and guard sit in the new
  package, and the analyzer's unit check is G-ANL-F3's.
- **I11, applied.** The quotation is cited as the lock's v0.1 text, §1.
- **I12, applied.** The text now reads "a `*.py` file directly in `valence_core/m`".
- **I13, applied.** The text now reads "Thirty-one … and one build hazard".
- **The notes.**
  - The header now reads "Written … at HEAD `24ebeae` = origin, and revised after two blind values-checks before its push".
  - The entry's stamp is refreshed.
  - "Build-complete" at :16 and :52 is cited.
  - Q6 notes the seat's "where the package moves anyway" premise.
