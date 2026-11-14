# PROPOSAL-p -- the campaign wiring's BUILD: blind reviews (Code's reviewer, rounds 1-3)

*Code's raw, PI date 2026-11-14. 3 blind review rounds of the uncommitted campaign wiring (`valence_core/p/stage.py`, `scripts/p_sessions.py`; the seat's read of G-F0m-OLMo (p) x3, `results/raw/2026-11-12_p-qual_design-to-code_answers.md`, §4.3 item 2), by one reviewer continued from round to round. It worked read-only against the main checkout at HEAD `3e1b614`, in scratch: copies of the two files, and mutants each loaded as `valence_core.p.stage` (or as the driver) with the real `__file__`, in a fresh process. It edited no repository file. Round 1's brief quoted the list of record v2's items 1-5 verbatim; rounds 2 and 3 were sent under the same rules. Each report is verbatim, with the hand-back's frame removed and local paths scrubbed (`<repo>`, `<tmp>`), its headings set two levels down under its round's heading. Code's dispositions follow each round; Code applied or declared every finding before the next round, and the last round's before the commit.*

## Round 1

### Blind review: the campaign wiring (uncommitted `valence_core/p/stage.py` and `scripts/p_sessions.py`)

**Bottom line:** one MAJOR finding, four MINOR, seven NOTEs. 48 mutants: 21 killed, 27 survived. Of the survivors, 4 are equivalent and 23 are test gaps; one of those gaps (S3) predates this change.

**What I reviewed**
- `valence_core/p/stage.py`, sha256 9f8ed822f62059bbecf0b01ea3f91ea8b5761e01e9a5ecd64bbf5de5b64263b5
- `scripts/p_sessions.py`, sha256 4d1d3d1e79d338d016eaa945412c0b6b7e0fffb69d029c8f7a406d8daeea9f25
- The baseline was HEAD 3e1b614. Both files hashed the same at the end of the review, and `git status` was unchanged.

**Baselines**
- `scripts/p_sessions.py --selftest`: 195/195.
- My harness, which runs the stage and driver self-tests on the unmodified sources: 65/65 (48 stage, 17 driver).

#### Findings

**MAJOR-1: when the end look fires at a terminal end, p's report records the wrong status.**
- **What m does.** For COMPLETE, CAP, or a PI stop at a launch count that is not a multiple of 40, m evaluates the end look. If it fires, `_campaign_end` returns status PAUSE while the terminal state stands. The checkpoint then holds the terminal plus an unadjudicated `end_look` pause, m's report says PAUSE, and the run returns PAUSE (exit 3).
- **What p does.** p's `campaign_state` reads "ended", and `build_report` takes `m_resume.ended_status`, which is the terminal's status.
- **Probe.** I added one case to a scratch copy of the stage self-test, patching `m_stages.campaign_look` so the "end" evaluation fires, on m's scripted double. Results:
  - run status PAUSE; m's report status PAUSE;
  - terminal {COMPLETE, 112}; last pause {end_look, 112, adjudication None};
  - **p's report status COMPLETE**;
  - a later `--resume` is refused ("p's report exists").
