# n — G-CAL-n's delta: the blind values-check of its texts, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the delta's three texts, drafts of:
- T1, the RESULTS.md entry: `57c15d70…fba5` (77 lines), its values-check paragraph a placeholder;
- T2, the review raw, `results/raw/2026-11-19_n-gcal-delta_review.md` here: `fbc49c08…55a9` (227 lines), its head and
  §1 checked, its §2 checked only for being the report as returned;
- T3, the self-test raw, `results/raw/2026-11-19_n-gcal-delta_selftest.txt` here: `bf9c25ac…c4e5` (40 lines).

**The checker's brief** (`77a6f3d5…a2db`, 81 lines, given to the checker as a file, with its sha256 to verify):
- named the texts and the sources: in Code's scratch, by name and sha256, drafts 4 and 5 of both files, the review's
  brief and report, and both self-test outputs with their exit files; in the repository, the BUILD's two files (the
  delta's base), the seat's answers, RESULTS.md's BUILD entry and close lines, the BUILD values-check raw and the
  supplement raw, the code the texts describe, read only, and the package digest in `package_sha256_of`'s form over
  HEAD's blobs and with draft 5's `gcal.py` in place;
- asked for every factual claim to be checked: each figure, count, quotation, hash and hash abbreviation, citation,
  and statement of what the code does or the self-test checks, of what the review found and each disposition did,
  and each departure; and the count claim, that draft 5 adds exactly two checks to draft 4's 542;
