# n — the N-pod campaign's specification as the texts state it, Code's readings CP1–CP20, and the coordinating session's routing of them

PI date 2026-11-23. Code (the n-build session).

**What this raw holds.** It serves the seat's read of the eight starred readings (the block committed beside it) and
the N-pod campaign's BUILD (n §8 step 14):
- **§1, Code's readings CP1–CP20 as sent, verbatim** (`fd80cf43…23b0`, 190 lines). They went to the coordinating
  session as a note in the sessions' notes folder (`2026-11-23_n-build_campaign-pins.md`), a byte copy of Code's
  scratch file checked by `cmp`, named in Code's message by its name, its sha256's abbreviation and its line count;
  the coordinating session re-hashed it equal before it routed them (§2). It is in no other repository file.
- **§2, the coordinating session's message routing them, with the PI's answer, verbatim** (`90769590…58b8`, 19
  lines). It is in no other repository file.
- **§3, Code's addendum to the readings, verbatim** (`e8171ce0…dd75`, 39 lines). It sets the eight points of the
  seat's raw of its second sitting of 2026-11-23 (its §2) against CP1–CP20 as sent, as that raw's routing item N.2
  asks ("§2's eight points carried into the PINs"), routed by the PI's "Route as given". No PIN changes; CP8 and
  CP12 each gain a sentence. It went to the coordinating session as a note in the sessions' notes folder
  (`2026-11-23_n-build_campaign-pins-addendum.md`), a byte copy of Code's scratch file checked by `cmp`. It is in no
  other repository file.
- **§4, the survey's brief** (`c940d92d…6f02`, 105 lines). One change: the repository's full path, on its second
  line, is written `<repo>` (`8b0d1ce3…6601`).
- **§5, the survey's report, verbatim** (`7f728f96…43d1`, 342 lines). A subagent compiled it read-only at HEAD
  `098218c`: the campaign's specification as the texts state it, with a citation for its claims, and the questions
  the texts leave open. It was extracted from the subagent's hand-back by `jq` when it returned, on 2026-11-23. Its
  departures are in its last section, for the seat to class.

**The cited lines.** Every file:line in §1, §3 and §5 is the repository's at `098218c`, but §3's seat:N, the seat's
raw's line N, committed unchanged at `c26b117`. This raw's parent is `c26b117`; among the cited files it changes
`RESULTS.md` alone, so §1's R: anchors are `098218c`'s.

**Three points in §1, one in §3 and two in §5, as sent, are imprecise, and CP8 takes a correction.** §1, §3 and §5
stay verbatim; the block carries each as below.
- CP8's pause record ("kind, read id, launch index, arms, `also_fired`"): the schema's field for the arms is
  `arms_in_scope` (schema.py:1174–1175), and the record also holds the binomial's batch where it has one
  (schema.py:1178–1180).
- CP8's figure for a ceiling pause, "the fidelity value against C": the record's figure against C is `absdiff`,
  |margin − fresh margin| (schema.py:416); the stdout line prints `rel`, `absdiff / scale`, against TAU
  (schema.py:418; runner.py:509–511). The block names `absdiff`.
- CP12's "(ans22a §1.4, extended from G-VER of record to the campaign)": §1.4's words are "no end other than PASS is
  Code's alone" (ans22a:26); "every end but PASS goes to the seat and the PI", which §5 quotes, is ans22a:8.
- §3's point 1 cites LOCK:361 for the delta the BUILD's entry declares. That line speaks of a gate re-run's delta;
  the BUILD's move of the pin is LOCK:356–358 and :382, which the seat cites beside it (ans23b:24).
- §5's 2.3 cites "4,278 arrays (drv:4653–4657)": the driver's line (drv:4654) names the 138 cells, "120 of 40 rows
  and 18 of 160"; 4,278 is 138 × 31 layers by arithmetic, as CP10 has it.
- §5's 3.6 reads "the excerpt" as "m's form (m:330)": the word is not in m's text; m's form is the confined
  adjudication read (m:271's last sentence; m:318's exception (1)) and its file beside the checkpoint
  (`valence_core/m/stages.py`:272–278). CP8, as sent, already corrects it.
- **CP8's correction (Code's, declared):** CP8 as sent names, for a rendering pause, "the first differing position
  and its two token ids". The package's problem lines never quote a token id (`valence_core/n/ids.py`:688), and G-VER
  of record's record holds none (ans22a:24), so the block drops the token ids: the excerpt gives a rendering pause by
  digest and computes no position. For an untold read the digest is the session's `ids_sha` against BK's, as the
  runner tests it (runner.py:477–479); for N4-T and N4-Ts it is the told or sham sequence's `ids_sha` as found now;
  or the renderer's own refusal, in the package's masked form (`valence_core/n/ids.py`:148–151).

**How §2 was taken.** It was extracted from this session's transcript, a departure declared in the entry that commits
this raw: `sed -n` of the message's record, through `jq` for its content, then `sed -n` of the content's lines 3–21.
Those are the message's own 19 lines, without the delivery wrapper, which names a session by its id.

**What it does not name.** None of the five sections names a path in the home folder or the scratch folder's full
path, once §4's one line is written as above. Scratch files are named S/...

## 1. Code's readings CP1–CP20, as sent