- **Consequences.**
  - The driver prints "P-REPORT campaign-OLMo-sft (p): COMPLETE" and exits 3.
  - Where `campaign-report` writes the record instead (for example after the run's write failed), it exits 0 (EXIT_CODES["COMPLETE"]).
  - So p's record disagrees with m's report, and the escalation depends on which path wrote the record. At the gates, a PAUSE is recorded as PAUSE.
  - No self-test covers this case: B3 survives.
- **Fix.** At the campaign, record m's status for that end: PAUSE when the terminal campaign's last pause is an unadjudicated `end_look` (or take `status` from m's report, which p already names and hashes). Keep the terminal status beside it. Add this case to the self-test, with exit 3 from both the run and `campaign-report`.

**MINOR-1: `run_gate` no longer refuses the campaign.**
- The precheck now admits STAGES, and `run_gate` relied on it to reject non-gates.
- **Probe.** `run_gate("OLMo-sft", "campaign", ...)` on the stub (cap 40, qualified root):
  - the adapter factory is called (the model load, off the stub);
  - `OLMo-sft_campaign_p-calls.jsonl` is created, with a run line "campaign-OLMo-sft (p)" and an end line carrying KeyError;
  - `KeyError('campaign')` is raised from `templates_counts` (`COUNTS[gate]`).
- At HEAD this was refused before anything ran. The driver never routes `campaign` to `run_gate`, so this is latent, but the stray log would turn the real campaign's first run into a `--resume`.
- **Fix.** `run_gate` refuses any gate not in GATES before the precheck; keep a self-test case for it.

**MINOR-2: the hour cap must be a whole number.**
- `campaign_hour_cap` accepts only `type(v) is int and v > 0`. m's `hour_cap_exceeded` takes int, float, str or Fraction hours (`resume._q`).
- A cap share of, say, 4.5 h is treated as unset: the precheck says "the hour cap is not set", which is misleading.
- The `> 0` guard itself is correct but untested (V6 survives; a 0 cap would reach m after the load).
- **Fix.** Accept the positive numbers m accepts (not bool) and format the lock line from the same value. Alternatively, declare whole hours in the PIN and give a set-but-not-integer value its own refusal message.

**MINOR-3: the driver's campaign path is untested past the ruling files.**
- Both driver campaign cases stop at `ruling_texts`. Nothing reaches the precheck call, the DRIVER/WEIGHTS/RULING lines, the arguments passed to `stage.run_campaign`, the exit mapping, or `_say`.
- Survivors: D1, D2, D4, D5, D6, D9. Two matter most:
  - D4 prints a ruling's text in the RULING line, which the PIN forbids.
  - D5 makes `campaign-report` re-derive the qualification's report. Its only test case is a non-unit refusal, which happens before the gate is chosen.
- **Fix.** Add the gates' "simulated clear box" case for `campaign`: stand-in precheck and weights check, a recorder in place of `stage.run_campaign`, the loader trapped, `--resume` and both ruling files. Check:
  - the DRIVER < WEIGHTS < RULING order;
  - that the RULING line shows sha16s and never a text;
  - the keyword arguments: adjudication, pi_stop, resume, stub False, the pre at campaign;
  - exit 3 on PAUSE, 2 on a StageRefusal, 4 on a SystemExit;
  - a TOTALS probe printed through `_say`.
  Also add `campaign-report` to the `rr_ok` loop.

**MINOR-4: the stage's campaign refusals and the precheck's binding to the lock and G-PWR are untested.**
- THE STOP PIN treats any SystemExit inside m's stage as a STOP (a marker, then the seat). So the pre-load refusals R6 (an unreadable checkpoint) and R8 (a ruling that does not fit) are what stop a misfit ruling or a damaged checkpoint from loading the model and ending in a STOP marker. Neither is exercised.
- L3, L4 and G3 are the only binding between the lock and G-PWR (p)'s record, and between the lock and the campaign lines. The precheck's non-stub path never runs at `campaign` in either self-test.
- Other survivors:
  - R2/R3: the only STOP case leaves both the marker and the stop mark on the end line, so each guard masks the other.
  - R9, G1, G2, C2, C3, C4, LB1.
  - C2–C4 are self-test gaps only: the code matches m (see "What holds", item 2).
- **Fix.** Add run cases, each refused before the factory is called: an unreadable checkpoint, NO PAUSE TO ADJUDICATE, RULING REUSED, CHECKPOINT MISMATCH, and dirty schedules. Add a precheck-at-campaign case over a stand-in committed lock and G-PWR record (patch `m_stages._committed`), gpwr perturbations of the sham count and the schema, and the three remaining ruling branches.

**NOTE-1: an unexpected state after a normal return writes no report, silently.**
If the state after a normal return is "unreadable" or "pending" rather than open or ended, the run returns without a report. The driver then prints "P-CAMPAIGN …: COMPLETE; p's report is written once the campaign has ended" and exits by m's status (0). Suggested fix: on "open", no report; on anything other than "ended", raise a StageStop that names the inconsistency.

**NOTE-2: `campaign-report` lines are not redacted.**
Its REFUSED and STOP lines print through `gate_report` without `redact_totals`, yet the driver docstring says every campaign REFUSED/STOP line passes through it. `build_report` reads with `json.loads`, with no `_check_state`, so no totals line can arise there. Either narrow the claim or use `_say` there.

**NOTE-3: no restart route after a box change.**
m:302 and m:251 say a box change mid-campaign "restarts" the campaign; m's own message says "at a NEW checkpoint path". p passes no `ckpt_path` and names its call log and marker per unit. So a `--resume` on a new pod reaches m's CHECKPOINT MISMATCH (pod_id) after the load, which becomes a p STOP. That is safe, but undeclared: it needs a sentence in THE CAMPAIGN PIN, or the seat's word.

**NOTE-4: departures from m's driver for the seat to see.**
- (a) A later run always needs `--resume`. m shows a paused campaign "with or without --resume" and re-finishes a pending end "whatever resume says". This one is declared.
- (b) The RULING line prints before the state and ruling refusals, and drops `ruling_line`'s "offered for the pause at …" clause and its "already records" note. So a RULING line can precede the refusal of that same ruling.
- (c) The campaign lines are whole lines; m uses substrings. This is stricter.
- (d) The campaign report reuses the gates' read domain under ruling (h). m:318 applies; this is the seat's call.

**NOTE-5: leftover text.**
- The docstrings still name only `time-report`/`qual-report`: THE CALL LOG (line 94), P'S REPORT (line 114, which also says "m's report and reads"), and `stage_lock` (line 816).
- "The self-test plants … at each gate" has no campaign case.
- The `prior_problems` docstring still says "G-TIME (p)'s checkpoint".
- `STAGE_NAMES` in `p_sessions.py` is now unused.
- The `git check-ignore` self-test case covers GATES only. My probe of the 18 campaign outputs (p's call logs, markers and reports; m's checkpoints, excerpts and reports) found all admitted, and the 6 lock/reservation paths ignored: correct today, untested.

**NOTE-6: one early campaign failure skips the rest of the stage self-test.**
The campaign cases read m's checkpoint unconditionally (`ck_p = m_ck(rcp)`, `m_ck(rcs)`). An early campaign failure raises FileNotFoundError and the remaining stage checks are skipped (seen with R10 and S4). The run still fails, so the mutant is still caught; only the count drops.

**NOTE-7: two survivors predate this change.**
- S2 is equivalent: m's production path catches no SystemExit, so `stop_in` already sees every ProxyStop.
- S3 is a gap shared with the gates: the backend comparison never runs on the stub.

#### What holds

1. **`_run_recorded` is HEAD's code.** Its body equals HEAD's except `gate`→`stage` at 3 sites and the m call →`call_m(px)`. The gate's lambda makes the same call with the same values inside the same `try`, and `write_report` still follows it. Gate behaviour is identical; every gate check passes.
2. **m's driver is mirrored faithfully.**
   - An AST-normalized diff shows only two real differences: the arm set and `_sha` in place of `hashlib`.
   - Differential test against m's `_campaign_state`/`campaign_ruling_problems` (extracted by AST, never imported), over 6,000 synthetic checkpoints × 9 rulings, arm names mapped: 54,000 ruling comparisons and 6,000 state comparisons, 0 mismatches. This covers the words, the order and the OLMo arms.
   - The `ruling_texts` body is identical to m's.
   - `TOTALS_RX` and `TOTALS_REDACTED` are m's.
3. **Refusal order and pause semantics hold**, apart from MAJOR-1's status and R5's equivalence.
   - The order is: report → marker → call log without `--resume` → call log unreadable → stopped runs → no run line → log consistency → checkpoint unreadable/ended → rulings → cap → schedules → prior.
   - A PAUSE leaves no marker and no report; a shown pause launches nothing; an ended campaign is refused.
   - p's report is written if and only if the checkpoint has ended with nothing pending.
4. **The values passed to m are right:** floors 80/32 from `schedule.FLOORS`, launch counts 96/64 contrast first, the cap, the unit's qualification checkpoint as prior, substrate olmo, the out root, the rulings as read, resume as given.
5. **G-PWR (p)'s record is bound correctly.** It is the committed blob, schema p-gpwr-v1, L A0 96 / A0s 64 for all three units, sha256 bc2b0909…d604, and the lock must name it.
   - A read-only probe of the real non-stub precheck at `campaign` gives exactly the expected refusals: the cap unset; G-SHAPE-p and G-ANL-p stale; the lock not naming the package, driver, licence line and G-PWR record; the lock lacking the launch-counts line (and, with a cap patched in, "hour cap = 4 h"); the two files uncommitted; POD ID ABSENT.
6. **The lock's line forms, the cap-unset refusal (in the precheck and the run) and all-None caps** are in place.

#### Mutants

Each mutant was a scratch file loaded as `valence_core.p.stage` with the real `__file__`, or as the driver module, in a fresh process. Stage mutants ran the stage and driver self-tests; driver mutants ran the driver's.

| id | change | result | survivor |
|---|---|---|---|
| S1 | `_fill_cause` under "time" | KILLED: ProxyStop-at-qual case | |
| S2 | STOP read from the exception only | SURVIVED | equivalent (predates change) |
| S3 | backend-identifier check dropped | SURVIVED | gap (predates change) |
| S4 | gate's m call passes `prior_ckpt=None` | KILLED: full G-F0m case (+5) | |
| R1 | p-report-exists refusal dropped | KILLED: full campaign case | |
| R2 | STOP-marker refusal dropped | SURVIVED | gap (masked by R3's guard) |
| R3 | stopped-run refusal dropped | SURVIVED | gap (masked by R2's guard) |
| R4 | call-log-without-resume refusal dropped | KILLED: pause case | |
| R5 | m-checkpoint-without-resume refusal dropped | SURVIVED | equivalent (still refused by another check) |
| R6 | unreadable checkpoint not refused | SURVIVED | gap |
| R7 | ended checkpoint not refused | KILLED: full campaign case | |
| R8 | rulings not checked before the load | SURVIVED | gap |
| R9 | dirty schedules not refused | SURVIVED | gap |
| R10 | prior checked at "qual" | KILLED: full campaign case | |
| R12 | call log checked under the qual label | KILLED: 3 campaign cases | |
| C1 | Q-F0 arms accepted | KILLED: campaign_state case | |
| C2 | CHECKPOINT MISMATCH unstripped | SURVIVED | gap |
| C3 | recorded PI stop beside pending refused | SURVIVED | gap |
| C4 | SCHEDULE EXHAUSTED beside the PI's stop | SURVIVED | gap |
| C5 | any last pause counted as open | KILLED (self-test raised) | |
| C6 | RULING REUSED checks the last pause only | KILLED (raised) | |
| C9 | no refusal beside an end pending | KILLED: ruling case | |
| T1 | byte-order mark kept | KILLED: ruling_texts case | |
| T2 | zero-width space counted as visible | KILLED (raised) | |
| T3 | ruling text stripped | KILLED: ruling_texts case | |
| V1 | floors passed as launch counts | KILLED: recorder case | |
| V2 | m always told resume | SURVIVED | equivalent (m reads resume only in `load_or_init`) |
| V3 | PI stop never passed to m | KILLED: PI-stop case | |
| V5 | dpo sham count 60 | KILLED: values case | |
| V6 | cap ≤ 0 accepted | SURVIVED | gap |
| G1 | G-PWR schema unchecked | SURVIVED | gap |
| G2 | sham L not read from the record | SURVIVED | gap |
| G3 | record sha not returned | SURVIVED | gap |
| L1 | substring test instead of whole line | KILLED: values case | |
| L3 | precheck's lock lines dropped | SURVIVED | gap |
| L4 | precheck's G-PWR problems dropped | SURVIVED | gap |
| B1 | pending not refused in `build_report` | SURVIVED | equivalent |
| B2 | every terminal recorded as COMPLETE | KILLED: PI-stop case | |
| B3 | report gated on m's returned status | SURVIVED | gap (MAJOR-1's case) |
| O1 | excerpt named beside m's report | KILLED: values case | |
| LB1 | non-unit campaign labelled "G-F0m" | SURVIVED | gap (cosmetic) |
| P1 | precheck cap refusal dropped | KILLED: precheck case | |
| D1 | `_say` unredacted | SURVIVED | gap |
| D2 | adjudication/PI stop swapped | SURVIVED | gap |
| D4 | RULING line prints the text | SURVIVED | gap |
| D5 | `campaign-report` uses "qual" | SURVIVED | gap |
| D6 | exit 0 always | SURVIVED | gap |
| D9 | refusals reported as STOP (exit 4) | SURVIVED | gap |

#### Disclosures

**Reads beyond the brief's list**
- More of `valence_core/m/stages.py`: constants, the path helpers, `_committed`, `gate_line`, `prior_gate`, `campaign_look`, `_show_pause`, `_campaign_report`, `_refinish_campaign`.
- More of `valence_core/m/resume.py`: TOTALS_SEALED, `load_or_init`, `refuse_ended`, `hour_cap_exceeded`, `_q`.
- `m/keys.templates` and the `schedule.FLOORS` line.
- The `except` lines in `m/runner_olmo.py` and `verify.py`.
- In `scripts/m_sessions.py` beyond the listed ranges: `stage_precheck`, `_run_stage`, `ruling_line`.
- The 2026-11-12 answers lines 30–60, the 2026-11-10 answers §0–§3, and PROPOSAL-m lines 192, 247, 251, 302, 316, 318 and 330.

**Data reads**
- `data/p/gates/G-PWR-p.json`: its keys, schema, L and looks; `shasum`, `git rev-parse HEAD:`, `git hash-object`.
- `n` and cell counts from `data/p/schedules/*campaign*.json`.
- Name-only `ls` of `data/p/schedules/` and `git ls-files data/p/gates/`.
- Nothing under the repository's `data/*/ckpt` or `data/*/reports` was opened, listed or searched.

**Searches and other commands**
- `/usr/bin/grep -rn` over `valence_core/p/` and `scripts/` (no data paths; it matched a `.pyc`), and greps of p's `.py` files.
- `ps` of my own harness PIDs.
- `git show HEAD:` of the two files into scratch.

**Runs**
- The real precheck(stub=False) at `campaign`, read-only: m's `_committed` git reads of committed non-data/ckpt files; the pod id absent from the environment.
- `git check-ignore -q` over 24 campaign paths, through a probe copy of the self-test (the stage self-test's own form; not on item 1's list; the paths do not exist).
- Three probe copies of the self-test: end look, `run_gate` at campaign, git check-ignore.
- p's full self-test once.
- No model was loaded, nothing was written in the repository, and no git state changed.

All harnesses, mutants, results and probe files are in <tmp>/scratchpad/campwire-review/ (mutant results are in its `mutants/` subfolder).

### Code's dispositions, round 1

- **MAJOR-1** (a fired end look at a terminal end, recorded as the terminal status): applied.
  - At the campaign, `build_report` records m's status for that end: PAUSE when the terminal campaign's last pause is
    an unadjudicated end_look, with `campaign_terminal` beside it.
  - The run returns PAUSE. Both the run and `campaign-report` therefore exit 3 (EXIT_CODES["PAUSE"]).
  - New case: the end look made to fire by a stand-in `campaign_look` at "end", on m's scripted double. Run PAUSE;
    p's report PAUSE, terminal COMPLETE; exit code 3; the later run refused.
- **MINOR-1** (`run_gate` no longer refused the campaign): applied. `run_gate` refuses any gate not in GATES before
  the precheck. New case: the factory is never called and no call log is written.
- **MINOR-2** (whole hours only): applied.
  - `campaign_hour_cap` takes a positive finite int or float, as m's `hour_cap_exceeded` does. A bool, zero, a
    negative, an infinity or a text reads as unset. The lock line is formatted from the same value.
  - Cases: 4, 4.5, 0, -1, True, inf, "4", None.
- **MINOR-3** (the driver's campaign path untested): applied.
  - The RULING line moved into the stage, after the campaign's own refusals: each ruling's sha16 and the campaign's
    last pause, never the text (NOTE-4 (b)'s order).
  - New driver case on a simulated clear box (recorder; stand-in precheck and weights; loader trapped; --resume; both
    ruling files):
    - the DRIVER then the WEIGHTS line;
    - the kwargs as read;
    - the precheck at the campaign;
    - exits 3 on PAUSE, 2 on a refusal, 4 on a STOP;
    - the totals redacted at the print;
    - no ruling text printed.
  - `campaign-report` joins the report-command loop. `gate_report`'s lines go through `_say` (NOTE-2).
- **MINOR-4** (the stage's refusals and the precheck's binding untested): applied.
  - New cases on a paused campaign, each refused before the factory is called: NO PAUSE TO ADJUDICATE, RULING REUSED,
    CHECKPOINT MISMATCH, an unreadable checkpoint, unclean schedules, a marker with no STOP line, and a STOP line with
    no marker. The last two keep R2 and R3 apart.
  - The three untested ruling branches (C2-C4) as synthetic cases.
  - The non-stub precheck at the campaign with sentinels: G-PWR's and the lock lines' problems among its refusals, and
    the lock required to name G-PWR (p)'s record.
  - `gpwr_problems` against a record of another schema and a sham count of 60.
- **NOTE-1**: applied. After a normal return, a state other than open or ended (unreadable, pending, absent) is a
  StageStop, never a silent end. The recorder case now shows it.
- **NOTE-2**: applied (`_say` in `gate_report`).
- **NOTE-3**: declared in THE CAMPAIGN PIN. There is no restart route after a box change: a --resume on another pod
  meets m's CHECKPOINT MISMATCH (the pod id) after the load, a STOP; m:302's restart is the seat's to route.
- **NOTE-4**:
  - (a), (c) and (d) are declared, for the BUILD entry and the seat.
  - (b) is applied: the RULING line now follows the refusals and names the campaign's last pause.
- **NOTE-5**: applied.
  - THE CALL LOG, P'S REPORT and `stage_lock` now name `campaign-report`.
  - The planted-exclusion sentence names the campaign's report as built by the same function.
  - `prior_problems`' docstring now covers the campaign's prior.
  - STAGE_NAMES is removed.
  - The git check-ignore case covers the campaign's outputs and m's three campaign files.
- **NOTE-6**: applied. A safe checkpoint reader keeps one early failure from skipping the rest.
- **NOTE-7**: S2 is equivalent; S3 is the gates' shared gap (the backend comparison never runs on the stub), noted as
  is.
- p's self-test: 201/201.

## Round 2

### Round 2 review: the campaign wiring (revised `valence_core/p/stage.py` and `scripts/p_sessions.py`)

**Bottom line:** no MAJOR finding this round. Three MINORs remain, all about ordering or untested paths, plus four NOTEs. 42 mutants: 30 killed, 12 survived (5 equivalent, 7 gaps). 21 of round 1's 23 gap survivors are now killed; S3 and LB1 still survive.

**What I reviewed**
- `valence_core/p/stage.py`, sha256 5ba046a0ad0a6651c8a3de7a7accdf2632a7429fb41b3f919be1ae9ed91d3173
- `scripts/p_sessions.py`, sha256 04da458d3e4ee585f51a8316b855f3ddf267b47247e047cc6ba38b61c0ab9fcd
- The baseline was HEAD 3e1b614. Both files hashed the same at the end of the review, and `git status` was unchanged.

**Baselines**
- `scripts/p_sessions.py --selftest`: 201/201.
- My harness (stage and driver self-tests): 71/71 (53 stage, 18 driver).

#### Where round 1's findings stand

- **MAJOR-1, MINOR-1, MINOR-2: closed and tested.**
  - N1 and N2 are killed (`build_report`'s PAUSE and `campaign_terminal`), and so is the adapted B3a.
  - N5 is killed (`run_gate` refusing the campaign).
  - V6a, N6 and N7 are killed (the cap's accepted forms).
  - I checked the end-look logic by reading it: PAUSE is recorded only where a terminal stands and the last pause is an unadjudicated `end_look`. A STOP keeps STOP, and a look pause adjudicated before a COMPLETE keeps COMPLETE. This matches m's `_campaign_end`.
- **MINOR-3: closed for the driver's campaign path.** D1, D2, D5, D6, D9 and N15 are killed, and the RULING-line text mutant (moved into the stage) is killed too. Two residuals remain: N12 and N13 (MINOR-C and NOTE-B below).
- **MINOR-4: closed.** R2, R3, R6, R8, R9, C2–C4, G1–G3, L3 and L4 are all killed now.
- **NOTE-2, NOTE-3 and NOTE-5:** applied.
- **NOTE-1 and NOTE-6:** partly closed; see NOTE-A and NOTE-C below.
- **NOTE-4 (b):** partly closed; see MINOR-A below.

#### Findings

**MINOR-A: the RULING line still prints before three of the campaign's own refusals.**
- **Where it sits.** The line follows the state and ruling refusals but comes before the cap, schedules and prior refusals.
- **What the docs say.** The driver docstring says "then the campaign's own refusals (its state, the rulings against it, the prior) and, after them, the stage's RULING line". `_run_campaign_locked`'s own docstring counts the cap, schedules and prior among "the campaign's own" refusals.
- **Probe.** In a scratch copy of the self-test: a paused campaign with one schedule file overwritten, offered an adjudication. The run printed "RULING campaign-OLMo-sft (p): the seat's adjudication (sha16 147ec625b8dd0637); the campaign's last pause: look at 40 launches, open", then was refused ("the schedules at schedules are not clean"). The factory was not called.
- **Not pinned.** N8, which moves the line before even the ruling refusals, survives. The refusal probe captures each run's output but never checks it.
- **Fix.** Print the line just before `_run_recorded`, after the prior check, where m's driver prints its RULING line, just before the load. Assert that no refused run in the refusal probe prints a RULING line.

**MINOR-B: no campaign case ends in m's own STOP.**
- p's report at an m STOP (a hair trigger, or G-VER) is untested, and so is the terminal guard the new code relies on. At a STOP, an end-look pause raised at the STOP point (C9(ii)) must leave the status STOP with no `campaign_terminal`.
- N3 (the terminal no longer required) survives. Under it, such a STOP would be recorded as PAUSE with `campaign_terminal` "STOP".
- The only STOP case in the self-test is p's proxy STOP, where m's stage raises and no m end is written.
- **Fix.** Add a campaign case where m's hair trigger fires on the scripted double, asserting p's report status STOP and no `campaign_terminal`. Add a second where the end look also fires at that STOP point, using the same `campaign_look` stand-in the end-look case uses.

**MINOR-C: `campaign-report`'s exit code for a written report is untested.**
- The dispositions say "the run and `campaign-report` therefore exit 3". The stage case checks only a computed `m_stages.EXIT_CODES[rep_e["status"]] == 3`. The driver's report-command loop exercises only the STOP and refusal exits.
- N13 (`gate_report` returns 0 for any written report) survives.
- **Fix.** In the driver test, run `campaign-report` over a scratch root holding an ended campaign, either a stand-in `stage.write_report` returning reports with status PAUSE and COMPLETE, or the end-look case's output. Assert exits 3 and 0.

**NOTE-A: the new post-run StageStop is recorded nowhere.**
- It is raised after `_run_recorded` returned, so it leaves no marker, and the end line carries m's status with no stop mark.
- Its message says "the seat adjudicates", but nothing enforces that. A later `--resume` re-finishes a "pending" checkpoint and starts afresh on an "absent" one; only "unreadable" is refused next time. With m's real stage, "pending" and "absent" cannot follow a normal return.
- N11 (an "unreadable" state after the run, read as a pause) survives. Only "absent", via the recorder, is tested.
- **Fix.** Do the state check inside the recorded run (wrap `call_m` so it checks after m returns), so THE STOP's machinery records it. Otherwise, word it as an unrecorded alert.

**NOTE-B: `gate_report`'s `_say` is untested.**
N12 survives. No totals line can arise on that path, so this is a guard only.

**NOTE-C: some new probes still abort the rest of the self-test on an early failure.**
- I re-applied round 1's R10 to the revised stage. The stage self-test fails, then raises KeyError('campaign'), so only 39 of 53 stage checks run.
- Remaining unconditional reads:
  - the pause case's detail tuple, `ck_p["campaign"]["pauses"][:1]`;
  - the refusal probe's `doctored` edits, `ppf["p_calls"].read_bytes()`, and `sorted((rcf / "schedules").glob("*.json"))[0]`.
- The driver's recorder reads `kw.get("pre", {}).get("gate")`, which raises when `pre` is None. N15 is caught by that raise, and only 13 of 18 driver checks run.
- These are still failures; only the count drops.

**NOTE-D: leftover text and cosmetics.**
- `REPORT_TEXT["campaign"]["form"]` still says "written once the campaign has ended (m's ended_status), never at a pause", while a PAUSE report is now written at a terminal end whose end look fired.
- THE CAMPAIGN PIN's "as m's hour_cap_exceeded takes it" overstates: m also takes str and Fraction, and p takes int or float only (the dispositions declare this).
- Beside an end pending, the RULING line names the last persisted pause, not m's "beside an end pending".
- `summary_lines` prints PAUSE without the terminal.
- LB1 survives: the non-unit campaign label, cosmetic.

#### Mutants

42 in all: round 1's 27 survivors (24 re-applied unchanged, 3 adapted) plus 15 new.
- The 3 adapted ones: V6a because the function was rewritten, B3a because the post-run gate was rewritten, and D4a because the RULING line moved from the driver into the stage.
- The pre-existing gap is S3. The equivalents are S2 and B1 (unchanged code, with reasons in round 1), plus R5, V2 and N4 (reasons in the table).

| id | change | origin | result | survivor |
|---|---|---|---|---|
| S2 | STOP read from the exception only | re-applied | SURVIVED | equivalent |
| S3 | backend-identifier check dropped | re-applied | SURVIVED | gap (pre-existing) |
| R2 | STOP-marker refusal dropped | re-applied | KILLED: refusal probe | |
| R3 | stopped-run refusal dropped | re-applied | KILLED: refusal probe | |
| R5 | m-checkpoint-without-resume refusal dropped | re-applied | SURVIVED | equivalent (still refused by another check) |
| R6 | unreadable checkpoint not refused | re-applied | KILLED: refusal probe | |
| R8 | rulings not checked before the load | re-applied | KILLED: refusal probe | |
| R9 | dirty schedules not refused | re-applied | KILLED: refusal probe | |
| C2 | CHECKPOINT MISMATCH unstripped | re-applied | KILLED: three-branch case | |
| C3 | recorded PI stop beside pending refused | re-applied | KILLED: three-branch case | |
| C4 | SCHEDULE EXHAUSTED beside the PI's stop | re-applied | KILLED: three-branch case | |
| V2 | m always told resume | re-applied | SURVIVED | equivalent (m reads resume only in `load_or_init`) |
| G1 | G-PWR schema unchecked | re-applied | KILLED: sentinel/G-PWR case | |
| G2 | sham L not read from the record | re-applied | KILLED: sentinel/G-PWR case | |
| G3 | record sha not returned | re-applied | KILLED: sentinel/G-PWR case | |
| L3 | precheck's lock lines dropped | re-applied | KILLED: sentinel case | |
| L4 | precheck's G-PWR problems dropped | re-applied | KILLED: sentinel case | |
| B1 | pending not refused in `build_report` | re-applied | SURVIVED | equivalent |
| LB1 | non-unit campaign labelled "G-F0m" | re-applied | SURVIVED | gap (cosmetic) |
| D1 | `_say` unredacted | re-applied | KILLED: driver clear-box case | |
| D2 | adjudication/PI stop swapped | re-applied | KILLED: driver clear-box case | |
| D5 | `campaign-report` uses "qual" | re-applied | KILLED: report-command loop | |
| D6 | exit 0 always | re-applied | KILLED: driver clear-box case | |
| D9 | refusals reported as STOP (exit 4) | re-applied | KILLED: driver clear-box case | |
| V6a | cap ≤ 0 accepted | adapted | KILLED: values case (caps table) | |
| B3a | report gated on m's returned status | adapted | KILLED: recorder case, end-look case | |
| D4a | RULING line prints the ruling's text | adapted | KILLED: pause case (RULING form, no text) | |
| N1 | end-look PAUSE override dropped | new | KILLED: end-look case | |
| N2 | `campaign_terminal` not recorded | new | KILLED: end-look case | |
| N3 | terminal not required for the PAUSE | new | SURVIVED | gap (MINOR-B) |
| N4 | `end_look` adjudication not checked | new | SURVIVED | equivalent (never adjudicated through stages) |
| N5 | `run_gate` refusal dropped | new | KILLED: run_gate case | |
| N6 | infinite cap accepted | new | KILLED: values case | |
| N7 | bool cap accepted | new | KILLED: values case | |
| N8 | RULING line before the ruling refusals | new | SURVIVED | gap (MINOR-A) |
| N9 | RULING line says open/adjudicated swapped | new | KILLED: pause case | |
| N10 | post-run StageStop dropped | new | KILLED: recorder case | |
| N11 | unreadable-after-run read as a pause | new | SURVIVED | gap (NOTE-A) |
| N12 | `gate_report` STOP line unredacted | new | SURVIVED | gap (NOTE-B) |
| N13 | `gate_report` exit 0 for a written report | new | SURVIVED | gap (MINOR-C) |
| N14 | adapter factory called before the refusals (aimed at the probes) | new | KILLED: proxy-STOP, no-prior/no-cap and refusal cases | |
| N15 | driver passes `pre=None` to the stage | new | KILLED: driver self-test raised AttributeError | |

#### Disclosures

**Reads**
- The dispositions file at <tmp>/scratchpad/campwire/dispositions_r1.md, plus a name-only `ls` of that folder.
- Snapshots of the two working-tree files, diffed against my round-1 copies.

**Runs**
- The harness baseline; 42 mutants, four at a time under `nice -n 10`; two probe copies of the stage self-test (the RULING order, and R10 re-applied); p's full self-test once; `git status`, `shasum`, `git rev-parse`.
- The revised self-tests themselves run the non-stub precheck at the campaign (git reads of committed files, the G-PWR record included, with a stand-in lock) and `git check-ignore -q` over the campaign's outputs. That is the self-test's own code.

**Not done**
- I opened, listed or searched nothing under the repository's `data/*/ckpt` or `data/*/reports`.
- No model was run, nothing was written in the repository, and no git state changed.

Everything is in <tmp>/scratchpad/campwire-review/r2/ (mutant results in its `mutants/` subfolder, probes as `probe_*.py` and `probe_*.json`).

### Code's dispositions, round 2

- **MINOR-A** (the RULING line printed before three refusals): applied.
  - The line now prints after every refusal, just before the recorded run, where m's driver prints it.
  - Beside an end pending it says so ("an end pending, which the stage re-finishes first").
  - The refusal probe asserts that no refused run prints a RULING line. Its unclean-schedules case now offers a
    fitting ruling, which is the reviewer's probe.
- **MINOR-B** (no campaign case ending in m's own STOP): applied. Two new cases with a G-VER failure (a record edited
  after the runner returns):
  - one plain;
  - one with the end look fired at the STOP point.
  - Both: status STOP, p's report STOP, no campaign_terminal, no p marker. The second records m's end_look pause.
- **MINOR-C** (campaign-report's exit for a written report): applied. A driver case with a stand-in report writer:
  exits 3 on PAUSE, 0 on COMPLETE, and 4 on a STOP whose totals are redacted at the print.
- **NOTE-A** (the post-run StageStop recorded nowhere): applied. The state check runs inside the recorded run
  (`call_m`), so THE STOP's machinery records it: a marker, and the end line's stop mark. The recorder case asserts the
  marker for an absent checkpoint (no write) and an unreadable one (garbage written).
- **NOTE-B**: covered by MINOR-C's STOP case (`_say` in gate_report).
- **NOTE-C**: applied. The pause case's detail, and the refusal probe's edits and reads, are guarded. The driver
  recorder reads `(kw.get("pre") or {})`.
- **NOTE-D**: applied.
  - REPORT_TEXT["campaign"]["form"] names the end-look PAUSE.
  - The PIN says p's cap is a number: m's hour_cap_exceeded also takes a text or a Fraction.
  - summary_lines prints the terminal beside a PAUSE.
  - The non-unit campaign label is asserted (LB1).
- p's self-test: 203/203.
- A final round follows the cap's change: the PI's cap share, then the BUILD.

## Round 3

### Round 3 review: the campaign wiring (revised `valence_core/p/stage.py` and `scripts/p_sessions.py`)

**Bottom line:** no MAJOR finding. One MINOR, a test gap only: the driver's exit codes for a STOP of m's own are untested at both commands. The code itself maps them correctly. Of round 2's seven gaps, six are now killed; only S3, which predates this change, still survives.

The cap of 2 reaches m's `run_campaign` as `hour_cap` for every unit, the precheck requires "hour cap = 2 h" as a whole line, and nothing else assumes an unset cap.

**What I reviewed**
- `valence_core/p/stage.py`, sha256 e81a25be9e257aad9fd7cc71919858bf50799a5103692e710cdd7e542812fb11
- `scripts/p_sessions.py`, sha256 f419091c12428b934b22e19aef4c23812c0c47d111cf47e7326f3fe4b3231286
- The baseline was HEAD 3e1b614. Both files hashed the same at the end of the review, and `git status` was unchanged.

**Baselines**
- `scripts/p_sessions.py --selftest`: 203/203.
- My harness (stage and driver self-tests): 73/73 (54 stage, 19 driver).

#### Round 2's survivors, re-derived

- **Killed:** N3, N8 (as N8a), N11 (as N11a), N12, N13 and LB1.
- **Still surviving:** S3 (it predates this change).
- **Adapted, because their code moved:**
  - N8a: the RULING line now sits after the prior check.
  - N11a: the post-run state check moved into `call_m`.

#### The three checks you asked for

1. **The cap value reaches m.** In a probe copy of the self-test I replaced m's `run_campaign` with a recorder and ran p's `run_campaign` for each unit with the shipped cap, no stand-in. Every unit received `hour_cap` 2 (int). The recorder writes no checkpoint, so the new in-run check then STOPs, as designed.
2. **The precheck requires "hour cap = 2 h".** A read-only probe of the real non-stub precheck at `campaign` shows the same for all three units: the cap-unset refusal is gone, and the refusals name "the campaign's line 'hour cap = 2 h' is not a whole line of the lock", the launch-count line, and the lock not naming G-PWR (p)'s record. All three are expected until LOCK-p v1.0 exists. The self-test also asserts the caps of record and their lines.
3. **Nothing else assumes an unset cap.**
   - `CAMPAIGN_HOUR_CAP` and `campaign_hour_cap` are used only in `stage.py` (17 sites), and every use is consistent with a set cap.
   - No other p module, nor the driver, `p_analyze.py` or `p_gpwr.py`, reads the cap.
   - The unset path is now exercised only through explicit `hour_cap(None)` cases in the self-test.
   - G-PWR (p)'s committed record still says the cap share is "not set"; that is its historical text and needs no change.

#### Findings

**MINOR-1: the driver's exit for a STOP of m's own is untested at both commands.**
- When m's stage returns STOP normally (and p writes its report), both commands should exit 4. Neither case is tested:
  - `campaign`'s clear-box recorder only returns PAUSE; its STOP mode raises an exception instead.
  - `campaign-report`'s stand-in covers PAUSE, COMPLETE and a raised STOP, but not a written STOP report.
- Two mutants survive: N22 (`campaign-report` exits 0 for a written STOP report) and N26 (`campaign` exits 0 for a returned STOP).
- The code is right (`EXIT_CODES["STOP"]` is 4); only the escalation path is unpinned.
- **Fix.** Add returned STOP and terminal results to the recorder (exits 4 and 0), and a written STOP report to the stand-in (exit 4).

**NOTE-1: the RULING line's end-pending wording is untested** (N17 survives). The only ruling that reaches that line beside an end pending is the PI's stop, offered again with the recorded text.

**NOTE-2: N25 is equivalent at the caps of record.** All three caps are 2, so a mutant that passes sft's cap to every unit cannot be told apart. The self-test's campaign runs use OLMo-sft only. If the caps ever differ per unit, add a per-unit case.

**NOTE-3: one docstring was missed.** `campaign_hour_cap`'s docstring still says "as m's hour_cap_exceeded takes it". The PIN now says p's cap is a number; the function docstring was not updated.

**NOTE-4 (forward, for LOCK-p v1.0):**
- p's code has no lock generator. v1.0 must carry "launch counts = A0-OLMo-{ckpt} 96, A0s-OLMo-{ckpt} 64" and "hour cap = 2 h" bare, as whole lines; a backticked line fails `campaign_lock_problems`.
- v1.0 must also name G-PWR (p)'s record sha256 (bc2b0909…d604).
- The cap edit changes p's package and driver hashes, so the G-SHAPE-p and G-ANL-p re-runs and v1.0 must follow the final code.

**What holds from round 2's dispositions**
- MINOR-A (the RULING line's place): N8a and N16 are killed. The line prints after the prior check, and the refusal probe asserts no RULING line on any refused run.
- MINOR-B (no m-STOP case): N3 and N21 are killed by the two G-VER STOP cases (status STOP, no `campaign_terminal`, no p marker). N21 was also killed by a gate case.
- MINOR-C (`campaign-report`'s exit): N12 and N13 are killed.
- NOTE-A (the post-run STOP recorded nowhere): N18, N19, N20 and N11a are killed. The in-run check now writes the marker for an absent or an unreadable checkpoint.
- NOTE-C: no mutant made the self-test raise this round.
- NOTE-D: applied, apart from NOTE-3 above.

#### Mutants

18 in all: 13 killed, 5 survived (1 equivalent, 4 gaps). That is the 17 you asked for plus N26, which I added to check MINOR-1 at the `campaign` command.

| id | change | origin | result | survivor |
|---|---|---|---|---|
| S3 | backend-identifier check dropped | re-applied | SURVIVED | gap (predates the change; shared with the gates) |
| LB1 | non-unit campaign labelled "G-F0m" | re-applied | KILLED: values case | |
| N3 | terminal not required for the PAUSE | re-applied | KILLED: m-STOP (G-VER) case | |
| N8a | RULING line before the ruling refusals | adapted | KILLED: refusal probe (no RULING line on a refused run) | |
| N11a | in-run check lets an unreadable checkpoint through | adapted | KILLED: recorder case (marker) | |
| N12 | `gate_report` STOP line unredacted | re-applied | KILLED: campaign-report exit case | |
| N13 | `gate_report` exit 0 for any written report | re-applied | KILLED: campaign-report exit case | |
| N16 | RULING line back at round 2's place | new | KILLED: refusal probe (unclean schedules) | |
| N17 | end-pending wording dropped | new | SURVIVED | gap |
| N18 | in-run state check dropped | new | KILLED: recorder case | |
| N19 | in-run check raises a non-SystemExit (no marker) | new | KILLED: recorder case | |
| N20 | absent checkpoint let through | new | KILLED: recorder case | |
| N21 | m's own STOP given a p marker | new | KILLED: G-F0m STOP case, m-STOP case | |
| N22 | `campaign-report`: written STOP report exits 0 | new | SURVIVED | gap (MINOR-1) |
| N23 | dpo cap 3 h | new | KILLED: caps-of-record check | |
| N24 | cap line written as "2.0 h" | new | KILLED: values case | |
| N25 | every unit passed sft's cap | new | SURVIVED | equivalent at the caps of record |
| N26 | `campaign`: returned STOP exits 0 | new (extra) | SURVIVED | gap (MINOR-1) |

#### Disclosures

**Reads**
- The dispositions file at <tmp>/scratchpad/campwire/dispositions_r2.md.
- Snapshots of the two files, diffed against round 2.
- `/usr/bin/grep` for the cap's uses over `valence_core/p/*.py`, `scripts/p_sessions.py`, `scripts/p_analyze.py` and `scripts/p_gpwr.py` (no data paths), and a name-only `ls scripts`.

**Runs**
- The harness baseline and 18 mutants (four at a time, under `nice -n 10`).
- One probe copy of the self-test (cap flow per unit: m's stage replaced by a recorder, p's prior check stubbed, temp roots).
- A read-only probe of the real non-stub precheck at `campaign` (git reads of committed files; the pod id removed from the environment).
- p's full self-test once; `git status`, `shasum`, `git rev-parse`.

**Not done**
- I opened, listed or searched nothing under the repository's `data/*/ckpt` or `data/*/reports`.
- No model was run, nothing was written in the repository, and no git state changed.

Everything is in <tmp>/scratchpad/campwire-review/r3/ (mutant results in its `mutants/` subfolder, the probes as `probe_*`).

### Code's dispositions, round 3

- **MINOR-1** (the driver's exit for a STOP of m's own, untested at both commands): applied, tests only.
  - `campaign`'s clear-box recorder gains two returned ends, each with p's report written: a STOP (exit 4) and a
    COMPLETE (exit 0); p's report's lines printed through a stand-in.
  - `campaign-report`'s stand-in writer gains a written STOP report (exit 4), beside the raised STOP.
- **NOTE-1** (the RULING line's end-pending wording untested): applied. A new stage case on the refusal probe's root:
  the checkpoint doctored to carry an end pending and the PI's recorded stop, the same stop offered again, the
  recorded run stood in for. The line prints the stop's sha16 and "the campaign carries an end pending, which the
  stage re-finishes first", and the factory is never called.
- **NOTE-2** (N25, equivalent at the caps of record): recorded. The three caps are equal, so no case can tell a unit's
  cap from sft's. A per-unit case is added if the caps ever differ.
- **NOTE-3** (`campaign_hour_cap`'s docstring): applied, worded as THE CAMPAIGN PIN words it.
- **NOTE-4** (forward, for LOCK-p v1.0): taken up there. Each v1.0 carries the two campaign lines as bare whole lines
  and names G-PWR (p)'s record by its sha256, and v1.0 follows the final code and the two re-runs.
- Checked by tool, not by a fourth blind round:
  - p's self-test: 204/204.
  - The reviewer's harness over the final files: 74/74 (55 stage, 19 driver).
  - The three new gap survivors, re-derived on the final files and run through the reviewer's harness: N17 fails
    the new end-pending case, N22 the campaign-report exit case, and N26 the clear-box case. All three are killed.
  - S3 is unchanged: the gates' shared gap, declared in the BUILD entry.
- Code's own citation sweep after round 3, before the values-check:
  - The hour cap was cited to m:251, which is the pod-sessions paragraph. It is now cited to m:249 ("Hour caps:
    wall-clock of detached generation time, set by the PI in that unit's LOCK v1.0"), at both sites: the constants'
    PIN and `campaign_hour_cap`'s docstring.
  - THE CAMPAIGN PIN's quote of §4.3 item 2 began "the campaign wiring, p's own move", where the source reads
    "**The campaign wiring**, p's own move". The quote now begins at "p's own move", which is byte-exact.
  - The driver's docstring listed the refusals before the RULING line as "its state, the rulings against it, the
    prior". It now names the cap and the schedules as well, and says the line prints just before the load.
  - One docstring line, P'S REPORT's, is reflowed.
  - All four are text only. The checks were re-run on the final files: p's self-test 204/204; the analyzer's self-test
    525/525, then 14/14; the gates' regression byte-identical; the harness 74/74, with N17, N22 and N26 each killed.
