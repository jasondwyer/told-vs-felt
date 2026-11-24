# n — eight starred readings for the seat before the N-pod campaign's run: CP2, CP6, CP8, CP9, CP11, CP12, CP13 and CP16 (code → design)

*The n-build session (Code), PI date 2026-11-23. For the seat's next sitting, before the N-pod campaign's run (n §8
step 14; ans23b:68). The PI's word governs only the nudge to the seat.*

*Where things stand:*
- *LOCK-n v1.0 is committed at `098218c`, sha256 `59e0b1bc…00aa`, "the lock the N-pod campaign follows" (LOCK:3–4),
  and is on origin. The seat's previous thread read v1.0's draft (ans23a) and handed off (ans22b:31; rt23a:37–38).*
- *The seat's new thread accepted v1.0 as committed (ans23b §1) and named the lines the starred readings will be
  ruled against (its §2, ans23b:24–31). Its routing item N.2, "§2's eight points carried into the PINs", routed by
  the PI's "Route as given" (rt23b), is answered by Code's addendum to the readings, the spec raw's §3.*
- *The campaign has no stage command: "Stages the campaign and G-READ-n are wired at their own steps." (drv:285).
  The driver's pin of the lock's sha256, `LOCK_SHA256`, is still LOCK-n v0.1's (drv:3820), so `gtime` and `gver`
  refuse at this HEAD until the BUILD moves it (LOCK:356–361), and the self-test fails on the same checks (drv:4562,
  :5549).*
- *A read-only survey of the texts at `098218c` returned 19 open questions. Code's readings CP1–CP20 answer them as
  PINs.*
- *The PI's answer, relayed verbatim by the coordinating session on 2026-11-23, was "Build on the PINs". So the build
  goes ahead on CP1–CP20 as PINs, in the driver alone (CP1).*
- *The eight starred readings go to the seat before the run, not before the build: rt23a item 3's
  "[go, on the next thread's ruling before any run]" (rt23a:27–31). That is G-TIME-n's and G-VER's order: their
  blocks, `2ca24e8` and `d92500b`, went in before their BUILDs, `91f0d35` and `2834c2d`.*

*Sources, by sha256 or commit:*
- *The campaign's spec raw, `results/raw/2026-11-23_n-campaign_spec.md`, committed with this block:*
  - *§1, Code's readings CP1–CP20 as sent (`fd80cf43…23b0`, 190 lines);*
  - *§2, the coordinating session's routing of them, with the PI's answer;*
  - *§3, Code's addendum to the readings, the seat's eight points set against them (`e8171ce0…dd75`, 39 lines);*
  - *§4, the survey's brief;*
  - *§5, the survey's report (`7f728f96…43d1`, 342 lines, compiled at `098218c`).*
- *The texts: PROPOSAL-n v0.2 (`PROPOSAL-n-bk-reconciliation-v0_2.md`, cited n:line); LOCK-n v1.0 (`LOCK-n.md`, cited
  LOCK:line, the file's line: v1.0's part is lines 1–395, with v0.1's text beneath it); ADDENDUM-n3 (A-n3:line);
  PROPOSAL-m v1.11 (`PROPOSAL-m-gating-campaign-v1_11.md`, cited m:line).*

*Cited forms:*
- *ans18c: is `results/raw/2026-11-18_n-step4-run-pause_design-to-code_answers.md`;*
- *ans21b: is `results/raw/2026-11-21_n-gtime-starred-seven_design-to-code_answers.md`;*
- *ans21c: is `results/raw/2026-11-21_n-gtime-record-read_design-to-code_answers.md`;*
- *ans22a: is `results/raw/2026-11-22_n-gver-starred-seven_design-to-code_answers.md`;*
- *ans22b: is `results/raw/2026-11-22_n-gver-record-read_design-to-code_answers.md`;*
- *ans23a: is `results/raw/2026-11-23_n-lock-v1_0-read_design-to-code_answers.md`;*
- *rt21b: is `results/raw/2026-11-21_second-sitting_pi-routing.md`;*
- *ans23b: is `results/raw/2026-11-23_n-lock-v1_0-committed-close_design-to-code_answers.md` (the seat's second
  sitting of 2026-11-23, committed at `c26b117`);*
- *rt23a: is `results/raw/2026-11-23_first-sitting_pi-routing.md`;*
- *rt23b: is `results/raw/2026-11-23_second-sitting_pi-routing.md`, the PI's routing of ans23b (committed at
  `c26b117`);*
