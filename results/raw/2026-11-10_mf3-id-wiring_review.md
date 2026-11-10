# The `id` wiring (G-ID-F3): the blind review, Code's dispositions, and round 2's mutant runs

*Code's raw, PI date 2026-11-10.*
- *What was reviewed:* the uncommitted edit that wires `id` in `scripts/mf3_sessions.py`. The candidate (sha256
  `1a8270fa…8422`) was the working tree's file at the review. It was checked against HEAD's driver blob
  (`1b593ba0…87c6`).
- *How:* one blind agent, read-only on the main checkout, under a brief that quotes the list of record v2's items 1–5
  as written (brief sha256 `4b2736aa…`, 107 lines).
  - It worked in a sparse clone, with every `data/*/ckpt` and `data/*/reports` directory left out of the working tree.
  - It ran the self-test with every model import blocked.
  - It built 30 one-defect mutants of the production code.
- *Outcome:* no MAJOR, 3 MINOR and 7 NOTEs.
  - All three MINORs are self-test gaps found by mutation. The code they guard is right.
  - Of the 30 mutants, 25 were KILLED and 5 SURVIVED: 1 equivalent and 4 gaps.
- *After the review:* Code applied the three MINORs and five of the NOTEs' points (below).
  - The self-test passes 197/197 on the final bytes. The candidate the review read passed 195/195.
  - Round 2 re-ran mutants through the reviewer's harness against the fixed self-test: the four gap survivors, M23,
    the five that had stopped the id block at an unguarded read (NOTE-3), and the equivalent M14.
  - All ten defect mutants are killed, the four gaps among them. The equivalent M14 survives, as in round 1 (round 2's
    table).
- *Code's masked scan of the reviewer's transcript* (no output text printed):
  - 78 distinct Bash calls, 3 of them naming `data/`.
  - None is in a barred metadata form over a `ckpt` or `reports` directory.
  - The scan's two content-form flags are both the clone's own setup:
    - a `tail` on git's output, in a command where the protected paths appear only as sparse-checkout patterns;
    - a name-only `ls -d` that confirmed their absence in the clone.
- *This raw:* Code's dispositions, round 2's table, then the report verbatim.
  - The report was extracted by script from the agent's hand-back (the text's sha256 `5a3f5d78…`, 264 lines).
  - The raw holds no local path and no clock time.
- *Nothing ran on a model.*

## Code's dispositions

- **MINOR-1 (M12), the artifact refusal under `--resume`.** Agreed. Two refusal cases are added, each with an open
  G-ID checkpoint under `--resume`: an artifact on disk, and a dangling link at its path. Both refuse with
  `artifact: G-ID ARTIFACT EXISTS`.
- **MINOR-2 (M15), id's out-root seam.** Agreed. Time's seam case is added for `run_id`.
  - An out root given with no factory is refused before the identity, with exit 2.
  - The loader and both stages are never reached.
- **MINOR-3 (M28), the state at G-ID-F3.** Agreed. The passing case is added: the first run's checkpoint at its own
  name, beside the re-run's.
  - It reaches the loader, and its bytes are untouched.
  - It is planted at cap 60 on the stub's weights binding, because `resume.Identity` admits 60 there only.
  - The precheck never reads the first run's file; its prior gate reads the re-run's.
- **NOTE-1 (M21), a looping link at the prior path.** Agreed. The case is added in the form of time's looping-link case:
  - on Python 3.12 it gives `prior: the prior checkpoint path does not resolve (RuntimeError)`;
  - on 3.13 and later, where the loop no longer raises, it gives `prior: PRIOR STAGE ABSENT`.
- **NOTE-2, the not-wired check.** Agreed. Its three calls now run on a test root, with the loader and both stages
  trapped and the laptop checklist stubbed. A dropped guard can no longer reach `data/mf3`.
- **NOTE-3, unguarded reads.** Agreed. The reads in the resume and pending cases are guarded. A failing run now fails
  its check, and the block goes on to the final audit.
