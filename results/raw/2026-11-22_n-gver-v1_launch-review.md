# n — G-VER's launch files v1: the blind launch review, as returned, with every disposition

PI date 2026-11-22. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over G-VER's launch files v1, at G-VER's BUILD `2834c2d`, before
the relay:
- the box script `gver_v1.sh` as it then stood, `cb17ca22…c27c` (449 lines); its manifest `69fa4ec4…0fb6` (66
  lines, unchanged since) with its builder `make_manifest_gver_v1.sh` `c83f0fbc…62dc`, G-TIME-n's builder under a new
  name; and the launch note's draft `3cc8b74f…35bb` (280 lines), its slots for the script's, the hashes file's and
  the tests' figures not yet filled;
- the laptop tests as they then stood:
  - the harness `8a486f21…286e` (303 lines) with its stand-in `28e7eb9a…69d0` (230 lines), and the harness's first
    run's output `a280e70b…f0df` (282 lines), from before one change to the script: its line 201 then held the
    section sign as the raw character;
  - the generator of the driver's own outputs, `gen_real_v1.py` `ff83a872…2073` (260 lines);
  - the snippet test of the script's Python check: `make_fixtures_v1.sh` `0706ae6e…5646`, `run_snippet_test_v1.sh`
    `cda637b4…d8e2` and `make_sample_v1.sh` `21bcfe98…fb8d`, with its dry run's output `c1ae8b8c…9bf3`;
  - the generator and the snippet test had not yet run: their battery window came after the review;
- the model, G-TIME-n's launch files: `gtime_v1.sh` (`eeee8c2e…39b6`) and its launch note v2 (`87a1d360…3cd0`),
  read where they help.

Each file as reviewed is kept in Code's scratch.

**The reviewer's brief** (`76856239…42e2`, 114 lines):
- named those files by sha256, each to be verified before it was read (the box script whole, G-TIME-n's files where
  they help), and the code they must match at `2834c2d`:
  - the driver's G-VER section and `main()`'s `gver` branch, with the helpers they call;
  - `ids.py`'s `load`, `verify.py`'s report and `_masked`, and `m/resume.py`'s `json_text` and `atomic_write_json`;
  - the seat's raw of 2026-11-22 (§1.2–§1.4, §1.6, §2 and §6), the BUILD's review raw and entry;
  - CLAUDE.md's respawn protocol, its rules 2 and 27, and the `.gitignore`'s G-VER block;
- quoted the coordinating session's request for the launch files (its six items) and the hash-refusal procedure as it
  agreed it with the pod session;
- listed, to be checked, what Code declared: two readings added to Code's INTEGRITY list; the box's count of 728 by
  arithmetic; the manifest; the wall time in whole seconds; the environment held; and the exit 4;
- asked for findings, surviving mutants, box risks, observations and any command a rule bars. It also quoted the list
  of record v2's items 1–5 and the rules on interpreters, writes, guard markers, `data/m[f]3`, and ckpt and reports
  files.

One error of Code's in the brief: it said the generator makes 30 refusals. It made 27, as the review's O6 found, and
it makes 28 since O2's case.

**The report** is in §3, as returned: the subagent's hand-back message, by `jq` from its transcript (171 lines,
sha256 `0ab03938…6107`). It names scratch files only as `S/...`. Its own hash abbreviations are kept as it wrote them,
five-character tails among them.

**Totals:** no BUG; 4 RISK (F1–F4) and 8 NIT (F5–F12); 14 surviving mutants (M1–M14); 10 box risks (B1–B10); 11
observations (O1–O11).

## 1. Dispositions

The dispositions as Code wrote them after the review (`fe32ad76…e781`, 95 lines), below from their first section
on, with their headings one level down.