```text
# The N-pod campaign (n v0.2 §8 step 14): Code's PINs CP1–CP20, for routing

Code, PI date 2026-11-23. Built on the read-only spec survey of HEAD `098218c`, which is origin's
(`S/step4b/camp/spec/survey_report_v1.md`, `7f728f96…43d1`, 342 lines, the subagent's hand-back by `jq`; its brief
`S/step4b/camp/spec/survey_brief_v1.md`, `c940d92d…6f02`, 105 lines). Its 19 open questions are answered below, the
Q-number in brackets, with Code's own checks of the lines the readings turn on. ★ = the seat's. The route is rt23a
item 3's: the BUILD on these PINs, the spec raw and the starred readings committed for the seat's next thread before
any run, "[go, on the next thread's ruling before any run]". Every other PIN is Code's. Nothing goes to the box.

Short forms as in the survey: n = PROPOSAL-n v0.2; LOCK:N = LOCK-n.md at `098218c`, file line (v1.0's part 1–395;
v0.1's L:k = LOCK:395+k); A-n1, A-n3 = the addenda; drv = scripts/n_sessions.py; anl = scripts/n_analyze.py;
runner, schema, cells = valence_core/n/<name>.py; m = PROPOSAL-m v1.11; the raws as the survey names them (ans16b,
ans20b, ans21b, ans21c, ans22a, ans22b, ans23a, rt21b, rt23a, gtrun, gvrun).

## The stage

- **CP1 A `campaign` command in the driver alone [Q1].**
  - `valence_core/n/` does not change: the package and its closure stay LOCK §18's (`06b55761…1d39`, twelve files;
    LOCK:1171–1214). G-READ-n refuses a probe run "under another n package than the campaign's" (anl:6469–6474), and
    ans22b:22 says "The runner and the package do not change."
  - The stage is the package's: `schema.STAGES` holds "campaign" (schema:256); the plan is `schema.read_plan`, 7,680
    reads at `read_plan_sha256` `7f7d7301…88a6` (LOCK:862; drv:3843–3844), ordered by `runner.campaign_order`
    (runner:140–164) and run by `runner.run` (runner:376–555).
  - Options: `--resume` with `--ruling PAUSE_ID=PATH`, since the runner needs a ruling for each standing pause
    (runner:418–428); `--pi-stop PATH` (CP9). No `--smoke` (CP2), and no `--out`: the run of record writes only its
    root and its report (CP10).
- **CP2 ★ No smoke [Q1].**
  - **The texts:** G-TIME-n had one (GT14); G-VER of record had none (GV8). n:97: "every arm runs its full read set;
    there are no looks." A smoke's steered reads would be reads of the campaign's own sessions outside the campaign,
    held under item 2 as G-TIME-n's two steered cells are (ans21b §1.8), which needed a ruling of their own.
  - **The reading:** none. Before the first read the path is checked by the box self-test (CP19), the refusals and
    the weights of record (CP4, CP12), the start's G-VER (CP7) and the runner's own refusals. A refusal before the
    load is a FAIL of the launch, Code's to fix (ans21b:39's form for the smoke's refusals).
  - **For the seat:** whether it wants a smoke, and if so of what (a shadow-only read set in a root outside the
    repository, say), with its cells' handling ruled before it runs.
- **CP3 The identity at "campaign" [Q2].** `gtime_identity`'s fields (drv:3944–3963) with stage "campaign":
  - `lock_sha256` v1.0's `59e0b1bc…00aa` (CP4); the dose map, the fidelity rule with C and the identity bound C, as
    G-TIME-n's lock inputs give them (drv:3894–3941, drv:3857–3863); the package, weights, backend and pod measured as
    G-TIME-n measures them. There is no driver field in the identity (schema:448–481), and no cap field: the cap is
    the runner's input and the report's (schema:1208–1214).
  - `directions`: the 28 directions the campaign injects (schema:302–311): `valence` for N1-V and N1-P; `rand_00` to
    `rand_23` for N1-R; `span_reward`, `span_sentiment` and `span_character` for N2-E, N2-S and N2-C. N4-T, N4-Ts and
    the shadow inject none. Each sha16 is pinned in the driver from LOCK:697–708 (valence `ba4da67fb717b5bb`; the
    three spans rows 1–3 of `directions_L32.npy`; the 24 as G-VEC records them, `random_sha16`).
  - Before the load each unit vector is rebuilt and held to its pin: rows 0–3 from G-VEC's committed directions file
    at its record's sha256 (as `gcal_gvec_inputs` holds row 0 now), and the 24 drawn by `keys.random_directions`
    (LOCK §21: "the keys'"), each sha16 the pin. A miss refuses (exit 1, INTEGRITY: CP12).
  - The realized fidelity sample (15 of 160, `3c70f5ff…a81d`) and N4's schedule (`228ab470…55f3`) are re-derived by
    `keys` at the start, as LOCK §5 forms them (LOCK:805–817), and refused unless equal (ans20b:32: the sample pin
    "lets the campaign's report be checked against the lock").
- **CP4 The lock pin moves, one pin [Q3].**
  - **The texts:** "Step 14's BUILD moves the pin to this file's committed sha256" (LOCK:358); "its lock sha256, the
    cap's 14,400,000 ms" (LOCK:382); a gate re-run "would move the pin first" (LOCK:361).
  - **The reading:** the one `LOCK_SHA256` (drv:3820) becomes `59e0b1bc…00aa`, and every stage's lock check reads it
    (G-TIME-n's, G-VER's and the campaign's). The v0.1 wording at drv:3816, :3914, :4292, :5407 and :5549 ("not LOCK-n
    v0.1's (GT4)", "under LOCK-n v0.1", "LOCK-n v0.1's sha256 (GV4)") becomes the lock in force's. The other `LOCK_*`
    pins are v1.0's unchanged, since v1.0 carries v0.1's text beneath (LOCK:393–394).
  - G-TIME-n's and G-VER's records stay of record as committed under v0.1 (LOCK §5). The campaign's path reads neither
    (Code's check by tool at the BUILD). A re-run of either would be under v1.0's pin, and after v1.0 a box change is
    a new lock version anyway (LOCK:191–194).
  - This also clears the tree's present state: with LOCK-n.md v1.0 and the pin v0.1's, the self-test, `gtime` and
    `gver` refuse at HEAD (LOCK:359–361; the survey's 2.4 and 4.2). No battery window is asked before the draft that
    moves the pin.
  - **The driver of record:** v1.0 §4's driver (`55885e65…385f`, at `d714372`) is the driver at the lock. The
    campaign's STAGE line prints the BUILD's driver blob and the BUILD's entry names it: m-F3's convention "since the
    `time` wiring" (results/raw/2026-11-15_lock-m-f3-v1_design-to-code_answers.md:43), the seat's to confirm for n.
- **CP5 The cap [Q4].** A driver constant `LOCK_HOUR_CAP_MS = 14_400_000` (LOCK:104–123: "4 × 3,600,000 =
  **14,400,000 ms**"), passed as `StageInputs.hour_cap_ms`; a resume keeps it (runner:412–416). The lock's sha256
  binds the text, the constant the value; the self-test holds the constant to the committed lock's §2 line. The CAP
  end state is the runner's (runner:467–469, :536–537): "A CAP end state ends the campaign; a resume refuses another
  cap" (LOCK:122–123). Its exit is CP12's. The 8 h pod budget is the PI's and is enforced by no code (LOCK:119–121;
  box:31); the launch prints each invocation's wall time.

## The run

- **CP6 ★ "All arms, no looks" while it runs [Q5].** The order is the runner's ORDER (LOCK:1251–1253). No session
  reads a margin before the campaign's last invocation has ended and its cells are committed:
  - the driver's stdout is n:130's (session index, arm, dose, the fidelity value against TAU, timing; runner:475,
    :509–511), and the end-wait is on the PID alone (item 5);
  - between invocations the report (the read domain, no margins; n:130) is read for its end state, its standing
    pause and the cap's `used_ms`, and for nothing else, in every session;
  - cells and arrays are checked by name and digest alone (ans22b §1.3 (ii)); the copy-back prints digests and
    counts, never content.
  For the seat: whether this is "no looks" as n means it, and whether the pod session and the coordinating session
  may read more of the report between invocations.
- **CP7 G-VER at the start and at each resume [Q18].** The stage's own, not of record, "before any read" (LOCK:938;
  GV7: "its STOP is the campaign's `no-arm:gver-stop` cause"; ans22a §1.1). Its form is G-VER of record's (drv:253–260):
  the eight non-shard files hashed against the model manifest's pins, tokenizers 0.22.2 held, MANIFEST.json's pin,
  then `verify.verify`. It is stricter than GT7's decode-only form, and already built. Each resume runs it again
  before its load: "one load and one G-VER each" (ans21c:33).
- **CP8 ★ The pauses, and "the excerpt" [Q6].**
  - A fired monitor ends the invocation for every arm (LOCK:933–934): end state PAUSE, exit 3, the report carrying the
    pause's record (schema's pause form: kind, read id, launch index, arms, `also_fired`).
  - **The excerpt** ("its pauses to the seat on the excerpt", ans22b:32, ans23a:53). m's is a confined adjudication
    excerpt, a file beside the checkpoint holding the fired round and the harness lines around it (m:271's last
    sentence; m:318's exception (1); valence_core/m/stages.py:272–278); the word is not in m's text, so the survey's
    "m's form (m:330)" is corrected here. n generates nothing (n:16), so Code reads n's excerpt as: the pause's record
    from the report; the paused read's stdout lines; and the monitor's own figure against its bar: k of n above TAU
    in the tile for a binomial fire; the fidelity value against C for a ceiling; the d = 0 figure against C for the
    identity bound; the first differing position and its two token ids for a rendering pause; the path for a
    non-finite number. Never a margin (n:130). A file in m's form, under `data/n/reports/`, only if the seat asks.
  - No conditional rulings in advance unless the seat issues them (the precedent:
    results/raw/2026-11-18_n-step4-bext2-p01_conditional-ruling.md). The chance of at least one false pause over the
    campaign is 0.3827 (LOCK:1070–1074).
  - The ruling's route: the seat's raw committed by path in a window; the resume in a fresh sparse copy at that
    commit, with the run's report, cells and arrays copied in by name and checked by sha256 (R:7842–7847's form). The
    runner records the ruling file's sha256 (runner:420–421).
  - For the seat: the excerpt's content, and whether it pre-rules any pause kind.
- **CP9 ★ The STOP reports, and the PI's stop [Q7].** The runner writes no STOP (runner:363), and nothing resumes
  after one (runner:330–331).
  - (a) **The start's G-VER STOP:** the driver writes G-VER's report `data/n/reports/campaign_gver_stop.json` and
    the campaign's report in the schema's G-VER-STOP form: no pause, no record, `rendering_mismatches` G-VER's
    mismatches (at least one), and the stop record {kind, `record_sha256` that file's, detail of at most 200
    characters} (schema:1195–1199, :1533–1537). It is checked by the schema before it is written, so that the
    analyzer's `no-arm:gver-stop` has its input (anl:6710–6719). On a PASS, G-VER prints its lines, as at G-TIME-n.
  - (b) **A G-VER STOP at a resume,** after reads exist, cannot take that form (no record allowed). The resume
    refuses before its load, the report stays as the last invocation left it, and it is a STOP for the seat
    (LOCK:938).
  - (c) **The PI's stop:** `campaign --pi-stop RAW` writes end state PI-STOP only while a pause stands (schema:208–210),
    the stop record citing the committed raw's sha256 (schema:1197); no load. n:134 names "a PI stop" among the
    NOT-RUN causes, and nothing writes one now.
  - For the seat: the three forms.
- **CP10 What is written where [Q8].**
  - The root `data/n/ckpt/campaign/` (138 cell JSONs, "120 of 40 rows and 18 of 160", drv:4654; their 4,278 arrays,
    138 × 31 layers) and the report `data/n/reports/campaign.json`, on the stages' pattern (drv:617–618, :3796–3797).
  - The BUILD's `.gitignore` admits the 138 cell JSONs, the report, G-VER's STOP report, and GT11's two lines for
    G-TIME-n's steered cells (ans21b §1.8), tested in a scratch repository. Never the arrays (A-n1:54; schema:74–89;
    ans16b:41). The comment at .gitignore:335–337 ("stay on the box's volume") is corrected.
  - On the laptop the arrays are held outside the repository, beside G-TIME-n's, named at the copy-back; their
    sha256s go in the close's raw (digests are item 1's).
- **CP11 ★ The close: "raws and checkpoints committed before the pod stops" (n:159) [Q9].**
  1. The last invocation ends (COMPLETE, CAP or a STOP).
  2. The copy-back by name (CP14).
  3. G-TIME-n's two steered cells are placed by name from their holding folder into `data/n/ckpt/time/`, and their
     sha256s are checked against G-TIME-n's report (`fa823370…10c0`, `63634361…9968`; LOCK:386). That is the copy's
     own hash check, the one ans21b §1.8 excepts.
  4. They are committed by path in the same commit as the campaign's cells and report (LOCK:385–388), in a window.
  5. The pod stops only after that commit is verified.
  For the seat: the order, and whether step 3's check is the exception ans21b §1.8 means.
- **CP12 ★ The ends: exits and classes [Q11].**
  - Exits: COMPLETE 0, PAUSE 3, CAP 5, G-VER-STOP 6 (report written), PI-STOP 7 (report written), and 1 for a
    refusal or a crash. 2 is left to Python's usage errors (F5's lesson at G-VER: the launch reads each end by its
    exit, its last line and the report).
  - Classes: a hash or byte-count refusal (the weights, the model manifest, the eight files, the lock, G-VEC's and
    G-CAL-n's files, the package and its closure, a direction's sha16) is INTEGRITY: stop, touch nothing, escalate
    (ans22a §1.4; ans22b §1.4). An environment or launch refusal is a FAIL of the launch, Code's to fix. A crash
    leaves the cells replayable (runner:12–15), "a crashed invocation's absent load" a declared gap (A-n3:60).
  - Every end but COMPLETE goes to the seat and the PI (ans22a §1.4, extended from G-VER of record to the campaign).
  - For the seat: the codes, and the extension.
- **CP13 ★ One pod session: a restart, a box change [Q12].**
  - The identity holds the pod and the backend identifier (LOCK §17; schema:458–459: "a pod change refuses a
    resume"). Before each invocation the launch checks that the pod has not restarted since the last (gvrun:42–63's
    form). A restart is reported to the seat and the PI, and nothing runs until they rule (CLAUDE.md's respawn
    protocol).
  - A box change aborts the campaign (m:251: "no splicing"); after v1.0 it is "a new lock version" (LOCK:191–194;
    ans22a:33). The aborted run's report and cells are committed as they stand (rule 27). The new version's Clock is
    the PI's: n:152 dates v1.0 alone.
  - For the seat: a restart on the same pod id, and the aborted run's record.
- **CP14 The copy-back by name [Q10].** The names: the report's `cells` (138), and for each `schema.capture_filename`
  over layers 33–63 (31 each); the report; G-VER's STOP report if any; the run's stdout and exit raws. No listing of
  `data/n/ckpt/campaign/` on the box or the laptop (ans22b §1.3 (ii)). Each JSON is held to the report's
  `json_sha256`; each array is hashed by name on the box and again on the laptop; the transfer goes by an explicit
  list, with no `._*` (the analyzer refuses stray files, anl:3199–3203). The self-test's temporary folder is on the
  box's local disk and refused under `/workspace` (ans22b §1.3 (i); R:1131–1140).
- **CP15 G-READ-n's inputs [Q13, Q17].** Every array comes back (A-n1:54). The package is frozen through the campaign
  and G-READ-n (anl:6469–6474). G-READ-n's command is built at step 15. A-n3:60's "committed at step 14" is read as
  the campaign's cell files and its report; G-READ-n's artifact is step 15's, on the laptop (n:121, n:159). The seat
  may read A-n3:60 otherwise.
- **CP16 ★ The push before VERDICTS [Q16].** The cells hold margins; "a push publishes them" (ans21b:29), and the
  screen halts on any match under ckpt (item 4). The close commit is not pushed before VERDICTS unless the PI says
  so (rule 27 is met by the commit; origin is public).

## The BUILD

- **CP17 The entries [Q14].** n:161 names none for step 14. Code's names: "N-pod campaign — BUILD (n v0.2 §8 step
  14)" for the BUILD, and "N-pod campaign (n)" for the close. The seat may rename them.
- **CP18 The box's cleanup [Q15].** Nothing on the box is removed before the close commit is verified. G-TIME-n's
  smoke folder and the run copies stay until the PI's word after the close (R:2799; gtrun:226–227).
- **CP19 The self-test.** The driver's self-test gains the campaign's cases: the identity and its 28 directions, the
  cap's constant against the lock, the three STOP writers and the exits, the refusals, the start's G-VER, the
  copy-back's names from a report, and box safety (the traps of drv:5007–5025). Its count follows the BUILD, run in
  battery windows. On the box its temporary folder is local (CP14).
- **CP20 The route [Q19].** rt23a item 3, as at G-TIME-n and G-VER:
  - a seat block (these readings; the routing by `jq`; the brief with its repository path as `<repo>`; the report)
    committed by path in a window, ahead of the BUILD's commit;
  - drafts in scratch, self-tests in battery windows, one blind review, one values-check, and the BUILD's commit
    window;
  - launch files to the coordinating session first, nothing to the box before "launch cleared", and the run after
    the seat's ruling on the starred eight. Ledger (88): the seat opens `main`'s command list before routing a launch
    (ans22a:84).
```

