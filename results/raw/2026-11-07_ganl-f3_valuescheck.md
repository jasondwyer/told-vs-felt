# Blind values-check: G-ANL-F3, the canonical run's entry and raw (2026-11-07)

Checked: ENTRY `<scratch>/ganl/entry_ganl.md` (40 lines) and RAW `<scratch>/ganl/2026-11-07_ganl-f3.txt` (540 lines; to be committed as `results/raw/2026-11-07_ganl-f3.txt`), against HEAD `9480f9b`, the artifact `data/m/gates/G-ANL-F3.json` (untracked), the test copy `<scratch>/ganl/regen/G-ANL-F3.json`, the pre-scrub raw `<scratch>/ganl/ganl_raw.txt` (531 lines) and `<scratch>/ganl/regen_out.txt` (529 lines). `<scratch>` is this session's scratchpad directory.

Anchors: entry:N, raw:N (the scrubbed raw), pre:N (pre-scrub), regen:N, and `m_analyze.py:N` at HEAD `9480f9b` (blob `d347ea0c…5e48`).

## Items

1. **Artifact sha256, "`b91a8c67…936c`" (entry:2, :37) and in full (entry:24).** PASS.
   - `shasum -a 256 data/m/gates/G-ANL-F3.json` gives `b91a8c672e85f1d493444c6b6388588ab0a646a8c36971320421c9f03aef936c`.
   - The driver's own line prints the same value (raw:531, pre:530).

2. **"81,161 bytes" (entry:24).** PASS. `wc -c` gives 81161 for the canonical file and for the test copy.

3. **Analyzer "`d347ea0c…5e48`" (entry:3, :27).** PASS.
   - The working-tree file and `git show HEAD:scripts/m_analyze.py` both hash to `d347ea0c9b69f73ced13484f3683f0b52f79a826cc9963a81359b2adc2205e48`.
   - The artifact's `analyzer.sha256` is the same, and pre:1 recorded it at the start.

4. **m's `package_sha256` "`7756dcf4…49bb`" (entry:27).** PASS.
   - `valence_core.m.resume.package_sha256_of(REPO/"valence_core/m")` gives `7756dcf42532b222b50e3bd8f41e2dc20053fa0a7a2b60e033dda559666349bb`.
   - The same recipe (resume.py:328) over HEAD's 18 blobs via `git show` gives the same value.
   - It equals the artifact's `package_sha256`.

5. **Base closure "`a3bc7bb9…b22b` (15 modules)" (entry:27–28).** PASS.
   - `closure()` (m_analyze.py:1828) gives 15 modules plus 1 data file (`data/olmo/a1_repair_roster.json`). Its sha256 is `a3bc7bb9df3d8361bfa803238e61a61a7eef76a6d839540413e53cd7919cb22b`.
   - That equals the artifact's `closure` and `closure_sha256`. The sha256 recomputed from the artifact's own map is the same, and so is `RECORD_CLOSURE_SHA256` (m_analyze.py:129).

6. **Q-F3 closure "`d19f336d…f039` (22 modules)" (entry:28).** PASS.
   - `closure(lazies=LAZY_VERDICT_MODULES + LAZY_F3_MODULES)` gives 22 modules (the 15 plus 7 mf3 modules) and the same single data file.
   - Its sha256 is `d19f336dc69e987b7be0b69d84d32f4a55cc47c8f4728c0f13b0378608cbf039`, equal to `g_anl_f3.f3_closure` / `f3_closure_sha256`.

7. **Proposal "`42ab36ec…6c6b`" (entry:29).** PASS. The working tree, HEAD, the artifact's `proposal.sha256` and `PROPOSAL_SHA256` (m_analyze.py:98) all give `42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b`. The battery line raw:5 agrees.

