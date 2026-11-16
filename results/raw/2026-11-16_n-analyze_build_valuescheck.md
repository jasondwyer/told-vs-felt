# n_analyze.py BUILD: the blind values-check, two passes (PI date 2026-11-16)

Code's raw for the entry `n package — scripts/n_analyze.py, BUILD`. Two blind values-checkers, each a subagent of
this session under a brief quoting the list of record v2's items 1–5 and allowing no Python, checked the entry, the
review raw and the selftest raw against their sources, claim by claim. The first pass checked the first drafts; the
second, the drafts revised after the first, and then whether each of the first pass's dispositions was carried. Each
report is reproduced whole (its headings demoted two levels), and each is followed by Code's dispositions. The
checkers write SCRATCH for Code's scratch folder and REPO for the repository.

## 1. The first pass: the checker's report, whole

### Blind values-check: the n_analyze.py BUILD drafts (PI date 2026-11-16)

Checker: a blind values-checker subagent. Read only; no Python of any kind; nothing under `data/mf3` touched; no file
under any `data/*/ckpt` or `data/*/reports`; git status only scoped to named paths. SCRATCH is the author's scratch
folder for this build, REPO the repository. Line numbers `l.N` are REPO/scripts/n_analyze.py's unless named.

**Drafts checked (sha256 of the bytes read):**
- SCRATCH/block/build_entry.md: `671d7308ad4a8ad054aa6238fe498759bd5439f533db94b189b42fd8f25f4ad6` (its "Values-check" line skipped)
- SCRATCH/block/2026-11-16_n-analyze_build_review.md: `0084e842924b662930921aaa4cc66b6b74078a547c83ccaa3208d93ffc6a268b`
- SCRATCH/block/2026-11-16_n-analyze_build_selftest.txt: `205244eec3f584bcd4d7dd65497d19bba948dddcf27c6f1b150c104696b5062f`

**How.** Every hash by `shasum -a 256` of the file named (the schema and the proposal also through `git show <commit>:<path>`).
The selftest raw against SCRATCH/runs/record.out by `diff` (raw lines 2–174 against record.out with the repository root
replaced by `<repo>`). Every table row of the review raw rebuilt from the TSVs and outputs and searched for as exact
text. Round-2 `.old` occurrences by `/usr/bin/grep -o -F -f` (every `.old` is one line without a newline). The §6 diff
by `diff` of the round-2 base against REPO/scripts/n_analyze.py. Code claims read in REPO/scripts/n_analyze.py.
Quotations against the committed files at HEAD (each clean by scoped `git status --porcelain`). Messages between
sessions, the PI's words as relayed and window grants are not on file: UNVERIFIABLE unless a file records them.

---

#### 1. The entry (SCRATCH/block/build_entry.md)

