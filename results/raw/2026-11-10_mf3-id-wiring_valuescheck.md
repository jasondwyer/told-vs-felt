# The `id` wiring (G-ID-F3): the values-check of its entry, its review raw and its self-test output

*Code's raw, PI date 2026-11-10.*
- *What was checked:* the entry draft, the review raw and the scrubbed self-test output, before the commit.
- *How:* one blind agent, read-only, under a brief quoting the list of record v2's items 1–5 as written (brief sha256
  `1d81d451…`, 61 lines). It needed nothing under `data/` and was told to open nothing there. It ran no model.
- *Outcome:* 94 items: 79 CONFIRMED, 9 IMPRECISE, 1 FAIL, 5 NOT CHECKABLE.
  - The FAIL and every IMPRECISE item are applied (below), most in the checker's own words.
  - Of its three observations, two are applied: the new blob's full sha256 is now named, and the entry gains a
    values-check section and a line on the check's site. The third is answered below.
- *Not run:* a second pass. The changes apply the checker's own fixes. Code checked each one against its source by
  tool: the anchors `:102` and `:109`, the seat's §5 item 1 quote, and the revised sentence in full.
- *Code's masked scan of the checker's transcript* (no output text printed):
  - 170 distinct Bash calls, 4 of them naming `data/`, each issued twice:
    - a `grep` of `valence_core/mf3/stages.py` for the string `data/mf3`;
    - a `grep` of RESULTS.md together with a `git grep` that carries `':!data/**'`.
  - None is in a barred metadata or content form over a `ckpt` or `reports` directory.
  - The checker's own disclosures follow its report.
- *This raw:* Code's dispositions, then the report verbatim.
  - The report was extracted by script from the agent's hand-back (the text's sha256 `9f367546…`, 198 lines).
  - The raw holds no local path and no clock time.
- *Nothing ran on a model.*

## Code's dispositions

- **72, FAIL: "The precheck reads neither file's content"** (the review raw's disposition of MINOR-3). Agreed: the
  precheck's prior gate reads the re-run's checkpoint (`stages.prior_gate`, through `rs.read_checkpoint`). Applied
  in the checker's words: "The precheck never reads the first run's file; its prior gate reads the re-run's."
- **25, IMPRECISE: m's third function is `_run_stage`.** Agreed. Applied: "(m's `stage_identity_extra`,
  `stage_precheck` and `_run_stage`; here `run_stage`)".
- **30, IMPRECISE: the anchor of the Q2 condition.** Agreed. Applied: the seat's §5 item 1 is quoted ("named in its
  entry with the DRIVER line's new blob, recorded at v0.2"), "as the `time` wiring carried the step-10 read's Q2
  condition".
- **32, IMPRECISE: the revised sentence, cut short.** Agreed. It is now quoted in full, "(the id wiring's PIN,
  below)" included.