- **NOTE-4, the factory seam.** Not changed.
  - It is time's seam, as in m: the self-test's own, and `main` cannot reach it.
  - Refusing a non-stub adapter from a factory would change time's seam too, which this edit leaves as it is.
- **NOTE-5 (a), F-7's site.** Agreed. The docstring and the id PIN now cite `stages.gid_decide` for the 2/2
  criterion, and the seat's F-7 (`stages._gid_pair`) for each pair's identity.
- **NOTE-5 (b), the carried `time` PINs.** Not changed. Their texts are carried verbatim, and what they say holds
  through the wrappers. The id PINs name the stage-generic functions.
- **NOTE-5 (c), the lock's anchors.** Recorded for LOCK-m-F3 v0.2. R3's `scripts/mf3_sessions.py:88` and `:95` refer
  to blob `1b593ba0…`, and v0.2 re-anchors them on the new blob.
- **NOTE-5 (d), the post-load refusal.** Agreed. The id PIN in `stage_precheck` now names, as made only after the
  load, `_finish_gid`'s G-ID ARTIFACT DIFFERS on a re-finish of G-ID-F3's own pending end.
- **NOTE-6, 194/195 under the harness.** As the reviewer says: blocking `mlx_lm` makes the constants check's
  `find_spec` return None. Code's own runs, without the block, pass 195/195 (the reviewed candidate) and 197/197 (the
  final bytes).
- **NOTE-7, HEAD.** After the brief named `54b1e51`, HEAD moved by two RESULTS.md-only commits from other sessions
  (`9699ce3` and `29fe1fa`). The driver's HEAD blob is the same.

## Round 2: the mutants against the fixed self-test

- *How:* through the reviewer's harness, its work directory moved to a fresh sparse clone at HEAD `29fe1fa`, with the
  model imports blocked. The mutants were regenerated by the reviewer's generator, unchanged, on the fixed candidate
  (`8d878f4a…00e7`). The fix moved no anchor its replacements use.
- *Scope:* the four round-1 gaps, M23, the five that had stopped the id block at an unguarded read (NOTE-3), and the
  equivalent M14. The other 19 mutants, killed in round 1, were not re-run.
  - The edits since round 1 add cases: three in the refusal table, the seam case, and the first-beside case, whose
    loader reach moves the final audit's count from 3 to 4. They also guard reads and move the not-wired check to a
    test root.
  - None removes or weakens an assertion those kills rest on. That is by reading, not by a run.
- *The baseline under the harness* is 196/197. The one FAIL is NOTE-6's constants check, which reads mlx_lm's source
  while the harness blocks it. "Killed" means any further FAIL, or fewer checks run.

| mutant | the defect | round 1 | round 2 | killed by |
|---|---|---|---|---|
| M12 | the artifact refusal skipped under `--resume` | SURVIVED (gap) | KILLED, 194/197 | the refusal table (the two `--resume` artifact cases); the final audit |
| M15 | the out-root refusal made for `time` only | SURVIVED (gap) | KILLED, 195/197 | the new seam case |
| M21 | RuntimeError and OSError from the prior path no longer caught | SURVIVED (gap) | KILLED, 188/190 | the looping-link case: the precheck's RuntimeError escaped (the self-test reports "integration selftest raised"), so the block stopped there |
| M28 | the prior also refused whenever `Q-F3_time.json` exists | SURVIVED (gap) | KILLED, 194/197 | the new first-beside case; the final audit |
| M23 | `stage_precheck`'s not-wired guard dropped | KILLED, after a real `qual` precheck (NOTE-2) | KILLED, 195/197 | the not-wired check, now on a test root with the traps in place |
| M05 | `locked_path` added for `id` | KILLED, the block stopped at a read | KILLED, 183/197 | 13 checks, the block run to its end |
| M06a | the stage's prior is `Q-F3_time.json` | KILLED, the block stopped at a read | KILLED, 188/197 | 8 checks, the block run to its end |
| M09a | `ID_REASONING_CAP = 60` | KILLED, the block stopped at a read | KILLED, 184/197 | 12 checks, the block run to its end |
| M16 | the stage given `stages.DEFAULT_OUT`, not the run's root | KILLED, the block stopped at a read | KILLED, 190/197 | 6 checks, the block run to its end |
| M17 | the stage given `ckpt_path` = time's r2 checkpoint | KILLED, the block stopped at a read | KILLED, 189/197 | 7 checks, the block run to its end |
| M14 | the precheck loads time's schedule files for `id` | SURVIVED (equivalent) | SURVIVED, 196/197 (the baseline) | equivalent: `load_committed` verifies the whole directory against its regeneration, manifest included |