- allowed `shasum` by name (on this machine a Perl script, which the list of record's item 1 permits), and barred any
  other interpreter, any write, any network, any guard marker in an argv (a grep pattern included), anything under
  `data/mf3`, any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the named
  files and the brief itself;
- quoted the list of record v2's items 1–5, verbatim; required item 3's pathspec and the `data/mf3` exclusion on every
  git command over the tree, with `.` as the include for `git ls-files`, that a glob is expanded and read before it is
  looped over, and the `rev-parse` form for a tracked-and-clean check.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (242 lines, sha256
`fd50ca98…bcad`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 103 items: 82 CONFIRMED, 7 IMPRECISE, 0 FAIL, 14 NOT CHECKABLE; and 9 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

- **The IMPRECISE items,** each applied in the checker's words or near them:
  - 11, 79 and 103: the box's 555 is the laptop's 544 plus 11 checks more, its 14 HF checks in place of the laptop's
    three skip lines, as at the BUILD; B1's pin sits inside G-CAL-n's one HF-path check, so the difference stays 11
    (T1, T2's B1 line, T3's box section);
  - 62: the review's brief named the deltas' FROM and TO files by sha256, with the `git diff --no-index -U3` form;
  - 74: F4's two texts, the docstring's "+ρ" and CONVENTIONS["arrival"]'s "+rho";
  - 78: M4 is killed by a smoke's `early_stop` asserted false in both self-tests, and by its printing no "early STOP"
    line in the driver's;
  - 102: T3 now says that no other check is added or removed, draft 5's other self-test changes extending existing
    checks.
- **The NOT CHECKABLE items** stand: Code's acts and plans (3, 8, 12, 52–56, 94, 97, 98), its reasoning on R12's
  timing (45), its own departures line (46), and the checker's departures (51). Item 48, which waited on G-VEC's run
  entry, is settled by its commit at `355e3a2`.
- **The observations:**
  - 1, applied: T1 and T3 name `89a55c3`, the BUILD, as the base, with the same bytes at every commit since.
  - 2, closed in draft 6, on the coordinating session's word: a rewrite of the baseline's call to the shared helper
    into an inline `>` or `>= 35` passed every check of draft 5, since no flow run had a baseline of exactly 36
    coherent turns. Draft 6 adds one check to `gcal.py`'s self-test, flow runs whose baseline has exactly 36 coherent
    turns (no PAUSE) and exactly 35 (a PAUSE), and nothing else: +23 −0 on draft 5, inside `_selftest`, no production
    line. Its self-test ran 545/545.
  - 3, applied: O9's precondition is named among the applied observations.
  - 4, applied: the reviewer's reads beyond its brief's files are named, for the seat to class.
  - 5, applied: the entry says that both reports were extracted from the subagents' hand-backs by `jq`, as at the
    BUILD.
  - 6 is settled: G-VEC's run entry is committed at `355e3a2`, before this commit.
  - 7, applied: O1's bullet sets §5's reason for O7 beside the STOP-first reading.
  - 8 is declared in the entry as wording owed at the driver's next change.
  - 9, applied: T3's two output lines are marked "verbatim".

## 2. The text changed after the check, and the edits checked by tool

- **The text changed after the check** by the dispositions above, and in T1 by its values-check paragraph, which
  replaces the placeholder, and by a fuller statement of the reviewer's and the checker's departures.
- **The edits, checked by tool:** a fixed-string count over each text unwrapped, for each disposition's new wording
  and each removed wording's absence: 29 of 29; then, for draft 6's changes to the texts (its hashes, digest, counts
  and observation 2's disposition), 40 of 40 (28 wordings, and 12 figures against their sources).
- **Draft 6** came after the check: tests only, on the coordinating session's word, closing observation 2. No second
  full pass was made over the texts; the claims draft 6 changed were re-checked by tool, above.
- **The finals:** the entry `16bc9eb1…45b3` (110 lines); the review raw `1e93fc22…29c0` (229 lines); the
  self-test raw `19ae7a20…dc3c` (50 lines). The code: draft 5's production lines, unchanged since the check, with
  draft 6's one self-test check (`gcal.py` `61bcafc9…14fc`).

## 3. The report as returned

G-CAL-n's delta: blind values-check of T1 (the entry), T2 (the review raw's head and §1) and T3 (the self-test raw)

Inputs, checked first:
- The brief is 77a6f3d5…a2db, 81 lines.
- Every named scratch file matches its stated sha256 and line count: T1 57c15d70…fba5 (77), T2 fbc49c08…55a9 (227), T3 bf9c25ac…c4e5 (40), S/step4b/gcal/review4_report.md cdb6cade…a3b7 (154) and S/step4b/gcal/review4_brief.md 8a0a4aed…cf4b (75). The same holds for drafts 4 and 5 of both files and for both self-test outputs. Both .exit files read "exit 0".
- HEAD is 1194982. No later commit has landed.
- Every repository file I read is tracked and clean (rev-parse HEAD:<path> against hash-object).

Shorthand:
- G5 = S/step4b/gcal/draft5/gcal.py
- D5 = S/step4b/gcal/draft5/n_sessions.py
- RB = S/step4b/gcal/review4_brief.md
- A = results/raw/2026-11-19_n-starred-twelve_design-to-code_answers.md
- R = RESULTS.md
- SU = results/raw/2026-11-19_n-starred-eleven-supplement_code-to-design_STOP.md
- VB = results/raw/2026-11-19_n-gcal-build_valuescheck.md
- BS = results/raw/2026-11-19_n-gcal-build_selftest.txt

ITEMS

T1, the entry

1. T1:1–3. The three changes and their sections, "the answers of 2026-11-19, first sitting". CONFIRMED. A:3, A:32 (§1.9), A:38 (§1.12 (d)), A:63 (§5, O7).
2. T1:3–4. "with the wording owed at the BUILD. One blind review on the delta, every finding applied in draft 5." CONFIRMED. R:95–101; A:80 (§8 item 2). The findings are items 71–77.
3. T1:4. "Nothing has run on the box." NOT CHECKABLE, an act. It agrees with T3:39.
4. T1:6. "each against `a33252a`'s (git's numstat)". CONFIRMED. Both paths have the same blob at 89a55c3, a33252a and 1194982 (gcal.py 1c0a7c74…, n_sessions.py bb2678af…). See observation 1.
5. T1:7. gcal.py `5a4c7e80…e82a` (+185 −72; 851 lines). CONFIRMED by shasum, `git diff --no-index --numstat` (185, 72) and `wc -l` (851 = 738 + 185 − 72).
6. T1:8. n_sessions.py `655430f3…d027` (+109 −36; 3624 lines). CONFIRMED the same way (109, 36; 3624 = 3551 + 109 − 36).
7. T1:9–10. The digest moves from `8f785fba…0152` to `1c22d8b5…6d04`, both by shell in package_sha256_of's form. CONFIRMED.
   - The form is from valence_core/m/resume.py:328–350: "{rel}\n{len}\n" and then the bytes, files sorted by path.
   - The 16 names came from `git ls-tree --name-only HEAD valence_core/n/` and the bytes from `git show HEAD:<path>`.
   - HEAD's bytes give 8f785fba…0152. With draft 5's gcal.py in place, they give 1c22d8b5…6d04. Hash tails were taken by `cut`.
8. T1:10–11. "Neither is printed by the package's own `hashes` until G-CAL-n's launch files are made". NOT CHECKABLE, a plan. `hashes` exists (D5:14–15), and neither self-test output prints a digest.
9. T1:11–12. Draft 4 (the bytes the review read) 542/542; draft 5 544/544. CONFIRMED by S/step4b/gcal/selftest_run4.txt and selftest_run5.txt, and both .exit files read "exit 0". RB:13–14 gives draft 4's hashes as the review's TO files.
10. T1:12 and T1:19. The two raws' names and links. CONFIRMED against the commit names in this brief (its lines 17–18).
11. T1:12–13. "On the box, by arithmetic only: 555, the 544 plus the box's 11 HF cases, restated at the launch files". IMPRECISE.
   - The sum 555 = 544 + 11 holds, but 11 is how many more checks the box runs, not how many HF cases it has.
   - On the box, hftiny.run makes 12 checks (valence_core/n/hftiny.py:71–124, two of them in the loop at :114–120). The laptop prints one skip line for it instead (:55–57).
   - The backend-ext HF case (D5:1521–1534) and G-CAL-n's HF path (D5:3498–3523) are one line at either site.
   - So the box runs 14 HF checks where the laptop prints 3 skip lines. BS:54–56 words the BUILD's count this way.
   - Instead: "On the box, by arithmetic only: 555, the 544 plus the box's 11 checks more (its 14 HF checks in place of the laptop's three skip lines, as at the BUILD), restated at the launch files;"
12. T1:14–15. Nothing ran on a checkpoint's weights; the runs were in battery windows granted for their bytes, model-free, under `nice -n 19`. NOT CHECKABLE, acts. It agrees with T3:13–22.
13. T1:16–17. 0 BUG; 7 findings (2 RISK, 5 NIT); 5 mutants; 3 box risks; 9 observations. CONFIRMED. T2:82, :90–119, :123–147, :153–167, :171–214.
14. T1:17–18. "Every finding is applied, each mutant meets a check, B1's pin is added, O3 and O7 are applied, and O1, O2 and O5 go to the seat below." CONFIRMED by the draft 4→5 diffs (items 71–89). O1, O2 and O5 are at T1:49–55. See observations 2 and 3.
15. T1:21. `STEER_FROM = 0`. CONFIRMED. G5:139.
16. T1:21–23. Steering runs from the user turn's first token, position 0, through the last generated token, in `generate` and the steering check alike. CONFIRMED.
   - G5:212 and G5:231 both place the injection from STEER_FROM through `placed` (G5:193–195).
   - `placed` uses PositionSpec.from_index, which covers every p ≥ start (valence_core/adapters/base.py:65–66, :76–77).
   - Each step forwards the whole sequence so far (G5:216–222). The self-test pins this at G5:631–636.
17. T1:22. "(the (v) render adds no special token)". CONFIRMED.
   - valence_core/n/ids.py:549 encodes the user turn and the whole text with the encoder it is given.
   - cmd_render_ids_v gives it `enc` (D5:2883–2885), which is the add_special_tokens=False call (D5:417–421).
   - ids.py:550–557 requires the whole text's ids to begin with the user turn's.
18. T1:23–24. The record's `constants.first_steered_position`, and CONVENTIONS["steering"]. CONFIRMED. G5:480 and :162–163, pinned at G5:828.
19. T1:25–27. The batches run in GENERATION_ORDER, and each batch is scored as soon as it is generated. CONFIRMED. G5:136, :383, :403–404, pinned at G5:690–697.
20. T1:27. "+ρ's two hurdles are evaluated, once." CONFIRMED. G5:406–408 (`len(turns) == 2`) and :422–423 (that evaluation is reused), pinned at G5:718.
21. T1:27–30. A coherence or arrival fail is a STOP (exit 2), with the quoted line, the record, turns and dose map written, and no +ρ/2 or −ρ turn. CONFIRMED.
   - G5:330: a batch passes only if both hurdles pass. G5:409–413 breaks the loop, and :433 sets the status.
   - D5:2814 writes the outputs. T1 quotes the first clause of D5:2832–2833. D5:2837 returns 2.
   - Pinned at G5:711–721 and D5:3245–3252.
22. T1:30. "Otherwise all four batches are generated and the status is as built." CONFIRMED. G5:433, :336–340.
23. T1:30–31. The record keeps n:113's order, records `early_stop`, and `constants.generation_order` names the order run. CONFIRMED.
   - G5:414 and :445–447 follow BATCHES' order (G5:117–118). `early_stop` is at :474 and the order at :479.
   - Pinned at G5:696, :829 and :836. The seat's own words are at A:38.
24. T1:31. "The seat's fallback (the order alone) is not needed." CONFIRMED. A:38 offers the fallback only "If Code finds the early STOP larger than the order line and the status logic", and the early STOP is built (G5:406–413).
25. T1:32–34. STOP at ±ρ; PAUSE (exit 3) at +ρ/2 alone or with fewer than 36 of 48 coherent baseline turns; PASS otherwise. CONFIRMED. G5:336–340, :120–121; D5:2838–2841. Pinned at G5:753–761 and :731–737.
26. T1:34. The baseline's `coherence_pass` comes from `coherent_enough`, the one bar. CONFIRMED. G5:311–314, :326, :330, :418.
27. T1:35–36. The driver's `gcal` docstring now says GC1–GC23 and lists the failed-run folder among its refusals. CONFIRMED. D5:155, :158. Owed at R:97–98.
28. T1:36. gcal.py's "on every PASS, STOP and PAUSE". CONFIRMED. G5:71–72 (wrapped). Owed at R:99–100.
29. T1:36–37. Departure (9) is in gcal.py's docstring. CONFIRMED. G5:90–91, in the words of R:93–94. Owed at R:101.
30. T1:37. The BUILD values-check's O3: the mid-run check's count is now pinned exactly. CONFIRMED. VB:44–45 and :212; D5:3196–3216 counts k5 from the run of record's turns and asserts `len(logged) == k5`.
31. T1:39. Departure (10), from GC23 (c)'s words "a raise after every turn is generated". CONFIRMED. SU:57 verbatim; G5:92–93.
32. T1:39–41. A non-finite score raises when its batch is scored: +ρ's and the baseline's before +ρ/2 and −ρ are generated. CONFIRMED. G5:383, :403–404, :294–295, :77–79, pinned at D5:3217–3229 (48 +ρ rows).
33. T1:41–42. GC23 (b)'s kept turns: the failed-run folder holds the log of every turn generated. CONFIRMED. SU:53–56; D5:2809–2824; G5:450–457.
34. T1:42–43. The reviewer reads (10) as sound and as required by §1.12's "as soon as a steered batch and the baseline exist" (its O6). CONFIRMED. T2:187–191; A:38 verbatim.
35. T1:44. The seam is `figures_of`, default None, with `batch_figures` looked up when called. CONFIRMED. G5:365, :376.
36. T1:44–45. The self-tests force the hurdles' pass through the seam. CONFIRMED.
   - gcal.py's self-test passes `figures_of` (G5:622–623, :637–638, :687–689, :708–709, :729–730).
   - The driver's self-test patches the module attribute that the default looks up (D5:3080, :3238).
   - The stated reason is Code's. D5:3080's comment says "the double's +rho outcome is not the test's".
37. T1:46. Production passes none, and the canned compute's keyword check pins that. CONFIRMED. D5:2811–2813; D5:3126–3132, :3148.
38. T1:46–47. `gcal.batch_figures` is patched around two runs, restored in `finally` blocks, and the restore is asserted after the last. CONFIRMED. D5:3080–3084, :3238–3242, :3248. The mid-run case is no longer patched (D5:3186–3191).
39. T1:49–51. O1 and its quotation; an incoherent baseline with a +ρ fail exits 2, and a baseline of empty turns, whose t is undefined, does the same. CONFIRMED.
   - The quotation is A:38 verbatim.
   - The early read never consults the baseline's coherence (G5:406–413), and STOP is tested before PAUSE (:336–339).
   - With fewer than two baseline scores there is no t, so arrival fails (:276–277, :323). See also T2:171–174.
40. T1:52–53. O2 and its quotation; with +ρ passing, the 48 −ρ turns are generated before the PAUSE; one condition at the early read would change that. CONFIRMED. A:38 verbatim; G5:406–413, :433; T2:176.
41. T1:54–55. O5. CONFIRMED.
   - G5:139 and :212: every steered G-CAL-n turn steers position 0.
   - valence_core/n/sessions.py:76 and :142–144: turn spans tile from position 0. Lines :88–92: S covers the cue's turns, SU all twelve. See also T2:182–185.
42. T1:56–58. R12 by the launch order, Code's call (§3): after G-CAL-n's run, as its own runner and schema delta before G-TIME-n, in one commit with F5's assertions and R13's two runner texts, with n-analyzer's fixtures and schema pin after it. CONFIRMED. A:51 ("before G-TIME-n"; "Code's call by the launch order"); A:50 (R13's "two runner texts"; F5 "asserted in the schema"); R:818–821.
43. T1:58–59. The change moves the digest, and G-CAL-n's launch files pin the digest they run under. CONFIRMED. A:51 ("it moves the package digest"); SU:76–77 ("which G-CAL-n's launch files hash").
44. T1:59. "G-CAL-n reads no fidelity monitor, so the tile changes nothing it runs". CONFIRMED by reading. gcal.py imports only adapters.base, keys, schema and sessions (G5:107–109) and reads no monitor. run_gcal calls no runner function (D5:2693–2843).
45. T1:59–61. "one runner change after its run keeps this delta to the seat's three changes, and lands the tile, F5 and R13 together, for one review and one fixture move". NOT CHECKABLE, Code's reasoning.
46. T1:63. "Code: none for this delta's texts." NOT CHECKABLE. See observation 5.
47. T1:63–64. The `jq` reads are declared in n-build's close line on `89a55c3`'s entry. CONFIRMED. R:175–176.
48. T1:64. "…and G-VEC's run entry". NOT CHECKABLE. RESULTS.md at 1194982 has G-VEC's BUILD entry (R:470) but no run entry. See observation 6.
49. T1:65–66. The reviewer's `awk` filter, an interpreter its brief barred. CONFIRMED. T2:218; RB:3, :55.
50. T1:66–68. The reviewer read the harness's saved copy of an oversized diff output, outside the scratch folder and the repository. CONFIRMED. T2:219.
51. T1:69. The values-checker's departures. NOT CHECKABLE: they are in this report.
52. T1:71–72. Committed by path. NOT CHECKABLE, a plan.
53. T1:74. A home-folder prefix count of 0 at commit time; nothing ran on a model; not pushed. NOT CHECKABLE until the commit. Today `grep -c '/Users/'` gives 0 on T1, T2, T3 and both draft 5 files.
54. T1:75–76. Next: (v)'s render under the rendering of record, then the launch files after G-VEC's PASS is committed. CONFIRMED against A:80 (§8 item 2). The "own battery window and commit" is Code's plan.
55. T1:76. "which waits for the seat's ruling on G-VEC's STOP". NOT CHECKABLE: HEAD has no G-VEC run entry and no STOP.

T2, the review raw (head and §1)

56. T2:3. PI date; Code (the n-build session). NOT CHECKABLE.
57. T2:5–7. One blind pass over draft 4: the delta from `89a55c3`'s bytes, clean at HEAD `a33252a`, to the three changes (§1.9, §1.12 (d), §5 O7). CONFIRMED. RB:1–2, :7, :10–14; T2:78. The blob ids are equal at 89a55c3 and a33252a.
58. T2:8. gcal.py from `aba3700c…a3a0` to `8a1a90cd…e98c` (800 lines), read in full. CONFIRMED by `git show HEAD:valence_core/n/gcal.py | shasum`, draft 4's shasum and `wc -l` (800). The reading in full is the brief's instruction, RB:16.
59. T2:9–10. n_sessions.py from `37b8268d…f030` to `20b30972…4665` (3621 lines), with the G-CAL-n section and self-test read in full. CONFIRMED the same way; RB:16.
60. T2:11. Draft 4's self-test had not run when the brief went out, and it ran 542/542. CONFIRMED by RB:16–17 and selftest_run4.txt. "While the review ran" cannot be checked.
61. T2:13. The brief, `8a0a4aed…cf4b`, 75 lines. CONFIRMED.
62. T2:14. "gave the two deltas in `git diff --no-index` form". IMPRECISE.
   - RB:10–15 names each delta's FROM and TO files by sha256 and tells the reviewer to take each delta itself ("Get each delta with `git diff --no-index -U3 <from> <to>`"). The brief contains no delta.
   - Instead: "gave the two deltas' FROM and TO files, by sha256, and the `git diff --no-index -U3` form;" This is the form the BUILD review raw uses at its :14.
63. T2:14–16. The brief gave the seat's answers (§1.9, §1.12, §5, §6), the owed wording and departure (9), O3, and the five code files, read only. CONFIRMED. RB:19–32.
64. T2:17–18. The brief names (10) and the seam, and asks its three questions. CONFIRMED. RB:33–38.
65. T2:19. The brief asks for findings, mutants, box risks, observations and departures. CONFIRMED. RB:40–50.
66. T2:20–22. The brief quotes the list of record v2's items 1–5 verbatim, and its bars. CONFIRMED. RB:71–75 hashes to 2373155c…c185, the same as results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md:18–22 and as this brief's copy. The bars are at RB:55–63.
67. T2:24. The report is in §2, extracted verbatim, 154 lines, `cdb6cade…a3b7`. CONFIRMED. `tail -n +74` of T2 hashes to cdb6cade…a3b7, and `cmp` finds it byte-equal to S/step4b/gcal/review4_report.md (154 lines). "By `jq`" cannot be checked.
68. T2:25. The report names scratch files only by their paths inside the scratch folder. CONFIRMED. Its only scratch names are S/step4b/gcal/draft4/gcal.py and …/n_sessions.py (T2:80). There is no "/Users/", "/private/" or "tmp/claude" anywhere in T2.
69. T2:27. The totals. CONFIRMED, as item 13.
70. T2:31–32. Draft 5's hashes and line counts, with keys.py, ids.py and guard.py at the BUILD's bytes. CONFIRMED by shasum and `wc -l`. The n package's tree is b2b1b203… at 89a55c3, a33252a and HEAD.
71. T2:34–36. F1. CONFIRMED.
   - G5:382, :406–409 and :422–423: +ρ is evaluated once and that evaluation is reused.
   - G5:703–721 asserts `es_calls == [(["+rho"] * N_TURNS, base_es, 1)]`, a failing +ρ figure, sign 1 and 48 turns.
   - M1's sign change and its two batch swaps would each change es_calls.
72. T2:37–40. F2 and its kills. CONFIRMED.
   - G5:654 checks the baseline's count against its turns.
   - G5:723–737 adds step_mute: PAUSE, four batches, no early STOP, every baseline turn empty.
   - G5:311–314, :326, :330 and :418 use the one helper, tested at 35 and 36 at :781.
   - See observation 2.
73. T2:41. F3. CONFIRMED. G5:81.
74. T2:42–43. F4: "the docstring and CONVENTIONS["arrival"] say "at every dose generated (after an early STOP, +ρ alone)"". IMPRECISE.
   - The docstring has those words (G5:57–58, wrapped). CONVENTIONS["arrival"] says "+rho alone" (G5:167–169).
   - Instead: "the docstring says "at every dose generated (after an early STOP, +ρ alone)", and CONVENTIONS["arrival"] the same with "+rho""
75. T2:44–46. F5. CONFIRMED. D5:2835–2840, :3145. "The one way" follows from G5:406–413 and :422–423: +ρ's recorded figures are the early read's, which passed.
76. T2:47. F6. CONFIRMED. D5:3506, :3511–3512.
77. T2:48–49. F7. CONFIRMED. D5:2964–2968.
78. T2:50–51. The M1–M5 dispositions, including "M4 by new assertions that a smoke's `early_stop` is false and that it prints no "early STOP" line, in both self-tests". IMPRECISE.
   - Both self-tests assert that `early_stop` is false (G5:815; D5:3157).
   - Only the driver's asserts that no "early STOP" line is printed (D5:3157). gcal.py's smoke runs with a silent `say` (G5:812).
   - The dispositions of M1, M2, M3 and M5 hold (items 71–72).
   - Instead: "M4 by new assertions that a smoke's `early_stop` is false, in both self-tests, and that it prints no "early STOP" line, in the driver's."
79. T2:52–54. B1 is folded into the existing HF check and runs on the box only, "so the box's count of HF cases stays 11". IMPRECISE.
   - The pin does sit inside G-CAL-n's one HF check (D5:3507, :3516), which is a skip line elsewhere (D5:3523).
   - But the box runs 14 HF checks (item 11). What stays at 11 is the difference.
   - Instead: "It is folded into G-CAL-n's existing HF check (one line at either site, a skip on the laptop), so the box's count stays 11 above the laptop's; it runs on the box only."
80. T2:55–56. B2 asks for nothing. B3: `sample` refuses a non-finite step, so it ends as a failure with its turns kept. CONFIRMED. T2:158–167; G5:187–188; D5:2817–2824.
81. T2:57–58. O1 and O2 go to the seat as readings, with A:38's words. CONFIRMED. T1:49–53; A:38.
82. T2:59–60. O3 is applied, with the §1.12 quotation, and an early STOP's record is tested. CONFIRMED. G5:479, :834–838; A:38 verbatim.
83. T2:61. O4 stands: no `n-gcal-v1` record exists yet, and the fields it names are new in this delta. CONFIRMED.
   - RECORD_SCHEMA "n-gcal-v1" is at G5:112 and at :102 in HEAD's file.
   - HEAD's gcal.py has no "early_stop" or "first_steered_position". Its four uses of `coherence_pass` are all for steered batches, none for the baseline.
   - No tracked file exists under data/n/gcal/.
84. T2:62–63. O5 goes to the seat. CONFIRMED. T1:54–55.
85. T2:64. O6, declared in the entry. CONFIRMED. T1:39–43.
86. T2:65–66. O7 is applied. CONFIRMED. D5:3248; D5:3186–3191.
87. T2:67. O8 confirms the owed wording. CONFIRMED. T2:202–207.
88. T2:67–69. O9. CONFIRMED.
   - D5:3377 and :3392 add the precondition. turns1 is the run of record's turns file, with +ρ's index 0 first (G5:445–447).
   - D5:3228 asserts the 48 rows. A turn with no emitted id is never forwarded (G5:288–289), so it cannot raise.
89. T2:70. The reviewer's departures are in the entry. CONFIRMED. T1:65–68.

T3, the self-test raw

90. T3:1–2. The three changes and their sections. CONFIRMED. A:32, :38, :63. The date and the session cannot be checked.
91. T3:4–6. The delta is on 89a55c3's versions, the same bytes at a33252a, with the two hashes and numstats. CONFIRMED, as items 4–6. See observation 1.
92. T3:7–10. The two digests in full, the first "89a55c3's, unchanged at a33252a", both by shell. CONFIRMED, as item 7. The package's tree id is the same at both commits.
93. T3:10. "The self-test prints no digest". CONFIRMED. cmd_selftest prints only FAIL lines and the count (D5:234–237, :356), and both outputs are the single count line.
94. T3:10–11. `hashes` runs when the launch files are made, in a window of its own. NOT CHECKABLE, a plan.
95. T3:13–14. Model-free, as at the BUILD: the HF cases run only where torch and transformers are present, and are skipped and counted as skipped elsewhere; the schema module's cases count as one line. CONFIRMED. D5:6–9, :241–242; hftiny.py:55–57; D5:1534, :3523; BS:17–19.
96. T3:15. The BUILD's overlay: 161 files, a git archive of 1185e15 on G-VEC's BUILD self-test paths. CONFIRMED. BS:20–22.
97. T3:15–16. "with the BUILD's keys.py, ids.py and guard.py and each run's two drafts in place". NOT CHECKABLE, the overlay's state.
98. T3:17–22. The command, the windows, the re-hash and the empty temporary folder. NOT CHECKABLE, acts. The command is the same as BS:23–26.
99. T3:24–28. Run 4. CONFIRMED.
   - The shasums, the line counts (800 and 3621) and "exit 0" all match. The output is one line, sha256 49901248…8c10.
   - T3:28 is that line verbatim: `grep -x -F` finds it at :28, and :28 with its newline hashes to 49901248…8c10.
100. T3:30–34. Run 5. CONFIRMED the same way: 150f718f…2ec5, and T3:34 is the output line verbatim.
101. T3:35–36. Draft 5 adds two checks to draft 4's 542, both in gcal.py's own self-test: O7's PAUSE in the flow (F2) and an early STOP's record (O3). CONFIRMED.
   - The draft 4→5 diffs add two `chk(` calls, at G5:731–737 and :834–838. Both are unconditional in `_selftest`.
   - The driver's diff adds or removes none. Lines with `chk(` go from 36 to 38 in gcal.py and stay at 147 in n_sessions.py.
   - 542 + 2 = 544, which is run 5's count.
102. T3:36–37. "every other change of draft 5 is inside an existing check." IMPRECISE.
   - Draft 5's production changes (coherent_enough, early_fig, the order filter in `write`, the STOP and PAUSE lines, the docstrings) are not in any check.
   - Its new self-test scaffolding (fail_rec, step_mute, out_es) sits outside the checks it feeds.
   - Instead: "no other check is added or removed: draft 5's other self-test changes extend existing checks."
103. T3:39–40. The box's 555, "the 544 plus the box's 11 HF cases (…the count of HF cases stays 11)". IMPRECISE, for the reason in item 11. That B1's pin is inside G-CAL-n's HF check holds (D5:3516).
   - Instead: "2. THE BOX, by arithmetic only: 555, the 544 plus the box's 11 checks more (its 14 HF checks in place of the laptop's three skip lines, as at the BUILD; B1's pin is inside G-CAL-n's one HF-path check, a skip on the laptop and a check on the box, so the difference stays 11); restated at G-CAL-n's launch files, where the box runs it."

TOTALS: 103 items.
- 82 CONFIRMED.
- 7 IMPRECISE: items 11, 62, 74, 78, 79, 102 and 103.
- 0 FAIL.
- 14 NOT CHECKABLE: items 3, 8, 12, 45, 46, 48, 51, 52, 53, 55, 56, 94, 97 and 98.

OBSERVATIONS

1. Which commit the diff is against.
   - T1:6 names a33252a, and T3:4 and :8 name 89a55c3 and a33252a. HEAD is 1194982, which will be this commit's parent unless another lands first.
   - The BUILD entry named its parent (R:30), as the BUILD values-check's O4 asked (VB:213).
   - The bytes are the same at all three commits, so only the naming changes. Suggested:
     - T1:6: "each against `1194982`'s (git's numstat; the same bytes at `89a55c3` and `a33252a`)"
     - T3:4: "on 1194982's versions of these paths (each the same bytes at 89a55c3 and a33252a)"
     - T3:8: "(89a55c3's, unchanged at a33252a and 1194982)"
2. A moved copy of M3 survives.
   - The shared helper fixes the bar wherever it is called. But replacing the call at G5:418 with `bk > COHERENT_MIN` passes every check unless some run's baseline has exactly 36 coherent turns.
   - G5:655 restates the bar with `>=`, which agrees with `>` everywhere except at 36, and the mute run's baseline has 0.
   - The same edit at G5:326 or :330 is killed by k36 (G5:774–784).
   - T2:40's "kills M2, M3 and M5" holds for M3 as the reviewer stated it. A compute run whose baseline has exactly 36 coherent turns would also kill the moved copy.
3. T1:17–18 names O3 and O7 as applied, but draft 5 also applies O9's precondition (`turns1[0]["n_tok"] > 0`, D5:3392; T2:67–68). Suggested: "O3, O7 and O9's precondition are applied".
4. The reviewer lists four reads beyond its brief's named files as "not departures under the rules" (T2:221–225).
   - The seat's §6 counts "reads beyond their briefs' lists" among the inert departures (A:68).
   - The BUILD entry put its own reviewer's reads outside the list to the seat (R:117–120).
   - T1:65–68 could name these four "as its report states them, for the seat to class".
5. T1:63 says Code has no departure for this delta's texts, while T2:24 records that the report was extracted "from the subagent's hand-back by `jq`".
   - The BUILD entry treated the same step as no departure (results/raw/2026-11-19_n-gcal-build_review.md:25; R:113–135).
   - §6 does name "Code's transcript reads by `jq`" (A:68). If the hand-back was read from this session's transcript, T1:63 may need to say so.
6. T1:64 and T1:76 rely on G-VEC's run entry and its STOP. Neither is in RESULTS.md at HEAD 1194982, which has only G-VEC's BUILD entry (R:470). If this entry lands first, both references point at nothing committed.
7. T1:49–51 (O1) gives only the STOP-first reading. The reviewer also cited §5's "neither hurdle can be read" against an incoherent baseline (T2:174; A:63), which argues the other way. The seat may want both texts in front of it.
8. F5 moved the STOP and PAUSE lines to name the dose map, but three texts still say "its record and turns": run_gcal's docstring (D5:2700–2701), the gcal command's docstring (D5:170–171) and the exits check's name (D5:3142–3143). This is wording for a later change, not a defect.
9. T3:28 and :34 show each output line at its own two-space indent, below lines indented five. The BUILD raw indented its output and said so (BS:33–35). This is cosmetic: "output 1 line, sha256 …, verbatim:" would tell the reader the line is the file's.

DEPARTURES

1. Two `sed -e "s#<the scratch path>#S#g"` filters over `git diff --no-index` output, to print S/ in place of the scratch folder's path. sed is not among the interpreters the brief names, but it does run a script. Stated for the seat to class.
2. One `git log -1 --format='%H %s' HEAD` without item 3's pathspec. It printed only an id and a subject, which item 1 permits over any path. I read it as not over the tree.

Not departures under the rules, stated for completeness:
- Reads beyond the brief's named sources, each checked clean at HEAD:
  - valence_core/n/hftiny.py, read and grepped;
  - results/raw/2026-11-19_n-gcal-build_selftest.txt;
  - the head of results/raw/2026-11-19_n-gcal-build_review.md;
  - two passages of results/raw/2026-11-19_n-close-lines-twelve_valuescheck.md;
  - lines 18–22 of results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md, hashed;
  - RESULTS.md beyond the BUILD entry and its close line: the supplement entry and its close line, the close line on 003ae7d's entry with part of the entry after it, and greps for "G-CAL-n's BUILD", "G-VEC" and "R12".
- One `git grep -l -F` and one `git ls-files`, each with item 3's pathspec and the mf3 exclusion.
- One redirect to the shell's own standard output.
- One zsh error from an unquoted `===`, which ran nothing.

Otherwise I wrote nothing, used no network, and ran no interpreter but shasum (and the sed above). No guard marker was in any argv or pattern. Nothing under data/*/ckpt, data/*/reports or data/mf3 was read, listed, sized or timed, and nothing in S was listed, searched with find or globbed.