8. **ADDENDUM-m1 "`ea08322d…9001`" (entry:29).** PASS. The working tree, HEAD, `g_anl_f3.addendum.sha256` and `ADDENDUM_M1_SHA256` (m_analyze.py:137) all give `ea08322d601011923524021832d27d0ddf57b3e51ee4d88f265985c6c9bf9001`.

9. **Placeholder "`44f1a2d4…0af9`" (entry:29).** PASS. `data/m/gates/m_posting_sentences.placeholder.json` hashes to `44f1a2d42064fd1bb295b5988082619316fb3db8a200792147f5e4e854db0af9` in the working tree, at HEAD and in the artifact's `placeholder.sha256`.

10. **v2 placeholder "`cd3df574…d240`" (entry:30).** PASS. `data/m/gates/m_posting_sentences.placeholder-v2.json` hashes to `cd3df57495588bfa473d583210f20b696570f537a02264ee4cb806580506d240` in the working tree, at HEAD and in `g_anl_f3.placeholder_v2.sha256`.

11. **Flag of record, `G-CAL_model-free.json` "(`aad8096a…34af`), value true" (entry:31).** PASS.
    - The file hashes to `aad8096a6aa90ebb6e4bd476e47a9cb40d50e666c1801270031b899abc1834af` in the working tree and at HEAD.
    - The artifact's `flag_of_record` is {value true, the same sha256, introduced_at bab921c}.
    - The file has schema `m-gcal-model-free-v1` and an `f1_012` block, which is `flag_of_record`'s TRUE condition (m_analyze.py:1750–1782).

12. **Lexicons "`1b7d5a01…8088`" (entry:32).** **FAIL.**
    - `sha256(json.dumps(artifact["g_anl_f3"]["counter_c"], sort_keys=True, separators=(',', ':')))` is `1b7d5a01af967d9f7953168dbce3468c562602b9f754069041f32b740d088028`.
    - Its last four characters are **`8028`**, not `8088`. The block is pure ASCII, so the value is the same with `ensure_ascii=False`.
    - The scratch LOCK draft (`<scratch>/lock/LOCK-m-F3.draft.md:131`) carries the full value correctly.
    - Fix: `1b7d5a01…8028`.

13. **Preprint "`45b67246…7a41`" as blob, table and tree file; `head_file_is_table` true; "`1523cce`'s blob" (entry:22, :34–35).** PASS.
    - `git show 1523cce:PREPRINT-v1_0-draft.md | shasum -a 256` gives `45b67246f2b2bcb40774e95462ad4e3c5f559fdd0358387cceec0155bebe7a41` (88,668 bytes).
    - The working tree and HEAD give the same value, and so does `preprint.sha256` in `data/m/gates/m_posting_sentences.json`.
    - The artifact's `g_anl_f3.regression.preprint` has `blob_sha256`, `table_sha256` and `head_file_sha256` all equal to `45b67246…7a41`, with `head_file_is_table` true and `commit` 1523cce.

14. **"The two passes over those evaluations hash to `83df98b12a27be8e…`, as in the BUILD's self-test (`e0b4f2c`)" (entry:35–36).** PASS.
    - The artifact's `battery.outputs_sha256` is `83df98b12a27be8e4cd6abee6db7145599774d68ed7bb9b2675fa674de3b813c`.
    - raw:241 (STR-DETERMINISM) prints `83df98b12a27be8e`, and `git show e0b4f2c:results/raw/2026-11-06_ganl-f3_build_selftest.txt` prints the same at its line 252.
    - "Those evaluations" is accurate. `_bt_tuple_pass` (m_analyze.py:5834) hashes `v1_outputs(t, reasons_all, flag, table)` over the same 1,080 tuples × 2 flags, with the same clock:pi-declined reasons, that `_bt_v1_unchanged` (:9932) compares.
    - Structure note only: the bullet hangs `v1_unchanged` and `battery.outputs_sha256` under "the regression's preprint block", but they are separate fields.