- *mF3ans: is `results/raw/2026-11-15_lock-m-f3-v1_design-to-code_answers.md`;*
- *gvrun: is `results/raw/2026-11-22_n-gver-v2_run.txt`;*
- *R: is `RESULTS.md` at `098218c`; its line anchors move with every entry (this block's parent is `c26b117`);*
- *drv: is `scripts/n_sessions.py`, anl: is `scripts/n_analyze.py`, and runner:, schema: and ids: are the modules of
  that name under `valence_core/n/`. Every code file:line is at `098218c`: the driver's last change is `2834c2d`,
  and the package's is `ef105f1`.*

*Code reads, builds and asks. Every reading below is Code's, and the seat rules each one; Code adjudicates none.*

## 0. The short form

- **Eight readings.** Each comes with its texts, what Code will build, and what another answer would change.
- **They are ruled before the campaign's run, not before its build** (rt23a:27–31). None needs a run to be ruled.
  - Three shape the driver: CP9 (who writes the two STOP reports, and in what form), CP12 (the exit codes the launch
    reads each end by) and CP8 (the excerpt the driver prints at a pause).
  - Three bind the launch files and the sessions while the campaign runs: CP2 (no smoke), CP6 (what "no looks" bars
    between invocations) and CP13 (a pod restart, a box change).
  - Two bind the close: CP11 (its order, and the hash check of G-TIME-n's two steered cells) and CP16 (no push
    before VERDICTS).
- **One correction of Code's own, in CP8:** CP8 as sent gives a rendering pause's excerpt "the first differing
  position and its two token ids". The package never quotes a token id in a problem line (ids:688), so the block
  gives that pause by digest. The seat rules on it with Q3.
- **The dependencies.** The campaign's run waits for:
  - the seat's answers on the eight (rt23a item 3);
  - the BUILD's commit;
  - the launch files, relayed to the box by the coordinating session after its "launch cleared";
  - the box itself, up through the campaign ("[stays up]", rt23a:39).
- **The questions** are Q1–Q8 in §3, one per reading.

## 1. The eight (to be built on them as PINs)

**CP2 — a smoke before the run (the survey's open question 1).**
- *Code's reading:* none. The campaign's first invocation is the run of record. Before its first read, the path is
  checked by:
  - the box self-test, its temporary folder on the box's local disk (CP19; ans22b:22 (i));
  - the refusals before the load: the pod, the weights of record, the driver of record, the lock and its inputs, the
    package and its closure, and the 28 directions rebuilt and held to their pins (CP3, CP4);
  - the start's G-VER, in G-VER of record's form (CP7);
  - the runner's own refusals before its first launch (runner:397–410).

  A refusal before the load is a FAIL of the launch, Code's to fix, or INTEGRITY, by CP12's classes.
- *The texts:*
  - n:97: "No optional stopping: every arm runs its full read set; there are no looks."; n:159's step 14: "The N-pod
    campaign within one pod session (all arms, no looks), raws and checkpoints committed before the pod stops.";
  - G-TIME-n had a smoke, and its two ends were ruled (ans21b:39). G-VER of record had none: "No option and no smoke
    (GV8)" (drv:260);
  - a smoke's steered reads would be reads of the campaign's own sessions outside the campaign, as G-TIME-n's two
    steered cells are: "on this backend are the campaign's own reads of those cells" (ans21b:29). Those two are held
    outside the repository until step 14's close, by a ruling of their own (ans21b §1.8; rt21b item 2).
- *As Code will build it:* `campaign` takes no `--smoke` and no `--out`; it writes only its root and its report, and
  at a G-VER STOP at the start G-VER's record beside the report (CP1, CP9 (a), CP10).
- *Another answer:* a smoke of what the seat names (a shadow-only read set, which injects nothing, say), in a root
  outside the repository, with its cells' handling ruled before it runs. That adds a smoke and its folder to the
  driver before the launch files, and a step to the launch.

**CP6 — "all arms, no looks" while it runs (the survey's open question 5).**
- *Code's reading:* the order is the runner's ORDER PIN, "the shadows first, then arm-major in `schema.ARMS` order"
  (LOCK:1252). No session reads a margin before the campaign's last invocation has ended and its cells are
  committed:
  - the driver's stdout is n:130's, the runner's line per read (runner:475, :509–511): the read's index, the session,
    the arm, the direction and the dose, the fidelity value against TAU, and the time; never a margin. The end-wait is
    on the PID alone (the list of record's item 5);
  - between invocations, the report (the read domain, item 2; it holds no margin) is read for three things only, in
    every session: its end state, its standing pause, and the cap's `used_ms`;
  - the cells and arrays are checked by name and digest alone (ans22b:22 (ii)); the copy-back prints digests and
    counts, never content.
- *The texts:*
  - n:97 (above), and n:148: "No looks (§2.5).";
  - n:130: "the blinding question is who sees margins before VERDICTS: nobody. Margins go to checkpoint files; stdout
    prints session index, arm, dose, the fidelity value against TAU, timing — never a margin";
  - the list of record's items 2 and 5;
  - beyond these, no text says what "no looks" bars while the campaign runs (the survey's 3.5).
- *As Code will build it:* nothing new in the driver for the reads: the runner's line holds no margin. The launch
  files print the report's three fields by `jq` between invocations, and nothing else of it.
- *Another answer:* a narrower read (the end state alone, by the exit and the last line) or a wider one (more of the
  report's fields, none of which holds a margin). Either changes the launch files and no code.

**CP8 — the pauses, and "the excerpt" (the survey's open question 6).**
- *Code's reading:*
  - **A pause.** A fired monitor ends the invocation for every arm (LOCK:933–934): end state PAUSE, exit 3 (CP12),
    and the report carrying the pause's record: its id, kind, read id and launch index, `arms_in_scope`,
    `also_fired`, and the binomial's batch where it has one (schema:1169–1184).
  - **The excerpt.** ans22b:32 and ans23a:53 send the campaign's pauses "to the seat on the excerpt". m's form is a
    confined adjudication read: "An adjudication read (§4 exception (1)) is confined to the fired round(s) and the
    harness lines around them" (m:271's last sentence; m:318's exception (1)), kept in a file beside the checkpoint
    ("The confined adjudication excerpt beside a checkpoint (m:271)", `valence_core/m/stages.py`:272). The word
    "excerpt" is not in m's text; the survey's "m:330" is corrected in CP8 as sent. n generates nothing in the
    campaign (n:16), so there is no fired round. Code reads n's excerpt as three parts, none of them a margin
    (n:130):
    - the pause's record, from the report;
    - the paused read's stdout lines, which the run's raw already holds;
    - the monitor's figure against its bar: for a binomial fire, k of n above TAU in the tile against p0 at alpha
      (the pause's record); for a ceiling or the identity bound, the paused read's `absdiff`, |margin − fresh
      margin|, against C = 0.25 (its record; schema:416, :428); for a non-finite number, which path was not finite;
      and for a rendering pause, whose read was not launched and has no record, the mismatch by digest, the read's
      sequence derived as the runner derives it (runner:470–479): for an untold read, the session's `ids_sha` against
      BK's, as the runner tests it; for N4-T and N4-Ts, the told or sham sequence's `ids_sha` as found now, since the
      runner tests those by the renderer alone; or the renderer's own message in the package's masked form
      (ids:148–151: its token ids masked); never a token id (Code's correction, above).
  - **No conditional rulings in advance** unless the seat issues them (the precedent:
    `results/raw/2026-11-18_n-step4-bext2-p01_conditional-ruling.md`, a ruling raw given before `backend-ext-2`
    ran). The chance of at least one false pause over the campaign is 0.3827 (LOCK:1070–1074).
  - **Each excerpt in its own raw** (ans23b:27: "Every pause comes to the seat on the excerpt, in its own raw"; the
    spec raw's §3, point 4): each pause's excerpt, the driver's EXCERPT lines with the paused invocation's lines
    around them, is committed as a raw of its own, one for each pause, for the seat's ruling.
  - **The ruling's route:** the seat's raw committed by path in a window; the resume in a fresh sparse copy at that
    commit, with the run's report, cells and arrays copied in by name and checked by sha256 (R:7842–7847's form);
    `campaign --resume --ruling <pause id>=<the raw>`. The runner records the raw's sha256 (runner:420–421). Each
    resume costs one load and one G-VER (ans21c:33).
- *The texts:* ans22b:32; ans23a:53; ans23b:27; m:271; m:318; `valence_core/m/stages.py`:272–278; n:16; n:130;
  n:148: "Every pause STOPs the arm's launches until adjudicated; Code never self-adjudicates"; LOCK:933–934;
  LOCK:1070–1074; runner:418–428.
- *As Code will build it:* `--resume` with `--ruling PAUSE_ID=PATH`, since the runner needs a ruling for each
  standing pause (runner:418–428); the driver refuses a ruling that is not a repository file at HEAD's committed
  bytes, the route's committed raw. At a PAUSE the driver prints the excerpt's first and third parts after the
  runner's lines, the third read by the stage's own code from the paused read's record (item 2). Where an excerpt
  cannot be formed (a cell the stage's code refuses, say), the driver prints one line naming the pause and the
  error's kind, and the exit stays 3, with the runner's report. No excerpt file.
- *Another answer:* the excerpt as a file, written by the driver at a pause. m keeps its file beside the checkpoint
  (`valence_core/m/stages.py`:272–278); here it would sit under `data/n/reports/`, since the analyzer refuses a file
  beside the cells that no cell names (anl:3199–3203). Or a narrower or a wider content, or conditional rulings before
  the run. A file adds code to the driver before the launch files; the others change what the launch files carry to
  the seat.

**CP9 — the STOP reports, and the PI's stop (the survey's open question 7).**
- *Code's reading:* the runner writes no STOP (its report's `"stop": None`, runner:363), and "nothing resumes after a
  STOP" (runner:331). So the driver writes the campaign's STOP forms:
  - **(a) the start's G-VER STOP.** The driver writes G-VER's record (`n-gver-v1`),
    `data/n/reports/campaign_gver_stop.json`, and the campaign's report in the schema's G-VER-STOP form: no pause, no
    record, `rendering_mismatches` G-VER's failed checks counted from its record (at least one; a session whose ids
    fail counts once, since `verify` checks it no further), and the stop record {kind, `record_sha256` that file's,
    `detail` of at most 200 characters} (schema:1195–1199, :1533–1537). G-VER's record is checked by the driver's
    `check_gver` and the report by the schema, each before its write and read back after it, so that the analyzer's
    `no-arm:gver-stop` has its input (anl:6710–6719). The two stand together: if the report's write fails, the
    record is removed and the invocation fails, exit 1. No weights load and no read follows: "no read is launched and
    the campaign does not start" (LOCK:938).
  - **(b) a G-VER STOP at a resume,** after reads exist, cannot take that form: the schema allows no record in a
    G-VER-STOP report (schema:1533–1537). The resume ends before its load, with G-VER's record printed whole, as at
    G-TIME-n (drv:4345–4346); the campaign's report stays as the last invocation left it; it is a STOP for the seat
    (LOCK:938). A MANIFEST.json off its pin reaches this STOP at a resume as at the start: the identity's
    `rendering_id` is the pin, not the loaded file's sha256, which would refuse the resume as another identity.
  - **(c) the PI's stop.** `campaign --pi-stop RAW` writes end state PI-STOP, by Code's design only while a pause
    stands (the schema names that case, schema:208–210: "the PI may stop a unit whose pause stands", and asks only for
    the stop record, schema:213), the stop record citing the committed raw's sha256 (schema:1197); no load. n:134
    names "a PI stop" among NOT-RUN's causes, and nothing writes one now.
- *The texts:*
  - LOCK:938, G-VER's row: "G-VER-STOP of any of its causes (…): a STOP for the seat, never a pause and never an
    exclusion; no read is launched and the campaign does not start";
  - GV7, which stands (ans22a:39): the campaign's own G-VER runs before its load, "and its STOP is the campaign's
    `no-arm:gver-stop` cause" (`results/raw/2026-11-22_n-gver_spec.md`:136–138);
  - n:134; schema:208–210, :1195–1199, :1533–1537; runner:331, :363; anl:6710–6719;
  - G-TIME-n's G-VER STOP writes no report: "G-VER STOP: no weights load, nothing is read, no report" (drv:4348).
- *As Code will build it:* (a) and (c) in the driver, G-VER's record checked by `check_gver` and each report by the
  schema before the write, and each read back after it; at (a) the record and the report stand together; (b) as
  above. Their exits are CP12's: 6 for (a) and (b), 7 for (c).
- *Another answer:* a G-VER STOP at the start with no report, as at G-TIME-n, which leaves the analyzer's
  `no-arm:gver-stop` without its input; another form for (b); or no PI-STOP writer, which leaves n:134's "a PI stop"
  with no record. Each changes the driver before the launch files.

**CP11 — the close (the survey's open questions 9 and 10).**
- *Code's reading:* "raws and checkpoints committed before the pod stops" (n:159), in this order:
  1. the last invocation ends (COMPLETE, CAP or a STOP);
  2. the copy-back by name (CP14): the report's 138 cells, each cell's 31 arrays by `schema.capture_filename`, the
     report, G-VER's STOP record if any, and the run's stdout and exit raws; each JSON held to the report's
     `json_sha256`, and each array hashed by name on the box and again on the laptop;
  3. G-TIME-n's two steered cells are placed by name from their holding folder into `data/n/ckpt/time/`, and their
     sha256s are checked against G-TIME-n's report (`fa823370…10c0`, `63634361…9968`; LOCK:386). Code reads that
     check as the copy's own hash check, which ans21b §1.8 excepts;
  4. they are committed by path in the same commit as the campaign's cells and report (LOCK:385–388), in a window;
  5. the pod stops only after that commit is verified.
- *The tension* (the survey's 3.9): ans21b:31 bars hashing them "before the campaign's cells are committed", and
  ans21b:32 commits them "with the campaign's own cells". Any check before that commit comes before the campaign's
  cells are committed. Code reads step 3's as the exception's "copy-back's own hash check", since placing them in the
  repository is their copy.
- *The texts:* n:159; ans21b:31: "no session lists, opens or hashes them before the campaign's cells are committed,
  the copy-back's own hash check excepted"; ans21b:32: "committed by path at step 14's close, with the campaign's own
  cells and before the pod stops …, with GT11's two `.gitignore` lines and the entry citing the report's sha256s";
  rt21b:23–26; LOCK:385–388 (v1.0 §13); ans23a:44 (its §3's edit 2); m:251 and n:103 (rule 27).
- *As Code will build it:* nothing in the driver; the BUILD adds the `.gitignore` lines (CP10). Steps 2 and 3 are the
  close's script, a launch file sent to the coordinating session first; step 4 is a commit window; step 5 is the PI's
  and the pod session's.
- *Another answer:* the two cells committed with no check before the commit (their sha256s checked after it), or in
  a commit of their own after the campaign's. Either changes the close's script and no code.

**CP12 — the ends: exits and classes (the survey's open question 11).**
- *Code's reading:*
  - **The exits:** COMPLETE 0; PAUSE 3; CAP 5; G-VER's STOP 6, at the start with its report written (CP9 (a)) and at
    a resume without one (CP9 (b)); PI-STOP 7, its report written (CP9 (c)); and 1 for a refusal or a crash, any
    SystemExit a seam raises, with no message too, among them. 2 is left to Python's usage errors (argparse exits
    2), so that no end of the stage shares a code with one: the launch reads each end by three things together, the
    exit, the last line and the record on disk (ans22a:25, the supplement's F5), here the report. At a G-VER STOP at
    a resume (CP9 (b)) the exit and the last line name the STOP, while the report keeps the last invocation's end
    state by design. At a PAUSE, an excerpt that cannot be formed leaves the exit 3 (CP8).
  - **The classes,** as ruled for G-VER of record (ans22a:26–29; ans22b:24) and extended by Code to the campaign: a
    refusal on a file's hash or byte count is INTEGRITY, "stop, touch nothing, escalate" (ans22a:27). The rulings
    name the weights folder's files (the folder missing included), the eight non-shard files and the ids' files;
    Code adds the model manifest, the lock, G-VEC's and G-CAL-n's files, the package and its closure, and a
    direction's sha16. An environment or launch refusal is "a FAIL of the launch, Code's to fix" (ans22a:28). A
    crash leaves the cells replayable (runner:12–15); "a crashed invocation's absent load is a declared reporting
    gap" (A-n3:60).
  - **Every end but COMPLETE goes to the seat and the PI:** ans22a:8's "every end but PASS goes to the seat and the
    PI", ruled for G-VER of record, and in the seat's words for every stage on the box, "Every end but PASS of any
    stage on the box goes to the seat and the PI before anything else runs there (ans22b §1.4)" (ans23b:28; the
    spec raw's §3, point 5), each with COMPLETE in PASS's place.
- *The texts:* ans22a:8, :25–29; ans22b:24; ans23b:28; G-TIME-n's exits (drv:4384–4385, :4391–4405 and :4448: 0
  COMPLETE, 3 PAUSE, 2 a G-VER STOP or a refusal, and 1 otherwise, CAP among them); A-n3:60; runner:12–15.
- *As Code will build it:* the exits above, each end with its own last line; the self-test holds each code (CP19).
- *Another answer:* other codes (G-TIME-n's, say, with CAP at 1 and a G-VER STOP at 2), or other classes. The codes
  change the driver and the launch files; the classes change only what the launch files and the sessions do.

**CP13 — one pod session: a restart, a box change (the survey's open question 12).**
- *Code's reading:*
  - **A restart.** The identity holds the pod and the backend identifier: "a pod change refuses a resume and the
    stage restarts under a new root (Code's reading)" (schema:458–459). Before each invocation the launch checks
    that the pod has not restarted since the last, in G-VER v2's form (gvrun:42–63: the same pod id, and the
    container's first process older than the last invocation's launch). A restart is reported to the seat and the
    PI, and nothing runs until they rule (Code's reading; the respawn protocol has its two steps PASS before anything
    runs on a new or replacement box).
  - **A box change** aborts the campaign: "a mid-campaign box change aborts and restarts that checkpoint's
    campaign; no splicing" (m:251, which n:101 carries). After v1.0 it is "a new lock version" (LOCK:191–194;
    ans22a:33). The aborted run's report and cells are committed as they stand (rule 27). The new version's Clock is
    the PI's: n:152 dates v1.0 alone.
- *The texts:* n:101: "the campaign within one pod session (m:251 carried: a box change restarts the campaign; gate
  stages may span boxes)"; m:251, whose clause on a restart reads "after a restart the new `BACKEND` entry's
  identifier is the campaign's backend of record and supersedes the lock's field, which is not rewritten; the resume
  identity carries the new identifier"; LOCK:191–194; LOCK:1164: "A verdict campaign completes on one characterized
  backend"; ans22a:33; schema:458–459; gvrun:42–63; CLAUDE.md's respawn protocol and its consistency clause.
- *As Code will build it:* nothing new in the driver: the pod pin refuses another pod before any read (exit 1). The
  no-restart check is the launch files'.
- *Another answer:* a restart on the same pod id read as the same session, its resume allowed once the respawn
  protocol's two steps pass (the identity's pod and backend identifier unchanged); or the aborted run's record kept
  another way. Neither changes code; both change the launch files and the record.

**CP16 — the push before VERDICTS (the survey's open question 16).**
- *Code's reading:* the campaign's cells hold margins; "a push publishes them" (ans21b:29), and the pre-push screen
  halts on any match under a ckpt folder (the list of record's item 4). The close commit is not pushed before
  VERDICTS unless the PI says so. Rule 27 is met by the commit; origin is public.
- *The texts:* ans21b:29; ans18c:32: "The blinding binds reading, not the repository", said of `backend-ext`'s cell,
  with "the pre-push screen's halt on `data/n/ckpt/**` is cleared by this ruling" and "The push itself is the PI's
  word, as always."; the list of record's item 4; n:130.
- *As Code will build it:* nothing in the driver. The close's entry says "Not pushed".
- *Another answer:* the push with the close commit, on the PI's word and a ruling like ans18c:32's for the
  campaign's cells. That changes no code.

## 2. The dependencies, and what Code does meanwhile

- **The build goes ahead on CP1–CP20 as PINs** (the PI's "Build on the PINs"), declared in its BUILD entry.
  - It is in the driver alone, so `valence_core/n/` stays at `06b55761…1d39`.
  - It moves the one `LOCK_SHA256` pin to v1.0's committed sha256 (CP4), adds the cap's constant, 14,400,000 ms
    (CP5), and adds the `campaign` command with its self-test cases (CP1, CP19).
  - It comes with self-tests in battery windows the coordinating session grants, one blind review, one
    values-check, and the BUILD's commit window.
- **The campaign runs only after** the seat's answers on the eight, the BUILD's commit, and the launch files' relay
  to the box.
  - A ruling against a PIN before the run changes the driver or the launch files before the launch.
  - Each reading's "another answer" line above says what a different ruling costs.
- **The campaign's ends, pre-declared in the build** (CP12): 0 COMPLETE, 3 PAUSE, 5 CAP, 6 G-VER's STOP, 7 PI-STOP,
  and 1 a refusal or a crash. Every end but COMPLETE goes to the seat and the PI.
- **The twelve readings that are not starred** (CP1, CP3, CP4, CP5, CP7, CP10, CP14, CP15, CP17, CP18, CP19 and
  CP20) are Code's, as G-TIME-n's and G-VER's unstarred readings were. They are in the spec raw's §1, and the BUILD
  entry declares them. Two carry points the seat may want before the run, named here and not starred:
  - CP4's driver of record: v1.0 §4's driver is the driver at the lock, and the campaign's DRIVER line prints the
    BUILD's driver's sha256 (CP4 as sent said its STAGE line, the driver's blob), m-F3's convention (mF3ans:43),
    "the seat's to confirm for n";
  - CP15's reading of A-n3:60's "committed at step 14" as the campaign's cell files and its report; G-READ-n's
    artifact is step 15's, on the laptop.
- **The survey's declared departures (four items) and Code's own.** The survey's are in the spec raw's §5, the
  report's last section, for the seat to class. Code's are in the entry that commits this block.

## 3. The questions for the seat

- **Q1 (CP2).** Does the campaign run with no smoke, its first invocation the run of record? If a smoke, of what,
  and how are its cells handled?
- **Q2 (CP6).** Is "no looks" while the campaign runs these: stdout as n:130 has it, the end-wait on the PID alone,
  and, between invocations, the report read for its end state, its standing pause and the cap's `used_ms` alone, in
  every session? May the pod session and the coordinating session read more of the report?
- **Q3 (CP8).** Is n's excerpt the pause's record, the paused read's stdout lines and the monitor's figure against
  its bar, never a margin, with a rendering pause given by digest (Code's correction of CP8 as sent)? Each pause's
  excerpt goes to the seat as a raw of its own (ans23b:27): does the seat want, beside it, a file in m's form? Does
  it pre-rule any pause kind, as it did for `backend-ext-2`?
  - The excerpt prints a ceiling's `absdiff` at full precision, and the runner's per-read line has already printed
    that read's `rel`. Their ratio gives the cached path's scale, max(|log p(S)|, |log p(U)|): the size of a
    log-probability, not a margin or a pick. Is that within n:130?
- **Q4 (CP9).** Are the three STOP forms right: (a) the start's G-VER STOP written by the driver, as G-VER's record
  and the campaign's report in the schema's G-VER-STOP form; (b) a G-VER STOP at a resume, a STOP for the seat with
  the campaign's report left as it stood; (c) `--pi-stop` writing PI-STOP while a pause stands?
  - Once a G-VER STOP at the start is ruled, what follows: a new root, the report moved aside, or a new lock version?
    Its report blocks any resume of that root (runner:330–331), and VERDICTS reads it as `no-arm:gver-stop`
    (anl:6710–6719).
  - Should the PI's stop be open with no pause standing? The schema allows it (schema:213), and n:134's "a PI stop"
    is not tied to a pause (a decision on spend, say).
  - The PI's stop runs on the characterized pod, where the report and its cells are. If the PI stops the campaign
    after the pod is gone, the report stays PAUSE, which VERDICTS refuses (anl:6677–6679), and n:134's "a PI stop"
    has no record. Should a standing pause hold the pod until the seat and the PI rule, or may the stop be written
    elsewhere, from the copied report and cells?
- **Q5 (CP11).** Is the close's order right, and is step 3's hash check of G-TIME-n's two steered cells the exception
  ans21b §1.8 means ("the copy-back's own hash check")?
- **Q6 (CP12).** Are the exit codes right (0, 3, 5, 6, 7 and 1)? Do G-VER of record's classes (INTEGRITY; a FAIL of
  the launch) and "every end but PASS goes to the seat and the PI" extend to the campaign's ends, with COMPLETE in
  PASS's place?
- **Q7 (CP13).** May a pod restarted with the same id resume once the respawn protocol's two steps pass, or does a
  restart abort the campaign as a box change does? m:251's clause on a restart carries a restart's new identifier
  into the resume identity, while LOCK:191–194 makes a box change after v1.0 a new lock version: which governs a
  restart for n? What is an aborted run's record, and which report would VERDICTS read?
- **Q8 (CP16).** Is the close commit held from the push until VERDICTS unless the PI says otherwise, or pushed with
  a ruling like ans18c:32's?
