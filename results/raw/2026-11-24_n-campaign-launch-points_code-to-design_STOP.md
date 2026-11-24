# n — the N-pod campaign's launch set v1: six points and the INTEGRITY readings, for the seat with the eight starred readings (code → design)

*The n-build session (Code), PI date 2026-11-24. For the seat's next sitting, to be read with the eight starred
readings (`fcab1e5`'s block) before the N-pod campaign's run (n §8 step 14). The push of the commit that carries it
waits for the PI's word, and the PI then nudges the seat.*

*Where things stand:*
- *The campaign's BUILD is `e1be6d9`, on origin. Its run waits for the seat's ruling on the eight and the PI's word,
  then the coordinating session's "launch cleared" (rt23a item 3: "[go, on the next thread's ruling before any
  run]").*
- *Code's launch set v1 went to the coordinating session first, on 2026-11-24. The coordinating session read it
  whole and checked it by tool; at its word the set stays frozen as sent. Nothing has gone to the box, and nothing
  ran on a model.*
- *The set's note carried six points and Code's INTEGRITY readings. The coordinating session asked the PI how they
  reach the seat before its ruling; the PI's answer, relayed verbatim, was "Commit a raw". This is that raw. It
  carries the six points and the readings, both sides, as the set's note gives them, stated more exactly from the
  set's own files where the note was short (points 1, 3 and 4, and G-VER's readings), with the texts each rests on,
  because the set itself is outside the repository.*
- *Each point is put to the seat, not ruled. Point 2 bears on CP6, one of the eight (the eight's Q2).*

*The set, outside the repository, by sha256:*
- *for the box, side by side in one folder: the launch script `camp_v1.sh` (`16485a25…58f5`, 939 lines), in four
  modes, `start`, `resume`, `pistop` and `names`, which checks its three siblings by sha256 as its first step, after
  its argument checks and the new work folder: the manifest `camp_manifest_v1.txt` (`de1f52c1…be71`, 66 lines: the
  files the box's copy must hold, each at `e1be6d9`'s blob), `camp_hashes_v1.txt` (`a853932b…522b`, 13 lines: the
  driver's `hashes` at `e1be6d9`, the package's digest and its closure's files, G-TIME-n's and G-VER's file byte for
  byte) and the plan `camp_plan_v1.txt` (`551eb1bf…a658`, 7,680 lines, one line a read);*
- *the pod session's note, `camp_launch_note_v1.md` (`42b3efd0…bb14`, 302 lines);*
- *for the laptop, Code's close placement, `camp_place_v1.sh` (`2127906a…9ce7`, 136 lines);*
- *the blind launch review's report (`de0604cf…dc7c`) and Code's dispositions of it (`fb36e13f…223c`). Its findings
  are cited by number as the launch review's (F, B and O); the BUILD review is the raw committed with the BUILD,
  `results/raw/2026-11-23_n-campaign-build_review.md`;*
- *the set's note to the coordinating session (`ba220eab…a7d7`, 226 lines), whose points and readings follow.*

*Cited forms:*
- *blk: is `results/raw/2026-11-23_n-campaign-starred-eight_code-to-design_STOP.md`, the eight's block, and spec: is
  `results/raw/2026-11-23_n-campaign_spec.md`, both committed at `fcab1e5`;*
- *ans22b: is `results/raw/2026-11-22_n-gver-record-read_design-to-code_answers.md`; ans23b: is
  `results/raw/2026-11-23_n-lock-v1_0-committed-close_design-to-code_answers.md`; gvrun: is
  `results/raw/2026-11-22_n-gver-v2_run.txt`; rt23a: is `results/raw/2026-11-23_first-sitting_pi-routing.md`;*
- *R: is `RESULTS.md` at `e1be6d9`; drv: is `scripts/n_sessions.py`, anl: is `scripts/n_analyze.py` and runner: is
  `valence_core/n/runner.py`, each at `e1be6d9`; n:line is PROPOSAL-n v0.2's line; A-n3:line is ADDENDUM-n3's line;
  `LOCK-n.md:N` is a line of the file at `098218c`.*

*Code reads and asks. Every reading below is Code's, and the seat rules each one; Code adjudicates none.*

## 0. The short form

- **Six points,** each with what the set does, the texts it rests on, and what another answer would change:
  1. a resume, or the PI's stop, runs in a fresh copy at a later commit, and one version of the script checks it;
  2. CP6's three fields of the report are printed by the launch's own Python check, not by `jq`, with counts and
     each check's verdict beside them (the launch review's O3(2));
  3. the close's copy-back lands outside the repository, and the arrays stay there (CP10; the launch review's F10);
  4. a resume after a crash is not built: its route is the seat's, and a new launch version (F11);
  5. CP13's no-restart check is the pod session's own, before each invocation, in G-VER v2's form;
  6. an excerpt's words are the driver's, to the seat verbatim; the launch holds its form and count.
