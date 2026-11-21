# n — seven starred readings for the seat before G-TIME-n's run: GT1, GT4, GT8, GT9, GT10, GT12 and GT16 (code → design)

*The n-build session (Code), PI date 2026-11-21. For the seat, before G-TIME-n's run. The PI's word governs only the
nudge to the seat.*

*Where things stand:*
- *LOCK-n v0.1 is committed at `deabf3f`, sha256 `88d9fe7b…e9d5`. G-TIME-n (n §8 step 11) runs under it.*
- *G-TIME-n's stage command is not built: "Stages G-TIME-n, G-VER, the campaign and G-READ-n are wired at their own
  steps" (drv:182).*
- *A read-only survey of the texts, at `deabf3f`, returned 17 open questions. Code's readings GT1–GT17 answer them as
  PINs.*
- *The PI's answer, relayed verbatim by the coordinating session on 2026-11-21, was "Build on the PINs". So the build
  goes ahead on GT1–GT17 as PINs, in the driver alone (GT3).*
- *The seven starred readings go to the seat before the run, not before the build. That is G-CAL-n's order: its block,
  `99196e1`, went in before its BUILD, `89a55c3`.*
- *Item N.2's words are on record. The coordinating session's notes commit, `c9d35e2`, holds the PI's paste block
  (`results/raw/2026-11-20_second-sitting_pi-routing.md`) and quotes items 2 and 3 in its entry (R:55–57). That
  answers the survey's open question 14 and GT17's last clause.*

*Sources, by sha256 or commit:*
- *G-TIME-n's spec raw, `results/raw/2026-11-21_n-gtime_spec.md`, committed with this block:*
  - *§1, Code's PINs GT1–GT17 as sent (`f3fa5f05…f42f`, 153 lines);*
  - *§2, the coordinating session's routing of them, with the PI's answer;*
  - *§3, the survey's brief;*
  - *§4, the survey's report (`a23831e4…05e7`, 245 lines, compiled at `deabf3f`).*
- *The texts: PROPOSAL-n v0.2 (`PROPOSAL-n-bk-reconciliation-v0_2.md`, cited n:line); LOCK-n v0.1 (`LOCK-n.md`, cited
  L:line); ADDENDUM-n1 and ADDENDUM-n2 (A-n1:line, A-n2:line).*

*Cited forms:*
- *ans16b: is `results/raw/2026-11-16_n-build_design-to-code_answers.md`;*
- *ans19: is `results/raw/2026-11-19_n-starred-twelve_design-to-code_answers.md`;*
- *ans20: is `results/raw/2026-11-20_n-gvec-gcal-reads_design-to-code_answers.md`;*
- *ans20b: is `results/raw/2026-11-20_n-lock-v0_1-read_design-to-code_answers.md`;*
- *box: is `results/raw/2026-11-18_box-gpu_design-to-code_answers.md`;*
- *rv3: is `results/raw/2026-11-16_n-build_review-step3.md`;*
- *R: is `RESULTS.md` at `c9d35e2`, this block's parent; its line anchors move with every entry;*
- *drv: is `scripts/n_sessions.py`, and schema:, runner:, primitive:, cells: and probe: are the modules of that name
  under `valence_core/n/`. Every code file:line is at `c9d35e2`, where no code has changed since `deabf3f`.*

*Code reads, builds and asks. Every reading below is Code's, and the seat rules each one; Code adjudicates none.*

## 0. The short form

- **Seven readings.** Each comes with its texts, what Code will build, and what another answer would change.
- **They must be ruled before G-TIME-n's run, not before its build.** Each sits in one place in the driver, and
  G-TIME-n's figures are measured once, on the box. Two of them, GT1's read set and GT4's identity, cannot be changed
  after the run without running it again.
- **The other five can mostly be ruled after the run.**
  - GT8's formula is re-derived from what the run stores: every read's cached and fresh shares.
  - GT9's alternatives are re-derived from its stored figures too.
  - GT10 runs on the laptop.
  - GT12 and GT16 change no read.
