# The counters script's blind review, rounds 1 and 2, with Code's dispositions (Code; PI date 2026-11-16)

*The dpo VERDICTS session's counters script, `scripts/p_verdicts_counters.py`, reviewed blind before its commit in two rounds. Round 1 reviewed the script as at its first self-test (sha256 `f4ec08c30990f546005db54fa4c57fee9b04d1034ab4494c05daec9c806a9339`, self-test 23/23). Round 2 reviewed it as revised for round 1 (sha256 `a268701037823ed46528e661c0233d8c314328f6a914cae5ff44196c38db5b29`, self-test 35/35). Each reviewer was a fresh subagent with no part in the build, and round 2's saw round 1's findings only as its brief's short list of them, not the report. Each brief named the script, the seat's answers of 2026-11-16 (§3, §4), `valence_core/p/report.py`, `valence_core/p/stage.py` (from line 950), the task_correct raw, the seat's line 34 of 2026-11-09 and m's `readrule`, `scaffold`, `resume` and `corr`; round 1's also the joint block's §4, round 2's also `valence_core/p/corrupt.py`, `valence_core/p/guard.py`, LOCK-p-OLMo-dpo §8.1 and m's `runner_olmo`. Each bound its reviewer to the list of record v2, items 1–5 (quoted), and to the laptop's rules for Q-F3's campaign: no Python, nothing under `data/mf3`, no whole-tree `git status`, and nothing under `data/p/ckpt` or `data/p/verdicts` opened. Round 1's own account: "I edited nothing and ran no Python. My only shell actions were digests (shasum), greps of code and of the named raws, `git log`, and `git status --porcelain` scoped to explicit paths. I read nothing under data/." Round 2's: "I ran no Python and edited nothing. I did not open data/mf3, data/p/ckpt or data/p/verdicts." The reports are reproduced verbatim below, with one exception: in round 1's, one phrase naming the machine-path prefix is reworded as "an absolute machine path" (the raw-scrub rule). Code's dispositions follow each. Calendar dates only; the commit hash is the record.*

## Round 1: the report, verbatim

Review of scripts/p_verdicts_counters.py. I edited nothing and ran no Python. My only shell actions were digests (shasum), greps of code and of the named raws, `git log`, and `git status --porcelain` scoped to explicit paths. I read nothing under data/.

**MAJOR: none.** I found no way a printed count could come out wrong, no licence breach, and no §3 or §4 condition the code leaves unmet.

**MINOR**

1. **Some counts print before a STOP** (:527–562, and the unit loop). The sham task_correct check (:557–562) runs after that stage's p §2.3 block is printed (:531–556), and a STOP at a later checkpoint comes after earlier units were printed. Example: the dpo qual sham recount misses 63/64. Stdout already holds all of sft's counts and dpo's time and qual §2.3 blocks, the qual block from a record that has just failed its check. Fix: two passes. Load and check all nine (identity, sha binding, read domain, sham task_correct), then print.

2. **Exits outside the declared table.**
   - `read_checkpoint` raises a bare `SystemExit(str)` (resume.py:674, :558).
   - A missing checkpoint or p report raises FileNotFoundError (:511, :521).
   - task_correct's `CounterError`, `LexiconStop` and `CorrStop` are not caught either.
   - All of these exit 1, which the docstring reserves for "selftest FAIL", and the message carries an absolute machine path.
   - Fix: catch them in `run` and map each to exit 2 or 4 with a repo-relative path.

3. **"Unchanged" is not verified.** Only report.py's sha256 is printed (:499). The predicates also depend on `m.gcal.normalize`, `m.banner`, `p.corrupt.FUNCTION_WORDS` and `p.proxy.LINE_BREAKS`. The read-domain equality catches drift only where it touches the read domain. A change that moves only contrast-round tokens would pass. Fix:
   - assert `p.guard.package_sha256()` equals each p report's recorded `p_package_sha256` (stage.py:996);
   - assert `guard.m_module_sha256s()` equals LOCK-p v1.0's licence lines;
   - print both.

4. **Each checkpoint is read twice** (:511–512). The sha256 comes from the first read and the records from the second. Fix: parse `ck_bytes` once, or re-hash after `read_checkpoint` and assert the two are equal.

5. **The gate and the order are not enforced.**
   - Output existence does not mean "the third run has ended" (:283–286, docstring :48–49). A run that wrote VERDICTS and then raised, which §5 step 2 makes a STOP for the seat, still opens the gate.
   - `run` does not check the seat's "committed, with its self-test, before it reads any released record".
   - Fix: require an explicit statement of the three end notices' exit-0 statuses, and refuse unless the script's bytes equal HEAD's blob (`git hash-object` against `rev-parse`) and an in-process `run_selftest()` returns 0.

