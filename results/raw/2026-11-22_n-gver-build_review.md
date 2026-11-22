# n — G-VER of record's BUILD: the blind review of draft 1, as returned, with every disposition

PI date 2026-11-22. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over the change as draft 1 had it, at HEAD `d92500b`:
- `scripts/n_sessions.py`, HEAD's (`4616f9c3…2553`) to draft 1 (`f5baf379…7b2c`, 6,031 lines);
- `.gitignore`, HEAD's to the draft with one block added for G-VER's record (`2e105c34…d8a8`).

Draft 1 had passed its self-test, 687/687, in a battery window.

**The reviewer's brief** was given to the reviewer as its prompt: Code's scratch file `S/step4b/gver/review_brief.md`
(`d9ad5c96…9411`, 102 lines). It:
- named the change and the specification: G-VER's spec raw and the seat's block, both committed at `d92500b`, the
  texts, and the code the change must match;
- named eight things Code knew of, to be declared;
- asked for findings, surviving mutants, box risks, observations and departures;
- barred any interpreter but `shasum`, any write, any network, any guard marker in an argv (a grep pattern and the
  command's own text included), and Q-F3's folder by its plain name in any argv;
- barred anything under `data/m[f]3`, any whole-tree git status, any read, listing, size or time of a ckpt or reports
  file, and anything in Code's scratch but the two named files and the brief itself;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec with `':!data/m[f]3/**'` on every
  git command over the tree.

**The report** is in §2, extracted verbatim by `jq` from the hand-back in the subagent's own transcript (164 lines,
sha256 `3bb14a39cf22642726a4439b8dcc958e9047d7ce101326caf3c8867c2108411d`). It names scratch files only by their paths
inside the scratch folder.

**In sum:**
- one BUG, F1;
- 11 findings: F1 BUG, F2–F7 RISK, F8–F11 NIT;
- 17 surviving mutants, M1–M17;
- 8 box risks, B1–B8;
- 7 observations, O1–O7;
- one departure, a glob in a grep's arguments before the folder was listed.

**The drafts after it:**
- Draft 2 (`3df537d6…83c1`, 6,195 lines) builds in F1–F4, F6–F9 and F11, a kill for every mutant (by Code's reading
  of each case, not by a mutation run), and B2; F10 is in the `.gitignore`'s second draft. It passed its self-test,
  716/716, in a battery window.
- Draft 3 (`8df113e4…3f02`, 6,195 lines) is draft 2 with one stale docstring (two lines) corrected:
  `gver_environment`'s, which still said GV4 held no pin on tokenizers' version. The supplement's values-check found
  it (its observation 6). Draft 3 passed its self-test, 716/716, in its own window.
- Draft 4 (`55885e65…385f`, 6,224 lines), the BUILD's driver, is draft 3 with the seat's hash set: GV3 hashes the
  weights folder's eight non-shard files, not the three tokenizer files (the seat's §1.2). With it come the record's
  field `hashed_files`, the renames that follow it, and the module docstring's `gver` paragraph as ruled. Draft 4
  passed its self-test, 717/717, in its own window.

F5 is carried to the launch files. Of the box risks, B2 is applied in the driver, and B4 in draft 4 as the seat ruled
it (§1.2); B3, B5, B6 and B8 go to the launch files; B1 is agreed, and B7 declared and ruled (§1.6). Five items change
what the seat's block (`d92500b`) says or asks: F3, F4, O3, O5 and B7. On the coordinating session's routing they went
to the seat in the supplement, committed at `9b71bbb`. F5 went with them, as the supplement's §1.6, on that
supplement's values-check. The seat ruled all six at its first sitting of 2026-11-22
(`results/raw/2026-11-22_n-gver-starred-seven_design-to-code_answers.md`). In its short form, G-VER "runs as Code built
it, with two additions and one rule on its ends" (§0). For the driver that is as built, but for the hash check, which
it widened to every non-shard file of the weights folder (§1.2). Draft 4 builds that.

## 1. Dispositions

- **F1 (BUG), a record could stand after a failed write. Applied.** The atomic write is inside `gver_write`'s cleanup.
  On any failure from the write on, the directory's fsync after the replace among them, the file is removed. An
  OSError there ends as SystemExit, so the run prints its FAILED line and exits 1 with no record. A new case kills it:
  the directory's fsync, patched to fail after the replace, is refused with the OSError named and no file left.
- **F2 (RISK), the loaders' own exceptions ended by traceback. Applied.** `_gver_loaded` turns the session set's
  ValueError, and `ids.load`'s missing file, bad JSON, missing key or type error, into a refusal before G-VER. Each ends
  on a REFUSED line naming the loader and the exception's kind, with exit 1. `ids.load`'s own SystemExit passes as it
  is. The self-test's doubles now raise the real kinds: ValueError for the session set; FileNotFoundError and KeyError,
  beside `ids.load`'s own refusal, for the ids. G-TIME-n has the same pattern (there exit 1, not GT6's 2). It is
  declared and not changed, since G-TIME-n's run is of record.
- **F3 (RISK), cuBLAS's setting is held, through R6. Applied, and to the seat.** G-TIME-n's rule-2 check by name
  stands after the pod and before the STAGE line, with exit 1. The docstring now says the setting is held. The block's
  "not held" (`d92500b`, B:141–142) is corrected for the seat in the supplement's §1.1. The seat accepted it (§1.2).
- **F4 (RISK), tokenizers' version not held against L §17. Applied, and to the seat.** `LOCK_TOKENIZERS = "0.22.2"`
  (L:767–768) is held in two places: before G-VER, where another version is a refusal with exit 1, and in
  `check_gver`'s environment block. The supplement's §1.2 gives the added pin to the seat with Q2, and the seat
  accepted it (§1.2). Draft 3 corrects `gver_environment`'s docstring to match.
- **F5 (RISK), exit 2 is not unique to G-VER's STOP. Carried to the launch files, and to the seat.** The launch files
  will name each end by the exit code, the last line of stdout and the record's presence together, and will capture
  stderr. A STOP is exit 2 with the STOP line last and the record on disk, and any other combination is a failure. On
  the supplement's values-check (its item 12 and observation 1), the supplement's §1.6 gives the seat G-VER's ends as
  the launch files will read them. The seat accepted the three-way reading as the launch files' part (§1.4).
- **F6 (RISK), the production seams were never exercised. Applied.**
  - `_gver_verify` runs with `verify.verify` swapped for a spy. It must pass the session set, the loaded ids, the
    decoder and `keys.n4_schedule`'s schedule, with no keyword (M13).
  - `_gver_load_tokenizer` runs behind a stand-in for `transformers` in `sys.modules`, restored after, which loads
    nothing. It must give the folder's path and `local_files_only=True` (M14).
  - `_tokenizers_version` must equal `importlib.metadata`'s version, or "absent" (M15).
  - The seam check now names `pod` and `load_sessions` too (M12).
- **F7 (RISK), the pass rule and the form checks under-tested. Applied.**
  - New tampers, each with its field: `manifest_ok` false; the counts at 159; `n4_ok` alone; no kept label; `labels_ok`
    zero; a problem line on a PASS. Each is refused "at status" (M1–M6).
  - `manifest_ok` not a bool, at "verify" (M8).
  - The package, n's and the characterization's identifiers, the weights and the driver's sha256, each at "pins" (M9).
  - `tokenizers` popped and another version, at "environment"; an extra durations key (M10).
  - A STOP whose counts are zero, the G-VER trial's shape, passes as a record and ends through the flow with exit 2 and
    the record (M7).
- **F8 (NIT). Applied:** the check before the write asserts the record's folder was not even made (M11).
- **F9 (NIT). Applied:** the FAILED line now says "this run wrote no record".
- **F10 (NIT). Applied in the `.gitignore`'s second draft** (`81f5f227…b610`), whose comment no longer presupposes the
  seat's answers to Q1 and Q5.
- **F11 (NIT). Applied in wording.** The durations line and the constants' comment call the two durations a lower bound
  of the pod time, and the decode "verify.verify's whole run". The launch files will print the wall time beside them.
- **M1–M17.** Each is killed, by Code's reading, by the case its row names: M1–M10 by F7's tampers and the zero STOP;
  M11 by F8's assert; M12–M15 by F6's cases; M16 by main() refusing every option, all thirteen (eleven by "gver takes
  no option", and `--bench-dir` and `--gcal-dir` by their own messages); M17 by an assert that the PASS run's ids line
  ends ": equal".
- **B1, agreed.** No self-test case loads a tokenizer or weights or writes the record's path, on the box after the
  commit too: the one case that calls the production tokenizer loader (F6) does so behind a stand-in for
  `transformers` that loads nothing.
- **B2 (a symlink on the volume). Applied.** The symlink case catches an OSError: where the filesystem refuses the
  symlink, that file is missing, and the refusal is the same.
- **B3.** Met by F3's check by name. The launch files will export the setting. The closure is held to the lock's twelve
  files, and a mismatch refuses with exit 1.
- **B4, ruled.** The seat's §1.2 has GV3 hash every non-shard file of the weights folder at its sha256, `config.json`,
  `vocab.json` and `merges.txt` among the eight; the shards stay at byte counts and respawn step (i). Draft 4 builds
  it.
- **B5, B6 and B8. Carried to the launch files:** stderr captured; the copy-back checked against the printed record
  sha256; on exit 1, a check that no record stands before anything is copied; the copy a checkout at the BUILD's
  commit, as G-TIME-n's was.
- **B7. In the supplement's §1.5 for Q6, and declared:** a re-run must move the committed record aside first, and
  after a box change the committed record no longer passes the new driver's check. The seat ruled it (§1.6): the
  committed record goes by `git mv` to `results/raw/<date>_n-gver_<the old box>_gver.json` at the re-run's commit, and
  after a box change G-VER re-runs last before the campaign.
- **O1 and O2, noted:** the readings as built; each starred reading sits in one place.
- **O3. In the supplement's §1.3, for Q4.** The seat ruled it (§1.2): a MANIFEST.json or an ids file that `ids.load`
  refuses never reaches `verify`. That is a refusal, and an ids file off MANIFEST.json's sha256 or count is §1.4's
  INTEGRITY kind.
- **O4, noted:** every real `verify` problem line passes `check_gver`'s form.
- **O5. In the supplement's §1.4, for Q2.** Code has read the file the review did not check. The pinned
  `tokenizer_config.json`, in the tokenizer folder the ids' renders used, names `"tokenizer_class": "GPT2Tokenizer"`.
  The seat ruled the question moot (§0, §1.2): the check hashes all eight non-shard files.
- **O6.** The box's count at draft 1 was 698, and at drafts 2 and 3 727. At draft 4, with one check more, it is 728,
  by arithmetic.
- **O7. Applied:** the module docstring now says the provenance before a load makes a CUDA context.
- **The reviewer's departure,** a glob in one grep's arguments before the folder was listed, is declared in the BUILD
  entry.

## 2. The report as returned

BLIND REVIEW: G-VER of record's BUILD (n §8 step 12)

The draft is S/step4b/gver/draft/n_sessions.py and the .gitignore is S/step4b/gver/commit/gitignore_v1.

Setup checks:
- Both S files are at the brief's sha256s (f5baf379…7b2c, 2e105c34…d8a8).
- scripts/n_sessions.py and .gitignore are tracked and clean at d92500b (rev-parse equals hash-object), and the driver is at 4616f9c3…2553.
- The driver delta has 5 hunks: the docstring (238–279), cmd_selftest (456–461), the new section (5120–5883), main()'s choices (5903) and main()'s gver branch (5924–5935).
- The .gitignore delta is one 8-line block after G-TIME-n's block.
- No local change under valence_core/, scripts/n_* or .gitignore. valence_core/n last changed at ef105f1.
- By my count the self-test adds 53 checks: 52 in _gver_selftest and the environment check in cmd_selftest. That agrees with 634 + 53 = 687.

FINDINGS

F1 BUG (an edge case, unlikely). gver_write, lines 5280–5295.
- `m_resume.atomic_write_json(p, rec)` (5281) sits outside the `try` (5282).
- Its last step, `_fsync_dir(p.parent)` (valence_core/m/resume.py:235), runs after `os.replace`. An OSError there (anything but EINVAL/ENOTSUP), or an interrupt in that window, leaves data/n/gver/gver.json in place.
- The exception then propagates past run_gver, which catches SystemExit only. The result is Python's exit 1 with a record standing. That contradicts the docstring ("a failed record never stands") and GV5 ("1 … with no record"), and a re-run is then refused as "exists".
- Fix: move the call inside the try (`p.parent.mkdir(...)`, then `try: m_resume.atomic_write_json(p, rec); got = p.read_bytes(); …`). p was absent at entry, so unlinking it on any failure is safe.

F2 RISK. _gver_prepare line 5379; the self-test's "sessions" case at 5753 and its check at 5774–5778.
- `sessions.load_sessions()` refuses by ValueError (valence_core/n/sessions.py:109, :112, :128 and _check_session :135–146), not by SystemExit.
- In production, a session set that is not BK's therefore ends by traceback: exit 1 and no record, which is within GV5. But there is no "REFUSED before G-VER" line, no end line, and the trace goes to stderr.
- The self-test's double raises SystemExit, so the check "each exit 1 with its reason on a REFUSED line" claims something production does not do for this cause.
- The block's GV9 line ("the out file is its only trace") holds only if the out file captures stderr.
- ids.load's other failures behave the same way: MANIFEST.json absent, bad JSON, KeyError.
- Fix: convert the ValueError in _gver_prepare (`except ValueError as e: raise SystemExit(f"the session set is not BK's: {e}")`) and make the double raise ValueError. Or declare it and reword the check.
- G-TIME-n has the same pattern already: there it would have been exit 1, not GT6's 2.

F3 RISK. The docstring (262–264), GV4 as sent and the block all say "not held: cuBLAS's setting". The behaviour at 5384–5387 says otherwise: R6 holds it.
- environment_provenance reads CUBLAS_WORKSPACE_CONFIG into the provenance (742).
- backend_identifier keeps it (BACKEND_DROP is only n_encodes_clipped, path and seed).
- CHARACTERIZED_PROVENANCE pins ":4096:8" (628), and L §17 pins it too (L:767–768).
- So a launch that drops the export because "G-VER doesn't need it" refuses at 5385 with exit 1, under an R6 message that never names cuBLAS. numpy's version, the GPU, CUDA and the capability are held the same way.
- Fix: declare in the BUILD entry, and for Q2, that R6 holds these and the launch must export the setting. Optionally add G-TIME-n's explicit rule-2 check (4276–4277) before R6, for a clearer refusal.

F4 RISK. Declared by Code, but I read it as unsound against L §17. Code at 5391–5394; reading GV3.
- L §17 pins "tokenizers 0.22.2" for n's runs on the box (L:767–768), and GV3 names it as the decode's environment.
- The decode, G-VER's only computation, runs in tokenizers' backend, which R6's six libraries leave out. The build records the version and holds nothing.
- verify's decode equality would still catch a behavioural change. But a run under another tokenizers version is not under LOCK-n v0.1 as §17 writes it.
- Fix: add a `LOCK_TOKENIZERS = "0.22.2"` refusal before G-VER (exit 1) and/or hold it in check_gver's environment block. Or put the departure to the seat with Q2.

F5 RISK. main() 5920–5934; affects GV5 and GV15.
- Exit 2 is not unique to G-VER's STOP:
  - argparse's ap.error exits 2 with no record, for every gver option and for --bench-dir or --gcal-dir;
  - Python exits 2 when the script cannot be opened.
- Uncaught exceptions (F2, the tokenizer's load, verify) end with exit 1 and a traceback, with no "G-VER (n): …" line.
- Fix, in the launch files: name each end by the exit code, the last stdout line and the record's presence together. Exit 2 is a STOP only when the last line is "G-VER (n) STOP: the record is written; …" and the record exists. Treat any other combination as a failure, and capture stderr.

F6 RISK. Production seams are never exercised (5320–5345).
- The self-test never calls `_gver_verify`, `_gver_load_tokenizer` or `_tokenizers_version`; it only checks their identity.
- The seam check (5835–5843) omits production_gver_env's `pod` and `load_sessions`.
- `_gver_verify` is the one place this build forms verify's call (N4's schedule and verify's defaults), so a mistake there shows first on the box (M12–M15).

F7 RISK. The pass rule (`_gver_pass_holds`, 5175–5183) and the form checks (5209–5250) are under-tested.
- Only `m["equal"]` is tested on its own. The only STOP records (rep_stop, rep_pin) also fail on first_problems or on the manifest, so each other conjunct survives deletion (M1–M6).
- No record has a zero count, so `x >= 0` can become `x > 0` (M7). A real STOP with ids_ok = 0 (the G-VER trial's shape) would then fail the record check and end with exit 1 and no record, instead of exit 2 with the record.
- Several form clauses have no tamper at all (M8–M10).

F8 NIT. gver_write 5278 and the check at 5634–5639.
- The check before the write is not isolated: r_w4 passes with it deleted, because the check after the write gives the same message and unlinks the file (M11).
- Fix: assert `not wp4.parent.exists()`, since the mkdir comes after the first check.

F9 NIT. run_gver 5446. "nothing is left at {path}" is also printed for gver_write's own exists refusal (5276–5277), where a file that is present is correctly left in place. Practically unreachable; rewording it as "this run wrote no record" would be accurate.

F10 NIT. gitignore_v1's comment ("its entry, "G-VER (n)", is the gate LOCK-n v1.0 and the campaign follow") presupposes the answers to Q1 and Q5, which are the seat's. Suggest: "the record of n §8 step 12 (GV1, GV9), written at PASS and at STOP".

F11 NIT. The durations at 5429–5435 (GV12).
- "decode" times verify as a whole: the decode plus all of verify's checks and N4's schedule.
- Both durations leave out the pod time before G-VER: importing torch, the CUDA context, the folder listing, hashing the tokenizer files, the closure.
- GV12's entry line should call them a lower bound, or put the launch's wall time beside them.

SURVIVING MUTANTS (each passes every self-test check by my reading; each kill is a check to add)

- M1, line 5181: drop `v["manifest_ok"] is True and`. Kill: tamper rec_p with verify.manifest_ok=False; expect "malformed at status".
- M2, line 5181: drop `n == schema.N_SESSIONS and`. Kill: rec_p with sessions, ids_ok, spans_ok and n4_ok all 159; expect "status".
- M3, line 5182: drop the `ids_ok == spans_ok == n4_ok == n` conjunct. Kill: rec_p with n4_ok=159 alone; expect "status".
- M4, line 5182: `labels_kept > 0` becomes `>= 0`. Kill: labels_kept=labels_ok=0 on rec_p; expect "status".
- M5, line 5183: drop `labels_ok == labels_kept`. Kill: labels_ok=0 on rec_p.
- M6, line 5183: drop `first_problems == []`. Kill: first_problems=["x"] on rec_p.
- M7, line 5210: `x >= 0` becomes `x > 0`. Kill: a zero-count STOP report through rec_of, plus one flow case expecting exit 2 with the record.
- M8, line 5218: drop the `isinstance(v["manifest_ok"], bool)` clause. Kill: manifest_ok="yes" on rec_s; expect "verify".
- M9, lines 5238–5241: drop any one of the package_sha256, backend_identifier, characterization_identifier or weights_sha256 comparisons, or the driver hex64 check. Kill: one tamper each (only pod_id, lock_sha256 and imported_sha256 are tampered now).
- M10, lines 5244 and 5248: drop the key-set clause of environment or of durations_ms. Kill: pop environment["tokenizers"]; add a durations key.
- M11, line 5278: delete gver_write's check before the write. Kill: F8's assert.
- M12, line 5344: `pod=m_resume.pod_id` becomes `pod=lambda: CHARACTERIZED_POD`. This defeats the pod pin on a same-class box. Kill: add `penv.pod is m_resume.pod_id and penv.load_sessions is sessions.load_sessions` to the seam check.
- M13, line 5327: change `[s.present_first_is_S …]` to `[not s.present_first_is_S …]`. On the box that gives a false STOP of record on N4. Kill: call `_gver_verify` with `verify.verify` patched to record its arguments, and compare against `keys.n4_schedule(...)` with no keyword overrides.
- M14, line 5322: drop `local_files_only=True`. Kill: a box check that patches `AutoTokenizer.from_pretrained` to record its kwargs, or a source check.
- M15, line 5333: `version("tokenizers")` becomes `version("transformers")`. Kill: compare `_tokenizers_version()` with `importlib.metadata.version("tokenizers")`, or "absent" when it is not installed.
- M16, line 5930: drop `("--ids-dir", …)` (likewise --tokenizer-dir, --root, --report, --ruling, --convention or --pi-date). The option is then silently ignored. Kill: try every option; only five are tried now.
- M17, line 5383: print the "not equal …" text unconditionally. Kill: assert that env1's ids line ends with ": equal".

BOX RISKS

- B1: Can the box self-test, run after the commit with RUNPOD_POD_ID set, reach a production path that loads a tokenizer or writes data/n/gver/gver.json? By my reading, no:
  - every flow case runs on doubles, with out under the temporary directory, and genv refuses an out inside the repository (5682);
  - main()'s cases pop RUNPOD_POD_ID, trap the four loaders and swap run_gver for a recorder;
  - the argv cases end in argparse;
  - no other self-test calls main with gver.
  If the recorder ever failed, _gver_prepare reads only the record's existence before refusing at the pod check.
- B2: The tw3 symlink (5538) is the driver's first `symlink_to`.
  - The box self-test's temporary directory is under the work folder on /workspace (gtout:73), a volume that has refused `cp -p` (EPERM) before.
  - If it refuses symlinks too, _gver_selftest raises, the count falls short and the launch stops. That is safe, but it blocks the run.
  - Either skip-and-count on OSError, or put the self-test's TMPDIR on local disk.
- B3: R6 in this process needs a visible GPU and CUBLAS_WORKSPACE_CONFIG=:4096:8 (F3). environment_provenance imports torch and creates a CUDA context.
  - The closure measured in this process should equal LOCK_CLOSURE: the G-VER path imports nothing outside n beyond the twelve files the box's `hashes` printed at G-TIME-n's launch (gtout:80–92).
  - A mismatch refuses with exit 1; it can never produce a wrong PASS.
- B4: The tokenizer load is the same call `_gver_tokenizer` made on this pod, which PASSed (gtout:121–122, :185–186). vocab.json, merges.txt and config.json are covered by byte counts only (and by respawn (i)'s full re-hash).
- B5: The exits (F5). The launch must capture stderr; a traceback has no end line.
- B6: Copy-back.
  - Use the printed "record … sha256" to check the copy.
  - On exit 1, check that no record stands before copying anything (F1's window).
- B7: Re-runs after the record is committed.
  - Any later box copy at a newer commit contains data/n/gver/gver.json, so G-VER refuses with "exists". GV13's re-run, or any re-run the seat rules, needs the record moved aside, as G-VEC's does.
  - After a box change the driver's CHARACTERIZED_* constants change, so the committed record no longer passes check_gver under the new driver.
- B8: weights_of_record, driver_bytes and committed_bytes shell out to git. The copy must be a checkout at the BUILD's commit holding LOCK-n.md, the model manifest and the driver.

OBSERVATIONS

O1: Each reading against the code.
- GV1: does it (GVER_STAGE "G-VER (n)", the command, the record).
- GV2: does it (driver and .gitignore only; no schema stage; package and closure held at 5395–5399).
- GV3: does it (pod pin; the committed instruct path; the three files hashed before the load, symlinks refused; local_files_only; _decoder's form, checked through the stub's kwargs). Departures: three files only (declared; Q2) and tokenizers not held (F4).
- GV4: does it. Code's correction is sound against L:543, declared, and tested by env3. One undeclared inaccuracy: cuBLAS is held through R6 (F3).
- GV5: does it (the status is verify's; check_gver re-derives PASS from the report). The edges are F1, F2 and F5.
- GV6: does it (exit 2 with the record; the end line quotes L:543).
- GV7: unchanged.
- GV8: does it (M16 aside).
- GV9: does it (F1 aside).
- GV10: does it.
- GV11 and GV14: nothing in the driver.
- GV12: does it (F11).
- GV13: does it as far as the pod pin goes (B7).
- GV15: not in this change.
- GV16: does it, model-free (gaps F6–F8).

O2: Each starred reading sits in one place, and the build does what the block says:
- GV4: one function, _gver_prepare;
- GV9: one writer and one checker (gver_write, check_gver), plus gver_record and the .gitignore block;
- GV6: exit 2 with the record;
- GV13: the pod pin, exit 1;
- GV1: the command;
- GV11 and GV14: nothing.

O3: GV4's correction only reaches verify when MANIFEST.json is still consistent with the ids files. ids.load checks each file's sha256 and count against it, so an inconsistent folder is ids.load's refusal (exit 1). This is worth stating with Q4.

O4: Every real verify problem passes check_gver's form. The unmasked lines (spans, manifest, labels) contain no "]", masking leaves only "[..]" groups, and all are under 200 characters (verify.py:77–138). So no real STOP is refused on that account under the current count rule.

O5: For Q2: the 22-file folder holds vocab.json, merges.txt and config.json beside the three hashed files. As I recall transformers' AutoTokenizer, it reads config.json only when tokenizer_config.json names no tokenizer_class; I did not check that file. The folder has no chat-template or added-tokens file. The laptop render used a folder of the three files alone; the stages' G-VER decoded from the full folder and PASSed.

O6: Expected box self-test count by arithmetic: 645 (gtout:76) + 53 = 698, unless B2 bites.

O7: "Nothing runs on the GPU" is true of kernels, but the process holds a CUDA context (from `get_device_name(0)`).

DEPARTURES
- One grep took the glob `valence_core/n/*.py` before I had listed that folder. I listed it straight afterwards (name-only ls): no file name there holds a guard marker, so none reached an argv, and it was not a loop.
- Otherwise none:
  - no interpreter except shasum; no write; no network;
  - no marker in any argv or command text (the adapter module and the model manifest were read with the file-reading tool only);
  - nothing under data/*/ckpt, data/*/reports or data/m[f]3 read, listed or sized; no whole-tree git status;
  - tree-wide git commands took item 3's pathspec with Q-F3's exclusion;
  - in S only the two named files were read.
- Beyond the brief's list, I read two committed raws, results/raw/2026-11-21_n-gtime-v1_out.txt (lines 60–129, plus greps) and the G-TIME-n launch review. They are not barred.

