# n — the schema follow-up's texts: the blind values-check, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was checked.** One blind pass by a subagent over three drafts:
- T1, the entry (`RESULTS.md`, the Log's head), sha256 `200ced08…84ce`;
- T2, the self-test raw, `6b5bf586…5991`;
- T3, the review raw's head and dispositions, `d57165c0…cf28`.

**The checker's brief** (`6432aa4e…96d6`, 142 lines, given to the checker as a file, with its sha256 to verify):
- named the change's files (HEAD's four, the final drafts, the reviewed drafts and the first draft's runner) and the
  `git diff --no-index` form;
- named the sources:
  - in the repository: ADDENDUM-n2, the seat's answers of the fourth sitting, the PI's routing raw, backend-ext-2's
    box self-test and hashes raws, v2f's and v2g's self-test raws, `RESULTS.md`, HEAD's package and
    `valence_core/m/resume.py`, HEAD's `scripts/n_analyze.py`, `.gitignore`, and git history;
  - in Code's scratch, by name only: the drafts, the three runs' outputs and exit files, the review's report and
    brief, and the shell form of the package digest, which it could run on the repository's package and on the
    self-test overlay's;
  - the coordinating session's words and n-analyzer's, which are in no file, quoted verbatim;
- quoted the list of record v2's items 1–5, verbatim; required item 3's pathspec and the `data/mf3` exclusion on every
  git command over the tree, that a glob is expanded and read before it is looped over, and the `rev-parse` form for a
  tracked-and-clean check;
- barred any interpreter, any write, any network and any guard marker in an argv; anything under `data/mf3`; any
  content read, listing, size or time of a ckpt or reports file; and, in Code's scratch, anything but the named files.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (352 lines, sha256
`b29c85c1…516a`). It names no local path.

**Totals:** 115 items: 87 CONFIRMED, 11 IMPRECISE, 1 FAIL, 16 NOT CHECKABLE; and 14 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

- **The FAIL, item 21** (T1, "in `schema.py`, four refuse cases"): corrected to three. The checker accounted for all
  25 lines the change removes from HEAD's `schema.py`.