15. **G-SHAPE artifact shas "`38ba8e28…`" and "`0c9de56e…1461`" (entry:12–13).** PASS.
    - Working tree and HEAD agree: `G-SHAPE-F0.json` is `38ba8e28cc37e73d0ff387b458529f82f3c54cf35ccc5a3bf223a0a934553b51` and `G-SHAPE-F3.json` is `0c9de56e17d0872851f941473933c4811a79e754cfd99ebcdf589ca5f4e91461`.
    - The messages of 0786c11 and f9700ba cite `38ba8e28...3b51` and `0c9de56e...1461`.
    - Format note: F0's sha is given as a prefix only, F3's as first8…last4.

16. **"525 of 525 checks pass (`EXPECTED_CHECKS` 525; a skipped assertion is a failure)" and "525/525" (entry:3, :21, :37).** PASS.
    - raw:529–530 and regen:526–527 say so, and `EXPECTED_CHECKS = 525` (m_analyze.py:4903).
    - The artifact's battery has checks_pass = checks_total = expected_checks = 525.
    - The pre-scrub raw holds 525 `[PASS]` lines and 0 `[FAIL]`.

17. **"all 538 coverage ids" (entry:3, :21).** PASS.
    - raw:528 says so.
    - `_REQUIRED` has 538 entries, all distinct.
    - The artifact's `battery.coverage_ids` has 538 entries, equal to `sorted(set(_REQUIRED))`.

18. **"The v2 space's 519,480 tuples are each asserted (481 × 5 × 216)" (entry:21).** PASS.
    - 481 × 5 × 216 = 519,480, and 300,625 + 218,855 = 519,480.
    - raw:493 reads "per flag value 300625 + 218855 = 519,480 tuples, every one asserted (481 x 5 x 216)".
    - The count is per flag value: each tuple is asserted under both values (2 × 519,480 tuple-evaluations). The entry therefore understates rather than overstates.

19. **"2,160 of 2,160 evaluations equal" (entry:35).** PASS.
    - The artifact's `g_anl_f3.v1_unchanged` is {evaluations 2160, equal 2160, distinct_reason_equal 2160, tables_equal true}.
    - `battery.evaluations` is 2160, and raw:462 agrees.

20. **"42 file entries (sources, import closure, tooling)", "52 (sources, import closure)" and "the 94 entries" (entry:12–14).** PASS.
    - G-SHAPE-F0's provenance has sources 26 + import_closure 14 + tooling 2 = 42.
    - G-SHAPE-F3's provenance has sources 38 + import_closure 14 = 52. It has no tooling key; its tooling file, `scripts/mf3_sessions.py`, is in sources.
    - 42 + 52 = 94.

21. **"Neither map lists `scripts/m_analyze.py`" (entry:12).** PASS. No key of either map contains "m_analyze", and neither artifact's text contains that string anywhere.

22. **"Every one of the 94 entries' recorded sha256 equals HEAD's blob and the working tree at `9480f9b`" (entry:14).** PASS.
    - `<scratch>/vc/gshape.py` checked all 94: recorded = sha256(working tree) = sha256(`git show HEAD:`) = sha256(`git show <run commit>:`). There were 0 mismatches.
    - Beyond the 94, G-SHAPE-F3's `m_module_sha256` (11 entries) and both recorded package shas (m `7756dcf4…`, mf3 `f30ad505…`) also equal today's values.

23. **"No file either map lists changed between its run's commit (`0786c11`, `f9700ba`) and `9480f9b`" (entry:14–15).** PASS.
    - `git diff --name-only 0786c11 HEAD -- <F0's 42>` and `git diff --name-only f9700ba HEAD -- <F3's 52>` are both empty.
    - `git log <c>..HEAD -- <files>` lists no commit for either: no commit touched any of the files, so there was no change at all, not merely no net change.
    - Both artifacts are themselves unchanged since their commits. `git diff 993eba1 HEAD -- <files>` (the tree both runs ran on) is also empty.