- **34, IMPRECISE: what is re-anchored.** Agreed. Applied: "v0.2 records both on the new blob, and re-anchors R3's
  `:88` and `:95` there (now `:102` and `:109`; the review's NOTE-5 (c))".
- **41, IMPRECISE: the prior gate's reach.** Agreed. Applied in the checker's words:
  - six refusals are the gate's;
  - the first run's two are the path's;
  - and a looping link at the prior path.
- **45, IMPRECISE: "Each is now a case".** Agreed. Applied: "MINOR-1 is now two cases, and MINOR-2 and MINOR-3 one
  each".
- **48, IMPRECISE: "the carried `time` PIN texts".** Agreed. Applied: "the carried `time` PIN texts that NOTE-5 (b)
  names".
- **50, IMPRECISE: "the five … that had stopped the id block early".** Agreed: M07 stopped it too, at an uncaught
  ValueError, and was not re-run. Applied in the entry and the review raw: "the five that had stopped the id block at
  an unguarded read (NOTE-3)".
- **86, IMPRECISE: "change no check those kills rest on".** Agreed. Applied:
  - the edits add cases (the refusal table's three, the seam case, and the first-beside case, whose loader reach moves
    the final audit's count from 3 to 4), guard reads, and move the not-wired check to a test root;
  - "None removes or weakens an assertion those kills rest on. That is by reading, not by a run."
- **7 and 52, the placeholders and the acts still to come.** Filled at the commit.
- **64 and 66, the transcript scan and the extraction.** These are Code's statements. The checker was barred from
  transcripts.
- **74, the branch for 3.13 and later.** As the checker says, it is the case's coded expectation, in time's form. No
  run on 3.13 or later is on record.
- **The observations.**
  - **The new blob's full sha256:** applied.
    - The entry names it.
    - The self-test raw's first line now carries it: a header Code added after the check, above the output, which is
      unchanged.
  - **M07's failure mode:** as the checker says, `stub_run` catches only an interrupt. Any other exception from the
    stage still ends the id block before its final audit, and the run still fails. Not changed: it is the form of
    time's `stub_run`.
  - **The entry's missing sections:** a values-check section, and a line on the check's site, are added.
- **The checker's disclosures.** Neither touches the list of record v2's items. Both are departures from the brief,
  disclosed here.
  - (1) **A partial execution of HEAD's driver source**, against the brief's "no run of `scripts/mf3_sessions.py` in
    any form". By its account:
    - Python ran the module's docstring, its stdlib imports and its REPO line, then stopped at the first repository
      import;
    - nothing loaded and nothing was written;
    - a traceback printed.
  - (2) **`git show --name-only 93ecaf9`.** It printed three names under `data/mf3/ckpt` and `data/mf3/reports`, as
    names only. Item 1 permits the form. The brief's practice line asked that nothing there be listed.
- **Code's own slip, after the check.** While Code wrote the self-test raw's header, an unquoted heredoc made zsh
  try to execute `scripts/mf3_sessions.py` as a command. The shell refused it, because the file is not
  executable, so nothing ran. The header was repaired.

## The checker's report (verbatim)

**Values-check of the `id` wiring's drafts: 94 items. 79 CONFIRMED, 9 IMPRECISE, 1 FAIL, 5 NOT CHECKABLE.**

HEAD was `29fe1fa` at my start and at my end. The working tree is unchanged: 32 porcelain entries, the driver's sha256 still `8d878f4a…`, and G still holds its 20 entries. There is one accidental breach (a partial execution of HEAD's driver source) and one departure from the brief's "list nothing there" line; both are under "Disclosures" at the end.

Shorthand used below:
- **E** = `G/entry_wiring_filled.md`
- **R** = `G/review_raw_full.md`
- **S** = `G/2026-11-10_mf3-id-wiring_selftest.txt`
- **D** = the working-tree `scripts/mf3_sessions.py` (the final bytes, identical to `G/review2/candidate_mf3_sessions.py`)
- **D@HEAD** = HEAD's blob of the driver
- **C1** = `G/review/candidate_mf3_sessions.py`
- **seat** = `results/raw/2026-11-10_gtime-f3-r2_design-to-code_answers.md`

### A. The entry (E)

1. **CONFIRMED.** E:1–2: `id` is wired under LOCK-m-F3 v0.1 as re-issued, at m:295, in m's forms. PROPOSAL-m v1.11:295 is G-ID-F3, and the four id PINs each name an m form "carried" (D:128, :273, :375, :571).
2. **CONFIRMED.** E:2: "an edit of F-1's kind" is the seat's phrase (seat:45).
3. **CONFIRMED.** E:2–3: only the driver changes, `1b593ba0…87c6` → `8d878f4a…00e7`.
   - `git diff --name-only` lists the driver alone.
   - sha256(D@HEAD) = 1b593ba0…87c6, which is LOCK R1's driver row; sha256(D) = 8d878f4a…00e7.
   - `git check-attr -a` gives the driver no attributes, so no filter sits between the bytes and the blob.
4. **CONFIRMED.** E:3–4: mf3's package, m's, the analyzer and the lock are untouched, and G-SHAPE-F3 is not re-run.
5. **CONFIRMED.** E:4: 197/197 (S:209).
6. **CONFIRMED.** E:4–5: 30 mutants, no MAJOR, three MINORs (all gaps), five NOTE points applied (R:113–116; the C1→D diff).
7. **NOT CHECKABLE.** E:6: `@@STAMP@@` is a placeholder.
8. **CONFIRMED.** E:7–9: the seat file's path, its sha256 `54679f70…f01d`, and `54b1e51` as the only commit touching it.
9. **CONFIRMED.** E:9: the PI's "Route as given" on 2026-11-10 is at RESULTS.md:257 (the close line `54b1e51` added).
10. **CONFIRMED.** E:9–11: the §8 item 4 quote is byte-equal to seat:65.
11. **CONFIRMED.** E:13: `run_gid_pair_f3` is unchanged (stages.py:1241; nothing under valence_core is modified).
12. **CONFIRMED.** E:14:
    - keys `m-id|F3|{template}|{s}` (keys.py:93–96);
    - A2s and A3s (keys.py:31);
    - 2/2 decided by `gid_decide` (stages.py:1174–1199).
13. **CONFIRMED.** E:15: F-7 is `_gid_pair`'s PIN (stages.py:1208).
14. **CONFIRMED.** E:16: m:295 says a divergence sends Q-F3 uncached.
15. **CONFIRMED.** E:17–19: the identity.
    - D:327–331 adds `locked_path` for time only and validates with `_extra(…, stub=False)`.
    - stages.py:605–627 drops `locked_path` from `want` for id and refuses any cap but 120 on a model run.
    - LOCK-m-F3.md:263: "the path is recorded at LOCK-m-F3 v0.2".
16. **CONFIRMED.** E:20–21: the prior is taken by path (D:361–370; D:121, :143).
17. **CONFIRMED.** E:22–23:
    - D:366–368 refuses the resolved name when it is `FIRST_RUN_CKPT_NAME` (= `Q-F3_time.json`, D:122).
    - The quote is byte-equal to A-m2 v0.5:75 (§4.3) and to LOCK-m-F3.md:183 (R4 item 2).
18. **CONFIRMED.** E:24–25:
    - In the precheck, D:430–432 passes `require_real=True` and the identity's cap of 120.
    - In the stage, stages.py:722–727 passes `require_real=not stub`.
19. **CONFIRMED.** E:26: the artifact is at `data/mf3/gates/Q-F3_G-ID.json` (guard.py:44, :76–77), and it is write-once.
20. **CONFIRMED.** E:27–28: D:437–443 refuses an artifact that exists or is a link, unless an end is pending; there is no resume term.
21. **CONFIRMED.** E:29: the stage's B7 refusal is at stages.py:1251–1256.
22. **CONFIRMED.** E:30–31: the output names follow m's stem (stages.py:100–118).
23. **CONFIRMED.** E:32: the exit codes (stages.py:73; D:562–653).
24. **CONFIRMED.** E:34: `WIRED_CMDS` (D:100).
25. **IMPRECISE.** E:35–36 says time's three functions "become m's stage-generic forms, `stage_identity_extra`, `stage_precheck` and `run_stage`".
    - m's third function is `_run_stage` (m_sessions.py:1503); `run_stage` (D:562) is mf3's public name for it.
    - The wrapper form is m's (m_sessions.py:978–980, :1462–1464, :1763–1765; m's self-test at :4603 calls them "the step-10 wrappers").
    - **Fix:** "(m's `stage_identity_extra`, `stage_precheck` and `_run_stage`; here `run_stage`)".