- *Outcome:* all ten defect mutants are killed, the four round-1 gaps among them. The equivalent M14 survives, as in
  round 1. In every run the model-import blocks held, and the clone changed only in its driver.

## The reviewer's report (verbatim)

# Blind review: the `id` wiring (G-ID-F3) in `scripts/mf3_sessions.py`, before its commit

`report.md` was not written: the tool layer refuses report files from a subagent. This message is the full report; save it as `report.md` in the work directory if you need the file.

What was reviewed:
- **The candidate:** sha256 `1a8270fa…8422`. It is byte-identical to the main checkout's working-tree file.
- **The diff:** sha256 `1d19bc6b…964b`. It is identical to `git diff scripts/mf3_sessions.py` in the main checkout.
- **HEAD:** `29fe1fa`, not the brief's `54b1e51` (NOTE-7). The driver's HEAD blob is the same at both.

Line numbers below are the candidate's (`:N`), unless a file is named.

## Verdict

- **Spec:** the production code does what the seat's §5 item 1 says, item by item.
- **`time`:** unchanged in what it does, prints and refuses.
- **Hazards:** none of question 3's hazards can be reached from the command line.
- **Findings:** no MAJOR finding. There are three MINOR findings. All three are gaps in the self-test, found by mutation; the code those cases would guard is correct today. There are also seven NOTEs.
- **Mutation:** 30 one-defect mutants of the production code. 25 were KILLED and 5 SURVIVED.
  - 1 survivor is equivalent (M14).
  - 4 survivors are gaps: M12, M15, M28 and M21.
  - The brief's eight example mutants were all killed.

## Findings (most severe first)

### MINOR-1 — The artifact refusal is never tested under `--resume` (M12 survives)

- **Where:** the refusal is at `:438`.
  - The id cases at `:1946–1948` (an artifact, a dangling link) run without `--resume`.
  - The case at `:2001` runs `--resume` with no artifact.
- **The code today is right:** `:438` refuses an artifact or a link with or without `--resume`.
- **The gap:** a one-clause edit at `:438`, `… and not pending and not resume_run:`, passes the self-test (194/195, the baseline).
- **Failure scenario:** `id --resume`, with an open `Q-F3_id.json` and an artifact still in `data/mf3/gates`. That is B7's case: an old artifact not yet set aside.
  - The precheck passes, the DRIVER and SNAPSHOT lines print, and Qwen loads.
  - Only then does the stage's B7 check (`stages.py:1255`) STOP the run. That is hazard (a): the model loads before the refusal.
  - With a dangling link there instead, the stage's `exists()` test passes it. At the finish, the atomic write (`os.replace`) replaces the link. The one refusal the PIN says only the precheck makes is lost.
- **Fix:** add two cases to `i_refused`, each expecting `artifact: G-ID ARTIFACT EXISTS`:
  - `id_ckpt(None)` plus `artifact`, with `resume_flag=True`;
  - `id_ckpt(None)` plus `dangling`, with `resume_flag=True`.

### MINOR-2 — id's out-root refusal is not asserted (M15 survives)