## 2. The coordinating session's routing, with the PI's answer

```text
The PI's word on step 14's route: "Build on the PINs". Build on CP1–CP20 now, by your CP20's route.

The PI's answer, verbatim: "Build on the PINs" (17 bytes). It is the wrap-up button of my ask "Build step 14 on n-build's PINs now, with the starred eight to the seat before any run?"; the other button was "Seat first". PI date 2026-11-23. Saved on receipt in my scratch, sha256 2232e004…a989.

Checked by tool before this relay:
- no untracked file under results/raw;
- HEAD = origin main = 098218c;
- your readings note re-hashed equal (fd80cf43…23b0, 190 lines);
- valence_core/n/ unchanged from ef105f1 to HEAD (0 names by name-only diff).

What it routes, as rt23a item 3 and your CP20 give it, in the G-TIME-n and G-VER form:
1. The BUILD on CP1–CP20 now: the driver only, the package 06b55761…1d39 unchanged, drafts in your scratch.
2. The seat block first: your readings, the routing by jq, the brief with its repository path as <repo>, and the report, committed by path in a window I grant ahead of the BUILD's commit. Send me its window request with every sha256; I check each input by tool before the grant. That commit needs no further PI word. The PI's word governs only the nudge to the seat's next thread, which I put to the PI once the block is committed.
3. Self-tests in battery windows, one at a time, each requested with its sha256s; one blind review; one values-check; then the BUILD's commit window.
4. The starred eight (CP2, CP6, CP8, CP9, CP11, CP12, CP13, CP16) go to the seat's next thread in that block. No run before its ruling: item 3's "[go, on the next thread's ruling before any run]".
5. The launch files come to me first, carrying item 3's "three requirements, the INTEGRITY correction and the steered cells' commitment". Nothing goes to the box before "launch cleared".
6. Nothing pushed.

The pod session is not messaged; nothing goes to it before the launch files.
```

## 3. Code's addendum to the readings: the seat's eight points set against them

```text
# The N-pod campaign (n v0.2 §8 step 14): Code's addendum to CP1–CP20, the seat's eight points set against them

Code, PI date 2026-11-23. The seat's raw of its second sitting of 2026-11-23, the first of a new thread
(`results/raw/2026-11-23_n-lock-v1_0-committed-close_design-to-code_answers.md`, `e07fba2c…eba9`, 68 lines, placed
untracked), §2 lists "the lines the starred readings will be ruled against, named now so that n-build's PINs can
carry them", and its routing item N.2 asks for "§2's eight points carried into the PINs", routed by the PI's "Route as
given" (relayed by the coordinating session on 2026-11-23). Each point is set against
the readings as sent (`fd80cf43…23b0`). No PIN changes; two readings gain a sentence each (points 4 and 5). Short
forms as in the readings; seat:N is the seat's raw's line N.

1. **The lock** (seat:24): CP3 and CP4. The identity carries `lock_sha256` `59e0b1bc…00aa` and no other; the BUILD
   moves the one pin from `88d9fe7b…e9d5` (drv:3820), in a delta its entry declares (LOCK:361); no gate re-runs in
   the interval. Carried as sent.
2. **The cap** (seat:25): CP5. `LOCK_HOUR_CAP_MS` 14,400,000 = 4 × 3,600,000 (LOCK:106); a CAP end is an end state
   (LOCK:949), not resumable under another cap. As built, a resume after a CAP end is refused before any load, the
   campaign over (LOCK:122–123): the cap is a guard, not a target (seat:25). Carried as sent.
3. **The order and the plan** (seat:26): CP1 and CP6. The runner's ORDER (LOCK:1252) and `read_plan_sha256`
   `7f7d7301…88a6` (LOCK:862), 7,680 reads, 48 tiles of 160 with no tail (LOCK:1070); the BUILD holds the plan's
   count and sha256 to the lock's before any load. Carried as sent.
4. **The monitors** (seat:27): the runner's own, unchanged (CP1: the package does not change), as LOCK:936–950's
   table and v0.1 §13 (LOCK:1041) have them, the kinds' order at LOCK:931; no looks (CP6). The sentence "Every
   pause comes to the seat on the excerpt, in its own raw" (seat:27) refines CP8's route: each pause's excerpt (the
   driver's EXCERPT lines, with the paused invocation's lines around them) is committed as its own raw, one for each
   pause, for the seat's ruling.
5. **The campaign's own G-VER at its start** (seat:28): CP7 and CP9. "Every end but PASS of any stage on the box goes
   to the seat and the PI before anything else runs there (ans22b §1.4)" (seat:28) is CP12's extension, now in the
   seat's words, so CP12 cites it beside ans22a:8; at the campaign, COMPLETE stands in PASS's place.
6. **The launch files** (seat:29): CP14 and CP20 (LOCK:382–385; ans22b §1.3–§1.4): the self-test's temporary
   folder on the box's local disk, every cell checked by name and digest, no cell root listed or counted, the
   copy-back by name, the weights folder missing classed INTEGRITY, and "launch cleared" before the pod session runs
   anything. Carried as sent.
7. **The close** (seat:30): CP10, CP11 and CP14 (LOCK:385–389): the campaign's cells committed by path before the pod
   stops, with G-TIME-n's two steered cells' JSON; every capture array stays on the box until then, and none is ever
   committed. Carried as sent.
8. **The route to the seat** (seat:31): CP20. The spec raw first, in `2026-11-21_n-gtime_spec.md`'s and
   `2026-11-22_n-gver_spec.md`'s form (the readings and the coordinating session's routing verbatim, the starred
   readings marked), with its entry; then the starred block, read whole with the spec raw; the seat rules in one
   sitting; the unstarred readings stay PINs for the BUILD's read. Carried: the spec raw and the block go in one
   commit with their entry, ahead of the BUILD's commit.
```

