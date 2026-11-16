# n_analyze.py BUILD: the blind review, its mutants and the dispositions (PI date 2026-11-16)

Code's raw for the entry `n package — scripts/n_analyze.py, BUILD`.

- **Round 1, blind.** A reviewer read the draft at sha256 `4db3a206…ed46`, frozen as a copy before the review. The
  reviewer was a subagent of this session, under a brief quoting the list of record v2's items 1–5. It returned
  findings F1–F15 and notes N1–N15 (§1, as saved from the reviewer's hand-back, unedited in substance) and forty
  mutants M01–M40 written against the frozen copy. Code ran one unmutated baseline of the frozen copy (159/159), then
  the forty mutants (§2): 12 killed and 28 survived, each as the reviewer predicted (the 12 marked "no", the 28
  marked "yes" or, once, "yes (likely)").
- **The dispositions.** Code disposed of every finding and note (§3): fixed, registered as a reading (N3), or kept
  with its reason (N12's `sys.executable`; N2's helpers for the `verdicts` command).
- **Round 2, Code's mutants.** Fifty mutants: each of round 1's 28 survivors re-expressed on the new code (R01–R03,
  R05–R29; R04 re-expresses M05, which round 1 killed), and new mutants on the fixes (R30–R50); R07b re-targets R07's
  defect. A first run, on the fixed draft before the values-check (sha256 `fc479b81…ef5f`), killed 50 of its 51 runs.
  R07 survived because no check could see its swap: no check read N2's per-f SDs, and the one per-f count a check
  read (RD-SENSITIVITY's) is equal at both f. With a check of N2's per-f counts and SDs added, all 51 runs on the
  amended draft (sha256 `cc0fa5b1…3ea8`, 171/171) were killed (§4).
- **Appendix A** of the committed question block, compared form by form with the code (§5): 28 of 28 equal.
- **The committed bytes** differ from the mutation-tested draft in the repository line and in one string of the
  OPEN register, OPEN-Q6's text, which no check reads (§6).

Every run here was inside a battery window the coordinating session granted (the frozen copy's unmutated baseline
beyond its window's wording, declared when that window was released): one process at a time, `nice -n 19`, in the
foreground, with temp folders outside the repository. Nothing ran on a model or on the box. Each mutant was applied
as an exact, unique text replacement (`.old` → `.new`, asserted to occur once) to a fresh copy of its base. That
copy's battery ran with `--selftest`, and "killed" means a non-zero exit.

## 1. Round 1: the reviewer's findings, as saved from its hand-back (unedited in substance)

### MAJOR

- **F1. `build_state` crashes when a shadow is non-finite or absent and another arm is complete** (l.1948–1962,
  l.2008–2039, l.1909–1912). `delta_m` returns `None` when any session's `N1-V|none|0` shadow is missing or
  non-finite; `build_state` guards only on the arm's own completeness, then calls `_vec(None)`. Scenario: the shadow of
  one session written non-finite; §6 pauses only N1-V's launches; every other arm completes; `complete["N1-R"]` True,
  `dm("N1-R", …)` None, `_vec(None)` raises TypeError (exit 1). Expected: N1, dose, N2 INDETERMINATE
  (incomplete:N1-V), N4 decided. Related: `_cross_checks` never refuses an absent shadow.
- **F2. N2's INDETERMINATE counts a pause on N2-E only** (l.443). §5: "INDETERMINATE iff an unadjudicated pause stands
  on N2's reads"; the code ignores pauses on N2-S and N2-C, undeclared. (MINOR if "the guards decide nothing" is read to
  cover their pauses: an undeclared reading to register.)

### MINOR

- F3. The dose sentence's `[value]` is the pinned d_eq even when the read was taken at the point it merged into.
- F4. A Clock-cause NOT-RUN dated D_n itself is accepted; §7.4 makes D_n inclusive, so LOCK v1.0 can still be
  committed that day; the `date` field's meaning is undeclared.
- F5. `ganl --dose-map` accepts null rho, R and R_ell (§2.3's formula skipped); a string d_eq exits 1, not 2.
- F6. The sensitivity row's bootstrap contradicts PIN-n-12 (a matrix per point under `drop`); l.1998's identical
  branches.
- F7. A non-finite read counts as "not obtained": the arm becomes "incomplete" although every planned read exists;
  undeclared.
- F8. §4's per-arm statistics are incomplete: N1-P has |mean| only; no N2 arm gets a slope or floor
  (`n2_slope_points` is battery-only).
- F9. The oracle is not independent for Code's sentence forms; Appendix A is never checked (M26–M28).
- F10. Filled sentences are tested only for "no slot left" and 7.1's opening words (M29–M31).
- F11. The synthetic campaigns are symmetric: floor/P/E absolute values, N2's f mapping, N1-P's ±1 mapping, N4's 98%
  level and the slopes' d = 0 point are untested (M03, M04, M06–M10).
- F12. G-READ-n is always all PASS or all FAIL in the battery (M23, M32).
- F13. The dose and N2 ceilings are computed twice; P(+1) < L everywhere hides divergence (M19, M21).
- F14. Counters and the TAU/4 filter are tested only through copies; RD-SENSITIVITY's shift exceeds TAU and TAU/4
  alike; identity-bound and label-mass counters never asserted (M35–M37).
- F15. One-sided refusal tests (M14, M15); no map exactly 0.05 from a merge point (M12); CMD-GANL-REFUSE accepts
  whichever refusal fires, `d == REPO` never probed (M39); RD-REFUSE lacks inconsistent-cues and unbalanced-schedule
  cases (M33, M34).

### NOTE

N1 a stale raw date in OPEN's comment; N2 unused or battery-only helpers (`lock_names` never called: the lock's sha256
never checked; `kept_label`, `n2_slope_points`, `tau4_keep`, `label_mass_below`, `gleak_table`, `gread_table`
battery-only; `Campaign.nonfinite` unread); N3 secondaries rest on undeclared readings ((a) share of S picks; (c)
ordered cue pairs, N4 left out; (d) no floor of 20); N4 the hook resolves relative paths against the repository, checks
only the first positional argument, no os.open or subprocess cover; N5 the snapshot prunes ckpt/reports/verdicts at
any depth, `_barred` bars them at data/<unit>/ only; N6 `schema_module` hashes one file but never checks the imported
module is that file; N7 `fill` KeyError on an unknown route, `[a]` "not computed" inside an "answered" sentence; N8 in
the TAU/4 row an arm or point that loses every read STOPs (exit 4), a fully dropped N1-R cell makes L NaN and
certification silently False; N9 GATE_STAGES omits G-DATA and G-ACQ; N10 canonical `ganl` calls battery helpers; N11
the battery's canonical `run_ganl(None, None)` would recurse if its refusals moved; N12 `main()` prints
`sys.executable` and the draft hard-codes the absolute repository path; N13 `not-run` writes canonically without the
committed-blob check; N14 `write_once` check-then-write race; N15 `load_campaign` records the sha256 of a second read
and never verifies `capture_sha256`.

## 2. Round 1: the mutants on the frozen copy

The unmutated frozen copy first: 159/159 (`out1/BASE.out`; the runner printed its exit, 0, to the session). Then
M01–M20 and M21–M40, in two parts. The reviewer's columns are as written in its `mutants.tsv`; the last column is the
run's, with the first failing check of a killed mutant (the coverage and count lines left out; a text longer than 90
bytes is cut and marked "…").

| Id | Function | What it breaks | Reviewer: expected killer / suspected survivor | Result on the frozen copy |
|---|---|---|---|---|
| M01 | boot_key (l.125) | the bootstrap stream key of PIN-n-12 (the lock's "seed") becomes "n-boot:{arm}"; every CI is drawn from an undeclared stream | none: NUM-BOOT-DETERMINISM checks repeat-equality, cross-arm difference and range only; no check pins a matrix or a CI value / yes | SURVIVED |
| M02 | Est.excludes0 (l.145) | a CI whose lower bound is exactly 0 counts as excluding 0 (PIN-n-8) | BND-CI-LO-ZERO; N4-BND-CI-LO-ZERO / no | killed (fails=3; first: boundary: a CI with lower bound exactly 0 does not exclude 0 {'state': 'REPLICATED', 'conj…) |
| M03 | build_state (l.1976) | N1-V's slope and the 24 random slopes (the floor) are fitted without the d = 0 point (Δm(0) = 0), against OPEN-Q1's carried reading (a) | none on the reader path: NUM-SLOPE-INTERCEPT tests session_slopes alone; no RD-* outcome moves / yes | SURVIVED |
| M04 | build_state (l.2024) | the floor becomes the largest signed mean random slope instead of the largest \|mean slope\| (§4, C12) | none: every synthetic random direction has the same tiny slope; RD-NULL's tuple is unchanged (only its failing list moves, unchecked) / yes | SURVIVED |
| M05 | build_state (l.2016) | L(d) becomes the largest signed mean instead of max \|mean\| (§3 G-LEAK-n) | RD-NULL (N2 NULL becomes SHARED); RD-SPECIFIC (N2 SPECIFIC becomes SHARED) / no | killed (fails=3; first: reader path: nothing moves -> (NOT-REPLICATED, NOT-DETECTABLE, NULL, DEAD) ('NOT-REPLICATE…) |
| M06 | build_state (l.2029) | P(d) loses its absolute value, so a negative same-pole leak never enters max(L, P) | none: the synthetic N1-P mean is tiny and below L / yes | SURVIVED |
| M07 | build_state (l.2050) | E loses its absolute value; a negative sham mean lowers PASS's bar to mean > -\|E\| | none: the synthetic sham mean is about 0 / yes | SURVIVED |
| M08 | build_state (l.2035) | N2-E/S/C's f = 0.10 and f = 0.20 estimates are swapped, so N2 is decided on the f = 0.10 reads | none: in every RD campaign N2-E is certified at both f, or zero at both / yes | SURVIVED |
| M09 | build_state (l.2027) | P(+1) and P(-1) are swapped, so conjunct (iii) at +1 reads N1-P's -1 leak | none: the synthetic N1-P deltas do not depend on the dose / yes | SURVIVED |
| M10 | build_state (l.2049) | N4's m_told CI is 95% instead of §4's 98% (PCT98) | none expected: RD-PARTIAL's terminal INDETERMINATE holds at 95% (CI about [-0.02, +0.52], by hand); no check reads Est.level / yes (likely) | SURVIVED |
| M11 | build_state (l.2048) | m_told's sign flips (told-S counts -m, told-U +m) | RD-POSITIVE (N4 PASS becomes REVERSE); RD-SPECIFIC; RD-PAUSE / no | killed (fails=5; first: reader path: a campaign written with the schema's builders (7,360 reads, 136 cells, nothin…) |
| M12 | DoseMap._resolve (l.281) | a point exactly 0.05 (IEEE double) from a candidate is kept, not merged (§2.3 "within 0.05"); the reader then refuses a dose map the schema accepts | none: no map in NUM-DOSEMAP-SHAPES or NUM-DOSEMAP-SCHEMA's grid lies at a binary distance of exactly 0.05 / yes | SURVIVED |
| M13 | DoseMap._resolve (l.280) | merge ties go to the later candidate (PIN-n-14: the earlier) | NUM-DOSEMAP-SCHEMA (d_eq in (0.025, 0.05] folds into +d_20 instead of 0: the schema refuses, the analyzer does not) / no | killed (fails=2; first: the merge rule (PIN-n-14) agrees with the schema's dose_points on 400 maps (d_eq 0.003 to …) |
| M14 | DoseMap.problems (l.254) | only a d_20 above min(1, 2*d_eq) is refused; one below passes (e.g. DoseMap(0.4, 0.6)) | none: NUM-DOSEMAP-REFUSE's only d_20 case lies above (0.9 against 0.8) / yes | SURVIVED |
| M15 | DoseMap.problems (l.257) | only a rho above 0.3 is refused; a rho below 0.3 with a d_eq computed from it passes | none: NUM-DOSEMAP-REFUSE's only rho case is 0.30000000000000004 / yes | SURVIVED |
| M16 | certified (l.358) | certification on the signed mean instead of \|mean\| (§3 G-LEAK-n) | BND-NEG-CERT; DOSE-DET-NEG / no | killed (fails=3; first: a negative Δm(+1) beyond the ceiling is certified (\|mean\|); (i) fails, (ii)-(iii) hold, C…) |
| M17 | n1_outcome (l.401) | conjunct (ii) holds with the slope equal to its floor (PIN-n-7: strictly above) | BND-SLOPE-EQ-FLOOR / no | killed (fails=2; first: boundary: a slope equal to its floor does not exceed it ((ii) fails) {'state': 'REPLICATED…) |
| M18 | n1_outcome (l.407) | PARTIAL no longer requires the CI at +1 to exclude 0 | N1-NOTREP-ci+1; BND-CI-LO-ZERO / no | killed (fails=5; first: N1 NOT-REPLICATED failing ['ci+1'] {'state': 'PARTIAL', 'conjuncts': {'i': False, 'ii': Tr…) |
| M19 | dose_outcome (l.427) | dose's certification at d_eq takes P(+1) (OPEN-Q2's reading (b), undeclared) while the reported "ceiling" stays L(d_eq): the decision and the figure diverge | none: P(+1) = 0.04 < L = 0.05 in every literal state and the synthetic P is below L; BND-P-ABSENT checks the separately computed "ceiling" key / yes | SURVIVED |
| M20 | n2_outcome (l.442) | N1-P's incompleteness no longer makes N2 INDETERMINATE when the norm-matched point is +1 (OPEN-Q6) | N2-INDET-incomplete:N1-P / no | killed (fails=2; first: N2 INDETERMINATE by incomplete:N1-P where d_20 sits at +1 (shape b: the ceiling takes P(+1…) |
| M21 | n2_outcome (l.447) | N2's reported ceiling (the [c] slot) drops P(+1) at a +1 norm-matched point while cert_e and cert_v still use it | none: no check reads N2's "ceiling"; P(+1) < L everywhere / yes | SURVIVED |
| M22 | n4_outcome (l.473) | DEAD with an upper bound equal to 0.5 (§5: strictly below) | N4-BND-HI-EQ-DEAD / no | killed (fails=2; first: N4 boundary: an upper bound equal to 0.5 is not DEAD (strict <) {'state': 'DEAD', 'no_read…) |
| M23 | outcomes (l.489) | the tuple's G-READ-n coordinate reads valence at +1 instead of at d_eq (§3 G-ANL-n), and the dose label and sentence follow it | none: every outcomes() call in the battery has G-READ-n all PASS or all FAIL / yes | SURVIVED |
| M24 | label (l.561) | §0.6's conjunction becomes a disjunction: "answered" when N4 PASS or G-READ-n PASS | TUP-T7; TUP-T10; TUP-T2 / no | killed (fails=5; first: tuples T2: 1051/1921 evaluations: the set equals the oracle's (§5's verbatim cells read f…) |
| M25 | sentence_dose (l.594) | NOT-DETECTABLE's not-answered branch keyed on N4 instead of G-READ-n (A.5 and A.6 swapped) | TUP-T2; TUP-T10 / no | killed (fails=3; first: tuples T2: 1601/1921 evaluations: the set equals the oracle's (§5's verbatim cells read f…) |
| M26 | C_N4 (l.543) | N4's DEAD sentence states the bar as 0.05 nats instead of §5's 0.5 | none: the oracle takes C_N4 from the module; no check compares Code's forms with Appendix A / yes | SURVIVED |
| M27 | CONJUNCT_TEXT (l.553) | conjunct (ii)'s name reads "below its floor" | none: SENT-FAILING-PARTIAL and SENT-FAILING-NOTREP compare against CONJUNCT_TEXT itself / yes | SURVIVED |
| M28 | NOT_RUN_CAUSES (l.97) | no-arm:cap's reason reads "before a PI stop", identical to no-arm:pi-stop's | none: NR-no-arm:cap compares with the constant itself; there is no distinctness check / yes | SURVIVED |
| M29 | fill (l.2093) | N1's [z] slot carries the valenced slope instead of the floor | none: RD-FILLED checks only that no slot is left and 7.1's opening words / yes | SURVIVED |
| M30 | fill (l.2102) | the dose sentence's [value] carries d_20 instead of d_eq | none: RD-FILLED as above / yes | SURVIVED |
| M31 | fill (l.2117) | N4 REVERSE's [-e] prints +E | none: no battery path fills a REVERSE sentence / yes | SURVIVED |
| M32 | sentence_set_filled (l.2132) | N1 NOT-REPLICATED's §0.6 label reads G-READ-n at d_eq instead of at +1 | none: RD-GREAD and RD-FILLED have G-READ-n all FAIL or all PASS / yes | SURVIVED |
| M33 | _cross_checks (l.1913) | a session whose cues or present order differ between reads is accepted (refused only at three distinct variants) | none: RD-REFUSE has no inconsistent-cues case / yes | SURVIVED |
| M34 | _cross_checks (l.1925) | the 80 S / 80 U schedule check never fires | none: RD-REFUSE's zone case is refused by the per-session check first / yes | SURVIVED |
| M35 | counters (l.2156) | the "fidelity exceedances at TAU/4" counter counts exceedances at TAU | none: RD-SENSITIVITY's 40 shifted reads (rel about 0.23) exceed TAU and TAU/4 alike / yes | SURVIVED |
| M36 | counters (l.2160) | the label-mass counter counts a mass of exactly 0.20 (PIN-n-17: below .20) | none: CNT-LABEL-MASS tests label_mass_below, which counters does not call; every synthetic mass is 0.5 / yes | SURVIVED |
| M37 | tau4_drop (l.2172) | the TAU/4 sensitivity row drops reads above TAU instead of above TAU/4 | none: RD-SENSITIVITY's shifted reads exceed both; NUM-TAU4-DROP tests tau4_keep, not tau4_drop / yes | SURVIVED |
| M38 | secondaries (l.2201) | secondary (c) withholds a group's mean at exactly 20 events (decidable-n floor 20) | none: no synthetic group has n = 20 (54/106/160 on the 160-session arms, 336/624/960 on N1-R) / yes | SURVIVED |
| M39 | run_ganl (l.2571) | an --out equal to the repository root is accepted and the artifact written at the root | none: CMD-GANL-REFUSE probes data/n, a subdirectory / yes | SURVIVED |
| M40 | not_run_reason (l.747) | the premature-date refusal applies to no-arm causes instead of Clock causes | NR-REFUSE-PREMATURE / no | killed (fails=2; first: NOT-RUN record refused (PREMATURE) no exception) |

## 3. The dispositions (every finding and note)

| Item | Disposition | Where (fixed draft) | The check that now kills it |
|---|---|---|---|
| F1 | Fixed. A steered arm is usable only when the shadows of every session it reads are present and finite; otherwise `shadow:<arm>`; no exception. `_cross_checks` refuses an absent shadow. | `build_state`, `_cross_checks` | RD-SHADOW; RD-REFUSE (shadow-absent) |
| F2 | Fixed: a pause on N2-S's or N2-C's reads makes N2 INDETERMINATE (§5, n:140: "an unadjudicated pause stands on N2's reads"). A pause on N1-V's or N1-R's reads, or on N1-P's where d_20 sits at +1, alone leaves N2 evaluated: the block's Q6 reading, "as written", now said in those words in the code's OPEN-Q6 text and tested. | `n2_outcome` | N2-INDET-pause:N2-S, -N2-C; N2-NOT-PAUSED-BY-N1 |
| F3 | Fixed: where §2.3's merge moved d_eq, the dose sentence prints d_eq's value and the point read beside it (VALUE_MERGED, a new Code form under OPEN-Q8). | `value_text` | RD-MERGED-DEQ |
| F4 | Fixed, PIN-n-21: a Clock cause is refused on or before D_n (inclusive). | `not_run_reason` | NR-REFUSE-PREMATURE |
| F5 | Fixed: `ganl --dose-map` takes exactly the five figures, each a finite JSON float; every refusal before the battery is named (`ganl_precheck`). | `dose_map_input_problems`, `ganl_precheck` | CMD-GANL-REFUSE (18 refusals by name, one pass) |
| F6 | Fixed in the reader (a matrix per statistic's session count in the TAU/4 row; the identical branches gone); PIN-n-12's text amended to say so. | `build_state`, PINS | RD-SENSITIVITY |
| F7 | Fixed, PIN-n-20: a non-finite read is present but no read; its arm is not usable, cause `nonfinite:<arm>`. | `Campaign.usable`, `_causes` | RD-NONFINITE |
| F8 | Fixed: N1-P's signed estimates, N2's per-arm slopes and N2's floor are computed and returned with `build_state`'s figures (OPEN-Q9's points); the `verdicts` command, not in this BUILD, reports them. | `build_state` | RD-ASYM (N2 slope) |
| F9 | Fixed: Code's 31 forms pinned by digest (CODE_FORMS_SHA256), distinct, declared slots only. Appendix A checked against the code by tool (§5). | `code_forms`, `_bt_sentences` | SENT-CODE-FORMS |
| F10 | Fixed: the filled sentences against the battery's own literal text, figure for figure, for REPLICATED, DETECTABLE (plain and merged), SHARED, SPECIFIC, PARTIAL, PASS, REVERSE and N4's terminal INDETERMINATE. | `_bt_reader` | RD-FILLED-FIGURES, RD-FILLED-FORMS, RD-MERGED-DEQ |
| F11 | Fixed: an asymmetric campaign read to a hand computation (polyfit slopes with the d = 0 point, floor as max \|mean slope\|, L and P as \|mean\| at their own points, ceilings, E by f, N2's per-f n and SD (added after the values-check), N2's slope, E_sham, m_told's 98% CI). | `_bt_reader` | RD-ASYM |
| F12 | Fixed: mixed G-READ-n states, each label and the coordinate reading its own cell. | `_bt_reader` | RD-GREAD-MIXED |
| F13 | Fixed: each ceiling is computed once (`above`, one `ceiling` call per site); the reported ceiling is the one certification used. | outcome layer | RD-ASYM, RD-MERGED |
| F14 | Fixed: the counters through `counters` (TAU/4 apart from TAU, the identity bound, label mass strictly below .20); the TAU/4 row through `tau4_drop` and `build_state`, a shadow's exceedance dropping its session everywhere. `tau4_keep` (battery-only) removed. | `counters`, `_bt_reader` | CNT-COUNTERS, RD-SENSITIVITY |
| F15 | Fixed: two-sided dose-map refusals; the merge rule at a decimal distance of exactly 0.05; `--out` at the repository root; RD-REFUSE with inconsistent cues, an 81/79 schedule, capture bytes and absence, absent shadows. | battery | NUM-DOSEMAP-REFUSE, NUM-MERGE-EDGE, CMD-GANL-REFUSE, RD-REFUSE |
| N1 | Fixed: the OPEN register cites the committed block (2026-11-16). | OPEN | STR-PINS (registered = cited) |
| N2 | `lock_names` is for the `verdicts` command (not in this BUILD); `kept_label`, `gleak_table`, `gread_table` likewise; `n2_slope_points` now used by the reader; `tau4_keep` removed; `label_mass_below` now used by `counters`; `Campaign.nonfinite` now read. | — | — |
| N3 | Registered as PIN-n-22: secondaries (a) and (c) readings; (a), (c) and (d) report at n ≥ 20 (d's floor added). | `secondaries` | RD-SECONDARY, RD-SECONDARY-FLOOR |
| N4 | Fixed: the hook resolves a relative path as the OS does (the working directory) and, for a process's arguments, against the repository too; checks file= / path= / args= / cwd= keywords; covers os.open and subprocess.run; its probes name absent paths only, and data/mf3 by string or through a process that reads no argument. | `_norm`, `_Hook` | STR-OPEN-HOOK |
| N5 | Fixed: the snapshot prunes exactly the directories `_barred` bars. | `_bt_snapshot` | STR-NO-CANONICAL-WRITE |
| N6 | Fixed: the imported schema module must be the hashed file. | `schema_module` | — (no battery case: an import from elsewhere cannot be staged without a second file) |
| N7 | Fixed: a route other than A or B STOPs; a dose sentence that calls the state readable without an AUC STOPs. | `fill` | RD-GREAD-MIXED |
| N8 | Fixed in the reader: an arm the TAU/4 row empties is `tau4-emptied`, never a STOP or NaN. | `build_state` | — |
| N9 | Fixed: GATE_STAGES lists §3's pre-lock gates, G-DATA and G-ACQ included. | constants | — |
| N10 | Fixed: the reach helpers the canonical path calls are renamed out of the `_bt` prefix (`map_reach`, `map_reach_by_hand`), and so is the literal-state builder `map_reach` calls (`literal_state`, formerly `_bt_state`; renamed after the values-check found it still on the canonical path). | — | NUM-REACH-CLASS |
| N11 | Fixed: `ganl_precheck` holds every pre-battery refusal; the battery tests it, never `run_ganl`. | `ganl_precheck` | CMD-GANL-REFUSE |
| N12 | Kept: `main()` prints `sys.executable` (the house form of m_analyze and p_analyze; raws carry it as `<repo>/…`). The absolute repository path is the scratch draft's only; the committed file derives it from `__file__`. | — | — |
| N13 | Fixed: `not-run` writes its output of record only from the committed analyzer, and a --out only outside the repository (`not_run_precheck`). | `not_run_precheck` | CMD-NOTRUN-REFUSE |
| N14 | Fixed: write-once links a private temporary file into place (os.link fails if the name exists). | `write_once` | CMD-NOTRUN |
| N15 | Fixed in the reader: the cell's hash is of the bytes parsed; the capture file's bytes are checked against `capture_sha256`. | `load_campaign` | RD-REFUSE (capture, capture-absent) |

## 4. Round 2: the mutants on the amended draft

The base: the amended draft, sha256 `cc0fa5b1…3ea8` (171/171). It is the fixed draft with the first values-check
pass's three code findings applied: N2's per-f n and SD checked in RD-ASYM; `_bt_state` renamed `literal_state`, with
its docstring; and the battery's quotations of §5 made verbatim, with the N1-P pause case added. It also carries four
docstring edits: the `not-run` usage text, `State`'s, `map_reach_by_hand`'s and `literal_state`'s. Run in three
parts: R01–R17, R18–R34, and R35–R50 with R07b.

**A first run of round 2,** on the fixed draft before the values-check (sha256 `fc479b81…ef5f`, 171/171), killed 50 of
its 51 runs, and R07 survived. The values-check showed R07 was not equivalent. The loop it edits computes each
estimate from its own reads (`tgt[f]` from `fv[f]`), but it also sets `fig["n"]` and `fig["sd0"]` by label, so the
swap exchanges N2's per-f counts and SDs. No check could see that: no check read N2's per-f SDs, and the one per-f
count a check read (RD-SENSITIVITY's) is equal at both f. The check added for it kills it: R07's failing sub-check is
"N2's per-f n and SD (ddof 0)" (`out3/R07.out`; the table's cell is cut before it).

| Id | What it breaks | Expected killer | Result on the amended draft |
|---|---|---|---|
| R01 | M01: the bootstrap stream key | NUM-BOOT-DETERMINISM | killed (fails=2; first: the resample matrix is PIN-n-12's stream, re-derived literally from its words for N1-V, N1…) |
| R02 | M03: N1-V slope without d = 0 | RD-ASYM | killed (fails=2; first: reader path (F11): an asymmetric campaign -- a random direction with a negative slope and …) |
| R03 | M04: floor signed | RD-ASYM | killed (fails=2; first: reader path (F11): an asymmetric campaign -- a random direction with a negative slope and …) |
| R04 | M05: L signed | RD-ASYM, RD-NULL | killed (fails=6; first: reader path: nothing moves -> (NOT-REPLICATED, NOT-DETECTABLE, NULL, DEAD) ('NOT-REPLICATE…) |
| R05 | M06: P loses abs | RD-ASYM | killed (fails=3; first: reader path: R_ell 50 merges +d_20 into +1 -> 6,240 reads; N2's norm-matched point is +1, …) |
| R06 | M07: E loses abs | RD-ASYM | killed (fails=2; first: reader path (F11): an asymmetric campaign -- a random direction with a negative slope and …) |
| R07 | M08: N2 f labels swapped (first loop) | RD-ASYM | killed (fails=2; first: reader path (F11): an asymmetric campaign -- a random direction with a negative slope and …) |
| R08 | M09: P(+1)/P(-1) swapped | RD-ASYM | killed (fails=3; first: reader path: R_ell 50 merges +d_20 into +1 -> 6,240 reads; N2's norm-matched point is +1, …) |
| R09 | M10: N4 at 95% | RD-ASYM | killed (fails=2; first: reader path (F11): an asymmetric campaign -- a random direction with a negative slope and …) |
| R10 | M12: merge strict | NUM-MERGE-EDGE | killed (fails=2; first: the merge rule at a decimal distance of exactly 0.05 (IEEE decides): 0.45 folds into +1/2 …) |
| R11 | M14: d_20 refused only above | NUM-DOSEMAP-REFUSE | killed (fails=2; first: the dose map refuses d_20 above or below min(1.0, 2.0 * d_eq), a non-positive or nonfinite…) |
| R12 | M15: rho refused only above | NUM-DOSEMAP-REFUSE | killed (fails=2; first: the dose map refuses d_20 above or below min(1.0, 2.0 * d_eq), a non-positive or nonfinite…) |
| R13 | M19: dose certified against P(+1) | RD-ASYM | killed (fails=2; first: reader path (F11): an asymmetric campaign -- a random direction with a negative slope and …) |
| R14 | M21: N2 reported ceiling drops P | RD-MERGED | killed (fails=2; first: reader path: R_ell 50 merges +d_20 into +1 -> 6,240 reads; N2's norm-matched point is +1, …) |
| R15 | M23: the coordinate reads +1 | RD-GREAD-MIXED | killed (fails=2; first: reader path (F12): G-READ-n FAIL at d_eq only -> the coordinate FAIL, N1's label answered,…) |
| R16 | M26: a Code form (C_N4 DEAD) changed | SENT-CODE-FORMS | killed (fails=2; first: Code's 31 sentence forms (OPEN-Q8) are pinned by digest (CODE_FORMS_SHA256), pairwise dist…) |
| R17 | M27: CONJUNCT_TEXT changed | SENT-CODE-FORMS | killed (fails=2; first: Code's 31 sentence forms (OPEN-Q8) are pinned by digest (CODE_FORMS_SHA256), pairwise dist…) |
| R18 | M28: two NOT-RUN reasons identical | SENT-CODE-FORMS | killed (fails=2; first: Code's 31 sentence forms (OPEN-Q8) are pinned by digest (CODE_FORMS_SHA256), pairwise dist…) |
| R19 | M29: [z] carries the slope | RD-FILLED-FIGURES | killed (fails=3; first: reader path: the filled set (REPLICATED, DETECTABLE, SHARED, PASS) equals the battery's li…) |
| R20 | M30: [value] carries d_20 | RD-FILLED-FIGURES | killed (fails=2; first: reader path: the filled set (REPLICATED, DETECTABLE, SHARED, PASS) equals the battery's li…) |
| R21 | M31: REVERSE prints +E | RD-FILLED-FORMS | killed (fails=2; first: reader path: Code's forms filled, against the battery's literal text: N2 SPECIFIC with its…) |
| R22 | M32: N1 label reads d_eq | RD-GREAD-MIXED | killed (fails=2; first: reader path (F12): G-READ-n FAIL at d_eq only -> the coordinate FAIL, N1's label answered,…) |
| R23 | M33: inconsistent cues accepted | RD-REFUSE | killed (fails=2; first: reader path refuses: a file no cell names; a stage identity that differs between cells; a …) |
| R24 | M34: 80/80 check never fires | RD-REFUSE | killed (fails=2; first: reader path refuses: a file no cell names; a stage identity that differs between cells; a …) |
| R25 | M35: TAU/4 counter counts TAU | CNT-COUNTERS | killed (fails=2; first: reader path (F14): the TAU/4 row (PIN-n-16) drops the 40 reads above TAU/4 at +1 (none abo…) |
| R26 | M36: label mass at exactly .20 counted | CNT-LABEL-MASS, CNT-COUNTERS | killed (fails=3; first: the label-mass counter (PIN-n-17) counts reads strictly below .20 (0.19 counts; 0.20 and 0…) |
| R27 | M37: TAU/4 row drops above TAU | RD-SENSITIVITY | killed (fails=2; first: reader path (F14): the TAU/4 row (PIN-n-16) drops the 40 reads above TAU/4 at +1 (none abo…) |
| R28 | M38: (c) withholds at exactly 20 | RD-SECONDARY-FLOOR | killed (fails=2; first: reader path: secondary (c) reports a group's mean at exactly 20 events (the decidable-n fl…) |
| R29 | M39: ganl --out at the repository root | CMD-GANL-REFUSE | killed (fails=2; first: ganl's 18 refusals before any battery run, each by name (a canonical run whose bound files…) |
| R30 | F1: shadows of all 160 sessions for N1-R | RD-SHADOW | killed (fails=2; first: reader path: a non-finite shadow at run 100 -> N1, dose and N2 INDETERMINATE, N1's causes …) |
| R31 | F1: the shadow guard removed | RD-SHADOW | killed (fails=3; first: reader path: group raised AnlStop: STOP: Δm of N1-P\|valence\|+1 at neu_b3/100 without a fi…) |
| R32 | PIN-n-20: nonfinite named incomplete | RD-NONFINITE, RD-SHADOW | killed (fails=3; first: reader path: one non-finite read in N1-V at +1 -> N1-V not usable (PIN-n-20) -> N1 INDETER…) |
| R33 | F2: N2 pauses on N2-E only | N2-INDET-pause:N2-S/C | killed (fails=3; first: N2 INDETERMINATE by pause:N2-S (§5, n:140: 'an unadjudicated pause stands on N2's reads';…) |
| R34 | F3: merged point not shown | RD-MERGED-DEQ | killed (fails=2; first: reader path: d_eq ≈ 0.52 merged into +1/2 -> the dose question reads +1/2, and its sente…) |
| R35 | F5: ints and bools accepted as map figures | CMD-GANL-REFUSE | killed (fails=2; first: ganl's 18 refusals before any battery run, each by name (a canonical run whose bound files…) |
| R36 | F5: extra map keys accepted | CMD-GANL-REFUSE | killed (fails=2; first: ganl's 18 refusals before any battery run, each by name (a canonical run whose bound files…) |
| R37 | N14: write-once accepts other bytes | CMD-NOTRUN | killed (fails=2; first: not-run writes N-pod_NOT-RUN.json once (written, then identical), refuses other bytes (wri…) |
| R38 | N4: os.open not hooked | STR-OPEN-HOOK | killed (fails=2; first: the battery's hook refuses, before any filesystem call or process start, 9 probes: opens (…) |
| R39 | N4: keyword paths not checked | STR-OPEN-HOOK | killed (fails=2; first: the battery's hook refuses, before any filesystem call or process start, 9 probes: opens (…) |
| R40 | N13: not-run --out at the repository root | CMD-NOTRUN-REFUSE | killed (fails=2; first: not-run's refusals before any write: the output of record only from the committed analyzer…) |
| R41 | N2 certifies V at the f = 0.10 point | RD-ASYM | killed (fails=7; first: N2 NULL (N2-NULL) {'state': 'SPECIFIC', 'point': 0.6666666666666666, 'ceiling': 0.05, 'cer…) |
| R42 | N7: a readable dose sentence without AUC | RD-GREAD-MIXED | killed (fails=2; first: reader path (F12): G-READ-n FAIL at d_eq only -> the coordinate FAIL, N1's label answered,…) |
| R43 | N7: an unknown route | RD-GREAD-MIXED | killed (fails=2; first: reader path (F12): G-READ-n FAIL at d_eq only -> the coordinate FAIL, N1's label answered,…) |
| R44 | identity counter inverted | CNT-COUNTERS | killed (fails=2; first: reader path (F14): the TAU/4 row (PIN-n-16) drops the 40 reads above TAU/4 at +1 (none abo…) |
| R45 | PIN-n-21: Clock record on D_n accepted | NR-REFUSE-PREMATURE | killed (fails=2; first: NOT-RUN record refused (PREMATURE) no exception) |
| R46 | F15: canonical uncommitted not refused | CMD-GANL-REFUSE | killed (fails=2; first: ganl's 18 refusals before any battery run, each by name (a canonical run whose bound files…) |
| R47 | an absent shadow not refused | RD-REFUSE (shadow-absent) | killed (fails=2; first: reader path refuses: a file no cell names; a stage identity that differs between cells; a …) |
| R48 | N15: capture bytes unchecked | RD-REFUSE (capture) | killed (fails=2; first: reader path refuses: a file no cell names; a stage identity that differs between cells; a …) |
| R49 | a Code form (VALUE_MERGED) changed | SENT-CODE-FORMS, RD-MERGED-DEQ | killed (fails=3; first: Code's 31 sentence forms (OPEN-Q8) are pinned by digest (CODE_FORMS_SHA256), pairwise dist…) |
| R50 | N1-P not read for N2 at +1 | N2-INDET-incomplete:N1-P | killed (fails=2; first: N2 INDETERMINATE by incomplete:N1-P where d_20 sits at +1 (shape b: the ceiling takes P(+1…) |
| R07b | M08 re-targeted: N2 reads mapped to the other f | RD-ASYM | killed (fails=2; first: reader path (F11): an asymmetric campaign -- a random direction with a negative slope and …) |

## 5. Appendix A against the code

`tools/appendix_check.py` (Code's scratch) imported the fixed draft (sha256 `fc479b81…ef5f`) and read the committed
block `results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md`. It compared each italic span of Appendix A with the
form of that name in `code_forms()`. The forms have not changed since: the committed file's battery passes
SENT-CODE-FORMS against the same pinned digest. Its output, whole:

```
MATCH A.1 C_N1_PARTIAL
MATCH A.2 C_N1_NOT_REPLICATED
MATCH A.3 C_N1_INDET
MATCH A.3 C_DOSE_INDET
MATCH A.3 C_N2[INDETERMINATE]
MATCH A.3 C_N4[NO-READ]
MATCH A.4 C_NOT_RUN
MATCH A.4 NOT_RUN_CAUSES[clock:no-box]
MATCH A.4 NOT_RUN_CAUSES[clock:gate-stopped]
MATCH A.4 NOT_RUN_CAUSES[clock:pi-declined]
MATCH A.4 NOT_RUN_CAUSES[clock:not-locked]
MATCH A.4 NOT_RUN_CAUSES[no-arm:pi-stop]
MATCH A.4 NOT_RUN_CAUSES[no-arm:gver-stop]
MATCH A.4 NOT_RUN_CAUSES[no-arm:cap]
MATCH A.5 C_DOSE_ND_NOT_READABLE
MATCH A.6 C_DOSE_ND_READABLE_N4
MATCH A.7 C_N2[SPECIFIC]
MATCH A.7 C_N2[SHARED]
MATCH A.7 C_N2[NULL]
MATCH A.8 C_N4[PASS]
MATCH A.8 C_N4[REVERSE]
MATCH A.8 C_N4[DEAD]
MATCH A.8 C_N4[INDETERMINATE]
MATCH A.9 CONJUNCT_TEXT[i]
MATCH A.9 CONJUNCT_TEXT[iv]
MATCH A.9 CONJUNCT_TEXT[ci+1]
MATCH A.9 CONJUNCT_TEXT[ii]
MATCH A.9 CONJUNCT_TEXT[iii]
forms in the code: 31; in Appendix A: 28; compared: 28; differing: 0
in the code, not in Appendix A: ['ROUTE_TEXT[A]', 'ROUTE_TEXT[B]', 'VALUE_MERGED']
```

The three forms in the code that Appendix A does not list go to the seat with the BUILD entry, under OPEN-Q8: the two
fills of §5's route slot (in the draft at the block's time, unlisted there), and VALUE_MERGED, the dose sentence's
[value] when §2.3's merge moved d_eq (new since, F3).

## 6. The committed bytes against the mutation-tested draft

`diff` of the amended draft (sha256 `cc0fa5b1…3ea8`) against the committed `scripts/n_analyze.py`, whole. The old
line's absolute repository path is shown as `<repo>`. Two places change. The repository line is derived from
`__file__`. OPEN-Q6's register text is corrected after the second values-check pass: the block's Q6 already carried
the reading that a pause on the N1 arms leaves N2 evaluable, "as written". No check reads that string's content.

```
49c49
< REPO = Path("<repo>")   # DRAFT: Path(__file__).resolve().parents[1] in the tree
---
> REPO = Path(__file__).resolve().parents[1]                     # scripts/n_analyze.py -> the repository
1676,1677c1676
<                "while a pause on those N1 arms alone leaves N2 evaluated (a reading added since the block, for the "
<                "seat); a pause on N4's reads (N4)",
---
>                "while a pause on those N1 arms alone leaves N2 evaluated, as written; a pause on N4's reads (N4)",
```
