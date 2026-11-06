# PROPOSAL-n v0.2 step 3 — the blind values-check, and Code's dispositions

*The checker was a blind subagent, given the three texts and the sources but not Code's reasoning, and it ran
read-only. Its report follows verbatim, with Code's scratch directory written as `<scratch>`. The harness refused the
checker's own report file, so the text below is the report as the checker returned it. Code re-checked every
IMPRECISE item and every observation at source; the dispositions are in §2.*

## 1. The checker's report (verbatim)

# Blind values-check of the PROPOSAL-n v0.2 step-3 commit texts

**No FAIL. 16 IMPRECISE, each correct in substance.** One process item needs action before the commit: `data/n/` is gitignored (item 50 / O1).

**Totals:** 188 graded items, plus 1 that cannot be verified from here (item 175).
- **PASS 172**
- **FAIL 0**
- **IMPRECISE 16:** items 18, 32, 38, 43, 44, 49, 50, 80, 102, 129, 135, 137, 147, 158, 172, 180.

The harness refused the report file ("Subagents should return findings as text, not write report files"), so nothing exists at `<scratch>/vc_n02/report.md`. The full report is below. My scripts are in `<scratch>/vc_n02/scripts/`; they ran under `python3 -I`, with BK files passed as arguments. Nothing in the repo or the BK clone was modified or executed.

Locators: E = the entry draft, R = the referent-check raw, S = SOURCE.md, bk = `bk_v2.txt`, v0.2:N = a line of PROPOSAL-n v0.2.

## The IMPRECISE items

