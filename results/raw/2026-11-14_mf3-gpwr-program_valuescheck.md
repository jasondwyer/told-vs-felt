# G-PWR (Q-F3)'s program: its values-check

*Code's raw, PI date 2026-11-14.*
- *What was checked:* the draft of the RESULTS.md entry for G-PWR (Q-F3)'s program; `scripts/mf3_gpwr.py` (sha256
  `2b575ef8…d161`, untracked at the check); and its two raws, `results/raw/2026-11-14_mf3-gpwr-program_selftest.txt`
  (`3ef41a0d…3ebc`) and `results/raw/2026-11-14_mf3-gpwr-program_review.txt` (`bb893fd0…5f8b` at the check).
- *Against:* the seat's answers of 2026-11-14 (at `cdccc66`); PROPOSAL-m v1.11; F-5; Q7; LOCK-m-F3 v0.2; RESULTS.md
  (the G-F3 entry, the close line at `cdccc66`, G-PWR (p)'s two entries); `scripts/m_gpwr.py`, `scripts/p_gpwr.py`,
  the analyzer's `f3_power_block` and mf3's modules; the builder's independent recomputation in scratch.
- *How:* one blind agent, read-only, under a brief quoting the list of record v2's items 1–5 as written. It opened
  nothing under `data/`, and ran no model. Its one program run was the self-test, once, as its brief permitted.
- *Outcome:* 78 items: 57 CONFIRMED, 13 IMPRECISE, 0 FAIL, 8 NOT CHECKABLE. Its own self-test run gave 28/28. HEAD
  was `bd8808c` at its start and at its end.
- *Code's masked scan of the transcripts* (counts only; no command text printed), over this checker's, the
  reviewer's and the builder's tool calls (130, 223 and 182 distinct):
  - none names a ckpt or reports path under `data/`, and no metadata form names `data/`; none runs a Read, Grep or
    Glob under `data/`; none opens a transcript;
  - the builder's four calls under the tasks folder read the outputs of its own background commands.
- *This raw:* Code's dispositions, then the report verbatim.
  - Code extracted the report by script from the agent's hand-back: sha256 `e1f97f52…12f1`, 227 lines, no final
    newline. Code's leak check found no local path, user name, session id or temp-dir id, and no clock time.

## Code's dispositions

- **All thirteen IMPRECISE items are applied, as the checker's fixes have them** (items 17, 20, 24, 28, 34, 35, 37,
  43, 48, 56, 61, 64 and 74). Two of them, 61 and 64, also apply to the review raw's header, which is Code's text and
  not a verbatim section. The header is corrected and the raw rebuilt from the same sources, so its sha256 as
  committed is `4a5989e5…0f6a`. Its twelve sections were re-checked by tool: each equals its source with the two
  local roots replaced.
