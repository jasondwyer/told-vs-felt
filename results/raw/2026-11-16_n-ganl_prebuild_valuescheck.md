# n — G-ANL-n's question block and its entry: the blind values-check, with Code's dispositions

*The n-analyzer session (Code), PI date 2026-11-16. What was checked: the drafts of the block
`results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md` (checked under its draft name, dated 2026-11-15, and renamed
for its commit date) and of its RESULTS.md entry, side by side. Who checked: a blind values-checker subagent, under a
brief that quoted the list of record v2's items 1–5 verbatim and the coordinating session's lines on `data/mf3`; it
read the sources itself (the proposal, PROPOSAL-m, the seat's answers, BK's files under `data/n/bk`, BK's paper, the
draft analyzer) and was not given Code's conclusions. A first run of the check was stopped unfinished when the
coordinating session closed the battery windows for Q-F3's launch; it wrote no report. The run of record started after
"windows open", in a window the coordinating session granted: its Python reruns first, in one burst (nice -n 19, one
process at a time), then reads only. Its report follows verbatim; the local scratch folder is named by description
inside it. Code's dispositions follow the report. Calendar dates only; the commit hash is the record.*

## The checker's report, verbatim

# Values-check — D1 (the G-ANL-n question block) and D2 (its log entry), blind

Checker: a blind values-checker subagent, calendar date 2026-11-16. Scope: every factual claim in
D1 = the author's scratch `n9/block/2026-11-15_n-ganl_code-to-design_prebuild.md` (109 lines) and
D2 = the author's scratch `n9/block/entry.md` (43 lines); placeholders SCHEMA_COMMIT, SCHEMA_SHA, SCHEMA_LINE and
VALUES_LINE skipped. "n:N" = `PROPOSAL-n-bk-reconciliation-v0_2.md` line N at the repository root; "m:N" =
`PROPOSAL-m-gating-campaign-v1_11.md` line N; "D1:N" / "D2:N" = the draft's own line N. Nothing in the repository was
edited, committed, pushed or switched.

## 0. What I ran