- **The dependencies.** G-TIME-n's run waits for:
  - the seat's answers on the seven;
  - the BUILD's commit;
  - the launch files, relayed to the box by the coordinating session;
  - the box itself, kept up through G-TIME-n and the campaign (the PI's routing of 2026-11-20, second sitting, item
    3, "as ruled this morning": the first sitting's item 4, "[stays up]").
- **The questions** are Q1–Q7 in §3, one per reading.

## 1. The seven (to be built on them as PINs)

**GT1 — the read set (the survey's open question 1).**
- *Code's reading:* 18 reads, three on each of six sessions.
  - **The sessions:** runs 0, 32, 64, 95, 127 and 159. These are round(k·159/5) for k = 0..5, evenly spaced over the
    session set's order: two floor sessions (runs 0 and 32) and four neutral.
  - **Why they are not drawn:** v0.1 names no G-TIME-n key, and the keys are a lock item.
  - **The reads, on each session:**
    - (a) the shadow, N1-V `none` at d = 0, re-computed (reason `dose-rule`), with its identity check;
    - (b) N1-V `valence` at +1, re-computed (`dose-rule`);
    - (c) N1-V `valence` at +1/2, the cached path alone.
  - **The kinds are attributes of reads, not separate reads:**
    - shadow: 6, the (a) reads;
    - steered: 12, the (b) and (c) reads, 6 of them cached only;
    - fidelity re-compute: 12, the (a) and (b) reads, each with `duration_ms_fresh`;
    - capture-on: all 18.

    So every kind has at least six reads.
  - **Why N1-V's cells stand for the campaign's (Code's reading):** a read's cost does not depend on its arm or its
    direction. Every arm's read is the same forwards: one prefill and two label continuations, and with a
    re-computation two full forwards. The steered reads run under the same additive hook; the unsteered ones (the
    shadows, N4-T and N4-Ts) run through the same hook path with no injection placed.
  - **Length barely varies:** 144 of the 160 sessions are 1273 tokens long and the rest 1266–1272, so the choice of
    sessions does not move the cost. The six are 1273 tokens long five times and 1268 once (run 127), by Code's count
    over `data/n/ids/sessions.jsonl`, the same figures as its ranking of 2026-11-20 over BK's skeleton files.
  - **N4's reads are a little longer:** they add their told line's tokens to the session's (schema:113). G-TIME-n
    reads no N4 arm, so the projection takes the sessions' lengths for N4's 320 reads, a few tokens short (Code's
    reading).
- *The texts:*
  - n:118: "Six reads of each kind (steered, shadow, fidelity re-compute, capture-on) timed on the box; projections; the
    cap set by the PI";
  - schema:88–89: "every read captures: G-TIME-n's "capture-on" kind is every read";
  - schema:1042–1050: at "time", a read at d ∈ {0, ±1} may carry the `dose-rule` re-computation, and a
    re-computation at any other point is `timing`;
  - schema:1071–1082: an unsteered re-computed read carries the identity check at the lock's bound;
  - primitive:213–217: a steered read needs its shadow's record on disk;
  - the keys: L:397–404 (§5's table names no G-TIME-n key) and n:117 (the keys are LOCK-n v0.1's item).
- *As Code will build it:*
  - one constant, the six runs, asserted equal to round(k·159/5);
  - a plan builder: the six shadows, then the six +1 reads, then the six +1/2 reads, launch indices 0..17. This is
    GT2's order: the shadows first, as the runner's ORDER has them (runner:18–22).
  - Each record carries its cell, run, `seq_len`, `duration_ms` and `duration_ms_fresh`, and the projection artifact
    copies them (GT11).
- *Another answer:*
  - Other sessions, arms or points, or separate reads per kind: the constant and the plan builder change, and G-TIME-n
    runs again (18 reads: about 10 s of model time at the extension's medians, A-n2:40, beside one load).
  - A drawn set needs a key, and a key is a lock item. v0.1 names none, so a key would wait for v1.0 or a dated note.

**GT4 — the identity at "time" (the survey's open question 7).**
- *Code's reading:* every field from LOCK-n v0.1.
  - **The stage and the lock:** stage `time`; `lock_sha256` `88d9fe7b…e9d5`.
  - **The dose map of record:** ρ 0.3, R 25.54500811131038, R_ℓ 21.98789170395024, d_eq 0.2869170055735837 and d_20
    0.5738340111471674, all seven points kept (L:360–374). It comes from G-CAL-n's `gcal.json`, status PASS
    (`4c92f228…bb8f`), and `dose_map.json` (`d4a73b54…efb3`), both committed at `db00d6d` (L:375–379).
  - **The fidelity rule** (L:486–497, L:505–511, L:662–664): TAU; p0 1 of 26; cadence 160; alpha 0.01; the ceiling
    C = 0.25; the median rel 0.0013026706058596332; the key `n-fid|{s}`; and as `sample_rule`, the lock's words for
    the sample (L:406–410). `identity_bound` is C.
  - **The directions:** {`valence`: `ba4da67fb717b5bb`} (L:302–303), the only direction G-TIME-n injects.
  - **The rest as the lock has them:**
    - the read window, 4,096;
    - the site, 32, and the band, 33–63;
    - the weights, `36f05404…0fdb`;
    - n's backend identifier, `8264f719efd347a9`, bridged to the characterization's `4ed3f2c70fe8afbf`;
    - the pod, `emw1e4embiwe9b`;
    - the rendering, MANIFEST `53a8cd74…99d8`;
    - the label convention, "space".
  - **The package** `06b55761…1d39` and its twelve-file closure (L:781–813). They are unchanged because the build is
    in the driver alone (GT3).
  - **No cap, beside the identity:** the runner's `hour_cap_ms` is None (runner:266; the report's `cap.hour_cap_ms`,
    schema:1209). The cap is not an identity field, so a cap would not move the identity's sha256; a resume refuses
    another cap (runner:413).
- *The texts:*
  - ans20b:58: "its identity carries v0.1's sha256 and C";
  - ans19:50: R14, "the ceiling binds at G-TIME-n, whose identity carries the lock's C" (L:560);
  - L:740–742: "its identity carrying v0.1's sha256 and C";
  - schema:448–481, the identity's fields;
  - schema:845–852: `lock_sha256`, `dose_map`, `identity_bound`, `ceiling` and `median_rel` are null only at
    backend-ext;
  - schema:876–878, F5's p0 floor;
  - schema:507–508: `sample_rule` is "the lock's words for the 10% sample";
  - the cap: L:554, the cap row's "where" is the campaign. The BACKEND extension's R5 had "no cap" (drv:95).
- *As Code will build it:*
  - one function builds the identity from the lock's pins in the driver.
  - For a run of record, each pin is checked against the committed file that carries it, before the load:
    - LOCK-n.md's HEAD bytes hash to the lock's sha256;
    - `gcal.json` and `dose_map.json` are HEAD's bytes at their sha256s, `gcal.json` a PASS and pinnable;
    - the map rebuilt by `gcal.dose_map` from G-VEC's record equals both;
    - the valence row's sha16 is G-VEC's of-record one and the lock's;
    - n's backend identifier is the lock's;
    - the weights are the lock's;
    - the package digest and the closure are §18's;
    - `schema.check_stage_identity` passes.
- *Another answer:* one function, before the run. For example:
  - a cap at G-TIME-n, which would let the stage end early as CAP;
  - another `sample_rule`;
  - another direction set.

  After the run, any change to the identity is a re-run: the identity is in every cell file and, with its sha256, in
  the report.

**GT8 — the cap's basis: the projection of model time (the survey's open question 3).**
- *Code's reading:* T = N·median(c) + K·median(f).
  - **c and f:** for each read, its cached share is c = `duration_ms` − `duration_ms_fresh`, or `duration_ms` where it
    has no re-computation. Its fresh share is f = `duration_ms_fresh`. So c comes from all 18 reads and f from the 12
    re-computed ones.
  - **N = 7,680**, the campaign's reads.
  - **K = 3,637**, its re-computations, by runner:147's rule over the plan of record (Code's count):
    - 3,040 under the dose rule, at d ∈ {0, +1, −1}: N1-V's three cells (480), N1-R's ±1 (1,920), N1-P's ±1 (320),
      and N4-T and N4-Ts (320);
    - 597 in the keyed sample: its 15 sessions at the eleven other cells outside N1-R (165), and its 6 floor sessions
      at N1-R's 72 other cells, 24 directions × 3 points (432). The 15, 6 of them floor, are
      `results/raw/2026-11-20_n-lock-v0_1_fidsample_out.txt`'s.

    The stage computes K with the package's own functions (`runner.campaign_order` over the campaign's view of this
    identity). It asserts that view's `read_plan_sha256` equal to the lock's `7f7d7301…88a6` (L:467).
  - **Beside it:** T at the maxima (the largest c over the 18, the largest f over the 12), in ms and in hours.
  - **Why T is the cap's basis:** the cap counts model time as the runner computes it. The PI sets the cap in hours at
    v1.0.
  - **The extension's figures** (309.0 ms cached, 357.1 ms for the fresh pair, "used by nothing", A-n2:40) are printed
    beside, not used.
- *The texts:*
  - n:120: LOCK-n v1.0 holds "Projections, the cap";
  - L:591–592 and L:600–604, OPEN 2's split of record: "inside it, the reads' and re-computations' model time as the
    runner computes `cap`";
  - runner:66–70: the cap is the sum of the records' `duration_ms`;
  - schema:121–124: `duration_ms` is "the read's wall-clock of model work, both paths", and `duration_ms_fresh` "the
    fresh path's share … for G-TIME-n's kinds and the cap";
  - primitive:205–207, primitive:237–241 and primitive:283–284: one clock over the read, the fresh pair timed
    inside it;
  - A-n2:40: the extension's figures;
  - n:101: §2.7's planning values, "G-TIME-n governs".
- *As Code will build it:*
  - After a COMPLETE run, the stage's own code reads its records, as the BACKEND extension's does (drv:1157–1160).
  - It computes every read's c and f, their medians (numpy's `median`) and maxima, N and K, and T at both.
  - It writes them, with the formula's text, into the projection artifact `data/n/gtime/gtime.json` (GT11). Every
    read's c and f are stored.
