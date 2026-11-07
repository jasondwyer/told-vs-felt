# G-ANL-F3 build: blind values-check of the build design and the entry (Code's raw, 2026-11-06)

*A blind values-check agent (fresh context, read-only) checked Code's build-design raw (`results/raw/2026-11-06_ganl-f3_build_design.md`, as drafted) and the RESULTS.md entry's draft against their sources. Its sources were the code in Code's scratch worktree, the repository at HEAD (54bbfe5, then 0415438 and e7e070f), and the run outputs. Four passes ran, the first three each a fresh agent:*
- *the first, on the drafts and the code as first built;*
- *the second, on the corrections and the changes made on the blind code review;*
- *the third, on the texts written after the second (with the commit message and Code's dispositions of the second pass). It also reviewed the last code delta, the follow-up review's fixes, which no reviewer had yet read. After it started, the site check found N12, and Code sent it the new texts as further items;*
- *the fourth, the third pass's agent again, on Code's fixes for its four code NOTEs and on the texts changed on its report.*

*The reports follow verbatim, local paths scrubbed (`<tmp>` = Code's session scratch), each followed by Code's dispositions. The scratch commits the reports name (69ff08d, 5f9a696, 54c9d64, bcd15c9, 8e2cec3) are detached commits in Code's scratch worktree and are not in the repository's history. The BUILD commit's five files are byte-identical to 8e2cec3's (sha256 in the selftest raw).*

## 1. The first pass (verbatim)

116 items: 96 CONFIRMED, 2 FAIL, 14 IMPRECISE, 4 NOT CHECKABLE

How I checked: I only read. I did not touch the repository or the worktree. Throwaway helper scripts went in my own scratch folder (vc_build), and no bytecode was left in the worktree. The worktree's HEAD is the scratch commit 69ff08d, and its working tree equals that commit; the diffs below are against 273ca8f. I re-ran the following myself, outside the battery:
- the regression: both outputs byte-identical (ec7d2082…, 81,084 bytes; dcaaaac3…, 12,052 bytes);
- the v1-unchanged check: 2,160 equal, 2,160 equal with distinct reasons, tables equal;
- the regression without the preprint blob: AnlRefusal at V1, with neither the campaign nor the OLMo-states file opened;
- `table_problems` at HEAD on both analyzers;
- `closure()` with and without the lazy F3 modules;
- both package hashes, now and at 273ca8f;
- the v2 placeholder file against the builder's bytes.

Main's HEAD moved during the check. It went from 54bbfe5 to 0415438 through three commits from a parallel session: 6ce8b9a (G-CAL-OLMo: condition (4) fails on all three checkpoints, each NOT-RUN "dose not completable", escalated to the seat, "No LOCK-m-OLMo written"), 3b22158 and 0415438. I re-checked every "at HEAD" claim at 0415438. Item 115 is stale because of this; nothing else changed.

DESIGN RAW (results/raw/2026-11-06_ganl-f3_build_design.md, as drafted)

Header
1. Answers path, sha256 4edfbb8e…ca42e — CONFIRMED.
2. The STOP's close is at 54bbfe5 — CONFIRMED (its commit message).
3. The relay quote "G-ANL-F3, to A1–A5: Build it in scratch, per C1. Apply B as written." — NOT CHECKABLE. It is a chat relay. Only "Apply B as written" is on record (the close line at RESULTS.md@54bbfe5:212; referent check N3).
4. No LOCK-m-OLMo-*.md exists — CONFIRMED at 0415438, both in the tree and in the index. The re-check "immediately before the commit" lies in the future.
5. m = PROPOSAL-m v1.11, sha256 42ab36ec…6c6b — CONFIRMED.
6. A-m1 sha256 ea08322d…9001 — CONFIRMED.

§1 A1
7. `_bt_qf0_regression` runs Q-F0's VERDICTS and secondary computations in-process through `run_verdicts` — CONFIRMED.
8. `git cat-file blob ed8e886:scripts/m_analyze.py` hashes to 655e0f7f…c16f (`RECORD_ANALYZER_SHA256`) — CONFIRMED.
9. LOCK-m-F0.md:147–149 names the package 5f646db6…d771 and the closure a3bc7bb9…b22b — CONFIRMED.
10. PIN-14 runs inside `run_verdicts` against those three, and the lock names all three — CONFIRMED.
11. `inputs.lock` is LOCK-m-F0.md as the record has it (fc7e9db8…, equal to HEAD's file) — CONFIRMED.
12. Temp directory; byte-for-byte; both identical; the shas and byte counts — CONFIRMED (re-run).
13. A difference fails the check, and the battery's STOP writes nothing (`run_ganl`, exit 4) — CONFIRMED.
14. `REGRESSION_REPORT` is in the artifact's g_anl_f3 block; its shows / does-not-show text and PIN-42 — CONFIRMED.
15. `PIN29_RELEASED`, `_OpenHook._check` / `_blob_ok`; each of the seven pins equals HEAD's blob (recomputed) — CONFIRMED.
16. `BLOCKED_REL` gains the three mf3 roots; `_bt_snapshot` covers data/mf3 — CONFIRMED.
17. The hook checks in both directions (battery lines 451–452) — CONFIRMED.
18. `_bt_v1_unchanged`: the record blob is exec'd as a module; 2,160 evaluations; two reason sets; the tables are equal — CONFIRMED (re-run).

§1 A2
19. `check_tuple_v2` raises `PendingAtV2` with `PENDING_AT_V2`, which quotes m:324 and both branches — CONFIRMED.
20. 481×5×91 = 218,855 refusals and 481×5×125 = 300,625 full, per flag value — CONFIRMED.
21. `not-run --v2-closure`: pending-closed-at-v2 only; refused without the flag; refused for Q-F0 (the cause is olmo-only) — CONFIRMED.
22. `crosscheck_coordinate(v2=True)` admits pending-closed-at-v2 and refuses PENDING — CONFIRMED.

§1 A3
23. `run_verdicts_f3` is dispatched after V0's gate line — CONFIRMED.
24. The V1 refusal list (proposal, Clock, committed analyzer and lock, the lock naming three shas with the Q-F3 closure, the v1 of-record output, the adjudication-reads file) — CONFIRMED.
25. V2: `_campaign_structure` plus the six-arm floors — CONFIRMED.
26. V3 `f3rr.release_full`; V4 `_f3_check_record` STOP; V5 `f3_unit_state` — CONFIRMED.
27. V6–V7 per contrast arm (outcome, power, sentence, rates and tests, guard at the last look); `f3_beside_blocks` per arm — CONFIRMED.
28. The outputs are written once in data/mf3/verdicts; the secondary carries (a)–(f) — CONFIRMED.
29. `run_posting_v2`, `crosscheck_f3`, `table_problems(posting="v2")`, the output names, `posting_comparator_v2`, `rewrite_ids(posting="v2")` — CONFIRMED.
30. The v2 placeholder: 21 v1 rows plus P22–P26; theses on P25 (main) and P26 (fallback-1); the file equals the builder's bytes (cd3df574…) — CONFIRMED.
31. 519,480 tuples asserted per flag value; `_bt_oracle_v2` is a second implementation; V1–V12 per flag value — CONFIRMED.
32. A3*: 30,000×3 / 10,000 / 40,000×2 / 120,000 / 625 — CONFIRMED (re-derived: per A1×A2 pair, no-hit 1 each, CONFIRMED 4, DISCORDANT 4, null-class under PASS 2 each, UNLICENSED 12, all ×625).
33. Ceiling: Main 375, Fallback-1 21,250, Fallback-2 279,000 — CONFIRMED (re-derived from m:341).
34. Withholding 40,625 / 240,000 / 20,000 and the v1-note's six values — CONFIRMED (re-derived).
35. L1 75,000; §8.2 closed 1,875; Step 6 "none" 225,625 — CONFIRMED.
36. The 26 rows' fires (`PLACEHOLDER_FIRES_V2`), `BTREAT_V2`, the second-pass sha — CONFIRMED.
37. "this is the analyzer's one hash-moving round while an OLMo unit is open" — FAIL. See below.

§1 A4
38. `_prod_committed` decides "outside" from the resolved path — CONFIRMED.
39. "main resolves every path argument against the repository root (_cli_path)" — IMPRECISE.
40. A relative --flag-source reads TRUE; `stages._committed` is unchanged (valence_core/m is untouched) — CONFIRMED.
41. D1 = CLOCK_DATE 2026-10-30 (unchanged since 273ca8f), D_O_PRIME 2026-11-30, D2 2026-12-22 — CONFIRMED.
42. `clock_problems` (A-m1:28, :40, `ADDENDUM_M1_SHA256`); `constants_by_line` m:16; PIN-31 — CONFIRMED.
43. `_clock_refusal` runs in `run_verdicts`, `run_verdicts_f3` and `analyzer_binding` (not-run, both postings) — CONFIRMED.
44. `clock_of_record`; `date_is_clock_of_record`; `pending_era` / PIN-V2-10 — CONFIRMED.

§1 A5, B
45. Built as STOP §3 has it, with both notes (`F3_SENTENCE["null"]`, `pending_state`). I spot-checked items 1, 2, 3, 4, 5, 6, 7, 9 and 11 — CONFIRMED.
46. PIN-V2-1 to PIN-V2-23 — CONFIRMED.
47. F-6 applied on "Apply B as written" — CONFIRMED.
48. No per-line list (`strip_contrast`, `TIME_SESSION_KEYS`, `_contrast_block_time`) — CONFIRMED.
49. "CAP TRIGGER …: k of <= 36 …" attributed to `stages.cap_trigger` — IMPRECISE.
50. Contrast booleans and totals stay in the checkpoint — CONFIRMED.
51. Sham per-line cap_hit is in the reads file — IMPRECISE (it is Code's reading of the seat's "in the report").
52. The readrule and stages docstrings — CONFIRMED.
53. F-7: `GID_CRITERION`; `_gid_pair` requires both; FAIL sends Q-F3 uncached; the self-test asserts it — CONFIRMED.
54. The seat PIN is set at v0.1, before G-ID-F3 — CONFIRMED (the seat's F-7 words).
55. F-1 to F-5 and finding 3 need no change; mf3's `announce_stop` already names a line-1 bar — CONFIRMED.

§2
56. `PINS_F3` site↔entry check (set equality, planted control) — CONFIRMED.
57. "its site is a … comment" — IMPRECISE.
58. Strikable until v1.0 (answers:50) — CONFIRMED.
59. The 23 table subjects match `PINS_F3` — CONFIRMED.
60. `SEAT_RULED_F3` A1–A5 — CONFIRMED.
61. Two PIN-29 sites (m_analyze.py:112, :4943) carry the marker; the PI's "[acknowledged]" is at RESULTS.md@54bbfe5:240 — CONFIRMED.

§3
62. N1: the banner since 32aefcc; 5d677a72…4467; "not a text of record" — CONFIRMED.
63. The table binds 45b67246…7a41 / 88,668 / 468; LOCK-m-F0 names it (:204, :414; PIN-40) — CONFIRMED.
64. `table_problems` refuses at HEAD — CONFIRMED (run).
65. The 1523cce blob is served and asserted — CONFIRMED.
66. "This is the same reading the seat gave the analyzer blob" — IMPRECISE.
67. With the blob both outputs reproduce; without it the run refuses before computing — CONFIRMED (run).
68. The FLAG: v1 posting and a Q-F0 verdicts re-run refuse at HEAD on both analyzers, with that message — CONFIRMED.
69. The quotes "No other change to the analyzer is licensed" (A-m1:44) and "Nothing else rides" — CONFIRMED.
70. N2: nine values become m:340's seven; STOP §3 item 3 was corrected by its values-check, not struck — CONFIRMED.
71. "The list is read only for a decision naming Q-F3's other_state" — IMPRECISE (minor).
72. N3: mf3's package moves 44110d15…3842 to f30ad505…6310 on these bytes; the three files are in G-SHAPE-F3's 38-file sources map — CONFIRMED.
73. N3 is the referent check's N3 as amended (values-check items 65, 67, 68, 76) — CONFIRMED.
74. N4: the search and its null result reproduce — CONFIRMED.
75. round2.md:19, "accepted as the entry lists them" — CONFIRMED.
76. FID-3 and FID-6 "For v1.0's notes" (review raw :2280–2284) — CONFIRMED.
77. RESULTS.md@54bbfe5:4296–4304 — IMPRECISE (anchor).
78. RESULTS.md@54bbfe5:2569–2575, the R2 3 round of 2026-10-14 — CONFIRMED.
79. "Nothing else rides"; not a completeness proof — CONFIRMED.
80. N5: the posting / v2 keyword defaults are v1's — CONFIRMED.
81. "V2 block moved into _campaign_structure unchanged" — IMPRECISE (minor).
82. `production_env()` takes no argument except for Q-F3 — CONFIRMED.
83. Base closure a3bc7bb9…b22b, recomputed — CONFIRMED.
84. The v1 groups, regression and v1-unchanged checks pass (525/525) — CONFIRMED.
85. N6: the A-m1:40 quote; POSTING-v1_outputs.of-record.json — CONFIRMED.
86. N7: m:340, "f2 is written then" — CONFIRMED.
87. N8: the key is in the secondary; m:312 "reports agreement with the rule" — CONFIRMED.
88. N9: 845/846 (sitecheck_out/m_sessions.txt) — CONFIRMED.
89. The failing check's text; the case "a lock-named non-proposal" (m_sessions.py:4478) passes scripts/m_analyze.py and expects "startup: banner" — CONFIRMED.
90. 16b56512… is not in LOCK-m-F0, which binds 655e0f7f…; the refusal message is lock §1's — CONFIRMED.
91. "Q-F0's drivers refuse an analyzer their lock does not bind" — IMPRECISE.
92. Any in-place G-ANL-F3 commit moves the premise, under (a) or (b) — CONFIRMED.
93. TOOLING_FILES entry (m gshape.py:105) — CONFIRMED; "so under the step-10 read's Q2 the change re-runs G-SHAPE-F0" — IMPRECISE (anchor). Counted once, as IMPRECISE.
94. The other nine suites pass (ganl/sitecheck_final_summary.txt) — CONFIRMED.

§4
95. 525/525; 538 ids; G-ANL-F0 448 and 461 (LOCK-m-F0 v1.0 §1); EXPECTED_CHECKS 525 — CONFIRMED.
96. Q-F3 closure d19f336d…f039: 22 modules, 15 plus the 7 named — CONFIRMED (recomputed).
97. m's package 60199b36…feec, unchanged — CONFIRMED.
98. "see the site-check raw" and "the raws beside this one are verbatim, paths scrubbed" — NOT CHECKABLE (not written yet). Scratch shows the mf3 module self-tests at 124/124 and the final site check at 9 of 10.

ENTRY DRAFT
99. Heading: m:291; A-m1 §2.5; A1–A5 and B; in place; F-6 and F-7 to mf3; order (a) — CONFIRMED.
100. A1's regression holds as stated — CONFIRMED.
101. All 519,480 asserted — CONFIRMED.
102. "One FLAG goes to the seat (N1 below)." — FAIL.
103. "No LOCK-m-OLMo-*.md existed at the commit"; "Not pushed" — NOT CHECKABLE (commit-time). Both are true at 0415438.
104. The relay quote — NOT CHECKABLE (as item 3).
105. "Order (a) with the second-STOP flip (C1); no second STOP was needed." — IMPRECISE.
106. The A1 bullet — CONFIRMED.
107. The A2 bullet's "The closure runs upstream (`not-run --v2-closure`)" — IMPRECISE.
108. The A3 bullet (seed 20261106, outputs, placeholder path) — CONFIRMED.
109. The A4 and A5 bullet — CONFIRMED. "At every run" holds for D1/D2 against m:16 only through the sha256-pinned proposal, which the parenthesis says.
110. The B bullet — CONFIRMED.
111. The hashes: m's package unchanged; base closure unchanged, so no mf3 byte; mf3's package moved from 44110d15…3842 — CONFIRMED.
112. The FLAG (N1) paragraph — CONFIRMED.
113. The dated-notes summary N1–N8 — IMPRECISE (it omits N9).
114. Next: the canonical ganl run writes G-ANL-F3.json in its own commit; G-ANL-F0.json is untouched — CONFIRMED.
115. "Then the first LOCK-m-OLMo-{ckpt} v0.1 may name this analyzer (order (a); the pod session's)." — IMPRECISE (stale).
116. LOCK-m-F3 v0.1 names this analyzer and its lexicons (m:292) and the re-run G-SHAPE-F3, and waits for the coordinating session's word (referent check N3) — CONFIRMED.

FAIL items and corrections

37. Source:
- answers:26: "G-ANL-F3's in-place commit lands only when no OLMo unit is open — "open" from its LOCK v0.1 to its VERDICTS entry".
- The answers' A3: "One hash-moving round, not two: … no in-place analyzer commit while an OLMo unit is open".
- `SEAT_RULED_F3["A3"]` states it correctly.

The draft says this round happens "while an OLMo unit is open", the opposite of the seat's rule.

Corrected: "**The one-round rule** (answers:26; the answers' A3): one hash-moving round, not two, and no in-place analyzer commit while an OLMo unit is open ("open" from its LOCK v0.1 to its VERDICTS entry). This round lands before any OLMo lock (order (a))."

102. Source: the design raw's §3 now has two FLAGs, N1 and N9. The final site check is 9 of 10 (m_sessions 845/846).

Corrected: "Two FLAGs go to the seat, neither adjudicated: N1 (the preprint of record at HEAD) and N9 (`scripts/m_sessions.py --selftest` is 845/846 on this analyzer: its "a lock-named non-proposal" case expects the banner refusal, and LOCK-m-F0 does not name the extended analyzer)."

@@SITE@@ must then read: nine of ten pass; m_sessions 845/846 (N9).

IMPRECISE items and corrections

39. ganl's --out is not passed through `_cli_path`. It resolves against the working directory (`run_ganl`, `resume.refuse_canonical_out`).

Corrected: "main resolves every path argument of verdicts, not-run and posting against the repository root (`_cli_path`); ganl's --out, a non-canonical test directory, resolves as before."

The same overstatement is in `PINS_F3["PIN-V2-8"]` and in PIN-V2-8's site comment in `_prod_committed`, which are analyzer bytes. Correcting them is Code's call.

49. The line is printed by `stages._finish_gate`, not by `cap_trigger`.

Corrected: "(printed by `stages._finish_gate` from `stages.cap_trigger`'s report, which has no `lines` key)".

51. Source: the seat's F-6 says "Sham sessions keep their per-line booleans in the report (nothing of theirs is withheld)". In the build the per-line booleans are in the stage's reads file (`redact_sham`, `_LINE_KEEP`). The report's sham block (`_sham_block` → `line_counts`) carries counts only, and B's edits did not change it.

Corrected: "A sham session withholds nothing: each line's `cap_hit` is in the stage's reads file (`readrule.redact_sham`, `_LINE_KEEP`), and the report's sham block carries the counts. Code reads the seat's "in the report" as met by the reads file (Code's reading)."

57. PIN-V2-9 has two sites: m_analyze.py:131 (the constants) and :562 (`clock_problems`). The battery compares sets, so it does not count sites.

Corrected: "each has at least one site, a `# PIN (Code, declared at LOCK-m-F3 v0.1 …): PIN-V2-n --` comment (PIN-V2-9 two)".

66. The seat ruled on the analyzer blob only. Applying the same reasoning to the preprint is Code's analogy and should be labelled as such.

Corrected: "This is Code's reading (PIN-V2-11), by analogy with the seat's A1 on the analyzer blob ("no blob but `655e0f7f…` can satisfy LOCK-m-F0's binding"): no preprint blob but 1523cce's can satisfy the table's binding."

71. The G-ANL-F3 manifest also records the list (`decisions_other_states`), and the battery reads it (F3O-A3STAR).

Corrected: "On the verdicts and not-run paths the list is read only for a decision naming Q-F3's other_state; the G-ANL-F3 manifest also records it."

77. "No ruling schedules their correction" is at :4293, and "and when they are corrected is open" is at :4305. Both fall outside the cited range.

Corrected anchor: `RESULTS.md@54bbfe5:4290–4305`.

81. The moved code is unchanged apart from parameter names (campaign, adjudication, pi_stop, allow_stub, olmo). The old V2 block's floors and gate-checkpoint checks stay in `run_verdicts`.

Corrected: "`run_verdicts`' V2 checkpoint-structure refusals moved into `_campaign_structure` unchanged but for parameter names; the floors and gate-checkpoint checks stay in `run_verdicts`, unchanged."

91. The refusal that fires is lock §1's proposal binding (m_sessions.py:917–920, "(lock §1 binds the proposal of record)"), applied to the analyzer file passed as `--proposal-file`. It is not an analyzer binding check; licence (f) is that check.

Corrected: "Code's reading: the driver's behaviour is right — it refuses a `--proposal-file` whose sha256 LOCK-m-F0's committed text does not name in full (lock §1), and the extended analyzer's sha256 is not named there; Q-F0's stages are finished."

93. The step-10 read's Q2 (G-TIME-F0_read.md:45) clears only an edit that wires a subcommand. The re-run follows from PIN-S10, which Q2 leaves unamended.

Corrected: "That file is a TOOLING_FILES entry; the step-10 read's Q2 clears only a subcommand-wiring edit, so under PIN-S10 ("any difference re-runs G-SHAPE-F0 first", valence_core/m/gshape.py:233–236) the change re-runs G-SHAPE-F0."

105. "no second STOP was needed" is Code's judgement, and N9 bears on it. A site-check suite fails; the BUILD (F3) precedent had all ten pass; and the PI's routing says "STOP on anything unresolved; minor residues as dated notes" (RESULTS.md@54bbfe5:241). The design raw's §3 heading, "minor residues", also covers two FLAGs.

Corrected: "Order (a) with the second-STOP flip (C1). Code's reading: no second STOP; N1 and N9 go to the seat as FLAGs."

107. Source: the seat's A2: "as a PI-stop record or a NOT-RUN record". `not-run --v2-closure` covers only the no-session branch.

Corrected: "The closure runs upstream: a PI stop through the campaign driver for a checkpoint with sessions, `not-run --v2-closure` for one with none."

113. Add: "N9 FLAG: `scripts/m_sessions.py --selftest` 845/846 on this analyzer ("a lock-named non-proposal")."

115. Stale against the record. 6ce8b9a (committed after 54bbfe5) records G-CAL-OLMo's condition (4) failing on all three checkpoints: each is NOT-RUN "dose not completable", escalated to the seat, "No LOCK-m-OLMo written".

Corrected: "An OLMo lock follows only if the seat's adjudication of G-CAL-OLMo (6ce8b9a) leaves a checkpoint to lock; if one is written, it names this analyzer (order (a))."

Observations (not counted)
- answers:50 says each Code PIN "is listed as a flag in the BUILD entry". The entry draft gives the PIN-V2 register only by reference to the design raw.
- The battery and site check ran in the scratch worktree, which is based on 273ca8f. Main is now at 0415438, which adds committed files under data/m/ckpt and data/m/gates. They are outside what the analyzer reads, but the canonical runs will be on the new HEAD.

### Code's dispositions of the first pass

Each item marked FAIL, IMPRECISE or NOT CHECKABLE was re-checked at source before acting. The 96 CONFIRMED items need no change, except where the review's fixes changed the code (§1 below names those claims, re-checked in the second pass).

| Item | Verdict | Re-checked at source | Disposition |
|---|---|---|---|
| 37 | FAIL | answers:26 ("lands only when no OLMo unit is open"); the answers' A3 ("no in-place analyzer commit while an OLMo unit is open"). | Applied. The one-round rule now reads as the seat's, and adds that after `6ce8b9a` an OLMo lock follows only if the seat's adjudication leaves a checkpoint to lock. |
| 102 | FAIL | The design raw's §3 carries N1 and N9; the final site check is 9 of 10. | Applied, before this pass ended (the PI ruled on N9 meanwhile). The entry names two FLAGs and quotes the PI's ruling. |
| 3, 104 | NOT CHECKABLE | The relay is in the coordinating session's message, not a file. | Labelled "in its message, not a file". |
| 39 | IMPRECISE | ganl's `--out` was not passed through `_cli_path`. | Fixed in code instead: the review's NOTE 8 routes ganl's `--out` through `_cli_path`, so "every path argument" now holds. PIN-V2-8's text says "(ganl's --out included; an empty argument as before)". |
| 49 | IMPRECISE | `stages._finish_gate` prints the CAP TRIGGER line from `cap_trigger`'s report. | Applied as proposed. |
| 51 | IMPRECISE | The seat's F-6: "in the report"; the build keeps the booleans in the reads file. | Applied as proposed, labelled as Code's reading. |
| 57 | IMPRECISE | PIN-V2-9 has two sites. | Applied: "at least one site … (PIN-V2-9 two)"; the battery's check text says "at least one site" too. |
| 66 | IMPRECISE | The seat ruled on the analyzer blob only. | Applied as proposed (Code's reading, PIN-V2-11, by analogy). |
| 71 | IMPRECISE | The manifest records the list too. | Applied as proposed. |
| 77 | IMPRECISE | The passage runs RESULTS.md@54bbfe5:4290–4305. | Applied. |
| 81 | IMPRECISE | The floors and gate-checkpoint checks stay in `run_verdicts`. | Applied as proposed, in N5 and in A3's V2 line. |
| 91 | IMPRECISE | m_sessions.py:917–920: lock §1 binds the proposal of record; the analyzer file is passed as `--proposal-file`. | Applied, labelled as Code's reading. |
| 93 | IMPRECISE | G-TIME-F0_read.md:45 clears only a subcommand-wiring edit; PIN-S10 is `valence_core/m/gshape.py:233–236`. | Applied as proposed. |
| 105 | IMPRECISE | The judgement is Code's; the PI has since ruled on N9. | Applied: "Code's reading: no second STOP; N1 and N9 go to the seat as FLAGs, and on N9 the PI ruled 'Commit with flag'". |
| 107 | IMPRECISE | The seat's A2: "as a PI-stop record or a NOT-RUN record". | Applied, in the entry and in the design raw's A2 (with the review's finding 4: the no-session check). |
| 113 | IMPRECISE | The summary omitted N9. | Applied (N9 and the new N10). |
| 115 | IMPRECISE | 6ce8b9a records G-CAL-OLMo's condition (4) failing on all three checkpoints. | Applied as proposed. |
| 98, 103 | NOT CHECKABLE | Not yet written, or true only at commit time. | The raws are written at the commit. The LOCK-m-OLMo check is re-run immediately before it. |
| Obs. 1 | — | answers:50: "is listed as a flag in the BUILD entry". | Applied: the entry lists PIN-V2-1 to -24 as flags, with their subjects and the cost of striking one. |
| Obs. 2 | — | HEAD moved to 0415438 with data-only commits. | The canonical `ganl` run is on the new HEAD after the commit. `git diff --name-only 273ca8f 0415438` shows no code file changed. |

## 2. The second pass (verbatim)

49 items: 41 CONFIRMED, 1 FAIL, 6 IMPRECISE, 1 NOT CHECKABLE

What this pass covers: the code at scratch commit 5f9a696 in the worktree, with the analyzer at sha256 ec7ea234…, matching selftest_g.sha. The drafts as of 22:38. I read the full 69ff08d..5f9a696 diff, which touches scripts/m_analyze.py only.

What I re-ran myself on the final bytes:
- The regression is byte-identical (ec7d2082…, 81,084 bytes; dcaaaac3…, 12,052 bytes).
- The v1-unchanged check is 2,160 / 2,160 / 2,160 and the tables are equal.
- The base closure is a3bc7bb9… with 15 modules. The Q-F3 closure is d19f336d… with 22. m's package is 60199b36…, mf3's is f30ad505….
- The v2 placeholder file equals its builder.
- Every S6_* text is on m:342.
- `PINS_F3` has 24 ids; every id has one site except PIN-V2-9, which has two.
- The scorer's four review cases give the values the battery asserts.
- Step 6's texts, old against new, over all tuples.

selftest_g has 525 PASS and 0 FAIL. The second site check (sitecheck_final2_summary.txt) gives nine suites PASS and m_sessions FAIL at 845/846; the failing case quotes "its sha256 ec7ea234a6c1f252…".

(a) The earlier FAIL and IMPRECISE items, as now worded
1. Item 37, the one-round rule. CONFIRMED. It now reads as answers:26 and the answers' A3. The added clause on 6ce8b9a is supported (no LOCK-m-OLMo at 0415438).
2. Item 102, "Two FLAGs go to the seat (N1 and N9 below)". CONFIRMED. The PI's ruling is item 17.
3. Item 39, A4 (1). CONFIRMED, now true in the code: `main` passes ganl's --out through `_cli_path` unless it is empty or whitespace, and `run_ganl` still refuses an empty one. PIN-V2-8's text was updated to match.
4. Item 49, the CAP TRIGGER line printed by `_finish_gate`. CONFIRMED.
5. Item 51, the sham booleans sit in the reads file, labelled Code's reading. CONFIRMED.
6. Item 57, "at least one site … (PIN-V2-9 two)". CONFIRMED (counted).
7. Item 66, N1's analogy. CONFIRMED. The quote matches the seat's A1 exactly.
8. Item 71, N2. CONFIRMED.
9. Item 77, N4's anchor RESULTS.md@54bbfe5:4290–4305. CONFIRMED.
10. Item 81, N5 and A3's V2 line. CONFIRMED.
11. Item 91, the design raw's N9 reading. CONFIRMED, but the entry's N9 block repeats the old wording (item 44).
12. Item 93, the design raw's PIN-S10 anchor (valence_core/m/gshape.py:233–236). CONFIRMED, but the entry repeats the old anchor (item 45).
13. Item 105, the routing labelled as Code's reading. CONFIRMED.
14. Item 107, the two closure branches, in both drafts. CONFIRMED.
15. Item 113, the notes summary now has N9 and N10. CONFIRMED.
16. Item 115, the entry's Next line on the OLMo lock. CONFIRMED.

(b) Claims added or changed
17. The PI's ruling on N9, "Commit with flag", in the design raw's header and N9 and in the entry's header, routing and N9 block. NOT CHECKABLE: it is a chat relay and is in no file except the drafts.
18. The header's review tally: no MAJOR, five MINOR, five NOTEs, and all five MINOR fixed. CONFIRMED against review_report.md and the diff.
19. The header's "as are the NOTEs that changed a text a reader would trust", together with §5 NOTE 7. IMPRECISE.
20. A2's closure: the no-session branch runs through `--v2-closure`; it is refused for a campaign with sessions, read for the count only; an absent or empty campaign is accepted; `--campaign` without the flag is refused. CONFIRMED (`run_not_run`; the F3N-V2-CLOSURE cases).
21. A3's V1 list: the posted v1 output must be committed with the declared schema, posting, table_kind and bar PASS; --olmo-states and --flag-source are refused; --sentences must be committed, accepted as v2 and of kind of-record; adjudication-read entries are [stage, template, s]; the v1 reader refuses --adjudication-reads and --v1-dir. CONFIRMED.
22. A3's posting bullet, the PIN-V2-24 clause. CONFIRMED. `run_posting_v2` binds an of-record table to the sha256 that Q-F3's VERDICTS or its no-first-read NOT-RUN recorded; a Clock NOT-RUN record carries none.
23. A4 (1), "ganl's --out included (an empty argument as before)". CONFIRMED.
24. A5, "The readings are declared as PIN-V2-1 to PIN-V2-24 (§2)". IMPRECISE (minor).
25. §2's opening sentence: 24 PINs, listed as flags in the BUILD entry, strikable until v1.0 (answers:50). CONFIRMED.
26. §2's cost sentence. CONFIRMED as Code's statement. It fits answers:50 ("at the cost Code states") and PIN-37's write-once supersession.
27. §2 table, the new subjects for V2-6, -13, -14, -20 and -24. CONFIRMED against `PINS_F3`.
28. §2 table, V2-12's subject "(…; the inputs each reader takes)". IMPRECISE (minor).
29. N1's new bullet, "the v1 posting is the next step, so this flag is its blocker", and the same sentence in the entry's N1 paragraph. IMPRECISE.
30. N6. CONFIRMED. The code checks POSTING-v1_outputs.posted.json for commitment, schema m-posting-v1-outputs-v1, posting v1, table kind posted and bar PASS. `run_posting` writes the posted file only on a PASS. m:349's enumeration over the preprint of record is the run that refuses at HEAD, so "waits on N1" holds.
31. N9 in the design raw. CONFIRMED on the final bytes: 845/846; the case and its expected "startup: banner"; the lock §1 message (m_sessions.py:917–920); Code's reading labelled; the PIN-S10 anchor; m_sessions.py unchanged; the other nine suites PASS.
32. N10. CONFIRMED. m:312 says "each mentioned own-pair label takes the nearest polarity term within the window", and a shared nearest term makes the line ambiguous. The scorer gives "ambiguous" with prism positive and slate positive; slate's "clean" is one token back. F3C-SCORER records the case.
33. §5 Finding 1. CONFIRMED.
34. §5 Finding 2. CONFIRMED.
35. §5 Finding 3. CONFIRMED (only campaign entries exclude).
36. §5 Finding 4. CONFIRMED.
37. §5 Finding 5. CONFIRMED (P* characters become spaces; four cases).
38. §5 NOTE 6, "Two texts changed with it". FAIL.
39. §5 NOTE 8. CONFIRMED (--out; each reader refuses the other's inputs; the help texts).
40. §5 NOTE 9. CONFIRMED (PIN-V2-21's base-closure clause; the f3_closure sha is recomputed; 601,250 = 300,625 × 2).
41. §5 NOTE 10. CONFIRMED.
42. §4's counts on the final bytes (525/525, 538, the closures, the packages). CONFIRMED.
43. The entry's A3 clause, "run only after the v1 posting's posted re-run PASSed, … the v2 table of record as a bound input". CONFIRMED.
44. The entry's N9 block, "The refusal is the right behaviour: Q-F0's drivers refuse an analyzer their lock does not bind." IMPRECISE: the same defect as old item 91, and not labelled as Code's.
45. The entry's N9 block, "the G-SHAPE-F0 re-run the step-10 read's Q2 then requires". IMPRECISE: the same defect as old item 93.
46. The entry's N9 block, its factual lines (the quote, the case, LOCK-m-F0 binds 655e0f7f…, the message, no change to m_sessions.py). CONFIRMED.
47. The entry's A5 wording, "declared among PIN-V2-1 to PIN-V2-24". CONFIRMED.
48. The entry's dated-notes summary (N6, N9, N10). CONFIRMED.
49. The entry's PIN flag list: 24 ids, the subjects match `PINS_F3`, and the cost matches §2. CONFIRMED.

FAIL items and corrections
38. Source: the old and new `step6_text`, compared over all tuples. Three texts changed, not two:
- FAIL;
- REVERSE;
- the NULL clause's power slot, on 1,875 tuples per flag value (A1 PASS, A2 PASS, A3* NULL). "[the power figure of record for the realised n, the screen's]" (or "f2's") became "[… realised n — the screen's]", from m:342's "— f2's if f2 ran, else the screen's".

Corrected: "Three texts changed with it: FAIL now reads m:342's "scoped at this scaffolding and stimulus strength", REVERSE carries m:342's parenthesis, and the NULL clause's power slot takes m:342's dash ("… for the realised n — f2's" or "— the screen's") (PIN-V2-6)."

IMPRECISE items and corrections
19. review_dispositions.md has NOTE 7 "Applied, but for two items": COUNTERS stays Q-F0's declarations, and the era boundary is kept. §5 discloses the era boundary only. The manifest's counters field still says reasoning_line_defect is "not tabulated at Q-F0" (m_analyze.py:923), with Q-F3's counters in the block's counters_q_f3.
- §5 NOTE 7, add: "COUNTERS (the manifest's counters field) stays Q-F0's declarations, unchanged; Q-F3's are in the block (counters_q_f3)."
- Header: "…as are the NOTEs that changed a text a reader would trust, but for two items of NOTE 7 (§5)."

24. PIN-V2-24 comes from the review's finding 2, and PIN-V2-11 from A1, not from STOP §3's eleven. The entry already says "among".

Corrected: "The readings are declared among PIN-V2-1 to PIN-V2-24 (§2), beside the readings the build and the review added."

28. PIN-V2-12's text covers only Q-F3's reader refusing Q-F0's inputs. The v1 reader's new refusal of --adjudication-reads and --v1-dir (m_analyze.py:2243–2244) has no PIN text or site.

Corrected subject: "the Q-F3 reader's V1 (the Q-F3 closure; the posted v1 precondition; Q-F0's inputs refused)". Alternatively, extend PIN-V2-12's text and mark a site at the v1 refusal; that changes the analyzer's bytes, so it is Code's call.

29. RESULTS.md@0415438:90–93 (the G-CAL-OLMo entry): "Which NOT-RUN records and posting text follow, and what the pod does next, are the seat's and the PI's." There is no OLMo NOT-RUN output in data/m/verdicts at 0415438, and the escalation is not adjudicated.

Corrected (both drafts): "With the three OLMo checkpoints NOT-RUN "dose not completable" on the record at 6ce8b9a (escalated to the seat; which NOT-RUN records and posting text follow is the seat's and the PI's), the v1 posting is the m track's next step once those records exist, and this flag blocks it."

44. Corrected: "Code's reading: the refusal is right — the driver refuses a --proposal-file whose sha256 LOCK-m-F0's committed text does not name in full (lock §1), and this analyzer's is not named there. What moved is the case's premise, and any in-place G-ANL-F3 commit moves it."

45. Corrected: "Its fix, and the G-SHAPE-F0 re-run that PIN-S10 then requires (the step-10 read's Q2 clears only a subcommand-wiring edit), are the seat's call."

Observation (not counted): §3's heading still says "minor residues", but it now holds three FLAGs (N1, N9, N10).

I wrote only helper scripts, in my own scratch folder vc_build. I touched nothing in the repository or the worktree.

### Code's dispositions of the second pass

Each item marked FAIL, IMPRECISE or NOT CHECKABLE was re-checked at source before acting.

| Item | Verdict | Re-checked at source | Disposition |
|---|---|---|---|
| 38 | FAIL | `step6_text`'s NULL branch replaces m:342's "f2's if f2 ran, else the screen's" with "f2's" or "the screen's", so m:342's dash stays before it; the earlier render had a comma there. | Applied as proposed, in §5 NOTE 6 and in the review's dispositions (finding 6's row). |
| 19 | IMPRECISE | `COUNTERS`' Q-F3 entry (`scripts/m_analyze.py:923`) still reads "not tabulated at Q-F0: Q-F3's runner and scorer (G-ANL-F3, step 19)"; §5 NOTE 7 disclosed the era boundary alone. | Applied: NOTE 7 names both kept items, and the header says "but for two items of NOTE 7". |
| 24 | IMPRECISE | PIN-V2-11 comes from A1 and PIN-V2-24 from the review's finding 2, not from the STOP's §3. | Applied as proposed. |
| 28 | IMPRECISE | PIN-V2-12's text names Q-F0's inputs refused. The v1 reader's refusal of `--adjudication-reads` and `--v1-dir` (`run_verdicts`) has no PIN text. | The subject is corrected as proposed. PIN-V2-12's text is not extended: the refusal is a guard on inputs that the analyzer of record does not take, not a reading of the record (`git show ed8e886:scripts/m_analyze.py` has none of `--adjudication-reads`, `--v1-dir`, `--v2-closure` or `--f3-verdicts-dir`; its `--campaign` is `verdicts`' only, not `not-run`'s), and §5 NOTE 8 discloses it. (Corrected on the third pass's item 12, which found the first form of this parenthesis wrong on `--campaign`.) |
| 29 | IMPRECISE | RESULTS.md@0415438:92–93: "Which NOT-RUN records and posting text follow, and what the pod does next, are the seat's and the PI's." `data/m/verdicts` at 0415438 holds Q-F0's four files only. | Applied as proposed, in both drafts. |
| 44 | IMPRECISE | The design raw's N9 carries the corrected reading; the entry's N9 block did not. | Applied as proposed. |
| 45 | IMPRECISE | As the first pass's item 93: the step-10 read's Q2 clears only a subcommand-wiring edit, and the re-run is PIN-S10's. | Applied as proposed. |
| 17 | NOT CHECKABLE | The PI's ruling reached Code in the coordinating session's message, not a file. | Quoted as relayed; labelled "relayed" in the design raw (header, N9) and in the entry's N9 block. |
| Obs. | — | §3 held three FLAGs (N1, N9, N10) under "minor residues". | §3 is retitled "Dated notes and FLAGs …". The entry's header and routing now name the FLAGs: these three, and N12, found after this pass by the final site check. |

## 3. The third pass, with the review of the last code delta (verbatim)

(A) 0 MAJOR, 0 MINOR, 4 NOTE (plus 1 observation outside the delta, not counted). (B) 18 items: 8 CONFIRMED, 9 IMPRECISE, 1 FAIL. No item is wholly NOT CHECKABLE; the chat-only parts inside items 10, 12, 13, 16 and 17 are marked NOT CHECKABLE where they occur.

**Versions checked:** the drafts as of 23:11, unchanged since:
- entry_build.md, 9,765 B, sha256 334d25b2…
- design_raw.md, 27,414 B, b85f6ab3…
- commit_build.txt, 3,630 B, 2bb52701…
- vc2_dispositions.md, 2,423 B, 3e4cf4e7…

**What I ran.** Everything was read-only on the repo and the worktree. I wrote only under vc3/. That folder already held four files from an earlier pass (hist.py, lock_hashes.txt, pkg_at.py, quotes.py), which I left alone. Mine are delta.diff, pins_f3.txt, probe_a.py, tmp_probe/ and old_m_analyze.py.
- **The diff.** Blob ids show that only scripts/m_analyze.py changes across 5f9a696..bcd15c9. The other four build files are identical at 5f9a696, 54c9d64, bcd15c9 and in the worktree. The analyzer is 455f0f18…, which matches selftest_h.sha.
- **probe_a.py.** Runs `run_not_run` in-process on `_bt_env` (probes P1–P6), plus `_cli_path` and `main` on a "~user" path.
- **Other checks:**
  - a dump of PINS_F3;
  - both analyzers' `table_problems` on the table of record at HEAD;
  - `score_line_c` on N10's sentence;
  - mf3's and m's package hashes, recomputed from git blobs;
  - `git check-ignore -v --no-index`;
  - greps of the site-check outputs, head_m_sessions.txt, gcalprobe_out.txt and the dry raws.
- No suite and no `--selftest` was run. The worktree's status is unchanged: only the untracked HANDOFF file that was already there. Main's HEAD is e7e070f, not 0415438 as the brief said.

## (A) The code delta

**A1. NOTE: `--campaign none`, and any identity-matching file, are taken on the operator's word** (m_analyze.py:2570–2588).
- With `none`, no file is read, and data/m/ckpt/{U}_campaign.json is never consulted.
- A file passed instead only has to carry identity {unit, stage campaign} and an empty sessions list. It need not be committed, and it need not be the canonical checkpoint.
- Failure case (probe P1):
  - data/m/ckpt/OLMo-dpo_campaign.json is committed and records sessions.
  - `not-run --unit OLMo-dpo --record R --v2-closure --campaign none` still writes OLMo-dpo_NOT-RUN.json, cause pending-closed-at-v2, with `v2_closure` = {"campaign": "declared none", "sessions": 0}.
  - The v2 posting then admits it (`crosscheck_coordinate` with v2=True, :2659). But m:324 sends a checkpoint with sessions to analysis, not to NOT-RUN.
  - A stale pre-session copy of the checkpoint, with sessions [], also passes.
- The declaration is recorded in the output, so this is not silent. But `"sessions": 0` under "declared none" is declared, not read.
- The follow-up review suggested "present and committed, or a declared attestation when it is absent". The fix applies it as "present, or declared", with no check that the file is absent.
- Fix: refuse `none` when the canonical path exists (or is in HEAD), and require `env.committed` for a file that is passed.

**A2. NOTE: the campaign file is read twice.** The check uses `read_text` (:2576); the output's sha256 uses a separate `read_bytes` (:2629); the gate reads happen in between.
- Probe P2: I rewrote the file between the two reads. The result is "ok", and the recorded sha256 belongs to bytes that record a session, not to the bytes that were checked.
- Probe P3: I removed the file between the reads. The result is an uncaught FileNotFoundError, which exits 1 through `main`. PIN-26 reserves exit 1 for a selftest FAIL (:46); this should have been a refusal.
- Fix: read the bytes once with `_read_bytes`, parse them, and record their sha256.

**A3. NOTE: `_cli_path`'s `Path(a).expanduser()` (:11195) raises RuntimeError for "~name/…" when no such user exists.**
- `main` catches only AnlPostingFail and SystemExit (:11284–11290), and the `ganl` branch calls `_cli_path` outside the try (:11235).
- Probe P4: `main(["not-run","--unit","OLMo-dpo","--record","~nosuchuser_zz9/r.json"])` ends in a RuntimeError traceback, exit 1.
- At 5f9a696 the same argument resolved inside the repo and was refused with exit 2.
- This touches every path argument of every command, v1's included, though the input is unlikely.
- Fix: catch RuntimeError, then either leave the path unexpanded or refuse it.

**A4. NOTE: the module docstring is stale.** Its usage line (:35) reads "not-run … [--v2-closure]" with no `--campaign`, which is now required with `--v2-closure`. The argparse help text (:11220) is correct.

**Nothing else found:**
- Each of the new cases c6–c12 can fail: removing or loosening its refusal flips the case.
- F3R-READER-REFUSALS:
  - its 12 `refs` keys equal `why_`'s, and each substring occurs only in its intended refusal;
  - `V` always returns a 4-tuple, so the dropped None guard in the diagnostic is safe.
- The v1 paths are unchanged apart from A3. A `not-run` with neither flag still reaches `base not in NOT_RUN_FROM_RECORD`. `--campaign none` without `--v2-closure` is refused (P6).
- Real campaign checkpoints satisfy the identity predicate. Q-F0_campaign.json has identity Q-F0/campaign and a sessions list of 129. resume.py:1110 shows the OLMo form.
- The battery is 525/525 on these bytes (selftest_h, and sitecheck_out/m_analyze.txt).

**Outside the delta (not counted): PIN-V2-12's site comment (:4088) is stale.**
- It still reads "the v1 posting's output present", which describes the guard before the fix.
- The code (:4112–4122) and PINS_F3["PIN-V2-12"] now require the posted output to be committed and to have passed C7's bar.
- The comment is unchanged since 69ff08d. The finding-1 disposition says "PIN-V2-12 and N6 are reworded", but only the register text was.

## (B) Values-check

**1. CONFIRMED.**
- review_report.md: no MAJOR, five MINOR, five NOTEs.
- review_dispositions.md: findings 1–5 applied; NOTE 7 "Applied, but for two items".
- review_followup.md: "four NOTEs and no MAJOR or MINOR"; in §4, NOTEs 1–3 applied and NOTE 4 recorded as N11.
- NOTE 2 was applied only in part; see item 9.

**2. CONFIRMED.**
- answers:14: the quote is verbatim.
- m:324; resume.py:139 has the PI-STOP terminal.
- m_analyze.py:2567–2590 and :2627–2630.
- Q-F0 is refused by the OLMo-only cause rule (:534–535).
- `crosscheck_coordinate`: :2644–2660.

**3. IMPRECISE.**
- STOP §3's item 10 (round 2's rule) is not declared among PIN-V2-1…24. No PINS_F3 text or PIN-V2 site names it. It lives in SEAT_RULED_F3["A4"] (:4517–4518) and as dated note N4.
- Corrected: "Ten of the eleven are declared among PIN-V2-1 to PIN-V2-24 (§2), beside the readings the build and the review added; item 10, round 2's rule, is a procedure, carried out as N4."
- The entry's A5 line ("Code's eleven readings, declared among PIN-V2-1 to PIN-V2-24") needs the same fix.

**4. CONFIRMED.**
- All 24 subjects match the PINS_F3 texts dumped from the worktree analyzer.
- V2-12's parenthetical matches its text. The text also names the declared v2 table, the adjudication-reads file and the outputs; the subject is a summary.
- V2-20's "(`--campaign` required; no campaign session)" matches.
- Each PIN has one site, V2-9 two.

**5. IMPRECISE (minor).**
- The facts hold. RESULTS.md@0415438:90–93 has the NOT-RUN on the record, and "which NOT-RUN records and posting text follow … are the seat's and the PI's". data/m/verdicts at HEAD holds Q-F0's four files only.
- But "the m track" is not a term the record uses, and Q-F3's track (A-m1 §4 step 5) runs in parallel. A-m1 §4 puts POSTING v1 (step 6) after the OLMo track (step 4).
- Corrected: "…the v1 posting (A-m1 §4 step 6) is the next step after the OLMo track once those records exist, and this flag blocks it."

**6. CONFIRMED.** I checked the current heading, which names N1, N9, N10 and N12 as FLAGs.
- Each of those four notes is labelled "FLAG, not adjudicated"; N11 is not.
- "The e9b5022 precedent" is the PI's routing phrase "minor residues as dated notes (the e9b5022 precedent)", RESULTS.md:435.

**7. CONFIRMED.**
- `git check-ignore -v --no-index`:
  - .gitignore:273 `/data/mf3/*` matches Q-F3_VERDICTS.json and Q-F3_NOT-RUN.json (and Q-F3_secondary.json);
  - .gitignore:235 `!/data/m/gates/*.json` admits the v2 placeholder and G-ANL-F3.json;
  - lines 272–285 admit only schedules, gates, reports and ckpt under data/mf3.
- `run_posting_v2` reads both Q-F3 files for PIN-V2-24 (:4364–4373).
- PIN-25's text defers data/m/verdicts' admit block to the first commit that writes there.

**8. IMPRECISE (the follow-up's NOTE 2 bullet only).**
- NOTE 6 CONFIRMED:
  - S6_* (:3164–3182) equal m:342's texts;
  - `constants_by_line` checks them (:5184);
  - `_bt_m342` reads m:342 at run time (:10077);
  - the null clause's power slot (:3210) now keeps m:342's dash, where 69ff08d rendered ", {whose}" (:3152).
- NOTE 7 CONFIRMED:
  - PINS["PIN-29"] (:4698–4704);
  - GANL_F3_BLOCK_KEYS and the block at :11096–11097;
  - `pending_state`'s message (:606–607);
  - PIN-V2-10's text;
  - COUNTERS (:922–923), which feed the manifest's counters field (:11124).
- Follow-up NOTEs 1, 3 and 4: CONFIRMED.
- NOTE 2: "the malformed and other-unit cases have their own message" — the two cases share one message (:2584–2585), separate from the sessions refusal (:2587). The bullet also does not say that the file need not be committed, or that `none` is not checked against the tree.
- Corrected: "…or `none`, declared and recorded (not checked against the tree); a malformed or another unit's file is refused with one message of its own, apart from the sessions refusal, and an absent path as unreadable; the file need not be committed (PIN-V2-20)."

**9. IMPRECISE (row 2).**
- Row 1 CONFIRMED. At 5f9a696, `_cli_path` (:11152–11153) had no `expanduser`, and `run_ganl` (:10967) expanded only for its canonical comparison.
- Rows 3 and 4 CONFIRMED. The check-ignore output is exactly as quoted.
- Row 2 says "Applied" without saying that the suggestion's "committed" half and the absence check for `none` were not adopted. "A malformed or other unit's file gets its own message" is also loose: it is one shared message.
- Corrected: "Applied in part. … A malformed or another unit's file is refused with one message of its own, and an absent path as unreadable (PIN-V2-20). Not adopted: the file is not required to be committed, and `none` is not checked against an existing data/m/ckpt/{U}_campaign.json. …"

**10. IMPRECISE (the N1 paragraph).**
- **Header FLAG sentence:** CONFIRMED; the PI's ruling is NOT CHECKABLE.
- **Routing bullet:**
  - CONFIRMED: 54bbfe5 is the STOP's close; "(a) with the second-STOP flip" matches answers:38 and RESULTS.md:431; Code's reading is labelled.
  - NOT CHECKABLE: the relay quote and "Commit with flag". Only "Apply B as written" appears in a file (RESULTS.md:410).
- **A2 clause:** CONFIRMED.
- **N1 paragraph:**
  - CONFIRMED: the 32aefcc banner; HEAD's preprint is 5d677a72…; 1523cce's blob is 45b67246…7a41, the table's own value (88,668 bytes, 468 lines), which LOCK-m-F0.md names; I ran `table_problems` from both ed8e886's analyzer and bcd15c9's, and both refuse the table of record at HEAD.
  - IMPRECISE: "the m track's next step", as in item 5.
- **N9's unchanged lines:** CONFIRMED.
  - the case at m_sessions.py:4478–4479;
  - LOCK-m-F0.md names 655e0f7f…, not 455f0f18…;
  - lock §1's message appears in the FAIL line;
  - TOOLING_FILES at gshape.py:105, and PIN-S10 at gshape.py:233–236;
  - Q2's scope as answers:24 restates it.
- **Dated-notes bullet, N9–N12:** CONFIRMED. `score_line_c` gives "ambiguous" with prism and slate both positive. m:292 lists "G-ANL-F3's analyzer and lexicon hashes" and "G-SHAPE-F3's result".
- **Next bullet:** CONFIRMED against PIN-V2-23, answers:38 and m:292; its plan parts are NOT CHECKABLE. Cosmetic: one line of it is not re-wrapped.

**11. CONFIRMED** for every claim not covered by item 17.
- No LOCK-m-OLMo-*.md exists in the tree or at HEAD.
- ed8e886's analyzer is 655e0f7f….
- In the final run, the regression, v1-unchanged and v2 checks pass (sitecheck_out/m_analyze.txt:450, :459, :490–491).
- PIN29_RELEASED has seven entries, and BLOCKED_REL includes mf3's three roots.
- 218,855 + 300,625 = 519,480.
- Recomputed: the base closure a3bc7bb9… and m's package 60199b36… are unchanged; mf3's package goes from 44110d15…3842 at 0415438 to f30ad505… at bcd15c9.
- N1 and N10 as in item 10.
- The process and plan claims are NOT CHECKABLE.

**12. FAIL (row 28).**
- Row 38 CONFIRMED. Row 19 CONFIRMED (:923). Row 24 CONFIRMED.
- **Row 28, FAIL.** It says ed8e886's analyzer has no `--campaign`, but it has one for `verdicts` (ed8e886 :8191; its docstring :19 shows "[--campaign P]"). The other four flags are indeed absent, and the v1 refusal (:2244) fires only on `--adjudication-reads` and `--v1-dir`.
  - Corrected: "(`git show ed8e886:scripts/m_analyze.py` has none of `--adjudication-reads`, `--v1-dir`, `--v2-closure` or `--f3-verdicts-dir`; its `--campaign` is `verdicts`' only, not `not-run`'s)".
  - The row's rationale, "would move the analyzer's bytes after the checks of record", is Code's call. Note, though, that the bytes did move after the second values-check, for the follow-up NOTEs.
- **Row 29, IMPRECISE (anchor):** the quoted sentence is RESULTS.md@0415438:92–93, not :93. The data/m/verdicts claim is CONFIRMED.
- Rows 44 and 45 CONFIRMED. The first pass's item 93 is about Q2 and PIN-S10.
- **Row 17:** the ruling is NOT CHECKABLE. The disposition is IMPRECISE: "relayed" appears in the design raw (header and N9) and in the entry's N9 block, but not in the entry's header or routing bullet, nor in the commit message.
  - Corrected: "Quoted as relayed; labelled "relayed" in the design raw (header, N9) and the entry's N9 block."
- The Obs. row is item 18.

**13. IMPRECISE.**
- The counts are CONFIRMED:
  - 845/846 on the 273ca8f base, with N9's case alone failing (raw_sitecheck.txt:54–55);
  - 843/846 on bcd15c9 (FAILs at sitecheck_out/m_sessions.txt :636, :780, :832);
  - 844/846 at e7e070f (FAILs at head_m_sessions.txt :636, :832);
  - e7e070f differs from 0415438 only in RESULTS.md and results/raw/2026-11-06_n-gacq{,_valuescheck}.md.
- The problem is "the base the commit lands on (0415438 …)". The commit lands on main's HEAD, e7e070f: finalize.sh copies the files into the main checkout, and e7e070f was committed at 22:57:35, during the site check.
- Corrected: "On the commit's base, `e7e070f` (it differs from `0415438`, main's HEAD when the site check started, in RESULTS.md and two raws only): 843/846 with this analyzer (the site check on `0415438` plus the five files) and 844/846 without it (at `e7e070f`); N12's two cases fail either way."
- In the added sentence, "put on the 845/846 count" is NOT CHECKABLE. "The same one on either base" is CONFIRMED: the same sub-case, "a lock-named non-proposal", fails with lock §1's message on both analyzers (16b56512… and 455f0f18…).

**14. IMPRECISE (minor).**
- CONFIRMED:
  - e7e070f's analyzer is 655e0f7f…, and head-wt is clean at e7e070f;
  - 844/846, with the two FAIL texts at head_m_sessions.txt:636 and :832 (sources: gcal.py:2411 and m_sessions.py:6924);
  - 6ce8b9a adds the three G-CAL_olmo checkpoints;
  - the probe shows CHECKPOINT EXISTS for sft and instruct;
  - 273ca8f is an ancestor of 6ce8b9a, and its base ran 845/846;
  - the five build files touch neither test file;
  - gcal.py is in m's package (valence_core/m/*.py, gshape.py:233), and m_sessions.py is a TOOLING_FILES entry;
  - the dry raw's last sections hold the HEAD run and the probe.
- Imprecise: "expects the pod-id refusal". The driver case (m_sessions.py:6915–6925) runs `run_gcal_completability(None, …, unit="OLMo-instruct")` and expects exit 2 naming both "POD ID ABSENT" and "weights:".
- Corrected: "…and expects its refusal before any load — the pod id's, and in the driver's case the weights' too."
- The dry raw's probe heading, "gcal.precheck as the two cases call it", is loose in the same way.

**15. CONFIRMED.**
- The heading is as in item 6.
- mf3_modules_selftest2.txt: 13 modules, TOTAL 124/124. valence_core/mf3 has 14 modules besides `__init__`, and testing.py is the only one without a self-test.
- sitecheck_final4_summary.txt: nine suites PASS and m_sessions FAILs. The 843/846 and 844/846 counts are as in item 13.

**16. IMPRECISE.**
- CONFIRMED: the header's "Four FLAGs" sentence, the routing bullet, and "N12 above".
- The N9 counts bullet, "On the commit's base, 843/846 with this analyzer and 844/846 without it", has the same problem as item 13.
  - Corrected: "On the commit's base (`e7e070f`), 844/846 without this analyzer; with it, 843/846 on `0415438` plus the five files (`0415438` differs from `e7e070f` in RESULTS.md and two raws only); N12's two cases fail either way."
- The added sentence is as in item 13.
- The N12 block is CONFIRMED except "expecting the pod-id refusal", as in item 14.
- Observation: the drafts record no PI word on N12. "Commit with flag" was given on the 845/846 count, before N12 was found. The drafts do not claim it covers N12.

**17. IMPRECISE.**
- "Four FLAGs" and "N1-N12": CONFIRMED.
- The N9 sentence: CONFIRMED; the PI's quote is NOT CHECKABLE.
- The N12 sentence has two problems. "843/846 on the commit's base" was measured on 0415438 plus the five files. "The pod-id refusal the cases expect" omits that the driver case also expects the weights refusal.
- Corrected: "…the precheck refuses on CHECKPOINT EXISTS before the refusals the cases expect (the pod id's; in the driver's case the weights' too)); with this analyzer the suite is 843/846 on 0415438 plus the five files (0415438 and e7e070f differ in RESULTS.md and two raws only)."

**18. CONFIRMED.**
- §3 is retitled, and the entry's header and routing name N1, N9, N10 and N12.
- N12 first appears in the final run on bcd15c9 (03:56:58Z–04:05:41Z). That is after the second values-check's report, around 22:54 local.
- Earlier runs on the 273ca8f base were 845/846, with N9's case alone failing. The 22:54 final3 summary has no m_sessions line.

### Code's dispositions of the third pass

Each item was re-checked at source before acting. Part (A)'s fixes move the analyzer's bytes once more, so the battery and the site check ran again on the final bytes (the selftest and site-check raws), and the reviewer was asked to check the fixes (§4 below).

**(A) The code delta**

| Item | Grade | Re-checked at source | Disposition |
|---|---|---|---|
| A1 | NOTE | `run_not_run` at bcd15c9: with `none`, no file is read; a passed file needs only the identity and a sessions list, and its commitment is not checked. | Applied. `none` is refused while `data/m/ckpt/{U}_campaign.json` exists in the tree or at HEAD (`Env.head_has`; in production `git cat-file -e HEAD:<rel>`). A passed checkpoint must be committed at HEAD, its bytes as read equal to HEAD's blob (rule 27). PIN-V2-20's text and site comment say so. F3N-V2-CLOSURE gains four cases: c13 (a canonical file planted in the tree), c14 (HEAD has the path), c15 (not committed) and c16 (bytes that are not HEAD's blob). |
| A2 | NOTE | The check used `read_text`, and the output's sha256 a separate `read_bytes`, with the gate reads between them. | Applied: the bytes are read once (`_read_bytes`, so an absent file is a refusal, exit 2), and the committed-blob comparison, the parse and the recorded sha256 all use them. |
| A3 | NOTE | `Path("~name/x").expanduser()` raises RuntimeError when no such user exists. `main` caught only AnlPostingFail and SystemExit, and ganl's `_cli_path` call was outside its try. | Applied: `_cli_path` refuses such an argument (AnlRefusal, exit 2), and ganl's `--out` is resolved inside the try. PIN-V2-8's text says so. F3R-CLI-PATHS asserts the refusal and exit 2 from `ganl` and `not-run`. |
| A4 | NOTE | The usage line read `[--v2-closure]`. | Applied: `[--v2-closure --campaign P|none]`. |
| Obs. | — | PIN-V2-12's site comment read "the v1 posting's output present". | Applied: the comment names the posted re-run, committed and PASSing C7's bar, and the v2 table of record. |

**(B) The values-check**

| Item | Verdict | Re-checked at source | Disposition |
|---|---|---|---|
| 3 | IMPRECISE | The STOP's §3 item 10 (`results/raw/2026-11-06_ganl-f3_code-to-design_prebuild.md:115`) is round 2's rule, a search procedure; no PIN-V2 text names it. | Applied as proposed, in the design raw's A5 and in the entry's and the commit message's A5. |
| 5; 10 (N1) | IMPRECISE | ADDENDUM-m1 §4 (lines 54–62): step 4 is the OLMo track, step 5 Q-F3 in parallel, step 6 `POSTING v1`. | Applied as proposed, in both drafts. |
| 8 | IMPRECISE | The malformed and other-unit refusals share one message. | Applied: the NOTE 2 bullet says so and names the second step (A1 above). |
| 9 | IMPRECISE | As item 8. | Applied: the row now reads "Applied, in two steps" and names the third pass's A1. |
| 10 (Next) | cosmetic | One line was not re-wrapped. | Re-wrapped. |
| 12 (row 28) | FAIL | `git show ed8e886:scripts/m_analyze.py`: `verdicts` takes `--campaign` (its option loop); `not-run` does not. | Applied: the parenthesis is corrected. The rationale now rests on what the refusal is, a guard on inputs the analyzer of record does not take, since the bytes moved again after the second pass. |
| 12 (row 29) | IMPRECISE | The quoted sentence runs RESULTS.md@0415438:92–93. | Applied. |
| 12 (row 17) | IMPRECISE | "relayed" appears in the design raw (header, N9) and in the entry's N9 block only. | Applied as proposed. |
| 13; 16 (N9's counts); 17 (the base of 843/846) | IMPRECISE | The site check ran on 0415438 plus the five files; e7e070f was committed during it. | Settled by the re-run: the final site check runs on e7e070f plus the five files (the site-check raw), and N9 reads "On the commit's base (`e7e070f`), 843/846 with this analyzer and 844/846 without it". |
| 14; 16, 17 (N12's expectation) | IMPRECISE | `scripts/m_sessions.py:6915–6925`: the driver case expects exit 2 naming both "POD ID ABSENT" and "weights:". | Applied as proposed in the design raw, the entry and the commit message; the site-check raw's probe heading is reworded too. |
| Observations | — | No PI word on N12. | None is claimed; N12 goes to the seat as a FLAG. |

## 4. The fourth pass: the third pass's agent on the fixes and the changed texts (verbatim)

(A') 0 MAJOR, 0 MINOR, 2 NOTE. (B') 7 items: 7 CONFIRMED, with remarks. All five fixes do what I asked, and I found no regression. The site check was still running when I finished (23:40 EST): m_sessions is done at 843/846; m_analyze and mf3_sessions had not finished.

**What I checked**
- Worktree HEAD is 8e2cec3, whose parent is e7e070f. The analyzer is 6ec3222b…93d9. The other four build files have the same blob ids as at bcd15c9.
- The delta is `git diff bcd15c9 8e2cec3`, saved as vc3/delta2.diff.
- vc3/probe_b.py, writing only to vc3/tmp_probe_b:
  - P1a–e, P2, P3 on the battery env;
  - P4 with `run_ganl` stubbed, so no battery could run;
  - P8a–f with `production_env()` end to end (read-only git in the worktree; outputs under vc3).
- Greps of selftest_i.txt, sitecheck_out/*, ADDENDUM-m1 and the HEAD tree.
- I ran no suite and no `--selftest`. The worktree status is unchanged: only the untracked HANDOFF file, which was already there.

## (A') The fixes

**Verified:**
- **A1, the 'none' check.**
  - `canon_` (:2583) defaults to REPO/data/m/ckpt. `none` is refused if that file exists, is a symlink, or is in HEAD (`env.head_has`).
  - P1a: refused with a planted canonical file. P1d: refused with a dangling symlink. P1b/P1c: accepted with an empty or absent canonical file.
  - P8a: `_prod_head_has` is True for Q-F0_campaign.json and False for OLMo-dpo's. P8b: production `none` → ok, `v2_closure` {"campaign": "declared none", "sessions": 0}.
- **A1, a passed file.** It must equal HEAD's blob as read (:2592–2598).
  - P8c: a file outside the repo is refused ("not committed at HEAD as read").
  - P8d/P8e: committed Q-F0_campaign.json and G-CAL_olmo-dpo.json, passed for OLMo-dpo, are refused with the identity message.
- **A2, one read.** P2: the file was rewritten after the check, and the recorded sha256 equals the checked bytes. P3: the file was removed after the check, and the run completes without a crash.
- **A3.**
  - P4: `_cli_path("~nosuchuser_zz9/…")` → AnlRefusal ("names no user"). `main` returns 2 for `not-run` and 2 for `ganl`, and `run_ganl` was never called for it; a plain `~/x` still expands.
  - ganl's `_cli_path` call is now inside the try (:11301–11303).
- **A4.** The usage line (:35) now reads `[--v2-closure --campaign P|none]`.
- **The observation.** PIN-V2-12's site comment now matches :4134–4145.
- **Can each new case fail?** Yes. Each of c13–c16 flips if its own test is removed: c13 the exists() test, c14 head_has, c15 the problems test, c16 the blob comparison. c14 runs with an empty canonical dir, so head_has is the only reason it is refused.
- **F3R-CLI-PATHS on the original defect.** `tilde_` fails cleanly: the RuntimeError becomes "group raised" through `B.group`.
- **selftest_i.txt** carries the new labels, the 14-element diagnostic with c13–c16 refused, and {'ganl': 2, 'not-run': 2}; 525/525, 538 ids, exit 0.
- **No regression:**
  - `ckpt_dir` is a trailing default; the CLI never passes it.
  - The v1 `not-run` path is untouched.
  - `Env.head_has` has a default, so all four Env constructions still build.
  - Ordinary paths through `_cli_path` are unchanged.

**NOTE A'1: the `none` check ignores set-asides.** resume.py:842 moves a checkpoint aside as `{name}.podchange-{stamp}`; the follow-up review cited this case. P1e: a canonical dir holding only `OLMo-dpo_campaign.json.podchange-20261201`, with sessions, still lets `none` through. Whether a set-aside's sessions count under m:324 is the seat's call. Refusing `none` while a `{U}_campaign.json.podchange-*` exists, in the tree or at HEAD, would force that decision instead of declaring past it.

**NOTE A'2: F3R-CLI-PATHS's `main(["ganl","--out","~nosuchuser_zz9_m/x"])` (:10031) can recurse instead of failing.**
- Failure case: a regression that makes `_cli_path` silently accept the argument, e.g. `except RuntimeError: q = Path(a)`.
- That path then resolves to `REPO/~nosuchuser_zz9_m/x`, outside resume.py:151's CANONICAL_ROOTS, so `run_ganl` runs `battery()` (:11108). That battery re-enters the same call, and the batteries nest until RecursionError — hours, not a clean FAIL. Nothing is written, since every level fails.
- The not-run half cannot catch that regression either: it returns 2 because the REPO-relative record is unreadable.
- Fix: stub `run_ganl` for that call, as my P4 did, so the regression shows up as rc ≠ 2.

**Remarks, not graded:**
- `Env.head_has` defaults to False (fail-open), and only `production_env` sets it. That is fine while `production_env` alone serves the CLI.
- `_prod_head_has` has no try around git. A missing git is refused earlier anyway, in `analyzer_binding` through `_committed`'s OSError catch.
- "Read once" (PIN-V2-20, A2's paragraph, the third-pass bullet): `stages._committed` re-reads the working tree for its own comparison. Because `blob_ != cb_` refuses, the check, parse and hash stay bound to HEAD's blob and any drift fails closed. The wording is defensible; no change needed.

## (B') Values-check

**1. design_raw.md: CONFIRMED.**
- The header's new sentence matches my pass-3 report (0 MAJOR, 0 MINOR, 4 NOTEs, 1 observation), and all five are applied in the delta.
- A2's closure paragraph matches :2580–2612 (with the "read once" remark above).
- A4 (1)'s added clause matches `_cli_path` (:11252–11262) and P4.
- A5's line is my proposed wording.
- The V2-20 subject agrees with PINS_F3["PIN-V2-20"].
- N1's bullet matches A-m1 §4: :58 is step 4, the OLMo track; :59 step 5, Q-F3; :60 step 6, POSTING v1.
- N9's counts:
  - 845/846 is raw_sitecheck.txt:54–55.
  - 843/846 is the re-run on 8e2cec3 (sitecheck_out/m_sessions.txt, 23:37:59). Its FAILs are at :636, :780 and :832, and N9's case names 6ec3222b….
  - 844/846 is head_m_sessions.txt.
- N12's "Each reaches …":
  - gcal.py:2395–2398 calls `precheck(out_path=None, unit="OLMo-sft")` and expects POD ID ABSENT.
  - The driver's `run_gcal_completability` calls `gcal.precheck(out_path=None, …)`, and its case expects exit 2 with both "POD ID ABSENT" and "weights:".
- The §5 NOTE 2 bullet is confirmed.
- The third-pass subsection is confirmed. Its last bullet (525 checks, 538 ids, the new cases as sub-cases) matches selftest_i.txt.

**2. entry_build.md: CONFIRMED.**
- The A2 clause, the A5 line, N1, N9's counts (the re-run, as in item 1) and N12 are confirmed.
- The Next bullet is re-wrapped (lines 98–102 are 107, 116, 113, 112 and 15 characters), with its text unchanged.

**3. commit_build.txt: CONFIRMED.**
- The A2 parenthesis is confirmed. "None refused while a checkpoint exists" is loose for "the unit's campaign checkpoint, in the tree or at HEAD", but acceptable.
- The A5 sentence is confirmed.
- The N12 sentence is confirmed, including 843/846 on e7e070f, by the re-run.

**4. review_followup.md §4, row 2: CONFIRMED.** "The suggestion's other half" refers accurately to the follow-up's suggestion. The set-aside example in that NOTE's problem statement is still open; see A'1.

**5. vc2_dispositions.md rows 28, 29 and 17: CONFIRMED.**
- Row 28: in ed8e886, `verdicts`' option loop (:8191) includes `campaign`, `not-run`'s loop (:8196) has only time, qual and out, and the other four flags are absent.
- Row 29: the anchor is :92–93.
- Row 17: its restricted claim matches the drafts. The entry's header, the routing bullet and the commit message carry no "relayed".

**6. vc3_dispositions.md: CONFIRMED, row by row.**
- **Intro:** the battery re-ran on the new bytes (selftest_i's labels). The site check's re-run had finished m_sessions; m_analyze and mf3_sessions were still running at 23:40.
- **(A) rows A1–A4 and Obs.:** each matches the delta and the probes. A1's "PIN-V2-20's text and site comment" and c13–c16 are as described.
- **(B) row 3:** the STOP's line 115 is round 2's rule; the design raw, the entry and the commit message all apply it.
- **Row "5; 10 (N1)":** A-m1 lines 54–62 are §4, from its heading to the blank line after step 6.
- **Rows 8, 9, 10 (Next), 12 (28/29/17), 14/16/17 and Observations:** each is as stated. The probe heading is reworded (see item 7).
- **Row "13; 16; 17":** sitecheck_final5_summary.txt and sitecheck_out/m_sessions.txt now exist. The re-run is on e7e070f plus the five files and gives 843/846 with the same three FAILs, and N9 reads as quoted.

**7. make_raws.py's probe heading: CONFIRMED.** gcal's case calls `precheck` with unit OLMo-sft (gcal.py:2397). The driver case runs `run_gcal_completability(None, …, unit="OLMo-instruct")` (m_sessions.py:6919). gcalprobe.py calls `gcal.precheck` for both units.

### Code's dispositions of the fourth pass

Each item was re-checked at source before acting. Neither NOTE moves the analyzer's bytes: one is a question for the seat, and the other guards against a regression that has not happened.

| Item | Grade | Re-checked at source | Disposition |
|---|---|---|---|
| A'1 | NOTE | `resume._set_aside` (`valence_core/m/resume.py:840–848`) renames a checkpoint to `{name}.podchange-{stamp}` and never deletes it. The `none` check (`run_not_run`; PIN-V2-20) looks only for `data/m/ckpt/{U}_campaign.json`, in the tree and at HEAD. | Recorded as the design raw's N13, a FLAG for the seat, with Code's reading: the respawn protocol's consistency clause (CLAUDE.md:127–130) puts a set-aside's sessions outside the campaign of record, so `none` stays a true declaration. If the seat reads it otherwise, the fix refuses `none` beside a set-aside. That would be a second hash-moving round, the seat's to authorize. No change here. |
| A'2 | NOTE | F3R-CLI-PATHS calls `main(["ganl", "--out", "~nosuchuser_zz9_m/x"])`. If `_cli_path` accepted that argument, `run_ganl` would run the battery inside the battery. | Disclosed, no change. No such regression exists, and none can arise without another analyzer edit, which only the seat can authorize under the one-round rule. Any later edit to `_cli_path` should first stub `run_ganl` in that check (the design raw's §5). |
| (B') 3 | remark | "none refused while a checkpoint exists" is loose. | Applied: the commit message now says "while the unit's campaign checkpoint exists in the tree or at HEAD". |
| (B') 1–7 | CONFIRMED | — | No change. |
| Remarks | — | `Env.head_has` fails open by default; `_prod_head_has` has no try; "read once" is defensible. | No change. Only `production_env` serves the CLI, and git's absence is refused earlier (`analyzer_binding`). |

The texts written after this pass (N13, the FLAG counts that name it, §5's fourth-pass bullet and this table) were checked by Code at source, not by an agent: `resume.py:840–848`, CLAUDE.md:127–130, and the final site check's raw.
