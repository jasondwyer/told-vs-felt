# The `qual` wiring (G-F3): the blind review, Code's dispositions, and round 2's mutant runs

*Code's raw, PI date 2026-11-12.*
- *What was reviewed:* the uncommitted edit that wires `qual` in `scripts/mf3_sessions.py`. The candidate (sha256
  `fd5821bd…627d`) was the working tree's file at the review. It was checked against HEAD's driver blob
  (`8d878f4a…00e7`, at `05ef75d`).
- *How:* one blind agent, read-only on the main checkout, under a brief that quotes the list of record v2's items 1–5
  as written.
  - It worked in a sparse clone, with every `data/*/ckpt` and `data/*/reports` directory left out of the working tree.
  - It ran the self-test with every model import blocked.
  - It built 44 one-defect mutants of the production code.
- *Outcome:* no MAJOR, 1 MINOR and 7 NOTEs.
  - Of the 44 mutants, 39 were KILLED and 5 SURVIVED: 3 equivalent and 2 gaps. The gaps are the MINOR's.
- *After the review:* Code applied the MINOR and four of the NOTEs, one of them in part (below).
  - The self-test passes 214/214 on the final bytes. The candidate the review read passed 211/211.
  - Round 2 re-ran the five survivors through the reviewer's harness against the fixed self-test, in a fresh sparse
    clone. Both gaps are killed, and two of the three equivalents with them; Q20 survives, equivalent (round 2's table).
- *Code's masked scan of the reviewer's transcript* (no output text printed but one count):
  - 93 distinct Bash commands, over every row of the transcript (16 of them are held only in its request-blob rows).
  - Two name a `ckpt` or `reports` path, both clone-internal:
    - the clone's set-up: its sparse-checkout patterns, and a `find` over its data/ directories that prunes every
      `*/ckpt` and `*/reports` (the report's "pruned `find`": the same call, not a third);
    - a name-only count of those directories in the clone, which printed 0.
  - None ran `git status` in the main checkout: every `git status` it ran was in the clone.
- *This raw:* Code's dispositions, round 2's table, then the report verbatim.
  - The report was extracted by script from the agent's hand-back (the text's sha256 `a9714872…`, its final newline
    included; 187 lines).
  - It holds no local path and no clock time.
- *Nothing ran on a model.*

## Code's dispositions

- **MINOR-1 (Q35, Q36), qual's post-load STOPs untested.** Agreed. Time's three stand-in-loader cases are added for
  `qual`, and for `id`, which had the same gap:
  - a re-read that refuses;
  - a moved refs/main;
  - another model id.

  Each STOPs with exit 4 before the stage, naming its evidence, with no re-read line.
- **NOTE-1 (Q20), the precheck's schedule list.** Not changed. It is equivalent (`verify_schedule_dir` checks the
  whole directory), the same as the `id` wiring's M14.
- **NOTE-2 (Q12), leading whitespace.** Agreed. The lock-line check gains a case: v0.2 with its path line indented
  is refused for `qual`, and accepted for `time` and `id`.
- **NOTE-3 (Q13), the refusal order.** Agreed. A case is added: an earlier blob that also names `corr.py` with a second
  sha256.
  - `qual` refuses it for the missing lines alone, so the line check comes first, as the PIN says.
  - `time` refuses it for the doubled sha256.
- **NOTE-4, the `id` precheck's PIN.** Agreed. Its text now reads "the prior -- id_prior_checkpoint
  (stage_prior_checkpoint for "id"), then stages.prior_gate …". v0.2 §5 quotes the old text verbatim on the blob of
  record, and v1.0 re-quotes it (NOTE-5).