- *Another answer:*
  - A formula over the stored figures needs no box re-run: it is re-derived on the laptop from the artifact, declared.
    That covers another statistic (a mean, or a percentile), and a split by kind (c over the shadows against the
    steered reads, f over the shadows against the +1 reads).
  - A basis that needs reads G-TIME-n does not take, such as N1-R's or N4's own, is a re-run (GT1).

**GT9 — pod hours beside the cap, outside it (the survey's open questions 3 and 4).**
- *Code's reading:* three terms, beside the cap and outside it.
  - **(a) The loads:** G-TIME-n's measured load for each invocation (the report's `loads_ms`).
  - **(b) The I/O.** Code's PIN is option (i), a model-free append benchmark on the box's volume after the reads:
    - it appends 160 example records to one scratch cell. The cell is in a folder outside the repository
      (`guard.refuse_test_out`), on the same filesystem as the stage's root (asserted);
    - each append is timed;
    - a per-append cost a + b·k, where k is the records already in the cell, is fitted by least squares over k =
      0..159;
    - the fit is summed over the campaign's 138 cells: 18 of 160 rows and 120 of 40, so Σ = 7,680·a + 322,560·b;
    - one 160-row cell stands for every cell. A cell's first append creates its arrays at the cell's capacity, and
      every later append maps the whole array (cells:185–197), so a 40-row cell's appends may cost less than the fit
      says. The first append, k = 0, is fitted with the rest.

    Beside it, the stage's own per-read I/O: the time from one per-read line to the next, minus that read's
    `duration_ms`, timed by the driver's printer hook. Those cells hold at most six rows, so this figure cannot show
    the growth.
  - **(c) Not measured, and reported as such:** the captures' copy-back (about 4.9–5.0 GB at the campaign's 7,680
    rows, schema:83–85; A-n1:54's 4.7–4.8 GB at 7,360 reads), G-VER of record (step 12), and the campaign's resumes.
  - **The alternatives for the seat:**
    - (ii) the measured per-read I/O × 7,680, declared a lower bound;
    - (iii) no I/O projection, left to the 8 h budget's slack.
