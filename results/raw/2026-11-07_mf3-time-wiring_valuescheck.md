# G-TIME-F3's wiring -- the blind values-check of the entry and its raws, with Code's dispositions (2026-11-07)

*Code's raw. One blind pass by an agent given the drafts and the sources, not Code's conclusions: 58 items, 40 PASS, 12 IMPRECISE, 6 FAIL. Code's dispositions follow the report. The reports name scratch paths relative to the session's scratch directory (`scratchpad/…`); local roots are scrubbed.*

---

# Blind values-check: G-TIME-F3's wiring (the driver edit, the entry, four raws), against HEAD 1e79955

Checked: (E) `time/entry_wiring.md`, (D) `time/2026-11-07_mf3-time-wiring_design.md`, (R) Code's text in
`time/2026-11-07_mf3-time-wiring_review.md` (the header and the three "Code's dispositions" sections),
(C) `time/2026-11-07_mf3-time-wiring_sitecheck.txt`, (T) `time/2026-11-07_mf3-time-wiring_selftest.txt`, and the
driver `site-wt/scripts/mf3_sessions.py` (identical to `wire-wt`'s). Line numbers are those files' own. "Driver :N" is
the final driver at line N; "m:N" is `git show 1e79955:scripts/m_sessions.py` at line N.

Method. Every check was read-only. I edited, staged or committed nothing and wrote nothing under any `data/`. I never
ran `time`. Two in-memory harnesses live in my scratch (`scratchpad/vc_wiring/`):
- `inmem_driver_checks.py` reads the final driver's source and execs it as a module whose `__file__` is the canonical
  site-wt path. It optionally applies a mutant's text replacements in memory, then runs `_selftest(chk)` with `mlx`,
  `mlx.core`, `jlens_qwen` and `jlens_qwen.model` blocked and `HF_HUB_OFFLINE=1`.
- `inmem_reviewer_mutant.py` does the same with the round-3 reviewer's own replacement lists, taken from
  `review3/harness/make_mutants_r3new.py` and `make_mutants_r3extra.py`.

After the runs, site-wt's `git status` was unchanged, no file under site-wt was newer than Code's own driver copy
(21:30:50), and the driver still hashed to `1773ae7f…`. My only writes were to `scratchpad/vc_wiring/` and to this file.

## Hashes

1. **Claim:** the driver's pre-edit blob is `fad31c20…0cbb`. **Location:** E:3, E:39-40, D:6, D:50, D:206.
   **Verdict:** PASS. **Evidence:** `git show 1e79955:scripts/mf3_sessions.py | shasum -a 256` gives `fad31c20e444…0cbb`.
   `driver_before.py` hashes the same.
2. **Claim:** the final bytes hash to `1773ae7f…9a56`. **Location:** E:3, D:6, C:35, T:1, R:1218. **Verdict:** PASS.
   **Evidence:** `wire-wt` and `site-wt` both give `1773ae7f3dc3ddd256f5ff8188129397bf0b1ebbcf5f81da4b7c56beff6e9a56`,
   and `cmp` finds them identical. (Cosmetic: E:3 and D:6 wrap the value in double backticks, where the rest of the
   text uses single ones.)
3. **Claim:** mf3's `package_sha256` (`f30ad505…6310`) and m's (`7756dcf4…49bb`) stand. **Location:** E:3, D:5.
   **Verdict:** PASS. **Evidence:** `valence_core.m.resume.package_sha256_of` run in site-wt gives `f30ad5053904…6310` for
   `valence_core/mf3` and `7756dcf42532…49bb` for `valence_core/m`. LOCK-m-F3.md:96 names the first.
4. **Claim:** the analyzer is `d347ea0c…5e48`. **Location:** D:5. **Verdict:** PASS. **Evidence:** at both 1e79955 and
   site-wt, `scripts/m_analyze.py` hashes to `d347ea0c9b69…5e48`.
5. **Claim:** the lock is `377c5d60…6ce7`. **Location:** D:4. **Verdict:** PASS. **Evidence:** at both 1e79955 and
   site-wt, `LOCK-m-F3.md` hashes to `377c5d602709…6ce7`.
6. **Claim:** G-SHAPE-F3's artifact is `0c9de56e…1461`, and its sources map records the driver at `fad31c20…0cbb`.
   **Location:** E:39-40, D:50-51, D:206. **Verdict:** PASS. **Evidence:** `data/mf3/gates/G-SHAPE-F3.json` (1e79955 and
   the main tree) hashes to `0c9de56e17d0…1461`. `provenance.sources["scripts/mf3_sessions.py"]` is
   `fad31c20e444…0cbb`. No stage or analyzer code compares that map with HEAD at run time: a grep of
   `valence_core/mf3/{stages,guard,resume}.py` and `scripts/m_analyze.py` finds no reader. The stale entry is therefore a
   record only, as declared.

## Scope and the code against (D) §3

7. **Claim:** only the driver changes, and nothing under `valence_core/`. **Location:** E:2-3, D:4-6. **Verdict:** PASS.
   **Evidence:** `git diff 1e79955 --stat` in site-wt shows 1 file, `scripts/mf3_sessions.py`, +1221/−27 (round 3's
   "+1,179" was the pre-round-3 state). `git status` shows only that file and the untracked handoff copy. wire-wt
   (at `a28bef6`) shows the same single file.
8. **Claim:** the edit wires a subcommand at its step and touches no scoring-stack function, so G-SHAPE-F3 is not
   re-run. **Location:** E:37-38, D:45-50. **Verdict:** PASS. **Evidence:** the diff hunks touch the docstring, the imports
   (`os`, `stages`), the new constants, `refusal()`, new functions after `run_gshape`, `_selftest` and `main`.
   `build_schedules`, `hashes` and `run_gshape` are untouched, and no `valence_core` file changes.
9. **Claim:** "The other driver changes are incidental to the wiring:" the refusal text for id, qual and campaign; the
   self-test's runner capturing stderr; the self-test's own additions. **Location:** D:46-49. **Verdict:** IMPRECISE.
   **Evidence:** the diff also changes:
   - the "no action" refusal (driver :1429 adds "gshape or time");
   - the argparse description (:1391-1392) and the refused subparsers' help ("refused until its step", :1407);
   - the module docstring;
   - the imports of `os` and `stages`;
   - the position of the self-test's quarantine check, now after `_selftest_time` (:581);
   - a local name, `committed` → `committed_` (:542).

   None of these touches a scoring-stack function, so F-1's reading stands. **Fix:** list them, or write "among them".
10. **Claim:** the pre-load checks as each is named (E), and D §3's account of `_load_qwen`, `redact_totals`/`_say`,
    `time_identity_extra`, `time_precheck`, `driver_problems`, `qwen_snapshot`/`snapshot_line`, `run_time` (its order and
    exits) and `main`. **Location:** E:13-23, D:81-126. **Verdict:** PASS. **Evidence:** driver :177-508 and :1388-1430.
    - `_load_qwen`, `redact_totals`, `_say`, `snapshot_line`, `TOTALS_RX`, `TOTALS_REDACTED`, `HF_OFFLINE_ENV` and
      `MLX_LM_ALLOW_PATTERNS` match m:408-412, m:840-852, m:1082-1084 and m:627-634.
    - `qwen_snapshot`'s checks match m:1003-1079 line for line. The one text difference is the `HF_HUB_OFFLINE`
      message, which is not a check.
    - `run_time` follows m:1574-1676's Qwen order without the rulings: flags, out root, identity alone; then precheck,
      driver, snapshot and revision refused together; then DRIVER, SNAPSHOT, load, re-read, MOVED, MODEL ID, the re-read
      line, the stage.
    - Exits: 2 before the load, 4 on SystemExit, otherwise `EXIT_CODES`.
    - The top-level refusal is m:7563 verbatim.
11. **Claim:** `lock_m_modules` and `lock_weights` read the one sha256 per m file and the one WEIGHTS line. A WEIGHTS line
    is not glued to a letter, digit, underscore or hyphen, and must name `QWEN_MODEL_ID`. They refuse: none, two
    different values, another model. **Location:** D:83-86. **Verdict:** PASS. **Evidence:** driver :184-213 and :106
    (`(?<![\w-])WEIGHTS …`). The self-test exercises the cases at :702-727.
12. **Claim:** the snapshot's revision is refused before the load if it is not the lock's weights revision, which
    extends m's REVISION_STAGES (qual and campaign in m) to `time`. **Location:** E:22-23, D:67-70, D:137-138.
    **Verdict:** PASS. **Evidence:** driver :475-477 compares with `extra["weights_revision"]`. m:651 has
    `REVISION_STAGES = ("qual", "campaign")`, and m:1615-1617 holds its refusal.
13. **Claim:** "The constants (m's `TIME_*` values)". **Location:** D:74 (and the PIN at driver :81: "m's TIME_* values
    carried"). **Verdict:** IMPRECISE (low). **Evidence:** m:574-582 has `TIME_UNIT`, `TIME_COUNTS`
    (`(("A0",1),("A0s",1))`), `TIME_LOCKED_PATH`, `TIME_LOCK_FILE` (`"LOCK-m-F0.md"`) and `TIME_FLAGS`.
    - `TIME_FLAGS` and `TIME_LOCKED_PATH` carry m's values.
    - `TIME_LOCK_FILE` and `TIME_COUNTS` carry Q-F3's values in m's form.
    - `TIME_REASONING_CAP` and `TIME_FLAG_HELP` have no m counterpart.

    The values themselves are right: `keys.TEMPLATES` is (A1, A1s, A2, A2s, A3, A3s), and each committed `Q-F3_time_*.json`
    has n = 1. **Fix:** "(m's `TIME_*` form)".
14. **Claim:** "The self-test reads each of these from its source rather than importing it." **Location:** D:80.
    **Verdict:** IMPRECISE (low). **Evidence:** the constants check (driver :772) compares `QWEN_MODEL_ID` with
    `rs.QWEN_MODEL_ID` and `gshape.QWEN_MODEL_ID` by import; `QWEN_MODEL_ID` is `rs.QWEN_MODEL_ID` (:102), so the first
    comparison is an identity. The adapter's default, mlx_lm's `_download` list and m's constants are read from source by
    `ast`, as the PIN at :97-101 says precisely. **Fix:** "reads the adapter's, mlx_lm's and m's values from their source
    rather than importing them".
15. **Claim:** the differences from m: mf3's identity keys; no `--unit`, ruling files or prior adjudication; `DRIVER_REL`
    the pre-existing constant (m derives it from `__file__`); the revision refusal at `time`; what the self-test ports.
    **Location:** D:128-140. **Verdict:** PASS. **Evidence:**
    - m:7489 has `--unit`, m:1484-1485 the ruling files, and m:7417-7420 the OLMo-only `--prior-adjudication-file`.
    - m:626 derives `DRIVER_REL` from `__file__`, while the driver's :66 is unchanged from 1e79955.
    - mf3.resume's self-test line (T:94) shows the identity keys.
16. **Claim:** the values a run takes. The analyzer, package and renders values come as flags in m's form; the m files
    and the weights come from the lock's text. (f) holds by construction, and (e′) and (g) bind them.
    **Location:** E:44-47, D:63-66. **Verdict:** PASS. **Evidence:** driver :256-265, and `stages.licence_problems`'
    docstring (stages.py:283-290) for what (e′), (f) and (g) each check. The planted-lock check (:677-692) shows (e′)
    and (g) refusing with (f) silent.
17. **Claim:** the checks "add only refusals before a load, plus a SNAPSHOT line in the raw. No measurement or verdict
    path changes." **Location:** E:33, D:60. **Verdict:** IMPRECISE. **Evidence:** the checks named include the post-load
    re-read with its STOPs. SNAPSHOT RE-READ REFUSED, SNAPSHOT MOVED and MODEL ID come after the load, with exit 4 and
    before any session (:489-498), and the run also prints a "SNAPSHOT re-read after the load" line (:499-500) and the
    DRIVER line. The conclusion (no measurement or verdict path changes) holds. **Fix:** "they add only refusals before
    the load and STOPs after it, before any session, plus the DRIVER, SNAPSHOT and re-read lines in the raw".
18. **Claim:** `time` is the first Q-F3 stage that loads Qwen. **Location:** E:30, D:58. **Verdict:** PASS.
    **Evidence:** PROPOSAL-m v1.11 :290-293 orders G-SHAPE-F3 (model-free; Layer T loads only the tokenizer), G-ANL-F3,
    LOCK-m-F3 v0.1, then G-TIME-F3 "(Qwen, uncached)".

## PINs

19. **Claim:** nine PIN sites, at :72, :81, :97, :107, :220, :283, :333, :358 and :441, each opening "PIN (Code,
    declared at LOCK-m-F3 v0.2; the time wiring; …". **Location:** E:48, D:144-156. **Verdict:** PASS. **Evidence:**
    `grep -n 'PIN ('` in the final driver finds exactly those nine lines, each with that opening. The 1e79955 driver has
    0, which matches LOCK-m-F3.md:432-433. The subjects in D's table match the PIN texts.
20. **Claim:** declared at v0.2 "as m's step-10 sites were at LOCK v0.2", and "as the seat's G-TIME-F0 read (Q3) had
    v0.2 declare m's step-10 sites". **Location:** E:48, D:144. **Verdict:** PASS. **Evidence:** m:559, :628, :861, :988,
    :1007, :1296 and :1519 read "PIN (Code, declared at LOCK v0.2)". In
    `results/raw/2026-10-13_m-design-to-code_G-TIME-F0_read.md:47` (Q3), v0.2's §5.2 names the driver's blob, and "The
    five step-10 PIN sites … are carried on C6's terms as extended".
21. **Claim (driver text):** the PIN at :333-336 quotes Q2 as "the new blob's sha256 printed by the DRIVER line and
    recorded in the entry of the stage it wires and in the next lock revision" and closes the quote there.
    **Location:** driver :333-336. **Verdict:** IMPRECISE. **Evidence:** the source,
    `2026-10-13_m-design-to-code_G-TIME-F0_read.md:45`, goes straight on with "— v0.2 for `id`, v1.0 for `qual`, and for
    `campaign`, which follows v1.0, the campaign's launch entry". The PIN applies the clause to "every wiring of its
    kind". This is the truncation the 2026-10-13 review confirmed against m's own PIN (TF2-1,
    `results/raw/2026-10-13_m-gid-driver_review.txt:859-862`). m:988-992 now quotes through "the campaign's launch entry".
    **Fix:** add "…" or quote it through, as m does.
22. **Claim:** "That is the step-10 read's Q2 condition" / "The step-10 read's Q2 condition". **Location:** E:42-43,
    D:52. **Verdict:** IMPRECISE (low). **Evidence:** Q2 (read.md:45) states four "Conditions":
    - no change under `valence_core/m`;
    - the build reviewed, with the self-test extended;
    - the DRIVER-line record;
    - the new PIN sites declared.

    The DRIVER record is one of them. All four hold here, and E names each elsewhere. **Fix:** "one of the step-10 read's
    Q2 conditions".
23. **Claim:** the new blob is "recorded in the G-TIME-F3 entry and in LOCK-m-F3 v0.2"; "LOCK-m-F3 v0.2 records".
    **Location:** E:41-42, D:51, D:53, R:1038, R:1206. **Verdict:** PASS. **Evidence:** this is the house form for an act
    still to come. LOCK-m-F3.md:679 itself writes "which LOCK-m-F3 v0.2 records". Neither record exists yet, which the
    entry's "Next" makes clear.

## Quotes

24. **Claim:** the seat's F-1, verbatim. **Location:** D:14-16. **Verdict:** PASS. **Evidence:** a byte check (whitespace
    normalized) against `2026-11-06_ganl-f3_design-to-code_answers.md:24` finds it a substring.