## 4. The survey's brief

```text
You compile, read-only, the full specification of one stage of the jspace-lab repository (at
<repo>, HEAD 098218c), so that Code can build it: **the N-pod campaign**, step 14
of PROPOSAL-n v0.2's §8 order, which gives it one sentence (n:159): "The N-pod campaign within one pod session (all
arms, no looks), raws and checkpoints committed before the pod stops." Step 13, LOCK-n v1.0, is committed at 098218c;
its sha256 is the campaign identity's `lock_sha256`. The stage command is not built: scripts/n_sessions.py says (its
line 285) "Stages the campaign and G-READ-n are wired at their own steps.", and its lock pin (lines 3819–3820) is still
LOCK-n v0.1's. The package valence_core/n/ already carries the stage "campaign" (schema.py:256), its read plan
(schema.py:585–606) and the runner's `campaign_order` and `run` (runner.py:140, :376). The PI's routing of the seat's
last sitting (results/raw/2026-11-23_first-sitting_pi-routing.md, item 3) names the BUILD: "step 14's BUILD (pins
moved to v1.0's committed sha256; hour_cap_ms 14,400,000; the campaign's stage command)", and its launch files
"carrying the three requirements, the INTEGRITY correction and the steered cells' commitment". You run no interpreter
of any kind (no python, python3, node, perl, awk), write no file anywhere, and return your report as your final
message.

WHAT TO FIND, with a file:line citation for every claim:
1. The specification as the texts state it:
   - PROPOSAL-n-bk-reconciliation-v0_2.md: §0.4 (about line 16), §2.4 "Arms and reads (N-pod)" (about line 83), §2.7
     the hours and the pod budget (about line 101), the LOCK-n paragraphs of §3, G-READ-n (about line 121), §5's
     verdict, NOT-RUN and Clock rules, §8's step 14 (line 159) and its entries list (line 161), and anything else that
     names the campaign, the N-pod, "no looks", the one pod session, the cap, a pause or a STOP during the run, or what
     is committed before the pod stops;
   - LOCK-n.md (v1.0, committed at 098218c): the v1.0 part (lines 1–395) whole; beneath it LOCK-n v0.1's text, whose
     line k is the file's line 395+k: its §0, §5 (the keys), §6 (the arms and read sets), §7, §8 (the identity bound),
     §10 (every trigger with its bar), §11 (the pod budget's split), §13, §15, §16, §17, §18 (the package of record and
     its closure), §21, §22, §23 and §24; and every line that names the campaign (39 lines; among them 336, 352–388,
     503, 525, 858–875, 938–954, 988–989, 1070–1103, 1164, 1352, 1383–1392 and 1428);
   - ADDENDUM-n1, ADDENDUM-n2 and ADDENDUM-n3, each at the repository root, wherever they bind the campaign (the
     rendering of record, G-READ-n's band, fidelity on the box of record, the capture convention, the reward gate, the
     interval);
   - every item in the seat's answers raws and the PI's routing raws under results/raw/ dated 2026-11-15 to 2026-11-23
     whose names hold "n-", "sitting" or "routing" that binds the campaign or its launch: among them the launch-file
     requirements and the INTEGRITY correction (results/raw/2026-11-22_n-gver-record-read_design-to-code_answers.md
     §1.3–§1.4), the steered cells' commitment (results/raw/2026-11-23_n-lock-v1_0-read_design-to-code_answers.md §3
     edit 2 and §4, and the rulings they cite: ans21b §1.8, rt21b item 2), the cap (the third sitting of 2026-11-21),
     G-VER's place before any read, the box of record and a box change (ans21b §1.7, ans22a §1.6), "its pauses to the
     seat on the excerpt" (the 2026-11-23 raw's §4), and G-TIME-n's Q8 on its two steered cells;
   - RESULTS.md's entries that bear on the campaign: "LOCK-n v1.0 — COMMITTED" (098218c, at the Log's head), the
     "G-VER (n)" entry (fd5d61c) with its production observations on the runner's cell roots and the campaign's launch
     files, G-TIME-n's entries (the projections, its launch files, the copy-back, the two steered cells), the G-CAL-n
     and BACKEND-extension runs (the stage pattern on the box), and the n package BUILD entry.
2. What already exists in the code that the campaign could use or must match:
   - valence_core/n/runner.py: `campaign_order`, `run` (resume, the cap, the pauses, the report, the cells and how
     they are written), `StageInputs`, `Monitors`, and its self-test's campaign cases;
   - valence_core/n/schema.py: STAGES, the stage identity's fields (`lock_sha256` at :453 among them) and their null
     rules for stage "campaign", `read_plan` and `read_plan_sha256`, the report and cell forms, the record checks'
     campaign rules, and anything else that names the campaign;
   - valence_core/n/cells.py, sessions.py, ids.py, verify.py, primitive.py, probe.py, keys.py and directions.py: what
     the campaign calls and what it writes (the cells, the captures G-READ-n reads);
   - scripts/n_sessions.py: each stage command as a template (`cmd_gtime` with its options, `cmd_gver`, `cmd_gcal`,
     `cmd_gvec`, `cmd_backend_ext`); their common pieces (the refusals, the weights of record, the driver of record,
     the ids of record, the provenance bridge R6, the stage identity, the pins: `LOCK_PATH` and `LOCK_SHA256` at
     :3819–3820 and every other pinned digest); the G-VER each stage runs before its load; the printing rules; the
     self-test's structure (its check count, its box-safety traps); every line that names the campaign (51 lines); and
     every place `LOCK_SHA256` is read, since moving it moves the gtime and gver commands' checks too;
   - scripts/n_analyze.py: what VERDICTS and G-READ-n read from the campaign (the identity's `lock_sha256` check at
     :6687–6689; the report and cells it expects and their paths; the NOT-RUN and Clock causes), so that the campaign
     writes what the analyzer reads;
   - the committed launch raws of G-TIME-n's and G-VER's box runs under results/raw/ (their launch scripts' names and
     sha256s, the checks they made on the box, their copy-back), as the launch files' template; and the root
     .gitignore's lines for data/n/.
3. What the texts leave open for a build: every point Code would have to decide that no text decides, stated as a
   question with the texts that come nearest. Do not decide them. At least: the command's name and options (smoke,
   resume, rulings, out); the identity's fields for stage "campaign" and where each comes from; how the lock pin moves
   (one constant for every stage, or the campaign's own) and what that does to the gtime and gver commands; how
   `hour_cap_ms` is enforced and what a cap hit ends as; the order of arms and reads and what "all arms, no looks"
   bars during the run; the pauses and STOPs during the run, who reads them, on what, and how the run resumes; G-VER at
   the campaign's start; what is written where (cells, captures, report), what is committed and when ("raws and
   checkpoints committed before the pod stops"), and G-TIME-n's two steered cells' commitment at the close; the
   copy-back by name and digest without listing a cell root; the self-test's temporary folder on local disk;
   INTEGRITY versus FAIL ends; what a crash, a restart or a box change inside the one pod session does; and what
   G-READ-n needs the campaign to leave.
4. Anything that would make the campaign need the seat or the PI before it runs (a missing input, a conflict between
   texts, a reading that must precede the run).

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
  is read, listed or hashed (G-TIME-n's two steered cells are held outside the repository under item 2 until step
  14's close: you do not look for them).
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

## 5. The N-pod campaign's specification as the texts state it (the survey's report, as returned)

```text
SURVEY — the N-pod campaign (PROPOSAL-n v0.2 §8 step 14), read-only, at HEAD 098218c

