# G-PWR (p), its run of record: the blind values-check of its entry, record, raw and program, before the commit.
# Code stamp: 2026-11-13 (date). One checker subagent, briefed with the list of record v2 items 1-5 quoted; its
# report below is verbatim except for local paths (<repo>, <scratch>). Code applied its two IMPRECISE items and
# its observations O3, O4 and O6 to the entry (each addition checked by tool), as the entry says.

BLIND VALUES-CHECK — G-PWR (p), its run of record: the entry draft (entry_run.md), the record data/p/gates/G-PWR-p.json, the run raw (scratch run_raw.txt, to be committed as results/raw/2026-11-13_p-gpwr.txt), and the program at 4c882e7.

Result: 135 claims. 129 CONFIRMED, 2 IMPRECISE, 0 FAIL, 4 NOT CHECKABLE. No figure is wrong. Every figure was recomputed independently on the standard library, and each matches the record exactly.

== CLAIMS ==
Header (entry lines 1–5)
1. Entry date 2026-11-13: CONFIRMED (the raw's Code stamp date).
2. PROPOSAL-p v0.2 §4.1: CONFIRMED (the chain "… → G-PWR; the PI's cap share → LOCK v1.0").
3. §8 step 6: CONFIRMED.
4. m:285: CONFIRMED (the G-PWR line).
5. The seat's read, §4.3 item 1: CONFIRMED.
6. Routed by the PI on 2026-11-13: CONFIRMED (a2c354e's message, "Route as given", 2026-11-13).
7. From the program's commit 4c882e7: CONFIRMED (HEAD and the record's head are both 4c882e77…).
8. k = 23, 24 and 24 of 24: CONFIRMED (the record, and the seat's §4.3 item 1).
9. "gives m:209's row": CONFIRMED (m:209 is "| 24–21 | 96 | 64 | **160** | 4 |…").
10. L 96 contrast, 64 sham: CONFIRMED.
11. 160 launches: CONFIRMED.
12. 4 looks: CONFIRMED.
13. Power at the floors .878: CONFIRMED, recomputed.
14. No n raised: CONFIRMED (n_raised is false).
15. The three campaigns come to 3.35 h at m:205's basis: CONFIRMED (see O3).
16. p's 12 h budget: CONFIRMED (p §6.1; budget_h 12).
17. The cap share is the PI's; STOP: CONFIRMED (seat §4.3 item 1 and §8 item 4).

The record
18. The path data/p/gates/G-PWR-p.json: CONFIRMED (untracked, not ignored).
19. Written once by the run: CONFIRMED (write-once refusal in the program; the second run wrote to scratch).
20. sha256 bc2b0909…d604 in full: CONFIRMED (shasum is equal; the second-run copy is byte-identical).

The run
21. By a wrapper: CONFIRMED.
22. The project's venv, Python 3.12.9: CONFIRMED (raw; record; I re-ran the version print).
23. -I -B: CONFIRMED (raw command; isolated true).
24. A pycache prefix that does not exist: CONFIRMED (wrapper and program both refuse if it exists; it is still absent).
25. Under env -i: CONFIRMED.
26. No fsck.*, core.fsmonitor or core.hooksPath in git's config: CONFIRMED (raw; the config is empty now too).
27. git status over the five paths empty: CONFIRMED by the raw.
28. Working-tree blob equal to HEAD's: CONFIRMED (b742a69a… both).
29. The record absent at launch: CONFIRMED by the raw.
30. No git fsck, with list v2 item 2 as the reason: CONFIRMED.
31. The self-test runs from the committed blob at HEAD in its own process: CONFIRMED (_P_CHILD_BOOT).
32. 24/24: CONFIRMED (24 PASS lines, identical to the committed self-test raw at 4c882e7).
33. HEAD 4c882e7: CONFIRMED.
34. Script 3e4348b1…0464: CONFIRMED (working tree and HEAD).
35. m_gpwr 1d7c0fe3…111c: CONFIRMED.
36. Executed from its blob 6d05c8e6…: CONFIRMED (rev-parse HEAD:scripts/m_gpwr.py).
37. Q-F0's G-PWR blob unchanged: CONFIRMED (the blob at 43f3bb2 is the same; Q-F0's record has script_sha256 1d7c0fe3…; the only commit to m_gpwr is 78f5602).
38. Analyzer d347ea0c…5e48: CONFIRMED.
39. m's package 7756dcf4…49bb: CONFIRMED (recomputed over HEAD's 18 valence_core/m/*.py blobs and on disk; the LOCK-p files name the same value).
40. Every repository module loaded was bound to its blob: CONFIRMED by construction. The run refuses otherwise, and the 13 closure hashes equal HEAD's and the disk's.
41. Each input's committed text at its commit: CONFIRMED (all 9 source sha256s recomputed with git show at their commits).
42. The three pinned sha256s equal: CONFIRMED (answers, PROPOSAL-m, PROPOSAL-p).
43. A second run on the same interpreter and settings: CONFIRMED (wrapper line 310).
44. Its record byte-identical: CONFIRMED (cmp; same sha256).
45. Its stdout identical except the WROTE line: CONFIRMED (the .cmp files are identical, and each is its stdout minus the WROTE line).
46. The verifier is out of process and standard library only: CONFIRMED (json, sys, fractions, math).
47. Python 3.9.6, -I -S: CONFIRMED.
48. 63/63: CONFIRMED (63 PASS lines, 0 others).
49. "It recomputes every figure but the Fisher half, the union and the grid maxima": IMPRECISE. The verifier does not recompute:
   - the power at the floors or PIN-3 (it only checks that the stored exact value is ≥ .85 and that the display is its rounding);
   - the rows at other k ("the same row at k = 21–24");
   - the Fisher cells or the 99 grid values.
   It compares k, r and the sham seconds against constants. The review raw also says "Power (.8784) was not recomputed independently", so the power was recomputed by neither.
   Fix: "It recomputes the launch rule, the totals and looks, every case's looks, round_degeneracy, the guard's absolute half and the hours. It does not recompute the Fisher half, the union or the grid maxima, which the blind review recomputed and the self-test pins. It checks the power at the floors only against .85 and its display; the power is bound to Q-F0's value by m_gpwr's pin and the regression." Optionally add: "this values-check recomputed the power: .8784, exact."
50. The blind review recomputed those: CONFIRMED (review raw: guard table at .20; round 2 recomputed the grid maxima).
51. They are pinned in the self-test: CONFIRMED (REVIEWED and REVIEWED_GRID).
52. WRAPPER EXIT 0: CONFIRMED.
53. The raw at results/raw/2026-11-13_p-gpwr.txt: NOT CHECKABLE. It is not yet committed; its content is the scratch run_raw.txt.
54. The raw carries the output, the wrapper's source and the verifier's: CONFIRMED. After the scrub, both sections equal the scratch files byte for byte.
55. Local paths scrubbed: CONFIRMED.

The table
56. sft: 23; 23/24. CONFIRMED.
57. dpo: 24; 1. CONFIRMED (the record has 1/1).
58. instruct: 24; 1. CONFIRMED.
59. sft 7/8, 16/16: CONFIRMED (also in the a225a89 entry).
60. dpo 8/8, 16/16: CONFIRMED.
61. instruct 8/8, 16/16: CONFIRMED.
62. ceil(1.15 floor) = 92 and 37: CONFIRMED.
63. N90 at sft = 86, 35: CONFIRMED.
64. N90 at dpo = 80, 32: CONFIRMED.
65. N90 at instruct = 80, 32: CONFIRMED.
66. 96, 64; 160; 4 at each unit: CONFIRMED.
67. sft power .878 (.8784): CONFIRMED.
68. PIN-3 .878 at each unit: CONFIRMED.
69. dpo and instruct power .878: CONFIRMED.
70. sft: (160 + 26) × 22.7 s = 1.17 h. CONFIRMED.
71. dpo: the same. CONFIRMED.
72. instruct: × 19.5 s = 1.01 h. CONFIRMED.

After the table
73. The same row at k = 21–24 (m:209): CONFIRMED (k_with_this_row is [21, 22, 23, 24]; recomputed).
74. The hours sum to 3.35 h: CONFIRMED.
75. "3.4, m:214's figure at 160 each": CONFIRMED.
76. Beside p §6.1's 12 h: CONFIRMED.
77. The sham seconds are "m's report's sum over the sixteen": CONFIRMED against the a225a89 entry. The report itself was not opened.
78. Beside, no basis: CONFIRMED.
79. 102.105 s: CONFIRMED.
80. 88.389 s: CONFIRMED.
81. 85.237 s: CONFIRMED (the seat gives 102.1, 88.4, 85.2).

False-pause figures
82. The same at all three units except sft's floor case: CONFIRMED by a structural diff of the three units.
83. Looks at launches 40, 80, 120 and 160: CONFIRMED.
84. A0 20, 40, 60, 96: CONFIRMED.
85. A0s 20, 40, 60, 64: CONFIRMED.
86. p0 .02, α .05: CONFIRMED (also m:330).
87. Sham rounds 200, 400, 600, 640: CONFIRMED.
88. crit_j 8, 14, 19, 20: CONFIRMED.
89. .0863: CONFIRMED.
90. The common rate .20: CONFIRMED.
91. Fisher half .0699: CONFIRMED.
92. The pausing figure on OLMo (m:316): CONFIRMED.
93. Absolute half .0929: CONFIRMED.
94. Crits 8, 13, 18, 27: CONFIRMED.
95. The absolute half reported only: CONFIRMED (m:316).
96. Union .1311: CONFIRMED.
97. Grid maximum .0768 at 1/2: CONFIRMED.
98. Refined .0768 at 251/500: CONFIRMED.
99. "The union's maximum over p ≤ .20 is .1311, at .20": IMPRECISE. It is a grid maximum over p = j/100 (the record's key is union_grid_max_p_le_p0, and the raw says "union grid max"). Fix: "The union's grid maximum over p ≤ .20 is .1311, at .20."

Q7 (a)'s cases
100. ceil(32/r) = 34 at sft: CONFIRMED (ceil(768/23)).
101. 130 launches: CONFIRMED.
102. .0705: CONFIRMED.
103. Fisher .0553: CONFIRMED.
104. Absolute .0868: CONFIRMED.
105. Union .1198: CONFIRMED.
106. At 32, the same as ceil(32/r) at dpo and instruct: CONFIRMED (in the record, those units' floor_r equals floor_min).
107. 128 launches: CONFIRMED.
108. .0609: CONFIRMED.
109. Fisher .0545: CONFIRMED.
110. Absolute .0873: CONFIRMED.
111. Union .1198: CONFIRMED.
112. 160 of 160 realised rounds at each checkpoint: CONFIRMED (the record's inputs; a225a89).
113. The projection's, .0863: CONFIRMED.

The joint and what is not figured
114. The joint is round_degeneracy's own, .0863: CONFIRMED.
115. The Fisher half beside, .0699: CONFIRMED.
116. Not computed, with one sentence why (Q7 (c)): CONFIRMED.
117. Hair triggers: no p0. CONFIRMED.
118. Lexical: no domain on OLMo (m:330). CONFIRMED.

Readings
119. Ten readings in the record: CONFIRMED (the raw's READINGS has 10 lines, equal to the record).
120. The form is F-5's for Q-F3, applied to p: CONFIRMED (ganl-f3 answers, line 28).
121. Q7's methods carried to p's units: CONFIRMED.
122. The Fisher half alone pauses on OLMo, and the joint's guard beside is the Fisher half: CONFIRMED.
123. Q-F0's record carries the union: CONFIRMED (its joint.guard_beside is 0.1496, which is its projection's union; its Fisher half is .0766).
124. round_degeneracy at OLMo's p0, by bars' own calls: CONFIRMED (reading 5).

Cap share and close
125. The cap share per checkpoint within 12 h is the PI's at G-PWR: CONFIRMED.
126. The quote "[your call at G-PWR]", seat §8 item 4: CONFIRMED, verbatim.
127. This run sets none: CONFIRMED (the record says "not set by this program").
128. The figures go to the coordinating session for the PI: NOT CHECKABLE (future act).
129. The track STOPs until the cap share is given: NOT CHECKABLE. It is the entry's own act, and it is consistent with p §4.1, §8 step 6 and the program entry's "Next".
130. LOCK-p v1.0 ×3 carry the launch counts, the looks and the cap share: CONFIRMED (seat §4.3 item 3).
131. D_p is 2026-12-15: CONFIRMED (p §5.3).
132. The campaign wiring's build may proceed (§4.3 item 2): CONFIRMED.
133. Committed by path: the record, the raw, the values-check raw and the entry. NOT CHECKABLE (future act).
134. Nothing ran on a model or a box: CONFIRMED for this run (the program is model-free; the raw says "no model process").
135. Not pushed: CONFIRMED (origin/main is 16c99d5, and 4c882e7 is not in its log).

== TOTALS ==
135 claims: 129 CONFIRMED, 2 IMPRECISE (49 and 99), 0 FAIL, 4 NOT CHECKABLE (53, 128, 129, 133).

== RECOMPUTATIONS ==
All on the standard library only, run with -I -S under nice -n 10. No repository import. Each result equals the record's exact Fraction, at all three units.

Launch rule
- k = 23 (r = 23/24):
  - A0: ceil(1.15 × 80) = 92. N90 = 86, because P(Bin(85, 23/24) ≥ 80) = .8563 < .90 and P(Bin(86, 23/24) ≥ 80) = .9323. L = ceil to 32 of max(92, 86) = 96.
  - A0s: ceil(36.8) = 37. N90 = 35, because P(Bin(34, 23/24) ≥ 32) = .8326 and P(Bin(35, 23/24) ≥ 32) = .9434. L = 64.
- k = 24: N90 is 80 and 32, giving L 96 and 64.
- Total 160; looks ⌈160/40⌉ = 4.
- I rebuilt the rows for k = 1–24; they equal the record's rows_by_k. The row (96, 64, 160, 4) holds exactly at k = 21–24.

round_degeneracy on the projection
- Sham rounds are cumulative: 200, 400, 600, 640. p0 = 1/50, α = 1/20.
- crit_j = 8, 14, 19, 20. P(X ≥ crit) is .0493, .0327, .0359, .0359; at crit − 1 it is .1086, .0619, .0610, .0603.
- The exact sequential false pause, from a dynamic programme over the cumulative count that absorbs at each look's crit, is 0.0863046… → .0863.
- The floor cases:
  - [200, 340, 340, 340]: crits [8, 12, 12, 12], false pause .0705.
  - [200, 320, 320, 320]: crits [8, 12, 12, 12], false pause .0609.

Beyond the minimum (each exactly equal to the record)
- Every case's looks under the campaign rule.
- The guard, with my own hypergeometric tail and joint dynamic programme:
  - projection: absolute .0929 (crits 8, 13, 18, 27), Fisher .0699, union .1311; Fisher cells 119, 568, 1384, 2436;
  - floor_r at sft: .0868, .0553, .1198 (cells 119, 556, 1085, 1213);
  - floor 32: .0873, .0545, .1198 (cells 119, 546, 1033, 1135).
- All 99 Fisher grid values. The grid maximum is .0768 at 1/2; refined in steps of .001 over 49/100–51/100, it is .0768 at 251/500. The union's grid maximum for p ≤ 1/5 is .1311 at 1/5.
- Power at the floors. I implemented the base case myself: each map 40 at clean share .70 with the half-per-map condition, the sham 32 at .5, α .01. The critical count at n = 80 is 51 (m:190's own "80 at .01 → 51"). Power is .8784 → .878, equal to both the power and PIN-3 fields.
- Hours: 7037/6000 (1.17, 1.2), 403/400 (1.01, 1.0); the sum is 20119/6000 (3.35, 3.4).

The raw against the record
- I re-rendered the raw's 144 report lines from the record with my own renderer: 0 mismatches.
- The PROVENANCE and SOURCES lines parse equal to the record, and the WROTE sha256 is equal.
- Raw lines 16–188 equal first-run.stdout.txt verbatim.
- Leak scan of the raw:
  - no local path: only the <repo> and <scratch> placeholders, plus /usr/bin, /var/empty and the nonexistent pycache prefix;
  - no clock time or timestamp: dates only;
  - no IP, port or email: "@" appears only in "${ENVI[@]}";
  - no $ figure: "$" appears only in shell expansions.

== OBSERVATIONS ==
O1. Claim 49 broadens the program entry's scope. The program entry says the verifier recomputes "all but" three figures within the reviewed figures; this entry says "every figure". The power .8784 is recomputed by neither the verifier nor the review. It rests on m_gpwr's sha256 pin of Q-F0's value and the regression. This check recomputed it, and it is equal.
O2. Claim 99: the union's figure is a grid maximum, not a supremum.
O3. This is for the PI's cap share:
   - The 3.35 h includes each checkpoint's 26 gate sessions, which have already run. That follows m:205's convention, and p §6.1 calls these "campaign figures".
   - It does not include the cold load per checkpoint that p §6.1 adds.
   - p §6.1's 12 h covers G-CAL-p, the gate stages and the campaigns together.
   - The table shows "(160 + 26)", but the header line does not; one clause would make it explicit. I add no figure here.
O4. The raw's "wrapper rc=0" line is not printed by the wrapper and is not in its source. Because the wrapper ends with an echo, its exit status is 0 whatever WRAPPER EXIT prints. The entry rightly cites WRAPPER EXIT 0. The raw could say where that line comes from, or drop it.
O5. The raw's wrapper and verifier sections equal the current scratch files. That they are "as it ran" cannot be checked independently, but the verifier's 63 check names match its code.
O6. Optional additions the entry could carry:
   - the run's 24 self-test lines are identical to the committed self-test raw;
   - nine sources were verified;
   - a2c354e beside the routing date, as the program entry has it;
   - the LOCK-p v0.2 files name the same analyzer, package and proposal sha256s.
O7. Otherwise the entry, raw, record and program entry agree, and the program entry's "Next" was carried out as declared.

== DISCLOSURES ==
- Reads beyond the brief:
  - p_gpwr.py lines 1–330, 772–787 and 1100–1232;
  - m_gpwr.py lines 231–430;
  - bars.fisher_sf;
  - m_analyze.power_exact, which I read to learn the pass conditions before writing my own power code;
  - resume.package_sha256_of;
  - parts of the program's review and self-test raws;
  - RESULTS.md at HEAD, lines 1–117;
  - RESULTS.md at a225a89, lines 24–168. That range runs into the next entries and includes a write-time stamp, which I have not reproduced.
- Further reads: PROPOSAL-m lines 185–216, 271, 285, 316 and 330; PROPOSAL-p lines 82–135; step-15 answers lines 44–56; the F-5 line of the ganl-f3 answers; count-only greps of the three LOCK-p files for four hashes; Q-F0_G-PWR.json (provenance, joint, guard, inputs).
- Scratch files read beyond the brief: the first-run and second-run stdout and .cmp files, run_p_gpwr.sh, verify_p_gpwr.py, and G-PWR-p.second-run.json (hashed and compared with cmp). The second-run WROTE line holds a scratch path, which I masked in my output.
- Commands outside item 1's list:
  - git config --get-regexp (printed nothing);
  - git check-ignore -q on the record (exit status only);
  - git show <commit>:<path> on committed texts and source blobs, none under data/;
  - git hash-object --no-filters;
  - wc -l on scripts and raws, none under data/;
  - version prints of /usr/bin/python3 and the project's venv Python under env -i;
  - an existence test on the pycache prefix;
  - od -c on the raw's tail;
  - git rev-parse origin/main.
- Nothing under data/*/ckpt or data/*/reports was opened, listed, hashed or searched. The only data files read were the two gate artifacts (data/p/gates/G-PWR-p.json and data/m/gates/Q-F0_G-PWR.json), plus git ls-files of data/p/gates. Every grep was a single-file /usr/bin/grep; there was no tree search and no pickaxe.
- No git write. p_gpwr.py was not run. No model process.
- I wrote only in my own scratch folder, not the repo:
  - <scratch>/vc_gpwr_run/recompute.py
  - <scratch>/vc_gpwr_run/render.py
  - <scratch>/vc_gpwr_run/raw_wrapper.txt
  - <scratch>/vc_gpwr_run/raw_verifier.txt
- No departure from list v2 items 1–5 that I know of.
