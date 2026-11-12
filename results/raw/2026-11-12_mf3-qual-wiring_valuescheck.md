# The `qual` wiring (G-F3): the values-check of its entry, review raw and self-test raw

*Code's raw, PI date 2026-11-12.*
- *What was checked:* the drafts of the wiring's entry, its review raw and its self-test raw, before the commit. They
  were checked against the edit (the working tree's driver, `285eed04…0e44`, and HEAD's), the self-test output, the
  routing, the lock, m's code and the stage library's, and the review's materials.
- *How:* one blind agent, read-only, under a brief quoting the list of record v2's items 1–5 as written. It ran no
  model and no run of the driver.
- *Outcome:* 101 items: 82 CONFIRMED, 7 IMPRECISE, 5 FAIL, 7 NOT CHECKABLE. HEAD was `a225a89` at its start and at
  its end.
  - Every FAIL and IMPRECISE item is applied (below).
- *Not run:* a second pass. Each change applies the checker's own fix or corrects a claim the checker showed false.
  Where a change carries a figure, Code took it by tool:
  - the final blob's PIN anchors, by grep;
  - the report's digest and line count, by script;
  - the commit range, by `git diff --name-only` (data/ outside data/p by a count only);
  - the transcript scans' counts, by script.
- *Code's masked scan of the checker's transcript* (no output text printed but counts):
  - 125 distinct Bash commands, over every row of the transcript (50 of them held only in its request-blob rows).
  - None names a `ckpt` or `reports` path, and none of its other tool calls names data/ or a barred path.
  - Two name data/: its two name-only diffs, each piped to a count (its disclosure 1).
  - Its two `git status --porcelain` runs in the main checkout (item 1's form), at its start and at its end, printed
    no name under data/.
  - It opened nothing under the tasks directory and none of the three scratch subdirectories the brief barred.
- *This raw:* Code's dispositions, then the report verbatim, but for one reworded list (below).
  - The report was extracted by script from the agent's hand-back (the text's sha256 `19c925e5…`; the text has no
    final newline; 198 lines).
  - It holds no local path and no clock time. Its item 100 listed the generic path words its leak scan searched
    for; Code reworded those words in square brackets before the commit. That is the one change to the
    report, and the digest above is of the hand-back's text before it.
- *Nothing ran on a model.*

## Code's dispositions

- **73, FAIL: the review report's digest.** Agreed. `a9714872…` is the digest of the text with its final newline;
  the review raw now says so.
- **74, FAIL: "188 lines".** Agreed: 187. The extraction script counted the empty piece after the final newline.
- **85, FAIL: NOTE-7's "does not break the self-test".** Agreed, on reading the variants (`.replace(…, 1)`).
  - The review raw's disposition now says NOTE-7 is applied in part. It names the gap and records it for the campaign
    wiring, the next driver edit. The entry says so too.
  - Not fixed now, for three reasons:
    - the failure would be loud, a FAIL, never a false PASS;
    - no committed lock restates the line;
    - a driver change now would re-open the review and this check before G-F3.
- **87, FAIL: the commit range.** Agreed: `a225a89` also added four `results/raw/2026-11-11_p-qual*` files.
  Corrected. Code confirmed that nothing else changed, data/ outside data/p by a count of names (0).
- **90, FAIL: "two production texts".** Agreed. Since round 1, only the `id` precheck's PIN changed in production
  code; the WIRED_CMDS sentence was already revised in the candidate. Corrected. The scope line now also names
  NOTE-7's relaxed assertion, and the identity-check kills' other conjuncts (item 91).
- **13, IMPRECISE: the launch order.** Applied: "in §2.4's table order; the stage launches them in its own rotation
  (`schedule.gate_launch_order`)".
- **28 and 82, IMPRECISE: the anchors.** Applied. The review raw's NOTE-5 disposition gives the final blob's anchors,
  by grep, and the entry points to them.
- **31, IMPRECISE: "The rest of `time` and `id` is unchanged".** Applied, in the checker's terms: the PIN texts, and
  what the two do, print and refuse, are unchanged; the shared lines become stage-keyed; `_selftest_id`'s not-wired
  case uses `campaign`.
