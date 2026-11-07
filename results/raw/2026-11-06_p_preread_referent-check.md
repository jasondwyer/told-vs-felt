# PROPOSAL-p v0.1: the referent check (p §9), with Code's dispositions (Code's raw, 2026-11-06)

*For p §8 step 2. A blind referent-check agent (fresh context, read-only) checked every anchor p §9 lists, and every other anchored claim in p's body, against its source. p is untracked at root, sha256 `1821a235…9953`. The agent worked at HEAD `e0b4f2c`, which moved to `0f35954` near its end. That commit added m's three NOT-RUN records and outputs and committed the seat's answers raw with its sha256 unchanged; it touched no code file, gate artifact, m, A-m1, n or p. The agent did not recompute the renders (Code did; the renders raw). Its report follows verbatim, local paths scrubbed (`<tmp>` = Code's session scratch). Code's dispositions follow it: every item not CONFIRMED was re-checked at source before it was used. p is the seat's document, so every correction is the seat's to make in v0.2, and Code edits nothing of p.*

## 1. The report (verbatim)

**107 items: 85 CONFIRMED, 17 IMPRECISE, 3 FAIL, 2 NOT CHECKABLE.**

**HEAD.** I started on `e0b4f2c`. HEAD moved to `0f35954` near the end of the check. That commit adds the three OLMo NOT-RUN records, commits the seat's answers raw with its sha unchanged (4c3f57d4…bf82), and adds 89 lines at the top of RESULTS.md. It touched no code file, artifact, m, A-m1, n or p. RESULTS anchors below are given @e0b4f2c; add 89 to get the line @0f35954. p is still untracked with sha256 1821a235…9953 (verified). I changed nothing in the repo; my probe scripts are in <tmp>/p_refcheck/