26. **CONFIRMED.** E:37: `time`'s refusals, lines and exit codes are unchanged, and every time check passes as before.
    - Every changed string in the diff, evaluated for `"time"`, gives HEAD's text: the REFUSED lines, the lock refusal through `stage_name("time")` = G-TIME-F3, `STAGE_HELP["time"]`, and the `--resume` help.
    - The identity's keys are in HEAD's order.
    - The only output changes are the top-level description (D:2154) and the no-action line (D:2193); neither is time's.
    - `_selftest_time` has no hunk in the diff.
    - Against the committed 182/182 raw (run on this same HEAD blob): of 181 shared checks, 177 are byte-identical. The other 4 differ only in run-local detail and all PASS.
27. **CONFIRMED.** E:38–39: the new names (D:361, :660, :141–148, :2164–2168).
28. **CONFIRMED.** E:40–41: the F-1 reading, worded as RESULTS.md:2832–2834.
29. **CONFIRMED.** E:42: the DRIVER line prints the new blob before the load.
30. **IMPRECISE.** E:43 says "(the step-10 read's Q2 condition)".
    - The step-10 read's Q2 names four conditions, and it was written for m's driver (results/raw/2026-10-13_m-design-to-code_G-TIME-F0_read.md:45).
    - The time wiring's entry records this one for Q-F3 as "one of the step-10 read's four Q2 conditions, which Code reads F-1's 'with the same scope' as carrying" (RESULTS.md:2837–2839), and D:96–97 keeps that clause.
    - For `id`, the direct anchor is now seat:45: "named in its entry with the DRIVER line's new blob, recorded at v0.2".
    - **Fix:** cite §5 item 1, or carry the time entry's wording.
