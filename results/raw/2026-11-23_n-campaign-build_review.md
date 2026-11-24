# n — the N-pod campaign's BUILD: the blind review of draft 1, as returned, with every disposition

PI date 2026-11-23. Code (the n-build session). LOCK-n.md is cited as LOCK-n v1.0 cites it (LOCK-n.md:54–57):
`L:N` is line N of v0.1's text, as `deabf3f` numbers it; a line of the file at `098218c` is `LOCK-n.md:N`. The
report in §2, as returned, writes `L:N` for the file's line at `098218c`, its brief's form.

**What was reviewed.** One blind pass by a subagent over the change as draft 1 had it, at HEAD `098218c`:
- `scripts/n_sessions.py`, HEAD's (`55885e65…385f`) to draft 1 (`9b51bb18…64c0`, 7,570 lines);
- `.gitignore`, HEAD's (`81f5f227…b610`) to the draft (`fe865233…03ed`): G-TIME-n's two steered cells' lines and its
  comment changed, and one block added for the campaign.

Draft 1 had passed its self-test, 764/764, in a battery window.

**The reviewer's brief** was given to the reviewer as its prompt: Code's scratch file `S/step4b/camp/review_brief.md`
(`aebb58a4…6004`, 125 lines). It:
- named the change and its specification: Code's readings CP1–CP20 as sent, the seat block as then drafted
  (`033ecaf1…4a60`, 320 lines), the survey's report, the texts, and the code the change must match or use;
- named eleven things Code knew of, to be declared;
- asked for findings, surviving mutants, box risks, observations and departures;
- barred any interpreter but `shasum`, any write, any network, any guard marker in an argv (a grep pattern and the
  command's own text included), and Q-F3's folder by its plain name in any argv;
- barred anything under `data/m[f]3`, any whole-tree git status, any read, listing, size or time of a ckpt or reports
  file, any look for G-TIME-n's two steered cells, and anything in Code's scratch but the named files and the brief;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec with `':!data/m[f]3/**'` on every
  git command over the tree.

**The report** is in §2, extracted verbatim by `jq` from the hand-back in the subagent's own transcript (180 lines,
sha256 `be059ba1270e3d845f20cd74e85d14559921fe7f08563309fbd215b87bb2e572`). It names scratch files only by their paths
inside the scratch folder. One abbreviation in its first lines is a slip: the block's sha256 `033ecaf1…2a60` is
`033ecaf1…4a60` by tool (the brief gives it in full).

**In sum:**
- two BUGs, F1 (latent) and F2 (low);
- 11 findings: F1–F2 BUG, F3–F5 RISK, F6–F11 NIT;
- 13 surviving mutants, M1–M13;
- 9 box risks, B1–B9;
- 11 observations, O1–O11;
- its departures, declared: line counts by `wc -l` of named files; the two prescribed diffs piped into `grep` and
  `sed -n`; and tool output (never an argv) that printed Q-F3's folder and marker-named paths as text.

**The drafts after it:**
- Draft 2 (`7249b88f…d9b5`, 7,831 lines) builds in F1–F5, F8–F10, F11's docstring, B7, O4 and O6. It adds a kill
  for every mutant, by Code's reading of each case and not by a mutation run: 10 run-time checks more, 8 new `chk`
  calls and 2 argv cases, with several checks extended. It passed its self-test, 774/774, in a battery window.
- Draft 3 (`fd643681…26d9`, 7,834 lines) is draft 2 with four corrections in docstrings and a comment after the
  BUILD's values-check (+6 −3; its items 14, 80 and 81, and its observations 8 and 9). No check reads them. It passed
  its self-test, 774/774, in its own window, its output run 2's bytes.
- Draft 4 (`47abe489…c21a`, 7,836 lines), the BUILD's driver, is draft 3 with one docstring clause and the `campaign`
  command's usage message corrected after the focused values-check (+4 −2; its item 76 and its observation 4). No
  check reads either. It passed its self-test, 774/774, in its own window, its output run 3's bytes.

The seat block was still in scratch at the review. F1, F3, F4, O2, O4, O6 and B7 change what its CP8, CP9 and CP12
say Code will build, and O3 and O5 are questions for the seat; the block carries them (its Q3 and Q4 for O3 and O5), as
edits made after its values-check and replayed by tool at its commit.

## 1. Dispositions

