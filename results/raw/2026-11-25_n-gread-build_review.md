# n — G-READ-n's BUILD: the blind review of draft 1, as returned, with every disposition

PI date 2026-11-25. Code (the n-build session). LOCK-n.md is cited by file line, `LOCK-n.md:N` (the file is the same
at `05ac941` as at `098218c`). In the report in §2, as returned, `TO:N` is a line of draft 1.

**What was reviewed.** One blind pass by a subagent over the change as draft 1 had it, at HEAD `05ac941`:
- `scripts/n_sessions.py`, HEAD's (`47abe489…c21a`) to draft 1 (`5a1d84a3…24e8`, 8,834 lines);
- `.gitignore`, HEAD's (`fe865233…03ed`) to the draft (`3aac58be…6482`): three lines added after G-ANL-n.json's
  admit line.

Draft 1 had passed its self-test, 833/833, in a battery window, and `hashes` on its overlay had printed the lock's
package digest and a closure equal to the lock's.

**The reviewer's brief** was a file the reviewer read itself, as its prompt directed: Code's scratch file
`S/step4b/gread/review_brief.md` (`458aa49b…5cfd`, 132 lines). It:
- named the change and its specification: Code's readings GR1–GR14 as sent, the seat block and the spec raw as
  committed at `05ac941`, the texts, and the code the change must match or use;
