# n — two starred readings for the seat before G-READ-n's run: GR3 and GR5 (code → design)

*The n-build session (Code), PI date 2026-11-25. For the seat's next sitting, before G-READ-n's run (n §8 step 15;
rt4 item 2). The PI's routing of the seat's sft read puts this block first there: "G-READ-n's spec raw and starred
block take precedence when they land" (rtp item 4).*

*Where things stand:*
- *The N-pod campaign's run of record and its close are committed at `95cd461`, which is on origin. The seat's
  fourth sitting accepted them as committed (ans4 §1; rt4 item 1) and named six points it holds G-READ-n's BUILD to
  (ans4 §3).*
- *G-READ-n has no stage command: "Stage G-READ-n is wired at its own step (n v0.2 §8 step 15)." (drv:351). The
  driver holds its benchmark, `gread-bench` (drv:235–237, :4533–4604), and the campaign start's refusals and pins,
  which the command will reuse (GR1).*
- *A read-only survey of the texts at `95cd461` returned 15 open questions. Code's readings GR1–GR14 answer them as
  PINs and carry ans4 §3's six points.*
- *The coordinating session put the readings to the PI first, as the campaign's were. The PI's answer, relayed
  verbatim by the coordinating session on 2026-11-25, was "push both and build on the pins". Its "build on the pins"
  answers the question put with the readings; "push both" was the push of `5ceb8dd` and `0081351` (push #27), which
  the coordinating session has done (the spec raw's §2). So the build goes ahead on GR1–GR14 as PINs, in the driver
  alone (GR1).*
- *The two starred readings go to the seat before the run, not before the build: rt4 item 2's "[go, on the seat's
  ruling before the run]" (rt4:24–29). That is the campaign's order: its block, `fcab1e5`, went in before its BUILD,
  `e1be6d9`.*

*Sources, by sha256 or commit:*
- *G-READ-n's spec raw, `results/raw/2026-11-25_n-gread_spec.md`, committed with this block:*
  - *§1, Code's readings GR1–GR14 as sent (`17d66da9…9b43`, 195 lines);*
  - *§2, the coordinating session's routing of them, with the PI's answer (`4e686ed0…1dd0`, 18 lines);*
  - *§3, the survey's brief;*
  - *§4, the survey's report (`979bf23e…73c4`, 394 lines, compiled at `95cd461`).*
- *The texts: PROPOSAL-n v0.2 (`PROPOSAL-n-bk-reconciliation-v0_2.md`, cited n:line); LOCK-n v1.0 (`LOCK-n.md`, cited
  LOCK:line, the file's line, which ans4 writes L:line; v0.1's own L:k is LOCK:395+k); ADDENDUM-n1
  (`ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md`, cited A-n1:line).*

*Cited forms:*
- *ans4: is `results/raw/2026-11-25_n-campaign-close-read_design-to-code_answers.md`, the seat's fourth sitting of
  its thread (committed at `13ca2fe`);*
- *rt4: is `results/raw/2026-11-25_fourth-sitting_pi-routing.md`, the PI's routing of ans4 (committed at `13ca2fe`);*
- *rtp: is `results/raw/2026-11-25_p-sft-read_pi-routing.md`, the PI's routing of the seat's read of p's sft VERDICTS
  (committed at `5ceb8dd`);*
- *ans21b: is `results/raw/2026-11-21_n-gtime-starred-seven_design-to-code_answers.md`;*
- *ans18c: is `results/raw/2026-11-18_n-step4-run-pause_design-to-code_answers.md`;*
- *R: is `RESULTS.md` at `95cd461`, as in the readings; its line anchors move with every entry (this block's parent is
  `0081351`);*
- *drv: is `scripts/n_sessions.py` (`47abe489…c21a`), anl: is `scripts/n_analyze.py` (v7, `735da934…a7a8`), and
  probe:, cells: and schema: are the modules of that name under `valence_core/n/` (the package `06b55761…1d39`).
  Every code file:line is the same at `95cd461` and at `0081351`: no code file changed between them.*

*Code reads, builds and asks. Every reading below is Code's, and the seat rules each one; Code adjudicates none.*

## 0. The short form

- **Two readings.** Each comes with its texts, what Code will build, and what another answer would change.
- **They are ruled before G-READ-n's run, not before its build** (rt4 item 2). Neither needs a run to be ruled.
  - GR3 bounds what the command reads of a cell: the package's reader checks every field of each record, the
    margins among them, and the command keeps the session ids and the capture rows alone.
  - GR5 names the comparator the valence +1 result is held to: the random directions' +1 against their own −1 (the
    lock's pinned reading), or their +1 against the shadow.
- **One point made explicit, in GR3.** The readings as sent say that `check_cell` validates each record, "margins
  included". It does more than parse them: it holds each record's `margin` to `logprob_S − logprob_U`, and the
  fidelity block's numbers to their formula (schema:1007–1031, :1039–1069), in memory, printing a field path alone
  on a refusal. So "No margin … is computed on" holds of the command's own code, not of the package's check. The
  block states it, and Q1 asks about it.
- **The dependencies.** G-READ-n's run waits for:
  - the seat's answers on the two, and the PI's routing of them (the spec raw's §2, point 3);
  - the BUILD's commit;
  - a battery window on the laptop from the coordinating session, Q-F3 beside it (ans4 §3 point 4).
- **The questions** are Q1 and Q2 in §3, one per reading.

## 1. The two (to be built on them as PINs)

**GR3 — what the command reads of a cell (the survey's open question 6).**
- *Code's reading:* each cell is read through the package's reader, as the package BUILD's PIN of record has it:
  `load_cell(staging, arm, direction_id, dose_label, identity=None, keep_arrays=…)` (cells:135–174). It parses the
  cell's JSON whole (cells:146) and checks it with `check_cell` (cells:148), which checks every record field by field
  (schema:893, :1092–1124). The command keeps from each record its `session_id` and its capture row, and drops the
  cell before any fit. The labels are the cells (the + pole, the − pole or the shadow); the groups are the session
  ids. Nothing the command itself computes on, prints or writes is a margin, a log-probability, a pick or a
  fidelity value.
- *The texts:*
  - ans4:32: "nothing of the cells' margins read or printed — the probe reads residuals and labels, and stdout prints
    AUCs, counts and digests";
  - n:130: "the blinding question is who sees margins before VERDICTS: nobody", and the campaign's "stdout prints
    session index, arm, dose, the fidelity value against TAU, timing — never a margin";
  - the package BUILD's PIN, declared to n-analyzer (R:11583–11585): "G-READ-n's driver reads captures only through
    `cells.load_cell(..., keep_arrays=True)`. That call checks each layer's written rows against the cell's
    `capture_sha256`, and each row against its record's sha16, before a fit.";
  - `load_cell`'s docstring: "Each map is dropped once checked, unless ``keep_arrays``: a reader (G-READ-n's
    driver) then gets the arrays, read-only." (cells:139–140);
  - what `check_cell` checks of a record's numbers (schema:1007–1031, :1039–1069): each log-probability not positive
    and each sum `math.fsum` of its tokens; `margin` equal to `logprob_S − logprob_U`; the restricted read's
    probabilities, its sum to 1 and its pick; the fresh margin equal to its two log-probabilities' difference; and
    the fidelity block's numbers equal to `fidelity_numbers`' formula. A refusal prints its field path alone, never a
    value (cells:72–75, :150).
- *As Code will build it:* `load_cell` with `identity=None` on all 138 cells (GR2), the arrays kept for the cells
  probed alone, two cells open at a time (GR9). The self-test plants values it can recognize in every margin field
  of its stand-in cells, consistent with `check_cell`'s checks, and asserts that none reaches the probe's inputs,
  stdout or the artifact (GR13).
- *Another answer:* a reader that never checks the margin fields: the driver's own JSON parse, keeping `session_id`
  and `capture.row` and checking the rows against `capture_sha256` and the sha16s itself, since the package cannot
  change (ans4 §3 point 2). The JSON is decoded whole either way; what changes is that the margins are not checked
  before they are dropped. The PIN of record (R:11583) would be superseded for G-READ-n, and the new reader would
  need self-test cases of its own. The fits do not change.

**GR5 — the comparator the valence +1 result is held to (the survey's open question 5).**
- *Code's reading:* the lock's pinned one. At +1, each random direction's comparator reads its +1 cell against its
  own −1 cell on the 40 floor sessions, the ± contrast valence +1 is read on (N1-R reads +1 and −1 on those
  sessions, LOCK:834); at +1/2, +d_20 and +d_eq, its cell at the point against the 40 floor sessions' shadows. Each
  comparator then reads the same contrast as the result it is the floor for. span_reward's f0.10 and f0.20 take
  +d_eq's and +d_20's comparators (LOCK:964–965).
- *The texts:*
  - probe:32–33, Code's reading at the package BUILD, which LOCK:1261 pins ("The probe's (probe.py:29–34): the
    contrasts and the comparator"): "COMPARATOR -- each random direction's band median on the same contrast at the
    same dose point (its own 40 sessions), not shuffled.";
  - A-n1:56 and LOCK:962–964: "the 24 random directions probed at the matched point without shuffles", the contrast
    "the − pole at valence +1, else the shadow";
  - ans21b:23 (Q5, "Stands as built"), on the count: "a comparator is a property of the point — 24 directions at that
    norm against the shadow — not of the axis compared against it";
  - LOCK:965–966: "The comparator's band medians are over each random direction's 40 floor sessions against the
    axis's 160";
  - the count is the same under either reading: 4 points × 24 directions × 31 layers = 2,976 calls on 80 rows
    (ans21b:23; drv:4533–4547).
- *As Code will build it:* at +1, N1-R's +1 and −1 cells for each of the 24 directions; at +1/2, +d_20 and +d_eq,
  N1-R's cell at the point against the rows of N1-V's shadow cell for the 40 floor sessions, by session id (GR6).
  Each point's 24 band medians are computed once and shared by the results matched to it (ans21b:23).
- *Another answer:* at +1 as at the other points, each direction's +1 against the 40 floor sessions' shadows. Then
  the valence +1 result, a ± contrast, is held to a floor read on + against the shadow, and N1-R's −1 cells are
  checked (GR2) but never probed. The change is one argument in the driver; the count and the time do not change.

## 2. The dependencies, and what Code does meanwhile

- **The build goes ahead on GR1–GR14 as PINs** (the PI's "build on the pins"), declared in its BUILD entry.
  - It is in the driver alone, so `valence_core/n/` stays at `06b55761…1d39` and `scripts/n_analyze.py` at v7
    (ans4 §3 points 1–2).
  - It adds the `gread` command (GR1), its pins (the close list's sha256, GR2; the two seeds, GR7) and its self-test
    cases (GR13).
  - It comes with self-tests in battery windows the coordinating session grants (no Python on the laptop outside
    one while Q-F3 runs), one blind review, one values-check, and the BUILD's commit window.
- **G-READ-n runs only after** the seat's answers on the two, the PI's routing of them, the BUILD's commit, and a
  battery window beside Q-F3.
  - A ruling against a PIN before the run changes the driver before the run.
  - Each reading's "another answer" line above says what a different ruling costs.
- **G-READ-n's ends, pre-declared in the build** (GR8, GR9): exit 0 when the artifact is written, whatever its six
  statuses; 1 on any refusal or failure, with no artifact. A crash or a stop leaves no artifact, and the run repeats
  whole in a new window.
- **The twelve readings that are not starred** (GR1, GR2, GR4 and GR6–GR14) are Code's, as the campaign's unstarred
  readings were. They are in the spec raw's §1, and the BUILD entry declares them. §1's section "Notes for the seat"
  holds four citations and no question, beside the survey's departures: ans4 §3 point 4's ans18c:40, which is the
  exclusion of Q-F3's folder from git commands (the window's texts are ans21b:23 and :80); probe.py's docstring
  anchors; the lock's two L:N forms; and the observation at R:12996 on the shadow contrast. The spec raw's head
  names four points of the readings as sent that are imprecise: GR3's and GR5's, which this block carries, and
  GR7's and GR8's, which the BUILD builds as the head has them.
- **The survey's declared departures and Code's own.** The survey's are in the spec raw's §4, the report's last
  section, for the seat to class. Code's are in the entry that commits this block.

## 3. The questions for the seat

- **Q1 (GR3).** Does ans4:32's "nothing of the cells' margins read or printed" admit the package reader's parse and
  check of each record whole, `load_cell` and `check_cell`, through which the package BUILD's PIN binds the rows
  (R:11583)? Under it the command keeps each record's `session_id` and row alone; its own code computes on, prints
  and writes no margin, and the self-test's planted values assert it. Or must G-READ-n read the cells by a parse of
  its own that never checks the margins, the PIN superseded for it?
- **Q2 (GR5).** At valence +1, is each random direction's comparator its +1 against its own −1 on the 40 floor
  sessions (probe:32–33, which LOCK:1261 pins), or its +1 against those sessions' shadows (ans21b:23's sentence)? At
  +1/2, +d_20 and +d_eq the two readings agree.
