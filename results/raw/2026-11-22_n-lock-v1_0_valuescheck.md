# n — LOCK-n v1.0's draft, entry and checks raw: the first blind values-check, as returned, with every disposition

PI date 2026-11-22. Code (the n-build session).

**What was checked.** One blind pass by a subagent over three texts, at HEAD `fd5d61c`:
- T1, LOCK-n v1.0's draft 7, sha256 `5cadc821…5908` (1374 lines: the v1.0 part 316, v0.1's text 1058);
- T2, the entry as drafted, `4a49984b…be65` (111 lines), with placeholders not to be checked: the draft's name at
  the root and one sentence on it (the placement, then a question with the coordinating session), later sweeps, later
  drafts, the checker's summary and its departures;
- T3, the checks raw as staged, `16a1fb92…4fa7` (36 lines).

**The checker's brief** was its prompt by reference: Code's scratch file `S/step4b/lock10/vc_brief.md` (`5c22ca32…6ef4`,
136 lines), which the checker read whole and hashed first. It:
- named the texts and the sources: in the repository, the files the texts cite, at `fd5d61c` (BK's 26 files by
  `shasum -c` alone, the report by `shasum` alone); in Code's scratch, the tools (the fill script and the commit
  kit's library among them), the entry's source and Code's two notes of values, the seven kept drafts and the
  generator's re-run;
- allowed `shasum` by name, and `jq` on the sweep record, on this session's transcript and on committed JSON and JSONL
  outside `data/*/ckpt`, `data/*/reports` and `data/m[f]3`;
- set the transcript's use: a sweep of Code's tool calls from G-VER (n)'s entry's final sweep to the brief's own hash,
  with Code's extraction of the span up to its last record (162 calls) beside it;
- barred any other interpreter, any write and any network; any guard marker in an argv (a path, a grep pattern, a
  variable or glob that expands to one, a loop, the command's own text); anything under `data/m[f]3` and any
  whole-tree git status; any read, listing, size or time of a ckpt or reports file, and any `--stat` form over a
  commit that holds one; and anything in Code's scratch but the named files;
- quoted the list of record v2's items 1–5 verbatim (byte-equal to the G-VER entry's brief's, by `cmp`), and required
  item 3's pathspec and the campaign folder's exclusion on every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (234 lines, sha256
`844739d2…0a08`). It names scratch files by their paths inside the scratch folder (L is `S/step4b/lock10`) and the
transcript as T.

**Totals:** 127 items: 104 CONFIRMED, 11 IMPRECISE, 3 FAIL, 9 NOT CHECKABLE; and 12 observations. Code counted them
again by tool, by the verdict on each item's line inside the report's ITEMS section.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

Every FAIL and every IMPRECISE item is applied, in the checker's words or near them; every observation is applied,
met or noted; three NOT CHECKABLE items are acted on. "Draft 8" is the draft that applies them; drafts 9 and 10 carry
them unchanged, and the second values-check read draft 9; "the entry" is the entry as revised.

- **Items 104, 106 and 116 (FAIL), the entry's departures list.** Applied: three memory notes, not four (two by a `for`
  loop over their names); eleven named paths, not ten; and every kind item 116 lists, in its terms.
- **Items 45, 50 and 74 (IMPRECISE), the draft.** Applied in draft 8:
  - 45, v1.0 §5 item 5: "which G-TIME-n's artifact (its `lock_sha256`) and G-VER's record (its `pins.lock_sha256`)
    carry". The key is top-level in `data/n/gtime/gtime.json`, by `jq`, so the artifact is named rather than an
    identity;
  - 50, v1.0 §5: "its "where" cell "before any read"" (L:541's head: trigger, where, bar, on fire, source);
  - 74, v1.0 §10 (b), in the checker's words, with "for a crashed invocation" from L:872.
- **Items 91, 94, 96, 97, 99, 101, 103 and 110 (IMPRECISE), the entry.** Applied:
  - 91: the cap, its sum, the forwards' planning value revised and the loads measured (with observation 2);
  - 94: each draft was made by the generator as it then stood, and the checks raw re-runs the final generator and
    finds the placed draft byte for byte;
  - 96 and 99: in the checker's words;
  - 97: draft 4's omitted changes listed, and "v0.1 §11 (a)'s words quoted beside R3" for "R3 stated";
  - 101: "the 12 files the part names a commit for (eight commits), each commit the file's last change";
  - 103: the commit's 17th path, RESULTS.md, by `shasum` and `wc -l`; `ps -p 8051` printed 8051 (Q-F3's campaign,
    running); `pgrep -f n_sessions` found none;
  - 110: the scratch kinds completed, with item 116's.