- named twelve things Code knew of, to be declared;
- asked for findings, surviving mutants, run risks, observations and departures;
- barred any interpreter but `shasum`, any write, any network, any guard marker in an argv (a grep pattern and the
  command's own text included), and Q-F3's folder by its plain name in any argv;
- barred anything under `data/m[f]3`, any whole-tree git status, any read, listing, size or time of a ckpt or reports
  file, anything outside the repository but the named scratch files (the staging folder above all), and any naming
  of G-TIME-n's holding folder in an argument;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec with `':!data/m[f]3/**'` on every
  git command over the tree.

**The report** is in §2, extracted verbatim by `jq` from the subagent's hand-back (234 lines, sha256
`690b5daf00f3a0d2de950c5410b4d4af60911ea20f79bbd8b6470eda35cd1d32`). It names scratch files only by their paths inside
the scratch folder. One abbreviation in its first lines is a slip: the brief's sha256, `458aa49b…fcfd` there, is
`458aa49b…5cfd` by tool (the prompt gave it in full).

**In sum:**
- no BUG;
- 12 findings: F1–F6 RISK, F7–F12 NIT;
- 10 surviving mutants, M1–M10;
- 8 run risks, R1–R8;
- 9 observations, O1–O9;
- its departures, declared: one `awk`, which the brief barred by name, in a pipeline over a definitions `grep`; two
  `sed -n` line-range filters of the prescribed diff; and, within the rules as it read them, `git check-attr -a` on
  four named paths (two under `data/`), commands on the committed close list, its file tool's read of the HF adapter
  module and `wc -l` of named files (the BUILD entry lists them whole).

**The draft after it.** Draft 2 (`176aef3d…a826`, 9,021 lines) builds in F1–F6 and F12, F7 in part (four refusal
cases, its sentence narrowed), R5 and O6, the wording of F8–F10, and a kill for every mutant, by Code's reading of
each case and not by a mutation run: 20 run-time checks more (6 new `chk` calls, 6 refusal cases and 8 refused
options in main()'s loop), several checks extended, and the stand-in's band three layers. It passed its self-test,
853/853, in its own battery window. Draft 3 (`35c4c73e…4808`, 9,025 lines), the BUILD's bytes, adds the BUILD
values-check's three points on the driver: two docstrings and a refusal case (under F3, F4 and F11 below). It passed
its self-test, 854/854, in its own battery window.

## 1. Dispositions

- **F1 (RISK), a leftover temporary file found only after every fit. Applied.** `_gread_prepare` refuses
  `G-READ-n.json.tmp`, beside the artifact's own check and before any fit. A new check plants one and finds the run
  refused and the file left as it was.
- **F2 (RISK), the failure paths after the rename. Applied.** `gread_write`'s folder fsync is inside its guarded
  block, so a failure after the rename removes the artifact; the read-back's guard spans the artifact's sha256 and the
  end line. New checks: a failure inside the fits (exit 1, "G-READ-n FAILED: ValueError", no artifact, no temporary
  file) and a read-back that fails check_gread (exit 1, the artifact removed). They kill M2 and M3.
- **F3 (RISK), `--staging` read against the working folder. Applied.** A relative `--staging` is read from the
  repository's root, wherever the command runs (the run step's `cd` into the venv's folder among them); the usage text
  and main()'s message say so. A new case passes `data` and finds it refused as inside the repository, which a reading
  against the working folder would not give in the self-test's overlay, where the working folder lies outside it.
  Draft 3 adds a case that holds from any working folder but the root (the values-check's observation 3): a relative
  path naming a tampered stand-in copy from the root, refused at its byte check.
- **F4 (RISK), a failure's message could carry a local path. Applied.** A failure prints its cause in the analyzer's
  form (`_gread_err`, after anl:4611–4619): a schema error by its field path, a file-system error by its type and
  strerror ("no strerror" where it has none, and the analyzer its message: draft 3's docstring says so), any other
  error by its type alone. Python's warnings are recorded, not shown, and printed after the end line by category and
  message, never by their file. An interrupt's traceback can still print paths to stderr (R7).
- **F5 (RISK, low), the second read not held to the report. Applied.** Every second read of a cell, arrays kept,
  goes through `probe_cell`, which holds its capture_sha256, record count and identity to the report's again.
- **F6 (RISK), the comparator's numbers never checked. Applied.** The stand-in's band is three layers, so a median is
  not a mean. A new check computes each direction's band median from the recorder's AUCs on the expected inputs, and
  holds each point's 24, in RANDOM_IDS' order, and their max, to every result matched to the point. It kills M1 and
  M9.
- **F7 (NIT), refusals with no case. Applied in part, and the sentence narrowed.** New cases: a listed JSON's sha256
  against the report's json_sha256; a cell under another identity; the shuffle seed; a staged symlink; the staging
  folder at the repository's root (M7); a relative staging folder (F3). New unit checks: the writer's refusals and
  cleanup (M6), and the binding conditions on six tampered copies of the artifact (M8). The self-test's docstring now
  says it cases the refusals a tampered input can reach, and names the backstopped ones it does not: those
  check_report or the pinned list already make, and N1-R sessions with no shadow row.
- **F8 (NIT), the sentinels' reach. Applied in wording.** The self-test's docstring names the sentinels: the margin,
  its two log-probability sums and their fresh copies. The restricted read keeps example_record's values; the command
  reads none of these fields.
- **F9 (NIT). Applied:** the real layer_auc runs twice on one 80-row contrast, as the self-test's docstring and the
  BUILD entry now say.
- **F10 (NIT). Applied:** the usage text's GR9 line reads "cells two at a time as sent, one at a time as built (a
  declared departure)".
- **F11 (NIT), the staging folder checked before the driver, the lock and the package. Declared** in the BUILD
  entry and, in draft 3, in `_gread_prepare`'s docstring; the order is kept: each check comes before any fit, and an
  earlier refusal costs nothing.
- **F12 (NIT), the guard's label and form. Applied:** genv's output passes `guard.refuse_test_out`, raising, and the
  check's label names what it checks.
- **M1–M10.** Each is killed by a check in draft 2, by Code's reading: M1 and M9 by F6's ordered check; M2 by the
  failure case; M3 by the read-back case; M4 by a check that every row `gread_rows` returns owns its data; M5 by eight
  more refused options in main()'s loop, whose refused argvs are fifteen in all; M6 by the writer's unit checks; M7
  by the staging folder at the root; M8 by the binding conditions on tampered copies; M10 by a check that the
  environment line names all five thread variables.
- **R1 and R2.** Met by F3 and F1.
- **R3–R6.** Noted. Under R5, the −1 cell's rows are now released after their result. The run's out raw will show the
  I/O and the times.
- **R7.** A crash or a stop leaves no artifact; a kill inside the write's window leaves the temporary file, which the
  next run refuses (F1). An interrupt's traceback goes to stderr; the run's err raw is read and screened before it is
  committed.
- **R8.** Met by F12.
- **O1, O2, O4, O5, O8 and O9.** Noted. O2's two undeclared departures are F10's and F11's, now declared.
- **O3.** Each starred reading sits in one place: GR3 in `gread_load` (with `gread_rows`), GR5 in
  `gread_comparator_cells`. The block's "another answer" for each is that small change.
- **O6.** The environment line now names numpy's BLAS (`np.show_config(mode="dicts")`; "not reported" where numpy
  cannot say). A second repeat check at 320 rows is beyond GR10: the seat's call, not built.
- **O7.** LOCK-n.md:964–965's "or their merged points" is not built: the lock's dose map keeps every point
  (LOCK-n.md:763–765), and `gread_points` refuses a map that does not. Declared.
- **The reviewer's departures** are declared in the BUILD entry.

## 2. The report as returned

BLIND REVIEW: G-READ-n's stage command (n §8 step 15), the BUILD drafts at HEAD 05ac941

Short form: TO = S/step4b/gread/draft/n_sessions.py. Every TO:N is a line of that file.

Inputs checked first:
- The brief: 458aa49b…fcfd, 132 lines.
- TO: 5a1d84a3…24e8, 8,834 lines.
- S/step4b/gread/build/gitignore_v1: 3aac58be…6482.
- S/step4b/gread/spec/gr_readings_v1.md: 17d66da9…9b43, 195 lines.
- HEAD is 05ac941. scripts/n_sessions.py is clean at HEAD (rev-parse equals hash-object, 0a7cdab3…) and its sha256 is 47abe489…c21a.

The deltas came from `git diff --no-index -U3`:
- The driver: six hunks (the docstring, cmd_selftest's call, the new section TO:7728–8645, and three hunks in main()).
- The .gitignore: the three lines after G-ANL-n.json's admit. They are correct: `/data/n/gates/*` comes before `!/data/n/gates/G-READ-n.json`, so the .tmp stays ignored. No git attribute is set on the inputs' paths or the artifact's.

Headline: I found no BUG-class defect. On the success path these all match the PINs and the lock:
- the contrasts;
- the comparator (GR5's pinned reading) and the matching;
- the seeds and the six results;
- the artifact's JSON form (equal to anl:4606);
- the binding conditions.

What I found is RISK and NIT: failure paths with no test, the comparator's numbers never checked, and the launch's working folder.

FINDINGS

F1. RISK. TO:7958–7960 with TO:7888–7890.
- What is wrong: a leftover data/n/gates/G-READ-n.json.tmp is checked only inside gread_write, after every fit. It can come from a kill during the write, or from M6. The next run would then refuse about 2.65 h in.
- Fix: in _gread_prepare, beside the artifact's own check, refuse when `out.with_name(out.name + ".tmp")` exists or is a symlink. Add one self-test case.

F2. RISK. TO:7908, TO:8142–8156, TO:8169–8171.
- No case tests "exit 1 with no artifact" on any failure path. No case reaches "G-READ-n FAILED", and none fails the read-back (M2, M3).
- Two steps after the rename sit outside any cleanup. One is m's _fsync_dir at TO:7908, outside gread_write's try; it re-raises any error but EINVAL/ENOTSUP (resume.py:197–198). The other is the sha and COMPLETE prints at TO:8152–8155. If either fails, the run exits 1 with the artifact on disk.
- Fix: put _fsync_dir inside the guarded block, unlinking out if it fails after the rename, and extend the read-back's try over the two prints. Add a FAILED case and a read-back-failure case.

F3. RISK. TO:7961 and TO:7968.
- `--staging` is resolved against the process's working directory. GR14's run step first cds into the venv's bin folder by a glob.
- So the repository-relative form every text uses (../jspace-lab-box.noindex/n/campaign-v1/) would name another folder there. The run would refuse with "not a folder". An absolute path instead puts the local root into the launch command's raw.
- The STAGE line prints the folder relative to the repository, which then differs from what was typed.
- Fix: resolve a relative --staging against REPO (`(REPO / staging).resolve()` unless it is absolute), and state this in the docstring and the argparse message. Otherwise, declare the launch's form.

F4. RISK. TO:8170, with TO:8040–8045 and TO:7893–7900.
- The FAILED line prints the exception's message whole. An OSError raised outside the package's reader carries an absolute staging or repository path into the out raw: from the re-hash's stat or `open(f, "rb")`, from gread_write's open or rename, or from _fsync_dir.
- Python warnings (for example a numpy RuntimeWarning from fit_lr's exp) and tracebacks also print absolute module paths to stderr.
- So departure 7 ("no local root reaches the run's out raw") holds only on the success and refusal paths.
- Fix: print a FAILED cause as anl's _err_where does (anl:4611–4619: the type and strerror, no path), or catch OSError in the re-hash and refuse naming p.

F5. RISK, low. TO:7826–7835; the loads at TO:8082, TO:8092–8093 and TO:8123–8124.
- The second read of each probed cell (arrays kept) is not bound to the report again. load_cell re-reads the JSON and checks the rows against that JSON's own capture_sha256.
- Only the first pass compared capture_sha256, the record count and the identity with the report (TO:8055–8058). A staged file changed between the passes would be probed while the artifact names the report's digests.
- Fix: give gread_load the report's entry, and check capture_sha256 and the record count on every load.

F6. RISK. Production TO:8115–8116; self-test TO:8404–8412 and TO:8426–8433.
- No check reads the comparator's numbers. The self-test checks the fits' inputs, and that the four points' comparators are distinct and shared as matched.
- It never checks that each band median is the median of that direction's recorded AUCs, in RANDOM_IDS order (M1, M9). At a band of two layers the median also equals the mean.
- Fix: compute the 24 expected band medians per point from fake_auc's deterministic AUCs on want_c, and compare them in order with each result's comparator.band_medians. Use a stand-in band of three layers.

F7. NIT. TO:8187–8189, and GR13's "every refusal … one tampered input each".
These refusals have no case:
- the listed JSON's sha256 against json_sha256 (TO:8027–8031);
- a cell's identity (TO:8055–8056) and its record count (TO:8057);
- the cells' set against the plan (TO:8018, first half);
- the shuffle seed (TO:8021, second half);
- the checks redundant with check_report (TO:8005, TO:8007, TO:8011–8015);
- the symlink refusal (TO:8040);
- N1-R sessions with no shadow row (TO:8100–8102);
- the binding conditions (TO:8136–8138) and the read-back (TO:8145–8146);
- gread_write's two refusals;
- a staging folder inside the repository but outside data/ (M7).

Most are backstopped (by check_report, the pinned list or the package digest), so today their removal changes no reachable outcome; the sentence overclaims. Fix: add the reachable cases (the odd JSON sha256, the identity, the binding, the read-back, gread_write), or narrow the sentence.

F8. NIT. TO:8181, TO:8272, TO:8278 and TO:8450–8453; also the block's GR3 "values it can recognize in every margin field".
- The sentinels are the log-probability sums, the margin, and the fidelity block's fresh copies of them.
- The per-token log-probabilities and the restricted read keep example_record's defaults and are never checked. The restricted read's values are p_S 0.75, p_U 0.25, label_mass 0.5 and its pick.
- The command reads none of these fields, so this is a wording claim, not a leak.
- Fix: name the fields that carry sentinels, or plant distinctive values there as well (consistent with check_record) and check them.

F9. NIT. TO:8188 and item 6's fourth departure. "The real layer_auc runs once" is not right: it runs twice on the one 80-row contrast (a1 and a2, TO:8586–8587).

F10. NIT. TO:396–397. Under "the PINs, in short (as sent …)", the GR9 line gives the built form, "one cell's maps open at a time". GR9 as sent says two at a time. Fix: "two as sent; one as built, a declared departure".

F11. NIT. TO:7961–7966 against TO:7970–7983 (docstring TO:357–359). The staging folder's location and folder checks run before the driver, LOCK-n.md and the package. GR8 puts "the staging folder (GR2)" last. This is harmless (both are before any fit) and the docstring states it, but it is not in item 6's list. Declare it.

F12. NIT. TO:8371–8372. The guard's label says "every path the flow cases read or write". The flows also read LOCK-n.md and the committed close list in the repository, and one case passes REPO/data as its staging folder. The check covers four write and staging paths. Fix the label (see R8 for the guard's form).

SURVIVING MUTANTS (each passes every self-test check by my reading)

M1. TO:8115: `bands.append(probe.band_median(per))` becomes `bands.append(per[-1]["auc"])` (or the max).
- Effect: the comparator's bar changes, and every status stays PASS under the recorder.
- Kill: F6's check.

M2. TO:8171: `return 1` becomes `return 0`.
- Effect: no case reaches the FAILED branch.
- Kill: a flow whose recorder raises ValueError (or whose stand-in −1 cell holds other sessions), asserting rc 1, a last line starting "G-READ-n FAILED: ", and no artifact and no .tmp.

M3. TO:8148: `os.unlink(out)` becomes `pass`.
- Effect: no case fails the read-back.
- Kill: patch cells.json_bytes or schema.check_gread for one read-back so it returns something else or raises; assert rc 1 and no artifact.

M4. TO:7847: `np.array(caps.arrays[int(l)][row], dtype=np.float32)` becomes `caps.arrays[int(l)][row]`.
- Effect: the rows become views of the read-only maps, which then stay open (the shadow's 31 for the whole run). This breaks GR9's "rows copied" and departure 1; the values are unchanged.
- Kill: assert that every row gread_rows returns owns its data (`v.base is None`, not a memmap).

M5. TO:8694: `("--root", a.root is not None)` becomes `("--root", False)`. The same holds for --report, --ruling, --convention, --model-dir, --tokenizer-dir, --ids-dir and --pi-date.
- Effect: the option is silently ignored. main()'s cases try only --out, --smoke and --resume.
- Kill: one argv case per option the gread branch refuses.

M6. TO:7904: `os.unlink(tmp)` becomes `pass`.
- Effect: a failed write leaves the .tmp behind, which leads to F1.
- Kill: call gread_write with a text that cannot be encoded ("\ud800") and assert neither file is left; then call it with a .tmp already present and assert the refusal.

M7. TO:7962: `_within(st, REPO.resolve())` becomes `_within(st, REPO.resolve() / "data")`.
- Effect: a staging folder elsewhere in the repository is accepted; the only in-repository case is REPO/data.
- Kill: a case with the staging folder at REPO itself (it is refused before any read).

M8. TO:7866: `if ca["cells"] != want:` becomes `if False:` (or any one condition of gread_binding_problems is dropped).
- Effect: the copy is exercised only on a good artifact. This matters only if probe.artifact also erred.
- Kill: put tampered copies of the COMPLETE artifact through gread_binding_problems (cells, package, layers, merged, the plan sha256 and the identity sha256), as anl's gread-* cases do (anl:5711–5721).

M9. TO:8116: `comparator[p] = bands` becomes `comparator[p] = sorted(bands)`.
- Effect: the per-direction order is lost; the max is unchanged.
- Kill: F6's ordered check.

M10. TO:7750–7751: one name dropped from GREAD_THREAD_VARS.
- Effect: the stdout check reads only the line's prefix.
- Kill: check that the environment line names all five variables.

RUN RISKS

R1. The working folder: --staging and the run step's cd (F3).

R2. A stale .tmp is found only at the end of a run (F1).

R3. The real close list and report. The list is pinned (42682630…fe6d, clean at HEAD). I checked its order against camp_copy_names by name alone:
- 138 blocks of 32 lines (cell JSONs at lines 2, 34, 66, … 4386);
- the cell names in C order, which equals Python's sorted() on these ASCII names;
- each block's arrays at L33 through L63, in order.

The report is read as its working bytes and through `git show HEAD:`. Its path carries no attribute, so the two are equal while it is clean.

R4. The I/O. The arrays are read three times, about 13.6 GB in all:
- the re-hash: about 4.9 GB;
- the first pass over all 138 cells: about 4.9 GB;
- the second pass: the shadow, all 120 N1-R cells and seven 160-row cells, about 3.9 GB.

Each load_cell hashes every row twice (about 238,000 rows in the first pass and 188,000 in the second). That is minutes beside the fits, and the page cache helps.

R5. Memory and files.
- The shadow's rows held for the run: 160 × 31 × 5,120 float32, about 101.6 MB.
- A primary result's 31 contrasts in float64: about 406 MB.
- Its + pole's rows (101.6 MB), and at valence +1 the −1 cell's rows (101.6 MB, held into the next result), plus about 12 MB of copies per fit.
- Peak about 0.75 GB.
- At most one cell's 31 maps open at a time (but see M4).

R6. Time. At gread-bench's medians the fits take about 2.65 h: about 25.8 min per primary result and about 66 s per comparator point. No line is printed between those (by design; the end-wait is on the PID). The fits use numpy's default BLAS threads under nice -n 19 beside Q-F3, so contention lengthens the run.

R7. The write, a crash, a stop.
- A crash or stop leaves no artifact, except a .tmp from a kill inside the millisecond write window (F1).
- A KeyboardInterrupt prints a traceback with absolute paths (F4).
- The repeat check is one 80-row call (see O6).

R8. The self-test's safety. No case, and no call of main() in the self-test, can reach the real staging folder or write under data/n/:
- Every flow environment comes from genv, with its output under the self-test's tmp.
- The staging folders are tmp copies, tmp/no-such-folder, or REPO/data, which is refused at _within before anything is read.
- production_gread_env() is only constructed, never run.
- main()'s cases end in argparse errors or call a stand-in cmd_gread. If the stand-in failed to install, the real command would refuse at "not a folder" (staging-arg is never created) before its driver check.

It is fragile, though. The guard at TO:8371 is a chk that records a failure and carries on. genv's output does not pass through refuse_test_out, and the writer's own guard (refuse_out) admits data/n/. A future case built with GreadEnv's default output (GREAD_OUT) would write to the artifact of record's path. Route genv's out through guard.refuse_test_out, raising.

OBSERVATIONS

O1. Each reading against the code:
- GR1: done. The command is in the driver; --staging is its only option; the other options are refused, with only three tried (M5); no --out, smoke or resume; refused on a pod in gread-bench's form.
- GR2: done.
  - The lock is checked through gver_lock_check. The list is checked at its pin and HEAD's bytes, and the report at HEAD's bytes and the list's first line.
  - The report must be COMPLETE with every arm complete. Its identity's lock, package (also equal to this process's), band, plan and own sha256 are checked, and its 138 cells must be the plan's.
  - The 4,417 files are re-hashed by name. Every cell goes through load_cell with identity=None. The JSON's sha256 is held to json_sha256 through the list, and capture_sha256, the identity and the record count to the report's. A staging folder in the repository is refused.
  - Notes: reading every cell twice is declared and sound; the check order is F11; the second read is F5.
- GR3★: as the head has it. load_cell parses and checks every record whole; gread_rows keeps session_id and capture.row; no margin is printed or written. The sentinel claim is narrower than stated (F8).
- GR4: done, in GREAD_AXES order. The contrasts are as pinned, `merged` comes from the dose map, and probe.result runs at 200 shuffles with the one cv_seed.
- GR5★: done, in gread_comparator_cells.
- GR6: done. Each point is computed once and shared through GREAD_MATCH; the floor sessions' shadow rows are taken by session id. The values are not tested (F6).
- GR7: done. The two new pins are held to probe's constants; one cv_seed goes to the comparator, probe.result and probe.artifact; NOT-COMPUTED is never produced.
- GR8: done, with the head's correction; the exits are 0 and 1; see F2 and F11.
- GR9: done. One cell's maps at a time is declared and sound; see F1 and F10.
- GR10: done. No variable is set, the five are printed, and the first comparator call is computed twice and refused before the primary fits if it differs.
- GR11: done; see F4.
- GR12: done. The path and form are as GR12 says, it is refused if present, the .gitignore line is right, and the artifact is read back.
- GR13: mostly. The direct file forms are declared and sound; see F7, F8, F9 and M1–M10.
- GR14: nothing in the code; F3 bears on it.

O2. Item 6's list. Every entry is sound and declared, with these notes:
- Entry 3: np.save writes the same .npy form as open_memmap; atomic_write_json is append_record's own JSON writer; check_cell runs before each write and load_cell reads the cells back.
- Entry 5: it is equivalent to anl at VERDICTS. anl binds the report to the repository's cells (report_problems) and the artifact to those cells; the driver binds the artifact to the report. It is exercised only on a good artifact (M8).
- Entry 6: anl's write_once places the file with os.link; check-then-rename leaves only a single-writer race. No _assert_native, but probe converts every number to a native type.
- Entry 7: holds only off the failure path (F4).
- Entry 8: checked (R3).
- Entry 9: its branches are untested (M2, M3, F2).
Two departures are undeclared: F10 and F11.

O3. Each starred reading sits in one place.
- GR3★ is gread_load (TO:7826–7835), with gread_rows (TO:7838–7850) as what is kept. The other answer replaces gread_load's body with a reader that returns the same (cell, caps) shape. _gread_prepare uses the identity, capture_sha256 and the record count from it; gread_rows uses session_id, capture.row and the arrays. That is a contained change plus that reader's own cases, as the block says.
- GR5★ is gread_comparator_cells (TO:7815–7823). The shadow answer deletes TO:7821–7822, since _gread_run already takes the shadow path for any point whose other cell is the shadow. Two self-test expectations change (TO:8261 and TO:8422); the count and the time do not. N1-R's −1 cells would then be checked and never probed, as the head says.
- The block's "two cells open at a time" is built as one (declared).

O4. The head's points.
- GR8 is built as the head has it: refuse_out, then the command's own existence test at TO:7958–7960, and again at the write.
- GR7's probe:41 claim and GR3's "computed on" sentence appear nowhere in the code. The first pass's line names check_cell.
- The survey's open questions 1–13 each have an answer in the code.

O5. The chain is closed at VERDICTS, not here: staging JSON, then the close list, then the report's json_sha256, then the repository's JSON. G-READ-n never reads the repository's cell JSONs.

O6. Determinism (rule 2, rule 27). The environment line prints python, numpy, the CPU count and the five thread variables, but not numpy's BLAS backend. The one 80-row repeat cannot see nondeterminism at 320 rows or under load. Printing the BLAS name is cheap; a second repeat at 320 rows is beyond GR10 and so the seat's call.

O7. LOCK:964–965's "or their merged points" is not built: gread_points refuses a map that drops a comparator point. That cannot happen under the lock's map (all seven points kept, LOCK:763–765).

O8. Measuring the closure imports every production module, the HF adapter module among them. That module imports torch only inside its constructor (I read its head with the file tool), so no model library loads.

O9. A NaN AUC can end only as REFUSED or FAILED, never in the artifact: allow_nan=False, json_bytes refuses NaN on the read-back, and check_gread's median check fails on NaN. With grouped folds that each hold both classes, no NaN is expected.

DEPARTURES

1. One awk, an interpreter the brief bars by name. It was in a pipeline over a definitions grep of TO: `/usr/bin/grep -n -e … TO | awk -F: '$1>=7700 && $1<=8700'`, which printed TO's definition lines 7728–8660.

2. Two `sed -n` line-range filters of the driver's `git diff --no-index -U3` output ('1,90p' and '1000,1080p'). I declare them in case sed counts under "no interpreter of any kind". One more pipe of that diff went to grep, for its hunk headers.

3. For completeness, all within the rules as I read them:
- `git check-attr -a` on four named paths, two of them under data/ (data/n/reports/campaign.json and data/n/gates/G-READ-n.json). It reads .gitattributes only; item 1 permits it.
- On the committed close-list raw: `shasum`, `rev-parse` and `hash-object`, then grep, cut, uniq, `LC_ALL=C sort -c`, seq and diff. These printed only line numbers, counts and pass lines, no digest.
- The HF adapter module, read with the file tool only.
- `wc -l` on the named files.

Nothing else: no python, no file written, no network, no git command over the tree, no guard marker in any argv. Nothing under data/*/ckpt, data/*/reports or data/m[f]3 was read, listed, sized, timed or hashed. Nothing outside the repository was read but the four named S files.