Abbreviations (repository paths only): n:N = PROPOSAL-n-bk-reconciliation-v0_2.md; LOCK:N = LOCK-n.md at 098218c, file line (v1.0 part 1–395; v0.1's L:k = LOCK:395+k); A-n1/A-n2/A-n3:N = the three ADDENDUM-n files at root; drv:N = scripts/n_sessions.py; anl:N = scripts/n_analyze.py; runner/schema/cells/probe/keys:N = valence_core/n/<name>.py; R:N = RESULTS.md at 098218c; m:N = PROPOSAL-m-gating-campaign-v1_11.md. Raws under results/raw/: ans15 = 2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md; ans16b = 2026-11-16_n-build_…; ans16g = 2026-11-16_n-ganl_…; ans18c = 2026-11-18_n-step4-run-pause_…; ans18d = 2026-11-18_n-step4-resume_…; ans19 = 2026-11-19_n-starred-twelve_…; ans20b = 2026-11-20_n-lock-v0_1-read_…; ans21b = 2026-11-21_n-gtime-starred-seven_…; ans21c = 2026-11-21_n-gtime-record-read_…; ans22a = 2026-11-22_n-gver-starred-seven_…; ans22b = 2026-11-22_n-gver-record-read_…; ans23a = 2026-11-23_n-lock-v1_0-read_… (all …_design-to-code_answers.md); rt21b/rt21c/rt22b/rt23a = 2026-11-21_second-sitting_, 2026-11-21_third-sitting_, 2026-11-22_second-sitting_, 2026-11-23_first-sitting_pi-routing.md; box = 2026-11-18_box-gpu_design-to-code_answers.md; spec22 = 2026-11-22_n-gver_spec.md; gtrun = 2026-11-21_n-gtime-v1_run.txt; gvrun = 2026-11-22_n-gver-v2_run.txt; gvout = 2026-11-22_n-gver-v2_out.txt.

Checked at this read: HEAD 098218c; LOCK-n.md sha256 59e0b1bcb364af06630753ba09fde127518c451e0aa679cea1d979d0ec9900aa (shasum), last changed at 098218c, committer date 2026-11-23, so D_n 2026-12-15 is met; the driver 55885e65…385f (unchanged since 2834c2d), the analyzer v7 735da934…a7a8 and schema.py 1cab28df…edff, each equal to LOCK:161–162, :212–215; valence_core/n last changed at ef105f1; those paths clean; no untracked file under results/raw/.

## 1. The specification as the texts state it

1.1 PROPOSAL-n v0.2
- Step 14 (n:159): "14. The N-pod campaign within one pod session (all arms, no looks), raws and checkpoints committed before the pod stops." Step 15: "G-READ-n from the captures; then analysis in a later session on the PI's word". The entries list (n:161) names no entry for step 14 and none for its BUILD; it ends "…NOT-RUN where §5 requires one; adjudication entries as fired."
- §0.4 (n:16): "Every campaign read is one forward over a fixed token sequence; nothing is generated under steering in the campaign." The exposure table is at n:18–26 ("struck beyond d = −1": 48 / 320 / 960), and n:28 says "The VERDICTS entry reports the realised counts".
- §2.1 (n:77): the read is m = log p(S) − log p(U). The fidelity re-computation covers every read at d ∈ {0, +1, −1} plus a 10% keyed sample `n-fid|{s}`; "a fire pauses and the seat adjudicates (rule 21); the primary analysis is ungated". The identity check is at d = 0.
- §2.2 (n:79): the residual is captured "on every forward, for G-READ-n".
- §2.4 (n:83–95): the arms table.
- §2.5 (n:97): "No optional stopping: every arm runs its full read set; there are no looks."
- §2.7 (n:101): "Pod budget proposed: 8 h for N-pod, the cap set by the PI at LOCK-n v1.0 … the campaign within one pod session (m:251 carried: a box change restarts the campaign; gate stages may span boxes)." m:251: "a mid-campaign box change aborts and restarts that checkpoint's campaign; no splicing … raw outputs and checkpoints are committed before any pod instance stops (rule 27), under §4's blinding rule".
- §2.8 (n:103): the resume identity is "this document's hash, the lock hash, the session set's hash, the directions' shas, the dose map's figures, the backend identifier and the pod instance id … a resume is skip-only; checkpoints atomic; raws and checkpoints committed before any pod instance stops (rule 27)".
- §3: G-VER (n:119), "before any read; mismatch → STOP". G-READ-n (n:121) is "computed after the campaign from the captured residuals, before VERDICTS". G-LEAK-n (n:122) is computed with VERDICTS.
- §4 (n:130): "who sees margins before VERDICTS: nobody. Margins go to checkpoint files; stdout prints session index, arm, dose, the fidelity value against TAU, timing — never a margin".
- §5 (n:134): "A unit is NOT-RUN iff its LOCK v1.0 is not committed by its Clock date (…), or it is locked and produces no arm's full read set before a PI stop, a G-VER STOP or its cap. An arm with a partial read set is INDETERMINATE; a locked unit that completes any arm is analyzed on what it obtained." N1 and N2 are INDETERMINATE "iff an unadjudicated pause stands" on their reads (n:136, n:140).
- §6 (n:148): "No looks (§2.5). Pause-and-adjudicate: the fidelity binomial (§2.1); a rendering mismatch; NaN/inf; the identity bound exceeded at d = 0 … Every pause STOPs the arm's launches until adjudicated; Code never self-adjudicates; verdict criteria are untouchable (rule 21)."
- §7.4 (n:152): D_n 2026-12-15, measured on the committer date of LOCK v1.0. No text sets a date for the campaign itself.

1.2 LOCK-n v1.0 part (LOCK:1–395)
- Status (LOCK:3–4): "…of record from that commit, superseding LOCK-n v0.1; the lock the N-pod campaign follows."
- §1 (LOCK:73–100): T = 1.0494 h at the medians, 1.6334 h at the maxima. The I/O is 0.9–2.6 h, "outside the cap". The copy-back runs at "15.5 MB/s, so the campaign's 4.9–5.0 GB … is about 5–6 minutes" (LOCK:92–93). G-READ-n takes 2.650 h on the laptop, "after the campaign".
- §2, the cap (LOCK:104–123):
  - "4 h of model time"; "`hour_cap_ms` (runner.py:266): 4 × 3,600,000 = **14,400,000 ms**, the runner's input from the lock … Step 14's BUILD is to pass it (unbuilt; G-TIME-n's stage passed none, n_sessions.py:4373), and a resume keeps the stage's cap (runner.py:413–414)".
  - The cap counts the reads' and re-computations' model time; the loads are outside it.
  - The budget line: "the 8 h N-pod budget … 4 h of cap + up to 2.6 h of I/O + the loads and G-VER + the copy-back's minutes, with margin for a pause and its resume" (LOCK:119–121).
  - "A CAP end state ends the campaign; a resume refuses another cap … so a cap that binds is a new lock version, not a longer session." (LOCK:122–123)
- §4 (LOCK:160–165): the driver at d714372 (55885e65…) and the package 06b55761…1d39.
- §5 (LOCK:167–208):
  - G-VER of record is d1dcc337…e90a at fd5d61c, "PASS, 160 of 160".
  - "The box of record is unchanged through the chain: pod `emw1e4embiwe9b` … a box change before the campaign re-runs the characterization, the extension, G-TIME-n and G-VER, in that order …, and after this commit is a new lock version." (LOCK:191–194)
  - "The campaign's own G-VER at its start stays the row's "before any read"" (LOCK:208).
- §6 (LOCK:217–221): VERDICTS checks the lock's sha256 against the identity's `lock_sha256`.
- §12 (LOCK:352–361):
  - "The driver pins LOCK-n v0.1's sha256 now (`LOCK_SHA256`, n_sessions.py:3820) … Step 14's BUILD moves the pin to this file's committed sha256".
  - "Between step 13's commit and step 14's BUILD those checks refuse on this tree … No gate re-run is scheduled in that interval; one would move the pin first, in a delta Code declares in its entry."
- §13 (LOCK:381–389): the BUILD "moves the driver's pins to v1.0 (its lock sha256, the cap's 14,400,000 ms)". The launch files carry:
  - "the self-test's temporary folder on the box's local disk";
  - "every cell checked by name and digest, no cell root listed or counted";
  - "the copy-back by name";
  - "the weights folder missing on the box of record classed INTEGRITY, not a launch FAIL";
  - G-TIME-n's two steered cells' JSON (`N1-V__valence__p1.json` fa823370…10c0, `N1-V__valence__p1_2.json` 63634361…9968), "committed by path with the campaign's own cells at step 14's close, before the pod stops".
- Where v0.1 differs, v1.0 is of record (LOCK:393–394).

1.3 LOCK-n v0.1's text, beneath
- §1 (LOCK:576–640): MANIFEST 53a8cd74…99d8; the label convention "space"; N4's join.
- §2 (LOCK:644): the session set be50011a…ba84.
- §3 (LOCK:655–733): Route B, site 32. The valence direction is `ba4da67fb717b5bb`. N2's three are `span_reward` 8f32921fcd1798db, `span_sentiment` f4136430145a2960 and `span_character` 006f5174a82193f9 (LOCK:699–701). The 24 random sha16s are at LOCK:702–708.
- §4 (LOCK:735–785): R 25.54500811131038, R_ℓ 21.98789170395024, d_eq 0.2869170055735837, d_20 0.5738340111471674; seven points, none merged.
- §5 (LOCK:787–825): the realized fidelity sample is "15 of 160 sessions", digest 3c70f5ff…a81d (LOCK:805–810). N4's schedule is 228ab470…55f3 (LOCK:811–817).
- §6 (LOCK:827–877):
  - 7,680 reads; `read_plan_sha256` 7f7d7301…88a6 (LOCK:862).
  - Captures on every forward, 31 layers 33–63, "one array per cell per layer" (LOCK:855–857, :869).
  - A-n3:60's OPEN 1 (LOCK:873).
- §7–§8 (LOCK:879–908): TAU, p0 1/26, C = 0.25.
- §10 (LOCK:928–978):
  - "A fired monitor ends the invocation for every arm, and the resume after the ruling continues all" (LOCK:933–934).
  - The G-VER row, "before any read": "…a STOP for the seat, never a pause and never an exclusion; no read is launched and the campaign does not start" (LOCK:938).
  - The pause rows (LOCK:944–948).
  - The cap row: "the stage's records' summed `duration_ms` against the lock's cap (v1.0's, the PI's) | CAP end state" (LOCK:949).
- §11 (LOCK:980–1003): the budget 8 h; the one pod session (LOCK:988–989); the split of record (OPEN 2).
- §13 (LOCK:1041–1074): the tile sentence; alpha 0.01. "**E = 48** … **1 − 0.99^E = 0.3827098590577118**", "the chance of at least one false pause over the campaign" (LOCK:1070–1074).
- §17 (LOCK:1141–1169):
  - The backends: "n on H100 SXM pod `emw1e4embiwe9b`, identifier `4ed3f2c70fe8afbf`"; n's identifier 8264f719efd347a9.
  - The environment: python 3.12.3, torch 2.8.0+cu128, transformers 5.15.0, tokenizers 0.22.2, `:4096:8`.
  - "A verdict campaign completes on one characterized backend" (LOCK:1164).
  - The weights 36f05404…0fdb.
- §18 (LOCK:1171–1214): the package 06b55761…1d39 and its twelve-file closure.
- §21 (LOCK:1251–1259): the runner's PINs — ORDER, PAUSE, SCOPE, BINOMIAL, NON-FINITE/CEILING/IDENTITY, RENDERING and CAP.
- §24 (LOCK:1392–1393): "The stage commands for G-TIME-n, G-VER and the campaign are wired at their own steps".

1.4 The addenda
- A-n1:54: captures "About 150 MB per layer over 7,360 reads, so about 4.7–4.8 GB: kept on the box's volume during the campaign, copied to the laptop with its hashes before the pod stops (rule 27's spirit: it is a gate's input), never committed to git".
- A-n1:56: where G-READ-n's probe runs is "Code's call … counted in the cap where it runs on the box". A-n1:58 gives the PASS rule. A-n1:24: G-VER runs before any read. A-n1:40: "Nothing is generated in the campaign".
- A-n2:24–26: the ceiling C "pauses at once", and the identity bound is C.
- A-n3:38: `reward_f020` is "the campaign's own injection for N2-E at `f0.20`".
- A-n3:60, OPEN 1: the hash lists are recorded in "the campaign's committed cell files, the stage report's `cells`, G-READ-n's artifact's `campaign.cells`, copied with their hashes before the pod stops and committed at step 14".
- A-n3:60, OPEN 2: the cap clause, and "a crashed invocation's absent load is a declared reporting gap".

1.5 The seat's answers and the PI's routing (2026-11-15 to 2026-11-23)
- rt23a:27–31, item 3: "After the seat's handoff: step 14's BUILD (pins moved to v1.0's committed sha256; hour_cap_ms 14,400,000; the campaign's stage command), its spec raw and starred readings committed for the seat's next thread before any run, as G-TIME-n's and G-VER's were; the launch files carrying the three requirements, the INTEGRITY correction and the steered cells' commitment. [go, on the next thread's ruling before any run]".
  - rt23a:39: the box "up through the campaign. [stays up]".
  - The seat's handoff is "in the project … not the tree" (rt23a:37–38); not read here.
- ans23a:53: "…the campaign in one pod session, its pauses to the seat on the excerpt, G-READ-n, VERDICTS on the PI's word." Its edits 2–4 are at ans23a:44–46, its §5 item 3 at ans23a:63.
- ans22b §1.3 (ans22b:22), the requirements verbatim:
  - "(i) the self-test's temporary folder on the box's local disk, as v2 has it";
  - "(ii) every cell checked by name and digest — the reports name their cells — and no cell root (`data/n/ckpt/<stage>/`) listed, counted or compared against an expected set, since `atomic_write_json` rewrites each cell's JSON on every append and a root on the volume can hold a `.nfs…` name for a moment";
  - "(iii) the copy-back by name, as now … The runner and the package do not change."
  - §1.4 (ans22b:24): the INTEGRITY readings, and the correction: "the weights folder missing on the box of record is INTEGRITY — stop, touch nothing, escalate — not a launch FAIL". Routed at rt22b:25–27.
  - ans22b:32 (§2): "its pauses to the seat on the excerpt".
- ans22a:
  - §1.1 (ans22a:14): "The campaign repeats G-VER at its own start, not of record (GV7); both stand." GV7 as written (spec22:136–138; stands, ans22a:39): "its STOP is the campaign's `no-arm:gver-stop` cause".
  - §1.4 (ans22a:24–29): the ends and the refusal classes. A hash or byte-count refusal is INTEGRITY; an environment or launch refusal is a FAIL of the launch; "every end but PASS goes to the seat and the PI" (ruled for G-VER of record).
  - §1.6 (ans22a:33): "a box change after v1.0's commit is a new lock version carrying the new box's chain".
- ans21b:
  - §1.8 (ans21b:29–34), Q8 option (iii): "no session lists, opens or hashes them before the campaign's cells are committed, the copy-back's own hash check excepted"; "committed by path at step 14's close, with the campaign's own cells and before the pod stops … with GT11's two `.gitignore` lines and the entry citing the report's sha256s"; "the smoke's folder … stays on the box … until the campaign's cleanup". Routed at rt21b:23–26.
  - §1.7 (ans21b:27): after v1.0, a box change's "re-run's projections enter a dated note beside and the cap stands unless the PI re-sets it, which is a new lock version".
  - §2 (ans21b:38–39): GT6's exits, the smoke's two ends, and "A refusal at the smoke is a FAIL of the launch, Code's to fix".
- ans21c:33: the campaign's resumes cost "one load and one G-VER each". ans21c:43–45: the cap. rt21c:21: "[4 h — PI's figure: 4 h]".
- ans20b:
  - :32: the sample pin "lets the campaign's report be checked against the lock";
  - :39: "Cap and alpha as the runner's inputs from the lock, a resume refused under another: accepted";
  - :41: a G-VER-STOP of any cause;
  - :44: the I/O is outside the cap.