### Findings
- **F1 (RISK), nothing checked the copy between the self-test and the stage. Applied.** Step 3b runs copy_clean and
  the data/n/gver test again after the self-test and hashes; on a failure the stage does not start ("STAGE NOT
  STARTED: the copy changed during the self-test or hashes (step 3b)"), and the end is FAIL. Cases st_stray, st_gver,
  hashes_pycache; rgit2 now fails at 3b. Mutants G40–G42.
- **F2 (RISK), the weights folder missing classed INTEGRITY against the seat's "a missing folder". Applied.** The
  pattern is removed: the weights folder missing is the seat's "a missing folder", a FAIL of the launch. The header and
  the INTEGRITY end's words name what remains: a file's hash, byte count or record count, or the weights folder's
  listing of its files. The two kinds of "missing" stay apart, and the note says why: one of the eight is a file on the
  box's volume, which Code's reading in the BUILD's entry covers; an ids file is the copy's, which step 1 has just
  checked at the commit's bytes (a file missing there is a FAIL of the launch, its sparse checkout).
- **F3 (RISK), a step-1 failure always FAIL. Applied.** The script classes step 1's output: a file off the commit's
  bytes after a clean checkout (shasum's "FAILED") is of the INTEGRITY kind, exit 4, on Code's reading (the copy's files
  of record changed on the volume); a file missing ("FAILED open or read") or an unreadable manifest is a FAIL of the
  launch. Cases rman and rman_assume (a change git status cannot see: assume-unchanged) INTEGRITY, rman_missing FAIL;
  mutants G25–G25d. The note says that the manifest-pin STOP and ids.load's sha256 and count refusals cannot fire on
  this launch (O7).
- **F4 (RISK), no bound on the stage's stdout. Applied.** At PASS and STOP the stdout must be the driver's 20 lines
  alone. G-TIME-n's run of record on this box printed its 52 declared lines and no other (its committed out file), so
  no library writes to stdout there. Cases pass_foreign, stop_foreign; mutants P30, G46.
- **F5 (NIT). Applied:** the harness's comment on the symlink case corrected, its want pinned to "the copy's changed
  set"; the -L halves of the data/n/gver tests declared equivalent in the mutation tool's header.
- **F6 (NIT). Applied:** the note's tool check names what the script runs beyond bash's builtins.
- **F7 (NIT). Applied:** the note and the header: a kill can leave the empty data/n/gver/, or a record that was never
  read back or checked, which is not of record.
- **F8 (NIT). Applied:** the usage error moved to "anything else".
- **F9 (NIT). Applied:** the wall times are in ms, by bash 5's EPOCHREALTIME (whole seconds only on a bash without
  it), so the two durations lie inside the stage's wall time to the millisecond.
- **F10 (NIT). Applied:** the procedure's trigger is the script's INTEGRITY end, and, on the pod session's own reading,
  the agreed "a refusal on a hash or byte count" with Code's listed readings; "a pin" is dropped. At INTEGRITY nothing
  at all comes back before the coordinating session's word.
- **F11 (NIT). Applied** in the harness's header. **F12 (NIT). Applied:** the exit file is among the raws.

### Surviving mutants
- **M1:** killed by stslow (a self-test of 3 s: the stage's wall time under 3,000 ms, the launch's at least 3,000);
  mutants G43–G45.
- **M2, M3:** "read together: none-of-the-four" checked on ref_pod_exit2 and ref_tok_record (and ref_r6_after,
  ref_tok_noend).
- **M4:** flows stop_norec and stop_symlink. **M5:** failed_exit2.
- **M6:** each INTEGRITY case checks its exact reason.
- **M7:** the stand-in refuses a driver call whose working folder is not the copy; mutants G35, G36.
- **M8:** the stand-in's self-test writes its warning to stderr, and work/selftest.txt must hold it; mutant G37.
- **M9: declared equivalent, after a test.** Case gexcl (GIT_CONFIG_GLOBAL with an excludes file listing gver.json)
  was added as the review proposed, but its mutant (G39) survived the first mutation pass: the repo's .gitignore names
  every path the record can take (`!/data/n/gver/`, `!/data/n/gver/gver.json`), and git gives a .gitignore's patterns
  the last word over core.excludesFile, so no global exclude can hide the record. A global exclude elsewhere moves a
  stray from `??` to `!!`, which the two-status comparison refuses either way. The override stays, as at G-CAL-n's
  and G-TIME-n's launches; gexcl stays as the case that a global excludes file does not break a PASS; the mutation
  tool's header names G39 as equivalent.
- **M10:** case gidx (a tracked file's mtime moved; the copy's index byte-identical after the run); mutant G38.
- **M11:** each refusal and failure print check has a flow that fails it alone and a check of its message, and the
  end line's "prints 0" or "prints 1" is checked (ref_tok_refx, ref_tok_dupend, ref_tok_gverx, failed_form,
  failed_failx, failed_dupend, failed_nohead, failed_gverx, failed_durline).