| # | Claim | Status | Evidence / correction |
|---|---|---|---|
| E1 | Date 2026-11-16 | CONFIRMED | The raws' PI date; the related commits (5a97527, 8e3bf91, 18102d0) are dated 2026-11-16. |
| E2 | Entry name "n package — `scripts/n_analyze.py`, BUILD" | CONFIRMED | The review raw names the same entry. |
| E3 | PROPOSAL-n v0.2 §3 "G-ANL-n", §8 step 9 | CONFIRMED | n:115 "**G-ANL-n.**" under §3; §8 "9. G-ANL-n (385 tuples)". |
| E4 | The seat's answers of 2026-11-15, §5.1–§5.2 | CONFIRMED | results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md (sha256 `1f3ce1f9…df84b`, committed at a215c28): §5.1 "Sessions", §5.2 "Order and gates". |
| E5 | N-pod's analyzer and its battery, 171/171 | CONFIRMED | `UNIT = "N-pod"`; record.out "171/171". |
| E6 | "reviewed blind and mutation-tested in two rounds" | IMPRECISE | The blind review is round 1 only; round 2's fifty mutants are Code's own (the review raw: "Code wrote fifty mutants"), which the entry's Round 2 bullet does not say. See corrections. |
| E7 | Without the `verdicts` command, which waits for n-build's stage-report and G-READ-n forms | CONFIRMED | main() (l.3254) has `--selftest`, `ganl`, `not-run` only; the module docstring says verdicts "is added when their forms are committed (n-build's package)". |
| E8 | Without G-ANL-n's canonical run, which waits for the seat's answers and G-CAL-n's dose map | CONFIRMED | The block's §0 ("What this block stops"); `ganl_precheck` refuses a canonical run without `--dose-map` ('canonical-no-map'). |
| E9 | Model-free: nothing ran on a model or on the box; no stage ran | UNVERIFIABLE | Session acts. Consistent: every battery output on file passes "no model library is imported by the battery". |
| E10 | sha256 `468308…e2a0` | CONFIRMED | REPO/scripts/n_analyze.py (= SCRATCH/tree/scripts/n_analyze.py). |
| E11 | Schema at `5a97527`, `valence_core/n/schema.py`, sha256 `77c12d6d…94bc` | CONFIRMED | `git show 5a97527:valence_core/n/schema.py` hashes to it; the working-tree file equals it and is clean. |
| E12 | Which it pins and refuses otherwise | CONFIRMED | `SCHEMA_SHA256` l.1848; `schema_module` (l.1866) refuses other bytes, and an import from another file (l.1876). |
| E13 | Binds PROPOSAL-n v0.2 by sha256 `30a3d0f5…04f4` | CONFIRMED | `PROPOSAL_SHA256` l.55 = the file's hash (committed at 5916097); `load_campaign` refuses another `proposal_sha256`; battery STR-PROPOSAL-SHA. |
| E14 | Commands `--selftest`; `ganl [--out DIR] [--dose-map FILE]`; `not-run --record FILE [--out DIR]` | CONFIRMED | main()'s parser. |
| E15 | Battery run "from this path" | CONFIRMED | record.out: `INVOCATION: … scripts/n_analyze.py --selftest`. |
| E16 | Run "once" | UNVERIFIABLE | One output of record on file; other runs cannot be excluded from files. |
| E17 | 171/171 checks | CONFIRMED | record.out: 171 [PASS], 0 [FAIL], last line 171/171. |
| E18 | Every one of the 172 coverage ids reached | CONFIRMED | record.out's coverage line; `_REQ` (l.861–896) counts 172. |
| E19 | Exit 0 | CONFIRMED | Inferred: main returns 0 iff `battery()["ok"]` (l.3269): all pass, count = EXPECTED_CHECKS 171, coverage complete; all hold in the output. The exit status itself is not recorded. |
| E20 | The selftest raw's name | CONFIRMED | Matches the draft raw. |
| E21 | Reads cell files through the schema's own checks and the cross-record checks the schema leaves to the analyzer | CONFIRMED | `load_campaign` (sm.check_cell, sm.cell_filename, sm.read_plan) and `_cross_checks`; schema at 5a97527, l.97–101: "CROSS-RECORD PROPERTIES are not checked here … The analyzer re-checks what it uses." |
| E22 | §4's statistics: Δm against the shadow, session bootstrap, per-session slopes and floor, L(d), P(d) | CONFIRMED | `delta_m` (l.2046), `boot_index`/`mean_est`, `session_slopes`/`slope_est`, `floor_V`, `L`, `P` in `build_state`. |
| E23 | §5's outcomes in order (NOT-RUN by cause, N1, dose, N2, N4), G-LEAK-n's certification and G-READ-n's states as inputs | CONFIRMED | `outcomes()` l.479, `not_run_reason`; the module docstring says the same (G-LEAK-n's certification is computed in the analyzer by `ceiling`/`above`; G-READ-n's states come in as an artifact). |
| E24 | One §7 sentence set per tuple from §5's four verbatim sentences and Code's 31 forms | CONFIRMED | `VERBATIM`'s four T_ sentences (l.496–504); `code_forms()` = 8 + C_N2 4 + C_N4 5 + CONJUNCT_TEXT 5 + NOT_RUN_CAUSES 7 + ROUTE_TEXT 2 = 31; raw check T1. |
| E25 | Counters (rule 23) and secondaries | CONFIRMED | `counters` l.2321, `secondaries` l.2353; section 13's header "(rule 23 …)". |
| E26 | 385 tuples (1,921 evaluations) | CONFIRMED | Raw l.111. |
| E27 | Oracle reads §5's verbatim cells from the proposal file | CONFIRMED | Raw l.102 (T2); section 8's header. |
| E28 | Code's forms pinned by digest | CONFIRMED | `CODE_FORMS_SHA256` l.2245; raw l.100. |
| E29 | Reachability per merge shape | CONFIRMED | Raw l.115–117 (shapes a, b, d); `pinned_map_reach`. |
| E30 | The review raw's name | CONFIRMED | Matches the draft raw. |
| E31 | Round 1 on the draft frozen at `4db3a206…ed46` | CONFIRMED | SCRATCH/review/n_analyze.under-review.py. |
| E32 | A subagent of this session, under a brief quoting the list of record v2's items 1–5 | UNVERIFIABLE | The brief as sent is a message. SCRATCH/brief_rules.md quotes items 1–5, each line identical to the committed list (results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md, fc43249). |
| E33 | Findings F1–F15 and notes N1–N15 | CONFIRMED | SCRATCH/review/findings.md. |
| E34 | Forty mutants | CONFIRMED | SCRATCH/review/mutants/mutants.tsv, 40 rows. |
| E35 | Two MAJOR: a crash on a non-finite or absent shadow; N2's pauses read from N2-E only | CONFIRMED | Findings F1, F2. |
| E36 | 159/159 unmutated | CONFIRMED | out1/BASE.out (invokes the frozen copy). |
| E37 | 12 killed, 28 survived | CONFIRMED | out1/all.summary. |
| E38 | Each as the reviewer predicted | CONFIRMED | The 12 marked "no" are the 12 killed; the 27 "yes" and one "yes (likely)" (M10) are the 28 survivors. |
| E39 | §3 disposes of every finding and note | CONFIRMED | §3: 30 rows, F1–F15 then N1–N15. |
| E40 | "fixed, registered as a reading, or (N12) kept with its reason" | IMPRECISE | N2 is also partly kept: `lock_names` (never called), `kept_label`, `gleak_table`, `gread_table` (battery-only) stay for the `verdicts` command (§3's N2 row). |
| E41 | Fifty mutants against the fixed draft `fc479b81…f5f` | CONFIRMED | mutants2/mutants.tsv R01–R50 (+R07b); the round-2 base hashes to `fc479b81…3ef5f`; each Rnn.py is the base with one line changed. |
| E42 | The fixed draft 171/171 | CONFIRMED | Inferred: no unmutated run of these bytes is on file under their hash; runs/sel2.out (the scratch draft, 171/171) has a body identical to record.out's, and out2/R07.out (the base with one line no check reads) is 171/171. |
| E43 | "Each round-1 defect is re-expressed on the new code" | IMPRECISE | True of round 1's 28 survivors (R01–R03, R05–R29) and of M05 (R04; killed in round 1); not of the other eleven killed round-1 mutants. |
| E44 | New mutants target the fixes | CONFIRMED | R30–R50 named for F1, F2, F3, F5, F15, PIN-n-20, PIN-n-21, N4, N7, N13, N14, N15 and others. |
| E45 | 49 killed | CONFIRMED | out2/all.summary. |
| E46 | "R07 survived as an equivalent mutant" | IMPRECISE | R07 exchanges N2's per-f figures `fig["n"]` and `fig["sd0"]` between the two f labels; no output moves only because nothing in this BUILD reads them (see R68). |
| E47 | Re-targeted as R07b, killed | CONFIRMED | out2/R07b.out, rc 1. |
| E48 | Appendix A: 28 of 28 equal | CONFIRMED | SCRATCH/runs/appx1.out. |
| E49 | Three places (the raw's §6) | CONFIRMED | Three diff hunks. |
| E50 | Root from `__file__` instead of an absolute path; two docstrings changed | CONFIRMED | The diff. |
| E51 | No code path changed | CONFIRMED | The one executable change (REPO, l.49) yields the same root for scripts/n_analyze.py; no branch changes. |
| E52 | The block is `8e3bf91` | CONFIRMED | Commit exists; it commits the block. |
| E53 | "Each is carried pending the seat, like Q1–Q9's" | IMPRECISE | PIN-n-20–22 and PIN-n-12 sit in `PINS`, "Code's readings, declared (each strikable by the seat until LOCK-n v1.0)" (l.1628), which the block's §3 calls "Not questions"; only `OPEN` entries are "each pending the seat" (l.1657). |
| E54 | PIN-n-20: non-finite read → arm not usable (`nonfinite:<arm>`); steered arm needs every session's shadow present and finite (`shadow:<arm>`) | CONFIRMED | PINS l.1646; `Campaign.usable`; `shadows_ok` in `build_state`; `_causes`. |
| E55 | "An arm the TAU/4 row empties is `tau4-emptied` in that row" | IMPRECISE | The cause is `tau4-emptied:<arm>` (PIN-n-20's text; `_causes` renders reason + ":" + arm), for an arm emptied at a point. |
| E56 | PIN-n-21 | CONFIRMED | PINS l.1650; `not_run_reason` refuses a Clock cause dated ≤ D_N. |
| E57 | PIN-n-22 | CONFIRMED | PINS l.1652; `secondaries` uses FLOOR_EVENTS = 20 for (a), (c), (d). |
| E58 | PIN-n-12, amended (TAU/4 row, own count) | CONFIRMED | PINS l.1633. |
| E59 | OPEN-Q6: "a pause on N1-V's or N1-R's reads alone leaves N2 evaluated" | IMPRECISE | The code also leaves N2 evaluated under a pause on N1-P where d_20 sits at +1: `n2_outcome` counts pauses on N2-E/S/C only (l.440–442), and OPEN-Q6 (l.1669) says "a pause on those N1 arms alone", those arms including N1-P there. |
| E60 | Their incompleteness remains a cause | CONFIRMED | `n2_outcome`'s non-pause causes over N2-E, N1-V, N1-R (and N1-P at +1). |
| E61 | OPEN-Q8: three forms, quoted | CONFIRMED | `ROUTE_TEXT` l.2217 and `VALUE_MERGED` l.2220, verbatim; appx1.out lists exactly these three as absent from Appendix A. |
| E62 | The seat's answers to the block are not in yet | CONFIRMED | No commit of answers to 8e3bf91 since it; item 9 puts them at the seat's next sitting. |
| E63 | "The PI's routing of 2026-11-16, section N, item 9" | CONFIRMED | §8 "Routing block for the PI", "N. n", item 9 of results/raw/2026-11-16_p-verdicts-decisions_design-to-code_answers.md (committed at 18102d0, "Route as given"). |
| E64 | The quotation of item 9 | FAIL | The committed item reads "… the build proceeds on Code's interim readings **as its entries have it** [noted]." The quote drops "as its entries have it" without a mark (and the commit ids' backticks). The relay's own words are not on file. |
| E65 | `verdicts` built after n-build's forms, in an entry of its own | UNVERIFIABLE | Plan; consistent with the module docstring. |
| E66 | Its rules "as n-build's schema v4.1 sets them", agreed with n-build (four rules) | UNVERIFIABLE | Messages; no schema v4.1 is committed. Agrees with SCRATCH/PLAN.md ("verdicts command: report semantics"). |
| E67 | `data/n/gates/G-ANL-n.json` | CONFIRMED | `GANL_REL` l.2864. |
| E68 | It waits for the seat's answers and G-CAL-n's pinned dose map | CONFIRMED | As E8. |
| E69 | Refuses any `valence_core/n/schema.py` but the bytes at 5a97527 | CONFIRMED | `schema_module` (reading path and battery; `not-run` loads no schema). |
| E70 | n-build's next schema commit, waiting on its blind pass, will change that file | UNVERIFIABLE | n-build's state; agrees with PLAN.md. |
| E71 | The analyzer then refuses until its pin moves | CONFIRMED | Follows from E69 (the rest is plan). |
| E72 | "Apart from the departures below, every Python run in this BUILD was inside a battery window the coordinating session granted" | FAIL | Contradicted by the committed entry of 8e3bf91 (RESULTS.md, "n — G-ANL-n: nine questions…", "Declarations, by date"): on 2026-11-15, "before any window existed", short Python processes (four against BK's files under data/n/bk, and interpreter checks); and short system-Python runs outside windows before Q-F3's launch ("edits and syntax checks of Code's scratch files, and one run of the span parser"). That entry says its declarations are "to be repeated in the G-ANL-n entry". |
| E73 | Windows: one process at a time, nice -n 19, foreground, temp folders outside the repository | UNVERIFIABLE | Grants are messages; consistent with SCRATCH/review/run_mutants.sh (sequential loop, `nice -n 19`, outputs in SCRATCH). |
| E74 | The three windows since the review and their runs | UNVERIFIABLE | Grants are messages; the outputs match one for one: out1 (BASE + 40), runs/sel1.out (168/171, before the two pins), runs/sel2.out, runs/appx1.out, out2 (51), runs/record.out. |
| E75 | The two system-interpreter starts and what they did | UNVERIFIABLE | Agrees with PLAN.md "Departures to declare"; the command parts quoted name no model marker. |
| E76 | The coordinating session called the second harmless and asked both declared | UNVERIFIABLE | Message. |
| E77 | One process beyond a window's wording: the baseline, declared at release | UNVERIFIABLE | Message; out1/BASE.out exists. |
| E78 | Committed by path; not pushed | UNVERIFIABLE | Future. |
| E79 | Next | UNVERIFIABLE | Plan. |

#### 2. The review raw (SCRATCH/block/2026-11-16_n-analyze_build_review.md)

| # | Claim | Status | Evidence / correction |
|---|---|---|---|
| R1 | Title; PI date 2026-11-16 | CONFIRMED | |
| R2 | Code's raw for the entry `n package — scripts/n_analyze.py, BUILD` | CONFIRMED | The entry's name. |
| R3 | Draft at `4db3a206…ed46` | CONFIRMED | |
| R4 | "frozen as a copy before the review" | UNVERIFIABLE | Timing; the copy exists with that hash (also SCRATCH/n_analyze.round1-base.py). |
| R5 | Subagent; brief quoting items 1–5 | UNVERIFIABLE | As E32. |
| R6 | F1–F15, N1–N15 | CONFIRMED | |
| R7 | Forty mutants M01–M40 written against the frozen copy | CONFIRMED | Every `.old` is one line, found once in the frozen copy; the line refs match it (M01 l.125, M02 l.145, M12 l.281, M26 l.543, M28 l.97, M39 l.2571, M40 l.747 of that copy). |
| R8 | One unmutated baseline of the frozen copy, 159/159 | CONFIRMED | out1/BASE.out. |
| R9 | 12 killed, 28 survived, as predicted ("no" ×12; "yes" or once "yes (likely)" ×28) | CONFIRMED | |
| R10 | "Code fixed the draft for every finding and note (§3)" | IMPRECISE | §3 itself keeps N12 ("Kept") and part of N2, and registers N3 (PIN-n-22). |
| R11 | Fixed draft `fc479b81…f5f` | CONFIRMED | (3-character tail: see observations.) |
| R12 | "(the scratch copy, before the move to `scripts/`, which changes one line)" | IMPRECISE | The committed file differs from `fc479b81` in three hunks (§6): the move changes the REPO line; the two docstrings were edited separately (the scratch draft now, `806f25c1…`, has them and still the absolute path). |
| R13 | Passes its battery 171/171 | CONFIRMED | As E42 (inferred). |
| R14 | Code wrote fifty mutants R01–R50 against the fixed draft and ran them | CONFIRMED | Counts and base; authorship not on file. |
| R15 | "Each round-1 defect is re-expressed on the new code" | IMPRECISE | As E43. |
| R16 | 49 of the fifty killed | CONFIRMED | |
| R17 | "R07 survived: it is equivalent in the fixed code" | IMPRECISE | As E46; see R68. |
| R18 | Re-targeted as R07b, killed (50 of 51 runs) | CONFIRMED | |
| R19 | Appendix A 28 of 28 equal | CONFIRMED | |
| R20 | Committed bytes differ only in the repository line and two docstrings | CONFIRMED | |
| R21 | "Every run here was inside a battery window the coordinating session granted …" | IMPRECISE | The entry declares this raw's baseline run "beyond a window's wording". The windows themselves are messages. |
| R22 | Nothing ran on a model or on the box | UNVERIFIABLE | Session acts. |
| R23 | Each mutant an exact, unique replacement (`.old` → `.new`, asserted once) on a fresh copy of its base | CONFIRMED | run_mutants.sh l.11–15 (`cp`, perl count must be 1, else APPLY-FAIL; none in any summary); every Mnn.py / Rnn.py is its base plus its one change. |
| R24 | Battery with `--selftest`; "killed" = non-zero exit | CONFIRMED | run_mutants.sh l.18, l.21. |
| R25 | §1's text | CONFIRMED | Lines 25–75 equal findings.md lines 6–56 exactly, its `##` headings shown as `###`. |
| R26 | "as returned" | IMPRECISE | The only record of the hand-back is Code's save, findings.md, whose header says the text is the reviewer's "unedited in substance"; §1 also changes its heading levels. |
| R27 | "`BASE rc=0`, 159/159" | CONFIRMED | 159/159 from BASE.out; rc 0 inferred from the frozen copy's exit rule (its l.2683). No summary or output carries a "BASE rc=0" line (observations). |
| R28 | Two parts, M01–M20 and M21–M40 | CONFIRMED | out1/part1, part2.summary; all.summary is their concatenation. |
| R29 | "The reviewer's columns are as written in its `mutants.tsv`" | FAIL | Four "expected killer" cells are cut at 120 characters mid-word, unmarked: M01 ("…or a CI v"), M04 ("…failing list move"), M10 ("…reads Est.l"), M19 ("…the separately "). The TSV cells are 124, 133, 124 and 142 characters (full texts in the corrections). The other 36 rows are exact; the cut is already in SCRATCH/review/round1_table.md. |
| R30 | Rows otherwise (id, function, what it breaks, suspected survivor), in order M01–M40 | CONFIRMED | Each row rebuilt from the TSV and found once. |
| R31 | The result column | CONFIRMED | 12 killed cells: `fails=` equals each Mnn.out's [FAIL] count and all.summary; the first failing check (coverage and count lines excluded), cut at 90 characters; the 28 "SURVIVED" are rc 0, each output 159/159. |
| R32 | F1 fixed: shadows present and finite or `shadow:<arm>`; `_cross_checks` refuses an absent shadow | CONFIRMED | `build_state` (`shadows_ok`, `unusable`); `_cross_checks` "is not on disk" refusal; RD-SHADOW, RD-REFUSE. |
| R33 | F2: a pause on N2-S's or N2-C's reads makes N2 INDETERMINATE | CONFIRMED | `n2_outcome` l.441 (pauses on N2_ARMS). |
| R34 | F2's quotation (§5, "a pause on N2's reads") | FAIL | Not in the proposal (0 occurrences). n:140 reads "INDETERMINATE iff an unadjudicated pause stands on N2's reads". |
| R35 | F2: "a pause on N1-V's or N1-R's alone does not" | IMPRECISE | As E59 (N1-P where d_20 sits at +1 too). |
| R36 | F3 | CONFIRMED | `value_text` l.2223; RD-MERGED-DEQ (raw l.149). |
| R37 | F4 (PIN-n-21) | CONFIRMED | `not_run_reason`. |
| R38 | F5 | CONFIRMED | `dose_map_input_problems` (keys exactly five; each a finite float, so ints and bools refused); `ganl_precheck`'s named refusals; the battery's 18 cases. |
| R39 | F6 | CONFIRMED | Each statistic draws `boot_index(arm, len(…))`; no "if drop is None else" remains (round 1's l.1998 had identical branches); PIN-n-12 amended. |
| R40 | F7 (PIN-n-20) | CONFIRMED | `Campaign.usable`, `_causes`. |
| R41 | F8: N1-P's signed estimates, N2's slopes and floor "computed and reported" | IMPRECISE | Computed into `build_state`'s figures (`fig["P_signed"]`, `["slopes_N2"]`, `["floors_N2"]`); no output of this BUILD writes them (the `verdicts` command will). |
| R42 | F9 | CONFIRMED | `code_forms`, `CODE_FORMS_SHA256`; SENT-CODE-FORMS in `_bt_sentences`. |
| R43 | F10 | CONFIRMED | Raw l.139, l.143, l.149 (RD-MERGED-DEQ asserts DETECTABLE). |
| R44 | F11 | CONFIRMED | `asym_ok`'s keys (round-2 base l.2665–2681); raw l.148. |
| R45 | F12 | CONFIRMED | Raw l.152. |
| R46 | F13 | CONFIRMED | Each outcome function computes its ceiling once, decides with `above`, and returns that ceiling. |
| R47 | F14 | CONFIRMED | `counters` (TAU/4 apart from TAU, identity bound, `label_mass_below`); `tau4_drop`; a shadow's exceedance drops its session in `build_state`'s `dm`; `tau4_keep` absent. |
| R48 | F15 | CONFIRMED | Raw l.132, l.156, l.158, l.162. |
| R49 | N1 | CONFIRMED | OPEN's comment (l.1657) cites the committed block. |
| R50 | N2 | CONFIRMED | `lock_names` never called; `kept_label`, `gleak_table`, `gread_table` battery-only; `n2_slope_points` in `build_state`; `tau4_keep` absent; `label_mass_below` in `counters`; `Campaign.nonfinite` read in `usable`. |
| R51 | N3 (PIN-n-22) | CONFIRMED | |
| R52 | N4 | CONFIRMED | `_norm`; `_Hook` (file=/path= keywords; args=/cwd= and a repository base for processes; os.open and subprocess.run covered); the nine probes all name absent paths; data/mf3 through `/usr/bin/true` and `hook.check`. |
| R53 | N5 | CONFIRMED | `_bt_snapshot` prunes by `_barred`. |
| R54 | N6 | CONFIRMED | l.1876. |
| R55 | N7 | CONFIRMED | `fill`: l.2256 (route), l.2276 (no AUC). |
| R56 | N8 | CONFIRMED | `emptied()` marks `tau4-emptied`; NaN slopes route to it. |
| R57 | N9 | CONFIRMED | `GATE_STAGES` l.101 = §3's seven pre-lock gates (G-DATA, G-ACQ, G-VEC, G-CAL-n, G-ANL-n, G-TIME-n, G-VER). |
| R58 | N10 "Fixed: the reach helpers the canonical path calls are renamed out of the `_bt` prefix" | FAIL | The renaming holds; the fix does not: `map_reach` still builds its states with the battery helper `_bt_state` (l.1361), and canonical `ganl` reaches it (`run_ganl` → `ganl_artifact` l.2991 → `pinned_map_reach` l.2975 → `map_reach`). The file's own rule (l.857): "Selftest-only helpers carry the `_bt` prefix." In round 1, `pinned_map_reach` called `_bt_reach`, which called `_bt_state`; only the outer name changed. |
| R59 | N11 | CONFIRMED | The battery's ganl cases call `ganl_precheck` only; `run_ganl` appears in the battery only in a comment. |
| R60 | N12 kept; house form; committed file derives REPO from `__file__` | CONFIRMED | l.3256; m_analyze.py l.11269 and p_analyze.py l.696 print the same; l.49. |
| R61 | N13 | CONFIRMED | `not_run_precheck` l.3237. |
| R62 | N14 | CONFIRMED | `write_once` (`os.link` l.2884). |
| R63 | N15 | CONFIRMED | `load_campaign`: hash of the bytes parsed (l.1967); capture bytes against `capture_sha256` (l.1957). |
| R64 | Every check id named in §3 and §4 | CONFIRMED | Each is in `_REQ`. |
| R65 | §4: base `fc479b81…f5f` (171/171), three parts R01–R17, R18–R34, R35–R50 with R07b | CONFIRMED | out2/part1–3.summary; all.summary their concatenation. |
| R66 | "R07 is equivalent" | IMPRECISE | As E46. |
| R67 | The loop pairs each f label with its own reads (`tgt[f]` from `fv[f]`) | CONFIRMED | l.2175–2176. |
| R68 | "swapping the labels there renames only `fig["n"]`'s keys, whose two counts are equal" | FAIL | The loop also sets `fig["sd0"][(arm, lab)] = sd0(_vec(fv[f]))` (l.2178): R07 exchanges the two SDs between "f0.10" and "f0.20", which differ in general; in the TAU/4 row (`drop` set) the two counts need not be equal either (`dm` drops reads per label). Nothing in this BUILD reads `fig["n"]` or `fig["sd0"]` (the battery reads only `fig11["floor_dir"]`, `["P_signed"]`, `["slopes_N2"]`, l.2669–2676), which is why no output moves; the battery has no check of N2's per-f counts or SDs. |
| R69 | R07b on the comprehension mapping each label to its reads; killed | CONFIRMED | R07b.old is l.2171's comprehension; out2/R07b.out. |
| R70 | Table: id, what it breaks, expected killer | CONFIRMED | All 51 rows equal mutants2/mutants.tsv. |
| R71 | Table: results | CONFIRMED | 50 killed cells match Rnn.out (first failing check, coverage and count lines excluded, cut at 80 characters); R07 SURVIVED (rc 0, 171/171). |
| R72 | Each round-2 `.old` occurs once in the round-2 base | CONFIRMED | 51 one-line `.old` files, one occurrence each; every `.new` differs. |
| R73 | The tool "imported the fixed draft" | UNVERIFIABLE | appx1.out records no invocation; the 31 forms are byte-identical in every candidate (fc479b81, the scratch draft, the committed file), so the result stands for each. |
| R74 | It read the committed block | CONFIRMED | The tree, scratch and 8e3bf91 copies are one blob (`2cd1acdf…ed03`). |
| R75 | It compared each italic span with the form of that name in `code_forms()` | CONFIRMED | SCRATCH/tools/appendix_check.py. |
| R76 | Its output, whole | CONFIRMED | Lines 228–257 equal appx1.out (30 lines). |
| R77 | "The three forms the code adds since the block" | IMPRECISE | `ROUTE_TEXT`'s two fills were already in the draft at the block's time (SCRATCH/n_analyze.pre-ganl.py, EXPECTED_CHECKS 154 as the block reports, has `ROUTE_TEXT`; so does the frozen round-1 copy); only `VALUE_MERGED` is new since (F3). The entry's "three forms the block did not list" is right. |
| R78 | They go to the seat with the BUILD entry, under OPEN-Q8 | CONFIRMED | The entry's OPEN-Q8 bullet. |
| R79 | §6 is the whole diff | CONFIRMED | `diff` of the round-2 base and REPO/scripts/n_analyze.py equals §6's block, the one path shown as `<repo>`; SCRATCH/tree/diff_vs_round2_base.txt likewise. |
| R80 | The old line's path shown as `<repo>` | CONFIRMED | The base's l.48 holds the repository path exactly once; no other line of it holds a local path. |
| R81 | No code path changed; two docstrings say what the code does | CONFIRMED | The not-run usage text matches `not_run_precheck` and main (0 written or identical, 2 refused); State's docstring names `build_state`. |

#### 3. The selftest raw (SCRATCH/block/2026-11-16_n-analyze_build_selftest.txt)

| # | Claim | Status | Evidence / correction |
|---|---|---|---|
| S1 | The battery of record, `scripts/n_analyze.py --selftest` | CONFIRMED | Its INVOCATION line. |
| S2 | sha256 `468308…e2a0` | CONFIRMED | The tree file's hash; the output itself records no hash. |
| S3 | Run from the repository root | CONFIRMED | The relative `scripts/n_analyze.py` in INVOCATION. |
| S4 | At nice -n 19 in a battery window the coordinating session granted | UNVERIFIABLE | Not recorded in the output; grants are messages. |
| S5 | PI date 2026-11-16 | CONFIRMED | |
| S6 | 171/171 | CONFIRMED | 171 [PASS], 0 [FAIL]. |
| S7 | Exit 0 | CONFIRMED | As E19 (inferred). |
| S8 | The repository root shown as `<repo>` | CONFIRMED | record.out holds the path once (INVOCATION); the raw shows it as `<repo>`. |
| S9 | The output its header says | CONFIRMED | Raw lines 2–174 are byte-identical to SCRATCH/runs/record.out with the repository root replaced by `<repo>` (`diff` empty, 173 lines). |

#### 4. Across the three drafts

| # | Claim | Status | Evidence |
|---|---|---|---|
| X1 | No local path or user name beyond the `<repo>` form | CONFIRMED | `/usr/bin/grep -i` for the user name, home and temp roots, the scratchpad and session folder, `~/`, `.claude`: no match in any of the three. |
| X2 | Calendar dates only; no clock time or end stamp | CONFIRMED | No time pattern; dates 2026-11-15, 2026-11-16, and D_n 2026-12-15 in battery lines. |

---

#### Totals

| Draft | CONFIRMED | IMPRECISE | FAIL | UNVERIFIABLE | Claims |
|---|---|---|---|---|---|
| Entry | 57 | 7 | 2 | 13 | 79 |
| Review raw | 63 | 10 | 4 | 4 | 81 |
| Selftest raw | 8 | 0 | 0 | 1 | 9 |
| Across | 2 | 0 | 0 | 0 | 2 |
| **All** | **130** | **17** | **6** | **18** | **171** |

#### FAILs and IMPRECISE items, in order of importance, with corrections

1. **FAIL R68 (with IMPRECISE E46, R17, R66): R07's equivalence argument is wrong.** The loop R07 edits sets `fig["n"]` and `fig["sd0"]` (l.2175–2178); the swap exchanges both between the f labels, and the SDs differ in general (the counts too, in the TAU/4 row). No output moves only because nothing in this BUILD reads either. Correction for §4: "**R07 survives, and only because nothing in this BUILD reads what it moves:** in the fixed draft the loop it edits computes each estimate from its own reads (`tgt[f]` from `fv[f]`), so swapping the labels there exchanges only `fig["n"]`'s and `fig["sd0"]`'s entries for the two f labels — N2's per-f counts and SDs, which no output of this BUILD writes and no check reads. Its defect was re-targeted as R07b …". In the top bullet, the entry and §4's first sentence, replace "equivalent" by that reason. The finding under it: the battery has no check of N2's per-f counts or SDs; once `verdicts` reports them, R07 is a live survivor unless a check is added.
2. **FAIL E72: the windows declaration.** The committed entry of 8e3bf91 records Python runs of this build outside windows (2026-11-15 before any window; system-Python runs before Q-F3's launch). Correction: "Since the block (8e3bf91), apart from the departures below, every Python run in this BUILD was inside a battery window …; the processes before it are declared in 8e3bf91's entry ('Declarations, by date')" — or repeat those declarations here, as that entry says they are "to be repeated in the G-ANL-n entry" (if this BUILD entry is meant to be it).
3. **FAIL R58: N10 is not fully fixed.** Correction: "Partly fixed: the reach helpers the canonical path calls are renamed out of the `_bt` prefix (`map_reach`, `map_reach_by_hand`); `map_reach` still builds its states with `_bt_state` (l.1361), so canonical `ganl` still calls one `_bt` helper" — or move or rename `_bt_state` in the code (the author's call; a code change needs its own battery run).
4. **FAIL E64: the item-9 quotation.** Quote the committed item verbatim: "The seat's answers on `718c48e`, `8e3bf91` and `e5aba51` come at its next sitting; the build proceeds on Code's interim readings as its entries have it [noted]." (results/raw/2026-11-16_p-verdicts-decisions_design-to-code_answers.md, §8, "N. n", item 9; committed at 18102d0.)
5. **FAIL R29: four reviewer cells cut under "as written".** Restore them in full (or mark the cut "…" and say the column is cut at 120 characters):
   - M01: "none: NUM-BOOT-DETERMINISM checks repeat-equality, cross-arm difference and range only; no check pins a matrix or a CI value / yes"
   - M04: "none: every synthetic random direction has the same tiny slope; RD-NULL's tuple is unchanged (only its failing list moves, unchecked) / yes"
   - M10: "none expected: RD-PARTIAL's terminal INDETERMINATE holds at 95% (CI about [-0.02, +0.52], by hand); no check reads Est.level / yes (likely)"
   - M19: "none: P(+1) = 0.04 < L = 0.05 in every literal state and the synthetic P is below L; BND-P-ABSENT checks the separately computed "ceiling" key / yes"
6. **FAIL R34: §5 misquoted in F2's disposition.** Correction: (§5, n:140: "an unadjudicated pause stands on N2's reads").
7. **IMPRECISE E53: the new PINs described as pending the seat.** Correction: "PIN-n-20 to -22 and PIN-n-12's amendment are Code's readings, declared as the block's §3 readings are (strikable by the seat until LOCK-n v1.0); the additions to OPEN-Q6 and OPEN-Q8 are carried pending the seat, like Q1–Q9's:".
8. **IMPRECISE E59, R35: N1-P left out of the OPEN-Q6 addition** (the same kind of omission the block's values-check called substantive for Q6). Correction: "a pause on N1-V's or N1-R's reads, or on N1-P's where d_20 sits at +1, alone leaves N2 evaluated".
9. **IMPRECISE R21: the raw's windows sentence against the entry's own declaration.** Correction: "Every run here was inside a battery window the coordinating session granted (the frozen copy's unmutated baseline beyond its window's wording, declared when that window was released): …".
10. **IMPRECISE E40, R10: the dispositions' summary.** Entry: "fixed, registered as a reading, or kept with its reason (N12; and, under N2, `lock_names`, `kept_label`, `gleak_table` and `gread_table`, kept for the `verdicts` command)". Raw: "Code disposed of every finding and note (§3): fixed, registered as a reading (N3), or kept with its reason (N12's `sys.executable`; N2's helpers for the `verdicts` command)."
11. **IMPRECISE R77:** "The three forms in the code that Appendix A does not list go to the seat …: the two fills of §5's route slot (in the draft at the block's time, unlisted there), and VALUE_MERGED (new since, F3)."
12. **IMPRECISE E43, R15:** "Each of round 1's 28 surviving mutants is re-expressed on the new code (R01–R03, R05–R29; R04 re-expresses M05, which round 1 killed), and new mutants target the fixes."
13. **IMPRECISE R12:** "(the scratch copy as mutation-tested; the committed file differs from it in the repository line, which the move to `scripts/` changes, and in two docstrings: §6)".
14. **IMPRECISE E55:** "An arm the TAU/4 row empties at a point is not usable in that row (cause `tau4-emptied:<arm>`)."
15. **IMPRECISE R41 (F8):** "computed and returned with `build_state`'s figures (the `verdicts` command, not in this BUILD, reports them)".
16. **IMPRECISE E6:** "reviewed blind (round 1) and mutation-tested in two rounds"; and in Round 2, "Code's fifty mutants ran against the fixed draft …".
17. **IMPRECISE R26:** "(§1, as saved from the reviewer's hand-back, unedited in substance)", and the same in §1's heading.

#### Observations (no status)

- `fc479b81…f5f` carries a 3-character tail where every other abbreviation in the drafts carries 4 (`…ef5f`); correct as written.
- The "…" after M40's and R45's result cells ("NOT-RUN record refused (PREMATURE) no exception…") marks a cut that did not occur: that check text ends there.
- No output on file records a run's exit status or the sha256 of the bytes it ran. The exits (BASE, the fixed draft, the run of record) and the run of record's bytes are inferred from the battery's exit rule, the runner and the files' present hashes. `BASE rc=0` in code type reads like a recorded summary line; none exists.
- 8e3bf91's entry asks for its 2026-11-15 declarations (the schema-independent layers drafted before the schema commit, and the early processes) to be "repeated in the G-ANL-n entry". SCRATCH/PLAN.md §0b places them in "the G-ANL-n entry". If that is this BUILD entry, they are absent (item 2 above).
- The round-2 "Expected killer" column is a prediction, and the table does not claim it was met. Spot-checks (13 mutants) find the expected check among the failing ones; R31 fails through the reader group's AnlStop.

#### This checker's own departures

- Beyond the brief's tool list, I used `cut` once (to shorten a git-log subject line), `tr` once (to join a name-only `ls` listing), `join` and `sort` once (to pair the round-1 TSV's labels with the summary), `basename` in loops, shell `echo`/`printf`/tests, `diff -q`, and `sed` without `-n` in some pipelines (printing only, never in place).
- I wrote two temporary files into SCRATCH/vc (the selftest raw's body, and record.out with the root scrubbed) for one `diff`, then removed both with `rm`; every later comparison used process substitution. Apart from that and this report, nothing was written.
- No Python, no model process, nothing in the background. Nothing under `data/mf3`, `data/*/ckpt` or `data/*/reports` listed, read or stat'ed. Git: status scoped to named paths only; one `git grep` with `':!data/**'`; `git log`/`show`/`rev-parse` of commits and committed files. One recursive `/usr/bin/grep` over SCRATCH (outside the repository).

## 2. Code's dispositions of the first pass (every FAIL and IMPRECISE item)

| Item | Status | Disposition |
|---|---|---|
| R68 (with E46, R17, R66) | FAIL | Accepted. R07 was not equivalent: the loop it edits also sets `fig["sd0"]`, so the swap exchanges N2's per-f SDs (and, in the TAU/4 row, possibly the counts), which no check read. Code change: the asymmetric campaign's N2-E now has different spreads at f = 0.10 and f = 0.20, and RD-ASYM checks N2's per-f n and SD (ddof 0) against a hand computation. Round 2 re-ran on the amended draft (the review raw's §4); the entry and the raw no longer call R07 equivalent. |
| E72 | FAIL | Accepted. The windows sentence is scoped to the time since the block (`8e3bf91`), and the processes before it are cited to that entry's "Declarations, by date", which asks that they be repeated in G-ANL-n's entry. |
| R58 | FAIL | Accepted, fixed in the code rather than the text: `_bt_state` is renamed `literal_state`, so the canonical `ganl` path calls no `_bt` helper; N10's disposition says so. |
| E64 | FAIL | Accepted. The item is quoted verbatim from the committed raw, with its file and commit (`18102d0`). |
| R29 | FAIL | Accepted. The round-1 table is rebuilt with the reviewer's cells whole (M01, M04, M10 and M19 were cut at 120 characters); a result cell is now cut only where the check's text is longer than 90 bytes, and only then marked "…" (90 bytes, not characters: the second pass's item 8, §4). |
| R34 | FAIL | Accepted. F2's disposition quotes n:140 verbatim; the two battery lines that paraphrased §5 as if quoting it now quote it ("an unadjudicated pause stands on N2's reads"). |
| E53 | IMPRECISE | Accepted: the PINs are Code's readings, strikable by the seat until LOCK-n v1.0; only the OPEN additions are pending the seat. |
| E59, R35 | IMPRECISE | Accepted: the OPEN-Q6 addition names N1-P where d_20 sits at +1, as the code's OPEN text and `n2_outcome` have it; the battery case now covers it (shape b, N1-P paused). The second pass found this reading already in the block's Q6, so it is no addition (§4, item 1). |
| R21 | IMPRECISE | Accepted: the raw's windows sentence names the baseline's departure. |
| E40, R10 | IMPRECISE | Accepted: the summaries name what is kept (N12; N2's helpers for the `verdicts` command) and what is registered (N3). |
| R77 | IMPRECISE | Accepted: the route fills were in the draft at the block's time and unlisted in Appendix A; VALUE_MERGED is new (F3). |
| E43, R15 | IMPRECISE | Accepted: round 2 re-expresses round 1's 28 survivors (R01–R03, R05–R29) and M05 (R04), and adds new mutants on the fixes (R30–R50). |
| R12 | IMPRECISE | Superseded: after the re-run, the committed file differs from the mutation-tested draft in the repository line and, after the second pass, in OPEN-Q6's register text (§6 of the review raw; this raw's §4, item 1). |
| E55 | IMPRECISE | Accepted: the cause is `tau4-emptied:<arm>`, for an arm emptied at a point. |
| R41 | IMPRECISE | Accepted: F8's figures are computed and returned with `build_state`'s figures; the `verdicts` command reports them. |
| E6 | IMPRECISE | Accepted: only round 1 is blind; round 2's mutants are Code's. |
| R26 | IMPRECISE | Accepted: §1 is "as saved from the reviewer's hand-back, unedited in substance", in the head and in §1's heading. |
| Observations | — | The `fc479b81…` abbreviation now carries four characters (`…ef5f`); the "…" mark appears only on cut cells; "BASE rc=0" is replaced by the exit as the runner printed it to the session, beside the output file's 159/159. |
| The checker's departures | — | Noted: tools beyond the brief's list (`cut`, `tr`, `join`, `sort`, `basename`, `diff -q`, `sed` without `-n`, all printing only), and two temporary files written to and removed from Code's scratch. No Python, nothing under `data/mf3` or any `ckpt` or `reports`. |

## 3. The second pass: the checker's report, whole

### Blind values-check, second pass: the n_analyze.py BUILD drafts (PI date 2026-11-16)

Checker: a blind values-checker subagent. Read only: no Python of any kind, no interpreter running a script, nothing
started in the background. Nothing under `data/` was listed, read, stat'ed or searched (so nothing under `data/mf3`, any
`ckpt` or any `reports`), and no `git status` was run. SCRATCH is the author's scratch folder for this build (its `n9`
folder), REPO the repository. `l.N` is a line of REPO/scripts/n_analyze.py unless another file is named.

**Drafts checked (sha256 of the bytes read):**
- SCRATCH/block/build_entry.md: `4148260eb0b3aae1a8e94185c95372c5ba7b693c925d3eb559d08741346e9dc9` (its "Values-check" line skipped)
- SCRATCH/block/2026-11-16_n-analyze_build_review.md: `cfc72ee4e1b87a8012139395b888ded9c659f6654ee01071de7a968754de06a6`
- SCRATCH/block/2026-11-16_n-analyze_build_selftest.txt: `603359e08b143c1b3fd5e71e4a9eafbdde77d0f44cc724236620f21c38fa5140`

**How.** Hashes by `shasum -a 256` of the file named; the schema at `5a97527` also by `git show 5a97527:… | shasum`.
The selftest raw's lines 2–174 against SCRATCH/runs/record2.out by `diff` (repository root replaced by `<repo>`), through
process substitution. The review raw's tables rebuilt in `awk` from the TSVs and from the first non-coverage, non-count
`[FAIL]` line of each `.out`, then compared row by row with `diff`. Every mutant's `.old` counted in its base by an
`awk` whole-file `index` loop (non-overlapping, as the runner's perl count); every `out1/out2/out3` `*.py` compared
with its base plus its one replacement. The §6 diff by `diff` of SCRATCH/review/n_analyze.round2b-base.py and
REPO/scripts/n_analyze.py. Code claims read in REPO/scripts/n_analyze.py; quotations against the committed files.
Messages between sessions, the PI's words as relayed and window grants are not on file: UNVERIFIABLE unless a file
records them (SCRATCH/PLAN.md is the author's notes and counts as no record).

---

### Part 1 — Blind pass

#### 1. The entry (SCRATCH/block/build_entry.md)

| # | Claim | Status | Evidence / correction |
|---|---|---|---|
| E1 | Date 2026-11-16 | CONFIRMED | Session date; 5a97527, 8e3bf91, 18102d0 are dated 2026-11-16. |
| E2 | Entry name "n package — `scripts/n_analyze.py`, BUILD" | CONFIRMED | The review raw's line 3 names the same entry. |
| E3 | PROPOSAL-n v0.2 §3 "G-ANL-n", §8 step 9 | CONFIRMED | Proposal line 115 "**G-ANL-n.**" under §3; line 159 "9. G-ANL-n (385 tuples)". |
| E4 | The seat's answers of 2026-11-15, §5.1–§5.2 | CONFIRMED | results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md (sha256 `1f3ce1f9…df84b`, a215c28): §5.1 "Sessions" (n-analyzer: step 9's `n_analyze.py`), §5.2 "Order and gates". |
| E5 | N-pod's analyzer and its battery, 171/171 | CONFIRMED | `UNIT = "N-pod"`; record2.out "171/171". |
| E6 | Reviewed blind (round 1), mutation-tested in two rounds | CONFIRMED | findings.md (round 1); out1, out2/out3. |
| E7 | Without `verdicts`, which waits for n-build's stage-report and G-READ-n forms | CONFIRMED | `main()` (l.3266–3297) has `--selftest`, `ganl`, `not-run` only; module docstring: verdicts "is added when their forms are committed (n-build's package)". |
| E8 | Without G-ANL-n's canonical run, which waits for the seat's answers and G-CAL-n's dose map | CONFIRMED | The block's §0; `ganl_precheck` refuses a canonical run without `--dose-map` ("canonical-no-map"). |
| E9 | Model-free: nothing on a model or the box; no stage ran | UNVERIFIABLE | Session acts. Consistent: every battery output on file passes STR-NO-HEAVY. |
| E10 | sha256 `67f35ecbd86afa7a295d067e94402da6df1aeae0a90a88e56256a709896382db` | CONFIRMED | REPO/scripts/n_analyze.py (= SCRATCH/tree/scripts/n_analyze.py). |
| E11 | Schema at `5a97527`, `valence_core/n/schema.py`, sha256 `77c12d6d…94bc` | CONFIRMED | `git show 5a97527:valence_core/n/schema.py` hashes to `77c12d6d…73494bc`; the working-tree blob equals 5a97527's and HEAD's. |
| E12 | Which it pins and refuses otherwise | CONFIRMED | `SCHEMA_SHA256` l.1853; `schema_module` (l.1871) refuses other bytes, and an import from another file. (Scope: see E62.) |
| E13 | Binds PROPOSAL-n v0.2 by sha256 `30a3d0f5…04f4` | CONFIRMED | `PROPOSAL_SHA256` = the file's hash; `load_campaign` refuses another `proposal_sha256`; STR-PROPOSAL-SHA. |
| E14 | Commands `--selftest`; `ganl [--out DIR] [--dose-map FILE]`; `not-run --record FILE [--out DIR]` | CONFIRMED | `main()`'s parser (metavars are the entry's). |
| E15 | "Its battery, run once from this path" | IMPRECISE | Two battery runs from `scripts/` are on file: record.out (the "first run of record from `scripts/`", of the pre-values-check bytes) and record2.out (these bytes). Correction: "Its battery on these bytes, run once from this path (the first run of record from `scripts/` was of the pre-values-check bytes)". |
| E16 | 171/171 checks | CONFIRMED | record2.out: 171 `[PASS]`, 0 `[FAIL]`. |
| E17 | Every one of the 172 coverage ids reached | CONFIRMED | record2.out's coverage line (count from `len(REQUIRED_COVERAGE)`). |
| E18 | Exit 0 | CONFIRMED | Inferred: `main` returns 0 iff `battery()["ok"]` (all pass, count = EXPECTED_CHECKS 171, coverage complete), which record2.out shows. The exit itself is on no file. |
| E19 | The selftest raw's name | CONFIRMED | Matches the draft. |
| E20 | Reads cell files through the schema's own checks and the cross-record checks the schema leaves to the analyzer | CONFIRMED | `load_campaign` (`sm.check_cell`, `sm.cell_filename`, `sm.read_plan`), `_cross_checks` (l.2002). |
| E21 | §4's statistics: Δm against the shadow, session bootstrap, per-session slopes and floor, L(d), P(d) | CONFIRMED | `delta_m` (margin minus `N1-V|none|0` shadow), `boot_index`/`mean_est`, `slope_est`/`session_slopes`, `floor_V`, `L`, `P` in `build_state`. |
| E22 | "From them it gives §5's outcomes in order: the unit's NOT-RUN by cause, then N1, dose, N2 and N4" | IMPRECISE | N1, dose, N2, N4 come from the statistics (`outcomes`); the NOT-RUN by cause comes from a NOT-RUN record (`not-run`, `not_run_reason`), not from them. Correction: "It gives §5's outcomes in order: the unit's NOT-RUN by cause (from a NOT-RUN record), then, from the statistics, N1, dose, N2 and N4, with …". |
| E23 | One §7 sentence set per tuple from §5's four verbatim sentences and Code's 31 forms | CONFIRMED | `VERBATIM`'s four T_ sentences; `code_forms()` = 8 + C_N2 4 + C_N4 5 + CONJUNCT_TEXT 5 + NOT_RUN_CAUSES 7 + ROUTE_TEXT 2 = 31. |
| E24 | Counters (rule 23) and secondaries | CONFIRMED | `counters`, `secondaries` (section 13). |
| E25 | 385 tuples (1,921 evaluations) | CONFIRMED | Selftest raw line 111. |
| E26 | Oracle reads §5's verbatim cells from the proposal file | CONFIRMED | Selftest raw line 102 (T2); `battery()` reads the proposal and passes its spans to `_bt_tuples`. |
| E27 | Code's forms pinned by digest | CONFIRMED | `CODE_FORMS_SHA256` l.2250; selftest raw line 100. |
| E28 | Reachability per merge shape | CONFIRMED | Selftest raw lines 115–117 (shapes a, b, d). |
| E29 | The review raw's name | CONFIRMED | Matches the draft. |
| E30 | Round 1 on the draft frozen at `4db3a206…ed46` | CONFIRMED | SCRATCH/review/n_analyze.under-review.py (also SCRATCH/n_analyze.round1-base.py). |
| E31 | A subagent of this session, under a brief quoting the list of record v2's items 1–5 | UNVERIFIABLE | The brief is a message. SCRATCH/brief_rules.md quotes items 1–5; nothing records it as the reviewer's brief. |
| E32 | Findings F1–F15 and notes N1–N15 | CONFIRMED | SCRATCH/review/findings.md. |
| E33 | Forty mutants | CONFIRMED | SCRATCH/review/mutants/mutants.tsv, 40 rows; M01–M40 `.old`/`.new`. |
| E34 | Two MAJOR: a crash on a non-finite or absent shadow; N2's pauses read from N2-E only | CONFIRMED | findings.md F1, F2 under "MAJOR". |
| E35 | 159/159 unmutated | CONFIRMED | out1/BASE.out (invokes the frozen copy). |
| E36 | 12 killed, 28 survived | CONFIRMED | out1/all.summary. |
| E37 | Each as the reviewer predicted | CONFIRMED | The 12 TSV rows marked "no" are exactly the 12 killed; 27 "yes" + 1 "yes (likely)" (M10) are the 28 survivors. |
| E38 | §3 disposes of every finding and note | CONFIRMED | §3: 30 rows, F1–F15 and N1–N15, four columns each. |
| E39 | Fixed, registered, or kept (N12; under N2 `lock_names`, `kept_label`, `gleak_table`, `gread_table`, kept for `verdicts`) | CONFIRMED | §3's N12 and N2 rows; in the code `lock_names` (l.1914) is never called, the other three are used by the battery only. |
| E40 | Fifty mutants: R01–R03, R05–R29 re-express round 1's 28 survivors; R04 re-expresses M05 (killed in round 1); R30–R50 new on the fixes | CONFIRMED | mutants2/mutants.tsv: R01–R29 name M01, M03, M04, M05, M06–M10, M12, M14, M15, M19, M21, M23, M26–M39; the 28 survivors of out1 are exactly those minus M05. |
| E41 | First run on the fixed draft (`fc479b81…ef5f`) killed 50 of its 51 runs | CONFIRMED | out2/all.summary; every out2 `*.py` equals SCRATCH/review/n_analyze.round2-base.py (`fc479b81…f3ef5f`) plus its one replacement. |
| E42 | R07 survived | CONFIRMED | out2: R07 rc=0, fails=0. |
| E43 | "because no check read N2's per-f counts and SDs, which it moves" | IMPRECISE | No check read the per-f SDs; but a check did read an N2 per-f count: RD-SENSITIVITY's "TAU/4 row drops 40 + 40 + run 2" asserts `fig_s["n"][("N2-E", "f0.10")] == 159` (fixed draft l.2755–2757; committed l.2767–2769). In that campaign both f lose only run 2, so the counts are equal and the swap is invisible. Correction: "because no check could see it: no check read N2's per-f SDs, which it exchanges, and the one per-f count a check read (RD-SENSITIVITY's N2-E at f = 0.10, 159) is the same at both f there". |
| E44 | With that check added, all 51 runs on the amended draft (`cc0fa5b1…3ea8`, 171/171) were killed | CONFIRMED | out3/all.summary (51 killed); every out3 `*.py` = round2b-base + its replacement; sel3.out 171/171; out3/R07.out fails on "N2's per-f n and SD (ddof 0)". |
| E45 | Appendix A: 28 of 28 equal, by tool | CONFIRMED | SCRATCH/runs/appx1.out. |
| E46 | Committed bytes differ from the mutation-tested draft only in the repository line, derived from `__file__` (§6) | CONFIRMED | `diff` round2b-base vs REPO/scripts/n_analyze.py: one hunk, l.49. |
| E47 | The block is `8e3bf91` | CONFIRMED | 8e3bf91 adds results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md. |
| E48 | PIN-n-20–22 and PIN-n-12's amendment: Code's readings, declared as the block's §3 readings, strikable by the seat until LOCK-n v1.0 | CONFIRMED | None of them is in the frozen copy or the 154-check drafts; `PINS`' comment "Code's readings, declared (each strikable by the seat until LOCK-n v1.0)"; block §3 "each strikable until LOCK-n v1.0". |
| E49 | The OPEN additions carried pending the seat, like Q1–Q9's | CONFIRMED | `OPEN`'s comment: "each pending the seat". |
| E50 | PIN-n-20 (nonfinite / shadow / tau4-emptied, with causes) | CONFIRMED | `PINS["PIN-n-20"]`; `Campaign.usable`, `build_state` (`shadows_ok`, `emptied`), `_causes`. |
| E51 | PIN-n-21 (dated the PI date; Clock cause refused on or before D_n, inclusive, §7.4) | CONFIRMED | `PINS["PIN-n-21"]`; `not_run_reason` (`date <= D_N`); proposal §7.4 "each the day inclusive". |
| E52 | PIN-n-22 ((a), (c) readings; n ≥ 20 for (a), (c), (d)) | CONFIRMED | `PINS["PIN-n-22"]`. |
| E53 | PIN-n-12 amended (TAU/4 row: each statistic at its own count) | CONFIRMED | `PINS["PIN-n-12"]`; `boot_index(arm, len(…))` per statistic in `build_state`. |
| E54 | "Added to OPEN-Q6: a pause on N1-V's or N1-R's reads, or on N1-P's where d_20 sits at +1, alone leaves N2 evaluated", under "Readings registered since the block" | IMPRECISE | The code's `OPEN-Q6` text gained the clause since the frozen copy, but the block itself already carried this reading in its Q6 (block line 46): "A pause standing on N1-V's, N1-R's or N1-P's reads leaves N2 evaluable, as written." It is not a new reading for the seat. Correction: "Written into the code's OPEN-Q6 register (the block's Q6 already carried it: 'A pause standing on N1-V's, N1-R's or N1-P's reads leaves N2 evaluable, as written'); new since the block is the battery's case for it, and F2's fix, which counts pauses on N2-S's and N2-C's reads." (The code's own OPEN-Q6 text says "a reading added since the block, for the seat", l.1674–1677: the same wording in the bytes to be committed.) |
| E55 | §5's N2 reads are N2-E's, N2-S's, N2-C's; those arms' incompleteness remains a cause | CONFIRMED | `n2_outcome` (l.432): pauses counted on `N2_ARMS` only; non-pause causes over N2-E, N1-V, N1-R (+ N1-P where d_20 is at +1). |
| E56 | OPEN-Q8: the route fills "on their direction" / "on a reconstructed direction" (in the draft at the block's time) and VALUE_MERGED "{value} (read at d = {point}, the point it merges into under §2.3)" (new since, F3) | CONFIRMED | `ROUTE_TEXT` l.2222, `VALUE_MERGED` l.2225, verbatim; appx1.out lists exactly these three outside Appendix A; the 154-check drafts (SCRATCH/n_analyze.pre-cmds.py, pre-ganl.py; the block reports 154 checks) have `ROUTE_TEXT` and no `VALUE_MERGED`; the frozen copy likewise. |
| E57 | The seat's answers to the block are not in yet | CONFIRMED | No commit after 8e3bf91 touches the block or answers it (HEAD 9464f61); item 9 puts them at the next sitting. |
| E58 | The PI's routing (file, `18102d0`, "N. n", item 9) and its quotation | CONFIRMED | Verbatim, backticks included, at line 69 of results/raw/2026-11-16_p-verdicts-decisions_design-to-code_answers.md (blob identical at 18102d0 and HEAD), §8 "Routing block for the PI"; 18102d0's subject records the PI's "Route as given". |
| E59 | `verdicts` built after n-build's forms, in an entry of its own | UNVERIFIABLE | Plan; consistent with the module docstring. |
| E60 | Its rules "as n-build's schema v4.1 sets them", agreed with n-build (PAUSE refused; STOP or cap with no arm complete → NOT-RUN no-arm; else analyzed; a pause stands only under PI-STOP, its arms INDETERMINATE) | UNVERIFIABLE | Agreement is a message; no committed or n-build file in reach names schema v4.1 (the committed schema is 5a97527's; the untracked REPO/valence_core/n/runner.py lists end states COMPLETE, PAUSE, STOP, CAP, PI-STOP). Agrees with SCRATCH/PLAN.md, whose commit-order note names the coming schema commit "v4.4". |
| E61 | Canonical run `data/n/gates/G-ANL-n.json`; waits for the seat's answers and G-CAL-n's pinned map | CONFIRMED | `GANL_REL` l.2876; "canonical-no-map". |
| E62 | "The analyzer refuses any `valence_core/n/schema.py` but the bytes at `5a97527`" (and "then refuses until its pin moves") | IMPRECISE | The pin binds where the schema is loaded (`schema_module`: the reader and the battery). With other bytes, `--selftest` fails (its groups record the refusal; exit 1), `ganl` STOPs (exit 4) writing nothing, and `not-run` loads no schema and proceeds. Correction: "The analyzer's reader and battery refuse any … (so `--selftest` fails and `ganl` stops); `not-run` reads no schema." |
| E63 | n-build's next schema commit, now waiting on its blind pass, will change that file | UNVERIFIABLE | n-build's state; the working-tree schema still equals 5a97527's blob. |
| E64 | The pin's move in its own entry: reader's calls re-checked, battery re-run in a window | UNVERIFIABLE | Plan. |
| E65 | Since the block, apart from the departures, every Python run inside a granted battery window: one at a time, `nice -n 19`, foreground, temp folders outside the repository | UNVERIFIABLE | Grants are messages. Consistent: SCRATCH/review/run_mutants.sh runs one mutant at a time at `nice -n 19`; the battery's temp folders come from `tempfile.TemporaryDirectory` (l.2525, l.3163). |
| E66 | The processes before the block are declared in 8e3bf91's entry ("Declarations, by date"), which asks for them in G-ANL-n's entry | CONFIRMED | REPO/RESULTS.md, added by 8e3bf91: "**Declarations, by date** (to be repeated in the G-ANL-n entry, as the coordinating session asked)". |
| E67 | Window 1: the frozen copy's baseline and its 40 mutants | CONFIRMED | out1/BASE.out, out1/M01–M40.out. |
| E68 | Window 1: "and one battery run of the fixed draft" | IMPRECISE | The five battery outputs on file map one to one onto the listed runs; the only one left for window 1, SCRATCH/runs/sel1.out, is 168/171: "check count 171 == EXPECTED_CHECKS 159" and the forms digest failing against an unpinned constant. Those are the bytes of SCRATCH/n_analyze.pre-pin.py, which differs from `fc479b81` only in those two pins. Correction: "one battery run of the fixed draft before its check count and forms digest were pinned (168/171)". |
| E69 | Window 2: a confirming run, the Appendix A check, the 51 round-2 runs | CONFIRMED | sel2.out (171/171), appx1.out, out2 (51). Window grant UNVERIFIABLE. |
| E70 | Window 3: the first run of record from `scripts/` | CONFIRMED | record.out (`INVOCATION: … scripts/n_analyze.py --selftest`), the pre-values-check texts. |
| E71 | Window 4: a battery run of the amended draft, round 2's 51 runs on it, the run of record | CONFIRMED | sel3.out (171/171), out3 (51), record2.out. |
| E72 | Two system-interpreter starts outside any window during Q-F3's campaign (the two commands), each told to the coordinating session at the time | UNVERIFIABLE | Only the author's notes (SCRATCH/PLAN.md "Departures to declare") record them. |
| E73 | Neither read a file or imported beyond startup; no model marker; no Q-F3 invocation starting | UNVERIFIABLE | The quoted command parts name no model marker; the rest is not on file. |
| E74 | The coordinating session called the second harmless and asked that both be declared | UNVERIFIABLE | Message. |
| E75 | One process beyond a window's wording: the baseline, declared at release | UNVERIFIABLE | Message; out1/BASE.out exists. |
| E76 | Committed by path (five items); not pushed | UNVERIFIABLE | Future. |
| E77 | Next | UNVERIFIABLE | Plan. |

#### 2. The review raw (SCRATCH/block/2026-11-16_n-analyze_build_review.md)

##### Head and method

| # | Claim | Status | Evidence / correction |
|---|---|---|---|
| V1 | Title; PI date 2026-11-16 | CONFIRMED | |
| V2 | Code's raw for the entry `n package — scripts/n_analyze.py, BUILD` | CONFIRMED | The entry's name. |
| V3 | Draft at `4db3a206…ed46` | CONFIRMED | |
| V4 | "frozen as a copy before the review" | UNVERIFIABLE | Timing; the copy exists with that hash. |
| V5 | Subagent of this session; brief quoting items 1–5 | UNVERIFIABLE | As E31. |
| V6 | F1–F15, N1–N15 | CONFIRMED | |
| V7 | §1 is the text as saved | CONFIRMED | §1 (lines 27–77) equals findings.md lines 6–56 exactly, its `##` headings shown as `###`. |
| V8 | "unedited in substance" against the hand-back | UNVERIFIABLE | The hand-back is a message; findings.md is Code's save. |
| V9 | Forty mutants M01–M40 written against the frozen copy | CONFIRMED | Each `.old` is one line found exactly once in the frozen copy, at the line the TSV states (all 40 `l.N` refs match); every out1 `*.py` = frozen copy + its replacement. |
| V10 | One unmutated baseline, 159/159 | CONFIRMED | out1/BASE.out. |
| V11 | 12 killed, 28 survived, as predicted ("no" ×12; "yes" or once "yes (likely)" ×28) | CONFIRMED | As E36–E37. |
| V12 | The dispositions' summary (fixed; registered (N3); kept: N12's `sys.executable`, N2's helpers) | CONFIRMED | §3. |
| V13 | Round 2's composition (as E40) | CONFIRMED | |
| V14 | "R07b re-targets R07's defect" | CONFIRMED | R07b swaps the f mapping of N2's reads (`fv`), the defect M08 named and R07 meant to re-express. |
| V15 | First run on `fc479b81…ef5f`: 50 of 51 killed, R07 survived | CONFIRMED | As E41–E42. |
| V16 | "because no check read N2's per-f counts and SDs, which it moves" | IMPRECISE | As E43. |
| V17 | All 51 on `cc0fa5b1…3ea8` (171/171) killed (§4) | CONFIRMED | As E44. |
| V18 | Appendix A 28 of 28 (§5) | CONFIRMED | |
| V19 | Committed bytes differ only in the repository line (§6) | CONFIRMED | |
| V20 | Every run inside a granted window (the baseline beyond its wording, declared at release); one at a time, `nice -n 19`, foreground, temp folders outside | UNVERIFIABLE | As E65. |
| V21 | Nothing ran on a model or on the box | UNVERIFIABLE | Session acts. |
| V22 | Each mutant an exact, unique replacement (asserted once) on a fresh copy of its base; `--selftest`; "killed" = non-zero exit | CONFIRMED | run_mutants.sh (`cp`; perl count must be 1, else APPLY-FAIL, none in any summary; `nice -n 19 … --selftest`; rc ≠ 0 → killed); every `*.py` in out1/out2/out3 is its base plus its one replacement. |

##### §2 (round 1 table)

| # | Claim | Status | Evidence / correction |
|---|---|---|---|
| V23 | Baseline 159/159 (`out1/BASE.out`) | CONFIRMED | |
| V24 | "the runner printed its exit, 0, to the session" | UNVERIFIABLE | Not on file; run_mutants.sh cannot run the baseline (it needs `BASE.old`), so whatever printed it is not recorded. |
| V25 | M01–M20 and M21–M40 in two parts | CONFIRMED | out1/part1.summary, part2.summary. |
| V26 | The reviewer's columns are as written in `mutants.tsv` | CONFIRMED | All 40 rows rebuilt from the TSV (cells whole, `|` escaped as `\|`) equal the table's first four columns. |
| V27 | Last column: the run's, first failing check with coverage and count lines left out; "…" only where cut | CONFIRMED | Rebuilt from out1/Mnn.out: `fails=` = the `[FAIL]` count (= all.summary); the 28 SURVIVED are rc 0; M40's uncut cell has no "…". |
| V28 | "a text longer than 90 characters is cut and marked "…"" | IMPRECISE | The cut is at 90 bytes of UTF-8, not 90 characters: cells whose text has Δ, § or ≈ before the cut end 1–2 characters early (round 1: M16 "…hold, C…", M24 and M25 "…read f…"; round 2: R31 "…without a fi…", R33 "…reads';…", R34 "…its sente…"), and R31's pipes are escaped after the cut. All 91 result cells equal the outputs under a 90-byte cut. Correction: "cut at 90 bytes", or re-cut at 90 characters. |
| V29 | The table, 40 rows | CONFIRMED | `diff` against the rebuilt rows: empty. |

##### §3 (the dispositions; each row's code claim read in REPO/scripts/n_analyze.py, each named check id in `_REQ`)

| # | Claim | Status | Evidence / correction |
|---|---|---|---|
| V30 | 30 rows, F1–F15 and N1–N15 | CONFIRMED | |
| D-F1 | Shadows present and finite or `shadow:<arm>`; `_cross_checks` refuses an absent shadow; RD-SHADOW, RD-REFUSE | CONFIRMED | `build_state` (`shadows_ok`, `unusable`), `_cross_checks` "is not on disk"; selftest lines 146, 156. |
| D-F2a | A pause on N2-S's or N2-C's reads makes N2 INDETERMINATE; the n:140 quotation | CONFIRMED | `n2_outcome`; proposal line 140 contains "an unadjudicated pause stands on N2's reads" verbatim. |
| D-F2b | "(added to OPEN-Q6, for the seat)" for the N1-arm pause reading | IMPRECISE | As E54: the block's Q6 already carried it. |
| D-F3 | VALUE_MERGED in `value_text`; RD-MERGED-DEQ | CONFIRMED | l.2225–2234; selftest line 149 (DETECTABLE, literal text). |
| D-F4 | PIN-n-21 in `not_run_reason`; NR-REFUSE-PREMATURE | CONFIRMED | |
| D-F5 | Exactly five finite JSON floats; named refusals (`ganl_precheck`); 18 refusals, one pass | CONFIRMED | `dose_map_input_problems`; `cases` has 18 entries; selftest line 162. |
| D-F6 | A matrix per statistic's session count in the TAU/4 row; identical branches gone; PIN-n-12 amended | CONFIRMED | `boot_index(arm, len(…))` per statistic; no `drop is None` branch pair. |
| D-F7 | PIN-n-20 (`Campaign.usable`, `_causes`); RD-NONFINITE | CONFIRMED | |
| D-F8 | N1-P's signed estimates, N2's slopes and floor computed and returned with `build_state`'s figures; `verdicts` reports them | CONFIRMED | `fig["P_signed"]`, `["slopes_N2"]`, `["floors_N2"]`. |
| D-F9 | 31 forms by digest, distinct, declared slots; Appendix A by tool | CONFIRMED | |
| D-F10 | Filled sentences against literal text for the listed states | CONFIRMED | Selftest lines 139, 143, 149. |
| D-F11 | The asymmetric campaign's hand computation, with N2's per-f n and SD added after the values-check | CONFIRMED | `asym_ok`'s keys (l.2672–2690), `np.polyfit` hands. |
| D-F12 | Mixed G-READ-n states | CONFIRMED | Selftest line 152. |
| D-F13 | Each ceiling computed once; the reported ceiling is the one used | CONFIRMED | `n1_outcome`/`dose_outcome`/`n2_outcome` each call `ceiling` once per site and decide with `above`. |
| D-F14 | Counters through `counters` (TAU/4 apart from TAU, identity bound, label mass < .20); TAU/4 row through `tau4_drop`/`build_state`; `tau4_keep` removed | CONFIRMED | `tau4_keep` absent; `label_mass_below` called in `counters`. |
| D-F15 | Two-sided refusals; merge edge at 0.05; `--out` at the root; RD-REFUSE's new cases | CONFIRMED | Selftest lines 132, 156, 158, 162. |
| D-N1 | OPEN cites the committed block | CONFIRMED | `OPEN`'s comment names results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md. |
| D-N2 | `lock_names` etc. kept for `verdicts`; `n2_slope_points` used; `tau4_keep` removed; `label_mass_below` used; `Campaign.nonfinite` read | CONFIRMED | |
| D-N3 | PIN-n-22; RD-SECONDARY, RD-SECONDARY-FLOOR | CONFIRMED | |
| D-N4 | The hook (OS-relative and repository-relative for processes; file=/path=/args=/cwd=; os.open, subprocess.run; absent probe paths; data/mf3 by string and through a process reading no argument) | CONFIRMED | `_Hook`, `_norm`; the nine probes (`/usr/bin/true`, `hook.check`). |
| D-N5 | The snapshot prunes exactly what `_barred` bars | CONFIRMED | `_bt_snapshot`'s `os.walk` filter. |
| D-N6 | The imported schema module must be the hashed file | CONFIRMED | `schema_module`. |
| D-N7 | Unknown route STOPs; readable dose sentence without AUC STOPs | CONFIRMED | `fill`. |
| D-N8 | TAU/4-emptied arm marked `tau4-emptied`, never a STOP or NaN | CONFIRMED | `emptied()`; NaN floor slopes routed to it. |
| D-N9 | GATE_STAGES lists §3's pre-lock gates with G-DATA and G-ACQ | CONFIRMED | l.101 = the proposal §3's seven pre-lock gates. |
| D-N10 | `map_reach`, `map_reach_by_hand`, `literal_state` (formerly `_bt_state`) | CONFIRMED | Canonical path `run_ganl` → `ganl_artifact` → `pinned_map_reach` → `map_reach` → `literal_state`: no `_bt` call; `_bt_state` absent; the frozen copy had `_bt_reach`, `_bt_expected_reach`. |
| D-N11 | `ganl_precheck` holds every pre-battery refusal; the battery never calls `run_ganl` | CONFIRMED | `run_ganl(` occurs only in `main`. |
| D-N12 | `main()` prints `sys.executable` (house form of m_analyze, p_analyze); committed file derives REPO from `__file__` | CONFIRMED | REPO/scripts/m_analyze.py l.11269, p_analyze.py l.696 print the same INVOCATION line; l.49. |
| D-N13 | `not_run_precheck` | CONFIRMED | |
| D-N14 | Write-once by `os.link` from a private temp file | CONFIRMED | `write_once`. |
| D-N15 | Cell hash of the bytes parsed; capture bytes against `capture_sha256` | CONFIRMED | `load_campaign`. |

##### §4, §5, §6

| # | Claim | Status | Evidence / correction |
|---|---|---|---|
| V31 | Base: the amended draft `cc0fa5b1…3ea8` (171/171) | CONFIRMED | Hash; sel3.out. |
| V32 | "It is the fixed draft with the values-check's three code findings applied: …" | IMPRECISE | The three named changes are in the diff `fc479b81` → `cc0fa5b1`, but so are three docstring edits it does not name: the `not-run` usage text and `State`'s docstring ("(build_state)"), both already in SCRATCH/n_analyze.pre-vc.py, and `map_reach_by_hand`'s docstring (now citing the question block's Q5). Correction: "… the fixed draft with two docstrings edited before the values-check (the `not-run` usage text; `State`'s) and its three code findings applied (…), and `map_reach_by_hand`'s docstring citing the block." |
| V33 | Three parts: R01–R17, R18–R34, R35–R50 with R07b | CONFIRMED | out3/part1–3.summary. |
| V34 | First run on `fc479b81…ef5f` (171/171): 50 of 51, R07 survived | CONFIRMED | out2; the 171/171 by inference (out2/R07.out, a run that moves no checked figure, ends 171/171; sel2.out). |
| V35 | "The values-check showed R07 was not equivalent." | UNVERIFIABLE (blind) | Depends on the earlier pass; see Part 2 (its R68). |
| V36 | The loop: `tgt[f]` from `fv[f]`; `fig["n"]`, `fig["sd0"]` set by label; the swap exchanges N2's per-f counts and SDs | CONFIRMED | Fixed draft l.2175–2178; committed l.2180–2183. |
| V37 | "which no check read" | IMPRECISE | As E43. |
| V38 | R07's failing sub-check is "N2's per-f n and SD (ddof 0)" | CONFIRMED | out3/R07.out: the RD-ASYM `[FAIL]` line ends `["N2's per-f n and SD (ddof 0)"]`. |
| V39 | "below" | IMPRECISE | The table's R07 cell is cut before the sub-check list, so it does not show it. Correction: "R07's failing sub-check (in its output; the table's cell is cut before it) is …". |
| V40 | Table columns Id / What it breaks / Expected killer | CONFIRMED | All 51 rows equal mutants2/mutants.tsv. |
| V41 | Results column | CONFIRMED | `fails=` and the first failing check of each out3/Rnn.out (90-byte cut, as V28). |
| V42 | Each round-2 `.old` applied exactly once | CONFIRMED | Each of the 51 `.old` texts occurs exactly once in SCRATCH/review/n_analyze.round2b-base.py (and once in round2-base.py). |
| V43 | The tool "imported the fixed draft (`fc479b81…ef5f`)" | UNVERIFIABLE | appx1.out names neither input. The result does not depend on it: the 31 forms are byte-identical in every draft that has VALUE_MERGED (pre-pin, pre-vc, fc479b81, cc0fa5b1, the committed file). |
| V44 | It read the committed block | CONFIRMED | SCRATCH/block's copy, REPO's file and `git show 8e3bf91:…` all hash to `2cd1acdf…7ed03`. |
| V45 | It compared each italic span with the form of that name in `code_forms()` | CONFIRMED | SCRATCH/tools/appendix_check.py. |
| V46 | Forms unchanged since; the committed battery passes SENT-CODE-FORMS against the same pinned digest | CONFIRMED | `CODE_FORMS_SHA256` identical in fc479b81 and the committed file; record2.out line 100. |
| V47 | Its output, whole | CONFIRMED | Lines 239–268 equal appx1.out (30 lines). |
| V48 | The three forms go to the seat under OPEN-Q8; route fills at the block's time; VALUE_MERGED new (F3) | CONFIRMED | As E56. |
| V49 | §6: `diff` of `cc0fa5b1…3ea8` against the committed `67f35ecb…82db`, whole | CONFIRMED | `diff` output equals lines 282–285 with the absolute root shown as `<repo>`; SCRATCH/tree/diff_vs_round2b_base.txt likewise. |
| V50 | `<repo>` scrub; only the repository line changes; derived from `__file__` | CONFIRMED | |

#### 3. The selftest raw (SCRATCH/block/2026-11-16_n-analyze_build_selftest.txt)

| # | Claim | Status | Evidence / correction |
|---|---|---|---|
| S1 | The battery of record, `scripts/n_analyze.py --selftest` | CONFIRMED | Its INVOCATION line. |
| S2 | sha256 `67f35ecb…82db` (full in the header) | CONFIRMED | The hash of REPO/scripts/n_analyze.py. |
| S3 | "on the committed bytes": the run executed those bytes | UNVERIFIABLE | No output records the bytes it ran. Consistent: the body equals sel3.out's (the amended draft) apart from the invocation, and the two files differ only in the REPO line, which prints nothing. |
| S4 | Run from the repository root | CONFIRMED | The relative `scripts/n_analyze.py` in INVOCATION. |
| S5 | `nice -n 19`, in a granted battery window | UNVERIFIABLE | Not in the output; grants are messages. |
| S6 | PI date 2026-11-16 | CONFIRMED | |
| S7 | 171/171 | CONFIRMED | |
| S8 | Exit 0 | CONFIRMED | As E18 (inferred). |
| S9 | The repository root shown as `<repo>` | CONFIRMED | |
| S10 | The output its header says | CONFIRMED | Lines 2–174 equal SCRATCH/runs/record2.out (173 lines) with the root replaced by `<repo>` (`diff` empty). |

#### 4. Across the three drafts

| # | Claim | Status | Evidence |
|---|---|---|---|
| X1 | No local path or user name beyond `<repo>` | CONFIRMED | `/usr/bin/grep -i` for the user name, the home root, the private and temp roots, the scratchpad and session roots: no match. |
| X2 | Calendar dates only, no clock time | CONFIRMED | No time pattern (the only hits were the class name `Est`). |
| X3 | No pod address or port | CONFIRMED | No IP or port pattern. |
| X4 | The entry's figures match the selftest raw | CONFIRMED | 171/171, 172 ids, 385 tuples / 1,921 evaluations, 31 forms; the review's 18 refusals (line 162). |

#### Totals (blind pass)

| Draft | CONFIRMED | IMPRECISE | FAIL | UNVERIFIABLE | Claims |
|---|---|---|---|---|---|
| Entry | 58 | 6 | 0 | 13 | 77 |
| Review raw | 67 | 6 | 0 | 8 | 81 |
| Selftest raw | 8 | 0 | 0 | 2 | 10 |
| Across | 4 | 0 | 0 | 0 | 4 |
| **All** | **137** | **12** | **0** | **23** | **172** |

#### FAILs and IMPRECISE items, in order of importance

No FAIL.

1. **E54, D-F2b — the OPEN-Q6 "addition" is the block's own Q6 reading.** The block (8e3bf91, line 46) already carries: "A pause standing on N1-V's, N1-R's or N1-P's reads leaves N2 evaluable, as written." Only the code's register text is new. Correction for the entry: "Written into the code's OPEN-Q6 register (the block's Q6 already carried it); new since the block is the battery's case for it and F2's fix (pauses on N2-S's and N2-C's reads count)". For the raw's F2 row: "… alone does not (the block's Q6 reading, now in OPEN-Q6's text)". The code's OPEN-Q6 says the same ("a reading added since the block, for the seat", l.1674–1677); changing it changes the committed bytes and needs its own run. The author decides.
2. **E43, V16, V37 — why R07 survived.** RD-SENSITIVITY reads an N2 per-f count, `fig_s["n"][("N2-E", "f0.10")] == 159` (fixed draft l.2757; committed l.2769); it is equal at both f there, so the swap was invisible. Correction: "no check could see it: no check read N2's per-f SDs, which it exchanges, and the one per-f count a check read (RD-SENSITIVITY's N2-E at f = 0.10) is the same at both f in that campaign".
3. **V32 — the amended draft's description** leaves out three docstring edits in the same diff (the `not-run` usage text and `State`'s docstring, both from before the values-check; `map_reach_by_hand`'s). Correction as in the table.
4. **E68 — window 1's "one battery run of the fixed draft"** was, by the outputs on file, a 168/171 run of the fixed code before its two pins (SCRATCH/runs/sel1.out; = SCRATCH/n_analyze.pre-pin.py). Correction: "one battery run of the fixed draft before its check count and forms digest were pinned (168/171)".
5. **E62 — "refuses any schema.py".** The pin binds the reader and the battery. Other bytes make `--selftest` fail and `ganl` stop; `not-run` reads no schema. Correction as in the table.
6. **E15 — "run once from this path".** There are two runs from `scripts/` (record.out of the earlier bytes, record2.out). Correction: "its battery on these bytes, run once from this path".
7. **E22 — NOT-RUN "from them".** The NOT-RUN comes from a record, not from §4's statistics. Correction as in the table.
8. **V28 — "90 characters".** The cut is at 90 bytes, so six cells (M16, M24, M25, R31, R33, R34) are cut 1–2 characters short. Correction: "90 bytes", or re-cut.
9. **V39 — "below".** The R07 cell is cut before its sub-check. Correction as in the table.

---

### Part 2 — The earlier pass and the author's dispositions

Opened only after Part 1: SCRATCH/vc/build_report.md (on the earlier drafts, sha256 `671d7308…`, `0084e842…`,
`205244ee…`) and SCRATCH/block/vc_dispositions.md.

| Disposition item (first pass) | Now carried? | Evidence in the current drafts |
|---|---|---|
| R68 (with E46, R17, R66), FAIL: R07 not equivalent | APPLIED | Code: the round2-base → round2b-base diff gives N2-E different spreads by f and adds RD-ASYM's "N2's per-f n and SD (ddof 0)"; round 2 re-ran on the amended draft (out3: 51/51 killed, R07 on that sub-check). Neither draft calls R07 equivalent; review raw line 172: "The values-check showed R07 was not equivalent" (this also settles V35: the first pass's R68 says so). Note: the reason now given ("no check read N2's per-f counts") comes from the first pass's evidence for R68 ("the battery reads only `fig11[…]`"). That evidence missed RD-SENSITIVITY's `fig_s["n"]` reads; see Part 1 item 2. |
| E72, FAIL: windows declaration | APPLIED | Entry: "Since the block (`8e3bf91`), apart from the departures below, …; The processes before the block are declared in `8e3bf91`'s entry ("Declarations, by date"), which asks that they be repeated in G-ANL-n's entry." |
| R58, FAIL: `_bt_state` on the canonical path | APPLIED | `literal_state` (l.949) replaces `_bt_state` (absent); `map_reach` calls it, and no `_bt` helper is on `ganl`'s canonical path; the N10 row says so. |
| E64, FAIL: item-9 quotation | APPLIED | Verbatim with "as its entries have it", backticks, file and `18102d0`. |
| R29, FAIL: reviewer cells cut | APPLIED | All 40 reviewer cells whole (= TSV); "…" only on cut cells (M40 and R45 unmarked). Residue: the result cells are cut at 90 bytes, not the 90 characters the disposition and the raw state (Part 1 item 8). |
| R34, FAIL: §5 misquoted in F2 | APPLIED | F2's row quotes n:140 verbatim; the battery's pause lines quote it (selftest lines 41–43). |
| E53, IMPRECISE: PINs "pending the seat" | APPLIED | "Code's readings, declared as the block's §3 readings are (strikable by the seat until LOCK-n v1.0). The additions to OPEN-Q6 and OPEN-Q8 are carried pending the seat". |
| E59, R35, IMPRECISE: N1-P left out of the OPEN-Q6 addition | APPLIED | Entry and F2 row name "N1-P's where d_20 sits at +1"; the battery case `g_npb` (shape b, N1-P paused; l.1081), selftest line 47. Residue: the reading itself predates the block (Part 1 item 1). |
| R21, IMPRECISE: windows sentence vs the baseline | APPLIED | Raw head: "(the frozen copy's unmutated baseline beyond its window's wording, declared when that window was released)". |
| E40, R10, IMPRECISE: dispositions' summary | APPLIED | Entry names N12 and N2's four helpers; raw names N3, N12's `sys.executable`, N2's helpers. |
| R77, IMPRECISE: "three forms added since the block" | APPLIED | Raw §5 and the entry: route fills "in the draft at the block's time, unlisted there"; VALUE_MERGED "new since, F3". |
| E43, R15, IMPRECISE: "each round-1 defect re-expressed" | APPLIED | Both: "each of round 1's 28 survivors re-expressed … (R01–R03, R05–R29; R04 re-expresses M05, which round 1 killed), and new mutants on the fixes (R30–R50)". |
| R12, IMPRECISE: "changes one line" | APPLIED (superseded, as stated) | §6 is now one hunk; the two docstrings are in the amended draft. |
| E55, IMPRECISE: `tau4-emptied` cause form | APPLIED | "An arm the TAU/4 row empties at a point is not usable in that row (cause `tau4-emptied:<arm>`)". |
| R41, IMPRECISE: F8 "reported" | APPLIED | "computed and returned with `build_state`'s figures (OPEN-Q9's points); the `verdicts` command, not in this BUILD, reports them". |
| E6, IMPRECISE: only round 1 blind | APPLIED | "reviewed blind (round 1) and mutation-tested in two rounds"; "Round 2, Code's mutants." |
| R26, IMPRECISE: "as returned" | APPLIED | Head and §1's heading: "as saved from the reviewer's hand-back, unedited in substance". |
| Observations (abbreviation tail; "…" on uncut cells; "BASE rc=0") | APPLIED | `fc479b81…ef5f` in all three places; no "…" on uncut cells; "159/159 (`out1/BASE.out`; the runner printed its exit, 0, to the session)". Residue: that exit is still on no file (V24). |
| The checker's departures | Not a draft item | Nothing to carry. |

All 18 dispositions are carried. Two leave a residue: R29, where the cut is in bytes, and R68, where the wording rests on
evidence that missed RD-SENSITIVITY.

---

#### This checker's departures

- Tools beyond the brief's list, all printing only, never in place, on scratch outputs and committed files only:
  - `cut` once, to shorten a `git log` subject.
  - `tr` twice, to join name-only `ls` listings.
  - `tail` once, on SCRATCH/review/out1/BASE.out.
  - `sort` and `uniq -c` once, on `awk` output from the review raw.
  - `sed` without `-n`, with `s///` path scrubs.
  - `git hash-object` once, on REPO/valence_core/n/schema.py (digest only).
  - `git ls-files` on named paths.
  - `diff -q`, shell `echo` and `printf`.
  - `cat` appeared once, in a command line that zsh aborted at an `echo ==` before reaching it; the file (SCRATCH/vc/exitcodes.txt, from an earlier check, not used here) was then printed with `sed`.
  - `> /dev/null` once, to discard output.
- Read, in REPO, untracked files of another session: a name-only `ls` of `valence_core/n/`, a non-recursive
  `/usr/bin/grep` over `valence_core/n/*.py`, and `sed -n` of `valence_core/n/runner.py` lines 1–45. Nothing under `data/`.
- No temporary file was written; this report is the only write. No Python, no model process, nothing in the background,
  no `git status`, no tree-wide search, no pickaxe.

## 4. Code's dispositions of the second pass (every IMPRECISE item; there was no FAIL)

| Item | Disposition |
|---|---|
| 1. The OPEN-Q6 "addition" is not new (E54; §3 F2) | Accepted. The block's Q6 already says "A pause standing on N1-V's, N1-R's or N1-P's reads leaves N2 evaluable, as written." The entry now says OPEN-Q6 is not extended, and that what is new since the block is F2's fix and the battery's case. F2's disposition row says the same. The code's own OPEN-Q6 text said "a reading added since the block, for the seat"; it now ends "as written". That is a code change, so the committed bytes differ from the mutation-tested draft in this string as well as the repository line (the review raw's §6). No check reads the string's content, so the mutants' results stand. A new run of record covers the committed bytes. |
| 2. Why R07 survived (E43; review head and §4) | Accepted. No check could see the swap: no check read N2's per-f SDs, and the one per-f count a check read (RD-SENSITIVITY's) is equal at both f. |
| 3. The amended draft's description (§4) | Accepted. §4 lists the docstring edits the amended draft carries. The checker named three (`not-run`'s usage text, `State`'s, `map_reach_by_hand`'s); `literal_state`'s, rewritten with the rename, is the fourth. |
| 4. Window 1's battery run (entry) | Accepted: "one battery run of the fixed draft before its two pins (168/171: the forms digest and the check count, then pinned)". |
| 5. What the pin refuses (entry) | Accepted: the reader and the battery refuse, so `--selftest` fails and `ganl` stops; `not-run` loads no schema. |
| 6. "Run once from this path" (entry) | Accepted: "run from this path on these bytes (the run of record; earlier runs from this path were of earlier bytes)". |
| 7. NOT-RUN "from them" (entry) | Accepted: the unit's NOT-RUN comes from a NOT-RUN record; N1, dose, N2 and N4 from the statistics. |
| 8. "Cut at 90 characters" (§2) | Accepted: "90 bytes". |
| 9. "R07's failing sub-check below" (§4) | Accepted: §4 names the sub-check and its output file, and says the table's cell is cut before it. |
| UNVERIFIABLE: "schema v4.1" | Worded "as n-build's schema sets them from v4.1 on". The rules came in n-build's message on v4.1, and its later messages (v4.2, the commit order for v4.4) left them unchanged. |
| The checker's departures | Noted. It used printing-only tools beyond the list (`cut`, `tail`, `tr`, `sort`, `uniq -c`, `sed` scrubs, `diff -q`, `echo`, `printf`), plus `git hash-object` on the schema and `git ls-files` on named paths. It read another session's untracked `valence_core/n/` files: a name-only `ls`, a non-recursive grep, and `runner.py`'s first 45 lines. It edited nothing, wrote no file but its report, ran no Python, and touched nothing under `data/`. |
