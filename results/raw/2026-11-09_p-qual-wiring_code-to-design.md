# G-F0m-OLMo (p) is not wired: B5's chain stops before LOCK-p v0.2 — four questions for the seat (Code → design)

*Code's raw (the pod/p session), PI date 2026-11-09. On the PI's routing of 2026-11-09 (evening), item B5, relayed by
the coordinating session, and the seat's answer on G-TIME-OLMo (p)
(`results/raw/2026-11-09_p-gtime_design-to-code_answers.md`, sha256 `7b8b1d5f…adc3`), §2 and §6. `p:N` is line N of
PROPOSAL-p v0.2; `m:N` is line N of PROPOSAL-m v1.11; code and lock lines are at `9eed029`. Nothing was built and
nothing ran on a model or the box. Nothing is pushed.*

## 0. The short form

B5 routes: "LOCK-p v0.2 ×3 committed by path; then G-F0m-OLMo (p) ×3 on the box, batched (24 sessions per
checkpoint), then STOP for the seat's read [go]". The run cannot be made on p's code as committed, and a lock
committed first cannot license it:

- **G-F0m-OLMo (p) has no path in p's package.** p's stage runs m's gate `time` only, and the driver refuses `qual`
  (§1).
- **Wiring it moves values the lock must name.** The wiring edits p's stage module and the driver. That moves p's
  `package_sha256` and the driver's sha256, both of which `stage.lock_required` lists, and it makes G-SHAPE-p's and
  G-ANL-p's artifacts stale by the stage's own checks. The stage would refuse a LOCK-p v0.2 committed before the
  wiring, before any load (§2).
- **The gap is Code's.** The step-6 BUILD wired `time` alone and said so only in the driver. Neither the BUILD entry
  nor Code's G-TIME block (`2258c52`) raised it, and the seat's answers plan LOCK-p v0.2 → G-F0m-OLMo (p) directly
  (§3).

**B5's "LOCK-p v0.2 ×3 committed by path" and the three runs are held for the seat's order ruling. LOCK-p v0.2 stays
a scratch draft, and nothing is built.** Four questions (§4): the order (Q1), the move's scope (Q2), the lock's form
after a move (Q3), and the read B3's counter needs (Q4).

## 1. What stops it

**1.1 p's stage is G-TIME's alone** (`valence_core/p/stage.py`):

- `:4`, the module docstring: "m's ``stages.run_gate_stage`` with gate ``time`` (m:302: two sessions, one per arm,
  uncached)";