- **M12:** verify_moved and verify_other (the line-after test), pass_refusedline, pass_failedline and pass_tbline.
- **M13:** gen_real's clock gives 3 ms and 7 ms; snippet mutant m54. **M14:** fixture m_long; snippet mutant m55.

### The mutation pass after the dispositions
The first pass ran 141 mutants in four lanes (null mutant first: 649 of 649 in mutation mode): 129 killed, 12
survived. G39 is M9's, declared above. The other 11 are the per-kind line counts of check_prints (P2, P4, P6, P8,
P10, P12, P14, P16, P19, P22, P24): with F4's 20-line bound, every case that doubles a kind also adds a line, so the
end alone could not show a count. The harness now checks each count's own message in the variant cases at PASS and
at STOP, and the 11 are re-run.

### Box risks
- **B1:** declared; the count is by arithmetic, and G-TIME-n's merged form held on this box.
- **B2: Applied:** `grep -a` in c(), the line-after test and integrity_of (equivalent on the laptop's valid text;
  declared in the mutation tool's header).
- **B3:** declared; at a failure the out file prints both statuses.
- **B4: Applied:** an exception whose traceback names check_weights_folder or gver_hashed_files ends INTEGRITY (Code's
  reading, for the seat); cases tb_weights, tb_hashed; mutants I12–I14.
- **B5: Applied in the note:** a "PID alive at +30 min" report; the end-wait stays on the PID alone.
- **B6:** as F7. **B7: Applied in the note:** the python of G-TIME-n's launch, which R6 characterized.
- **B8:** declared; no HF offline variables on the box, as at G-TIME-n; the stage loads the tokenizer with
  local_files_only. **B9, B10:** noted.

### Observations
- **O1, O3, O9–O11:** noted. **O2:** the v block's base text is now generated (gen_real's ref_idsbase_v, replayed
  as INTEGRITY). **O4:** agreed: the window request names `a853932b…522b`, and any other is a stop. **O5:** every test
  re-runs on the final bytes. **O6:** Code's error, above. **O7:** in the note.