- **Items 21, 49 and 80 (NOT CHECKABLE), the draft.** Acted on in draft 8: v1.0 §2 says step 14's BUILD is to pass the
  cap, unbuilt, G-TIME-n's stage having passed none (n_sessions.py:4373); v1.0 §12 states the driver's pin as it
  stands (`LOCK_SHA256`, v0.1's) and the campaign's citation of this file once committed. The other six NOT CHECKABLE
  items are plans or the checker's limits, left as stated.
- **Observation 1, the form.** Applied in draft 8: the part ends with `---` and the precedence sentence, as LOCK-m-F3
  v1.0's does (LOCK-m-F3.md:321), and gains v1.0 §11 (Code's readings, and what the commit closes), §12 (how the
  campaign cites this file) and §13 (what follows).
- **Observation 2, the loads.** Applied: v1.0 §1 carries ans21c:26's loads, one of the figures of §1.2–§1.4 that
  rt21c item 1 has v1.0 carry.
- **Observations 3 and 4, R3 and R1.** Applied: both are rulings, not readings. v1.0 §2 cites ans21b:23 for the fits
  outside the cap; v1.0 §10 cites ans21a:8 and ans21a:40 for the corrected words, and WORKFLOW.md:43 for the form.
- **Observation 5, R4.** Applied: v1.0 §8 shows the three lines in a blockquote, which the analyzer does not read
  (n_analyze.py:6264–6265), and cites ans20b:50; the generator still asserts one whole line of each.
- **Observation 6, R2's numbering.** Applied: v1.0 §5 says the seat's "§10" is v0.1's numbering.
- **Observation 7, R5.** Noted in the entry: the driver's lock checks (n_sessions.py:3913–3914, :5167–5168) refuse a
  `LOCK-n.md` that is not HEAD's committed bytes, so a draft over it would stop G-TIME-n's and G-VER's commands on
  this tree. The placement is with the PI.
- **Observation 8, the committed bytes.** Applied: v1.0 §13 gives the committed status line's words, Code's, for the
  seat to set, as it set v0.1's (ans20b:18).
