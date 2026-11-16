# n_analyze.py, the `verdicts` command: the blind values-check, three passes (PI date 2026-11-16)

Code's raw for the entry `n package — scripts/n_analyze.py, the verdicts command`. Three blind values-checkers, each a
subagent of this session under a brief quoting the list of record v2's items 1–5 and allowing no Python, checked the
entry and the review raw against their sources, claim by claim.
- The first pass checked the first drafts.
- Each later pass checked the drafts as revised after the pass before it, and whether each of that pass's
  dispositions was carried and is true.

The first two passes each reported one observation outside their claims, and each became a change with a battery
run and a mutation run of its own (the review raw's §5):
- the first, the write order (a code change);
- the second, a battery gap (a battery case).

Each report is reproduced whole, its headings moved down two levels, and is followed by Code's dispositions. The first
pass's report is the file it wrote. The second's and third's are their hand-back messages, taken from the subagents'
transcripts by script (their Write tools refused report files). The checkers write SCRATCH for Code's scratch folder
and REPO for the repository.

## 1. The first pass: the checker's report, whole

### Values-check, pass 1 (blind): the `verdicts` entry draft and its review raw

Checker: a blind values-checker (a subagent). Tools used: `shasum -a 256` + `cut`, `diff`, `/usr/bin/grep`, `sed`,
`awk`, `perl` occurrence counts, `git show <rev>:<path>`, `git log --format`, `git show --name-only`, `git ls-files`.
No Python or other interpreter ran on the code; nothing under `data/` was touched; nothing in the repository was edited.
Working files went to SCRATCH/v2/vc/pass1_tmp (removed at the end). Paths: SCRATCH = the n9 scratch directory,
REPO = the repository. "final" = SCRATCH/v2/final/n_analyze.py; "frozen" = SCRATCH/v2/review/n_analyze.verdicts-under-review.py;
"base2" = SCRATCH/v2/review/n_analyze.round2-verdicts-base.py.

#### Digests (computed by tool, abbreviated with `cut`)

| File | sha256 | Abbrev. | Text says |
|---|---|---|---|
| final | `5187089219eb0a7709078205fcb0bf88afab1a27e926eb8056a06c64e6b683a6` | `51870892…83a6` | `FINAL_SHA` (placeholder) |
| frozen | `0b555476…843c` | | `0b555476…843c` ✓ |
| base2 | `b5328332…78c2` | | `b5328332…78c2` ✓ |
| `git show 2822721:scripts/n_analyze.py` (= HEAD's) | `4f63903f…5d73` | | ✓ |
| `git show 14e65d8:valence_core/n/schema.py` (= HEAD's, = working tree's) | `4bed3f9a…4665` | | ✓ |
| REPO/PROPOSAL-n-bk-reconciliation-v0_2.md | `30a3d0f5…04f4` | | ✓ |

#### Claims

##### Text 1: SCRATCH/v2/raw/entry.md

1. l.1, dated 2026-11-16. CONFIRMED (the session's date; the review raw carries the same PI date).
2. l.1, `verdicts` is PROPOSAL-n v0.2 §8 step 15. CONFIRMED (proposal l.159, step 15: "`PROPOSAL-n N-pod — VERDICTS` … `— secondary DVs`").
3. l.1–2, on n-build's `n-report-v1` and `n-gread-v1` at `14e65d8`. CONFIRMED (schema at 14e65d8 l.994–995).
4. l.2–3, it gives VERDICTS and secondary DVs, or the NOT-RUN derived from the stage report. CONFIRMED (final `run_verdicts` l.4220–4321).
5. l.3, "Its battery passes 185/185". UNVERIFIABLE for the committed bytes until the run of record. Consistent: final `EXPECTED_CHECKS = 185` (l.866); base2 ran 185/185 (SCRATCH/runs/v2r2_2.out); the §6 diff changes no check, and the per-arm cases' new strings are what the schema's refusal prints (schema l.1135 → `_err_where` l.2925–2933 → "SchemaError at report.per_arm.N2-C").
6. l.3, "reviewed blind". UNVERIFIABLE (the reviewer's brief is not a file). The review of the frozen copy exists (review/findings.md).
7. l.3–4, 65 of 66 mutants killed; the survivor is equivalent. CONFIRMED: 65 outputs in out_r2 have ≥ 2 `[FAIL]` lines and N/185 < 185, which exits 1 (final l.3612, l.4356). M08.out is 185/185 with no FAIL. The equivalence is the schema's per_arm rule plus the cells check (see 58).
8. l.4–5, four PINs (PIN-n-23 to 26) and an amendment to PIN-n-16 are Code's readings, flagged. CONFIRMED (final PINS l.1644–1689; 2822721 has PIN-n-7…22 and the shorter PIN-n-16).
9. l.5, model-free: nothing ran on a model or on the box, and no stage ran. UNVERIFIABLE (session conduct). Consistent: the module imports numpy and the standard library; every run in the sources is `--selftest`.
10. l.6, `4f63903f…5d73` at `2822721`. CONFIRMED.
11. l.6–7, still pinned to the schema at `14e65d8` (`4bed3f9a…4665`). CONFIRMED (final l.1882).
12. l.7, binds PROPOSAL-n v0.2 by sha256 (`30a3d0f5…04f4`). CONFIRMED (final l.60).
13. l.8–11, the four commands and their options, with `verdicts` new. CONFIRMED (final `main` l.4331–4353; at 2822721 only `--selftest`, `ganl` and `not-run` exist).
14. l.13–14, run of record: 185/185, all 188 coverage ids reached, exit 0. UNVERIFIABLE (not yet run). Consistent: v2r2_2.out on base2 shows 185/185 with 188 ids, and the §6 diff touches neither `EXPECTED_CHECKS` nor `_REQ`.
15. l.14–15, the selftest raw's name. UNVERIFIABLE (the file does not exist yet; the name follows `2026-11-16_n-analyze_build_selftest.txt`'s form).
16. l.17, it reads the stage report through the schema's `check_report`. CONFIRMED (l.4237).
17. l.19, it refuses a PAUSE. CONFIRMED (l.4239–4241).
18. l.20, it refuses a report that is not a campaign of PROPOSAL-n v0.2. CONFIRMED (l.4243–4244).
19. l.21, it refuses a lock that is not the identity's `lock_sha256`. CONFIRMED (l.4250).
20. l.21–22, it refuses a lock that does not name this analyzer's sha256. CONFIRMED (l.4254).
21. l.22, it refuses a lock that does not say it is LOCK-n v1.0. CONFIRMED (`lock_route` l.3945).
22. l.22, "or that states no direction of record (PIN-n-26)". IMPRECISE: `lock_route` also refuses two route lines, and a route line naming neither A nor B (l.3947–3950; VD-REFUSE lock-two-routes and lock-route-C). Fix: "or that does not state exactly one direction of record, Route A or Route B, as a whole line (PIN-n-26)".
23. l.16–22, the list under "The checks before anything is written". IMPRECISE: as a list of what is checked before any write, it leaves out three refusals:
    - the date, which is the first refusal (l.4234);
    - the precheck (l.4192–4217): of record, a lock, report, G-READ-n artifact or cosines file outside the repository or not committed as it stands, and any `--out` inside the repository;
    - a report with no cell beside a non-empty campaign directory (l.4267–4268).

    Fix: add them, or introduce the list as "Among its refusals".
24. l.24–26, it binds the report to the cells on disk: the identity, every cell by both shas and record count, the counters and the cap's used time against the records, and the launches and pauses. CONFIRMED (`report_problems` l.4006–4063; `camp.cells` holds both shas and the record count, l.2001–2002).
25. l.27–28, PI-STOP, G-VER-STOP or the cap with no arm complete gives NOT-RUN `no-arm:pi-stop`, `no-arm:gver-stop` or `no-arm:cap`. CONFIRMED (l.3935, l.4270).
26. l.28–29, the NOT-RUN is bound to the report, its end state, the STOP record, the lock and the schema module. CONFIRMED (l.4273–4275; the VD-NOTRUN-* check).
27. l.30, otherwise it binds G-READ-n's artifact to the campaign (PIN-n-25). CONFIRMED (l.4280–4285).
28. l.30–31, it computes the state, the outcomes and the filled sentences on the reader path, with the route from the lock. CONFIRMED (l.4256, l.4288–4291).
29. l.31–32, it writes, write-once, the secondary DVs and then VERDICTS. CONFIRMED (l.4299, l.4318).
30. l.33, VERDICTS carries the tuple, the outcomes, the sentences and §4's figures. CONFIRMED (l.4301–4303).
31. l.34, it carries G-LEAK-n's and G-READ-n's tables. CONFIRMED (`gleak`, `gread.table`).
32. l.35, it carries both counter forms. CONFIRMED (`counters.records`, `counters.report`).
33. l.36, it carries §0.4's exposure realised (PIN-n-23). CONFIRMED (`exposure`).
34. l.37, it carries the TAU/4 sensitivity row (PIN-n-16). CONFIRMED (`sensitivity`).
35. l.38, it carries the cosines when G-VEC's file is given. CONFIRMED (`cosines`, null without `--gvec`).
36. l.39, it binds every input, and the secondary, by sha256. CONFIRMED: the lock, the report, the artifact, the cosines source, the schema module, the proposal, the analyzer, the cells and the secondary are each bound by sha256.
37. l.40, one outcome per unit: neither output is written beside the other, in either command. CONFIRMED (`one_outcome` l.2992–2997, called at l.2987, l.4276 and l.4297; VD-ONE-OUTCOME).
38. l.41, "What it prints: one line, with the tuple and each output's name and sha256, and no margin". IMPRECISE: `main` prints the INVOCATION line first (l.4333) and then `verdicts_line` (l.4324–4328), which also says how each output was written. Neither line carries a margin ✓. Fix: "Besides the INVOCATION line every command prints, one line: the tuple, and each output's name, how it was written and its sha256; no margin".
39. l.42, a schema refusal prints its field path only. CONFIRMED (`_err_where` l.2925–2933; the battery's schema-blind check, l.3523–3524). It prints to stderr, as "REFUSED: <what>: SchemaError at <path>".
40. l.43–44, the review raw's name. UNVERIFIABLE (the file is still to be written).
41. l.45, the reviewer read the draft frozen at `0b555476…843c`. CONFIRMED (the frozen copy's hash; findings.md l.12).
42. l.45–46, the reviewer was a subagent of this session, under a brief quoting the list of record v2's items 1–5. UNVERIFIABLE.
43. l.46–47, it returned production findings F1–F12 and battery findings B1–B4. CONFIRMED (findings.md).
44. l.47, 38 mutants, with predictions of 10 killed and 28 surviving. CONFIRMED (mutants/mutants.tsv: 38 rows; "no" ×10, "yes" ×27, "yes (equivalent)" ×1).
45. l.47–48, nothing in the production path gives a wrong output on what the runner and probe write today. CONFIRMED (findings.md l.7–8, "produce" there).
46. l.48, its main finding was the battery. CONFIRMED (findings.md l.8).
47. l.49, its 38 mutants were not run on the frozen copy. UNVERIFIABLE. Consistent: SCRATCH/v2/review has no output for V01–V38.
48. l.51, fixed: F1, F3, F4 (except the binomial batch), F6–F10, F12, F5's lock-version half, and B1–B3. CONFIRMED in the code: F1 l.2983; F3 l.4077–4084; F4 l.4030–4063; F5 l.3945; F6 l.2992; F7 l.4174–4189 and l.4296–4316; F8 l.4273–4275; F9 l.4198–4210; F10 l.2925; F12 l.2920. B1–B3 are in `_bt_verdicts`.
49. l.52, "registered as Code's reading: F2". IMPRECISE (minor): the review raw §3 has F5's version half "fixed and registered" (PIN-n-26), so the two texts disagree. Fix: "registered as Code's reading: F2, and the lock form F5's fix rests on (PIN-n-26)".
50. l.53, kept with reasons: F11 (now documented), F5's D_n half and B4. CONFIRMED (docstring l.4000–4003; review §3).
51. l.54, 66 mutants ran on the fixed draft (`b5328332…78c2`). CONFIRMED: base2's hash matches. out_r2 holds 66 outputs. Each out_r2/Mnn.py is base2 with its own `.old` → `.new` applied (checked by `diff` for all 66), and each `.old` occurs exactly once in base2.
52. l.54–55, M01–M38 re-express the reviewer's 38. CONFIRMED: 28 use the same replacement text. Ten are re-anchored on moved code with the same defect (M10, M11, M13, M14, M22, M25, M29, M31, M32, M35).
53. l.55, "M39–M66 are new, on the fixes". IMPRECISE (minor): M47 (a pause's read not on disk) and M52 (the probe's package) mutate checks the frozen copy already had (frozen l.3685, l.3705–3706). They are caught by refusal cases it already had (pause-read, gread-package). Fix: "M39–M66 are new: on the fixes, and on two checks the reviewer's mutants did not reach (M47, M52)".
54. l.55, 65 were killed. CONFIRMED.
55. l.55–56, "each by the check expected to kill it". IMPRECISE (minor): this holds at the coverage-id level, but M65 was killed by "verdicts: group raised ValueError", an exception its precheck call raised before VD-PRECHECK's own check ran (out_r2/M65.out). The review raw §4 says so; the entry does not. Fix: add "(M65 by an exception its precheck raised inside the verdicts group)".
56. l.56, M08 survived. CONFIRMED (M08.out 185/185, no FAIL).
57. l.56–57, M08 is equivalent, as the reviewer said of V08. CONFIRMED (mutants.tsv V08: "yes (equivalent)").
58. l.57, "the schema's per_arm rule, with `check_report`'s plan and cell-record checks, refuses a per-arm lie before `report_problems` runs". IMPRECISE: this holds for a lie confined to `per_arm` (schema l.1135, l.1250, l.1262). A `per_arm.obtained` lie carried into the report's own cells' record counts passes `check_report` and is refused by `report_problems`' cells check (final l.4014–4017), which M08 leaves in place. The reviewer's V08 reason names "the identity and cells checks", and the committed docstring says "once the cells are the files on disk". Fix: "refuses a lie confined to per_arm before report_problems runs, and report_problems' cells check refuses one carried into the cells' record counts".
59. l.58, the committed bytes differ from round 2's base in four places. CONFIRMED (`diff` base2 final: 4 hunks).
60. l.59, one is the repository line. CONFIRMED (hunk 54c54).
61. l.60, one is PIN-n-16's register text. CONFIRMED (hunk 1657c1657,1658).
62. l.61, one is the two per-arm refusal cases, which now expect the schema's refusal. CONFIRMED (hunk 3467,3468c3468,3472).
63. l.62, one is `report_problems`' docstring, which says which of its checks cannot fire alone. CONFIRMED (hunk 3996c4000,4003).
64. l.63, the readings are strikable until LOCK-n v1.0, "as the block's §3 readings are". IMPRECISE (minor): this is true of REPO/results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md §3 ("each strikable until LOCK-n v1.0") and of the module docstring (l.15), but the entry never names "the block". Fix: "as the G-ANL-n prebuild block's §3 readings are (`8e3bf91`)".
65. l.64–66, PIN-n-23's paraphrase. CONFIRMED (PINS l.1672–1674; `exposure()` l.4120–4133 supplies "against the plan" and "the campaign generates nothing").
66. l.67–72, PIN-n-24's rules: PAUSE refused; no-arm NOT-RUN; any other end analyzed; one outcome. CONFIRMED (PINS l.1675–1682).
67. l.70, a standing pause is possible only under PI-STOP. CONFIRMED (schema l.1342–1344 allows a standing pause only under PAUSE or PI-STOP, and PAUSE is refused, l.4239).
68. l.74–75, new from F2: an arm's full read set is the report's `complete`, every planned read produced. CONFIRMED (the frozen copy's PIN-n-24 lacks the clause; the final's has it).
69. l.75–76, a non-finite read makes its arm INDETERMINATE and never makes the unit NOT-RUN. CONFIRMED (`Campaign.usable` l.1960–1963; the NOT-RUN test reads the report's `complete`, l.4270).
70. l.76–77, under the other reading a cap or STOP could give NOT-RUN where this code writes VERDICTS. CONFIRMED (follows from l.4270; findings F2's scenario).
71. l.78, PIN-n-25: "binds exactly the campaign's cells and capture layers". IMPRECISE (incomplete paraphrase of a reading flagged for the seat): PIN-n-25 (l.1683–1686) and `gread_problems` also bind the plan and identity shas, the campaign's n package, and each result to a kept point listing its merged labels. Fix: "binds the campaign: its plan and identity shas, exactly its cells by both shas, its n package, exactly its capture layers, each result at a kept point with the labels merged into it".
72. l.78–79, statuses are read per (axis, point) by the point's value, and an absent one is NOT-COMPUTED. CONFIRMED (`gread_states` l.4095–4112).
73. l.79–80, the AUC is the band median at d_eq's kept label. CONFIRMED (l.4110–4112).
74. l.81–82, PIN-n-26 is two whole lines. CONFIRMED (PINS l.1687–1689; `lock_route`).
75. l.82, "LOCK-n v1.0's drafter writes both". UNVERIFIABLE (no source says so; the PIN states the form `verdicts` checks).
76. l.83–84, PIN-n-16 amended: a finite read whose re-computation is non-finite stays in the TAU/4 row, being not above TAU/4. CONFIRMED (PINS l.1655–1658; `tau4_drop` l.2379–2387 keeps a null `exceeds_tau4`).
77. l.86, a binomial batch in a pause is not checked against the records. CONFIRMED (no such check in `report_problems`; docstring l.3999–4000).
78. l.86–87, its counting is the runner's, and no outcome reads it. CONFIRMED (the outcome layer reads no binomial field; VERDICTS only copies `binomial_state`, l.4307).
79. l.88, the analyzer does not check that LOCK-n v1.0 was committed by D_n. CONFIRMED (`committed_problems` l.3622–3636 checks "committed as it stands" only).
80. l.88–89, whether a unit runs is the Clock's, and a Clock NOT-RUN comes as a record through `not-run`. CONFIRMED (`run_not_run` l.2983).
81. l.90, "Every stage report the battery reads is built by the battery to n-build's counting". IMPRECISE (minor): VD-REFUSE's not-campaign case reads the schema's own `example_report` (l.3456–3457). Fix: "…built by the battery to n-build's counting (the not-campaign case uses the schema's example report)".
82. l.91, n-build's runner writes no STOP report yet. CONFIRMED (REPO/valence_core/n/runner.py l.335, `"stop": None`).
83. l.91, the first stage report n-build's code writes is the first independent input. CONFIRMED (consequence of 82; no runner-written report is among the battery's inputs).
84. l.93–94, G-ANL-n's canonical run waits for the seat's answers (Q1–Q9, `8e3bf91`) and for G-CAL-n's dose map. CONFIRMED (`8e3bf91` "nine questions for the seat"; no answers commit in `git log` since; final docstring l.16–17 and l.23–25).
85. l.95, N-pod's VERDICTS of record come after the campaign. CONFIRMED (proposal §8 steps 14–15).
86. l.96–97, every Python run in this work was inside a battery window the coordinating session granted. UNVERIFIABLE.
87. l.97, one process at a time at `nice -n 19`, in the foreground, with temp folders outside the repository. UNVERIFIABLE in part:
    - SCRATCH/review/run_mutants.sh l.9–21 runs the mutants in a sequential foreground loop under `nice -n 19`;
    - the battery's temp folders are system temp folders (out_r2/M65.out);
    - the four battery runs' INVOCATION lines do not show `nice`.
88. l.98, before the review: two runs of the draft (179/181, then 181/181 after a battery fix). CONFIRMED (runs/v2_1.out, v2_2.out). 181 is the frozen copy's `EXPECTED_CHECKS`. v2_1's one failing case was gread-package "no exception", which the frozen copy's package-sha choice (frozen l.3177) addresses.
89. l.99–100, after the fixes: 183/185, then 185/185, then the 66 mutant runs. CONFIRMED (runs/v2r2_1.out, v2r2_2.out; out_r2).
90. l.101, the run of record from `scripts/`, in the commit window. UNVERIFIABLE (future).
91. l.103–104, "One departure …: the first of those windows named one battery run, and it held two". UNVERIFIABLE, and it CONTRADICTS the review raw §5 (see 170).
92. l.106–107, committed by path; not pushed. UNVERIFIABLE (future).
93. l.107–108, Next: G-ANL-n's canonical run waits for the seat and G-CAL-n. CONFIRMED (as 84).

##### Text 2: SCRATCH/v2/raw/review.md

94. l.1, PI date 2026-11-16. CONFIRMED.
95. l.3, it is the raw for the entry "n package — scripts/n_analyze.py, the verdicts command". CONFIRMED (the entry's headline).
96. l.5, the reviewer read the draft at `0b555476…843c`. CONFIRMED.
97. l.5, "frozen as a copy before the review". UNVERIFIABLE (timing). Consistent with findings.md l.12: "unchanged at the end".
98. l.5–6, the frozen copy is "the committed analyzer (`2822721`) with the `verdicts` command and its battery group added". IMPRECISE: `diff` of committed-2822721.py and the frozen copy also changes existing code, which the reviewer reviewed as "Changed helpers":
    - `gread_table` drops its −1 row;
    - the `dir_slopes` fix in `build_state`;
    - `run_not_run` is rebuilt on `not_run_doc`;
    - `_bt_write_campaign` gains a `lock_sha256` parameter;
    - `EXPECTED_CHECKS` goes from 171 to 181;
    - the module docstring changes, and the repository line is a DRAFT one.

    Fix: "…with the verdicts command and its battery group added, and three helpers changed (gread_table, build_state's dir_slopes, run_not_run)".
99. l.6–7, the reviewer was a subagent, under a brief quoting the list of record v2's items 1–5. UNVERIFIABLE.
100. l.7–8, its spec was PROPOSAL-n v0.2 (`30a3d0f5…04f4`) and the schema at `14e65d8` (`4bed3f9a…4665`). CONFIRMED (findings.md l.13–14).
101. l.8–9, it also read n-build's untracked runner.py and probe.py, only to check the analyzer's claims. CONFIRMED (findings.md l.15–16; `git ls-files valence_core/n/` lists only `__init__.py` and `schema.py`).
102. l.9, it ran nothing. CONFIRMED (findings.md l.17, the reviewer's own statement).
103. l.9–10, F1–F12 (F1–F6 MINOR, F7–F12 NOTEs) and B1–B4. CONFIRMED.
104. l.10–11, 38 mutants V01–V38 were written against the frozen copy. CONFIRMED (each `.old` occurs exactly once in the frozen copy, by a perl count).
105. l.11, predictions of 10 killed and 28 surviving, V08 among them as equivalent. CONFIRMED.
106. l.12, the reviewer's mutants were not run on the frozen copy. UNVERIFIABLE (consistent).
107. l.12–13, Code re-expressed all 38 as M01–M38 and ran them on the fixed draft. CONFIRMED.
108. l.14–15, every finding was disposed of in §3. CONFIRMED (§3 covers F1–F12 and B1–B4).
109. l.16, M01–M38 re-express V01–V38. CONFIRMED.
110. l.16–17, "M39–M66 are new, on the fixes". IMPRECISE (minor; as 53).
111. l.17, the base was the fixed draft at `b5328332…78c2` (185/185). CONFIRMED (hash; v2r2_2.out). That output records no hash of the bytes it ran (see 181).
112. l.17–18, 65 were killed, each at the check expected of it. CONFIRMED.
113. l.18, M08 survived and is equivalent, as the reviewer said of V08. CONFIRMED.
114. l.19, the first run passed 183/185. CONFIRMED.
115. l.19–20, "a case of the new battery stat'ed under `data/n/verdicts`, and the battery's own hook refused it". IMPRECISE (minor): the hook recorded two refusals of `data/n/verdicts` itself, not of paths under it (v2r2_1.out l.182). Which case made them is not in the output. Fix: "stat'ed `data/n/verdicts`".
116. l.20, after the fix, 185/185. CONFIRMED.
117. l.21–22, "The committed bytes differ from round 2's base in the repository line, the two per-arm refusal cases' expected messages, and `report_problems`' docstring". FAIL: the diff (base2 against final) has a fourth hunk, PIN-n-16's register text (1657c1657,1658), which §6 and the entry both list. Fix: "…in the repository line, PIN-n-16's register text, the two per-arm refusal cases' expected messages, and `report_problems`' docstring (§6)".
118. l.24, every run here was inside a battery window the coordinating session granted. UNVERIFIABLE.
119. l.24–25, one process at a time, `nice -n 19`, in the foreground, with temp folders outside the repository. UNVERIFIABLE in part (as 87).
120. l.25, nothing ran on a model or on the box. UNVERIFIABLE.
121. l.25–26, each mutant was an exact, unique text replacement on a fresh copy of its base. CONFIRMED (run_mutants.sh l.10–17; all 66 copies checked).
122. l.26–27, `--selftest`, and "killed" means a non-zero exit. CONFIRMED (run_mutants.sh l.18–21).
123. l.31–32, the reviewer's Write tool refused report files, its report came in its hand-back, and Code saved it. UNVERIFIABLE (findings.md's preamble l.3–5, Code's own note, says the same).
124. l.32, the headings are moved down one level. CONFIRMED.
125. l.32–33, "the moving draft was this session's own". UNVERIFIABLE (the reviewer wrote "another session's edits").
126. l.33–34, every finding is about the frozen copy, with its line numbers. CONFIRMED (F1 2948–2957, F2 3882, F3 3701–3708, F4 3676–3687 and F5 3857–3868 land on the cited code in the frozen copy).
127. l.36–128, §1 matches findings.md from "Nothing in the production path" to the end, with headings moved down one level. CONFIRMED (identical, 93 lines).
128. l.29, "(unedited in substance)". CONFIRMED (identical text).
129. l.132, the reviewer's table (`mutants.tsv`, five columns), as written. CONFIRMED.
130. l.132–133, "These 38 were not run on the frozen copy". UNVERIFIABLE (as 106).
131. l.133, M01–M38 re-express them on the fixed draft (§4). CONFIRMED.
132. l.135–174, the §2 table. CONFIRMED (38 rows, identical to mutants.tsv rendered as a table).
133. l.178–179, the §3 lead-in. CONFIRMED.
134. F1. CONFIRMED: refusal at l.2983–2985, message as quoted; the VD-ONE-OUTCOME "not-run on a no-arm cause" case, with nothing written (l.3368–3376); M56 killed by VD-ONE-OUTCOME.
135. F2. CONFIRMED: PIN-n-24 and the `run_verdicts` docstring carry the reading, and N1 is INDETERMINATE in the scenario. Note: the reviewer's scenario said "every question INDETERMINATE"; the raw keeps the part the code guarantees.
136. F3. CONFIRMED: l.4077–4084; the four named cases exist; M13 and M14 killed. probe.py l.88–95 lists every cell of the report.
137. F4, the cap.used_ms, pause-kind and resumption checks, and "runner.py computes it the same way". CONFIRMED (l.4030–4031, l.4038–4043, l.4055–4058; runner.py l.374 and l.470).
138. F4, the three more pause rules and their tests. CONFIRMED (l.4033–4037 and l.4059–4063; launch-gap, two-standing and standing-not-last).
139. F4, the rules were "added while the review ran, from n-build's answer of 2026-11-16". UNVERIFIABLE. Consistent: they are absent from the frozen copy.
140. F4, the binomial batch is not checked, and the docstring says so. CONFIRMED.
141. F4, the named tests (VD-COMPLETE's nonfinite pause on the fresh path alone, l.3155–3171) and mutants M42–M50. CONFIRMED.
142. F5, the version line, the lock-version test and M39. CONFIRMED.
143. F5, D_n is not checked, with the reasons given. CONFIRMED.
144. F6, `one_outcome` in both commands before any write, the test and M53–M55. CONFIRMED.
145. F7: the secondary first, named by name and sha256; the cosines with their source in both documents; six finite float pairs; null without `--gvec`; the tests and M59–M61. CONFIRMED.
146. F8, the docstring, the four bindings and M57–M58. CONFIRMED.
147. F9, of-record inputs committed as they stand, the two tests, M22 and M65. CONFIRMED.
148. F10, `_err_where`'s three forms, the schema-blind tests, M04 and M66. CONFIRMED.
149. F11, the sha checks tied by `check_report`, and M51 killed. CONFIRMED (out_r2/M51.out: the identity case is refused by the sha check's message instead of its own).
150. F11, the per-arm check "is implied by the schema's per_arm rule … together with check_report's plan and cell-record checks". IMPRECISE (as 58: it also needs `report_problems`' cells check).
151. F11, the two per-arm cases expect "SchemaError at report.per_arm.<arm>". CONFIRMED.
152. F12, `allow_nan=False`, exit 4 under `verdicts`, VD-PLAIN and M62. CONFIRMED.
153. B1, all seven bullets and M01, M02, M15, M18, M25–M27, M31, M32. CONFIRMED (in `_bt_verdicts`; VD-SOME-ARMS, VD-MERGED-ROUTE-A, VD-ONE-OUTCOME and VD-PLAIN are the four ids new since the frozen copy, 184 → 188).
154. B2. CONFIRMED (`_bt_report_for` → `_bt_files`; `label_mass=True` on the main report; VD-COMPLETE checks literal counts; label-mass; M05, M06, M40, M41).
155. B3. CONFIRMED: the seven named refusal cases are absent from the frozen copy's 20. CMD-NOTRUN writes the record with indent=1 (l.3826) and checks its file's sha256. The mutant list is correct.
156. B4: the runner writes stop null, and the cap's used time is computed as runner.py does. CONFIRMED.
157. B4, "as its answer of 2026-11-16 states it". UNVERIFIABLE.
158. §4, the base `b5328332…78c2`, frozen as a copy. CONFIRMED (hash; the out_r2 copies).
159. §4, M01–M38 re-express V01–V38, "same defect, new anchor". CONFIRMED (as 52; the anchor is new for ten of them).
160. §4, "M39–M66 are new, on the fixes". IMPRECISE (as 53).
161. §4, the 66 ran in six parts. UNVERIFIABLE.
162. §4, 65 killed, each by the check named as its expected killer. CONFIRMED: every killed mutant's unreached coverage ids include its expected killer's. M65 is covered by the next sentence.
163. §4, for VD-REFUSE kills, "each was a case named in the table". IMPRECISE: M04's detail also shows per-arm failing, a case named only in M08's row. That detail is cut at 200 characters (`'per-arm': 'wro...`), so M04's full failing set cannot be read from it. M66's failing entry is `schema-blind`, written "schema-report: blind" in the table. Every other VD-REFUSE kill fails exactly its named cases. Fix: "each was a case named in its row, except M04's, whose detail (cut at 200 characters) also shows per-arm failing".
164. §4, M65 was killed by an exception inside the verdicts group. CONFIRMED (out_r2/M65.out).
165. §4, "as predicted when the mutant was written". UNVERIFIABLE (mutants_r2.spec and mutants.tsv record no such prediction).
166. §4, the M08 equivalence reason ("refuses any per-arm lie") and "the reviewer said the same of V08". IMPRECISE (as 58). The reviewer's V08 reason includes "the identity and cells checks".
167. §4, "the first failing check, cut at 80 characters". IMPRECISE: the cut is at 80 bytes, so the seven rows whose line contains "§" (M19, M20, M27, M53–M56) are cut at 79 characters. Fix: "cut at 80 bytes". (`<tmp>`/`<repo>` masking ✓.)
168. §4, the table's rows. CONFIRMED for 65 rows: columns 1–5 equal mutants_r2/mutants.tsv; "fails" equals the `[FAIL]` line count; "first" is the first `[FAIL]` line, masked and cut at 80 bytes; M08 survived. The spec's headers also equal the tsv.
169. §4, M65's row: "first: verdicts: group raised ValueError: '<tmp>' is not in the subpath of '<repo>', from xp.relative_to(root)". FAIL: the first `[FAIL]` line of out_r2/M65.out ends at "…is not in the subpath of '<repo>'"; ", from xp.relative_to(root)" is not in the output. Fix: drop it from the cell (the lead-in's M65 sentence can carry it).
170. §5, "Both runs were in the first window the coordinating session granted for this work, which named one run". UNVERIFIABLE, and it CONTRADICTS the entry (l.96–104). Per both texts every Python run in this work was in a granted window, and runs/v2_1.out and v2_2.out are two earlier runs of this work, on the 181-check draft the reviewer read. So the window holding 183/185 and 185/185 was not the first, or it held four runs. And if that later window too named one run, the entry's "One departure" undercounts. Fix: reconcile the two texts — name each window and its runs, and count departures.
171. §5, the first run was 183/185. CONFIRMED.
172. §5, every verdicts check passed. CONFIRMED (v2r2_1.out fails only l.182 and l.185).
173. §5, the hook check failed, and the coverage check with it. CONFIRMED (`['STR-OPEN-HOOK']`; the hook check covers that id, l.1861).
174. §5, "two stat calls under `data/n/verdicts`, recorded beside its own probe". IMPRECISE (minor; as 115): the two refused calls were on `data/n/verdicts` itself, recorded beside the hook's own probe path.
175. §5, both came from the VD-PRECHECK case that passed `<repo>/data/n/verdicts`. UNVERIFIABLE (the pre-fix draft is not among the sources). Consistent with the final's comment at l.3567.
176. §5, `Path.resolve()` stats each part of a path. CONFIRMED (standard-library realpath lstat's each component, consistent with the two refusals).
177. §5, the hook refuses any stat under data/n's ckpt, reports and verdicts before the filesystem is touched. CONFIRMED (`_barred` l.1730–1741; `_Hook.check` raises before the original call).
178. §5, the case now passes `<repo>/data`. CONFIRMED (l.3567).
179. §5, as the `not-run` precheck's case already did. CONFIRMED (l.3841).
180. §5, the second run: 185/185, all 188 ids reached, exit 0. CONFIRMED (v2r2_2.out; exit 0 follows from l.3612 and l.4356).
181. §5, "on the draft at sha256 `b5328332…78c2`". UNVERIFIABLE (the output records no hash). Consistent: 185 checks, and base2 already passes `<repo>/data`.
182. §6, the diff is of round 2's base against the committed file, whole. CONFIRMED (`diff` base2 final, with the path masked, is identical to the block).
183. §6, the absolute path is shown as `<repo>`. CONFIRMED.
184. §6, the repository line is derived from `__file__`. CONFIRMED.
185. §6, PIN-n-16's register text changes, and `tau4_drop`'s behavior is unchanged. CONFIRMED (`tau4_drop` is not in the diff).
186. §6, the two per-arm refusal cases (F11; M08). CONFIRMED.
187. §6, `report_problems`' docstring. CONFIRMED.
188. §6, "The battery's run of record is on these bytes". UNVERIFIABLE (future).
189. §6, the diff block. CONFIRMED (identical, 25 lines).

#### Totals

189 claims: **137 CONFIRMED, 19 IMPRECISE, 2 FAIL, 31 UNVERIFIABLE**.
- Entry: 93 claims, of which 69 CONFIRMED, 10 IMPRECISE, 0 FAIL and 14 UNVERIFIABLE.
- Review raw: 96 claims, of which 68 CONFIRMED, 9 IMPRECISE, 2 FAIL and 17 UNVERIFIABLE.

#### FAIL items and fixes

- **117** (review raw l.21–22): the lead-in's list of the committed bytes' differences leaves out PIN-n-16's register text. Add it: "the repository line, PIN-n-16's register text, the two per-arm refusal cases' expected messages, and `report_problems`' docstring (§6)".
- **169** (review raw §4, M65's row): the "first:" cell adds ", from xp.relative_to(root)", which is not in out_r2/M65.out. End the cell at "…'<repo>')".

#### IMPRECISE items and fixes

- **22**: "states no direction of record" → "does not state exactly one direction of record, Route A or Route B, as a whole line (PIN-n-26)".
- **23**: the pre-write list leaves out the date, the precheck (of record: inputs outside the repository or not committed as they stand; `--out` inside the repository), and a cell-less report beside a non-empty campaign directory. Add them, or say "Among its refusals".
- **38**: "one line" → "besides the INVOCATION line every command prints, one line: the tuple and each output's name, how it was written and its sha256; no margin".
- **49**: the entry registers F2 only, while the review raw has F5's version half "fixed and registered". Align the texts, for example "registered: F2, and the lock form F5's fix rests on (PIN-n-26)".
- **53 / 110 / 160**: "M39–M66 are new, on the fixes" → "…on the fixes, and on two checks the reviewer's mutants did not reach (M47, M52)".
- **55**: add "(M65 by an exception its precheck raised inside the verdicts group)".
- **58 / 150 / 166**: the M08 equivalence also needs `report_problems`' cells check: "the schema's per_arm rule and check_report's plan and cell-record checks refuse a lie confined to per_arm; report_problems' cells check refuses one carried into the cells' record counts". The reviewer's V08 reason names the cells check.
- **64**: "as the block's §3 readings are" → "as the G-ANL-n prebuild block's §3 readings are (`8e3bf91`)".
- **71**: give PIN-n-25's full binding: the plan and identity shas, exactly the cells by both shas, the n package, exactly the capture layers, and each result at a kept point with its merged labels.
- **81**: "…built by the battery to n-build's counting (the not-campaign case uses the schema's example report)".
- **98**: the frozen copy also changed three helpers (`gread_table`, `build_state`'s `dir_slopes`, `run_not_run`), plus `_bt_write_campaign`, `EXPECTED_CHECKS` and the docstring. Say so.
- **115 / 174**: "stat'ed under `data/n/verdicts`" → "stat'ed `data/n/verdicts`" (the refusals were of that path itself).
- **163**: "each was a case named in its row, except M04's, whose detail (cut at 200 characters) also shows per-arm failing".
- **167**: "cut at 80 characters" → "cut at 80 bytes"; the seven rows containing "§" are cut at 79 characters.

#### Contradiction to reconcile (UNVERIFIABLE on both sides)

- **91 / 170**: the review raw §5 puts the 183/185 and 185/185 runs in "the first window … for this work, which named one run". The entry puts two earlier runs of this work in a window (179/181 and 181/181; runs/v2_1.out and v2_2.out exist), and reports one departure: "the first of those windows named one battery run, and it held two". Both cannot hold. The texts should name each window, its runs and the departure count.

#### Placeholder value

- `FINAL_SHA` = `5187089219eb0a7709078205fcb0bf88afab1a27e926eb8056a06c64e6b683a6` (`51870892…83a6`), the sha256 of SCRATCH/v2/final/n_analyze.py as checked here.

#### Observation outside the claims (no verdict)

- In the final `run_verdicts` the secondary is written (l.4299) before VERDICTS is assembled. VERDICTS' `_plain` calls (`outcomes`, `state_figures`, `gleak_table`, `gread_table`, the sensitivity row) and `json_text(verd)` run only after that write (l.4301–4318). An AnlStop there (a non-finite figure, or `allow_nan=False`) would leave N-pod_secondary.json without N-pod_VERDICTS.json. In the frozen copy every `_plain` ran before either write, and `json_text` could not STOP: that is the reviewer's "every AnlStop fires before the first write". The F7 and F12 fixes reopened that window. No text claims otherwise; the seat or the next pass may want to know.

## 2. Code's dispositions of the first pass

Every item is accepted. One of them, the observation outside the claims, is accepted as a code change. The texts were
then revised to the code as it now stands: the review raw's sections are renumbered (§5 is new; the battery runs are
§6; the committed bytes are §7).

### FAIL

- **117** (the review raw's lead-in; the committed bytes' differences). Carried, and moot: after the code fix below,
  the mutants re-ran on a new base, and the committed bytes differ from that base in the repository line only. The
  lead-in and §7 now say so; PIN-n-16's text and the other post-run edits are in the new base.
- **169** (M65's row). The §4 table is now the re-run's, generated by script from `out_r3/M65.out`, with nothing
  added by hand. The temp path is masked without eating its closing quote, and the repository path is masked before
  the cut.

### IMPRECISE

- **22**: taken as given ("does not state exactly one direction of record, Route A or Route B, as a whole line").
- **23**: the entry now lists every refusal, in the order checked: the precheck, the date, the report's schema
  check, PAUSE, not a campaign, the lock, the binding (or a cell-less report beside a non-empty directory), G-READ-n's
  artifact and the cosines file where it analyzes, and one outcome and write-once.
- **38**: taken as given.
- **49**: aligned. The entry now has F5's lock version as fixed, "whose line form is registered as PIN-n-26", and F2 as
  the registered reading.
- **53 / 110 / 160**: taken as given in both texts, with M47's and M52's checks named in §4.
- **55**: taken as given, for the first run and for the re-run.
- **58 / 150 / 166**: taken as given in the entry, the raw's §3 (F11) and §4.
- **64**: "as the question block's §3 readings are (`8e3bf91`)". `8e3bf91`'s subject calls it "G-ANL-n: nine questions
  for the seat before its canonical run".
- **71**: taken as given (PIN-n-25 in full).
- **81**: taken as given.
- **98**: taken as given, with the draft's absolute repository line added.
- **115 / 174**: taken as given.
- **163**: moot for the table, which is now the re-run's. The re-run's spec corrects M04's expected killer to "every
  case the schema refuses" (the per-arm cases among them) and M66's to the case `schema-blind`.
- **167**: the table is regenerated with a character cut (perl with UTF-8 decoding), so "cut at 80 characters" now
  holds.

### The contradiction (91 / 170)

Reconciled. There were three windows before the commit, and both texts now name each one:
- Before the review, a window for up to three runs of the draft's battery. It held two (179/181, 181/181).
- After the fixes, a window for one battery run and then the 66 mutant runs. It held two battery runs (183/185,
  185/185) and the 66 runs: the one departure, told at release.
- After pass 1, a window for one battery run and the 68 mutant runs. It held exactly that.

### The observation outside the claims (the write order)

Accepted as a code change (the review raw's §5):
- `run_verdicts` forms both outputs' text before writing either; the secondary's sha256 comes from its text.
- `write_all_once` checks every target before writing any.
- VD-WRITE-ONCE and VD-PLAIN gained cases for it, and M67 and M68 test them.
- The battery: 185/185 on the new base (sha256 `56c9b788…5b5b`). The re-run: 67 of 68 killed, M08 equivalent.

### The placeholder

`FINAL_SHA` changed with the code fix. It is filled from `shasum`: `b5c87c8b…6aab`, the commit form of the new base
(the new base with the repository line derived from `__file__`).

## 3. The second pass: the checker's report, whole

### Values-check, pass 2 (blind): the `verdicts` entry draft, its review raw, and pass 1's dispositions

**Bottom line.** I checked 270 claims: 212 CONFIRMED, 7 IMPRECISE, 6 FAIL, 45 UNVERIFIABLE.
- All hashes check out.
- The §2, §4 and §7 tables and blocks match their sources (one minor note on M65's cell).
- §1 matches findings.md.
- The write path behaves as the texts say.
- The 6 FAILs come from three things: two stale section pointers in the entry; an undercount of the new mutants that target code the frozen copy already had (it appears in three places); and one false statement in the dispositions.

**How I checked.**
- Tools: `shasum -a 256` with `cut`, `diff`, `/usr/bin/grep`, `sed`, `awk`, `cmp`, and perl one-liners for counting, masking and an 80-character cut. Also `git show <rev>:<path>`, `git log --format`, `git show --name-only`, `git ls-files`, and a `git status --porcelain` limited to named paths.
- No Python or other interpreter ran on the code. Nothing under `data/` was touched. Nothing in the repository was edited.
- My working files went to SCRATCH/v2/vc/pass2_tmp and I removed them at the end.
- I did not write SCRATCH/v2/vc/pass2.md: my standing instructions bar writing report files. This hand-back is the only copy.
- Path names used below:
  - "final" = SCRATCH/v2/final/n_analyze.py
  - "frozen" = …/review/n_analyze.verdicts-under-review.py
  - "base2" = …round2-verdicts-base.py
  - "base3" = …round3-verdicts-base.py
  - "schema" = `git show 14e65d8:valence_core/n/schema.py`

#### Digests (computed by tool)

| File | sha256 (cut 1–8 … 61–64) | Text |
|---|---|---|
| final | `b5c87c8b…6aab` (full `b5c87c8b4b3a1c2f09aa520abcd5f4a3d70a272a32f8cd243545b925f7826aab`) | entry l.7 full hash ✓ |
| frozen | `0b555476…843c` | ✓ |
| base2 | `b5328332…78c2` | ✓ |
| base3 | `56c9b788…5b5b` | ✓ |
| `2822721:scripts/n_analyze.py` (= HEAD's = committed-2822721.py) | `4f63903f…5d73` | ✓ |
| `14e65d8:valence_core/n/schema.py` (= HEAD's = working tree's) | `4bed3f9a…4665` | ✓ |
| REPO/PROPOSAL-n-bk-reconciliation-v0_2.md | `30a3d0f5…04f4` | ✓ |

The commits `2822721`, `14e65d8` and `8e3bf91` exist and their subjects match what the texts say about them. `diff base3 final` is a single hunk, `54c54`.

#### Claims

##### Text 1: SCRATCH/v2/raw/entry.md

1. l.1, dated 2026-11-16. CONFIRMED (the work's commits and the review raw carry this date).
2. l.1, the command is PROPOSAL-n v0.2 §8 step 15. CONFIRMED (proposal l.159, step 15: "`PROPOSAL-n N-pod — VERDICTS` … `— secondary DVs`").
3. l.1–2, on n-build's `n-report-v1` and `n-gread-v1` at `14e65d8`. CONFIRMED (schema l.994–995).
4. l.2–3, it gives VERDICTS and secondary DVs, or the NOT-RUN derived from the stage report. CONFIRMED (final `run_verdicts` l.4249–4352).
5. l.3, "Its battery passes 185/185". CONFIRMED on the latest run of the same code: runs/v2r3_1.out ran base3, which differs from final only at l.54. The run of record is pending.
6. l.3, "reviewed blind". UNVERIFIABLE: the reviewer's brief would settle it. findings.md's title, "Blind review…", is consistent.
7. l.3–4, 67 of 68 mutants killed. CONFIRMED: in out_r3, 67 runs have ≥2 `[FAIL]` lines and N/185 < 185, which makes `main` return 1 (l.4387). M08 is 185/185 with no FAIL.
8. l.4, "the survivor is equivalent". CONFIRMED in substance (see 64 for the wording of the reason).
9. l.4–5, PIN-n-23 to PIN-n-26 and an amendment to PIN-n-16 are Code's readings, flagged. CONFIRMED (PINS l.1655–1658 and l.1672–1689; 2822721's PIN-n-16 ends at "re-computation are kept").
10. l.5, model-free; nothing ran on a model or on the box; no stage ran. UNVERIFIABLE: the session transcript would settle it. Consistent: module-level imports are numpy and the standard library, and every run in the sources is `--selftest`.
11. l.6–7, the file's full sha256. CONFIRMED.
12. l.7, `4f63903f…5d73` at `2822721`. CONFIRMED.
13. l.7–8, still pinned to the schema at `14e65d8` (`4bed3f9a…4665`). CONFIRMED (l.1882).
14. l.8, binds PROPOSAL-n v0.2 by sha256 (`30a3d0f5…04f4`). CONFIRMED (l.60).
15. l.9–13, the four commands and their options, `verdicts` new. CONFIRMED (`main` l.4362–4419; 2822721's docstring says verdicts "is added when their forms are committed").
16. l.15–16, the run of record gives 185/185, all 188 coverage ids, exit 0. UNVERIFIABLE (not yet run). Consistent: v2r3_1.out shows 185/185 and "every one of the 188 required ids"; I hand-counted `_REQ` (l.868–906) at 188; `EXPECTED_CHECKS = 185` (l.866).
17. l.17, the selftest raw's name. UNVERIFIABLE (the file is still to be written). It follows the form of the committed `2026-11-16_n-analyze_build_selftest.txt`.
18. l.19, every refusal comes before anything is written, with exit 2. CONFIRMED:
    - `main` l.4403–4412;
    - every AnlRefusal precedes `write_once` / `write_all_once`;
    - `write_all_once` checks before writing (l.2960–2963).
19. l.19, the bullets are "in the order they are checked". CONFIRMED: precheck (l.4403) → date (l.4265) → report (l.4268–4275) → lock (l.4277–4287) → binding (l.4293–4299) → G-READ-n and cosines (l.4311–4317) → one outcome and write-once (l.4307–4309, l.4348–4349).
20. l.19–35, the list as "Its refusals" (read as complete). IMPRECISE. It leaves out four kinds of refusal (all exit 2, all before any write):
    - `schema_module`'s own refusal (l.1900–1911: the schema file is not the pinned bytes), which comes between the date and the report;
    - `load_campaign`'s refusals of the cells themselves (l.1966–2059). They fire at the binding step, before `report_problems`. They cover:
      - a cell the schema's `check_cell` refuses;
      - a misnamed cell;
      - capture bytes that do not match;
      - an identity that differs between cells;
      - a read in two cells, or files no cell names;
      - the analyzer's own dose-map or plan derivation disagreeing;
      - reads outside the plan;
      - the cross-record checks;
    - an unreadable or non-JSON report (l.3989–3990);
    - an unreadable lock (l.4278–4279).

    Fix: insert "the schema module not the pinned bytes" after the date, and open the binding bullet with "cells the reader refuses (the schema's cell checks, their bytes, the plan, the cross-record checks), or …". Alternatively, introduce the list as "Its refusals include".
21. l.20–22, the precheck bullet. CONFIRMED (`verdicts_precheck` l.4221–4246).
22. l.23, the date. CONFIRMED (l.4265).
23. l.24–25, a report `check_report` refuses (by its field path alone), a PAUSE, or a report that is not a v0.2 campaign. CONFIRMED (l.4268 with `_err_where` l.2929–2930, where SchemaError subclasses ValueError, schema l.287; l.4270–4275).
24. l.26–28, the four lock conditions, including exactly one route line A or B (PIN-n-26). CONFIRMED (l.4281, l.4285, `lock_route` l.3974–3979).
25. l.29–30, a report not bound to the cells (identity, cells by both shas and record count, counters and the cap's used time, launches and pauses). CONFIRMED (`report_problems` l.4037–4092).
26. l.31, a report with no cell beside a campaign directory that is not empty. CONFIRMED (l.4298–4299).
27. l.32–33, where it analyzes: G-READ-n's artifact missing, refused by the schema or not bound (PIN-n-25); a malformed cosines file. CONFIRMED (l.4311–4317).
28. l.34–35, an output of the other outcome already present, or an output with other bytes. CONFIRMED (`one_outcome` l.3001–3005; `write_once` l.2952; `write_all_once` l.2960–2962).
29. l.36–37, PI-STOP, G-VER-STOP or CAP with no arm complete gives NOT-RUN `no-arm:<end>`. CONFIRMED (l.3964, l.4301–4310).
30. l.37–38, the NOT-RUN is bound to the report, its end state, the STOP record, the lock and the schema module. CONFIRMED (l.4304–4306; VD-NOTRUN-* l.3365–3375).
31. l.39–40, otherwise it computes the state, outcomes and filled sentences on the reader path, with the route from the lock. CONFIRMED (l.4318–4322, l.4287).
32. l.40–41, both outputs are formed before either is written; a STOP while forming (exit 4) writes nothing. CONFIRMED (l.4326–4349; `main` l.4413–4415; VD-PLAIN l.3573–3587 asserts that `out_stop` never exists).
33. l.41–42, it writes, write-once, the secondary and then VERDICTS. CONFIRMED (l.4349).
34. l.43, VERDICTS carries the tuple, outcomes, sentences and §4's figures. CONFIRMED (l.4331–4333).
35. l.44, G-LEAK-n's and G-READ-n's tables. CONFIRMED (l.4333, l.4335).
36. l.45, both counter forms. CONFIRMED (l.4336).
37. l.46, the exposure realised (PIN-n-23). CONFIRMED (l.4339).
38. l.47, the TAU/4 row (PIN-n-16). CONFIRMED (l.4340–4343).
39. l.48, the cosines when G-VEC's file is given. CONFIRMED (l.4325, l.4331).
40. l.49, every input and the secondary by sha256. CONFIRMED:
    - lock, report, schema module, proposal, analyzer (l.4288–4291);
    - the artifact (l.4334);
    - the cosines source (l.4325);
    - the cells (l.4344–4345);
    - the secondary (l.4346).
41. l.50, one outcome per unit, in either command. CONFIRMED (`one_outcome` at l.2996, l.4307, l.4348; VD-ONE-OUTCOME l.3376–3395).
42. l.51–52, besides the INVOCATION line, one line: the tuple and each output's name, how and sha256; no margin. CONFIRMED (l.4364, l.4355–4359, l.4416; VD-STDOUT).
43. l.53–54, the review raw's name. UNVERIFIABLE (still to be written).
44. l.55, the reviewer read the draft frozen at `0b555476…843c`. CONFIRMED.
45. l.55–56, the reviewer was a subagent under a brief quoting the list's items 1–5. UNVERIFIABLE (the brief or the transcript would settle it).
46. l.56–57, F1–F12 and B1–B4. CONFIRMED (findings.md).
47. l.57, 38 mutants; 10 predicted killed, 28 surviving. CONFIRMED (mutants.tsv: "no" ×10, "yes" ×27, "yes (equivalent)" ×1).
48. l.57–58, nothing in the production path gives a wrong output on what the runner and probe write today. CONFIRMED (findings.md l.7–8).
49. l.58, its main finding was the battery. CONFIRMED (findings.md l.8).
50. l.59, its mutants were not run on the frozen copy. UNVERIFIABLE (the transcript would settle it). Consistent: no `V??.out` or `V??.py` exists anywhere under the n9 scratch.
51. l.61–62, the fixed list. CONFIRMED:
    - F1 l.2992; F3 l.4106–4113; F4 l.4059–4092;
    - F5 l.3974 with PIN-n-26 l.1687; F6 l.3001;
    - F7 l.4203–4218 and l.4325–4346; F8 l.4304–4306 and l.4260;
    - F9 l.4229–4240; F10 l.2925–2933; F12 l.2920;
    - B1–B3 in `_bt_verdicts`.
52. l.63, F2 registered in PIN-n-24. CONFIRMED (l.1679–1681).
53. l.64, kept: F11 (documented), F5's D_n half, B4. CONFIRMED (l.4029–4032).
54. l.65, M01–M38 re-express the reviewer's 38. CONFIRMED (the tsv's round-1 column is V01–V38 in order).
55. l.65–67, "M39–M66 are new, on the fixes and on two checks the frozen copy already had that the reviewer's mutants did not reach (M47, M52)". **FAIL.**
    - Five more mutate code the frozen copy already had: M40, M41, M51, M63 and M64. Each one's `.old` occurs exactly once, verbatim, in frozen (perl count):
      - M40: the label-mass check;
      - M41: the label-mass floor in `report_counters`;
      - M51: the identity check;
      - M63: `_plain`'s key-fold STOP;
      - M64: `tau4_drop` (frozen's version has the same line; only its docstring changed).
    - None of these lines is touched by any V mutant.
    - M51's check is caught by a refusal case the frozen copy already had (`identity`), exactly as M47's and M52's are.

    Fix: "M39–M66 are new: 21 on the fixes (M39, M42–M46, M48–M50, M53–M62, M65, M66) and 7 on checks the frozen copy already had that the reviewer's mutants did not reach (M40, M41, M47, M51, M52, M63, M64)."
56. l.67, M67 and M68 are on the values-check's code finding. CONFIRMED (mutants_r3.spec).
57. l.68–69, first run on `b5328332…78c2`: 66 mutants, 65 killed, each by its expected check. CONFIRMED:
    - each out_r2 copy is base2 plus its one replacement, and each `.old` occurs once in base2;
    - every killed mutant's expected killer is among its unreached coverage ids.
58. l.69, M65 was killed by an exception inside the verdicts group. CONFIRMED (out_r2/M65.out, first `[FAIL]`).
59. l.69, M08 survived. CONFIRMED.
60. l.70–72, the re-run on `56c9b788…5b5b`: 68 mutants, 67 killed, each by its expected check. CONFIRMED:
    - all 68 out_r3 copies are base3 plus their one replacement;
    - every expected-killer id is among the unreached ids;
    - every named VD-REFUSE or VD-PRECHECK case fails in the run's detail.
61. l.72, M65 again by an exception. CONFIRMED (out_r3/M65.out l.176).
62. l.72, M08 survived again. CONFIRMED.
63. l.73, M08 is equivalent "as the reviewer said of V08". CONFIRMED (tsv: "yes (equivalent)").
64. l.73–75, the reason: the per_arm rule, `check_report`'s plan and cell-record checks, and `report_problems`' cells check refuse a per-arm lie. IMPRECISE: the reason also needs `report_problems`' identity check (l.4037).
    - Counter-case: a report whose identity has a dose map keeping more labels than the cells' map. It can carry per_arm counts true to its own plan, which passes schema l.1246–1262, and cells equal to the files, which passes the cells check.
    - Under M08, only the identity check (with the two sha checks tied to it) refuses that report.
    - The reviewer's V08 reason names "the identity and cells checks".

    Fix: "…with check_report's plan and cell-record checks and report_problems' own identity and cells checks, …".
65. l.76–77, pass 1's finding: the secondary was written before VERDICTS was formed. CONFIRMED (base2 `run_verdicts`: `write_once(sec)` at about l.4292, before `verd`'s `_plain` calls and `json_text(verd)`).
66. l.77–78, both outputs now formed first; `write_all_once` checks both targets before writing. CONFIRMED (l.4329–4349, l.2957–2963).
67. l.78–79, VD-WRITE-ONCE and VD-PLAIN test it (M67, M68). CONFIRMED (l.3237–3247, l.3573–3587). out_r3: M67 leaves VD-WRITE-ONCE unreached; M68 leaves VD-COMPLETE, VD-PLAIN and VD-STDOUT unreached.
68. l.80, the committed bytes differ from the re-run's base in the repository line only. CONFIRMED.
69. l.80, "(the raw's §6)". **FAIL**: in the review raw the committed bytes are §7; §6 is the battery runs. Fix: "(the raw's §7)".
70. l.81, the readings are strikable until LOCK-n v1.0. CONFIRMED (l.1643, l.16).
71. l.81–82, "as the question block's §3 readings are (`8e3bf91`)". CONFIRMED (8e3bf91's raw: "## 3. Not questions: Code's readings, declared (each strikable until LOCK-n v1.0)").
72. l.83–85, PIN-n-23 paraphrase. CONFIRMED (l.1672–1674; `exposure` docstring l.4150–4152).
73. l.86–91, PIN-n-24's end-state rules and one outcome. CONFIRMED (l.1678–1682).
74. l.89–90, a standing pause is possible only under PI-STOP. CONFIRMED (schema l.1343–1344; PAUSE refused at l.4270).
75. l.93–94, new in PIN-n-24 from F2: the full read set is the report's `complete`. CONFIRMED (frozen's PIN-n-24 lacks it). Note: the F4 binding rules and "one outcome per unit" (F6) are also new since the frozen copy but are not marked so.
76. l.94–95, a non-finite read makes its arm INDETERMINATE and never the unit NOT-RUN. CONFIRMED (l.1960–1963, l.4301).
77. l.95–96, under the other reading, NOT-RUN where this code writes VERDICTS. CONFIRMED.
78. l.97–100, PIN-n-25 paraphrase. CONFIRMED (l.1683–1686; l.4096–4141).
79. l.101–102, PIN-n-26 is two whole lines and v1.0 must carry both. CONFIRMED (l.1687–1689; `lock_route`).
80. l.103–104, PIN-n-16 amended. CONFIRMED (l.1655–1658; `tau4_drop` l.2386 keeps a null `exceeds_tau4`).
81. l.106, the binomial batch is not checked. CONFIRMED (no such check; docstring l.4028–4029).
82. l.106–107, its counting is the runner's and no outcome reads it. CONFIRMED (only copied into the output, l.4337).
83. l.108, there is no check that LOCK-n v1.0 was committed by D_n. CONFIRMED.
84. l.108–109, whether the unit runs is the Clock's, and a Clock NOT-RUN comes through `not-run`. CONFIRMED (l.2992).
85. l.110–111, the battery builds every report it reads to n-build's counting, with `example_report` for not-campaign. CONFIRMED (l.3053–3087; l.3475).
86. l.111, the runner writes no STOP report yet. CONFIRMED (REPO/valence_core/n/runner.py l.335, `"stop": None`).
87. l.111–112, the first report n-build's code writes is the first independent input. CONFIRMED (follows from 85–86).
88. l.114–115, the canonical run waits for the answers to Q1–Q9 (`8e3bf91`) and for G-CAL-n's dose map. CONFIRMED (8e3bf91's subject; no answers commit since in `git log`; docstring l.16–18 and l.23–26).
89. l.116, VERDICTS of record come after the campaign. CONFIRMED (proposal §8 steps 14–15).
90. l.117–118, every Python run was inside a granted window. UNVERIFIABLE (the coordinating session's grants would settle it).
91. l.118, one process at a time, `nice -n 19`, foreground, temp folders outside the repository. UNVERIFIABLE in part:
    - run_mutants.sh l.9–21 runs a sequential loop under `nice -n 19`;
    - the battery's temp folders are system temp folders (out_r3/M65.out);
    - `nice` is not visible in the battery runs' INVOCATION lines.
92. l.119, a window for "up to three runs" before the review. UNVERIFIABLE.
93. l.119–120, two runs: 179/181, then 181/181 after a battery fix. CONFIRMED (runs/v2_1.out fails only gread-package "no exception" and the coverage check; v2_2.out is 181/181; frozen l.3177 has the package fix).
94. l.121, the window after the fixes named one battery run and then the 66. UNVERIFIABLE.
95. l.121–122, two battery runs (183/185, 185/185), then the 66 mutant runs. CONFIRMED (v2r2_1, v2r2_2; 66 out_r2 outputs).
96. l.122, "after the fix in the review raw's §5". **FAIL**: that fix is described in the raw's §6; §5 is the values-check's code finding. Fix: "§6".
97. l.123, the window after pass 1 named one battery run and the 68. UNVERIFIABLE.
98. l.123–124, one battery run (185/185), then the 68 runs. CONFIRMED (v2r3_1.out ran base3; 68 out_r3 outputs).
99. l.124, "it held exactly that". UNVERIFIABLE.
100. l.125, the run of record from `scripts/` in the commit window. UNVERIFIABLE (future).
101. l.127–128, the one departure, told at release. UNVERIFIABLE (messages). Consistent with v2r2_1 and v2r2_2.
102. l.130–131, what is committed by path; not pushed. UNVERIFIABLE (future).
103. l.131, next: the coordinating session verifies. UNVERIFIABLE (plan).
104. l.131–132, the canonical run waits for the seat and G-CAL-n. CONFIRMED (as 88).

##### Text 2: SCRATCH/v2/raw/review.md

105. l.1, PI date 2026-11-16. CONFIRMED.
106. l.3, the raw is for the entry "n package — scripts/n_analyze.py, the verdicts command". CONFIRMED (the entry's headline).
107. l.5, the draft at `0b555476…843c`. CONFIRMED.
108. l.5, "frozen as a copy before the review". UNVERIFIABLE (timing). Consistent: findings.md says "unchanged at the end".
109. l.6–7, against `2822721` the draft adds `verdicts` with §16, PIN-n-23 to PIN-n-26 and its battery group. CONFIRMED (`diff committed-2822721.py frozen`: §16 at 3583–3831, `main`, PINS 1670–1683, the `_bt_*` helpers, `battery()`, 12 VD ids).
110. l.7–9, the other changes (`gread_table` −1 row, `dir_slopes`, `run_not_run`, `_bt_write_campaign`, `EXPECTED_CHECKS` 171→181, the docstring) and the absolute repository line. CONFIRMED (hunks 704–707, 2151, 2912–2925, 2422–2429, 859, 31–32, 49).
111. l.9–10, subagent under a brief. UNVERIFIABLE.
112. l.10–11, the spec and the schema, with their hashes. CONFIRMED (findings.md "Spec read").
113. l.11–12, it read the untracked runner.py and probe.py only to check the analyzer's claims. CONFIRMED (findings.md; `git status` shows `??` for both).
114. l.12, "It ran nothing". CONFIRMED as reported (findings.md l.17).
115. l.12–13, F1–F6 MINOR, F7–F12 NOTEs, B1–B4. CONFIRMED.
116. l.13–14, V01–V38 were written against the frozen copy. CONFIRMED (each V `.old` occurs exactly once in frozen).
117. l.14–15, predictions 10/28, with V08 as equivalent. CONFIRMED.
118. l.16, not run on the frozen copy. UNVERIFIABLE (as 50).
119. l.16–17, re-expressed as M01–M38 and run on the fixed draft. CONFIRMED.
120. l.18–19, every finding disposed of in §3. CONFIRMED.
121. l.20, M01–M38 re-express V01–V38. CONFIRMED.
122. l.20–21, M39–M66 "on the fixes and on two checks … (M47, M52)". **FAIL** (as 55; same fix).
123. l.22, first run on `b5328332…78c2`, 185/185. CONFIRMED (hash; v2r2_2.out is 185/185 but records no hash, which is consistent).
124. l.22–23, 65 of 66 killed; M08 survived and is equivalent, as said of V08. CONFIRMED.
125. l.24, pass 1 found that the secondary was written before VERDICTS was formed. CONFIRMED (pass1.md's observation; base2).
126. l.25–26, the re-run with M67 and M68 on `56c9b788…5b5b` (185/185): 67 of 68 killed, M08 the survivor. CONFIRMED.
127. l.27–28, the battery runs: 183/185, then 185/185, and 185/185 on the re-run's base. CONFIRMED.
128. l.27–28, the battery's hook refused `data/n/verdicts`. CONFIRMED (v2r2_1.out l.182: `hook.caught[:3]` = `data/n/verdicts` twice, then the first probe).
129. l.27, "a case of the new battery stat'ed" it. UNVERIFIABLE (the output names no case; the pre-fix draft would settle it). Consistent with base2 l.3563's comment.
130. l.29, the committed bytes differ in the repository line only (§7). CONFIRMED.
131. l.31, every run was in a granted window. UNVERIFIABLE.
132. l.31–32, one process, `nice`, foreground, temp outside the repository. UNVERIFIABLE in part (as 91).
133. l.32, nothing ran on a model or on the box. UNVERIFIABLE.
134. l.32–33, an exact, unique replacement applied to a fresh copy of the base. CONFIRMED (run_mutants.sh l.10–17; all 66 and 68 copies checked against base plus replacement).
135. l.33–34, `--selftest`, and "killed" means a non-zero exit. CONFIRMED (run_mutants.sh l.18–21).
136. l.38–39, the Write tool refused, so the report came in the hand-back and Code saved it. UNVERIFIABLE (findings.md's preamble is Code's own note; the subagent's transcript would settle it).
137. l.39, headings moved down one level. CONFIRMED.
138. l.39–40, the moving draft was this session's own. UNVERIFIABLE (the reviewer wrote "another session's edits"). Consistent: v2_*.out and v2r2_*.out ran SCRATCH/v2/n_analyze.py, the file the reviewer saw move.
139. l.40–41, every finding and its line numbers refer to the frozen copy. CONFIRMED (F1 2948–2957, F2 3882, F3 3701–3708, F4 3676–3687 and F5 3857–3868 all land on the cited code).
140. l.43–135, §1 equals findings.md from "Nothing in the production path" to the end, headings one level down. CONFIRMED (93 identical lines; the raw adds one blank line before §2).
141. l.36, "(unedited in substance)". CONFIRMED against findings.md.
142. l.139, the reviewer's table (`mutants.tsv`, five columns), as written. CONFIRMED.
143. l.139–140, not run on frozen. UNVERIFIABLE.
144. l.140, M01–M38 re-express them (§4). CONFIRMED.
145. l.142–181, the §2 table. CONFIRMED (38 rows identical to the tsv).
146. l.185–186, the §3 lead-in. CONFIRMED.
147. F1: the refusal and its quoted message. CONFIRMED (l.2992–2994).
148. F1: VD-ONE-OUTCOME (nothing written) and M56. CONFIRMED (l.3387–3394).
149. F2: registered in PIN-n-24 and in the docstring. CONFIRMED (l.4252–4254).
150. F2: the reading. CONFIRMED.
151. F2: in the scenario, VERDICTS with N1 INDETERMINATE; the other reading gives NOT-RUN; the seat decides; the entry flags it. CONFIRMED.
152. F3: exact cells by both shas, and exact layers. CONFIRMED (l.4106–4113).
153. F3: the probe lists every cell. CONFIRMED (probe.py l.88–95).
154. F3: the four tests, M13 and M14. CONFIRMED.
155. F4: `cap.used_ms`, computed as in runner.py. CONFIRMED (l.4059; runner.py l.374 and l.470).
156. F4: the pause-kind checks. CONFIRMED (l.4084–4087).
157. F4: resumptions. CONFIRMED (l.4067–4072).
158. F4: three rules "added while the review ran, from n-build's answer of 2026-11-16". UNVERIFIABLE (timing and source). Consistent: absent from frozen, present from base2 on.
159. F4: the three rules and their tests. CONFIRMED (l.4061–4066, l.4088–4092).
160. F4: binomial not checked; the docstring and the entry say so. CONFIRMED.
161. F4: tests and M42–M50. CONFIRMED. Note: M47 is the pre-existing pause-read check, as §4 says.
162. F5: the whole line is required, and a v0.1 G-VER-STOP report is refused rather than given a NOT-RUN. CONFIRMED (`lock_route` at l.4287 precedes the NOT-RUN branch at l.4301).
163. F5: lock-version and M39. CONFIRMED.
164. F5: D_n is not checked, with its reasons. CONFIRMED.
165. F6. CONFIRMED.
166. F7. CONFIRMED (l.4349, l.4346, l.4325–4331, l.4212–4217; VD-COMPLETE l.3219–3226).
167. F8. CONFIRMED (l.4260, l.4304–4306).
168. F9. CONFIRMED.
169. F10. CONFIRMED (l.2925–2933; l.3542–3543).
170. F11: documented in the docstring. CONFIRMED.
171. F11: the sha checks are tied by `check_report`; M51 is killed. CONFIRMED (schema l.1236–1241; out_r3/M51 shows the identity case refused by the sha check's message).
172. F11: the per-arm check is "implied by" the per_arm rule, the plan and cell-record checks and the cells check. IMPRECISE (as 64: needs the identity check). The parenthetical about a lie carried into the cells is CONFIRMED.
173. F11: the per-arm cases expect "SchemaError at report.per_arm.<arm>". CONFIRMED (l.3489–3491).
174. F12. CONFIRMED (l.2920–2922; exit 4 under `verdicts`, l.4413–4415).
175. B1: TAU/4-only shifts, and n 120 against 160, rand_00 null, tau4-emptied, N1 INDETERMINATE. CONFIRMED (l.3158–3164, l.3261–3273).
176. B1: the other six bullets. CONFIRMED.
177. B1: the mutant list. CONFIRMED.
178. B2. CONFIRMED (l.3020–3087, l.3181, l.3211–3218, l.3498).
179. B3: VD-COMPLETE's reads. CONFIRMED.
180. B3: VD-PLAIN new; VD-SENSITIVITY reaches the `dir_slopes` fix. CONFIRMED.
181. B3: VD-SOME-ARMS exposure. CONFIRMED (l.3317–3325).
182. B3: the seven new refusal cases. CONFIRMED (none is among frozen's 20 cases).
183. B3: the two VD-PRECHECK cases. CONFIRMED (l.3593, l.3596).
184. B3: CMD-NOTRUN. CONFIRMED (l.3855–3866).
185. B3: the mutant list. CONFIRMED.
186. B4: stop is null, the cap's used time is as in runner.py, the first independent input, the entry flags it. CONFIRMED.
187. B4: "as its answer of 2026-11-16 states it". UNVERIFIABLE.
188. §4 l.285, "same defect, new anchor". CONFIRMED. Note: 23 of the 38 keep the reviewer's `.old`/`.new` byte for byte; 15 are re-anchored (M04, M06, M10, M11, M13, M14, M21, M22, M23, M25, M29, M31, M32, M35, M38).
189. §4 l.285–287, M39–M66 "(M47 …; M52 …)". **FAIL** (as 55).
190. §4, M67 and M68 are on §5's fix. CONFIRMED.
191. §4, each base was frozen before its runs. UNVERIFIABLE (timing). Consistent: the copies equal base plus replacement.
192. §4, the first run on `b5328332…78c2` (185/185, §6): M01–M66. CONFIRMED.
193. §4, "in six parts". UNVERIFIABLE.
194. §4, 65 killed by their expected killers; M65 by the group exception. CONFIRMED.
195. §4, "the failing cases were read from each run's detail". UNVERIFIABLE (procedure).
196. §4, M08 survived. CONFIRMED.
197. §4 l.293–295, the equivalence reason. IMPRECISE (as 64).
198. §4, "The reviewer said the same of V08 (F11)". CONFIRMED in substance (the reviewer's version names the identity check).
199. §4, after this run, the per-arm cases and the docstring changed. CONFIRMED (`diff base2 base3`).
200. §4, the re-run on `56c9b788…5b5b`, same spec with M04's and M66's labels corrected, M67 and M68 added. CONFIRMED (M01–M66 `.old`/`.new` are byte-identical in r2 and r3; the tsv diff shows only those two labels plus the two new rows).
201. §4, 67 killed (M65 again by an exception); M08 survived. CONFIRMED.
202. §4 l.304, the last cell is the first failing check, cut at 80 characters, with `<tmp>` and `<repo>`. CONFIRMED.
203. §4, rows M01–M64 and M66–M68. CONFIRMED (regenerated from mutants_r3/mutants.tsv and out_r3/*.out with a character cut after masking: identical).
204. §4 l.373, M65's cell. IMPRECISE (minor): after masking, the line is complete at 76 characters, yet the cell ends in "…", which marks a cut that never happened. Fix: drop the "…" in M65's cell, or say that "…" closes every cell.
205. §5, pass 1 reported that the draft after round 2's first run wrote the secondary before `_plain` and `json_text`. CONFIRMED.
206. §5, a STOP there would have left the secondary alone. CONFIRMED.
207. §5, in the frozen copy every `_plain` ran before either write and `json_text` could not STOP. CONFIRMED (frozen `run_verdicts` l.3907–3933; `json_text` l.2909–2910, no `allow_nan`).
208. §5, the F7 and F12 fixes reopened it. CONFIRMED.
209. §5, the fix's order: form, sha from text, one outcome, write. CONFIRMED (l.4329–4349).
210. §5, `write_all_once`. CONFIRMED.
211. §5, VD-WRITE-ONCE. CONFIRMED (l.3237–3247).
212. §5, VD-PLAIN: no output directory created. CONFIRMED (l.3573–3587).
213. §5, M67 and M68. CONFIRMED.
214. §6, the window after the fixes and its terms. UNVERIFIABLE.
215. §6, first run 183/185. CONFIRMED.
216. §6, every verdicts check passed. CONFIRMED (all 14 verdicts-group lines PASS; the only FAILs are l.182 and l.185).
217. §6, the hook check failed, and coverage with it. CONFIRMED (`['STR-OPEN-HOOK']`).
218. §6, `data/n/verdicts` refused and recorded twice beside its own probe. CONFIRMED (l.182).
219. §6, that the two calls were stats. UNVERIFIABLE (the hook records paths, not call kinds).
220. §6, both came from the VD-PRECHECK case that passed `<repo>/data/n/verdicts`. UNVERIFIABLE (the pre-fix draft is not among the sources).
221. §6, `Path.resolve()` stats each part. CONFIRMED (standard-library `realpath` lstat's each component; consistent with the record).
222. §6 l.406–407, "the hook refuses any stat under data/n's ckpt, reports and verdicts". IMPRECISE (minor):
    - the path refused was `data/n/verdicts` itself;
    - `_barred` (l.1730–1741) bars those directories themselves, any unit's `data/<unit>/{ckpt,reports,verdicts}`, `data/mf3` and `results/raw`.

    Fix: "refuses any stat of data/n's ckpt, reports or verdicts directory or anything in it".
223. §6, the case now passes `<repo>/data`. CONFIRMED (l.3596).
224. §6, as the `not-run` precheck's case already did. CONFIRMED (2822721 l.3181; frozen l.3500).
225. §6, second run 185/185, 188 ids, exit 0. CONFIRMED.
226. §6, frozen right after, with no edit between. UNVERIFIABLE.
227. §6, beyond the window's wording; told at release. UNVERIFIABLE.
228. §6, the window after pass 1 and its terms. UNVERIFIABLE.
229. §6, one run (185/185, 188, exit 0) on the frozen base itself, then the 68. CONFIRMED (v2r3_1.out's INVOCATION names the base3 file).
230. §6, "held exactly what it named". UNVERIFIABLE.
231. §7, the diff of base3 against the committed file, whole. CONFIRMED.
232. §7, the path shown as `<repo>`. CONFIRMED.
233. §7, one line changes: the repository line, from `__file__`. CONFIRMED.
234. §7, the run of record is on these bytes. UNVERIFIABLE (future).
235. §7, the block. CONFIRMED (identical to a fresh `diff`, masked).

##### Text 3: SCRATCH/v2/vc/pass1_dispositions.md

236. Every item accepted; the observation accepted as a code change. CONFIRMED.
237. The raw's sections renumbered (§5 new, §6 battery runs, §7 committed bytes). CONFIRMED for the raw. Not carried into the entry's two references (69, 96).
238. 117: carried and moot; new base; repository line only; post-run edits are in base3. CONFIRMED (`diff base2 base3`, `diff base3 final`; raw l.29 and §7).
239. 169: the table is the re-run's, from out_r3, nothing by hand. CONFIRMED (identical to my regeneration).
240. 169: the quote is kept and the repository path is masked before the cut. CONFIRMED.
241. 22. CONFIRMED (entry l.27–28).
242. 23: "the entry now lists every refusal, in the order checked". IMPRECISE: the order and the listed items are carried, but "every" is overstated (see 20).
243. 38. CONFIRMED.
244. 49. CONFIRMED (entry l.61–63; raw §3 F5).
245. 53/110/160: taken as given in both texts, with M47 and M52 named in §4. CONFIRMED as a carry. The carried wording FAILs (55, 122, 189).
246. 55. CONFIRMED (entry l.68–72).
247. 58/150/166: taken as given. CONFIRMED as a carry. The carried wording is IMPRECISE (64, 172, 197).
248. 64: the wording, and `8e3bf91`'s subject. CONFIRMED.
249. 71. CONFIRMED.
250. 81. CONFIRMED.
251. 98. CONFIRMED.
252. 115/174. CONFIRMED (raw l.27 and l.405); see 222 for the rule sentence.
253. 163: the labels corrected. CONFIRMED. Note: `schema-blind` is a failure key added by l.3542–3543, not one of the 43 cases.
254. 167: character cut. CONFIRMED (the "§" rows reproduce exactly).
255. The contradiction is reconciled; there were three windows. CONFIRMED (the texts no longer conflict).
256. "both texts now name each one". **FAIL**: the review raw names only the second and third windows (§6 l.401–415); the pre-review window (179/181, 181/181) is only in the entry. Fix: "the entry names all three; the review raw, which reports the runs from round 2 on, names the second and third."
257. Window 1's terms. UNVERIFIABLE.
258. Window 1's two runs. CONFIRMED.
259. Window 2's terms. UNVERIFIABLE.
260. Window 2's runs (183/185, 185/185, the 66). CONFIRMED.
261. The departure, told at release. UNVERIFIABLE.
262. Window 3's terms. UNVERIFIABLE.
263. Window 3's runs (185/185, the 68). CONFIRMED.
264. "exactly that". UNVERIFIABLE.
265. Observation: texts formed first, sha from text. CONFIRMED.
266. `write_all_once`. CONFIRMED.
267. VD-WRITE-ONCE and VD-PLAIN gained cases; M67 and M68 test them. CONFIRMED.
268. 185/185 on `56c9b788…5b5b`. CONFIRMED.
269. 67 of 68, M08 equivalent. CONFIRMED.
270. `FINAL_SHA` is `b5c87c8b…6aab`, the commit form of base3. CONFIRMED.

#### Totals

270 claims: **212 CONFIRMED, 7 IMPRECISE, 6 FAIL, 45 UNVERIFIABLE**.

| Text | Claims | CONFIRMED | IMPRECISE | FAIL | UNVERIFIABLE |
|---|---|---|---|---|---|
| Entry | 104 | 82 | 2 | 3 | 17 |
| Review raw | 131 | 102 | 4 | 2 | 23 |
| Dispositions | 35 | 28 | 1 | 1 | 5 |

#### FAIL items and fixes

- **55 / 122 / 189** (entry l.65–67; raw l.20–21 and §4 l.285–287): "two checks the frozen copy already had (M47, M52)". In fact seven: M40, M41, M51, M63 and M64 mutate code that is verbatim in frozen, and no V mutant touched them. Fix: "21 on the fixes (M39, M42–M46, M48–M50, M53–M62, M65, M66) and 7 on checks the frozen copy already had that the reviewer's mutants did not reach (M40, M41, M47, M51, M52, M63, M64)".
- **69** (entry l.80): "(the raw's §6)" → "(the raw's §7)".
- **96** (entry l.122): "the fix in the review raw's §5" → "§6".
- **256** (dispositions): "both texts now name each one" → "the entry names all three windows; the review raw names the second and third".

#### IMPRECISE items and fixes

- **20 / 242**: the refusal list omits `schema_module`'s refusal (after the date), `load_campaign`'s refusals on the cells (at the binding step) and unreadable report or lock files. Add them, or say "include".
- **64 / 172 / 197**: M08's equivalence also needs `report_problems`' identity check. Fix: "…and report_problems' own identity and cells checks…" (the reviewer's V08 reason names it).
- **204**: M65's cell ends in "…" though nothing was cut (76 characters).
- **222**: "any stat under data/n's ckpt, reports and verdicts" → "any stat of data/n's ckpt, reports or verdicts directory or anything in it".

#### First-pass dispositions: carried or not

- Intro (renumbering): carried in the raw; **not** carried into the entry's §6/§5 pointers (69, 96).
- 117: carried; true.
- 169: carried; true (M65's "…" is a new nit, 204).
- 22: carried; true.
- 23: carried; "every refusal" overstated (20).
- 38: carried; true.
- 49: carried; true.
- 53/110/160: carried in both texts; the wording itself undercounts (55/122/189).
- 55: carried; true.
- 58/150/166: carried; the wording omits the identity check (64/172/197).
- 64: carried; true.
- 71: carried; true.
- 81: carried; true.
- 98: carried; true.
- 115/174: carried; true (the rule sentence in §6 still says "under", 222).
- 163: carried; true.
- 167: carried; true.
- Contradiction 91/170: reconciled; "both texts name each window" is false (256).
- Observation (write order): carried (raw §5, entry l.76–79); code and tests confirmed.
- Placeholder: carried (entry l.7); true.

#### Observation outside the claims (no verdict)

No battery case reaches `write_all_once` through `run_verdicts`. VD-WRITE-ONCE's `run_verdicts` case ("another date") is refused on the secondary first, with "write-once" in the message whether or not the helper is used. Its third case calls `write_all_once` directly. VD-PLAIN's STOP fires before any write.

So a mutant that replaced l.4349 with two sequential `write_once` calls would likely survive. That mutant would bring back the old failure: with an old VERDICTS present and no secondary, it writes a new secondary and then refuses VERDICTS. A case that closes the gap: run, delete the secondary, run again with another date, and assert both a refusal and no secondary.

## 4. Code's dispositions of the second pass

Every item is accepted. The observation outside the claims is accepted as a battery change, with a third mutant run of
its own. The first pass's dispositions (§2) are left as pass 2 read them; where one was false, the correction is below.

### FAIL

- **55 / 122 / 189** (the new mutants' targets). Taken as given in the entry, the review raw's lead-in and its §4,
  which list both groups:
  - 21 on code new since the frozen copy (M39, M42–M46, M48–M50, M53–M62, M65, M66), counting the three pause rules
    added while the review ran (M44, M45, M50) among them;
  - 7 on checks the frozen copy already had that the reviewer's mutants did not reach (M40, M41, M47, M51, M52, M63,
    M64).
- **69**: "(the raw's §7)".
- **96**: "(the fix in the review raw's §6)".
- **256**: the first pass's disposition said both texts name each window; the review raw named only the later two. The
  review raw's §6 now names the pre-review window as well, so that disposition holds as written now. It was false
  when pass 2 read it.

### IMPRECISE

- **20 / 242**: the entry's list of refusals now adds:
  - the schema module that is not the pinned bytes, after the date;
  - a stage report or lock that cannot be read;
  - the cells the reader refuses (the schema's cell checks, their bytes, the plan, the cross-record checks), at the
    binding step;
  - a G-READ-n artifact or cosines file that cannot be read.
- **64 / 172 / 197**: the identity check is added to M08's equivalence in the entry, the review raw's §3 (F11) and its
  §4. §4 names all three cases: a lie confined to `per_arm`, a lie carried into the cells' record counts, and a lie
  carried into the report's identity. `report_problems`' docstring says the same: "once the identity is the cells' and
  the cells are the files on disk". That is a docstring change in the third run's base.
- **204**: the table generator now adds "…" only where a cut was made, and §4 says so.
- **222**: "any stat of data/n's ckpt, reports or verdicts directory, or of anything in them".

### Notes taken (no verdict)

- **188**: §4 now says that 23 of M01–M38 keep the reviewer's `.old` and `.new` byte for byte, and names the 15 at a
  new anchor.
- **253**: M66's expected killer is now called `schema-blind`, "the failure key of VD-REFUSE's blind clause", not a
  case.

### The observation outside the claims (the battery gap)

Accepted as a battery change (the review raw's §5):
- VD-WRITE-ONCE runs `verdicts`, deletes the secondary, and runs it again with another date. It asserts a refusal
  naming `N-pod_VERDICTS.json`, and that no secondary was written.
- M69, which replaces `write_all_once` in `run_verdicts` with two `write_once` calls, tests the new case.
- The third run's base (sha256 `0e82b54c…358f`) differs from the second's by that case and the docstring sentence of
  64; no production behaviour changed. Its results are in the review raw's §4 and §6.
- The commit form is the third run's base with the repository line derived from `__file__`: sha256 `34a513f9…98b6`.

## 5. The third pass: the checker's report, whole

### Values-check, pass 3 (blind): the `verdicts` entry, its review raw, and pass 2's dispositions

**Bottom line.** I checked 290 claims: 238 CONFIRMED, 7 IMPRECISE, 0 FAIL, 45 UNVERIFIABLE.
- **Hashes and blocks:** every hash and every abbreviation checks out. §1 equals findings.md, the §2 table equals the reviewer's tsv, the §4 table equals my own regeneration, and §7 equals a fresh `diff`.
- **Mutants:** every copy in out_r2, out_r3 and out_r4 is its base plus exactly one replacement. The kills are 65/66, 67/68 and 68/69, with M08 the survivor each time. Every expected killer is among its run's unreached ids. The six mutants said to raise inside the verdicts group are exactly as stated (read from the .out files).
- **Code:** the write path behaves as described. The M08 equivalence argument holds against the schema.
- **Dispositions:** every second-pass disposition is carried. One of them (256) claims more than is now true.
- **The 7 IMPRECISE items are all wording:**
  - "no case reached `write_all_once`" (entry and raw §5), though VD-COMPLETE reaches it;
  - "in the same way" for the third run (entry);
  - three loose sentences in raw §5;
  - 256's "holds as written now".

**How I checked.**
- Tools: `shasum -a 256` with `cut`, `diff`, `cmp`, `/usr/bin/grep`, `sed`, `awk`, and perl one-liners for occurrence counts, replacement checks, masking and the 80-character cut. Also `git show <rev>:<path>`, `git log --format`, `git show --name-status`, `git ls-files`, and a `git status --porcelain` scoped to named paths.
- I ran no Python or other interpreter on the code. I did not run gen_table.pl; I regenerated the §4 table independently.
- I did not touch anything under `data/`. I edited nothing in the repository.
- My working files went to SCRATCH/v2/vc/pass3_tmp and are removed.
- I did not write SCRATCH/v2/vc/pass3.md: my standing instructions bar report files. This hand-back is the only copy.
- Names used below:
  - "final" = SCRATCH/v2/final/n_analyze.py;
  - "frozen" = review/n_analyze.verdicts-under-review.py;
  - "base2", "base3", "base4" = review/n_analyze.round{2,3,4}-verdicts-base.py;
  - "schema" = `git show 14e65d8:valence_core/n/schema.py`.

#### Digests (by tool)

| File | sha256 (cut 1–8 … 61–64) | Texts |
|---|---|---|
| final | `34a513f9…98b6`; the full sha256 equals entry l.7 character for character | ✓ (entry l.7; dispositions l.50) |
| frozen | `0b555476…843c` | ✓ |
| base2 | `b5328332…78c2` | ✓ |
| base3 | `56c9b788…5b5b` | ✓ |
| base4 | `0e82b54c…358f` | ✓ |
| `2822721:scripts/n_analyze.py` (= HEAD's = committed-2822721.py) | `4f63903f…5d73` | ✓ |
| `14e65d8:valence_core/n/schema.py` (= HEAD's = the working tree's) | `4bed3f9a…4665` | ✓ |
| PROPOSAL-n-bk-reconciliation-v0_2.md (HEAD = the working tree) | `30a3d0f5…04f4` | ✓ |

**Diffs between the bases:**
- base4 → final: one hunk, `54c54` (the repository line).
- base3 → base4: the VD-WRITE-ONCE pair case, and one docstring sentence in `report_problems` ("once the identity is the cells' and").
- base2 → base3:
  - code: `write_all_once`, and `run_verdicts`' write path and docstring;
  - the PIN-n-16 amendment;
  - battery: VD-WRITE-ONCE's direct case, VD-PLAIN's run_verdicts STOP, and the per-arm cases' expected message;
  - the `report_problems` docstring;
  - line splits.

The commits `2822721`, `14e65d8` and `8e3bf91` exist, and their subjects match the texts. `8e3bf91`'s raw has "## 3. Not questions: Code's readings, declared (each strikable until LOCK-n v1.0)". No commit since it answers G-ANL-n's Q1–Q9.

#### Claims

##### Text 1: entry.md

1. l.1, dated 2026-11-16. CONFIRMED (the session date; the review raw's PI date).
2. l.1, PROPOSAL-n v0.2 §8 step 15. CONFIRMED (proposal l.159, step 15).
3. l.1–2, on n-build's `n-report-v1` and `n-gread-v1` at `14e65d8`. CONFIRMED (schema l.994–995; 2822721's subject calls 14e65d8 "n-build's schema commit").
4. l.2–3, it gives VERDICTS and secondary DVs, or the NOT-RUN derived from the stage report. CONFIRMED (final `run_verdicts` l.4257–4360).
5. l.3, "Its battery passes 185/185". CONFIRMED on the latest run of the same code: runs/v2r4_1.out ran base4 (185/185), and base4 differs from final only at l.54. The run of record is pending.
6. l.3, "reviewed blind". UNVERIFIABLE (the reviewer's brief would settle it). findings.md is titled "Blind review…".
7. l.3–4, 68 of 69 mutants killed. CONFIRMED: 68 out_r4 runs have ≥2 `[FAIL]` lines; M08 is 185/185 with none.
8. l.4, the survivor is equivalent. CONFIRMED (see 66).
9. l.4–5, four PINs (PIN-n-23 to 26) and an amendment to PIN-n-16, Code's readings, flagged. CONFIRMED (final PINS l.1655–1658 and l.1672–1689). 2822721 has 12 PINs, none of 23–26, and its PIN-n-16 ends "reads with no re-computation are kept".
10. l.5, model-free: nothing ran on a model or on the box, and no stage ran. UNVERIFIABLE (session conduct). Consistent: every run in the sources is `--selftest`, and STR-NO-HEAVY passes.
11. l.6–7, the file's full sha256. CONFIRMED.
12. l.7, `4f63903f…5d73` at `2822721`. CONFIRMED.
13. l.7–8, pinned to the schema at `14e65d8` (`4bed3f9a…4665`). CONFIRMED (l.1882).
14. l.8, binds PROPOSAL-n v0.2 by sha256 (`30a3d0f5…04f4`). CONFIRMED (l.60).
15. l.9–13, the four commands and their options, with `verdicts` new. CONFIRMED (main l.4374–4392). 2822721's docstring says verdicts "is added when their forms are committed".
16. l.15–16, the run of record: 185/185, all 188 ids, exit 0. UNVERIFIABLE (not yet run). Consistent: v2r4_1.out; `EXPECTED_CHECKS = 185` (l.866); `_REQ` hand-counted at 188 (l.868–906); exit 0 follows from main l.4394–4395.
17. l.17, the selftest raw's name. UNVERIFIABLE (not yet written). It follows the form of the committed `…_build_selftest.txt`.
18. l.19, every refusal before anything is written, exit 2. CONFIRMED:
    - the precheck returns 2 in main l.4411–4414;
    - AnlRefusal returns 2 at l.4418–4420;
    - every raise precedes `write_once`/`write_all_once`;
    - `write_all_once` checks before it writes (l.2960–2963).
19. l.19, "in the order they are checked". CONFIRMED: precheck l.4411 → date l.4273 → schema l.4275 → report l.4276–4283 → lock l.4284–4295 → cells l.4301–4307 → G-READ-n and cosines l.4319–4325 → one outcome and write-once (l.4315–4317 on the NOT-RUN path; l.4356–4357 otherwise).
20. l.20–22, the precheck bullet. CONFIRMED (`verdicts_precheck` l.4236–4254; `committed_problems` l.3658–3672).
21. l.23, the date. CONFIRMED (l.4273).
22. l.24, a schema module that is not the pinned bytes. CONFIRMED (l.1904–1906). Its sibling refusal, an import from another file (l.1909–1910), is folded in.
23. l.25, a report that cannot be read, or that `check_report` refuses, shown by field path alone. CONFIRMED (`_load_checked` l.3990–3998; `_err_where` l.2929–2930).
24. l.25–26, a PAUSE. CONFIRMED (l.4278–4280).
25. l.26, not a campaign of PROPOSAL-n v0.2. CONFIRMED (l.4282–4283).
26. l.27–29, the lock's five conditions, in code order. CONFIRMED (l.4284–4295; `lock_route` l.3981–3987).
27. l.30, the cells the reader refuses. CONFIRMED (`load_campaign` l.1966–2028; `_cross_checks` l.2031–2059). The parenthetical summarises them.
28. l.30–32, a report not bound to the cells (PIN-n-24). CONFIRMED (`report_problems` l.4041–4101).
29. l.32–33, a report with no cell beside a non-empty campaign directory. CONFIRMED (l.4306–4307).
30. l.34–35, G-READ-n's artifact missing, unreadable, refused or unbound; the cosines file unreadable or malformed. CONFIRMED (l.4319–4325; `_load_gvec` l.4215–4225).
31. l.36–37, an output of the other outcome present, or one with other bytes. CONFIRMED (l.3001–3005, l.2949–2953, l.2960–2962).
32. l.38–39, the NOT-RUN and its three causes. CONFIRMED (l.3971, l.4309–4318).
33. l.39–40, the NOT-RUN's bindings: report, end state, STOP record, lock, schema module. CONFIRMED (l.4312–4314; VD-NOTRUN-* l.3368–3382).
34. l.41–42, the reader path, with the route read from the lock. CONFIRMED (l.4326–4330, l.4295).
35. l.42–43, both outputs formed before either is written; a STOP (exit 4) writes nothing. CONFIRMED (l.4337–4357; main l.4421–4423; VD-PLAIN l.3580–3594).
36. l.43, the secondary, then VERDICTS, write-once. CONFIRMED (l.4357).
37. l.45, tuple, outcomes, sentences, §4's figures. CONFIRMED (l.4339–4341).
38. l.46, G-LEAK-n's and G-READ-n's tables. CONFIRMED (l.4341, l.4343).
39. l.47, both counter forms. CONFIRMED (l.4344).
40. l.48, exposure (PIN-n-23). CONFIRMED (l.4347).
41. l.49, the TAU/4 row. CONFIRMED (l.4348–4351).
42. l.50, the cosines when given. CONFIRMED (l.4333, l.4339).
43. l.51, every input and the secondary by sha256. CONFIRMED (l.4296–4299, l.4333, l.4342, l.4352–4354).
44. l.52, one outcome per unit, in either command. CONFIRMED (l.2996, l.4315, l.4356; VD-ONE-OUTCOME).
45. l.53–54, what it prints, with no margin. CONFIRMED (l.4372; `verdicts_line` l.4363–4367; VD-STDOUT).
46. l.55–56, the review raw's name. UNVERIFIABLE (not yet written).
47. l.57, frozen at `0b555476…843c`. CONFIRMED.
48. l.57–58, a subagent under a brief quoting items 1–5. UNVERIFIABLE.
49. l.58–59, F1–F12 and B1–B4. CONFIRMED.
50. l.59, 38 mutants; predicted 10 killed and 28 surviving. CONFIRMED (tsv: "no" ×10, "yes" ×27, "yes (equivalent)" ×1).
51. l.59–61, nothing wrong in the production path on what the runner and probe write today. CONFIRMED (findings.md l.7).
52. l.61, the main finding was the battery. CONFIRMED.
53. l.62, not run on the frozen copy. UNVERIFIABLE. Consistent: there is no V*.out or V*.py anywhere under n9.
54. l.64–65, the fixed list. CONFIRMED (raw §3 and the code it cites).
55. l.66, F2 registered in PIN-n-24. CONFIRMED (l.1679–1681).
56. l.67, kept: F11 (documented), F5's D_n half, B4. CONFIRMED (docstring l.4036–4040).
57. l.69, M01–M38 re-express the reviewer's 38. CONFIRMED.
58. l.70–71, 21 on code new since the frozen copy, with their ids. CONFIRMED: the count is 21, and none of their `.old` texts occurs in frozen.
59. l.71–72, 7 on checks frozen already had, with their ids. CONFIRMED:
    - the `.old` of M40, M41, M51, M52, M63 and M64 each occurs once, verbatim, in frozen;
    - M47's check is in frozen as `elif rid not in camp.records`, with the same message;
    - no V `.old` touches any of them.
60. l.73, M67 and M68 on pass 1's code finding, M69 on pass 2's battery finding. CONFIRMED (specs).
61. l.75, three runs. CONFIRMED (out_r2, out_r3, out_r4).
62. l.76–77, the first run: 66, 65 killed by expected checks, M65 by an exception in the group, M08 survived. CONFIRMED.
63. l.78–79, the second run: 68, 67 killed, M08 survived. CONFIRMED.
64. l.80–81, the third run: "69 mutants, 68 killed in the same way". **IMPRECISE.** Each was killed by its expected check, but not "in the same way" as the earlier runs. In the first run only M65 raised inside the group. In the third, M05, M06, M37, M41, M43 and M48 also raised: VD-COMPLETE failed, then the new case's `unlink()` hit FileNotFoundError on out_pair's secondary. Only 173 checks ran.
65. l.82, M08 equivalent, as the reviewer said of V08. CONFIRMED.
66. l.82–84, the reason. CONFIRMED (schema l.1134–1135, l.1246–1262; `report_problems` l.4045, l.4051):
    - `check_report` ties `planned` to the report's identity's plan, `obtained` to the report's cells' record sums, and `complete` to obtained == planned;
    - with identity == the cells' and cells == the files, the per-arm entries must equal `want`.
67. l.86–88, pass 1's finding: the secondary was written before VERDICTS was formed. CONFIRMED (base2 l.4292 writes it; VERDICTS is formed at l.4294–4309).
68. l.87–88, the fix. CONFIRMED (l.4337–4357, l.2957–2963).
69. l.88, VD-WRITE-ONCE and VD-PLAIN test it (M67, M68). CONFIRMED (out_r4: M67 leaves VD-WRITE-ONCE unreached; M68 leaves VD-COMPLETE, VD-PLAIN, VD-STDOUT and VD-WRITE-ONCE unreached).
70. l.89, "no battery case reached `write_all_once` through `verdicts`". **IMPRECISE.** In base3, VD-COMPLETE's run (written, written) and VD-WRITE-ONCE's repeat (identical, identical) both reach it. What no case reached was its refusal when the first output is absent or identical and the second has other bytes.
71. l.89–90, two `write_once` calls would have survived. CONFIRMED (by reading base3's battery: every case gives the same result under the two-call form).
72. l.90–91, the new case and M69. CONFIRMED (l.3242–3254). In out_r4, M69's only unreached id is VD-WRITE-ONCE.
73. l.92, repository line only (the raw's §7). CONFIRMED.
74. l.93–94, strikable until LOCK-n v1.0, as `8e3bf91`'s §3 readings are. CONFIRMED (l.1643; 8e3bf91's raw).
75. l.95–97, PIN-n-23. CONFIRMED (l.1672–1674; `exposure` l.4157–4170).
76. l.98–103, PIN-n-24's end-state rules and one outcome. CONFIRMED (l.1678–1682).
77. l.101, a standing pause is possible only under PI-STOP. CONFIRMED (schema l.1343–1344, and PAUSE is refused).
78. l.105–106, "New in it, from the review (F2)". CONFIRMED: frozen's PIN-n-24 lacks it. Note: F4's binding items, F6's "one outcome per unit", and n-build's launch-index and standing-pause rules were also added since frozen (pass 2's note 75, not taken). The optional wording "F2's reading, new in it from the review:" avoids the implication that F2's is the only addition.
79. l.106–107, a non-finite read makes its arm INDETERMINATE, never the unit NOT-RUN. CONFIRMED (l.1960–1963, l.4309).
80. l.107–108, the other reading. CONFIRMED.
81. l.109–112, PIN-n-25. CONFIRMED (l.1683–1686; l.4104–4149).
82. l.113–114, PIN-n-26; v1.0 must carry both lines. CONFIRMED (l.1687–1689; `lock_route`).
83. l.115–116, PIN-n-16 amended. CONFIRMED (l.1655–1658; `tau4_drop` l.2384–2386 keeps a null `exceeds_tau4`).
84. l.118–119, the binomial batch is not checked, and no outcome reads it. CONFIRMED (docstring l.4035–4036; the batch is only copied out at l.4345).
85. l.120, no D_n check. CONFIRMED.
86. l.120–121, the Clock's NOT-RUN comes through `not-run`. CONFIRMED (l.2992–2994).
87. l.122–123, the battery builds every report, except that the not-campaign case uses `example_report`. CONFIRMED (l.3053–3087, l.3482).
88. l.123–124, the runner writes no STOP report yet. CONFIRMED (REPO/valence_core/n/runner.py l.335, `"stop": None`).
89. l.124, the first independent input. CONFIRMED (follows from 88).
90. l.126–127, the canonical run waits for Q1–Q9 (`8e3bf91`) and G-CAL-n's map. CONFIRMED (docstring l.16–18; `git log` since 8e3bf91 has no answers to them).
91. l.128, VERDICTS of record come after the campaign. CONFIRMED (proposal §8 steps 14–15).
92. l.129–130, every Python run was in a granted window. UNVERIFIABLE.
93. l.130, one process at a time, `nice -n 19`, foreground, temp outside the repository. UNVERIFIABLE in part:
    - run_mutants.sh runs a sequential loop under `nice -n 19`;
    - the battery's temp folders are under the system temp folder (out_r4/M65.out);
    - `nice` and foreground for the battery runs are not recorded.
94. l.131, the pre-review window's terms. UNVERIFIABLE.
95. l.131–132, two runs: 179/181, then 181/181. CONFIRMED (runs/v2_1.out fails only `gread-package` "no exception" and coverage; v2_2.out).
96. l.133, the post-fix window's terms. UNVERIFIABLE.
97. l.133–134, 183/185 then 185/185 (fix in raw §6), then 66 runs. CONFIRMED (v2r2_1, v2r2_2; 66 outputs).
98. l.135, the post-pass-1 window's terms. UNVERIFIABLE.
99. l.136, one run at 185/185, then 68. CONFIRMED (v2r3_1.out ran base3 itself).
100. l.136, "held exactly that". UNVERIFIABLE.
101. l.137, the post-pass-2 window's terms. UNVERIFIABLE.
102. l.138, one run at 185/185, then 69. CONFIRMED (v2r4_1.out ran base4 itself).
103. l.138, "held exactly that". UNVERIFIABLE.
104. l.139, the run of record's window. UNVERIFIABLE (future).
105. l.141–142, the one departure, told at release. UNVERIFIABLE. Consistent with v2r2_1 and v2r2_2.
106. l.144–145, committed by path; not pushed. UNVERIFIABLE (future).
107. l.145, next: the coordinating session verifies. UNVERIFIABLE (plan).
108. l.145–146, the canonical run waits. CONFIRMED (as 90).

##### Text 2: review.md

109. l.1, PI date 2026-11-16. CONFIRMED.
110. l.3, the raw is for that entry. CONFIRMED.
111. l.5, the draft at `0b555476…843c`. CONFIRMED.
112. l.5, frozen as a copy before the review. UNVERIFIABLE (findings.md: "unchanged at the end").
113. l.6–7, against `2822721` it adds `verdicts` with §16, PIN-n-23 to 26 and the battery group. CONFIRMED (diff hunks 3263a3583,3831, 3266a3835,3936, 1660a1670,1683, 2927a3005,3245, 2942a3261, 896a904,905).
114. l.7–9, the other changes. CONFIRMED (hunks 704–707 `gread_table`, 2151 `build_state`, 2912–2925 `run_not_run`, 2422–2429 `_bt_write_campaign`, 859 171→181, 31–32 the docstring).
115. l.9, the absolute repository line. CONFIRMED (frozen l.54).
116. l.10, a subagent under a brief. UNVERIFIABLE.
117. l.11–12, the spec and schema hashes. CONFIRMED.
118. l.12–13, it read the untracked runner.py and probe.py. CONFIRMED as reported. The two paths show `??` in a status scoped to them.
119. l.13, "It ran nothing". CONFIRMED as reported.
120. l.14, F1–F6 MINOR, F7–F12 NOTEs, B1–B4. CONFIRMED.
121. l.15, V01–V38 were written against frozen. CONFIRMED (each `.old` occurs exactly once in frozen).
122. l.15–16, predictions 10/28, with V08 equivalent. CONFIRMED.
123. l.17, not run on frozen. UNVERIFIABLE (as 53).
124. l.17–18, re-expressed and run on the fixed draft. CONFIRMED.
125. l.19–20, every finding disposed of. CONFIRMED (F1–F12 and B1–B4 in §3).
126. l.21, M01–M38. CONFIRMED.
127. l.21–22, the 21 and the 7. CONFIRMED.
128. l.22–23, M67–M69 (§5). CONFIRMED.
129. l.24, the first run: base2, 185/185, 65 of 66. CONFIRMED. The 185/185 run (v2r2_2) ran the live draft before it was frozen. base2+M08, which is equivalent, also runs 185/185.
130. l.25–26, the second run: base3, 185/185, 67 of 68. CONFIRMED.
131. l.27, the third run: base4, 185/185, 68 of 69. CONFIRMED.
132. l.29, M08 survived each run; equivalent. CONFIRMED.
133. l.30, two runs before the review. CONFIRMED.
134. l.30–31, 183/185. CONFIRMED.
135. l.31, "a case of the new battery stat'ed `data/n/verdicts`". UNVERIFIABLE (the pre-fix draft is not among the sources). Consistent with base2 l.3563's comment.
136. l.31–32, the hook refused it. CONFIRMED (v2r2_1.out l.182).
137. l.32, 185/185 after the fix; one run on each later base. CONFIRMED.
138. l.33, repository line only (§7). CONFIRMED.
139. l.35, every run in a granted window. UNVERIFIABLE.
140. l.35–36, one process, `nice`, foreground, temp outside. UNVERIFIABLE in part (as 93).
141. l.36, nothing on a model or the box. UNVERIFIABLE.
142. l.36–37, an exact, unique replacement on a fresh copy. CONFIRMED (run_mutants.sh l.10–17). All 66, 68 and 69 copies equal base plus one replacement, `.old` count 1.
143. l.38, `--selftest`, and "killed" means non-zero exit. CONFIRMED (run_mutants.sh l.18–21). Every .out's INVOCATION line names its own copy. Note: the rc lines were not saved; the tables count `[FAIL]` lines, which is equivalent by main l.4395 and `battery()` l.3640–3648.
144. l.40, "(unedited in substance)". CONFIRMED.
145. l.42–43, the Write tool refused, and Code saved the hand-back. UNVERIFIABLE.
146. l.43, headings moved down one level. CONFIRMED.
147. l.43–44, the moving draft was this session's own. UNVERIFIABLE (the reviewer wrote "another session's edits"). Consistent: the runs ran that file.
148. l.44–45, findings and line numbers are frozen's. CONFIRMED (F1 2948–2957, F2 3882, F3 3701–3708, F4 3676–3687 and F5 3857–3868 all land on the cited code).
149. l.47–139, §1 = findings.md from l.7 to the end, headings one level down. CONFIRMED (93 lines, identical).
150. l.143, the reviewer's table (`mutants.tsv`, five columns), as written. CONFIRMED. The rows are identical; the header is relabelled.
151. l.143–144, not run on frozen. UNVERIFIABLE.
152. l.144, M01–M38 re-express them (§4). CONFIRMED.
153. l.146–185, the §2 table. CONFIRMED (38 rows identical to the tsv).
154. l.189–190, the §3 lead-in. CONFIRMED.
155. F1, the refusal and its message. CONFIRMED (l.2992–2994).
156. F1, VD-ONE-OUTCOME and M56. CONFIRMED (l.3394–3401).
157. F2, registered in PIN-n-24 and the docstring. CONFIRMED (l.4260–4262).
158. F2, the reading. CONFIRMED.
159. F2, the scenario (VERDICTS, N1 INDETERMINATE); the other reading; the entry flags it. CONFIRMED.
160. F3, exact cells by both shas and exact layers. CONFIRMED (l.4114–4121).
161. F3, the probe lists every cell. CONFIRMED (probe.py l.94–95).
162. F3, the tests, M13 and M14. CONFIRMED.
163. F4, `cap.used_ms`, as runner.py computes it. CONFIRMED (l.4067; runner.py l.374, l.470).
164. F4, pause kinds. CONFIRMED (l.4092–4095).
165. F4, resumptions. CONFIRMED (l.4075–4080).
166. F4, the three rules "added while the review ran, from n-build's answer". UNVERIFIABLE. Consistent: absent from frozen, present from base2 on.
167. F4, the three rules and their tests. CONFIRMED (l.4070–4074, l.4096–4100; launch-gap, two-standing, standing-not-last).
168. F4, the binomial batch; the docstring and the entry say so. CONFIRMED.
169. F4, the tests and M42–M50. CONFIRMED (M47 is the pre-existing check, as §4 says).
170. F5, the whole line is required, so a v0.1 G-VER-STOP is refused. CONFIRMED (l.4295 comes before l.4309).
171. F5, lock-version and M39. CONFIRMED.
172. F5, D_n is kept, with its reasons. CONFIRMED.
173. F6. CONFIRMED.
174. F7. CONFIRMED (l.4333–4354, l.4357, l.4220–4225; VD-COMPLETE l.3219–3226).
175. F8. CONFIRMED (l.4268, l.4312–4314).
176. F9. CONFIRMED (l.4236–4249).
177. F10. CONFIRMED (l.2925–2933, l.3549–3550).
178. F11, documented; the sha checks; M51 killed (its "identity" case refused by the sha message); per-arm implied by the identity and cells checks; M08 equivalent. CONFIRMED.
179. F11, "SchemaError at report.per_arm.<arm>". CONFIRMED (l.3496–3498).
180. F12. CONFIRMED (l.2920–2922).
181. B1, TAU/4-only exceedances. CONFIRMED (l.3162–3164).
182. B1, VD-SENSITIVITY's figures. CONFIRMED (l.3266–3280).
183. B1, the other six bullets. CONFIRMED.
184. B1, the mutant list. CONFIRMED.
185. B2. CONFIRMED (l.3020–3087, l.3181, l.3211–3218, l.3505).
186. B3, what VD-COMPLETE reads. CONFIRMED.
187. B3, VD-PLAIN new, and VD-SENSITIVITY reaching the `dir_slopes` fix. CONFIRMED.
188. B3, VD-SOME-ARMS's exposure. CONFIRMED (l.3314–3334).
189. B3, the seven new cases. CONFIRMED (none is among frozen's 20).
190. B3, the two VD-PRECHECK cases. CONFIRMED (l.3600, l.3603).
191. B3, CMD-NOTRUN. CONFIRMED (l.3860–3873).
192. B3, the mutant list. CONFIRMED.
193. B4, stop null. CONFIRMED.
194. B4, "as its answer of 2026-11-16 states it". UNVERIFIABLE.
195. B4, the used time; the first independent input; the entry flags it. CONFIRMED.
196. §4, 23 byte for byte and the 15 re-anchored ones. CONFIRMED (`cmp` against V01–V38; the 15 express the same defects).
197. §4, the 21 and the three pause rules (M44, M45, M50). CONFIRMED.
198. §4, the 7 and their labels. CONFIRMED.
199. §4, M67, M68 and M69. CONFIRMED.
200. §4, each base frozen before its runs. UNVERIFIABLE.
201. §4, the first run's base, 185/185, M01–M66. CONFIRMED.
202. §4, "in six parts". UNVERIFIABLE.
203. §4, 65 killed; M65 by an exception. CONFIRMED.
204. §4, the failing cases read from each run's detail. CONFIRMED (every named case is visible in round 2's details).
205. §4, M08 survived. CONFIRMED.
206. §4, the three equivalence cases. CONFIRMED.
207. §4, the reviewer said the same. CONFIRMED.
208. §4, after the first run: the per-arm cases and the docstring. CONFIRMED (base2→base3).
209. §4, the second run's base. CONFIRMED.
210. §4, the same spec with M67/M68 added and two labels corrected. CONFIRMED: the r2→r3 tsv and spec diffs show only those; M01–M66 files are identical.
211. §4, 67 killed, M65 by its exception, M08 survived. CONFIRMED.
212. §4, the third run's base, and the spec with only M69 added. CONFIRMED.
213. §4, 68 killed by their expected killers; M65; M69 by the new case; M08. CONFIRMED. Note: M04's detail is cut at 200 characters, so per-arm-no-arm is not visible; by the code it fails too.
214. §4, the six make the complete run refuse or STOP. CONFIRMED: VD-COMPLETE's detail lists `ran` among its failed keys. By the code, M37 STOPs and the other five refuse.
215. §4, VD-COMPLETE fails first. CONFIRMED.
216. §4, the new case raises; 173 of 185. CONFIRMED (FileNotFoundError on out_pair/N-pod_secondary.json; "check count 173").
217. §4, it cannot let a mutant pass. CONFIRMED (`B.group` l.935–939 records a FAIL).
218. §4, the last-cell rule. CONFIRMED.
219. §4, the table. CONFIRMED (my regeneration from the tsv and out_r4 is identical, 71 lines; M65's cell is 76 characters with no "…").
220. §5 l.411, "Each values-check pass reported one observation outside its claims". **IMPRECISE.** It is true of passes 1 and 2 (pass1.md l.270, pass2.md l.418). This third pass reports none of that kind, so in the assembled raw "each" overreaches.
221. §5, the first pass's finding. CONFIRMED (base2).
222. §5, the secondary would be left alone. CONFIRMED.
223. §5, in frozen every `_plain` ran before either write, and `json_text` could not stop. CONFIRMED (frozen l.3903–3926, l.2909–2910).
224. §5 l.418, "The F7 fix (the secondary written first, …)". **IMPRECISE.** Frozen already wrote the secondary first (its write loop, l.3923). What F7's fix changed was writing it before VERDICTS was formed.
225. §5, the fix's order. CONFIRMED.
226. §5, `write_all_once`. CONFIRMED.
227. §5, VD-WRITE-ONCE's direct case. CONFIRMED (l.3237–3241).
228. §5, VD-PLAIN, with no output directory created. CONFIRMED.
229. §5, M67 and M68. CONFIRMED.
230. §5 l.430, "No battery case reached `write_all_once` through `verdicts`". **IMPRECISE** (as 70).
231. §5, the three sub-bullets. CONFIRMED (base3).
232. §5, the two-call form would have survived. CONFIRMED.
233. §5, it brings back the failure. CONFIRMED.
234. §5, the fix. CONFIRMED (l.3242–3254).
235. §5, M69. CONFIRMED.
236. §5 l.440, "No production code changed." **IMPRECISE.** The fix touched only the battery, but the same base also changes a production docstring sentence (`report_problems`, base3→base4 at l.4032). No behaviour changed.
237. §6, the pre-review window's terms. UNVERIFIABLE.
238. §6, two runs at 179/181 and 181/181. CONFIRMED.
239. §6, the gread-package case changed. CONFIRMED (v2_1's only failing case).
240. §6, "which equalled the example identity's". UNVERIFIABLE. Consistent: the schema's `example_identity` and `example_gread` both use package `"2"*64`, and the fixed case picks `"5"*64` unless the identity's is that.
241. §6, the post-fix window's terms. UNVERIFIABLE.
242. §6, 183/185. CONFIRMED.
243. §6, every verdicts check passed. CONFIRMED (all 14 PASS).
244. §6, the hook check and coverage failed. CONFIRMED.
245. §6, `data/n/verdicts` recorded twice beside the probe. CONFIRMED.
246. §6, the VD-PRECHECK case it came from. UNVERIFIABLE.
247. §6, `Path.resolve()` stats each part. CONFIRMED (the venv's Python is 3.12.9; its realpath lstat's each component).
248. §6, the hook refuses any stat of those directories or anything in them. CONFIRMED (`_barred` l.1730–1741; `_Hook` l.1744–1789). It bars every unit's, not only data/n's.
249. §6, the fix passes `<repo>/data`, as not-run's case did. CONFIRMED (l.3603; 2822721 l.3181).
250. §6, 185/185, 188, exit 0. CONFIRMED.
251. §6, frozen right after, with no edit between. UNVERIFIABLE (consistent; see 129).
252. §6, beyond the window's wording; told at release. UNVERIFIABLE.
253. §6, the post-pass-1 window's terms. UNVERIFIABLE.
254. §6, one run on base3 itself, then 68. CONFIRMED.
255. §6, "held exactly". UNVERIFIABLE.
256. §6, the post-pass-2 window's terms. UNVERIFIABLE.
257. §6, one run on base4 itself, then 69. CONFIRMED.
258. §6, "held exactly". UNVERIFIABLE.
259. §7, the diff, whole. CONFIRMED.
260. §7, `<repo>`. CONFIRMED.
261. §7, one line, from `__file__`. CONFIRMED.
262. §7, the run of record on these bytes. UNVERIFIABLE (future).
263. §7, the block. CONFIRMED (byte-identical to a fresh masked `diff`).

##### Text 3: pass2_dispositions.md

264. l.3, every item accepted. CONFIRMED.
265. l.3–4, a battery change with a third mutant run. CONFIRMED.
266. l.4, pass 1's dispositions "(§2) are left as pass 2 read them". UNVERIFIABLE (there is no earlier copy). Consistent: every passage pass 2 quotes is present. The §2 pointer is CONFIRMED by assemble.sh.
267. l.4, where one was false, the correction is below. CONFIRMED (256).
268. l.8–9, 55/122/189 carried in the entry, the lead-in and §4. CONFIRMED.
269. l.10–11, the 21 ids, with the three pause rules. CONFIRMED.
270. l.12–13, the 7 ids. CONFIRMED.
271. l.14, 69. CONFIRMED (entry l.92).
272. l.15, 96. CONFIRMED (entry l.134).
273. l.16, what pass 1's disposition said; the raw named only the later two. CONFIRMED.
274. l.16–17, §6 now names the pre-review window. CONFIRMED (l.444–446).
275. l.17, "so that disposition holds as written now". **IMPRECISE.** The naming holds: both texts name every window, the one after pass 2 included. But that disposition also says "There were three windows before the commit". There are now four, plus the run of record's.
276. l.18, false when pass 2 read it. CONFIRMED.
277. l.22–27, 20/242's four additions. CONFIRMED (entry l.24, 25, 27, 30, 34–35).
278. l.28–29, 64/172/197 in the entry, §3 F11 and §4. CONFIRMED.
279. l.29–30, §4's three cases. CONFIRMED.
280. l.30–31, the docstring quote. CONFIRMED (l.4039–4040).
281. l.31, a docstring change in the third run's base. CONFIRMED.
282. l.32, 204. CONFIRMED (gen_table.pl; §4 l.334–335).
283. l.33, 222. CONFIRMED (§6 l.453–454).
284. l.37–38, note 188. CONFIRMED.
285. l.39–40, note 253. CONFIRMED (l.3549–3550; it is not one of the 43 cases).
286. l.44–46, the new VD-WRITE-ONCE case. CONFIRMED.
287. l.47, M69. CONFIRMED.
288. l.48–49, the base differences, with no production behaviour changed. CONFIRMED.
289. l.49, results in §4 and §6. CONFIRMED.
290. l.50, the commit form's sha256 `34a513f9…98b6`. CONFIRMED.

#### Totals

| Text | Claims | CONFIRMED | IMPRECISE | FAIL | UNVERIFIABLE |
|---|---|---|---|---|---|
| Entry | 108 | 87 | 2 | 0 | 19 |
| Review raw | 155 | 126 | 4 | 0 | 25 |
| Dispositions | 27 | 25 | 1 | 0 | 1 |
| **All** | **290** | **238** | **7** | **0** | **45** |

#### FAIL items

None.

#### IMPRECISE items and fixes

- **64** (entry l.80–81). Fix: "69 mutants, 68 killed, each by its expected check (M65 again by its exception, M69 by VD-WRITE-ONCE's new case); for six of them (M05, M06, M37, M41, M43, M48) VD-COMPLETE failed and the new case then raised inside the verdicts group, so 173 checks ran (the raw's §4)."
- **70 / 230** (entry l.89; raw §5 l.430). Fix: "no battery case reached `write_all_once`'s refusal through `verdicts` (VERDICTS with other bytes while the secondary was absent)".
- **220** (raw §5 l.411). Fix: "The first two values-check passes each reported one observation outside their claims (the values-check raw)". vc_head.md already says it this way.
- **224** (raw §5 l.418). Fix: "The F7 fix (the secondary written before VERDICTS was formed, so that VERDICTS could name it by sha256)".
- **236** (raw §5 l.440). Fix: "No production behaviour changed." This is the dispositions' own wording.
- **275** (dispositions l.17). Fix: "…so both texts now name every window, the one after pass 2 included; that disposition's count of three windows predates it."

#### Second-pass dispositions: carried or not

- 55/122/189: carried (entry l.69–72, raw l.21–22, §4 l.293–298); true.
- 69: carried; true.
- 96: carried; true.
- 256: carried (raw §6 l.444–446). But "holds as written now" overreaches (275).
- 20/242: carried; true. The list is now complete up to the summarised cell refusals.
- 64/172/197: carried in all three places and in the docstring; true. The equivalence holds against the schema.
- 204: carried; true.
- 222: carried; true.
- Note 188: carried; true (23 and 15 verified by `cmp`).
- Note 253: carried; true.
- The observation (the battery gap): carried (raw §5, §4's M69 row and run text, §6; entry l.80–81, 89–91, 137–138); true. The one wording issue is "reached" (70/230).

#### Observation outside the claims

None that calls for a code or battery change. Two notes:
- **Detail truncation.** The battery's detail strings are cut at 200 characters, so in rounds 3 and 4 M04's run shows schema-report, schema-gread and per-arm but not per-arm-no-arm. Its label ("every case the schema refuses") rests on the code for that case.
- **The new case ends the group early.** The VD-WRITE-ONCE pair case calls `unlink()` without `missing_ok`. Any defect that makes the complete run refuse or STOP therefore also ends the verdicts group, and 13 later checks' diagnostics are lost. This never lets a mutant pass, and the raw's §4 already says so.

## 6. Code's dispositions of the third pass

Every item is accepted, all as wording. The second pass's dispositions (§4) are left as pass 3 read them; where one
overreached, the correction is below. The edits after this pass were checked by tool: a `diff` of each text against
its copy as pass 3 read it shows these sentences changed and nothing else.

### IMPRECISE

- **64** (the entry's third run): taken as given. "68 killed, each by its expected check (M65 again by its exception,
  M69 by VD-WRITE-ONCE's new case). For six of them (M05, M06, M37, M41, M43, M48), VD-COMPLETE failed and the new
  case then raised inside the verdicts group, so 173 checks ran (the raw's §4)."
- **70 / 230** (the entry; the review raw's §5): taken as given. "no battery case reached `write_all_once`'s refusal
  through `verdicts` (VERDICTS with other bytes while the secondary was absent)".
- **220** (the review raw's §5): "The first two values-check passes each reported one observation outside their
  claims".
- **224** (the review raw's §5): "The F7 fix (the secondary written before VERDICTS was formed, so that VERDICTS could
  name it by sha256)".
- **236** (the review raw's §5): "No production behaviour changed."
- **275** (the second pass's disposition of 256): it overreached. Both texts now name every window, the one after pass
  2 included, but the count in the first pass's disposition ("There were three windows before the commit") predates
  the window after pass 2 and the run of record's. Corrected here.

### A note taken

- **78:** PIN-n-24's addition is now labelled "F2's reading, new in it from the review", so it no longer implies that
  F2's is the only addition since the frozen copy.

### Notes not acted on

- **The detail truncation** (M04's run shows schema-report, schema-gread and per-arm, but not per-arm-no-arm): M04's
  label rests on the code for that case, as pass 3 says. No change.
- **The new case ends the group early** (`unlink()` without `missing_ok`): the review raw's §4 already says that this
  can only end a mutant's run sooner. Changing the battery now would mean another mutation run with no kill to gain,
  so the battery is left as tested.