25. **Claim:** the seat's F-2, verbatim. **Location:** D:17-19, E:25-28. **Verdict:** PASS. **Evidence:** the same check
    against line 25 of that file finds it a substring, from "**F-2.**" to "until then."
26. **Claim:** the F3 build design §8 has it "come with the driver's stage wiring (flag F-2)". **Location:** D:55-56.
    **Verdict:** IMPRECISE. **Evidence:** `2026-11-06_mf3-build_design.md:145` (in §8) reads "…the SNAPSHOT line)
    **comes** with the driver's stage wiring (flag F-2)". The quoted string is not a substring of the source.
    **Fix:** quote "comes with the driver's stage wiring (flag F-2)", or bracket the change: "come[s]".
27. **Claim:** the PIN in `stages.licence_problems` says "built with the stage wiring (flag F-2)". **Location:** D:56-57,
    E:32. **Verdict:** PASS. **Evidence:** `valence_core/mf3/stages.py:297-298` at 1e79955.
28. **Claim:** LOCK-m-F3 v0.1 §11 item 1: "the `time` subcommand is wired in `scripts/mf3_sessions.py` at its step,
    after this lock's commit." **Location:** D:10-11, driver :74. **Verdict:** PASS. **Evidence:** LOCK-m-F3.md:670-671.
29. **Claim:** the PI's routing, item 1, quoted at RESULTS.md@139635f:81: "… canonical `ganl` → LOCK-m-F3 v0.1 →
    G-TIME-F3 [go] …". **Location:** D:12-13, E:8, driver :75-76. **Verdict:** PASS. **Evidence:** line 81 of
    `git show 139635f:RESULTS.md` reads "> 1. G-ANL-F3: hygiene commit (N9, N12) → G-SHAPE-F0/F3 re-runs → canonical
    `ganl` → LOCK-m-F3 v0.1 → G-TIME-F3 [go]; N10 …".
30. **Claim:** the coordinating session's routing, relayed in chat (not in the repo). **Location:** E:9-11, D:20-41.
    **Verdict:** PASS (internal consistency). **Evidence:**
    - E's opening quote matches D's first lines; the elision "…" stands for D's five-item list.
    - E carries what the routing asks for: the dated note, F-2 quoted with Code's reading, the five checks each named,
      the DRIVER line with the F-1 reading, the lock-read values with flag-borne hashes, and the ruling forms left with
      the campaign.
    - LOCK-m-F3.md:674-681 describes the same routing.
31. **Claim:** "the e9b5022 precedent" for a dated note. **Location:** E:24. **Verdict:** PASS. **Evidence:** the
    commit exists (PROPOSAL-k v1.1, 2026-09-09). The PI's routings use the phrase for dated notes at RESULTS.md:1331,
    :1582, :1811, :1890 and :1971.