24. **"before anything ran … So neither gate re-runs" (entry:10, :16).** PASS.
    - The seat's rule (answers.md:11) re-runs a gate only if its map lists `m_analyze.py`, and neither map does (item 21).
    - The timing is a self-report (raw:3) that cannot be reproduced after the fact. Its result reproduces at HEAD.

25. **Quote: "the check fix → N1 → the canonical `ganl` on that HEAD → LOCK-m-F3 v0.1 → G-TIME-F3" (entry:7).** PASS.
    - It is a byte-equal substring of `results/raw/2026-11-07_n1-battery_design-to-code_answers.md:11`, in §1 ("## 1. The order: (b)").
    - The bold "Order:" and the final period lie outside the quote.

26. **Quote: "N1 before `ganl` so that `G-ANL-F3.json` records the restored tree" (entry:7–8).** PASS. It is byte-equal to answers.md:11 in §1.

27. **Quote: "Code checks whether either G-SHAPE map lists `m_analyze.py` before running anything; if one does, that gate re-runs once more on the final HEAD" (entry:10–11).** PASS. It is byte-equal to answers.md:11 in §1.

28. **"The seat's answer of 2026-11-07 on N1 (…, §1, at `f105bdd`)" (entry:5–7).** PASS.
    - answers.md:3 reads "PI date 2026-11-07", and the title is "N1 against F3R-PREPRINT-OF-RECORD".
    - All three quotes are in §1 (:9–13).
    - `git log -- <path>` lists only f105bdd, which adds the file (31 lines). Its sha256 is `6b711d94…b409`, as f105bdd's message states.

29. **"The check fix is `10a2bbb`" (entry:8).** PASS.
    - Its subject is "G-ANL-F3 -- the check fix, order (b) …".
    - It changes `scripts/m_analyze.py` (26 lines), RESULTS.md and two raws.
    - It is 9480f9b's parent.

30. **"N1 is `9480f9b` (the coordinating session's commit)" (entry:8–9).** PASS.
    - Its subject is "N1 -- the preprint's bytes of record restored, its status banner moved to a sidecar …".
    - The attribution comes from 10a2bbb's message and RESULTS.md:128 ("N1, which is the coordinating session's commit"). Git metadata cannot attest which session made a commit: every commit has the same author.

31. **f105bdd committed the seat's answer (entry:6–7).** PASS. `git show --stat f105bdd` shows RESULTS.md and `results/raw/2026-11-07_n1-battery_design-to-code_answers.md` (+31).

32. **"the BUILD's self-test (`e0b4f2c`)" (entry:36).** PASS. Its subject is "G-ANL-F3 -- BUILD (m:291; ADDENDUM-m1 s2.5; …)". It adds `results/raw/2026-11-06_ganl-f3_build_selftest.txt` (541 lines; :540–541 read 525/525).

33. **"(`9480f9b`, tracked files unmodified; Code stamp 2026-11-07 23:34:27 UTC at the start)" (entry:17; raw:2).** PASS.
    - pre:1 reads "# STAMP 2026-11-07 23:34:27 UTC HEAD 9480f9b analyzer d347ea0c…".
    - pre:2 reads "# tracked changes before the run: []".
    - `<scratch>/ganl/run_ganl.sh` writes both lines (`date -u`; `git status --porcelain --untracked-files=no`) before it invokes the driver.
    - The artifact's mtime, 18:37 local (23:37 UTC), is consistent. Today there are still 0 tracked changes, at HEAD 9480f9b.

