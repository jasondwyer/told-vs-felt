# n — the supplement to the eleven starred readings: the blind values-check, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the supplement's draft, T1, sha256 `def58aea…8a80` (104
lines).

**The checker's brief** (`5eddce01…295c`, 78 lines, given to the checker as a file, with its sha256 to verify):
- named the text and the sources: in the repository at `99196e1`, the files the text cites; in Code's scratch, by name
  and sha256 only, G-CAL-n's review report on draft 1, the coordinating session's routing of GC23 as received, and
  G-CAL-n's drafts 3 (the build as it will be committed) and 1;
- asked for every factual claim to be checked: each number, hash, citation and quotation; what the build does or did;
  what the review found and the routing said; and what G-VEC stores. Code's reasoning about other answers was to be
  checked where it says what code does;
- allowed `shasum` by name (on this machine a Perl script, which the list of record's item 1 permits), and barred any
  other interpreter, any write, any network, any guard marker in an argv (a grep pattern included), anything under
  `data/mf3`, any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the named
  files and the brief itself;
- quoted the list of record v2's items 1–5, verbatim; required item 3's pathspec and the `data/mf3` exclusion on every
  git command over the tree, with `.` as the include for `git ls-files`, that a glob is expanded and read before it is
  looped over, and the `rev-parse` form for a tracked-and-clean check.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (202 lines, sha256
`4e858b10…f8e4`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 64 items: 53 CONFIRMED, 9 IMPRECISE, 0 FAIL, 2 NOT CHECKABLE; and 12 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

- **The IMPRECISE items** (18, 23, 24, 30, 39, 40, 42, 51 and 60), each applied in the checker's words or near them.
- **The NOT CHECKABLE items** stand: 10 is a plan; 7's word "checked" is gone by observation 10.
- **The observations:**
  1. Applied: the review's own form of (c), a None and a STOP, is named in §1's other answers and in Q12.
  2. Applied: the hard-stop path is named in (b) and in §1's last answer. The launch files are to bring back whichever
     folder the run left, and a re-run needs that folder moved aside on the box first, on the seat's word.
  3. Applied in the supplement: a flip ruled after G-CAL-n's BUILD commit is a code change, a self-test run in its own
     window and a commit, and it moves the package's digest. The build's docstring and its comment on the line stand:
     the line is the order's one place, and the self-test pins it.
  4. Applied: the record's four-batch order is called the build's order of record, n:113's three then the baseline,
     the baseline's place being the build's reading.
  5. Applied: O8 says that ganl's input check takes exactly the five keys, so a status field would make ganl refuse
     the map.
  6. Applied: the paired t runs over the prompts scored on both sides.
  7. Applied: the sources name ADDENDUM-n1 and the review, and §5 quotes the coordinating session's routing of GC23
     verbatim, with its next message's line on draft 3.
  8. Applied: the header gives draft 3's two sha256s.
  9. Applied: m's checkpoint is cited beside p's.
  10. Applied: G-VEC's launch files are "drafted in Code's scratch and held".
  11. Applied: rule 25 is cited C:348–349.
  12. Applied: the kept turns carry no arrival score, and a later score is a re-computation that adds no generation
      (E:229–230).

## 2. The text changed after the check, and the edits checked by tool

- **The text changed after the check** by the dispositions above, and by §5, which quotes the routing verbatim.
- **The edits, checked by tool:** a fixed-string search over the unwrapped final text, each edit's new wording present
  and the wording it replaced absent, 40 of 40; §5's two quotations byte-equal to the messages as Code received them,
  by `cmp`.
- **The final:** the supplement `c94410ce…e3ba`.

## 3. The report as returned

```text
VALUES-CHECK OF T1 (S/step4b/seat12/supp_src.md)

Preliminaries. The brief matched its sha256 (5eddce01…295c). T1 matched def58aea…8a80 and has 104 lines (wc -l). Every named S file matched its stated sha256: the review 75d4200f…cd5e, the routing b7bcdc6b…48aa, draft 3 gcal.py aba3700c…a3a0 and n_sessions.py 37b8268d…f030, draft 1 gcal.py be63ef41…1f5e and n_sessions.py 5258bcfc…6a02. HEAD is 99196e1. Each cited repository file is tracked and clean (git rev-parse HEAD:<path> equals git hash-object <path>): E, S, PROPOSAL-n-bk-reconciliation-v0_2.md, CLAUDE.md, ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md, valence_core/p/gcal.py, valence_core/m/gcal.py, valence_core/n/gvec.py, valence_core/n/directions.py, scripts/n_analyze.py, scripts/n_sessions.py, .gitignore. Below, "gcal.py" and "n_sessions.py" without a prefix mean draft 3 (S/step4b/gcal/draft3/); draft 1 is written S/step4b/gcal/draft/….

ITEMS

1. L1. The supplement holds GC23, three notes (O3, O5, O6) on Q1 and Q11, and three list items (O7, O8, O12). CONFIRMED. Routing:5–8; T1 §2–§3.

2. L3. "PI date 2026-11-19". CONFIRMED. This is the session's date, and the same date as E:3 and RESULTS.md:24 (99196e1's entry).

3. L3. "For the PI to route, in the same sitting as the eleven (99196e1)". CONFIRMED. Routing:5 ("a short supplement to 99196e1 for the same sitting") and routing:9.

4. L5. "No lock is in force." CONFIRMED. RESULTS.md:31. `git ls-files -- . <item-3 exclusions> ':!data/mf3/**'` filtered for LOCK-n returns nothing.

5. L6–8. E and S are committed at 99196e1, beside each other. CONFIRMED. `git show --name-only 99196e1` lists RESULTS.md, results/raw/2026-11-19_n-gcal_spec.md, results/raw/2026-11-19_n-starred-eleven_code-to-design_STOP.md and the values-check raw.

6. L9. "G-VEC is built at da7bdec and has not run." CONFIRMED. da7bdec's subject is "n -- G-VEC's BUILD…". RESULTS.md:29 says "G-VEC has not run". The ls-files filter `^data/n/gvec/` counts 0.

7. L9–10. "Its launch files are checked and held until the PI answers on its run order." NOT CHECKABLE. E:7 says "drafted in Code's scratch", and no named source records a check. "Until the PI answers" agrees with E:12–13.

8. L11. "draft 1 had one blind review, which found no BUG". CONFIRMED. Review:1–5 ("I found no BUG-class defect"); its files are S/step4b/gcal/draft/ (review:3).

9. L11. The report's sha256 is 75d4200f…cd5e. CONFIRMED (shasum; the tails taken by cut).

10. L11–12. "goes into the repository with G-CAL-n's BUILD". NOT CHECKABLE (a plan).

11. L12. "Its findings are applied in Code's later drafts." CONFIRMED for F1–F12 against draft 3:
   - F2 gcal.py:554–568; F3 :602–612; F4 :669–695; F5 :15–23, 134–138, 704–707; F6 :74–83; F7 :118–120, 182–184 and n_sessions.py:2755–2758;
   - F8 n_sessions.py:2674–2675, 2680; F9 :2884–2918, 2939–2948; F10 gcal.py:288–306; F11 n_sessions.py:2636–2643, 2760–2763; F12 :3385–3386;
   - F1 is applied as GC23. Its third fix (record a non-finite arrival as None plus a STOP, review:18) is not taken: GC23 (c) keeps the raise (observation 1).

12. L12–13. F1 became GC23. CONFIRMED. Routing:1.

13. L13–14. GC23 was routed as a PIN declared in the BUILD entry, to go to the seat before the run. CONFIRMED. Routing:2 and :5.

14. L14. "G-CAL-n's build is in Code's scratch, not committed." CONFIRMED. `git rev-parse HEAD:valence_core/n/gcal.py` fails ("does not exist in 'HEAD'"); the ls-files filter for gcal paths counts 0.

15. L16. PROPOSAL-n v0.2 is PROPOSAL-n-bk-reconciliation-v0_2.md. CONFIRMED by that file's line 2. The Sources list leaves things out (observation 7).

16. L23–24. "A failed run keeps the turns it generated, and the batches are generated −ρ last." CONFIRMED. gcal.py:126, 349, 365–366, 405–412; n_sessions.py:2804–2819.

17. L24. (d) is "the one part that touches n:113's words". CONFIRMED. Routing:4.

18. L24–25. "It is one line, which a ruling flips back." IMPRECISE.
   - The line is gcal.py:126, but the self-test pins the order as a literal (gcal.py:635–637: `GENERATION_ORDER == ("+rho", "+rho/2", "baseline", "-rho")`). A flip of that line alone fails the self-test.
   - Instead: "It is one line, which a ruling flips back, with the self-test's pin of the order changed to match."

19. L26–27. The notes are what striking G1's centring costs G-CAL-n, plus two properties of the arrival form. CONFIRMED. Review:186, 194, 196.

20. L29. The dependencies are E §3's with Q12 added: "all twelve answers". CONFIRMED. E:48, E:242–243.

21. L33. "the review's F1, RISK, on draft 1". CONFIRMED. Review:9.

22. L34. "held all 192 turns in memory until its end". CONFIRMED. Review:11. In S/step4b/gcal/draft/gcal.py:252–293, the turns stay in a dict until compute returns; S/step4b/gcal/draft/n_sessions.py:2788–2796 writes only after that.

23. L35–36. "Any failure after the load removed the staging folder: a CUDA or memory error, the non-finite-arrival raise, an error in writing, or an interrupt." IMPRECISE.
   - In draft 1 the staging folder is made at n_sessions.py:2788, after the load (2772) and its provenance, shape and eos checks. `except BaseException: shutil.rmtree` is at 2794–2795.
   - The review (review:12) adds that a pod kill leaves an empty staging folder.
   - Instead: "Any failure raised once the staging folder was made, after the load and its checks, removed it: a CUDA or memory error, the non-finite-arrival raise, an error in writing, or an interrupt. A pod kill left it in place, empty."

24. L37–38. "would be lost to the seat's read (rule 25, C:348) and to §0.4's count (n:20: "48 turns at −ρ (≤ 80 tokens each)")". IMPRECISE.
   - The quote is verbatim at n:20, and C:348 opens rule 25.
   - The count was not lost. Review:13 says "the realised exposure then exists only as stdout's per-turn lines", and draft 1 printed each turn's batch, index, label and n_tok as it was generated (S/step4b/gcal/draft/gcal.py:272).
   - Instead: "…would be lost to the seat's read (rule 25, C:348), and §0.4's count of them (n:20: "48 turns at −ρ (≤ 80 tokens each)") would rest on stdout's per-turn lines alone."

25. L39. A re-run is allowed only on the seat's word (S:59) and "would add up to 48 more". CONFIRMED. S:59; review:13.

26. L40. "m's and p's G-CAL wrote a checkpoint after every generation (valence_core/p/gcal.py:509–538)". CONFIRMED. p's loop at :509–538 calls `_write(pa["ckpt"], ck)` at :537 (atomic, :346–351). m's does the same at valence_core/m/gcal.py:1152–1174 (observation 9).

27. L42–43. "one shot under GC19: a new out folder, no resume, a re-run only on the seat's word". CONFIRMED. S:59; n_sessions.py:2715–2716, 2721–2724.

28. L44–45. (a): each turn is appended to `gcal_turns.partial.jsonl` as it is generated, as one JSON line, flushed and fsynced before the next turn. CONFIRMED. gcal.py:122, 365–366, 405–412; n_sessions.py:2804–2808.

29. L45–46. The log is removed only on a clean end, once the record, turns and dose map are written. CONFIRMED. n_sessions.py:2809–2811; gcal.py:415–436.

30. L47–48. (b): "On any failure after the staging folder is made, the folder is renamed to the failed-run folder and never removed." IMPRECISE.
   - The rename runs only in `except BaseException` (n_sessions.py:2812–2819). If os.replace fails, the folder stays at the staging path.
   - A hard stop that skips the handler (a pod kill) leaves data/n/.gcal.staging in place with its log, and the next run refuses on it (2717–2720).
   - Instead: "(b) On any failure raised after the staging folder is made, the folder is renamed to the failed-run folder and never removed. On a run of record that is data/n/.gcal.failed, which git ignores. A hard stop that skips the handler, such as a pod kill, leaves the staging folder in place with its log. A later run refuses, before the load, while either folder exists."

31. L48. "On a run of record that is data/n/.gcal.failed, which git ignores." CONFIRMED.
   - n_sessions.py:2563, 2714 and 2721 give out_p.parent / ".gcal.failed".
   - HEAD's .gitignore:263 (`/data/n/*`, with :260–261's "any later n artifact … needs its own line") ignores it. The build's own ignore lines were not among my named files; the review's O2 says they mirror G-VEC's block (.gitignore:307–314), which admits named files only.

32. L48–49. "A later run refuses, before the load, while that folder exists." CONFIRMED. n_sessions.py:2721–2724, before the load at 2787.

33. L50. (c): a non-finite arrival is a raise after every turn is generated, and (b) keeps all its turns. CONFIRMED. gcal.py:277–278 raises; generation runs at :349–369, before arrival at :370–372. The self-test at n_sessions.py:3172–3182 finds 192 turns in the log.

34. L51–52. (d): the order +ρ, +ρ/2, the baseline, then −ρ, so that a failure in another batch spends no −ρ turn. CONFIRMED. gcal.py:126, 349.

35. L52–53. "The record and the turns file keep n:113's order", with the quote. CONFIRMED. The quote is verbatim at n:113. gcal.py:108, 373, 400–402 and 427 keep the order (the record's "batches" list); the self-test at :572–575 checks it. See observation 4.

36. L53. "Each turn's seed fixes its draws, so the order changes no turn's inputs." CONFIRMED. gcal.py:196 makes a fresh `default_rng(seed)` per turn; :164 and :357 give each turn its seed.

37. L55–56. (d)'s text as built is one line in valence_core/n/gcal.py, `GENERATION_ORDER = ("+rho", "+rho/2", "baseline", "-rho")`. CONFIRMED verbatim at gcal.py:126.

38. L56. "The record carries it as constants.generation_order." CONFIRMED. gcal.py:433.

39. L59–60. "Striking (a)–(c) restores draft 1's form: a failure leaves nothing, and any −ρ turns it had generated are lost to the read and to the count." IMPRECISE, for the same reasons as items 23–24 (draft 1's rmtree; a pod kill's empty folder; stdout's per-turn lines).
   - Instead: "Striking (a)–(c) restores draft 1's form: a failure leaves no turn on disk, and any −ρ turns it had generated are lost to the read, their count left to stdout's per-turn lines."

40. L61–62. "Flipping (d) sets that one line to n:113's order, ("+rho", "-rho", "+rho/2", "baseline"), and changes nothing else." IMPRECISE.
   - The tuple is right: it is the comment at gcal.py:124–125 and draft 1's BATCHES order (S/step4b/gcal/draft/gcal.py:78).
   - "Nothing else" is not: the self-test pin (gcal.py:635–637) fails, the docstring (:37–40) states the order, and the record's constants.generation_order follows the line.
   - Instead: "Flipping (d) sets that one line to n:113's order, ("+rho", "-rho", "+rho/2", "baseline"), and the self-test's pin of the order and the docstring's sentence with it; the record's constants.generation_order follows the line. Nothing else changes."

41. L62. "A failure in +ρ/2 or in the baseline would then come after the 48 −ρ turns were spent." CONFIRMED (the order +ρ, −ρ, +ρ/2, baseline).

42. L63–64. "After a failure, under any answer: G-CAL-n's launch files bring the failed-run folder back by hash, its turns are read and counted…, and the seat rules on a re-run (GC19)." IMPRECISE.
   - Under the answer that strikes (a)–(c) there is no failed-run folder (item 39).
   - The launch files are not drafted; routing:10 sends only B3, B4 and O13 to them, later.
   - Instead: "After a failure, with (a)–(c) standing and under either answer on (d): G-CAL-n's launch files, not yet drafted, are to bring the failed-run folder back by hash; its turns are then read and counted against §0.4's exposure, and the seat rules on a re-run (GC19)."

43. L64–65. "How those turns are kept in the repository is not built; it is the seat's." CONFIRMED. Draft 3 has no path that admits or commits the folder, and HEAD's .gitignore:263 ignores it.

44. L69–70. G-VEC stores the uncentred valence direction as the `valence_uncentred` row of `directions_alt_L{i}.npy` (gvec.py:92, 352). CONFIRMED. valence_core/n/gvec.py:92 (ALT) and :352; it is written on a PASS at :106–107 and :421–429.

45. L70–71. If the centring is struck, the direction of record and its sha16 move to that row (E:70–73). CONFIRMED. E:70–71.

46. L72–73. `gcal_gvec_inputs` reads only row 0 of `directions_L{site}.npy` and checks it against of_record's sha16. CONFIRMED. n_sessions.py:2647–2655 (`read_rows(dp)[NAMED.index("valence")]`, where NAMED[0] is valence at gvec.py:91).

47. L74. "G-CAL-n would refuse, safely, until that reader is changed and re-tested." CONFIRMED. The refusal is SystemExit at n_sessions.py:2654–2655, called at 2759, before the load at 2787. Review:186 says "refuse, safely, until changed".

48. L75. "E's G1 paragraph does not name this reader." CONFIRMED. E:54–77; grep -c 'gcal_gvec_inputs' over the whole of E is 0.

49. L76–77. Prompt i's turns share seed_i and so their uniforms (common random numbers). CONFIRMED. gcal.py:164, 357, 174, 196; review:194.

50. L78–79. Where the paired scores correlate positively, Welch's unpaired t overstates the SE, so |t| ≥ 2 is stricter than nominal. CONFIRMED. Review:194 says "conservative", and T1's conditional form is no stronger. Welch's t is unpaired at gcal.py:255–264.

51. L80–81. "A paired t over the 48 prompts is the alternative. batch_figures would then keep each score's prompt, which it now drops." IMPRECISE.
   - The content is right: gcal.py:298 and :375 keep the scores without their index.
   - The point is the review's O3 (its GC12 bullet, review:182), not O5, which T1 files it under.
   - Instead: "A paired t over the 48 prompts is the alternative (the review's O3, on GC12). batch_figures would then keep each score's prompt, which it now drops."

52. L82–83. The arrival score is the mean over every position of an unsteered forward over the emitted ids alone. CONFIRMED. gcal.py:267–279; n_sessions.py:2056–2060 (`_hf_forward`, no injections) and 2617.

53. L84–85. Position 0, "typically the high-norm attention-sink position", is in every mean with weight 1/n_tok and weighs most in short turns. CONFIRMED. This is the review's O6 at the same strength (review:196); gcal.py:274–276.

54. L86. G-VEC counts every token the same way (G1: "every token counts in the passage mean and in R"). CONFIRMED. The quote is verbatim at E:57; gvec.py:139–146; directions.py:47–52.

55. L90. "The baseline's coherent count is recorded and binds nothing." CONFIRMED. gcal.py:376–377 and :428 record it; stage_status at :310–316 reads only ±ρ and +ρ/2.

56. L90–91. Rule 21's annotation (C:338–341) is already on the list (E §3, against GC2). CONFIRMED. C:338–341; E:252–253.

57. L91–92. The baseline is the unprovoked domain, and below 36 coherent would point at the prompt, the rendering or TEMP. CONFIRMED. This is the review's O7 at the same strength (review:198); COHERENT_MIN is 36 at gcal.py:113.

58. L93. dose_map.json carries no status and is written on a STOP or a PAUSE too. CONFIRMED. gcal.py:423–425 writes only the five keys; n_sessions.py:2809 writes before the status branches at 2824–2830.

59. L93–94. `ganl --dose-map` accepts any map whose formulas hold (scripts/n_analyze.py:5500–5511). CONFIRMED. :5500–5511 runs the read, `dose_map_input_problems` and `DoseMap.problems`, with no status check.

60. L94–95. "The lock takes the map only where gcal.json says pinnable, which is a PASS." IMPRECISE.
   - pinnable is a PASS (gcal.py:428). But the review says "should" (review:200), and no lock is drafted, so the indicative states a rule nobody has set.
   - Instead: "The lock should take the map only where gcal.json says pinnable, which is a PASS."

61. L96. gcal-decode is "the laptop's one decode comparison (A-n1 §1.4)" and prints each differing turn's two decodes. CONFIRMED. A-n1:26; n_sessions.py:2921–2923, 2945–2948.

62. L96–97. "Its raw therefore carries turn text before the analyzer's output exists." CONFIRMED. Review:208; n:159 puts G-CAL-n at step 8, before G-ANL-n at step 9.

63. L97–98. "When the seat reads the turns (GC1, S:37, on the list; n:130)". CONFIRMED. S:37; n:130; E:250–251.

64. L102–104. Q12 restates (a)–(c) and (d) consistently with §1. CONFIRMED.

TOTALS: 64 items. CONFIRMED 53, IMPRECISE 9 (items 18, 23, 24, 30, 39, 40, 42, 51, 60), FAIL 0, NOT CHECKABLE 2 (items 7, 10).

OBSERVATIONS

1. Q12 and "What another answer would change" do not name the review's own form of (c): F1's fix, "Record a non-finite arrival as None plus a STOP instead of raising" (review:18).
   - As built, a non-finite arrival writes no gcal.json, no status and no dose map. The seat gets only the failed-run folder, whose log holds all 192 turns with arrival None (gcal.py:363–366; n_sessions.py:3172–3182).
   - Under the review's form, the record would be written and read as a STOP. The seat may want that answer offered.

2. The hard-stop path is unnamed.
   - A pod kill leaves data/n/.gcal.staging, not .gcal.failed, so the launch files would have to bring back whichever folder exists.
   - The driver never removes either folder and refuses while either exists (n_sessions.py:2717–2724). A re-run on the seat's word therefore also needs that folder moved aside on the box, and T1 does not say who does that.

3. The build's own docstring (gcal.py:39–40, "a ruling against (d) changes that one line") and its comment (:124–125) carry the imprecision of items 18 and 40. A flip ruled after the BUILD commit is a code change, a self-test run and a commit, and it moves the n package's digest, which the launch files hash.

4. n:113 orders only "+ρ, −ρ and +ρ/2" and names the baseline afterwards, in its arrival clause. Putting the baseline last in BATCHES (gcal.py:108; read the same way in the docstring at :36–37) is the build's reading. T1:52–53 and T1:61 call the four-batch tuple "n:113's order" without saying so.

5. On O8: ganl's input check takes exactly the five keys (scripts/n_analyze.py:5453–5463, `set(m) == set(DOSE_MAP_KEYS)`). A status field in dose_map.json would make ganl refuse the map, so the gate has to sit where the lock takes the map (pinnable). Saying so would head off "add a status" as the fix.

6. Under a paired t, a turn with no arrival score (departure (2), gcal.py:76, 271–272) drops its pair. So "over the 48 prompts" means over the prompts scored on both sides.

7. The Sources list (T1:16–17) omits ADDENDUM-n1 (cited at T1:96), the review and the routing. GC23's routing is in no repository file: S §2 holds GC1–GC22's routing verbatim, but nothing holds GC23's. The seat cannot check T1:13–14 against the repository unless it is quoted verbatim.

8. Routing:9 lets this supplement land before G-CAL-n's BUILD, so the "as built" files and the review may be absent when the seat reads T1. Giving the build's sha256s would let the seat tie T1's claims to the BUILD commit: S/step4b/gcal/draft3/gcal.py aba3700c…a3a0 and S/step4b/gcal/draft3/n_sessions.py 37b8268d…f030 (tails by cut).

9. T1:40 cites p's code for "m's and p's". m's equivalent is valence_core/m/gcal.py:1152–1174 (`atomic_write_json` after each record).

10. On T1:9–10's "checked": E:7 says "drafted", and 99196e1's subject names G-VEC's launch files as next. If a check has run since, cite it; otherwise write "drafted".

11. C:348 is the first line of rule 25, which runs C:348–349.

12. The kept log's rows carry arrival None (n_sessions.py:3167–3171). After a failure, any scores are a re-computation from the recorded ids, which E:229–230 says adds no generation.

DEPARTURES
- Two `git show --name-only --format='%h %s'` runs, on 99196e1 and on da7bdec, were made without item 3's pathspec and the mf3 exclusion. They printed only subjects and names, none under data/: RESULTS.md, results/raw/ files, .gitignore, scripts/n_sessions.py and four valence_core/n/ files.
- Otherwise none:
  - shasum was the only interpreter-class program, and no argv held a guard marker.
  - Nothing under data/mf3, a ckpt folder or a reports folder was read, listed, sized or timed, and no git status was run.
  - The other tree-wide git command (git ls-files) carried the pathspec and the mf3 exclusion. `git rev-parse HEAD` and `git log -1 --format='%H %s'` list no path.
  - In S, only the brief and the named files were read: by shasum, wc -l, tail and od on T1, sed and grep on the named drafts, and the file-reading tool. Nothing was listed or globbed.
  - No file was written, and nothing used the network.
```
