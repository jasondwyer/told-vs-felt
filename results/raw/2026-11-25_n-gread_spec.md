# n — G-READ-n's specification as the texts state it, Code's readings GR1–GR14, and the coordinating session's routing of them

PI date 2026-11-25. Code (the n-build session).

**What this raw holds.** It serves the seat's read of the two starred readings (the block committed beside it) and
G-READ-n's BUILD (n §8 step 15):
- **§1, Code's readings GR1–GR14 as sent, verbatim** (`17d66da9…9b43`, 195 lines). They went to the coordinating
  session as a note in the sessions' notes folder (`2026-11-25_n-build_gread-pins.md`), a byte copy of Code's
  scratch file, equal by `cmp`, named in Code's message by its path, its sha256 and its line count; the coordinating
  session checked it at its sha256 and read it whole before it put the readings to the PI. It is in no other
  repository file.
- **§2, the coordinating session's message relaying the PI's answer, with what it routes, verbatim**
  (`4e686ed0…1dd0`, 18 lines). It is in no other repository file.
- **§3, the survey's brief** (`d1fa766e…13fb`, 107 lines). One change: the repository's full path, on its second
  line, is written `<repo>` (`43eca2d5…72ce`).
- **§4, the survey's report, verbatim** (`979bf23e…73c4`, 394 lines). A subagent compiled it read-only at HEAD
  `95cd461` (its HEAD at start and at end, by its own report): G-READ-n's specification as the texts state it, with
  a citation for its claims, and the questions the texts leave open. It was extracted from the subagent's hand-back
  by `jq` when it returned, on 2026-11-25. Its departures are in its last section, for the seat to class.

