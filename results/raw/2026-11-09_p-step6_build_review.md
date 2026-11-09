# PROPOSAL-p step 6 -- the BUILD's blind reviews (Code's reviewers, rounds 1-5)

*Code's raw, PI date 2026-11-09. Five blind reviews of the uncommitted step-6 build: the stage driver
(`valence_core/p/stage.py`), p's analyzer (`scripts/p_analyze.py`, `valence_core/p/analysis.py`), G-ANL-p's groups,
register entries (3) and (6)-(9), and the `daca8b0` rulings. Each reviewer read the build against the seat's answers
(`de729c4`), PROPOSAL-p v0.2 and PROPOSAL-m v1.11, and ran its own experiments in scratch roots, editing no repository
file. Each report is verbatim, with local paths scrubbed (`<repo>`, `<tmp>`) and its headings set one level down under
its round's heading; a quoted line separator (U+2028) is written `<U+2028>`. Code applied or answered every finding
before the next round, and round 5's before the commit; the BUILD entry states how.*

## Round 1

### Blind review: PROPOSAL-p step 6 (uncommitted build)

I edited no file in the repository. Every experiment ran from scripts and temporary roots under `<tmp>/scratchpad/podwatch/rev/`. `git status` was identical before and after every run.

#### MAJOR

**1. A register site re-enters inside the stage after the model load, so a live library thread STOPs the stage.**
- **Where:** `valence_core/p/schedule.py:117-120`, then `:59`, then `valence_core/p/keys.py:65`, then `register.py:173`. It is reached from m's `load_committed` (`valence_core/m/stages.py:904`, called at `:1475`), which runs after the factory at `stage.py:261`.
- **What:** entry (7)'s replacement regenerates p's schedules through `keys.substituted_keys()`, which calls `register.substituted(2)` and so `assert_single_threaded` again. This contradicts the seat's Q4 ("a library thread alive after the load ... does not offend the term ... recorded, never raised"). It also contradicts the register's own PIN (`register.py:21-23`, `:29-31`) and `stage.py:22-23`. It is the same defect class as the BUILD review's R2-1.
- **Scenario (experiment A):** a factory that leaves one Python thread alive produced `RegisterStop: register entry (2) runs only in single-threaded stage code (term (d)); 2 threads alive`. The stage stopped before any session. On the box that means a wasted cold load, exit 4, and a code fix that moves the p package, so G-SHAPE-p re-runs and all three locks are re-issued.
- **Fix:**
  - Don't re-enter the register when entry (2) is already in force: build directly when `m_keys.<fn> is keys.<fn>`.
  - Or compute the expected blobs before the load and have the replacement compare against them. Verifying `data/p/schedules` in the precheck also fails fast.
  - Add a self-test case where the factory leaves a thread alive.

**2. Blinding: the p report and stdout reveal the contrast session's free-round count, which is the free-round exclusion position.**
- **Where:** `stage.py:274`, `:284-286`, `:314`. Read against `report.py:279` (`n_sham_rounds`) and `:294` (`n_forced_rounds`).
- **What:** `proxy.n_generate` counts every `generate` call, one per round, contrast free rounds included. So n_generate − sham rounds − contrast forced rounds = the contrast free rounds generated. m withholds exactly this: `readrule.py:13-15` ("Whole-session validity, completeness and seconds go too, because each one encodes the free-round exclusion position"), `stages.py:1327-1333`, m:271, m:318. It also contradicts `report.WITHHELD` (`report.py:249`, "every count over a contrast free round"). `n_cuts` likewise counts contrast free-round events.
- **Scenario (experiment B):** with a lexical claim planted at contrast free round ci=1, m prints only `excluded:excluded@free`. p prints `P-REPORT proxy: 16 calls` (20 with no exclusion), and the arithmetic gives 2, equal to the checkpoint's 2 free rounds. The report is committed under `data/p/reports`.
- **Fix:**
  - Report proxy counts only over the sham session and the contrast forced rounds.
  - Move the totals and `n_cuts` into the withheld cut log under `ckpt/`.
  - Add a self-test that the report and summary lines don't change with a contrast free-round exclusion's position.

**3. The cut log and p's report are lost on any exception or tail failure, and cannot be re-derived.**
- **Where:**
  - `stage.py:259-294`: the cut log is held in memory and written only after a clean return.
  - The precheck (`stage.py:172-213`) never loads the lexicon, and `gcal.committed_problems` (`gcal.py:170-180`) doesn't cover it.
  - A `ProxyStop` carries `returned_text`, which is never printed or recorded (`p_sessions.py:243-245`).
- **Scenario (experiment G):** with the lexicon absent, m persisted `stage_end PASS`, then `LexiconStop` was raised. No p report and no cut log were written. Re-runs, with and without `--resume`, were refused by m with "STAGE ENDED", so the cut log is gone for good.
  - The same loss follows any `ProxyStop` (the §2.3 trigger itself) or any other m `SystemExit`.
  - On `--resume`, the counts and the cut log cover only the resumed process, with no mark that they are partial.
  - Q4's "a failure there is recorded in the entry" cannot happen on these paths.
- **Fix:**
  - Load and commit-check the lexicon in the precheck; consider `-text` in `.gitattributes`.
  - Write each cut ahead to a file under `ckpt/` (or in the `finally`, with `ProxyStop.returned_text`).
  - Add a command that re-derives p's report from the checkpoint and cut log.
  - Mark resumed counts as partial.

**4. Entry (7)'s declared term (c) self-test is missing and, as built, cannot pass.**
- **Where:** `schedule.py:117-126` and its `_selftest`. The requirement is the seat's Q2 (`2026-11-08_p-step6_design-to-code_answers.md:8`): "with m's keys and root substituted back it reproduces m's verifier's verdict on `data/m/schedules`".
- **What:** no such case exists anywhere. p's verifier has no keys switch and regenerates only p's 18 files and p's manifest.
- **Scenario (snippet):** m's verifier on `data/m/schedules` returns `[]`. p's logic with m's keys returns 8 problems: `manifest.json` differs, plus 7 Q-F0 files reported as unlisted.
- **Fix:** parameterize p's verifier by keys and root so that with m's it regenerates m's file set and manifest, then add the case.

**5. G-ANL-p never runs p's VERDICTS path, and its Q-F0 "regression" compares m's outputs with themselves.**
- **Where:** `scripts/p_analyze.py:120-141`, `:131`, `:162-200`, `:241-378`. The requirement is the seat's Q8: "p's own groups run m's verdicts, not-run and posting functions under entry (3)".
- **What:**
  - `run_verdicts_p` is called only from `main()`; no group runs `run_verdicts` under entry (3).
  - `_regression_qf0` calls `m_analyze.run_verdicts` directly inside `run_staged(block=None)` (`:189-192`), so the only p code it tests is a byte copy.
  - It is a restatement of m's `_bt_qf0_regression` that drops m's PIN-29 pins, the lock-names-all-three check and the preprint-blob sha check.
  - `run_verdicts_p` cannot run Q-F0 at all: it hard-codes `olmo_states`, `sentences` and `flag_source` to None, and `inputs_extra` duplicates every field, so any key raises `TypeError`.
