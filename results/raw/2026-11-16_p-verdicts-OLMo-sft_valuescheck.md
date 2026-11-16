# PROPOSAL-p OLMo-sft — VERDICTS and — secondary DVs: the blind values-check, two passes, with Code's dispositions (Code, the sft VERDICTS session; PI date 2026-11-16)

*The texts: the two entries and this session's close line on `9189623`'s entry, drafted in this session's scratch, and the run's raw (`results/raw/2026-11-16_p-verdicts-OLMo-sft.txt`), its header and closing section. Each pass was a fresh checker with shell tools only: no Python, and no checkpoint, call log or report opened. Pass 1 read the four texts in full. Pass 2 read the counters bullet (filled from the counters step's raw, `922d7a3`), every passage changed after pass 1, the rewritten close line and the raw's scrub item. The reports follow verbatim but for one scrub: this session's scratch directory is written `<scratch>`, and the repository's root `<repo>`. Calendar dates only; the commit hash is the record.*

## Pass 1

# Blind values-check, pass 1 — PROPOSAL-p OLMo-sft VERDICTS entry, secondary-DVs entry, close line on 9189623's entry, and the raw's header (1–33) and closing section (checker: a fresh session; shell tools only, no Python; HEAD 645bd3f; placeholders ⟨RAW-SHA⟩, ⟨COUNTERS⟩, ⟨VC⟩ skipped)

Conventions: `V` = `data/p/verdicts/OLMo-sft_VERDICTS.json`, `Sec` = `data/p/verdicts/OLMo-sft_secondary.json`, `In` = `data/p/verdicts/OLMo-sft_decisions.json` (all read with jq); `ans` = `results/raw/2026-11-16_p-verdicts-decisions_design-to-code_answers.md`; `blk` = `results/raw/2026-11-16_p-verdicts-decisions_code-to-design.md`; `raw` = `results/raw/2026-11-16_p-verdicts-OLMo-sft.txt`; `pre.sh` / `run.sh` = the session's scratch `pre_verdicts_check.sh` / `run_verdicts_sft.sh`; `R:` = RESULTS.md line. Verbatim quotes were compared mechanically (draft flattened, markdown wrap removed; `grep -F` / shell substring) unless noted. Every abbreviated hash was re-derived with `cut -c1-8` / `cut -c61-64` from a full sha256 computed by `shasum` or read from the output; all 18 distinct abbreviations in the drafts match.

## Text 1 — `entry_verdicts_sft_draft.md` (the VERDICTS entry)

1. Title cites p v0.2 §4.4 and §8 step 7 — CONFIRMED (p:90 §4.4 the analyzer route; p:130 §8 step 7 the VERDICTS entries).
2. LOCK-p-OLMo-sft v1.0 = `038bf3e` — CONFIRMED (`git log -- LOCK-p-OLMo-sft.md`: 038bf3e "v1.0 -- COMMITTED").
3. ADDENDUM-p1 v0.1 = `fa27c45` — CONFIRMED (`git log --diff-filter=A` on the addendum).
4. The seat's answers of 2026-11-16 = `18102d0` — CONFIRMED (`git log -- ans`: 18102d0).
5. A0-OLMo-sft PASS; P = 72/80; Δ_c = +0.4000; two-sided CP 95% CI [+0.3124, +0.4558]; E = 0.0625 from A0s-OLMo-sft — CONFIRMED (V `.arm.state`, `.arm.stats.k/.n/.delta/.E`, `.sentence`).
6. Exact one-sided p toward clean = 32490460747/2^80 — CONFIRMED (V `.tests.p_up.p` = 32490460747/1208925819614629174706176; `bc` 2^80 = 1208925819614629174706176).
7. "The output's row: OLMo-sft *Answered*" — CONFIRMED (V `.rows`).
8. ANALYZED, COMPLETE at its floors — CONFIRMED (V `.unit_state` ANALYZED, `.ended` COMPLETE, `.counts.domain` = `.floors` 80/32).
9. "G-CAL-p passed at the bar, 47/64 against 47" — CONFIRMED (V `.p.declared_sentences`; `results/raw/2026-11-08_p-gcal_design-to-code_answers.md`:9).
10. "The reads" (m:318) open; the entry closes at the seat's read — CONFIRMED (m:318; ans:41 "each entry open at "the reads""; ans:46 "Each read ... closes its entry").
11. ADDENDUM-p1 §2.4, m:318's form: computed with Q-F0's outcome known and after the re-specification — CONFIRMED (ADDENDUM-p1:30).
12. Q-F0's outcome A0 PASS at `bfc179c` — CONFIRMED (`git log -1 bfc179c`: "Q-F0 VERDICTS ... A0: PASS").
13. (p-1) committed at `fa27c45`; the input records it as its fifth item, Q-F0 PASS known — CONFIRMED (In/V `.decisions_with_other_outcomes_known[4]`, date 2026-11-15, Q-F0 / PASS).
14. The disclosure, verbatim as `p.disclosure` — CONFIRMED (mechanical match to V `.p.disclosure`).
15. It is F-p3's sentence under p §5.4 — CONFIRMED (R:6199 "Disclosure (p §5.4; F-p3's sentence, verbatim)"; R:7272).
16. p §5.4: "The disclosure is a reported fact, not a caveat on a verdict." — CONFIRMED (p:102).
17. The SFT sentence: the seat's answer of 2026-11-08, `daca8b0` §0.1, declared for "every entry, lock line and posted sentence that reports OLMo-SFT's A0 outcome"; in `p.declared_sentences` — CONFIRMED (that raw:3 "PI date 2026-11-08", :9 verbatim; `git log` on it: daca8b0; V `.p.declared_sentences`).
18. "The words (each verbatim ...)": B item 6 quoted as "6. ADDENDUM-p1 v0.1: referent check, … [go, after its commit]." — IMPRECISE. The committed verbatim record of the item (R:485 in 9189623's entry; R:1034 in fa27c45's entry) has no leading "6. "; the rest is byte-identical. Correction: drop "6. " inside the quotation marks (the item number is already given as "section B, item 6"), or cite where the numbered form is recorded.
19. The PI's routing of 2026-11-15 (evening), "Route as given", section B, item 6 — CONFIRMED (R:1014–1035).
20. The PI's word in chat "Start them" — CONFIRMED (R:487–488).
21. The PI's "Route as given" (PI date 2026-11-16) on the seat's answers to 9189623's block; section B quoted in full in the instruct session's close — CONFIRMED (R:566; instruct close R:589, items 1–6 at R:599–604).
22. "This session's close line there, for OLMo-sft, is in this commit." — NOT CHECKABLE (pending commit).
23. "the seat's item 8" — CONFIRMED (ans:66, section C item 8; R:580).
24. The PI's word "Yes, push first" — NOT CHECKABLE (no file holds it; R:469–470 records only that the runs were held for the PI's answer on item 8).
25. `origin/main` at `645bd3f`, with `db2e821` in its history — CONFIRMED (`git rev-parse origin/main` = 645bd3fe…; `git merge-base --is-ancestor db2e821 origin/main`; remote reflog "645bd3f update by push").
26. The push came before the first run / before this run — NOT CHECKABLE (no file records the push's or the runs' order).
27. One raw, `results/raw/2026-11-16_p-verdicts-OLMo-sft.txt` — CONFIRMED (file present; one invocation's stdout, raw:35–40).
28. The window was granted by the coordinating session; the third of three, after instruct's and dpo's; one at a time — NOT CHECKABLE (relayed; only the raw's own closing records it, raw:44, :46; instruct-first follows from "the second run (dpo)" + "third of three").
29. Q-F3's campaign running on this laptop — CONFIRMED (the brief's binding rules).
30. End notice "sft verdicts ended, EXIT=0", with the window released, and nothing else — IMPRECISE. The raw gives the session's whole message as "sft verdicts ended, EXIT=0. Window released." (raw:44). Correction: quote the whole message as the raw does.
31. Precheck = Code's read-only script, shell/git/shasum/jq, no Python — CONFIRMED (pre.sh:1–15).
32. Run inside the run script just before the command, output verbatim in the raw's header, ALL CLEAR at HEAD 645bd3f — CONFIRMED (run.sh:17–29; raw:7–29; raw:8 = `git rev-parse 645bd3f`).
33. Also run "once as its own call in the window" (so "run twice, both ALL CLEAR") — NOT CHECKABLE (no recorded output of that run).
34. m's analyzer `d347ea0c…5e48`, p's `d3758fc4…7008` — CONFIRMED (`shasum`; LOCK-p-OLMo-sft.md:57–58).
35. m's package_sha256 `7756dcf4…49bb`, p's `a38d93bb…a2d7`, recomputed in the shell by `package_sha256_of`'s rule — CONFIRMED (re-computed here in the shell with pre.sh's `pkg` form: both equal; rule at valence_core/m/resume.py:328–349).
36. Driver `9c641e19…a96d` and `olmo_hf.py` `df80b79b…92dc`, each named in the lock — CONFIRMED (`shasum` of scripts/p_sessions.py and valence_core/adapters/olmo_hf.py; LOCK-p-OLMo-sft.md:60, :139).
37. PROPOSAL-m `42ab36ec…6c6b`, PROPOSAL-p `42f2977b…3b32`, ADDENDUM-m1 `ea08322d…9001`, the values m's analyzer and p's package pin — CONFIRMED (`shasum`; scripts/m_analyze.py:98, :137; valence_core/p/gcal.py:90, identity.py:41).
38. Lock `fafb786d…2bc4` equal to its blob at HEAD; code paths with no tracked change or untracked file; no sft output present — CONFIRMED (`git hash-object` = `git rev-parse HEAD:LOCK-p-OLMo-sft.md` = f9253b00…; pre.sh:27–36; raw:19–24).
39. Decisions input `54df4b85…e881`, m-decisions-v1's shape (keys, unit, no PENDING, no own unit), equal to its blob at HEAD — CONFIRMED (`shasum`; pre.sh:39–46; hash-object = rev-parse = 9ae36e7f…).
40. … "added at `db2e821`" — CONFIRMED (`git log --diff-filter=A -- In` = db2e821; `git show --name-status db2e821`: A ×3 decisions files). (The script itself does not assert this; see observations.)
41. Command from the root, `nice -n 19`, `$PY` = the repository's `jlens-qwen36/.venv/bin/python`, the argument list — CONFIRMED (run.sh:9, :38–39; raw:2–3).
42. "(G-ANL-p's interpreter)" — CONFIRMED (`results/raw/2026-11-14_p-ganl.txt`:2, committed at 82c3c44).
43. `--campaign`, `--time`, `--qual` at defaults `data/p/ckpt/OLMo-sft_{campaign,time,qual}.json` — CONFIRMED (scripts/p_analyze.py:61, :177–181; V `.inputs`).
44. No `--adjudication` (no pause), no `--pi-stop` — CONFIRMED (run.sh:38–39; V `.pauses` [], `.adjudication` null, `.pi_stop_record` null).
45. Relative paths resolved against the root (`_cli_path`, `m_analyze.py:11254`; PIN-V2-8) — CONFIRMED (m_analyze.py:11254–11262; p_analyze.py:736 `cli = m_analyze._cli_path`).
46. EXIT=0, stderr empty — CONFIRMED (scratch exit file "0"; scratch stderr file 0 bytes; raw:43).
47. Printed: INVOCATION, the gate line (V0), the §5 sentence, `VERDICTS OLMo-sft: written: …`, two `P-OUTPUT` lines — CONFIRMED (raw:35–40; m_analyze.py:2244 "V0 -- the gate line"; p_analyze.py:696, :763).
48. "No battery ran at this step." — NOT CHECKABLE (session's acts; run.sh runs only the verdicts command).
49. The brief bars `p_analyze.py --selftest`, `ganl` and m's battery on the laptop while Q-F3 runs — CONFIRMED (the brief's rules as given to this checker).
50. G-ANL-p's run of record is `82c3c44`'s — CONFIRMED (R:2415–2419: the canonical re-run, `ba89279`'s artifact superseded; 82c3c44 subject).
51. Outputs written once (`p.staging`) — CONFIRMED (V `.p.staging`: "wrote the file once").
52. `OLMo-sft_VERDICTS.json` sha256 2795b610…853c (full) — CONFIRMED (`shasum`; raw:39).
53. `OLMo-sft_secondary.json` sha256 e9cfe52d…fa54 (full) — CONFIRMED (`shasum`; raw:40).
54. Each equal by `shasum` to its `P-OUTPUT` line — CONFIRMED.
55. Schemas `m-verdicts-v1`, `m-secondary-v1`, each with `proposal_p_sha256` `42f2977b…3b32` — CONFIRMED (V/Sec `.schema`, `.proposal_p_sha256`).
56. `.gitignore` admits `data/p/verdicts/*.json` already (:311–313), no `-diff` — CONFIRMED (.gitignore:311–313; `git check-ignore -v` → :313; `git check-attr diff` → unspecified).
57. "Committed by path in this commit, with the raw." — NOT CHECKABLE (pending).
58. Inputs: lock `fafb786d…2bc4`, decisions `54df4b85…e881`, repository-relative paths — CONFIRMED (V `.inputs`).
59. Campaign `28c52e58…9ed2`, equal to the copy-back raw's (`41bfab4`) — CONFIRMED (V `.inputs.campaign`; `results/raw/2026-11-15_p-campaign_copyback.txt`:9; `git log` on that raw and on the checkpoint: 41bfab4).
60. Time `aa56d5cf…d3e2`, equal to its stage raw's (`2258c52`) — CONFIRMED (`results/raw/2026-11-09_p-gtime.txt`:8, :64, :242; committed 2258c52).
61. Qual `1dff86df…4af8`, equal to its stage raw's (`a225a89`) — CONFIRMED (`results/raw/2026-11-11_p-qual.txt`:9, :83, :335; committed a225a89).
62. The analyzer alone read the checkpoints; this session opened, listed and hashed none — NOT CHECKABLE (session's acts).
63. Pins: `proposal_sha256` m's `42ab36ec…6c6b` (kept m's, p §4.4), `proposal_p_sha256` beside — CONFIRMED (V; p:90).
64. `analyzer_sha256` `d347ea0c…5e48`, `package_sha256` `7756dcf4…49bb`, `closure_sha256` `a3bc7bb9…b22b` — CONFIRMED (V).
65. p block: `scripts/p_analyze.py` `d3758fc4…7008`; `valence_core/p` `a38d93bb…a2d7`; D_p 2026-12-15 (p:100) with no problem; register entry (3), `clock_of_record`, `crosscheck_coordinate` — CONFIRMED (V `.p.analyzers`, `.p.d_p` problems [], `.p.register[0]` n 3; p:100).
66. Decisions: m:318's record, PIN-35, the seat's Q1 (c) — CONFIRMED (m:318; m_analyze.py:657–666; ans:7, :15).
67. Six items verbatim from the input as the output carries them, each Q-F0 / PASS — CONFIRMED (sorted-key jq of V and In lists hash equal; each item's text and date matched mechanically).
68. Item 1, 2026-11-06, ADDENDUM-m1 decision (16) text — CONFIRMED (V/In [0]).
69. Item 2, 2026-11-07, PROPOSAL-p adopted text — CONFIRMED ([1]).
70. Item 3, 2026-11-14, cap share "2 h each" text — CONFIRMED ([2]).
71. Item 4, 2026-11-14, "Place the locks" text — CONFIRMED ([3]).
72. Item 5, 2026-11-15, (p-1) text — CONFIRMED ([4]).
73. Item 6, 2026-11-15, the campaigns' go text — CONFIRMED ([5]).
74. `p.decisions_beside`: m's three NOT-RUN outputs, each "dose not completable", committed at `0f35954` — CONFIRMED (V `.p.decisions_beside`; `git log --diff-filter=A` on each: 0f35954).
75. Their sha256s `72745cb4…b5b0`, `94869b83…8e96`, `e2ecef56…87e8` — CONFIRMED (`shasum` of the three files; V).
76. "Item 1 is in m's three records too." — CONFIRMED (`grep -c -F` of item 1's text = 1 in each `data/m/verdicts/OLMo-*_not-run-record.json` and `*_NOT-RUN.json`; date 2026-11-06 in the sft record).
77. Items 2–6 and the goes came after them; `0f35954` is an ancestor of `18b0111` and `ec0d9d3` — CONFIRMED (`git merge-base --is-ancestor`, both; also of 38f9974, the rulings the 2026-11-07 routing confirmed).
78. The goes: each taken with Q-F0's PASS and m's NOT-RUNs known; listed as the joint block's (iv) gathers it — CONFIRMED (bfc179c ancestor of 0f35954; blk:182–199; the campaigns' go of (iv) is item 6 of the input under Q1 (c)).
79. G-CAL-p: the PI's routing of 2026-11-07, item 1, quote; `ec0d9d3` — CONFIRMED (R:6188–6189; blk:183–184; ec0d9d3 = the G-CAL-p entry).
80. LOCK-p v0.1 and G-TIME-OLMo (p): routing of 2026-11-08, item 2, quote; each LOCK-p v0.1's header — CONFIRMED (the quote is in LOCK-p-OLMo-{sft,dpo,instruct}.md, one each; sft :256).
81. LOCK-p v0.2 and G-F0m-OLMo (p): routing of 2026-11-10, B1, quote; each LOCK-p v0.2's header — CONFIRMED (in all three locks; sft :161).
82. G-PWR (p), the campaign wiring, LOCK-p v1.0: routing of 2026-11-13, item 4, quote; `a2c354e` — CONFIRMED (R:3342, the routing block's item 4; the elision matches blk:189–191; a2c354e = the close carrying it).
83. These sessions: 2026-11-15 (evening) B.6 "[go, after its commit]" and "Start them" — CONFIRMED (R:485, :487–488).
84. The seat's ruling (its §1) verbatim — CONFIRMED (ans:17, mechanical).
85. Three inputs committed at `db2e821` before the first run — CONFIRMED (db2e821 adds the three files; its subject: "committed before the first run"; R:615–632).
86. "No session read a sibling's output before this run, the third, ended, and each end notice carried the exit status alone." — FAIL (unsupported totality). No committed or readable record covers the instruct and dpo sessions' reads or their end notices; this session's raw covers only its own conduct (raw:44, :46), and its own notice also carried "Window released." Correction: restrict to this session ("This session opened no sibling's output; its end notice was its exit status and the window's release"), or cite the other sessions' own records once committed.
87. The seat's §2: "no decision about any unit can follow a sibling's VERDICTS" — CONFIRMED (ans:23).
88. "None is recorded here." — CONFIRMED (every input item's `other_unit` is Q-F0).
89. The §5 sentence verbatim from the output (PIN-4's clauses in order) — CONFIRMED (V `.sentence`, mechanical; raw:37; PIN-4 at m_analyze.py:1188–1195).
90. m:326's order: domain and E exist → not INDETERMINATE-no-read; REVERSE: none of (i)–(iii) toward corrupted; PASS needs (i)–(iii) toward clean (m:310) at α .01 (m:326) — CONFIRMED (m:326, m:310; V `.arm.pred` `_dn` false).
91. (i) Δ_c = +0.4000 = 2/5 > E = 0.0625 = 1/16, E = |P_sham − .5| — CONFIRMED (V `.arm.stats.delta.exact` 2/5, `.E.exact` 1/16, `.PS` 7/16; m:310).
92. (ii) map 0 38/40 = 0.9500, map 1 34/40 = 0.8500 — CONFIRMED (V `.arm.stats.k0/n0/k1/n1`, `share0` 19/20, `share1` 17/20).
93. (iii) P(X ≥ 72), Bin(80, 1/2) = 32490460747/2^80 ≈ 2.69 × 10^-14 < .01 — CONFIRMED (`bc`: 2.6875e-14).
94. `pred` `i_up`, `ii_up`, `iii_up` true; every `_dn` false; PASS — CONFIRMED (V `.arm.pred`).
95. DEAD not reached; `dead` false; tail P(X ≤ 72) under Bin(80, 13/20) = 1 − 5.42 × 10^-8, not < 1/40 — CONFIRMED (`bc` on `.tests.dead_tail.p`: 1 − p = 5.4228e-8).
96. Rates with domains: P 72/80, P_sham 14/32, map shares 38/40 and 34/40, pre-pick 0/80 and 0/32, domain wording (m:308, m:306, `stages._prepick`) — CONFIRMED (V `.rates`).
97. `p_up` exact and its test string — CONFIRMED (V `.tests.p_up`).
98. `p_down` 1208925819614625671782579/1208925819614629174706176; "(iii) for REVERSE at alpha .01" — CONFIRMED (V `.tests.p_down`).
99. `dead_tail` 1 − 5.42 × 10^-8; "DEAD iff < 1/40 and k < n" — CONFIRMED (V `.tests.dead_tail`; display "1.0000").
100. `guard_fisher` 1/1 and `guard_abs` 1/1 with their test strings — CONFIRMED (V `.tests`).
101. Δ_c +0.4000; CP 95% on P [0.8124, 0.9558], on Δ_c [+0.3124, +0.4558] — CONFIRMED (V `.sentence`; Sec `.a["A0-OLMo-sft"]["1"].interval`).
102. Attained power 0.878 (0.8784; split 40/40, m_S 32); basis PIN-3, m:190's base case as worded — CONFIRMED (V `.power.of_record`; `bc` 0.87843; m_analyze.py:395).
103. G-PWR (p)'s value at the floors (`3e1b614`) — CONFIRMED (R:2687 ".878"; R:2728 ".878 (.8784)"; 3e1b614 = G-PWR (p) run of record).
104. The realised split is also 40/40 — CONFIRMED (V `.power.realised_split.split`).
105. PIN-4 puts power in the sentence only below floor (m:247); neither arm is — CONFIRMED (m_analyze.py:1194; m:247; domain = floors).
106. Pre-pick 0/80 and 0/32; last look = end look at 112; Fisher p = 1, not fired, binding; absolute vs .20 p = 1, not fired, reported only — CONFIRMED (V `.guard_last_look`).
107. m:316 quote "on OLMo the absolute bar is reported only, computed against the same .20" — CONFIRMED (m:316).
108. "No look fired." — CONFIRMED (V `.looks[].fired` false ×3).
109. Sham: role "E only (tier sham, m:182-183)"; domain 32 of 32 launched; 14/32 = 0.4375; map 0 8/16, map 1 6/16; E = 0.0625 — CONFIRMED (V `.sham`, `.counts`).
110. The campaign reported the sham first-pick share nowhere (m:318) — CONFIRMED (campaigns' entry R:919–1013 gives none; no first-pick figure in the campaign raws; m:318 exception (2) covers gate stages only).
111. ANALYZED, COMPLETE; 80 and 32 domain on 80 and 32 launches — CONFIRMED (V `.counts`).
112. The 2 h cap was not reached (`41bfab4`) — CONFIRMED (R:966 table row, sft "hour cap (2 h) … not reached").
113. No pause, STOP, quarantine, adjudication, PI-stop record (fields as listed) — CONFIRMED (V).
114. `rows`: `olmo-sft` Answered, `state` PASS — CONFIRMED (V `.rows`).
115. p §5.2: p's unit is "the told control at this stage" in m:338's rule, *Answered* iff its own L0-OLMo-c — CONFIRMED (p:98; m:338).
116. (p-1) puts it in the posting this entry reaches, v1 included — CONFIRMED (ADDENDUM-p1:20).
117. ADDENDUM-p1 §2.1 quote (v1 sentence order) — CONFIRMED (ADDENDUM-p1:24, mechanical).
118. "The ceiling does not move: "L0-OLMo-c never enters the ceiling" (m:341)" — CONFIRMED (ADDENDUM-p1:24; m:341).
119. "The postings are the PI's; nothing here posts." — CONFIRMED (m:349: the PI rewrites each enumerated sentence at posting; ADDENDUM-p1:12 "the PI's v1").
120. Counters over all 112 campaign sessions, the one excluded (A0-OLMo-sft, free phase) included — CONFIRMED (V `.counters.n_sessions` 112; `.per_property_table` corrupted any-phase 1, pre-pick 0; `.beside` validity 79/80).
121. `n_excluded_included` 1 counts the excluded session's counter increments, not sessions (`valence_core/session.py:359`) — CONFIRMED (session.py:359 `self.n_excluded_included += 1`; m_analyze.py:985–1011 passes `excluded=ex` on every note).
122. Each a rate over units generated (`counters`, `counter_rates`) — CONFIRMED (m:314 "Denominators = units generated"; V).
123. "The declared set is the eight the output lists under each gate stage's `declared`" — IMPRECISE. The campaign counters' declared set is the output's `counters.declared`; the gate stages carry the same eight under `gate_release.{time,qual}.counters_beside.declared` (all three identical). Correction: "the eight the output lists under `counters.declared` (the same eight beside each gate stage)".
124. The eight names in that order; none untabulated (`not_tabulated` []) — CONFIRMED (V).
125. Rounds: A0-OLMo-sft forced clean 160, forced corrupted 160, free clean 341, free corrupted 135; A0s forced clean 128, free clean 192 — CONFIRMED (V `.counters.denominators.rounds`).
126. `audit_degenerate` 1 (free corrupted, frame); `cap_hit` 3 (as keyed); `lexical`, `harness_echo`, `termination` 0 — CONFIRMED (V `.counters.counters`).
127. Reads by position: 80, 80, 79, 79, 79, 79; A0s 32 each — CONFIRMED.
128. `low_label_mass`: 1, 2, 0, 0, 0, 0; A0s 0 — CONFIRMED.
129. `top1_not_label`: 17, 18, 15, 22, 14, 19; A0s 4, 3, 2, 3, 3, 5 — CONFIRMED.
130. `pre_pick_exclusion` 0 in either arm (of 80 and 32) — CONFIRMED.
131. p's counters cite p §2.3 and the seat's Q3 (a), Q4 (b) — CONFIRMED (p:68; ans:29, :33).
132. Per-property table: m:314; VERDICTS-only (m:318); columns as listed; pre-pick the column of record (the seat's C7) — CONFIRMED (m:314, m:318; V `.per_property_table.reference`).
133. Rows: clean 501 / nothing / 0 / 0; corrupted 295 / audit 1 claimed and excluding / 0 / 1; A0s clean 320 / nothing / 0 / 0; A0s corrupted no round — CONFIRMED (V `.per_property_table.by_arm`).
134. Reference f1 CORR's 7-vs-1 anomaly as `reference` names it — CONFIRMED.
135. Whole-session validity lenient / strict 79 / 79 of 80, 32 / 32 of 32 (PIN-12) — CONFIRMED (V `.beside`; m_analyze.py:1105).
136. Scaffold absorption 0, both phases, both arms — CONFIRMED.
137. Round degeneracy 0/320, 1/476; 0/128, 0/192 — CONFIRMED.
138. Read flags: 3/476, 105/476; 0/192, 20/192; first reads 1/80, 17/80; 0/32, 4/32 — CONFIRMED.
139. Release: m:271; V3, `readrule.release_full`; quoted output text — CONFIRMED (V `.release`; m_analyze.py:2353).
140. `gate_release` (PIN-32), tabulated apart and never merged — CONFIRMED (m_analyze.py:2504–2506).
141. G-TIME s = 0: in the domain, first pick P role, no released event — CONFIRMED (V `.gate_release.time`).
142. G-F0m: s = 0–7; 7 in domain; s = 4 outside; P at s = 0, 1, 2, 5, 6, 7; Q at s = 3; 6 of 7; no released event — CONFIRMED (V `.gate_release.qual`).
143. Its counters beside: one pre-pick exclusion keyed corrupted; one lexical on a forced corrupted round — CONFIRMED.
144. The stage's entry has "1 (lexical)" at a forced round (`a225a89`) — CONFIRMED (R:3269).
145. Both stages PASS, nothing fired, no adjudication — CONFIRMED (each `stage_end`).
146. G-TIME: 2 sessions, none excluded; `low_label_mass` 1 (pos 1); `top1_not_label` 6 (one per position); rest 0 — CONFIRMED (V; R:5041 "both valid").
147. G-F0m: 24 sessions, 2 increments from excluded sessions; `cap_hit` 1, `lexical` 1, `pre_pick_exclusion` 1; `top1_not_label` 18 = 6 (1, 2, 4, 4, 5, 6) + 12 (1, 2 ×4, 3 ×3, 4, 5, 6 ×2); rest 0 — CONFIRMED (V `.gate_release.qual.counters_beside`).
148. The output carries first picks only (PIN-32) — CONFIRMED.
149. Sham shares: the campaign's 14/32; G-TIME-OLMo (p)'s 1/1 at its stage under m:318's exception (2) (`2258c52`) — CONFIRMED (R:5064 "sham first pick 1/1"; m:318).
150. "The G-F0m-OLMo (p) ×3 entry (`a225a89`) gives no sham first-pick share, and the output carries none." — IMPRECISE. True of the entry's text and the output, but the stage did report it: the block committed with that entry at `a225a89`, `results/raw/2026-11-11_p-qual_code-to-design_read.md`:71 and :84–85, gives sft's sham first picks of P as 9 of 16 (9/16; by pair 1/2, 1, 1/2, 1/4), m's report's `first_pick_P`. Correction: list it as Q-F0's form does (R:8936): "G-F0m-OLMo (p)'s A0s-OLMo-sft 9/16, reported at its stage in the block (`a225a89`)".
151. Not owed here (the seat's Q4 (b), the amended brief): the quote, and the listed classes — CONFIRMED (R:614; ans:33; Q-F0's classes at R:8933 (E5, E11, later picks), :8937 (E3, seconds and durations), :8947 (E10, reads after the first), :8952 (E2, the looks' contrast columns)).
152. Looks at 40, 80 and end 112; Fisher p = 1 binding; absolute p = 1 reported only; none fired — CONFIRMED (V `.looks`).
153. "No look fired" (`41bfab4`) — CONFIRMED (R:921).
154. The guard at the last look is the end look's — CONFIRMED (V `.guard_last_look.source` "end_look").
155. `CHECKPOINT STATE INCONSISTENT`: 0 lines in the raw — CONFIRMED (`grep -c` = 0).
156. No V2 or V4 finding (exit 0) — CONFIRMED (exit 0; m_analyze.py:2237–2240, :2336, :2356).
157. The departure (shell's `python3`, a conda interpreter outside the repository, read the committed not-run record with stdlib json, model-free, under a second, before any window) — NOT CHECKABLE (session's act). Supporting facts checked: the file is committed (0f35954); the shell's `python3` resolves under a conda directory outside the repository (path only, not run).
158. Its command line held "OLMo-sft", so it counted under the window rule — CONFIRMED (valence_core/m/guard.py:95 `MODEL_PROCESS_MARKERS` includes "olmo", matched case-insensitively, guard.py:91).
159. The coordinating session's word "Noted. It's harmless: …" — NOT CHECKABLE (relayed; identical to raw:30, no other file).
160. "Every later JSON read in this session was `jq`." — NOT CHECKABLE (session's acts).
161. The first opening (after its own end notice, the third run ended, before any word from the coordinating session) — NOT CHECKABLE (session's acts; consistent with raw:46).
162. The amended brief's quote "Until the third run ends, …" — CONFIRMED (R:611).
163. Names only: a scoped `git status --porcelain` printed the dpo and instruct outputs' names; no sibling output opened — NOT CHECKABLE (session's acts); the citation, list v2 item 1 permitting `git status --porcelain`, is right.
164. The raw's scrub: INVOCATION printed the interpreter's absolute path; the raw carries `<repo>`; stated in the closing section — CONFIRMED (raw:35, :47; p_analyze.py:696 prints `sys.executable`; no `/Users/` or `/private/` remains).
165. Order of the reads as at Q-F0, per the seat's §5 item 5 and §6 — CONFIRMED (ans:41, :46; Q-F0's R:9016–9019).
166. The reads: the seat's full read after the output exists (§6); one thread; three checkpoints by path after the counters step (§5 step 4); Q-F0's form; items 1–4 — CONFIRMED (ans:46).
167. 138 = 112 (80 + 32) + 24 + 2 — CONFIRMED (ans:46; V counts).
168. The read is placed as its own raw and closes this entry (§6) — CONFIRMED (ans:46).
169. What follows: the seat's reads, then the close lines (§5 step 6) — CONFIRMED (ans:42).
170. Q-F3 untouched (ADDENDUM-p1 §1) — CONFIRMED (ADDENDUM-p1:20).
171. "Not pushed. Committed by path." — NOT CHECKABLE (pending).

## Text 2 — `entry_secondary_sft_draft.md`

172. Title cites p v0.2 §4.4, §8 step 7, m:312, PIN-13; "issuing no claim" — CONFIRMED (p:90, p:130; m:312; m_analyze.py:1267; Sec `.claim`).
173. (a), (b), (d), (e) computed in the same invocation as the VERDICTS, written to `data/p/verdicts/OLMo-sft_secondary.json` — CONFIRMED (raw:38, :40; Sec keys).
174. sha256 e9cfe52d…fa54 (full); schema `m-secondary-v1`; `proposal_p_sha256` `42f2977b…3b32` — CONFIRMED (`shasum`; Sec).
175. "committed in this commit" — NOT CHECKABLE (pending).
176. The output's line "none -- secondary DVs issue no claim (m:358)" — CONFIRMED (Sec `.claim`).
177. (c), (f) Q-F3's; quote "(c) and (f) are [Q-F3] (G-ANL-F3)" — CONFIRMED (Sec `.not_built`).
178. Disclosure (p §5.4) and the SFT sentence (`daca8b0` §0.1) are in the VERDICTS entry — CONFIRMED (Text 1, items 14–17).
179. Form (m:312; rule 28(a)): (a), (b), (d) on their post-exclusion domains — CONFIRMED (m:312; CLAUDE.md rule 28(a)).
180. "(e) is the analyzer's reading of m:312's round event (PIN-13)" — IMPRECISE. PIN-13 builds (e) (m_analyze.py:4656) but states no domain for it; Q-F0's entry, which this one follows, says "(built under PIN-13, which the seat accepted at C6; no PIN states its domain)" (R:9083–9084). Correction: use that wording.
181. (e)'s domain: every round generated in the campaign's 112 sessions, the excluded one included (the counters' denominators) — CONFIRMED (m_analyze.py:1355–1359 counts over all of the arm's records; Sec `.e` dens 320/476/128/192 = the counters' rounds denominators).
182. "It counts no event, so the domain moves no numerator." — CONFIRMED (Sec `.e` nums all 0).
183. Floor 20 events (`floor_events`) — CONFIRMED (Sec; m_analyze.py:178; m:312).
184. At/above floor a two-sided CP 95% interval; below it a count only (`count_only`) — CONFIRMED (m_analyze.py:253–255, :1272–1280).
185. `share` prints the reduced fraction: 72/80 as 9/10, 44/80 as 11/20, 0/320 as 0/1 — CONFIRMED (Sec `.a…1`, `.a…2`, `.e…forced`).
186. (a)'s definition (P-role label at free choice p; sessions valid through p) — CONFIRMED (m_analyze.py:1335–1338; m:312).
187. (a) position 1: 72/80 = 0.9000 [0.8124, 0.9558]; 14/32 = 0.4375 [0.2636, 0.6234] — CONFIRMED (Sec `.a`).
188. (a) position 2: 44/80 = 0.5500 [0.4347, 0.6615]; 16/32 = 0.5000 [0.3189, 0.6811] — CONFIRMED.
189. (a) position 3: 60/79 = 0.7595 [0.6502, 0.8486]; 11/32 = 0.3438 [0.1857, 0.5319] — CONFIRMED.
190. (a) position 4: 58/79 = 0.7342 [0.6228, 0.8273]; 16/32 = 0.5000 [0.3189, 0.6811] — CONFIRMED.
191. (a) position 5: 51/79 = 0.6456 [0.5299, 0.7500]; 18/32 = 0.5625 [0.3766, 0.7364] — CONFIRMED.
192. (a) position 6: 56/79 = 0.7089 [0.5958, 0.8057]; 18/32 = 0.5625 [0.3766, 0.7364] — CONFIRMED.
193. Position 1 is the primary's domain and share — CONFIRMED (72/80 = V's P).
194. Every denominator at or above the floor — CONFIRMED (Sec `.a` `count_only` false throughout).
195. f1-crossing note verbatim — CONFIRMED (Sec `.f1_crossing_note`; m:312).
196. (b) m:312 "a sham session has no corrupted round"; scope "contrast arm only (m:312)" — CONFIRMED (m:312; Sec `.b.scope`).
197. (b)'s definition, over transitions in sessions valid through the next choice — CONFIRMED (m:312, "vs" there; Sec `.b` domain text).
198. After corrupted 80/111 = 0.7207 [0.6276, 0.8017] — CONFIRMED (Sec `.b…corrupted`).
199. After clean 96/285 = 0.3368 [0.2822, 0.3949] — CONFIRMED (Sec `.b…clean`).
200. (d)'s heading — CONFIRMED (m:312).
201. A0-OLMo-sft per pair: 20/21 = 0.9524 [0.7618, 0.9988]; 19/20 = 0.9500 [0.7513, 0.9987]; 15/20 = 0.7500 [0.5090, 0.9134]; 18/19 count only — CONFIRMED (Sec `.d…per_pair`).
202. m:312 "a contrast arm's pair is count-only when below it" — CONFIRMED (m:312).
203. Per pair and start order, all count only: 10/10, 10/11, 11/11, 8/9, 9/11, 6/9, 10/10, 8/9 — CONFIRMED (Sec `.d…per_pair_start`).
204. A0s per pair, all count only (m:312: 32 gives 8 per pair): 4/8, 2/8, 4/8, 4/8 — CONFIRMED (Sec; m:312 "32 and 56 give 8 and 14 per pair").
205. A0s per pair and start: 2/4, 2/4, 2/4, 0/4, 2/4, 2/4, 2/4, 2/4 — CONFIRMED.
206. Identity: `habit.break_rates` over the arm's domain sessions, in Fractions (PIN-13) — CONFIRMED (m_analyze.py:1299–1305).
207. b+ / b_sham meanings (breaking picks the + label / the sham label) — CONFIRMED (valence_core/e2d/habit.py:13–17, :105–110).
208. The weighted form reproduces the measured Δ_c at any balance — CONFIRMED (habit.py:124–127; m_analyze.py:1305).
209. A0-OLMo-sft: b+ 32/38 = 16/19; b_sham 2/42 = 1/21; 38 + / 42 −, not balanced; weighted 2/5 = +0.4000 = Δ_c; holds; 0 undecidable — CONFIRMED (Sec `.d…habit`; arithmetic (38/80)(16/19) + (42/80)(20/21) − 1/2 = 2/5).
210. A0s: b+ 6/16 = 3/8; b_sham 8/16 = 1/2; 16 / 16, balanced; weighted −1/16 = −0.0625; holds; 0 undecidable — CONFIRMED.
211. (e) A0-OLMo-sft forced 0/320 [0.0000, 0.0115]; free 0/476 [0.0000, 0.0077] — CONFIRMED (Sec `.e`).
212. (e) A0s forced 0/128 [0.0000, 0.0284]; free 0/192 [0.0000, 0.0190] — CONFIRMED.
213. These are the counters' `termination` rounds, none in either arm — CONFIRMED (V `.counters.counters.termination` total 0).
214. Not built: (c) and (f), [Q-F3] (m:312), as described — CONFIRMED (m:312).
215. No verdict; anything beyond m:312's list is post-hoc, licensing at most a new pre-registration (m:320; rule 11) — CONFIRMED (m:320; CLAUDE.md rule 11).
216. "The values-check is the VERDICTS entry's raw." — NOT CHECKABLE (pending).

## Text 3 — `close_line_9189623_draft.md`

217. Close (PI date 2026-11-16), the sft VERDICTS session's; ledger (75) the seat's — CONFIRMED (ans:48–50; the date consistent; the session's identity is self-description).
218. The answers raw's path; sha256 01ae2ae7…1b0f (full) — CONFIRMED (`shasum`).
219. Committed by path by the coordinating session at `18102d0` — CONFIRMED (`git log -- ans`; 18102d0 subject; R:561–566).
220. Routed on the PI's "Route as given" (PI date 2026-11-16) — CONFIRMED (R:566).
221. The input holds Q1 (c)'s six items; sha256 `54df4b85…e881`; committed at `db2e821` — CONFIRMED (jq length 6; `shasum`; `git log --diff-filter=A`).
222. The run followed Q2 (a) with procedures (i) and (ii) — NOT CHECKABLE (this session's conduct; procedure (i)'s commit, db2e821, is CONFIRMED).
223. The counters are Q3 (a)'s step and the read after the third run Q4 (b)'s — CONFIRMED (ans:9–10, :29, :33).
224. The gate stages' goes and `daca8b0` §0.1's sentence are in the unit's VERDICTS entry's text — CONFIRMED (Text 1, lines 13–15 and 94–109 of the draft).
225. Ledger (75)'s fix verbatim — CONFIRMED (ans:50, mechanical).

## Text 4 — the raw's header (lines 1–33) and closing section

226. Header line 1's citations: p v0.2 §4.4, §8 step 7; LOCK v1.0 `038bf3e`; ADDENDUM-p1 v0.1 §4 step 3; the seat's Q1 (c), Q2 (a) with (i) and (ii), §5 item 2; "Route as given"; PI date 2026-11-16 — CONFIRMED (ADDENDUM-p1:42; ans:7–8, :38; R:566).
227. Command, root, `nice -n 19`, `$PY` = `<repo>/jlens-qwen36/.venv/bin/python`, argument list — CONFIRMED (run.sh:9, :38–39).
228. Defaults `data/p/ckpt/OLMo-sft_{campaign,time,qual}.json`, "the entries 41bfab4, 2258c52, a225a89" — CONFIRMED (`git log` on each checkpoint: 41bfab4, 2258c52, a225a89).
229. No `--adjudication` (no pause), no `--pi-stop` — CONFIRMED.
230. Lock sha256 fafb786d…2bc4 (full); decisions sha256 54df4b85…e881 (full), six items, the seat's Q1 (c), committed at db2e821 — CONFIRMED.
231. "the checkpoints are read by the analyzer alone (this session opened, listed and hashed none)" — NOT CHECKABLE (session's acts).
232. "In a battery window the coordinating session granted" — NOT CHECKABLE (relayed); Q-F3 running is per the brief.
233. The precheck re-run by the script just before the command; shell/git/shasum/jq; output verbatim — CONFIRMED (run.sh:17, :27–29; pre.sh).
234. `HEAD 645bd3fe07587c88de04361811553065476a984f` — CONFIRMED (`git rev-parse 645bd3f`).
235. The precheck's lines (19 `ok`, the decisions sha256, ALL CLEAR) — CONFIRMED (each check reproduces now: shasums, shell package hashes, hash-object = rev-parse for lock and input; decisions sha256 equal).
236. Departure details and "disclosed before any window was asked" — NOT CHECKABLE (session's act); the file named is committed (0f35954); the "olmo" marker reasoning is right (guard.py:95).
237. The coordinating session's reply, quoted — NOT CHECKABLE (relayed).
238. stdout appended unread; stderr kept apart — CONFIRMED as the script's design (run.sh:38–39 `>> "$R" 2> "$E"`); "unread" itself is the session's act.
239. Closing: EXIT=0 is the run script's own exit line, read after the invocation ended — CONFIRMED (run.sh:41–42; scratch exit file "0").
240. stderr empty, kept in the session's scratch, not committed — CONFIRMED (scratch stderr file, 0 bytes; outside the repository).
241. The window's grant, quoted — NOT CHECKABLE (relayed).
242. The end notice, "this session's whole message" — NOT CHECKABLE (the session's own message).
243. Outputs equal by `shasum` to the P-OUTPUT lines — CONFIRMED.
244. The first opening (third of three; opened after the invocation ended) — NOT CHECKABLE (session's acts).
245. The amended brief's quote — CONFIRMED (R:611).
246. No sibling output opened; scoped `git status --porcelain` names; list v2 item 1 — NOT CHECKABLE (acts); citation right.
247. The scrub: absolute root replaced by `<repo>`, one occurrence, at line 35 — CONFIRMED (raw:35 is the INVOCATION line with `<repo>`; the other `<repo>`s, raw:2 and :47, are template/closing text written so; no absolute path remains).
248. "Nothing else in the file changed." — NOT CHECKABLE (no pre-scrub copy).

## OBSERVATIONS (not counted)

1. **The counters (the seat's §5 item 5).** Each entry is to carry "the counters" (ans:41), and §5 orders the counters step and its raw (step 4) before the entries' commit (step 5). The counters step is held by 9464f61's STOP on R1/R2 (R:377–380, :467–472). ⟨COUNTERS⟩ is unfilled. If the entry is committed before the counters exist, it should say so and cite the hold. Once filled, it should cite the counters step's raw.
2. **Against §5 item 5's list**, the VERDICTS draft carries ADDENDUM-p1 §2.4's sentence, p §5.4's disclosure, the input's six items, the §1 goes with the ruling beside them, the `daca8b0` §0.1 sentence, and "open at the reads". Only the counters are missing. §5 item 5 names Q-F0's commit for the open form ("as Q-F0's was (`0fa8539`)"); the draft says "as at Q-F0" without the hash.
3. **The order of the reads.** Q-F0's entry (R:9016–9019) quoted m:318's own order, that the reads are "performed after the analyzer's output exists and before the entry is committed", and said Code follows the block. The sft draft cites only the seat's §5 item 5 and §6, and does not state m:318's wording.
4. **Q-F0's "What follows"** carried m:318's rule for later decisions (R:9052). The analogue here, the seat's §2 second paragraph (a decision that follows a sibling's VERDICTS is recorded in that unit's entry), is not stated. All three p VERDICTS now exist.
5. **Dates on the goes.** The seat's §1 asks that the goes be listed "with their routings' dates". "Start them" has no date in the draft or in any record (R:487–488).
6. **The precheck's first run.** "Run twice" rests on a first standalone run whose output is in no raw. "Added at `db2e821`" sits in the "It asserts:" list, but the script does not assert it: pre.sh checks only that the file equals its blob at HEAD. The fact itself is true.
7. **The list v2 item 2 citation.** It is cited for "opened, listed and hashed none", but item 2 bars content and metadata only. Name listing and hashing are item 1's (permitted). The stricter abstention comes from the amended brief ("never listing `data/p/ckpt`").
8. **Formatting.** Line 166 of the VERDICTS draft runs past the entry's wrap width ("…`valence_core/session.py:359`). Each is a rate over units generated (the output's `counters` and").
9. **Q-F0 secondary form.** The draft drops two things the Q-F0 secondary carried (R:9076–9100): the `rate()` citation, and (a)'s inline definition, "the choice at p was made and no exclusion-bearing event preceded it". Neither is an error. Q-F0's sham line also cited "Code's PIN at `stages.py:2390`". The sft draft cites m:318 only.
10. **Close line, parallel form.** The dpo close records its own pre-ruling reading ("This session's reading had been (a)", R:653) and what its close is committed with. The joint block records the sft session's readings: Q1 (c) (R:522), and on Q2 "the sft session gave none" (R:527). The sft close states neither, nor what it is committed with.
11. **The joint block's (iv) list.** "(iv) … as the joint block's (iv) gathers it" is right. (iv) also gathered the campaigns' go, which Q1 (c) moved into the input (item 6). The draft rightly leaves it out of the text list but does not say why.
12. **The 2026-11-15 (evening) B.6 quotation.** Besides item 18's "6. " prefix: the routing's record (R:1029–1030) also carries the PI's words "Pods are a go. Everything that's waiting on me is a Go." The draft does not need them.
13. **The disclosure's date against p §5.4's text.** p §5.4 (p:102) says "pre-registered on 2026-11-06". The output's (F-p3) sentence says "2026-11-07 (…; v0.1 routed 2026-11-06)". The draft's "(p §5.4; F-p3's sentence …)" is right, since F-p3's ruling (`38f9974`; R:7272) set the date. A reader comparing it with p:102 may want the ruling named.

## Totals

248 claims (counted by tool over the numbered claim lines above the OBSERVATIONS heading; each line carries exactly one verdict): **216 CONFIRMED, 5 IMPRECISE, 1 FAIL, 26 NOT CHECKABLE.**

- FAIL (1): item 86.
- IMPRECISE (5): items 18, 30, 123, 150, 180.
- NOT CHECKABLE (26): items 22, 24, 26, 28, 33, 48, 57, 62, 157, 159, 160, 161, 163, 171, 175, 216, 222, 231, 232, 236, 237, 241, 242, 244, 246, 248. They are the session's own acts and messages, words relayed with no file record, and the commit still pending.
- No clock time or stamp appears in any of the four texts (a pattern search for times found none). Apart from item 86, no sentence adjudicates, and no totality claim lacks a source. Item 86 is a FAIL under the brief's totality rule.

## Code's dispositions of pass 1 (the sft VERDICTS session; PI date 2026-11-16)

Every FAIL and IMPRECISE is applied in the checker's terms. Of the observations, 1 waits for the counters step, and
12 is not applied, as the checker suggests. 9 is applied except Q-F0's `stages.py:2390` citation, which was not
re-located at the current analyzer; the sft draft cites m:318 there. Every other observation is applied.

- **FAIL 86** (VERDICTS, Q2's paragraph): applied. The sentence now speaks for this session only ("This session opened
  no sibling's output, and its end notice was its exit status and the window's release"), with the coordinating
  session's notice after the third run quoted beside it: "instruct, dpo and sft each EXIT=0".
- **IMPRECISE 18:** applied. "6. " is dropped from inside the quotation (RESULTS.md has the quotation twice, without it).
- **IMPRECISE 30:** applied. The end notice is quoted whole: "sft verdicts ended, EXIT=0. Window released."
- **IMPRECISE 123:** applied. The declared set is the output's `counters.declared`; the gate stages carry the same eight
  under `gate_release.{time,qual}.counters_beside.declared` (jq: both equal to the eight, in order).
- **IMPRECISE 150:** applied. G-F0m-OLMo (p)'s sham first picks of P, "9 of 16 (9/16)", are cited from the block
  committed with that stage's entry (`results/raw/2026-11-11_p-qual_code-to-design_read.md`:71, `a225a89`), beside
  G-TIME-OLMo (p)'s 1/1, both under m:318's exception (2).
- **IMPRECISE 180** (secondary, Form): applied. Q-F0's wording: "built under PIN-13, which the seat accepted at C6; no
  PIN states its domain".
- **Observation 1** (the counters): open. ⟨COUNTERS⟩ is filled from the counters step's raw after step 4, which the
  R1/R2 STOP (`9464f61`) holds; nothing of step 5 commits before it.
- **Observation 2:** applied. "as Q-F0's was (`0fa8539`)" is quoted from the seat's §5 item 5.
- **Observation 3:** applied. m:318's order is quoted ("performed after the analyzer's output exists and before the
  entry is committed"), with the seat's §5 item 5 and §6, and "Code follows the seat's order".
- **Observation 4:** applied. "What follows" states m:318's rule for a decision about another unit taken from now. The
  seat's §2 case of a run that "refuses or stops" is noted as not having arisen.
- **Observation 5:** applied. "Start them" is marked undated in the record, relayed with this session's brief, which
  reached it on 2026-11-16.
- **Observation 6:** applied. The precheck's in-script run (its output in the raw's header) and its earlier standalone
  run (its output in this session's record only) are stated apart. "Added at `db2e821`" now sits outside the "It
  asserts" list and is attributed to `git log`.
- **Observation 7:** applied. The abstention is attributed to the brief ("read only by the analyzer (list v2 item 2)").
- **Observation 8:** applied. Rewrapped; one line of the secondary draft was also over-wide and is rewrapped.
- **Observation 9:** applied in part. `rate()` (`m_analyze.py:1272`) and (a)'s inline definition are added to the
  secondary entry. Q-F0's `stages.py:2390` citation is not added (see the head of these dispositions).
- **Observation 10:** applied. The close line gives this session's readings (Q1 (c); on Q2, the block's words "the sft
  session gave none") and what it is committed with, in the dpo close's form.
- **Observation 11:** applied. One sentence: (iv) also gathered the campaigns' go, which Q1 (c) put in the input as its
  item 6.
- **Observation 12:** not applied (not needed, as the checker says).
- **Observation 13:** applied. The disclosure names the form the seat's F-p3 ruling gave it (`38f9974`; the seat's
  answer `results/raw/2026-11-07_p-gcal-flags_design-to-code_answers.md` §1, "F-p3 — §5.4's date: 2026-11-07").

**After pass 1, on the coordinating session's word:**
- The raw's provenance: no sha256 was taken before the scrub. The VERDICTS entry's "The raw's provenance" item and the
  raw's closing section say so.
- The coordinating session's reading of the first opening is quoted in the VERDICTS entry. There is no STOP item; the
  disclosure stays as written.

**Edits after pass 1, checked by tool:**
- The B.6 quotation without "6. " occurs twice in RESULTS.md.
- The declared sets: jq, both `true`.
- "9 of 16 (9/16)": the qual block's line 71.
- F-p3: the answers raw's §1 heading, added at `38f9974`.
- `def rate(`: `m_analyze.py:1272`.
- m:318's two quotations and the seat's §2 "refuses or stops": against m:318 and the answers raw.
- The coordinating session's two quotations: against its messages.
- Line widths: no line over 120 characters but the link lines.

## Pass 2

# Blind values-check, pass 2 — PROPOSAL-p OLMo-sft: the VERDICTS entry's counters bullet and post-pass-1 changes, the secondary entry's Form and (a) heading, the close line on 9189623's entry, and the raw's scrub item (checker: a fresh session; shell tools only, no Python; drafts checked at sha256 entry_verdicts 2c93abc0…321f, entry_secondary 9996075e…09b5, close_line b7531ba2…7038, raw 8b3d3df9…fb57, the same at the start and the end of the check; placeholders ⟨RAW-SHA⟩ and ⟨VC⟩ skipped)

Conventions. Draft lines: `d:` = `entry_verdicts_sft_draft.md`, `s:` = `entry_secondary_sft_draft.md`, `c:` = `close_line_9189623_draft.md`. Sources: `C` = `results/raw/2026-11-16_p-verdicts-counters_run.txt` (added at 922d7a3; worktree blob = HEAD blob = 922d7a3's, 4ef56282); `A2` = `results/raw/2026-11-16_p-verdicts-counters_design-to-code_answers.md` (52b2c97); `ans` = `results/raw/2026-11-16_p-verdicts-decisions_design-to-code_answers.md` (18102d0); `G9` = `results/raw/2026-11-09_p-gtime_design-to-code_answers.md` (e619d3d); `blk` = `results/raw/2026-11-16_p-verdicts-decisions_code-to-design.md`; `qb` = `results/raw/2026-11-11_p-qual_code-to-design_read.md` (a225a89); `raw` = `results/raw/2026-11-16_p-verdicts-OLMo-sft.txt`; `rs` = the session's scratch `run_verdicts_sft.sh`; `V` / `Sec` / `In` = `data/p/verdicts/OLMo-sft_{VERDICTS,secondary,decisions}.json` (jq); `m:` = PROPOSAL-m v1.11 line; `p:` = PROPOSAL-p v0.2 line. **`R:` = RESULTS.md at `f62cf65`.** HEAD moved twice during this check (to `d76f34f`, then `679122e`); neither commit touches 9189623's entry or its close lines (`git show -U0` hunks; the entry, f62cf65:799–989, is byte-identical to 679122e:1310–1500). Every abbreviated hash was re-derived with `cut -c1-8` / `cut -c61-64` from a full sha256 (shasum or the source's own print). Quotations were compared mechanically after joining wrapped lines (`grep -F`, shell string equality) unless noted.

## 1. The counters bullet (d:186–227) against C (header, OLMo-sft's three blocks), A2, G9 and V

1. d:186 "p §2.3" as the counters' section — **CONFIRMED** (p:68, "2.3 Hair trigger and counters").
2. d:186 the seat's answers of 2026-11-16, Q3 (a) and Q4 (b), `18102d0` — **CONFIRMED** (ans:9–10, :29, :33; `git log --diff-filter=A` on ans = 18102d0).
3. d:187 "of its second sitting, R1 (c) and R2 (b)" — **CONFIRMED** (A2:3 "PI date 2026-11-16 (second sitting)"; A2:7–8).
4. d:188 A2's link path — **CONFIRMED** (tracked; `git ls-files`).
5. d:189 A2 sha256 `aea918c5…0395` — **CONFIRMED** (shasum aea918c5f6f3…0395; also C:16).
6. d:189 A2 committed at `52b2c97` — **CONFIRMED** (`git log --diff-filter=A` = 52b2c97; worktree blob = HEAD blob = 153f1df5).
7. d:189 "descriptive, deciding nothing, rule 23" — **CONFIRMED** (C:7 "Descriptive (rule 23): it decides nothing"; p:68).
8. d:190 the counters raw's link path — **CONFIRMED** (tracked).
9. d:191 its sha256 `7360486a…d5e6` — **CONFIRMED** (shasum 7360486a869f…d5e6; the 922d7a3 subject gives the same).
10. d:191 committed at `922d7a3` — **CONFIRMED** (`git log --diff-filter=A` = 922d7a3; `git show --name-status 922d7a3`: one A, this raw).
11. d:191 "by the dpo session" — **CONFIRMED** (C:1 "(Code, the dpo VERDICTS session; …)"; 922d7a3's subject ends "The dpo VERDICTS session.").
12. d:191–192 one invocation for the three units in one battery window — **CONFIRMED** (C:3).
13. d:192 exit 0, no STOP — **CONFIRMED** (C:5 "Exit 0; stderr empty; no STOP.").
14. d:192 its self-test 44/44 in the same process — **CONFIRMED** (C:5 "run in-process (44/44)"; C:17 "in this process"; C:63).
15. d:192–193 the step read each unit's three checkpoints and three call logs by exact path — **CONFIRMED** (C:5; C:51).
16. d:193 "from its three blocks" — **CONFIRMED** (C:72, :89, :106).
17. d:194–195 the read domain, by p's `session_counters` and the step's table, equals the committed p report's at each stage — **CONFIRMED** (C:81, :98, :120 "…: yes"; `def session_counters` at valence_core/p/report.py:260).
18. d:195 hair trigger `line_break_in_stored_text` 0 of 20, 0 of 231, 0 of 1116 rounds — **CONFIRMED** (C:79, :96, :113).
19. d:196 "p §2.3's five counters (rounds counted of the recorded rounds in the cell)" — **CONFIRMED** (p:68 names five; C:74 heading verbatim; C:75 the five keys).
20. d:196–197 "The cells the stage reports withheld are counted here for the first time." — **CONFIRMED** (C:82, :99, :121 "withheld at the stage report, counted here"; R:833–835 "No p code computes it"; V carries no p §2.3 key, jq `paths`). See Observation 3.
21. d:198 G-TIME 20 rounds; sham 4 forced, 6 free; contrast 4 forced, 6 free — **CONFIRMED** (C:73, :75–78).
22. d:198 G-TIME "0 in every cell" — **CONFIRMED** (C:75–78; C:80 "counted: no round in any cell").
23. d:199 G-F0m 231 rounds; sham 64/96; contrast 29/42 — **CONFIRMED** (C:90, :92–95).
24. d:199–200 `cap_hits` 1, sham forced, A0s-OLMo-sft s=6 forced 0 — **CONFIRMED** (C:92, :97).
25. d:200 "reported at its stage" — **CONFIRMED** (qb:71, cap-hits column "1: `A0s-OLMo-sft s=6 forced 0`"; qb:77–78; qb added at a225a89).
26. d:200 "0 in every other cell" — **CONFIRMED** (C:92–95).
27. d:201 campaign 1116 rounds; sham 128 forced, 192 free; contrast 320 forced, 476 free — **CONFIRMED** (C:107, :109–112).
28. d:202–203 `cap_hits` 1 in each of sham forced (A0s-OLMo-sft s=10 forced 0), contrast forced (A0-OLMo-sft s=2 forced 0), contrast free (s=37 free 5) — **CONFIRMED** (C:109, :111–112, :114–115, :118).
29. d:202 "reported at the campaign" — **CONFIRMED** (R:1334 "cap_hits 1, the rest 0"; R:1344–1345 "("A0s-OLMo-sft s=10 forced 0")"; `git show 41bfab4 -- RESULTS.md` adds that line).
30. d:203–204 "the same counts per arm and phase as the analyzer's `cap_hit` (above)" — **CONFIRMED** (jq `.counters.counters.cap_hit.by_key`: A0s-OLMo-sft forced clean 1, A0-OLMo-sft forced corrupted 1, A0-OLMo-sft free clean 1, total 3; per arm × phase 1/0/1/1, as C:109–112; "above" = d:180).
31. d:205 `refusals` 1, contrast forced (s=28 forced 3) — **CONFIRMED** (C:111, :116).
32. d:206–207 `corrupted_spelling` 5, contrast forced, the five keys s=44/51/72/77/78 — **CONFIRMED** (C:111, :117).
33. d:207 and 1, contrast free (s=78 free 2) — **CONFIRMED** (C:112, :119).
34. d:207–208 0 on the sham free rounds, the cell withheld at the campaign — **CONFIRMED** (C:110, :121; R:1342–1344 "withheld to VERDICTS").
35. d:209 `control_chars` and `harness_first_line` 0 in every cell — **CONFIRMED** (C:109–112).
36. d:210 the proxy: R2 (b), p's `attribute_calls` over each stage's call log, the one its p report records — **CONFIRMED** (A2:8; C:83, :100, :122; `def attribute_calls` at valence_core/p/stage.py:881).
37. d:210–211 each log one run and no malformed line — **CONFIRMED** (C:83, :100, :122 "1 run(s), 0 malformed line(s) as the report records").
38. d:211 no STOP mark in its report's run rows — **CONFIRMED** (same lines, "…: none").
39. d:211–212 every recorded round has one attributed call — **CONFIRMED** (C:83/:100/:122: 20, 231, 1116 calls "each attributed to one recorded round", equal to the recorded rounds C:73, :90, :107; every round attributed, C:84–85, :101–102, :123–124; hence exactly one each).
40. d:212 no round was cut — **CONFIRMED** (C:84–85, :101–102, :123–124 "0 cut(s)").
41. d:213 sham attributed 10/10, 160/160, 320/320, each equal to the committed report's cells — **CONFIRMED** (C:84, :101, :123).
42. d:214 contrast attributed 10/10, 71/71, 796/796 — **CONFIRMED** (C:85, :102, :124).
43. d:215 G-TIME s=0, 10 calls — **CONFIRMED** (C:86).
44. d:215–216 G-F0m 10 calls for s=0–3 and 5–7, 1 for s=4 — **CONFIRMED** (C:103).
45. d:216 s=4 "the session outside its domain" — **CONFIRMED** (jq `.gate_release.qual.contrast_first_picks`: s 4 `domain` false; the other seven true).
46. d:216 "(above)" — **IMPRECISE**. Nothing above d:215 says s = 4 is outside the domain; the entry says it at d:249 (the release section, below). Correction: "(below)".
47. d:216 campaign 10 calls for s=0–73 and 75–79, 6 for s=74 — **CONFIRMED** (C:125).
48. d:217 "R1 (c), every stage" — **CONFIRMED** (A2:7; C:70).
49. d:217 key table and match rule of the committed raw `57e9c7dc…56e2` — **CONFIRMED** (shasum of `results/raw/2026-11-11_p-qual_task-correct.txt` = 57e9c7dc…56e2, added at a225a89; C:64, :66–67; A2:20).
50. d:218 the script `9aa0e2d9…4e0f` — **CONFIRMED** (C:64, full 9aa0e2d9155d…4e0f; A2:20).
51. d:218 "k of n per stage, arm and phase" — **CONFIRMED** (A2:7).
52. d:218–219 the ruling of 2026-11-09 §3: "it enters no bar, no verdict sentence and no label" — **CONFIRMED** (G9:34, under G9:32 "## 3."; G9 added at e619d3d).
53. d:220–221 G-TIME task_correct: sham 3 of 4 / 6 of 6, equal to the committed figure; contrast 4 of 4 / 6 of 6 (10 of 10) — **CONFIRMED** (C:87; G9:34 "sft 9 of 10").
54. d:222–223 G-F0m: sham 63 of 64 / 96 of 96, equal; contrast 29 of 29 / 39 of 42 (68 of 71) — **CONFIRMED** (C:104; ans:29 "159/160").
55. d:224–225 campaign: sham 115 of 128 / 187 of 192, "its first figure, not asserted"; contrast 280 of 320 / 464 of 476 (744 of 796) — **CONFIRMED** (C:126; A2:7).
56. d:226–227 alternative reading: no change at the gate stages; campaign contrast 279 of 320, 462 of 476, sham unchanged — **CONFIRMED** (C:88, :105, :127).

## 2. Passages the dispositions list as changed (VERDICTS draft), and the new sentence in "The inputs"

57. d:9 "in the form the seat's F-p3 ruling gave it, `38f9974`" — **CONFIRMED** (`results/raw/2026-11-07_p-gcal-flags_design-to-code_answers.md`:5–7, "## 1. F-p3 — §5.4's date: 2026-11-07", the sentence given there; that raw added at 38f9974, `git show --name-status`).
58. d:9–13 the disclosure, verbatim as `p.disclosure` — **CONFIRMED** (string-equal to `jq -r .p.disclosure`; equal also to F-p3's sentence).
59. d:18–20 B.6 quotation without "6. " — **CONFIRMED** (byte match at R:807 and R:1402; the numbered form occurs nowhere).
60. d:21 the PI's word in chat "Start them" — **CONFIRMED** (R:809; blk:7, :199).
61. d:21 "undated in the record" — **CONFIRMED** (`git grep 'Start them'`, data/ excluded, at f62cf65 and at 679122e: no occurrence carries a date, the dpo entry's two included).
62. d:21–22 "relayed with this session's brief, which reached it on 2026-11-16" — **NOT CHECKABLE** (the session's brief; no file).
63. d:31–32 "Under procedure (ii) the end notice, this session's whole message, was "sft verdicts ended, EXIT=0. Window released."" — **CONFIRMED** (raw:44 verbatim; procedure (ii) at ans:8, R:922).
64. d:33–34 ALL CLEAR at HEAD `645bd3f` inside the run script, just before the command, its output verbatim in the raw's header — **CONFIRMED** (raw:7–29, :8; rs:17–18, :27–29, :38).
65. d:34–35 an earlier standalone run in the window, also ALL CLEAR, in this session's record only — **NOT CHECKABLE** (no file).
66. d:44 "(`git log` names `db2e821` as the commit that added it.)" — **CONFIRMED** (`git log --diff-filter=A -- data/p/verdicts/OLMo-sft_decisions.json` = db2e821).
67. d:69 "The analyzer alone read the three checkpoints" — **FAIL** (totality the record contradicts; made inconsistent by the filled counters bullet). C:5 (committed at 922d7a3) has the counters step read "each unit's three checkpoints and three call logs" after the runs, and d:192–193 says so; the sentence gives no scope. Correction: "At this run the analyzer alone read the three checkpoints" (or "Until the third run ended, …").
68. d:69 the brief: "read only by the analyzer (list v2 item 2)" — **CONFIRMED** (the three briefs' text as blk:357 quotes it: "p's checkpoints and call logs (`data/p/ckpt`) are read only by the analyzer (list v2 item 2). Never open them yourself.").
69. d:69–70 this session opened, listed and hashed none of them, and no call log — **NOT CHECKABLE** (the session's acts).
70. d:70–71 after the third run the amended brief gives the checkpoints and the call logs to the counters step alone (below) — **CONFIRMED** (R:934–935, the first amendment, checkpoints; A2:26 §2.2 and A2:62 item 5, "three checkpoints and three call logs"; R:1179–1181 "the counters step alone reads "each unit's three checkpoints and three call logs""; "below" = d:186).
71. d:108–109 "and the PI's "Start them" (undated; above)" — **CONFIRMED** (d:21; item 61).
72. d:111 "(iv) also gathered the campaigns' go" — **CONFIRMED** (blk:182, (iv); its item "the campaigns, given in steps", blk:192–198).
73. d:111 "which Q1 (c) put in the input as its item 6" — **CONFIRMED** (ans:15; In `[5]`, 2026-11-15, the campaigns' go).
74. d:116 the three inputs committed at `db2e821` before the first run — **CONFIRMED** (db2e821 adds the three; its subject "committed before the first run"; R:937).
75. d:117 "This session opened no sibling's output" — **NOT CHECKABLE** (the session's act).
76. d:117 "its end notice was its exit status and the window's release" — **CONFIRMED** (raw:44).
77. d:117–118 the coordinating session's notice "instruct, dpo and sft each EXIT=0" — **NOT CHECKABLE** (no file holds these words; the three exit statuses, 0 each, are recorded at C:3 and C:13).
78. d:118–119 the seat's §2, with both procedures: "no decision about any unit can follow a sibling's VERDICTS" — **CONFIRMED** (ans:23).
79. d:119 "No such decision is recorded here." — **CONFIRMED** (In: every item's `other_unit` Q-F0).
80. d:173 the declared set is the output's `counters.declared`, eight names — **CONFIRMED** (jq length 8).
81. d:174–175 the eight names, in that order — **CONFIRMED** (jq `.counters.declared[].name`).
82. d:175–176 the gate stages carry the same eight under `gate_release.{time,qual}.counters_beside.declared` — **CONFIRMED** (jq equality: true, true).
83. d:176 "None is untabulated (`not_tabulated` `[]`)" — **CONFIRMED** (jq).
84. d:262 "the campaign's A0s-OLMo-sft 14/32 (above)" — **CONFIRMED** (V `.rates`, P_sham 14/32; d:157–158).
85. d:262–263 the gate stages' shares were reported at their stages under m:318's exception (2) — **CONFIRMED** (m:318 exception (2), "the sham-template first-pick shares reported at G-TIME and qualification stages").
86. d:263 G-TIME-OLMo (p)'s A0s-OLMo-sft 1/1 (its entry, `2258c52`) — **CONFIRMED** (R:5432, sft row, "sham first pick" 1/1; `git show 2258c52 -- RESULTS.md` adds the row).
87. d:264–265 G-F0m-OLMo (p)'s 9/16, "9 of 16 (9/16)", in the block committed with that stage's entry (qb, `a225a89`) — **CONFIRMED** (qb:71; qb added at a225a89, the G-F0m-OLMo (p) ×3 entry's commit).
88. d:265 "The output carries none." — **CONFIRMED** (jq: `.gate_release.{time,qual}` hold `contrast_first_picks`, `counters_beside`, `released_free_round_events`, `stage`, `stage_end` only; no first-pick path outside `contrast_first_picks`).
89. d:284–286 the coordinating session's reading, quoted — **NOT CHECKABLE** (relayed; no file).
90. d:284 its inner quotation, Q2 (ii) holds "until the third run ends" — **CONFIRMED** (ans:8; R:922).
91. d:289 the analyzer's stdout went straight to the raw's path, unread — **CONFIRMED** as the script's design (rs:38–39 `>> "$R" 2> "$E"`; rs:5); "unread" itself is the session's act.
92. d:289–290 scrubbed, the repository root to `<repo>`, one occurrence, its INVOCATION line — **CONFIRMED** (raw:35 holds one `<repo>`; p_analyze.py:696 prints `sys.executable`; no `/Users/`, `/private/`, `/home/` or `/workspace/` remains; raw:2's `<repo>` is the header template, rs:22).
93. d:290–291 its closing section was appended — **CONFIRMED** (rs:7; raw:42–47 follow the stdout).
94. d:291 no sha256 taken before the scrub — **NOT CHECKABLE** (the session's act).
95. d:292–293 m:318: "the reads" "performed after the analyzer's output exists and before the entry is committed" — **CONFIRMED** (m:318 verbatim).
96. d:293–294 the seat's §5 item 5: committed open at "the reads", "as Q-F0's was (`0fa8539`)" — **CONFIRMED** (ans:41; 0fa8539's subject: Q-F0's VERDICTS and secondary entries).
97. d:294 "its §6 has the read close it" — **CONFIRMED** (ans:46 "Each read is placed as its own raw and closes its entry").
98. d:294 "Code follows the seat's order." — **CONFIRMED** (d:296, the entry drafted OPEN at "the reads", as ans:41 orders).
99. d:309 a decision about another unit taken from now is taken with this unit's outcome known — **CONFIRMED** (m:318, "A decision about one unit taken after another unit's VERDICTS exist").
100. d:309–310 m:318 records it "in that unit's VERDICTS entry or NOT-RUN record as taken with the other unit's outcome known" — **CONFIRMED** (m:318 verbatim).
101. d:310–311 the seat's §2 case of a run that "refuses or stops" — **CONFIRMED** (ans:25).
102. d:311 "did not arise: the three runs exited 0" — **CONFIRMED** (C:3, C:13, gate 1: "OLMo-sft=0, OLMo-dpo=0, OLMo-instruct=0", the end notices' statuses).
103. d:311 "(the coordinating session's notice)" — **NOT CHECKABLE** (relayed; no file).

## 3. The secondary entry: the Form bullet and the (a) heading

104. s:8 "**Form** (m:312; rule 28(a))" — **CONFIRMED** (m:312 opens "rule 28(a): each defined against the exclusion rule …").
105. s:8–9 (a), (b) and (d) each defined against the exclusion rule on its post-exclusion domain — **CONFIRMED** (m:312).
106. s:9 (e) the analyzer's reading of m:312's round event — **CONFIRMED** (m:312 "(e) a round"; Sec `.e` domains "… rounds generated").
107. s:9 "built under PIN-13" — **CONFIRMED** (m_analyze.py:4656, PIN-13 "Secondaries (a), (b), (d) and (e) are built now (m:312, pre-registered)").
108. s:9 "which the seat accepted at C6" — **CONFIRMED** (`results/raw/2026-10-10_m-design-to-code_pre-LOCK-v0.1.md`:75, C6: "PIN-13 accepted").
109. s:9–10 "no PIN states its domain" — **CONFIRMED** (m_analyze.py's register, :4445–4879: PIN-13 is the only entry naming (e), and states no domain; no p PIN names (e); Q-F0's entry has the same words, R:9451–9452).
110. s:10–11 every round generated in the campaign's 112 sessions, the one excluded session included (the counters' denominators) — **CONFIRMED** (Sec `.e` dens 320/476/128/192 = sums of V `.counters.denominators.rounds`; V `.counters.n_sessions` 112; V `.beside` 79/80 valid, 32/32).
111. s:11 "It counts no event, so the domain moves no numerator." — **CONFIRMED** (Sec `.e` nums 0 ×4).
112. s:11–12 m's decidable-n floor 20 events (the output's `floor_events`) — **CONFIRMED** (m:312 "m's floor is 20 events"; Sec `.floor_events` 20; m_analyze.py:178).
113. s:12–13 at or above it a two-sided Clopper–Pearson 95% interval, `rate()` at `m_analyze.py:1272` — **CONFIRMED** (m_analyze.py:1272 `def rate(`; :253–254 `cp_interval` "Two-sided Clopper-Pearson 95%"; the file's sha256 d347ea0c…5e48, the analyzer of record).
114. s:13 below it a count without an interval (`count_only`) — **CONFIRMED** (m_analyze.py:1274–1279).
115. s:13–14 "Every rate is num/den with its domain." — **CONFIRMED** (`rate()` returns num, den, domain; each Sec rate carries them).
116. s:14–15 `share` prints the reduced fraction (72/80 as 9/10, 44/80 as 11/20, 0/320 as 0/1); num and den carry the counts — **CONFIRMED** (Sec `.a["A0-OLMo-sft"]["1"]`, `["2"]`, `.e["A0-OLMo-sft"].forced`).
117. s:16 "(a) Clean-label share by position 1–6, by arm" — **CONFIRMED** (m:312).
118. s:16–17 (a)'s definition: the P-role label at free choice p, over sessions valid through p, "the choice at p was made and no exclusion-bearing event preceded it" — **CONFIRMED** (PIN-13, m_analyze.py:4657–4658; `valid_through`, :1284–1285; Sec domain "… sessions valid through position p"; identical to Q-F0's heading, R:9460–9461).

## 4. The close line (c:1–16), against 9189623's entry and close lines (R:799–989) and the raws it cites

119. c:1 "Close (PI date 2026-11-16): the sft VERDICTS session's." — **CONFIRMED** (ans:3, :62: the VERDICTS sessions add close lines; the date is the routing's, R:887–888).
120. c:1–2 the seat's raw names the three VERDICTS sessions for close lines — **CONFIRMED** (ans:3).
121. c:3 the answers raw's link path — **CONFIRMED** (tracked).
122. c:4 sha256 `01ae2ae7…1b0f` (full) — **CONFIRMED** (shasum, full string equal).
123. c:4–5 committed by path by the coordinating session at `18102d0` — **CONFIRMED** (`git log --diff-filter=A` on ans = 18102d0; its subject; R:883–886, :913–914).
124. c:5 on the PI's "Route as given" (PI date 2026-11-16) — **CONFIRMED** (R:887–888).
125. c:5–6 committed with OLMo-sft's outputs, raws and entries — **NOT CHECKABLE** (pending commit).
126. c:6 "on the paste block's item 6" — **CONFIRMED** (R:926 "6. Close lines on 9189623's entry citing the raw; ledger (75)."; ans:62).
127. c:8 Q1 (c), this session's reading — **CONFIRMED** (blk:64, :389; R:844).
128. c:8–9 the input holds the six items — **CONFIRMED** (jq length 6).
129. c:9 sha256 `54df4b85…e881` — **CONFIRMED** (shasum 54df4b851b97…e881).
130. c:9 committed by the instruct session at `db2e821` — **CONFIRMED** (`git log --diff-filter=A` = db2e821; its subject "with the instruct session's close line"; R:914).
131. c:9–10 this session confirmed the file by reading it only — **CONFIRMED** (R:954 "The sft and dpo sessions each confirmed their unit's file, reading it only.").
132. c:11 Q2 (a), with procedures (i) and (ii) — **CONFIRMED** (ans:8).
133. c:11 "which the run followed" — **FAIL** (adjudicates). It declares compliance with procedure (ii), which binds every session ("no session reads a sibling's output", ans:8, R:922), when this session can attest only its own conduct (pass 1's FAIL 86, applied at d:116–117); and (ii)'s "end notices carry the exit status alone" sits against this session's notice "sft verdicts ended, EXIT=0. Window released." (raw:44; d:32, d:117), which the entry reports without a reading, its first-opening disclosure being left to the seat (d:281–286). Correction: state the facts, e.g. "Q2 (a), with procedures (i) and (ii): the inputs were committed at `db2e821` before the first run; this session opened no sibling's output; its end notice is quoted in the VERDICTS entry".
134. c:11–12 on Q2 this session had given no reading — **CONFIRMED** (blk:396 "The sft session gave no reading on Q2.").
135. c:12 (the block: "the sft session gave none") — **IMPRECISE**. The words are 9189623's entry's (R:849, its summary of "the block's §5"); the block raw has no "gave none" (grep: 0) and reads "The sft session gave no reading on Q2." (blk:396). Correction: "(9189623's entry: "the sft session gave none")", or quote the block's own sentence.
136. c:13 the counters are the dpo session's step — **CONFIRMED** (R:891–893, the coordinating session's division; C:1; 922d7a3).
137. c:13 the read after the third run is Q4 (b)'s — **CONFIRMED** (ans:10, :33).
138. c:14 the gate stages' goes and `daca8b0` §0.1's sentence are in the VERDICTS entry's text — **CONFIRMED** (d:14–16, d:98–115).
139. c:15–16 ledger (75)'s fix verbatim — **CONFIRMED** (ans:50).

## 5. The raw's closing section, last item (raw:47)

140. "the INVOCATION line's interpreter path carried the repository's absolute root" — **CONFIRMED** (p_analyze.py:696 prints `sys.executable`; the interpreter is the repository's `jlens-qwen36/.venv/bin/python`, rs:38, raw:2; raw:35 reads `<repo>/jlens-qwen36/.venv/bin/python` after the scrub).
141. "It is replaced by <repo>, one occurrence, at line 35." — **CONFIRMED** (raw:35 holds one `<repo>`, the INVOCATION line; no absolute path remains; the other `<repo>`s are raw:2, the script's header template, rs:22, and raw:47 itself).
142. "Nothing else in the file changed." — **NOT CHECKABLE** (no pre-scrub copy). See Observation 7.
143. "No sha256 was taken before the scrub" — **NOT CHECKABLE** (the session's act).
144. "the sha256 an entry gives is the final file's" — **NOT CHECKABLE** (⟨RAW-SHA⟩ unfilled; consistent with d:291).

## 6. Scan of the two entry drafts for statements the changes made inconsistent

- d:69 "The analyzer alone read the three checkpoints" against d:192–193 "The step read each unit's three checkpoints and three call logs by exact path" (item 67, FAIL).
- d:216 "(above)" points at a statement that is below (d:249) (item 46, IMPRECISE).
- Outside the two entries but in the texts checked: c:11 "which the run followed" against d:31–32 and d:117 with procedure (ii)'s "exit status alone" (item 133, FAIL).
- The rest was read whole for this one thing. The changed passages agree with the unchanged ones on the arm-and-phase round counts (C 320/476/128/192 against d:177–178), G-F0m's s = 4 (1 call, 1 forced round, the pre-pick lexical exclusion at d:251–252 and d:257–258), the one excluded campaign session (s=74's 6 calls against d:171 and the 79/80 validity), the cap hits (d:180, d:199–204, d:257), the dpo session's step (d:191, c:13), and the end notice (d:32, d:117). The secondary's Form agrees with the VERDICTS counters on the 112 sessions and the one excluded session.

## OBSERVATIONS (not counted)

1. **RESULTS.md moved during this check.** HEAD went f62cf65 → d76f34f (n's ids, +83 lines at the top) → 679122e (dpo's VERDICTS entries, +416 at the top; +12 at the end of 9464f61's entry). Every `R:` here is f62cf65's. 9189623's entry is at 679122e:1310–1500, byte-identical to f62cf65:799–989. Pass 1's and the dispositions' RESULTS.md line numbers no longer match HEAD.
2. **"Yes, push first" is now in the record.** Pass 1 marked d:26's quotation NOT CHECKABLE. R:1174 (the coordinating session's close at 52b2c97, C.5) now records "`fa27c45..645bd3f`, 13 commits, on the PI's word "Yes, push first"". The entry could cite it. The passage is unchanged and was not re-graded here.
3. **"For the first time" (d:196–197)** holds for p §2.3's cells. m's analyzer had already counted the contrast cap hits under its own `cap_hit` at the VERDICTS run, before the counters step, as d:203–204 says. Writing "p's withheld cells" would make the scope explicit.
4. **What the step read.** C:5 has the step read "each stage's committed p report" too. d:192–193 names only the checkpoints and the call logs. This is not a claim of "only", so it is not an error.
5. **d:264 names no arm.** It reads "G-F0m-OLMo (p)'s 9/16"; G-TIME's share beside it names A0s-OLMo-sft. Pass 1's suggested wording was "G-F0m-OLMo (p)'s A0s-OLMo-sft 9/16".
6. **Whom "alone" binds (d:70–71).** The amended briefs' "counters step alone" binds the sessions. The seat reads the checkpoints after the counters step under its §6 (d:296–298), and the coordinating session's line carries "(the seat's own reads are §6's)" (R:899). The two passages are not inconsistent, but a reader may want that clause.
7. **Scope of raw:47's "Nothing else in the file changed".** The closing section itself was appended after capture (d:290–291). "The scrub changed nothing else" would be exact.
8. **The "It asserts" list.** The dispositions say "Added at db2e821" now sits outside it. In the draft the parenthetical is still inside the list's third bullet (d:43–44), though attributed to `git log`, which is fine as worded.
9. **The end notice in the entry.** The entry sets the notice's words beside procedure (ii) without a reading (d:31–32, d:116–117), which is the drafting role's form. Only c:11 reads compliance (item 133).
10. **The three runs' exits.** d:117–118 and d:311 rest on a relayed notice. C:3 and C:13, committed at 922d7a3, record the three exit statuses (0 each), and could be cited beside it.
11. **Line widths.** Only the two link lines run past 120 characters (d:188, c:3), which matches the dispositions.
12. **This check's own reads.** No Python. Of `data/p/verdicts`, only OLMo-sft's three files were read, with jq. Nothing under `data/*/ckpt`, `data/*/reports` or `data/mf3` was opened or listed, and `git status` was path-scoped. Content searches over the tree used `':!data/**'`.
    - Checking item 61 and the notice in item 77, this check read two passages of the dpo entry committed at 679122e (RESULTS.md 679122e:28–36, :80–87) and grepped the dpo raw and the dpo values-check raw for "EXIT=0" and "Start them".
    - `git show --name-status 679122e` printed the dpo output files' names (names only).
    - A grep over the scratch directory listed match lines in the drafter's `drytest/` files; they were not otherwise read.

## Totals

144 claims, counted by tool over the numbered claim lines above the scan section (each carries exactly one bold verdict): **128 CONFIRMED, 2 IMPRECISE, 2 FAIL, 12 NOT CHECKABLE.**

- FAIL (2): items 67 and 133.
- IMPRECISE (2): items 46 and 135.
- NOT CHECKABLE (12): items 62, 65, 69, 75, 77, 89, 94, 103, 125, 142, 143 and 144. They are the session's own acts and record, words relayed with no file, the pending commit and the unfilled ⟨RAW-SHA⟩.
- Clock times or stamps: none in the texts checked (pattern search over the three drafts and the raw).
- Adjudication: one sentence adjudicates, item 133.
- Unsupported totality claims: item 67, contradicted by C:5. Every other "every / all / none / no" claim in scope is sourced or is the session's own act.

## Code's dispositions of pass 2 (the sft VERDICTS session; PI date 2026-11-16)

Both FAILs and both IMPRECISEs are applied in the checker's terms, and so is every observation but the first, which
asks nothing of the texts.

- **FAIL 67** (VERDICTS, "The inputs"): applied. The sentence is scoped to the run: "At this run, the analyzer alone
  read the three checkpoints". The same paragraph keeps the counters step's later read ("After the third run, the
  amended brief gives the checkpoints and the call logs to the counters step alone").
- **FAIL 133** (the close line, Q2): applied. The bullet states the facts: the inputs committed at `db2e821` before
  the first run; this session opened no sibling's output; its end notice quoted in the VERDICTS entry. The VERDICTS
  entry's "For the seat" items gain one, **The end notice**. It quotes procedure (ii)'s "carry the exit status
  alone", this session's whole notice ("sft verdicts ended, EXIT=0. Window released.") and the coordinating
  session's grant ("and nothing else, and release"), and offers no reading.
- **IMPRECISE 46:** applied. G-F0m-OLMo (p)'s s=4 is "the session outside its domain (below)". The statement is in
  the release's gate-stage picks, which follow the counters bullet.
- **IMPRECISE 135:** applied. The close line quotes the block's own sentence: "The sft session gave no reading on
  Q2." (`results/raw/2026-11-16_p-verdicts-decisions_code-to-design.md`:396).
- **Observations:**
  - HEAD moved during the check (to `679122e`, the dpo VERDICTS entries). The entries cite no RESULTS.md line
    number. Each report's RESULTS.md citations are pinned to the HEAD its header names.
  - "Yes, push first" now cites the coordinating session's close at `52b2c97`: "`fa27c45..645bd3f`, 13 commits, on
    the PI's word "Yes, push first"".
  - "counted here for the first time" is scoped to p §2.3's cells.
  - The arm is named: "G-F0m-OLMo (p)'s A0s-OLMo-sft 9/16".
  - The raw's scrub item now reads "The scrub changed nothing else". The raw's sha256 moved with it, and the entry
    cites the final file's.
  - The counters step's gate 1 (`922d7a3`) is cited beside the coordinating session's notice that the three runs
    exited 0, in the Q2 paragraph and in "What follows".

**Edits after pass 2, checked by tool, not by a third blind pass:**
- The block's sentence: its line 396.
- The `52b2c97` quotation: RESULTS.md, the pickaxe over RESULTS.md alone naming `52b2c97`.
- The counters raw's gate 1: its line 13.
- The grant's words: against its message.
- Line widths: no line over 120 characters but the link lines.
- The final texts: no placeholder.
