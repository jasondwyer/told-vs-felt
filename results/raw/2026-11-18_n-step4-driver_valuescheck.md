# n step 4 — the BACKEND extension's driver commit: the blind values-check, as returned, with every disposition

PI date 2026-11-18. Code (the n-build session).

**What was checked.** One blind pass by a subagent over four drafts:
- T1, the driver's entry, sha256 `44eadf84…5ab6`;
- T2, n-build's close line on `0eb7671`'s entry, `90d68861…b351`;
- T3, the self-test raw, `b20a5a4e…4b4c`;
- T4, the Code-written parts of the two review raws: the first's header (`e4c5b368…3a27`, lines 1–31) and the
  second's header and its O3 (`a5295b59…7d7d`, lines 1–20 and 70–72). The reviewers' reports inside them are records
  and were sources, not checked.

**The checker's brief:**
- named the sources:
  - the seat's answers of the second sitting and the STOP of `0eb7671`;
  - the box raws of 2026-11-18 and the A100 check's raws;
  - the box, corpus and 2026-11-16 answers, and the respawn raw;
  - PROPOSAL-n v0.2, ADDENDUM-n1 and RESULTS.md;
  - the driver at HEAD and the draft, the n package, the self-test outputs, the review raws and the box script v2;
  - the package digest rule;
- said what is not in the tree: the PI's word and the coordinating session's window grants, as relayed;
- quoted the list of record v2's items 1–5, verbatim;
- carried the seat's line of 2026-11-18 (second sitting, §4): a git command in a check takes item 3's pathspec;
- barred any interpreter, any guard marker in an argv, anything under `data/mf3`, any write but one scratch file,
  and any opening of the smoke's report or root.

**The report** is in §3 below, extracted verbatim from the subagent's hand-back by `jq` (390 lines, sha256
`7afb202c…4c68`). It writes `R/…` for the repository and `S/…` for Code's scratch. HEAD moved from `dc6a1cf` to
`25c9340` during the check (its observation 1): the coordinating session's dated note and its close line on the box
entry. Neither touches the driver, the package or `0eb7671`'s entry.

**Totals:** 70 items — 52 CONFIRMED, 11 IMPRECISE, 2 FAIL, 5 NOT CHECKABLE — and 13 observations.

**The checker's departures,** as its report's DEPARTURES section states them. All were model-free. No guard marker
was in any argv, and nothing under `data/mf3`, `data/*/ckpt` or `data/*/reports` was listed or read.
- Two scratch files it wrote by redirection for a `cmp`, then removed, beyond the one the brief allowed.
- Path-taking git commands without item 3's pathspec, each scoped to paths outside `data/` and printing names, but
  for one `git grep -l` over `results/raw`. For the seat to class.
- Two recursive greps over `results/raw`, which holds no `ckpt` or `reports` folder, without the prune. For the seat
  to class.

## 1. Dispositions

**The two FAILs, applied: one miscount in two places.** The first review's surviving mutants are 12, not 11: the
report marks M1, M3, M4 and M7–M15 as surviving, and Code's own list there kills M2, M5 and M6 by existing checks and
gives the 12 survivors their tests. Code re-counted by tool: 12 lines of the report read "SURVIVES".
- **10** (T1): "with 15 mutants, 12 surviving its reading".
- **60** (T4, the first review's header): "and 15 mutants, of which 12 survived by its reading".

**The IMPRECISE items, all applied:**
- **4** (T1): "PROPOSAL-n v0.2 §3 G-ACQ and G-ACQ's dated note GA-5".
- **6** (T1). "Unchanged to HEAD `dc6a1cf`" is now "which no commit since has changed", so the sentence cannot go
  stale. The commit's gate checks HEAD's driver blob against `b523f6a`'s.
- **9** (T1): the quote "The smoke passed for the commit's purpose" is cited to §0, where it stands.
- **11** (T1): "The first, of v1's first draft (`80d30846…b03d`) on 2026-11-16".
- **20** (T1). The 40-of-40 rule is taken out of the list of conventions §5.5 leaves open, and stated after it as
  "§5.5 keeps the rule".
- **23** (T1): "the largest per-label |logprob − fresh_logprob| over the 24 reads (one maximum over both labels)".
- **25** (T1): "(GA-4; rule 28(d)(c))".
- **27** (T1). N.9's scope is now quoted, and the extension is marked as Code's reading: "The run proceeds on them as
  the BUILD's flags do: Code reads the PI's routing of 2026-11-16, N.9, "the build proceeds on Code's interim
  readings as its entries have it", as covering the driver's."
- **29** (T1): "later n stages need the same bridge (that both identifiers stand in the record is the box answers' §2
  item 4)".