## Header
- H1. p sha256 — CONFIRMED (shasum 1821a235…9953).
- H2. m `42ab36ec…6c6b` — CONFIRMED (tracked, clean, committed at 05c4636).
- H3. A-m1 at `f26bc59` — CONFIRMED (the only commit that touches the file).
- H4. n v0.2 at `5916097` — CONFIRMED (`PROPOSAL-n-bk-reconciliation-v0_2.md`, clean).
- H5. gcal set; schema `m-gcal-completability-v1` — CONFIRMED (entry RESULTS.md@e0b4f2c:216–325 = @6ce8b9a:24; the artifacts' `schema` field).
- H6. Seat's answers raw 4c3f57d4…bf82 — CONFIRMED.
- H7. Dating convention, m:6 — CONFIRMED ("the commit hash is the timestamp of record").
- H8. The letter o is reserved — CONFIRMED (n:4 "decision (12)'s state-present told control, if written, takes o (the PI confirmed at the 11-05 routing)"; m:16 (12)).
- H9. Rule numbers as used (9, 11, 21, 23, 25, 27, 28(c), 28(d)(a)) — CONFIRMED. §2.1's use of 28(d) is item 46.

## §0.1
1. Pod `qny1x4v8padeke`, backend identifier `641ee466f4553b6a`, box HEAD `1bf94a6` — CONFIRMED (artifacts' identity and provenance; @e0b4f2c:246, :254).
2. "the sixteen renders Qwen's G-CAL had passed" — CONFIRMED (`renders_sha256` a04f67b0… in all four artifacts; Qwen's verdict PASS).
3. Corrupted 42/44/42 of 64; clean 62/61/59; bars 7/10 and 93/128, 183/256, 177/256 — CONFIRMED (artifacts' `accuracy` and `condition_4.rel_bar`; @e0b4f2c:248–252).
4. Covariates +5/16, +17/64, +17/64; Qwen +9/64 (57/64 vs 48/64, PASS) — CONFIRMED (`covariate.fraction`; data/m/gates/G-CAL_completability_qwen.json).
5. The m:324 quote, and Qwen STOPs where OLMo goes NOT-RUN — CONFIRMED (m:324 verbatim; m:176 "(3) or (4) failing → STOP and re-specify" against "G-CAL-OLMo … NOT-RUN"; m:302).

## §0.2
6. m:338 needs the told control before an OLMo Q3 row is answered — CONFIRMED (m:338 "Answered iff its own L0-OLMo-c").

## §0.3
7. The 16 renders and their x/y/z hits — CONFIRMED (every string and every count matches the records).
8. Clean misses — counts 2/3/5 CONFIRMED; the list is IMPRECISE. It leaves out SFT clean item 4 s0, `▁4` (U+2581 then "4"; read raw :84).
   - Fix: "wrong answers (`September.`, `▁4`, `Four`, `<<April`)".
9. "`thiru` → *thirteenth* (12 of 12)" — **FAIL.** Only 6 of 12 say thirteenth (dpo and instruct, s1–s3). SFT answers 'maanum', February, 'Tishri', 'Narlei'; dpo s0 and instruct s0 refuse (read raw O1, :53).
   - Fix: "(6 of 12; the other six are SFT's four non-answers and one refusal each at DPO and instruct)".
10. "`miyms` → a year or a product" — IMPRECISE. The strings are there (`2025` ×8, `4050` ×1, plus `4.5`), but the read p cites (O1) calls these answers "multiplies or squares (2025, 4050, 4.5)", and 2025 = 45².
    - Fix: "`2025` (45², or a year), `4050` (a product), once `4.5`".
11. `ftrst`/`ybaa` listed in class (a) — IMPRECISE. All five item-8 misses give January in a corrupted spelling (`Janbaa`, `Januwy` ×2, `Janyooar`, `Janaury`), which is class (c).
    - Fix: drop it from (a).
12. Class (b) strings, concentrated on items 5/11/15, whose clean renders score 4/4/4 — CONFIRMED (records).
13. Class (c) strings — CONFIRMED (dpo/instruct 8 s2; sft 8 s2; dpo 8 s3; dpo/instruct 11 s1; instruct 1 s1).
14. Items 0, 3, 6, 12 score 16/16/16 — CONFIRMED.
15. "floor of 3 on every failing item (n_eligible 19, 10, 14, 14)" — IMPRECISE. "Failing item" is never defined. The four n values are items 2, 9, 11, 15 (≤ 2 of 4 on every checkpoint). Item 7 is 2 of 4 at instruct and sits at k = 7.
    - Fix: "on the four items at ≤ 2 of 4 on every checkpoint (2, 9, 11, 15; …)".
16. The k vectors at rates 0.10 and 0.15 — CONFIRMED (data/m/gates/G-CAL_model-free.json `renders_of_record.k`, `k_sum` 54; (10n+50)//100 clipped gives 5 at item 7 and 3 at items 4 and 10).
17. "m's operand exclusion (v1.7, m:176)" — **FAIL.** The exclusion re-specified v1.7's rule: m:176 says "lose 2, 1 and 3 positions against v1.7's rule"; archive/PROPOSAL-m-gating-campaign-v1_7.md:59 reads "fixed at rate 0.15." and v1_8.md:137 reads "…, operand excluded."
    - Fix: "(v1.8, re-specifying v1.7's rule; m:176)". The seat's answers §2 has the same slip.
18. "under b3's banner … under e2a's" — IMPRECISE. Both substrates use the same banner bytes (`banner_sha256` 6124c724… in the Qwen and the OLMo artifacts; gcal.py:44–46 "so the prompt bytes are Qwen's").
    - Fix: "on b3's generation path … on e2a's (same banner bytes, same renders)".
19. "the covariate doubles" — CONFIRMED (17/64 or 20/64 against 9/64 is ×1.9 to ×2.2).
20. "the arithmetic items with a garbled verb 4/4 on every checkpoint" — IMPRECISE. All six Compute renders garble the verb. Item 9 (`Comgute`, 1/1/0) and item 14 (`Coltute`, 3/2/2) do not score 4/4.
    - Fix: "the four arithmetic items whose operator stayed legible scored 4/4 on every checkpoint".

## §0.4
21. "(n:§0.4; figure4.csv: … 0.0366 at base, 0.978 at DPO)" — **FAIL (anchor).** n §0.4 (n:16) is "Welfare and exposure", and n v0.2 quotes no slope anywhere. The figures themselves are right: data/n/bk/experiment_results_csv/figure4.csv (tracked, sha256 c8f8dbe8…) gives base 0.03658… and dpo 0.97844…, as do A-m1:67 (§5) and :32 (§1.5).
    - Fix: "(A-m1 §1.5, §5; figure4.csv …)".
22. The row text "…was not run: dose not completable" — CONFIRMED (m:338's template filled with the phrase from `NOT_RUN_CAUSES`).
23. "≈ 3.4–4.5 h for three campaigns, m:214" — CONFIRMED.
24. "a quarter-hour of GPU" — CONFIRMED (15 min 51 s).

## §0.5 and §0.6
25. Cause code `dose-not-completable` — CONFIRMED.
26. Ledger numbers 56 and 57 — CONFIRMED (n:14 "(47 → 55)"; no other (56) or (57) found).
27. (56): five units; two golds unrecoverable — CONFIRMED (m:176 "serves all five units"; "14 of 16 golds recoverable").
28. (57): "(gcal read §4 O5)" — CONFIRMED (read raw :57). Note that O5 itself says "properties of b3's generation path"; the rule-28(d) reading is the seat's answers §3.

## §1
29. The 16 frame-word lists — CONFIRMED (re-derived from data/f/pools.json under §1.1's rule).
30. m:176's eligible positions — CONFIRMED (m:176; corr.py:187–201).
31. `keys.stream(f"corr|{i}")` — CONFIRMED (corr.py:224; keys.py:27–29 is m:176's form).
32. One permutation, one `integers(25)` draw per visited slot, the replacement formula, the roster skip — CONFIRMED (corr.py:225, :233, :236, :240).
33. The k formula; the floor of 3 is the visibility criterion — CONFIRMED (corr.py:209; m:176).
34. n (m → p), k = 3 throughout, k sums 48 against m's 54 — CONFIRMED (the m column is m:176's list and the model-free artifact; the p column re-derived as 6, 8, 8, 7, 8, 7, 6, 12, 8, 6, 8, 7, 6, 8, 6, 7).
35. m's renders for items 0 and 12 are "Clopuie 31 + 46." and "Cnmzote 11 + 33.", and those are the two items whose eligible set is unchanged — CONFIRMED (records; model-free artifact).
36. The golds column — CONFIRMED (pools.json, all 16).
37. `keys.stream_known_answer()` exists — CONFIRMED (keys.py:37–49).
38. "numpy 2.2.6" in the seat's shell — NOT CHECKABLE.
39. Conditions (1)–(2) of m:176 are structural — CONFIRMED.
40. §1.4's imports — IMPRECISE. `_k_m` (:204), `load_pool` (:176) and the roster words (:138/:141) can be imported; the replacement arithmetic cannot, because it is inline in `corrupt_m` (corr.py:236).
    - Fix: "…, with corr.py:236's replacement expression restated and asserted equal".
41. corr.py is one of the eleven m files LOCK-m-F3 v0.1 will name — CONFIRMED (@e0b4f2c:609–618: ten imported modules plus `__init__`; `corr` `74818109…7fce` matches corr.py at HEAD).
42. `data/f/pools.json` `8547d9a11ba55b95` — CONFIRMED (sha256; corr.py:80).

## §2
43. "olmo_hf.py:290–294: … content_seen set after the stop check" — IMPRECISE. Lines 290–294 are `_is_stop` alone. The check-then-set order is at :251/:256 and :274/:279.
    - Fix: "olmo_hf.py:290–294 with :251–256, :274–279".
44. The mechanism — CONFIRMED by the code: the first content-bearing token is appended whatever it carries. That it was a single token `---\n\n` cannot be checked, because no token ids are stored.
45. The two texts "---\n\nTask: Write the opposite of 'enter" and "…'help" — CONFIRMED (dpo and instruct, corrupted item 15 s0).
46. "(rule 28(d)'s class)" — IMPRECISE. 28(d)'s class is positional delivery whose boundary is found by token comparison under an encode with a length limit. This defect is a stop-discipline boundary, which is rule 13.
    - Fix: "(a declared-boundary defect in rule 13's stop discipline, analogous to 28(d))".
47. n:§8 step 6 imports olmo_hf unchanged; LOCK-n v0.1 comes later — CONFIRMED (n:159; LOCK-n v0.1 is step 10).
48. The DEL in instruct item 7 s1 — CONFIRMED.
49. m:258's eight declared strings — CONFIRMED.

## §3
50. The procedure block and seeds — CONFIRMED (artifacts' `procedure`: uncached, injections=(), newline stop, ban ids sha16 `2dd86a453a2275ef` (scaffold_{ckpt}.json per checkpoint), STOP_CAP 60, TEMP 0.7, the rule 28(d)(a) boundary assertion, seeds `crc32('m-cal|{pool}|{i}|{seed}') % 2**31`, seed 0..3).
51. No clean generation of record carries a line break — CONFIRMED.
52. "so §2.2 changes none of them" — NOT CHECKABLE.
    - Today's loop breaks before it appends the stop token (olmo_hf.py:251–254, :274–277), so any content inside the stop token before its newline (for example `.\n`) is dropped from the stored text.
    - §2.2 instead stores text up to the line break and token ids through the line-break token.
    - The records hold no token ids. Code should check the clean pool's stop tokens, or word §2.2 so it matches the existing rule once content has been seen.
53. The grader is f0's, "ported verbatim" — CONFIRMED (artifact `procedure.grader`; m:176).
54. Bars 47/46/45 — CONFIRMED (⌈.7×64⌉ = 45; ⌈¾×62⌉ = 47, ⌈¾×61⌉ = 46, ⌈¾×59⌉ = 45).
55. Covariates reported beside, including f1's 0.12 figure of +.078 — CONFIRMED (`f1_012_of_record` "0.078125 (+.078)"; m:176).
56. §3.3's tallies (20/19/18 of 24; 5/5/5 of 12; 17/20/19 of 28; clean 26/25/23) — CONFIRMED (records).
57. §3.3's "verb garbled" and "operator words now intact" — IMPRECISE against §1.2's own renders. Items 7 ("State wsbch…") and 8 ("Name ttf…") keep their verb, and item 3's "by" becomes "bh".
    - Fix: "five of the seven with the verb garbled"; "operator words intact except item 3's `by`".

## §4
58. "P/Q label delivery of m:155–159" — IMPRECISE. m:155 is §1's last paragraph and m:156–158 are blank lines and the §2 heading. The P/Q split is at m:159; the sham arms' CORR_clean is at m:172.
    - Fix: "(m:159, m:172)".
59. Item streams (m:159), floors 80/32 (m:205), α .01 and the outcome order (m:326) — CONFIRMED.
60. Hair triggers, round_degeneracy at .02 on the sham domain, the G-TIME-OLMo bar (m:271, m:302), the cadence (m:330) — CONFIRMED.
61. Blinding (m:318); the reads (m:271, m:§3) — CONFIRMED.
62. The lock chain (m:302) — CONFIRMED. "— secondary DVs" comes from A-m1:59.
63. The box-change rule (m:302, §2.4) — CONFIRMED (m:251 lies inside §2.4).
64. Hours and looks (m:205–214, m:330) — CONFIRMED.
65. Base not run, decision (7′) — CONFIRMED (m:16 (7′), (14)).
66. NOT-RUN and PENDING (m:324) — CONFIRMED.
67. m:318's decisions taken with outcomes known; A-m1's (16) — CONFIRMED (A-m1:24).
68. §4.2: Q1 (C2), `cd9756e`; imported, never copied; PIN-S10's map includes m_sessions.py; the licence form — CONFIRMED (f3-build prebuild answers :9–14; @e0b4f2c:609–618).
69. G-SHAPE-F0 — CONFIRMED (data/m/gates/G-SHAPE-F0.json; gshape.py:233).
70. §4.3: Q2's order; G-ANL-F3 lands once no OLMo unit is open — CONFIRMED (prebuild answers :20, :26; gcal answers :25). STATE: G-ANL-F3's BUILD is committed (`e0b4f2c`) and `data/m/gates/G-ANL-F3.json` is not yet committed, so §4.4 (a)'s condition is already false and only (b) remains.
71. "m:291's computations" — IMPRECISE. m:291 is G-ANL-F3 (Q-F3, plus the v2 tuples with OLMo as coordinates). The per-arm A0-OLMo outcomes are m:278 (G-ANL-F0).
    - Fix: "m:278's and m:291's computations".
72. A-m1 §2.5 (3)'s regression — CONFIRMED (A-m1:44).
73. "the prebuild answers' R1" — IMPRECISE. R1 is Code's recommendation in the G-ANL-F3 STOP (…_ganl-f3_code-to-design_prebuild.md:35), ruled at the seat's G-ANL-F3 answers A1 (…_ganl-f3_design-to-code_answers.md:7). The F3-build prebuild answers have no R1.
    - Fix: "under the seat's G-ANL-F3 answers' A1 (R1)".
74. not-run's usage — CONFIRMED at HEAD (m_analyze.py:35; subparser :11280–11287). It differs at `ed8e886` (:25; :8193–8197): `--v2-closure`/`--campaign` are new, Q-F3 is now accepted, and `date_is_clock_of_record` now comes from `clock_of_record(unit)` instead of `CLOCK_DATE`. p's command works on both.
75. `NOT_RUN_CAUSES["dose-not-completable"]` — CONFIRMED and identical (HEAD :449–450, ed8e886 :405–406: phrase "dose not completable", units "olmo").
76. `validate_not_run_record` — CONFIRMED, body identical (HEAD :632–654, ed8e886 :533–555). Its keys are exactly also, cause, date, decisions_with_other_outcomes_known, detail, schema, unit; schema `m-not-run-v1`.
77. `UNITS` — CONFIRMED and identical (HEAD :162, ed8e886 :118): ("Q-F0", "OLMo-sft", "OLMo-dpo", "OLMo-instruct"). No p unit. The analyzer blob is 6ec3222b…93d9 at HEAD and 655e0f7f…c16f at ed8e886 (= 273ca8f).

## §5
78. §5.1's chain — content CONFIRMED (m:338; A-m1:42; the m:338 "none" form); placement IMPRECISE. A-m1 §2.4 (b) attaches its sentence to §8.1's status sentence (m:343), not to the m:338 label.
    - Fix: "rows carry m:338's label; §8.1's status sentence (m:343) is followed by A-m1 §2.4 (b)'s sentence, then by one sentence…".
    - Uncounted note: the bracketed state text also differs from the seat's answers :9 ("corrupted-pool accuracy [x]/64 against 7/10 and ¾ × [clean]"). p adds the date and "/64".
79. §5.2: m:338's rule; `posting --posting v2`; PIN-23 — CONFIRMED (m:337–338; m_analyze.py:11289, HEAD only; :2660–2663).
80. C7's convention — CONFIRMED (A-m1:28; RESULTS.md@18c32df:73).
81. D2 2026-12-22; D_n 2026-12-15, D_n-lap 2027-01-15 — CONFIRMED (m:16 (11); A-m1:40; n:152).
82. "p has no decision (16)" — CONFIRMED (A-m1:24).

## §6
83. 02:20:02Z–02:35:53Z, "16 minutes … with their loads" — CONFIRMED (gcal raw :24–30: one process and one load per checkpoint).
84. m:214's 3.4/3.9/4.5 h at 160/192/224 — CONFIRMED.
85. "26 × 20–23 s + one load ≈ 15 min", sourced "from m:214 and the smoke raw" — IMPRECISE.
    - The 19.5 / 22.7 s per session is m:205's basis. The smoke raw has no per-session times (generations take 0.2–5.4 s; the loads are 211.6 / 175.7 / 183.3 s at :19, :39, :59).
    - On those figures the stage comes to ≈ 11.5–13.4 min per checkpoint, not ≈ 15.
    - m:214's figures already include these 26 sessions per checkpoint (m:205 "applied to the unit's total + 26 sessions per checkpoint"), so the ≈ 45 min is counted twice.
    - Fix: "the gate sessions are inside m:214; add one cold load per checkpoint (176–212 s) ≈ 10 min for the three".
86. $1.79/h — CONFIRMED (@e0b4f2c:288).
87. "at G-PWR, per checkpoint" — CONFIRMED (A-m1:48).
88. §6.2's respawn, BACKEND entry and box-change rule — CONFIRMED.
89. "G-ACQ (n) continues as routed" — IMPRECISE (stale). G-ACQ (n) was committed as PASS at `e7e070f` (@e0b4f2c:132); its BACKEND extension waits for the n package (GA-5).
    - Fix: "G-ACQ (n) is complete (e7e070f)".
90. m:330 cadence and round_degeneracy — CONFIRMED.

## §7 and §8
91. m:338 and m:343 — CONFIRMED.
92. Step 1's command and record fields — CONFIRMED (seat's answers :9). STATE: step 1 is now done at `0f35954`, run on HEAD's analyzer 6ec3222b… rather than the analyzer of record 655e0f7f…. p does not say which analyzer should write these records.
93. "(m:358 step 17; m:318 exception (4))" — CONFIRMED. Treating G-CAL-OLMo as a "gate-stage session" is the seat's reading (answers :7).

## §9
94. RESULTS anchors — CONFIRMED: G-CAL-OLMo @e0b4f2c:216–325 (@6ce8b9a:24); BUILD (F3) :579–678 (@cd9756e:24); G-ANL-F3 STOP :465–546 (@958e762:24), its close :498 (@54bbfe5:196).
95. Read raw §4 (O1–O7, :52–59) and §5 (:61–545) — CONFIRMED.
96. corr.py:187–200 (`_eligible_m`) — IMPRECISE. The function runs to :201.
    - Fix: "corr.py:187–201".
97. corr.py:204–209 (`_k_m`), :212–252 (`corrupt_m`); keys.py:27–29 (`stream`) — CONFIRMED, exact.
98. olmo_hf.py:237–294 — CONFIRMED (hook setup :237, loops :249–280, `_is_stop` :290–294; the file is unchanged since e26e9c9).

## 2. Code's dispositions

Each item not CONFIRMED was re-checked at source, and each finding held; item 38 stays not checkable. None changes a STOP question except item 52, which became Q2 (b); item 40 also underlies Q0. The rest are text corrections for the seat's v0.2, listed in the STOP's §4.

| Item | Verdict | Re-checked at source | Disposition |
|---|---|---|---|
| 9 | FAIL | The artifacts' corrupted item 2: SFT gives 'maanum' …, February, 'Tishri' and 'Narlei'; DPO and instruct refuse at seed 0 and say "The thirteenth month …" at seeds 1–3. | For v0.2: 6 of 12. |
| 17 | FAIL | m:176: "items 5, 11 and 15 lose 2, 1 and 3 positions against v1.7's rule". `archive/PROPOSAL-m-gating-campaign-v1_7.md:59`: "fixed at rate 0.15."; `…v1_8.md:137`: "fixed at rate 0.15, operand excluded." | For v0.2: v1.8, re-specifying v1.7's rule. The seat's answers (ans:15) carry the same slip. |
| 21 | FAIL | n:16 is "**0.4 Welfare and exposure.**". A-m1:32 (§1.5) and :67 (§5) quote figure4.csv's slopes. | For v0.2: anchor to A-m1 §1.5 and §5. |
| 8 | IMPRECISE | SFT clean item 4 has text `▁4` (a miss). | For v0.2. |
| 10 | IMPRECISE | Item 9's misses are `2025` ×8, `4050` ×1 and `4.5` ×1, and 2025 = 45². | For v0.2. |
| 11 | IMPRECISE | Item 8's five misses: `Janbaa`, `Januwy` ×2, "… is Janyooar.", "… is Janaury". All answer January in a corrupted spelling. | For v0.2: class (c), not (a). |
| 15 | IMPRECISE | m's k vector: item 7 is at k = 7 and scores 2 of 4 at instruct; the four n values 19, 10, 14, 14 are items 2, 9, 11, 15. | For v0.2. |
| 18 | IMPRECISE | Both artifacts' `procedure.prompt` starts with `SESSION_BANNER`, and both record `banner_sha256` `6124c724…`. `gcal.py:44–46`: b3's banner "is SESSION_BANNER itself". | For v0.2. |
| 20 | IMPRECISE | Corrupted items 9 and 14 score 1/1/0 and 3/2/2. | For v0.2. |
| 40 | IMPRECISE | `corr.py:236`: the replacement expression is inline in `corrupt_m`. | Q0 of the STOP. |
| 43 | IMPRECISE | `olmo_hf.py`: `_is_stop` is checked at :251 and :274, and `content_seen` is set at :256 and :279; :290–294 is `_is_stop` alone. | For v0.2. |
| 46 | IMPRECISE | CLAUDE.md rule 28(d)'s class is "any positional-delivery design whose boundary is found by token comparison … under any encode with a length limit". The O5 defect is a stop-discipline boundary (rule 13). | For v0.2 (the seat's classification). |
| 57 | IMPRECISE | The renders raw: item 7 "State wsbch …" and item 8 "Name ttf …" keep their verb; item 3's "by" → "bh". | For v0.2. |
| 58 | IMPRECISE | m:155 is §1's closing paragraph. m:159 is §2.1 (the P/Q split). m:172 has "Sham arms serve `CORR_clean` to both labels". | For v0.2. |
| 71 | IMPRECISE | m:278 is G-ANL-F0 (A0-OLMo's per-arm outcomes); m:291 is G-ANL-F3. | For v0.2. |
| 73 | IMPRECISE | (R1) is Code's recommendation in `results/raw/2026-11-06_ganl-f3_code-to-design_prebuild.md:35`, ruled in the seat's G-ANL-F3 answers, A1. | For v0.2. |
| 78 | IMPRECISE | A-m1:42, (b): "§8.1's status sentence for each OLMo row (m:343 …) is followed by one sentence". | For v0.2. |
| 85 | IMPRECISE | m:205: "OLMo basis 19.5 s per session at instruct and 22.7 s at SFT/DPO … applied to the unit's total + 26 sessions per checkpoint (24 qualification + 2 timing)". | For v0.2; it bears on the pod budget (the STOP's §4). |
| 89 | IMPRECISE | `e7e070f`: G-ACQ (n), PASS on every part run; its BACKEND extension waits for the n package (GA-5). | For v0.2. |
| 96 | IMPRECISE | `_eligible_m` ends with `return out` at `corr.py:201`. | For v0.2. |
| 38 | NOT CHECKABLE | — | The renders reproduce on numpy 2.5.1 (the renders raw). |
| 52 | NOT CHECKABLE | `olmo_hf.py:251–254` and `:274–277` break before appending the stop token. | The STOP's Q2 (b). |
| 92 (state) | — | `0f35954`: m's three NOT-RUN outputs, written at `e0b4f2c`. | The STOP's §3, recorded. |
