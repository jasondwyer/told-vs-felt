# PROPOSAL-p -- the qual wiring's BUILD: blind reviews (Code's reviewers, rounds 1-2)

*Code's raw, PI date 2026-11-10. 2 blind review(s) of the uncommitted qual wiring (`valence_core/p/stage.py`, `scripts/p_sessions.py`; the seat's answers of 2026-11-10, `42c5a92`, §1-§3), each run in a detached scratch worktree at `42c5a92`, editing no repository file. Each brief quoted the list of record v2's items 1-5 verbatim. Each report is verbatim, with local paths scrubbed (`<repo>`, `<tmp>`) and its headings set two levels down under its round's heading; Code's dispositions follow each round. Code applied or answered every finding before the next round, and the last round's before the commit.*

## Round 1

### Blind review r1: the `qual` wiring (G-F0m-OLMo (p)), with (h) and (j)

#### Pin

- `git -C WT rev-parse HEAD`: `42c5a92abcf90c330297437460177492d93b5b51` (a detached worktree; the two files below carry uncommitted edits, and `git status --porcelain` shows only those two).
- `valence_core/p/stage.py` sha256: `e165391be047098b4e7e9f596587b2180d3c53af3b60e3045e6d26fc7e9213fc`
- `scripts/p_sessions.py` sha256: `942236adccf6d2233ce87efb2faf9ad4d57f9af3217a8c2f3d0971fa57e170df`
- I re-hashed both files at the end of the review. Neither had changed.

**Counts: MAJOR 0, MINOR 0, NOTE 7.**

#### What I ran

All commands were model-free, run under `nice -n 19` with the jlens venv's python and `-B`.

- **p's self-test in WT.** 178 of 178 checks pass (about 38 s). Afterwards the WT held no new file: `git status --porcelain` showed the two edits only, and a pruned `find` found no `__pycache__` and no `.pyc`.
- **The (j) closure.** In one process I imported p's driver by path and computed four closures:
  - `stage.fresh_import_closure()`;
  - `gshape.import_closure(committed=True)`, right after the import;
  - the same, again after `gshape.inputs_of_record(canonical=False)`;
  - the committed `data/p/gates/G-SHAPE-p.json`'s `provenance.import_closure`.

  All four are the same 14 files, with the same committed-blob sha256s. `stage.gshape_drift_problems` on the committed artifact reports only the two uncommitted sources-map files, which is expected in WT.
- **The precheck at both gates.** I ran `stage.precheck("OLMo-sft", stub=False, gate=...)` at `time` and at `qual`, with `RUNPOD_POD_ID` unset. They give 10 and 11 problems. The only problem at `qual` that `time` lacks is the v0.2 line on the committed v0.1 lock; the POD ID ABSENT line also differs, by the stage name only. Neither reports import-closure drift.
- **Time's report strings.** I parsed HEAD's `build_report` strings from `git show HEAD:valence_core/p/stage.py` with `ast`. HEAD's `form`, `rule` and `contrast` are byte-identical to `REPORT_TEXT["time"]`.
- **Git rules for the qual outputs** (names only, via `git check-ignore` and `git check-attr diff`):
  - m's and p's qual outputs under `data/p` are admitted;
  - every `ckpt/` file is `-diff`;
  - the `.lock` files and the `.reserve-1` names are ignored.

**Departures, disclosed:**

1. I first wrote the self-test's stdout to `<tmp>/scratchpad/qualbuild/review_selftest_r1.txt`. I read its tail and deleted it. The brief allows this review file only.
2. One malformed command piped HEAD's `stage.py` into `python -`. It stopped at the file's first relative import, after stdlib imports only. Nothing was written, and nothing beyond those imports ran.

Nothing under `data/*/ckpt` or `data/*/reports` was read, listed or sized. I read no file in `scratchpad/qualbuild/` except the brief.

#### Findings

##### N-1 NOTE: `valence_core/p/stage.py:28-29` (the docstring's THE QUALIFICATION)

- **What is wrong.** The docstring says "p requires it whole, N-4's form". But N-4's form (`lock_names`, `:415-418`) accepts a value as a whole line *or* between backticks. `qual_lock_problems` (`:437-443`) accepts a whole line only. The code follows the seat's §3 ("carries the whole line"), so the defect is in the wording, not in the check.
- **Failure scenario.** A v0.2 drafter reads "N-4's form". In item 1's sentence they write `` `G-TIME-OLMo-sft port acceptance recorded` ``, the backtick form the generator uses for every other value. G-F0m-OLMo (p)'s precheck then refuses with exit 2, before the load. The cost is one lock re-commit. No run happens on wrong inputs.
- **Fix.** Write "as a whole line (N-4's whole-line form only; a value between backticks does not satisfy it)".

##### N-2 NOTE: `valence_core/p/stage.py:988-990`

- **What is wrong.** The backend STOP's message still carries the clause the move replaced: "(m:302; a superseding BACKEND entry is the seat's to route)". The PIN at `:54-59` now has §2 item 6's "a differing identifier STOPs and the seat rules". The two do not contradict each other, but they no longer match.
- **Failure scenario.** On a box whose identifier is not `641ee466f4553b6a`, the STOP line printed into the raw names the old route. The STOP and the seat's ruling are unchanged.
- **Fix.** Word the message to item 6, for example `... is not the lock's ... (m:302; a differing identifier STOPs and the seat rules) -- nothing generated`. Otherwise, name the kept wording in the BUILD entry.

##### N-3 NOTE: `valence_core/p/stage.py:296-300` (`fresh_import_closure`)

- **What is wrong.** The child interpreter runs with no `timeout`, and an `OSError` from `subprocess.run` is not caught.
- **Failure scenario.**
  - The spawn itself fails. Examples: `sys.executable` is gone after a venv rebuild under a live shell, or fork returns EAGAIN. The `OSError` escapes `lock_required` and `precheck`. The driver catches only `SystemExit`, so the run ends in a traceback with exit 1, at both gates and in the lock generator. The declared exit-2 refusal naming the problem never appears.
  - A child that blocks while importing (for example, on the network volume) hangs the precheck with no bound.

  In both cases nothing is loaded and nothing is recorded, so the effect is fail-closed. Only the declared refusal form is lost.
- **Fix.** Add a `timeout=` of a few minutes. Catch `(OSError, subprocess.TimeoutExpired)` and return a named problem, as the non-zero-exit branch already does.

##### N-4 NOTE: `valence_core/p/stage.py:137` (also `:20-22`, `:429-434`)

- **What is wrong.** The counts (8 + 16) are code constants. Their equality with the committed gate files' `n` is asserted in two places only:
  - the self-test (`:1700-1721`);
  - at run time, m's `run_gate_stage` (`valence_core/m/stages.py:1480-1482`), which runs after the load. It raises a `ValueError`, not a `SystemExit`, so p records an interruption rather than a STOP, and the driver exits 1 on the traceback.

  The docstring's "its counts m's from the committed gate files" also reads as though the counts were read from the files.
- **Failure scenario.** This is unreachable in the reviewed state: the lock names every schedule file's sha256, and the self-test asserts 8 + 16 for every unit. It becomes reachable if a later `COUNTS` edit, or a schedule rebuild with other `n` re-pinned in a lock, ships without the self-test. G-F0m-OLMo (p) would then load the model, write its run line, and fail inside m's stage.
- **Fix.** In `precheck`, compare `templates_counts(unit, gate)` with the `n` of `data/p/schedules/{unit}_{gate}_{t}.json` and refuse before the load. Reword the docstring to "m:302's counts, asserted equal to the committed gate files' n".