31. **CONFIRMED.** E:44: four new PIN sites (D:128, :273, :375, :571); PIN openings go from 10 at HEAD to 14.
32. **IMPRECISE.** E:44–46, the revised sentence.
    - The old sentence is verbatim (D@HEAD:85).
    - The new sentence continues "(the id wiring's PIN, below)." (D:98–99), and the quote stops before that without marking the cut.
    - Checked byte by byte: of the ten time-wiring and re-issue PIN paragraphs, this is the only one whose text changed.
    - **Fix:** quote the sentence in full, or end the quote with "…".
33. **CONFIRMED.** E:46: neither text is recorded yet. Neither is in LOCK-m-F3.md, and the time design raw lists that PIN site by subject only (results/raw/2026-11-07_mf3-time-wiring_design.md:160).
34. **IMPRECISE.** E:46–47 says "re-anchored on the new blob (the review's NOTE-5 (c))".
    - NOTE-5 (c) is about R3's two anchors: `scripts/mf3_sessions.py:88` (the TIME_* PIN) and `:95` (the re-issue PIN), both on `1b593ba0…` (LOCK-m-F3.md:141, :173). They are now at D:102 and D:109.
    - The four id PINs and the revised sentence have never been anchored, so there is nothing to re-anchor.
    - **Fix:** "v0.2 records both on the new blob; R3's `:88` and `:95` are re-anchored there (now `:102` and `:109`; the review's NOTE-5 (c))".
35. **CONFIRMED.** E:48–49: 182 → 197 on the final bytes, local roots scrubbed.
    - 182 is the committed raw's count on HEAD's blob (9d54d25 at f674583 and at HEAD).
    - S's 15 id lines match D's 15 `chk` calls one-to-one, including the seam case, the first-beside case and the 33-case table.
36. **CONFIRMED.** E:49: 15 checks (D:1562–2126; S:189–191, :195–202, :204–207).
37. **CONFIRMED.** E:50–51 (S:189–190; D:1648–1677).
38. **CONFIRMED.** E:52 (S:191).
39. **CONFIRMED.** E:53–58 (S:195–199). The no-prior case runs no `time` first, as its own words say.
40. **CONFIRMED.** E:60: 33 refusals (the code asserts it at D:2025; S:200; 33 keys counted).
41. **IMPRECISE.** E:60–61 says "the real prior gate on a prior that is … the first run's, or a looping link".
    - `prior_gate` makes six of these refusals: absent, stub-written, another proposal, not ended, ended STOP, cap 60 (stages.py:460–506).
    - The first run's two cases are refused earlier, by `id_prior_checkpoint`'s path check ("PRIOR PATH REFUSED", D:366–368), which runs as `prior_gate`'s argument (D:430).
    - On Python 3.12 the loop is refused because the path does not resolve (D:435–436).
    - So the real gate is in place in all nine cases but is reached in only six.
    - **Fix:** "Among them, with the real prior gate in place: its refusals of a prior absent, stub-written, under another proposal, not ended, ended STOP or at cap 60; the path's refusal of the first run's, by name or through a link; and a looping link at the prior path."