34. **The pre-battery check: "committed at HEAD with identical working-tree bytes (PIN-39 widened, PIN-V2-23): the analyzer, both placeholders, the proposal, ADDENDUM-m1, `valence_core/m/*.py`, `valence_core/mf3/*.py`, and both closures' modules and data" (entry:18–20).** PASS.
    - On the canonical path, `run_ganl` (m_analyze.py:11073) calls `ganl_commit_problems` (:11059–11070) at :11088, and refuses with exit 2 before `battery()` (:11110).
    - Its base list (PIN-39): the analyzer, the placeholder, the proposal, `valence_core/m/*.py` (18 files), and the base closure's 15 modules and 1 data file.
    - Its PIN-V2-23 additions: the v2 placeholder, ADDENDUM-m1, `valence_core/mf3/*.py` (15 files), and the Q-F3 closure's modules and data not in the base (7 mf3 modules, 0 data).
    - It matches the code comments (:11077–11086) and the PIN-V2-23 register text (:4527–4529, "PIN-39 widened to the v2 placeholder, ADDENDUM-m1, valence_core/mf3/*.py and the Q-F3 closure"). It also matches the PIN-39 register text (:4758–4761).
    - `stages._committed` (stages.py:415) requires that HEAD hold the path as exactly one regular blob and that the working-tree bytes equal it.
    - Re-run now, `ganl_commit_problems(_prod_committed, closure(), closure(lazies=…))` returns []. An independent comparison of every listed path (61 entries, 54 distinct), working tree against `git show HEAD:`, found 0 differences.

35. **"The battery's own check finds that it wrote nothing canonical" (entry:21).** PASS.
    - raw:527 reads "[PASS] the battery wrote nothing canonical (data/m before == after; blocked dirs by os.stat only) []" (m_analyze.py:11039, STR-NO-CANONICAL-WRITE).
    - Its snapshot (`_bt_snapshot`, :5149–5165) covers both data/m and data/mf3, which is wider than the label's "data/m".

36. **"`F3R-PREPRINT-OF-RECORD` reports `('45b67246…', '45b67246…', True)`: the regression is served by `1523cce`'s blob, and the file in the tree is the table's" (entry:22–23).** PASS.
    - raw:452 prints `('45b67246f2b2bcb4', '45b67246f2b2bcb4', True)`: 16-hex prefixes, which the entry elides to 8.
    - At m_analyze.py:9983–9988, the tuple is (blob_sha256[:16], head_file_sha256[:16], head_file_is_table). The check asserts only blob = table, and it carries the coverage id F3R-PREPRINT-OF-RECORD.
    - The blob is read at `REGRESSION_PREPRINT_COMMIT = "1523cce"` (:9854). `head_file_sha256` hashes the tree's file (`head_pre = REPO / pre["path"]`, :9891).

37. **"written (no file existed before)" (entry:24).** PASS.
    - raw:531 and pre:530 read "G-ANL-F3: written: data/m/gates/G-ANL-F3.json …".
    - `write_texts_once` (m_analyze.py:1914) returns "written" only when a target is new. An existing identical file gives "identical"; a different one gives a refusal.
    - `run_ganl` prints "NOTE: … exists" for an existing file (:11108), and no NOTE line appears in the raw.

38. **"Schema `m-ganl-f3-v1`, verdict PASS, no timestamp and no HEAD" (entry:24).** PASS.
    - The artifact has schema `m-ganl-f3-v1` (= `GANL_F3_SCHEMA`, m_analyze.py:4443), verdict `PASS` and stage `G-ANL-F3`.
    - A recursive scan finds no time or stamp key.
    - The text holds no `9480f9b` or `10a2bbb` and no clock time.
    - Its only dates are declared ones: the Clock dates (D1 2026-10-30, D_O′ 2026-11-30, D2 2026-12-22, era boundary 2026-11-05) and record dates (2026-10-10, -14, -19; 2026-11-06).
    - Note: the nested keys `head_file_sha256` and `head_file_is_table` exist. They describe the tree's preprint file, not a commit, so "no HEAD" holds in the sense that no commit of the run is recorded.