**18. E:38–39.** "'Everything else as the 11-05 routing had it' carries the 11-05 block's PROPOSAL-n lines."
- Decision 7 (the pod order) is not among those lines (RESULTS.md:340–343).
- It is in the block's ADDENDUM-m1 lines, RESULTS.md:339: `>   Pod order: [OLMo units first, then PROPOSAL-n's N-pod].`
- The clause should name both. The citation of the ADDENDUM-m1 entry's quote (RESULTS.md:325–346) is right.

**32. E:60.** "Every [S] figure reproduces from `reduced.json`'s 160 neutral sessions (the raw §2.4)."
- The statistical [S] figures do.
- v0.2 §9's [S] list (v0.2:165) also contains figures that do not come from `reduced.json`:
  - the §2.4 and §0.4 counts and the tuple count 385 (arithmetic on v0.2's own text);
  - 0.916/3 (arithmetic);
  - the ladder's 0.1222 (interpolated from `figureA10.csv`).
- All of them reproduce. Only the stated source is wrong.

**38. E:70.** N2: "§2.4's '≈ 420' is 464, so ≈ 3,184 re-computations and ≈ 10,544 forwards."
- The arithmetic is right under Code's reading, but the reading is not stated.
- N4-T and N4-Ts are 320 reads at "none (d = 0)" (v0.2:92–93).
- v0.2 §2.1 (v0.2:77) re-computes "every read" at d ∈ {0, +1, −1} and samples 10% only of "the other points".
- On that rule:
  - the 10% sample is 10% of 4,320 = 432;
  - re-computations are 480 + 1,920 + 320 + 320 + 432 = 3,472;
  - forwards are 10,832.
- §2.4's own list (v0.2:95) puts N4 in neither group, and the seat's ≈ 420 is nearer 432 than 464.
- See also item 158.

**43. E:76.** "`data/n/bk/`, 34 MB, `reduced.json` 28 MB of it." The units are mixed.
- The folder is 35,334,379 bytes: 35.3 MB, or 33.7 MiB (`du -sh` prints "34M", in MiB).
- `reduced.json` is 28,053,197 bytes: 28.1 MB, or 26.8 MiB.
- Use "35 MB / 28 MB" or "34 MiB / 27 MiB".

**44. E:77–81.** "Contents. The G-DATA (ii) set: … BK's `LICENSE`."
- `LICENSE` is not in G-DATA (ii)'s list (v0.2:107 (ii)). It is Code's addition (R N5).
- SOURCE.md has it right: "G-DATA (ii) list plus `LICENSE`".

**49. E:84–86.** "The attribution line (`data/n/bk/SOURCE.md`): … at `7631f8a…`, licensed CC BY 4.0, copied unmodified and read as data."
- Every value is correct. But this is not SOURCE.md's line. SOURCE.md reads: "Replication files from the authors' repository, github.com/camberg23/act-on-valence, at commit `7631f8a06cde…` (tree `d6f1d505…`, committed 2026-10-05), licensed CC BY 4.0. The license text is `LICENSE` in this folder, copied unmodified."
- In SOURCE.md, "copied unmodified" refers to `LICENSE`, and "read as data" is the file's heading.
- Quote the line, or mark the entry's version as a summary.

**50. E:87.** "Committed by path: … `data/n/bk/` (the 26 files, `SHA256SUMS`, `SOURCE.md`) …" This is a process issue and needs action.
- `data/n/` is gitignored:
  - `.gitignore:5` is `/data/*`, with no `!/data/n/` exception;
  - `git check-ignore -v` reports `.gitignore:5:/data/*` for the files;
  - `git status --porcelain --ignored data/n` shows `!! data/n/`.
- A by-path `git add` refuses these paths unless run with `-f`.
- The repo's convention (.gitignore:8–10, "Exceptions are per-directory and deliberate, never blanket") is a commented exception block like the one for data/m/. That would put `.gitignore` into this commit, and the list does not name it. The block would have to admit `.jsonl`, `.csv`, `LICENSE`, `SHA256SUMS` and `.md` under `data/n/bk/`.

**80. R:54.** "k:111–127 is its [5(f)'s] rule-level block ✓." The locator is off.
- The 5(f) bullet is k:111–125 and ends "passed. Full text in Appendix A."
- k:126–127 open the next bullet, "- **5(d)** [verify] governs prefix-steered/choice-unsteered reads at ≥ 0.20 …", which runs to k:129 and includes 5(e).
- The v0.1 STOP raw's C10 (STOP raw:238–239) already split it this way: "the 5(f) readout class (k:111–125) and the head of its 5(d) bullet (k:126–127)".

**102. R:89.** Under §3.2.2: "To construct the unsteered cache, we reprocess the same sequence of tokens without steering."
- The sentence is in §3.2.1, "Separating the text and hidden-state channels" (bk:240).
- §3.2.2 starts at bk:248.

**129. R:146–147.** "All figures below come from `reduced.json`'s 160 neutral sessions …; the scripts are v0.1's `repro_s.py` and `spans.py`, run again."
- These table rows come from neither `reduced.json` nor those scripts:
  - the §2.4 reads, re-computations and forwards rows;
  - the §0.4 row;
  - the tuples row;
  - 0.916/3.
- They are arithmetic on v0.2's text (Code's `arith_v02.txt`), and the ladder row comes from `figureA10.csv`.

**135. R:156.** "SE at +1: 0.049 | 0.0494." The conventions are mixed.
- 0.0494 is SD(ddof 1)/√160 = 0.625264/12.649 = 0.049431.
- Under the ddof-0 convention that v0.2 §2.5 declares and that the table's SD row uses, it is 0.623307/√160 = 0.049277, i.e. 0.0493.
- The table's §2.5 SE of 0.0195 is a ddof-0 figure.
- The [S] value 0.049 holds either way.

**137. R:158.** "§2.4 reads: 960; 4,800; 320; 320 + 320 (N2-E; N2-S/N2-C 320 each); 160; 160 | ✓, sum 7,360."
- As written, these numbers sum to 7,040.
- v0.2:165 lists "960; 4,800; 320; 320; 320 + 320; 160; 160": N1-V, N1-R, N1-P, N2-E, N2-S + N2-C, N4-T, N4-Ts. That sums to 7,360.
- One 320 is missing from the row. The total itself is right.

**147. R:176–178.** "No released BK file and no section of the paper defines it either: a search of every string in the clone's JSON, MD, TXT and TEX files, and of the PDF's text, finds only mean scales, `mean_scale_nats` and `mean_scale_{clean,natural}_nats`."
- The conclusion holds. I walked every JSON/JSONL key and value (214 files) and searched the 32 .py, 18 .R, 8 .md and 4 .tex files and the paper text. No per-read scale is defined anywhere.
- But "finds only mean scales" is wrong. The JSON also carries:
  - 411 `scale` objects ("sd of the choice margin at dose 0 … standardized slopes"), in `strength_ladder/analysis.json` (a copied file) and in the span_sweep, exposure_sweep and strength_ladder_extension analyses;
  - `absolute_tolerance_as_fraction_of_scale` (77 occurrences);
  - `steered_sep_scale` and `steered_sep_scale_254`, `norm_match_scale`, `vs_unscaled_e1`;
  - in `dose_calibration/panel_prereg.json`: "TAU = 0.0178835444, derived from the old 0.20-nat tolerance and OLMo rows only".
- The clone has no TXT files, and the stated scope omits its .py and .R files. Those contain no definition either.

**158. R:198–200.** N2: "464 by §2.4's own table … the rest … N2; N4."
- The arithmetic is correct, but putting N4 in "the rest" is an unstated reading.
- By §2.1's rule, N4's d = 0 reads are fully re-computed, which gives 432 / 3,472 / 10,832 (details in item 38).
- N2 should name the reading, or LOCK v0.1 should settle which text governs.

**172. R:264.** "On the neutral reads at gen_point 0 (n = 2,400)."
- BK's neutral reads at gen_point 0 number 4,640: 160 `none`, 640 valenced, 3,840 random.
- The 2,400 are the ones that carry `fidelity_absdiff`: 160 at d = 0, 320 valenced at ±1, 1,920 random at ±1.
- The same shorthand, "the 2,400 neutral reads", appears at R:131 and R:191.
- The counts are all right: 0 exceed TAU × scale, 570 (0.2375) exceed TAU/4 × scale, the max ratio is 0.012143, and over all 2,640 reads the counts are 0 and 626.

**180. S.** "The license text is `LICENSE` in this folder, copied unmodified."
- It is copied unmodified: sha 9570384a… in both places.
- But BK's `LICENSE` is a short notice, not the license text: a title, a copyright line, a scope sentence, and "The full licence terms are available at https://creativecommons.org/licenses/by/4.0/legalcode."
- Suggested wording: "BK's licence notice, which links the CC BY 4.0 legal code, is `LICENSE` …".

## Observations (not claims in the texts)

- **O1 — action before the commit.** The gitignore issue in item 50.
- **O2 — for the push** (your memory note: screen hosts against N12 PUBLIC_HOSTS). The only URL host in the copied files is `creativecommons.org`, in BK's `LICENSE`.
  - It is not in `scripts/audit_note_N12_history.py`'s PUBLIC_HOSTS (lines 784–801).
  - `audit_note_N12_licenses.py:2934` and `:2979` do know it.
- **O3 — further support for N1's identification.** Under max(|lpS|, |lpU|), BK's other numbers also reproduce:
  - session-level retention ×0.25 = 93/240 = 0.3875 and ×0.5 = 233/240 = 0.970833, equal to `retention_relative_x0.25` and `_x0.5`;
  - `absolute_tolerance_as_fraction_of_scale` 0.017931671874052292 equals 0.20/`mean_scale_nats` exactly;
  - 0.20/TAU = 11.1835 nats.
- **O4 — informational.** BK's Fig. A8 OLMo passage slope (0.916730) is not the per-session OLS mean over `reduced.json` (0.916417, the [S] 0.916; the pooled fit is the same, and a fresh-margin variant gives 0.918078). v0.2 quotes the two correctly as different figures; they should not be equated later.

## v0.2's own arithmetic, recomputed from its text

- **§2.4 reads:** 960 + 4,800 + 320 + 320 + 320 + 320 + 160 + 160 = 7,360. Correct.
- **Re-computations:** 480 + 1,920 + 320 are correct. "≈ 420" does not follow: it is 464 with N4 in "the rest", or 432 with N4's d = 0 reads fully re-computed. "≈ 3,140 / ≈ 10,500" therefore become 3,184 / 10,544, or 3,472 / 10,832. These are planning values.
- **§0.4:** all cells and totals are consistent: 48 / 320 / 960; +48 / +640 / +1,920; −48 / −320 / −960.
- **§2.5:** 0.545 is half of 1.0900. The bar is about 11 SE below the mean, so P > .99. A mean of 0.10 is 2.03 SE, so its CI excludes 0. 0.916/3 = 0.305, the ladder value 0.1222, the interpolated SD 0.2469 and the SE 0.0195 are all correct.
- **Tuples:** 4 × 3 × 4 × 4 × 2 + 1 = 385. Correct.

## All items

### A. Entry (E)

1. Title: COMMITTED, PI date 2026-11-06, at §8 step 3. **PASS**.
2. The process line ("minor residues as dated notes"). **PASS**.
3. The v0.2 sha256 30a3d0f5…b104f4. **PASS**: matches both shasum and RESULTS.md:176.
4. The five §1 questions, "one factor at a time". **PASS**.
5. v0.1 9248d06c…b6a6 moves to archive/, uncommitted. **PASS**.
6. BK files copied with shas and the attribution line. **PASS**.
7. HEAD db97d8e is three commits ahead of origin's 9cbacdb. **PASS**.
8. No n artifact at step 1. **PASS**.
9. Every §9 referent resolves and every [S] figure reproduces. **PASS**.
10. Nothing substantive; five notes. **PASS**.
11. N1 identifies the scale by reproduction. **PASS**.
12. Unit states and dates. **PASS**.
13. G-DATA waits for the OLMo-2 tokenizer (the HF cache holds only Olmo-3-1125-32B among allenai models); nothing built; no pod. **PASS**.
14. The stamp 17:56:21 UTC. **PASS**: matches the draft's mtime, 12:56 EST.
15. The routing quote. **PASS**: byte-identical to RESULTS.md:172–186 once the 6- and 4-space list indents are removed.
16. "as dc1ffe1's close line quotes it". **PASS**.
17. "the record of §0.9's decisions". **PASS**.
18. **IMPRECISE** (above).
19. The letter n; o for the told control. **PASS**.
20. Decision 1, the date. **PASS**.
21. Decision 2. **PASS**.
22. Decision 3, with §0.4. **PASS**.
23. Decision 4, with §0.8. **PASS**.
24. Decision 5. **PASS**.
25. Decision 6, with §7.4 and §2.7. **PASS**.
26. Decision 7, its value. **PASS**.
27. The v0.2 and v0.1 hashes. **PASS**.
28. 28 untracked entries; the routing names only v0.2 among them. **PASS**.
29. No data/n/, valence_core/n/, scripts/n_* or LOCK-n*, and no git history for any of them. **PASS**.
30. Referents resolve in the repo, the PDF and the BK repo at 7631f8a. **PASS**.
31. Carried referents are byte-unchanged since 24ebeae. **PASS**.
32. **IMPRECISE** (above).
33. N1's locators, §2.1 and §9. **PASS**.
34. No file or the paper defines the scale. **PASS**.
35. An exact reproduction of 11.153449684153905 over 2,640 reads (float `==`). **PASS**.
36. G-DATA (vi), in C13's form. **PASS**.
37. 0 of 2,400, so p0 = 0 and a hair trigger. **PASS**.
38. **IMPRECISE** (above).
39. Planning values. **PASS**.
40. N3. **PASS**.
41. N4. **PASS**.
42. N5. **PASS**.
43. **IMPRECISE** (above).
44. **IMPRECISE** (above).
45. The contents list. **PASS**.
46. 26 files byte-identical (cmp). **PASS**.
47. SHA256SUMS checks 26/26. **PASS**.
48. The concatenation be50011a…c3ba84, as STOP raw:353–354 records. **PASS**.
49. **IMPRECISE** (above).
50. **IMPRECISE** (above).
51. Not pushed; origin is told-vs-felt, which is public. **PASS**.

### B. Raw (R)

52. The header sha. **PASS**.
53. The ✓ semantics (STOP raw:260). **PASS**.
54. The process-line quote. **PASS**.
55. HEAD, origin, and the three local commits. **PASS**.
56. v0.2's hash. **PASS**.
57. v0.1's full hash. **PASS**.
58. The 28-entry composition: 5+1+1+1+6+1+2+4+6+1. **PASS**.
59. The routing names only v0.2; the prebuild answers are at dc1ffe1 (aec58440…). **PASS**.
60. No n history. **PASS**.
61. The only PROPOSAL-n entry is RESULTS.md:225 at db97d8e. **PASS**.
62. STOP §5 resolved most of §9. **PASS**.
63. `git diff 24ebeae HEAD` is empty for all nine paths. **PASS**.
64. The clone's commit, tree and clean state; the PDF hash. **PASS**.
65. PROPOSAL-m sha 42ab36ec…6c6b. **PASS**.
66. m:6. **PASS**.
67. m:48. **PASS**.
68. m:52. **PASS**.
69. m:159. **PASS**.
70. m:172, and the groundwork note. **PASS**.
71. m:205. **PASS**.
72. m:251. **PASS**.
73. m:267. **PASS**.
74. m:283. **PASS**.
75. m:318 (inner quotes swapped only). **PASS**.
76. m:345. **PASS**.
77. m:349. **PASS**.
78. A-m1 (16) and §4 step 4. **PASS**.
79. The k:111 quote. **PASS**.
80. **IMPRECISE** (above).
81. k:212–213. **PASS**.
82. k:226. **PASS**.
83. g:164–170, g:165, h:165–167, LOCK-g:167–170. **PASS**.
84. RESULTS.md@18c32df:73. **PASS**.
85. :7329–7334. **PASS**.
86. :7342 (exact). **PASS**.
87. :7436 (exact). **PASS**.
88. a3_axes_dpo.json and a5_budget.json fields: 3c53e5a54fbaa233, 55.4476, 24/24, 0.0825465. **PASS**.
89. The manifest's four entries. **PASS**.
90. olmo_hf.py. **PASS**.
91. gcal.py:39–40 at 9cbacdb (exact). **PASS**.
92. m_sessions.py:491–492 at 9cbacdb. **PASS**.
93. The prebuild raw §1 quotes it (:60–62). **PASS**.
94. Both raws are committed (24ebeae, 9cbacdb). **PASS**.
95. The CLAUDE.md rules and sections. **PASS**.
96. The PDF sha (second copy byte-identical). **PASS**.
97. §1 quote (bk:77). **PASS**.
98. Table 1 and table1_banks: four stages at 32. **PASS**.
99. The four §3.1 quotes. **PASS**.
100. §3.2 and eq. (1). **PASS**.
101. The §3.2.2 heading, "turns associated with S" and m(c_uns(d)). **PASS**.
102. **IMPRECISE** (above).
103. §4.1 (bk:290). **PASS**.
104. §4.2. **PASS**.
105. §4.3 (bk:392, exact). **PASS**.
106. The Fig. 4 caption (bk:356–360). **PASS**.
107. Appendix E, all quotes (bk:1072–1086). **PASS**.
108. No batch size; the 48 is v0.2's own. **PASS**.
109. Table A2 (bk:1090–1098). **PASS**.
110. Appendix A: eight states with (1) and (2), no (3). **PASS**.
111. The clone is clean; the tree. **PASS**.
112. The three README quotes (exact) and §0.4's paraphrase. **PASS**.
113. The table1_banks rows. **PASS**.
114. figure3 panel D values; N = 160; 24 directions (0–23); the label. **PASS**.
115. figure4. **PASS**.
116. figureA8 values. **PASS**.
117. figureA10 values and label. **PASS**.
118. prereg.json values; op_member 0.3. **PASS**.
119. analysis.json members.olmo_32b. **PASS**.
120. The precondition_cache quote (exact). **PASS**.
121. No scale definition in that field. **PASS**.
122. injected_l2 7.647312 on all 160 reads at +1 (and at −1). **PASS**.
123. Fidelity median 0.0312492, max 0.1250014, 573. **PASS** (wording: see 172).
124. Mean scale 11.15 is analysis.json's field. **PASS**.
125. spec.json. **PASS**.
126. The skeletons: 160 records with all 8 fields, 6+6 turns, 79/81, 616.918750 = 616.91875. **PASS**.
127. The transcript's line 66 (U+2212 matches) and its 1273 tokens. **PASS**.
128. strength_ladder files. **PASS**.
129. **IMPRECISE** (above).
130. SDs 0.623307, 0.370276, 0.454627. **PASS**.
131. Slope mean 0.916417, SD 0.446579. **PASS**.
132. Random slopes −0.287970 (dir 12) to +0.364064 (dir 5) on one shared set, floor_b0–b7, 5 each. **PASS**.
133. The minimum at +1, +0.125008, 160/160 positive. **PASS**.
134. 154/160 negative at −1; maximum +0.406249. **PASS**.
135. **IMPRECISE** (above).
136. R = 25.491. **PASS**.
137. **IMPRECISE** (above).
138. 3,184 (arithmetic). **PASS**.
139. 10,544 (arithmetic). **PASS**.
140. The §0.4 row. **PASS**.
141. 385. **PASS**.
142. 0.3053. **PASS**.
143. Ladder 0.122151. **PASS**.
144. 23.875%, 0.03125, 0.125. **PASS**.
145. SD 0.246851, SE 0.019515. **PASS**.
146. N1's gap and locator. **PASS**.
147. **IMPRECISE** (above).
148. Code not released; Route A not sent. **PASS**.
149. The identification is exact. **PASS**.
150. The other candidates miss by 0.5119–10.065. **PASS**.
151. The script in §3 (declaration order cannot be verified). **PASS**.
152. The "mean scale" locator. **PASS**.
153. "As C13 does". **PASS**.
154. 0 of 2,400; max ratio 0.012143. **PASS**.
155. p0 = 0 means a hair trigger. **PASS**.
156. 570 (23.75%). **PASS**.
157. Retention ×0.25 is session-level (it reproduces as 93/240). **PASS**.
158. **IMPRECISE** (above).
159. 3,184 and 10,544; §9 keeps the rounded figures. **PASS**.
160. Planning values. **PASS**.
161. The §7.4 quote (exact). **PASS**.
162. (16)'s quote (exact; the summary omits "committed before any posting"). **PASS**.
163. N3's reading. **PASS**.
164. N4: 9cbacdb as "the prebuild raw's HEAD at its push". **PASS**: the raw was written at 24ebeae, and the files are identical at both commits.
165. 71cc23c built both. **PASS**.
166. The N5 quotes. **PASS**.
167. CC BY 4.0 §3(a)(1)(C), text or URI. **PASS**.
168. The clone's details; the commit dated 2026-10-05T20:43:51+02:00. **PASS**.
169. The PDF's path, sha and PDFKit. **PASS**.
170. 26 copies; the full concatenation hash. **PASS**.
171. The N1 script and its 8 rows (all 16 numbers match). **PASS**.
172. **IMPRECISE** (above).
173. G-DATA not run; no tokenizer. **PASS**.
174. Nothing built; no pod. **PASS**.
175. The pod watch "in its own session": **NOT VERIFIABLE**, not counted. A `podwatch` scratch folder dated 11:19 is consistent with it.

### C. SOURCE.md (S)

176. The citation, arXiv:2609.35591v2. **PASS**.
177. The authors' repository. **PASS**.
178. The commit, tree and committed 2026-10-05. **PASS**.
179. CC BY 4.0. **PASS**.
180. **IMPRECISE** (above).
181. 26 byte-for-byte copies. **PASS**.
182. `shasum -c` checks them. **PASS**.
183. G-DATA (ii) plus LICENSE. **PASS**.
184. The skeleton listing: 8×5 + 6×20 = 160. **PASS**.
185. The CSVs. **PASS**.
186. neutral_passages. **PASS**.
187. strength_ladder. **PASS**.
188. Copied at step 3; G-DATA (ii) re-verifies. **PASS**.
189. Nothing executed. **PASS**.

## 2. Code's dispositions (each re-checked at source before it was applied)

| item | re-check at source | disposition |
|---|---|---|
| 18 | RESULTS.md's 11-05 block: the pod-order line sits among its ADDENDUM-m1 lines | applied: the entry names both |
| 32 | v0.2 §9's [S] list carries arithmetic and `figureA10.csv` figures | applied: the entry states each figure's source |
| 38, 158 | v0.2 §2.1: "at d ∈ {0, +1, −1} every read is re-computed … (and on a 10% keyed sample of the other points"; N4-T and N4-Ts are at d = 0 | applied: N2 now follows §2.1's rule, giving 432 / 3,472 / 10,832, and records the first reading (464 / 3,184 / 10,544) as superseded; in the entry and the raw §2.4 and N2 |
| 43 | the byte counts as the checker gives them | applied: "35 MB, `reduced.json` 28 MB of it" (decimal) |
| 44 | v0.2 G-DATA (ii)'s list has no `LICENSE` | applied: `LICENSE` is named as Code's addition |
| 49 | SOURCE.md's text | applied: the entry quotes SOURCE.md's attribution line verbatim, after item 180's edit |
| 50 (O1) | `git check-ignore -v`: `.gitignore:5:/data/*` | applied: a commented `.gitignore` exception admits `data/n/bk/` alone. A probe file under `data/n/` stays ignored, and the 28 files under `data/n/bk/` are admitted. `.gitignore` joins the commit (N5, the entry). The exception admits the folder, not a list of extensions: its contents are fixed, and `SHA256SUMS` lists them |
| 80 | k:124–129: the 5(f) bullet ends at k:125, and 5(d) opens at k:126 | applied: the raw gives C10's two-part span |
| 102 | bk:226–250: §3.2.1's heading precedes bk:240, and §3.2.2 starts at bk:248 | applied: the quote moves to §3.2.1; m(c_uns(d)) stays under §3.2.2, where Δm_fixed is defined |
| 129 | as the checker states | applied: the raw §2.4 names each row's source |
| 135 | 0.6253/√160 = 0.0494; 0.6233/√160 = 0.0493 | applied: the row states both; the [S] 0.049 holds either way |
| 137 | v0.2:165's list | applied: the row now reads 960; 4,800; 320; 320; 320 + 320; 160; 160 |
| 147 | `strength_ladder/analysis.json`'s first `scale` object: "sd of the choice margin at dose 0 across this cell's sessions; the standardized slopes are the raw slope divided by it" | applied: N1 names the other scale fields and the extended search scope, credited to the checker |
| 172 | 4,640 neutral reads at gen_point 0; 2,400 carry `fidelity_absdiff` | applied at all three places in the raw |
| 180 | BK's `LICENSE` is a notice that links the legal code | applied: SOURCE.md now says so |
| O2 | — | carried to the entry's push line: `creativecommons.org`, in BK's `LICENSE`, is outside N12's `PUBLIC_HOSTS` |
| O3 | Code re-ran it: at ×0.25 / ×0.5 / ×0.75 / ×1.0, 93 / 233 / 240 / 240 of 240 sessions, equal to BK's `retention_relative_x*`; 0.20/`mean_scale_nats` = 0.017931671874052292, equal to `absolute_tolerance_as_fraction_of_scale` | applied: N1 carries it, credited |
| O4 | — | noted. v0.2 quotes the per-session mean 0.916 (§2.5) and figureA8's 0.916730 (its random floor beside it) as different figures, and nothing equates them |
| 175 | — | the pod watch runs in a separate Code session, started from this one at the PI's "New session" |