- `:109`, `GATE = "time"`;
- `:315–317`, `templates_counts` returns one session per arm (m:302's G-TIME form);
- `:420–428`, `out_paths` names the call log, the STOPPED marker, the lock file and p's report `{unit}_{GATE}_p…`,
  so `_time_`;
- `:744`, `run_time` is the only stage entry point, and it runs m's stage with `GATE`;
- nothing in it passes m's `prior_ckpt`. m's qualification stage requires it: `run_gate_stage`'s docstring
  (`valence_core/m/stages.py:1449–1460`), `PRIOR_STAGE`'s `"qual": "time"` (`:644`), `prior_gate` (`:784`).

**1.2 The driver refuses `qual`** (`scripts/p_sessions.py`), exit 2:

- `:95–98`: `STAGE_CMDS = ("qual", "campaign")`; `STAGE_AFTER`'s `"qual"` is "its checkpoint's LOCK-p v0.2";
- `:59–60`, the docstring: "and refuses ``qual`` and ``campaign`` (G-F0m-OLMo (p), the campaign): each is wired
  after its checkpoint's LOCK-p v0.2 or v1.0, on its own word.";
- `:326–329`, the driver's self-test asserts both refusals.

**1.3 Nothing is missing on m's side or in p's data.**

- m's OLMo qualification stage exists: `valence_core/m/stages.py:154`, `GATES = ("time", "qual")`.
- m's driver requires, for an OLMo qualification, the lock line `G-TIME-OLMo-{ckpt} port acceptance recorded`
  (`scripts/m_sessions.py:680`, `OLMO_QUAL_LOCK_LINE`; the check at `:933`).
- p's schedules hold the qualification files, in the manifest LOCK-p v0.1 names: per checkpoint
  `data/p/schedules/OLMo-{ckpt}_qual_A0-OLMo-{ckpt}.json` (n 8) and `…_qual_A0s-OLMo-{ckpt}.json` (n 16).

## 2. Why LOCK-p v0.2 cannot come first

The stage's precheck refuses unless the lock at HEAD names, verbatim, every value `stage.lock_required` lists
(`stage.py:236–298`), computed from the code at the run. Five of them move with the wiring:

- **p's `package_sha256`** (`guard.package_sha256()`): the wiring edits `valence_core/p/stage.py`.
- **p's licence line** (`LICENCE valence_core/p package_sha256 …`, from `guard.licence_lines()`, `stage.py:294–295`),
  which carries the same package hash.
- **The driver's sha256** ("the driver (scripts/p_sessions.py)", `guard.driver_sha256()`): the wiring edits the
  driver.
- **G-SHAPE-p's artifact.** `lock_required` runs `stale_problems` on its recorded p and m packages and
  `gshape_drift_problems` on its recorded sources map and import closure. The driver is in G-SHAPE-p's sources map
  (`valence_core/p/gshape.py:90`, `TOOLING_FILES`), so either edit makes the artifact stale, and G-SHAPE-p must be
  re-run.
- **G-ANL-p's artifact.** `stale_problems` runs on its recorded p and m packages and both analyzers, so the package
  edit makes it stale, and G-ANL-p must be re-run.

A LOCK-p v0.2 committed now would name the current values. After the wiring, G-F0m-OLMo (p)'s precheck would refuse
it, exit 2, before the load.

The m precedent does not carry, for two reasons:

- **m's lock records the driver after the run; it does not test it.** m's driver checks that it is committed
  unmodified and prints its sha256 on the DRIVER line (`driver_problems`, `scripts/m_sessions.py:983–1000`; the DRIVER
  line at `:1739` for the OLMo stages). The value
  then goes into the stage's entry and the next lock revision. LOCK-m-F0 v0.2 §3 records m's driver at its tree and
  quotes the step-10 read's Q3: "Nothing tests a driver hash as a substring". Its rule for later driver edits put the
  `qual` wiring's blob in "the next lock revision — v0.2 for `id`, v1.0 for `qual`". So m's `qual` wiring could
  follow v0.2 (m:358's step 14). Code's departure there, in the step-14 entry's ping Q4, was starting that wiring
  before v0.2's commit.
- **m's wiring was the driver's alone.** The same rule required "no change under `valence_core/m`", because m's stage
  functions already ran `qual`. p's stage module runs `time` only, so p's wiring moves p's package.

p's stage tests the lock against the running code. `lock_required` lists p's package and the driver at every
version, and the precheck refuses a lock that does not name them (`stage.py:365–371`, then `:389–390`).

## 3. The gap (Code's)

- The step-6 pre-build block proposed register entry (6) "for every p gate stage and the campaign", and the seat
  declared it so (`de729c4`, §1, Q1). The seat's order (the same answer, §4) called the step-6 package final
  ("G-SHAPE-p re-run on the final package") and runs LOCK v0.2 → G-F0m-OLMo (p) directly.
- The step-6 BUILD (`d215d5b`) wired `time` alone. It said so in the driver's docstring and self-test only, not in
  the BUILD entry.
- Code's G-TIME block (`2258c52`) asked about LOCK-p v0.2's contents (Q2) and did not say that G-F0m-OLMo (p) needs
  a build first.
- So the seat's answers and the PI's B5 route a run the code cannot make. Code found it at B5's LOCK-p v0.2 step,
  before any code edit.

## 4. The questions

**Q1. The order.** Code's proposal:

1. the `qual` wiring, a p package move (Q2's scope), built only on the PI's word;
2. p's self-tests, m's battery and G-ANL-p's groups; blind review rounds and a values-check, as the step-6 BUILD had
   them;
3. G-SHAPE-p re-run, `fdd79d8`'s artifact superseded in F-p12's form (moved aside with `git mv`, kept in history);
4. G-ANL-p re-run, `f8b16d5`'s artifact superseded in the same form;
5. LOCK-p v0.2 ×3 to the answer's §2, its values generated on the moved code (Q3);
6. G-F0m-OLMo (p) ×3 on the box, batched as G-TIME was (the three checkpoints back to back), 24 sessions per
   checkpoint, uncached;
7. STOP for the seat's read.

With the move, the seat's §4 applies as written:

- (h): "The stage's PIN (`stage.py:36–38`) and the BUILD entry's (h) are left as written until the next package
  move, where the wording follows". The PIN's wording follows §2 item 6's form.
- (j): "deferred to the next package move, if one comes before the campaigns". This move comes before them, so the
  fix (a fresh-interpreter closure for p's drift check) lands with it.

For the seat: this order, or another.

**Q2. The move's scope.**

- **(A) `qual` alone** (Code's recommendation), wired as `time` was:
  - the gate a parameter of p's stage (`time` | `qual`), with m's counts from the committed gate files (8 + 16);
  - G-TIME (p)'s checkpoint passed to m's stage as the prior. m's `prior_gate` checks that it ended PASS, is this
    unit's, carries m's proposal pin (F-p8) and is not the stub's;
  - the lock's v0.2 line checked before the load (Q3);
  - the call log, marker, lock file and p's report under `_qual_` names;
  - p's report over the 24 sessions, on the seat's read domain: the proxy attribution over the sixteen sham
    sessions, and every contrast count withheld, as at G-TIME;
  - the driver's `qual` and `qual-report`, as `time` and `time-report`;
  - `time`'s behaviour unchanged (its records stand), and `campaign` still refused;
  - no `prior_adjudication` input. All three G-TIME stages PASSed, so a PAUSE has no path in this build.
- **(B) `qual` and the campaign in one move,** with one G-SHAPE-p and G-ANL-p re-run before both v0.2 and v1.0.
  - The campaign's wiring is the larger build: m's OLMo campaign was never wired either, and its looks and cap come
    from m:330 and G-PWR.
  - It would hold G-F0m-OLMo (p) behind it.
- Under (A), the campaign's wiring is its own move before v1.0, with its own two re-runs.

**Q3. The lock's form after a move.** §2 has each lock "re-issued above its v0.1 text kept verbatim". After the move,
v0.1's text names the superseded package, driver, G-SHAPE-p and G-ANL-p values. Code's form:

- v0.2's header and §2's eight items;
- then the values of record at v0.2: every value `lock_required` lists on the moved code, in the generator's form;
- then v0.1's text verbatim, under one line saying that where its values differ from v0.2's, v0.2's are of record;
- one `BACKEND OF RECORD` line in the file, v0.1's, unchanged (`641ee466f4553b6a`), since the precheck requires
  exactly one;
- item 1 (the acceptance) carries the line `G-TIME-OLMo-{ckpt} port acceptance recorded` as a whole line. It is the
  text of m's `OLMO_QUAL_LOCK_LINE` (`scripts/m_sessions.py:680`), since p's records keep m's unit strings (p:84).
  p's `qual` precheck would require it (Q2 (A)), as m's driver does for m's units.

For the seat: this form, or another.

**Q4. B3's read and the list of record.**

- B3 routes the `task_correct` counter as "Code's own step at each entry"; the answer's §3 has it "Tabulated by
  Code's own step from the records at each entry".
- The sham sessions' rounds are in m's reads files, `data/p/reports/OLMo-{ckpt}_{stage}_reads.json`.
- The list of record's item 2 bars, on those files, `json.load` "or any read of their content outside the stage's
  own code, G-VER, the analyzer, the seat's read of the reports, and the pre-push screen of item 4". Code's step is
  none of the five.
- **Code's reading:** B3 is the seat's licence for that one read. It covers the reads files' sham sessions only,
  never the checkpoint, the call log or a contrast session, and prints k of n per checkpoint and phase and nothing
  else.
- **The same question covers the figures a stage entry takes from m's and p's reports,** as the G-TIME entry's table
  did. Code's reading: the reports are the read domain (m:271), and reading them for the entry is part of the read.

For the seat's word before the G-F0m-OLMo (p) entry.

## 5. The pod

- Pod `qny1x4v8padeke` stays up and idle on the PI's answer, verbatim (PI date 2026-11-09, in chat): "Keep it up".
  It replied to the coordinating session's question "Keep the pod up through G-F0m-OLMo (p)?", which that session's
  closing message had asked as "Should I keep the pod up through G-F0m-OLMo (p) (my recommendation), or stop it
  now?". B5 says the same: "The pod stays up through G-F0m-OLMo (p) [up]."
- The run is now behind a build, its reviews, two gate re-runs and three locks, each after the seat's word and the
  PI's routing. Idle, the pod costs $1.79/hr, about $43 a day.
- Whether it stays up meanwhile is the PI's call. Code changes nothing on the box.

## 6. Meanwhile

- Committed before this block, at `e619d3d`: the seat's answer, with the close line on the G-TIME entry,
  (h)'s dated note on the BUILD entry, and the close line on this session's disclosure entry (C4).
- LOCK-p v0.2 ×3's §2 text is drafted in scratch, not committed. Its values wait on the code.
- Nothing is built or run. The box repo stays at `0afd842`, with G-TIME's fifteen outputs untracked, identical to
  `2258c52`'s.

*Nothing follows until the seat answers and the PI routes. The list of record (the sweeps ruling of 2026-11-09, §2)
binds this session and every brief it writes. Nothing is pushed.*