6. **A failing synthetic-cells check crashes the self-test** (:432–435, :366). `got_cells` has tuple keys, and `json.dumps(..., default=str)` raises TypeError on non-string keys (`default` does not apply to keys). That check's FAIL line is lost and the checks after it never run. Fix: key the cells as `f"{a} {ph}"`.

7. **`run()` itself is untested.** The self-test covers the shared functions but not `run`'s ordering, its binding and identity STOPs, or its prints. It also tests `checkpoint_paths`, which `run` never calls (:510 builds the paths inline). Fix: make the root a parameter, add a synthetic scratch-root case (including a sha mismatch and a read-domain mismatch), and have `run` iterate `checkpoint_paths()`.

**NOTE**

- `check_round` does not tie a corrupted round's task text to its item's render. The synthetic item-2 round carries item 12's render, "Cnmzote 11 + 33." (:355), and passes. The withheld contrast counts take their gold and key from `item`. m asserts this binding at schedule time (scaffold.py:605–606), so the risk is low.
- `bool(r["cap_hit"])` (:206) and the read-domain partition (:231–245) restate session_counters' inline code. They are identical and checked against the report, so no count can move. Calling `p_report.session_counters(records, pool)` and comparing it to `rep["counters"]` whole would remove the restatement.
- Self-test check (1) compares sham control-character texts from the reads files, where `redact_sham` has replaced own-pair labels in free texts (readrule.py:460, :481). A sham free round carrying both a control character and a label would FAIL even though nothing is wrong; the check fails safe.
- The self-test does not pin the six reads-file digests the raw prints (raw lines 12–14, 23–25).
- The domain is recorded rounds only:
  - G-VER-quarantined launches and interrupted sessions are never in a checkpoint (resume.py:607–610);
  - set-aside checkpoints lie outside the nine paths;
  - the entries should say "every recorded round".
- The listing-call source check (:472–474) covers this file only.

**Checked and correct**

- **Loading task_correct.py** (Q1):
  - the raw hashes to 57e9c7dc…;
  - lines 29 to EOF hash to 9aa0e2d9… (both by shasum), so the extraction boundary and trailing newline are right;
  - the header marker occurs once;
  - it runs under a module name that is not `__main__`, so `main` never runs;
  - the source has no import-time effects;
  - nothing is copied.
- **Tabulation** (Q2): the same predicates with the same arguments as report.py:277–300.
  - The pool is `m_corr.load_pool`, asserted equal to task_correct's.
  - `clean_task_words(pool)`, `pool[item]["gold"]` and the default pinned lexicon are used as session_counters uses them.
  - The hair trigger runs over every round.
  - The arm and phase split is right, and the printed withheld line matches WITHHELD's three parts.
- **Read-domain comparison** (Q3): it covers exactly the count cells session_counters writes. Both sides are sorted and compared as dicts, n = len(keys) is asserted, and the sham corrupted-spelling domain is the sham forced rounds. It cannot pass when the counts differ, and it fails only in the label edge case above.
- **Self-test** (Q4): it reproduces 63/64+96/96, 63/64+96/96 and 64/64+96/96, and G-TIME's 3/4+6/6, 4/4+6/6 and 4/4+6/6.
  - It does so both through the imported `tally_file` and through `tc_rows`, with the alternative reading compared too.
  - It reads only the raw, the pools file, the lexicon, the reads files, the time and qual p reports, its own source and a temp directory.
- **The synthetic cases**, worked by hand with `normalize`:
  - Of the nine texts, only `Januwy` counts for corrupted_spelling (distance 2 to `january`).
  - `Cold.`, `Seven`, `March`, `Shut`, `twenty four` and `i m`/`can t` (by their parts) are excluded by the lexicon; `12` is too far from `two` (distance 3, threshold 1); `\x07` and `\x7f` normalize to nothing.
  - The control characters are `\x07` and `\x7f`, but not `\r`, which is the one line break.
  - The cells, the hair trigger, the control-character keys and every task_correct expectation are right ([1,2], [2,3], [2,2], [0,2]).
  - All four mutations STOP.
- **Run mode** (Q5):
  - The gate is checked before any checkpoint read.
  - The nine exact paths match `out_paths` (stage.py:673; stages.py:224), and nothing is listed.
  - Each checkpoint is bound to its report's `checkpoint.sha256` (stage.py:985) and to the unit, and a mismatch STOPs before that stage prints.
  - It prints only counts, keys, digests, readings and control-character texts. `json.dumps` escapes `\x07` and `\x7f`.