39. **"A second run … (`ganl --out`, the same HEAD and tree) writes the same bytes: 525/525, sha256 `b91a8c67…936c`, `cmp` identical" (entry:37).** PASS.
    - My own `cmp` of the two files found them identical: both have sha256 `b91a8c67…936c` and 81,161 bytes.
    - regen_out.txt holds 525 `[PASS]` lines and 0 `[FAIL]`. It reads "525/525" and "written: …/regen/G-ANL-F3.json (sha256 b91a8c67…)".
    - Its battery lines are byte-identical to the canonical run's: a diff of the two bodies, excluding the INVOCATION, written and EXIT lines, is empty.

40. **The scrubbed raw equals the pre-scrub raw except for the header lines and the INVOCATION line's root.** PASS.
    - Compared mechanically (`<scratch>/vc/scrub.py`): pre:3–531, with the repo root replaced by `<repo>`, equals raw:4–532 byte for byte (529 lines).
    - Header pre:1–2 become raw:1–3. Only pre:3 contained a local path.

41. **The last section reflects regen_out.txt faithfully, with only roots scrubbed.** PASS.
    - raw:535 = regen:1 and raw:536–539 = regen:526–529, with the repo root replaced by `<repo>` and the scratchpad root by `<tmp>`. Nothing else differs.
    - raw:540's "IDENTICAL" is confirmed by my own `cmp`.
    - Its "last four lines" include regen's `EXIT=0`, which the wrapper wrote, not the driver; the main section has the same line.

42. **No identifying path survives in the scrubbed raw.** PASS.
    - It contains none of the identifying strings searched for: the home directory's root, the user name, the private and system temp roots, the sandbox user directory, the session id, "scratchpad", "Documents" or "var/folders". (Code reworded this line before the commit so the raw does not name them.)
    - The only path-like tokens are "/A3*]" (raw:147, plain text) and "/outside-the-repository.json" (raw:456, a synthetic battery path).
    - raw:288's `<tmp>` is the analyzer's own scrub, already present at pre:287.