**The cited lines.** Every file:line in §1 and §4 is the repository's at `95cd461`, but ans4's (that raw's line N):
ans4 was untracked there and is committed unchanged at `13ca2fe`. This raw's parent is `0081351`; between the two
only `RESULTS.md` and raws under `results/raw/` changed, so every code and text file:line holds at the parent, and
§1's and §4's R: anchors are `95cd461`'s.

**Points in §1 and §4, as sent, that are imprecise or since superseded.** §1 and §4 stay verbatim. The block
carries GR3's and GR5's points; the BUILD builds GR7's and GR8's as below.
- Imprecise in §1:
  - GR3's "No margin, log-probability, pick or fidelity value is computed on, printed or written": `check_cell`,
    which `load_cell` runs on every cell, holds each record's `margin` to `logprob_S − logprob_U` and the fidelity
    block's numbers to their formula, in memory (`valence_core/n/schema.py`:1007–1031, :1039–1069), and prints a
    field path alone on a refusal. The sentence holds of the command's own code, not of the package's check (the
    block's §0 and GR3).
  - GR5's "never reads N1-R's −1 cells", of the shadow reading: under GR2 every one of the 138 cells is read and
    checked, so under that reading the −1 cells would be checked and never probed (the block's GR5).
  - GR7's "k's `fit_lr`, `kfold_auc` and `kfold_shuffle_null` (probe:41; …)": probe:41 imports `kfold_auc` and
    `kfold_shuffle_null` alone; `fit_lr` reaches the probe through `kfold_scores`
    (`valence_core/echo/probe.py`:78–92), which `kfold_auc` calls (:97).
  - GR8's "the output absent (`guard.refuse_out`, guard:74–81)": `refuse_out` refuses a path under its refused
    roots, or inside the repository outside `data/n/`; it never tests whether the output exists. The test of
    absence is GR12's "refused if it exists", which the command makes itself.
- Imprecise in §4: its 2.8's "The only `VECLIB_MAXIMUM_THREADS` is in a note-audit script
  (scripts/audit_note_N3_compute.py:1156)": that script names it at :710, :1156 and :1184, and one raw names it
  (`results/raw/2026-10-08_note-N3-echo-compute.md`:9). None is in n's code, so the point stands.
- True at `95cd461` and superseded since:
  - §4's 1.5, "The PI's routing item 2, as the brief quotes it, is not committed at HEAD": it is committed at
    `13ca2fe`, in `results/raw/2026-11-25_fourth-sitting_pi-routing.md`:24–29, in the brief's words;
  - §4's 1.5, "The latest committed routing raw is 2026-11-24's": two of 2026-11-25 are committed since, at
    `13ca2fe` and `5ceb8dd`;
  - §1's and §4's heads call the seat's raw untracked: it is committed unchanged at `13ca2fe`.

**How §2 was taken.** It was extracted from this session's transcript, a departure declared in the entry that
commits this raw: `sed -n` of the message's record, through `jq` for its content, then `sed -n` of the content's
lines 3–20. Those are the message's own 18 lines, without the delivery wrapper, which names a session by its id.

**What it does not name.** None of the four sections names a path in the home folder or the scratch folder's full
path, once §3's one line is written as above. Scratch files are named S/...

## 1. Code's readings GR1–GR14, as sent

```text
# G-READ-n (n v0.2 §8 step 15): Code's PINs GR1–GR14, for routing

Code, PI date 2026-11-25. Built on the read-only spec survey of HEAD `95cd461`, which is origin's
(`S/step4b/gread/spec/survey_report_v1.md`, `979bf23e…73c4`, 394 lines, the subagent's hand-back by `jq`; its brief
`S/step4b/gread/spec/survey_brief_v1.md`, `d1fa766e…13fb`, 107 lines), and on the seat's fourth sitting
(`results/raw/2026-11-25_n-campaign-close-read_design-to-code_answers.md`, `7f5020b9…37f4`, untracked), whose §3's six
points are carried in. The survey's 15 open questions are answered below, the Q-number in brackets, with Code's own
checks of the lines the readings turn on. ★ = the seat's. The route is item 2 of the PI's routing of that sitting:
"the survey and PINs, the spec raw and the starred readings committed for the seat before the run, in the campaign's
form … [go, on the seat's ruling before the run]". Every other PIN is Code's. Nothing goes to the box.

Short forms: n = PROPOSAL-n v0.2; LOCK:N = LOCK-n.md's file line N at `098218c` (ans4's L:N; v0.1's own L:k is
LOCK:395+k); A-n1 = ADDENDUM-n1; drv = scripts/n_sessions.py (`47abe489…c21a`); anl = scripts/n_analyze.py, v7
(`735da934…a7a8`); probe, cells, schema, guard = valence_core/n/<name>.py; kprobe = valence_core/echo/probe.py; R:N =
RESULTS.md's line N at `95cd461`; ans4 = the fourth sitting's raw; ans24, ans21b, ans18c, rt23a as the survey names
them; the close list = results/raw/2026-11-25_n-campaign_close-names.txt (`42682630…fe6d`, 4,417 lines); the report =
data/n/reports/campaign.json (`1cabeadf…c4e3`); the staging folder = `../jspace-lab-box.noindex/n/campaign-v1/`.

## The stage

- **GR1 A `gread` command in the driver alone [Q1].**
  - The analyzer's bytes and the package's do not change (ans4 §3 points 1–2): VERDICTS refuses a lock that does not
    name v7 (anl:6691–6693; LOCK:212–215) and an artifact whose probe ran under another n package (anl:6473–6474).
    So the command lives in drv beside `gread-bench` (drv:4533–4604). drv already holds the pins it needs
    (`LOCK_SHA256`, the package and its closure, the read plan's sha256; drv:3894–3918) and the campaign start's
    refusals (`_camp_prepare`, drv:6554–6669); a script of its own would copy them. The package's import guard
    admits either (primitive.py:6).
  - Its one option is `--staging DIR`, the staging folder; every other option is refused, as gread-bench refuses all
    (drv:7755–7759). It writes the artifact of record at its one path (GR12): no `--out`, no smoke, no resume, "one
    model-free run" (ans4:32). Refused on a pod, in gread-bench's form (drv:4588–4589).

- **GR2 The inputs, and what binds each [Q2, Q3, Q4, Q13].**
  - From the repository, HEAD's committed bytes each: LOCK-n.md at `LOCK_SHA256` (`gver_lock_check`, drv:6606); the
    close list at a new pin, its sha256; the report at the sha256 of the close list's first line, held to the lock:
    `end_state` COMPLETE, every arm complete, its identity's `lock_sha256`, `package_sha256` and `capture_layers` (33
    through 63, LOCK:869), its `read_plan_sha256` `LOCK_READ_PLAN_SHA256`, its `stage_identity_sha256` the identity's
    own (schema's `identity_sha256`), 138 cells.
  - From the staging folder, by name and never by listing: each of the close list's 4,417 paths re-hashed under
    `--staging` and held to its line (the report's copy, the 138 JSONs, the 4,278 arrays), as `shasum -c` held them at
    the close (R:160–167). Then each cell through `load_cell(staging, arm, direction, label, identity=None,
    keep_arrays=…)` (cells:135–174; the package BUILD's PIN, R:11583–11585): `check_cell` (which holds each record's
    `capture.row` to its index, schema:1124), each layer's written rows against the cell's `capture_sha256`, each row
    against its record's sha16. With `identity=None` a missing cell refuses (cells:142–144), never a new empty one.
    Each staged JSON's sha256 is held to the report's `json_sha256`, and its `capture_sha256` and `stage_identity` to
    the report's.
  - All 138 cells are read and checked, so the artifact's `campaign.cells`, every cell as anl:6469–6472 requires, are
    "the cells read" (schema:1240). The arrays are kept only for the cells probed (GR4–GR6).
  - Not inputs: anything on the box (ans4:45), G-TIME-n's cells, and anything in the staging folder the close list
    does not name. A staging root inside the repository is refused.

- **GR3 ★ What is read of a cell [Q6].**
  - **The texts:** ans4:32: "nothing of the cells' margins read or printed — the probe reads residuals and labels";
    n:130: stdout prints "never a margin". The package BUILD's PIN: "G-READ-n's driver reads captures only through
    `cells.load_cell(..., keep_arrays=True)`" (R:11583); `load_cell` parses every record and `check_cell` validates
    it, margins included (cells:146–150), a refusal redacted to its field path (cells:72–75).
  - **The reading:** the package's reader parses each record whole, as the PIN of record has it; the command takes
    from each record its `session_id` and its row and nothing else, and drops the cell before any fit. No margin,
    log-probability, pick or fidelity value is computed on, printed or written. The labels are the cells (+ pole,
    − pole or shadow); the groups are the session ids. The self-test plants sentinel values in every margin field
    of its stand-in cells and asserts that none reaches the probe's inputs, stdout or the artifact.
  - **For the seat:** whether "nothing of the cells' margins read" admits the package reader's parse. The other
    answer needs a reader that skips the margins. The package cannot change, so that reader would be the driver's own
    JSON parse, outside `check_cell` and outside the PIN that binds the rows through `load_cell`.

## The probe

- **GR4 The six primary results, their contrasts and rows [—].**
  - One result per (axis, point) of `GREAD_AXES` (schema:1135): valence at +1, +1/2, +d_20 and +d_eq; span_reward at
    f0.10 and f0.20. Every point is kept and none merged (LOCK:763–765), so `merged` is [] in each result, as
    anl:6477–6483 checks against the dose map.
  - The contrasts (n:121; A-n1:56; LOCK:964; probe:29–31; `check_gread`): valence +1 against valence −1, `contrast`
    "pole" (N1-V's two cells, 160 sessions each); every other result against the shadow, `contrast` "shadow" (N1-V's
    `none` `0` cell, the same 160 sessions; N2-E's two cells for span_reward). y is 1 for the + pole's rows and 0 for
    the other's; the groups are the session ids (`contrast_rows`, probe:52–60, which refuses unequal session sets).
  - Each result by `probe.result` (probe:86–113) over the 31 layers, one (X, y, groups) per layer, at 1 + 200 calls a
    layer (`layer_auc` at `N_SHUFFLES`, `SHUFFLE_SEED` and the `cv_seed` given).

- **GR5 ★ The comparator at +1 [Q5].**
  - **The texts:** probe:32–33, the reading LOCK:1261 pins ("The probe's (probe.py:29–34): the contrasts and the
    comparator"): "each random direction's band median on the same contrast at the same dose point (its own 40
    sessions), not shuffled". ans21b:23 (Q5, "Stands as built"): "a comparator is a property of the point — 24
    directions at that norm against the shadow — not of the axis compared against it". LOCK:962–964: "the 24 random
    directions probed at the matched point without shuffles; the contrast the − pole at valence +1, else the shadow".
    The count is the same either way: 2,976 calls on 80 rows (drv:4533–4547).
  - **The reading:** the lock's pinned one. At +1, each random direction's +1 against its own −1 (N1-R reads −1 on
    the same 40 floor sessions, LOCK:834), the contrast valence +1 is read on; at +1/2, +d_20 and +d_eq, its point
    against the shadow. The comparator then reads the same contrast as the result it is the floor for. ans21b:23's
    sentence holds at every point but +1, where only valence is matched.
  - **For the seat:** which comparator the +1 result is held to. The shadow reading holds valence's ± contrast to the
    random directions' + against the 40 floor sessions' shadows, a floor on a different contrast from the result's,
    and never reads N1-R's −1 cells. Nothing else changes.

- **GR6 The comparator's form and matching [—].**
  - Per random point (+1, +1/2, +d_20, +d_eq) and direction (the 24 of `RANDOM_IDS`): `layer_auc(…, shuffles=0,
    cv_seed=…)` at each of the 31 layers and `band_median` over them (probe:63–75). The 24 band medians are the point's
    comparator, computed once per point and shared by the results matched to it (ans21b:23). A shadow contrast takes
    the shadow cell's rows for the 40 floor sessions, by session id (N1-R's sessions, schema:278–279, :594).
  - The matching (LOCK:964–965; drv:4536–4538): each valence point to its own; span_reward's f0.10 to +d_eq and its
    f0.20 to +d_20.

- **GR7 The settings, the bar and NOT-COMPUTED [Q10].**
  - The probe is unchanged: k's `fit_lr`, `kfold_auc` and `kfold_shuffle_null` (probe:41; kprobe, `d90f9281…2b81`, in
    the lock's closure). `cv_seed` 20261116 and `shuffle_seed` 20260905 stand as ruled (LOCK:322–323; LOCK:823–825);
    the command holds `probe.CV_SEED` and `probe.SHUFFLE_SEED` to two new driver pins of those values, and passes the
    one `cv_seed` to both `probe.result` and `probe.artifact` (R:11587).
  - PASS iff the band median ≥ .90 and above the largest of the comparator's band medians, with no per-layer
    condition (A-n1:58; LOCK:950), as `probe.verdict` and `check_gread` compute it. 403,620 fits (ans21b:23).
  - NOT-COMPUTED is `probe.result`'s for a contrast whose reads are incomplete (probe:93–96). The report is COMPLETE
    with every arm complete, so all six results are computed; a missing or failing input is a refusal before any fit
    (GR2), never a NOT-COMPUTED result.

## The run

- **GR8 Pins and refusals [Q7].** Before any fit, in order: no pod; numpy's stream known answer (drv:6579–6581); the
  output absent (`guard.refuse_out`, guard:74–81); the driver at HEAD's committed bytes (drv:6600–6605); LOCK-n.md;
  the package and its closure measured in process, equal to the lock's (drv:6634–6638) and to the report identity's
  `package_sha256`; the close list's pin; the report; the two seeds; the staging folder (GR2). Exit 0 when the
  artifact is written, whatever its statuses; 1 on any refusal or failure, with no artifact. The artifact has no
  field for the environment or the times (schema:1231–1251), so the run's out raw records them (GR11).

- **GR9 Time, no resume [Q8].** 2.650 h at the medians and 2.769 h at the maxima for the fits (LOCK:94–95), with the
  reads of about 5 GB beside them; outside the cap (LOCK:111–114). No checkpoint inside the run: the artifact is
  written once, at the end (a temporary file beside it, fsynced, then renamed). A crash or a stop leaves no artifact,
  and the run repeats whole in a new window. Cells are opened two at a time and their rows copied before the maps
  are dropped, so the open files stay bounded (each kept map holds a file open).

- **GR10 Threads and determinism [Q9].** No text sets either. The fits run at numpy's defaults, as gread-bench timed
  them (R:4244), under `nice -n 19`; the thread variables are printed as set or unset. One repeat at the start: the
  first comparator call is computed twice and its AUCs must be equal, else a refusal before the primary fits.

- **GR11 What stdout prints [Q6].** The head: the inputs by sha256 and the environment (python, numpy, CPUs, the
  thread variables). One line per comparator point: the largest of its 24 band medians, and the ms. One line per
  result: axis, point, contrast, rows, band median, comparator max, status, layers above their null, and the ms.
  The end: the artifact's path and sha256, and the six statuses. Never a margin or a per-session value (n:130;
  ans4:32).

## The record

- **GR12 The artifact, the entry and the raws [Q11].**
  - The artifact is `data/n/gates/G-READ-n.json` (`n-gread-v1`, `probe.artifact`'s dict, checked by
    `check_gread`). It is written as G-ANL-n.json is (sorted keys, one-space indent) at its one path, refused if it
    exists, and has its own `.gitignore` admit line (.gitignore:261–262; :327–330's form).
  - It is committed by path in a window with the entry `G-READ-n` (n:161; ans4:33), which carries its sha256, and with
    the raws: the run's out and err, the window's check and after outputs, and the self-test.
  - The entry reports the six statuses, band medians and comparator maxima, the counts, the times and the
    environment. The result enters n §5 only where §0.6 says (LOCK:950). Then VERDICTS run on the PI's word, with
    `--gread` the committed artifact (ans4:58).

- **GR13 The self-test [Q12].**
  - It is part of the driver's self-test and runs in battery windows, one draft at a time.
  - Stand-ins: a small synthetic campaign (identity, report, close list, cells and arrays), written under the
    self-test's TMPDIR by the package's own writer at a small band and width; the production readers are replaced by
    stand-ins, and no pod id is set.
  - It checks:
    - every refusal of GR8 and GR2, one tampered input each;
    - the contrasts and the comparator's matching;
    - the margins' sentinels (GR3);
    - the repeat check and the write-once;
    - the artifact, through `check_gread` and the analyzer's binding conditions as anl:6459–6484 states them.
  - It cannot read the staging folder or write under data/n/ (`guard.refuse_test_out`).

- **GR14 The launch [—].**
  - It comes after the BUILD's commit and the seat's ruling on GR3 and GR5, in a battery window the coordinating
    session grants, with Q-F3 beside and declared (ans21b:23, :80).
  - It runs in G-ANL-n's three steps (R:6186–6197):
    - `check`: HEAD; the inputs at their pins; data/n/gates holding G-ANL-n.json alone; the Python processes listed.
    - `run`: the venv's interpreter, reached by a glob in a `cd`, with `-I -B`, `nice -n 19` and TMPDIR in scratch;
      in the background under `caffeinate`, the end-wait on the PID alone, and its out and err unread until it ends.
    - `after`: the inputs unchanged, and the artifact present at its printed sha256.

## Notes for the seat (citations; no question) [Q14, Q15]

- ans4 §3 point 4 cites ans18c:40 for the window beside Q-F3. That line is the `data/mf3` exclusion (ans18c §5.3);
  the window's texts are ans21b:23 and ans21b:80.
- ans4 §3 point 2's probe.py:20–22 and :24–27 are the docstring's; the import is probe:41 and the band's refusal is
  probe:122–124. "PIN-n's probe readings" is not a phrase in the lock; the nearest are LOCK:1261 with LOCK:962–968,
  LOCK:823–825 and LOCK:869.
- LOCK-n v1.0's own L:N is v0.1's line N (LOCK:54–57); ans4's L:N is the file's line. These readings write LOCK:N,
  the file's line.
- ADDENDUM-n1's commit entry recorded an observation that was never put as a question: "G-READ-n's shadow contrast
  tests the state's presence, where rule 5(f)(ii) names the sign" (R:12996). The contrasts are n:121's and A-n1:56's
  as the lock carries them; Code builds them and rules on nothing.
- The survey's departures, to be declared with the spec raw for the seat to class: one `awk` in a pipeline (nothing
  printed); two `sed -n` filters of `git grep` output; one `git grep` whose pattern held a guard marker unbracketed
  (`ipykernel`), in a search of m's guard and drivers; pathspec forms other than item 3's (quoted globs, two plain
  paths, and `':!data/**'`). Nothing under data/*/ckpt, data/*/reports or the Q-F3 folder was read, listed, sized,
  timed or hashed.

## The route from here

First, the seat block in its own window, its request carrying every sha256: the spec raw (these readings, the routing
by `jq`, the brief, the survey's report), with GR3 and GR5 as the starred questions. Next, the BUILD's drafts: the
self-test in battery windows, one blind review, one values-check, and then the BUILD's window. The launch files go to
the coordinating session first. The run comes after the seat's ruling, in a window. Nothing is built before the
coordinating session routes these readings.
```

## 2. The coordinating session's routing, with the PI's answer

```text
The PI's answer on your G-READ-n PINs (PI date 2026-11-25): build on the PINs. It is relayed verbatim below. It came in the same message as the push of 5ceb8dd and 0081351 (push #27, done).

The tree: HEAD = origin's main = 008135156811cde761a5f567f74e338444d97ef5. Push #27 was 13ca2fe..0081351: the seat's sft read with my notes, and the dpo session's dated note; nothing of n's. Nothing is staged, and nothing is untracked under results/raw. Your commits go on 0081351.

The PI's message, verbatim, between the two lines of dashes:

----------
push both and build on the pins
----------

What this means for you:
- "build on the pins" answers the question I put to the PI with your PINs (17d66da9…9b43): build now on your PINs, with GR3 and GR5 starred for the seat in the committed block before any run, rather than wait for the seat's ruling on them first. The "push both" part was mine, and it is done.
- The form is the campaign's (the seat's fourth sitting, item 2; step 14's order, fcab1e5 then e1be6d9):
  1. Your seat block first. The spec raw takes my routing with this answer; GR3 and GR5 are starred; your survey's departures are declared. It is committed by path for the seat (code → design; STOP for the seat's read). Today's routing of the seat's sft read (item 4) puts G-READ-n's spec raw and starred block first at the seat when they land.
  2. Then the BUILD on the PINs. n_analyze.py's bytes (v7) and the package (06b55761…1d39) stay unchanged. Its self-test runs only in a battery window from me: no Python on the laptop outside one, since Q-F3 is running. It is reviewed and values-checked as e1be6d9 was, and committed in a window from me.
  3. The run waits for the seat's ruling on GR3 and GR5 and the PI's routing of it. Then it runs in a battery window beside Q-F3, on the laptop, from the staging folder's arrays, with no margin read or printed.
- Each commit needs its own window. Ask for the seat block's window first, with its paths, each file's sha256 and line count, and the message's file and sha256.
Reply when the seat block is ready for its window.
```

## 3. The survey's brief

```text
You compile, read-only, the full specification of one stage of the jspace-lab repository (at
<repo>, HEAD 95cd461 = origin), so that Code can build it: **G-READ-n**, step 15
of PROPOSAL-n v0.2's §8 order, which gives it one clause (n:159): "15. G-READ-n from the captures; then analysis in a
later session on the PI's word". Step 14, the N-pod campaign, ran COMPLETE and is closed at 95cd461: its report
data/n/reports/campaign.json and its 138 cell JSONs under data/n/ckpt/campaign/ are committed; its 4,278 capture
arrays are held outside the repository (you do not look for them). The design seat's fourth sitting placed its raw
untracked at results/raw/2026-11-25_n-campaign-close-read_design-to-code_answers.md (65 lines; read it whole first):
its §3 lists six points the seat holds the BUILD to, each with anchors (its head defines L:N as LOCK-n.md's own line
N). The PI's routing of that sitting, item 2, verbatim: "G-READ-n's BUILD (step 15): the survey and PINs, the spec raw
and the starred readings committed for the seat before the run, in the campaign's form; §3's six points carried into
the PINs — above all n_analyze.py's bytes unchanged (the lock names v7; lock_names refuses otherwise) and the package
unchanged, so the command lives in the driver or its own script; A-n1 §6.2–§6.4's form and bar; the run on the laptop
in a battery window beside Q-F3, from the staging folder's arrays. [go, on the seat's ruling before the run]". The
coordinating session may commit while you read (that raw, and a close line on 95cd461's entry in RESULTS.md): print
`git rev-parse HEAD` at your start and at your end, and cite RESULTS.md by its entry's heading as well as its line.
You run no interpreter of any kind (no python, python3, node, perl, awk), write no file anywhere, and return your
report as your final message.

WHAT TO FIND, with a file:line citation for every claim:
1. The specification as the texts state it:
   - PROPOSAL-n-bk-reconciliation-v0_2.md: G-READ-n (line 121), §0.6 (line 32), §4's blinding (line 130), every use of
     G-READ-n in §5 (lines 136–142), §8's step 15 (line 159) and its entries list (line 161), and any other line that
     names G-READ-n, the probe, the captures or readability;
   - LOCK-n.md (v1.0, committed at 098218c): every line that names G-READ-n, gread, the probe, the band,
     `capture_layers`, `cv_seed`, the label shuffles, the comparator, the AUC bar, NOT-COMPUTED, the analyzer of record
     or the package of record (18 lines name G-READ-n or gread; among them L:950, the bar, and L:212–215, the analyzer);
     and whatever the lock calls "PIN-n's probe readings";
   - ADDENDUM-n1 (at the repository root) whole, §6.2–§6.4 above all (A-n1:54 and :58 among them); ADDENDUM-n3 where it
     fixes what the captures hold (positions, layers, the capture convention); ADDENDUM-n2 wherever it binds G-READ-n;
   - every item in the seat's answers raws and the PI's routing raws under results/raw/ that binds G-READ-n or its
     inputs: the fourth sitting's §3 (check each of its anchors at HEAD and say where one does not hold); ans24 §1.5 and
     LQ3 (results/raw/2026-11-24_n-campaign-starred-eight-and-launch-points_design-to-code_answers.md); the raws the
     fourth sitting abbreviates as ans18c and ans21b (find them; ans18c:40 and ans21b:23 place the run beside Q-F3);
     rt23a item 3 (the route's form); any ruling on the probe's readings, its band, its fits or its time;
   - RESULTS.md's entries that bear on G-READ-n: G-TIME-n's (7d01b02: gread-bench's 2.650 h at the medians for 403,620
     fits, and the benchmark's form), the n package BUILD entry (the probe code), G-ANL-n's (the analyzer's `--gread`
     and its battery), LOCK-n v1.0's, and the campaign's (95cd461: the close list, the arrays in the staging folder at
     their sha256s).
2. What already exists in the code that G-READ-n could use or must match:
   - valence_core/n/probe.py whole: every function with its inputs and outputs; what it imports (k's classifier at
     probe.py:20–22: name the module and its file, and read the functions it uses); the band; the capture-layer check
     (probe.py:24–27); the folds and `cv_seed`; the shuffles; the comparator; the AUC; the PASS and NOT-COMPUTED rules;
     and any artifact it builds;
   - valence_core/n/schema.py: the artifact `n-gread-v1` (schema:217–238, :1231–1264) field by field with every check
     on it; anything that names gread, the probe, a capture or the gates folder; the report's `cells` entries
     (`json_sha256`, `capture_sha256`) and the identity fields the artifact must carry;
   - valence_core/n/cells.py: `load_cell` and `keep_arrays` (cells:135–140); the row hashes; how a cell's arrays are
     named and found relative to its JSON (so that a root other than the repository's can be given); and which parts
     of a cell are residuals, labels or margins, so that a build can read the first two and never the third;
   - scripts/n_sessions.py: `gread-bench` (drv:222–237, :3884–3885, :4533–4554): its options, what it computes and
     times, its stand-in data, its outputs; the stage commands as a template (`cmd_campaign`, `cmd_gtime`): the
     refusals, the pins (`LOCK_SHA256`, the package's digest, any analyzer pin), the stage identity, the printing rules
     (never a margin), the self-test's structure and count and its box-safety traps; every line that names G-READ-n or
     gread (45 lines);
   - scripts/n_analyze.py: `--gread` (anl:42–46) and every check VERDICTS makes on the artifact (anl:6466–6476 among
     them: the plan and identity sha256s, the package, `campaign.cells`); `lock_names` (anl:6691–6693); how PASS, FAIL
     and NOT-COMPUTED enter each verdict and sentence, and what happens without `--gread`; the G-ANL-n battery's cases
     for G-READ-n's states (187 lines name gread or G-READ);
   - data/n/gates/ (G-ANL-n.json: its top-level keys and form only) and the root .gitignore's lines for data/n/;
   - the interpreter and libraries of record for the laptop's runs of n's code (G-ANL-n's run, the self-tests' battery
     windows), as committed raws and entries name them: the interpreter's form, numpy, scikit-learn, thread settings;
     and whatever any text says about the determinism of the probe's fits on a CPU.
3. What the texts leave open for a build: every point Code would have to decide that no text decides, stated as a
   question with the texts that come nearest. Do not decide them. At least: the command's name and place (the driver
   beside gread-bench, or a script of its own) and its options (the staging root, the artifact's path, a self-test);
   how the arrays are bound (the cells' row hashes, the close list's sha256s, the report's `capture_sha256`); what the
   run reads (residuals and labels), what it never reads (margins), and what stdout prints; the identity and pins the
   artifact carries and where each comes from; the number of fits and the time, any checkpoint or resume inside the run,
   and what a crash or a stop does; thread settings and determinism on a CPU beside Q-F3; NOT-COMPUTED's causes; what is
   committed (the artifact under data/n/gates/, the raws, the entry) and the .gitignore's admission of it; what the
   entry reports; the self-test's stand-ins and its battery window; and whether anything from the box, or G-TIME-n's
   cells, is an input.
4. Anything that would make G-READ-n need the seat or the PI before it runs (a missing input, a conflict between texts,
   a reading that must precede the run).

REPORT FORM: numbered sections 1–4 as above; in each, short items, each with its citation(s). Quote exact words where a
number, a bar, a STOP, a formula or a name is at stake. End with "OPEN QUESTIONS" (from 3 and 4), numbered. Write a
scratch file, if you must name one, as S/...; a repository file by its repository path; never a full local path.

RULES FOR EVERY COMMAND YOU RUN (binding; a breach is reported in a final DEPARTURES section, "none" if none):
- No interpreter of any kind, no write of any file, no network, no model or adapter code run.
- No argv may contain any of these five guard markers, in any case: mlx, jlens, qwen, olmo, ipykernel. Paths count,
  and so do search patterns and the text of the shell command itself (the shell runs each command as one zsh -c
  string, so a marker typed anywhere in a command is in that zsh's argv). File names under results/raw/ and at the
  root count too (p's lock files and drafts hold one in mixed case). A file whose path holds a marker (the model's
  data folder, the OLMo adapter, the model manifest, p's lock files) is read only with your file-reading tool, which
  runs no process; a git pathspec glob in quotes, such as 'data/ol*/...', keeps a marker out of argv for git's own
  commands. A shell variable or glob that expands to a marker in an argument is a breach, and so is a loop that
  passes a marker-named path to a command as an argument. Never glob the repository root or results/raw/ in an
  argument; use git ls-files with a quoted pathspec, or your file-search tool, instead. Write a search pattern for a
  marker bracketed ([o]lmo) if you must search for one.
- Nothing under data/m[f]3 is listed or read, and its name is never written plainly in an argument: write it
  bracketed. No whole-tree git status. Nothing under data/*/ckpt or data/*/reports is read, listed, sized or timed.
- Code's scratch folder is not read at all, but for this brief's own file; and nothing else outside the repository
  is read, listed, sized, timed or hashed: the staging folder that holds the campaign's arrays
  (../jspace-lab-box.noindex/n/campaign-v1/) above all, and any other folder beside the repository, are never looked
  into or for. The seat's raw named above is untracked inside the repository: read it with your file-reading tool.
- Every git command over the tree takes item 3's pathspec and the exclusion of Q-F3's folder: `-- .
  ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/m[f]3/**'` (a git command on named non-data files may name them
  instead).
- A glob is expanded and read before it is looped over.
- The list of record v2, items 1-5, verbatim (it governs every read):
1. **Permitted (names, ids, digests):** a bare `git status --porcelain`; a name-only `ls` (no `-l`, `-t`, `-s`, `-la`); `git ls-files`; `git ls-tree --name-only`; `git diff --name-status` and `--name-only`; `git show --name-only` and `--name-status`; `git log --name-only`; `git log` with `--format` of ids, subjects and commit times over any path; `shasum`/`sha256sum` and any program's digest that prints no byte, size or time; `git rev-parse <rev>:<path>` compared in the shell; `git check-attr`; a `find` that prunes every `*/ckpt` and `*/reports` directory (`find … \( -path '*/ckpt' -o -path '*/reports' \) -prune -o … -print`).
2. **Content.** Files under `data/*/ckpt` (the checkpoints and call logs) are read by nothing but the stage's own code, G-VER, the analyzer and the pre-push screen of item 4: no `cat`, `head`, `tail`, `json.load`, editor or search over them. Files under `data/*/reports` are the read domain (m:271; the stage writes them redacted) and may be read for their content by Code and by the seat — for a stage entry's figures, a declared counter, or a read — with nothing from them printed into a raw beyond what the entry's form reports. **Metadata:** no size or time of either directory or any file in them, in any form (`--stat`, `--numstat`, `ls -l/-t/-s/-la`, `du`, `wc -c`, `stat`, `git ls-tree -l`, `git cat-file -s`, any unpruned `find`, `mdfind` over them).
3. **Content searches** over a checkout or a tree — `git grep`, recursive `grep`, `rg`, `mdfind -onlyin`, and the pickaxe (`git log -S` / `-G`) over any range — exclude the checkpoint and report files with a form tested on this git: `-- . ':!data/*/ckpt/**' ':!data/*/reports/**'` (equivalently `':(exclude,glob)data/*/ckpt/**' ':(exclude,glob)data/*/reports/**'`, or `':!data/**'` where nothing under `data/` is wanted), or the prune for `find`-driven greps. The bare `':!data/*/ckpt'` form is not an exclusion on git 2.39.5 and is not used. A pickaxe search without the pathspec can name a commit whose checkpoint matched, which is content; it is a departure.
4. **The pre-push screen** may read every file in the range, `ckpt` and `reports` included, and prints only a per-class verdict, range totals, and one line per distinct match outside those directories; a match inside one is a count by path class and a halt for the seat.
5. **A running stage:** the end-wait is on the PID alone (O3-1); no `stat`, listing, `tail`, `Monitor` or read of its raw, checkpoint or reports until the invocation has ended — in every session, including the coordinating one.
```

## 4. G-READ-n's specification as the texts state it (the survey's report, as returned)

```text
REPORT: G-READ-n (n §8 step 15). A read-only survey of its full specification.

HEAD at start: 95cd461e518628265eea500f4e6500bff5f912c9, equal to origin/main. HEAD at end: the same, still equal to origin/main. `git log -3`, run with the pathspec, shows that no commit landed while I read. The working bytes of RESULTS.md are HEAD's blob (97f9c0c8…, checked by rev-parse against hash-object), so every R:N below is a line of RESULTS.md at 95cd461. The seat's fourth-sitting raw is untracked (`??`); I read all 65 lines first. I read the brief, S/step4b/gread/spec/survey_brief_v1.md, with the file tool and did not hash it.

Short forms used below:
- n:N is a line of PROPOSAL-n-bk-reconciliation-v0_2.md.
- L:N is line N of LOCK-n.md at HEAD. Its blob, 2f865790…, is the blob at 098218c, so this matches the seat's convention (ans4:3).
- A-n1, A-n2, A-n3 are the three addenda at the root.
- probe, cells and schema are the files of the same names under valence_core/n/.
- kprobe is valence_core/echo/probe.py; discrim is valence_core/discrim.py.
- drv is scripts/n_sessions.py; anl is scripts/n_analyze.py.
- Raws:
  - ans4 = results/raw/2026-11-25_n-campaign-close-read_design-to-code_answers.md
  - ans24 = results/raw/2026-11-24_n-campaign-starred-eight-and-launch-points_design-to-code_answers.md
  - ans23a = …/2026-11-23_n-lock-v1_0-read_design-to-code_answers.md
  - ans23b = …/2026-11-23_n-lock-v1_0-committed-close_design-to-code_answers.md
  - ans22a = …/2026-11-22_n-gver-starred-seven_design-to-code_answers.md
  - ans22b = …/2026-11-22_n-gver-record-read_design-to-code_answers.md
  - ans21a = …/2026-11-21_n-lock-committed-close_design-to-code_answers.md
  - ans21b = …/2026-11-21_n-gtime-starred-seven_design-to-code_answers.md
  - ans21c = …/2026-11-21_n-gtime-record-read_design-to-code_answers.md
  - ans20b = …/2026-11-20_n-lock-v0_1-read_design-to-code_answers.md
  - ans19b = …/2026-11-19_n-gvec-stop-lock-opens_design-to-code_answers.md
  - ans18a, ans18b, ans18c = …/2026-11-18_n-corpus-adoption_, _n-step4-smoke-pause_, _n-step4-run-pause_design-to-code_answers.md
  - ans16b, ans16g = …/2026-11-16_n-build_, _n-ganl_design-to-code_answers.md
  - ans15 = …/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md
  - PI routing raws: rt23a = …/2026-11-23_first-sitting_pi-routing.md; rt21b and rt21c = …/2026-11-21_second-sitting_ and _third-sitting_pi-routing.md; rt20b = …/2026-11-20_second-sitting_pi-routing.md; rt16b = …/2026-11-16_second-sitting_pi-routing.md
  - Code's raws: spec-camp = results/raw/2026-11-23_n-campaign_spec.md; spec-gt = results/raw/2026-11-21_n-gtime_spec.md; bench = results/raw/2026-11-21_n-gtime-v1_gread-bench.txt; campST = results/raw/2026-11-23_n-campaign-build_selftest.txt; closelist = results/raw/2026-11-25_n-campaign_close-names.txt

## 1. The specification as the texts state it

### 1.1 PROPOSAL-n v0.2

- **n:121, the gate itself:**
  - "computed after the campaign from the captured residuals, before VERDICTS".
  - It runs "Per axis (valence of record; `span_reward`) and dose point: an L2 logistic probe on the residual at the read position (layer 32; and the final layer)".
  - The contrast is "the +pole from the −pole where both exist, else the +pole from the shadow", "against the 24 norm-matched random directions as comparator".
  - The CV is "grouped leave-one-session-out CV", with "AUC against 200 label shuffles".
  - The bar: "**PASS iff the band median AUC ≥ .90** … and above the comparator's band".
  - Its result "enters §5 only where §0.6 says".
- **n:32 (§0.6):** a null is "*concluded, not answered* unless (i) … told positive control … PASSED and (ii) G-READ-n (§3) PASSED for that axis and dose".
- **n:48 (B3):** "§3 adds G-READ-n (the readability probe at the read position, per axis and dose, k's form and bar)".
- **n:79:** the residual is captured "at layers 32 and the final layer on every forward, for G-READ-n". A-n1:54 amends this to a band.
- **n:101:** "G-READ-n's probes CPU" (a planning value).
- **n:115:** G-ANL-n covers "G-READ-n PASS/FAIL per axis and dose", and its tuple coordinate is "G-READ-n for N1-V at d_eq {PASS, FAIL}". That gives 384 tuples, plus NOT-RUN, for 385.
- **n:130 (Blinding):** "stdout prints session index, arm, dose, the fidelity value against TAU, timing — never a margin"; "the seat's full read of the checkpoint files … follows the analyzer's output".
- **§5:**
  - n:136: "a NOT-REPLICATED under G-READ-n FAIL at d = +1 is *concluded, not answered*".
  - n:138: dose is "*answered* under G-READ-n PASS at d_eq", and its sentence carries "(AUC [a])".
  - n:140 (N2) names no G-READ-n. A-n1:64 adds span_reward at the decision f.
  - n:142: N4 PASS licenses answered "(§0.6, with G-READ-n)".
  - n:144: N3 uses "readability".
- **n:159:**
  - Step 6 built "the probe code for G-READ-n".
  - Step 15: "G-READ-n from the captures; then analysis in a later session on the PI's word". VERDICTS reports "G-READ-n's AUCs".
- **n:161:** the entries list includes `G-READ-n`.

### 1.2 LOCK-n v1.0 (committed at 098218c; the same blob at HEAD)

- **The 18 lines that name G-READ-n or gread:** L:35, 77, 94, 111, 336, 389, 501, 823, 873, 950, 962, 973, 993, 997, 1001, 1261, 1392, 1398.
- **The bar, L:950:** "band median AUC ≥ .90 and above the largest of the comparator's 24 band medians; NOT-COMPUTED is not PASS", with the result "PASS or FAIL, entering §5 only where §0.6 says".
- **The settings, L:962–968:**
  - "grouped 10-fold CV by session (`kfold10`) on the folds of `cv_seed`, 200 label shuffles for the primary cells, the 24 random directions probed at the matched point without shuffles".
  - "the contrast the − pole at valence +1, else the shadow".
  - span_reward's comparator is "at +d_eq and +d_20".
  - "The comparator's band medians are over each random direction's 40 floor sessions against the axis's 160".
  - "Where the fits run is Code's call".
- **The seeds, L:823–825:** "`cv_seed` 20261116 and `shuffle_seed` 20260905", with `fit_lr` at "seed 7, 300 iterations, rate 0.1, l2 0.01". They are ruled as pinned by v1.0's dated note (L:314–323; ans20b:46).
- **The band, L:869:** "`capture_layers` = 33 through 63, 31 layers".
- **The captures, L:855–857.** The hash lists are L:870–877, which quote A-n3:60's OPEN 1.
- **Answered, L:973:** answered "iff N4 PASS and G-READ-n PASS for the axis and dose".
- **Time and cap:**
  - L:94–95: "9,538,600 ms = **2.650 h**, 2.769 h at the maxima; 403,620 fits … Outside the box and the cap; after the campaign".
  - L:111–114: on the laptop the fits are outside the cap, and "the sum v1.0 states is the runner's figure alone".
  - L:993 and L:997–998: the clause for fits run on the box, which does not apply here.
  - L:35 and L:77 carry the 2.650 h figure.
- **The analyzer, L:212–215:** v7 at `735da934…a7a8`, with the schema pin `1cab28df…edff`. L:217–221 lists what VERDICTS reads from the lock.
- **The package, L:1176–1182:** `06b55761…1d39`, in m's `package_sha256_of` form. Its closure of 12 files is L:1195–1208, including kprobe at `d90f9281…2b81` and discrim.
- **"PIN-n's probe readings":** the lock has no such phrase. The nearest is L:1261, "The probe's (probe.py:29–34): the contrasts and the comparator (§10's G-READ-n settings)", together with L:962–968, L:823–825 and L:869.
- **The order:** L:389 and L:1392.
- **A convention clash.** v1.0's own `L:N` means line N of v0.1's text (L:54–57). v0.1 occupies file lines 396–1453 (R:1557–1558; RESULTS.md entry "2026-11-23 — n — LOCK-n v1.0 — COMMITTED…", R:1551). drv:290–291 uses the lock's form. ans4:3 and ans24:3 use file line N at 098218c.

### 1.3 ADDENDUM-n1 (read whole)

- **A-n1:12:** the defect of capturing at the injection layer.
- **A-n1:20:** the laptop's tokenizer environment, G-DATA's venv: "Python 3.12.9, transformers 5.5.0, tokenizers 0.22.2".
- **A-n1:52 (§6.1):** the site.
- **A-n1:54 (§6.2):**
  - Captures are taken "at every decoder layer from the injection index + 1 through the last", "in float32, one array per cell per layer, hashed per layer in its cell".
  - They are "copied to the laptop with its hashes before the pod stops", and are "never committed to git".
  - "the lock pins the per-cell hash lists" is read as "the lock pins their form and the place of their record" (A-n3:69).
- **A-n1:56 (§6.3):**
  - "k's L2 logistic (`fit_lr` at seed 7, 300 iterations, rate 0.1, l2 0.01) per axis and kept point on each layer of the band".
  - "**grouped 10-fold cross-validation by session, the fold seed in the lock**".
  - "200 label shuffles for the primary cells", and "the 24 random directions probed at the matched point without shuffles".
  - "Where it runs … is Code's call, timed at G-TIME-n and counted in the cap where it runs on the box".
- **A-n1:58 (§6.4):** "PASS iff the band median AUC ≥ .90 and above the largest of the comparator's 24 band medians. No per-layer condition. NOT-COMPUTED is not PASS."
- **A-n1:64:** answered means "N4 PASS and G-READ-n PASS for the axis and dose — N1 at d = +1, dose at d_eq, N2 for `span_reward` at its decision f".
- **A-n1:74:** the sentence for the cell where G-READ-n PASSes and N4 does not, with "(AUC [a])".
- **A-n1:80, :82 and :86:** what changed; decision (n-2), the band; and the referent "`14e65d8`'s entry: the G-READ-n artifact's fields".

### 1.4 ADDENDUM-n3 and ADDENDUM-n2

- **A-n3:18 (§1.1)** is G-VEC's capture convention (position 0 left out). It does not touch the campaign's read-position captures, whose form is fixed at schema:74–89 and A-n1:54.
- **A-n3:60, OPEN 1:**
  - The form: "per cell and layer, the sha256 of the written rows, the cell file's `capture_sha256`".
  - The places of record: the committed cells, the report's `cells`, and "G-READ-n's artifact's `campaign.cells`".
  - Its "committed at step 14" is re-read as step 15 by ans24:55.
- **A-n3:60, OPEN 2:** fits on the box are counted in the cap.
- **A-n3:40:** N2 is decided at f = 0.20 iff the gate passes and 2·d_eq ≤ 1. So span_reward's cell that enters §5 is f0.20 (see also anl:999).
- **ADDENDUM-n2** names G-READ-n nowhere (a grep returned 0 lines). A-n2:40 keeps the cached path as the read of record. The captures are that path's prefill residuals; the fresh path's residuals are only hashed (schema:75–76, :86–87).

### 1.5 The seat's and the PI's raws; the fourth sitting's §3 anchors, checked at HEAD

- **ans4 §3** is at lines 29–34, items 1–6. **§5 (line 45):** "Nothing on the box is an input to G-READ-n or VERDICTS". The volume is to be kept until the artifact is committed. Routing items 2, 3 and 5 are at lines 55, 58 and 62.
- **The PI's routing item 2**, as the brief quotes it, is not committed at HEAD. The latest committed routing raw is 2026-11-24's.
- **The §3 anchors that hold:**
  - anl:6691–6693 (`lock_names` refusal);
  - L:212–215;
  - drv:235–237;
  - anl:42–46;
  - anl:6473–6474;
  - `06b55761…1d39`;
  - A-n1:58;
  - L:950;
  - schema:217–238 and :1231–1264;
  - anl:6467–6471;
  - cells:135–140;
  - ans21b:23;
  - `7d01b02`, the G-TIME-n entry;
  - ans24 §1.5 and LQ3;
  - n:161;
  - n:130;
  - rt23a item 3 (rt23a:27–31).
- **The anchors that hold only in part:**
  - probe.py:20–22 and :24–27 are docstrings. The import is at probe:41, and the layer refusal is at probe:122–124.
  - "PIN-n's probe readings" is not a phrase in the lock (see 1.2).
  - L:N holds under ans4's definition only (see 1.2).
  - **ans18c:40** (L:517 resolves the short form to …n-step4-run-pause…) is §5.3: "every git command over the tree while the campaign runs takes the `data/mf3` exclusion as well as item 3's". It names neither G-READ-n nor the laptop nor a window. spec-camp:546 glosses it the same way, and spec-camp:744 is the source of the paired citation.
- **ans24:**
  - :31 (§1.5): "G-READ-n's input layout is step 15's BUILD question: the staging folder's `data/n/ckpt/campaign/` holds the complete cells (JSON and arrays), where `load_cell` with `keep_arrays` reads them (cells:135–140), and step 15 points the probe there or declares another form in its entry".
  - :31 also says the analyzer "does not read them (anl:3160–3167)".
  - :46: "LQ3 … Ruled at §1.5".
  - :55 (CP15): the artifact's `campaign.cells` "is committed with G-READ-n's entry, on the laptop".
  - :71: "G-READ-n (step 15, on the laptop, in a battery window beside Q-F3; its command the next BUILD)".
- **ans21b:**
  - :23 (Q5): the fits run "on the laptop's CPU, outside the cap", timed by gread-bench "Q-F3's campaign beside it and the figure declared high for it".
  - :23 also gives the count: "six primary results × 31 layers × (1 + 200 shuffles) = 37,386 … calls, 373,860 fits, over 320 rows; the comparator's 24 random directions at the four matched points … = 2,976 calls, 29,760 fits, over 80 rows; 403,620 in all".
  - And: "a comparator is a property of the point — 24 directions at that norm against the shadow".
  - :70 is item 1. :80 is item 7: the battery window "Q-F3 beside and declared; one model run at a time, announced".
- **PI and seat lines on the fits:** rt21b:20, :29 and :43–44; ans21c:9 and :35 ("declared high for the campaign beside it"); rt21c:20; ans22b:30; ans23a:14–15 and :53; ans23b:15 and :30.
- **rt23a item 3, the route's form:** "its spec raw and starred readings committed for the seat's next thread before any run … [go, on the next thread's ruling before any run]".
- **The earlier rulings:**
  - ans16b:39–44 (the band; the probe; "About 404,000 fits"; the PASS rule) and ans16b:50 (the comparator for span_reward; `GREAD_LR`; "`kfold10` with its seed").
  - rt16b:26: decision (n-2), adopted.
  - ans16g:27, :29, :42 ("A G-READ-n cell not computed takes the not-readable sentence"), :48 ("an absent or not-computed G-READ-n cell not PASS") and :57.
  - ans18a:71 and ans18b:42: the fourth NOT-DETECTABLE form's clause on readability.
  - ans19b:39 and :41; ans20b:9 and :46; rt20b:21; ans15:62.

### 1.6 RESULTS.md entries (cited by heading and line)

- **"2026-11-25 — n — N-pod campaign (n)…" (R:24):**
  - R:59–60: 138 cells, each at the report's `json_sha256`.
  - R:67–70: "The 4278 capture arrays … stay in the staging folder outside the repository, `../jspace-lab-box.noindex/n/campaign-v1/` … Each is at the box's sha256 in the close list".
  - R:160–167: a tar stream "under repository paths, with the list at its root". `shasum -c` found 4417 of 4417 OK at each end.
  - R:177–179: the close list (`42682630…fe6d`, 4417 lines). Its lines read "<sha256>  <repo path>" (closelist:1–3), and arrays are named `<stem>.L<layer>.npy` (closelist:139–141).
  - R:317–319: G-READ-n is next, "its command the next BUILD".
- **The G-TIME-n run, "2026-11-21 — n — G-TIME-n's run of record…" (R:4210):**
  - R:4240–4243 quote the counts and the projection "9538599.963 ms = 2.6496111008333334 h".
  - R:4244: "under numpy 2.5.1 and python 3.12.9 on 14 CPUs, 10 calls at each shape".
  - The raw, bench:1–5, shows median times of 248.0795 ms on 320 rows and 88.676 ms on 80 rows.
- **"…G-TIME-n's BUILD…" (R:5233):** R:5262 describes gread-bench as "on the laptop, model-free, refused on a pod".
- **"2026-11-16 — n package — BUILD…" (R:11378):**
  - R:11428–11431 describe the probe code.
  - R:11435–11436: "Not built here: … G-READ-n's assembly from the campaign's cells".
  - R:11574: the comparator's medians are "conservative, and worth a line in the lock".
  - R:11583–11587 are the PINs: "G-READ-n's driver reads captures only through `cells.load_cell(..., keep_arrays=True)`", and "One `cv_seed`, the lock's, is passed to both `probe.result` and `probe.artifact`".
- **The G-ANL-n canonical run (R:6163):**
  - R:6164–6174: the battery passed 242/242 with 246 coverage ids, and the artifact is `e775cbb4…6088`.
  - R:6190–6193 give the interpreter's form.
  - R:6233–6250 give the form of the .gitignore admit.
- **"…the `verdicts` command" (R:13045):**
  - R:13057: `verdicts --campaign DIR --report FILE --lock FILE --date … [--gread FILE] …`.
  - R:13064–13066: the inputs must be committed.
  - R:13078–13079: the refusals.
  - R:13156–13159: PIN-n-25.
- **The schema's second commit (R:13388):** R:13463–13478 list the artifact's fields.
- **Schema v5 (R:12036):** R:12043–12054 cover the band, `kfold10` and `cv_seed`.
- **The LOCK-n v1.0 draft (R:2029):** R:2047–2048 and R:2077–2078 state that the fits are outside the cap (ans21b:23).
- **The campaign BUILD (R:659):** R:913–915 and R:920–921 give CP15.
- **"ADDENDUM-n1 v0.1 — COMMITTED" (R:12958):** R:12996 holds an observation recorded and never applied: "G-READ-n's shadow contrast tests the state's presence, where rule 5(f)(ii) names the sign".

## 2. Code that exists, which G-READ-n can use or must match

### 2.1 valence_core/n/probe.py (220 lines; last changed at ef105f1)

- **Constants (probe:44–49):** `AUC_BAR` 0.90, `N_SHUFFLES` 200, `K_FOLDS` 10, `CV_FORM` "kfold10", `SHUFFLE_SEED` 20260905, `CV_SEED` 20261116. All equal the lock's values.
- **Imports:** numpy; `from ..echo.probe import kfold_auc, kfold_shuffle_null` (probe:41); and schema (probe:42).
- **`contrast_rows(caps_pos, caps_neg)`** takes two maps of {session_id: [D] residual}. It returns X [2n, D] as float64, y = [1]*n + [0]*n, and groups = the session ids twice. It refuses if the two poles are not read on the same sessions (probe:52–60).
- **`layer_auc(X, y, groups, *, shuffles, seed, cv_seed)`** returns {"auc"}. With shuffles it also returns "null_p95" (the 95th percentile of the null) and "above_null", computed on the statistic's own folds (probe:63–71).
- **`band_median`** is `np.median` over the layers' AUCs (probe:74–75).
- **`verdict(axis_layers, comparator_bands)`** gives PASS iff the comparator is non-empty, the band median is ≥ .90, and the band median exceeds the comparator's maximum (probe:78–83). An empty comparator gives FAIL.
- **`result(axis, dose_label, merged, contrast, layer_data, layers, comparator_bands, *, cv_seed)`** builds one result:
  - `layer_data` must be one (X, y, groups) per layer.
  - `layer_data=None` gives NOT-COMPUTED, "a contrast's reads incomplete" (probe:86–113).
  - It computes the shuffles itself, at `N_SHUFFLES` and `SHUFFLE_SEED`.
- **`artifact(campaign_report, package_sha256, layers, results, *, cv_seed)`** builds `n-gread-v1`:
  - It refuses `layers` other than the identity's `capture_layers` (probe:122–124).
  - It copies the report's `read_plan_sha256`, its `stage_identity_sha256`, and every report cell's `json_sha256` and `capture_sha256`.
  - It runs `check_gread`, returns a dict, and writes no file (probe:116–135).
- **Nothing in the module** reads cells or builds comparator bands. The comparator is built by calling `layer_auc(shuffles=0)` per direction and layer, then `band_median`.
- **Code's PINs (probe:29–33):**
  - "per axis and dose point d > 0: +pole at d against -pole at -d where both are read (the valence axis at +1 / -1), else +pole at d against the session's shadow".
  - The COMPARATOR is "each random direction's band median on the same contrast at the same dose point (its own 40 sessions), not shuffled".
- **The self-test** (probe:138–220) has 16 checks on synthetic data.

### 2.2 k's classifier: valence_core/echo/probe.py (sha256 d90f9281…2b81) and discrim

- **`kfold_auc`** (kprobe:95–97) calls `kfold_scores` (kprobe:78–92) and then `auc_from_scores` (discrim:47–62, a Mann–Whitney AUC with ties scored 0.5, NaN if a class is empty).
- **`grouped_folds(groups, k, seed)`** (kprobe:69–75) permutes the sorted unique session ids with `default_rng(seed)` and folds them `perm[i::k]`. So every layer and every primary result shares the same folds.
- **`fit_lr`** (kprobe:22–35; constants at :19) standardizes on the fit set (sd + 1e-6), draws w from N(0, 0.01) by `default_rng(7)`, and runs 300 full-batch GD steps at rate 0.1 with l2 0.01, in float64 numpy.
- **`kfold_shuffle_null`** (kprobe:100–114) permutes y across all rows from `perm_seed` and reuses `fold_seed`'s folds.
- discrim imports `.adapters.base` (discrim:32). base imports numpy and the standard library only (valence_core/adapters/base.py:24–31). `sha16_arr` is defined at base:34–40.

### 2.3 valence_core/n/schema.py (sha256 1cab28df…edff, equal to the analyzer's pin)

- **The artifact, `n-gread-v1`** (fields at schema:1231–1264):
  - schema;
  - campaign: `read_plan_sha256`, `stage_identity_sha256`, and `cells`, a map from name to {json_sha256, capture_sha256}, where each name must be in `VALID_CELL_NAMES` (schema:1285–1296);
  - probe: `package_sha256`, `lr`, `shuffles`, `shuffle_seed`, `cv`, `cv_seed`, `layers`, `bar`;
  - results: `axis`, `dose_label`, `merged`, `contrast`, `status`, `band_median_auc`, `per_layer` as [{layer, auc, null_p95, above_null}] with `above_null == auc > null_p95` (schema:1344–1353), `comparator` as {24 band medians, max = max} or both null (schema:1354–1364), and `bar`.
- **`check_gread`** (schema:1551–1598) checks:
  - the schema name;
  - a bar of 0.90, 200 shuffles, and at least one layer;
  - `lr == GREAD_LR` {7, 300, 0.1, 0.01};
  - cv is "kfold10";
  - each (axis, point) is in `GREAD_AXES` (valence: +1, +1/2, +d_20, +d_eq; span_reward: f0.10, f0.20), with no repeat;
  - merged may hold only +d_20 or +d_eq, on valence only;
  - the contrast is "pole" exactly at valence +1, else "shadow";
  - a NOT-COMPUTED result carries no comparator, no band median and no per_layer;
  - `per_layer` is in the probe's layer order, the band median is their median, and the status matches the PASS rule.
- **What `check_gread` does not check:** the values of `cv_seed`, `shuffle_seed` and `package_sha256`, or the campaign's sha256s. The reader checks those (anl:6459–6484).
- **The docstring** (schema:217–238): "A computed result without a comparator is a FAIL". The campaign field is described as "the cells read" (schema:1240).
- **The report's `cells`** map each name to {json_sha256, capture_sha256 per layer, records} (schema:1159–1161). `check_report` holds the layers to `capture_layers` (schema:1403–1412).
- **Identity:** `capture_layers` must equal `list(range(layer + 1, n_layers))` (schema:471, :865–866). The identity's sha256 is canonical JSON (schema:1267–1271).
- **Captures (schema:74–89):** they come "From the cached path's prefill, at the read position", one float32 `.npy` per cell per layer of shape [capacity, d_model] (capacity 40 for N1-R, 160 otherwise), "row r holding the cell's r-th record". The per-layer `capture_sha256` hashes the written rows.
- **Names:** cells are `{arm}__{direction}__{slug}.json`, and arrays are "the same stem with `.L{layer}.npy`" (schema:525–537).
- **What a build may read and must not read in a record:**
  - May read (residuals and grouping): `session_id`, and `capture` {row, sha16 per layer} (schema:384, :405–408). The probe's class labels come from which cell a row is in.
  - Must not read (margins): `logprob_S/U_tokens`, `logprob_S/U`, `margin`, `restricted` (p_S, p_U, label_mass, pick), `fidelity` (fresh_margin, absdiff, scale, rel, …), and `identity` (schema:377–390, :393–430).

### 2.4 valence_core/n/cells.py

- **`load_cell(root, arm, direction_id, dose_label, identity=None, *, keep_arrays=False)`** (cells:135–174):
  - It reads `root/<cell name>` and runs `check_cell`.
  - With an identity given, it refuses a different identity.
  - For every capture layer it opens `root/<stem>.L{l}.npy` read-only, checks each record's `sha16_arr` and the sha256 of the written rows, and returns the arrays read-only if `keep_arrays` is set.
  - `root` can be any folder; the arrays sit beside the JSON (cells:78–83).
- **Hazard 1: a missing cell.** With `identity=None`, a missing cell raises FileNotFoundError. With an identity given, it returns a new, empty cell (cells:142–145).
- **Hazard 2: margins in memory.** `load_cell` parses every record into memory, margins included. Schema refusals print only the field path (`redacted`, cells:72–75).
- **The row hash forms:** `rows_sha256` (cells:90–95) and base:34–40.

### 2.5 scripts/n_sessions.py (sha256 47abe489…c21a, the BUILD e1be6d9)

- **The 45 lines that name G-READ-n or gread** cover the docstring (drv:222, 235–237, 344, 351), the constants (drv:3884–3885), gread-bench (drv:4533–4604, 4608, 4613), the self-test (drv:5084–5200) and main (drv:7686, 7755–7760). None of them is a stage. drv:351 reads "Stage G-READ-n is wired at its own step".
- **gread-bench:**
  - It takes no option (drv:7755–7759) and is "refused on a pod" (drv:4588–4589).
  - It uses synthetic float32 noise (`GREAD_BENCH_SEED` 20261122) at shapes of 320×5120 and 80×5120, timing `probe.layer_auc(..., shuffles=0, cv_seed=probe.CV_SEED)` 10 times at each shape (drv:4550–4576).
  - It prints 5 lines (drv:4592–4603) and writes nothing.
  - `gread_counts` computes 6×31×201 and 4×24×31 calls, 403,620 fits (drv:4533–4547).
- **Pins:**
  - `LOCK_SHA256` = 59e0b1bc…00aa (drv:3894), `LOCK_PACKAGE_SHA256` (drv:3903), `LOCK_CLOSURE` (drv:3904–3917), `LOCK_READ_PLAN_SHA256` (drv:3918), `LOCK_SITE` 32, and `N_LAYERS, D_MODEL = 64, 5120` (drv:696).
  - There is no analyzer pin and no `cv_seed` pin in the driver.
- **The campaign as a template** (`_camp_prepare`, drv:6554–6669):
  - `refuse_out` on the outputs;
  - the pod and cuBLAS checks;
  - the stream known answer (drv:6579–6581);
  - rulings as committed raws;
  - the STAGE, WEIGHTS and DRIVER lines (the driver must be HEAD's committed bytes, drv:6600–6605);
  - LOCK-n.md checked by `gver_lock_check` (drv:5239–5246);
  - the package and closure measured in process and held to the lock (drv:6634–6638; `_package_closure` at drv:4297–4299 imports every PRODUCTION module);
  - then the identity and the plan.
  - Exits: 0, 3, 5, 6 and 7, plus 1 (drv:6185).
- **The primitive's import guard** admits only valence_core/n/ or "a `scripts/n_*.py` driver" (primitive.py:6, 45–64). guard.py:9–10 explains why the closure is measured by the driver.
- **The self-test:** 774/774 on the laptop at e1be6d9 (campST:42–76) and 785 on the box (ans4:15).
- **Its traps for box safety:** RUNPOD_POD_ID is unset, the production loaders are replaced by raising stubs, a recorder stands in for the stage, and stage paths inside the repository are refused (drv:5084–5152, 7645–7665).

### 2.6 scripts/n_analyze.py (sha256 735da934…a7a8, v7, b6ea27f)

- **`--gread` is optional in argparse** (anl:6802). But when VERDICTS analyzes, a missing `--gread` gives "REFUSED: VERDICTS bind G-READ-n's artifact (--gread)" (anl:6720–6721). The NOT-RUN path needs none (anl:6710–6719).
- **`gread_problems`** (anl:6459–6484) checks:
  - the plan and identity sha256s are the report's;
  - the cells exactly equal `camp.cells` by both sha256s. `camp.cells` is computed from the JSONs under `--campaign` (anl:3197). This is anl:6469–6472.
  - the probe's package is the identity's (anl:6473–6474);
  - the layers are the identity's (anl:6475–6476);
  - each result is at a kept point, with `merged` equal to the dose map's.
- **`gread_states`** (anl:6487–6504) reads the statuses per point value. An absent result counts as NOT-COMPUTED (PIN-n-11, anl:498–499). The dose sentence's AUC is the band median at d_eq's kept label.
- **The lock:** its sha256 must equal the identity's `lock_sha256` (anl:6687–6689), and it must name the analyzer: `lock_names` (anl:3138–3140) is used at anl:6691–6693.
- **Committed inputs:** VERDICTS of record require the lock, the report, the G-READ-n artifact and the cosines file to be committed (anl:6625–6645, using `committed_problems` at anl:5892–5906).
- **`load_campaign` reads no array** (anl:3161–3167).
- **The battery's coverage ids:** GREAD-PASS, FAIL, NOT-COMPUTED, ENTERS-N1, ENTERS-DOSE and ENTERS-N2 (anl:1231); N2-GATE-GREAD (anl:1223); RD-GREAD and RD-GREAD-MIXED (anl:1249–1250); VD-GREAD-MIXED (anl:1257).
- **The refusal cases** gread-missing, -plan, -identity, -capture, -json, -cells-missing, -package, -layers, -merged and -not-kept are at anl:5711–5721, under VD-REFUSE (anl:5774–5791).
- The test fixture `_bt_gread_for` lists every cell of the campaign (anl:4792–4809).

### 2.7 data/n/gates/ and the .gitignore

- **G-ANL-n.json** is 462 lines of JSON, one-space indent with sorted keys, sha256 e775cbb4…6088 (equal to L:183). Its top-level keys are: addendum, addendum2, addendum3, analyzer, battery, dose_map, open, pins, proposal, schema ("n-ganl-v1"), schema_module, spec, stage ("G-ANL-n"), tuple_space, verdict ("PASS").
- **.gitignore:**
  - :261–262: "any later n artifact … needs its own line".
  - :328–330 admit `data/n/gates/G-ANL-n.json` alone.
  - :363–367 admit the campaign's `N*.json` and its two reports.
- **The artifact's file name** appears in no text or code. ans4:33 says only "under `data/n/gates/`".

### 2.8 Interpreter, libraries and determinism on the laptop

- **Interpreter of record:** G-DATA's venv, Python 3.12.9 (A-n1:20; L:589–590). numpy 2.5.1 and 14 CPUs (bench:1; R:4244).
- **The form:** `cd` into the venv's bin folder by a glob, then `nice -n 19 ./python -I -B …` with `TMPDIR` in scratch (R:6190–6193; campST:25–28), offline flags for the self-tests, and battery windows granted by the coordinating session (campST:29–34).
- **Why the form matters:** m's guard counts as a model process any python whose command line names a marker (valence_core/m/guard.py:87–95).
- **scikit-learn:** no n code imports it, and no n text names it.
- **Thread settings:** none is named for n's runs. The only `VECLIB_MAXIMUM_THREADS` is in a note-audit script (scripts/audit_note_N3_compute.py:1156), not in n's code.
- **Determinism of the probe's fits on a CPU:** no text addresses it. Only the fold assignment is stated to be deterministic (kprobe:70).

### 2.9 My checks at HEAD

- **Digests:** anl 735da934…a7a8, schema 1cab28df…edff, drv 47abe489…c21a, LOCK-n.md 59e0b1bc…00aa, kprobe d90f9281…2b81, discrim 7d171ae7…de89.
- **Last changes:** valence_core/n/ last changed at ef105f1 (L:1178 calls it "its last change"), anl at b6ea27f, and drv at e1be6d9.
- **Status:** a scoped status of these paths is clean.

## 3. What the texts leave open for a build (questions only, not decided)

Each item gives the nearest texts.

1. **The command's name and place, and its options.** Is it a driver command beside gread-bench or a script of its own? A script must be named `scripts/n_*.py` if it imports the primitive (primitive.py:6). What options does it take: the staging root, the artifact's path, `--out`, a self-test? Nearest texts: ans4:29, ans24:31, R:6164–6166.
2. **How the arrays are bound.** By `load_cell`'s row hashes alone (R:11583–11585; ans4:32)? Also by checking each staging JSON against the committed report's `json_sha256`, which VERDICTS binds to the repository's JSONs (anl:6469–6472)? Also by the close list's file sha256s, and by whom? Which report does the run read, the committed one or the staging copy (closelist:1)?
3. **Does `load_cell` take `identity=`?** If it does, a missing cell comes back as a new, empty cell (cells:142–145).
4. **Which cells are read.** Only those probed (about 104 to 128 of the 138), or every cell? The artifact lists all 138 cells (probe:128–129; anl:6461), while schema:1240 says "the cells read".
5. **Is the comparator at +1 pole or shadow?** That is, rand(+1) against rand(−1), or rand(+1) against the shadow. probe:32–33 says "the same contrast"; ans21b:23 says "against the shadow"; L:963–964 is ambiguous.
6. **What "never reads margins" means.** `load_cell` parses and schema-checks the margins in memory, while ans4:32 says "nothing of the cells' margins read or printed". What does stdout print: per-layer AUCs, band medians, comparator maxima, digests (ans4:32; n:130)?
7. **The pins and identity the command checks.** Candidates: LOCK-n.md at `LOCK_SHA256`, the driver as HEAD's committed bytes, the package and closure measured in process, `cv_seed` and `shuffle_seed` against L:823, the stream known answer, the absence of a pod id, and the report's identity. The artifact itself carries no lock, analyzer, timing or environment field (schema:1231–1251).
8. **Time.** The fits come to 403,620 at 2.650 h, while gread-bench timed calls without the I/O of reading about 5 GB through `load_cell`. Is there any checkpoint or resume inside the run, and what do a crash or a stop leave? Is the artifact written once only (as `ganl` is, anl:34–37)?
9. **Determinism and threads on a CPU beside Q-F3.** Is a BLAS thread setting required? Is a repeat-run identity check required? (No text.)
10. **The causes of NOT-COMPUTED.** The campaign is complete and its non-finite count is 0 (R:54–56), so "a contrast's reads incomplete" cannot occur. Is a non-finite residual or a missing staging cell a refusal or NOT-COMPUTED? Must all six results be present?
11. **What is committed.** The artifact's name and its .gitignore admit (.gitignore:328–330); the raws (out, self-test, survey and spec, the starred block, values-checks); the entry `G-READ-n` with its sha256 (n:161; ans4:33). What does the entry report: statuses, AUCs, durations, environment?
12. **The self-test.** What stand-ins does it use, what traps make it unable to read the staging folder or write under data/n/gates, and in what battery window does it run?
13. **Inputs.** Nothing from the box is an input (ans4:45). G-TIME-n's cells are not the campaign's (PIN-n-25). No text says this outright for G-TIME-n's cells.

## 4. What would need the seat or the PI before the run

1. **The route.** The survey and PINs, the spec raw and the starred readings committed for the seat, then the seat's ruling and the PI's go (PI item 2, "[go, on the seat's ruling before the run]"; rt23a:27–31). Then the coordinating session's battery window (ans21b:80).
2. **A conflict between texts** on the comparator's contrast at +1 (3.5 above).
3. **A reading that must come before the run:** whether `load_cell`'s parse in memory meets "nothing of the cells' margins read" (ans4:32 against R:11583).
4. **A missing input:** no text names the artifact's file name or its .gitignore line (2.7).
5. **Citations:**
   - The PINs must name which L:N convention they use (1.2).
   - ans18c:40 does not support "beside Q-F3" (1.5).
   - The observation that the shadow contrast tests presence while rule 5(f)(ii) names the sign (R:12996) was never ruled. n:121 and A-n1:56 set the contrasts, so this does not block.
6. **The volume cleanup** is the PI's word after the artifact is committed (ans4:45, :62). It does not block.

## OPEN QUESTIONS

1. Is the command in the driver beside gread-bench, or in a script of its own (named `scripts/n_*.py`)? What are its name and options (staging root, artifact path, `--out`, self-test)?
2. How are the staged arrays bound before any fit: `load_cell`'s row hashes alone, or also each staged JSON against the committed report's `json_sha256`, and the close list's file sha256s (checked by the stage's code or by `shasum -c`)? Which report is read, the committed one or the staging copy?
3. Does the run call `load_cell` with `identity=` (where a missing cell is silently empty) or with `identity=None`?
4. Are only the probed cells verified and read, or all 138? The artifact lists all 138, but schema:1240 says "the cells read".
5. At +1, is the comparator rand(+1) against rand(−1) (probe:32–33) or rand(+1) against the shadow (ans21b:23)?
6. Does `load_cell`'s parse in memory satisfy "nothing of the cells' margins read"? Exactly what does stdout print?
7. Which pins and refusals does the command hold: the lock, the driver, the package and closure, the seeds, the stream known answer, no pod, the report's identity? Where is the environment recorded, given the artifact has no field for it?
8. Is there a checkpoint or resume within the run? What do a crash or a stop leave? Is the artifact write-once?
9. Is a thread setting or a repeat-run determinism check required for the CPU fits beside Q-F3?
10. What are NOT-COMPUTED's causes beyond incomplete reads, and must all six results be present?
11. What are the artifact's file name and its .gitignore admit? Which raws are committed? What does the `G-READ-n` entry report?
12. What are the self-test's stand-ins and traps, and in what battery window does it run?
13. Should the PINs say outright that G-TIME-n's cells and anything on the box are not inputs?
14. Which convention for L:N do the PINs use: the lock's (lines of v0.1) or the seat's (lines of the file at 098218c)?
15. Does the seat want ans18c:40 re-cited, and the presence-versus-sign observation (R:12996) ruled, before the run?

## DEPARTURES

1. **One `awk`** (an interpreter the brief bars by name). It ran in a pipeline over `git grep` output of the driver's `def` lines (`awk -F: '$2 >= 3800' | head -0`). head refused its count, and nothing from that pipeline was printed.
2. **Two `sed -n 'A,Bp'` filters** of `git grep` output: anl's gread lines 101–200, and the driver's list of definitions. I declare them in case sed counts under "no interpreter of any kind".
3. **A guard marker in argv.** One `git grep -n -i -E` pattern held "ipykernel" unbracketed (and "python" twice). It searched m's guard and drivers for the process check, and the marker stood in the zsh -c string and in git's argv. Neither process's argv[0] was python, which is the condition in valence_core/m/guard.py:87–94.
4. **Pathspec forms other than item 3's exact form:**
   - quoted glob pathspecs, both in that same command ('valence_core/m/*.py', 'valence_core/m[f]3/*.py', 'scripts/m_*.py', 'scripts/m[f]3_*.py') and in one `git grep` over 'results/raw/2026-11-1[6-9]_*answers*' and 'results/raw/2026-11-2[0-4]_*answers*' with root documents named;
   - one `git grep -c` that named `RESULTS.md results/raw` as plain paths;
   - one `git grep` with `-- . ':!data/**'`, item 3's stricter equivalent of the brief's form.
   Their output named raws, some with marker names in mixed case (output, not argv). None of them searched under data/.

Declared for completeness, and within the rules as I read them:
- I read lines 1–3 and 139–141 of the close-list raw with the file tool. They hold names and digests only (the report, one cell JSON and four arrays).
- I took `openssl dgst -sha256` digests of six repository files and of data/n/gates/G-ANL-n.json.
- I ran scoped `git status --porcelain -- <named paths>` only; no whole-tree status.
- No python ran, no file was written, and no network was used.
- Nothing under data/*/ckpt, data/*/reports or data/m[f]3 was opened, listed, sized, timed or hashed.
- Nothing outside the repository was read except the brief.
```