42. **CONFIRMED.** E:62–67 (S:201–202, :204–206).
43. **CONFIRMED.** E:68 (S:207; D:2119–2126).
44. **CONFIRMED.** E:69–71: round 1's counts. The round-1 summary.txt has five runs at 194/195 with one FAIL (M12, M14, M15, M21, M28); the other 25 are killed.
45. **IMPRECISE.** E:72–73 says "Each is now a case".
    - MINOR-1 is now two cases (D:1986–1991); MINOR-2 is one (D:2040–2062) and MINOR-3 one (D:2063–2070).
    - **Fix:** "MINOR-1 is now two cases, MINOR-2 and MINOR-3 one each".
46. **CONFIRMED.** E:74–75: the five NOTE points (D:1939–1944 and :1980–1982; :1648–1670; :1803–1809 and :1833; :33–34 and :131–132; :382–384).
47. **CONFIRMED.** E:76: the factory seam is unchanged. It is the self-test's seam in m too (m_sessions.py:1519–1521), and `main` passes no factory (D:2187–2189).
48. **IMPRECISE.** E:76 says "and the carried `time` PIN texts" are not changed, but E:44 itself reports one of them revised (D:98–99).
    - **Fix:** "the carried `time` PIN texts NOTE-5 (b) names" (C1:391, :577).
49. **CONFIRMED.** E:77–78: round 2's results (review2/runs/summary.txt and each run's FAIL lines).
50. **IMPRECISE.** E:77 and R:17 say "the five mutants that had stopped the id block early".
    - Six round-1 runs stopped the block early: M05, M06a, M09a, M16 and M17 at the unguarded read (188 checks, CHECKPOINT UNREADABLE), and M07 (185 checks, an uncaught ValueError at the first id stub run; review/runs/M07_swap_stage.txt).
    - R:72 anchors the five with "(NOTE-3)"; E:77 and R:17 do not.
    - **Fix:** "the five that had stopped the id block at an unguarded read (NOTE-3)".
51. **CONFIRMED.** E:79–80: "Nothing ran on a model".
52. **NOT CHECKABLE.** E:79–80: "Committed by path …" and "Not pushed" describe acts not yet made.
53. **CONFIRMED.** E:81: announce, then launch on the acknowledgement. This is seat:46 (§5 item 2), with precedent at RESULTS.md:316. The act itself is still to come.

### B. The review raw (R)

