# G-TIME-F3's wiring -- the blind code review, three rounds, with Code's dispositions (2026-11-07)

*Code's raw. Three blind review rounds over the `time` wiring of `scripts/mf3_sessions.py`, each by an agent given the code and m's reference forms, not Code's conclusions; each round ran the self-test, mutation probes under traps and state probes. Round 1's harness trapped the loader and the mlx / mlx_lm / jlens_qwen imports, and watched data/mf3 by hash. Round 2 added traps on writes under data/, network connects and a nested self-test, and round 3 kept them all. In the mutation runs the stage trap is the self-test's own; rounds 1 and 2's state probes, which call run_time outside the self-test, patched the stage themselves. Between rounds Code re-checked each finding at source and applied, declared or disclosed it; the dispositions follow each round. Round 1: 0 MAJOR, 3 MINOR, 13 NOTEs (41 mutants, 18 survived). Round 2: 0 MAJOR, 1 MINOR, 12 NOTEs (74 mutants, 16 survived). Round 3: 0 MAJOR, 1 MINOR, 12 NOTEs (99 runs, 16 survived, 7 of them equivalent). Round 3's reviewer could not write its report file (its harness refused it) and returned the text; Code saved it as given. The reviewers' harnesses, mutants and logs are Code's scratch, not committed.*

---

# Round 1

# Blind review r1: the `time` wiring of scripts/mf3_sessions.py (G-TIME-F3)

**Reviewed:** the worktree `scratchpad/wire-wt`, detached at `a28bef6` (the scratch commit that carries
LOCK-m-F3.md). `scripts/mf3_sessions.py` is modified there, sha256 `22a52598ee4928dc…`, and `time/wiring.diff` is
the diff. The reference is `scripts/m_sessions.py` at main `02dadb3`. Line numbers below are the worktree
driver's unless prefixed `m:` (m_sessions.py) or `stages.py:` (valence_core/mf3/stages.py).

**Read-only:** checked after the work. Main is still at `02dadb3` with no tracked change. The worktree is still at
`a28bef6`, and its driver's bytes are still `22a52598…`. Nothing was written under either tree's `data/`.

**Verdict: 0 MAJOR, 3 MINOR, 13 NOTEs.**
- The production path is a faithful port of m's Qwen `time` path. Its behavioural differences are justified by
  mf3's package, with one exception: MINOR-2.
- No self-test case can load the model, run a session on it or write `data/mf3`, in any state of the tree or the
  machine tried. Two caveats: the safety claim's stated mechanism is inaccurate, and one conjunct of the seam check
  is vacuous (MINOR-1).
- The self-test carries only part of m's checks for this path. 18 of 41 single mutants of the production code
  survive (MINOR-3).

## Method

- **Static comparison.** Each ported function was compared with m's original, code diffed with the docstrings
  stripped (`review/harness/fn_diff*.py`).
- **Isolated clone.** `review/clone` is a `git clone --shared` checked out at `a28bef6`, with the modified driver
  copied in. A `diff -rq` against the worktree shows no other difference.
- **The harness** (`review/harness/trapped_selftest.py`):
  - It replaces `valence_core.adapters.qwen_or_explain`, `get_adapter` and `QwenMLXAdapter` with traps.
  - It blocks any import of `mlx`, `mlx_lm` or `jlens_qwen`.
  - It hashes `data/mf3` in the main tree, the worktree and the clone, before and after each run.
- **Baselines.**
  - Full self-test: 149/149 with `HF_HUB_OFFLINE` unset, and 149/149 with `HF_HUB_OFFLINE=1`.
  - The driver's integration checks alone: 25/25.
  - In every baseline: no trap hit, no watched tree changed.
- **Committed state** (the riskiest state of the tree and machine). In the clone, the wired driver was committed on
  top of the lock, so the real `driver_problems()` and the real `qwen_snapshot()` are both clear. The machine was
  on AC power through a 140 W adapter, with `HF_HUB_OFFLINE=1`. Full self-test: 149/149, no trap hit, no watched
  tree changed.
- **Mutation.** 41 single mutants of the driver's production code. Each ran under the trapped harness with
  `HF_HUB_OFFLINE=1`; the table is at the end. No mutant hit a trap or changed a watched tree. The clone was
  restored afterwards.

## 1. Safety

**Self-test.**
- For the code as written, no case reaches the real load, runs a session on the real model, or writes the real
  `data/mf3`. This holds with the lock committed, the driver committed, `HF_HUB_OFFLINE=1`, AC power and no other
  model process. It was confirmed by running in the committed state above.
- Run from the main tree it behaves the same, because every path is REPO-relative. Before the lock is committed
  there, the identity refuses and the checks fail, which is safe.
- How each kind of call is protected:
  - **The 25 `time_q` calls** (:803-833) trap `_load_qwen` and `stages.run_gate_stage`, point
    `stages.DEFAULT_OUT` at a test root, and stub `preflight_laptop`, the driver check and the snapshot check.
  - **The stub run** (:956) traps `_load_qwen`.
  - **The seam call (:888) and the two ended-checkpoint calls (:978)** run with nothing patched. The seam call is
    protected only by the refusal it tests, and behind that by the absence of schedule files in its test root. The
    ended calls are protected by their stub factory. See MINOR-1.

**Production path.**
- Every refusal comes before `_load_qwen()` (:464). In order: flags (:438), out root (:442), identity (:446-450),
  then the precheck, driver check and snapshot check, refused together (:454-460). Mutants `load_before_precheck`
  and `load_before_lines` are killed.