- **None changes the driver.** Points 1–5 bind the launch files and the sessions; point 6 binds what the launch
  checks of a pause (CP8).
- **The INTEGRITY readings** (§2): beyond what ans22b §1.4 ruled and CP12 extends, five readings of the campaign's own
  on the safer side, and two that go the other way.
- **The questions** are LQ1–LQ8 in §3: one per point, and two on the readings.

## 1. The six points

**Point 1 — a resume, or the PI's stop, runs in a fresh copy at a later commit.**
- *The set:* a resume after a PAUSE runs in a fresh sparse copy at the commit that holds the seat's ruling, and the
  PI's stop at the commit that holds the PI's raw; the coordinating session names it. The copy is a fresh clone that
  holds the history back to the BUILD, neither shallow nor a worktree, so that the ancestor check below can see the
  BUILD (the note's box step 4). The script takes that commit as an argument and checks, before the stage runs:
  - the copy's HEAD is that commit;
  - the BUILD `e1be6d9` is an ancestor of HEAD;
  - the driver at HEAD is the BUILD's blob;
  - the manifest's 66 files are at the BUILD's bytes (a file off them is INTEGRITY, a missing one a FAIL);
  - the ruling, or the PI's raw, is a file at HEAD's committed bytes.

  So one version of the script serves every resume. The cells and arrays the paused invocation wrote are then copied
  in from its copy by name, each checked by sha256 at both ends and the cells against the report (the BUILD review's
  B4).
- *The texts:* the stage takes each `--ruling` as a repository file at HEAD's committed bytes and runs only HEAD's
  committed driver (R:47, :49); a ruling is a committed raw, and the resume runs in a fresh sparse copy at its commit
  (CP8, blk:153–162); the PI's stop cites a committed raw (CP9 (c), blk:189–192).
- *Another answer:* a new launch version for each resume, its commit pinned in the script as the start's is. That
  changes the launch files alone.

**Point 2 — CP6's "by `jq`": the launch's own Python check prints the three fields.**
- *CP6 as starred:* "The launch files print the report's three fields by `jq` between invocations, and nothing else
  of it." (blk:120–121). The three are the report's end state, its standing pause, and the cap's `used_ms`.
- *The set:* Code does not know that the box has `jq`, so the three fields are printed by the launch's own Python
  check of the report, a part of the script run with the box's python (`camp_v1.sh`:299–509, its bytes
  `505f373a…1ae6`, tested in the two battery windows the coordinating session granted). Each time it checks the
  report, it prints three lines and nothing else of the report:
  - "the report (CP6's three fields): end state …; the standing pause …; the cap's used_ms … of …": the three
    fields, with the standing pause's kind beside its id and the cap's `hour_cap_ms` beside `used_ms`;
  - counts: the cells the report names, each checked by name at its `json_sha256` ("held" or "NOT held"), their
    arrays by name, and the records in the cells;
  - each check's verdict by its name ("… holds" or "… FAILS"): the identity line, the cells by name and digest, no
    record lost, and the like.

  When the report cannot be read as declared, it prints one line naming the exception's type instead. The counts
  and verdicts are the launch review's O3(2): none is a field of the report, and none is a margin.
  - The check runs after an invocation that ends COMPLETE, PAUSE or CAP, at the start's G-VER STOP, or at the PI's
    stop; not after a resume's G-VER STOP, a refusal or a failure. At a resume and the PI's stop it runs also on the
    copied-in report before the stage, so its lines print twice and the pod session reports the second CP6 line. It
    runs once more at the close, in `names`.
  - It also writes two counts, the reads obtained and the cells named, to a work file the script reads: at a resume,
    for where the per-read lines start; at each end, for whether the cells' folder is listed. At a resume, that work
    file for the copied-in report (`prior.txt`) is among the files copied back.
  - Run in its names mode at a resume, the PI's stop and the close, it writes the names of the cells the report names
    and of their arrays to a work file (`names.txt`, by camp_copy_names's rule), for the copy-in and the close's
    list; the script prints their counts alone. At a resume and the PI's stop that file is among the files copied
    back: names, and no margin, but more of the report than the three fields.
- *The texts:* n:130 ("Margins go to checkpoint files; stdout prints session index, arm, dose, the fidelity value
  against TAU, timing — never a margin"); the list of record's items 2 and 5; CP6 (blk:103–124).
- *Another answer:* the three fields alone, the check's other prints removed; or `jq`, on the pod session's word that
  the box has it. Either is a new launch version, with no code change.

**Point 3 — the close's copy-back lands outside the repository, and the arrays stay there.**
- *The set:* after the last invocation, `names` writes the close's list on the box: the report, G-VER's record if
  there is one, and each cell the report names with its 31 arrays, each hashed by name. The copy-back copies by that
  list alone into the laptop's `../jspace-lab-box.noindex/n/campaign-v1/` (from the repository's root; new), under
  repository paths, and it is checked there by `shasum -a 256 -c`.
  - The arrays stay there, outside the repository, beside G-TIME-n's (its copy-back's folder in the same staging
    folder), where G-READ-n reads them (step 15, on the laptop; Code's reading).
  - Code's placement script copies only the JSONs into the repository, each checked there. The close's one commit
    carries them, G-TIME-n's two steered cells, and the raws, the close's list verbatim among them (every file's
    sha256, the arrays' included).
- *Changed with the launch review's F10:* the reviewed draft of the placement script copied every file, the arrays'
  ~4.9–5.0 GB (LOCK-n.md:92–93) among them, into the repository's `data/n/ckpt/campaign/`, where the BUILD's
  `.gitignore` ignores the arrays, after the BUILD review's B8. CP10 as sent reads "On the laptop the arrays are held
  outside the repository, beside G-TIME-n's" (spec:192), and it governs. That also spares a second ~5 GB copy.
- *The texts:* CP10 (spec:186–193); CP11 (blk:207–231). The analyzer takes a campaign's folder as its argument
  (anl:3161), refuses a file beside the cells that no cell names (anl:3199–3203), and binds the arrays by their
  cells' row hashes without reading them: "an absent array is no refusal" (anl:3167).
- *Another answer:* the arrays copied into the repository's campaign root as well, ignored there, a second ~5 GB
  copy. That changes the placement script alone.

**Point 4 — a resume after a crash is not built.**
- *The set:* a crash (an invocation killed, or the container restarted mid-run) leaves the records written before it
  on disk, and the runner replays them at a resume (runner:12–15). These launch files cannot carry them into one:
  - after a crash at the start, no report exists, and a resume's copy-in ends FAIL ("no report");
  - after a crash in a resume that moved a cell the copied-in report names, the copy-in's check ends INTEGRITY ("a
    cell of the run copy off the report", §2);
  - a crashed resume that wrote only cells the report does not name leaves the report and its cells as they were.
    The copy-in's checks then pass, the script would accept a second resume on the same ruling, and the crashed
    invocation's new cells would stay behind in its copy. The note's word below is then the only barrier.

  The note routes a crash to the seat and a new launch version: "these files cannot resume after it"
  (`camp_launch_note_v1.md`:203). The pod session stops every process of the launch and confirms that no
  `n_sessions.py` remains, and the end goes to the seat and the PI. Where the driver itself ends an invocation as
  failed after G-VER (exit 1), the script's line says so too: "these files cannot resume after a crash (a new launch
  version, the seat's route)", beside the driver's "the records on disk replay at a resume" (drv:6767). A kill or a
  restart ends the script itself, and the note governs it.
- *The pod session's note* gives both crashes' ends in one sentence ending "so 1b would stop INTEGRITY"
  (`camp_launch_note_v1.md`:203–205), as the set's note does. Since it routes a crash to a new launch version, step
  1b does not run after one under v1, and the sentence changes nothing the pod session does.
- *The texts:* CP12 (blk:232–257: exit 1 for a refusal or a crash; "A crash leaves the cells replayable
  (runner:12–15)"); A-n3:60: "a crashed invocation's absent load is a declared reporting gap"; the launch review's
  F11.
- *Another answer:* a resume after a crash built before the run: a launch version that copies in the cells as the
  crashed invocation left them, under a rule the seat states for their records. That changes the launch files, and
  the seat's rule may reach the driver.

**Point 5 — CP13's no-restart check is the pod session's own.**
- *The set:* before each invocation, the pod session checks the box read-only, in G-VER v2's form (gvrun:42–63):
  - the same pod id;
  - no restart since the last launch on this box: the container's first process older than that launch, by two
    durations compared, with no box file's time read;
  - the volume as left; the new names free; `/tmp` on the local disk; the GPU idle, with no `n_sessions.py` process.

  A restart or a box change stops everything: the pod session reports it, and nothing runs until the seat and the PI
  rule. The script does not check for a restart itself; the driver's pod pin refuses another pod before any read
  (exit 1).
- *The texts:* CP13 (blk:258–280) and the eight's Q7; the respawn protocol (CLAUDE.md): "Both PASS before anything
  runs".
- *Another answer:* the check inside the script, a new launch version; or, by the seat's answer to Q7, a restart on
  the same pod allowed to resume once the respawn protocol's two steps pass.

**Point 6 — an excerpt's words are the driver's.**
- *The set:* at a PAUSE the stage prints one EXCERPT line for the one standing pause. The launch holds the excerpt's
  form and count: one EXCERPT line, naming the standing pause by its id in the driver's form (a monitor's kind, or
  "unavailable" when the excerpt cannot be formed), and, by the Python check, the binomial or rendering line the
  pause's record needs. It does not check the excerpt's words. Code builds the pause's raw for the seat from the out
  file's EXCERPT lines and the paused invocation's lines around them, verbatim.
- *The texts:* CP8 (blk:125–171) and the eight's Q3; ans23b:27: "Every pause comes to the seat on the excerpt, in its
  own raw"; the launch review's O3(6).
- *Another answer:* the words checked as well, against a form per pause kind. That is a new launch version.

## 2. The INTEGRITY readings

The launch's last line names each end, and its exit is the stage's, with INTEGRITY 4: "stop, touch nothing on the
box, escalate at once" (the respawn protocol; ans22b §1.4). Every other refusal is a FAIL of the launch (exit 1),
reported verbatim, with no retry.

- **Ruled, and carried.** ans22b §1.4 accepted G-VER's launch readings: MANIFEST.json's (i)–(iii) part not the base
  its `iv` block names; a file of the copy off the commit's bytes after a clean checkout (a missing one a FAIL); an
  exception whose traceback names `check_weights_folder` or `gver_hashed_files`; and Code's reading in G-VER's BUILD
  entry, that a missing or symlinked one of the eight non-shard files, the weights folder's listing and byte counts,
  and the ids' sha256 and count are of the INTEGRITY kind. It corrected one: the weights folder missing on the box of
  record is INTEGRITY. The set carries each. CP12's extension to the campaign (the model manifest, the lock, G-VEC's
  and G-CAL-n's files, the package and its closure, a direction's sha16) is before the seat as the eight's Q6.
- **The campaign's own, on the safer side** (Code's readings; each only stops the launch and escalates):
  1. a file copied in at a resume or the PI's stop (a cell or an array the report names) missing from the run copy,
     or off the run copy's bytes after the copy;
  2. a cell of the run copy off the report's `json_sha256`;
  3. an exception inside a cell's checks, a traceback whose frame is `load_cell`;
  4. the cells module's own refusals, before the load or after it: a cell unreadable; an array missing, unreadable,
     or of another shape (the launch review's F1, a BUG in its reviewed draft);
  5. the G-VEC texts the stage reaches first, `gcal_gvec_inputs`'s: G-VEC's record absent or not HEAD's committed
     bytes; a G-VEC file absent, not HEAD's committed bytes or not the record's; a row not the record's of_record
     one, the gate's row included (the launch review's F2).
