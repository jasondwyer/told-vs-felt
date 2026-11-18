# n step 4 — the run of record's pause and the diagnostic, for the seat: the blind values-check, as returned, with every disposition

PI date 2026-11-18. Code (the n-build session).

**What was checked.** One blind pass by a subagent over four drafts:
- T1, the block for the seat (`results/raw/2026-11-18_n-step4-run-pause_code-to-design_STOP.md` as drafted), sha256
  `10efa7c0…3ae2`;
- T2, its entry, `115e7ca4…6289`;
- T3, the diagnostic's self-test raw, `b3b8c645…4164`;
- T4, the `.gitignore` with its admit block, `ea56cbb6…2d06`, against HEAD's.

**The checker's brief:**
- named the sources: the run's and the diagnostic's box outputs and the pod session's records of them, the diagnostic
  script, the box scripts and manifests, the seat's answers, the earlier block (`0eb7671`), PROPOSAL-n v0.2,
  WORKFLOW.md, `primitive.py`, `schema.py`, the driver and `labels.json`;
- allowed only `shasum`, `jq 'keys'` and `jq '.cells'` on the stage report, and only `shasum` on the cell, with no
  listing, `find` or `grep` inside the scratch folder that holds their copies;
- quoted the list of record v2's items 1–5, verbatim, and the seat's line that a git command in a check takes item 3's
  pathspec;
- barred any interpreter, any guard marker in an argv, anything under `data/mf3`, any write, and any token id printed.

**The report** is in §3 below, extracted verbatim from the subagent's hand-back by `jq` (307 lines, sha256
`1a9ecd5e…9f69`). It writes `R/…` for the repository and `S/…` for Code's scratch.

**Totals:** 63 items — 54 CONFIRMED, 3 IMPRECISE, 2 FAIL, 4 NOT CHECKABLE — and 9 observations.

**The checker's departures,** as its report states them. All were model-free; nothing under `data/mf3`, `data/*/ckpt`
or `data/*/reports` was listed, and no size or time of any ckpt or reports file was taken.
- (a) A loop over a glob in Code's self-test overlay that it had not seen expand. It expanded to the 14 package module
  names, none holding a marker.
- (b) Path-taking git commands without item 3's pathspec, each on named non-data paths, or printing a count or
  attributes. For the seat to class.
- (c) A wider exclusion than needed, on one `git diff --name-only`.
- (d) Its reading of one long command's output from the harness's own tool-results folder, where the harness had saved
  it, outside the repository and the scratch.

## 1. Dispositions

**The two FAILs, both applied, both in T1.**
- **25**: "The rest summed is token 1's to within 2e-06 (token 2's size)". These are the checker's words.
- **36**: "Seven reads print fid 0.000000 (rel below 5e-7), and ten exceed TAU. The per-token values are nonzero in
  every read (the minima in §3)."

**The IMPRECISE items, all applied, all in T1:**
- **12**: "the run's stdout carries no margin and no pick (the records' margins and restricted-read picks are in the
  cell, under `data/n/ckpt`), so nothing in it is redacted".
- **38**: "the self-tests (344/344 and 30/30), the run's package and closure hashes and its G-VER, the diagnostic's
  hash of the run's stdout, and R6's bridge in both".
- **43**: "its self-test raw (the laptop's run, the box's lines beside it)".

**The NOT CHECKABLE items** (60–63) are the PI's words, the coordinating session's words and grants, Code's own
conduct, and the commit to come. They stand as declared. No change.

**The observations:**
1. Applied in T1 §0. The "PAUSE (pass)" convention "speaks of a smoke; Code reads its 'for this stage' as covering the
   run of record".