##### N-5 NOTE: `valence_core/p/stage.py:948-957`

- **What is wrong.** The pre-load prior check is m's `prior_gate` alone. Its proposal clause compares the prior's `identity.proposal_sha256` with m's pin, and every p record carries that pin (F-p8). So the check cannot tell a G-TIME (p) checkpoint from:
  - an m-run G-TIME-OLMo-{ckpt} checkpoint;
  - a G-TIME run under another PROPOSAL-p.

  p's own identity fields (`proposal` "PROPOSAL-p" and `proposal_p_sha256`, in `identity.P_FIELDS`) are never checked.
- **Failure scenario.** m's own G-TIME-OLMo-sft checkpoint, or one from a superseded p proposal, sits at `data/p/ckpt/OLMo-sft_time.json`. G-F0m-OLMo (p) is then licensed on a prior that never ran through p's register. The reach is small: `data/p` is p's root and m's non-stub out-root guard refuses it, so only a file placed by hand gets there.
- **Fix.** Before the load, also require the prior identity's `proposal` and `proposal_p_sha256` to equal those in `identity.run_values()`. The stage's own code may read the checkpoint. Alternatively, record the gap as accepted.

##### N-6 NOTE: `scripts/p_sessions.py:376-381` (the checks at `:388-400`)

- **What is wrong.** In the `time`/`qual` refusal case, only POD ID ABSENT keeps `stage.run_gate` off `data/p`:
  - `stage.DEFAULT_OUT_P` is not pointed at the scratch root there, although the report case does this at `:462`;
  - the OLMo adapter module is not a stand-in in that block. The loader is trapped, so a load itself cannot happen.
- **Failure scenario.** The code is safe as written: with `RUNPOD_POD_ID` removed, the precheck always refuses. The risk is a later precheck change that drops or defers the pod-id problem, run on the box at a commit whose lock and artifacts are current. The self-test's `qual` case would then reach `run_gate` on `data/p`. It would reserve the marker and write a run line into the real call log before the trapped loader raises, leaving an interruption recorded in a stage's record.
- **Fix.** Patch `stage.DEFAULT_OUT_P` to `Path(td) / "p"` in that block too. That restores the "scratch roots" layer the gcal cases have.

##### N-7 NOTE: the self-tests (`valence_core/p/stage.py:1696-1866`; `scripts/p_sessions.py:376-480`)

**What is wrong.** No test pins the wiring that keeps qual's refusals before the load. Six gaps:

- **(a) The prior's non-stub arguments.** Every stage run in the self-test is a stub run. So p's pre-load arguments to `prior_gate` (`require_real=not stub`, `proposal_sha256=` m's pin, no adjudication) are never exercised with their non-stub values. A regression to `require_real=False` would pass the self-test. On the box, a stub-written or foreign prior would then be refused only by m's own call after the load, which is a STOP.
- **(b) A prior that ended STOP.** A G-TIME (p) prior that ended STOP, or PAUSE without an adjudication, is never exercised. The absent and not-ended cases are tested (`:1784-1798`).
- **(c) The lock-line wiring.** `precheck`'s use of `qual_lock_problems` (at qual only, non-stub only) is not asserted. The function itself is tested (`:1706-1709`), and the driver's qual refusal checks only POD ID ABSENT and the stage name. I confirmed by hand that the WT's precheck at qual adds exactly the v0.2-line problem to time's list.
- **(d) The (j) fix.**
  - `fresh_import_closure`'s fail-closed branches are untested: a child exit other than 0, output that is not JSON, a file outside the repo.
  - `gshape_drift_problems`' use of `fresh_import_closure` is untested. The (j) check calls `fresh_import_closure` and `_drift` directly, so reverting `gshape_drift_problems` to the in-process closure would still pass.
  - Nothing compares the fresh closure with what G-SHAPE-p actually records (gshape's in-process closure after `inputs_of_record`). The two are equal today (14 files). If they ever diverged, every gate stage would refuse, and re-running G-SHAPE-p would not cure it.
- **(e) The gate mismatch.** `run_gate`'s new refusal of a precheck taken at another gate (`:884-887`) is untested.
- **(f) Qual-only paths.** The following are tested at `time` only, or not at all:
  - a qual stage that ends STOP on a bar (p's report status STOP, exit 4);
  - an interruption followed by `--resume` over the 24 sessions;
  - the driver's `qual --resume`;
  - the qual run's arm keys (`p-olmo-qual|`), which time asserts as `p-olmo-time|` at `:1258`.

**Failure scenario.** Each gap lets a regression that turns a pre-load refusal into a post-load STOP pass the battery.

**Fix.**

- Put a recorder in place of `m_stages.prior_gate` on a non-stub call, or factor the prior check into a helper and test it with stub False.
- Add a case with a G-TIME prior that ended STOP.
- Assert that the qual precheck refuses a v0.1 lock text naming the line, and that time's precheck does not.
- Add a failing-child case (`sys.executable` patched to a binary that exits 1), and assert that `gshape_drift_problems` calls `fresh_import_closure`.
- Assert key-set equality between `fresh_import_closure()` and `gshape.import_closure` after `inputs_of_record`.
- Add a qual resume case.

#### Answers

##### Q1. Does the change implement §2 of the 2026-11-10 answers item by item?

Yes. Every item of §2, and §1's two deferred fixes, is implemented.

| §2 item | Where it is implemented |
|---|---|
| The gate is a parameter of p's stage (`time` \| `qual`) | `stage.py:133` (`GATES`); `label` `:194-201`; `precheck(..., gate=)` `:458-466`; `out_paths(..., gate=)` `:552-562`; `run_gate` `:878-897` (`run_time` kept at `:900-902`); `p_sessions.py:111` (`GATE_CMDS`) |
| m's counts from the committed gate files (8 + 16) | `stage.py:137` (`COUNTS`) and `:429-434`, passed at `:991`. Equality with the files' `n` is checked by the self-test (`:1700-1721`) and, after the load, by m (`m/stages.py:1480-1482`). See N-4. |
| G-TIME (p)'s checkpoint passed to m's stage as the prior | `stage.py:948-950` and `:991-993` (`prior_ckpt=`) |
| m's `prior_gate`: ended PASS, this unit's, m's pin (F-p8), not the stub's | `stage.py:951-957` before the load (`require_real=not stub`, the pin from `identity_extra`), and again inside m's stage (`m/stages.py:1472` → `:1134-1142`) |
| The lock's v0.2 line checked before the load (§3) | `stage.py:140` (`QUAL_LOCK_LINE`), `:437-443`, `:504-505` |
| Call log, marker, lock file and p's report under `_qual_` names | `stage.py:558-561`; the reservation by the marker's name, `:649-651` |
| p's report over the 24 sessions, on the read domain | `stage.py:796-868`, with `REPORT_TEXT["qual"]` (`:178-183`) and `CONTRAST_WITHHELD_QUAL` (`:167-169`) |
| The driver's `qual` and `qual-report`, as `time` and `time-report` | `p_sessions.py:241-301`, `:555-561`, `:578-581` |
| `time`'s behaviour unchanged | Defaults are `gate="time"`, and `REPORT_TEXT["time"]` is byte-identical to HEAD (checked). See Q2. |
| `campaign` still refused | `p_sessions.py:113-121`, `:562-563`, `:582-584`; `precheck` also refuses any non-gate (`stage.py:462-464`) |
| No `prior_adjudication` input | `stage.py:952` passes `None`, and `:991-993` does not pass one; the driver has no option for it |
| A fired G-F0m-OLMo bar is a STOP under m's rule | m's OLMo qual bar is binomial with a STOP (`m/bars.py:618-619`), read by m's `_gate_end`. Nothing in p alters this. |
| §1: (h)'s PIN wording | `stage.py:54-59` (see Q6) |
| §1: (j)'s fix | `stage.py:274-347` (see Q6) |

Nothing is missing. The only nuance is the second row: the counts are constants, not read from the files (N-4).

##### Q2. Is gate `time`'s behaviour unchanged?

Yes, apart from (j), which §1 intends.

**Outputs and names.** These are unchanged: `label(unit)` is still `G-TIME-OLMo-{ckpt} (p)`, and `out_paths(unit, root)` still gives the `_time_` names (checked by the self-test at `:1724-1729` and by me). m's paths are unchanged.

**Report form.** Byte-identical: `form`, `rule` and `contrast` equal HEAD's strings, checked by parsing HEAD with `ast`.

**Refusals.**

- Every message `time` prints is unchanged: the driver's DRIVER/WEIGHTS/REFUSED lines, `time-report`'s refusals, and the "re-derive ... with the driver's time-report" texts.
- One message changed wording only: the refusal of a mismatched precheck (`:884-887`) now names the gate as well as the stub flag.
- The precheck's returned dict renamed a key: the gate line is now `gate_line`, and `gate` now holds the gate. This is internal; nothing outside `stage.py` reads either key (searched).
- The driver's no-action message now lists the new commands.

**The one behavioural change.** `gshape_drift_problems` now takes the import closure from a fresh `python -I -B` interpreter, at both gates. `time`'s precheck therefore depends on a child interpreter starting (see Q6 and N-3). This removes the false drift FLAG (j) described, and on the recorded artifact it gives the same 14 files.

##### Q3. At `qual`, can a problem be discovered only after the model load?

No new one. Every prior case and the lock refuse before the load, with nothing recorded and nothing loaded. The only thing left on disk is the gitignored flock file.

**The prior** runs through m's `prior_gate` at `stage.py:951-957`, before the reservation, the run line and the factory. Its cases:

- **Absent.** Refused with PRIOR STAGE ABSENT (tested).
- **Not ended.** Refused with PRIOR STAGE NOT ENDED (tested).
- **Not PASS.** A STOP, or a PAUSE without an adjudication, is refused with "PRIOR STAGE STOP" or "PRIOR STAGE PAUSE" (untested, N-7 (b)).
- **Written on the stub.** On the box `require_real` is True, so this is refused with PRIOR STAGE ON THE STUB (untested, N-7 (a)).
- **Another proposal.** A prior under another m proposal is refused with PRIOR STAGE UNDER ANOTHER PROPOSAL. A prior run under another p proposal, or by m itself, is not detected, because both carry m's pin under F-p8 (N-5).
- **Wrong unit or stage at that path.** Refused with PRIOR STAGE MISMATCH.

I checked that the pre-load call is the same as m's call inside the stage: same path, same pin, an empty re-adoption list on both sides, no adjudication, and `require_real` equal on the box. I also checked that m's checkpoint reader (`_check_state`) reads no substituted global, so calling it outside the substitutions gives the same answer.

**The lock.** The v0.2 line and every `lock_required` value are checked in `precheck`, before the weights check and before the DRIVER line. They are checked on the committed blob whose sha256 enters `identity_extra`.

**What can still surface after the load:**

- **m's duplicate checks.** m's own licence and `prior_gate` re-read the same lock and checkpoint. They fire only if those files change between the precheck and the load. No p writer can change them then: G-TIME has ended and has its own flock, and its report command never writes the checkpoint.
- **The backend identifier.** This check needs the adapter's provenance, so it is post-load by construction, exactly as at time. Per the seat's (h), it is a STOP.
- **A counts mismatch.** Unreachable (N-4).
- **The resume-only identity and licence comparisons**, as at time.

**p's own G-TIME STOP record is not consulted.** That record is the marker, or a log line carrying the stop mark. It could only coexist with m's PASS if m swallowed a `ProxyStop`. No production path in m catches `SystemExit`; m's handlers that do are all inside its self-tests.

##### Q4. Is the LOCK-p v0.2 line check right, on time, and strict enough?

**Right line.** Yes. `QUAL_LOCK_LINE` is formatted with `gcal.unit_ckpt(unit)` (sft, dpo or instruct). It is the text of m's `OLMO_QUAL_LOCK_LINE` at `scripts/m_sessions.py:680`, which the self-test reads as text and compares. That matches §3: m's string, kept because p's records keep m's unit strings.

**Right time.** Yes. It is checked in `precheck` (`:504-505`):
- before the load, the weights check, and the DRIVER/WEIGHTS lines;
- only at `qual`, and only on a non-stub run;
- on the lock's committed bytes (`_committed`: at HEAD, working tree identical). These are the same bytes whose sha256 enters `identity_extra`, and which m's licence re-reads after the load.

`time` does not require the line. I confirmed this by hand: the WT's qual precheck adds exactly this one problem to time's list, because the committed lock is v0.1.

**Strict enough.** Yes.
- It must be a whole line after stripping, case-exact, for the unit's own checkpoint. That is strictly stronger than m's substring test (`scripts/m_sessions.py:933`).
- A line from another checkpoint, a prefixed sentence, and the v0.1 header are all refused (self-test).
- It does not check that the line sits in item 1 or under a v0.2 header. It does not need to: the rest of the precheck requires the moved package, the driver, and the re-run G-SHAPE-p and G-ANL-p hashes, which no v0.1 text can name. The committed v0.1 locks do not contain the line.

The docstring's "N-4's form" overstates what is accepted (N-1).

##### Q5. Can p's outputs carry contrast-session information beyond the read domain?

I found no leak.

**p's report and closing lines.** They carry the following:

- **Sham sessions.** Their counters, keyed by round, and the proxy attribution: rounds, attributed, cuts, cut keys and unattributed keys.
- **Contrast forced rounds.** Their control-character texts by key, and the number of forced rounds (F-p13 (a); the seat's (a) and (b)).
- **The hair trigger.** Its count over every round, which is zero by construction.
- **Outputs.** Paths and sha256s.
- **Runs.** Number, resume flag, outcome, exception type and stop flag.
- **Other.** Term (d)'s states and the register entries.

They carry no proxy count over a contrast session, no `n_generate` or `n_cuts` total (both stay in the withheld end line), and nothing per contrast free round. Seed attribution draws on 31-bit per-session seeds, so a contrast round cannot plausibly collide with a sham round's seed and so alter the sham attribution.

The qual blinding test plants a contrast free-round exclusion in session 3 at free round 0, at free round 1, or nowhere. The free rounds generated differ (6, 1, 2), while p's report and closing lines are identical up to the outputs' sha256s.

**The call log's run line.** It holds the schema, run number, resume flag, stage, unit, register entries, the p package and PROPOSAL-p sha256s, and the names of stale reservations. There is no session data.

**The STOP marker.** It holds the stage, unit, run number and the STOP's message, which is either m's own blinded words or p's ProxyStop message with no text and no call index. It sits under `ckpt/`, which is `-diff` and withheld.

**Stdout.** p adds only the GATE, P-STALE, P-STOP and P-REPORT lines. Two things on stdout come from m, as before this change:
- m's own session lines print a contrast session's exclusion by phase (m:318);
- a STOP's message is printed verbatim. That is the seat's (f) handling, inherited; at qual it now has 8 contrast sessions to cover instead of 1.

##### Q6. (h) and (j)

**(h): the PIN's wording.** The PIN at `stage.py:54-59` is §2 item 6 verbatim, clause by clause:

1. "a backend change after the lock STOPs the stage";
2. "a box of the same class gives the same identifier and is not detected";
3. "a box change follows p §6.2's respawn protocol with a new `BACKEND — characterization` entry, recorded by a dated note at the lock in force, no re-issue";
4. "a differing identifier STOPs and the seat rules".

It adds two parentheticals: "(before it generates)", which comes from the old PIN, and "(m:267)", which §4 (h) cites for the same-class clause. It drops the old "a box change ... STOPs" and "m:302's superseding BACKEND entry is the seat's to route", as §4 (h) asks. The runtime STOP message still carries that old route clause (N-2).

One observation for the seat, not a code finding: "recorded by a dated note at the lock in force" does not say where the note lives.
- If it were written into the lock file, the lock's sha256 would move. That sha256 is an identity field and the subject of m's licence check (c). A stage in flight under that lock would then be refused on resume by m's identity check after the load, which is a STOP.
- If the note sits on the lock's RESULTS entry, the seat's usual place for dated notes, nothing moves.

**(j): correct and exact.** Yes.
- The child imports p's driver by path under another name, so `main` never runs.
- It prints every loaded `valence_core` module.
- The parent applies `gshape.import_closure`'s filters and hashing unchanged: p and m excluded, the file must be a regular file in the repo, hashed by its committed blob.

On the laptop this matches the recorded closure exactly, as described under "What I ran". The precheck in WT reports no closure drift.

**(j): fail-closed.** Mostly. A child that exits non-zero, output that is not JSON, a file outside the repo, and an uncommitted or edited closure file each become a problem, and therefore a refusal before the load. A failed spawn, or a hang, does not become a named refusal (N-3), although nothing is loaded or recorded.

**(j): an environment where the fresh `-I -B` interpreter fails although the stage runs.** Yes: any environment whose third-party packages are reachable only through `PYTHONPATH` or the user site directory. `-I` ignores both, so the child's import of the driver fails at `numpy`.

What follows: the precheck at both gates, and the lock generator, report `G-SHAPE-p.json: the current import closure: the import closure: a fresh interpreter importing scripts/p_sessions.py failed ([...last stderr line...])`. The run exits 2 with nothing loaded or recorded. A G-SHAPE-p re-run cannot cure it; only the environment can, or an interpreter the seat routes.

On the box of record this is not expected: RESULTS records a venv at `/workspace/venv` created with `--system-site-packages`, and no `PYTHONPATH`. Also, `guard.runtime_import_set` already uses the same flags (Layer P, and the self-test's licence check), so p's self-test on any such box would fail first.

##### Q7. The driver

**`qual` wiring.** `run_gate_stage` runs in this order:
1. `precheck` at the gate;
2. the weights files on this box;
3. the DRIVER then the WEIGHTS line;
4. `stage.run_gate(unit, gate, ...)` with the driver's own precheck, refused if its unit, gate or stub flag differ;
5. the summary lines and m's exit code.

A `StageRefusal` exits 2; any other `SystemExit` exits 4, printed verbatim. The prior refusal surfaces as a `StageRefusal`, so exit 2. The order matches the docstring at `:62-70`.

**`qual-report` wiring.** `gate_report`:
- refuses a non-unit;
- refuses an existing report, both before and while holding the gate's own flock;
- writes p's report once.

The self-test covers a STOP when no stage has ended (named as the qual stage), a non-unit refusal, and a refusal while the flock is held.

**`campaign` still refused.** It is a subparser with no arguments that prints `refusal()` and exits 2. Passing `--unit` is an argparse error, also exit 2. Below the driver, `precheck` refuses any non-gate and `out_paths` raises on one.

**Can the self-tests load a model or write a record?** No.
- The `gcal`, `time` and `qual` refusal case runs with the pod id removed (POD ID ABSENT is unconditional) and the loader trapped.
- The wiring case replaces `precheck`, the weights check and `run_gate` with stand-ins, and makes the OLMo adapter module a stand-in.
- The report case points `DEFAULT_OUT_P` at a temporary root.
- Every stage self-test run is a stub run under `tempfile.mkdtemp` (`refuse_test_out` refuses the repo). The one non-stub call (`:1410`) is refused on the stub mismatch before the flock.
- `fresh_import_closure`'s child only imports.

Afterwards the WT had no new file. The refusal case's safety rests on one layer (N-6).

##### Q8. Self-test coverage: is anything important untested?

Yes. The gaps all sit on the non-stub path that keeps qual's refusals before the load (N-7):

- p's non-stub arguments to `prior_gate`;
- a G-TIME prior that ended STOP or PAUSE;
- `precheck`'s use of the v0.2 line, at qual only;
- `fresh_import_closure`'s failure branches, `gshape_drift_problems`' use of it, and the fresh closure against G-SHAPE-p's recorded one;
- `run_gate`'s gate-mismatch refusal;
- at qual: a bar-ended STOP, an interruption with resume over 24 sessions, the driver's `qual --resume`, and the arm keys.

Everything else in §2 is exercised:
- names and counts;
- a full qual PASS after G-TIME in one root, with the prior recorded;
- the report re-derived byte for byte;
- cross-gate log consistency;
- absent and not-ended priors refused before the factory;
- blinding at qual;
- a ProxyStop recorded under qual's names, blocking resume;
- the git admit and ignore rules;
- the campaign refusal.

178 of 178 pass on WT.

### Code's dispositions, round 1

No MAJOR or MINOR; seven NOTEs.

- **N-1, applied.** THE QUALIFICATION's PIN now says that the line must be whole: N-4's whole-line form only, and the
  line between backticks does not satisfy it. m's driver requires it of LOCK-m-OLMo's text as a substring.
- **N-2, not applied.** The backend STOP's message keeps its step-6 wording ("a superseding BACKEND entry is the seat's
  to route").
  - This keeps G-TIME's texts as they were, so `time`'s behaviour is unchanged, as the seat's §2 has it.
  - The wording does not contradict §2 item 6, and the seat's (h) asked for the PIN's wording (2026-11-09, §4 (h)).
  - The BUILD entry names it.
- **N-3, applied.** `fresh_import_closure` has a 600 s timeout (`CLOSURE_TIMEOUT_S`). It catches `OSError` and
  `subprocess.TimeoutExpired`, and each becomes a named problem, so the precheck refuses with exit 2.
- **N-4, applied at `qual`.**
  - `counts_problems` compares `COUNTS` with the committed gate files' n before the load. It runs in `precheck` at
    `qual` only, so G-TIME's precheck is unchanged.
  - The docstring now calls the counts m:302's. m's stage checks them against the files after the load, and at
    `qual` the precheck checks them before it.
- **N-5, applied.** `prior_problems` runs m's `prior_gate`, then requires the prior identity's `proposal` and
  `proposal_p_sha256` to be this run's (`identity.run_values()`).
  - `_run_gate_locked` calls it before the load.
  - `p_package_sha256` is not compared: G-TIME (p) ran under the step-6 package, which this move supersedes.
- **N-6, applied.** The driver's refusal case points `stage.DEFAULT_OUT_P` at its scratch root, beside the
  pod id's removal and the trapped loader.
- **N-7, applied.** New self-test cases:
  - **(a), (b): the prior.** `prior_problems` licenses a stub G-TIME (p) prior for a stub run and refuses it for a
    real run (PRIOR STAGE ON THE STUB). It refuses a prior under another m pin, one that ended STOP, and one whose
    identity is m's or another p proposal's.
  - **(c): the lock line and the counts.** A recorder on `qual_lock_problems` in the non-stub precheck, with the pod
    id removed: it is called at `qual` only. The counts check passes on the committed files and refuses a `COUNTS`
    that does not match them.
  - **(d): (j)'s edges.**
    - The fresh interpreter's three failure branches (it exits 1, prints no JSON, or cannot start) are each a named
      problem with an empty closure.
    - A recorder shows that the drift check takes its closure from `fresh_import_closure`.
    - The fresh closure has the same files as G-SHAPE-p's record-time closure: gshape's in-process closure after
      `inputs_of_record`, computed in a fresh process.
  - **(e): the gate mismatch.** A precheck taken at `time` and handed to a `qual` run is refused before anything is
    read or loaded.
  - **(f): the qual-only paths.**
    - A qual interruption, then `--resume`.
    - A qual bar STOP: m's status, p's report written with it, no p marker, and a later run refused before the load.
    - The qual arm keys (`p-olmo-qual|`).
    - The driver's `qual --resume`.
- **The reviewer's observation on (h), for the seat; nothing changed.**
  - §2 item 6's "recorded by a dated note at the lock in force" does not say where the note lives. A note written into
    the lock file would move the lock's sha256, which is an identity field and the subject of m's licence check.
  - Code's reading: the note sits on the lock's RESULTS entry, the seat's usual place for dated notes. The BUILD entry
    flags this for the seat and does not adjudicate it.
- **The reviewer's two disclosed departures.**
  - It wrote a scratch file of its self-test's output, and deleted it.
  - One malformed command stopped at an import.
  - Neither is a departure from the list of record: no file under `data/*/ckpt` or `data/*/reports` was read, listed or
    sized. The round-2 brief bars scratch files and redirected output.

## Round 2

### Blind review r2: the fixes after round 1 of the `qual` wiring (G-F0m-OLMo (p)), with (h) and (j)

#### Pin

- `git -C WT rev-parse HEAD`: `42c5a92abcf90c330297437460177492d93b5b51`. The worktree is detached. `git status --porcelain` showed only ` M scripts/p_sessions.py` and ` M valence_core/p/stage.py`, before my runs and after them.
- `valence_core/p/stage.py` sha256: `b8d6b7a4847a9c3418190fdde735e2b1b8c81462499045c3eeffb798c74696ab`
- `scripts/p_sessions.py` sha256: `e31af4f5ceb698ae1c1aa3ce13ead8e8de94b287f15a15b22b47ab237539a916`
- I re-hashed both files after the last run. Neither had changed.

**Counts: MAJOR 0, MINOR 0, NOTE 5.**

#### What I ran

Everything was model-free. Python always ran as the jlens venv's interpreter (3.12.9) with `-B`, under `nice -n 19`.

- **p's self-test in WT.** 183 of 183 checks pass, in 54 s. Round 1 had 178; the five new checks are the new stage cases. Afterwards:
  - `git status --porcelain` was unchanged;
  - a pruned `find` found no `__pycache__` and no `.pyc`;
  - the temp directory held no `p_stage_*` or `p-selftest-*` entry.
- **Time's strings against HEAD.**
  - I parsed `git show HEAD:valence_core/p/stage.py` with `ast`. HEAD's `build_report` `form`, `rule` and `contrast` strings are byte-identical to `REPORT_TEXT["time"]` and `CONTRAST_WITHHELD`.
  - I also diffed every non-self-test string literal of both files between HEAD and WT (the results are in Q3).
- **Time's precheck against HEAD.** I compiled HEAD's `stage.py` (from `git show`) into an in-memory module. With `RUNPOD_POD_ID` unset I ran three non-stub prechecks: HEAD's (time), WT's at time and WT's at qual.
  - They give 10, 10 and 11 problems.
  - HEAD's and WT's time lists are identical.
  - Qual adds exactly the v0.2-line problem; its POD ID ABSENT line differs by the stage name only.
- **The counts check.**
  - `counts_problems(u, "qual")` is `[]` for all three units.
  - In a throwaway process I set `COUNTS` to `{"qual": (9, 16), "time": (2, 1)}`. `precheck("OLMo-sft", stub=True, gate="qual")` then refuses, naming `the counts: ... n 8, not m:302's 9 at qual (COUNTS)`. At `time` the precheck passes, as declared.
- **(j).**
  - `fresh_import_closure()` returns 14 files with no problem. The map equals the committed `data/p/gates/G-SHAPE-p.json`'s `provenance.import_closure`, keys and sha256s, read by `git show`.
  - `gshape_drift_problems` on that artifact reports only the two uncommitted sources-map files, which is expected in WT.
- **The timeout's problem line.** I rendered it from a constructed `TimeoutExpired`, with no subprocess (see R2-3).
- **Git rules for the qual names**, via `git check-attr diff` and `git check-ignore -v -n`:
  - every `data/p/ckpt/*_qual*` name is `-diff`, and the reports are diffable;
  - the `.lock` and `.reserve-1` names are ignored;
  - the checkpoint and report names are admitted.
- **The step-6 review's labels.** I read the headings and a few note lines of the committed `results/raw/2026-11-09_p-step6_build_review.md`, to check the N-labels (R2-5).
- **m's code, read only:**
  - `prior_gate` (`m/stages.py:784-854`);
  - `_licensed` (`:1134-1142`);
  - `_licence` (`:611-634`);
  - `run_gate_stage` (`:1449-1529`);
  - `read_checkpoint`, `_read` and `_check_state` (`m/resume.py:682-684`, `:670-679`, `:555-638`);
  - `_script_policy` (`m/stages.py:2574-2606`);
  - the OLMo bars (`m/bars.py:594-620`).

**Departures, disclosed:**

1. **nice.** Python ran under `nice -n 19`. Most of the light git, grep, sed, find, ls and shasum commands ran without it; the brief says "each under `nice -n 19`".
2. **`git check-ignore -v -n`.** I ran it on qual output names under `data/p/ckpt` and `data/p/reports`. It is not on item 1's list. It prints the matching `.gitignore` rule and the name, with no size, time or content. None of those qual files exists in WT.
3. **A file the harness wrote.** One `git grep`, run with the brief's `-- . ':!data/**'` pathspec, matched lines in `results/raw/` and printed more than the tool shows. The tool harness saved that output to its own file, `<harness>/tool-results/b2bkzyqfi.txt`. I did not open it. It is a file written outside this review, though not by me. I re-ran the search over `*.py` only.
4. **A listing of `scratchpad/qualbuild/`.** One name-only `ls` showed the author's working files' names. There I read only the brief and `review_r1.md`.
5. **HEAD's `stage.py` run in memory.** This was the comparison above. No file was written and nothing was loaded.
6. **A committed raw outside the brief's spec list:** the step-6 review, as above. It is not under `ckpt` or `reports`.

Nothing under `data/*/ckpt` or `data/*/reports` was read, listed or sized.

#### Findings

##### R2-1 NOTE: `valence_core/p/stage.py:1940-1953`. N-4's precheck wiring is untested, and the check's text claims a refusal it never runs

- **What is wrong.** The case calls `counts_problems` directly, with `COUNTS["qual"]` patched to (9, 16). It never runs `precheck` with a bad count. The check's description still says "a COUNTS that does not is refused before the load (N-4)".
  - The call that makes the refusal is `precheck`'s `if gate == "qual": probs += [... counts_problems(unit, gate)]` (`:537-538`). No assertion depends on that call.
  - The qual stub runs do execute it, but it always returns `[]` there.
- **Failure scenario.** A later edit drops that call or narrows it to the wrong gate, and 183/183 still pass. A `COUNTS` edit, or a rebuilt qual schedule with another `n` re-pinned in a v0.2 lock, then surfaces only after the load. There it is m's `ValueError` (`m/stages.py:1480-1482`): p records an interruption, and the driver exits 1 on the traceback. That is round 1's N-4 scenario, back.
- **Fix.** Under the same patch, assert that `precheck(unit, stub=True, gate="qual")` raises a `StageRefusal` containing `the counts:`. With `COUNTS["time"]` patched, assert that `precheck(unit, stub=True, gate="time")` passes; that also pins "G-TIME's precheck unchanged". Both are stub prechecks: cheap, with no pod id and no git writes.

##### R2-2 NOTE: residual gaps in N-7's new cases (`valence_core/p/stage.py:1898-1939`, `:2014-2044`)

None of these assertions can pass vacuously, but four paths stay unpinned:

- **(a) The prior check's call site.** `_run_gate_locked` passes `stub=stub` to `prior_problems` (`:1003`). The non-stub argument is tested on the helper only (`:1913`), and every stage run in the battery is a stub run.
  - *Scenario:* a regression to `stub=True` at `:1003` passes the battery. A stub-written G-TIME checkpoint at `data/p/ckpt`, which can only be placed by hand, would then be refused only after the load, by m's `_licensed`. That is a STOP, not a refusal.
  - *Fix:* add one case through `run_gate(unit, "qual", fac, stub=False, pre=<stand-in: unit, gate "qual", stub False, identity_extra with m's pin, gate_line None>)`. Point `DEFAULT_OUT_P` at a scratch root holding p's schedules and a stub-written G-TIME checkpoint. Assert PRIOR STAGE ON THE STUB and that the factory is never called. The refusal comes before the substitutions; only the scratch lock file is created.
- **(b) The lock-line spy (`:1927`).** It records the unit only. Nothing asserts two things:
  - that the v0.2-line problem enters the qual refusal (and not the time one);
  - the check's claim "on the committed lock".

  *Scenario:* `precheck` keeps calling `qual_lock_problems` but drops its result, or passes it the working-tree text. A v0.2 lock generated on the moved code but missing item 1's whole line (round 1's N-1 backtick case) then passes. G-F0m-OLMo (p) would run under a lock that does not record G-TIME's port acceptance.

  *Fix:* have the spy return a sentinel problem, and assert it appears in `pc["qual"]` and not in `pc["time"]`. Record the text and compare it with `m_stages._committed(lock_rel(unit))[1].decode("utf-8", "replace")`.
- **(c) Two of `fresh_import_closure`'s branches.** The `TimeoutExpired` branch and the "not a regular file in the repo" branch (`:325-327`) are not exercised. The check at `:2036` cites "round 1's N-3", but only `OSError` reaches the shared `except`.
  - *Scenario:* a regression that drops `timeout=` or `subprocess.TimeoutExpired` from the tuple passes the battery. A hanging child then blocks the precheck with no bound, or escapes as a traceback.
  - *Fix:* patch `subprocess.run` in a narrow `with` to raise `TimeoutExpired`. Assert "could not run" and "TimeoutExpired", and that `timeout=CLOSURE_TIMEOUT_S` was passed (from the mock's call arguments). Have a second stand-in return stdout `[["valence_core.x", "/etc/hosts"]]` and assert the named problem.
- **(d) A G-TIME prior that ended PAUSE**, given without an adjudication, is untested. m refuses it (`m/stages.py:839-845`), and p never passes one. Low value while no adjudication input exists. Note it for the campaign's move.

##### R2-3 NOTE: `valence_core/p/stage.py:307-309`. The timeout's problem line drops the bound and prints the child's code

- **What is wrong.** `str(e)[:200]` of a `TimeoutExpired` is `Command '[...]' timed out after 600 seconds`, which is 684 characters with this command. The cut keeps the command's repr and loses the tail. Rendered for a box interpreter, the problem line is:

  `... could not run (TimeoutExpired: Command '['/workspace/venv/bin/python', '-I', '-B', '-c', '\nimport importlib.util, json, sys\nfrom pathlib import Path\nrepo = Path(sys.argv[1]).resolve()\nsys.path.insert(0, str(repo))\nspec = impor)`

  The type is named, so the refusal is still named.
- **Failure scenario.** On a box where the import stalls on the network volume, the refusal printed into the raw shows a fragment of `_CLOSURE_CODE` instead of the 600 s bound.
- **Fix.**
  - For `TimeoutExpired`, write `timed out after {CLOSURE_TIMEOUT_S} s`.
  - For `OSError`, write `{type(e).__name__}: {e.strerror} ({e.filename})`.

##### R2-4 NOTE: the docs lag the N-4 and N-5 fixes

- **What is wrong.**
  - **The driver's docstring for `qual`** (`scripts/p_sessions.py:66-70`) names, before the load, "``time``'s precheck at ``qual``, which also requires LOCK-p v0.2's line", then the prior "through m's ``prior_gate`` (ended PASS; no adjudication input)". It names neither the counts check (N-4) nor the requirement that the prior be p's (N-5: `proposal` and `proposal_p_sha256`). Nor does it name `prior_gate`'s other conditions (this unit's, m's pin, not the stub's).
  - **The stage's BEFORE THE LOAD paragraph** (`valence_core/p/stage.py:49-57`) enumerates the precheck's refusals but omits the counts at `qual`. THE QUALIFICATION paragraph does name them (`:20-23`).
  - **`lock_required`'s docstring** (`:363`) still says "every value the checkpoint's LOCK-p v0.1 must name verbatim". At `qual` the v0.2 lock must name the same values (the seat's §3: "every value `stage.lock_required` lists on the moved code").
- **Failure scenario.** Someone drafting the BUILD entry, LOCK-p v0.2 or the box checklist from the driver's docstring leaves out two pre-load refusals. They would be surprised by a refusal of an m-written or foreign prior. No run happens on wrong inputs, because the code refuses.
- **Fix.** Add the two clauses to `p_sessions.py:66-70`, for example "..., which also requires ... as a whole line and m:302's counts equal to the committed qual files' n" and "... through m's `prior_gate` (this unit's, ended PASS, m's pin, not the stub's; no adjudication input), then as p's (its identity's `proposal` and `proposal_p_sha256` this run's)". Add the counts to `:49-57`. Make `:363` say "LOCK-p v0.1 (and, at qual, v0.2)".

##### R2-5 NOTE: the new citations reuse labels that already name step 6's findings in the same file

- **What is wrong.** This build cites its round 1 as "round 1's N-3/N-4/N-5/N-7", and in places as bare "(N-4)" and "(N-7 (f))". The file already uses the bare labels for step 6's round-2 notes (the committed `results/raw/2026-11-09_p-step6_build_review.md`, where N-3 is "the attribution flag", N-4 "lock values as substrings" and N-5 "the gate line"). That review also has its own "## Round 1". Concretely:
  - `:1241` "(N-4)" (step 6: lock naming) and `:1949` "(N-4)" (this build: the counts) are the same label for two findings, in the same self-test.
  - `:31`, "N-4's whole-line form only" (step 6; the line N-1 fixed), sits in THE QUALIFICATION. That paragraph also introduces `counts_problems`, whose docstring cites "round 1's N-4" (`:450`) for a different finding.
  - "N-3" at `:181` and `:187` (step 6) versus "round 1's N-3" at `:295` and `:2036` (this build: the timeout).
  - "(N-5)" at `:1240` (step 6) versus "round 1's N-5" at `:493`.
  - Bare "N-7 (e)" and "(N-7 (f))" at `:1970-1971`; step 6's round 2 also has an N-7 (entries (8)/(9) pairing).
- **Failure scenario.** A reader tracing `:1949`'s "(N-4)", or "round 1's N-4", to the committed review lands on the lock-naming finding, not the counts one.
- **Fix.** Qualify the series wherever this build cites its review, for example "the qual review's round 1, N-4". Drop the bare "(N-4)", "N-7 (e)" and "(N-7 (f))" forms at `:1949` and `:1970-1971`.

#### Round 1's notes: dispositions checked

| Round-1 note | The author's disposition | My verdict |
|---|---|---|
| N-1 (docstring: "N-4's form") | THE QUALIFICATION says "as a whole line -- N-4's whole-line form only; the line between backticks does not satisfy it" (`stage.py:30-32`) | **Complete and correct.** The text now matches `qual_lock_problems` (`:469-475`) and the seat's §3. Its "N-4" label collides with this build's N-4 (R2-5). |
| N-2 (backend STOP message keeps the old route clause) | Not applied; to be named in the BUILD entry | **Acceptable.** The seat's §4 (h) and the 2026-11-10 §1 move the PIN's wording, which now follows §2 item 6 (`:58-63`). They do not move the runtime message. The message's "a superseding BACKEND entry is the seat's to route" does not contradict "a differing identifier STOPs and the seat rules": the STOP, its marker and the refusal of every later run are unchanged. The message has never printed (all three G-TIME (p) runs PASSed), so no record carries it. Keeping it leaves `time`'s strings byte-stable. **Condition:** the BUILD entry names it. Optionally, word the message to item 6 at `qual` only. |
| N-3 (no timeout; `OSError` uncaught) | `timeout=CLOSURE_TIMEOUT_S` (600 s); `except (OSError, subprocess.TimeoutExpired)` returns a named problem with an empty map (`:296`, `:304-309`) | **Complete and correct.** On expiry, `subprocess.run` kills and reaps the child, then re-raises. Spawn failures (ENOENT, EACCES, EAGAIN) are `OSError`. `_drift` turns either into a precheck problem, so the refusal is named, before the load, at both gates and in the lock generator. Wording: R2-3. The timeout branch is untested: R2-2 (c). |
| N-4 (counts asserted only after the load) | `counts_problems` (`:449-466`) in `precheck` at `qual` only (`:537-538`); docstring reworded (`:20-23`) | **Correct.** Complete at `qual`: the path is m's `schedule_filename` form, the bytes are HEAD's blob with the working tree identical, and a mismatch refuses before the load (probed). `time` keeps m's post-load `ValueError` deliberately, which keeps its precheck unchanged. That residual is pinned by the self-test's constant `COUNTS == {"time": (1, 1), ...}` and the committed n check. The precheck wiring is untested: R2-1. |
| N-5 (prior not checked as p's) | `prior_problems` (`:490-505`): m's `prior_gate`, then the prior identity's `proposal` and `proposal_p_sha256` against `identity.run_values()`; called by `_run_gate_locked` before the reservation, the run line and the factory (`:1000-1006`) | **Complete and correct.** The arguments match m's `prior_gate` signature and m's in-stage call (`_licensed`). The m-written and foreign-p priors of round 1's scenario are refused. It rightly does not check `p_package_sha256`, which moved since G-TIME. Details in Q2. |
| N-6 (driver refusal case not on a scratch root) | `mock.patch.object(stage, "DEFAULT_OUT_P", Path(td) / "p")` in that block (`p_sessions.py:376-379`) | **Complete and correct.** It covers `gcal`, `time` and `qual`. A hypothetical precheck that let a run through would now reach `run_gate` on a scratch root without schedules, and be refused at `verify_schedule_dir`, before the load, with nothing under `data/p`. |
| N-7 (a)-(f) (untested pre-load wiring) | New cases at `stage.py:1898-2044` and `p_sessions.py:395-401`, `:436-462` | **Correct; mostly complete.** Covered: (a) on the helper; (b) STOP; (c) by spy; (d) exit 1, not JSON, cannot start, the drift check's use of the fresh closure, and the fresh closure against G-SHAPE-p's record-time closure, computed in a fresh process; (e); and all of (f): bar STOP, interruption plus resume, arm keys `p-olmo-qual|`, the driver's `qual --resume`. Residual: R2-1 (the counts wiring) and R2-2 (the call site's `stub`, the spy's result and text, the timeout and outside-repo branches, PAUSE). |

#### Answers

##### Q2. Do the fixes introduce any new defect?

No code defect. The five NOTEs are tests, wording and docs.

**`prior_problems`.**

- **Argument order.** Correct. `m_stages.prior_gate(unit, "qual", prior_ckpt, None, proposal_sha256=..., prior_proposal_sha256s=(), require_real=not stub)` follows the signature `(unit, stage, prior_ckpt, prior_adjudication=None, *, proposal_sha256, prior_proposal_sha256s, require_real)`. It equals m's in-stage call in `_licensed` (`m/stages.py:1140-1142`):
  - the same path;
  - `proposal_sha256` from the same `identity_extra`;
  - `()` against `_extra`'s `[]`, since p passes no `prior_proposal_sha256s`;
  - no adjudication;
  - `require_real`: p's `not stub` against m's `not _is_stub(adapter)`, equal on the box (a real adapter behind the proxy) and on the stub.
- **Reads.** It reads the checkpoint as m does: through m's `prior_gate` (`_resume.read_checkpoint`, then `_read` and `_check_state`), then m's `read_checkpoint` again for the identity. It runs outside the substitutions, but none of that path reads a substituted global:
  - `_check_state` never consults `IDENTITY_KEYS_OLMO` or `Identity`;
  - `_check_unit` calls `keys.templates`, which entry (2) does not replace (`P_FUNCS` is `item_key`, `arm_key`, `sched_key`, `gate_sched_key`);
  - `stage_name`, `written_on_stub` and `accepted_proposals` read nothing substituted.

  So the pre-load answer is m's in-stage answer, unless the file changes in between. No p writer can change it: G-TIME has ended, and `time-report` writes only p's report.
- **Error handling.**
  - It catches `SystemExit` and `ValueError` from `prior_gate`, which covers everything `prior_gate` raises by design, and `SystemExit` from the second read.
  - A hand-corrupted checkpoint whose identity lacks `n` would raise `KeyError` inside m's `_check_state` (`m/resume.py:588`). It escapes as a traceback (exit 1), before the load and with nothing recorded. That is unchanged from round 1's direct call, and m's in-stage call does the same. It is not new.
  - The p-identity message prints at most 24 characters of the prior's `proposal` and `proposal_p_sha256`: no session data.

**`counts_problems`.**

- **Paths.** `data/p/schedules/{unit}_{gate}_{template}.json` is m's `schedule_filename` form. The six qual files it reads (two per unit) are in `git ls-files`, beside the six time files.
- **Committed versus working tree.** It reads through `_committed`: HEAD's blob, with the working-tree bytes required identical. On the box that is exactly what m's `load_committed` reads from `out/schedules` = `data/p/schedules`. In a stub run m reads the scratch root's regeneration, which is byte-equal by construction; the driver's self-test asserts the committed directory equals a fresh regeneration.
- **Side effect.** Stub qual runs now need those files committed. That is fail-loud in a dirty tree, and not a defect.
- **Hard-coded root.** `data/p` is written out rather than derived from `DEFAULT_OUT_P`, consistent with `SCHED_MANIFEST_REL`.

**The timeout and exception handling.** Correct; see N-3's row. The only new rough edge is the message (R2-3). `for name, f in loaded` assumes a list of pairs. Another JSON shape on the last line would raise `TypeError`, but only a foreign `sys.executable` could print one, so it is not reachable with the fixed child code.

**The new tests.**

- **Vacuous passes.** None. Each new assertion can fail:
  - the prior cases need a passing stub G-TIME first; a failed one raises, and the battery records "_selftest raised";
  - `seen_lk == [unit]`, `seen_fc == [1]` and `rec_keys == sorted(fc1)` fail on a missing call, a double call or a failed child;
  - the failure-branch cases check the branch-specific words.

  Two check texts claim more than they assert: R2-1's "refused before the load", and `:1948`'s "on the committed lock" (R2-2 (b)).
- **State left behind.** None. Every patched global is restored:
  - `qual_lock_problems` (`:1927`, `finally :1939`);
  - `fresh_import_closure` (`finally` after `gshape_drift_problems`);
  - `COUNTS`, restored in place by `clear()` and `update()` in a `finally`, keeping its identity and order;
  - `sys.executable` (`mock.patch.object` context);
  - `os.environ` (`patch.dict(..., clear=True)`);
  - the phantom `sys.modules` entry (popped in a `finally`).

  In the driver, `stage.precheck`, `stage.run_gate`, `weights_files_problems`, `_load_olmo`, the stand-in adapter module and `stage.DEFAULT_OUT_P` all sit in `mock` contexts. Each assignment sits directly before its `try`, with nothing between them that can raise.
- **Records written.** None:
  - every stage run is a stub run under `tdir` (`mkdtemp`, removed in a `finally`), and `refuse_test_out` refuses repo roots;
  - the non-stub prechecks write nothing;
  - the children run `-I -B`;
  - the `rec_code` child's `inputs_of_record(canonical=False)` and m's `olmo_stack` only read.

  After the run, WT was unchanged and the temp directory held no leftover.
- **A model run.** None. The double is m's scripted adapter. The non-stub prechecks refuse on POD ID ABSENT (`pod_id()` reads the environment only). The driver's loader is trapped.

##### Q3. Is `time`'s behaviour still unchanged?

Yes.

- **Outputs and names.** These are unchanged:
  - `out_paths` defaults to `time`, giving the `_time_` names;
  - the run line's keys and `stage`, the end line and the marker document are the same;
  - `label(unit)` is `G-TIME-OLMo-{ckpt} (p)`.
- **Report form.** HEAD's `form`, `rule` and `contrast` are byte-identical to `REPORT_TEXT["time"]` (checked with `ast`).
- **Refusals.**
  - HEAD's and WT's non-stub precheck at `time` give the same 10 problems, verbatim. `counts_problems` and `qual_lock_problems` do not run at `time`.
  - Of HEAD's string literals, every one absent from WT is now a `{gate}`-formatted string that renders identically at `time`, with one exception: `run_gate`'s refusal of a mismatched precheck now names the gate. The driver cannot reach that refusal, because it always passes its own precheck at its own gate.
  - `time-report`'s refusals and its lock's `what` render identically.
- **Intended changes.** The only behavioural change is (j)'s fresh interpreter in `gshape_drift_problems`, at both gates, which the seat's §1 intends. The backend STOP's text is kept on purpose (N-2).

##### Q4. Is anything from round 1's questions 3-5 now worse?

No.

- **Refusals after the load (round 1's Q3).** Better. At `qual`, the counts mismatch (N-4) and an m-written or foreign-p prior (N-5) are now refused before the load. A hung or unstartable closure child is a named pre-load refusal (N-3). Nothing new runs after the factory. m's licence (`_licence`) has no gate-specific clause, and m's in-stage `prior_gate` gets the same arguments as p's pre-load call. As before, only the backend identifier, by construction, and file changes between the precheck and the load can surface after it.
- **The lock line (round 1's Q4).** Unchanged in code. The docstring is fixed (N-1).
- **Blinding (round 1's Q5).** Unchanged. The new messages carry the prior's proposal name and hash, schedule-file `n`, file paths and a child's last stderr line. None of them carries contrast-session data. The qual blinding case still passes (6, 1, 2 free rounds, identical report and lines).

### Code's dispositions, round 2

No MAJOR or MINOR; five NOTEs. All were applied before the commit. They were checked by the self-tests, not by a third
blind round. The reviewer's verdicts on round 1's dispositions are in its table: N-2's disposition is "acceptable",
on condition that the BUILD entry names it, and it does.

- **R2-1, applied.** With `COUNTS` patched, the case asserts two things:
  - the stub precheck at `qual` refuses with "the counts:";
  - the precheck at `time` passes, so G-TIME's precheck is unchanged.
- **R2-2, applied.**
  - **(a): the call site.** A non-stub qual run on a stub-written G-TIME (p) prior, through `_run_gate_locked`
    itself, is refused before the load (PRIOR STAGE ON THE STUB). The factory is never called, and no call log or
    reservation is written.
  - **(b): the lock spy.** It records the unit and the text and returns a sentinel problem. The case asserts:
    - the text is the committed lock's;
    - the sentinel enters the qual refusal and not the time one.
  - **(c): two branches.** A `TimeoutExpired`, with `timeout=CLOSURE_TIMEOUT_S` passed and named, and a module file
    outside the repository are each a named problem with an empty closure.
  - **(d): a PAUSE prior.** A G-TIME prior that ended PAUSE, with no adjudication (no input for one exists), is refused
    (PRIOR STAGE PAUSE).
- **R2-3, applied.** The problem line now reads "TimeoutExpired: timed out after 600 s", or, for an `OSError`, its type,
  `strerror` and filename. It no longer quotes the child's code.
- **R2-4, applied.**
  - The driver's `qual` docstring names the counts check and the prior's p-identity check, and gives `prior_gate`'s
    conditions in full.
  - BEFORE THE LOAD names the counts at `qual`.
  - `lock_required`'s docstring says "LOCK-p v0.1 -- and, at `qual`, its v0.2".
- **R2-5, applied.**
  - Every citation of this build's review now reads "the qual review's ...", so the bare labels belong to step 6's
    reviews.
  - THE QUALIFICATION's "N-4" now reads "the whole-line form of step 6's N-4".
  - The BUILD entry's values-check found two citations this relabelling had missed: a comment capitalised "Round 1's",
    and one split across a line break. Both were relabelled before the commit, and the checks ran again on the final
    code.
- **The reviewer's six disclosed departures.** For item 8 of the list of record, one of them belongs with the seat:
  `git check-ignore -v -n` over names under `data/p/ckpt` and `data/p/reports`.
  - Item 1 does not list it, and item 2 does not bar it. It prints the matching `.gitignore` rule and the name, and
    nothing of a file; none of those files existed in the worktree.
  - Others ran the same kind of command:
    - round 1's reviewer, `git check-ignore`;
    - Code's own check of the qual names, `git check-ignore -q`, exit codes only;
    - the stage's self-test, as at step 6, now over both gates' names.
  - The BUILD entry lists them for the seat. Code rules on none.
- **The reviewer's other five departures** read nothing under `data/*/ckpt` or `data/*/reports`:
  - light commands run without `nice`;
  - one `git grep`, with the brief's pathspec, whose long output the harness saved to its own file, unopened;
  - a name-only `ls` of Code's scratch directory;
  - HEAD's `stage.py` run in memory;
  - a committed raw outside the brief's list.