- ans19:50–51: R12, R13 ("a ruled ceiling pause clears nothing") and R14.
- ans18c:32: "The blinding binds reading, not the repository … the pre-push screen's halt on `data/n/ckpt/**` is cleared by this ruling … The push itself is the PI's word" — said of backend-ext's cell. ans18c:40: the mf3 exclusion on every git command while Q-F3 runs.
- ans18d:51: the copy-back's address-and-port count, counts only.
- ans16b:41: the captures, "never in git". ans16b:50: "a fired monitor ends the invocation for every arm", and the cap clause.
- ans16g:50: PIN-n-24, "complete means every planned read produced, finite or not".
- box:14, :31: no splicing; "The spend is the PI's at every step."
- The other raws in the range bind Q-F3 or p, not this campaign. One is a precedent: the m-F3 lock's driver convention (results/raw/2026-11-15_lock-m-f3-v1_design-to-code_answers.md:43).

1.6 RESULTS.md
- R:24–35 and R:156–160: v1.0's commit, and "Next: step 14's BUILD".
- R:1131–1140: G-VER v2's fix, TMPDIR on `/tmp`, refused under `/workspace`.
- R:1202–1220, the production observations: a cell root on the volume "can briefly hold a `.nfs…` name"; "The campaign's launch files (step 14), on that reading: cells checked by name, never a root's listing; the self-test's `TMPDIR` on the local disk; the copy-back by name". R:1221–1232: the INTEGRITY causes, exit 4.
- R:2661–2821, G-TIME-n's run:
  - the steered cells sit outside the repository under item 2 (R:2714–2719); the arrays stay on the box (R:2720–2721);
  - the launch files, harness and review (R:2750–2768); the sparse copy (R:2773–2776);
  - the copy-back by explicit name (R:2793–2807); "The smoke's artifact, cells and arrays stay on the box until the campaign's cleanup" (R:2799).
- R:5452–5516: G-CAL-n's launch pattern.
- R:7842–7851, a resume precedent: "in a fresh sparse copy …, holding byte copies of the run copy's stage report, cell file and 31 capture arrays, taken by name … checked by sha256".
- R:9886–9887, the n package BUILD: "Not built here: the stage commands (… the campaign) and G-READ-n's assembly from the campaign's cells."

## 2. What exists in the code

2.1 runner.py
- `campaign_order` (runner:140–164) puts the 160 shadows first, then follows `schema.ARMS` order, with cells by `arm_cells` and sessions in the set's order; N1-R reads the 40 floor sessions. The fidelity reason is dose-rule at 0/±1, else `sample` by `keys.fid_sampled`. It asserts the plan equals `schema.read_plan`.
- `run` (runner:376–555):
  - it refuses records or a report on disk without a resume (:397–399);
  - it loads cells by name (no listing) and holds the records to the plan's reads 0..M−1 (:404–410);
  - "a resume keeps the stage's cap" (:412–416);
  - every standing pause needs a `rulings` path, whose sha256 it records (:418–428); then the replay (:430–458);
  - before each launch it ends as CAP if `used_ms >= hour_cap_ms` (:467–469); it checks the rendering (:476–485) and the window (:489–491);
  - the per-read line has no margin (:475, :509–511); a pause ends the invocation (:512–519);
  - the tail is evaluated at the end (:521–535); COMPLETE becomes CAP when the cap is reached (:536–537);
  - the report is written atomically (:548–552).
- `StageInputs` (runner:255–274) takes `hour_cap_ms` and a required `load_ms`, `directions` as direction_id → unit vector, `rulings`, the printer and the clock.
- `_prior_report` refuses any resume after a STOP: "nothing resumes after a STOP" (runner:330–331). `_report` always writes `stop: None` (runner:363). The runner has no path that writes PI-STOP or G-VER-STOP.
- The self-test's campaign and cap cases are at runner:583–612, :810–812, :826–827 and :1074–1088.

2.2 schema.py
- `STAGES = ("campaign", "time", "backend-ext")` (schema:256). The identity fields are at schema:448–481; at the campaign, `lock_sha256`, `dose_map`, `identity_bound`, `ceiling` and `median_rel` must be set (schema:845–852). `pod_id`: "a pod change refuses a resume and the stage restarts under a new root (Code's reading)" (schema:458–459). There is no cap in the identity; the cap is only in the report (schema:1208–1214).
- `read_plan` and `read_plan_sha256` are campaign-only (schema:585–604). At the campaign, a report must carry the plan's arms and sha, and "COMPLETE with an incomplete arm" is refused (schema:1388–1400, :1526–1527).
- End states (schema:207–215): STOP_KINDS are G-VER-STOP and PI-STOP (:1134). The STOP record is "{kind, record_sha256, detail}", where record_sha256 is "G-VER's report; the PI's stop raw" (:1195–1199). A G-VER-STOP report must have "no pause, no record" and at least one mismatch (:1533–1537). "the PI may stop a unit whose pause stands" (:208–210).
- Record rules at the campaign: the dose-rule re-computation at 0/±1, the `sample` elsewhere, and `timing` refused (schema:1042–1050).
- The captures are "kept on the box's volume … copied to the laptop with their hashes before the pod stops, never committed to git" (schema:74–89).
- G-READ-n's artifact form is at schema:217–238 and :1231–1264.