- **F1 (BUG, latent), a rendering pause's excerpt on N4's told reads. Applied.**
  - `_camp_rendering(plan, loaded, pause)` takes the paused read from the plan by its launch index.
  - For N4-T and N4-Ts it builds the told or sham line by the schedule's zone, as the runner does (runner:472–474).
  - It compares the sequence's `ids_sha` with BK's only for an untold read. A told or sham sequence's is printed "as
    found now".
  - The renderer's refusal is given in the package's masked form (`ids._problem`).
  - The PAUSE branch passes the plan.
  - A new check runs each form on the ids of record: an untold read, N4-T, N4-Ts, a missing sequence, a pause whose
    read is not the plan's at its launch index, a launch index past the plan, a pause of another kind, and a
    rendering pause with no launch index (none for each of the last two). It kills M9.
- **F2 (BUG, low), G-VER's failed checks over-counted (a session whose ids failed, three times). Applied.**
  `camp_gver_mismatches` counts:
  - the sessions whose ids failed;
  - among the sessions whose ids passed, those whose spans failed and those whose N4 sequences failed;
  - the kept label candidates that failed;
  - the two manifest flags;
  - at least one in all.

  The counting check's fixtures are states `verify` can return. One bad session's ids alone make 1, and every term
  counts in a case of 7, which kills M10. The flow's STOP fixture now has ids, spans and N4 at 159.
- **F3 (RISK), a failing excerpt turned exit 3 into exit 1. Applied.** The excerpt runs inside a handler. A failure
  prints one line, "EXCERPT pNN unavailable: <kind>; the pause stands in the report", and the exit stays 3. A new
  check refuses the paused cell through a stand-in for `cells.load_cell`.
- **F4 (RISK), G-VER's record left without a report. Applied.**
  - `_camp_write_report` takes `new=`. A write or read-back that fails ends as SystemExit, naming an OSError by its
    kind, and a new report is then removed.
  - When the start's report fails, `run_campaign` removes G-VER's record, says so, and fails with exit 1.
  - The PI's stop (`new=False`) removes nothing: the file stays as the failed write left it (the PAUSE report,
    unless the replace had happened), for the seat.
  - A new check fails the report's write through a stand-in for `m_resume.atomic_write_json`, in two forms (an
    OSError, and bytes on disk other than those written). Neither file is left.
- **F5 (RISK), coverage. Applied, with a case for each of (i)–(vi):**
  - (i) a resume with its ruling reaches the runner with resume True, the ruling, the stage's root and report (never
    G-VER's STOP record's path) and the cap (M6–M8);
  - (ii) five failures after the preparation, each exit 1 with the runner not called and nothing written: the
    tokenizer's load refused, a SystemExit(0) from the decode, the loaded adapter's provenance and its shape (M4, M5),
    and a SystemExit(None) at the load;
  - (iii) a valid COMPLETE report with `--resume`, refused before any load (M1);
  - (iv) a record on disk with no report, then a resume ending at G-VER's STOP: exit 6, nothing written (M2);
  - (v) a ceiling pause whose read is in a cell, with another read's record first in it (M3);
  - (vi) the PI's stop on another pod (M11).
- **F6 (NIT), CP4's "the BUILD's driver blob". Declared** in the BUILD entry, and named in the module docstring's
  PINs header (draft 3). The DRIVER line prints the driver's sha256,
  m-F3's convention as written (mF3ans:43), and the module docstring's CP4 line says so.
- **F7 (NIT), GT11's two `.gitignore` lines added at the BUILD. Declared** in the BUILD entry. ans21b:32 has the lines
  come "at step 14's close". They come now (CP10), and admit nothing until the two names are placed at the close, so
  the close's commit needs no `.gitignore` change.
- **F8 (NIT). Applied:** a binomial fire with no read is "at the run's end (the tail's evaluation)", checked.
- **F9 (NIT). Applied:** `LOCK_CAP_LINE` is the lock's whole span, "4 × 3,600,000 = **14,400,000 ms**"
  (LOCK-n.md:106; U+00D7, bytes C3 97 by `od`). The check holds the leading "4 × ".
- **F10 (NIT). Applied:** the status check reads LOCK-n.md's third line, the status line.
- **F11 (NIT). Applied in wording, and checked at the commit.** GT11's docstring sentence now says the two steered
  cells are committed with the campaign's cells at step 14's close (LOCK-n v1.0 §13), as the `.gitignore` says. The
  two raw names the docstring cites are the seat block's commit's, by tool: both are files of `fcab1e5` (`git
  cat-file -e` of each there), and draft 4 cites each once.