32. **Claim:** the records left as they are. **Location:** D:204-215, E:66-70. **Verdict:** PASS. **Evidence:**
    - LOCK-m-F3.md:502 has the F57 row ("what is wired (selftest, schedules, hashes, gshape) and refused (the four
      stages); …").
    - :432-433 reads "F57's is the exception: its site, `scripts/mf3_sessions.py`, carries no PIN line", which the elided
      quote matches.
    - `stages.py:12` reads "none is wired in the driver at the build".
    - The 1e79955 `main` dispatches `--selftest` and `--build-schedules` before any subcommand and prints its refusals
      to stdout, so the drift is pre-existing.

## Counts

33. **Claim:** the self-test goes from 136 to 160 and passes 160/160. The module checks are unchanged at 124. The driver's
    checks go from 12 to 36: one changed, 24 new. **Location:** E:4, E:49, D:160-162. **Verdict:** PASS. **Evidence:**
    - `results/raw/2026-11-07_ganl-f3_checkfix_runs.txt:35` and :64 read "136/136 mf3 selftest checks pass", and the
      driver is unchanged since (`git log -- scripts/mf3_sessions.py`: 993eba1 is the last).
    - At 1e79955, `_selftest` has 12 `chk` calls, so 136 − 12 = 124 module checks.
    - T has 160 `[PASS]` lines and 0 `[FAIL]`: 124 `mf3.*` and 36 `mf3_sessions:`. The one changed check is the
      refused-stages check (old :151-152, new :549-554); the other 11 keep their labels.
34. **Claim:** the 24 new checks as grouped (4 + 2 + 5 + 5 + 8). The fake-cache section has 19 cases, and
    MLXLM_USE_MODELSCOPE is tested in four letter cases. **Location:** D:164-193. **Verdict:** PASS. **Evidence:**
    - The groups sum to 24 and match T:141-168.
    - The `sq` dict (:837-857) has 19 keys: 2 clear, and 17 refused, which :888 asserts.
    - The modelscope cases are 'True', 'true', 'TRUE' and 'tRuE', with 'False' clear (:890-897).
35. **Claim:** 35 refused cases. **Location:** D:186, T:160. **Verdict:** PASS. **Evidence:** `t_refused` (:1166-1227)
    has 35 keys, and :1249 asserts `len(t_refused) == 35`.
36. **Claim:** the final trap counts: the loader 4 times, the stage once, no escape, `data/mf3` unchanged.
    **Location:** D:193, T:168. **Verdict:** PASS. **Evidence:** :1355-1362. The four loads are reach_load, abs_paths,
    resume_open and pending, each asserting `loads == 1`. The one stage reach is post_ok. The post-load STOP cases use a
    stand-in loader, so they add no load.
37. **Claim:** round 1 had 0 MAJOR, 3 MINOR, 13 NOTEs, with 41 mutants of which 18 survived. Round 2 had 0 MAJOR, 1
    MINOR, 12 NOTEs, with 74 mutants of which 16 survived. Round 3 had 0 MAJOR, 1 MINOR, 12 NOTEs, with 99 runs of which
    16 survived. **Location:** E:55-57, R:3. **Verdict:** PASS. **Evidence:**
    - Round 1: R:19; NOTEs 1-13 at R:312-347; "Killed 23, survived 18" at R:400.
    - Round 2: R:491; NOTE-1 to NOTE-12; 41 + 33 = 74 runs, 3 + 13 = 16 survived (R:634, R:690).
    - Round 3: R:1050 and R:1070; `review3/mutation_table.md` has 99 rows (58 + 16 + 24 + 1 variant), and
      `mutation_summary.txt` reads "killed 83, survived 16".
38. **Claim:** round 3's 16 survivors include "6 equivalent". **Location:** E:57, R:3. **Verdict:** FAIL.
    **Evidence:** R:1070-1072, the reviewer's own count: round 2's 16 survivors re-run leave "6 that survive [and] are all
    equivalent", and of the 10 new survivors "1 is equivalent". That one is r3_x2, "equivalent: identical bytes on
    stderr" (mutation_table.md row 39), so 7 are equivalent. **Fix:** "16 survived, 7 of them equivalent".
39. **Claim:** the site-check numbers, all ten suites passing: regression 154, format_recon 67, k1_stage1 21,
    k1_analyze 20, e2d_d2_analyze 46, recon_echo 18, closure_verify3 24, m_sessions 846, m_analyze 525 and
    mf3_sessions 160. **Location:** E:60-62. **Verdict:** PASS. **Evidence:** C:23-33 and `sitecheck_summary2.txt` are
    identical, and C:37 shows 160/160 on the final bytes.
40. **Claim:** closure_verify3 fails its two R13 checks (22/24) without the untracked handoff, "the raw records that
    run", and passes 24/24 with it, "as the earlier site checks had it". **Location:** E:63-65, C:2, C:12, C:18-19.
    **Verdict:** PASS. **Evidence:**
    - C:12 records FAIL and C:18 "two failures were its R13 checks".
    - The two R13 checks that read the handoff are in the 24/24 output (`sitecheck_out/closure_verify3.txt:31-32`), and
      the reviewer saw 22/24 independently (R:1156-1158).
    - Precedent: `2026-11-07_ganl-f3_checkfix_runs.txt:4-5`, `2026-11-07_ganl-f3_hygiene_sitecheck.txt:6` and
      `2026-11-06_ganl-f3_build_sitecheck.txt:7`.
    - Run 1's own closure_verify3 output was overwritten by run 2 and is not kept.

## Safety and overstatements

41. **Claim:** "Every case that can reach the Qwen branch runs with these in place: `_load_qwen` a trap, or a stand-in
    …; `stages.run_gate_stage` a trap, except where a stub factory needs the real stage; `stages.DEFAULT_OUT` a test root,
    and m:267's checklist stubbed; `build_schedules` and `run_selftest` traps." **Location:** D:195-199 (the same wording
    is in the `_selftest_time` docstring, driver :586-590). **Verdict:** IMPRECISE. **Evidence:**
    - All four hold only for `time_q` (:1110-1129).
    - `stub_run` (:1001-1017) traps the loader and sets `DEFAULT_OUT` and `GATES_DIR` to test paths. It does not stub
      `guard.preflight_laptop` and does not trap `build_schedules` or `run_selftest`.
    - The seam call (:1264-1273) traps the loader and the stage and stubs the checklist, but does not trap the two
      escapes.
    - Neither can reach the Qwen branch as written (a factory is given, or the out root is refused), and neither calls
      `main`, so neither can reach the escapes. The safety holds; the four-item list does not describe every case.

    **Fix:** say which case carries which trap.
42. **Claim:** the constants check calls the real `_load_qwen` with `qwen_or_explain` answering, `get_adapter`
    refusing, and the mlx, mlx_lm and jlens_qwen imports failing. The fake-cache section holds the hub offline by its own
    constant. **Location:** D:201-202. **Verdict:** PASS. **Evidence:** :758-767 patch `qwen_or_explain` and
    `get_adapter`, and set `sys.modules` to None for mlx, mlx.core, mlx_lm, jlens_qwen and jlens_qwen.model. :794 patches
    `huggingface_hub.constants.HF_HUB_OFFLINE` to True around the whole fake-cache section.
43. **Claim:** "No case can load the model, run a session or write `data/mf3`: the loader, the stage, the schedules
    writer and the self-test are trapped throughout." **Location:** E:50-51. **Verdict:** FAIL. **Evidence:** no case can
    load the model or write `data/mf3`, but the rest is wrong:
    - The stub-factory cases run sessions through the real `stages.run_gate_stage`, on the stub adapter: "six sessions,
      PASS" (:1019, :1032, :1041-1046, :1077). The stage is therefore not "trapped throughout", and D:197 says so. The
      code's docstring (:589) has "run a session **on it**".
    - The loader is not trapped throughout either: the constants check runs the real `_load_qwen` (E:52 says so), and
      the post-load cases use a stand-in.
    - The schedules writer and the self-test are trapped only in `time_q`.

    **Fix:** "No case can load the model, run a session on it or write `data/mf3`." Then say where each trap applies:
    every Qwen-branch route has the loader trapped (a stand-in after the load); the stage is trapped except where the
    stub factory runs it; `DEFAULT_OUT` is a test root; the time invocations through `main` also trap the schedules
    writer and the self-test.
44. **Claim:** "The constants check's real `_load_qwen` call runs with every route to a model closed." **Location:**
    E:52. **Verdict:** IMPRECISE (low). **Evidence:** the self-test closes these routes:
    - `qwen_or_explain` (answered);
    - `get_adapter` (refused);
    - the mlx, mlx.core, mlx_lm, jlens_qwen and jlens_qwen.model imports.

    That closes every Qwen route, including a direct `QwenMLXAdapter`, whose constructor imports mlx.core and
    jlens_qwen.model first (qwen_mlx.py:72-73). A direct `OLMoHFAdapter` route is closed only because the laptop venv has
    no torch (`find_spec('torch')` is None); the self-test itself does not close it. **Fix:** "every Qwen route", or
    list the routes, as D:201-202 does.