- **Two the other way:**
  1. a G-VEC record that fails to parse after its bytes are verified is a FAIL: the bytes are HEAD's, so the defect
     is the code's (F2);
  2. a `hashes` mismatch at the launch's step 3 is the launch's FAIL, where the launch would class the stage's own
     refusal of the package or its closure off its pin INTEGRITY (CP12's extension; the launch review's O7). Either
     way it stops before any load.

## 3. The questions for the seat

- **LQ1 (point 1).** May a resume, and the PI's stop, run in a fresh copy at the commit that holds the ruling or the
  PI's raw, under the one launch version and its checks? Or does each resume take a launch version of its own, its
  commit pinned?
- **LQ2 (point 2; CP6).** Is the Python check's print in CP6's place within "no looks": the three fields (with the
  pause's kind and the cap's `hour_cap_ms`), the counts and each check's verdict by name, at the ends where it runs,
  at a resume's copy-in and at the close; and the names file copied back at a resume? Or the three fields alone, or
  `jq`?
- **LQ3 (point 3; CP10).** Do the arrays stay in the laptop's staging folder outside the repository, with only the
  JSONs placed in the repository and every file's sha256 in the close's raw?
- **LQ4 (point 4).** After a crash, is the route a new launch version on the seat's ruling, as the set has it, or is
  a resume after a crash to be built before the run? What is a crashed invocation's record? Must no resume follow a
  crash, whatever the copy-in's checks show? Does the pod session's note, which gives both crashes' ends as
  INTEGRITY, need a v2?
- **LQ5 (point 5; CP13).** Is the no-restart check the pod session's own, before each invocation, in G-VER v2's form,
  with a restart stopping everything until the seat and the PI rule (with the eight's Q7)?
- **LQ6 (point 6; CP8).** Does the launch hold an excerpt's form and count alone, its words going to the seat
  verbatim?
- **LQ7 (the safer side).** Are the campaign's five readings in §2 of the INTEGRITY kind?
- **LQ8 (the other way).** Is a G-VEC record that fails to parse after its bytes are verified a FAIL, and a `hashes`
  mismatch at step 3 the launch's FAIL rather than INTEGRITY?