- **M1–M13.** Each is killed, by Code's reading, by the case its row names:
  - M1 by F5 (iii), M2 by (iv), M3 by (v), M4 and M5 by (ii), M6–M8 by (i), and M11 by (vi);
  - M9 by F1's check;
  - M10 by F2's;
  - M12 by two more argv cases, `--tokenizer-dir` and `--ids-dir`, each refused;
  - M13 by the PI's stop over a valid report at "time", refused as not the campaign's.

  No mutant has been run.
- **B1, agreed, and the new cases keep to it.**
  - Every new flow runs on the doubles, with writes under the self-test's temporary folder.
  - The two stand-ins are restored in `finally`, and each restore is asserted.
  - The case that calls `committed_bytes` on a path in that folder ends in its ValueError before any git call.
- **B2. Met** by F5 (ii)'s two post-load cases.
- **B3, noted.**
  - A resume after COMPLETE is now tested (M1).
  - A pause on the read that crosses the cap ends PAUSE with the cap hit. The resume after its ruling then costs one
    load and one G-VER only to write CAP, which is the runner's form. Declared in the BUILD entry.
- **B4. Carried to the launch files, and applied in part.**
  - A resume's copy is checked by name and sha256 for every cell and array before the launch, since the runner first
    opens the arrays after the load.
  - The driver now refuses a ruling that is not committed (O6).
- **B5. Met** by F3.
- **B6.**
  - (a) Applied by F4.
  - (c) The `.nfs` names a concurrent open can leave on the volume: carried to the launch files, whose copy-back is by
    name.
  - (c) The PI's stop runs only on the characterized pod: O5 is a question for the seat (Q4).
- **B7. Applied.** `_camp_why` turns any SystemExit from a seam into exit 1 with its REFUSED or FAILED line, a
  SystemExit with no message (None, 0) included, in all four handlers. The tokenizer's load and the decode have a
  handler of their own. Cases: SystemExit(0) and SystemExit(None) among the refusals before any read, SystemExit(0)
  from the decode, SystemExit(None) at the load, and SystemExit(0) from the PI's stop's pod seam.
- **B8. Carried to the close's script,** a launch file the coordinating session reads first.
  - It names the copy-back's files from the report by `camp_copy_names`'s rule: the report's cells in name order, each
    followed by its 31 arrays.
  - The laptop's campaign folder takes only those files, since the analyzer refuses any other (anl:3172–3203),
    `._*.json` included.
  - Any archive is built with `--exclude='._*'`.
- **B9. Carried to the launch files:** the campaign's box copy is a fresh checkout at the BUILD's commit, and
  G-TIME-n's run copy is left at its own commit.
- **O1, noted:** the readings as built.
- **O2. Applied in the block:** CP9 (a) now says G-VER's record is checked by `check_gver` and the report by the
  schema.
- **O3. To the seat,** in the block's Q3: the excerpt's `absdiff` beside the runner's `rel` gives the cached path's
  scale, a log-probability's size.
- **O4. Applied:** the identity's `rendering_id` is the manifest's pin, so a MANIFEST.json off its pin at a resume is
  G-VER's STOP, as at the start (L:543, LOCK-n.md:938), and not a refusal as another identity. Checked, and in the
  block's CP9 (b).
- **O5. To the seat,** in the block's Q4: a PI's stop after the pod is gone would leave the report PAUSE, which
  VERDICTS refuses (anl:6677–6679).
- **O6. Applied:** each `--ruling` must be a repository file at HEAD's committed bytes, as the PI's stop raw must;
  checked (git cannot show it; outside the repository).
- **O7, noted.** The seat's newest raw (`e07fba2c…eba9`) §2 item 4 asks for each pause "on the excerpt, in its own
  raw". The coordinating session put that raw to the PI for routing, and Code's reading of the point goes with it:
  each pause's excerpt, from the invocation's stdout, committed as a raw of its own.
- **O8, noted:** a rendering pause after the same invocation's G-VER PASS is defensive.
- **O9, noted and declared:** G-TIME-n's committed artifact and G-VER's committed record carry v0.1's lock sha256, and
  would fail their checks under the moved pin if anything re-checked them. Nothing on the campaign's path does.