45. **Claim:** "Each MINOR was a gap in the self-test against m's. Each was fixed." **Location:** E:58. **Verdict:** FAIL.
    **Evidence:** only three of the five MINORs were such gaps (round 1's MINOR-3 and the MINOR-1 of rounds 2 and 3).
    - Round 1's MINOR-2 (R:246-267) was a production defect: `driver_problems` checked the canonical path, not the running
      file. The fidelity table at R:88 grades it "defect, MINOR-2" against m's `DRIVER_REL` derived from `__file__`. It
      was fixed in `driver_problems` (R:421-424; driver :341-347).
    - Round 1's MINOR-1 (R:204-244) was the self-test's own trap coverage: the seam and ended calls ran unpatched. It was
      not a comparison with m's checks.

    Each was fixed. **Fix:** describe the two separately.
46. **Claim:** "Code's check on the final bytes: round 3's ten surviving mutants were rebuilt on the final bytes … the
    six gaps, the label over-claim, the two unpinned forms and the load route. All ten are killed." **Location:** E:59.
    **Verdict:** FAIL. **Evidence:**
    - Round 3's 16 survivors are 6 from round 2 (all equivalent) and 10 new: r3_g1-g5, r3_p2, r3_pl1, r3_h1, r3_w3 and
      r3_x2. r3_k1 was killed in round 3: "killed (15/16) | RAISED(SystemExit: REVIEW-TRAP: the real Qwen loader was
      reached)" (mutation_table.md row 31). Code's ten are the nine non-equivalent new survivors plus r3_k1, not "ten
      surviving mutants".
    - Code's rebuilt r3_p2 is not the reviewer's mutant (item 54).

    "All ten are killed" does hold for the reviewer's exact replacement lists on the final bytes. My in-memory run gave
    r3_g1 34/36; r3_p2, r3_g2, r3_g3, r3_g4, r3_g5, r3_pl1, r3_w3 and r3_h1 35/36 each; and r3_k1 RAISED 15/16 at the
    self-test's own get_adapter refusal, against a 36/36 baseline.

    **Fix:** "round 3's nine surviving non-equivalent mutants and the load route r3_k1 (which round 3 killed only at the
    reviewer's loader trap)". Rebuild r3_p2 as the reviewer built it.
47. **Claim:** "Site check (the final bytes on `1e79955`): all ten suites pass", and "the site check is re-run on the
    final bytes with the untracked HANDOFF … copied in". **Location:** E:60; R:1210-1211 (round 3 NOTE-12).
    **Verdict:** IMPRECISE. **Evidence:** C:21 says run 2, the ten-suite run, was on "the driver after review round 3's
    fixes, **before the help-pairing pin**". Only the driver's suite ran on the final bytes (C:35-37). Timestamps agree:
    run 2's `mf3_sessions.txt` is from 21:30:44, site-wt's driver became the final bytes at 21:30:50, and
    `mf3_sessions_final.txt` is from 21:31:47. The run-2 output differs from the final one only in the help check's label.
    No other suite reads the driver: no reference to `mf3_sessions` and no glob over `scripts/` in their code. So the
    substance holds; the wording does not. **Fix:** "all ten suites pass (run 2, on the bytes before the help-pairing
    pin), and the driver's suite 160/160 again on the final bytes", in both places.

## Code's text in (R)

48. **Claim:** "each round ran the self-test, mutation probes under traps (loader, stage, imports of mlx / mlx_lm /
    jlens_qwen, writes under data/, network, a nested self-test) and state probes". **Location:** R:3.
    **Verdict:** IMPRECISE. **Evidence:**
    - Round 1's harness (`review/harness/trapped_selftest.py`; R:34-37) trapped the loader routes and blocked the three
      imports, and watched `data/mf3` by hash before and after. It had no write, network or nested-self-test trap; round
      2 "adds four more" (R:524-530).
    - No reviewer harness trapped the stage. The stage trap is the self-test's own `t_stage`.

    **Fix:** "round 1: the loader and the imports, `data/mf3` watched by hash; rounds 2-3 added traps on writes under
    data/, network connects and a nested self-test".
49. **Claim:** the three reports are the reviewers' own, round 3 saved as given. **Location:** R:3. **Verdict:** PASS.
    **Evidence:** R:9-410 is identical to `review_r1.md`, R:472-1016 to `review_r2.md` and R:1050-1182 to `review_r3.md`
    (`diff` empty). The disposition blocks match `dispositions_r1/2/3.md`, apart from the filled `@@MUTS@@`.
50. **Claim:** round 1's dispositions as applied. **Location:** R:414-466 (except item 51). **Verdict:** PASS.
    **Evidence:** the seam call with its traps (:1264-1278), `stub_run` with its traps, the running-file refusal
    (:341-347), and MINOR-3's list of cases, all in the driver. The counts match the scratch outputs:
    - `selftest2.txt` reads 149/149 with "in 20 cases";
    - `selftest4.txt` reads 156/156 with "in 33 cases";
    - round 2 confirmed both (R:536-541, R:594).

    The "3 times" final count was round 1's state (R:564).
51. **Claim:** "`id`, `qual`, `campaign` and "no action" keep their pre-existing stdout lines; this edit leaves them
    alone (declared)." **Location:** R:455-457. **Verdict:** IMPRECISE. **Evidence:** the edit, already in
    `time/wiring.diff` as round 1 reviewed it (:123-126, :988-989), changes both texts: "is not wired at the F3 build"
    becomes "is not wired yet", and the no-action line gains "or time". D:47 lists the first as a change. Only the stream,
    stdout, is left alone. **Fix:** "keep their pre-existing stream (stdout); their texts change with the wiring".
52. **Claim:** round 2's dispositions as applied, and "159/159, then 160/160 after round 3". **Location:** R:1020-1044.
    **Verdict:** PASS. **Evidence:** in the driver:
    - (a) `w_cut` and the pending case (:1064-1083, :1295);
    - (b) and (c) `w_default` and `w_names` (:957-973);
    - (d) the same-name copy (:1213-1214);
    - (e) multi with the licence, renders, preflight, driver and snapshot (:1252-1262);
    - (f) the loop lock (:1170) and `t_ckpt` (:1134-1138);
    - the escape traps (:1115-1116, :1361);
    - the HF_HUB_OFFLINE patch (:794);
    - the `(?<![\w-])` anchor and the OLD-WEIGHTS case (:106, :711);
    - the exact top-level line (:1250);
    - `TIME_FLAG_HELP` (:91-95).

    The counts: `selftest5.txt` 159/159, `selftest7.txt` 160/160, C:15.
53. **Claim:** round 3's dispositions MINOR-1 (a)-(d) and NOTE-1 to NOTE-11 as applied. **Location:** R:1186-1209.
    **Verdict:** PASS. **Evidence:** in the driver:
    - (a) and (d): :1232 and :1258-1262;
    - (b): :1233;
    - (c): :1325-1336;
    - NOTE-1: the licence inside the patch (:680-682) and the final label (:1356-1358);
    - NOTE-2: :758-767;
    - NOTE-3: :712-713;
    - NOTE-4: :1192-1193;
    - NOTE-5: :781-790;
    - NOTE-7: :961-966.
54. **Claim:** "Code rebuilt the round-3 survivors and re-ran them …: the six gaps (r3_g1 … r3_p2); … the load route
    (r3_k1). Results: … r3_p2 by the refused battery (CHECKPOINT EXISTS beside STAGE ENDED) and the final count; …"
    **Location:** R:1212-1218. **Verdict:** FAIL. **Evidence:**
    - The reviewer's r3_p2 moves `rs.refuse_ended(cpath)` after the CHECKPOINT EXISTS test, with two replacements
      (`review3/harness/make_mutants_r3new.py:71-72`; its file has the call at :315).
    - Code's `time/mut/final/r3_p2_ended_after_exists.py`, and `mut/mutants/`'s, only delete it (`diff`: "309d308" and
      nothing added). That is round 1's `drop_refuse_ended` in effect. It is killed because "ended --resume" reaches the
      loader, hence the final count (`mut/final1.txt`), and it does not exercise round 3's MINOR-1 (b) assertion
      (:1233).
    - "CHECKPOINT EXISTS beside STAGE ENDED" is the reviewer's mutant's symptom, not the symptom of the mutant Code ran.
      Run in memory on the final bytes, the reviewer's own r3_p2 is killed 35/36 by the refused battery alone; the final
      count passes.
    - Also: Code's r3_g1 adds a second DRIVER print (`diff`: "478a479" only), while the reviewer's moves it. Both are
      killed by the refused battery and multi.
    - r3_k1 is not a round-3 survivor (item 46).

    **Fix:** rebuild r3_p2 with both of the reviewer's replacements and record "r3_p2 by the refused battery (CHECKPOINT
    EXISTS beside STAGE ENDED)". Say r3_g1 was rebuilt as an added print, or rebuild it. Call the set "the round-3
    survivors that are not equivalent, and the load route r3_k1".

## (C) and (T)

55. **Claim:** C is faithful to the runs it describes. **Location:** C:1-37. **Verdict:** PASS. **Evidence:**
    - C:6-16 equal `time/sitecheck_summary.txt` (run 1, 159/159, closure_verify3 FAIL), and C:23-33 equal
      `time/sitecheck_summary2.txt`.
    - Run 1's driver `bf34c11b…` is the one round 3 reviewed (R:1056). The second worktree (`site2-wt`) is at 1e79955
      with `bf34c11b…` and the handoff.
    - The gating is as `sitecheck_time.sh` does it: on the summary-line regex, never on an exit code after a pipe.
    - The final section matches `sitecheck_out/mf3_sessions_final.txt`.
    - "the only change since run 2, a self-test check" agrees with the pre-pin mutants differing from the final ones only
      by the help check (:780-790).
    - The stamp, 02:32:25 UTC, is 21:32 EST, the file's own mtime.