- **Scenario:** a defect in `run_verdicts_p` (default paths, argument plumbing, the p block on VERDICTS and secondary) first shows up at the campaign's VERDICTS of record.
- **Fix:**
  - Add a p-form VERDICTS group on a synthetic OLMo campaign (m's `_Camp`), compared with m's form minus the two added keys.
  - Route the Q-F0 regression through `run_verdicts_p` with `p_mode=False`, fixing `inputs_extra` via `dataclasses.replace`.

**6. p_analyze's outputs are not bound to p's code.**
- **Where:** `p_analyze.py:67-78`, `:81-83`; `analysis.py:124-133`; m's V1 at `m_analyze.py:2268-2278`.
- **What:** `valence_core/p/analysis.py` holds entry (3)'s replacements, `D_P`, `run_staged` and the p block, yet:
  - not-run, verdicts and posting never commit-check `valence_core/p/*.py` (only `ganl` adds `gcal.committed_problems`);
  - no output records p's `package_sha256` (experiment D: absent);
  - nothing checks `p_analyze.py` or p's package against the lock. m's PIN-14 checks only m's analyzer, package and closure, and m's closure is computed for `m_analyze` alone (`m_analyze.py:1830-1841`).
- **Scenario:** after LOCK-p v1.0, an uncommitted edit to `analysis.py` (`D_P`, `crosscheck_coordinate_p`) writes VERDICTS of record. Every check passes, and the output cannot reveal it.
- **Fix:**
  - Add `guard.package_sha256()` to `analyzer_blobs()` and the p block.
  - Require p's package committed in `binding_problems`.
  - On verdicts, require the lock to name `p_analyze.py`'s sha256 and p's `package_sha256`.

#### MINOR

**7. D_p's check is decoupled from the value in use** (`analysis.py:33-35`, `:62`, `:71-81`).
- `d_p_problems` tests the literal `D_P_SENTENCE`, while `clock_of_record_p` returns the separate `D_P`.
- Snippet: with `D_P = "2026-12-31"`, `d_p_problems()` still returns `[]`.
- Fix: build the sentence from `D_P`, or parse `D_P` from the committed line.

**8. `lock_required` omits values a lock must name, and holds one unstable value** (`stage.py:122-152`, `:65`, `:263-266`).
- Omitted:
  - the schedules (p's manifest sha256 or the identity's `schedule_sha256`; m:302 "that checkpoint's schedules"; `hashes` prints the manifest sha but nothing requires it);
  - PROPOSAL-p's sha256 (F-p8, "locks' identity blocks") and PROPOSAL-m's;
  - the covariate (seat's §4, m:302);
  - the banner sha and ban-list sha16 (m:302).
- Unstable: `BACKEND_OF_RECORD` is a code constant. Any box change, even before the lock (which the seat's §4 called free), forces an edit that moves the package and so a re-lock. That is contrary to m:302's "under its existing lock".
- Fix: add the missing values, and read the backend identifier from the lock or the newest BACKEND record.

**9. The precheck accepts superseded or stale gate artifacts** (`stage.py:104-119`).
- It checks only `verdict == PASS`, never the recorded package shas. G-ANL-p's artifact (`p_analyze.py:412-419`) records no p package at all.
- Concrete today: `data/p/gates/G-SHAPE-p.json` is 5009e77's artifact (p package `717958da…`, current `22851727…`), which F-p12 ruled superseded. `lock_required` lists its sha (`3fb0f640…`), and a lock naming it would pass.
- Fix: compare the recorded package and analyzer shas with the current ones.

**10. The p report's `register` field is wrong** (`stage.py:287-288`).
- It records `[1, 2, 3, 6, 7, 8]` (experiment B): entry (3) was never entered at the stage, and entry (9), which was entered, is omitted.
- Fix: record the entries `stage_substitutions` actually entered.

**11. The v2 posting records absolute machine paths** (`p_analyze.py:148-150`).
- Q-F0 and Q-F3 are recorded as `<repo>/data/m/verdicts` and `<repo>/data/mf3/verdicts` (experiment F), in a committed output of a public repository, while the OLMo entries are repo-relative.
- The cross-check uses the bound `m_verdicts`, not the argument, so the two can disagree.
- Fix: record repo-relative paths, and refuse an argument that differs from the bound directory.

**12. Term (e)'s static check is blind to `m_analyze`** (`guard.py:257-280`).
- A planted `import m_analyze; m_analyze.clock_of_record = None` gives `[]`; the `valence_core.m` control is flagged.
- Fix: track `import m_analyze` as an m import, and add the planted case.

**13. `run_staged`'s seeding is never exercised, and it changes m's re-run semantics** (`analysis.py:159-162`).
- Every G-ANL-p case runs into an empty or absent final directory, so the reason for the seat's Q7 seeding (exclusivity, and the posted re-run's comparator) is untested.
- Experiment D: a p re-run on unchanged inputs is refused ("exists with different bytes -- write-once", exit 2), while m's own re-run reports "identical" (PIN-37). STAGING_NOTE doesn't say so.
- Fix: add the seeded cases, and document or handle the re-run.

**14. p_analyze's CLI doesn't resolve path arguments against the repository** (`p_analyze.py:410`, `:474-483`).
- m does, via `_cli_path` (PIN-V2-8). From another directory, `not-run --record x.json` reads `CWD/x.json`; m commit-checks no record.
- Fix: use `m_analyze._cli_path`.

#### NOTE

- **N1. Entry (9)'s refusal test cannot fail** (`register.py:246`). `{"Identity": None}` would be refused as a wrong replacement even if entry (9) were built, so the case cannot fail for the pending property. Pass `identity.identity_p` and assert the PENDING message.
- **N2. `run_time` trusts any precheck** (`stage.py:244-246`). With `stub=False` it accepts any `pre` naming the unit, including a `precheck(stub=True)` result. The driver never does this, but `pre` should carry its stub flag.
- **N3. The Q9 (b) sentinel case is weak** (`p_analyze.py:287-304`). It proves only that the sentinels never reach the output; a read that tolerates absence (the v2-closure `canon_.exists()`) passes, and it covers not-run only. Use a sentinel that raises on use, under all three commands.
- **N4. The NOT-RUN regression is partly self-referential** (`p_analyze.py:215-221`). It feeds back package and closure values read from the outputs under comparison, checked only by 8-hex prefixes. Pin the full values.
- **N5. Two Code readings should go to the seat.** `contrast_forced_control_chars` (`report.py:292-294`, `stage.py:311-312`) is a class field with forced-round positions, which ruling (h) keeps out of m's G-TIME report, though the read's texts show the same. `session_counters` also narrows Q5's "over the checkpoint" to the sham domain. Flag both in the BUILD entry.
- **N6. p's own refusals exit 4.** `AnalysisRefusal` and p's write-once `GuardStop` exit 4 through `_exit_of` (the docstring promises m's codes). m's "STAGE ENDED" refusal surfaces from `time` as "STOP", exit 4.
- **N7. A test binding is not restored in a `finally`.** The `analysis.bind(...)` rebinding in `_selftest` (`p_analyze.py:264`, `:368`) is restored outside a `finally`.
- **N8. Duplicate constant.** `identity.PROPOSAL_P_SHA256` duplicates `gcal.PROPOSAL_P_SHA256`, with no equality assert.
- **N9. Schedules are verified only after the load.** A dirty `data/p/schedules` wastes a cold load.
- **N10. `run_staged` checks too little.** It copies whatever m reports as written by name, without asserting the file lies in staging. `map_staging_paths` maps neither dict keys nor mid-string paths.
- **N11. G-ANL-p has no write snapshot for `data/p`.** m's battery has PIN-29's for `data/m` and `data/mf3`.
- **N12. m's stage report and reads lack p's sha.** Those written under `data/p/reports` carry no `proposal_p_sha256` (F-p8, "every p artifact"), and p's report doesn't name them.

#### Checked and sound
- Entry (9) is refused in production before the factory runs (experiment C: `RegisterStop`, zero factory calls).
- Every seam (`admit_9`, `olmo_stub_startup`, the identity hand patch, the sentinel patch) restores. The sentinel patch is reachable only through `ganl`'s battery.
- The outer entry order and the renders-cache assertion hold. The driver's imports and the precheck leave the cache empty and one thread alive.
- The identity wrapper is correct for `_validated` and for non-OLMo identities, and adds exactly p's four fields.
- Stub and test roots inside the repository are refused.
- The lexicon matches its pin (`be41ad97…`, byte-identical to `/usr/share/dict/web2`) and is admitted with `-diff`.

#### Counts
MAJOR 6, MINOR 8, NOTE 12.

#### Commands run
1. `git status --short`, `git diff --stat`, `git diff` (register, proxy, report, `p_sessions`, `.gitignore`, `.gitattributes`), `git log`.
2. `nice -n 19 jlens-qwen36/.venv/bin/python -B scripts/p_sessions.py --selftest`: 138/138 pass, exit 0, 14 s; tree unchanged.
3. `nice -n 19 jlens-qwen36/.venv/bin/python -B scripts/p_analyze.py --selftest`: m's battery 525/525 (538 coverage ids), G-ANL-p 9/9, exit 0, 2 min 47 s; tree unchanged.
4. `exp_stage.py` (scratch roots) gave three results:
   - A: `RegisterStop` at entry (2) with a thread alive.
   - B: 20 vs 16 calls; derived contrast free rounds equal the actual ones (6 and 2); register field `[1,2,3,6,7,8]`.
   - C: production refusal at entry (9) before the factory; all attributes restored.
5. `exp_tail.py`: `LexiconStop` after m persisted PASS; no report or cut log; both re-runs refused with "STAGE ENDED".
6. `exp_analyze.py`: the p re-run is refused (exit 2) while m's direct re-run is "identical"; no p package sha in the output; the resolution has absolute paths.
7. In-memory snippets:
   - mutating `D_P` leaves `d_p_problems() == []`;
   - p's verifier logic with m's keys finds 8 problems on `data/m/schedules` where m's finds `[]`;
   - the planted `m_analyze` write is not flagged (control flagged);
   - listed `lock_required('OLMo-sft')`;
   - the driver import plus stub precheck leave the cache at 0 and 1 thread;
   - checked the lexicon's sha256, ignore rule and attributes;
   - checked G-SHAPE-p's recorded package sha.

## Round 2

### Blind review, round 2: PROPOSAL-p step 6 (uncommitted build)

I edited no file in the repository. Every experiment ran from scripts and scratch roots under `<tmp>/scratchpad/podwatch/rev2/`; each script's output is saved beside it as `out_*.json`. `git status --short` was identical at the start, after every run and at the end (HEAD `2018ffc`).

**Self-tests:**
- `scripts/p_sessions.py --selftest`: 157/157 (the brief said 156), exit 0, 18 s.
- `scripts/p_analyze.py --selftest`: m's battery 525/525 (538 coverage ids), then G-ANL-p 13/13, exit 0, 2 min 47 s.

#### Round-1 findings

| # | Verdict | Evidence |
|---|---|---|
| MAJOR 1 (register re-entered after the load) | Fixed | `keys.keys_context` uses the entry (2) the stage holds (keys.py:69-89), and the schedule builder takes it (schedule.py:80). The self-test's case with a thread started in the factory passes. A thread alive before the run is refused by the precheck before the load (exp_edges 1: RegisterStop, no factory call). |
| MAJOR 2 (free-round count in p's report and stdout) | Fixed | The report holds proxy figures for the sham session only; the totals moved to the call log's end line. exp_blind: an exclusion planted at each of contrast ci 0-5, or a contrast free-round cut, leaves p's report and closing lines identical apart from the sha256s. A contrast forced-round exclusion changes only `n_forced_rounds`, which is ruling (h)'s count. |
| MAJOR 3 (cut log and report lost) | Fixed, new defects in the fix | All of these now work (exp_timereport; self-test): the write-ahead call log (stage.py:367-389), the lexicon in the precheck, `time-report`, and a report rebuilt from the whole log. New defects: the log is gitignored (M-2); a resume after a ProxyStop is unguarded (M-1); a torn line drops the next run's line (m-1). |
| MAJOR 4 (entry (7) term (c) test) | Fixed | `verify_schedule_dir(form="m")` returns m's verdict on `data/m/schedules`, on the self-test's 4 tampered copies and on 6 more (exp_pin). |
| MAJOR 5 (G-ANL-p never runs p's VERDICTS path) | Fixed | A p-form VERDICTS on a synthetic OLMo-sft campaign is compared with m's form (p_analyze.py:301-334, :456-489). The Q-F0 regression now runs through `run_verdicts_p` (`dataclasses.replace`), with m's PIN-29, identity and preprint checks taken from `_bt_qf0_regression`. |
| MAJOR 6 (outputs not bound to p's code) | Fixed | The p block names both analyzers and p's `package_sha256`. `binding_problems` requires p's package and both drivers committed. VERDICTS requires the lock to name p's analyzer and package (p_analyze.py:155-166). One gap remains: G-ANL-p's own record can drift (m-4). |
| MINOR 7 (D_p check decoupled) | Fixed | The sentence is built from `D_P` at call time, and a moved `D_P` fails the check (analysis.py:75-91; self-test). |
| MINOR 8 (lock_required gaps, backend constant) | Fixed, one reading open | Now required: schedules (manifest and per file), both proposals, the covariate, the banner parts, the ban list, the scaffold set, the driver, the licence lines and the register (exp_precheck). The backend comes from the lock's single BACKEND line. A box change therefore forces a lock edit, where m:302 has a superseding BACKEND entry under the existing lock; the PIN declares this as the seat's to route. Values are matched as substrings (N-4). |
| MINOR 9 (stale gate artifacts accepted) | Partly fixed | Package and analyzer shas are compared (stage.py:183-188, :218-226). G-SHAPE-p's sources map and import closure are not (m-3). |
| MINOR 10 (register field wrong) | Fixed | `register_entered` comes from the run lines: [1, 2, 6, 7, 8, 9] (exp_timereport). |
| MINOR 11 (absolute paths in the resolution) | Fixed | Paths are repo-relative or "(a test directory)", and an m directory other than the bound one is refused (p_analyze.py:199-201). |
| MINOR 12 (static check blind to m_analyze) | Fixed | `M_SCRIPT_MODULES` (guard.py:259-282); the three planted forms are caught (self-test). |
| MINOR 13 (seeding untested, re-run semantics changed) | Fixed | Tested: seeded exclusivity, the posted re-run's comparator and the refused p re-run. STAGING_NOTE records the change. The refusal's wording is misleading (N-9). |
| MINOR 14 (CLI paths unresolved) | Fixed | `main` uses `m_analyze._cli_path` throughout (p_analyze.py:701-713). |
| N1 | Fixed | Entry (9) is refused with its declared replacement, and the PENDING message is asserted (register.py:252-263). |
| N2 | Fixed | `run_time` refuses a precheck whose stub flag differs from the run's (stage.py:520-522; self-test). |
| N3 | Fixed | The sentinels record and raise on use under not-run, verdicts and posting. Only `repr` and `is` pass silently (exp_analyze2), and m's code uses neither on p's paths. The v2-closure branch is still not exercised (N-8). |
| N4 | Fixed | The three NOT-RUN bindings are pinned in full and checked against each output (p_analyze.py:69-72, :270). |
| N5 (contrast forced-round control chars; Q5 narrowed) | Not fixed | The code is unchanged (report.py:293-294, stage.py:608). No PIN flags the tension with ruling (h) ("no class and no round position") for the seat. |
| N6 | Fixed | p's own refusals exit 2 (`P_REFUSALS`). An ended stage is now refused by p, with exit 2, before m runs. |
| N7 | Fixed | The production binding is restored in a `finally` (p_analyze.py:585). |
| N8 | Fixed | The self-test asserts the two `PROPOSAL_P_SHA256` constants are equal. |
| N9 | Fixed | Schedules are verified before the load (stage.py:543-546); on a dirty root the factory is never called (self-test). |
| N10 | Fixed | Outputs outside staging are refused, and keys and mid-string paths are mapped. Two new gaps (no leftover check, non-atomic final writes) are N-1. |
| N11 | Fixed | The battery snapshots `data/p` before and after. |
| N12 | Partly fixed | p's report names m's report and reads with their sha256s. m's own files under `data/p/reports` still carry no `proposal_p_sha256`; this reading of F-p8 should go in the BUILD entry. |

#### New findings

##### MAJOR

**M-1. A plain `--resume` lifts a STOP that p raises inside a session (ProxyStop), and p's report of record then shows a PASS with no trace of the STOP.**
- **Where:**
  - stage.py:530-551: `run_time` checks p's report, the call log's existence and m's `stage_end`. Nothing reads how earlier runs ended.
  - proxy.py:81 and :144: both ProxyStops are raised inside m's session, so m writes no stop record.
  - stage.py:451-512: `build_report` records no per-run outcome.
- **What:** the seat's Q5: "the stage is STOPPED, and the seat adjudicates before anything resumes". m's own rule is "a resume never lifts a STOP" (`stages._refuse_stopped`, `resume.load_or_init`). After a ProxyStop nothing that p or m checks is persisted. m's checkpoint holds the earlier sessions with no stop, no `stage_end` and no end pending, and `run_time` accepts `resume=True` whenever the call log exists.
- **Scenario (exp_stop):**
  - A ProxyStop was planted at a contrast free round, at a contrast forced round and at a sham free round.
  - Each run ended in ProxyStop. A `--resume` whose generation no longer broke then returned PASS and wrote p's report.
  - The report and the closing lines never mention the STOP. `call_log.n_runs` = 2 is the only trace, and an ordinary interruption gives the same 2.
  - By contrast, m's own hair trigger (exp_hair) persists STOP, and a resume is refused.
- **Fix:**
  - Before the load, read the call log's end lines and refuse (exit 2) when any run ended in a STOP class: ProxyStop at least, and also StageStop, RegisterStop, KeysStop, ScheduleStop. Resume only on an adjudication input the seat defines.
  - Carry each run's outcome (its outcome and exception type, never the message) in p's report and in a closing line.
  - Add a self-test: a ProxyStop followed by `--resume` is refused.

**M-2. git ignores the write-ahead call log, which holds the only record p's report is derived from and the STOP's text.**
- **Where:** .gitignore:304-307. `/data/p/ckpt/*` re-admits only `*.json` and `*.json.podchange-*`, while the log is `ckpt/{U}_time_p-calls.jsonl` (stage.py:39-45, :363).
- **What:**
  - `git check-ignore -v` names `.gitignore:305:/data/p/ckpt/*` for all three `data/p/ckpt/OLMo-{sft,dpo,instruct}_time_p-calls.jsonl` paths.
  - The PIN says the log is "withheld like the checkpoint", and the checkpoint is committed.
  - p's committed report names the log's sha256.
  - `time-report` can only rebuild the report from the log. With the log absent: "P-REPORT STOP: ... ran under p package(s) []" (exp_calllog e).
  - Q5's adjudication needs the STOP's `returned_text`, which lives only in the log.
  - `git add data/p/ckpt` silently skips the file; only an explicit path fails, and then loudly.
  - Ledger 27: "A run that exists only on a box does not exist."
  - Knock-on: a box without the log but with m's checkpoint loads the model before m refuses (m-2).
- **Fix:** add `!/data/p/ckpt/*_p-calls.jsonl`; the existing `/data/p/ckpt/** -diff` already covers it. Add a self-test asserting that `git check-ignore` exits 1 for the three log paths and the p-report paths.

##### MINOR

**m-1. A torn last line silently swallows the next run's "run" line, and `build_report` validates the log too little.**
- **Where:**
  - stage.py:367-389: CallLog appends without checking for a trailing newline.
  - stage.py:392-412 and :465-472: only the parsed run lines' package is checked. Nothing checks their unit, stage or schema, or pairs runs with end lines.
- **Scenario (exp_calllog):**
  - **(a)** An interrupted run, then a partial line appended (a crash mid-write), then `--resume`: PASS. The resumed run's "run" line is lost inside a "not JSON" line, so the report says `n_runs` 1 for two runs (`attribution_complete` false).
  - **(b)** A log holding only a torn first line, then `--resume`: m's stage runs to PASS. p's report can then never be built, neither at the stage nor by `time-report` ("ran under p package(s) []"). A re-run is refused because the stage has ended.
  - **(d)** OLMo-dpo's log copied over OLMo-sft's: the report is built and written, counting the dpo run as sft's.
- **Fix:**
  - On open, if the file is non-empty and does not end in `\n`, write `\n` (or a `torn` event) first.
  - In `build_report`, require every run line's schema, unit and stage to be this stage's, and pair run lines with end lines by run number.

**m-2. The "second run is a --resume" refusal reads p's call log, not m's checkpoint, so a lost log costs a cold load.**
- **Where:** stage.py:533-535. m's own driver refuses "CHECKPOINT EXISTS ... pass --resume" before the load (scripts/m_sessions.py, `stage_precheck`).
- **Scenario (exp_edges 2):** an interrupted stage whose call log is gone (as after M-2 on a re-cloned volume), then a plain run. The factory is called once (a model load), and only then does m raise "CHECKPOINT EXISTS".
- **Fix:** before the load, refuse when m's checkpoint exists and `resume` is false.

**m-3. G-SHAPE-p's staleness check compares package hashes only.**
- **Where:** stage.py:218-226.
- **What:** G-SHAPE-p records a 48-file sources map (scripts/p_sessions.py, olmo_hf.py and data configs) and an import closure. gshape can recompute both (`sources_map`, `import_closure`; gshape.py:288-289, :442-446), but the precheck never compares them.
- **Scenario (exp_precheck):** today the recorded map differs from the current one on more than 10 files, yet the precheck reports only the p package hash. Suppose the package were unchanged but the driver or olmo_hf.py had moved. A lock re-issued with the new driver sha and the old G-SHAPE-p would then pass.
- **Fix:** also compare `provenance.sources` and `provenance.import_closure` with the committed current maps.

**m-4. G-ANL-p records its code shas after its 3-minute battery, with no drift check.**
- **Where:** p_analyze.py:630-650. `binding_problems` runs before `run_battery()`, but `analyzer_blobs()` and `code_shas()` are evaluated after it.
- **What:** an edit that lands during the battery (a parallel session in the same tree) is recorded as the code of record. Once committed, it passes the stage's stale check (stage.py:224-226), though the battery never ran it. G-SHAPE-p guards exactly this case (gshape.py:442-446).
- **Fix:** take both records before the battery, and refuse if they differ afterwards.

##### NOTE

- **N-1. `run_staged` (analysis.py:186-221) has no leftover check, and its final writes are not all-or-nothing.**
  - An output m writes into staging without reporting it is dropped silently (exp_analyze2 1).
  - A link or non-file at a later final target is never seeded, so m cannot see it. The earlier output is written, then GuardStop (exp_analyze2 2). m's `write_texts_once` checks every target before writing any.
  - Fix: compare staging's listing with the seeds plus the reported writes, and check every target before the first write.
- **N-2.** `keys.keys_context` (keys.py:69-89) honours any state in which all four m key functions are p's, including a hand-set one (exp_pin). This is safe while term (e)'s static check holds. Alternatively, the register could track its active entries.
- **N-3.** `proxy.attribution_complete` (stage.py:501) is computed over every round, contrast free rounds included. The module's own rule withholds every proxy figure over the contrast session. It is a flag, not a count, and it did not vary in practice: identical across the 6 free-round plantings, the contrast cut and the 4 resumed interruptions. Scope it to the read domain anyway.
- **N-4.** `lock_required` values are matched as substrings of the lock text (stage.py:316). For instance, a lock reading "...: 1/80" satisfies the covariate line "...: 1/8" (instruct). Match whole lines.
- **N-5.** At G-TIME the precheck's logged gate line reads "analyzer present d347ea0c... -- not read by G-CAL" (exp_edges 3; `m_gcal.gate_line`'s text). The wording is wrong for this stage.
- **N-6.** The driver prints any SystemExit raised inside a session verbatim (p_sessions.py:247-249). m's BOUNDARY INCIDENT message carries the prefix token count, and at a contrast free round that count depends on the transcript, picks included. The behaviour is inherited from m's driver, but it is the one STOP text p can print that carries contrast information.
- **N-7.** The seat's §2 says entries (8) and (9) are entered and restored together. Nothing enforces the pairing; `stage_substitutions` simply happens to enter both.
- **N-8. G-ANL-p coverage gaps:**
  - The p-form VERDICTS fixture checkpoints carry m's identity, not p's four fields.
  - The not-run `--v2-closure` branch (`ckpt_dir or REPO / CKPT_REL`, m_analyze.py:2583) never runs under the sentinels.
- **N-9.** A p re-run on unchanged inputs is refused with m's text "exists with different bytes -- write-once (move it aside by hand on the seat's ruling, PIN-37)". Applied to p's own correct output, that instruction invites moving a good record aside. Catch the refusal and say what it means.
- **N-10.** The p_sessions self-test count is 157/157, not the 156 the brief states.

#### Checked and sound

- **Blinding of p's report and closing lines.** Each case was compared with an unplanted run and the outputs matched apart from the sha256s:
  - a contrast free-round exclusion at each of ci 0-5;
  - a contrast free-round cut, using a cut-capable double;
  - m's own hair trigger at contrast free ci 0 and ci 3 (status STOP);
  - an interruption followed by `--resume` at four positions: contrast free ci 1 and ci 4, contrast forced, sham forced.

  A sham planting is reported, as it may be. A contrast forced exclusion moves only ruling (h)'s count.
- **ProxyStop messages** are identical at forced and free rounds and carry no text. The text detail is only in the call log.
- **Precheck side effects:** after a non-stub precheck the renders cache is 0 and one thread is alive. A thread alive before the run is refused before any load.
- **The AST pin** catches a dropped statement, an early return, a changed message and a rebound free name (exp_pin).
- **Rebuilt report:** byte-identical on an unchanged log. In the patched-root test only the `root` field differed, and that was an artifact of the patch.
- **Entry (9):** the register refuses it as PENDING in production, before any factory call.
- **Seams:** every one was restored after each experiment, including `register.BY_N[9]`, `olmo_startup`, the pod variable, `DEFAULT_OUT` and m's key functions.

#### Counts

- **Round 1 (26 items):** 23 fixed (MAJOR 3 counted fixed, its new defects listed separately), 2 partly fixed (MINOR 9, N12), 1 not fixed (N5).
- **New:** MAJOR 2, MINOR 4, NOTE 10.

#### Commands run

1. `git status --short` (start and after every run), `git diff --stat`, `git diff` of `.gitattributes`, `.gitignore`, keys, guard; full reads of the build's modules and drivers and of the spec files; `git check-ignore -v` on the call-log, report and lexicon paths; `git ls-files data/p`.
2. `nice -n 19 jlens-qwen36/.venv/bin/python -B scripts/p_analyze.py --selftest` (background): 525/525 and 13/13, exit 0, 2:47.
3. `nice -n 19 jlens-qwen36/.venv/bin/python -B scripts/p_sessions.py --selftest`: 157/157, exit 0, 18 s.
4. `exp_blind.py`: 12 plantings, report and line invariance.
5. `exp_stop.py`: ProxyStop at three positions, each then resumed; interruptions at four positions, each then resumed.
6. `exp_calllog.py`: a torn line mid-log and a torn first line, garbage lines, another unit's log, an absent log, an old-package run line.
7. `exp_precheck.py`: non-stub precheck side effects and problems; `lock_required`'s contents; G-SHAPE-p's sources map against the current one.
8. `exp_pin.py`: four AST-pin variants and a rebound free name; form "m" on six more tampered copies; `keys_context` on a hand-set state.
9. `exp_analyze2.py`: `run_staged` with an unreported output and with a link at a target; CLI refusals; sentinel tolerances; G-ANL-p's record order.
10. `exp_edges.py`: a thread before the stage; a checkpoint present without its log; the G-TIME gate line.
11. `exp_timereport.py`: the driver's `time-report` (exit 0, then 2).
12. `exp_hair.py`: m's hair trigger at two contrast free positions.
13. In-memory: `m_stages.startup_problems()` (`[]`; cache 0, one thread); `build_report` against the rewritten report (differs only in `root`).

## Round 3

### Blind review, round 3: PROPOSAL-p step 6 (uncommitted build)

I edited no file in the repository and ran no git command that writes. Every experiment ran from scripts and scratch roots under `<tmp>/scratchpad/podwatch/rev3/`; each script's output is saved beside it as `out_*.json`. `git status --short` was identical at the start and the end (HEAD `2018ffc`; no `data/p/reports` or `data/p/verdicts` created). After every experiment each seam was restored: `register._ACTIVE` all 0, entry (9) PENDING, and m's `olmo_startup`, `Identity`, `DEFAULT_OUT` and key functions, with the pod variable unset.

**Self-tests:**
- `scripts/p_sessions.py --selftest`: 162/162, exit 0, 21 s.
- `scripts/p_analyze.py --selftest`: m's battery 525/525 (538 coverage ids), then G-ANL-p 14/14, exit 0, 2 min 47 s.

#### Round-2 items

| Item | Verdict | Evidence |
|---|---|---|
| M-1 (a resume lifts a ProxyStop) | **Partly fixed** | Refused before the load when the log's lines are written and readable: the cut-boundary ProxyStop, the hair-trigger ProxyStop, a SystemExit in a session and a STOP in run 2 of a resumed stage (exp_stop3 A, B, C, F). Each run's outcome is in the report and in a closing line. The guard fails open in four cases: the log is undecodable (new MAJOR), or the end line or STOP line is not written or is torn (new MINOR 1). |
| M-2 (call log gitignored) | Fixed | `.gitignore:310`. `git check-ignore -q` exits 1 for the checkpoint, the call log, the adjudication excerpt, m's report and reads, p's report, a `.podchange-*` set-aside and the lexicon, and 0 for `*_p-calls.jsonl.tmp`. Attributes: `-diff` on `ckpt/**`; `-diff -text` on the lexicon. A self-test covers it (stage.py:1017-1023). |
| m-1 (torn line, weak validation) | **Partly fixed** | Fixed: an ASCII torn line is terminated (self-test; exp_calllog3 K2). A log already ending in `\n` gains no blank line (K4). `log_consistency_problems` runs both at the stage start and in `build_report`. Not fixed: a tear inside a multi-byte character makes the whole log unreadable (new MAJOR), and a line read back with U+2028 or U+0085 splits (new MINOR 2). |
| m-2 (lost log costs a cold load) | Fixed | stage.py:613-618. Self-test: both refusals happen with zero factory calls. |
| m-3 (G-SHAPE-p staleness: package only) | Fixed | stage.py:191-204, :239. In a `p_sessions.py time` process the import closure at precheck equals G-SHAPE-p's recorded closure key for key, 14 modules, so there is no false refusal (exp_closure). A moved driver, a shortened closure and absent provenance are each reported (exp_drift3). |
| m-4 (G-ANL-p records code after the battery) | Fixed | p_analyze.py:663-668. With a stubbed battery that moves the code record: exit 4, "the code moved during the battery", nothing written (exp_drift3). |
| N-1 (run_staged leftovers, all-or-nothing) | Fixed, with one caveat | An unreported or changed file in staging is refused (exp_staged3 S2). Every target is checked before the first write. The writes are not transactional (NOTE 2). |
| N-2 (hand-set key state honoured) | Fixed, with one caveat | keys.py:69-79. `in_force()` is false with nothing substituted, true under the register, and raises KeysStop for a partial or by-hand state (exp_register3). The count is kept per entry number (NOTE 1). |
| N-3 (attribution flag over contrast rounds) | Fixed | stage.py:577 reads the sham rounds only. |
| N-4 (lock values as substrings) | Fixed for the stage's lock | `lock_names` (stage.py:272-275) plus a self-test. p_analyze's VERDICTS-lock check still matches substrings (NOTE 3). |
| N-5 (G-TIME gate line wording) | Fixed | `m_stages.gate_line(label(unit), PROPOSAL-p)` (stage.py:349-357), with PROPOSAL-p and CLAUDE.md commit-checked. The self-test asserts no "G-CAL" text. |
| N-6 (SystemExit printed verbatim) | Answered | Draft item (f). The behaviour is unchanged (p_sessions.py:247-249). |
| N-7 ((8)/(9) pairing) | Fixed, with one caveat | register.py:139, :183-185, plus a self-test. The pairing is checked by entry number (NOTE 1). |
| N-8 (G-ANL-p coverage) | Fixed | p_analyze.py:330-334: the fixture checkpoints carry p's four fields. :513-532: `--v2-closure` runs under the sentinels. Both pass. |
| N-9 (re-run refusal wording) | Fixed | analysis.py:198-209, plus a self-test. |
| N-10 (self-test count) | Answered | The draft keeps a placeholder. Today the counts are 162/162 and 525/525 + 14/14. |
| Round-1 MINOR 9 (round 2: partly fixed) | Fixed | G-SHAPE-p is checked on both packages plus its sources map and closure. G-ANL-p is checked on all four code shas (stage.py:236-242). |
| Round-1 N12 (round 2: partly fixed) | Answered | Draft item (g). p's report names m's report and reads by sha256. |
| Round-1 N5 (round 2: not fixed) | Answered | Draft items (a) and (b), pinned at report.py:272-276. |

#### New findings

##### MAJOR

**M-1. A torn line that splits a multi-byte character makes the whole call log unreadable. The stage then treats the log as empty: every STOP in it is lifted by a plain `--resume`, run numbers restart at 1, and p's report can never be built.**

- **Where:** three places in stage.py:
  - `read_calls` (:428-448) decodes the file in one call (:434, `p.read_bytes().decode("utf-8")`), so one invalid byte anywhere returns `[], ["...: unreadable (UnicodeDecodeError)"]`.
  - `run_time` discards those problems (:632, `events, _lp = read_calls(...)`). The STOP guard (:633), the consistency check (:637) and the run number (:640) then all read `[]`.
  - `CallLog.__init__` (:409-410) terminates the torn line with `\n` but leaves the bad byte in place. `CallLog.write` (:420) writes `ensure_ascii=False`, so cut and STOP records carry the model's raw text. The hair-trigger message also contains "§" raw.
- **What:**
  - m-1's fix assumes a torn line is only malformed JSON. A tear inside a non-ASCII character makes the whole file undecodable, and `run_time` reads that as an empty log, so M-1's guard fails open.
  - The premise is the one m-1 was built for: a crash mid-write. OLMo text routinely carries non-ASCII characters (’, —, é).
  - Any invalid byte in the file has the same effect.
- **Scenario (exp_calllog3 K1):**
  1. Run 1: a cut whose text is "café". The log is then cut after the first byte of "é", with no end line, as a crash would leave it.
  2. Run 2 (`--resume`): the log reads as 0 events. The run is written as `"run": 1` and hits a ProxyStop; its STOP line and an end line with `stop: true` are written.
  3. Run 3 (`--resume`): **not refused**. m's stage runs to PASS.
  4. p's report is not written: "P-REPORT STOP: the call log's runs ran under p package(s) [], not the current …". `time-report` fails the same way and always will.
  5. The file now holds three `"run": 1` lines (log lines 1, 13 and 21), and the STOP sits at lines 19-20.
- **Fix:**
  - Write the log ASCII-only (`ensure_ascii=True` at :420), so no tear can split a character. This also removes MINOR 2.
  - Split on `b"\n"` and decode each line separately, so a bad line is one malformed line.
  - In `run_time`, refuse before the load when `read_calls` reports the log unreadable (fail closed).
  - In `build_report`, name an unreadable log as such instead of "package(s) []".
  - Add a self-test: a torn multi-byte character after a STOP, then `--resume` refused.

##### MINOR

**m-1. The STOP mark rides on one write: a failed or torn write leaves a STOPPED stage resumable.**

- **Where:**
  - stage.py:662-673: the end line's `"stop": isinstance(err, SystemExit)`. A failed end-line write only echoes "P-CALL LOG END NOT WRITTEN (OSError); the run's call lines stand".
  - proxy.py:126-131: the STOP call line is written inside `except ProxyStop`. If that write raises, the OSError replaces the ProxyStop. The in-memory `px.calls` still holds the STOP record (proxy.py:111-115), but nothing reads it.
- **Scenario (exp_stop3 D, E; exp_calllog3 K3):**
  - **(D)** A SystemExit in a session (m's BOUNDARY INCIDENT form, contrast free round) with the end-line write failing (ENOSPC planted). `--resume` gives PASS. The report shows run 1 as "no end line (the process ended first)".
  - **(E)** A ProxyStop whose STOP-line write fails. The run ends as `OSError` with `__context__` ProxyStop, and the end line records `{type: OSError, stop: false}`. `--resume` gives PASS. The report shows run 1 as "exception OSError".
  - **(K3)** The end line after a SystemExit is torn 40 bytes in. `stopped_runs` returns `[]`, and `--resume` gives PASS.
- **Fix:**
  - Compute the mark from the exception chain (`__context__`/`__cause__`) and from `px.calls`.
  - After a SystemExit, record the STOP twice: a separate O_EXCL marker file (e.g. `ckpt/{U}_time_p-STOPPED`) that `run_time` checks before the load, as well as the end line.
  - Make the failed-write echo say that the STOP is not recorded and that nothing may resume without the seat.

**m-2. Cut and STOP records whose text carries U+0085, U+2028 or U+2029 are read back as fragments, so p's report miscounts the sham cuts and calls an intact log malformed.**

- **Where:**
  - stage.py:420: `ensure_ascii=False` writes these characters raw; json escapes only characters below 0x20.
  - stage.py:434: `str.splitlines()` treats them as line boundaries.
- **Scenario (exp_lsep3):** a sham forced round returning "Two.<U+2028>ok\nTask: leak" is cut. The call line comes back as 3 "not JSON" fragments. The report then shows:
  - sham `n_cuts` 0 instead of 1;
  - "A0s-OLMo-sft s=0 forced 2" unattributed, `attribution_complete` false;
  - `well_formed` false with 3 malformed lines.

  U+0085 gives the same result. This is a C1 control character, the class F-p13's counter exists for. A ProxyStop whose returned text holds U+2028 loses its STOP line (0 seen); only the end line keeps the stage STOPPED, so with MINOR 1 nothing would.
- **Fix:** the same as the MAJOR: ASCII-only lines, split on `b"\n"`.

**m-3. A STOP raised while the substitutions are entered leaves an empty call log, unrecorded. The next legitimate first run must then be a `--resume`, and it is recorded as `resume: true`.**

- **Where:**
  - stage.py:641 opens the log (O_CREAT) before `stage_substitutions()` (:644). The run line is written only after every entry succeeds.
  - The precheck never checks that every entry in `ENTERED` is substitutable.
  - The stage's own PIN (stage.py:451-454) lists RegisterStop and StageStop as classes that block.
- **Scenario (exp_entry3 I1, exp_entry3b):**
  - **(I1)** In the register's production state today, entry (9) PENDING, the run gets RegisterStop at entry (9) with no factory call. `OLMo-sft_time_p-calls.jsonl` is left at 0 bytes. After admitting (9), a plain run is refused ("the call log exists; a second run is a --resume"). `--resume` gives PASS, with run 1 recorded as `resume: true`.
  - **(I3b)** m's renders are cached between the schedules check and entry (1). The StageStop leaves a 0-byte log, `stopped_runs` returns `[]`, and `--resume` gives PASS.
  - A thread alive before the run is refused by the precheck, before any log (I2): sound.
- **Fix:**
  - Open the log inside the substitutions, just before the run line.
  - In the precheck, refuse (exit 2) when any entry in `ENTERED` is not in `register.SUBSTITUTABLE`.

##### NOTE

1. **The register counts by entry number, not by (entry, module)** (register.py:140, :183-199).
   - (8) entered on a stand-in module named `valence_core.m.resume` admits (9) on m's real `resume`, whose key set is then not extended.
   - Entry (2) on a stand-in, plus the four key functions set by hand on m's real `keys`, makes `keys.in_force()` true.
   - A restoration whose `setattr` fails leaves the count up for the process (exp_register3).
   - None of these is reachable from p's code. A key of `(n, id(module))` closes all three.
2. **`run_staged`'s writes are pre-checked, not transactional** (analysis.py:234-246).
   - With the second of two writes failing (ENOSPC planted), the first output stays written (exp_staged3 S7).
   - For a VERDICTS and its secondary, every later p re-run is then refused with "the record stands and nothing is to be moved aside" (:208), although the set is incomplete.
   - The comment "(all or nothing)" at :234 over-claims.
3. **p_analyze's lock binding matches substrings** (p_analyze.py:164, `if v not in text`). A lock holding p's analyzer and package shas only inside longer hex runs passes (exp_staged3 P1). N-4's whole-line or backtick rule would apply here too.
4. **No concurrency guard.**
   - Two processes that read the log before either writes its run line both take run 1. The stage then ends with p's report unbuildable ("run numbers [1, 1]"), and every later run is refused (exp_calllog3 K5, simulated).
   - m has no lock either. An `fcntl.flock` on the call log for the run's duration would close it.
5. **Any m refusal after the run line is a permanent STOP** (stage.py:669, `stop: isinstance(err, SystemExit)`).
   - With `olmo_startup` refusing once, before any session and before m's checkpoint exists, both `--resume` and a plain run are refused (exp_stop3 H).
   - m's own rule ("a resume never lifts a STOP") concerns m's STOP records; m lets a refused stage re-run once the cause is fixed.
   - The draft declares this as "a refusal once the run had begun", but it is p's extension and should be put to the seat.
   - The way out is the seat's ruling plus moving the committed call log aside by hand (m's PIN-37 precedent). No adjudication input is defined.

#### Draft-entry claims

- **M-1 bullet.** "...blocks every later run before the load" does not hold:
  - when the log is undecodable (the MAJOR);
  - when the end or STOP line fails or tears (MINOR 1).

  "(Q5; m's rule, a resume never lifts a STOP)": m's rule does not cover m's refusals, which p's guard also turns into STOPs (NOTE 5).
- **m-1 bullet.** "a torn last line is terminated before the next run appends" is true, but a tear inside a multi-byte character keeps the whole log unreadable (the MAJOR). A line torn by a failed write within a run is not terminated before that run's own end line is appended, so the two glue into one malformed line.
- **"Throughout: the write-ahead call log ... Every event is written ... a STOP's detail".** The records are written, but a cut or STOP record carrying U+0085, U+2028 or U+2029 does not read back (MINOR 2).
- **THE STAGE bullet's list of what the lock must name.** It includes "the backend identifier of record", which is not a `lock_required` value: it is the separate rule of exactly one `BACKEND OF RECORD` line (`lock_backend`). The list also omits values `lock_required` holds (the proposals, p's package, the covariate, the schedules, the banner parts, the ban list, the scaffold set). The MINOR 8 bullet names them, so this is imprecise rather than wrong.
- **stage.py:451-454's PIN** lists StageStop and RegisterStop as blocking classes. Those raised while the substitutions are entered are not recorded (MINOR 3).
- **analysis.py:234's "(all or nothing)"** over-claims (NOTE 2). The BUILD entry's wording, "checks every target before the first write", is accurate.

#### Checked and sound

- **STOP guard on the normal path:**
  - Refused before the load, with no factory call: a cut-boundary ProxyStop, a hair-trigger ProxyStop (cut disabled for the run), a SystemExit in a session, and a STOP in run 2 of a resumed stage (exp_stop3 A, B, C, F).
  - Ctrl-C is an interruption: `--resume` gives PASS, and the report shows "1 first exception KeyboardInterrupt; 2 resume returned" (G).
  - m's own hair trigger: the report is written, and a later run is refused ("p's report exists") (exp_hair3).
- **Blinding of the round-2 fields** (per-run outcomes and exception types, `well_formed`, `n_malformed_lines`, term (d) per end line, the closing lines; exp_blind3 and exp_hair3). Reports and lines were identical within each group, sha256s aside:
  - RuntimeError at 6 positions (contrast free ci0, ci1, ci4, contrast forced, sham forced, sham free), each resumed;
  - Ctrl-C at the same 6 positions;
  - a contrast free exclusion at ci0..ci5 followed by a sham interruption;
  - an exclusion at ci0 or ci3 against none;
  - a contrast free cut against none;
  - m's hair trigger at contrast free ci0 against ci3, with and without an earlier interruption.

  The gate line is computed before the run. The refusal texts name run numbers only.
- **The register:** a failing `setattr` on entry leaves the count down and the attribute restored. Nesting counts 1, 2, 1, 0 with the replacement kept between (exp_register3). Stage entry with (9) PENDING unwinds every entry, and all counts return to 0.
- **The lock check:** `lock_names` and `lock_backend` behave as pinned. The author's generator writes LICENCE, REGISTER and BACKEND lines in code blocks and every other value in backticks, which matches.
- **run_staged:** a seeded file changed without a report is refused. A seeded file reported unchanged is refused write-once. A seeded file deleted by m is harmless.
- **identity.py:** the open50 §2 term (c) checks hold through the register. (9) stays PENDING in production.

#### Counts

- **Round-2 items (16):** 12 fixed (M-2, m-2, m-3, m-4, N-1, N-2, N-3, N-4, N-5, N-7, N-8, N-9), 2 partly fixed (M-1, m-1), 2 answered (N-6, N-10).
- **Round-1 carry-overs:** MINOR 9 fixed; N12 and N5 answered.
- **New:** MAJOR 1, MINOR 3, NOTE 5.

#### Commands run

1. `git status --short` (start and end; saved to `podwatch/status_before_rev3.txt` and diffed), `git diff --stat`, `git diff` of `.gitattributes`, `.gitignore`, keys, guard, proxy and p_sessions; full reads of stage, register, keys, schedule, proxy, report, identity, analysis, p_sessions and p_analyze; m's `run_gate_stage`, `_finish_gate`, `load_or_init`, `licence_problems`, `gate_line`, `assert_boundary` and `_set_aside`; `git check-ignore -q` and `git check-attr` on every G-TIME output path; `shasum` and `wc -l` on the lexicon.
2. `nice -n 19 jlens-qwen36/.venv/bin/python -B scripts/p_analyze.py --selftest` (background): 525/525 and 14/14, exit 0, 2:47.
3. `... scripts/p_sessions.py --selftest`: 162/162, exit 0, 21 s.
4. `exp_closure.py precheck`: the time process's import closure against G-SHAPE-p's.
5. `exp_stop3.py`: STOP-guard cases A-H.
6. `exp_calllog3.py`: K1 split UTF-8, K2 torn run line, K3 torn end line, K4 trailing newline, K5 two writers.
7. `exp_entry3.py` and `exp_entry3b.py`: STOPs at the substitutions' entry.
8. `exp_blind3.py` and `exp_hair3.py`: blinding of the new fields.
9. `exp_register3.py`: the in-force count, `keys.in_force` states, pairing by number.
10. `exp_staged3.py`: `run_staged` edges, the VERDICTS lock binding.
11. `exp_drift3.py`: the drift comparison and G-ANL-p's drift refusal.
12. `exp_lsep3.py`: U+2028 and U+0085 in cut and STOP records.

## Round 4

### Blind review, round 4: PROPOSAL-p step 6 (uncommitted build), focused on round 3's fixes

I edited no repository file and ran no git command that writes. `git status --short` was identical at the start and
the end (HEAD `2018ffc`; saved as `podwatch/git_status_start_rev4.txt` and `rev4/git_status_end.txt`, diffed). No
`data/p/reports`, `data/p/verdicts` or lock file appeared under `data/p`. Every experiment ran from scripts and scratch
roots under `<tmp>/scratchpad/podwatch/rev4/`.
Each script's output sits beside it as `out_*.json`. After every script the seams were restored and checked:
`register._ACTIVE` empty, entry (9) PENDING, m's `olmo_startup`, `Identity`, `DEFAULT_OUT` and key functions m's own,
`guard.write_once_bytes`, `CallLog.write`/`_put`, `fcntl.flock`, `os.replace` and `stage.write_report` the real ones,
and the pod variable unset.

**Self-tests:**
- `scripts/p_sessions.py --selftest`: 166/166, exit 0, 24 s.
- `scripts/p_analyze.py --selftest`: m's battery 525/525 (538 coverage ids), then G-ANL-p 14/14, exit 0, 2 min 50 s.

#### Round-3 items

| Item | Verdict | Evidence |
|---|---|---|
| MAJOR (a torn multi-byte line made the log unreadable, and the guard failed open) | **Fixed** | Lines are ASCII (stage.py:440) and read per `b"\n"` (:457-470). K1 replayed (A1): a tear inside the ASCII escape `\u00e9` is one malformed line, run 2's ProxyStop is recorded (marker and end line), run 3 is refused with no factory call, and runs are numbered 1, 2. An invalid byte mid-log with the marker removed is one malformed line, and the end line still refuses (A2). A mode-000 log is refused before the load (A3), and `build_report` names it on an ended stage (X1). |
| MINOR 1 (the STOP mark rode on one write) | **Partly fixed** | Round 3's single planted failures are now held, each refused before the load: D (B1), E (B2), K3 (B3), and an end line torn after the marker (T4). Not held: one cause that fails both records (ENOSPC/EIO: N2, N2b, T1) still leaves the stage resumable, announced only on stdout (new NOTE 1). The marker's own write window is a new gap (new MINOR m-1). |
| MINOR 2 (U+0085, U+2028, U+2029) | Fixed | C: with U+2028, U+0085 or neither in a sham cut, the log is ASCII with 22 events, no problems, sham `n_cuts` 1, attribution complete and well formed. A ProxyStop whose text carries U+2028 keeps its STOP line, and the returned text reads back exactly. |
| MINOR 3 (a STOP while the substitutions are entered left an empty log) | Fixed | D1: with (9) PENDING, the precheck refuses (StageRefusal) before the lock and the factory, leaving no file. A precheck taken with (9) admitted, then run with (9) PENDING, gives RegisterStop and no call log. N10: the renders-cache StageStop leaves no log, no checkpoint and no marker. After each, a plain run PASSes as run 1 with `resume: false`. |
| NOTE 1 (the register counted by entry number) | Fixed | Counts are keyed `(n, id(module))` (register.py:140-151, :192-205). (8) on a stand-in refuses (9) on m's `resume`. A stand-in (2) plus hand-set functions gives KeysStop. A failed restoration leaves the count at 0. ValueError, KeyboardInterrupt and SystemExit raised inside nested entries each return the count to none (exp_misc4 N1a-d). |
| NOTE 2 (`run_staged` was not transactional) | **Partly fixed** | `guard.write_once_all` (guard.py:184-230): a phase-2 exception writes nothing (self-test). A crash leaves temps after which every later write of the set raises a raw FileExistsError (N2a). A part-written set is refused on re-run as "the record stands" (N2d). See new NOTE 4. |
| NOTE 3 (the lock binding matched substrings) | Fixed | p_analyze.py:156-165 uses `stage.lock_names`. The substring lock now gives both problems, the backtick and whole-line forms pass, and a lock naming one value gets the other flagged (exp_misc4 N3). |
| NOTE 4 (no concurrency guard) | Fixed, with caveats | `stage_lock` (stage.py:494-512): while a second process holds the lock, the run is refused and the factory is never called. Once that process is killed, the run proceeds. A stale lock file does not block (N7a, N7b). Caveats: the driver's `time-report` takes no lock (new NOTE 3), and any flock error reads as "another run holds its lock" (new MINOR m-2). |
| NOTE 5 (any m refusal after the run line was a permanent STOP) | Answered | Draft item (i) and the PIN (stage.py:50-57) put p's extension to the seat. The behaviour is unchanged. |
| Draft claim: the M-1 bullet | Partly | "blocks every later run before the load" holds for the planted cases. "Round 3 closed the guard's remaining gaps" does not (m-1, NOTE 1). m's rule is now worded as p's extension, for the seat. |
| Draft claim: the m-1 bullet (glue) | Answered | The draft now says the torn line and the end line "read back as one malformed line"; N4 confirms it. |
| Draft claim: "Throughout ... a STOP's detail" | Fixed | Confirmed by C. |
| Draft claim: THE STAGE's lock list | Fixed | It names every `lock_required` value, with the BACKEND line separate. p's manifest lists 6 schedule files per unit (18 in all), as the list says. |
| Draft claim: the PIN on StageStop and RegisterStop | Fixed | The PIN now scopes the STOP to "once its run line is written" and says a STOP while the entries are entered leaves no record (stage.py:45-46, :50-57). D1 and N10 behave so. |
| Draft claim: "(all or nothing)" | Fixed | analysis.py:233 now reads "every target checked, then two-phase writes". The guard docstring states the phase-3 residual, but omits a crash (NOTE 4). |

#### New findings

##### MAJOR

None.

##### MINOR

**m-1. The STOP marker's own write window. A KeyboardInterrupt during it skips the end line; a crash during it leaves only the marker's temp file, which the guard never reads. Either way, a STOP of any class except a ProxyStop is lifted by a plain `--resume`.**

- **Where:**
  - stage.py:738-750: `except (OSError, SystemExit) as me` around `guard.write_once_bytes(pp["p_stopped"], ...)`.
  - guard.py:151-181: the marker is written to `...-STOPPED.json.tmp` and renamed, and `except BaseException` unlinks the temp.
  - stage.py:673: the guard checks the marker's final name only.
- **What:** the marker is the first of the two records, and two events in its window leave neither record.
  - **A KeyboardInterrupt** raised inside the write (a Ctrl-C, perhaps after an fsync stalls on the network volume) leaves the `finally` before the end line is written. The temp is unlinked, so nothing records the STOP.
  - **A crash** (SIGKILL, OOM kill, pod preemption, power loss) between the temp's creation and the rename leaves only `ckpt/{U}_time_p-STOPPED.json.tmp`, which is gitignored, and no end line. The driver's `STOP:` line is never printed, so the run looks like a crash, and a crash invites `--resume`.
  - A ProxyStop survives both, through its STOP call line (N1b). Not covered: m's SystemExits (BOUNDARY INCIDENT, m's refusals) and p's backend StageStop.
  - The seat's Q5 forbids exactly this outcome ("the seat adjudicates before anything resumes").
- **Scenario:**
  - **N1:** a SystemExit STOP (m's BOUNDARY INCIDENT form, at a contrast free round), with a KeyboardInterrupt raised inside the marker's write. Afterwards there is no marker, no temp, no end line and no STOP line. `--resume` PASSes with the factory called, and p's report shows run 1 as "no end line (the process ended first)".
  - **N3:** the files a crash leaves, built from a real STOPPED run (the marker moved to its temp name, the end line removed). `--resume` PASSes.
  - **N1b:** the same with a ProxyStop: refused (its STOP call line).
- **Fix:**
  1. Create the marker at its final name with `O_CREAT|O_EXCL|O_NOFOLLOW`, then write and fsync its content: its existence is the record, so a torn marker still refuses. Alternatively, refuse while a file exists at the marker's temp name.
  2. Catch BaseException around the marker, hold it, write the end line, then re-raise.
  3. Guard the two `echo` calls in that `finally`, so a failing print cannot skip the end line.
  4. Add self-tests: a KeyboardInterrupt in the marker's write, and a left-over marker temp, each refused before the load.

**m-2. The stage lock's flock has never run on the volume it will run on, and every flock error is reported as "another run of this stage holds its lock".**

- **Where:**
  - stage.py:503-509.
  - On the box the repo is at `/workspace/repo/jspace-lab` (scripts/box_respawn_check.py:26, scripts/box_smoke_olmo.py:25, and the scratch wrapper `podwatch/run_gtime_p.sh`), so `data/p/ckpt/*_p.lock` lies on the network volume.
  - Nothing else in `valence_core/` or `scripts/` takes a flock.
- **What:**
  - `except OSError:` maps ENOLCK, EOPNOTSUPP, EINVAL and the like to the specific claim that a second process holds the lock.
  - If the volume's flock is unsupported or has no lock manager, every G-TIME run is refused before the load with a false diagnosis. The cure is then a change to p's package after LOCK-p v0.1, which means re-running G-SHAPE-p and G-ANL-p and re-issuing three locks.
  - A read-only `ckpt/` or a symlinked lock file surfaces as a raw PermissionError or OSError (ELOOP), not a refusal, so the driver prints a traceback. This fails closed: nothing loads, and the symlink's target is not created.
- **Scenario:**
  - **N7d:** flock raising ENOLCK, or EOPNOTSUPP, each gives "REFUSED: another run of this stage holds its lock (OLMo-sft_time_p.lock) -- nothing loaded".
  - **N7c:** `ckpt/` at mode 555 gives a PermissionError, not a StageRefusal; the factory is not called.
  - **N7e:** a symlinked lock gives OSError ELOOP; the target is not created.
- **Fix:**
  - Catch `BlockingIOError` alone for "holds its lock". Any other OSError, including the open's, becomes a StageRefusal that names the errno ("the stage lock could not be taken").
  - Before LOCK-p v0.1, run a model-free two-process `LOCK_NB` probe in `/workspace/repo/jspace-lab/data/p/ckpt` on the pod, and log it with the BACKEND entry.

##### NOTE

1. **One cause fails both records** (round 3's MINOR 1, residual).
   - **What:** ENOSPC or EIO on the volume at the moment of a STOP fails the marker and the end line alike, and for a ProxyStop its STOP line too. The stage is then resumable, and only stdout says so.
   - **The box wrapper:** the scratch `run_gtime_p.sh` sends stdout and stderr to `/workspace/gtime_p/gtime_p-{ck}.txt`, on the same volume. On a full volume, that announcement is lost as well.
   - **The echo:** if the echo inside the marker's `except` raises (a print to a full or broken stdout), the end line is skipped.
   - **Scenario:**
     - N2 (SystemExit STOP, ENOSPC at the marker and at the end line): both echoes print, the second being "THIS STOP IS NOT RECORDED -- nothing may resume without the seat". `--resume` PASSes.
     - N2b (ProxyStop, ENOSPC at the STOP line, the marker and the end line): `--resume` PASSes.
     - T1 (EIO at the marker, the end line short-written): one malformed line, and `--resume` PASSes.
   - **Fix:** either reserve the record before it is needed, or state the residual in the PIN, where "recorded twice" shares one volume. Reserving means:
     - after the run line, create a placeholder at a reserved name;
     - on a STOP, rename it to the marker (a rename needs no data blocks);
     - delete it at a non-STOP end, and at the next run's start when a crash left it.

2. **Malformed lines are skipped, never fail closed** (stage.py:430-440, :457-470, :692-703).
   - **A torn line glues to the next one.** A short write followed by an error leaves the tail unterminated for the same run's next write. N4: a STOP line short-written, then EIO; the run ends as a ProxyStop, with its marker written. Read back, the STOP line and the end line are one malformed line: `stopped_runs` is `[]` with 0 end lines, so the marker is the only record. With the marker removed, `--resume` PASSes.
   - **A log with no parseable line reads as an empty record**, even when m's checkpoint exists, against the PIN's "(never read as an empty record)". A4: a STOPPED log with its newlines removed and its marker removed gives 0 events; `--resume` PASSes and appends a new `"run": 1`.
   - **Fix:**
     - `CallLog` keeps a dirty-tail flag, set before a write and cleared after it completes, and starts the next write with `b"\n"`.
     - `_run_time_locked` refuses when m's checkpoint exists and the log holds no run line.
     - Optionally, it also refuses a malformed line that is not the last, or one carrying `"stop": true` or `"stop": {`.

3. **`time-report` takes no stage lock** (p_sessions.py:255-273).
   - **What:**
     - The PIN's "spans the reads, the checks and the appends" covers runs only.
     - A `time-report` during a run's tail (m's end persisted, the end line not yet written) writes p's report of record without that run's end line.
     - The run then STOPs at its own report write. Its stated remedy, `time-report`, is now refused, because the report exists.
   - **Scenario (N6):** time-report's own call, `write_report`, made at the moment the run writes its end line.
     - The time-report writes the report.
     - The run gives "StageStop ... p's report was not written (GUARD STOP: p's report EXISTS ...)".
     - The report of record shows run 1 as "no end line (the process ended first)", with `term_d_at_stage_end` `[]`.
   - **Fix:** `time_report` takes `stage_lock`, and is refused while a run holds it.

4. **`write_once_all` after a crash** (guard.py:208-213, :184-189; analysis.py:201-209).
   - **What:**
     - **A left-over temp blocks the set.** Phase 2 opens temps with O_EXCL, and its cleanup is an `except` clause, so a crash in phase 2 or 3 leaves temps. Every later write of that set then raises a raw FileExistsError until someone deletes a gitignored file. The error escapes p_analyze's `P_REFUSALS` (AnalysisRefusal and GuardStop), so the analyzer prints a traceback.
     - **The writers differ.** `write_once_bytes`, which writes p's report and the marker, overwrites a stale temp (O_TRUNC).
     - **A part-written set's re-run is mis-worded.** After a rename fails, or a crash in phase 3, a p re-run is refused as "already written once ... the record stands and nothing is to be moved aside", though one output is missing.
     - **The docstring is incomplete.** Its "only by a rename failing" omits a crash. The behaviour fails closed throughout.
   - **Scenario:**
     - N2a: a stale `y.json.tmp` gives FileExistsError on both attempts, and nothing is written.
     - N2b: `write_once_bytes` on the same stale temp writes.
     - N2c: the second rename failing leaves `x.json` and `y.json.tmp`; the retry gives FileExistsError.
     - N2d: through `run_staged`, the same leaves `V.json` and `V2.json.tmp`; the re-run gives "ANALYSIS REFUSED: V.json is a p output, already written once ...".
   - **Fix:** either refuse an existing temp in phase 1 as a GuardStop that names it, or open temps with O_TRUNC as `write_once_bytes` does. Either way, add "or a crash in (3)" to the docstring.

5. **Housekeeping:**
   - (a) A refused run now leaves `out/ckpt/` and the lock file, created at stage.py:502-503 before any check. N8: a run refused because p's report exists leaves `ckpt/OLMo-sft_time_p.lock`. The file is gitignored and harmless, but the self-test text "refused before it writes anything" (stage.py:969-970) is no longer literal.
   - (b) `CallLog.__init__` leaks its fd when ending a torn line fails (stage.py:425-428). N9: open fds go from 5 to 6.
   - (c) When a STOP line fails to write, the STOP's detail (its stored and returned text) lives only in memory. `e.log_error` (proxy.py:133-134) reaches no end line, no marker and no stdout, so the seat's read loses the text. The marker, withheld under `ckpt/`, could carry the proxy's STOP record from `px.calls`.
   - (d) The lock refusal's message lacks the `{label} REFUSED:` prefix that every other refusal carries.

#### Draft-entry claims

- **Round-3 paragraph, MAJOR:** accurate (A1-A3, X1).
- **Round-3 paragraph, MINOR 1** ("Now the STOP is recorded twice ..."): accurate for one failed write. A common cause (NOTE 1) and the marker's own window (m-1) still leave the stage resumable.
- **Round-3 paragraph, MINORs 2 and 3:** accurate.
- **Round-3 paragraph, NOTEs:**
  - 1 and 3: accurate.
  - 2: "A failure before the renames writes nothing" holds for an exception, but a crash leaves temps that block every later write of the set (NOTE 4).
  - 4: holds for runs; `time-report` runs unlocked (NOTE 3).
- **Round-2 paragraph, M-1:** "Round 3 closed the guard's remaining gaps" over-claims (m-1, NOTE 1).
- **"Throughout"**, "One run at a time: a `flock` on a local lock file spans the reads, the checks and the appends":
  - true for runs, but `time-report` reads the log and writes the report outside the lock (NOTE 3);
  - on the box the lock file is on the network volume, not a local disk (m-2).
- **"The STOP"**, "Every later run refuses before the load while either stands, or while the log is unreadable": true as worded. stage.py's PIN adds "(never read as an empty record)", but a log with no parseable line is read as one (NOTE 2).
- **The way out.** The draft's "the record moved aside by hand (m's PIN-37)", which item (i) spells as "(the call log and the marker)", is incomplete:
  - Those two moved alone leave m's checkpoint, and every run is still refused. A plain run gives "m's checkpoint exists ... pass --resume", and `--resume` gives "the earlier runs' record is lost" (X3).
  - Moving only the marker leaves the end line's stop mark, so the run is still refused (X3b).
  - So a restart needs m's checkpoint moved too, and no move of files can carry out a "resume" ruling.
  - The PIN should name all three files, or the form for each ruling. Committed first, the files stay tracked under `git mv` (PIN-37), so `.gitignore` does not bar their superseded names.
- **THE STAGE's lock list:** accurate.
- **Placeholders:** `@@STAMP@@`, `@@E9SHA@@`, `@@GANL@@`, `@@PKG@@` and `@@CHECKS@@` remain to be filled. Today's counts are 166/166 (`p_sessions`) and 525/525 plus 14/14 (`p_analyze`).

#### Checked and sound

- **The STOP guard's other paths.**
  - A marker present with the log moved away: plain and `--resume` are both refused (X2).
  - Only the marker moved aside: still refused, by the end line (X3b).
  - The end line torn after the marker (B3, T4): refused by the marker.
  - A KeyboardInterrupt at the end line after the marker (T3): refused by the marker.
  - A ProxyStop whose marker fails and whose end line is torn: held by its STOP line (T2).
- **The order of refusals in `_run_time_locked`.** The checks run in this order, each before the substitutions and the factory:
  1. p's report exists;
  2. the marker exists, or is a link;
  3. the log exists on a plain run;
  4. m's checkpoint exists on a plain run;
  5. the log is lost on a `--resume`;
  6. m's checkpoint records the stage's end;
  7. the log is unreadable;
  8. a run ended in a STOP;
  9. the log is not this stage's;
  10. the schedules are not clean.
- **A STOP in the report's write after m returned (N5):**
  - the run gives StageStop with no marker, which is right: the stage ended, it is not STOPPED;
  - the next run is refused because m's checkpoint records the end;
  - `time-report` then writes the report, with run 1 "returned".
- **Blinding, re-run on round 3's code.** exp_blind4 is round 3's exp_blind3, unchanged. Reports and closing lines were identical within each group, sha256s aside:
  - a RuntimeError at 6 positions;
  - a Ctrl-C at the same 6;
  - a contrast free exclusion at ci0..ci5, then a sham interruption;
  - an exclusion at ci0 or ci3 against none;
  - a contrast cut against none.

  exp_hair4: m's hair trigger at contrast free ci0 against ci3, with and without an earlier interruption, gives a STOP status, identical reports and lines, and a later run refused. The end line's new `stop_marker` field reaches no report field or closing line.
- **`stage_lock`:**
  - Its fd is closed on the refusal and at the end, and is non-inheritable (PEP 446).
  - flock is per open file description on macOS and on local Linux filesystems, so the self-test's same-process holder is a valid conflict.
  - The refusal comes before any read of the record.
  - A stale lock file is harmless, and a symlinked lock is refused without touching its target.
- **`stop_in`:** it walks `__cause__`/`__context__` with a cycle guard. m's production stage path catches no SystemExit or BaseException (`grep` over `valence_core/m`), so a SystemExit m has already handled cannot mark a run STOPPED.
- **Git admission and diffs:**
  - `*_p-STOPPED.json` is git-admitted (`!/data/p/ckpt/*.json`) and `-diff`;
  - the lock, `*.tmp` and the marker's temp are ignored;
  - the three call logs and the reports are admitted.
- **The register:** the per-(entry, module) count holds under exceptions and nested entries, and `keys.keys_context` inside a stage does not re-enter (count 1).
- **p_analyze:** its lock binding behaves as the NOTE 3 row says. `run_ganl`'s code record and its drift refusal are unchanged.

#### Counts

- **Round-3 items (9):**
  - fixed (6): MAJOR, MINOR 2, MINOR 3, NOTE 1, NOTE 3, and NOTE 4 with its caveats;
  - partly fixed (2): MINOR 1, NOTE 2;
  - answered (1): NOTE 5.
- **Round-3 draft-entry claims (6):** 4 fixed, 1 partly (the M-1 bullet), 1 answered (the m-1 bullet).
- **New:** MAJOR 0, MINOR 2, NOTE 5.

#### Commands run

1. `git status --short` at the start and the end (saved and diffed), `git rev-parse HEAD`, and `git diff --stat`.
2. `git diff` of `guard.py`, `.gitignore` and `.gitattributes`.
3. `git check-ignore -q` on the marker, the lock, the temps, the call log and the report paths, and on set-aside names; `git check-attr -a` on the marker and the lock.
4. Full reads of `stage.py` and `proxy.py`. Reads of:
   - `register.py`'s `substituted`, `_ACTIVE` and `active`;
   - `keys.py`'s `in_force` and `keys_context`;
   - `guard.py`'s write helpers;
   - `analysis.py`'s `run_staged`;
   - `p_analyze.py`'s `binding_problems`, `lock_binding_problems`, `run_ganl` and `main`;
   - `p_sessions.py`'s `run_time_stage` and `time_report`;
   - m's `run_gate_stage`, `_finish_gate`, `_begin`, `load_or_init`, `_set_aside` and PIN-37;
   - the draft entry, and the scratch `run_gtime_p.sh`.
5. `grep` for:
   - m's SystemExit/BaseException handlers;
   - other flock users;
   - the box repo path;
   - m's write-once wording.
6. `nice -n 19 jlens-qwen36/.venv/bin/python -B scripts/p_analyze.py --selftest` (in the background): 525/525 and 14/14, exit 0.
7. `... -B scripts/p_sessions.py --selftest`: 166/166, exit 0.
8. `rev4/exp_items4.py`: A1-A4 (the MAJOR), B1-B3 (MINOR 1), C (MINOR 2), D1 (MINOR 3). Its D2 patched p's schedule verifier and so tripped entry (7)'s identity check (a RegisterStop, no log) instead of the renders cache; the renders-cache case is exp_new4's N10.
9. `rev4/exp_new4.py`: N1-N10 (the marker's window, common-cause failures, a crash in the marker, the glue, the report's STOP, the time-report race, the lock, the refusal footprint, the fd leak, the renders-cache STOP).
10. `rev4/exp_misc4.py`: the register, `keys.in_force`, `write_once_all`, `run_staged` on a part-written set, and the lock binding.
11. `rev4/exp_extra4.py`: X1-X3b (`build_report` on an unreadable log, the marker without the log, the declared way out).
12. `rev4/exp_tail4.py`: T1-T4 (the end line under a STOP in flight).
13. `rev4/exp_blind4.py` and `rev4/exp_hair4.py`: round 3's blinding experiments, unchanged, against the round-3 code.

## Round 5

### Blind review, round 5: PROPOSAL-p step 6 (uncommitted build), round 4's fixes

**Scope and hygiene**
- I edited no repository file and ran no git command that writes.
- `git status --short` was identical at the start and the end (HEAD `2018ffc`). The two snapshots are saved and were diffed:
  - <tmp>/scratchpad/podwatch/rev5/git_status_start_rev5.txt
  - <tmp>/scratchpad/podwatch/rev5/git_status_end.txt
- Nothing was written under `data/p`: no lock file, no `reports/` and no `verdicts/` appeared.
- Scripts, scratch roots and outputs (`out_*.json`) are all under <tmp>/scratchpad/podwatch/rev5/ (below, "rev5/").
- Every script prints its seams restored at the end:
  - entry (9) PENDING, and `register._ACTIVE` empty;
  - m's attributes m's own;
  - `os.rename`, `os.write`, `fcntl.flock`, `_fsync_dir`, the `CallLog` methods and `stop_in` the real ones;
  - the pod variable unset.
- Code locations are relative to <repo>/.

**Self-test**
- `scripts/p_sessions.py --selftest`: 168/168, exit 0, 28 s.
- `p_analyze --selftest` was skipped, as instructed.

#### Round-4 items

| Item | Verdict | Evidence |
|---|---|---|
| m-1: the marker's own write window | **Fixed.** The residual is stated, but its scope is too narrow (NOTE 1). | The marker is now a rename of a fsynced reservation, so it is never half-written. **S1** (an m-style SystemExit, then a Ctrl-C inside the rename): the end line is written with its stop mark and `NOT IN PLACE (KeyboardInterrupt)`, the Ctrl-C is re-raised, and `--resume` is refused. **SIGKILL in the directory fsync after the rename:** refused by the marker. **SIGKILL just before the rename:** resumable, which is the PIN's stated residual. |
| m-2: flock errors all read "held" | **Fixed.** | **L1:** only BlockingIOError reads "held" (EAGAIN/EWOULDBLOCK; EALREADY and EINPROGRESS also map there, but flock never returns them on Linux or macOS). ENOLCK, EOPNOTSUPP, ENOTSUP, EINVAL, EBADF, EINTR, EIO, EDEADLK and ENOMEM read "unavailable". **N7c, N7e, L2, L3:** a read-only `ckpt/`, `ckpt/` a regular file, a symlinked lock and `ckpt/` a symlink each give a labelled StageRefusal; the factory is never called and no symlink target is created. |
| NOTE 1: one cause fails both records | **Partly fixed.** | **ENOSPC is fixed:** the self-test and the re-run N2/N2b fail every log write, the renamed marker holds, and `--resume` is refused. **Not fixed:** EIO at both the rename and the end line (S5), or a second Ctrl-C at the end line (W2), records nothing; `--resume` PASSes, and the echo contradicts itself (new m-1). |
| NOTE 2: malformed lines never fail closed | **Fixed.** | **S13** (round 4's N4, with the tear made inside the real `_put`): the end line parses after the torn STOP line; with the marker removed, `--resume` is refused by the end line. **A4 re-run:** refused with "m's checkpoint exists but the call log holds no run line". Round 4's N4 seam writes outside `_put`, so it still glues; that is a seam artifact. |
| NOTE 3: `time-report` unlocked | **Fixed.** | **L5:** `time-report` through the driver, at the run's tail, exits 2 with "another process holds the stage's lock". The run then writes the report with its end line (run 1 "returned", one term (d) entry). Round 4's N6 called `write_report` directly, bypassing the driver, so it still writes. |
| NOTE 4: `write_once_all` after a crash | **Partly fixed.** | **N2a:** a stale temp no longer blocks (written, then identical). **N2c:** a retry at `write_once_all`'s level completes the set. **N2d:** through `run_staged` the re-run is refused, but the text still does not say that this set is incomplete (NOTE 7). |
| NOTE 5(a): self-test wording | **Fixed.** | **N8:** a refused run still leaves `ckpt/` and the lock file. The self-test now says "(the local lock file aside)". |
| NOTE 5(b): fd leak in `CallLog.__init__` | **Fixed.** | **N9:** open fds go 5 → 5. |
| NOTE 5(c): a failed STOP line's detail | **Fixed** while the end line is written. | **S13:** the end line's `stop_line_failed` carries `log_error`, `returned_text` and `stored_text`. If the end line also fails, the detail is lost and the marker has none (NOTE 4). |
| NOTE 5(d): the lock refusal's label | **Fixed.** | The run's refusal reads "G-TIME-OLMo-sft (p) REFUSED: another process holds the stage's lock ...". `time-report`'s reads "time-report (G-TIME-OLMo-sft (p)) REFUSED: ...". |

**Round 4's draft-entry claims, against the current draft (`podwatch/step6_build_entry.md`, 01:53)**
- **Fixed (6):**
  - the round-3 MINOR 1 paragraph now points forward to round 4;
  - round-3 NOTE 2's "A failure before the renames writes nothing" is now true (temps no longer block);
  - round-3 NOTE 4 and "Throughout" now cover `time-report` and the nfs4 volume;
  - the round-2 M-1 over-claim is now "Rounds 3 and 4 then found and closed further gaps ...; the residual is the STOP PIN's";
  - "(never read as an empty record)" is now true (A4);
  - the way out names all three files. S16: with all three moved aside, a plain run PASSes as run 1. X3 and X3b: with fewer moved, the run is refused.
- **Accurate, as before (3):** the round-3 MAJOR; MINORs 2 and 3; THE STAGE's lock list.
- **Still open (1):** the placeholders `@@STAMP@@`, `@@E9SHA@@`, `@@GANL@@`, `@@PKG@@` and `@@CHECKS@@`. Today's `p_sessions` count is 168/168 (round 4: 166).
- **The draft's round-4 bullets:**
  - m-1: accurate for one Ctrl-C (S1) and for the echo. A second Ctrl-C at the end line drops both records (W2).
  - m-2: accurate, but it cites a raw that is not in the tree (NOTE 6).
  - NOTE 1's "The rename needs no new space": true. The EIO case is stated nowhere.
  - NOTE 4's "the part-written case is stated": true of the docstring, not of the analyzer's refusal text.
  - "The STOP" residual, "a process killed between an m-raised STOP and the rename", is too narrow (NOTE 1).

**Round 4's experiments re-run on the current code** (rev5/exp_*4_r5.py, the paths moved to rev5)

*exp_items4*
- A1–A3, B1–B3, C and D1 hold as in round 4.
- A4 is now refused (in round 4 it PASSed).
- D2 still trips entry (7)'s identity check, as its seam did in round 4.

*exp_new4*
- **N2 and N2b: now refused (both PASSed in round 4).** The marker seam no longer fires, and ENOSPC at the end line is held by the renamed marker.
- **N1 and N1b:** their seam (a Ctrl-C inside the marker's `write_once_bytes`) no longer applies. The analog, S1, holds.
- **N3: still PASSes,** but its files (the marker's temp) cannot arise now. Its analog is a SIGKILL just before the rename, the PIN's residual.
- **N4: still PASSes,** a seam artifact; S13 holds.
- **N5:** holds.
- **N6: still writes,** because it bypasses the driver; L5 holds.
- **N7a–e:** all are now labelled StageRefusals. N7c and N7e were raw errors in round 4; N7d read "holds".
- **N8:** the same footprint as before.
- **N9:** fixed.
- **N10:** holds.

*exp_misc4*
- N1a–d and N3 hold.
- N2a is fixed.
- N2c: the retry completes the set.
- N2d: the refusal is reworded.

*exp_extra4*
- X1–X3b hold.

*exp_tail4*
- T3 and T4 hold.
- T1 and T2's marker seam no longer fires (the marker is present and the run refused). The analogs are S4 and S5.

*exp_blind4, exp_hair4*
- Both outputs are identical to round 4's, and every group's reports and closing lines are identical.

#### New findings

##### MAJOR

None.

##### MINOR

**m-1. When both STOP records fail, the stage stays resumable, and the last stdout line says the STOP is recorded.**
- **Where:**
  - <repo>/valence_core/p/stage.py:820-828, the two echoes in the inner `finally`;
  - the PIN, stage.py:59-61.
- **What:** `P-STOP MARKER {marker}: the STOP rests on the call log's end line alone` prints whenever the marker is not in place, including when the end line failed too.
  - It then follows "THIS STOP IS NOT RECORDED -- nothing may resume without the seat".
  - That is exactly the case where stdout is the only record, and the box wrapper sends stdout to the same volume.
  - The PIN states only the killed-process residual.
- **Scenario:** each of the following leaves no marker, no end line and `reserve-1` behind. `--resume` then PASSes, and the echo prints "...END NOT WRITTEN (...); THIS STOP IS NOT RECORDED..." followed by "P-STOP MARKER NOT IN PLACE (...): the STOP rests on the call log's end line alone".
  - **S5:** EIO at the rename and at the end line.
  - **S5b:** EIO at the rename, then a Ctrl-C at the end line.
  - **W2:** a Ctrl-C at the rename, then a second at the end line.
- **Fix:**
  1. Track `end_written`, and print the "rests on" line only when it is true.
  2. In the double failure, print one line to both stdout and stderr naming both failures.
  3. State this residual in the PIN.
  4. Optionally, hold SIGINT (`signal.pthread_sigmask`) from the inner `finally`'s first statement until the end line has been attempted. This also closes **W1**: a Ctrl-C before `stop` is computed leaves `stop` False, so the outer `finally` unlinks the reservation, nothing is recorded, and `--resume` PASSes.

##### NOTE

1. **The PIN's residual is narrower than the code's.**
   - **Where:** <repo>/valence_core/p/stage.py:59-61 ("its STOP raised by m's code"), and the draft's "an m-raised STOP".
   - **What:** a STOP that p raises has the same window: a StageStop, KeysStop, ScheduleStop or RegisterStop inside m's stage, or the backend StageStop. With a SIGKILL just before the rename (a p StageStop raised inside m's stage), there is no marker and no end line, and `--resume` PASSes. Only a ProxyStop whose STOP line was written survives (refused).
   - **Window:** short in every case, because m's production stage path does no cleanup I/O on the exception path (grep: its only `finally` sits in a self-test).
   - **Fix:** reword the residual as "any STOP but a ProxyStop whose STOP line was written".
   - **Also:** <repo>/scripts/p_sessions.py:55 lists `time-report`'s exit 2 as "(the report exists, or no p unit)". The lock refusals exit 2 as well (L4): held, unavailable, cannot be opened, a link in its path.

2. **The end line misreports a marker that is in place.**
   - **Where:** <repo>/valence_core/p/stage.py:797-806. Any exception in the `try` sets `NOT IN PLACE`, including one raised after a successful rename.
   - **Scenario:**
     - **S2:** a Ctrl-C in the directory fsync.
     - **S3:** an NFS rename that succeeds on the server but reports ENOENT on retransmission.
     - In both, the marker stands and `--resume` is refused. But the end line records `"stop_marker": "NOT IN PLACE (...)"`, and the echo says the STOP "rests on the call log's end line alone".
   - **Effect:** fail-safe, but the record is false.
   - **Fix:** in the `except`, test `pp["p_stopped"].exists()`, and when it is there record "renamed into place (directory fsync failed: ...)".

3. **Stale reservations are never read or removed, and a refusal can delete one it did not write.**
   - **Where:** <repo>/valence_core/p/stage.py:834-838, and nothing reads `*.reserve-*`.
   - **What leaves one behind:** a SIGKILL mid-session, a SIGKILL before the rename, and S5 each leave `reserve-k` beside a run with no end line. The file outlives the resumed PASS, and it is the only trace that distinguishes S5 and W2 from a clean exit.
   - **S9:** a stale `reserve-1` with other bytes refuses the run ("the STOP's record cannot be reserved"). The outer `finally` then unlinks it, and the retry PASSes.
   - **Fix:**
     - unlink only a reservation this run wrote;
     - at a run's start, name the stale reservations of runs with no end line, in a line or a run-line field, for the seat;
     - the seat may choose to make them refuse.

4. **The marker no longer carries the STOP's cause.**
   - **Where:** <repo>/valence_core/p/stage.py:765-769. The marker is the reservation's text: "the exception's type and message are in the run's end line, when it is written".
   - **Scenario:** when the end line fails (B1, N2: ENOSPC), the seat gets the fact of a STOP and its run number. The cause is on stdout alone, which the box wrapper writes to the same full volume.
   - **Assessment:** better than round 4, which recorded nothing, but the class of the STOP can be lost.
   - **Fix (optional):** pad the reservation's `detail` with about 4 KiB of spaces. After the rename, overwrite the padding in place with the type and the start of the message (`pwrite`, then `fsync`; no new blocks), best-effort.

5. **A write that fails before any byte still marks the tail dirty.**
   - **Where:** <repo>/valence_core/p/stage.py:448. `dirty` is set before the first `os.write`.
   - **Scenario (S14):** ENOSPC on a call line's first `os.write` (nothing written), then the end line.
     - The log gains a blank line, which `read_calls` counts as "not JSON".
     - The resumed PASS report reads `well_formed: false`, `n_malformed_lines: 1`, though nothing was torn.
   - **Fix:** set `dirty` only after a short write (bytes written, bytes left), or count empty lines apart from malformed ones.

6. **The flock probe.**
   - **(a) The cited raw is not in the tree.** <repo>/valence_core/p/stage.py:532 and the draft cite `results/raw/2026-11-09_p-step6_flock-probe.txt`. Only <tmp>/scratchpad/podwatch/flock_probe_raw.txt exists, so the raw must land in or before the build commit.
   - **(b) Cross-pod exclusion is unprobed.**
     - The probe ran within one pod, so on one NFS client.
     - It kept only three mount fields (`split()[:3]`), dropping the options.
     - So whether flock reaches the server (the `local_lock=` option), and so excludes a second pod on the same volume, is not shown.
   - **(c) An NFSv4 lock can outlive its pod.** The lock of an abruptly terminated pod persists for the server's lease. A run on a respawned pod within the lease reads "another process holds the stage's lock": fail-closed, but misattributed.
   - **Fix:**
     - commit the raw;
     - record the mount options in the BACKEND entry;
     - word the PIN as "exclusive across processes on one pod".

7. **`write_once_all` and the analyzer's refusal.**
   - **(a) O_TRUNC gives up a concurrency guard.**
     - **Where:** <repo>/valence_core/p/guard.py:212.
     - **What:** O_TRUNC reopens what O_EXCL had closed. Two concurrent `p_analyze` runs writing one set can interleave bytes in a shared temp before one of them renames it.
     - **Why it matters:** `p_analyze` holds no lock, and a second session may share the tree.
   - **(b) The refusal does not say the set is part-written.**
     - **Where:** <repo>/valence_core/p/analysis.py:204-209.
     - **What:** the N-9 refusal on a part-written set (N2d) reads "the record stands -- ... unless the seat rules the set incomplete". It does not say that `V2.json` is missing and `V2.json.tmp` was left.
   - **(c) Where the refusal comes from.**
     - **Where:** guard.py:190.
     - **What:** "A re-run is then refused" holds only through `run_staged` (m's write-once check). `write_once_all` itself completes the set on a retry (N2c).
   - **Fix:**
     - in the N-9 branch, list each output that is missing or has a `.tmp` sibling, and say "part-written";
     - for (a), take an flock over the write phase, or keep O_EXCL with a GuardStop that names the stale temp.

#### Checked and sound

- **The STOP record on its normal paths.** A ProxyStop, an m-style SystemExit, and every log write failing with ENOSPC: the marker is in place and no reservation is left (self-test; N2/N2b; B1/B2).
- **The reservation's order.** It is written under the lock, inside the substitutions, before the log opens and before the factory is called. A refusal there loads nothing.
- **A torn run line (S10).** The reservation is released and a plain run is refused (the log exists). `--resume` reuses run 1 and PASSes, with one malformed line.
- **A SIGKILL after the reservation and the log's open.** The identical stale reservation is reused, then released.
- **The marker and a reservation together (S11).** Refused by the marker; no file touched.
- **A rename that fails.** EXDEV or EPERM (S4): held by the end line, refused.
- **Atomicity.** On Linux nfs4 and on macOS, a crash leaves either the reservation or the marker, never a torn marker. A spurious ENOENT after a successful rename fails safe (NOTE 2).
- **A Ctrl-C after the rename (W3, in term (d)'s state).** The marker holds.
- **A STOP from the report write after m returned (S18, N5).** No marker and no reservation. m's end refuses re-runs, and `time-report` re-derives the report.
- **`stage_lock`'s errno mapping, on both platforms.** Python maps exception classes by errno name. flock's "held" is EWOULDBLOCK. Linux NFS maps NFS4ERR_DENIED to EAGAIN and retries GRACE and DELAY.
- **`time-report` under the lock (L4).**
  - Exit 2: a non-unit; the report exists; the lock held; ENOLCK; a symlinked lock (no target created).
  - Exit 4: no ended stage; a STOPPED stage.
  - Exit 0: an ended stage. Its re-derived report differs from the run's only in `root`, an artefact of the patched `DEFAULT_OUT_P`.
- **The dirty tail (S14b).** An empty write on a clean tail writes nothing, and a clean file opens not dirty.
- **gitignore.** `*.reserve-*` and their `.tmp` files are ignored. The marker, the call logs and the reports are admitted, and the marker is `-diff`.
- **Blinding:** unchanged (exp_blind4, exp_hair4).
- **The declared way out (S16):** holds.

#### Counts

- **Round-4 items:**
  - m-1: fixed (its residual's scope is NOTE 1);
  - m-2: fixed;
  - NOTE 2 and NOTE 3: fixed;
  - NOTE 5 (a)–(d): fixed, (c) while the end line is written;
  - NOTE 1 and NOTE 4: partly fixed.
- **Round 4's draft-entry claims:** 6 fixed, 3 accurate as before, 1 open (the placeholders, by design).
- **New:** MAJOR 0, MINOR 1, NOTE 7.

#### Commands run

1. `git status --short` at the start and the end (saved and diffed); `git rev-parse HEAD`.
2. `git diff` of `guard.py`, `.gitignore`, `.gitattributes` and `scripts/p_sessions.py`.
3. `git check-ignore -q` on the marker, the reservations (`reserve-1`, `reserve-12`, `reserve-1.tmp`), the lock, the marker's `.tmp`, the call log, the report and m's checkpoint. `git check-attr -a` on the marker and a reservation.
4. **Reads:**
   - `stage.py` in full;
   - `guard.py`'s write helpers;
   - `analysis.py`'s `run_staged`;
   - `proxy.py`;
   - `register.single_thread_state`;
   - m's `resume._fsync_dir` and `persist_end`, and `stages.run_gate_stage` / `_finish_gate`, read only;
   - the draft entry;
   - the flock probe's raw and script;
   - `run_gtime_p.sh`.
5. **grep:** the callers of `write_once_*`; m's `finally`/`except` handlers on the exception path; the cited raw in `results/raw`.
6. `nice -n 19 jlens-qwen36/.venv/bin/python -B scripts/p_sessions.py --selftest`: 168/168, exit 0.
7. Round 4's seven experiments, re-run as `rev5/exp_{items,new,misc,extra,tail,blind,hair}4_r5.py`, with `rev5/rev5_common.py` copied from round 4's helper.
8. `rev5/exp_stop5.py`: S1–S5b, S9–S11, S13–S14b, S16, S18.
9. `rev5/exp_kill5.py` with `rev5/kill_runner.py`: a SIGKILL in subprocesses at six points.
10. `rev5/exp_lock5.py`: L1–L5.
11. `rev5/exp_window5.py`: W1–W3.
12. `diff` of L4's two reports (they differ in `root` only).