2.3 The other modules
- cells: a cell is `{arm}__{direction}__{slug}.json` (schema:525–529), with arrays `{stem}.L{layer}.npy` (schema:532–537) of 40 or 160 rows (schema:540–544). Rows are fsynced before the JSON's `atomic_write_json` (cells:248). "Nothing here lists a directory it was not given" (cells:23). `done_read_ids` works by name (cells:252–260). `load_cell` checks every row against `capture_sha256` (cells:161–170).
- The campaign has 138 cells (120 of 40 rows, 18 of 160) and so 4,278 arrays (drv:4653–4657).
- primitive: `read` (primitive:197) through `HFBackend` (drv:1134–1136).
- ids: `ids_of` and `label_ids` (ids:605–627).
- verify: G-VER is `verify.verify`, through `_gver_tokenizer`, which decodes only (drv:1120–1125).
- keys: `random_directions`, `fid_sampled` and `n4_schedule` (keys:42–80).
- probe: `probe.artifact` takes `campaign.cells` from the report and requires the identity's `capture_layers` (probe:116–135).

2.4 scripts/n_sessions.py
- drv:285: "Stages the campaign and G-READ-n are wired at their own steps." `main`'s command choices have no campaign (drv:6094–6096).
- The template is `gtime` (`_gtime_prepare`, drv:4237–4375):
  1. The refusals: the smoke goes to a new folder outside the repository; the run of record writes only to its own root and report; the pod must be `CHARACTERIZED_POD`; the cuBLAS setting; the stream known answer; each ruling must be a file.
  2. The weights of record: the manifest at HEAD's bytes, the folder exact by listing and byte counts (drv:688–716).
  3. The driver must be HEAD's committed bytes.
  4. The ids' MANIFEST pin; the lock's inputs; the R6 bridge; the package and closure.
  5. The identity; the campaign's counts, with `read_plan_sha256` the lock's.
  6. `prior_state`.
  7. G-VER before the load. On a STOP: "no weights load, nothing is read, no report" (drv:4344–4349).
  8. The load and provenance; `StageInputs(hour_cap_ms=None)` (drv:4373).
  - The exits are 0 COMPLETE, 3 PAUSE, 2 a G-VER STOP or a refusal, and 1 otherwise, CAP included (drv:4391–4405). The options are `--bench-dir`, `--smoke` with `--out`, and `--resume` with `--ruling PAUSE_ID=PATH` (drv:6129–6142).
  - `gver` takes no options (drv:6117–6128), exits 0/2/1, and hashes the eight non-shard files (drv:253–260).