56. **Claim:** no local path, user name, session id or temp-dir id in C. **Location:** C. **Verdict:** PASS.
    **Evidence:** a search for the identifying strings (the home, private and temp roots, the user name, the sandbox
    user directory, the session id, the temp directory's id segment and its truncated heads, and the folder names)
    finds nothing, and there is no 20+ character non-hex run. (Code reworded this evidence before the commit so the
    raw does not spell them out.)
57. **Claim:** T is the self-test of record on the final bytes, in a worktree at 1e79955 with the driver uncommitted.
    **Location:** T:1-170. **Verdict:** PASS. **Evidence:** `diff` against `sitecheck_out/mf3_sessions_final.txt` shows
    only T's two header lines and the scrubs, at INVOCATION and lines 110-111, 114 and 152-153. T:167
    (`driver_problems`: "working-tree bytes are not HEAD's blob") confirms the uncommitted driver.
58. **Claim:** "Local roots scrubbed". **Location:** T:1 and T:105. **Verdict:** FAIL. **Evidence:** T:105 keeps a
    truncated head of the temp root, at the end of the printed value of the check whose message begins "NOT THE
    FIXED CAP: G-ID-F3 would run at reasoning cap 60; G-TIME-F3's lines at". The committed precedent scrubs the same check's text to "G-TIME-F3's lines at <tmp>"
    (`results/raw/2026-11-06_mf3-build_selftest.txt:104`). No user name, session id or macOS temp-dir id remains (the temp
    directory's id segment and the root's folder-name fragments were searched for), and no 20+ character non-hex run (the long runs are identifiers such as
    `line_triples_identical`). Note: Python tempfile names survive after `<tmp>/` (`tmptt8ag_8_`, `tmpwxr354n1`,
    `tmp2poh20qu`). They are random and not identifying; the precedent raw dropped them (:115 has `<tmp>/mf3/…`).
    **Fix:** replace the truncated head with "<tmp>" at T:105, and re-run the search. (Code reworded item 58's
    evidence, fix line and totals entry before the commit so the raw does not spell the fragments out.)

## Totals

58 items: **40 PASS, 12 IMPRECISE, 6 FAIL.**

- FAIL: 38 (round 3's equivalent count: 7, not 6), 43 (E's "no case … trapped throughout"), 45 (E's "each MINOR a
  self-test gap"), 46 (E's "round 3's ten surviving mutants"), 54 (R's rebuilt r3_p2: a deletion, not the reviewer's
  move), 58 (T:105, a truncated temp root).
- IMPRECISE: 9, 13, 14, 17, 21, 22, 26, 41, 44, 47, 48, 51.
- No FAIL touches a hash, the scope, the production code's behaviour or the self-test's outcome. The final bytes kill
  all ten of the reviewer's round-3 mutants as built by the reviewer's own generators (my in-memory runs), and the
  self-test's safety holds as written. The defects are in the records' wording, one count, one scrub, and the
  description of one rebuilt mutant.

## Code's dispositions (2026-11-07; each item re-checked at source before it was applied)

- **38 (FAIL), "6 equivalent".** Confirmed: seven, counting r3_x2. Fixed in the entry and in the review raw's header.
- **43 (FAIL), "no case can … run a session".** Confirmed: the stub runs run sessions on the stub through the real
  stage. The entry now says "run a session on it" and where each trap applies; so do the design raw's §6 and the
  self-test's docstring.
- **45 (FAIL), "each MINOR was a gap against m's".** Confirmed. The entry now distinguishes:
  - round 1's MINOR-2, a production defect, fixed in `driver_problems`;
  - round 1's MINOR-1, the self-test's trap coverage;
  - three gaps against m's self-test.
- **46 (FAIL), "round 3's ten surviving mutants".** Confirmed. The entry and the review raw now say the nine
  non-equivalent survivors, plus r3_k1 (killed in round 3, run as a check of NOTE-2's fix).
- **54 (FAIL), Code's r3_p2 and r3_g1 not the reviewer's mutants.** Confirmed: Code's r3_p2 deleted the call, and its
  r3_g1 added a print. Both were rebuilt as the reviewer's moves and run on the final bytes:
  - r3_p2 is killed 35/36 by the refused battery alone;
  - r3_g1 is killed 34/36 by the refused battery and multi.
  The review raw's record is restated.
- **58 (FAIL), a truncated temp root in the self-test raw.** Confirmed. The scrub now also replaces, with `<tmp>`, a truncated
  head of the temp root (its folder-path prefix cut short by a printed value) and the temp directory's id segment. The raws were regenerated and searched:
  - no fragment of the temp root's folder path;
  - no 6-character piece of the id segment;
  - no user name or session id.
- **9, the incidental changes.** Applied: the full list is in the design raw's §2. None is a scoring-stack function.
- **13, "m's TIME_* values".** Applied: "m's TIME_* form", with Q-F3's values, in the design raw and in the driver's
  PIN at :81. The PIN now says that TIME_REASONING_CAP and TIME_FLAG_HELP have no counterpart in m.
- **14, the constants read from source.** Applied: QWEN_MODEL_ID is compared with mf3.resume's and gshape's by
  import, and the adapter's, mlx_lm's and m's values are read from source.
- **17, "they add only refusals …".** Applied in the entry and the design raw: refusals and the SNAPSHOT line before
  the load, with the DRIVER line, and after it the re-read line and three STOPs. The routing's own sentence, quoted
  in the design raw §1, is left as the routing wrote it.
- **21, the PIN's Q2 quote truncated.** Applied: an ellipsis closes the quote in `driver_problems`' docstring.
- **22, "the Q2 condition".** Applied: one of four, and the design raw's §2 lists all four as holding.
- **26, "come with".** Applied: "comes with", as the build design has it.
- **41, the protections listed for every Qwen-reaching case.** Applied: the design raw's §6 and the self-test's
  docstring now say where each trap applies.
- **44, "every route to a model".** Applied: "every Qwen route".
- **47, "the final bytes" for the ten-suite run.** Applied: the entry, the review raw and the site-check raw say that
  the ten-suite run used the bytes before the help-pairing pin, and that the driver's suite ran on the final bytes.
- **48, the review raw's trap list.** Applied: the header says which round's harness trapped what, and that the stage
  trap is the self-test's own.
- **51, round 1's NOTE 8 disposition.** Applied: the stream is unchanged, and the texts change.
- **The driver's bytes after these fixes:** sha256 `890084e6c626a3ced2007c4285c255fb73978c07aeca15427172fc17028690af`.
  - The fixes touch comments and docstrings only. Its code's syntax tree, docstrings stripped, is identical to
    `1773ae7f…`'s (ast.dump; comments are never in the tree).
  - Its self-test passes 160/160, and the reviewer-form r3_p2 and r3_g1 were run on these bytes.

---

# Pass 2

# Blind values-check, second pass: G-TIME-F3's wiring after the first pass's fixes (driver `890084e6…90af`), against HEAD 1e79955

Checked: (E) `time/entry_wiring.md`, (D) `time/2026-11-07_mf3-time-wiring_design.md`, (R) Code's text in
`time/2026-11-07_mf3-time-wiring_review.md` (R:1-5 and the three "Code's dispositions" sections, R:412-468,
R:1018-1046, R:1184-1241), (C) `time/2026-11-07_mf3-time-wiring_sitecheck.txt`, (T)
`time/2026-11-07_mf3-time-wiring_selftest.txt`, (V) `time/2026-11-07_mf3-time-wiring_valuescheck.md`, and the driver
`wire-wt/scripts/mf3_sessions.py`. S is the session's scratch directory; every path here is under it. Line numbers
are those files' own. "Driver :N" is line N of the bytes `890084e6…90af`. "VC1 N" is item N of the first pass
(`time/valuescheck_wiring.md`). "m:N" is `git show 1e79955:scripts/m_sessions.py` at line N.

Method. Read-only throughout. I edited, staged or committed nothing, wrote nothing under any `data/`, and never ran
`time` or the driver's CLI. My writes are this file and `vc_wiring2/`:
- `ast_compare.py` compares two sources' syntax trees, with docstrings kept and stripped, and their comments.
- `inmem_mut.py` applies one mutant's exact replacement list, taken from the round-3 reviewer's generators
  (`time/review3/harness/make_mutants_r3new.py`, `make_mutants_r3extra.py`), to a worktree driver's source in memory.
  It then runs `_selftest(chk)` with `mlx`, `mlx.core`, `jlens_qwen` and `jlens_qwen.model` blocked and
  `HF_HUB_OFFLINE=1`.
- `inmem_p2_say.py` does the same for r3_p2 and records every `_say` line.
- `rebuilt/` holds the reviewer's generators' output on 1773ae7f and on 890084e6 (mutant copies only).
- `driver_prepin_rebuilt.py` is item 28's reconstruction.

The in-memory runs used `mut-wt3` (1e79955, driver 890084e6, uncommitted). Afterwards it had no file newer than its
driver, its `data/` tree hashed the same as before the runs, its driver still hashed to 890084e6, and
`git --no-optional-locks status` was unchanged. The main tree is at 1e79955 with no tracked change.

## 1. The first pass's FAIL and IMPRECISE items, re-derived at source

1. **VC1 38: "99 runs, 16 survived, 7 of them equivalent".** **Location:** E:60, R:3. **Verdict:** PASS.
   **Evidence:**
   - `time/review3/mutation_table.md` marks seven rows equivalent: rows 1, 3, 4, 14, 15 and 16 (round 2's six
     survivors) and row 39 (r3_x2, "identical bytes on stderr").
   - The reviewer agrees (R:1070-1072): "the 6 that survive are all equivalent", and of the 10 new survivors "1 is
     equivalent".
   - The table has 99 rows, and `mutation_summary.txt` reads "killed 83, survived 16".
2. **VC1 43: "No case can load the model, run a session on it, or write `data/mf3`", with where each trap
   applies.** **Location:** E:51-55; also D:207-219 and the `_selftest_time` docstring (driver :587-595).
   **Verdict:** PASS. **Evidence:**
   - `time_q` (:1099-1121) patches `stages.DEFAULT_OUT` to the test root, `run_gate_stage` to `t_stage`,
     `preflight_laptop` to a stub, and `_load_qwen` to `t_loader` (a stand-in in the post-load cases). It also
     patches `build_schedules` and `run_selftest` to `t_escape`.
   - `stub_run` (:1006-1019) patches `GATES_DIR`, `DEFAULT_OUT` and `_load_qwen`, and runs the real stage on the
     stub factory.
   - The seam call (:1268-1278) patches `DEFAULT_OUT`, the stage, the checklist and the loader.
   - The constants check (:764-772) answers `qwen_or_explain`, refuses `get_adapter`, and sets `sys.modules` to
     None for mlx, mlx.core, mlx_lm, jlens_qwen and jlens_qwen.model.

   E's three sentences say exactly this.
3. **VC1 45: the five MINORs, each fixed.** **Location:** E:61-65. **Verdict:** PASS. **Evidence:**
   - Round 1's MINOR-1 (R:204) is the self-test's trap coverage: "The seam and ended calls run the production path
     with no loader trap".
   - Round 1's MINOR-2 (R:246) is the production defect: "`driver_problems` checks the canonical path, not the
     running file". It was fixed in `driver_problems`, which compares the running file with `REPO / DRIVER_REL`
     (driver :342-348).
   - The other three are gaps against m's self-test: R:269 ("a subset of m's checks"), R:803 ("Residue of round 1's
     MINOR-3") and R:1081 ("m's self-test checks six more time-path behaviours").
4. **VC1 46: the set re-run is the nine non-equivalent round-3 survivors, plus r3_k1.** **Location:** E:66-67,
   R:1214-1221, V:445-446. **Verdict:** PASS. **Evidence:**
   - The table's survivors among the new mutants are the six gaps (r3_g1 to r3_g5 and r3_p2), the label over-claim
     r3_pl1, the two unpinned forms r3_h1 and r3_w3, and the equivalent r3_x2. R:1072 gives the same split.
   - r3_k1 is row 31, "killed (15/16)".
   - The rewritten passages have errors of their own: items 28-31.
5. **VC1 54: r3_p2 and r3_g1 rebuilt in the reviewer's form and run on the final bytes.** **Location:** R:1224-1231,
   E:68-69, V:447-451. **Verdict:** PASS. **Evidence:**
   - `time/mut/final2/r3_p2_ended_after_exists_moved.py` and `r3_g1_driver_line_before_refusal_moved.py` are
     byte-identical (`cmp`) to `make_mutants_r3new.py`'s output on 890084e6.
   - The results are confirmed in item 24.
6. **VC1 58: the truncated temp root in T.** **Location:** T:1, T:105. **Verdict:** PASS (for T). **Evidence:**
   - T:105 now reads "G-TIME-F3's lines at <tmp>", as the committed precedent has it.
   - A search of T and C finds none of these: the home, private or temp roots or their truncated heads; the user
     name; the session id or any 8-character piece of it; the temp root's folder-name fragments; any 6-character
     piece of the temp directory's id segment.
   - The only 20+ character non-hex run in T is `IncompleteSnapshotError`. The three Python tempfile names left
     after `<tmp>/` are random.
   - V does not pass the same search: item 37.
7. **VC1 9: the incidental changes, now listed.** **Location:** D:45-56. **Verdict:** PASS. **Evidence:** the
   diff fad31c20 → 890084e6 has 13 hunks. Beside the wiring itself (the constants and PINs, the new functions, the
   time subparser and dispatch, `_selftest_time`), the changes are exactly D's list:
   - in `refusal()`, "is not wired at the F3 build" becomes "is not wired yet";
   - the no-action line goes from "hashes or gshape" to "hashes, gshape or time";
   - the argparse description, and the refused subparsers' help ("refused until its step");
   - the module docstring;
   - the `os` and `stages` imports;
   - in `_selftest`: the runner's stderr capture, the quarantine check moved after `_selftest_time` (:581-583), and
     `committed` renamed `committed_`.

   The refused-stages check's change is stated in D §6 (D:173-174).
8. **VC1 13: "m's `TIME_*` form".** **Location:** D:84-87, driver :81 and :85-86. **Verdict:** IMPRECISE (low).
   **Evidence:** fixed where it was flagged:
   - m:574-582 has TIME_UNIT, TIME_COUNTS, TIME_LOCKED_PATH, TIME_LOCK_FILE and TIME_FLAGS. It has no
     TIME_REASONING_CAP or TIME_FLAG_HELP, as D:86-87 and the PIN's new sentence say.
   - But D:161, the PIN register's row for :81, still reads "(m's TIME_* values)". It now disagrees with the PIN it
     summarizes ("m's TIME_* form carried").
   - V:458 says the change was applied "in the design raw".

   **Fix:** "(m's TIME_* form)" at D:161.
9. **VC1 14: the constants, compared by import or read from source.** **Location:** D:91-92. **Verdict:** PASS.
   **Evidence:** driver :773-783 asserts `QWEN_MODEL_ID == rs.QWEN_MODEL_ID == qm_default ==
   assigned("QWEN_MODEL_ID") == gshape.QWEN_MODEL_ID`.
   - `qm_default` is parsed by `ast` from `valence_core/adapters/qwen_mlx.py` (:745-751).
   - mlx_lm's `_download` list is parsed from its `utils.py` (:752-760).
   - m's values come from `assigned()` over `ast.parse` of `scripts/m_sessions.py` (:735-744).
10. **VC1 17: what the checks add.** **Location:** E:33-34, D:69-70. **Verdict:** PASS. **Evidence:** in
    `run_time` (driver :470-509), the order is:
    - the refusals (exit 2);
    - DRIVER, SNAPSHOT, then `_load_qwen()`;
    - SNAPSHOT RE-READ REFUSED, SNAPSHOT MOVED and MODEL ID (SystemExit, exit 4);
    - the re-read line, then the stage.

    D:35 keeps the routing's own sentence as a quote.
11. **VC1 21: the PIN's Q2 quote closed with an ellipsis.** **Location:** driver :334-337 (`driver_problems`'
    docstring). **Verdict:** PASS. **Evidence:** the quote now ends "…in the next lock revision …")". The source,
    `results/raw/2026-10-13_m-design-to-code_G-TIME-F0_read.md:45`, goes on: "— v0.2 for `id`, v1.0 for `qual`, …".