- **44, IMPRECISE: the stub heading.** Applied: "On the stub, at a test root", with the runs after time and a FAILed
  id named apart from the STOP cases.
- **45, IMPRECISE: "time's others".** Applied. The 35 cases are `id`'s 33, less its four for an existing artifact,
  plus the earlier blob and five for G-ID-F3's artifact.
- **52, IMPRECISE: the NOTEs.** Applied: the applied, recorded and unchanged NOTEs are listed apart.
- **26's note: the subparser.** Applied: the entry says `qual`'s subparser comes from `main`'s loop over
  `WIRED_CMDS`.
- **70, NOT CHECKABLE, with a question.** Code re-scanned the reviewer's transcript.
  - The "pruned `find`" ran inside the clone's set-up call, beside the sparse-checkout patterns. So two calls name a
    `ckpt` or `reports` path, not three. The review raw now names it.
  - The re-scan also showed what the raw's "93 distinct Bash calls" counted: distinct command texts over every row of
    the transcript, 16 of them held only in its request-blob rows. The raw now says "commands".
- **69, NOT CHECKABLE.** Code checked the round-2 clone's HEAD by `git rev-parse`: `a225a89`.
- **67 and 72, NOT CHECKABLE.** Code's own runs.
- **7, 35 and 55, NOT CHECKABLE.** Placeholders and a future record: the placeholders are filled at the commit.
- **The checker's disclosures.**
  - (1) Two `git diff --name-only 05ef75d a225a89` commands limited to data/ pathspecs, each piped to a line count,
    each printing a number only. They are item 1's names-only form, and a departure from this brief's narrower "list
    nothing under data/". Code ran the same form once, for data/ outside data/p, as a count only (0), to confirm
    item 87.
  - (2) Its own tool output showed fragments of the per-user temp-dir id, where one of its masks missed truncated
    path heads in the unscrubbed self-test output. None of it is in the report.

## The checker's report (verbatim; item 100's list reworded, as above)

# Values-check: the `qual` wiring's drafts (entry, review raw, self-test raw)

HEAD at start: `a225a89`. HEAD at end: `a225a89`. The working-tree driver's sha256 was `285eed04…0e44` at both points.

"Q" below means Code's scratch directory for this task. Line numbers: "driver :N" is the working tree's `scripts/mf3_sessions.py`; "HEAD :N" is `git show HEAD:scripts/mf3_sessions.py`; "raw :N" is `Q/review_raw_full.md`; "st :N" is the scrubbed self-test raw `Q/2026-11-12_mf3-qual-wiring_selftest.txt`.

## A. The entry (`Q/entry_qual.md`)

1. :1–2, "qual (G-F3, m:297) is wired … under LOCK-m-F3 v0.2, in scripts/m_sessions.py's forms": **CONFIRMED.** The PINs at driver :154, :306, :432 and :638 carry m's QUAL_*, stage_identity_extra, stage_precheck and _run_stage forms. m:297 is G-F3.
2. :2, "an edit of F-1's kind": **CONFIRMED.**
   - F-1 is at `results/raw/2026-11-06_ganl-f3_design-to-code_answers.md:24` ("an edit that wires a subcommand at its step, touching no scoring-stack function, does not re-run G-SHAPE-F3").
   - The same form is used at RESULTS.md:321 (id) and :3255–3257 (time).
   - Note: the edit also changes id's shared lines and id's self-test. That counts as wiring on Code's reading, as at the id wiring.
3. :2–3, the blob moves `8d878f4a…00e7` → `285eed04…0e44`: **CONFIRMED.** These are the sha256 of HEAD's and the working tree's file. `git status --porcelain` shows no other tracked change.
4. :3–4, the package, m's, the analyzer and the lock stand; G-SHAPE-F3 is not re-run: **CONFIRMED.** No other tracked file is modified, and LOCK-m-F3.md's working tree equals HEAD (`ac82b943…`).
5. :4, "214/214": **CONFIRMED.** `Q/selftest_q3.txt` has 214 PASS lines and 0 FAIL.
6. :4–5, 44 mutants, no MAJOR, the MINOR and four NOTEs applied: **CONFIRMED.**
   - Report: raw :85–147. `Q/review/mutants/index.tsv` has 44 rows.
   - NOTE-2, -3, -4 and -7 are in the final bytes at :2335, :2350–2360, :443–444 and :2325.