- Pins (drv:3816–3854): `LOCK_SHA256` v0.1 (:3820) and the other `LOCK_*` values, with `CHARACTERIZED_*` at drv:630–641. There is no pin for the cap, for N2's three sha16s or for the 24 random sha16s. The lock-input helpers return the valence row (drv:3894–3941) and G-CAL-n's `span_reward` row (drv:2780–2824) only.
- Every read of `LOCK_SHA256`: drv:3913–3914 (refusal "not LOCK-n v0.1's (GT4)"), :3937, :3954 (gtime's identity), :4127, :4157 (`_check_gtime`), :4292 (STAGE line "under LOCK-n v0.1"), :4631, :4731, :5167–5169 (`gver_lock_check`), :5263 (`_check_gver`), :5407, :5549 (self-test check "LOCK-n v0.1's sha256 (GV4)") and :5624. `LOCK_PATH` is also read at drv:4572, :5552 and :5572.
- At this HEAD (my reading of the code; nothing was run): LOCK-n.md is v1.0 and the pin is v0.1's. So `gtime_lock_inputs(work)` raises at drv:4562, which the self-test counts as "G-TIME-n's self-test ran to its end" FAIL (drv:457–460), and drv:5549 fails too. `--selftest`, `gtime` and `gver` cannot pass on this tree until the pin moves (LOCK:359–361).
- The self-test (drv:339–476) runs the module self-tests and five command self-tests, each in try/except, plus hftiny on the box. Its temporary folder is made by `tempfile` outside the repository (drv:351–354). It counted 717/717 on the laptop (R:1485) and 728/728 on the box (gvout:77). Its box-safety traps: `RUNPOD_POD_ID` unset, the production loaders replaced by raising stubs, and `main()` driven through a recorder (drv:5007–5025, :6000–6018).
- The 51 campaign lines are mostly gtime's: drv:196–226, :3808–3844, :3966–3982, :4026–4184, :4209–4233, :4339–4381, :4441, :4534–4923. Also drv:273 (GV7), :285, :1958, :3294 and :5504.

2.5 scripts/n_analyze.py
- `verdicts` takes `--campaign` (the cell directory), `--report`, `--gread`, `--lock`, `--date`, `--gvec` and `--out` (anl:6798–6807).
- Of record, the lock, report, G-READ-n artifact and cosines file must be committed files in the repository (anl:6625–6650).
- `run_verdicts` refuses a report that ends in PAUSE (anl:6677–6679) and refuses `lock_sha != ident["lock_sha256"]` (anl:6687–6689). With the end state in {PI-STOP, G-VER-STOP, CAP} and no arm complete, it writes NOT-RUN `no-arm:*` (anl:6238, :6710–6719). A report with no cells and a non-empty campaign directory is refused (anl:6702–6708).
- `load_campaign` lists the directory and refuses any file no cell names; "an absent array is no refusal" (anl:3161–3203).
- `report_problems` binds the report to the cells: at most one pause standing, and it is the stage's last event (anl:6340–6456).
- `gread_problems` requires every campaign cell and the same package as the campaign: "its probe ran under another n package than the campaign's" (anl:6469–6474).
- The NOT-RUN causes are at anl:116–128.

2.6 The launch template, from the committed raws
- G-TIME-n (gtrun):
  - three files hashed and relayed (:28–38); the respawn statement (:40–49); a bundle sync (:51–57);
  - the fresh sparse copy `'/*' '!/data/m[f]3/' '!/data/*/ckpt/' '!/data/*/reports/'` (:59–71);
  - `nohup`, with the end-wait on the PID alone (:73–84);
  - the copy-back by explicit name with the address/port count; the steered cells went "straight from the box", "never staged, counted, opened or listed" (:138–162, :212–216);
  - what was left on the box (:222–231).
- G-VER v2 (gvrun):
  - the no-restart check (:42–63); `df -T` showing `/tmp` on overlay and `/workspace` on nfs4 (:65–77);
  - the copy, with "153G available of 466G" before it (:79–94); the run (:96–114); the copy-back by name (:162–191);
  - gvout:74–79 has the self-test on `/tmp`; gvout:122–130 reads the end three ways.

2.7 .gitignore and .gitattributes
- .gitignore:261–262: "any later n artifact (captures, checkpoints, reads) needs its own line". There is no line for a campaign root or report, or for the two steered cells (:338–341 admits only the shadow cell). The comment at :335–337 still says the steered cells "stay on the box's volume".
- .gitattributes:21: `/data/n/ckpt/** -diff`.

## 3. What the texts leave open — questions, with the nearest texts

3.1 The command's name and options. Nearest texts: rt23a:27; schema:256; drv:285, :6129–6142, :6117–6128; anl:6800–6801. Open:
- whether there is a smoke (GT14 had one; GV8 none; a smoke's cells stay on the box under item 2, R:2799, ans21b:39);
- `--resume`/`--ruling` (the runner requires them);
- an option for a PI-STOP (schema:208–210, :1197), which nothing writes;
- `--out` only for a smoke.

3.2 The identity at "campaign":
- From the texts:
  - `lock_sha256` 59e0b1bc…00aa (R:31–33);
  - the package and closure (LOCK:163–165; LOCK:1176–1208);
  - the weights, backend and pod (LOCK:1141–1169); the window 4,096; the session set; MANIFEST; "space"; layer 32; the band 33–63;
  - the dose map (LOCK:758–785); the fidelity rule and C (drv:3857–3863; LOCK:879–908).
- Open:
  - the `directions` map's 28 injected entries: valence, three `span_*` and 24 random, against LOCK:697–708 or `gvec.json`'s `random_sha16`;
  - whether the realized sample digest (LOCK:805–810) and the N4 schedule digest (LOCK:811–817) are checked before the load (ans20b:32).

3.3 How the lock pin moves. v1.0 §12 says "moves the pin" (one pin), and any gate re-run "would move the pin first" (LOCK:356–361). Open:
- whether to move the one shared `LOCK_SHA256` or add a campaign constant.
- What a shared move does to gtime and gver: their identities and records would carry v1.0's sha; `_check_gtime` and `_check_gver` would refuse the committed v0.1 artifact and record if ever re-checked (drv:4157, :5263); the "v0.1" texts at drv:3816, :3914, :4292, :5407 and :5549 become stale.
- v1.0 §4 names the driver at d714372, but the campaign runs a new driver. The precedent for that is m's, not n's (results/raw/2026-11-15_lock-m-f3-v1_design-to-code_answers.md:43).

3.4 The cap.
- The value is 14,400,000 ms (LOCK:106). No whole cap line exists in v1.0 to parse, unlike m-F3's "hour cap = 480 h" (results/raw/2026-11-15_lock-m-f3-v1_design-to-code_answers.md:22), so the open question is constant versus parse.
- The CAP exit code is open: gtime returns 1.
- CAP with no arm complete is NOT-RUN `no-arm:cap`; CAP with arms complete is analyzed (n:134; anl:6710–6719).
- The 8 h pod-hours envelope is enforced by no code (LOCK:119–121; box:31).

3.5 "All arms, no looks". The order is fixed (LOCK:1251–1253). Beyond n:130's stdout rule and item 5's end-wait, the texts do not say what "no looks" bars during the run, for example:
- reading the report between invocations — the report is the read domain and holds no margin;
- the copy-back's `jq` cross-checks of the staged report (gtrun:239–240).

3.6 The pauses. "On the excerpt" (ans22b:32; ans23a:53) is m's form (m:330); its content under n's no-margin blinding (n:130) is undefined. Also open:
- conditional rulings in advance (precedent: results/raw/2026-11-18_n-step4-bext2-p01_conditional-ruling.md:3), given the 0.3827 chance of a false pause;
- how the ruling raw reaches the box (the runner hashes the path, runner:420–421);
- whether the resume runs in the same copy or in a fresh copy with the state copied in by name (R:7842–7847);
- each resume's load and G-VER (ans21c:33).

3.7 The STOPs.
- GV7 makes the start's G-VER STOP the `no-arm:gver-stop` cause. The analyzer derives that only from a report with end state G-VER-STOP and a stop record (anl:6710–6719). gtime's form writes no report (drv:4344–4349), and the runner cannot write one. Who writes it is open, and so is what `rendering_mismatches` counts for a non-token cause (LOCK:938; schema:1533–1537).
- Whether the seat may re-specify and restart is open: a STOP report blocks any resume (runner:330–331).
- A G-VER STOP at a resume, after reads exist, cannot take the G-VER-STOP form (schema:1533–1537).
- No PI-STOP writer exists.

3.8 What is written where.
- The root and report paths are named by no text; by analogy they would be `data/n/ckpt/campaign/` and `data/n/reports/campaign.json` (drv:617–618, :3796–3797).
- The arrays' folder on the laptop is unnamed, "the class the campaign's capture arrays will use" (ans21b:31).
- The `.gitignore` admits (138 cell JSONs, the report, GT11's two lines) and which commit adds them are open (.gitignore:261–262; ans21b:32).

3.9 The steered cells at the close. "no session … hashes them before the campaign's cells are committed" (ans21b:31) versus committing them "with the campaign's own cells" (ans21b:32): whether their sha256s may be verified against time.json's for that same commit, and in what order.

3.10 The copy-back by name.
- The names come from the report's 138 cells times 31 layers.
- The report carries each cell's `json_sha256`; the arrays have no file digest of record, so they would be checked by sha256 at both ends, with `capture_sha256` binding their rows.
- The copy's changed-set check must not list the cell root (ans22b:22 (ii); G-TIME-n named `data/n/ckpt/time/` at R:2786–2788).
- `load_campaign` refuses any stray file, such as `._*` (anl:3199–3203).

3.11 The self-test's TMPDIR in v2's form (R:1131–1140) is required. Its new count follows the BUILD.

3.12 INTEGRITY versus FAIL.
- The classes were ruled for G-VER of record (ans22a:26–29; ans22b:24; R:1221–1232).
- Whether they, and "every end but PASS goes to the seat and the PI", extend to the campaign's ends is open. Those ends are COMPLETE, PAUSE, CAP, G-VER-STOP, a refusal and a crash, and their exit codes are open too.

3.13 A crash, a restart, a box change.
- A crash is replayed (runner:12–15; schema:152–155; cells:10–13), and the absent load is a declared gap (A-n3:60).
- Whether a restarted pod (same id; respawn first, gvrun:42–43) is still "one pod session" (n:101; m:251) and may resume is open. The identity holds `pod_id` and the backend identifier.
- A box change mid-campaign "aborts and restarts" (m:251). After v1.0 it is "a new lock version" (LOCK:191–194; ans22a:33), against a "dated note" (WORKFLOW.md:43; ans21b:27). Open: the Clock for a later version (n:152), what is committed of the aborted run, and which report VERDICTS reads.

3.14 What G-READ-n needs from the campaign.
- The final report; every cell's JSON; the arrays beside them (`load_cell` with `keep_arrays`, cells:135–140).
- The same package as the campaign (anl:6473–6474), so `valence_core/n` must not change at the BUILD (ans22b:22).
- G-READ-n's command is unbuilt (drv:285).
- Whether the arrays, 4.9–5.0 GB, come back whole or only the probed cells is open; A-n1:54 says all of them.

3.15 The entry names for step 14's BUILD and run (n:161 names none).

3.16 The box's cleanup "until the campaign's cleanup": when, and by whom (R:2799; gtrun:226–227).

3.17 The push of the campaign's cells before VERDICTS. ans18c:32 cleared backend-ext's cell; the screen halts on any ckpt match (item 4); "a push publishes them" (ans21b:29).

3.18 A-n3:60 OPEN 1's "G-READ-n's artifact's `campaign.cells` … committed at step 14", against n:121 and n:159 (G-READ-n after the campaign, on the laptop, ans21b:23).

3.19 Whether the start's G-VER (and each resume's) takes G-VER of record's eight-file hash check and tokenizers check (ans22a:17–19), or GT7's decode-only form.

## 4. What the campaign needs from the seat or the PI before it runs

4.1 The route: the spec raw and the starred readings to the seat's next thread, its ruling before any run, then the BUILD, the launch files to the coordinating session, the relay and the PI's word (rt23a:27–31; ans23a:63). Ledger (88): the seat opens `main`'s command list before routing a launch (ans22a:84).

4.2 The pin must move before any command, self-test or gate can pass on this tree (LOCK:359–361; drv:4562, :5549). Any gate re-run after it is declared in its entry (LOCK:361).

4.3 Rulings that bear on the build:
- the G-VER-STOP and PI-STOP report forms (3.7);
- the excerpt (3.6);
- hashing the steered cells at the close (3.9);
- a box change after v1.0 (3.13);
- the A-n3:60 wording (3.18).

4.4 The PI's:
- the box stays up (rt23a:39), its restart status, and the spend (box:31);
- the push of the campaign's cells (3.17);
- G-READ-n's later laptop window beside Q-F3 (ans18c:40; ans21b:23).

## OPEN QUESTIONS

1. The command's name and options, and whether it has a smoke (3.1).
2. The identity's `directions` (28 entries) and their pins; the sample and N4 digest checks (3.2).
3. One shared `LOCK_SHA256` or a campaign pin; what a move does to gtime and gver and their committed records; the driver hash v1.0 names (3.3).
4. The cap: a constant or parsed; CAP's exit; the 8 h envelope (3.4).
5. What "no looks" bars during the run beyond stdout and item 5 (3.5).
6. The n form of "the excerpt"; conditional rulings; the ruling's route to the box; the resume's copy (3.6).
7. Who writes a G-VER-STOP or PI-STOP report, and in what form; a G-VER STOP at a resume; whether a restart is possible after a STOP (3.7).
8. The root, the report and the laptop arrays' paths; the `.gitignore` admits and their commit (3.8).
9. Hashing the steered cells at the close, and the order (3.9).
10. The copy-back's list source and digests; a changed-set check without listing the root (3.10).
11. The exit codes, and INTEGRITY versus FAIL for the campaign's ends (3.12).
12. A pod restart within "one pod session"; a box change mid-campaign: a new lock version or a dated note; the Clock; the aborted run's record (3.13).
13. Whether all arrays come back; G-READ-n's input layout; the package frozen (3.14).
14. The entry names for step 14 (3.15).
15. The box cleanup (3.16).
16. Pushing the campaign's cells before VERDICTS (3.17).
17. The A-n3:60 OPEN 1 wording against step 15 (3.18).
18. What the start and resume G-VER checks hold (3.19).
19. The route: the seat's ruling on the spec raw and starred readings before any run (4.1).

## DEPARTURES

1. One `awk` process, an interpreter the brief bars: `git grep -n -i -E 'wired at their own|campaign' -- RESULTS.md | awk -F: '$2>=9829 && $2<=10055' | cut -c1-260`. It printed two lines of RESULTS.md (R:9886–9887). No marker was in its argv and nothing under `data/` was touched.
2. `shasum` twice: `/usr/bin/shasum` is Perl, which the brief bars, though list item 1 names `shasum`. The runs covered LOCK-n.md, and the driver, the analyzer and schema.py; digests only.
3. `git grep` with quoted pathspec globs, which git expanded:
   - at the root: `ADDENDUM-n*` and `ADDENDUM-n1-*` (`ls-files` also used `PROPOSAL-n*` and `LOCK-n*`);
   - under `results/raw/`: dated `*answers.md`, `*routing*`, `*ruling.md` and `n-step4*` sets.
   The brief names `git ls-files` as the form, so these are for the seat to class. No matched file is marker-named; the November routing set gave 0 of 18 by a bracketed count.
4. Also used: one scoped `git status --porcelain` on four named paths and one `git ls-files -o` of `results/raw/`, both with no output; `wc -l` of 15 named non-data files; `git log` with a commit date; and bracketed `/usr/bin/grep` patterns.

There was no marker in any argv. Nothing under `data/m[f]3`, `data/*/ckpt` or `data/*/reports` was read, listed, sized or timed. No file was written, nothing went over the network, and only the brief was read from the scratch folder.
```