- **69, NOT CHECKABLE (the review raw's message and report sections, whose sources are transcripts):** checked by
  tool, as above.
- **7, 29, 73, 75, 77 (future acts), 10 (Code's read of the program) and 44 (the recomputation's file as the
  script's output):** no change.
- **The checker's disclosures:** no change needed. One `git grep` was limited to `RESULTS.md` and lacked the
  `':!data/**'` form; one recursive grep ran over three `valence_core` folders, which hold no `data` directory;
  `git blame` and content diffs ran on RESULTS.md; and two whole-tree `git status --porcelain` runs (item 1's bare
  form) were filtered by grep.

## The checker's report (verbatim)

# Values-check: G-PWR (Q-F3)'s program entry (draft), `scripts/mf3_gpwr.py` and its two raws

**HEAD at start: `bd8808c`. HEAD at end: `bd8808c`.**

Placeholders: S is Code's scratch folder for this track; V is my notes folder inside it. "d:N" is line N of the draft.

**What I checked**
- The draft, S/entry_program.md: 113 lines, sha256 `484b7cc2…` (hashed at my end; its graded phrases re-checked at their lines).
- `scripts/mf3_gpwr.py`: sha256 `2b575ef813af5079dd80ce0e16b1a14c7e3629dd0574a269135cb2cbe5bed161`, 2,160 lines.
- The self-test raw: `3ef41a0d…3ebc`.
- The review raw: `bb893fd0…5f8b`.

All three files were untracked, and unchanged at start and end. RESULTS.md was unmodified throughout.

**The permitted self-test, run once as written from the repository root:** 28 PASS, 0 FAIL, exit 0, stderr empty. Last line: `selftest: PASS (0 failed)`. Its stdout is line-identical to the self-test raw's lines 11–39.

## Items

### Header and routing (d:1–9)
1. **CONFIRMED.** The citations hold.
   - m:285 is G-PWR's line; m:298 is "G-VER, G-PWR, LOCK-m-F3 v1.0 as §3.1 …".
   - F-5 is `results/raw/2026-11-06_ganl-f3_design-to-code_answers.md:28`.
   - §A.7 is at the seat's raw @cdccc66:50 and §D item 3 at :92.
   - The routing is the close line that cdccc66 added to RESULTS.md.
2. **CONFIRMED.** The sha256 `2b575ef8…d161` is the file's.
3. **CONFIRMED.** "A sibling of scripts/m_gpwr.py that imports its functions unchanged": m_gpwr's blob is executed as the module m_gpwr (mf3_gpwr.py:100–117, 125), and its functions are used as `M.*`.
4. **CONFIRMED.** "Self-test 28/28": there are 28 `chk()` calls in `selftest()` (AST count), and my run gave 28/0.
5. **CONFIRMED.** "Three rounds, 119 mutant runs": table rows counted by tool are 51 (m\*), then 13 r\* + 33 n\* = 46, then 12 q\* + 10 c\* = 22.
6. **CONFIRMED.** "Found no wrong figure" (review raw:16, 114, 401, 620).
7. **NOT CHECKABLE.** "The record … is the run of record's, which follows this commit": a future act.
8. **CONFIRMED.** §D item 3 is quoted verbatim (seat raw@cdccc66:92).
9. **CONFIRMED.** "Route as given", relayed by the coordinating session, is in cdccc66's close line: "The PI's word, in chat, to the coordinating session's question … (its relay of 2026-11-14): "Route as given"".
10. **NOT CHECKABLE.** "A builder subagent wrote the program from Code's brief; Code read it in full": a builder brief exists in S and names `scripts/mf3_gpwr.py` as its one file, but no record shows Code's read.

### What it computes (d:10–29)
11. **CONFIRMED.** The uncached path is LOCK-m-F3 v0.2 §3 (LOCK-m-F3.md:1, :107–109). k = 29 of 40 is the seat's §A.2 (seat raw:15). See mf3_gpwr.py:138–139.
12. **CONFIRMED.** The launch per arm, the cross-check, the rows and the looks are as described.
    - Floors and balance units: m:184–186; mf3 schedule.py:42, 44.
    - The `_n90_exact` cross-check: mf3_gpwr.py:916–919, :881.
    - The rows against m:234–241, m:243 and m:330: :873–899.
    - ⌈total/40⌉: m_gpwr.py:267–268.
    - Remark: F-5 says "A1 96/32" in so many words. The program's 80 is m:184's uncached floor, by Code's reading (READINGS item 8, :266–269).
13. **CONFIRMED.** The power is the analyzer's `f3_power_block` (m_analyze.py:3402–3420): A1 at α .01 and P .70, A2 at α .01 and P .65, A3 at α .05 and P .65.
    - A1 and A2 are gated and A3 is reported (mf3_gpwr.py:147–149, 820–849).
    - Power below .85 STOPs (:837–840). m:190's raise and grid rule are not applied.
14. **CONFIRMED.** Q7's methods are as the draft says.
    - The projection runs under mf3's interleave (:750–773).
    - The floor case is at two launch counts, as at Q-F0 (:927–932; m_gpwr.py:395–400).
    - The realised case uses 189 of 240 rounds and 98 of 144 lines (:164). The G-F3 entry @2193832 has "7/189 … 2/98 … the planned 240 and 144", and so does the seat's raw at :13.
15. **CONFIRMED.** Each bar's p0, its α .05 and its domain match m:330, mf3/bars.py:205, 208, 211, 46, and mf3_gpwr.py:153–161.
16. **CONFIRMED.** The guard is figured per pair at .20.
    - Both halves bind on Qwen (m:316; mf3/bars.py:214, 219), so each pair's figure is the union.
    - The grid is figured on the projection only (:970).
    - The unit's figure is at :793–800. It is exact under Q7 (b)'s model (:247–248).
17. **IMPRECISE.** "The joint as Q7 (c) has it, carried to three bars" (d:27).
    - Q7 (c) (step-15 raw:50) makes the joint "`round_degeneracy`'s own". The program reports each bar's own (:995–999).
    - That is Code's reading (READINGS item 17, "adapted"). Its literal alternative goes to the seat (review raw:160, 327–328).
    - Fix: "the joint by Code's reading of Q7 (c) (READINGS item 17): each bar's own figure, the guards' beside; Q7 (c)'s literal, round_degeneracy's alone, goes to the seat".
18. **CONFIRMED.** The hours are at m:230's basis (:165, 975–977), with §A.5's six rows beside, verbatim (seat raw:39–44; :225–234). See item 74.
19. **CONFIRMED.** No cap is set, per §D item 4 (seat raw:93; :235–236).

### Its form (d:30–44)
20. **IMPRECISE.** "The record carries twenty readings" (d:30).
    - READINGS has 20 entries (:253–332). Items 1–6 are the seat's §A.7, F-5, and Q7's preamble, (a), (b) and (c), verbatim (:186, 254–259). Only items 7–20, fourteen, are Code's readings.
    - Placed beside Q7's "strikable", the sentence reads as twenty strikable readings.
    - G-PWR (p)'s "ten readings" (RESULTS.md:725 @bd8808c) were all Code's readings.
    - Fix: "the record's READINGS carry the seat's, F-5's and Q7's texts verbatim (items 1–6) and Code's fourteen readings (items 7–20)".
21. **CONFIRMED.** "Strikable until v1.0's commit; a strike recomputes figures only" is verbatim (step-15 raw:46).
22. **CONFIRMED.** m_gpwr is run from the load commit's blob, and valence_core (m and mf3) from that commit's blobs, through m_gpwr's finder (:100–133; m_gpwr.py:88–159).
    - No attribute of an m or mf3 module is substituted. By AST, the only attribute assignments on module objects are `mod.__file__` and `mod._GPWR_COMMIT` (:113–114). They are set on the fresh m_gpwr module before its source runs, as m_gpwr's own `_CHILD_BOOT` does (m_gpwr.py:1648).
    - The probes stand in only the program's own globals and its own `M` (:1577–1585, 1943–1951).
23. **CONFIRMED.** `m_gpwr.compute` serves A0/A0s only (m_gpwr.py:171–174, 428–508). The composition and its Q-F0 check are at :1512–1533.
    - Remark: `project_arms` is m_gpwr.project's loop rewritten over six arms (:750–773). It is asserted equal to `m_gpwr.project` at Q-F0's inputs (:1523–1525).
24. **IMPRECISE.** Departure 1 (d:38–40).
    - p_gpwr also reads LOOK_EVERY from valence_core.m.resume (p_gpwr.py:120 `bars, resume, schedule = M.bars, M.resume, M.schedule`; :426, :877). p has no resume module; its stage imports m's (valence_core/p/stage.py:152).
    - What differs: Q-F3's own stage reads LOOK_EVERY through mf3's resume (mf3/stages.py:52, 69). The program takes it from m's instead and binds mf3's two lines (:644–645).
    - Fix: "LOOK_EVERY is read from valence_core.m.resume, as p_gpwr reads its units' (p has no resume of its own), not from Q-F3's own package; mf3's two committed lines that make its LOOK_EVERY m's are required verbatim."
25. **CONFIRMED.** Importing valence_core.mf3.resume would open a file under data/ through valence_core.m.corr.
    - mf3/resume.py:34 imports m.corr. corr.py:133, `OLMO_ROSTER = olmo_roster()`, reads `data/olmo/a1_repair_roster.json` at import (:77, :118–130). I read these files; I did not import them.
    - By a static AST closure, mf3.resume adds nine modules to the program's closure. Among their import-time calls, only corr.py:133 reads a file.
26. **CONFIRMED.** Departure 2 (d:41–42).
    - p_gpwr's `_qf0_regression` reads the Q-F0 record's blob at the load commit and compares it field by field (p_gpwr.py:806–812; RESULTS.md:745–747 @bd8808c).
    - mf3_gpwr instead uses m_gpwr's own checks, whose pins include "the record's figures" `a5aaea47…` (m_gpwr.py:641–681; mf3_gpwr.py:1517–1519).
    - Neither departure moves a value.
27. **CONFIRMED.** The reviewer found the record's figures hash equal to the pin (review raw:257).
28. **IMPRECISE (minor).** "Opens nothing under data/ … writes its record there, once" (d:43). True in substance:
    - The static closure of what the program executes (25 modules plus the analyzer) has no import-time file read. The data reads in e2d/config.py:98–99 sit inside `load_audit()`, which is never called at import. The one in m/bars.py:1219 sits inside `_selftest`.
    - m_gpwr's self-test writes only in temporary directories (m_gpwr.py:838, 1013–1034, 1103–1110).
    - The reviewer's audit hook refused nothing (review raw:263).
    - But the run of record also writes through a temporary file beside the record, and reads the record back for its WROTE line (m_gpwr.py:1400–1418; mf3_gpwr.py:2154–2155).
    - Fix: "… writes its record there once (through a temporary file beside it) and reads it back for its sha256."
29. **NOT CHECKABLE.** "The readings … go with the run's entry, in Code's block": a future act. It matches practice (RESULTS.md:887 @bd8808c).

### Its inputs (d:45–56)
30. **CONFIRMED.** Each quote is built from its constant and must be verbatim at its own commit; a constant that differs refuses the run (:561–679, 2116–2118; 31 bound cases at :1861–1891).
31. **CONFIRMED.** Each pinned commit is its citation (:682–700).
    - cdccc66 resolves to cdccc664…7754, and 2193832 to 21938326…0803.
    - The seat's raw is absent from cdccc66's parent tree.
    - None of the three entry quotes is in the RESULTS.md of 2193832's parent (0190c6d); each appears once at 2193832.
32. **CONFIRMED.** The seat's answers at cdccc66 hash to `6b963adf…0db3a`, at cdccc66 and at HEAD.
33. **CONFIRMED.** The G-F3 entry's three quotes are at RESULTS.md@2193832:27, 28, 32.
34. **IMPRECISE.** PROPOSAL-m's line list (d:53).
    - The sha256 `42ab36ec…6c6b` is right.
    - But the 33 quotes also bind m:249: "Hour caps: wall-clock of detached generation time, set by the PI in that unit's LOCK v1.0" (:616).
    - By tool, the quotes sit at m:184–186, 190 (×4), 192 (×3), 230, 234–241, 243, 249, 285, 297 (×2), 298, 316 (×2) and 330 (×6).
    - Fix: add m:249.
35. **IMPRECISE.** "LOCK-m-F3 v0.2 (its path line and its launch table)" (d:54).
    - The two quotes are both in §3: the path line (LOCK-m-F3.md:109) and the launches line (:129), "The campaign's launches are the uncached table's, m:234–241 (v0.2 §4)". That line points to the table; it is not the table.
    - Fix: "its path line and its launches line (§3)".
36. **CONFIRMED.** F-5 hashes to `4edfbb8e…a42e` and Q7 to `07cd8e5f…0767`.
37. **IMPRECISE (minor).** "Its two `LOOK_EVERY` lines" (d:56).
    - The two lines are the import `from valence_core.m import resume as m_resume` (resume.py:35) and the assignment `LOOK_EVERY = m_resume.LOOK_EVERY` (:44). Only the second is a LOOK_EVERY line.
    - Fix: "its two lines that make its LOOK_EVERY m's", as d:38–39 says.

### The reviewed figures (d:57–59), against S/build/indep_recompute.py and S/build/indep_figures.json
38. **CONFIRMED.** The recomputation uses the standard library alone: json, sys, Fraction, comb and hashlib (indep_recompute.py:17–20, 357).
    - It has no exec, importlib, runpy or subprocess.
    - It imports none of the program, m_gpwr, valence_core or the analyzer, and reads no file.
39. **CONFIRMED.** Its algorithms are written apart from the program's (:8–15):
    - N90 by an ascending scan with a one-step tail recurrence (:51–64);
    - the projection by an explicit rotation (:79–96);
    - the bars by an integer pmf recurrence (:100–144);
    - the Fisher set by tails per margin total (:148–161);
    - the guard by a 2-D list DP (:164–197);
    - the power by direct enumeration (:216–240).
40. **CONFIRMED.** I rebuilt the canonical object from the JSON's exact fields, in exact_figures()' form (mf3_gpwr.py:1041–1062). It hashes to REVIEWED_EXACT_SHA256 `ab9f2fc8…9575` (:527), as does the file's own `exact_sha256`.
41. **CONFIRMED.** Every REVIEWED_* display literal equals the JSON's, field by field: the rule, power, rows, the four cases' stops, looks, bars and guards, the grids and maxima, and the hours.
42. **CONFIRMED.** 1 − Π(1 − u) over the JSON's exact unions gives 0.53901381, 0.53179360 and 0.51046676. These display as .5390, .5318 and .5105, equal to REVIEWED_GUARD_UNIT (:526).
43. **IMPRECISE (minor).** Wording at d:57–59.
    - "Gives every printed figure" includes the unit's guard figure, which the recomputation does not give.
    - "By the same rule" has no stated antecedent.
    - Fix: "gives every printed figure but the unit's guard figure, whose displays are Code's, by 1 − Π(1 − u) over that recomputation's exact unions".
44. **NOT CHECKABLE.** That the JSON is the script's output as it now stands: running the script would be a second program run, which the brief does not permit. The JSON's form matches the script's output.

### The self-test (d:60–78)
45. **CONFIRMED.** Checks 1–4 (:1657–1667).
46. **CONFIRMED.** Checks 5–7 (:1668–1675).
47. **CONFIRMED.** Checks 8–10 (:1676–1690).
48. **IMPRECISE.** "Compute's nine STOP branches" (d:67–68).
    - compute()'s docstring names ten STOPs (:903–905), and power_block_f3 adds four more of its own (:830–845).
    - Check 20 (:1588–1607, :1814–1816) provokes nine of compute's ten. By AST these are: the bars, k = 0, the launch cross-check, a launch row other than m:238's, non-integer units, the look count, the realised case's denominators, the rows' oracles, and the citation's total.
    - The power floor's STOP is check 11's (:1691–1698). power_block_f3's other three are check 21's (:1989–1995).
    - Fix: "nine of compute's ten STOP branches (the tenth, the power floor, is the power check's)".
49. **CONFIRMED.** Checks 14–17, and "39 (n1, n2) points".
    - Counted by tool from REVIEWED_CASES: 35 distinct projection points plus 4 from the floor cases' last looks. `regions_ok` requires exactly 39 (:1725–1733).
    - The probes: the record check's is check 18, evaluate()'s is inside check 21 (:1996–1999), and the regions' is check 17.
50. **CONFIRMED.** Checks 18, 19 and 21.
51. **CONFIRMED.** Check 22's QUOTE_COUNTS (18, 3, 33, 2, 1, 5, 2) equal my independent rebuild, with every quote found. The four sha256 pins are in `sources_shape_ok` (:2006–2011). There are 31 bound-constant cases (AST count). The citations check is check 24.
52. **CONFIRMED.** Checks 27, 25 and 28. Checks 13 and 23 go unnamed in the bullets; the count of 28 stands.
53. **CONFIRMED.** The self-test raw's header: HEAD `bd8808c5…448c` equals `git rev-parse bd8808c`, and its sha256 and exit 0 are right. Its body matches my run.

### The blind review (d:79–102)
54. **CONFIRMED.** One reviewer, briefed with list v2 items 1–5. Each of the five quoted items (review raw:92–96) is verbatim in the 2026-11-10 ruling. It was blind in round 1 and read Code's dispositions in rounds 2–3 (raw:4–5, 367, 593).
55. **CONFIRMED.** Round 1: 51 mutants, no wrong figure, MINOR-1 and MINOR-2 as described (raw:114–116, 127–134).
56. **IMPRECISE.** "MINOR-3, eight checks that no run made fire" (d:82).
    - The finding names eight surviving mutants and lists nine checks. The ninth, power_block_f3's cached-A1-floors STOP, was found "by reading only" (raw:118, 136–141). The disposition probes all nine (raw:310–318).
    - Fix: "MINOR-3, checks no run made fire (eight surviving mutants, and a ninth check found by reading)".
57. **CONFIRMED.** Round 1 has eleven NOTEs (raw:151–166).
58. **CONFIRMED.** NOTE 5 and what Code did about it (raw:160, 322–335).
59. **CONFIRMED.** Round 2: 46 = 13 + 33, MINOR-A and MINOR-B, and seven NOTEs (raw:9–10, 401–449).
60. **CONFIRMED.** Round 3 as described: 22 = 12 + 10, one survivor in two forms, no MAJOR or MINOR, NOTE 1 applied, no fourth round, and the self-test failing on c10 and on n32 (raw:11–15, 620–686, 709–726). Those last two runs are recorded only in the raw's own statement.
61. **IMPRECISE.** "Round 2's 11 gap survivors" (d:87).
    - The round-2 report counts ten gaps and classes n31 as "survived: equivalent at these inputs" (raw:405, 507).
    - "Eleven gap survivors" is the label of Code's round-3 brief and of the raw's header (raw:11, 602).
    - Fix, here and in the raw's header at :11: "round 2's eleven survivors its revision answered (ten gaps and n31)".
62. **CONFIRMED.** Every MAJOR and MINOR finding is applied: dispositions at raw:291–320 and 544–567; code at :189–191, 673–700, 1258–1268, 1758–1781, 1967–2003, 2014–2017.
63. **CONFIRMED.** The surviving mutants are equivalent or redundant, and the raw names each (raw:586, 714–718). c10's gap was closed by NOTE 1's change (raw:709–711, 723–726).
64. **IMPRECISE.** "The NOTEs on Code's readings are not applied" (d:92).
    - Round 1's NOTE 5, headed "The joint (READINGS item 16)", was "applied in part" (raw:322–335), as d:83–84 itself says.
    - Fix: "The NOTEs on Code's readings are not applied, but for NOTE 5's unit figure and sentence; the readings go to the seat as declared readings."
65. **CONFIRMED.** The recomputations (raw:236–258, 511–516).
66. **CONFIRMED.** The disclosures and the one departure (raw:24–27, 262–279, 361–363, 530, 698).
67. **CONFIRMED.** Four sections per round: 12 headers.
68. **CONFIRMED.** "Verbatim but for local paths": the three briefs and three dispositions are each byte-identical to their files in S/review after the header's stated substitution.
69. **NOT CHECKABLE.** The same claim for Code's three messages and the three reports: their sources are session transcripts, which my brief bars.

### Figures and Next (d:103–113)
70. **CONFIRMED.** "None is reported here": the entry carries inputs only.
71. **CONFIRMED.** The `git fsck` sentence is committed precedent, verbatim at RESULTS.md:617 (from 3e1b614) and :787 (from 4c882e7), @bd8808c.
72. **CONFIRMED.** The record is `data/mf3/gates/Q-F3_G-PWR.json`, written once (:71, 2096–2097, 2154).
73. **NOT CHECKABLE.** The second run and the verifier are future acts. Precedent: RESULTS.md:627–629 @bd8808c.
74. **IMPRECISE.** "Beside its hours line (§D item 3)" (d:111).
    - §D item 3 says "beside its m:205 line" (seat raw:92, quoted at d:6–7).
    - The program's line is at m:230's basis, by Code's reading of §A.7's "m:205's basis" (READINGS item 18, :317–322). That reading is round 1's NOTE 1, for the seat (review raw:151–156, 348–349).
    - The entry never ties the two together.
    - Fix: at d:28, "the hours at m:230's basis — Code's reading of §A.7's and §D item 3's 'm:205' (READINGS item 18; for the seat) —". At d:111, "beside its hours line (§D item 3's 'm:205 line', by that reading)".
75. **NOT CHECKABLE.** Code's block, the figures to the coordinating session, and the STOP for the cap are future acts. They match §D item 4 and RESULTS.md:791–792 @bd8808c.
76. **CONFIRMED.** "Nothing ran on a model": the program and both raws are model-free. Nothing in the record shows a box run.
77. **NOT CHECKABLE.** "Not pushed. Committed by path.": future acts.
78. **CONFIRMED.** No rule or precedent is stated without a record.
    - The fsck sentence, the write-once record, the second run, the verifier, Code's block and committing by path all have committed precedent; committing by path is in the seat's §0 C (ledger 68).
    - The cap is §D item 4's.
    - KNOWN_LOCKS' premise (a lock is re-issued in place, never removed; :220) is Code's, and the entry does not state it.

## Tally
78 items: **57 CONFIRMED, 13 IMPRECISE, 0 FAIL, 8 NOT CHECKABLE.**

**Not CONFIRMED:**
- **IMPRECISE (13):**
  - 17: the joint "as Q7 (c) has it".
  - 20: "twenty readings".
  - 24: departure 1; p_gpwr also reads m's resume.
  - 28: data/; the run reads its record back.
  - 34: m:249 missing from the list.
  - 35: "launch table".
  - 37: "two LOOK_EVERY lines".
  - 43: "every printed figure" and "the same rule".
  - 48: "compute's nine STOP branches".
  - 56: MINOR-3 "eight checks".
  - 61: "11 gap survivors".
  - 64: NOTE 5 was applied in part.
  - 74: m:205 against m:230.
- **NOT CHECKABLE (8):** 7, 10, 29, 44, 69, 73, 75, 77.

**Suggested VALUESCHECK fill:** "a blind check of the draft, the script and both raws before the commit: 78 claims, 57 CONFIRMED, 13 IMPRECISE, 0 FAIL, 8 NOT CHECKABLE (future acts, process claims, the sources of the reports and messages, the recomputation's run). Its own self-test run gave 28/28."

## Disclosures
- **The one permitted run** used exactly the given command, run in the background, with stdout and stderr redirected to files in V and the exit status echoed there. m_gpwr's child self-test, by design, creates and removes system temporary directories.
- **One `git grep`** ("Code's block") was limited to the pathspec `RESULTS.md` and lacked `':!data/**'`. That departs in form from the brief's rule that every content search carries the tested form. It could reach nothing under data/.
- **One recursive `/usr/bin/grep`** (LOOK_EVERY) ran over valence_core/{p,mf3,m} with `--include='*.py'` and no data exclusion. A pruned `find` shows those folders hold no data directory.
- **Forms outside item 1's list**, all on files outside data/:
  - `git blame --porcelain` on two RESULTS.md lines, printing only the commit id;
  - `git diff <c>^ <c> -- RESULTS.md` content hunks at cdccc66 and 2193832;
  - two whole-tree `git status --porcelain` runs, filtered by grep, which printed nothing beyond the three target files.
- **Reads beyond the listed sources:** S/review's six brief and disposition files, and the opening of S/brief_build.md.
- **My scripts:** stdlib-only `python3 -I` scripts in V parsed repository .py files with `ast` and read texts through `git show`. None imported repository code. A copy of the seat's raw at cdccc66 is saved in V.
- **Nothing else:** nothing under data/ was opened, listed, sized or traversed; no size or time of any file; no `--stat`-type form; nothing in tasks/ or any transcript; no git writes; no writes outside V. Nothing broke a rule beyond what is listed above.