7. :6, `@@STAMP@@`: **NOT CHECKABLE** (placeholder).
8. :7–8, the routing (§5 and §9 item 5; PI 2026-11-11, "Route as given"; close line at `a6c6297`): **CONFIRMED.** The close line ("PI date 2026-11-11") is at RESULTS.md:287–309, inside the G-ID-F3 entry that opens at :198. `git show a6c6297 -- RESULTS.md` added it, with the PI's "Route as given".
9. :8–9, the item 5 quote: **CONFIRMED** verbatim. Sources: answers file :67, LOCK-m-F3.md:13 and the close line. The final period is outside the quote.
10. :9, "LOCK-m-F3 v0.2 (`05ef75d`), §9 item 1": **CONFIRMED** (LOCK :263–268; `05ef75d` is v0.2's commit).
11. :11, run_gate_stage with gate "qual", unchanged: **CONFIRMED** (driver :723–725; stages.py:967; valence_core is unmodified).
12. :11–12, the counts: 8×A1s, A2s, A3s (24 sham); 8×A3, 4×A1, 4×A2 (16 contrast): **CONFIRMED** (driver :169; m:297).
13. :12–13, "These are the committed qual schedules' counts, in the stage's launch order.": **IMPRECISE.**
    - QUAL_COUNTS is in §2.4's table order (keys.TEMPLATES). run_gate_stage checks it in that order against the committed files' n (stages.py:982–984).
    - The launch order is the stage's own rotation (`schedule.gate_launch_order`, stages.py:985).
    - Fix: "…counts, in §2.4's table order; the stage launches them in its rotation."
14. :14–15, the two QUAL_LOCK_LINES at a line's start, v0.2 §2 and §3: **CONFIRMED** (driver :172, :361–366; LOCK :91, :109).
15. :16, the re-issue's and v0.1's blobs are refused, as m's qual refused LOCK-m-F0 v0.1's: **CONFIRMED.**
    - `f674583` (`70da4a70…`) and `1e79955` (`377c5d60…`) contain neither string.
    - m's PIN, scripts/m_sessions.py:946–950, says "v0.1's blob, for one -- is refused here"; the check is at :951–955.
16. :17, Code's intent declared at v0.2 §9 item 1: **CONFIRMED** (LOCK :266–268).
17. :18–19, a line-start test against m's substring test, and v0.2 writing each string once: **CONFIRMED.** The driver tests each line (:363); m tests `x not in lock_text` (m_sessions.py:952). In the committed v0.2 each string occurs exactly once, at a line's start (:91, :109).
18. :20–22, the identity is time's, and `_locked` gives PATH MISMATCH with an end pending aside: **CONFIRMED** (driver :373–377; the self-test asserts ex_q == ex_t; stages.py:688–698).
19. :23–24, the prior is taken by path and the first run's name is refused, also when resolved (v0.5 §4.3): **CONFIRMED.** The driver resolves the path through checkpoint_path, then checks the name (:409–421). The v0.5 §4.3 sentence is at ADDENDUM-m2 v0.5:77.
20. :25, require_real on in the precheck and in the stage: **CONFIRMED** (driver :494–498; stages.py:722–727, `require_real=not stub`).
21. :26–27, at "qual" the artifact must be on disk, at the cap, any verdict, under this proposal, not stub-written: **CONFIRMED** (stages.py:518–525, 435–457).
22. :28–29, the outputs `Q-F3_qual.json` and the report and reads names: **CONFIRMED** (stages.py:56, 100–111, 114–117; qual passes no ckpt_path).
23. :30, exit codes 0, 4 and 2: **CONFIRMED** (stages.py:73; gate stages end PASS or STOP; run_stage :663–729).
24. :32, WIRED_CMDS, with campaign refused: **CONFIRMED** (driver :110).
25. :33–34, the qual branches, `stage_prior_checkpoint`, and the `id_prior_checkpoint` wrapper: **CONFIRMED** (driver :361–377, :409–426, :474–475, :494, :719–725).
26. :35–37, the new names and the qual subparser: **CONFIRMED** (driver :168–173, :179–181, :742–744). Note: no subparser code was added. main's loop over WIRED_CMDS (:2863–2867) builds it; at HEAD, qual had the refused subparser.
27. :38, two texts that v0.2 §5 quotes verbatim are revised: **CONFIRMED.** These are LOCK :181 (the :92 PIN), :200–201 and :197 (the :375 PIN). Comparing each PIN paragraph, exactly these 2 of the 13 v0.2-quoted texts differ.
28. :38–39, "v1.0 … re-anchors the other sites (the review's NOTE-5, its table in the review raw)": **IMPRECISE.**
    - The table (raw :130–136) gives the reviewed candidate's lines.
    - NOTE-4's re-wrap (driver :443–444) moves every later site down one line in the final bytes:
      - time :451→:452, :528→:529, :553→:554, :649→:650;
      - id :643→:644;
      - the new PIN :637→:638.
    - Fix: give the final blob's anchors, or say v1.0 re-derives them on `285eed04…`.
29. :40–42, the WIRED_CMDS sentence, before and after: **CONFIRMED** verbatim (HEAD :98–99; driver :108–109).
30. :43–45, the id precheck PIN, before and after: **CONFIRMED** verbatim (HEAD :378; driver :443–444).
31. :46, "The rest of time and id is unchanged.": **IMPRECISE.**
    - It holds for the other v0.2-quoted PIN texts (all unchanged, the re-issue's PIN too) and for behaviour: every time and id check passes, and the reviewer's Q2 agrees.
    - It does not hold line for line. These shared lines changed:
      - `want_lock` (:333), `reasoning_cap` (:373) and `wanted` (:474) became stage-keyed dicts;
      - the precheck's prior block (:494) became shared;
      - the PRIOR PATH REFUSED text is now built with `stages.stage_name` (same output for id);
      - `else` became `elif stage == "id"` (:719);
      - run_stage's docstring, the parser description (:2853) and the "no action" line (:2892);
      - `_selftest_id`'s not-wired case moved from qual to campaign (:1744–1756).
    - Fix: "The rest of time's and id's PIN texts, and what they do, print and refuse, is unchanged; their shared lines become stage-keyed."
32. :47, "touches no scoring-stack function; every change is in the driver": **CONFIRMED.** Only the driver changed, and its changed functions are wiring or self-test functions.
33. :48, the full new blob: **CONFIRMED.**
34. :48–49, the DRIVER line prints it before the load: **CONFIRMED** (driver :694 before :697; checked by st :226).
35. :49, recorded in the G-F3 entry and at v1.0: **NOT CHECKABLE** (future). It is consistent with the PIN at driver :154–167.
36. :50, four new PIN sites declared at v1.0: **CONFIRMED** (driver :154, :306, :432, :638; HEAD has 14 sites, the final 18).
37. :51–53, NOTE-6's two commitments: **CONFIRMED** (they match raw :143 and :52–55).
38. :54, "197 → 214, 214/214 … at HEAD a225a89": **CONFIRMED.** The id raw's last line is 197/197. `Q/selftest_q3.head` reads a225a89 before and after, `.sha` reads 285eed04 before and after, and `.exit` is 0.
39. :55, the link and "local roots scrubbed": **CONFIRMED** (same form as RESULTS.md:372; see 99–100).
40. :55–56, 16 qual checks: **CONFIRMED** (st :210–229).
41. :57–62, the four lock forms: **CONFIRMED** (driver :2331–2349; st :211).
42. :63, the order: **CONFIRMED** (driver :2350–2360; st :212).
43. :64, `qual --help`: **CONFIRMED** (st :213).
44. :65–68, the stub group: **IMPRECISE** (minor).
    - The bullets are right (st :217–221).
    - The heading "after time and a FAILed id" fits the PASS, exit-code, --resume and end-pending runs. The STOP cases set up other states: PATH MISMATCH runs after a PASSed id, "no prior" has neither time nor id, and "no artifact" has time only.
    - Fix: "On the stub, at a test root:".
45. :70–71, "35 refusals … and time's others": **IMPRECISE.**
    - 35 is right (st :222; asserted at driver :2705).
    - The other cases are id's carried cases, not time's: id's 33 (st :201), minus its four artifact-EXISTS cases, plus the earlier-lock case and five artifact cases.
    - Time's own table has 36 cases (st :181), and several are not carried: the looping-link proposal or lock, the sha16-only form, the licence's (f) and (g), the known answers, the gate line, and the driver run from a copy.
    - Fix: "…an earlier lock blob, and id's others."
46. :72–78, the rest of the Qwen-path group: **CONFIRMED** (st :223–228).
47. :79, nothing loaded or written: **CONFIRMED** as asserted (st :229).
48. :80–81, id gains one check, so 197 + 16 + 1 = 214: **CONFIRMED.** The id block goes from 15 to 16 checks (st :207). The only other change in the check list is a reworded check (st :152).
49. :82–83, one blind round, the dispositions, and round 2: **CONFIRMED.**
50. :84, 0/1/7, and 39 killed, 5 survived (3 equivalent, 2 gaps): **CONFIRMED** (`Q/review/runs/summary.txt`; `survivors.tsv` lists Q12, Q13, Q20, Q35, Q36).
51. :85–86, the MINOR's two gaps are now asserted: **CONFIRMED** (driver :2189–2215, :2777–2803).
52. :87–92, "The NOTEs' applied points": **IMPRECISE.**
    - The headline (:5) says four NOTEs are applied. These five bullets cover six NOTEs: 2, 3, 4 and 7 are applied, while NOTE-5 is "Recorded" and NOTE-6 "adopted" (raw :48–55).
    - Each bullet's content is right.
    - Fix: "Applied: …; recorded: NOTE-5 for v1.0, NOTE-6 for G-F3."
53. :93, Q20 "as at the id wiring": **CONFIRMED** (id review raw :95, :97, M14).
54. :94–95, round 2's outcome: **CONFIRMED** (`Q/review2/runs/summary.txt`).
55. :96, `@@VC@@`: **NOT CHECKABLE** (placeholder).
56. :97–98, nothing ran on a model: **CONFIRMED** as far as the sources show. The commit list is future.
57. :99, "Next … waits for the ack": **CONFIRMED.** It is the id entry's form (RESULTS.md:418) and matches LOCK :271.

## B. The review raw (`Q/review_raw_full.md`)

58. :3, "PI date 2026-11-12": **CONFIRMED.**
59. :4–6, the candidate `fd5821bd…627d`, checked against `8d878f4a…00e7` at `05ef75d`: **CONFIRMED.** The file `Q/review/candidate_mf3_sessions.py` has that sha. At `05ef75d` the driver is `8d878f4a…`. The reviewer states the working tree had that digest before and after (raw :90).
60. :7–8, the brief quotes the list's items 1–5 as written: **CONFIRMED.** `Q/review/brief_review_qual.md` lines 82–86 are byte-equal to the ruling's §2 items 1–5.
61. :9, a sparse clone with ckpt and reports left out: **CONFIRMED** as reported (the brief's pattern at brief :66; report :252).
62. :10, every model import blocked: **CONFIRMED** (the harness's `run_selftest.py` blocks five modules; report :264).
63. :11, 44 one-defect mutants of the production code: **CONFIRMED** (44 files; the generator refuses replacements inside the self-test region).
64. :12–13, the outcome counts: **CONFIRMED.**
65. :14, the MINOR and four NOTEs applied: **CONFIRMED.**
66. :15, 214/214 on the final bytes: **CONFIRMED.**
67. :15, "The candidate the review read passed 211/211.": **NOT CHECKABLE.** No run of the candidate outside the harness is in the permitted sources. It is consistent with brief :18 and the reviewer's 210/211 baseline under the block.
68. :16–17, round 2's re-runs and outcome: **CONFIRMED.**
69. :16 and :61, "a fresh sparse clone at HEAD `a225a89`": **NOT CHECKABLE.** The clone is off-limits, and no run output prints its HEAD.
70. :18–22, the masked transcript scan (93 calls; the two clone-internal; no `git status` in the main checkout): **NOT CHECKABLE** (transcripts are off-limits). Consistent with report :250. One note: report :256 lists "a pruned find over data/" in the clone, and that command form names `*/ckpt` and `*/reports`. Code may confirm it is the "name-only count" the raw cites, and not a third such call.
71. :23, the structure: **CONFIRMED.**
72. :24, "extracted by script from the agent's hand-back": **NOT CHECKABLE.**
73. :24, "the text's sha256 `a9714872…`": **FAIL** under the stated definition (the text without the file's final newline).
    - The text without the final newline hashes to `2e0f9bab…`.
    - `a9714872…` is the hash of `Q/review_report_verbatim.md` including its final newline.
    - Fix: give `2e0f9bab…`, or say the digest includes the final newline.
74. :24, "188 lines": **FAIL.** The report has 187 lines: the verbatim file's `wc -l` is 187, and the raw's verbatim part is :83–269. 188 is the number of pieces when split on newlines, counting the empty piece after the final newline.
75. :25, no local path and no clock time: **CONFIRMED** (scanned; only durations appear).
76. :26, nothing ran on a model: **CONFIRMED.**
77. :30–36, MINOR-1's disposition: **CONFIRMED** (driver :2189–2215, :2777–2803; time's cases at :1605–1611).
78. :37–38, NOTE-1's disposition: **CONFIRMED** (schedule.py:326–352; id review raw :95).
79. :39–40, NOTE-2's disposition: **CONFIRMED** (driver :2335, :2338).
80. :41–44, NOTE-3's disposition: **CONFIRMED** (driver :2350–2360).
81. :45–47, NOTE-4's disposition: **CONFIRMED** (driver :443–444; LOCK :197).
82. :48–51, NOTE-5's disposition, "with the reviewer's table": **IMPRECISE.** Six of the table's anchors are stale on the final blob (see item 28).
83. :52–55, NOTE-6's disposition: **CONFIRMED.** The checkpoint does not bind the driver: `stages._identity` (:700–709) and `LICENCE_KEYS` (:526) carry no driver blob.
84. :56–57, NOTE-7's "one or more" assertion: **CONFIRMED** (driver :2325).
85. :56–57, "so a v1.0 that restates them does not break the self-test": **FAIL.**
    - The "moved" and "indented" variants (driver :2334–2335) use `.replace(QUAL_LOCK_LINES[1], …, 1)`, which changes only the path line's first occurrence.
    - Suppose v1.0, placed above v0.2, restates the path line, or even quotes its exact text. The replacement then hits v1.0's occurrence, and v0.2's :109 line still opens a line.
    - qual would accept both variants, and the check at :2341–2349 would fail. This is by reading; I did not run it.
    - Only the identity check's count is fixed. A restated cap line is safe, because "dropped" removes every occurrence.
86. :61, the reviewer's harness with its work directory moved and model imports blocked: **CONFIRMED.** `diff -r` shows only the `W=` line differs, in four `.sh` files.
87. :61–62, "(RESULTS.md and data/p only since `05ef75d`)": **FAIL.** `a225a89` also added four `results/raw/2026-11-11_p-qual*` files. Nothing under scripts/, valence_core/, LOCK-m-F3.md or data/ outside data/p changed.
88. :62–63, all 44 mutants regenerated unchanged on `285eed04…`, every anchor matched: **CONFIRMED.**
    - The generator file is identical between rounds.
    - The index rows match by name, mode and description.
    - Each mutant is one replacement of the final candidate, and the sha12s match.
    - The generator writes nothing unless each anchor occurs exactly once.
89. :64, scope (the five survivors; 39 not re-run): **CONFIRMED.**
90. :64–65, "change two production texts, a PIN's and the WIRED_CMDS sentence's": **FAIL.**
    - Since round 1, only one production text changed: the id precheck PIN (candidate :443 → final :443–444).
    - The WIRED_CMDS sentence was already revised in the reviewed candidate (:108, quoted by the reviewer as the candidate's).
    - The edits also relaxed one assertion (NOTE-7's count, :2325).
91. :65–66, none weakens an assertion those kills rest on: **CONFIRMED** by reading. The identity-check kills (Q03, Q06a, Q08a, Q15, Q31) fail on other conjuncts.
92. :67–68, baseline 213/214, the constants FAIL, and the "Killed" definition: **CONFIRMED** (`Q/review2/runs/BASE.txt`).
93. :70–76, the five table rows: **CONFIRMED.** Round-2 counts match `summary.txt`. The FAIL lines are the post-load check plus the final audit (Q35, Q36), the lock-line check (Q12) and the order check (Q13); Q20 is at baseline.
94. :78–79, the blocks held and the clone changed only in its driver: **CONFIRMED.** Six "BLOCKED STILL NONE: True" lines, and six status files show only the driver modified.
95. :81–269, the verbatim part is intact: **CONFIRMED** (byte-identical to `Q/review_report_verbatim.md`).

## C. The self-test raw

96. The header's driver sha256: **CONFIRMED.**
97. "main checkout on HEAD a225a89, edit applied, uncommitted at the run": **CONFIRMED** (`.head`, `.sha`; the INVOCATION interpreter path).
98. "exit status 0": **CONFIRMED.**
99. "Local roots scrubbed (<repo>, <tmp>); otherwise unchanged": **CONFIRMED.**
    - Exactly 6 body lines differ from `Q/selftest_q3.txt` (original lines 1, 130, 131, 134, 172, 173).
    - Each differs only where a local root, whole or truncated by the self-test's cut, became `<repo>` (once) or `<tmp>` (7 times). There is no `<home>`.
100. No local path, user name, session id or temp-dir id survives: **CONFIRMED.** I scanned for the home directory, the user name, [the users root, the private root, the temp-folders root and a fragment of it], the claude temp root, the session-id prefix, [the repository's parent folders, the temp root's last component], and every 6-character run of the per-user temp-dir id. Observation: three Python tempfile directory names (`tmp` + 8 characters) remain after `<tmp>`, as in the committed id raw.
101. The last line, "  214/214 mf3 selftest checks pass", ends with one newline and equals the original's: **CONFIRMED.**

## Tally

101 items: 82 CONFIRMED, 7 IMPRECISE, 5 FAIL, 7 NOT CHECKABLE.

**Not CONFIRMED:**
- **FAIL:**
  - 73: the sha prefix (`2e0f9bab…` without the final newline);
  - 74: "188 lines" (it is 187);
  - 85: NOTE-7's "does not break the self-test";
  - 87: "RESULTS.md and data/p only";
  - 90: "two production texts".
- **IMPRECISE:**
  - 13: "in the stage's launch order";
  - 28 and 82: the NOTE-5 table's anchors;
  - 31: "The rest of time and id is unchanged";
  - 44: the stub heading;
  - 45: "time's others";
  - 52: the NOTEs' applied points versus "four".
- **NOT CHECKABLE:**
  - 7 and 55: placeholders;
  - 35: a future record;
  - 67: the candidate's 211/211;
  - 69: the round-2 clone at a225a89;
  - 70: the transcript scan;
  - 72: extraction by script.

## Disclosures

- To check item 87, I ran two `git diff --name-only 05ef75d a225a89` commands limited to data/ pathspecs (data outside data/p, and data/p), each piped to a line count. Each printed a single number and nothing else. They are name-only forms under the list's item 1, but they depart from this task's "list nothing under data/".
- My own tool output (not this report) showed fragments of the per-user temp-dir id when one mask missed the truncated path heads in `Q/selftest_q3.txt`.
- Nothing was written, staged or committed, and no model or `scripts/mf3_sessions.py` run happened. The forbidden Q subdirectories, the transcripts and the tasks directory were not opened.