- **Readings** (Q6): the code does what R1 and R2 say. task_correct runs on time and qual only, the sham rows are rechecked, and the campaign is skipped. No call log is read.
- **Files the script cites:** the ruling digest 01ae2ae7… matches, and `valence_core/p` and `valence_core/m` are clean.

## Round 1: Code's dispositions

Each MINOR is applied in the revised script; each NOTE is applied or answered. The revised script's self-test (run 2) is in the self-test raw.

| Finding | Disposition |
|---|---|
| MINOR 1, counts printed before a STOP | Applied: two passes. `collect` reads and checks all nine checkpoints, printing nothing; `emit` prints only after every check has passed. Self-test case: five mutations (a report not recording its checkpoint's sha256, a differing read-domain cell, a checkpoint naming another stage, a sham `task_correct` row off its figure, a campaign report from another p package) each STOP with nothing printed. |
| MINOR 2, exits outside the declared table | Applied: `main` maps any other `SystemExit` (m's reader, task_correct's `CounterError`, the lexicon's and the pool's stops) and any `OSError` to exit 2, and any other exception to exit 4, each message with repository paths made relative to the root. |
| MINOR 3, "unchanged" not verified | Applied, in another form than the one proposed. p's `package_sha256` and m's are asserted equal to the values every LOCK-p v1.0 names (`a38d93bb…`, `7756dcf4…`; the lock names m's beside its per-module licence lines), as `run`'s gate 3 and as a self-test check. The campaign's p report must record the lock's p package. Not each report's: the gate stages' reports were built by the p packages in force at their stages, which the locks' earlier versions name, so the run prints each report's recorded package beside it rather than asserting it. |
| MINOR 4, each checkpoint read twice | Applied: the bytes are hashed before and after m's `read_checkpoint`; a difference STOPs. |
| MINOR 5, the gate and the order not enforced | Applied: `run` takes the three end notices' exit statuses (`--exit UNIT=STATUS`, each required and each 0; gate 1), then the outputs' existence (gate 2), the packages (gate 3), this script's bytes equal to its blob at HEAD (gate 4) and the self-test in the same process (gate 5), before any checkpoint is read. Self-test cases for gate 1 (a missing status; a status of 2) and gate 2. |
| MINOR 6, a failing synthetic check crashes | Applied: the cells are keyed by strings. |
| MINOR 7, `run` untested | Applied: `run`'s two passes are `collect` and `emit`, with the root and the reader as parameters; `run` iterates `checkpoint_paths`. Self-test: nine synthetic checkpoints and their p reports (built by p's own `session_counters`) in a scratch directory, the good case printed into a captured buffer and checked, and the five STOP cases above. |
| NOTE, corrupted task text not tied to its item's render | Applied: `check_round` requires a corrupted round's task text to be its item's render of record (`p.corrupt.RENDERS_OF_RECORD`, whose sha256 the self-test checks). The synthetic corrupted round now carries item 2's render; a mutation to item 12's render STOPs. |
| NOTE, the read-domain partition restates `session_counters` | Applied: `collect` also runs p's own `session_counters` over the released records and asserts its read-domain cells equal the committed report's, beside this step's table (kept, for the withheld cells). The self-test asserts the two agree on the synthetic records, where each read-domain arm and phase has a hit (the sham harness-line and refusal counters have none). |
| NOTE, the redaction edge case in self-test check (1) | Answered: it fails safe (a FAIL with nothing wrong), and no sham free round in the six reads files carries a control character (the committed reports' sham counts are 0 except sft's qual cap hit). Unchanged. |
| NOTE, the reads files' digests not pinned | Applied: the six digests the task_correct raw printed are pinned (`READS_SHA256`) and checked in the self-test before each file is used. |
| NOTE, the domain is recorded rounds only | Applied in the wording: the script says "recorded rounds" and "recorded sessions"; the entries will say so. |
| NOTE, the listing-call check covers this file only | Answered: as declared; the imported modules are m's and p's, unchanged. |

## Round 2: the report, verbatim

Round-2 review of scripts/p_verdicts_counters.py (sha256 a2687010…5b29, untracked). I ran no Python and edited nothing. I did not open data/mf3, data/p/ckpt or data/p/verdicts.

**MAJOR: none.** I found no path that gives a wrong count, breaches a licence, or leaves the seat's §3/§4 condition unmet.

**MINOR 1. main :816–818: after the gates, a failure is called a refusal.** Every SystemExit other than Stop, and every OSError, exits 2 "REFUSED". That includes failures inside `collect`, after all five gates have passed and released records have been read. Examples:
- m's `read_checkpoint` raises a bare SystemExit for "CHECKPOINT STATE INCONSISTENT" or "UNREADABLE" (resume.py:558, 674–678).
- A missing checkpoint (:362) or p report (:375) raises FileNotFoundError.

Scenario: the instruct campaign checkpoint fails m's `_check_state` after eight checkpoints have been read. The output is "REFUSED: SystemExit: CHECKPOINT STATE INCONSISTENT…", exit 2. That reads as "a gate closed, nothing read". The script's own exit table calls a record that is not as the rule reads it a STOP (4). Fix: once gate 5 passes, wrap `collect` so that any exception other than Stop is re-raised as Stop.

**MINOR 2. run :473: an error inside the gate-5 self-test is not contained.** `run` only tests the self-test's return value. A Stop raised by the self-test's unguarded calls escapes `run` (the `check_round` loop at :639–641, the synthetic `collect` at :713). `collect` builds `rel`/`rrel` from the repository templates whatever root it is given (:361, :374). So `main` prints, for example, "STOP: OLMo-sft time: … data/p/reports/OLMo-sft_time_p-report.json" with exit 4. That cannot be told apart from a STOP on the released record, though no checkpoint was read. In `--selftest` mode the same failure exits 4 or 2, not 1. Fix: turn exceptions in the self-test body into FAILs, or wrap the gate-5 call so it raises "REFUSED (gate 5)". Also have `collect` name its paths relative to the root it was given.

**NOTEs**
1. Test coverage:
   - The step-table STOP (:384–388) is never exercised: `bad_cell` trips the `session_counters` comparison at :382–383 first.
   - The synthetic reader bypasses `read_checkpoint`, so MINOR 1's path is untested.
   - The check at :718 says each stage prints "its withheld cells", but nothing asserts that line.
   - Gates 3–5 are never exercised through `run`.
2. Docstring accuracy. :52 says `run` reads "nothing until five gates pass". In fact `run` reads the task_correct raw, the pools file and the lexicon before gate 1 (:449–452), and gate 5 reads the time/qual p reports and reads files. All of these are licensed. :59–62 "before anything is printed" should say "before any count is printed".
3. In the self-test, `p23_table` over the reads-file records (:627) computes the withheld sham-free corrupted-spelling cell in memory. It uses items taken from the redacted Task lines, and it ran before VERDICTS. It is never printed. Restrict that table to the cells being compared.
4. Each checkpoint is now read three times (:362–364), and the parsed bytes are not the hashed bytes. The stability check is adequate, but it multiplies reads of pick-bearing files.
5. Output ordering. `run` and `emit` print without flushing, while `chk` and stderr flush. If the raw is captured with stderr merged into stdout, a STOP line lands before the imports/readings lines. Flush before `collect`.
6. A G-VER STOP's record is quarantined in `stop`, never in `sessions` (m stages.py:2269, 2308). Neither p's reports nor this step tabulates it. If any campaign stopped on G-VER, the entry should say so.
7. The "no directory-listing call" self-check (:774–776) holds for the script's source text. The process itself still lists a scratch directory (`shutil.rmtree`) and the package directories (`package_sha256`'s glob). Nothing under data/p/ckpt is listed.
8. `_scrub`: REPO is already resolved, so the set has one element (harmless). Temp-directory paths and KeyboardInterrupt tracebacks are not scrubbed.
9. Reading R1 omits the seat's "from G-F0m-OLMo (p) on" (gtime answers :34). That phrase bears on both G-TIME's contrast row and the campaign, so R1 should quote it.