12. **VC1 22: "one of the step-10 read's four Q2 conditions", all four holding.** **Location:** E:42-44, D:57-62.
    **Verdict:** PASS. **Evidence:** read.md:45 states four "Conditions, all already Code's practice at step 10":
    - no change under `valence_core/m`;
    - "the build reviewed as the step-10 edit was, with the self-test extended";
    - the DRIVER-line record;
    - "the new PIN sites declared on C6's terms as extended".

    D lists all four, and each holds: site-wt's status shows the driver alone, there were three review rounds, and D
    §5 declares the sites. The driver's own PIN keeps the singular: item 33.
13. **VC1 26: the quote "comes with the driver's stage wiring (flag F-2)".** **Location:** D:64-65.
    **Verdict:** PASS. **Evidence:** `results/raw/2026-11-06_mf3-build_design.md:145` (1e79955) ends "…the SNAPSHOT
    line) comes with the driver's stage wiring (flag F-2)." D's quote is a substring. E:32 paraphrases without
    quoting.
14. **VC1 41: where each trap applies.** **Location:** D:207-219, driver :587-595. **Verdict:** PASS.
    **Evidence:** as item 2; each sub-list matches the code. Two details are left unsaid, and neither is a trap
    claim:
    - the seam call also stubs the checklist (:1274);
    - `stub_run`'s exit-code call passes its own `stage` (:1014-1015) and so runs no sessions.
15. **VC1 44: "every Qwen route closed".** **Location:** E:55. **Verdict:** PASS. **Evidence:** :764-772 close
    `qwen_or_explain`, `get_adapter` and the mlx / jlens_qwen imports. QwenMLXAdapter's constructor imports
    `mlx.core` and `jlens_qwen.model` first.
16. **VC1 47: the ten-suite run on the pre-pin bytes; the driver's suite on the final bytes.** **Location:**
    E:72-77, R:1210-1213. **Verdict:** PASS. **Evidence:**
    - C:21 records run 2 "before the help-pairing pin", and C:23-33 hold its results.
    - T and `sitecheck_out/mf3_sessions_final2.txt` give 160/160 on 890084e6 (item 25).
    - C:35's own wording has gone stale: item 34.