- **The code:** `:591–594` refuses an `out_root` given without a factory, for both stages.
- **The gap:** only time's form is asserted (`:1453–1468`). `_selftest_id` has no counterpart. On this refusal, the requirement "a self-test asserting the refusals as `time`'s does" is not fully met.
- **Failure scenario:** an edit narrows the check to `stage == "time"`, and the self-test still passes. Then `run_id(out_root=<dir>)` with no factory:
  - runs the precheck on `<dir>`;
  - prints the DRIVER and SNAPSHOT lines;
  - loads Qwen;
  - and is refused by `stages._out_root_guard` (`stages.py:156–161`) only after the load. That is hazard (a).
- **Reach:** the Python API only. `main` never passes an out root.
- **Fix:** give id a copy of time's seam case.

### MINOR-3 — The real state at G-ID-F3 is never modelled (M28 survives)

- **The real state:** at G-ID-F3, `data/mf3/ckpt` holds both checkpoints: the first run's `Q-F3_time.json` and the re-run's `Q-F3_time-r2.json` (A-m2 v0.5 §4.3; lock R2).
- **The self-test's cases:**
  - In every id case where the prior passes, the root holds only `Q-F3_time-r2.json`: the stub roots built by `time_then` (`:1714`) and the Qwen-path roots built by `plant_time()` (`:1866`).
  - `Q-F3_time.json` is present only in cases built to refuse: `first_link` (`:1884`) and the stub `firstlink` case (`:1763`).
  - time's self-test does model this state (`rf`, "first_beside", `:1486–1493`).
- **Failure scenario:** M28 adds one condition at `:364` and refuses whenever `Q-F3_time.json` exists at all — an over-broad reading of "refuse the first".
  - The self-test still passes.
  - Every real G-ID-F3 would then be refused at the precheck (exit 2, PRIOR PATH REFUSED).
  - Nothing loads and nothing is written, but the stage is blocked.
- **Fix:** add a passing case: `plant_time()` with `plant_time(name=FIRST_RUN_CKPT_NAME, cap=60)` beside it. Assert that the loader is reached and that the first run's bytes are unchanged.

### NOTE-1 — A looping link at the prior path is untested (M21 survives)

- **The code:** the `except (RuntimeError, OSError)` clause at `:431–432` is reached by no case.
- **What a loop does:** on the venv's Python 3.12.9, a symlink loop at `Q-F3_time-r2.json` makes the non-strict `resolve()` in `stages.checkpoint_path` raise RuntimeError.
- **If the clause were dropped:** `id` would exit 1 with a traceback before the load, instead of printing the REFUSED line. Nothing loads and nothing is written. Only the form of the refusal is lost.
- **Comparison:** time's self-test has the matching case for its own checkpoint (`:1380`).

### NOTE-2 — The not-wired check runs without traps against the real `data/mf3` (M23 is killed, but after a read)

- **The code:** `:1646–1647` call `stage_precheck("qual", …, out_root=real_out)` and `run_stage("qual", …)`.
  - No test root and no loader trap are in place, and `preflight_laptop` is not stubbed.
  - The calls rely on the not-wired guard being the first statement.
- **With `stage_precheck`'s guard dropped (M23):** the self-test runs a full "qual" precheck on the real `data/mf3`:
  - the licence and the schedules;
  - `rs.refuse_ended` and `rs.pending_at` on `data/mf3/ckpt/Q-F3_qual.json`, which reads that checkpoint's content once G-F3 has written it. That would breach list item 2. Today the file does not exist.
  - The check then fails, but only after the read.
- **`run_stage("qual")`** is safe even without its guard: `stage_identity_extra("qual")` returns no identity before any load.
- **Suggested fix:** run these three calls on a `fresh()` root, with the traps in place.

### NOTE-3 — Unguarded reads abort the rest of the id block

- **The code:** `:1784` and `:1788` (`rs.read_checkpoint`) and `:1812` (`read_bytes`) read without an `is_file()` guard, unlike `:1717`.
- **What happened:** five killed mutants (M05, M06a, M09a, M16, M17) stopped there with "integration selftest raised SystemExit: CHECKPOINT UNREADABLE".
  - The remaining id checks were skipped, including the final no-load, no-write audit (`:2044`).
  - The check total dropped to 188.
