# n — the R12, F5 and R13 runner delta: the blind values-check, as returned, with every disposition

PI date 2026-11-20. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the drafts of the commit's three texts, at draft 2:
- T1, the RESULTS.md entry: `b79bf5ff…f203` (84 lines), with its values-check paragraph and the checker's departures
  as placeholders;
- T2, the review's raw, `results/raw/2026-11-20_n-tile-delta_review.md` here: `1373cbfc…5bd8` (256 lines);
- T3, the self-test raw, `results/raw/2026-11-20_n-tile-delta_selftest.txt` here: `867555e1…b09a` (44 lines).

**The checker's brief** (`0ceb6dbb…4e5b`, 86 lines, given to the checker as a file, with its sha256 to verify):
- named the texts and the sources: in Code's scratch, HEAD's two files and drafts 1 and 2 of each, the two self-test
  runs' outputs and exit files, the review's brief and report, the overlay the runs used (its two drafts, and its
  `valence_core/n` files for the package digest, recomputed by shell in `package_sha256_of`'s form) and Code's sweep
  of its own shell commands; in the repository, RESULTS.md (the entries of `db00d6d` and `003ae7d`), the seat's
  answers of the first sitting, the schema follow-up's values-check, G-CAL-n's record, `keys.py`, `cells.py`, and
  HEAD's `runner.py` and `schema.py`;
- asked for every factual claim to be checked (each figure, count, quotation, hash, line count and diff count, each
  citation, each statement of what the code does and of how the review was disposed of, the counts of checks and the
  package digests), Code's departures against the sweep, and T2's §2 to be byte-equal to the review's report;
- warned that several sources hold guard-marker words in their content, never to enter an argv;
- barred any interpreter but `shasum`, any write, any network, any guard marker in an argv, anything under
  `data/mf3`, any whole-tree git status, any read, listing, size or time of a ckpt or reports file, and, in Code's
  scratch, anything but the named files and the brief itself; and quoted the list of record v2's items 1–5, verbatim.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (217 lines, sha256
`9dc293fd…3826`); it holds no local root, and nothing in it is changed. It names scratch files only by their paths
inside the scratch folder. Its line numbers are draft 2's: the brief's draft files are `S/step4b/tile/draft/`'s, which
held draft 2 at the check (kept since at `S/step4b/tile/draft2/`). Draft 3 changes only the schema (§2), so the
report's runner lines and its schema lines up to 1802 are the committed bytes' own; its schema lines 1804–2261 are one
later in the committed bytes, 2263 is two later, and from 2265 on they are three later.

**Totals:** 101 items: 82 CONFIRMED, 9 IMPRECISE, 0 FAIL, 10 NOT CHECKABLE; and 7 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

- **The FAILs:** none.
- **The IMPRECISE items,** each applied in the checker's words or near them:
  - 9 (T1): `clear_batch` is gone, with its two calls in `run()` and the self-test's one (HEAD's `runner.py`: the
    definition at :248, the calls at :451 and :530 in `run()` and at :629 in the self-test; none in drafts 2 and 3);
  - 35 (T1): n-analyzer's cumulative fixtures are the review's O5; a fire at read 500, `example_pause`'s default,
    whose batch 341–500 does not start at a multiple of the cadence, is the review's F2;
  - 49 (T1): the departures state plainly the overlay check's `git hash-object` and `git cat-file --batch-check`
    against `db00d6d` (the paths on stdin; six runs by the second sweep, the sixth placing draft 3) and the one run
    of the kit's verify of `db00d6d`'s commit;
  - 57 (T2): the review's brief gave the FROM files by path, at HEAD, and the TO files by sha256;
  - 69 (T2): one refuse case, a batch on a non-finite pause that did not fire it, still injects `example_pause`'s
    default batch, 341–500; draft 3 pins it to its check's message (observation 2);
  - 74 (T2): F5's check name is "two exceedances in a tail shorter than a tile (2 of its 4 trials)", and its comment
    "two fidelity exceedances in a tail shorter than a tile";
  - 93 (T3): the command's `TMPDIR` is `<scratch>/step4b/tile/tmp`;
  - 97 and 100 (T3): 217, 228 and 233 are the schema's `accept(`/`refuse(` call lines; at run time its cases are 239,
    250 and 255, by reading. Code counted the five loops that call more than once, in each version: the ten records
    of `good`, the three alpha values, the report loop's seven reports, the PI-STOP loop's five and the binomial
    loop's two, 22 cases more than call lines. No call sits mid-line: each version's occurrences are its call lines
    and the two definitions.