17. **VC1 48: which round's harness trapped what, and "The stage trap is the self-test's own".** **Location:** R:3.
    **Verdict:** IMPRECISE (low). **Evidence:** the harness sentences are right:
    - Round 1's `review/harness/trapped_selftest.py` traps `qwen_or_explain`, `QwenMLXAdapter` and `get_adapter`
      (:65-70) and blocks mlx, mlx_lm and jlens_qwen (:49). It hashes `data/mf3` before and after (R:34-37).
    - Round 2 "adds four more" (R:524-530): a write trap under `data/`, a network trap, a nested-`run_selftest`
      trap, and a sha256-and-mtime watch.
    - Round 3's harness keeps "every earlier trap" (R:1178).
    - None of the three `trapped_selftest*.py` files names the stage. In the mutation runs, the stage trap is the
      self-test's `t_stage` (driver :625-627).

    But R:3 names the state probes in the same sentence, and two of them trapped the stage themselves:
    - round 1's `review/harness/state_probe.py` (the seam probe, :95-99, "REVIEW-TRAP: stages.run_gate_stage
      reached");
    - round 2's `state_probe2.py` (:176), which patches `run_gate_stage` to raise.

    They call `run_time` outside the self-test, so "The stage trap is the self-test's own" does not describe them.
    The first pass's evidence covered the harnesses only.
    **Fix:** "In the mutation runs the stage trap is the self-test's own; rounds 1 and 2's state probes patched the
    stage themselves".
18. **VC1 51: round 1's NOTE 8, the stream unchanged and the texts changed.** **Location:** R:455-457.
    **Verdict:** PASS. **Evidence:** the two text changes are in item 7. Both lines still print to stdout (driver
    :1432, :1434). D §2 declares them.

## 2. The driver's new bytes

19. **The final bytes hash to `890084e6…90af`.** **Location:** E:3, D:6, C:39, T:1, R:1228, V:476. **Verdict:**
    PASS. **Evidence:**
    - wire-wt and site-wt give `890084e6c626a3ced2007c4285c255fb73978c07aeca15427172fc17028690af`, and `cmp` finds
      the two copies identical.
    - mut-wt, mut-wt2 and mut-wt3 hold the same bytes.
    - Cosmetic, as the first pass noted: E:3 still wraps the hash in double backticks.
20. **The 1773ae7f bytes used for the comparison.** **Location:** `time/driver_1773ae7f.py`. **Verdict:** PASS.
    **Evidence:**
    - The file hashes to `1773ae7f3dc3ddd256f5ff8188129397bf0b1ebbcf5f81da4b7c56beff6e9a56`, the full value the
      first pass recorded (VC1 2).
    - It differs from Code's `time/mut/final/r3_w3_letters_hyphen_only.py` by r3_w3's one line (:106) only.
    - Each of the other nine files in `mut/final/` differs from it by its own mutation only.
21. **"The fixes touch comments and docstrings only."** **Location:** V:477, E:76-77, E:85, C:39. **Verdict:** PASS.
    **Evidence:** `diff` 1773ae7f → 890084e6 has four hunks:
    - :81, the PIN comment: "values" becomes "form";
    - :85 → :85-86, the same PIN comment: one sentence added, which takes one more line;
    - :335 → :336, `driver_problems`' docstring: the ellipsis;
    - :586-590 → :587-595, `_selftest_time`'s docstring, rewritten.

    The tokenizer's comment lists (77 and 78 comments) differ only in the two PIN hunks.
22. **"Its code's syntax tree, docstrings stripped, is identical to `1773ae7f…`'s."** **Location:** V:477-478,
    C:39, E:77, E:85. **Verdict:** PASS. **Evidence:** from `vc_wiring2/ast_compare.py`:
    - With docstrings kept, the dumps differ in exactly two of the 12 docstrings: `driver_problems` and
      `_selftest_time`.
    - With all 12 stripped from both files, `ast.dump` is identical (sha16 `800898cead0189ab` for both).
    - Each file has 59 definitions and 1,668 constants; the constants differ only at the two docstrings.
    - Nothing reads a docstring at run time: there is no `__doc__`, `getdoc` or `getsource` in the driver.

    Note: one self-test check reads the driver's own text, comments included: `guard.forbidden_hits` over
    `REPO / DRIVER_REL` (:564, :572). The tree's identity alone therefore does not cover the comment changes. The
    160/160 re-run on these bytes does (item 25).

## 3. The runs the dispositions cite

23. **The reviewer-form mutants in `time/mut/final2/`.** **Location:** R:1228, V:448. **Verdict:** PASS.
    **Evidence:** `make_mutants_r3new.py`, run on 890084e6 into my scratch, gives files byte-identical to both.
    - r3_p2 removes `rs.refuse_ended(cpath)` after `checkpoint_path` and adds it after the CHECKPOINT EXISTS test
      (two replacements).
    - r3_g1 swaps the refusal block and the DRIVER print.
24. **"r3_p2 is killed 35/36 by the refused battery alone (CHECKPOINT EXISTS beside STAGE ENDED); r3_g1 is killed
    34/36 by the refused battery and multi (a DRIVER line on stdout)".** **Location:** R:1230-1231, V:448-451;
    `time/mut/final2_p2.txt`, `final2_g1.txt`. **Verdict:** PASS. **Evidence:**
    - The two files read 35/36 (failing: the refused battery) and 34/36 (failing: the refused battery and the
      multi check).
    - My in-memory runs of the same replacements on 890084e6 give the same counts and the same failing checks.
    - Recording `_say` under r3_p2: in the ENDED case without `--resume`, the REFUSED line carries CHECKPOINT
      EXISTS before STAGE ENDED; the `--resume` case does not carry it (`vc_wiring2/inmem_p2_say.txt`).
    - Under r3_g1 the DRIVER line prints before the refusal, so multi's `"DRIVER " not in` its stdout fails.
    - The runs were in the lanes at 1e79955. `final2_*.txt` were written at 22:06:51, the same second mut-wt's and
      mut-wt2's drivers were restored to 890084e6.
25. **The self-test on the new bytes: 160/160.** **Location:** `time/sitecheck_out/mf3_sessions_final2.txt`;
    E:75-76, E:85-86, C:41, V:479. **Verdict:** PASS. **Evidence:**
    - 160 `[PASS]`, 0 `[FAIL]`, and the last line reads "160/160 mf3 selftest checks pass".
    - It was written at 22:07:22, 59 s after site-wt's driver became 890084e6 (22:06:23).
    - It differs from `mf3_sessions_final.txt` (the 1773ae7f run) only in Python tempfile names (its lines 114,
      152 and 153), as code-identical bytes would.
26. **T is that run, scrubbed.** **Location:** T:1-170. **Verdict:** PASS. **Evidence:**
    - `diff` T against `mf3_sessions_final2.txt` shows only T's header (T:1-2) and the scrubs: INVOCATION (T:3,
      the interpreter's root as `<repo>`), T:105, T:112-113, T:116 and T:154-155. Nothing else differs.
    - T:167 (`driver_problems`: "working-tree bytes are not HEAD's blob") shows the driver uncommitted.
    - 36 of the 160 checks are `mf3_sessions:` checks.
27. **"All ten are killed", for the reviewer's own forms on the final bytes.** **Location:** E:66-67, E:70,
    R:1232-1240. **Verdict:** PASS (supporting). **Evidence:** my in-memory runs (`vc_wiring2/inmem_mut.py`,
    mut-wt3) applied the reviewer's exact replacement lists to 890084e6. Against a 36/36 baseline:
    - r3_g1: 34/36;
    - r3_p2, r3_g2, r3_g3, r3_g4, r3_g5, r3_h1, r3_pl1 and r3_w3: 35/36 each;
    - r3_k1: 15/16, raised at the constants check's `get_adapter` refusal.

    Each is killed by the check that R:1232-1238 names.

## 4. New errors in the changed text

28. **"Code's first runs (bytes `1773ae7f…9a56`) killed every mutant but r3_h1, which survived the presence-only form
    of the help check. The help-pairing pin was added, and r3_h1 was then killed on the bytes with it."**
    **Location:** R:1222-1223. **Verdict:** FAIL. **Evidence:**
    - The runs in which r3_h1 survived are `time/mut/lane1-3.txt`, written 21:22-21:23 (r3_h1: "RESULT 36/36").
    - Their mutants (`time/mut/mutants/`, 21:21:16) lack the help-pairing pin. Each differs from Code's
      1773ae7f-based mutant in `mut/final/` only by the pin's hunk (:783-789).
    - Undoing r3_w3's line gives their base, sha256 `360febd7…7150` (96,085 bytes, `vc_wiring2/driver_prepin_rebuilt.py`).
      It differs from 1773ae7f by the pin alone.
    - On 1773ae7f (`mut/final/`, `final1-3.txt`, 21:26) all ten were killed, r3_h1 among them at 35/36.
    - So the hash names the bytes after the pin, and the sentence contradicts C:35.

    **Fix:** "(the bytes before the help-pairing pin)", and "r3_h1 was then killed on `1773ae7f…`, where all ten
    were killed".
