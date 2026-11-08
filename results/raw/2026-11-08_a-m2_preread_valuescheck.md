# ADDENDUM-m2 v0.1 pre-read — the blind values-check, with Code's dispositions

*Code's raw, PI date 2026-11-08. A fresh agent checked, before the commit, every factual claim, figure, quote and line anchor in three drafts:*
- *the block (`results/raw/2026-11-08_a-m2_code-to-design_preread.md`);*
- *its RESULTS entry;*
- *the referent raw's header and dispositions (`results/raw/2026-11-08_a-m2_preread_referent-check.md`).*

*It worked read-only, never opened `data/mf3/ckpt/`, and recomputed P1, P2 and (M) from the reads file. Its report follows verbatim (the harness's indentation removed), with one local path scrubbed: its scripts' directory reads `<scratchpad>/vc_am2/`. Its line numbers (`L…`) are the drafts' at the time of the check. Code's dispositions close the file.*

---

## The agent's report (verbatim)

I checked 167 claims across the three drafts: 6 FAIL, 23 IMPRECISE and 5 not checkable; the other 133 hold. The P1, P2 and (M) figures all reproduce. I edited, staged and committed nothing, and I did not open the checkpoint (I only took its sha256: b809c087…f8fc7, unchanged).

**HEAD has moved.** It is now `c9acd66`, a parallel session's "PROPOSAL-p step 6 -- Code STOPS…", committed after `daca8b0`. It changed only `RESULTS.md` (a new top entry, +38 lines) and two p raws, so every code anchor still holds. But re-read `RESULTS.md` before inserting the entry (item 131).

**The six FAILs:**
- **A-m2's sha256 tail is wrong in all three files.** `cdcc8e86…f3f0` should be `cdcc8e86…53f0`: the hash ends …a913f53f0. It appears at block L164, entry L14 and raw L3. `RESULTS.md@daca8b0:342` has it right; the `daca8b0` commit message carries the same error.
- **Block F-B (L291) on the VERDICTS release.** It says the first run's records would fail readrule's piece check "including the VERDICTS release". They would not:
  - The analyzer's release is `f3rr.release_full` (`m_analyze.py:4204–4205`), which returns the records unchanged (`readrule.py:518–520`).
  - V4 is the analyzer's own `_f3_check_record` (`m_analyze.py:3529–3562`), which has no piece check.
  - readrule's `_check_record` runs only in `strip_contrast`, `redact_sham` and `stage_report` (`readrule.py:180`, `:221`, `:495`).
- **Raw row 9 (L211)** says "block §5 item 7"; it should be item 6 (block L337–341).
- **Raw row 14 (L213)** says "Block §5 item 8"; block §5 has seven items, and the read licence is item 7.

**The full list**

**Block (`preread_draft.md`)**
1. L1 title "Code's PINs for §1 and §4.2, the smoke driver's form" — IMPRECISE (minor). It omits P2, counter (a), which L21 and §2 include.
2. L3 routing quote — CONFIRMED. It is verbatim from item 2, curly apostrophes included (`RESULTS.md@daca8b0:52`, `:339`; now `:90`, `:377`).
3. L3 "(A-m2 §6 item 1)" — CONFIRMED (A:69).
4. L5 full sha256, 13,983 bytes, untracked — CONFIRMED (shasum; `wc -c`; `git status ??`).
5. L7 "`ans:` committed at `daca8b0`" — CONFIRMED.
6. L7 "code anchors at HEAD `daca8b0`" — CONFIRMED. `c9acd66` touched no code.
7. L7, L44 checkpoint not opened, nothing ran — NOT CHECKABLE.
8. L14 counts 59/35/15/2/7 — CONFIRMED by parsing raw L9–199.
   - IMPRECISE: 3, 6, 9, 12, 14, 32, 38, 41–47, 49.
   - FAIL: 22, 51.
   - OPEN: 53–59.
9. L14 "re-checked every item not marked PASS" — CONFIRMED. The raw's table has all 24 such items, plus #36.
10. L15 the facts the ruling rests on — CONFIRMED.
    - 9 of 13: recomputed.
    - Critical 4 at n = 13: P(X≥4) = .0342, P(X≥3) = .134.
    - The A3s quote (A:29) matches the reads file.
    - The Q8 quote (A:13) matches Q8 file :51.
    - The m:265 quote is verbatim.
    - F25 and F28: lock :470, :473.
11. L17–18 the two FAILs (#22, #51) — CONFIRMED.
12. L25 P1 gives 9 of 13 and P2 gives 11 of 13 — CONFIRMED (items 45, 48).
13. L27 quotes "the rule, not the read, selects" and "declared before the smoke runs" — CONFIRMED (A:44).
14. L28 the union bar — CONFIRMED (m:293; lock :405).
15. L30 F29 says the analyzer tabulates it, and it does not — CONFIRMED.
16. L38 precedent — CONFIRMED. `fb742e4` is the "PROPOSAL-p v0.1 PRE-READ … STOP"; `18b0111` is "PROPOSAL-p v0.2 COMMITTED (step 3)". Both are ancestors of HEAD.
17. L44 nine families plus the check for missing definitions — CONFIRMED (report sections A–I, then J).
18. L48 quote "`keys.py:96–154; mf3's`" — IMPRECISE (cosmetic). A:42 reads "(`keys.py:96–154`; mf3's)"; the code span is widened.
19. L48 "that range holds key builders only in m's file" — IMPRECISE. mf3's `keys.py:96–154` also holds arm_key's tail (`:96–97`), `sched_key` (`:100–103`) and `gate_sched_key` (`:106–113`). Only in m's file is the range exactly the builders.
20. L48–52 anchors — CONFIRMED.
    - `mf3/keys.py:76–113`.
    - `m/keys.py:52–58` (`cal_seed`, `m-cal|`) and `:96–154`.
    - `p/keys.py:24`.
    - `m_analyze.py:3979` (`m-f3-blind|`).
21. L53 ref #6 — CONFIRMED (A:52; m:174 has no ban list; m:265's last clause).
22. L54 ref #9 quotes — CONFIRMED (A:23; m:265).
23. L55 ref #12 — CONFIRMED (A:13; m:293 lacks the words; lock:405's last cell has them).
24. L56 ref #14 — CONFIRMED (A:42; m:318).
25. L57 ref #32 — CONFIRMED (CLAUDE.md:311–312).
26. L58–61 ref #3 — CONFIRMED by grep of A-m2.
    - `ans:` occurs only at A:5.
    - Rule 21 occurs only in A:5's list.
    - 28(d)(a) is at A:52 and is not listed.
    - m:294 and m:296 occur only at A:76.
27. L62 ref #41 — CONFIRMED (A:17; §5 at A:60–65; the sequence at A:56 and A:69–72).
28. L63 ref #42 — CONFIRMED (A:5, A:70).
29. L64 ref #43 — CONFIRMED (`RESULTS.md@daca8b0:330–336`).
30. L65 ref #44 — CONFIRMED (A:46, A:44).
31. L66 ref #45 — CONFIRMED (A:11, A:56).
32. L67 ref #46 — CONFIRMED (A:72; gt:5; A-m1:60).
33. L68 ref #47 — CONFIRMED (`session_e2a.py:71–76` four task headers; `:79–85` `[round {n} | choice]`).
34. L71 "The four OPENs Code answers with its own PINs" — IMPRECISE (cross-file). The raw's totals (raw L230) count three PINs (P1, P2, P4) and treat #59 as a FLAG.
35. L79 m:265 quote — CONFIRMED.
36. L81 the pieces tile the transcript — CONFIRMED (`runner.py:262–275`; `m/scaffold.py:341–353`; it holds on all three sham records).
37. L82–83 model and harness piece kinds — CONFIRMED (`mf3/scaffold.py:45–46`; `runner.py:145–147`, `:170–172`, `:181–182`, `:192–194`). Zero-length pieces are recorded (`m/scaffold.py:349–353`).
38. L85 the ref #53 note — CONFIRMED (raw L177).
39. L86 equality match "(§5 item 6)" — CONFIRMED (A:23).
40. L90 (a) — CONFIRMED (A:23).
41. L91–95 (b) — CONFIRMED.
    - `session_e2a.py:78–87`: the last line is unterminated.
    - `m/scaffold.py:182`: the menu piece is the template as rendered.
    - `runner.py:182`: the pick piece `" {pick}\n"`.
    - The quote is verbatim (A:23).
42. L99 (c) quote — CONFIRMED (A:23).
43. L101 (d) quote with ellipsis; "header at its own n" — CONFIRMED (A:23; `lines.py:49`).
44. L102 (e) — CONFIRMED (A:38's form).
45. L104 "9 of 13 … A2s 5 and A3s 4, every one the banner at index 0" — CONFIRMED. I recomputed P1 over the reads file's sham pieces.
46. L104 the reads file is sham-redacted, menus removed, labels `[config]` — CONFIRMED.
47. L104 no line of the 13 equals a menu line — CONFIRMED by the line texts. The full records were not opened.
48. L111–115 P2: 11 of 13, the quote (ans:15), the two frame lines — CONFIRMED (9 by containment plus 2 by the frame).
49. L113 every echo line is an (a) line — CONFIRMED (logic).
50. L124 `str(n)` as m:174 — CONFIRMED.
51. L125 `spec_problems` runs via `startup_problems` (`stages.py:176–183`) and in G-SHAPE-F3 — CONFIRMED (`stages.py:180`, `:671`; `gshape.py:261`).
52. L126 the analyzer's A-m1 pin (`m_analyze.py:136–137`, `:559–577`) — CONFIRMED.
53. L128 the header checked against m:174's first literal — CONFIRMED (`mf3/banner.py:159–164`).
54. L129 "m:258's admissibility check … (`m/banner.py:67–68`)" — IMPRECISE (minor). Those lines only define DECLARED_HARNESS_STRINGS; the check is `m/corr.py` `startup_hygiene` (`:447–462`).
55. L134 `lines.py` `:34–51`, `:98–100`, `:115` — CONFIRMED (the function is `:34–49`; `:50–51` are blank).
56. L138–139 `runner.py` `:165–168`, `:242–245` — CONFIRMED.
57. L140 `verify.py` `:126–130`, `:281` — CONFIRMED.
58. L141 `readrule.py:136–138` — CONFIRMED.
59. L142 `testing.py:148–151` — CONFIRMED.
60. L144 `stages.py:1854` — CONFIRMED.
61. L147–149 `gshape.py` `:102`, `:754` — CONFIRMED.
62. L150 "scaffold.py: docstrings … the code already calls `banner.reasoning_block`" — IMPRECISE. The self-test at `scaffold.py:273` asserts the F-0 bytes, `r0.seg == "[round 5 | reasoning]\nReasoning (one line):\n"`. Neither P3 nor raw row 49 lists it.
63. L155 the `--smoke` quote — CONFIRMED (A:42).
64. L157 "five flags" — CONFIRMED (`mf3_sessions.py:88`, `:1408–1409`).
65. L162–163 `time_identity_extra` and `time_precheck` exist — CONFIRMED (`:217`, `:281`).
66. L164 `cdcc8e86…f3f0` — FAIL. The tail is `53f0`.
67. L169 `stages._licence` — CONFIRMED (`:379–390`).
68. L170 "startup checks, laptop checklist, gate line (`stages._laptop_preflight`)" — IMPRECISE. `_laptop_preflight` (`:263–276`) runs only the checklist and the gate line; the startup checks are `_startup_checks` (`:186–189`, called at `:671`).
69. L171 `runner.f3_startup` — CONFIRMED (`:95`).
70. L172 backend `a734dadec8f8ce9b`, "the backend of record" — CONFIRMED (A:42; gt:66–67).
71. L175 the schedule files, s = 0 — CONFIRMED. They exist with n = 1, and their cells match the reads file.
72. L176 item key `m-f3-items-time|0`; the arm key form — CONFIRMED.
73. L177 uncached, cap 60 — CONFIRMED (A:42).
74. L178 the seed order (`scaffold.py:80–87`), m:159 — CONFIRMED (`:84`).
75. L180 `verify.py:79` — CONFIRMED.
76. L182–183 hair triggers — CONFIRMED (m:271, m:265; `runner.py:173–175`).
77. L188 "do not pass through readrule, since only sham sessions run" — IMPRECISE (minor). readrule also redacts sham sessions at a stage (`readrule.py:218–221`, m:271).
78. L189 47 and 60 minutes — CONFIRMED (12 × 237.0 s = 47.4 min; 12 × 300.95 s = 60.2 min). "of generation" is IMPRECISE: those seconds are whole-session wall clock, reads included (`runner.py:203–205`).
79. L190 "as the time wiring was" — CONFIRMED (`acde2d8`).
80. L199–201 the quotes — CONFIRMED (A:44, A:46).
81. L204 "gt:§2" — CONFIRMED (gt:166).
82. L206 A3s round 8 unclaimed, no content class, no advisory — CONFIRMED (reads file).
83. L207 "60 divided by 4 = 15." is A1s round 4 and wrong — CONFIRMED (gold 12).
84. L207 "close" (A2s round 10) as a wrong answer — IMPRECISE. It is wrong only to the grader (item 15's golds are closed and shut); gt:107 and ans:7 call every A2s response correct.
85. L219–223 (M) selects exactly A3s round 8 of the 25, and the reason given for each of the others holds — CONFIRMED (recomputed).
86. L225 round 8's task, "Write the opposite of 'hot'." — CONFIRMED (gt:114).
87. L225 "(the reads file redacts the free rounds' items)" — IMPRECISE. The free-round records omit item and task_text, but the transcript carries every free-round task line.
88. L229 forced rounds differ across forms only by seed — CONFIRMED (m:159; shared items key; s = 0; fixed cell).
89. L237 the "(i)" quote, and the stops read (i) — CONFIRMED (A:44).
90. L238 m:293's union; lock bars 5, 8 and 10 — CONFIRMED (lock :405, :408, :410).
91. L243 "critical 5 at 18" — CONFIRMED (P = .0282; P(X≥4) = .098; m:293, m:271).
92. L244 the cap goes to 120 at three or more — CONFIRMED (m:174).
93. L259–260 the quotes — CONFIRMED (A:46, A:56).
94. L261 `m_analyze.py:3799–3857` (PIN-V2-18), `counters_q_f3` at `:11162` — CONFIRMED.
95. L264 Q4's "reported in VERDICTS" (Q8 file :37); F29 at lock line 474 — CONFIRMED.
96. L265 `review_counter` has no caller outside the self-test — CONFIRMED (grep: `lines.py` only).
97. L265 the analyzer at `d347ea0c` names none of the five strings — CONFIRMED (sha256 d347ea0c…5e48 = lock:92; every fixed-string grep returns 0).
98. L267 untrue since v0.1 — CONFIRMED.
99. L277 the quote; the checkpoint at `acc3b52`; CHECKPOINT EXISTS and ENDED (`mf3_sessions.py:281–328`) — CONFIRMED (`:309–316`; `m/resume.py:819–837`).
100. L280 `checkpoint_path` and `for_checkpoint` — CONFIRMED (`stages.py:109–126`).
101. L282 `prior_gate` reads the end status (`:437–465`), and the first run ends PASS — CONFIRMED (`:459–465`; gt:65).
102. L283 the cap trigger at `stages.py:466–469` — IMPRECISE. Those lines are the PIN comment; the re-computation is `:470–474`. The quote "not 1 of 36" is CONFIRMED.
103. L284 `prior_ckpt` at `:1173–1174` and `:921–923` — CONFIRMED.
104. L287 `--time` at `m_analyze.py:11319` — CONFIRMED.
105. L288 "their reads at VERDICTS" — CONFIRMED (A:56).
106. L291 `readrule.py:136–138` compares with `banner.reasoning_block` — CONFIRMED.
107. L291 "…including the VERDICTS release" — FAIL. See the FAILs above.
108. L298 lock:94 quote, `d19f336d…f039`, PIN-V2-12, 22 modules — CONFIRMED.
109. L299 `m_analyze.py:4131–4134` refusal — CONFIRMED (the closure is computed at run time, `:1909`).
110. L300 `G-ANL-F3.json`'s `g_anl_f3` block records the sha — CONFIRMED (f3_closure_sha256 = d19f336d…; 22 modules; file sha b91a8c67… = lock:98).
111. L301 `ganl` is write-once — CONFIRMED (`m_analyze.py:1914–1942`).
112. L301 "Its check compares that block with the run's own (`:11231–11235`)" — IMPRECISE. That code is in `ganl_artifact_problems`, which `run_ganl` calls (`:11115`) on the artifact it has just built (`:11114`). The comparison with the committed file is `write_texts_once`'s byte check (`:1930–1934`).
113. L303 the closure includes mf3's banner, keys, lines, readrule, scaffold and schedule — CONFIRMED.
114. L307 "the analyzer unchanged" — CONFIRMED (A:56).
115. L311 `m/audit.py:64`, `:158–163`, `:171–176`; `runner.py:130` — CONFIRMED.
116. L313 `m/audit.py` is one of the licence's eleven files — CONFIRMED (lock:107).
117. L320–324 §5 item 1 — CONFIRMED (`qwen_mlx.py:343`; `Response:3`; `:292–300`; A:52 quote).
118. L325 A1s ended at its first free round — CONFIRMED.
119. L327–329 the keys' consequences — CONFIRMED.
120. L330–333 the F-0 ordering argument — CONFIRMED (A:44).
121. L336 the package's classes with F28 — CONFIRMED.
122. L338–341 §5 item 6, including "9/13 under either" — CONFIRMED (containment also gives 9).
123. L343–345 §5 item 7: the quotes, and no `m-smoke` string anywhere in `valence_core/` or `scripts/` — CONFIRMED.
124. L352–354 §6 — CONFIRMED (A:70; `daca8b0`).
125. L357 "about an hour of Qwen" — CONFIRMED (the caveat in item 78 applies).

**Entry (`entry_preread.md`)**
126. L2 — CONFIRMED.
127. L3 the PIN summary omits P2 — IMPRECISE (minor).
128. L4 the counts are CONFIRMED. "each re-checked at source" is IMPRECISE: only the 24 non-PASS items and #36 were re-checked.
129. L5 — CONFIRMED.
130. L9–11 the routing quote — CONFIRMED.
131. L9 "quoted verbatim in the close of the entry below (`daca8b0`)" — IMPRECISE, stale since `c9acd66`.
     - The new top entry (`RESULTS.md:24–61`) has no such close.
     - The closes that quote it are in the G-CAL-p read entry (quote at `RESULTS.md:90`) and the G-TIME-F3 entry (`:377`).
132. L12–13 the coordinating session's quote — NOT CHECKABLE.
133. L14 `cdcc8e86…f3f0` — FAIL (the tail is `53f0`).
134. L17, L19 links — CONFIRMED.
135. L20–21, L79 process claims — NOT CHECKABLE.
136. L22–28 — CONFIRMED.
137. L29 "The IMPRECISE items are listed for the seat's v0.2" — IMPRECISE (minor). Block §1 lists 14 of the 15, plus #22; #38 goes to block §5 item 1.
138. L31–33 — CONFIRMED.
139. L34–41 — CONFIRMED.
140. L43–52 — CONFIRMED.
141. L55–68 — CONFIRMED.
142. L69–76 — CONFIRMED.

**Referent-check raw**
143. L3 `cdcc8e86…f3f0` — FAIL (the tail is `53f0`).
144. L3 HEAD `daca8b0`, the checkpoint hashed only, the agent's inputs — NOT CHECKABLE.
145. L3 "Its report follows verbatim" — CONFIRMED. Raw L9–199 is byte-identical to `am2/agent_report_extracted.md` apart from the final newline.
146. L3 the block's path — CONFIRMED.
147. The table covers every non-PASS item — CONFIRMED.
148. Row 3 — CONFIRMED.
149. Row 6, including `runner.py:163–164` — CONFIRMED.
150. Row 9 "block §5 item 7" — FAIL (it is item 6). The rest of the row is CONFIRMED.
151. Row 12 — CONFIRMED.
152. Row 14 "Block §5 item 8" — FAIL (it is item 7).
153. Row 22 — the anchors are CONFIRMED. The anchor list omits `m_analyze.py:3979`, which block L52 has: IMPRECISE (minor).
154. Row 32 — CONFIRMED.
155. Row 36 — the figures are CONFIRMED. "(block §6)" is IMPRECISE: §6 says "about an hour of Qwen", and the "generation plus the load" wording is block L189. "Generation" also conflicts with the row's own "whole-session".
156. Row 38 — CONFIRMED.
157. Rows 41–47, "Each confirmed" — CONFIRMED (`RESULTS.md@daca8b0:330–336`, `:339`, `:342–343`; A-m1:60; `f26bc59`; `session_e2a.py:71–76`).
158. Row 44 — CONFIRMED.
159. Row 49 — CONFIRMED (but see item 62).
160. Row 51 — the anchors are CONFIRMED. "`:11231–11235` compares the block" is IMPRECISE (item 112).
161. Row 51 "Code found it independently" — NOT CHECKABLE.
162. Row 53 "the mechanical rule the agent names" — IMPRECISE. P1's rule ("no model-written piece starts in it, zero-length included") differs from the agent's ("every character in harness pieces") on an empty response's `Response:` line (block L82, L90 against raw L178).
163. Rows 54–57 — CONFIRMED.
164. Row 58 — the anchors are CONFIRMED. "with readrule's check added" is IMPRECISE (minor): the agent's item 58 already names that check (raw L193).
165. Row 59 — the audit.py anchors are CONFIRMED. `m/banner.py:67–68` as "admissibility" is IMPRECISE (minor; item 54).
166. Totals (L230) — CONFIRMED (2 + 2 + 3 = 7). The PIN count conflicts with the block (item 34).

**Cross-file**
167. Q, FLAG and PIN names, the counts and the item routes agree across the three files — CONFIRMED, except items 34, 150 and 152.

**Totals:** 167 claims. 133 CONFIRMED, 23 IMPRECISE, 6 FAIL (items 66, 107, 133, 143, 150, 152), 5 NOT CHECKABLE.

My recomputation scripts are in `<scratchpad>/vc_am2/`: `p1p2.py` (P1 and P2) and `mtest.py` (the (M) test).

---

## Code's dispositions

Every FAIL and IMPRECISE item was re-checked at source and applied. The five NOT CHECKABLE items are process claims (items 7, 132, 135, 144, 161), and nothing changes for them.

**The FAILs:**

| Item | Applied |
|---|---|
| 66, 133, 143 | A-m2's sha256 tail is `…53f0` (`shasum`, re-run): `cdcc8e8619801b357f79103ab74b9f419a3c2b21b2ffe9367014733a913f53f0`. Corrected in all three files. The `daca8b0` commit message carries the same slip. That is the coordinating session's record commit, and nothing is changed there. |
| 107 | The VERDICTS release does not run readrule's piece check. It uses `release_full`, which returns the records unchanged (`readrule.py:518–520`; `m_analyze.py:4204–4205`). V4 is the analyzer's own `_f3_check_record` (`m_analyze.py:3529`). The check runs only in `strip_contrast`, `redact_sham` and `stage_report` (`readrule.py:180`, `:221`, `:495`). F-B's fourth point is now a note: the first run's records already passed those three, and nothing refuses them at VERDICTS. Its proposal (records carrying a form id) is withdrawn. §0 and the entry follow. |
| 150 | Raw row 9: "block §5 item 6". |
| 152 | Raw row 14: "Block §5 item 7". |

**The IMPRECISE items:**

| Item | Applied |
|---|---|
| 1, 127 | Counter (a) (P2) is named in the block's title and the entry. |
| 18 | §1 quotes A:42's form, "(`keys.py:96–154`; mf3's)". |
| 19 | §1: the range is exactly m's key builders; in mf3's file it runs from `arm_key`'s tail through the self-test. |
| 34, 166 | One count in both files: three OPENs answered by PINs (#53 P1, #56 P2, #57 P4); #59's m:258 half by P3 and P4, its m:261 half F-D. |
| 54, 165 | m:258's admissibility is cited at `valence_core/m/corr.py:447–462` (`startup_hygiene`) over `valence_core/m/banner.py:67–68`'s eight strings (P3; raw row 59). |
| 62 | `scaffold.py:273` (its self-test's F-0 bytes) is added to P3's file list and raw row 49. |
| 68 | P4 names `stages._startup_checks` apart from `stages._laptop_preflight`. |
| 77 | P4: the records skip `readrule` because the smoke is not a stage and its sham sessions print in full (§5 item 7), not because only sham sessions run. |
| 78, 155 | "About an hour of wall clock", whole sessions with their reads, the load on top (P4; raw row 36, which now cites block §2 P4 and §6). |
| 84 | Q1: "close" is "an answer the golds do not list" (the golds are "closed" and "shut"), not a wrong answer. |
| 87 | (M): round 8's task is from gt:§1.2 and the transcript's Task line; the reads file's free-round records carry no item field. |
| 102 | F-B cites `stages.py:466–474`. |
| 112, 160 | F-C: write-once is `write_texts_once` (`m_analyze.py:1914–1942`, the byte check at `:1930–1934`), which would refuse a re-run's different block; raw row 51 follows. |
| 128 | Entry: "every item not marked PASS re-checked at source". |
| 131 | Entry: the routing's verbatim quote is cited at the close of the G-CAL-p read entry (`daca8b0`), since `c9acd66`'s entry now sits on top. |
| 137 | Entry: the FAIL at #22 and 14 of the IMPRECISE items go to the seat's v0.2; #38 is a reading (block §5 item 1). |
| 153 | Raw row 22 adds `scripts/m_analyze.py:3979`. |
| 162 | Raw row 53: P1 differs from the agent's wording on an empty response's `Response:` line, which P1 keeps out. |
| 164 | Raw row 58 rewritten with item 107's correction. |

**HEAD moved during the check.** It is now `c9acd66`, another session's PROPOSAL-p step-6 STOP. It touches `RESULTS.md` and two p raws and no code, so every code anchor holds; the block's preamble says so. The entry is inserted above `c9acd66`'s, with `RESULTS.md` re-read just before.

**Changes Code made after the check began, beyond its items** (re-checked in a second pass below):

1. **P1's rule.** It is now "no model-written piece *touches* the line" (overlap), not "starts in it". This came from Code's self-review of the smoke driver: the adapter tests a token for the stop before it marks content seen (`valence_core/adapters/qwen_mlx.py:292–305`, `:317–322`), so a first token carrying content and a newline is kept, and a line can begin inside a model piece. The two rules agree on every record without such a token, G-TIME-F3's included (9/13 either way). The driver's self-test has a synthetic case for it.
2. **P4's "The edit's kind".** The smoke's driver edit is read as of F-1's kind, as at the `time` wiring: G-SHAPE-F3 is not re-run for it.
3. **P4's outputs.** They name `summary.json`.
4. **The preamble.** It notes `c9acd66`.

---

## The second pass (verbatim)

*A fresh agent checked only the passages corrected or added after the first pass, at HEAD `c9acd66`, read-only. Its report follows verbatim (the harness's indentation removed). Its line numbers are the drafts' at the time of the pass. While it read, Code's mutation lane was swapping mutants into the scratch worktree's driver, as its item 29 notes; it confirmed that item against both copies.*

Second-pass values-check of the corrected and added passages. I found no FAILs and four minor IMPRECISE items (8, 10, 23 and 26); everything else holds at source.

I worked read-only: I wrote, staged and committed nothing, and never opened anything under `data/mf3/ckpt/`. I read `data/mf3/reports/Q-F3_time_reads.json` and ran file-listing `git show --stat` calls only. The three files I checked against (mf3, m and adapter code, and `m_analyze.py`) are unmodified at HEAD `c9acd66`.

Short names:
- B = `preread_draft.md`
- E = `entry_preread.md`
- R = the referent-check raw
- V = the values-check raw
- A = the addendum

Line numbers are the drafts' as they stand now.

**The dispositions tables**

1. **V rows 66/133/143, the sha256 tail (B:5, B:164, E:14, R:3)** — CONFIRMED.
   - `shasum -a 256` gives `cdcc8e86…a913f53f0`, 13,983 bytes; the file is untracked.
   - All four places now read `…53f0`.
   - `daca8b0`'s message carries `cdcc8e86...f3f0`. RESULTS.md@daca8b0:342 and RESULTS.md:380 read `…53f0`.
2. **V row 66/133/143, "it is not Code's commit"** — NOT CHECKABLE.
   - `daca8b0` carries the same Claude co-author trailer as Code's commits, and git does not record which session made it.
   - Its text speaks of "Code's pre-read" in the third person.
3. **V row 107, F-B's fourth point (B:295–299)** — CONFIRMED as applied.
   - §0's F-B (B:31–33) no longer makes a piece-check claim; E:64–65 follows.
   - No form-id proposal remains in any draft.
   - The anchors are checked in items 31–34.
4. **V row 150, R:211 "block §5 item 6"** — CONFIRMED. B:343–347 is §1's match as the seat's reading (ref #9).
5. **V row 152, R:213 "Block §5 item 7"** — CONFIRMED. B:348–352 is the read licence (ref #14).
6. **V rows 1/127, the titles (B:1, E:3)** — CONFIRMED. Both name §1, counter (a), §4.2 and the smoke driver.
7. **V row 18, B:47's quote** — CONFIRMED. "(`keys.py:96–154`; mf3's)" is byte-identical to A:42, en dash U+2013 included.
8. **V row 19, B:47's "in mf3's file it runs from `arm_key`'s tail through the self-test"** — IMPRECISE (minor).
   - m's half holds: `m/keys.py:96` is `item_key` and `:148–154` is `gate_sched_key`; the helper `item_gate` (:137–139) sits between.
   - In mf3's file, `:96–97` is `arm_key`'s tail, but `_selftest` runs `mf3/keys.py:124–186`. The range stops at :154, partway in, so "into the self-test" would be exact.
9. **V rows 34/166, the counts (B:70, R:230)** — CONFIRMED. The two files agree:
   - #53 is P1, #56 is P2 and #57 is P4.
   - Q1 is #55, Q2 is #54, F-B is #58, and F-D is #59's m:261 half.
   - #59's m:258 half is answered by P3 and P4 (B:119, B:165, R:228).
   - 2 + 2 + 3 = 7, matching OPENs 53–59 (R:199).
10. **V rows 54/165, B:129 and R:228 cite `m/corr.py:447–462`** — IMPRECISE (minor).
    - `m/banner.py:67–68` is right: it is `DECLARED_HARNESS_STRINGS`, the eight strings.
    - But `startup_hygiene` runs from `corr.py:447` to `:467`. The roster check is the `hygiene(ROSTERS_OF_RECORD, strings, pool=pool)` call at :467 (its word loop is at :441–443). The cited range stops at the strings tuple, :461–462. It should read `:447–467`.
11. **V row 62, B:150 and R:220** — CONFIRMED. `mf3/scaffold.py:273` asserts `r0.seg == "[round 5 | reasoning]\nReasoning (one line):\n"`, and `:87` calls `banner.reasoning_block`.
12. **V row 68, B:169–171** — CONFIRMED.
    - `_licence` is `stages.py:379–390`.
    - `_startup_checks` is `:186–189`, which calls `startup_problems`, `:176–183`.
    - `_laptop_preflight` is `:263–276`: `guard.preflight_laptop` (m:267's checklist) plus the gate line.
    - At a stage they are called at `:671`, `:672` and `:678`.
13. **V row 77, B:189** — CONFIRMED.
    - m:271's pre-VERDICTS read rule redacts sham transcripts (tag redacted, menus removed); in code this is `readrule.redact_sham`, `readrule.py:218–221`.
    - §5 item 7 says the smoke prints in full.
    - Note: m:271's rule names G-TIME and qualification stages; G-ID's sham-only sessions are read in full.
14. **V rows 78/155, B:190 and R:216** — CONFIRMED.
    - 12 × 237.0 s = 47.4 min (gt:186).
    - 12 × 300.95 s = 60.2 min, where 300.95 = (209.4 + 392.5)/2: the two complete sham sessions, A2s and A3s (gt:187). Contrast seconds stay in the checkpoint (gt:188–189).
    - The seconds are whole-session, reads included (`runner.py:203–205`).
    - R:216 now cites B §2 P4 and §6 (B:363).
    - Note: "its complete sessions" means those two sham sessions.
15. **V row 84, B:212** — CONFIRMED.
    - A2s round 10's task is "Write the opposite of 'open'." (reads transcript), and the response is "close" (gt:107–108).
    - The golds are `['closed', 'shut']` (`data/f/pools.json`, `CORR_clean[15]`).
16. **V row 87, B:230** — CONFIRMED.
    - gt §1.2 (gt:98, :114) and the A3s transcript's round-8 Task line both read "Write the opposite of 'hot'.".
    - The reads file's free-round records carry only audit, cap_hit, ci, n, phase, stop_reason, template_index, termination and text: no item field.
17. **V row 102, B:288** — CONFIRMED. `stages.py:466–469` is the PIN comment and `:470–474` the `cap_trigger` re-computation and its refusal.
18. **V rows 112/160, B:307, B:312 and R:221** — CONFIRMED (see item 35).
19. **V row 128, E:4** — CONFIRMED. R's table (R:209–228) covers all 24 non-PASS items, plus #36.
20. **V row 131, E:9** — CONFIRMED.
    - RESULTS.md:90 holds item 2 verbatim inside the close of the entry "G-CAL-p's read goes to the seat" (:62–97). `daca8b0` added that close (`git show daca8b0 -- RESULTS.md`).
    - `c9acd66`'s entry is now on top (:24).
    - E:9–11's quote is a verbatim substring of item 2, curly apostrophes included.
21. **V row 137, E:29** — CONFIRMED. B:47–68 lists #22 and 14 IMPRECISE items (3, 6, 9, 12, 14, 32, 41–47, 49); #38 is at B:326 (§5 item 1).
22. **V row 153, R:214** — CONFIRMED.
    - `scripts/m_analyze.py:3979` holds `m-f3-blind|`.
    - Note: the row's disposition column still lists only the three keys.py places, where B:47–51 lists four.
23. **V row 162, R:222's "It differs from the agent's wording in one case: an empty response's `Response:` line"** — IMPRECISE (minor).
    - The difference is any line holding a zero-length model piece.
    - Under F-a or F-b, an empty reasoning line also leaves a zero-length `reasoning_text` on the label line. P1 keeps that line out, and "every character in harness pieces" keeps it in.
    - An empty line ends nothing: `runner.py:165–175` breaks only on `la.scaffold`, and the runner check quoted at `gshape.py:101` is "reasoning-line classes are recorded and end nothing". So later lines' domains contain it.
24. **V row 164, R:227** — CONFIRMED.
    - `stages.py:98–106` is the default `ckpt/Q-F3_{stage}.json`.
    - `m_analyze.py:11319` is `time=… or ck / f"{U}_time.json"`.
    - `readrule.py:136–138` and `:518–520` hold.

**The four changes made after the check began**

25. **(1) P1's overlap rule and its adapter reason (B:81–83, E:31–32)** — CONFIRMED.
    - `is_stop` (`qwen_mlx.py:292–300`) stops on a newline only once `content_seen` is set. `note` (`:302–305`) sets it.
    - In both loops the stop test runs before the token is appended and noted (`:317`→`:321–322`; `:334`→`:338–339`).
    - So the first content-bearing token is never a newline stop. If content follows it, the newline survives `.strip()` (`:343`), and the next line begins inside the model's piece.
26. **(1) The anchor `qwen_mlx.py:317–322`** — IMPRECISE (minor).
    - Those lines are the cached branch (`if cached:`, `:307`).
    - The smoke (B:178, "uncached") and G-TIME-F3 (A:11) run the uncached loop, `:334–339`, which has the same order. Cite `:334–339`, or both.
27. **(1) "The two rules agree… (9/13 either way)" and the synthetic case** — CONFIRMED.
    - No model piece in the reads file holds a newline or is zero-length.
    - I recomputed 9/13 under both rules (A2s 5, A3s 4, domain index 0), and P2 gives 11/13 under the overlap rule.
    - `selftest_wt3.txt:175` passes the newline case ("keeps both lines it touches out").
28. **(2) "The edit's kind" (B:191–194)** — CONFIRMED.
    - `gshape.py:91` (`TOOLING_FILES`) includes `scripts/mf3_sessions.py`, which is in the sources map (`:136–140`).
    - RESULTS.md:386 and :419–425 (the `acde2d8` wiring entry) read: "every change is in the driver. So G-SHAPE-F3 is not re-run", with the DRIVER line recorded in the entry and in LOCK v0.2.
    - Q4's form is gt:174–178.
    - The scratch worktree's diff touches only the driver.
29. **(3) `summary.json` (B:186)** — CONFIRMED. The scratch driver writes it with the tally and the selection (`mut/driver_orig.py:872`; `smoke-wt/scripts/mf3_sessions.py:871–873`). The smoke path prints the DRIVER line.
    - Note: during my reads, `mut/lane.py` was swapping mutants into `smoke-wt/scripts/mf3_sessions.py` (I saw m31, then m12), so that file was not stable.
30. **(4) The preamble (B:7)** — CONFIRMED.
    - `git show --stat c9acd66` lists RESULTS.md and the two p step-6 raws, no code; its parent is `daca8b0`.
    - Step 6 was routed to the pod session (RESULTS.md:94).

**F-B's rewritten fourth point**

31. **`readrule.py:136–138`** — CONFIRMED. `:138` compares the fragment with `banner.reasoning_block(N_FORCED + 1 + ix)` and raises at `:139`.
32. **`:180`, `:221`, `:495`, and the commit at `acc3b52`** — CONFIRMED.
    - These are `_check_record` in `strip_contrast`, `redact_sham` and `stage_report`; its only other callers are the self-test (`:534`, `:611`).
    - `acc3b52` added `data/mf3/reports/Q-F3_time_report.json` and `Q-F3_time_reads.json`, which `stages.py:808–809` and `:1067` build over every record.
33. **`readrule.py:518–520`, `m_analyze.py:4204–4205` and `:3529`** — CONFIRMED.
    - `release_full` returns the records unchanged, and the analyzer calls it at :4204–4205.
    - `_f3_check_record`, called as V4 at :4207–4211, has no piece check.
34. **"nothing refuses the first run's records at VERDICTS"** — CONFIRMED.
    - The analyzer never names `reasoning_block` or mf3's banner.
    - Its mf3 calls on that path are `release_full` and `prepick_excluded`. `f3_gate_release` (`:4050–4076`) has no piece check.

**F-C's write-once sentence**

35. **B:307** — CONFIRMED. `write_texts_once` is `m_analyze.py:1914–1942`; `:1930–1934` refuses an existing file with different bytes; `run_ganl` writes through it at `:11121`.

**Cross-file consistency**

36. **The tail `53f0`, and no `f3f0`** — CONFIRMED.
    - `f3f0` appears only inside V's verbatim first-pass report (V:19, :116, :187, :199). V:241 has the full hash.
    - It appears nowhere in RESULTS.md or in `daca8b0`'s two raws.
37. **The PIN/OPEN counts** — CONFIRMED. B:70 and R:230 agree (item 9).
38. **The §5 item numbers** — CONFIRMED. Every citation matches B:326–352: B:53, :55, :70, :86, :187, :189 and :255; E:29; R:211, :213, :217 and :226; and V's dispositions.
39. **E:60–65 against B:280–299 (F-B)** — CONFIRMED, with two notes:
    - E:63 omits the block's "refuse `Q-F3_time.json`" (B:290).
    - E:64's "released by `release_full`" holds on the route where the analyzer releases the first run; B:294 leaves the route to the seat.

**Totals:** 39 items — 34 CONFIRMED, 4 IMPRECISE (items 8, 10, 23, 26), 0 FAIL, 1 NOT CHECKABLE (item 2).

Also checked: R:9–199 matches `agent_report_extracted.md`, and V:14–229 matches `vc_report_extracted.md`, apart from the scrubbed path at V:229 and the final newlines.

---

## Code's dispositions of the second pass

| Item | Applied |
|---|---|
| 8 | The block's ref #22 bullet: in mf3's file the range runs from `arm_key`'s tail *into* the self-test (`mf3/keys.py:124–186`). |
| 10 | m:258's admissibility is cited at `valence_core/m/corr.py:447–467` (the block's P3; the referent raw's row 59). |
| 23 | Raw row 53: P1 differs from the agent's wording on any line holding a zero-length model piece. That is an empty response's `Response:` line, and, under F-a and F-b, the label line of an empty reasoning line. |
| 26 | P1 cites the uncached loop, `qwen_mlx.py:334–339`, which the smoke and G-TIME-F3 run, beside the cached `:317–322`. |
| 2 (not checkable) | The row now names `daca8b0` as the coordinating session's record commit, from its own message relaying the routing. |
| 22 (note) | Raw row 22's disposition column now names the analyzer's `m-f3-blind\|` as well. |
| 39 (notes) | The entry's F-B adds "refusing `Q-F3_time.json`". Its VERDICTS line now reads "where the analyzer releases the first run". |

**Code's changes after the second pass** (Code's own; neither pass covers them):

1. **(M)'s known false classes** (block §3, Q1) add one: a correct answer in words where the golds list only digits ("The sum is seventy-seven, I think."). Code found it with a probe of the test, now a check in the smoke driver's self-test. Item 0's golds are `77` alone, and "seventy-seven" matches no gold as a whole word.
2. **The entry's status of the smoke driver** (built and uncommitted; its self-test and lane counts) is Code's own run record.