43. **Entry: "(the INVOCATION line's local root scrubbed)" (entry:25).** **IMPRECISE.**
    - The raw scrubs more than that line. In its last section: raw:535 (`<repo>` and `<tmp>`), raw:538 (`<tmp>` in the driver's "G-ANL-F3: written:" line) and raw:540 (`<tmp>`).
    - The entry names only the INVOCATION line. The raw declares only the `<repo>` scrub (raw:2), and raw:534 says nothing of `<tmp>`.
    - Suggest "(local roots scrubbed to `<repo>` and `<tmp>`)" in the entry, and a `<tmp>` clause on raw:534.

44. **Raw:1: "model-free; the synthetic battery only (no checkpoint, no pick)".** **FAIL.**
    - The phrase is carried over from G-ANL-F0 (`results/raw/2026-10-10_m-ganl-f0.txt:1`), where it was true ("The analyzer reads no checkpoint or contrast pick in step 8", `results/raw/2026-10-10_m-steps7-8_build-inputs.md:61`).
    - This battery's A1 regression reads Q-F0's seven released files by committed blob and recomputes Q-F0's VERDICTS from them (raw:450–454). raw:454 says the battery admitted "the campaign, time and qual checkpoints, the decisions, the OLMo states and the two outputs".
    - `data/m/ckpt/Q-F0_campaign.json` carries 1,986 `"pick"` keys. The artifact's `g_anl_f3.regression` has every pin true and both outputs identical.
    - The analyzer's docstring states the same carve-out (m_analyze.py:52–55: "save Q-F0's seven released files, admitted by blob for the regression").
    - So the raw contradicts its own line 454. "Model-free" holds; "synthetic only, no checkpoint, no pick" does not.
    - Suggest: "model-free; the synthetic battery plus A1's regression over Q-F0's seven released files (admitted by blob; no unreleased pick)". The entry does not repeat the phrase.

45. **Raw:534 "(no file was edited between the two runs)" and entry:37 "the same HEAD and tree".** PASS: consistent, though not provable in full.
    - HEAD is still 9480f9b and the tracked tree is clean.
    - The byte-identical artifact binds every hashed input: the analyzer, m's package, both closures, the proposal, ADDENDUM-m1, both placeholders, the flag, the preprint and the 538 ids.
    - An edit-and-revert of an unhashed file between the runs cannot be ruled out after the fact.

46. **"the regression records the restored tree" (entry:3).** PASS.
    - `g_anl_f3.regression.preprint.head_file_sha256` = `table_sha256` = `45b67246…7a41`, and `head_file_is_table` is true (item 13).
    - This is what answers.md:11 asks for.

47. **"Next: LOCK-m-F3 v0.1 … Then the `time` wiring at its step, and G-TIME-F3's six sessions" (entry:39–40).** PASS, as a plan.
    - It matches answers.md:11 and :26 ("→ LOCK-m-F3 v0.1 → G-TIME-F3's six sessions").
    - It matches RESULTS.md:128–130 (10a2bbb's Next, which includes the `time` wiring).
    - "N10's dated note" matches RESULTS.md:386 and :590 ("N10 m:312 stands [confirmed]").

48. **The entry's universal claims (task item 9).** PASS.
    - Each is backed by a check reproduced here: "all 538" (item 17), "Neither map" (21), "Every one of the 94" (22), "No file either map lists changed" (23), "neither gate re-runs" (24), "each asserted" (18), "nothing canonical" (35), "no file existed before" (37), "no timestamp and no HEAD" (38), and "all `45b67246…7a41`" (13).
    - The one unbacked universal is in the raw, not the entry (item 44).

## Notes (not counted)

- entry:4 `@@STAMP@@` and entry:38 `@@VC@@` are unfilled placeholders.
- Process: helper scripts are at `<scratch>/vc/` (hashes.py, gshape.py, scrub.py). Nothing was written in the repository.
- `git status` before and after: 0 tracked changes and the same 29 untracked entries.
- Repo code was imported only under `python -B` with `PYTHONDONTWRITEBYTECODE=1`; `closure()` spawns its own `python -I -B`.
- I did not run `ganl`.

## Totals

**48 items: PASS 45, IMPRECISE 1 (item 43), FAIL 2 (items 12, 44).**

## Code's dispositions (2026-11-07; each item re-checked at source before it was applied)

- **Item 12 (FAIL), the lexicons hash.** Confirmed: `json.dumps(counter_c, sort_keys=True, separators=(',', ':'))`
  hashes to `1b7d5a01af967d9f7953168dbce3468c562602b9f754069041f32b740d088028`, so the abbreviation ends `8028`. The
  entry's `8088` was Code's typo. Applied: the entry now reads `1b7d5a01…8028`. The lock draft's full value was
  already right.
- **Item 44 (FAIL), the raw's first line.** Confirmed: A1's regression reads Q-F0's seven released files by committed
  blob, among them the campaign checkpoint and its picks (raw's regression lines; `m_analyze.py:52–55`). The phrase
  "the synthetic battery only (no checkpoint, no pick)" was carried from G-ANL-F0's raw, where it was true. Applied:
  the first line now says the run is model-free and reads the synthetic battery's inputs and, for A1's regression,
  Q-F0's seven released files by blob (PIN-29's exception, which the battery checks admitted exactly those files).
- **Item 43 (IMPRECISE), the scrub note.** Applied: the entry says "local roots scrubbed to `<repo>` and `<tmp>`". The
  raw's second header line names both placeholders, and its last section's header says what `<tmp>` stands for.
- **Item 14 (not counted), structure.** Applied: the preprint block, v1's unchanged evaluations and the outputs hash
  are now separate bullets, each named by its field.
- **Item 15 (not counted), format.** Applied: G-SHAPE-F0's artifact is given as `38ba8e28…3b51`.
- The two placeholders (the stamp and this check's line) are filled at write time.
- **This raw.** Item 42's first bullet was reworded by Code so that the committed raw does not spell out the
  identifying strings. The finding itself is unchanged.