- **55** (T4, the first review's header): "the BACKEND extension on the box, then ADDENDUM-n1 §2's label-convention
  comparison in the same session, here in one invocation".
- **64** (T4, the second review's header): "the step-4 driver as frozen after the first review (which read its first
  draft, `80d30846…b03d`), and box-tested on 2026-11-16".

**The NOT CHECKABLE items** (33, 37, 47, 59, 66) are Code's own disclosures, process and briefs, and the commit to
come. They stand as declared. No change.

**The observations:**
1. No text change beyond item 6. The rebuild finds both anchors by text on HEAD `25c9340`.
2. No text change. Noted for Code's gates: on this git, `git ls-files` with a directory path and an exclude pathspec
   prints nothing. No gate of this commit uses that form, and the diagnostic's own tracked-check names its path
   alone.
3. Applied with item 23: "The smoke's two reads differ between the paths and the run of record's plan begins with
   them, so if the box repeats them the bound is not 0".
4. Applied: "nothing of this driver ran on a checkpoint's weights before this commit".
5. Applied: "Every finding is applied, two of them as declared readings (the first review's 3 and 9)".
6. No change. The first review's M13 has its test in Code's list: the flow test's bridge refusals.
7. Applied: T2 cites the quote to §0.
8. Applied: T2 reads "The PI's word on the paste block of 2026-11-18 (second sitting) was "Route as given", as the
   coordinating session's close line at `25c9340` quotes it".
9. Applied: the second review's O3 now reads "The reviewer read the H100 smoke as R6's first run on hardware".
10. Applied: the first review's header reads "the driver's self-test (every n module's self-test and the driver's own
    checks)".
11.–13. No change: they confirm.

## 2. The edits after the check, checked by tool

- **The diffs.** `diff -U0` of each final text against its checked draft holds only the dispositions above, and Code
  read each diff in full.
  - T1 has 9 hunks:
    - item 4;
    - item 6;
    - items 9, 10 and 11 with observations 4 and 5, in one hunk;
    - item 20;
    - item 23 with observation 3;
    - item 25;
    - item 27;
    - item 29;
    - the values-check line that filled the placeholder.
  - T2 has 2 hunks: observations 8 and 7.
  - T3 has none.
  - The first review raw has 3 hunks: items 55 and 60, and observation 10.
  - The second review raw has 2 hunks: item 64 and observation 9.
- **The quotes.** Every quote in T1 and T2 is found, joined across wrapped lines, in the text and in its source: 11
  of 11. Nine are from the seat's answers, one is N.9 of 2026-11-16, and one is "(second sitting)".
- **The rebuild.** On HEAD `25c9340` it gives two insertions and nothing else: T1 after line 23, the Log's head, and
  T2 at the end of `0eb7671`'s entry.
- **The finals:**
  - T1, sha256 `b032fe66…171b`, 114 lines;
  - T2, `19af9db5…8ba7`, 18 lines;
  - T3, `b20a5a4e…4b4c`, 40 lines;
  - the first review raw, `9b0daf10…e8f5`, 321 lines;
  - the second review raw, `c456153b…4f44`, 319 lines.
- **The commit's gate** re-runs these checks on the staged blobs, rebuilds RESULTS.md from HEAD, and compares both
  the working file and the staged blob.

## 3. The report as returned

```text
BLIND VALUES-CHECK, PI date 2026-11-18, of the four texts for n step 4's driver commit. T1 S/step4b/commit/entry_driver.md sha256 44eadf842e00e957f4e3165cb5b6bbc30ca38a0fa820fd46a3e56048cf845ab6. T2 S/step4b/commit/close_0eb7671.md sha256 90d6886193ab9cc8e88c39aa8c667924f20584fee0147e66620bf1968584b351. T3 S/step4b/commit/selftest.txt sha256 b20a5a4e378b156446d3e52042bbd587515a445b8d93209906e8c1034cbd4b4c. T4 is S/step4b/commit/review1.md lines 1–31 (sha256 e4c5b368c5190e0d7316add92abcb2f66ecf064d15cdbef892babb3771db3a27) and S/step4b/commit/review2.md lines 1–20 and O3 at :70–72 (sha256 a5295b59ef943c2de0a27e2aa60bb008f183297a3e2188f20580756667402d7d). All five hashed the same at the end of the check. R's HEAD was dc6a1cf at the start and 25c9340 at the end (observation 1).

Short names: "ans" = R/results/raw/2026-11-18_n-step4-smoke-pause_design-to-code_answers.md; "STOP" = R/results/raw/2026-11-18_n-step4-smoke-pause_code-to-design_STOP.md; "box ans" = R/results/raw/2026-11-18_box-gpu_design-to-code_answers.md; "corpus ans" = R/results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md; "11-16 ans" = R/results/raw/2026-11-16_n-build_design-to-code_answers.md; "driver" = S/step4b/commit/n_sessions.py; "box1" = S/step4b/commit/box1_{out,run}.txt; "box2_out"/"box2_run" = R/results/raw/2026-11-18_n-step4_bext-box2_{out,run}.txt. Hashes are abbreviated by cut (first 8, last 4).

ITEMS

T1 — entry_driver.md

1. T1:1–3. The driver is committed by path before its run of record. The smoke of this date ended PAUSE on the fidelity binomial "as the rule requires". The authority is the seat's answers of 2026-11-18, second sitting, §1.3 item 1 and §2 (Q2 yes). CONFIRMED.
   - ans :3 reads "(second sitting)".
   - §1.3 item 1 (:20) asks for "an entry that says the smoke ended PAUSE on the fidelity binomial, as the rule requires".
   - §2 (:36) opens "Yes.".
   - box ans §2 item 5 (:28): "committed by path before step 4's run of record, the entry saying so".

2. T1:3–4 and T2:4–5. The PI's "Route as given", relayed by the coordinating session (T2: "on the paste block's section N"). CONFIRMED as relayed.
   - The coordinating session's close line was committed at 25c9340 during this check (R/RESULTS.md at 25c9340, the close on the box entry). It reads: "The PI's word on the paste block of 2026-11-18 (second sitting), verbatim: "Route as given"". The word covers the whole block.
   - The PI's own words are outside the tree, and so is the paste block's sectioning (observation 8).

3. T1:4–6. The governing texts named, apart from GA-5. CONFIRMED.
   - PROPOSAL-n v0.2 §3 G-ACQ: R/PROPOSAL-n-bk-reconciliation-v0_2.md :109, inside §3 (:105–123).
   - ADDENDUM-n1 §2: R/ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md :30–32.
   - The 11-16 answers: "(second sitting)" at :3, §2.4 at :37, §5 step 4 at :63.
   - corpus ans §5.5 at :69; box ans §2 items 4–5 at :27–28.

4. T1:4, "PROPOSAL-n v0.2 §3 G-ACQ, GA-5". IMPRECISE.
   - GA-5 is not in the proposal (the file has no "GA-" string).
   - It is G-ACQ's dated note in G-ACQ's entry (R/RESULTS.md at dc6a1cf :10479), and the driver's docstring (:39) calls it "G-ACQ's dated note GA-5".
   - Fix: "PROPOSAL-n v0.2 §3 G-ACQ and G-ACQ's dated note GA-5;".

5. T1:8–9. The driver is 18f19b8e…4f5c, built on b523f6a's scripts/n_sessions.py, numstat +1040 −8, and the n package is unchanged at f927608c…3c03. CONFIRMED.
   - The draft hashes to 18f19b8e…4f5c.
   - `git log` on the path (with ':!data/**') gives b523f6a as the newest commit, and HEAD's and b523f6a's blobs are both 4922c09….
   - `git diff --no-index --numstat` of S/step4b/chk/vc_head_driver.py (written by `git show HEAD:scripts/n_sessions.py`) against the draft gives "1040 8".
   - The package digest rule at HEAD gives f927608c…3c03. valence_core/n was last changed at b523f6a, and `git status --porcelain` on it is empty.

6. T1:8, "unchanged to HEAD dc6a1cf". IMPRECISE, now stale.
   - HEAD moved to 25c9340 during the check. The driver is unchanged to it too: the blob is still 4922c09….
   - Fix: "unchanged to HEAD `25c9340`", re-checked against HEAD at the commit.

7. T1:10–11. Self-test 333/333 on the laptop, 344/344 at the box. CONFIRMED.
   - S/step4b/out/selftest_v2d_2.txt reads "  333/333 n selftest checks pass", and its .exit file reads 0.
   - box2_out :31–32.
   - ans §1.3 item 1 (:20) gives the same pair.

8. T1:12–14. The smoke: two reads, never of record, the STOP 0eb7671. Every step before the monitor held; it ended PAUSE on the fidelity binomial at the run's end; p0 = 0; read 1 was above TAU. CONFIRMED.
   - box2_out :1–46 are steps 0–3. At :47–63: "read 1 s=5 N1-V none 0 fid=0.086070 > TAU" and "PAUSE fidelity-binomial at the run's end".
   - STOP §0 :35–48; ans §0 :8.

9. T1:14, the quote "The smoke passed for the commit's purpose" cited to §2. IMPRECISE.
   - The sentence is verbatim at ans :8, which is §0 (the short form, Q2).
   - §2 (:36) opens "Yes. The smoke's purpose was to show the driver runs on the box" and does not contain it.
   - Fix: "(§0)" in place of "(§2)".

10. T1:15–16, the first review's "with 15 mutants, 11 surviving its reading". FAIL.
   - review1.md :123–137 mark 12 of the 15 as SURVIVES: M1, M3, M4 and M7–M15 (`grep -c SURVIVES` gives 12).
   - Three were killed: M2, M5 and M6 (:124, :127, :128). Code's own line at :237 reads "Killed by existing checks: M2, M5 and M6".
   - Code's list of new tests for the survivors (:239–252) has 12 entries.
   - "13 (6 RISK, 7 NIT, no BUG)" and "15 mutants" are right: findings 1–6 are RISK and 7–13 NIT (:39–121), and the report says "I found no hard BUG" (:35).
   - Fix: "with 15 mutants, 12 surviving its reading".

11. T1:15, "The first, of v1 on 2026-11-16". IMPRECISE.
   - The date is right (review1.md :3).
   - The first review read v1's first draft, 80d30846…b03d (review1.md :8). S/step4/n_sessions.v1.py hashes to it, and the report's cited lines :218, :245, :259, :276, :289, :307, :330, :342, :364, :371, :385, :415 and :458 are that file's lines.
   - T1:68's "v1" is the frozen 64cf6ee1…16cb, which the A100 ran (box1_run :15).
   - Fix: "The first, of v1's first draft (`80d30846…b03d`) on 2026-11-16, …".

12. T1:16–17. The second review found 10 (2 RISK, 8 NIT, no BUG) with 10 surviving mutants. Every finding is applied, and every survivor has a test written to kill it. CONFIRMED.
   - review2.md's Totals (:313–316) and its header (:19).
   - Its F1–F10 are all "Applied" (:24–59), and :61–63 read "each now has its killing test".
   - review1's dispositions of findings 1–13 are at :157–233, and its 12 survivor tests at :239–252.
   - Spot checks in the driver: the R1 pin check :955, "median 0.0123457" :1124, "over its 48 values" :1212, "(unchecked)" :1257–1259, the pod refusal's text :1300, redirect_stderr :1314.
   - See observations 5 and 6.

13. T1:18. Nothing ran on a checkpoint's weights before this commit except the smoke. CONFIRMED for this driver.
   - The A100 check loaded no weights (box1_run :8–11).
   - The laptop runs are model-free.
   - The box self-test's HF cases build a tiny config with no weights (R/valence_core/n/hftiny.py :1–7).
   - See observation 4.

14. T1:19–33. What the command does: seven steps in order, one model load. CONFIRMED against run_backend_ext (driver :798–912). The code runs:
   - the root and report refusals for a smoke and for a run of record (:808–821);
   - the pod check, refusing none or another pod (:822–827); the cuBLAS setting; stream_known_answer (:830); the ruling files;
   - weights_of_record (:486; HEAD's manifest bytes, the instruct entry, check_weights_folder :470) and the WEIGHTS line (:838);
   - the driver check: a run of record is refused unless the bytes are HEAD's (:844), and the DRIVER line prints the sha256;
   - the ids against MANIFEST_OF_RECORD (:851), the pre-load bridge (:855), the identity, prior_state (:865), BK's table (:867), and comparison_ids for every candidate (:873);
   - G-VER, whose STOP returns 1 before make_adapter (:874–879);
   - the load and the provenance re-check (:881–884), then runner.run (:894);
   - on COMPLETE, the discordance, in_band (:907), counts_line (:703–707, "the count of {n_floor} and the median |value - BK's| over its {2 * n_floor} values, nats") and convention_line (:911).

15. T1:26, rendering_id fdf73d85…ef38. CONFIRMED. It equals ids.MANIFEST_OF_RECORD (R/valence_core/n/ids.py :74) and the sha256 of R/data/n/ids/MANIFEST.json.

16. T1:35. CHARACTERIZED_POD is emw1e4embiwe9b and CHARACTERIZED_IDENTIFIER is 4ed3f2c70fe8afbf. CONFIRMED (driver :412, :420).

17. T1:36–37. CHARACTERIZED_PROVENANCE is the block R/results/raw/2026-11-18_respawn_determinism.txt prints and equals the committed artifact's; the self-test checks it with the artifact's sha256 pinned. CONFIRMED.
   - The driver's literal (:413–419) and the raw's block (:11–37) match on all 15 keys.
   - The artifact data/olmo/determinism_base_h100-sxm.json (reached by cd and a glob) hashes to 1dd9199f…d3c1, the value pinned at driver :424. Its provenance, read with jq, equals the literal.
   - The check is at driver :1003–1007.

18. T1:38–39. d5d08fa is cited throughout; R6 is retargeted, not dropped; n's own identifier, under its 4,096 window, prints beside the box's. CONFIRMED.
   - The driver cites d5d08fa at :86, :409, :826 and :1300.
   - box ans :27: "R6 is retargeted … it is not dropped".
   - The backend line is at driver :888; box2_out prints "n's identifier 8264f719efd347a9 (window 4096); the characterization's 4ed3f2c70fe8afbf".

19. T1:41–43. The median is the mean of the middle two; a non-finite value enters as +inf and never matches; six significant digits, in nats; §5.5 leaves these open. CONFIRMED.
   - statistics.median is at :673; d = inf and the isfinite gate at :668–670; ":.6g" and "nats" at :705–707.
   - corpus ans :69 fixes none of the three.

20. T1:44–45. "exactly one candidate at 40 of 40 is the convention of record; otherwise the seat rules…" is listed among the conventions "§5.5 leaves open". IMPRECISE.
   - §5.5 states this rule itself (corpus ans :69): "Exactly one candidate at 40 of 40 is still the convention of record; otherwise the seat rules on the four counts and the four medians". So does ADDENDUM-n1 §2 (:32).
   - Fix: take the bullet out of the list and add after it: "§5.5 keeps the rule: exactly one candidate at 40 of 40 is the convention of record; otherwise the seat rules on the four counts and the four medians."

21. T1:46. "as the seat ruled them (§1.5: "R1–R6 stand")". CONFIRMED (ans :32, verbatim).

22. T1:47–48, R1 and R2. CONFIRMED.
   - BEXT_KEY "n-bext" (:396); bext_sessions (:438–444); BEXT_SESSIONS_SHA256 10f3a127…6b64 (:427) and its check (:955).
   - BEXT_CONVENTION "bare" (:398), with the docstring's R2 at :74.

23. T1:49–50, R3: "each label's largest |logprob − fresh_logprob| over the 24". IMPRECISE.
   - The bound is one maximum over both labels and all reads: discordance's label.max (:581, pooled over S and U) is passed as `float(disc["label"]["max"])` (:909).
   - The docstring's R3 (:76) says "the largest per-label |logprob - fresh_logprob| over the 24 reads". "each label's largest" can be read as two bounds.
   - The rest is right: "the margin's distribution printed beside it".
   - Fix: "the comparison's bound is the largest per-label |logprob − fresh_logprob| over the 24 reads (one maximum over both labels)".
   - See observation 3 on "the bound is not 0".

24. T1:52–53, R4's values. CONFIRMED.
   - The capture site 32 is BEXT_LAYER (:399), and nothing is injected.
   - The band is range(33, 64) (:555), which the self-test checks.
   - The window is schema.MAX_WINDOW = 4096 (R/valence_core/n/schema.py :254).
   - "1,276 tokens with the longest label": the committed ids of R/data/n/ids/sessions.jsonl run 1,266–1,273 tokens and the longest candidate label is 4 tokens (lengths only, via jq). The forward is 1,273 + 4 − 1 = 1,276 tokens (comparison_ids :636), matching the docstring's R4.

25. T1:53, the window's citation "(rule 28(d))". IMPRECISE.
   - The driver's R4 cites GA-4 for the window (:80, "schema.MAX_WINDOW (GA-4)").
   - The schema's entry has "(rule 28(d)(c); GA-4)" (R/RESULTS.md at dc6a1cf :3721).
   - Fix: "(GA-4; rule 28(d)(c))".

26. T1:54–57: R5, R6, p0 and the end-of-run evaluation, with their quotes. CONFIRMED.
   - R5: BEXT_ALPHA 0.01 (:400) and hour_cap_ms=None (:893).
   - "moot at p0 = 0", "right for this run" and "accepted as the rule's form" are verbatim at ans :32.
   - The fidelity_rule carries p0_count 0 and p0_n 2400.

27. T1:58, "(the run proceeds on them, by the PI's routing of 2026-11-16, N.9)". IMPRECISE.
   - N.9 is at R/results/raw/2026-11-16_p-verdicts-decisions_design-to-code_answers.md :69: "The seat's answers on `718c48e`, `8e3bf91` and `e5aba51` come at its next sitting; the build proceeds on Code's interim readings as its entries have it [noted]." It names the build and those three blocks, not this driver or its run.
   - The BUILD entry (R/RESULTS.md at dc6a1cf :967) and STOP §6 cite it for the package's flags only.
   - Fix: quote N.9's scope and mark its extension as Code's reading. For example: "(flagged; the run proceeds on them as the BUILD's flags do, Code reading the PI's routing of 2026-11-16, N.9, "the build proceeds on Code's interim readings as its entries have it", as covering the driver's)".

28. T1:59–60. The first two still-flagged readings: at a G-VER STOP the raw is the STOP's record with no stage report, and a ruled non-finite read leaves the comparison refused on every later invocation. CONFIRMED.
   - None of ans, box ans, corpus ans or 11-16 ans rules either.
   - The driver matches both: the docstring at :54–57, and :903–905 returns 1 after any COMPLETE with a non-finite read, so every resumed invocation repeats the refusal.

29. T1:61–62. "n's own identifier and the characterization's both stand in the record, and later n stages need the same bridge", listed as still flagged. IMPRECISE.
   - The first half is box ans §2 item 4 (:27): "The extension records n's own provenance hash under its window beside the box's identifier; both go in the dated note and in LOCK-n v0.1".
   - Only "later n stages need the same bridge" is unruled.
   - Fix: "- later n stages need the same bridge (that both identifiers stand in the record is the box answers' §2 item 4)".

30. T1:63–66. The box script's convention amendment; the box scripts are Code's scratch files, never committed; no second smoke. CONFIRMED.
   - The quote and "PAUSE (pass)" are verbatim at ans :36 (§2), as is "for this stage and for any stage whose smoke can reach a monitor".
   - No bext box script is tracked or was ever committed: the only .sh files in history are scripts/run_b2r.sh and scripts/run_bphase.sh, and the only '*bext*box*' commit is 0eb7671 (the box2 raws).
   - "binds the next one" is Code's reading of §2's scope and is stated as such.

31. T1:68–72. v1 on the A100 pod, 2026-11-16: steps 0–3 held; CUDA error 802; R6 refused before G-VER; no weights loaded, nothing read or written. CONFIRMED.
   - box1_run :1–11, and :15 names the driver 64cf6ee1…16cb.
   - box1_out :1–42 are steps 0–3 (selftest 278/278, the package 60d892dc…cc66).
   - :44 is "Error 802: system not yet initialized", and :48 is R6's refusal against 641ee466f4553b6a.
   - There is no G-VER line, and :50 reads "SMOKE IDENTITY NOT CHECKED: no smoke report". box1_run :11 adds "the smoke wrote no file".
   - box1_out hashes to e2d9774c…831f, the value STOP :27 cites.

32. T1:73–74. v2d on the H100 pod, 2026-11-18, its raws committed at 0eb7671: steps 0–3 held and the smoke ended PAUSE. CONFIRMED.
   - `git show --name-only 0eb7671` lists both raws.
   - box2_run :7–12; box2_out hashes to 202e6bd7…a872 and box2_run to 7933fb33…2590, as the STOP cites.

33. T1:76–78. Three read-only commands on 2026-11-16 carried a guard marker in their argv, and none of these ran Python. NOT CHECKABLE: these are Code's disclosures. They are consistent with Code's scratch note S/step4/departures.md (observation 13).

34. T1:78–79. A box script was changed in place after its hash had gone for relay, and nothing ran on the stale version. CONFIRMED. box1_run :19–21: "The relay first named bext_box.sh 6bf8351d...f9d7; the file on disk was d27d6daa...1527 … 6bf8351d was never run."

35. T1:80–84, the two 2026-11-18 departures. CONFIRMED.
   - Both are in STOP §6 (:186–192) and seat §4 (ans :50).
   - 332/333 with exit 1: S/step4b/out/selftest_v2d.txt and .exit. 333/333 with exit 0: selftest_v2d_2.
   - The window grants are NOT CHECKABLE.

36. T1:86, "The seat ruled the two of 2026-11-18 inert (§4)". CONFIRMED (ans :50: "Code's two (`0eb7671` §6) … Inert.").

37. T1:88–95, the committed-by-path list. NOT CHECKABLE: it describes the commit to come. It is consistent with S/step4b/commit, which holds the v2d draft, selftest.txt, review1.md, review2.md, box1_out.txt, box1_run.txt, the entry and the close.

38. T1:97–98. Next: the run of record, then the diagnostic (§1.3 items 2–3). CONFIRMED (ans :21–22). "Not pushed" describes the commit to come.

T2 — close_0eb7671.md

39. T2:1–4. Second sitting; the raw's name; sha256 cdecf39e…01d3; committed by path at dc6a1cf by the coordinating session. CONFIRMED.
   - ans :3 reads "(second sitting)", and the file hashes to cdecf39e…01d3.
   - `git show --name-only dc6a1cf` lists only this raw.
   - The coordinating session's close at 25c9340 says it "is committed by path at `dc6a1cf`".
   - "read … in full" is NOT CHECKABLE.

40. T2:6–8. The Q1 (a) quote and the diagnostic sentence. CONFIRMED. The quote is verbatim at ans :7 (§0). The diagnostic sentence matches §0 :7 and §1.3 item 3 (:22).

41. T2:9–11. Q2 yes: the quote, the amendment, "PAUSE (pass)" with (§2), and "No second smoke." CONFIRMED.
   - All are verbatim: :8 for the first quote, :36 for the rest. "(§2)" belongs to the amendment, which is in §2.
   - See observation 7.

42. T2:12–14. The §1.5 quote; ledger (82) the seat's (§1.2); Code's two departures inert (§4). CONFIRMED.
   - The quote is verbatim at ans :32.
   - Ledger (82) is at :9 and :17, the departures at :50.

43. T2:15–17. This session's part, in §1.3's order; its entry heads the Log; the cost estimate (§1.4). CONFIRMED.
   - §1.3 items 1–5 are at :20–24, the record at §5 :55, and §1.4 at :30 ("n-build estimates its cost … for G-TIME-n").
   - S/step4b/commit/rebuild_results.sh puts entry_driver.md directly after the Log heading (HEAD's lines 1–23) and the close at the end of 0eb7671's entry.

T3 — selftest.txt

44. T3:1–2, the header. CONFIRMED (ans §1.3 item 1, :20).

45. T3:4–6. The driver's full sha256, and the package valence_core/n at b523f6a with its full digest. CONFIRMED (items 5 and 15).

46. T3:8–9. The HF cases are skipped where torch and transformers are absent, and counted as skipped. CONFIRMED.
   - The driver's docstring is at :6–12.
   - hftiny.run (:55–57) records one skip check, and hftiny.available needs both libraries.
   - The driver's vanilla-score skip check is at :1149.

47. T3:10–17, the overlay and the command line. NOT CHECKABLE: this is Code's process. It is consistent with what is on disk:
   - S/step4b/overlay/scripts/n_sessions.py is v2d (18f19b8e…4f5c), and the overlay's valence_core/n hashes to f927608c…3c03 by the digest rule.
   - The overlay holds the H100 raw (equal to R's) and the artifact (1dd9199f…d3c1).
   - The listed paths exist at d5d08fa (`git ls-tree --name-only`).

48. T3:19–21. Run 1's window, and the seat's §4 "inert". CONFIRMED for §4 (ans :50). The grant is NOT CHECKABLE.

49. T3:22–23, run 1's whole output, exit 1. CONFIRMED byte for byte: `cmp` of T3 :22–23, its 5-space indent removed, against S/step4b/out/selftest_v2d.txt is equal, including the trailing space after "names:". The .exit file reads 1.

50. T3:24–25. The check reads the characterization's committed artifact and raw (d5d08fa), which the overlay lacked. CONFIRMED.
   - The check reads both at driver :1000–1007.
   - Both files are d5d08fa's (`git show --name-only d5d08fa`).
   - The FAIL line's empty detail is box_line[:40] with the raw absent.
   - How they were added is NOT CHECKABLE.

51. T3:27–29, run 2's whole output, exit 0. CONFIRMED byte for byte (`cmp` against S/step4b/out/selftest_v2d_2.txt). The .exit file reads 0.

52. T3:31–33. The box: pod emw1e4embiwe9b, the H100 SXM of d5d08fa, 2026-11-18; step 2 of bext_box_v2.sh, in a scratch copy at d5d08fa with exactly the driver changed. CONFIRMED.
   - box2_out :1–3 and box2_run :1 and :34–42.
   - S/step4b/box/bext_box_v2.sh hashes to 2bde09d9…af51 and has 95 lines, as STOP §9 says. Its step 2 (:54) is the self-test.

53. T3:34–38, box2_out lines 28–32 verbatim. CONFIRMED byte for byte: `cmp` with the 5-space indent removed is equal.

54. T3:39–40. The box runs 11 checks more: hftiny's 12 in place of one skip line, and the HF-path vanilla score in place of its skip line. CONFIRMED.
   - hftiny.run makes 12 chk calls when available (:71, :73, :78, :80, :88, :90, :94, :99, :120 twice in its loop, :121, :124).
   - No other availability branch exists in valence_core/n.
   - The driver's vanilla score is at :1136–1149.
   - 333 − 1 + 12 − 1 + 1 = 344.

T4 — review1.md :1–31

55. r1:3–5. "It is §5 step 4 of the seat's order: the BACKEND extension and ADDENDUM-n1 §2's label-convention comparison, in one invocation on the box." IMPRECISE.
   - The step is right: 11-16 ans :63.
   - The seat's words are "The BACKEND extension on the box, then §2.4's comparison in the same session". ADDENDUM-n1 §2 (:32) says "in the BACKEND extension's session". One invocation is the driver's design.
   - Fix: "…label-convention comparison in the same session (§5 step 4), here in one invocation on the box."

56. r1:7, "the package (60d892dc…cc66) is unchanged". CONFIRMED. The digest rule applied to the blobs at 83a50a0 and at 977b78b gives 60d892dc…cc66, and box1_out :30 shows the same value.

57. r1:8, the first draft 80d30846…b03d. CONFIRMED (S/step4/n_sessions.v1.py; the line-number match in item 11). "a Code subagent" is NOT CHECKABLE.

58. r1:9–14, the governing texts. CONFIRMED that each exists:
   - n v0.2 §2.1 and §3 G-ACQ; ADDENDUM-n1 §1.3 and §2; the 11-16 answers §2.4 and §5;
   - GA-4 and GA-5 (R/RESULTS.md at dc6a1cf :10477–10480);
   - 7ab4d2f holds results/raw/2026-11-15_respawn_determinism.txt.
   - What the brief gave is NOT CHECKABLE.

59. r1:15–22, the brief's rules, and "given to the reviewer to check, not to adjudicate". NOT CHECKABLE: the brief is not in the tree. It is consistent with the report ("I ran nothing and wrote nothing", :35; "Fix, for the seat since R3 is a reading", :63).

60. r1:23–24, "15 mutants, of which 11 survived by its reading". FAIL.
   - 12 survived (item 10's evidence).
   - "13 findings (6 RISK, 7 NIT; no BUG)" and "15 mutants" are right. "Each survivor came with the test that would kill it" holds (observation 6).
   - Fix: "and 15 mutants, of which 12 survived by its reading".

61. r1:26–28, the edited sentence: "The draft as frozen (64cf6ee1…16cb) passed the package self-test at 267/267…". CONFIRMED.
   - 64cf6ee1…16cb is S/step4/scripts/n_sessions.py, and its blob is in no commit: `git log --all --find-object` with item 3's pathspec found none, while the control blob 4922c09 gave b523f6a. So "as frozen" is right, where the scratch version's "committed" was not.
   - 267/267 matches the raw's own runs section (:316–318), and the A100's 278 = 267 + 11 (box1_out :27).
   - The venv, the nice level and the windows are NOT CHECKABLE.
   - See observation 10.

62. r1:30–31. The report is reproduced as returned, its line numbers are the first draft's, and "P" is Code's scratch folder. CONFIRMED.
   - review1.md :35–151 equals S/step4/review_returned.md byte for byte (`cmp`).
   - The line numbers match the first draft (item 11).
   - The report writes "P/step4/scripts/n_sessions.py".

T4 — review2.md :1–20 and O3

63. r2:1 and :3, the title and the date. CONFIRMED: the three parts of the delta are in the report's "What checks out" (:103–113).

64. r2:6, V1 as "the step-4 driver as reviewed in the first review and box-tested on 2026-11-16". IMPRECISE.
   - The sha256 and the box test are right (box1_run :15).
   - The first review read the first draft, 80d30846…b03d (review1.md :8). V1 is that draft with the review's dispositions applied (review1.md :26).
   - Fix: "the step-4 driver as frozen after the first review (which read its first draft, `80d30846…b03d`), and box-tested on 2026-11-16;".

65. r2:7–9. V2C 491584aa…c63d, its composition and its citations. CONFIRMED.
   - S/step4b/n_sessions.v2c.py hashes to 491584aa…c63d.
   - The report's :89 and :103 say "By tool, V2C = HEAD + V1's change + item 7 + the re-pin".
   - HEAD's driver at b523f6a is the blob 4922c09.

66. r2:11–14, the brief. NOT CHECKABLE. It is consistent with the report's Method (:93–99).

67. r2:16–17. §2 has 236 lines, sha256 85f52a0b…8cc6, and writes `<repo>` and `<scratch>`. CONFIRMED.
   - review2.md :82–317 is 236 lines and hashes to 85f52a0b…8cc6.
   - It is byte-equal to S/step4b/review2_returned.md.
   - "by jq" is NOT CHECKABLE.

68. r2:19, the Totals. CONFIRMED (report :313–316; O1–O6).

69. r2:70–72, the edited O3 sentence: "R6 had run on the A100 on 2026-11-16 and refused before the load, and the H100 smoke is the first in which its bridge held (the STOP of 0eb7671, §4)". CONFIRMED.
   - STOP §4 (:147–157): the A100 smoke "refused before the load, at R6", and the H100 smoke is "the first in which R6's bridge held (on the A100 it ran before the load and refused)".
   - box1_out :48.
   - The review preceded the smoke: V2C was reviewed, and V2D ran.
   - See observation 9.

Cross-checks

70. T1 and T2 agree with each other and with 0eb7671's STOP and entry: Q1 (a), Q2 yes, the same §1.5, §2 and §4 rulings, and the same next steps. The STOP's figures recur unchanged: 23/23, 344/344, 333/333, 332/333, the fid values and the A100's refusal at R6. CONFIRMED.
   - Neither text adjudicates.
   - Neither states as ruled anything the seat did not rule. The exceptions in scope are items 20 (grouping), 27 (N.9's scope) and 29 (a half-ruled item still listed as flagged).

OBSERVATIONS

1. HEAD moved during the check, from dc6a1cf to 25c9340: the coordinating session's dated note at the Log's head (+82 lines) and its close line on the box entry (+43 lines). The commit touched RESULTS.md and two raws only.
   - The driver, the package and 0eb7671's entry are untouched. The entry is at :140 at dc6a1cf and :222 at 25c9340.
   - The rebuild script's anchors still hold: line 22 is the Log heading and line 23 is blank. T1 would sit above the new note, still heading the Log.
   - RESULTS.md anchors in this report are at dc6a1cf unless marked.

2. A quirk of git 2.39.5 here: `git ls-files -- <path with a directory part> <any exclude form>` prints nothing, even for a tracked literal path.
   - Tested with ':!data/**', ':(exclude,glob)data/**' and ':!data/*/ckpt/**'.
   - With '.' or a pattern with no directory part, it lists correctly.
   - `git status --porcelain`, `git grep`, `git diff --name-only` and `git log` with the same pairs were unaffected.
   - So a tracked-or-not check written as ls-files plus item 3's pathspec plus a directory path passes vacuously.

3. R3's "The smoke's two reads differ between the paths, so the bound is not 0" is an inference.
   - The smoke printed no bound: it paused before the distribution.
   - It holds for the run of record if the box repeats the smoke's reads, which are its plan's first two (STOP §7).
   - A wording such as "…so on the run of record, which repeats them, the bound cannot be 0" would make that explicit.

4. T1:18 reads as being about this driver. Another unit's runs on weights are not in its scope, and saying "of this driver" would remove the ambiguity.

5. "Every finding is applied" holds in a broad sense.
   - review1's finding 9 took the reviewer's second remedy: it was declared as a reading (:223).
   - Finding 3 was applied as a revised reading (:172–173).

6. review1's M13 carries its test by reference to finding 6 (:135, which points to finding 6's fix at :96–107), not with a "Test:" of its own.

7. The quote "The smoke passed for the commit's purpose" is §0's. T1 cites it to §2 (item 9), and T2 gives no section.

8. The seat's §6 routing block has two sections headed "N.": n-build (items 1–5) and n-analyzer (item 6). The paste block's sectioning is not in the tree.

9. review2's O3 still opens with the reviewer's reading as a fact ("The H100 smoke is R6's first run on hardware.") before qualifying it. A wording such as "The reviewer read the H100 smoke as R6's first run on hardware; …" would avoid the apparent contradiction.

10. review1 :26–27's "the package self-test" is the driver's `--selftest`: every n module's self-test plus the driver's checks (driver docstring :6).

11. Outside T4's scope, review2 :23's "V2C plus 119 lines and minus 21" is right: `git diff --no-index --numstat` of S/step4b/n_sessions.v2c.py against v2d gives 119 and 21, and v2d equals the commit draft by `cmp`.

12. No laptop path, scratch path, user name or IPv4-like string appears in T1–T4 or in box1_out.txt or box1_run.txt (grep counts 0). No pod address or port was seen anywhere.

13. T1:76–78's three 2026-11-16 commands match Code's scratch note S/step4/departures.md item for item.

TOTALS
- 70 items: 52 CONFIRMED, 11 IMPRECISE (4, 6, 9, 11, 20, 23, 25, 27, 29, 55, 64), 2 FAIL (10, 60), 5 NOT CHECKABLE (33, 37, 47, 59, 66).
- 13 observations.

COMMANDS RUN, by class
- Shell builtins cd, printf and echo. I reached data/olmo by `cd data/ol*`, in R and in S/step4b/overlay, and passed file names alone.
- Names-only `ls` of S/step4b/{commit,out,chk}, S/step4b, S/step4, S/step4/scripts, R/data (its top-level names), R/valence_core/n and S/step4b/overlay/valence_core/n. Inside R/data/olmo, `ls | grep -c .`, a count of names only.
- Reads and comparisons: sed -n, cat -n, cut, awk, tr, sort, wc -l, od -c, cmp (with process substitution), diff and jq.
  - jq read the H100 artifact's keys and provenance, and the lengths only of R/data/n/ids/labels.json and sessions.jsonl.
  - `head -c 300` of sessions.jsonl was run with every digit masked; no id was printed.
- shasum -a 256 throughout. wc -c only inside the package digest rule (valence_core/n files, and the same rule over blobs at 83a50a0, 977b78b and d5d08fa).
- /usr/bin/grep on named files.
- git:
  - rev-parse; log --format with ids and subjects, using ':!data/**' or item 3's pathspec;
  - log --all --find-object and log --all --name-only, with the pathspec;
  - show --name-only with item 3's pathspec plus ':!data/mf3/**';
  - show <rev>:<path> for the driver, the package files and RESULTS.md;
  - diff --no-index --numstat on scratch files;
  - diff --stat, -U0 and -U1 on RESULTS.md between dc6a1cf and 25c9340, with ':!data/**';
  - ls-files; ls-tree --name-only; status --porcelain on named paths; grep -l on results/raw; hash-object without -w; --version.
- Nothing else: no Python of any kind, no model, no network, no ssh, no commit, and no edit to T1–T4 or any repository file.

DEPARTURES
(a) I wrote two scratch files beyond the one allowed: S/step4b/chk/vc_t3_box.txt and S/step4b/chk/vc_box2_28_32.txt, by shell redirection for a cmp. I then removed both with rm and used process substitution from there on. The allowed S/step4b/chk/vc_head_driver.py is left in place.
(b) Several path-taking git commands ran without item 3's pathspec. All were scoped to paths outside data/, and all printed names, except one git grep over results/raw:
   - git ls-files on 'results/raw/*bext*', 'results/raw/*n-step4*', '*n-step4*', a literal box2 path, and a no-exclusion control while characterizing observation 2;
   - git status --porcelain -- archive;
   - git grep -l 'N\.9' -- results/raw;
   - git diff --name-only HEAD~5 HEAD -- results/raw;
   - git ls-tree --name-only on named paths at d5d08fa, and on valence_core/n/ at three revisions.
   For the seat to class.
(c) Two recursive /usr/bin/grep -r over R/results/raw, which holds no ckpt or reports directory, without the find-prune form.
No guard marker was in any argv; nothing under data/mf3, data/*/ckpt or data/*/reports was listed or read; no whole-tree git status was run; S/step4b/box/out and anything named smoke-root were never opened or listed.
```