- **Observations 9–12.** Applied in the entry: the checks raw made twice (`ddfdce0a…69d5`, removed after the
  generator's one-line edit, and remade) in its checks paragraph, the removal in its departures; and in its
  departures, the campaign folder's plain name in four of Code's command outputs, output only; the file tool's calls
  in scratch; and the steps before `fd5d61c`'s window.

## 2. Beside the check, and the second check

Draft 8 also carries what the seat's second sitting of 2026-11-22 routed after the check began (the PI's "PI: route as
given", relayed by the coordinating session): it is anchored at the HEAD of the coordinating session's commit of that
sitting's raw (`results/raw/2026-11-22_n-gver-record-read_design-to-code_answers.md`, ans22b); v1.0 §0 quotes that
sitting's item 2 and the raw's §2 (raw:30); v1.0 §4 hashes the raw, the PI's routing raw of that sitting and
WORKFLOW.md; v1.0 §5 cites G-VER's acceptance as the gate of record (ans22b:7); and v1.0 §13 carries the raw's
§1.3–§1.4 for step 14's launch files. A second blind values-check reads draft 9 and the entry as revised:
[`2026-11-22_n-lock-v1_0_valuescheck2.md`](results/raw/2026-11-22_n-lock-v1_0_valuescheck2.md).

## 3. The report, as returned

```text
**Values-check of LOCK-n v1.0's draft (T1), its entry (T2) and the checks raw (T3)**

The brief was read whole and its sha256 (5c22ca32…6ef4, 136 lines) confirmed. HEAD is `fd5d61c`. T1, T2, T3, L/sweep.jsonl, L/sweep_view.txt, the tools, the seven kept drafts and L/regen_draft7.md all match the sha256s given. Every cited repository file is tracked and clean at `fd5d61c`.

Overall: T1 holds up. Every sha256, quotation, anchor, table row and code claim checks out, and T1 committed as the lock would pass the analyzer's lock rules. The problems are in T2, which has 3 FAILs and several imprecise statements: two wrong counts in its departures list, and a list that does not name every kind of command Code ran.

## ITEMS

**T1 — the v1.0 part (lines 1–316) and the tail**

1. **T1:1** — refs: n §3 "LOCK-n v1.0" and §8 step 13. **CONFIRMED.** n:120 is in §3 (n:105–123); step 13 is at n:159.
2. **T1:3–5** — the commit plan (by path, on the PI's routing, by D_n, superseding v0.1). **NOT CHECKABLE.** It is a plan.
3. **T1:7–8** — drafted at HEAD `fd5d61c`, G-VER (n)'s commit, on rt22a item 3 and rt21c item 4. **CONFIRMED.** Checked by `git rev-parse` and fd5d61c's subject.
4. **T1:8–9** — in LOCK-m-F3 v1.0's form: a v1.0 part above the earlier text kept verbatim. **CONFIRMED.** LOCK-m-F3.md has its v1.0 part at :1–321 and v0.2's text from :323. See Obs 1.
5. **T1:9–11** — a tool placed the sha256s and the line count, the package digest and both tables. **CONFIRMED.** gen_v10.sh:17–24, :30–35 and :39–50 do this; the placeholders are in v10_part_src.md.
6. **T1:11–12** — a tool found every quotation, and BK's commit and tree ids, in its source. **CONFIRMED.** check_quotes.sh:24–71 lists 48 entries. Every quoted span in T1's part is one of them or a substring of one.
7. **T1:12** — each commit named for a file is the file's last change. **CONFIRMED.** For 11 files by `git log -1` per path. For the report, by its digest equalling G-TIME-n's entry (the brief allows a digest only).
8. **T1:12–13** — "Code typed the prose. Nothing in this file has run." **NOT CHECKABLE.**
9. **T1:17–19** — n:120, verbatim. **CONFIRMED** by `cmp`.
10. **T1:21–23** — rt21c:24–29, verbatim. **CONFIRMED** by `cmp` after joining the wrapped lines.
11. **T1:25–27** — rt22a:29–31, verbatim. **CONFIRMED** the same way.
12. **T1:29–40** — §0's list of sections. **CONFIRMED.** It matches the headings at T1:60–305.
13. **T1:42–43** — v0.1 is `LOCK-n.md` at `deabf3f`, 1058 lines, `88d9fe7b…e9d5`. **CONFIRMED.** The file has one commit, `deabf3f`.
14. **T1:44–58** — the conventions and short forms (ans21a/b/c, ans22a and their sittings; rt21a–rt22a; n:, A-n1–3:, C:). **CONFIRMED.** Checked against each raw's header and LOCK-n.md:104–111.
15. **T1:62–64** — rt21c:17–20, verbatim. **CONFIRMED.**
16. **T1:67–80** — the eight ans21c quotations (:18, :19, :23, :27 twice, :31, :32, :35). **CONFIRMED.** schema.py:83–85 holds the 4.9–5.0 GB the :32 quotation cites.
17. **T1:81–83** — gtime.json, `n-gtime-v1`, `d6d475b7…`, at `7d01b02`. **CONFIRMED.**
18. **T1:84–85** — time.json `3ae33a39…`, by `shasum`, committed at `7d01b02`. **CONFIRMED.** Digest by `shasum`; RESULTS.md:1655–1657; gtime.json's `report_sha256` is equal.
19. **T1:89–90** — the cap is 4 h; rt21c:21; rt22a:30. **CONFIRMED.**
20. **T1:91–92** — `hour_cap_ms` (runner.py:266) = 14,400,000 ms; ans20b:39. **CONFIRMED.**
21. **T1:92–93** — "The campaign's wiring … passes it". **NOT CHECKABLE.** The wiring is not built; G-TIME-n passed `hour_cap_ms=None` (n_sessions.py:4373).
22. **T1:93** — a resume keeps the cap (runner.py:413–414). **CONFIRMED.**
23. **T1:94–95** — what the cap counts, as v0.1 §11 has it. **CONFIRMED** at L:600–602.
24. **T1:96–97** — the quotations of L:602–603. **CONFIRMED.**
25. **T1:97–99** — R3. **CONFIRMED** as to what ans21c:35 holds; a fair reading. See Obs 3.
26. **T1:100–106** — the ans21c:45 quotations and the items beside the cap. **CONFIRMED.**
27. **T1:107–108** — ans21c:43. **CONFIRMED.** runner.py:412–416 holds the resume's cap and alpha refusals.
28. **T1:112–113** — n:152, §7.4. **CONFIRMED.**
29. **T1:114–115** — D_n is 2026-12-15 as L:985 has it; n:159's quotation. **CONFIRMED.**
30. **T1:115** — "falls on or before it". **NOT CHECKABLE.**
31. **T1:116** — n:134. **CONFIRMED.**
32. **T1:116–118** — the four `clock:` causes. **CONFIRMED** at n_analyze.py:120–124.
33. **T1:122–127** — the proposal's and addenda's sha256s, each v0.1 §23's. **CONFIRMED.** Recomputed; L:969–973; n_analyze.py:70–77.
34. **T1:128** — CLAUDE.md `955788de…`. **CONFIRMED.**
35. **T1:129–130** — v0.1 `88d9fe7b…`. **CONFIRMED.**
36. **T1:131–135** — the seat's four raws since v0.1. **CONFIRMED.** The sha256s match, and these are exactly the design-to-code raws added in `deabf3f..fd5d61c`.
37. **T1:136–140** — the four routing raws' sha256s. **CONFIRMED.**
38. **T1:142–143** — n_sessions.py at `2834c2d`, `55885e65…`. **CONFIRMED.** It is the file's last change and equals gver.json's `pins.driver_sha256`.
39. **T1:144–146** — the package `06b55761…1d39` by `pkg_rev` over 16 `.py` blobs. **CONFIRMED.** Re-derived by my own pipeline; equals L:781 and gver.json's `pins.package_sha256`.
40. **T1:150–153** — ans22a:31. **CONFIRMED.**
41. **T1:154–155** — the chain's order; G-DATA, and G-ACQ under v0.1 §17. **CONFIRMED.** n:159; L:770–774.
42. **T1:156–158** — G-VEC at `e3b48ed`, both sha256s. **CONFIRMED.**
43. **T1:159–162** — G-CAL-n at `db00d6d`, three sha256s. **CONFIRMED.**
44. **T1:163–164** — G-ANL-n at `1641948`, `e775cbb4…`. **CONFIRMED.**
45. **T1:165–166** — "which G-TIME-n's and G-VER's identities carry". **IMPRECISE.** G-VER has no stage identity (ans22a:17); its record carries the lock in `pins.lock_sha256`. Instead: "which G-TIME-n's identity and G-VER's record (its `pins.lock_sha256`) carry:".
46. **T1:167** — G-TIME-n at `7d01b02`, COMPLETE. **CONFIRMED.**
47. **T1:168–169** — G-VER PASS at `fd5d61c`, `d1dcc337…`. **CONFIRMED.**
48. **T1:170–171** — VERDICTS refuses another lock. **CONFIRMED** at n_analyze.py:6687–6689.
49. **T1:170** — the campaign's identity will carry this file's sha256. **NOT CHECKABLE** (future).
50. **T1:172–173** — R2, "its trigger "before any read"". **IMPRECISE.** "before any read" is the row's "where" cell (header at L:541: trigger | where | …). Instead: "…is v0.1 §10's row (L:543), its "where" cell "before any read", kept verbatim below…". The reading itself is fair.
51. **T1:173–176** — the record in §1.5's words; the entry "G-VER (n)". **CONFIRMED.** gver.json: status PASS, sessions/ids/spans/n4 160, labels 4; RESULTS.md:24.
52. **T1:176–182** — the end line is stage.txt:20 (its last line) and out.txt:118. **CONFIRMED.**
53. **T1:184** — the campaign's own G-VER stays "before any read". **CONFIRMED** (ans22a:31).
54. **T1:188–189** — the analyzer is v7 at `b6ea27f`, unchanged since, `735da934…`. **CONFIRMED.**
55. **T1:190–192** — the schema pin and the four documents bound. **CONFIRMED.** n_analyze.py:3049–3050 and :70–77.
56. **T1:193–197** — VERDICTS's three reads. **CONFIRMED** at n_analyze.py:6684–6695. No other production code reads the lock's text.
57. **T1:198–199** — rt21c:32 and rt22a:34. **CONFIRMED.**
58. **T1:203–206** — 26 files, the repository, commit, tree, CC BY 4.0, SOURCE.md's sha256. **CONFIRMED.** SOURCE.md:4–6 and :9; 28 tracked files in the folder (the 26 plus SOURCE.md and SHA256SUMS).
59. **T1:207** — SHA256SUMS `359e0a12…`. **CONFIRMED.**
60. **T1:208** — `shasum -c` gives 26 lines ending ": OK". **CONFIRMED.** Exit 0, 26 OK, nothing else.
61. **T1:211–238** — the 26 rows. **CONFIRMED.** `diff` against rows rebuilt from SHA256SUMS by `sed -n`.
62. **T1:242–243** — A-n3:62. **CONFIRMED.**
63. **T1:245–247** — the whole line `lock: LOCK-n v1.0`. **CONFIRMED.** It occurs once, at T1:246.
64. **T1:249–252** — R4: the route and gate lines each occur once, as v0.1's (L:844 = T1:1160, L:935 = T1:1251), and are not restated. **CONFIRMED.** A fair reading. See Obs 5.
65. **T1:253–254** — the analyzer's reading and its refusals. **CONFIRMED** at n_analyze.py:6243–6282.
66. **T1:255–256** — v0.1's own `lock:` line (L:843); `verdicts` checks for `lock: LOCK-n v1.0` at :6248 only. **CONFIRMED.**
67. **T1 under the analyzer's lock rules** (checked by bracketed greps). **CONFIRMED.**
    - `lock_route` passes and returns B.
    - `lock_gate` passes, giving Gate(48, PASS); gcal.json has 48 coherent, pass true.
    - `lock_names` passes; the analyzer's sha256 appears in backticks at T1:189 and :834.
    - T1 has no tab, no Python-only line break, no Unicode space, and is valid UTF-8, so Python splits and strips its lines as grep does.
    - The lock-sha256 check binds whatever bytes are committed.
68. **T1:260–264** — ans21b:25 and ans21c:37. **CONFIRMED.**
69. **T1:265–267** — the row's place and the "where" cell's words. **CONFIRMED.** RESULTS.md:1651–1652 and :1663; `7d01b02` is G-TIME-n's entry commit.
70. **T1:269–278** — the exposure table. **CONFIRMED.** Nine rows are byte-equal to n:18–26; the added row matches ans21b:25; the totals are unchanged.
71. **T1:282–286** — ans21a:15. **CONFIRMED.**
72. **T1:286–288** — R1. **CONFIRMED** as to the texts; a fair reading. See Obs 4.
73. **T1:289–290** — note (a): L:430; ans20b:46. **CONFIRMED.**
74. **T1:291** — note (b): "rules every flag the sentence lists". **IMPRECISE.** ans20b §4 rules ten of L:870's eleven flags; the eleventh, `loads_ms`, is the one the sentence itself names as already ruled (A-n3:60). Instead: "…(ans20b §4) rules every flag the sentence lists as unruled; the one it names as ruled since, `loads_ms`, is A-n3:60's (v0.1 §11);".
75. **T1:292** — note (c): committed by path at `deabf3f`. **CONFIRMED.** deabf3f's message says "Committed by path".
76. **T1:293–298** — A-n3:68–71. **CONFIRMED** by `cmp`.
77. **T1:300–303** — ans22a:44–45 and rt22a:30–31. **CONFIRMED** by `cmp`.
78. **T1:307–308** — the seat reads the draft whole first, in ans22a §1.7's order. **CONFIRMED** (ans22a:35).
79. **T1:309–311** — n:159 step 13's quotation; L:3–4. **CONFIRMED.**
80. **T1:309–315** — the commit itself, and the BUILD moving the driver's pins. **NOT CHECKABLE.** The driver's `LOCK_SHA256` is still v0.1's (n_sessions.py:3820).
81. **T1:312–315** — step 14 in one pod session; the launch-file observation (RESULTS.md:180–181); step 15. **CONFIRMED.**
82. **T1:317–1374** — `cmp` against `git show fd5d61c:LOCK-n.md`. **CONFIRMED.**
83. **Completeness** — against rt21c item 4, rt22a item 3, n:120 and v0.1's deferrals (L:4, :75, :554, :587–608, :738–744, :847, :852, :948, :985, :996). **CONFIRMED,** with Obs 2.

**T2 — the entry**

84. **T2:1–3** — the routings; `5cadc821…5908`, 1374 lines; anchors at `fd5d61c`. **CONFIRMED.**
85. **T2:1, 7–10, 108** — the placement as @PLACE@ in this commit's window. **NOT CHECKABLE.**
86. **T2:3–5** — the seat's reading order; Code's readings flagged in the draft. **CONFIRMED.**
87. **T2:5–6** — committed by path; step 13 commits the draft. **NOT CHECKABLE.**
88. **T2:6** — model-free. **CONFIRMED.** No Python and no box tool in the span; the three messages went to one local session.
89. **T2:8–12** — the headline facts. **CONFIRMED.**
90. **T2:13–26** — what v1.0 carries. **CONFIRMED.**
91. **T2:28–30** — "the cap, its sum and the planning values revised". **IMPRECISE.** Only the forwards' value is revised (ans21c:23); v0.1's "cold loads 130–200 s each" (L:606–607) is not. Instead: "the cap, its sum and the forwards' planning value revised (L:554; L:587–607)". All the anchors are correct.
92. **T2:31–35** — the lock rules as the generator asserts them; "No Python read the draft". **CONFIRMED.** gen_v10.sh:66–72 and my greps.
93. **T2:36–46** — R1–R5, as to what the texts hold. **CONFIRMED.** All are fair readings. R5's premise holds: `LOCK-n.md` was first added at `deabf3f`.
94. **T2:47–48** — "by a generator (`gen_v10.sh`, `fd99927b…ea98`)". **IMPRECISE.**
    - Draft 7 was generated at 02:32:21 by an earlier version of gen_v10.sh, `8a28f414…`, as the first check run records.
    - `fd99927b…` is the script after a one-line edit at 02:34:03 that only strips `wc`'s padding.
    - Its re-run reproduces draft 7 byte for byte.
    - Instead: "by a generator (`gen_v10.sh`; draft 7 by its version before a one-line edit of its printed counts, which the edited `fd99927b…ea98` regenerates byte for byte)".
95. **T2:50–52** — the seven drafts' abbreviations. **CONFIRMED** by tool. All 15 abbreviations in T2 match their full digests.
96. **T2:53** — "2 and 3 rewrap". **IMPRECISE.** Every over-wide line did hold a 64-hex hash, and 2→3 is a pure rewrap. But 1→2 restructures: hashes moved to line ends or their own bullets, bullets added, one sentence split, no value changed. Instead: "2 restructures the sentences that a 64-character hash had widened past 120 characters (each hash to a line's end or a bullet of its own; no value changed); 3 rewraps the six lines 2 left over 120;".
97. **T2:54–57** — draft 4's changes. **IMPRECISE.**
    - Every change it lists is in the 3→4 diff. `@PKG@` was added to the generator at 02:22:15, before draft 4.
    - R3, though, was already flagged in draft 3. Draft 4 added v0.1 §11 (a)'s quotation (L:602–603).
    - The list omits:
      - the header's tool sentence, rewritten;
      - "item N.3" changed to "item 3";
      - §2's "the runner's input from the lock (ans20b:39…)", added;
      - "pins it" changed to "passes it";
      - "ans20b:46" added in §10 (a).
    - Instead: add these, and read "v0.1 §11 (a)'s words quoted beside R3" for "R3 stated".
98. **T2:58–59** — drafts 5, 6 and 7. **CONFIRMED** by `diff`.
99. **T2:61** — "on the placed bytes". **IMPRECISE.** The checks ran on L's draft 7 before any placement. Instead: "on draft 7's bytes in Code's scratch (the bytes placed), at `fd5d61c`".
100. **T2:62–66** — the checks' results: the raw's sha256, `cmp`, the width check, 48 quotations, the tail, the tools' abbreviations. **CONFIRMED.**
101. **T2:65** — "the 12 commits". **IMPRECISE.** These are 12 files and 8 distinct commits. Instead: "the 12 files the part names a commit for (eight commits), each commit the file's last change".
102. **T2:68–71** — "162 calls, 86 of them shell commands"; bracketed counts 0 and 0. **CONFIRMED.**
     - L/sweep.jsonl equals my own extraction from T byte for byte.
     - Over the whole span (to 02:36:44.676Z, the brief's hash) the commands' text holds [0] markers and [0] instances of the plain campaign-folder name.
     - The whole span is 197 calls, 104 of them Bash; after the extraction come 35 calls, 18 of them Bash.
103. **T2:72–74** — the commit window and its check. **IMPRECISE.** The six window steps and the tool check are as stated, with two exceptions. fd5d61c has 17 paths: the manifest's 16 went into `shasum`, and RESULTS.md was checked beside them. And `ps -p 8051` printed 8051 (Q-F3's campaign, alive), not none. Instead: "`git show` of the manifest's 16 paths into `shasum` and of RESULTS.md, the commit's 17th, into `shasum` and `wc -l`, …, and `ps -p 8051` (Q-F3's campaign, alive) and `pgrep -f n_sessions` (none)".
104. **T2:75** — "`sed -n` of four memory notes". **FAIL.** Three were read: one at 01:58:00 and two at 01:58:35 by a `for` loop. Instead: "`sed -n` of three memory notes, by name, after a `cd` into the memory folder (two by a `for` loop over their names; no glob there); memory edits (two notes, three edits);".
105. **T2:76–80** — the reads of committed files and the Read calls. **CONFIRMED.** LOCK-m-F0.md gave one line.
106. **T2:81–83** — "`git rev-list` … over ten named paths". **FAIL.** check_ids.sh:21–32 has twelve lines; less the report, that is eleven paths at each run. Instead: "over eleven named paths".
107. **T2:84–85** — the report's `shasum` and clean check. **CONFIRMED** (02:05:33, and the generator).
108. **T2:86–89** — `pkg_rev` and the older digest script. **CONFIRMED.** values.txt records `e3b0c442…b855`, the empty input's digest.
109. **T2:90** — `shasum -c` by a subshell's `cd`. **CONFIRMED** (02:03:42).
110. **T2:91–94** — the scratch kinds. **IMPRECISE (incomplete).** Scripts outside the four named ones also ran (see item 116). Scratch reads by `sed -n`, `head -n`, `tail -n`/`-c` and `wc -l` are not named; T2 names only `diff`, `cmp`, `od`, `cat` and `head -c`.
111. **T2:95–96** — the one narrow `git grep`. **CONFIRMED** (02:00:34).
112. **T2:97–98** — the one recursive grep. **CONFIRMED** (02:17:51).
113. **T2:99–100** — the `LOCK-m*.md` glob. **CONFIRMED.** It matches only LOCK-m-F0.md and LOCK-m-F3.md.
114. **T2:101–102** — the two zsh slips. **CONFIRMED.** At 01:59:13 zsh printed "===A-n3 not found"; at 02:03:07 there is `awk_never=0` before `sed`.
115. **T2:104** — "No Python ran; nothing went to the box". **CONFIRMED** for the commands. The scripts the brief did not name were not read.
116. **T2:104** — "Code knows of no others", i.e. the list is complete. **FAIL.** These kinds are not covered:
     - 01:48:41: the G-VER entry's edits-check script, run by `bash`.
     - 01:50:33: the G-VER entry's commit-build script, run by `bash`.
     - 01:50:45: `rm -r` of that entry's scratch commit folder, then a second build run.
     - 01:50:56: a `sed` redirect writing the commit message, and `wc -c` of it.
     - 01:51:03: the message-check script, run outside the window.
     - 01:51:09: the dry gate's output redirected into a scratch file.
     - 01:51:31: `git show HEAD:RESULTS.md` into `cmp`, before the window.
     - 01:52:22: the window-request fill script (uncovered unless it is what T2 means by "the fill script").
     - 02:03:26: `mkdir -p` and a `printf` redirect writing a notes file in L.
     - 02:03:42: a redirect writing L/values.txt.
     - 02:05:33: an append of the report's digest to a note in L.
     - 02:25:07: the redirect writing L/sweep.jsonl.
     - 02:33:51 and 02:34:05: L/make_check_raw.sh, run by `bash`.
     - 02:34:05: `rm` of the check raw and L/regen_draft7.md before re-making them.
     - Redirects to `/dev/null` at 01:58:20, 01:58:35, 02:03:42, 02:17:51, 02:18:35 and 02:23:12.
     - Scratch reads by `sed -n`, `head -n`, `tail` and `wc -l` at 01:50:12, 01:50:33, 02:18:54, 02:23:12, 02:24:25, 02:24:32, 02:24:47, 02:26:37, 02:34:15, 02:36:38 and 02:36:44.

     No loop, variable or glob passed a marker-named path. I checked the 16-path manifest loop (fd5d61c's paths hold no marker), the 28-path loop, the scratch glob (it expanded to S/step4b/schema/pkgsha.sh only) and the root glob. Instead: add these kinds, and keep "Code knows of no others" only after them.
117. **T2:106–110** — the remaining plans. **NOT CHECKABLE.**

**T3 — the checks raw**

118. **T3:1** — the title line. **CONFIRMED.**
119. **T3:3** — the draft's sha256, 1374 lines = 316 + 1058. **CONFIRMED.**
120. **T3:5–10** — the six tools' sha256s. **CONFIRMED.**
121. **T3:14–15** — the re-run's lines. **CONFIRMED.** regen_draft7.md is `5cadc821…`; the analyzer's rules were re-derived by grep.
122. **T3:16** — "gen exit: 0". **CONFIRMED** by consequence: the generator moves its output into place only after every assertion passes, and the re-run file exists and is equal.
123. **T3:17** — `cmp` equal. **CONFIRMED.**
124. **T3:21** — no over-wide line. **CONFIRMED.** Re-derived; only table rows and blockquotes exceed 120 characters.
125. **T3:25–27** — 316 lines; 48 quotations found, 0 not; exit 0. **CONFIRMED** by my own in-shell match.
126. **T3:31–32** — 12 last changes, 0 not; exit 0. **CONFIRMED.** By `git log` for 11 files; by digest for the report.
127. **T3:36** — the tail. **CONFIRMED.**

## TOTALS

| Verdict | Count |
|---|---|
| CONFIRMED | 104 |
| IMPRECISE | 11 |
| FAIL | 3 |
| NOT CHECKABLE | 9 |

## OBSERVATIONS

1. **Form.** LOCK-m-F3 v1.0 ends its part with `---` and a precedence sentence: where the earlier text differs, v1.0 is of record (LOCK-m-F3.md:319–321). T1 has neither between T1:315 and :317. v0.1's text below keeps its status line (L:3–4), `lock: LOCK-n v0.1` and the three sentences that §10 corrects. LOCK-m-F3 v1.0 also had sections for Code's readings (§11) and for how the campaign cites the lock (§12); T1 has neither.
2. **Completeness.** G-TIME-n's load figure (12,375 ms per invocation; ans21c:26) is not in T1 §1. It revises v0.1's "cold loads 130–200 s" (L:605–608), and rt21c item 1 says v1.0 carries "the figures of §1.2–§1.4". A question for the seat.
3. **R3 is a seat ruling, not only Code's reading.** ans21b:23 ruled that the fits, run on the laptop, are outside the cap.
4. **R1 has more support** than T1 cites: ans21a:8 ("LOCK-n v1.0 carries the corrected words") and ans21a:40.
5. **R4 has an alternative.**
   - The analyzer counts only stripped lines that start with each head (n_analyze.py:6250, :6269); a blockquoted line is not counted (:6264–6265).
   - So v1.0 §8 could quote the three lines together in a blockquote without a second whole line.
   - T2's "refuses … two of either" holds for whole lines only.
   - ans20b:50 and :6259–6260 support R4.
6. **R2's numbering.** The seat's "v1.0's §10" is v0.1's numbering; T1's own v1.0 §10 is the dated notes. One clause would keep them apart.
7. **R5.** Placing the draft over the tracked `LOCK-n.md` would make the driver's lock checks refuse on this tree until the commit (n_sessions.py:3913, :5167). RESULTS.md:49 and ans21c:11 both say "untracked at the root".
8. **The committed bytes.** The status line changes at the commit (T1:309–311), so the lock's sha256 of record will not be draft 7's. For v0.1, the seat set the committed status line's words in advance (ans20b:18). Stating v1.0's committed status line would let the seat's read cover those bytes.
9. **T3 was made twice.** The 02:33:51 raw (`ddfdce0a…`, under gen_v10.sh `8a28f414…`) was removed at 02:34:05, after the 02:34:03 edit, and re-made as T3. Neither T2 nor T3 says so.
10. **The plain campaign-folder name appeared in Code's tool output** in four Bash outputs: 01:58:35 [1], 02:01:23 [3], 02:23:12 [1] and 02:27:08 [3]. Earlier raws declared outputs of this kind (ans21b:48 (d)). Marker words appear in several outputs only, never in an argv.
11. **File-tool calls in scratch.** T2 is silent on Code's Write, Edit and Read calls in scratch.
12. **Pre-window steps.** The 01:48:41–01:52:22 commands prepared fd5d61c's commit after that entry's final sweep. Only T2 can declare them, and it does not.

## DEPARTURES

1. **Device redirects, four, no file written:**
   - `>/dev/null 2>&1` on the BK `shasum -c` run;
   - `>/dev/stdout` before a pipe, which zsh duplicated; I discarded that count and redid it;
   - `>/dev/fd/2 2>&1` on a `diff`;
   - `>/dev/null` on a `jq`.
2. One `git show --name-only --format= fd5d61c` run without item 3's pathspec; only its count (17) was printed.
3. One environment assignment named `awk_free=1` before a `cut`; no awk ran.
4. **Two prints from T beyond what a finding needed:**
   - a lookup keyed on the time of day alone, which matched another day's record and printed an unrelated harness summary;
   - 02:23:12's result, which printed two LOCK-m-F3.md lines, one naming the campaign folder's package path plainly (output only).
5. **Tools beyond the brief's four on files that hold the marker, by their own paths:**
   - `wc -l` on T1, T3, the stage raw and SHA256SUMS;
   - `tail -c 1` on T1 and the stage raw;
   - a `head -c 0` on T1, which failed with a usage error and printed nothing;
   - `iconv` into `cmp` on T1.
6. **Reads at another commit:**
   - `git show deabf3f:LOCK-n.md` into `shasum`;
   - `git log -1 --format=%B deabf3f` into a bracketed `grep -o`, a commit-body read beyond ids, subjects and times.
7. `wc -c` of the sixteen `valence_core/n` `.py` blobs (taken via `git show fd5d61c:`) to re-derive the package digest. None of them is in a closed folder.

No interpreter beyond `shasum` and `jq` ran, no file was written, and nothing went over the network.
```