- **Python, one burst, first, one process at a time, foreground** (`nice -n 19`, the venv's Python 3.12.9, `-I`), cwd
  the author's scratch folder; outputs in my scratch folder `n9/vc/`:
  (a) `bk_slope_check.py` → `a_bk_slope_check.txt`, exit 0; (b) `grid_check.py` → `b_grid_check.txt`, exit 0;
  (c) `n_analyze.py --selftest` → `c_selftest.txt`, exit 0, **140/140**; (d) my own `vc/vc_dump.py` (read-only: BK's
  three neutral_passages JSON files flattened to TSV, and the draft analyzer's module- and class-level constants
  extracted by `ast` — literals parsed, a few constant expressions such as `C_N2` evaluated in a builtins-restricted
  namespace; the module itself never imported or executed) → `flat_*.tsv`, `tables/`, `const/`, `const_INDEX.tsv`,
  exit 0.
  Then "python done" was sent to main; **no Python process of any kind ran afterwards.**
- After the burst: the Read tool, `shasum`, `/usr/bin/grep`, `awk` (including an independent recomputation,
  `vc/indep.awk`, from the TSV of BK's reads), `git log` / `git show` of committed files, `osascript` (the PDF
  re-extraction with the author's `extract.js`, to `vc/bk_vc.txt`). Departures from that list, disclosed: shell
  builtins (`cd`, `echo`, `printf`, `while read` loops), `head` as a line limiter on grep/git output, and one
  `sort | uniq -c` on a grep of BK's `prereg.json` / `analysis.json` (no hit). Before the burst: `mkdir` of `vc/` and a
  name-only `ls` of the author's scratch folder.
- Nothing under `data/mf3` was listed, read, stat'ed or searched; no `data/*/ckpt` or `data/*/reports` file was read;
  `results/raw/` was never listed or searched as a directory (only named, committed raws were read; one
  `git log --name-only` over `results/raw/*design-to-code*`, committed files only, found the 2026-11-06 answers); no whole-tree
  `git status`; no model process; nothing in the background. (The battery (c), run as instructed, hashes `data/n`'s
  files outside ckpt/reports/verdicts and its hook refuses the `data/mf3` probes before any filesystem call — its own
  line 137.)

## 1. FAIL and IMPRECISE (first), with suggested fixes

**FAIL: none.**

**IMPRECISE (17).** Ordered by weight; the first is substantive.

- **#79 (D1:46, Q6, N2) — "those being the arms its certification reads" is incomplete.** Where d_20 is at +1
  (shapes (b) and (d): the cap binds, or 2·d_eq within 0.05 of 1 — D1's own Q7 illustration, d_eq ≈ 0.725, is shape
  (b)), N2's ceiling at the norm-matched point is max(L(+1), P(+1)), so its certification also reads **N1-P**. The
  draft analyzer does the same: `n2_outcome` takes `ceiling(st.L[m20], st.P.get(m20))` with m20 = +1, but its
  INDETERMINATE causes list only N2-E, N1-V and N1-R (author's `n_analyze.py`, `n2_outcome`, the `causes = …` line and
  the docstring). An incomplete N1-P in shape (b) would leave N2 evaluated with a P(+1) from a partial arm (or none).
  *Fix:* "N2 is also INDETERMINATE when N2-E, N1-V or N1-R is incomplete — and N1-P where d_20 is at +1 (shapes (b),
  (d)), whose P(+1) its certification then reads"; and either add N1-P to the code's causes in those shapes or state
  the shape-(a) scope in the ask.
- **#131 (D2:8–10) — item 10 quoted truncated, with no ellipsis.** The same relayed item, as RESULTS.md records it in
  the 2026-11-16 schema entry (RESULTS.md@`5a97527`:31–35), continues after "from that schema." with two more
  sentences (one session instead if Code judges the coupling too tight; then steps 7–15 as written, drafted locks to
  the seat, [go]). *Fix:* add " …" at the cut, or quote the item in full; if the relay to this session really was
  shorter, say so.
- **#25 (D1:8) — "each marked *pending the seat* in the code and in the battery's lines".** In the code: yes — the
  OPEN register's comment says "each pending the seat" for OPEN-Q1–Q9 (`n_analyze.py`, the comment above `OPEN = {`),
  and docstrings tag Q1 and Q9. In the battery's printed lines: only five of nine — OPEN-Q2, Q5, Q7, Q1, Q9
  (`c_selftest.txt` lines 27, 34, 46, 120, 131); no battery line names Q3, Q4, Q6 or Q8. *Fix:* "each registered in
  the code as OPEN-Q1–Q9, pending the seat (the battery's lines name Q1, Q2, Q5, Q7 and Q9)", or add the tags to the
  battery lines for Q3, Q4, Q6, Q8.
- **#77 (D1:45, Q6 dose item) — numbering differs from the code's register.** D1 carries dose's "points incomplete"
  under Q6; the code registers it under **OPEN-Q5** ("…; dose's 'points incomplete' beside N1's causes"), its battery
  line says "OPEN-Q5, pending the seat" (`c_selftest.txt` line 34), and the code's OPEN-Q6 omits it. A ruling on "Q6"
  would not reach that line. *Fix:* move it to OPEN-Q6 in the code (and the battery line), or write "(registered as
  OPEN-Q5)" in D1's Q6 dose item.
- **#111 (D1:87) — the merge rule as declared omits two parts of the code's rule.** PIN-n-14 and `DoseMap._resolve` /
  `problems()` also fix *a tie goes to the earlier candidate* (+1, +1/2, 0, −1, then +d_20) and *a fold into 0 is
  refused*; the n-build schema entry (RESULTS.md, 2026-11-16) lists both as flagged readings. *Fix:* add "a tie goes to
  the earlier candidate; a fold into 0 is refused".
- **#112 (D1:87) — "The analyzer … refuses a dose map whose recorded merges differ".** The draft re-derives the merges
  (`DoseMap._resolve`, `expected_points`) and refuses inconsistent d_eq / d_20 / ρ, but has no comparison with a
  recorded dose map: its docstring says the reader is "not in this draft". *Fix:* "re-derives the merges from d_eq and
  d_20; the reader, built from the committed schema, will refuse a dose map whose recorded merges differ".
- **#113 (D1:87) — "Code has asked n-build to check the same rule on its side" understates the record.** The analyzer's
  PIN-n-14 says "agreed 2026-11-15", and n-build's committed entry (RESULTS.md, 2026-11-16, `5a97527`) says the rule was
  "Settled with n-analyzer before this commit (by message; each side checks the same rule)". *Fix:* "n-build's schema
  checks the same rule on its side (agreed 2026-11-15; committed at SCHEMA_COMMIT)".
- **#44 (D1:20, Q2) — bold dropped from the n:122 quote, undeclared.** The quote's second fragment, "certified at d iff
  |mean Δm_V(d)| > max(L(d), P(d))", lies inside n:122's bold span `**A signed valenced effect is certified at d iff …
  max(L(d), P(d))**`; D1 prints it plain. Text otherwise exact (grep -F: both fragments on n:122 only). *Fix:* add
  "(bold dropped)" after the quote, as Q4 does for m:278.
- **#31 (D1:14, Q1) — "Figs. A7 and A8 the same".** The quoted sentence is Fig. 4's caption only (PDF p. 9). Figs.
  A7 and A8 — and also A9, A10, A11 and A12 — state it in other words: "an OLS regression of the difference in choice
  margin on the steering dose" (re-extracted text, the captions on PDF pp. 31–36). *Fix:* "(Fig. 4's caption; Figs.
  A7–A12 say the same in other words)".
- **#20 (D1:3) — "the PDF has moved within the PI's local reference folder".** It is no longer at the path n:4 names
  (shasum: no such file) and is in the PI's local reference folder with n:4's sha256 — i.e. it moved *into* that folder
  from the folder above it, not within it. *Fix:* "the PDF has moved into the PI's local reference folder (a subfolder
  of the folder the proposal's header names), its sha256 unchanged".
- **#73 (D1:41, Q5) — "the battery reports separately which tuples can occur on the pinned map".** No map is pinned;
  the draft battery reports reachability on three enumerated shapes, (a), (b), (d) (`c_selftest.txt` lines 109–111;
  `_bt_reachability`). *Fix:* "…which tuples can occur on each merge shape, and so on the pinned map once G-CAL-n pins
  d_eq".
- **#68 (D1:37–38, Q5) — "§2.3's merges remove more: every point distinct: 28 … so 224 tuples".** The first bullet is
  the no-merge case and removes nothing beyond the 160 (224 = 384 − 160); only (b) and (d) remove more. *Fix:* "With
  every point distinct, 28 triples occur, so 224 tuples (the 384 less the 160). §2.3's merges remove more [C, …]:" then
  the two merge bullets.
- **#104, #106 (D1:83–84, §3) — quotes recapitalised.** n:136 reads "exceeds its floor" and "its CI excluding 0"
  (lowercase; grep -F finds the capitalised forms nowhere in the proposal). The code's PINs quote them lowercase.
  *Fix:* "[E]xceeds its floor" / "[I]ts CI excluding 0", or "n:136's "exceeds its floor" is …".
- **#27 (D1:9) — "Each gives the text that leaves it open, the readings, the consequence, and the reading Code carries
  meanwhile."** Q1, Q2, Q3 and Q9 label readings; Q4, Q5, Q7 and Q8 give their alternatives only in the Ask; Q6 states
  no alternative reading and no consequence (only "confirm or rule each"). *Fix:* "Each gives the text that leaves it
  open, the reading Code carries meanwhile, and the alternatives (as readings or in its Ask)", or add an alternative and
  a consequence to Q6.
- **#141 (D2:31–32) — "Four read BK's files under data/n/bk: prereg.json twice, reduced.json's structure once, and one
  stopped at its numpy import before reading".** Internally inconsistent: by its own breakdown three read BK's files
  and one did not. *Fix:* "Four were run against BK's files under data/n/bk: three read them (prereg.json twice,
  reduced.json's structure once), and one stopped at its numpy import before reading". (The facts themselves are
  UNVERIFIABLE, #140.)
- **#146 (D1:3 against D2:30–37) — D1's "What ran" is narrower than D2's declarations.** D1 lists only the in-window
  battery and the two scripts; D2 discloses earlier pre-window Python processes on BK's files and later system-Python
  runs (syntax checks, a span-parser run on the proposal's text). *Fix:* add to D1's header "(earlier Python processes,
  and short system-Python runs, are disclosed in the entry)".

## 2. Every claim

C = CONFIRMED, I = IMPRECISE (§1), U = UNVERIFIABLE. Evidence is a file and line or a command and its output.

### D1 — header (D1:1–3) and §0 (D1:5–10)

| # | where | claim | status | evidence |
|---|---|---|---|---|
| 1 | D1:1 | nine questions | C | Q1–Q9 at D1:14–73 |
| 2 | D1:3 | PI date 2026-11-15 | U | the PI's calendar; see note N1 |
| 3 | D1:3 | n §3 "G-ANL-n", §8 step 9 | C | n:115 (G-ANL-n under §3); n:159 step 9 "G-ANL-n (385 tuples)" |
| 4 | D1:3 | the coordinating session asked for one early block | U | a message between sessions |
| 5 | D1:3 | nothing ran on a model, nothing of record | U | process claim |
| 6 | D1:3 | battery windows granted, nice -n 19, model-free | U | process claim; consistent with the seat's raw §2.3 item 2 ("model-free test batteries at low priority, one at a time") |
| 7 | D1:3 | the schema-independent battery, 140 checks, all passing | C | my run `c_selftest.txt`: "140/140 n_analyze battery checks pass", exit 0; the draft's docstring: "the schema-independent layers only". The author's `run3.txt` differs from my run only on the count line (139/140 before the count fix) |
| 8 | D1:3 | two short scripts read BK's `reduced.json` | C | `bk_slope_check.py` and `grid_check.py` open only `neutral_passages/reduced.json` |
| 9 | D1:3 | PROPOSAL-n v0.2 sha256 `30a3d0f5…04f4` | C | `shasum -a 256` → 30a3d0f55a66…b104f4 (working tree = HEAD blob) |
| 10 | D1:3 | the seat's answers `1f3ce1f9…df84b` | C | shasum → 1f3ce1f9c668…5220df84b; also `git show a215c28:<raw> \| shasum` |
| 11 | D1:3 | committed at `a215c28` | C | `git log --diff-filter=A` on the raw → a215c28, 2026-11-15 |
| 12 | D1:3 | the raw's §2.3, §5, §9 | C | raw lines 31–34, 58–70, 87–94 |
| 13 | D1:3 | the schema is `valence_core/n/schema.py` | C | `git log -1 --name-only 5a97527` lists it (placeholders not checked) |
| 14 | D1:3 | `prereg.json` `c55ab6b9…` | C | shasum → c55ab6b9b9f4… |
| 15 | D1:3 | `analysis.json` `12c35645…` | C | shasum → 12c35645a914… |
| 16 | D1:3 | `reduced.json` `ec5fea59…` | C | shasum → ec5fea59c6ef… |
| 17 | D1:3 | each its `SHA256SUMS` entry | C | `data/n/bk/SHA256SUMS` lines 7–9, identical digests |
| 18 | D1:3 | BK's paper sha256 `e92c69cb…fa49`, unchanged | C | shasum of the PDF in the PI's local reference folder → e92c69cb…5a82fa49 = n:4's value |
| 19 | D1:3 | the PDF has moved since n:4 named it | C | shasum at n:4's path: "No such file or directory" |
| 20 | D1:3 | moved "within" the PI's local reference folder | I | §1 |
| 21 | D1:3 | not opened: checkpoints, reports, verdicts, `data/mf3`, `data/p` | U | process claim (the battery's own hook refusals, `c_selftest.txt` line 137, cover the battery only) |
| 22 | D1:3 | "n:N is PROPOSAL-n v0.2's line N" | C | every n:N in D1/D2 resolves to the cited text (below) |
| 23 | D1:7 | the canonical run writes the artifact and fixes the analyzer sha256 LOCK-n v0.1 binds (n:117) | C | n:117 lists "the analyzer hash"; "canonical run" / "artifact" are the program's G-ANL terms (RESULTS.md: G-ANL-F3, G-ANL-p entries) |
| 24 | D1:7 | LOCK-n v0.1 follows G-ANL-n; both wait | C | n:159 steps 9 → 10 |
| 25 | D1:8 | each reading marked pending the seat in the code and the battery's lines | I | §1 |
| 26 | D1:8 | n-build's steps: the package, G-VEC, G-CAL-n | C | n:159 steps 6–8; the seat's raw §5.1 names n-build for step 6 and n-analyzer for step 9 only, so steps 7–8 (G-VEC, G-CAL-n) fall to n-build by elimination; §5.2 gives the order |
| 27 | D1:9 | each Q gives text, readings, consequence, carried reading | I | §1 |
| 28 | D1:9 | §2 facts, §3 readings, §4 order, Appendix A verbatim | C | D1:75–109; Appendix A verified in #120 |

### D1 — Q1 (D1:14–18)

| # | where | claim | status | evidence |
|---|---|---|---|---|
| 29 | D1:14 | n:126 quote incl. `**the floor for an arm**` | C | `grep -F` of the whole quote: D1 1 hit, proposal n:126 only |
| 30 | D1:14 | BK's sentence, Fig. 4's caption | C | re-extracted text (identical to the author's extraction, sha256 73b71051…4f96 both), PDF p. 9, text lines 362–363 |
| 31 | D1:14 | "Figs. A7 and A8 the same" | I | §1 |
| 32 | D1:14 | `prereg.json` `rules.primary` quote with "…" | C | `grep -F` finds both fragments; the elided text is ", with a session-cluster bootstrap 95% CI." |
| 33 | D1:14 | none of the three says intercept | C | n:126, Fig. 4's caption, `rules.primary`: no intercept wording; `prereg.json` and `analysis.json`: 0 hits for "intercept" |
| 34 | D1:14 | the paper has no intercept or origin wording | C | re-extracted text: "intercept" 0 hits; "origin" only inside "original(ly)" (lines 71, 80, 238, 247, 249, …) |
| 35 | D1:15 | symmetric grid: 0.9164 either way | C | rerun (b): "intercept 0.9164 origin 0.9164"; independent awk 0.916417 (Σx = 0 makes the fits identical) |
| 36 | D1:15 | symmetric floor 0.3641 | C | rerun (b) 0.3641 / 0.3641; awk 0.364064 (direction 5) |
| 37 | D1:15 | on N1-V's points the fits differ | C | battery line 120 (0.8114 vs 0.8444 on an asymmetric grid); #39 |
| 38 | D1:15 | the restricted grid {+1, +1/2, 0, −1}; BK read neither d_eq nor d_20 | C | n:81 N1-V's points ∩ `prereg.json` `dose_points` [−1, −0.5, 0, 0.5, 1] |
| 39 | D1:15 | 0.9114 with an intercept, 0.9329 through the origin | C | rerun (b); awk 0.911438 / 0.932890 over 160 sessions |
| 40 | D1:15 | 24-direction floor 0.3658 against 0.3641 | C | rerun (b); awk 0.365849 / 0.364064 (direction 5 in both) |
| 41 | D1:16 | the fit enters (ii) and every arm's slope | C | n:136 (ii); n:126 "per arm, the OLS slope" |
| 42 | D1:18 | carried: (a) | C | `session_slopes` is OLS with an intercept (docstring "OPEN-Q1 (pending the seat)"); battery line 119 |

### D1 — Q2 (D1:20–23)

| # | where | claim | status | evidence |
|---|---|---|---|---|
| 43 | D1:20 | n:122 quote, first fragment | C | `grep -F`: n:122 only |
| 44 | D1:20 | n:122 quote, second fragment | I | §1 (bold dropped, undeclared) |
| 45 | D1:20 | N1-P reads +1 and −1 only | C | n:89 |
| 46 | D1:20 | dose certifies at d_eq (n:138); N2 at the norm-matched point (n:140), d_20's | C | n:138; n:140; n:81 d_20 = min(1, 2·d_eq) |
| 47 | D1:20 | no P(d) unless the point merges into +1 | C | n:89; the code's `ceiling()` comment |
| 48 | D1:21 | (c) +320 reads, positive doses | C | 160 × 2 points (when both are distinct) |
| 49 | D1:22 | consequence of (a); (b) stricter where P(+1) > L(d) | C | logic of n:122's max(L, P) |
| 50 | D1:23 | carried: (a) | C | `ceiling()`: "L(d) alone"; battery line 27 |

### D1 — Q3 (D1:25–29)

| # | where | claim | status | evidence |
|---|---|---|---|---|
| 51 | D1:25 | n:32 quote with "…", and the paraphrase | C | `grep -F` both fragments at n:32; the elision is "(N4 on Instruct; N3's control on Qwen)" |
| 52 | D1:25 | n:142 quote | C | `grep -F`: n:142 |
| 53 | D1:25 | n:138 quote (bold and italics kept) | C | `grep -F`: n:138 |
| 54 | D1:27 | §5's not-answered sentence | C | `grep -F`: n:138; note N4 (italics → quotation marks) |
| 55 | D1:27 | it would be false in that cell | C | logic: the cell has G-READ-n PASS |
| 56 | D1:27 | 1,920 evaluations of the 384 tuples, 256 in that cell [C] | C | battery line 104 "NOT-DETECTABLE 64 / 320 / 256"; 16 (N1 × N2) × 16 non-PASS N4 evaluations = 256 |
| 57 | D1:27 | the interim text is A.6 | C | D1:106 = constant `C_DOSE_ND_READABLE_N4` |
| 58 | D1:28 | n:136 names only "G-READ-n FAIL at d = +1"; n:140 no label; §0.6 covers any null | C | n:136; n:140; n:32 |
| 59 | D1:29 | carried: (a) for dose, N1, N2 | C | OPEN-Q3; battery line 101 (T7) |

### D1 — Q4 (D1:31–35)

| # | where | claim | status | evidence |
|---|---|---|---|---|
| 60 | D1:31 | n:115 quote | C | `grep -F`: n:115 |
| 61 | D1:32–34 | three more inputs (n:136; span_reward at 0.20; n:142 "with *no read obtained*") | C | n:136; n:121; `grep -F` n:142 |
| 62 | D1:35 | m:278 quote, "bold dropped" declared | C | m:278 "…conditioned on the **0.12-artifact-existence input flag**" |
| 63 | D1:35 | m:278 as the precedent | C | m:278's 1,080 tuples exclude the flag; m:291: "an input of this analyzer as of G-ANL-F0's" |
| 64 | D1:35 | 384 × 4 + 96 × 4 + 1 = 1,921 | C | arithmetic; battery line 105 |
| 65 | D1:35 | the tuple count stays 385 | C | n:115 |

### D1 — Q5 (D1:37–41)

| # | where | claim | status | evidence |
|---|---|---|---|---|
| 66 | D1:37 | n:138 "or the points are incomplete"; dose INDETERMINATE iff N1 (under Q6's reading) | C | `grep -F` n:138; battery line 107 |
| 67 | D1:37 | 160 = 64 + 96 | C | 1 × 2 × 4 × 4 × 2 = 64; 3 × 1 × 4 × 4 × 2 = 96 |
| 68 | D1:37–38 | "merges remove more", first bullet the no-merge case | I | §1 |
| 69 | D1:38 | every point distinct: 28 triples, 224 | C | battery line 109; 28 × 8 = 224 = 384 − 160; hand count 4 + 24 |
| 70 | D1:39 | d_20 at +1: 24 triples, 192; the condition; N2 cannot be NULL | C | battery line 110; hand count (removes N1 ∈ {REP, PART} × 2 doses × NULL = 4); merge tolerance n:81 |
| 71 | D1:40 | d_eq at +1 as well: 17 triples, 136 | C | battery line 111; hand count 24 − 6 − 1 = 17 |
| 72 | D1:41 | total sentence functions, one set per tuple, as n:115 asks | C | n:115 "asserts one §7 sentence set per tuple"; battery line 95 (T1) |
| 73 | D1:41 | reachability "on the pinned map" | I | §1 |
| 74 | D1:41 | m:291 and the seat's A2 of 2026-11-06 (PENDING tuples refused) | C | m:291; `results/raw/2026-11-06_ganl-f3_design-to-code_answers.md` line 14 (A2: "the refusal", 218,855 PENDING tuples), committed 54bbfe5, 2026-11-06 |

### D1 — Q6 (D1:43–48)

| # | where | claim | status | evidence |
|---|---|---|---|---|
| 75 | D1:44 | n:136 names N1-R and N1-P; n:134 quote; carried N1 INDETERMINATE | C | n:136; `grep -F` n:134; `n1_outcome` causes over N1-V, N1-R, N1-P |
| 76 | D1:45 | dose "the points are incomplete" (n:138); carried | C | n:138; `dose_outcome` "incomplete:points" beside N1's cause |
| 77 | D1:45 | (the same item, against the code's register) | I | §1 (registered as OPEN-Q5) |
| 78 | D1:46 | n:140 quote with "…" | C | `grep -F` both fragments at n:140 (elision: "stands") |
| 79 | D1:46 | N2's causes are "the arms its certification reads" | I | §1 (N1-P omitted in shapes (b), (d)) |
| 80 | D1:46 | a pause on N1-V/N1-R leaves N2 evaluable, as written | C | n:140 names only a pause on N2's reads |
| 81 | D1:47 | n:142 quote; carried: a pause on N4's reads → no read obtained | C | `grep -F` n:142; `n4_outcome` via `_causes`; battery lines 53–54 |

### D1 — Q7 (D1:50–55)

| # | where | claim | status | evidence |
|---|---|---|---|---|
| 82 | D1:50 | n:81 quotes (the map; "scaled to f · R_ℓ at f ∈ {0.10, 0.20}") | C | `grep -F`: n:81 both |
| 83 | D1:50 | N1-V's and N1-R's largest norm ρ·R, at d = +1 | C | n:81 ‖ṽ(d)‖ = \|d\|·ρ·R; note N5 |
| 84 | D1:51–53 | if 2·d_eq > 1: N2-E exceeds every N1-V point; d_20 = 1; the ratio is 2·d_eq | C | 0.20·R_ℓ = 2·d_eq·ρ·R |
| 85 | D1:53 | n:140 quote "N1-V's at the norm-matched point" | C | `grep -F`: n:140 |
| 86 | D1:54 | n:81's illustration → d_eq ≈ 0.725, ratio ≈ 1.45 [C] | C | awk: 0.10 × 55.45 / (0.30 × 25.49) = 0.72512, × 2 = 1.45024 (0.72509 / 1.45019 with R = 7.6473 / 0.30) |
| 87 | D1:55 | carried: d_20's point, ratio reported | C | OPEN-Q7; `match_ratio`; battery line 46 |

### D1 — Q8 (D1:57–68)

| # | where | claim | status | evidence |
|---|---|---|---|---|
| 88 | D1:57 | §5 words four cells | C | n:136 (REPLICATED), n:138 (three); battery line 90 |
| 89 | D1:58 | n:136 quote "name the failing conjunct and the figures" | C | `grep -F`: n:136 |
| 90 | D1:59–63 | Appendix A covers PARTIAL, NOT-REPLICATED, every INDETERMINATE and NOT-RUN, N2's four, N4's five, the expansion, Q3's cell | C | A.1–A.8: N2 = A.7 × 3 + A.3; N4 = A.8 × 4 + A.3 |
| 91 | D1:62 | Code adds "the state is" | C | A.5 against n:138's two NOT-DETECTABLE sentences |
| 92 | D1:65 | NOT-DETECTABLE with \|mean\| above the ceiling but a CI incl. 0; n:138's phrase | C | n:138 ("otherwise"); `grep -F` phrase; battery line 31 |
| 93 | D1:66 | DETECTABLE and PARTIAL can carry a negative effect | C | n:122 (\|mean\|); battery lines 28, 30 |
| 94 | D1:67 | a cell not computed takes the not-readable sentence | C | PIN-n-11; `State.gr` |

### D1 — Q9 (D1:70–73)

| # | where | claim | status | evidence |
|---|---|---|---|---|
| 95 | D1:70 | N1-V lists d = 0 (n:81); N2's row f = 0.10, 0.20 only (§2.4) | C | n:81; n:90 |
| 96 | D1:71 | reading (a): {0, d_eq, 2·d_eq}, floor at d_eq's and d_20's points | C | `n2_slope_points`; battery line 131 |
| 97 | D1:72 | no §5 outcome reads it | C | n:140 |

### D1 — §2 (D1:75–79)

| # | where | claim | status | evidence |
|---|---|---|---|---|
| 98 | D1:77 | G-DATA (iii)'s figures: 1.0900 / 0.5072 / −0.3841 / −0.7554; SDs 0.6233 / 0.3703 / 0.4546; slope 0.9164, SD 0.4466; random −0.2880 to +0.3641 [C] | C | battery line 123; rerun (a); awk (1.090039, 0.507178, −0.384083, −0.755373; 0.623307, 0.370276, 0.454627; 0.916417, 0.446579; −0.287970 to 0.364064); `figure3.csv` panel D; G-DATA raw (iii) table (`results/raw/2026-11-06_n-gdata.md` lines 41–53); note N6 |
| 99 | D1:77 | G-DATA (vi): 0 of 2,400 above TAU, 570 above TAU/4, largest 0.012143 [C] | C | battery line 124; awk over the 2,400 reads with a re-computation (ratio = \|cached − fresh\| / max(\|log p(S)\|, \|log p(U)\|)): 0 / 570 / 0.012143; RESULTS.md G-DATA (n) (vi); G-DATA raw lines 192–197 |
| 100 | D1:78 | n:77 quote; secondary (b) has no free text | C | `grep -F` n:77; n:128 (b) |
| 101 | D1:78 | n-build flags it at its BUILD | C | RESULTS.md 2026-11-16 (`5a97527`), reading 7: "The BUILD entry puts this to the seat" |
| 102 | D1:79 | reachability is Q5's; reductions depend on d_eq | C | #66–#71 |

### D1 — §3 (D1:81–91)

| # | where | claim | status | evidence |
|---|---|---|---|---|
| 103 | D1:81 | strikable until LOCK-n v1.0 | C | the code's comment above `PINS`: "each strikable by the seat until LOCK-n v1.0" (Code's declaration) |
| 104 | D1:83 | "Exceeds its floor" | I | §1 |
| 105 | D1:83 | = the signed mean slope above the floor (n:136 (ii)) | C | n:136 (ii); PIN-n-7; `n1_outcome` |
| 106 | D1:84 | "Its CI excluding 0" | I | §1 |
| 107 | D1:84 | wholly on one side; an endpoint at 0 does not exclude | C | PIN-n-8; `Est.excludes0`; battery lines 21–22 |
| 108 | D1:85 | absent / not computed is not PASS | C | PIN-n-11; `State.gr` |
| 109 | D1:86 | n:126 "4,000 resamples, seed in the lock" | C | `grep -F`: n:126 |
| 110 | D1:86 | one matrix per arm, `n-boot\|{arm}`, m:159's function, 4,000 rows, session order, linear percentiles 2.5/97.5 and 1/99 | C | `boot_key`, `boot_index`, `pct_interval`, `PCT95`/`PCT98`; m:159 "`default_rng(crc32(key.encode()) % 2**31)`"; battery lines 113–118 |
| 111 | D1:87 | the merge rule as declared | I | §1 (tie rule and fold-into-0 refusal omitted; the rest matches PIN-n-14) |
| 112 | D1:87 | the analyzer refuses a recorded map whose merges differ | I | §1 |
| 113 | D1:87 | Code "has asked" n-build to check the same rule | I | §1 |
| 114 | D1:88 | (iv) evaluated; A1 "struck beyond d = −1", the routing of 2026-11-06 | C | RESULTS.md, PROPOSAL-n v0.2 COMMITTED entry: the routing quoted ("A1 negative pole: [struck beyond d = −1]") and "3. A1, the negative pole: struck beyond d = −1"; PIN-n-19 |
| 115 | D1:89 | TAU/4 row (n:77, n:128 (f)) and its reading | C | n:77; n:128 (f); PIN-n-16; battery line 130 |
| 116 | D1:90 | label-mass counter below .20 (n:128; n:99; m:283) | C | n:128 counters; n:99; m:283 "low label mass (< .20; …)"; PIN-n-17 |
| 117 | D1:91 | secondary (d) is Pearson's r (n:128 (d)) | C | n:128 (d); PIN-n-18; battery line 128 |

### D1 — §4 and Appendix A (D1:93–109)

| # | where | claim | status | evidence |
|---|---|---|---|---|
| 118 | D1:95 | the order (build on; canonical run and LOCK-n v0.1 after the answers) | C | n:159 steps 9–10 |
| 119 | D1:99 | "theirs 1.09 [1.00, 1.19]" is text; brackets are slots | C | n:136; every bracketed token at D1:99–109 is one of the analyzer's 22 `SLOTS` except "[1.00, 1.19]" (×3) |
| 120 | D1:101–109 | Appendix A verbatim = the analyzer's constants | C | each of the 21 italic spans, extracted with awk, has the sha256 of exactly one constant: `C_N1_PARTIAL`, `C_N1_NOT_REPLICATED`, `C_N1_INDET`, `C_DOSE_INDET`, `C_N2['INDETERMINATE']`, `C_N4['NO-READ']`, `C_NOT_RUN`, `C_DOSE_ND_NOT_READABLE`, `C_DOSE_ND_READABLE_N4`, `C_N2['SPECIFIC'/'SHARED'/'NULL']`, `C_N4['PASS'/'REVERSE'/'DEAD'/'INDETERMINATE']`, `CONJUNCT_TEXT['i'/'iv'/'ci+1'/'ii'/'iii']`; all 21 sentence constants are covered |
| 121 | D1:109 | A.9's conjunct texts | C | (i) = n:136 (i) in substance; note N8 |

### D2

| # | where | claim | status | evidence |
|---|---|---|---|---|
| 122 | D2:1 | dated 2026-11-15 | U | note N1 |
| 123 | D2:1–2 | anchors: §3 "G-ANL-n", §8 step 9; the seat's answers §5.1–§5.2 | C | n:115, n:159; raw lines 60, 62 |
| 124 | D2:2 | the coordinating session's go for one early block | U | message |
| 125 | D2:2–4 | STOP scope; interim readings each marked pending the seat | C | consistent with D1 §0; the code's OPEN register comment |
| 126 | D2:4 | nothing ran on a model, on the box, or of record | U | process claim |
| 127 | D2:6 | the block's file name | C | equals D1's file name; the analyzer's OPEN comment cites the same path |
| 128 | D2:7 | the PI's "Route as given" on the 2026-11-15 (evening) routing | C | a215c28's subject; RESULTS.md 2026-11-16 entry ("section N, item 10") |
| 129 | D2:7–8 | the paste block's header | C | RESULTS.md quotes the identical header (ADDENDUM-p1 entry; the 2026-11-16 entry) |
| 130 | D2:8 | item 10 | C | the raw's §10 item 10 ("n-build and n-analyzer start now (§5.1–§5.2) [go]"); RESULTS.md "section N, item 10" |
| 131 | D2:8–10 | item 10's text | I | §1 (truncated, no ellipsis) |
| 132 | D2:8 | "as the coordinating session relayed it" | U | a relay to this session |
| 133 | D2:10–11 | the raw's sha / commit; sessions and order in §5.1–§5.2 | C | #10, #11; raw lines 60, 62 |
| 134 | D2:11–12 | the go's terms (one committed block, numbered, readings and consequences, what it stops) | U | message (see #27 for the block's structure) |
| 135 | D2:13–15 | what it stops / does not stop (n:117) | C | n:117; agrees with D1:7–8 |
| 136 | D2:16–22 | the nine questions' summary, 0.9114 / 0.9329 [C], "no source says" | C | agrees with D1 §1; #33, #39; `analysis.json` has no intercept wording either |
| 137 | D2:23–24 | facts declared | C | agrees with D1 §2; #98–#101 |
| 138 | D2:25 | declarations to be repeated, as asked | U | message |
| 139 | D2:26–29 | the 2026-11-15 declaration, acknowledged | U | messages; its content matches the draft's docstring (schema-independent layers; the reader from the committed schema) |
| 140 | D2:30–33 | the pre-window processes: four, their files, no model, no checkpoint or `data/mf3`, no campaign running | U | processes before any window |
| 141 | D2:31–32 | "Four read BK's files … one stopped … before reading" | I | §1 |
| 142 | D2:33–35 | the disclosure; three first, then four | U | messages |
| 143 | D2:35–37 | runs since then inside windows, apart from system-Python runs | U | process claims |
| 144 | D2:40 | committed by path; not pushed | U | future |
| 145 | D2:41–43 | the canonical run waits for the answers and G-CAL-n's dose map | C | n:113 (G-CAL-n pins d_eq, d_20); n:159 order |

### Cross-checks

| # | claim | status | evidence |
|---|---|---|---|
| 146 | D1's "What ran" against D2's declarations | I | §1 |
| 147 | D1 and D2 otherwise agree (title, scope, the nine questions, facts, shas, commit, dates) | C | side-by-side read; D2's §5.1–§5.2 and D1's §2.3/§5/§9 are compatible |
| 148 | neither draft names a pod's IP address or port, a local absolute path, a clock time or the user's name | C | `/usr/bin/grep` for absolute-path prefixes, dotted quads, `H:MM`, UTC/GMT, am/pm, "port", "ssh", the user name, pod ids: no hit; the only time-of-day word is "(evening)" inside D2's quoted paste-block header |

## 3. Notes (no status of their own)

- **N1 (dates).** D1 and D2 carry 2026-11-15; the schema commit D1 cites as a source (`5a97527`) carries git date
  2026-11-16, and today's calendar date is 2026-11-16. Under the program's convention (PI-local dates; near-midnight
  differences are not corrected) this is the author's to confirm at commit, not a finding.
- **N2 (Appendix A, the [reason] slot).** A.4's [reason] is filled from seven Code-written texts (`NOT_RUN_CAUSES`, e.g.
  the Clock-date reasons; printed in the battery's NOT-RUN lines) that Appendix A does not show; the seat adopting Q8's
  forms may want them listed beside A.4.
- **N3 (the code, for #79).** `n2_outcome` reads P(+1) in shapes (b)/(d) but lists no N1-P cause; the battery's N2
  INDETERMINATE lines (`c_selftest.txt` 40–43) exercise only N2-E, N1-V and N1-R.
- **N4 (italics).** D1:27 quotes n:138's whole italic sentence in quotation marks without the asterisks; acceptable
  for a whole-span quote, but if the "bold dropped" convention is meant to cover emphasis generally, add "(italics
  dropped)".
- **N5.** #83: the same largest norm is reached at d = −1.
- **N6.** RESULTS.md's G-DATA (n) entry prints three Panel D means; the G-DATA raw's (iii) table carries −0.3841 in
  parentheses, and `figure3.csv` has all four. D1's four values are each correct.
- **N7 (placeholders, out of scope).** `valence_core/n/schema.py` exists at `5a97527` with sha256 `77c12d6d…94bc`
  (git show | shasum), for the author's fill.
- **N8.** A.9's (iv) says "its 95% CI" where n:136 (iv) says "its CI"; n:126 makes it 95%; Code's wording, not a quote.
- **Reruns.** My battery output equals the author's `run3.txt` except the count line (139/140 → 140/140). Reruns (a)
  and (b) match every [C] figure D1 prints, and the independent awk recomputation from BK's raw reads matches them to
  the printed precision.

## 4. Summary

148 claims checked across D1 and D2: 115 CONFIRMED, 17 IMPRECISE, 0 FAIL, 16 UNVERIFIABLE (processes before any window,
messages between sessions, the PI's calendar date, and D2's future commit). Every [C] figure reproduces from my own
reruns and, independently, from BK's raw reads by awk (0.9164 / 0.3641; 0.9114 / 0.9329; floors 0.3658 / 0.3641;
Panel D means and SDs; 0 / 570 / 0.012143 on 2,400 fidelity reads); every sha256 prefix, commit and anchor resolves;
all 21 Appendix A sentence forms equal the draft analyzer's constants byte for byte; the battery passes 140/140; neither
draft names an IP address, port, local absolute path, clock time or the user's name. The one substantive IMPRECISE is
Q6's N2 cause list, which omits N1-P where d_20 sits at +1 (shapes (b)/(d)), as the draft code does too. The rest are
wording: D2's item 10 quote is truncated without an ellipsis; the battery's lines tag only five of the nine OPEN-Qs and
the code files dose's "points incomplete" under OPEN-Q5, not Q6; §3's merge-rule text omits the tie and fold-into-0
rules, states the reader's future refusal as present, and understates the settled agreement with n-build; an
undeclared bold drop (n:122); two recapitalised quotes; "Figs. A7 and A8 the same"; the PDF moved "within" its folder;
reachability "on the pinned map"; Q5's "remove more" framing; Q6's missing alternatives; D2's "Four read …" count; and
D1's narrower "What ran".

## Code's dispositions

Every IMPRECISE item is applied; no item is disputed. The edits after the check were verified by tool (each changed
string asserted present, each replaced string asserted absent), not re-checked blind.

- **#79 (substantive), applied in the block and in the draft code.** The block's Q6 now reads, for N2: "Carried: N2 is
  also INDETERMINATE when N2-E, N1-V or N1-R is incomplete, and N1-P where d_20 sits at +1 (the cap binds, or 2·d_eq
  within 0.05 of 1), whose P(+1) the ceiling then takes: the arms its certification reads." In the draft analyzer,
  `n2_outcome` adds N1-P to its causes where the norm-matched point is one N1-P reads (+1 or −1); `gleak_table` no
  longer certifies on a partial N1-P where P enters the ceiling; a new battery line checks shape (b) with N1-P
  incomplete (N2 INDETERMINATE by incomplete:N1-P) against shape (a) (N2 evaluated).
- **#131, applied:** the entry quotes item 10 in full.
- **#25, applied:** the draft's battery now tags OPEN-Q3 (the tuple pass's label assertion), OPEN-Q4 (the outcome
  space's count), OPEN-Q6 (each INDETERMINATE cause §5 does not name) and OPEN-Q8 (the sentence-form checks), beside
  the Q1, Q2, Q5, Q7 and Q9 tags; the block says the questions are "registered in the code as OPEN-Q1 to OPEN-Q9 and
  tagged *pending the seat* in the battery's lines that test it".
- **#77, applied in the code:** dose's "points incomplete" moves to OPEN-Q6 (the register, the code's comment and the
  battery line), as the block files it.
- **#111, #112, #113, applied in §3:** the merge rule now states the candidate order, the tie to the earlier candidate
  and the refused fold into 0; the refusal of a differing dose map is the reader's (built from the committed schema,
  present in the draft since the schema landed); n-build's side is stated as settled ("agreed 2026-11-15; committed
  at `5a97527`"), with the merge's reach to N1-R cited as n-build's block's Q3.
- **#44, applied:** "(the second fragment's bold dropped)".
- **#31, applied:** "(Fig. 4's caption; Figs. A7–A12 say the same in other words)".
- **#20, applied:** "the PDF now sits in a reference subfolder of the folder the proposal's header names, its sha256
  unchanged".
- **#73, applied:** "on each merge shape, and so on the pinned map once G-CAL-n pins d_eq".
- **#68, applied:** the no-merge count is stated first, as the 384 less the 160; only the two merge shapes are "remove
  more"; a line adds that these counts assume n-build's form of the merge (its block's Q3).
- **#104, #106, applied:** §3 quotes n:136's "exceeds its floor" and "its CI excluding 0" in their own case.
- **#27, applied:** §0 now says each question gives "the text that leaves it open, the reading Code carries meanwhile,
  its consequence, and the alternatives, as readings or in its ask"; Q6 now gives readings (a) and (b) and the
  consequence of (b).
- **#141, applied:** the entry reads "Four were run against BK's files under `data/n/bk`: three read them (…), and
  one stopped at its numpy import before reading".
- **#146, applied:** the block's header adds "Earlier Python processes, and short system-Python runs, are disclosed in
  the entry."
- **Notes.** N1: the block and entry are dated 2026-11-16, the commit date, and the block's file is renamed. N2:
  Appendix A.4 now lists the seven [reason] texts, each asserted by tool to equal the draft analyzer's
  `NOT_RUN_CAUSES`. N3: applied with #79. N4: Q3's quote of n:138's italic span now says "italics dropped". N5: Q7
  now says the largest norm is reached "at d = ±1". N6: no change (the block's four Panel D values are each correct, as
  the note says). N7: the schema reference is filled (`5a97527`, `77c12d6d…94bc`, re-hashed by Code). N8: no change
  (A.9's wording is Code's form, under Q8).
- **Changes beside the findings,** made after the check: the block cites n-build's block of the same date
  (`results/raw/2026-11-16_n-schema_code-to-design_questions.md`) for its Q2 (secondary (b)), Q3 (the merge's reach
  to N1-R) and Q5 (G-READ-n's capture layer, new to §2 as a fact for the analyzer's inputs); the header's battery  figure is the draft's latest run, 154 checks, all passing (the checker's run, before the reader was merged, passed 140 of 140).