- **O8: Applied:** a record standing at an end that is not PASS or STOP comes back only on the coordinating session's
  word, to a folder of its own, marked not of record (the script's line and the note).

### The reviewer's departures (for the entry)
One grep refused by the permission system before it ran (its glob would have put the adapter module's marker-named
path in its argv); one zsh loop over PATH refused by a safety check (no marker); reads beyond the brief's list, not
barred; `git diff --name-only` and `git ls-files` printing marker-holding names in their output only.

## 2. The tests after, on the bytes for the relay

The script as relayed is `34103c35…6f63` (490 lines, ASCII), with the dispositions above applied. On it:
- **the harness:** 677 checks of 677 (`da871f03…c91a`), and 677 of 677 as the null mutant, in the mutation tool's
  mode;
- **the mutation pass:** 141 one-line mutants in four lanes, 129 killed and 12 surviving. The 11 per-kind line counts
  among the 12 were each killed in one re-run, after the harness gained a check of each count's own message. The
  twelfth, G39, is equivalent (M9 above), so the tool lists 140, all killed;
- **in one battery window the coordinating session granted:**
  - `hashes` from a `git archive` of `2834c2d`: 13 lines, `a853932b…522b`, byte for byte G-TIME-n's;
  - the generator: 32 cases of 32 as wanted, exit 0, stderr empty (`5489ab42…3ba3`);
  - the snippet test: 90 fixtures of 90 and 54 mutants of 54 killed (`f80420c6…e93f`);
- **the replay** of the generator's 32 outputs through the script: 128 checks of 128 (`141655e2…9f69`). It found PASS
  once, STOP twice, INTEGRITY 10 times and FAIL 19 times.

The set went to the coordinating session frozen: its set note `eee0e3de…5ed4` and its index `64407bfa…f3cc`. It was
cleared and ran on the box, where it ended FAIL at its self-test, 726 of 728 (G-VER's entry). Launch files v2 moved
the self-test's temporary folder to the box's local disk. On the coordinating session's call, that delta had no
blind review of its own.

## 3. The report as returned

BLIND REVIEW: G-VER of record's launch files v1 (n §8 step 12)

SETUP CHECKS
- All 14 named S files are at the brief's sha256s (shasum).
- These are tracked and clean at HEAD 2834c2d (rev-parse = hash-object): scripts/n_sessions.py (sha256 55885e65…385f), valence_core/n/ids.py, valence_core/n/verify.py, valence_core/m/resume.py and .gitignore (81f5f227…b610). `git diff --name-only HEAD` with item 3's pathspec and Q-F3's exclusion is empty.
- Verdict in short: I found no BUG. The script's ends, classes and checks are right on my reading. The defects are classification gaps against the seat's §1.4, two test gaps, and the surviving mutants below. None of them can produce a wrong PASS.

THE SIX ITEMS AND THE PROCEDURE: WHETHER THE FILES CARRY EACH, AND WHERE
1. The hash-refusal procedure, on Code's INTEGRITY reading: carried.
   - Note: "The INTEGRITY kind" (192–218) and "The hash-refusal procedure" (220–230). Its four points are the agreed text, with "me" written as "the coordinating session". Also the end (238) and the copy-back (253–254).
   - Script: the patterns INTEGRITY_RES (103–112), integrity_of (354–363), exit 4 (431–435, 447) and the header (46–48).
   - Deviations: F2, F3, F10.
2. F5 and B5, the three-way reading with stderr captured: carried.
   - Step 5 reads the exit, the last stdout line and the record together (381–392).
   - The stage's stderr goes to <work>/gver.err (373) and is printed after the run (378). The self-test's stderr is merged into selftest.txt (170); hashes' stderr goes to the out file (181).
   - Note 34–36 and 138–150. The labels have gaps: M2–M5.
3. B3, the cuBLAS export: carried. Exported at 139–140, before any Python runs, with the prior value printed. Note 37–38 and 107.
4. B6, the copy-back against the printed sha256: carried.
   - The record's sha256 is checked against the stage's printed line (398–403).
   - At every other end the script prints "no record stands" or "RECORD STANDS" (436–440).
   - Note 39–41 and 249–259.
5. B8, the checkout at 2834c2d: carried. COMMIT is pinned (53) and HEAD checked (155–157). Note 42–43, 62–74 and 97–101.
6. F11, the wall time: carried. The stage's wall time from SECONDS (372–377) and the launch's (442), in whole seconds. Note 44–45 and 133–135. See M1 and F9.

FINDINGS
- F1 RISK. S/step4b/gver/launch/gver_v1.sh, 165–188 and 365–379: nothing checks the copy between steps 2–3 and step 4.
  - A side effect of the self-test or of hashes in the copy is seen only after the stage of record has written its record. That includes a stray or ignored file, and data/n/gver itself (the BUILD review's B1 hazard).
  - At PASS it turns the run into "FAIL … RECORD STANDS": the run of record is lost and a v2 is needed. At a refusal it is blamed on the stage ("COPY FAIL after the refusal", or "exists").
  - G-TIME-n's smoke ran copy_clean between its self-test and its run. G-VER has no smoke, so nothing sits there.
  - Right today: by my reading the self-test at 2834c2d writes nothing into the copy.
  - Fix: run copy_clean and the data/n/gver absence check again before step 4. On a failure print "STAGE NOT STARTED" and end FAIL. Add a harness case whose stand-in self-test writes stray.txt, and one that makes data/n/gver.
- F2 RISK. INTEGRITY_RES[2] (line 106), the note's INTEGRITY item 3 (201–205) and its FAIL list (211–214).
  - The script classes the weights folder missing ("the weights path … is not a folder on this box") as INTEGRITY, as "Code's reading, added here".
  - The seat's §1.4 lists "a missing folder" among the FAILs of the launch. The note's FAIL list, "as the seat lists them", silently drops that item.
  - This is the safer side, but it departs from the ruling's words without saying so.
  - It is also inconsistent: a missing ids file ("listed in MANIFEST.json but absent") is FAIL, while a missing one of the eight is INTEGRITY.
  - The script's own wording omits the folder: header 46–47 and the INTEGRITY end's reason (434) say "a file's hash, byte count, record count or listing".
  - Fix: quote the seat's "a missing folder" and state the reading, or put it to the seat. Name the folder in 46 and 434.
- F3 RISK. Step 1 (165–166) and the note (216–230): a step-1 failure is always FAIL ("gver v1 FAIL: the manifest").
  - Step 1 is the first check to see three of the seat's classes:
    - an ids file off its sha256 (INTEGRITY, §1.4);
    - MANIFEST.json off its pin (G-VER's STOP with a record, §1.2);
    - LOCK-n.md or the driver off their bytes (FAIL).
  - The copy is a fresh git checkout, so a mismatch there means bytes changed on the volume: a question about what the box holds.
  - The procedure reaches only REFUSED lines. Step 1 prints shasum's "FAILED" lines, so the procedure never covers it. The note never says how a step-1 failure is classed.
  - Fix: say in the note that a step-1 failure on an ids file or the model manifest is reported word for word under the procedure (or is the seat's to class). Alternatively, the script classes step 1's FAILED lines by path and exits 4 for those.
  - Also say that the manifest-pin STOP is unreachable on this launch by construction (O7).
- F4 RISK. check_prints (274–316); the header (31) and the note (153) claim "each line … as declared".
  - Each declared kind is counted, but the total is never bounded. A foreign stdout line passes at PASS and at STOP: a library printing to stdout, or a driver line no pattern names. "The stage's prints: as wanted" is printed anyway.
  - The driver prints exactly 20 lines at both ends: STAGE, WEIGHTS, DRIVER, LOCK-n.md, the ids line, backend, package, 8 hashed lines, the G-VER line, verify's report, durations, record, end.
  - Fix: require 20 lines (`wc -l`), and add a print mode that adds a foreign line.
- F5 NIT. S/step4b/gver/launch/test/harness_gver.sh 279–282: the comment says git lists neither an empty record folder nor a symlink in its place, "so the existence check alone sees it".
  - That is false for the symlink. `/data/n/*` ignores it, and `!/data/n/gver/` matches folders only. The run ended at step 0's status check: "rgver_link: … FAIL: the copy's changed set" (S/step4b/gver/launch/test/harness_run1.txt:280).
  - The loose want ("gver v1 FAIL:") hides this. The script's `-L` branch (160) is reached by no case, and it is redundant on any git.
  - Fix: correct the comment and pin the want to "the copy's changed set".
- F6 NIT. Note 102–103: `command -v git shasum sed grep cmp tee tail cut`.
  - The script runs no sed. It runs head, cat, dirname, basename, mkdir and rmdir, all coreutils, as are tee, tail and cut, which are listed.
  - So "the script's tools beyond coreutils" is inexact. Fix: list what the script runs beyond bash builtins.
- F7 NIT. Note 243–247 (a kill), and the script header 9–10.
  - A kill can also leave the empty data/n/gver/ (the mkdir before the write).
  - A record a kill leaves behind was never read back or checked. The note should say it is not of record and nothing of it is copied back, as the script says at its own non-PASS ends.
  - The header's "writes its record … at PASS and at STOP only" also omits the empty folder after a failure at the record (which 426 handles).
- F8 NIT. Note 211–214: "a usage error" is listed among the REFUSED-line FAILs. argparse's error is not a REFUSED line: it is exit 2 with no stdout, the table's "anything else". Move it there.
- F9 NIT. Note 133–135 and script 377: "both lie inside the wall time".
  - That holds for the true elapsed time. The printed figure is a difference of SECONDS values (whole seconds at both ends), so it can fall up to a second short. The printed whole seconds could, in principle, be less than the two durations' sum.
  - In practice the imports and the CUDA context leave a gap of seconds. Fix: say "to within a second", or time the stage with GNU `date +%s%N` on the box.
- F10 NIT. Note 222–224 and 253–254.
  - The agreed trigger is "a refusal on a hash or byte count". The note widens the pod session's "safer side" to any REFUSED line naming "a pin" (and more).
  - A pin covers most FAIL-class refusals: the weights' aggregate, the driver's and LOCK-n.md's bytes, n's identifier, tokenizers' version, the package and closure. The pod session's class could then differ from the script's last line.
  - At INTEGRITY only the out file is said to wait for the word. The exit file, gver.txt, gver.err, selftest.txt and hashes.txt are not mentioned.
  - Fix: keep the agreed trigger plus Code's listed readings, and say nothing at all comes back before the word.
- F11 NIT. harness_gver.sh header (2–7): "writes a new numbered folder … and removes nothing". It also makes outside_<i> beside runs_<n> (260) and chmods the stand-in (23).
- F12 NIT. Note 260–262: the raws to commit omit the exit file. G-TIME-n committed results/raw/2026-11-21_n-gtime-v1_exit.txt.

SURVIVING MUTANTS
By my reading, each passes every harness case (bash) or every fixture (the Python check). Impact is low unless stated.
- M1 (F11), line 375: `GT=$((SECONDS - T0))` becomes `GT=$SECONDS` (or 372 `T0=0`).
  - The stage's wall time would include steps 0–3. Every case only matches `[0-9]+ s`.
  - Kill: a stand-in self-test mode that sleeps 2 s, with `hasre "^the stage's wall time \(F11\): [01] s"`.
- M2, line 389: drop `[ "$GX" = 1 ] &&`. ref_pod_exit2 and ref_idssha_exit2 keep their rc and fragment, but are read as "refusal". Kill: `has ref_pod_exit2 "read together: none-of-the-four"`.
- M3, line 389: drop `&& [ "$RECP" = absent ]`. ref_tok_record and ref_offpin1_record still pass. Kill: `has ref_tok_record "read together: none-of-the-four"`.
- M4, line 388: drop `&& [ "$RECP" = on-disk ]`.
  - No flow ends with exit 2, the STOP line and no record (or a symlink or folder). The verdict stays FAIL by the record line, but the end is read as STOP.
  - Kill: stop_norec and stop_symlink flows.
- M5, line 390: drop `[ "$GX" = 1 ] &&`. No flow has the FAILED end line with another exit. Kill: a failed_exit2 flow.
- M6, line 359: echo `$x` (the pattern) instead of `$r`. The cases `has` only the prefix "…INTEGRITY kind: ". Kill: `has` each case's exact reason.
- M7 (medium), lines 170 and 181: drop `cd "$FR" &&`.
  - The stand-in answers --selftest and hashes from any working folder.
  - On the box, the self-test and hashes would then run on whatever scripts/n_sessions.py the wrapper's working folder holds.
  - Kill: the stand-in refuses (exit 3) unless its working folder is the case's copy.
- M8, line 170: drop `2>&1`. The stand-in writes its self-test warning to stdout. Kill: write it to stderr, and check work/selftest.txt holds it.
- M9, line 145: drop `-c core.excludesFile=/dev/null`.
  - Kill: run the pass case with GIT_CONFIG_GLOBAL pointing at a config whose excludes file lists gver.json. Without the override, A is empty and B2 lists the record.
- M10, line 145: drop `GIT_OPTIONAL_LOCKS=0`. Kill: the copy's .git/index sha256 before and after the pass case.
- M11, line 325 deleted, or any one check of check_failed_prints (340–350).
  - At a refusal or failure, the prints check never moves the verdict. ref_hashedline(_env) only checks rc and fragment, and no failed-flow negative case exists.
  - Kill: `has ref_hashedline "PRINT FAIL: lines of G-VER's run 1"`, plus failed flows with a stray durations line, a missing G-VER line, or a line between FAILED and the end.
- M12, lines 304–307 deleted, or line 312 deleted.
  - No mode reorders lines, and no PASS-shaped flow prints a REFUSED, FAILED or Traceback line.
  - On the box the Python check's verify-line check covers 304–307. Only the driver's control flow covers 312.
  - Kill: a mode swapping the verify and durations lines, and a flow printing a FAILED line before the PASS end.
- M13 (Python), lines 257–258: compare `[d["decode"], d["tokenizer_load"]]`, swapped.
  - gen_real's clock ticks 1 ms per call (S/step4b/gver/launch/gen/gen_real_v1.py:65–70). Every real output has 1 ms and 1 ms, and W2 cannot tell them apart either.
  - Kill: unequal ticks in gen_real (e.g., 1 ms, then 7 ms).
- M14 (Python), line 248: `re.fullmatch` becomes `re.match`.
  - No fixture has more than 64 hex (m_short has 63). Kill: an m_long fixture ("d"×65 on stop_ne, want 1).
  - Unreachable on the box: the driver's check_gver holds hex64 before writing.

BOX RISKS
- B1. The self-test count of 728 is by arithmetic (14 HF checks in place of 3 skip lines, as G-TIME-n's 645 vs 634).
  - A different count stops the launch before the stage: a safe FAIL, but a lost launch and a v2.
  - The count must also be the last line of a merged stdout and stderr file. A stderr write during interpreter teardown would stop the launch. G-TIME-n's form held on this box.
- B2. The harness's tools differ from the box's.
  - Laptop: /usr/bin/grep is BSD 2.6.0 (zsh's `grep` function is not inherited by bash, and PATH holds no other grep), bash is Homebrew's, git 2.39.5.
  - Box: GNU grep, Ubuntu bash, git 2.43.0.
  - New relative to G-TIME-n's script: `grep -A 1` (304) and the per-pattern `grep -q -E` with process substitution (356–361).
  - In a UTF-8 locale, GNU grep's binary-file heuristic suppresses matching lines in a file holding an invalid byte. integrity_of would then see no REFUSED line (FAIL instead of INTEGRITY), and 304 would fail. Unlikely, since the stage prints UTF-8.
  - Fix: `grep -a` in those two places.
- B3. git 2.43.0: the post-stage check relies on `--ignored` listing an ignored file inside the record's untracked folder (pass_ignored, pass_extra). This is shown on 2.39.5 only. G-TIME-n's form kept its root out of `--ignored`.
- B4. An OSError in the weights checks is not caught: os.listdir or stat in check_weights_folder, read_bytes in gver_hashed_files (EIO, EACCES).
  - It ends with a traceback on stderr, exit 1 and the STAGE line last: "none of its four", FAIL. By cause it is about what the box holds.
  - The pod session should read gver.err before classing.
- B5. No planning time and no escalation bound. A hang (e.g., a CUDA init stall) waits on the PID indefinitely.
- B6. A kill after os.replace and before the read-back leaves an unchecked record (F7). The note's pgrep step covers the orphaned python behind tee.
- B7. <python>: R6 refuses any interpreter but the characterized one, so a wrong one is a safe FAIL. The note does not name the interpreter G-TIME-n's launch used.
- B8. Environment differences.
  - The laptop's self-test ran with HF_HUB_OFFLINE=1 and TRANSFORMERS_OFFLINE=1. The box's self-test and stage run without them, as G-TIME-n's did. The stage's tokenizer load is local_files_only.
  - The self-test, hashes and the stage run without -I, so PYTHONPATH and user-site are honored. The closure guard and the package pin catch a foreign valence_core.
- B9. The volume: the self-test's TMPDIR is under /workspace (the BUILD's symlink fallback is handled). The record's atomic write and directory fsync are on the same volume as G-TIME-n's artifact, which held.
- B10. RUNPOD_POD_ID: a whitespace value passes the script (369) and is refused by the driver. A safe FAIL.

OBSERVATIONS
- O1. Every line the script matches is a driver f-string, verbatim.
  - The lines: STAGE (with _shown → data/n/gver/gver.json), WEIGHTS, DRIVER, LOCK-n.md, the ids line in both forms, backend, package, hashed file, the G-VER line, verify's json.dumps(sort_keys) (starting '{"first_problems": '), durations, record, and the PASS, STOP, refusal and failure ends.
  - Also the FAILED and REFUSED prefixes and the self-test count line.
- O2. All 8 INTEGRITY patterns are real texts: of gver_hashed_files (2), check_weights_folder (3) and ids.load (3).
  - No FAIL-class text the driver or ids.load can raise matches any of them.
  - For a missing or symlinked one of the eight, check_weights_folder's listing or byte-count refusal fires first. GV3's "not a regular file" is reachable only if the folder changes between the two checks.
  - The v-block base text ("(i)-(iv) part … v block") is matched by pattern 8 on reading only; gen_real does not generate it.
- O3. The manifest.
  - 49 of its 66 lines verified by `shasum -c` against HEAD's clean files (the lines without the marker).
  - Between 91f0d35 and 2834c2d, `git diff --name-only` shows only scripts/n_sessions.py among the 66 changed. So "one line differs" holds, and the other 17 are G-TIME-n's box-checked bytes.
  - HNAMES and HSHAS, the aggregate, n_files 22 and the revision's hex form match the model manifest's instruct entry (read with the file tool). The eight files total 9,730,209 bytes (≈9.7 MB).
- O4. The package and closure are unchanged since G-TIME-n, so gver_hashes_v1.txt should be byte-identical to G-TIME-n's gtime_hashes_v1.txt and to the committed box raw results/raw/2026-11-21_n-gtime-v1_hashes.txt (a853932b…a522b). Any other @HSHA@ is worth a stop.
- O5. Both test outputs predate line 201's change.
  - dry_1.txt's snippet is 9a9b1361…. The current lines 194–270 hash to 0b051a34…47ac9.
  - harness_run1.txt is likewise from the earlier draft.
  - The change is inside the heredoc, which the stand-in does not execute, so by reasoning the result carries over. Still, re-run both the plain harness and the GVER_REAL replay on cb17ca22… so that @TESTED@ names the final bytes.
- O6. gen_real has 31 cases: pass, stop, stop_ne, failed and 27 refusals (10 of the INTEGRITY kind, 17 FAIL). That is not "30 refusals".
- O7. On this launch the manifest-pin STOP (L:543) and ids.load's sha and count refusals are unreachable. Step 1 holds MANIFEST.json and the ids files at the commit's blobs, and MANIFEST.json's blob is the pin. IDS_NE_RE and the stop_ne cases are for completeness.
- O8. At a STOP whose launch checks fail (e.g., a stray file in the copy), the script withholds the record from the copy-back. §1.3's read would then lack it. The coordinating session may want it copied back as evidence, marked not of record.
- O9. At refusals and failures, the prints check (PR) never changes the verdict; it is descriptive only. This is consistent with §1.4.
- O10. The copy-back lands in scratch, which is cleaned after about four days. Commit the entry promptly.
- O11. Code's six declarations hold:
  - the two INTEGRITY additions are in the script and in the note's items 3 and 5;
  - 728 is by arithmetic;
  - the manifest is G-TIME-n's list at the new blobs, with one line different;
  - the wall time is in whole seconds;
  - ENV_PINS equals CHARACTERIZED_PROVENANCE's Python and six libraries plus LOCK_TOKENIZERS;
  - exit 4 is never the stage's: run_gver returns 0, 1 or 2; argparse exits 2; Python 1 or 2; signals 128+n.

DEPARTURES
- One command was refused by the permission system before it ran. It was a grep whose file arguments included the glob valence_core/adapters/*.py, which would have expanded to the marker-named adapter module in grep's argv. It is a breach had it run. It did not run, and I re-ran the grep on resume.py alone.
- One command was refused by a safety check before it ran: a zsh loop over PATH's entries. It held no marker.
- Reads beyond the brief's list, not barred:
  - G-TIME-n's committed box raws: out, selftest, run-err and exit, plus the sha256 of its hashes and selftest raws;
  - the BUILD's self-test raw;
  - the model manifest, with the file-reading tool only;
  - parts of .gitignore and guard.py, and further sections of the driver (its docstring, cmd_hashes, cmd_selftest, _package_closure, and G-TIME-n's self-test guard lines).
- `git diff --name-only` (91f0d35..2834c2d and HEAD) and `git ls-files`, each with the pathspec, printed marker-holding names in their output only.
- Otherwise none. No interpreter but shasum, no write, no network. No marker in any argv or command text that ran. Nothing under data/*/ckpt, data/*/reports or data/m[f]3 was read, listed or sized. No whole-tree git status. In S, only the named files were read.