- **The NOT CHECKABLE items** stand (3, 16, 24, 27, 40, 45, 51, 52, 89, 91): Code's acts and readings and the
  coordinating session's routing and grants, each consistent with its sources where it has one. Item 91's figures are
  the overlay check's own lines (168 files; 166 equal to `db00d6d`'s blobs; 2 differing, the drafts), printed at each
  of its runs.
- **The observations:**
  - 1: T2's head now says the review's line numbers are draft 1's, with the shifts for M1, M4–M5 and M6; this raw's
    head says the same of this report's (draft 2's), with draft 3's shifts;
  - 2: applied, in draft 3. Both refuse cases on a batch's presence ("a batch on a non-finite pause that did not fire
    it", "a binomial pause without its batch") now name their check's message, `expect="is set exactly when the
    pause's read fired the binomial"`, so a weakening of either direction no longer passes by another check's
    refusal. On the unmutated schema each case refuses by that message: `_fail` raises at the first failing check,
    and nothing before it in `check_report` reads the batch (Code's reading; the self-test's run 3: 578/578,
    exit 0);
  - 3: applied, in draft 3, as one docstring sentence: "The default read, 500, ends no tile, so a binomial fire at a
    read names its L." The default itself stays 500: 13 calls in the schema's own cases, one in the runner's and one
    in `scripts/n_analyze.py` use it for pauses that are not binomial fires (Code's count, by `awk` over the calls'
    arguments; `scripts/n_analyze.py:5116` passes 500 explicitly for its binomial fire);
  - 4: not applied in the code: binding a read-less tail's end to the stage's last read is of the family of F3's
    optional bound, not taken for the same reason (it would tie the example report's and n-analyzer's fixtures to
    read counts). T1 and T2 now say "exact at a read" and name the tail's unbound end;
  - 5: T1's departures now state plainly Code's `awk` (text edits and checks of its scratch files, and of its memory
    index) and its writes to its memory folder, outside the repository; and the kit's scripts' runs (item 49);
  - 6: a second sweep, from the first sweep's last command to the sweep itself, made after the check; T1's list rests
    on both;
  - 7: T1's power bullet now states the tiles' make-up under the runner's ORDER PIN and G-CAL-n's map, nothing
    merged: the 18 tiles outside N1-R are one cell's 160 reads each, 7 at dose-rule cells (160 trials) and 11 at the
    keyed sample's sessions only; N1-R's 30 tiles span four 40-read cells each, mixing its ±1 points with the others
    (Code's reading of `campaign_order`, `ARMS` and `ARM_CELLS`).

## 2. The code and the texts changed after the check, and the edits checked by tool

- **The code changed after the check,** as draft 3, in the schema only (observations 2 and 3):
  `valence_core/n/schema.py` `1cab28df…edff` (2527 lines, +6 −3 on draft 2), the runner unchanged. Its self-test, run
  3, in a battery window of its own: 578/578, exit 0, the output run 2's byte for byte (the self-test raw). The n
  package's digest, by shell: `06b55761…1d39`.
- **The texts changed after the check** by the dispositions above; by draft 3's figures (the schema's hash and diff
  counts and the package digest in T1 and T3, run 3 in T3, draft 3's sentence in T2); and in T1 by its values-check
  paragraph and the checker's departures, which replace the placeholders.
- **The edits, checked by tool:** fixed-string counts over each text unwrapped, for each disposition's new wording
  and each removed wording's absence; T2's §2 byte-equal to the review's report; T3's three output lines equal to
  the runs' outputs; and this raw's §3 equal to the values-check's report: 55 of 55.
- **No second full pass** was made over the texts.
- **The finals:** the entry `c40c80ef…42c5` (116 lines); the review's raw `06309853…9985` (264 lines); the self-test
  raw `cb37471c…8612` (56 lines).

## 3. The report as returned

BLIND VALUES-CHECK: the R12, F5 and R13 runner delta's texts (T1 entry, T2 review raw, T3 self-test raw)

Checked first:
- The brief is 0ceb6dbb…4e5b with 86 lines, as stated.
- T1 b79bf5ff…f203 (84 lines), T2 1373cbfc…5bd8 (256), T3 867555e1…b09a (44) and S/step4b/tile/review_report.md dbe9cce8…0517 (175) all match the brief.
- HEAD is db00d6d. Every named repository source is tracked and clean (rev-parse = hash-object): RESULTS.md, both raws, data/n/gcal/gcal.json, valence_core/n/{keys,cells,runner,schema}.py.
- S/step4b/tile/base/ equals HEAD's blobs. The overlay's runner.py and schema.py are draft 2's.
- I abbreviated every hash with a tool, not by eye.

ITEMS

T1 (S/step4b/tile/commit/entry.md)
1. T1:1–2. Claim: the binomial's window is the tile, F5's floor is asserted in the schema, and R13's two runner texts are corrected. CONFIRMED. Evidence: S/step4b/tile/draft/runner.py:35–54 (PIN) and :211–252 (Monitors); draft/schema.py:876–878; runner :50–51 and :1008.
2. T1:2–4. Claim: cites §3, §4 (b) and item 4, quoting "in G-CAL-n's delta or after its run by the launch order". CONFIRMED. Evidence: results/raw/2026-11-19_n-starred-twelve_design-to-code_answers.md:47–51, :56 and :82 (verbatim).
3. T1:4. Claim: "the coordinating session's routing after `db00d6d`". NOT CHECKABLE: no source holds it.
4. T1:4–5. Claim: model-free, on the laptop; moves the digest; lands before G-TIME-n. CONFIRMED.
   - The digest move is item 21.
   - "Before G-TIME-n" is in the answers at :51.
   - The sweep's only interpreter runs are the two self-tests (sweep lines 39 and 57).
5. T1:7. Claim: "the runner's cumulative-since-the-last-fire batch becomes the tile". CONFIRMED. Evidence: answers:51 (verbatim); the batch_*, next_due and unevaluated fields are replaced by tile_* (runner :179–184).
6. T1:7–9. Claim: the tile is the `cadence` reads launched since the previous evaluation, evaluated at its cadence-th read, a trial or not. CONFIRMED. Evidence: runner :35–38; :228 evaluates outside the trial branch.
7. T1:9–10. Claim: a fire's batch is the tile's first and last reads, ending at the read that fired it. CONFIRMED. Evidence: :211–214 (set at every read) and :241–243.
8. T1:10–11. Claim: the next tile starts at the next read; every read lies in one tile; a ruling clears nothing. CONFIRMED. Evidence: :245–247 reset the tile after every evaluation, fired or not; PIN :40–41.
9. T1:11. Claim: "`clear_batch` and its two calls are gone". IMPRECISE.
   - HEAD had three calls besides the def at S/step4b/tile/base/runner.py:248: two in run() (:451, :530) and one in the self-test (:629).
   - Draft 2 has none (grep count 0).
   - Instead: "`clear_batch` is gone, with its two calls in `run()` and the self-test's one".
10. T1:11–12. Claim: the tail is evaluated once when no read remains, and its fire has no read. CONFIRMED. Evidence: runner :521–533 (COMPLETE or CAP, then mon.pending()); :250–252.
11. T1:12–13. Claim: the alpha, p0 and SCOPE stand; a fire stands on the arms with a trial in its tile. CONFIRMED. Evidence: :30–31, :46–49 and :387–391.
12. T1:14–17. Claim: the premise is asserted, with its three reasons; run() refuses any other set before a launch; the tile-j formula follows. CONFIRMED.
    - :401 sorts on_disk by launch index.
    - :408–410 is the assert, before the launch loop at :464.
    - The invocation halts at :469, :485 and :519.
    - PIN :41–44; T2:111–113 (F2) and :199–201 (O3).
13. T1:18–19. Claim: F5 applies at every stage but backend-ext, "by Laplace's rule". CONFIRMED. Evidence: schema :256, :845 (pre_lock means backend-ext) and :876–878.
14. T1:19–20. Claim: the example p0 is 1 of 26, and 0 of 2400 at backend-ext. CONFIRMED. Evidence: schema :1647.
15. T1:20–21. Claim: example_pause takes its batch's p0 and alpha from an identity. CONFIRMED. Evidence: schema :1796–1812.
16. T1:21. Claim: "as agreed with n-analyzer". NOT CHECKABLE: only Code's review brief states it (S/step4b/tile/review_brief.md:26–28, "in no file").
17. T1:22–24. Claim: R13's two texts (the PIN quote; "adjudicated", not "cleared"). CONFIRMED.
    - runner :50–51 (verbatim across the line wrap) and :1008.
    - base :944 read "cleared".
    - These are the two texts of results/raw/2026-11-19_n-schema-followup_valuescheck.md:413 and :415 (its observations 9 and 10).
18. T1:25–28. Claim: the schema's form checks, which are Code's, plus the cadence refusal. CONFIRMED. Evidence: schema :183–187, :1479–1492, :1496–1498 and :874–875.
19. T1:28–29. Claim: the field texts name the tile. CONFIRMED. Evidence: schema :1186–1190 and :1203–1205.
20. T1:30–31. Claim: runner 9bf75cbb…d61e (+169 −87) and schema bedba2c7…c66a (+124 −28). CONFIRMED by shasum and by `git diff --no-index --numstat` from base to draft (169/87 and 124/28).
21. T1:31. Claim: the digest moves from e40c9871…9523 to 2984d642…eaec, by shell. CONFIRMED.
    - I recomputed both in the brief's form: over HEAD's 16 valence_core/n/*.py blobs, and over the overlay's 16 files.
    - 14 of the overlay's 16 files equal HEAD's blobs; the other two are draft 2.
22. T1:32. Claim: 575/575 and 578/578. CONFIRMED. Evidence: S/step4b/tile/selftest_run1.txt and selftest_run2.txt; both .exit files read "exit 0".
23. T1:33. Claim: run under `nice -n 19`. CONFIRMED: sweep lines 39 and 57.
24. T1:32–33. Claim: each run in a battery window the coordinating session granted. NOT CHECKABLE.
25. T1:33. Claim: 589 on the box by arithmetic. CONFIRMED: 578 + 11; the 11 appears at RESULTS.md:143 and :1875–1876.
26. T1:34–36. Claim: Code's readings in the PIN and the field text. CONFIRMED.
    - runner :44–45 and :51–53; schema :183 and :1203–1205.
    - evaluate() counts every evaluation.
    - binom_tail returns 1.0 at k = 0 (:93–94), so a tile with no trial cannot fire.
27. T1:38. Claim: "(n-analyzer's note, 2026-11-19)". NOT CHECKABLE.
28. T1:38–40. Claim: only the dose rule's points (0, +1, −1) always re-compute; elsewhere only the keyed 10% of sessions. CONFIRMED. Evidence: schema :275; valence_core/n/keys.py:5, :15–17 and :32.
29. T1:40–41. Claim: a tile at those points holds 160 trials, elsewhere about a tenth; §3's "about two and a half" holds for the former only. CONFIRMED.
    - answers:51 is quoted verbatim.
    - Under p0 = 1/26, a doubling is about 2.5 null standard errors over 160 trials and about 0.8 over 16.
30. T1:42–43. Claim: nothing merged; 7,680 reads make 48 tiles, with no tail. CONFIRMED.
    - gcal.json:51–84: all seven points have "merged": []; the status is PASS at :273.
    - schema :1978 gives 7,680 reads.
    - 7680 / 160 = 48, remainder 0.
31. T1:44–46. Claim: the review's O4. CONFIRMED. Evidence: T2:203–206; runner :32–34; schema :1440–1441; at HEAD, evaluation sat inside the trial branch.
32. T1:47–48. Claim: the review's O6. CONFIRMED. Evidence: T2:226; schema :872 and :876 both admit 3 of 3; runner :97–98.
33. T1:49–50. Claim: n-analyzer moves its pin and fixtures in its own commit; §3 is quoted. CONFIRMED. Evidence: answers:50 (verbatim) and :86; review_brief.md:33–34.
34. T1:50. Claim: n-analyzer's pin is 003ae7d's schema. CONFIRMED: scripts/n_analyze.py:2766 holds 5cbf60db…574c, which is base/schema.py.
35. T1:50–51. Claim: "its cumulative fixtures, and `example_pause`'s default fire at read 500, are not tiles the new checks accept (the review's O5)". IMPRECISE.
    - The facts hold: schema :1796 defaults to 500, giving the batch 341–500, which :1480–1482 refuse; scripts/n_analyze.py:5116 builds a fire at 500.
    - O5 (T2:220–224) does not mention read 500. The unaligned 341–500 is F2's point (T2:109).
    - Instead: "its cumulative fixtures (the review's O5), and a fire at read 500, `example_pause`'s default, whose batch 341–500 does not start at a multiple of the cadence (the review's F2), are not tiles the new checks accept".
36. T1:52. Claim: 0 BUG; 5 findings (3 RISK, 2 NIT); 8 mutants; 8 observations. CONFIRMED: T2:93–236.
37. T1:52–54. Claim: every finding is applied and each mutant meets a killing case. CONFIRMED by reading the draft-1-to-draft-2 diffs, not by running anything. See items 65–76; F3's optional bound was not taken, as T2:49 says.
38. T1:55–56. Claim: the raws' names. CONFIRMED: this brief, lines 13–14 and 18–19.
39. T1:58. Claim: the sweep covers Code's shell commands since db00d6d's commit time. CONFIRMED: S/step4b/tile/sweep/cmds.txt (6689e3f9…bf92, 65 commands); the time bound in line 65 equals db00d6d's commit time (`git log -1 --format=%cI`).
40. T1:58. Claim: "Code knows of no others". NOT CHECKABLE.
41. T1:59–61. Claim: jq reads of task outputs, each the hand-back's message only. CONFIRMED as far as the sweep reaches: line 44. The values-check's extraction comes after the sweep.
42. T1:61–62. Claim: one jq read of its own transcript, writing the sweep. CONFIRMED: line 65.
43. T1:62–63. Claim: one limited `git status --porcelain`. CONFIRMED: line 8 is the only git status. Its output ("printed nothing") is not in the sweep.
44. T1:64. Claim: `git show HEAD:<path>` into scratch copies. CONFIRMED: line 21.
45. T1:64–66. Claim: the kit's digest internals (ls-tree, cat-file -s, show; wc -c). NOT CHECKABLE: lines 43 and 61 call kit_lib.sh, whose body the sweep does not show. My recomputation in that form matches.
46. T1:66–67. Claim: git grep runs with ':!data/**'. CONFIRMED: lines 13, 15, 26 and 27.
47. T1:67–68. Claim: unpruned finds in the overlay, which is a copy of G-CAL-n's launch overlay. CONFIRMED: finds at lines 29, 36, 41, 52, 55 and 60; the copy is made at line 28. "No ckpt or reports folder" is not checkable by me.
48. T1:68. Claim: removals of Code's scratch check folders. CONFIRMED: lines 35 and 55.
49. T1:64–68, the list as a whole. IMPRECISE: it omits two things the sweep holds.
    - Five runs of S/step4b/gcal2/decode/overlay_check.sh against db00d6d (lines 28, 29, 35, 52, 55). This is T3:15–16's join of git hash-object against git cat-file --batch-check, which db00d6d's entry stated plainly (RESULTS.md:205–206).
    - The kit's verify of db00d6d's commit (line 1, kit_verify.sh).
    - Add: "the overlay check's `git hash-object` and `git cat-file --batch-check` over the scratch overlay's 168 files against `db00d6d`, the paths on stdin, in five runs; and one run of the kit's verify of `db00d6d`'s commit".
50. T1:69–75. Claim: the reviewer's departures. CONFIRMED: T2:240–250.
51. T1:78–83. Claim: committed by path; the home-folder count; nothing ran on a model; not pushed; Next. NOT CHECKABLE yet. As of now, T1–T3 and both drafts each hold 0 local-path matches.

T2 (S/step4b/tile/commit/review_raw.md)
52. T2:3. Claim: the PI date and the author. NOT CHECKABLE.
53. T2:5–6. Claim: one pass over draft 1; FROM is db00d6d's bytes, unchanged since 003ae7d. CONFIRMED: base blobs equal HEAD's; git log puts both files' last change at 003ae7d; one hand-back was extracted (sweep line 44).
54. T2:7–8. Claim: e8e81ab0…f787 (1022 lines) → db18cb48…81dd (1058); 5cbf60db…574c (2428) → 21cbe294…b389 (2492). CONFIRMED.
55. T2:9. Claim: run once, before the review: 575/575, exit 0. CONFIRMED: one run-1 command at line 39, before line 42 (filling the brief) and line 44 (extracting the report).
56. T2:11. Claim: the brief is fda516b3…e1ff, 82 lines. CONFIRMED.
57. T2:12. Claim: "gave the two deltas' FROM and TO files, by sha256". IMPRECISE.
    - review_brief.md:7–11 gives FROM by repository path at HEAD, with no sha256. Only TO carries one.
    - Instead: "gave the two deltas' FROM files (HEAD's, by path) and TO files (by sha256), and the `git diff --no-index -U3` form".
58. T2:12–15. Claim: the specification's sources. CONFIRMED: review_brief.md:14–32.
59. T2:16–18. Claim: the questions. CONFIRMED: :39–49.
60. T2:19. Claim: what the report must contain. CONFIRMED: :51–58.
61. T2:20–22. Claim: the list of record quoted verbatim, and the bars. CONFIRMED: :63–82. Its lines 78–82 are byte-identical to this brief's lines 82–86 (same sha256 for both five-line tails).
62. T2:24–25. Claim: §2 extracted by jq; 175 lines; dbe9cce8…0517; it names scratch files only by S/ paths. CONFIRMED: `tail -n +82 | cmp` against S/step4b/tile/review_report.md shows them equal; 0 local-path matches.
63. T2:27. Claim: the totals. CONFIRMED.
64. T2:31–33. Claim: draft 2 is 9bf75cbb…d61e (1104 lines, +65 −19) and bedba2c7…c66a (2524, +67 −35); 578/578, exit 0. CONFIRMED by numstat, wc -l and run 2's files.
65. T2:35–37. Claim: F1 is applied; the case is single-defect and kills M6. CONFIRMED by reading.
    - schema :2375–2376 and :2382–2384.
    - Only :1477–1478 refuses that batch: 160 is a multiple of the cadence, the span is 160, n is within the span, and the sums are within the state.
66. T2:38–40. Claim: F2's premise and its test case. CONFIRMED.
    - runner :408–410 is the assert; :1100–1104 copy the COMPLETE "ok" stage (:795–797) and remove one cell.
    - valence_core/n/cells.py:135–145 treats a missing cell as new, so the refusal comes from the assert.
67. T2:41–43. Claim: check_report's form checks. CONFIRMED: schema :1479–1490. See observation 4 on "exact".
68. T2:44. Claim: a cadence that is not positive is refused. CONFIRMED: :874–875, and check_report runs check_stage_identity (:1385) before the modulo at :1480.
69. T2:45. Claim: "The binomial fixtures sit on aligned tiles…". IMPRECISE.
    - True of every fire's fixture: :2373–2376, :2404–2406, :2411–2414 and :2225.
    - But the refuse case at :2261–2262 still injects example_pause's default batch, 341–500.
    - Instead: "…and the tail from 0 or 160; one refuse case, a batch on a non-finite pause that did not fire it, still injects `example_pause`'s default batch, 341–500".
70. T2:45–46. Claim: the docstring's L + 1 rule. CONFIRMED: schema :1799–1803.
71. T2:47–48. Claim: F3's sums, and 320 trials and 2 exceedances for two fires. CONFIRMED: :1419–1420, :1491–1492, :1496–1498, :1776–1777 and :1789–1790.
72. T2:49–51. Claim: the optional bound is not taken; M4 is killed in the runner. CONFIRMED: there is no evaluations bound in the schema; runner :1075–1078. The rationale is Code's reading.
73. T2:52–53. Claim: F4 is applied at both places. CONFIRMED: runner :44–45 and :51–53; schema :1203–1205.
74. T2:54. Claim: F5's quote, ""two exceedances (2 of its 4 trials)" in the check's name, and in its comment". IMPRECISE.
    - The name (runner :1017–1018) reads "two exceedances in a tail shorter than a tile (2 of its 4 trials)".
    - The comment (:984) reads "two fidelity exceedances in a tail shorter than a tile".
    - Instead: "F5 (NIT), applied: "two exceedances in a tail shorter than a tile (2 of its 4 trials)" in the check's name, and "two fidelity exceedances" in its comment."
75. T2:54–56. Claim: P = 0.00843, 0.00148 and 0.145. CONFIRMED: runner :878–881; shell arithmetic gives 3851/456976 = 0.0084271, 1/676 = 0.0014793, and 1 − 390625/456976 = 0.1451958.
76. T2:57–67. Claim: M1–M8 are each met by a killing case. CONFIRMED by reading, not run:
    - M1: runner :706–716.
    - M2: :682–690.
    - M3: :691–697.
    - M4: :1075–1078.
    - M5: :1092–1098 (reads 4–5 at +1/2 carry no re-computation, :762–766).
    - M6: item 65.
    - M7: schema :2393–2394.
    - M8: schema :2400–2403.
77. T2:68–70. Claim: O1, O2, O5 and O7 ask for nothing. CONFIRMED.
78. T2:71. Claim: O3 is applied. CONFIRMED: runner :408–410.
79. T2:72–74. Claim: O4 is in the PIN and the entry. CONFIRMED: :32–34 and T1:44–46.
80. T2:75–76. Claim: O6 is not applied. CONFIRMED: schema :876.
81. T2:77. Claim: O8 is applied. CONFIRMED: :2404–2407.
82. T2:78. Claim: the reviewer's departures are in the entry. CONFIRMED.
83. T2:80–256. Claim: §2 is byte-equal to the report. CONFIRMED by cmp.

T3 (S/step4b/tile/commit/selftest_raw.txt)
84. T3:1–2. Claim: the citations. CONFIRMED (answers :47–51, :56, :82). The date and author are not checkable.
85. T3:4–6. Claim: full hashes and diff counts. CONFIRMED.
86. T3:7–9. Claim: both digests in full. CONFIRMED (item 21).
87. T3:10. Claim: the digest follows package_sha256_of's form. CONFIRMED: valence_core/m/resume.py:328–349 and :86; my recomputation in that form gives both values.
88. T3:10–11. Claim: the self-test prints no digest. CONFIRMED: each run's output is one count line.
89. T3:13–14. Claim: the HF cases are skipped and counted where torch is absent. NOT CHECKABLE. It is consistent with the box's 11 extra checks.
90. T3:14. Claim: the schema's cases count as one aggregated line. CONFIRMED by arithmetic: the totals move 570 → 575 → 578 exactly with the runner's chk( lines (69 → 74 → 77), not with the schema's (217 → 228 → 233).
91. T3:15–16. Claim: the overlay has 168 files, 166 equal to HEAD. NOT CHECKABLE: I am barred from listing beyond valence_core/n, where 14 of 16 match and 2 are the drafts. RESULTS.md:205 gives 168 for the launch overlay, and sweep line 28 copies it.
92. T3:17–20. Claim: the command form (subshell; cd and a glob into the venv's bin folder; offline variables; nice). CONFIRMED: sweep lines 39 and 57.
93. T3:19. Claim: "TMPDIR=<scratch>". IMPRECISE.
    - Both runs set TMPDIR to S/step4b/tile/tmp (sweep lines 39 and 57).
    - The next line uses <scratch> to mean S.
    - Instead: "TMPDIR=<scratch>/step4b/tile/tmp".
94. T3:21–22. Claim: re-hashed before and after; tmp empty. CONFIRMED as commands: sweep lines 38/41 and 56/60. Their printed results are not in the sweep, and the window grant is not checkable.
95. T3:24–28. Claim: run 1. CONFIRMED: T3:28 is byte-equal to selftest_run1.txt (79c2940f…ef94).
96. T3:29–32. Claim: draft 1 adds five checks to 570. CONFIRMED.
    - chk( lines go from 69 to 74.
    - The additions are m3b (:698), m3c (:706), m3d (:718), m9 (:722) and rep_wb2 (:890).
    - The count was 570 at db00d6d (RESULTS.md:143), and no code commit has landed since bc50244.
97. T3:32. Claim: "The schema module's own cases grow from 217 to 228." IMPRECISE.
    - 217 and 228 are accept(/refuse( call lines in the source; Code's own count at sweep line 35 is of "calls".
    - The module counts a case per call at run time (schema :1863–1879).
    - Five loops call more than once (:1905, :2161, :2227, :2317, :2377), adding 22 cases in every version.
    - So by my reading (not run) the module counts 239 → 250.
    - Instead: "The schema module's own accept/refuse calls grow from 217 to 228 (its cases at run time from 239 to 250, by reading)".
98. T3:34–38. Claim: run 2. CONFIRMED: T3:38 is byte-equal to selftest_run2.txt (59841608…0f09).
99. T3:39–41. Claim: three checks added, three strengthened, one reworded. CONFIRMED.
    - Added (chk( 74 → 77): m3e (:691), rep_t (:1093) and the holes case (:1100–1104).
    - Strengthened: :690, :706–716 and :1078.
    - Reworded: rep7's name at :1017.
100. T3:41. Claim: "grow to 233". IMPRECISE, as item 97: 233 call lines, but 255 at run time by my reading. Instead: "…grow to 233 (255 at run time, by reading)".
101. T3:43–44. Claim: the box's count would be 589 = 578 + 11. CONFIRMED. "Nothing ran there" is consistent with the sweep.

TOTALS: 101 items: 82 CONFIRMED, 9 IMPRECISE (9, 35, 49, 57, 69, 74, 93, 97, 100), 0 FAIL, 10 NOT CHECKABLE (3, 16, 24, 27, 40, 45, 51, 52, 89, 91).

OBSERVATIONS
1. §2's line numbers are draft 1's. T2:84 names S/step4b/tile/draft/, which held draft 1 at the review and now holds draft 2 (draft 1 was kept at S/step4b/tile/draft1/, sweep line 52).
   - Against the committed bytes the numbers shift: M1's :240 is now :247, M4/M5's :514 is :524, and M6's schema :1472 is :1477.
   - The schema follow-up's review raw had a sentence in its head saying which bytes its line numbers refer to (that values-check's observation 11). T2's head could add one.
2. The refuse case at draft/schema.py:2261–2262 has no `expect`, and four or more checks refuse it besides the targeted one (:1467–1469): the alignment check, the k-above-state check, the sums check and the fires count.
   - So a one-directional weakening of :1467 would survive the schema's battery, as it would at HEAD (by reading).
   - `expect="is set exactly when"` would pin it.
3. example_pause's default launch_index is still 500. For a binomial kind that gives a batch check_report now refuses, which contradicts its own docstring; scripts/n_analyze.py:5116 builds such a fire. A default of 479, or a docstring line saying so, would help n-analyzer's pin move.
4. "Exact" (T2:38, :41; T1:53) holds for a fire at a read. A read-less tail is not bound to end at the stage's last read (the sum of per_arm obtained, minus 1). For example, rep_ft's accepted tail of 160–259 sits in a report whose reads run well past 259. This is the same family as F3's declined optional bound.
5. The sweep's search patterns (line 65) cannot see some things:
   - awk (lines 2, 17, 24, 33, 42, 46, 51, 55, 62, 63);
   - writes to Code's memory index (lines 2 and 37);
   - the insides of kit_verify.sh, overlay_check.sh and kit_lib.sh.
   No earlier entry declared Code's awk, so I graded nothing on this.
6. T1:59–61 includes the values-check's jq extraction, which comes after the sweep. A second sweep after it, as db00d6d's entry ran, would cover it.
7. The power bullet (T1:38–41) assumes a tile sits wholly at dose-rule points or wholly elsewhere. A tile's actual mix depends on the campaign's launch order, which the entry does not state.

DEPARTURES
None that a rule bars, by my reading. Stated plainly:
- Reads beyond the named repository sources, each file checked tracked and clean:
  - valence_core/m/resume.py :86 and :320–349;
  - scripts/n_analyze.py, two greps (its schema pin; its example_pause calls);
  - RESULTS.md, grepped whole beyond its two named entries.
- Git commands outside item 3's pathspec form:
  - `git log -4 --format='%h %H %ci'` with no pathspec;
  - `git log --format='%h %ci' bc50244..HEAD -- valence_core/n scripts/n_sessions.py`, which names a folder and printed nothing.
- For the digest: `git cat-file -s` and `blob` of HEAD's 16 n files; `wc -c` (by redirection) and `cat` of the overlay's 16; and `git hash-object` of those 16 against HEAD's blobs.
- Two commands were stopped by zsh's `=` expansion (an unquoted `echo ==` and `echo ==base`) before their later parts ran. One held a stray assignment, `awk_free=1`; no awk ran.
- I used zsh's own arithmetic for the P values.
- Otherwise:
  - no interpreter but shasum, no write, no network;
  - no guard marker in any argv;
  - nothing under data/mf3, data/*/ckpt or data/*/reports touched;
  - in S, only named files and the overlay's valence_core/n files by explicit name (one name-only `ls`), with no glob, find or folder grep.