**Checked and correct**
- **A (round-1 fixes):**
  - `collect` prints nothing, and `emit` runs only after all nine checkpoints pass.
  - The gates run in order, and gate 1 comes before gate 2's existence check.
  - The self-test's nested `run()` calls refuse at gate 1, so there is no recursion and no checkpoint read.
  - No GOT value carries tuple keys. `_scrub` maps repository paths correctly.
  - A self-test FAIL never exits 0.
- **B (read-domain cross-check):** sound. A correct checkpoint passes it.
  - report.py and proxy.py last changed at d215d5b, and corrupt.py at a665a09.
  - The later p commits (e8779b1, 40086e8, c0f1c69) touched only identity.py, register.py and stage.py.
  - m's package has not changed since 993eba1, and the lexicon and pools are unchanged.
  - The gate-stage reports were built after d215d5b, each by the package that ran its stage (stage.py:959–963).
  - `release_full` returns its input unchanged (readrule.py:799–805).
  - `read_checkpoint` and `build_report` parse the same JSON (resume.py:670–684; stage.py:924–925, 964–966).
  - Nothing writes a checkpoint after its p report: the gate and campaign runs refuse once the p report exists, and the analyzer writes none.
- **C (corrupted rounds):**
  - "Corrupted" means a contrast session's role-Q rounds, forced and free (corr.py:395–405).
  - Their task text is `renders[i]`. Under register entry (1), which every p stage enters (register_entered; identity renders_sha256_p), those renders equal `RENDERS_OF_RECORD`, and G-VER checked them.
  - Clean rounds carry the pool's task text. `check_round` cannot STOP a correct record.