- **The IMPRECISE items:**
  - items 8 and 84 (the box's 420): applied, in the checker's words: the box's 11 checks more, its 13 HF checks in
    place of the laptop's two skip lines. Code checked the counts: `hftiny.py`'s one skip line and twelve box checks,
    and the driver's HF-path vanilla score with its skip line;
  - item 17 ("second in the precedence after `nonfinite`"): applied, "directly after `nonfinite` in the precedence";
  - items 23 and 75 ("granted for its four files"): stand. Run 2's window, in full, named all four files: after its
    first line it says "My check: the overlay's 159 files, of which exactly four differ from 732a58f, with none
    absent:" and lists each file's full sha256 and numstat. The brief quoted only the window's first line;
  - item 34 (`runner.py:326`, "at a resume"): applied, in the checker's words;
  - item 41 (the paths still to run): applied, with observation 3;
  - item 51 (R13, "as a trial and an exceedance"): applied in the entry. `runner.py`'s docstring keeps "a trial, and
    an exceedance" until the file's next change (observation 9), and the entry says so;
  - item 59 (F6's description): applied;
  - item 81 (run 3, "the blind review's findings applied"): applied, "all but F5 (F7 by declaration)";
  - item 111 (T3, where the §4 citation stands): applied, in the checker's words.
- **The NOT CHECKABLE items** (7, 11, 30, 39, 43, 47, 61, 62, 64, 65, 72, 74, 76, 83, 93 and 101) stand: files not yet
  made, Code's own acts, and words that are in no file.
- **The observations:**
  1. Applied: the entry runs Departures, then Values-check, then Committed by path, as the entries of `9f64305`,
     `732a58f` and `1272702` do.
  2. Applied: F7 joins R10 to R14 and F5 on LOCK-n v0.1's list, in T1 and T3.
  3. Applied: the entry states as Code's reading that condition (a) concerns reports written under the old schema,
     and quotes the coordinating session's acceptance of the call sites: "(a) holds, with the call sites as you list
     them; the entry states them."
  4. Applied: "Every finding but F5 is applied (F7 by declaration)".
  5. Applied: "A-n2 §…" and "the answers' §…" in the entry's list of what the change does.
  6. Applied: the self-test raw now cites the compliant form, with item 3's exclusions and `data/mf3`'s, which
     printed nothing when Code ran it. Code's earlier run of the bare form is a departure in the entry.
  7. Applied: the monitors' refusal of a ceiling that is not positive.
  8. Applied: a headline line, in v2g's form: nothing of the change ran on a checkpoint's weights.
  9. Left: changing `runner.py`'s docstring now would move self-tested bytes after run 3. R13's entry text states the
     exact form and that the docstring is corrected at the file's next change.
  10. Applied in T3 ("adjudicated"). The check's name in `runner.py` waits with observation 9, and the entry says so.
  11. Applied: a sentence in the review raw's head on the report's line numbers.
  12. Applied: a line in the self-test raw on the 400-character cut.
  13. Applied: "which serves the BACKEND extension's two commands, backend-ext and backend-ext-2".
  14. Applied: the second draft's comment, with the review's O1 bound of 4 nats.

## 2. The texts changed after the check, and the edits checked by tool

- **All three texts changed after the check,** by the dispositions above. The entry and the self-test raw changed
  also by the coordinating session's wording for the package digest (its message after run 3): the digest stated
  "as computed by shell", the same computation reproducing HEAD's recorded digest, and the package's own `hashes` at
  G-VEC's launch files, in a window of its own, with the box comparing against it.
- **The edits, checked by tool:**
  - a fixed-string search over the unwrapped final texts: each disposition's new wording present, and the wording it
    replaced absent, 44 of 44;
  - the section order, by line;
  - the entry's quotations found in their sources, 19 of 19, and the review head's, 4 of 4.
- **The finals:** the entry `71110a2f…79d8`; the self-test raw `9f063645…3a83`; the review raw `5f841fe8…8663`.

## 3. The report as returned

```text
VALUES-CHECK: T1 (S/step4b/schema/commit/entry.md), T2 (S/step4b/schema/commit/selftest_raw.txt), T3 (S/step4b/schema/commit/review_head.md)

Before checking, I confirmed that the brief and all three texts hash to the sha256s the brief gives (brief: 142 lines). HEAD is 9f64305. Every named repository file I used is tracked and clean (`rev-parse HEAD:<path>` equals `hash-object`).

ITEMS

T1, the entry

1. T1:1–6. Header: the date; the citations (A-n2 v0.1 §2.1, §2.2, §6.3 (3); answers §4, §5; the PI's item 4 of "N. n-build (and the pod session on the box)", "route as given"); committed after backend-ext-2's entry; what the change adds. **CONFIRMED.** A-n2 lines 24, 26, 48; answers lines 39, 43; routing raw lines 14, 18, 26; 9f64305's parent is 732a58f and its subject is backend-ext-2's entry.

2. T1:8. All four files on HEAD 9f64305 are as 732a58f left them. **CONFIRMED.** `git diff --name-only 732a58f 9f64305 --` over the four files (plus hftiny.py and n_analyze.py) prints nothing.

3. T1:9–11. The four hash abbreviations and their numstats. **CONFIRMED.**
   - shasum of S/step4b/schema/draft/*.py, abbreviated with cut: 5cbf60db…574c, e8e81ab0…f787, dca64c0f…8a2a, e284a9f2…32b6.
   - `git diff --no-index --numstat`: 141/25, 98/17, 7/2, 11/3.

4. T1:11. hftiny.py and n_analyze.py do not change. **CONFIRMED** (neither is one of the four; both clean at HEAD).

5. T1:12–14. The digest moves f927608c…3c03 → f09898ee…b8f9; it is computed by shell in package_sha256_of's form; HEAD's files give the first; the self-test prints no digest. **CONFIRMED.**
   - pkgsha.sh on valence_core/n gives f927608c…3c03; on S/step4b/schema/overlay/valence_core/n it gives f09898ee…b8f9.
   - I also recomputed both independently, by a shell loop over HEAD's 14 files named one by one, with schema/runner/primitive taken from S/step4b/schema/draft/ for the final. The results are the same two digests.
   - The form matches valence_core/m/resume.py:328–350 (with REPO at :86, so rel = valence_core/n/<name>).
   - The three run outputs hold only FAIL lines and the count.

6. T1:15–16. 409/409; 400/403; 404/404. **CONFIRMED** (S/step4b/schema/selftest_run3/1/2.txt; the .exit files say exit 0 / 1 / 0).

7. T1:16, :133–134. The two raws' names and contents. **NOT CHECKABLE.** Neither file exists yet; name-only `ls` shows no collision, including …_valuescheck.md.

8. T1:17. "420, the 409 plus the 11 box-only HF cases". **IMPRECISE.**
   - The arithmetic is right: 409 + 11 = 420, and 11 = 408 (results/raw/2026-11-19_n-step4_bext2-v1_selftest.txt:3) − 397 (results/raw/2026-11-18_n-step4-driver-v2g_selftest.txt:34).
   - But 11 is a net difference, not a count of cases. The box runs 13 HF checks (hftiny.py's 12 at :71–124, plus the driver's HF vanilla score at scripts/n_sessions.py:1468) in place of the laptop's two skip lines (hftiny.py:56; n_sessions.py:1471).
   - **Fix:** "On the box, by arithmetic only: 420, the 409 plus the box's 11 checks more (its 13 HF checks in place of the laptop's two skip lines);"

9. T1:18–20. Review totals; "Every finding but F5 is applied"; each mutant killed; F5 goes to the seat and n-analyzer. **CONFIRMED.** review_report.md has F1–F5 RISK, F6–F8 NIT, M1–M7, O1–O9 and "I found no BUG". The kills are item 105; F5's routing is in (c4). See observation 4.

10. T1:21–22. SCHEMA_SHA256 is now 0ea39600…0db6, which is d791bd9's schema.py and HEAD's; n-analyzer moves it in its own commit. **CONFIRMED.** scripts/n_analyze.py:2730; shasum of valence_core/n/schema.py; rev-parse d791bd9:… equals HEAD:… (compared in the shell); n-analyzer's (b).

11. T1:23–24. n-analyzer "confirmed it on 2026-11-19". **NOT CHECKABLE.** n-analyzer's words carry no date. "The seat's names in §5" is confirmed (answers line 43).

12. T1:25–26. The PAUSE_KINDS tuple and the §5 quote. **CONFIRMED** (draft/schema.py:1122; answers line 43).

13. T1:27–31. The three new fields, their null and floor rules, and "entered as (k + 1, n + 2)". **CONFIRMED.** draft/schema.py:487–499, :262–263, :839–853 (:852 is "Code's addition"); A-n2 line 24; answers line 43.

14. T1:32. The identity bound equals the ceiling where both are set; "its bound is C". **CONFIRMED** (draft/schema.py:854–856; A-n2 line 26).

15. T1:33–34. The counter's null and int rules. **CONFIRMED** (draft/schema.py:1205–1208, :1510–1515; draft/runner.py:370).

16. T1:35–36. check_report's alpha and ceiling rules. **CONFIRMED** (draft/schema.py:1458–1460, :1429–1430).

17. T1:37–38. The runner fires, "second in the precedence after `nonfinite`". **IMPRECISE.**
   - The behaviour is right: draft/runner.py:197–207 checks any re-computed read; the counter is at :203; the pause comes at once at :512–519; A-n2 §2.1 says "pauses at once".
   - But in PAUSE_KINDS (draft/schema.py:1122) the kind is third, after rendering and nonfinite. It is second only in observe()'s list.
   - **Fix:** "…fires `fidelity-ceiling` at once (§2.1: "pauses at once"), directly after `nonfinite` in the precedence, and is counted."

18. T1:39. With no ceiling it never fires. **CONFIRMED** (draft/runner.py:201; the check at :662–665).

19. T1:39–40. A wrong alpha is refused before any read. **CONFIRMED.** draft/runner.py:388–390 comes before the root's mkdir (:394) and before the launch loop. The check at :768–771 asserts nothing is written.

20. T1:41–42. example_identity's values. **CONFIRMED** (draft/schema.py:1614–1616; the accept at :2130ff).

21. T1:42–46. The moved tests: "in `schema.py`, four refuse cases". **FAIL.**
   - The primitive and runner changes are right: draft/primitive.py:398 (bound 0.25) and :459 (fresh_bias 2.0, was 0.5); draft/runner.py:638 (shift 0.5, was 0.25).
   - The schema moves three refuse cases, not four: :2059 (bound 0.0 → 0.25), :2060–2061 (shift 0.25 → 0.5) and :2077 (bound 0.0 → 0.25).
   - All 25 lines removed in HEAD→final are accounted for. "a bound not the lock's" (:2062) is unchanged.
   - **Fix:** "in `schema.py`, three refuse cases;"

22. T1:47–48. The driver's backend-ext identity gains BEXT_ALPHA 0.01 with a null ceiling and median rel, and its self-test expects them. **CONFIRMED.** HEAD scripts/n_sessions.py:436 has `BEXT_ALPHA = 0.01`; draft/n_sessions.py:602–604 and the check at :1177–1186.

23. T1:49–50. "each in a battery window the coordinating session granted for its four files". **IMPRECISE.**
   - Per (c1), the windows for runs 1 and 3 named all four files' sha256s.
   - Run 2's window was "on draft 2", naming only runner.py 10a33707….
   - **Fix:** "…each in a battery window the coordinating session granted for its bytes (runs 1 and 3 naming the four files' sha256s, run 2 draft 2's `runner.py`):"

24. T1:51. The first draft's runner c615681c…f1ec, with the second draft's other three files, ran 400/403, exit 1. **CONFIRMED.** (c1)'s run-1 hashes equal draft_reviewed's three files; selftest_run1.txt:4; the .exit file says exit 1.

25. T1:52–54. The three failing checks' names. **CONFIRMED** (selftest_run1.txt:1–3; the checks are at draft/runner.py:836, :953, :960).

26. T1:55–57. The cause: +2.0 on logit 9 in every steered re-computation, about 2 nats, above 0.25; each stage paused as fidelity-ceiling at read 2, before its binomial. **CONFIRMED.**
   - The doubles' `full` does `if injections: rows[:, 9] += 2.0` (draft/runner.py:824–830, :925–931).
   - The ceiling of 0.25 comes from test_identity → example_identity() (valence_core/n/primitive.py:356–365).
   - In run 1's output, all three pauses are kind 'fidelity-ceiling', launch_index 2, binomial None.
   - "About 2 nats" is the second draft's own comment (:831), not something I computed.

27. T1:58–62. The second draft is +13 −3, in the self-test only; the three tests run under ceiling = bound = 10.0; one new check; 404/404, exit 0. **CONFIRMED.** Numstat draft1_runner.py → draft_reviewed/runner.py is 13/3, all inside _selftest (ident4 at :814, ident_hi at :920, the rep_c check). Run 2's file and .exit agree.

28. T1:63–64. The (c2) quote. **CONFIRMED** (verbatim).

29. T1:64–65. TAU bounds the relative discordance and C the absolute one in nats. **CONFIRMED** (valence_core/n/schema.py:397–400, :529–536; draft/schema.py:496–497).

30. T1:65–66. "the double's margin scales have not been measured". **NOT CHECKABLE.**

31. T1:67–68. The third draft: four more runner checks, one primitive check, the schema's three new cases inside one line; 409/409, exit 0. **CONFIRMED.**
   - Runner checks at draft/runner.py:651–653, :657–658, :769–771, :944–949; primitive at :401–403; schema at :2124–2129.
   - The driver reports the schema's self-test as one line (draft/n_sessions.py:196–197).
   - Run 3's file and .exit agree.

32. T1:69. The first draft's output is kept, 8a4123f3…993e. **CONFIRMED.** T2 lines 39–42, with the five-space indent cut off, hash to that value, which is selftest_run1.txt's.

33. T1:70–71. The grep's scope and the line basis. **CONFIRMED.** I ran my own greps over the same files. A whole-tree `git grep -l check_report`, with item 3's exclusions and data/mf3's, finds no other code file.

34. T1:72. runner.py:326 (`_prior_report`, called from run() at :397), "at a resume". **IMPRECISE.**
   - The line numbers are right.
   - But run() calls `_prior_report` on every invocation (:397), before it looks at `resume` (:398). So the check also runs on a fresh run that finds a report, which is refused after the check.
   - **Fix:** "the stage's own report on disk, at every invocation that finds one (a resume; a fresh run over one is refused after the check);"

35. T1:73. runner.py:551. **CONFIRMED** (the check runs before the atomic write at :553).

36. T1:74–75. n_sessions.py:867 (`prior_state`) and :902 (`first_stage_check`), called only from run_backend_ext at :1055 and :1057; both stages COMPLETE. **CONFIRMED.** These are the draft's lines; there is no other caller; both stages' COMPLETE is shown at RESULTS.md:24–25 and :66.

37. T1:76. n_analyze.py:5660 and :5666. **CONFIRMED.**

38. T1:77. n_analyze.py:4258: the fixture's counters lack the new field. **CONFIRMED** (:4243–4246).

39. T1:77–78. "n-analyzer has it in hand in its own draft". **NOT CHECKABLE.**

40. T1:79. The self-test call sites: runner.py:700 and :751, n_sessions.py:1786 and :1788, and the schema's own. **CONFIRMED.**

41. T1:81–82. The summary: check_report "reads only a stage's own report through the runner … and the campaign's report". **IMPRECISE.**
   - The battery fixture (:4258) and the self-tests also call check_report on paths still to run.
   - **Fix:** "So on a path still to run, beyond the self-tests' and n-analyzer's battery's own fixtures, `check_report` reads only a stage's own report through the runner, written under this schema, and the campaign's report in `scripts/n_analyze.py`."
   - See observation 3.

42. T1:83–86. Why the old reports and cells fail, and that a cell fails through load_cell → check_cell. **CONFIRMED** by reading the checks.
   - `_check_table` refuses missing keys (valence_core/n/schema.py:637–643).
   - HEAD's bext_identity writes a fidelity_rule with six keys (HEAD scripts/n_sessions.py:597–598); HEAD's runner writes no such counter (HEAD runner.py:347–351).
   - The reports were checked before writing (HEAD runner.py:526).
   - cells.py:148 → check_cell → check_stage_identity (schema.py:1050).

43. T1:83. "no run was made on them". **NOT CHECKABLE.**

44. T1:87–88. backend-ext.json was committed at 6df2131 and 6e3474d (HEAD's); its cell at 6df2131. **CONFIRMED.** `git log --format` over each named path; rev-parse comparisons show 6e3474d's report is HEAD's, 6df2131's report differs from it, and 6df2131's cell is HEAD's.

45. T1:89–90. backend-ext-2's report and cell were committed at 9f64305. **CONFIRMED** (same method).

46. T1:91–92. No campaign report exists; the figures stand; re-reading needs 9f64305's package. **CONFIRMED.** n-analyzer's (a): "no campaign report exists under the old schema"; draft/schema.py:146–150; the review's O2.

47. T1:93–94. LOCK-n v0.1's draft will carry R10–R14 and F5. **NOT CHECKABLE** (a plan). See observation 2.

48. T1:95–100. R10 and its grounds. **CONFIRMED.** Answers line 43 (the §5 quote, allowing for bold markup); the v2f quote is at RESULTS.md:711–712, in 1272702's entry.

49. T1:101–103. R11. **CONFIRMED.** §5 names the counter but gives no null rule; the quoted form is at draft/schema.py:200.

50. T1:104–107. R12; the §4 quote; the (c4) quote. **CONFIRMED** (draft/runner.py:33–42, :450–451; answers line 39).

51. T1:108–109. R13: "as a trial and an exceedance". **IMPRECISE.**
   - The read does stay in the batch (only a binomial fire clears it, :450–451), and it is a trial (:210–217).
   - But it is an exceedance only if its rel is above TAU (:220–223). Since rel = absdiff / scale (schema.py:529–536), an absdiff just above C = 0.25 exceeds TAU only where the cached scale is below C/TAU, about 14 nats.
   - **Fix:** "A ruled `fidelity-ceiling` pause leaves its read in the binomial's batch, as a trial, and as an exceedance where its rel is above TAU."

52. T1:110–111. R14. **CONFIRMED.** draft/schema.py:839 and :844–846; STAGES is ("campaign", "time", "backend-ext") per RESULTS.md:708; the "timing" re-computation fires (:654–658).

53. T1:112–114. F5's description. **CONFIRMED** (review F5; (c4)).

54. T1:115–118. The §6.3 (3) quote and the two commit subjects. **CONFIRMED** (A-n2 line 48; `git log --format=%s` of 2822721 and 977b78b).

55. T1:119–120. The pin sequence, and that Code sends n-analyzer the commit and schema.py's sha256. **CONFIRMED** against n-analyzer's (b) and (c3) item 1; the sending itself is still to come.

56. T1:121–125. The box (O5). **CONFIRMED.**
   - hftiny.py:102–103 builds its identity from test_identity (ceiling 0.25) with the bound set to 1e-3; it calls check_record only (:116).
   - check_record (schema.py:845) never calls check_stage_identity; only check_cell (:1050) and check_report (:1330) do.
   - The new rules at draft/schema.py:849–856 would refuse that identity. The 420 arithmetic is item 8's.

57. T1:126–127. The review's scope and totals. **CONFIRMED.**

58. T1:128–131. F1–F4 and F8 as applied; "These kill M1 to M7". **CONFIRMED** (items 96–105).

59. T1:131. "F6 (docstrings and check names)". **IMPRECISE.**
   - F6 changed docstrings, one comment (draft/runner.py:266) and one check's name (draft/n_sessions.py:1177–1179).
   - **Fix:** "F6 (docstrings, a comment and a check's name)"

60. T1:132. Declared: F7, R10–R14; not applied: F5, O5, and O9 ("two unreachable lines"). **CONFIRMED.** O9's lines are now draft/runner.py:413–414 (they were :406–407 in the reviewed draft).

61. T1:137–140. Code's transcript greps. **NOT CHECKABLE.**

62. T1:141–143. Code's `git log` with %ad, and the rev-parse values printed. **NOT CHECKABLE.**

63. T1:144–146. The reviewer's departures. **CONFIRMED** (review_report.md:127–132).

64. T1:148–151. The committed-by-path list. **NOT CHECKABLE.**

65. T1:153–154. The commit-time count is 0 "(the third sitting's answers, §5.2)"; not pushed. **NOT CHECKABLE.** That source is not one of the brief's; the citation matches RESULTS.md:136 and :264.

66. T1:155–157. Next. **CONFIRMED** against (c5) and (c3) item 1. See observation 2.

T2, the self-test raw

67. T2:1–3. The header. **CONFIRMED.**

68. T2:5–6. `git diff --name-only 732a58f 9f64305 -- valence_core scripts` prints nothing. **CONFIRMED** (I ran it as written; output empty). See observation 6.

69. T2:7–10. The four full sha256s. **CONFIRMED** (each line contains the computed digest).

70. T2:11–16. The digests and their form; f927608c… "as v2f's raw records it". **CONFIRMED** (item 5; results/raw/2026-11-18_n-step4-driver-v2f_selftest.txt:7).

71. T2:18–20. HF cases are skipped and counted on the laptop; the schema module counts as one line. **CONFIRMED** (scripts/n_sessions.py:6–9, :191–192, :1470–1471 at HEAD; hftiny.py:55–57).

72. T2:21–23. The overlay was a git archive of 732a58f on v2g's paths with the three exclusions, with the drafts swapped in. **NOT CHECKABLE.** pkgsha.sh's digest of the overlay's package equals the final drafts' digest, which is consistent.

73. T2:23–24. HEAD then moved to 9f64305, which changed none of the overlay's paths. **CONFIRMED.**
   - 9f64305's parent is 732a58f.
   - `git show --name-only --format= 9f64305`, with the three exclusions, lists .gitignore, RESULTS.md and eight results/raw/2026-11-19_n-step4_bext2-v1_* files. None is on v2g's path list (v2g raw lines 13–17).
   - Its data/n changes are under ckpt/ and reports/, which the overlay excludes.

74. T2:25–28. The command. **NOT CHECKABLE** (same form as the v2f and v2g raws).

75. T2:29–30. The windows were granted "for its four files". **IMPRECISE** (as item 23).
   - **Fix:** "Each run was in a battery window the coordinating session granted for its bytes (runs 1 and 3 naming the four files' sha256s, run 2 draft 2's runner.py), each file re-hashed in the overlay just before the run."

76. T2:30. Each file was re-hashed before the run. **NOT CHECKABLE.**

77. T2:32–36. Run 1's four hashes. **CONFIRMED** (and they match (c1)).

78. T2:37–42. Exit 1; the output sha256; the reproduced output. **CONFIRMED** (the .exit file; lines 39–42 without the indent are byte-identical to selftest_run1.txt).

79. T2:44–47. The explanation. **CONFIRMED** (item 26; the comment is at draft_reviewed/runner.py:812–813).

80. T2:49–56. Run 2: its hash, description, the other three files, exit 0, the output sha, the reproduced line. **CONFIRMED.**

81. T2:58. "the blind review's findings applied". **IMPRECISE** (F5 was not applied).
   - **Fix:** "the blind review's findings applied, all but F5"

82. T2:58–62. Five checks more (four runner, one primitive; the schema's three inside one line); exit 0; the output. **CONFIRMED** (line 62 without the indent hashes to b7f87ff9…d868).

83. T2:64. "The box has not run this change." **NOT CHECKABLE.** It is consistent with the record: the box's last self-test raw is v2g's 408/408.

84. T2:64–65. "the laptop's 409 plus the 11 box-only HF cases". **IMPRECISE** (as item 8).
   - **Fix:** "420, the laptop's 409 plus the box's 11 checks more (its 13 HF checks in place of the laptop's two skip lines: 408 on the box against v2g's 397 on the laptop, at backend-ext-2's start)"

85. T2:65–66. 408 against 397; the change adds no box-only check. **CONFIRMED.** RESULTS.md:62–64; no new check in the four deltas is gated on HF availability; hftiny.py is unchanged.

86. T2:66–67. The box's next self-test is at G-VEC's launch. **CONFIRMED** against (c4), (c5) and O5.

T3, the review raw's head

87. T3:1–3. Title, PI date, Code. **CONFIRMED.**

88. T3:5–11. What was reviewed, and the hashes. **CONFIRMED** (review_brief_final.md:7–16, :49–55).

89. T3:13. The review brief: c6505851…6cca, 90 lines. **CONFIRMED.**

90. T3:14–20. What the review brief contained. **CONFIRMED** (review_brief_final.md:15, :18–47, :49–55).

91. T3:21–26. The list of record v2 and the bars. **CONFIRMED.** Lines 86–90 of the review brief hash equal to lines 138–142 of this brief.

92. T3:28–29. The report: 133 lines, dc822457…2ea0, no local path. **CONFIRMED** (a containment check for local-path strings finds none).

93. T3:28. "extracted … by `jq`". **NOT CHECKABLE.**

94. T3:31. The totals. **CONFIRMED.**

95. T3:35–37. The third draft's hashes, and 409/409 in a window granted for them. **CONFIRMED** ((c1) run 3).

96. T3:39–40. F1. **CONFIRMED** (draft/runner.py:768–771; the inputs' alpha is 0.01 at :734).

97. T3:41–46. F2's three checks. **CONFIRMED.** draft/runner.py:651–653 uses margins 1.875 and 2.125 from example_record's literals (schema.py:1592–1595, :1623–1624); also :654–658 and :940–949, with the counter at 2.

98. T3:47–48. F3. **CONFIRMED** (draft/schema.py:2128–2129; draft/primitive.py:399–403).

99. T3:49–50. F4. **CONFIRMED** (draft/schema.py:2124–2127).

100. T3:51–54. F5 not applied; the agreed form's words; the (c4) quote. **CONFIRMED** (review_brief_final.md:29–30; (c4) verbatim).

101. T3:54, :62, :71. "n-analyzer is told" / "relayed with the sha". **NOT CHECKABLE.**

102. T3:55–60. Where F6 was applied. **CONFIRMED** (draft/schema.py:101–106, :423, :1595–1596; draft/runner.py:266; draft/n_sessions.py:1177–1179, :126–130).

103. T3:61–62. F7 is declared in a code comment and in the entry. **CONFIRMED** (draft/schema.py:852; T1:30).

104. T3:63. F8. **CONFIRMED** (draft/schema.py:843).

105. T3:64. M1–M7 are each killed by the named check. **CONFIRMED** by reading the code.
   - M1 fires on k_eq; M2 misses k_reach; M3 lets the alpha run proceed.
   - M4 accepts a bound of 0.25 under a ceiling of 0.3; M5 refuses a median of 0.0.
   - M6 refuses the exact-0.25 accept (example_record sets `within` by `<=`, schema.py:1641); M7 makes sh0 not within.

106. T3:65–67. O1. **CONFIRMED** (draft/runner.py:937–938).

107. T3:68–69. O2. **CONFIRMED** (draft/schema.py:146–150; draft/n_sessions.py:126–130).

108. T3:70. O3. **CONFIRMED.**

109. T3:72–75. O5; the (c4) quote; 420. **CONFIRMED.**

110. T3:76–79. O6: R12 declared in the docstring and the entry; the (c4) quote. **CONFIRMED** (draft/runner.py:38–42).

111. T3:77–78. "The citation no longer sits inside the batch's PIN." **IMPRECISE.**
   - The §4 citation is still inside the FIDELITY BINOMIAL PIN (draft/runner.py:33–48). What changed is that it is now in its own sentence (:39–41), followed by the nesting reading (:41–42).
   - **Fix:** "The citation now stands in a sentence of its own, on alpha's value, followed by the reading that the evaluations nest and that LOCK-n states which form binds."

112. T3:80–81. O7. **CONFIRMED** (draft/runner.py:55–56; the check at :648–650).

113. T3:82. O8. **CONFIRMED** (draft/runner.py:44–45, :53–55).

114. T3:83. O9 is left. **CONFIRMED.**

115. T3:84. The reviewer's departures are listed in the entry. **CONFIRMED** (T1:144–146).

TOTALS: 115 items. 87 CONFIRMED, 11 IMPRECISE (8, 17, 23, 34, 41, 51, 59, 75, 81, 84, 111), 1 FAIL (21), 16 NOT CHECKABLE.

OBSERVATIONS

1. **Section order.** If @VC_BLOCK@ is the values-check bullet, it sits before Departures (T1:135–136). The entries of 9f64305, 732a58f and 1272702 all run Departures, then Values-check, then Committed by path.

2. **F7 on the lock's list.** (c4) puts "F7, R10 and R12–R14" in the entry *and* on the lock's list. T1:93–94 ("all of them, and F5") and T1:157 ("R10 to R14 and F5") leave F7 off, and so does T3:61–62.

3. **Condition (a)'s parenthetical.** (c3)(a) asks that nothing call check_report on a backend-ext or backend-ext-2 report "(or on any stage other than "campaign")" on any path still to run, and says that if one exists it becomes a STOP.
   - Read literally, runner.py:326 and :551 check whatever stage the runner runs, including G-TIME-n's ("time").
   - The schema's and driver's self-tests check backend-ext-stage reports they build themselves (including through n_sessions.py:867/:902).
   - n_analyze.py:5660 runs check_report before the stage test at :5666.
   - All of these are under the new schema. The entry's closing sentence reads (a) as being about old-schema reports. That reading may be right, but it is Code's; it should be stated as such, or confirmed with the coordinating session.

4. **F7 classed two ways.** T1:19 says "Every finding but F5 is applied", but T1:128–132 lists F7 under Declared, not Applied. Suggest "…applied (F7 by declaration)".

5. **Unqualified section numbers.** In T1, §2.1 and §2.2 (lines 29, 32, 38) mean ADDENDUM-n2, while §4 and §5 (lines 26, 31, 97, 101, 105) mean the answers. The answers also have a §2.1 and §2.2. Writing "A-n2 §…" would remove the ambiguity.

6. **A possible undeclared departure.** T2:5–6 cites `git diff --name-only … -- valence_core scripts`, which names two folders without item 3's exclusions or data/mf3's. 732a58f's entry declared this class as a departure. If Code ran that form, T1's departures should list it.

7. **An omitted behaviour.** The Monitors now refuse a ceiling that is not positive (draft/runner.py:189–190, checked at :666–671). T1 does not mention it.

8. **A missing headline line.** The 732a58f and 1272702 headlines say nothing ran on a checkpoint's weights and that the runs were model-free (nice -n 19, under Q-F3's laptop rules). T1 has no such line.

9. **R13's wording is also in the code.** draft/runner.py:44–45 says the read stays "a trial, and an exceedance". Changing it moves self-tested bytes, so it may have to wait for the next runner change.

10. **"Cleared".** The check name at draft/runner.py:944–945, and T3:44–45, say the ruled ceiling pause is "cleared", while R13 says a ceiling ruling "clears nothing in the batch". "Adjudicated" would avoid the clash.

11. **The report's line numbers.** T3 §2 cites the second draft's line numbers (for example PAUSE_KINDS at schema.py:1115 there, :1122 in the final; O9's runner.py:406–407, now :413–414). Its "S/step4b/schema/draft/" held the second draft at the time; that draft is now in draft_reviewed/. A sentence in the head saying so would prevent misreading.

12. **The truncated FAIL line.** T2's run-1 third line ends mid-hash because the driver cuts FAIL lines at 400 characters (scripts/n_sessions.py:187; the line is exactly 400 characters). A one-line note would stop it reading as a transcription fault.

13. **"the BACKEND extension's command".** At T1:74–75, run_backend_ext serves both backend-ext and backend-ext-2 (scripts/n_sessions.py:1111, :1990). "its two commands" would match "Both of its stages".

14. **Attribution of "about 2 nats".** T1:55–56 states "about 2 nats" as fact. T2 attributes it to the draft's comment; T1 could do the same. Per the review's O1, the value is 2 − L₂(S) + L₂(U), always below 4 nats.

DEPARTURES

1. One `awk` filter (`awk -F: '$1>1900'`) over `/usr/bin/grep -n` output from valence_core/n/schema.py. awk is an interpreter, which the brief bars. It was read-only and touched nothing under data/.

2. Two `sed` substitutions inside pipelines: one relabelling shasum output, one trimming `ls` error lines. These are a departure if the seat counts sed as an interpreter.

3. Git commands without item 3's pathspec, all printing names, ids or subjects only:
   - `git diff --name-only 732a58f 9f64305 -- valence_core scripts` (run as T2 cites it; it printed nothing);
   - `git ls-tree --name-only` on valence_core/n/ at 732a58f and at HEAD;
   - three `git log --format` calls on single commits (2822721, 977b78b, 9f64305) with no path.

4. Not barred by my reading, but stated for the seat to class:
   - the shell loop recomputing the package digest from named files (printf, wc -c, cat, shasum), alongside pkgsha.sh;
   - reading the whole of ADDENDUM-n2 and of the fourth-sitting answers, and RESULTS.md:20–23, beyond the sections the brief lists;
   - reading HEAD's scripts/n_sessions.py (the change's FROM file);
   - shasum and cat attempts on three non-existent scratch names (`selftest_run{1,2,3}.txt.exit`) before finding the actual `.exit` files, with no listing or glob;
   - `head`, `tail`, `cut`, `wc` and `tr` on named scratch files.

Nothing under data/mf3 was touched. No ckpt or reports file was read, listed, sized or timed: only `git log --format` and in-shell rev-parse comparisons named those paths. No writes, no network, and no guard marker in any argv.
```