29. **"Two first builds were not the reviewer's mutants. The wiring values-check found both"; "r3_p2 and r3_g1 are
    counted as rebuilt in the reviewer's form".** **Location:** R:1224-1227, E:68-69 (and R:1215, "Code rebuilt the
    nine non-equivalent round-3 survivors"). **Verdict:** FAIL. **Evidence:** I ran the reviewer's generators on
    1773ae7f and compared their output with Code's `mut/final/` builds. r3_g2, r3_g3, r3_g5, r3_w3 and r3_k1 are
    byte-identical. r3_g1 and r3_p2 differ in kind (VC1 54). Three more differ too:
    - r3_h1: the reviewer's swaps the analyzer's and the package's help strings (`mutation_table.md` row 28). Code's
      swaps the package's and the renders'.
    - r3_pl1: the reviewer's replaces `lock_weights(lock_text)` with the hub binding at `gshape.QWEN_REVISION`,
      revision and sha256 both. Code's keeps `lock_weights` and takes only `weights_sha256` from the binding, at
      the lock's revision.
    - r3_g4: the same move (both ids dropped), in other words.

    No kill or killer changes: the reviewer's own three are killed on 890084e6 by the checks R names (item 27).
    **Fix:** count five first builds that differ, two of them in kind. Say Code's r3_g4, r3_h1 and r3_pl1 were
    variants of the reviewer's, or rebuild them from the generator.
30. **"(`890084e6…90af`, whose code is identical to `1773ae7f…`'s; §7 of the design raw)".** **Location:**
    R:1228-1229. **Verdict:** IMPRECISE. **Evidence:** D §7 (D:221-232) is "Records left as they are". D nowhere
    names 1773ae7f, the syntax tree or the values-check's fixes. The claim is in C:39 and V:476-479. **Fix:** cite
    the site-check raw's last section or the values-check raw.
31. **"Code's check on the final bytes: … All ten are killed"; "Verification by mutation, on the final bytes."**
    **Location:** E:66-67, R:1214. **Verdict:** IMPRECISE (low). **Evidence:**
    - Eight of Code's ten ran on 1773ae7f (`mut/final/`, `final1-3.txt`). Only r3_p2 and r3_g1 ran on 890084e6
      (`final2_*.txt`).
    - The substance holds: the code is identical (item 22), no mutation touches a changed line, and the reviewer's
      ten are killed on 890084e6 (item 27).

    **Fix:** "on `1773ae7f…` (code-identical to the final bytes); r3_p2 and r3_g1 on the final bytes".
32. **"The nine sites at the final bytes": :72, :81, :97, :107, :220, :283, :333, :358, :441.** **Location:**
    D:156-168. **Verdict:** FAIL. **Evidence:**
    - On 890084e6, `grep -n 'PIN ('` finds :72, :81, :98, :108, :221, :284, :334, :359 and :442.
    - The values-check fix added a line to the PIN at :81 (now :86), so every later site moved down by one. The
      table keeps 1773ae7f's lines (VC1 19).
    - LOCK-m-F3 v0.2 is to declare these sites.

    **Fix:** renumber the seven.
33. **The driver's PIN at :72: "(the step-10 read's Q2 condition, which Code reads F-1's "with the same scope" as
    carrying; …)".** **Location:** driver :76-77. **Verdict:** IMPRECISE (low). **Evidence:**
    - This is the phrase VC1 22 graded in E and D, which now say "one of the step-10 read's four Q2 conditions".
      The PIN keeps the singular.
    - It is pre-existing and outside VC1 22's locations.
    - A fix is comment-only, so the code's tree would not change, but it moves the blob; it may instead be left as
      it is, and noted.
34. **"The driver's suite on the final bytes (sha256 1773ae7f…)".** **Location:** C:35. **Verdict:** IMPRECISE.
    **Evidence:** C:39 now heads "The final bytes (sha256 890084e6…)", so C calls two different blobs "the final
    bytes". C:35 was true when it was written. **Fix:** "on 1773ae7f… (before the values-check's fixes)".
35. **"Code stamp at writing: 2026-11-08 02:32:25 UTC".** **Location:** C:2. **Verdict:** IMPRECISE (low).
    **Evidence:** C:39-41 report `mf3_sessions_final2.txt`, written at 22:07:22 local (03:07 UTC), after the
    stamp. The single stamp is the first writing's. **Fix:** stamp the appended section, or say that the stamp is
    the first writing's.
36. **"S in the report is the session's scratch directory".** **Location:** V:3. **Verdict:** IMPRECISE (low).
    **Evidence:** the report never uses S. It writes `scratchpad/vc_wiring/` (V:16, V:24), `time/…` and `site-wt/…`.
    **Fix:** drop the sentence, or name the form the report uses.
37. **"local roots are scrubbed" (V:3), and the 58 disposition's search, which reports no temp-root head and "no
    6-character piece of the id segment" (V:454-455).** **Location:** V:415, V:417, V:420, V:428. **Verdict:** FAIL.
    **Evidence:**
    - V:417 quotes, with an ellipsis, the first six characters of the macOS temp directory's id segment, and two
      fragments of the temp root's folder names.
    - V:415, V:420 and V:428 quote the temp root's truncated head.
    - All of these sit in the first pass's item 58 and totals, which V carries verbatim.
    - Item 56's evidence was reworded for exactly this reason (V:399-402), and V's dispositions report the search
      clean. V is a raw for commit.

    **Fix:** reword item 58's evidence, its fix line and the totals' FAIL entry as item 56's was, with the same
    disclosure. Then run the search over V as well.
38. **The 58 disposition: "The scrub now also replaces a truncated `<tmp>` head and the temp directory's id segment
    with `<tmp>`."** **Location:** V:452-453. **Verdict:** IMPRECISE. **Evidence:** the scrub rewrote Code's own
    words. `time/dispositions_vc.md` names the temp root's head at that place; as V has it, the sentence says the
    scrub replaces `<tmp>` with `<tmp>`. This is the only difference between V's dispositions and their source.
    **Fix:** describe the head in words, for example "the temp root's truncated head".

## Totals

38 items: **25 PASS, 9 IMPRECISE, 4 FAIL.**

- Section 1: all 18 of the first pass's items are resolved where they were flagged; 16 PASS. Two are IMPRECISE
  (low): VC1 13, whose D:161 register row was not updated; and VC1 48, whose new "The stage trap is the self-test's
  own" leaves out rounds 1 and 2's state probes, which trapped the stage themselves.
- Sections 2 and 3: all nine PASS.
  - 890084e6 changes only comments and two docstrings against 1773ae7f; the code's syntax tree, docstrings stripped,
    is identical.
  - Its self-test is 160/160, and T is that run, scrubbed.
  - The reviewer-form r3_p2 and r3_g1 are the reviewer's bytes and give the results stated.
  - The reviewer's own ten mutants are all killed on 890084e6.
- New errors (section 4):
  - FAIL: 28 (R:1222, the first runs' bytes named 1773ae7f, where they were the pre-pin bytes); 29 (R:1224 and
    E:68, "two" first builds not the reviewer's, where there were five); 32 (D:156-168, the PIN register's line
    numbers, stale by one for seven sites at 890084e6); 37 (V's report, which carries the temp directory's id
    fragment and the truncated temp root).
  - IMPRECISE: 30 (R:1229, "§7 of the design raw"), 31 (E:66 and R:1214, "on the final bytes" for runs on
    1773ae7f; low), 33 (driver :76-77, the singular "Q2 condition"; low, pre-existing), 34 (C:35, "the final
    bytes"), 35 (C:2, the stamp; low), 36 (V:3, "S in the report"; low), 38 (V:453, the scrubbed disposition).
- No finding touches the production code's behaviour, a hash of record, the self-test's outcome or a kill. The
  defects are in the records: one wrong hash attribution, one undercount of differing builds, stale line anchors
  from the values-check's own PIN fix, and an incomplete scrub of V.

## Code's dispositions of pass 2 (2026-11-07; each item re-checked at source, then the fix checked by tool)

- **8:** the PIN register's row for :81 now says "(m's TIME_* form)".
- **17:** the review raw's header now says that rounds 1 and 2's state probes, which call `run_time` outside the
  self-test, patched the stage themselves, and that in the mutation runs the stage trap is the self-test's own.
- **28 (FAIL):** confirmed. The first runs were on the bytes before the help-pairing pin (`360febd7…`), and on
  `1773ae7f…` all ten builds were killed. The review raw states the runs by bytes.
- **29 (FAIL):** confirmed. Five builds differ from the reviewer's generators: r3_p2 and r3_g1 in kind, and r3_g4,
  r3_h1 and r3_pl1 as variants. The review raw and the entry say so. The reviewer's own versions are killed on the
  final bytes (this pass ran them).
- **30:** the review raw now cites the site-check raw's last section and this raw for the code-identity claim, not
  the design raw's §7.
- **31:** the entry and the review raw now say which bytes each run used. Eight ran on `1773ae7f…`, whose code is
  identical to the final bytes', and r3_p2 and r3_g1 on the final bytes.
- **32 (FAIL):** confirmed. The fix at :81 added a line, so the design raw's PIN register is renumbered to the final
  bytes: :72, :81, :98, :108, :221, :284, :334, :359, :442. A script compared the cited lines with the driver's PIN
  openings, and they match.
- **33:** left as is. The PIN at :72 still says "the step-10 read's Q2 condition" in the singular. A further
  comment-only edit would move the blob once more for no change in code. The design raw (§2) and the entry list all
  four conditions. LOCK-m-F3 v0.2, which declares the PIN, can carry the plural.
- **34:** the site-check raw's section heading names `1773ae7f…` as the bytes before the values-check's comment fixes.
- **35:** the site-check raw's stamp is now "at the first writing", and the appended section carries its own stamp.
- **36:** this raw's header now describes the reports' path form.
- **37 (FAIL):** confirmed. Pass 1's item 58 evidence, its fix line and its totals entry are reworded so the raw does
  not spell out the temp root's fragments, with a disclosure. The search is re-run over this raw.
- **38:** the item-58 disposition now describes the truncated head in words.