- Nothing is written before the load. The pre-load path only:
  - runs git object reads (`cat-file`, `ls-tree`, `rev-parse`);
  - runs `pmset`, `pgrep` and `df`;
  - reads files (the lock, the proposal, the analyzer, the m files, the hub cache's refs and index);
  - calls `snapshot_download(local_files_only=True)`, whose offline branch only reads.
- The first write is the stage's checkpoint, after the load (stages.py:957-958).

## 2. Fidelity to m's forms

Unchanged from m except for the docstring:
- `_load_qwen`, `redact_totals`, `_say` and `snapshot_line` have identical code.
- `TOTALS_RX`, `TOTALS_REDACTED`, `HF_OFFLINE_ENV` and `MLX_LM_ALLOW_PATTERNS` are identical.
- The DRIVER line (:461), the SNAPSHOT line (:463), the re-read line (:478) and the three post-load STOP messages
  (:470-477) are byte-identical in form to m:1622-1642.

| difference | where | m | mf3 | ruling |
|---|---|---|---|---|
| stages API | :240, :333, :319 | `stages._committed`, `stages._repo_rel` | `stages.committed`, the driver's own `_repo_rel` (also catches RuntimeError) | justified (mf3's package API) |
| DRIVER_REL | :65, :333 | from `__file__` (m:626) | the constant `"scripts/mf3_sessions.py"` | **defect, MINOR-2** |
| missing-flags message | :439 | `{stage} --unit Q-F0 needs …; lock §0` | `time needs …; lock §1` | justified (no unit; mf3's lock section) |
| out-root message | :443 | "writes data/m only" | "writes data/mf3 only" | justified |
| lock cited | :237 | LOCK-m-F0.md | LOCK-m-F3.md | justified |
| m_module_sha256 and weights | :253-259 | absent (Q-F0's identity has neither) | read from the lock's committed text | justified (the routing; see §3) |
| refusal guards | :448, :458 | `if probs`, `if pre` | add `or extra is None`, `or dsha is None or snap is None` | justified hardening |
| REVISION_STAGES test | — | qual and campaign only (m:1615-1617) | none | as m's `time`; see NOTE-3 |
| `HF_HUB_OFFLINE` message | :359 | "...rules for every later Qwen stage of Q-F0" | "...the licence's (g) and the step-10 read, Q5" | justified |
| stage call | :482 | `unit=`, `substrate="qwen"` | neither | justified (mf3's signature) |
| top-level-flags refusal | main | `refused: {cmd} takes no …` via a stderr print | `REFUSED: time takes no … (the run writes data/mf3 only); nothing loaded` via `_say` | harmless (NOTE-8) |
| subcommand refusals, "no action" | main | stderr | stdout (as before the edit) | pre-existing (NOTE-8) |

**Order of checks** is m's for the Qwen `time` path, without the campaign's rulings and RULING line: flags, out
root, identity, then precheck + driver + snapshot refused once, then DRIVER, then SNAPSHOT, then the load, then the
re-read, SNAPSHOT MOVED and MODEL ID, then the re-read line, then the stage.

**Exit codes** are m's:
- 2: refused before the load.
- 4: any SystemExit from the loader, the post-load checks or the stage.
- Otherwise `stages.EXIT_CODES[status]`: PASS 0, STOP 4.

**Streams** are m's: REFUSED and STOP go to stderr through `_say`; INVOCATION, DRIVER, SNAPSHOT and the re-read
line go to stdout. **`time_precheck` against m's `stage_precheck("time")`:** the same checks in the same order
(licence, startup, renders, schedules, checkpoint path, ENDED, EXISTS, laptop checklist, gate line, CLAUDE.md and
analyzer committed), and the same `redact_totals` pass.

## 3. The identity

**Can a lock text pass the parsers while naming the wrong values?** Yes, but the licence then refuses.
- `lock_m_modules` takes whatever single sha256 sits on the lines naming a path, so a lock with a wrong value for
  `corr.py` parses. That was probed: `ffff…` is accepted by the parser.
- The licence's (e′) then compares that value with the file as hashed now, and refuses.
- The WEIGHTS line likewise: (g) compares the revision with the hub cache's `refs/main` and recomputes the binding.
- The parsers can never make the licence pass when it should not. In the stage, (e′) and (g) are the binding checks
  for these keys.

**Is (f) still a check for these keys?** Not for these keys. With the values read from the lock's own text, (f)
holds by construction for `m_module_sha256`, `weights_revision` and `weights_sha256` (NOTE-1). (f) remains a real
check for the two flag-borne hashes, the analyzer's and the package's. That is sound: the values are the lock's,
by construction rather than by an operator-typed flag that (f) then has to check.

**Too strict for the real lock?** No.
- In LOCK-m-F3.md at `a28bef6` each of the eleven m paths is named on exactly one line (:97-107), and there is
  exactly one WEIGHTS line (:112).
- The self-test's identity and licence checks pass on it: the licence comes out `[]` with `HF_HUB_OFFLINE=1`.
- The parsers fail safe on later revisions (NOTE-2).

**Is reading these from the lock sound against (e′), (f) and (g)?** Yes, as above. The checkpoint's identity and
licence record `m_module_sha256` and the weights, so a resume under other values is refused. The pre-load window
between (g)'s read of `refs/main` and the snapshot check's read is NOTE-3.

## 4. The precheck

**Before the load** it checks:
- the licence (a)-(g);
- `startup_problems` on the named proposal;
- the renders of record;
- the six committed time schedules;
- the checkpoint path, ENDED, and an existing checkpoint without `--resume` and with no end pending;
- m:267's checklist;
- the gate line, and CLAUDE.md and the analyzer committed.

`run_time` adds the driver check and the snapshot check, and refuses once.

**The stage makes each of these again after the load** (`_begin`, `_licensed`, `_renders_of_record`,
`load_committed`, `rs.load_or_init`). The one exception is the looping link at the checkpoint path, which only the
precheck refuses. **Made only after the load:**
- the provenance check;
- `runner.f3_startup`'s pins;
- the counts against the committed n;
- `bars.assert_firing_complete()`;
- `_locked`;
- `_record_licence`.

The last four are model-free; m did not make them before the load either.

**Nothing m's precheck makes for `time` is missing.**

## 5. The self-test

**Checks that assert what their labels claim:**
- the identity and its licence;
- the parsers;
- the constants (but see NOTE-5);
- the 21 fake-cache snapshot cases;
- the 20 pre-load refusals (the loader trapped, the stage trapped, the test root's hashes unchanged);
- reach-load (DRIVER before SNAPSHOT, then the loader);
- the four post-load cases;
- the stub PASS run;
- the ended STOP.

**Over-claims and vacuous passes:** MINOR-1, NOTE-6, NOTE-7. Mutation table at the end.

## 6. Scope

- The worktree's `git status` shows only `scripts/mf3_sessions.py`; nothing under `valence_core/` changed.
- The driver still refuses `id`, `qual` and `campaign`: exit 2, the refusal text, checked at :528-533. `time` has
  left `REFUSED_CMDS`.
- The edit moves a file that G-SHAPE-F3's canonical artifact records (NOTE-10).

## 7. Blinding

The new code prints nothing pick-bearing.
- The DRIVER, SNAPSHOT and re-read lines carry paths, hashes, revisions and the model id. REFUSED lines carry
  check problems: paths, hashes, flags.
- An ENDED STOP checkpoint is named through `m_resume._stop_words`, the blinded class only.
- STOP lines carry the stage's own SystemExit messages, as m's driver does. None interpolates a pick, a label or a
  per-line list; the full list in stages.py, runner.py and resume.py was read.
- No totals reach print, since the line is sealed at source (NOTE-5).
- The self-test checks the stub run's stdout for roster labels, case-sensitively (NOTE-7). Its contents were not
  read separately.

---

## Findings

### MINOR-1 — The seam and ended calls run the production path with no loader trap

**Where.** The seam check's "loader never reached" conjunct is vacuous, and the time checks' safety claim
over-states its mechanism. Lines :565-568 (the `_selftest_time` docstring), :884-891 (the seam call and its check),
:973-981 (the two ended-checkpoint calls) and :982-985 (the final check's label).

**What happens.**
- The docstring says that "every case that reaches the stage path without a stub factory also traps
  stages.run_gate_stage, writes under a test root only (stages.DEFAULT_OUT patched) and stubs m:267's laptop
  checklist". The final check's label says "loaded nothing … (the loader a trap throughout …)".
- But the seam call `run_time(**tflags, resume_run=False, out_root=base / "seam")` runs the production function
  with nothing patched. Its conjunct `len(loads) == n0` cannot fail, because `_load_qwen` is not `t_loader` during
  that call. Were the real loader reached, `loads` would not change.
- The two ended re-invocations also run with `_load_qwen` unpatched. Only their factory keeps them off the Qwen
  branch.
- The final check asserts only the `data/mf3` hashes. It asserts nothing about loads.

**Failure scenario.** A regression drops the out-root refusal at :442, as mutant `seam_through` does. The
self-test's seam call then runs, for real:
- the identity;
- the precheck (the real licence, and the real laptop checklist: AC power, the one-process check, disk);
- `driver_problems`;
- `qwen_snapshot`.

Run in the clone with the lock and the driver committed, `HF_HUB_OFFLINE=1` and the 140 W adapter, every real check
passed except one: "schedules: SCHEDULES NOT CLEAN at …/seam/schedules". That fires only because the seam root
happens to hold no schedule files, so it was refused with exit 2. With schedule files under the same kind of root,
the same call printed the DRIVER line (seen) and, in the code's order, the SNAPSHOT line, then reached
`_load_qwen`. My patch trapped it there; in an unpatched self-test that is the real Qwen load
(`review/harness/state_probe.py seam`).

The check does still fail on the mutant, by its message, so the regression would be reported. But one regression
leaves only an incidental barrier between the self-test and the model. The code as written is safe; the tests'
stated mechanism is not what protects it.

**Fix.** Run the seam call and both ended calls inside the same `ExitStack` patches `time_q` uses (`t_loader`,
`t_stage`, `DEFAULT_OUT`, `preflight_laptop`). Assert `len(loads) == n0` with `_load_qwen` actually patched, and
have the final check assert that no trap was reached, or correct its label.

**Confirmed by running:** yes. The `seam_through` mutant was committed in the clone and both cases were run
(state_probe seam (a) and (b)). The vacuity is confirmed by reading.

### MINOR-2 — `driver_problems` checks the canonical path, not the running file

**Where.** :65 and :333 (against m:626 and m:983-1000). In mf3, `DRIVER_REL` is the constant
`"scripts/mf3_sessions.py"`. m derives it from `__file__`.

**Failure scenario.** The stage is launched from an edited, untracked copy of the driver inside the repository
(any depth-1 path, so that REPO still resolves to the repository). Every check passes, and the DRIVER line records
the canonical committed blob's sha256 although other code ran. This breaks the step-10 read's Q2 condition, as the
PIN states it: "the value recorded is a value the run logged".

Probe, in the clone with the wired driver committed: an untracked copy `scripts/mf3_sessions_review_copy.py` (an
appended comment, sha256 `cd927f73…`) returned `([], '22a52598ee4928dc…')` from its own `driver_problems()`. That
is the canonical file's sha. m's form, applied to that file, returns "not committed at HEAD".

The routing's launch script uses the canonical path, so the record of record is unaffected.

**Fix.** In `driver_problems`, or before it in `run_time`, refuse unless
`Path(__file__).resolve() == (REPO / DRIVER_REL).resolve()`. Or derive `DRIVER_REL` as m does; the self-test's
scans use the constant, so the assertion is the smaller edit. Add a self-test case that loads a copy and expects
the refusal.

**Confirmed by running:** yes (`review/harness/state_probe.py driver_rel`).

### MINOR-3 — The self-test carries a subset of m's checks for this path

**Where.** `_selftest_time`, :564-985, against m:4020-4600. 18 of the 41 production-code mutants survive. Each
behaviour below is correct in the code today, as read and compared with m. The self-test would not catch a
regression in any of them.

**(a) Pre-load checks the routing named for this wiring, not pinned.**
- **The hub's own offline resolution:** `drop_hub_resolution` survives. m's tree-listing, called-once and
  other-directory cases are m:4169-4213.
- **The re-read's position after the load:** `reread_before_load` survives. m's snapshot, load, snapshot order
  check is m:4579-4592.
- **MLXLM_USE_MODELSCOPE in any case:** `modelscope_two_spellings` survives (m:4115-4123).
- **qwen_snapshot's production defaults** (HF_HUB_CACHE and os.environ read at call time):
  `snapshot_wrong_default_cache` survives (m:4125-4167).

**(b) Stage-path behaviours m's self-test pins and mf3's does not.**
- an ENDED checkpoint refused before the load, with and without `--resume` (`drop_refuse_ended`);
- CLAUDE.md committed (`drop_claude_committed`);
- the gate line's own problems (`drop_gate_line`);
- a lock that names the proposal by its sha16 only (`proposal_by_prefix`);
- the problems refused together in one REFUSED line (`refuse_not_together`; m's "multi" case, m:4510-4520);
- `--resume` reaching the precheck and the stage (`main_ignores_resume`, `precheck_ignores_resume`,
  `stage_resume_false`). `time_q`'s `resume_flag` is never set; m has the resume and end-pending clear cases and
  m:4299-4324.
- a STOP *returned* by the stage exiting 4 (`exit_ignores_status`): every G-TIME-F3 stub run passes, while m's has
  a fired sham bar;
- DRIVER and SNAPSHOT on stdout (`lines_to_stderr`): `run()` at :502-509 now returns stdout + stderr joined, and
  m's `capture` keeps them apart;
- the real `driver_problems` and `qwen_snapshot` through `run_time`, and planted driver answers
  (`driver_none_branch`; fail-safe through `dsha is None`);
- symlink loops at the proposal, lock and checkpoint paths;
- a lock-named file that is not a proposal (the banner check);
- absolute flag paths.

**Failure scenario.** An edit that moved the re-read before the load, or dropped the hub's own resolution, or
reported a G-TIME-F3 STOP as exit 0, would pass 149/149.

**Fix.** Port m's cases under mf3's names. That means the 11 refusal cases mf3 lacks, the multi case, the
resume and end-pending clear cases, the order check, the hub-resolution, production-defaults and modelscope cases,
and a stub run that STOPs. Keep stdout and stderr apart in the time checks.

**Confirmed by running:** yes. All 18 survivors were run.

### NOTEs

1. **(f) tautological for lock-read keys.** (f) holds by construction for `m_module_sha256` and the weights; (e′)
   and (g) carry those keys. The wiring entry could say so.
2. **The parsers fail safe.** Probed:
   - They accept two identical WEIGHTS lines, and an unanchored `XWEIGHTS`.
   - They refuse a backticked model id, with a confusing message.
   - They would refuse a later lock that quotes an old WEIGHTS line, or that names an m file beside another hash on
     any line.
3. **Pre-load revision not compared.** The snapshot check's revision (:456) is never compared with
   `extra["weights_revision"]`. (g) read `refs/main` earlier in the precheck; a move between the two reads is caught
   only after the load, as LICENCE REFUSED, STOP 4. m made the same comparison for qual and campaign before the load
   (m:1615-1617). The fix is one line.
4. **The factory seam is not stub-only.** A non-stub `adapter_factory` skips the driver check, the snapshot check
   and the DRIVER and SNAPSHOT lines (:453, :480). m's seam is the same, and the CLI cannot reach it.
5. **Redaction is a guard on a sealed form.** `TOTALS_RX` cannot match a live line, because resume seals the totals
   at source (TOTALS_SEALED). So the surviving `say_no_redact` and `precheck_no_redact` are harmless. The constants
   check's label says "the redaction's pattern" but compares `TOTALS_REDACTED` (:686).
6. **Two labels over-claim.**
   - The stub check claims "reads" but asserts only the report file.
   - The reach-load check matches only the DRIVER prefix, not m's full-line regex.
7. **The stub path's blinding scan is weaker than m's.** It is case-sensitive and covers stdout only. m's
   `stdout_problems` uses re.I, menu fragments and pick lines.
8. **Message and stream drift.** The top-level-flags refusal wording differs from m's. Refused `id`, `qual`,
   `campaign` and "no action" still print to stdout (pre-existing; m uses stderr).
9. **Docstring imprecision.** :20-23 says the identity is "refused together" with the precheck. It is refused
   first, alone, in m's order.
10. **A recorded hash goes stale.** G-SHAPE-F3's canonical artifact records `provenance.sources
    ["scripts/mf3_sessions.py"] = fad31c20…`, HEAD's pre-edit blob. After the wiring commit, a map check of
    "recorded = HEAD" fails for that entry. F-1 clears the re-run, but the entry should name it. Also stale:
    LOCK-m-F3 §9's F57 row and stages.py's module docstring ("none is wired in the driver").
11. **No help strings.** The `time` flags have none; m's have.
12. **`me = sys.modules[__name__]` (:577) is fragile.** It assumes the running module is registered under its own
    name, which holds for script, `-m` and runpy runs. `run_time.__globals__` would be robust.
13. **(g)'s offline condition is not pinned through the precheck.** `licence_env_forced` survives. In production,
    qwen_snapshot's own check still refuses.

---

## Mutation results

41 single mutants of the production code. Each ran with the driver's integration checks under the trapped harness
with `HF_HUB_OFFLINE=1`. Every run: no trap hit, no watched `data/mf3` changed.

| # | mutant | what it changes | result | killed by |
|---|---|---|---|---|
| 1 | drop_preflight | m:267's checklist removed from the precheck | killed | refusals (20) |
| 2 | swap_driver_snapshot | SNAPSHOT line printed before DRIVER | killed | reach-load |
| 3 | skip_reread | post-load re-read replaced by the pre-load answer | killed | post-load |
| 4 | load_before_precheck | `_load_qwen()` before `time_precheck` | killed | refusals; reach-load |
| 5 | load_before_lines | load before the DRIVER and SNAPSHOT lines | killed | reach-load |
| 6 | accept_other_lock | the LOCK-m-F3.md test removed | killed | refusals ("other lock") |
| 7 | drop_proposal_in_lock | proposal-in-lock test removed | killed | refusals |
| 8 | accept_two_weights | two different WEIGHTS lines accepted | killed | parsers |
| 9 | accept_two_m_sha | an m file with two sha256 accepted | killed | parsers |
| 10 | seam_through | out root without a factory not refused | killed | seam check (by message; MINOR-1) |
| 11 | say_no_redact | `_say` skips redact_totals | **survived** | — |
| 12 | precheck_no_redact | precheck skips redact_totals | **survived** | — |
| 13 | say_to_stdout | REFUSED and STOP to stdout | killed | seam; ended |
| 14 | lines_to_stderr | DRIVER and SNAPSHOT to stderr | **survived** | — |
| 15 | drop_refuse_ended | precheck's ENDED refusal removed | **survived** | — |
| 16 | drop_gate_line | `gate_line()` problems dropped | **survived** | — |
| 17 | drop_claude_committed | CLAUDE.md dropped from the committed loop | **survived** | — |
| 18 | main_ignores_resume | `main` passes `resume_run=False` | **survived** | — |
| 19 | stage_resume_false | stage called with `resume=False` | **survived** | — |
| 20 | precheck_ignores_resume | EXISTS refused even with `--resume` | **survived** | — |
| 21 | drop_driver_check | `driver_problems` not called | killed | refusals; reach-load |
| 22 | drop_snapshot_probs | snapshot problems not added to the refusal | killed | refusals |
| 23 | drop_model_id | MODEL ID STOP removed | killed | post-load |
| 24 | drop_moved | SNAPSHOT MOVED STOP removed | killed | post-load |
| 25 | main_top_flags | `time` with a top-level `--out` or `--build-schedules` not refused | killed | refusals |
| 26 | exit_ignores_status | exit 0 whatever the stage's status | **survived** | — |
| 27 | precheck_default_root | precheck reads data/mf3, not the run's root | killed | refusals |
| 28 | drop_licence | licence dropped from the precheck | killed | refusals |
| 29 | stop_returns_2 | a SystemExit STOP returns 2 | killed | reach-load; post-load; ended |
| 30 | weights_any_model | WEIGHTS for another model accepted | killed | parsers |
| 31 | licence_env_forced | precheck's licence forced to `HF_HUB_OFFLINE=1` | **survived** | — |
| 32 | snapshot_offline_any | any set `HF_HUB_OFFLINE` accepted | killed | fake caches |
| 33 | drop_hub_resolution | the hub's own offline resolution removed | **survived** | — |
| 34 | drop_local_path | local-path refusal removed | killed | fake caches |
| 35 | stub_default_root | `out_root` ignored (default root) | killed | stub run; ended |
| 36 | reread_before_load | re-read moved before the load | **survived** | — |
| 37 | refuse_not_together | precheck refused before the driver and snapshot checks run | **survived** | — |
| 38 | modelscope_two_spellings | only `'True'` and `'true'` refused | **survived** | — |
| 39 | snapshot_wrong_default_cache | default cache `HF_HOME`, not `HF_HUB_CACHE` | **survived** | — |
| 40 | proposal_by_prefix | lock need name only the proposal's sha16 | **survived** | — |
| 41 | driver_none_branch | unreadable driver gives `([], None)` | **survived** | — (fail-safe through `dsha is None`) |

**Killed 23, survived 18.**

## Artifacts

All under `scratchpad/time/review/`:
- `harness/`: `trapped_selftest.py`, `state_probe.py`, `parser_probe.py`, `make_mutants*.py`, `run_mutants*.sh`,
  `fn_diff*.py`;
- `mutants/` and `mutants2/`: the mutated drivers;
- `mut_logs_*.txt`, `mut2_logs_*.txt`, `mutant_results*.txt`: the mutant runs;
- `baseline_*.txt`, `committed_full_off1.txt`: the baselines and the committed-state run;
- `clone/`: 467 MB, restored to `a28bef6` plus the wired driver. It can be deleted.

## Code's dispositions of round 1 (2026-11-07; each finding re-checked at source before it was applied)

- **MINOR-1: the seam call and the two ended calls ran the real path unpatched.** Confirmed by reading: the seam
  call patched nothing, so its `len(loads) == n0` could not fail.
  - Applied: the seam call now runs with the loader trap, the stage trap, a test-root `DEFAULT_OUT` and the
    checklist stubbed, and it asserts that neither trap was reached.
  - Every stub-factory run (`stub_run`) has the loader trapped and `DEFAULT_OUT` set to a test root.
  - The final check asserts the traps' counts over the whole battery: the loader 3 times (the three cases that
    clear every pre-load check) and the stage once (the post-load case that reaches it). Its label says so.
- **MINOR-2: `driver_problems` checked the canonical path, not the running file.** Confirmed: the review's
  `driver_rel` probe on a copy returned the canonical blob's sha. Applied: `driver_problems` refuses unless
  `Path(__file__).resolve()` is `REPO/DRIVER_REL`. A self-test case runs it with `__file__` set to a copy's path
  ("driver: this process runs").
- **MINOR-3: the self-test carried only part of m's checks.** Applied, under mf3's names:
  - the hub's own offline resolution (m's tree-listing case, the call's arguments, a resolution elsewhere, and a hub
    that raises);
  - the order snapshot → load → re-read, recorded;
  - MLXLM_USE_MODELSCOPE in four letter cases, with 'False' clear;
  - qwen_snapshot's production defaults (HF_HUB_CACHE and os.environ read at call time);
  - an ENDED checkpoint before the load, with and without --resume;
  - CLAUDE.md uncommitted, and the gate line's own problems;
  - a lock naming the proposal by sha16 only;
  - all problems refused in one REFUSED line ("multi");
  - --resume through the precheck (an open checkpoint passes to the loader) and through the stage (an interrupted
    stub run resumed to PASS, only A3 and A3s launched);
  - the stage's status mapped to the exit code (PASS 0, STOP 4);
  - stdout and stderr kept apart in every time case;
  - the real driver and snapshot checks through `run_time`;
  - a looping link as the proposal and at the checkpoint path;
  - a lock-named file that is not a proposal (`startup: banner`);
  - absolute flag paths.
  The refused-case battery grew from 20 to 33 cases. The self-test is 149 → 156 checks, 156/156.
- **NOTE 1** (f) by construction: no change. The reading is declared in the design raw.
- **NOTE 2, the parsers:** the WEIGHTS pattern is anchored with `\b`, and a case refuses a glued "XWEIGHTS". A
  backticked model id still refuses, with the model-id message (fail-safe; declared).
- **NOTE 3, the pre-load revision:** applied. `run_time` refuses, before the load, a snapshot revision other than the
  lock's weights revision (m's REVISION_STAGES refusal, carried), and a case covers it.
- **NOTE 4, the seam accepts a non-stub adapter:** no change. It is m's seam, and the CLI cannot reach it (declared).
- **NOTE 5, the redaction label:** applied. The check now compares TOTALS_RX's pattern with m's as well.
- **NOTE 6, the stub check's label and the DRIVER line's prefix:** applied. The reads file is asserted, and the
  DRIVER line is compared in full, HEAD included.
- **NOTE 7, the blinding scan:** applied. Labels are searched in any letter case, over stdout and stderr, in the stub
  run and in every refused case.
- **NOTE 8, the top-level refusal's form:** applied, m's form `refused: time takes no --selftest / --build-schedules
  / --out` on stderr. `id`, `qual`, `campaign` and "no action" keep stdout: the stream is unchanged. Their texts
  change with the wiring ("is not wired yet"; "… gshape or time") (declared).
- **NOTE 9, the docstring's "together":** applied. The identity is refused on its own, then the rest together.
- **NOTE 10, G-SHAPE-F3's tooling map and the unwired-stage texts:** no code change. The wiring's entry names
  G-SHAPE-F3's recorded blob of the driver and the new one, under F-1. F57's register row and `stages.py`'s docstring
  are left: the first is the build's record, and editing the second would move mf3's package. LOCK-m-F3 v0.2
  records the driver.
- **NOTE 11, help strings:** applied.
- **NOTE 12, `sys.modules[__name__]`:** applied. The module's globals are patched through `mock.patch.dict(globals())`.
- **NOTE 13, the licence's offline condition through the precheck:** applied, with a case run unpatched and
  HF_HUB_OFFLINE removed ("licence: weights: HF_HUB_OFFLINE is None").

---

# Round 2

# Blind review r2: the `time` wiring of scripts/mf3_sessions.py (G-TIME-F3)

**Reviewed:** the worktree `scratchpad/wire-wt`, detached at `a28bef6` (the scratch lock commit).
`scripts/mf3_sessions.py` is modified there:
- sha256 `64fc9ad1daa39604…`, 1,309 lines (HEAD's has 240).
- The whole edit is `git diff` against HEAD: +1,096 / −27.
- The change since round 1 (`22a52598…` → `64fc9ad1…`) is `review2/r1_to_r2.diff` (874 lines).

The reference is `scripts/m_sessions.py` on main. Line numbers are the revised driver's unless prefixed `m:`.

**Read-only:**
- Main has no tracked change. Its HEAD moved from `02dadb3` to `1e79955` during the review. That commit is LOCK-m-F3
  v0.1, committed by another session, not by this review (NOTE-12).
- wire-wt is still at `a28bef6`, and its driver is still `64fc9ad1…`.
- Nothing was written under any `data/`. Every harness run trapped in-process writes under main's, wire-wt's and the
  review copy's `data/`. It also watched `data/mf3` in all three by sha256 and by mtime.
- The write trap fired twice, both times on a mutant's route into a review copy's `data/mf3/schedules`. Each was an
  `os.mkdir` with `exist_ok`; the trap refused it and no file was written (NOTE-1).

**Verdict: 0 MAJOR, 1 MINOR, 12 NOTEs.**
- All three of round 1's MINORs are resolved in substance:
  - MINOR-1 and MINOR-2 are resolved, and correctly.
  - MINOR-3 is resolved except for a residue, which is MINOR-1 below.
- 38 of round 1's 41 mutants are now killed (round 1 killed 23). The 3 survivors are equivalent.
- Of 33 new mutants, 20 are killed and 13 survive:
  - 5 are real gaps, folded into MINOR-1;
  - 3 are label over-claims or an unpinned form;
  - 5 are equivalent.
- No self-test case can load the model or write `data/mf3` with the code as written, in any state tried:
  - the driver uncommitted and committed;
  - `a28bef6`'s scratch lock and `1e79955`'s committed lock;
  - `HF_HUB_OFFLINE` unset and `=1`;
  - AC power, with the real hub cache present.
- Two cases are each one regression away from a side effect other than the load:
  - a write into `data/mf3/schedules`, or a recursive self-test (NOTE-1);
  - a Hub download into temporary caches (NOTE-2).

## Method

**Copies.**
- `review2/clone` is a copy of round 1's clone (a `git clone --shared` at `a28bef6`), with the revised driver. A
  `diff -rq` against wire-wt, excluding `.git`, shows no difference.
- `lane1`–`lane8` are APFS copy-on-write copies of it (`cp -Rc`):
  - `lane5` has the revised driver committed: the committed state.
  - `lane6` has the `seam_through` mutant committed.
  - `lane8` is checked out at `1e79955`, with the revised driver. Between `a28bef6` and `1e79955` only
    `LOCK-m-F3.md`, `RESULTS.md` and two raws differ; nothing under `data/` does.

**Harness** (`review2/harness/trapped_selftest2.py`). It keeps round 1's traps:
- `valence_core.adapters.qwen_or_explain`, `get_adapter` and `QwenMLXAdapter` replaced by traps;
- any import of `mlx`, `mlx_lm` or `jlens_qwen` blocked.

It adds four more:
- **a write trap** on any path under main's, wire-wt's or the copy's `data/`. It covers `open` and `io.open` in write
  modes, `os.open` with write flags, and `os.replace`, `rename`, `mkdir`, `symlink`, `link`, `unlink`, `remove`,
  `rmdir`, `utime` and `chmod`;
- **a network trap** on every IPv4 and IPv6 connect;
- **a trap on a nested `run_selftest`**;
- **a watch** on `data/mf3` in all three trees, by sha256 and mtime, before and after.

**Baselines.** No run hit a trap or changed a watched tree.

| state | mode | `HF_HUB_OFFLINE` | result |
|---|---|---|---|
| uncommitted | full self-test | unset | 156/156 |
| uncommitted | full self-test | `1` | 156/156 |
| uncommitted | driver checks only | `1` | 32/32 |
| uncommitted | driver checks only, network trap on | unset | 32/32 |
| committed (`lane5`: lock and driver committed, AC power, real hub cache) | full self-test | `1` | 156/156 |
| `1e79955`'s committed lock (`lane8`), driver uncommitted | full self-test | `1` | 156/156 |

**Mutation.**
- Each mutant was copied over a lane's canonical driver path. The driver's checks then ran under the harness, with
  `HF_HUB_OFFLINE=1`.
- Four lanes ran in parallel. The original driver was restored after each lane, and its sha256 checked.
- Parallel lanes cannot change an outcome: the time checks stub m:267's preflight everywhere, so the real one
  (`pgrep`) never runs.

**Probes** (`review2/harness/state_probe2.py`):
- `driver_problems` on copies of the driver, uncommitted and committed;
- the revision check through `run_time` against the real lock.

## 1. Round 1's findings, re-derived at source

### MINOR-1 — resolved, correctly

What the revision does:
- **The seam call** (:1143-1157) now runs inside an `ExitStack` that points `stages.DEFAULT_OUT` at a test root and
  traps `stages.run_gate_stage`, `guard.preflight_laptop` and `_load_qwen`. Its conjuncts on the loader and the stage
  are now live.
- **The two ended calls** now go through `stub_run` (:929-945). It traps `_load_qwen` and points `DEFAULT_OUT` and
  `GATES_DIR` at test directories.
- **The final check** (:1229-1234) asserts the trap counts: the loader 3 times, the stage once.
- **The docstring** (:581-585) now states the mechanism accurately.

Confirmed by running:
- `seam_through` was committed in the committed state (`lane6`). Every real pre-load check passed, and the call
  reached the self-test's own loader trap.
- The seam check and the final count check (4 loads) failed, and no harness trap fired.
- In round 1 the same scenario reached the real `_load_qwen` call site.

Residue: NOTE-1 and NOTE-2.

### MINOR-2 — resolved, correctly

What the revision does:
- `driver_problems` (:336-342) refuses unless `Path(__file__).resolve() == (REPO / DRIVER_REL).resolve()`.
- The case "driver (a copy running)" (:1104-1106) pins it; mutant n01 is killed.

Probe (`state_probe2.py driver_rel`), in both states:
- refused: an edited copy beside the driver (`scripts/mf3_sessions_review_copy.py`), and a same-name copy in another
  directory of the repository;
- clear once committed, returning `64fc9ad1…`: the driver of record, a symlink to it, and the driver loaded with a
  relative `__file__`.

Residue:
- The self-test pins only a differently named copy (n03, MINOR-1).
- The self-test now passes only when run from the canonical path (NOTE-4).

### MINOR-3 — largely resolved; residue in MINOR-1

- 15 of round 1's 18 surviving mutants are now killed (table below).
- Refusal cases: m had 11 that mf3 lacked. 10 are now carried; m's "loop lock" is still missing. mf3 adds 3 of its own,
  for 33 in all.
- Also now ported: the multi case, the resume-open clear case, the order check, the hub's own resolution, the
  production defaults, and modelscope in any letter case.
- stdout and stderr are kept apart (`run3`, :614-622).
- **Not carried:** the end-pending clear case, which round 1's fix named. See MINOR-1.

### Round 1's NOTEs

| r1 | status | at source |
|---|---|---|
| NOTE-1 | open, for the entry | no code change is needed; n39 shows the identity check cannot tell the lock's values from the files' (NOTE-3) |
| NOTE-2 | partly resolved | `XWEIGHTS` is refused by `\b` (:101), pinned by `p_glued` (:680), n12 killed; `OLD-WEIGHTS` is still read as a WEIGHTS line, a backticked id is still refused confusingly, and identical duplicates are accepted, all fail-safe (NOTE-7) |
| NOTE-3 | resolved | :467-472 refuses before the load any refs/main other than the lock's `weights_revision`; pinned by "snapshot revision not the lock's" (:1111), n06 and n07 killed; the probe shows the lock's revision reaching the loader and another refused (`snapshot: refs/main is eeee…, not the lock's weights revision c000ac2c…`); naming: NOTE-6 |
| NOTE-4 | open, as in m | unchanged (m's seam) |
| NOTE-5 | partly resolved | TOTALS_RX's pattern is now compared with m's (:733; `assigned` now reads `re.compile`'s argument), n21 killed; the new label is inaccurate (NOTE-3); `say_no_redact` and `precheck_no_redact` still survive, both equivalent |
| NOTE-6 | resolved | the stub check asserts the reads file (:957); reach-load compares the whole DRIVER line (:1168) |
| NOTE-7 | partly resolved | `labelled` (:636) is case-insensitive and scans stdout and stderr, in the stub check and every refusal case; m's menu-fragment and pick-line scans (m:1816-1821) are not carried (NOTE-11) |
| NOTE-8 | partly resolved | the top-level-flags refusal is now m's form, to stderr (:1288 = m:7563); refused `id`, `qual`, `campaign` and "no action" still print to stdout (pre-existing; NOTE-11) |
| NOTE-9 | resolved | :20-25 |
| NOTE-10 | open | NOTE-10 below |
| NOTE-11 | resolved | help strings at :1275-1279 (NOTE-9 below) |
| NOTE-12 | resolved | `G = globals()` (:596) and `mock.patch.dict(G, …)` (:610-612); patch.dict restores by clearing and re-filling the module dict, which is safe here: exits are LIFO, nothing assigns module globals at run time (no `global`, no caches), and there is one thread |
| NOTE-13 | resolved | case "licence (g), offline" (:1082); `licence_env_forced` killed |

## 2. Mutation

### Round 1's 41 mutants

**Mapping.** Each of round 1's replacements (`review/harness/make_mutants.py`, `make_mutants2.py`) applied unchanged
to the revised bytes, exactly once each (asserted), so none had to be regenerated.

Where the code around the mutated text moved, two mutants now do more:
- **`drop_snapshot_probs`** also drops the new revision refusal, whose problem is appended to `sprobs` just above the
  mutated line.
- **`main_top_flags`** now routes `--build-schedules time` to `build_schedules(None)`. The write trap caught
  `os.mkdir` on the copy's `data/mf3/schedules`.
  - Round 1's run of this mutant had no write trap and took the same route.
  - There, `write_schedule_files` found every file identical and wrote nothing.

**Result: killed 38, survived 3, all three equivalent.** The short names in "killed by" are listed after the
table.

| # | mutant | result | killed by |
|---|---|---|---|
| 1 | drop_preflight | killed | refusals{preflight}; multi; final counts |
| 2 | swap_driver_snapshot | killed | reach-load |
| 3 | skip_reread | killed | post-load; final counts |
| 4 | load_before_precheck | killed | refusals{a lock-named non-proposal, licence (d) (e) (f) (g), renders}; multi; reach-load; post-load; final counts |
| 5 | load_before_lines | killed | reach-load |
| 6 | accept_other_lock | killed | refusals{other lock} |
| 7 | drop_proposal_in_lock | killed | refusals{proposal not in lock, sha16 only} |
| 8 | accept_two_weights | killed | parsers |
| 9 | accept_two_m_sha | killed | parsers |
| 10 | seam_through | killed | seam (committed state: also final counts, 4 loads) |
| 11 | say_no_redact | **survived** | equivalent: TOTALS_RX cannot match a live line, because resume seals the totals at source (m.resume.TOTALS_SEALED) |
| 12 | precheck_no_redact | **survived** | equivalent, as 11 |
| 13 | say_to_stdout | killed | stub-ended; stub-resume; refusals (all); multi; seam; reach-load; … |
| 14 | lines_to_stderr | killed (r1 survivor) | reach-load |
| 15 | drop_refuse_ended | killed (r1 survivor) | refusals{ended, ended --resume}; final counts |
| 16 | drop_gate_line | killed (r1 survivor) | refusals{gate line}; final counts |
| 17 | drop_claude_committed | killed (r1 survivor) | refusals{gate line CLAUDE.md}; final counts |
| 18 | main_ignores_resume | killed (r1 survivor) | abs+resume-open; final counts |
| 19 | stage_resume_false | killed (r1 survivor) | stub-resume |
| 20 | precheck_ignores_resume | killed (r1 survivor) | abs+resume-open; final counts |
| 21 | drop_driver_check | killed | refusals{driver, driver (real check), driver (a copy running)}; multi; reach-load; final counts |
| 22 | drop_snapshot_probs | killed | refusals{snapshot, snapshot (real check), snapshot revision not the lock's}; multi; final counts |
| 23 | drop_model_id | killed | post-load; final counts |
| 24 | drop_moved | killed | post-load; final counts |
| 25 | main_top_flags | killed | refusals{top-level --out, --build-schedules}; final counts; write trap on `os.mkdir` of the copy's `data/mf3/schedules` |
| 26 | exit_ignores_status | killed (r1 survivor) | exit codes |
| 27 | precheck_default_root | killed | refusals{exists, ended, ended --resume, checkpoint loop, schedules}; final counts |
| 28 | drop_licence | killed | refusals{licence (d) (e) (f) (g)}; final counts |
| 29 | stop_returns_2 | killed | stub-ended; stub-resume; reach-load; abs+resume-open; post-load |
| 30 | weights_any_model | killed | parsers |
| 31 | licence_env_forced | killed (r1 survivor) | refusals{licence (g), offline}; final counts |
| 32 | snapshot_offline_any | killed | fake caches |
| 33 | drop_hub_resolution | killed (r1 survivor) | hub resolution |
| 34 | drop_local_path | killed | fake caches |
| 35 | stub_default_root | killed | stub run; stub-ended; raised (`CHECKPOINT UNREADABLE` at the resume read, so the remaining time checks are skipped: NOTE-5) |
| 36 | reread_before_load | killed (r1 survivor) | post-load (the order) |
| 37 | refuse_not_together | killed (r1 survivor) | multi |
| 38 | modelscope_two_spellings | killed (r1 survivor) | modelscope |
| 39 | snapshot_wrong_default_cache | killed (r1 survivor) | production defaults |
| 40 | proposal_by_prefix | killed (r1 survivor) | refusals{sha16 only} |
| 41 | driver_none_branch | **survived** | equivalent: `stages.committed` never returns `([], None)` (stages.py:210-244), and `run_time` refuses `dsha is None` regardless |

The short names refer to these checks:
- **refusals{…}**: the 33-case refusal check, with the failing cases in braces;
- **final counts**: the last check (the `data/mf3` hashes and the trap counts);
- **reach-load**: every pre-load check clear, the DRIVER and SNAPSHOT lines, the loader;
- **post-load**: the re-read, the moved revision, the model id and the order;
- **abs+resume-open**: absolute flag paths, and `--resume` on an open checkpoint.

### New mutants (33), for the code added since round 1

`review2/harness/make_mutants_r2new.py` (31) and `make_mutants_r2extra.py` (2). **Result: killed 20, survived 13.**

**driver_problems' running-file check:**

| mutant | change | result | killed by / ruling |
|---|---|---|---|
| n01_here_check_dropped | the running-file `if` removed | killed | refusals{driver (a copy running)} |
| n02_here_check_fail_open | on a resolve error, `here = (REPO/DRIVER_REL).resolve()` | survived | equivalent: resolving the running file's own path cannot raise in a normal run |
| n03_here_check_name_only | compares only file names | survived | **real gap** (MINOR-1 d) |

**run_time's snapshot revision against the lock's:**

| mutant | change | result | killed by / ruling |
|---|---|---|---|
| n06_rev_check_dropped | the check removed | killed | refusals{snapshot revision not the lock's}; final counts |
| n07_rev_check_inverted | `!=` changed to `==` | killed | refusals; reach-load; abs+resume-open; post-load; final counts |
| n08_rev_check_vs_code_constant | compares with `gshape.QWEN_REVISION` | survived | equivalent in this tree: gshape's constant is the lock's WEIGHTS revision (`c000ac2c…`), and the fake snapshot uses it |
| n09_rev_check_no_none_guard | the `snap is not None` guard dropped | killed | raised (TypeError) |
| n11_rev_check_vs_lock_sha | compares with `weights_sha256` | killed | reach-load; abs+resume-open; post-load; final counts |

**The anchored WEIGHTS pattern:**

| mutant | change | result | killed by / ruling |
|---|---|---|---|
| n12_weights_unanchored | `\b` removed | killed | parsers (the glued case) |
| n13_weights_bullet_anchor | `(?m)^- WEIGHTS` | survived | equivalent on every text parsed: the real lock's line and the synthetic lines all start `- WEIGHTS` |

**The top-level refusal's form:**

| mutant | change | result | killed by / ruling |
|---|---|---|---|
| n15_toplevel_to_stdout | the refusal printed to stdout | killed | refusals{top-level --out, --selftest, --build-schedules} |
| n16_toplevel_drop_build | `a.build_schedules` dropped from the condition | killed | refusals{--build-schedules}; **write trap** on `os.mkdir` of the copy's `data/mf3/schedules` (NOTE-1) |
| n17_toplevel_drop_selftest | `a.selftest` dropped from the condition | killed | refusals{--selftest}; **nested `run_selftest` trap** (unpatched, this recurses; NOTE-1) |
| n18_toplevel_round1_form | round 1's `_say("REFUSED: …; nothing loaded")` | survived | the form is not pinned (NOTE-8); cosmetic |
| n20_toplevel_any_cmd | `a.cmd == "time"` dropped | killed | raised in `_selftest` (`--build-schedules --out` refused) |

**Aimed at the new self-test cases:**

| mutant | change | result | killed by / ruling |
|---|---|---|---|
| n21_totals_rx_changed | `\S+` changed to `\d+` in TOTALS_RX | killed | constants |
| n22_modelscope_any_value | `if ms:` | killed | fake caches; modelscope ('False'); hub resolution; production defaults |
| n23_hub_online | `local_files_only=False` | killed | hub resolution; with `HF_HUB_OFFLINE` unset, 88 Hub connects were caught by the network trap (NOTE-2) |
| n24_env_or_default | `env = environ or os.environ` | killed | fake caches; production defaults |
| n25_identity_no_runtimeerror | RuntimeError dropped from the identity's `except` | killed | raised (symlink loop): "a looping link" |
| n26_startup_on_record_proposal | `startup_problems(stages.PROPOSAL_PATH)` | killed | refusals{a lock-named non-proposal}; final counts |
| n27_ckpt_no_resolve_catch | RuntimeError dropped from the checkpoint's `except` | killed | raised (symlink loop): the checkpoint-loop case |
| n28_driver_problems_swallowed | `return [], None` | killed | refusals{driver (real check)}; then raised (TypeError at :1227; NOTE-5) |
| n30_driver_line_short | ", working tree identical" dropped | killed | reach-load (the whole line) |
| n31_identity_rel_as_given | the identity keeps the flag as given | killed | abs+resume-open (`_extra` refuses an absolute path); final counts |
| n32_seam_after_identity | the out-root refusal moved after the identity | survived | **label over-claim**: "refuses before anything" (NOTE-3) |

**Gaps against m's self-test:**

| mutant | change | result | ruling |
|---|---|---|---|
| n33_precheck_refuses_pending | `and not rs.pending_at(cpath)` dropped | survived | **real gap** (MINOR-1 a) |
| n34_snapshot_cwd_default_repo | `REPO` in place of `Path.cwd()` | survived | **real gap** (MINOR-1 b) |
| n35_weight_backslash_allowed | the `"\\" in w` test dropped | survived | **real gap** (MINOR-1 c) |
| n36_weight_dotdot_allowed | `".."` allowed | survived | equivalent in outcome: still refused, as "incomplete", through `is_file` |
| n37_weight_empty_allowed | `""` allowed | survived | equivalent in outcome, as n36 |
| n38_precheck_licence_early_return | the precheck returns the licence's problems alone | survived | **real gap** (MINOR-1 e) |
| n39_m_modules_from_files | `m_module_sha256` from the files, not the lock | survived | **label over-claim**: "as the lock lists them"; fail-safe through (f) (NOTE-3) |

### What each new self-test case kills

"Unique" means no other check kills that mutant.

**Production-side checks:**
- parsers, glued case → n12 (unique).
- constants, TOTALS_RX → n21 (unique).
- modelscope in any case → modelscope_two_spellings (unique), n22.
- hub resolution → drop_hub_resolution (unique), n23 (unique), n22.
- production defaults → snapshot_wrong_default_cache (unique), n24, n22.

**The stub path:**
- stub ended, via `stub_run` → say_to_stdout, stop_returns_2, stub_default_root.
- stub resume → stage_resume_false (unique).
- exit codes → exit_ignores_status (unique).

**The new refusal cases:**
- "a looping link" → n25.
- "sha16 only" → proposal_by_prefix (unique).
- "a lock-named non-proposal" → n26 (unique).
- "licence (g), offline" → licence_env_forced (unique).
- "ended" and "ended --resume" → drop_refuse_ended (unique).
- "a looping link at the checkpoint" → n27.
- "gate line" → drop_gate_line (unique).
- "gate line CLAUDE.md" → drop_claude_committed (unique).
- "driver (real check)" → n28.
- "driver (a copy running)" → n01 (unique).
- "snapshot (real check)" → drop_snapshot_probs.
- "snapshot revision not the lock's" → n06 (unique).

**The Qwen path:**
- multi → refuse_not_together (unique).
- the seam, with traps → seam_through (unique).
- reach-load, whole line and streams → n30 and lines_to_stderr (each unique).
- abs+resume-open → n31, main_ignores_resume, precheck_ignores_resume.
- post-load order → reread_before_load (unique).

**Checks with no unique kill:**
- **Final counts** kills alongside 21 mutants (22 with committed seam_through) but is never the unique killer. It is a backstop, and it is sensitive both ways:
  - 2 loads under main_ignores_resume, precheck_ignores_resume and n31;
  - 2 stage reaches under drop_model_id, drop_moved and skip_reread;
  - 4 loads under committed seam_through.
- **The stub check's new conjuncts** (the reads file; stderr scanned, in any letter case) guard the stage's outputs, which no driver mutant reaches.

---

## 3. Findings

### MINOR-1 — Residue of round 1's MINOR-3: the self-test still leaves five behaviours unpinned (five surviving mutants)

**Where.** `_selftest_time` (:580-1234), against m:4020-4600.

**What.**
- **(a) The end-pending clear case.**
  - Production: the precheck lets a checkpoint whose end is pending through without `--resume`
    (:308, `not rs.pending_at(cpath)`).
  - m pins it (`t_pending`, m:4401; `rc_pe`, m:4523), and round 1's fix named it.
  - n33 drops the condition and survives.
- **(b) The local-path refusal's default directory.**
  - Production: `qwen_snapshot()` tests the process working directory (:376).
  - Every mf3 case passes `cwd=` explicitly. m pins the default (`w_default`, m:4217-4222).
  - n34, which tests `REPO` instead, survives.
  - This refusal is one of the five pre-load parts the routing names (lock §11 item 1).
- **(c) Weight names `..`, `''` and one with a backslash** (:398).
  - m pins all three at m:4228-4235.
  - n35 (a backslash allowed) survives.
  - n36 and n37 survive but are equivalent: the name is still refused, as "incomplete".
- **(d) The MINOR-2 fix, for a copy with the driver's own name.**
  - "driver (a copy running)" sets `__file__` to `<tmp>/copy.py`, so comparing file names alone passes (n03).
  - Production refuses a same-name copy in another directory (probe (c)).
- **(e) The multi case.**
  - mf3's multi (:1135-1142) stubs the licence clear and carries no renders problem.
  - m's (m:4510-4520) refuses the licence, renders, preflight, driver and snapshot problems in one line.
  - A precheck that returns the licence's problems alone passes (n38).
- **(f) Weaker forms.**
  - The loop at the lock path (m:4474) is absent.
  - The checkpoint-loop case expects only `"checkpoint: "` (:1088), where m names the Python version's message.
  - "exists" and "resume_open" plant `{}` (:1039-1042), not an open checkpoint; m builds one with
    `resume.load_or_init`.
  - A STOP's exit code is tested through a replaced stage (:986), not a stub run whose bar fires (m:4269). That is
    acceptable, since the mapping is what the driver owns.

**Failure scenario.**
- A refactor that resolves the local-path check against `REPO` (n34) passes 156/156.
- Launched from a directory other than the repository root that holds `mlx-community/Qwen3.6-27B-4bit/`, the run would
  not refuse, and mlx_lm would load that local directory.
- Nothing after the load would see it: the re-read reads the hub cache, and the model-id check compares the id string.
- The launch checklist runs from the repository root, where this mutant is equivalent.
- (a) fails closed: a re-finish is refused CHECKPOINT EXISTS until `--resume` is given.

**Fix.** Port m's cases under mf3's names:
- `w_default` and `w_names`;
- the pending clear case (a stub run cut after its end is written pending, as m's `t_pending` does);
- the loop-lock case;
- m's multi arguments;
- a same-name copy in another directory for "driver (a copy running)".

**Confirmed by running:** yes. n33, n34, n35, n03 and n38 survive, and so do the equivalent n36 and n37.

### NOTEs

**NOTE-1 — Three top-level-flag cases are protected only by the refusal they test (main's order is not m's).**

Where: :1113-1118, and main at :1287-1293.

What:
- The refusal (:1287) is the only barrier before `if a.selftest: return run_selftest()` and
  `if a.build_schedules: return build_schedules(a.out)`.
- `time_q` patches neither route.
- In m, the stage dispatch (m:7561-7570) comes before `--selftest` and `--build-schedules` (m:7580-7583). If m's
  refusal regresses, the call falls through to the trapped stage path.

If the refusal regresses:
- **`--build-schedules time`** runs `build_schedules(None)` on the canonical `data/mf3/schedules`.
  `write_schedule_files` makes the directory (`exist_ok`), skips identical files, writes any missing one, and refuses
  differing ones.
- **`--selftest time`** re-enters `run_selftest`. Its time checks reach the same case again, without bound.

Confirmed:
- main_top_flags and n16 each hit the write trap on `os.mkdir(<copy>/data/mf3/schedules)`.
- n17 hit the nested `run_selftest` trap.
- The code as written is safe.

Fix: patch `schedule.DEFAULT_OUT` (or `build_schedules`) and `run_selftest` with traps in `time_q`, or dispatch
`time` first, as m does.

**NOTE-2 — The self-test's real `snapshot_download` calls are offline only through the code under test.**

Where: :412 (production) and :779-901 (the self-test).

What:
- Every `qs`/`real_qs` case, and `rec_sd`'s pass-through, calls the real hub with `local_files_only=True`, the
  production argument under test.

Confirmed:
- n23 (`local_files_only=False`), run with `HF_HUB_OFFLINE` unset: 88 connects to huggingface.co:443, each caught by the
  network trap; 31/32.
- Unblocked, `snapshot_download` would fetch mlx_lm's allow-listed files, `model*.safetensors` included, into each
  temporary fake cache.

This is m's form (m:4183-4211).

Fix: patch `huggingface_hub.constants.HF_HUB_OFFLINE` to True around those cases. `is_offline_mode()` reads it at call
time (huggingface_hub 1.22.0).

**NOTE-3 — Three labels claim more than they assert.**
- **The seam check** (:1154) says "refuses before anything". It pins only "before the load": moving the refusal after
  the identity passes (n32).
- **The identity check** (:655) says "as the lock lists them". It compares with the files' hashes now: deriving
  `m_module_sha256` from the files passes (n39). That is fail-safe through (f).
- **The constants check** (:729) says "the redaction replaces the sealed totals form". The string it redacts is the old,
  unsealed form; the sealed form is `m.resume.TOTALS_SEALED`, which TOTALS_RX does not match. m calls the redaction "a
  guard on the old form" (m:839).

**NOTE-4 — The self-test passes only when run as `REPO/scripts/mf3_sessions.py`.**
- Run from a copy at another path, "driver (real check)" fails (31/32, confirmed): the running-file refusal fires
  before the planted answer.
- A mutation harness must overwrite the canonical path, and the failure does not say why.

**NOTE-5 — An exception anywhere in `_selftest_time` skips every later time check, the final one included.**

Two dependencies make that easier now:
- The Qwen-path cases depend on the stub path: `ended_ckpt = ck_p.read_bytes()` (:990), and `rs.read_checkpoint`
  (:970), which raises SystemExit on a missing file.
- The final driver check evaluates `hashlib.sha256(blob_d)` before `cp_d == []` (:1227), so it raises instead of
  failing.

Confirmed:

| mutant | checks recorded | raised |
|---|---|---|
| stub_default_root | 19/22 | `CHECKPOINT UNREADABLE` |
| n28 | 28/30 | TypeError |
| n09, n25, n27 | 23/24 each | — |

Each still reports a FAIL.

**NOTE-6 — The pre-load revision refusal (:467-472) is an extension of m's.**
- It extends m's REVISION_STAGES (qual and campaign; m:651, m:1615) to `time`.
- LOCK-m-F3 §11 item 1 (at both `a28bef6` and `1e79955`) lists the routed pre-load parts without it.
- Neither docstring names it.
- Name it in the wiring entry and in v0.2. Its comment's "carried" means extended to `time`.

**NOTE-7 — The WEIGHTS anchor is `\b`.** (:101; label :683)
- It refuses letter-, digit- and underscore-glued forms.
- It still reads `OLD-WEIGHTS …` as a WEIGHTS line. That is fail-safe: a second distinct value refuses.
- The label's "a word glued to it is none" holds only for word-glued forms.
- Round 1's backticked-id message is unchanged.

**NOTE-8 — The top-level refusal is m's verbatim (:1288 = m:7563), but only part of its form is pinned.**
- Pinned: stderr, "refused" in any letter case, and the phrase.
- Round 1's `_say("REFUSED: …")` form passes (n18). Cosmetic.

**NOTE-9 — Help strings** (:1275-1279).
- They are paired with TIME_FLAGS by `zip`. If TIME_FLAGS grew, `zip` would drop the new flag's `add_argument`
  silently, and argparse would then reject the flag.
- The wording differs from m's (m:7492-7503).

**NOTE-10 — Round 1's NOTE-10 is still open, with two more records to update.**
- G-SHAPE-F3's artifact records the pre-edit driver sha.
- LOCK-m-F3 §9's F57 row still reads "what is wired (selftest, schedules, hashes, gshape) and refused (the four
  stages)" (1e79955:502).
- `stages.py:12` is unchanged.
- New: 1e79955:432-433 says F57's site "carries no PIN line". The wiring adds nine PIN lines, each declared at
  LOCK-m-F3 v0.2 (m's precedent for its own time wiring).

**NOTE-11 — Round 1's NOTE-7 and NOTE-8 residue, all pre-existing.**
- m's menu-fragment and pick-line scans are not carried.
- Refused `id`, `qual`, `campaign` and "no action" print to stdout.
- `--selftest id` and `--build-schedules qual` run; m refuses both (m:7561-7564).

**NOTE-12 — Main moved during the review.**
- `1e79955` is LOCK-m-F3 v0.1, committed by another session. Its `LOCK-m-F3.md` differs from `a28bef6`'s scratch lock.
- The wiring's parsers read `1e79955`'s lock: 11 m files, one WEIGHTS line (`c000ac2c…`), and the proposal's and the
  manifest's sha256 named in full.
- The full self-test with the wired driver over `1e79955` passes 156/156 under the traps.
- The wiring commit belongs on `1e79955`. This review's base is the scratch `a28bef6`.

---

## 4. Fidelity to m's forms (new or changed lines)

| lines | change | m's form | ruling |
|---|---|---|---|
| :20-25 | module docstring: "the identity (refused on its own)" | — | accurate (r1 NOTE-9) |
| :72, :81, :92, :102, :215, :278, :328, :353, :436 | PIN headers "declared at LOCK-m-F3 v0.2; the time wiring" | m's time-path PINs are "declared at LOCK v0.2" (m:983-995) | m's precedent; NOTE-10 for the lock's F57 text |
| :101 | `\b` anchor | m tests lock lines as substrings | justified; NOTE-7 |
| :336-342 | running-file refusal | m derives DRIVER_REL from `__file__` (m:626) | equivalent protection, and stricter: a committed copy at another path is refused too |
| :467-472 | refs/main against the lock's revision | m's REVISION_STAGES refusal (m:1615), qual and campaign only | justified extension; NOTE-6 |
| :1275-1279 | help strings | m:7492-7503 | wording differs; NOTE-9 |
| :1287-1289 | top-level refusal | m:7562-7564 verbatim | faithful; the dispatch order is not m's (NOTE-1) |
| :580-1234 | self-test | m:4020-4600 | ported: modelscope any case (plus 'False' clear), hub resolution (plus a raising hub), production defaults, 30 of m's 31 refusal cases, multi (narrower), resume-open, order, post-load; not carried: MINOR-1's list |

Unchanged from round 1 and still faithful:
- `_load_qwen`, `redact_totals`, `_say` and `snapshot_line`;
- the post-load STOPs;
- the order: flags, out root, identity, then precheck + driver + snapshot refused once, then DRIVER, SNAPSHOT, load,
  re-read, MOVED and MODEL ID, the re-read line, the stage;
- the exit codes (2 before the load, 4 on any SystemExit, otherwise `EXIT_CODES`).

**Blinding.**
- The new refusal messages carry paths, revisions and flags: the running file's path, refs/main against the lock's
  revision.
- The self-test now scans stdout and stderr of every refusal case and of the stub run for roster words, in any letter
  case.

## Artifacts

All under `scratchpad/time/review2/`:
- `harness/`:
  - the runner and harness: `trapped_selftest2.py`, `run_lane.py`;
  - the mutant generators: `make_mutants_r2new.py`, `make_mutants_r2extra.py`, and round 1's `make_mutants.py` and
    `make_mutants2.py` (copied);
  - the probes and tooling: `state_probe2.py`, `probe_apply.py`, `table.py`;
- `mutants_r1/`, `mutants_new/`, `mutants_extra/`: the mutated drivers;
- `logs/`: the mutant logs (`mut_*.txt`), the baselines, `committed_full_off1.txt`, `committed_seam_through.txt`,
  `on_1e79955_full_off1.txt`, `selftest_from_copy_path.txt` and `mut_n23_offline_unset.txt`;
- `results_lane*.txt`, `results_extra*.txt`, `mutation_table.tsv`: the run results;
- `r1_to_r2.diff`: the delta since round 1;
- `orig_r2_mf3_sessions.py`: the revised driver (`64fc9ad1…`);
- `clone/`, `lane1`–`lane8`: copy-on-write copies, 467 MB logical. `lane5` and `lane6` carry scratch commits in their
  own `.git`; `lane8` is at `1e79955`. All can be deleted.

## Code's dispositions of round 2 (2026-11-07; each finding re-checked at source before it was applied)

- **MINOR-1, the residue of round 1's MINOR-3**, applied under mf3's names:
  - (a) an end-pending checkpoint, made by m's `cut_at_end` carried (the first checkpoint write carrying a `stage_end`
    dies), passes the precheck without `--resume` and reaches the loader trap;
  - (b) the local-path refusal's default working directory (m's `w_default`);
  - (c) weight names `..`, `''` and one with a backslash (m's `w_names`);
  - (d) a copy of the driver with its own name, running from elsewhere;
  - (e) m's multi arguments (licence, renders, preflight, driver, snapshot) refused in one line;
  - (f) a looping link as the lock; `exists` and `resume_open` plant the open checkpoint of a stub run interrupted
    in A3.
- **NOTE 1:** `time_q` traps `build_schedules` and `run_selftest`. The final check asserts that neither is reached.
- **NOTE 2:** the fake-cache section runs with `huggingface_hub.constants.HF_HUB_OFFLINE` patched true.
- **NOTE 3:**
  - the seam call is given a lock the identity would refuse, and the out root's refusal is asserted;
  - the planted-lock check proves the values come from the lock's text;
  - the constants label is reworded.
- **NOTE 4:** "driver (real check)" sets `__file__` to the canonical path, so it holds wherever the self-test runs.
- **NOTE 5:** the final driver check tests the blob before hashing it. A crash elsewhere still fails the battery,
  through `run_selftest`'s catch (declared).
- **NOTE 6:** the pre-load revision refusal is named in the entry and in the design raw. LOCK-m-F3 v0.2 records it.
- **NOTE 7:** the WEIGHTS pattern is `(?<![\w-])WEIGHTS`, with an `OLD-WEIGHTS` case.
- **NOTE 8:** the top-level refusal's exact line is pinned.
- **NOTE 9:** `TIME_FLAG_HELP` is keyed by flag.
- **NOTE 10:** the stale records are declared in the design raw (§7) and the entry.
- **NOTE 11:** the pre-existing drift is declared (design raw §7).
- **NOTE 12:** the wiring is rebased onto `1e79955`, where the self-test passed 159/159, then 160/160 after round 3.

---

# Round 3

**Blind review, round 3: the `time` wiring in `scripts/mf3_sessions.py` (G-TIME-F3). Verdict: 0 MAJOR, 1 MINOR, 12 NOTEs.**

*Saved by Code from the reviewer's final message: the reviewer's harness refused it a report file ("Subagents should return findings as text, not write report files"). The mutation table is the reviewer's own file, `review3/mutation_table.md`; its rows are summarized below as the message gave them.*

## Summary

**What was reviewed.** `site-wt/scripts/mf3_sessions.py`, detached at `1e79955`; sha256 `bf34c11b…`, 1,392 lines.
wire-wt holds the identical file. Since round 2 the file changed by a 335-line diff. Against HEAD the whole edit is
+1,179 / −27, in that one file.

**Read-only.** Main, site-wt and wire-wt were not changed. 114 trapped runs watched `data/mf3` in all four trees by
sha256 and mtime: none changed. `time` was never invoked outside the self-test's own traps. The harness traps fired
only in the three runs where a mutant planted the route on purpose: r3_e2 (write trap; the `os.mkdir` was refused),
r3_e3 (nested self-test trap) and r3_k1 (loader trap).

**Round 2's findings.** Round 2's MINOR (missing m self-test cases) is resolved, correctly, in parts (a)–(e). Mutants
n33, n34, n35, n03 and n38 are killed, and so are n36 and n37, which round 2 called equivalent. Part (f) is resolved
except one form (NOTE-4). Round 2's NOTEs 1, 2, 3, 4, 7, 8 and 12 are resolved. NOTEs 5 and 9 are resolved with a
residue. NOTEs 6, 10 and 11 stay open as documentation or pre-existing behaviour.

**Mutation: 99 runs, 83 killed, 16 survived.** Round 2's 16 survivors, re-run: 10 are now killed; the 6 that survive
are all equivalent. The other 58 mutants from rounds 1 and 2 are all still killed. 24 new mutants: 14 killed and 10
survive. Of the 10, 6 are gaps against m (MINOR-1), 1 is a label over-claim (NOTE-1), 2 are unpinned and cosmetic,
and 1 is equivalent. n23 re-run with `HF_HUB_OFFLINE` unset is killed and made 0 network connects (round 2: 88).

**Safety.** As written, no self-test case can load the model or write `data/mf3`: with the driver uncommitted and
committed; with `HF_HUB_OFFLINE` set and unset; with the hub cache and without it; when the self-test runs from a
copy path. One case is a single regression away from a real load (NOTE-2, carried from m).

**Scope.** The edit touches nothing under `valence_core/`. `id`, `qual` and `campaign` still exit 2, each named.

## MINOR-1 — m's self-test checks six more time-path behaviours that mf3's does not (six surviving mutants)

**Where.** Production: `run_time`, :478-498, and `time_precheck`, :307-317. The self-test: the refused-case battery
(:1197-1201), the multi case (:1217-1226) and the post-load cases (:1286-1297). m's assertions: m:4495, m:4509,
m:4517-4518 and m:4571-4577.

- **(a) A refused run prints no DRIVER or SNAPSHOT line.** m asserts `"DRIVER " not in stdout and "SNAPSHOT " not in
  stdout` on every refused case (m:4495), at its other stages too (m:4810, m:5076, m:5199, m:5806), and in its multi
  case (m:4517). mf3's battery only asserts that "refused" is absent from stdout. Mutant r3_g1 moves the DRIVER print
  above the combined refusal (:479-483) and passes 35/35; under it the "driver (real check)" case prints on stdout
  `DRIVER scripts/mf3_sessions.py None: committed at HEAD 1e7995560f4e…, working tree identical`, then on stderr
  `REFUSED: G-TIME-F3: ['driver: selftest: driver uncommitted']; nothing loaded` (`probe_g1.txt`).
- **(b) An ENDED checkpoint gets no CHECKPOINT EXISTS advice.** m asserts the advice is absent in both ENDED cases
  (m:4509). Mutant r3_p2 moves `rs.refuse_ended(cpath)` (:309) after the exists test (:313) and passes; under it the
  "ended" refusal reads `['checkpoint: CHECKPOINT EXISTS at …; pass --resume to continue it or move it aside (never
  overwritten)', "checkpoint: STAGE ENDED at … (PASS): a finished gate stage is never resumed, …"]` (`probe_p2.txt`).
- **(c) The post-load STOP messages keep their evidence.** m asserts both revisions in order (m:4571), the re-read's
  problems (m:4574) and both model ids (m:4576-4577). mf3's `bad_post` (:1295-1297) asserts only each STOP's prefix.
  r3_g2 (revisions swapped, :494-495), r3_g3 (problems dropped, :491-492) and r3_g4 (ids dropped, :497-498) pass.
- **(d) The combined refusal names the stage.** m asserts `err.count("REFUSED: G-TIME-F0:") == 1` (m:4518). mf3's
  multi case only counts lines starting with "REFUSED" (:1219). r3_g5 drops the name at :480 and passes.

**Failure scenario.** (a): a refactor that prints the DRIVER line before the refusal passes 159/159; launched with the
driver uncommitted, such a run writes to its raw a DRIVER line saying "committed at HEAD …, working tree identical"
over the sha `None` — the line the PIN at :333-340 makes the record of the driver's blob — then the REFUSED line on
stderr, and nothing loads. (b): the refusal advises `--resume`, which is then refused with STAGE ENDED. (c), (d): a
STOP or a refusal loses the evidence the seat adjudicates from. None of these can load the model or write
`data/mf3`; the same class round 2 graded MINOR.

**Fix.** Port m's assertions under mf3's names: `"DRIVER " not in out and "SNAPSHOT " not in out` in every refused
case and in multi; `"CHECKPOINT EXISTS" not in err` in both ENDED cases; in the post-load cases both revisions in
order, the re-read's problems, both ids, and no re-read line; `err.count("REFUSED: G-TIME-F3:") == 1` in multi.

**Confirmed by running.** r3_g1, r3_p2, r3_g2, r3_g3, r3_g4 and r3_g5 each pass 35/35 under the trapped harness; (a)
and (b) also with instrumented copies of the self-test inside its own traps.

## NOTEs

- **NOTE-1.** Two labels claim more than they assert. The planted-lock check (:681-685) claims "and the weights", but
  only corr.py is planted: r3_pl1 (weights from the hub's binding) passes. Its "(e')" claim is also satisfied by (f),
  because the licence call at :685 runs against the real committed lock, outside the patch. The final check's "only
  by the four cases" (:1315) asserts only the total: r3_p1 shifts one reach from "pending" to "exists" and the final
  check passes.
- **NOTE-2.** The constants check (:751-752) calls the real `_load_qwen()` with only `qwen_or_explain` patched, while
  `get_adapter` and `QwenMLXAdapter` are left open. `QwenMLXAdapter` loads the model in its constructor
  (qwen_mlx.py:91). r3_k1 (routing through `get_adapter`) reached the harness's loader trap there; in a real
  `--selftest` that would be a 27B load. This is m's form (m:4154-4157), and the docstring at :589 holds only for the
  code as written. Fix: trap `get_adapter` and `QwenMLXAdapter` as well around the call, or block the `mlx` and
  `jlens_qwen` imports there.
- **NOTE-3.** The WEIGHTS anchor `(?<![\w-])` (:106) is checked for letters and hyphens only. Digits and underscore are
  unpinned (r3_w3 survives), though the label is accurate. `.WEIGHTS`, `/WEIGHTS` and `` `WEIGHTS `` still parse as
  WEIGHTS lines; that is fail-safe. n13 is equivalent.
- **NOTE-4.** The checkpoint-loop case (:1160-1162) accepts either message on any Python, where m names the running
  version's (m:4483-4484). The residue of round 2's MINOR-1 (f).
- **NOTE-5.** `TIME_FLAG_HELP` (:91-95, :1361-1362) removes the zip hazard: r3_h2 and r3_h3 are killed. The help text
  itself is unpinned (r3_h1 survives), its wording differs from m's (m:7492-7503), and m checks its top-level `--help`
  (m:3966-3978) where mf3 does not.
- **NOTE-6.** The escape traps (:608-614, :1084-1085) patch the two functions, not the schedules directory. The dispatch
  order (:1370-1376) is still not m's (m:7561-7583). Safe as written: n16, n17 and main_top_flags now stop at the
  escape trap with no harness trap.
- **NOTE-7.** `contextlib.chdir` (:934) needs Python 3.11 or later; m uses `os.chdir` with `finally` (m:4218-4222). The
  venv runs 3.12.9.
- **NOTE-8.** Round 2's NOTE-5 is partly resolved: n28 no longer raises. n09, n25, n27, r3_g6 and stub_default_root still
  kill by raising. The Qwen block now reads three stub-block products: `ended_ckpt`, `open_ckpt` and `pending_ckpt`
  (:1012, :1032, :1048).
- **NOTE-9.** Round 2's NOTE-6 and NOTE-10 stay open for the entry and v0.2: the revision refusal (:472-477) is unnamed
  in both docstrings; LOCK-m-F3's F57 row (:502) is unchanged; lock lines :432-433 still say F57's site "carries no
  PIN line", but the driver now has 9; stages.py:12 still says none is wired; G-SHAPE-F3.json records the pre-edit
  driver, `fad31c20…`.
- **NOTE-10.** Round 2's NOTE-11 is unchanged and pre-existing: the refusals at :1384-1388 print to stdout, and
  `--selftest id` and `--build-schedules qual` still run.
- **NOTE-11.** With no hub cache (`HF_HUB_CACHE` set to an empty directory), nothing round 3 added fails. The full
  self-test passes 150/154 and the driver checks 32/35, with no network attempt; the failures are gshape's
  self-test, `gshape --out`, "hashes" (WEIGHTS unreadable, exit 4) and "that identity is licensed now" — the time
  wiring's only hub-dependent check (since round 1), failing exactly as "hashes" does.
- **NOTE-12.** The concurrent site check finished 9/10: closure_verify3 fails 22/24 because its R13 checks read
  `HANDOFF-2026-09-04-design.md`, untracked in main and so absent from the worktree. Nothing in that failure involves
  the driver; mf3_sessions passed 159/159 there and m_sessions 846/846.

## Mutation table (99 runs; driver checks under the trapped harness, `HF_HUB_OFFLINE=1` unless noted)

- **Round 2's 16 survivors:** killed — n03, n18, n32, n33, n34, n35, n36, n37, n38, n39; survived, equivalent — n02
  (resolving the running file's own path cannot raise), n08 (gshape's constant is the lock's revision in this tree),
  n13 (equivalent on every text parsed), say_no_redact and precheck_no_redact (totals sealed at source),
  driver_none_branch (`stages.committed` never returns `([], None)`).
- **Round 3's new mutants (24):** killed — r3_c1, r3_e1, r3_e2, r3_e3, r3_e4, r3_g6 (raised), r3_h2 (raised), r3_h3,
  r3_k1 (raised, after the harness loader trap fired in the constants check: NOTE-2), r3_p1, r3_w1, r3_w2, r3_x1,
  r3_x3, and n23 re-run with `HF_HUB_OFFLINE` unset (0 connects); survived — r3_g1, r3_g2, r3_g3, r3_g4, r3_g5, r3_p2
  (gaps: MINOR-1), r3_pl1 (label over-claim: NOTE-1), r3_h1 (help unpinned, cosmetic: NOTE-5), r3_w3 (digits and
  underscore unpinned: NOTE-3), r3_x2 (equivalent: identical bytes).
- **Rounds 1 and 2, killed in round 2:** all 58 still killed (accept_other_lock through weights_any_model; the full
  per-mutant rows, with the failing checks, are in `review3/mutation_table.md`).

## Method (the reviewer's)

Copies: `review3/clone` is an APFS copy of round 2's lane8, a `--shared` clone at `1e79955` with the r3 driver copied
in; `lane1`–`lane8` and `probe` are copies of it; `lane5` has the driver committed (scratch commit `a5f679e`, never
pushed). Harness `trapped_selftest3.py`: round 2's, with site-wt added to the write trap and the watch, every earlier
trap kept — `qwen_or_explain`, `get_adapter` and `QwenMLXAdapter` replaced by a loader trap; importing `mlx`,
`mlx_lm` or `jlens_qwen` blocked; writes under the four trees' `data/` trapped; network connects trapped; a nested
`run_selftest` trapped. Baselines: 35/35 driver checks and 159/159 full self-test, uncommitted and committed, with
`HF_HUB_OFFLINE` set and unset, and from a copy path; 150/154 and 32/35 with an empty hub cache.

## Code's dispositions of round 3 (2026-11-07; each finding re-checked at source before it was applied)

- **MINOR-1**, m's assertions ported:
  - (a) no DRIVER or SNAPSHOT line on stdout in any refused case or in multi;
  - (b) no CHECKPOINT EXISTS advice in either ENDED case;
  - (c) the post-load STOPs carry their evidence: the re-read's problems, both revisions in order, and both model ids;
  - (d) the multi line names the stage (`REFUSED: G-TIME-F3:` once).
- **NOTE-1:** the planted lock plants the corr.py line's sha256 and the WEIGHTS sha256, and the licence runs inside
  the patch. It refuses (e′) and (g), and nothing for (f). The final check's label now says what it asserts: 4
  reaches in all, each of the four cases asserting its own.
- **NOTE-2:** the constants check's real `_load_qwen()` runs with `qwen_or_explain` answering, `get_adapter`
  refusing, and the `mlx`, `mlx.core`, `mlx_lm`, `jlens_qwen` and `jlens_qwen.model` imports failing (`sys.modules`
  entries None). A routing of `_load_qwen` through `get_adapter` fails the check instead of loading.
- **NOTE-3:** cases for a digit and an underscore glued to WEIGHTS. A non-word character before it (`.`, `/`, `` ` ``)
  still parses, which is fail-safe (declared).
- **NOTE-4:** the checkpoint-loop case names the running Python's message (3.12: "does not resolve"; 3.13+:
  "CHECKPOINT EXISTS").
- **NOTE-5:** `time --help` is checked to list each flag with its help text. The wording is Code's (declared).
- **NOTE-6:** no change. Time's refusal precedes the top-level dispatch, and the escape traps cover a regression.
  The order differs from m's (declared).
- **NOTE-7:** `os.chdir` with `finally`, m's form.
- **NOTE-8:** no change. A raise fails the battery.
- **NOTE-9:** named in the entry and in the design raw (§2, §7). LOCK-m-F3 v0.2 records them.
- **NOTE-10:** pre-existing, declared.
- **NOTE-11:** no change. The one hub-dependent time check fails on a machine without the hub cache, as the
  pre-existing "hashes" check does. The suite is the laptop's.
- **NOTE-12:**
  - The ten-suite site check is re-run with the untracked `HANDOFF-2026-09-04-design.md` copied in, as the earlier
    site checks had it. That run used the bytes before the help-pairing pin.
  - The driver's suite, the only one that reads the driver, is re-run on the final bytes.
- **Verification by mutation.**
  - Code built the nine non-equivalent round-3 survivors and ran them under the driver checks, in worktrees at
    `1e79955` with the `mlx` and `jlens_qwen` imports blocked. The nine:
    - the six gaps, r3_g1 to r3_g5 and r3_p2;
    - the label over-claim, r3_pl1;
    - the two unpinned forms, r3_w3 and r3_h1.
  - Code also ran the load route r3_k1, which round 3 had killed, as a check of NOTE-2's fix. r3_x2, equivalent, was
    not re-run.
  - **The runs, by bytes:**
    - on the bytes before the help-pairing pin, every mutant but r3_h1 was killed. r3_h1 survived the presence-only
      form of the help check;
    - the pin was added, giving `1773ae7f…9a56`, and on those bytes all ten of Code's builds were killed;
    - the values-check's comment and docstring fixes then gave the final bytes, `890084e6…90af`. Their code's syntax
      tree is identical to `1773ae7f…`'s; the site-check raw's last section and the values-check raw record that.
  - **Five of Code's builds differ from the reviewer's generators.** The wiring values-check, passes 1 and 2, found
    them:
    - two in kind. Code's r3_p2 deleted `rs.refuse_ended(cpath)`, which is round 1's drop_refuse_ended; the
      reviewer's moves it after the CHECKPOINT EXISTS test. Code's r3_g1 added a second DRIVER print; the
      reviewer's moves the print above the refusal;
    - three as variants of the same move. In r3_g4 the ids are dropped in other words. In r3_h1, Code swapped the
      package's and the renders' help where the reviewer swapped the analyzer's and the package's. In r3_pl1, Code
      took only `weights_sha256` from the hub binding where the reviewer took both values from it.
  - **r3_p2 and r3_g1, rebuilt as the reviewer's moves and run on the final bytes:**
    - r3_p2 is killed 35/36 by the refused battery alone (CHECKPOINT EXISTS beside STAGE ENDED);
    - r3_g1 is killed 34/36 by the refused battery and multi (a DRIVER line on stdout).
  - **The other eight**, killed on `1773ae7f…`:
    - r3_g2, r3_g3 and r3_g4: the post-load check's evidence;
    - r3_g5: multi's stage name;
    - r3_pl1: the planted-lock check;
    - r3_w3: the parsers' digit and underscore cases;
    - r3_h1: the help-pairing pin;
    - r3_k1: the constants check, which refused the get_adapter route (SystemExit; no model import possible).
  - The values-check ran the reviewer's own ten mutants, built from the reviewer's generators, in memory: on
    `1773ae7f…` (pass 1) and on `890084e6…` (pass 2). All ten were killed both times.
  - Each lane's driver was restored, and compared with the bytes under test, after its run.