- **NOTE-5, re-quoting and re-anchoring at v1.0.** Recorded for v1.0:
  - the WIRED_CMDS sentence and the `id` precheck PIN are re-quoted;
  - the other v0.2 sites are re-anchored on the new blob;
  - the four new PIN sites are declared at v1.0.

  The reviewer's table gives the candidate's lines. NOTE-4's re-wrap adds a line at `:443–444`, so on the final blob
  (`285eed04…`) every site below it sits one line lower (the values-check's item 28). The final anchors, by grep:
  - `time`: `:102`, `:112`, `:183`, `:193`, `:318`, `:452`, `:529`, `:554`, `:650`;
  - `id`: `:138`, `:313`, `:440`, `:644`;
  - the re-issue's PIN: `:119`;
  - the four new sites: `:154`, `:306`, `:432`, `:638`.
- **NOTE-6, what binds G-F3's inputs.** Both suggestions are adopted, as Code's commitments for G-F3:
  - the G-F3 entry records, at launch, the digests of its prior (`Q-F3_time-r2.json`) and of G-ID-F3's artifact;
  - no driver commit lands while G-F3 is open, because a `--resume` after one would continue under another DRIVER
    line.
- **NOTE-7, the self-test's "exactly once".** Agreed in part. The identity check now asserts that each line opens
  some line of the committed lock (one or more).
  - That alone does not make a restating v1.0 safe (the values-check's item 85, by reading). The "moved" and
    "indented" variants edit only the path line's first occurrence. A v1.0 above v0.2 that restated that line would
    take the edit, v0.2's own line would still open a line, `qual` would accept both variants, and the lock-line
    check would FAIL.
  - That failure would be loud, a FAIL, never a false PASS. No committed lock restates the line, and no driver
    commit lands while G-F3 is open (NOTE-6).
  - Recorded for the campaign wiring, the next driver edit: the two variants are to edit every line that opens with
    the path line.

## Round 2: the mutants against the fixed self-test

- *How:* the reviewer's harness, its work directory moved to a fresh sparse clone at HEAD `a225a89`, with the model
  imports blocked. Since `05ef75d`, only RESULTS.md, four `results/raw/2026-11-11_p-qual*` files and data/p had
  changed. The reviewer's generator regenerated all 44 mutants, unchanged, on the fixed candidate
  (`285eed04…0e44`). Every anchor still matched.
- *Scope:* the five round-1 survivors. The other 39, killed in round 1, were not re-run.
  - The edits since round 1 add cases, change one production text (the `id` precheck's PIN, NOTE-4) and relax one
    assertion (the identity check's count, NOTE-7). The WIRED_CMDS sentence was already revised in the candidate.
  - The kills that rest on the identity check (Q03, Q06a, Q08a, Q15, Q31) fail on its other conjuncts, so the
    relaxation does not reach them: by reading, not by a run (the values-check's item 91 reads it the same way).
- *The baseline under the harness* is 213/214. The one FAIL is the constants check, which reads mlx_lm's source while
  the harness blocks it. "Killed" means any further FAIL, or fewer checks run.

| mutant | the defect | round 1 | round 2 | killed by |
|---|---|---|---|---|
| Q35 | the post-load MODEL ID STOP skipped for qual | SURVIVED (gap) | KILLED, 211/214 | the new post-load check for qual; the final audit (the stage reached) |
| Q36 | the post-load SNAPSHOT MOVED STOP skipped for qual | SURVIVED (gap) | KILLED, 211/214 | the same two |
| Q12 | `lstrip()` before `startswith` | SURVIVED (equivalent on every committed blob) | KILLED, 212/214 | the lock-line check's indented case |
| Q13 | the lock-line check after the m-file and WEIGHTS reads | SURVIVED (equivalent: order only) | KILLED, 212/214 | the new refusal-order check |
| Q20 | qual's precheck loads time's schedule files | SURVIVED (equivalent) | SURVIVED, 213/214 (the baseline) | equivalent: `load_committed` verifies the whole directory |

- *Outcome:* both gaps are killed, and so are two of the three equivalents, by the cases NOTE-2 and NOTE-3 led to. Q20
  survives, equivalent. In every run the model-import blocks held, and the clone changed only in its driver.

## The reviewer's report (verbatim)

# Blind review: the `qual` wiring in `scripts/mf3_sessions.py` (candidate `fd5821bd…627d`)

**Bottom line:** no MAJOR finding. The wiring does what the routing (§9 item 5) and v0.2 §9 item 1 say. `time` and `id` are unchanged in what they do, print and refuse. No path in question 3 is reachable.
- The self-test killed 39 of 44 one-defect mutants of the edit's production code.
- Of the 5 survivors, 3 are equivalent.
- The other 2 sit on shared post-load lines the edit did not touch, and they expose the one real test gap (MINOR-1).

The diff applied to HEAD `05ef75d` (driver blob `8d878f4a…`) reproduces `fd5821bd…627d` byte for byte. The main checkout's working file had that same digest before and after the review.

Bare line numbers below are the candidate's. "m" means `scripts/m_sessions.py`.

## Findings (most severe first)

**MINOR-1. qual's post-load STOPs are never tested for qual.**
- **Where:** the candidate's post-load checks at :700–711 (SNAPSHOT RE-READ REFUSED, SNAPSHOT MOVED, MODEL ID) are tested only for `time`, in `_selftest_time` at :1601–1625. `_selftest_qual` tests only the clean re-read (`post_ok`, :2737), the same as `_selftest_id` (:2188).
- **The carried form does more:** m's qual self-test checks all three STOPs for qual (m :5125–5154 and :5186–5218).
- **Failure scenario:** an edit that makes any of these STOPs skip qual still passes 211/211. G-F3 would then run its 40 sessions on an adapter whose model id is not the snapshot's, or after refs/main moved during the load.
- **Shown by:** mutants Q35 (:707) and Q36 (:704). Each adds a one-line `stage != "qual" and` condition, and both survive the full self-test.
- **Severity:** no wrong run with the candidate as written, since the code is stage-independent. The gap is outside the edit's lines and the same as the `id` wiring's.
- **Fix:** add the three stand-in-loader cases from :1601–1612 to qual's Qwen section.

**NOTE-1. qual's precheck schedule list is not pinned (Q20 survives; equivalent).**
- `wanted` for qual (:473–474) could name another stage's files with no change in behaviour.
- The reason: `stages.load_committed` first runs `schedule.verify_schedule_dir` over the whole directory (every file byte-identical to the regeneration, the manifest's shas, no unlisted file). The stage then loads qual's six files itself after the load.
- m's self-test spies on `load_committed` per stage (m :5188–5221); mf3's does not. Adding the spy is optional.

**NOTE-2. "At a line's start" is not pinned against leading whitespace (Q12 survives; no committed lock is affected).**
- Using `ln.lstrip().startswith(x)` instead passes the self-test, because its "moved" variant prefixes `x `, not spaces.
- No committed LOCK-m-F3.md blob is affected:
  - v0.2 (`ac82b943…`) has each line exactly once, at column 0 (:91 and :109 of the lock).
  - The re-issue (`70da4a70…`, `f674583`) and v0.1 (`377c5d60…`, `1e79955`) contain neither string even as a substring, so any form of the check refuses them.

**NOTE-3. Refusal order is untested (Q13 survives; equivalent).**
- Moving the lock-line check after `lock_m_modules`/`lock_weights` changes only which message wins when a lock fails both checks, and no committed blob does.
- The PIN at :306–311 says the check comes "before the m files and the weights are read"; nothing tests that order.

**NOTE-4. The id precheck's PIN names a call the precheck no longer makes.**
- The PIN at :440–449 (declared at v0.2 and quoted verbatim in v0.2 §5 at :375) says "the prior -- id_prior_checkpoint, then stages.prior_gate".
- The precheck now calls `stage_prior_checkpoint(stage, paths)` at :495, which `id_prior_checkpoint` wraps.
- It is true in effect but literally stale; a reader checking the quote against the code won't find the call. Fix the text, or note it in v1.0.

**NOTE-5. v1.0 will need to re-quote one PIN sentence and re-anchor the rest.**
- One v0.2-quoted PIN changes text: the `time` wiring's WIRED_CMDS sentence (blob of record :98–99, candidate :108–109).
  - It was: "qual and campaign stay refused until their steps; id is wired at its own step (the id wiring's PIN, below)."
  - It is now: "campaign stays refused until its step; id and qual are wired at their own steps (the id and qual wirings' PINs, below)."
- Every other quoted site is unchanged in text but has moved:

| wiring | blob of record → candidate |
|---|---|
| time | :92→:102, :102→:112, :150→:183, :160→:193, :278→:318, :386→:451, :462→:528, :487→:553, :577→:649 |
| id | :128→:138, :273→:313, :375→:440, :571→:643 |
| the re-issue's PIN | :109→:119 |

- The four new PIN sites, declared at v1.0, are at :154, :306, :432 and :637.

**NOTE-6. What does and doesn't bind G-F3's inputs (the stage library's and m's form, not the edit's).**
- The prior and the artifact are checked by content (identity, end, cap, provenance, proposal), not against the digests v0.2 §1 records (r2 checkpoint `ff644fa1…`, artifact `ea8f7d3a…`). The committed artifact does match `ea8f7d3a…`.
- G-F3's checkpoint records the prior's path and status, not its digest.
- The checkpoint identity binds the lock, proposal, package, m files, weights, cap and path, but not the driver blob. So a `--resume` after any later driver commit would continue G-F3 under a different DRIVER line, with no refusal.
- Neither can cause a wrong-path run: the path is the lock's constant, and `_locked` STOPs a G-ID PASS for this backend.
- Suggestion: the G-F3 entry records both digests at launch, and no driver commit is made while G-F3 is open.

**NOTE-7. The self-test's lock-line count will break at v1.0.**
- :2297 asserts each line occurs exactly once at a line's start in the committed lock; the driver needs only one or more.
- A v1.0 that restates either line in its own part would fail the self-test at v1.0's commit, though the driver would accept it. No effect on G-F3.

## Mutant table

44 one-defect mutants. Each is an exact single replacement in production code outside `_short`…`main`, generated from the candidate.

- **Screening:**
  - Mutants that change only qual were screened by the qual block alone (14 checks, about 32 s).
  - Mutants that also change `time` or `id` (marked "driver") were screened by the driver's whole integration self-test (67 checks, about 86 s).
- **Confirmation:** every screen survivor was re-run through the full `--selftest` (211 checks, about 130 s).
- **Survival rule:** the run made the baseline number of checks, and its only FAIL is the baseline's mlx_lm-source constants check.
- **Baselines under the import block:** full 210/211, driver-only 66/67, qual-only 14/14.

Short names used in the table:
- "the refusal table": the self-test's 35 pre-load refusal cases ("qual refuses before the load").
- "the trap count": the final "loaded nothing" check, which counts how often the loader trap was reached.
- "lock-line check": the earlier-blob, "moved" and "dropped" variants, plus "time and id accept all three".
- "load-reach group": the cases that clear every pre-load check and must reach the loader.

| mutant | defect | result | killed by / why it survived |
|---|---|---|---|
| Q01 | lock-line check dropped | KILLED | lock-line check (earlier blob); the refusal table |
| Q02 | lock-line check made a substring test | KILLED | lock-line check ("moved") |
| Q03 | QUAL_LOCKED_PATH = "cached" | KILLED | identity check; stub PASS run (PATH MISMATCH on the FAIL artifact); 6 more |
| Q04a | precheck `require_real=False` (driver) | KILLED | id's and qual's refusal tables; both trap counts |
| Q04b | `require_real` off for qual only | KILLED | the refusal table (prior or artifact on the stub, prior at another cap); the trap count |
| Q05 | qual's precheck calls `prior_gate` as "id", so the artifact is skipped | KILLED | the refusal table (5 artifact cases); the joined REFUSED line; the trap count |
| Q06a | QUAL_PRIOR_CKPT_NAME = the first run's name | KILLED | identity and constants check; stub runs; 9 more |
| Q07a | stage called with `resume=False` | KILLED | stub `--resume` check |
| Q07b | `main` drops `--resume` for qual | KILLED | load-reach group (an open checkpoint with `--resume`); the trap count |
| Q08a | QUAL_COUNTS with A1 8, A3 4 | KILLED | identity check (counts ≠ the plan); then the stage's ValueError |
| Q08b | stage given TIME_COUNTS | KILLED | crash: `run_gate_stage` ValueError, so "integration selftest raised" |
| Q09 | stage given gate "time" | KILLED | crash: `prior_gate` ValueError ("takes no prior stage") |
| Q10 | qual calls `run_gid_pair_f3` | KILLED | crash: `_extra` ValueError (`locked_path` at G-ID) |
| Q06b | first-run refusal applies to id only | KILLED | stub STOP check; the refusal table (link and name cases); the trap count |
| Q06c | the stage's prior is `out_paths("time")` (m's form) | KILLED | stub PASS, STOP, resume and pending checks (PRIOR STAGE ABSENT) |
| Q06d | the precheck's prior is `out_paths("time")` | KILLED | the refusal table; joined line; load-reach group; `post_ok`; the trap count |
| Q06e | first-run check tests the name constant, not the resolved path (driver) | KILLED | id's and qual's link cases; id's stub check; both trap counts |
| Q37 | ID_PRIOR_CKPT_NAME used for both stages (same value) | KILLED | only through the self-test's patch of QUAL_PRIOR_CKPT_NAME: stub STOP check, "by name" case, the trap count |
| Q38 | the stage's prior taken through `id_prior_checkpoint` (same value except the STOP message's stage name) | KILLED | stub STOP check, through the same patch |
| Q11a | only the cap line required | KILLED | lock-line check ("moved") |
| Q11b | only the path line required | KILLED | lock-line check ("dropped") |
| Q12 | `lstrip()` before `startswith` | SURVIVED (full 210/211) | equivalent on every committed blob (NOTE-2) |
| Q13 | lock-line check after the m-file and WEIGHTS reads | SURVIVED (full) | equivalent: refusal order only (NOTE-3) |
| Q32 | lock-line check applied to id too (driver) | KILLED | "time and id accept all three" |
| Q33 | lock-line check applied to time too (driver) | KILLED | same |
| Q15 | QUAL_REASONING_CAP = 60 | KILLED | identity check (`_extra` refuses 60 on a model); 10 more |
| Q31 | qual's `locked_path` never set | KILLED | identity check; 10 more |
| Q17 | precheck prior block for id only (HEAD's form) | KILLED | the refusal table; joined line; the trap count |
| Q18 | id's ARTIFACT EXISTS refusal applied to qual | KILLED | load-reach group; `post_ok`; the trap count |
| Q19 | qual's own checkpoint checked at time's r2 path | KILLED | the refusal table; load-reach group; `post_ok`; the trap count |
| Q20 | qual's precheck loads time's schedule files | SURVIVED (full) | equivalent: `verify_schedule_dir` checks the whole directory (NOTE-1) |
| Q07c | CHECKPOINT EXISTS ignores `--resume` for qual | KILLED | load-reach group; the trap count |
| Q30 | qual's `prior_gate` given `proposal_sha256=None` | KILLED | the refusal table (prior and artifact under another proposal); the trap count |
| Q21 | stage given `out_root=DEFAULT_OUT` | KILLED | the stub checks (no schedules at the default root); `post_ok` alone cannot see this |
| Q22 | stage given `ckpt_path` = time's r2 | KILLED | the stub checks (STAGE ENDED) |
| Q23 | stage given no prior | KILLED | the stub checks (PRIOR STAGE REQUIRED) |
| Q24 | out-root seam refusal skipped for qual | KILLED | the seam check |
| Q25 | Qwen path skips the precheck for qual | KILLED | the refusal table; joined line; the trap count |
| Q26 | snapshot-revision refusal skipped for qual | KILLED | the refusal table; the trap count |
| Q27 | driver check skipped for qual | KILLED | the refusal table; joined line; load-reach group; the trap count |
| Q34 | qual exits 0 whatever the status | KILLED | the exit-code check |
| Q35 | post-load MODEL ID STOP skipped for qual (shared lines) | SURVIVED (full) | gap (MINOR-1) |
| Q36 | post-load SNAPSHOT MOVED STOP skipped for qual (shared lines) | SURVIVED (full) | gap (MINOR-1) |
| Q28 | `--selftest`/`--build-schedules`/`--out` refusal skipped for qual | KILLED | the refusal table (3 top-level cases); the trap count |

The four "crash" kills (Q08a's second failure, Q08b, Q09, Q10) come from the stage library's own ValueError inside the stub run. On the Qwen path the same defects would raise after the load and before any session runs.

## What I checked and found right

**Question 1, spec conformance:**
- **Counts and launch:** QUAL_COUNTS are m:297's counts in `keys.TEMPLATES` order and equal `schedule.GATE_PLAN`'s qual rows (40 sessions, 24 sham). They go through `stages.run_gate_stage(gate="qual")` at :722–724, which refuses any other counts. Keys are `m-f3|{template}|{s}`; the outputs are `Q-F3_qual*` under data/mf3.
- **The lock:** must be LOCK-m-F3.md committed at HEAD with an identical working tree, naming the proposal's sha. Both QUAL_LOCK_LINES must then open a line (:361–366), before the m-file and WEIGHTS reads. The self-test's "earlier blob" is byte for byte the re-issue's committed blob (`70da4a70…`), which carries v0.1's text.
- **Path and cap:** `locked_path` "uncached" and cap 120, both validated by `_extra(stub=False)`. The cached path is reachable only with `locked_path` "cached":
  - `_locked` turns a G-ID PASS for this backend into PATH MISMATCH.
  - The FAIL artifact licenses uncached on every backend.
- **The prior:** `<root>/ckpt/Q-F3_time-r2.json` through `checkpoint_path`, with a resolved name of `Q-F3_time.json` refused, a link included. A copy of the first run under the r2 name is refused by `prior_gate`'s cap check (60 ≠ 120).
- **The prior gate:** `prior_gate("qual", require_real=True, cap 120)` runs in the precheck and checks:
  - G-TIME-F3 ended PASS, under this proposal, not on the stub, at cap 120;
  - the G-ID artifact is a file, under this proposal, not on the stub, at cap 120.
  - The stage repeats it after the load.
- **Refusal coverage:** the self-test's 35 refusal cases are id's 33 minus its four artifact-EXISTS cases, plus the earlier-lock case and five artifact cases.

**Question 2, `time` and `id` unchanged:**
- The lock-file and cap lookups give the same values for `time` and `id`, and the lock-line check and `locked_path` branch are qual-only.
- id's precheck makes the same prior call and the same artifact-EXISTS check, and its PRIOR PATH REFUSED text renders identically.
- The time and id branches of `run_stage` and their `--help` output are unchanged.
- Only top-level output changed: the parser description, the qual subparser's help line, and the "no action" line.

**Question 3, hazards:**
- The order is: flags → out-root seam → identity → precheck, driver check and snapshot check (with the revision checked against the lock), refused together → DRIVER and SNAPSHOT lines → load → re-read and model-id check → stage.
- `main` never passes `adapter_factory`. An out root without a factory is refused before the identity is built, and `_out_root_guard` refuses a non-stub root outside data/mf3.
- qual writes nothing to gates/.
- The only refusal after the load is PATH MISMATCH, which needs the loaded backend and cannot fire on the FAIL artifact; the precheck's PIN declares this.
- No production branch still treats "not time" as "id".

## Disclosures

- **Outside the work directory:** one stray file, written by mistake by a shell redirect into the per-user temp root above the scratchpad. It held a `diff` of HEAD's driver against the candidate (code text only) and was deleted in the next command.
- **Main checkout, read-only:**
  - Read by path: the spec files the brief names, plus excerpts of `valence_core/m/resume.py`.
  - `git show` of LOCK-m-F3.md at HEAD, `f674583` and `1e79955`, and of the driver at HEAD; `git rev-parse`; `shasum` of LOCK-m-F3.md and the working driver.
  - `grep` over named files only (including the glob `valence_core/mf3/*.py`).
  - Nothing else: no listing, no `git status`, nothing under data/ read, nothing written, staged or committed. jlens-qwen36/ untouched apart from running its venv's interpreter.
- **The clone:**
  - Made with the brief's no-checkout, sparse-checkout form. Its object store holds history's checkpoint and report blobs, as any clone does; none was checked out, opened or searched.
  - Run in it:
    - `git status --porcelain`;
    - `git apply` of the diff, then `checkout -- .`;
    - a pruned `find` over data/ (directories only);
    - name-only `ls` of data/mf3 and data/mf3/gates;
    - `git show | shasum` of data/mf3/gates/Q-F3_G-ID.json and data/mf3/schedules/manifest.json (digests only);
    - `git ls-tree --name-only` of the schedules.
  - Each self-test run hashed the clone's data/mf3 (schedules and gates only; it has no ckpt or reports).
  - The clone and its temp area are deleted. The work directory keeps the harness, the mutants and the run outputs.
- **Python:**
  - The venv's interpreter with `-B` and `HF_HUB_OFFLINE=1`.
  - The five model modules were blocked before the driver's import, and every run asserted they were still blocked at its end.
  - One harness process at a time, sequentially (checked with `pgrep` before each). The text-only mutant generator ran between runs.
  - Each run also spawned the self-test's own fresh-interpreter import check (`-I -B`, mf3's production modules, none of which imports a model library).
  - No model was loaded, and no stage or subcommand ran outside the self-test's traps.
- **Beyond the brief's harness:** I added the qual-only and driver-only screens to fit the time budget. Every screen survivor was confirmed with the full self-test.
- **Time:** about 1.5 hours, over the brief's hour, mostly in mutant runs. All 44 mutants and all 5 full confirmations completed.