- *The texts:*
  - ans20b:44: "The reads' I/O outside the cap: the cap is model time as the runner computes it (§11); I/O is outside
    and declared so.";
  - R:5921–5922, the n package's BUILD entry: "31–32 row writes with fsync per read, and the cell JSON rewritten per
    append. G-TIME-n times it on the volume.";
  - rv3:196: "outside the cap but inside pod hours; G-TIME-n should time it on the volume";
  - cells:200–249: every append re-checks the whole cell (`check_cell`) and rewrites its JSON;
  - L:587–590: the N-pod budget of 8 h. box:31: "The spend is the PI's at every step.";
  - A-n1:54: the copy-back.
- *As Code will build it:*
  - The benchmark is one function in the driver. It runs only after a COMPLETE run, in the same invocation, in a
    temporary folder under `--bench-dir`, a folder outside the repository that the stage removes at its end.
  - The benchmark's cell is N1-V `valence` +1. Its records are the stage's own first +1 record (launch index 6),
    re-keyed to each session of the set in turn (its session's ids, read id and launch index), with capture rows of
    noise. That is the campaign's record form with its re-computation, the larger form, so the fit is an upper bound
    for cells without re-computations. No example builder of the schema runs in the stage (schema:240–242: "no
    production path calls them").
  - Every append's time, the fit (a, b) and the sum are stored in the artifact, with the per-read I/O.
- *Another answer:*
  - (ii) and (iii) need no re-run: (ii) is re-derived from the stored per-read figures, and (iii) is a line.
  - A different benchmark (another record form, another cell, or another count) changes the one function and means
    another box run.

**GT10 — G-READ-n's fits (the survey's open question 5).**
- *Code's reading:*
  - **Where they run** is Code's call (A-n1:56). They run on the laptop's CPU, after the copy-back, so they are outside
    the box's cap.
  - **Timed at step 11** by a model-free benchmark on the laptop, in a battery window the coordinating session grants.
    It times probe.py's statistic at its pinned settings:
    - k's `fit_lr` at seed 7, 300 iterations, rate 0.1 and l2 0.01;
    - the grouped 10-fold folds of `cv_seed` 20261116;
    - synthetic float32 arrays of the contrasts' two shapes.
  - **The count,** by Code's arithmetic, which reproduces the seat's "About 404,000 fits in all" (ans16b:42).
    - The primary results are six (valence +1, +1/2, +d_20 and +d_eq; `span_reward` f0.10 and f0.20). Each takes 31
      layers × (1 + 200 shuffles) grouped 10-fold calls over 320 rows (160 sessions, two rows each). That is 37,386
      calls, or 373,860 fits.
    - The comparator is the 24 random directions at the four random points the results are matched to (+1, +1/2,
      +d_20 and +d_eq). Each takes 31 layers × one call over 80 rows (40 floor sessions, two rows each). That is 2,976
      calls, or 29,760 fits.
    - The comparator's band medians are computed once per point and shared by the results matched to it: valence
      +d_eq with `span_reward` f0.10, and valence +d_20 with f0.20 (schema:229–231). Computed per result, it would be
      4,464 calls (44,640 fits, 418,500 in all), which does not reproduce the seat's figure.
    - In all, 403,620 fits.
  - **The projection:** 37,386 × the median call at 320 rows + 2,976 × the median call at 80 rows. It is reported
    beside the projections at v1.0.
  - **The alternative for the seat:** run them on the box, timed there and counted in the cap. L:598: "timed by their
    own artifact and counted against the cap in v1.0's accounting".
- *The texts:*
  - A-n1:56: "Where it runs (the box's GPU or the laptop's CPU) is Code's call, timed at G-TIME-n and counted in the
    cap where it runs on the box.";
  - ans16b:42;
  - L:598 and L:600–604, OPEN 2 (a);
  - probe:44–49, the module's settings;
  - n:121: G-READ-n is "computed after the campaign from the captured residuals".
- *As Code will build it:*
  - A model-free command, `gread-bench`, in the driver. It draws the synthetic arrays from a seeded stream, groups them
    as `probe.contrast_rows` does, and times a declared number of calls at each shape.
  - It prints every call's time, the counts and the projection, and writes no file. Its stdout is the raw of record,
    committed with G-TIME-n's entry.
  - The laptop runs Q-F3's campaign beside it, so the figure may be high. That is declared.
- *Another answer:*
  - On the box: the same command is run there, or G-READ-n's own run is timed, and the sum enters the cap (L:598).
  - Another count is one constant.

**GT12 — exposure (the survey's open question 11).**
- *Code's reading:*
  - G-TIME-n reads no point below d = 0: its 12 steered reads are on `valence` at +1 and +1/2.
  - §0.4's table counts the negative pole's generations and forwards under the PI's option A1, "struck beyond d = −1"
    (L:986–987). G-CAL-n's 48 turns at −ρ are among them.
  - Whether positive-pole timed reads need a line in it is the seat's call.
- *The texts:*
  - n:16–28, §0.4 and its table;
  - n:14, ledger (53): "the exposure count is computed from the gate list, in gate order, as a table".
- *As Code will build it:* no read at d < 0. The plan's constant holds none, and the entry reports zero negative-pole
  reads.
- *Another answer:* a line in §0.4's table (v1.0's text) for G-TIME-n's 12 positive-pole reads, or a zero line. No read
  changes.

**GT16 — who reads it (the survey's open questions 13 and 15).**
- *Code's reading:*
  - The report, the artifact, the raw and the entry are committed.
  - The projections go to the PI for the cap at v1.0 (ans20b:71; the PI's item 2 of 2026-11-20, second sitting: "the
    projections to me"). The coordinating session relays them (Code's reading).
  - The seat reads the record with v1.0's draft. A COMPLETE run is followed by no STOP for the seat; a pause is the
    seat's.
  - The figures stand for the box they ran on. If the box changes before the campaign, whether G-TIME-n runs again is
    the PI's call. n:101 has "gate stages may span boxes", and ans20:58 has a new box re-run the characterization and
    the BACKEND extension first.
- *The texts:*
  - ans20b:71: "the projections to you for the cap at v1.0";
  - n:118 and n:120;
  - n:101;
  - ans20:58;
  - m's and p's G-TIME stages, which stopped for the seat's read (R:12800 and R:14163: "Stopped for the seat's
    read."; the survey's §4).
- *As Code will build it:* COMPLETE exits 0 with the artifact written. The entry names the projections for the PI.
- *Another answer:* a STOP for the seat's read after a COMPLETE run, as m and p had. The entry becomes a STOP block, and
  the PI's cap waits for the seat. No read changes.

## 2. The dependencies, and what Code does meanwhile

- **The build goes ahead on GT1–GT17 as PINs** (the PI's "Build on the PINs"), declared in its BUILD entry.
  - It is in the driver alone, so `valence_core/n/` stays at `06b55761…1d39`.
  - It comes with self-tests in battery windows the coordinating session grants, one blind review, one values-check,
    and the BUILD's commit window.
- **G-TIME-n runs only after** the seat's answers on the seven, the BUILD's commit, and the launch files' relay to the
  box.
  - A ruling against a PIN before the run changes the driver before the launch files.
  - After the run, each reading's "another answer" line above says what a different ruling costs.
- **G-TIME-n's ends, pre-declared in the build** (GT5–GT7; the spec raw's §1):
  - COMPLETE: exit 0, the artifact written;
  - a monitor's fire: a PAUSE, exit 3. The report is written and no projection, for the seat. After its ruling, a
    resume continues, skip-only, and the projection is written only at COMPLETE. That is GT5's "A ruling precedes
    any use of the projections";
  - G-VER's STOP: exit 2, before the weights load, with no read and no report;
  - a refusal before any read: exit 2;
  - anything else: exit 1.

  G-TIME-n has no pass rule: n:118 states no bar, and the report's end states hold no PASS (schema:1131).
- **The ten readings that are not starred** (GT2, GT3, GT5, GT6, GT7, GT11, GT13, GT14, GT15 and GT17) are Code's, as
  G-CAL-n's unstarred readings among GC1–GC22 were. They are in the spec raw's §1, and the BUILD entry declares them.
- **The survey's declared departures (five items) and Code's own.** The survey's are in the spec raw's §4, the
  report's last section, for the seat to class. Code's are in the entry that commits this block.

## 3. The questions for the seat

- **Q1 (GT1).** Is the read set Code's 18 reads?
  - That is the six evenly spaced sessions, each with three reads: the shadow re-computed, N1-V +1 re-computed, and
    N1-V +1/2 on the cached path alone.
  - The kinds are attributes of those reads, and N1-V's cells stand for the campaign's.

  If not, which reads?
- **Q2 (GT4).** Is the identity at "time" Code's: the lock's values and the directions {valence}? And, beside it, no
  cap (the runner's `hour_cap_ms` None)? If not, what differs?
- **Q3 (GT8).** Is the cap's basis T = 7,680·median(c) + 3,637·median(f), with the maxima beside and the extension's
  figures beside and unused? If not, what statistic or terms?
- **Q4 (GT9).** Are the pod hours beside the cap these three terms?
  - the loads;
  - the I/O by option (i)'s append benchmark, fitted as a + b·k and summed over the 138 cells;
  - the terms not measured, named.

  Or (ii), or (iii)? And does the one 160-row cell stand for the 40-row cells, with k = 0 in the fit?
- **Q5 (GT10).** Where do G-READ-n's fits run? Code's reading is on the laptop's CPU, outside the cap, timed by
  `gread-bench` and projected to 403,620 fits. The other is on the box, timed there and counted in the cap. And is the
  comparator's set of band medians computed once per random point and shared (403,620 fits), or once per result
  (418,500)?
- **Q6 (GT12).** Does §0.4's table gain a line for G-TIME-n's 12 positive-pole reads (or a zero line), or none?
- **Q7 (GT16).** After a COMPLETE run, do the projections go to the PI for the cap, with the seat's read at v1.0's
  draft? Or does the seat read G-TIME-n first, as a STOP? And if the box changes before the campaign, does G-TIME-n run
  again?