- **Effect:** no regression can pass this way, because the run still fails. But in exactly the failing runs, the trap audit is not reported.

### NOTE-4 — The factory seam skips the precheck, the driver check and the snapshot check

- **The code:** `:603–637`. This is by design, and the same as time's at HEAD.
- **Scenario:** a factory that returns a real adapter, for example `run_id(adapter_factory=_load_qwen)`.
  - G-ID-F3 would then run on `data/mf3` with only the stage's own checks: the licence, `prior_gate` with `require_real`, B7 and the out-root guard.
  - No DRIVER line would be printed.
- **Reach:** `main` cannot reach this path.
- **Option:** refuse a non-stub adapter that comes from a factory (`stages._is_stub`).

### NOTE-5 — Citations and carried text (for the seat-citation sweep)

- **(a) F-7 is cited at the wrong site.** `:33` says "criterion 2/2 (stages.gid_decide, the seat's F-7)" and `:130–131` says "(stages.gid_decide under the seat's F-7)".
  - F-7 is the per-pair identity: `stages._gid_pair`'s PIN and `guard.GID_CRITERION`.
  - `gid_decide`'s PIN cites the seat's Q8 and N2.
- **(b) The carried time PINs still name the wrappers as the doers:** `:391` ("``run_time`` adds the driver check's…") and `:577` ("time_precheck, the driver check …"). Both are true through the wrappers, but the work is now done in `stage_precheck` and `run_stage`.
- **(c) The lock's anchors moved.** The re-issued lock's R3 anchors `scripts/mf3_sessions.py:88` and `:95` refer to blob `1b593ba0…`. In the candidate those sites are at `:101` and `:108`. LOCK-m-F3 v0.2 should re-anchor them with the new blob.
- **(d) One post-load refusal is not listed.** The id PIN's list of refusals made only after the load (`:373–392`, carried from time) leaves out one of id's own: `_finish_gid`'s "G-ID ARTIFACT DIFFERS" on a pending re-finish (`stages.py:1361–1364`).

### NOTE-6 — Under the brief's harness the baseline is 194/195, not 195/195

- **Why:** the constants check (`:924–934`) reads mlx_lm's source through `importlib.util.find_spec("mlx_lm")`.
  - That call returns None once `sys.modules["mlx_lm"] = None`. I confirmed this in isolation.
  - So `pats` comes back `[]`, and the check fails.
- **Scoring:** every mutant was scored against that baseline. KILLED means any further FAIL, or fewer checks run.
- **Not reproduced:** I did not run without the block, so the author's 195/195 was not reproduced as such.

### NOTE-7 — HEAD has moved since the brief

- The brief names HEAD `54b1e51`; the repository's HEAD is `29fe1fa`.
- The two newer commits, `9699ce3` and `29fe1fa`, change RESULTS.md only.
- The driver's HEAD blob is `9d54d25` at both commits (sha256 `1b593ba0…87c6`, the value in the re-issued lock's R1 table). The diff is against that blob.

## The mutant table

How the mutants were run:
- Each mutant is one change to production code. The self-test region, `_short` through `run_selftest`, was left untouched.
- Each was run through the full `--selftest` in the sparse clone, with the model imports blocked.
- The baseline is 194/195 (NOTE-6).
- "Refusal table" means the check at `:1964–1983`. "Final audit" means `:2044`.