- **O10:** CP4's driver of record, the seat's to confirm, is in the block's §2.
- **O11, noted:** F5's cases now cover the resume's wiring, which "the runner is a seam" did not.
- **The reviewer's departures** are declared in the BUILD entry.

## 2. The report as returned

BLIND REVIEW — the N-pod campaign's stage command (n §8 step 14). Read-only; nothing run but shasum.

Verified before reading: HEAD 098218c. scripts/n_sessions.py clean (rev-parse = hash-object 83716a92…), sha256 55885e65…385f. .gitignore clean (ef284ae9…). S/step4b/camp/draft/n_sessions.py 9b51bb18…64c0 (7,570 lines). S/step4b/camp/build/gitignore_v1 fe865233…03ed. cp_readings_v1 fd80cf43…23b0. block_v2 033ecaf1…2a60. survey_report_v1 7f728f96…43d1. results/raw/2026-11-23_n-lock-v1_0-committed-close_design-to-code_answers.md e07fba2c…eba9. All match. `git diff --name-only HEAD` with item 3's pathspec printed nothing, so valence_core/ is unchanged in the tree.

Line references: d:N is S/step4b/camp/draft/n_sessions.py line N; g:N is S/step4b/camp/build/gitignore_v1 line N.

FINDINGS

F1 BUG (latent). d:6465–6479, `_camp_rendering`.
- What is wrong: for every rendering pause it re-derives the session's untold sequence, `ids.ids_of(loaded)(s, None)` (d:6476). On N4-T and N4-Ts the runner's rendering pause comes from `ids_of(s, told)`, using the told or sham line chosen by the schedule zone (runner.py:472–483). For such a pause the excerpt prints the untold sequence's ids_sha "against BK's" — two equal digests that do not show what the pause records.
- The path is never run in the self-test.
- Reach is very low: G-VER, run in the same invocation on the same `loaded`, has already checked each session's ids_sha and both N4 lines (verify.py:94–124).
- Fix: take the paused PlannedRead from the plan by launch_index. Build the line as the runner does. Call `ids_of(loaded)(s, told)` and return `ids._problem(e, sid)` on RenderingMismatch. Compare ids_sha only when told is None. Add a test for each form.

F2 BUG (low severity; a descriptive figure). d:6316–6325, `camp_gver_mismatches`.
- What is wrong: `verify.verify` skips a session's spans and N4 checks once its ids fail (verify.py:94–105, `continue`). So `n - spans_ok` and `n - n4_ok` count that session again, and one bad sequence gives rendering_mismatches = 3. The docstring calls checks that never ran "failed".
- The self-test's fixtures cannot show it: `rep_stop` (d:7061: ids_ok 159, spans_ok 160, n4_ok 160) and the counting case at d:6944 (ids 159, spans 160, n4 158) are states verify cannot return.
- Fix: k = (n − ids_ok) + (ids_ok − spans_ok) + (ids_ok − n4_ok) + (labels_kept − labels_ok) + the two manifest flags, still max(1, k). Use fixtures with spans_ok and n4_ok ≤ ids_ok.
- Impact: nothing reads the figure on the NOT-RUN path, and the schema needs only ≥ 1.