54. **CONFIRMED.** R:1 and R:3 (title and date).
55. **CONFIRMED.** R:4–6: sha256(C1) = 1a8270fa…8422; R:102 reports it byte-identical to the working tree; HEAD's blob is 1b593ba0…87c6.
56. **CONFIRMED.** R:7–8: the review brief's sha256 is 4b2736aa… and it has 107 lines. Its items 1–5 (brief:88–92) are byte-equal to the ruling's §2.
57. **CONFIRMED.** R:9: the sparse clone, per R:336–338 and brief:69–72. The round-1 clone is deleted; round 2's clone carries the same exclusions.
58. **CONFIRMED.** R:10: model imports blocked. All 31 round-1 runs print the harness's blocked-imports line as True, and each clone status shows the driver alone.
59. **CONFIRMED.** R:11: 30 mutants, each one change from C1 and all outside the self-test.
60. **CONFIRMED.** R:12–14.
61. **CONFIRMED.** R:15.
62. **CONFIRMED.** R:16: selftest_final.txt is 197/197; selftest_1.txt is 195/195, and its 13 id lines match C1's 13 `chk` calls one-to-one.
63. **CONFIRMED.** R:17–18: the results hold (the wording problem is item 50).
64. **NOT CHECKABLE.** R:19–24: the masked scan of the reviewer's transcript. The brief bars me from transcripts.
65. **CONFIRMED.** R:26: sha256 `5a3f5d78…` and 264 lines. I computed both over R:97–360 without the final newline; that text is byte-identical to review/report_verbatim.md.
66. **NOT CHECKABLE.** R:26: "extracted by script from the agent's hand-back". The hand-back is not openable under the brief.
67. **CONFIRMED.** R:27: no local path, user name, session id or clock time in the raw.
68. **CONFIRMED.** R:28.
69. **CONFIRMED.** R:32–34: MINOR-1 is at D:1986–1991. In round 2, M12 fails the refusal table, and the final audit counts 6 loader reaches instead of 4.
70. **CONFIRMED.** R:35–37: MINOR-2 (D:2040–2062).
71. **CONFIRMED.** R:38–41: MINOR-3.
    - The case is at D:2063–2070.
    - It plants the first run's checkpoint with `cap=60, stub_weights=True` because `resume.Identity` admits 60 only on the stub's weights (resume.py:192–199; A-m2 v0.5:73).
72. **FAIL.** R:42 says "The precheck reads neither file's content."
    - The precheck passes the re-run's checkpoint to `stages.prior_gate` (D:430).
    - `prior_gate` reads it (`ck = rs.read_checkpoint(p)`, stages.py:473) and checks its unit, stage, proposal, provenance, end and cap.
    - The case's own text says "the real prior gate reading the re-run's" (D:2067; S:204).
    - What does hold: nothing in the precheck reads the first run's file, because the path check compares the resolved name only (D:366).
    - **Fix:** "The precheck never reads the first run's file; its prior gate reads the re-run's."
73. **CONFIRMED.** R:43–44: NOTE-1's case.
    - It is at D:1939–1944 and :1980–1982, and it uses the same version split as time's loop case (D:1384–1386).
    - Round 2's M21 run shows the loop raising RuntimeError on the venv's Python, so D:435–436 prints "(RuntimeError)".
74. **NOT CHECKABLE.** R:45: the result on Python 3.13+ is the case's coded expectation. No 3.13 run is in the sources.
75. **CONFIRMED.** R:46–47: NOTE-2 (D:1648–1670). With the guard dropped, a "qual" precheck reads only committed files, the hub and the test root, and round 2's M23 final audit passes.
76. **CONFIRMED** within NOTE-3's own scope. R:48–49: D:1803–1809 and :1833; round 2's five runs all reach the final audit.
77. **CONFIRMED.** R:50–52.
78. **CONFIRMED.** R:53–54 (D:33–34, :131–132; stages.py:1179, :1208).
79. **CONFIRMED.** R:55–56: neither of the two time PIN texts has a hunk, and D:571 names the stage-generic functions.
80. **CONFIRMED.** R:57–58 (LOCK-m-F3.md:141, :173; D@HEAD:88, :95).
81. **CONFIRMED.** R:59–60 (D:382–384; stages.py:1363).
82. **CONFIRMED.** R:61–63: round 1's baseline is 194/195 and its one FAIL is the constants check.
83. **CONFIRMED.** R:64–65: both commits are RESULTS.md-only, and the driver blob is 9d54d25 at all three commits. On "from other sessions": 9699ce3's message names the pod session; 29fe1fa's names no committing session.
84. **CONFIRMED.** R:69–71: round 2's setup.
    - run_selftest.py and make_mutants.py are byte-identical between rounds; run_one.sh differs only in its work-directory line.
    - The round-2 clone is at 29fe1fa with the checkpoint and report exclusions.
    - All 30 regenerated mutants are each one change from D and are the same change as in round 1, so every anchor matched (the generator refuses otherwise).