| mutant | the defect | result | killed by, or why it survived |
|---|---|---|---|
| M01 | `id_prior_checkpoint` drops the first run's name check (`:364`) | KILLED | stub first-run check (no PRIOR PATH REFUSED); refusal table: the link case reached the loader, the by-name case refused as PRIOR STAGE ABSENT; final audit |
| M02a | precheck drops `prior_gate`, keeps the path refusal (`:426–428`) | KILLED | refusal table: the six real-gate prior cases reached the loader; multi (no `prior:` problem); final audit |
| M02b | precheck drops the whole prior block | KILLED | as M02a |
| M03 | precheck drops the artifact refusal (`:438`) | KILLED | refusal table: the artifact and dangling-link cases reached the loader; multi; final audit |
| M04 | `require_real=False` in the precheck (`:427`) | KILLED | refusal table: "prior on the stub" reached the loader; "at another cap" refused as NOT THE FIXED CAP; final audit |
| M05 | `locked_path` added for id (`:326–327`) | KILLED | identity check; cap and lock check; stub runs; aborted at `:1784` |
| M06a | the stage's prior is `out_paths("time")["ckpt"]`, i.e. `Q-F3_time.json`, m's form (`:644`) | KILLED | stub PASS check (STOP: PRIOR STAGE ABSENT); exit-code and no-prior checks; aborted at `:1784` |
| M06b | the precheck's `prior_gate` reads `Q-F3_time.json`, m's form | KILLED | refusal table; reach-load (PRIOR STAGE ABSENT); post-load; final audit |
| M07 | stage swapped: id calls `run_gate_stage`, time's stage (`:638`) | KILLED | "integration selftest raised ValueError: identity_extra must carry exactly …" at the first id stub run |
| M08a | the stage is called with `resume=False` (`:643`) | KILLED | stub `--resume` check (CHECKPOINT EXISTS with `--resume`) |
| M08b | `main` drops `--resume` for id (`:2114`) | KILLED | reach-load / `--resume` / pending check (`rr` refused); final audit |
| M08c | the precheck's CHECKPOINT EXISTS ignores `--resume` for id (`:417`) | KILLED | as M08b |
| M09a | `ID_REASONING_CAP = 60` (`:140`) | KILLED | identity check (cap 120); stub runs; aborted at `:1784` |
| M10 | the artifact test is `exists()` only, so a link passes (`:438`) | KILLED | refusal table: the dangling-link case reached the loader; final audit |
| M11 | the artifact is refused even with an end pending (`:438`) | KILLED | reach-load / pending check (`rp` refused); final audit |
| M12 | the artifact refusal is skipped under `--resume` (`:438`) | **SURVIVED: gap** | no case combines an artifact (or a link) with `--resume` (MINOR-1) |
| M13 | the precheck checks id's own checkpoint at time's r2 path (`:412`) | KILLED | refusal table: the exists and ended cases reached the loader; reach-load (STAGE ENDED); post-load; final audit |
| M14 | the precheck loads time's schedule files for id (`:404–405`) | **SURVIVED: equivalent** | `load_committed` first verifies the whole directory against the regeneration, manifest included (`schedule.verify_schedule_dir`), so a defect in either of id's files is refused whichever files are named; the stage reloads id's files after the load |
| M15 | the out-root refusal is made for time only (`:591`) | **SURVIVED: gap** | no id seam case (MINOR-2) |
| M16 | the stage is given `out_root=stages.DEFAULT_OUT` (`:644`) | KILLED | stub PASS and exit-code checks; aborted at `:1784` |
| M17 | the stage is given `ckpt_path` = time's r2 checkpoint | KILLED | stub PASS check (STAGE ENDED on the r2); exit-code and no-prior checks; aborted at `:1784` |
| M18 | the `--selftest` / `--build-schedules` / `--out` refusal is made for time only (`:2100`) | KILLED | refusal table: the three top-level cases; final audit (escapes) |
| M19 | the precheck's `prior_gate` gets `proposal_sha256=None` (`:426`) | KILLED | refusal table: "under another proposal" reached the loader; final audit |
| M20 | the first-run check tests the name constant, not the resolved path (`:364`) | KILLED | stub link case; refusal table: the link case reached the loader; final audit |
| M21 | RuntimeError and OSError from the prior path are no longer caught (`:431`) | **SURVIVED: gap** | no looping link at the prior path (NOTE-1) |
| M22 | the Qwen path skips `stage_precheck` for id (`:604`) | KILLED | refusal table: the licence, renders, prior, artifact and other cases reached the loader; multi; final audit |
| M23 | `stage_precheck`'s not-wired guard is dropped (`:393`) | KILLED | the not-wired check (`:1645–1658`), but after a real "qual" precheck had run on the clone's `data/mf3` (NOTE-2) |
| M24 | the Qwen path skips the pre-load snapshot check for id (`:606`) | KILLED | refusal table: the snapshot cases; multi; reach-load (SNAPSHOT line); post-load; final audit |
| M27 | id's FAIL and NOT-DETERMINED exit 0 (`:648`) | KILLED | exit-code check (FAIL 5, NOT-DETERMINED 6) |
| M28 | `id_prior_checkpoint` also refuses whenever `Q-F3_time.json` exists (`:364`) | **SURVIVED: gap** | the first run's checkpoint is never beside a passing r2 in any id case (MINOR-3) |