- **D (synthetic cases), worked by hand:**
  - All nine synthetic rounds give the cells claimed.
  - For `### Response: March \x1b`: ESC is category Cc, so it is a control character; the first line starts `### Response:`; task_correct's tokens are [response, march], which match the key `march`.
  - `normalize` blanks \x07, \x1b and \x7f.
  - `Januwy` is the only spelling hit (distance 2 from `january`). `Seven\r` is the only line break.
  - task_correct rows: sham 1/2 forced and 2/3 free; contrast 2/2 forced and 0/2 free.
  - All ten mutations (five in `check_round`, five in `collect`) STOP for the reason their names give.
- **Pins:** these all match their committed sources: the task_correct raw's sha and the embedded script's sha, the six reads-file digests, the six committed sham figures, and the package values in all three locks (§8.1).
- **Sham recount on released texts:** it equals the committed figures, which were computed on the redacted reads files. `redact_sham` replaces only whole `\b`-delimited tags, and no roster tag is a key or a number word.

## Round 2: Code's dispositions

Both MINORs are applied; each NOTE is applied or answered. The script as committed is the one round 2's fixes produced, and its self-test of record is in the self-test raw.

| Finding | Disposition |
|---|---|
| MINOR 1, after the gates a failure is called a refusal | Applied: `run` passes pass 1 through `collect_guarded`, which re-raises any exception other than a STOP -- m's reader's own refusal, a missing file, anything else -- as a STOP (exit 4). Self-test case: a reader that refuses and a reader whose file is missing each give a STOP. |
| MINOR 2, an error inside the gate-5 self-test not contained | Applied: the self-test's body runs inside `run_selftest`, which turns any exception into a FAIL (exit 1 under `--selftest`; gate 5 closed under `run`), and `run` wraps the call as a backstop ("REFUSED (gate 5)"). `collect` names its paths relative to the root it is given. |
| NOTE 1, test coverage | Applied in part. The step-table branch is exercised: with this step's view altered by one round, pass 1 STOPs on "this step's read-domain cells differ" with nothing printed. The guarded pass 1 is exercised (MINOR 1's case). The withheld-cells line is asserted for all nine stages. Gates 3–5 are not driven through `run`, since gate 2 opens only on the repository's own outputs, which exist only after the third run; gate 3's check runs in the self-test, and gates 4 and 5 are checked by the run itself. |
| NOTE 2, docstring accuracy | Applied: the docstring says what `run` reads before gate 1 and in gate 5, and "before any count is printed". |
| NOTE 3, a withheld cell computed in memory in the self-test | Applied: the reads-file comparison now runs p's own `session_counters`, which computes only the read domain (its corrupted-spelling counter on the sham forced rounds); this step's table is checked against `session_counters` on the synthetic records only. `task_correct` over the sham rounds, free included, stays: it is the counter task_correct.py's own run read from the same files. |
| NOTE 4, three reads | Applied: two reads. m's reader parses the checkpoint; its bytes are then read and hashed, and the parsed content is asserted equal to the bytes hashed (m's `_check_state` mutates nothing). |
| NOTE 5, output ordering | Applied: every line `run` and `emit` print is flushed. |
| NOTE 6, G-VER-quarantined records | Answered: no p stage stopped. The gate stages ended PASS (the G-TIME-OLMo (p) ×3 and G-F0m-OLMo (p) ×3 entries) and the campaigns COMPLETE with no pause and no STOP (the campaigns' entry, `41bfab4`), so no record is quarantined. The entries say "every recorded round". |
| NOTE 7, the listing check's scope | Applied in the check's wording. The script's source makes none of the six listing calls the check names; the script lists only its scratch directory (`TemporaryDirectory`, `shutil.rmtree`), and the package hashes list their own package directories; nothing under `data/p/ckpt` is listed. |
| NOTE 8, `_scrub` | Answered: harmless, as noted. No line a passing run prints names a temporary directory. |
| NOTE 9, R1 omits "from G-F0m-OLMo (p) on" | Applied: the docstring, `READING_R1` and the block quote it, and the block's R1 sets out its bearing on G-TIME's contrast row and on the campaign. |