85. **CONFIRMED.** R:72–73: round 2 ran the baseline plus 11 mutants, leaving 19 not re-run.
86. **IMPRECISE.** R:73–74 says the edits "change no check those kills rest on".
    - The edits did change checks many of the 19 kills rest on: the refusal table gained three cases (its count assertion went from 30 to 33, D:2025), and the final audit's loader count went from 3 to 4 (D:2124). The not-wired check also moved to a test root.
    - What holds, by reading rather than by a run: no case or assertion those kills rest on was removed or weakened.
    - **Fix:** "add cases (the refusal table's three; a fourth loader reach), guard reads and move the not-wired check to a test root; none removes or weakens an assertion those kills rest on".
87. **CONFIRMED.** R:75–76: the baseline is 196/197; its one FAIL is the constants check, whose detail shows mlx_lm's patterns as an empty list.
88. **CONFIRMED.** R:80–90: every row's totals match summary.txt.
    - Further FAILs: 2, 1, the raise, 2, 1, 13, 8, 12, 6, 7 and 0.
    - The five ran to the final audit.
89. **CONFIRMED.** R:92–93: in all 12 round-2 runs the import blocks held and the clone status shows the driver alone.
90. **CONFIRMED.** R:95–360: the verbatim part is intact (item 65).

### C. The scrubbed self-test (S)

91. **CONFIRMED.** S differs from `G/selftest_final.txt` in six lines (1, 130, 131, 134, 172, 173). Every changed span is a local path root, or the truncated head of one. `<repo>` appears once and `<tmp>` seven times; there is no `<home>`. Both files have 209 lines.
92. **CONFIRMED.** No absolute path, user name, session id or per-user temp-directory id survives; a 5-gram check of every path part found nothing. The three mkdtemp names after `<tmp>/` remain; the committed 182/182 raw and the time wiring's self-test raw keep theirs too.
93. **CONFIRMED.** The last line is "  197/197 mf3 selftest checks pass", newline-terminated.
94. **CONFIRMED.** 197 PASS lines and 0 FAIL.

### Everything not CONFIRMED

- **FAIL:** 72 (R:42).
- **IMPRECISE:** 25 (E:35–36), 30 (E:43), 32 (E:44–46), 34 (E:46–47), 41 (E:60–61), 45 (E:72–73), 48 (E:76), 50 (E:77 and R:17), 86 (R:73–74).
- **NOT CHECKABLE:** 7 (E:6), 52 (E:79–80), 64 (R:19–24), 66 (R:26), 74 (R:45).

### Observations (not graded)

- **No full sha256 of the new blob.** None of the three drafts carries it; all write `8d878f4a…00e7`. The time wiring's self-test raw put the full sha256 in a header. The seat's §5 item 1 asks the entry to name "the DRIVER line's new blob".
- **M07's failure mode still stops the block.** `stub_run` catches only `stages._Interrupt` (D:1711), so any other exception from the stage still ends the id block before the final audit. M07 was not re-run in round 2.
- **Missing sections.** The time wiring's entry carried a site check and a values-check section; this entry has neither yet.

### Disclosures

1. **A partial execution of HEAD's driver source (the brief bars any run of the driver).** I piped `git show HEAD:scripts/mf3_sessions.py` into `python3 -I -` and also gave that command a heredoc. zsh joined the two into one stdin, so Python executed the driver source itself.
   - It ran the module docstring, the stdlib imports and the REPO path line, then stopped at its first repository import with an import error.
   - No repository module loaded, `main` was not reached, no model was loaded and nothing was written.
   - What printed: a short Python traceback.
   - I redid the comparison with git called from inside the script.
2. **Names under data/ printed.** I ran `git show --name-only` on `93ecaf9`. It printed three file names under `data/mf3/ckpt` and `data/mf3/reports`: names only, no content, size or time. Item 1 permits that form, but the brief's practice line asks that nothing there be listed.