## What I checked and found right

### Spec conformance (§5 item 1)
- **The stage library's keys and templates.** `run_stage` hands G-ID-F3 to `stages.run_gid_pair_f3` (`:643`).
  - That function supplies `keys.GID_TEMPLATES`, which is (A2s, A3s).
  - It builds the keys with `keys.arm_key("id", …)`, giving `m-id|F3|{template}|{s}`.
  - It decides with `gid_decide` (2/2) and judges each pair with `_gid_pair` (F-7).
  - The precheck loads id's two committed schedule files (`:404–409`).
  - Nothing in the driver re-derives keys.
- **No `locked_path`.** `:323–327`. `_extra(stage="id")` requires the exact key set without it (`stages.py:605–609`).
- **Cap 120.**
  - `ID_REASONING_CAP` (`:140`) is validated with `stub=False` (`:329`, `stages.py:624`), so even the factory seam cannot run id at 60.
  - `prior_gate` fixes the cap at 120 when `require_real` is on (`stages.py:499–513`).
- **The prior.**
  - `id_prior_checkpoint` (`:359–367`) is used by both the precheck (`:426`) and the stage call (`:644`). It builds `<root>/ckpt/Q-F3_time-r2.json` through `checkpoint_path`, so the path is resolved, stays inside `ckpt/`, and contains no roster word.
  - It refuses the first run's name on the resolved path.
  - Independent backstop: the first run ran at cap 60. `prior_gate` with `require_real` therefore refuses it on any run on a model ("PRIOR STAGE AT ANOTHER CAP"), whatever its name — a copy, a hard link, or a case-variant link on macOS's case-insensitive filesystem.
- **`prior_gate` with `require_real` on.** In the precheck it is set explicitly (`:426–428`). After the load, the stage's own `_licensed` call sets it again (`require_real=not stub`).
- **The artifact.** It is written at `guard.gid_artifact_path()`, under `data/mf3/gates`.
  - The precheck refuses an existing file or link unless an end is pending (`:433–439`).
  - The stage's B7 (`stages.py:1255`) and `_finish_gid`'s byte-identical rule (`stages.py:1361–1364`) cover the same.
  - The driver never moves an artifact.
- **The self-test.** It has 13 id checks.
  - 30 refusal cases follow time's form: exit 2, output on stderr only, no DRIVER or SNAPSHOT line, the loader and both stages never reached, the root and its gates directory unchanged, and no label printed.
  - There are also the multi, reach-load and post-load cases, and the final audit.

### `time` is unchanged
- **Same results for "time".** `stage_identity_extra`, `stage_precheck` and `run_stage` give:
  - the same identity dict, with the same keys in the same order;
  - the same problem strings;
  - the same REFUSED and STOP lines ("G-TIME-F3 cites …" now comes from `stages.stage_name("time")`, which is the same text);
  - the same stage call.
- **The wrappers.** `run_time` and `time_identity_extra` are now wrappers. No time self-test patches the wrapped names, so none was weakened.
- **The parser.** time's subparser has HEAD's help strings, for the subcommand and for `--resume`.
- **The self-test.** `_selftest_time` is unchanged by the diff and passes in full in the clone. The identity check asserts `time_identity_extra(...) == stage_identity_extra("time", ...)`.
- **What did change:** only the top-level `--help` description and the "no action" refusal line. Neither belongs to `time`.