2. **Applied, and the commit grows by one file.** The cell's records carry each read's margin and the restricted
   read's pick, and `data/n/ckpt/` had no `-diff` rule. The commit now adds `/data/n/ckpt/** -diff` to
   `.gitattributes`, in the form m, mf3 and p have (m:318's form). T1's "Not questions" and record, and T2, say so. Two
   things were checked by tool:
   - in a scratch repository, `git check-attr` gives the cell `diff: unset` and the report none;
   - the file's diff against HEAD is the four added lines.
   The line was added after the check, on this observation, so the checker did not read it.
3. No text change: `origin/main` is at `ad856f0`, and T1 and T2 speak of the new commit only.
4. Applied twice in T1, in Q1 and Q2: "Code's reading: the discordance is a property of the two paths on this box",
   and "Code's reading: … the condition reads as met; the decision is the seat's".
5. Applied: "What follows the ruling (§1.3 item 4, which names no difference between the two forms)".
6. Applied in T4's comment: "on the coordinating session's word", where it had "ruled".
7. Applied: "in the output's order".
8. Applied in T1 Q2. The cost comes from the diagnostic's own timing; the records' `duration_ms_fresh` are in the
   cell, closed to Code, and the seat or the analyzer at G-TIME-n may read them there.
9. Applied as Code's reading in T1 §3: token 1's row takes the same input for both labels, so a difference between
   the paths that moves both labels alike cancels in the margin.

## 2. The edits after the check, checked by tool

- **The diffs.** `diff -U0` of each final text against its checked draft holds only the dispositions above, and Code
  read each diff in full.
  - T1 has 13 hunks:
    - items 12, 25 and 38;
    - item 36 with observation 5, in one hunk;
    - item 43;
    - observations 1, 7, 8 and 9;
    - observation 4, twice;
    - observation 2, twice.
  - T2 has 2 hunks: the values-check and cell lines, with the `.gitattributes` line's provenance; and the record's
    `.gitattributes` line.
  - T3 has none. T4 has 1, observation 6.
- **The checks on the final T1:**
  - The two verbatim blocks equal the run's output lines 57–80 and the diagnostic's lines 37–49.
  - Every quote in T1 and T2 is found, joined across wrapped lines, in its source: 7 of 7.
  - T3's quoted lines are their sources' bytes.
- **The finals:**
  - T1, sha256 `3b803810…63bc`, 224 lines;
  - T2, `97fadeec…d57e`, 58 lines;
  - T3, `b3b8c645…4164`, 26 lines;
  - the `.gitignore`, `9c9bcdd9…6640`, 348 lines;
  - the `.gitattributes`, `117eff71…8b07`, 21 lines.
- **The commit's gate** re-runs these checks on the staged blobs. Of the cell it takes the sha256 only, and of the
  report its `cells` record only. Its scrubs exclude `data/*/ckpt` and `data/*/reports` by item 3's pathspec.

## 3. The report as returned

```text
Blind values-check, 2026-11-18, of the drafts for n step 4's run-pause commit. The drafts as found, re-hashed equal at the end of the check:
- T1 S/step4b/rec_commit/stop.md, sha256 10efa7c08a49697d5a072cdca6d973e68aaeb47bbcdd80efe21e978a94913ae2
- T2 entry.md, sha256 115e7ca437889237d0235f70afc5e878912c3a1c48dd4f82c9883cc514f16289
- T3 diag_selftest.txt, sha256 b3b8c645c757301d51f1a5f8f1dd20b9e23415aa99ff98b1f0ec96fdd1444164
- T4 gitignore_new.txt, sha256 ea56cbb6758691e1faf33ba9d3a1dc080780649e885a8efdab3e1cf7f24a2d06, checked against `git show HEAD:.gitignore` at ad856f0.

Totals: 54 CONFIRMED, 3 IMPRECISE, 2 FAIL, 4 NOT CHECKABLE (63 items). Both FAILs are in T1 (items 25 and 36), and each comes with its fix.

## Items

### T1

1. **The abbreviated sha256s** (T1:7–10, 14–24, 119, 191, 201–209; T2:23; T3:6, 11, 14). CONFIRMED. Each was recomputed with shasum and cut (first 8, last 4) and matches:
   - driver 18f19b8e…4f5c: equal to R/scripts/n_sessions.py and to `git show ad856f0:scripts/n_sessions.py`
   - box script v3 f56fd61d…5369
   - diagnostic c0ac67e4…08d1 (T3:6's full form is exact)
   - bext_diag_v1.sh 64384fa4…8e55
   - run output 910e20a7…0e48 and its record 3a3fef2e…d44c
   - diag output 0d311f01…fc8b and its record 61e73ce4…07c5
   - report 27bc906a…2496 and cell 80770a19…78ea
   - seat's answers cdecf39e…01d3
   - primitive.py 7e7bb0a0…0b0c
   - labels.json 43a32a1b…49da
   - run.txt e4e1c810…e378
   - package f927608c…3c03 (run3_out:35)

   The copies in rec_commit are byte-equal (cmp) to S/step4b/run3/out, S/step4b/diag/out and S/step4b/diag/n_bext_diag.py.

2. **T1:5–6** (pod emw1e4embiwe9b, the H100 SXM of d5d08fa; the seat's answers of 2026-11-18, second sitting, §1.3 items 2–3). CONFIRMED. d5d08fa's subject names this box. The seat's raw has "(second sitting)" at :3, item 2 (the run of record) at :21 and item 3 (the diagnostic) at :22.

3. **T1:6 "No lock is in force".** CONFIRMED. `git ls-files 'LOCK-n*'` is empty, and the seat places ADDENDUM-n2 "before LOCK-n v0.1" (:9, :26).

4. **T1:7–8 and T2:6–7** (a fresh copy at ad856f0, clean, nothing extracted over it; the driver is HEAD's bytes). CONFIRMED by run3_out:1–4 and :51, and by run3_run item 4.

5. **T1:9–11** (the diagnostic ran in a second copy at ad856f0 after the run had ended; nothing was resumed). CONFIRMED by diag_run :1–3 and :8–11, its items 2–3 (the run's exit file read 0 before launch), and diag_out:1–3.

6. **T1:25 "its 31 capture arrays".** CONFIRMED. `jq '.cells'` shows 31 capture_sha256 keys, 33–63, contiguous.

7. **T1:29–32, the short form** (paused at its end as pre-registered; every step before the reads held; 24 reads, each printed; 10 above TAU and 14 at or below, 7 of them at 0.000000; the end-of-run evaluation fired under p0 = 0 of 2,400, pause p01; nothing resumed). CONFIRMED.
   - Run output: run3_out:57–88. Seat: :7 and :21.
   - p0 and cadence: n_sessions.py:557 (p0_count 0, p0_n 2400, cadence 160).
   - Firing path: runner.py:496–508 (the end-of-run evaluation prints exactly "PAUSE fidelity-binomial at the run's end").
   - Pause id: runner.py:283–285 (ids p{n:02d}). The run started with no report (run3_out:4), so this pause is p01.
   - "Nothing was resumed": run3_run :11 and diag_run :11.
   - I did not read the report's pauses.

8. **T1:33 and T2:13** ("PAUSE (pass)", the seat's §2 convention). CONFIRMED by run3_out:88, bext_run_v3.sh:17–19 and :111–119, and seat :36. See observation 1.

9. **T1:34–37, the diagnostic's short form.** CONFIRMED (items 24 and 27).

10. **T1:38–39, T1:175 and T2:21** (Q1 is p01's adjudication, §1.3 item 4; Q2 is the read of record, §1.4 "the seat decides at the adjudication"). CONFIRMED verbatim at seat :23 and :30.

11. **T1:45–46, the n :130 quote** "the fidelity value against TAU, timing — never a margin". CONFIRMED verbatim against R/PROPOSAL-n-bk-reconciliation-v0_2.md:130, with T1's wrapped lines joined.

12. **T1:46–47 "the run has no pick and no contrast session, so nothing is redacted".** IMPRECISE.
    - The run's stdout carries no margin and no pick (run3_out:57–80; runner.py:483–486).
    - The run's records do carry both. Each holds `margin` and the restricted read with its `pick` (primitive.py:145–159 and :224–233; schema.py:363–364 and :381). They are written to the cell under data/n/ckpt; n :130 says "Margins go to checkpoint files".
    - Fix: "…and the run's stdout carries no margin and no pick (the records' margins and restricted-read picks are in the cell, under data/n/ckpt), so nothing in it is redacted."

13. **T1:48–49** (the report holds the counters §1.3 item 4 names — trials, exceedances at TAU and at TAU/4 — plus p01 and the binomial's state). CONFIRMED by code and keys.
    - runner.py:342–349: binomial_state, and counters.fidelity per cell as {trials, exceed_tau, exceed_tau4}.
    - `jq 'keys'` shows binomial_state, counters and pauses. Seat :23.

14. **T1:50–53** (the diagnostic's files hold no margin, no log-probability and nothing per session; the cell is not for reading, item 2). CONFIRMED.
    - diag_out holds only n, the min/median/max of |cached − fresh|, two counts and the timing. A grep for margin, pick and logprob finds words only (diag_out:47). diag_run is the same.
    - Script: diag script :120–145 and :288–290.

15. **T1:57–84 verbatim block against run3_out:57–80.** CONFIRMED (diff exit 0, 24 lines).

16. **T1:86–88, before the reads.** The claims: the copy was the commit, the root and report absent; manifest 23/23; self-test 344/344; package and closure lines equal to the laptop's before the run; then DRIVER, G-VER PASS, R6's bridge, identifier 8264f719efd347a9 under the 4,096 window, load 12,804 ms. CONFIRMED.
    - run3_out:3–4, :6–28 (23 OK), :32–33, :51, :53 and :56.
    - run3_out:35–48 has the package line and 11 closure lines; bext_run_v3.sh:64–80 starts the run only if they are equal.
    - See observation 7 on order.

17. **T1:89–92, the counts by tool.** CONFIRMED by awk over run3_out:57–80 with TAU = 0.017883544377937845 (schema.py:248).
    - Above TAU: 10, at launch indices 1, 4, 7, 8, 10, 14, 16, 19, 20 and 23; the largest is 0.086070.
    - Above TAU/4 (0.0044709): 15.
    - At 0.000000: 7. Nonzero below 1e-5: 0.000003 and 0.000001.
    - The printed >/<= marks agree (10 and 14).

18. **T1:93 and T2:10–11** (reads 0 and 1 repeat the smoke's 0.014660 and 0.086070; 0eb7671). CONFIRMED by R/results/raw/2026-11-18_n-step4_bext-box2_out.txt:56–57 (s=0 and s=5), committed at 0eb7671 (git log).

19. **T1:94–95 and T2:12** (the end lines; the report's end_state PAUSE; identity lines equal step 3's). CONFIRMED by run3_out:81–82 and :86–87. hashes.txt and run-identity.txt both hash to 93783db0…7b36, which equals bext_hashes_v3.txt.

20. **T1:96** (each read's ms, both paths: min 630, median 657.0, max 973). CONFIRMED.
    - By awk: the median is the mean of the 12th and 13th sorted values, 657 and 657.
    - primitive.py:206–208 and :283–284: duration_ms spans the prefill, the continuations and both full forwards. Every read was re-computed (each line prints a numeric fid).

21. **T1:100–116 verbatim block against diag_out:37–49.** CONFIRMED (diff exit 0, 13 lines).

22. **T1:118–120, the diagnostic before the reads** (the copy was the commit with exactly the diagnostic untracked; manifest 22/22; self-test 30/30; run.txt by path is e4e1c810…e378 and equals the run's output lines 50–83; one load of 31,053 ms; the bridge held). CONFIRMED.
    - diag_out:3, :5–26 (22 OK), :28–29, :31 and :34–36.
    - cmp of S/step4b/run3/out/run.txt against run3_out:50–83: exit 0, 34 lines.
    - The diag script checks the bridge before and after the load (:175–176, :186–187).

23. **T1:121–124, the two paths.** CONFIRMED against primitive.py:113–120, :294–300 and :324–353.
    - prefill runs with keep=1; its last-position row predicts token 0.
    - continue_label is one forward over the label's tokens but the last, through the cache. Row j predicts token j+1, and the cache is cropped back afterwards.
    - full is one uncached forward over ids + label[:-1]; row i predicts token i.
    - Every "bare" label has 3 tokens (jq), so there are two continuation positions.

24. **T1:125–129 and T2:15–18** (token 0 is equal in all 24 reads for both labels; token 1 medians 0.0031/0.0086 and maxima 0.0375/0.0492; token 2 below 2e-06 in every read). CONFIRMED.
    - Token 0: diag_out:37 and :42 print min, median and max 0. The diag script prints with %.6g (:116), which would show any nonzero value.
    - Token 1 and token 2: diag_out:38–39 and :43–44. The token-2 maxima are 1.44522e-06 and 1.81453e-06.

25. **T1:130 "The rest summed is token 1's to within 1e-06."** FAIL.
    - The two maxima for S differ by 1.5e-06: token 1 is 0.0375112, the rest summed 0.0375097 (diag_out:38 and :41). The other five pairs are within 3.6e-07.
    - The rest summed is the absolute value of the sum over t ≥ 1 of (cached_t − fresh_t) (diag script :130–132). Per read it can differ from token 1's value by at most token 2's, whose maxima are 1.44522e-06 (S) and 1.81453e-06 (U).
    - Fix: "The rest summed is token 1's to within 2e-06 (token 2's size)."

26. **T1:131–133, the first token.** The claims: it is the same id in all 12 "bare" labels; labels.json counts 1, 12 and 10 distinct ids at tokens 0, 1 and 2; on the cached path it is one prefill row for both labels; its fresh value is identical in 24 of 24; it cancels in both margins. CONFIRMED.
    - jq over R/data/n/ids/labels.json, candidate "bare": 12 labels, lengths [3], distinct ids 1/12/10. No id was printed.
    - primitive.py:133–135 and :219–233; diag_out:47.

27. **T1:134–135, T1:37 and T2:19** (rel equals the run's fid to six decimals in 24 of 24 reads). CONFIRMED by diag_out:48 and diag script :106 and :137.

28. **T1:139–143** (two additions, the two counts and the timing line; §1.4 asks for the fresh path's cost; the records carry duration_ms_fresh, closed under item 2). CONFIRMED.
    - The diag script marks both additions "Code's addition" (:21–26). Seat :30. primitive.py:281.
    - The coordinating session's OK: item 61.

29. **T1:144–145** (Code's reading: a cell of fewer than three reads prints its count only; every cell here has n 24). CONFIRMED by diag script :27, :52 and :113–117, and diag_out:37–46.

30. **T1:146–150, T1:183–184 and T2:20** (the fresh pair's median 357.1 against the cached read's 309.0, about 1.16; maxima 387.2 and 601.4; the stage's median 657.0). CONFIRMED.
    - diag_out:49. 357.1/309.0 = 1.1557.
    - diag script :92–99: the cached read is the prefill plus two continuations; the fresh pair is two full forwards.
    - The stage median: item 20.

31. **T1:153–154 "Item 2 lists any unpruned find among the forms barred over those files".** CONFIRMED against the list of record v2, item 2 ("Metadata: … any unpruned `find` …"). The event itself: item 62.

32. **T1:155–156** (the pod session's departures: none; its first ship stopped at its own check because the folder name was in use, and it renamed the folder in its scripts; its record, item 1). CONFIRMED by diag_run :21–24. Neither pod record names a departure (a grep for depart, deviat and disclos finds nothing).

33. **T1:160 and T1:172–173** (§1.3 item 4: "cleared as the measurement, or a defect named"; the ruling's sha256 enters the report; the resume `--resume --ruling p01=PATH` completes skip-only; it prints the distribution and ADDENDUM-n1 §2's comparison). CONFIRMED verbatim at seat :23. See observation 5.

34. **T1:163–164** (the end-of-run evaluation is the only one a 24-read stage reaches; p0 = 0 of 2,400 is BK's rate on BK's hardware, n §2.1; 10 of 24 reads exceed TAU). CONFIRMED by runner.py:33–41, cadence 160 (n_sessions.py:557), seat :15 and :32, and PROPOSAL-n:77.

35. **T1:165–170** (reads 0 and 1 repeat; the diagnostic reproduced all 24; token 0 agrees exactly, token 1 carries the discordance, token 2 nearly none; the seat's §1.1 reading puts it in the continuation tokens). CONFIRMED by items 18, 24 and 27, and seat :15. See observation 4.

36. **T1:171 "Seven reads have no discordance at all, and ten exceed TAU."** FAIL.
    - The seven reads print fid 0.000000, which means rel is below 5e-7 at six decimals (runner.py:484–485; schema.py:529–536).
    - The diagnostic shows nonzero per-token discordance in every one of the 24 reads. The token-1 minimum is 1.38117e-07 nats for each label; the token-2 minima are 3.14713e-09 (S) and 1.06959e-09 (U) (diag_out:38–39 and :43–44).
    - T1:31 states this correctly. See observation 9.
    - Fix: "Seven reads print fid 0.000000 (rel below 5e-7), and ten exceed TAU."

37. **T1:178–182** (the §1.4 quote with "…"; the quantity is unchanged, the margin at the choice position under the steered-span mask; the implementation would depart from BK's). CONFIRMED verbatim at seat :30. The "…" stands for "— one full forward per label under the identical mask, the computation BK's own identity check calls the reference —". See observation 4.

38. **T1:188–189 "The steps before the reads, in both runs: the copies, the manifests, the self-tests (344/344 and 30/30), the hashes, G-VER and R6's bridge".** IMPRECISE.
    - G-VER ran only in the run of record (run3_out:52–53). The diagnostic runs none: run() at diag script :148–196 has no G-VER call, and diag_out has no G-VER line.
    - The diagnostic's hash step hashes the run's stdout (diag_out:30–31), not the package and closure lines.
    - Fix: "… the self-tests (344/344 and 30/30), the run's package and closure hashes and its G-VER, the diagnostic's hash of the run's stdout, and R6's bridge in both."

39. **T1:190–191 and T2:22–23** (the report's cells record has json_sha256 80770a19…78ea, equal to the copied cell's sha256, and 24 records). CONFIRMED by `jq '.cells'` and shasum of the cell.

40. **T1:192–193** (the capture arrays stay on the box's volume, their digests in the committed cell). CONFIRMED as to code and record.
    - cells.py:5 names the arrays `<stem>.L{layer}.npy`; cells.py:239 puts capture_sha256 in the cell; runner.py:331–332 copies it to the report.
    - R/RESULTS.md:977; run3_run items 7–9 (the stage's root is left on the box).
    - The attribution to the coordinating session and v1's plan: item 61.

41. **T1:194–195** (the box stays up through the resume on the PI's standing word, §5; both copies and their work folders are left in place). CONFIRMED by seat :56, run3_run item 9 and diag_run item 7.

42. **T1:199–209, the paths and line counts** (88, 94 and 51 lines). CONFIRMED by wc -l. The new raw names are unused in the tree (git ls-files), and T3:7 names the script raw the same way.

43. **T1:210 "its laptop self-test".** IMPRECISE. T3 holds both the laptop run and the box's step-2 lines; T3:1 says "its self-test, on the laptop and at the box".
    - Fix: "its self-test raw (the laptop's run, the box's lines beside it)".

44. **T1's form against R/WORKFLOW.md §4 (:32–37).** CONFIRMED.
    - Path form: `<date>_<topic>_code-to-design_STOP.md`.
    - Header: the session, the PI date and "For the PI to route."; what ran, with the lock (none) and the driver and scripts by hash; the sources read and not opened, by sha256.
    - Body: the short form; the reads in m:271's form (PROPOSAL-m v1.11:271, the pre-VERDICTS read rule); the declared items, with departures and their class; Q1 and Q2, each with readings to weigh; Not questions; "Code adjudicates nothing".
    - T2:4 says "STOP for the seat's read", as §4's first bullet requires.

45. **Adjudication check (T1, T2).** CONFIRMED. Neither text rules on p01 or the read of record, and neither states as ruled anything the seat did not rule. Observations 1, 4 and 5 note readings phrased as findings.

### T2

46. **T2:1–5, the heading and block link.** CONFIRMED. The link path equals T1's path of record (T1:199); the facts are those of items 4–8.

47. **T2:6–13.** CONFIRMED (items 4, 7, 8 and 16–19).

48. **T2:14–20.** CONFIRMED (items 5, 22, 24, 27 and 30).

49. **T2:24–25.** CONFIRMED: its departure line agrees with T1:152–154. The event itself: item 62.

50. **T2:26–27 "two loads on the box".** CONFIRMED. Each output has one "Loading weights" line (run3_out:54, diag_out:34) and one load (run3_out:56, diag_out:36). The laptop half: item 62.

51. **T2:29–37, the committed-by-path list.** CONFIRMED: it equals T1 §8.

52. **T2 against T1 overall.** CONFIRMED. No figure or attribution differs, and T2 repeats neither of T1's two FAIL sentences.

### T3

53. **T3:1–8.** CONFIRMED. The diagnostic's sha256 is exact. The script's docstring (:7) says never of record, no package change, writes nothing. The box's manifest checked the 14 package modules at ad856f0 (diag_out:7–20).

54. **T3:10–14.** CONFIRMED where checkable.
    - Model-free over the numpy double: diag script :205–208, :237 and :244.
    - S/step4b/diagov/scripts/n_sessions.py is 18f19b8e…4f5c, and scripts/n_bext_diag.py is c0ac67e4…08d1.
    - diagov's 14 valence_core/n modules are byte-equal (cmp) to ad856f0's. valence_core/n is unchanged from dc6a1cf to ad856f0 (git diff --name-only), and its package line is f927608c…3c03 (run3_out:35).
    - diagov's results/raw/2026-11-18_respawn_determinism.txt and scripts/box_e0_corpus.py are byte-equal to dc6a1cf's.
    - primitive.py:45–57 admits an importer at scripts/n_*.py.

55. **T3:19–20.** CONFIRMED. Line 20 without its 5-space indent is byte-equal (cmp) to S/step4b/diag/selftest_run1.txt, whose whole output is that one line. selftest_run1.exit reads "exit=0".

56. **T3:22–26.** CONFIRMED. Lines 24–26 without the indent are byte-equal (cmp) to diag_out:27–29. This is step 2 of bext_diag_v1.sh (:53–57); the pod and the copy are as in diag_run :1–3 and item 2.

### T4

57. **One inserted block, nothing else changed.** CONFIRMED. The diff is "282a283,295": 13 new lines (4 comment lines, 8 patterns, 1 blank), with no trailing whitespace (cat -et).

58. **It admits exactly data/n/reports/backend-ext.json and data/n/ckpt/backend-ext/N1-V__none__0.json.** CONFIRMED from the patterns:
    - data/n stays re-included (`/data/*`, then `!/data/n/`), and `/data/n/*` still ignores every child.
    - `!/data/n/ckpt/` re-includes that directory only, and `/data/n/ckpt/*` re-ignores everything in it.
    - `!/data/n/ckpt/backend-ext/` re-includes one subdirectory, and `/data/n/ckpt/backend-ext/*` re-ignores everything in it: arrays, temporaries, subfolders and dotfiles.
    - Only the literal `!/data/n/ckpt/backend-ext/N1-V__none__0.json`, which has no glob character, re-includes a file.
    - The reports lines work the same way: `!/data/n/reports/`, then `/data/n/reports/*`, then `!/data/n/reports/backend-ext.json`.
    - No later pattern names data/n; only the mf3 and p blocks follow.
    - Nothing is tracked under data/n/ckpt or data/n/reports now (git ls-files count 0), and neither directory exists in R.

59. **T4's comment attributions.** CONFIRMED.
    - "n v0.2 §3 G-ACQ": PROPOSAL-n:109, the BACKEND extension.
    - "§1.3 item 2": the run of record.
    - Written on the box by the run of record: bext_run_v3.sh:4–6.
    - One cell: `jq '.cells'` has one entry.
    - .npy arrays with their digests in the cell: cells.py:5 and :239.
    - "Record, not cache (ledger 27)": CLAUDE.md ledger 27.
    - "copied back by hash" and "as v1's plan had it and the coordinating session ruled": items 61–62 and observation 6.

### NOT CHECKABLE

60. **The PI's words:** "Route as given" (T1:6, T2:4).

61. **The coordinating session's OKs and words:**
    - the diagnostic's two additions (T1:139);
    - the capture arrays' disposition and "v1's plan" (T1:193 and T4's comment); `git grep "v1's plan" -- . ':!data/**'` finds no committed text on it;
    - the battery window (T3:11);
    - the disclosures made to it (T1:154, T2:25).

62. **Code's own conduct:**
    - reading only the report's cells record (T1:18–19, :49, :191; T2:22);
    - the cell hashed only (T1:24);
    - nothing under data/mf3 opened (T1:25);
    - the unpruned find and what it printed (T1:152–154; T2:24–25);
    - the copy-back by hash (T1:24; T4's comment);
    - the overlay's construction and the laptop command (T3:12–13, :15–18);
    - "On the laptop, nothing ran on a model" (T2:26–27).

63. **"Nothing is pushed" / "Not pushed"** (T1:211, T2:37), for a commit not yet made. See observation 3.

## Observations

1. **The scope of the seat's §2 convention.** Its sentence speaks of "a smoke that ends PAUSE …", while its scope is "this stage and … any stage whose smoke can reach a monitor". Box script v3 (:17–19) restates the convention as "a run that ends PAUSE". T1:33's attribution is therefore a reading of "for this stage" for the run of record, which the seat may confirm.

2. **No -diff rule for data/n/ckpt/.**
   - `git check-attr -a` reports no attribute for data/n/ckpt/backend-ext/N1-V__none__0.json, while data/m/ckpt/… and data/p/ckpt/… report "diff: unset" (HEAD:.gitattributes:6, :10, :14).
   - By the code, the cell's 24 records carry the margin, the log-probabilities and the restricted read's pick (schema.py:363–364 and :381; primitive.py:224–233). Under n :130, nobody sees margins before VERDICTS.
   - These d = 0 reads are the same computation, on the same box, as the campaign's N1-V d = 0 reads of those 24 sessions.
   - As drafted, any git show, git diff or git log -p of the commit would print those fields. A `/data/n/ckpt/** -diff` line in m:318's form, as m, mf3 and p have, or the seat's word, before the cell is committed, would close this.
   - This is not a claim in T1–T4; T4's admits are as stated.

3. **origin/main is already at ad856f0.** git rev-parse shows it, and its reflog subject reads "update by push", although ad856f0's own message ends "Not pushed." T1:211 and T2:37 speak of the new commit only.

4. **Readings phrased as findings.** T1:166 "So the discordance is a deterministic property of the two paths on this box" rests on reproduction to six decimals of rel. T1:178 "The condition §1.4 sets is met" is borne out by the data, but §1.4 leaves the decision to the seat. Writing "Code's reading:" or "reproducible to six decimals" would mark them as readings.

5. **"each ruling" (T1:172).** §1.3 item 4 names the ruling's sha256 and the resume without telling "cleared" apart from "a defect named". "each" is the literal reading.

6. **"ruled" against "word".** T4's comment says "the coordinating session ruled"; T1:193 calls the same thing "the coordinating session's word". The two texts could use the same word; in WORKFLOW §2 the rulings are the seat's.

7. **Order of the bridge and G-VER.** T1:87–88 and T2:8–9 list "G-VER PASS, R6's bridge" in the output's printed order. In the driver, the pre-load bridge check (n_sessions.py:855) runs before G-VER (:874), a second check follows the load (:884), and the line reporting both prints after the load (:888). This is accurate as the printed order.

8. **Source of the cost figure.** §1.4 names the records' duration_ms_fresh as the source. T1 §4 uses the diagnostic's own timing instead, declared as an addition, with the records kept closed under item 2. The seat may want the records' figure at the adjudication.

9. **Why fid prints 0.000000 despite nonzero per-token discordance.** The token-1 minimum is identical for S and U (1.38117e-07). That fits T1 §3's description of the paths: on each path, the row that predicts token 1 takes the same input, the shared first token, for both labels. Per-label differences can therefore cancel in the margin, which explains fid 0.000000 alongside nonzero per-token discordance (item 36).

## Commands run, and departures

**Command classes:**
- shasum -a 256: on the drafts, the sources, the frozen scripts and manifests, and R files; on the report and the cell by explicit path only.
- jq: on the report, only `jq 'keys'` and `jq '.cells'` (the latter's output counted with grep and awk). On R/data/n/ids/labels.json, structure and distinct-id counts only, with no id printed.
- Read-only text tools on files outside ckpt and reports: cat -n, cat -et, sed -n, awk, cut, tr, fold, sort, uniq, head, tail -c, od -c, wc -l; diff and cmp with process substitution; /usr/bin/grep on single named files only; the Read tool on the drafts, sources and R files.
- Names-only ls: S/step4b, and its rec_commit, run3, run3/out, run3/frozen, diag, diag/out, diag/frozen and diagov folders (diagov with three of its subfolders); R/data/n.
- git, read-only: rev-parse; branch --show-current; show <rev>:<path> (compared or hashed, with only .gitignore and .gitattributes printed); hash-object; status --porcelain on named paths; log with --format of ids, parents, dates and subjects; reflog show origin/main with --format of ids and subjects; diff --name-only; show --name-only; ls-files; one grep with ':!data/**'; check-attr -a.
- Shell builtins only otherwise.

**What I did not do:**
- No Python, no model, no network, no ssh.
- No file written by me.
- Nothing listed, found or grepped under S/step4b/run3/rec/.
- Nothing under data/mf3 listed or read.
- No size or time of any ckpt or reports file.
- No guard marker in any argv.

S/step4b/diagov (Code's self-test overlay, which is not in the brief's source list) was used for names, hashes and cmp only, to check T3:10–14.

**Departures:**

(a) **A loop over an unseen glob.** I ran `for f in valence_core/n/*.py` in S/step4b/diagov in the same command as the names-only ls of that folder, so I had not seen its expansion before it ran. It expanded to the 14 package module names, none holding a marker (its output lists them). The brief bars loops over globs that may expand to such a name. My shasum over globs in run3/out, run3/frozen, diag/out and diag/frozen ran only after names-only listings of those folders had shown no marker names.

(b) **git commands that took paths without item 3's pathspec:**
- git status --porcelain on named files (twice);
- git log --format='%h' on three named raws;
- git ls-files with 'PROPOSAL-m*', 'LOCK-n*', 'ADDENDUM-n*' and 'results/raw/2026-11-18_n-step4*';
- git ls-files on data/n/ckpt and data/n/reports (count 0) and on data/n/ids (count 6);
- git check-attr -a on four literal paths: the two new data/n paths and two made-up data/m and data/p ckpt names.

Each named explicit or root-anchored non-data paths, or printed only a count or attributes. Nothing under data/*/ckpt or data/*/reports was named, beyond that count of 0.

(c) **A wider exclusion than needed.** git diff --name-only dc6a1cf ad856f0 used the ckpt/reports exclusion where ':!data/**' fitted, since nothing under data/ was wanted. It printed no data/ path.

(d) **A harness-saved output.** The harness saved the long output of one command (cat -n of R/valence_core/n/primitive.py) to its own tool-results folder, outside R and S, and I then read it there. That file was written by the harness, not by me.
```