F3 RISK. d:6718–6724.
- What is wrong: the excerpt runs after the runner has written the PAUSE report, outside any try. Any error in `_camp_paused_record` (cells.load_cell's SystemExit on a cell or array check, a volume OSError) or in `_camp_rendering` ends with exit 1 and a traceback or bare message. The report on disk says PAUSE, so the launch's three-way read (exit, last line, report) contradicts itself.
- Fix: wrap the excerpt loop, print one "EXCERPT … unavailable: <type>" line, and still return 3.

F4 RISK. d:6669–6677.
- What is wrong: G-VER's STOP at the start writes the record (`gver_write`, which removes only its own failed file), then the report. If the report's write fails, the record stays without a report:
  - a schema refusal is caught and exits 1;
  - an OSError from atomic_write_json is not caught at all.
- Every later start is then refused at d:6536 ("nothing resumes after a STOP"), and VERDICTS has no report for no-arm:gver-stop.
- Fix: on any failure of the report's write, unlink the record and re-raise.

F5 RISK (coverage). The runner is a seam, and the self-test never checks what a resume hands it:
- No flow case reaches the runner stub with --resume (env5, d:7189–7198, stops at G-VER). So `resume=` (d:6711), `rulings=` (d:6709) and `root=` / `report_path=` (d:6705) are unchecked.
- The post-load provenance and shape refusals (d:6699–6702) never fire.
- `_camp_paused_record`'s lookup is reached only with an empty root (env2).
- `_camp_rendering` is never run past its guard.
- A resume after COMPLETE is never tested (CAP only, d:7264–7266).
- M1–M8 survive because of these gaps. Add:
  - (i) a PAUSE-report fixture plus `--resume --ruling` with G-VER PASS, asserting the stub got resume True, the rulings, and the root and report paths;
  - (ii) a stub adapter with another provenance, and one with another shape, each exit 1 with the runner not called;
  - (iii) a valid COMPLETE report fixture with --resume (prior_state reads JSON only, so per_arm and cells entries need only sum to the plan);
  - (iv) a cell JSON with one record and no report, --resume and G-VER STOP, expecting exit 6 with nothing written;
  - (v) a ceiling pause whose read is in a cell on disk;
  - (vi) --pi-stop on another pod.

F6 NIT (declare). d:6566 against CP4.
- CP4 as sent says "the campaign's STAGE line prints the BUILD's driver blob". The build prints the driver's sha256 on its DRIVER line, which is m-F3's convention as written (results/raw/2026-11-15_lock-m-f3-v1_design-to-code_answers.md:43: "the campaign's DRIVER line prints the new one").
- Sound, and the docstring's CP4 line (d:319–320) says so, but item 6's list does not name it. Declare it in the BUILD entry.

F7 NIT (declare). g:343–344 against ans21b:32.
- The ruling commits the two steered cells "at step 14's close … with GT11's two .gitignore lines". The BUILD adds the two lines now (CP10).
- Sound (the names stay absent until the close), but a departure from the ruling's words that CP10 does not name. Declare it, or move the two lines to the close's commit.

F8 NIT. d:6429. A binomial fire at the run's end prints "at read None (None)". Say "at the run's end" instead.

F9 NIT. d:6158 and d:6822–6823. LOCK_CAP_LINE omits the lock's "4 × " (L:106), so the check named "4 x 3,600,000 = 14,400,000 ms" never holds the 4. Pin the whole span.

F10 NIT. d:6821. The test that the status line is "**Status: LOCK-n v1.0 — COMMITTED" would also pass on L:376, the code block holding the draft's proposed status wording. Tie it to the file's third line. The sha256 equality already covers the file, so only the check's name claims too much.

F11 NIT.
- d:288 and d:312 cite results/raw/2026-11-23_n-campaign-starred-eight_code-to-design_STOP.md and results/raw/2026-11-23_n-campaign_spec.md. Neither is in the tree yet; check both names at their commit.
- d:225 (GT11 in the docstring) still says the steered cells "stay on the box until the seat rules on them", the sentence g:335–339 corrects.

SURVIVING MUTANTS (each one line of production code; every self-test check still passes by my reading)

| # | Line and change | Wrong behaviour | Check that would kill it |
|---|---|---|---|
| M1 | d:6616: `("COMPLETE", "CAP")` → `("CAP",)` | A resume after COMPLETE loads the weights and rewrites the report with another loads_ms entry | F5 (iii) |
| M2 | d:6619: `fresh = prior is None` (drop the done_read_ids term) | After a crashed first invocation, G-VER's STOP writes the record, the report fails the schema, exit 1, and the record blocks the stage | F5 (iv) |
| M3 | d:6462: `==` → `!=` | The excerpt prints another read's absdiff | F5 (v) |
| M4 | d:6699: condition → `False` | A mismatched loaded provenance is not refused | F5 (ii) |
| M5 | d:6701: condition → `False` | A wrong checkpoint shape is not refused | F5 (ii) |
| M6 | d:6711: `resume=False` | Every resume is refused by the runner after the load | F5 (i) |
| M7 | d:6709: `rulings={}` | Same as M6 | F5 (i) |
| M8 | d:6705: `report_path=ctx["gver_stop"]` | The runner writes the campaign's report over G-VER's STOP path | F5 (i), or assert in1.report_path in the COMPLETE flow |
| M9 | d:6471: `[3]` → `[2]` (or any change past d:6469) | Wrong session in the rendering excerpt; never run | A rendering-pause flow (F1's fix) |
| M10 | d:6322: drop `+ (n - int(v["spans_ok"]))` | Count wrong | A counting case with spans_ok below ids_ok |
| M11 | d:6742: `if pod is None:` | The PI's stop runs on any pod | F5 (vi) |
| M12 | d:7451: drop the `--tokenizer-dir` tuple (or d:7452's `--ids-dir`) | The option is accepted and ignored | Two more argv cases at d:7356–7367 |
| M13 | d:6403: drop `ident["stage"] != CAMP_STAGE or` | A PI stop over another stage's report (low; production reads only campaign.json) | A fixture under a "time" identity |

BOX RISKS

B1 The self-test on the box (RUNPOD_POD_ID set, code committed, weights present): by my reading no case loads a tokenizer or the weights, or writes under data/n/ckpt/campaign or data/n/reports.
- Every run_campaign and run_campaign_pi_stop call runs on `genv` doubles. Its root, report and STOP record sit under the self-test's tmp, and genv refuses any of them inside the repository (d:7113–7115).
- Direct writes go only under tmp. The "rawrepo" case's committed_bytes raises ValueError before any git call.
- main()'s cases pop RUNPOD_POD_ID, trap the four loaders, and swap both stage functions for recorders (d:7316–7397).
- Residual: the twelve argv cases rely on argparse erroring first. If one did not, the real stage would run `guard.refuse_out` and stat data/n/reports/campaign_gver_stop.json, then refuse at the pod check, with no load and no write. `environment_provenance` (which makes a CUDA context) is untrapped but comes after the pod check.
- A tmp folder on the box's local disk remains the launch files' job; the driver refuses only a tmp inside the repository (d:412–413).

B2 The load is the same as G-TIME-n's (d:6694–6704 against d:4420–4429), but the campaign's own post-load refusals are untested (M4, M5).

B3 The cap:
- The cap reaches StageInputs (asserted), and CAP exits 5.
- A resume after CAP is refused before the load (tested); after COMPLETE also refused, but untested (M1).
- A pause on the read that crosses the cap ends in PAUSE with cap.hit set. The resume after the ruling costs one load and one G-VER only to write CAP (the runner's form).

B4 A resume in a fresh copy:
- Before the load the driver reads only the report and the cell JSONs. The 4,278 arrays are first opened by the runner after the weights load, so an array missing or off its hash costs a load and a G-VER before exit 1.
- The launch's by-name sha256 check of every copied array is the only guard.
- A ruling need only be a file (d:6550–6552); see O6.

B5 The excerpt's read of a paused cell uses read-only maps and unlinks nothing, so there is no `.nfs` hazard. But any failure there turns exit 3 into exit 1 (F3).

B6 The STOP writers:
- (a) writes the record and the report as two separate writes (F4).
- (c) replaces data/n/reports/campaign.json atomically on the volume. A concurrent open of the old file can leave a `.nfs…` name there, which the by-name copy-back passes over.
- (c) runs only on the characterized pod with the PI's raw committed at the copy's HEAD (see O5).

B7 The exits:
- An uncaught exception exits 1 with no last line.
- A SystemExit with a non-string code (None or 0) is re-raised (d:6655, 6683, 6717) and would exit 0, COMPLETE's code, with no COMPLETE line. The launch's three-way read catches it.

B8 The copy-back:
- `camp_copy_names` (d:6304–6313) has no command, so the close's script builds its list another way, and the self-tested function may not be the one that runs.
- The laptop's campaign folder may hold only the cell JSONs and arrays they name: the analyzer refuses any other file, `._*.json` included (n_analyze.py:3172–3203).

B9 If a box copy that holds G-TIME-n's steered cells under data/n/ckpt/time/ is moved to the BUILD's commit, g:343–344 un-ignore them and `git status` there lists them. Leave G-TIME-n's run copy at its own commit.

OBSERVATIONS

O1 Readings CP1–CP20 against the code:
- CP1 holds: the driver alone; the plan by campaign_order, held to read_plan_sha256 and 7,680 reads (d:6294–6301); the runner's run; options --resume, --ruling and --pi-stop.
- CP2 holds: argparse refuses --smoke and --out.
- CP3 holds:
  - all 28 sha16s equal LOCK:697–708 by name (compared one by one);
  - rows 0–3 come from the committed directions file at gvec.json's files_sha256;
  - the 24 random directions come from keys.random_directions;
  - the sample (15 ids joined by newlines, no trailing newline) and N4's schedule are re-derived as LOCK:805–817 forms them.
- CP4 holds, with F6.
- CP5 holds, with F9 and M1.
- CP6: no margin on any driver line (but see O3).
- CP7: G-VER of record's form, before every load.
- CP8 holds as the block builds it, with F1 and F3.
- CP9:
  - (a) d:6669–6677 and d:6348–6370; the record is checked by check_gver and the report by the schema, each read back;
  - (b) nothing written, the record printed whole;
  - (c) PAUSE only, raw at HEAD's committed bytes;
  - with F2 and F4.
- CP10 holds, with F7.
- CP11, CP13, CP16, CP17, CP18, CP20: nothing in the driver, as stated.
- CP12 holds: per-end last lines; F3.
- CP14: B8.
- CP15 holds.
- CP19: 46 checks, which with HEAD's 717 and the wrapper's 1 make 764; with F5.

O2 The eight starred readings each sit in one place: CP2 in main's option list and the STAGE line; CP8 in the three excerpt functions and the PAUSE branch; CP9 in the G-VER branch and the two STOP writers; CP12 in CAMP_EXITS (d:6178) and the last lines; CP6, CP11, CP13 and CP16 in no code. Each "As Code will build it" holds, except F1. One wording point in the block's CP9 (a): "Each is checked by the schema" — G-VER's record is checked by the driver's check_gver, not the schema.

O3 For Q3: the excerpt prints absdiff at full precision, and the runner's per-read line already printed that read's rel. absdiff / rel gives the cached path's scale, max(|log p(S)|, |log p(U)|). That is a log-probability magnitude, not a margin or a pick.

O4 For Q4 and Q6:
- (b) after a crashed first invocation (records on disk, no report) writes nothing, so no report exists at all.
- At a resume, a MANIFEST.json off its pin changes the identity's rendering_id (set from the loaded file, d:6605). It is refused before G-VER (exit 1, "another stage identity"), whereas at the start the same cause is G-VER's STOP (a), as LOCK:938 lists it.

O5 For Q4: the PI's stop needs the live characterized pod. If the PI stops after the pod is gone, the report stays PAUSE, which VERDICTS refuses (n_analyze.py:6677–6679), so n:134's "a PI stop" would have no record.

O6 A ruling raw need only be a file, while the PI's raw must be committed. The launch should check that the ruling is committed (CP8's route).

O7 The seat's newest raw §2 item 4 says "on the excerpt, in its own raw". The build prints the excerpt into the invocation's out raw; a separate raw per pause is the seat's call (Q3).

O8 A rendering pause is practically unreachable in the campaign after the same invocation's G-VER PASS (see F1); the rendering excerpt is defensive.

O9 With the pin moved, the committed G-TIME-n artifact and G-VER record (both carrying v0.1's lock sha) would fail `_check_gtime` (d:4226) and `check_gver` (d:5333) if anything re-checked them. Nothing on the campaign's path does.

O10 LOCK v1.0 §4 (L:160–162) names the driver at d714372; the campaign runs the BUILD's driver (CP4's question for the seat).

O11 Item 6's list:
- All entries are sound as declared.
- "The runner is a seam" must not be read as covering the resume wiring (F5).
- `_report` is used in production, `_pause` in the self-test only; that is safe while the package is frozen.
- The G-VER STOP forms carry F2 and F4.
- "Fresh" and the COMPLETE refusal are untested at their boundaries (M1, M2).
- The `N*.json` admit is right: every arm starts with N; `*.json.tmp`, `._*` and `*.npy` files stay ignored.
- I did not recompute the package digest (no interpreter).

DEPARTURES
- `wc -l` on the five named scratch files and on eleven named repository code files (line counts only; nothing under data/).
- The two prescribed `git diff --no-index -U3` runs. The driver's diff was piped into /usr/bin/grep for its hunk headers and twice into `sed -n` for paging.
- Tool output, never argv, printed Q-F3's data folder plainly: my Read of .gitignore lines 230–405, and the seat raws' "not opened" lines. Reads of the draft and package also printed marker-named paths as text constants; no file with a marker in its path was opened.
- Otherwise none: no interpreter but shasum, no write, no network, no marker in any argv or pattern, no whole-tree git status, nothing in S listed, nothing under data/m[f]3, data/*/ckpt or data/*/reports read, listed, sized or timed.