### Question 3, the hazards, from the command line
- **(a) Loading the model before a refusal.** Every refusal the precheck can make comes before `_load_qwen`. After the load, only the declared refusals remain, plus NOTE-5 (d).
- **(b) Writing outside `data/mf3`.** The stage writes only under `data/mf3`: the checkpoint and its `.tmp`, the report and reads, the adjudication excerpt and the artifact. Stub runs are refused on canonical paths.
- **(c) A cap other than 120.** Not possible.
- **(d) The first run's checkpoint as the prior.** Not possible on a model run: the name check plus the cap backstop.
- **(e) Overwriting or setting aside an existing artifact.** Not possible.
- **(f) Skipping the precheck, the driver check or the snapshot check on the Qwen path.** Not possible from `main`. The factory seam is NOTE-4.

### Run hygiene
In all 31 runs:
- the model-import blocks held;
- the clone's `git status --porcelain` showed only the driver.

## Disclosures

### In the main checkout (read-only)
- **Item 1's forms:**
  - a bare `git status --porcelain`;
  - `git rev-parse` of HEAD and of two blobs;
  - `git diff --name-only 54b1e51 29fe1fa`;
  - `git log --format='%h %s' -n 4`;
  - `git ls-files` on named spec paths;
  - `shasum -a 256` of the candidate, the driver and the diff;
  - a name-only `ls` of `.git/hooks`.
- **Read-only commands beyond item 1's list, none of them touching `data/`:**
  - `git diff scripts/mf3_sessions.py | shasum`, which printed a digest only;
  - `git show HEAD:scripts/mf3_sessions.py`, saved to the work directory;
  - `git config --get-regexp` for filters, and `cat .gitattributes`;
  - `git --version`;
  - `wc -l` of seven spec and code files.
- **Reading and searching:** Read, `sed -n` and `/usr/bin/grep` on named files only. That covers the brief's spec files and a few more code files:
  - `valence_core/mf3/{schedule,resume,keys,scaffold,gshape}.py`;
  - `valence_core/m/resume.py`;
  - `valence_core/adapters/__init__.py`;
  - `valence_core/e2d/config.py`'s ROSTER, read to make sure no temp path held a roster word.
- **What was not done:** no recursive search over a tree; nothing under `data/*/ckpt` or `data/*/reports` read, listed or measured; nothing edited, staged, committed, stashed or reset; `jlens-qwen36/` used only for its Python, with `-B` so no bytecode was written.

### The clone (in the work directory)
- **Object store:** `git clone --no-checkout` copies the whole object store. So the clone held, as git objects, the blobs of every committed `data/*/ckpt` and `data/*/reports` file.
  - None was read.
  - The sparse checkout kept them out of the working tree. A name-only glob count gave 0 and 0.
  - The clone is now deleted.
- **After each run:** I restored the clone with `git checkout -- .` and `git clean -fd`, in the clone only.

### What each self-test run did
- **Files:** it hashed the files under the clone's `data/mf3` (schedules and gates only).
- **The hub cache:** it read the real HF hub cache read-only, with `HF_HUB_OFFLINE=1` (licence (g) and `hashes`). No weights were loaded.
- **Processes:** it spawned its own fresh-interpreter import check, one child Python per run, run sequentially.
- **Temp files:** it wrote only temp directories, with TMPDIR set inside the work directory and removed after each run.

### Python processes, all mine and run one at a time
- 31 harness runs: the baseline and 30 mutants. About 47 minutes in all, so the hour was slightly exceeded.
- The mutant generator, twice.
- A version check.
- A `find_spec` check with the blocks in place.
- `pgrep` checks: none found another harness running.

### Files left in the work directory
- `harness/`: the run scripts and the mutant generator.
- `mutants/`: the 30 mutant files.
- `runs/`: per-run output and status files. They contain absolute temp paths and are not for committing.
- `work/head_mf3_sessions.py`: HEAD's driver.
- No `report.md`: the tool layer refused the write.
